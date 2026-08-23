/* ============================================================
   Tri-County Archers — rendering + interaction
   Reads everything from data.js. Nothing here needs editing to
   update the schedule.
   ============================================================ */
(function () {
  'use strict';

  /* ---------- date helpers ---------- */
  var MON = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  var DAY = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

  function parse(iso) {
    var p = iso.split('-');
    return new Date(+p[0], +p[1] - 1, +p[2]);
  }
  function fmtLong(iso) {
    var d = parse(iso);
    return DAY[d.getDay()] + ', ' + MON[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear();
  }
  function fmtShort(iso) {
    var d = parse(iso);
    return MON[d.getMonth()].slice(0, 3) + ' ' + d.getDate();
  }
  function fmtMid(iso) {
    var d = parse(iso);
    return DAY[d.getDay()].slice(0, 3) + ' · ' + MON[d.getMonth()].slice(0, 3) + ' ' + d.getDate() + ', ' + d.getFullYear();
  }
  /* "Feb 13 – 14" for a two-day event, "Feb 13" for one day */
  function fmtSpan(e) {
    if (!e.end) return fmtShort(e.date);
    var a = parse(e.date), b = parse(e.end);
    return a.getMonth() === b.getMonth()
      ? MON[a.getMonth()].slice(0, 3) + ' ' + a.getDate() + ' – ' + b.getDate()
      : fmtShort(e.date) + ' – ' + fmtShort(e.end);
  }
  function fmtSpanMid(e) {
    if (!e.end) return fmtMid(e.date);
    var a = parse(e.date), b = parse(e.end);
    return DAY[a.getDay()].slice(0, 3) + '–' + DAY[b.getDay()].slice(0, 3) + ' · '
         + MON[a.getMonth()].slice(0, 3) + ' ' + a.getDate() + '–' + b.getDate() + ', ' + b.getFullYear();
  }
  /* "February 13-14, 2027" / "February 6, 2027" - for dates quoted in copy */
  function fmtSpanLong(e) {
    var a = parse(e.date);
    if (!e.end) return MON[a.getMonth()] + ' ' + a.getDate() + ', ' + a.getFullYear();
    var b = parse(e.end);
    return a.getMonth() === b.getMonth()
      ? MON[a.getMonth()] + ' ' + a.getDate() + '\u2013' + b.getDate() + ', ' + b.getFullYear()
      : MON[a.getMonth()] + ' ' + a.getDate() + ' \u2013 ' + MON[b.getMonth()] + ' ' + b.getDate() + ', ' + b.getFullYear();
  }
  function fmtMonthDay(e) {
    var a = parse(e.date);
    return MON[a.getMonth()] + ' ' + a.getDate();
  }

  function today() {
    var n = new Date();
    return new Date(n.getFullYear(), n.getMonth(), n.getDate());
  }
  function daysOut(iso) {
    return Math.round((parse(iso) - today()) / 86400000);
  }
  function addWeeks(iso, w) {
    var d = parse(iso);
    d.setDate(d.getDate() + w * 7);
    return d;
  }
  function countdown(iso) {
    var d = daysOut(iso);
    if (d < 0) return '';
    if (d === 0) return 'Today';
    if (d === 1) return 'Tomorrow';
    if (d < 7) return 'In ' + d + ' days';
    if (d < 14) return 'Next week';
    if (d < 70) return 'In ' + Math.round(d / 7) + ' weeks';
    return 'In ' + Math.round(d / 30) + ' months';
  }

  /* ---------- add-to-calendar and maps links ---------- */
  function pad(n) { return String(n).padStart(2, '0'); }

  /* All-day events: DTEND / the second date is exclusive, so it's the day
     after the last day of the event. */
  function exclusiveEnd(e) {
    var d = parse(e.end || e.date);
    d.setDate(d.getDate() + 1);
    return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate());
  }
  function parseRegTimeRange(reg) {
    if (!reg || typeof reg !== 'string') return null;
    var m = reg.match(/(\d{1,2})(?::(\d{2}))?\s*(am|pm)\s*(?:\u2013|\u2014|-|to)\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)/i);
    if (!m) return null;

    function to24(h, ampm) {
      var hh = h % 12;
      return ampm.toLowerCase() === 'pm' ? hh + 12 : hh;
    }

    return {
      sh: to24(+m[1], m[3]),
      sm: m[2] ? +m[2] : 0,
      eh: to24(+m[4], m[6]),
      em: m[5] ? +m[5] : 0
    };
  }
  function gcalDateTime(iso, h, m) {
    var d = parse(iso);
    return d.getFullYear()
      + pad(d.getMonth() + 1)
      + pad(d.getDate())
      + 'T'
      + pad(h)
      + pad(m)
      + '00';
  }
  function gcalUrl(e) {
    var t = !e.end ? parseRegTimeRange(e.reg) : null;
    var dates = t
      ? gcalDateTime(e.date, t.sh, t.sm) + '/' + gcalDateTime(e.date, t.eh, t.em)
      : e.date.replace(/-/g, '') + '/' + exclusiveEnd(e);
    var q = 'action=TEMPLATE'
      + '&text=' + encodeURIComponent(e.name + ' — Tri-County Archers')
      + '&dates=' + dates
      + '&details=' + encodeURIComponent(
          (e.reg && e.reg !== '—' ? e.reg + '\n' : '')
          + (e.fees && e.fees !== '—' ? e.fees + '\n\n' : '\n')
          + e.detail)
      + '&location=' + encodeURIComponent(CLUB.address);
    return 'https://calendar.google.com/calendar/render?' + q;
  }
  function icsEscape(s) {
    return String(s || '')
      .replace(/\\/g, '\\\\')
      .replace(/\n/g, '\\n')
      .replace(/,/g, '\\,')
      .replace(/;/g, '\\;');
  }
  function eventIcsUrl(e) {
    var start = e.date.replace(/-/g, '');
    var end = exclusiveEnd(e);
    var t = !e.end ? parseRegTimeRange(e.reg) : null;
    var stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d{3}Z$/, 'Z');
    var uid = 'tca-' + start + '-' + icsEscape(e.name).replace(/[^a-zA-Z0-9]+/g, '-').toLowerCase() + '@tricountyarchers';
    var dtstart = t
      ? 'DTSTART:' + gcalDateTime(e.date, t.sh, t.sm)
      : 'DTSTART;VALUE=DATE:' + start;
    var dtend = t
      ? 'DTEND:' + gcalDateTime(e.date, t.eh, t.em)
      : 'DTEND;VALUE=DATE:' + end;
    var lines = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//Tri-County Archers//Event//EN',
      'CALSCALE:GREGORIAN',
      'METHOD:PUBLISH',
      'BEGIN:VEVENT',
      'UID:' + uid,
      'DTSTAMP:' + stamp,
      dtstart,
      dtend,
      'SUMMARY:' + icsEscape(e.name + ' — Tri-County Archers'),
      'DESCRIPTION:' + icsEscape((e.reg && e.reg !== '—' ? e.reg + '\n' : '')
                    + (e.fees && e.fees !== '—' ? e.fees + '\n\n' : '\n')
                    + e.detail),
      'LOCATION:' + icsEscape(CLUB.address),
      'END:VEVENT',
      'END:VCALENDAR'
    ];
    return 'data:text/calendar;charset=utf-8,' + encodeURIComponent(lines.join('\r\n'));
  }
  function mapsUrl() {
    return 'https://www.google.com/maps/dir/?api=1&destination='
      + encodeURIComponent(CLUB.address);
  }

  /* ---------- number formatting ---------- */
  function fmtAvg(n) {
    if (typeof n !== 'number') return n;
    return String(Math.round(n * 100) / 100);
  }
  function fmtNum(n) {
    if (typeof n !== 'number') return n;
    return n.toLocaleString('en-US');
  }
  function place(i) {
    return ['1st', '2nd', '3rd'][i] || (i + 1) + 'th';
  }

  /* ---------- shared bits ---------- */
  function whoBadge(who) {
    return who === 'public'
      ? '<span class="badge b-public">Open to the public</span>'
      : '<span class="badge b-members">Members</span>';
  }
  function catBadge(cat) {
    var m = { '3D': 'b-3d', 'Indoor': 'b-indoor', 'League': 'b-league', 'Work': 'b-social', 'Meeting': 'b-league', 'Social': 'b-social' };
    return '<span class="badge ' + (m[cat] || 'b-league') + '">' + cat + '</span>';
  }
  /* Yellow tags so nothing on the page is silently invented. */
  function tags(o) {
    var out = '';
    if (o.guess)  out += ' <span class="tbd" title="Placeholder — needs the club\'s real value">guess</span>';
    if (o.verify) out += ' <span class="tbd" title="Real date from the club, but it does not match the stated rule — needs one more check">verify date</span>';
    if (o.tag)    out += ' <span class="tbd">' + o.tag + '</span>';
    return out;
  }
  function upcoming() {
    return EVENTS.filter(function (e) { return daysOut(e.end || e.date) >= 0; })
                 .sort(function (a, b) { return a.date < b.date ? -1 : 1; });
  }

  /* ---------- alert strip ---------- */
  function renderAlert() {
    var el = document.getElementById('alert');
    if (!el || !CLUB.alert || !CLUB.alert.text) return;
    el.className = 'alert' + (CLUB.alert.tone === 'ok' ? ' alert-ok' : '');
    el.innerHTML = '<div class="wrap">' + CLUB.alert.text + '</div>';
  }

  /* The league card is the one that needs thinking about: because members
     can shoot their score any day of the week, what matters is which week
     of the season we're in, not which night it is. */
  function leagueCard() {
    var running = null, next = null;
    LEAGUES.forEach(function (l) {
      var d0 = daysOut(l.start);
      var week = Math.floor(-d0 / 7) + 1;
      if (d0 <= 0 && week <= l.weeks) { running = { l: l, week: week }; }
      else if (d0 > 0 && (!next || daysOut(next.start) > d0)) { next = l; }
    });

    if (running) {
      var l = running.l;
      return '<div class="nu">'
        + '<div class="nu-label">League — running now</div>'
        + '<div class="nu-title">' + l.name + '</div>'
        + '<div class="nu-date">Week ' + running.week + ' of ' + l.weeks + tags({ verify: l.verify }) + '</div>'
        + '<div class="nu-meta">'
        +   '<div><strong>Round:</strong> ' + l.round + '</div>'
        +   '<div><strong>Shooting:</strong> ' + l.time + '</div>'
        + '</div>'
        + '<div class="nu-foot">' + whoBadge('members') + '</div></div>';
    }
    if (next) {
      return '<div class="nu">'
        + '<div class="nu-label">Next League</div>'
        + '<div class="nu-title">' + next.name + '</div>'
        + '<div class="nu-date">' + fmtMid(next.start) + ' &nbsp;<span class="muted small">'
        +   countdown(next.start) + '</span>' + tags({ verify: next.verify }) + '</div>'
        + '<div class="nu-meta">'
        +   '<div><strong>Length:</strong> ' + next.weeks + ' weeks</div>'
        +   '<div><strong>Entry:</strong> ' + next.cost + '</div>'
        + '</div>'
        + '<div class="nu-foot">' + whoBadge('members')
        +   ' <a class="nu-cal" target="_blank" rel="noopener" href="'
        +   gcalUrl({ date: next.start, name: next.name + ' — Week 1',
                      reg: next.night, fees: next.cost, detail: next.round + ' ' + next.time })
        +   '" title="Add week 1 to Google Calendar">+ Calendar</a></div></div>';
    }
    return '<div class="nu"><div class="nu-label">Leagues</div>'
      + '<div class="nu-title">Between seasons</div>'
      + '<p class="nu-meta">Indoor league starts the first Thursday in January; outdoor 3D league in the summer.</p></div>';
  }

  function renderNextUp() {
    var el = document.getElementById('nextup');
    if (!el) return;
    var up = upcoming();
    var pick = function (fn) { for (var i = 0; i < up.length; i++) if (fn(up[i])) return up[i]; return null; };

    var cards = [
      { label: 'Next Shoot',           cls: 'nu-blaze', ev: pick(function (e) { return e.type === 'shoot'; }) },
      { league: true },
      { label: 'Next Monthly Meeting', cls: 'nu-brown', ev: pick(function (e) { return e.type === 'meeting'; }) },
      { label: 'Coming Up',            cls: 'nu-brown', ev: pick(function (e) { return e.type === 'social'; }) }
    ];

    el.innerHTML = cards.map(function (c) {
      if (c.league) return leagueCard();
      if (!c.ev) {
        return '<div class="nu ' + c.cls + '"><div class="nu-label">' + c.label + '</div>'
             + '<div class="nu-title">Nothing scheduled yet</div>'
             + '<p class="nu-meta">Watch the schedule page — dates go up as the club sets them.</p></div>';
      }
      var e = c.ev;
      return '<div class="nu ' + c.cls + '">'
        + '<div class="nu-label">' + c.label + '</div>'
        + '<div class="nu-title">' + e.name + '</div>'
        + '<div class="nu-date">' + fmtSpanMid(e) + ' &nbsp;<span class="muted small">' + countdown(e.date) + '</span>'
        +   tags({ verify: e.verify }) + '</div>'
        + '<div class="nu-meta">'
        +   '<div><strong>' + (e.type === 'meeting' || e.type === 'work' ? 'Time' : 'Hours') + ':</strong> ' + e.reg + '</div>'
        +   (e.fees !== '—' ? '<div><strong>Cost:</strong> ' + e.fees + '</div>' : '')
        + '</div>'
        + '<div class="nu-foot">' + whoBadge(e.who)
        +   ' <a class="nu-cal" target="_blank" rel="noopener" href="' + gcalUrl(e)
        +   '" title="Add to Google Calendar">+ Calendar</a></div>'
        + '</div>';
    }).join('');
  }

  /* ---------- schedule page ---------- */
  function renderSchedule() {
    var body = document.getElementById('sched-body');
    if (!body) return;

    var all = EVENTS.slice().sort(function (a, b) { return a.date < b.date ? -1 : 1; });
    var filter = 'all';

    function draw() {
      var rows = all.filter(function (e) {
        if (filter === 'all') return true;
        if (filter === 'public') return e.who === 'public';
        if (filter === 'members') return e.who === 'members';
        return e.cat === filter;
      });
      rows = rows.filter(function (e) { return daysOut(e.end || e.date) >= 0; });

      if (!rows.length) {
        body.innerHTML = '<tr><td colspan="4">Nothing on the calendar matches that filter yet.</td></tr>';
        return;
      }
      body.innerHTML = rows.map(function (e) {
        var d = parse(e.date);
        var slug = (e.name + '-' + e.date).toLowerCase().replace(/[^a-z0-9]+/g, '-');
        var icsHref = eventIcsUrl(e);
        var dayLine = e.end
          ? DAY[d.getDay()].slice(0, 3) + '–' + DAY[parse(e.end).getDay()].slice(0, 3) + ' ' + d.getFullYear()
          : DAY[d.getDay()] + ' ' + d.getFullYear();
        return '<tr>'
          + '<td data-l="Date"><strong>' + fmtSpan(e) + '</strong><br><span class="small muted">' + dayLine + '</span>'
          + '<div class="cal-cell-action"><details class="cal-menu">'
          + '<summary class="btn btn-forest btn-sm cal-icon-btn" aria-label="Add to calendar" title="Add to calendar">'
          +   '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          +     '<rect x="3" y="4" width="18" height="17" rx="2"></rect>'
          +     '<line x1="8" y1="2.5" x2="8" y2="6"></line>'
          +     '<line x1="16" y1="2.5" x2="16" y2="6"></line>'
          +     '<line x1="3" y1="9" x2="21" y2="9"></line>'
          +   '</svg>'
          + '</summary>'
          + '<div class="cal-pop">'
          +   '<a target="_blank" rel="noopener" href="' + gcalUrl(e) + '">Google Calendar</a>'
          +   '<a href="' + icsHref + '">Apple / Outlook (.ics)</a>'
          +   '<a href="' + icsHref + '" download="tri-county-archers-' + slug + '.ics">Download .ics</a>'
          + '</div>'
          + '</details></div></td>'
          + '<td data-l="Event"><span class="ev-name">' + e.name + '</span>' + tags(e)
          +   '<div class="small muted" style="margin-top:4px">' + e.detail + '</div>'
          +   '<div style="margin-top:8px; display:flex; gap:6px; flex-wrap:wrap">' + whoBadge(e.who) + catBadge(e.cat) + '</div></td>'
          + '<td data-l="Hours">' + e.reg + '</td>'
          + '<td data-l="Cost">' + e.fees + '</td>'
          + '</tr>';
      }).join('');
    }

    var chips = document.querySelectorAll('#sched-filters .chip');
    Array.prototype.forEach.call(chips, function (c) {
      c.addEventListener('click', function () {
        Array.prototype.forEach.call(chips, function (x) { x.classList.remove('on'); });
        c.classList.add('on');
        filter = c.getAttribute('data-f');
        draw();
      });
    });
    draw();
  }

  /* ---------- leagues page ---------- */
  function renderLeagues() {
    var el = document.getElementById('leagues');
    if (!el) return;
    el.innerHTML = LEAGUES.map(function (l) {
      var last = addWeeks(l.start, l.weeks - 1);
      var span = fmtLong(l.start) + ' through the week of '
               + MON[last.getMonth()] + ' ' + last.getDate() + ', ' + last.getFullYear();
      return '<div class="lg">'
        + '<div class="lg-top"><div class="night">' + l.night + (l.indoor ? ' · Indoor' : ' · Outdoor')
        +   tags({ tag: l.nightTag }) + '</div>'
        +   '<h3>' + l.name + '</h3></div>'
        + '<div class="lg-body">'
        +   '<dl class="dl">'
        +     '<div><dt>Round</dt><dd>' + l.round + '</dd></div>'
        +     '<div><dt>Entry</dt><dd><strong>' + l.cost + '</strong></dd></div>'
        +     '<div><dt>Length</dt><dd>' + l.weeks + ' weeks</dd></div>'
        +     '<div><dt>Season</dt><dd>' + span + tags({ verify: l.verify }) + '</dd></div>'
        +     '<div><dt>Shooting</dt><dd>' + l.time + '</dd></div>'
        +     '<div><dt>Who</dt><dd>' + l.who + '</dd></div>'
        +     '<div><dt>Contact</dt><dd>' + l.coord + tags({ tag: l.coordTag }) + '</dd></div>'
        +   '</dl>'
        +   '<p class="small muted" style="margin:0">' + l.note + '</p>'
        + '</div></div>';
    }).join('');
  }

  /* ---------- standings (on the Leagues page) ---------- */
  /* Two shapes: the outdoor league is shot in two-archer teams and decided on
     total points; the indoor league is individual. Both come from RESULTS. */
  function standingsHead(r) {
    return '<div class="sec-head" style="margin-bottom:14px">'
      + '<h3 style="margin-bottom:6px">' + r.title + ' &middot; ' + r.season + '</h3>'
      + '<p style="margin-bottom:0">' + r.status + tags({ tag: r.scoringTag }) + '</p>'
      + '</div>';
  }

  function weekCols(n) {
    var out = '';
    for (var w = 1; w <= n; w++) out += '<th class="num">' + w + '</th>';
    return out;
  }
  function scoreCells(scores) {
    return scores.map(function (sc) {
      return typeof sc === 'number'
        ? '<td class="num">' + sc + '</td>'
        : '<td class="num muted">' + sc + '</td>';
    }).join('');
  }

  function teamStandings(r) {
    /* Ranked on total points, which is what decides the league. The average
       column is context — it can order teams differently when somebody has
       missed weeks, so total leads and average follows. */
    var summary = '<div class="tbl-wrap" style="margin-bottom:18px">'
      + '<table class="t stack"><thead><tr>'
      + '<th>Place</th><th>Team</th><th>Archers</th>'
      + '<th class="num">Total points</th><th class="num">Average</th>'
      + '</tr></thead><tbody>'
      + r.teams.map(function (t, i) {
          return '<tr class="rank' + (i + 1) + '">'
            + '<td data-l="Place">' + place(i) + '</td>'
            + '<td data-l="Team"><strong>Team ' + t.team + '</strong></td>'
            + '<td data-l="Archers">' + t.archers.map(function (a) { return a.name; }).join(' &amp; ') + '</td>'
            + '<td data-l="Total points" class="num tot">' + fmtNum(t.total) + '</td>'
            + '<td data-l="Average" class="num">' + fmtAvg(t.avg) + '</td>'
            + '</tr>';
        }).join('')
      + '</tbody></table></div>';

    var detail = '<details class="wk"><summary>Week-by-week scores</summary>'
      + '<div class="tbl-wrap"><table class="t"><thead><tr>'
      + '<th>Team</th><th>Archer</th>' + weekCols(r.weeks)
      + '<th class="num">Total</th><th class="num">Avg</th>'
      + '</tr></thead><tbody>'
      + r.teams.map(function (t) {
          return t.archers.map(function (a, j) {
            return '<tr>'
              + (j === 0 ? '<td rowspan="' + t.archers.length + '"><strong>' + t.team + '</strong></td>' : '')
              + '<td>' + a.name + '</td>'
              + scoreCells(a.scores)
              + '<td class="num tot">' + fmtNum(a.total) + '</td>'
              + '<td class="num">' + fmtAvg(a.avg) + '</td>'
              + '</tr>';
          }).join('');
        }).join('')
      + '</tbody></table></div>'
      + '<p class="small muted" style="margin:10px 0 0"><strong>X</strong> means that week wasn\'t shot. '
      + 'An archer\'s average counts only the weeks they shot, so a team can sit higher on average than '
      + 'on total. The league goes on total.</p>'
      + '</details>';

    return summary
      + (r.decidedBy ? '<p class="small muted" style="margin:0 0 14px"><strong>' + r.decidedBy + '</strong></p>' : '')
      + detail;
  }

  function individualStandings(r) {
    if (!r.rows || !r.rows.length) {
      return '<div class="note" style="margin:0">' + (r.empty || 'Scores go up here through the season.') + '</div>';
    }
    return '<div class="tbl-wrap"><table class="t"><thead><tr>'
      + '<th>Place</th><th>Archer</th>' + weekCols(r.weeks)
      + '<th class="num">Total</th><th class="num">Avg</th>'
      + '</tr></thead><tbody>'
      + r.rows.map(function (a, i) {
          return '<tr class="rank' + (i + 1) + '">'
            + '<td>' + place(i) + '</td><td>' + a.name + '</td>'
            + scoreCells(a.scores)
            + '<td class="num tot">' + fmtNum(a.total) + '</td>'
            + '<td class="num">' + fmtAvg(a.avg) + '</td>'
            + '</tr>';
        }).join('')
      + '</tbody></table></div>';
  }

  function renderResults() {
    var el = document.getElementById('results');
    if (!el) return;
    el.innerHTML = Object.keys(RESULTS).map(function (k) {
      var r = RESULTS[k];
      return '<section id="' + k + '" style="margin-bottom:46px">'
        + standingsHead(r)
        + (r.format === 'team' ? teamStandings(r) : individualStandings(r))
        + '</section>';
    }).join('');

    var sr = document.getElementById('shoot-results');
    if (sr) {
      sr.innerHTML = SHOOT_RESULTS.length
        ? SHOOT_RESULTS.map(function (sh) {
            return '<tr>'
              + '<td data-l="Date"><strong>' + fmtShort(sh.date) + '</strong> ' + parse(sh.date).getFullYear() + '</td>'
              + '<td data-l="Shoot"><span class="ev-name">' + sh.name + '</span>' + tags(sh)
              +   '<div class="small muted">' + sh.note + '</div></td>'
              + '<td data-l="Entries" class="num">' + sh.entries + '</td>'
              + '<td data-l="Results"><a href="#">Full results</a></td>'
              + '</tr>';
          }).join('')
        : '<tr><td colspan="4">No shoot results posted yet. Results go up here within a few days '
          + 'of each shoot — the Brush Shoot in February and both outdoor 3D shoots in the spring.</td></tr>';
    }
  }

  /* ---------- contests page ---------- */
  function renderContests() {
    var el = document.getElementById('contests');
    if (!el) return;
    el.innerHTML = CONTESTS.map(function (c) {
      return '<div class="card card-pad">'
        + '<h3 style="margin-bottom:10px">' + c.name + tags(c) + '</h3>'
        + '<dl class="dl">'
        +   '<div><dt>Entry</dt><dd><strong>' + c.entry + '</strong></dd></div>'
        +   '<div><dt>Runs</dt><dd>' + c.season + '</dd></div>'
        +   '<div><dt>Who</dt><dd>' + c.who + '</dd></div>'
        +   (c.prize ? '<div><dt>Prize</dt><dd><strong>' + c.prize + '</strong></dd></div>' : '')
        + '</dl>'
        + '<p style="margin-bottom:0">' + c.detail + '</p>'
        + '</div>';
    }).join('');
  }

  /* ---------- membership page ---------- */
  function renderDues() {
    var el = document.getElementById('dues-body');
    if (!el) return;
    el.innerHTML = DUES.map(function (d) {
      return '<tr>'
        + '<td data-l="Level" class="center"><span class="ev-name">' + d.level + '</span>' + tags(d) + '</td>'
        + '<td data-l="Dues" class="center"><strong>' + d.price + '</strong></td>'
        + '<td data-l="Notes">' + d.notes + '</td>'
        + '</tr>';
    }).join('');
  }

  /* ---------- sponsors page ---------- */
  function renderTiers() {
    var el = document.getElementById('tiers');
    if (!el) return;
    el.innerHTML = SPONSOR_TIERS.map(function (t) {
      return '<div class="card card-pad">'
        + '<h3 style="color:var(--forest)">' + t.name + tags(t) + '</h3>'
        + '<ul class="tick" style="margin-bottom:0">'
        + t.perks.map(function (p) { return '<li>' + p + '</li>'; }).join('')
        + '</ul></div>';
    }).join('');
  }

  /* ---------- club facts sprinkled in copy ---------- */
  function fillFacts() {
    CLUB.years = new Date().getFullYear() - CLUB.founded;
    Array.prototype.forEach.call(document.querySelectorAll('[data-club]'), function (el) {
      var v = CLUB[el.getAttribute('data-club')];
      if (v !== undefined) el.textContent = v;
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-maps]'), function (el) {
      el.setAttribute('href', mapsUrl());
    });
    /* Dates quoted mid-sentence come from the schedule, so body copy can't
       drift out of step with the calendar:
         <span data-event-date="Brush Shoot">…</span>                    */
    Array.prototype.forEach.call(document.querySelectorAll('[data-event-date]'), function (el) {
      var name = el.getAttribute('data-event-date');
      var fmt = el.getAttribute('data-event-format');
      var up = upcoming(), i;
      for (i = 0; i < up.length; i++) {
        if (up[i].name === name) {
          el.textContent = fmt === 'monthday' ? fmtMonthDay(up[i]) : fmtSpanLong(up[i]);
          return;
        }
      }
      /* Nothing scheduled — say so rather than leaving last year's date up. */
      el.textContent = 'dates to be announced';
    });
    /* The club email lives in one place (CLUB.email) and every link to it
       is filled from there, so changing it is a one-line edit. */
    Array.prototype.forEach.call(document.querySelectorAll('[data-club-email]'), function (el) {
      if (!CLUB.email) return;
      el.setAttribute('href', 'mailto:' + CLUB.email);
      el.textContent = CLUB.email;
    });
    /* Copyright year, so the footer doesn't need an annual edit */
    Array.prototype.forEach.call(document.querySelectorAll('[data-year]'), function (el) {
      el.textContent = new Date().getFullYear();
    });
    /* data-next="meeting" etc. — always shows the real next date */
    Array.prototype.forEach.call(document.querySelectorAll('[data-next]'), function (el) {
      var want = el.getAttribute('data-next');
      var up = upcoming();
      for (var i = 0; i < up.length; i++) {
        if (up[i].type === want) { el.textContent = fmtLong(up[i].date); return; }
      }
      el.textContent = 'to be posted';
    });
  }

  /* ---------- ICS download ---------- */
  function wireIcs() {
    var btn = document.getElementById('ics');
    if (!btn) return;
    btn.addEventListener('click', function (ev) {
      ev.preventDefault();
      var L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Tri-County Archers//Schedule//EN', 'X-WR-CALNAME:Tri-County Archers'];
      EVENTS.forEach(function (e, i) {
        var start = e.date.replace(/-/g, '');
        var end = exclusiveEnd(e);
        L.push('BEGIN:VEVENT', 'UID:tca-' + i + '@tricountyarchers', 'DTSTART;VALUE=DATE:' + start,
               'DTEND;VALUE=DATE:' + end, 'SUMMARY:' + e.name,
               'DESCRIPTION:' + (e.reg + ' — ' + e.fees + '. ' + e.detail).replace(/,/g, '\\,'),
               'LOCATION:' + CLUB.address.replace(/,/g, '\\,'), 'END:VEVENT');
      });
      L.push('END:VCALENDAR');
      var a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([L.join('\r\n')], { type: 'text/calendar' }));
      a.download = 'tri-county-archers-schedule.ics';
      a.click();
    });
  }

  /* ---------- links that leave the site ---------- */
  /* Anything pointing at another site opens in a new tab, so nobody loses
     their place on the schedule. Done here rather than by hand on every
     link, so anything added later — including generated links — is covered.
     mailto:, tel: and #anchors are left alone. */
  function wireExternalLinks() {
    var here = location.hostname;
    Array.prototype.forEach.call(document.querySelectorAll('a[href]'), function (a) {
      if (a.protocol !== 'http:' && a.protocol !== 'https:') return;
      if (!a.hostname || a.hostname === here) return;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
    });
  }

  /* ---------- mobile nav ---------- */
  function wireNav() {
    var b = document.querySelector('.burger'), n = document.querySelector('.nav');
    if (b && n) b.addEventListener('click', function () { n.classList.toggle('open'); });
  }

  /* ---------- membership application ---------- */
  /* Same approach as the contact form: build a complete mailto and hand it
     to the applicant's own email app, addressed to the club. */
  function wireForm() {
    var f = document.getElementById('apply');
    if (!f) return;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var val = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : '';
      };
      var level = val('lv') || 'Membership';
      var body = [
        'Name:    ' + val('fn') + ' ' + val('ln'),
        'Email:   ' + val('em'),
        'Phone:   ' + (val('ph') || '—'),
        'Address: ' + (val('ad') || '—'),
        'Level:   ' + level,
        'Family members: ' + (val('hh') || '—'),
        '',
        'What they shoot: ' + (val('ex') || '—'),
        '',
        '— sent from the Tri-County Archers website'
      ].join('\n');

      window.location.href = 'mailto:' + CLUB.email
        + '?subject=' + encodeURIComponent('Membership application — ' + val('fn') + ' ' + val('ln'))
        + '&body=' + encodeURIComponent(body);

      var m = document.getElementById('apply-done');
      if (m) { m.classList.remove('hide'); m.scrollIntoView({ block: 'center' }); }
    });
  }

  /* ---------- contact form ---------- */
  /* Builds a mailto: so this works on a static site with no backend and no
     third-party account. Swapping in a form service later means changing
     this function only. */
  function wireContact() {
    var f = document.getElementById('contact');
    if (!f) return;
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var val = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : '';
      };
      var topic = val('c-topic') || 'Website enquiry';
      var body = [
        'Name:  ' + val('c-name'),
        'Email: ' + val('c-email'),
        'Phone: ' + (val('c-phone') || '—'),
        'About: ' + topic,
        '',
        val('c-msg'),
        '',
        '— sent from the Tri-County Archers website'
      ].join('\n');

      window.location.href = 'mailto:' + CLUB.email
        + '?subject=' + encodeURIComponent(topic + ' — via the website')
        + '&body=' + encodeURIComponent(body);

      var done = document.getElementById('contact-done');
      if (done) {
        done.classList.remove('hide');
        done.scrollIntoView({ block: 'center' });
      }
    });
  }

  /* ---------- go ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    renderAlert(); renderNextUp(); renderSchedule(); renderLeagues();
    renderResults(); renderContests(); renderDues(); renderTiers(); fillFacts();
    wireIcs(); wireNav(); wireForm(); wireContact(); wireExternalLinks();
  });
})();

/* ============================================================
   Tri-County Archers — SITE DATA
   ------------------------------------------------------------
   THIS IS THE ONLY FILE THAT NEEDS EDITING FOR ROUTINE UPDATES.
   The homepage "What's Next" block, the Shoot Schedule page and
   the calendar feed are all generated from what's below, so a
   date typed here can never disappear from one page and linger
   on another.

   TAGS that render on the page so nothing is silently invented:
     tag:"..."     a yellow note — something still to confirm
     verify:true   a real date from the club that doesn't line up
                   with the stated rule; needs one more check
     guess:true    a placeholder Claude invented
   Delete the flag when the real value goes in.
   ============================================================ */

const CLUB = {
  name: "Tri-County Archers",
  counties: "Grant · Iowa · Lafayette",
  founded: 1937,
  formerName: "Iowa-Grant Conservation Club",
  address: "9145 County Line Rd, Platteville, WI 53818",
  phone: "###-###-####",                            // real number still needed
  email: "tricountyarcheryclub@gmail.com",
  facebook: "https://www.facebook.com/TriCountyArchers/",
  instagram: "https://www.instagram.com/tricountyarchers/",

  // Membership
  dues: 25,                                         // dollars/year, single or family
  duesNote: "Single or family, same price. Calendar year.",
  guestFee: 5,                                      // dollars per guest brought by a member
  shootFee: 15,                                     // dollars per person, Brush Shoot + both outdoor 3D shoots

  // Facility
  targetsOutdoor: 40,     // outdoor 3D course
  targetsIndoor: 28,      // indoor 3D, set for the Brush Shoot

  // Meeting rule — see MEETING_RULE below, which generates the dates
  meeting: "3rd Wednesday June–December · 3rd Thursday January–May, 7:00–8:00 pm",

  // Homepage alert strip. text:"" hides it entirely.
  alert: {
    text: "Membership is $25 a year — single or family, no work-hour requirement. Apply any time.",
    tone: "ok"      // "ok" = green, "warn" = orange (cancellations, closures)
  }
};

/* ------------------------------------------------------------
   DATE HELPERS — used by the generators below
   ------------------------------------------------------------ */
function _nthWeekday(year, month, weekday, n) {
  var first = new Date(year, month, 1);
  var shift = (weekday - first.getDay() + 7) % 7;
  return new Date(year, month, 1 + shift + (n - 1) * 7);
}
function _iso(d) {
  return d.getFullYear() + '-' +
         String(d.getMonth() + 1).padStart(2, '0') + '-' +
         String(d.getDate()).padStart(2, '0');
}
function _addDays(isoDate, n) {
  var p = isoDate.split('-');
  var d = new Date(+p[0], +p[1] - 1, +p[2]);
  d.setDate(d.getDate() + n);
  return _iso(d);
}
function _addWeeks(isoDate, w) {
  var p = isoDate.split('-');
  var d = new Date(+p[0], +p[1] - 1, +p[2]);
  d.setDate(d.getDate() + w * 7);
  return _iso(d);
}

/* Everything dated below is worked out relative to today, so the calendar
   rolls forward on its own. Nobody has to come back in January and type in
   next year's meeting or league dates. */
var _now = new Date();
var _thisYear = _now.getFullYear();
var _todayIso = _iso(new Date(_now.getFullYear(), _now.getMonth(), _now.getDate()));

/* ------------------------------------------------------------
   MONTHLY MEETINGS — generated from the rule, not typed out.
   January–May : 3rd Thursday
   June–December: 3rd Wednesday
   Both 7:00–8:00 pm. Nine chances a year to publish a wrong
   date, so it's generated instead of hand-maintained.
   ------------------------------------------------------------ */
const MEETING_RULE = {
  winter: { months: [0, 1, 2, 3, 4], weekday: 4, label: "3rd Thursday" },   // Jan–May, Thursday
  summer: { months: [5, 6, 7, 8, 9, 10, 11], weekday: 3, label: "3rd Wednesday" }, // Jun–Dec, Wednesday
  nth: 3,
  time: "7:00 – 8:00 pm"
};

function _meetings(fromYear, toYear) {
  var out = [];
  for (var y = fromYear; y <= toYear; y++) {
    for (var m = 0; m < 12; m++) {
      var wd = MEETING_RULE.winter.months.indexOf(m) > -1
        ? MEETING_RULE.winter.weekday
        : MEETING_RULE.summer.weekday;
      out.push({
        date: _iso(_nthWeekday(y, m, wd, MEETING_RULE.nth)),
        name: "Monthly Club Meeting",
        type: "meeting", cat: "Meeting", who: "members",
        reg: MEETING_RULE.time,
        fees: "—",
        detail: "At the clubhouse. Attendance is recommended, not required. " +
                "Anybody thinking about joining the club is welcome to sit in.",
        contact: "Club secretary"
      });
    }
  }
  return out;
}

/* ------------------------------------------------------------
   LEAGUE SEASONS — one row per season, not one per night.
   The Leagues page and the homepage card compute the current
   week from `start` and `weeks`.
   ------------------------------------------------------------ */
/* Each league starts on a fixed rule, so the season dates work themselves
   out year after year. `overrides` is the escape hatch for a year that
   doesn't follow the rule — add "2029": "2029-06-13" and that season moves,
   everything else carries on as normal. */
const LEAGUE_DEFS = [
  {
    key: "indoor",
    night: "Thursday Nights",
    name: "Indoor League",
    indoor: true,
    rule: { month: 0, weekday: 4, nth: 1, label: "the first Thursday in January" },
    overrides: {},
    weeks: 10,
    scoring: "individual",
    cost: "$40 for the season",
    round: "30-arrow Vegas at 20 yards — three-spot face, one arrow per spot, 300 possible.",
    time: "League night is Thursday — but shoot your score any day of the week that works for you.",
    who: "Members",
    coord: "League coordinator",
    coordTag: "name and contact needed",
    note: "Ten weeks of indoor Vegas, shot individually, starting the first Thursday in January."
  },
  {
    key: "outdoor",
    night: "Wednesday Nights",
    name: "Outdoor 3D League",
    indoor: false,
    rule: { month: 5, weekday: 3, nth: 1, label: "the first Wednesday in June" },
    overrides: {},
    weeks: 10,
    scoring: "team",
    cost: "$35 for the season",
    round: "14 targets, two arrows each — foam animals at unmarked distances, judged by eye. "
         + "28 arrows a week, 20 points possible per arrow, 560 possible for the week. Shot in teams of two.",
    time: "League night is Wednesday — but shoot your score any day of the week that works for you.",
    who: "Members",
    coord: "League coordinator",
    coordTag: "name and contact needed",
    note: "Ten weeks out on the 3D course, shot in two-archer teams, from the first Wednesday in June."
  }
];

/* Resolve each league to the season that's running right now, or the next one
   coming up if we're between seasons. */
function _resolveLeagues(defs) {
  return defs.map(function (d) {
    var l = {}, k;
    for (k in d) if (Object.prototype.hasOwnProperty.call(d, k)) l[k] = d[k];
    for (var y = _thisYear - 1; y <= _thisYear + 2; y++) {
      var start = d.overrides[y]
        || _iso(_nthWeekday(y, d.rule.month, d.rule.weekday, d.rule.nth));
      var end = _addWeeks(start, d.weeks - 1);
      if (_todayIso <= end) {
        l.start = start;
        l.end = end;
        l.seasonYear = y;
        l.season = "Starts " + d.rule.label;
        return l;
      }
    }
    return l;
  });
}

const LEAGUES = _resolveLeagues(LEAGUE_DEFS);

/* ------------------------------------------------------------
   EVENTS
   type: shoot | league | meeting | social | work
   who:  public | members
   end:  optional — for multi-day events
   ------------------------------------------------------------ */
/* ------------------------------------------------------------
   SHOOTS AND THE BANQUET — generated from rules, same as the
   meetings and the league seasons. Nothing to update each year.

   `nth` is which of that weekday in the month (1 = first).
   weekday: 0 = Sunday … 6 = Saturday.  month: 0 = January.
   `days` is how long it runs, so a Sat–Sun shoot is days: 2.

   `overrides` is the escape hatch for a year that moves — say the
   course isn't ready, or another club has that weekend:
       overrides: { 2029: "2029-04-14" }
   ------------------------------------------------------------ */
const SHOOT_DEFS = [
  {
    name: "Annual Banquet", type: "social", cat: "Social", who: "public",
    rule: { month: 1, weekday: 6, nth: 1, label: "the first Saturday in February" },
    overrides: {}, days: 1,
    reg: "Time to be posted", fees: "Tickets to be posted",
    detail: "Raffles from local sponsors, food, drink and fellowship. The one night of the year the "
          + "whole club is in the same room.",
    contact: "Club secretary", tag: "time and ticket price to confirm"
  },
  {
    name: "Brush Shoot", type: "shoot", cat: "Indoor", who: "public",
    rule: { month: 1, weekday: 6, nth: 2, label: "the second Saturday in February" },
    overrides: {}, days: 2,
    reg: "Hours to be posted", fees: "$" + CLUB.shootFee + " per person",
    detail: "The club's indoor 3D shoot — 28 targets set through the clubhouse with brush and trees "
          + "hauled in to build a walk-through course indoors. Short ranges, awkward angles, and "
          + "nothing else like it in the area.",
    contact: "Shoot chair", tag: "hours and contact to confirm"
  },
  {
    name: "Outdoor 3D Shoot", type: "shoot", cat: "3D", who: "public",
    rule: { month: 3, weekday: 6, nth: 1, label: "the first Saturday in April" },
    overrides: {}, days: 2,
    reg: "Hours to be posted", fees: "$" + CLUB.shootFee + " per person",
    detail: "First of the year's two outdoor 3D shoots. 40 targets on the walk-through course, "
          + "unmarked distances.",
    contact: "Shoot chair", tag: "hours and contact to confirm"
  },
  {
    /* Fourth Saturday, which is what the 2026-27 dates worked out to.
       If it's really the LAST Saturday, that differs in months with five —
       change nth to 5 and add an override for the years with only four. */
    name: "Outdoor 3D Shoot", type: "shoot", cat: "3D", who: "public",
    rule: { month: 4, weekday: 6, nth: 4, label: "the fourth Saturday in May" },
    overrides: {}, days: 1,
    reg: "Hours to be posted", fees: "$" + CLUB.shootFee + " per person",
    detail: "Second outdoor 3D shoot of the year. 40 targets on the walk-through course, "
          + "unmarked distances.",
    contact: "Shoot chair", tag: "hours and contact to confirm"
  }
];

/* One occurrence per year across the window. Last year keeps the "Past
   events" filter useful; next year means there's always a future date up. */
function _shoots(defs, fromYear, toYear) {
  var out = [];
  defs.forEach(function (d) {
    for (var y = fromYear; y <= toYear; y++) {
      var start = d.overrides[y]
        || _iso(_nthWeekday(y, d.rule.month, d.rule.weekday, d.rule.nth));
      var e = {
        date: start, name: d.name, type: d.type, cat: d.cat, who: d.who,
        reg: d.reg, fees: d.fees, detail: d.detail, contact: d.contact
      };
      if (d.days > 1) e.end = _addDays(start, d.days - 1);
      if (d.tag) e.tag = d.tag;
      out.push(e);
    }
  });
  return out;
}

/* ------------------------------------------------------------
   EVENTS — everything dated, assembled from the rules above.
   type: shoot | league | meeting | social | work
   who:  public | members
   ------------------------------------------------------------ */
const EVENTS = _shoots(SHOOT_DEFS, _thisYear - 1, _thisYear + 1).concat(
  /* ---- League season openers and finals, from LEAGUES ---- */
  LEAGUES.reduce(function (acc, l) {
    acc.push({
      date: l.start,
      name: l.name + " — Week 1",
      type: "league", cat: "League", who: "members",
      reg: l.night.replace(' Nights', ' nights') + ", or any day that week",
      fees: l.cost,
      detail: l.round + " " + l.weeks + " weeks. " + l.time,
      contact: l.coord,
      verify: l.verify,
      tag: l.coordTag
    });
    acc.push({
      date: _addWeeks(l.start, l.weeks - 1),
      name: l.name + " — Final Week",
      type: "league", cat: "League", who: "members",
      reg: l.night.replace(' Nights', ' nights') + ", or any day that week",
      fees: "Included with season entry",
      detail: "Last scoring week of the " + l.weeks + "-week season. Standings finalized after.",
      contact: l.coord,
      verify: l.verify,
      tag: "end date follows from the start date — confirm any skip weeks"
    });
    return acc;
  }, [])
).concat(
  /* ---- Monthly meetings, generated from the rule ---- */
  /* Last year through two years out: keeps the "Past events" filter useful
     and means the calendar never runs dry. */
  _meetings(_thisYear - 1, _thisYear + 2)
);

/* Course setup and teardown days are real events members turn out for,
   but no dates have been set yet. Add them here when they are:
   { date:"2027-04-17", name:"3D Course Setup", type:"work", cat:"Work",
     who:"members", reg:"8:00 am start", fees:"—",
     detail:"Set stakes and place targets for the outdoor season.",
     contact:"Grounds chair" }                                          */

/* ------------------------------------------------------------
   RESULTS  (frame — replace with real score sheets)
   ------------------------------------------------------------ */
const RESULTS = {

  /* Summer 2026 outdoor league — real scores, from the club's spreadsheet.
     Two-archer teams. TOTAL POINTS over the ten weeks decides the league;
     the average column is context only. "X" = that week wasn't shot, and an
     archer's average counts only the weeks they did shoot. */
  "outdoor-3d-league-2026": {
    title: "Outdoor 3D League",
    season: "Summer 2026",
    status: "Final · 10 weeks · two-archer teams · 14 targets, 2 arrows each, 560 possible per week",
    format: "team",
    weeks: 10,
    updated: "2026-08-22",
    decidedBy: "Total points over the ten weeks decides the league.",
    teams: [
      { team: 3, total: 10185, avg: 509.25, archers: [
        { name: "Dustin", total: 5110, avg: 511,
          scores: [380, 470, 530, 530, 490, 550, 530, 540, 545, 545] },
        { name: "Jake",   total: 5075, avg: 507.5,
          scores: [465, 505, 525, 525, 485, 520, 510, 510, 525, 505] }
      ]},
      { team: 2, total: 9040, avg: 452, archers: [
        { name: "Dave", total: 4185, avg: 418.5,
          scores: [225, 460, 460, 425, 430, 445, 445, 455, 400, 440] },
        { name: "Paul", total: 4855, avg: 485.5,
          scores: [455, 495, 475, 445, 455, 485, 515, 515, 485, 530] }
      ]},
      { team: 1, total: 7930, avg: 464.5357142857143, archers: [
        { name: "Will",  total: 4755, avg: 475.5,
          scores: [440, 455, 460, 510, 490, 470, 445, 510, 465, 510] },
        { name: "Chris", total: 3175, avg: 453.5714285714286,
          scores: [480, 405, 360, 480, 490, 510, 450, "X", "X", "X"] }
      ]}
    ]
  },

  /* Indoor league is shot individually. Add archers here as scores come in:
     rows: [ { name:"...", total:0, avg:0, scores:[...] } ]                  */
  "indoor-league-2027": {
    title: "Indoor League",
    season: "Winter 2027",
    status: "Starts January 7 · 10 weeks · individual",
    format: "individual",
    weeks: 10,
    updated: "2026-08-22",
    rows: [],
    empty: "Scores go up here through the season. Indoor league is shot individually — "
         + "30-arrow Vegas at 20 yards, 300 possible."
  }
};

/* Shoot results get added after each shoot. Empty until real cards arrive.
   { date:"2027-02-14", name:"Brush Shoot", entries:0, note:"Indoor 3D, 28 targets" } */
const SHOOT_RESULTS = [];

/* ------------------------------------------------------------
   CONTESTS — season-long member contests and one-off promotions.
   Add a new one here and it appears on the Contests page.
   ------------------------------------------------------------ */
const CONTESTS = [
  {
    name: "Big Buck — Bow",
    season: "Archery deer season",
    entry: "$10",
    who: "Members",
    prize: "Winner takes the pot",
    detail: "The bow side of the club's big buck contest. Everybody who pays in builds the pot, and "
          + "the winner takes the whole thing.",
    tag: "entry deadline and how it's scored to confirm"
  },
  {
    name: "Big Buck — Gun",
    season: "Gun deer season",
    entry: "$10",
    who: "Members",
    prize: "Winner takes the pot",
    detail: "Same contest, run for gun season. Separate pot from the bow side, so you can enter one "
          + "or both.",
    tag: "entry deadline and how it's scored to confirm"
  },
  {
    name: "Fall Turkey",
    season: "Fall turkey season",
    entry: "$10",
    who: "Members",
    prize: "Winner takes the pot",
    detail: "Run through the fall turkey season.",
    tag: "confirm the turkey contest pays out the same way"
  }
];

/* ------------------------------------------------------------
   MEMBERSHIP
   ------------------------------------------------------------ */
const DUES = [
  { level:"Single", price:"$25", hours:"None required",
    notes:"One adult. Runs with the calendar year." },
  { level:"Family", price:"$25", hours:"None required",
    notes:"Same price as single — covers the household. Runs with the calendar year." }
];

/* ------------------------------------------------------------
   SPONSORS — tiers and prices are a starting point for the board
   ------------------------------------------------------------ */
const SPONSOR_TIERS = [
  { name:"Bullseye — $500", perks:[
      "Banner at the Brush Shoot and both outdoor 3D shoots",
      "Raffle recognition at the annual banquet",
      "Logo on the website homepage and sponsors page",
      "Recognition from the podium at the banquet"
    ], guess:true },
  { name:"Gold — $250", perks:[
      "Banner at both outdoor 3D shoots",
      "Raffle recognition at the annual banquet",
      "Logo on the sponsors page"
    ], guess:true },
  { name:"Supporting — $100", perks:[
      "Name on the sponsors page",
      "Name listed at the banquet",
      "Sign at the food stand"
    ], guess:true }
];

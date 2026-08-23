#!/usr/bin/env python3
"""Tri-County Archers — static site generator.
Run:  python3 build.py     (writes the .html files next to it)
Header/footer/nav live here so all pages stay identical."""
import os, datetime

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html",    "Home"),
    ("schedule.html", "Schedule"),
    ("leagues.html",  "Leagues"),
    ("contests.html", "Contests"),
    ("range.html",    "Range"),
    ("photos.html",   "Photos"),
    ("about.html",    "About"),
    ("contact.html",  "Contact"),
]

FB = "https://www.facebook.com/TriCountyArchers/"
IG = "https://www.instagram.com/tricountyarchers/"
MAPS = ("https://www.google.com/maps/dir/?api=1&destination="
        "9145+County+Line+Rd%2C+Platteville%2C+WI+53818")

DRAFT = ('<div class="draftbar"><div class="wrap">'
         '<strong>Preview.</strong> This site is still being updated — anything tagged '
         '<span class="tbd">like this</span> likely needs more info. · rev 2026.08.23.1</div></div>')

def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Tri-County Archers · Platteville, Wisconsin</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
{DRAFT}
<header class="hdr">
  <div class="hdr-in">
    <a class="brand" href="index.html">
      <img src="assets/img/logo-white.png" alt="Tri-County Archers logo">
      <span class="brand-txt">
        <span class="brand-name">Tri-County Archers</span>
        <span class="brand-sub">Grant · Iowa · Lafayette · Wisconsin</span>
      </span>
    </a>
    <button class="burger" aria-label="Menu">☰</button>
    <nav class="nav">
      {''.join(f'<a href="{h}" class="{"on" if h==page else ""}">{t}</a>' for h,t in NAV)}
      <a href="membership.html" class="cta{' on' if page=='membership.html' else ''}">Join the Club</a>
    </nav>
  </div>
</header>
"""

FOOT = f"""
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div class="ftr-brand">
        <img src="assets/img/logo-white.png" alt="">
        <p><strong style="color:#fff">Tri-County Archers</strong><br>
        9145 County Line Rd<br>Platteville, WI 53818<br>
        <span data-club="phone">###-###-####</span> <span class="tbd">number needed</span></p>
        <p class="small"><a href="{MAPS}" style="display:inline" target="_blank" rel="noopener noreferrer">Directions in Google Maps &rarr;</a></p>
        <p class="small">Serving Grant, Iowa and Lafayette counties since
          <span data-club="founded">1937</span>.</p>
      </div>
      <div>
        <h4>Shooting</h4>
        <a href="schedule.html">Shoot Schedule</a>
        <a href="leagues.html">Leagues</a>
        <a href="leagues.html#standings">League Standings</a>
        <a href="contests.html">Contests</a>
      </div>
      <div>
        <h4>The Club</h4>
        <a href="membership.html">Become a Member</a>
        <a href="range.html">Range &amp; Directions</a>
        <a href="photos.html">Photos</a>
        <a href="sponsors.html">Our Sponsors</a>
        <a href="about.html">About the Club</a>
        <a href="contact.html">Contact Us</a>
      </div>
      <div>
        <h4>Stay in the loop</h4>
        <p class="small">League start dates, weather calls and shoot reminders. No more than a couple of emails a month.</p>
        <form class="news" onsubmit="event.preventDefault();this.innerHTML='<p class=\\'small\\' style=\\'margin:0;color:#A8D5B8\\'>Thanks — you\\'re on the list.</p>'">
          <input type="email" placeholder="your@email.com" required aria-label="Email">
          <button class="btn btn-blaze btn-sm" type="submit">Go</button>
        </form>
        <p class="small" style="margin-top:14px">
          <a href="{FB}" style="display:inline" target="_blank" rel="noopener noreferrer">Facebook</a> ·
          <a href="{IG}" style="display:inline" target="_blank" rel="noopener noreferrer">Instagram</a></p>
      </div>
    </div>
    <div class="ftr-bot">
      <span>&copy; <span data-year>2026</span> Tri-County Archers Club, Inc. · Established 1937 as the Iowa-Grant Conservation Club</span>
      <span>Home to the Iowa-Grant Trap Team · Grant County 4-H Shooting Sports · UW-Platteville Pioneer Sportsman's Club</span>
    </div>
  </div>
</footer>
<script src="assets/js/data.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>"""

def phead(crumb, h1, p):
    return f"""<section class="phead"><div class="wrap">
  <div class="crumb">{crumb}</div><h1>{h1}</h1><p>{p}</p>
</div></section>"""

def write(name, title, desc, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(head(title, desc, name) + body + FOOT)
    print("wrote", name)

# ================================================================
# HOME
# ================================================================
write("index.html", "Home",
"Tri-County Archers is an archery club in Platteville, Wisconsin serving Grant, Iowa and Lafayette counties. Established 1937. 3D shoots, indoor Vegas league, outdoor 3D league. $25 a year.",
"""
<div id="alert"></div>

<section class="hero">
  <div class="hero-bg" style="background-image:url('assets/img/flag-sunset.jpg')"></div>
  <div class="hero-in">
    <div class="hero-eyebrow">Platteville, Wisconsin · Est. <span data-club="founded">1937</span></div>
    <h1>Forty targets<br>in the timber.</h1>
    <p class="hero-lede">Tri-County Archers has been on this ground since 1937, when it started life as
      the Iowa-Grant Conservation Club. Indoor Vegas league through the winter, a 40-target 3D course
      through the summer, three shoots a year, and twenty-five dollars to belong.</p>
    <div class="hero-btns">
      <a href="schedule.html" class="btn btn-blaze">See the shoot schedule</a>
      <a href="membership.html" class="btn btn-ghost">Become a member</a>
    </div>
  </div>
</section>

<!-- WHAT'S NEXT -->
<section class="sec sec-tight" style="background:var(--cream-warm)">
  <div class="wrap">
    <div class="eyebrow">What's next at the club</div>
    <div class="nextup" id="nextup"></div>
  </div>
</section>

<!-- NEVER BEEN HERE BEFORE -->
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Never been here before?</div>
        <h2>Three easy ways in.</h2>
        <p class="lead">You don't need to be a member and you don't need to know anybody.
          Plenty of people shoot their first arrow ever at a Tri-County shoot.</p>
        <ol class="steps" style="margin-bottom:26px">
          <li>
            <h3>Send us a note</h3>
            <p>Tell us a bit about yourself and what you're after — joining, sponsoring, getting a kid
              started — and somebody will get back to you.</p>
            <a href="contact.html" class="btn btn-blaze btn-sm">Email the club</a>
          </li>
          <li>
            <h3>Come to a monthly meeting</h3>
            <p>Third Wednesday June&ndash;December, third Thursday January&ndash;May, 7:00&ndash;8:00 pm at the
              clubhouse. Next one: <strong data-next="meeting">&mdash;</strong>. You can sign up in person.</p>
          </li>
          <li>
            <h3>Come out to a shoot</h3>
            <p>Every event on our schedule is open to non-members &mdash; the Brush Shoot in February and
              both outdoor 3D shoots in the spring. Or come as a member's guest for
              $<span data-club="guestFee">5</span>.</p>
            <a href="schedule.html" class="btn btn-out btn-sm">See the schedule</a>
          </li>
        </ol>
        <p class="small muted" style="margin:0">Membership is $<span data-club="dues">25</span> a year &mdash;
          single or family, same price, no work-hour requirement. Bringing a kid?
          <a href="membership.html#youth">Grant County 4-H practices here and provides the equipment.</a></p>
      </div>
      <div class="split-img">
        <img src="assets/img/indoor-archers.jpg" alt="Archers on the indoor line at the Tri-County Archers clubhouse">
      </div>
    </div>
  </div>
</section>

<!-- THREE TILES -->
<section class="sec sec-cream">
  <div class="wrap">
    <div class="grid g3">
      <a class="tile card-link" href="leagues.html">
        <img class="card-img" src="assets/img/arrows-wide.jpg" alt="Arrows in a quiver on the indoor range">
        <div class="tile-body">
          <h3>Two leagues, ten weeks each</h3>
          <p>Indoor Vegas from the first Thursday in January, outdoor 3D from the first Wednesday in
             June — and you can shoot your score any day of the week that suits you.</p>
          <span class="tile-more">See the leagues and standings &rarr;</span>
        </div>
      </a>
      <a class="tile card-link" href="contests.html">
        <img class="card-img" src="assets/img/arrows.jpg" alt="Arrows and vanes on the indoor line">
        <div class="tile-body">
          <h3>Big Buck and Fall Turkey</h3>
          <p>Bow and gun big buck, plus fall turkey. Ten dollars in, and the winner takes the whole
             pot. Other promotions land here through the year too.</p>
          <span class="tile-more">See the contests &rarr;</span>
        </div>
      </a>
      <a class="tile card-link" href="membership.html">
        <img class="card-img" src="assets/img/banner-sunset.jpg" alt="Sunset over the Tri-County Archers grounds">
        <div class="tile-body">
          <h3>Twenty-five dollars a year</h3>
          <p>Single or family, same price, and no work-hour requirement. Printed right here on the
             page — no PDF download required to find out what it costs.</p>
          <span class="tile-more">See membership →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="sec sec-forest">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="n" data-club="targetsOutdoor">40</div><div class="l">Targets on the 3D course</div></div>
      <div class="stat"><div class="n" data-club="targetsIndoor">28</div><div class="l">Indoor targets at the Brush Shoot</div></div>
      <div class="stat"><div class="n">$25</div><div class="l">A year to join</div></div>
      <div class="stat"><div class="n" data-club="years">89</div><div class="l">Years on this ground</div></div>
    </div>
  </div>
</section>

<!-- BRUSH SHOOT -->
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div class="split-img">
        <img src="assets/img/indoor-3d-Brush-shoot.jpg" alt="The clubhouse set up as an indoor 3D brush shoot course">
      </div>
      <div>
        <div class="eyebrow" data-event-date="Brush Shoot">February 13–14, 2027</div>
        <h2>We build a forest<br>inside the clubhouse.</h2>
        <p>Once a year the indoor range gets filled with brush and trees hauled in from outside, and
          twenty-eight 3D targets get set through it. You walk it like a course — short ranges,
          awkward angles, shots you'd never get on an open lane.</p>
        <p>It's the club's signature shoot and there's nothing else like it around here. Open to
          the public, no membership needed.</p>
        <a href="schedule.html" class="btn btn-out">See the full schedule</a>
      </div>
    </div>
  </div>
</section>

<!-- SPONSORS STRIP -->
<section class="sec sec-tight sec-cream">
  <div class="wrap center">
    <div class="eyebrow" style="text-align:center">Our shoots and our banquet raffle run on their support</div>
    <h2 style="margin-bottom:26px">Club sponsors</h2>
    <div class="spons" style="max-width:620px;margin:0 auto 26px;grid-template-columns:repeat(3,1fr)">
      <div class="spon">Sponsor logo</div>
      <div class="spon">Sponsor logo</div>
      <div class="spon">Sponsor logo</div>
      <div class="spon">Sponsor logo</div>
      <div class="spon">Sponsor logo</div>
      <div class="spon">Sponsor logo</div>
    </div>
    <p class="muted" style="max-width:36em;margin:0 auto 22px">
      Send us your sponsor list with logos and web addresses and these fill in.
      <span class="tbd">needs sponsor list</span></p>
    <a href="sponsors.html" class="btn btn-forest">Become a sponsor</a>
  </div>
</section>

<!-- CTA -->
<section class="sec sec-forest">
  <div class="wrap narrow center">
    <h2>Come shoot with us.</h2>
    <p class="lead" style="color:#C7DACD">Twenty-five dollars a year for you or your whole family,
      running with the calendar year. No work hours required — though you'll usually find members out
      here putting the course up in spring, working the shoots and keeping the grass down.</p>
    <div class="hero-btns" style="justify-content:center;margin-top:26px">
      <a href="membership.html" class="btn btn-blaze">Apply for membership</a>
      <a href="range.html" class="btn btn-ghost">Get directions</a>
    </div>
  </div>
</section>
""")

# ================================================================
# SCHEDULE
# ================================================================
write("schedule.html", "Shoot Schedule",
"Every Tri-County Archers shoot, league date, banquet and monthly meeting — with hours, fees and whether it's open to the public.",
phead("The calendar", "Shoot Schedule",
 "One page, every date. Three shoots a year, two leagues, the banquet and the monthly meetings.") + """
<section class="sec">
  <div class="wrap">

    <div class="filters" id="sched-filters">
      <span class="filters-lbl">Show</span>
      <button class="chip on" data-f="all">Everything</button>
      <button class="chip" data-f="public">Open to the public</button>
      <button class="chip" data-f="members">Members</button>
      <button class="chip" data-f="3D">Outdoor 3D</button>
      <button class="chip" data-f="Indoor">Indoor</button>
      <button class="chip" data-f="League">Leagues</button>
      <button class="chip" data-f="Meeting">Meetings</button>
    </div>

    <div class="tbl-wrap">
      <table class="t stack t-sched">
        <thead><tr><th>Date</th><th>Event</th><th>Hours</th><th>Cost</th></tr></thead>
        <tbody id="sched-body"></tbody>
      </table>
    </div>

    <div class="grid g2" style="margin-top:38px">
      <div class="call call-forest">
        <h3>Put the whole season on your phone</h3>
        <p>Every event above has an <strong>Add to Google Calendar</strong> button. Or take the whole
          season in one file and import it into Google Calendar, Apple Calendar or Outlook.</p>
        <a href="#" id="ics" class="btn btn-forest btn-sm">Download calendar file (.ics)</a>
      </div>
      <div class="call">
        <h3>Printable season schedule</h3>
        <p>One page, folds in a pocket. This is the sheet to hand out at other clubs' shoots —
          it's how word actually spreads in this sport.</p>
        <a href="#" class="btn btn-out btn-sm">Season schedule PDF <span class="tbd">to build</span></a>
      </div>
    </div>

    <div class="note">
      <strong>How the year runs.</strong> Indoor league starts the first Thursday in January and runs
      ten weeks. The banquet is in early February, and the Brush Shoot — our indoor 3D shoot —
      lands a week after it. The two outdoor 3D shoots come in the spring once the course is set. The
      outdoor 3D league starts the first Wednesday in June and runs ten weeks through the summer.
      Monthly meetings carry on year round: third Wednesday June through December, third Thursday
      January through May.
    </div>

    <div class="note">
      <strong>Course setup and teardown days aren't on here yet.</strong> The 3D course goes up in the
      spring and comes down in the fall, and that's members turning out with tools and a trailer. Once
      the dates are set they'll appear on this page like everything else.
      <span class="tbd">needs dates</span>
    </div>

    <h2 id="first-time" style="margin-top:56px">First time at a shoot?</h2>
    <p class="lead" style="max-width:46em">Everything worth knowing before you drive out.</p>

    <div class="grid g2" style="margin-top:26px">
      <div class="card card-pad">
        <h3>How a 3D shoot works</h3>
        <p>Show up any time inside the posted hours, pay at the clubhouse and get a scorecard. Then
          walk the course &mdash; 40 foam animal targets set along trails through the woods, at
          distances you judge yourself. The scoring rings sit in the vitals; the tighter the ring you
          hit, the more points.</p>
        <p>You go at your own pace with whoever you came with. There's no start gun and no assigned
          groups. Most people take two to three hours and stop at the food stand somewhere in the
          middle. At the end you turn in your card.</p>
        <p style="margin-bottom:0">Nobody there is going to laugh at your first score. Half of them
          can tell you exactly what they shot the first time and it wasn't good either.</p>
      </div>
      <div class="card card-pad">
        <h3>What to bring</h3>
        <p>Your own bow and arrows, <strong>field points only</strong> &mdash; broadheads tear foam
          targets apart. Bring your release if you shoot compound.</p>
        <ul class="tick" style="margin-bottom:0">
          <li><strong>Cash</strong> for the door fee and the food stand. Card readers are hit or miss out here.</li>
          <li><strong>Boots</strong> for the outdoor course. It's timber, and it's often wet.</li>
          <li><strong>Bug spray</strong> May through August. This is not optional in June.</li>
        </ul>
      </div>
      <div class="card card-pad">
        <h3>What it costs</h3>
        <div class="kv" style="margin:0">
          <div><dt>Posted shoots</dt><dd>$<span data-club="shootFee">15</span> per person</dd></div>
          <div><dt>Guest of a member</dt><dd>$<span data-club="guestFee">5</span> to shoot the course</dd></div>
          <div><dt>Membership</dt><dd>$<span data-club="dues">25</span> a year, single or family</dd></div>
          <div><dt>League entry</dt><dd>$40 indoor &middot; $35 outdoor, per 10-week season</dd></div>
        </div>
      </div>
      <div class="card card-pad">
        <h3>Walk-through shooting</h3>
        <p>Our 3D shoots are walk-through: no assigned groups, no start time, turn up inside the posted
          hours. Most people take two to three hours on the 40-target outdoor course; the indoor Brush
          Shoot is quicker.</p>
        <p style="margin-bottom:0">Got a question first? <a href="contact.html">Send us a note</a> and
          somebody who's actually out here will answer it &mdash; what to bring, whether your setup is
          fine, whether to bring the kids.</p>
      </div>
    </div>
  </div>
</section>
""")

# ================================================================
# LEAGUES
# ================================================================
write("leagues.html", "Leagues &amp; Standings",
"Tri-County Archers leagues: a 10-week individual indoor Vegas league starting the first Thursday in January, and a 10-week two-archer-team outdoor 3D league starting the first Wednesday in June. Standings on the page.",
phead("Weekly shooting", "Leagues &amp; Standings",
 "Two leagues, ten weeks each — and you can shoot your score any day of the week.") + """
<section class="sec">
  <div class="wrap">

    <div class="anchor-nav">
      <a href="#leagues">The leagues</a>
      <a href="#formats">Formats</a>
      <a href="#standings">Standings</a>
      <a href="#shoots">Shoot results</a>
      <a href="#archive">Past seasons</a>
    </div>

    <div class="call call-forest" style="margin-bottom:34px">
      <h3>You don't have to shoot on league night</h3>
      <p style="margin-bottom:0">Most people do — it's more fun with a crowd. But if league night is
        when you work, or the kid has practice, or you'd rather have the course to yourself some other
        day: <strong>shoot your score whenever it's convenient during the week.</strong>
        It counts the same. That's the answer to almost every reason people give for not joining a league.</p>
    </div>

    <div class="grid g2" id="leagues"></div>

    <h2 id="formats" style="margin-top:56px">Formats, explained</h2>
    <p class="lead" style="max-width:46em">The vocabulary you'll hear around here, in one place.</p>

    <div class="grid g2" style="margin-top:26px">
      <div class="card card-pad">
        <h3>30-arrow Vegas</h3>
        <p>Thirty arrows at 20 yards on the Vegas three-spot face — three small targets stacked
          vertically, one arrow into each. Inner ring scores 10, so a perfect round is 300. It's the
          round most indoor tournaments in the country use, which makes it a good one to keep sharp on.</p>
        <p class="small muted" style="margin-bottom:0">This is what our indoor league shoots —
          ten weeks starting the first Thursday in January, shot individually.</p>
      </div>
      <div class="card card-pad">
        <h3>3D, unknown distance</h3>
        <p>Foam animal targets set through the timber at unmarked ranges. You judge the distance
          yourself — that's most of the skill, and it's why 3D translates to hunting better than
          anything shot on a flat lane. Scoring rings sit in the vitals.</p>
        <p class="small muted" style="margin-bottom:0">Our outdoor league shoots this in <strong>teams of
          two</strong> over ten weeks — 14 targets, two arrows each, 20 points possible per arrow, 560
          possible for the week — and the league is decided on total points. Field points only —
          broadheads destroy foam targets.</p>
      </div>
      <div class="card card-pad">
        <h3>Brush shoot</h3>
        <p>An indoor 3D course. Brush and trees get hauled into the clubhouse and twenty-eight targets
          get set through them, so you're shooting short, tight, awkward-angle shots through cover
          instead of down an open lane.</p>
        <p class="small muted" style="margin-bottom:0">Ours is
          <span data-event-date="Brush Shoot">February 13–14, 2027</span>, and it's open to
          the public.</p>
      </div>
      <div class="card card-pad">
        <h3>Classes</h3>
        <p>Leagues usually split shooters into classes by equipment and age so a first-year archer
          isn't scored head-to-head against somebody with a scope and a twenty-year habit.</p>
        <p class="small muted" style="margin-bottom:0">Tri-County's class breakdown isn't listed here
          yet. Tell the league coordinator what you shoot and they'll sort you out.
          <span class="tbd">needs the club's class list</span></p>
      </div>
    </div>

    <div class="note" style="margin-top:38px">
      <strong>Not sure which one to shoot?</strong> If you hunt and want to hold your form through the
      winter, the indoor Vegas league is the one — ten weeks of 20-yard discipline while there's snow
      on the ground. If you'd rather be outside and would rather judge yardage than count X's, the
      outdoor 3D league runs the course all summer. Plenty of people shoot both.
    </div>

    <!-- STANDINGS -->
    <h2 id="standings" style="margin-top:64px">Standings</h2>
    <p class="lead" style="max-width:46em">Updated weekly through the season, right here on the page.
      The outdoor league is shot in teams of two and decided on total points; the indoor league is
      individual.</p>

    <div class="note">
      <strong>Summer 2026 outdoor league standings are in below.</strong> Indoor league standings go
      up here once that season starts.
    </div>

    <div id="results" style="margin-top:38px"></div>

    <div class="note">
      <strong>One thing worth knowing about our standings.</strong> Because members can shoot their
      league score any day of the week, scores come in out of order. These tables are built around
      <em>week numbers</em> rather than dates, so a score shot on a Sunday counts for that week the
      same as one shot on league night.
    </div>

    <h2 id="shoots" style="margin-top:52px">Shoot results</h2>
    <p class="muted" style="max-width:44em">Results from the Brush Shoot and the two outdoor 3D shoots
      go up within a few days of each one.</p>
    <div class="tbl-wrap">
      <table class="t stack">
        <thead><tr><th>Date</th><th>Shoot</th><th class="num">Entries</th><th>Results</th></tr></thead>
        <tbody id="shoot-results"></tbody>
      </table>
    </div>

    <h2 id="archive" style="margin-top:52px">Past seasons</h2>
    <div class="grid g4">
      <div class="card card-pad"><h3 style="margin-bottom:4px">2025–26</h3><p class="small muted" style="margin:0">Both leagues <span class="tbd">to load</span></p></div>
      <div class="card card-pad"><h3 style="margin-bottom:4px">2024–25</h3><p class="small muted" style="margin:0">Both leagues <span class="tbd">to load</span></p></div>
      <div class="card card-pad"><h3 style="margin-bottom:4px">2023–24</h3><p class="small muted" style="margin:0">Both leagues <span class="tbd">to load</span></p></div>
      <div class="card card-pad"><h3 style="margin-bottom:4px">Older</h3><p class="small muted" style="margin:0">Whatever the club has kept</p></div>
    </div>

  </div>
</section>
""")

# ================================================================
# CONTESTS
# ================================================================
write("contests.html", "Contests",
"Tri-County Archers member contests \u2014 Big Buck for bow and gun, and Fall Turkey. $10 to enter and the winner takes the pot.",
phead("Member contests", "Contests",
 "Season-long contests for members. Ten dollars in, winner takes the pot.") + """
<section class="sec">
  <div class="wrap">

    <div class="grid g2" id="contests"></div>

    <div class="call call-forest" style="margin-top:38px">
      <h3>How to enter</h3>
      <p>Contests are open to <strong>members</strong>, and entry is <strong>$10</strong> each. Everybody
        who pays in builds the pot, and the winner takes the whole thing &mdash; so the more people who
        enter, the better it gets.</p>
      <p>Bow and gun run as separate contests with separate pots, so you can enter one or both. Sign up
        at a league night, at a monthly meeting, or send us a note and we'll tell you who to pay.</p>
      <p style="margin-bottom:0">
        <a href="contact.html" class="btn btn-forest btn-sm">Email the club</a>
        <span class="tbd">entry deadline and who collects to confirm</span></p>
    </div>

    <div class="note" style="margin-top:34px">
      <strong>Other promotions come up through the year.</strong> Raffles, side pots at a shoot,
      one-off contests somebody thinks up at a meeting. When they do, they land on this page rather
      than living and dying in a Facebook post.
    </div>

  </div>
</section>
""")

# ================================================================
# MEMBERSHIP
# ================================================================
write("membership.html", "Membership",
"Tri-County Archers membership is $25 a year for a single or family membership, with no work-hour requirement. Membership runs with the calendar year.",
phead("Join", "Become a Member",
 "Twenty-five dollars a year, single or family, no work-hour requirement. The whole thing, printed on the page.") + """
<section class="sec">
  <div class="wrap">

    <div class="split" style="margin-bottom:52px">
      <div>
        <div class="eyebrow">What it costs</div>
        <h2>Twenty-five dollars.<br>That's the whole thing.</h2>
        <p class="lead">Single or family, same price, running with the calendar year — and no
          work-hour requirement to keep track of.</p>
        <ul class="tick">
          <li><strong>$25 a year</strong> — and a family membership costs the same as a single one</li>
          <li><strong>No required work hours</strong>, and no bill at the end of the year for hours you didn't work</li>
          <li><strong>Bring a guest</strong> out to shoot the course for $5</li>
          <li><strong>Shoot both leagues</strong> at member entry — $40 indoor, $35 outdoor, ten weeks each</li>
          <li><strong>Enter the member contests</strong> — Big Buck and Fall Turkey, $10 each</li>
          <li><strong>A say in how the place runs</strong> at the monthly meetings</li>
        </ul>
      </div>
      <div class="split-img">
        <img src="assets/img/flag-sunset.jpg" alt="Sunset over the flagpole at the Tri-County Archers grounds">
      </div>
    </div>

    <h2 id="dues">Dues</h2>
    <p class="muted" style="max-width:44em">Membership runs with the <strong>calendar year</strong> —
      January through December.</p>
    <div class="tbl-wrap">
      <table class="t stack">
        <thead><tr><th class="center">Level</th><th class="center">Dues / year</th><th>Notes</th></tr></thead>
        <tbody id="dues-body"></tbody>
      </table>
    </div>

    <div class="call" style="margin-top:34px">
      <h3>What members actually do around here</h3>
      <p>There's no work-hour requirement — but the course doesn't set itself. Members turn out to put
        the 3D course up in the spring and take it down in the fall, work the shoots, cut the grass,
        and generally keep the place looking like somewhere you'd want to bring your kids.</p>
      <p style="margin-bottom:0">Nobody's counting hours or sending you a bill. Show up when you can;
        it's how ninety years of this has worked.</p>
    </div>

    <h2 id="how" style="margin-top:56px">How to join</h2>
    <ol class="steps" style="margin-bottom:44px">
      <li>
        <h3>Fill out an application</h3>
        <p>Use the form below, or download the paper version and bring it out with you. Either way it
          lands with the membership chair.</p>
      </li>
      <li>
        <h3>Or just come to a meeting</h3>
        <p>Monthly meetings run <strong data-club="meeting">third Wednesday June–December, third Thursday
          January–May, 7:00–8:00 pm</strong> at the clubhouse. Turn up, meet people, sign up in person.
          Next one: <strong data-next="meeting">—</strong>.</p>
      </li>
      <li>
        <h3>Pay your $25</h3>
        <p>Check by mail, or in person at a league night or a meeting. Online payment for renewals is
          something we can add later. <span class="tbd">to set up</span></p>
      </li>
    </ol>

    <h2 id="youth">Youth and new archers</h2>
    <div class="grid g2" style="margin:22px 0 44px">
      <div class="card card-pad">
        <h3>Getting a kid started</h3>
        <p><strong>Grant County 4-H Shooting Sports holds its archery practices at Tri-County</strong>,
          and <strong>all the equipment is provided</strong> — a kid needs nothing but shoes.
          Practices run Sunday afternoons through the winter and spring, and 4-H covers air rifle,
          air pistol, .22 and shotgun alongside archery.</p>
        <p style="margin-bottom:0">Sign-up goes through Grant County 4-H rather than through the club
          — enrollment is via 4hOnline, with an April 1 project deadline if you want to shoot
          the county fair competition. <a href="https://grant.extension.wisc.edu/" target="_blank" rel="noopener noreferrer">Grant County
          UW-Extension</a> has the details, or <a href="contact.html">send us a note</a> and we'll point
          you at the right person.
          <span class="tbd">confirm the current 4-H contact before publishing</span></p>
      </div>
      <div class="card card-pad">
        <h3>New to archery, or at the university</h3>
        <p>The <a href="https://www.facebook.com/UWPlattevillePioneerSportmansClub/" target="_blank" rel="noopener noreferrer">UW-Platteville
          Pioneer Sportsman's Club</a> runs an archery league and keeps gear its members can borrow.
          It meets on campus and it's the easy way in if you're a student.</p>
        <p style="margin-bottom:0">Otherwise, the
          <a href="schedule.html#first-time">first-time section on the schedule page</a> covers what to
          bring, how a 3D shoot works and what it costs — and
          <a href="range.html#safety">range safety is on the Range page</a>.</p>
      </div>
    </div>

    <div class="grid g2">
      <div>
        <h2 id="apply" style="margin-bottom:6px">Application</h2>
        <p class="muted small" style="margin-bottom:20px">Fill this in and hit submit — it opens your
          email app with everything already written out, addressed to the club. Nothing sends until
          you press send yourself.</p>
        <form class="form" id="apply">
          <div class="fg fg-2">
            <div><label for="fn">First name</label><input id="fn" required></div>
            <div><label for="ln">Last name</label><input id="ln" required></div>
          </div>
          <div class="fg fg-2">
            <div><label for="em">Email</label><input id="em" type="email" required></div>
            <div><label for="ph">Phone</label><input id="ph" type="tel"></div>
          </div>
          <div class="fg"><label for="ad">Mailing address</label><input id="ad"></div>
          <div class="fg fg-2">
            <div>
              <label for="lv">Membership</label>
              <select id="lv">
                <option>Single — $25</option>
                <option>Family — $25</option>
              </select>
            </div>
            <div><label for="hh">Family members (if family)</label><input id="hh" placeholder="Names, if you're signing up a household">
              <div class="hint">Same $25 either way — this is just so we know who's out here.</div></div>
          </div>
          <div class="fg">
            <label for="ex">What do you shoot?</label>
            <textarea id="ex" rows="3" placeholder="Compound, recurve, first bow arriving next week — whatever's true. Helps us point you at the right league."></textarea>
          </div>
          <button class="btn btn-blaze" type="submit">Submit application</button>
        </form>
        <div class="call hide" id="apply-done" style="margin-top:20px">
          <h3>Your email app should be opening.</h3>
          <p>Everything you filled in is in the message, addressed to the club. Give it a read and
            press send.</p>
          <p style="margin-bottom:0" class="small muted">Nothing happened? Some browsers and webmail
            setups block this. Email the club directly at
            <a data-club-email href="#">tricountyarcheryclub@gmail.com</a>, or use the paper
            application to the right.</p>
        </div>
      </div>

      <div>
        <h2 style="margin-bottom:6px">Prefer paper?</h2>
        <p class="muted small" style="margin-bottom:20px">Plenty of members do.</p>
        <div class="card card-pad" style="margin-bottom:20px">
          <h3>Download the application</h3>
          <p>Print it, fill it out, and mail it with a check or hand it in at a meeting.</p>
          <p class="small muted">We'll build this as a PDF — never a Word file, since those won't open
            cleanly on a phone. <span class="tbd">needs the club's current form</span></p>
          <a href="#" class="btn btn-out btn-sm">Membership application (PDF)</a>
        </div>
        <div class="card card-pad">
          <h3>Mail it to</h3>
          <p style="margin-bottom:0">Tri-County Archers<br>
            Attn: Membership<br>
            9145 County Line Rd<br>
            Platteville, WI 53818</p>
        </div>
        <div class="note">
          <strong>Just want to shoot once first?</strong> Every event on the
          <a href="schedule.html">schedule</a> is open to non-members — and if you know somebody who's
          a member, they can bring you out to shoot the course for
          $<span data-club="guestFee">5</span>.
        </div>
      </div>
    </div>
  </div>
</section>
""")

# ================================================================
# CONTACT
# ================================================================
write("contact.html", "Contact Us",
"Contact Tri-County Archers \u2014 send us a note about joining, sponsoring, the youth program or anything else. Address, phone, directions and social.",
phead("Get in touch", "Contact Us",
 "Thinking about joining, sponsoring, or bringing a kid out? Send us a note and somebody will get back to you.") + f"""
<section class="sec">
  <div class="wrap">
    <div class="grid g2">

      <div>
        <h2 style="margin-bottom:6px">Send us a note</h2>
        <p class="muted small" style="margin-bottom:20px">Fill this in and hit the button &mdash; it
          opens your email app with everything already written out and addressed to the club. Nothing
          sends until you press send yourself.</p>

        <form class="form" id="contact">
          <div class="fg"><label for="c-name">Your name</label><input id="c-name" required></div>
          <div class="fg fg-2">
            <div><label for="c-email">Email</label><input id="c-email" type="email" required></div>
            <div><label for="c-phone">Phone <span class="muted">(optional)</span></label><input id="c-phone" type="tel"></div>
          </div>
          <div class="fg">
            <label for="c-topic">What's this about?</label>
            <select id="c-topic">
              <option>Joining the club</option>
              <option>Sponsoring the club</option>
              <option>Youth archery and 4-H</option>
              <option>A shoot or league question</option>
              <option>Using the grounds</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="fg">
            <label for="c-msg">Your note</label>
            <textarea id="c-msg" rows="6" required placeholder="A sentence or two is plenty. If you're new to archery, say so - it helps us point you at the right person."></textarea>
          </div>
          <button class="btn btn-blaze" type="submit">Open email with this filled in</button>
        </form>

        <div class="call hide" id="contact-done" style="margin-top:20px">
          <h3>Your email app should be opening.</h3>
          <p>Everything you typed is in the message, addressed to the club. Give it a read and press
            send.</p>
          <p style="margin-bottom:0" class="small muted">Nothing happened? Some browsers and webmail
            setups block this. Email the club directly at
            <a data-club-email href="#">tricountyarcheryclub@gmail.com</a>, or message us on
            <a href="{FB}" target="_blank" rel="noopener noreferrer">Facebook</a>.</p>
        </div>
      </div>

      <div>
        <h2 style="margin-bottom:6px">Or reach us directly</h2>
        <p class="muted small" style="margin-bottom:20px">Facebook is usually the fastest.</p>

        <div class="card card-pad" style="margin-bottom:18px">
          <h4>Email</h4>
          <p style="font-weight:700;margin-bottom:0"><a data-club-email href="#">tricountyarcheryclub@gmail.com</a></p>
        </div>

        <div class="card card-pad" style="margin-bottom:18px">
          <h4>Phone</h4>
          <p style="font-size:1.2rem;font-weight:700;margin-bottom:4px" data-club="phone">###-###-####</p>
          <p class="small muted" style="margin:0">Real number still to come.
            <span class="tbd">number needed</span></p>
        </div>

        <div class="card card-pad" style="margin-bottom:18px">
          <h4>Social</h4>
          <p style="font-weight:700;margin-bottom:4px">
            <a href="{FB}" target="_blank" rel="noopener noreferrer">Facebook</a> &middot; <a href="{IG}" target="_blank" rel="noopener noreferrer">Instagram</a></p>
          <p class="small muted" style="margin:0">Shoot photos, weather calls and the day-to-day.</p>
        </div>

        <div class="card card-pad" style="margin-bottom:18px">
          <h4>Find us</h4>
          <p style="margin-bottom:12px">Tri-County Archers<br>9145 County Line Rd<br>Platteville, WI 53818</p>
          <a class="btn btn-forest btn-sm" href="{MAPS}" target="_blank" rel="noopener noreferrer">Get directions in Google Maps</a>
          <p class="small muted" style="margin:12px 0 0">Rural address &mdash; the
            <a href="range.html">Range page</a> has written directions and a GPS warning worth reading.</p>
        </div>

        <div class="call call-forest">
          <h3>Or just come to a meeting</h3>
          <p>Third Wednesday June&ndash;December, third Thursday January&ndash;May, 7:00&ndash;8:00 pm at
            the clubhouse. You don't need to be a member to sit in.</p>
          <p style="margin-bottom:0">Next one: <strong data-next="meeting">&mdash;</strong></p>
        </div>
      </div>

    </div>

    <div class="grid g3" style="margin-top:44px">
      <div class="card card-pad">
        <h3>Thinking about joining?</h3>
        <p>Dues, what members do, and an application you can fill in now.</p>
        <a href="membership.html" class="btn btn-out btn-sm">Membership</a>
      </div>
      <div class="card card-pad">
        <h3>Thinking about sponsoring?</h3>
        <p>What a sponsorship gets you, and what the banquet raffle is worth.</p>
        <a href="sponsors.html" class="btn btn-out btn-sm">Sponsors</a>
      </div>
      <div class="card card-pad">
        <h3>Want to come shoot?</h3>
        <p>Every event on the schedule is open to non-members.</p>
        <a href="schedule.html" class="btn btn-out btn-sm">Schedule</a>
      </div>
    </div>
  </div>
</section>
""")

# ================================================================
# RANGE & DIRECTIONS
# ================================================================
write("range.html", "Range &amp; Directions",
"Directions to Tri-County Archers at 9145 County Line Rd, Platteville WI — indoor range, 40-target outdoor 3D course, clubhouse.",
phead("The place", "Range &amp; Directions",
 "9145 County Line Rd, Platteville, WI 53818. Rural address — read the written directions, not just the GPS.") + f"""
<section class="sec">
  <div class="wrap">

    <div class="grid g4" style="margin-bottom:44px">
      <div class="card card-pad center"><h3 style="color:var(--forest);font-size:2.2rem;margin-bottom:2px" data-club="targetsOutdoor">40</h3><p class="small muted" style="margin:0">Targets on the outdoor 3D course</p></div>
      <div class="card card-pad center"><h3 style="color:var(--forest);font-size:2.2rem;margin-bottom:2px" data-club="targetsIndoor">28</h3><p class="small muted" style="margin:0">Indoor targets set for the Brush Shoot</p></div>
      <div class="card card-pad center"><h3 style="color:var(--forest);font-size:2.2rem;margin-bottom:2px">20 yd</h3><p class="small muted" style="margin:0">Indoor range — lane count <span class="tbd">needed</span></p></div>
      <div class="card card-pad center"><h3 style="color:var(--forest);font-size:2.2rem;margin-bottom:2px" data-club="founded">1937</h3><p class="small muted" style="margin:0">On this ground since</p></div>
    </div>

    <div class="split" style="margin-bottom:52px">
      <div>
        <div class="eyebrow">Getting here</div>
        <h2>Driving directions</h2>
        <p><strong>From Platteville</strong> — north on Highway 81 about nine miles, then east on
          County Road A to County Line Road and south. The club is just outside Arthur, heading
          toward Rewey.</p>
        <p class="small muted">Those are the directions Grant County tourism and Grant County 4-H both
          publish for this address, so they're the ones people actually use.
          <span class="tbd">club to confirm and add any landmarks worth naming</span></p>
        <p><strong>From Dubuque</strong> — US 151 north to Platteville, then as above.
          <span class="tbd">drive time to confirm</span></p>
        <p><strong>From Dodgeville or Mineral Point</strong> — south and west through Rewey.
          <span class="tbd">needs real directions</span></p>
        <div class="note">
          <strong>Heads up on GPS.</strong> County Line Road is exactly what it sounds like — the line
          between Grant and Iowa counties — and some phones put the pin on the wrong side of it. Look
          for the club sign.
        </div>
        <div class="hero-btns" style="margin-top:20px">
          <a class="btn btn-blaze" href="{MAPS}" target="_blank" rel="noopener noreferrer">Get directions in Google Maps</a>
          <a class="btn btn-out" href="https://maps.google.com/?q=9145+County+Line+Rd,+Platteville,+WI+53818" target="_blank" rel="noopener noreferrer">Just show me the map</a>
        </div>
      </div>
      <div class="split-img">
        <img src="assets/img/banner-sunset.jpg" alt="Flagpole and treeline at the Tri-County Archers grounds at sunset">
      </div>
    </div>

    <h2>The facilities</h2>
    <div class="grid g2" style="margin-top:22px">
      <div class="card">
        <img class="card-img" src="assets/img/indoor-archers.jpg" alt="Archers shooting on the indoor range">
        <div class="card-pad">
          <h3>Indoor range</h3>
          <p>Twenty yards, taped shooting positions, and heat that works in January. This is where the
            Vegas league shoots and where the Brush Shoot gets built every February.</p>
          <p class="small muted" style="margin-bottom:0">Lane count and how members get in outside
            league nights still to be confirmed. <span class="tbd">needed</span></p>
        </div>
      </div>
      <div class="card">
        <img class="card-img" src="assets/img/dino-3d-target.jpg" alt="A 3D target set in the timber on the outdoor course">
        <div class="card-pad">
          <h3>Outdoor 3D course</h3>
          <p>Forty targets set along walking trails through the timber, at unmarked distances. There's a
            raptor and a dinosaur out there — you'll see. Members put the course up in the spring and
            take it down in the fall.</p>
          <p class="small muted" style="margin-bottom:0">Walk-through format, cards at the clubhouse.</p>
        </div>
      </div>
      <div class="card">
        <img class="card-img" src="assets/img/banquet.jpg" alt="Members gathered in the clubhouse at the annual banquet">
        <div class="card-pad">
          <h3>Clubhouse</h3>
          <p>Kitchen and food stand, meeting space, and a bathroom that isn't a portable toilet.
            Monthly meetings, the annual banquet and shoot registration all happen here — and once a
            year it fills up with brush and becomes a 3D course.</p>
          <p class="small muted" style="margin-bottom:0">The club also hosts Grant County 4-H shooting
            practices, the Iowa-Grant Trap Team and Rewey Fire Department trainings.</p>
        </div>
      </div>
      <div class="card card-pad" style="justify-content:center">
        <h3>Course map</h3>
        <p>A clean map of the trail loops and target numbers goes here — useful for first-timers
          and for the people who post shoot photos.</p>
        <p class="small muted">Send a photo of the map posted at the clubhouse, or a hand sketch,
          and I'll redraw it properly. <span class="tbd">needs course map</span></p>
      </div>
    </div>

    <div class="call" style="margin-top:38px">
      <h3>Parking and where to go when you arrive</h3>
      <p style="margin-bottom:0">Go into the clubhouse first to pay and pick up a scorecard, even for a
        walk-through shoot. Somebody will point you at the first stake.
        <span class="tbd">parking details to confirm</span></p>
    </div>

    <h2 id="safety" style="margin-top:56px">Range safety</h2>
    <div class="grid g2" style="margin-top:22px">
      <div class="card card-pad">
        <h3>The short version</h3>
        <ul class="tick" style="margin-bottom:0">
          <li>Never draw a bow without a target in front of it, indoors or out.</li>
          <li>Nobody goes forward of the shooting line until everybody on the line is done.</li>
          <li>On the 3D course, look and call before you walk to a target — trails cross.</li>
          <li>Field points only. Broadheads tear foam targets apart.</li>
          <li>No alcohol on the shooting line, indoor or out.</li>
          <li>Kids stay with an adult on the course.</li>
        </ul>
      </div>
      <div class="card card-pad" style="justify-content:center">
        <h3>Full club rules</h3>
        <p>The complete rules are posted in the clubhouse, and they'll go up here too.</p>
        <p class="small muted" style="margin-bottom:0">Send a photo of the posted sheet and it goes on
          this page. <span class="tbd">needs the club's rules sheet</span></p>
      </div>
    </div>
  </div>
</section>
""")

# ================================================================
# PHOTOS
# ================================================================
write("photos.html", "Photos",
"Photos from Tri-County Archers shoots, leagues and the annual banquet.",
phead("The gallery", "Photos",
 "Shoots, leagues, the Brush Shoot and the annual banquet.") + """
<section class="sec">
  <div class="wrap">
    <div class="anchor-nav">
      <a href="#recent">Around the club</a>
      <a href="#submit">Send us photos</a>
    </div>

    <h2 id="recent">Around the club</h2>
    <div class="gal" style="margin-bottom:52px">
      <figure><img src="assets/img/indoor-archers.jpg" alt="Archers on the indoor line">
        <figcaption>League night on the indoor line</figcaption></figure>
      <figure><img src="assets/img/indoor-3d-Brush-shoot.jpg" alt="Indoor brush shoot course">
        <figcaption>The Brush Shoot, built inside the clubhouse</figcaption></figure>
      <figure><img src="assets/img/dino-3d-target.jpg" alt="3D target in the timber">
        <figcaption>Not every target on the course is a whitetail</figcaption></figure>
      <figure><img src="assets/img/banquet.jpg" alt="Members at the annual banquet">
        <figcaption>The annual banquet</figcaption></figure>
      <figure><img src="assets/img/flag-sunset.jpg" alt="Flag at sunset over the grounds">
        <figcaption>Summer evening at the club</figcaption></figure>
      <figure><img src="assets/img/arrows.jpg" alt="Arrows in a quiver">
        <figcaption>Feathers and vanes on the indoor line</figcaption></figure>
      <figure><img src="assets/img/buck-mounts-indoors.jpg" alt="Mounts on the clubhouse wall">
        <figcaption>Inside the clubhouse</figcaption></figure>
      <figure><img src="assets/img/see-you-at-the-club.jpg" alt="See you at the club">
        <figcaption>See you at the club</figcaption></figure>
    </div>

    <div class="note">
      <strong>This gallery is running on eight photos.</strong> Send 20–40 shots from the last couple
      of seasons — grouped in folders by event and year if you can — and it fills out into something
      worth browsing. The Brush Shoot and the banquet are the two that would earn their own galleries.
      <span class="tbd">needs more photos</span>
    </div>

    <h2 id="submit" style="margin-top:52px">Got photos?</h2>
    <div class="call">
      <p>Anybody who shoots here can send photos in — league nights, shoots, course setup days, kids'
        first arrows, the food stand at seven in the morning.
        <a href="contact.html">Send them through the contact page</a>, or message us on
        <a href="https://www.facebook.com/TriCountyArchers/" target="_blank" rel="noopener noreferrer">Facebook</a> or
        <a href="https://www.instagram.com/tricountyarchers/" target="_blank" rel="noopener noreferrer">Instagram</a>.</p>
      <p style="margin-bottom:0">If you'd rather not be in a photo on the website, tell us and we'll
        take it down, no discussion needed.</p>
    </div>
  </div>
</section>
""")

# ================================================================
# SPONSORS
# ================================================================
write("sponsors.html", "Sponsors",
"The businesses that support Tri-County Archers shoots and the annual banquet raffle, and how to become a club sponsor.",
phead("Support", "Our Sponsors",
 "Our shoots, trophies and the banquet raffle run on local support.") + """
<section class="sec">
  <div class="wrap">
    <div class="note">
      <strong>This page is a frame waiting for a list.</strong> Send sponsor names, logos and web
      addresses and it fills in. The tier structure and prices below are a starting point for the
      board to work from. <span class="tbd">needs sponsor list</span>
    </div>

    <div class="tier" style="margin-top:40px">
      <div class="tier-name">Bullseye Sponsors</div>
      <div class="spons">
        <div class="spon">Logo</div><div class="spon">Logo</div><div class="spon">Logo</div>
      </div>
    </div>
    <div class="tier">
      <div class="tier-name">Gold Sponsors</div>
      <div class="spons">
        <div class="spon">Logo</div><div class="spon">Logo</div><div class="spon">Logo</div><div class="spon">Logo</div>
      </div>
    </div>
    <div class="tier">
      <div class="tier-name">Supporting Sponsors</div>
      <div class="spons">
        <div class="spon">Name</div><div class="spon">Name</div><div class="spon">Name</div>
        <div class="spon">Name</div><div class="spon">Name</div><div class="spon">Name</div>
      </div>
    </div>

    <h2 id="become" style="margin-top:20px">Become a sponsor</h2>
    <p class="lead" style="max-width:46em">Sponsorship isn't a donation — it puts your name in front of
      the archers and families who come through here for three shoots a year, two leagues, and a
      banquet that fills the hall.</p>
    <div class="grid g3" id="tiers" style="margin:26px 0 34px"></div>

    <!-- IDEAS (temporary working block — remove before launch) -->
    <div style="margin:6px 0 34px; padding:20px 22px; background:#FFF8E8; border:2px dashed #C08A16; border-radius:14px">
      <p style="margin:0 0 16px; color:#6B5111; font-size:.92rem">
        <strong style="color:#4E3A08">Working ideas — not published yet.</strong> A scratch list of
        sponsorship mechanisms for the board to sort through, on top of the recommended tiers above.
        Keep, drop or rework these before any of it goes to a business.
        <span class="tbd">internal — remove before launch</span></p>

      <div class="grid g2">
        <div class="card card-pad">
          <h3>Placement &amp; signage</h3>
          <ul class="tick" style="margin-bottom:0">
            <li><strong>Sponsor a target</strong> — a sign or plaque at a specific target on the 3D
              course carrying the sponsor's name, renewed each year</li>
            <li><strong>Title a shoot</strong> — "Brush Shoot, presented by ___" on the banner, the
              schedule and the posts</li>
            <li><strong>Year-round clubhouse banner</strong> for top-tier sponsors, not just on shoot days</li>
            <li><strong>QR code on target and course signs</strong> pointing straight to the sponsor's site</li>
          </ul>
        </div>
        <div class="card card-pad">
          <h3>Branded keepsakes</h3>
          <p class="small muted" style="margin-top:0">Co-branded with the club logo — something people
            keep, so the sponsor's name travels with it.</p>
          <ul class="tick" style="margin-bottom:0">
            <li>T-shirts</li>
            <li>Can coozies</li>
            <li>Branded poker chips</li>
            <li>Challenge coins</li>
            <li>Hats, stickers or patches as lower-cost options</li>
          </ul>
        </div>
      </div>

      <div class="grid g2" style="margin-top:16px">
        <div class="card card-pad">
          <h3>Raffle &amp; prizes</h3>
          <ul class="tick" style="margin-bottom:0">
            <li><strong>Donate raffle items</strong> for the banquet — the club leans on this, so make
              it an easy, clearly recognized way in</li>
            <li>Signage on each raffle prize crediting the business that donated it</li>
            <li><strong>Back a contest payout or trophy</strong> — Big Buck or Fall Turkey named for the
              sponsor</li>
          </ul>
        </div>
        <div class="card card-pad">
          <h3>Community &amp; youth</h3>
          <ul class="tick" style="margin-bottom:0">
            <li>Back the <strong>Grant County 4-H</strong> program or its equipment and get credited for it</li>
            <li>Sponsor a <strong>league season</strong> — name on the standings and the league posts</li>
          </ul>
        </div>
      </div>

      <div class="grid g2" style="margin-top:16px">
        <div class="card card-pad">
          <h3>In-kind &amp; flexible</h3>
          <ul class="tick" style="margin-bottom:0">
            <li><strong>Count an in-kind donation toward a tier</strong> — a donated $500 bow could
              qualify a business for Bullseye, or whatever tier the value matches</li>
            <li>Recognize <strong>in-kind help</strong> — materials, food, printing — the same as a cash sponsor</li>
            <li>Let sponsors <strong>pick their channel</strong> — signage, keepsakes or raffle — for the
              same tier price</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="grid g2">
      <div class="call call-forest">
        <h3>What sponsors get out of it</h3>
        <p>The <strong>banquet raffle</strong> on
          <span data-event-date="Annual Banquet" data-event-format="monthday">February 6</span> is the
          big one — a room full of members and
          families, and every prize on the table has a name attached to it. That's the clearest return
          a local business gets out of this club.</p>
        <p style="margin-bottom:0">On top of it: the <strong>Brush Shoot</strong> in February and
          <strong>two outdoor 3D shoots</strong> in the spring, all open to the public and drawing
          people in from across three counties and the river.</p>
      </div>
      <div class="card card-pad">
        <h3>Ready to sign up?</h3>
        <p>Send us a note and we'll come straight back to you with what's available and what it costs.</p>
        <p style="margin-bottom:14px"><a href="contact.html" class="btn btn-blaze btn-sm">Email the club</a></p>
        <p class="small muted">A one-page sponsor form will live here too — the kind you can hand
          to a business owner across a counter. <span class="tbd">to build</span></p>
        <a href="#" class="btn btn-out btn-sm">Sponsor form (PDF)</a>
      </div>
    </div>

    <div class="call" style="margin-top:34px">
      <h3>2027 is the club's 90th year</h3>
      <p style="margin-bottom:0">Tri-County has been on this ground since 1937, which makes the
        February 2027 banquet the 90th-anniversary one. Worth deciding early whether the club wants to
        make something of it — an anniversary is an easier ask than a normal one.</p>
    </div>

  </div>
</section>
""")

# ================================================================
# ABOUT & CONTACT
# ================================================================
write("about.html", "About the Club",
"About Tri-County Archers — established 1937 as the Iowa-Grant Conservation Club. Board, meeting schedule, the groups who use our grounds, and the groups who use our grounds.",
phead("The club", "About the Club",
 "Who we are, who runs it, when we meet, and who else uses these grounds.") + """
<section class="sec">
  <div class="wrap">

    <div class="split" style="margin-bottom:52px">
      <div>
        <div class="eyebrow">Established <span data-club="founded">1937</span></div>
        <h2>Ninety years<br>on this ground.</h2>
        <p>Tri-County Archers started in <strong>1937 as the Iowa-Grant Conservation Club</strong>.
          The name it carries now comes from the corner of Wisconsin where Grant, Iowa and Lafayette
          counties meet — it's right there in the logo, wrapped around an archer at full draw.</p>
        <p>It's still run the same way it always was: entirely by its members, on volunteer time.
          Bowhunters keeping sharp through the winter, people chasing indoor scores, kids on 4-H
          equipment, and a good number who mostly come for the coffee and the arguing.</p>
        <p class="small muted">The middle of the story is the part we don't have written down. When the
          name changed, when the clubhouse went up, how the 3D course came to be, who's remembered. If
          somebody has the old minutes, a club history sheet, or a photo of an Iowa-Grant Conservation
          Club sign, that's the good stuff and it belongs here — especially with the 90th year coming
          up in 2027. <span class="tbd">needs club history</span></p>
      </div>
      <div class="split-img">
        <img src="assets/img/logo-dark.png" alt="Tri-County Archers logo" style="aspect-ratio:1;object-fit:contain;background:#fff;padding:34px">
      </div>
    </div>

    <h2 id="board">Board &amp; officers</h2>
    <p class="muted" style="max-width:44em">Who to ask about what.
      <span class="tbd">needs names and contacts</span></p>
    <div class="tbl-wrap" style="margin-bottom:44px">
      <table class="t stack">
        <thead><tr><th>Role</th><th>Name</th><th>Contact</th><th>What they handle</th></tr></thead>
        <tbody>
          <tr><td data-l="Role"><strong>President</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Runs meetings, speaks for the club</td></tr>
          <tr><td data-l="Role"><strong>Vice President</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Shoots and the banquet</td></tr>
          <tr><td data-l="Role"><strong>Secretary</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Minutes, membership records, this website</td></tr>
          <tr><td data-l="Role"><strong>Treasurer</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Dues, sponsors, the books</td></tr>
          <tr><td data-l="Role"><strong>Membership Chair</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Applications and renewals</td></tr>
          <tr><td data-l="Role"><strong>Grounds Chair</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Course setup and teardown, mowing, upkeep</td></tr>
          <tr><td data-l="Role"><strong>Indoor League Coordinator</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">Vegas league scores and standings</td></tr>
          <tr><td data-l="Role"><strong>Outdoor League Coordinator</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">—</td><td data-l="Handles">3D league scores and standings</td></tr>
          <tr><td data-l="Role"><strong>Contests</strong></td><td data-l="Name"><span class="tbd">name needed</span></td><td data-l="Contact">&mdash;</td><td data-l="Handles">Big Buck and Fall Turkey entries</td></tr>
        </tbody>
      </table>
    </div>

    <div class="grid g2" style="margin-bottom:44px">
      <div class="call call-forest">
        <h3>Monthly meetings</h3>
        <p><strong>June through December</strong> — third Wednesday, 7:00–8:00 pm.<br>
           <strong>January through May</strong> — third Thursday, 7:00–8:00 pm.<br>
           At the clubhouse.</p>
        <p>Next meeting: <strong data-next="meeting">—</strong></p>
        <p style="margin-bottom:0">Attendance is recommended, not required. If you're thinking about
          joining, this is a good night to turn up — you can sign up in person.</p>
      </div>
      <div class="call">
        <h3>Who else uses these grounds</h3>
        <p>Tri-County Archers Club, Inc. is a registered nonprofit
          <span class="tbd">confirm exempt status for the footer</span>, and the property does a lot
          more than archery:</p>
        <ul class="tick" style="margin-bottom:0">
          <li><strong>Iowa-Grant Trap Team</strong> <span class="tbd">needs a contact or link</span></li>
          <li><strong><a href="https://grant.extension.wisc.edu/" target="_blank" rel="noopener noreferrer">Grant County 4-H Shooting Sports</a></strong>
              — archery practices here, equipment provided</li>
          <li><strong><a href="https://www.facebook.com/UWPlattevillePioneerSportmansClub/" target="_blank" rel="noopener noreferrer">UW-Platteville
              Pioneer Sportsman's Club</a></strong></li>
          <li><strong><a href="https://www.facebook.com/SWWCHC/" target="_blank" rel="noopener noreferrer">Southwestern Wisconsin Coon Hunters
              Club</a></strong></li>
          <li><strong><a href="https://www.facebook.com/ReweyFire/" target="_blank" rel="noopener noreferrer">Rewey Fire Department</a></strong>
              — trainings on the property</li>
        </ul>
      </div>
    </div>

    <div class="grid g2">
      <div class="card card-pad">
        <h3>Get in touch</h3>
        <p>Questions about joining, sponsoring, the youth program or anything else — the contact
          page gets it to the right person.</p>
        <p style="margin-bottom:0"><a href="contact.html" class="btn btn-blaze btn-sm">Contact the club</a></p>
      </div>
      <div class="card card-pad">
        <h3>Seven Oaks Archery</h3>
        <p>Our neighbours down the road. Worth a look if you're chasing a shoot on a weekend we're not
          running one.</p>
        <p style="margin-bottom:0"><a href="https://www.facebook.com/SevenOaksArcheryinc" target="_blank" rel="noopener noreferrer">Seven Oaks
          Archery on Facebook</a></p>
      </div>
    </div>
  </div>
</section>
""")

for gone in ("new-archers.html", "results.html"):
    _p = os.path.join(OUT, gone)
    if os.path.exists(_p):
        os.remove(_p)
        print("removed", gone)

print("\nBuild complete.")

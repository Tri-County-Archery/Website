# Tri-County Archers — Website Plan

**Club:** Tri-County Archers Club, Inc. — 9145 County Line Rd, Platteville, WI 53818
**Established:** 1937, as the **Iowa-Grant Conservation Club**
**Counties:** Grant · Iowa · Lafayette (it's in the logo)
**Social:** [Facebook](https://www.facebook.com/TriCountyArchers/) · [Instagram](https://www.instagram.com/tricountyarchers/)
**Other web presence:** an empty venue stub on [wiarchery.com](https://wiarchery.com/venue/tri-county-archers/)
**Status:** All ten pages built, and **the real club facts in §2 are live on the site** (§8). Every date is confirmed and internally consistent, the club email is real, and shoot fees are set. What's left is the club phone number, board names, and scores (§7).
**Updated:** August 23, 2026

> **Where this stands.** The first draft filled every unknown with a plausible guess, each tagged
> yellow **guess** on the page. Dustin has since supplied the real schedule, dues, league structure,
> history and affiliations — that's §2, and it's now applied to the site. §7 is what's still
> genuinely unknown; §8 records what changed and how the site keeps itself honest about the rest.

---

## 1. What we're trying to accomplish

Five jobs, in priority order:

1. **Answer "what's happening and when"** — the #1 reason anyone visits a club site. Right now that answer only exists in Facebook posts, which are unsearchable and invisible to non-users.
2. **Convert curious locals into members** — publish dues and the join process openly, with an online application. At **$25/year with no work-hour requirement**, TCA has the easiest yes in the state. That's the headline.
3. **Serve current members** — league standings, meeting dates, weather cancellations, work-day calls.
4. **Make sponsors visible** — a real page that makes banquet sponsorship worth paying for.
5. **Show the club is alive** — photos, results that were updated last week and not last year.

### Research basis
I surveyed 12 Wisconsin club/league sites (Racine Instinctive Bowmen, West Allis Bowmen, Rib Mountain Bowmen, South Central Wisconsin Archers in Monroe, Kenosha Bowmen, Eau Claire Archers, Janesville Bowmen, Horicon Marsh Archers, Chippewa Bow Hunters, Blackhawk Bowhunters, Beloit Field Archers, KMFAL). The plan below copies what they do well and fixes what nearly all of them get wrong. Full source list at the bottom.

**What almost all of them do badly — our openings:**

| Common failure | Seen at | Our fix |
|---|---|---|
| Stale "upcoming events" showing months-old dates | SCWA, Janesville | One data file drives the homepage; nothing is typed twice |
| Schedule described on one page, dates on another | West Allis, Rib Mountain | One canonical schedule page, one source of truth |
| Results published as raw .xlsx / .docx downloads | Horicon (8 weekly xlsx files), RIB, West Allis | HTML tables on the page; PDF only as a printable extra |
| No dues prices — download the PDF to find out | RIB, Horicon, West Allis | Full price table in plain HTML |
| Work-hour obligations buried, then billed as a surprise | Kenosha ($50/hr), Horicon ($35/hr) | **Not an issue here — TCA has no work-hour requirement, which is a genuine differentiator worth saying out loud** |
| Not feeding wiarchery.com | Tri County today | Post every shoot there — free statewide distribution |
| No email list; Facebook-only | 10 of 12 | Newsletter signup in the footer of every page |

---

## 2. Club facts — confirmed

This section is the source of truth. Everything else in the plan, and everything in
`site/assets/js/data.js`, should trace back to here.

### 2.1 The club

| | |
|---|---|
| **Established** | 1937, as the **Iowa-Grant Conservation Club** |
| **Address** | 9145 County Line Rd, Platteville, WI 53818 |
| **Facebook** | https://www.facebook.com/TriCountyArchers/ |
| **Instagram** | https://www.instagram.com/tricountyarchers/ |
| **Nonprofit** | Tri County Archers Club, Inc. — registered nonprofit, EIN 39-1401126 ([ProPublica](https://projects.propublica.org/nonprofits/organizations/391401126)) |

**1937 means 2027 is the club's 90th anniversary.** That is a real hook — for the banquet, for a
sponsor push, for a "90 years" page, and for local press. Worth deciding early whether to build the
2027 season around it.

### 2.2 Membership

- **Membership year runs with the calendar year** (January–December).
- **$25/year — single or family, same price.**
- **No work-hour requirement.** Active members do pitch in: setting up and tearing down the 3D
  course, working shoots, cutting grass, and general upkeep to keep the place looking good. It's
  culture, not an invoice.
- **Guests:** a member may bring a non-member to shoot for **$5 per guest**.
- **How to join:** apply through the website, or come to one of the monthly meetings.
- **Non-members** are welcome at any posted event on the schedule.

The $25 / no-hours combination is the strongest membership pitch in the state. Every other club I
looked at is $55–$205 with 12+ billable work hours. Lead with it.

### 2.3 Leagues

Both leagues run **10 weeks**. Most people shoot on league night, but **members may shoot their
score any time during the week that's convenient** — that flexibility is unusual and should be said
plainly on the Leagues page, because it removes the main reason people don't sign up.

| | Indoor League | Outdoor League |
|---|---|---|
| **Round** | 30-arrow Vegas — 300 possible | 14 targets, 2 arrows each, 20 pts/arrow — **560 possible per week** |
| **Format** | **Individual** | **Two-archer teams**, decided on **total points** |
| **Length** | 10 weeks | 10 weeks |
| **Entry** | **$40** | **$35** |
| **Starts** | First **Thursday** in January — **Jan 7, 2027** | First **Wednesday** in June — **Jun 2, 2027** |
| **Ends** | Week of **Mar 11, 2027** | Week of **Aug 4, 2027** |
| **Shoot-any-day** | Yes | Yes |

**The outdoor league is a team league, and that matters for the standings.** Two archers per team;
each archer's average counts only the weeks they actually shot, but **the league is decided on total
points**. Those two measures can disagree — see §4.3.

**The league's 14-target course is separate from the 40-target course used for the two public
outdoor 3D shoots** — a shorter loop for a weekly night, not the same walk. Confirmed: the top score
in the 2026 data (550) checks out cleanly at 98% of the 560 possible, which is exactly the range a
strong week should land in.

### 2.4 Shoots

Three per year — one indoor, two outdoor.

| Shoot | Format | Targets | Next date |
|---|---|---|---|
| **Brush Shoot** | Indoor 3D | **28** | **Feb 13–14, 2027** (Sat–Sun) |
| **Outdoor 3D #1** | Outdoor 3D | **40** | **Apr 3–4, 2027** (Sat–Sun) |
| **Outdoor 3D #2** | Outdoor 3D | **40** | **May 22, 2027** (Sat) |

### 2.5 Banquet

Annual banquet with **raffles from local sponsors, food, drink and fellowship**.
**Next: February 6, 2027** (Saturday).

This is the sponsor engine. The Sponsors page should point at the banquet raffle explicitly — that's
what a local business is actually buying.

### 2.6 Monthly meetings

Attendance is **recommended, not mandatory**. Prospective members are welcome to come to one.

| Season | Night | Time |
|---|---|---|
| **June – December** | 3rd **Wednesday** | 7:00 – 8:00 pm |
| **January – May** | 3rd **Thursday** | 7:00 – 8:00 pm |

### 2.7 Affiliations and groups that use the grounds

TCA hosts and partners with more than archers — this is a conservation-club footprint, and it's a
better story than "we shoot bows here." What I was able to verify online:

| Group | What I found |
|---|---|
| **Iowa-Grant Trap Team** | Iowa-Grant School District, Livingston WI. High-school trap in Wisconsin runs through the [Wisconsin State High School Clay Target League](https://wi.usaclaytarget.com/). I could not confirm the team's roster page or coach online — **need a contact and a link from the club.** |
| **4-H Youth Archery Instruction** | **Confirmed.** Grant County 4-H Shooting Sports holds its winter/spring practices at Tri County Archery, 9145 Co Line Rd. Sundays 1:00–3:00 pm, roughly monthly Feb–May. Disciplines: air rifle, air pistol, archery, .22 rifle, shotgun. **All equipment is provided.** Enrollment via 4hOnline by April 1; two practices required to shoot the fair competition. Contacts listed as Rhonda Hughey (778-8415) and Dave Vosberg (943-8492). Source: [Grant County 4-H Echo newsletter](https://grant.extension.wisc.edu/files/2025/02/February-March-2025-Echo.pdf) |
| **UW-Platteville Pioneer Sportsman's Club** | Official name is the **Pioneer Sportsman's Club**. Unites students around clay target, pistol, **archery** and hunting; runs shooting leagues, keeps gear for members to borrow, meets bi-weekly Mondays 6:00 pm in Ottensman Hall. Advisor Julie Durst. [Facebook](https://www.facebook.com/UWPlattevillePioneerSportmansClub/) · [Shooting Sports UWP](https://www.facebook.com/ShootUWP/) |
| **Southwestern Wisconsin Coon Hunters Club** | Full name **Southwestern Wisconsin Coon Hunters Club**, Platteville. Runs UKC coonhound events — bench shows, nite hunts, youth events. [Facebook](https://www.facebook.com/SWWCHC/) |
| **Rewey Fire Department** | Rewey Volunteer Fire Dept & First Responders, 218 West St, Rewey WI 53580 (Iowa County), ~14 volunteers. Uses the grounds for trainings. [Facebook](https://www.facebook.com/ReweyFire/) |

**Note on names:** the draft site lists NFAA / Wisconsin Archery Alliance / Wisconsin Bowhunters as
affiliations. Those were guesses and should come off unless they're real — the list above is the
real one and it's more interesting.

### 2.8 The 2026–27 calendar, assembled

Everything above, in date order. This is what goes into `data.js`.

| Date | Day | Event | Who |
|---|---|---|---|
| Sep 16, 2026 | Wed | Monthly meeting, 7–8 pm | Members |
| Oct 21, 2026 | Wed | Monthly meeting, 7–8 pm | Members |
| Nov 18, 2026 | Wed | Monthly meeting, 7–8 pm | Members |
| Dec 16, 2026 | Wed | Monthly meeting, 7–8 pm | Members |
| **Jan 7, 2027** | **Thu** | **Indoor League week 1** — 30-arrow Vegas, individual, 10 weeks, $40 | Members |
| Jan 21, 2027 | Thu | Monthly meeting, 7–8 pm | Members |
| **Feb 6, 2027** | **Sat** | **Annual Banquet** — raffles, food, drink | — |
| **Feb 13–14, 2027** | Sat–Sun | **Brush Shoot** — indoor 3D, 28 targets | Public |
| Feb 18, 2027 | Thu | Monthly meeting, 7–8 pm | Members |
| Mar 18, 2027 | Thu | Monthly meeting, 7–8 pm | Members |
| Mar 11, 2027 | Thu | Indoor League final week | Members |
| **Apr 3–4, 2027** | Sat–Sun | **Outdoor 3D Shoot #1** — 40 targets | Public |
| Apr 15, 2027 | Thu | Monthly meeting, 7–8 pm | Members |
| May 20, 2027 | Thu | Monthly meeting, 7–8 pm | Members |
| **May 22, 2027** | **Sat** | **Outdoor 3D Shoot #2** — 40 targets | Public |
| **Jun 2, 2027** | **Wed** | **Outdoor League week 1** — 3D course, two-archer teams, 10 weeks, $35 | Members |
| Jun 16, 2027 | Wed | Monthly meeting, 7–8 pm | Members |
| Jul 21, 2027 | Wed | Monthly meeting, 7–8 pm | Members |
| **Aug 4, 2027** | Wed | Outdoor League final week | Members |
| Aug 18, 2027 | Wed | Monthly meeting, 7–8 pm | Members |

Course setup and teardown days aren't dated yet — those are real events members show up for, and
they belong on the calendar. See §7.

---

## 3. Sitemap

Eight top-level items plus the join button. Results folded into Leagues, the first-timer page folded
into Schedule and Membership, and Contact split out to its own page because prospective members and
prospective sponsors both land there.

```
Home
Shoot Schedule
Leagues & Standings
Contests
Range & Directions
Photos
About the Club
Contact Us
   └─ Membership (the "Join the Club" button)
   └─ Sponsors (from Contact and the homepage strip)
```

Footer on every page: address · phone · Google Maps directions · Facebook · Instagram · email
newsletter signup.

---

## 4. Page-by-page content

### 4.1 Home

**A. Weather / cancellation banner** — a slot at the very top, normally hidden. One line + timestamp. Outdoor 3D gets rained out and right now that news lives only on Facebook.

**B. Hero** — the 3D course photo. Club name, "Platteville, Wisconsin · **Est. 1937**", and one sentence of what the club is. Two buttons: **Shoot Schedule** and **Become a Member**.

**C. "What's Next" block** — four cards generated from the schedule data, each with an **Add to Google Calendar** link:

| Card | Shows |
|---|---|
| Next Shoot | Name, dates, format, **Open to the Public** badge, fees |
| Next League | Which league is next, or **which week of the season we're in** if one is running |
| Next Monthly Meeting | Date + 7–8 pm |
| Coming Up | The banquet, or whatever social event is next |

**D. "Three easy ways in"** — the section that replaced "can I just show up." Numbered, in order of how easy they are:

1. **Send us a note** → the Contact page. The lowest-commitment first step, and the one that works at 11pm on a Tuesday.
2. **Come to a monthly meeting** — with the next date shown live.
3. **Come out to a shoot** — every posted event is open to non-members, or come as a member's guest for $5.

Below it, one line on the $25 membership and a pointer to the 4-H youth program.

**E. Three tiles** — Leagues & Standings · Contests · Membership.

**F. Stat row** — 40 outdoor targets · 28 indoor at the Brush Shoot · $25 a year · years on this ground.

**G. Brush Shoot feature** — the club's most distinctive event gets a photo and a paragraph.

**H. Sponsor logo strip** → Sponsors page.

---

### 4.2 Shoot Schedule — the canonical page

One page, one table, whole season, driven by §2.8. Filter chips: **Everything · Open to the public · Members · Outdoor 3D · Indoor · Leagues · Meetings · Past events**.

Each row carries name, dates, hours, cost, an **Open to the Public / Members** badge, and an
**Add to Google Calendar** button. The old Contact column is gone — it only ever held placeholders,
and contact now has a page of its own.

Also on this page:

- **Add to Google Calendar per event**, plus a whole-season **.ics download** for people who'd rather import once
- **Printable one-page season schedule PDF** — clubs hand these out at other clubs' shoots
- A note on the shape of the year, and a note that course setup/teardown days will appear here once dated

**"First time at a shoot?"** — four cards absorbed from what used to be its own page: how a 3D shoot
works, what to bring, what it costs, and what walk-through means. This content belongs next to the
dates rather than on a separate page nobody clicks.

---

### 4.3 Leagues & Standings

Two cards, titled the way members talk:

**Thursday Night Indoor League** — 30-arrow Vegas · individual · 10 weeks · **$40** · starts the first Thursday in January (**Jan 7, 2027**)
**Wednesday Outdoor 3D League** — the 3D course · two-archer teams · 10 weeks · **$35** · starts the first Wednesday in June (**Jun 2, 2027**)

**The box at the top of the page:** *"You don't have to shoot on league night — shoot your score
whenever it's convenient during the week."* That's the single best answer to "I'd join but I work
Thursdays," and it goes above the league cards, not below them.

Plus a **Formats** section explaining a 30-arrow Vegas round, unknown-distance 3D, and what a brush
shoot is.

**Standings live on this page too**, rather than on a separate Results page. A member checking their
score and a visitor reading about the league want the same page, and splitting them meant two clicks
and a stale-looking Results tab between seasons. Anchor nav across the top gets you straight to
standings.

**Summer 2026 outdoor league is live on the page** from the club's spreadsheet — three teams, ten
weeks, real names and scores. Two tables per season:

- **Standings summary** — place, team, archers, **total points**, average. Stacks into cards on a phone.
- **Week-by-week detail** behind a "Week-by-week scores" toggle — every archer's ten weekly scores, total and average. Thirteen columns, so it scrolls inside its own box rather than forcing the page sideways.

Two things the data made clear, both now handled explicitly:

1. **Total points decides the league, and it disagrees with average.** In 2026, Team 1 finished
   *second on average* but *third on total*, because Chris missed three weeks — his average counts
   only the seven he shot, which flatters the team average while the total takes the hit. The table
   ranks on total, marks total as the deciding column, and says so in a line under the table. Ranking
   on the average column would have published the wrong runner-up.
2. **Missed weeks need to be visible.** `X` renders greyed rather than as a zero or a blank, with a
   note explaining that an archer's average covers only the weeks they shot.

Indoor is individual, and shows an empty-state note until that season starts rather than placeholder
names.

- Keyed to **week numbers rather than dates**, because scores arrive out of order when people shoot any day.
- Shoot results table below it, then a per-year archive.
- PDF alongside for printing and pinning up in the clubhouse; the web page stays canonical.

---

### 4.4 Contests

**"Contests" rather than "Promotions."** Promotions reads like discounts and marketing; these are
contests you enter and try to win. The page carries the two standing ones and has room for whatever
else comes up:

- **Big Buck — Bow** — $10, members, archery deer season
- **Big Buck — Gun** — $10, members, gun deer season, separate pot from the bow side
- **Fall Turkey** — $10, members, fall turkey season

**Winner takes the pot.** Everybody who pays in builds it, so the page says the more people enter the
better it gets — which is the actual incentive, and beats a vague "prizes awarded" line.

Each is a card generated from `CONTESTS` in the data file, so adding a one-off side pot or raffle is
one entry, not a page edit.

Also: a **How to enter** block, a note that other promotions land here through the year rather than
living and dying in a Facebook post, and a **Past winners** section waiting on records. That last one
is the part people come back for.

Still needed: entry deadlines, how Big Buck is scored (gross, net, typical vs. non-typical), and when
the pot gets paid out.

---

### 4.5 Membership

**A. Lead with the price.** $25, single or family, no work hours — in the headline, not a price table.

| Membership | Dues | Work hours |
|---|---|---|
| Single | **$25 / year** | None required |
| Family | **$25 / year** | None required |

Membership runs with the **calendar year**.

**B. What members actually do** — course setup and teardown, working shoots, mowing — framed as
belonging rather than billing, because that's what it is.

**C. How to join** — three steps: apply online, or come to a meeting; then pay your $25.

**D. Youth and new archers** — two cards absorbed from the old first-timer page:

- **Getting a kid started:** Grant County 4-H Shooting Sports practices here and **provides all the equipment**. Sign-up goes through 4-H, not the club.
- **Students:** the UW-Platteville Pioneer Sportsman's Club runs an archery league and lends gear.

**E. Online application form** — plus a PDF for paper people.

**F. Guests** — $25 gets you a membership; $5 gets your buddy a round on the course.

---

### 4.6 Range & Directions

- **Two map buttons**: *Get directions in Google Maps* (opens turn-by-turn from wherever they are) and *Just show me the map* (a plain pin, for people who want to see where it is first).
- Written directions from Platteville, using the wording Grant County tourism and Grant County 4-H both publish, plus a GPS warning about County Line Road.
- **The facility in concrete numbers**: 40 targets outdoors, 28 indoors for the Brush Shoot, 20-yard indoor range, clubhouse.
- Course map image.
- **Range safety** — absorbed from the old first-timer page. Six rules, plus a slot for the club's full posted rules sheet.

---

### 4.7 Photos

One gallery, organized by year and event. The Brush Shoot and the banquet are the two that would earn
their own galleries once there are enough photos. Submissions route through the Contact page.

---

### 4.8 About the Club

- **History: founded 1937 as the Iowa-Grant Conservation Club.** 90 years in 2027, and it leads the page.
- Officers and board with roles and what each one handles — including a **Contests** row.
- **Monthly meeting schedule** — third Wednesday June–December, third Thursday January–May, with the next date shown live.
- **Who else uses these grounds** — the real list from §2.7. This section does more work than a generic affiliations line: it says the club is community infrastructure, not a hobby group.
- A card pointing at Contact, and one for **Seven Oaks Archery** — the only other club the site links to.

Contact details have moved off this page entirely — see 4.9.

---

### 4.9 Contact Us

Its own page, because the two highest-value visitors — a prospective member and a prospective sponsor
— both need to reach a human, and neither should have to hunt for it.

**A. The form.** Name, email, phone, a **"What's this about?"** dropdown (joining · sponsoring · youth
archery and 4-H · a shoot or league question · using the grounds · something else) and a message.
Submitting composes a complete, addressed email and hands it to the sender's own mail app.

That mechanism is deliberate: it works today on a static site with no accounts, no monthly fee and
no backend, and the club's email address isn't even settled yet. When it is, a form service like
Formspree or JotForm drops in behind the same form so messages land straight in an inbox — that's a
change to one function, nothing else on the page moves. The page says so out loud, and gives a
fallback (direct email, or Facebook) in case a browser blocks the handoff.

**B. Reach us directly** — email, phone, Facebook, Instagram, postal address, and a **Get directions
in Google Maps** button.

**C. "Or just come to a meeting"** — with the next date live.

**D. Three routing cards** at the bottom: thinking about joining → Membership; thinking about
sponsoring → Sponsors; want to come shoot → Schedule.

---

### 4.10 Sponsors

The banquet raffle is the product. The page states what a sponsor gets — banner at the Brush Shoot
and both outdoor 3D shoots, recognition at the **February 6 banquet raffle**, website logo — with a
price for each tier, framed as a product rather than a favour.

**2027 is the 90th year**, which makes the anniversary banquet an easier ask than a normal one.

Sponsorship enquiries route through the Contact page.

---

## 5. Look and feel

**Direction:** clean and outdoors, not busy. Big photos, generous white space, a real type hierarchy. The goal is that it looks better than every other club site in Wisconsin while still loading instantly on a phone in a gravel parking lot.

- **Palette:** deep forest green + warm dark brown, with a blaze-orange accent used sparingly for buttons and "Open to the Public" badges. Off-white page background, near-black text.
- **Type:** one sturdy sans for headings, a highly readable sans for body. No script fonts.
- **Mobile-first.** Most visits are phones. Tables collapse to cards; the "What's Next" block is the first thing on screen.
- **Badges** carry meaning: green = Open to the Public, brown = Members, orange = happening now.
- **Accessibility:** real contrast, alt text on photos, tap targets big enough for gloves.
- **No ads, no free-subdomain branding.** A club domain — `tricountyarchers.com` is taken by a New York/Pennsylvania club, so likely `tricountyarcherswi.com` or `tcarchers.com` **[CONFIRM]** preference.

---

## 6. Images I need

Drop these in the TCA folder. Phone photos are fine — real beats stock every time. Landscape orientation for anything wide.

**The one real gap:** a **wide outdoor shot of the course or grounds**. Everything supplied so far is portrait or indoor, and the hero wants a landscape frame.

**Essential:**

1. **Hero shot** — the 3D course from a trail, wide/landscape, nothing cluttered in the foreground.
2. **Clubhouse / entrance** — what someone sees when they pull in. Goes on Range & Directions so first-timers know they're in the right place.
3. **Course map** — a photo of the posted map, or a hand sketch. I'll redraw it clean.

**Strongly wanted (one each):**

4. **Archers at a league night** — a few people on the line, casual, backs or faces both fine.
5. **The Brush Shoot in progress** — a group at a stake, scorecards out. Sells the atmosphere, and it's the club's most distinctive event.
6. **Youth or family shooting** — a kid on the line with an adult, ideally from a 4-H practice. Highest-converting image on any club site.
7. **Banquet or raffle table** — sells sponsorship.
8. **Course setup or a work day** — people building targets, mowing, hanging butts. Shows the culture honestly, which matters more here precisely because there's no hours requirement.

**For galleries — bulk is good:**

9. **20–40 event photos** from the last couple of seasons, ideally grouped in folders by event and year.
10. **Sponsor logos** — one file per sponsor, plus their website URL. A text list of names + URLs is enough if you don't have the logos; I'll chase them down.

**Nice to have:**

11. Aerial or drone shot of the grounds.
12. Seasonal contrast — the same view in snow and in summer green.
13. **Anything from the club's history** — an old sign, a vintage photo, an Iowa-Grant Conservation Club document, a founding-era trophy. With 1937 confirmed and a 90th anniversary coming, this went from "nice to have" to worth actually digging for.

**Naming:** `2027-02-brushshoot-01.jpg` or a folder per event both work. Don't rename anything on my account — I'll sort it.

---

## 7. Still open

Short list now. Everything not here is answered in §2.

### Club details

| Item | Need |
|---|---|
| **Phone number** | Three numbers are in circulation: the draft site has **608-778-8742**; Grant County tourism lists **608-348-8100**; the 4-H newsletter lists Rhonda Hughey at **778-8415**. Which is the club's public number? |
| **Officers / board** | Names and contacts — President, VP, Secretary, Treasurer, membership, grounds, league coordinators. This is the single most-visited kind of content after the schedule. |
| **League coordinators** | One name and contact per league — indoor and outdoor. |
| **History, 1937 → today** | When it became Tri-County Archers, when the clubhouse went up, how the 3D course came to be, who's remembered. |
| **Nonprofit status** | Confirm 501(c)(3) specifically vs. another exempt class, so the site can state it accurately. |
| **Domain preference** | `tricountyarcherswi.com`, `tcarchers.com`, or something else. |

### Schedule gaps

| Item | Need |
|---|---|
| **Course setup / teardown days** | Real dates. Members turn out for these and they belong on the calendar. |
| **Shoot registration times** | Registration open–close for each of the three shoots — "8am" isn't enough, 3D shooters plan a drive around it. |
| **Shoot fees** | Adult / youth / cub pricing for the Brush Shoot and the two outdoor shoots. |
| **Target brand** | Rinehart, Delta McKenzie, mixed? 3D shooters genuinely choose shoots on this. |
| **Indoor league end date** | 10 weeks from Jan 7 lands on Mar 11 if run straight through. Any skip weeks? |
| **Indoor league scoring** | Individual, confirmed. Are there classes, or is it one flat list? |
| **Team pairing** | How do outdoor league teams get formed — drawn, chosen, carried over year to year? |
| **Fourth or last Saturday in May?** | The May shoot is generated as the **fourth** Saturday, which matches the confirmed 2027 date. If the club actually means the *last* Saturday, those differ in years when May has five — check a past year or two and I'll switch it. |
| **Do the two outdoor shoots have distinct names?** | Both currently read "Outdoor 3D Shoot" on the schedule, which is accurate but reads oddly twice. If the club calls them different things, that's better. |
| **Indoor range specs** | Number of lanes and distance. |
| **Member access** | Is there key or code access to the indoor range outside league nights? On every good club site this is the headline benefit — and it matters more here since members can shoot their league score any day. |
| **Brush Shoot extras** | Is there a raffle, food stand, or charity tie-in? SCWA in Monroe runs theirs as a toy drive; if TCA does something similar it belongs on the page. |

### Contests

| Item | Need |
|---|---|
| **Entry deadline** | For Big Buck and Fall Turkey, and who collects the $10 |
| **Scoring** | Is Big Buck gross, net, typical vs. non-typical? |
| **Weapon** | Bow-only, or any legal weapon? |
| **Prize and award night** | What the winner gets, and whether it's handed out at the banquet |
| **Past winners** | Any list the club has kept, however rough — it's the part people come back for |
| **Anything else running** | Other promotions, side pots or raffles that should live on that page |

### Results and sponsors

| Item | Need |
|---|---|
| **How scores are kept today** | Paper cards, a spreadsheet, a scorer's laptop? Decides whether we build a paste-in workflow or a simple entry form. Photos of last season's wall sheet would let me fill the tables in and show the board what it looks like working. |
| **Regional circuit?** | Do the leagues belong to any wider circuit? If so we link to their standings rather than duplicating. |
| **Past league seasons** | 2026 outdoor is in. Anything older, in any format, extends the archive. |
| **Sponsor list** | Names + web addresses; I'll chase the logos. The tier structure on the draft site (Bullseye $500 / Gold $250 / Supporting $100) is invented as a starting point for the board to argue about. |
| **Affiliation contacts** | A link or contact for the **Iowa-Grant Trap Team** — it's the one affiliation I couldn't verify online. |

---

## 8. What changed on the site

All of this is applied and live in the built pages. The guesses below were **removed**, not inverted —
nobody should read this site and come away with a list of things they can't do here.

### Removed

| Was on the site | Now |
|---|---|
| "Yes, you can just show up" for non-members | Non-members are welcome at **any posted event**; a member can bring a guest for **$5** |
| Loaner bows available | Gone. Where equipment genuinely is provided — the **4-H youth program** — that's now said positively, on the New Archers page |
| Member count (180) | Gone, no number published |
| Harvest / Big Game wall | Section removed from Photos; homepage section replaced with a **Brush Shoot** feature |
| Acreage (40 acres) | Gone from the facility specs |
| Work hours (12/yr, $30/hr unworked) | Gone. Replaced with what members actually do — course setup, working shoots, mowing — framed as belonging, not billing |
| Dues tiers (7 levels, $20–$400) | Two rows: **Single $25, Family $25**, no work hours |
| Non-member day rate ($10) | Replaced by the **$5 guest fee** |
| Member sponsor required + voted in at a meeting | Gone. Joining is: apply online, or come to a meeting |
| 24/7 door code, family included | Gone until confirmed |
| 18 invented events | Gone — including "Bill Hoffman Memorial 3D", a shoot and a person I made up |

### Corrected

| Was | Now |
|---|---|
| Founded 1962 | **1937**, as the Iowa-Grant Conservation Club — and it now leads the About page and the hero |
| Meeting: second Thursday | **3rd Wednesday Jun–Dec, 3rd Thursday Jan–May, 7–8 pm** — generated from the rule, so it can't drift |
| "Vegas 450" | **30-arrow Vegas**, 300 possible |
| Four leagues | **Two**: indoor Vegas $40, outdoor 3D $35, twelve weeks each |
| Outdoor course "28 targets" | **40** outdoors; 28 is the indoor Brush Shoot |
| Brush Shoot as a December toy drive | **February 13–14, 2027**, indoor 3D |
| Banquet in March | **February 6, 2027** |
| Club year starts April 1 | **Calendar year** |
| Affiliations: NFAA / WAA / Wisconsin Bowhunters | The real list from §2.7 — trap team, 4-H, UW-Platteville, coon hunters, Rewey Fire |
| Facebook only | Facebook **and Instagram** |
| Phone 608-778-8742 | **`###-###-####`** until the club confirms which number is public |

### Added

- **The flexible-week rule gets its own box on the Leagues page.** No other club site in the state says "shoot your score whenever suits you," and it's the best answer to "I'd join but I work Thursdays."
- **$25 / no work hours leads the membership page and the homepage** instead of sitting in a price table. It's the strongest membership pitch of the twelve clubs surveyed.
- **The 4-H program is named on the New Archers page**, with the fact that equipment is provided. That's the real on-ramp for a kid with no gear.
- **90th-anniversary framing** on the About and Sponsors pages, since 1937 → 2027.
- **A results note explaining that standings are keyed to week numbers, not dates** — necessary because scores arrive out of order when people shoot any day of the week.

### How the site stays honest about what's still missing

Three tags render in yellow on the page, so nothing unfinished is silent:

| Tag | Means |
|---|---|
| a short yellow note | something specific still to confirm — "hours, fees and contact to confirm" |
| **verify date** | a real date from the club that doesn't match the stated rule |
| **guess** | a placeholder that was invented |

**No `verify date` flags are live.** Two were, briefly — the first outdoor 3D shoot and the outdoor
league start. Both are now confirmed (**April 3–4** and **June 2**), every date falls on the day of
the week its rule implies, and the flags are gone. The mechanism stays in place for the next date
that doesn't add up.

### Mechanics

Meeting dates and league season dates are now **generated from rules** rather than typed out — nine
meetings a year on a rule that changes in June is nine chances to publish a wrong date. Change
`MEETING_RULE` or a league's `start` in `assets/js/data.js` and the schedule table, homepage cards,
Leagues page and calendar download all follow.

The homepage league card now computes **which week of the season it is** rather than showing a
league night, which is the right unit given people shoot any day.

One layout fix along the way: the fourth "What's Next" card was orphaning onto its own row at
laptop widths. All four now sit on one line from about 960px up.

### Second round: structure, tone and buttons

**Pages removed.** *New Here?* and *Results* are gone. Neither had a content problem — they had a
placement problem. First-timer material belongs next to the dates people are already reading, and
standings belong on the same page as the league they belong to. Nothing was thrown away:

| Was on New Here? | Now lives on |
|---|---|
| How a 3D shoot works · what to bring · what it costs · walk-through explainer | **Schedule** — "First time at a shoot?" |
| Getting a kid started (4-H, equipment provided) · students (UW-Platteville) | **Membership** — "Youth and new archers" |
| Range safety rules | **Range** — "Range safety" |
| "Still not sure?" | **Contact** |

| Was on Results | Now lives on |
|---|---|
| Standings tables · shoot results · season archive · scorer instructions | **Leagues & Standings**, under an anchor nav |

**Pages added.**

- **Contact Us** — its own page rather than a block on About, because a prospective member and a prospective sponsor are the two most valuable visitors the site gets and neither should have to hunt. Form composes a complete addressed email and hands it to the sender's mail app: no backend, no accounts, no monthly fee, works today even though the club's email address isn't settled. A form service drops in later behind the same form.
- **Contests** — Big Buck and Fall Turkey, $10 each. Card-per-contest generated from the data file, so a one-off side pot is one entry rather than a page edit.

**On the name:** *Contests* rather than *Promotions*. Promotions reads like discounts or marketing;
these are contests you enter and try to win, and that's the word members would use.

**Tone swept.** Ten places compared Tri-County favourably to other clubs — "standings you can
actually read," "no spreadsheet downloads," "every club site throws these names around," "named
humans is the norm at every club in the state." All gone. The competitive analysis was useful for
deciding *what to build*; it has no business being visible to a visitor, and a club site that opens
by knocking the neighbours reads badly however true it is. The reasoning stayed here in the plan,
where it belongs. Also removed: a board-facing note on the Sponsors page about which businesses to
approach.

**Buttons added.**

- **Add to Google Calendar** on every schedule row and every "What's Next" card, including the league card. All-day and multi-day events get a correct exclusive end date, so a two-day shoot lands as two days rather than three. The whole-season `.ics` download stays for people who'd rather import once.
- **Get directions in Google Maps** on the Range page, the Contact page and in the footer of every page — turn-by-turn from wherever the visitor is, rather than a pin they then have to route from. The Range page keeps a plain "just show me the map" link alongside it, for people orienting themselves before they commit to driving.

### Third round: real scores, real contests, and links that don't lose your place

**Leagues are 10 weeks, not 12.** Corrected in the data, so the season end dates recomputed
themselves: indoor now ends the week of **Mar 11** and outdoor the week of **Aug 4**. That also
dissolved a clash the 12-week figure had created, where the outdoor league's final week landed on the
same Wednesday as the August meeting.

**Summer 2026 outdoor league standings are live**, from `Outdoor League Stats.xlsx`. See §4.3 — the
short version is that the league is decided on **total points**, ranking on average would have
published the wrong runner-up, and both facts are now visible on the page rather than implied.

**Contests split into bow and gun.** Big Buck runs as two separate contests with separate pots, plus
Fall Turkey. **Winner takes the pot** — stated on every card and in the how-to-enter block. That
answered two of the open questions from the previous round; what's left is deadlines, scoring method
and payout timing.

**External links open in a new tab.** Anything pointing off-site gets `target="_blank"` and
`rel="noopener noreferrer"`, so nobody loses their place on the schedule. Done two ways on purpose:
the static links carry the attributes in the built HTML, and a small runtime pass catches everything
else — generated calendar links, and any link added later without remembering the rule. `mailto:`,
`tel:` and same-page anchors are deliberately left alone.

**Nearby clubs trimmed to Seven Oaks.** The old list of four was inherited from research rather than
from the club. One real neighbour beats four strangers.

### Fourth round: designing the maintenance out

The goal here was to stop *making the work easier* and start *removing the work*. Anything that
follows a rule is now computed from the rule at page load, relative to today:

| Was | Now |
|---|---|
| League start dates typed in each year | Derived from "first Thursday in January" / "first Wednesday in June", + 10 weeks |
| Meetings generated for a fixed 2026–27 window | Generated relative to today, four years at a time — the calendar can't run dry |
| Copyright year hardcoded | Self-updating |
| "February 13–14, 2027" written into three pages of body copy | Pulled from the schedule, so prose can't contradict the calendar |

Verified by running the data file against six different "todays" from 2026 to 2031: every season
resolved to the right dates with no edits, correctly holding a season that's mid-run and rolling to
the next one once it ends.

Each league keeps an `overrides` map for years that don't follow the rule, so an exception moves one
season without breaking the pattern.

**What's left for a human in a normal year: three shoot dates and the banquet.** Those stayed manual
on purpose — archery clubs commonly set shoot dates around what neighbouring clubs are running, so a
rule would be a guess. That said, the 2027 dates all landed on clean patterns (banquet = 1st Saturday
in February, Brush Shoot = 2nd, outdoor #1 = 1st Saturday in April, outdoor #2 = 4th Saturday in May).
If those hold, each becomes a rule and the annual edit list goes to zero — that question is in §7.

One deliberate behaviour: while a shoot has no future date on the calendar, prose that refers to it
reads "dates to be announced" rather than quietly showing last year's date.

**Then the shoots and the banquet went rule-driven too**, once the patterns were confirmed:

| Event | Rule |
|---|---|
| Annual Banquet | 1st Saturday in February |
| Brush Shoot | 2nd Saturday in February, Sat–Sun |
| Outdoor 3D Shoot | 1st Saturday in April, Sat–Sun |
| Outdoor 3D Shoot | 4th Saturday in May |

All four rules reproduce the confirmed 2027 dates exactly — Feb 6, Feb 13–14, Apr 3–4, May 22 — which
is the check that matters: the generated calendar is identical to the hand-entered one, and it keeps
going. Verified again across 2028, 2029 and 2031: every date lands on the right weekday and the next
occurrence appears as soon as the last one passes.

**So every date on the site is now generated.** There is nothing to update in a normal year. What's
left for a human is league scores during a season, and the occasional weather notice.

Each shoot keeps its own `overrides` map for a year that moves. One thing to keep an eye on: the May
shoot is set to the **fourth** Saturday, matching the confirmed date. If it's really the *last*
Saturday those differ whenever May has five — worth checking against a past year or two.

## 9. How it's built

**Built as a static site with the schedule and results in editable data files.** No database, no monthly platform fee, instant page loads, nothing to hack. The club edits a simple file (or a Google Sheet we read) and the homepage, schedule page, and calendar feed all update from it.

| Option | Cost | Who can update it | Verdict |
|---|---|---|---|
| **Static site + data files, hosted free** (Netlify/Cloudflare Pages) | ~$15/yr domain only | Anyone comfortable editing one text file — or a Google Sheet, if we wire that up | **This is what I built.** Drag the folder onto netlify.com/drop and it's live in fifteen seconds. |
| Squarespace | ~$200/yr | Anyone, fully point-and-click | Good fallback if nobody at the club wants to touch a file. Slower, and the events widget is mediocre. |
| WordPress + events plugin | ~$100–150/yr + upkeep | Anyone, after training | Powerful but it's the option that rots. Someone has to do updates. |
| ClubExpress (Kenosha uses it) | ~$500+/yr | Built-in member management | Hard to justify against $25 dues. Public-facing pages look dated. |

**What's actually built** — ten pages:

| Page | State |
|---|---|
| Home | Hero, "What's Next" cards with calendar links, three-ways-in block, three tiles, stat row, Brush Shoot feature, sponsor strip |
| Shoot Schedule | Filterable table, per-event Google Calendar buttons, .ics download, "first time at a shoot" block |
| Leagues & Standings | Two league cards, shoot-any-day box, formats reference, standings tables, shoot results, season archive |
| Contests | Big Buck and Fall Turkey cards, how to enter, past-winners frame |
| Membership | Dues table, join steps, youth and new-archer cards, working application form |
| Range & Directions | Facility specs, written directions, two map buttons, facilities cards, course map placeholder, range safety |
| Photos | Gallery on the photos provided |
| Sponsors | Tier structure and logo frame, waiting on the list |
| About the Club | History, board table, meetings, groups on the grounds |
| Contact Us | Working email form with topic routing, direct contact details, map button, routing cards |

**Still to wire up:** the club's real email behind the contact form (or a form service in front of
it); application form → membership chair's inbox; membership application and season schedule as PDFs;
real course map; domain and hosting.

**The "never stale" mechanism.** Everything dated lives in one file (`assets/js/data.js`). The
homepage cards, the schedule page and the calendar download all read from it, so a date can't be
updated in one place and left to rot in another. Add an event once; it appears everywhere. This is
the single defect that plagues almost every club site I looked at, and here it's designed out rather
than managed.

The monthly meetings are a good test of this: nine meetings a year on a rule that changes in June
means nine chances to publish a wrong date. Generated from the rule, it can't drift.

**Weather cancellations.** There's an alert strip at the top of the homepage — one line in the data
file turns it orange for a cancellation or green for good news. Right now that information only
exists on Facebook, where it's invisible to anyone not logged in.

---

## 10. Next steps

1. **Click through the restructured site and redline it.** Eight nav items now, two pages gone and two added — worth walking the whole thing to check nothing you valued got lost in the move (§8 lists where each piece went).
2. **Get the board roster and the club phone.** Biggest remaining hole, and the second-most-visited content after the schedule. The phone reads `###-###-####` until you confirm which number is public.
3. **Fill in the contest details** — entry deadlines, how Big Buck is scored, and when the pot pays out. Plus any past-winner list, however rough.
4. **Send a wide outdoor photo of the course or grounds.** Still the only real gap in the image set.
5. **Decide on the 90th anniversary.** 1937 → 2027. If the club wants to make something of it, that decision shapes the banquet, the sponsor ask and the About page.
6. **Take it to the board.** Much easier to get the rest of §7 answered with a working site to look at.

Two things worth doing regardless of what happens to this website:

- **Post every shoot to [wiarchery.com](https://wiarchery.com/) via "Add Listing."** Free, it's the state's main shoot-finder, and the club's venue page there currently shows zero events. Three shoots a year is three listings — an hour of work for statewide distribution.
- **Ask Seven Oaks for a reciprocal link.** Club link pages are how archers actually find clubs in this sport, and we link to them already.

Keep Facebook and Instagram as the informal, chatty channels — but make the website canonical for schedule, results and membership, and have social posts link back to it.

---

## Sources

**Club and affiliations:** [Tri County Archers — Facebook](https://www.facebook.com/TriCountyArchers/) · [Instagram](https://www.instagram.com/tricountyarchers/) · [Tri County Archers Club Inc — ProPublica Nonprofit Explorer](https://projects.propublica.org/nonprofits/organizations/391401126) · [Grant County Sportsman Clubs directory](http://grantcounty.org/tourism/outdoor-activities/sportsman-clubs/) · [Grant County 4-H Echo newsletter (Feb–Mar 2025)](https://grant.extension.wisc.edu/files/2025/02/February-March-2025-Echo.pdf) · [Grant County 4-H Shooting Sports](https://www.youthshootingsa.com/product/grant-county-4-h-shooting-sports/) · [Wisconsin 4-H Shooting Sports](https://4h.extension.wisc.edu/opportunities/projects/outdoor-education/shooting-sports/leaders-and-additional-resources/) · [UW-Platteville Pioneer Sportsman's Club](https://www.facebook.com/UWPlattevillePioneerSportmansClub/) · [Shooting Sports UW-Platteville](https://www.facebook.com/ShootUWP/) · [Southwestern Wisconsin Coon Hunters Club](https://www.facebook.com/SWWCHC/) · [Rewey Fire Dept. & First Responders](https://www.facebook.com/ReweyFire/) · [Wisconsin State High School Clay Target League](https://wi.usaclaytarget.com/) · [Iowa-Grant School District](https://en.wikipedia.org/wiki/Iowa-Grant_School_District)

**Wisconsin club sites reviewed:** [Racine Instinctive Bowmen](https://www.ribarchery.com/) · [West Allis Bowmen](https://westallisbowmen.com/) · [Rib Mountain Bowmen](https://www.ribmountainbowmen.com/) · [South Central Wisconsin Archers](https://www.thescwa.com/) · [Kenosha Bowmen](https://www.kenoshabowmen.com/) · [Eau Claire Archers](https://www.eauclairearchers.org/) · [Janesville Bowmen](https://janesvillebowmen.wordpress.com/) · [Horicon Marsh Archers](https://hmarchers.com/) · [Chippewa Bow Hunters](https://chippewabowhunters.com/) · [Blackhawk Bowhunters](http://www.blackhawkbowhunters.com/) · [Beloit Field Archers](http://www.beloitfieldarchers.com/) · [KMFAL](https://kmfalarchery.com/)

**Directories:** [WI Archery](https://wiarchery.com/) · [Tri County Archers venue listing](https://wiarchery.com/venue/tri-county-archers/) · [NFAA Wisconsin](https://www.nfaausa.com/sections/great-lakes/wisconsin)

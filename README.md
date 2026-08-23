# Tri-County Archers — website

The live site is everything at the root of this repo. Two companion files:

- **[TCA-Website-Plan.md](TCA-Website-Plan.md)** — what the site is for, every confirmed club fact,
  and the running list of what's still unanswered. Start here.
- **`source-data/`** — the spreadsheets the standings come from.

> Both sit inside the published directory, so they're reachable on the live site at
> `/TCA-Website-Plan.md` and `/source-data/…`. Nothing links to them, but they aren't secret.
> If that stops being fine, they move up one level and Cloudflare Pages publishes only `site/`.


Ten pages, static HTML. No database, no monthly fee, nothing to hack.
Open `index.html` in any browser to look at it.

## Updating the schedule, leagues, dues and standings

**Edit one file: `assets/js/data.js`.**

Everything else reads from it. Add a date there and it shows up on the
Shoot Schedule page, in the homepage "What's Next" cards, and in the
downloadable calendar file — all at once. That's the fix for the single
most common failure on club websites: a homepage still advertising a
shoot that happened in March.

Inside `data.js`:

| Block | Controls |
|---|---|
| `CLUB` | Address, phone, founding year, dues, guest fee, target counts, the orange/green alert strip on the homepage |
| `MEETING_RULE` | The monthly meeting rule — **the dates are generated from it**, not typed out |
| `LEAGUES` | The two leagues: start date, length, entry fee, round |
| `CONTESTS` | The Contests page — Big Buck, Fall Turkey, and any one-off promotion |
| `EVENTS` | The three shoots, the banquet, and anything else dated. League dates and meeting dates are appended automatically from `LEAGUES` and `MEETING_RULE` |
| `RESULTS` | League standings tables |
| `SHOOT_RESULTS` | The shoot results list (empty until real cards arrive) |
| `DUES` | The dues table on the Membership page |
| `SPONSOR_TIERS` | Sponsorship levels and what each one gets |

### What updates itself, and what needs you

Anything that follows a rule is worked out from the rule at page load, relative to
today's date. That means it rolls forward on its own — nobody has to come back in
January and type in next year's dates.

| Thing | Who does it |
|---|---|
| Monthly meetings | **Automatic** — 3rd Wednesday Jun–Dec, 3rd Thursday Jan–May, generated four years at a time |
| Indoor league season | **Automatic** — first Thursday in January, + 10 weeks |
| Outdoor league season | **Automatic** — first Wednesday in June, + 10 weeks |
| Which league is "next" | **Automatic** — the season running now, or the next one up |
| Week N of the season | **Automatic** — counted from the start date |
| Copyright year | **Automatic** |
| Dates quoted in body copy | **Automatic** — pulled from the schedule, so prose can't contradict the calendar |
| Brush Shoot | **Automatic** — 2nd Saturday in February, Sat–Sun |
| Outdoor 3D shoots | **Automatic** — 1st Saturday in April (Sat–Sun), 4th Saturday in May |
| Annual banquet | **Automatic** — 1st Saturday in February |
| Contests, sponsors, photos | **You**, when they change |
| League standings | **You**, weekly during a season |
| Weather cancellations | **You**, when it happens |

**Every date on the site is now generated from a rule.** In a normal year there is nothing to
update — the calendar rolls forward on its own. What's left is scores during a season, and the
occasional cancellation notice.

#### When a season doesn't follow the rule

Every league has an `overrides` map for the years reality disagrees with the rule:

```js
rule: { month: 5, weekday: 3, nth: 1, label: "the first Wednesday in June" },
overrides: { 2029: "2029-06-13" },   // that year only, starts a week late
```

The rule stays intact; only that season moves.

#### Changing a shoot's rule, or moving one year

All four live in `SHOOT_DEFS` in `data.js`:

```js
{
  name: "Brush Shoot", type: "shoot", cat: "Indoor", who: "public",
  rule: { month: 1, weekday: 6, nth: 2, label: "the second Saturday in February" },
  overrides: {}, days: 2,
  ...
}
```

`month` is 0-based (so `1` = February), `weekday` runs 0 = Sunday to 6 = Saturday, `nth` is which
one of that weekday in the month, and `days` is how long it runs — `2` gives a Saturday–Sunday shoot.

If a shoot moves in one particular year — course not ready, another club has that weekend — don't
touch the rule, add an override:

```js
overrides: { 2029: "2029-04-14" },
```

**One judgment call to be aware of:** the May shoot is set to the **fourth** Saturday, which is what
the confirmed 2027 date worked out to. If it's really the *last* Saturday of May, those differ in
years with five Saturdays. Worth checking against a couple of past years.

Occurrences are generated for last year, this year and next, so there's always a future date up and
the "Past events" filter has something in it.

### Tags

Three flags make unfinished information visible rather than silent:

| Flag | Renders as | Means |
|---|---|---|
| `tag:"..."` | that text, in yellow | something specific still to confirm |
| `verify:true` | **verify date** | a real date from the club that doesn't match the stated rule |
| `guess:true` | **guess** | a placeholder that was invented |

Delete the flag when the real value goes in. No `verify:true` flags are live
right now — every date checks out.

### Weather cancellations

In `data.js`, edit `CLUB.alert`:

```js
alert: { text: "Sunday's 3D shoot is cancelled — course is under water.", tone: "warn" }
```

`tone: "warn"` is orange, `"ok"` is green, and `text: ""` hides the strip
entirely. This is the thing that currently only exists on Facebook.

## Rebuilding the pages

The header, footer and navigation live in `build.py` so all ten pages stay
identical. If you change any of those, run:

```
python3 build.py
```

You do **not** need to run this to update the schedule or scores — only to
change page structure or copy.

## Files

```
index.html            Home
schedule.html         Shoot Schedule — the canonical calendar, with per-event calendar buttons
leagues.html          The two leagues, formats, and all the standings
contests.html         Big Buck, Fall Turkey and other promotions
membership.html       Dues, how to join, youth/4-H, application form
range.html            Directions, facilities, range safety
photos.html           Gallery
sponsors.html         Sponsors and sponsorship tiers
about.html            History, board, meetings, groups on the grounds
contact.html          The email form and every way to reach the club
build.py              Page generator (header/footer/nav)
assets/js/data.js     ← the file you actually edit
assets/js/site.js     Rendering logic
assets/css/site.css   All styling
assets/img/           Photos and logo
```

## Every date is confirmed

All shoots, both league seasons and the monthly meetings are confirmed and internally consistent —
each one falls on the day of the week its rule implies. No `verify date` flags are live.

For reference, the 2027 season:

| Date | Event |
|---|---|
| Thu, Jan 7 | Indoor League week 1 — individual, 10 weeks, $40 |
| Sat, Feb 6 | Annual Banquet |
| Sat–Sun, Feb 13–14 | Brush Shoot — indoor 3D, 28 targets |
| Thu, Mar 11 | Indoor League final week |
| Sat–Sun, Apr 3–4 | Outdoor 3D Shoot #1 — 40 targets |
| Sat, May 22 | Outdoor 3D Shoot #2 — 40 targets |
| Wed, Jun 2 | Outdoor 3D League week 1 — two-archer teams, 10 weeks, $35 |
| Wed, Aug 4 | Outdoor 3D League final week |

## Standings

`RESULTS` in `data.js` holds one entry per league season. Two shapes:

- `format: "team"` — the **outdoor** league. Teams of two. Ranked on **total points**, which is what
  decides the league. Each team needs `total`, `avg` and an `archers` array; each archer needs
  `scores` (one per week, `"X"` for a week not shot), `total` and `avg`.
- `format: "individual"` — the **indoor** league. Same idea, but a flat `rows` array. Leave `rows`
  empty and the `empty` message shows instead of placeholder names.

**Rank the teams in the order you list them** — the table renders them top to bottom and puts the
medals on the first three. Sort by `total`, not by `avg`: those two can disagree. In Summer 2026 they
did, because a missed week lifts an archer's average (it only counts weeks shot) while flattening
their total.

Averages are stored raw and rounded for display, so paste them straight out of the spreadsheet.

## The contact form

`contact.html` collects a name, email, phone, a topic and a message, then builds a complete
`mailto:` and hands it to the visitor's own email app. That means it works on a static site with
no backend, no accounts and no monthly fee — and it works right now, before the club has settled
on an email address.

The address it targets is `CLUB.email` in `data.js`, currently a placeholder. **That one line is the
only place the club email lives** — the form, the two links on the Contact page and anything added
later all read from it, so switching addresses is a single edit.

**To make messages land straight in an inbox instead**, point the form at a service like Formspree
or JotForm. That's a change to `wireContact()` in `assets/js/site.js` and nothing else — the form
markup, the fields and the page all stay as they are.

## Add to Google Calendar

Every row on the schedule page and every "What's Next" card on the homepage has one. The link is
built by `gcalUrl()` in `site.js` from the same event data as everything else, so a new event gets
its button automatically.

All-day events need an *exclusive* end date — the day after the last day — or a two-day shoot shows
up as three. `exclusiveEnd()` handles that, and both the Google Calendar links and the `.ics`
download use it.

## Links that leave the site

Anything pointing at another site opens in a new tab. Handled twice on purpose: `build.py` writes
`target="_blank" rel="noopener noreferrer"` into the static links, and `wireExternalLinks()` in
`site.js` sweeps the page at load for anything else — generated links, or a link added later without
remembering the rule. `mailto:`, `tel:` and `#anchors` are left alone.

Nothing to do when adding a link: just write it normally.

## Still to do

- **A real club email** — the contact form is addressed to `CLUB.email`, currently a placeholder
- The club's public phone number — currently `###-###-####` in `CLUB.phone`
- Board and officer names and contacts (`about.html`, in `build.py`)
- League coordinator names (`LEAGUES` in `data.js`)
- Shoot registration hours and fees by age bracket (`EVENTS` in `data.js`)
- A real club email address, not tied to one person's inbox
- Club history between 1937 and now — **2027 is the 90th year**
- Contest details — entry deadlines, how Big Buck is scored, payout timing, past winners (`CONTESTS` in `data.js`)
- What a perfect round is on the 3D course, so the league scores can be read in context
- Point the membership application at the membership chair's inbox (about ten minutes with a form service)
- Build the membership application and season schedule as PDFs
- Real sponsor logos and the sponsor list
- Course map
- Register a domain and host it — Netlify or Cloudflare Pages will serve this for free
- Post all three shoots to wiarchery.com via "Add Listing" (free statewide distribution; the club's venue page there currently shows zero events)

## Hosting

Drag this whole folder onto netlify.com/drop and it's live in about
fifteen seconds, for free. Point a domain at it whenever the club buys
one. Same for Cloudflare Pages.

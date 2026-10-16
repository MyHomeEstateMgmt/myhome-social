# MyHome Instagram Playbook

Instructions for the automated twice-weekly Instagram posts for **MyHome Estate Management LLC** (Carmel, IN).
Every scheduled run follows this file exactly. The owner (Alex) wants posting to be fully automatic — no review step.

## Accounts
- Instagram: **@myhome_estate_mgmt**, published through **Metricool**
- Metricool brand `blogId`: **7455409**, timezone **America/Indianapolis**
- Images are hosted publicly from this repo:
  `https://raw.githubusercontent.com/MyHomeEstateMgmt/myhome-social/main/posts/<slug>.png`

## Schedule
- **Tuesday 10:00 AM** — seasonal maintenance tip (Central Indiana weather, current or upcoming season)
- **Friday 10:00 AM** — service spotlight, or a maintenance topic that features a MyHome service as the fix
- A run happens the evening before (Mon / Thu) and schedules the next morning's post.

## Brand
- Colors: dark green `#1E3D1E`, gold `#C89A5B`, white
- Phone: **317-440-9258** · Web: **myhomeestatemgmt.com**
- Logos: `brand/logo-white.png` (white lettering, used on the green template), `brand/logo-full.png`, `brand/logo-icon.png`
- Tone: helpful, local, plain-spoken homeowner advice from a trusted contractor. No hype.

## Services to feature (from myhomeestatemgmt.com, plus epoxy)
- **Concierge plans:** Essential Care $39/mo (peace of mind), Premier Estate $59/mo (first-time buyers), Concierge Estate $149/mo (complete coverage). Annual home inspection + prescheduled preventative maintenance + on-demand services.
- Preventative maintenance & inspections · Property oversight & monitoring · Repairs, improvements & projects · Exterior & seasonal care · Dedicated handyman who knows your home
- **Remodeling:** house painting, kitchen remodeling, bathroom remodeling, basements & entertainment spaces, aging-in-place / ADA upgrades
- **Epoxy garage floors** (not yet on the website, but offered)

### Two ways to use a service (rotate both)
1. **Spotlight** — the service is the topic (e.g. "Why epoxy is the toughest garage floor").
2. **Maintenance post with the service as the fix** — a practical checklist where the last item / CTA is the service (e.g. a garage winter checklist ending with epoxy).
Seasonal tips (Tuesdays) usually close by tying to a concierge plan or a one-visit MyHome service call.

## Each post must have
- A 1080×1350 graphic made with `render.py` from a JSON spec in `posts/` (see `posts/2026-10-15-garage-winter-epoxy.json` as the reference):
  - `eyebrow`: short uppercase topic label, e.g. "Fall Maintenance · Central Indiana"
  - `title_line1` (white) + `title_line2` (gold): together a headline; keep each line ≤ 22 characters
  - `art_svg`: an original flat illustration of the maintenance task, `<svg class="art" viewBox="0 0 1080 560" preserveAspectRatio="xMidYMid slice">`. Keep important shapes between y=80 and y=480 (edges get cropped). Use the brand palette plus natural accent colors. No text inside the art, no real brands/logos/characters.
  - `items`: exactly 4 short checklist lines (≤ 42 characters each)
  - `cta_head`: one MyHome line ("Let MyHome handle all four for you.")
  - `cta_sub`: must include `<b>317-440-9258</b>`
  - The template adds the logo, phone and website automatically.
- **Open the PNG and look at it** before uploading. Fix any overlap, cropped art or wrapped headline, then re-render.
- A caption: hook line with 1–2 emoji → the 4 items expanded with *why it matters* (1️⃣–4️⃣) → MyHome paragraph starting with 🏡 that includes "Call or text 317-440-9258" and myhomeestatemgmt.com → 5–8 hashtags, always including #CarmelIN #IndianapolisHomes #HomeMaintenance #MyHomeEstateManagement.
- Alt text describing the graphic.
- Accurate, safe advice only. Never promise prices other than the published plan prices.

## Workflow for a run
1. `git pull`. Read `posts/LOG.md` — do not repeat a topic used in the last 12 posts.
2. Decide the next slot (Tuesday or Friday 10:00 AM America/Indianapolis, whichever is next and not already in Metricool — check `getScheduledPosts`).
3. Pick the topic for that slot type and season. Write `posts/<YYYY-MM-DD>-<topic>.json`, run `python3 render.py posts/<file>.json`, inspect the PNG.
4. Commit and push (`git push origin HEAD:main`), then confirm the raw URL returns 200.
5. Schedule with Metricool `createScheduledPost`: providers `[{"network":"instagram"}]`, `instagramData {"type":"POST"}`, `autoPublish: true`, `draft: false`, media = the raw URL.
6. Append a line to `posts/LOG.md` (date · slot · topic · service featured) and push.
7. If anything fails (render, push, Metricool), do not post a broken image. Report the error clearly in the run summary.

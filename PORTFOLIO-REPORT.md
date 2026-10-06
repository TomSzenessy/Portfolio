# Portfolio Refresh — Review & Change Plan

> Status: **IMPLEMENTED 2026-10-06** (v2) — every P0/P1 item and the content plan below is now in the code on branch `portfolio-final`; §7's list doubles as the checklist of what shipped. Remaining future work: full `/` vs `/en/` page de-duplication (the shared-script port fixed the bug; the two page files still duplicate markup).
> Branch: `portfolio-final` · Site: szenessy.com · Goal: *"If someone Googles my name — recruiter, AI, or anyone — they are impressed and want to hire me."*
> Companion files: `research-positioning.md` (cited research brief)

---

## 0. TL;DR

**The content is strong; the execution loses trust at exactly the moments that matter.** A squished background-less favicon, hero face and share image; a dead project link; video cards that look like link-previews instead of YouTube; and a consent system that re-prompts after you already said yes (a real bug — see B6). Every one of these is a 5-second credibility leak on a page whose entire job is credibility.

**Bugs to fix before anything else (P0):** consent Escape-key leak + declined-re-prompt, the block-rendering nav rail on `/`, the 404 project link, the three face images (favicon/hero/og), the hero H1 that never says who he is, and the YouTube card chrome.

**Strategy:** less, but proven. Keep the 6 projects (fix one link), keep 8 curated awards but re-order them, put third-party press proof next to claims, sharpen skills to what the projects demonstrate, one warm hobbies line. Tone: naked facts + one journey sentence per story; **no over-claims** (the page must never say something its own proof link contradicts — e.g. Jugend forscht was **2nd prize + CIB Special Prize**, not "winner"). One canonical identity sentence across site/LinkedIn/GitHub so Google and AI assistants quote it back correctly.

---

## 1. The strategy: how to "sell" Tom

### 1.1 What the site actually has to do

- Recruiters scan fast — the widely-cited Ladders study puts a first résumé screen at ~7 s with most attention on name/role/education/dates. That study measures **résumé** scanning, so treat it as intuition, not law — but the design implication holds: the first screen must answer *who / what / for whom / with what* without scrolling. (Sources in `research-positioning.md`.)
- A portfolio **helps a junior only if it is polished and maintained** — a broken or stale page is net negative ([Profy.dev survey of 60+ hiring managers](https://profy.dev/article/portfolio-websites-survey)). Fixing the bugs *is* the strategy, not a prelude to it.
- **69% of hiring managers Google candidates** (CareerBuilder/Harris 2017). The site's real job: make the **name-search result** impressive and make the CV believable — not to contain everything.
- AI assistants increasingly summarize people from their sites. What helps: one **canonical, quotable identity sentence** repeated verbatim on site/LinkedIn/GitHub; plain-text facts (LLMs don't read JSON-LD); every claim linked to third-party evidence; freshness ([GEO study, KDD 2024](https://dl.acm.org/doi/10.1145/3637528.3671900): citations/quotes/stats boost AI visibility).

**Design target:** one scannable page, one voice, one dominant CTA. Competence in the top half, personality in the bottom third. *Let third-party evidence do the bragging.*

### 1.2 Positioning — fix the first screen (P0)

Current hero renders "Hi, I'm Tom" + a subline + a stack line. Problems: the H1 contains neither the full name nor the role (bad for name search and for the 5-second test), there is no proof chip and no availability/CTA beyond "See My Work". Note `translations.js:187` already contains an unused `hero_h1` key with the right idea.

Proposed first screen:

> # Tom Szenessy
> **Business Informatics student at TUM (Munich).** I build and ship full-stack products — games, plugins and self-hosted platforms.
> `Jugend forscht 2024 — 2nd prize + CIB Special Prize` · `1.0 Abitur`
> TypeScript · Python · Go · Cloudflare Workers · React · Node.js · Kotlin · PostgreSQL
> **[See my work]** **[Get in touch]**

Rules baked in:
- **Name in the H1** — it's what a name-searcher looks for and what Google bolds.
- Proof chips state **naked facts with exact wording the proof link confirms**. "Jugend forscht 2024 — 2nd prize + CIB Special Prize" is verifiable in the [CIB article](https://www.cib.de/en/partizipation-record-jugend-forscht-iberia-2024-lisboa/). Never "winner".
- **No "looking for work" line** (your call: the goal is *visibility*, not job-hunting) — the CTA stays a warm "Get in touch", which reads well to recruiters, friends and AI assistants alike without a job-market tone.
- The warmth line ("Still learning, always curious…") stays below the fold of attention — it's the valve that keeps the page from reading as a trophy case.
- The joke "Just a chill, friendly…" (currently the LinkedIn headline and the site `<title>`, `translations.js:4`) moves out of both; humour stays in body copy where it reads as personality, not positioning.

### 1.3 Tone rules (likable, not boastful)

1. **Naked facts beat adjectives.** "2nd prize + CIB Special Prize, Jugend forscht 2024" + link. The reader supplies the impressiveness.
2. **Never humblebrag** (Sezer et al. 2018: humblebragging is *less* likable than plain bragging). Genuine journey beats are fine — "lost to an unrehearsed demo on stage, wrote down why on the way home, kept building" works because it's true and effort-focused.
3. **Warmth near competence, but don't make it a formula.** High competence + zero warmth triggers envy (Cuddy/Fiske). Vary how warmth appears — a patterned "one warm sentence after every claim" reads engineered to a sharp reader.
4. **1–2 journey sentences per story** raise warmth at zero competence cost (Nault/Sezer/Klein): "after two years of weekend tinkering", "wrote down why on the way home".
5. **Never self-deprecate real achievements** ("my little project"). One small authentic imperfection elsewhere is enough — the page already has a good one: *"making videos nobody asked me to make."* Keep it.
6. **Specific beats generic**: "a stubborn Chopin nocturne" > "piano".
7. Front-load the first words of every block (F-pattern scanning).
8. One voice: a friendly, precise person explaining his work to a smart stranger.

### 1.4 Hobbies: include them — one compact line

Evidence-based answer to your four questions:

- *Is it boasting?* No. Boasting is an evaluative claim ("I'm disciplined"). "Three years taekwondo, two judo, one karate" is a bare fact — a life detail, not a claim.
- *What are recruiters looking for?* Once competence is established they're largely checking culture fit and "would I enjoy this person around". Shared interests create rapport (similarity-attraction research); team sports are among the few hobby signals that measurably raise hireability (teamwork/discipline read-through).
- *Is it helpful?* Three jobs: **memorability** ("the taekwondo/piano guy from TUM" beats a 5th framework chip), **warmth** (the pressure valve on an award-heavy page), and **conversation material** for the friends/dates/peers audience.
- *Worth it?* **At one line, yes** (~10 words for likability + memorability). It becomes a liability only if it grows into a section with bullets and photos.

Proposed line: *"Off-screen: volleyball and padel, six years of martial arts (taekwondo 3, judo 2, karate 1), piano, board games — and running a student stand-up comedy club, StuStandUp."* (**Poker: dropped per your decision.** The comedy club is confirmed real and goes in as a personality line — never as a project card.)

---

## 2. Bugs & fixes

Every root cause below was verified against the source (file:line correct as of HEAD `197fbd5`).

### P0 — these cost you trust in the first 10 seconds

| # | Bug | Root cause (evidence) | Fix |
|---|-----|----------------------|-----|
| B1 | Favicon looks squished in the tab | The favicon **files are all square and undistorted** (measured: `favicon.webp` 512×512, all PNGs square) — so the squish has 3 real causes: (a) **favicon cache**: `main` served a 400×515 photo at the same `/favicon.webp` URL, and browsers pin favicons hard; (b) **no `favicon.ico`** exists, so the default `/favicon.ico` probe 404s; (c) the artwork is a bare head cut-out on transparency (hair at top edge, neck cut) which reads as cramped noise at 16px. Bonus: legacy `index.html:7` points at a deleted 400×515 photo | Add a real `favicon.ico` (16/32/48), cache-bust by renaming (`/favicon-v2.webp` or `?v=2`), and redraw the artwork: face inside a rounded-square cream tile (`#f6eee2`) with ~12% padding. Repair/remove the legacy `index.html` icon link |
| B2 | Hero face squished, no background | Three stacked causes (pixel-measured): (a) `Tom Passfoto-square.webp` is a **non-uniform resample — ~4–6% vertically stretched** — of the 2147×2761 passport photo; (b) commit `6a637c8` removed the circle's `bg-gradient` backdrop, so the **cut-out's transparent pixels** show the white card through → floating head; (c) `object-cover` on the tight crop cuts chin and hair at the circle rim (`Hero.astro:16-24`) | Regenerate the square with a uniform crop from `Tom Passfoto.png` (`-gravity center -crop … +repage -resize 512x512`), restore a circle backdrop (`bg-accent-soft` or the gradient) **or** use an opaque photo, and loosen the crop. Recommended source: "Tom leaning against a wall" (1200×1200, relaxed, has background) — see open question 5. Also fix mismatched `width`/`height` props in `ParallaxQuote.astro:22` and `PeekingTom.astro:16` |
| B3 | Dead project link | `Projects.astro:62` → `github.com/TomSzenessy/AlpacaTradingBot` → **404** (verified) | Per your decision: publish a sanitized repo, then keep the card. Until it's public, hide the card — a dead link is the worst trust signal on a portfolio |
| B4 | Video cards don't look like YouTube | Pre-consent poster is a plain CSS gradient with a custom orange circle play button (`LiteYouTube.astro:18-43`); post-consent real thumbnails *are* already loaded from `i.ytimg.com` (`LiteYouTube.astro:184-211`). Missing: YouTube's chrome — red embed play button, duration badge, channel/title/views row. (The 4 SVGs in `public/videos/thumbnails/` are dead files, referenced nowhere — delete them) | Restyle cards to YouTube's embed anatomy (§3) |
| B5 | Hover → ~3 s to video | 400 ms hover delay before iframe creation (`LiteYouTube.astro:103-108`), then the player boots; nothing pre-warmed | Create the embed on hover start (drop the timer) + `preconnect` to the embed domain (§3) |
| B6 | Consent prompts keep coming back | **Two real bugs.** (a) The dialog's keydown handler is removed via `overlay.addEventListener('remove', …)` (`LiteYouTube.astro:356-357`) — the DOM never fires `'remove'`, so the handler leaks and **any later Escape press stores "declined"** (repro: accept → close an award lightbox with Esc → next video click prompts again). (b) After an explicit decline, every card click re-opens the modal anyway (`addIframe`, `LiteYouTube.astro:218-221`) — which also contradicts the site's own privacy policy ("you will not be asked again unless you clear your browser storage", `[legal].astro:45`) | Remove the listener in `finish()`; make DECLINED mean quiet link-outs forever (clicks open youtube.com); keep the existing one-shot first-visit dialog (`initConsentGate`, `LiteYouTube.astro:369-385`); add a footer "change video preference" link (GDPR Art. 7(3) wants easy withdrawal) |
| B7 | Hero H1 says nothing | `Hero.astro:29` renders `hero_greeting` ("Hi, I'm Tom") as the only H1; name+role appear nowhere in any heading | H1 = "Tom Szenessy", role + proof chips as in §1.2 |
| B8 | Nav rail renders as colored blocks on `/` | The scroll-spy rail ("the scrollbar" that worked on main). Refresh made each dot a 44×44 tap target (`Navigation.astro:26-34`) but the root page's script still paints `bg-accent`/`bg-text-muted` on the whole `<a>` (`src/pages/index.astro:150-160`) → one orange + four grey squares. The fixed script (classes on the inner dot) exists only in `src/pages/[lang]/index.astro:165-180` | Port the fix — better: extract one shared script component, or redirect `/` → `/en/` (root currently just canonicalizes to `/en/`, `index.astro:17`); add `rounded-full` as belt-and-braces |
| B9 | Share preview looks broken | `public/og-image.png` (1200×630) is the same stretched floating head in a black circle — it's the preview for **every** link share (`BaseLayout.astro:64,70`) | Redesign the OG card: name, role, one proof point, brand cream background, properly framed photo |

### P1 — quality and correctness

| # | Bug | Root cause | Fix |
|---|-----|-----------|-----|
| B10 | Consent dialog is English-only | Dialog copy is hardcoded in JS (`LiteYouTube.astro:270-277`); the translated `youtube_consent_*` keys (EN/DE/ES, `translations.js:27-31` etc.) are dead code — German recruiters get an English legal modal | Wire the existing keys; keep copy in sync with `[legal].astro` |
| B11 | LinkedIn URLs disagree | `BaseLayout.astro:32` (`…/tom-szenessy-ab34a6276`) vs `Navigation.astro:58` (`…/tom-szenessy`); the latter is what Google indexes | Use `https://www.linkedin.com/in/tom-szenessy` everywhere |
| B12 | `<title>` is a joke | `translations.js:4`: "Just a chill, friendly Business Informatics Student" | `Tom Szenessy — Business Informatics @ TUM | Projects & Videos` |
| B13 | Awards lead with a participation ribbon | First card is "hackaTUM 2025 — Participation" (`Awards.astro:14`) *above* the Jugend forscht 2nd prize + CIB award | Order: strongest first (Jugend forscht ×2 → BwInf → Math Olympiad → …); participation last. Also: award cards are non-focusable `div`s (`Awards.astro:43`) — make them keyboard-operable buttons with focus management in the lightbox |
| B14 | Discoverability plumbing missing | No `sitemap.xml`, no `robots.txt`, no `404.html`, **zero hreflang tags** despite an EN/DE/ES site | Add all four (`@astrojs/sitemap` + a `404.astro` + hreflang alternates). Only then may "SEO/i18n" appear as a skill chip — view-source disproves it today |
| B15 | Video JSON-LD non-compliant | `Projects.astro:79-85`: VideoObject lacks `description` + `thumbnailUrl` (required for video rich results) | Complete the fields from `videos.json` |
| B16 | Shorts leak into the video grid | `MAXRES_MIN_W/H` declared but unused (`fetch-videos.mjs:32-33`); `hasLandscapeThumb` only checks `res.ok` — Shorts *do* have maxres thumbs. Verified: 3 of the feed's Shorts are in `videos.json` (ranks 3, 6, 8) and **rank 3 is one of the 4 videos displayed on the site** | Detect Shorts properly — from the feed URL (`/shorts/`) or duration via yt-dlp at snapshot time, not thumbnail probing |
| B17 | `prebuild` rewrites `videos.json` every build | `package.json:5` → `fetch-videos.mjs:149-151`; any manually captured fields (durations!) will be wiped | Make fetch-videos merge/preserve manual fields |

### P2 — the polish pack a meticulous recruiter catches

- **DE copy errors** (German recruiters read this!): `about_p1` is broken German ("Ich mag alles was mit Technik zu tun hat arbeite gerne…", `translations.js:224-225`); ES keeps "Kangaroo Mathematics" untranslated (`translations.js:488-489`); fix wording pass over DE/ES.
- **Dead hover class** `text-accent-text-text` (typo ×3: `Projects.astro:122,157`, `About.astro:195`) — hover color changes silently do nothing.
- **Impressum** cites "§ 5 TMG" (superseded by § 5 DDG since May 2024); contact email differs between pages: `tom@szenessy.de` (`Contact.astro:33`, `Footer.astro:14`) vs `tom.szenessy@tum.de` (legal pages) — one identity everywhere.
- **Accessibility/robustness:** no `prefers-reduced-motion` anywhere (reveal animations, particle loop `index.astro:108-131`, `scroll-smooth`); `Intl.NumberFormat('en')` hardcoded on DE/ES pages (`Projects.astro:118`); duplicate `hero_stack` key (`translations.js:190,192`); `bg-fixed` parallax jank on iOS (`ParallaxQuote.astro:16`); delete the 4 dead SVGs in `public/videos/thumbnails/`.
- **Browser scrollbar** (your "scrollbar" complaint — the CSS was **not** removed; `global.css:82-92` is byte-identical to main): three real causes for "looks broken now": (a) the new **dark consent overlay is scrollable** (`LiteYouTube.astro:262`) and shows the cream track + orange thumb over a black scrim; (b) the rule set is incomplete — no `height`/`::-webkit-scrollbar-corner`, and no `scrollbar-color`/`scrollbar-width` so Firefox ignores it entirely; (c) classic-vs-overlay scrollbar differences across browsers. Fix: add `html { scrollbar-color:#d07a3d #f6eee2; scrollbar-width:thin }`, `::-webkit-scrollbar{height:8px}` + corner rule, and a **dark scrollbar for the consent overlay and award lightbox**. (If you meant the side-nav dot rail, that's B8 — both get fixed.)
- **Legacy root `index.html` is fully broken on this branch**: its image refs (`./public/Fotos/*`, `./public/Preise/*`) point at files moved to `src/assets` → 404s, and its scripts live only in `legacy/`. It's not part of the Astro build — delete or archive it (it also carries the non-square favicon link from B1).
- **Orphan award asset**: `src/assets/Preise/hackaTUM 2025 certificate.pdf` (634 KB) is referenced nowhere — attach it to the hackaTUM award card's lightbox like the others.
- **Smaller still**: `ParallaxQuote.astro:22`/`PeekingTom.astro:16` pass `width/height` props that don't match the photo's intrinsic ratio (masked by `object-cover` today); `Awards.astro:31` decorative quote is ~1.9:1 contrast; `README.md` still names the old fonts (Bricolage Grotesque); `.gitignore` ends with a dangling comment; `hackaTUM certificate` label says "Participation" — consider "hackaTUM 2025 — MunichPulse (team of 5)".

---

## 3. YouTube section — buildable spec

Target: a visitor can't tell the card from a real YouTube embed until they touch it — and after one consent answer, everything just plays.

**Card anatomy (YouTube's own chrome):**
- 16:9 thumbnail (`i.ytimg.com/vi/ID/maxresdefault.jpg`, `hqdefault` fallback — already implemented), 12px radius.
- YouTube's **red embed play button** (`#f00` rounded rect ≈68×48, white triangle) centered — not a custom circle.
- **Duration badge** bottom-right (`rgba(0,0,0,.8)`, white 12px semibold); hide the badge when duration is unknown.
- Below: **channel · title · views · age** in YouTube's text style ("Tom Szenessy · 3.7K views · 1 month ago"), with locale-aware number + relative-date formatting for EN/DE/ES.

**Behavior:**
1. **One consent dialog, on first visit** (exists: `initConsentGate`), localized via the existing `youtube_consent_*` keys (B10). Accept → everything loads with zero further prompts. Decline → cards become quiet link-outs to youtube.com **forever** (fix `addIframe`, B6); footer link "change video preference" reopens the choice.
2. **Embed domain: `youtube-nocookie.com` everywhere** (hover + click) — required by the site's own privacy policy, `[legal].astro:45`.
3. **Hover (desktop):** create the iframe **immediately** (remove the 400 ms timer, `LiteYouTube.astro:103-108`) with `autoplay=1&mute=1&controls=0&loop=1&rel=0&modestbranding=1`; remove on mouse-leave **after N seconds idle** (today every re-hover pays a full cold player load). On click, **upgrade the warm preview iframe in place** (switch params to `controls=1&autoplay=1`) instead of tearing it down and creating another cold iframe (`renderIframe` does the latter today).
4. **Touch:** first tap = muted inline preview (mobile autoplay policy allows muted); the player's own controls give sound/fullscreen. No hover semantics on touch — skip the timer there entirely.
5. **Performance & compliance:** `preconnect` to `www.youtube-nocookie.com` + `i.ytimg.com` once consent exists and the videos section approaches the viewport (`IntersectionObserver`, `rootMargin: 200px`). **Gate preconnect behind consent** — a preconnect is itself a third-party request. **No hidden pre-created iframes** — four pre-warmed players means four player-JS downloads and clashes with the site's own 89 MB → 7.4 MB performance story.
6. **Interaction clarity:** exactly two hit areas per card — the thumbnail (hover preview / click to play) and one "Watch on YouTube ↗" link below. Remove the current duplicate link.
7. **JS-off fallback:** cards render as plain links to the watch URLs.

**Data (`npm run videos`):** keep the top-4-by-views ranking (your decision). Extend `fetch-videos.mjs` to: (a) detect Shorts by **duration** (yt-dlp at snapshot) not thumbnail probing (B16), (b) capture `duration`, `channelName`, `thumbnailUrl` into the snapshot, (c) **preserve** manual fields across builds (B17).

**Compliance:** the GDPR/TTDSG gate stays (a real legal risk for a German site) — but as *one* first-visit dialog plus an in-page withdrawal link, which is also exactly the experience you asked for.

---

## 4. What to include (content plan)

Principle: **fewer, proven, linked items beat a long list.** Every shown item gets a working link; every claim links to third-party proof. Unverifiable → cut.

### 4.1 Projects — keep 6, fix one link

| Project | Proof | Verdict |
|---|---|---|
| **RoadTax** — hex multiplayer strategy game, server-validated moves ("road tags" = this) | ✅ [roadtax.app](https://roadtax.app/) | **Flagship** — current work, live, playable, real full-stack multiplayer |
| **Mino** — AI notes → mindmaps, **Jugend forscht 2024: 2nd prize + CIB Special Prize** | ✅ [mino.ink](https://mino.ink/) · [repo](https://github.com/TomSzenessy/MinoAI) · 🏆 [CIB press](https://www.cib.de/en/partizipation-record-jugend-forscht-iberia-2024-lisboa/) | **Origin story** — award + live product + independent press. Link the article |
| **WorldFolder** — self-hosted game-server platform | ✅ [worldfolder.com](https://worldfolder.com/) (renders a real product page: "Minecraft Server Hosting — Players Just Join") · [SaaSHub](https://www.saashub.com/worldfolder-status) | **Business signal** — "built a shipping product" |
| **ToMindMap** — Obsidian mind-map plugin | ✅ [GitHub](https://github.com/TomSzenessy/Mindmap-Plugin-for-Obsidian) (active, MIT) | **Open-source artifact** with install story |
| **SideStroll** — AI quest engine (TUM.ai Makeathon 2026, team of 5) | ✅ [sidestroll.com](https://sidestroll.com/) · teammate LinkedIn posts | **Keep — but merge its story with the Makeathon card** (currently told twice as if unrelated) |
| **Agentic Trading Bot** — LLM proposes, Python validates risk | ❌ repo 404s today | **Hidden until the sanitized repo is public** (your decision); the card returns the moment the link works |

Cut (per your decision + verification): RoText ≈ transcription artifact of *RoadTax*; the "self-hosted email" thing has no trace. **StuStandUp is real** — it goes in "Beyond the Screen" as a personality line (done in §1.4), never as a project card.

Other upgrades:
- **Ecosia internship copy** is currently "two-week internship focused on software development"; per your CV you built an **FAQ chatbot prototype with source links and a clickbait/"polemic score" news widget**. Concrete beats generic — this one rewrite makes the card impressive.
- **MunichPulse & Drontom: out of sight** (your call). Remove the MunichPulse repo link from the hackaTUM card and add no Drontom line; the hackathon stays as a plain narrative entry with its certificate.

### 4.2 Awards — keep 8, re-order, add external proof

Current set is the right size (17 certificates exist; more would dilute). Re-order strongest-first (B13). Link external proof: [CIB article](https://www.cib.de/en/partizipation-record-jugend-forscht-iberia-2024-lisboa/) (Jugend forscht) and [Costa del Sol Online](https://costadelsol-online.es/abifeier-deutsche-schule-malaga-2025/) (names him among five students with the "dream grade 1.0"). Optional: one pull-quote from the CIB piece ("Tom gave a passionate and agile presentation…") as social proof in About — verify the mentor name before quoting it.

### 4.3 Skills — only what the projects prove

Add: **Android/Kotlin + Play Store release** (Mino app, MunichPulse — surface `skill_kotlin`), **LLM agents / RAG / vector search** (Mino, SideStroll, trading bot — sharper than "Machine Learning"), **realtime multiplayer / server-authoritative state** (RoadTax), **Linux self-hosting + K8s ops** (WorldFolder), **i18n/SEO/web-perf** — *only after B14's hreflang/sitemap actually ship*. Nothing padding-shaped; recruiters check.

### 4.4 Chinese A1

Keep the claim in Languages (recent, distinctive) + the planned Tsinghua exchange as a forward-looking line. **No certificate scan** — your consistency argument is right: none of the other language claims carry certificates (German, English C2, Spanish C1), so a single Chinese scan would look odd; portfolios state language levels as copy, not documents.

---

## 5. Discoverability (Google + AI)

Today, a "Tom Szenessy" search shows: LinkedIn → GitHub → the CIB award article → SaaSHub/WorldFolder → teammate posts — **the portfolio doesn't rank yet**. Goal: [1] portfolio, [2] LinkedIn, [3] GitHub, [4] CIB article.

1. **One canonical identity sentence**, verbatim on site hero, LinkedIn About, GitHub bio, YouTube About:
   *"Tom Szenessy is a Business Informatics student at TU Munich who builds and ships full-stack products — games, plugins and self-hosted platforms."*
2. **Fix Person JSON-LD**: add `image`, `alumniOf`, `knowsAbout`, stable `@id`, and the corrected LinkedIn `sameAs` (B11).
3. **Every fact also as visible prose** — LLMs read text, not JSON-LD.
4. **Third-party anchors on the page**: [CIB article](https://www.cib.de/en/partizipation-record-jugend-forscht-iberia-2024-lisboa/), [Costa del Sol article](https://costadelsol-online.es/abifeier-deutsche-schule-malaga-2025/), [Devpost](https://hackatum25.devpost.com/project-gallery?page=5), [SaaSHub](https://www.saashub.com/worldfolder-status).
5. **Plumbing** (B14/B15): sitemap, robots.txt, hreflang alternates, 404 page, complete VideoObject, `dateModified`.
6. **Profile alignment**: identical name/photo/one-liner everywhere. Verified today: GitHub has **no bio and no website link** (`"blog": "", "bio": null`) — add both. YouTube "About" gets the portfolio link too.
7. `<title>` per B12.

---

## 6. Decisions & remaining questions

### Decisions taken (2026-10-06)
- **Unverifiable projects → cut.** ("RoText" ≈ transcription artifact of *RoadTax*; the "self-hosted email" memory has no trace anywhere.)
- **StuStandUp → real** (student stand-up comedy club): one personality line in "Beyond the Screen", not a project card.
- **Trading bot → publish a cleaned-up repo**; card hidden until the link works.
- **Drontom & MunichPulse → not visible** (your call): no Drontom line, MunichPulse links removed from the hackathon card.
- **Chinese A1 certificate → not added** (consistency: no other language claim carries a certificate). Claim stays in copy.
- **Poker → dropped.**
- **Videos → objective top-4-by-views**, fetched from YouTube at build time.
- **Hobbies → one compact line** (§1.4).
- **No job-seeking line** — the goal is visibility; CTA = "Get in touch".
- **Hero photo** — decided by visual evaluation (see §7 step 4); the passport cut-out is out regardless (it is the "squished, no background" complaint).

---

## 7. Implementation order

1. **Consent fixes** (B6): kill the keydown leak, DECLINED = quiet link-outs forever, footer withdrawal link, align `[legal].astro` copy. *(Your exact complaint, correctly diagnosed.)*
2. **De-duplicate `/` vs `/en/`** and fix the root-page rail blocks (B8) — one shared script or a redirect.
3. **Trading-bot link** (B3): publish repo or hide card.
4. **The three face images** (B1/B2/B9): regenerate the portrait asset with a uniform crop (it is measurably ~4–6% stretched today), restore a circle backdrop, then derive favicon tile (plus real `favicon.ico` + cache-busted URL), hero avatar, og-image from one good square photo.
5. **Localize the consent dialog** + delete dead files/keys (B10).
6. **First screen** (B7/B12): H1 with name, role, proof chips, availability/CTA.
7. **Awards re-order + keyboard access** (B13).
8. **Discoverability plumbing** (B14/B15) + profile alignment (§5.6).
9. **fetch-videos.mjs** (B16/B17): duration-based Shorts detection, preserve manual fields; then the YouTube card chrome (§3).
10. **Polish pack** (P2 table): scrollbar completion (incl. dark overlay scrollbar), delete/archive the legacy root `index.html`, attach the orphan hackaTUM certificate, DE/ES copy pass, typo classes, Impressum/email, reduced-motion, locale formatting.

---

## 8. v3 revision — post-deploy review (2026-10-06)

The owner reviewed the deploy preview; these decisions supersede earlier ones where they conflict:

1. **Hackathon copy: never frame as a loss.** The "Lost to an unrehearsed demo" / "Didn't place" journey-beats are gone — the research-supported journey clause lost to a simpler rule from the owner: describe what was *built* and the positive outcome ("Built SideStroll end to end… pitched the working app on the big stage").
2. **StuStandUp, Tom's Time Bluff and the Agentic Trading Bot are project cards** (8 cards now). Link targets are per-project: live site if it exists (Time Bluff → [toms-time-bluff.com](https://toms-time-bluff.com/)), GitHub for strictly-code projects (ToMindMap), and an accessible in-page detail dialog when there is no public URL (StuStandUp, Trading Bot). The dead AlpacaTradingBot repo link is gone entirely.
3. **"Beyond the Screen" removed** — hobbies were costing attention without earning it. (Poker was already out.)
4. **Micro-quotes float in the beige background** (decorative, rotated, low-contrast, `xl+` only) instead of sitting inside the content cards.
5. **Hero is exactly one fold** (`min-h: calc(100svh - nav)`), so the next section starts at the fold for a consistent first impression (verified: section top 901px at 900px viewport).
6. **Hover never plays video.** Hovering only preloads the embed player invisibly behind the thumbnail (autoplay=0); playback starts strictly on click (instant, since the player is warm).
7. **Hackathons sit in the same grid row as Experience** for symmetry; Milestones became a full-width 4-up band.

Verified end-to-end with two DevTools Protocol QA suites (11/11 new-behavior checks, 23/23 regression checks), including the detail dialog's focus management, zero quote/card overlaps, and the exact fold position.

---

## Sources

See `research-positioning.md` for the fully cited research brief (Ladders eye-tracking, Profy.dev survey, Sezer et al. 2018, Cuddy/Fiske, Nault et al., Pratfall effect, GEO/KDD 2024, exemplar sites).

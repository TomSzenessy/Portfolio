# Research: How a 3rd-semester TUM CS student should "sell" himself on a portfolio site

Research basis for the redesign. Goal: "Anyone who Googles my name — recruiter, AI assistant, or a potential friend — is immediately impressed and wants to hire me." Constraint: convince, don't cram.

---

## 1. What recruiters actually look at (and for how long)

**The 6–7.4 second scan is real — for resumes.** Ladders' eye-tracking studies ([2018 PDF](https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf), [PRNewswire release](https://www.prnewswire.com/news-releases/ladders-updates-popular-recruiter-eye-tracking-study-with-new-key-insights-on-how-job-seekers-can-improve-their-resumes-300744217.html); original [2012 study](https://www.prnewswire.com/news-releases/theladders-reveals-that-job-seekers-have-six-seconds-to-succeed-143629046.html)) found recruiters spend **7.4 s (2018) / 6 s (2012)** on an initial screen, and **~80% of that time on six fields: name, current title/company, previous title/company, both date ranges, education**. Everything else is keyword pattern-matching. There is no equivalent peer-reviewed eye-tracking study for portfolio sites — the honest synthesis ([grigora.co evidence review](https://www.grigora.co/blog/do-recruiters-look-at-portfolio-websites/), [showproof.io scan guide](https://showproof.io/guides/how-recruiters-read-developer-portfolios/)) is that the *pattern* (fast, top-left-weighted, binary keep/close decision) transfers, and portfolio pages get even less time because scrolling is slower than reading.

**Reading pattern: F-shape.** NN/g's F-pattern research (summarized with portfolio implications in [showproof.io](https://showproof.io/guides/how-recruiters-read-developer-portfolios/)): (1) a long horizontal sweep across the top, (2) a shorter second sweep, (3) a vertical sweep down the left edge catching the *first words* of each block. Consequences: hero is premium real estate; keep key text left-aligned; lead each section with its most important word/phrase ("TUM Computer Science" beats "I am a student at…").

**Where attention lands** (showproof's engagement estimates): hero ≈ 100% → featured project ≈ 60% → GitHub activity ≈ 40% → testimonials ≈ 30% → case studies ≈ 15% → about/bio ≈ 10%; contact gets high engagement *only once the visitor has decided yes*. The hero + one featured project do the heavy lifting. Optimize those first.

**Do portfolios convert? The evidence is nuanced.**
- [Profy.dev survey](https://profy.dev/article/portfolio-websites-survey) (300+ recruiters & React team leads contacted, 60+ answered): **93% would likely look at an inexperienced candidate's portfolio site**, but **51% said a candidate without one has the same chances**; a portfolio only helps if it's good and *maintained* — "an ugly or broken page just hurts their chances." Website design is itself judged as work product.
- [Minenko (2025), a thesis interviewing IT recruiters](https://exa.ai/library/publication/665g3s0jvxf): standalone flashy portfolios are *not* decisive for juniors; a strong CV with **one or two real projects** plus technical-interview performance is what gets hired.
- NACE Job Outlook 2026 (cited in [grigora.co](https://www.grigora.co/blog/do-recruiters-look-at-portfolio-websites/)): employers "want to see examples," not skill lists.
- Hover 2017 survey (n=121 hiring professionals, cited in [grigora.co](https://www.grigora.co/blog/do-recruiters-look-at-portfolio-websites/)): 86% would visit a portfolio when offered; 71% said its quality influences the decision (note: sample skewed toward domain-owning customers).
- The third moment matters enormously: **Harris Poll for CareerBuilder 2017** (cited in [grigora.co](https://www.grigora.co/blog/do-recruiters-look-at-portfolio-websites/)): **69% of hiring managers use search engines to research candidates; 57% are less likely to interview someone they can't find online.**

**Takeaways for this project:** one page that answers *who / what he does / proof* within the first screen; exactly **one featured project** with a live link and a one-line outcome, not a project grid; freshness signals (current semester, recent commits); fast load; zero broken links. The site's job is not to contain everything — it's to make the CV and the Google result believable.

## 2. Own-your-name SEO, E-E-A-T, structured data

- **Google's own guidance** ([Creating Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en/en/searchqualityevaluatorguidelines.pdf)): people-first content, a clear site purpose, demonstrated first-hand **experience**, visible **authorship** ("Who": bylines that lead to info about the person), transparent "How", and a people-serving "Why". **Trust is the most important E-E-A-T pillar.** A personal site is literally one of Google's listed beneficial page purposes ("to demonstrate a personal experience, perspective, skill").
- **Person schema (JSON-LD)** with `name`, `jobTitle`, `image`, `sameAs`, `alumniOf`, `knowsAbout`, a stable `@id` feeds Google's Knowledge Panel; validate with Google's Rich Results Test. Critically, [practitioner analysis](https://slobodandekanic.com/how-to-rank-your-name-on-google/) notes **LLMs read the visible prose, not just the JSON-LD** — every fact must appear in plain text as well. `sameAs` should list LinkedIn, GitHub, and any directory/award pages that corroborate the same person.
- **Consistency is the mechanic.** Same full name, same photo, same one-sentence self-description across the site, LinkedIn, GitHub, and any award/directory listing ([instantpress.co](https://www.instantpress.co/blog/how-to-rank-for-your-name-in-google), [path.cv](https://path.cv/blog/rank-for-your-name)). Mismatched titles ("CS student" vs "software developer") split the entity and slow ranking.
- **Own the first result.** A one-page site on `firstname-lastname.de` with clear identity statements typically reaches top-3 for the name within 2–6 months given a few inbound links (LinkedIn bio, GitHub profile, university/hackathon pages) ([instantpress.co](https://www.instantpress.co/blog/how-to-rank-for-your-name-in-google)). For most names the SERP is weakly contested — one good page wins ([path.cv](https://path.cv/blog/rank-for-your-name)).
- **Credibility optics matter:** real headshot (same everywhere), custom favicon, professional meta/OG tags, no stale dates. AI answer engines cite the URLs that rank for your name — if you own them, you control the summary ([instantpress.co](https://www.instantpress.co/blog/how-to-rank-for-your-name-in-google)).

## 3. Likable ≠ arrogant: the psychology

**Humblebragging backfires — worse than plain bragging.** Sezer, Gino & Norton, [*Humblebragging: A Distinct—and Ineffective—Self-Presentation Strategy*](https://www.hbs.edu/faculty/Pages/item.aspx?num=52825), JPSP 114(1), 2018 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/28922000/), [PDF](https://www.hbs.edu/ris/Publication%20Files/Sezer%20Gino%20Norton%20Humblebragging_0533fa02-7fcd-4585-91c9-b7281174edf9.pdf)): across 9 studies, bragging masked by complaints or fake humility ("I still can't believe they picked *me*…") **reduces liking, perceived competence, and cooperation — significantly more than straightforward bragging** — because it reads as insincere. Complaint-based humblebrags are the worst. ⇒ Never mask achievements in disclaimers. Plain, factual statements of achievement are the *safe* option.

**Warmth first, competence second.** Fiske, Cuddy & Glick's Stereotype Content Model ([Trends in Cognitive Sciences 2007](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(06)00329-9); [Wikipedia summary](https://en.wikipedia.org/wiki/Stereotype_content_model)): all first impressions run on two axes — **warmth** (intent) and **competence** (ability) — and warmth is judged first and weighted more. Critically, **high competence + low warmth triggers envy**, the exact failure mode of an award-laden student site. Every competence signal needs a nearby warmth cue (first person, humor, team credit, gratitude, hobbies).

**Journey beats trophy list.** Nault, Sezer & Klein (7 studies, 2,500+ participants; summarized in [IE Insights](https://www.ie.edu/insights/articles/why-telling-your-story-beats-listing-your-wins/)): professional intros that include *journey* elements — challenges, growth, what was learned — are rated **significantly warmer and more likable, with no loss of perceived competence**, and make readers want to connect/recommend. Effects are strongest in **text** (exactly what a website is). **One or two well-chosen journey sentences suffice.** Also memory mechanics ([personal-branding storytelling](https://www.instantpress.co/blog/personal-branding-storytelling)): highlight reels without tension are forgotten; a compact "origin → turn → proof" story is what people repeat to others.

**The Pratfall effect.** Aronson, Willerman & Floyd 1966 ([paper](https://link.springer.com/content/pdf/10.3758/bf03342263.pdf); [Wikipedia](https://en.wikipedia.org/wiki/Pratfall_effect)): a clearly superior person becomes **more** likeable after a small clumsy blunder (it humanizes the "too good" figure); the same blunder hurts an average person. Caveats: the imperfection must be *minor*, authentic, and adjacent to established competence; observer self-esteem and blunder size moderate it. ⇒ One small, true imperfection (a quirky hobby, a failed first attempt, a "currently learning" line) is likability insurance — but never fake it.

**Self-deprecation: use sparingly.** Recent preregistered studies ([Self-Deprecation, person-perception paper](http://static1.1.sqspcdn.com/static/f/409296/28698143/1756836974543/OJC_SelfDep.pdf?token=eXObop5m%2BR%2FMNxSXVyhF7lNjWig%3D)) find perceivers **take self-deprecation literally**: for people believed to be of high standing it lowers perceived ability, likability, and authenticity; its charm only works for people of low standing. Humor helps, though: [Bitterly et al.](https://faculty.wharton.upenn.edu/wp-content/uploads/2020/02/The-impression-management-benefits-of-humorous-self-disclosures-How-humor-influences-perceptions-of-veracity..pdf) show that pairing humor with a negative disclosure ("I'm not great at X — that's where I draw the line") boosts warmth *and* competence. ⇒ Don't downplay elite achievements ("just a small competition"); self-deprecate only about non-core, visible stuff (spilled coffee-grade, not "my code is probably bad").

**Third-party evidence is the humble channel.** Because any first-person superlative risks both bragging and humblebrag perception, the low-risk pattern is: state the verifiable fact once, without adjective inflation, and link the evidence (award page, video, repo, jury citation). Let "2. Platz, Bundeswettbewerb Informatik" stand naked; the reader supplies the impressiveness. Show-don't-tell vignettes beat attribute claims ([ghostwriting/storytelling analysis](https://workbravely.substack.com/p/3-lessons-executive-ghostwriting)).

## 4. Hobbies: include them — compact, specific, strategically chosen

- **Extracurriculars are hiring signals with real effects.** A 2025 experimental study in the [Journal of Personnel Psychology](https://econtent.hogrefe.com/doi/full/10.1027/1866-5888/a000376) (gaming vs. team sport on resumes) found **team sports raised hirability and resume-quality ratings** vs. gaming, regardless of proficiency; team sports are credited with teamwork/leadership/discipline signals (Tanguay et al. 2012, cited therein). Signaling theory (Spence): what you list implies traits — but rater biases mean some activities (e.g. gaming/gambling-adjacent ones) can misfire even when skill-building.
- **Cultural matching is real**: Rivera's hiring research and follow-ups ([review of similarity-attraction in hiring](https://link.springer.com/article/10.1007/s11301-022-00313-5); [Rivera-type cultural-matching study](https://www.academia.edu/89655500/The_Fit_Interview_and_Cultural_Matching_Examining_Equity_in_Hiring_Processes_in_Law_Firms_in_Canada)) show recruiters favor candidates whose **hobbies and lifestyles resemble theirs** — interests give interviewers the "in" for rapport. An interest line is a conversation-starter slot: recruiters and interviewers report starting there ([Wake Forest alumni career post](https://alumni.opcd.wfu.edu/2018/03/this-easy-resume-trick-will-help-you-land-more-interviews/); practitioner consensus in recruiter LinkedIn threads: "once you're in the room, you are the pitch, not the paper").
- **Specificity beats generic labels.** "Volleyball" is fine; "clătite/Romanian crêpes" beats "cooking"; "saltwater fly fishing" beats "fishing" ([Wake Forest](https://alumni.opcd.wfu.edu/2018/03/this-easy-resume-trick-will-help-you-land-more-interviews/)). Practical rules from practitioners: **one line only**; keep only things you can talk about for two minutes; avoid partisan/controversial items.
- **Signal map for his specific list:** team sports (volleyball) → teamwork; racquet sports (tennis, table tennis, padel) → competitive but social; martial arts (3 yrs taekwondo, 2 yrs judo, 1 yr karate) → discipline + long-term commitment + curiosity across styles; piano → deliberate practice/patience; board games → strategic thinking; poker → probability/game-theory mindset — **but** it is the one item with gambling connotations (analogous to the gaming-study rater bias), so present it analytically ("poker as a study of decision-making under uncertainty") or drop it.
- **Recommendation:** *include*, but as a single compact "Beyond the screen" block of 1–2 lines (optionally with one small candid photo), placed after the work — never above it. This block is also where the Pratfall/humanizing effect lives: it's the likability valve for an otherwise elite-achievements page.

## 5. AI-readiness: designing for the summarizer

- **GEO research** ([Aggarwal et al., GEO: Generative Engine Optimization, KDD 2024](https://dl.acm.org/doi/10.1145/3637528.3671900), [arXiv](https://arxiv.org/pdf/2311.09735)): content that includes **citations, quotations, and concrete statistics** gets up to **40% more visibility** in generative-engine answers; authoritative, fluent phrasing also helps.
- **Competitive GEO** ([What Gets Cited, 2026](https://dl.acm.org/doi/pdf/10.1145/3805712.3808445), 252k trials across 6 LLMs): the biggest citation drivers are **topical relevance, freshness (recent timestamps), completeness, and claims backed by evidence**; purely formatting edits have little impact. ⇒ Keep the site dated/current; back claims with links.
- **Entity clarity.** Practitioner guidance for AI-era name searches ([slobodandekanic.com](https://slobodandekanic.com/how-to-rank-your-name-on-google/); [AEO for developers](https://abdullah-faheem.vercel.app/blog/answer-engine-optimization-aeo-developers-2026); [agenticism.co on cross-platform legibility](https://www.agenticism.co/post/ai-search-chatgpt-gemini-perplexity-now-surfaces-candidates-experts-by-consistent-cross-platform)): AI assistants write "who is X" paragraphs from the clearest, most-repeated, cross-corroborated facts. Best practices converging:
  1. One **quotable identity sentence** near the top: *"[Name] is a 3rd-semester Computer Science student at TU Munich who builds …"* — the sentence an AI can lift verbatim.
  2. The same sentence, word-for-word, on LinkedIn, GitHub bio, and any profile (models trust repetition across independent sources).
  3. **Plain-prose facts + Person schema**; a compact "fact sheet"/FAQ block ("What has he built? What is he looking for?") with direct 40–60-word answers.
  4. **Third-party links** (award sites, hackathon results, repos, videos) as citation anchors — LLMs prefer verifiable claims with sources.
  5. Clear availability/CTA ("Open to working-student roles / internships from …") so a recommendation has an obvious next step.

## 6. Exemplar sites that balance professional + personal

- **[Brittany Chiang](https://v4.brittanychiang.com/)** (cited in [wearedevelopers roundup](https://www.wearedevelopers.com/magazine/161-top-23-web-developer-portfolio-examples-to-inspire-your-own), [levamo roundup](https://levamo.com/blog/web-developer-portfolios-inspiration/)): the canonical junior-dev reference. Hero: "Hi, my name is / Brittany Chiang. / I build things for the web." + one-sentence positioning + current employer + a *single* CTA ("Check out my work"). About is warm first-person prose ending with off-duty personality ("When I'm not in front of a computer…"). Restrained dark design; experience timeline; everything scannable in one page.
- **[Lee Robinson](https://leerob.com/)**: one-paragraph bio that interleaves credential ("engineer and writer… ML at SpaceX, formerly Cursor/Vercel… coding for 15 years") with personhood ("a husband to my much cooler wife, a father to two radiant daughters, and a massive music fan"). Has a ["Things I Believe" page](https://leerob.com/beliefs) — a high-warmth, high-memorability device.
- **[Josh Comeau](https://www.joshwcomeau.com/about-josh/)**: "Hi there! I'm Josh. I started building on the web in 2007 and never stopped." Playful, teacherly tone; showcases "cool / weird stuff" (generative art machine) alongside senior credentials — competence wrapped in curiosity.
- **[Bruno Simon](https://levamo.com/blog/web-developer-portfolios-inspiration/)**: playable 3D car portfolio — extreme "show, don't tell"; the site *is* the proof of skill (a caution: gimmicks only work if flawless).
- Common pattern: **one page, one voice, one CTA; competence in the top half, personality in the bottom third; personality is specific and concrete, never "I'm passionate and hardworking."**

---

# Positioning playbook (recommendation)

## Hero positioning strategy

Answer three recruiter questions in the first screen (per showproof): *what do you do, for whom, with what?* Then one warmth cue and one CTA. Template:

> **[First Last]** — Computer Science student at TU Munich building **[specific thing: e.g. reliable web tools / AI-powered …]** with **[stack: TypeScript, React, Python]**.
> Two-time national competition finalist · Currently looking for a working-student role from [month].
> **[One warm line]** When I'm not coding, I'm on the volleyball court or trying to finally master a Chopin nocturne.
> **[CTA]** → Email me / See my best project / Lebenslauf (PDF)

Rules: name + "Computer Science student at TU Munich" must be literal text (Google + LLM quotability); stack keywords visible without scrolling; one dominant CTA and one secondary; ≤ 15 words in the main headline.

## Tone guidelines

**Do:** first person, present tense, concrete nouns, numbers; gratitude and team credit ("with a great team of four"); curiosity framing ("I wanted to understand how X works, so I built…"); short sentences; one mild, true imperfection or "currently learning" line; dry humor if it's genuinely his voice.

**Don't:** superlatives about himself ("passionate", "exceptional", "world-class", "genius"); humblebrags ("I guess I just got lucky…", "still can't believe they nominated me"); fake self-deprecation of real achievements ("my *little* project"); adjective inflation around award names; exclamation marks; German CV clichés ("zielstrebig", "teamfähig"); anything he wouldn't say out loud to a stranger.

## How to phrase elite achievements (Math Olympiad, Jugend forscht, Bundeswettbewerb Informatik, hackathons, martial arts)

1. **Naked facts win.** Award name + rank + year + one link, no adjectives: "Jugend forscht — 2nd place, national final, 2023" not "proud winner of the prestigious Jugend forscht prize."
2. **One journey clause per achievement** (Nault/Sezer/Klein): "…after two years of weekend tinkering in the school lab" — effort, not glory.
3. **Frame as curiosity, not status:** "I got into programming through the Bundeswettbewerb Informatik — the problems pulled me in."
4. **Team/mentor credit where true** — instantly warms competence signals.
5. **Let third parties speak:** link the award site, the jury page, the demo video, the repo. The link does the bragging.
6. **Martial arts:** one line with *durations*, not belt colors: "Three martial arts so far — taekwondo (3 yrs), judo (2), karate (1); currently sticking with judo." Durations signal discipline; "so far" signals curiosity; it's a built-in Pratfall (a relatable collector's restlessness).
7. **Cluster, don't scatter:** one compact "Milestones" strip (3–5 items) beats the same awards woven into 4 paragraphs.

## Hobbies: include or not?

**Include — as one compact block ("Beyond the screen", 1–2 lines, after the work), not a section with paragraphs.** Sample line:

> Off-screen: volleyball and padel with friends, three martial arts so far (taekwondo, judo, karate), piano (slowly working through Chopin), board games, and poker — mostly as an excuse to think about probabilities.

- Keep team sports + martial arts + piano (highest-signal trio: teamwork, discipline, deliberate practice).
- Specific nouns ("Chopin", "padel") invite conversation; generic labels don't.
- Poker: keep it with the probability framing or cut it; never list it alone.
- Cut anything he can't talk about for two minutes.
- Optional: one candid photo strip — warmth at near-zero word cost.

## 8 copywriting rules

1. **5-second test:** after one screen, a stranger must be able to say "TUM CS student, builds X with Y, wants Z." Anything that delays that goes below the fold.
2. **Show, don't tell:** replace every adjective claim with a fact, link, number, or mini-story. No "passionate", "skilled", "hardworking" — ever.
3. **No humblebrags, no false humility (Sezer et al.):** plain statements of fact are more likable than achievements dressed in disclaimers. If it sounds like "I can't believe they picked me", delete and rewrite flat.
4. **Warmth within one sentence of every competence signal (Cuddy/Fiske):** team credit, journey clause, or humor adjacent to each trophy; otherwise the page reads "high competence, low warmth" = envy.
5. **One or two journey sentences per story (Nault et al.):** effort and turning points raise warmth without costing competence — especially in text.
6. **Front-load the first words of each block (F-pattern):** lead headings and paragraphs with the payload ("Bundeswettbewerb Informatik, national round 2023" not "In 2023 I took part in…").
7. **Be quotable by machines:** one canonical identity sentence, repeated verbatim on LinkedIn/GitHub; plain-text facts plus Person schema `sameAs`; every claim backed by a link (GEO: citations + stats + freshness boost AI visibility).
8. **One voice, one page, one CTA:** write like a friendly, precise human explaining his work to a smart stranger; end every section with a reason to continue and the page with an easy, warm invitation ("Write me — I answer fast.").

## Length

One scrollable page plus optional project detail pages. Depth lives behind "Read more" links (case studies serve the *second* look, ~15% of visitors), never in the first screen. Staleness is the biggest risk to a student site: put "last updated"/current-semester signals and keep GitHub visibly alive.

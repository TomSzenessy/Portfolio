# CV strategy — Oct 2026

Content lives in `build.py` (EN and DE side by side). Run `./render.sh` to regenerate `cv-*.html` and the PDFs. The script warns if either one spills onto a second page.

## What an employer wants to know, in scan order
1. **Who and what for.** Name, current role and what you're looking for. That's the header card.
2. **Hard facts at a glance.** Four number widgets: 1.0 Abitur, 4 live products, Jugend forscht prize, 5 languages.
3. **Education.** For students, recruiters always look here ([Ladders eye-tracking](https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf)).
4. **Experience.** Internships are the strongest hiring factor ([NACE Job Outlook 2026](https://naceweb.org/talent-acquisition/candidate-selection/the-key-skills-employers-seek-on-college-students-resumes)).
5. **Projects with live links.** Recruiters value personal projects above the degree (HackerRank recruiter survey).
6. **Teamwork and communication.** These are NACE's top three skills, so the "Hackathons & Teams" card shows team size and roles.
7. **Skills, languages and awards** sit in the side column as chips and dots that can be scanned in seconds.

Every item is one line of title plus one line of description. Detail belongs in the interview and on szenessy.com.

## Cut from the June 2025 CV (and why)
| Item | Why |
|---|---|
| Header date "10. June, 2025" | Dates the document. A CV carries no date. |
| Mindvalley self-development program | Reads as a lifestyle course, not a credential. |
| PHP, "basic Java", VS Code, Google DevTools, Plex, operating systems | Filler. No current project shows them. |
| TrueNAS/Plex NAS project | Superseded by WorldFolder and the Portainer GitOps homelab. |
| AI e-commerce platform "in progress" | Never shipped. Unfinished work dilutes finished work. |
| Radio antenna at age 13, Rubik's cubes, Minecraft/Factorio gaming | Age-13 item. Research shows gaming lowers hireability ratings compared with sports. |
| Känguru 116/120 (2019), BwInf 1st round | Weaker than what remains. Too many awards dilute the top one. |
| Atech 1-week internship | One week of PC maintenance. It took space from Ecosia and the projects. |
| Drontom | Hidden on the portfolio by your own decision, so it is hidden here too. |

## Added
TUM degree, Chinese and the planned Tsinghua exchange · WorldFolder · RoadTax · Mino v2 · trading bot · ToMindMap · AI_TEMPLATE · EHL Finals · TUM.ai Makeathon · hackaTUM · CHECK24 GenDev · StuStandUp · EYP · availability line · Chinese A1.

## Evidence behind each claim
- Commit counts come from the GitHub contributors API on 2026-10-15: sidestroll 252 of ~271, RoadTax 178, worldfolder 62, AI_TEMPLATE 306.
- All live URLs returned HTTP 200 on 2026-10-15.
- WorldFolder: scale-to-zero, wake-on-ping and Firecracker are taken from the repo README. "Sub-second wake" is not claimed because it was never measured.
- RoadTax: the GA-trained policy network is documented in its README.
- Jugend forscht 2nd prize + CIB prize: certificate in `src/assets/Preise` and the CIB press article.

## Open questions — please confirm, then edit the HTML
1. **EHL Finals result.** If you placed, add the rank. It would be the strongest line on the page.
2. **Ecosia year:** 2023 (old CV) or 2024 (repo dates)?
3. **Tsinghua exchange:** still "planned", or accepted? If accepted, say so.
4. **Phone:** a German +49 number would read better for Munich employers than +34.
5. **Photo (DE):** the passport cut-out works, but a proper headshot with a plain background and a collared shirt would be better.
6. **TUM grade average:** add it if it is ≤ 2.0. Otherwise leave it off.
7. hackaTUM team size: the portfolio says five, but GitHub shows four contributors.

## Next level (not CV content)
- Tailor each application: reorder Projects so the one closest to the role comes first, and mirror 3–4 keywords from the posting.
- Add a "CV (PDF)" link on szenessy.com and use the same headline on LinkedIn.
- Pin WorldFolder, RoadTax, MinoAI and ToMindMap on the GitHub profile. If the WorldFolder and RoadTax repos stay private, recruiters can only see the live sites.

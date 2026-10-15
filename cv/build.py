"""Generate the CV pages from one content source.

For each language this writes two pages:
  cv-<lang>.html      designed card layout (for email, fairs, people)
  cv-<lang>-ats.html  plain single-column layout (for application portals / ATS)

Edit CONTENT, then run ./render.sh (it calls this script first).
Item tuples are (title, link, when, short, long). The card layout shows `short`;
the ATS layout shows `long` when given (a list of bullet strings), else `short`.
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).parent

# (icon, text, href)
LINKS = [
    ("mail", "tom@szenessy.de", "mailto:tom@szenessy.de"),
    ("phone", "+34 693 015 063", None),
    ("web", "szenessy.com", "https://szenessy.com"),
    ("github", "TomSzenessy", "https://github.com/TomSzenessy"),
    ("linkedin", "tom-szenessy", "https://www.linkedin.com/in/tom-szenessy"),
]
# Full URLs for the ATS layout, where icons carry no meaning.
ATS_LINKS = [
    "tom@szenessy.de", "+34 693 015 063", "szenessy.com",
    "github.com/TomSzenessy", "linkedin.com/in/tom-szenessy",
]

# 24x24 stroke icons (Lucide-style shapes)
ICONS = {
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "web": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "github": '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.1-1.3-.3-2.5-1-3.5.3-1.2.3-2.4 0-3.5 0 0-1 0-3 1.5-2.6-.5-5.4-.5-8 0C6 2 5 2 5 2c-.3 1.1-.3 2.3 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.4.5-.7 1-.8 1.7-.2.6-.3 1.2-.2 1.8v4"/><path d="M9 18c-4.5 2-5-2-7-2"/>',
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    "cake": '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1M2 21h20M7 8v3M12 8v3M17 8v3"/>',
}

SKILLS = ["TypeScript", "Python", "Go", "Kotlin", "SQL", "React", "Docker", "Cloudflare", "LLM agents & RAG"]

CONTENT = {
    "en": {
        "title": "Tom Szenessy — CV",
        "more": {"proj": ("More projects at szenessy.com", "https://szenessy.com/en/#projects"),
                 "awards": ("All certificates at szenessy.com", "https://szenessy.com/en/#awards")},
        "role": "Business Informatics Student · TU Munich",
        "tech": "Technical",
        "location": "Munich, Germany",
        "extra_links": [],
        "stats": [
            ("1.0", "Abitur grade"),
            ("3+", "projects built and live"),
            ("2nd", "prize, Jugend forscht 2024"),
        ],
        "h": {"edu": "Education", "exp": "Experience", "proj": "Projects", "hack": "Hackathons",
              "skills": "Skills", "langs": "Languages", "awards": "Awards", "int": "Interests"},
        "edu": [
            ("B.Sc. Business Informatics", None, "Oct 2025 – 2028", "Technical University of Munich (TUM) · 3rd semester", None),
            ("Abitur · grade 1.0", None, "2025", "Deutsche Schule Málaga, Spain", None),
            ("Exchange year, California, USA", None, "2022 – 23", "Vista Murrieta High School · rank 24 of 829 in Grade 12 (top 3%)", None),
        ],
        "exp": [
            ("House Representative", None, "since Feb 2026",
             "Studentenstadt Munich · elected for 150+ residents, house events",
             ["Elected in February 2026 to represent the 150+ residents of my building.",
              "Organise community events and parties for the house."]),
            ("Software Development Intern", None, "2023",
             "Ecosia, Berlin · RAG chatbot (Python, LangChain, OpenAI, Milvus)",
             ["Built a retrieval-augmented support chatbot prototype in Python (LangChain, OpenAI API, Milvus vector database) that answers user questions from Ecosia’s FAQ pages with source links.",
              "Built a news widget that summarises articles with an LLM and flags clickbait headlines with a “polemic score”."]),
        ],
        "proj": [
            ("WorldFolder", ("worldfolder.com", "https://worldfolder.com"), "2026",
             "Go + Docker hosting · idle servers sleep at zero cost",
             ["On-demand Minecraft server hosting written in Go and Docker: idle servers shut down to zero compute cost and wake automatically when a player joins.",
              "Edge proxy, lifecycle state machine, crash guards, control API and Firecracker snapshots for fast wake-up."]),
            ("RoadTax", ("roadtax.app", "https://roadtax.app"), "2026",
             "Real-time multiplayer game · WebSockets on Cloudflare",
             ["Browser strategy game for 2–5 players with server-authoritative real-time multiplayer over WebSockets on Cloudflare Workers and Durable Objects.",
              "AI opponents driven by a policy network trained with a genetic algorithm in Python."]),
            ("ToMindMap", ("GitHub", "https://github.com/TomSzenessy/Mindmap-Plugin-for-Obsidian"), "2026",
             "Open-source mind-map plugin for Obsidian · JavaScript",
             ["Open-source mind-mapping plugin for Obsidian Canvas (JavaScript) with auto-layout, nested linked maps and touch controls on phones."]),
        ],
        "hack": [
            ("European Hackathon League Finals", None, "2026", "AI agent that negotiates prices on its own",
             ["Built an autonomous AI buyer agent (Python, LLM) that negotiated with supplier bots over five live rounds with no human in the loop."]),
            ("TUM.ai Makeathon · SideStroll", ("sidestroll.com", "https://sidestroll.com"), "2026",
             "Lead developer of an AI side-quest app · 500+ participants",
             ["Lead developer in a team of five (500+ participants) of SideStroll, an AI app that plans real-world outings from interests, free time and weather (TypeScript, Python, PostgreSQL)."]),
            ("hackaTUM · MunichPulse", None, "2025", "App to find people to go to events with · Kotlin",
             ["Team app (Kotlin Multiplatform) that matches people who want company for events."]),
        ],
        "langs": [("German", "Native"), ("English", "C2"), ("Spanish", "C1"), ("French", "A2"), ("Chinese", "A1")],
        "awards": [
            ("Jugend forscht", "2nd + CIB prize · 2024", "Jugend forscht Iberia 2024 — 2nd prize and CIB Special Prize"),
            ("Math Olympiad", "3rd prize · 2019", "Mathematics Olympiad — 3rd prize (2019)"),
            ("Informatik-Biber", "2nd prize · 2020, 2023", "Informatik-Biber — 2nd prize (2020, 2023)"),
        ],
        "int": ["Piano, since age 5", "Martial arts", "Padel", "Beach volleyball", "Drone filming"],
    },
    "de": {
        "title": "Tom Szenessy — Lebenslauf",
        "more": {"proj": ("Weitere Projekte auf szenessy.com", "https://szenessy.com/de/#projects"),
                 "awards": ("Alle Urkunden auf szenessy.com", "https://szenessy.com/de/#awards")},
        "role": "Student der Wirtschaftsinformatik · TU München",
        "tech": "Technisch",
        "location": "München · geb. 29.12.2005",
        "extra_links": [("cake", "29.12.2005", None)],
        "stats": [
            ("1,0", "Abiturnote"),
            ("3+", "eigene Projekte live"),
            ("2.", "Preis, Jugend forscht 2024"),
        ],
        "h": {"edu": "Ausbildung", "exp": "Praxiserfahrung", "proj": "Projekte", "hack": "Hackathons",
              "skills": "Kenntnisse", "langs": "Sprachen", "awards": "Auszeichnungen", "int": "Interessen"},
        "edu": [
            ("B.Sc. Wirtschaftsinformatik", None, "10/2025 – 2028", "Technische Universität München (TUM) · 3. Semester", None),
            ("Abitur · Note 1,0", None, "2025", "Deutsche Schule Málaga, Spanien", None),
            ("Austauschjahr, Kalifornien, USA", None, "2022 – 23", "Vista Murrieta High School · Rang 24 von 829 in Klasse 12 (Top 3 %)", None),
        ],
        "exp": [
            ("Haussprecher", None, "seit 02/2026",
             "Studentenstadt München · gewählt, 150+ Bewohner, Hausevents",
             ["Im Februar 2026 gewählt, um die 150+ Bewohner meines Hauses zu vertreten.",
              "Organisation von Veranstaltungen und Partys für das Haus."]),
            ("Praktikum Softwareentwicklung", None, "2023",
             "Ecosia, Berlin · RAG-Chatbot (Python, LangChain, OpenAI, Milvus)",
             ["RAG-Support-Chatbot-Prototyp in Python (LangChain, OpenAI API, Milvus-Vektordatenbank), der Nutzerfragen anhand der Ecosia-FAQ mit Quellenlinks beantwortet.",
              "News-Widget, das Artikel per LLM zusammenfasst und Clickbait-Titel mit einem „Polemik-Score“ markiert."]),
        ],
        "proj": [
            ("WorldFolder", ("worldfolder.com", "https://worldfolder.com"), "2026",
             "Go + Docker · Gameserver schlafen im Leerlauf kostenlos",
             ["Gameserver-Hosting in Go und Docker: Inaktive Minecraft-Server fahren auf null Rechenkosten herunter und starten automatisch, sobald ein Spieler beitritt.",
              "Edge-Proxy, Lifecycle-Zustandsautomat, Crash-Schutz, Control-API und Firecracker-Snapshots für schnelles Aufwachen."]),
            ("RoadTax", ("roadtax.app", "https://roadtax.app"), "2026",
             "Echtzeit-Multiplayer-Spiel · WebSockets auf Cloudflare",
             ["Browser-Strategiespiel für 2–5 Spieler mit serverautoritativem Echtzeit-Multiplayer über WebSockets auf Cloudflare Workers und Durable Objects.",
              "KI-Gegner mit einem per genetischem Algorithmus trainierten Policy-Netz (Python)."]),
            ("ToMindMap", ("GitHub", "https://github.com/TomSzenessy/Mindmap-Plugin-for-Obsidian"), "2026",
             "Open-Source-Mindmap-Plugin für Obsidian · JavaScript",
             ["Open-Source-Mindmap-Plugin für Obsidian Canvas (JavaScript) mit Auto-Layout, verschachtelten Maps und Touch-Steuerung."]),
        ],
        "hack": [
            ("European Hackathon League Finals", None, "2026", "KI-Agent, der selbstständig Preise verhandelt",
             ["Autonomer KI-Einkaufsagent (Python, LLM), der in fünf Live-Runden ohne menschliches Eingreifen mit Lieferanten-Bots verhandelte."]),
            ("TUM.ai Makeathon · SideStroll", ("sidestroll.com", "https://sidestroll.com"), "2026",
             "Lead-Entwickler einer KI-Sidequest-App · 500+ Teilnehmende",
             ["Lead-Entwickler im Fünferteam (500+ Teilnehmende) von SideStroll, einer KI-App, die aus Interessen, Freizeit und Wetter reale Ausflüge plant (TypeScript, Python, PostgreSQL)."]),
            ("hackaTUM · MunichPulse", None, "2025", "App, um Leute für gemeinsame Events zu finden · Kotlin",
             ["Team-App (Kotlin Multiplatform), die Menschen zusammenbringt, die Begleitung für Events suchen."]),
        ],
        "langs": [("Deutsch", "Muttersprache"), ("Englisch", "C2"), ("Spanisch", "C1"), ("Französisch", "A2"), ("Chinesisch", "A1")],
        "awards": [
            ("Jugend forscht", "2. + CIB-Preis · 2024", "Jugend forscht Iberia 2024 — 2. Preis und CIB-Sonderpreis"),
            ("Mathe-Olympiade", "3. Preis · 2019", "Mathematik-Olympiade — 3. Preis (2019)"),
            ("Informatik-Biber", "2. Preis · 2020, 2023", "Informatik-Biber — 2. Preis (2020, 2023)"),
        ],
        "int": ["Klavier, seit dem 5. Lebensjahr", "Kampfsport", "Padel", "Beachvolleyball", "Drohnenaufnahmen"],
    },
}


def e(s):
    return escape(s, quote=True)


def link(text, href):
    return f'<a href="{e(href)}">{e(text)}</a>' if href else e(text)


def more_link(c, key):
    """A plain-language link to the matching portfolio section, if one exists."""
    more = c["more"].get(key)
    return f'<a class="more" href="{e(more[1])}">{e(more[0])} ↗</a>' if more else ""


def items(rows):
    out = []
    for title, lk, when, desc, _long in rows:
        a = f' <a href="{e(lk[1])}">{e(lk[0])}</a>' if lk else ""
        out.append(f'<div class="item"><span class="t">{e(title)}{a}</span><span class="w">{e(when)}</span><span class="d">{e(desc)}</span></div>')
    return "\n      ".join(out)


def page(lang, c):
    links = "".join(
        f'<li><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg>{link(t, h)}</li>'
        for i, t, h in c["extra_links"] + LINKS
    )
    stats = "".join(f'<div class="card stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in c["stats"])
    skills = '<ul class="chips">' + "".join(f"<li>{e(s)}</li>" for s in SKILLS) + "</ul>"
    langs = "".join(f'<li><span>{e(n)}</span><span class="lvl">{e(l)}</span></li>' for n, l in c["langs"])
    awards = "\n      ".join(f'<div class="item"><span class="t">{e(t)}</span><span class="d">{e(d)}</span></div>' for t, d, _ in c["awards"])
    ints = "".join(f"<li>{e(i)}</li>" for i in c["int"])
    h = c["h"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{e(c["title"])}</title>
<meta name="author" content="Tom Szenessy">
<link rel="stylesheet" href="cv.css">
</head>
<body>
<div class="page">

  <header class="card head">
    <img class="photo" src="photo.png" alt="Tom Szenessy">
    <div class="id">
      <h1>Tom Szenessy</h1>
      <p class="role">{e(c["role"])}</p>
    </div>
    <ul class="links">{links}</ul>
  </header>

  <div class="stats">{stats}</div>

  <div class="cols">
    <div class="col main">
      <section class="card"><h2>{e(h["edu"])}</h2>
      {items(c["edu"])}
      </section>
      <section class="card"><h2>{e(h["exp"])}</h2>
      {items(c["exp"])}
      </section>
      <section class="card"><h2>{e(h["proj"])}</h2>
      {items(c["proj"])}
      {more_link(c, "proj")}
      </section>
      <section class="card grow"><h2>{e(h["hack"])}</h2>
      {items(c["hack"])}
      </section>
    </div>
    <div class="col side">
      <section class="card"><h2>{e(h["skills"])}</h2>{skills}</section>
      <section class="card"><h2>{e(h["langs"])}</h2><ul class="langs">{langs}</ul></section>
      <section class="card"><h2>{e(h["awards"])}</h2>
      {awards}
      {more_link(c, "awards")}
      </section>
      <section class="card grow"><h2>{e(h["int"])}</h2><ul class="chips">{ints}</ul></section>
    </div>
  </div>

</div>
</body>
</html>
"""


def ats_items(rows, org_in_desc=False):
    """One plain text line per entry (title, organisation, link, dates), then bullets.

    With org_in_desc, the part of the short text before " · " is the organisation
    (e.g. "Ecosia, Berlin") and moves into the title line.
    """
    out = []
    for title, lk, when, desc, long in rows:
        org = desc.split(" · ")[0] if org_in_desc else ""
        head = e(title) + (f", {e(org)}" if org else "")
        url = f" · {e(lk[1].removeprefix('https://'))}" if lk else ""
        bullets = "".join(f"<li>{e(b)}</li>" for b in (long or [desc]))
        out.append(f'<div class="item"><p class="row"><b>{head}</b>{url} | {e(when)}</p><ul>{bullets}</ul></div>')
    return "\n".join(out)


def ats_page(lang, c):
    """Single column, standard headings, real text only: safe for applicant tracking systems."""
    h = c["h"]
    contact = " · ".join([c["location"]] + ATS_LINKS)
    more = lambda k: f'<p class="more">{e(c["more"][k][0])}: {e(c["more"][k][1])}</p>'
    awards = "".join(f"<li>{e(full)}</li>" for _, _, full in c["awards"])
    langs = ", ".join(f"{n} ({l})" for n, l in c["langs"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{e(c["title"])}</title>
<meta name="author" content="Tom Szenessy">
<link rel="stylesheet" href="ats.css">
</head>
<body>
<h1>Tom Szenessy</h1>
<p class="role">{e(c["role"])}</p>
<p class="contact">{e(contact)}</p>

<h2>{e(h["edu"])}</h2>
{ats_items(c["edu"])}

<h2>{e(h["exp"])}</h2>
{ats_items(c["exp"], org_in_desc=True)}

<h2>{e(h["proj"])}</h2>
{ats_items(c["proj"])}
{more("proj")}

<h2>{e(h["hack"])}</h2>
{ats_items(c["hack"])}

<h2>{e(h["awards"])}</h2>
<ul>{awards}</ul>

<h2>{e(h["skills"])}</h2>
<p><b>{e(c["tech"])}:</b> {e(", ".join(SKILLS))}</p>
<p><b>{e(h["langs"])}:</b> {e(langs)}</p>
<p><b>{e(h["int"])}:</b> {e(", ".join(c["int"]))}</p>
</body>
</html>
"""


for lang, c in CONTENT.items():
    (HERE / f"cv-{lang}.html").write_text(page(lang, c), encoding="utf-8")
    (HERE / f"cv-{lang}-ats.html").write_text(ats_page(lang, c), encoding="utf-8")
    print(f"wrote cv-{lang}.html, cv-{lang}-ats.html")

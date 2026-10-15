"""Generate cv-en.html and cv-de.html from one content source.

Edit the CONTENT dict, then run ./render.sh (it calls this script first).
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

# 24x24 stroke icons (Lucide-style shapes)
ICONS = {
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "web": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "github": '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.1-1.3-.3-2.5-1-3.5.3-1.2.3-2.4 0-3.5 0 0-1 0-3 1.5-2.6-.5-5.4-.5-8 0C6 2 5 2 5 2c-.3 1.1-.3 2.3 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.4.5-.7 1-.8 1.7-.2.6-.3 1.2-.2 1.8v4"/><path d="M9 18c-4.5 2-5-2-7-2"/>',
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    "cake": '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1M2 21h20M7 8v3M12 8v3M17 8v3"/>',
}

SKILLS = {
    "code": ["TypeScript", "Python", "Go", "Kotlin", "SQL"],
    "stack": ["React", "Docker", "Cloudflare"],
    "ai": ["LLM agents & RAG"],
}

CONTENT = {
    "en": {
        "title": "Tom Szenessy — CV",
        "more": {"proj": ("More projects", "https://szenessy.com/en/#projects"),
                 "awards": ("Certificates", "https://szenessy.com/en/#awards")},
        "role": "Business Informatics Student · TU Munich",
        "extra_links": [],
        "stats": [
            ("1.0", "Abitur grade"),
            ("3+", "projects built and live"),
            ("2nd", "prize, Jugend forscht 2024"),
        ],
        "h": {"edu": "Education", "exp": "Experience", "proj": "Projects", "hack": "Hackathons",
              "skills": "Skills", "langs": "Languages", "awards": "Awards", "int": "Interests"},
        "edu": [
            ("B.Sc. Business Informatics", None, "Oct 2025 – 2028", "Technical University of Munich (TUM) · 3rd semester"),
            ("Abitur · grade 1.0", None, "2025", "Deutsche Schule Málaga, Spain"),
            ("Exchange year, California, USA", None, "2022 – 23", "Vista Murrieta High School · rank 24 of 829 in Grade 12 (top 3%)"),
        ],
        "exp": [
            ("House Representative", None, "since Feb 2026", "Studentenstadt Munich · represent the house, run events and parties"),
            ("Software Development Intern", None, "2023", "Ecosia, Berlin · built an AI chatbot that answers user questions"),
        ],
        "proj": [
            ("WorldFolder", ("worldfolder.com", "https://worldfolder.com"), "2026", "Game-server hosting that costs nothing while idle · Go"),
            ("RoadTax", ("roadtax.app", "https://roadtax.app"), "2026", "Online multiplayer strategy game with AI bots · JavaScript"),
            ("ToMindMap", ("GitHub", "https://github.com/TomSzenessy/Mindmap-Plugin-for-Obsidian"), "2026", "Open-source mind-map plugin for Obsidian · JavaScript"),
        ],
        "hack": [
            ("European Hackathon League Finals", None, "2026", "AI agent that negotiates prices on its own"),
            ("TUM.ai Makeathon · SideStroll", ("sidestroll.com", "https://sidestroll.com"), "2026", "Lead developer of an AI side-quest app · 500+ participants"),
            ("hackaTUM · MunichPulse", None, "2025", "App to find people to go to events with · Kotlin"),
        ],
        "langs": [("German", "Native", 5), ("English", "C2", 5), ("Spanish", "C1", 4), ("French", "A2", 2), ("Chinese", "A1", 1)],
        "awards": [
            ("Jugend forscht", "2nd + CIB prize · 2024"),
            ("Math Olympiad", "3rd prize · 2019"),
            ("Informatik-Biber", "2nd prize · 2020, 2023"),
        ],
        "int": ["Piano, since age 5", "Martial arts", "Padel", "Beach volleyball", "Drone filming"],
    },
    "de": {
        "title": "Tom Szenessy — Lebenslauf",
        "more": {"proj": ("Mehr Projekte", "https://szenessy.com/de/#projects"),
                 "awards": ("Urkunden", "https://szenessy.com/de/#awards")},
        "role": "Student der Wirtschaftsinformatik · TU München",
        "extra_links": [("cake", "29.12.2005", None)],
        "stats": [
            ("1,0", "Abiturnote"),
            ("3+", "eigene Projekte live"),
            ("2.", "Preis, Jugend forscht 2024"),
        ],
        "h": {"edu": "Ausbildung", "exp": "Praxiserfahrung", "proj": "Projekte", "hack": "Hackathons",
              "skills": "Kenntnisse", "langs": "Sprachen", "awards": "Auszeichnungen", "int": "Interessen"},
        "edu": [
            ("B.Sc. Wirtschaftsinformatik", None, "10/2025 – 2028", "Technische Universität München (TUM) · 3. Semester"),
            ("Abitur · Note 1,0", None, "2025", "Deutsche Schule Málaga, Spanien"),
            ("Austauschjahr, Kalifornien, USA", None, "2022 – 23", "Vista Murrieta High School · Rang 24 von 829 in Klasse 12 (Top 3 %)"),
        ],
        "exp": [
            ("Haussprecher", None, "seit 02/2026", "Studentenstadt München · Vertretung des Hauses, Events und Partys"),
            ("Praktikum Softwareentwicklung", None, "2023", "Ecosia, Berlin · KI-Chatbot für Nutzerfragen entwickelt"),
        ],
        "proj": [
            ("WorldFolder", ("worldfolder.com", "https://worldfolder.com"), "2026", "Gameserver-Hosting ohne Kosten im Leerlauf · Go"),
            ("RoadTax", ("roadtax.app", "https://roadtax.app"), "2026", "Online-Multiplayer-Strategiespiel mit KI-Bots · JavaScript"),
            ("ToMindMap", ("GitHub", "https://github.com/TomSzenessy/Mindmap-Plugin-for-Obsidian"), "2026", "Open-Source-Mindmap-Plugin für Obsidian · JavaScript"),
        ],
        "hack": [
            ("European Hackathon League Finals", None, "2026", "KI-Agent, der selbstständig Preise verhandelt"),
            ("TUM.ai Makeathon · SideStroll", ("sidestroll.com", "https://sidestroll.com"), "2026", "Lead-Entwickler einer KI-Sidequest-App · 500+ Teilnehmende"),
            ("hackaTUM · MunichPulse", None, "2025", "App, um Leute für gemeinsame Events zu finden · Kotlin"),
        ],
        "langs": [("Deutsch", "Muttersprache", 5), ("Englisch", "C2", 5), ("Spanisch", "C1", 4), ("Französisch", "A2", 2), ("Chinesisch", "A1", 1)],
        "awards": [
            ("Jugend forscht", "2. + CIB-Preis · 2024"),
            ("Mathe-Olympiade", "3. Preis · 2019"),
            ("Informatik-Biber", "2. Preis · 2020, 2023"),
        ],
        "int": ["Klavier, seit dem 5. Lebensjahr", "Kampfsport", "Padel", "Beachvolleyball", "Drohnenaufnahmen"],
    },
}


def e(s):
    return escape(s, quote=True)


def link(text, href):
    return f'<a href="{e(href)}">{e(text)}</a>' if href else e(text)


def heading(c, key):
    """Section title, plus a small link to the portfolio section if one exists."""
    more = c["more"].get(key)
    link_html = f'<a class="more" href="{e(more[1])}">{e(more[0])} ↗</a>' if more else ""
    return f'<h2>{e(c["h"][key])}{link_html}</h2>'


def items(rows):
    out = []
    for title, lk, when, desc in rows:
        a = f' <a href="{e(lk[1])}">{e(lk[0])}</a>' if lk else ""
        out.append(f'<div class="item"><span class="t">{e(title)}{a}</span><span class="w">{e(when)}</span><span class="d">{e(desc)}</span></div>')
    return "\n      ".join(out)


def page(lang, c):
    links = "".join(
        f'<li><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg>{link(t, h)}</li>'
        for i, t, h in c["extra_links"] + LINKS
    )
    stats = "".join(f'<div class="card stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in c["stats"])
    skills = '<ul class="chips">' + "".join(f"<li>{e(s)}</li>" for v in SKILLS.values() for s in v) + "</ul>"
    langs = "".join(
        f'<li><span>{e(n)} <span class="lvl">{e(l)}</span></span><span class="dots">'
        + "".join('<i class="on"></i>' if i < d else "<i></i>" for i in range(5)) + "</span></li>"
        for n, l, d in c["langs"]
    )
    awards = "\n      ".join(f'<div class="item"><span class="t">{e(t)}</span><span class="d">{e(d)}</span></div>' for t, d in c["awards"])
    ints = "".join(f"<li>{e(i)}</li>" for i in c["int"])  # rendered as chips
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
      <section class="card">{heading(c, "edu")}
      {items(c["edu"])}
      </section>
      <section class="card">{heading(c, "exp")}
      {items(c["exp"])}
      </section>
      <section class="card">{heading(c, "proj")}
      {items(c["proj"])}
      </section>
      <section class="card grow">{heading(c, "hack")}
      {items(c["hack"])}
      </section>
    </div>
    <div class="col side">
      <section class="card">{heading(c, "skills")}{skills}</section>
      <section class="card">{heading(c, "langs")}<ul class="langs">{langs}</ul></section>
      <section class="card">{heading(c, "awards")}
      {awards}
      </section>
      <section class="card grow">{heading(c, "int")}<ul class="chips">{ints}</ul></section>
    </div>
  </div>

</div>
</body>
</html>
"""


for lang, c in CONTENT.items():
    (HERE / f"cv-{lang}.html").write_text(page(lang, c), encoding="utf-8")
    print(f"wrote cv-{lang}.html")

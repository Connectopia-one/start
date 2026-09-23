"""
Zet kalender.md om in kalender.html, klaar om als pdf te printen.

  python3 naar-html.py

kalender.md is de export van het Claude-document "Social media kalender,
30 dagen". Is het document veranderd? Exporteer het opnieuw als markdown,
zet het hier neer en draai dit script en daarna render.js.
"""
import html
import pathlib
import re

BRON = pathlib.Path(__file__).parent
md = (BRON / "kalender.md").read_text()

# het document schrijft datums en de naam van de auteur in het Engels
md = md.replace("Sep 23, 2026 · @Someone", "23 september 2026 · Connectopia vzw")
md = md.replace("van Sep 23, 2026 tot Oct 22, 2026", "van 23 september tot 22 oktober 2026")
md = md.replace("## Wat ik nog van jou nodig heb", "## Wat er nog moet komen")
# die alinea is aan Kim gericht; in de pdf leest ze gek, want de pdf gaat net naar
# de begeleidster toe
md = md.replace(
    "De kalender is af en kan zo naar je begeleidster. Deze zeven dingen maken hem compleet. "
    "Vink af wat klaar is, dan zie je meteen wat er nog rest.",
    "Dit is wat er nog bij moet. Wat aangevinkt staat, is klaar.",
)


def inline(t: str) -> str:
    t = html.escape(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t


def cellen(regel: str):
    return [c.strip() for c in regel.strip().strip("|").split("|")]


uit = []
regels = md.splitlines()
i = 0
eerste_h2 = True

while i < len(regels):
    r = regels[i]

    if not r.strip():
        i += 1
        continue

    if r.startswith("### "):
        uit.append(f"<h3>{inline(r[4:])}</h3>")
        i += 1
        continue

    if r.startswith("## "):
        klasse = "eerste" if eerste_h2 else ""
        eerste_h2 = False
        uit.append(f'<h2 class="{klasse}">{inline(r[3:])}</h2>')
        i += 1
        continue

    if r.startswith("# "):
        uit.append(f"<h1>{inline(r[2:])}</h1>")
        i += 1
        continue

    # een tabel
    if r.startswith("|"):
        kop = cellen(r)
        i += 2  # de kop en de streepjesregel
        rijen = []
        while i < len(regels) and regels[i].startswith("|"):
            rijen.append(cellen(regels[i]))
            i += 1
        uit.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in kop) + "</tr></thead><tbody>")
        for rij in rijen:
            uit.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in rij) + "</tr>")
        uit.append("</tbody></table>")
        continue

    # een citaat: de tekst van de post zelf
    if r.startswith(">"):
        alineas = []
        lopend = []
        while i < len(regels) and regels[i].startswith(">"):
            tekst = regels[i][1:].strip()
            if tekst:
                lopend.append(tekst)
            else:
                if lopend:
                    alineas.append(" ".join(lopend))
                    lopend = []
            i += 1
        if lopend:
            alineas.append(" ".join(lopend))
        uit.append('<blockquote>' + "".join(f"<p>{inline(a)}</p>" for a in alineas) + "</blockquote>")
        continue

    # een lijst, met of zonder vakjes om aan te vinken
    if re.match(r"^[-*] ", r):
        items = []
        vakjes = False
        while i < len(regels) and re.match(r"^[-*] ", regels[i]):
            tekst = regels[i][2:]
            vakje = ""
            if tekst.startswith("[ ] "):
                vakje, tekst, vakjes = "☐ ", tekst[4:], True
            elif tekst.lower().startswith("[x] "):
                vakje, tekst, vakjes = "☑ ", tekst[4:], True
            items.append(f"<li>{vakje}{inline(tekst)}</li>")
            i += 1
        soort = ' class="vakjes"' if vakjes else ""
        uit.append("<ul" + soort + ">" + "".join(items) + "</ul>")
        continue

    # een gewone alinea; de regels die het beeld aankondigen krijgen hun eigen stijl
    klasse = ' class="beeld"' if r.startswith(("Foto:", "Beeld:")) else ""
    uit.append(f"<p{klasse}>{inline(r)}</p>")
    i += 1

(BRON / "kalender.html").write_text(
    (BRON / "sjabloon.html").read_text().replace("<!--INHOUD-->", "\n".join(uit))
)
print("kalender.html geschreven,", len(uit), "blokken")

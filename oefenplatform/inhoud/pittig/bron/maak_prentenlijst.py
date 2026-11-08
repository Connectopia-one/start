"""Maakt de lijst van afbeeldingen die Kim moet zoeken, per pittig hoofdstuk.

Gebruik (uit oefenplatform/inhoud/pittig/bron): python3 maak_prentenlijst.py <uitvoer.html>
Enkel echte bronnen (zelf=False) komen op de lijst; tijdlijnen en kaarten tekent Claude.
"""
import html, importlib, re, sys
from pathlib import Path

HIER = Path(__file__).parent
sys.path.insert(0, str(HIER))
bron = (HIER / "beyond_geschiedenis.py").read_text()
THEMAS = re.findall(r'\("(\w+)", "([^"]+)"\),', bron.split("THEMAS = [", 1)[1].split("]", 1)[0])

rijen, nr = [], 0
for mod, titel in THEMAS:
    m = importlib.import_module("beyond_geschiedenis_themas." + mod)
    zoeken = [p for p in m.PRENTEN if not p["zelf"]]
    rijen.append(f'<h2>{html.escape(titel)} — pittig</h2>')
    if not zoeken:
        rijen.append('<p class="leeg">Niets te zoeken: de prenten van dit hoofdstuk teken ik zelf.</p>')
        continue
    for p in zoeken:
        nr += 1
        rijen.append(f'''<div class="kaart"><label><input type="checkbox"> <b>{nr}. {html.escape(p["bestand"])}</b></label>
<p><b>Wat:</b> {html.escape(p["wat"])}</p>
<p><b>Waar zoeken:</b> {html.escape(p.get("waar", ""))}</p>
<p><b>Voor:</b> {html.escape(p["vragen"])}</p></div>''')

pagina = f'''<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Afbeeldingen pittig geschiedenis Beyond</title><style>
body{{font-family:Nunito,system-ui,sans-serif;background:#fbf6ea;color:#2f4a22;max-width:760px;margin:0 auto;padding:24px;font-size:17px;line-height:1.65}}
h1{{font-size:26px}} h2{{font-size:20px;margin-top:32px}}
.kaart{{background:#fff;border:1px solid #d9cfb4;border-radius:20px;padding:14px 18px;margin:12px 0}}
.kaart p{{margin:6px 0}} .leeg{{color:#6b7a5e;font-style:italic}}
.uitleg{{background:#fff;border-radius:20px;padding:14px 18px;border:2px solid #2f4a22}}
</style></head><body>
<h1>Afbeeldingen voor pittig geschiedenis Beyond</h1>
<div class="uitleg"><p>Dit zijn enkel de echte bronnen (foto's, affiches, schilderijen, spotprenten). Tijdlijnen, kaarten en grafieken teken ik zelf.</p>
<p>Bewaar elke afbeelding onder de vetgedrukte naam (een jpg of png mag ook, ik zet ze zelf om) en stuur ze in de thread. Liefst rechtenvrij, zoals op Wikimedia Commons. Vink af wat je hebt.</p>
<p>Totaal tot nu toe: {nr} afbeeldingen voor {len(THEMAS)} hoofdstukken. De lijst groeit mee met de volgende hoofdstukken.</p></div>
{"".join(rijen)}
</body></html>'''
Path(sys.argv[1]).write_text(pagina)
print(nr, "afbeeldingen,", len(THEMAS), "hoofdstukken")

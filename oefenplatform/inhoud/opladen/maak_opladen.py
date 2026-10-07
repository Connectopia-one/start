# -*- coding: utf-8 -*-
"""Bouwt de opladpagina voor Kim.

Twee regels die Kim zelf gaf en die deze pagina vormgeven:

1. Op de pagina staat **enkel wat nieuw is**. Alles wat ze eerder al kreeg,
   heeft ze meteen gedraaid, dus het hoort hier niet opnieuw bij te staan.
2. Een vragenbestand krijgt een **kopieerknop**, geen link die een bladzijde
   opent. Alleen een zip blijft een download, want die kan je niet plakken.
"""
import html, json, pathlib, zipfile

WORTEL = pathlib.Path("/home/claude/start/oefenplatform/inhoud")
TAK = "claude/drie-projecten-planning-87h9wg"
RAW = f"https://raw.githubusercontent.com/Connectopia-one/start/{TAK}/oefenplatform/inhoud/leerbundels/"

# De zips met leerbundels die er deze ronde bij gekomen zijn.
# (afvinksleutel, naam, categorie, zipnaam)
BUNDELS = [
    ("b-tec", "Toegepaste economie", "🚀 Boost dubbele finaliteit",
     "toegepaste-economie-boost-dubbele-finaliteit"),
    ("b-ebw", "Economie en bedrijfswetenschappen", "🚀 Boost dubbele finaliteit",
     "economie-en-bedrijfswetenschappen-boost-dubbele-finaliteit"),
    ("b-gzw", "Gezondheid, zorg en welzijn", "🚀 Boost dubbele finaliteit",
     "gezondheid-zorg-en-welzijn-boost-dubbele-finaliteit"),
    ("b-oph", "Ontwikkeling en pedagogisch handelen", "🚀 Boost dubbele finaliteit",
     "ontwikkeling-en-pedagogisch-handelen-boost-dubbele-finaliteit"),
]

# Vragenbestanden die opnieuw ingeladen moeten worden, met de reden erbij.
# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom)
VRAGEN = [
    ("v-oph", "Ontwikkeling en pedagogisch handelen", "🚀 Boost dubbele finaliteit",
     "boost-dubbele-finaliteit", "ontwikkeling-en-pedagogisch-handelen",
     "In de vragen over Kohlberg stond acht keer het woord belonging in plaats van "
     "beloning. Dat is rechtgezet, dus dit bestand mag er nog eens over."),
]


def tel_vragen(pad):
    g = json.loads(pad.read_text(encoding="utf-8"))
    h = g["hoofdstukken"]
    return len(h), sum(len(x["vragen"]) for x in h)


def tel_pdfs(pad):
    with zipfile.ZipFile(pad) as z:
        return len([n for n in z.namelist() if n.lower().endswith(".pdf")])


bundelrijen = []
for sleutel, naam, cat, zipnaam in BUNDELS:
    zippad = WORTEL / "leerbundels" / f"{zipnaam}.zip"
    pdfs = tel_pdfs(zippad)
    mb = round(zippad.stat().st_size / 1024 / 1024, 1)
    bundelrijen.append(f'''
      <article class="vak" data-sleutel="{sleutel}">
        <label class="afvink"><input type="checkbox" class="vinkje"><span>opgeladen</span></label>
        <header class="vakkop">
          <div class="vaknaam">
            <h3>{html.escape(naam)}</h3>
            <p class="cat">{cat}</p>
          </div>
        </header>
        <div class="knoppen">
          <a class="zip" href="{RAW}{zipnaam}.zip">
            Download de {pdfs} leerbundels <span class="mee">zip van {mb} MB</span>
          </a>
        </div>
      </article>''')

vraagrijen = []
for sleutel, naam, cat, map_, bestand, waarom in VRAGEN:
    jsonpad = WORTEL / map_ / f"{bestand}.json"
    tekst = jsonpad.read_text(encoding="utf-8")
    assert "</script" not in tekst.lower(), bestand
    hoofdstukken, vragen = tel_vragen(jsonpad)
    kb = round(len(tekst.encode("utf-8")) / 1024)
    vraagrijen.append(f'''
      <article class="vak" data-sleutel="{sleutel}">
        <label class="afvink"><input type="checkbox" class="vinkje"><span>ingeladen</span></label>
        <header class="vakkop">
          <div class="vaknaam">
            <h3>{html.escape(naam)}</h3>
            <p class="cat">{cat}</p>
          </div>
          <span class="etiket">zet vervangen aan</span>
        </header>
        <p class="raad">{html.escape(waarom)}</p>
        <div class="knoppen">
          <button class="kopieer" type="button" data-bron="j-{sleutel}">
            Kopieer de {vragen} vragen <span class="mee">{kb} KB tekst</span>
          </button>
        </div>
        <p class="gelukt" hidden>Gekopieerd. Plak het nu in het vak Vragen importeren.</p>
        <p class="handmatig" hidden>Het kopiëren lukte niet vanzelf. De tekst staat hieronder
          klaar: tik erin, selecteer alles en kopieer.</p>
        <textarea class="bak" readonly hidden aria-label="de vragen van {html.escape(naam)}"></textarea>
        <script type="text/plain" id="j-{sleutel}">{tekst}</script>
      </article>''')

HIER = pathlib.Path(__file__).parent
SJABLOON = (HIER / "sjabloon.html").read_text(encoding="utf-8")
PAGINA = HIER / "opladen.html"
PAGINA.write_text(SJABLOON
                  .replace("<!--BUNDELS-->", "".join(bundelrijen))
                  .replace("<!--VRAGEN-->", "".join(vraagrijen))
                  .replace("<!--AANTAL-->", str(len(bundelrijen) + len(vraagrijen))),
                  encoding="utf-8")
print(f"{PAGINA} — {PAGINA.stat().st_size / 1024 / 1024:.2f} MB, "
      f"{len(bundelrijen)} zips en {len(vraagrijen)} vragenbestanden")

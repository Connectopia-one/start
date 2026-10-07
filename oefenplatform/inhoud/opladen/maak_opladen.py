# -*- coding: utf-8 -*-
"""Bouwt de opladpagina voor Kim: per vak één kopieerknop met de vragen erin
en één downloadknop voor de zip met leerbundels.

De vragen staan in de pagina zelf, in een <script type="text/plain">, zodat
één klik ze op het klembord zet. Kim hoeft dus geen bladzijde meer te openen.
"""
import html, json, pathlib

WORTEL = pathlib.Path("/home/claude/start/oefenplatform/inhoud")
TAK = "claude/drie-projecten-planning-87h9wg"
RAW = f"https://raw.githubusercontent.com/Connectopia-one/start/{TAK}/oefenplatform/inhoud/leerbundels/"

# (afvinksleutel, naam, categorie, etiket, map, bestandsnaam, zipnaam, toelichting)
VAKKEN = [
    ("v-sgw", "Sociale en gedragswetenschappen", "🚀 Boost doorstroom", "nieuw vak",
     "boost-doorstroom", "sociale-en-gedragswetenschappen",
     "sociale-en-gedragswetenschappen-boost-doorstroom",
     "Dit vak bestaat nog niet in Beheer, dus maak het eerst aan."),
    ("v-kuf", "Kunstbeschouwing en filosofie", "🚀 Boost doorstroom", "nieuw vak",
     "boost-doorstroom", "kunstbeschouwing-en-filosofie",
     "kunstbeschouwing-en-filosofie-boost-doorstroom",
     "Dit vak bestaat nog niet in Beheer, dus maak het eerst aan."),
    ("v-wbas", "Wiskunde basis", "🚀 Boost doorstroom", "nieuw vak",
     "boost-doorstroom", "wiskunde-basis", "wiskunde-basis-boost-doorstroom",
     "Niet te verwarren met Wiskunde: dat is de gevorderde. Maak dit vak eerst aan."),
    ("v-ak", "Aardrijkskunde", "🚀 Boost doorstroom", "kijk eerst na",
     "boost-doorstroom", "aardrijkskunde", "aardrijkskunde-boost-doorstroom",
     "Stond bij de vakken zonder hoofdstukken. Staat het er intussen wel, sla het dan over."),
    ("v-bio", "Biologie", "🚀 Boost doorstroom", "kijk eerst na",
     "boost-doorstroom", "biologie", "biologie-boost-doorstroom",
     "Stond bij de vakken zonder hoofdstukken. Staat het er intussen wel, sla het dan over."),
    ("v-che", "Chemie", "🚀 Boost doorstroom", "kijk eerst na",
     "boost-doorstroom", "chemie", "chemie-boost-doorstroom",
     "Stond bij de vakken zonder hoofdstukken. Staat het er intussen wel, sla het dan over."),
    ("v-fys", "Fysica", "🚀 Boost doorstroom", "kijk eerst na",
     "boost-doorstroom", "fysica", "fysica-boost-doorstroom",
     "Stond bij de vakken zonder hoofdstukken. Staat het er intussen wel, sla het dan over."),
    ("df-tec", "Toegepaste economie", "🚀 Boost dubbele finaliteit", "nieuw vak",
     "boost-dubbele-finaliteit", "toegepaste-economie",
     "toegepaste-economie-boost-dubbele-finaliteit",
     "Acht hoofdstukken boekhouden en acht ICT. Maak dit vak eerst aan."),
    ("df-ebw", "Economie en bedrijfswetenschappen", "🚀 Boost dubbele finaliteit", "nieuw vak",
     "boost-dubbele-finaliteit", "economie-en-bedrijfswetenschappen",
     "economie-en-bedrijfswetenschappen-boost-dubbele-finaliteit",
     "Maak dit vak eerst aan."),
    ("df-gzw", "Gezondheid, zorg en welzijn", "🚀 Boost dubbele finaliteit", "nieuw vak",
     "boost-dubbele-finaliteit", "gezondheid-zorg-en-welzijn",
     "gezondheid-zorg-en-welzijn-boost-dubbele-finaliteit",
     "Maak dit vak eerst aan."),
    ("df-oph", "Ontwikkeling en pedagogisch handelen", "🚀 Boost dubbele finaliteit", "nieuw vak",
     "boost-dubbele-finaliteit", "ontwikkeling-en-pedagogisch-handelen",
     "ontwikkeling-en-pedagogisch-handelen-boost-dubbele-finaliteit",
     "Maak dit vak eerst aan."),
]


def tel(pad):
    """Hoeveel hoofdstukken en vragen staan er echt in het bestand?"""
    g = json.loads(pad.read_text(encoding="utf-8"))
    h = g["hoofdstukken"]
    return len(h), sum(len(x["vragen"]) for x in h)


def telzip(pad):
    import zipfile
    with zipfile.ZipFile(pad) as z:
        return len([n for n in z.namelist() if n.lower().endswith(".pdf")])


rijen = []
for sleutel, naam, cat, etiket, map_, bestand, zipnaam, toelichting in VAKKEN:
    jsonpad = WORTEL / map_ / f"{bestand}.json"
    zippad = WORTEL / "leerbundels" / f"{zipnaam}.zip"
    tekst = jsonpad.read_text(encoding="utf-8")
    assert "</script" not in tekst.lower(), bestand
    hoofdstukken, vragen = tel(jsonpad)
    pdfs = telzip(zippad)
    kb = round(len(tekst.encode("utf-8")) / 1024)
    mb = round(zippad.stat().st_size / 1024 / 1024, 1)
    klasse = {"nieuw vak": "e-nieuw", "kijk eerst na": "e-kijk"}[etiket]
    rijen.append(f'''
    <article class="vak" data-sleutel="{sleutel}">
      <label class="afvink"><input type="checkbox" class="vinkje"><span>gedaan</span></label>
      <header class="vakkop">
        <div class="vaknaam">
          <h3>{html.escape(naam)}</h3>
          <p class="cat">{cat}</p>
        </div>
        <span class="etiket {klasse}">{etiket}</span>
      </header>
      <p class="raad">{html.escape(toelichting)}</p>
      <dl class="cijfers">
        <div><dt>hoofdstukken</dt><dd>{hoofdstukken}</dd></div>
        <div><dt>vragen</dt><dd>{vragen}</dd></div>
        <div><dt>leerbundels</dt><dd>{pdfs}</dd></div>
      </dl>
      <div class="knoppen">
        <button class="kopieer" type="button" data-bron="j-{sleutel}">
          Kopieer de {vragen} vragen <span class="mee">{kb} KB tekst</span>
        </button>
        <a class="zip" href="{RAW}{zipnaam}.zip">
          Download de {pdfs} leerbundels <span class="mee">zip van {mb} MB</span>
        </a>
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
PAGINA.write_text(SJABLOON.replace("<!--RIJEN-->", "".join(rijen)), encoding="utf-8")
print(f"{PAGINA} — {PAGINA.stat().st_size / 1024 / 1024:.2f} MB, {len(rijen)} vakken")

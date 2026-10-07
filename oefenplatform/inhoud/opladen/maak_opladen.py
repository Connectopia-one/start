# -*- coding: utf-8 -*-
"""Bouwt de plakpagina voor Kim.

Drie regels die Kim zelf gaf en die deze pagina vormgeven:

1. Op de pagina staat **enkel wat nieuw is**. Alles wat ze eerder al kreeg,
   heeft ze meteen gedraaid, dus het hoort hier niet opnieuw bij te staan. Een
   uitzondering: een import die met "vervangen" aan gaat, kan geen kwaad als ze
   hem twee keer doet, en dan mag hij blijven staan tot ze hem afvinkt.
2. Een vragenbestand krijgt een **kopieerknop**, geen link die een bladzijde
   opent. Alleen een zip blijft een download, want die kan je niet plakken.
3. Eén pagina, niet drie. Kim vroeg op 7 oktober 2026 uitdrukkelijk om alles
   van de nieuwe vakken op één plakpagina.
"""
import html, json, pathlib, zipfile

WORTEL = pathlib.Path("/home/claude/start/oefenplatform/inhoud")
TAK = "claude/drie-projecten-planning-87h9wg"
BASIS = f"https://raw.githubusercontent.com/Connectopia-one/start/{TAK}/oefenplatform/inhoud/"

DOOR = "🚀 Boost doorstroom"
DF = "🚀 Boost dubbele finaliteit"

# Vragenbestanden die ingeladen moeten worden, met de reden erbij.
# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom)
VRAGEN = [
    ("v-fr", "Frans", DOOR, "boost-doorstroom", "frans",
     "Bij de trappen van vergelijking stond plus meilleur als juist antwoord, en dat "
     "bestaat niet in het Frans: het is meilleur. Dat is rechtgezet, dus dit bestand mag "
     "er nog eens over."),
    ("v-oph", "Ontwikkeling en pedagogisch handelen", DF,
     "boost-dubbele-finaliteit", "ontwikkeling-en-pedagogisch-handelen",
     "In de vragen over Kohlberg stond acht keer het woord belonging in plaats van "
     "beloning. Dat is rechtgezet, dus dit bestand mag er nog eens over."),
]

# De zips met leerbundels van de acht nieuwe vakken.
# (afvinksleutel, naam, categorie, zipnaam)
BUNDELS = [
    ("b-fr", "Frans", DOOR, "frans-boost-doorstroom"),
    ("b-sgw", "Sociale en gedragswetenschappen", DOOR,
     "sociale-en-gedragswetenschappen-boost-doorstroom"),
    ("b-kbf", "Kunstbeschouwing en filosofie", DOOR,
     "kunstbeschouwing-en-filosofie-boost-doorstroom"),
    ("b-wib", "Wiskunde basis", DOOR, "wiskunde-basis-boost-doorstroom"),
    ("b-tec", "Toegepaste economie", DF, "toegepaste-economie-boost-dubbele-finaliteit"),
    ("b-ebw", "Economie en bedrijfswetenschappen", DF,
     "economie-en-bedrijfswetenschappen-boost-dubbele-finaliteit"),
    ("b-gzw", "Gezondheid, zorg en welzijn", DF,
     "gezondheid-zorg-en-welzijn-boost-dubbele-finaliteit"),
    ("b-oph", "Ontwikkeling en pedagogisch handelen", DF,
     "ontwikkeling-en-pedagogisch-handelen-boost-dubbele-finaliteit"),
]

# De zips met oefenbundels van dezelfde acht vakken. Zelfde namen, andere map.
OEFENBUNDELS = [("o" + s[1:], naam, cat, zipnaam) for s, naam, cat, zipnaam in BUNDELS]


def tel_vragen(pad):
    g = json.loads(pad.read_text(encoding="utf-8"))
    h = g["hoofdstukken"]
    return len(h), sum(len(x["vragen"]) for x in h)


def tel_pdfs(pad):
    with zipfile.ZipFile(pad) as z:
        return len([n for n in z.namelist() if n.lower().endswith(".pdf")])


def zipkaarten(lijst, map_, wat):
    rijen = []
    for sleutel, naam, cat, zipnaam in lijst:
        zippad = WORTEL / map_ / f"{zipnaam}.zip"
        pdfs = tel_pdfs(zippad)
        mb = round(zippad.stat().st_size / 1024 / 1024, 1)
        rijen.append(f'''
      <article class="vak" data-sleutel="{sleutel}">
        <label class="afvink"><input type="checkbox" class="vinkje"><span>opgeladen</span></label>
        <header class="vakkop">
          <div class="vaknaam">
            <h3>{html.escape(naam)}</h3>
            <p class="cat">{cat}</p>
          </div>
        </header>
        <div class="knoppen">
          <a class="zip" href="{BASIS}{map_}/{zipnaam}.zip">
            Download de {pdfs} {wat} <span class="mee">zip van {mb} MB</span>
          </a>
        </div>
      </article>''')
    return rijen


bundelrijen = zipkaarten(BUNDELS, "leerbundels", "leerbundels")
oefenrijen = zipkaarten(OEFENBUNDELS, "oefenbundels", "oefenbundels")

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
aantal = len(bundelrijen) + len(oefenrijen) + len(vraagrijen)
PAGINA.write_text(SJABLOON
                  .replace("<!--VRAGEN-->", "".join(vraagrijen))
                  .replace("<!--BUNDELS-->", "".join(bundelrijen))
                  .replace("<!--OEFENBUNDELS-->", "".join(oefenrijen))
                  .replace("<!--AANTAL-->", str(aantal)),
                  encoding="utf-8")
print(f"{PAGINA} — {PAGINA.stat().st_size / 1024 / 1024:.2f} MB, "
      f"{len(vraagrijen)} vragenbestanden, {len(bundelrijen)} leerbundelzips, "
      f"{len(oefenrijen)} oefenbundelzips")

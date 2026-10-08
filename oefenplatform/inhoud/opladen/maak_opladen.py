# -*- coding: utf-8 -*-
"""Bouwt de plakpagina voor Kim.

Vier regels die Kim zelf gaf en die deze pagina vormgeven:

1. Op de pagina staat **enkel wat nieuw is**. Alles wat ze eerder al kreeg,
   heeft ze meteen gedraaid of opgeladen, dus het hoort hier niet opnieuw bij
   te staan. Controleer dat met `git log -1 -- <bestand>`: wijst dat naar een
   commit van een vorige ronde, dan hoort het bestand er niet meer bij. Een
   uitzondering: een import die met "vervangen" aan gaat, kan geen kwaad als
   ze hem twee keer doet.
2. Een vragenbestand krijgt een **kopieerknop**, geen link die een bladzijde
   opent. Alleen een zip blijft een download, want die kan je niet plakken.
3. Eén pagina, niet drie. Kim vroeg op 7 oktober 2026 uitdrukkelijk om alles
   van een ronde op één plakpagina.
4. Zeg bij een download wat er na het klikken gebeurt.

Alles van één ronde staat in de drie blokken onderaan: `VAKKEN`, `VRAGEN` en
`SECTIES`. De rest van het bestand hoeft niet mee te veranderen, en het
sjabloon al helemaal niet: kop, secties, voettekst en de sleutel waarin de
vinkjes bewaard worden, komen alle vier uit dit bestand.
"""
import html, json, pathlib, zipfile

WORTEL = pathlib.Path("/home/claude/start/oefenplatform/inhoud")
TAK = "claude/drie-projecten-planning-87h9wg"
BASIS = f"https://raw.githubusercontent.com/Connectopia-one/start/{TAK}/oefenplatform/inhoud/"


def tel_vragen(pad):
    g = json.loads(pad.read_text(encoding="utf-8"))
    h = g["hoofdstukken"]
    return len(h), sum(len(x["vragen"]) for x in h)


def tel_pdfs(pad):
    with zipfile.ZipFile(pad) as z:
        return len([n for n in z.namelist() if n.lower().endswith(".pdf")])


def zipkaarten(lijst, map_, wat, voor=""):
    """Een kaart per zip, met het aantal pdf's en de grootte erbij."""
    rijen = []
    for sleutel, naam, cat, zipnaam in lijst:
        zippad = WORTEL / map_ / f"{zipnaam}.zip"
        pdfs = tel_pdfs(zippad)
        mb = round(zippad.stat().st_size / 1024 / 1024, 1)
        rijen.append(f'''
      <article class="vak" data-sleutel="{voor}{sleutel}">
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


def vraagkaarten(lijst):
    """Een kaart per vragenbestand, met de hele json in een kopieerknop."""
    rijen = []
    for sleutel, naam, cat, map_, bestand, waarom in lijst:
        jsonpad = WORTEL / map_ / f"{bestand}.json"
        tekst = jsonpad.read_text(encoding="utf-8")
        assert "</script" not in tekst.lower(), bestand
        hoofdstukken, vragen = tel_vragen(jsonpad)
        kb = round(len(tekst.encode("utf-8")) / 1024)
        rijen.append(f'''
      <article class="vak" data-sleutel="v-{sleutel}">
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
    return rijen


# ════════════════════════════════════════════════════════════
# Vanaf hier staat alles van déze ronde. Enkel dit wijzigt.
# ════════════════════════════════════════════════════════════

TITEL = "Plakpagina Beyond"
SLEUTEL = "connectopia-plakpagina-beyond-8-oktober"
VOET = "Bijgewerkt op 8 oktober 2026"
INTRO = """<p>De zes vakken van 🌍 Beyond die nog geen bundels hadden, hebben ze nu. Dit is
      allemaal nieuw: niets van deze pagina heb je eerder gekregen. Er is geen SQL en geen
      vragenbestand bij, enkel documenten om op te laden.</p>"""

BEYOND = "🌍 Beyond"
BEYOND_DF = "🌍 Beyond dubbele finaliteit"

# (afvinksleutel, naam, categorie, zipnaam)
VAKKEN = [
    ("ak", "Aardrijkskunde", BEYOND, "aardrijkskunde-beyond"),
    ("en", "Engels", BEYOND, "engels-beyond"),
    ("fr", "Frans", BEYOND, "frans-beyond"),
    ("akd", "Aardrijkskunde", BEYOND_DF, "aardrijkskunde-beyond-dubbele-finaliteit"),
    ("end", "Engels", BEYOND_DF, "engels-beyond-dubbele-finaliteit"),
    ("frd", "Frans", BEYOND_DF, "frans-beyond-dubbele-finaliteit"),
]

# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom)
VRAGEN = []

SECTIES = [
    dict(kop="De leerbundels van zes vakken",
         uitleg="Dit is de leerstof om te lezen, één bundel per thema. Klik op de knop, dan "
                "komt er een zip in je map Downloads. Pak die uit en sleep de pdf's in "
                "<span class=\"pad\">Beheer</span>, <span class=\"pad\">Leerstof</span>. "
                "Staan deel 1 en deel 2 van een hoofdstuk apart in de lijst, laad dan "
                "dezelfde bundel twee keer op: ze behandelen dezelfde stof.",
         kaarten=zipkaarten(VAKKEN, "leerbundels", "leerbundels", voor="b-")),
    dict(kop="De oefenbundels van dezelfde zes vakken",
         uitleg="Afdrukbare bundels met ándere opgaven dan die op het scherm, met een "
                "antwoordblad achteraan. Net zo opladen als de leerbundels. Ze staan op een "
                "witte achtergrond, zodat een thuisprinter geen volvlak moet drukken.",
         kaarten=zipkaarten(VAKKEN, "oefenbundels", "oefenbundels", voor="o-")),
]

if VRAGEN:
    SECTIES.append(dict(
        kop="De vragenbestanden",
        uitleg="Klik op de knop, ga naar <span class=\"pad\">Beheer</span>, "
               "<span class=\"pad\">Vakken</span>, open het vak en dan "
               "<span class=\"pad\">Vragen importeren</span>, en plak met ctrl+V. Zet "
               "<span class=\"pad\">Bestaande vragen vervangen</span> wél aan, anders staat "
               "elke vraag een tweede keer in de databank.",
         kaarten=vraagkaarten(VRAGEN)))


def bouw():
    stukken = []
    for nr, s in enumerate(SECTIES, 1):
        stukken.append(f'''  <section>
    <h2><span class="nr">{nr}</span> {s["kop"]}</h2>
    <p>{s["uitleg"]}</p>
    <div class="vakken">{"".join(s["kaarten"])}</div>
  </section>
''')
    aantal = sum(len(s["kaarten"]) for s in SECTIES)
    hier = pathlib.Path(__file__).parent
    pagina = hier / "opladen.html"
    pagina.write_text((hier / "sjabloon.html").read_text(encoding="utf-8")
                      .replace("<!--TITEL-->", TITEL)
                      .replace("<!--INTRO-->", INTRO)
                      .replace("<!--SECTIES-->", "\n".join(stukken))
                      .replace("<!--AANTAL-->", str(aantal))
                      .replace("<!--VOET-->", VOET)
                      .replace("<!--SLEUTEL-->", SLEUTEL),
                      encoding="utf-8")
    print(f"{pagina} — {pagina.stat().st_size / 1024 / 1024:.2f} MB, "
          f"{len(SECTIES)} secties, {aantal} kaarten")


if __name__ == "__main__":
    bouw()

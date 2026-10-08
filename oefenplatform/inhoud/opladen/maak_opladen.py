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
5. Elke ronde schrijft naar haar **eigen** bestand (`BESTAND`). Publiceer je
   twee rondes vanuit dezelfde bestandsnaam, dan overschrijft de tweede de
   plakpagina van de eerste op hetzelfde adres, met haar vinkjes erbij. Dat is
   één keer gebeurd op 8 oktober 2026.

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


def sqlkaarten(lijst):
    """Een kaart per sql-bestand, met de hele inhoud in een kopieerknop.

    Kim draait zo'n bestand in de SQL-editor van Supabase. Dat is plakwerk,
    geen download, dus het gaat op dezelfde manier als een vragenbestand.
    """
    rijen = []
    for sleutel, naam, waar, bestand, waarom in lijst:
        pad = WORTEL.parent / "supabase" / bestand
        tekst = pad.read_text(encoding="utf-8")
        assert "</script" not in tekst.lower(), bestand
        regels = tekst.count("\n") + 1
        rijen.append(f'''
      <article class="vak" data-sleutel="s-{sleutel}">
        <label class="afvink"><input type="checkbox" class="vinkje"><span>gedraaid</span></label>
        <header class="vakkop">
          <div class="vaknaam">
            <h3>{html.escape(naam)}</h3>
            <p class="cat">{html.escape(waar)}</p>
          </div>
          <span class="etiket">sql-editor</span>
        </header>
        <p class="raad">{html.escape(waarom)}</p>
        <div class="knoppen">
          <button class="kopieer" type="button" data-bron="q-{sleutel}">
            Kopieer {html.escape(bestand)} <span class="mee">{regels} regels</span>
          </button>
        </div>
        <p class="gelukt" hidden>Gekopieerd. Plak het nu in de SQL-editor en klik op Run.</p>
        <p class="handmatig" hidden>Het kopiëren lukte niet vanzelf. De tekst staat hieronder
          klaar: tik erin, selecteer alles en kopieer.</p>
        <textarea class="bak" readonly hidden aria-label="de inhoud van {html.escape(bestand)}"></textarea>
        <script type="text/plain" id="q-{sleutel}">{tekst}</script>
      </article>''')
    return rijen


# ════════════════════════════════════════════════════════════
# Vanaf hier staat alles van déze ronde. Enkel dit wijzigt.
# ════════════════════════════════════════════════════════════

BESTAND = "opladen-statistiek.html"
TITEL = "Plakpagina statistiek"
SLEUTEL = "connectopia-plakpagina-statistiek-8-oktober"
VOET = "Bijgewerkt op 8 oktober 2026, 's avonds"
INTRO = """<p>Eén nieuw vak: <strong>statistiek</strong> van 🌍 Beyond doorstroom, gebouwd op de
      vakfiche van de examencommissie. Achttien thema's, zesendertig hoofdstukken, 720 vragen,
      met achttien leerbundels en achttien oefenbundels erbij. De eerste stap moet je echt
      eerst doen, want anders is er geen vak om de vragen in te plakken.</p>
      <p>Onderaan staat nog één los stukje sql, voor de dubbele weetjes van Febe.</p>"""

BEYOND_DO = "🌍 Beyond doorstroom"

# (afvinksleutel, naam, categorie, zipnaam)
LEERBUNDELS = [
    ("lb-stat", "Statistiek", BEYOND_DO, "statistiek-beyond"),
]
OEFENBUNDELS = [
    ("ob-stat", "Statistiek", BEYOND_DO, "statistiek-beyond"),
]

# (afvinksleutel, naam, waar, bestandsnaam, waarom)
SQL = [
    ("weetjes-dubbel", "Dubbele weetjes opruimen", "oefenplatform", "weetjes-dubbel.sql",
     "Ruimt de eenentwintig briefjes van Febe op tot één, en zorgt dat hetzelfde kind "
     "hetzelfde weetje niet nog eens kan insturen. Wat al op het bord hangt blijft hangen."),
]

# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom)
VRAGEN = [
    ("stat", "Statistiek", BEYOND_DO, "beyond", "statistiek",
     "Nieuw vak, dus er staat nog niets in. Vervangen aanzetten kan geen kwaad."),
]

SECTIES = [
    dict(kop="Maak eerst het vak zelf",
         uitleg="Ga naar <span class=\"pad\">Beheer</span>, <span class=\"pad\">Vakken</span>, "
                "kies de categorie <span class=\"pad\">🌍 Beyond doorstroom</span> en klik op "
                "<span class=\"pad\">Een vak toevoegen</span>. Noem het <span class=\"pad\">Statistiek</span> "
                "en zet het vinkje <span class=\"pad\">Rekenmachine (GeoGebra)</span> aan. Dat vinkje "
                "is geen extraatje: twee van de achttien thema\u2019s zijn niet op te lossen zonder de "
                "kansrekenmachine of het rekenblad, en die zitten in dat tabblad. Vergeet je het, "
                "dan kan je het later nog aanzetten met de knop rechts van de vaknaam.",
         kaarten=[]),
    dict(kop="Plak de vragen in het nieuwe vak",
         uitleg="Open het vak dat je net maakte, klik op <span class=\"pad\">Vragen importeren</span> "
                "en plak met ctrl+V. Zet <span class=\"pad\">Bestaande vragen vervangen</span> aan. "
                "Het bestand kiest zelf de categorie, dus de zesendertig hoofdstukken komen onder "
                "🌍 Beyond doorstroom terecht, ook als je ergens anders staat.",
         kaarten=vraagkaarten(VRAGEN)),
    dict(kop="De bundels om af te drukken",
         uitleg="Deze twee hoef je nergens op te laden: ze staan al op het oefenplatform, bij "
                "elk hoofdstuk. Ze staan hier zodat je ze in één keer kan downloaden als je "
                "iets wil afdrukken. Klikken opent het downloadvenster van je browser; daarna "
                "staat er een zip in je map Downloads die je moet uitpakken.",
         kaarten=zipkaarten(LEERBUNDELS, "leerbundels", "leerbundels", voor="l-")
                 + zipkaarten(OEFENBUNDELS, "oefenbundels", "oefenbundels", voor="o-")),
    dict(kop="En nog één stukje sql",
         uitleg="Dit heeft niets met statistiek te maken. Ga naar Supabase, het project van het "
                "<span class=\"pad\">oefenplatform</span>, open de <span class=\"pad\">SQL Editor</span>, "
                "plak en klik op <span class=\"pad\">Run</span>. Je mag het gerust twee keer draaien.",
         kaarten=sqlkaarten(SQL)),
]


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
    pagina = hier / BESTAND
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

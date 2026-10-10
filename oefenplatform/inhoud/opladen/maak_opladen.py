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

BESTAND = "opladen-notatie.html"
TITEL = "Plakpagina wiskundige notatie"
SLEUTEL = "connectopia-plakpagina-notatie-10-oktober"
VOET = "Bijgewerkt op 10 oktober 2026"
INTRO = """<p>Na de opmerking van Enya staan <strong>wiskunde gevorderd</strong> en
      <strong>fysica</strong> van 🌍 Beyond volledig in <strong>echte wiskundige notatie</strong>,
      met tekeningen bij de theorie en veel zwaardere oefenbundels.</p>
      <p>De site staat al online, maar de vragen in jouw databank zijn nog de oude. Daarvoor zijn
      de twee bestanden hieronder: zonder die stap blijft er bij een kind nog altijd
      &#8220;wortel uit vijftig&#8221; staan in plaats van de formule.</p>
      <p>Onderaan staan ook de bundels van twee vakken die er nog helemaal niet in zaten.</p>"""

BEYOND = "🌍 Beyond doorstroom"

# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom)
VRAGEN = [
    ("wg-beyond", "Wiskunde gevorderd", BEYOND, "beyond", "wiskunde-gevorderd",
     "Alle 44 hoofdstukken zitten in dit ene bestand, dus vervangen moet aan. "
     "De antwoorden van de kinderen blijven staan."),
    ("fy-beyond", "Fysica", BEYOND, "beyond", "fysica",
     "Zelfde als hierboven: alle 46 hoofdstukken zitten erin, dus vervangen aan."),
]

# (afvinksleutel, naam, categorie, zipnaam)
LEER_OM = [
    ("l-wg", "Wiskunde gevorderd", BEYOND, "wiskunde-gevorderd-beyond"),
    ("l-fy", "Fysica", BEYOND, "fysica-beyond"),
]
OEF_OM = [
    ("o-wg", "Wiskunde gevorderd", BEYOND, "wiskunde-gevorderd-beyond"),
    ("o-fy", "Fysica", BEYOND, "fysica-beyond"),
]
LEER_NIEUW = [
    ("l-sgw", "Sociale en gedragswetenschappen", BEYOND, "sociale-en-gedragswetenschappen-beyond-doorstroom"),
    ("l-fr", "Filosofie en recht", BEYOND, "filosofie-en-recht-beyond-doorstroom"),
]
OEF_NIEUW = [
    ("o-sgw", "Sociale en gedragswetenschappen", BEYOND, "sociale-en-gedragswetenschappen-beyond-doorstroom"),
    ("o-fr", "Filosofie en recht", BEYOND, "filosofie-en-recht-beyond-doorstroom"),
]

SECTIES = [
    dict(kop="Laad de twee vragenbestanden opnieuw in",
         uitleg="Open het vak in <span class=\"pad\">Beheer</span>, "
                "<span class=\"pad\">Vakken</span>, categorie "
                "<span class=\"pad\">🌍 Beyond doorstroom</span>, klik op "
                "<span class=\"pad\">Vragen importeren</span>, plak met ctrl+V en zet "
                "<span class=\"pad\">Bestaande vragen vervangen</span> aan. Zonder dat vinkje "
                "krijg je alles dubbel. Dit is de stap die de notatie bij de kinderen brengt.",
         kaarten=vraagkaarten(VRAGEN)),
    dict(kop="Vervang de leerbundels van die twee vakken",
         uitleg="Ga naar <span class=\"pad\">Beheer</span>, <span class=\"pad\">Leerstof</span>. "
                "Pak de zip uit en sleep alle pdf&#8217;s er in één keer in: het formulier zoekt "
                "zelf het juiste hoofdstuk en vraagt of het de oude mag vervangen. Zeg ja, want "
                "in de oude staat de theorie nog in woorden.",
         kaarten=zipkaarten(LEER_OM, "leerbundels", "leerbundels")),
    dict(kop="Vervang ook de oefenbundels",
         uitleg="Zelfde plek en zelfde werkwijze. Deze zijn niet alleen in notatie herschreven, "
                "ze zijn ook veel groter geworden: waar er elf oefeningen stonden, staan er nu "
                "een dertigtal, met echt rekenwerk in plaats van enkel begrippen.",
         kaarten=zipkaarten(OEF_OM, "oefenbundels", "oefenbundels")),
    dict(kop="Twee vakken die nog geen enkele bundel hebben",
         uitleg="Sociale en gedragswetenschappen en filosofie en recht staan wel in het "
                "oefenplatform, maar er hangt nog geen leerstof aan. Hier is er niets te "
                "vervangen, je laadt ze gewoon op. Twintig leerbundels per vak.",
         kaarten=zipkaarten(LEER_NIEUW, "leerbundels", "leerbundels")),
    dict(kop="En hun oefenbundels",
         uitleg="Zelfde twee vakken, zelfde werkwijze. Twintig oefenbundels per vak, elk met een "
                "antwoordblad achteraan dat je eraf scheurt voor je ze aan een kind geeft.",
         kaarten=zipkaarten(OEF_NIEUW, "oefenbundels", "oefenbundels")),
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

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
    for sleutel, naam, cat, map_, bestand, waarom, *rest in lijst:
        # Het etiket staat standaard op "vervangen aan". Eén bestand per ronde
        # wil het omgekeerde: start/wiskunde-extra.json zet de tweede reeks
        # vragen erbíj, dus daar moet het vinkje uit.
        etiket = rest[0] if rest else "zet vervangen aan"
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
          <span class="etiket">{html.escape(etiket)}</span>
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
VOET = "Bijgewerkt op 11 oktober 2026"
INTRO = """<p>Na de opmerking van Enya staat <strong>het hele oefenplatform</strong> in
      <strong>echte wiskundige notatie</strong>: breuken met een streep, wortels, exponenten,
      graden, en bij de wetenschappen ook de symbolen (<em>Q</em>, &#916;<em>T</em>,
      <em>E</em><sub>p,gr</sub>) en de tekeningen erbij.</p>
      <p>De site staat online, maar de vragen in jouw databank zijn nog de oude. Daarvoor zijn de
      kopieerknoppen hieronder: zonder die stap blijft er bij een kind nog altijd
      &#8220;wortel uit vijftig&#8221; staan in plaats van de formule.</p>
      <p>Het zijn veel bestanden, want het ging over alle acht de categorie&#235;n. Je kan rustig
      per blok werken: de vinkjes blijven staan als je de pagina sluit, ook op je telefoon.
      De twee bovenaan stonden al op deze pagina; de rest is van vandaag.</p>"""

BEYOND = "🌍 Beyond doorstroom"
BEYOND_DF = "🌍 Beyond dubbele finaliteit"
BOOST = "🚀 Boost doorstroom"
BOOST_DF = "🚀 Boost dubbele finaliteit"
SPARK = "✨ Spark"
START = "🌱 Start"
# Let op: BASIS is hierboven de raw-link van github, vandaar NIV_BASIS.
NIV_BASIS = "🧱 Basis"
HOEK = "🔭 Uitdagingshoek"

AL = ("Alle hoofdstukken van dit vak zitten in dit ene bestand, dus vervangen moet aan. "
      "De voortgang van de kinderen blijft staan.")
ERBIJ = ("Dit bestand raakt enkel zijn eigen hoofdstukken aan; de andere hoofdstukken van het "
         "vak blijven ongemoeid.")

# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom, [etiket])
# De sleutels wg-beyond en fy-beyond stonden al op de pagina van 10 oktober:
# laat ze staan zoals ze zijn, anders verliest Kim haar vinkje erop.
VR_BEYOND = [
    ("wg-beyond", "Wiskunde gevorderd", BEYOND, "beyond", "wiskunde-gevorderd", AL),
    ("fy-beyond", "Fysica", BEYOND, "beyond", "fysica", AL),
    ("st-beyond", "Statistiek", BEYOND, "beyond", "statistiek", AL),
    ("ch-beyond", "Chemie", BEYOND, "beyond", "chemie",
     "De scheikunde blijft met kleine cijfertjes geschreven (SO₄²⁻, H₂O); enkel het rekenwerk "
     "eromheen is formule geworden. " + AL),
    ("nw-beyond", "Natuurwetenschappen", BEYOND, "beyond", "natuurwetenschappen", AL),
]
VR_BEYOND_DF = [
    ("wi-bdf", "Wiskunde", BEYOND_DF, "beyond-dubbele-finaliteit", "wiskunde", AL),
    ("nw-bdf", "Natuurwetenschappen", BEYOND_DF, "beyond-dubbele-finaliteit",
     "natuurwetenschappen", AL),
]
VR_BOOST = [
    ("wb-boost", "Wiskunde basis", BOOST, "boost-doorstroom", "wiskunde-basis", AL),
    ("wg-boost", "Wiskunde gevorderd", BOOST, "boost-doorstroom", "wiskunde-gevorderd", AL),
    ("fy-boost", "Fysica", BOOST, "boost-doorstroom", "fysica", AL),
    ("ch-boost", "Chemie", BOOST, "boost-doorstroom", "chemie", AL),
    ("nw-boost", "Natuurwetenschappen", BOOST, "boost-doorstroom", "natuurwetenschappen", AL),
]
VR_BOOST_DF = [
    ("wi-sdf", "Wiskunde", BOOST_DF, "boost-dubbele-finaliteit", "wiskunde", AL),
    ("nw-sdf", "Natuurwetenschappen", BOOST_DF, "boost-dubbele-finaliteit",
     "natuurwetenschappen", AL),
]
VR_SPARK = [
    ("wi-spark", "Wiskunde", SPARK, "spark", "wiskunde",
     "Meetkunde en metend rekenen zitten hier in, met hun tekeningen. " + AL),
    ("wu-spark", "Wiskunde — het uitdagingshoofdstuk", SPARK, "uitdaging",
     "spark-wiskunde-uitdaging",
     "Open hetzelfde vak Wiskunde. " + ERBIJ),
    ("nw-spark", "Natuurwetenschappen", SPARK, "spark", "natuurwetenschappen", AL),
    ("nu-spark", "Natuurwetenschappen — het uitdagingshoofdstuk", SPARK, "uitdaging",
     "spark-natuurwetenschappen-uitdaging",
     "Open hetzelfde vak Natuurwetenschappen. " + ERBIJ),
    ("te-spark", "Techniek", SPARK, "spark", "techniek", AL),
]
VR_START = [
    ("wi-start", "Wiskunde — de eerste reeks", START, "start", "wiskunde",
     "Doe deze eerst, met vervangen aan: hij zet de twintig eerste vragen per hoofdstuk."),
    ("wx-start", "Wiskunde — de tweede reeks", START, "start", "wiskunde-extra",
     "Doe deze meteen daarna, en zet vervangen nu UIT: hij legt de twintig andere vragen "
     "erbij, zodat je weer aan veertig per hoofdstuk komt.", "zet vervangen UIT"),
    ("wr-start", "Wiskunde — Rekenen en breuken", START, "start",
     "wiskunde-rekenen-en-breuken",
     "Het gratis proefhoofdstuk, 37 vragen. Open hetzelfde vak Wiskunde. " + ERBIJ),
    ("wp-start", "Wiskunde — de pittige hoofdstukken", START, "pittig",
     "start-wiskunde-pittig", "Open hetzelfde vak Wiskunde. " + ERBIJ),
    ("wu-start", "Wiskunde — het uitdagingshoofdstuk", START, "uitdaging",
     "start-wiskunde-uitdaging", "Open hetzelfde vak Wiskunde. " + ERBIJ),
    ("wt-start", "Wetenschap en techniek", START, "start", "wetenschap-en-techniek", AL),
    ("tp-start", "Wetenschap en techniek — de pittige hoofdstukken", START, "pittig",
     "start-wetenschap-en-techniek-pittig",
     "Open hetzelfde vak Wetenschap en techniek. " + ERBIJ),
    ("tu-start", "Wetenschap en techniek — het uitdagingshoofdstuk", START, "uitdaging",
     "start-wetenschap-en-techniek-uitdaging",
     "Open hetzelfde vak Wetenschap en techniek. " + ERBIJ),
]
VR_BASIS = [
    ("wi-basis", "Wiskunde — de tien hoofdstukken", NIV_BASIS, "basis", "wiskunde", AL),
    ("wx-basis", "Wiskunde — kommagetallen en breuken in beeld", NIV_BASIS, "basis",
     "wiskunde-extra",
     "De twee hoofdstukken die er later bij kwamen. Open hetzelfde vak Wiskunde. " + ERBIJ),
]
VR_HOEK = [
    ("hr-hoek", "De ruimte", HOEK, "hoekje", "de-ruimte", AL),
    ("hc-hoek", "Coderen en computers", HOEK, "hoekje", "coderen-en-computers", AL),
    ("hp-hoek", "Paradoxen en weetjes", HOEK, "hoekje", "paradoxen-en-weetjes", AL),
]

# (afvinksleutel, naam, categorie, zipnaam)
LEER_OM = [
    ("l-wg", "Wiskunde gevorderd", BEYOND, "wiskunde-gevorderd-beyond"),
    ("l-fy", "Fysica", BEYOND, "fysica-beyond"),
    ("l-st", "Statistiek", BEYOND, "statistiek-beyond"),
    ("l-ch", "Chemie", BEYOND, "chemie-beyond"),
    ("l-nw", "Natuurwetenschappen", BEYOND, "natuurwetenschappen-beyond"),
    ("l-wibdf", "Wiskunde", BEYOND_DF, "wiskunde-beyond-dubbele-finaliteit"),
    ("l-nwbdf", "Natuurwetenschappen", BEYOND_DF, "natuurwetenschappen-beyond-dubbele-finaliteit"),
    ("l-wbbo", "Wiskunde basis", BOOST, "wiskunde-basis-boost-doorstroom"),
    ("l-wgbo", "Wiskunde gevorderd", BOOST, "wiskunde-gevorderd-boost-doorstroom"),
    ("l-fybo", "Fysica", BOOST, "fysica-boost-doorstroom"),
    ("l-chbo", "Chemie", BOOST, "chemie-boost-doorstroom"),
    ("l-nwbo", "Natuurwetenschappen", BOOST, "natuurwetenschappen-boost-doorstroom"),
    ("l-wisdf", "Wiskunde", BOOST_DF, "wiskunde-boost-dubbele-finaliteit"),
    ("l-nwsdf", "Natuurwetenschappen", BOOST_DF, "natuurwetenschappen-boost-dubbele-finaliteit"),
    ("l-wisp", "Wiskunde", SPARK, "wiskunde-spark"),
    ("l-nwsp", "Natuurwetenschappen", SPARK, "natuurwetenschappen-spark"),
    ("l-wist", "Wiskunde", START, "wiskunde-start"),
    ("l-wiba", "Wiskunde", NIV_BASIS, "wiskunde-basis"),
]
OEF_OM = [
    ("o-wg", "Wiskunde gevorderd", BEYOND, "wiskunde-gevorderd-beyond"),
    ("o-fy", "Fysica", BEYOND, "fysica-beyond"),
    ("o-st", "Statistiek", BEYOND, "statistiek-beyond"),
    ("o-ch", "Chemie", BEYOND, "chemie-beyond"),
    ("o-nw", "Natuurwetenschappen", BEYOND, "natuurwetenschappen-beyond"),
    ("o-wibdf", "Wiskunde", BEYOND_DF, "wiskunde-beyond-dubbele-finaliteit"),
    ("o-nwbdf", "Natuurwetenschappen", BEYOND_DF, "natuurwetenschappen-beyond-dubbele-finaliteit"),
    ("o-wbbo", "Wiskunde basis", BOOST, "wiskunde-basis-boost-doorstroom"),
    ("o-wgbo", "Wiskunde gevorderd", BOOST, "wiskunde-gevorderd-boost-doorstroom"),
    ("o-fybo", "Fysica", BOOST, "fysica-boost-doorstroom"),
    ("o-chbo", "Chemie", BOOST, "chemie-boost-doorstroom"),
    ("o-nwbo", "Natuurwetenschappen", BOOST, "natuurwetenschappen-boost-doorstroom"),
    ("o-wisdf", "Wiskunde", BOOST_DF, "wiskunde-boost-dubbele-finaliteit"),
    ("o-nwsdf", "Natuurwetenschappen", BOOST_DF, "natuurwetenschappen-boost-dubbele-finaliteit"),
    ("o-wisp", "Wiskunde", SPARK, "wiskunde-spark"),
    ("o-nwsp", "Natuurwetenschappen", SPARK, "natuurwetenschappen-spark"),
    ("o-wist", "Wiskunde", START, "wiskunde-start"),
]
LEER_NIEUW = [
    ("l-sgw", "Sociale en gedragswetenschappen", BEYOND, "sociale-en-gedragswetenschappen-beyond-doorstroom"),
    ("l-fr", "Filosofie en recht", BEYOND, "filosofie-en-recht-beyond-doorstroom"),
]
OEF_NIEUW = [
    ("o-sgw", "Sociale en gedragswetenschappen", BEYOND, "sociale-en-gedragswetenschappen-beyond-doorstroom"),
    ("o-fr", "Filosofie en recht", BEYOND, "filosofie-en-recht-beyond-doorstroom"),
]

WEG = ('Open <span class="pad">Beheer</span>, <span class="pad">Vakken</span>, '
       'categorie <span class="pad">%s</span>, dan het vak, dan '
       '<span class="pad">Vragen importeren</span>. Plak met ctrl+V en zet '
       '<span class="pad">Bestaande vragen vervangen</span> aan, tenzij het bij de kaart '
       'anders staat. Zonder dat vinkje krijg je de vragen dubbel.')

SECTIES = [
    dict(kop="🌍 Beyond doorstroom", uitleg=WEG % BEYOND, kaarten=vraagkaarten(VR_BEYOND)),
    dict(kop="🌍 Beyond dubbele finaliteit", uitleg=WEG % BEYOND_DF,
         kaarten=vraagkaarten(VR_BEYOND_DF)),
    dict(kop="🚀 Boost doorstroom", uitleg=WEG % BOOST, kaarten=vraagkaarten(VR_BOOST)),
    dict(kop="🚀 Boost dubbele finaliteit", uitleg=WEG % BOOST_DF,
         kaarten=vraagkaarten(VR_BOOST_DF)),
    dict(kop="✨ Spark", uitleg=WEG % SPARK, kaarten=vraagkaarten(VR_SPARK)),
    dict(kop="🌱 Start", uitleg=WEG % START + " Bij wiskunde is de volgorde hier wél "
         "belangrijk: eerst de eerste reeks met vervangen aan, dan de tweede met het "
         "vinkje uit.", kaarten=vraagkaarten(VR_START)),
    dict(kop="🧱 Basis", uitleg=WEG % NIV_BASIS, kaarten=vraagkaarten(VR_BASIS)),
    dict(kop="🔭 De uitdagingshoek", uitleg=WEG % HOEK, kaarten=vraagkaarten(VR_HOEK)),
    dict(kop="De leerbundels van die vakken vervangen",
         uitleg="Ga naar <span class=\"pad\">Beheer</span>, <span class=\"pad\">Leerstof</span>. "
                "Pak de zip uit en sleep alle pdf&#8217;s er in één keer in: het formulier zoekt "
                "zelf het juiste hoofdstuk en vraagt of het de oude mag vervangen. Zeg ja, want "
                "in de oude staat de theorie nog in woorden.",
         kaarten=zipkaarten(LEER_OM, "leerbundels", "leerbundels")),
    dict(kop="En hun oefenbundels",
         uitleg="Zelfde plek en zelfde werkwijze. Deze zijn niet alleen in notatie herschreven, "
                "ze zijn ook zwaarder geworden: meer echt rekenwerk en minder begrippen. "
                "🧱 Basis staat hier niet bij, want dat niveau heeft nog geen oefenbundels.",
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

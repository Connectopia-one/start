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

BESTAND = "opladen-inhoudsronde.html"
TITEL = "Plakpagina inhoudsronde"
SLEUTEL = "connectopia-plakpagina-inhoudsronde-13-oktober"
VOET = "Bijgewerkt op 13 oktober 2026"
INTRO = """<p>Deze ronde gaat over de <strong>inhoud van de vragen zelf</strong>, niet over het
      platform. Twee dingen zijn rechtgezet.</p>
      <p><strong>Eén.</strong> De opties van een meerkeuzevraag worden bij het tonen door elkaar
      gezet, zodat het juiste antwoord niet altijd bovenaan staat. Maar in de uitleg stond bij
      166 vragen nog &#8220;De eerste drie zijn juist&#8221; of &#8220;De laatste moet it rains
      zijn&#8221;. Een kind dat die uitleg las, zag die drie niet bovenaan staan. Dat is nu
      overal vervangen door iets dat blijft kloppen: <em>de drie juiste antwoorden</em>,
      <em>de twee andere</em>, <em>het foute antwoord</em>.</p>
      <p><strong>Twee.</strong> Bij Techniek ✨ Spark stonden 59 van de 66 aankruisvragen op
      precies drie juiste antwoorden. Drieëntwintig vragen zijn herschreven naar twee of vier,
      zodat een kind het aantal niet meer kan afleiden. Dat is het eerste vak van die lijst van
      49; de andere volgen vak per vak, en elk vak komt op deze pagina te staan zodra het
      helemaal af is.</p>
      <p>Elke kaart hieronder is één bestand met één klik. De vinkjes blijven staan als je de
      pagina sluit, ook op je telefoon.</p>"""

BEYOND = "🌍 Beyond doorstroom"
BEYOND_DF = "🌍 Beyond dubbele finaliteit"
BOOST = "🚀 Boost doorstroom"
BOOST_DF = "🚀 Boost dubbele finaliteit"
SPARK = "✨ Spark"
START = "🌱 Start"
NIV_BASIS = "🧱 Basis"
HOEK = "🔭 Uitdagingshoek"

AL = ("Alle hoofdstukken van dit vak zitten in dit ene bestand, dus vervangen moet aan. "
      "De voortgang van de kinderen blijft staan.")
WISSEL = ("De wisselende woorden van de grammaticahoofdstukken zitten er al in, dus je hoeft "
          "het aparte variantenbestand er niet meer bij te doen. " + AL)

# (afvinksleutel, naam, categorie, map, bestandsnaam, waarom, [etiket])
VR_BEYOND = [
    ("u-fr-be", "Filosofie en recht", BEYOND, "beyond", "filosofie-en-recht",
     "Hier zaten de meeste: 69 vragen begonnen met &#8220;De eerste twee.&#8221; " + AL),
    ("u-fy-be", "Fysica", BEYOND, "beyond", "fysica", AL),
    ("u-gs-be", "Geschiedenis", BEYOND, "beyond", "geschiedenis", AL),
    ("u-nw-be", "Natuurwetenschappen", BEYOND, "beyond", "natuurwetenschappen", AL),
    ("u-en-be", "Engels", BEYOND, "beyond", "engels", AL),
    ("u-frs-be", "Frans", BEYOND, "beyond", "frans", AL),
]
VR_BEYOND_DF = [
    ("u-nl-bdf", "Nederlands", BEYOND_DF, "beyond-dubbele-finaliteit", "nederlands", AL),
    ("u-en-bdf", "Engels", BEYOND_DF, "beyond-dubbele-finaliteit", "engels", AL),
    ("u-frs-bdf", "Frans", BEYOND_DF, "beyond-dubbele-finaliteit", "frans", AL),
]
VR_BOOST = [
    ("u-nl-bo", "Nederlands", BOOST, "boost-doorstroom", "nederlands", WISSEL),
    ("u-en-bo", "Engels", BOOST, "boost-doorstroom", "engels", WISSEL),
    ("u-frs-bo", "Frans", BOOST, "boost-doorstroom", "frans", AL),
    ("u-gs-bo", "Geschiedenis", BOOST, "boost-doorstroom", "geschiedenis", AL),
    ("u-ec-bo", "Economie", BOOST, "boost-doorstroom", "economie", AL),
    ("u-sgw-bo", "Sociale en gedragswetenschappen", BOOST, "boost-doorstroom",
     "sociale-en-gedragswetenschappen", AL),
    ("u-wb-bo", "Wiskunde basis", BOOST, "boost-doorstroom", "wiskunde-basis", AL),
]
VR_BOOST_DF = [
    ("u-nl-sdf", "Nederlands", BOOST_DF, "boost-dubbele-finaliteit", "nederlands", WISSEL),
    ("u-en-sdf", "Engels", BOOST_DF, "boost-dubbele-finaliteit", "engels", WISSEL),
    ("u-gs-sdf", "Geschiedenis", BOOST_DF, "boost-dubbele-finaliteit", "geschiedenis", AL),
    ("u-nw-sdf", "Natuurwetenschappen", BOOST_DF, "boost-dubbele-finaliteit",
     "natuurwetenschappen", AL),
    ("u-gzw-sdf", "Gezondheid, zorg en welzijn", BOOST_DF, "boost-dubbele-finaliteit",
     "gezondheid-zorg-en-welzijn", AL),
]
VR_SPARK = [
    ("u-te-sp", "Techniek", SPARK, "spark", "techniek",
     "Dit is het vak waar ook het aantal juiste antwoorden rechtgetrokken is: 23 vragen "
     "staan nu op twee of vier in plaats van drie. " + AL),
    ("u-nl-sp", "Nederlands", SPARK, "spark", "nederlands", WISSEL),
    ("u-gs-sp", "Geschiedenis", SPARK, "spark", "geschiedenis", AL),
    ("u-nw-sp", "Natuurwetenschappen", SPARK, "spark", "natuurwetenschappen", AL),
    ("u-se-sp", "Samenleving en economie", SPARK, "spark", "samenleving-en-economie", AL),
]

WEG = ('Open <span class="pad">Beheer</span>, <span class="pad">Vakken</span>, '
       'categorie <span class="pad">%s</span>, dan het vak, dan '
       '<span class="pad">Vragen importeren</span>. Plak met ctrl+V en zet '
       '<span class="pad">Bestaande vragen vervangen</span> aan. Zonder dat vinkje krijg je '
       'de vragen dubbel.')

SECTIES = [
    dict(kop="🌍 Beyond doorstroom", uitleg=WEG % BEYOND, kaarten=vraagkaarten(VR_BEYOND)),
    dict(kop="🌍 Beyond dubbele finaliteit", uitleg=WEG % BEYOND_DF,
         kaarten=vraagkaarten(VR_BEYOND_DF)),
    dict(kop="🚀 Boost doorstroom", uitleg=WEG % BOOST, kaarten=vraagkaarten(VR_BOOST)),
    dict(kop="🚀 Boost dubbele finaliteit", uitleg=WEG % BOOST_DF,
         kaarten=vraagkaarten(VR_BOOST_DF)),
    dict(kop="✨ Spark", uitleg=WEG % SPARK, kaarten=vraagkaarten(VR_SPARK)),
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

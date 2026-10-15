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
import html, json, pathlib, sys, zipfile

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

BEYOND = "🌍 Beyond doorstroom"
BEYOND_DF = "🌍 Beyond dubbele finaliteit"
BOOST = "🚀 Boost doorstroom"
BOOST_DF = "🚀 Boost dubbele finaliteit"
SPARK = "✨ Spark"
HOEK = "🔭 Uitdagingshoek"

AL = ("Alle hoofdstukken van dit vak zitten in dit ene bestand, dus vervangen moet aan. "
      "De voortgang van de kinderen blijft staan.")
EEN = ("In dit bestand zit enkel het hoofdstuk Uitdaging — alles door elkaar van dit vak. "
       "De andere hoofdstukken blijven gewoon staan; vervangen moet toch aan, anders komen "
       "die twintig vragen dubbel.")
WISSEL = ("De wisselende woorden van de grammaticahoofdstukken zitten er al in, dus je hoeft "
          "het aparte variantenbestand er niet meer bij te doen. " + AL)

GETAL = {2: "twee", 3: "drie", 4: "vier", 5: "vijf", 6: "zes"}

# Enkel de vaknamen die niet gewoon de bestandsnaam met hoofdletter zijn.
NAMEN = {
    "sociale-en-gedragswetenschappen": "Sociale en gedragswetenschappen",
    "kunstbeschouwing-en-filosofie": "Kunstbeschouwing en filosofie",
    "filosofie-en-recht": "Filosofie en recht",
    "samenleving-en-economie": "Samenleving en economie",
    "economie-en-bedrijfswetenschappen": "Economie en bedrijfswetenschappen",
    "gezondheid-zorg-en-welzijn": "Gezondheid, zorg en welzijn",
    "ontwikkeling-en-pedagogisch-handelen": "Ontwikkeling en pedagogisch handelen",
    "toegepaste-economie": "Toegepaste economie",
    "wiskunde-basis": "Wiskunde basis",
    "nederlands-begrijpend-lezen": "Nederlands — begrijpend lezen",
    "nederlands-spelling-varianten": "Nederlands — spelling",
    "spark-nederlands-uitdaging": "Nederlands — Uitdaging, alles door elkaar",
    "spark-geschiedenis-uitdaging": "Geschiedenis — Uitdaging, alles door elkaar",
}


def naam_van(bestand):
    if bestand in NAMEN:
        return NAMEN[bestand]
    return bestand.replace("-", " ").capitalize()


def meet(pad):
    """Hoeveel juiste antwoorden een aankruisvraag heeft, de wisselende beurten
    meegeteld, en hoe vaak "Geen van deze antwoorden" erbij staat."""
    data = json.loads(pad.read_text(encoding="utf-8"))
    tel, gvd, gvd_juist = {}, 0, 0
    for h in data["hoofdstukken"]:
        for v in h.get("vragen", []):
            opties = v.get("opties") or []
            plaats = [i for i, o in enumerate(opties) if "Geen van deze" in str(o)]
            if plaats:
                gvd += 1
                a = v.get("antwoord")
                if a == plaats[0] or (isinstance(a, list) and plaats[0] in a):
                    gvd_juist += 1
            for b in [v] + [{**v, **w} for w in (v.get("varianten") or [])]:
                a = b.get("antwoord")
                if isinstance(a, list) and len(a) >= 2 and all(isinstance(x, int) for x in a):
                    tel[len(a)] = tel.get(len(a), 0) + 1
    return tel, gvd, gvd_juist


def opsomming(stukken):
    if len(stukken) == 1:
        return stukken[0]
    return ", ".join(stukken[:-1]) + " en " + stukken[-1]


def waarom_van(map_, bestand, staart):
    """De regel onder de vaknaam, gerekend uit het bestand zelf."""
    tel, gvd, gvd_juist = meet(WORTEL / map_ / f"{bestand}.json")
    delen = []
    if tel:
        n = sum(tel.values())
        zin = opsomming([f"{a} op {GETAL[k]}" for k, a in sorted(tel.items())])
        delen.append(f"Het aantal juiste antwoorden is gespreid: {zin}. "
                     f"Het grootste groepje is {round(100 * max(tel.values()) / n)} procent "
                     f"van de {n} aankruisvragen.")
    else:
        delen.append("Dit vak heeft geen aankruisvragen, dus daar was niets te spreiden.")
    if gvd:
        hoe = (f", en bij {gvd_juist} is ze ook het juiste antwoord" if gvd_juist
               else ", telkens als afleider")
        delen.append(f"Bij {gvd} vragen staat de optie “Geen van deze antwoorden” erbij{hoe}.")
    delen.append(staart)
    return " ".join(delen)


def kaarten_van(map_, cat, bestanden, staarten=None):
    staarten = staarten or {}
    lijst = [(f"{map_}-{b}", naam_van(b), cat, map_, b,
              waarom_van(map_, b, staarten.get(b, AL)))
             for b in bestanden]
    return vraagkaarten(lijst)


WEG = ('Open <span class="pad">Beheer</span>, <span class="pad">Vakken</span>, '
       'categorie <span class="pad">%s</span>, dan het vak, dan '
       '<span class="pad">Vragen importeren</span>. Plak met ctrl+V en zet '
       '<span class="pad">Bestaande vragen vervangen</span> aan. Zonder dat vinkje krijg je '
       'de vragen dubbel.')

DRIE = """<p><strong>Eén.</strong> De opties van een meerkeuzevraag worden bij het tonen door
      elkaar gezet, zodat het juiste antwoord niet altijd bovenaan staat. Maar in de uitleg
      stond bij 166 vragen nog “De eerste drie zijn juist” of “De laatste moet it rains zijn”.
      Een kind dat die uitleg las, zag die drie niet bovenaan staan. Dat is nu overal vervangen
      door iets dat blijft kloppen: <em>de juiste antwoorden</em>, <em>de twee andere</em>,
      <em>het foute antwoord</em>.</p>
      <p><strong>Twee.</strong> Het aantal juiste antwoorden bij een aankruisvraag. Bij de meeste
      vakken stond bijna alles op precies drie, dus kon een kind er drie aanvinken zonder de
      leerstof te kennen. Dat is nu <strong>in elk vak</strong> gespreid, van 🌱 Start tot
      🌍 Beyond: het grootste groepje zit overal tussen een derde en de helft, en op elke kaart
      hieronder staat de verdeling van dat vak erbij. Bij chemie, biologie en filosofie en recht
      van 🌍 Beyond is het de helft twee en de helft drie, en dat is net zo onvoorspelbaar.</p>
      <p><strong>Drie.</strong> Het idee van Febe: vragen waarbij <strong>geen enkel</strong>
      antwoord juist is, of net <strong>alle</strong>. In negen vakken van ✨ Spark staat nu bij
      tien vragen de optie “Geen van deze antwoorden”, en bij vier van die tien is ze ook het
      juiste antwoord. Dat ze er staat, verklapt dus niets. Die optie blijft bij het schudden
      altijd onderaan, want in het midden van een lijst leest ze als onzin.</p>"""

SAMEN = """<p>Alle vragen van een ronde samen zijn te veel tekst voor één pagina, dus staan ze
      op twee. %s</p>
      <p>Elke kaart hieronder is één bestand met één klik, met de verdeling van dat vak erbij.
      De vinkjes blijven staan als je de pagina sluit, ook op je telefoon. Ze zijn wel één keer
      leeggemaakt, omdat er vakken bij gekomen zijn: had je er vandaag al een ingeladen, doe het
      dan gewoon opnieuw met vervangen aan. Twee keer inladen met dat vinkje aan kan geen
      kwaad.</p>"""

PAGINAS = [
    dict(
        bestand="opladen-meldingen-15-oktober.html",
        titel="Plakpagina — de meldingen van 15 oktober",
        sleutel="connectopia-plakpagina-meldingen-15-oktober",
        voet="Bijgewerkt op 15 oktober 2026",
        intro="""<p>Drie meldingen uit het oefenplatform zijn rechtgezet. Twee kleine
      bestanden volstaan: ze bevatten enkel de hoofdstukken waarin iets veranderde, dus
      je hoeft geen heel vak opnieuw in te laden.</p>
      <p><strong>Eén.</strong> De Tweede Wereldoorlog stond bij 🚀 Boost in de
      hedendaagse tijd. Dat klopt niet: de moderne tijd loopt tot 1945 en pas daarna
      begint de hedendaagse tijd. De leerbundel van Boost zei 1914, terwijl ✨ Spark en
      🌍 Beyond overal 1945 aanhouden. Alles staat nu op 1945.</p>
      <p><strong>Twee.</strong> In De prehistorie (✨ Spark) stonden Homo sapiens en
      Homo erectus met een kleine letter, terwijl natuurwetenschappen ze wel met een
      hoofdletter schrijft.</p>
      <p><strong>Drie.</strong> Vijf uitlegteksten bij filosofie en recht toonden een
      opmaakteken als gewone tekst op het scherm. Dat teken is weg.</p>
      <p>De codetaal onder de tekeningen van de tocht is ook hersteld, maar daar hoef je
      niets voor te doen: dat zat in het platform zelf en staat al online.</p>""",
        secties=[
            dict(
                kop="Twee kleine bestanden",
                uitleg="Elk hoofdstuk draagt zijn categorie zelf mee, dus je kiest enkel "
                       "het vak. " + WEG % "de categorie maakt hier niet uit",
                kaarten=vraagkaarten([
                    (
                        "herstel-geschiedenis",
                        "Geschiedenis",
                        "✨ Spark en 🚀 Boost, drie hoofdstukken",
                        "herstel",
                        "geschiedenis-herstel",
                        "Hierin zitten De prehistorie — deel 1 van ✨ Spark en Het "
                        "historisch referentiekader — deel 1 van allebei de "
                        "Boost-richtingen. De rest van het vak blijft zoals het is.",
                    ),
                    (
                        "herstel-filosofie",
                        "Filosofie en recht",
                        "🌍 Beyond doorstroom, drie hoofdstukken",
                        "herstel",
                        "filosofie-en-recht-herstel",
                        "Enkel de drie hoofdstukken waarin een uitlegtekst veranderde.",
                    ),
                ]),
            ),
        ],
    ),
    dict(
        bestand="opladen-inhoudsronde.html",
        titel="Plakpagina inhoudsronde — 🌍 Beyond",
        sleutel="connectopia-plakpagina-inhoudsronde-beyond",
        voet="Bijgewerkt op 13 oktober 2026",
        intro="""<p>Deze ronde gaat over de <strong>inhoud van de vragen zelf</strong>, niet over
      het platform. Drie dingen zijn rechtgezet.</p>
      """ + DRIE + SAMEN % ("Hier staan de achttien vakken van 🌍 Beyond; 🚀 Boost, ✨ Spark en "
                            "de uitdagingshoek staan op <a href=\"https://claude.ai/artifact/KZSHgn7GrQawBMJVdYF9Hz\">de tweede plakpagina</a>."),
        secties=[
            dict(kop=BEYOND, uitleg=WEG % BEYOND, kaarten=kaarten_van(
                "beyond", BEYOND,
                ["nederlands", "engels", "frans", "geschiedenis", "aardrijkskunde",
                 "samenleving-en-economie", "sociale-en-gedragswetenschappen",
                 "filosofie-en-recht", "biologie", "chemie", "fysica", "natuurwetenschappen"])),
            dict(kop=BEYOND_DF, uitleg=WEG % BEYOND_DF, kaarten=kaarten_van(
                "beyond-dubbele-finaliteit", BEYOND_DF,
                ["nederlands", "engels", "frans", "geschiedenis", "aardrijkskunde",
                 "natuurwetenschappen"])),
        ],
    ),
    dict(
        bestand="opladen-inhoudsronde-2.html",
        titel="Plakpagina inhoudsronde — 🚀 Boost en ✨ Spark",
        sleutel="connectopia-plakpagina-inhoudsronde-boost-spark",
        voet="Bijgewerkt op 13 oktober 2026",
        intro="""<p>Deze ronde gaat over de <strong>inhoud van de vragen zelf</strong>, niet over
      het platform. Drie dingen zijn rechtgezet.</p>
      """ + DRIE + SAMEN % ("Hier staan 🚀 Boost, ✨ Spark en de uitdagingshoek; de achttien "
                            "vakken van 🌍 Beyond staan op "
                            "<a href=\"https://claude.ai/artifact/WRm2P4DqFzuMzy7Gxp5Kb1\">"
                            "de eerste plakpagina</a>."),
        secties=[
            dict(kop=BOOST, uitleg=WEG % BOOST, kaarten=kaarten_van(
                "boost-doorstroom", BOOST,
                ["nederlands", "engels", "frans", "geschiedenis", "aardrijkskunde", "economie",
                 "sociale-en-gedragswetenschappen", "kunstbeschouwing-en-filosofie",
                 "wiskunde-basis", "biologie", "chemie", "fysica", "natuurwetenschappen"],
                {"nederlands": WISSEL, "engels": WISSEL})),
            dict(kop=BOOST_DF, uitleg=WEG % BOOST_DF, kaarten=kaarten_van(
                "boost-dubbele-finaliteit", BOOST_DF,
                ["nederlands", "engels", "frans", "geschiedenis", "aardrijkskunde",
                 "economie-en-bedrijfswetenschappen", "toegepaste-economie",
                 "ontwikkeling-en-pedagogisch-handelen", "gezondheid-zorg-en-welzijn",
                 "natuurwetenschappen"],
                {"nederlands": WISSEL, "engels": WISSEL})),
            dict(kop=SPARK, uitleg=WEG % SPARK, kaarten=kaarten_van(
                "spark", SPARK,
                ["nederlands", "nederlands-spelling-varianten", "nederlands-begrijpend-lezen",
                 "engels", "frans", "geschiedenis", "aardrijkskunde", "samenleving-en-economie",
                 "techniek", "natuurwetenschappen", "wiskunde"],
                {"nederlands": WISSEL, "engels": WISSEL})),
            # Dit zijn de uitdagingshoofdstukken van twee gewone vakken van
            # ✨ Spark, niet de 🔭 Uitdagingshoek. Kim merkte op 14 oktober 2026
            # dat hier "Uitdagingshoek" boven stond: "de uitdagingshoek heeft
            # toch geen nederlands?" Klopt, die heeft vier eigen vakken. 
            dict(kop=SPARK + " — het uitdagingshoofdstuk",
                 uitleg=(WEG % SPARK) + " Dit is niet de 🔭 Uitdagingshoek: het gaat om het "
                        "hoofdstuk Uitdaging — alles door elkaar, dat bij het gewone vak hoort.",
                 kaarten=kaarten_van(
                     "uitdaging", SPARK,
                     ["spark-nederlands-uitdaging", "spark-geschiedenis-uitdaging"],
                     {"spark-nederlands-uitdaging": EEN,
                      "spark-geschiedenis-uitdaging": EEN})),
        ],
    ),
    dict(
        bestand="opladen-examenvragen.html",
        titel="Plakpagina — de vragen van de examens",
        sleutel="connectopia-plakpagina-examenvragen",
        voet="Bijgewerkt op 14 oktober 2026",
        intro="""<p>Kim merkte op 14 oktober 2026 dat een vraag op het examen naar een tekst
      verwees die er niet bij stond: <em>Dezelfde tekst over de schoolyard. Welke
      hoofdpunten staan erin?</em> Die tekst stond in de vraag ervoor, en op een examen
      lopen de vragen van alle hoofdstukken door elkaar.</p>
      <p>116 vragen van Engels en Frans (✨ Spark, 🚀 Boost doorstroom en
      🚀 Boost dubbele finaliteit) dragen hun tekst nu zelf. Dat gebeurt met één
      sql-bestand, zodat je die zes vragenbestanden niet opnieuw moet importeren.</p>""",
        secties=[
            dict(
                kop="Eén sql-bestand",
                uitleg="Plak het in de sql-editor van Supabase, op het project van "
                       "het oefenplatform, en klik op Run.",
                kaarten=sqlkaarten([
                    (
                        "vraagtekst",
                        "De vragen dragen hun eigen tekst",
                        "oefenplatform — sql-editor",
                        "vraag-draagt-haar-tekst.sql",
                        "Onderaan komt er een getal uit: dat hoort 116 te zijn. "
                        "Staat er een lager getal, zeg het dan, dan kijk ik welke "
                        "vraag niet meer woord voor woord dezelfde was.",
                    ),
                ]),
            ),
        ],
    ),
    dict(
        bestand="opladen-vinkjes.html",
        titel="Plakpagina — de vinkjes en de opvolging",
        sleutel="connectopia-plakpagina-vinkjes",
        voet="Bijgewerkt op 14 oktober 2026",
        intro="""<p>Een ouder meldde op 14 oktober 2026 dat haar dochters vanaf een bepaalde
      reeks geen vinkje en geen ster meer kregen. Dat lag niet aan die hoofdstukken: om
      de vinkjes te zetten vroeg de pagina élk antwoord op dat dat kind ooit gaf, en de
      databank geeft op zo'n vraag hoogstens duizend rijen terug, zonder iets te
      melden. Wie veel oefent, zit daarboven, en wat erna kwam viel buiten het
      antwoord.</p>
      <p>Het platform haalt de rijen nu blok per blok op, dus de vinkjes staan er al
      zonder dat je iets hoeft te doen. Het eerste sql-bestand laat de databank het werk
      zelf samenvatten, één rij per hoofdstuk: dat is lichter en het kan niet meer
      afgekapt worden.</p>
      <p>Het derde maakt de examenster: wie een examen van een vak drie keer zonder
      fouten aflegt, verdient de ster van dat vak. Een afgelegd examen komt in een eigen
      tabel, dus de vinkjes en de sterren van de hoofdstukken blijven onaangeroerd.</p>
      <p>Het tweede hoort bij je vraag over de opvolging: enkel de groep
      PLUSKLAS26HASSELT krijgt nog de volle fiche met de opgeloste testen, de
      opmerkingen en het werk van thuis. Bij de andere groepen blijft het bij de tabel
      met hun voortgang.</p>""",
        secties=[
            dict(
                kop="Drie sql-bestanden",
                uitleg="Plak ze een na een in de sql-editor van Supabase, op het "
                       "project van het oefenplatform, en klik telkens op Run. De eerste "
                       "twee heb je al gedaan; enkel het derde is nieuw.",
                kaarten=sqlkaarten([
                    (
                        "vinkjes",
                        "De databank vat de voortgang zelf samen",
                        "oefenplatform — sql-editor",
                        "voortgang-per-hoofdstuk.sql",
                        "Onderaan komt er één getal uit: hoeveel antwoorden het "
                        "ijverigste kind al gaf. Zeg me welk getal er staat, dan weet "
                        "ik zeker dat dit de oorzaak was.",
                    ),
                    (
                        "opvolging",
                        "Volle opvolging enkel voor PLUSKLAS26HASSELT",
                        "oefenplatform — sql-editor",
                        "volledige-opvolging.sql",
                        "Dit zet het vinkje volle opvolging op de code "
                        "PLUSKLAS26HASSELT en op geen enkele andere. Onderaan komt het "
                        "lijstje van je codes met dat vinkje erbij; verzetten kan je "
                        "daarna zelf bij Beheer, Plusklas-codes.",
                    ),
                    (
                        "examens",
                        "De examenster na drie feilloze examens",
                        "oefenplatform — sql-editor",
                        "examens.sql",
                        "Dit maakt de tabel waarin een afgelegd examen terechtkomt, los "
                        "van de voortgang. Vinkjes en sterren van de hoofdstukken blijven "
                        "dus onaangeroerd. Onderaan komt er een nul uit: er is nog geen "
                        "examen bewaard.",
                    ),
                ]),
            ),
        ],
    ),
    dict(
        bestand="opladen-uitdagingshoofdstuk.html",
        titel="Plakpagina — het uitdagingshoofdstuk van ✨ Spark",
        sleutel="connectopia-plakpagina-uitdagingshoofdstuk",
        voet="Bijgewerkt op 14 oktober 2026",
        intro="""<p>Op de vorige plakpagina stond boven deze twee bestanden
      <strong>🔭 Uitdagingshoek</strong>. Dat was fout van mij. Het gaat om het hoofdstuk
      <em>Uitdaging — alles door elkaar</em> van twee gewone vakken van ✨ Spark: het ene
      hoort bij <strong>Nederlands</strong>, het andere bij <strong>Geschiedenis</strong>.
      De uitdagingshoek heeft zijn eigen vier vakken en geen Nederlands.</p>
      <p><strong>Laadde je er al een in bij de uitdagingshoek?</strong> Ga dan eerst naar
      Beheer, Vakken, categorie 🔭 Uitdagingshoek, open het vak waar je het inlaadde, en
      verwijder daar het hoofdstuk <em>Uitdaging — alles door elkaar</em>. Daarna laad je
      het hieronder opnieuw in, bij het juiste vak.</p>""",
        secties=[
            dict(
                kop=SPARK + " — het uitdagingshoofdstuk",
                uitleg=(WEG % SPARK) + " Kies dus het vak Nederlands of Geschiedenis van "
                       "✨ Spark, niet een vak van de uitdagingshoek.",
                kaarten=kaarten_van(
                    "uitdaging", SPARK,
                    ["spark-nederlands-uitdaging", "spark-geschiedenis-uitdaging"],
                    {"spark-nederlands-uitdaging": EEN,
                     "spark-geschiedenis-uitdaging": EEN})),
        ],
    ),
    dict(
        bestand="opladen-geschiedenis-van-belgie.html",
        titel="Plakpagina — Geschiedenis van België terugzetten",
        sleutel="connectopia-plakpagina-geschiedenis-van-belgie",
        voet="Bijgewerkt op 14 oktober 2026",
        intro="""<p>Je vroeg of de vragen van <strong>Geschiedenis van België</strong> terug
      kunnen. Ze staan hier allemaal: de vier hoofdstukken met hun tachtig vragen, woord
      voor woord zoals ze gemaakt zijn.</p>
      <p><strong>Wat er kan gebeurd zijn.</strong> Een import vervangt enkel de vragen van
      een hoofdstuk met exact dezelfde titel in exact dezelfde categorie. Het bestand van
      ✨ Spark draagt de titel <em>Uitdaging — alles door elkaar</em> en de categorie
      ✨ Spark, en die bestond nog niet in dit vak. Het heeft er dus een hoofdstuk bíj
      gezet in plaats van iets te overschrijven. Dat nieuwe hoofdstuk zit ook in een
      andere categorie, en in Beheer, Vakken zie je altijd enkel de hoofdstukken van de
      categorie die je bovenaan koos: sta je in ✨ Spark, dan zie je in dit vak enkel dat
      ene hoofdstuk en lijken de vier andere weg.</p>
      <p>Toch terugzetten kan geen kwaad. Laad het bestand hieronder in met vervangen aan:
      de vier hoofdstukken krijgen opnieuw precies deze tachtig vragen, en de voortgang
      van de kinderen blijft staan.</p>""",
        secties=[
            dict(
                kop=HOEK + " — Geschiedenis van België",
                uitleg=(WEG % HOEK) + " Kies het vak Geschiedenis van België.",
                kaarten=vraagkaarten([(
                    "hoekje-geschiedenis-van-belgie",
                    "Geschiedenis van België — alle vier de hoofdstukken",
                    HOEK, "hoekje", "geschiedenis-van-belgie",
                    "Van 1830 tot de Eerste Wereldoorlog, Van de Koningskwestie tot vandaag, "
                    "Legendes, uitvinders en oude tijden, en Van de Romeinen tot de jaren "
                    "tachtig: vier hoofdstukken van twintig vragen. " + AL,
                )])),
        ],
    ),
]


def bouw(enkel=()):
    hier = pathlib.Path(__file__).parent
    sjabloon = (hier / "sjabloon.html").read_text(encoding="utf-8")
    for pag in PAGINAS:
        if enkel and pag["bestand"] not in enkel:
            continue
        stukken = []
        for nr, s in enumerate(pag["secties"], 1):
            stukken.append(f'''  <section>
    <h2><span class="nr">{nr}</span> {s["kop"]}</h2>
    <p>{s["uitleg"]}</p>
    <div class="vakken">{"".join(s["kaarten"])}</div>
  </section>
''')
        aantal = sum(len(s["kaarten"]) for s in pag["secties"])
        pagina = hier / pag["bestand"]
        pagina.write_text(sjabloon
                          .replace("<!--TITEL-->", pag["titel"])
                          .replace("<!--INTRO-->", pag["intro"])
                          .replace("<!--SECTIES-->", "\n".join(stukken))
                          .replace("<!--AANTAL-->", str(aantal))
                          .replace("<!--VOET-->", pag["voet"])
                          .replace("<!--SLEUTEL-->", pag["sleutel"]),
                          encoding="utf-8")
        print(f"{pagina.name} — {pagina.stat().st_size / 1024 / 1024:.2f} MB, "
              f"{len(pag['secties'])} secties, {aantal} kaarten")


if __name__ == "__main__":
    # Zonder argument bouwt het alle plakpagina's opnieuw; met een bestandsnaam
    # enkel die ene. Geef dus de pagina van déze ronde mee, anders schrijven de
    # oudere pagina's zich opnieuw met de inhoud van vandaag erin.
    bouw(sys.argv[1:])

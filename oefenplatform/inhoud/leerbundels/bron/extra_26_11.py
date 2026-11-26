# -*- coding: utf-8 -*-
"""Leer- en oefenbundels voor drie hoofdstukken die er nog geen hadden
(26 november 2026):

  * Start Nederlands, Begrijpend lezen — de avond van de vleermuizen
  * Start Nederlands, Begrijpend lezen — van fles tot trui
  * Spark aardrijkskunde, Werken met Geopunt

De leesteksten en woordenlijsten komen uit ../../start/bron/begrijpend_lezen.py
(zelf geschreven). De oefenbundels stellen andere vragen dan het scherm.
De Geopunt-schermafbeeldingen staan in public/examenvormen/aardrijkskunde-spark
en zijn schermafbeeldingen van Geopunt Vlaanderen (Digitaal Vlaanderen).

Eigen main, want de bestandsnamen volgen de hoofdstuktitels:

    python3 extra_26_11.py
"""
import pathlib, re, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent.parent / "start" / "bron"))
import bundel, oefenbundel
import begrijpend_lezen as bl

tabel = bundel.tabel
SPARK = "✨ Spark — 1ste en 2de middelbaar"
PUBLIC = HIER.parents[2] / "public" / "examenvormen" / "aardrijkskunde-spark"
GEO_BRON = "Schermafbeelding: Geopunt Vlaanderen, Digitaal Vlaanderen"
W, WW = "120px", "200px"


def tekst_html(tekst):
    """Leestekst: alinea's op lege regels, *woord* wordt vet."""
    alineas = [" ".join(a.split()) for a in tekst.strip().split("\n\n")]
    alineas = [re.sub(r"\*(.+?)\*", r"<strong>\1</strong>", a) for a in alineas]
    return "".join(f'<p style="margin:0 0 7px">{a}</p>' for a in alineas)


def leeskader(tekst, titel):
    return (f'<div style="font-size:10.5pt;line-height:1.55;color:#1f2a18;border:1.5px solid #2f4a22;'
            f'border-radius:14px;padding:10px 14px;margin:0 0 10px -30px;background:#fff">'
            f'<div style="font-weight:800;font-size:12pt;margin-bottom:6px">{titel}</div>{tekst_html(tekst)}</div>')


LEESAANPAK = [
    ("p", "<strong>Voor je leest:</strong> lees de titel en kijk wat de tekst al verraadt. Vraag je af wat je er al over weet."),
    ("p", "<strong>Terwijl je leest:</strong> lees alinea per alinea. Zeg na elke alinea in één zin waar ze over ging. "
          "Kom je een moeilijk woord tegen, lees dan de zin ervoor en erna: vaak legt de tekst het woord zelf uit."),
    ("p", "<strong>Na het lezen:</strong> vat de tekst samen in een paar zinnen, in je eigen woorden en zonder je mening."),
]

VRAAGSOORTEN = tabel(["Soort vraag", "Wat moet je doen?"], [
    ["Hoofdgedachte", "Zeg in één zin waar de hele tekst over gaat, niet één alinea."],
    ["Detail", "Zoek het precieze stukje op. Het antwoord staat letterlijk in de tekst."],
    ["Volgorde", "Zet de gebeurtenissen of stappen op een rij zoals ze in de tekst staan."],
    ["Betekenis", "Leid uit de zinnen rond een woord af wat het betekent."],
    ["Feit of mening", "Een feit kan je nakijken. Een mening is wat iemand ervan vindt."],
    ["Verwijswoord", "Zoek waar woorden als hij, zij, die, dat, hun of daarmee naar terugwijzen."],
    ["Besluit trekken", "Combineer wat er staat tot iets wat er niet letterlijk staat."],
], "100%")


def lees_leerbundel(titel, tekst, woorden, onder, voorbeelden, onthoud):
    return dict(
        vak="Nederlands", titel=titel, onder=onder,
        secties=[
            dict(kop="Zo lees je een tekst", blokken=LEESAANPAK),
            dict(kop="De tekst", blokken=[("kader", tekst_html(tekst))]),
            dict(kop="Moeilijke woorden", blokken=[
                ("p", "Deze woorden staan vet in de tekst. Zo begrijp je ze:"),
                ("fig", tabel(["Woord", "Betekenis"], [[w, b] for w, b in woorden], "100%")),
            ]),
            dict(kop="Soorten vragen bij een tekst", blokken=[("fig", VRAAGSOORTEN)] + voorbeelden),
        ],
        onthoud=onthoud)


BUNDELS = {}

BUNDELS["nederlands/begrijpend-lezen-de-avond-van-de-vleermuizen"] = lees_leerbundel(
    "Begrijpend lezen — de avond van de vleermuizen", bl.TEKST_1, bl.WOORDEN_1,
    "Een verhaal met veel weetjes: lezen, moeilijke woorden begrijpen en de juiste vraag herkennen.",
    [
        ("p", "<strong>Een verwijswoord opzoeken.</strong> In 'Dit toestel vertaalt <em>hun</em> geroep' wijst <em>hun</em> terug naar "
              "de vleermuizen uit de zin ervoor. Lees dus altijd een stukje terug."),
        ("p", "<strong>Een verhaal en weetjes door elkaar.</strong> Deze tekst wisselt af: stukjes over Lotte in het park, en stukjes "
              "die uitleggen hoe vleermuizen leven. Vraag je bij elke alinea af: is dit het verhaal of een weetje?"),
    ],
    ["Lees eerst de titel, dan alinea per alinea.",
     "Een moeilijk woord leg je uit met de zinnen eromheen.",
     "Een feit kan je nakijken, een mening niet.",
     "Een verwijswoord wijst terug: lees een stukje terug.",
     "Een samenvatting is kort, in je eigen woorden en zonder mening."])

BUNDELS["nederlands/begrijpend-lezen-van-fles-tot-trui"] = lees_leerbundel(
    "Begrijpend lezen — van fles tot trui", bl.TEKST_2, bl.WOORDEN_2,
    "Een uitleggende tekst over recycleren: stappen volgen, moeilijke woorden begrijpen en het doel van de schrijver zien.",
    [
        ("p", "<strong>Signaalwoorden voor volgorde.</strong> In een tekst die stappen uitlegt, helpen woorden als <em>eerst, "
              "daarna, dan, pas als</em> en <em>wat overblijft</em>. Onderstreep ze terwijl je leest."),
        ("p", "<strong>Het doel van de schrijver.</strong> Wil de schrijver je iets uitleggen (informeren), je van iets overtuigen, "
              "of je laten lachen? Een tekst kan ook twee doelen hebben: eerst uitleggen, en op het einde je aansporen om iets te doen."),
    ],
    ["Signaalwoorden (eerst, daarna, pas) tonen de volgorde.",
     "Een moeilijk woord leg je uit met de zinnen eromheen.",
     "Een feit kan je nakijken, een mening niet.",
     "Vraag je af wat de schrijver wil: informeren, overtuigen of amuseren.",
     "Een samenvatting is kort, in je eigen woorden en zonder mening."])


def geofoto(naam, breedte="100%"):
    return bundel.foto(str(PUBLIC / f"{naam}.webp"), breedte, GEO_BRON)


BUNDELS["aardrijkskunde/werken-met-geopunt-spark"] = dict(
    vak="Aardrijkskunde", niveau=SPARK, titel="Werken met Geopunt",
    onder="Het startscherm, een adres zoeken, kaartlagen, meten en een klein onderzoek.",
    secties=[
        dict(kop="Wat is Geopunt? Het startscherm", blokken=[
            ("p", "<strong>Geopunt</strong> is de gratis kaartenwebsite van de Vlaamse overheid (Digitaal Vlaanderen). "
                  "Je vindt er kaarten, luchtfoto's en gegevens over heel Vlaanderen, tot op het niveau van één huis."),
            ("p", "Geopunt toont alleen <strong>Vlaanderen</strong> in detail. Wil je iets weten over Wallonië, Europa of de wereld, "
                  "dan neem je de <strong>atlas</strong>."),
            ("fig", geofoto("geopunt-start"), "Het startscherm van Geopunt"),
            ("fig", tabel(["Waar?", "Wat?", "Waarvoor?"], [
                ["linksboven", "de zoekbalk", "een adres of plaatsnaam zoeken"],
                ["rechtsboven", "de meetlat", "een afstand of oppervlakte meten"],
                ["rechtsonder", "Lagen", "kaartlagen aanzetten, uitzetten en toevoegen"],
                ["onderaan", "de schaalbalk", "hoe lang een stukje kaart in het echt is"],
            ], "100%")),
            ("p", "Onderaan staat ook <strong>Lambert 2008</strong>: het coördinatenstelsel dat Vlaanderen gebruikt, in meters. "
                  "Zoom je in, dan verandert de schaalbalk mee: van 20 km naar bijvoorbeeld 20 m."),
        ]),
        dict(kop="Een adres zoeken", blokken=[
            ("p", "Typ straat, huisnummer en gemeente in de zoekbalk en kies het juiste adres uit de lijst. "
                  "In het <strong>linkerpaneel</strong> verschijnen dan het adres, de <strong>kadastrale informatie</strong> "
                  "(over het perceel) en de <strong>coördinaten</strong>."),
            ("fig", geofoto("geopunt-adres"), "Een gevonden adres met het linkerpaneel"),
        ]),
        dict(kop="Kaartlagen", blokken=[
            ("p", "Een kaart in Geopunt bestaat uit <strong>lagen</strong> die op elkaar liggen, zoals doorzichtige vellen. "
                  "Met <strong>+ Lagen toevoegen</strong> kies je een thema, bijvoorbeeld Hoogte, Water, Bodem of Historische kaarten. "
                  "De laag die bovenaan in de lijst staat, ligt op de kaart bovenop de andere."),
            ("fig", geofoto("geopunt-laagknoppen", "80%"), "De knopjes bij een kaartlaag"),
            ("fig", tabel(["Knopje", "Wat doet het?"], [
                ["oogje", "de laag tonen of even verbergen"],
                ["lijstjes", "de legende tonen: welke kleur wat betekent"],
                ["half rondje", "de laag doorzichtig maken met een schuifbalk"],
                ["rood vuilbakje", "de laag helemaal verwijderen"],
            ], "100%")),
            ("p", "Twee hoogtelagen lijken op elkaar. Het <strong>digitaal terreinmodel</strong> geeft de hoogte van de grond zelf. "
                  "Het <strong>digitaal oppervlaktemodel</strong> telt ook gebouwen en bomen mee."),
            ("p", "Bij Historische kaarten vind je de <strong>Ferrariskaart</strong> (1771-1778), een van de oudste nauwkeurige kaarten van onze streken. "
                  "Een <strong>luchtfoto</strong> toont dan weer wat er vandaag echt op de grond staat."),
            ("weetje", "Zie je een laag niet? Zoom dan verder in. Sommige lagen verschijnen pas als je dicht genoeg zit."),
        ]),
        dict(kop="Afstanden en oppervlakten meten", blokken=[
            ("fig", geofoto("geopunt-meten"), "Een afstand meten met de meetlat"),
            ("p", "Klik op de <strong>meetlat</strong> en kies <strong>Afstand</strong> of <strong>Oppervlakte</strong>. "
                  "Klik op de kaart om te meten, hoek per hoek bij een oppervlakte. <strong>Dubbelklik</strong> om te stoppen. "
                  "Het resultaat staat in een geel vakje."),
            ("p", "Grote oppervlakten druk je uit in <strong>hectare</strong>. 1 ha is een vierkant van 100 m op 100 m, dus 10 000 m²."),
            ("fig", tabel(["m²", "ha", "Hoe reken je?"], [
                ["10 000 m²", "1 ha", "—"],
                ["35 000 m²", "3,5 ha", "35 000 : 10 000 = 3,5"],
                ["0,8 ha", "8 000 m²", "0,8 × 10 000 = 8 000"],
            ], "100%")),
        ]),
        dict(kop="Een klein onderzoek met Geopunt", blokken=[
            ("p", "Een geografisch onderzoek volgt vijf stappen: een <strong>onderzoeksvraag</strong> stellen, een <strong>hypothese</strong> "
                  "(je vermoeden) opschrijven, de juiste <strong>kaartlagen</strong> kiezen, die lagen <strong>vergelijken</strong> en een "
                  "<strong>antwoord</strong> formuleren."),
            ("kader", "<strong>Voorbeeld.</strong> Onderzoeksvraag: stond er rond 1775 al bos op de plaats van het bos in mijn gemeente? "
                      "Hypothese: ik denk van wel. Lagen: de Ferrariskaart en een luchtfoto. Maak de bovenste laag doorzichtig en vergelijk. "
                      "Antwoord: wat je ziet, bevestigt je hypothese of niet."),
        ]),
    ],
    onthoud=[
        "Geopunt = Vlaanderen in detail. Voor de rest van de wereld: de atlas.",
        "Zoekbalk linksboven, meetlat rechtsboven, Lagen rechtsonder, schaalbalk onderaan.",
        "Oogje = verbergen, vuilbakje = verwijderen, half rondje = doorzichtig.",
        "Terreinmodel = hoogte van de grond, oppervlaktemodel = met gebouwen en bomen.",
        "Meten: klik, klik, ... dubbelklik om te stoppen.",
        "1 ha = 10 000 m².",
    ])

# ================================================================
# OEFENBUNDELS (andere vragen dan op het scherm)
# ================================================================
HOE_LEES = [
    "Lees eerst de hele tekst. Daarna mag je bij elke vraag teruglezen.",
    "Schrijf met potlood, dan kan je gerust iets uitgommen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]
OEFEN = {}

OEFEN["nederlands/oefenbundel-begrijpend-lezen-de-avond-van-de-vleermuizen"] = dict(
    vak="Nederlands", titel="Begrijpend lezen — de avond van de vleermuizen",
    onder="{aantal} oefeningen op papier bij één tekst, met een antwoordblad achteraan.", hoe=HOE_LEES,
    reeksen=[
        dict(kop="Lees de tekst", oefeningen=[("tekst", leeskader(bl.TEKST_1, "De avond van de vleermuizen"))]),
        dict(kop="Details", oefeningen=[
            ("kies", "Hoe laat stond Lotte aan de ingang van het park?", ["om negen uur", "om kwart over negen", "om half tien", "om kwart voor negen"], 1),
            ("kort", "Boven wat scheerde het donkere vlekje heen en weer?", "boven de vijver", WW),
            ("waar", "Een vleermuis heeft veren, net als een vogel.", False),
            ("waar", "Met haar vlieghuid kan een vleermuis bijzonder scherp draaien.", True),
            ("open", "Noem de drie plaatsen uit de tekst waar vleermuizen hun winterslaap houden.", "een kelder, een oude spoorwegtunnel, een spleet in een muur", 2),
        ]),
        dict(kop="Woorden", oefeningen=[
            ("rij", [("je weg vinden met de echo van je eigen geroep", "echolocatie"), ("een diepe slaap van maanden", "winterslaap"),
                     ("dieren die hun jongen melk geven", "zoogdieren")], "Welk vet gedrukt woord uit de tekst past bij de uitleg?", WW),
            ("open", "Wat betekent 'scheerde heen en weer' in de tweede alinea? Leg uit in je eigen woorden.", "Het vloog snel en laag heen en weer.", 2),
        ]),
        dict(kop="Volgorde", opdracht="Zet een 1, 2, 3 of 4 bij elke gebeurtenis, in de volgorde van de tekst.", oefeningen=[
            ("rij", [("Lotte hoort geratel.", "3"), ("De gids deelt toestellen uit.", "1"),
                     ("Lotte vraagt of ze volgend jaar opnieuw mag komen.", "4"), ("Lotte hoort eerst alleen geruis.", "2")], "", "50px"),
        ]),
        dict(kop="Verwijswoorden", oefeningen=[
            ("kies", "'Haar papa lachte.' Over wie gaat 'haar'?", ["over de gids", "over de vleermuis", "over Lotte", "over de mama"], 2),
            ("kort", "'Dit toestel vertaalt hun geroep.' Naar wie wijst 'hun'?", "naar de vleermuizen", WW),
        ]),
        dict(kop="Feit of mening", opdracht="Schrijf feit of mening.", oefeningen=[
            ("rij", [("Een vleermuis eet op één nacht honderden muggen.", "feit"), ("Vleermuizen zijn de leukste dieren van het park.", "mening"),
                     ("Alle vleermuizen in ons land zijn beschermd.", "feit"), ("Een batdetector is een prachtig toestel.", "mening")], "", "90px"),
        ]),
        dict(kop="Nadenken over de tekst", oefeningen=[
            ("kies", "Waar hang je volgens de tekst best een vleermuiskast?", ["in een koele, vochtige kelder onder het huis", "boven de vijver waar ze 's avonds jagen",
                                                                            "tegen een muur die 's avonds nog warm is", "op een donkere zolder onder de pannen"], 2),
            ("open", "Waarom is een vleermuis een handig dier in je tuin? Gebruik de tekst.", "Ze eet op één nacht honderden muggen en motten, dus er zijn minder muggen.", 2),
            ("open", "Wat moet iemand doen die een zolder verbouwt waar vleermuizen zitten?", "Rekening houden met de vleermuizen: hun verblijfplaats mag je niet verstoren.", 2),
            ("open", "Geef de alinea over echolocatie een eigen titel.", "Eigen antwoord, bijvoorbeeld: Zien met je oren.", 1),
            ("open", "Vat de tekst samen in drie zinnen.", "Eigen antwoord: vleermuizen jagen met echolocatie, houden winterslaap en zijn beschermd; geen mening.", 3),
        ]),
    ])

OEFEN["nederlands/oefenbundel-begrijpend-lezen-van-fles-tot-trui"] = dict(
    vak="Nederlands", titel="Begrijpend lezen — van fles tot trui",
    onder="{aantal} oefeningen op papier bij één tekst, met een antwoordblad achteraan.", hoe=HOE_LEES,
    reeksen=[
        dict(kop="Lees de tekst", oefeningen=[("tekst", leeskader(bl.TEKST_2, "Van fles tot trui"))]),
        dict(kop="Details", oefeningen=[
            ("kies", "Waarmee worden de lichte folies opzij geblazen?", ["met magneten", "met luchtstromen", "met water", "met licht"], 1),
            ("kort", "Waaraan herkennen toestellen uit welke soort plastic een stuk gemaakt is?", "aan het teruggekaatste licht", WW),
            ("waar", "Vlokken nemen meer plaats in dan dezelfde flessen in één stuk.", False),
            ("waar", "Van de vezels kan men ook de vulling van een slaapzak maken.", True),
            ("open", "Je wil drie fleecetruien maken. Hoeveel flessen heb je ongeveer nodig? Schrijf je berekening op.", "3 × 20 = 60 flessen", 2),
        ]),
        dict(kop="Volgorde", opdracht="Zet een 1, 2, 3, 4 of 5 bij elke stap, in de volgorde van de tekst.", oefeningen=[
            ("rij", [("versnipperen tot vlokken", "3"), ("sorteren per soort plastic", "1"), ("stof weven", "5"),
                     ("wassen", "2"), ("smelten en door gaatjes duwen", "4")], "", "50px"),
        ]),
        dict(kop="Woorden en verwijswoorden", oefeningen=[
            ("open", "'... maar het zakt wel een trapje.' Wat bedoelt de schrijver met 'een trapje zakken'?", "Het materiaal wordt minder goed, minder waard.", 2),
            ("kies", "'Daarmee is het verhaal van dat flesje niet gedaan.' Waarnaar verwijst 'daarmee'?",
             ["naar de ophaalwagen die het afval meeneemt", "naar de fleecetrui uit gerecycleerd plastic", "naar het flesje leegdrinken en in de blauwe zak gooien", "naar het sorteercentrum waar alles toekomt"], 2),
        ]),
        dict(kop="Feit of mening", opdracht="Schrijf feit of mening.", oefeningen=[
            ("rij", [("Een drankfles is bijna altijd van pet.", "feit"), ("Recycleren is saai werk.", "mening"),
                     ("Eén verkeerd gevulde zak kan een hele partij bederven.", "feit"), ("Een fleecetrui is de mooiste trui die er is.", "mening")], "", "90px"),
        ]),
        dict(kop="Nadenken over de tekst", oefeningen=[
            ("open", "Noem vier dingen die jij volgens de tekst kan doen.", "de fles platduwen, de dop erop laten, vet of saus eruit spoelen, geen zak in een zak steken", 3),
            ("kies", "Wat wil de schrijver vooral?",
             ["je doen lachen met grappige weetjes over afval",
              "uitleggen hoe recycleren werkt en je aansporen om goed te sorteren",
              "je overtuigen om een fleecetrui te kopen",
              "vertellen over iemand die in een sorteercentrum werkt en wat die meemaakt"], 1),
            ("open", "Waarom staat recycleren pas op de derde plaats? Leg uit met de tekst.", "Plastic wordt bij elke keer smelten zwakker (downcycling); beter is een fles vermijden of opnieuw vullen.", 2),
            ("open", "Vat de tekst samen in drie zinnen.", "Eigen antwoord: de weg van fles tot trui, waarom het niet eindeloos kan, wat jij kan doen; geen mening.", 3),
        ]),
    ])

HOE_GEO = [
    "Je kan deze bundel zonder computer maken. Bij de laatste reeks heb je wel Geopunt nodig.",
    "Schrijf bij een rekenvraag altijd je tussenstappen op.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFEN["aardrijkskunde/oefenbundel-werken-met-geopunt-spark"] = dict(
    vak="Aardrijkskunde", niveau=SPARK, titel="Werken met Geopunt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE_GEO,
    reeksen=[
        dict(kop="Het scherm en de knoppen", oefeningen=[
            ("rij", [("de zoekbalk", "linksboven"), ("de meetlat", "rechtsboven"), ("Lagen", "rechtsonder"), ("de schaalbalk", "onderaan")],
             "Waar staat dit op het startscherm?", W),
            ("rij", [("de laag even verbergen", "oogje"), ("de laag doorzichtig maken", "half rondje"),
                     ("tonen welke kleur wat betekent", "lijstjes (legende)"), ("de laag helemaal weghalen", "vuilbakje")], "Welk knopje gebruik je?", W),
            ("kies", "Je zoomt flink in. Wat gebeurt er met de schaalbalk?", ["hij verdwijnt tot je weer uitzoomt", "hij blijft altijd op 20 km staan",
                                                                            "hij toont een kortere afstand, bv. 20 m", "hij schuift naar de andere kant van het scherm"], 2),
        ]),
        dict(kop="Kaartlagen", oefeningen=[
            ("kies", "Je wil weten hoe hoog de daken in je straat zijn. Welke laag kies je?", ["digitaal terreinmodel", "digitaal oppervlaktemodel", "Ferrariskaart", "kadastrale kaart"], 1),
            ("kies", "In welk thema zoek je de overstromingsgevoelige gebieden?", ["Hoogte", "Bodem", "Historische kaarten", "Water"], 3),
            ("waar", "Met het oogje verwijder je een laag voorgoed.", False),
            ("waar", "Het digitaal terreinmodel toont de hoogte van de grond zonder gebouwen en bomen.", True),
            ("waar", "Een laag die onderaan in de lijst staat, ligt op de kaart bovenop de andere.", False),
            ("waar", "Lambert 2008 geeft coördinaten in meters.", True),
        ]),
        dict(kop="Geopunt of atlas?", opdracht="Schrijf Geopunt of atlas.", oefeningen=[
            ("rij", [("de oppervlakte van de voetbalvelden in jouw gemeente", "Geopunt"), ("de hoofdsteden van Afrika", "atlas"),
                     ("hoe jouw straat er rond 1775 uitzag", "Geopunt"), ("de hoogste bergen van Europa", "atlas")], "", W),
        ]),
        dict(kop="Meten en rekenen", opdracht="Schrijf je tussenstappen op.", oefeningen=[
            ("open", "Hoeveel hectare is 30 000 m²?", "30 000 : 10 000 = 3 ha", 2),
            ("open", "Hoeveel m² is 4,5 ha?", "4,5 × 10 000 = 45 000 m²", 2),
            ("open", "Hoeveel hectare is 7 500 m²?", "7 500 : 10 000 = 0,75 ha", 2),
            ("open", "Je meet een fietsroute in drie stukken: 1 250 m, 800 m en 450 m. Hoeveel km is de route?", "1 250 + 800 + 450 = 2 500 m = 2,5 km", 2),
            ("open", "Een sportpark is 200 m lang en 150 m breed. Hoeveel hectare is dat?", "200 × 150 = 30 000 m²; 30 000 : 10 000 = 3 ha", 2),
        ]),
        dict(kop="Stappen", opdracht="Zet een 1, 2, 3 of 4 bij elke stap om een afstand te meten.", oefeningen=[
            ("rij", [("Dubbelklik om te stoppen.", "3"), ("Klik op de meetlat en kies Afstand.", "1"),
                     ("Lees het resultaat in het gele vakje.", "4"), ("Klik op het beginpunt en daarna op elk volgend punt.", "2")], "", "50px"),
        ]),
        dict(kop="Zelf onderzoeken met Geopunt", oefeningen=[
            ("open", "Onderzoeksvraag: stond er rond 1775 al bos op de plaats van een bos bij jou in de buurt? Schrijf je hypothese op.", "Eigen antwoord, bv. Ik denk dat er toen al bos stond.", 2),
            ("open", "Welke twee lagen leg je over elkaar om die vraag te beantwoorden? En wat doe je met de bovenste laag?", "de Ferrariskaart en een luchtfoto; de bovenste laag doorzichtig maken", 2),
            ("open", "Zoek je school op in Geopunt en meet de afstand in rechte lijn tot je huis. Schrijf de afstand op.", "Eigen antwoord, met eenheid (m of km).", 1),
        ]),
    ])


def maak():
    for soort, lijst, maker, basis in (
        ("leerbundel", BUNDELS, bundel, HIER.parent),
        ("oefenbundel", OEFEN, oefenbundel, HIER.parent.parent / "oefenbundels"),
    ):
        for pad, b in lijst.items():
            tijdelijk = pad.replace("/", "-")
            maker.schrijf(b, tijdelijk)
            subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True)
            doel = basis / f"{pad}.pdf"
            doel.parent.mkdir(parents=True, exist_ok=True)
            doel.write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
            print("  ", doel.relative_to(HIER.parent.parent))


if __name__ == "__main__":
    maak()

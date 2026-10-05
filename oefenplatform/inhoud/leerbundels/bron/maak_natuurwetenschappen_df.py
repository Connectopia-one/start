# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche natuurwetenschappen van de 2de graad dubbele
finaliteit, geldig vanaf 1 januari 2027. Eén fiche voor bedrijf en organisatie
en voor maatschappij en welzijn. Ze weegt zelf: biologie 25 %, chemie 25 %,
fysica 40 %, en wetenschappelijk onderzoek en STEM 10 %.

Dertien bundels, één per thema van `boost-dubbele-finaliteit/natuurwetenschappen.json`.
Zes bundels komen zo goed als ongewijzigd van 🚀 Boost doorstroom, want die
leerstof is dezelfde. Zes zijn hier opnieuw samengesteld uit de stukken van
doorstroom die blijven gelden, aangevuld met wat deze fiche extra vraagt. En
één is helemaal nieuw: de fiche zet de prikkels, de hormonen en de klieren
samen onder één kop, "Biologische feedback", waar doorstroom ze over drie
thema's spreidt.

Wat hier bewust niet in staat, omdat de fiche het niet vraagt: arbeid, de
formules van de kinetische, de gravitationele en de elastische energie, de
specifieke warmtecapaciteit, de latente warmte, het warmtetransport, de vrije
val, de verticale worp, de veerconstante, de zwaarteveldsterkte, de
hydrostatische druk, het beginsel van Pascal, de gaswetten met de kelvinschaal,
en de indeling van het leven in domeinen en rijken. Achteraan zegt de fiche
uitdrukkelijk welke vier formules je moet kennen: P = |ΔE| / Δt, het
rendement, p = F / A en R = U / I. Onderaan dit bestand loopt er een controle
over alle bundels die daarop toekijkt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag.
`python3 dekking.py ../../boost-dubbele-finaliteit/natuurwetenschappen.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import maak_natuurwetenschappen_boost as doorstroom

VAK = "Natuurwetenschappen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
tabel = bundel.tabel

# De bundels die van doorstroom meekomen: (sleutel daar, sleutel hier, titel
# hier). Staat er None, dan blijven de sleutel en de titel dezelfde.
MEE = [
    ("biodiversiteit-en-micro-organismen",
     "micro-organismen-het-microbioom-en-bewaring",
     "Micro-organismen, het microbioom en bewaring"),
    ("voortplanting-en-de-hormonale-regeling", None, None),
    ("mengsels-en-zuivere-stoffen", None, None),
    ("enkelvoudige-en-samengestelde-stoffen-en-chemische-reacties",
     "chemische-formules-en-chemische-reacties",
     "Chemische formules en chemische reacties"),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", None, None),
    ("elektriciteit-en-de-wet-van-ohm",
     "elektriciteit-de-wet-van-ohm-en-veiligheid",
     "Elektriciteit, de wet van Ohm en veiligheid"),
    ("veilig-werken-meten-en-levensreddend-handelen", None, None),
    ("grootheden-eenheden-en-wetenschappelijk-onderzoek", None, None),
]

# Woorden die bij de doorstroomfiche horen en niet bij deze.
VERBODEN = [
    "arbeid",
    "valversnelling",
    "vrije val",
    "verticale worp",
    "veerconstante",
    "zwaarteveldsterkte",
    "warmtecapaciteit",
    "latente warmte",
    "merkbare warmte",
    "calorimeter",
    "joulevat",
    "warmtetransport",
    "convectie",
    "hydrostatisch",
    "beginsel van pascal",
    "kelvin",
    "isotherm",
    "isochoor",
    "isobaar",
    "ideaal gas",
    "ideale gas",
    "driedomeinen",
    "vijfrijken",
    "prokaryo",
    "eukaryo",
    "relatieve atoommassa",
    "absolute massa",
    "atoommassa-eenheid",
    "uitgebreide fiche",
    "basisfiche",
    "de vakfiche",
    "de fiche",
    "deze fiche",
    "de leerstof",
]


def tekst_van(blok) -> str:
    return " ".join(str(d) for d in blok[1:])


def _bron(kort: str) -> dict:
    sleutel = kort + OUD
    if sleutel not in doorstroom.BUNDELS:
        raise SystemExit(f"Onbekende doorstroombundel: {sleutel}")
    return doorstroom.BUNDELS[sleutel]


def sectie(kort: str, kop: str, nieuwe_kop: str = None, zonder: tuple = ()) -> dict:
    """Een hele sectie uit een doorstroombundel, los gekopieerd.

    `zonder` zijn haakjes: elk blok waarin zo'n stukje tekst staat, valt weg.
    Elk haakje moet precies één blok raken, anders stopt het script.
    """
    raak = [s for s in _bron(kort)["secties"] if s["kop"] == kop]
    if len(raak) != 1:
        raise SystemExit(f"{kort}: {len(raak)} secties heten {kop!r}, verwacht 1")
    uit = copy.deepcopy(raak[0])
    for haak in zonder:
        treffers = [i for i, b in enumerate(uit["blokken"]) if haak in tekst_van(b)]
        if len(treffers) != 1:
            raise SystemExit(f"{kort} §{kop}: {len(treffers)} blokken met {haak!r}, verwacht 1")
        uit["blokken"].pop(treffers[0])
    if nieuwe_kop:
        uit["kop"] = nieuwe_kop
    return uit


def blok(kort: str, kop: str, haak: str):
    """Eén blok uit een sectie van een doorstroombundel."""
    raak = [b for b in sectie(kort, kop)["blokken"] if haak in tekst_van(b)]
    if len(raak) != 1:
        raise SystemExit(f"{kort} §{kop}: {len(raak)} blokken met {haak!r}, verwacht 1")
    return raak[0]


# ─────────────────────────────────────────────────────────────
# De ingrepen op de bundels die meekomen.
# ─────────────────────────────────────────────────────────────

# De bouw van de micro-organismen en de weg waarlangs ze binnenkomen. Die
# vervangt bij deze fiche het hele stuk over de indeling van het leven.
MICRO_BOUW = dict(
    kop="De bouw van bacteriën, virussen, gisten en schimmels",
    blokken=[
        ("p", "Je moet bacteriën, virussen, schimmels en gisten kunnen onderscheiden op "
              "<strong>vier punten</strong>: hun <strong>bouw</strong>, hun "
              "<strong>vermenigvuldigingswijze</strong>, hun <strong>voedingswijze</strong> en de "
              "<strong>plaatsen waar ze voorkomen</strong>. En om ze op een afbeelding te herkennen."),
        ("p", tabel(
            ["", "Bouw", "Vermeerdert zich door"],
            [["bacterie", "eencellig, geen kern, wel een celwand", "celsplitsing"],
             ["gist", "eencellig, met een kern", "knopvorming"],
             ["schimmel", "meercellig, schimmeldraden", "sporen, aseksueel of seksueel"],
             ["virus", "geen cel, erfelijk materiaal in een eiwitmantel", "een gastheercel"]],
        )),
        ("p", "Onder de microscoop zie je aan de <strong>vorm</strong> van een bacterie al veel. Ze "
              "zijn <strong>bolvormig, staafvormig, kommavormig of spiraalvormig</strong>, en die "
              "vormen hebben eigen namen: <strong>kokken</strong>, <strong>bacillen</strong>, "
              "<strong>vibrionen</strong> en <strong>spirillen</strong>."),
        ("p", "Bij een bacterie kan je deze onderdelen terugvinden: het <strong>DNA</strong> dat "
              "vrij in de cel ligt, een <strong>celmembraan</strong> met daarrond een "
              "<strong>celwand</strong>, en daarbij vaak nog een <strong>slijmlaag</strong>, een "
              "<strong>plasmide</strong> (een extra ringetje DNA), <strong>pili</strong> en een "
              "<strong>zweephaar</strong> om zich te bewegen. Een <strong>echte kern met een "
              "kernmembraan heeft ze niet</strong>."),
        ("p", "Een organisme dat <strong>eencellig is, geen kern heeft en zich door celsplitsing "
              "vermeerdert, is dus een bacterie</strong>. Een <strong>gist is ook eencellig maar "
              "heeft wél een kern</strong>, een <strong>schimmel is meercellig</strong> en bestaat "
              "uit <strong>schimmeldraden</strong>, en een virus is geen cel."),
        ("p", "Een <strong>virus</strong> bestaat uit <strong>erfelijk materiaal</strong> in een "
              "<strong>eiwitmantel of kapsel</strong>, bij sommige soorten met een "
              "<strong>enveloppe</strong> en <strong>spikes</strong> errond. Virussen zijn "
              "<strong>gastheerafhankelijk</strong>: ze vermeerderen zich alleen binnen in een "
              "levende cel. Naar hun gastheer deelt men ze in <strong>dierlijke virussen, "
              "plantaardige virussen en bacteriofagen</strong>. Een "
              "<strong>bacteriofaag</strong> gebruikt bacteriën als gastheer."),
        ("p", "De <strong>voedingswijze</strong> zegt waar een micro-organisme zijn energie haalt. "
              "<strong>Autotroof</strong> maakt zijn energierijke stoffen zelf, "
              "<strong>heterotroof</strong> haalt ze uit andere organismen. "
              "<strong>Aeroob</strong> heeft zuurstof nodig, <strong>anaeroob</strong> niet. En "
              "de <strong>plaatsen van voorkomen</strong> gaan van je eigen microbioom tot de "
              "bodem, het water en de lucht van een heel ecosysteem."),
        ("p", "Micro-organismen dringen je lichaam binnen <strong>langs de mond, de luchtwegen, "
              "de ogen en wondjes in de huid</strong>. De gave huid is een goede barrière, de "
              "openingen van je lichaam niet. Daarom sluiten handen wassen, hoesten in je "
              "elleboog, en een wondje afdekken net die wegen af."),
        ("weetje", "Bacteriofagen worden onderzocht als middel tegen bacteriën die niet meer op "
                   "antibiotica reageren: je zet dan het ene micro-organisme in tegen het andere."),
    ],
)

# De elektronenconfiguratie en het stipmodel. Die vervangen bij deze fiche het
# stuk over de relatieve en de absolute atoommassa.
ATOOM_ELEKTRONEN = dict(
    kop="De elektronen op hun plaats",
    blokken=[
        ("p", "Uit de <strong>symbolische voorstelling van een atoom</strong>, met zijn "
              "<strong>massagetal A</strong> linksboven en zijn <strong>atoomnummer Z</strong> "
              "linksonder het symbool, lees je af <strong>hoeveel protonen, neutronen en "
              "elektronen</strong> het atoom heeft: Z protonen, in een neutraal atoom ook Z "
              "elektronen, en A min Z neutronen. Het atoomnummer zegt je ook "
              "<strong>waar in het PSE</strong> het atoom staat."),
        ("p", "Omgekeerd werkt het ook: krijg je het <strong>aantal van de elementaire "
              "deeltjes</strong>, dan kan je de symbolische voorstelling opschrijven en het "
              "element in het periodiek systeem terugvinden."),
        ("p", "De <strong>elektronenconfiguratie volgens Bohr</strong> zegt hoeveel elektronen er "
              "op elk <strong>energieniveau</strong> zitten. Je vult van binnen naar buiten: "
              "<strong>2</strong> in de eerste schil, dan <strong>8</strong>, dan <strong>8</strong>. "
              "Voor de <strong>eerste achttien elementen</strong> moet je dat kunnen noteren."),
        ("p", tabel(
            ["Atoom", "Atoomnummer", "Configuratie"],
            [["waterstof H", "1", "1"],
             ["zuurstof O", "8", "2, 6"],
             ["natrium Na", "11", "2, 8, 1"],
             ["zwavel S", "16", "2, 8, 6"],
             ["argon Ar", "18", "2, 8, 8"]],
        )),
        ("kader", "Een <strong>zwavelatoom met atoomnummer 16</strong> krijgt dus "
                  "<strong>2, 8, 6</strong>: eerst twee, dan acht, en de zes die overblijven in de "
                  "derde schil. Tel altijd na of je uitkomt op het atoomnummer."),
        ("p", "In het <strong>elektron-stipmodel</strong> zet je <strong>alleen de elektronen van "
              "de buitenste schil</strong> als stipjes rond het symbool van het element. Bij "
              "zuurstof zijn dat er zes, bij natrium één. De binnenste schillen laat je weg, want "
              "<strong>de buitenste bepaalt hoe het atoom reageert</strong>."),
        ("p", "Met die kennis van het PSE, de bouw van het atoom en de elektronenconfiguratie los "
              "je oefeningen op: hoeveel deeltjes zitten erin, welk element is het, en wat doet "
              "het liever, elektronen afstaan of opnemen?"),
    ],
)

INGREPEN = [
    # (sleutel hier, soort, waar, inhoud)
    ("micro-organismen-het-microbioom-en-bewaring", "schrap-sectie", "Het leven indelen", None),
    ("micro-organismen-het-microbioom-en-bewaring", "sectie-vooraan", None, MICRO_BOUW),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", "schrap-sectie",
     "Relatieve en absolute massa", None),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", "sectie-achteraan", None, ATOOM_ELEKTRONEN),
    # De calorimeter staat niet in de instrumentenlijst van deze fiche.
    ("veilig-werken-meten-en-levensreddend-handelen", "vervang-blok", "Calorimeter", [
        ("p", tabel(["Instrument", "Meet"], [
            ["Balans", "massa"],
            ["Chronometer", "tijd"],
            ["Thermometer", "temperatuur"],
            ["Dynamometer", "kracht"],
            ["pH-meter", "zuurtegraad"],
            ["Manometer", "druk"],
            ["Multimeter", "stroomsterkte, spanning en weerstand"],
            ["Meetlint", "lengte"],
        ])),
    ]),
    # Deze fiche zet bij temperatuur de graad Celsius, niet de kelvin.
    ("grootheden-eenheden-en-wetenschappelijk-onderzoek", "vervang-blok", "SI-eenheid", [
        ("p", tabel(["Grootheid", "SI-eenheid", "Grootheid", "Eenheid"], [
            ["lengte", "meter", "kracht", "newton"],
            ["massa", "kilogram", "energie", "joule"],
            ["tijd", "seconde", "vermogen", "watt"],
            ["temperatuur", "graden Celsius", "druk", "pascal"],
        ])),
    ]),
]

ONDERTITELS = {
    "micro-organismen-het-microbioom-en-bewaring":
        "De bouw van bacteriën, virussen, gisten en schimmels, wat ze voor ons doen, en hoe je je "
        "ertegen beschermt.",
    "chemische-formules-en-chemische-reacties":
        "Symbolen en formules, de stoffen die je moet kennen, en hoe je een reactievergelijking "
        "kloppend maakt.",
    "de-bouw-van-het-atoom-en-het-periodiek-systeem":
        "De deeltjes in een atoom, het atoomnummer en het massagetal, de elektronenconfiguratie, "
        "en wat je uit het PSE kan aflezen.",
    "elektriciteit-de-wet-van-ohm-en-veiligheid":
        "De wet van Ohm, geleiders en isolatoren, het Joule-effect, en de risico's en de "
        "beveiliging van een installatie.",
}

# De onthoudlijstjes die moeten mee veranderen.
ONTHOUD = {
    "micro-organismen-het-microbioom-en-bewaring": [
        "Bacterie: eencellig, geen kern, wel een celwand, vermeerdert zich door celsplitsing.",
        "Gist: eencellig met een kern, door knopvorming. Schimmel: meercellig, schimmeldraden.",
        "Bacterievormen: kokken bolvormig, bacillen staafvormig, vibrionen kommavormig, spirillen spiraalvormig.",
        "Een bacterie kan ook een slijmlaag, een plasmide, pili en een zweephaar hebben.",
        "Een virus is erfelijk materiaal in een eiwitmantel, soms met enveloppe en spikes.",
        "Virussen naar gastheer: dierlijke, plantaardige en bacteriofagen. Ze vermeerderen zich alleen in een gastheercel.",
        "Autotroof maakt zijn stoffen zelf, heterotroof niet; aeroob heeft zuurstof nodig, anaeroob niet.",
        "Micro-organismen komen binnen langs de mond, de luchtwegen, de ogen en wondjes in de huid.",
        "Een antibioticum werkt op bacteriën, niet op virussen; tegen schimmels gebruik je een antimycoticum.",
        "Antibioticaresistentie: de bacteriën die het middel overleven, vermeerderen zich verder.",
        "Een vaccin laat je afweersysteem oefenen zonder dat je eerst ziek wordt.",
        "Bewaren: koelen, drogen, roken, pasteuriseren, steriliseren, opleggen in zuur, alcohol of suiker, pekelen, uv.",
        "Je darmmicrobioom en je huidmicrobioom helpen je; overmatige hygiëne en antibiotica verstoren ze.",
    ],
    "de-bouw-van-het-atoom-en-het-periodiek-systeem": [
        "In de kern zitten protonen en neutronen, daarrond de elektronen.",
        "Het atoomnummer Z is het aantal protonen; in een neutraal atoom ook het aantal elektronen.",
        "Massagetal A min atoomnummer Z is het aantal neutronen.",
        "Isotopen zijn atomen van hetzelfde element met een ander aantal neutronen.",
        "Een ion is een atoom dat elektronen afgestaan (positief) of opgenomen (negatief) heeft.",
        "De elektronenconfiguratie volgens Bohr vult van binnen naar buiten: 2, dan 8, dan 8.",
        "Zwavel met atoomnummer 16 wordt 2, 8, 6.",
        "In het elektron-stipmodel zet je alleen de buitenste schil rond het symbool.",
        "Een periode is een rij, een groep een kolom; het periodenummer geeft het aantal schillen.",
        "Elementen in dezelfde groep hebben evenveel valentie-elektronen en reageren daarom gelijk.",
        "Een volle buitenste schil is de stabiele edelgasconfiguratie.",
    ],
}


# ─────────────────────────────────────────────────────────────
# De bundels die hier opnieuw samengesteld worden.
# ─────────────────────────────────────────────────────────────
HERBOUW = {}

HERBOUW["energieomzettingen-vermogen-en-rendement"] = dict(
    vak=VAK, niveau=DF, titel="Energieomzettingen, vermogen en rendement",
    onder="De energievormen en hun eenheden, de energiebalans met haar nuttige en ongewenste "
          "energie, en hoe je vermogen en rendement berekent.",
    secties=[
        dict(kop="De energievormen en hun eenheden", blokken=[
            ("p", "Er staan acht <strong>soorten energie</strong> op je lijst: de "
                  "<strong>gravitationele</strong> energie (door de hoogte van een voorwerp), de "
                  "<strong>elastische</strong> energie (in een uitgerekte veer of katapult), de "
                  "<strong>kinetische</strong> energie (doordat iets beweegt), de "
                  "<strong>chemische</strong> energie (in brandstof en voeding), de "
                  "<strong>thermische</strong> energie of <strong>warmte</strong>, de "
                  "<strong>stralingsenergie</strong> (van de zon of een lamp), de "
                  "<strong>kernenergie</strong> en de <strong>elektrische</strong> energie."),
            ("p", "De energie die een voorwerp heeft <strong>door zijn hoogte boven de "
                  "grond</strong> is de <strong>gravitationele potentiële energie</strong>. Hoe "
                  "hoger en hoe zwaarder, hoe meer. De energie die een voorwerp heeft "
                  "<strong>omdat het beweegt</strong>, is de <strong>kinetische energie</strong>. "
                  "Rek je een katapult uit, dan sla je <strong>elastische energie</strong> op."),
            ("p", "Energie meet je in <strong>joule</strong>, en voor grotere hoeveelheden in "
                  "<strong>kilojoule</strong>, <strong>kilowattuur</strong> en "
                  "<strong>kilocalorie</strong>. Een <strong>kilowattuur</strong> is duizend watt "
                  "gedurende één uur, dus <strong>3 600 000 joule</strong>. Daarom rekent je "
                  "elektriciteitsfactuur in kilowattuur en niet in joule."),
            ("kader", "Een <strong>kilowattuur is energie, geen vermogen</strong>. De watt is het "
                      "vermogen, de wattuur en de joule zijn de energie. Dat verschil is op het "
                      "examen al vaak de hele vraag."),
        ]),
        dict(kop="Open, gesloten en geïsoleerd", blokken=[
            ("p", "Of energie een systeem in of uit kan, hangt af van het soort systeem:"),
            ("p", tabel(
                ["Systeem", "Wisselt uit met de omgeving"],
                [["open", "energie én materie"],
                 ["gesloten", "alleen energie, geen materie"],
                 ["geïsoleerd", "niets van de twee"]],
            )),
            ("p", "Een <strong>open kookpot</strong> is een open systeem: er gaat warmte weg en er "
                  "verdwijnt ook waterdamp. Doe je het deksel erop, dan heb je bijna een "
                  "<strong>gesloten</strong> systeem. Een goede thermosfles komt in de buurt van "
                  "een <strong>geïsoleerd</strong> systeem, maar helemaal lukt dat nooit."),
        ]),
        dict(kop="Energieomzettingen en de energiebalans", blokken=[
            ("p", "De <strong>wet van behoud van energie</strong> zegt dat energie "
                  "<strong>niet kan verdwijnen</strong>, enkel <strong>van vorm kan "
                  "veranderen</strong>. Op die wet steunt de <strong>energiebalans</strong>: alles "
                  "wat erin gaat, komt er ook weer uit, al is het in een andere vorm."),
            ("p", tabel(
                ["Waar", "Welke omzetting"],
                [["een vallende steen", "gravitationele energie wordt kinetische energie"],
                 ["een lamp op het net", "elektrische energie wordt stralingsenergie en warmte"],
                 ["een gasfornuis", "chemische energie wordt thermische energie"],
                 ["een zonnepaneel", "stralingsenergie wordt elektrische energie"],
                 ["een windmolen", "kinetische energie van de wind wordt elektrische energie"],
                 ["een remmende fiets", "kinetische energie wordt warmte in de rem"]],
            )),
            ("p", "Een <strong>stroomdiagram</strong> toont hoe de energie bij een omzetting over "
                  "de vormen verdeeld wordt: één brede pijl gaat erin, en er komen smallere pijlen "
                  "uit, één per vorm."),
            ("p", "Bij elke omzetting in het dagelijkse leven gaat <strong>een deel van de "
                  "bruikbare energie naar een minder bruikbare of ongewenste vorm, meestal "
                  "warmte</strong>. Dat heet <strong>energiedissipatie</strong>. Wat je wél wou, "
                  "is de <strong>nuttige energie</strong>; de rest is de <strong>niet-nuttige of "
                  "ongewenste energie</strong>."),
            ("p", "Bij een <strong>gloeilamp</strong> is het licht de nuttige energie en de warmte "
                  "de ongewenste: het <strong>grootste deel komt als warmte vrij</strong>, dus is "
                  "haar rendement voor licht laag. Een <strong>ledlamp</strong> geeft bij hetzelfde "
                  "licht veel minder warmte. Een rem die warm wordt op een afdaling is net "
                  "hetzelfde verhaal: de wrijving zet de energie van de bewegende fiets om in "
                  "warmte."),
            ("p", "Omdat die ongewenste warmte in het systeem blijft, heeft een toestel "
                  "<strong>koeling of isolatie</strong> nodig. Een <strong>computer</strong> moet "
                  "gekoeld worden omdat <strong>een deel van de elektrische energie warmte "
                  "wordt</strong>; zonder ventilator loopt de temperatuur te hoog op. Laat je de "
                  "deur van een <strong>koelkast</strong> in een afgesloten keuken openstaan, dan "
                  "<strong>stijgt</strong> de temperatuur in die keuken: de koelkast verplaatst "
                  "warmte en de motor zet er zelf nog elektrische energie in warmte om."),
            ("weetje", "Daarom bestaat er geen koelkast die een kamer koelt. Een airco kan dat "
                       "alleen omdat ze haar warmte aan de <em>buitenkant</em> van het huis kwijt "
                       "kan; de keuken met een open koelkast heeft die buitenkant niet."),
        ]),
        sectie("arbeid-energie-vermogen-en-rendement", "Vermogen en rendement"),
    ],
    onthoud=[
        "Soorten energie: gravitationele, elastische, kinetische, chemische, thermische, stralings-, kern- en elektrische energie.",
        "De energie door de hoogte is de gravitationele potentiële energie; door de beweging de kinetische.",
        "Energie meet je in joule, kilojoule, kilowattuur en kilocalorie. Eén kilowattuur is 3 600 000 joule.",
        "Een kilowattuur is energie, een watt is vermogen.",
        "Open systeem: energie en materie. Gesloten: alleen energie. Geïsoleerd: niets van de twee.",
        "Energie kan niet verdwijnen, enkel van vorm veranderen. Daarop steunt de energiebalans.",
        "Energiedissipatie: een deel van de energie gaat naar een ongewenste vorm, meestal warmte.",
        "Nuttige energie is wat je wou, de rest is de ongewenste energie.",
        "Een stroomdiagram toont hoe de energie bij een omzetting over de vormen verdeeld wordt.",
        "Koeling en isolatie zijn nodig omdat de ongewenste warmte anders in het systeem blijft.",
        "Vermogen = omgezette energie gedeeld door de tijd, in watt: P = |ΔE| / Δt.",
        "Rendement = nuttige energie gedeeld door totale energie. Honderd procent bestaat niet.",
    ],
)

HERBOUW["warmte-faseovergangen-en-inwendige-energie"] = dict(
    vak=VAK, niveau=DF, titel="Warmte, faseovergangen en inwendige energie",
    onder="Het verschil tussen warmte en temperatuur, de warmtebalans, de inwendige energie, en de "
          "faseovergangen met hun toepassingen.",
    secties=[
        dict(kop="Warmte en temperatuur", blokken=[
            blok("warmte-en-faseovergangen", "Temperatuur en warmte", "zegt hoe warm iets is"),
            ("p", "<strong>Warmte</strong> is de energie die van het ene systeem naar het andere "
                  "gaat <strong>door een verschil in temperatuur</strong>. Zonder "
                  "temperatuurverschil gaat er geen warmte over. Warmte zit dus niet in een "
                  "voorwerp; ze is energie die <strong>onderweg</strong> is. Daarom meet je "
                  "<strong>temperatuur in graden Celsius</strong> en <strong>warmte in "
                  "joule</strong>, en zijn het <strong>geen twee woorden voor hetzelfde</strong>."),
            blok("warmte-en-faseovergangen", "Temperatuur en warmte", "Koude bestaat niet"),
            ("p", "Een voorwerp met een <strong>hogere temperatuur bevat niet automatisch meer "
                  "warmte</strong>: dat hangt ook af van de massa en van de stof. Een kopje thee "
                  "van 80 graden geeft veel minder warmte af dan een vol bad van 40 graden. Een "
                  "<strong>thermometer</strong> meet dan ook de <strong>temperatuur</strong>, niet "
                  "de warmte."),
            ("p", "In een concrete situatie moet je kunnen zeggen <strong>wie warmte afgeeft en "
                  "wie ze opneemt</strong>. Leg je een <strong>warm blok metaal in koud "
                  "water</strong>, dan <strong>geeft het blok warmte af en neemt het water ze "
                  "op</strong>, tot ze dezelfde temperatuur hebben. Roer je <strong>koude melk in "
                  "warme koffie</strong>, dan <strong>neemt de melk op wat de koffie afgeeft</strong>."),
            ("p", "Dat laatste is de <strong>warmtebalans</strong>, en die is niets anders dan de "
                  "<strong>wet van behoud van energie</strong>: wat het ene systeem afgeeft, komt "
                  "bij het andere terecht. Hebben twee systemen uiteindelijk dezelfde temperatuur "
                  "en gaat er geen warmte meer over, dan is er <strong>thermisch "
                  "evenwicht</strong>: een glas water dat al een uur in de kamer staat, een "
                  "thermometer die niet meer verandert, twee blokken metaal met dezelfde "
                  "temperatuur tegen elkaar."),
            ("p", "Wil je de <strong>eindtemperatuur</strong> van een mengsel "
                  "<strong>berekenen</strong>, dan stel je zo'n <strong>warmtebalans</strong> op: "
                  "de warmte die het warme deel afgeeft, is de warmte die het koude deel opneemt."),
        ]),
        dict(kop="De inwendige energie", blokken=[
            ("p", "De energie die in de <strong>deeltjes van een stof zelf</strong> zit, is de "
                  "<strong>inwendige energie</strong>. Ze bestaat uit twee delen: de "
                  "<strong>inwendige kinetische energie</strong> van de bewegende deeltjes, en de "
                  "<strong>inwendige potentiële energie</strong> die in de krachten tussen de "
                  "deeltjes zit."),
            ("p", "Verwarm je een stof <strong>zonder faseovergang</strong>, dan gaan de deeltjes "
                  "<strong>sneller bewegen</strong>: de inwendige <strong>kinetische</strong> "
                  "energie stijgt, en dat lees je af op de thermometer. Gebeurt er een "
                  "<strong>faseovergang</strong>, dan gaat de warmte naar het <strong>losmaken van "
                  "de deeltjes uit hun plaats</strong>: de inwendige <strong>potentiële</strong> "
                  "energie stijgt en de <strong>temperatuur blijft gelijk</strong>."),
            ("p", "De krachten die de deeltjes van een vloeistof bij elkaar houden, zijn de "
                  "<strong>cohesiekrachten</strong>. Om een vloeistof te laten verdampen moet je "
                  "die overwinnen, en dat kost veel energie."),
        ]),
        sectie("warmte-en-faseovergangen", "De faseovergangen"),
        dict(kop="Warmte bij een faseovergang", blokken=[
            blok("warmte-en-faseovergangen", "Latente warmte", "Alle toegevoerde warmte gaat naar"),
            blok("warmte-en-faseovergangen", "Latente warmte", "blijft ijs van nul graden"),
            ("p", "Daarom kan je je <strong>lelijk verbranden aan stoom van honderd graden</strong>, "
                  "erger dan aan water van honderd graden: bij het <strong>condenseren op je "
                  "huid</strong> komt de warmte er weer uit die het water nodig had om te "
                  "verdampen, en die komt <strong>bovenop</strong> de warmte van het water zelf. "
                  "Let dus op als je het deksel van een stoomapparaat opent."),
            ("p", "Hetzelfde mechanisme houdt een drankje koud. Een <strong>ijsblokje</strong> "
                  "neemt <strong>warmte uit het water op om te kunnen smelten</strong>, zonder "
                  "zelf warmer te worden. Zolang er ijs smelt, blijft het mengsel rond nul graden; "
                  "pas als het laatste blokje weg is, warmt het drankje op. "
                  "<strong>Koude bestaat niet</strong> als iets dat overgaat."),
        ]),
        dict(kop="Warmte in het dagelijkse leven", blokken=[
            ("p", "<strong>Water</strong> gedraagt zich bijzonder: het <strong>neemt veel warmte "
                  "op zonder snel op te warmen</strong>. Daarom is het een <strong>goede "
                  "koelvloeistof</strong> in een motor, en daarom blijft het aan de "
                  "<strong>kust</strong> in de winter zachter dan in het binnenland: het zeewater "
                  "<strong>geeft zijn warmte traag en lang af</strong>. In september is de zee nog "
                  "warm terwijl de lucht al afkoelt."),
            ("p", "Wie zijn <strong>buitenmuren en dak isoleert</strong>, zorgt dat hij "
                  "<strong>minder warmte verliest en dus minder moet verwarmen</strong>. "
                  "Isolatie vertraagt het weglopen van de warmte naar buiten. "
                  "<strong>Zweten</strong> doet het omgekeerde: het water op je huid "
                  "<strong>verdampt en neemt daarvoor warmte van je lichaam op</strong>, en zo koel "
                  "je af. In vochtige lucht verdampt zweet slechter, en dus koel je minder goed af."),
            ("p", "Twee toepassingen die op het eerste gezicht vreemd lijken. "
                  "<strong>Fruitboeren beregenen hun bomen</strong> als er nachtvorst op weg is, "
                  "omdat <strong>water bij het bevriezen warmte afgeeft</strong> aan de knoppen en "
                  "ze zo rond nul graden houdt. En een <strong>brandwonde</strong> houd je onder "
                  "<strong>koud stromend water</strong>, omdat dat water de <strong>warmte uit de "
                  "huid blijft wegnemen</strong>; koude breng je niet binnen, warmte voer je af."),
        ]),
    ],
    onthoud=[
        "Temperatuur hangt samen met de beweging van de deeltjes en meet je in graden Celsius.",
        "Warmte is energie die overgaat door een temperatuurverschil, en meet je in joule.",
        "Warmte gaat altijd van warm naar koud, tot het thermisch evenwicht. Koude bestaat niet.",
        "Een hogere temperatuur betekent niet meer warmte: de massa en de stof spelen mee.",
        "De warmtebalans is de wet van behoud van energie: wat het ene afgeeft, neemt het andere op.",
        "Inwendige energie = inwendige kinetische energie plus inwendige potentiële energie.",
        "Verwarmen zonder faseovergang: de deeltjes bewegen sneller en de temperatuur stijgt.",
        "Bij een faseovergang stijgt de potentiële energie en blijft de temperatuur gelijk.",
        "Cohesiekrachten houden de deeltjes van een vloeistof bij elkaar.",
        "Stollen, condenseren en desublimeren geven warmte af; smelten, verdampen en sublimeren nemen op.",
        "Het smeltpunt en het stolpunt van een zuivere stof liggen op dezelfde temperatuur.",
        "Stoom verbrandt erger dan water van honderd graden, want bij condenseren komt er warmte vrij.",
        "Water neemt veel warmte op zonder snel op te warmen: goede koelvloeistof, zacht zeeklimaat.",
        "Zweten koelt doordat het verdampen warmte uit je huid haalt.",
        "Beregenen beschermt tegen nachtvorst, want bevriezend water geeft warmte af.",
    ],
)

HERBOUW["kracht-als-vector-en-bewegingstoestand"] = dict(
    vak=VAK, niveau=DF, titel="Kracht als vector en bewegingstoestand",
    onder="De vier kenmerken van een kracht, het samenstellen van krachtvectoren, de "
          "bewegingstoestand van een lichaam en de traagheid in het verkeer.",
    secties=[
        dict(kop="Een kracht tekenen", blokken=[
            ("p", "Een <strong>kracht</strong> is een <strong>vectoriële grootheid</strong>. Ze "
                  "heeft dus niet alleen een getal, maar <strong>vier kenmerken</strong>: een "
                  "<strong>grootte</strong>, een <strong>richting</strong>, een <strong>zin</strong> "
                  "en een <strong>aangrijpingspunt</strong>. De eenheid van kracht is de "
                  "<strong>newton</strong>."),
            ("p", "Je stelt een kracht voor <strong>met een pijl die in het aangrijpingspunt "
                  "begint</strong>. De <strong>lengte</strong> van de pijl geeft de grootte, de "
                  "<strong>lijn</strong> waarop ze ligt de richting, en de <strong>punt</strong> de "
                  "zin. Twee krachten van tien newton kunnen elkaar opheffen of samen twintig "
                  "newton geven: dat hangt af van hun zin."),
            ("p", "Bij een voorbeeld moet je <strong>alle krachten</strong> die op een voorwerp "
                  "werken kunnen tekenen en met het <strong>juiste symbool</strong> benoemen, en "
                  "daarbij rekening houden met de <strong>bewegingstoestand</strong>: ligt het "
                  "voorwerp in <strong>rust</strong>, beweegt het met een <strong>constante "
                  "snelheid</strong>, <strong>versnelt</strong> het of <strong>vertraagt</strong> "
                  "het? De grootte van je pijlen moet daarbij passen."),
            ("p", "Een <strong>dynamometer</strong> of krachtmeter meet de grootte van een kracht "
                  "rechtstreeks, in newton."),
        ]),
        sectie("vrije-val-verticale-worp-en-krachten", "Krachten",
               nieuwe_kop="De soorten krachten en de resulterende kracht",
               zonder=("Hangt een gewicht",)),
        dict(kop="Rust, constante snelheid, versnellen of vertragen", blokken=[
            ("p", "Staat een <strong>kist stil op de vloer</strong>, dan is de "
                  "<strong>resulterende kracht nul newton</strong>: de <strong>zwaartekracht en de "
                  "normaalkracht heffen elkaar op</strong>. Hetzelfde geldt voor een boek op een "
                  "tafel. Dat is het <strong>traagheidsbeginsel</strong>: een voorwerp "
                  "<strong>blijft in rust of beweegt rechtdoor met een constante snelheid zolang "
                  "de resulterende kracht nul is</strong>."),
            ("p", "Een kracht is dus <strong>niet nodig om een beweging aan te houden</strong>, "
                  "alleen om ze te <strong>veranderen</strong>. Een voorwerp dat "
                  "<strong>vertraagt</strong>, heeft dus wél een kracht op zich: een resulterende "
                  "kracht <strong>tegen de beweging in</strong>. Bij een auto die remt is dat de "
                  "wrijvingskracht van de remmen en van de weg."),
            ("p", "Die drie veranderingen samen noemen we de <strong>dynamische effecten</strong> "
                  "van een resulterende kracht: <strong>versnellen</strong>, "
                  "<strong>vertragen</strong> en <strong>van richting veranderen</strong>."),
        ]),
        sectie("vrije-val-verticale-worp-en-krachten", "Krachten samenstellen"),
        dict(kop="Rekenen met krachten op één lijn", blokken=[
            ("p", "Op <strong>één lijn en in dezelfde zin</strong> tel je de grootten op. Duwen "
                  "twee mensen een kast in dezelfde zin, de een met <strong>80</strong> en de "
                  "ander met <strong>50 newton</strong>, dan is de resulterende kracht "
                  "<strong>130 newton</strong>."),
            ("p", "Op <strong>één lijn maar in tegengestelde zin</strong> trek je ze van elkaar "
                  "af, en de <strong>zin van de grootste</strong> wint. Werken er <strong>60</strong> "
                  "en <strong>25 newton</strong> tegen elkaar in, dan blijft er <strong>35 "
                  "newton</strong> over. Zijn ze <strong>precies even groot</strong>, dan is de "
                  "resulterende kracht <strong>nul</strong>, en niet het dubbele."),
        ]),
        dict(kop="Zwaartekracht, massa en gewicht", blokken=[
            ("p", "De <strong>zwaartekracht</strong> is de kracht waarmee de aarde aan een voorwerp "
                  "trekt. Ze is een <strong>veldkracht</strong>: ze werkt <strong>zonder "
                  "contact</strong>. Een <strong>normaalkracht</strong> of een "
                  "<strong>wrijvingskracht</strong> heeft wel contact nodig."),
            blok("vrije-val-verticale-worp-en-krachten", "Zwaartekracht, massa en gewicht",
                 "hoeveelheid materie"),
            ("p", "Zet je de gemeten <strong>zwaartekracht tegenover de massa</strong> in een "
                  "grafiek, dan krijg je een <strong>rechte door de oorsprong</strong>: de twee "
                  "zijn <strong>recht evenredig</strong>. Twee keer zoveel massa geeft twee keer "
                  "zoveel zwaartekracht."),
            blok("vrije-val-verticale-worp-en-krachten", "Zwaartekracht, massa en gewicht",
                 "ruimtestation"),
            ("p", "Het punt waarin je de <strong>hele zwaartekracht</strong> op een voorwerp "
                  "laat aangrijpen, is het <strong>zwaartepunt</strong>. Bij een regelmatig "
                  "voorwerp ligt dat in het midden; bij een onregelmatig voorwerp niet, en net "
                  "daarom kipt het sneller om."),
            ("p", "De <strong>veerkracht</strong> is de kracht waarmee een veer terugduwt of "
                  "terugtrekt als je ze indrukt of uitrekt. Ze werkt <strong>tegen de vervorming "
                  "in</strong>, en laat je de veer los, dan brengt die kracht ze terug naar haar "
                  "oorspronkelijke lengte."),
        ]),
        dict(kop="Traagheid in het verkeer", blokken=[
            ("p", "De <strong>lading van een vrachtwagen</strong> moet goed vastgemaakt worden "
                  "omdat ze <strong>door haar traagheid bij het remmen doorschuift</strong>. Zonder "
                  "kracht gaat die lading verder met de snelheid die ze had, tot iets haar "
                  "tegenhoudt."),
            ("p", "Een <strong>vrachtwagen en een auto die met dezelfde snelheid rijden, hebben "
                  "niet dezelfde remkracht nodig</strong>. De vrachtwagen heeft veel meer massa en "
                  "dus veel meer traagheid: om hem op dezelfde afstand tot stilstand te brengen is "
                  "een <strong>veel grotere remkracht</strong> nodig."),
            ("p", "De <strong>remafstand</strong> hangt af van de <strong>snelheid</strong> en van "
                  "de <strong>wrijvingskracht</strong>. Op een <strong>natte weg</strong> is de "
                  "wrijvingskracht tussen de band en het wegdek <strong>kleiner</strong>, dus "
                  "vertraagt de auto minder hard en wordt de remweg langer. Bij een hogere "
                  "snelheid loopt die afstand nog veel sneller op."),
            ("p", "Op een <strong>vliegtuig in de lucht</strong> werken de <strong>stuwkracht</strong> "
                  "van de motoren, de <strong>zwaartekracht</strong> naar beneden en de "
                  "<strong>wrijvingskracht van de lucht</strong>, naast de draagkracht van de "
                  "vleugels. Een <strong>normaalkracht</strong> is er niet: die bestaat alleen "
                  "zolang het vliegtuig op een oppervlak rust. Bij een raket is de "
                  "<strong>stuwkracht</strong> wat hem vooruit laat gaan; bij een auto heet die "
                  "kracht de <strong>motorkracht</strong>."),
            ("p", "Een <strong>kist die stil op een helling staat</strong> en niet wegschuift, "
                  "wordt tegengehouden door de <strong>wrijvingskracht</strong> tussen de kist en "
                  "de helling."),
        ]),
    ],
    onthoud=[
        "Een kracht heeft vier kenmerken: grootte, richting, zin en aangrijpingspunt. Eenheid: newton.",
        "Je tekent een kracht als een pijl die in het aangrijpingspunt begint.",
        "Soorten krachten: normaalkracht, wrijvingskracht, zwaartekracht, veerkracht, stuwkracht, motorkracht.",
        "Teken je krachten, let dan op de bewegingstoestand: rust, constante snelheid, versnellen of vertragen.",
        "Traagheidsbeginsel: in rust of constante snelheid zolang de resulterende kracht nul is.",
        "Dynamische effecten van een resulterende kracht: versnellen, vertragen, van richting veranderen.",
        "Op één lijn en dezelfde zin: optellen. Tegengestelde zin: aftrekken, de grootste wint.",
        "Twee even grote krachten in tegengestelde zin geven samen nul, niet het dubbele.",
        "Massa is de hoeveelheid materie en blijft overal gelijk; gewicht is een kracht in newton.",
        "De zwaartekracht is een veldkracht: ze werkt zonder contact.",
        "Zwaartekracht tegenover massa in een grafiek geeft een rechte door de oorsprong.",
        "Een dynamometer meet de grootte van een kracht in newton.",
        "Lading vastmaken: bij het remmen schuift ze door haar traagheid door.",
        "Meer massa betekent meer traagheid en dus een grotere remkracht.",
        "Een natte weg geeft minder wrijving en dus een langere remafstand.",
    ],
)

HERBOUW["druk-in-het-dagelijkse-leven"] = dict(
    vak=VAK, niveau=DF, titel="Druk in het dagelijkse leven",
    onder="De formule p = F / A, de eenheden pascal, kilopascal en hectopascal, de luchtdruk met "
          "haar overdruk en onderdruk, en de druk van een gas.",
    secties=[
        sectie("druk-en-de-gaswetten", "Druk op een oppervlak"),
        dict(kop="Rekenen met de druk", blokken=[
            ("p", "De formule in woorden: <strong>druk is de grootte van de kracht per "
                  "oppervlakte</strong>, of <strong>p = F / A</strong>. De grootheid die je door de "
                  "oppervlakte deelt, is dus de <strong>kracht</strong>. Duw je met <strong>600 "
                  "newton op 0,2 vierkante meter</strong>, dan is de druk <strong>3000 "
                  "pascal</strong>, of 3 kilopascal."),
            ("p", "De eenheden: de <strong>pascal</strong> is de SI-eenheid, en daarnaast gebruik "
                  "je de <strong>kilopascal</strong> en de <strong>hectopascal</strong>. "
                  "<strong>Eén kilopascal is 1000 pascal</strong> en <strong>één hectopascal is 100 "
                  "pascal</strong>; de 1013 hectopascal van het weerbericht zijn dus 101 300 "
                  "pascal. De <strong>newton</strong> is géén eenheid van druk, maar van kracht."),
            ("p", "Uit de formule volgt rechtstreeks hoe je de druk <strong>kleiner</strong> maakt: "
                  "het <strong>oppervlak vergroten</strong> of de <strong>kracht "
                  "verkleinen</strong>. Daar werken de <strong>brede rupsbanden</strong> van een "
                  "graafmachine op, de <strong>sneeuwschoenen</strong> van een wandelaar, de "
                  "<strong>brede poten</strong> onder een zware kast en de brede banden van een "
                  "rugzak. Een <strong>duimspijker</strong> wil net het omgekeerde: alle kracht op "
                  "een piepklein oppervlak."),
            ("kader", "Zo'n keuze tussen twee gelijkaardige voorwerpen is een klassieke "
                      "examenvraag: welke van de twee kies je, en waarom? Je legt dat telkens uit "
                      "met <strong>p = F / A</strong>: welke kracht werkt er, en op hoeveel "
                      "oppervlak?"),
        ]),
        dict(kop="Luchtdruk, overdruk en onderdruk", blokken=[
            ("p", "De <strong>luchtdruk</strong> of <strong>atmosferische druk</strong> komt van "
                  "het gewicht van de lucht boven ons en is op zeeniveau ongeveer <strong>1013 "
                  "hectopascal</strong>. Hij is <strong>niet op elke hoogte dezelfde</strong>: hoe "
                  "hoger je komt, hoe minder lucht er nog boven je ligt en hoe lager de luchtdruk. "
                  "Daarom staat een zak chips in de bergen bol."),
            blok("druk-en-de-gaswetten", "Druk in vloeistoffen", "barometer"),
            ("p", "Een druk die <strong>hoger</strong> is dan die van de omgeving, is "
                  "<strong>overdruk</strong>; een druk die <strong>lager</strong> is, is "
                  "<strong>onderdruk</strong>. In een opgepompte fietsband heerst overdruk, in een "
                  "vacuümzak voor voeding onderdruk."),
            ("p", "Met die twee verklaar je een rij alledaagse dingen. Je kan een vloeistof "
                  "<strong>met een rietje opzuigen</strong> omdat je in het rietje "
                  "<strong>onderdruk</strong> maakt: het verschil met de luchtdruk op de drank in "
                  "het glas <strong>duwt de vloeistof omhoog</strong>. En je "
                  "<strong>oren suizen bij het opstijgen van een vliegtuig</strong> omdat de "
                  "<strong>luchtdruk buiten daalt</strong> terwijl de druk in je oor nog hoog "
                  "blijft; slikken of gapen maakt die twee weer gelijk."),
        ]),
        sectie("druk-en-de-gaswetten", "Druk in gassen", zonder=("temperatuurschaal",)),
        dict(kop="Gasdruk in het dagelijkse leven", blokken=[
            ("p", "Omdat de deeltjes <strong>in alle richtingen</strong> bewegen, duwt een gas "
                  "<strong>overal even hard</strong> tegen de wand, dus ook naar boven en naar de "
                  "zijkanten. <strong>Niet alleen naar beneden</strong>: de deeltjes vallen niet "
                  "naar de bodem."),
            ("p", "Verwarm je een gas, dan gaan de deeltjes "
                  "<strong>sneller bewegen</strong> en botsen ze <strong>vaker en harder</strong> "
                  "tegen de wand. In een <strong>gesloten fles</strong>, die niet kan uitzetten, "
                  "<strong>stijgt dan de druk</strong>. Daarom kan een <strong>gasfles in de volle "
                  "zon</strong> ontploffen, staat er op een spuitbus dat je ze niet mag verwarmen, "
                  "en pompen <strong>wielrijders hun banden in de zomer wat minder hard op</strong>."),
            ("p", "Op een drukvat zit daarom een <strong>veiligheidsklep</strong>: die "
                  "<strong>gaat open zodra de druk binnen te hoog wordt</strong> en laat gas "
                  "ontsnappen voor het vat kan barsten."),
            ("p", "Koel je een gas af, dan gebeurt het omgekeerde. Een <strong>ballon in de "
                  "koelkast</strong> loopt wat leeg: de deeltjes bewegen trager, de druk daalt en "
                  "de ballon krimpt tot de druk binnen weer in evenwicht is met de luchtdruk "
                  "buiten."),
            blok("druk-en-de-gaswetten", "De gaswetten", "fietsband wordt warm"),
        ]),
    ],
    onthoud=[
        "Druk is de grootte van de kracht per oppervlakte: p = F / A, in pascal.",
        "Bij dezelfde kracht geeft een kleiner oppervlak een grotere druk.",
        "De druk kleiner maken: het oppervlak vergroten of de kracht verkleinen.",
        "Eén kilopascal is 1000 pascal, één hectopascal is 100 pascal. De newton is geen drukeenheid.",
        "600 newton op 0,2 vierkante meter geeft 3000 pascal.",
        "De luchtdruk is op zeeniveau ongeveer 1013 hectopascal en daalt als je hoger komt.",
        "Een barometer meet de luchtdruk buiten, een manometer de druk in een vat of leiding.",
        "Overdruk is hoger dan de omgevingsdruk, onderdruk lager.",
        "Een rietje werkt met onderdruk; de luchtdruk duwt de drank omhoog.",
        "Je oren suizen bij het opstijgen omdat de luchtdruk buiten daalt.",
        "De gasdruk komt van de botsingen van de deeltjes tegen de wand, in alle richtingen.",
        "Verwarmen in een gesloten vat doet de druk stijgen: gasflessen uit de zon, banden in de zomer zachter.",
        "Een veiligheidsklep gaat open als de druk te hoog wordt.",
        "Een gas in een kleiner volume persen geeft een hogere druk.",
    ],
)

# ─────────────────────────────────────────────────────────────
# De bundel die hier helemaal nieuw is.
# ─────────────────────────────────────────────────────────────
HERBOUW["biologische-feedback-en-homeostase"] = dict(
    vak=VAK, niveau=DF, titel="Biologische feedback en homeostase",
    onder="Hoe een organisme zijn inwendige milieu stabiel houdt: de vier schakels van een "
          "feedbacksysteem, en de regeling van de lichaamstemperatuur en de glucosespiegel.",
    secties=[
        dict(kop="Homeostase", blokken=[
            ("p", "<strong>Homeostase</strong> betekent dat een organisme zijn <strong>inwendige "
                  "milieu binnen nauwe grenzen houdt</strong>, terwijl de omgeving verandert. Het "
                  "is <strong>geen stilstand</strong>: je lichaamstemperatuur, je glucosegehalte "
                  "en je bloeddruk schommelen voortdurend een beetje en worden telkens "
                  "teruggebracht."),
            ("p", "Een organisme <strong>heeft die regeling nodig om zich te handhaven</strong>, "
                  "want zijn <strong>cellen werken alleen binnen nauwe grenzen</strong> van "
                  "temperatuur en samenstelling. Loopt het te ver uit, dan vallen de processen in "
                  "de cellen stil."),
            ("p", "De waarde waarrond het lichaam het inwendige milieu houdt, is de "
                  "<strong>normwaarde</strong>. Voor de lichaamstemperatuur ligt die rond 37 "
                  "graden. Wijkt de gemeten waarde daarvan af, dan grijpt het systeem in."),
            ("p", "Zo'n afwijking begint met een <strong>prikkel</strong>: <strong>elke "
                  "verandering in het inwendige of het uitwendige milieu</strong>. Koude lucht op "
                  "je huid is een <strong>uitwendige</strong> prikkel, een dalend glucosegehalte "
                  "in je bloed een <strong>inwendige</strong>."),
            ("p", "De regeling zelf gebeurt met een <strong>regelsysteem</strong> of "
                  "<strong>feedbacksysteem</strong>: het <strong>gebruikt het gevolg van een "
                  "proces om dat proces bij te sturen</strong>. Het <strong>meet</strong>, het "
                  "<strong>vergelijkt met de normwaarde</strong> en het <strong>stuurt bij</strong>, "
                  "dag en nacht, ook terwijl je beweegt. Een afwijking hoeft dus niet groot te "
                  "worden voor het systeem in werking komt, en net daardoor blijft de verstoring "
                  "klein."),
        ]),
        dict(kop="De vier schakels", blokken=[
            ("p", "Elk feedbacksysteem doorloopt dezelfde weg: <strong>prikkel, receptor, "
                  "conductor, effector, reactie</strong>. Die reactie verandert de prikkel zelf "
                  "weer, en zo is de cirkel rond."),
            ("p", tabel(
                ["Schakel", "Wat ze doet", "Wat het bij de mens is"],
                [["receptor", "vangt de prikkel op en zet hem om in een signaal",
                  "zintuigcellen, bijvoorbeeld de warmte- en koudereceptoren in de huid"],
                 ["conductor", "geeft het signaal door", "het zenuwstelsel en de hormonen"],
                 ["controlecentrum", "vergelijkt met de normwaarde en beslist",
                  "de hersenen en de hersenstam"],
                 ["effector", "voert de reactie uit", "de spieren en de klieren"]],
            )),
            ("p", "De <strong>signaaloverdracht</strong> verloopt op <strong>twee "
                  "manieren</strong>: <strong>elektrisch via de zenuwbanen</strong> of "
                  "<strong>chemisch via de hormonen</strong>. Een zenuwsignaal is "
                  "<strong>snel</strong> en gaat naar een nauwkeurig doel; een hormoon gaat met het "
                  "bloed mee, werkt <strong>langzamer</strong>, maar bereikt <strong>alle cellen "
                  "die er gevoelig voor zijn</strong>, en niet alleen de cellen die de zenuwen "
                  "aanwijzen."),
            ("p", "Op een <strong>schema</strong> van een feedbacksysteem geeft een "
                  "<strong>pijl</strong> de richting van de invloed. Gaat de pijl van de "
                  "<strong>huid naar de hersenen</strong>, dan is dat het <strong>signaal van de "
                  "receptoren naar het controlecentrum</strong>; de pijlen die terugkeren naar de "
                  "bloedvaten en de klieren zijn de <strong>bevelen aan de effectoren</strong>. "
                  "Een <strong>minteken</strong> op een pijl betekent dat die invloed "
                  "<strong>remmend</strong> is, een plusteken dat ze <strong>stimuleert</strong>."),
        ]),
        dict(kop="Negatieve en positieve feedback", blokken=[
            ("p", "Bij <strong>negatieve feedback</strong> werkt de reactie de gemeten verandering "
                  "<strong>tegen</strong>; bij <strong>positieve feedback</strong> "
                  "<strong>versterkt</strong> ze die juist. De woorden zeggen dus "
                  "<strong>niets over goed of slecht</strong>."),
            ("p", "Bijna alles wat je lichaam regelt, werkt met <strong>negatieve</strong> "
                  "feedback: je gaat <strong>zweten</strong> als je temperatuur stijgt, je "
                  "alvleesklier geeft <strong>insuline</strong> af als je glucosegehalte stijgt, en "
                  "de <strong>huidmondjes</strong> van een plant gaan dicht bij te veel "
                  "waterverlies. Telkens duwt de reactie de waarde terug naar de normwaarde."),
            ("p", "<strong>Positieve</strong> feedback komt veel minder voor en stopt pas als het "
                  "doel bereikt is. Bij een <strong>bloeding</strong> lokken de eerste "
                  "stollingsstoffen <strong>nog meer stolling</strong> uit tot de wonde dicht is, "
                  "en bij een <strong>bevalling</strong> worden de weeën <strong>steeds "
                  "krachtiger</strong>."),
        ]),
        dict(kop="De lichaamstemperatuur", blokken=[
            ("p", "De receptoren die meten of je het warm of koud hebt, zitten <strong>in de "
                  "huid</strong>: de <strong>warmte- en koudereceptoren</strong>. De huid is het "
                  "grensvlak met de omgeving. Hun signaal gaat naar de hersenen, die het met de "
                  "normwaarde vergelijken."),
            ("p", tabel(
                ["Je hebt het", "Wat de effectoren doen", "Wat je merkt"],
                [["te warm", "de bloedvaten in de huid verwijden, de zweetklieren geven zweet af",
                  "je huid wordt roder en je zweet"],
                 ["te koud", "de bloedvaten in de huid vernauwen, de spieren beginnen te rillen",
                  "je huid wordt bleek en koud, je rilt"]],
            )),
            ("p", "<strong>Verwijde</strong> bloedvaten brengen meer warm bloed naar de huid, waar "
                  "de warmte weg kan; <strong>vernauwde</strong> bloedvaten houden het warme bloed "
                  "in je binnenste, zodat je organen op temperatuur blijven terwijl je handen koud "
                  "worden. <strong>Rillen</strong> maakt extra warmte met je spieren."),
            ("p", "<strong>Zweet</strong> koelt je af doordat het <strong>water verdampt en "
                  "daarvoor warmte van je lichaam opneemt</strong>. In vochtige lucht verdampt "
                  "zweet slechter, en dan werkt dat koelen minder goed. De "
                  "<strong>zweetklieren</strong> zijn hier de effector."),
        ]),
        dict(kop="De glucosespiegel in het bloed", blokken=[
            ("p", "De <strong>alvleesklier</strong> maakt de <strong>twee hormonen</strong> die "
                  "elkaar tegenwerken: <strong>insuline</strong> en <strong>glucagon</strong>. "
                  "Welk van de twee ze afgeeft, hangt af van het glucosegehalte dat ze meet. De "
                  "<strong>lever</strong> en de <strong>spiercellen</strong> zijn de effectoren."),
            ("p", tabel(
                ["Het gehalte", "Hormoon", "Wat de lever en de spiercellen doen"],
                [["te hoog, na een maaltijd", "insuline",
                  "glucose uit het bloed halen en opslaan als glycogeen"],
                 ["te laag, na een paar uur niet eten", "glucagon",
                  "glycogeen afbreken en glucose aan het bloed geven"]],
            )),
            ("p", "<strong>Glycogeen</strong> is een lange keten van glucosemoleculen. Let op de "
                  "rolverdeling: het is <strong>insuline</strong> dat de lever glucose laat "
                  "<strong>opslaan</strong>, en <strong>glucagon</strong> dat het glycogeen weer "
                  "laat <strong>afbreken</strong>. Zweet voert geen glucose af."),
            ("p", "Dit is <strong>negatieve feedback</strong>, want de reactie brengt het gehalte "
                  "telkens <strong>terug naar de normwaarde</strong>: stijgt het, dan volgt een "
                  "reactie die het doet dalen, en daalt het, dan volgt een reactie die het doet "
                  "stijgen."),
            ("p", "Bij <strong>diabetes type 1</strong> maakt de alvleesklier <strong>geen "
                  "insuline</strong> meer. Het meten gaat nog, maar het <strong>signaal valt "
                  "weg</strong>: de lever en de spiercellen krijgen geen bevel om glucose op te "
                  "nemen, en het <strong>gehalte blijft te hoog</strong> staan."),
        ]),
        dict(kop="Nog drie feedbacksystemen", blokken=[
            ("p", "Drie andere voorbeelden, en ze werken met dezelfde schakels."),
            ("p", "De <strong>bloeddruk</strong>: <strong>receptoren in de wand van grote "
                  "bloedvaten</strong> meten de druk, de <strong>hersenstam</strong> is het "
                  "controlecentrum, en het <strong>hart en de bloedvaten</strong> zijn de "
                  "effectoren. Bij een te hoge druk <strong>vertraagt het hart en verwijden de "
                  "bloedvaten</strong>."),
            ("p", "Het <strong>hartritme bij stress</strong>: je hartritme "
                  "<strong>versnelt</strong>, zodat je <strong>spieren meer zuurstof en glucose "
                  "krijgen</strong> en je lichaam klaar is om te handelen. Het vertraagt dus niet "
                  "om energie te sparen. Is de stress voorbij, dan brengt het lichaam het ritme "
                  "weer naar zijn normwaarde."),
            ("p", "De <strong>waterhuishouding bij planten</strong>: dreigt een plant te veel water "
                  "te verliezen, dan <strong>sluit ze haar huidmondjes</strong>. Ook dat is "
                  "negatieve feedback: het waterverlies is de prikkel, de huidmondjes zijn de "
                  "effector, en door te sluiten gaat het verlies naar beneden."),
            ("weetje", "Een koortsthermometer meet niet of je ziek bent, maar of je lichaam zijn "
                       "normwaarde <em>zelf</em> hoger gezet heeft. Bij koorts stuurt je lichaam "
                       "even naar een andere waarde toe, en daarom heb je het koud terwijl je "
                       "temperatuur stijgt."),
        ]),
    ],
    onthoud=[
        "Homeostase: het inwendige milieu binnen nauwe grenzen houden terwijl de omgeving verandert.",
        "De normwaarde is de waarde waarrond het systeem regelt; voor de temperatuur rond 37 graden.",
        "Een prikkel is elke verandering in het inwendige of het uitwendige milieu.",
        "Een feedbacksysteem meet, vergelijkt met de normwaarde en stuurt bij.",
        "De weg: prikkel, receptor, conductor, effector, reactie.",
        "Receptoren zijn zintuigcellen, conductoren het zenuwstelsel en de hormonen, effectoren de spieren en de klieren.",
        "De hersenen en de hersenstam zijn het controlecentrum.",
        "Signaaloverdracht: elektrisch via de zenuwbanen of chemisch via de hormonen.",
        "Op een schema betekent een minteken een remmende invloed, een plusteken een stimulerende.",
        "Negatieve feedback werkt de verandering tegen, positieve feedback versterkt ze.",
        "Positieve feedback: bloedstolling en de weeën bij een bevalling.",
        "Te warm: bloedvaten verwijden, zweetklieren geven zweet af. Te koud: vernauwen en rillen.",
        "Zweet koelt doordat het verdampt en daarvoor warmte van je lichaam opneemt.",
        "Insuline laat de lever glucose opslaan als glycogeen; glucagon laat glycogeen afbreken.",
        "De alvleesklier maakt beide hormonen; de lever en de spiercellen zijn de effectoren.",
        "Bij diabetes type 1 valt het signaal insuline weg en blijft het glucosegehalte te hoog.",
        "Bloeddruk: receptoren in de vaatwand, de hersenstam, het hart en de bloedvaten.",
        "Bij stress versnelt je hartritme; een plant sluit haar huidmondjes bij waterverlies.",
    ],
)

# De volgorde van de fiche: biologie, chemie, fysica, en achteraan het veilig
# werken en het onderzoek.
ORDE = [
    "biologische-feedback-en-homeostase",
    "micro-organismen-het-microbioom-en-bewaring",
    "voortplanting-en-de-hormonale-regeling",
    "mengsels-en-zuivere-stoffen",
    "chemische-formules-en-chemische-reacties",
    "de-bouw-van-het-atoom-en-het-periodiek-systeem",
    "energieomzettingen-vermogen-en-rendement",
    "warmte-faseovergangen-en-inwendige-energie",
    "kracht-als-vector-en-bewegingstoestand",
    "druk-in-het-dagelijkse-leven",
    "elektriciteit-de-wet-van-ohm-en-veiligheid",
    "veilig-werken-meten-en-levensreddend-handelen",
    "grootheden-eenheden-en-wetenschappelijk-onderzoek",
]


def pas_toe(bundels: dict):
    for kort, soort, waar, inhoud in INGREPEN:
        if kort not in bundels:
            raise SystemExit(f"Onbekende bundel in INGREPEN: {kort}")
        secties = bundels[kort]["secties"]
        if soort == "schrap-sectie":
            raak = [i for i, s in enumerate(secties) if s["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} secties heten {waar!r}, verwacht 1")
            secties.pop(raak[0])
        elif soort == "sectie-vooraan":
            secties.insert(0, copy.deepcopy(inhoud))
        elif soort == "sectie-achteraan":
            secties.append(copy.deepcopy(inhoud))
        elif soort == "vervang-blok":
            raak = [
                (i, j)
                for i, s in enumerate(secties)
                for j, b in enumerate(s["blokken"])
                if waar in tekst_van(b)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} blokken bevatten {waar!r}, verwacht 1")
            i, j = raak[0]
            secties[i]["blokken"][j : j + 1] = inhoud
        else:
            raise SystemExit(f"Onbekende ingreep: {soort}")


def bouw() -> dict:
    uit = {}
    for bron, nieuwe_kort, nieuwe_titel in MEE:
        b = copy.deepcopy(_bron(bron))
        b["niveau"] = DF
        kort = nieuwe_kort or bron
        if nieuwe_titel:
            b["titel"] = nieuwe_titel
        uit[kort] = b
    pas_toe(uit)
    for kort, onder in ONDERTITELS.items():
        if kort not in uit:
            raise SystemExit(f"Onbekende bundel in ONDERTITELS: {kort}")
        uit[kort]["onder"] = onder
    for kort, lijst in ONTHOUD.items():
        if kort not in uit:
            raise SystemExit(f"Onbekende bundel in ONTHOUD: {kort}")
        uit[kort]["onthoud"] = list(lijst)
    uit.update(copy.deepcopy(HERBOUW))

    if sorted(uit) != sorted(ORDE):
        tekort = sorted(set(ORDE) - set(uit))
        teveel = sorted(set(uit) - set(ORDE))
        raise SystemExit(f"De bundels kloppen niet met ORDE. Ontbreekt: {tekort}. Te veel: {teveel}.")

    for kort, b in uit.items():
        alles = " ".join(
            [b["onder"], b["titel"]]
            + [s["kop"] for s in b["secties"]]
            + [tekst_van(blokje) for s in b["secties"] for blokje in s["blokken"]]
            + list(b.get("onthoud", []))
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{kort} gebruikt nog {woord!r}, dat staat niet op deze fiche")
        if not b.get("onthoud"):
            raise SystemExit(f"{kort} heeft geen onthoudlijstje")

    return {kort + NIEUW: uit[kort] for kort in ORDE}


BUNDELS = bouw()

if __name__ == "__main__":
    for sleutel, b in BUNDELS.items():
        bundel.schrijf(b, sleutel)
        print(" ", sleutel)

# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche wiskunde 2de graad dubbele finaliteit, geldig vanaf
1 januari 2027. Die fiche geldt voor bedrijf en organisatie en voor
maatschappij en welzijn. Anders dan bij doorstroom is er maar één wiskundefiche
voor de dubbele finaliteit, en ze heet gewoon wiskunde. Daarom dragen deze
bundels het vak "Wiskunde" en niet "Wiskunde gevorderd".

Negen van de dertien bundels komen van doorstroom. Die leerstof is dezelfde en
wordt hier overgenomen met de verschillen erin gepatcht. Vier bundels zijn
nieuw geschreven, omdat de fiche daar een andere nadruk legt:

  * logica en bewijzen, de parabool, de tweedegraadsvergelijking, de
    sinusregel, de cosinusregel, de vectoren en de puntenwolk staan **niet**
    op de DF-fiche en vallen hier weg;
  * de goniometrie in een rechthoekige driehoek, de stelsels van twee
    eerstegraadsvergelijkingen, het tekenverloop en het verloopschema, en de
    misleiding met cijfers krijgen er juist méér ruimte.

De gewichten achteraan de fiche: relaties en verandering 40 %, meetkunde 30 %,
getallenleer 15 %, data en onzekerheid 12,5 %, telproblemen 2,5 %.

De sleutels eindigen op "-boost-dubbele-finaliteit", de volledige naam van de
categorie, net zoals bij doorstroom. De vragen komen uit
`../../boost-dubbele-finaliteit/wiskunde.json`.
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import maak_wiskunde_boost as doorstroom

VAK = "Wiskunde"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"

# Welke doorstroombundels we overnemen, en onder welke sleutel ze hier komen.
# Staat er een tweede naam bij, dan verandert de titel van het hoofdstuk mee.
OVERNEMEN = {
    "een-opgave-aanpakken-van-context-naar-wiskunde": None,
    "reele-getallen-wortels-en-machten": None,
    "ordenen-afronden-intervallen-en-wetenschappelijke-notatie": (
        "ordenen-afronden-en-intervallen",
        "Ordenen, afronden en intervallen",
    ),
    "rechten-vlakken-en-gelijkvormigheid": None,
    "pythagoras-en-de-rechthoekige-driehoek": None,
    "formules-omvormen-en-eerstegraadsvergelijkingen": None,
    "functies-en-de-rechte": None,
    "telproblemen-met-boom-en-venndiagram": None,
    "statistiek-voorstellingen-centrum-en-spreiding": None,
}

# (bundelsleutel zonder categorie, tekst waarop de ingreep aanhaakt, wat, blokken)
PATCHES = [
    (
        "ordenen-afronden-en-intervallen",
        "Wetenschappelijke notatie",
        "schrap-sectie",
        None,
    ),
    (
        "een-opgave-aanpakken-van-context-naar-wiskunde",
        "En ICT is hulp bij het rekenen en het tekenen",
        "na",
        [
            (
                "kader",
                "Op het examen krijg je een <strong>online wetenschappelijk rekentoestel</strong> en een "
                "webpagina met <strong>rekenapps</strong>. Andere hulpmiddelen mag je niet gebruiken. "
                "Een geodriehoek, een passer of een meetlat mag je wel altijd vragen.",
            )
        ],
    ),
]

# Losse zinnen die te diep zitten voor een blokingreep, met het aantal keer dat
# ze mogen voorkomen. Klopt dat aantal niet, dan stopt het script.
TEKSTFIXES = [
    ("in andere driehoeken heb je de cosinusregel nodig", "in andere driehoeken werkt ze niet", 1),
    ("rekenapps gebruiken en constructies maken in GeoGebra", "het online rekentoestel en de rekenapps gebruiken", 1),
    ("Wiskunde gevorderd", VAK, 9),
]

ONDERTITELS = {
    "ordenen-afronden-en-intervallen": "Getallen vergelijken en schatten, netjes afronden, en intervallen lezen en schrijven.",
}

# Regels die uit het onthoudlijstje van een bundel moeten, met hun bundel erbij.
ONTHOUD_WEG = [
    ("ordenen-afronden-en-intervallen", "Wetenschappelijke notatie: één cijfer van 1 tot 9 voor de komma, maal een macht van tien."),
    ("ordenen-afronden-en-intervallen", "Een negatieve exponent maakt het getal klein, niet negatief."),
]

# Wat niet op de DF-fiche staat. Staat een van deze woorden na alle ingrepen nog
# in een bundel, dan stopt het script.
VERBODEN = [
    "cosinusregel",
    "sinusregel",
    "wetenschappelijke notatie",
    "parabool",
    "tweedegraadsvergelijking",
    "waarheidstabel",
    "geogebra",
    "wiskunde gevorderd",
]


def tekst_van(blok) -> str:
    return " ".join(str(d) for d in blok[1:])


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        secties = bundels[sleutel]["secties"]
        if wat == "schrap-sectie":
            raak = [i for i, s in enumerate(secties) if s["kop"] == haak]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} secties heten {haak!r}, verwacht 1")
            secties.pop(raak[0])
            continue
        raak = [
            (i, j)
            for i, s in enumerate(secties)
            for j, b in enumerate(s["blokken"])
            if haak in tekst_van(b)
        ]
        if len(raak) != 1:
            raise SystemExit(f"{sleutel}: {len(raak)} blokken bevatten {haak!r}, verwacht 1")
        i, j = raak[0]
        if wat == "vervang":
            secties[i]["blokken"][j : j + 1] = nieuw
        elif wat == "na":
            secties[i]["blokken"][j + 1 : j + 1] = nieuw
        else:
            raise SystemExit(f"Onbekende ingreep: {wat}")


def fix_teksten(ding, oud: str, nieuw: str) -> tuple:
    """Vervangt oud door nieuw, hoe diep het ook zit, en telt hoe vaak."""
    if isinstance(ding, str):
        return ding.replace(oud, nieuw), ding.count(oud)
    if isinstance(ding, dict):
        aantal = 0
        for k, v in ding.items():
            ding[k], n = fix_teksten(v, oud, nieuw)
            aantal += n
        return ding, aantal
    if isinstance(ding, (list, tuple)):
        stuks, aantal = [], 0
        for v in ding:
            v, n = fix_teksten(v, oud, nieuw)
            stuks.append(v)
            aantal += n
        return type(ding)(stuks), aantal
    return ding, 0


def overgenomen() -> dict:
    uit = {}
    for kort, hernoem in OVERNEMEN.items():
        bron = kort + OUD
        if bron not in doorstroom.BUNDELS:
            raise SystemExit(f"Onbekende doorstroombundel: {bron}")
        nieuw = copy.deepcopy(doorstroom.BUNDELS[bron])
        nieuw["niveau"] = DF
        if hernoem:
            kort, nieuw["titel"] = hernoem
        uit[kort + NIEUW] = nieuw
    pas_toe(uit)
    for oud, nieuw, hoevaak in TEKSTFIXES:
        uit, aantal = fix_teksten(uit, oud, nieuw)
        if aantal != hoevaak:
            raise SystemExit(f"{oud!r} staat {aantal} keer in de bundels, verwacht {hoevaak}")
    for kort, onder in ONDERTITELS.items():
        uit[kort + NIEUW]["onder"] = onder
    for kort, regel in ONTHOUD_WEG:
        lijst = uit[kort + NIEUW]["onthoud"]
        if regel not in lijst:
            raise SystemExit(f"{kort}: deze onthoudregel staat er niet meer: {regel!r}")
        lijst.remove(regel)
    return uit


def controleer(bundels: dict):
    for sleutel, b in bundels.items():
        alles = " ".join(
            [b["titel"], b["onder"]]
            + [s["kop"] for s in b["secties"]]
            + [tekst_van(blok) for s in b["secties"] for blok in s["blokken"]]
            + list(b.get("onthoud", []))
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
        if b["vak"] != VAK:
            raise SystemExit(f"{sleutel} draagt het vak {b['vak']!r}, verwacht {VAK!r}")
        if b["niveau"] != DF:
            raise SystemExit(f"{sleutel} draagt het niveau {b['niveau']!r}")


BUNDELS = overgenomen()
NIEUWE = {}


# ─────────────────── 6. De rechthoekige driehoek oplossen en toepassen
NIEUWE["de-rechthoekige-driehoek-oplossen-en-toepassen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="De rechthoekige driehoek oplossen en toepassen",
    onder="Zijden en hoeken berekenen met sinus, cosinus en tangens, en die toepassen op kijkhoeken en hellingen.",
    secties=[
        dict(kop="Welke zijde is welke?", blokken=[
            ("p", "De <strong>schuine zijde</strong> (de hypotenusa) ligt tegenover de rechte hoek en is altijd "
                  "de langste zijde. De twee andere heten <strong>rechthoekszijden</strong>. Welke van die twee "
                  "de overstaande en welke de aanliggende is, hangt af van de hoek waar je naar kijkt."),
            ("p", tabel(["Zijde", "Hoe je ze herkent bij hoek A"], [
                ["schuine zijde", "ligt tegenover de rechte hoek, en dus nooit tegenover A"],
                ["overstaande zijde", "de rechthoekszijde die tegenover A ligt"],
                ["aanliggende zijde", "de rechthoekszijde die tegen A aan ligt"],
            ])),
            ("kader", "Twee zijden raken hoek A: de schuine zijde en een rechthoekszijde. Met <strong>aanliggende "
                      "zijde</strong> bedoelen we altijd die rechthoekszijde. Kijk je naar de andere scherpe hoek, "
                      "dan wisselen overstaande en aanliggende van plaats."),
            ("p", "De drie verhoudingen hangen enkel van de <strong>hoek</strong> af, niet van hoe groot je de "
                  "driehoek tekent. Twee driehoeken met dezelfde hoeken zijn immers <strong>gelijkvormig</strong>: "
                  "alle zijden worden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg."),
        ]),
        dict(kop="De drie verhoudingen in cijfers", blokken=[
            ("p", "Neem de driehoek met zijden 3, 4 en 5, en kijk naar de hoek tegenover de zijde 3. Dan is de "
                  "overstaande zijde 3, de aanliggende 4 en de schuine 5."),
            ("p", tabel(["Verhouding", "Breuk", "Uitkomst"], [
                ["sinus", "overstaande op schuine, dus 3 op 5", "0,6"],
                ["cosinus", "aanliggende op schuine, dus 4 op 5", "0,8"],
                ["tangens", "overstaande op aanliggende, dus 3 op 4", "0,75"],
            ])),
            ("p", "Bij de sinus en de cosinus deel je door de schuine zijde, en die is altijd de langste. Een "
                  "<strong>sinus van een scherpe hoek is dus altijd kleiner dan 1</strong>. Bij de tangens komt de "
                  "schuine zijde niet voor, en daarom <strong>kan een tangens wél groter zijn dan 1</strong>."),
            ("p", "Bij een hoek van <strong>45 graden</strong> zijn de twee rechthoekszijden even lang, dus zijn "
                  "de sinus en de cosinus daar aan elkaar gelijk en is de tangens precies 1."),
            ("weetje", "Een goniometrisch getal van een scherpe hoek is nooit negatief: je deelt twee lengtes door "
                       "elkaar, en een lengte is altijd positief."),
        ]),
        dict(kop="Een zijde zoeken", blokken=[
            ("p", "Kies de verhouding waarin de zijde die je kent én de zijde die je zoekt allebei voorkomen. "
                  "Dan blijft er één onbekende over."),
            ("p", tabel(["Je kent", "Je zoekt", "Je rekent"], [
                ["hoek en schuine zijde", "overstaande zijde", "sinus maal schuine zijde"],
                ["hoek en schuine zijde", "aanliggende zijde", "cosinus maal schuine zijde"],
                ["hoek en aanliggende zijde", "overstaande zijde", "tangens maal aanliggende zijde"],
                ["hoek en aanliggende zijde", "schuine zijde", "aanliggende zijde gedeeld door de cosinus"],
            ])),
            ("p", "<strong>Voorbeeld.</strong> Een ladder van 6 meter staat onder 60 graden met de grond. De "
                  "hoogte die hij bereikt is de overstaande zijde: 6 maal de sinus van 60 graden, ongeveer "
                  "<strong>5,20 meter</strong>. De afstand van zijn voet tot de muur is de aanliggende zijde: "
                  "6 maal de cosinus van 60 graden, en dat is 6 maal 0,5, dus precies <strong>3 meter</strong>."),
            ("p", "<strong>Nog een.</strong> De sinus van een hoek is 0,5 en de schuine zijde is 10. De overstaande "
                  "zijde is dan 0,5 maal 10, dus 5."),
        ]),
        dict(kop="Een hoek zoeken", blokken=[
            ("p", "Ken je twee zijden, dan reken je eerst hun verhouding uit en gebruik je daarna de "
                  "<strong>inverse</strong> van het bijbehorende goniometrische getal op je rekentoestel."),
            ("p", tabel(["Je kent", "Je deelt", "Je gebruikt"], [
                ["overstaande en schuine zijde", "overstaande op schuine", "de inverse sinus"],
                ["aanliggende en schuine zijde", "aanliggende op schuine", "de inverse cosinus"],
                ["de twee rechthoekszijden", "overstaande op aanliggende", "de inverse tangens"],
            ])),
            ("p", "Ken je één goniometrisch getal, dan haal je het andere uit de <strong>grondformule</strong>: "
                  "sinus in het kwadraat plus cosinus in het kwadraat is 1. Is de cosinus 0,96, dan is de sinus in "
                  "het kwadraat gelijk aan 1 min 0,9216, dus 0,0784, en de sinus zelf <strong>0,28</strong>."),
            ("p", "De derde hoek vind je zonder te rekenen met verhoudingen: alle hoeken samen zijn 180 graden en "
                  "de rechte hoek neemt er al 90 in. De twee scherpe hoeken zijn dus <strong>samen 90 graden</strong>. "
                  "Bij een scherpe hoek van 30 graden is de andere dus 60 graden."),
            ("kader", "Krijg je voor een scherpe hoek een uitkomst van 91 graden, dan zit er een fout in je "
                      "berekening. In een rechthoekige driehoek blijft elke scherpe hoek onder 90 graden."),
        ]),
        dict(kop="De driehoek oplossen", blokken=[
            ("p", "Een rechthoekige driehoek <strong>oplossen</strong> betekent: alle zijden en alle hoeken ervan "
                  "berekenen. Daarvoor heb je twee gegevens nodig naast de rechte hoek: twee zijden, of één zijde "
                  "en één scherpe hoek. Met <strong>één zijde alleen lukt het niet</strong>."),
            ("p", "Drie gewoontes die veel fouten voorkomen:"),
            ("p", tabel(["Gewoonte", "Waarom"], [
                ["eerst een schets maken", "dan zie je welke zijde overstaand en welke aanliggend is"],
                ["je rekentoestel op graden zetten", "anders klopt je uitkomst niet terwijl je redenering wel juist is"],
                ["pas op het einde afronden", "elke afronding onderweg stapelt zich op in je eindantwoord"],
            ])),
            ("p", "Toont je toestel 5,1962 en moet je antwoord in centimeters nauwkeurig, rond dan dáár af, niet "
                  "bij elke tussenstap."),
        ]),
        dict(kop="Kijkhoek, hoogte en helling", blokken=[
            ("p", "Hier komt de leerstof in de echte wereld terecht. Twee situaties komen steeds terug."),
            ("p", "<strong>De hoogte uit een kijkhoek.</strong> Je staat op een afstand van iets hoogs en kijkt "
                  "onder een hoek naar de top. Je afstand is de aanliggende zijde en de hoogte is de overstaande, "
                  "dus je gebruikt de <strong>tangens</strong>. Sta je 20 meter van een gebouw en kijk je onder "
                  "35 graden, dan is 20 maal de tangens van 35 graden ongeveer 14,0 meter. Zit je oog op "
                  "1,6 meter hoogte, dan is het gebouw <strong>15,6 meter</strong> hoog: je ooghoogte komt erbij."),
            ("p", "<strong>Het hoogteverschil uit een hellingshoek.</strong> De lengte van het pad is de schuine "
                  "zijde en de gewonnen hoogte is de overstaande, dus je gebruikt de <strong>sinus</strong>. Een "
                  "bergpad van 500 meter onder 12 graden geeft 500 maal de sinus van 12 graden, ongeveer "
                  "<strong>104 meter</strong> hoogte. Hoe steiler de helling, hoe groter die sinus."),
            ("p", tabel(["Situatie", "Wat je kent", "Wat je gebruikt"], [
                ["hoogte van een boom of gebouw", "afstand en kijkhoek", "tangens"],
                ["hoogte van een vlieger", "touwlengte en hoek met de grond", "sinus"],
                ["hoogte uit een schaduw", "schaduwlengte en zonnehoogte", "tangens"],
                ["hoogteverschil van een pad", "padlengte en hellingshoek", "sinus"],
            ])),
            ("p", "Een vlieger aan 40 meter touw onder 55 graden hangt 40 maal de sinus van 55 graden hoog, "
                  "ongeveer 32,8 meter. Een mast met een schaduw van 12 meter bij een zonnehoogte van 40 graden "
                  "is 12 maal de tangens van 40 graden hoog, ongeveer 10,1 meter."),
            ("p", "Een <strong>hellingspercentage</strong> is de tangens van de hellingshoek, uitgedrukt in "
                  "procent. Acht procent betekent dat je <strong>8 meter stijgt over 100 meter horizontaal</strong>. "
                  "Dat is niet hetzelfde als acht graden: acht procent komt overeen met ongeveer 4,6 graden. "
                  "Honderd procent is wél precies 45 graden, want daar is de tangens 1. Een helling van 25 procent "
                  "komt overeen met ongeveer 14 graden."),
            ("kader", "Een oprit die hoogstens 5 procent mag hellen, stijgt 5 centimeter per meter. Om 30 "
                      "centimeter te overbruggen heb je dus minstens <strong>6 meter</strong> nodig."),
        ]),
    ],
    onthoud=[
        "Overstaande en aanliggende hangen af van de hoek waar je naar kijkt; de schuine zijde niet.",
        "De verhoudingen hangen enkel van de hoek af, want driehoeken met dezelfde hoeken zijn gelijkvormig.",
        "Een sinus van een scherpe hoek blijft onder 1; een tangens kan erboven.",
        "Overstaande = sinus × schuine; overstaande = tangens × aanliggende; schuine = aanliggende ÷ cosinus.",
        "Twee zijden gekend? Deel ze en neem de inverse sinus, cosinus of tangens.",
        "Grondformule: sin²α + cos²α = 1. Uit cosinus 0,96 volgt sinus 0,28.",
        "De twee scherpe hoeken van een rechthoekige driehoek zijn samen 90 graden.",
        "Oplossen betekent alle zijden en hoeken berekenen; met één zijde alleen kan dat niet.",
        "Hoogte uit afstand en kijkhoek: tangens. Hoogte uit padlengte en hellingshoek: sinus.",
        "Een hellingspercentage is de tangens in procent: 8 % is 8 meter op 100 meter horizontaal, niet 8 graden.",
        "Schets eerst, zet je toestel op graden, en rond pas op het einde af.",
    ],
)


# ─────────────────── 8. Stelsels van twee eerstegraadsvergelijkingen
NIEUWE["stelsels-van-twee-eerstegraadsvergelijkingen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Stelsels van twee eerstegraadsvergelijkingen",
    onder="Substitutie, gelijkstelling en combinatie, de koppelvoorstelling, het strijdige stelsel, en wat je op de grafiek ziet.",
    secties=[
        dict(kop="Wat is een stelsel?", blokken=[
            ("p", "Een <strong>stelsel</strong> van twee eerstegraadsvergelijkingen met twee onbekenden zijn twee "
                  "vergelijkingen die <strong>tegelijk</strong> moeten kloppen. Je zoekt dus niet eerst de ene op "
                  "en dan de andere, maar de waarden van x en y waarvoor allebei kloppen."),
            ("p", "De <strong>algemene vorm</strong> van één zo'n vergelijking is <em>ax + by = c</em>. De "
                  "onbekenden staan in de eerste graad, elk met hun eigen <strong>coëfficiënt</strong> ervoor, en "
                  "rechts staat een getal."),
            ("kader", "Eén vergelijking met twee onbekenden kan je niet oplossen. Aan x + y = 5 voldoen oneindig "
                      "veel koppels: (0, 5), (1, 4), (2, 3) … Pas een tweede voorwaarde kiest er één uit."),
        ]),
        dict(kop="De oplossing is een koppel", blokken=[
            ("p", "De oplossingenverzameling schrijf je met een <strong>koppelvoorstelling</strong>: één koppel "
                  "getallen tussen haakjes, met de <strong>x altijd eerst</strong> en de y tweede. Het koppel "
                  "(2, 3) betekent dus dat x gelijk is aan 2 en y aan 3. Daarom zijn (1, 2) en (2, 1) niet "
                  "dezelfde oplossing: de volgorde ligt vast."),
            ("p", "<strong>Controleer altijd in allebei de vergelijkingen.</strong> Neem het stelsel x + y = 5 en "
                  "x − y = 3, en het koppel (4, 1). Dan is 4 plus 1 gelijk aan 5, en 4 min 1 gelijk aan 3. "
                  "Allebei kloppen, dus (4, 1) is de oplossing."),
            ("p", "Invullen kost weinig tijd en vangt de meeste rekenfouten. Klopt je koppel maar in één van de "
                  "twee vergelijkingen, dan is het geen oplossing van het stelsel."),
        ]),
        dict(kop="Substitutie: invullen", blokken=[
            ("p", "Bij de <strong>substitutiemethode</strong> schrijf je uit één vergelijking één onbekende alleen, "
                  "en die uitdrukking vul je in de andere vergelijking in. Substitueren betekent letterlijk "
                  "vervangen."),
            ("p", "Neem y = 2x en x + y = 9. Vul y is 2x in de tweede vergelijking in: x plus 2x is 3x, en 3x is 9, "
                  "dus <strong>x is 3</strong>. Dan is y gelijk aan 6, en de oplossing is het koppel (3, 6)."),
            ("p", "Staat er nergens een onbekende alleen, dan maak je er zelf een vrij. Uit 2x + y = 7 haal je "
                  "y = 7 − 2x: je brengt 2x naar de andere kant, en wat je links aftrekt, trek je ook rechts af. "
                  "Je kiest zelf welke onbekende je uitschrijft; neem er bij voorkeur een met coëfficiënt 1."),
            ("p", "Staat er al een onbekende vast, dan is het nog korter. Bij x = 5 en 2x + y = 13 vul je 5 in: "
                  "2 maal 5 is 10, en 10 plus y is 13, dus y is 3."),
        ]),
        dict(kop="Gelijkstelling: twee keer hetzelfde", blokken=[
            ("p", "Bij de <strong>gelijkstellingsmethode</strong> schrijf je in allebei de vergelijkingen dezelfde "
                  "onbekende uit, en dan stel je die twee uitdrukkingen aan elkaar gelijk. Staat er twee keer "
                  "<em>y is iets</em>, dan moeten die twee uitdrukkingen wel even groot zijn."),
            ("p", "Neem y = x + 1 en y = 3x − 5. Dan is x plus 1 gelijk aan 3x min 5, dus 6 is 2x en "
                  "<strong>x is 3</strong>. Vul in: y is 4. De oplossing is het koppel (3, 4)."),
        ]),
        dict(kop="Combinatie: iets laten wegvallen", blokken=[
            ("p", "Bij de <strong>combinatiemethode</strong> tel je de twee vergelijkingen op of trek je ze van "
                  "elkaar af, zo dat één onbekende wegvalt. Daarvoor moet die onbekende in beide vergelijkingen "
                  "dezelfde coëfficiënt hebben. Is dat niet zo, dan mag je een vergelijking langs beide kanten met "
                  "hetzelfde getal vermenigvuldigen; ze blijft dan gelijkwaardig."),
            ("p", tabel(["Stelsel", "Wat je doet", "Wat je vindt"], [
                ["x + y = 10 en x − y = 4", "optellen, de y valt weg", "2x is 14, dus x is 7 en y is 3"],
                ["2x + y = 8 en 2x − y = 4", "aftrekken, de x valt weg", "2y is 4, dus y is 2 en x is 3"],
            ])),
            ("p", "Welke methode je kiest, hangt af van hoe het stelsel eruitziet. Staat er ergens al een onbekende "
                  "alleen, dan is <strong>substitutie</strong> het snelst. Heeft een onbekende in allebei de "
                  "vergelijkingen dezelfde coëfficiënt, dan valt ze met <strong>combinatie</strong> in één stap weg."),
        ]),
        dict(kop="Drie soorten stelsels", blokken=[
            ("p", "Niet elk stelsel heeft precies één oplossing. Er zijn er drie soorten, en je herkent ze aan wat "
                  "er overblijft als je alles hebt weggewerkt."),
            ("p", tabel(["Soort", "Wat je uitkomt", "Oplossingenverzameling"], [
                ["bepaald", "één waarde voor x en één voor y", "één koppel"],
                ["strijdig", "iets als 0 = 7, wat nooit klopt", "de lege verzameling"],
                ["onbepaald", "0 = 0, een ware uitspraak", "oneindig veel koppels"],
            ])),
            ("p", "Een <strong>strijdig</strong> stelsel heeft geen enkele oplossing: de twee vergelijkingen "
                  "spreken elkaar tegen. Bij x + y = 5 en x + y = 8 kan dezelfde som niet tegelijk 5 en 8 zijn. "
                  "Werk je het uit, dan krijg je 0 is 3, en dat klopt nooit."),
            ("p", "Een <strong>onbepaald</strong> stelsel heeft er oneindig veel. Bij x + y = 5 en 2x + 2y = 10 is "
                  "de tweede vergelijking gewoon de eerste maal twee. Ze zeggen hetzelfde, dus elk koppel dat aan "
                  "de eerste voldoet, voldoet ook aan de tweede."),
        ]),
        dict(kop="Wat je op de grafiek ziet", blokken=[
            ("p", "Elke vergelijking van het stelsel is de vergelijking van een <strong>rechte</strong>. De "
                  "oplossing van het stelsel zijn de punten die de twee rechten gemeen hebben. Daarom kan je een "
                  "stelsel ook grafisch oplossen: teken de twee rechten en lees het <strong>snijpunt</strong> af."),
            ("p", tabel(["Op de grafiek", "Het stelsel"], [
                ["twee snijdende rechten", "bepaald: precies één oplossing"],
                ["twee evenwijdige rechten", "strijdig: geen enkele oplossing"],
                ["twee samenvallende rechten", "onbepaald: oneindig veel oplossingen"],
            ])),
            ("p", "Twee rechten met dezelfde richtingscoëfficiënt maar een ander snijpunt met de y-as zijn "
                  "<strong>evenwijdig</strong>. Ze blijven even ver van elkaar en snijden elkaar nergens, dus dat "
                  "stelsel is strijdig."),
            ("kader", "Tekenen geeft een goede schatting van het snijpunt, maar niet altijd een exact antwoord. "
                      "Reken je grafisch gevonden koppel dus na, of laat de grafiek tekenen wanneer de getallen "
                      "lastig zijn."),
        ]),
        dict(kop="Vraagstukken", blokken=[
            ("p", "Schrijf altijd eerst op <strong>wat x en wat y voorstelt</strong>. Zonder die afspraak weet je "
                  "achteraf niet wat je uitkomst betekent, en kan niemand je oplossing volgen."),
            ("p", "Het aantal stuks komt vóór de onbekende. Kosten twee kaarten en drie broodjes samen 13 euro, "
                  "met k de prijs van een kaart en b die van een broodje, dan is dat <strong>2k + 3b = 13</strong>."),
            ("p", tabel(["Vraagstuk", "Het stelsel", "De oplossing"], [
                ["twee broodjes en een soep kosten 9 euro, een broodje en een soep 6 euro",
                 "2b + s = 9 en b + s = 6", "aftrekken geeft b is 3 euro, dus s is 3 euro"],
                ["een klas van 25 telt 7 jongens meer dan meisjes",
                 "j + m = 25 en j − m = 7", "optellen geeft 2j is 32, dus 16 jongens en 9 meisjes"],
            ])),
        ]),
    ],
    onthoud=[
        "Een stelsel is twee vergelijkingen die tegelijk moeten kloppen; de algemene vorm is ax + by = c.",
        "De oplossing is een koppel (x, y): x eerst, y tweede, dus (1, 2) is niet (2, 1).",
        "Controleer je koppel altijd in allebei de vergelijkingen.",
        "Substitutie: schrijf één onbekende uit en vul ze in de andere vergelijking in.",
        "Gelijkstelling: schrijf in allebei dezelfde onbekende uit en stel de uitdrukkingen gelijk.",
        "Combinatie: tel op of trek af zodat een onbekende wegvalt; vermenigvuldigen mag, langs beide kanten.",
        "0 = 7 betekent strijdig, en de oplossingenverzameling is de lege verzameling.",
        "0 = 0 betekent onbepaald: oneindig veel oplossingen.",
        "Snijdende rechten: één oplossing. Evenwijdig: strijdig. Samenvallend: oneindig veel.",
        "Schrijf bij een vraagstuk eerst op wat x en wat y voorstelt.",
    ],
)


# ─────────────────── 10. Tekenverloop, verloopschema en grafisch oplossen
NIEUWE["tekenverloop-verloopschema-en-grafisch-oplossen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Tekenverloop, verloopschema en grafisch oplossen",
    onder="Nulwaarden, het teken en het verloop van een functie, intervallen op een getallenas, en twee grafieken naast elkaar.",
    secties=[
        dict(kop="De nulwaarde", blokken=[
            ("p", "De <strong>nulwaarde</strong> van een functie is de x-waarde waarvoor de functiewaarde nul is. "
                  "Op de grafiek is dat de x van het punt waar ze de <strong>x-as snijdt</strong>. f(x) = 0 "
                  "oplossen is dus hetzelfde als die snijpunten zoeken."),
            ("p", tabel(["Functie", "Vergelijking", "Nulwaarde"], [
                ["f(x) = 2x − 6", "2x − 6 = 0, dus 2x = 6", "x = 3"],
                ["f(x) = 3x + 12", "3x + 12 = 0, dus 3x = −12", "x = −4"],
            ])),
            ("p", "Verwar de nulwaarde niet met het <strong>snijpunt met de y-as</strong>. Daar vul je nul in voor "
                  "x en bereken je f(0). Bij de nulwaarde stel je de functiewaarde gelijk aan nul en zoek je de x. "
                  "Dat zijn twee verschillende vragen."),
            ("p", "Een eerstegraadsfunctie waarvan de richtingscoëfficiënt niet nul is, is een schuine rechte, en "
                  "die snijdt de x-as in <strong>precies één punt</strong>. Een constante functie zoals f(x) = 5 "
                  "is een horizontale rechte op hoogte 5 en heeft dus <strong>geen</strong> nulwaarde."),
        ]),
        dict(kop="Het tekenverloop", blokken=[
            ("p", "Een <strong>tekenverloop</strong> is een schema dat toont waar de functiewaarde positief is en "
                  "waar ze negatief is. Het gaat enkel over het teken: een <strong>plusteken</strong> of een <strong>minteken</strong>. Hoe groot de waarde daar is, "
                  "staat er niet in."),
            ("p", "De nulwaarden zijn de <strong>grenzen</strong> van het schema. Onder een nulwaarde zet je een "
                  "<strong>nul</strong>, want daar is de functiewaarde precies nul, en dus niet positief en niet "
                  "negatief. Tussen twee grenzen blijft het teken hetzelfde."),
            ("p", tabel(["Functie", "Negatief", "Nul", "Positief"], [
                ["f(x) = 2x − 6 (stijgt)", "links van 3", "in 3", "rechts van 3"],
                ["f(x) = −x + 4 (daalt)", "rechts van 4", "in 4", "links van 4"],
                ["f(x) = 5", "nergens", "nergens", "overal"],
            ])),
            ("p", "Bij een stijgende rechte ligt het positieve stuk dus <strong>rechts</strong> van de nulwaarde, "
                  "bij een dalende rechte <strong>links</strong>. Dat is precies waarom het antwoord op een "
                  "ongelijkheid ervan afhangt of de rechte stijgt of daalt. Teken haar even, dan zie je het meteen."),
            ("p", "Om een tekenverloop van een grafiek af te lezen, kijk je naar twee dingen: waar de nulwaarden "
                  "liggen, en aan welke kant daarvan de grafiek boven of onder de x-as loopt."),
            ("kader", "<strong>Stijgen is niet hetzelfde als positief zijn.</strong> Stijgen gaat over de richting "
                      "van de grafiek, positief zijn over haar ligging ten opzichte van de x-as. Een stijgende "
                      "rechte begint links van haar nulwaarde onder de x-as en is daar dus negatief, terwijl ze al "
                      "aan het stijgen is."),
        ]),
        dict(kop="Het verloopschema", blokken=[
            ("p", "Een <strong>verloopschema</strong> toont iets anders: waar de functie <strong>stijgt</strong> "
                  "en waar ze <strong>daalt</strong>. Je tekent het met pijltjes omhoog en omlaag."),
            ("p", "Bij een rechte is dat schema kort. Een rechte verandert nergens van richting: heeft ze een "
                  "positieve richtingscoëfficiënt, dan is het één pijl die over de hele getallenas omhoog wijst. "
                  "Is de richtingscoëfficiënt negatief, dan wijst één pijl overal omlaag."),
        ]),
        dict(kop="Intervallen en de getallenas", blokken=[
            ("p", "De oplossing van een ongelijkheid is meestal geen enkel getal maar een <strong>heel stuk</strong> "
                  "van de getallenas. Daarom schrijf je ze als een <strong>interval</strong>, of arceer je ze op een "
                  "getallenas."),
            ("p", tabel(["In woorden", "Als interval", "Op de getallenas"], [
                ["alle x groter dan 3", "]3, +∞[", "open bolletje op 3, alles rechts gearceerd"],
                ["alle x groter dan of gelijk aan 3", "[3, +∞[", "vol bolletje op 3, alles rechts gearceerd"],
                ["alle x tussen 1 en 4, grenzen niet mee", "]1, 4[", "twee open bolletjes, het stuk ertussen"],
            ])),
            ("p", "Een haakje naar buiten betekent dat die grens er <strong>niet</strong> bij hoort, en dan zet je "
                  "op de getallenas een open bolletje. Een haakje naar binnen neemt de grens wél mee, en dan wordt "
                  "het bolletje vol. Bij f(x) ≥ 0 staat het gelijkheidsteken erbij, dus telt de nulwaarde zelf mee "
                  "en sluit het haakje. Bij oneindig, het <strong>oneindigteken</strong> ∞, staat het haakje <strong>altijd</strong> open: "
                  "oneindig is geen getal dat je kan bereiken."),
        ]),
        dict(kop="Twee functies naast elkaar", blokken=[
            ("p", "Heb je twee functies f en g, dan gaat het om hun <strong>gemeenschappelijke punten</strong> en "
                  "hun <strong>onderlinge ligging</strong>."),
            ("p", tabel(["Je lost op", "Op de grafiek"], [
                ["f(x) = g(x)", "je zoekt de gemeenschappelijke punten van de twee grafieken"],
                ["f(x) > g(x)", "je zoekt waar de grafiek van f boven die van g ligt"],
                ["f(x) < g(x)", "je zoekt waar de grafiek van f onder die van g ligt"],
            ])),
            ("p", "Neem f(x) = x + 1 en g(x) = 3x − 5. Dan is x plus 1 gelijk aan 3x min 5, dus 6 is 2x en "
                  "<strong>x is 3</strong>; de functiewaarde daar is 4. Het snijpunt is de <strong>grens</strong>: "
                  "aan de ene kant ervan loopt f hoger, aan de andere kant g. Snijden ze in x = 2 en ligt f er "
                  "links van lager, dan is de oplossingenverzameling van f(x) ≤ g(x) gelijk aan ]−∞, 2], want in 2 "
                  "zelf zijn ze gelijk en dat gelijkheidsteken sluit het haakje."),
            ("p", "Niet elke opgave van de vorm f(x) = g(x) heeft precies één oplossing. Bij evenwijdige rechten "
                  "is er geen enkele, en bij samenvallende rechten zijn er oneindig veel. Ligt de grafiek van f "
                  "overal boven die van g, dan hebben ze geen enkel punt gemeen en is er dus geen oplossing. Twee "
                  "<strong>verschillende</strong> rechten kunnen elkaar nooit in twee punten snijden, want door "
                  "twee punten gaat maar één rechte."),
            ("weetje", "Twee grafieken kunnen elkaar snijden zonder dat een van beide de x-as snijdt: twee schuine "
                       "rechten die in het getoonde stuk allebei boven de x-as blijven, kruisen elkaar toch."),
        ]),
        dict(kop="Een vraagstuk grafisch oplossen", blokken=[
            ("p", "Je mag een vraagstuk grafisch oplossen <strong>zonder de vergelijking of de ongelijkheid zelf "
                  "op te schrijven</strong>. Je maakt van elke situatie een grafiek en leest af welke boven de "
                  "andere ligt. Bij eenvoudige opgaven teken je zelf; bij moeilijkere vraagstukken met lastige "
                  "getallen laat je de grafieken met een <strong>hulpmiddel</strong> tekenen en lees je daar af."),
            ("p", "<strong>Voorbeeld.</strong> Een fietsenwinkel heeft kosten K(x) = 300 + 20x en opbrengst "
                  "O(x) = 50x. De twee rechten snijden elkaar bij 10 fietsen: daar is alles 500 euro. Dat is het "
                  "<strong>break-evenpunt</strong> of <strong>omslagpunt</strong>, waar de winst nul is. Pas vanaf de <strong>elfde</strong> fiets "
                  "ligt de opbrengst erboven en is er winst."),
            ("p", "In een woordprobleem betekent een snijpunt dus altijd hetzelfde: de situatie waarin de twee "
                  "grootheden <strong>even groot</strong> zijn. Twee abonnementen die evenveel kosten, kosten en "
                  "opbrengst die gelijk zijn, twee tanks met evenveel water erin."),
            ("p", "Ligt een grafiek tussen x = 1 en x = 4 onder de x-as en daarbuiten erboven, dan is f(x) kleiner "
                  "dan nul op ]1, 4[: enkel tussen de twee nulwaarden, en in 1 en 4 zelf is de functiewaarde precies "
                  "nul."),
            ("kader", "Een grafiek helpt omdat je meteen ziet aan welke kant van de grens de oplossing ligt. Wie "
                      "enkel rekent, vergeet makkelijk het ongelijkheidsteken om te draaien. Maar aflezen is "
                      "schatten: je zit makkelijk een half hokje verkeerd, dus reken een snijpunt na."),
        ]),
    ],
    onthoud=[
        "De nulwaarde is de x waarvoor f(x) nul is: het snijpunt met de x-as.",
        "f(0) is het snijpunt met de y-as; dat is iets anders dan de nulwaarde.",
        "Een tekenverloop toont waar de functie positief en waar ze negatief is, met een nul onder elke nulwaarde.",
        "Een verloopschema toont waar ze stijgt en waar ze daalt; bij een rechte is dat één pijl.",
        "Stijgen gaat over de richting, positief zijn over de ligging ten opzichte van de x-as.",
        "Een stijgende rechte is positief rechts van haar nulwaarde, een dalende links.",
        "Open haakje en open bolletje: de grens telt niet mee. Vol bolletje: ze telt wel mee.",
        "Bij ∞ staat het haakje altijd open.",
        "f(x) = g(x) zoekt de gemeenschappelijke punten; f(x) > g(x) zoekt waar f boven g ligt.",
        "Twee verschillende rechten snijden elkaar in hoogstens één punt.",
        "Het break-evenpunt is waar kosten en opbrengst gelijk zijn; de winst begint erna.",
    ],
)


# ─────────────────── 13. Misleiding met cijfers en grafieken
NIEUWE["misleiding-met-cijfers-en-grafieken" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Misleiding met cijfers en grafieken",
    onder="Assen, schaal en vorm, wat er weggelaten wordt, percentages en procentpunt, en welk middelpunt iemand kiest.",
    secties=[
        dict(kop="Kijk eerst naar de assen", blokken=[
            ("p", "De meeste misleiding met grafieken zit in de <strong>assen</strong>. Daar kijk je dus als "
                  "eerste, nog voor je naar de staven of de lijn kijkt. Zeker bij een grafiek die je op sociale media tegenkomt, zonder de cijfers erbij."),
            ("p", "De <strong>verticale as</strong> van een staafdiagram hoort in principe <strong>bij nul te beginnen</strong>. De hoogte van een "
                  "staaf stelt de grootte voor, dus knip je het onderste stuk weg, dan klopt de verhouding tussen "
                  "de staven niet meer. Begint de as bij 90, dan lijken kleine verschillen veel groter dan ze zijn."),
            ("p", "Een as kan ook <strong>foutief geijkt</strong> zijn. Loopt ze van 0 naar 10 naar 100 naar 1000 "
                  "met gelijke tussenafstanden, dan staan gelijke afstanden niet voor gelijke verschillen. Of er "
                  "worden stukken <strong>overgeslagen</strong>: slaat een tijdas de jaren 2019 en 2020 over, dan "
                  "loopt de lijn vlakker of steiler dan het verloop echt was. Ontbrekende stukken hoor je te tonen, "
                  "bijvoorbeeld met een breukteken."),
            ("p", "Ten slotte kan een grafiek <strong>ongepast geschaald</strong> zijn. Dat merk je goed bij een <strong>lijndiagram</strong>: dezelfde cijfers in een "
                  "smalle grafiek geven een veel dramatischer beeld dan in een brede: de lijn lijkt steiler en de "
                  "verandering heftiger. Twee grafieken naast elkaar met een verschillende schaal mag je daarom "
                  "niet zomaar met elkaar vergelijken; kijk eerst naar hun assen."),
            ("kader", "Een as die niet bij nul begint, is niet altijd bedrog. Bij lichaamstemperatuur of bij "
                      "beurskoersen is inzoomen zinvol. Het moet dan wel <strong>duidelijk aangegeven</strong> staan."),
        ]),
        dict(kop="De vorm van het beeld", blokken=[
            ("p", "Ook zonder aan de assen te raken kan een beeld je oog sturen."),
            ("p", tabel(["Ingreep", "Wat er gebeurt"], [
                ["een cirkeldiagram in drie dimensies", "de sectoren vooraan krijgen meer oppervlakte en lijken groter"],
                ["een plaatje twee keer zo breed én zo hoog", "de oppervlakte wordt vier keer zo groot bij een verdubbeling"],
                ["staven die niet even breed zijn", "de bredere staven trekken meer aandacht dan hun waarde verdient"],
            ])),
            ("p", "Een verdubbeling tonen met een plaatje dat vier keer zo veel plaats inneemt, heet "
                  "<strong>uitvergroten</strong>; die ingreep heet een <strong>uitvergroting</strong>. In een staafdiagram hoort enkel de <strong>hoogte</strong> iets "
                  "te betekenen; verschil in breedte voegt een tweede signaal toe dat er niet is."),
            ("p", "Een cirkeldiagram toont delen van <strong>één</strong> geheel: alle sectoren horen bij dezelfde "
                  "groep en dezelfde periode. Zet iemand er een stuk bij dat van elders komt, dan stelt de cirkel "
                  "niets meer voor."),
            ("p", "Verder hoort een grafiek een <strong>titel</strong>, <strong>namen bij de assen</strong>, een "
                  "<strong>legende</strong> bij meerdere reeksen en een <strong>bron</strong> te hebben. Een legende legt uit waar elke kleur of elk symbool voor staat. Zonder "
                  "namen weet je niet wat er gemeten is of in welke eenheid; zonder legende niet welke lijn bij "
                  "welke groep hoort; zonder bron kan je niet nagaan of de cijfers kloppen. Let er ook op of de "
                  "onderdelen <strong>correct benoemd</strong> zijn: zet iemand 'omzet' naast 'winst' in hetzelfde "
                  "diagram, dan vergelijkt hij twee verschillende grootheden, en omzet is altijd groter dan winst."),
        ]),
        dict(kop="Wat er níét staat", blokken=[
            ("p", "Een van de sterkste manieren om te misleiden is <strong>informatie of data weglaten</strong>. "
                  "Wat je niet toont, kan de lezer ook niet wegen. Toont een grafiek enkel de vier beste maanden "
                  "van het jaar, dan klopt elk getal en klopt het verhaal toch niet."),
            ("p", "Hetzelfde geldt voor een aantal zonder het <strong>totaal</strong> erbij. Een stijging van 2 "
                  "naar 4 zegt iets heel anders bij een groep van 10 mensen dan bij een groep van 10 000. Vraag "
                  "dus altijd welke periode, welke groep of welk totaal ontbreekt."),
        ]),
        dict(kop="Percentages, en het verschil met procentpunt", blokken=[
            ("p", "Hier worden de meeste fouten gemaakt, en niet altijd met opzet."),
            ("p", tabel(["Woord", "Wat het meet", "Van 4 % naar 6 %"], [
                ["procentpunt", "het gewone verschil tussen twee percentages", "2 procentpunt"],
                ["procent", "de verandering ten opzichte van het startgetal", "50 procent"],
            ])),
            ("p", "Van 4 naar 6 procent is er 2 procentpunt bij gekomen. Maar ten opzichte van de 4 waar je van "
                  "vertrok, is dat de helft meer, dus een <strong>relatieve</strong> stijging van 50 procent. Wie "
                  "de twee woorden verwisselt, maakt een cijfer veel groter of kleiner dan het is."),
            ("p", "Twee kortingen na elkaar mag je <strong>niet</strong> optellen. Een jas van 100 euro met eerst "
                  "20 procent en dan nog eens 10 procent korting kost 80 euro en daarna 72 euro: dat is samen "
                  "<strong>28</strong> procent korting, niet 30. Om dezelfde reden brengt een prijs die eerst 10 "
                  "procent stijgt en daarna 10 procent daalt je niet terug bij het begin: 100 wordt 110, en 10 "
                  "procent van 110 is 11, dus je eindigt op 99."),
            ("p", "Let ook op de woorden rond het getal. <strong>'Tot 70 procent korting'</strong> zet enkel een "
                  "bovengrens: misschien haalt één artikel die korting en de rest veel minder. Een winst die "
                  "<strong>'met 200 procent groeide'</strong> is verdrievoudigd, want er kwam twee keer het "
                  "oorspronkelijke bedrag bij. En bij <strong>'het risico verdubbelt'</strong> wil je vooral weten "
                  "hoe groot dat risico eerst was: van 1 op een miljoen naar 2 op een miljoen is ook een "
                  "verdubbeling."),
            ("kader", "Een percentage zonder het aantal waarop het slaat, zegt weinig. Honderd procent van twee "
                      "mensen klinkt indrukwekkend en stelt niets voor."),
        ]),
        dict(kop="Welk middelpunt toont iemand?", blokken=[
            ("p", "Het <strong>rekenkundig gemiddelde</strong> telt elk getal mee met zijn volle grootte, dus één "
                  "uitschieter trekt het ver weg. De <strong>mediaan</strong> is gewoon het middelste getal van de "
                  "reeks op volgorde, en die verschuift daar nauwelijks door. Bij een even aantal getallen neem je "
                  "het gemiddelde van de twee middelste."),
            ("p", "Neem een bedrijf waar vier mensen 2000 euro verdienen en één persoon 12 000 euro."),
            ("p", tabel(["Maat", "Berekening", "Uitkomst"], [
                ["rekenkundig gemiddelde", "20 000 euro gedeeld door 5 mensen", "4000 euro"],
                ["mediaan", "het derde getal van 2000, 2000, 2000, 2000, 12 000", "2000 euro"],
            ])),
            ("p", "Adverteert dat bedrijf met <em>bij ons verdien je gemiddeld 4000 euro</em>, dan klopt het getal "
                  "en beschrijft het niemand: vier van de vijf werknemers verdienen veel minder. Allebei de "
                  "getallen zijn juist. Wie de lonen hoog wil laten lijken, toont het gemiddelde; wie ze laag wil laten lijken, de mediaan. <strong>Wie kiest welk getal hij toont, stuurt daarmee het verhaal.</strong>"),
        ]),
        dict(kop="Wie zegt het, en aan wie is het gevraagd?", blokken=[
            ("p", "Bij elk cijfer horen twee vragen die niets met rekenen te maken hebben."),
            ("p", "<strong>Aan wie is het gevraagd?</strong> Wie je bevraagt, bepaalt je antwoord. Een enquête over "
                  "sportgewoontes die enkel aan de ingang van een fitnesszaal wordt afgenomen, levert een groep op "
                  "die per definitie meer sport dan gemiddeld; die groep is niet <strong>representatief</strong>. "
                  "Bij <em>negen op de tien tandartsen raden dit aan</em> wil je weten hoeveel tandartsen er "
                  "gevraagd zijn, en wie de vraag gesteld heeft."),
            ("p", "<strong>Wie brengt het naar buiten?</strong> Wie belang heeft bij een uitkomst, kan de "
                  "voorstelling kleuren. De cijfers zelf kunnen perfect kloppen terwijl de keuze van de grafiek, "
                  "van de periode of van het middelpunt het verhaal stuurt."),
            ("kader", "Bijna alle misleiding met cijfers gebeurt met <strong>kloppende getallen</strong>. Een "
                      "cijfer dat helemaal juist is, kan dus best een verkeerde indruk geven."),
        ]),
    ],
    onthoud=[
        "Kijk bij elke grafiek eerst naar de assen: waar begint de schaal en is ze gelijkmatig geijkt?",
        "Een staafdiagram hoort bij nul te beginnen; anders lijken kleine verschillen groot.",
        "Een smalle grafiek maakt dezelfde verandering dramatischer: dat is ongepast schalen.",
        "Twee keer zo breed én zo hoog is vier keer zo veel oppervlakte: uitvergroten.",
        "In drie dimensies lijken de sectoren vooraan groter dan ze zijn.",
        "Titel, namen bij de assen, legende en bron horen erbij.",
        "Wat weggelaten is, kan je niet wegen: vraag welke periode of welke groep ontbreekt.",
        "Procentpunt is het verschil tussen twee percentages, procent de verandering ten opzichte van het begin.",
        "Twee kortingen na elkaar tel je niet op: 20 % en dan 10 % is samen 28 %.",
        "Met 200 procent groeien is verdrievoudigen, niet verdubbelen.",
        "Eén uitschieter trekt het gemiddelde weg; de mediaan blijft het middelste getal.",
        "Een cijfer dat klopt, kan toch een verkeerde indruk geven.",
    ],
)

BUNDELS.update(NIEUWE)
controleer(BUNDELS)

VOLGORDE = [
    "een-opgave-aanpakken-van-context-naar-wiskunde",
    "reele-getallen-wortels-en-machten",
    "ordenen-afronden-en-intervallen",
    "rechten-vlakken-en-gelijkvormigheid",
    "pythagoras-en-de-rechthoekige-driehoek",
    "de-rechthoekige-driehoek-oplossen-en-toepassen",
    "formules-omvormen-en-eerstegraadsvergelijkingen",
    "stelsels-van-twee-eerstegraadsvergelijkingen",
    "functies-en-de-rechte",
    "tekenverloop-verloopschema-en-grafisch-oplossen",
    "telproblemen-met-boom-en-venndiagram",
    "statistiek-voorstellingen-centrum-en-spreiding",
    "misleiding-met-cijfers-en-grafieken",
]
verwacht = {k + NIEUW for k in VOLGORDE}
if set(BUNDELS) != verwacht:
    raise SystemExit(
        "De bundels komen niet overeen met de dertien thema's:\n"
        f"  te veel: {sorted(set(BUNDELS) - verwacht)}\n"
        f"  te weinig: {sorted(verwacht - set(BUNDELS))}"
    )
BUNDELS = {k + NIEUW: BUNDELS[k + NIEUW] for k in VOLGORDE}

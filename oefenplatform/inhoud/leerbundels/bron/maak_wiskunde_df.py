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
import svg
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
    ("ordenen-afronden-en-intervallen", "Wetenschappelijke notatie: één cijfer van \\(1\\) tot \\(9\\) voor de komma, maal een macht van tien."),
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
            ("fig", svg.goniodriehoek(),
             "Vanuit de hoek alfa gezien heet elke zijde anders."),
            ("p", "De <strong>schuine zijde</strong> (de hypotenusa) ligt tegenover de rechte hoek en is altijd "
                  "de langste zijde. De twee andere heten <strong>rechthoekszijden</strong>. Welke van die twee "
                  "de overstaande en welke de aanliggende is, hangt af van de hoek waar je naar kijkt."),
            ("p", tabel(["Zijde", r"Hoe je ze herkent bij hoek \(\alpha\)"], [
                ["schuine zijde", r"ligt tegenover de rechte hoek, en dus nooit tegenover \(\alpha\)"],
                ["overstaande zijde", r"de rechthoekszijde die tegenover \(\alpha\) ligt"],
                ["aanliggende zijde", r"de rechthoekszijde die tegen \(\alpha\) aan ligt"],
            ])),
            ("kader", r"Twee zijden raken hoek \(\alpha\): de schuine zijde en een rechthoekszijde. Met "
                      r"<strong>aanliggende zijde</strong> bedoelen we altijd die rechthoekszijde. Kijk je naar de "
                      r"andere scherpe hoek, dan wisselen overstaande en aanliggende van plaats."),
            ("p", "De drie verhoudingen hangen enkel van de <strong>hoek</strong> af, niet van hoe groot je de "
                  "driehoek tekent. Twee driehoeken met dezelfde hoeken zijn immers <strong>gelijkvormig</strong>: "
                  "alle zijden worden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg."),
        ]),
        dict(kop="De drie verhoudingen in cijfers", blokken=[
            ("p", r"Neem de driehoek met zijden \(3\), \(4\) en \(5\), en kijk naar de hoek tegenover de zijde "
                  r"\(3\). Dan is de overstaande zijde \(3\), de aanliggende \(4\) en de schuine \(5\)."),
            ("p", tabel(["Verhouding", "Breuk", "Uitkomst"], [
                [r"\(\sin \alpha\)", r"\(\frac{\text{overstaande}}{\text{schuine}} = \frac{3}{5}\)", r"\(0{,}6\)"],
                [r"\(\cos \alpha\)", r"\(\frac{\text{aanliggende}}{\text{schuine}} = \frac{4}{5}\)", r"\(0{,}8\)"],
                [r"\(\tan \alpha\)", r"\(\frac{\text{overstaande}}{\text{aanliggende}} = \frac{3}{4}\)", r"\(0{,}75\)"],
            ])),
            ("p", r"Bij de sinus en de cosinus deel je door de schuine zijde, en die is altijd de langste. Een "
                  r"<strong>sinus van een scherpe hoek is dus altijd kleiner dan \(1\)</strong>. Bij de tangens komt "
                  r"de schuine zijde niet voor, en daarom <strong>kan een tangens wél groter zijn dan \(1\)</strong>."),
            ("p", r"Bij een hoek van <strong>\(45^{\circ}\)</strong> zijn de twee rechthoekszijden even lang, dus "
                  r"geldt daar \(\sin 45^{\circ} = \cos 45^{\circ}\) en is \(\tan 45^{\circ} = 1\)."),
            ("weetje", "Een goniometrisch getal van een scherpe hoek is nooit negatief: je deelt twee lengtes door "
                       "elkaar, en een lengte is altijd positief."),
        ]),
        dict(kop="Een zijde zoeken", blokken=[
            ("p", "Kies de verhouding waarin de zijde die je kent én de zijde die je zoekt allebei voorkomen. "
                  "Dan blijft er één onbekende over."),
            ("p", tabel(["Je kent", "Je zoekt", "Je rekent"], [
                ["hoek en schuine zijde", "overstaande zijde", r"\(\sin \alpha \cdot \text{schuine}\)"],
                ["hoek en schuine zijde", "aanliggende zijde", r"\(\cos \alpha \cdot \text{schuine}\)"],
                ["hoek en aanliggende zijde", "overstaande zijde", r"\(\tan \alpha \cdot \text{aanliggende}\)"],
                ["hoek en aanliggende zijde", "schuine zijde", r"\(\frac{\text{aanliggende}}{\cos \alpha}\)"],
            ])),
            ("p", r"<strong>Voorbeeld.</strong> Een ladder van \(6\) meter staat onder \(60^{\circ}\) met de grond. "
                  r"De hoogte die hij bereikt is de overstaande zijde: \(6 \cdot \sin 60^{\circ} \approx "
                  r"5{,}20\) meter. De afstand van zijn voet tot de muur is de aanliggende zijde: "
                  r"\(6 \cdot \cos 60^{\circ} = 6 \cdot 0{,}5 = 3\) meter."),
            ("p", r"<strong>Nog een.</strong> Is \(\sin \alpha = 0{,}5\) en de schuine zijde \(10\), dan is de "
                  r"overstaande zijde \(0{,}5 \cdot 10 = 5\)."),
        ]),
        dict(kop="Een hoek zoeken", blokken=[
            ("p", "Ken je twee zijden, dan reken je eerst hun verhouding uit en gebruik je daarna de "
                  "<strong>inverse</strong> van het bijbehorende goniometrische getal op je rekentoestel."),
            ("p", tabel(["Je kent", "Je deelt", "Je gebruikt"], [
                ["overstaande en schuine zijde", r"\(\frac{\text{overstaande}}{\text{schuine}}\)", r"\(\sin^{-1}\)"],
                ["aanliggende en schuine zijde", r"\(\frac{\text{aanliggende}}{\text{schuine}}\)", r"\(\cos^{-1}\)"],
                ["de twee rechthoekszijden", r"\(\frac{\text{overstaande}}{\text{aanliggende}}\)", r"\(\tan^{-1}\)"],
            ])),
            ("p", r"Ken je één goniometrisch getal, dan haal je het andere uit de <strong>grondformule</strong> "
                  r"\(\sin^{2}\alpha + \cos^{2}\alpha = 1\). Is \(\cos \alpha = 0{,}96\), dan is "
                  r"\(\sin^{2}\alpha = 1 - 0{,}9216 = 0{,}0784\), en dus \(\sin \alpha = 0{,}28\)."),
            ("p", r"De derde hoek vind je zonder te rekenen met verhoudingen: alle hoeken samen zijn "
                  r"\(180^{\circ}\) en de rechte hoek neemt er al \(90^{\circ}\) in. De twee scherpe hoeken zijn "
                  r"dus <strong>samen \(90^{\circ}\)</strong>. Bij een scherpe hoek van \(30^{\circ}\) is de andere "
                  r"dus \(60^{\circ}\)."),
            ("kader", r"Krijg je voor een scherpe hoek een uitkomst van \(91^{\circ}\), dan zit er een fout in je "
                      r"berekening. In een rechthoekige driehoek blijft elke scherpe hoek onder \(90^{\circ}\)."),
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
            ("p", r"Toont je toestel \(5{,}1962\) en moet je antwoord in centimeters nauwkeurig, rond dan dáár af, "
                  r"niet bij elke tussenstap."),
        ]),
        dict(kop="Kijkhoek, hoogte en helling", blokken=[
            ("p", "Hier komt de leerstof in de echte wereld terecht. Twee situaties komen steeds terug."),
            ("p", r"<strong>De hoogte uit een kijkhoek.</strong> Je staat op een afstand van iets hoogs en kijkt "
                  r"onder een hoek naar de top. Je afstand is de aanliggende zijde en de hoogte is de overstaande, "
                  r"dus je gebruikt de <strong>tangens</strong>. Sta je \(20\) meter van een gebouw en kijk je "
                  r"onder \(35^{\circ}\), dan is \(20 \cdot \tan 35^{\circ} \approx 14{,}0\) meter. Zit je oog op "
                  r"\(1{,}6\) meter hoogte, dan is het gebouw <strong>\(15{,}6\) meter</strong> hoog: je ooghoogte "
                  r"komt erbij."),
            ("p", r"<strong>Het hoogteverschil uit een hellingshoek.</strong> De lengte van het pad is de schuine "
                  r"zijde en de gewonnen hoogte is de overstaande, dus je gebruikt de <strong>sinus</strong>. Een "
                  r"bergpad van \(500\) meter onder \(12^{\circ}\) geeft \(500 \cdot \sin 12^{\circ} \approx 104\) "
                  r"meter hoogte. Hoe steiler de helling, hoe groter die sinus."),
            ("p", tabel(["Situatie", "Wat je kent", "Wat je gebruikt"], [
                ["hoogte van een boom of gebouw", "afstand en kijkhoek", r"\(\tan\)"],
                ["hoogte van een vlieger", "touwlengte en hoek met de grond", r"\(\sin\)"],
                ["hoogte uit een schaduw", "schaduwlengte en zonnehoogte", r"\(\tan\)"],
                ["hoogteverschil van een pad", "padlengte en hellingshoek", r"\(\sin\)"],
            ])),
            ("p", r"Een vlieger aan \(40\) meter touw onder \(55^{\circ}\) hangt \(40 \cdot \sin 55^{\circ} "
                  r"\approx 32{,}8\) meter hoog. Een mast met een schaduw van \(12\) meter bij een zonnehoogte van "
                  r"\(40^{\circ}\) is \(12 \cdot \tan 40^{\circ} \approx 10{,}1\) meter hoog."),
            ("p", r"Een <strong>hellingspercentage</strong> is de tangens van de hellingshoek, uitgedrukt in "
                  r"procent. \(8\,\%\) betekent dat je <strong>\(8\) meter stijgt over \(100\) meter "
                  r"horizontaal</strong>. Dat is niet hetzelfde als \(8^{\circ}\): \(8\,\%\) komt overeen met "
                  r"\(\tan^{-1} 0{,}08 \approx 4{,}6^{\circ}\). \(100\,\%\) is wél precies \(45^{\circ}\), want "
                  r"daar is \(\tan \alpha = 1\). Een helling van \(25\,\%\) komt overeen met ongeveer "
                  r"\(14^{\circ}\)."),
            ("kader", r"Een oprit die hoogstens \(5\,\%\) mag hellen, stijgt \(5\) centimeter per meter. Om "
                      r"\(30\) centimeter te overbruggen heb je dus minstens <strong>\(6\) meter</strong> nodig."),
        ]),
    ],
    onthoud=[
        "Overstaande en aanliggende hangen af van de hoek waar je naar kijkt; de schuine zijde niet.",
        "De verhoudingen hangen enkel van de hoek af, want driehoeken met dezelfde hoeken zijn gelijkvormig.",
        r"\(\sin \alpha\) van een scherpe hoek blijft onder \(1\); \(\tan \alpha\) kan erboven.",
        r"overstaande \(= \sin \alpha \cdot\) schuine; overstaande \(= \tan \alpha \cdot\) aanliggende; schuine \(= \frac{\text{aanliggende}}{\cos \alpha}\).",
        r"Twee zijden gekend? Deel ze en neem \(\sin^{-1}\), \(\cos^{-1}\) of \(\tan^{-1}\).",
        r"Grondformule \(\sin^{2}\alpha + \cos^{2}\alpha = 1\): uit \(\cos \alpha = 0{,}96\) volgt \(\sin \alpha = 0{,}28\).",
        r"De twee scherpe hoeken van een rechthoekige driehoek zijn samen \(90^{\circ}\).",
        "Oplossen betekent alle zijden en hoeken berekenen; met één zijde alleen kan dat niet.",
        r"Hoogte uit afstand en kijkhoek: \(\tan\). Hoogte uit padlengte en hellingshoek: \(\sin\).",
        r"Een hellingspercentage is de tangens in procent: \(8\,\%\) is \(8\) meter op \(100\) meter horizontaal, niet \(8^{\circ}\).",
        "Schets eerst, zet je toestel op graden, en rond pas op het einde af.",
    ],
)


# ─────────────────── 8. Stelsels van twee eerstegraadsvergelijkingen
NIEUWE["stelsels-van-twee-eerstegraadsvergelijkingen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Stelsels van twee eerstegraadsvergelijkingen",
    onder="Substitutie, gelijkstelling en combinatie, de koppelvoorstelling, het strijdige stelsel, en wat je op de grafiek ziet.",
    secties=[
        dict(kop="Wat is een stelsel?", blokken=[
            ("p", r"Een <strong>stelsel</strong> van twee eerstegraadsvergelijkingen met twee onbekenden zijn twee "
                  r"vergelijkingen die <strong>tegelijk</strong> moeten kloppen. Je zoekt dus niet eerst de ene op "
                  r"en dan de andere, maar de waarden van \(x\) en \(y\) waarvoor allebei kloppen."),
            ("p", r"De <strong>algemene vorm</strong> van één zo'n vergelijking is \(ax + by = c\). De onbekenden "
                  r"staan in de eerste graad, elk met hun eigen <strong>coëfficiënt</strong> ervoor, en rechts "
                  r"staat een getal."),
            ("kader", r"Eén vergelijking met twee onbekenden kan je niet oplossen. Aan \(x + y = 5\) voldoen "
                      r"oneindig veel koppels: \((0, 5)\), \((1, 4)\), \((2, 3)\) \(\ldots\) Pas een tweede "
                      r"voorwaarde kiest er één uit."),
        ]),
        dict(kop="De oplossing is een koppel", blokken=[
            ("p", r"De oplossingenverzameling schrijf je met een <strong>koppelvoorstelling</strong>: één koppel "
                  r"getallen tussen haakjes, met de <strong>\(x\) altijd eerst</strong> en de \(y\) tweede. Zo "
                  r"betekent \(V = \{(2, 3)\}\) dat \(x = 2\) en \(y = 3\). Daarom zijn \((1, 2)\) en \((2, 1)\) "
                  r"niet dezelfde oplossing: de volgorde ligt vast."),
            ("p", r"<strong>Controleer altijd in allebei de vergelijkingen.</strong> Neem het stelsel "
                  r"\(x + y = 5\) en \(x - y = 3\), en het koppel \((4, 1)\). Dan is \(4 + 1 = 5\) en "
                  r"\(4 - 1 = 3\). Allebei kloppen, dus \((4, 1)\) is de oplossing."),
            ("p", "Invullen kost weinig tijd en vangt de meeste rekenfouten. Klopt je koppel maar in één van de "
                  "twee vergelijkingen, dan is het geen oplossing van het stelsel."),
        ]),
        dict(kop="Substitutie: invullen", blokken=[
            ("p", "Bij de <strong>substitutiemethode</strong> schrijf je uit één vergelijking één onbekende alleen, "
                  "en die uitdrukking vul je in de andere vergelijking in. Substitueren betekent letterlijk "
                  "vervangen."),
            ("p", r"Neem \(y = 2x\) en \(x + y = 9\). Vul \(y = 2x\) in de tweede vergelijking in: "
                  r"\(x + 2x = 3x\), en \(3x = 9\), dus <strong>\(x = 3\)</strong>. Dan is \(y = 6\), en de "
                  r"oplossing is het koppel \((3, 6)\)."),
        ]),
        dict(kop="Een onbekende vrijmaken", blokken=[
            ("p", r"Staat er nergens een onbekende alleen, dan maak je er zelf een vrij. Uit \(2x + y = 7\) haal "
                  r"je \(y = 7 - 2x\): je brengt \(2x\) naar de andere kant, en wat je links aftrekt, trek je ook "
                  r"rechts af. Je kiest zelf welke onbekende je uitschrijft; neem er bij voorkeur een met "
                  r"coëfficiënt \(1\)."),
            ("p", r"Staat er al een onbekende vast, dan is het nog korter. Bij \(x = 5\) en \(2x + y = 13\) vul je "
                  r"\(5\) in: \(2 \cdot 5 = 10\), en \(10 + y = 13\), dus \(y = 3\)."),
        ]),
        dict(kop="Gelijkstelling: twee keer hetzelfde", blokken=[
            ("p", r"Bij de <strong>gelijkstellingsmethode</strong> schrijf je in allebei de vergelijkingen dezelfde "
                  r"onbekende uit, en dan stel je die twee uitdrukkingen aan elkaar gelijk. Staat er twee keer "
                  r"\(y = \ldots\), dan moeten die twee uitdrukkingen wel even groot zijn."),
            ("p", r"Neem \(y = x + 1\) en \(y = 3x - 5\). Dan is \(x + 1 = 3x - 5\), dus \(6 = 2x\) en "
                  r"<strong>\(x = 3\)</strong>. Vul in: \(y = 4\). De oplossing is het koppel \((3, 4)\)."),
        ]),
        dict(kop="Combinatie: iets laten wegvallen", blokken=[
            ("p", "Bij de <strong>combinatiemethode</strong> tel je de twee vergelijkingen op of trek je ze van "
                  "elkaar af, zo dat één onbekende wegvalt. Daarvoor moet die onbekende in beide vergelijkingen "
                  "dezelfde coëfficiënt hebben. Is dat niet zo, dan mag je een vergelijking langs beide kanten met "
                  "hetzelfde getal vermenigvuldigen; ze blijft dan gelijkwaardig."),
            ("p", tabel(["Stelsel", "Wat je doet", "Wat je vindt"], [
                [r"\(x + y = 10\) en \(x - y = 4\)", r"optellen, de \(y\) valt weg",
                 r"\(2x = 14\), dus \(x = 7\) en \(y = 3\)"],
                [r"\(2x + y = 8\) en \(2x - y = 4\)", r"aftrekken, de \(x\) valt weg",
                 r"\(2y = 4\), dus \(y = 2\) en \(x = 3\)"],
            ])),
            ("p", "Welke methode je kiest, hangt af van hoe het stelsel eruitziet. Staat er ergens al een onbekende "
                  "alleen, dan is <strong>substitutie</strong> het snelst. Heeft een onbekende in allebei de "
                  "vergelijkingen dezelfde coëfficiënt, dan valt ze met <strong>combinatie</strong> in één stap weg."),
        ]),
        dict(kop="Drie soorten stelsels", blokken=[
            ("fig", svg.driestelsels(),
             "Snijden de rechten elkaar, lopen ze naast elkaar, of liggen ze op elkaar?"),
            ("p", "Niet elk stelsel heeft precies één oplossing. Er zijn er drie soorten, en je herkent ze aan wat "
                  "er overblijft als je alles hebt weggewerkt."),
            ("p", tabel(["Soort", "Wat je uitkomt", "Oplossingenverzameling"], [
                ["bepaald", r"één waarde voor \(x\) en één voor \(y\)", "één koppel"],
                ["strijdig", r"iets als \(0 = 7\), wat nooit klopt", r"\(V = \emptyset\)"],
                ["onbepaald", r"\(0 = 0\), een ware uitspraak", "oneindig veel koppels"],
            ])),
            ("p", r"Een <strong>strijdig</strong> stelsel heeft geen enkele oplossing: de twee vergelijkingen "
                  r"spreken elkaar tegen. Bij \(x + y = 5\) en \(x + y = 8\) kan dezelfde som niet tegelijk \(5\) "
                  r"en \(8\) zijn. Werk je het uit, dan krijg je \(0 = 3\), en dat klopt nooit."),
            ("p", r"Een <strong>onbepaald</strong> stelsel heeft er oneindig veel. Bij \(x + y = 5\) en "
                  r"\(2x + 2y = 10\) is de tweede vergelijking gewoon de eerste maal twee. Ze zeggen hetzelfde, "
                  r"dus elk koppel dat aan de eerste voldoet, voldoet ook aan de tweede."),
        ]),
        dict(kop="Wat je op de grafiek ziet", blokken=[
            ("p", "Elke vergelijking is de vergelijking van een <strong>rechte</strong>, en de oplossing zijn "
                  "de punten die ze gemeen hebben: het <strong>snijpunt</strong>."),
            ("p", tabel(["Op de grafiek", "Het stelsel"], [
                ["twee snijdende rechten", "bepaald: precies één oplossing"],
                ["twee evenwijdige rechten", "strijdig: geen enkele oplossing"],
                ["twee samenvallende rechten", "onbepaald: oneindig veel oplossingen"],
            ])),
        ]),
        dict(kop="Evenwijdig, samenvallend of snijdend", blokken=[
            ("p", r"Twee rechten met dezelfde richtingscoëfficiënt maar een ander snijpunt met de \(y\)-as zijn "
                  r"<strong>evenwijdig</strong>. Ze blijven even ver van elkaar en snijden elkaar nergens, dus dat "
                  r"stelsel is strijdig. Vallen ze samen, dan hebben ze ook dezelfde \(q\) en is het stelsel "
                  r"onbepaald. Verschilt de richtingscoëfficiënt, dan snijden ze elkaar altijd ergens."),
            ("kader", "Tekenen geeft een goede schatting van het snijpunt, maar niet altijd een exact antwoord. "
                      "Reken je grafisch gevonden koppel dus na, of laat de grafiek tekenen wanneer de getallen "
                      "lastig zijn."),
        ]),
        dict(kop="Vraagstukken", blokken=[
            ("p", r"Schrijf altijd eerst op <strong>wat \(x\) en wat \(y\) voorstelt</strong>. Zonder die afspraak "
                  r"weet je achteraf niet wat je uitkomst betekent, en kan niemand je oplossing volgen."),
            ("p", r"Het aantal stuks komt vóór de onbekende. Kosten twee kaarten en drie broodjes samen \(13\) "
                  r"euro, met \(k\) de prijs van een kaart en \(b\) die van een broodje, dan is dat "
                  r"<strong>\(2k + 3b = 13\)</strong>."),
            ("p", tabel(["Vraagstuk", "Het stelsel", "De oplossing"], [
                [r"twee broodjes en een soep kosten \(9\) euro, een broodje en een soep \(6\) euro",
                 r"\(2b + s = 9\) en \(b + s = 6\)", r"aftrekken geeft \(b = 3\), dus \(s = 3\) euro"],
                [r"een klas van \(25\) telt \(7\) jongens meer dan meisjes",
                 r"\(j + m = 25\) en \(j - m = 7\)", r"optellen geeft \(2j = 32\), dus \(16\) jongens en \(9\) meisjes"],
                [r"drie koffies en twee thees kosten \(13\) euro, één koffie en twee thees \(7\) euro",
                 r"\(3k + 2t = 13\) en \(k + 2t = 7\)", r"aftrekken geeft \(2k = 6\), dus \(k = 3\) en \(t = 2\) euro"],
            ])),
            ("kader", r"Lees je uitkomst altijd terug in de situatie. Komt er een prijs van \(-4\) euro uit, of "
                      r"\(7{,}5\) leerlingen, dan is er iets misgegaan: een negatieve prijs en een halve leerling "
                      r"bestaan niet, hoe netjes het rekenwerk er ook uitziet."),
        ]),
    ],
    onthoud=[
        r"Een stelsel is twee vergelijkingen die tegelijk moeten kloppen; de algemene vorm is \(ax + by = c\).",
        r"De oplossing is een koppel \((x, y)\): \(x\) eerst, \(y\) tweede, dus \((1, 2)\) is niet \((2, 1)\).",
        "Controleer je koppel altijd in allebei de vergelijkingen.",
        "Substitutie: schrijf één onbekende uit en vul ze in de andere vergelijking in.",
        "Gelijkstelling: schrijf in allebei dezelfde onbekende uit en stel de uitdrukkingen gelijk.",
        "Combinatie: tel op of trek af zodat een onbekende wegvalt; vermenigvuldigen mag, langs beide kanten.",
        r"\(0 = 7\) betekent strijdig, en de oplossingenverzameling is \(V = \emptyset\).",
        r"\(0 = 0\) betekent onbepaald: oneindig veel oplossingen.",
        "Snijdende rechten: één oplossing. Evenwijdig: strijdig. Samenvallend: oneindig veel.",
        r"Schrijf bij een vraagstuk eerst op wat \(x\) en wat \(y\) voorstelt.",
    ],
)


# ─────────────────── 10. Tekenverloop, verloopschema en grafisch oplossen
NIEUWE["tekenverloop-verloopschema-en-grafisch-oplossen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Tekenverloop, verloopschema en grafisch oplossen",
    onder="Nulwaarden, het teken en het verloop van een functie, intervallen op een getallenas, en twee grafieken naast elkaar.",
    secties=[
        dict(kop="De nulwaarde", blokken=[
            ("p", r"De <strong>nulwaarde</strong> van een functie is de \(x\)-waarde waarvoor de functiewaarde "
                  r"nul is. Op de grafiek is dat de \(x\) van het punt waar ze de <strong>\(x\)-as snijdt</strong>. "
                  r"\(f(x) = 0\) oplossen is dus hetzelfde als die snijpunten zoeken."),
            ("p", tabel(["Functie", "Vergelijking", "Nulwaarde"], [
                [r"\(f(x) = 2x - 6\)", r"\(2x - 6 = 0\), dus \(2x = 6\)", r"\(x = 3\)"],
                [r"\(f(x) = 3x + 12\)", r"\(3x + 12 = 0\), dus \(3x = -12\)", r"\(x = -4\)"],
            ])),
            ("p", r"Verwar de nulwaarde niet met het <strong>snijpunt met de \(y\)-as</strong>. Daar vul je \(0\) "
                  r"in voor \(x\) en bereken je \(f(0)\). Bij de nulwaarde stel je de functiewaarde gelijk aan "
                  r"\(0\) en zoek je de \(x\). Dat zijn twee verschillende vragen."),
            ("p", r"Een eerstegraadsfunctie waarvan de richtingscoëfficiënt niet nul is, is een schuine rechte, en "
                  r"die snijdt de \(x\)-as in <strong>precies één punt</strong>. Een constante functie zoals "
                  r"\(f(x) = 5\) is een horizontale rechte op hoogte \(5\) en heeft dus <strong>geen</strong> "
                  r"nulwaarde."),
        ]),
        dict(kop="Het tekenverloop", blokken=[
            ("fig", svg.tekenverloop(),
             "Een stijgende rechte met nulwaarde 4: links ligt ze onder de as, rechts erboven."),
            ("p", r"Een <strong>tekenverloop</strong> is een schema dat toont waar de functiewaarde positief is en "
                  r"waar ze negatief is. Het gaat enkel over het teken: een <strong>plusteken</strong> of een "
                  r"<strong>minteken</strong>. Hoe groot de waarde daar is, staat er niet in."),
        ]),
        dict(kop="De nulwaarden als grenzen", blokken=[
            ("p", r"De nulwaarden zijn de <strong>grenzen</strong> van het schema. Onder een nulwaarde zet je een "
                  r"<strong>\(0\)</strong>, want daar is de functiewaarde precies nul, en dus niet positief en "
                  r"niet negatief. Tussen twee grenzen blijft het teken hetzelfde."),
            ("p", tabel(["Functie", "Negatief", "Nul", "Positief"], [
                [r"\(f(x) = 2x - 6\) (stijgt)", r"links van \(3\)", r"in \(3\)", r"rechts van \(3\)"],
                [r"\(f(x) = -x + 4\) (daalt)", r"rechts van \(4\)", r"in \(4\)", r"links van \(4\)"],
                [r"\(f(x) = 5\)", "nergens", "nergens", "overal"],
            ])),
        ]),
        dict(kop="Stijgen is niet positief zijn", blokken=[
            ("p", "Bij een stijgende rechte ligt het positieve stuk <strong>rechts</strong> van de nulwaarde, "
                  "bij een dalende rechte <strong>links</strong>. Dat is precies waarom het antwoord op een "
                  "ongelijkheid ervan afhangt of de rechte stijgt of daalt. Teken haar even, dan zie je het meteen."),
            ("p", r"Om een tekenverloop van een grafiek af te lezen, kijk je naar twee dingen: waar de nulwaarden "
                  r"liggen, en aan welke kant daarvan de grafiek boven of onder de \(x\)-as loopt."),
            ("kader", r"<strong>Stijgen is niet hetzelfde als positief zijn.</strong> Stijgen gaat over de richting "
                      r"van de grafiek, positief zijn over haar ligging ten opzichte van de \(x\)-as. Een stijgende "
                      r"rechte begint links van haar nulwaarde onder de \(x\)-as en is daar dus negatief, terwijl "
                      r"ze al aan het stijgen is."),
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
                [r"alle \(x > 3\)", r"\(\left]3, +\infty\right[\)",
                 r"open bolletje op \(3\), alles rechts gearceerd"],
                [r"alle \(x \geq 3\)", r"\(\left[3, +\infty\right[\)",
                 r"vol bolletje op \(3\), alles rechts gearceerd"],
                [r"alle \(x\) tussen \(1\) en \(4\), grenzen niet mee", r"\(\left]1, 4\right[\)",
                 "twee open bolletjes, het stuk ertussen"],
            ])),
            ("p", r"Een haakje naar buiten betekent dat die grens er <strong>niet</strong> bij hoort, en dan zet je "
                  r"op de getallenas een open bolletje. Een haakje naar binnen neemt de grens wél mee, en dan wordt "
                  r"het bolletje vol. Bij \(f(x) \geq 0\) staat het gelijkheidsteken erbij, dus telt de nulwaarde "
                  r"zelf mee en sluit het haakje. Bij het <strong>oneindigteken</strong> \(\infty\) staat het "
                  r"haakje <strong>altijd</strong> open: oneindig is geen getal dat je kan bereiken."),
        ]),
        dict(kop="Twee functies naast elkaar", blokken=[
            ("p", r"Heb je twee functies \(f\) en \(g\), dan gaat het om hun <strong>gemeenschappelijke "
                  r"punten</strong> en hun <strong>onderlinge ligging</strong>."),
            ("p", tabel(["Je lost op", "Op de grafiek"], [
                [r"\(f(x) = g(x)\)", "je zoekt de gemeenschappelijke punten van de twee grafieken"],
                [r"\(f(x) > g(x)\)", r"je zoekt waar de grafiek van \(f\) boven die van \(g\) ligt"],
                [r"\(f(x) < g(x)\)", r"je zoekt waar de grafiek van \(f\) onder die van \(g\) ligt"],
            ])),
        ]),
        dict(kop="Het snijpunt is de grens", blokken=[
            ("p", r"Neem \(f(x) = x + 1\) en \(g(x) = 3x - 5\). Dan is \(x + 1 = 3x - 5\), dus \(6 = 2x\) en "
                  r"<strong>\(x = 3\)</strong>; de functiewaarde daar is \(4\). Het snijpunt is de "
                  r"<strong>grens</strong>: aan de ene kant ervan loopt \(f\) hoger, aan de andere kant \(g\). "
                  r"Snijden ze in \(x = 2\) en ligt \(f\) er links van lager, dan is de oplossingenverzameling van "
                  r"\(f(x) \leq g(x)\) gelijk aan \(\left]-\infty, 2\right]\), want in \(2\) zelf zijn ze gelijk "
                  r"en dat gelijkheidsteken sluit het haakje."),
            ("p", r"Niet elke opgave van de vorm \(f(x) = g(x)\) heeft precies één oplossing. Bij evenwijdige "
                  r"rechten is er geen enkele, en bij samenvallende rechten zijn er oneindig veel. Ligt de grafiek "
                  r"van \(f\) overal boven die van \(g\), dan hebben ze geen enkel punt gemeen en is er dus geen "
                  r"oplossing. Twee <strong>verschillende</strong> rechten kunnen elkaar nooit in twee punten "
                  r"snijden, want door twee punten gaat maar één rechte."),
            ("weetje", r"Twee grafieken kunnen elkaar snijden zonder dat een van beide de \(x\)-as snijdt: twee "
                       r"schuine rechten die in het getoonde stuk allebei boven de \(x\)-as blijven, kruisen "
                       r"elkaar toch."),
        ]),
        dict(kop="Een vraagstuk grafisch oplossen", blokken=[
            ("p", "Je mag een vraagstuk grafisch oplossen <strong>zonder de vergelijking of de ongelijkheid zelf "
                  "op te schrijven</strong>. Je maakt van elke situatie een grafiek en leest af welke boven de "
                  "andere ligt. Bij eenvoudige opgaven teken je zelf; bij moeilijkere vraagstukken met lastige "
                  "getallen laat je de grafieken met een <strong>hulpmiddel</strong> tekenen en lees je daar af."),
            ("p", r"<strong>Voorbeeld.</strong> Een fietsenwinkel heeft kosten \(K(x) = 300 + 20x\) en opbrengst "
                  r"\(O(x) = 50x\). De twee rechten snijden elkaar bij \(10\) fietsen: daar is alles \(500\) euro. "
                  r"Dat is het <strong>break-evenpunt</strong> of <strong>omslagpunt</strong>, waar de winst nul "
                  r"is. Pas vanaf de <strong>elfde</strong> fiets ligt de opbrengst erboven en is er winst."),
        ]),
        dict(kop="Wat een snijpunt betekent", blokken=[
            ("p", "In een woordprobleem betekent een snijpunt dus altijd hetzelfde: de situatie waarin de twee "
                  "grootheden <strong>even groot</strong> zijn. Twee abonnementen die evenveel kosten, kosten en "
                  "opbrengst die gelijk zijn, twee tanks met evenveel water erin."),
            ("p", r"Ligt een grafiek tussen \(x = 1\) en \(x = 4\) onder de \(x\)-as en daarbuiten erboven, dan is "
                  r"\(f(x) < 0\) op \(\left]1, 4\right[\): enkel tussen de twee nulwaarden, en in \(1\) en \(4\) "
                  r"zelf is de functiewaarde precies \(0\)."),
            ("kader", "Een grafiek helpt omdat je meteen ziet aan welke kant van de grens de oplossing ligt. Wie "
                      "enkel rekent, vergeet makkelijk het ongelijkheidsteken om te draaien. Maar aflezen is "
                      "schatten: je zit makkelijk een half hokje verkeerd, dus reken een snijpunt na."),
        ]),
    ],
    onthoud=[
        r"De nulwaarde is de \(x\) waarvoor \(f(x) = 0\): het snijpunt met de \(x\)-as.",
        r"\(f(0)\) is het snijpunt met de \(y\)-as; dat is iets anders dan de nulwaarde.",
        r"Een tekenverloop toont waar de functie positief en waar ze negatief is, met een \(0\) onder elke nulwaarde.",
        "Een verloopschema toont waar ze stijgt en waar ze daalt; bij een rechte is dat één pijl.",
        r"Stijgen gaat over de richting, positief zijn over de ligging ten opzichte van de \(x\)-as.",
        "Een stijgende rechte is positief rechts van haar nulwaarde, een dalende links.",
        r"Open haakje: de grens telt niet mee; vol bolletje: wel. Bij \(\infty\) staat het altijd open.",
        r"\(f(x) = g(x)\) zoekt de gemeenschappelijke punten; \(f(x) > g(x)\) zoekt waar \(f\) boven \(g\) ligt.",
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
            ("fig", svg.afgekapteas(),
             r"links begint de as bij \(0\), rechts bij \(96\); het verschil blijft \(1\)"),
            ("p", "De meeste misleiding met grafieken zit in de <strong>assen</strong>. Daar kijk je dus als "
                  "eerste, nog voor je naar de staven of de lijn kijkt. Zeker bij een grafiek die je op sociale "
                  "media tegenkomt, zonder de cijfers erbij."),
            ("p", r"De <strong>verticale as</strong> van een staafdiagram hoort in principe <strong>bij \(0\) te "
                  r"beginnen</strong>. De hoogte van een staaf stelt de grootte voor, dus knip je het onderste "
                  r"stuk weg, dan klopt de verhouding tussen de staven niet meer. Begint de as bij \(90\), dan "
                  r"lijken kleine verschillen veel groter dan ze zijn."),
        ]),
        dict(kop="Foutief ijken", blokken=[
            ("p", r"Een as kan ook <strong>foutief geijkt</strong> zijn. Loopt ze van \(0\) naar \(10\) naar "
                  r"\(100\) naar \(1000\) met gelijke tussenafstanden, dan staan gelijke afstanden niet voor "
                  r"gelijke verschillen. Of er worden stukken <strong>overgeslagen</strong>: slaat een tijdas de "
                  r"jaren \(2019\) en \(2020\) over, dan loopt de lijn vlakker of steiler dan het verloop echt "
                  r"was. Ontbrekende stukken hoor je te tonen, bijvoorbeeld met een breukteken."),
        ]),
        dict(kop="Ongepast schalen", blokken=[
            ("p", "Ten slotte kan een grafiek <strong>ongepast geschaald</strong> zijn. Dat merk je goed bij een "
                  "<strong>lijndiagram</strong>: dezelfde cijfers in een smalle grafiek geven een veel dramatischer "
                  "beeld dan in een brede: de lijn lijkt steiler en de verandering heftiger. Twee grafieken naast "
                  "elkaar met een verschillende schaal mag je daarom niet zomaar met elkaar vergelijken; kijk "
                  "eerst naar hun assen."),
            ("kader", r"Een as die niet bij \(0\) begint, is niet altijd bedrog. Bij lichaamstemperatuur of bij "
                      r"beurskoersen is inzoomen zinvol. Het moet dan wel <strong>duidelijk aangegeven</strong> "
                      r"staan."),
        ]),
        dict(kop="De vorm van het beeld", blokken=[
            ("p", "Ook zonder aan de assen te raken kan een beeld je oog sturen."),
            ("p", tabel(["Ingreep", "Wat er gebeurt"], [
                ["een cirkeldiagram in drie dimensies", "de sectoren vooraan krijgen meer oppervlakte en lijken groter"],
                ["een plaatje twee keer zo breed én zo hoog", r"de oppervlakte wordt \(2 \cdot 2 = 4\) keer zo groot bij een verdubbeling"],
                ["staven die niet even breed zijn", "de bredere staven trekken meer aandacht dan hun waarde verdient"],
            ])),
            ("p", "Een verdubbeling tonen met een plaatje dat vier keer zo veel plaats inneemt, heet "
                  "<strong>uitvergroten</strong>; die ingreep heet een <strong>uitvergroting</strong>. In een "
                  "staafdiagram hoort enkel de <strong>hoogte</strong> iets te betekenen; verschil in breedte voegt "
                  "een tweede signaal toe dat er niet is."),
            ("p", "Een cirkeldiagram toont delen van <strong>één</strong> geheel: alle sectoren horen bij dezelfde "
                  "groep en dezelfde periode. Zet iemand er een stuk bij dat van elders komt, dan stelt de cirkel "
                  "niets meer voor."),
        ]),
        dict(kop="Wat erbij hoort te staan", blokken=[
            ("p", "Een grafiek hoort een <strong>titel</strong>, <strong>namen bij de assen</strong>, een "
                  "<strong>legende</strong> bij meerdere reeksen en een <strong>bron</strong> te hebben. Een "
                  "legende legt uit waar elke kleur of elk symbool voor staat. Zonder namen weet je niet wat er "
                  "gemeten is of in welke eenheid; zonder legende niet welke lijn bij welke groep hoort; zonder "
                  "bron kan je niet nagaan of de cijfers kloppen. Let er ook op of de onderdelen <strong>correct "
                  "benoemd</strong> zijn: zet iemand 'omzet' naast 'winst' in hetzelfde diagram, dan vergelijkt "
                  "hij twee verschillende grootheden, en omzet is altijd groter dan winst."),
        ]),
        dict(kop="Wat er níét staat", blokken=[
            ("p", "Een van de sterkste manieren om te misleiden is <strong>informatie of data weglaten</strong>. "
                  "Wat je niet toont, kan de lezer ook niet wegen. Toont een grafiek enkel de vier beste maanden "
                  "van het jaar, dan klopt elk getal en klopt het verhaal toch niet."),
            ("p", r"Hetzelfde geldt voor een aantal zonder het <strong>totaal</strong> erbij. Een stijging van "
                  r"\(2\) naar \(4\) zegt iets heel anders bij een groep van \(10\) mensen dan bij een groep van "
                  r"\(10\,000\). Vraag dus altijd welke periode, welke groep of welk totaal ontbreekt."),
        ]),
        dict(kop="Percentages, en het verschil met procentpunt", blokken=[
            ("p", "Hier worden de meeste fouten gemaakt, en niet altijd met opzet."),
            ("p", tabel(["Woord", "Wat het meet", r"Van \(4\,\%\) naar \(6\,\%\)"], [
                ["procentpunt", "het gewone verschil tussen twee percentages", r"\(2\) procentpunt"],
                ["procent", "de verandering ten opzichte van het startgetal", r"\(50\,\%\)"],
            ])),
            ("p", r"Van \(4\,\%\) naar \(6\,\%\) is er \(2\) procentpunt bij gekomen. Maar ten opzichte van de "
                  r"\(4\) waar je van vertrok, is dat de helft meer, dus een <strong>relatieve</strong> stijging "
                  r"van \(50\,\%\). Wie de twee woorden verwisselt, maakt een cijfer veel groter of kleiner dan "
                  r"het is."),
            ("p", r"Twee kortingen na elkaar mag je <strong>niet</strong> optellen. Een jas van \(100\) euro met "
                  r"eerst \(20\,\%\) en dan nog eens \(10\,\%\) korting kost \(80\) euro en daarna \(72\) euro: "
                  r"dat is samen <strong>\(28\,\%\)</strong> korting, niet \(30\,\%\). Om dezelfde reden brengt "
                  r"een prijs die eerst \(10\,\%\) stijgt en daarna \(10\,\%\) daalt je niet terug bij het begin: "
                  r"\(100\) wordt \(110\), en \(10\,\%\) van \(110\) is \(11\), dus je eindigt op \(99\)."),
        ]),
        dict(kop="De woorden rond het getal", blokken=[
            ("p", r"<strong>'Tot \(70\,\%\) korting'</strong> zet enkel een bovengrens: misschien haalt één "
                  r"artikel die korting en de rest veel minder. Een winst die <strong>'met \(200\,\%\) "
                  r"groeide'</strong> is verdrievoudigd, want er kwam twee keer het oorspronkelijke bedrag bij. En "
                  r"bij <strong>'het risico verdubbelt'</strong> wil je vooral weten hoe groot dat risico eerst "
                  r"was: van \(1\) op een miljoen naar \(2\) op een miljoen is ook een verdubbeling."),
            ("kader", r"Een percentage zonder het aantal waarop het slaat, zegt weinig. \(100\,\%\) van twee "
                      r"mensen klinkt indrukwekkend en stelt niets voor."),
        ]),
        dict(kop="Welk middelpunt toont iemand?", blokken=[
            ("p", "Het <strong>rekenkundig gemiddelde</strong> telt elk getal mee met zijn volle grootte, dus één "
                  "uitschieter trekt het ver weg. De <strong>mediaan</strong> is gewoon het middelste getal van de "
                  "reeks op volgorde, en die verschuift daar nauwelijks door. Bij een even aantal getallen neem je "
                  "het gemiddelde van de twee middelste."),
            ("p", r"Neem een bedrijf waar vier mensen \(2000\) euro verdienen en één persoon \(12\,000\) euro."),
            ("p", tabel(["Maat", "Berekening", "Uitkomst"], [
                ["rekenkundig gemiddelde", r"\(\frac{20\,000}{5}\)", r"\(4000\) euro"],
                ["mediaan", r"het derde getal van \(2000,\ 2000,\ 2000,\ 2000,\ 12\,000\)", r"\(2000\) euro"],
            ])),
            ("p", r"Adverteert dat bedrijf met <em>bij ons verdien je gemiddeld \(4000\) euro</em>, dan klopt het "
                  r"getal en beschrijft het niemand: vier van de vijf werknemers verdienen veel minder. Allebei de "
                  r"getallen zijn juist. Wie de lonen hoog wil laten lijken, toont het gemiddelde; wie ze laag wil "
                  r"laten lijken, de mediaan. <strong>Wie kiest welk getal hij toont, stuurt daarmee het "
                  r"verhaal.</strong>"),
        ]),
        dict(kop="Wie zegt het, en aan wie is het gevraagd?", blokken=[
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
        r"Een staafdiagram hoort bij \(0\) te beginnen; anders lijken kleine verschillen groot.",
        "Smal tekenen maakt een verandering dramatischer; twee keer zo breed én hoog is vier keer zo groot.",
        "In drie dimensies lijken de sectoren vooraan groter; titel, assen, legende en bron horen erbij.",
        "Wat weggelaten is, kan je niet wegen: vraag welke periode of welke groep ontbreekt.",
        "Procentpunt is het verschil tussen twee percentages, procent de verandering ten opzichte van het begin.",
        r"Twee kortingen na elkaar tel je niet op: \(20\,\%\) en dan \(10\,\%\) is samen \(28\,\%\).",
        r"Met \(200\,\%\) groeien is verdrievoudigen, niet verdubbelen.",
        "Eén uitschieter trekt het gemiddelde weg, niet de mediaan; een cijfer dat klopt kan toch misleiden.",
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

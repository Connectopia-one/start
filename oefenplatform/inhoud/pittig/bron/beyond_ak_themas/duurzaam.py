"""Duurzaam ruimtegebruik — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vier ingrepen ----------------------------------------------------------
VI = Prent("vier-ingrepen", "Vier ingrepen in een stad, vóór en na", "vier vakken A tot D, elk met een situatie voor en na een ingreep")
VAK = {"A": (40, 80), "B": (510, 80), "C": (40, 350), "D": (510, 350)}
for k, (x0, y0) in VAK.items():
    VI.rect(x0, y0, 450, 250, "#f7f4ea", DONKER, 12, 1)
    VI.pijl(x0 + 205, y0 + 150, x0 + 245, y0 + 150, DONKER, 3)
    VI.lijn(x0 + 20, y0 + 220, x0 + 430, y0 + 220, DONKER, 2)
    VI.letter(x0 + 30, y0 + 30, k)
# A: laag huis -> hoger gebouw met meerdere woningen (intensivering)
x0, y0 = VAK["A"]
VI.rect(x0 + 70, y0 + 160, 90, 60, "#c0603a", DONKER, 0, 2)
VI.rect(x0 + 290, y0 + 70, 90, 150, "#c0603a", DONKER, 0, 2)
for r in range(4):
    for c in range(2):
        VI.rect(x0 + 302 + c * 40, y0 + 84 + r * 34, 24, 18, "#f3efe6", DONKER, 0, 1)
# B: fabriek met schoorsteen -> zelfde gebouw met ramen en planten (hergebruik)
x0, y0 = VAK["B"]
for dx in (40, 260):
    VI.pad(f"M{x0 + dx} {y0 + 220} L {x0 + dx} {y0 + 140} L {x0 + dx + 40} {y0 + 120} L {x0 + dx + 40} {y0 + 140} L {x0 + dx + 80} {y0 + 120} L {x0 + dx + 80} {y0 + 140} L {x0 + dx + 130} {y0 + 120} L {x0 + dx + 130} {y0 + 220} Z", "#9a917a", DONKER, 2)
VI.rect(x0 + 140, y0 + 70, 18, 70, "#7d7466", DONKER, 0, 2)
for c in range(3):
    VI.rect(x0 + 275 + c * 38, y0 + 160, 24, 30, "#f3efe6", DONKER, 0, 1)
for c in range(3):
    VI.cirkel(x0 + 285 + c * 38, y0 + 135, 9, "#8fb36a", "none", 0)
# C: braakliggend terrein -> buurttuin met hek en tijdelijk bordje (tijdelijk)
x0, y0 = VAK["C"]
for i in range(5):
    VI.lijn(x0 + 50 + i * 30, y0 + 215, x0 + 60 + i * 30, y0 + 200, GRIJS, 2)
for i in range(4):
    VI.rect(x0 + 260 + i * 40, y0 + 190, 30, 30, "#8d6e4a", DONKER, 2, 1)
    VI.cirkel(x0 + 275 + i * 40, y0 + 180, 12, "#8fb36a", "none", 0)
VI.rect(x0 + 300, y0 + 90, 110, 40, "#ffffff", DONKER, 4, 1)
VI.tekst(x0 + 355, y0 + 116, "tot 2028", 16)
VI.lijn(x0 + 355, y0 + 130, x0 + 355, y0 + 190, DONKER, 2)
# D: woning + aparte winkel ver weg -> winkel beneden, wonen boven (verweving)
x0, y0 = VAK["D"]
VI.rect(x0 + 40, y0 + 160, 60, 60, "#c0603a", DONKER, 0, 2)
VI.rect(x0 + 130, y0 + 170, 60, 50, "#6a8cbf", DONKER, 0, 2)
VI.tekst(x0 + 160, y0 + 160, "winkel", 13)
VI.rect(x0 + 290, y0 + 100, 100, 70, "#c0603a", DONKER, 0, 2)
VI.rect(x0 + 290, y0 + 170, 100, 50, "#6a8cbf", DONKER, 0, 2)
VI.tekst(x0 + 340, y0 + 200, "winkel", 13, kleur="#ffffff")
ZVI = {k: [Prent.zone(x0, y0, 450, 250)] for k, (x0, y0) in VAK.items()}

# Klimaatrobuuste straat -------------------------------------------------
KS = Prent("klimaatrobuuste-straat", "Doorsnede van een klimaatrobuuste straat", "huizen links en rechts, een boom, een ondiepe grasgracht, een rijweg en een plein met open voegen, letters W, X, Y, Z")
KS.rect(40, 430, 920, 190, "#c9b48a", "none", 0, 0)
KS.rect(40, 220, 120, 210, "#c0603a", DONKER, 0, 2)
KS.rect(840, 220, 120, 210, "#c0603a", DONKER, 0, 2)
KS.rect(160, 420, 160, 10, "#bbb", DONKER, 0, 1)
for i in range(8):
    KS.lijn(165 + i * 20, 420, 165 + i * 20, 430, "#7aa060", 3)
KS.rect(230, 330, 14, 90, "#6b4f2a", "none", 0, 0)
KS.cirkel(237, 290, 70, "#8fb36a", DONKER, 1)
KS.pad("M330 430 Q 410 500 490 430 Z", "#a9c38a", DONKER, 2)
KS.pad("M350 445 Q 410 485 470 445", "none", BLAUW, 5)
KS.rect(500, 420, 200, 10, "#555", DONKER, 0, 1)
KS.rect(710, 420, 120, 10, "#ccc", DONKER, 0, 1)
for i in range(6):
    KS.lijn(715 + i * 20, 420, 715 + i * 20, 430, "#7aa060", 3)
for x in (380, 420, 460, 740, 780):
    KS.pijl(x, 180, x - 5, 230, BLAUW, 2)
LKS = {"W": (237, 170), "X": (410, 540), "Y": (600, 470), "Z": (770, 470)}
for k, (x, y) in LKS.items():
    KS.letter(x, y, k)
ZKS = {"W": [Prent.zone(160, 210, 160, 210), Prent.rond(*LKS["W"], 26)],
       "X": [Prent.zone(330, 420, 160, 70), Prent.rond(*LKS["X"], 26)],
       "Y": [Prent.zone(500, 410, 200, 30), Prent.rond(*LKS["Y"], 26)],
       "Z": [Prent.zone(710, 410, 120, 30), Prent.rond(*LKS["Z"], 26)]}

VRAGEN = [
    met_prent(VI.bestand, tabel(
        "Kijk naar de vier vakken. Welk principe van het omgevingsdenken zie je?",
        [
            ("intensivering", "A"),
            ("hergebruik", "B"),
            ("tijdelijk ruimtegebruik", "C"),
            ("verweving", "D"),
        ],
        "Meer op dezelfde plek, een nieuwe functie, even benutten, functies samen.",
        kolommen=["A", "B", "C", "D"],
    )),
    klik(
        "Klik op het vak waar een oud gebouw een nieuwe functie krijgt.",
        VI.bestand, ZVI["B"],
        "Een oude fabriek wordt woningen of lofts.",
    ),
    klik(
        "Klik op het vak waar een plek benut wordt tot ze een definitieve bestemming krijgt.",
        VI.bestand, ZVI["C"],
        "Een buurttuin op een braakliggend terrein.",
    ),
    met_prent(VI.bestand, tabel(
        "Kijk naar vak A en vak D. Klopt dit?",
        [
            ("In A wonen na de ingreep meer gezinnen op hetzelfde perceel.", J),
            ("In D hoef je na de ingreep minder te verplaatsen.", J),
            ("A vraagt extra open ruimte.", F),
        ],
        "Intensiveren gebeurt op een plek die al bebouwd is.",
    )),
    klik(
        "Klik op de wadi.",
        KS.bestand, ZKS["X"],
        "Een ondiepe grasgracht die regenwater opvangt en laat insijpelen.",
    ),
    klik(
        "Klik op de plek waar het regenwater het snelst naar de riool loopt.",
        KS.bestand, ZKS["Y"],
        "Asfalt laat geen water door.",
    ),
    met_prent(KS.bestand, tabel(
        "Kijk naar de straat in doorsnede. Klopt dit?",
        [
            ("W geeft schaduw op hete dagen.", J),
            ("Bij Z kan regenwater tussen de stenen in de bodem zakken.", J),
            ("X mag na een zware bui even onder water staan.", J),
            ("Y helpt het grondwater aan te vullen.", F),
        ],
        "Rijweg Y is volledig verhard.",
    )),
    tabel(
        "Welk principe van het omgevingsdenken is dit?",
        [
            ("een kerk wordt een bibliotheek", "hergebruik"),
            ("een extra verdieping op een bestaand huis", "intensivering"),
            ("een pop-upbar in een leeg pand", "tijdelijk ruimtegebruik"),
            ("een bakker met woningen erboven", "verweving"),
            ("een brownfield wordt een woonwijk", "hergebruik"),
        ],
        "Soms combineert een project meerdere principes.",
        kolommen=["intensivering", "hergebruik", "verweving", "tijdelijk ruimtegebruik"],
    ),
    tabel(
        "Klopt dit over intensivering?",
        [
            ("Het kan met een extra verdieping.", J),
            ("Het kan door een groot huis in twee woningen te splitsen.", J),
            ("Het vraagt altijd een toren.", F),
            ("Het spaart open ruimte.", J),
        ],
        "Hoogbouw is maar een van de manieren.",
    ),
    mk(
        "Waarom past een fabriek met zwaar vrachtverkeer niet goed tussen woningen?",
        [
            "Lawaai, geur en vrachtwagens hinderen de buurt",
            "Fabrieken mogen volgens de wet nooit in een stad staan",
            "Woningen geven te veel schaduw op het fabrieksdak",
            "De arbeiders willen zelf liever ver van hun werk wonen",
        ],
        0,
        "Verweving lukt vooral met functies die weinig hinder geven.",
    ),
    casus(
        "Een gemeente heeft een leegstaand terrein naast het station. Over vijf jaar wil ze er woningen bouwen.",
        [
            keuze(
                "In afwachting kan het terrein een buurttuin worden. Dat is [[*tijdelijk ruimtegebruik|intensivering|ontharding]].",
                "Het overbrugt de jaren tot het definitieve project.",
            ),
            tabel(
                "Klopt dit over de plek?",
                [
                    ("Een plek bij het station is goed bereikbaar.", J),
                    ("Hier dicht bouwen past bij het beleid.", J),
                    ("Een plek bij het station is de slechtste plek om te verdichten.", F),
                ],
                "Rond knooppunten van trein en bus kan je het best verdichten.",
            ),
        ],
    ),
    sorteer(
        "Maakt dit een straat klimaatrobuust?",
        ["Wel", "Niet"],
        [
            ("bomen planten", "Wel"),
            ("verharding wegnemen", "Wel"),
            ("een wadi aanleggen", "Wel"),
            ("een tuin volledig betegelen", "Niet"),
            ("regenwater meteen naar de riool sturen", "Niet"),
        ],
        "Water vasthouden, laten insijpelen en schaduw geven.",
    ),
    mk(
        "Waarom is een gedeelde parking voor een kantoor en appartementen slim?",
        [
            "Dezelfde plaatsen dienen overdag en 's avonds",
            "Kantoorwagens zijn kleiner dan de wagens van bewoners",
            "Een gedeelde parking hoeft geen verlichting te hebben",
            "De bewoners mogen dan gratis in het kantoor werken",
        ],
        0,
        "Overdag staan de werknemers er, 's avonds de bewoners.",
    ),
    sleep(
        "Bouwen met [[herbruikbare]] onderdelen heet [[circulair]] bouwen. Zo'n gebouw kan je later weer [[ontmantelen]].",
        ["wegwerp", "lineair", "verharden"],
        "De materialen krijgen een tweede leven.",
    ),
    tabel(
        "Klopt dit over leegstand boven winkels?",
        [
            ("Die ruimte ligt al centraal.", J),
            ("Ze opnieuw bewonen vraagt geen open ruimte.", J),
            ("Het versterkt de dorpskern.", J),
            ("Wonen boven winkels kan wettelijk nooit.", F),
        ],
        "Zo verdicht je zonder één nieuw gebouw.",
    ),
    koppel(
        "Koppel elk begrip van duurzaam ruimtegebruik aan zijn uitleg.",
        [
            ("brownfield", "oud industrieterrein dat opnieuw ontwikkeld wordt"),
            ("ontharden", "beton of asfalt weghalen"),
            ("kernversterking", "de dorpskern aantrekkelijker maken"),
            ("nabijheidsindex", "hoeveel voorzieningen er in de buurt liggen"),
        ],
        ["een nieuwe verkaveling in een weiland"],
        "Dat laatste is net het tegendeel van duurzaam ruimtegebruik.",
    ),
    mk(
        "Wie een bouwgrond heeft midden in de open ruimte, krijgt bouwrecht op een betere plek. Hoe heet dat?",
        [
            "Grondruil",
            "Verweving",
            "Gentrificatie",
            "Lintbebouwing",
        ],
        0,
        "Zo verschuift het bouwen naar een plek die er beter geschikt voor is.",
    ),
    volgorde(
        "Zet de vragen van het omgevingsdenken in de juiste volgorde.",
        [
            "Kan het op een plek die al in gebruik is?",
            "Kan een bestaand gebouw hergebruikt worden?",
            "Pas dan: is er open ruimte nodig, en zo ja waar?",
        ],
        "Open ruimte aansnijden is de laatste keuze.",
    ),
    tabel(
        "Klopt dit over een woning in een lint?",
        [
            ("Ze vraagt meer meter leiding en weg per woning.", J),
            ("De bewoners rijden meestal meer met de wagen.", J),
            ("Ze kost de samenleving minder dan een woning in een kern.", F),
        ],
        "Alles moet ver doorgetrokken worden langs de weg.",
    ),
    inv(
        "Een wadi is 20 m lang, 4 m breed en kan 0,5 m water bevatten. Hoeveel m³ regenwater kan hij bufferen?",
        ["40"],
        "20 x 4 x 0,5 = 40 m³.",
    ),
    tabel(
        "Waar bouw je volgens het beleid het best dichter?",
        [
            ("vlak bij een treinstation", J),
            ("in een dorpskern met school en winkels", J),
            ("langs een landelijke weg zonder bus", F),
            ("in een overstromingsgebied", F),
        ],
        "Nabijheid en bereikbaarheid bepalen waar verdichten zin heeft.",
    ),
    mk(
        "Buurtbewoners protesteren tegen een nieuw appartementsgebouw in de kern. Wat helpt het meest om verdichting aanvaardbaar te maken?",
        [
            "Publiek groen en ontmoetingsruimte voorzien",
            "Het gebouw zo hoog mogelijk maken",
            "Alle bomen in de straat kappen om er parking te maken",
            "Het project in het geheim goedkeuren",
        ],
        0,
        "Dichter wonen lukt als de buurt er ook iets bij krijgt.",
    ),
    keuze(
        "Een gebouw met winkels beneden, kantoren in het midden en woningen bovenaan heet een [[*gemengd gebouw|brownfield|lintbebouwing]].",
        "Verweving in één gebouw.",
    ),
    tabel(
        "Klopt dit over een volledig betegelde tuin?",
        [
            ("Regenwater kan er niet in de bodem.", J),
            ("Het water loopt naar de riool.", J),
            ("De tuin warmt sterker op in de zomer.", J),
            ("Het grondwater wordt er beter door aangevuld.", F),
        ],
        "Tegels eruit en planten erin helpt bij hitte en droogte.",
    ),
    keuze(
        "Een oude textielfabriek wordt omgebouwd tot twintig woningen. Dat is hergebruik en ook [[*intensivering|ontharding|tijdelijk ruimtegebruik]].",
        "Er wonen meer mensen op hetzelfde perceel.",
    ),
    tabel(
        "Welke vraag weeg je af bij een nieuw bouwproject?",
        [
            ("Ligt het dicht bij voorzieningen?", J),
            ("Neemt het open ruimte in?", J),
            ("Kan het regenwater op het terrein blijven?", J),
            ("Heeft de bouwheer een mooie wagen?", F),
        ],
        "Ligging, open ruimte en water wegen het zwaarst.",
    ),
    tabel(
        "Klopt dit over tijdelijk ruimtegebruik?",
        [
            ("Het overbrugt de tijd tot een definitief project.", J),
            ("Het kan een buurt levendiger maken.", J),
            ("Het geeft een plek voorgoed een nieuwe bestemming.", F),
        ],
        "Tijdelijk is tijdelijk.",
    ),
    mk(
        "Waarom staat intensiveren vooraan in het omgevingsdenken?",
        [
            "Het vraagt geen nieuwe open ruimte",
            "Het is altijd de goedkoopste oplossing",
            "Het mag zonder vergunning",
            "Het zorgt altijd voor meer groen",
        ],
        0,
        "Wat je op een bebouwde plek bijkrijgt, hoef je niet in de open ruimte te zoeken.",
    ),
    open_(
        "Leg uit hoe een straat beter bestand kan worden tegen hitte en zware buien.",
        "Je kan verharding wegnemen en vervangen door groen, zodat regenwater in de bodem zakt. Een wadi vangt water op bij een zware bui. Bomen geven schaduw en koelen de straat af op hete dagen.",
    ),
]

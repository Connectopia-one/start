"""De huidige klimaatverandering — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Broeikaseffect ---------------------------------------------------------
BK = Prent("broeikaseffect-schema", "Het broeikaseffect (schematisch)", "zon links boven, pijlen van zonlicht naar het aardoppervlak, warmtestraling omhoog, een deel teruggekaatst door een laag broeikasgassen")
BK.rect(40, 460, 920, 160, "#a9c38a", DONKER, 0, 1)
BK.rect(40, 200, 920, 40, "#e8dff0", "none", 0, 0)
BK.tekst(50, 228, "broeikasgassen", 15, "start", kleur=PAARS)
BK.cirkel(110, 110, 50, GEEL, ORANJE, 3)
BK.pijl(170, 130, 360, 455, ORANJE, 6)
BK.pijl(250, 120, 440, 455, ORANJE, 6)
BK.pijl(330, 120, 380, 190, ORANJE, 4)
BK.pijl(390, 195, 450, 80, ORANJE, 4)
for x in (600, 720, 840):
    BK.svg(f'<path d="M{x} 450 q 10 -15 0 -30 q -10 -15 0 -30 q 10 -15 0 -30 q -10 -15 0 -30 q 10 -15 0 -30 q -10 -15 0 -30" fill="none" stroke="{ROOD}" stroke-width="4"/>')
BK.svg(f'<path d="M840 270 q 10 -15 0 -30 q -10 -15 0 -30 q 10 -15 0 -30 q -10 -15 0 -30" fill="none" stroke="{ROOD}" stroke-width="4"/>')
BK.pijl(840, 120, 840, 70, ROOD, 4)
BK.svg(f'<path d="M600 250 q 30 20 40 60 q 10 40 40 60 q 20 20 20 70" fill="none" stroke="{ROOD}" stroke-width="4" stroke-dasharray="8 6"/>')
BK.pijl(720, 430, 722, 450, ROOD, 4)
LBK = {"A": (300, 300), "B": (470, 120), "C": (840, 160), "D": (690, 350)}
for k, (x, y) in LBK.items():
    BK.letter(x, y, k)
ZBK = {k: [Prent.rond(x, y, 32)] for k, (x, y) in LBK.items()}
ZBK["A"].append(Prent.zone(170, 130, 270, 320))
ZBK["C"].append(Prent.zone(815, 60, 50, 220))
ZBK["D"].append(Prent.zone(600, 250, 120, 200))

# Scenario's -------------------------------------------------------------
SC = Prent("scenarios-2100", "Opwarming tegenover de tijd vóór de industrie (vereenvoudigd)", "grafiek 1950 tot 2100 met een gemeten lijn tot nu en drie scenario's P, Q en R")
X, Y = assen(SC, 1950, 2100, 0, 5, "jaar", "opwarming (°C)", 25, 1, links=130, rechts=880)
gem = [(1950, 0.3), (1970, 0.35), (1990, 0.6), (2010, 0.95), (2025, 1.3)]
SC.pad("M" + " L ".join(f"{X(a):.0f} {Y(b):.0f}" for a, b in gem), "none", DONKER, 4)
for naam, eind, kl in (("P", 1.6, GROEN), ("Q", 2.8, ORANJE), ("R", 4.4, ROOD)):
    SC.pad(f"M{X(2025):.0f} {Y(1.3):.0f} Q {X(2060):.0f} {Y(1.3 + (eind - 1.3) * 0.55):.0f} {X(2100):.0f} {Y(eind):.0f}", "none", kl, 4)
SC.lijn(X(1950), Y(1.5), X(2100), Y(1.5), GRIJS, 2, stippel=True)
SC.tekst(X(1955), Y(1.5) - 8, "1,5 °C", 15, "start", kleur="#555")
LSC = {"P": (2100, 1.6), "Q": (2100, 2.8), "R": (2100, 4.4)}
for k, (a, b) in LSC.items():
    SC.letter(X(a) + 34, Y(b), k)
ZSC = {k: [Prent.rond(X(a) + 34, Y(b), 30), Prent.zone(X(2060), Y(b) - 25, X(2100) - X(2060), 50)] for k, (a, b) in LSC.items()}

VRAGEN = [
    klik(
        "Klik op de warmtestraling die door de broeikasgassen wordt tegengehouden.",
        BK.bestand, ZBK["D"],
        "Die straling wordt terug naar het aardoppervlak gestuurd.",
    ),
    klik(
        "Klik op het zonlicht dat het aardoppervlak opwarmt.",
        BK.bestand, ZBK["A"],
        "Kortgolvig zonlicht gaat vlot door de broeikasgassen.",
    ),
    met_prent(BK.bestand, tabel(
        "Kijk naar het schema van het broeikaseffect. Klopt dit?",
        [
            ("B is zonlicht dat meteen wordt weerkaatst.", J),
            ("C is warmtestraling die de ruimte in gaat.", J),
            ("Met meer broeikasgas wordt pijl D sterker.", J),
            ("De broeikasgassen houden vooral het zonlicht tegen.", F),
        ],
        "Ze houden de warmtestraling van de aarde tegen, niet het zonlicht.",
    )),
    klik(
        "Klik op het scenario waarin we de uitstoot het snelst verminderen.",
        SC.bestand, ZSC["P"],
        "Hoe minder uitstoot, hoe minder opwarming tegen 2100.",
    ),
    met_prent(SC.bestand, tabel(
        "Kijk naar de scenario's tot 2100. Klopt dit?",
        [
            ("We zitten nu al boven 1 °C opwarming.", J),
            ("Bij R zit de opwarming in 2100 boven 4 °C.", J),
            ("Ook bij P ligt de opwarming in 2100 boven 1,5 °C.", J),
            ("De scenario's lopen pas uit elkaar na 2100.", F),
        ],
        "Wat we nu uitstoten, bepaalt welke lijn we volgen.",
    )),
    met_prent(SC.bestand, inv(
        "Kijk naar de grafiek. Hoeveel graden scheelt scenario R met scenario P in 2100? Rond af op een geheel getal.",
        ["3"],
        "4,4 - 1,6 = 2,8, afgerond 3 graden.",
    )),
    tabel(
        "Mitigatie of adaptatie?",
        [
            ("dijken verhogen", "Adaptatie"),
            ("woningen isoleren", "Mitigatie"),
            ("bomen planten tegen hitte in de stad", "Adaptatie"),
            ("overschakelen op windenergie", "Mitigatie"),
            ("droogtebestendige gewassen telen", "Adaptatie"),
            ("minder vlees eten", "Mitigatie"),
        ],
        "Mitigatie pakt de oorzaak aan, adaptatie de gevolgen.",
        kolommen=["Mitigatie", "Adaptatie"],
    ),
    tabel(
        "Versterkt of remt dit de opwarming?",
        [
            ("zee-ijs smelt", "Versterkt"),
            ("permafrost ontdooit", "Versterkt"),
            ("een warmere aarde straalt meer warmte uit", "Remt"),
            ("meer waterdamp in de lucht", "Versterkt"),
        ],
        "Positief betekent hier versterkend, niet goed.",
        kolommen=["Versterkt", "Remt"],
    ),
    koppel(
        "Koppel elk broeikasgas aan een belangrijke bron.",
        [
            ("koolstofdioxide", "verbranden van steenkool, olie en gas"),
            ("methaan", "veeteelt en rijstvelden"),
            ("lachgas", "kunstmest op akkers"),
        ],
        ["zuurstof uit planten", "stikstof uit de lucht"],
        "Zuurstof en stikstof zijn geen broeikasgassen.",
    ),
    casus(
        "Een leerling zegt: 'Deze winter was het hier heel koud, dus van opwarming is niets te merken.'",
        [
            keuze(
                "Het klimaat is het gemiddelde weer over ongeveer [[*30 jaar|1 jaar|1 seizoen]].",
                "Eén winter is weer, geen klimaat.",
            ),
            tabel(
                "Klopt dit als antwoord aan de leerling?",
                [
                    ("Ook in een warmer klimaat zijn er koude winters.", J),
                    ("Je moet naar de hele wereld kijken, niet naar één plek.", J),
                    ("Een koude winter bewijst dat de opwarming gestopt is.", F),
                ],
                "Trends zie je pas over lange tijd en over de hele aarde.",
            ),
        ],
    ),
    mk(
        "Waarom warmt het Noordpoolgebied sneller op dan het wereldgemiddelde?",
        [
            "Smeltend ijs maakt plaats voor donker water",
            "De zon staat daar in de zomer het hoogst van de aarde",
            "Er wordt in het Noordpoolgebied het meest CO2 uitgestoten",
            "Er zitten daar geen broeikasgassen in de lucht",
        ],
        0,
        "Donker water slorpt meer zonlicht op dan wit ijs.",
    ),
    tabel(
        "Waarom stijgt de zeespiegel?",
        [
            ("landijs op Groenland smelt", J),
            ("warmer zeewater zet uit", J),
            ("gletsjers in de bergen smelten", J),
            ("drijvend zee-ijs smelt", F),
        ],
        "Drijvend ijs verplaatst al evenveel water als het zelf weegt.",
    ),
    sleep(
        "De oceaan neemt ongeveer [[een kwart]] van onze CO2 op. Daardoor wordt het zeewater [[zuurder]]. Dieren met een [[kalkskelet]] krijgen het daardoor moeilijk.",
        ["de helft", "zouter", "longen"],
        "Koralen en schelpdieren lijden het eerst.",
    ),
    mk(
        "Waarom stijgt de temperatuur nog een tijd verder, ook als we vandaag stoppen met uitstoten?",
        [
            "De oceaan warmt maar heel traag op",
            "De zon wordt elk jaar wat sterker",
            "Het CO2-gas wordt elk jaar vanzelf meer",
            "Het IPCC heeft dat zo afgesproken",
        ],
        0,
        "De oceaan heeft een enorme warmtecapaciteit.",
    ),
    tabel(
        "Klopt dit over het akkoord van Parijs?",
        [
            ("Het wil de opwarming ruim onder 2 °C houden.", J),
            ("Het streeft naar 1,5 °C.", J),
            ("Elk land beslist zelf hoe het bijdraagt.", J),
            ("Het verbiedt alle uitstoot meteen.", F),
        ],
        "Landen leggen hun eigen plannen voor.",
    ),
    keuze(
        "Klimaatneutraal betekent dat uitstoot en vastlegging [[*in evenwicht|allebei nul|heel klein]] zijn.",
        "Wat je nog uitstoot, moet ergens vastgelegd worden.",
    ),
    tabel(
        "Klopt dit over het IPCC?",
        [
            ("Het hoort bij de Verenigde Naties.", J),
            ("Het bundelt onderzoek van duizenden wetenschappers.", J),
            ("Het rekent verschillende scenario's door.", J),
            ("Het doet zelf de metingen op zee en in de lucht.", F),
        ],
        "Het vat bestaand onderzoek samen.",
    ),
    mk(
        "Hoe weten we dat de extra CO2 in de lucht uit fossiele brandstoffen komt?",
        [
            "Uit de verhouding van de koolstofisotopen",
            "Uit de kleur van de lucht boven grote steden",
            "Uit de hoeveelheid zuurstof in de oceaan",
            "Uit de stand van de aardas tegenover de zon",
        ],
        0,
        "Koolstof uit steenkool en olie heeft een eigen vingerafdruk.",
    ),
    sorteer(
        "Is dit een gevolg dat we nu al meten?",
        ["Al gemeten", "Geen gevolg"],
        [
            ("terugtrekkende gletsjers", "Al gemeten"),
            ("meer hittegolven", "Al gemeten"),
            ("stijgende zeespiegel", "Al gemeten"),
            ("een kortere dag", "Geen gevolg"),
        ],
        "De daglengte hangt af van de draaiing van de aarde.",
    ),
    inv(
        "Per graad opwarming kan de lucht ongeveer 7 % meer waterdamp bevatten. Hoeveel procent meer is dat bij 3 graden, als je gewoon optelt?",
        ["21"],
        "3 x 7 = 21 %.",
    ),
    tabel(
        "Klopt dit over klimaatrechtvaardigheid?",
        [
            ("Arme landen stootten historisch het minst uit.", J),
            ("Ze worden vaak het hardst getroffen.", J),
            ("Ze hebben minder geld om zich aan te passen.", J),
            ("Rijke landen voelen geen enkel gevolg.", F),
        ],
        "Ook bij ons zijn er hittegolven en overstromingen.",
    ),
    mk(
        "Waarom volstaat adaptatie alleen niet?",
        [
            "Bij sterke opwarming lukt aanpassen niet overal",
            "Adaptatie kost altijd meer dan alle uitstoot samen",
            "Adaptatie maakt de opwarming zelf groter",
            "Aanpassen kan pas na het jaar 2100",
        ],
        0,
        "Daarom zijn mitigatie en adaptatie samen nodig.",
    ),
    tabel(
        "Welke maatregel weegt het zwaarst in een gezin?",
        [
            ("minder vliegen", J),
            ("het huis beter isoleren", J),
            ("minder vlees eten", J),
            ("de gsm-lader uittrekken", F),
        ],
        "Vervoer, verwarming en voeding wegen het meest.",
    ),
    tabel(
        "Houdt dit gas warmtestraling tegen?",
        [
            ("waterdamp", J),
            ("methaan", J),
            ("ozon", J),
            ("stikstof", F),
            ("zuurstof", F),
        ],
        "Stikstof en zuurstof laten warmtestraling gewoon door.",
    ),
    mk(
        "Waarom geeft een rund zoveel methaan af?",
        [
            "Pensbacteriën breken gras af zonder zuurstof",
            "Runderen ademen meer CO2 uit dan andere dieren",
            "Mest op de weide verbrandt langzaam in de zon",
            "Koeien drinken water dat veel methaan bevat",
        ],
        0,
        "Dat gisten gebeurt in de maag van het dier.",
    ),
    keuze(
        "Sinds het begin van de industrie is de aarde gemiddeld ongeveer [[*1,2 °C|0,2 °C|5 °C]] warmer geworden.",
        "Dat lijkt weinig, maar het is een wereldgemiddelde.",
    ),
    tabel(
        "Klopt dit over bossen en het klimaat?",
        [
            ("Groeiende bomen halen CO2 uit de lucht.", J),
            ("Een bos slaat koolstof op in hout en bodem.", J),
            ("Een bos kappen en verbranden geeft CO2 vrij.", J),
            ("Een oud bos legt elk jaar meer vast dan een jong.", F),
        ],
        "Vooral groeiende bossen leggen veel koolstof vast.",
    ),
    tabel(
        "Klopt dit over de Milanković-cycli en de opwarming van nu?",
        [
            ("Ze werken over tienduizenden jaren.", J),
            ("Ze zouden nu eerder lichte afkoeling geven.", J),
            ("Ze verklaren de opwarming van de laatste eeuw.", F),
        ],
        "De opwarming van nu komt van de mens.",
    ),
    open_(
        "Leg uit wat het verschil is tussen het natuurlijke en het versterkte broeikaseffect.",
        "Het natuurlijke broeikaseffect bestaat altijd al: gassen zoals waterdamp en CO2 houden een deel van de warmte vast, waardoor het op aarde leefbaar is. Bij het versterkte broeikaseffect brengt de mens extra broeikasgassen in de lucht, door fossiele brandstoffen te verbranden, bossen te kappen en veeteelt. Daardoor wordt er meer warmte vastgehouden en warmt de aarde op.",
    ),
]

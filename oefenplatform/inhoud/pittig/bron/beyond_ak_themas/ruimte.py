"""Verstedelijking en ruimtegebruik — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Fasen van verstedelijking ----------------------------------------------
FV = Prent("fasen-verstedelijking", "Inwoners van de stadskern en van de rand doorheen de tijd (model)", "twee lijnen, kern en rand, met vier fasen 1 tot 4")
L, R_, B, O = 120, 920, 100, 500
FV.lijn(L, O, R_, O, DONKER, 2)
FV.lijn(L, O, L, B, DONKER, 2)
FV.tekst(L - 10, B - 14, "inwoners", 15, "start")
FV.tekst(R_, O + 30, "tijd", 15, "end")
for x in (320, 520, 720):
    FV.lijn(x, B, x, O, GRIJS, 1, stippel=True)
for i, x in enumerate((220, 420, 620, 820), 1):
    FV.letter(x, 70 + 0 * i, str(i))
FV.pad(f"M{L} 440 C 220 300 280 200 320 200 C 400 200 460 250 520 300 C 580 340 660 360 720 340 C 800 310 860 260 {R_} 240", "none", ROOD, 4)
FV.pad(f"M{L} 470 C 220 460 280 420 320 400 C 400 340 460 220 520 210 C 600 200 660 260 720 300 C 800 330 860 340 {R_} 345", "none", BLAUW, 4)
FV.lijn(560, 545, 600, 545, ROOD, 4)
FV.tekst(610, 551, "kern", 16, "start")
FV.lijn(700, 545, 740, 545, BLAUW, 4)
FV.tekst(750, 551, "rand", 16, "start")
ZFV = {str(i): [Prent.zone(x0, B - 50, 200, O - B + 50)] for i, x0 in enumerate((120, 320, 520, 720), 1)}

# Een Vlaamse gemeente van bovenaf ----------------------------------------
VG = Prent("gemeente-bovenaf", "Een Vlaamse gemeente van bovenaf (schematisch)", "dorpskern K, lange rij huizen langs een weg L, verkaveling met doodlopende straten M, open ruimte N")
VG.rect(40, 60, 920, 560, "#dfe8c9", "none", 0, 0)
VG.pad("M40 340 L 960 300", "none", "#999", 10)
VG.pad("M420 60 L 440 620", "none", "#999", 10)
for x, y in ((380, 280), (400, 300), (460, 290), (470, 350), (390, 360), (460, 380), (410, 250), (480, 260)):
    VG.rect(x, y, 26, 22, "#c0603a", DONKER, 2, 1)
VG.cirkel(430, 320, 14, "#efe8d2", DONKER, 1)
for i in range(10):
    x = 520 + i * 42
    y = 340 - (x - 40) * 40 / 920 - 30
    VG.rect(x, y, 24, 18, "#c0603a", DONKER, 2, 1)
VG.pad("M150 460 L 340 460 M 200 460 L 200 560 M 280 460 L 280 560 M 340 460 L 340 330", "none", "#bbb", 6)
for x in (170, 220, 250, 300):
    for y in (480, 520, 550):
        VG.rect(x - 8, y - 8, 16, 14, "#c0603a", DONKER, 2, 1)
for x, y in ((700, 460), (760, 500), (820, 450), (650, 540), (880, 530)):
    VG.cirkel(x, y, 18, "#8fb36a", "none", 0)
VG.rect(600, 100, 300, 120, "#e8e0b0", "none", 0, 0)
LVG = {"K": (520, 400), "L": (760, 230), "M": (120, 420), "N": (760, 430)}
for k, (x, y) in LVG.items():
    VG.letter(x, y, k)
ZVG = {"K": [Prent.zone(370, 240, 140, 150), Prent.rond(*LVG["K"], 26)],
       "L": [Prent.zone(510, 260, 440, 50), Prent.rond(*LVG["L"], 26)],
       "M": [Prent.zone(150, 455, 200, 110), Prent.rond(*LVG["M"], 26)],
       "N": [Prent.zone(600, 400, 340, 200), Prent.zone(600, 90, 300, 130), Prent.rond(*LVG["N"], 26)]}

VRAGEN = [
    klik(
        "Klik op de fase waarin de rand sterk groeit terwijl de kern inwoners verliest.",
        FV.bestand, ZFV["2"],
        "Dat is suburbanisatie.",
    ),
    klik(
        "Klik op de fase waarin de kern opnieuw inwoners wint.",
        FV.bestand, ZFV["4"],
        "Dat is re-urbanisatie.",
    ),
    met_prent(FV.bestand, tabel(
        "Kijk naar het model. Welke fase is dit?",
        [
            ("urbanisatie", "1"),
            ("suburbanisatie", "2"),
            ("desurbanisatie", "3"),
            ("re-urbanisatie", "4"),
        ],
        "Eerst groeit de kern, dan de rand, dan krimpt het geheel, dan herleeft de kern.",
        kolommen=["1", "2", "3", "4"],
    )),
    met_prent(FV.bestand, tabel(
        "Kijk naar de lijnen van kern en rand. Klopt dit?",
        [
            ("In fase 1 groeit vooral de kern.", J),
            ("In fase 3 dalen kern en rand allebei.", J),
            ("In fase 2 groeit de kern het snelst.", F),
        ],
        "In fase 2 trekt wie kan naar de rand.",
    )),
    klik(
        "Klik op de lintbebouwing.",
        VG.bestand, ZVG["L"],
        "Een lange rij huizen langs een weg.",
    ),
    klik(
        "Klik op de verkaveling.",
        VG.bestand, ZVG["M"],
        "Een stuk grond opgedeeld in bouwpercelen met eigen straten.",
    ),
    met_prent(VG.bestand, tabel(
        "Kijk naar de gemeente van bovenaf. Klopt dit?",
        [
            ("Bij K is bouwen volgens de bouwshift het best.", J),
            ("L snijdt de open ruimte in stukken.", J),
            ("Bij M hebben de bewoners voor bijna alles een wagen nodig.", J),
            ("N is de dorpskern.", F),
        ],
        "N is open ruimte met akkers en bos.",
    )),
    tabel(
        "Welke fase van verstedelijking is dit?",
        [
            ("door de industrie trekken mensen naar de stad", "urbanisatie"),
            ("stedelingen gaan in landelijke dorpen wonen", "rurbanisatie"),
            ("studenten en jonge werkenden zoeken de stadskern weer op", "re-urbanisatie"),
            ("gezinnen kopen een woning met tuin aan de stadsrand", "suburbanisatie"),
        ],
        "Rurbanisatie gaat verder dan de rand: tot op het platteland.",
        kolommen=["urbanisatie", "suburbanisatie", "rurbanisatie", "re-urbanisatie"],
    ),
    tabel(
        "Welke woonvorm vind je typisch waar?",
        [
            ("negentiende-eeuwse gordel", "rijwoning"),
            ("verkaveling aan de rand", "vrijstaande woning"),
            ("gerenoveerd pakhuis in de kern", "appartement"),
        ],
        "Hoe verder van de kern, hoe meer grond per woning.",
        kolommen=["rijwoning", "vrijstaande woning", "appartement"],
    ),
    casus(
        "Een oude arbeiderswijk bij het station wordt hip: er komen koffiebars, de huizen worden gerenoveerd en de prijzen stijgen.",
        [
            keuze(
                "Dat heet [[*gentrificatie|suburbanisatie|rurbanisatie]].",
                "Een volkswijk komt in de mode.",
            ),
            tabel(
                "Klopt dit over de gevolgen?",
                [
                    ("De wijk wordt netter en veiliger.", J),
                    ("Oorspronkelijke bewoners kunnen de huur vaak niet meer betalen.", J),
                    ("De sociale mix blijft altijd dezelfde.", F),
                ],
                "Gentrificatie heeft winnaars en verliezers.",
            ),
        ],
    ),
    mk(
        "Waarom is Vlaanderen 's nachts op satellietbeelden bijna overal verlicht?",
        [
            "Huizen en wegen liggen verspreid over het hele land",
            "Vlaanderen heeft de grootste steden van heel Europa",
            "In Vlaanderen staan de straatlampen feller dan elders",
            "Alle Vlamingen wonen in enkele grote stadskernen",
        ],
        0,
        "Dat beeld past bij de nevelstad Vlaanderen.",
    ),
    tabel(
        "Klopt dit over het stedelijk hitte-eiland?",
        [
            ("Beton en asfalt slaan warmte op.", J),
            ("Het verschil is het grootst op een zomernacht.", J),
            ("Groen en water koelen de stad af.", J),
            ("Overdag is het platteland altijd warmer.", F),
        ],
        "'s Nachts koelt het platteland sneller af.",
    ),
    koppel(
        "Koppel elk plan aan zijn kenmerk.",
        [
            ("gewestplan", "kleurde in de jaren zeventig elk perceel in"),
            ("RSV", "wou vanaf 1997 de groei bundelen in de steden"),
            ("BRV", "wil het bijkomend ruimtebeslag naar nul brengen"),
        ],
        ["verbiedt elke nieuwe woning", "schaft alle woongebieden af"],
        "Nieuwe woningen mogen nog, maar niet in de open ruimte.",
    ),
    sorteer(
        "Is dit een gevolg van verspreide bebouwing?",
        ["Gevolg", "Geen gevolg"],
        [
            ("duurdere leidingen per woning", "Gevolg"),
            ("meer autoverkeer", "Gevolg"),
            ("versnipperde natuur", "Gevolg"),
            ("kortere ritten naar school", "Geen gevolg"),
        ],
        "Verspreid wonen maakt afstanden net langer.",
    ),
    inv(
        "Een gemeente is 30 km² groot. Een derde is ruimtebeslag. Hoeveel km² is dat?",
        ["10"],
        "30 : 3 = 10 km².",
    ),
    mk(
        "Veel Vlamingen verzetten zich tegen de bouwshift. Wat is de belangrijkste reden?",
        [
            "Eigenaars van bouwgrond kunnen veel waarde verliezen",
            "Er is in de steden helemaal geen plaats meer om te bouwen",
            "De bouwshift verbiedt alle renovaties in de kernen",
            "Niemand weet waar de open ruimte in Vlaanderen ligt",
        ],
        0,
        "Veel percelen staan nog als woongebied op het gewestplan.",
    ),
    tabel(
        "Klopt dit over verharding?",
        [
            ("Verharde grond laat geen water door.", J),
            ("Ze verhoogt het risico op wateroverlast.", J),
            ("Ze warmt sterk op in de zon.", J),
            ("Ze vult het grondwater sneller aan.", F),
        ],
        "Regen loopt af in plaats van in de bodem te zakken.",
    ),
    sleep(
        "Wie in de rand woont en elke dag naar de stad gaat werken, is aan het [[pendelen]]. Dat zorgt voor [[files]] op de invalswegen.",
        ["verkavelen", "verharding"],
        "Hoe verder je woont, hoe langer je rit.",
    ),
    tabel(
        "Droeg dit bij aan de groei van de Vlaamse rand in de twintigste eeuw?",
        [
            ("goedkope treinabonnementen voor arbeiders", J),
            ("later de wagen voor bijna elk gezin", J),
            ("de overheid moedigde een eigen woning aan", J),
            ("een verbod op bouwen buiten de stad", F),
        ],
        "Er was net weinig regelgeving over waar je mocht bouwen.",
    ),
    keuze(
        "Groepen met eenzelfde inkomen of afkomst die in aparte wijken gaan wonen: dat heet sociale [[*segregatie|gentrificatie|urbanisatie]].",
        "Zo ontstaan rijke en arme buurten naast elkaar.",
    ),
    mk(
        "Een gezin woont in een dorpskern, een ander in een verkaveling ver buiten het dorp. Wat klopt meestal?",
        [
            "Het gezin in de kern verbruikt minder ruimte en energie",
            "Het gezin in de verkaveling rijdt minder kilometer met de wagen",
            "Beide gezinnen gebruiken evenveel ruimte en evenveel energie",
            "Het gezin in de kern betaalt meer voor leidingen en wegen",
        ],
        0,
        "Kleinere woningen, gedeelde muren en korte afstanden.",
    ),
    tabel(
        "Welke kernkwaliteit van het BRV is dit?",
        [
            ("school, winkel en werk op wandelafstand", "nabijheid"),
            ("een halte van bus of trein dichtbij", "bereikbaarheid"),
            ("plaats voor parken en waterlopen", "groen en water"),
        ],
        "Een goede plek combineert die kwaliteiten.",
        kolommen=["nabijheid", "bereikbaarheid", "groen en water"],
    ),
    keuze(
        "Sinds ongeveer [[*2007|1907|1957]] woont wereldwijd meer dan de helft van de mensen in een stad.",
        "De verstedelijking gaat vooral in Azië en Afrika snel.",
    ),
    tabel(
        "Klopt dit over urban sprawl?",
        [
            ("Het is lage, verspreide bebouwing rond een stad.", J),
            ("Het vraagt veel ruimte per inwoner.", J),
            ("Het maakt openbaar vervoer goedkoper.", F),
        ],
        "Weinig mensen per km² maakt een bus duur.",
    ),
    mk(
        "Welke groep trekt bij desurbanisatie vaak weg uit het hele stedelijk gebied?",
        [
            "Gezinnen op zoek naar rust op het platteland",
            "Studenten die dicht bij de hogeschool willen wonen",
            "Ouderen die dichter bij het ziekenhuis willen wonen",
            "Jonge werkenden die naar de stadskern verhuizen",
        ],
        0,
        "Ze nemen hun stedelijke levensstijl mee naar het dorp.",
    ),
    tabel(
        "Ruimtebeslag of geen ruimtebeslag?",
        [
            ("een tuin bij een woning", "Ruimtebeslag"),
            ("een parking", "Ruimtebeslag"),
            ("een akker", "Geen ruimtebeslag"),
            ("een bos", "Geen ruimtebeslag"),
        ],
        "Ook tuinen en parkings tellen mee, niet enkel gebouwen.",
        kolommen=["Ruimtebeslag", "Geen ruimtebeslag"],
    ),
    tabel(
        "Klopt dit over de nevelstad Vlaanderen?",
        [
            ("Er is geen scherpe grens tussen stad en platteland.", J),
            ("Bebouwing ligt als een nevel over het land.", J),
            ("Er liggen grote lege gebieden tussen de steden.", F),
        ],
        "Overal liggen huizen, wegen en bedrijven verspreid.",
    ),
    keuze(
        "Een stuk landbouwgrond wordt opgedeeld in bouwpercelen met wegen en leidingen. Dat is een [[*verkaveling|lintbebouwing|gentrificatie]].",
        "Typisch voor de groei van de rand.",
    ),
    open_(
        "Leg uit waarom het BRV wil dat er vooral in de kernen gebouwd wordt.",
        "In de kernen liggen school, winkel, werk en openbaar vervoer dichtbij, dus moeten mensen minder met de wagen rijden. Leidingen en wegen liggen er al. Zo blijft de open ruimte gespaard voor landbouw, natuur en water, en vermijd je extra verharding.",
    ),
]

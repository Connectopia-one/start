"""Inkomensongelijkheid, armoede en herverdeling — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

G = venster("ongelijkheid-lorenzcurven", 0, 100, 0, 100, 20, 20)
LAND_A = [(0, 0), (20, 8), (40, 20), (60, 36), (80, 58), (100, 100)]
LAND_B = [(0, 0), (20, 4), (40, 12), (60, 26), (80, 48), (100, 100)]


def lijn(pts):
    def f(x):
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if x0 <= x <= x1:
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        return None
    return f


GRAFIEKEN = [
    dict(naam=G, titel="Lorenzcurven van land A en land B",
         krommen=[(lambda x: x, "oranje", "", (0, 100)), (lijn(LAND_A), "blauw", "A", (0, 100)), (lijn(LAND_B), "groen", "B", (0, 100))],
         labelplek={"A": (72, 49), "B": (88, 51)},
         punten=[(x, y, "") for x, y in LAND_A[1:-1] + LAND_B[1:-1]],
         xlabel="% bevolking (van arm naar rijk)", ylabel="% inkomen", ijk_x=20, ijk_y=20),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat="Twee Lorenzcurven (land A en land B) en de diagonaal", vragen="klikvragen en rekenvragen over de Lorenzcurve en de Gini")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "Klik op de lijn die een perfect gelijke inkomensverdeling voorstelt.",
        P, [vak_zone(G, 30, 45, 31, 46)],
        "Bij perfecte gelijkheid heeft de armste 20 % ook 20 % van het inkomen: de diagonaal.",
    ),
    klik(
        "Klik op het punt dat toont welk deel van het inkomen de armste 40 % van land B samen heeft.",
        P, [punt_zone(G, 40, 12)],
        "Op curve B, boven 40 % van de bevolking: samen 12 % van het inkomen.",
    ),
    met_prent(P, mk(
        "Welk land heeft de grootste inkomensongelijkheid?",
        ["Land B, want zijn curve ligt het verst van de diagonaal", "Land A, want zijn curve ligt het dichtst bij de diagonaal",
         "Land B, want zijn curve ligt het dichtst bij de diagonaal", "Ze zijn even ongelijk, want beide curven eindigen in 100 %"],
        0,
        "Hoe verder van de diagonaal, hoe ongelijker.",
    )),
    met_prent(P, inv(
        "De oppervlakte tussen de diagonaal en de Lorenzcurve van land B is 0,22. Bereken de Gini-coëfficiënt. Schrijf het getal met een komma.",
        "0,44",
        "Gini = 0,22 / 0,5 = 0,44.",
    )),
    met_prent(P, inv(
        "Hoeveel procent van het inkomen heeft de rijkste 20 % van land A samen? Schrijf enkel het getal.",
        "42",
        "De armste 80 % heeft 58 %, dus de rijkste 20 % heeft 100 − 58 = 42 %.",
    )),
    met_prent(P, mk(
        "Land A voert een sterker progressieve belasting in en verhoogt de uitkeringen. Wat gebeurt er met zijn Lorenzcurve?",
        ["Ze schuift dichter naar de diagonaal", "Ze schuift verder van de diagonaal",
         "Ze valt samen met de curve van land B", "Ze verandert niet, want het bbp blijft gelijk"],
        0,
        "Herverdeling van rijk naar arm maakt de verdeling gelijker: de curve schuift naar de diagonaal en de Gini daalt.",
    )),
    tabel(
        "Gaat dit over de personele of de categoriale inkomensverdeling?",
        [
            ("Welk deel van het inkomen gaat naar de armste 10 % van de gezinnen?", "Personele"),
            ("Welk deel van het nationaal inkomen gaat naar lonen en welk deel naar winsten?", "Categoriale"),
            ("Hoeveel verdienen de rijkste 1 % van de personen?", "Personele"),
            ("Hoeveel van het inkomen gaat naar huur en intrest?", "Categoriale"),
        ],
        "Personeel: over personen of gezinnen. Categoriaal: over de productiefactoren (loon, intrest, huur, winst).",
        kolommen=["Personele", "Categoriale"],
    ),
    tabel(
        "Waar of niet waar over de Gini-coëfficiënt?",
        [
            ("Een Gini van 0 betekent perfecte gelijkheid.", J),
            ("Een land met Gini 0,26 is ongelijker dan een land met Gini 0,45.", F),
            ("Een lage Gini betekent dat een land rijk is.", F),
            ("Stijgt de Gini jaar na jaar, dan neemt de ongelijkheid toe.", J),
        ],
        "Hoe hoger de Gini, hoe ongelijker. Een lage Gini zegt niets over hoe rijk een land is.",
    ),
    mk(
        "Een land heeft een heel lage Gini, maar bijna iedereen is er arm. Kan dat?",
        ["Ja: iedereen heeft dan ongeveer even weinig", "Nee: een lage Gini betekent altijd dat er weinig armoede is",
         "Nee: een arm land heeft altijd een Gini dicht bij 1", "Ja, maar enkel als de overheid geen belastingen heft"],
        0,
        "Ongelijkheid en armoede zijn niet hetzelfde. De Gini meet verschillen, niet het niveau.",
    ),
    mk(
        "Hoe staat België ervoor op het vlak van inkomensongelijkheid, in vergelijking met veel andere landen?",
        ["Het heeft een relatief lage Gini", "Het heeft een Gini dicht bij 1", "Het heeft een Gini van precies 0", "Het meet geen Gini"],
        0,
        "België heeft in vergelijking met veel andere landen een relatief lage Gini.",
    ),
    sorteer(
        "Is dit een oorzaak van inkomensongelijkheid?",
        ["Wel een oorzaak", "Geen oorzaak"],
        [
            ["Verschillen in opleiding en beroep", "Wel een oorzaak"],
            ["Verschillen in vermogen, dat zelf huur, intrest of dividend oplevert", "Wel een oorzaak"],
            ["Het sociaal milieu: kansen op onderwijs, netwerk en steun thuis", "Wel een oorzaak"],
            ["Een progressieve personenbelasting", "Geen oorzaak"],
            ["De gezinsbijslag", "Geen oorzaak"],
        ],
        "Belastingen en sociale uitkeringen verkleinen de ongelijkheid net.",
    ),
    koppel(
        "Koppel elke armoede-indicator aan wat ze meet.",
        [
            ["AROP", "Inkomen onder 60 % van het mediaaninkomen"],
            ["SMSD", "Je kan je basisdingen niet veroorloven"],
            ["LWI", "Gezinnen met een lage werkintensiteit"],
            ["AROPE", "Minstens één van de drie andere"],
        ],
        ["Inkomen onder 50 % van het gemiddelde inkomen"],
        "De armoedegrens ligt op 60 % van het mediaaninkomen, niet van het gemiddelde.",
    ),
    inv(
        "Het mediaaninkomen in een land is 2 100 euro per maand. Onder welk bedrag ligt de armoedegrens voor AROP? Schrijf enkel het getal.",
        "1260",
        "60 % van 2 100 = 1 260 euro.",
    ),
    mk(
        "Waarom gebruikt men voor de armoedegrens het mediaaninkomen en niet het gemiddelde inkomen?",
        ["De mediaan reageert minder op enkele hoge inkomens", "Het gemiddelde is altijd lager dan de mediaan",
         "De mediaan is gemakkelijker uit te rekenen", "Het gemiddelde inkomen wordt in België niet gemeten"],
        0,
        "Enkele heel hoge inkomens trekken het gemiddelde omhoog, de mediaan niet.",
    ),
    inv(
        "Een land telt 12 miljoen inwoners. 1,5 miljoen van hen hebben een inkomen onder 60 % van het mediaaninkomen. Hoe groot is de AROP in procent? Schrijf het getal met een komma.",
        "12,5",
        "1,5 / 12 = 0,125 = 12,5 %.",
    ),
    casus(
        "Een personenbelasting heeft twee schijven: 25 % op de eerste 15 000 euro, en 50 % op alles daarboven.",
        [
            inv("Hoeveel belasting betaalt iemand die 10 000 euro verdient? Schrijf enkel het getal.", "2500",
                "25 % van 10 000 = 2 500 euro."),
            inv("Hoeveel belasting betaalt iemand die 40 000 euro verdient? Schrijf enkel het getal.", "16250",
                "25 % van 15 000 = 3 750, plus 50 % van 25 000 = 12 500. Samen 16 250 euro."),
            mk("Is deze belasting progressief?",
               ["Ja: elke hogere schijf krijgt een hoger tarief", "Nee: iedereen betaalt hetzelfde percentage",
                "Nee: wie meer verdient, betaalt een kleiner deel", "Ja, maar enkel voor wie onder 15 000 euro verdient"], 0,
               "Elke hogere inkomensschijf krijgt een hoger tarief: dat is progressief."),
        ],
    ),
    mk(
        "Wat is een vlaktaks?",
        ["Iedereen betaalt hetzelfde percentage belasting", "Wie meer verdient, betaalt een hoger percentage",
         "Iedereen betaalt hetzelfde bedrag in euro", "Een belasting op woningen met een plat dak"],
        0,
        "Een vlaktaks verkleint de ongelijkheid minder sterk dan een progressieve belasting.",
    ),
    tabel(
        "Is dit een vervangingsinkomen of een aanvulling op het inkomen?",
        [
            ("Een pensioen", "Vervangingsinkomen"),
            ("Een werkloosheidsuitkering", "Vervangingsinkomen"),
            ("De gezinsbijslag (het Groeipakket)", "Aanvulling op het inkomen"),
        ],
        "Een vervangingsinkomen komt in de plaats van een loon. De gezinsbijslag komt erbovenop.",
        kolommen=["Vervangingsinkomen", "Aanvulling op het inkomen"],
    ),
    tabel(
        "Hoort dit bij de zeven takken van de sociale zekerheid?",
        [
            ("Beroepsziekten", "Wel"),
            ("Jaarlijkse vakantie", "Wel"),
            ("Arbeidsongevallen", "Wel"),
            ("Het leefloon", "Niet"),
        ],
        "De zeven takken: pensioenen, werkloosheid, ziekte en invaliditeit, arbeidsongevallen, beroepsziekten, gezinsbijslag en jaarlijkse vakantie. Het leefloon is bijstand voor wie geen inkomen heeft.",
        kolommen=["Wel", "Niet"],
    ),
    keuze(
        "Volgens het [[*solidariteitsprincipe|verzekeringsprincipe]] dragen de sterkste schouders de zwaarste lasten. Volgens het [[*verzekeringsprincipe|solidariteitsprincipe]] is wie bijdraagt verzekerd tegen risico's.",
        "De sociale zekerheid steunt op beide principes.",
    ),
    mk(
        "Een gezin heeft een inkomen boven de armoedegrens, maar kan de huur en de verwarming niet betalen. Bij welke indicator telt het mee?",
        ["SMSD, en dus ook AROPE", "AROP, en dus ook AROPE", "LWI, maar niet AROPE", "Bij geen enkele indicator"],
        0,
        "Het kan zich de basisdingen niet veroorloven: ernstige materiële en sociale deprivatie. AROPE telt wie met minstens één van de drie te maken heeft.",
    ),
    sleep(
        "Op de assen van een Lorenzcurve staan het [[cumulatieve]] percentage van de bevolking, van [[arm]] naar rijk, en het cumulatieve percentage van het [[inkomen]].",
        ["gemiddelde", "rijk", "vermogen"],
        "Een punt (20 %, 6 %) betekent: de armste 20 % heeft samen 6 % van het inkomen.",
    ),
    open_(
        "Leg uit hoe belastingen en sociale zekerheid de Gini-coëfficiënt van een land verlagen.",
        "Een progressieve personenbelasting neemt een groter percentage van hoge inkomens. Met dat geld betaalt de overheid uitkeringen, zoals werkloosheid, pensioenen en gezinsbijslag, en een leefloon. Zo gaat er inkomen van rijk naar arm: de Lorenzcurve schuift naar de diagonaal en de Gini daalt.",
    ),
    met_prent(P, mk(
        "Hoeveel procent van het inkomen heeft de armste 20 % van land A samen?",
        ["8 %", "20 %", "4 %", "12 %"],
        0,
        "Op curve A, boven 20 % van de bevolking: 8 %.",
    )),
    mk(
        "De oppervlakte tussen de diagonaal en de Lorenzcurve van een land is 0,1. Hoe groot is de Gini?",
        ["0,2", "0,1", "0,05", "0,4"],
        0,
        "Gini = 0,1 / 0,5 = 0,2.",
    ),
    tabel(
        "Ongelijkheid of armoede: waarover gaat deze uitspraak?",
        [
            ("De rijkste 10 % verdient tien keer zoveel als de armste 10 %.", "Ongelijkheid"),
            ("Eén op acht gezinnen kan geen onverwachte rekening betalen.", "Armoede"),
            ("De Gini steeg van 0,26 naar 0,29.", "Ongelijkheid"),
            ("Het aantal mensen met een leefloon stijgt.", "Armoede"),
        ],
        "Ongelijkheid gaat over verschillen, armoede over wie te weinig heeft.",
        kolommen=["Ongelijkheid", "Armoede"],
    ),
    mk(
        "Wat helpt, naast de sociale zekerheid, nog tegen armoede?",
        ["Een leefloon en sociale woningen", "Een vlaktaks en hogere huurprijzen", "Minder kinderbijslag", "Een hogere btw op voeding"],
        0,
        "Een leefloon voor wie geen inkomen heeft en sociale woningen helpen rechtstreeks.",
    ),
    volgorde(
        "Zet deze landen van gelijk naar ongelijk.",
        ["Land met Gini 0,24", "Land met Gini 0,31", "Land met Gini 0,42", "Land met Gini 0,58"],
        "Hoe hoger de Gini, hoe groter de ongelijkheid.",
    ),
]

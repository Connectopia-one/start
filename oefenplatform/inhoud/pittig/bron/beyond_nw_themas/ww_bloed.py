"""Welzijnswetenschappen: het bloed — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en een eigen prent van een bloedgroepentest: bloedcellen,
hemoglobine en EPO, plasma, witte bloedcellen en afweer, stolling,
bloedgroepen en resusfactor.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, ROOD

# Een bloedgroepentest voor vier personen -------------------------------------------
BT = Prent("bloedgroepentest", "Een bloedgroepentest", "vier rijen P, Q, R en S; per rij twee druppels bloed, links gemengd met anti-A en rechts met anti-B; een klonterige druppel toont rode stipjes, een gladde druppel is egaal rood")
BT.tekst(430, 90, "druppel + anti-A", 20, vet=True)
BT.tekst(650, 90, "druppel + anti-B", 20, vet=True)
KLONT = {"P": (True, False), "Q": (False, True), "R": (True, True), "S": (False, False)}
RIJ = {}
for i, (k, (a, b)) in enumerate(KLONT.items()):
    y = 160 + i * 125
    RIJ[k] = y
    BT.rect(110, y - 55, 680, 110, "#ffffff", "#8a8470", 12, 1)
    BT.letter(170, y, k)
    for x, klont in ((430, a), (650, b)):
        if klont:
            BT.cirkel(x, y, 44, "#f6dcd8", ROOD, 2)
            for dx, dy in ((-20, -15), (5, -22), (22, -2), (-12, 12), (12, 20), (-25, 5), (0, 2)):
                BT.cirkel(x + dx, y + dy, 6, ROOD, ROOD, 1)
        else:
            BT.cirkel(x, y, 44, "#d9534f", ROOD, 2)
ZB = {k: [Prent.zone(110, y - 55, 680, 110)] for k, y in RIJ.items()}

EIGEN = [
    klik("Klik op de persoon met bloedgroep O.", BT.bestand, ZB["S"],
         "Geen A- en geen B-antigenen, dus geen enkele druppel klontert."),
    klik("Klik op de persoon die van elke ABO-groep rode bloedcellen kan krijgen.", BT.bestand, ZB["R"],
         "Bloedgroep AB heeft geen anti-A en geen anti-B in het plasma. Beide druppels klonteren, want A en B zitten op de cellen."),
    klik("Klik op elke persoon die anti-B-antilichamen in het plasma heeft.", BT.bestand, ZB["P"] + ZB["S"],
         "Groep A en groep O hebben anti-B. Bij P klontert enkel de druppel met anti-A, bij S geen enkele."),
    met_prent(BT.bestand, tabel("Welke bloedgroep heeft deze persoon?", [
        ("P", "A"), ("Q", "B"), ("R", "AB"), ("S", "O"),
    ], "Een druppel klontert als het antigen op de rode bloedcellen past bij het antilichaam dat je toevoegt.",
       kolommen=["A", "B", "AB", "O"])),
    met_prent(BT.bestand, keuze("Het samenklonteren in de druppels heet [[*agglutinatie|stolling|fagocytose]].",
              "Bij stolling vormen bloedplaatjes en fibrine een stolsel. Hier kleven rode bloedcellen samen door antilichamen.")),
    casus(
        "Bij een bloedafname heeft Amira een hematocrietwaarde van 52 procent. Ze komt "
        "net terug van drie weken hoogtestage in de bergen. Haar trainer vraagt zich af "
        "of dat gezond is.",
        [
            mk("Hoe komt het dat haar hematocriet hoger is dan normaal?",
               ["In de ijle lucht maakten haar nieren meer EPO",
                "In de ijle lucht maakte haar lever meer albumine",
                "Haar witte bloedcellen werden groter door de kou",
                "Haar bloedplaatjes hielden extra zuurstof vast"], 0,
               "Bij zuurstoftekort maken de nieren meer EPO en het rode beenmerg meer rode bloedcellen."),
            tabel("Klopt dit?", [
                ("De hematocriet is het percentage rode bloedcellen in het bloed.", J),
                ("Een te hoge hematocriet maakt het bloed dikker.", J),
                ("Meer rode bloedcellen is altijd beter.", F),
            ], "Te dik bloed stroomt moeilijker en verhoogt het risico op een bloedklonter."),
            keuze("Rode bloedcellen worden gemaakt in het [[*rode beenmerg|gele beenmerg|lymfeklieren]].",
                  "Alle bloedcellen ontstaan uit stamcellen in het rode beenmerg."),
        ],
    ),
    volgorde("Een buisje bloed met een middel tegen stolling wordt gecentrifugeerd. Zet de lagen van onder naar boven.", [
        "rode bloedcellen", "witte bloedcellen en bloedplaatjes", "bloedplasma",
    ], "De zwaarste cellen zakken het diepst. De dunne witte laag in het midden heet de buffy coat."),
    koppel("Koppel elke witte bloedcel aan haar taak.", [
        ["neutrofiel", "ruimt als eerste bacteriën op door fagocytose"],
        ["monocyt", "wordt in het weefsel een macrofaag"],
        ["B-lymfocyt", "wordt plasmacel en maakt antilichamen"],
        ["cytotoxische T-lymfocyt", "doodt lichaamscellen met een virus"],
    ], ["rode bloedcel"], "Samen vormen ze de afweer."),
    volgorde("Zet de stappen van de bloedstolling in de juiste volgorde.", [
        "de wand van een bloedvat raakt beschadigd",
        "bloedplaatjes kleven tegen de wonde",
        "stollingsfactoren starten een cascade",
        "trombine zet fibrinogeen om in fibrine",
        "fibrinedraden vangen bloedcellen en vormen een stolsel",
    ], "De stolling is een kettingreactie die eindigt met een net van fibrine."),
    tabel("Zit dit in bloedplasma, in bloedserum of in beide?", [
        ("fibrinogeen", "enkel plasma"),
        ("albumine", "beide"),
        ("glucose", "beide"),
        ("antilichamen", "beide"),
    ], "Serum is plasma zonder de stollingsfactoren.", kolommen=["enkel plasma", "beide"]),
    mk("Waarom kan een rode bloedcel veel zuurstof vervoeren?",
       ["Ze zit vol hemoglobine en heeft geen celkern",
        "Ze heeft veel mitochondriën die zuurstof opslaan",
        "Ze heeft een dikke celwand die zuurstof vasthoudt",
        "Ze maakt zelf zuurstof aan uit koolstofdioxide"], 0,
       "Zonder kern is er meer plaats voor hemoglobine. De ingedeukte schijfvorm geeft een groot oppervlak."),
    inv("Eén hemoglobinemolecule bindt maximaal vier zuurstofmoleculen. Hoeveel zuurstofmoleculen binden 250 hemoglobinemoleculen maximaal?",
        ["1000", "1 000"], "250 maal 4."),
    sleep("Hemoglobine met zuurstof heet [[oxyhemoglobine]]. Het meeste CO₂ reist als [[waterstofcarbonaat]] opgelost in het plasma.",
          ["fibrine", "albumine"], "Een klein deel CO₂ wordt aan hemoglobine gebonden."),
    tabel("Klopt dit over het zuurstoftransport?", [
        ("Het meeste zuurstof is opgelost in het plasma.", F),
        ("Hemoglobine bevat ijzer.", J),
        ("Een rode bloedcel leeft ongeveer 120 dagen.", J),
        ("Versleten rode bloedcellen worden in de nieren afgebroken.", F),
    ], "Zuurstof gaat vooral gebonden aan hemoglobine. Milt en lever breken oude rode bloedcellen af."),
    tabel("Kan de ontvanger dit bloed (rode bloedcellen) veilig krijgen?", [
        ("ontvanger A, donor O", J),
        ("ontvanger B, donor A", F),
        ("ontvanger AB, donor B", J),
        ("ontvanger O, donor AB", F),
    ], "De antilichamen van de ontvanger mogen niet passen op de antigenen van de donor."),
    mk("Een resusnegatieve moeder is zwanger van haar tweede resuspositief kind. Waarom is er gevaar?",
       ["Bij de eerste bevalling maakte ze anti-D aan",
        "Ze heeft van nature anti-D in haar bloed",
        "Het kind maakt anti-A tegen het bloed van de moeder",
        "Haar bloedplaatjes worden door het kind afgebroken"], 0,
       "Bij de eerste geboorte komt wat bloed van het kind in haar bloed en vormt ze anti-D. Die kunnen bij een volgend kind diens rode bloedcellen aanvallen."),
    sorteer("Is dit een granulocyt of niet?", ["Granulocyt", "Geen granulocyt"], [
        ["neutrofiel", "Granulocyt"],
        ["eosinofiel", "Granulocyt"],
        ["monocyt", "Geen granulocyt"],
        ["B-lymfocyt", "Geen granulocyt"],
    ], "Granulocyten hebben korrels in hun cytoplasma."),
    keuze("Albumine helpt om [[*water in de bloedvaten te houden|zuurstof te binden|bloed te doen stollen]].",
          "Het is het meest voorkomende plasma-eiwit."),
    klik("Klik op de persoon bij wie enkel de druppel met anti-B klontert.", BT.bestand, ZB["Q"],
         "Bij Q zit enkel het B-antigen op de rode bloedcellen: bloedgroep B."),
    met_prent(BT.bestand, mk("Persoon P heeft een bloedtransfusie nodig. Welke donor is veilig?",
       ["Een donor met dezelfde groep als S",
        "Een donor met dezelfde groep als R",
        "Een donor met dezelfde groep als Q",
        "Elke donor, want P heeft geen antilichamen"], 0,
       "P heeft groep A en dus anti-B. Groep O (zoals S) heeft geen antigenen en klontert niet.")),
    koppel("Koppel elk stuk aan zijn rol in de stolling.", [
        ["bloedplaatjes", "vormen eerst een prop tegen de wonde"],
        ["trombine", "zet fibrinogeen om"],
        ["fibrine", "vormt draden die het stolsel versterken"],
    ], ["albumine"], "Fibrinogeen is opgelost; fibrine vormt een net."),
    tabel("Start de stolling hier via de extrinsieke of de intrinsieke route?", [
        ("beschadigd weefsel buiten het bloedvat geeft stoffen af", "extrinsiek"),
        ("bloed komt in contact met een beschadigde vaatwand binnenin", "intrinsiek"),
        ("een snijwonde in de huid beschadigt het weefsel rond het bloedvat", "extrinsiek"),
    ], "Beide routes komen samen in dezelfde eindstappen.", kolommen=["extrinsiek", "intrinsiek"]),
    mk("Waarom moet men bij een bloedtransfusie ook naar de resusfactor kijken?",
       ["Een resusnegatieve ontvanger kan anti-D aanmaken",
        "Een resuspositieve ontvanger verliest dan zijn A-antigenen",
        "De resusfactor bepaalt hoe snel het bloed stolt",
        "Resuspositief bloed bevat geen hemoglobine meer"], 0,
       "Wie resusnegatief is, heeft van nature geen anti-D maar maakt die wel na contact met resuspositief bloed."),
    sleep("Een monocyt die het weefsel ingaat, wordt een [[macrofaag]]. Een geactiveerde B-lymfocyt wordt een [[plasmacel]] die antilichamen maakt.",
          ["erytrocyt", "bloedplaatje"], "Zo werken aangeboren en verworven afweer samen."),
    tabel("Klopt dit over de bloedcellen?", [
        ("Er zijn meer witte dan rode bloedcellen.", F),
        ("Bloedplaatjes zijn stukjes van grote cellen in het beenmerg.", J),
        ("Een rijpe rode bloedcel kan zich niet meer delen.", J),
    ], "Rode bloedcellen zijn veruit het talrijkst; zonder kern delen ze niet."),
    inv("Iemand heeft 5 liter bloed met een hematocriet van 45 procent. Hoeveel liter bestaat uit rode bloedcellen? Rond af op één cijfer na de komma.",
        ["2,3", "2.3", "2,25", "2.25"], "45 procent van 5 liter is 2,25 liter, afgerond 2,3 liter."),
    keuze("Bij een ontsteking komen als eerste [[*neutrofielen|plasmacellen|bloedplaatjes]] ter plaatse.",
          "Neutrofielen zijn de talrijkste witte bloedcellen en ruimen bacteriën op door fagocytose."),
    open_("Leg uit waarom iemand met bloedgroep O rode bloedcellen kan geven aan alle ABO-groepen, maar zelf enkel O kan krijgen.",
          "Op rode bloedcellen van groep O zitten geen A- of B-antigenen, dus geen enkel antilichaam van een ontvanger herkent ze. In het plasma van iemand met groep O zitten wel anti-A en anti-B, die elk bloed met A of B doen klonteren."),
]

VRAGEN = EIGEN

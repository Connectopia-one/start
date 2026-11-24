"""Welzijnswetenschappen: het uitscheidingsstelsel — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en een eigen prent van een nefron: bouw van nier en nefron,
filtratie, resorptie en secretie, osmoregulatie met ADH, aandoeningen en
dialyse.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, ROOD, BLAUW, GEEL

# Een nefron, schematisch, met zes letters ------------------------------------------
NF = Prent("nefron", "Een nefron, schematisch", "een nefron met zes letters: A het bolletje haarvaten, B de beker eromheen, C een kronkelend buisje, D de bocht van een lange lus naar beneden, E een tweede kronkelend buisje, F een dikke buis waarin meerdere nefronen uitkomen; links twee rode bloedvaatjes naar het bolletje")
NF.lijn(60, 140, 160, 160, ROOD, 7)
NF.lijn(60, 205, 160, 185, ROOD, 5)
NF.cirkel(190, 172, 62, "#eef3f8", DONKER, 3)
for dx, dy in ((-14, -10), (10, -14), (16, 8), (-8, 14), (0, 0)):
    NF.cirkel(190 + dx, 172 + dy, 14, "#e8a49c", ROOD, 2)
NF.pad("M252 172 q20 -40 40 0 t40 0 t40 0 t28 0", "none", DONKER, 12)
NF.pad("M252 172 q20 -40 40 0 t40 0 t40 0 t28 0", "none", "#f6efd6", 7)
NF.pad("M400 172 L400 520 Q440 580 480 520 L480 230", "none", DONKER, 12)
NF.pad("M400 172 L400 520 Q440 580 480 520 L480 230", "none", "#f6efd6", 7)
NF.pad("M480 230 q20 -40 40 0 t40 0 t40 0 t40 0 L660 230", "none", DONKER, 12)
NF.pad("M480 230 q20 -40 40 0 t40 0 t40 0 t40 0 L660 230", "none", "#f6efd6", 7)
NF.rect(660, 110, 36, 500, "#f6efd6", DONKER, 6, 3)
NF.pad("M696 150 L760 150", "none", DONKER, 10)
NF.pad("M696 380 L760 380", "none", DONKER, 10)
NF.pijl(678, 560, 678, 630, BLAUW, 4)
for k, (x, y) in {"A": (190, 172), "B": (190, 85), "C": (320, 110), "D": (440, 600), "E": (580, 170), "F": (820, 300)}.items():
    NF.letter(x, y, k)
NF.lijn(800, 300, 698, 300, DONKER, 2)
ZN = {
    "A": [Prent.rond(190, 172, 34)],
    "B": [Prent.zone(140, 60, 100, 50), Prent.zone(122, 110, 30, 130), Prent.zone(228, 110, 30, 130)],
    "C": [Prent.zone(250, 85, 150, 115)],
    "D": [Prent.zone(380, 430, 120, 195)],
    "E": [Prent.zone(480, 145, 180, 110)],
    "F": [Prent.zone(650, 105, 190, 510)],
}

EIGEN = [
    klik("Klik op de plaats waar water en kleine opgeloste stoffen uit het bloed geperst worden.",
         NF.bestand, ZN["A"], "In de glomerulus staat het bloed onder druk. Water en kleine stoffen gaan door de nierfilter naar het kapsel van Bowman."),
    klik("Klik op het deel waar de voorurine eerst terechtkomt.",
         NF.bestand, ZN["B"], "Het kapsel van Bowman vangt het filtraat op als een beker."),
    klik("Klik op het deel waar bij een gezond persoon alle glucose terug naar het bloed gaat.",
         NF.bestand, ZN["C"], "Glucose wordt in het eerste kronkelbuisje volledig teruggeresorbeerd."),
    klik("Klik op het deel dat diep in het niermerg duikt en helpt om geconcentreerde urine te maken.",
         NF.bestand, ZN["D"], "De lus van Henle loopt diep het niermerg in."),
    klik("Klik op het deel dat onder invloed van ADH meer water doorlaat.",
         NF.bestand, ZN["F"], "ADH maakt de wand van de verzamelbuis doorlaatbaarder voor water."),
    met_prent(NF.bestand, tabel("Kijk naar de letters. Klopt dit?", [
        ("In C zit al voorurine.", J),
        ("Rode bloedcellen komen normaal in B terecht.", F),
        ("In F kan nog water terug naar het bloed.", J),
        ("In E komt nog bloed binnen dat gefilterd moet worden.", F),
    ], "Bloedcellen zijn te groot voor de nierfilter. Het filtraat stroomt van B naar C, D, E en zo naar F.")),
    casus(
        "Senne (16) heeft een warme dag lang gefietst en bijna niets gedronken. "
        "Zijn urine is 's avonds weinig en donkergeel. Zijn broer heeft die avond "
        "op een feestje veel bier gedronken en moet telkens plassen.",
        [
            mk("Wat gebeurt er bij Senne?",
               ["Er komt meer ADH, zodat hij meer water terugneemt",
                "Zijn hypofyse geeft minder ADH af, zodat hij water bespaart",
                "Zijn nieren stoppen met filtreren tot hij weer gedronken heeft",
                "Zijn lus van Henle laat glucose door om water vast te houden"], 0,
               "Bij een te geconcentreerd bloed melden osmoreceptoren dat aan de hypothalamus. Er komt meer ADH en de urine wordt geconcentreerd."),
            keuze("Bij zijn broer remt alcohol de afgifte van [[*ADH|EPO|adrenaline]], waardoor hij meer plast.",
                  "Met minder ADH neemt de verzamelbuis minder water terug."),
            tabel("Klopt dit voor Senne?", [
                ("Hij krijgt dorst door een signaal van de hypothalamus.", J),
                ("Zijn verzamelbuizen laten minder water door dan normaal.", F),
                ("Zijn urine bevat relatief veel ureum.", J),
            ], "Weinig water, veel ADH: weinig maar geconcentreerde urine."),
        ],
    ),
    volgorde("Zet de stappen van de urinevorming in de juiste volgorde.", [
        "filtratie in het nierlichaampje",
        "resorptie van glucose en zouten in het eerste kronkelbuisje",
        "concentratie via de lus van Henle",
        "laatste terugname van water in de verzamelbuis",
    ], "Na de verzamelbuis gaat de urine naar het nierbekken."),
    koppel("Koppel elk proces aan wat er gebeurt.", [
        ["filtratie", "water en kleine stoffen gaan van het bloed naar het kapsel"],
        ["resorptie", "nuttige stoffen gaan terug naar het bloed"],
        ["secretie", "extra stoffen gaan actief van het bloed naar het buisje"],
        ["osmoregulatie", "het lichaam houdt water en zouten in evenwicht"],
    ], ["transfusie"], "Samen maken die processen van bloed urine."),
    tabel("Zit dit normaal in de voorurine, in de urine, in beide of in geen van beide?", [
        ("glucose", "enkel voorurine"),
        ("ureum", "beide"),
        ("rode bloedcellen", "geen van beide"),
        ("water", "beide"),
    ], "Glucose wordt volledig teruggeresorbeerd. Bloedcellen passeren de filter niet.",
       kolommen=["enkel voorurine", "beide", "geen van beide"]),
    mk("Waarom vindt een arts glucose in de urine een alarmsignaal?",
       ["Het filtraat bevat meer glucose dan de buisjes kunnen terugnemen",
        "Glucose mag nooit door de nierfilter tot in het kapsel",
        "De lever maakt dan ureum uit glucose in plaats van uit aminozuren",
        "De urineblaas lekt dan suiker uit haar eigen wand"], 0,
       "Bij een te hoge bloedsuiker, zoals bij suikerziekte, raken de transporteiwitten verzadigd."),
    sleep("Het bloed komt de glomerulus binnen via het [[aanvoerend]] nierslagadertje en verlaat ze via het [[afvoerend]] nierslagadertje.",
          ["nierader", "urineleider"], "Het afvoerend vaatje is smaller, zodat de druk in de glomerulus hoog blijft."),
    sorteer("Hoort dit bij de nierschors of bij het niermerg?", ["Nierschors", "Niermerg"], [
        ["de nierlichaampjes", "Nierschors"],
        ["de onderkant van de lus van Henle", "Niermerg"],
        ["de kronkelbuisjes", "Nierschors"],
        ["het grootste stuk van de verzamelbuizen", "Niermerg"],
    ], "De schors ligt buiten, het merg binnen, met de nierpiramiden."),
    inv("Per dag ontstaat ongeveer 180 liter voorurine en 1,5 liter urine. Hoeveel procent van het water wordt teruggeresorbeerd? Rond af op een geheel getal.",
        ["99", "99 %", "99%"], "1,5 van 180 is minder dan 1 procent. Meer dan 99 procent gaat dus terug."),
    keuze("De [[*interne|externe]] kringspier van de blaas werkt onbewust.",
          "De externe kringspier kan je bewust aanspannen."),
    mk("Waarom maakt de nier EPO aan?",
       ["Om de aanmaak van rode bloedcellen te stimuleren",
        "Om de wand van de verzamelbuis waterdoorlatend te maken",
        "Om de bloeddruk in de glomerulus te verlagen bij inspanning",
        "Om ureum af te breken voor het in de urine komt"], 0,
       "Bij een zuurstoftekort maakt de nier meer EPO, en het rode beenmerg meer rode bloedcellen."),
    tabel("Klopt dit over hemodialyse?", [
        ("Het bloed geeft afvalstoffen af aan een spoelvloeistof.", J),
        ("Men legt een shunt aan tussen een slagader en een ader.", J),
        ("Dialyse is nodig wanneer ureum zich in het bloed opstapelt.", J),
        ("Bij dialyse gaan de bloedcellen mee met de spoelvloeistof.", F),
    ], "Het membraan in de kunstnier houdt bloedcellen en grote eiwitten tegen, net als een gezonde nierfilter."),
    koppel("Koppel elke aandoening aan een passende maatregel.", [
        ["blaasontsteking", "behandeling van de bacteriën"],
        ["niersteen", "schokgolven die de steen verbrijzelen"],
        ["nierfalen", "hemodialyse of een niertransplantatie"],
    ], ["minder water drinken"], "Voldoende water drinken helpt net tegen nierstenen en blaasontsteking."),
    mk("Waarom wijst veel eiwit in de urine op een probleem?",
       ["De nierfilter laat dan grote moleculen door",
        "De lever maakt dan te weinig ureum uit eiwitten",
        "De blaas zet dan zelf ureum om in eiwitten",
        "De urineleider maakt dan eiwitten aan in zijn wand"], 0,
       "Grote eiwitten horen in het bloed te blijven."),
    klik("Klik op het tweede kronkelbuisje.",
         NF.bestand, ZN["E"], "Het tweede kronkelbuisje ligt na de lus van Henle en mondt uit in de verzamelbuis."),
    volgorde("Zet de delen in de volgorde waarin de urine ze doorloopt, vanaf de nier.", [
        "nierkelken", "nierbekken", "urineleider", "urineblaas", "urinebuis",
    ], "In het nierbekken komt de urine uit de nierkelken samen."),
    tabel("Klopt dit over de nierfilter?", [
        ("De wand van de haarvaten hoort erbij.", J),
        ("Kleine moleculen zoals glucose en ureum gaan erdoor.", J),
        ("Albumine gaat er bij een gezonde nier vlot door.", F),
    ], "Grote plasma-eiwitten zoals albumine blijven in het bloed."),
    mk("Wat is de functie van de bijnier?",
       ["Hormonen maken, onder meer adrenaline",
        "De urine opslaan tot de blaas vol is",
        "Het bloed filtreren als de nier overbelast raakt",
        "Ureum aanmaken uit de afbraak van aminozuren"], 0,
       "De bijnier ligt als een kapje op de nier, maar hoort bij het hormoonstelsel."),
    keuze("Ureum wordt gemaakt in de [[*lever|nier|blaas]] en uitgescheiden door de nier.",
          "De lever zet het giftige ammoniak uit aminozuren om in ureum."),
    sleep("Een nier telt ongeveer een [[miljoen]] nefronen. Elk nefron begint met een [[nierlichaampje]].",
          ["duizend", "nierbekken"], "Het nierlichaampje is de glomerulus met het kapsel van Bowman."),
    tabel("Gebeurt dit bewust of onbewust?", [
        ("de interne kringspier van de blaas opent", "onbewust"),
        ("je houdt je plas op tot je een toilet vindt", "bewust"),
        ("de afgifte van ADH stijgt na het sporten", "onbewust"),
    ], "Enkel de externe kringspier stuur je bewust aan.", kolommen=["bewust", "onbewust"]),
    inv("Per minuut ontstaat ongeveer 125 ml voorurine. Hoeveel liter is dat per uur?",
        ["7,5", "7.5", "7,5 l", "7,5 liter"], "125 ml maal 60 minuten is 7500 ml, dus 7,5 liter."),
    open_("Leg uit hoe de waterhuishouding een feedbacksysteem is. Gebruik de woorden osmoreceptoren, hypothalamus, ADH en verzamelbuis.",
          "Osmoreceptoren in de hypothalamus merken dat het bloed te geconcentreerd is. De hypofyse geeft dan meer ADH af. ADH maakt de verzamelbuis doorlaatbaarder, zodat meer water teruggaat naar het bloed. Is het bloed weer normaal, dan daalt de ADH-afgifte."),
]

VRAGEN = EIGEN

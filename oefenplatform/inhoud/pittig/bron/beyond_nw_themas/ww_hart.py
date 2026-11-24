"""Welzijnswetenschappen: het hart en de bloedvaten — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en een eigen prent van een schematisch hart: holtes, kleppen,
grote bloedvaten, impulsgeleiding, ECG, hartcyclus, bloedsomloop en
bloedvaten.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, ROOD, BLAUW, GRIJS

# Een schematisch hart, van voren bekeken ---------------------------------------------
HT = Prent("hart-schema", "Een hart, schematisch en van voren bekeken", "vier holtes met letters A tot D: boven twee kleinere (A links, B rechts), onder twee grotere (C links, D rechts, met de dikste wand); tussen boven en onder twee kleppen G en H; twee grote vaten bovenaan: E vertrekt uit D, F vertrekt uit C; links en rechts staat 'rechts' en 'links' van de persoon")
HT.tekst(120, 600, "rechts van de persoon", 16)
HT.tekst(880, 600, "links van de persoon", 16)
HT.rect(200, 190, 250, 140, "#f1e4df", DONKER, 14, 3)      # A rechterboezem
HT.rect(550, 190, 250, 140, "#f1e4df", DONKER, 14, 3)      # B linkerboezem
HT.rect(200, 350, 250, 220, "#f1e4df", DONKER, 14, 4)      # C rechterkamer
HT.rect(550, 350, 250, 220, "#f1e4df", DONKER, 14, 14)     # D linkerkamer
HT.rect(470, 190, 60, 380, GRIJS, DONKER, 6, 2)            # tussenschot
for x in (325, 675):
    HT.svg(f'<polygon points="{x-40},332 {x+40},332 {x},350" fill="#ffffff" stroke="{DONKER}" stroke-width="2"/>')
HT.rect(380, 70, 46, 290, "#f1e4df", DONKER, 8, 3)         # F longslagader uit C
HT.rect(574, 70, 46, 290, "#f1e4df", DONKER, 8, 3)         # E aorta uit D
HT.rect(230, 60, 40, 130, "#f1e4df", DONKER, 8, 3)         # holle ader boven
for k, (x, y) in {"A": (325, 260), "B": (720, 260), "C": (325, 470), "D": (690, 470),
                  "E": (597, 100), "F": (403, 100), "G": (240, 340), "H": (760, 340)}.items():
    HT.letter(x, y, k)
HT.lijn(260, 340, 290, 340, DONKER, 2)
HT.lijn(740, 340, 710, 340, DONKER, 2)
ZH = {
    "A": [Prent.zone(200, 190, 175, 140)], "B": [Prent.zone(625, 190, 175, 140)],
    "C": [Prent.zone(200, 360, 250, 210)], "D": [Prent.zone(550, 360, 250, 210)],
    "E": [Prent.zone(565, 60, 64, 120)], "F": [Prent.zone(371, 60, 64, 120)],
    "G": [Prent.zone(215, 318, 150, 44)], "H": [Prent.zone(635, 318, 150, 44)],
}

EIGEN = [
    klik("Klik op de holte die het bloed door de grote bloedsomloop pompt.", HT.bestand, ZH["D"],
         "De linkerkamer pompt het zuurstofrijke bloed via de aorta naar het hele lichaam. Daarom heeft ze de dikste wand."),
    klik("Klik op de holte waar de holle aders in uitkomen.", HT.bestand, ZH["A"],
         "De holle aders brengen zuurstofarm bloed uit het lichaam naar de rechterboezem."),
    klik("Klik op het bloedvat dat zuurstofarm bloed naar de longen brengt.", HT.bestand, ZH["F"],
         "De longslagader vertrekt uit de rechterkamer. Een slagader voert bloed van het hart weg, ook al is het zuurstofarm."),
    klik("Klik op de klep die het bloed van de linkerboezem naar de linkerkamer doorlaat.", HT.bestand, ZH["H"],
         "De mitralisklep heeft twee slippen en ligt tussen de linkerboezem en de linkerkamer."),
    klik("Klik op de holte waar de longaders in uitkomen.", HT.bestand, ZH["B"],
         "De longaders brengen zuurstofrijk bloed van de longen naar de linkerboezem."),
    met_prent(HT.bestand, tabel("Kijk naar de letters. Bevat dit deel zuurstofrijk of zuurstofarm bloed?", [
        ("A", "zuurstofarm"), ("D", "zuurstofrijk"), ("E", "zuurstofrijk"), ("F", "zuurstofarm"),
    ], "De rechterhelft van het hart (links op de prent) bevat zuurstofarm bloed, de linkerhelft zuurstofrijk.",
       kolommen=["zuurstofrijk", "zuurstofarm"])),
    met_prent(HT.bestand, volgorde("Zet de delen in de volgorde waarin het bloed ze doorloopt, vanaf de holle aders.", [
        "A", "G", "C", "F",
    ], "Holle aders, rechterboezem, tricuspidalisklep, rechterkamer, longslagader.")),
    casus(
        "Op een ECG van een sporter ziet een verpleegkundige elke seconde een P-top, "
        "een QRS-complex en een T-top. Even later krijgt een andere patiënt pijn op de "
        "borst: een kransslagader is verstopt geraakt.",
        [
            koppel("Koppel elk deel van het ECG aan wat het toont.", [
                ["P-top", "de prikkeling van de boezems"],
                ["QRS-complex", "de prikkeling van de kamers"],
                ["T-top", "het herstel van de kamers"],
            ], ["het sluiten van de aortaklep"], "Een ECG meet elektrische activiteit, geen kleppen of geluid."),
            inv("Hoeveel hartslagen per minuut heeft de sporter?", ["60"], "Eén slag per seconde is 60 slagen per minuut."),
            mk("Wat gebeurt er bij de tweede patiënt?",
               ["Een deel van de hartspier krijgt te weinig zuurstof",
                "De sinusknoop stopt en het hart klopt niet meer",
                "De longaders voeren geen zuurstofrijk bloed meer aan",
                "Het bloed stroomt plots achteruit door de mitralisklep"], 0,
               "Achter de verstopping krijgt de hartspier geen zuurstof meer: een hartinfarct."),
        ],
    ),
    volgorde("Zet de delen van het impulsgeleidingssysteem in de juiste volgorde.", [
        "sinusknoop", "AV-knoop", "bundel van His", "vezels van Purkinje",
    ], "De prikkel start in de rechterboezem en eindigt in de wand van de kamers."),
    mk("Wat zou er gebeuren als de AV-knoop de prikkel niet even vertraagde?",
       ["Boezems en kamers trekken tegelijk samen",
        "Het hart zou helemaal geen prikkel meer krijgen van de sinusknoop",
        "De kleppen tussen boezem en kamer zouden altijd openblijven",
        "De kransslagaders zouden geen bloed meer naar de hartspier voeren"], 0,
       "Boezems en kamers trekken zo na elkaar samen in plaats van tegelijk."),
    tabel("Gebeurt dit tijdens de kamersystole?", [
        ("de kamers trekken samen", J),
        ("de atrioventriculaire kleppen zijn dicht", J),
        ("de halvemaanvormige kleppen zijn dicht", F),
        ("de boezems trekken samen", F),
    ], "Bij de kamersystole gaat het bloed de aorta en longslagader in; de kleppen naar de boezems zijn dicht."),
    keuze("De hartspier krijgt zelf zuurstof via de [[*kransslagaders|longaders|holle aders]].",
          "Die vertrekken vlak boven de aortaklep uit de aorta."),
    sleep("De hartwand bestaat van binnen naar buiten uit het [[endocard]], het [[myocard]] en het [[epicard]].",
          ["pericard"], "Het pericard is het hartzakje rond het hart."),
    sorteer("Hoort dit bij een slagader of bij een ader?", ["Slagader", "Ader"], [
        ["dikke, gespierde en elastische wand", "Slagader"],
        ["kleppen die terugstromen voorkomen", "Ader"],
        ["hoge druk vlak na het hart", "Slagader"],
        ["spieren in de benen helpen het bloed omhoog", "Ader"],
    ], "Slagaders voeren bloed weg van het hart, aders brengen het terug."),
    volgorde("Zet de bloedvaten in de volgorde waarin het bloed ze doorloopt, van het hart naar de weefsels en terug.", [
        "slagader", "arteriool", "haarvat", "venule", "ader",
    ], "In de haarvaten gebeurt de uitwisseling met de weefsels."),
    tabel("Klopt dit over de bloedsomloop?", [
        ("De kleine bloedsomloop loopt van de rechterkamer naar de linkerboezem.", J),
        ("Bij één rondgang passeert het bloed twee keer door het hart.", J),
        ("Een slagader voert altijd zuurstofrijk bloed.", F),
        ("De druk in de aders is hoger dan in de slagaders.", F),
    ], "De longslagader voert zuurstofarm bloed. De druk daalt van slagader naar ader."),
    mk("Waarom loopt het bloed van de darmen eerst door de lever?",
       ["De lever verwerkt eerst de voedingsstoffen",
        "De lever pompt het bloed terug naar de darmen",
        "De lever voegt extra zuurstof toe aan het darmbloed",
        "De lever maakt er rode bloedcellen bij aan"], 0,
       "Via de leverpoortader komt het bloed tussen twee haarvatennetwerken: darm en lever."),
    inv("Het hart pompt per slag 70 ml bloed en klopt 72 keer per minuut. Hoeveel liter is dat per minuut? Rond af op één cijfer na de komma.",
        ["5,0", "5", "5.0", "5,04"], "70 maal 72 is 5040 ml, dus ongeveer 5,0 liter."),
    koppel("Koppel elke klep aan haar plaats.", [
        ["tricuspidalisklep", "tussen rechterboezem en rechterkamer"],
        ["mitralisklep", "tussen linkerboezem en linkerkamer"],
        ["aortaklep", "tussen linkerkamer en aorta"],
        ["pulmonalisklep", "tussen rechterkamer en longslagader"],
    ], ["tussen linkerboezem en longader"], "De atrioventriculaire kleppen liggen tussen boezem en kamer, de halvemaanvormige aan de uitgang van de kamers."),
    keuze("Het basisritme van het hart komt van de [[*sinusknoop|hersenen|AV-knoop]]; het autonoom zenuwstelsel past het enkel aan.",
          "Het hart klopt ook zonder zenuw, maar het zenuwstelsel versnelt of vertraagt."),
    klik("Klik op het bloedvat waarin de druk het hoogst is.", HT.bestand, ZH["E"],
         "De aorta krijgt het bloed rechtstreeks uit de linkerkamer, de sterkste pomp."),
    met_prent(HT.bestand, tabel("Kijk naar de letters in het hart. Klopt dit?", [
        ("G en H zijn atrioventriculaire kleppen.", J),
        ("E is een ader, want het bloed gaat naar het lichaam.", F),
        ("C pompt het bloed door de kleine bloedsomloop.", J),
    ], "E is de aorta, een slagader: ze voert bloed weg van het hart.")),
    tabel("Klopt dit over de ligging en bouw van het hart?", [
        ("Het hart ligt in de borstholte, iets naar links.", J),
        ("De punt van het hart heet de apex.", J),
        ("Het hartzakje bevat wat vocht zodat het hart vlot beweegt.", J),
        ("De boezems hebben een dikkere wand dan de kamers.", F),
    ], "De boezems duwen het bloed maar naar de kamers eronder; daarvoor volstaat een dunne wand."),
    sorteer("Komt dit bloedvat toe in het hart of vertrekt het uit het hart?", ["Komt toe", "Vertrekt"], [
        ["bovenste holle ader", "Komt toe"],
        ["longslagader", "Vertrekt"],
        ["longader", "Komt toe"],
        ["aorta", "Vertrekt"],
    ], "Aders komen toe, slagaders vertrekken."),
    keuze("In de haarvaten is de wand [[*één cellaag|drie lagen|enkele millimeter]] dik, zodat stoffen vlot uitwisselen.",
          "Een dunne wand maakt diffusie tussen bloed en weefsel snel."),
    tabel("Wat helpt het bloed in de beenaders terug naar het hart?", [
        ("kleppen in de aders", J),
        ("samentrekkende beenspieren rond de aders", J),
        ("de hoge druk in de haarvaten", F),
    ], "De druk is in de aders laag. Spieren knijpen de aders samen en kleppen houden het bloed op weg naar boven."),
    mk("Iemand heeft een lekkende mitralisklep. Wat gebeurt er bij elke kamersystole?",
       ["Wat bloed stroomt terug naar de linkerboezem",
        "Wat bloed stroomt terug van de longslagader naar de rechterkamer",
        "De sinusknoop slaat een of twee prikkels per minuut over",
        "De kransslagaders lopen vol met bloed uit de holle aders"], 0,
       "Een gesloten mitralisklep belet terugstromen tijdens de samentrekking van de linkerkamer."),
    open_("Leg uit waarom de linkerkamer een veel dikkere wand heeft dan de rechterkamer.",
          "De linkerkamer pompt het bloed door de grote bloedsomloop, door het hele lichaam. Daarvoor is een veel hogere druk nodig dan voor de korte weg naar de longen. Een dikkere spierwand levert die kracht."),
]

VRAGEN = EIGEN

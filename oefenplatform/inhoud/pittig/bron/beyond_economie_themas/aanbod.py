"""Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("aanbod-bewegen-verschuiven", 0, 24, 0, 14, 2, 2)
PUNTEN = {"A": (8, 6), "B": (12, 8), "C": (14, 6), "D": (4, 4)}

GRAFIEKEN = [
    dict(naam=G, titel="Aanbod van tomaten: A1 en A2",
         krommen=[(lambda q: 2 + 0.5 * q, "groen", "A1", (0, 22)), (lambda q: -1 + 0.5 * q, "blauw", "A2", (2, 24))],
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         labelplek={"A1": (21, 12.5), "A2": (23.2, 10.6)},
         xlabel="hoeveelheid", ylabel="prijs", ijk_x=4, ijk_y=2),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over bewegen op en verschuiven van de aanbodcurve")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "De markt staat in punt A. De tuinbouwers schakelen over op een nieuwe, goedkopere productietechniek. De prijs blijft even 6. Klik op het nieuwe punt.",
        P, [punt_zone(G, *PUNTEN["C"])],
        "Een goedkopere techniek verschuift de aanbodcurve naar rechts: van A1 naar A2. Bij een prijs van 6 wordt nu 14 aangeboden in plaats van 8.",
    ),
    klik(
        "De markt staat in punt A. De marktprijs van tomaten stijgt naar 8, en verder verandert er niets. Klik op het nieuwe punt.",
        P, [punt_zone(G, *PUNTEN["B"])],
        "Verandert de prijs van het goed zelf, dan beweeg je op dezelfde aanbodcurve A1, naar een grotere aangeboden hoeveelheid.",
    ),
    met_prent(P, mk(
        "De markt staat in punt C. Welke gebeurtenis brengt haar terug naar punt A?",
        ["De prijs van grondstoffen zoals meststof stijgt sterk",
         "De marktprijs van tomaten daalt van 6 naar 4 euro",
         "Er komen veel nieuwe tuinbouwers op de markt bij",
         "De overheid geeft een subsidie per kilo tomaten"],
        0,
        "Van C naar A verschuift de curve naar links bij dezelfde prijs. Duurdere grondstoffen doen dat. Nieuwe tuinbouwers en een subsidie verschuiven ze naar rechts.",
    )),
    met_prent(P, inv(
        "Bereken de prijselasticiteit van het aanbod op A1 van A (prijs 6, hoeveelheid 8) naar B (prijs 8, hoeveelheid 12), met A als vertrekpunt. Schrijf het getal met een komma.",
        "1,5",
        "Hoeveelheid: +4 / 8 = +50 %. Prijs: +2 / 6 = +33,3 %. Ea = 50 / 33,3 = 1,5.",
    )),
    met_prent(P, mk(
        "Van D naar A op A1: is het aanbod daar elastisch of inelastisch, met D als vertrekpunt?",
        ["Elastisch: Ea = 2", "Inelastisch: Ea = 0,5", "Unitair elastisch: Ea = 1", "Perfect elastisch: Ea is oneindig"],
        0,
        "Hoeveelheid van 4 naar 8: +100 %. Prijs van 4 naar 6: +50 %. Ea = 100 / 50 = 2.",
    )),
    tabel(
        "Verschuift de aanbodcurve van appels naar rechts of naar links?",
        [
            ("Een strenge vorst vernielt een deel van de oogst", "Naar links"),
            ("De overheid voert een belasting per kilo in", "Naar links"),
            ("Er komen meer fruitkwekers bij", "Naar rechts"),
            ("Een uitzonderlijk goede oogst", "Naar rechts"),
            ("Enkele fruitkwekers stoppen ermee", "Naar links"),
        ],
        "Meer producenten, een goede oogst, een nieuwe techniek of een subsidie: naar rechts. Het omgekeerde: naar links.",
        kolommen=["Naar rechts", "Naar links"],
    ),
    mk(
        "Waaruit leid je bij volkomen concurrentie de individuele aanbodcurve van een producent af?",
        ["Uit het stijgende deel van de marginale kostencurve, boven het minimum van de GVK",
         "Uit het dalende deel van de gemiddelde totale kostencurve van die producent",
         "Uit de optimale goederencombinatie van één consument bij verschillende prijzen",
         "Uit de som van de vaste kosten en de variabele kosten bij elke hoeveelheid"],
        0,
        "Elk punt op dat stijgende stuk van de MK-curve is de optimale productiegrootte bij die prijs.",
    ),
    mk(
        "De marktprijs zakt onder het minimum van de gemiddelde variabele kosten van een producent. Wat doet hij op korte termijn?",
        ["Hij biedt niets aan", "Hij biedt evenveel aan als voorheen", "Hij verhoogt zijn productie om de vaste kosten te dekken", "Hij verhoogt zijn prijs boven de marktprijs"],
        0,
        "Onder het minimum van de GVK dekt de prijs zelfs de variabele kosten niet. Dan stopt hij beter tijdelijk.",
    ),
    casus(
        "Drie bakkers verkopen broden. Bij 3 euro bieden ze 40, 50 en 30 broden aan. Bij 3,60 euro bieden ze 48, 62 en 34 broden aan.",
        [
            inv("Hoe groot is het collectieve aanbod bij 3,60 euro? Schrijf enkel het getal.", "144",
                "48 + 62 + 34 = 144 broden."),
            mk("Hoe groot is de prijselasticiteit van het collectieve aanbod van 3 naar 3,60 euro, met 3 euro als vertrekpunt?",
               ["1", "0,5", "2", "1,2"], 0,
               "Hoeveelheid van 120 naar 144: +20 %. Prijs van 3 naar 3,60: +20 %. Ea = 20 / 20 = 1."),
            mk("Hoe heet een aanbod met die elasticiteit?",
               ["Unitair elastisch", "Perfect elastisch", "Inelastisch", "Perfect inelastisch"], 0,
               "Ea = 1 is unitair elastisch."),
        ],
    ),
    inv(
        "De prijselasticiteit van het aanbod is 0,4 en de prijs stijgt met 15 %. Met hoeveel procent stijgt de aangeboden hoeveelheid? Schrijf enkel het getal.",
        "6",
        "0,4 · 15 = 6 %.",
    ),
    tabel(
        "Welke curve hoort bij welke elasticiteit van het aanbod?",
        [
            ("Ea = 0", "Verticaal"),
            ("Ea is oneindig", "Horizontaal"),
            ("Ea = 3", "Vlak stijgend"),
            ("Ea = 0,2", "Steil stijgend"),
        ],
        "Hoe vlakker de aanbodcurve bij dezelfde schaal, hoe elastischer het aanbod.",
        kolommen=["Verticaal", "Horizontaal", "Vlak stijgend", "Steil stijgend"],
    ),
    mk(
        "Welk voorbeeld past het best bij een perfect inelastisch aanbod?",
        ["De zitplaatsen in een uitverkocht stadion op de dag van de match",
         "Broden van een bakker die nog veel vrije capaciteit in zijn oven heeft",
         "T-shirts van een fabriek die een grote voorraad in haar magazijn heeft",
         "Smartphonehoesjes van een producent die snel een extra ploeg kan inzetten"],
        0,
        "Er kunnen geen zitplaatsen bij, wat de prijs ook is. Voorraad en vrije capaciteit maken het aanbod juist elastisch.",
    ),
    sorteer(
        "Maakt dit het aanbod elastischer of minder elastisch?",
        ["Elastischer", "Minder elastisch"],
        [
            ["De producent heeft een grote voorraad", "Elastischer"],
            ["Er is veel vrije productiecapaciteit", "Elastischer"],
            ["Je kijkt naar de lange termijn: een nieuwe fabriek bouwen kan", "Elastischer"],
            ["Je kijkt naar de korte termijn en de fabriek draait op volle toeren", "Minder elastisch"],
            ["De producent heeft geen voorraad en geen vrije capaciteit", "Minder elastisch"],
        ],
        "Voorraad, vrije capaciteit en tijd om aan te passen maken het aanbod elastischer.",
    ),
    tabel(
        "De vraag naar een goed stijgt. Wat gebeurt er met de prijs en de hoeveelheid?",
        [
            ("Perfect elastisch aanbod", "Enkel de hoeveelheid stijgt"),
            ("Perfect inelastisch aanbod", "Enkel de prijs stijgt"),
            ("Gewoon stijgend aanbod", "Prijs en hoeveelheid stijgen allebei"),
        ],
        "Hoe inelastischer het aanbod, hoe meer de vraagstijging in een hogere prijs terechtkomt.",
        kolommen=["Enkel de prijs stijgt", "Enkel de hoeveelheid stijgt", "Prijs en hoeveelheid stijgen allebei"],
    ),
    keuze(
        "Hoe [[*inelastischer|elastischer]] het aanbod, hoe sterker de prijs stijgt als de vraag stijgt.",
        "Kan het aanbod niet volgen, dan vangt de prijs de hogere vraag op.",
    ),
    inv(
        "Het inkomen stijgt met 4 % en de vraag naar restaurantbezoeken stijgt met 10 %. Hoe groot is de inkomenselasticiteit? Schrijf het getal met een komma.",
        "2,5",
        "Ey = 10 / 4 = 2,5.",
    ),
    tabel(
        "Welk soort goed hoort bij deze inkomenselasticiteit?",
        [
            ("Ey = −0,3", "Inferieur goed"),
            ("Ey = 0", "Indifferent goed"),
            ("Ey = 0,8", "Noodzakelijk goed"),
            ("Ey = 1,7", "Luxegoed"),
        ],
        "Negatief: inferieur. 0: indifferent. Tussen 0 en 1: noodzakelijk. Groter dan 1: luxe.",
        kolommen=["Inferieur goed", "Indifferent goed", "Noodzakelijk goed", "Luxegoed"],
    ),
    mk(
        "Het inkomen van een gezin stijgt met 10 % en het gezin neemt 3 % minder de bus. Wat zijn busritten voor dit gezin?",
        ["Een inferieur goed met een inkomenselasticiteit van −0,3",
         "Een noodzakelijk goed met een inkomenselasticiteit van 0,3",
         "Een luxegoed met een inkomenselasticiteit van −3",
         "Een indifferent goed, want ze blijven de bus nemen"],
        0,
        "Ey = −3 / 10 = −0,3. Een negatieve inkomenselasticiteit wijst op een inferieur goed.",
    ),
    mk(
        "Een leerling zegt: 'Een inferieur goed is een goed van slechte kwaliteit dat niemand wil.' Wat klopt?",
        ["Fout: het is een goed dat je minder koopt als je meer verdient, omdat je dan iets anders kiest",
         "Juist: daarom heeft een inferieur goed altijd een inkomenselasticiteit van precies nul, wat het inkomen ook doet",
         "Fout: het is een goed dat je meer koopt als je inkomen stijgt, zoals een verre reis",
         "Juist: de vraag naar een inferieur goed is daarom altijd perfect inelastisch, ook als de prijs sterk daalt"],
        0,
        "Inferieur zegt iets over hoe de vraag op het inkomen reageert, niet over de kwaliteit.",
    ),
    tabel(
        "Waar of niet waar over de inkomenselasticiteit?",
        [
            ("Noodzakelijke goederen en luxegoederen zijn allebei normale goederen.", J),
            ("Een goed met een inkomenselasticiteit van 0,8 is een luxegoed.", F),
            ("Een goed kan voor de ene consument normaal zijn en voor een andere inferieur.", J),
            ("Bij een indifferent goed daalt de vraag sterk als het inkomen stijgt.", F),
        ],
        "0,8 ligt tussen 0 en 1: noodzakelijk. Bij een indifferent goed verandert de vraag niet.",
    ),
    inv(
        "De inkomenselasticiteit van brood is 0,2 en het inkomen stijgt met 15 %. Met hoeveel procent stijgt de vraag naar brood? Schrijf enkel het getal.",
        "3",
        "0,2 · 15 = 3 %.",
    ),
    koppel(
        "Koppel elk voorbeeld aan het soort goed.",
        [
            ["Een verre vakantie", "Luxegoed"],
            ["Elektriciteit", "Noodzakelijk goed"],
            ["Zout", "Indifferent goed"],
        ],
        ["Complementair goed"],
        "Luxe: Ey groter dan 1. Noodzakelijk: tussen 0 en 1. Indifferent: 0.",
    ),
    sleep(
        "De prijselasticiteit van het aanbod is meestal [[positief]], omdat prijs en aangeboden hoeveelheid in [[dezelfde]] richting bewegen.",
        ["negatief", "tegengestelde", "nul"],
        "Bij een hogere prijs wil men meer aanbieden.",
    ),
    mk(
        "Stijgt de marktprijs van tomaten, wat gebeurt er dan met de aanbodcurve van tomaten?",
        ["Niets: je beweegt op de curve naar een grotere aangeboden hoeveelheid",
         "De hele aanbodcurve verschuift naar rechts, want tuinbouwers willen meer verkopen",
         "De hele aanbodcurve verschuift naar links, want tomaten worden duurder voor de kopers",
         "De aanbodcurve wordt verticaal, want de oogst van dit jaar ligt al vast"],
        0,
        "Een verandering van de eigen prijs geeft een beweging op de curve, geen verschuiving.",
    ),
    volgorde(
        "Zet deze aanbodsituaties van minst naar meest elastisch.",
        ["Ea = 0", "Ea = 0,6", "Ea = 1", "Ea = 2,5"],
        "Hoe groter Ea, hoe sterker de aangeboden hoeveelheid op de prijs reageert.",
    ),
    open_(
        "De vraag naar mondmaskers stijgt plots heel sterk. Leg uit waarom de prijs op korte termijn sterk stijgt, en waarom die stijging op lange termijn kleiner wordt.",
        "Op korte termijn kunnen producenten weinig extra maken: het aanbod is inelastisch, dus de hogere vraag geeft vooral een hogere prijs. Op lange termijn kunnen ze extra machines of fabrieken bijzetten en komen er producenten bij: het aanbod wordt elastischer, dus de hoeveelheid stijgt meer en de prijs minder.",
    ),
    mk(
        "Bij volkomen concurrentie: wat stelt elk punt op de individuele aanbodcurve van een producent voor?",
        ["De optimale productiegrootte bij die prijs", "De hoeveelheid waarbij de gemiddelde kosten het laagst zijn",
         "De hoeveelheid die de consumenten bij die prijs vragen", "De hoeveelheid waarbij de vaste kosten gedekt zijn"],
        0,
        "Bij elke prijs kiest de producent de hoeveelheid waar prijs gelijk is aan marginale kosten: zijn optimale productiegrootte.",
    ),
    keuze(
        "Bij dezelfde schaal wijst een [[*vlakkere|steilere]] aanbodcurve op een [[*elastischer|minder elastisch]] aanbod.",
        "Bij een vlakke curve reageert de aangeboden hoeveelheid sterk op een kleine prijsverandering.",
    ),
]

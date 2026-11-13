"""Een opgave aanpakken: van context naar wiskunde — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

GRAFIEKEN = []
PRENTEN = []

VRAGEN = [
    volgorde(
        r"Een tuin van \(12\) m op \(8\) m krijgt binnen de rand een pad van \(1\) m breed rondom. Je zoekt hoeveel m² gras er overblijft. Zet de stappen in een goede volgorde.",
        [
            "een schets maken en het pad erop aanduiden",
            r"de maten van het grasveld bepalen: \(10\) m op \(6\) m",
            r"de oppervlakte berekenen: \(60\) m²",
            "nagaan of het gras kleiner is dan de hele tuin",
        ],
        "Begrijpen (schets), plannen (welke maten), uitvoeren (rekenen) en reflecteren (klopt de grootteorde).",
    ),
    koppel(
        "Koppel elke aanpak aan de heuristiek die je gebruikt.",
        [
            [r"Je noemt de prijs van een schrift \(x\).", "variabelen invoeren"],
            ["Je lost eerst het geval met 2 tafels op, dan met 3, en zoekt de regel.", "een eenvoudiger geval bekijken"],
            ["Je start bij de eindprijs en rekent stap voor stap terug.", "achterwaarts werken"],
            [r"Je probeert \(10\), dat is te veel, dan \(8\), dat klopt.", "slim gissen en controleren"],
        ],
        ["een tegenvoorbeeld zoeken"],
        "Elke heuristiek is een manier om een opgave die je niet meteen ziet, toch aan te pakken.",
    ),
    mk(
        r"Na een prijsstijging van \(25\%\) kost een fietsslot \(75\) euro. Wat kostte het slot vóór de stijging?",
        [r"\(56{,}25\) euro", r"\(60\) euro", r"\(50\) euro", r"\(93{,}75\) euro"],
        1,
        r"\(75\) euro is \(125\%\) van de oude prijs: \(75 : 1{,}25 = 60\). Wie \(25\%\) van \(75\) aftrekt, neemt het percentage van de verkeerde prijs.",
    ),
    inv(
        r"Ik denk aan een getal. Ik vermenigvuldig het met \(3\), trek er \(7\) van af en deel de uitkomst door \(2\). Ik krijg \(10\). Aan welk getal dacht ik?",
        ["9"],
        r"Achterwaarts werken: \(10 \cdot 2 = 20\), \(20 + 7 = 27\), \(27 : 3 = 9\).",
    ),
    casus(
        r"Een school huurt een bus voor een uitstap. Firma A vraagt \(250\) euro vast plus \(1{,}80\) euro per kilometer. Firma B vraagt \(2{,}80\) euro per kilometer en geen vast bedrag.",
        [
            mk(
                r"Welke formule geeft de prijs \(p\) bij firma A voor \(k\) kilometer?",
                [r"\(p = 250k + 1{,}80\)", r"\(p = 251{,}80 \cdot k\)", r"\(p = 250 + 1{,}80k\)", r"\(p = (250 + 1{,}80) \cdot k\)"],
                2,
                r"Het vaste bedrag betaal je één keer, het bedrag per kilometer \(k\) keer.",
            ),
            inv(
                "Bij hoeveel kilometer kosten beide firma's evenveel?",
                ["250", "250 km", "250 kilometer"],
                r"\(250 + 1{,}80k = 2{,}80k\) geeft \(250 = k\).",
            ),
            tabel(
                "Juist of fout?",
                [
                    (r"Voor een rit van \(100\) km is firma B goedkoper.", J),
                    (r"Voor een rit van \(300\) km is firma B goedkoper.", F),
                    (r"Voor \(300\) km scheelt het \(50\) euro.", J),
                    ("Hoe langer de rit, hoe kleiner het verschil tussen beide firma's.", F),
                ],
                r"Bij \(100\) km: A \(430\) euro, B \(280\) euro. Bij \(300\) km: A \(790\) euro, B \(840\) euro. Voorbij \(250\) km groeit het verschil elke kilometer met \(1\) euro.",
            ),
        ],
    ),
    keuze(
        r"Een rechthoek heeft een omtrek van \(30\) cm en is twee keer zo lang als breed. Noem de breedte \(x\). Dan geldt [[*\(2x + 4x = 30\)|\(x + 2x = 30\)|\(x \cdot 2x = 30\)]], dus de breedte is [[*\(5\) cm|\(10\) cm|\(7{,}5\) cm]] en de oppervlakte is [[*\(50\) cm²|\(30\) cm²|\(15\) cm²]].",
        r"De omtrek telt twee breedtes en twee lengtes: \(2x + 2 \cdot 2x = 6x = 30\). Breedte \(5\), lengte \(10\), oppervlakte \(50\).",
    ),
    casus(
        r"Aan één tafel passen \(4\) stoelen. Schuif je tafels in een rij tegen elkaar, dan passen er bij \(2\) tafels \(6\) stoelen en bij \(3\) tafels \(8\).",
        [
            mk(
                r"Hoeveel stoelen passen er bij \(n\) tafels in zo'n rij?",
                [r"\(4n\)", r"\(2n + 2\)", r"\(4n - 2\)", r"\(n + 3\)"],
                1,
                r"Elke tafel geeft \(2\) stoelen aan de lange kanten, en aan beide uiteinden komt er nog \(1\) bij: \(2n + 2\). Controle: \(n = 3\) geeft \(8\).",
            ),
            inv(
                r"Hoeveel tafels heb je minstens nodig voor \(31\) gasten?",
                ["15", "15 tafels"],
                r"\(2n + 2 \geq 31\) geeft \(n \geq 14{,}5\). Een halve tafel bestaat niet, dus \(15\) tafels.",
            ),
        ],
    ),
    inv(
        r"\(130\) leerlingen gaan mee op uitstap. Een bus heeft \(50\) plaatsen. Hoeveel bussen moet de school bestellen?",
        ["3", "3 bussen"],
        r"\(130 : 50 = 2{,}6\). Demathematiseren: je kan geen \(0{,}6\) bus bestellen, en met \(2\) bussen blijven er \(30\) leerlingen thuis.",
    ),
    mk(
        r"Een leerling berekent de oppervlakte van een klaslokaal van \(8\) m op \(8\) m en vindt \(6400\). Wat ging er waarschijnlijk mis?",
        [
            "ze rekende in decimeter en vergat om te zetten naar m²",
            r"ze nam de omtrek in plaats van de oppervlakte",
            r"ze vermenigvuldigde met \(100\) in plaats van \(10\)",
            "ze rekende in centimeter en zette juist om naar m²",
        ],
        0,
        r"\(80\) dm maal \(80\) dm is \(6400\) dm², en dat is \(64\) m². Een lokaal van \(6400\) m² is zo groot als een voetbalveld: reflecteren had dat getoond.",
    ),
    tabel(
        "Kan deze uitkomst kloppen?",
        [
            ("Een leerling van 15 jaar weegt 520 kg.", "Kan niet kloppen"),
            ("Een fietser rijdt gemiddeld 18 km/u.", "Kan kloppen"),
            ("Een klas van 24 leerlingen heeft gemiddeld 1,4 broers of zussen per leerling.", "Kan kloppen"),
            ("De oppervlakte van een tafel is −2 m².", "Kan niet kloppen"),
            ("Een tank van 50 liter is na het tanken voor 112 % vol.", "Kan niet kloppen"),
        ],
        "Reflecteren betekent ook: past de uitkomst bij de situatie? Een gemiddelde mag een kommagetal zijn, een oppervlakte nooit negatief.",
        kolommen=["Kan kloppen", "Kan niet kloppen"],
    ),
    inv(
        r"Een vloer van \(4{,}2\) m op \(3\) m wordt betegeld met vierkante tegels van \(30\) cm. Hoeveel tegels zijn er nodig, als je niets hoeft te zagen?",
        ["140", "140 tegels"],
        r"Eerst dezelfde eenheid: \(420 : 30 = 14\) en \(300 : 30 = 10\), dus \(14 \cdot 10 = 140\) tegels.",
    ),
    mk(
        r"Welke waarde van \(n\) is een tegenvoorbeeld voor de bewering: '\(n^{2} + n + 41\) is voor elk natuurlijk getal \(n\) een priemgetal'?",
        [r"\(n = 1\)", r"\(n = 10\)", r"\(n = 40\)", r"\(n = 20\)"],
        2,
        r"\(40^{2} + 40 + 41 = 1681 = 41 \cdot 41\). De andere geven \(43\), \(151\) en \(461\): dat zijn priemgetallen, en die bewijzen niets.",
    ),
    sorteer(
        r"Iemand beweert: 'Als je twee getallen optelt, is de som altijd groter dan elk van de twee getallen.' Wat toont elk voorbeeld?",
        ["Toont aan dat de bewering vals is", "Toont niets aan"],
        [
            [r"\(3 + 5 = 8\)", "Toont niets aan"],
            [r"\(-2 + 6 = 4\)", "Toont aan dat de bewering vals is"],
            [r"\(0 + 7 = 7\)", "Toont aan dat de bewering vals is"],
            [r"\(10 + 20 = 30\)", "Toont niets aan"],
            [r"\(0{,}5 + 0{,}5 = 1\)", "Toont niets aan"],
        ],
        r"Eén tegenvoorbeeld volstaat om een bewering vals te maken: bij \(-2 + 6\) is de som niet groter dan \(6\), bij \(0 + 7\) niet groter dan \(7\). Voorbeelden die kloppen, bewijzen niets.",
    ),
    mk(
        r"Het product van twee opeenvolgende even getallen is \(168\). Welke getallen zijn het?",
        [r"\(12\) en \(14\)", r"\(8\) en \(21\)", r"\(13\) en \(14\)", r"\(10\) en \(12\)"],
        0,
        r"Slim gissen: \(\sqrt{168} \approx 13\), dus probeer de even getallen rond \(13\): \(12 \cdot 14 = 168\). \(8\) en \(21\) geven ook \(168\), maar zijn niet opeenvolgend en niet allebei even.",
    ),
    inv(
        r"Hoeveel is \(1 + 2 + 3 + \ldots + 40\)? Tip: zet de getallen in paren.",
        ["820"],
        r"\(1 + 40\), \(2 + 39\), ... geeft \(20\) paren van \(41\): \(20 \cdot 41 = 820\).",
    ),
    casus(
        r"Een gezin van vier gaat drie nachten kamperen. De camping rekent \(18\) euro per nacht voor de tent en \(4{,}50\) euro per persoon per nacht. Ze rijden er \(240\) km heen en evenveel terug. De auto verbruikt \(6\) liter per \(100\) km en de brandstof kost \(1{,}75\) euro per liter.",
        [
            inv(
                "Hoeveel kost de camping in totaal, in euro?",
                ["108", "108 euro"],
                r"Per nacht \(18 + 4 \cdot 4{,}50 = 36\) euro, voor drie nachten \(108\) euro.",
            ),
            mk(
                "Hoeveel kost de brandstof voor heen en terug?",
                [r"\(25{,}20\) euro", r"\(14{,}40\) euro", r"\(50{,}40\) euro", r"\(28{,}80\) euro"],
                2,
                r"\(480\) km aan \(6\) liter per \(100\) km is \(28{,}8\) liter, maal \(1{,}75\) euro is \(50{,}40\) euro. \(25{,}20\) euro is enkel de heenreis.",
            ),
            sleep(
                "Je splitste de vraag 'wat kost het weekend?' in camping en brandstof. Die heuristiek heet [[opsplitsen in deelproblemen]]. Je zette de gegevens om in berekeningen: dat is [[mathematiseren]].",
                ["achterwaarts werken", "demathematiseren"],
                "Een grote vraag in kleinere stukken knippen maakt ze aanpakbaar. De berekening opstellen is mathematiseren.",
            ),
        ],
    ),
    tabel(
        "Juist of fout over het oplossen van een opgave?",
        [
            ("Een goede schatting vervangt de exacte berekening.", F),
            ("Een schets is een volwaardige stap in de oplossing.", J),
            ("Twee voorbeelden die kloppen, bewijzen dat een eigenschap altijd geldt.", F),
            ("Bij reflecteren ga je ook na of je aanpak bij een andere opgave bruikbaar is.", J),
        ],
        "Een schatting toont de grootteorde, geen exacte uitkomst. Voorbeelden kunnen een vermoeden geven, geen bewijs.",
    ),
    mk(
        r"De rij \(3, 7, 11, 15, \ldots\) gaat zo verder. Welk getal staat op de \(50\)ste plaats?",
        [r"\(199\)", r"\(200\)", r"\(203\)", r"\(196\)"],
        0,
        r"Elke keer komt er \(4\) bij. Op plaats \(n\) staat \(3 + 4(n - 1)\), dus \(3 + 4 \cdot 49 = 199\). Wie \(50 \cdot 4\) neemt, telt één sprong te veel.",
    ),
    mk(
        r"Een rechthoekig stuk karton van \(30\) cm op \(20\) cm. Je knipt uit elke hoek een vierkant van \(5\) cm en plooit de randen omhoog tot een open doos. Wat is de inhoud van de doos?",
        [r"\(3000\) cm³", r"\(1000\) cm³", r"\(1500\) cm³", r"\(2000\) cm³"],
        1,
        r"De bodem wordt \(20\) cm op \(10\) cm, want aan elke kant gaat er \(5\) cm af. De hoogte is \(5\) cm: \(20 \cdot 10 \cdot 5 = 1000\) cm³. Wie \(30 \cdot 20 \cdot 5\) neemt, vergeet dat de randen omhoog geplooid zijn.",
    ),
    open_(
        r"Een leerling lost op: '\(130\) leerlingen, bussen van \(50\) plaatsen' en schrijft als antwoord '\(2{,}6\) bussen'. Leg in twee zinnen uit wat er mis is en wat het juiste antwoord is.",
        r"De berekening \(130 : 50 = 2{,}6\) klopt, maar de leerling vergat te demathematiseren: een deel van een bus kan je niet bestellen. Met \(2\) bussen blijven \(30\) leerlingen over, dus de school bestelt \(3\) bussen.",
    ),
    casus(
        r"Een trein vertrekt om 9.40 u en komt om 11.15 u aan. Hij rijdt gemiddeld \(84\) km/u.",
        [
            mk(
                "Je zoekt hoe ver de trein rijdt. Welke fout maken veel leerlingen?",
                [
                    r"ze nemen \(1{,}35\) uur in plaats van \(1\) uur en \(35\) minuten",
                    r"ze delen \(84\) door de reistijd",
                    r"ze tellen de wachttijd in het station mee",
                    r"ze rekenen met \(84\) m/s in plaats van km/u",
                ],
                0,
                r"\(1\) uur \(35\) minuten is \(1\tfrac{35}{60}\) uur, en dat is meer dan \(1{,}35\) uur.",
            ),
            inv(
                "Hoeveel km rijdt de trein?",
                ["133", "133 km"],
                r"\(95\) minuten is \(\tfrac{95}{60}\) uur: \(84 \cdot \tfrac{95}{60} = 133\) km.",
            ),
        ],
    ),
    koppel(
        "Koppel elke stap van het oplossen aan wat je doet bij de opgave 'Hoeveel verf heb je nodig voor een muur van 4,2 m op 2,6 m, als 1 liter 8 m² dekt?'",
        [
            ["begrijpen", "nagaan dat je liter verf zoekt en welke maten gegeven zijn"],
            ["plannen", "beslissen: eerst oppervlakte, dan delen door 8"],
            ["uitvoeren", r"\(4{,}2 \cdot 2{,}6 = 10{,}92\) en \(10{,}92 : 8 \approx 1{,}37\)"],
            ["reflecteren", "besluiten dat je een pot van 1,5 liter of meer koopt"],
        ],
        [],
        "De vier stappen volgen elkaar op, en reflecteren zet de uitkomst terug in de situatie.",
    ),
    mk(
        r"Een vierkant heeft een omtrek van \(36\) cm. Je verdubbelt elke zijde. Wat gebeurt er met de oppervlakte?",
        [r"ze wordt \(2\) keer zo groot", r"ze wordt \(4\) keer zo groot", r"ze wordt \(8\) keer zo groot", r"ze wordt \(36\) cm² groter"],
        1,
        r"Van \(9 \cdot 9 = 81\) cm² naar \(18 \cdot 18 = 324\) cm²: dat is \(4\) keer zo veel, want beide zijden verdubbelen.",
    ),
    inv(
        r"Een recept voor \(6\) personen vraagt \(450\) g bloem en \(3\) eieren. Je hebt nog maar \(4\) eieren en kookt voor zo veel mogelijk personen. Hoeveel gram bloem gebruik je dan?",
        ["600", "600 g", "600 gram"],
        r"De eieren beperken: \(1\) ei per \(2\) personen, dus \(4\) eieren voor \(8\) personen. Bloem per persoon \(450 : 6 = 75\) g, voor \(8\) personen \(600\) g.",
    ),
]

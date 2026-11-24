"""België na 1945: breuklijnen, federale staat en emancipatie — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="volksraadpleging-1950.svg", zelf=True,
         wat="Staafdiagram met het percentage ja-stemmen bij de volksraadpleging van 1950 (Beyond doorstroom).",
         vragen="tabel en klikvraag over de koningskwestie"),
]

VRAGEN = [
    # --- breuklijnen
    sorteer(
        "Bij welke breuklijn hoort elk conflict?",
        ["Gelovig - vrijzinnig", "Arbeid - kapitaal", "Communautair"],
        [
            ["de schoolstrijd", "Gelovig - vrijzinnig"],
            ["het Schoolpact van 1958", "Gelovig - vrijzinnig"],
            ["het sociaal pact van 1944", "Arbeid - kapitaal"],
            ["de taalgrens van 1962-1963", "Communautair"],
            ["Leuven Vlaams in 1968", "Communautair"],
            ["de staking in Herstal voor hoger loon", "Arbeid - kapitaal"],
        ],
        "Drie breuklijnen lopen door de Belgische politiek. Rond elke strekking groeiden eigen zuilen.",
    ),
    mk(
        "Welk verband is er tussen de breuklijnen en de verzuiling?",
        [
            "Rond elke strekking groeiden eigen organisaties",
            "De verzuiling schafte de breuklijnen in 1945 af",
            "De breuklijnen ontstonden pas na de ontzuiling",
            "Er is geen verband: de zuilen gingen enkel over sport",
        ],
        0,
        "Eigen scholen, ziekenfondsen, vakbonden en verenigingen per strekking.",
    ),
    # --- koningskwestie
    met_prent("volksraadpleging-1950.svg", tabel(
        "Bekijk de uitslag van de volksraadpleging van 1950 over de terugkeer van Leopold III. Welke uitspraken kun je staven?",
        [
            ("In het hele land stemde een meerderheid ja.", J),
            ("In Wallonië stemde een meerderheid ja.", F),
            ("Het verschil tussen Vlaanderen en Wallonië was groot.", J),
        ],
        "Een meerderheid in het land, maar een groot verschil tussen de landsdelen.",
    )),
    klik(
        "Klik in de grafiek op het landsdeel waar de meerderheid neen stemde.",
        "volksraadpleging-1950.svg",
        [[71.2, 12, 17.5, 84]],
        "Wallonië, onder de stippellijn van 50 %.",
    ),
    mk(
        "Waarom deed Leopold III toch troonsafstand, ondanks een ja in het hele land?",
        [
            "Er volgde zware onrust",
            "Hij was in 1950 al gestorven in het buitenland",
            "De grondwet verbood elke volksraadpleging",
            "De Verenigde Naties verplichtten hem ertoe",
        ],
        0,
        "Na zware onrust deed hij in 1951 troonsafstand ten gunste van Boudewijn.",
    ),
    tabel(
        "Welke uitspraken over de koningskwestie kloppen?",
        [
            ("Ze ging over de houding van Leopold III tijdens de bezetting.", J),
            ("Er was een volksraadpleging.", J),
            ("Boudewijn volgde zijn vader op in 1951.", J),
            ("Leopold III bleef koning tot zijn dood.", F),
        ],
        "De breuk tussen koning en regering in 1940 groeide uit tot de koningskwestie.",
    ),
    # --- schoolstrijd, taal
    casus(
        "Een katholieke school in 1955 klaagt: \"De regering wil ons minder geld geven.\" Een officiële school antwoordt: \"Overheidsgeld hoort bij het officiële onderwijs.\" In 1958 tekenen de partijen een akkoord.",
        [
            mk(
                "Waarover ging deze schoolstrijd?",
                [
                    "Over het geld voor het katholieke onderwijs",
                    "Over de taal waarin les gegeven werd",
                    "Over de vraag of meisjes naar school mochten",
                    "Over de afschaffing van alle scholen",
                ],
                0,
                "Het ging om de financiering, niet om de taal.",
            ),
            tabel(
                "Wat regelde het Schoolpact van 1958?",
                [
                    ("Vrij en officieel onderwijs worden allebei door de overheid betaald.", J),
                    ("Ouders kiezen vrij hun school.", J),
                    ("Alle katholieke scholen worden gesloten.", F),
                ],
                "Een compromis tussen de zuilen, typisch voor België.",
            ),
        ],
    ),
    tabel(
        "Welke uitspraken over de communautaire breuklijn kloppen?",
        [
            ("In 1962-1963 werd de taalgrens vastgelegd.", J),
            ("Over Voeren en de Brusselse rand is nog lang getwist.", J),
            ("Het Franstalige deel van de Leuvense universiteit verhuisde naar Louvain-la-Neuve.", J),
            ("De taalgrens werd al in 1831 vastgelegd.", F),
        ],
        "De taalwetten bepaalden ook per gebied de taal van bestuur en onderwijs.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["Het sociaal pact", "De troonsafstand van Leopold III", "Het Schoolpact", "De taalgrens", "Leuven Vlaams", "België een federale staat in de grondwet"],
        "1944, 1951, 1958, 1962-1963, 1968 en 1993.",
    ),
    # --- federale staat
    sorteer(
        "Gemeenschap, gewest of federaal?",
        ["Gemeenschap", "Gewest", "Federaal"],
        [
            ["onderwijs", "Gemeenschap"],
            ["cultuur", "Gemeenschap"],
            ["economie van een gebied", "Gewest"],
            ["leefmilieu", "Gewest"],
            ["defensie", "Federaal"],
            ["justitie", "Federaal"],
        ],
        "Gemeenschappen gaan over taal, cultuur en onderwijs, gewesten over grondgebied en economie. Defensie, justitie en buitenlands beleid bleven federaal.",
    ),
    keuze(
        "België telt [[*drie|twee|vier]] gemeenschappen en [[*drie|twee|zes]] gewesten.",
        "Drie van elk: twee soorten deelstaten.",
    ),
    mk(
        "Waarom heeft Brussel een bijzondere plaats in de federale staat?",
        [
            "Er zijn twee gemeenschappen bevoegd",
            "Het hoort bij geen enkele gemeenschap en geen enkel gewest",
            "Het is de enige stad die eentalig Nederlands is",
            "Het is een aparte staat buiten België",
        ],
        0,
        "Brussel is een eigen, tweetalig gewest: zowel de Vlaamse als de Franse Gemeenschap zijn er bevoegd.",
    ),
    tabel(
        "Welke uitspraken over de staatshervormingen kloppen?",
        [
            ("Er waren vier hervormingen tussen 1970 en 1993.", J),
            ("Daarna volgden er nog twee.", J),
            ("De communautaire breuklijn dreef ze vooruit.", J),
            ("Elke hervorming maakte voorgoed een einde aan de spanningen.", F),
        ],
        "Elke hervorming was een antwoord op een spanning, zelden het einde ervan.",
    ),
    mk(
        "Waarom gaat de munt in België niet meer over de federale staat, en ook niet over de deelstaten?",
        [
            "De munt is Europees geworden",
            "België heeft geen munt meer nodig",
            "De gewesten hebben elk hun eigen munt",
            "Brussel drukt alle munten van Europa",
        ],
        0,
        "Met de euro ging die bevoegdheid naar het Europese niveau.",
    ),
    # --- welvaart en werk
    tabel(
        "Wat werd in het sociaal pact van 1944 afgesproken?",
        [
            ("Een stelsel van sociale zekerheid", J),
            ("Overleg tussen werkgevers en vakbonden", J),
            ("Pensioen, kinderbijslag, ziekte en werkloosheid", J),
            ("De afschaffing van de vakbonden", F),
        ],
        "De basis van de welvaartsstaat, met overleg tussen arbeid en kapitaal.",
    ),
    mk(
        "Expo 58 in Brussel liet het Atomium na. Welk gevoel van die tijd drukt ze uit?",
        [
            "Geloof in vooruitgang",
            "De angst voor een nieuwe crisis",
            "Het einde van de Belgische industrie",
            "De dekolonisatie van Congo",
        ],
        0,
        "Het Atomium is er nog van over.",
    ),
    tabel(
        "Een gezin in 1965 kijkt terug op 1945. Wat is er veranderd?",
        [
            ("Auto, koelkast en televisie raakten verspreid.", J),
            ("Betaalde vakantie en een kortere werkweek gaven meer vrije tijd.", J),
            ("De werkloosheid steeg sterk.", F),
        ],
        "Een sterke groei van welvaart en verbruik. De grote werkloosheid kwam pas met de crisis van de jaren zeventig.",
    ),
    mk(
        "Hoe veranderde de crisis van de jaren zeventig de economische kaart van België?",
        [
            "Het zwaartepunt verschoof naar Vlaanderen",
            "Wallonië werd het rijkste gewest van Europa",
            "Alle mijnen in Limburg openden opnieuw",
            "De werkloosheid verdween volledig",
        ],
        0,
        "De zware industrie in Wallonië ging achteruit. De mijnen sloten, de laatste in Zolder in 1992.",
    ),
    tabel(
        "Welke uitspraken over de steenkoolmijnen kloppen?",
        [
            ("Ze sloten één na één.", J),
            ("De Waalse mijnen sloten eerst.", J),
            ("Zolder sloot als laatste in 1992.", J),
            ("De Limburgse mijnen sloten al voor de Waalse.", F),
        ],
        "Eerst Wallonië, later Limburg, met een zware omschakeling als gevolg.",
    ),
    # --- emancipatie
    volgorde(
        "Zet de stappen in de emancipatie in de juiste volgorde.",
        ["Vrouwen stemmen voor het parlement", "De staking in Herstal", "Abortus onder voorwaarden uit het strafrecht", "Huwelijk voor koppels van hetzelfde geslacht", "Adoptie voor koppels van hetzelfde geslacht"],
        "1948, 1966, 1990, 2003 en 2006.",
    ),
    casus(
        "Februari 1966. In de wapenfabriek van Herstal leggen drieduizend vrouwen het werk neer. Hun slogan: gelijk loon voor gelijk werk. De staking duurt drie maanden.",
        [
            mk(
                "Bij welke breuklijn of beweging hoort deze staking het best?",
                [
                    "Arbeid en kapitaal, en emancipatie",
                    "Bij de communautaire breuklijn",
                    "Bij de schoolstrijd",
                    "Bij de koningskwestie",
                ],
                0,
                "Het ging om loon (arbeid tegenover kapitaal) en om gelijkheid tussen vrouwen en mannen.",
            ),
            tabel(
                "Welke uitspraken over de positie van vrouwen kloppen?",
                [
                    ("Vrouwen stemden pas in 1948 voor het parlement.", J),
                    ("Tot in de jaren zeventig had de man wettelijk het laatste woord in het huwelijk.", J),
                    ("Vrouwen hadden al voor 1914 stemrecht voor het parlement.", F),
                ],
                "Dertig jaar na de mannen kregen vrouwen stemrecht. Gelijkheid in het huwelijk kwam nog later.",
            ),
        ],
    ),
    tabel(
        "Een leerling zegt: \"De emancipatiewetten dateren allemaal uit de negentiende eeuw.\" Welke gegevens spreken dat tegen?",
        [
            ("Abortus werd in 1990 onder voorwaarden uit het strafrecht gehaald.", J),
            ("Koppels van hetzelfde geslacht mogen sinds 2003 huwen.", J),
            ("Vrouwen stemden pas in 1948.", J),
            ("De grondwet van 1831 gaf grondrechten.", F),
        ],
        "De meeste emancipatiewetten komen van na 1960, en soms van na 2000.",
    ),
    mk(
        "België stelde in 2003 het huwelijk open voor koppels van hetzelfde geslacht. Wat is daar bijzonder aan?",
        [
            "België was het tweede land ter wereld",
            "België was het laatste land van Europa",
            "Het gebeurde al in de negentiende eeuw",
            "Het werd door de EU opgelegd",
        ],
        0,
        "Adoptie volgde in 2006.",
    ),
    tabel(
        "Wat betekent ontzuiling?",
        [
            ("De greep van de zuilen nam af.", J),
            ("Men kiest zijn ziekenfonds minder vanzelf binnen één strekking.", J),
            ("Alle zuilen werden bij wet verboden.", F),
        ],
        "Mensen kozen hun school, ziekenkas en vereniging minder vanzelf binnen één strekking.",
    ),
    mk(
        "Wat kenmerkte mei 1968?",
        [
            "Jongeren betwistten het gezag",
            "Jongeren eisten de terugkeer van Leopold III",
            "Jongeren vroegen meer macht voor de zuilen",
            "Jongeren steunden de mijnsluitingen",
        ],
        0,
        "Jongeren betwistten het gezag van school en kerk, en ook dat van hun ouders.",
    ),
    sleep(
        "Vergelijk je een gezin van 1950 met een gezin van 2020, dan werken veel meer [[vrouwen]] buitenshuis en zijn de [[gezinsvormen]] veelzijdiger geworden. Dat hoort bij de [[emancipatie]].",
        ["mannen", "zuilen", "verzuiling"],
        "Werk, huwelijk en gezin veranderden sterk na 1945.",
    ),
    open_(
        "Leg uit hoe België van een unitaire naar een federale staat evolueerde, en waarom.",
        "De communautaire breuklijn tussen Nederlandstaligen en Franstaligen zorgde voor spanningen, zoals over de taalgrens en Leuven Vlaams. Als antwoord kwamen vier staatshervormingen tussen 1970 en 1993, en daarna nog twee. Bevoegdheden zoals onderwijs, cultuur, leefmilieu en economie gingen naar drie gemeenschappen en drie gewesten. Sinds 1993 staat in de grondwet dat België een federale staat is.",
    ),
    open_(
        "Welke breuklijn weegt vandaag nog het zwaarst in de Belgische politiek? Leg uit.",
        "De communautaire breuklijn weegt nog het zwaarst: ze dreef de staatshervormingen en blijft een strijdpunt. De godsdienstige breuklijn weegt minder, onder meer door de ontzuiling en het Schoolpact. Daarnaast kwamen er nieuwe strijdpunten bij.",
    ),
]

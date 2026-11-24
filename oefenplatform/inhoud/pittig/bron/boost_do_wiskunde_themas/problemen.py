"""Een opgave aanpakken: van context naar wiskunde — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus

GRAFIEKEN = []
PRENTEN = []

VRAGEN = [
    volgorde(
        "Zet de vier stappen van het procedureel oplossen in de juiste volgorde.",
        ["Begrijp het probleem", "Maak een plan", "Voer het plan uit", "Reflecteer"],
        "Eerst weten wat gegeven en gevraagd is, dan een aanpak kiezen, dan rekenen, en tot slot nagaan of de uitkomst kan kloppen.",
    ),
    sorteer(
        "Bij welke stap van het oplossen hoort deze handeling?",
        ["Begrijp het probleem", "Maak een plan", "Voer het plan uit", "Reflecteer"],
        [
            ("Je onderstreept wat gegeven is en omcirkelt wat gevraagd wordt.", "Begrijp het probleem"),
            ("Je beslist om eerst de oppervlakte te berekenen en dan pas de kostprijs.", "Maak een plan"),
            (r"Je lost \(3x + 12 = 45\) op.", "Voer het plan uit"),
            ("Je vult je uitkomst opnieuw in de opgave in om te zien of ze klopt.", "Reflecteer"),
            ("Je vraagt je af of een snelheid van 300 km/u voor een fietser wel kan.", "Reflecteer"),
        ],
        "Begrijpen gaat over de opgave lezen, plannen over de aanpak kiezen, uitvoeren over rekenen, reflecteren over controleren.",
    ),
    koppel(
        "Verbind elke opgave met de heuristiek die het best past.",
        [
            ("Hoeveel handdrukken geven 5 mensen als iedereen iedereen één keer de hand geeft?", "Alle mogelijkheden opschrijven"),
            ("Twee getallen hebben als som 50 en als verschil 14. Welke getallen?", "Variabelen invoeren"),
            ("Een tegelvloer heeft links en rechts hetzelfde patroon.", "Gebruik maken van symmetrie"),
            ("Na drie keer verdubbelen heb je 96. Waarmee begon je?", "Terugrekenen"),
        ],
        ["Een tegenvoorbeeld zoeken"],
        "Elke heuristiek is een manier om een opgave die je niet meteen ziet, toch aan te pakken.",
    ),
    mk(
        "Na drie keer verdubbelen heb je 96. Hoeveel had je in het begin?",
        ["12", "32", "24", "16"],
        0,
        r"Terugrekenen: \(96 : 2 = 48\), \(48 : 2 = 24\), \(24 : 2 = 12\).",
    ),
    inv(
        "Vijf mensen geven elkaar elk één keer de hand. Hoeveel handdrukken zijn dat in totaal?",
        ["10", "tien"],
        r"Schrijf alle paren op: de eerste geeft er \(4\), de tweede nog \(3\) nieuwe, dan \(2\) en \(1\). Samen \(4 + 3 + 2 + 1 = 10\).",
    ),
    casus(
        r"Lien wil haar kamer schilderen. Eén muur is \(3{,}6\) m breed en \(2{,}5\) m hoog. In die muur zit een raam van \(1{,}2\) m op \(1{,}5\) m. Eén liter verf is genoeg voor \(8\) m\(^{2}\). Ze schildert de muur twee keer.",
        [
            mk("Hoeveel vierkante meter muur moet ze schilderen voor één laag?",
               [r"\(9\) m\(^{2}\)", r"\(7{,}2\) m\(^{2}\)", r"\(10{,}8\) m\(^{2}\)", r"\(1{,}8\) m\(^{2}\)"], 1,
               r"\(3{,}6 \cdot 2{,}5 = 9\) m\(^{2}\), min het raam \(1{,}2 \cdot 1{,}5 = 1{,}8\) m\(^{2}\), geeft \(7{,}2\) m\(^{2}\)."),
            mk("Hoeveel liter verf heeft ze nodig voor twee lagen?",
               [r"\(0{,}9\) liter", r"\(2{,}25\) liter", r"\(1{,}8\) liter", r"\(3{,}6\) liter"], 2,
               r"Twee lagen is \(14{,}4\) m\(^{2}\). \(14{,}4 : 8 = 1{,}8\) liter."),
            mk("Verf wordt verkocht in potten van 1 liter. Wat antwoordt Lien op de vraag hoeveel potten ze koopt?",
               ["1 pot, want 1,8 rond je af naar 2 en dat is te veel", "2 potten", "1,8 potten", "3 potten, voor de zekerheid"], 1,
               r"Dat is demathematiseren: \(1{,}8\) liter betekent in de winkel \(2\) potten, want een halve pot bestaat niet."),
        ],
    ),
    tabel(
        "Klopt deze uitspraak over het oplossen van problemen?",
        [
            ("Reflecteren kan je doen terwijl je rekent, niet enkel op het einde.", J),
            ("Een schets is pas nuttig als ze op schaal getekend is.", F),
            ("Eén tegenvoorbeeld volstaat om een algemene uitspraak te weerleggen.", J),
            ("Als drie voorbeelden kloppen, is een eigenschap bewezen.", F),
            ("Bij een probleem combineer je soms leerstof uit verschillende hoofdstukken.", J),
            ("Wie schat, hoeft niet meer exact te rekenen.", F),
        ],
        "Een schets hoeft niet op schaal te zijn, voorbeelden bewijzen niets, een schatting vervangt de berekening niet maar controleert ze.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Iemand beweert: 'Als je twee priemgetallen optelt, krijg je altijd een even getal.' Welk voorbeeld weerlegt dat?",
        [r"\(3 + 5 = 8\)", r"\(2 + 3 = 5\)", r"\(7 + 11 = 18\)", r"\(5 + 13 = 18\)"],
        1,
        r"\(2\) is een priemgetal en \(2 + 3 = 5\) is oneven. Eén tegenvoorbeeld is genoeg; de andere voorbeelden kloppen wel en bewijzen dus niets.",
    ),
    mk(
        r"Een leerling berekent dat een klaslokaal een vloer heeft van \(5400\) m\(^{2}\). Wat zegt reflecteren hier?",
        [
            "Dat klopt, een klas is groot",
            r"Die uitkomst is veel te groot, wellicht werden centimeters en meters door elkaar gehaald",
            r"Het antwoord moet in kubieke meter staan",
            "Reflecteren hoeft niet als de berekening klopt",
        ],
        1,
        r"Een klas is eerder \(50\) à \(60\) m\(^{2}\). Een uitkomst die zo ver van een schatting ligt, wijst op een fout met de eenheden.",
    ),
    inv(
        r"Een fietser rijdt \(18\) km in \(45\) minuten. Wat is zijn gemiddelde snelheid in km/u?",
        ["24", "24 km/u"],
        r"\(45\) minuten is \(0{,}75\) uur. \(18 : 0{,}75 = 24\) km/u. Controle: in een uur rijdt hij iets meer dan \(18\) km, dat klopt.",
    ),
    keuze(
        "Een situatie omzetten in een formule heet [[*mathematiseren|demathematiseren]]. Je uitkomst terugvertalen naar de situatie heet [[*demathematiseren|mathematiseren]].",
        "Mathematiseren is de heenweg naar de wiskunde, demathematiseren de terugweg naar de situatie.",
    ),
    mk(
        "Twee getallen hebben als som 50 en als verschil 14. Wat is het grootste getal?",
        ["36", "32", "18", "28"],
        1,
        r"Noem het kleinste \(x\): \(x + (x + 14) = 50\), dus \(2x = 36\) en \(x = 18\). Het grootste is \(32\). Controle: \(32 - 18 = 14\).",
    ),
    sorteer(
        "Is dit een vraagstuk of een probleem?",
        ["Vraagstuk", "Probleem"],
        [
            ("Een opgave waarvoor je enkel de stelling van Pythagoras nodig hebt.", "Vraagstuk"),
            ("Een opgave waarin je een vergelijking opstelt en daarna een oppervlakte met een gelijkvormigheid berekent.", "Probleem"),
            ("Een tekstopgave over procenten uit het hoofdstuk procenten.", "Vraagstuk"),
            ("Een opgave over een dak waarbij je goniometrie, oppervlakte en kosten combineert.", "Probleem"),
        ],
        "Een vraagstuk vraagt leerstof van één hoofdstuk, een probleem combineert hoofdstukken.",
    ),
    mk(
        r"Een rij gaat zo: \(1, 4, 9, 16, 25, \ldots\) Hoe ontdek je het patroon het snelst?",
        [
            "Door de getallen op te tellen tot je een mooi getal krijgt",
            "Door te zien dat het de kwadraten van 1, 2, 3, 4, 5 zijn",
            "Door het gemiddelde van de rij te berekenen",
            "Door het eerste getal door het laatste te delen",
        ],
        1,
        r"Een patroon ontdekken: \(1^{2}, 2^{2}, 3^{2}, 4^{2}, 5^{2}\). Het volgende getal is \(36\).",
    ),
    inv(
        r"Welk getal volgt in de rij \(3, 7, 15, 31, \ldots\)?",
        ["63"],
        r"Elk getal is het vorige maal \(2\) plus \(1\): \(31 \cdot 2 + 1 = 63\). Ook: de verschillen \(4, 8, 16\) verdubbelen, dus het volgende verschil is \(32\).",
    ),
    tabel(
        "Welke heuristiek gebruik je hier?",
        [
            ("Je tekent een ladder tegen een muur als een rechthoekige driehoek.", "Een schets maken"),
            ("Je noemt de prijs van één ticket \\(p\\).", "Variabelen invoeren"),
            ("Je deelt 'hoeveel kost een schoolreis' op in bus, inkom en eten.", "Opsplitsen in deelproblemen"),
            ("Je probeert 5, dan 7, dan 6 tot de som klopt.", "Slim gissen en controleren"),
        ],
        "Elke heuristiek helpt je om op gang te komen als je de oplossing niet meteen ziet.",
        kolommen=["Een schets maken", "Variabelen invoeren", "Opsplitsen in deelproblemen", "Slim gissen en controleren"],
    ),
    mk(
        r"Schat zonder rekentoestel: \(49 \cdot 21\) ligt het dichtst bij",
        [r"\(100\)", r"\(1000\)", r"\(10\,000\)", r"\(500\)"],
        1,
        r"\(50 \cdot 20 = 1000\). De exacte uitkomst \(1029\) ligt daar vlakbij. Zo'n schatting toont of je rekentoestel de juiste grootteorde geeft.",
    ),
    mk(
        r"Je berekent de hoogte van een boom en vindt \(-7{,}5\) m. Wat besluit je?",
        ["De boom is 7,5 m hoog, het minteken mag je weglaten",
         "Er ging iets mis in de berekening, want een hoogte kan niet negatief zijn",
         "De boom staat onder de grond",
         "Je rondt af naar 8 m en gaat verder"],
        1,
        "Reflecteren: een negatieve lengte kan niet. Zoek de fout in je berekening, en laat het minteken niet zomaar vallen.",
    ),
    sleep(
        "Bij een opgave met [[context]] vertaal je eerst de situatie in wiskundetaal. Na het rekenen [[controleer]] je of de uitkomst past bij de situatie, en je [[verantwoordt]] je tussenstappen zodat een lezer je redenering kan volgen.",
        ["gok", "vergeet"],
        "Context, controleren en verantwoorden horen bij elke goede oplossing.",
    ),
    inv(
        "Op een feest geeft iedereen iedereen één keer de hand. Er zijn 15 handdrukken. Hoeveel mensen zijn er?",
        ["6", "zes"],
        r"Bij \(n\) mensen zijn er \(1 + 2 + \ldots + (n-1)\) handdrukken. \(1 + 2 + 3 + 4 + 5 = 15\), dus \(6\) mensen.",
    ),
    mk(
        "Waarom schrijf je bij een meetkundig probleem de eigenschap die je gebruikt bij elke stap?",
        ["Omdat het antwoord anders fout is",
         "Zodat een lezer kan volgen waarom elke stap klopt",
         "Omdat je dan minder hoeft te rekenen",
         "Omdat een tekening dan overbodig wordt"],
        1,
        "Verantwoorden maakt je redenering controleerbaar, voor jezelf en voor wie je oplossing leest.",
    ),
    keuze(
        "Een zuiver wiskundige opgave noem je een opgave [[*zonder context|met context]]. Een opgave over een fietstocht is een opgave [[*met context|zonder context]].",
        "Met context: er zit een situatie uit de wereld in. Zonder context: abstract, zuiver wiskundig.",
    ),
    mk(
        r"Een tegel is \(30\) cm op \(30\) cm. Hoeveel tegels heb je minstens nodig voor een vloer van \(2{,}4\) m op \(1{,}5\) m?",
        [r"\(40\)", r"\(36\)", r"\(48\)", r"\(400\)"],
        0,
        r"In de lengte \(240 : 30 = 8\) tegels, in de breedte \(150 : 30 = 5\) tegels: \(8 \cdot 5 = 40\). Eerst alles in dezelfde eenheid zetten.",
    ),
    tabel(
        "Is dit een goede controle van de uitkomst?",
        [
            ("Je vult de gevonden x opnieuw in de vergelijking in.", J),
            ("Je kijkt of de eenheid van je uitkomst past bij wat gevraagd is.", J),
            ("Je rekent precies dezelfde stappen nog eens in dezelfde volgorde.", F),
            ("Je vergelijkt de uitkomst met een snelle schatting.", J),
        ],
        "Wie dezelfde stappen herhaalt, maakt vaak dezelfde fout opnieuw. Invullen, eenheden nakijken en schatten zijn echte controles.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Een getal wordt eerst met \(5\) vermenigvuldigd en daarna verminderd met \(7\). De uitkomst is \(38\). Welk getal was het?",
        ["9"],
        r"Terugrekenen: \(38 + 7 = 45\) en \(45 : 5 = 9\). Controle: \(9 \cdot 5 - 7 = 38\).",
    ),
    casus(
        r"Een sportclub huurt een bus voor \(480\) euro. De kosten worden gelijk verdeeld. Als er \(8\) leden minder meegaan, betaalt ieder \(2\) euro meer. Je zoekt hoeveel leden er eerst zouden meegaan.",
        [
            mk("Welke heuristiek ligt hier het meest voor de hand?",
               ["Slim gissen en controleren met een paar mogelijke aantallen",
                "Een tegenvoorbeeld zoeken voor de bewering van de club",
                "Gebruik maken van symmetrie in de verdeling",
                "Het antwoord achteraan in het boek opzoeken"], 0,
               "Je probeert een aantal en kijkt of beide prijzen kloppen. Een vergelijking opstellen kan ook, maar die wordt tweedegraads."),
            mk(r"Je probeert eerst \(40\) leden. Wat leer je daaruit?",
               [r"Het klopt: \(12\) euro en \(14\) euro",
                r"Het verschil is \(3\) euro, te groot, dus je moet meer leden proberen",
                r"Het verschil is \(1\) euro, te klein, dus je moet minder leden proberen",
                r"Met \(40\) leden kan je \(480\) niet eerlijk verdelen"], 1,
               r"\(480 : 40 = 12\) en \(480 : 32 = 15\): \(3\) euro verschil. Hoe meer leden, hoe kleiner het verschil, dus probeer een groter aantal."),
            inv("Hoeveel leden zouden er eerst meegaan?",
                ["48", "48 leden"],
                r"Bij \(48\) leden betaalt ieder \(10\) euro, bij \(40\) leden \(12\) euro: precies \(2\) euro meer."),
        ],
    ),
]

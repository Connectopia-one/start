"""Het ontstaan van België — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="europa-1815.webp", zelf=False,
         wat="Kaart van Europa na het Congres van Wenen (1815), met letters A, B en C.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="kaartvraag over het Verenigd Koninkrijk der Nederlanden"),
    dict(bestand="septemberdagen-1830.webp", zelf=False,
         wat="Gustaf Wappers, 'Episode uit de Septemberdagen 1830' (1834-1835), publiek domein.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over het schilderij als bron"),
]

VRAGEN = [
    # --- grieven
    sorteer(
        "Wie had last van welke maatregel van Willem I?",
        ["De katholieken", "De liberalen", "De Franstalige burgerij"],
        [
            ["de koning bemoeit zich met de benoeming van bisschoppen", "De katholieken"],
            ["priesters moeten naar een rijksschool", "De katholieken"],
            ["journalisten worden vervolgd", "De liberalen"],
            ["ministers moeten zich niet verantwoorden voor het parlement", "De liberalen"],
            ["het Nederlands wordt de taal van bestuur en rechtspraak", "De Franstalige burgerij"],
        ],
        "Godsdienst raakte de katholieken, pers en ministers de liberalen, en het taalbesluit van 1823 de Franstalige burgerij.",
    ),
    sorteer(
        "In welk domein situeer je elke grief van het Zuiden?",
        ["Politiek", "Economisch", "Cultureel"],
        [
            ["meer inwoners, maar niet meer zetels", "Politiek"],
            ["één tarief voor handelaars en fabrikanten", "Economisch"],
            ["het taalbesluit van 1823", "Cultureel"],
            ["de opleiding van priesters", "Cultureel"],
            ["ministers zonder controle van het parlement", "Politiek"],
        ],
        "Zetels en ministers zijn politiek, invoerrechten economisch, taal en godsdienst cultureel.",
    ),
    mk(
        "Waarom kon één tarief voor invoerrechten het Noorden en het Zuiden nooit allebei tevreden stellen?",
        [
            "Handelaars wilden lage rechten, fabrikanten hoge",
            "Het Noorden had geen havens en het Zuiden had geen enkele fabriek",
            "Willem I liet het tarief elk jaar door de bisschoppen vastleggen",
            "Het Zuiden betaalde in een andere munt dan het Noorden",
        ],
        0,
        "Het Noorden leefde van handel en wilde vrije invoer. Het Zuiden leefde van industrie en wilde bescherming tegen goedkope buitenlandse waren.",
    ),
    tabel(
        "Welke uitspraken over het taalbesluit van 1823 kloppen?",
        [
            ("Het maakte het Nederlands de taal van bestuur en rechtspraak in Vlaanderen en Brabant.", J),
            ("De Franstalige burgerij zag haar positie bedreigd.", J),
            ("Het werd in heel het Zuiden met vreugde onthaald.", F),
            ("De bestuurstaal stond vaak ver van het dialect dat de mensen spraken.", J),
        ],
        "Ook wie geen Frans sprak, herkende zich niet altijd in die bestuurstaal. Zo kreeg Willem I zelfs met een taalmaatregel weinig steun.",
    ),
    mk(
        "Tijdgenoten noemden het unionisme van 1828 een monsterverbond. Waarom?",
        [
            "Het bracht twee groepen samen die normaal tegenstanders waren",
            "Het was een verbond van alle legers van Europa tegen het kleine België",
            "Het verbond had zoveel leden dat het de grootste partij ter wereld werd",
            "Het was een geheim verbond van Willem I met de koning van Frankrijk",
        ],
        0,
        "Katholieken en liberalen verschilden sterk van mening. Alleen de gemeenschappelijke tegenstander bracht hen samen.",
    ),
    # --- revolutie
    volgorde(
        "Zet de gebeurtenissen van 1830 en 1831 in de juiste volgorde.",
        ["Rellen na een opera in de Muntschouwburg", "Gevechten in het Warandepark", "Het Voorlopig Bewind roept de onafhankelijkheid uit", "Het Nationaal Congres komt samen", "Leopold I legt de eed af"],
        "Augustus, september, 4 oktober en november 1830, en dan 21 juli 1831.",
    ),
    koppel(
        "Is dit een oorzaak of de aanleiding van de revolutie van 1830?",
        [
            ["de rellen na de opera in augustus 1830", "Aanleiding"],
            ["de grieven over godsdienst, pers en taal", "Oorzaak op lange termijn"],
            ["honger en duur brood na mislukte oogsten", "Oorzaak op korte termijn"],
        ],
        ["Gevolg"],
        "De opera was de vonk. De grieven stapelden zich jarenlang op, de honger maakte de onvrede net in 1830 groter.",
    ),
    mk(
        "Welke rol speelde de julirevolutie in Parijs voor de Belgische opstandelingen?",
        [
            "Ze bewees dat een vorst wél kon vallen",
            "Ze bracht een Frans leger dat Brussel in augustus veroverde",
            "Ze zorgde ervoor dat Willem I meteen zelfbestuur gaf",
            "Ze maakte van Leopold I de nieuwe koning der Fransen",
        ],
        0,
        "Wat in Parijs lukte, leek ook in Brussel mogelijk. Zo kreeg de opstand de wind in de zeilen.",
    ),
    tabel(
        "Wie maakte de revolutie van 1830?",
        [
            ("Op straat vochten vooral gewone mensen en arbeiders.", J),
            ("Het Voorlopig Bewind bestond uit mensen van de burgerij.", J),
            ("Het Nationaal Congres was een zaak van de burgerij.", J),
            ("Na de revolutie kregen de arbeiders stemrecht.", F),
        ],
        "De straat was van de arbeiders, het bestuur van de burgerij. Door het cijnskiesrecht hadden de arbeiders na 1830 nog altijd niets te zeggen.",
    ),
    mk(
        "Een historicus schrijft: \"De aarzeling van Willem I kostte hem het Zuiden.\" Wat bedoelt hij?",
        [
            "Willem I wachtte te lang en stuurde dan toch zijn leger",
            "Willem I gaf meteen toe aan alle eisen van de opstandelingen",
            "Willem I liet zijn leger nooit naar Brussel gaan",
            "Willem I was in 1830 al gestorven en had geen opvolger",
        ],
        0,
        "Hij gaf geen zelfbestuur en stuurde na een tijd troepen. Na de gevechten in september was de breuk onherstelbaar.",
    ),
    casus(
        "Bekijk het schilderij. Gustaf Wappers maakte het in 1834 en 1835 in opdracht van de Belgische staat. Het toont burgers, arbeiders en een vrouw met de Belgische vlag op de barricaden in Brussel, in september 1830.",
        [
            met_prent("septemberdagen-1830.webp", mk(
                "Wat wilde de opdrachtgever wellicht met dit schilderij?",
                [
                    "Een heldhaftig verhaal over het ontstaan van België",
                    "Een neutraal en volledig verslag van de gevechten in Brussel",
                    "Willem I bedanken voor zijn bestuur van het Zuiden",
                    "Tonen dat vooral boeren van het platteland gevochten hebben",
                ],
                0,
                "De jonge staat bestelde het werk. Licht, vlag en vastberaden gezichten maken van de opstand een heldendaad.",
            ), volgt=True),
            tabel(
                "Mag je op basis van dit schilderij deze besluiten trekken?",
                [
                    ("De Belgische staat wilde 1830 als een heldendaad herinneren.", "Mag"),
                    ("Iedere inwoner van het Zuiden steunde de opstand.", "Mag niet"),
                    ("Het schilderij toont precies hoe de gevechten verliepen.", "Mag niet"),
                ],
                "Het schilderij zegt veel over hoe België gezien wilde worden, en veel minder over wat er echt gebeurde.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- grondwet
    mk(
        "Waarom koos het Nationaal Congres niet voor een republiek?",
        [
            "Een republiek leek te veel op Frankrijk",
            "Het Congres wilde dat Willem I opnieuw koning zou worden van Noord en Zuid",
            "Een republiek was in de grondwet van Wenen verboden",
            "Er was geen enkele Belg die de eed op een grondwet wilde afleggen",
        ],
        0,
        "De grootmachten vreesden alles wat naar de Franse Revolutie rook, en België had hun erkenning nodig.",
    ),
    tabel(
        "Wat stond er in de grondwet van 1831?",
        [
            ("De macht van de koning werd begrensd.", J),
            ("Vrijheid van onderwijs en van godsdienst", J),
            ("Een recht op een uitkering bij ziekte", F),
            ("Regels over het loon in de fabrieken", F),
            ("Ministers die zich verantwoorden voor het parlement", J),
        ],
        "Politieke grondrechten wel, sociale rechten niet. Daarom noemt men de grondwet liberaal.",
    ),
    keuze(
        "De grondwet van 1831 was voor haar tijd [[*liberaal|absolutistisch|socialistisch]], maar België was nog geen democratie: door het [[*cijnskiesrecht|algemeen stemrecht|meervoudig stemrecht]] mocht ongeveer één op de [[*honderd|tien|twee]] inwoners stemmen.",
        "Grondrechten en een begrensde koning, maar enkel wie genoeg belasting betaalde, mocht stemmen.",
    ),
    mk(
        "Waarom kwam de vrijheid van onderwijs zowel de katholieken als de liberalen gelegen?",
        [
            "Elke groep kon zijn eigen scholen oprichten",
            "Ze schafte alle scholen in het land af en spaarde zo veel geld uit",
            "Ze legde vast dat enkel de koning scholen mocht openen",
            "Ze verplichtte alle kinderen om Nederlands te leren op school",
        ],
        0,
        "Onder Willem I mocht dat niet zomaar. Nu konden katholieken en liberalen elk hun eigen onderwijs inrichten.",
    ),
    open_(
        "Toon met twee argumenten dat de grondwet van 1831 modern was, en met één argument dat België toen nog geen democratie was.",
        "Modern: de macht van de koning werd door de grondwet begrensd, de ministers moesten zich verantwoorden voor het parlement, en er stonden grondrechten in zoals vrijheid van pers, vereniging, godsdienst en onderwijs. Geen democratie: door het cijnskiesrecht mocht maar ongeveer één op de honderd inwoners stemmen.",
    ),
    tabel(
        "Welke uitspraken over de taal in het nieuwe België kloppen?",
        [
            ("De grondwet liet het gebruik van de talen vrij.", J),
            ("In de praktijk werd het Frans de taal van het bestuur.", J),
            ("De grondwet maakte het Nederlands de enige officiële taal.", F),
        ],
        "Vrij op papier, maar in de praktijk Frans. Dat werd later een bron van spanning.",
    ),
    # --- erkenning
    mk(
        "Het Nationaal Congres koos een vorst uit het buitenland. Wat wilde het daarmee bereiken?",
        [
            "Om de nieuwe staat erkend te krijgen",
            "Omdat de grondwet een Belgische koning verbood",
            "Omdat Willem I zijn zoon als koning had aangeduid",
            "Omdat er in België geen adel meer was na de revolutie",
        ],
        0,
        "Een vorst met banden met de grote vorstenhuizen maakte het voor de mogendheden makkelijker om België te aanvaarden.",
    ),
    sleep(
        "Op [[21 juli 1831]] legde Leopold I de eed af. Kort daarna viel Willem I België binnen met de [[Tiendaagse Veldtocht]]. Hij erkende de onafhankelijkheid pas in [[1839]].",
        ["4 oktober 1830", "1815", "Conferentie van Wenen"],
        "21 juli is nog altijd de nationale feestdag. Na de Tiendaagse Veldtocht duurde het tot 1839 voor Willem I België erkende.",
    ),
    tabel(
        "Wat regelden de mogendheden op de Conferentie van Londen?",
        [
            ("De erkenning van België", J),
            ("De grenzen van België", J),
            ("De neutraliteit van België", J),
            ("Het algemeen stemrecht in België", F),
        ],
        "In Londen beslisten de grootmachten over erkenning, grenzen en neutraliteit. Het stemrecht was een Belgische zaak.",
    ),
    mk(
        "De mogendheden waarborgden de Belgische neutraliteit. Waarom schrijft men: \"In 1914 bleek wat zo'n waarborg waard was\"?",
        [
            "Een buurland viel België toch binnen",
            "België koos zelf partij en verklaarde de oorlog aan Frankrijk",
            "De grootmachten betaalden België een grote som geld",
            "Willem I erkende België pas in 1914",
        ],
        0,
        "Een belofte op papier hield een grootmacht niet tegen. In 1914 werd België toch in een oorlog meegesleurd.",
    ),
    tabel(
        "Wat gebeurde er bij het verdrag van 1839?",
        [
            ("Willem I erkende de onafhankelijkheid van België.", J),
            ("Limburg en Luxemburg werden gesplitst.", J),
            ("België verloor een deel van Limburg en Luxemburg.", J),
            ("België werd terug bij Nederland gevoegd.", F),
        ],
        "Acht jaar na de eed van Leopold I kwam de erkenning, maar België verloor een deel van Limburg en Luxemburg.",
    ),
    inv(
        "Hoeveel jaar zat er tussen de eedaflegging van Leopold I en de erkenning door Willem I?",
        ["8", "acht", "8 jaar", "acht jaar"],
        "Van 1831 tot 1839: acht jaar.",
    ),
    klik(
        "Bekijk de kaart van Europa in 1815. Klik op de staat waaruit België zich in 1830 losmaakte.",
        "europa-1815.webp",
        [[29.5, 33, 8, 20]],
        "Gebied A: het Verenigd Koninkrijk der Nederlanden, dat Wenen in 1815 als buffer tegen Frankrijk had opgericht.",
    ),
    # --- na 1830
    mk(
        "Waarom hield het unionisme na 1830 geen halve eeuw stand?",
        [
            "De tegenstander was weg, de schoolkwestie kwam boven",
            "Willem I verbood de samenwerking in het verdrag van 1839",
            "Leopold I schafte het parlement en de grondwet af in 1835",
            "De katholieken en liberalen werden samen één partij",
        ],
        0,
        "Zodra Willem I weg was, kwamen de verschillen naar boven. Rond het onderwijs ontstonden de eerste partijen.",
    ),
    tabel(
        "Welke ideologieën zie je in 1830 aan het werk?",
        [
            ("Liberalisme, in de eis voor grondrechten en een grondwet", J),
            ("Nationalisme, in het streven naar een eigen staat", J),
            ("Restauratie, in het herstel van de macht van Willem I", F),
        ],
        "Liberalen wilden grondrechten, nationalisten een eigen staat. Het herstel van de oude orde was net wat Wenen wilde.",
    ),
    open_(
        "Leg uit hoe een beslissing van het Congres van Wenen op lange termijn bijdroeg tot het ontstaan van België.",
        "Wenen voegde Noord en Zuid samen tot het Verenigd Koninkrijk der Nederlanden, als buffer tegen Frankrijk, zonder de bevolking iets te vragen. In het Zuiden groeiden grieven over godsdienst, pers, ministers, taal, economie en zetels. Katholieken en liberalen sloten daarom het unionisme, en in 1830 volgde de revolutie.",
    ),
    mk(
        "Welke uitspraak over 1830 is het best onderbouwd?",
        [
            "De straat vocht, de burgerij bestuurde",
            "Het was een opstand van boeren op het platteland tegen de adel",
            "Het was een revolutie die het algemeen stemrecht invoerde",
            "Het was een oorlog die Frankrijk alleen voerde tegen Nederland",
        ],
        0,
        "Arbeiders vochten op straat, maar het bestuur en de grondwet waren werk van de burgerij.",
    ),
    mk(
        "In 1828 en 1830 waren de grieven van het Zuiden dezelfde. Waarom brak de opstand pas in 1830 uit?",
        [
            "Honger en het voorbeeld van Parijs gaven de vonk",
            "Willem I had in 1829 alle grieven al opgelost",
            "Pas in 1830 kwamen er katholieken in het Zuiden wonen",
            "Pas in 1830 gaf het Congres van Wenen de toestemming",
        ],
        0,
        "Oorzaken stapelen zich op, maar een opstand heeft een vonk nodig. Duur brood, werkloosheid en de julirevolutie maakten 1830 het moment.",
    ),
]

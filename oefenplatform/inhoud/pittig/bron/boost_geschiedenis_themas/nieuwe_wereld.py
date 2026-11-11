"""De 'Nieuwe' Wereld en de driehoekshandel — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1400-1800.svg", zelf=True,
         wat="Tijdlijn van 1400 tot 1800, een groot streepje om de honderd jaar, een klein om de tien jaar.",
         vragen="klikvragen op 1492 en 1498"),
    dict(bestand="driehoekshandel.svg", zelf=True,
         wat="Schema van de driehoekshandel: Europa, West-Afrika en Amerika met drie genummerde pijlen.",
         vragen="koppelvraag lading per pijl, klikvraag middenpassage"),
    dict(bestand="pokken-florentijnse-codex.jpg", zelf=False,
         wat="Tekening uit de Florentijnse Codex (16de eeuw, gemaakt door Azteekse tekenaars) van zieke mensen met pokken.",
         waar="Wikimedia Commons, zoek op 'FlorentineCodex BK12 F54 smallpox' (publiek domein).",
         vragen="tabelvraag over de demografische inzinking en het standpunt van de bron"),
    dict(bestand="slavenschip-brookes.jpg", zelf=False,
         wat="De bekende doorsnede van het slavenschip Brookes (1788) met de mensen dicht opeen in het ruim.",
         waar="Wikimedia Commons, zoek op 'Slaveship Brookes' (publiek domein).",
         vragen="tabelvraag over de middenpassage"),
]

TL = "tijdlijn-1400-1800.svg"
DRIEHOEK = "/examenvormen/geschiedenis-boost/driehoekshandel.svg"

VRAGEN = [
    # --- ontdekkingsreizen
    sorteer(
        "Welk soort motief voor de ontdekkingsreizen is dit?",
        ["Economisch", "Godsdienstig", "Politiek"],
        [
            ["een eigen weg naar de specerijen van Azië", "Economisch"],
            ["het christendom verspreiden", "Godsdienstig"],
            ["aanzien voor de eigen vorst", "Politiek"],
            ["nieuw gebied voor de eigen vorst", "Politiek"],
        ],
        "Goud, God en glorie: handel, geloof en de eer en het gebied van de vorst. Bij bijna elke reis lopen ze door elkaar.",
    ),
    mk(
        "Wat was voor de Portugezen het grote voordeel van een eigen zeeweg naar Azië?",
        [
            "Ze hoefden de prijs niet meer te laten bepalen door tussenhandelaars",
            "De zeeweg was korter dan elke weg over land",
            "De paus verbood christenen om over land naar Azië te reizen",
            "Over land konden schepen de specerijen niet vervoeren",
        ],
        0,
        "Specerijen die via vele handen kwamen, waren in Lissabon peperduur. Een eigen zeeweg sloeg de tussenhandelaars over.",
    ),
    tabel(
        "Welke vernieuwingen maakten de reizen op open zee mogelijk? Klopt elke uitspraak?",
        [
            ("het kompas", J),
            ("het astrolabium", J),
            ("de scheepsmotor", F),
            ("een schip dat tegen de wind in kon laveren", J),
        ],
        "Kompas, astrolabium, jakobsstaf en schepen die konden laveren. Een motor bestond nog niet.",
    ),
    mk(
        "Waarvoor gebruikte een zeevaarder een astrolabium of een jakobsstaf?",
        [
            "Om de breedtegraad te bepalen uit de hoogte van zon of ster",
            "Om de diepte van het water onder het schip te meten",
            "Om de snelheid van de wind op open zee te meten",
            "Om de tijd te meten tussen twee havens",
        ],
        0,
        "Wie de hoogte van de zon of een ster meet, kan zijn breedtegraad bepalen, ook ver van de kust.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Columbus de Caraïben bereikt.",
        TL, [[24.0, 25, 2.2, 55]],
        "Columbus steekt in 1492 de Atlantische Oceaan over.",
    ),
    tabel(
        "Klopt elke uitspraak over Christoffel Columbus?",
        [
            ("Hij voer in dienst van Spanje.", J),
            ("Hij dacht dat hij in Azië was aangekomen.", J),
            ("Hij wist dat hij een voor Europa onbekend werelddeel bereikt had.", F),
            ("Het werelddeel kreeg zijn naam.", F),
        ],
        "Columbus voer voor Spanje en hield vol dat hij Azië bereikt had. Het werelddeel kreeg later de naam van Amerigo Vespucci.",
    ),
    koppel(
        "Welke beschrijving hoort bij elke persoon?",
        [
            ["Vasco da Gama", "voer als eerste rond Kaap de Goede Hoop tot in Indië"],
            ["Magellaan", "zijn vloot voer als eerste rond de wereld"],
            ["Amerigo Vespucci", "gaf zijn naam aan een werelddeel"],
            ["Cortés", "geen ontdekkingsreiziger maar een veroveraar"],
        ],
        ["bereikte als eerste de zuidpool"],
        "Da Gama vond de zeeweg naar Indië, Magellaans vloot voer rond de wereld, Vespucci gaf Amerika zijn naam en Cortés was een veroveraar. De zuidpool werd pas veel later bereikt.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Vasco da Gama in Calicut aankomt.",
        TL, [[25.3, 25, 2.2, 55]],
        "Vasco da Gama bereikt Calicut in 1498.",
    ),
    # --- kolonisatie
    mk(
        "Wat was het verschil tussen de koloniën van Portugal en die van Spanje?",
        [
            "Portugal bouwde handelsposten langs de kust, Spanje veroverde het binnenland",
            "Portugal veroverde grote rijken in het binnenland, Spanje bleef aan de kust",
            "Portugal had enkel koloniën in Amerika, Spanje enkel in Azië",
            "Portugal liet alle handel over aan Spanje in ruil voor bescherming",
        ],
        0,
        "Portugal wilde de handel beheersen, Spanje het land zelf.",
    ),
    sorteer(
        "Hoort dit land bij de eerste of bij de tweede kolonisatiegolf?",
        ["Eerste golf", "Tweede golf"],
        [
            ["Portugal", "Eerste golf"],
            ["Spanje", "Eerste golf"],
            ["Engeland", "Tweede golf"],
            ["Frankrijk", "Tweede golf"],
            ["de Verenigde Provinciën", "Tweede golf"],
        ],
        "De eerste golf begint rond 1500, de tweede in de 17de eeuw.",
    ),
    tabel(
        "Wat vernietigden de Spanjaarden in de 16de eeuw? Klopt elke uitspraak?",
        [
            ("het Aztekenrijk in Mexico", J),
            ("het Incarijk in de Andes", J),
            ("de Mayasteden in Midden-Amerika", J),
            ("het Chinese keizerrijk", F),
        ],
        "Azteken, Inca's en Maya's. China bleef buiten hun bereik.",
    ),
    met_prent(
        "pokken-florentijnse-codex.jpg",
        tabel(
            "Bekijk deze tekening uit de Florentijnse Codex, gemaakt door Azteekse tekenaars. Klopt elke uitspraak?",
            [
                ("Ze toont een ziekte waartegen de inheemse bevolking geen weerstand had.", J),
                ("Ze laat het standpunt van de overwonnenen zien.", J),
                ("Oorlog was de belangrijkste oorzaak van de sterfte.", F),
                ("Een Spaanse veroveraar maakte deze tekening.", F),
            ],
            "Ziekten zoals pokken en mazelen waren de belangrijkste oorzaak; oorlog en dwangarbeid kwamen erbovenop. De tekenaars waren Azteken.",
        ),
        volgt=True,
    ),
    inv(
        "Hoe heet het Spaanse systeem waarbij een kolonist arbeid mocht opeisen van de inheemse bevolking, in ruil voor bescherming en bekering? Antwoord met één woord.",
        ["encomienda", "encomiendasysteem", "het encomiendasysteem", "de encomienda"],
        "Dat is het encomiendasysteem. In de praktijk was het dwangarbeid in de mijnen en op de velden.",
    ),
    volgorde(
        "Zet deze stappen in de juiste volgorde: hoe hangen de sterfte in Amerika en de slavenhandel samen?",
        [
            "Kolonisten eisen arbeid op van de inheemse bevolking",
            "Een groot deel van de inheemse bevolking sterft",
            "Er zijn te weinig arbeiders voor mijnen en velden",
            "De arbeid wordt uit Afrika gehaald",
        ],
        "Stierf de inheemse bevolking weg, dan viel de gedwongen arbeid weg. Die arbeid haalde men daarna uit Afrika.",
    ),
    mk(
        "Waarom spreekt men in Brazilië Portugees en in de rest van Zuid-Amerika vooral Spaans?",
        [
            "Taal toont vandaag nog welk land welk gebied koloniseerde",
            "Brazilië koos die taal na zijn onafhankelijkheid zelf",
            "De inheemse volkeren in Brazilië spraken al Portugees",
            "Het Portugees is een makkelijkere taal voor handel",
        ],
        0,
        "Taal, plaatsnamen, godsdienst en rechtssysteem dragen nog het spoor van de kolonisator.",
    ),
    koppel(
        "Welk begrip over de koloniën past bij elke beschrijving?",
        [
            ["een heel gebied met één gewas beplant, voor de uitvoer", "Monocultuur"],
            ["de grond of de mijn uitputten zonder aan later te denken", "Roofbouw"],
        ],
        ["Kapitalisme"],
        "Monocultuur gaat over één gewas, roofbouw over uitputten.",
    ),
    sorteer(
        "Kwam dit product uit Amerika of uit Azië?",
        ["Uit Amerika", "Uit Azië"],
        [
            ["zilver", "Uit Amerika"],
            ["aardappelen", "Uit Amerika"],
            ["maïs", "Uit Amerika"],
            ["rijst", "Uit Azië"],
            ["specerijen", "Uit Azië"],
        ],
        "Zilver kwam uit de Andes, aardappelen en maïs uit Amerika. Rijst en specerijen kwamen uit Azië.",
    ),
    mk(
        "Een historicus zet het woord 'Nieuwe' in 'Nieuwe' Wereld tussen aanhalingstekens. Wat wil die daarmee zeggen?",
        [
            "Ze was enkel nieuw voor de Europeanen, er woonden al miljoenen mensen",
            "Het werelddeel was pas kort daarvoor uit de zee opgerezen",
            "De naam werd pas in de 20ste eeuw voor het eerst gebruikt",
            "Columbus noemde het werelddeel zelf nooit zo, maar Cortés wel",
        ],
        0,
        "Er bestonden al rijken en steden. Nieuw was die wereld alleen voor wie uit Europa kwam.",
    ),
    mk(
        "Waarom geeft een Spaanse kroniek over de verovering van Mexico geen volledig beeld?",
        [
            "Ze is door de winnaar geschreven, vaak om zichzelf te verdedigen",
            "Spaanse kronieken werden altijd pas eeuwen later geschreven",
            "Spanjaarden mochten van hun koning niets over Mexico schrijven",
            "De Azteken hebben alle Spaanse kronieken achteraf veranderd",
        ],
        0,
        "Wie wint, schrijft vaak om zijn eigen optreden te verdedigen. Azteekse verslagen vertellen het anders.",
    ),
    # --- driehoekshandel
    dict(
        **koppel(
            "Bekijk het schema van de driehoekshandel. Wat werd er langs elke pijl vervoerd?",
            [
                ["pijl 1", "wapens, textiel en alcohol"],
                ["pijl 2", "tot slaaf gemaakte mensen"],
                ["pijl 3", "suiker, katoen en tabak"],
            ],
            ["specerijen en zijde"],
            "Op elk been werd winst gemaakt. Specerijen en zijde kwamen uit Azië, langs een heel andere route.",
        ),
        afbeelding_url=DRIEHOEK,
    ),
    klik(
        "Bekijk opnieuw het schema. Klik op het been dat men de middenpassage noemt.",
        "driehoekshandel.svg", [[17.0, 70.0, 52.0, 27.0]],
        "De middenpassage is de oversteek van Afrika naar Amerika.",
    ),
    met_prent(
        "slavenschip-brookes.jpg",
        tabel(
            "Bekijk de doorsnede van het slavenschip Brookes. Klopt elke uitspraak?",
            [
                ("Mensen lagen weken in het ruim, vastgeketend.", J),
                ("Een groot deel van hen overleefde de overtocht niet.", J),
                ("Op dit schip werden specerijen uit Azië vervoerd.", F),
                ("Zo'n tekening toont mensen die tot koopwaar gemaakt werden.", J),
            ],
            "De overtocht was mensonterend en velen stierven. Wat op papier een handelsstroom is, gaat over mensen.",
        ),
        volgt=True,
    ),
    mk(
        "Waaraan zie je dat de slavenhandel in Europa lang als een gewone handel gold?",
        [
            "Er werd openlijk in geïnvesteerd, met aandelen en verzekeringen",
            "Alleen de koning mocht er geld aan verdienen",
            "Hij gebeurde enkel in het geheim, buiten elke wet",
            "De Kerk betaalde zelf alle schepen en verdeelde de winst",
        ],
        0,
        "Pas in de 18de eeuw groeit er een beweging die de slavenhandel wil afschaffen.",
    ),
    # --- commerciële revolutie
    tabel(
        "Klopt elke uitspraak over het handelskapitalisme?",
        [
            ("Winst wordt opnieuw geïnvesteerd om meer winst te maken.", J),
            ("Meerdere mensen leggen hun kapitaal samen.", J),
            ("Het risico wordt over veel aandeelhouders gespreid.", J),
            ("De schepen waren meestal eigendom van de vorst.", F),
        ],
        "Investeren, samenleggen en spreiden. De schepen waren meestal van particuliere compagnieën.",
    ),
    mk(
        "Wat houdt het mercantilisme in?",
        [
            "Een land moet meer uitvoeren dan invoeren om edelmetaal binnen te halen",
            "Een land moet vrij handelen met alle landen zonder invoerrechten",
            "Een land moet al zijn edelmetaal uitgeven aan nieuwe koloniën",
            "Een land moet de handel met zijn koloniën overlaten aan andere landen",
        ],
        0,
        "Daarom beschermde een vorst zijn eigen nijverheid met invoerrechten. Vrije handel is net niet wat het mercantilisme wil.",
    ),
    koppel(
        "Welke vorm van handel of nijverheid past bij elke beschrijving?",
        [
            ["een onderneming waarvan het kapitaal in verhandelbare delen verdeeld is", "Handelscompagnie"],
            ["een handelaar levert grondstof aan gezinnen die thuis werken", "Huisnijverheid"],
            ["arbeiders werken samen op één plaats, nog met de hand", "Manufactuur"],
        ],
        ["Gilde"],
        "De Verenigde Oost-Indische Compagnie is het bekendste voorbeeld van een handelscompagnie. Een gilde is een middeleeuwse vereniging van ambachtslui.",
    ),
    mk(
        "Hoe hangen de ontdekkingsreizen samen met het ontstaan van het handelskapitalisme?",
        [
            "Een reis vroeg veel geld vooraf en beloofde grote winst achteraf",
            "De ontdekkingsreizigers brachten het idee van aandelen mee uit Amerika",
            "De reizen werden altijd volledig door de Kerk betaald",
            "Na elke reis werd de winst gelijk verdeeld over alle inwoners",
        ],
        0,
        "Precies daarom legde men geld samen en spreidde men het risico.",
    ),
    keuze(
        "Bij het vruchtwisselstelsel staat elk jaar [[*een ander gewas|hetzelfde gewas]] op een veld, zodat er geen [[*braakland|weiland|bos]] meer nodig is. Voedergewassen zoals [[*klaver|rijst|katoen]] zorgen voor meer vee op stal, en dus voor meer mest. Kunstmest komt pas in de [[*19de|16de|17de]] eeuw.",
        "Meer voedsel per stuk grond liet de bevolking van Europa in de 18de eeuw sterk groeien.",
    ),
    casus(
        "Rond 1650 trouwt de dochter van een rijke Antwerpse koopman met de zoon van een verarmde edelman. De koopman koopt ook een ambt dat hem aanzien geeft.",
        [
            mk(
                "Wat toont dit voorbeeld over de standensamenleving in de vroegmoderne tijd?",
                [
                    "De standen bestaan nog, maar geld begint titels te kopen",
                    "De standen zijn afgeschaft en iedereen is voortaan gelijk",
                    "Een koopman wordt door zijn huwelijk meteen geestelijke",
                    "De adel heeft alle macht verloren aan de boeren",
                ],
                0,
                "De rijke burgerij wordt machtiger dan haar stand laat vermoeden, en sommige adellijke families verarmen.",
            ),
            tabel(
                "Klopt elke uitspraak over de vroegmoderne tijd?",
                [
                    ("De standen blijven in de wet bestaan tot de Franse Revolutie.", J),
                    ("De grond bleef grotendeels in handen van adel en Kerk.", J),
                    ("De rijke burgerij verloor in deze tijd haar macht.", F),
                    ("Het zilver uit Amerika maakte Spanje blijvend het sterkste land.", F),
                ],
                "De standen bleven, maar de verhoudingen schoven. Het zilver ging naar oorlogen en invoer, en de winst bleef bij de landen die leverden.",
            ),
        ],
    ),
]

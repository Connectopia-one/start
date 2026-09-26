# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Geschiedenis van België, deel 1: 1830 tot de Groote Oorlog."""

VAK = "Geschiedenis van België"
BESTAND = "geschiedenis-van-belgie.json"
TITEL = "Van 1830 tot de Groote Oorlog"
VOLGORDE = 1

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurde er op 25 augustus 1830 in de Muntschouwburg in Brussel?",
        "opties": [
            "Een opera bracht het publiek zo op dreef dat er rellen uitbraken",
            "Het Nederlandse leger bezette de zaal om een vergadering te stoppen",
            "De onafhankelijkheid van België werd er plechtig uitgeroepen",
            "Koning Willem I hield er een toespraak die verkeerd viel",
        ],
        "antwoord": 0,
        "uitleg": "Het ging om De Stomme van Portici, een opera over een opstand in Napels. Na het duet over de liefde voor het vaderland liep het publiek de straat op. De onvrede zat er natuurlijk al langer: over taal, belastingen en godsdienst.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Onder welk land viel ons gebied vlak vóór de opstand van 1830?",
        "opties": [
            "Het Verenigd Koninkrijk der Nederlanden",
            "Het keizerrijk van Napoleon in Frankrijk",
            "Het Oostenrijkse keizerrijk van de Habsburgers",
            "Het koninkrijk Pruisen, met Berlijn als hoofdstad",
        ],
        "antwoord": 0,
        "uitleg": "Het Congres van Wenen had in 1815, na de nederlaag van Napoleon, Noord en Zuid samengevoegd onder koning Willem I. Dat moest een buffer tegen Frankrijk zijn. Na vijftien jaar liep het spaak.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk jaar legde Leopold I de eed af als eerste koning der Belgen? Geef het jaartal.",
        "antwoord": "1831",
        "uitleg": "Op 21 juli 1831, en daarom is dat onze nationale feestdag. Hij was een Duitse prins, Leopold van Saksen-Coburg-Gotha, die enkele dagen eerder in De Panne voet aan wal zette.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De Belgische grondwet van 1831 gold in Europa als erg vooruitstrevend. Waarom?",
        "opties": [
            "De macht van de koning werd ingeperkt en er stonden vrijheden in",
            "Elke volwassen inwoner kreeg meteen stemrecht, ook de vrouwen",
            "Het land werd meteen opgedeeld in gewesten en gemeenschappen",
            "De koning werd door het volk verkozen in plaats van geërfd",
        ],
        "antwoord": 0,
        "uitleg": "Vrijheid van drukpers, van vereniging en van godsdienst, en een koning die alleen mag handelen met een minister die verantwoording aflegt. Stemrecht was er nog lang niet voor iedereen: eerst mochten alleen mannen stemmen die genoeg belasting betaalden.",
    },
    {
        "type": "waarofniet",
        "vraag": "Nederland erkende België pas negen jaar na de onafhankelijkheid.",
        "antwoord": True,
        "uitleg": "Koning Willem I bleef weigeren en stuurde in 1831 zelfs nog een leger, de Tiendaagse Veldtocht. Pas met het Verdrag van Londen in 1839 gaf hij toe. Daarbij verloor België wel een stuk Limburg en Luxemburg.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In 1835 reed er tussen Brussel en Mechelen iets wat nergens anders op het Europese vasteland bestond. Wat?",
        "opties": [
            "De eerste spoorlijn met een stoomtrein voor reizigers",
            "De eerste tramlijn die door paarden getrokken werd",
            "De eerste verharde steenweg tussen twee grote steden",
            "De eerste telegraaflijn waarmee je berichten kon sturen",
        ],
        "antwoord": 0,
        "uitleg": "Het jonge land wilde zich niet afhankelijk maken van Nederlandse waterwegen en legde daarom meteen een eigen spoornet aan. Alleen Engeland was ons voor. België had lange tijd het dichtste spoornet ter wereld.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waar draaide de industriële revolutie in de negentiende eeuw vooral in ons land?",
        "opties": [
            "In Wallonië, rond de steenkool en de staalfabrieken",
            "In Vlaanderen, rond de haven en de scheepsbouw",
            "In Brussel, rond de banken en de handelshuizen",
            "In de Kempen, rond de glas- en de zinkfabrieken",
        ],
        "antwoord": 0,
        "uitleg": "In de vallei van Samber en Maas lag steenkool aan de oppervlakte, en daar bouwde John Cockerill in Seraing zijn fabrieken. België was na Engeland het tweede land ter wereld dat industrialiseerde. Pas veel later, met de Kempense mijnen en de haven, draaide de verhouding om.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wie was in 1885 de eigenaar van de Kongo-Vrijstaat in Centraal-Afrika?",
        "opties": [
            "Koning Leopold II persoonlijk, niet de Belgische staat",
            "De Belgische staat, die het gebied met leningen had gekocht",
            "Een groep Antwerpse handelaars die er rubber wilden halen",
            "Frankrijk, dat het gebied aan België in bruikleen gaf",
        ],
        "antwoord": 0,
        "uitleg": "De conferentie van Berlijn kende hem het gebied toe als privébezit, tachtig keer zo groot als België. Onder het dwangregime voor ivoor en rubber vielen er enorm veel slachtoffers. Na internationale verontwaardiging nam de Belgische staat het in 1908 over.",
    },
    {
        "type": "waarofniet",
        "vraag": "Vanaf de grondwet van 1831 was Nederlands een officiële bestuurstaal in België.",
        "antwoord": False,
        "uitleg": "Het bestuur, het gerecht, het leger en het middelbaar onderwijs liepen in het Frans, terwijl de meerderheid van de bevolking Nederlands sprak. Pas met de Gelijkheidswet van 1898 werden de twee talen wettelijk evenwaardig, en zelfs daarna duurde het nog lang.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom viel het Duitse leger in augustus 1914 België binnen?",
        "opties": [
            "Het wilde via ons land snel tot bij Parijs geraken",
            "Het wilde de haven van Antwerpen in handen krijgen",
            "België had Duitsland eerst de oorlog verklaard",
            "Het kwam de Duitstalige inwoners van de Oostkantons halen",
        ],
        "antwoord": 0,
        "uitleg": "Het Duitse plan rekende op een bliksemsnelle doorsteek langs het vlakke België om Frankrijk te verrassen. België was officieel neutraal en weigerde de doortocht, en die weigering kostte de Duitsers kostbare weken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De slag bij Halen van 12 augustus 1914 kreeg een bijnaam. Welke?",
        "opties": [
            "De Slag der Zilveren Helmen",
            "De Slag van de Gouden Sporen",
            "De Slag om de IJzeren Poort",
            "De Slag van de Rode Duivels",
        ],
        "antwoord": 0,
        "uitleg": "De Belgische ruiterij hield de Duitse cavalerie tegen en hield het slagveld. De naam komt van de blinkende helmen van de Duitse kurassiers die achterbleven. Verwar het niet met de Guldensporenslag: die was in 1302 bij Kortrijk.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe stopte het Belgische leger eind oktober 1914 de Duitse opmars bij Nieuwpoort?",
        "opties": [
            "Het liet de vlakte achter de IJzer onder water lopen",
            "Het blies alle bruggen over de IJzer tegelijk op",
            "Het groef een aaneengesloten muur van zandzakken",
            "Het stak de duinen in brand om een rookgordijn te maken",
        ],
        "antwoord": 0,
        "uitleg": "Met de sluizen van Nieuwpoort lieten ze bij vloed zeewater binnen. De modderige vlakte werd onbegaanbaar voor kanonnen en paarden. Sluiswachter Karel Cogge en schipper Hendrik Geeraert kenden het ingewikkelde sluizenstelsel en wezen de weg.",
    },
    {
        "type": "waarofniet",
        "vraag": "De frontlijn in België bleef van eind 1914 tot 1918 vrijwel op dezelfde plaats liggen.",
        "antwoord": True,
        "uitleg": "Vier jaar loopgravenoorlog, met een front dat vaak maar enkele kilometers heen en weer schoof, voor honderdduizenden slachtoffers. Rond Ieper werd voor het eerst op grote schaal gifgas ingezet, in april 1915.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke bijnaam kreeg koning Albert I tijdens de Eerste Wereldoorlog?",
        "opties": [
            "De koning-ridder",
            "De koning-bouwer",
            "De koning-soldaat van Congo",
            "De laatste koning der Belgen",
        ],
        "antwoord": 0,
        "uitleg": "Hij bleef bij zijn leger achter de IJzer in plaats van naar het buitenland te vertrekken, en dat maakte hem erg geliefd. Koning-bouwer was de bijnaam van Leopold II, vanwege zijn vele grote bouwwerken.",
    },
    {
        "type": "invultekst",
        "vraag": "Op welke dag en maand wordt de wapenstilstand van 1918 herdacht? Schrijf bijvoorbeeld: 3 maart.",
        "antwoord": "11 november",
        "uitleg": "Het vuren stopte op 11 november 1918 om elf uur 's ochtends: het elfde uur van de elfde dag van de elfde maand. Het is in België nog altijd een wettelijke feestdag.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurt er sinds 1928 elke avond onder de Menenpoort in Ieper?",
        "opties": [
            "Brandweermannen blazen de Last Post voor de gesneuvelden",
            "De namen van alle gesneuvelden worden hardop voorgelezen",
            "Een klok luidt even veel slagen als er oorlogsjaren waren",
            "Kinderen leggen een krans namens de stad bij de poort",
        ],
        "antwoord": 0,
        "uitleg": "Elke avond om acht uur, met alleen een onderbreking tijdens de bezetting in de Tweede Wereldoorlog. In de poort staan bijna 55 000 namen van vermisten wier lichaam nooit gevonden werd.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe kwamen Eupen en Sankt Vith na de Eerste Wereldoorlog bij België?",
        "opties": [
            "Duitsland moest ze afstaan bij het Verdrag van Versailles",
            "De inwoners kochten zich met een grote volkslening vrij",
            "Nederland ruilde ze met België voor een stuk Limburg",
            "Ze hadden al sinds 1830 bij België gehoord",
        ],
        "antwoord": 0,
        "uitleg": "Daardoor heeft België sinds 1920 een Duitstalige gemeenschap, vandaag ongeveer 80 000 inwoners met een eigen parlement en regering. Ons land heeft dus drie officiële talen, geen twee.",
    },
    {
        "type": "waarofniet",
        "vraag": "In 1919 kregen alle Belgische mannen én vrouwen samen het stemrecht.",
        "antwoord": False,
        "uitleg": "In 1919 kwam het algemeen enkelvoudig stemrecht voor mannen vanaf 21 jaar; daarvoor konden rijkere mannen meerdere stemmen uitbrengen. Vrouwen mochten vanaf 1921 wel al bij de gemeenteraadsverkiezingen stemmen, maar pas in 1948 ook bij de nationale.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom gingen kinderen in de negentiende eeuw massaal in de fabriek werken?",
        "opties": [
            "Een arbeidersgezin kon niet rondkomen van één loon alleen",
            "De wet verplichtte kinderen vanaf tien jaar om te gaan werken",
            "Fabrieken betaalden kinderen meer dan volwassen arbeiders",
            "Er was toen nog geen enkele school in het hele land",
        ],
        "antwoord": 0,
        "uitleg": "Kinderen waren goedkoop en pasten in nauwe ruimtes tussen de machines. Pas in 1889 kwam er een eerste beperking, en de leerplicht tot veertien jaar kwam er in 1914, al ging die door de oorlog pas later echt in.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke twee zaken botsten in de negentiende eeuw in de Belgische politiek het hardst?",
        "opties": [
            "De katholieken en de liberalen, vooral over het onderwijs",
            "De Vlamingen en de Walen, vooral over de taalgrens",
            "De koning en het parlement, vooral over het leger",
            "De boeren en de handelaars, vooral over de graanprijs",
        ],
        "antwoord": 0,
        "uitleg": "Die twee partijen beheersten decennialang het toneel, met het onderwijs als heetste hangijzer: van de kerk of van de staat? Rond 1885 kwam daar met de Belgische Werkliedenpartij een derde stroming bij.",
    },
]

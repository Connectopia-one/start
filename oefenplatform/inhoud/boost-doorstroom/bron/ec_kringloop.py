# -*- coding: utf-8 -*-
"""De vragen voor "De economische kringloop" (🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek "de
economie als systeem". Dit thema neemt het eerste stuk: het eenvoudige
kringloopschema, de actoren erin en de twee stromen die tussen hen lopen.

Deel 1 gaat over het schema zelf: wat economie bestudeert, wie de actoren zijn
(gezinnen, bedrijven en de overheid), en wat elk van hen in de kringloop doet.
Deel 2 gaat over de twee stromen: de goederen- en dienstenstroom en de
geldstroom, die altijd in tegengestelde richting lopen, en over wat er gebeurt
als de overheid of het buitenland erbij komt.

Afspraak in dit thema: elke stroom wordt benoemd met wie ze verlaat en wie ze
bereikt, nooit met alleen een pijl, zodat een vraag ook zonder tekening klopt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarover gaat economie als wetenschap?",
        opties=[
            "Over de keuzes bij het produceren, verdelen en verbruiken van goederen en diensten",
            "Over het beleggen van geld op de beurs en het sparen van een gezin",
            "Over het opstellen van de boekhouding en de balans van een bedrijf",
            "Over de prijzen die de winkels in een land voor hun producten vragen",
        ],
        antwoord=0,
        uitleg="Economie betekent letterlijk huishoudkunde. Ze bestudeert welke keuzes mensen, bedrijven en de overheid maken bij produceren, verdelen en verbruiken, en wat die keuzes met de samenleving doen. Beleggen, boekhouden en prijzen zijn er maar stukjes van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie actoren staan in een eenvoudig economisch kringloopschema?",
        opties=[
            "De gezinnen, de bedrijven en de overheid",
            "De werknemers, de werkgevers en de vakbonden",
            "De kopers, de verkopers en de banken",
            "De producenten, de handelaars en de klanten",
        ],
        antwoord=0,
        uitleg="Het eenvoudige schema werkt met drie binnenlandse actoren: gezinnen, bedrijven en overheid. Vakbonden, banken en handelaars bestaan wel, maar krijgen in dit schema geen aparte plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen de gezinnen in de economische kringloop? Duid alles aan wat juist is.",
        opties=[
            "Ze leveren productiefactoren, zoals arbeid",
            "Ze kopen goederen en diensten bij de bedrijven",
            "Ze betalen belastingen aan de overheid",
            "Ze maken de goederen die in de winkel liggen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gezinnen leveren arbeid en andere productiefactoren, ze verbruiken goederen en diensten, en ze betalen belastingen. Het produceren zelf gebeurt bij de bedrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat krijgt een gezin in ruil voor de arbeid die het levert?",
        opties=[
            "Een loon",
            "Een dividend",
            "Een subsidie",
            "Een intrest",
        ],
        antwoord=0,
        uitleg="Elke productiefactor heeft zijn eigen vergoeding: arbeid wordt betaald met loon, kapitaal met intrest, natuur met pacht of huur, en ondernemerschap met winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie betaalt in de kringloop een vergoeding aan wie?",
        opties=[
            "De bedrijven betalen de gezinnen voor hun productiefactoren",
            "De gezinnen betalen de bedrijven voor hun productiefactoren",
            "De overheid betaalt de bedrijven voor de arbeid van de gezinnen",
            "De gezinnen betalen elkaar voor de arbeid die zij leveren",
        ],
        antwoord=0,
        uitleg="De gezinnen zetten hun productiefactoren ter beschikking van de bedrijven, en de bedrijven betalen daarvoor: dat is de stroom van lonen, intresten, pacht en winst.",
    ),
    dict(
        type="waarofniet",
        vraag="In de economische kringloop zijn de gezinnen alleen verbruikers en nooit leveranciers.",
        antwoord=False,
        uitleg="Ze zijn allebei. Een gezin verbruikt goederen en diensten, maar het levert ook de productiefactoren, in de eerste plaats de arbeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de overheid in de kringloop? Duid alles aan wat juist is.",
        opties=[
            "Ze int belastingen bij de gezinnen en de bedrijven",
            "Ze levert diensten, zoals onderwijs en veiligheid",
            "Ze betaalt uitkeringen en lonen van ambtenaren uit",
            "Ze bepaalt het loon dat elk bedrijf aan elke werknemer betaalt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De overheid int belastingen, levert collectieve diensten en betaalt uitkeringen en ambtenarenlonen. Lonen in de privésector worden niet door de overheid vastgelegd, maar afgesproken tussen werkgevers en werknemers.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vergoeding voor de productiefactor kapitaal? Schrijf één woord.",
        antwoord=["intrest", "interest", "rente"],
        uitleg="Kapitaal wordt vergoed met intrest. Arbeid krijgt loon, natuur pacht of huur, en ondernemerschap winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker koopt bloem bij een molenaar. Welke actoren staan hier tegenover elkaar?",
        opties=[
            "Twee bedrijven",
            "Een bedrijf en een gezin",
            "Een gezin en de overheid",
            "Een bedrijf en de overheid",
        ],
        antwoord=0,
        uitleg="De bakkerij en de maalderij zijn allebei bedrijven. Ook tussen bedrijven onderling lopen er stromen, want het ene bedrijf koopt bij het andere.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zelfstandige kapster zonder personeel staat in het kringloopschema bij de gezinnen.",
        antwoord=False,
        uitleg="Alles wat produceert om te verkopen, hoort bij de bedrijven, ook een eenmanszaak zonder personeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet het een kringloop en geen rechte lijn?",
        opties=[
            "Omdat wat de ene actor uitgeeft, bij een andere binnenkomt, en zo weer terugkeert",
            "Omdat de economie elk jaar opnieuw even groot wordt als het jaar ervoor",
            "Omdat de prijzen altijd stijgen en daarna weer dalen tot hun beginpunt",
            "Omdat de gezinnen evenveel verdienen als wat zij in een jaar uitgeven",
        ],
        antwoord=0,
        uitleg="De uitgave van de ene is het inkomen van de andere. Het loon dat een bedrijf uitbetaalt, komt via de aankopen van het gezin weer bij de bedrijven terecht: zo sluit de kring.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vergoeding voor de productiefactor arbeid? Schrijf één woord.",
        antwoord=["loon", "wedde"],
        uitleg="Arbeid wordt vergoed met loon. Dat is de grootste geldstroom van de bedrijven naar de gezinnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin spaart een deel van zijn inkomen. Wat gebeurt er dan met de kringloop?",
        opties=[
            "Er vloeit geld weg uit de kringloop, tot het via de banken weer wordt uitgeleend",
            "De kringloop stopt, want geld dat niet wordt uitgegeven, verdwijnt",
            "Het gespaarde geld telt dubbel mee, want het blijft binnen het gezin",
            "De bedrijven betalen dat spaargeld terug aan de overheid",
        ],
        antwoord=0,
        uitleg="Sparen is een lek: dat geld wordt niet meteen besteed. Via de banken komt het meestal weer in de kringloop als krediet voor investeringen.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke uitgave van de ene actor is een inkomen voor een andere actor.",
        antwoord=True,
        uitleg="Dat is precies de gedachte achter de kringloop: geld verdwijnt niet, het verandert van eigenaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over de overheid in de kringloop klopt?",
        opties=[
            "Ze is tegelijk ontvanger van belastingen en koper van goederen en diensten",
            "Ze ontvangt alleen belastingen en geeft zelf niets uit",
            "Ze koopt enkel bij het buitenland en nooit bij binnenlandse bedrijven",
            "Ze staat buiten de kringloop en speelt daarin geen enkele rol",
        ],
        antwoord=0,
        uitleg="De overheid staat midden in de kringloop: ze int belastingen, maar ze koopt ook goederen en diensten, betaalt lonen en keert uitkeringen uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geld dat een gezin van zijn inkomen niet uitgeeft? Schrijf één woord.",
        antwoord=["sparen", "spaargeld", "besparing"],
        uitleg="Wat niet besteed wordt, is sparen. In de kringloop is dat een lek, dat via de banken weer binnenkomt als krediet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf koopt een nieuwe machine. Hoe heet die uitgave?",
        opties=[
            "Een investering",
            "Een consumptie",
            "Een belasting",
            "Een subsidie",
        ],
        antwoord=0,
        uitleg="Een bedrijf dat kapitaalgoederen koopt om mee te produceren, investeert. Consumptie is wat de gezinnen kopen om te verbruiken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkloosheidsuitkering is een geldstroom van de overheid naar de gezinnen.",
        antwoord=True,
        uitleg="Uitkeringen gaan van de overheid naar de gezinnen, net als de lonen van ambtenaren. In de andere richting lopen de belastingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke actor hoort niet thuis in het eenvoudige binnenlandse kringloopschema?",
        opties=[
            "Het buitenland",
            "De gezinnen",
            "De bedrijven",
            "De overheid",
        ],
        antwoord=0,
        uitleg="Het eenvoudige schema blijft binnen de landsgrenzen. Zodra je invoer en uitvoer meeneemt, komt het buitenland erbij als vierde actor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is zo'n schema nuttig, ook al is het een vereenvoudiging?",
        opties=[
            "Het toont in één beeld wie met wie ruilt en in welke richting het geld loopt",
            "Het geeft de precieze bedragen weer die elk gezin in een jaar uitgeeft",
            "Het voorspelt wat de prijzen volgend jaar in de winkel zullen zijn",
            "Het vervangt de statistieken van de Nationale Bank van België",
        ],
        antwoord=0,
        uitleg="Een model laat met opzet details weg om de grote lijn te tonen: wie ruilt met wie, en in welke richting. De precieze cijfers haal je bij Statbel of de Nationale Bank.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke twee stromen lopen er in een economische kringloop?",
        opties=[
            "De goederen- en dienstenstroom en de geldstroom",
            "De invoerstroom en de uitvoerstroom",
            "De spaarstroom en de investeringsstroom",
            "De loonstroom en de belastingstroom",
        ],
        antwoord=0,
        uitleg="Bij elke ruil horen twee stromen: wat er geleverd wordt (goederen, diensten of productiefactoren) en wat ervoor betaald wordt (geld).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lopen die twee stromen ten opzichte van elkaar?",
        opties=[
            "In tegengestelde richting",
            "In dezelfde richting",
            "Allebei van de bedrijven naar de gezinnen",
            "Allebei van de gezinnen naar de bedrijven",
        ],
        antwoord=0,
        uitleg="Wie iets levert, krijgt er geld voor terug. De goederenstroom gaat dus de ene kant op en de geldstroom de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin koopt brood bij de bakker. Welke stroom gaat van het gezin naar de bakker?",
        opties=[
            "De geldstroom",
            "De goederenstroom",
            "De dienstenstroom",
            "De arbeidsstroom",
        ],
        antwoord=0,
        uitleg="Het brood gaat van de bakker naar het gezin, en het geld gaat de andere kant op, van het gezin naar de bakker.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij elke ruil horen altijd twee stromen in dezelfde richting.",
        antwoord=False,
        uitleg="Ze lopen net in tegengestelde richting: wat geleverd wordt de ene kant op, en de betaling de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer gaat werken bij een bedrijf. Welke stroom loopt er van het gezin naar het bedrijf?",
        opties=[
            "De stroom van de productiefactor arbeid",
            "De geldstroom in de vorm van een loon",
            "De goederenstroom in de vorm van een product",
            "De stroom van de belastingen",
        ],
        antwoord=0,
        uitleg="Het gezin levert arbeid aan het bedrijf; het bedrijf betaalt daar loon voor. De arbeid gaat dus heen, het geld terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je samen alles wat gezinnen en bedrijven aan elkaar leveren zonder geld? Schrijf twee woorden.",
        antwoord=["reële stroom", "reele stroom", "goederenstroom"],
        uitleg="De reële stroom is alles wat echt van hand verandert: goederen, diensten en productiefactoren. Daartegenover staat de geldstroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze stromen zijn geldstromen? Duid alles aan wat juist is.",
        opties=[
            "Het loon van een arbeider",
            "De btw die een winkel doorstort",
            "Een werkloosheidsuitkering",
            "Het brood dat de bakker aan een klant geeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Loon, belastingen en uitkeringen zijn allemaal geld dat van de ene actor naar de andere gaat. Het brood zelf hoort bij de goederenstroom.",
    ),
    dict(
        type="waarofniet",
        vraag="De diensten van een kapper horen bij de reële stroom en niet bij de geldstroom.",
        antwoord=True,
        uitleg="Een dienst is niet tastbaar, maar ze wordt wel echt geleverd. Dat hoort bij de reële stroom; het geld dat de klant betaalt, is de geldstroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid bouwt een school en betaalt daarvoor een aannemer. Welke richting heeft de geldstroom?",
        opties=[
            "Van de overheid naar het bedrijf",
            "Van het bedrijf naar de overheid",
            "Van de gezinnen naar het bedrijf",
            "Van het bedrijf naar de gezinnen",
        ],
        antwoord=0,
        uitleg="De overheid is hier de koper, dus betaalt zij. De bouw zelf, de dienst van de aannemer, loopt in de andere richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat komt erbij in de kringloop zodra je het buitenland meeneemt? Duid alles aan wat juist is.",
        opties=[
            "Invoer: goederen en diensten die binnenkomen",
            "Uitvoer: goederen en diensten die het land verlaten",
            "Geldstromen van en naar het buitenland",
            "Een vierde soort productiefactor, naast arbeid en kapitaal",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het buitenland brengt invoer, uitvoer en de bijbehorende geldstromen mee. De productiefactoren blijven dezelfde vier: arbeid, kapitaal, natuur en ondernemerschap.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je goederen die uit het buitenland het land binnenkomen? Schrijf één woord.",
        antwoord=["invoer", "import"],
        uitleg="Wat binnenkomt is invoer of import; wat het land verlaat is uitvoer of export.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgisch bedrijf verkoopt machines aan een klant in Spanje. Wat klopt?",
        opties=[
            "De goederen gaan naar Spanje en het geld komt naar België",
            "De goederen en het geld gaan allebei naar Spanje",
            "De goederen komen naar België en het geld gaat naar Spanje",
            "Er is alleen een geldstroom en geen goederenstroom",
        ],
        antwoord=0,
        uitleg="Bij uitvoer verlaten de goederen het land en komt de betaling binnen. De twee stromen blijven tegengesteld.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de ene actor minder uitgeeft, verliest een andere actor inkomen.",
        antwoord=True,
        uitleg="Dat is het kettingeffect van de kringloop: minder bestedingen bij de gezinnen betekent minder omzet bij de bedrijven, en dus minder inkomen daar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin krijgt 2 500 euro loon, betaalt 600 euro belasting en spaart 300 euro. Hoeveel blijft er over om te besteden?",
        opties=[
            "1 600 euro",
            "1 900 euro",
            "2 200 euro",
            "1 300 euro",
        ],
        antwoord=0,
        uitleg="2 500 min 600 belasting is 1 900 beschikbaar inkomen, min 300 sparen blijft 1 600 euro voor consumptie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het begrip 'lek' in de kringloop?",
        opties=[
            "Voor geld dat de kringloop tijdelijk verlaat, zoals sparen, belastingen en invoer",
            "Voor geld dat een bedrijf verliest door diefstal of door een slechte verkoop",
            "Voor het verschil tussen wat een gezin verdient en wat het aan loon vraagt",
            "Voor de fout die in een boekhouding sluipt als twee bedragen niet kloppen",
        ],
        antwoord=0,
        uitleg="Lekken zijn bestedingen die niet bij binnenlandse bedrijven terechtkomen: sparen, belastingen en invoer. Daartegenover staan injecties: investeringen, overheidsuitgaven en uitvoer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het omgekeerde van een lek, het geld dat in de kringloop binnenkomt? Schrijf één woord.",
        antwoord=["injectie", "injecties"],
        uitleg="Investeringen, overheidsuitgaven en uitvoer brengen geld in de kringloop: dat zijn injecties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn lekken uit de binnenlandse kringloop? Duid alles aan wat juist is.",
        opties=[
            "Sparen door de gezinnen",
            "Belastingen aan de overheid",
            "Invoer uit het buitenland",
            "Investeringen door de bedrijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Sparen, belastingen en invoer halen bestedingen uit de binnenlandse kringloop. Investeringen zijn net een injectie: ze brengen bestedingen binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Invoer is een injectie in de binnenlandse kringloop.",
        antwoord=False,
        uitleg="Invoer is een lek: dat geld gaat naar bedrijven in het buitenland. Uitvoer is wél een injectie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente geeft een subsidie aan een lokale sportclub. Hoe past dat in het schema?",
        opties=[
            "Als een geldstroom van de overheid naar een andere actor, zonder tegenprestatie in goederen",
            "Als een goederenstroom van de overheid naar de gezinnen",
            "Als een belasting, want het geld komt van de belastingbetaler",
            "Als een investering van de overheid in kapitaalgoederen",
        ],
        antwoord=0,
        uitleg="Een subsidie of een uitkering is een overdracht: er gaat geld heen zonder dat er een goed of een dienst tegenover staat. Dat heet een overdrachtsuitgave.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tekent een econoom de kringloop vaak met pijlen in twee kleuren?",
        opties=[
            "Om de reële stroom en de geldstroom uit elkaar te houden",
            "Om het verschil tussen binnenland en buitenland te tonen",
            "Om aan te geven welke bedragen groot en welke klein zijn",
            "Om het onderscheid te maken tussen gezinnen en bedrijven",
        ],
        antwoord=0,
        uitleg="De twee stromen lopen over dezelfde lijnen maar in tegengestelde richting. Met twee kleuren zie je in één oogopslag wat geleverd wordt en wat betaald wordt.",
    ),
]

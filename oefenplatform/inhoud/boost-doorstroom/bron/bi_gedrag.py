# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Gedrag en interactie.

Hoort bij de kop "gedrag en interactie" van de vakfiche biologie 2de graad
doorstroomfinaliteit, die 10 % van het examen weegt.

Deel 1 gaat over gedrag bij een individu: aangeboren en geleerd gedrag, de
vormen van leren, en gedrag als antwoord op een prikkel. Deel 2 gaat over
interacties tussen organismen: soortgenoten en groepsgedrag, en de relaties
tussen soorten (predatie, competitie, symbiose, parasitisme, commensalisme).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt een bioloog met gedrag?",
        opties=[
            "alles wat een dier doet als antwoord op prikkels van binnen of van buiten",
            "enkel de bewegingen die een dier met zijn skeletspieren maakt",
            "enkel wat een dier tijdens zijn leven van anderen leert",
            "de manier waarop een dier eruitziet en zich voortbeweegt",
        ],
        antwoord=0,
        uitleg="Gedrag is het waarneembare antwoord op prikkels. Honger is een inwendige prikkel, het geluid van een roofdier een uitwendige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor aangeboren gedrag? Kruis alles aan wat juist is.",
        opties=[
            "het staat vanaf de geboorte vast",
            "het verloopt bij alle dieren van die soort ongeveer gelijk",
            "het moet niet geleerd worden",
            "het verandert sterk met de ervaring van het dier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aangeboren gedrag zit in het erfelijk materiaal en is dus voorspelbaar. Veranderen met de ervaring is net het kenmerk van geleerd gedrag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je gedrag dat een dier niet moet leren omdat het van de geboorte af vastligt?",
        antwoord=["aangeboren gedrag", "aangeboren", "instinct"],
        uitleg="Aangeboren gedrag of instinctief gedrag verloopt bij elk dier van die soort hetzelfde. Een pasgeboren baby die zoekt om te zuigen is een voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is aangeboren gedrag nuttig voor een dier dat pas geboren is?",
        opties=[
            "het werkt meteen, zonder dat er tijd is om iets te leren",
            "het is altijd beter dan het gedrag dat een dier leert",
            "het kost het dier geen energie om uit te voeren",
            "het verandert mee met elke nieuwe omgeving waarin het dier komt",
        ],
        antwoord=0,
        uitleg="Een kuiken dat moet eten en vluchten heeft geen tijd om te oefenen. Het nadeel is dat zo'n gedrag zich niet aan iets nieuws aanpast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reflex is een vorm van aangeboren gedrag.",
        antwoord=True,
        uitleg="Een reflex ligt vast, verloopt bij iedereen gelijk en wordt niet geleerd. Daarmee is het aangeboren gedrag in zijn eenvoudigste vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is gewenning als vorm van leren?",
        opties=[
            "een dier reageert steeds minder op een prikkel die telkens zonder gevolg blijft",
            "een dier leert twee prikkels aan elkaar koppelen die altijd samen komen",
            "een dier leert iets nieuws door een soortgenoot na te doen",
            "een dier onthoudt een weg die het maar één keer gelopen heeft",
        ],
        antwoord=0,
        uitleg="Vogels die eerst van een vogelverschrikker schrikken, gaan er na een week vlak naast zitten. Het schrikken kostte energie en bracht niets op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het leren waarbij een dier een prikkel aan een gevolg koppelt, zoals een hond die kwijlt bij het geluid van zijn bak?",
        antwoord=["conditionering", "conditioneren", "klassieke conditionering"],
        uitleg="Bij conditionering komt een prikkel die eerst niets betekende, voor iets anders te staan. Het dier reageert dan al op het signaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van leren onderscheidt men bij dieren? Kruis alles aan wat juist is.",
        opties=[
            "gewenning",
            "conditionering",
            "leren door nadoen",
            "leren door erfelijkheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gewenning, conditionering, nadoen en leren door proberen zijn vormen van leren. Erfelijkheid geeft net het aangeboren gedrag door, dat niet geleerd wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een jong dier dat zijn moeder nadoet, is een voorbeeld van geleerd gedrag.",
        antwoord=True,
        uitleg="Het jong neemt over wat het ziet. Daarom eten jonge mezen wat hun ouders eten, en kraken sommige groepen noten en andere niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is geleerd gedrag een voordeel in een veranderende omgeving?",
        opties=[
            "het dier kan zijn gedrag bijstellen als de omstandigheden anders worden",
            "het dier hoeft dan geen aangeboren gedrag meer te hebben",
            "geleerd gedrag kost minder energie dan aangeboren gedrag",
            "geleerd gedrag wordt automatisch aan de nakomelingen doorgegeven",
        ],
        antwoord=0,
        uitleg="Verandert het voedsel of de vijand, dan kan een lerend dier een nieuwe aanpak vinden. Een vastliggend gedrag blijft doen wat het altijd deed.",
    ),
    dict(
        type="waarofniet",
        vraag="Geleerd gedrag wordt erfelijk aan de nakomelingen doorgegeven.",
        antwoord=False,
        uitleg="Wat een dier leert, zit niet in zijn erfelijk materiaal. Jongen kunnen het wel van hun ouders overnemen door te kijken en na te doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een sleutelprikkel?",
        opties=[
            "een bepaalde prikkel die een vast gedragspatroon in gang zet",
            "de sterkste prikkel die een dier in zijn leven ooit kreeg",
            "een prikkel die een dier eerst moet leren herkennen",
            "een prikkel die van binnen het lichaam van het dier komt",
        ],
        antwoord=0,
        uitleg="Een rode vlek op de snavel van een meeuw zet het kuiken aan om te bedelen. Eén kenmerk volstaat om het hele patroon te starten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het terugkerende ritme van een dier dat ongeveer een etmaal duurt?",
        antwoord=["dagritme", "biologische klok", "circadiaans ritme"],
        uitleg="Het dagritme regelt slapen, eten en actief zijn. Het loopt ook door als het licht niet verandert, want het dier heeft een eigen klok.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gedrag is bij vogels aangeboren maar wordt door leren bijgeschaafd?",
        opties=[
            "de zang, waarvan de uitvoering van soortgenoten geleerd wordt",
            "het ademen, dat van de eerste dag tot de laatste niet verandert",
            "de kniepeesreflex, die bij elke vogel van de soort gelijk blijft",
            "het kleuren van de veren, dat elk voorjaar opnieuw gebeurt",
        ],
        antwoord=0,
        uitleg="Een jonge vogel begint met een ruwe vorm en verfijnt die door oudere vogels te horen. Daarom hebben sommige soorten plaatselijke dialecten.",
    ),
    dict(
        type="waarofniet",
        vraag="Veel gedrag is deels aangeboren en deels geleerd.",
        antwoord=True,
        uitleg="De grondvorm ligt vaak vast, maar de uitvoering wordt met de ervaring beter. Zuigen is aangeboren, goed drinken wordt geleerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is inprenting?",
        opties=[
            "een jong dier legt in een korte gevoelige periode vast wie zijn ouder is",
            "een dier leert na vele herhalingen een weg door het landschap onthouden",
            "een dier schrikt niet meer van een prikkel die zonder gevolg blijft",
            "een dier neemt het gedrag over van een soort die de zijne niet is",
        ],
        antwoord=0,
        uitleg="Pas uitgekomen eendenkuikens volgen wat ze eerst zien bewegen. Dat venster duurt maar kort en gaat daarna niet meer open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke inwendige prikkels kunnen gedrag uitlokken? Kruis alles aan wat juist is.",
        opties=[
            "honger",
            "dorst",
            "een hormoonspiegel die stijgt in het broedseizoen",
            "het geluid van een roofdier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Honger, dorst en hormonen komen van binnen. Het geluid van een roofdier is een uitwendige prikkel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeker schrijft eerst zijn verklaring op en gaat daarna kijken of het dier zich zo gedraagt.",
        antwoord=False,
        uitleg="Het is net omgekeerd: eerst observeren en noteren, dan verklaren. Wie met een verklaring begint, ziet dingen die er niet zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hond gaat zitten zodra zijn baas een leeg koekjesdoosje laat ritselen. Hoe verklaar je dat?",
        opties=[
            "het geluid is door herhaling aan een belonend gevolg gekoppeld geraakt",
            "zitten is bij honden een aangeboren reflex op elk soort geritsel",
            "de hond raakt gewend aan het geluid en reageert daarom met zitten",
            "de hond doet dit na van een andere hond die het hem voordeed",
        ],
        antwoord=0,
        uitleg="Het geluid betekende eerst niets en kwam daarna telkens voor een koekje te staan. Dat is conditionering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker wil weten of muizen een doolhof leren. Wat is de beste aanpak?",
        opties=[
            "de tijd per poging meten bij een groep muizen en kijken of die daalt",
            "één muis één keer door het hele doolhof laten lopen",
            "de muizen beschrijven zoals ze er van buiten uitzien",
            "de muizen in het doolhof zetten zonder iets op te meten",
        ],
        antwoord=0,
        uitleg="Leren zie je aan een verbetering over herhaalde pogingen. Daarom meet je meerdere dieren en meerdere keren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een interactie tussen twee organismen?",
        opties=[
            "een wederzijdse invloed tussen twee organismen",
            "een gevecht tussen twee dieren van dezelfde soort",
            "een samenwerking waar beide altijd voordeel bij hebben",
            "een ontmoeting die voor beide zonder gevolg blijft",
        ],
        antwoord=0,
        uitleg="Een interactie kan voor beide goed zijn, voor één goed en voor de ander slecht, of voor één onverschillig. Die combinaties geven de soorten relaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is predatie?",
        opties=[
            "het ene organisme doodt en eet het andere",
            "twee organismen strijden om hetzelfde voedsel",
            "het ene organisme leeft op kosten van het andere zonder het te doden",
            "twee organismen hebben elk voordeel bij hun samenleven",
        ],
        antwoord=0,
        uitleg="Bij predatie is er een prooi en een roofdier. Dat is nadelig voor de prooi en voordelig voor de jager.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de strijd tussen twee organismen om dezelfde beperkte hulpbron?",
        antwoord=["competitie", "concurrentie", "de competitie"],
        uitleg="Bij competitie gaan twee organismen achter hetzelfde voedsel, licht of nestplaats aan. Dat werkt voor beide nadelig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen competitie binnen een soort en tussen soorten?",
        opties=[
            "binnen een soort overlappen de behoeften volledig",
            "tussen soorten is er nooit competitie",
            "binnen een soort is er nooit competitie",
            "tussen soorten gaat het altijd om nestplaatsen",
        ],
        antwoord=0,
        uitleg="Soortgenoten eten hetzelfde, nestelen op dezelfde plaats en zoeken dezelfde partner. Hun behoeften overlappen dus volledig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij symbiose hebben beide organismen voordeel bij hun samenleven.",
        antwoord=True,
        uitleg="Bij mutualistische symbiose winnen beide. Een bij die nectar haalt en daarbij stuifmeel verplaatst, is het schoolvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden zijn een vorm van symbiose waar beide voordeel bij hebben? Kruis alles aan wat juist is.",
        opties=[
            "een bij en een bloem",
            "een korstmos, waarin een alg en een schimmel samenleven",
            "de bacteriën in onze darm en wij",
            "een lintworm en zijn gastheer",
        ],
        antwoord=[0, 1, 2],
        uitleg="In die drie winnen beide partijen. Een lintworm leeft op kosten van zijn gastheer en is dus een parasiet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een organisme dat op of in een ander leeft en het schade toebrengt zonder het meteen te doden?",
        antwoord=["parasiet", "een parasiet", "parasieten"],
        uitleg="Een parasiet heeft er belang bij dat zijn gastheer blijft leven, want die is zijn voeding en zijn woonplaats. Een teek en een lintworm zijn parasieten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom doodt een parasiet zijn gastheer meestal niet?",
        opties=[
            "een dode gastheer levert geen voeding meer",
            "een parasiet is te klein om schade te doen",
            "de gastheer kan zich altijd verweren",
            "een parasiet eet geen levend materiaal",
        ],
        antwoord=0,
        uitleg="Een parasiet die zijn gastheer snel doodt, verliest zijn eigen bestaan. Daarom blijft de schade meestal beperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is commensalisme?",
        opties=[
            "de een heeft voordeel, de ander ondervindt niets",
            "beide organismen hebben voordeel bij het samenleven",
            "beide organismen ondervinden er nadeel van",
            "het ene organisme doodt en eet het andere op",
        ],
        antwoord=0,
        uitleg="Een zeepok op de huid van een walvis reist mee en de walvis merkt het niet. De een wint, de ander blijft onverschillig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eikel die door een gaai weggedragen wordt en elders ontspruit, toont dat een interactie voor beide partijen goed kan uitvallen.",
        antwoord=True,
        uitleg="De gaai krijgt voedsel en een voorraad, en de eik krijgt haar zaad ver van de moederboom. Beide hebben er dus baat bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voordeel heeft het leven in een groep voor een dier? Kruis alles aan wat juist is.",
        opties=[
            "meer ogen zien een roofdier sneller aankomen",
            "samen jagen levert grotere prooien op",
            "de jongen kunnen samen beschermd worden",
            "elk individu vindt meer voedsel voor zichzelf alleen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Veiligheid, samen jagen en zorg voor de jongen zijn de voordelen. Het nadeel is net dat je het voedsel moet delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nadeel van in een grote groep leven?",
        opties=[
            "er is meer competitie om voedsel en ziekten verspreiden zich sneller",
            "een roofdier vindt de groep moeilijker terug",
            "de jongen worden minder goed beschermd",
            "er is minder gelegenheid om een partner te vinden",
        ],
        antwoord=0,
        uitleg="Een groep is opvallender voor een roofdier, verbruikt het voedsel sneller en geeft ziekten makkelijk door. Daarom is er altijd een evenwicht tussen voor- en nadeel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de rangorde in een groep dieren, waarbij het ene dier voorrang heeft op het andere?",
        antwoord=["hiërarchie", "rangorde", "een hiërarchie"],
        uitleg="Een vaste rangorde spaart gevechten uit, want de uitkomst is al bekend. Daarom vecht een wolvenroedel of een kippenhok niet elke dag opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verdedigt een dier een territorium?",
        opties=[
            "om voedsel, dekking en een nestplaats te houden",
            "om zijn groep zo groot mogelijk te maken",
            "om soortgenoten te leren wat ze mogen eten",
            "om zijn dagritme op dat van de buren af te stemmen",
        ],
        antwoord=0,
        uitleg="Een territorium zijn de hulpbronnen van dat dier. Door het af te bakenen met zang of geur hoeft het niet telkens te vechten.",
    ),
    dict(
        type="waarofniet",
        vraag="Communicatie tussen dieren verloopt enkel met geluid.",
        antwoord=False,
        uitleg="Ook geur en beweging dragen een boodschap. Een hond ruikt wie er voorbijkwam en een bij danst de richting van het voedsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een feromoon?",
        opties=[
            "een geurstof waarmee soortgenoten elkaar iets doorgeven",
            "een hormoon dat het bloedglucosegehalte regelt",
            "een geluid dat enkel soortgenoten kunnen horen",
            "een kleurstof die een dier in het broedseizoen aanmaakt",
        ],
        antwoord=0,
        uitleg="Mieren leggen een spoor met feromonen en motten vinden er een partner mee. De boodschap gaat door de lucht of over de grond.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee soorten die precies hetzelfde eten op dezelfde plaats, kunnen op lange termijn moeilijk naast elkaar blijven bestaan.",
        antwoord=True,
        uitleg="Volledige overlap geeft volledige competitie, en dan verdringt de een de ander. Meestal verschuift er iets, zodat elk zijn eigen hoekje heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vogelsoorten eten insecten in dezelfde bomen, maar de ene zoekt in de kruin en de andere op de stam. Wat besluit je?",
        opties=[
            "door het verschil in zoekplaats blijft de competitie beperkt",
            "er is geen enkele competitie, want ze eten iets anders",
            "de ene soort zal de andere zeker verdringen",
            "ze vormen samen een symbiose",
        ],
        antwoord=0,
        uitleg="Ze eten hetzelfde maar niet op dezelfde plek. Zo'n opdeling verkleint de overlap en laat beide soorten naast elkaar leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een roofdierpopulatie als het aantal prooien sterk stijgt?",
        opties=[
            "de roofdieren nemen met wat vertraging ook toe, waarna de prooien weer dalen",
            "de roofdieren verdwijnen, want er is te veel keuze",
            "er verandert niets, want roofdieren hangen niet van prooien af",
            "de prooien blijven voor altijd in groot aantal",
        ],
        antwoord=0,
        uitleg="Veel voedsel geeft meer jongen bij de jagers, en die eten dan de prooien weer weg. Daardoor schommelen beide aantallen om elkaar heen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een roofdier dat uit een gebied verdwijnt, laat de rest van het ecosysteem onberoerd.",
        antwoord=False,
        uitleg="Zonder jager groeit de prooipopulatie, die dan haar voedselplanten kaalvreet. Zo werkt het effect door tot ver in het ecosysteem.",
    ),
]

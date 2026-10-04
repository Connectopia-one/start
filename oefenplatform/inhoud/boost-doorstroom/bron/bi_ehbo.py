# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Levensreddend handelen.

Eigen kop van de vakfiche biologie 2de graad doorstroomfinaliteit, die 5 %
van het examen weegt. In de fiche natuurwetenschappen staat dit onderdeel
niet als apart examengedeelte.

Deel 1 gaat over de eerste stappen bij een slachtoffer, over reanimatie en
over de automatische externe defibrillator. Deel 2 gaat over de andere
noodsituaties: bloedingen, brandwonden, verstikking, shock, botbreuken en
wat je vooral niet doet.

De richtlijnen volgen die van het Rode Kruis. Dit zijn vragen om de theorie
in te oefenen; echt leren reanimeren gebeurt op een cursus met een pop.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat doe je als eerste bij een ongeval?",
        opties=[
            "kijken of de plaats veilig is",
            "meteen beginnen met hartmassage",
            "het slachtoffer zo snel mogelijk verplaatsen",
            "het slachtoffer iets te drinken geven",
        ],
        antwoord=0,
        uitleg="Een tweede slachtoffer helpt niemand. Eerst de eigen veiligheid, dan die van het slachtoffer, dan de hulp.",
    ),
    dict(
        type="invultekst",
        vraag="Welk noodnummer bel je in België voor een ziekenwagen?",
        antwoord=["112", "1 1 2"],
        uitleg="112 is het Europese noodnummer voor ziekenwagen en brandweer. Voor de politie alleen bestaat ook 101.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vertel je zeker als je 112 belt? Kruis alles aan wat juist is.",
        opties=[
            "waar je precies bent",
            "wat er gebeurd is",
            "hoeveel slachtoffers er zijn en in welke toestand",
            "wie er volgens jou schuld aan heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Plaats, aard van het ongeval en toestand van de slachtoffers: daarmee kan de centralist de juiste hulp sturen. Wie schuld heeft, doet er dan niet toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je na of iemand bij bewustzijn is?",
        opties=[
            "je spreekt de persoon aan en schudt zacht",
            "je voelt meteen de hartslag in de hals",
            "je houdt een spiegel voor de mond",
            "je tilt de persoon rechtop",
        ],
        antwoord=0,
        uitleg="Aanspreken en zacht aanschudden is de eenvoudigste test. Reageert er niets, dan is de persoon niet bij bewustzijn en roep je hulp.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een slachtoffer dat niet reageert, kijk je daarna of het normaal ademt.",
        antwoord=True,
        uitleg="Je kantelt het hoofd lichtjes achterover, kijkt naar de borstkas en voelt of je adem op je wang voelt. Daarvoor neem je tien seconden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand is niet bij bewustzijn maar ademt normaal. Wat doe je?",
        opties=[
            "je legt de persoon in stabiele zijligging en belt 112",
            "je begint met hartmassage",
            "je zet de persoon rechtop tegen een muur",
            "je geeft de persoon water om bij te komen",
        ],
        antwoord=0,
        uitleg="In zijligging blijven de luchtwegen vrij en kan braaksel naar buiten lopen. Hartmassage is hier niet nodig, want het hart werkt nog.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de houding waarin je een bewusteloos slachtoffer legt dat normaal ademt?",
        antwoord=["stabiele zijligging", "zijligging", "de stabiele zijligging"],
        uitleg="Op de zij, met het hoofd lichtjes achterover en de mond naar beneden. Zo kan de tong de luchtweg niet afsluiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legt men een bewusteloos slachtoffer op de zij en niet op de rug?",
        opties=[
            "op de rug kan de tong of braaksel de luchtweg afsluiten",
            "op de zij komt het bloed sneller naar het hoofd",
            "op de rug wordt het slachtoffer sneller koud",
            "op de zij kan het slachtoffer makkelijker praten",
        ],
        antwoord=0,
        uitleg="Bij bewusteloosheid verslappen de spieren van de mond en de keel. Op de zij loopt alles naar buiten in plaats van naar de longen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer start je met reanimeren?",
        opties=[
            "als het slachtoffer niet reageert en niet normaal ademt",
            "als het slachtoffer niet reageert maar nog normaal ademt",
            "als het slachtoffer pijn in de borst heeft",
            "als het slachtoffer veel bloed verliest",
        ],
        antwoord=0,
        uitleg="Niet reageren én niet normaal ademen betekent dat het hart het bloed niet meer rondstuwt. Dan is reanimatie nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel borstcompressies geef je per reeks, voor je twee beademingen geeft?",
        antwoord=["30", "dertig"],
        uitleg="Bij een volwassene is het ritme telkens 30 compressies en 2 beademingen. Dat houd je aan tot er hulp komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe snel geef je borstcompressies bij een volwassene?",
        opties=[
            "ongeveer 100 tot 120 keer per minuut",
            "ongeveer 30 tot 40 keer per minuut",
            "ongeveer 200 tot 250 keer per minuut",
            "zo langzaam als je zelf kan volhouden",
        ],
        antwoord=0,
        uitleg="Dat is ongeveer twee keer per seconde. Het ritme van een stevig marcherend lied helpt om het tempo aan te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar leg je je handen bij een borstcompressie?",
        opties=[
            "midden op het borstbeen",
            "op de linkerkant van de borstkas",
            "onder aan de buik",
            "op de ribben aan de zijkant",
        ],
        antwoord=0,
        uitleg="Je legt de hiel van je hand midden op het borstbeen en je andere hand erbovenop. Met gestrekte armen duw je recht naar beneden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een borstcompressie duw je het borstbeen van een volwassene ongeveer één centimeter in.",
        antwoord=False,
        uitleg="Dat is veel te weinig om bloed te stuwen; het moet ongeveer vijf centimeter zijn. Je laat de borstkas daarna wel volledig terugkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je onderbreekt de hartmassage best zo vaak mogelijk om de toestand van het slachtoffer te controleren.",
        antwoord=False,
        uitleg="Elke onderbreking laat de bloeddruk wegzakken. Je gaat door tot de hulpdiensten er zijn of tot het slachtoffer weer normaal ademt.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de afkorting AED?",
        antwoord=["automatische externe defibrillator", "automatische externe defibrillatie"],
        uitleg="Zo'n toestel analyseert het hartritme en geeft indien nodig een stroomstoot. Het zegt zelf stap voor stap wat je moet doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een AED?",
        opties=[
            "hij meet het hartritme en geeft enkel een schok als dat nodig is",
            "hij geeft altijd een schok zodra je hem aanzet",
            "hij vervangt de hartmassage volledig",
            "hij beademt het slachtoffer automatisch",
        ],
        antwoord=0,
        uitleg="Het toestel beslist zelf. Daardoor kan ook iemand zonder opleiding er geen schade mee doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Iemand zonder opleiding mag een AED gebruiken.",
        antwoord=True,
        uitleg="De AED spreekt je stap voor stap toe en geeft geen schok als die niet nodig is. Hem niet gebruiken is het grootste risico.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het gebruik van een AED? Kruis alles aan wat juist is.",
        opties=[
            "het toestel aanzetten en de aanwijzingen volgen",
            "de elektroden op de ontblote borstkas kleven",
            "niemand aanraken op het ogenblik van de schok",
            "eerst de hartmassage een paar minuten staken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aanzetten, kleven en afstand houden bij de schok. De hartmassage gaat juist door tot het toestel vraagt om los te laten.",
    ),
    dict(
        type="waarofniet",
        vraag="Reanimeren verhoogt de kans om een hartstilstand te overleven aanzienlijk.",
        antwoord=True,
        uitleg="Elke minuut zonder hulp verkleint de kans sterk. Beginnen is dus altijd beter dan wachten, ook als je het niet perfect doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt iemand op straat die niet reageert en niet normaal ademt, en je staat er alleen voor. Wat doe je?",
        opties=[
            "je belt 112 met de luidspreker aan en begint te reanimeren",
            "je gaat eerst hulp zoeken in de huizen in de buurt",
            "je legt de persoon in stabiele zijligging en wacht af",
            "je brengt de persoon zelf naar het ziekenhuis",
        ],
        antwoord=0,
        uitleg="Alarm en reanimatie moeten samengaan, en een gsm op luidspreker maakt dat mogelijk. Zo verlies je geen tijd.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een hevige bloeding aan een arm?",
        opties=[
            "je drukt met een propere doek stevig op de wonde",
            "je bindt de arm zo stevig af dat er geen bloed meer door kan",
            "je wast de wonde eerst grondig met zeep uit",
            "je laat de wonde open om ze te laten drogen",
        ],
        antwoord=0,
        uitleg="Rechtstreekse druk op de wonde stopt de bloeding het best. Een afbindend verband wordt niet meer aangeraden, want dat snijdt alle doorbloeding af.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een bloeding houd je het gekwetste lichaamsdeel bij voorkeur hoger dan het hart.",
        antwoord=True,
        uitleg="Door de hoogte neemt de druk in het bloedvat af. Samen met de druk op de wonde stopt de bloeding sneller.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe lang koel je een brandwond met lauw stromend water?",
        antwoord=["20 minuten", "twintig minuten", "20 min"],
        uitleg="Water eerst, de rest komt later. Twintig minuten lauw stromend water beperkt de schade in de diepte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je niet bij een brandwond?",
        opties=[
            "er boter, tandpasta of zalf op doen",
            "er lauw stromend water over laten lopen",
            "sieraden in de buurt van de wonde afdoen",
            "de wonde daarna losjes bedekken",
        ],
        antwoord=0,
        uitleg="Vette stoffen houden de warmte juist vast en maken het nazicht moeilijker. Enkel water koelt echt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een blaar bij een brandwond prik je best zelf open.",
        antwoord=False,
        uitleg="De blaar is een steriel dekseltje over de wonde. Opengeprikt komt er een poort voor infectie vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verslikt zich en kan nog krachtig hoesten. Wat doe je?",
        opties=[
            "je laat de persoon doorhoesten en blijft erbij",
            "je geeft meteen vijf slagen tussen de schouderbladen",
            "je geeft meteen buikstoten",
            "je legt de persoon in stabiele zijligging",
        ],
        antwoord=0,
        uitleg="Hoesten is de krachtigste manier om een voorwerp eruit te krijgen. Je grijpt pas in als het hoesten niet meer lukt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verslikt zich en kan niet meer hoesten of spreken. Wat doe je?",
        opties=[
            "je geeft vijf slagen tussen de schouderbladen en daarna vijf buikstoten",
            "je geeft de persoon water om door te slikken",
            "je legt de persoon op de rug en begint te beademen",
            "je wacht tot de persoon zelf weer begint te hoesten",
        ],
        antwoord=0,
        uitleg="Afwisselend slaan en stoten tot het voorwerp eruit komt. Raakt de persoon buiten bewustzijn, dan start je met reanimeren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel slagen tussen de schouderbladen geef je bij een volledige verstikking, voor je overgaat op buikstoten?",
        antwoord=["vijf", "5"],
        uitleg="Vijf slagen met de hiel van je hand, tussen de schouderbladen, terwijl de persoon voorover leunt. Lukt het niet, dan volgen vijf buikstoten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke tekens kunnen op shock wijzen? Kruis alles aan wat juist is.",
        opties=[
            "een bleke, klamme huid",
            "een snelle en zwakke pols",
            "onrust, dorst of verwardheid",
            "een trage en diepe ademhaling",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij shock stuwt het hart te weinig bloed rond. Het lichaam spaart de huid uit voor de organen, en dat zie je aan de bleekheid. De ademhaling wordt juist snel en oppervlakkig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een slachtoffer in shock geef je best iets te drinken.",
        antwoord=False,
        uitleg="Het slachtoffer kan zich verslikken en moet misschien dringend geopereerd worden. Je houdt het warm en belt 112.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een vermoedelijke botbreuk in een arm?",
        opties=[
            "je laat de arm zo liggen als hij ligt, steunt hem en belt hulp",
            "je trekt het bot weer recht",
            "je laat de persoon de arm bewegen om te zien hoe erg het is",
            "je bindt de arm zo stevig mogelijk af",
        ],
        antwoord=0,
        uitleg="Rechttrekken kan zenuwen en bloedvaten beschadigen. Je beperkt de beweging en laat de rest aan de hulpdiensten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vermoeden van een nek- of rugwonde laat je het slachtoffer liggen zoals het ligt, tenzij er onmiddellijk gevaar is.",
        antwoord=True,
        uitleg="Verplaatsen kan het ruggemerg beschadigen en blijvende verlamming geven. Enkel acuut gevaar, zoals brand, weegt daar tegen op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand krijgt een epileptische aanval met schokken. Wat doe je?",
        opties=[
            "je zorgt dat de persoon zich niet kan stoten en legt iets zachts onder het hoofd",
            "je houdt de persoon stevig vast tot de schokken stoppen",
            "je steekt iets tussen de tanden",
            "je geeft de persoon meteen iets te drinken",
        ],
        antwoord=0,
        uitleg="Tegenhouden kan kwetsuren geven en iets tussen de tanden steken is gevaarlijk. Na de aanval leg je de persoon in zijligging.",
    ),
    dict(
        type="invultekst",
        vraag="Welk lichaamsdeel koel je bij een hittestuwing of een hitteslag niet met ijs, maar met lauw water?",
        antwoord=["de huid", "huid", "het hele lichaam"],
        uitleg="IJs trekt de bloedvaten in de huid samen, en dan kan de warmte er niet meer uit. Lauw water en wind koelen beter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand klaagt over drukkende pijn in de borst die naar de arm uitstraalt. Wat doe je?",
        opties=[
            "je belt 112, laat de persoon stil zitten en blijft erbij",
            "je laat de persoon wat wandelen om het bloed te doen stromen",
            "je wacht een uur om te zien of de pijn weggaat",
            "je geeft de persoon een koud bad",
        ],
        antwoord=0,
        uitleg="Dat kan een hartinfarct zijn, en dan telt elke minuut. Rust beperkt de belasting van het hart tot de hulp er is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een slachtoffer dat weer normaal begint te ademen tijdens de reanimatie, leg je in stabiele zijligging.",
        antwoord=True,
        uitleg="Dan werkt het hart weer en is massage niet meer nodig. Je blijft wel kijken of de ademhaling normaal blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een eenvoudige verbanddoos? Kruis alles aan wat juist is.",
        opties=[
            "steriele compressen",
            "een rol kleefpleister en een zwachtel",
            "wegwerphandschoenen",
            "een flesje alcohol om wonden uit te spoelen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Compressen, verband en handschoenen zijn het nuttigst. Een wonde spoel je met water, niet met alcohol, want dat beschadigt het weefsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Wegwerphandschoenen beschermen enkel het slachtoffer en niet de helper.",
        antwoord=False,
        uitleg="Ze houden ziekteverwekkers in beide richtingen tegen, dus beschermen ze beide. Zitten er geen in de doos, dan gebruik je iets anders als tussenlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig dat zoveel mensen mogelijk kunnen reanimeren?",
        opties=[
            "de eerste minuten bepalen de kans om te overleven, en de hulpdiensten zijn er niet meteen",
            "de hulpdiensten komen dan niet meer ter plaatse",
            "reanimeren vervangt het ziekenhuis",
            "zo hoeft er geen AED meer in gebouwen te hangen",
        ],
        antwoord=0,
        uitleg="Zonder bloedtoevoer raken de hersenen in minuten beschadigd. Een omstaander overbrugt net die kostbare eerste minuten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongeval op de autosnelweg. Wat doe je eerst?",
        opties=[
            "je zorgt voor je eigen veiligheid: stilstaan op een veilige plek, een hesje aan, de knipperlichten aan",
            "je loopt onmiddellijk naar de voertuigen toe",
            "je zet je wagen dwars over de rijstrook",
            "je haalt de slachtoffers meteen uit hun auto",
        ],
        antwoord=0,
        uitleg="Een helper die zelf aangereden wordt, maakt de toestand erger. Eigen veiligheid staat altijd eerst, ook als dat tijd kost.",
    ),
]

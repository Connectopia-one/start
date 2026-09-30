# -*- coding: utf-8 -*-
"""De vragen voor "Verbinden, afwerken en veilig werken" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom: het stuk "Verbindingen" en het stuk
"Gereedschappen, afwerking en persoonlijke beschermingsmiddelen" van het
constructiesysteem, samen met het onderdeel "Veiligheid" (leerdoel 06.39, veilig
en duurzaam werken met materialen, stoffen, organismen en technische systemen).

Deel 1 gaat over de verbindingen en de verbindingsproducten van de fiche, over
het kiezen van de juiste lijm, en over de afwerkingstechnieken.
Deel 2 gaat over gereedschap en machines, de persoonlijke beschermingsmiddelen
met hun pictogrammen, de veiligheidsinstructiekaart, en de goede en slechte
werkwijzen die de fiche opsomt.

De voorbeelden van de veiligheidsinstructiekaart komen uit bijlage 1 van de
fiche zelf, de kaart van de figuurzaag. Zo staat er niets in wat een kind niet
in zijn eigen vakfiche kan terugvinden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn soorten verbindingen?",
        opties=[
            "Een boutverbinding",
            "Een lasverbinding",
            "Een lijmverbinding",
            "Een beitsverbinding",
            "Een schuurverbinding",
        ],
        antwoord=[0, 1, 2],
        uitleg="Beitsen en schuren zijn afwerkingstechnieken, geen manieren om twee stukken aan elkaar te zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heb je nodig voor een boutverbinding?",
        opties=[
            "Een bout en een moer",
            "Een bout en wat houtlijm",
            "Een moer en een lange nagel",
            "Een bout en een stevige spijker",
        ],
        antwoord=0,
        uitleg="De bout gaat door beide stukken en de moer draai je er aan de andere kant op. Daarom heet het een bout- en moerverbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lasverbinding kan je makkelijk weer losmaken.",
        antwoord=False,
        uitleg="Bij lassen smelt het metaal aan elkaar. Dat krijg je er alleen nog uit door het weg te slijpen of door te zagen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verbinding kan je weer losmaken zonder iets kapot te maken?",
        opties=[
            "Een bout- en moerverbinding",
            "Een lasverbinding met een lasapparaat",
            "Een lijmverbinding met houtlijm",
            "Een soldeerverbinding met tin",
        ],
        antwoord=0,
        uitleg="Je draait de moer er gewoon weer af. Lassen, lijmen en solderen zijn bedoeld om te blijven zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een verstekverbinding?",
        opties=[
            "Twee stukken die schuin afgezaagd tegen elkaar komen",
            "Twee stukken die met een houten pin verbonden worden",
            "Twee stukken die met een laag lijm op elkaar komen",
            "Twee stukken metaal die aan elkaar gelast worden",
        ],
        antwoord=0,
        uitleg="Bij verstek zaag je allebei de stukken onder dezelfde hoek af, meestal 45 graden. Zo zie je in de hoek van een kader geen kopse kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een deuvelverbinding?",
        opties=[
            "Twee stukken hout die met houten pinnetjes vastzitten",
            "Twee metalen stukken die aan elkaar gelast zijn",
            "Twee stukken die met klittenband vastgemaakt zijn",
            "Twee draden die met gesmolten tin verbonden zijn",
        ],
        antwoord=0,
        uitleg="Een deuvel is een rond houten pennetje. Je boort in beide stukken een gat, lijmt de deuvel erin en drukt de stukken samen.",
    ),
    dict(
        type="invultekst",
        vraag="Twee draden aan elkaar zetten met gesmolten tin heet een ___.",
        antwoord="soldeerverbinding",
        uitleg="Solderen doe je met een soldeerbout en soldeertin. Het tin smelt, loopt rond de draden en houdt ze vast als het weer hard wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Velcro of klittenband is een verbinding die je telkens weer kunt openen.",
        antwoord=True,
        uitleg="De haakjes van de ene kant grijpen in de lusjes van de andere. Je kunt het duizenden keren open- en dichtmaken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een scharnier?",
        opties=[
            "Om een deel te laten draaien",
            "Om twee delen voorgoed vast te zetten",
            "Om een gat in een plank te boren",
            "Om een oppervlak glad te schuren",
        ],
        antwoord=0,
        uitleg="Een scharnier houdt twee delen vast en laat er toch één van bewegen. Zo werkt elke deur en elk deksel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar let je op als je een lijmsoort kiest?",
        opties=[
            "Welke materialen je aan elkaar lijmt",
            "Of de verbinding nat kan worden",
            "Hoeveel tijd je hebt om nog te schikken",
            "Welke kleur de verpakking van de lijm heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Op de verpakking van een lijm staat voor welke materialen ze dient, of ze watervast is en hoe lang de verwerkingstijd is. Dat is de productinformatie waar de fiche naar vraagt.",
    ),
    dict(
        type="waarofniet",
        vraag="De verwerkingstijd van een lijm zegt hoe lang je de stukken nog kunt verschuiven.",
        antwoord=True,
        uitleg="Daarna begint de lijm te binden en zit je vast aan de stand waarin de stukken staan. Bij snelle lijm is dat maar een paar seconden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke afwerkingstechniek maakt hout glad voor je het schildert?",
        opties=["Schuren", "Beitsen", "Lassen", "Solderen"],
        antwoord=0,
        uitleg="Schuurpapier haalt de oneffenheden weg. Zonder schuren zie je elke bult straks door de verf heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn afwerkingstechnieken?",
        opties=["Lakken", "Vernissen", "Oliën", "Boren", "Zagen"],
        antwoord=[0, 1, 2],
        uitleg="Afwerken doe je nadat het werkstuk gemaakt is: beitsen, lakken, verven, vernissen, oliën en schuren. Boren en zagen horen bij het maken zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Beitsen legt een dekkende laag over het hout zodat je de nerf niet meer ziet.",
        antwoord=False,
        uitleg="Beits trekt juist ín het hout, dus je blijft de nerf zien. Een laag die alles bedekt, krijg je met dekkende verf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt hout gevernist of gelakt?",
        opties=[
            "Om het te beschermen tegen vocht en slijtage",
            "Om het een flink stuk lichter te maken",
            "Om het beter stroom te laten geleiden",
            "Om het magnetisch te maken voor een magneet",
        ],
        antwoord=0,
        uitleg="Er komt een laagje op dat water en vuil tegenhoudt. Een tafelblad zonder afwerking zou bij de eerste gemorste drank vlekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk verbindingsproduct zet je twee houten planken aan elkaar zonder lijm?",
        opties=[
            "Met schroeven",
            "Met soldeertin",
            "Met klittenband",
            "Met een magneet",
        ],
        antwoord=0,
        uitleg="Schroeven bijten zich in het hout vast. Soldeertin werkt alleen op metaal, en een magneet doet niets met hout.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet kan als verbinding gebruikt worden.",
        antwoord=True,
        uitleg="De fiche noemt magneten uitdrukkelijk bij de verbindingsmogelijkheden. Denk aan een kastdeurtje dat magnetisch dichtklikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kies je een schroef in plaats van een nagel als je later nog uit elkaar wilt halen?",
        opties=[
            "Een schroef kan je er weer uitdraaien",
            "Een schroef is altijd goedkoper dan een nagel",
            "Een schroef kan helemaal niet gaan roesten",
            "Een schroef is veel sneller aangebracht",
        ],
        antwoord=0,
        uitleg="Een nagel krijg je er alleen uit door hem eruit te trekken, en dan beschadig je het hout. Een schroef draait er zo weer uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ritssluiting is geen verbinding.",
        antwoord=False,
        uitleg="Een ritssluiting staat gewoon in het rijtje verbindingsmogelijkheden van de fiche, naast velcro, scharnieren en magneten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een profiel in een constructie?",
        opties=[
            "Het verbindt delen en maakt het geheel stijver",
            "Het geeft de constructie een mooiere kleur en vorm",
            "Het maakt de constructie een flink stuk zwaarder",
            "Het meet de lengte van alle delen bij elkaar op",
        ],
        antwoord=0,
        uitleg="Een profiel is een staaf met altijd dezelfde doorsnede, bijvoorbeeld een L of een U. Je zet er delen mee aan elkaar en het maakt het geheel stijver.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn persoonlijke beschermingsmiddelen?",
        opties=[
            "Gehoorbescherming",
            "Veiligheidsschoenen",
            "Een mondmasker",
            "Een boormachine",
            "Een meetlat van een meter",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een persoonlijk beschermingsmiddel draag je zelf. Een boormachine en een meetlat zijn gereedschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram met een oorbeschermer?",
        opties=[
            "Gehoorbescherming verplicht",
            "Geluid maken is hier verboden",
            "Stilte houden in het hele lokaal",
            "Muziek beluisteren is toegelaten",
        ],
        antwoord=0,
        uitleg="De blauwe pictogrammen met een persoon erop zijn geboden: iets is verplicht. Dit is er een van de negen uit bijlage 1.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met een bril betekent dat een veiligheidsbril verplicht is.",
        antwoord=True,
        uitleg="Het staat in de reeks verplichte beschermingsmiddelen, samen met de helm, de handschoenen, de schoenen en het masker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bescherming draag je bij het boren in steen?",
        opties=[
            "Een veiligheidsbril",
            "Een paar handschoenen van dun stof",
            "Een schort van dik papier",
            "Een pet met een klep vooraan",
        ],
        antwoord=0,
        uitleg="Bij boren springen er stukjes weg, recht naar je gezicht. Een bril houdt die tegen. Vaak draag je er ook een stofmasker bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bescherming draag je in een lawaaierige werkplaats?",
        opties=[
            "Gehoorbescherming",
            "Een veiligheidsbril",
            "Veiligheidsschoenen",
            "Een stofmasker",
        ],
        antwoord=0,
        uitleg="Lawaai beschadigt je gehoor voorgoed, en je merkt het pas jaren later. Daarom is gehoorbescherming bij machines verplicht.",
    ),
    dict(
        type="invultekst",
        vraag="De drie letters die staan voor persoonlijke beschermingsmiddelen zijn ___.",
        antwoord="PBM",
        uitleg="PBM is de afkorting die je op werkbladen en instructiekaarten tegenkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op een veiligheidsinstructiekaart?",
        opties=[
            "De risico's van een machine en hoe je ze voorkomt",
            "De prijs en de leverancier van de machine",
            "De maten van de werkstukken die je gaat maken",
            "De namen van wie de machine mag aankopen",
        ],
        antwoord=0,
        uitleg="Links de risico's, rechts de voorkomingsmaatregelen, en de pictogrammen van wat verplicht is. De kaart van de figuurzaag staat als voorbeeld in de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor je een machine voor het eerst gebruikt, lees je de handleiding.",
        antwoord=True,
        uitleg="Dat staat als eerste punt op de veiligheidsinstructiekaart. Je weet dan wat de machine kan en wat er misloopt als je iets verkeerd doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn veilig?",
        opties=[
            "Gemorste producten meteen opkuisen",
            "De stekker uittrekken voor je iets aan de machine doet",
            "Lang haar samenbinden voor je begint",
            "Een elektrisch toestel bedienen met natte handen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie staan als goede werkwijze in de fiche. Natte handen en elektriciteit gaan nooit samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een elektrisch toestel bedienen met natte handen zolang je snel werkt.",
        antwoord=False,
        uitleg="Water geleidt stroom. Met natte handen loopt er veel makkelijker stroom door je lichaam, hoe kort je er ook aan komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bind je lang haar samen bij het werken met een machine?",
        opties=[
            "Het kan meegetrokken worden door draaiende delen",
            "Het staat een stuk netter op een werkplaats",
            "Het houdt je hoofd koeler tijdens het werken",
            "Het maakt de machine een heel stuk stiller",
        ],
        antwoord=0,
        uitleg="Een boor of een zaagblad dat draait, grijpt haar in een oogwenk mee. Om dezelfde reden draag je geen ringen, juwelen of losse kledij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met een meetinstrument als je klaar bent met meten?",
        opties=[
            "Je schakelt het uit",
            "Je laat het aanstaan tot de volgende dag",
            "Je legt het in een bak met water",
            "Je zet het op de allerhoogste stand",
        ],
        antwoord=0,
        uitleg="Uitschakelen spaart de batterij en beschermt het toestel. De fiche noemt het bij de goede werkwijzen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het meetbereik van een meetinstrument mag je overschrijden als het maar even duurt.",
        antwoord=False,
        uitleg="Buiten het meetbereik klopt de meting niet meer, en je kunt het toestel stukmaken. Respecteer het bereik en de nauwkeurigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je gereedschap onderhouden?",
        opties=[
            "Het blijft dan veilig en nauwkeurig werken",
            "Het wordt er een flink stuk zwaarder van",
            "Het gaat er veel mooier van blinken",
            "Het verbruikt dan minder stroom per uur",
        ],
        antwoord=0,
        uitleg="Een bot zaagblad of een losse steel is gevaarlijk. In de onderhoudsvoorschriften staat wat je wanneer moet nakijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gereedschap gebruik je om een gat in hout te maken?",
        opties=["Een boormachine", "Een verfborstel", "Een sleuteltang", "Een hamer"],
        antwoord=0,
        uitleg="Een boormachine met een houtboor. Een hamer maakt een gat in de plank, maar geen net gat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hamer, een schroevendraaier en een verfborstel zijn handgereedschap.",
        antwoord=True,
        uitleg="Handgereedschap beweegt door jouw eigen kracht. Een boormachine en een zaagmachine hebben een motor: dat zijn machines.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen handgereedschap en een machine?",
        opties=[
            "Een machine werkt met een motor of een aandrijving",
            "Een machine is altijd groter dan handgereedschap",
            "Handgereedschap is altijd goedkoper in de winkel",
            "Handgereedschap is altijd van hout gemaakt",
        ],
        antwoord=0,
        uitleg="Bij handgereedschap lever jij de kracht, bij een machine doet de motor dat. Daarom is een machine ook gevaarlijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen staan op de veiligheidsinstructiekaart van een figuurzaag?",
        opties=[
            "Draag oogbescherming",
            "Gebruik de stofafzuiging",
            "Draag aangepaste gehoorbescherming",
            "Draag helemaal geen bescherming",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die kaart staat als voorbeeld in de fiche. Er staat ook op dat je de stofafzuiging aanzet vóór je de machine start.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag ringen en juwelen dragen terwijl je aan een zaagmachine werkt.",
        antwoord=False,
        uitleg="Op de veiligheidsinstructiekaart staat uitdrukkelijk geen ringen of juwelen. Ze kunnen aan een draaiend deel blijven haken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je eerst voor je aan een machine gaat sleutelen?",
        opties=[
            "De stekker uittrekken",
            "De machine nog even kort aanzetten",
            "Het snoer over de werktafel leggen",
            "De beschermkap eraf halen en wegleggen",
        ],
        antwoord=0,
        uitleg="Zolang de stekker in het stopcontact zit, kan de machine per ongeluk starten. Uittrekken is het eerste wat je doet.",
    ),
]

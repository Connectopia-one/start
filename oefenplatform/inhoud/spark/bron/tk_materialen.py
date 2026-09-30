# -*- coding: utf-8 -*-
"""De vragen voor "Materialen en grondstoffen" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Materialen en grondstoffen"
(7,5 % van het examen).

Deel 1 gaat over de indeling: grondstof, materiaal en product, enkelvoudige
metalen en legeringen, metalen en niet-metalen, ferro en non-ferro, natuurlijk
en kunstmatig, met de proeven waarmee je die groepen uit elkaar houdt.
Deel 2 gaat over de eigenschappen (elektrisch, fysisch, magnetisch, mechanisch,
technologisch), de eenvoudige onderzoekstechnieken uit de fiche, het kiezen van
een materiaal bij een eis, en de veiligheidspictogrammen van bijlage 1.

Twee dingen die de fiche uit elkaar houdt en waar hier apart naar gevraagd
wordt: de geleidingsproef zegt of iets een metaal is, de magneetproef zegt of
een metaal een ferrometaal is. Die twee worden voortdurend verwisseld.

Nergens wordt naar een pictogram gevraagd dat je moet zien: bij de oefeningen
staat geen afbeelding, dus elke vraag noemt het gevaar of de betekenis in
woorden. De pictogrammen zelf staan getekend in de leerbundel.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="IJzererts, klei, zand, wol en aardolie horen allemaal bij dezelfde groep. Welke?",
        opties=[
            "De grondstoffen",
            "De legeringen die in een fabriek gemaakt worden",
            "De kunstmatige materialen uit de scheikunde",
            "De afgewerkte producten die in de winkel liggen",
        ],
        antwoord=0,
        uitleg="Een grondstof haal je uit de natuur. Daar maak je een materiaal van, en van dat materiaal een product: van ijzererts maak je staal, en van staal een spijker.",
    ),
    dict(
        type="waarofniet",
        vraag="Staal is een grondstof.",
        antwoord=False,
        uitleg="Staal is een materiaal. De grondstof waar het uit gemaakt wordt, is ijzererts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn legeringen?",
        opties=["Brons", "Messing", "Inox", "Koper", "Aluminium"],
        antwoord=[0, 1, 2],
        uitleg="Brons, messing en inox zijn mengsels van metalen, dus legeringen. Koper en aluminium zijn enkelvoudige metalen: die bestaan uit één metaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een enkelvoudig metaal en een legering?",
        opties=[
            "Een legering is een mengsel van metalen",
            "Een legering roest nooit en een enkelvoudig metaal altijd",
            "Een legering komt in de natuur voor en een enkelvoudig metaal niet",
            "Een legering geleidt geen stroom en een enkelvoudig metaal wel",
        ],
        antwoord=0,
        uitleg="Een enkelvoudig metaal bestaat uit één metaal, zoals koper of aluminium. Een legering is een mengsel: brons, messing, inox, staal, soldeertin.",
    ),
    dict(
        type="invultekst",
        vraag="Roestvrij staal noemen we in de techniek meestal met de korte naam ___.",
        antwoord="inox",
        uitleg="Inox is een legering van staal met chroom. Het roest niet, en daarom zitten er bestek, gootstenen en werkbladen van gemaakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Hout is een niet-metaal.",
        antwoord=True,
        uitleg="Hout, steen en kunststof zijn niet-metalen. Ze geleiden stroom en warmte veel slechter dan een metaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke proef onderzoek je of een stof een metaal of een niet-metaal is?",
        opties=[
            "Je test of ze stroom geleidt",
            "Je houdt er een magneet tegen en kijkt of ze wordt aangetrokken",
            "Je legt ze een nacht in water en weegt ze daarna nog een keer",
            "Je verwarmt ze tot ze begint te smelten en meet de temperatuur",
        ],
        antwoord=0,
        uitleg="Metalen geleiden stroom, niet-metalen bijna niet. Je neemt het materiaal op in een stroomkring met een lampje of je meet met een multimeter. De magneetproef is een andere proef: die zegt of een metaal een ferrometaal is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee onderzoek je of een metaal een ferrometaal of een non-ferrometaal is?",
        opties=[
            "Met een magneet",
            "Met een weegschaal en een maatbeker met water",
            "Met een multimeter die in de stand ampère staat",
            "Met een thermometer in een pot met kokend water",
        ],
        antwoord=0,
        uitleg="Een ferrometaal bevat ijzer en wordt door een magneet aangetrokken. Een non-ferrometaal zoals aluminium of koper niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze metalen zijn non-ferrometalen?",
        opties=["Aluminium", "Koper", "Lood", "Staal", "Gietijzer"],
        antwoord=[0, 1, 2],
        uitleg="Non-ferro betekent zonder ijzer. Aluminium, koper en lood bevatten geen ijzer. Staal en gietijzer wel, dat zijn ferrometalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet trekt aluminium aan.",
        antwoord=False,
        uitleg="Aluminium is een non-ferrometaal: er zit geen ijzer in, dus een magneet doet er niets mee. Juist daarom werkt de magneetproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk van deze materialen is kunstmatig?",
        opties=["Composiet", "Marmer", "Leder", "Hout"],
        antwoord=0,
        uitleg="Composiet, kunststof en keramische materialen worden door de mens gemaakt. Marmer, leder en hout komen uit de natuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Leder is een natuurlijk materiaal.",
        antwoord=True,
        uitleg="Leder komt van de huid van een dier, dus uit de natuur. Net als hout en marmer is het een natuurlijk materiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen we kunststof een kunstmatig materiaal?",
        opties=[
            "Het wordt door de mens gemaakt",
            "Het komt alleen in warme landen van de wereld voor",
            "Het is altijd doorzichtig en weegt bijna niets",
            "Het kan alleen met een machine bewerkt worden",
        ],
        antwoord=0,
        uitleg="Kunstmatig wil zeggen dat de mens het materiaal maakt, meestal uit een grondstof zoals aardolie. Het bestaat niet kant en klaar in de natuur.",
    ),
    dict(
        type="invultekst",
        vraag="Het materiaal dat ontstaat als je twee of meer metalen samensmelt, heet een ___.",
        antwoord="legering",
        uitleg="Brons is een legering van koper en tin, messing van koper en zink. Je maakt zo'n mengsel om eigenschappen te krijgen die één metaal alleen niet heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij loopt van grondstof naar product?",
        opties=[
            "Klei, baksteen, muur",
            "Baksteen, klei, muur",
            "Muur, klei, baksteen",
            "Klei, muur, baksteen",
        ],
        antwoord=0,
        uitleg="Klei is de grondstof, baksteen het materiaal dat je ervan bakt, en de muur is het product. Die volgorde is altijd dezelfde: grondstof, materiaal, product.",
    ),
    dict(
        type="waarofniet",
        vraag="Zand is een materiaal en glas is een grondstof.",
        antwoord=False,
        uitleg="Het is net omgekeerd. Zand is de grondstof en glas het materiaal dat je er met veel hitte van maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof is géén metaal?",
        opties=["Steen", "Koper", "Lood", "Aluminium"],
        antwoord=0,
        uitleg="Steen is een niet-metaal. Koper, lood en aluminium zijn alle drie metalen, en alle drie non-ferrometalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over ferrometalen kloppen?",
        opties=[
            "Ze bevatten ijzer",
            "Een magneet trekt ze aan",
            "Ze kunnen roesten",
            "Ze wegen altijd minder dan een non-ferrometaal van dezelfde grootte",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ferro komt van ferrum, het Latijnse woord voor ijzer. Ferrometalen worden aangetrokken door een magneet en kunnen roesten. Over hun gewicht zegt dat niets: lood is een non-ferrometaal en is juist heel zwaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Inox is een legering.",
        antwoord=True,
        uitleg="Inox is staal waar chroom aan toegevoegd is. Het is dus een mengsel van metalen, en dat is precies wat een legering is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Soldeertin, brons en messing hebben iets gemeen. Wat?",
        opties=[
            "Het zijn alle drie legeringen",
            "Het zijn alle drie grondstoffen uit de natuur",
            "Het zijn alle drie natuurlijke materialen",
            "Het zijn alle drie niet-metalen zonder geleiding",
        ],
        antwoord=0,
        uitleg="Alle drie zijn ze een mengsel van metalen, dus legeringen. Ze komen niet als zodanig in de natuur voor: ze worden gemaakt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Bij welke groep eigenschappen hoort de hardheid van een materiaal?",
        opties=[
            "Bij de mechanische",
            "Bij de elektrische",
            "Bij de magnetische",
            "Bij de technologische",
        ],
        antwoord=0,
        uitleg="Hardheid hoort bij de mechanische eigenschappen, samen met elasticiteit, treksterkte, taaiheid, broosheid en gewicht. Dat zijn de eigenschappen die met kracht te maken hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze eigenschappen zijn mechanische eigenschappen?",
        opties=[
            "Hardheid",
            "Treksterkte",
            "Broosheid",
            "Smeltpunt",
            "Elektrische geleiding",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hardheid, treksterkte en broosheid zijn mechanisch. Het smeltpunt is een fysische eigenschap, de elektrische geleiding een elektrische.",
    ),
    dict(
        type="waarofniet",
        vraag="Het smeltpunt van een materiaal is een mechanische eigenschap.",
        antwoord=False,
        uitleg="Het smeltpunt is fysisch, net als het stolpunt, de massadichtheid en de warmtegeleiding. Mechanisch zijn de eigenschappen die met kracht te maken hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee onderzoek je de elasticiteit van een materiaal?",
        opties=[
            "Je rekt het uit",
            "Je dompelt het onder in een maatcilinder met water",
            "Je neemt het op in een gesloten elektrische stroomkring",
            "Je houdt er een magneet tegen en kijkt wat er gebeurt",
        ],
        antwoord=0,
        uitleg="Je trekt aan het materiaal en kijkt of het weer zijn vorm aanneemt als je loslaat. Dat is de proef die de fiche noemt bij elasticiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met de onderdompelingsmethode onderzoek je ...",
        opties=[
            "De massadichtheid",
            "De hardheid van het oppervlak",
            "De elektrische geleidbaarheid",
            "De verwerkingstijd van een lijmverbinding",
        ],
        antwoord=0,
        uitleg="Je laat het voorwerp in water zakken en kijkt hoeveel water het verplaatst. Zo ken je het volume, en met de massa erbij ken je de massadichtheid.",
    ),
    dict(
        type="invultekst",
        vraag="Om te weten of een materiaal stroom geleidt, neem je het op in een elektrische ___.",
        antwoord="stroomkring",
        uitleg="Je legt het materiaal in de kring tussen de batterij en het lampje. Brandt het lampje, dan geleidt het materiaal. Een multimeter als ampèremeter kan ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet trekt een ferromagnetisch materiaal aan.",
        antwoord=True,
        uitleg="Aantrekking en afstoting van ferromagnetische materialen zijn de magnetische eigenschappen uit de fiche. Daarop berust ook de magneetproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderdeel mag niet brandbaar zijn en moet tegen vocht kunnen. Welk materiaal kies je?",
        opties=["Kunststof", "Hout", "Karton", "Textiel"],
        antwoord=0,
        uitleg="Kunststof is watervast en brandt veel moeilijker dan hout, karton of textiel. Zo werkt materiaalkeuze: je legt de eisen naast de eigenschappen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hout is een goede keuze voor een onderdeel dat vochtbestendig en onbrandbaar moet zijn.",
        antwoord=False,
        uitleg="Hout brandt en het zuigt vocht op, waardoor het kan zwellen en rotten. Voor die twee eisen is kunststof een betere keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een materiaal broos is?",
        opties=[
            "Het breekt makkelijk",
            "Het geleidt de stroom heel erg goed",
            "Het kan zonder te breken worden uitgerekt",
            "Het smelt al bij een vrij lage temperatuur",
        ],
        antwoord=0,
        uitleg="Een broos materiaal barst of breekt zonder eerst te vervormen. Glas en gietijzer zijn broos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een materiaal dat veel kan verdragen voor het breekt, noemen we ...",
        opties=["Taai", "Broos", "Hard", "Zwaar"],
        antwoord=0,
        uitleg="Taaiheid is het tegengestelde van broosheid. Een taai materiaal vervormt eerst en breekt pas daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze gevaren hebben een eigen veiligheidspictogram?",
        opties=["Ontvlambaar", "Bijtend", "Giftig", "Duur", "Zwaar"],
        antwoord=[0, 1, 2],
        uitleg="Ontvlambaar, bijtend en giftig staan met een eigen pictogram op de verpakking, net als explosief, oxiderend, irriterend, gassen onder druk en gevaarlijk voor het milieu. Hoe duur of hoe zwaar iets is, is geen gevaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram voor bijtend of corrosief?",
        opties=[
            "De stof veroorzaakt brandwonden",
            "De stof kan ontploffen als ze warm wordt",
            "De stof is schadelijk voor het water en de vissen",
            "De stof staat onder druk en kan plots wegspuiten",
        ],
        antwoord=0,
        uitleg="Bijtend of corrosief betekent dat de stof je huid en je ogen aantast. Ontstoppers en sterke zuren dragen dat pictogram.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram voor oxiderende stoffen waarschuwt dat een stof brand kan veroorzaken of erger maken.",
        antwoord=True,
        uitleg="Oxiderende stoffen geven zuurstof af. Daardoor kan iets in de buurt vlam vatten of feller branden, en soms zelfs ontploffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pictogram hoort bij een stof die schadelijk is voor het water en de vissen?",
        opties=[
            "Gevaarlijk voor het aquatisch milieu",
            "Op lange termijn gevaarlijk voor de gezondheid",
            "Gassen onder druk",
            "Oxiderend",
        ],
        antwoord=0,
        uitleg="Dat pictogram betekent schadelijk voor het milieu en watervergiftiging. Zo'n stof mag dus nooit door de gootsteen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met de gasfles waarschuwt voor gassen onder druk.",
        antwoord=True,
        uitleg="Een gas onder druk zit opgesloten in een fles. Wordt die warm of valt ze om, dan kan ze openbarsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke groep eigenschappen hoort de warmtegeleiding?",
        opties=[
            "Bij de fysische",
            "Bij de mechanische",
            "Bij de magnetische",
            "Bij de technologische",
        ],
        antwoord=0,
        uitleg="Warmtegeleiding is een fysische eigenschap, samen met massadichtheid, smeltpunt en stolpunt.",
    ),
    dict(
        type="invultekst",
        vraag="De eigenschap die zegt hoeveel massa er in een bepaald volume van een stof zit, heet de ___.",
        antwoord=["massadichtheid", "dichtheid"],
        uitleg="De massadichtheid draagt het symbool rho en wordt uitgedrukt in kilogram per kubieke meter. Je vindt ze door de massa te delen door het volume.",
    ),
    dict(
        type="waarofniet",
        vraag="De verwerkingstijd van een lijm is een mechanische eigenschap.",
        antwoord=False,
        uitleg="De verwerkingstijd hoort bij de technologische eigenschappen, samen met vervormbaarheid, watervastheid en bewerkbaarheid. Die gaan over wat je met het materiaal kunt doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze eigenschappen zijn technologische eigenschappen?",
        opties=[
            "Vervormbaarheid",
            "Watervastheid",
            "Bewerkbaarheid",
            "Treksterkte",
            "Smeltpunt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Technologische eigenschappen gaan over wat je met het materiaal kunt doen: het buigen, het nat laten worden, het zagen of schuren. Treksterkte is mechanisch en het smeltpunt fysisch.",
    ),
]

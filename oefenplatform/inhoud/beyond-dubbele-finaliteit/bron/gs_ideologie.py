# -*- coding: utf-8 -*-
"""Marxisme, sociaaldemocratie, christendemocratie en migratie.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de ideologieën
die een antwoord gaven op de sociale kwestie, en de migratie die met de
industrialisering en met de heropbouw na 1945 samenhangt.

Deel 1 gaat over het marxisme en de scheiding der wegen die daarop volgde. Deel 2
gaat over de christendemocratie en over migratie, van de landverhuizers van de
negentiende eeuw tot de arbeidsmigratie van na de oorlog.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie schreef samen met Friedrich Engels het Communistisch Manifest?",
        opties=[
            "Karl Marx",
            "Adam Smith",
            "Leo XIII",
            "Charles Darwin",
        ],
        antwoord=0,
        uitleg="Het verscheen in 1848, het jaar van de revoluties in heel Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is volgens het marxisme de motor van de geschiedenis?",
        opties=[
            "de strijd tussen de klassen om de productiemiddelen",
            "de wil van de vorsten en hun oorlogen om gebied",
            "de vooruitgang van de wetenschap en de techniek",
            "de godsdienst en haar greep op het dagelijks leven",
        ],
        antwoord=0,
        uitleg="Wie de fabrieken en de grond bezit, bezit de macht. Daar draait volgens Marx alles om.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je volgens Marx de strijd tussen de bezittende en de werkende klasse?",
        antwoord=["de klassenstrijd", "klassenstrijd"],
        uitleg="Die strijd zou volgens hem onvermijdelijk op een revolutie uitlopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Marx met de meerwaarde?",
        opties=[
            "het verschil tussen wat de arbeid opbrengt en wat het loon kost",
            "de winst die een handelaar op de verkoop van goederen maakt",
            "de belasting die de staat op de winst van de fabriek heft",
            "de rente die een bank op een lening aan de fabriek vraagt",
        ],
        antwoord=0,
        uitleg="Die meerwaarde houdt de eigenaar in zijn zak. Daarin zag Marx de uitbuiting van de arbeider.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het marxisme kloppen?",
        opties=[
            "de productiemiddelen moeten gemeenschappelijk bezit worden",
            "een revolutie van de arbeiders is onvermijdelijk",
            "de kleine ondernemer is de hoop van de samenleving",
            "de staat moet de fabrieken aan hun eigenaars laten",
        ],
        antwoord=[0, 1],
        uitleg="Het laatste is juist de liberale stelling, en het marxisme verwachtte niets van de kleine ondernemer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke samenleving zag Marx als eindpunt van de geschiedenis?",
        opties=[
            "een samenleving zonder klassen en zonder privé-bezit",
            "een samenleving met een sterke koning en een vrije markt",
            "een samenleving waarin de kerk de armenzorg verzorgt",
            "een samenleving met een cijnskiesrecht voor wie bezit heeft",
        ],
        antwoord=0,
        uitleg="De fabrieken moesten gemeenschappelijk bezit worden. Daarvoor voorzag hij een tussenfase: de dictatuur van het proletariaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom riep het marxisme de arbeiders van alle landen op om zich te verenigen?",
        opties=[
            "de arbeiders van elk land hadden volgens Marx hetzelfde belang",
            "de arbeiders van elk land spraken volgens Marx dezelfde taal",
            "de arbeiders van elk land hadden dezelfde godsdienst nodig",
            "de arbeiders van elk land wilden hetzelfde leger oprichten",
        ],
        antwoord=0,
        uitleg="Klasse ging voor natie. Daarom werden er internationales opgericht die over de grenzen samenwerkten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover gingen de socialisten rond 1900 onderling van mening verschillen?",
        opties=[
            "over de weg: revolutie of hervorming",
            "over het doel: meer loon of een kortere werkdag",
            "over de taal: Frans of Nederlands in de beweging",
            "over de kleur: rood of groen voor hun vlaggen",
        ],
        antwoord=0,
        uitleg="Wie voor hervormingen koos, werd sociaaldemocraat. Wie bij de revolutie bleef, werd later communist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de sociaaldemocratie?",
        opties=[
            "zij wil de samenleving stap voor stap hervormen",
            "zij wil de macht met een gewapende revolutie veroveren",
            "zij wil de staat volledig buiten de economie houden",
            "zij wil de standenmaatschappij van vroeger herstellen",
        ],
        antwoord=0,
        uitleg="Niet met een revolutie, maar met wetten: stemrecht, een partij in het parlement en vakbonden aan de tafel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de socialistische stroming die de samenleving langs hervormingen wil veranderen?",
        antwoord=["de sociaaldemocratie", "sociaaldemocratie", "het reformisme"],
        uitleg="Zij heeft het parlement nodig, en dus ook het algemeen stemrecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen gebruikte de sociaaldemocratie om haar doelen te bereiken?",
        opties=[
            "een partij in het parlement, met verkozen afgevaardigden",
            "vakbonden die met de werkgevers onderhandelen",
            "een gewapende opstand tegen het staatsbestuur",
            "een verbod op partijen die het niet met haar eens zijn",
        ],
        antwoord=[0, 1],
        uitleg="Daarmee werden de werkdag, de lonen en later de sociale zekerheid stap voor stap afgedwongen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd na 1945 de kern van het sociaaldemocratische programma?",
        opties=[
            "een stelsel van sociale zekerheid voor iedereen",
            "de afschaffing van alle privé-bezit in het land",
            "de terugkeer naar het cijnskiesrecht van vroeger",
            "de afschaffing van het parlement en de partijen",
        ],
        antwoord=0,
        uitleg="Pensioen, kinderbijslag, ziekteverzekering en werkloosheidsuitkering: de welvaartsstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens het marxisme is de geschiedenis een opeenvolging van klassenstrijden.",
        antwoord=True,
        uitleg="Zo opent het Communistisch Manifest ook: de geschiedenis van elke samenleving is die van haar klassenstrijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Het marxisme wilde dat de fabrieken eigendom van hun fabrikanten bleven.",
        antwoord=False,
        uitleg="Precies het omgekeerde: de productiemiddelen moesten in handen van de gemeenschap komen.",
    ),
    dict(
        type="waarofniet",
        vraag="De sociaaldemocratie had het algemeen stemrecht nodig om haar plannen te kunnen uitvoeren.",
        antwoord=True,
        uitleg="Zonder stemmen geen zetels, en zonder zetels geen wetten. Daarom was stemrecht haar eerste eis.",
    ),
    dict(
        type="waarofniet",
        vraag="Het marxisme en de sociaaldemocratie waren het eens over de weg naar hun doel.",
        antwoord=False,
        uitleg="Over het doel, een rechtvaardiger samenleving, konden zij het vinden. Over revolutie of hervorming niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Marx verwachtte dat het kapitalisme aan zijn eigen tegenstellingen ten onder zou gaan.",
        antwoord=True,
        uitleg="Steeds grotere bedrijven en steeds armere arbeiders zouden volgens hem tot een breuk leiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een tekst uit 1870 die oproept de fabrieken aan de gemeenschap te geven en de staat van de burgerij af te breken. Welke ideologie herken je?",
        opties=[
            "het marxisme",
            "het liberalisme",
            "de christendemocratie",
            "het nationalisme",
        ],
        antwoord=0,
        uitleg="Gemeenschappelijk bezit van de productiemiddelen is het kenmerk waaraan je het marxisme herkent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een programma uit 1900 dat stemrecht, een wet op de werkdag en een ziekenkas eist. Welke stroming herken je?",
        opties=[
            "de sociaaldemocratie",
            "het economisch liberalisme",
            "het revolutionaire marxisme",
            "het modern imperialisme",
        ],
        antwoord=0,
        uitleg="Eisen die je langs het parlement kan afdwingen, horen bij de hervormingsgezinde stroming.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je het marxisme?",
        opties=[
            "in het economische domein, met het bezit van de fabrieken",
            "in het politieke domein, met de macht in de staat",
            "in geen van de maatschappelijke domeinen van die tijd",
            "uitsluitend in het culturele domein van de kunsten",
        ],
        antwoord=[0, 1],
        uitleg="Marx verbond beide: wie de productie bezit, bezit volgens hem ook de staat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke pauselijke brief van 1891 gaf de christelijke arbeidersbeweging haar grondslag?",
        opties=[
            "Rerum Novarum",
            "Het Communistisch Manifest",
            "De Rechten van de Mens",
            "De Wealth of Nations",
        ],
        antwoord=0,
        uitleg="Letterlijk: over de nieuwe dingen. Paus Leo XIII sprak zich daarin over de arbeidersvraag uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke standpunten nam Rerum Novarum in?",
        opties=[
            "de arbeider heeft recht op een rechtvaardig loon",
            "arbeiders mogen zich in eigen verenigingen organiseren",
            "het privé-bezit van fabrieken moet worden afgeschaft",
            "de klassenstrijd is de juiste weg voor de arbeider",
        ],
        antwoord=[0, 1],
        uitleg="Privé-bezit bleef overeind, en de klassenstrijd werd juist afgewezen in naam van de samenwerking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wijst de christendemocratie af aan het economisch liberalisme?",
        opties=[
            "dat de markt alleen de lonen en de werktijden bepaalt",
            "dat de staat de fabrieken van hun eigenaars afneemt",
            "dat de arbeiders zich in vakbonden mogen verenigen",
            "dat er een rechtvaardig loon voor een gezin moet zijn",
        ],
        antwoord=0,
        uitleg="Een loon moest volgens haar een gezin kunnen onderhouden, en niet louter de uitkomst van vraag en aanbod zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wijst de christendemocratie af aan het marxisme?",
        opties=[
            "de klassenstrijd en de afschaffing van het privé-bezit",
            "het recht van arbeiders om een vereniging te vormen",
            "de eis van een loon waarmee een gezin kan leven",
            "de zorg voor wie door ziekte niet kan werken",
        ],
        antwoord=0,
        uitleg="Zij zag klassen niet als vijanden maar als groepen die naar samenwerking moeten zoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe organiseerde de christelijke arbeidersbeweging zich in België?",
        opties=[
            "met eigen vakbonden, ziekenkassen en verenigingen",
            "met één partij die ook de socialisten omvatte",
            "zonder vakbonden, want die wees zij volledig af",
            "met een eigen leger naast dat van de staat",
        ],
        antwoord=0,
        uitleg="Naast de socialistische zuil groeide zo een tweede zuil, met eigen scholen en eigen ziekenhuizen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een netwerk van verenigingen, scholen, vakbonden en ziekenkassen van één strekking?",
        antwoord=["een zuil", "zuil", "verzuiling"],
        uitleg="België kende lange tijd een katholieke, een socialistische en een liberale zuil, elk met eigen diensten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom trokken in de negentiende eeuw miljoenen Europeanen naar Amerika?",
        opties=[
            "armoede en honger dreven hen weg, werk en grond lokten hen",
            "de regeringen van Europa verplichtten hen het land te verlaten",
            "de reis was gratis en werd door de Amerikaanse staat betaald",
            "zij werden door de fabrieken van Europa uitgenodigd te gaan",
        ],
        antwoord=0,
        uitleg="Zulke oorzaken worden duwfactoren en trekfactoren genoemd: wat je wegdrijft en wat je aantrekt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de oorzaken die iemand uit zijn eigen streek wegduwen?",
        antwoord=["duwfactoren", "pushfactoren", "de duwfactoren"],
        uitleg="Armoede, honger, oorlog en vervolging zijn er voorbeelden van. Daartegenover staan de trekfactoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke migratie hoort bij de industrialisering van de negentiende eeuw zelf?",
        opties=[
            "de trek van het platteland naar de industriesteden",
            "de trek van de steden terug naar het platteland",
            "de trek van Marokkanen en Turken naar België",
            "de trek van Belgen naar de Duitse mijnstreek",
        ],
        antwoord=0,
        uitleg="Wie op het land geen werk meer vond, trok naar de fabriek. Daardoor groeiden de steden zo snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom sloot België na 1945 akkoorden om arbeiders uit het buitenland te halen?",
        opties=[
            "er waren voor de mijnen en de heropbouw te weinig arbeiders",
            "er waren in België te veel werklozen om aan werk te helpen",
            "de mogendheden verplichtten België daartoe met een verdrag",
            "de mijnen in België waren toen juist allemaal gesloten",
        ],
        antwoord=0,
        uitleg="Steenkool was de brandstof van de heropbouw, en Belgen vonden het mijnwerk te zwaar en te gevaarlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk land sloot België in 1946 een akkoord over mijnwerkers?",
        opties=[
            "Italië",
            "Turkije",
            "Marokko",
            "Polen",
        ],
        antwoord=0,
        uitleg="In ruil voor arbeiders leverde België steenkool aan Italië. Later volgden akkoorden met andere landen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1956 in Marcinelle?",
        opties=[
            "een brand in een steenkoolmijn kostte 262 mensen het leven",
            "een akkoord met Marokko over arbeiders werd daar gesloten",
            "een staking van de mijnwerkers werd daar neergeslagen",
            "de laatste steenkoolmijn van het land sloot daar de deuren",
        ],
        antwoord=0,
        uitleg="Veel slachtoffers waren Italiaanse mijnwerkers. Italië stuurde daarna een tijd geen arbeiders meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke landen sloot België in 1964 akkoorden over arbeidsmigratie?",
        opties=[
            "Marokko en Turkije",
            "Italië en Polen",
            "Spanje en Portugal",
            "Congo en Rwanda",
        ],
        antwoord=0,
        uitleg="Daarvoor waren er al akkoorden met Italië, Spanje en Griekenland. Zo kwam de arbeidsmigratie van ver op gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1974 met de arbeidsmigratie naar België?",
        opties=[
            "de regering legde de aanwerving van nieuwe arbeiders stil",
            "de regering haalde juist veel meer arbeiders naar het land",
            "de regering gaf alle buitenlandse arbeiders de nationaliteit",
            "de regering sloot een nieuw akkoord met Turkije en Marokko",
        ],
        antwoord=0,
        uitleg="Na de oliecrisis was er werkloosheid. Wie al hier was, kon wel zijn gezin laten overkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Rerum Novarum verdedigde het recht van arbeiders om zich te verenigen.",
        antwoord=True,
        uitleg="Op die grond zijn de christelijke vakbonden en ziekenkassen in België opgericht.",
    ),
    dict(
        type="waarofniet",
        vraag="De christendemocratie wilde het privé-bezit van fabrieken afschaffen.",
        antwoord=False,
        uitleg="Zij verdedigde het privé-bezit, maar vond dat er plichten tegenover de werknemers bij hoorden.",
    ),
    dict(
        type="waarofniet",
        vraag="De gastarbeiders van de jaren vijftig en zestig werden naar België gehaald voor werk dat hier bleef liggen.",
        antwoord=True,
        uitleg="De mijnen, de bouw en de staalnijverheid vonden geen volk voor zwaar en gevaarlijk werk.",
    ),
    dict(
        type="waarofniet",
        vraag="De migratiestop van 1974 maakte een einde aan alle migratie naar België.",
        antwoord=False,
        uitleg="Gezinshereniging bleef mogelijk, en daardoor groeide het aantal inwoners van vreemde herkomst juist nog.",
    ),
    dict(
        type="waarofniet",
        vraag="In de negentiende eeuw trokken ook Belgen als landverhuizer naar andere werelddelen.",
        antwoord=True,
        uitleg="Vooral uit arme streken in Vlaanderen vertrokken gezinnen naar Amerika, en seizoenarbeiders naar Frankrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de arbeidsmigratie naar België kloppen?",
        opties=[
            "ze begon met akkoorden voor de steenkoolmijnen",
            "ze werd in 1974 officieel stilgelegd voor nieuwe arbeiders",
            "ze gebeurde zonder enig akkoord tussen de staten",
            "ze was bedoeld om de Belgische werkloosheid op te lossen",
        ],
        antwoord=[0, 1],
        uitleg="De akkoorden waren juist verdragen tussen staten, en ze kwamen er omdat er volk tekort was.",
    ),
]

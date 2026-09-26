# -*- coding: utf-8 -*-
"""De vragen voor "Ecologie en biodiversiteit" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel biologie, "Ecologie": wat een biotoop is, abiotische en
biotische factoren en hun rol, de gepaste meetinstrumenten om in een biotoop te
meten, hulpmiddelen om te determineren, de onderlinge relaties tussen
organismen, de rol van organismen in een voedselrelatie, de gevolgen van
verstoringen, de manieren om voedselrelaties voor te stellen, biodiversiteit en
het belang ervan, de negatieve en positieve invloed van de mens, en het verband
tussen de kenmerken van een organisme, zijn omgeving en zijn overleven.

Deel 1 gaat over de begrippen, de factoren en het meten in een biotoop.
Deel 2 gaat over voorspellen wat er gebeurt als er iets verandert, over de
invloed van de mens en over aanpassingen aan de omgeving.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een biotoop?",
        opties=["De plaats met eigen omstandigheden waar soorten leven", "Een tabel waarmee je planten en dieren kan determineren", "Een dier dat andere dieren opeet"],
        antwoord=0,
        uitleg="Een bos, een weiland, een moeras, een rivier of zelfs een woonwijk is een biotoop: een leefgebied met eigen omstandigheden waar bepaalde soorten bij passen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een abiotische factor?",
        opties=["Een invloed uit de niet-levende omgeving", "Een invloed van de andere organismen in het gebied", "Een soort voedselketen"],
        antwoord=0,
        uitleg="Abiotisch betekent 'niet-levend': licht, temperatuur, vocht, wind, zoutgehalte, bodemhardheid en voedingsstoffen in de bodem. Biotische factoren zijn de levende wezens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn abiotische factoren?",
        opties=["De temperatuur", "De luchtvochtigheid", "De bacteriën in de bodem", "De planten"],
        antwoord=[0, 1],
        uitleg="Temperatuur en luchtvochtigheid komen uit de niet-levende omgeving. Bacteriën, schimmels, planten en dieren zijn biotische factoren.",
    ),
    dict(
        type="invultekst",
        vraag="Alle levende invloeden in een biotoop noem je samen de ___ factoren.",
        antwoord="biotische",
        uitleg="Biotische factoren zijn de organismen zelf en wat ze doen: begrazen, jagen, bestuiven, ziek maken, beschutting geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk meetinstrument meet je de temperatuur in een biotoop?",
        opties=["Met een thermometer", "Met een anemometer", "Met een hygrometer"],
        antwoord=0,
        uitleg="De thermometer meet de temperatuur, de anemometer de windsnelheid en de hygrometer de luchtvochtigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je de windsnelheid?",
        opties=["Met een anemometer", "Met een lichtmeter", "Met een geluidsmeter"],
        antwoord=0,
        uitleg="Een anemometer meet hoe snel de wind waait. Een lichtmeter meet de verlichtingssterkte en een geluidsmeter de geluidssterkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke meetinstrumenten gebruik je om abiotische factoren te meten?",
        opties=["Een lichtmeter", "Een vochtigheidsmeter", "Een geluidsmeter", "Een determineertabel"],
        antwoord=[0, 1, 2],
        uitleg="Die drie meten licht, bodemvochtigheid en geluid. Een determineertabel is geen meetinstrument maar een hulpmiddel om een soort te herkennen.",
    ),
    dict(
        type="invultekst",
        vraag="Uitzoeken van welke soort een plant of dier is, met behulp van een tabel, heet ___.",
        antwoord="determineren",
        uitleg="Bij het determineren volg je een determineertabel of determineerkaart: telkens kies je tussen twee kenmerken tot je bij de juiste soort uitkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hulpmiddel gebruik je om een klein insect van dichtbij te bekijken in het veld?",
        opties=["Een loep of een binoculair", "Een dynamometer", "Een maatcilinder"],
        antwoord=0,
        uitleg="Een loep vergroot een paar keer en een binoculair toont het beestje in drie dimensies. Voor cellen heb je een lichtmicroscoop nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organismen zijn de producenten in een voedselketen?",
        opties=["De planten", "De planteneters", "De vleeseters"],
        antwoord=0,
        uitleg="Producenten maken zelf energierijke stoffen met fotosynthese. Elke voedselketen begint bij hen; alle andere organismen zijn consumenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen reducenten?",
        opties=["Ze breken dode resten af tot voedingsstoffen", "Ze eten levende planten op en houden de begroeiing kort", "Ze jagen op consumenten"],
        antwoord=0,
        uitleg="Bacteriën en schimmels breken dood materiaal helemaal af. Detrivoren, zoals de regenworm en de pissebed, eten dat dode materiaal eerst in stukken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vos die een muis vangt, is een predator.",
        antwoord=True,
        uitleg="Een predator of jager vangt en eet een prooi. De muis is hier de prooi; zelf is die muis een consument die zaden eet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt een voedselketen voor?",
        opties=[
            "Wie wat opeet, in één rij van pijlen",
            "Alle dieren van een biotoop door elkaar",
            "Het aantal organismen per laag",
        ],
        antwoord=0,
        uitleg="Een voedselketen is één rij: gras → konijn → vos. De pijl betekent 'wordt gegeten door', dus hij wijst in de richting waarin de energie stroomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voedselweb?",
        opties=["Alle voedselketens van een biotoop die aan elkaar hangen", "Een tabel met alle soorten die in een biotoop kunnen leven", "Één lange voedselketen"],
        antwoord=0,
        uitleg="In het echt eet een dier meestal van verschillende soorten. Al die ketens samen vormen een web, en dat toont meteen hoe alles met alles samenhangt.",
    ),
    dict(
        type="invultekst",
        vraag="Een voorstelling waarin elke laag smaller wordt naar boven toe, heet een voedsel___.",
        antwoord="piramide",
        uitleg="Een voedselpiramide toont dat er veel planten nodig zijn voor weinig planteneters, en veel planteneters voor weinig roofdieren: bij elke stap gaat er energie verloren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent biodiversiteit?",
        opties=[
            "De verscheidenheid aan soorten in een gebied",
            "Het aantal dieren van één soort",
            "De grootte van een biotoop",
        ],
        antwoord=0,
        uitleg="Biodiversiteit is de rijkdom aan verschillende soorten, en ook de variatie binnen een soort. Hoe groter ze is, hoe beter een ecosysteem tegen een stoot kan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ecosysteem is een biotoop samen met alle organismen die erin leven.",
        antwoord=True,
        uitleg="Het ecosysteem omvat de levende en de niet-levende delen én hun onderlinge relaties: voedsel, bescherming, voortplanting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hebben waterplanten licht nodig dat tot in het water raakt?",
        opties=[
            "Zonder licht kunnen ze geen fotosynthese doen",
            "Zonder licht krijgen ze geen zuurstof uit de bodem",
            "Zonder licht kunnen ze zich niet voortplanten",
        ],
        antwoord=0,
        uitleg="Licht is een abiotische factor die bepaalt waar planten kunnen groeien. In troebel water raakt het licht minder diep en verdwijnen de waterplanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderlinge relaties kunnen er tussen organismen zijn?",
        opties=["Voedsel", "Bescherming", "Voortplanting", "Luchtdruk"],
        antwoord=[0, 1, 2],
        uitleg="Organismen hebben elkaar nodig om te eten, om te schuilen en om zich voort te planten, bijvoorbeeld een bij die een bloem bestuift. Luchtdruk is geen relatie maar een abiotische factor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een regenworm is een producent in de voedselketen.",
        antwoord=False,
        uitleg="Niet juist. Een regenworm is een detrivoor: hij eet dood organisch materiaal, zoals gevallen bladeren, en maakt het fijn. Daarna breken de reducenten het verder af. Producenten zijn de planten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In een voedselketen gras → konijn → vos verdwijnen alle vossen. Wat gebeurt er eerst?",
        opties=["Er komen meer konijnen, en daardoor blijft er minder gras over", "Er komen minder konijnen omdat ze zonder vijand minder jongen krijgen", "Er verandert niets"],
        antwoord=0,
        uitleg="Zonder jager groeit de prooipopulatie tot het voedsel op raakt. Daarna sterven er konijnen van de honger: een verstoring werkt door de hele keten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen kan het uitsterven van bijen in een gebied hebben?",
        opties=[
            "Minder bestuiving, dus minder vruchten en zaden",
            "Minder voedsel voor dieren die die vruchten eten",
            "Minder soorten bloeiende planten",
            "Meer fotosynthese in het gebied",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bestuivers zitten onderaan veel relaties. Vallen ze weg, dan werkt dat door naar planten, vruchten en alles wat daarvan eet. Van meer fotosynthese is geen sprake.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan er in een voedselpiramide onderaan het meeste organismen?",
        opties=["Omdat er bij elke stap veel energie verloren gaat als warmte", "Omdat planten veel kleiner zijn dan de dieren die erboven staan", "Omdat roofdieren minder eten"],
        antwoord=0,
        uitleg="Van de energie die een dier opeet, gaat maar een klein deel naar groei; de rest verdwijnt als warmte en beweging. Daarom kan elke laag maar een kleine laag boven zich voeden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt een voedselkringloop voor?",
        opties=["Dat stoffen uit dode resten weer bij de planten komen", "Dat de energie eindeloos in de kringloop blijft rondgaan", "Dat elk dier maar één prooi heeft"],
        antwoord=0,
        uitleg="Stoffen draaien rond: planten nemen voedingsstoffen op, dieren eten, alles sterft, reducenten breken het af en de voedingsstoffen komen weer in de bodem. Energie daarentegen stroomt maar één kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze hebben een negatieve invloed op de biodiversiteit?",
        opties=["Ontbossing", "Overbevissing", "Monocultuur", "Ecoducten"],
        antwoord=[0, 1, 2],
        uitleg="Ontbossing, overbevissing, vervuiling, verharding en monocultuur maken een gebied armer aan soorten. Een ecoduct doet net het omgekeerde: het verbindt gebieden weer.",
    ),
    dict(
        type="invultekst",
        vraag="Een brug of tunnel waarlangs dieren veilig een autoweg kunnen kruisen, heet een ___.",
        antwoord="ecoduct",
        uitleg="Een ecoduct verbindt twee stukken natuur die door een weg doorsneden zijn, zodat dieren zich kunnen verplaatsen en populaties niet geïsoleerd raken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een exoot?",
        opties=["Een soort die van elders komt en hier niet thuishoort", "Een zeldzame inheemse plant die hier bijna verdwenen is", "Een dier dat uitgestorven is"],
        antwoord=0,
        uitleg="Sommige exoten, zoals de Japanse duizendknoop, verdringen inheemse soorten omdat ze hier geen natuurlijke vijanden hebben. Dan spreken we van een invasieve exoot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een weiland met tien soorten bloemen steviger dan een weiland met één soort gras?",
        opties=["Bij ziekte of droogte blijven er soorten over", "Omdat er meer zonlicht op tien soorten valt dan op één", "Omdat er minder insecten komen"],
        antwoord=0,
        uitleg="Dat is het belang van biodiversiteit: variatie is een verzekering. Een monocultuur kan door één ziekte of één droog jaar in zijn geheel verloren gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes verkleinen jouw ecologische voetafdruk?",
        opties=[
            "Dagen zonder vlees inlassen",
            "Streekeigen planten in de tuin zetten",
            "Minder verharding en meer groen rond het huis",
            "Elke dag met de auto naar school",
        ],
        antwoord=[0, 1, 2],
        uitleg="De ecologische voetafdruk is de oppervlakte natuur die nodig is voor jouw manier van leven. Minder vlees, meer streekeigen groen en minder beton maken ze kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="De hoeveelheid water die nodig is om te maken wat jij gebruikt, heet je water___.",
        antwoord="voetafdruk",
        uitleg="In je watervoetafdruk telt ook het verborgen water mee: het water dat nodig was om je kleren of je eten te produceren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een ijsbeer een dikke vetlaag en kleine oren?",
        opties=["Zo verliest hij minder warmte in een koude omgeving", "Zo kan hij sneller zwemmen als hij achter een prooi aan gaat", "Zo ziet hij beter in de sneeuw"],
        antwoord=0,
        uitleg="Aanpassingen verhogen de overlevingskans in een bepaalde omgeving. Een dikke isolatielaag en kleine uitsteeksels beperken het warmteverlies in de kou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een haas heeft ogen aan de zijkant van zijn kop, een vos vooraan. Wat verklaart dat?",
        opties=["Een prooidier kijkt rondom, een jager schat afstand", "Een jager heeft grotere ogen nodig om te kunnen jagen", "Een prooidier ziet minder scherp"],
        antwoord=0,
        uitleg="De stand van de ogen is een aanpassing: opzij geeft een bijna volledig overzicht om gevaar te zien, vooraan geeft dieptezicht om een prooi te grijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken van een plant zijn aanpassingen aan een droge omgeving?",
        opties=[
            "Kleine of naaldvormige bladeren",
            "Een dikke waslaag op het blad",
            "Diepe wortels",
            "Heel grote, dunne bladeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Minder bladoppervlak, een waslaag en diepe wortels beperken het waterverlies. Grote dunne bladeren horen net bij een schaduwrijke, vochtige omgeving.",
    ),
    dict(
        type="waarofniet",
        vraag="Kieuwen zijn een aanpassing om zuurstof uit de lucht te halen.",
        antwoord=False,
        uitleg="Niet juist. Vissen halen met hun kieuwen de opgeloste zuurstof uit het wáter. Landdieren halen zuurstof uit de lucht, met hun longen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een wintervacht van een haas in de sneeuw wit?",
        opties=["Schutkleur: zo wordt hij minder snel gezien", "Wit haar is in de sneeuw warmer dan bruin haar", "Wit haar groeit sneller"],
        antwoord=0,
        uitleg="Een schutkleur vergroot de overlevingskans, en wie langer leeft, krijgt meer nakomelingen. Zo blijven zulke kenmerken in een soort bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een vijver wordt mest van een akker gespoeld. Er komen enorm veel algen. Wat gebeurt er daarna?",
        opties=["Het water wordt troebel en er komt zuurstoftekort", "De biodiversiteit neemt toe door de vele nieuwe algen", "De vissen krijgen meer zuurstof"],
        antwoord=0,
        uitleg="Te veel voedingsstoffen zijn ook een verstoring. Algen nemen het licht weg, en als ze afsterven, verbruiken de reducenten zo veel zuurstof dat vissen stikken.",
    ),
    dict(
        type="waarofniet",
        vraag="Begrazing met schapen of runderen kan een natuurgebied soortenrijker maken.",
        antwoord=True,
        uitleg="Grazers houden gras en struiken kort, zodat kleine bloeiende planten licht krijgen. Daarom wordt begrazing als beheer gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelt een schimmel op een dode boomstam?",
        opties=["Reducent", "Producent", "Predator"],
        antwoord=0,
        uitleg="De schimmel breekt het dode hout af tot voedingsstoffen die weer in de bodem komen. Zonder reducenten zou de kringloop stilvallen en alles onder dood materiaal bedolven raken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet in een bos overdag 300 lux onder de bomen en 20 000 lux op de open plek. Wat besluit je?",
        opties=["Onder de bomen groeien planten die weinig licht nodig hebben", "Op de open plek is het overdag veel kouder dan onder de bomen", "De lichtmeter is stuk"],
        antwoord=0,
        uitleg="Verlichtingssterkte meet je in lux met een lichtmeter. Het grote verschil verklaart waarom op de open plek andere soorten groeien dan in de schaduw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over energie en stoffen in een ecosysteem kloppen?",
        opties=[
            "Stoffen gaan rond in een kringloop",
            "Energie komt van de zon en gaat uiteindelijk verloren als warmte",
            "Energie gaat net als stoffen eindeloos rond",
            "Reducenten zetten dode resten om in voedingsstoffen",
        ],
        antwoord=[0, 1, 3],
        uitleg="Stoffen draaien rond dankzij de reducenten, energie stroomt in één richting: van de zon, door de ketens, en weg als warmte. Daarom moet er telkens nieuwe zonne-energie bij.",
    ),
]

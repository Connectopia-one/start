# -*- coding: utf-8 -*-
"""🌍 Beyond — Elektromagnetisme en inductie.

Fysica, de kop "Elektromagnetisme" uit de vakfiche natuurwetenschappen 3DO.
Deel 1 gaat over de magneten zelf, de weissgebieden, het verschil tussen een
permanente magneet en een elektromagneet, en over het magnetisch veld met zijn
veldlijnen. Deel 2 gaat over de magnetische kracht op een stroom of een
bewegende lading en daarna over de elektromagnetische inductie met de wetten
van Lenz en Faraday.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn ferromagnetisch? Kruis alles aan wat juist is.",
        opties=["ijzer", "nikkel", "cobalt", "koper"],
        antwoord=[0, 1, 2],
        uitleg="Enkel die drie metalen worden door een magneet sterk aangetrokken. Koper is wel een goede geleider, maar geen ferromagnetische stof.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleine gebieden in een ferromagnetische stof die elk als een magneetje werken?",
        antwoord=["weissgebieden", "weissgebied", "magneculen"],
        uitleg="Ze heten ook elementaire magneetjes of magneculen. Liggen ze door elkaar, dan is de stof niet magnetisch; liggen ze op een rij, dan wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit ontstaat het magnetisme van een weissgebied op atomaire schaal?",
        opties=[
            "uit de kringstroom en de spin van de elektronen",
            "uit de beweging van de protonen in de kern",
            "uit de lading van de neutronen in de kern",
            "uit de trillingen van het hele kristalrooster",
        ],
        antwoord=0,
        uitleg="Een draaiend en om de kern lopend elektron werkt als een kleine stroomkring. Veel van die stroompjes samen in dezelfde zin geven een weissgebied.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je breekt een staafmagneet in twee. Wat heb je dan?",
        opties=[
            "twee kleinere magneten met elk een noord- en een zuidpool",
            "één stuk met enkel een noordpool en één met enkel een zuidpool",
            "twee stukken die niet meer magnetisch zijn",
            "één magneet en één gewoon stuk ijzer",
        ],
        antwoord=0,
        uitleg="De weissgebieden in beide helften blijven geordend. Je kan een noordpool dus nooit van zijn zuidpool scheiden, hoe klein je de stukjes ook maakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet kan je demagnetiseren door hem sterk op te warmen.",
        antwoord=True,
        uitleg="De warmte doet de weissgebieden door elkaar schudden tot ze niet meer geordend liggen. Hard slaan of een wisselend veld hebben hetzelfde gevolg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel waarbij een stuk ijzer bij een magneet zelf magnetisch wordt?",
        antwoord=["magnetische influentie", "influentie"],
        uitleg="De weissgebieden in het ijzer gaan zich naar het veld van de magneet richten. Daardoor trekt een magneet een hele ketting van paperclips aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een permanente magneet en een elektromagneet?",
        opties=[
            "een elektromagneet werkt enkel zolang er stroom door loopt",
            "een elektromagneet heeft geen noord- en zuidpool",
            "een permanente magneet trekt enkel koper aan",
            "een permanente magneet werkt enkel bij hoge temperatuur",
        ],
        antwoord=0,
        uitleg="Een permanente magneet houdt zijn weissgebieden geordend. Bij een elektromagneet maakt de stroom het veld, dus valt het veld weg als je uitschakelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een ferromagnetische kern in een elektromagneet?",
        opties=[
            "om het magnetisch veld van de spoel veel sterker te maken",
            "om de stroom door de spoel te doen stijgen",
            "om de spoel tegen opwarming te beschermen",
            "om het veld van richting te laten veranderen",
        ],
        antwoord=0,
        uitleg="De weissgebieden in de kern richten zich naar het veld van de spoel en versterken het. Met dezelfde stroom krijg je dus een veel sterkere magneet.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee noordpolen die je naar elkaar toe brengt, trekken elkaar aan.",
        antwoord=False,
        uitleg="Gelijksoortige polen stoten elkaar af, net als gelijksoortige ladingen. Enkel een noordpool en een zuidpool trekken elkaar aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt de zuidpool van het aardmagnetisch veld?",
        opties=[
            "in de buurt van de geografische noordpool",
            "in de buurt van de geografische zuidpool",
            "precies in het midden van de aarde",
            "aan de evenaar",
        ],
        antwoord=0,
        uitleg="Daarom wijst de noordpool van een kompasnaald naar het noorden: ze wordt door de magnetische zuidpool aangetrokken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Naar welke kant wijst de noordpool van een kompasnaald?",
        opties=[
            "naar het geografische noorden",
            "naar het geografische zuiden",
            "altijd naar beneden",
            "altijd naar de dichtste berg",
        ],
        antwoord=0,
        uitleg="De magnetische zuidpool van de aarde ligt daar, en ongelijksoortige polen trekken elkaar aan. Daarom kan je met een kompas de weg vinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kant op loopt een magnetische veldlijn buiten een magneet?",
        opties=[
            "van de noordpool naar de zuidpool",
            "van de zuidpool naar de noordpool",
            "altijd van links naar rechts",
            "altijd in een rechte lijn naar boven",
        ],
        antwoord=0,
        uitleg="Buiten de magneet gaan de veldlijnen van noord naar zuid, binnenin terug van zuid naar noord. Zo vormt elke veldlijn een gesloten lus.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het magnetisch veld daar is.",
        antwoord=True,
        uitleg="Daarom liggen ze het dichtst bij de polen van een magneet. Die veldlijnendichtheid is de manier om op een tekening de sterkte te laten zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk soort veld zit er tussen de twee benen van een hoefijzermagneet?",
        opties=[
            "een homogeen veld",
            "een dipoolveld",
            "helemaal geen veld",
            "een veld dat voortdurend van zin wisselt",
        ],
        antwoord=0,
        uitleg="Daar liggen de veldlijnen mooi parallel en op gelijke afstand. Rond een staafmagneet krijg je juist een dipoolveld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het veldpatroon rond een staafmagneet, met twee polen en gebogen veldlijnen?",
        antwoord=["dipoolveld", "dipool"],
        uitleg="Het is het veld van twee polen die bij elkaar horen. Binnen een lange spoel krijg je juist een homogeen veld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het magnetisch veld rond een rechte stroomvoerende draad uit?",
        opties=[
            "als cirkels rond de draad",
            "als rechte lijnen langs de draad",
            "als lijnen die van de draad weg lopen",
            "als een homogeen veld door de hele ruimte",
        ],
        antwoord=0,
        uitleg="Met je rechterduim in de stroomzin wijzen je gekromde vingers de zin van de veldlijnen aan. Dat is de rechterhandregel of kurkentrekkerregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je de rechterhandregel bij een spoel?",
        opties=[
            "om uit de stroomzin te bepalen waar de noordpool ligt",
            "om de grootte van de stroom te berekenen",
            "om de weerstand van de spoel te meten",
            "om het aantal windingen te tellen",
        ],
        antwoord=0,
        uitleg="Je vingers volgen de stroom rond de spoel en je duim wijst naar de noordpool. Draai je de stroom om, dan wisselen de polen van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een elektromagneet zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "meer stroom geeft een sterker veld",
            "meer windingen geeft een sterker veld",
            "de polen wisselen als je de stroomzin omdraait",
            "het veld blijft na uitschakelen even sterk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Stroom, windingen en een ferromagnetische kern bepalen de sterkte. Schakel je uit, dan verdwijnt het veld, en dat is juist het voordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toestellen werken met een elektromagneet? Kruis alles aan wat juist is.",
        opties=[
            "een elektrische deurbel",
            "een schrootkraan",
            "een relais",
            "een gewone kompasnaald",
        ],
        antwoord=[0, 1, 2],
        uitleg="In alle drie schakelt een stroom een magneet aan en uit. Een kompasnaald is een permanente magneet en heeft geen stroom nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="De magnetische kracht is geen veldkracht, want twee magneten moeten elkaar raken om kracht uit te oefenen.",
        antwoord=False,
        uitleg="Het is net wel een veldkracht: je voelt twee magneten al duwen of trekken voor ze elkaar raken. Ook de elektrische kracht en de zwaartekracht werken zo.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Hoe heet de magnetische kracht op een stroomvoerende geleider in een magnetisch veld?",
        antwoord=["Laplacekracht", "laplacekracht"],
        uitleg="Werkt de kracht op een losse bewegende lading, dan spreek je van de Lorentzkracht. Het is in beide gevallen dezelfde magnetische kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet de magnetische kracht op een bewegende lading?",
        opties=["de Lorentzkracht", "de Laplacekracht", "de coulombkracht", "de normaalkracht"],
        antwoord=0,
        uitleg="De Lorentzkracht buigt de baan van een geladen deeltje af. Bij een stroomdraad heet dezelfde kracht de Laplacekracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lading die stilstaat in een magnetisch veld, ondervindt geen magnetische kracht.",
        antwoord=True,
        uitleg="De lading moet bewegen voor er een magnetische kracht op werkt. Een elektrische kracht zou ze wel voelen, ook in stilstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een draad met stroom hangt in een magnetisch veld en krijgt een kracht. Wat gebeurt er als je de stroomzin omdraait?",
        opties=[
            "de kracht wijst de andere kant op",
            "de kracht wordt twee keer groter",
            "de kracht verdwijnt helemaal",
            "de kracht blijft precies dezelfde",
        ],
        antwoord=0,
        uitleg="De zin van de kracht hangt af van de stroomzin en van de zin van het veld. Draai je één van de twee om, dan keert de kracht om.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen berusten op een kracht op bewegende ladingen of op een stroomdraad? Kruis alles aan wat juist is.",
        opties=[
            "een gelijkstroommotor",
            "een luidspreker",
            "het noorderlicht",
            "een gewone weerstand in een schakeling",
        ],
        antwoord=[0, 1, 2],
        uitleg="In een motor en een luidspreker duwt het veld op een stroomdraad, en bij het noorderlicht buigt het aardveld geladen deeltjes af. Een weerstand zet enkel energie om in warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een massaspectrometer het magnetisch veld?",
        opties=[
            "om geladen deeltjes af te buigen volgens hun massa",
            "om de deeltjes van lading te doen wisselen",
            "om de deeltjes volledig tot stilstand te brengen",
            "om de deeltjes van kleur te doen veranderen",
        ],
        antwoord=0,
        uitleg="Een lichter deeltje buigt sterker af dan een zwaarder deeltje bij dezelfde lading en snelheid. Zo kan je de deeltjes van elkaar scheiden en meten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grootheid die zegt hoeveel magnetisch veld er door een winding gaat?",
        antwoord=["magnetische flux", "flux"],
        uitleg="Ze hangt af van de sterkte van het veld, van de oppervlakte van de winding en van de hoek waaronder het veld erdoor gaat. Verandert de flux, dan ontstaat er spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de magnetische flux door een winding af? Kruis alles aan wat juist is.",
        opties=[
            "van de sterkte van het magnetisch veld",
            "van de oppervlakte van de winding",
            "van de hoek tussen het veld en de normaal op de winding",
            "van de kleur van de draad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie bepalen samen hoeveel veld er door de winding gaat. Staat het veld langs de winding in de plaats van erdoor, dan is de flux nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Lenz?",
        opties=[
            "de inductiestroom werkt de verandering van de flux tegen",
            "de inductiestroom versterkt de verandering van de flux",
            "de inductiestroom is altijd even groot als de gewone stroom",
            "de inductiestroom loopt altijd in dezelfde zin",
        ],
        antwoord=0,
        uitleg="Daarmee bepaal je de zin van de stroom. Neemt de flux toe, dan maakt de stroom een veld dat die toename tegengaat, en omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spoel waarin de flux niet verandert, levert geen inductiespanning.",
        antwoord=True,
        uitleg="Enkel een verándering van de flux wekt spanning op. Een stilliggende magneet bij een stilstaande spoel geeft dus niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de grootte van de inductiespanning af? Kruis alles aan wat juist is.",
        opties=[
            "van hoe snel de flux verandert",
            "van het aantal windingen van de spoel",
            "van de grootte van de fluxverandering",
            "van de lengte van de draad naar de lamp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat is samen de wet van Faraday: snel en veel windingen geeft veel spanning. De aansluitdraden spelen daarin geen rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt een magneet sneller in dezelfde spoel. Wat gebeurt er met de inductiespanning?",
        opties=[
            "ze wordt groter",
            "ze wordt kleiner",
            "ze blijft precies dezelfde",
            "ze wordt nul",
        ],
        antwoord=0,
        uitleg="Sneller bewegen betekent een snellere fluxverandering. Trek je de magneet er weer uit, dan krijg je een spanning met de omgekeerde polariteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spoel met meer windingen levert bij dezelfde beweging een kleinere inductiespanning.",
        antwoord=False,
        uitleg="Het is net omgekeerd: elke winding draagt bij, dus geeft meer windingen meer spanning. Daarom hebben dynamo's en generatoren spoelen met heel veel windingen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stroompjes die in een vol stuk metaal ontstaan als de flux erdoor verandert?",
        antwoord=["wervelstromen", "foucaultstromen"],
        uitleg="Ze heten ook foucaultstromen. Ze verwarmen het metaal, en dat is precies hoe een inductiekookplaat een pan opwarmt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe warmt een inductiekookplaat een pan op?",
        opties=[
            "door wervelstromen in de bodem van de pan op te wekken",
            "door de pan met een elektrische weerstand te verwarmen",
            "door warme lucht tegen de bodem te blazen",
            "door licht op de bodem van de pan te stralen",
        ],
        antwoord=0,
        uitleg="Een wisselend magnetisch veld doet stroompjes in de bodem lopen en die verwarmen het metaal. Daarom werkt zo'n plaat enkel met een ferromagnetische pan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toestellen werken op elektromagnetische inductie? Kruis alles aan wat juist is.",
        opties=[
            "een dynamo op een fiets",
            "een elektrische gitaar",
            "een draadloze oplader",
            "een gewone zaklamp met batterij",
        ],
        antwoord=[0, 1, 2],
        uitleg="In alle drie wekt een veranderende flux spanning op. Een zaklamp op een batterij haalt zijn energie uit een chemische reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wekt een wisselspanningsgenerator spanning op?",
        opties=[
            "een winding draait in een magnetisch veld, dus verandert de flux voortdurend",
            "een magneet wordt steeds sterker gemaakt en weer zwakker",
            "een weerstand wordt voortdurend warmer en kouder",
            "een batterij wordt heel snel aan- en uitgeschakeld",
        ],
        antwoord=0,
        uitleg="Door het draaien verandert de hoek tussen veld en winding voortdurend. Daardoor krijg je een spanning die van plus naar min en terug gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een elektromagnetische rem heeft remblokken nodig die bij elke remming verslijten.",
        antwoord=False,
        uitleg="Hij remt met wervelstromen, die volgens de wet van Lenz de beweging tegengaan. Er raakt niets elkaar aan, dus is er ook geen slijtage.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat een magneet door een koperen buis vallen en hij valt veel trager dan verwacht. Waarom?",
        opties=[
            "de wervelstromen in het koper maken een veld dat de val tegenwerkt",
            "koper is ferromagnetisch en trekt de magneet omhoog",
            "de magneet wordt door de wrijving met het koper afgeremd",
            "de lucht in de buis kan niet snel genoeg weg",
        ],
        antwoord=0,
        uitleg="De veranderende flux wekt stroompjes op in het koper, en die werken volgens Lenz de verandering tegen. De magneet raakt de wand daarbij niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je trekt een magneet uit een spoel in de plaats van hem erin te duwen. Wat verandert er aan de inductiestroom?",
        opties=[
            "hij loopt in de omgekeerde zin",
            "hij wordt twee keer groter",
            "hij verdwijnt volledig",
            "hij blijft precies dezelfde",
        ],
        antwoord=0,
        uitleg="De flux neemt nu af in de plaats van toe, dus werkt de stroom die afname tegen. Volgens de wet van Lenz keert de zin dus om.",
    ),
]

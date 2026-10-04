# -*- coding: utf-8 -*-
"""De magnetische kracht op een stroom en op een lading — 🌍 Beyond, fysica.

Deel 1 gaat over de laplacekracht: de kracht op een stroomvoerende rechte
geleider in een magnetisch veld, hoe je haar richting en zin vindt, hoe je
haar berekent, en waarom twee evenwijdige geleiders elkaar aantrekken of
afstoten. Deel 2 gaat over de lorentzkracht op een bewegende lading, de
cirkelbaan die eruit volgt, en de toepassingen die de fiche noemt: de
massaspectrometer, het cyclotron, de hallsensor, het noorderlicht, de
luidspreker en de gelijkstroommotor.

De kern van het thema staat in één zin: de magnetische kracht staat loodrecht
op het veld én op de beweging. Daarom verandert ze wel de richting van een
lading, maar nooit haar snelheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de kracht op een stroomvoerende geleider in een magnetisch veld?",
        opties=[
            "de laplacekracht",
            "de coulombkracht",
            "de lorentzkracht",
            "de gravitatiekracht",
        ],
        antwoord=0,
        uitleg="De kracht op één bewegende lading heet de lorentzkracht. Het is in wezen "
        "dezelfde kracht, want een stroom is niets anders dan bewegende ladingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe staat de magnetische kracht op een stroomvoerende draad?",
        opties=[
            "loodrecht op de draad en loodrecht op het veld",
            "evenwijdig met de draad en loodrecht op het veld",
            "evenwijdig met het veld en loodrecht op de draad",
            "altijd in dezelfde zin als de stroom in de draad",
        ],
        antwoord=0,
        uitleg="Ze staat dus loodrecht op het vlak dat de draad en het veld samen bepalen. "
        "Met je rechterhand vind je aan welke kant van dat vlak ze wijst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een draad die evenwijdig met de veldlijnen ligt, voelt geen magnetische kracht.",
        antwoord=True,
        uitleg="In de formule staat de sinus van de hoek tussen de draad en het veld, en "
        "die is nul bij nul graden. De kracht is het grootst als de draad loodrecht op "
        "het veld staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de kracht op een stroomvoerende draad af? Kruis alles aan wat juist is.",
        opties=[
            "van de stroomsterkte in de draad",
            "van de lengte van de draad in het veld",
            "van de weerstand van de draad zelf",
            "van de spanning van de bron erachter",
        ],
        antwoord=[0, 1],
        uitleg="Ook de magnetische inductie en de hoek met het veld tellen mee. De "
        "weerstand telt alleen onrechtstreeks, want die bepaalt de stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een draad van 0,5 m ligt loodrecht in een veld van 0,2 T en voert 3 A. Hoe groot is de kracht?",
        opties=[
            "0,3 N",
            "3,2 N",
            "0,03 N",
            "30 N",
        ],
        antwoord=0,
        uitleg="De kracht is B maal I maal l: 0,2 maal 3 maal 0,5 is 0,3 newton. Bij een "
        "schuine hoek komt er nog een sinus bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de magnetische kracht op een stroomvoerende draad af? Kruis alles aan wat juist is.",
        opties=[
            "de stroomsterkte door de draad",
            "de sterkte van het magnetisch veld",
            "de lengte van de draad in het veld",
            "de eigen weerstand van de draad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ook de hoek met de veldlijnen telt mee: evenwijdig is de kracht nul. Keer je "
        "de stroom om, dan keert ook de zin van de kracht om.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht op één bewegende lading in een magnetisch veld?",
        antwoord=["lorentzkracht", "de lorentzkracht", "lorentz"],
        uitleg="De kracht op een hele stroomvoerende draad heet de laplacekracht. Beide "
        "staan loodrecht op het veld en op de beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee evenwijdige draden voeren stroom in dezelfde zin. Wat gebeurt er?",
        opties=[
            "ze trekken elkaar aan",
            "ze stoten elkaar af",
            "ze doen niets zolang ze elkaar niet raken",
            "ze draaien allebei een kwartslag weg",
        ],
        antwoord=0,
        uitleg="Elke draad zit in het veld van de andere, en de laplacekracht wijst dan naar "
        "elkaar toe. Lopen de stromen tegengesteld, dan stoten ze elkaar af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee evenwijdige draden voeren stroom in tegengestelde zin. Wat gebeurt er?",
        opties=[
            "ze stoten elkaar af",
            "ze trekken elkaar aan",
            "ze voelen geen enkele kracht van elkaar",
            "ze trekken enkel aan als ze dicht genoeg liggen",
        ],
        antwoord=0,
        uitleg="Het is precies omgekeerd aan het geval met gelijke stroomzin. Dat verschil "
        "is net het tegengestelde van wat je bij elektrische ladingen zou verwachten.",
    ),
    dict(
        type="waarofniet",
        vraag="De kracht tussen twee evenwijdige stroomvoerende draden wordt kleiner als ze dichter bij elkaar liggen.",
        antwoord=False,
        uitleg="Ze wordt juist groter. Het veld van een rechte draad neemt af met de "
        "afstand, dus is het veld op de plaats van de andere draad sterker als ze dichter "
        "liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de zin van de kracht op een stroomvoerende draad?",
        opties=[
            "met je rechterhand: vingers in de stroomzin, veld in de handpalm, duim geeft de kracht",
            "met je rechterhand: duim in de stroomzin, vingers geven de kracht aan",
            "met een kompas dat je naast de draad legt en laat uitdraaien",
            "met de wet van Ohm, want die geeft de zin van de stroom aan",
        ],
        antwoord=0,
        uitleg="Er bestaan meerdere versies van die handregel; houd je aan de versie uit je "
        "cursus. Wat telt is dat de kracht loodrecht op draad én veld komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een draad staat onder 30 graden met de veldlijnen in plaats van loodrecht. Wat gebeurt er met de kracht?",
        opties=[
            "ze wordt kleiner, want de sinus van 30 graden is maar een half",
            "ze wordt groter, want de hoek telt dubbel mee in de formule",
            "ze blijft precies gelijk, want de hoek doet er niet toe",
            "ze valt weg, want kracht ontstaat enkel bij 90 graden",
        ],
        antwoord=0,
        uitleg="De formule bevat de sinus van de hoek tussen draad en veld. Bij nul graden "
        "is de kracht nul en bij negentig graden het grootst.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk symbool schrijf je de magnetische inductie?",
        antwoord=["B", "de B", "B-vector"],
        uitleg="De eenheid is de tesla. De magnetische kracht schrijf je met F met een B "
        "als index.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stilstaande lading in een magnetisch veld voelt een magnetische kracht.",
        antwoord=False,
        uitleg="In de formule staat de snelheid, en die is dan nul. Alleen een bewegende "
        "lading voelt het magnetisch veld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de laplacekracht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is recht evenredig met de stroomsterkte",
            "ze is recht evenredig met de magnetische inductie",
            "ze is omgekeerd evenredig met de lengte van de draad",
            "ze is recht evenredig met de weerstand van de draad",
        ],
        antwoord=[0, 1],
        uitleg="Ze is ook recht evenredig met de lengte in het veld. Een langere draad in "
        "hetzelfde veld voelt dus een grotere kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een luidspreker?",
        opties=[
            "de wisselstroom in een spoel duwt het membraan heen en weer",
            "de wisselstroom warmt het membraan op en laat het trillen",
            "een permanente magneet draait rond en duwt de lucht weg",
            "een spoel zendt het geluid rechtstreeks als golf uit",
        ],
        antwoord=0,
        uitleg="De spoel zit in het veld van een permanente magneet, dus voelt ze een "
        "laplacekracht. Keert de stroom om, dan keert ook de kracht om, en het membraan "
        "trilt mee met het signaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom draait de spoel van een gelijkstroommotor?",
        opties=[
            "de krachten op de twee zijden wijzen in tegengestelde zin",
            "de spoel wordt door de magneet gewoon naar zich toe getrokken",
            "de warmte in de spoel zet het metaal plaatselijk uit",
            "de spanningsbron duwt de spoel rechtstreeks in het rond",
        ],
        antwoord=0,
        uitleg="De stroom loopt in de twee zijden tegengesteld, dus duwt de kracht de ene "
        "zijde omhoog en de andere omlaag. Dat koppel laat de spoel draaien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de collector in een gelijkstroommotor?",
        opties=[
            "om de stroom elke halve omwenteling om te keren",
            "om de stroom gelijkmatig over de spoelen te verdelen",
            "om de warmte uit de spoel naar buiten af te voeren",
            "om het magnetisch veld elke seconde te versterken",
        ],
        antwoord=0,
        uitleg="Zonder die omkering zou de spoel na een halve slag weer terugdraaien. Dankzij "
        "de collector duwt de kracht telkens in dezelfde draaizin.",
    ),
    dict(
        type="waarofniet",
        vraag="De magnetische kracht op een draad is het grootst als de draad loodrecht op de veldlijnen staat.",
        antwoord=True,
        uitleg="De sinus van negentig graden is één, en dat is de grootste waarde. "
        "Evenwijdig met het veld is de kracht juist nul.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kracht duwt het membraan van een luidspreker heen en weer?",
        antwoord=["laplacekracht", "de laplacekracht", "magnetische kracht"],
        uitleg="De spoel aan het membraan voert stroom en zit in het veld van een "
        "permanente magneet. Keert de stroom om, dan keert ook die kracht om.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de lorentzkracht op een bewegende lading af? Kruis alles aan wat juist is.",
        opties=[
            "van de grootte van de lading",
            "van de snelheid van de lading",
            "van de massa van het deeltje",
            "van de tijd die het deeltje al onderweg is",
        ],
        antwoord=[0, 1],
        uitleg="Ook het veld en de hoek tussen snelheid en veld tellen mee. De massa speelt "
        "pas een rol als je de baan wil berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lading van 2 mC beweegt met 500 m/s loodrecht door een veld van 0,4 T. Hoe groot is de kracht?",
        opties=[
            "0,4 N",
            "4 N",
            "0,04 N",
            "250 N",
        ],
        antwoord=0,
        uitleg="De kracht is q maal v maal B: 0,002 maal 500 maal 0,4 is 0,4 newton. Let "
        "op de omzetting van millicoulomb naar coulomb.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke baan volgt een lading die loodrecht een homogeen magnetisch veld binnenkomt?",
        opties=[
            "een cirkelbaan",
            "een rechte lijn zonder afwijking",
            "een parabool zoals bij een worp",
            "een spiraal die steeds groter wordt",
        ],
        antwoord=0,
        uitleg="De kracht staat altijd loodrecht op de snelheid, dus werkt ze als een "
        "middelpuntzoekende kracht. Komt de lading schuin binnen, dan wordt het een "
        "schroeflijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magnetisch veld kan de snelheid van een lading niet groter maken.",
        antwoord=True,
        uitleg="De kracht staat loodrecht op de beweging, dus verricht ze geen arbeid. Ze "
        "verandert alleen de richting, niet de grootte van de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de straal van de cirkelbaan van een lading in een magnetisch veld af? Kruis alles aan wat juist is.",
        opties=[
            "de massa van het deeltje",
            "de snelheid van het deeltje",
            "de sterkte van het magnetisch veld",
            "de temperatuur van de omgeving",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ook de lading zelf telt mee. Een sneller of zwaarder deeltje maakt een "
        "ruimere bocht, een sterker veld een krappere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee deeltjes met dezelfde lading en snelheid maken in hetzelfde veld een bocht met een andere straal. Wat verschilt er?",
        opties=[
            "hun massa",
            "hun teken van lading",
            "de sterkte van het veld",
            "de tijd die ze onderweg zijn",
        ],
        antwoord=0,
        uitleg="De straal is recht evenredig met de massa. Op dat principe berust de "
        "massaspectrometer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het toestel dat ionen op hun massa scheidt met een magnetisch veld?",
        antwoord=["massaspectrometer", "een massaspectrometer", "massaspectrometrie"],
        uitleg="Zwaardere ionen maken een wijdere bocht en komen verderop terecht. Zo kan je "
        "isotopen van elkaar onderscheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een positieve en een negatieve lading vliegen met dezelfde snelheid het veld binnen. Wat verschilt er?",
        opties=[
            "ze buigen naar tegengestelde kanten af",
            "ze buigen allebei dezelfde kant op af",
            "de negatieve lading voelt geen enkele kracht",
            "de positieve lading gaat veel sneller bewegen",
        ],
        antwoord=0,
        uitleg="Het teken van de lading keert de zin van de kracht om. De grootte van de "
        "kracht en de straal blijven wel gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een cyclotron?",
        opties=[
            "om geladen deeltjes tot hoge snelheid te versnellen",
            "om de massa van een onbekend ion te meten",
            "om de sterkte van een magnetisch veld af te lezen",
            "om een magnetisch veld uit elektriciteit te maken",
        ],
        antwoord=0,
        uitleg="Het magnetisch veld houdt de deeltjes in een cirkel, en een wisselspanning "
        "geeft ze bij elke halve omloop een duwtje. Zo worden de cirkels steeds wijder.",
    ),
    dict(
        type="waarofniet",
        vraag="In een cyclotron doet het magnetisch veld het versnellende werk.",
        antwoord=False,
        uitleg="Het magnetisch veld buigt de baan alleen om. De versnelling komt van het "
        "elektrisch veld tussen de twee helften.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een hallsensor?",
        opties=[
            "om de sterkte van een magnetisch veld te meten",
            "om de stroom in een kring te onderbreken",
            "om een magnetisch veld sterker te maken",
            "om een spoel tegen oververhitting te beschermen",
        ],
        antwoord=0,
        uitleg="In het plaatje duwt de lorentzkracht de ladingen naar één kant, en daardoor "
        "ontstaat er een spanning dwars op de stroom. Een teslameter werkt zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zie je het noorderlicht vooral in de buurt van de polen?",
        opties=[
            "het aardmagnetisch veld leidt de geladen deeltjes daarheen",
            "de zon schijnt daar het hele jaar door het schuinst",
            "de lucht is daar het dunst en dus het beste zichtbaar",
            "de aarde draait daar het traagst om haar eigen as",
        ],
        antwoord=0,
        uitleg="De deeltjes van de zonnewind volgen in een schroeflijn de veldlijnen, en die "
        "komen bij de polen de dampkring binnen. Daar botsen ze tegen gasdeeltjes en die "
        "lichten op.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kleur licht geeft zuurstof meestal in het noorderlicht?",
        antwoord=["groen", "groene", "groen licht"],
        uitleg="Op grote hoogte kan zuurstof ook rood geven, en stikstof paars of blauw. "
        "Welke kleur je ziet, hangt af van het gas en de hoogte.",
    ),
    dict(
        type="waarofniet",
        vraag="De magnetische kracht op een lading staat loodrecht op haar snelheid.",
        antwoord=True,
        uitleg="Daarom verandert ze wel de richting van de beweging, maar nooit de grootte "
        "van de snelheid. Een elektrische kracht kan juist wel versnellen of afremmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lading beweegt precies evenwijdig met de veldlijnen. Welke kracht voelt ze?",
        opties=[
            "geen enkele, want de hoek met het veld is nul",
            "de grootst mogelijke kracht van het hele veld",
            "een kracht die haar afremt tot ze stilstaat",
            "een kracht die haar in een cirkel laat draaien",
        ],
        antwoord=0,
        uitleg="In de formule staat de sinus van de hoek tussen de snelheid en het veld. Bij "
        "nul graden is die sinus nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen berusten op de kracht op bewegende ladingen? Kruis alles aan wat juist is.",
        opties=[
            "de massaspectrometer",
            "het cyclotron",
            "de gewone gloeilamp",
            "de mechanische veer in een pen",
        ],
        antwoord=[0, 1],
        uitleg="Ook de hallsensor en het noorderlicht horen daarbij. De luidspreker en de "
        "motor berusten op dezelfde kracht, maar dan op een hele stroomvoerende draad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de straal van de cirkelbaan als je het magnetisch veld verdubbelt?",
        opties=[
            "de straal wordt half zo groot",
            "de straal wordt twee keer zo groot",
            "de straal blijft precies gelijk",
            "de baan wordt dan een rechte lijn",
        ],
        antwoord=0,
        uitleg="In de formule voor de straal staat B in de noemer. Een sterker veld dwingt "
        "het deeltje dus in een nauwere bocht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een deeltje dat schuin een magnetisch veld binnenkomt, blijft gewoon rechtdoor gaan.",
        antwoord=False,
        uitleg="Het volgt een schroeflijn: het stuk van de snelheid langs het veld loopt "
        "door, het stuk dwars erop maakt een cirkel. Samen geeft dat een spiraal rond de "
        "veldlijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe weet je of een deeltje in een massaspectrometer zwaar of licht is?",
        opties=[
            "aan de straal van de bocht die het beschrijft",
            "aan de kleur van het spoor dat het achterlaat",
            "aan de tijd die het in het toestel doorbrengt",
            "aan de spanning die de detector aangeeft",
        ],
        antwoord=0,
        uitleg="Zwaardere deeltjes maken een wijdere bocht bij dezelfde lading en snelheid. "
        "De plaats waar ze aankomen, verraadt dus hun massa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de baan van een lading die loodrecht een homogeen magnetisch veld binnenkomt?",
        antwoord=["cirkelbaan", "een cirkel", "cirkel"],
        uitleg="De lorentzkracht werkt daarbij als middelpuntzoekende kracht. Komt de lading "
        "schuin binnen, dan wordt het een schroeflijn.",
    ),
]

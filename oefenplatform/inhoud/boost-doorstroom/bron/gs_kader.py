# -*- coding: utf-8 -*-
"""De vragen voor "Het historisch referentiekader" (🚀 Boost doorstroom, geschiedenis).

Uit de vakfiche, het eerste hoofdstuk: de zeven periodes van de courante
westerse periodisering, de structuurbegrippen rond tijd en rond ruimte, de vier
maatschappelijke domeinen, de scharnierpunten tussen periodes, en de
beperkingen van periodiseren.

Deel 1 zet de periodes, de tijdbegrippen en de domeinen neer. Deel 2 gaat over
ruimte, scharnierpunten en over wat periodisering níét kan.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel periodes telt de courante westerse periodisering?",
        opties=["zeven", "vier", "vijf", "tien"],
        antwoord=0,
        uitleg="Prehistorie, het oude nabije oosten, de klassieke oudheid, de middeleeuwen, de vroegmoderne tijd, de moderne tijd en de hedendaagse tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke periode komt meteen na de klassieke oudheid?",
        opties=[
            "de middeleeuwen",
            "de vroegmoderne tijd",
            "het oude nabije oosten",
            "de hedendaagse tijd",
        ],
        antwoord=0,
        uitleg="De volgorde is: prehistorie, oude nabije oosten, klassieke oudheid, middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de periode vóór het schrift, waarvan we alleen materiële resten hebben?",
        antwoord="de prehistorie",
        uitleg="Prehistorie betekent letterlijk: vóór de geschiedenis, dus vóór er geschreven bronnen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuurbegrippen horen bij tijd?",
        opties=["chronologie", "continuïteit", "gelijktijdigheid", "maritiem"],
        antwoord=[0, 1, 2],
        uitleg="Maritiem hoort bij ruimte. Tijdrekening, chronologie, periode, continuïteit, verandering, evolutie, revolutie, duur, gelijktijdigheid en ongelijktijdigheid horen bij tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen evolutie en revolutie?",
        opties=[
            "Evolutie is een geleidelijke verandering, revolutie een snelle en ingrijpende",
            "Evolutie gaat over natuur, revolutie over politiek",
            "Evolutie gebeurt in de oudheid, revolutie in de moderne tijd",
            "Er is geen verschil, het zijn twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Het gaat over tempo en omvang, niet over het onderwerp. De industriële revolutie was snel én ingrijpend; de groei van de steden ging geleidelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Continuïteit betekent dat iets over een lange tijd hetzelfde blijft.",
        antwoord=True,
        uitleg="Continuïteit en verandering zijn elkaars tegenhangers. Een historicus kijkt altijd naar allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee dingen gebeuren in hetzelfde jaar, maar op twee plaatsen die niets van elkaar weten. Welk begrip past?",
        opties=[
            "gelijktijdigheid",
            "ongelijktijdigheid",
            "continuïteit",
            "chronologie",
        ],
        antwoord=0,
        uitleg="Gelijktijdigheid gaat enkel over hetzelfde moment, niet over contact. Ongelijktijdigheid betekent dat een ontwikkeling ergens vroeger of later gebeurt dan elders.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het begin van de 13de eeuw schrijft men in het Arabische rijk al op papier, terwijl men in Europa nog perkament gebruikt. Wat toont dat?",
        opties=[
            "ongelijktijdigheid",
            "gelijktijdigheid",
            "een scharnierpunt",
            "een revolutie",
        ],
        antwoord=0,
        uitleg="Dezelfde tijd, maar een ontwikkeling die in de ene samenleving al doorgebroken is en in de andere nog niet. Dat is precies ongelijktijdigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Chronologie en periodisering betekenen hetzelfde.",
        antwoord=False,
        uitleg="Chronologie is gebeurtenissen in de juiste volgorde zetten. Periodisering is die volgorde daarna in stukken knippen en die stukken een naam geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel maatschappelijke domeinen onderscheidt de vakfiche?",
        opties=["vier", "drie", "vijf", "zeven"],
        antwoord=0,
        uitleg="Het culturele, het economische, het politieke en het sociale domein.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk domein hoort e-commerce thuis?",
        opties=[
            "het economische domein",
            "het culturele domein",
            "het politieke domein",
            "het sociale domein",
        ],
        antwoord=0,
        uitleg="Het gaat om kopen en verkopen, dus om productie en handel. Dat is economisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een geschilderd portret van sultan Süleyman I hoort in welke domeinen thuis?",
        opties=[
            "het politieke domein",
            "het culturele domein",
            "het economische domein",
            "het sociale domein",
        ],
        antwoord=[0, 1],
        uitleg="Het is een kunstwerk, dus cultureel, en het toont de macht van een heerser, dus ook politiek. Eén ding kan in meerdere domeinen zitten.",
    ),
    dict(
        type="invultekst",
        vraag="In welk maatschappelijk domein hoort een godsdienst thuis?",
        antwoord="het culturele",
        uitleg="Levensbeschouwing hoort bij het culturele domein, ook al heeft ze vaak politieke en sociale gevolgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebeurtenis hoort altijd maar in één maatschappelijk domein thuis.",
        antwoord=False,
        uitleg="De meeste gebeurtenissen raken meerdere domeinen tegelijk. Een oorlog is politiek, maar ook sociaal en economisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke periode situeer je de Tweede Wereldoorlog?",
        opties=[
            "de hedendaagse tijd",
            "de moderne tijd",
            "de vroegmoderne tijd",
            "de middeleeuwen",
        ],
        antwoord=0,
        uitleg="De hedendaagse tijd begint in de westerse periodisering rond het einde van de 18de eeuw en loopt tot vandaag.",
    ),
    dict(
        type="waarofniet",
        vraag="De middeleeuwen en de vroegmoderne tijd zijn de twee periodes die je voor dit vak grondig moet kennen.",
        antwoord=True,
        uitleg="De fiche geeft voor die twee periodes afgebakende leerinhouden. De andere periodes komen enkel aan bod om mee te vergelijken, en die info krijg je op het examen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijen horen bij het sociale domein?",
        opties=[
            "de gelaagde samenleving",
            "migratie",
            "slavernij",
            "de drukkunst",
        ],
        antwoord=[0, 1, 2],
        uitleg="De drukkunst is een culturele en technologische zaak. Wie waar staat in de samenleving, wie zich verplaatst en wie onvrij is, hoort bij het sociale domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tijdrekening begint overal ter wereld bij hetzelfde jaar nul.",
        antwoord=False,
        uitleg="De christelijke, de islamitische en de joodse tijdrekening hebben elk een ander beginpunt. Een tijdrekening is een afspraak, geen natuurwet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt een historicus met 'duur'?",
        opties=[
            "hoe lang een toestand of een ontwikkeling voortduurt",
            "hoe zwaar iets was om te dragen",
            "hoeveel iets kostte",
            "in welke volgorde gebeurtenissen kwamen",
        ],
        antwoord=0,
        uitleg="Sommige veranderingen duren enkele dagen, andere eeuwen. Duur helpt je die twee uit elkaar te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het historisch referentiekader bestaat uit begrippen over tijd, over ruimte en over de maatschappelijke domeinen.",
        antwoord=True,
        uitleg="Die drie assen samen laten je elk historisch gegeven een plaats geven, en dat is wat een referentiekader doet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke structuurbegrippen horen bij ruimte?",
        opties=["lokaal", "mondiaal", "maritiem", "revolutie"],
        antwoord=[0, 1, 2],
        uitleg="Revolutie hoort bij tijd. Lokaal, regionaal, West-Europees, mondiaal, westers, niet-westers, stedelijk, ruraal, continentaal en maritiem horen bij ruimte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'ruraal'?",
        opties=[
            "op het platteland",
            "in de stad",
            "aan zee",
            "in het binnenland",
        ],
        antwoord=0,
        uitleg="Ruraal en stedelijk zijn elkaars tegenhangers. Universiteiten ontstonden in een stedelijke context, kloosters vaak in een rurale.",
    ),
    dict(
        type="invultekst",
        vraag="Welk ruimtebegrip gebruik je voor iets dat de hele wereld raakt?",
        antwoord="mondiaal",
        uitleg="Mondiaal is de grootste schaal. Daaronder liggen continentaal, West-Europees, regionaal en lokaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Het begrip 'westers' verwijst naar een windstreek op de kaart en niets meer.",
        antwoord=False,
        uitleg="Westers en niet-westers gaan over een culturele en politieke traditie, niet over een windrichting. Australië ligt in het oosten en geldt als westers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt een kaart van het rijk van Karel V met een kaart van vandaag. Wat doe je dan?",
        opties=[
            "je situeert een historisch gegeven in de ruimte",
            "je situeert een historisch gegeven in de tijd",
            "je bepaalt een scharnierpunt",
            "je beoordeelt een bron op betrouwbaarheid",
        ],
        antwoord=0,
        uitleg="Zo'n vergelijking zegt welke hedendaagse landen tot dat rijk behoorden. Dat is werken op de as van de ruimte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een scharnierpunt?",
        opties=[
            "een gebeurtenis of evolutie die de overgang vormt tussen twee historische periodes",
            "het jaar precies in het midden van een historische periode, tussen begin en einde",
            "een jaartal dat je uit het hoofd moet kennen om een examen te kunnen afleggen",
            "een plaats op de wereldkaart waar twee culturen elkaar voor het eerst raken",
        ],
        antwoord=0,
        uitleg="Een scharnierpunt is het draaipunt waarop historici een nieuwe periode laten beginnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebeurtenissen worden als scharnierpunt gebruikt?",
        opties=[
            "het einde van het West-Romeinse Rijk",
            "de aankomst van Columbus op de Caraïben",
            "de val van Constantinopel",
            "de kroning van Karel de Grote",
        ],
        antwoord=[0, 1, 2],
        uitleg="De kroning van Karel de Grote ligt middenin de middeleeuwen en begint geen nieuwe periode. De drie andere worden wél als grens gebruikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het einde van het West-Romeinse Rijk wordt gebruikt als grens tussen de klassieke oudheid en de middeleeuwen.",
        antwoord=True,
        uitleg="476 is de symbolische datum. In werkelijkheid verdween het rijk stukje bij beetje over meer dan een eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laat men met de aankomst van Columbus een nieuwe periode beginnen?",
        opties=[
            "omdat de contacten tussen de continenten daarna blijvend veranderen",
            "omdat Columbus als allereerste mens ooit de Atlantische Oceaan is overgestoken",
            "omdat het werelddeel Amerika pas vanaf dat jaar door mensen bewoond raakte",
            "omdat de middeleeuwen volgens de afspraak precies honderd jaar geduurd hebben",
        ],
        antwoord=0,
        uitleg="Er komt een blijvende stroom van mensen, goederen, planten, ziekten en ideeën op gang tussen Europa, Afrika en Amerika. Dat is de breuk, niet de reis zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de twee principes waarmee je een periode afbakent?",
        opties=[
            "een selectie van kenmerken en gebeurtenissen, en een symbolische begin- en einddatum",
            "het aantal jaren dat ze duurt, en het aantal koningen dat er geregeerd heeft",
            "de taal die er gesproken wordt, en de godsdienst die er in die streek gold",
            "het klimaat van die eeuwen, en de omvang van de bevolking die er toen leefde",
        ],
        antwoord=0,
        uitleg="Je kiest waarop je let, en je kiest een datum die dat samenvat. Allebei zijn keuzes van mensen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een periodegrens is een harde breuk: op die dag verandert de samenleving echt.",
        antwoord=False,
        uitleg="Een symbolische datum is een afspraak. Rond 476 leefden de meeste mensen precies zoals de dag ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beperkingen heeft periodisering?",
        opties=[
            "ze is gebouwd op een selectie, dus wat niet gekozen is, valt weg",
            "ze suggereert een scherpe breuk waar de werkelijkheid geleidelijk is",
            "ze past niet even goed op niet-westerse samenlevingen",
            "ze maakt het onmogelijk om gebeurtenissen te dateren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dateren kan je nog altijd, dat is net wat een tijdrekening doet. De eerste drie zijn de echte beperkingen.",
    ),
    dict(
        type="waarofniet",
        vraag="De westerse periodisering past even goed op de geschiedenis van China als op die van Europa.",
        antwoord=False,
        uitleg="China kent zijn eigen indeling in dynastieën. Onze 'middeleeuwen' beginnen bij een Romeinse gebeurtenis die voor China niets betekende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Nederland gebruikt een eigen periodisering met tien tijdvakken. Wat zegt dat?",
        opties=[
            "dat de indeling van de geschiedenis een keuze is en geen natuurwet",
            "dat de Nederlandse geschiedenis anders verlopen is dan de Belgische",
            "dat tien tijdvakken wetenschappelijk juister zijn dan zeven",
            "dat Nederland geen middeleeuwen gekend heeft",
        ],
        antwoord=0,
        uitleg="Een andere selectie van kenmerken levert een andere indeling op, over exact dezelfde eeuwen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang tussen twee historische periodes met één woord?",
        antwoord="een scharnierpunt",
        uitleg="Het beeld is dat van een deur: hetzelfde hout, maar de beweging draait op dat ene punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet uitleggen waarom de Guldensporenslag tot het politieke én het sociale domein hoort. Wat doe je?",
        opties=[
            "je toont dat het om macht ging én om de verhouding tussen bevolkingsgroepen",
            "je zoekt op in welk jaar de slag plaatsvond en in welk seizoen dat viel",
            "je bepaalt of de bron waarin je erover leest primair of secundair is",
            "je zet de slag op een tijdlijn tussen twee andere veldslagen uit die eeuw",
        ],
        antwoord=0,
        uitleg="Situeren in domeinen betekent dat je per domein zegt wát er speelde, niet alleen dát het erbij hoort.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een gebeurtenis tegelijk situeren in de tijd, in de ruimte en in de maatschappelijke domeinen.",
        antwoord=True,
        uitleg="Dat is precies wat het referentiekader vraagt: drie assen, één gebeurtenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je de westerse periodisering met andere periodiseringen?",
        opties=[
            "om te zien dat elke indeling steunt op een keuze van kenmerken",
            "om te bewijzen dat de westerse indeling de beste van allemaal is",
            "om de jaartallen van de westerse indeling makkelijker te onthouden",
            "om het aantal periodes in elke indeling tot precies zeven terug te brengen",
        ],
        antwoord=0,
        uitleg="Naast elkaar gelegd zie je pas wát er gekozen is en wat daardoor buiten beeld valt.",
    ),
    dict(
        type="waarofniet",
        vraag="Hetzelfde jaartal kan in de ene periodisering een grens zijn en in de andere niet.",
        antwoord=True,
        uitleg="1492 is in de westerse indeling een scharnierpunt en in een Chinese indeling een gewoon jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze vier is géén maatschappelijk domein?",
        opties=[
            "het geografische domein",
            "het culturele domein",
            "het politieke domein",
            "het economische domein",
        ],
        antwoord=0,
        uitleg="De vier zijn cultureel, economisch, politiek en sociaal. Geografie is een vak, geen domein binnen dit kader.",
    ),
]

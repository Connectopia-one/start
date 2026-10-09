# -*- coding: utf-8 -*-
"""Socialisatie: posities, rollen en vier visies.

Het eerste van vijf thema's over sociale wetenschappen. Dat blok weegt
vijfentwintig procent van het examen. Waar gedragswetenschappen naar één mens
kijkt, kijkt dit blok naar de samenleving waarin die mens staat.

De lijstjes staan letterlijk in de fiche:

    sociologische begrippen: sociale positie, sociale rol, sociale status,
        macht
    vormen van socialisatie: primaire, secundaire en tertiaire socialisatie
    visies over socialisatie
        Emile Durkheim: de invloed van instituties op het vormen van het
            individu
        George Herbert Mead: het symbolisch interactionisme
        Talcott Parsons: het functionalisme
        Robert K. Merton: zijn bijdrage aan de referentiegroepentheorie

De drie vormen van socialisatie lopen gelijk met de drie opvoedingsmilieus uit
de pedagogiek: eerst het gezin, dan school en werk, dan de rest. Dat verband is
hier een vraag.

Deel 1 zijn de sociologische begrippen en de drie vormen van socialisatie.
Deel 2 zijn de vier visies.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is socialisatie?",
        opties=[
            "het proces waarin iemand de normen van zijn omgeving opneemt",
            "het proces waarin iemand lichamelijk opgroeit",
            "het proces waarin iemand vrienden maakt",
            "het proces waarin een groep beslissingen neemt",
        ],
        antwoord=0,
        uitleg="Socialiseren is lid worden van een samenleving: haar taal, haar regels en haar gewoonten tot de jouwe maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een sociale positie?",
        opties=[
            "de plaats die iemand in een geheel inneemt",
            "het gedrag dat van iemand verwacht wordt",
            "het aanzien dat aan een plaats hangt",
            "de mogelijkheid om anderen te doen gehoorzamen",
        ],
        antwoord=0,
        uitleg="Een sociale positie is een plaats: leerling, ouder, werknemer, buur. Bij elke positie hoort een rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een sociale rol?",
        opties=[
            "het gedrag dat bij een positie verwacht wordt",
            "de plaats die iemand in een geheel inneemt",
            "het aanzien dat aan een positie hangt",
            "de macht die iemand over anderen heeft",
        ],
        antwoord=0,
        uitleg="De positie is de plaats, de rol is het gedrag dat erbij hoort. Van een leerkracht wordt iets anders verwacht dan van een leerling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een sociale status?",
        opties=[
            "het aanzien dat aan een positie verbonden is",
            "de plaats die iemand in een geheel inneemt",
            "het gedrag dat bij een positie hoort",
            "het inkomen dat bij een beroep hoort",
        ],
        antwoord=0,
        uitleg="Status is hoe hoog een positie in de ogen van anderen staat. Twee beroepen met hetzelfde loon kunnen een heel andere status hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is macht in de sociologie?",
        opties=[
            "de mogelijkheid om anderen iets te doen doen",
            "het aanzien dat iemand bij anderen heeft",
            "de plaats die iemand in een geheel inneemt",
            "het gedrag dat van iemand verwacht wordt",
        ],
        antwoord=0,
        uitleg="Macht is kunnen doorwegen op wat anderen doen, ook als zij iets anders zouden willen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hanne is thuis dochter, op school leerling en in de jeugdbeweging leidster. Welk begrip past hierbij?",
        opties=[
            "iemand heeft meerdere sociale posities tegelijk",
            "iemand heeft maar één sociale positie",
            "iemand heeft bij elke positie dezelfde rol",
            "iemand heeft bij elke positie dezelfde status",
        ],
        antwoord=0,
        uitleg="Elke mens bezet verschillende posities, elk met een eigen rol. Soms botsen die rollen met elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Het aanzien dat aan een plaats in de samenleving hangt, heet de sociale ...",
        antwoord=["status"],
        uitleg="De sociale status. De plaats zelf is de sociale positie, en het verwachte gedrag de sociale rol.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sociale rol wordt niet door de persoon zelf bepaald maar door wat zijn omgeving verwacht.",
        antwoord=True,
        uitleg="Waar. Daarom is een rol sociaal: de verwachting komt van buiten, ook al vult iedereen een rol een beetje anders in.",
    ),
    dict(
        type="waarofniet",
        vraag="Sociale positie en sociale status betekenen hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. De positie is de plaats, de status is het aanzien van die plaats. Ze staan als twee aparte begrippen in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is primaire socialisatie?",
        opties=[
            "de eerste socialisatie, in het gezin",
            "de socialisatie op school en op het werk",
            "de socialisatie door media en vrije tijd",
            "de socialisatie bij een verhuis naar een ander land",
        ],
        antwoord=0,
        uitleg="De primaire socialisatie gebeurt in het gezin: de taal, de basisregels en de eerste gewoonten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is secundaire socialisatie?",
        opties=[
            "de socialisatie op school, op het werk en in verenigingen",
            "de socialisatie in het gezin van herkomst",
            "de socialisatie door reclame en sociale media",
            "de socialisatie die nooit meer verandert",
        ],
        antwoord=0,
        uitleg="Buiten het gezin leer je de regels van instellingen: wat mag in een klas, wat hoort op een werkvloer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is tertiaire socialisatie?",
        opties=[
            "de socialisatie door media, vrije tijd en publieke ruimte",
            "de socialisatie in het gezin van herkomst",
            "de socialisatie op school en op het werk",
            "de socialisatie die enkel bij kinderen voorkomt",
        ],
        antwoord=0,
        uitleg="De tertiaire socialisatie komt van buiten de instellingen: wat je ziet op een scherm, op straat en bij vrienden vormt je ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een negentienjarige begint te werken en leert op twee weken hoe het er in dat bedrijf aan toe gaat. Welke vorm van socialisatie is dit?",
        opties=[
            "secundaire socialisatie",
            "primaire socialisatie",
            "tertiaire socialisatie",
            "geen van de drie",
        ],
        antwoord=0,
        uitleg="Een bedrijf is een instelling met eigen regels. De regels van zo'n instelling leren, is secundaire socialisatie.",
    ),
    dict(
        type="invultekst",
        vraag="De socialisatie die in het gezin gebeurt, heet de ... socialisatie.",
        antwoord=["primaire", "primair"],
        uitleg="De primaire socialisatie. Daarna komen de secundaire en de tertiaire.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie vormen van socialisatie lopen gelijk met de drie opvoedingsmilieus uit de pedagogiek.",
        antwoord=True,
        uitleg="Waar. Primair is het gezin, secundair zijn de instellingen zoals school en werk, tertiair is de rest: media, buurt, vrije tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Socialisatie stopt volgens de fiche aan het einde van de adolescentie.",
        antwoord=False,
        uitleg="Niet waar. Bij elke nieuwe positie, zoals een eerste baan of het ouderschap, komt er socialisatie bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer is op kantoor afdelingshoofd en in zijn sportclub gewoon lid. Welke begrippen tonen dit het best?",
        opties=[
            "de sociale positie",
            "de sociale rol",
            "de macht",
            "de primaire socialisatie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Twee posities, twee rollen, en in de ene positie meer macht dan in de andere. Dat is precies het nut van de drie begrippen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om positie, rol, status en macht apart te houden?",
        opties=[
            "omdat ze niet altijd samen stijgen of dalen",
            "omdat ze bij elke mens precies gelijk zijn",
            "omdat ze elk bij een andere leeftijd horen",
            "omdat er altijd maar één van toepassing is",
        ],
        antwoord=0,
        uitleg="Een beroep kan veel status hebben en weinig macht, of omgekeerd. Door de begrippen te splitsen, zie je dat verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een rolconflict?",
        opties=[
            "twee rollen van dezelfde persoon vragen iets anders",
            "twee personen willen dezelfde rol opnemen",
            "een rol past niet bij de status van de positie",
            "een rol wordt door de omgeving niet erkend",
        ],
        antwoord=0,
        uitleg="Wie tegelijk leidster en examenstudent is, kan niet overal zijn. De verwachtingen van twee rollen botsen dan.",
    ),
    dict(
        type="invultekst",
        vraag="Het gedrag dat van iemand in een bepaalde plaats verwacht wordt, heet zijn sociale ...",
        antwoord=["rol"],
        uitleg="De sociale rol. De plaats zelf is de positie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel visies over socialisatie noemt de fiche bij naam?",
        opties=[
            "vier",
            "drie",
            "twee",
            "vijf",
        ],
        antwoord=0,
        uitleg="Vier: Durkheim, Mead, Parsons en Merton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar legt Emile Durkheim de nadruk op?",
        opties=[
            "op de invloed van instituties op het individu",
            "op de betekenis die mensen samen maken",
            "op de groep waarmee iemand zich vergelijkt",
            "op de biologische kant van de mens",
        ],
        antwoord=0,
        uitleg="Bij Durkheim vormen de instellingen van een samenleving, zoals school, kerk en recht, het individu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke visie hoort in de fiche bij George Herbert Mead?",
        opties=[
            "het symbolisch interactionisme",
            "het functionalisme",
            "de referentiegroepentheorie",
            "het conflictsociologisch perspectief",
        ],
        antwoord=0,
        uitleg="Mead. Zijn symbolisch interactionisme zegt dat het zelf ontstaat in de omgang met anderen, via gedeelde symbolen zoals taal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent symbolisch interactionisme?",
        opties=[
            "mensen vormen zichzelf in de omgang via gedeelde symbolen",
            "mensen worden gevormd door de instellingen boven hen",
            "mensen vergelijken zich met een groep van buitenaf",
            "mensen reageren alleen op belonen en straffen",
        ],
        antwoord=0,
        uitleg="Interactie en symbolen, taal op de eerste plaats. In het gesprek met anderen leer je zien wie jij bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke visie hoort in de fiche bij Talcott Parsons?",
        opties=[
            "het functionalisme",
            "het symbolisch interactionisme",
            "de referentiegroepentheorie",
            "de epigenetica",
        ],
        antwoord=0,
        uitleg="Parsons. Het functionalisme kijkt naar de functie die socialisatie voor het geheel heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van het functionalisme van Parsons?",
        opties=[
            "socialisatie houdt de samenleving aan het werk",
            "socialisatie is een strijd tussen groepen",
            "socialisatie gebeurt alleen in gesprekken",
            "socialisatie heeft geen enkel nut",
        ],
        antwoord=0,
        uitleg="Voor Parsons heeft elk deel van de samenleving een functie. Socialisatie zorgt dat mensen de rollen opnemen die nodig zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee droeg Robert K. Merton volgens de fiche bij?",
        opties=[
            "met de referentiegroepentheorie",
            "met het symbolisch interactionisme",
            "met het bio-ecologisch model",
            "met de rijpingstheorie",
        ],
        antwoord=0,
        uitleg="Merton. Een referentiegroep is de groep waaraan iemand zich spiegelt, ook als hij er geen lid van is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een referentiegroep?",
        opties=[
            "de groep waarmee iemand zich vergelijkt",
            "de groep waarvan iemand lid is",
            "de groep die een instelling bestuurt",
            "de groep met de hoogste status",
        ],
        antwoord=0,
        uitleg="Je referentiegroep is je meetlat. Een leerling die zich met studenten geneeskunde vergelijkt, legt zijn lat daar.",
    ),
    dict(
        type="invultekst",
        vraag="De visie van George Herbert Mead heet het symbolisch ...",
        antwoord=["interactionisme"],
        uitleg="Het symbolisch interactionisme. De naam zegt het: symbolen en interactie.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Merton kan iemand zich spiegelen aan een groep waarvan hij geen lid is.",
        antwoord=True,
        uitleg="Waar. Dat is net de kracht van het begrip: je meetlat hoeft niet je eigen groep te zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Durkheim en Mead geven precies dezelfde verklaring voor socialisatie.",
        antwoord=False,
        uitleg="Niet waar. Durkheim kijkt van boven naar beneden, naar de instellingen. Mead kijkt van onder naar boven, naar de omgang tussen mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker legt uit hoe het leerplichtonderwijs van een land zijn burgers vormt. Bij welke visie sluit dat het best aan?",
        opties=[
            "bij Durkheim, met de invloed van instituties",
            "bij Mead, met het symbolisch interactionisme",
            "bij Merton, met de referentiegroepen",
            "bij Bandura, met het imitatieleren",
        ],
        antwoord=0,
        uitleg="Het onderwijs is een institutie. Hoe die het individu vormt, is precies wat Durkheim onderzoekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker bekijkt hoe kinderen in hun spel leren wat van hen verwacht wordt. Bij welke visie sluit dat het best aan?",
        opties=[
            "bij Mead, met het symbolisch interactionisme",
            "bij Parsons, met het functionalisme",
            "bij Durkheim, met de instituties",
            "bij Merton, met de referentiegroepen",
        ],
        antwoord=0,
        uitleg="In het spel nemen kinderen rollen op en kijken ze door de ogen van de ander. Dat is de kern van Mead.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker vraagt zich af welke functie het gezin voor de samenleving als geheel heeft. Bij welke visie sluit dat aan?",
        opties=[
            "bij Parsons, met het functionalisme",
            "bij Mead, met de interactie",
            "bij Merton, met de referentiegroepen",
            "bij Vygotsky, met de scaffolding",
        ],
        antwoord=0,
        uitleg="De vraag naar de functie van een deel voor het geheel is de vraag van het functionalisme.",
    ),
    dict(
        type="invultekst",
        vraag="De visie van Talcott Parsons, die naar de functie van elk deel voor het geheel kijkt, heet het ...",
        antwoord=["functionalisme"],
        uitleg="Het functionalisme. Het staat in de fiche ook terug bij de verklaringsmodellen voor sociale stratificatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke visies kijken vooral van de samenleving naar het individu, van boven naar beneden?",
        opties=[
            "die van Durkheim",
            "die van Parsons",
            "die van Mead",
            "die van Dweck",
        ],
        antwoord=[0, 1],
        uitleg="Durkheim en Parsons vertrekken van de samenleving. Mead vertrekt bij de omgang tussen mensen.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche vraagt om de visies over socialisatie met elkaar te vergelijken en de gelijkenissen en verschillen te benoemen.",
        antwoord=True,
        uitleg="Waar. Dat staat er met zoveel woorden, naast het leggen van verbanden met onderzoek uit aangereikte bronnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een referentiegroep is volgens Merton altijd de groep met de hoogste status in een samenleving.",
        antwoord=False,
        uitleg="Niet waar. Het is de groep waaraan iemand zichzelf afmeet. Dat kan ook de buurt of de ploeg van zijn vader zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar tegen een zuiver functionalistische visie op socialisatie?",
        opties=[
            "ze verklaart moeilijk waarom mensen tegen de orde ingaan",
            "ze verklaart moeilijk waarom mensen de orde volgen",
            "ze laat de samenleving volledig buiten beschouwing",
            "ze werkt niet met sociale posities en rollen",
        ],
        antwoord=0,
        uitleg="Als elk deel een nuttige functie heeft, is verzet een stoornis. Juist daarom staat er in dit vak ook een conflictsociologisch perspectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn vier visies nuttiger dan één?",
        opties=[
            "omdat elke visie een ander stuk van de werkelijkheid vat",
            "omdat drie van de vier achterhaald zijn",
            "omdat je er op het examen moet kiezen welke juist is",
            "omdat ze samen precies hetzelfde zeggen",
        ],
        antwoord=0,
        uitleg="Instituties, interactie, functie en referentiegroep belichten elk iets anders. Samen leggen ze meer bloot dan elk apart.",
    ),
]

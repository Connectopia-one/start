# -*- coding: utf-8 -*-
"""Sociale stratificatie en de verklaringsmodellen.

Het tweede van vijf thema's over sociale wetenschappen. Stratificatie is de
gelaagdheid van een samenleving: wie staat waar, en waarom.

De lijstjes staan letterlijk in de fiche:

    stratificatiesystemen: slavenmaatschappij, kastenmaatschappij,
        standenmaatschappij, klassenmaatschappij
    conflictsociologisch perspectief: het verklaringsmodel van Marx (19de
        eeuw), van Weber (begin 20ste eeuw), van Dahrendorf (20ste eeuw) en
        van Bourdieu (20ste eeuw)
    functionalistisch perspectief: het verklaringsmodel van Davis en Moore
        (20ste eeuw)
    stratificatie vandaag: de EGP-klassenindeling van Goldthorpe en het belang
        van de sociaal-economische status

De fiche zet bij elk verklaringsmodel de eeuw. Die staan hieronder ook in de
vragen, want aan de orde van Marx, Weber, Dahrendorf en Bourdieu zie je hoe het
denken over klasse verschoven is: van bezit, over gezag, naar kapitaal in
verschillende vormen.

Deel 1 zijn het begrip en de vier stratificatiesystemen.
Deel 2 zijn de verklaringsmodellen, de EGP-indeling en de sociaal-economische
status.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is sociale stratificatie?",
        opties=[
            "de gelaagdheid van een samenleving in hogere en lagere plaatsen",
            "de verhuis van mensen van de ene streek naar een andere streek",
            "de verdeling van een samenleving in leeftijdsgroepen",
            "de samenwerking tussen groepen in een samenleving",
        ],
        antwoord=0,
        uitleg="Stratum betekent laag. Stratificatie is de ongelijke verdeling van geld, aanzien en macht over lagen in een samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier stratificatiesystemen noemt de fiche?",
        opties=[
            "de slavenmaatschappij",
            "de kastenmaatschappij",
            "de standenmaatschappij",
            "de kennismaatschappij",
            "de welvaartsmaatschappij",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier zijn slaven-, kasten-, standen- en klassenmaatschappij. De kennis- en welvaartsmaatschappij staan niet in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een slavenmaatschappij?",
        opties=[
            "een deel van de mensen is eigendom van anderen",
            "iedereen erft de laag waarin hij geboren is",
            "er zijn drie standen met eigen rechten",
            "iemands laag hangt af van zijn beroep",
        ],
        antwoord=0,
        uitleg="In een slavenmaatschappij is een groep mensen juridisch bezit van anderen. Dat is de scherpste vorm van ongelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een kastenmaatschappij?",
        opties=[
            "je laag ligt bij de geboorte vast en verandert niet",
            "je laag hangt af van je opleiding en van je werk",
            "je laag hangt af van je bezit en je inkomen",
            "je laag hangt af van je leeftijd",
        ],
        antwoord=0,
        uitleg="In een kastenmaatschappij erf je je plaats en blijf je er je hele leven in. Er is bijna geen mobiliteit mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een standenmaatschappij?",
        opties=[
            "er zijn standen met elk eigen rechten en plichten",
            "er zijn geen verschillen in rechten tussen groepen",
            "iedereen is eigendom van iemand anders",
            "iemands plaats hangt enkel af van zijn inkomen",
        ],
        antwoord=0,
        uitleg="Een standenmaatschappij heeft groepen met een eigen rechtspositie, zoals adel, geestelijkheid en de derde stand voor de Franse Revolutie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een klassenmaatschappij?",
        opties=[
            "je plaats hangt vooral samen met je positie in de economie",
            "je plaats ligt bij je geboorte volledig en blijvend vast",
            "je plaats hangt af van je stand in het recht",
            "er zijn helemaal geen lagen meer",
        ],
        antwoord=0,
        uitleg="In een klassenmaatschappij is de wet voor iedereen gelijk, maar bepaalt je plaats in de economie waar je terechtkomt. Daarom gaan alle verklaringsmodellen hierover.",
    ),
    dict(
        type="invultekst",
        vraag="Het stratificatiesysteem waarin je laag bij de geboorte vastligt en nooit verandert, is de ...maatschappij.",
        antwoord=["kasten", "kastenmaatschappij"],
        uitleg="De kastenmaatschappij. In een klassenmaatschappij is er wel beweging mogelijk, al is ze beperkt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een klassenmaatschappij is beweging tussen de lagen mogelijk, al is ze niet voor iedereen even gemakkelijk.",
        antwoord=True,
        uitleg="Waar. Dat verschil met de kastenmaatschappij maakt het onderwerp van het volgende thema mogelijk: de sociale mobiliteit.",
    ),
    dict(
        type="waarofniet",
        vraag="In een standenmaatschappij hebben alle groepen precies dezelfde rechten.",
        antwoord=False,
        uitleg="Niet waar. Juist niet: elke stand heeft eigen rechten en plichten. Dat is wat een stand onderscheidt van een klasse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een samenleving kent adel met eigen rechtbanken, geestelijken die geen belasting betalen en boeren en burgers die wel betalen. Welk systeem is dit?",
        opties=[
            "een standenmaatschappij",
            "een kastenmaatschappij",
            "een klassenmaatschappij",
            "een slavenmaatschappij",
        ],
        antwoord=0,
        uitleg="Verschillende rechten per groep, vastgelegd in het recht: dat is een standenmaatschappij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt de fiche de hedendaagse westerse samenleving een klassenmaatschappij?",
        opties=[
            "omdat de wet gelijk is maar de kansen verschillen",
            "omdat elke laag een eigen rechtspositie heeft",
            "omdat iemands plaats bij de geboorte vastligt",
            "omdat er geen enkele ongelijkheid meer bestaat",
        ],
        antwoord=0,
        uitleg="Formeel is iedereen gelijk voor de wet. De verschillen zitten in bezit, opleiding, beroep en netwerk, en die wegen zwaar door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee perspectieven onderscheidt de fiche om stratificatie in een klassenmaatschappij te verklaren?",
        opties=[
            "het conflictsociologisch perspectief",
            "het functionalistisch perspectief",
            "het symbolisch interactionisme",
            "het biologisch perspectief",
        ],
        antwoord=[0, 1],
        uitleg="Het conflictsociologisch perspectief, met Marx, Weber, Dahrendorf en Bourdieu, en het functionalistisch perspectief, met Davis en Moore.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van het conflictsociologisch perspectief op stratificatie?",
        opties=[
            "ongelijkheid komt uit een strijd tussen groepen",
            "ongelijkheid is nodig om de samenleving te laten werken",
            "ongelijkheid bestaat niet meer in onze tijd",
            "ongelijkheid hangt enkel van talent af",
        ],
        antwoord=0,
        uitleg="Volgens dit perspectief houdt een groep met macht haar voordeel in stand ten koste van een andere groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van het functionalistisch perspectief op stratificatie?",
        opties=[
            "ongelijkheid heeft een nut voor het geheel",
            "ongelijkheid is het gevolg van een strijd",
            "ongelijkheid is een fout die verdwijnt",
            "ongelijkheid komt alleen uit erfenis",
        ],
        antwoord=0,
        uitleg="Volgens Davis en Moore moeten belangrijke en moeilijke functies beter belonen, zodat de geschikte mensen zich aanbieden.",
    ),
    dict(
        type="invultekst",
        vraag="Het perspectief dat ongelijkheid verklaart als een strijd tussen groepen, heet het ...sociologisch perspectief.",
        antwoord=["conflict", "conflictsociologisch"],
        uitleg="Het conflictsociologisch perspectief. Daartegenover staat het functionalistisch perspectief.",
    ),
    dict(
        type="waarofniet",
        vraag="Het conflictsociologische en het functionalistische perspectief geven een verschillend antwoord op de vraag of ongelijkheid nuttig is.",
        antwoord=True,
        uitleg="Waar. Dat is net het grote verschil: het ene ziet nut voor het geheel, het andere een voordeel voor één groep.",
    ),
    dict(
        type="waarofniet",
        vraag="De vier conflictsociologische verklaringsmodellen van de fiche komen alle vier uit de negentiende eeuw.",
        antwoord=False,
        uitleg="Niet waar. Alleen Marx staat in de fiche bij de negentiende eeuw. Weber, Dahrendorf en Bourdieu staan in de twintigste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet de fiche bij elk verklaringsmodel de eeuw?",
        opties=[
            "omdat je zo ziet hoe het denken over klasse verschoven is",
            "omdat de oudste modellen vandaag niet meer zouden gelden",
            "omdat je de eeuw op het examen moet opsommen",
            "omdat elke eeuw maar één model toelaat",
        ],
        antwoord=0,
        uitleg="Marx kijkt naar bezit, Weber voegt status en macht toe, Dahrendorf kijkt naar gezag en Bourdieu naar verschillende soorten kapitaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een stand en een klasse?",
        opties=[
            "een stand staat in het recht, een klasse in de economie",
            "een klasse staat in het recht, een stand in de economie",
            "een stand is groter dan een klasse",
            "een klasse erf je, een stand niet",
        ],
        antwoord=0,
        uitleg="Standen hebben eigen rechten en plichten die in de wet staan. Klassen zijn verschillen in positie zonder verschil in recht.",
    ),
    dict(
        type="invultekst",
        vraag="Het Latijnse woord achter stratificatie betekent ...",
        antwoord=["laag", "lagen"],
        uitleg="Stratum betekent laag. Stratificatie is dus letterlijk het in lagen verdelen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarop baseert Marx zijn indeling in klassen?",
        opties=[
            "op het bezit van de productiemiddelen",
            "op het gezag binnen een organisatie",
            "op het aanzien van een beroep",
            "op het aantal jaren opleiding",
        ],
        antwoord=0,
        uitleg="Bij Marx is er een klasse die de fabrieken en de grond bezit en een klasse die haar arbeid moet verkopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voegt Weber toe aan de klassenindeling van Marx?",
        opties=[
            "naast bezit ook status en macht",
            "naast bezit ook leeftijd en gender",
            "naast bezit ook woonplaats en taal",
            "niets, hij neemt Marx volledig over",
        ],
        antwoord=0,
        uitleg="Weber werkt met meerdere assen. Iemand kan weinig bezit en veel aanzien hebben, of omgekeerd. Dat kan bij Marx niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop baseert Dahrendorf zijn klassenindeling?",
        opties=[
            "op wie binnen een organisatie gezag heeft",
            "op wie de productiemiddelen bezit",
            "op welke soorten kapitaal iemand heeft",
            "op hoe nuttig een functie voor het geheel is",
        ],
        antwoord=0,
        uitleg="Dahrendorf verschuift de vraag van bezit naar gezag: wie geeft bevelen en wie krijgt ze, ook in een organisatie die niemand bezit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke soorten kapitaal werkt Bourdieu?",
        opties=[
            "economisch kapitaal",
            "cultureel kapitaal",
            "sociaal kapitaal",
            "juridisch kapitaal",
        ],
        antwoord=[0, 1, 2],
        uitleg="Geld en bezit, kennis en omgangsvormen, en je netwerk. Volgens Bourdieu kan het ene kapitaal in het andere omgezet worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is cultureel kapitaal bij Bourdieu?",
        opties=[
            "kennis, taal en omgangsvormen die ergens voordeel geven",
            "het geld en het bezit waarover iemand beschikt",
            "het netwerk van mensen dat iemand kan inzetten als het nodig is",
            "het aantal jaren dat iemand gewerkt heeft",
        ],
        antwoord=0,
        uitleg="Wie thuis de taal van de school meekrijgt, heeft op school een voorsprong. Dat is cultureel kapitaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling krijgt via de vrienden van zijn ouders een stageplaats die niet werd bekendgemaakt. Welk kapitaal werkt hier?",
        opties=[
            "sociaal kapitaal",
            "economisch kapitaal",
            "cultureel kapitaal",
            "geen van de drie",
        ],
        antwoord=0,
        uitleg="Het netwerk levert hier het voordeel op. Bij Bourdieu is dat sociaal kapitaal.",
    ),
    dict(
        type="invultekst",
        vraag="De drie soorten kapitaal van Bourdieu zijn het economische, het sociale en het ... kapitaal.",
        antwoord=["culturele", "cultureel"],
        uitleg="Het culturele kapitaal: kennis, taal, smaak en omgangsvormen die ergens voordeel opleveren.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Bourdieu kan het ene soort kapitaal in het andere omgezet worden.",
        antwoord=True,
        uitleg="Waar. Geld kan in opleiding gaan, een netwerk in een baan, en een diploma weer in geld. Juist daardoor blijft ongelijkheid in stand.",
    ),
    dict(
        type="waarofniet",
        vraag="Marx, Weber, Dahrendorf en Bourdieu geven alle vier precies dezelfde verklaring voor klasse.",
        antwoord=False,
        uitleg="Niet waar. Bezit bij Marx, meerdere assen bij Weber, gezag bij Dahrendorf en soorten kapitaal bij Bourdieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zeggen Davis en Moore over ongelijke belonen?",
        opties=[
            "belangrijke, moeilijke functies moeten meer opbrengen",
            "alle functies moeten precies gelijk belonen",
            "belonen heeft met stratificatie helemaal niets te maken",
            "belonen moet afhangen van de afkomst",
        ],
        antwoord=0,
        uitleg="Volgens hen is dat nodig om mensen aan te zetten tot de lange opleiding en de verantwoordelijkheid die zulke functies vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar tegen het model van Davis en Moore?",
        opties=[
            "niet iedereen krijgt dezelfde kans op zo'n functie",
            "zij kijken enkel naar het bezit van productiemiddelen",
            "zij ontkennen dat er ongelijkheid bestaat",
            "zij werken niet met beroepen of functies",
        ],
        antwoord=0,
        uitleg="Het model veronderstelt dat de geschiktste mensen bovenkomen. Wie geen kans krijgt om zich te bewijzen, valt daar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop is de EGP-klassenindeling van Goldthorpe gebaseerd?",
        opties=[
            "op het beroep en de arbeidsverhouding van mensen",
            "op het inkomen en het bezit van mensen alleen",
            "op de opleiding van de ouders",
            "op de buurt waar iemand woont",
        ],
        antwoord=0,
        uitleg="De EGP-indeling kijkt naar wat iemand doet en onder welke voorwaarden: in loondienst of zelfstandig, met of zonder gezag, vast of los.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de sociaal-economische status van iemand doorgaans?",
        opties=[
            "uit inkomen, opleiding en beroep samen",
            "uit inkomen alleen",
            "uit opleiding alleen",
            "uit het inkomen en de leeftijd samen",
        ],
        antwoord=0,
        uitleg="De sociaal-economische status vat die drie samen. Daarom is ze zo sterk met gezondheid en schoolresultaat verbonden.",
    ),
    dict(
        type="invultekst",
        vraag="De afkorting voor de maat die inkomen, opleiding en beroep samenvat, is ...",
        antwoord=["SES", "ses"],
        uitleg="SES, de sociaal-economische status. De fiche noemt het belang ervan uitdrukkelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De sociaal-economische status van een gezin hangt samen met de schoolresultaten van de kinderen.",
        antwoord=True,
        uitleg="Waar. Dat verband is in heel veel onderzoek teruggevonden, en het staat aan de basis van het volgende thema over kansenongelijkheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De EGP-indeling en de klassen van Marx zijn twee namen voor dezelfde indeling.",
        antwoord=False,
        uitleg="Niet waar. Marx werkt met twee klassen op basis van bezit. De EGP-indeling werkt met meerdere groepen op basis van beroep en arbeidsverhouding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker vergelijkt twee scholen en vindt dat het verschil in resultaat vooral samenhangt met de thuissituatie van de leerlingen. Welk begrip gebruikt hij?",
        opties=[
            "de sociaal-economische status",
            "de EGP-klassenindeling",
            "de referentiegroep",
            "het stratificatiesysteem",
        ],
        antwoord=0,
        uitleg="Inkomen, opleiding en beroep van de ouders samen vormen de sociaal-economische status van een gezin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een manager zonder aandelen geeft leiding aan driehonderd mensen. Welk model legt zijn klasse het best uit?",
        opties=[
            "het model van Dahrendorf, met het gezag",
            "het model van Marx, met het bezit",
            "het model van Davis en Moore, met de functie",
            "de EGP-indeling, met de opleiding",
        ],
        antwoord=0,
        uitleg="Bij Marx zou hij geen bezitter zijn en dus bij de arbeiders horen. Dahrendorf lost dat op door naar gezag te kijken in plaats van bezit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vraagt de fiche om met de verklaringsmodellen te doen?",
        opties=[
            "ze vergelijken en de gelijkenissen en verschillen benoemen",
            "er een uitkiezen en de andere verwerpen",
            "ze alle vijf uit het hoofd opsommen met hun jaartal erbij",
            "ze op één van de drie basisvragen toepassen",
        ],
        antwoord=0,
        uitleg="De fiche vraagt vergelijken, en onderzoek vergelijken op de oorsprong, de mechanismen en de gevolgen van stratificatie.",
    ),
    dict(
        type="invultekst",
        vraag="Het verklaringsmodel dat ongelijkheid nuttig vindt voor het geheel, is van Davis en ...",
        antwoord=["Moore"],
        uitleg="Davis en Moore, het enige functionalistische model in de lijst van de fiche.",
    ),
]

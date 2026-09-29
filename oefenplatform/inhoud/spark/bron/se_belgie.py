# -*- coding: utf-8 -*-
"""De vragen voor "Hoe België bestuurd wordt" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik leef in een democratische
rechtsstaat" (15 % van het examen), tweede helft: de vier bestuursniveaus met
hun organen en hun bevoegdheden. De principes van de rechtsstaat staan in
[[se_democratie]].

Deel 1 gaat over de gemeente en de provincie, deel 2 over de gemeenschappen en
gewesten en over de federale overheid. In beide delen komt telkens terug wie de
wetgevende en wie de uitvoerende macht is op dat niveau, want dat is wat de
fiche vraagt te kunnen toepassen.

LET OP BIJ HET AANVULLEN. De bevoegdheden schuiven in België om de zoveel jaar
op door een staatshervorming. Wat hier staat, is de toestand zoals de vakfiche
ze beschrijft. Wie hier iets bijschrijft, kijkt dat na in de fiche zelf en niet
uit het hoofd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke bestuursniveaus zijn er in België?",
        opties=[
            "De gemeente of stad",
            "De provincie",
            "De gemeenschappen en de gewesten",
            "De federale overheid",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="België wordt op vier niveaus bestuurd: de gemeente, de provincie, de gemeenschappen en gewesten, en de federale overheid. Elk niveau heeft zijn eigen bevoegdheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bestuursniveau dat het dichtst bij de inwoners staat?",
        opties=[
            "De gemeente of stad",
            "De provincie waarin je woont",
            "Het gewest waarin je woont",
            "De federale overheid van het land",
        ],
        antwoord=0,
        uitleg="De gemeente is het kleinste bestuursniveau en dus het dichtst bij. Daar ga je voor je identiteitskaart, je huisvuil en je bouwvergunning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie vormen samen het dagelijks bestuur van een gemeente?",
        opties=[
            "De burgemeester en de schepenen",
            "De gemeenteraadsleden die verkozen raakten",
            "De provinciegouverneur en zijn medewerkers",
            "De ministers die bevoegd zijn voor die streek",
        ],
        antwoord=0,
        uitleg="Het college van burgemeester en schepenen is het dagelijks bestuur van de gemeente. Dat is daar de uitvoerende macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de gemeenteraad?",
        opties=[
            "Hij neemt de beslissingen en keurt de regels van de gemeente goed",
            "Hij voert elke dag uit wat de burgemeester beslist heeft voor de gemeente",
            "Hij spreekt recht als twee inwoners ruzie hebben",
            "Hij benoemt de gouverneur van de provincie",
        ],
        antwoord=0,
        uitleg="De gemeenteraad is op gemeentelijk niveau de wetgevende macht: hij beslist en keurt goed. Het college voert uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De leden van de gemeenteraad worden verkozen door de inwoners van de gemeente.",
        antwoord=True,
        uitleg="Klopt. Bij de gemeenteraadsverkiezingen kiezen de inwoners wie in de gemeenteraad zetelt. Uit die raad komt daarna het college.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor ga je naar het gemeentehuis?",
        opties=[
            "Voor een nieuwe identiteitskaart",
            "Voor een bouwvergunning",
            "Om je te laten inschrijven als je verhuist",
            "Om je paspoort te laten controleren aan de grens",
        ],
        antwoord=[0, 1, 2],
        uitleg="Identiteitskaarten, bouwvergunningen en het bevolkingsregister zijn zaken van de gemeente. Grenscontrole is dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken regelt de gemeente?",
        opties=[
            "Het ophalen van het huisvuil",
            "Het onderhoud van de straten in de gemeente",
            "De gemeentelijke basisschool",
            "De pensioenen van alle Belgen samen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Huisvuil, lokale wegen en de eigen scholen zijn gemeentelijke taken. Pensioenen worden federaal geregeld.",
    ),
    dict(
        type="waarofniet",
        vraag="De burgemeester wordt rechtstreeks door de inwoners verkozen tot burgemeester.",
        antwoord=False,
        uitleg="Je stemt op kandidaten voor de gemeenteraad. Wie daarna burgemeester wordt, hangt af van de meerderheid die gevormd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel provincies telt België?",
        opties=[
            "Tien",
            "Zes",
            "Negen",
            "Twaalf",
        ],
        antwoord=0,
        uitleg="Er zijn tien provincies: vijf in Vlaanderen en vijf in Wallonië. Het Brussels Hoofdstedelijk Gewest hoort bij geen enkele provincie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn Vlaamse provincies?",
        opties=[
            "Limburg",
            "Antwerpen",
            "Vlaams-Brabant",
            "Henegouwen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf Vlaamse provincies zijn Antwerpen, Limburg, Oost-Vlaanderen, West-Vlaanderen en Vlaams-Brabant. Henegouwen ligt in Wallonië.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Brussels Hoofdstedelijk Gewest ligt in een van de tien provincies.",
        antwoord=False,
        uitleg="Brussel hoort bij geen enkele provincie. Het is een gewest op zichzelf, met negentien gemeenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk orgaan neemt op provinciaal niveau de beslissingen?",
        opties=[
            "De provincieraad",
            "De deputatie van de provincie",
            "De gouverneur in zijn eentje",
            "Het college van burgemeester en schepenen",
        ],
        antwoord=0,
        uitleg="De provincieraad is de verkozen vergadering van de provincie en neemt daar de beslissingen. De deputatie voert ze uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie zorgt voor het dagelijks bestuur van een provincie?",
        opties=[
            "De deputatie, met de gouverneur als voorzitter",
            "De provincieraad die daarvoor elke week samenkomt",
            "De burgemeesters van alle gemeenten in de provincie",
            "De minister die bevoegd is voor binnenlands bestuur",
        ],
        antwoord=0,
        uitleg="De deputatie is het dagelijks bestuur van de provincie. De gouverneur zit die vergadering voor.",
    ),
    dict(
        type="waarofniet",
        vraag="De gouverneur van een provincie wordt benoemd en niet verkozen.",
        antwoord=True,
        uitleg="Klopt. De provincieraad wordt verkozen, maar de gouverneur wordt benoemd door de regering van het gewest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de taken van een provincie?",
        opties=[
            "Provinciale wegen en fietspaden",
            "Provinciale domeinen en natuurgebieden",
            "Provinciale scholen",
            "Het uitreiken van je identiteitskaart",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wegen, domeinen en eigen scholen op provinciaal niveau zijn provinciale taken. Je identiteitskaart krijg je bij de gemeente.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op elk bestuursniveau vind je dezelfde twee soorten organen terug. Welke?",
        opties=[
            "Een verkozen raad die beslist, en een bestuur dat uitvoert",
            "Een rechtbank die oordeelt, en een politie die optreedt",
            "Een gouverneur die leidt, en een secretaris die schrijft",
            "Een partij die regeert, en een partij die toekijkt",
        ],
        antwoord=0,
        uitleg="Overal is er een verkozen vergadering (de wetgevende kant) en een dagelijks bestuur (de uitvoerende kant). Alleen de namen verschillen.",
    ),
    dict(
        type="waarofniet",
        vraag="De gemeente en de provincie mogen elk hun eigen belastingen heffen.",
        antwoord=True,
        uitleg="Klopt. Naast de federale belastingen bestaan er ook gemeentelijke en provinciale opcentiemen en heffingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een carport bouwen naast je huis. Waar moet je daarvoor zijn?",
        opties=[
            "Bij je gemeente, voor een omgevingsvergunning",
            "Bij je provincie, want die gaat over gebouwen",
            "Bij het gewest, want dat gaat over ruimte",
            "Bij de federale overheid, want die gaat over wonen",
        ],
        antwoord=0,
        uitleg="Bouwen vraag je aan bij je gemeente. Het gewest maakt wel de regels, maar de aanvraag zelf loopt lokaal.",
    ),
    dict(
        type="waarofniet",
        vraag="De gemeenteraad en de provincieraad worden elk op een andere dag verkozen.",
        antwoord=False,
        uitleg="Ze vallen samen: de lokale en de provinciale verkiezingen zijn op dezelfde dag. Je krijgt die dag dus meer dan één stembiljet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het dagelijks bestuur van een gemeente, dat bestaat uit de burgemeester en de schepenen?",
        antwoord=["het college", "college", "het schepencollege", "schepencollege"],
        uitleg="Het college van burgemeester en schepenen is de uitvoerende macht van de gemeente.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel gemeenschappen en hoeveel gewesten telt België?",
        opties=[
            "Drie gemeenschappen en drie gewesten",
            "Twee gemeenschappen en drie gewesten",
            "Drie gemeenschappen en twee gewesten",
            "Vier gemeenschappen en vier gewesten",
        ],
        antwoord=0,
        uitleg="Er zijn drie gemeenschappen (de Vlaamse, de Franse en de Duitstalige) en drie gewesten (het Vlaamse, het Waalse en het Brussels Hoofdstedelijk Gewest).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover gaan de gemeenschappen?",
        opties=[
            "Over zaken die met personen en hun taal te maken hebben",
            "Over zaken die met het grondgebied te maken hebben",
            "Over zaken die het hele land tegelijk aanbelangen",
            "Over zaken die alleen in één gemeente spelen",
        ],
        antwoord=0,
        uitleg="Een gemeenschap is persoonsgebonden: ze gaat over mensen en hun taal. Een gewest is grondgebonden: dat gaat over het grondgebied.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bevoegdheden van een gemeenschap?",
        opties=[
            "Onderwijs",
            "Cultuur",
            "Welzijn en gezondheidszorg",
            "De aanleg van autosnelwegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onderwijs, cultuur, media en welzijn zijn persoonsgebonden en dus gemeenschapsmaterie. Wegen horen bij het gewest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bevoegdheden van een gewest?",
        opties=[
            "Milieu en natuur",
            "Ruimtelijke ordening en wonen",
            "Openbaar vervoer binnen het gewest",
            "De rechtbanken en de gevangenissen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Milieu, ruimtelijke ordening, wonen, economie en mobiliteit zijn grondgebonden en dus gewestmaterie. Justitie is federaal.",
    ),
    dict(
        type="waarofniet",
        vraag="In Vlaanderen zijn de gemeenschap en het gewest samengevoegd tot één parlement en één regering.",
        antwoord=True,
        uitleg="Klopt. Er is één Vlaams Parlement en één Vlaamse Regering die zowel de gemeenschaps- als de gewestbevoegdheden behartigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk niveau beslist over jouw schooldoelen en je diploma?",
        opties=[
            "De Vlaamse Gemeenschap",
            "De federale overheid van België",
            "De provincie waarin je school ligt",
            "De gemeente waarin je school ligt",
        ],
        antwoord=0,
        uitleg="Onderwijs is een gemeenschapsbevoegdheid. Voor Vlaanderen is dat de Vlaamse Gemeenschap, met haar eigen minister van Onderwijs.",
    ),
    dict(
        type="waarofniet",
        vraag="De Duitstalige Gemeenschap is een van de drie gemeenschappen van België.",
        antwoord=True,
        uitleg="Klopt. Naast de Vlaamse en de Franse Gemeenschap is er ook de Duitstalige Gemeenschap, in het oosten van de provincie Luik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk orgaan maakt de decreten van Vlaanderen?",
        opties=[
            "Het Vlaams Parlement",
            "De Vlaamse Regering",
            "De provincieraden samen",
            "De Kamer van volksvertegenwoordigers",
        ],
        antwoord=0,
        uitleg="Het Vlaams Parlement stemt de decreten. Dat zijn de wetten van de gemeenschap en het gewest, en ze gelden even sterk als een federale wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie voert in Vlaanderen uit wat het parlement beslist?",
        opties=[
            "De Vlaamse Regering met haar ministers",
            "Het Vlaams Parlement in een tweede stemming",
            "De gouverneurs van de vijf provincies",
            "De federale regering in Brussel",
        ],
        antwoord=0,
        uitleg="De Vlaamse Regering is de uitvoerende macht van Vlaanderen. Het parlement beslist, de regering voert uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken regelt de federale overheid?",
        opties=[
            "Justitie en de rechtbanken",
            "Defensie en het leger",
            "Asiel en migratie",
            "Het onderhoud van de gemeentelijke fietspaden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Justitie, defensie, asiel en migratie, pensioenen en buitenlandse handel zijn federaal. Lokale fietspaden zijn dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk niveau regelt de pensioenen?",
        opties=[
            "De federale overheid",
            "De gemeenschap waartoe je behoort",
            "Het gewest waarin je werkt",
            "De gemeente waarin je woont",
        ],
        antwoord=0,
        uitleg="Pensioenen horen bij de sociale zekerheid en die is federaal. Ze zijn dus voor het hele land hetzelfde geregeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minister hoort bij de wetgevende macht.",
        antwoord=False,
        uitleg="Een minister hoort bij de uitvoerende macht: hij of zij voert uit. Wie wetten stemt, is een volksvertegenwoordiger in het parlement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een volksvertegenwoordiger?",
        opties=[
            "Iemand die verkozen is om in het parlement mee wetten te stemmen",
            "Iemand die door de regering benoemd is om een dienst te leiden",
            "Iemand die als rechter uitspraak doet in naam van het volk",
            "Iemand die de bevolking vertegenwoordigt bij de gouverneur",
        ],
        antwoord=0,
        uitleg="Een volksvertegenwoordiger zetelt in het parlement en hoort dus bij de wetgevende macht. Hij of zij is verkozen door de kiezers.",
    ),
    dict(
        type="waarofniet",
        vraag="De federale overheid mag beslissen wat er in het Vlaamse onderwijs gebeurt.",
        antwoord=False,
        uitleg="Onderwijs is volledig een bevoegdheid van de gemeenschappen. De federale overheid gaat daar niet over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gezin verhuist naar een andere gemeente. Bij welke niveaus komt dat terecht?",
        opties=[
            "Bij de gemeente, voor je inschrijving in het bevolkingsregister",
            "Bij de federale overheid, want die beheert de identiteitsgegevens",
            "Bij de provincie, die elke verhuis binnen haar gebied moet goedkeuren",
            "Bij de gemeenschap, die je nieuwe school aanwijst",
        ],
        antwoord=[0, 1],
        uitleg="Je schrijft je in bij je nieuwe gemeente, en die past je federale identiteitsgegevens aan. De provincie komt er niet aan te pas, en je school kies je zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een decreet van het Vlaams Parlement heeft evenveel kracht als een federale wet.",
        antwoord=True,
        uitleg="Klopt. Binnen zijn eigen bevoegdheden is een decreet even sterk. Elk niveau is baas in wat het toegewezen kreeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over de koning van België klopt?",
        opties=[
            "Hij is het staatshoofd, maar bestuurt het land niet zelf",
            "Hij beslist welke wetten er gestemd worden",
            "Hij benoemt alle rechters van het land persoonlijk",
            "Hij wordt om de vijf jaar door de bevolking verkozen",
        ],
        antwoord=0,
        uitleg="De koning is staatshoofd en heeft vooral een symbolische rol. De echte beslissingen liggen bij het parlement en de regering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Er wordt beslist dat er een nieuw natuurgebied komt langs de Maas. Welk niveau is daarvoor bevoegd?",
        opties=[
            "Het gewest, want natuur is grondgebonden",
            "De gemeenschap, want natuur hoort bij cultuur",
            "De federale overheid, want de Maas loopt door het land",
            "De provincie, want die beheert alle waterlopen",
        ],
        antwoord=0,
        uitleg="Natuur en milieu horen bij het grondgebied en dus bij het gewest. Onthoud: gaat het over grond, dan is het gewest.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk bestuursniveau mag over alles beslissen wat het wil.",
        antwoord=False,
        uitleg="Elk niveau heeft zijn eigen lijst bevoegdheden. Buiten die lijst mag het niets beslissen, ook niet als het dat graag zou willen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de wet die een gemeenschap of een gewest stemt, en die geen wet maar anders heet?",
        antwoord=["een decreet", "decreet"],
        uitleg="Een decreet is de regelgeving van een gemeenschap of gewest. Binnen zijn bevoegdheden is die even sterk als een federale wet.",
    ),
]

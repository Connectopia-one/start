# -*- coding: utf-8 -*-
"""Humane wetenschappen: het recht in de samenleving.

Het vijfde van zes thema's over politieke wetenschappen, enkel voor humane
wetenschappen (fiche 3DDO, onderdeel "Het recht in de samenleving").

De lijstjes staan letterlijk in de fiche:

    functies van justitie: bestraffing, conflictbeslechting, ordehandhaving,
        preventie, veiligheid
    principes van de hedendaagse rechtspraak: hoor en wederhoor,
        onafhankelijkheid en onpartijdigheid van de rechters, openbaarheid,
        vermoeden van onschuld
    de gerechtelijke piramide en de bevoegdheden (territoriaal en materieel)
        van: vredegerecht, politierechtbank, rechtbanken van eerste aanleg
        (burgerlijke rechtbank, correctionele rechtbank, familierechtbank,
        jeugdrechtbank, strafuitvoeringsrechtbank), arbeidsrechtbank,
        ondernemingsrechtbank, hof van beroep, hof van assisen, Hof van
        Cassatie
    het verschil tussen burgerlijk recht en strafrecht, ook in casussen
    reflecteren over actuele thema's: (niet) uitvoering van vonnissen,
        afschaffing van de volksjury, alternatieve straffen (enkelband,
        werkstraf), hervorming van de procedure, internering, de kloof tussen
        burger en justitie, trial by media, transitiehuizen en
        detentiehuizen, procedurefouten, strengere straffen, uithandengeving
        bij minderjarigen, verjaring, vervroegde en voorwaardelijke vrijlating

Deel 1 zijn de functies van justitie, de principes en burgerlijk recht
tegenover strafrecht.
Deel 2 zijn de rechtbanken en hoven en enkele actuele thema's.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn functies van justitie?",
        opties=[
            "bestraffing",
            "conflictbeslechting",
            "ordehandhaving",
            "preventie",
            "wetgeving",
            "belastingen innen",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Ook veiligheid hoort erbij. Wetten maken is de taak van het parlement en belastingen innen die van de administratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee buren hebben ruzie over een haag die over de grens groeit. Een rechter hakt de knoop door. Welke functie van justitie zie je hier?",
        opties=["conflictbeslechting", "bestraffing", "preventie", "ordehandhaving"],
        antwoord=0,
        uitleg="De rechter beslist over een conflict tussen burgers. Er wordt niemand gestraft voor een misdrijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zware straf voor dronken rijden moet anderen ervan weerhouden om dronken achter het stuur te kruipen. Welke functie van justitie staat hier vooral voorop?",
        opties=["preventie", "conflictbeslechting", "ordehandhaving", "veiligheid"],
        antwoord=0,
        uitleg="Preventie betekent voorkomen. Een straf kan ook anderen afschrikken, zodat er minder misdrijven gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het principe van hoor en wederhoor?",
        opties=[
            "beide partijen mogen hun verhaal doen voor de rechter beslist",
            "de rechter mag enkel luisteren naar het openbaar ministerie",
            "de uitspraak wordt na de zitting luidop voorgelezen op de radio",
            "een getuige moet zijn verhaal twee keer na elkaar vertellen",
        ],
        antwoord=0,
        uitleg="Niemand mag veroordeeld worden zonder zich te kunnen verdedigen. Elke partij moet de argumenten van de andere kunnen horen en beantwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het vermoeden van onschuld?",
        opties=[
            "iemand is onschuldig tot een rechter zijn schuld bewezen heeft",
            "iemand is schuldig tot hij zelf zijn onschuld bewezen heeft",
            "iemand die zwijgt, wordt altijd schuldig verklaard",
            "iemand met een advocaat kan nooit veroordeeld worden",
        ],
        antwoord=0,
        uitleg="De bewijslast ligt bij wie beschuldigt. Zolang er geen veroordeling is, geldt een verdachte als onschuldig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het principe van openbaarheid in de rechtspraak?",
        opties=[
            "zittingen en uitspraken zijn in principe voor iedereen toegankelijk",
            "iedere burger mag zelf meebeslissen over de straf van een verdachte",
            "de namen van alle verdachten worden verplicht in de krant gezet",
            "de rechter moet zijn beslissing eerst laten goedkeuren door het parlement",
        ],
        antwoord=0,
        uitleg="Openbaarheid zorgt voor controle op de rechters. Soms gebeurt een zitting met gesloten deuren, bijvoorbeeld om minderjarigen te beschermen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechter moet oordelen over een zaak waarin zijn eigen schoonbroer de verdachte is. Welk principe komt in gevaar?",
        opties=[
            "de onpartijdigheid van de rechter",
            "de openbaarheid van de zitting",
            "het principe van hoor en wederhoor",
            "de scheiding tussen gemeenschap en gewest",
        ],
        antwoord=0,
        uitleg="Een rechter mag geen persoonlijk belang hebben in een zaak. Daarom moet hij zich hier laten vervangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen burgerlijk recht en strafrecht?",
        opties=[
            "burgerlijk recht regelt conflicten tussen burgers, strafrecht bestraft misdrijven",
            "burgerlijk recht geldt in de grote steden, strafrecht op het platteland",
            "burgerlijk recht gaat over volwassenen, strafrecht enkel over minderjarigen",
            "burgerlijk recht wordt door het parlement uitgevoerd, strafrecht door de regering",
        ],
        antwoord=0,
        uitleg="In het burgerlijk recht gaat het om bijvoorbeeld contracten, huur of schadevergoeding. In het strafrecht vervolgt het openbaar ministerie een dader in naam van de samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Lotte huurt een appartement, maar de eigenaar weigert haar waarborg terug te betalen. Over welk soort recht gaat dit?",
        opties=["burgerlijk recht", "strafrecht", "grondwettelijk recht", "internationaal recht"],
        antwoord=0,
        uitleg="Het is een conflict tussen twee burgers over een huurcontract. Er is geen misdrijf, dus het gaat om burgerlijk recht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jonas breekt in bij een buurman en steelt een laptop. Over welk soort recht gaat dit vooral?",
        opties=["strafrecht", "burgerlijk recht", "arbeidsrecht", "familierecht"],
        antwoord=0,
        uitleg="Diefstal is een misdrijf. Het openbaar ministerie kan Jonas vervolgen en een rechter kan hem een straf opleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie vervolgt in een strafzaak de verdachte in naam van de samenleving?",
        opties=["het openbaar ministerie", "de advocaat van de verdachte", "de burgemeester", "het parlement"],
        antwoord=0,
        uitleg="Het openbaar ministerie, ook het parket genoemd, onderzoekt misdrijven en vraagt de rechter om een straf.",
    ),
    dict(
        type="invultekst",
        vraag="Het principe dat iemand onschuldig is tot zijn schuld bewezen is, heet het vermoeden van ...",
        antwoord=["onschuld"],
        uitleg="Het vermoeden van onschuld staat ook in het Europees Verdrag voor de Rechten van de Mens.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechter mag een verdachte veroordelen zonder dat die zich heeft kunnen verdedigen.",
        antwoord=False,
        uitleg="Dat zou het principe van hoor en wederhoor schenden. Elke partij moet haar verhaal kunnen doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechter moet onafhankelijk zijn, dus mag hij geen bevelen krijgen van de regering over hoe hij een zaak beslist.",
        antwoord=True,
        uitleg="Onafhankelijkheid betekent dat de rechter enkel de wet volgt, zonder druk van de regering, het parlement of andere machten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een conflict over een huurcontract tussen twee burgers gaat het om strafrecht.",
        antwoord=False,
        uitleg="Een conflict tussen burgers over een contract is burgerlijk recht. Strafrecht gaat over misdrijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén feit kan zowel een strafzaak als een burgerlijke zaak opleveren.",
        antwoord=True,
        uitleg="Wie iemand in elkaar slaat, kan gestraft worden. Het slachtoffer kan daarnaast een schadevergoeding vragen, wat burgerlijk is.",
    ),
    dict(
        type="meerkeuze",
        vraag="De politie houdt een stille betoging in goede banen, zodat alles rustig verloopt. Welke functie van justitie zie je hier?",
        opties=["ordehandhaving", "bestraffing", "conflictbeslechting", "preventie"],
        antwoord=0,
        uitleg="Ordehandhaving betekent zorgen dat de regels gevolgd worden en de openbare orde bewaard blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een onafhankelijke rechtspraak belangrijk voor burgers?",
        opties=[
            "zo kunnen burgers ook tegen de overheid gelijk krijgen",
            "zo hoeven burgers nooit meer een advocaat te betalen",
            "zo kan de regering sneller nieuwe wetten maken",
            "zo kunnen rechters zelf beslissen welke wetten er komen",
        ],
        antwoord=0,
        uitleg="Als rechters los staan van de regering, kan een burger zelfs de overheid voor de rechter brengen en eerlijk behandeld worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol heeft een advocaat in een rechtszaak?",
        opties=[
            "hij verdedigt de belangen van zijn cliënt",
            "hij spreekt het vonnis uit in de zaak",
            "hij vervolgt de verdachte in naam van de samenleving",
            "hij schrijft de wet waarop de rechter zich baseert",
        ],
        antwoord=0,
        uitleg="De advocaat staat aan de kant van zijn cliënt. Het openbaar ministerie vervolgt en de rechter beslist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functie van justitie staat voorop als een rechter een gevaarlijke dader een gevangenisstraf geeft om de samenleving te beschermen?",
        opties=["veiligheid", "conflictbeslechting", "openbaarheid", "hoor en wederhoor"],
        antwoord=0,
        uitleg="Door een gevaarlijke dader op te sluiten, beschermt justitie de veiligheid van anderen. Openbaarheid en hoor en wederhoor zijn principes, geen functies.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt de gerechtelijke piramide voor?",
        opties=[
            "de opbouw van de rechtbanken en hoven, van laag tot hoog",
            "de verdeling van de zetels in het parlement over de partijen",
            "de bestuursniveaus van België, van gemeente tot federale overheid",
            "het aantal misdrijven per jaar, van licht tot zwaar",
        ],
        antwoord=0,
        uitleg="Onderaan staan het vredegerecht en de politierechtbank, in het midden de rechtbanken van eerste aanleg en de hoven van beroep, en bovenaan het Hof van Cassatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen territoriale en materiële bevoegdheid van een rechtbank?",
        opties=[
            "territoriaal gaat over het gebied, materieel over het soort zaak",
            "territoriaal gaat over het soort zaak, materieel over het gebied",
            "territoriaal gaat over de straffen, materieel over de schadevergoedingen",
            "territoriaal gaat over strafzaken, materieel over burgerlijke zaken",
        ],
        antwoord=0,
        uitleg="De materiële bevoegdheid zegt welke rechtbank een soort zaak behandelt. De territoriale bevoegdheid zegt welke rechtbank van die soort, bijvoorbeeld die van Gent of van Hasselt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechtbank behandelt een conflict tussen buren over geluidshinder?",
        opties=["het vredegerecht", "de correctionele rechtbank", "de ondernemingsrechtbank", "het hof van assisen"],
        antwoord=0,
        uitleg="De vrederechter behandelt kleinere burgerlijke geschillen en zaken zoals burenhinder en huur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechtbank behandelt een overtreding zoals te snel rijden?",
        opties=["de politierechtbank", "het vredegerecht", "de arbeidsrechtbank", "de familierechtbank"],
        antwoord=0,
        uitleg="De politierechtbank behandelt verkeersovertredingen en de schade bij verkeersongevallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechtbank behandelt een wanbedrijf zoals diefstal of slagen en verwondingen?",
        opties=["de correctionele rechtbank", "de politierechtbank", "het vredegerecht", "de ondernemingsrechtbank"],
        antwoord=0,
        uitleg="De correctionele rechtbank is een afdeling van de rechtbank van eerste aanleg die wanbedrijven bestraft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechtbank beslist over een echtscheiding en over waar de kinderen daarna wonen?",
        opties=["de familierechtbank", "de jeugdrechtbank", "de burgerlijke rechtbank", "het hof van assisen"],
        antwoord=0,
        uitleg="De familierechtbank behandelt zaken over gezin en familie, zoals echtscheidingen, verblijfsregelingen en erfenissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een minderjarige van 15 jaar pleegt een diefstal. Welke rechtbank behandelt de zaak in principe?",
        opties=["de jeugdrechtbank", "de correctionele rechtbank", "de familierechtbank", "de politierechtbank"],
        antwoord=0,
        uitleg="Minderjarigen komen in principe voor de jeugdrechtbank. Die kiest vooral voor maatregelen die opvoeden en herstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechtbank beslist of een veroordeelde met een enkelband of onder voorwaarden vroeger vrij mag?",
        opties=["de strafuitvoeringsrechtbank", "de correctionele rechtbank", "het Hof van Cassatie", "de jeugdrechtbank"],
        antwoord=0,
        uitleg="De strafuitvoeringsrechtbank beslist hoe een langere gevangenisstraf uitgevoerd wordt, bijvoorbeeld over voorwaardelijke invrijheidstelling of elektronisch toezicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer vindt dat hij onterecht ontslagen werd en stapt naar de rechter. Welke rechtbank is bevoegd?",
        opties=["de arbeidsrechtbank", "de ondernemingsrechtbank", "het vredegerecht", "de correctionele rechtbank"],
        antwoord=0,
        uitleg="De arbeidsrechtbank behandelt conflicten tussen werknemers en werkgevers en zaken over sociale zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf kan zijn schulden niet meer betalen en vraagt het faillissement aan. Welke rechtbank is bevoegd?",
        opties=["de ondernemingsrechtbank", "de arbeidsrechtbank", "de burgerlijke rechtbank", "het vredegerecht"],
        antwoord=0,
        uitleg="De ondernemingsrechtbank behandelt geschillen tussen ondernemingen en faillissementen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hof behandelt de zwaarste misdaden, zoals moord, met een volksjury?",
        opties=["het hof van assisen", "het hof van beroep", "het Hof van Cassatie", "het Grondwettelijk Hof"],
        antwoord=0,
        uitleg="Bij het hof van assisen beslist een jury van burgers mee over de schuld. Er is een maatschappelijk debat over het afschaffen van die volksjury.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand is het niet eens met een vonnis van de correctionele rechtbank. Waar kan hij in beroep gaan?",
        opties=["bij het hof van beroep", "bij het vredegerecht", "bij het hof van assisen", "bij de politierechtbank"],
        antwoord=0,
        uitleg="Tegen een vonnis van de rechtbank van eerste aanleg ga je in beroep bij het hof van beroep. Daar wordt de zaak opnieuw behandeld.",
    ),
    dict(
        type="invultekst",
        vraag="De rechtbank die verkeersovertredingen behandelt, heet de ...rechtbank.",
        antwoord=["politie", "politierechtbank"],
        uitleg="De politierechtbank staat samen met het vredegerecht onderaan de gerechtelijke piramide.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Hof van Cassatie staat bovenaan de gerechtelijke piramide.",
        antwoord=True,
        uitleg="Het Hof van Cassatie is het hoogste hof. Het kijkt na of de wet juist werd toegepast, maar beoordeelt de feiten niet opnieuw.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkstraf en een enkelband zijn straffen die je binnen de muren van de gevangenis uitzit.",
        antwoord=False,
        uitleg="Het zijn alternatieve straffen: je voert ze uit buiten de gevangenis. Of ze vaker gebruikt moeten worden, is een actueel debat.",
    ),
    dict(
        type="waarofniet",
        vraag="Het vredegerecht behandelt de zwaarste misdaden, zoals moord.",
        antwoord=False,
        uitleg="Het vredegerecht staat onderaan de piramide en behandelt kleinere burgerlijke zaken. Moord komt voor het hof van assisen.",
    ),
    dict(
        type="waarofniet",
        vraag="Verjaring betekent dat iemand na een bepaalde tijd niet meer vervolgd kan worden voor een misdrijf.",
        antwoord=True,
        uitleg="Na de verjaringstermijn kan een zaak niet meer vervolgd worden. Daarover is debat, bijvoorbeeld als een procedure lang aansleept.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met trial by media?",
        opties=[
            "de media stellen iemand al als schuldig voor, nog voor de rechter oordeelt",
            "de rechter laat de media beslissen welke straf iemand moet krijgen",
            "een rechtszaak die live op televisie uitgezonden wordt met een jury",
            "een rechtszaak tegen een journalist die een fout artikel schreef",
        ],
        antwoord=0,
        uitleg="Als de media iemand al schuldig voorstellen, komt het vermoeden van onschuld onder druk. Dat is een spanning tussen media en justitie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is uithandengeving bij een minderjarige?",
        opties=[
            "de jeugdrechter beslist dat een oudere minderjarige als volwassene berecht wordt",
            "een minderjarige wordt aan zijn ouders teruggegeven zonder straf",
            "een minderjarige mag zelf kiezen voor welke rechtbank hij komt",
            "de zaak van een minderjarige wordt doorgegeven aan een buitenlandse rechter",
        ],
        antwoord=0,
        uitleg="Bij zware feiten kan de jeugdrechter een minderjarige vanaf 16 jaar uit handen geven. Dan komt hij voor een gewone rechtbank. Of dat vaker moet, is een actueel debat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaak komt in eerste aanleg voor de burgerlijke rechtbank?",
        opties=[
            "een conflict over 40 000 euro schadevergoeding na een verbouwing",
            "een snelheidsovertreding op de autosnelweg bij Brussel",
            "een moord die gepleegd werd tijdens een gewapende overval",
            "een conflict tussen twee buren over een blaffende hond",
        ],
        antwoord=0,
        uitleg="Grotere burgerlijke geschillen gaan naar de burgerlijke rechtbank. Kleinere geschillen en burenhinder gaan naar de vrederechter.",
    ),
]

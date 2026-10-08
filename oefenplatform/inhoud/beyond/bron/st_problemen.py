# -*- coding: utf-8 -*-
"""Problemen oplossen en ICT gebruiken.

De eerste bouwsteen van de vakfiche statistiek 3DO: probleemoplossend denken.
De fiche zegt zelf dat mathematiseren en demathematiseren geïntegreerd aan bod
komen in de andere onderdelen, maar de heuristieken en het ICT-gebruik staan er
als aparte leerdoelen in, en op het examen mag je rekenapps en een online
rekentoestel gebruiken. Daarom staan ze hier vooraan.

Deel 1 is het oplossingsproces: de vier stappen, de heuristieken en wat
mathematiseren betekent.
Deel 2 is het ICT-gebruik: wanneer je de rekenapps mag inzetten, wat exact
werken betekent en wat je op het examen wel en niet bij je mag hebben.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier stappen doorloop je volgens de vakfiche bij een probleem?",
        opties=[
            "begrijp het probleem, maak een plan, voer het plan uit, reflecteer",
            "lees de vraag, zoek de formule, vul in, schrijf het antwoord netjes op",
            "schat de uitkomst, reken, controleer met de app, rond af op twee cijfers",
            "noteer de gegevens, teken een figuur, kies een schaal, meet het antwoord",
        ],
        antwoord=0,
        uitleg="Die vierde stap wordt het vaakst overgeslagen, en net daar vind je je eigen fouten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent mathematiseren?",
        opties=[
            "een concreet probleem omzetten in wiskundetaal en wiskundige symbolen",
            "een wiskundige uitkomst terugvertalen naar de situatie waarover het ging",
            "een berekening nog een tweede keer maken om ze te kunnen controleren",
            "een vraagstuk opsplitsen in kleinere vraagstukken die los van elkaar staan",
        ],
        antwoord=0,
        uitleg="De omgekeerde beweging heet demathematiseren: je uitkomst terug in gewone taal zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rekent uit dat een steekproef 23,7 mensen groot moet zijn. Wat doe je?",
        opties=[
            "je rondt naar boven af tot 24, want een steekproef bestaat uit hele mensen",
            "je rondt naar beneden af tot 23, want afronden gebeurt altijd naar beneden",
            "je laat 23,7 staan, want tussenresultaten mag je nooit afronden in een antwoord",
            "je rekent opnieuw, want een niet-geheel getal wijst altijd op een rekenfout",
        ],
        antwoord=0,
        uitleg="Demathematiseren betekent precies dit: kijken wat je uitkomst in de werkelijkheid betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een probleem is in de vakfiche iets anders dan een vraagstuk.",
        antwoord=True,
        uitleg="Een vraagstuk los je op met de leerstof van één hoofdstuk. Bij een probleem combineer je hoofdstukken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een opgave met context?",
        opties=[
            "een opgave die vertrekt van een concrete situatie uit de wereld rondom ons",
            "een opgave die abstract en zuiver wiskundig is, zonder verhaal eromheen",
            "een opgave waarbij je het antwoord op een schrijftablet moet noteren",
            "een opgave waarvoor je de rekenapps van de examencommissie nodig hebt",
        ],
        antwoord=0,
        uitleg="De fiche zegt bij elk leerdoel of je het met context, zonder context, of allebei moet kunnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een oplossingsstrategie zoals een schets maken of terugrekenen, met één woord?",
        antwoord=["heuristiek", "heuristieken", "een heuristiek"],
        uitleg="Heuristieken zijn geen formules maar manieren van aanpakken die vaak werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke heuristiek pas je toe als je bij een telprobleem eerst alle mogelijkheden opschrijft?",
        opties=[
            "alle mogelijkheden opsommen",
            "variabelen invoeren in de opgave",
            "het probleem opsplitsen in deelproblemen",
            "van achter naar voor werken, dus terugrekenen",
        ],
        antwoord=0,
        uitleg="Bij kleine aantallen werkt opsommen prima, en je ziet er vaak een patroon in dat de formule verklaart.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schets of tabel maken telt niet mee als wiskundig werk.",
        antwoord=False,
        uitleg="De fiche noemt een schets, tekening of tabel als eerste heuristiek. Het is wiskundig werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je in de stap reflecteren?",
        opties=[
            "je kijkt of je uitkomst redelijk is en of je werkwijze klopte",
            "je schrijft het antwoord nog eens netjes over in volledige zinnen",
            "je maakt dezelfde oefening nog een keer om zeker te zijn",
            "je zoekt op in je cursus of de formule die je koos de juiste was",
        ],
        antwoord=0,
        uitleg="Een kans van 1,4 of een negatieve standaardafwijking valt alleen hier door de mand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je berekent een kans en krijgt 1,25. Wat weet je meteen?",
        opties=[
            "er zit een fout in je berekening, want een kans ligt tussen nul en één",
            "de kans is groter dan honderd procent, dus de gebeurtenis gebeurt zeker",
            "je moet de uitkomst nog delen door het aantal mogelijke uitkomsten",
            "je hebt met een continue in plaats van een discrete kansvariabele gewerkt",
        ],
        antwoord=0,
        uitleg="Een kans ligt altijd tussen nul en één. Dat is de snelste controle die er bestaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het terugvertalen van een wiskundige uitkomst naar de situatie? Eén woord.",
        antwoord=["demathematiseren", "demathematiseer"],
        uitleg="Zonder die stap staat er een getal, maar geen antwoord op de vraag die gesteld was.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een probleem kies je zelf welke strategie je gebruikt.",
        antwoord=True,
        uitleg="Dat is precies het verschil met een vraagstuk: daar wijst het hoofdstuk de methode al aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aanpak hoort bij de heuristiek patronen en regelmaat ontdekken?",
        opties=[
            "je rekent enkele kleine gevallen uit en zoekt wat er telkens hetzelfde gaat",
            "je zoekt in je cursus naar een vraagstuk dat op het jouwe lijkt",
            "je vraagt je af of de uitkomst die je kreeg redelijk is",
            "je zet de gegevens in een grafiek met de rekenapps erbij",
        ],
        antwoord=0,
        uitleg="Zo vind je zelf de formule terug als je ze vergeten bent, bijvoorbeeld bij telproblemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is slim gissen en testen een geldige strategie?",
        opties=[
            "omdat je uit een fout gok leert welke richting je verder moet zoeken",
            "omdat het altijd sneller is dan een vergelijking opstellen en oplossen",
            "omdat je op het examen geen werkwijze hoeft te tonen bij gesloten vragen",
            "omdat een gok even veel punten oplevert als een uitgewerkte berekening",
        ],
        antwoord=0,
        uitleg="De fiche noemt het letterlijk: schatten, slim gissen en missen, testen, controleren.",
    ),
    dict(
        type="waarofniet",
        vraag="Taalvaardigheid hoort niet bij de vaardigheden die de vakfiche statistiek noemt.",
        antwoord=False,
        uitleg="De fiche noemt taalvaardigheid, rekenvaardigheid en ICT-vaardigheid uitdrukkelijk samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave vraagt naar het aantal mensen dat je minstens moet bevragen. Welke stap is hier het belangrijkst?",
        opties=[
            "demathematiseren, want je uitkomst moet een haalbaar aantal mensen worden",
            "mathematiseren, want je moet de vraag in symbolen kunnen zetten",
            "reflecteren, want je moet je werkwijze nog eens kunnen uitleggen",
            "een plan maken, want je moet eerst de juiste formule kiezen",
        ],
        antwoord=0,
        uitleg="Het woord minstens zegt al dat je naar boven moet afronden, hoe mooi je berekening ook uitkomt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een opgave die abstract en zuiver wiskundig is? Vul aan: een opgave ... context.",
        antwoord=["zonder"],
        uitleg="De fiche onderscheidt opgaven met context en opgaven zonder context, en zegt per leerdoel welke van de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het nut van variabelen invoeren bij een vraagstuk?",
        opties=[
            "je kan het verband tussen de gegevens opschrijven zonder alle getallen al te kennen",
            "je hoeft daardoor geen tussenstappen meer op te schrijven in je antwoord",
            "je kan het antwoord meteen aflezen zonder nog iets te moeten berekenen",
            "je vermijdt daarmee dat je ergens in de oefening moet afronden",
        ],
        antwoord=0,
        uitleg="Met een letter voor het onbekende kan je de zin van de opgave omzetten in een vergelijking.",
    ),
    dict(
        type="waarofniet",
        vraag="Een opgave kan zowel met als zonder context gesteld worden, afhankelijk van het leerdoel.",
        antwoord=True,
        uitleg="De fiche vermeldt bij elk leerdoel welke van de twee, en soms allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt bij een hypothesetoets een p-waarde van min 0,03. Wat doe je?",
        opties=[
            "je zoekt de fout, want een p-waarde is een kans en kan niet negatief zijn",
            "je besluit dat de nulhypothese zeker verworpen wordt, want min 0,03 is klein",
            "je neemt de absolute waarde en werkt verder met 0,03",
            "je verhoogt het significantieniveau tot de p-waarde positief wordt",
        ],
        antwoord=0,
        uitleg="Reflecteren betekent dat je zulke onmogelijke uitkomsten herkent voor je ze opschrijft.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke hulpmiddelen mag je volgens de vakfiche gebruiken tijdens het examen statistiek?",
        opties=[
            "de rekenapps van de examencommissie en een online wetenschappelijk rekentoestel",
            "je eigen grafisch rekentoestel en een samenvatting van één bladzijde",
            "je smartphone, zolang je er enkel een rekenmachine op opent",
            "een laptop met een rekenblad waarin je zelf formules hebt gezet",
        ],
        antwoord=0,
        uitleg="Andere ICT-middelen staat de examencommissie niet toe, en eigen materiaal meebrengen geldt als fraude.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag je eigen rekentoestel meebrengen naar het examen statistiek.",
        antwoord=False,
        uitleg="Je krijgt een online rekentoestel in het examen zelf. Eigen toestellen blijven in de locker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent exact werken?",
        opties=[
            "je laat breuken, wortels en logaritmen staan in plaats van ze te benaderen",
            "je noteert elk tussenresultaat met minstens vier cijfers na de komma",
            "je gebruikt voor elke berekening de rekenapps in plaats van hoofdrekenen",
            "je schrijft bij elke stap op welke formule je gebruikt hebt",
        ],
        antwoord=0,
        uitleg="Afronden doe je pas helemaal op het einde, anders sleept de afrondingsfout door je hele oefening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor moet je volgens de fiche ICT kunnen gebruiken bij statistiek?",
        opties=[
            "grafische voorstellingen maken, kengetallen berekenen en een onderzoek uitvoeren",
            "enkel om de grafieken te tekenen, want rekenen moet altijd met de hand",
            "enkel om de p-waarde te berekenen, want dat kan niet met de hand",
            "voor alles, want bij statistiek hoef je niets meer zelf uit te rekenen",
        ],
        antwoord=0,
        uitleg="De fiche zet die drie naast elkaar, en zegt per leerdoel waarvoor ICT nodig is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij functioneel gebruik van ICT moet je je tussenstappen nog altijd uitschrijven.",
        antwoord=True,
        uitleg="De fiche zegt het bij allebei de iconen: je toont je werkwijze en je redenering, met of zonder ICT.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel minuten duurt het examen statistiek? Schrijf het getal.",
        antwoord=["150", "honderdvijftig"],
        uitleg="Dat is twee en een half uur voor een digitaal examen met open en gesloten vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er bijzonder aan sommige vragen van dit examen?",
        opties=[
            "je noteert je antwoord met een digitale pen op een schrijftablet",
            "je spreekt je antwoord in met de hoofdtelefoon die je krijgt",
            "je mag ze overslaan en later opnieuw proberen zonder puntenverlies",
            "je krijgt er extra tijd voor bovenop de honderdvijftig minuten",
        ],
        antwoord=0,
        uitleg="Op de website van de examencommissie staat uitleg over examens met een schrijftablet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zwaar wegen de twee onderdelen van het examen statistiek?",
        opties=[
            "telproblemen, kansrekenen en statistiek zestig procent, grote datasets veertig",
            "telproblemen, kansrekenen en statistiek veertig procent, grote datasets zestig",
            "allebei precies vijftig procent, want ze zijn even belangrijk",
            "telproblemen vijfentwintig, kansrekenen vijfentwintig, datasets vijftig",
        ],
        antwoord=0,
        uitleg="Werken met grote datasets is dus vier tienden van je punten, en dat deel doe je volledig met de rekenapps.",
    ),
    dict(
        type="waarofniet",
        vraag="Er is giscorrectie op het examen statistiek.",
        antwoord=False,
        uitleg="De fiche zegt het uitdrukkelijk: er is geen giscorrectie. Een vraag blanco laten levert dus niets op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om thuis met de rekenapps te oefenen?",
        opties=[
            "omdat je op het examen tijd verliest als je ze dan pas moet leren bedienen",
            "omdat je er anders geen punten voor krijgt bij het onderdeel grote datasets",
            "omdat je thuis andere apps krijgt dan op het examen en je beide moet kennen",
            "omdat je ze op het examen enkel mag openen als je dat vooraf aanvraagt",
        ],
        antwoord=0,
        uitleg="De examencommissie raadt het zelf aan, en er staat ook een oefenexamen op hun website.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een uitdrukking niet benaderen of afronden? Vul aan: ... werken.",
        antwoord=["exact"],
        uitleg="Komt een breuk niet mooi uit, laat ze dan als breuk staan tot het einde van je berekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werk je met zo nauwkeurig mogelijke tussenresultaten?",
        opties=[
            "omdat een afgerond tussenresultaat je eindantwoord verder van de waarheid brengt",
            "omdat de verbeteraar anders niet ziet welke formule je gebruikt hebt",
            "omdat de rekenapps anders een foutmelding geven en opnieuw beginnen",
            "omdat je anders geen exacte waarde meer in je antwoord mag schrijven",
        ],
        antwoord=0,
        uitleg="Elke afronding onderweg stapelt op. Rond pas af als je klaar bent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een samenvatting meebrengen in de examenruimte geldt als examenfraude.",
        antwoord=True,
        uitleg="Net als een gsm, een smartwatch of cursusmateriaal. Alles blijft in de locker aan het onthaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat krijg je van de examencommissie zelf bij dit examen?",
        opties=[
            "een balpen, kladpapier en een hoofdtelefoon",
            "een grafisch rekentoestel en een formularium op papier",
            "een laptop met een rekenblad en een handleiding",
            "een woordenboek op papier en een geodriehoek",
        ],
        antwoord=0,
        uitleg="Een geodriehoek, passer of meetlat mag je altijd vragen als je er een wil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een vraag met een icoon dat zegt dat je ze zonder ICT moet oplossen. Wat betekent dat?",
        opties=[
            "je rekent met de hand, toont elke tussenstap en werkt exact",
            "je mag het rekentoestel enkel voor de laatste berekening gebruiken",
            "je hoeft bij die vraag geen werkwijze te noteren, enkel het antwoord",
            "je mag de vraag overslaan als je de rekenapps nodig hebt",
        ],
        antwoord=0,
        uitleg="Bij functioneel gebruik mag ICT wel, maar ook dan schrijf je al je stappen uit.",
    ),
    dict(
        type="invultekst",
        vraag="Waarmee schrijf je op het schrijftablet? Vul aan: met een digitale ...",
        antwoord=["pen"],
        uitleg="Oefen daar vooraf mee: schrijven op een tablet gaat anders dan op papier.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij open vragen beoordeelt de examencommissie enkel je eindantwoord.",
        antwoord=False,
        uitleg="Ook je notaties en begrippen tellen mee. De bijlage Begrippen en notaties zegt welke je moet gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er een bijlage met begrippen en notaties bij de vakfiche?",
        opties=[
            "omdat handboeken en websites verschillende symbolen gebruiken voor hetzelfde",
            "omdat je die bijlage op het examen moet kunnen opzeggen uit het hoofd",
            "omdat de bijlage alle formules bevat die je anders zou moeten memoriseren",
            "omdat je anders niet weet welke hoofdstukken je moet studeren",
        ],
        antwoord=0,
        uitleg="De examencommissie verwacht dat je de notatie uit die bijlage gebruikt, niet die van jouw boek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar leg je het examen statistiek af?",
        opties=[
            "in het examencentrum in Brussel",
            "thuis, online, met een camera die meekijkt",
            "in een school naar keuze in je eigen provincie",
            "in het examencentrum van de hogeschool waar je je inschrijft",
        ],
        antwoord=0,
        uitleg="Je meldt je aan met je identiteitskaart en start je examen met de code van je examensticker.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan je examen pas afsluiten vanaf een kwartier na de start.",
        antwoord=True,
        uitleg="Ten vroegste vijftien minuten na de start, met de knop beëindigen. Je kladblad geef je af.",
    ),
]

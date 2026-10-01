# -*- coding: utf-8 -*-
"""Programmeren: algoritmen, datastructuren en Python.

Het derde onderdeel van fiche G3, goed voor twintig procent van dat examen.
Het examen zelf is een programmeeropdracht in Python, dus deze vragen gaan
over de woorden en de keuzes die je daarbij maakt, niet over code uit het
hoofd leren.

Deel 1 is de basis: wat een algoritme is, de bouwstenen van een programma en
de vier datastructuren met hun verschillen.
Deel 2 zijn de algoritmische technieken, correctheid en eindigheid, het
in- en uitvoeren van bestanden en de drie toegelaten bibliotheken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een algoritme?",
        opties=[
            "een stappenplan dat na eindig veel stappen tot een oplossing komt",
            "een programma dat helemaal in de taal Python is geschreven en werkt",
            "een formule waarmee je een wiskundig probleem kan oplossen",
            "een lijst met alle gegevens die een programma nodig heeft",
        ],
        antwoord=0,
        uitleg="Een algoritme bestaat los van de taal. Pas daarna schrijf je het in Python.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een variabele in een programma?",
        opties=[
            "een naam waarachter een waarde zit die kan veranderen",
            "een getal dat in het programma nooit meer verandert",
            "een stukje code dat je op meerdere plaatsen oproept",
            "een voorwaarde waaraan de gegevens moeten voldoen",
        ],
        antwoord=0,
        uitleg="Je geeft hem een naam en zet er een waarde in. Later kan je die waarde overschrijven.",
    ),
    dict(
        type="invultekst",
        vraag="In welke programmeertaal schrijf je je oplossing op het examen? Schrijf het woord.",
        antwoord=["python"],
        uitleg="Je programmeert in een online omgeving, dus je moet niets op je eigen computer installeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een constante is een waarde die tijdens het programma niet verandert.",
        antwoord=True,
        uitleg="Bijvoorbeeld het aantal seconden in een uur. Je geeft die toch een naam, zodat je code leesbaar blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een conditie in een programma?",
        opties=[
            "ze laat een stuk code alleen lopen als iets waar is",
            "ze herhaalt een stuk code een aantal keer na elkaar",
            "ze bewaart een waarde onder een gekozen naam",
            "ze roept een stuk code op dat elders staat",
        ],
        antwoord=0,
        uitleg="In Python is dat de constructie met als en anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een iteratie?",
        opties=[
            "een herhaling van hetzelfde stuk code",
            "een keuze tussen twee stukken code",
            "een naam voor een waarde die vastligt",
            "een functie die zichzelf opnieuw oproept",
        ],
        antwoord=0,
        uitleg="Een lus, bijvoorbeeld over alle elementen van een lijst of zolang een voorwaarde geldt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een string is een rij tekens.",
        antwoord=True,
        uitleg="Letters, cijfers en leestekens na elkaar, tussen aanhalingstekens geschreven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke datastructuur bewaart paren van een sleutel en een waarde? Schrijf het woord.",
        antwoord=["dictionary", "woordenboek"],
        uitleg="Je zoekt er iets op met de sleutel, zoals een naam, en krijgt de bijbehorende waarde terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een list en een tuple?",
        opties=[
            "een tuple kan je achteraf niet meer wijzigen",
            "een tuple kan maar twee elementen bevatten",
            "een tuple bewaart de volgorde niet van de elementen",
            "een tuple kan geen getallen bevatten, enkel tekst",
        ],
        antwoord=0,
        uitleg="Allebei geordend, maar een list pas je aan en een tuple ligt vast zodra hij bestaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een set kan hetzelfde element twee keer bevatten.",
        antwoord=False,
        uitleg="Elk element komt er juist één keer in voor. Dubbels verdwijnen vanzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor kies je een set?",
        opties=[
            "als je enkel de verschillende waarden wil overhouden",
            "als je de volgorde van de gegevens wil bewaren",
            "als je bij elke sleutel een waarde wil opslaan",
            "als je de gegevens achteraf niet meer wil wijzigen",
        ],
        antwoord=0,
        uitleg="Dubbels eruit halen is precies waar een set voor dient.",
    ),
    dict(
        type="invultekst",
        vraag="Je steekt de getallen één, twee, twee en drie in een set. Hoeveel elementen bevat die set? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="De tweede twee verdwijnt, want in een set staat elk element maar één keer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geef je variabelen een zinvolle naam?",
        opties=[
            "omdat je code dan leesbaar blijft voor jezelf en anderen",
            "omdat het programma anders langzamer zal werken",
            "omdat Python korte namen niet aanvaardt in een functie",
            "omdat je anders geen commentaar meer mag toevoegen",
        ],
        antwoord=0,
        uitleg="De computer kan het niets schelen, maar een lezer wel, en dat telt mee in de beoordeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Commentaar in je code wordt mee uitgevoerd door het programma.",
        antwoord=False,
        uitleg="Commentaar wordt overgeslagen. Het staat er alleen voor wie de code leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is debuggen?",
        opties=[
            "fouten in je programma opsporen en herstellen",
            "je programma sneller laten lopen dan daarvoor",
            "je programma van commentaar voorzien achteraf",
            "je gegevens uit een bestand inlezen in de code",
        ],
        antwoord=0,
        uitleg="Het hoort bij de laatste stap: testen, en daarna herstellen wat er misgaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een functie in een programma?",
        opties=[
            "om een stuk code een naam te geven en te hergebruiken",
            "om de gegevens van het programma ergens in op te slaan",
            "om een keuze te maken tussen twee mogelijkheden",
            "om de volgorde van de gegevens vast te leggen",
        ],
        antwoord=0,
        uitleg="Je schrijft het één keer en roept het daarna zo vaak op als je wil, telkens met andere waarden.",
    ),
    dict(
        type="waarofniet",
        vraag="Je werkt een oplossing uit in vier stappen: analyseren, een algoritme ontwerpen, programmeren, en testen en debuggen.",
        antwoord=True,
        uitleg="Meteen beginnen typen zonder het probleem te analyseren kost je achteraf meer tijd dan het wint.",
    ),
    dict(
        type="invultekst",
        vraag="Uit hoeveel stappen bestaat die werkwijze om een probleem op te lossen? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg="Analyseren, ontwerpen, programmeren, testen en debuggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een geordende rij getallen bijhouden die je nog gaat aanpassen. Wat kies je?",
        opties=[
            "een list",
            "een tuple",
            "een set",
            "een string",
        ],
        antwoord=0,
        uitleg="Geordend én aanpasbaar, dat is precies een list. Een tuple ligt vast en een set is niet geordend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom test je je programma ook met randgevallen?",
        opties=[
            "omdat fouten zich meestal net daar verstoppen",
            "omdat het programma daardoor sneller gaat lopen",
            "omdat je anders geen gegevens kan exporteren",
            "omdat de opdracht altijd randgevallen bevat",
        ],
        antwoord=0,
        uitleg="Een lege lijst, één element, een nul, een negatief getal: dat is waar een programma struikelt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is recursie?",
        opties=[
            "een functie die zichzelf oproept",
            "een lus die een vast aantal keer loopt",
            "een programma dat zichzelf opnieuw start",
            "een gegeven dat zichzelf blijft herhalen",
        ],
        antwoord=0,
        uitleg="Het probleem wordt telkens een beetje kleiner tot het vanzelf oplosbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft elke recursieve functie nodig?",
        opties=[
            "een geval waarin ze zichzelf niet meer oproept",
            "een lus die het aantal oproepen telt onderweg",
            "een lijst waarin alle tussenstappen bewaard blijven",
            "minstens twee verschillende startwaarden om te werken",
        ],
        antwoord=0,
        uitleg="Zonder zo'n stopgeval blijft ze zichzelf oproepen tot het programma vastloopt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de techniek waarbij je een probleem opsplitst in kleinere deelproblemen en de deeloplossingen daarna samenvoegt? Schrijf het woord.",
        antwoord=["verdeel-en-heers", "verdeel en heers"],
        uitleg="Sorteren doe je zo: splits de lijst in twee, sorteer elke helft en voeg ze daarna samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dynamisch programmeren bewaar je tussenresultaten zodat je ze niet twee keer hoeft te berekenen.",
        antwoord=True,
        uitleg="Bij de rij van Fibonacci scheelt dat het verschil tussen een seconde en een eeuwigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een algoritme eindig is?",
        opties=[
            "het stopt na een eindig aantal stappen",
            "het werkt met een eindig aantal gegevens",
            "het bestaat uit een eindig aantal regels code",
            "het geeft altijd maar één enkel antwoord terug",
        ],
        antwoord=0,
        uitleg="Een programma dat eeuwig blijft lopen, lost niets op, ook al klopt elke stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de correctheid van een algoritme?",
        opties=[
            "het geeft voor elke toegelaten invoer het juiste antwoord",
            "het geeft voor de geteste invoer het juiste antwoord",
            "het is in een geldige programmeertaal geschreven",
            "het bevat geen enkele spelfout in de code zelf",
        ],
        antwoord=0,
        uitleg="Voor elke toegelaten invoer, niet alleen voor de gevallen die je toevallig uitprobeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recursieve functie zonder stopgeval blijft zichzelf oproepen tot het programma vastloopt.",
        antwoord=True,
        uitleg="Python geeft dan een foutmelding omdat de oproepen te diep gaan.",
    ),
    dict(
        type="invultekst",
        vraag="Naast een gewoon tekstbestand, welk soort bestand lees je in en schrijf je weg op het examen? Schrijf de drie letters.",
        antwoord=["csv"],
        uitleg="Een bestand waarin de waarden door komma's of puntkomma's gescheiden staan, zoals een tabel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bibliotheken mag je op het examen gebruiken?",
        opties=[
            "matplotlib, numpy en random",
            "alle bibliotheken die bij Python horen",
            "enkel numpy, en verder geen enkele andere",
            "geen enkele, je schrijft alles helemaal zelf",
        ],
        antwoord=0,
        uitleg="Alleen die drie, tenzij de opdracht er uitdrukkelijk een andere bij vermeldt en toelicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag op het examen om het even welke bibliotheek importeren.",
        antwoord=False,
        uitleg="Enkel matplotlib, numpy en random, of wat de opdracht zelf aanreikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je matplotlib?",
        opties=[
            "om grafieken te tekenen van je gegevens",
            "om snel met grote rijen getallen te rekenen",
            "om toevalsgetallen te laten genereren",
            "om bestanden in te lezen en weg te schrijven",
        ],
        antwoord=0,
        uitleg="Je gegevens in beeld brengen, bijvoorbeeld een functie of een spreidingsdiagram.",
    ),
    dict(
        type="invultekst",
        vraag="Welke van de drie toegelaten bibliotheken gebruik je om toevalsgetallen te laten genereren? Schrijf het woord.",
        antwoord=["random"],
        uitleg="Handig om een simulatie te schrijven, bijvoorbeeld van dobbelstenen of van een steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop vergelijk je twee oplossingen voor hetzelfde probleem?",
        opties=[
            "op snelheid, geheugengebruik en gedrag bij veel gegevens",
            "op het aantal regels code dat ze nodig hebben",
            "op het aantal functies dat erin gebruikt wordt en hoe lang ze zijn",
            "op de bibliotheken die ze allebei importeren",
        ],
        antwoord=0,
        uitleg="Een oplossing die bij tien getallen vlot werkt, kan bij een miljoen getallen onbruikbaar worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee algoritmen die hetzelfde antwoord geven, zijn ook even snel.",
        antwoord=False,
        uitleg="Allebei correct kan, maar het ene kan duizend keer trager zijn dan het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een numerieke methode?",
        opties=[
            "een manier om een antwoord te benaderen met rekenstappen",
            "een manier om een antwoord exact te berekenen met formules",
            "een manier om gegevens in een tabel te ordenen",
            "een manier om een grafiek nauwkeurig te tekenen",
        ],
        antwoord=0,
        uitleg="Je krijgt geen exacte formule maar een benadering, en die maak je zo nauwkeurig als je wil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe benader je met een programma een bepaalde integraal?",
        opties=[
            "je telt de oppervlakte van heel veel smalle stroken op",
            "je zoekt eerst met de computer een primitieve functie",
            "je tekent de grafiek en meet de oppervlakte op het scherm",
            "je berekent de afgeleide in een groot aantal punten",
        ],
        antwoord=0,
        uitleg="Precies de Riemannsom, maar dan door de computer uitgevoerd met heel veel stroken.",
    ),
    dict(
        type="waarofniet",
        vraag="Dynamisch programmeren kost meer geheugen maar wint tijd.",
        antwoord=True,
        uitleg="Je bewaart tussenresultaten, en dat nemen plaats in. In ruil hoef je niets twee keer te berekenen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke van de drie toegelaten bibliotheken gebruik je om vlot met grote rijen getallen te rekenen? Schrijf het woord.",
        antwoord=["numpy"],
        uitleg="Ze rekent met hele rijen tegelijk, veel sneller dan met een lus over een gewone list.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beargumenteer je de eindigheid van je algoritme?",
        opties=[
            "omdat een programma dat blijft lopen niets oplost",
            "omdat je anders geen bestanden mag wegschrijven",
            "omdat het programma anders fouten zou bevatten",
            "omdat het programma dan minder geheugen gebruikt",
        ],
        antwoord=0,
        uitleg="Bij een lus toon je dat de voorwaarde ooit vals wordt, bij recursie dat je het stopgeval altijd bereikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet in een gesorteerde lijst van duizend getallen nagaan of een getal erin staat. Wat is de slimste aanpak?",
        opties=[
            "telkens de helft wegnemen tot je het getal vindt",
            "de lijst van voor naar achter helemaal doorlopen",
            "de lijst eerst nog eens opnieuw laten sorteren",
            "alle getallen in een set steken en die doorlopen",
        ],
        antwoord=0,
        uitleg="Dat is verdeel-en-heers: in de helft kijken en de helft die niet kan kloppen meteen weggooien. Tien stappen volstaan dan.",
    ),
]

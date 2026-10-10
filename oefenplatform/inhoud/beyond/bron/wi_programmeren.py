# -*- coding: utf-8 -*-
r"""Programmeren: algoritmen, datastructuren en Python.

Het derde onderdeel van fiche G3, goed voor twintig procent van dat examen.
Het examen zelf is een programmeeropdracht in Python, dus deze vragen gaan
over de woorden en de keuzes die je daarbij maakt, niet over code uit het
hoofd leren.

Sleutelwoorden en stukjes code staan in \(\texttt{...}\), zodat je ze op het
scherm ziet staan zoals in een programma. Waar er echte wiskunde bij hoort
(de rij van Fibonacci, een Riemannsom, \(O(n)\)), staat die in notatie.

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
        uitleg=r"Na \(\texttt{n = 5}\) staat er een \(5\) achter de naam \(\texttt{n}\). Schrijf je later \(\texttt{n = 7}\), dan is die waarde overschreven.",
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
        vraag=r"Welk sleutelwoord laat een stuk code alleen lopen als een voorwaarde waar is?",
        opties=[
            r"\(\texttt{if}\)",
            r"\(\texttt{for}\)",
            r"\(\texttt{def}\)",
            r"\(\texttt{return}\)",
        ],
        antwoord=0,
        uitleg=r"Dat is de conditie. Wat er moet gebeuren als de voorwaarde niet geldt, zet je achter \(\texttt{else}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee sleutelwoorden schrijven een herhaling?",
        opties=[
            r"\(\texttt{for}\) en \(\texttt{while}\)",
            r"\(\texttt{if}\) en \(\texttt{else}\)",
            r"\(\texttt{def}\) en \(\texttt{return}\)",
            r"\(\texttt{try}\) en \(\texttt{except}\)",
        ],
        antwoord=0,
        uitleg=r"Met \(\texttt{for}\) loop je over alle elementen van een rij, met \(\texttt{while}\) herhaal je zolang een voorwaarde geldt.",
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
        vraag=r"Wat is het verschil tussen een \(\texttt{list}\) en een \(\texttt{tuple}\)?",
        opties=[
            r"een \(\texttt{tuple}\) kan je achteraf niet meer wijzigen",
            r"een \(\texttt{tuple}\) kan maar twee elementen bevatten",
            r"een \(\texttt{tuple}\) bewaart de volgorde van de elementen niet",
            r"een \(\texttt{tuple}\) kan geen getallen bevatten, enkel tekst",
        ],
        antwoord=0,
        uitleg="Allebei geordend, maar een list pas je aan en een tuple ligt vast zodra hij bestaat.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een \(\texttt{set}\) kan hetzelfde element twee keer bevatten.",
        antwoord=False,
        uitleg="Elk element komt er juist één keer in voor. Dubbels verdwijnen vanzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvoor kies je een \(\texttt{set}\)?",
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
        vraag=r"Je steekt \(\texttt{[1, 2, 2, 3, 3, 3]}\) in een set. Hoeveel elementen telt die set? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Elke waarde blijft maar één keer over, dus er blijven er drie staan.",
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
        uitleg=r"\(\texttt{aantal\_leerlingen}\) zegt iets, \(\texttt{a}\) niet. De computer kan het niets schelen, een lezer wel, en dat telt mee in de beoordeling.",
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
        vraag=r"Waarvoor dient \(\texttt{def}\) in een programma?",
        opties=[
            "om een stuk code een naam te geven en te hergebruiken",
            "om de gegevens van het programma ergens in op te slaan",
            "om een keuze te maken tussen twee mogelijkheden",
            "om de volgorde van de gegevens vast te leggen",
        ],
        antwoord=0,
        uitleg=r"Je schrijft een functie één keer en roept ze daarna zo vaak op als je wil. Wat ze teruggeeft, zet je achter \(\texttt{return}\).",
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
            r"een \(\texttt{list}\)",
            r"een \(\texttt{tuple}\)",
            r"een \(\texttt{set}\)",
            r"een \(\texttt{string}\)",
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
        uitleg=r"Een lege lijst, \(1\) element, een \(0\), een negatief getal: dat is waar een programma struikelt.",
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
        uitleg=r"De faculteit schrijf je zo: \(n! = n \cdot (n-1)!\), met \(0! = 1\) als stopgeval.",
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
        uitleg=r"Bij \(F(n) = F(n-1) + F(n-2)\) zijn dat \(F(0) = 0\) en \(F(1) = 1\). Zonder stopgeval loopt het programma vast.",
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
        uitleg=r"Reken je \(F(n) = F(n-1) + F(n-2)\) recursief uit zonder iets te bewaren, dan bereken je \(F(5)\) acht keer opnieuw.",
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
            r"\(\texttt{matplotlib}\), \(\texttt{numpy}\) en \(\texttt{random}\)",
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
        uitleg=r"Enkel \(\texttt{matplotlib}\), \(\texttt{numpy}\) en \(\texttt{random}\), of wat de opdracht zelf aanreikt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvoor gebruik je \(\texttt{matplotlib}\)?",
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
        vraag=r"De ene oplossing doet \(O(n)\) stappen, de andere \(O(n^{2})\). Wat betekent dat?",
        opties=[
            r"de tweede loopt steeds trager naarmate \(n\) groter wordt",
            r"de tweede loopt steeds sneller naarmate \(n\) groter wordt",
            r"ze zijn even traag, want \(n\) is in allebei hetzelfde",
            r"de tweede gebruikt meer geheugen, maar niet meer tijd",
        ],
        antwoord=0,
        uitleg=r"Bij \(n = 1000\) is dat \(1000\) tegenover \(1\,000\,000\) stappen. Je vergelijkt oplossingen op snelheid, geheugen en gedrag bij veel gegevens.",
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
        vraag=r"Je laat een programma \(\int_{a}^{b} f(x) \, dx\) benaderen. Wat laat je het berekenen?",
        opties=[
            r"\(\sum_{i=1}^{n} f(x_{i}) \cdot \Delta x\) met \(\Delta x = \tfrac{b-a}{n}\)",
            r"\(\sum_{i=1}^{n} f(x_{i})\), zonder de breedte van de stroken",
            r"\(\tfrac{f(b) - f(a)}{b - a}\), het gemiddelde verschil",
            r"\(f'(x_{i})\) in \(n\) punten na elkaar, en dan de som",
        ],
        antwoord=0,
        uitleg=r"Dat is de Riemannsom: heel veel smalle stroken optellen. Hoe groter \(n\), hoe beter de benadering.",
    ),
    dict(
        type="waarofniet",
        vraag="Dynamisch programmeren kost meer geheugen maar wint tijd.",
        antwoord=True,
        uitleg="Je bewaart tussenresultaten, en die nemen plaats in. In ruil hoef je niets twee keer te berekenen.",
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
        vraag=r"In een gesorteerde lijst van \(1000\) getallen zoek je telkens verder in de helft die nog kan kloppen. Hoeveel stappen heb je hoogstens nodig?",
        opties=[
            r"\(10\)",
            r"\(100\)",
            r"\(500\)",
            r"\(1000\)",
        ],
        antwoord=0,
        uitleg=r"Elke stap halveert: \(2^{10} = 1024 > 1000\), dus \(10\) stappen volstaan. Van voor naar achter doorlopen zou er \(1000\) vragen.",
    ),
]

# -*- coding: utf-8 -*-
"""De juiste grafische voorstelling kiezen en lezen.

De fiche somt zes voorstellingen bij naam op en geen andere: staafdiagram,
lijndiagram, dotplot, histogram, spreidingsdiagram en boxplot. Een cirkel- of
schijfdiagram staat er níét bij, dus daar komt geen vraag over.

Het leerdoel is scherper dan "een grafiek kunnen maken":
    "Je beoordeelt welke grafische voorstelling in de gegeven situatie
     zinvol is. Je kiest de meest geschikte voorstelling voor de gegeven
     dataset."
Kiezen dus, en daarna verantwoorden. Daarom gaan de meeste vragen van deel 1
over de vraag welke grafiek bij welke soort data hoort, en deel 2 over
grafieken lezen en over grafieken die misleiden.

Dat laatste sluit aan bij wat een ouder ons in oktober 2026 meegaf: zet de
waarden boven de staven als er een uitschieter is, en geef de zij-as een lijn
met getallen. Een grafiek die de lezer op het verkeerde been zet, is geen
stijlfout maar een inhoudelijke fout.

Deel 1 is de keuze van de voorstelling.
Deel 2 is grafieken lezen en misleidende grafieken herkennen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling kies je voor het aantal leerlingen per studierichting?",
        opties=[
            "een staafdiagram, want de richtingen zijn categorieën",
            "een histogram, want je groepeert de leerlingen in klassen",
            "een lijndiagram, want je volgt een verloop in de tijd",
            "een spreidingsdiagram, want je vergelijkt twee grootheden",
        ],
        antwoord=0,
        uitleg="Bij losse categorieën horen losse staven, met een spatie ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling kies je voor de lengte van duizend leerlingen, gegroepeerd in klassen?",
        opties=[
            "een histogram, want de klassen sluiten op elkaar aan",
            "een staafdiagram, want elke klasse is een eigen categorie",
            "een boxplot, want je wil de kwartielen tonen",
            "een dotplot, want elke leerling krijgt een eigen stip",
        ],
        antwoord=0,
        uitleg="Een histogram heeft staven die tegen elkaar staan, omdat de klassen een doorlopende getallenas vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een staafdiagram en een histogram?",
        opties=[
            "bij een histogram staan de staven tegen elkaar, bij een staafdiagram los",
            "bij een staafdiagram staan de staven tegen elkaar, bij een histogram los",
            "een histogram gebruikt geen verticale as met getallen erop",
            "een staafdiagram kan enkel met ICT gemaakt worden",
        ],
        antwoord=0,
        uitleg="Dat verschil is geen stijlkeuze: aansluitende staven zeggen dat de as doorloopt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lijndiagram is geschikt om een verloop in de tijd te tonen.",
        antwoord=True,
        uitleg="Het aantal geboortes per jaar of de temperatuur per maand: de lijn maakt de richting zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont een dotplot?",
        opties=[
            "voor elke waarde een stip boven de getallenas",
            "voor elke categorie een staaf met haar frequentie",
            "voor elk element een punt met twee gemeten waarden",
            "voor elke groep een vakje met de kwartielen",
        ],
        antwoord=0,
        uitleg="Komt een waarde drie keer voor, dan staan er drie stippen boven elkaar. Handig bij een kleine dataset.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling kies je om de resultaten van vier klassen in één beeld te vergelijken?",
        opties=[
            "vier boxplots naast elkaar op dezelfde as",
            "vier histogrammen op vier verschillende assen",
            "een lijndiagram met de vier klassen als punten",
            "een dotplot met alle leerlingen door elkaar",
        ],
        antwoord=0,
        uitleg="Een boxplot vat elke groep samen in vijf getallen, dus je ziet meteen welke groep hoger of breder ligt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke voorstelling gebruik je voor het verband tussen twee numerieke variabelen? Eén woord.",
        antwoord=["spreidingsdiagram", "scatterdiagram", "puntenwolk"],
        uitleg="Een spreidingsdiagram, ook puntenwolk of scatterdiagram genoemd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dotplot is onbruikbaar bij een dataset van tienduizend waarden.",
        antwoord=True,
        uitleg="Je zou tienduizend stippen moeten tekenen. Groepeer dan en maak een histogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zes voorstellingen noemt de vakfiche bij naam?",
        opties=[
            "staafdiagram, lijndiagram, dotplot, histogram, spreidingsdiagram en boxplot",
            "staafdiagram, cirkeldiagram, dotplot, histogram, puntenwolk en boxplot",
            "staafdiagram, lijndiagram, cirkeldiagram, histogram, boxplot en dotplot",
            "lijndiagram, cirkeldiagram, histogram, boxplot, dotplot en tabel",
        ],
        antwoord=0,
        uitleg="Een cirkeldiagram of schijfdiagram staat niet in de lijst van deze fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling kies je voor het aantal werklozen per maand over tien jaar?",
        opties=[
            "een lijndiagram, want de tijd loopt door",
            "een boxplot, want je vergelijkt de maanden",
            "een histogram, want je groepeert de maanden",
            "een spreidingsdiagram, want je hebt twee variabelen",
        ],
        antwoord=0,
        uitleg="Bij een reeks in de tijd geeft een lijn de beste blik op stijgingen, dalingen en seizoenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een histogram is geschikt voor een niet-numerieke variabele zoals haarkleur.",
        antwoord=False,
        uitleg="Dan gebruik je een staafdiagram. Een histogram hoort bij een doorlopende getallenas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kies je bij een continue variabele een histogram en geen staafdiagram?",
        opties=[
            "omdat de aansluitende staven tonen dat de waarden doorlopen",
            "omdat een staafdiagram geen verticale as mag hebben",
            "omdat een histogram minder klassen nodig heeft",
            "omdat een staafdiagram enkel voor kleine datasets dient",
        ],
        antwoord=0,
        uitleg="Losse staven suggereren losse categorieën. Bij lengte of gewicht zou dat een verkeerd beeld geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je volgens de fiche de grafische voorstellingen bij een grote dataset?",
        opties=[
            "met ICT, dus met de rekenapps van de examencommissie",
            "met de hand, want een rekenapp tekent geen histogram",
            "door alleen de eerste honderd gegevens te tekenen",
            "door de gegevens eerst te standaardiseren",
        ],
        antwoord=0,
        uitleg="De fiche vraagt het ook zo: je maakt met ICT de nodige grafische voorstellingen. Het beoordelen doe je zelf.",
    ),
    dict(
        type="invultekst",
        vraag="Welke voorstelling toont de vijf kengetallen van een dataset in één beeld? Eén woord.",
        antwoord=["boxplot", "een boxplot", "doosdiagram"],
        uitleg="Een boxplot, met het minimum, de drie kwartielen en het maximum.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor dezelfde dataset kan meer dan één voorstelling zinvol zijn.",
        antwoord=True,
        uitleg="Een histogram toont de vorm, een boxplot de spreiding en de uitschieters. Vaak maak je er twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil tonen of er een verband is tussen het aantal uren slaap en het punt op een toets. Wat kies je?",
        opties=[
            "een spreidingsdiagram met de slaap horizontaal",
            "twee histogrammen naast elkaar getekend",
            "een lijndiagram met de punten in volgorde",
            "een staafdiagram met de slaapuren als categorie",
        ],
        antwoord=0,
        uitleg="Twee numerieke variabelen per leerling, dus één punt per leerling in een puntenwolk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling kies je om de vorm van een verdeling te beoordelen op normaliteit?",
        opties=[
            "een histogram, want daar zie je de klokvorm",
            "een boxplot, want daar zie je de kwartielen",
            "een lijndiagram, want daar zie je het verloop",
            "een staafdiagram, want daar zie je de categorieën",
        ],
        antwoord=0,
        uitleg="De fiche vraagt dat je op basis van een grafische voorstelling beoordeelt of de normale verdeling past. Een histogram is daar het geschiktst voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een boxplot toont hoeveel gegevens er in elke klasse vallen.",
        antwoord=False,
        uitleg="Nee. Een boxplot toont vijf posities, niet de frequenties. Daarvoor heb je een histogram nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Staan de staven van een histogram tegen elkaar of los van elkaar? Antwoord in twee woorden.",
        antwoord=["tegen elkaar", "aan elkaar"],
        uitleg="Tegen elkaar, want de klassen vormen samen een doorlopende getallenas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling maakt een lijndiagram van het aantal leerlingen per studierichting. Wat zou je aanraden?",
        opties=[
            "een staafdiagram, want tussen twee richtingen zit geen verloop",
            "een histogram, want de richtingen zijn te groeperen",
            "een spreidingsdiagram, want er zijn twee variabelen",
            "niets aanpassen, een lijndiagram past bij elke dataset",
        ],
        antwoord=0,
        uitleg="Een lijn suggereert een overgang van de ene richting naar de andere, en die bestaat niet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom is een staafdiagram waarvan de verticale as bij tachtig begint misleidend?",
        opties=[
            "kleine verschillen lijken dan veel groter dan ze zijn",
            "de staven kunnen dan niet meer getekend worden",
            "de frequenties worden dan automatisch verkeerd geteld",
            "een verticale as moet altijd in procent staan",
        ],
        antwoord=0,
        uitleg="Een verschil van twee procent vult dan het halve beeld. Begin bij nul, of vermeld de breuk in de as uitdrukkelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af uit de hoogte van een staaf in een histogram?",
        opties=[
            "hoeveel gegevens er in die klasse vallen",
            "hoe breed de klasse gekozen is",
            "wat het gemiddelde van die klasse is",
            "welke klasse de mediaan bevat",
        ],
        antwoord=0,
        uitleg="Bij gelijke klassenbreedtes is de hoogte de frequentie. Bij ongelijke breedtes is de oppervlakte wat telt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek hoort altijd een titel en een naam bij elke as te hebben.",
        antwoord=True,
        uitleg="Zonder eenheid en benoeming kan een lezer niets met een grafiek. Dat kost op een examen punten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een histogram met één hoge staaf en veel lage staven rechts ervan. Hoe beschrijf je die verdeling?",
        opties=[
            "scheef naar rechts, met een lange staart aan de rechterkant",
            "scheef naar links, met een lange staart aan de linkerkant",
            "symmetrisch rond het gemiddelde van de dataset",
            "klokvormig en dus geschikt voor een normale verdeling",
        ],
        antwoord=0,
        uitleg="De staart bepaalt de richting van de scheefheid. Inkomens zien er bijna altijd zo uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een staaf in een diagram torent ver boven de andere uit. Wat doe je volgens goede praktijk?",
        opties=[
            "je zet de waarden boven de staven zodat de lezer de kleine ook kan lezen",
            "je laat de hoge staaf weg zodat het beeld leesbaar blijft",
            "je maakt van de hoge staaf een stippellijn zonder getal",
            "je verandert de eenheid zodat alle staven gelijk worden",
        ],
        antwoord=0,
        uitleg="Door een uitschieter worden de andere staven piepklein. De getallen erbij houden het beeld eerlijk en leesbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Bij welke waarde hoort de verticale as van een staafdiagram te beginnen? Geef het getal in cijfers.",
        antwoord=["0", "nul"],
        uitleg="Bij nul. Begint ze hoger, dan vermeld je dat uitdrukkelijk, want anders overdrijft het beeld de verschillen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek zonder getallen op de zij-as is nog altijd bruikbaar als de vorm klopt.",
        antwoord=False,
        uitleg="Zonder schaal weet je niet of een stijging groot of klein is. Zet er een lijn met getallen bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lijndiagram toont een scherpe stijging, maar de tijdsas loopt van 2020 naar 2021 naar 2025. Wat is het probleem?",
        opties=[
            "de afstanden op de tijdsas zijn ongelijk, dus de stijging is vertekend",
            "een lijndiagram mag geen jaren op de horizontale as hebben",
            "er zijn te weinig punten om een lijn te tekenen",
            "de tijd hoort altijd op de verticale as te staan",
        ],
        antwoord=0,
        uitleg="Vier jaar krijgt dezelfde breedte als één jaar. De lijn lijkt dan veel steiler dan ze is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee groepen worden met twee histogrammen vergeleken, maar de assen hebben een andere schaal. Wat doe je?",
        opties=[
            "je maakt de assen gelijk, anders kan je de vormen niet vergelijken",
            "je legt de twee histogrammen over elkaar in één beeld",
            "je vervangt ze door twee boxplots op aparte assen",
            "je laat het zo, de vorm van elk histogram klopt apart",
        ],
        antwoord=0,
        uitleg="Vergelijken kan alleen op dezelfde schaal. Anders lijkt de ene groep breder gespreid dan ze is.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een boxplot kan je afleiden waar de helft van de middelste gegevens ligt.",
        antwoord=True,
        uitleg="Dat is precies de doos: van het eerste tot het derde kwartiel zit de middelste helft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een histogram met twee duidelijke toppen. Wat is de beste eerste gedachte?",
        opties=[
            "er zitten misschien twee verschillende groepen in de data",
            "de klassen zijn verkeerd berekend in het histogram",
            "de normale verdeling past perfect bij deze data",
            "het gemiddelde ligt onder de laagste van de twee toppen",
        ],
        antwoord=0,
        uitleg="Lengtes van mannen en vrouwen door elkaar geven zo'n beeld. Splits de data en kijk opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat de nul bij een lijndiagram van de temperatuur niet altijd op de as?",
        opties=[
            "bij een temperatuur is de nul geen natuurlijk nulpunt van de schaal",
            "een lijndiagram mag nooit een nul op de as hebben staan",
            "de nul past niet in het beeld bij grote getallen",
            "een temperatuur wordt altijd relatief weergegeven",
        ],
        antwoord=0,
        uitleg="Bij aantallen en bedragen hoort nul wel op de as. Bij een temperatuurschaal is afwijken verdedigbaar, als je het zegt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een verdeling met een lange staart naar rechts? Eén woord.",
        antwoord=["scheef", "rechtsscheef", "asymmetrisch"],
        uitleg="Scheef naar rechts, of rechtsscheef. Het gemiddelde ligt daar boven de mediaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek met driedimensionale staven leest makkelijker dan een met vlakke staven.",
        antwoord=False,
        uitleg="Omgekeerd: het perspectief maakt de hoogtes moeilijker te vergelijken. Houd een grafiek vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dotplot toont vier stippen boven de waarde zeven. Wat betekent dat?",
        opties=[
            "de waarde zeven komt vier keer voor in de dataset",
            "de waarde zeven is vier eenheden groot",
            "er zijn vier waarden kleiner dan zeven",
            "het gemiddelde van de dataset is vier",
        ],
        antwoord=0,
        uitleg="Elke stip is één meting. De hoogte van de stapel is de frequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grafiek zou je kiezen om te laten zien dat één groep veel meer uitschieters heeft?",
        opties=[
            "twee boxplots naast elkaar op dezelfde as",
            "twee lijndiagrammen in hetzelfde beeld",
            "één staafdiagram met de twee groepen",
            "één spreidingsdiagram met beide groepen",
        ],
        antwoord=0,
        uitleg="Een boxplot zet uitschieters apart als losse punten buiten de snorharen. Dat valt onmiddellijk op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafische voorstelling kan statistisch juist zijn en de lezer toch misleiden.",
        antwoord=True,
        uitleg="Alle getallen kunnen kloppen terwijl de gekozen as, de schaal of de weggelaten context het beeld vertekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderschrift bij een grafiek bevat de uitleg van de hele theorie erachter. Wat zou je aanraden?",
        opties=[
            "een onderschrift zegt wat je ziet, de theorie hoort in de tekst",
            "de theorie hoort in het onderschrift zodat alles bij elkaar staat",
            "een grafiek heeft geen onderschrift nodig als de assen benoemd zijn",
            "het onderschrift moet de belangrijkste getallen herhalen",
        ],
        antwoord=0,
        uitleg="Een onderschrift is geen les. Het zegt kort wat de lezer in dit beeld moet zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil twee grootheden met heel verschillende eenheden in één beeld vergelijken. Wat is een eerlijke aanpak?",
        opties=[
            "twee grafieken boven elkaar met dezelfde tijdsas",
            "één lijndiagram met twee verschillende verticale assen",
            "één staafdiagram waarin je de eenheden weglaat",
            "één grafiek waarin je de kleinste grootheid maal honderd neemt",
        ],
        antwoord=0,
        uitleg="Twee assen in één beeld kan je zo schalen dat elk gewenst verband eruit komt. Twee grafieken zijn eerlijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling leest uit een histogram het exacte gemiddelde af. Wat zeg je?",
        opties=[
            "uit een histogram kan je het gemiddelde enkel schatten",
            "een histogram toont het gemiddelde als de hoogste staaf",
            "het gemiddelde staat altijd precies in het midden van de as",
            "een histogram toont het gemiddelde als een verticale lijn",
        ],
        antwoord=0,
        uitleg="De klassen hebben de afzonderlijke waarden samengevat. Voor het exacte gemiddelde heb je de ruwe data nodig.",
    ),
]

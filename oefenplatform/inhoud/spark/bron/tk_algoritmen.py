# -*- coding: utf-8 -*-
"""De vragen voor "Algoritmen en computationeel denken" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Algoritmen" (10 % van het
examen): een digitaal en niet-digitaal algoritme ontwerpen volgens de principes
van computationeel denken, en het debuggen.

Deel 1 gaat over wat een algoritme is, over de stappen om er een te ontwerpen
(probleemstelling, IPO, opsplitsen, testen), over de flowchart en over Scratch.
Deel 2 gaat over abstractie, decompositie en patroonherkenning, en over
debuggen.

De fiche noemt Scratch bij naam als de taal waarin je je algoritme vertaalt.
Verder blijft alles hier taalonafhankelijk: er wordt nergens naar een blokje of
een menu gevraagd, want die veranderen met elke nieuwe versie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een algoritme?",
        opties=[
            "Een stappenplan met instructies in een vaste volgorde",
            "Een tekening van een technisch systeem met alle maten",
            "Een tabel met de afmetingen van een werkstuk erop",
            "Een lijst met alle onderdelen van een machine erin",
        ],
        antwoord=0,
        uitleg="Volg je de stappen in die volgorde, dan kom je bij het einddoel of bij de oplossing van het probleem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn algoritmen?",
        opties=[
            "Een recept om een cake te bakken",
            "Een stappenplan om een boterham te smeren",
            "De code van een computerspel",
            "Een foto van een afgewerkte taart",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het recept en het computerspel staan allebei als voorbeeld in de fiche. Een foto is geen stappenplan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een algoritme moet altijd op een computer draaien.",
        antwoord=False,
        uitleg="Een algoritme kan digitaal zijn, maar evengoed niet-digitaal. Een recept of een handleiding is ook een algoritme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een niet-digitaal algoritme?",
        opties=[
            "Een stappenplan dat je zonder computer uitvoert",
            "Een programma dat werkt zonder een beeldscherm",
            "Een algoritme dat nog niet helemaal af is",
            "Een algoritme waar nog een fout in zit",
        ],
        antwoord=0,
        uitleg="Het voorbeeld van de fiche is een stappenplan om een boterham met choco te smeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van een digitaal algoritme?",
        opties=[
            "Een lampje laten flikkeren met een programma",
            "Een boterham smeren volgens een stappenplan",
            "Een kast in elkaar zetten met een handleiding",
            "Een plant elke dag op tijd water geven",
        ],
        antwoord=0,
        uitleg="Dat voorbeeld staat in de fiche. Digitaal wil zeggen dat een computer of een microcontroller de stappen uitvoert.",
    ),
    dict(
        type="invultekst",
        vraag="Een schema met pijlen dat de stappen van een algoritme toont, heet een ___.",
        antwoord=["flowchart", "stroomdiagram"],
        uitleg="In een flowchart zie je in één oogopslag de volgorde en de keuzes. Daarom teken je er vaak eerst een voor je begint te programmeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een flowchart heet ook een stroomdiagram.",
        antwoord=True,
        uitleg="Twee namen voor hetzelfde. De fiche zet ze naast elkaar: flowchart of stroomdiagram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een flowchart?",
        opties=[
            "Om de oplossing visueel voor te stellen",
            "Om het programma sneller te laten draaien",
            "Om de kleuren van het scherm te kiezen",
            "Om de prijs van het programma te berekenen",
        ],
        antwoord=0,
        uitleg="Een flowchart structureert je oplossing en maakt ze zichtbaar. Zo merk je een gat in je redenering voor je begint te typen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke programmeertaal vertaal je volgens de vakfiche je algoritme?",
        opties=["Scratch", "Python", "Java", "HTML"],
        antwoord=0,
        uitleg="De fiche noemt Scratch bij naam. Daarin sleep je blokjes in elkaar, zodat je je op de logica kunt richten in plaats van op schrijffouten.",
    ),
    dict(
        type="waarofniet",
        vraag="In een algoritme mag je de stappen zomaar van volgorde wisselen.",
        antwoord=False,
        uitleg="De volgorde ligt vast en hoort bij de definitie. Boter smeren voor je het brood uit de zak haalt, werkt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen volg je bij het ontwerpen van een algoritme?",
        opties=[
            "Je formuleert de probleemstelling",
            "Je analyseert het probleem met IPO",
            "Je test het algoritme uit",
            "Je koopt eerst een nieuwe computer",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt die drie, plus het probleem eventueel opdelen in kleinere deelproblemen en bijsturen waar nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat IPO bij het analyseren van een probleem?",
        opties=[
            "Input, process en output",
            "Idee, plan en oplossing",
            "Invoer, programma en onderhoud",
            "Instructie, proef en oefening",
        ],
        antwoord=0,
        uitleg="Wat gaat erin, wat gebeurt ermee, en wat komt eruit. Precies hetzelfde model als bij een informatieverwerkend systeem.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor je een algoritme schrijft, bekijk je wat erin gaat en wat eruit moet komen.",
        antwoord=True,
        uitleg="Dat is de IPO-analyse. Weet je niet wat het resultaat moet zijn, dan kan je ook niet nagaan of je algoritme klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom test je een algoritme uit?",
        opties=[
            "Om te zien of het echt doet wat je wilde",
            "Om de code een stuk korter te maken",
            "Om de computer wat te laten afkoelen",
            "Om het programma te kunnen verkopen",
        ],
        antwoord=0,
        uitleg="Een algoritme dat op papier logisch lijkt, kan in het echt toch iets anders doen. Testen is de enige manier om dat te weten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een stappenplan om een boterham met choco te smeren. Wat is dat?",
        opties=[
            "Een niet-digitaal algoritme",
            "Een digitaal algoritme",
            "Een flowchart met pijlen",
            "Een waarheidstabel van een poort",
        ],
        antwoord=0,
        uitleg="Het is een algoritme, want het is een stappenplan in een vaste volgorde. Er komt geen computer aan te pas, dus niet-digitaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een algoritme kan gebruikt worden voor eenvoudige én voor ingewikkelde problemen.",
        antwoord=True,
        uitleg="Van een boterham smeren tot een computerspel programmeren. Daarom is zelf een algoritme kunnen ontwerpen voor zoveel dingen nuttig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als één stap in een algoritme ontbreekt?",
        opties=[
            "Het resultaat klopt meestal niet meer",
            "Het algoritme draait juist wat sneller",
            "Er verandert helemaal niets aan het geheel",
            "De computer vult de stap zelf wel aan",
        ],
        antwoord=0,
        uitleg="Een computer doet precies wat er staat en niets meer. Vergeet je een stap, dan wordt die niet uitgevoerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je met een algoritme laten doen?",
        opties=[
            "Controleren of een getal een priemgetal is",
            "Getallen sorteren van klein naar groot",
            "Een rechthoek laten tekenen op het scherm",
            "De computer laten voelen wat jij denkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die eerste drie staan als voorbeeld in de fiche. Voor het laatste bestaat er geen stappenplan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recept is geen algoritme.",
        antwoord=False,
        uitleg="Een recept is wel degelijk een algoritme: instructies in een vaste volgorde die naar een resultaat leiden. De fiche geeft het zelf als voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je algoritme bij het testen niet het juiste resultaat geeft?",
        opties=[
            "Je stuurt het bij",
            "Je kiest dan maar een ander probleem",
            "Je verwijdert het algoritme helemaal",
            "Je test het voortaan nooit meer uit",
        ],
        antwoord=0,
        uitleg="Testen en bijsturen horen bij elkaar. Je zoekt waar het misloopt, past aan, en test opnieuw.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke principes van computationeel denken noemt de vakfiche?",
        opties=[
            "Abstractie",
            "Decompositie",
            "Patroonherkenning",
            "Het algoritme",
            "Improvisatie",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Die vier staan samen in de fiche. Improvisatie hoort er niet bij: computationeel denken is juist het omgekeerde van improviseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is abstractie?",
        opties=[
            "Details weglaten die er niet toe doen",
            "Een probleem in kleinere stukken knippen",
            "Gelijkenissen tussen problemen opzoeken",
            "Een fout in een programma opsporen",
        ],
        antwoord=0,
        uitleg="Door het overbodige weg te laten, los je het probleem vlotter op. Een metrokaart laat ook alle straten weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is decompositie?",
        opties=[
            "Een probleem in kleinere delen opsplitsen",
            "Onbelangrijke details gewoon weglaten",
            "Een fout opsporen en daarna oplossen",
            "Een programma sneller laten draaien",
        ],
        antwoord=0,
        uitleg="Je kiest de deelproblemen goed en pakt elk deel apart aan. Samen vormen de oplossingen weer het geheel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is patroonherkenning?",
        opties=[
            "Gelijkenissen tussen problemen zien",
            "Details weglaten die niet echt helpen",
            "Een probleem in kleine stukken knippen",
            "Een programma testen op zoek naar fouten",
        ],
        antwoord=0,
        uitleg="Zie je dat een nieuw probleem lijkt op iets wat je al eens opgeloste hebt, dan kan je die oplossing hergebruiken.",
    ),
    dict(
        type="invultekst",
        vraag="Het opsporen en oplossen van een fout in een algoritme heet ___.",
        antwoord="debuggen",
        uitleg="Het woord komt van bug, het Engelse woord voor insect. Er zat ooit letterlijk een mot in een computer die daardoor fout liep.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bug is een fout in een programma.",
        antwoord=True,
        uitleg="Een bug is de fout zelf, debuggen is die fout opsporen en wegwerken.",
    ),
    dict(
        type="waarofniet",
        vraag="Abstractie betekent zoveel mogelijk details toevoegen.",
        antwoord=False,
        uitleg="Precies omgekeerd: abstractie is irrelevante details weglaten zodat je sneller tot een oplossing komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je patroonherkenning?",
        opties=[
            "Je hergebruikt een oplossing die je al kent",
            "Je maakt het programma wat kleurrijker",
            "Je maakt het probleem opzettelijk moeilijker",
            "Je hoeft je algoritme dan niet meer te testen",
        ],
        antwoord=0,
        uitleg="Werkte iets eerder al, dan hoef je het niet opnieuw uit te vinden. Dat scheelt werk en er sluipen minder fouten in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een spel heeft tien niveaus die sterk op elkaar lijken. Welk principe helpt hier?",
        opties=[
            "Patroonherkenning",
            "Debuggen van het spel",
            "Abstractie van de kleuren",
            "Een waarheidstabel opstellen",
        ],
        antwoord=0,
        uitleg="Je schrijft de logica één keer en gebruikt ze voor alle tien de niveaus, met telkens andere gegevens.",
    ),
    dict(
        type="waarofniet",
        vraag="Decompositie maakt een groot probleem overzichtelijker.",
        antwoord=True,
        uitleg="In stukken is alles behapbaar. Je kunt de delen ook verdelen over meerdere mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een algoritme om de weg naar school uit te leggen. Welk detail laat je weg?",
        opties=[
            "De kleur van de huizen onderweg",
            "De straatnamen die je moet volgen",
            "De plaatsen waar je links of rechts moet",
            "De plaatsen waar je moet oversteken",
        ],
        antwoord=0,
        uitleg="Dat is abstractie: alles wat niet helpt om er te geraken, laat je weg. De kleur van een huis helpt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat helpt je om een efficiënt algoritme te schrijven?",
        opties=[
            "Abstractie",
            "Decompositie",
            "Patroonherkenning",
            "Zoveel mogelijk stappen toevoegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie principes samen brengen je naar een zo efficiënt mogelijk algoritme. Stappen bijzetten doet net het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een fout in een algoritme vind je alleen door ernaar te kijken, nooit door het uit te voeren.",
        antwoord=False,
        uitleg="Je voert het juist stap voor stap uit tot het resultaat niet meer klopt. Daar zit de bug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een programma moet een vierkant tekenen maar maakt maar drie zijden. Wat doe je?",
        opties=[
            "Je debugt het algoritme",
            "Je begint aan een volledig nieuw programma",
            "Je verandert het vierkant dan maar in een driehoek",
            "Je laat het gewoon zo staan en gaat verder",
        ],
        antwoord=0,
        uitleg="Zoek waar het misloopt. Meestal staat de herhaling op drie in plaats van op vier, en is één cijfer veranderen genoeg.",
    ),
    dict(
        type="waarofniet",
        vraag="Efficiënt betekent dat een algoritme zoveel mogelijk stappen heeft.",
        antwoord=False,
        uitleg="Efficiënt betekent juist met zo weinig mogelijk stappen bij het doel komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van decompositie bij het maken van een spel?",
        opties=[
            "Apart werken aan de beweging, de punten en het geluid",
            "Alle kleuren van het hele spel in één keer kiezen",
            "Alle fouten in het spel in één keer proberen op te lossen",
            "Het spel in één heel lange lijst instructies schrijven",
        ],
        antwoord=0,
        uitleg="Elk stuk is apart te maken en te testen. Daarna voeg je ze samen tot het hele spel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een korter algoritme met dezelfde uitkomst meestal beter?",
        opties=[
            "Er kunnen minder fouten in sluipen",
            "Het ziet er mooier uit op papier",
            "Het is altijd sneller in te typen",
            "De computer wordt er warmer van",
        ],
        antwoord=0,
        uitleg="Minder stappen betekent minder plaatsen waar het fout kan lopen, en het is ook makkelijker te begrijpen voor wie het later leest.",
    ),
    dict(
        type="waarofniet",
        vraag="Patroonherkenning helpt je een oplossing van een eerder probleem opnieuw te gebruiken.",
        antwoord=True,
        uitleg="Dat staat zo in de fiche: overeenkomsten herkennen met een eerder opgelost probleem om de oplossing te hergebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je decompositie?",
        opties=[
            "Als een probleem te groot is voor één keer",
            "Als verschillende delen los van elkaar werken",
            "Als je met meerdere mensen samen werkt",
            "Als het probleem allang opgelost is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opsplitsen helpt zolang er nog iets op te lossen valt. Bij een probleem dat al opgelost is, gebruik je patroonherkenning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de laatste stap bij het ontwerpen van een algoritme?",
        opties=[
            "Testen en bijsturen waar nodig",
            "De probleemstelling opschrijven",
            "Het probleem in delen opsplitsen",
            "Bepalen wat de input moet zijn",
        ],
        antwoord=0,
        uitleg="Net als bij het technisch proces sluit je af met testen en bijsturen. De andere drie horen bij het begin.",
    ),
]

# -*- coding: utf-8 -*-
"""Pittige vragen bij "Algoritmen en computationeel denken" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en 2 (vaste volgorde, IPO, de vormen van een flowchart, de vier
principes, debuggen en efficiëntie), maar je moet een algoritme zelf uitvoeren, een fout
terugvinden of een principe herkennen in een nieuwe situatie.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="In een flowchart staat de stap 'Vraag de gebruiker om een getal'. In welke vorm teken je die stap?",
        opties=[
            "In een parallellogram",
            "In een rechthoek, want het is een instructie",
            "In een ruit, want er wordt iets gevraagd",
            "In een afgeronde rechthoek",
        ],
        antwoord=0,
        uitleg="Een getal vragen is invoer, en invoer of uitvoer teken je in een parallellogram. Een ruit is voor een keuze met ja of nee, niet voor elke zin met 'vraag' erin.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Volg deze flowchart. Start. Invoer: de temperatuur in de klas. Ruit: is het kouder dan \(18\) graden? Bij ja: toon 'verwarming aan' en einde. Bij nee volgt een tweede ruit: is het warmer dan \(25\) graden? Bij ja: toon 'raam open'. Bij nee: toon 'niets doen'. Einde. Wat wordt er getoond bij \(22\) graden?",
        opties=[
            "Niets doen",
            "Verwarming aan",
            "Raam open",
            "Eerst verwarming aan en daarna raam open",
        ],
        antwoord=0,
        uitleg="Bij de eerste ruit is het antwoord nee, want 22 graden is niet kouder dan 18. Bij de tweede ruit is het ook nee, want 22 is niet warmer dan 25. Je volgt telkens één pijl, dus er kan maar één uitvoer verschijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep maakt een spel. Ze verdelen het werk in de beweging, de punten en het geluid. Bij het plannen laten ze de kleur van de figuurtjes nog buiten beschouwing. Daarna schrijven ze voor elk deel de stappen in een vaste volgorde. Welk principe van computationeel denken gebruiken ze in dit verhaal NIET?",
        opties=[
            "Patroonherkenning",
            "Decompositie",
            "Abstractie",
            "Het algoritme",
        ],
        antwoord=0,
        uitleg="Het werk verdelen is decompositie, de kleur weglaten is abstractie, en stappen in een vaste volgorde schrijven is het algoritme zelf. Nergens zoeken ze gelijkenissen met een probleem dat ze al kennen, dus patroonherkenning ontbreekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je maakt een quiz in Scratch. Je merkt dat elke vraag op dezelfde manier werkt: vraag stellen, antwoord vergelijken, punt geven. Daarom schrijf je dat één keer en gebruik je het voor alle twintig vragen. Welk principe pas je toe?",
        opties=[
            "Patroonherkenning",
            "Decompositie van het spel",
            "Abstractie van de vragen",
            "Debuggen van de quiz",
        ],
        antwoord=0,
        uitleg="Je ziet een gelijkenis tussen de twintig vragen en hergebruikt dezelfde oplossing: dat is patroonherkenning. Bij decompositie zou je de quiz juist in verschillende soorten delen opsplitsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt: 'Abstractie en decompositie zijn eigenlijk hetzelfde, want bij allebei hou je minder over.' Wat is er fout aan die redenering?",
        opties=[
            "Bij decompositie laat je niets weg, je verdeelt alleen",
            "Niets, de twee woorden betekenen hetzelfde",
            "Bij abstractie voeg je net extra details toe aan het probleem",
            "Bij decompositie zoek je gelijkenissen met eerdere problemen",
        ],
        antwoord=0,
        uitleg="Abstractie laat details weg die er niet toe doen. Decompositie splitst het probleem op in kleinere delen, maar alle delen blijven nodig. Gelijkenissen zoeken is weer een derde principe: patroonherkenning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ontwerpt een algoritme dat nagaat of een getal een priemgetal is. Welke IPO-analyse klopt?",
        opties=[
            "Input: het getal; output: ja of nee",
            "Input: ja of nee; output: het getal",
            "Input: het controleren; output: het getal zelf",
            "Input: het getal; output: het controleren ervan",
        ],
        antwoord=0,
        uitleg="Wat erin gaat, is het getal. Wat eruit moet komen, is het antwoord: ja, het is een priemgetal, of nee. Het controleren zelf is het process, de P in het midden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn digitale algoritmen (meerdere antwoorden mogelijk)?",
        opties=[
            "Een programma dat getallen van klein naar groot sorteert",
            "Een programma dat een lampje laat flikkeren",
            "Een recept dat je oma je voorleest uit een kookboek",
            "Een handleiding op papier om een kast in elkaar te zetten",
            "Een stappenplan op een briefje om je fiets te poetsen",
        ],
        antwoord=[0, 1],
        uitleg="Alle vijf zijn algoritmen, maar alleen de programma's worden door een computer uitgevoerd. Een recept, een handleiding of een stappenplan voer je zelf uit: dat zijn niet-digitale algoritmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een programma moet een rechthoek tekenen, maar er verschijnt een rare figuur. Welke aanpakken helpen om de bug te vinden (meerdere antwoorden mogelijk)?",
        opties=[
            "Het programma stap voor stap uitvoeren en kijken waar het afwijkt",
            "Vergelijken wat je verwachtte met wat er echt gebeurt",
            "Nagaan of een stap ontbreekt of in de verkeerde volgorde staat",
            "Het programma helemaal wissen en aan iets anders beginnen",
            "Alleen naar de code kijken, zonder ze ooit uit te voeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Debuggen is de fout opsporen en oplossen. Vaak zie je ze pas door het algoritme uit te voeren en te vergelijken met wat je verwachtte. Alles wissen lost niets op, en alleen kijken is vaak niet genoeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een algoritme om een boterham met choco te smeren staat de stap 'Smeer choco op de boterham'. Welke stappen moeten daar zeker vóór komen (meerdere antwoorden mogelijk)?",
        opties=[
            "Haal een boterham uit de zak",
            "Leg de boterham op je bord",
            "Open de chocopot",
            "Neem een mes",
            "Eet de boterham op",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Zonder boterham, zonder open pot of zonder mes kan je niet smeren: die stappen moeten ervoor staan. Opeten komt pas daarna. Daarom ligt de volgorde in een algoritme vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stappenplan om thee te zetten luidt: 1. Zet de waterkoker aan. 2. Vul de waterkoker met water. 3. Giet het water in de tas. Wat is de bug?",
        opties=[
            r"Stap \(1\) en stap \(2\) staan in de verkeerde volgorde",
            "Er ontbreekt een ruit om een keuze te maken",
            "Een stappenplan zonder computer kan geen bug bevatten",
            r"Stap \(3\) hoort helemaal vooraan te staan",
        ],
        antwoord=0,
        uitleg="Je zet de waterkoker pas aan als er water in zit. Alle stappen zijn er, maar de volgorde klopt niet, en in een algoritme ligt de volgorde vast. Ook een niet-digitaal algoritme kan zo'n fout hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Lotte schrijft meteen een Scratch-programma voor een rekenmachine, zonder eerst na te gaan welke getallen erin gaan en wat eruit moet komen. Welke ontwerpstap sloeg ze over?",
        opties=[
            "Het analyseren met IPO",
            "Het testen en bijsturen achteraf",
            "Het vertalen van het algoritme in Scratch",
            "Het tekenen van een metrokaart van het probleem",
        ],
        antwoord=0,
        uitleg="Nagaan wat erin gaat en wat eruit moet komen, is de IPO-analyse. Vertalen in Scratch deed ze wel, en testen komt pas op het einde. Zonder IPO weet ze straks niet eens wanneer het resultaat juist is.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een flowchart staat 'Is de deur open?' in een rechthoek met maar één pijl eruit. Wat is er fout?",
        opties=[
            "Een keuze hoort in een ruit, met een pijl voor ja en een voor nee",
            "Een vraag hoort in een afgeronde rechthoek, want daar begint alles",
            "Er is niets fout, want elke stap in een flowchart is een rechthoek",
            "Een vraag hoort in een parallellogram, want het is altijd uitvoer",
        ],
        antwoord=0,
        uitleg="'Is de deur open?' is een keuze met ja of nee, en een keuze teken je in een ruit. Uit die ruit vertrekken twee pijlen, één voor elk antwoord. Een rechthoek is voor een gewone bewerking of instructie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een algoritme met meer stappen dat hetzelfde resultaat geeft, is efficiënter omdat het grondiger werkt.",
        antwoord=False,
        uitleg="Efficiënt betekent juist zo weinig mogelijk stappen. Bij dezelfde uitkomst is het kortere algoritme beter, omdat er minder fouten in kunnen sluipen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een flowchart op papier en een programma in Scratch kunnen hetzelfde algoritme voorstellen.",
        antwoord=True,
        uitleg="Met een flowchart stel je de oplossing visueel voor, en daarna vertaal je hetzelfde algoritme in Scratch. Het stappenplan blijft hetzelfde, alleen de vorm verschilt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een flowchart duidt een parallellogram een keuze aan waarbij je ja of nee volgt.",
        antwoord=False,
        uitleg="Een parallellogram is voor invoer of uitvoer. Een keuze met ja of nee teken je in een ruit.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een probleem eerst met decompositie opsplitsen en daarna bij twee deelproblemen die op elkaar lijken patroonherkenning gebruiken.",
        antwoord=True,
        uitleg="De principes van computationeel denken werken samen. Eerst knip je het probleem in delen, en lijken twee delen op elkaar, dan hergebruik je de oplossing van het ene voor het andere.",
    ),
    dict(
        type="invultekst",
        vraag="Volg deze flowchart. Start. Invoer: een getal. Ruit: is het getal groter dan 10? Bij ja: trek er 10 van af. Bij nee: tel er 5 bij op. Uitvoer: toon het getal. Einde. Welk getal wordt getoond als de invoer 10 is? Antwoord met een getal.",
        antwoord="15",
        reken="10 + 5",
        uitleg="10 is niet groter dan 10, dus volg je de pijl bij nee en tel je er 5 bij op: 15. Wie 0 antwoordt, las 'groter dan' als 'groter dan of gelijk aan'.",
    ),
    dict(
        type="invultekst",
        vraag="Een algoritme sorteert getallen van klein naar groot. De input is 8, 3 en 5. Welk getal staat als tweede in de output? Antwoord met een getal.",
        antwoord="5",
        uitleg="De output is 3, 5, 8. Wie gewoon het tweede getal van de input neemt, antwoordt 3, maar dat is de volgorde vóór het sorteren.",
    ),
    dict(
        type="invultekst",
        vraag="Een stappenplan om je klaar te maken luidt: 1. Doe je schoenen aan. 2. Trek je sokken aan. 3. Strik je veters. Het resultaat klopt niet. Welke stap moet als eerste komen? Antwoord met een getal.",
        antwoord="2",
        uitleg="Sokken moeten aan vóór je schoenen, dus stap 2 hoort vooraan. Alle stappen zijn er, alleen de volgorde is fout: zo'n bug vind je door het stappenplan in gedachten uit te voeren.",
    ),
    dict(
        type="invultekst",
        vraag="Je legt in een stappenplan de weg naar het station uit en laat de merken van de geparkeerde auto's onderweg weg. Welk principe van computationeel denken gebruik je? Antwoord met één woord.",
        antwoord="abstractie",
        uitleg="Je laat details weg die niet helpen om er te geraken: dat is abstractie. Decompositie zou betekenen dat je de route in stukken opsplitst.",
    ),
]

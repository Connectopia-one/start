# -*- coding: utf-8 -*-
"""Het rekenblad Excel.

Het tweede thema uit "ik ben digitaal vaardig", en het zwaarste van de vier:
de fiche somt voor Excel meer op dan voor Word en PowerPoint samen.

Ook hier geldt: je werkt op het examen niet met het programma zelf maar met
schermafdrukken. De vragen hieronder testen dus wat een functie doet en hoe
een formule eruitziet, niet of je snel kan klikken.

Wat de fiche opsomt:
    structuurelementen   cel, celadres, bereik, rij, kolom, werkblad, werkmap
    opmaken              lettertype, randen en opvulling, uitlijnen,
                         rijhoogte en kolombreedte, cellen samenvoegen en
                         centreren, tekststand
    bewerken             rijen en kolommen invoegen en verwijderen, cellen
                         wissen, invoegen en verwijderen
    vulgreep
    getalnotatie         valuta, percentage, aantal decimalen, datum en tijd
    voorwaardelijke opmaak
    formules             de operatoren *, -, +, / en haakjes
    adressering          absoluut en relatief
    functies             SOM, GEMIDDELDE, MIN, MAX, VERT.ZOEKEN, ALS
    grafieken            kolom, lijn, staaf, cirkel en spreiding, met hun
                         opmaak en basisbewerkingen
    afdrukken            een werkblad of een deel ervan

Twee dingen die het vaakst fout gaan en daarom hier vaak terugkomen:

  1. **Elke formule begint met een isgelijkteken.** Zonder dat teken ziet
     Excel gewoon tekst.
  2. **Absoluut tegenover relatief.** A1 schuift mee als je de formule
     kopieert, $A$1 blijft staan. Het dollarteken zet vast wat erachter komt.

Deel 1 is de structuur, de opmaak, de getalnotatie en de vulgreep.
Deel 2 is formules, functies en grafieken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een cel in Excel?",
        opties=[
            "het vakje waar een rij en een kolom elkaar kruisen",
            "een volledige rij met gegevens",
            "een blad binnen een bestand",
            "een groep vakjes die je samen selecteert",
        ],
        antwoord=0,
        uitleg="Een groep vakjes samen heet een bereik, een blad een werkblad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een celadres?",
        opties=[
            "de kolomletter en het rijnummer samen, zoals B7",
            "de naam van het werkblad",
            "de plaats waar het bestand opgeslagen staat",
            "het aantal tekens in een cel",
        ],
        antwoord=0,
        uitleg="Eerst de letter van de kolom, dan het nummer van de rij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bereik?",
        opties=[
            "een groep cellen samen, zoals A1 tot en met A10",
            "één enkele cel",
            "een volledig werkblad",
            "het verschil tussen het grootste en het kleinste getal",
        ],
        antwoord=0,
        uitleg="Je noteert het met een dubbelpunt: A1:A10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een werkblad en een werkmap?",
        opties=[
            "een werkmap is het bestand, een werkblad is één tabblad erin",
            "een werkblad is het bestand, een werkmap is één tabblad erin",
            "ze betekenen hetzelfde",
            "een werkmap is een map op je computer",
        ],
        antwoord=0,
        uitleg="Eén werkmap kan veel werkbladen bevatten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de vulgreep?",
        opties=[
            "snel gegevens of formules doortrekken naar andere cellen",
            "de kolom breder maken tot de inhoud er volledig in past",
            "een cel of een hele rij met een achtergrondkleur opvullen",
            "een grafiek vergroten door aan de hoek ervan te trekken",
        ],
        antwoord=0,
        uitleg="Het vierkantje rechtsonder in de selectie, waarmee je sleept.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke getalnotatie gebruik je voor een bedrag in euro?",
        opties=["valuta", "percentage", "datum", "tekst"],
        antwoord=0,
        uitleg="De valutanotatie zet het muntteken erbij en lijnt de bedragen netjes uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je typt 0,25 in een cel met percentagenotatie. Wat zie je?",
        opties=["25%", "0,25%", "2,5%", "250%"],
        antwoord=0,
        uitleg="De percentagenotatie toont het getal maal honderd met een procentteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet voorwaardelijke opmaak?",
        opties=[
            "een cel automatisch opmaken als de inhoud aan een voorwaarde voldoet",
            "de cel opmaken zoals de cel ernaast",
            "een formule enkel uitvoeren onder een voorwaarde",
            "de opmaak van het hele werkblad vastzetten",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld elk getal onder nul vanzelf in het rood.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet samenvoegen en centreren?",
        opties=[
            "van meerdere cellen één cel maken met de tekst in het midden",
            "twee werkbladen van hetzelfde bestand tot één blad samenvoegen",
            "de getallen in een kolom optellen en de som eronder zetten",
            "de breedte van de geselecteerde kolommen aan elkaar gelijk maken",
        ],
        antwoord=0,
        uitleg="Handig voor een titel boven een tabel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de tekststand in de celopmaak?",
        opties=[
            "de hoek waaronder de tekst in de cel staat",
            "de plaats van de tekst links of rechts",
            "het lettertype van de tekst",
            "of de tekst vet staat",
        ],
        antwoord=0,
        uitleg="Zo kan je een smalle kolomtitel schuin of verticaal zetten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkmap kan meerdere werkbladen bevatten.",
        antwoord=True,
        uitleg="De werkmap is het bestand, elk tabblad is een werkblad.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bereik noteer je met een puntkomma tussen de twee celadressen.",
        antwoord=False,
        uitleg="Met een dubbelpunt: A1:A10. De puntkomma scheidt losse argumenten.",
    ),
    dict(
        type="waarofniet",
        vraag="Met de vulgreep kan je ook formules doortrekken.",
        antwoord=True,
        uitleg="De relatieve adressen schuiven dan mee op.",
    ),
    dict(
        type="waarofniet",
        vraag="Voorwaardelijke opmaak verandert de waarde in de cel.",
        antwoord=False,
        uitleg="Ze verandert enkel het uitzicht, niet de inhoud.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuurelementen van een rekenblad noemt de fiche?",
        opties=["de cel en het celadres", "het bereik", "het werkblad en de werkmap", "de grafiek"],
        antwoord=[0, 1, 2],
        uitleg="Een grafiek is geen structuurelement. Rij en kolom horen er ook bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke getalnotaties noemt de fiche?",
        opties=["valuta", "percentage", "datum en tijd", "formule"],
        antwoord=[0, 1, 2],
        uitleg="Een formule is geen notatie. Het aantal decimalen hoort er wel bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noteer je het bereik van cel C2 tot en met C9? Antwoord zoals Excel het schrijft.",
        antwoord=["C2:C9", "c2:c9"],
        uitleg="Een dubbelpunt tussen de eerste en de laatste cel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het vierkantje rechtsonder in een selectie waarmee je gegevens doortrekt?",
        antwoord=["vulgreep", "de vulgreep"],
        uitleg="Sleep eraan en Excel vult de volgende cellen aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de opmaak die een cel vanzelf kleurt als de inhoud aan een regel voldoet? Vul aan: ... opmaak.",
        antwoord=["voorwaardelijke", "voorwaardelijk"],
        uitleg="Bijvoorbeeld alle negatieve getallen in het rood.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil tussen rij 4 en rij 5 een nieuwe rij. Wat doe je?",
        opties=[
            "rij 5 selecteren en een rij invoegen",
            "rij 4 wissen en opnieuw typen",
            "de kolombreedte aanpassen",
            "de cellen samenvoegen",
        ],
        antwoord=0,
        uitleg="Een nieuwe rij komt boven de geselecteerde rij te staan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarmee begint elke formule in Excel?",
        opties=["met een isgelijkteken", "met een plusteken", "met een haakje", "met het woord formule"],
        antwoord=0,
        uitleg="Zonder dat teken ziet Excel enkel tekst en rekent het niets uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke operatoren noemt de fiche voor formules?",
        opties=[
            "maal, min, plus, gedeeld door en haakjes",
            "enkel plus en min",
            "machtsverheffen en worteltrekken",
            "groter dan en kleiner dan",
        ],
        antwoord=0,
        uitleg="De fiche schrijft ze als *, -, +, / en ().",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de functie SOM?",
        opties=[
            "alle getallen in een bereik optellen",
            "het gemiddelde van een bereik berekenen",
            "het grootste getal zoeken",
            "het aantal cellen tellen",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld =SOM(B2:B10).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de functie GEMIDDELDE?",
        opties=[
            "de getallen optellen en delen door hun aantal",
            "het middelste getal van een reeks zoeken",
            "het verschil tussen het grootste en het kleinste getal geven",
            "het meest voorkomende getal zoeken",
        ],
        antwoord=0,
        uitleg="Het middelste getal is de mediaan, en dat is een andere functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen MIN en MAX?",
        opties=[
            "het kleinste en het grootste getal uit een bereik geven",
            "het eerste en het laatste getal uit een bereik geven",
            "de minimale en maximale kolombreedte instellen",
            "het bereik verkleinen of vergroten",
        ],
        antwoord=0,
        uitleg="MIN is de kleinste waarde, MAX de grootste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen A1 en $A$1 in een formule?",
        opties=[
            "A1 schuift mee als je de formule kopieert, $A$1 blijft staan",
            "$A$1 schuift mee, A1 blijft staan",
            "$A$1 betekent dat de cel een bedrag bevat",
            "er is geen verschil",
        ],
        antwoord=0,
        uitleg="Het dollarteken zet vast wat erachter komt: de kolom, de rij of allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt in C1 het btw-percentage staan en wil in kolom C de btw van elke prijs berekenen. Welke verwijzing gebruik je naar C1?",
        opties=[
            "een absolute verwijzing met dollartekens",
            "een relatieve verwijzing zonder dollartekens",
            "een verwijzing naar een ander werkblad",
            "een bereik",
        ],
        antwoord=0,
        uitleg="Zonder dollartekens zou C1 mee opschuiven naar C2, C3 en zo verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de functie ALS?",
        opties=[
            "een ander resultaat geven naargelang een voorwaarde waar of niet waar is",
            "een cel enkel opmaken onder een voorwaarde",
            "een rij verbergen als ze leeg is",
            "een formule stoppen bij een fout",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld geslaagd of niet geslaagd, naargelang het punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de functie VERT.ZOEKEN?",
        opties=[
            "een waarde opzoeken in de eerste kolom van een tabel en iets uit dezelfde rij teruggeven",
            "een waarde opzoeken in de eerste rij van een tabel",
            "een kolom verticaal sorteren",
            "alle lege cellen in een kolom zoeken",
        ],
        antwoord=0,
        uitleg="Vert staat voor verticaal: het zoekt naar beneden in een kolom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grafiek past het best om het aandeel van elk deel in een geheel te tonen?",
        opties=["een cirkeldiagram", "een lijngrafiek", "een spreidingsdiagram", "een kolomgrafiek"],
        antwoord=0,
        uitleg="Een cirkel toont delen van een geheel, samen honderd procent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een formule in Excel hoeft niet met een isgelijkteken te beginnen.",
        antwoord=False,
        uitleg="Zonder dat teken blijft het gewoon tekst in de cel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij $A$1 blijft de verwijzing naar dezelfde cel wijzen als je de formule kopieert.",
        antwoord=True,
        uitleg="Dat is wat absoluut adresseren betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lijngrafiek past goed om een evolutie in de tijd te tonen.",
        antwoord=True,
        uitleg="De lijn laat zien hoe iets stijgt of daalt over de maanden of jaren.",
    ),
    dict(
        type="waarofniet",
        vraag="GEMIDDELDE en MIN geven altijd hetzelfde resultaat.",
        antwoord=False,
        uitleg="Alleen als alle getallen gelijk zijn vallen ze samen. Anders geeft MIN het kleinste getal en GEMIDDELDE het gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functies noemt de fiche voor Excel?",
        opties=["SOM", "GEMIDDELDE", "VERT.ZOEKEN", "AFRONDEN"],
        antwoord=[0, 1, 2],
        uitleg="AFRONDEN staat niet in de fiche. MIN, MAX en ALS wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grafiektypes noemt de fiche?",
        opties=["de kolomgrafiek", "de lijngrafiek", "het cirkeldiagram", "de boxplot"],
        antwoord=[0, 1, 2],
        uitleg="Een boxplot staat niet in de fiche. De staafgrafiek en de spreiding wel.",
    ),
    dict(
        type="invultekst",
        vraag="Welke functie telt alle getallen in een bereik op? Antwoord met de Nederlandse naam.",
        antwoord=["SOM", "som"],
        uitleg="Bijvoorbeeld =SOM(A1:A20).",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken zet je voor een kolomletter of een rijnummer om de verwijzing vast te zetten?",
        antwoord=["$", "dollarteken", "het dollarteken"],
        uitleg="$A$1 blijft staan, A1 schuift mee.",
    ),
    dict(
        type="invultekst",
        vraag="Welke functie geeft een ander resultaat naargelang een voorwaarde klopt? Antwoord met de Nederlandse naam.",
        antwoord=["ALS", "als"],
        uitleg="Bijvoorbeeld =ALS(B2>=50;\"geslaagd\";\"niet geslaagd\").",
    ),
    dict(
        type="meerkeuze",
        vraag="In B2 staat =SOM(A1:A3) en je sleept die formule naar B3. Wat staat er dan?",
        opties=["=SOM(A2:A4)", "=SOM(A1:A3)", "=SOM(B1:B3)", "=SOM(A1:A4)"],
        antwoord=0,
        uitleg="De verwijzingen zijn relatief, dus ze schuiven één rij mee naar beneden.",
    ),
]

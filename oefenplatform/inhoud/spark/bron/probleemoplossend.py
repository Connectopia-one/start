# -*- coding: utf-8 -*-
"""De vragen voor "Probleemoplossend denken" (✨ Spark, wiskunde).

De vakfiche zegt over dit onderdeel: je lost opgaven op door een strategie te
kiezen, je zet een probleem om in wiskundetaal en terug, en je kijkt achteraf
na of je antwoord kan kloppen. De vier stappen die de fiche noemt zijn: begrijp
het probleem, maak een plan, voer het plan uit, reflecteer.

Daarom staan hier vooral echte vraagstukken, en gaat maar een handvol vragen
over de strategie zelf. Een kind leert dit door het te doen, niet door de
namen van de heuristieken op te zeggen.

Deel 1 blijft bij opgaven van één of twee stappen. Deel 2 vraagt terugrekenen,
alle mogelijkheden overlopen, patronen zien en volhouden over meer stappen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Een fles water kost € 1,20. Hoeveel kosten er zeven?",
        opties=["€ 8,40", "€ 7,20", "€ 84"],
        antwoord=0,
        uitleg="7 × € 1,20 = € 8,40. Reken even na of het kan kloppen: zeven flessen van iets meer dan een euro moet iets meer dan zeven euro zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een opgave en je snapt niet meteen wat er gevraagd wordt. Wat doe je het best eerst?",
        opties=[
            "De opgave nog eens lezen en opschrijven wat je weet en wat je zoekt",
            "Alle getallen die je ziet bij elkaar optellen",
            "Naar de volgende vraag gaan",
        ],
        antwoord=0,
        uitleg="De eerste stap is altijd: begrijp het probleem. Pas als je weet wat gegeven is en wat gevraagd wordt, kan je een plan maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas van 24 leerlingen is een derde afwezig. Hoeveel leerlingen zijn er aanwezig?",
        opties=["16", "8", "21"],
        antwoord=0,
        uitleg="Een derde van 24 is 8, dus er zijn er 8 afwezig. Aanwezig: 24 − 8 = 16. Let op dat er naar de aanwezigen gevraagd wordt, niet naar de afwezigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoekige tuin is 12 m lang en 8 m breed. Hoeveel meter draad heb je nodig om er een hek rond te zetten?",
        opties=["40 m", "96 m", "20 m"],
        antwoord=0,
        uitleg="Rond de tuin is de omtrek: 2 × (12 + 8) = 40 m. Met 12 × 8 zou je de oppervlakte krijgen, en die staat in m², niet in m.",
    ),
    dict(
        type="invultekst",
        vraag="Een trein vertrekt om 9.45 u en rijdt 2 uur en 20 minuten. Hoe laat komt hij aan? (bijvoorbeeld 14.05)",
        antwoord="12.05",
        uitleg="9.45 u + 2 u = 11.45 u, en daar nog 20 minuten bij. 11.45 u + 15 min is 12.00 u, en nog 5 minuten geeft 12.05 u.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie vrienden delen € 45 eerlijk. Daarna geeft ieder € 2 aan een goed doel. Hoeveel houdt ieder over?",
        opties=["€ 13", "€ 15", "€ 39"],
        antwoord=0,
        uitleg="Eerst delen: 45 : 3 = € 15 per persoon. Dan elk € 2 af: 15 − 2 = € 13. Doe de stappen in de volgorde waarin ze gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een pak van 500 g koekjes kost € 3. Wat betaal je voor een kilo?",
        opties=["€ 6", "€ 1,50", "€ 3"],
        antwoord=0,
        uitleg="Een kilo is 1000 g, dus twee pakken: 2 × € 3 = € 6. Hier helpt een verhoudingstabel: 500 g ↔ € 3, dus 1000 g ↔ € 6.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je antwoord op een vraagstuk onmogelijk is (bijvoorbeeld een leeftijd van 200 jaar), mag je het toch opschrijven zolang je berekening netjes is.",
        antwoord=False,
        uitleg="Nee. De laatste stap is reflecteren: kan dit antwoord kloppen? Een onmogelijk antwoord betekent dat er iets misging, en dan zoek je de fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een film duurt 105 minuten. Hoe lang is dat in uren en minuten?",
        opties=["1 u 45 min", "1 u 5 min", "2 u 5 min"],
        antwoord=0,
        uitleg="105 : 60 = 1, met 45 over. Dus 1 uur en 45 minuten. Een uur heeft 60 minuten, geen 100.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je koopt vier broodjes van € 2,50 en betaalt met € 20. Hoeveel krijg je terug?",
        opties=["€ 10", "€ 17,50", "€ 12"],
        antwoord=0,
        uitleg="Vier broodjes: 4 × € 2,50 = € 10. Terug: 20 − 10 = € 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een handige eerste stap bij een vraagstuk met veel gegevens door elkaar?",
        opties=[
            "De gegevens in een tabel of schema zetten",
            "Beginnen met het grootste getal",
            "Meteen een formule opschrijven",
        ],
        antwoord=0,
        uitleg="Gegevens ordenen in een tabel of schema maakt zichtbaar wat bij wat hoort. Dat is een van de strategieën die de vakfiche noemt.",
    ),
    dict(
        type="invultekst",
        vraag="Een zwembad van 25 meter lang: hoeveel volledige lengtes zwem je als je 1 kilometer zwemt?",
        antwoord="40",
        uitleg="Een kilometer is 1000 m. 1000 : 25 = 40 lengtes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt 15 km per uur. Hoe lang doet hij over 45 km?",
        opties=["3 uur", "30 minuten", "60 uur"],
        antwoord=0,
        uitleg="45 : 15 = 3 uur. Controleer het omgekeerd: 3 uur aan 15 km per uur is 45 km.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een doos zitten 6 rijen van 8 chocolaatjes. Er zijn er al 12 op. Hoeveel blijven er over?",
        opties=["36", "48", "26"],
        antwoord=0,
        uitleg="Eerst het totaal: 6 × 8 = 48. Dan eraf: 48 − 12 = 36.",
    ),
    dict(
        type="waarofniet",
        vraag="Schatten voor je rekent, is tijdverlies.",
        antwoord=False,
        uitleg="Schatten kost weinig tijd en laat je meteen zien of je uitkomst in de buurt ligt. Het is een van de strategieën uit de vakfiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een recept voor 4 personen vraagt 300 g rijst. Hoeveel heb je nodig voor 6 personen?",
        opties=["450 g", "500 g", "400 g"],
        antwoord=0,
        uitleg="Ga eerst naar één persoon: 300 : 4 = 75 g. Dan maal zes: 6 × 75 = 450 g.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boek heeft 240 bladzijden. Je leest er elke dag 30. Op welke dag ben je klaar?",
        opties=["De achtste dag", "De zevende dag", "De tiende dag"],
        antwoord=0,
        uitleg="240 : 30 = 8, dus na acht dagen ben je rond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gsm kost € 240. Je spaart € 15 per week. Na hoeveel weken heb je genoeg?",
        opties=["16 weken", "15 weken", "24 weken"],
        antwoord=0,
        uitleg="240 : 15 = 16 weken. Controleer: 16 × 15 = 240.",
    ),
    dict(
        type="invultekst",
        vraag="Je hebt drie truien en twee broeken. Hoeveel verschillende combinaties kan je aantrekken?",
        antwoord="6",
        uitleg="Bij elke trui passen twee broeken: 3 × 2 = 6. Je kan ze ook alle zes opschrijven, dat is ook een strategie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rekent uit dat een klas van 25 leerlingen samen 3 potloden heeft. Wat doe je?",
        opties=[
            "Je berekening opnieuw nakijken, want dit klinkt onwaarschijnlijk",
            "Het antwoord opschrijven, want je hebt netjes gerekend",
            "Het getal afronden naar 25",
        ],
        antwoord=0,
        uitleg="Reflecteren hoort bij het oplossen. Een antwoord dat niet plausibel is, is een teken dat er ergens een stap misliep.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Ik denk aan een getal, tel er 7 bij op en vermenigvuldig het resultaat met 3. Ik krijg 36. Aan welk getal dacht ik?",
        opties=["5", "12", "9"],
        antwoord=0,
        uitleg="Reken terug, van achter naar voor: 36 : 3 = 12, en 12 − 7 = 5. Controleer vooruit: (5 + 7) × 3 = 36.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rij begint met 2, 5, 11, 23, … Welk getal komt er daarna?",
        opties=["47", "35", "46"],
        antwoord=0,
        uitleg="Elk getal is het vorige maal 2 plus 1: 2 → 5 → 11 → 23 → 47. Zoek bij een rij altijd eerst naar het verband tussen twee opeenvolgende getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een parking staan auto's en motors: samen 20 voertuigen en 70 wielen. Hoeveel motors staan er?",
        opties=["5", "10", "15"],
        antwoord=0,
        uitleg="Stel dat het allemaal auto's waren: 20 × 4 = 80 wielen, dat is er 10 te veel. Elke motor scheelt 2 wielen, dus 10 : 2 = 5 motors. Controleer: 5 motors (10 wielen) en 15 auto's (60 wielen) is 70.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel getallen van twee cijfers kan je maken met de cijfers 1, 2 en 3 als elk cijfer maar één keer gebruikt mag worden?",
        opties=["6", "9", "3"],
        antwoord=0,
        uitleg="Schrijf ze allemaal op: 12, 13, 21, 23, 31, 32. Dat zijn er 6. Drie keuzes voor het eerste cijfer, en dan nog twee over voor het tweede: 3 × 2 = 6.",
    ),
    dict(
        type="invultekst",
        vraag="Een kaars van 20 cm brandt 3 cm per uur op. Na hoeveel uur is ze nog 5 cm lang?",
        antwoord="5",
        uitleg="Er moet 20 − 5 = 15 cm wegbranden, en dat gaat 3 cm per uur: 15 : 3 = 5 uur. Let op dat er niet gevraagd wordt hoe lang ze helemaal opbrandt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie vrienden zitten aan een tafel. Ieder geeft ieder ander een hand. Hoeveel handdrukken zijn er?",
        opties=["3", "6", "9"],
        antwoord=0,
        uitleg="Noem ze A, B en C: AB, AC en BC. Dat zijn er 3. AB en BA is dezelfde handdruk, dus je mag niet gewoon 3 × 2 doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trui kost na 20 % korting € 32. Wat was de oude prijs?",
        opties=["€ 40", "€ 38,40", "€ 52"],
        antwoord=0,
        uitleg="€ 32 is 80 % van de oude prijs. Dus de oude prijs is 32 : 0,80 = € 40. Controleer: 20 % van 40 is 8, en 40 − 8 = 32.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kraan vult een vat in 6 uur, een tweede kraan doet er 12 uur over. Hoe lang duurt het als ze samen lopen?",
        opties=["4 uur", "9 uur", "18 uur"],
        antwoord=0,
        uitleg="Kijk naar 12 uur: de eerste kraan vult in die tijd 2 vaten, de tweede 1 vat. Samen 3 vaten in 12 uur, dus 1 vat in 4 uur. Samen gaat het altijd sneller dan de snelste alleen, dus 9 of 18 uur kon al niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel keer schrijf je het cijfer 1 als je alle getallen van 1 tot en met 20 opschrijft?",
        antwoord="12",
        uitleg="1 en 10 tot 19 geven elk één 1 op de plaats van de tientallen of de eenheden: 1, 10, 11 (twee keer), 12, 13, 14, 15, 16, 17, 18, 19. Samen 12.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tuin van 20 m lang krijgt om de 4 meter een paal, ook aan het begin en aan het einde. Hoeveel palen zijn er?",
        opties=["6", "5", "4"],
        antwoord=0,
        uitleg="20 : 4 = 5 tussenruimtes, maar palen staan op de grenzen: 5 + 1 = 6. Dit heet de paalfout; maak bij twijfel een tekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een som van drie opeenvolgende getallen is 48. Wat is het kleinste?",
        opties=["15", "16", "14"],
        antwoord=0,
        uitleg="Het middelste is 48 : 3 = 16, dus de getallen zijn 15, 16 en 17. Controleer: 15 + 16 + 17 = 48.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je koopt 3 kg appels en 2 kg peren voor € 11. Appels kosten € 2 per kilo. Wat kost een kilo peren?",
        opties=["€ 2,50", "€ 2", "€ 5"],
        antwoord=0,
        uitleg="De appels kosten 3 × € 2 = € 6. Blijft over voor de peren: 11 − 6 = € 5, voor 2 kilo. Dus 5 : 2 = € 2,50 per kilo.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een strategie niet werkt, is het slim om een andere te proberen in plaats van dezelfde weg te blijven gaan.",
        antwoord=True,
        uitleg="Juist. Terugkijken op je aanpak en die bijstellen hoort bij het oplossen. Een schets, een tabel of terugrekenen kan opeens wel werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zaal heeft rijen van 14 stoelen. Er komen 100 mensen. Hoeveel rijen zijn er nodig?",
        opties=["8", "7", "14"],
        antwoord=0,
        uitleg="100 : 14 = 7, met 2 over. Die 2 mensen hebben ook een stoel nodig, dus 8 rijen. Bij zo'n vraag rond je altijd naar boven af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het is nu 14.00 u. Hoe laat is het over 100 uur?",
        opties=["18.00 u", "16.00 u", "20.00 u"],
        antwoord=0,
        uitleg="100 : 24 = 4 volle dagen met 4 uur over. Vier dagen later is het weer 14.00 u, plus 4 uur is 18.00 u.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel kleine kubusjes zitten er in een kubus van 3 bij 3 bij 3?",
        antwoord="27",
        uitleg="3 × 3 × 3 = 27. Een laag is 3 × 3 = 9 kubusjes, en er zijn drie lagen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Anna is nu 12 en haar mama 40. Over hoeveel jaar is haar mama precies dubbel zo oud als Anna?",
        opties=["16 jaar", "14 jaar", "28 jaar"],
        antwoord=0,
        uitleg="Het verschil blijft altijd 28 jaar. Als mama dubbel zo oud is, is dat verschil gelijk aan Anna's leeftijd, dus Anna is dan 28 en mama 56. Dat is over 28 − 12 = 16 jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel verkoopt 4 flessen voor de prijs van 3. Eén fles kost € 2. Hoeveel procent korting krijg je op de vier samen?",
        opties=["25 %", "33 %", "20 %"],
        antwoord=0,
        uitleg="Vier flessen kosten normaal € 8, nu betaal je € 6. De korting is € 2 op € 8, en 2 : 8 = 0,25, dus 25 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdeelt 100 snoepjes over een aantal kinderen, elk evenveel, en er blijven er 4 over. Hoeveel kinderen kunnen er zijn?",
        opties=["8", "7", "9"],
        antwoord=0,
        uitleg="Er zijn 100 − 4 = 96 snoepjes eerlijk verdeeld, dus het aantal kinderen is een deler van 96. Van de drie is enkel 8 dat. En er moeten meer dan 4 kinderen zijn, anders kon je de rest nog verdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de laatste stap bij het oplossen van een vraagstuk?",
        opties=[
            "Nakijken of je antwoord de gestelde vraag beantwoordt",
            "De berekening netjes overschrijven",
            "Het grootste getal onderstrepen",
        ],
        antwoord=0,
        uitleg="Reflecteren: klopt het antwoord, is het mogelijk, en geeft het écht antwoord op wat er gevraagd werd? Een juist getal bij de verkeerde vraag is nog altijd fout.",
    ),
]

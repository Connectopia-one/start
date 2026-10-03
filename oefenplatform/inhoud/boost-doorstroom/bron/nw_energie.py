# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Arbeid, energie, vermogen en rendement.

Fysica, de koppen "Arbeid", "Energieomzettingen" en "Vermogen - rendement"
van de vakfiche natuurwetenschappen 2de graad doorstroom. Deel 1 gaat over
arbeid, de energievormen, het behoud van energie en de energiedissipatie;
deel 2 over het rekenen met de drie mechanische energievormen, het vermogen
en het rendement.

Arbeid staat alleen in de uitgebreide fiche (moderne talen en Latijn).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een kracht arbeid op een voorwerp?",
        opties=[
            "als het voorwerp zich verplaatst terwijl die kracht erop werkt",
            "als de kracht groot genoeg is, ook al blijft het voorwerp staan",
            "als het voorwerp zwaar is en de kracht er loodrecht op staat",
            "als de kracht lang genoeg blijft duwen tegen een vaste muur",
        ],
        antwoord=0,
        uitleg="Zonder verplaatsing is er geen arbeid. Duw je tegen een muur die niet beweegt, dan verricht je in de natuurkundige zin geen arbeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van arbeid en van energie?",
        opties=["de joule", "de newton", "de watt", "de pascal"],
        antwoord=0,
        uitleg="Eén joule is één newton over één meter. De watt is de eenheid van vermogen, dus joule per seconde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht die loodrecht op de verplaatsing staat, verricht geen arbeid.",
        antwoord=True,
        uitleg="De cosinus van 90 graden is nul. Daarom verricht de normaalkracht op een voorwerp dat horizontaal schuift geen arbeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is de arbeid van een kracht negatief?",
        opties=[
            "als de kracht tegengesteld aan de verplaatsing werkt",
            "als de kracht in dezelfde zin als de verplaatsing werkt",
            "als de kracht loodrecht op de verplaatsing werkt",
            "als de kracht op een voorwerp in rust blijft werken",
        ],
        antwoord=0,
        uitleg="De wrijvingskracht is daar het voorbeeld van. Zij haalt energie uit de beweging in plaats van ze toe te voegen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de energie die een voorwerp heeft omdat het beweegt?",
        antwoord="kinetische energie",
        uitleg="Ze hangt af van de massa en van het kwadraat van de snelheid. Twee keer zo snel betekent dus vier keer zo veel kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievormen zijn het? Kruis alles aan wat juist is.",
        opties=[
            "chemische energie",
            "stralingsenergie",
            "kernenergie",
            "wrijvingsenergie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wrijving is een kracht en zet energie om in warmte, maar is zelf geen energievorm. Thermische energie is de vorm die daarbij ontstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de wet van behoud van energie kan energie niet verdwijnen, enkel van vorm veranderen.",
        antwoord=True,
        uitleg="Wat je aan de ene kant verliest, vind je ergens anders terug. Vaak is dat als warmte, en die is moeilijker opnieuw te gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er bij een vallende steen?",
        opties=[
            "gravitationele potentiële energie wordt kinetische energie",
            "kinetische energie wordt gravitationele potentiële energie",
            "elastische potentiële energie wordt chemische energie",
            "chemische energie wordt stralingsenergie en daarna warmte",
        ],
        antwoord=0,
        uitleg="Hoe lager de steen komt, hoe minder hoogte-energie hij heeft en hoe sneller hij gaat. De som van de twee blijft gelijk zolang je de wrijving verwaarloost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is energiedissipatie?",
        opties=[
            "bruikbare energie die omgezet wordt in een minder bruikbare vorm",
            "energie die bij een omzetting volledig uit het systeem verdwijnt",
            "energie die bij een omzetting uit het niets ontstaat in het systeem",
            "energie die van de ene plaats naar de andere wordt overgebracht",
        ],
        antwoord=0,
        uitleg="Meestal is die minder bruikbare vorm warmte. De energie is er nog wel, maar je kan er weinig nuttigs meer mee doen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de energie die een voorwerp heeft door zijn hoogte boven de grond?",
        antwoord="gravitationele potentiële energie",
        uitleg="Ze is massa maal zwaarteveldsterkte maal hoogte. Daarom slaat een stuwmeer hoog in de bergen zo veel energie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er in een lamp op het net?",
        opties=[
            "elektrische energie wordt stralingsenergie en warmte",
            "chemische energie wordt elektrische energie en warmte",
            "kernenergie wordt rechtstreeks stralingsenergie in de lamp",
            "kinetische energie wordt stralingsenergie in de gloeidraad",
        ],
        antwoord=0,
        uitleg="Het licht is de nuttige energie, de warmte is de ongewenste. Bij een gloeilamp is dat laatste het grootste deel.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesloten systeem gaat er geen energie en geen materie naar buiten of naar binnen.",
        antwoord=False,
        uitleg="Een gesloten systeem wisselt wel energie uit, maar geen materie. Pas in een geïsoleerd systeem gaat ook geen energie naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rekt een katapult uit. Welke energievorm sla je daarmee op?",
        opties=[
            "elastische potentiële energie",
            "gravitationele potentiële energie",
            "kinetische energie",
            "chemische energie",
        ],
        antwoord=0,
        uitleg="Die energie zit in de vervorming van het elastiek. Laat je los, dan wordt ze kinetische energie van het projectiel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een rem warm als je met de fiets afdaalt en blijft remmen?",
        opties=[
            "de kinetische energie van de fiets wordt door wrijving warmte",
            "de rem haalt warmte uit de lucht die eromheen langs stroomt",
            "de chemische energie in het remblokje komt daarbij vrij",
            "de hoogte-energie van de fiets wordt rechtstreeks stralingsenergie",
        ],
        antwoord=0,
        uitleg="De wrijvingskracht verricht negatieve arbeid op de fiets. Die energie moet ergens heen, en dat wordt warmte in de rem.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een energieomzetting is de nuttige energie altijd gelijk aan de totale energie.",
        antwoord=False,
        uitleg="Er gaat bijna altijd een deel naar een ongewenste vorm, meestal warmte. Daarom is het rendement nooit honderd procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gewicht hangt stil aan een koord. Welke arbeid verricht de spankracht?",
        opties=[
            "geen arbeid, want er is geen verplaatsing",
            "positieve arbeid, want de kracht is naar boven gericht",
            "negatieve arbeid, want de kracht werkt tegen de zwaartekracht in",
            "evenveel arbeid als de zwaartekracht maar in tegengestelde zin",
        ],
        antwoord=0,
        uitleg="Arbeid vraagt kracht én verplaatsing. Blijft het gewicht hangen, dan is de arbeid van elke kracht erop nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheden worden voor energie gebruikt? Kruis alles aan wat juist is.",
        opties=["de joule", "het kilowattuur", "de kilocalorie", "de newton"],
        antwoord=[0, 1, 2],
        uitleg="Op je elektriciteitsfactuur staat kilowattuur, op een voedingslabel kilocalorie. De newton is de eenheid van kracht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een systeem dat energie met zijn omgeving uitwisselt maar geen materie?",
        antwoord="gesloten systeem",
        uitleg="Een kookpot met een deksel erop benadert dat. Een open pot laat ook damp naar buiten en is dus een open systeem.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stroomdiagram toont hoe de energie bij een omzetting over de verschillende vormen verdeeld wordt.",
        antwoord=True,
        uitleg="De breedte van de pijlen geeft dan hoeveel energie naar welke vorm gaat. Alles wat er in gaat, moet er ook weer uit komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt een doos van 3 meter ver met een kracht van 40 newton in de zin van de beweging. Hoeveel arbeid verricht je?",
        opties=["120 joule", "43 joule", "13 joule", "40 joule"],
        antwoord=0,
        uitleg="Je vermenigvuldigt de kracht met de verplaatsing: 40 maal 3. Werkt de kracht onder een hoek, dan komt er nog een cosinus bij.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de kinetische energie van een voorwerp?",
        opties=[
            "de massa maal het kwadraat van de snelheid, gedeeld door twee",
            "de massa maal de snelheid, gedeeld door twee",
            "het kwadraat van de massa maal de snelheid, gedeeld door twee",
            "de massa maal de snelheid maal de zwaarteveldsterkte",
        ],
        antwoord=0,
        uitleg="Omdat de snelheid in het kwadraat staat, weegt die zwaar door. Twee keer zo snel rijden geeft vier keer zo veel energie om weg te remmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp van 2 kilogram beweegt met 3 meter per seconde. Hoeveel kinetische energie heeft het?",
        opties=["9 joule", "6 joule", "18 joule", "3 joule",],
        antwoord=0,
        uitleg="Je rekent de helft van 2 maal 9. Dat geeft 9 joule.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie twee keer zo snel rijdt, heeft vier keer zo veel kinetische energie.",
        antwoord=True,
        uitleg="De snelheid staat in het kwadraat. Daarom wordt de remweg bij dubbele snelheid veel meer dan dubbel zo lang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de gravitationele potentiële energie van een voorwerp?",
        opties=[
            "de massa maal de zwaarteveldsterkte maal de hoogte",
            "de massa maal de hoogte, gedeeld door de zwaarteveldsterkte",
            "de massa maal het kwadraat van de hoogte, gedeeld door twee",
            "de zwaarteveldsterkte maal de hoogte, gedeeld door de massa",
        ],
        antwoord=0,
        uitleg="Hoe hoger en hoe zwaarder, hoe meer energie. Op de maan is die energie bij dezelfde hoogte zes keer kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de eenheid van vermogen?",
        antwoord="watt",
        uitleg="Eén watt is één joule per seconde. Een lamp van 10 watt gebruikt dus 10 joule per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het vermogen van een toestel?",
        opties=[
            "de omgezette energie delen door de tijd",
            "de omgezette energie vermenigvuldigen met de tijd",
            "de tijd delen door de omgezette energie",
            "de kracht vermenigvuldigen met de verplaatsing",
        ],
        antwoord=0,
        uitleg="Vermogen zegt hoe snel de energie omgezet wordt. Twee lampen met hetzelfde vermogen gebruiken in dezelfde tijd evenveel energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een toestel met een groter vermogen zet in dezelfde tijd meer energie om.",
        antwoord=True,
        uitleg="Vermogen is energie per seconde. Een waterkoker van 2000 watt kookt dus sneller dan een van 1000 watt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een motor zet 400 joule om in 5 seconden. Wat is zijn vermogen?",
        opties=["80 watt", "2000 watt", "405 watt", "8 watt"],
        antwoord=0,
        uitleg="Je deelt de energie door de tijd: 400 gedeeld door 5. Dat geeft 80 joule per seconde, dus 80 watt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het rendement van een omzetting zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is de nuttige energie gedeeld door de totale energie",
            "het blijft altijd onder de honderd procent",
            "je drukt het meestal in procent uit",
            "het kan boven de honderd procent uitkomen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Er komt nooit meer energie uit dan er in gaat, dus blijft het rendement onder honderd procent. Dat zou anders de wet van behoud van energie tegenspreken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel procent is het rendement als van 1000 joule 250 joule nuttig is?",
        antwoord="25",
        uitleg="Je deelt 250 door 1000 en dat is een kwart. De overige 750 joule gaat naar een ongewenste vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp krijgt 100 joule en geeft 5 joule licht. Wat gebeurt er met de rest?",
        opties=[
            "die 95 joule wordt warmte, de ongewenste energievorm hier",
            "die 95 joule verdwijnt en is daarna helemaal niet meer terug",
            "die 95 joule blijft als elektrische energie in de lamp zitten",
            "die 95 joule wordt teruggestuurd naar het elektriciteitsnet",
        ],
        antwoord=0,
        uitleg="Energie verdwijnt nooit. Bij een gloeilamp is de warmte veel groter dan het licht, en dat is precies waarom ze verboden werd.",
    ),
    dict(
        type="waarofniet",
        vraag="Het rendement van een gloeilamp is hoger dan dat van een ledlamp.",
        antwoord=False,
        uitleg="Een ledlamp zet veel meer van de elektrische energie om in licht. Een gloeilamp maakt vooral warmte, en daarom werd ze uit de handel gehaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal van 1 kilogram valt van 5 meter hoog. Hoeveel kinetische energie heeft hij net voor de bodem, met 10 newton per kilogram?",
        opties=["50 joule", "5 joule", "10 joule", "500 joule"],
        antwoord=0,
        uitleg="Alle hoogte-energie is dan omgezet: 1 maal 10 maal 5. De luchtweerstand verwaarloos je hier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de energiebalans van een slingerende schommel zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "in het hoogste punt is de hoogte-energie het grootst",
            "in het laagste punt is de kinetische energie het grootst",
            "zonder wrijving blijft de som van de twee gelijk",
            "in het hoogste punt is de kinetische energie het grootst",
        ],
        antwoord=[0, 1, 2],
        uitleg="De schommel wisselt voortdurend tussen die twee vormen. In het hoogste punt staat hij een ogenblik stil, dus is zijn kinetische energie daar juist nul.",
    ),
    dict(
        type="waarofniet",
        vraag="De ongewenste energie bij een omzetting is de totale energie min de nuttige energie.",
        antwoord=True,
        uitleg="Alles wat er in gaat, komt er ook uit, in de ene of de andere vorm. Wat niet nuttig is, is dus ongewenst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de elastische potentiële energie van een uitgerekte veer?",
        opties=[
            "de veerconstante maal het kwadraat van de uitrekking, gedeeld door twee",
            "de veerconstante maal de uitrekking, gedeeld door twee",
            "de veerconstante maal het kwadraat van de kracht, gedeeld door twee",
            "de massa maal het kwadraat van de uitrekking, gedeeld door twee",
        ],
        antwoord=0,
        uitleg="Net als bij de kinetische energie staat de verandering in het kwadraat. Twee keer zo ver uitrekken slaat dus vier keer zo veel energie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toestel van 2000 watt staat een half uur aan. Hoeveel energie gebruikt het?",
        opties=[
            "1 kilowattuur",
            "2 kilowattuur",
            "4 kilowattuur",
            "0,5 kilowattuur",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt het vermogen in kilowatt met de tijd in uur: 2 maal 0,5. Zo rekent ook je elektriciteitsmeter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de energie die bij een omzetting wel gebruikt wordt waarvoor ze bedoeld was?",
        antwoord="nuttige energie",
        uitleg="De rest is ongewenste energie, meestal warmte. Hun verhouding geeft het rendement.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kilowattuur is een eenheid van vermogen.",
        antwoord=False,
        uitleg="Een kilowattuur is vermogen maal tijd, dus een eenheid van energie. De kilowatt zelf is de eenheid van vermogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee waterkokers koken dezelfde liter water, de ene op 2 minuten en de andere op 4. Wat weet je?",
        opties=[
            "de snelste heeft het grootste vermogen, want hij zet sneller energie om",
            "de snelste gebruikt in totaal veel minder energie dan de andere",
            "de snelste heeft een kleiner vermogen maar een beter rendement",
            "ze hebben hetzelfde vermogen, want het water is even warm geworden",
        ],
        antwoord=0,
        uitleg="Voor dezelfde hoeveelheid energie in de helft van de tijd heb je dubbel het vermogen nodig. Het rendement kan daarnaast nog verschillen.",
    ),
]

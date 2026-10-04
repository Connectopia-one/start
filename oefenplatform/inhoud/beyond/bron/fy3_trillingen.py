# -*- coding: utf-8 -*-
"""Harmonische trillingen — 🌍 Beyond, fysica.

Deel 1 gaat over de grootheden van een harmonische trilling: de amplitude, de
evenwichtslijn, de uitwijking, de periode, de frequentie en de pulsatie, en
over de trillingsvergelijking y(t) = A · sin(ω · t + φ) met haar beginfase.
Deel 2 gaat over het faseverschil tussen twee trillingen, over in fase en in
tegenfase, over de terugroepkracht met haar krachtconstante, over de
eigenfrequentie van een massa-veersysteem en van een slinger, over de gedempte
trilling, en over resonantie met haar voorbeelden.

De rode draad is dat één vergelijking de hele beweging beschrijft, en dat je
uit een verloop in de tijd telkens diezelfde vier gegevens terugvindt. Omdat
er hier geen grafiek getekend kan worden, vragen de vragen naar het verloop in
woorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een harmonische trilling?",
        opties=[
            "een beweging waarvan de uitwijking een sinus van de tijd is",
            "een beweging waarvan de snelheid altijd dezelfde blijft",
            "een beweging waarvan de uitwijking steeds groter wordt",
            "een beweging die altijd dezelfde kant op blijft gaan",
        ],
        antwoord=0,
        uitleg="Ze herhaalt zich netjes rond een evenwichtsstand. Een massa aan een veer en "
        "een slinger met een kleine uitslag zijn de twee schoolvoorbeelden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grootste uitwijking van een trilling?",
        antwoord=["de amplitude", "amplitude", "A"],
        uitleg="Ze staat in meter en krijgt het symbool A. In de trillingsvergelijking is ze "
        "de factor voor de sinus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de evenwichtslijn van een trilling?",
        opties=[
            "de stand waar het lichaam zonder trilling zou blijven",
            "de stand waar het lichaam het verst uitgeweken is",
            "de stand waar het lichaam zijn kleinste snelheid heeft",
            "de lijn die de grootste uitwijking aangeeft",
        ],
        antwoord=0,
        uitleg="De uitwijking wordt vanaf die lijn gemeten. Daar is de snelheid net het "
        "grootst en de terugroepkracht nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de periode van een trilling?",
        opties=[
            "de tijd van één volledige heen-en-terugbeweging",
            "het aantal trillingen per seconde",
            "de tijd van de evenwichtsstand tot de uiterste stand",
            "de afstand van de ene uiterste stand tot de andere",
        ],
        antwoord=0,
        uitleg="Ze staat in seconde en krijgt het symbool T. Het aantal per seconde is de "
        "frequentie, haar omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trilling heeft een periode van 0,25 s. Welke frequentie heeft ze?",
        opties=[
            "4 Hz",
            "0,25 Hz",
            "2,5 Hz",
            "40 Hz",
        ],
        antwoord=0,
        uitleg="De frequentie is één gedeeld door de periode, dus één gedeeld door 0,25 is "
        "4 hertz. Er passen dus vier trillingen in een seconde.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de beginfase van een trilling uit?",
        antwoord=["radiaal", "rad", "in radiaal"],
        uitleg="De fase is een hoek in de sinus, dus geen afstand. De amplitude staat wel in "
        "meter en de periode in seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de trillingsvergelijking van een harmonische trilling?",
        opties=[
            "y is A maal de sinus van ω maal t plus φ",
            "y is A maal ω maal t plus φ",
            "y is A gedeeld door de sinus van ω maal t",
            "y is de sinus van A maal ω maal t",
        ],
        antwoord=0,
        uitleg="Hier is A de amplitude, ω de pulsatie en φ de beginfase. Met die drie ligt "
        "de hele beweging vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de pulsatie van een trilling?",
        opties=[
            "twee pi gedeeld door de periode",
            "de periode gedeeld door twee pi",
            "twee pi maal de periode",
            "de amplitude gedeeld door de periode",
        ],
        antwoord=0,
        uitleg="Ze staat in radiaal per seconde en heet ook de hoeksnelheid. Je kan ze ook "
        "schrijven als twee pi maal de frequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens lees je rechtstreeks uit de trillingsvergelijking? Kruis alles aan wat juist is.",
        opties=[
            "de amplitude van de trilling",
            "de pulsatie van de trilling",
            "de beginfase van de trilling",
            "de massa van het trillende lichaam",
        ],
        antwoord=[0, 1, 2],
        uitleg="De massa staat er niet in, al bepaalt ze bij een veer wel de pulsatie. Uit "
        "de pulsatie volgen de periode en de frequentie.",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een trilling staat in meter.",
        antwoord=True,
        uitleg="Ze is een uitwijking, dus een afstand. De beginfase staat wel in radiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trilling heeft een amplitude van 5 cm en een pulsatie van 4 rad/s, met beginfase nul. Welke uitwijking heeft ze na een halve periode?",
        opties=[
            "nul, want de sinus is dan weer nul",
            "5 cm, want de uitwijking is dan maximaal",
            "2,5 cm, want dat is de helft van de amplitude",
            "min 5 cm, want ze staat dan aan de andere kant",
        ],
        antwoord=0,
        uitleg="Na een halve periode is de fase pi, en de sinus van pi is nul. Het lichaam "
        "gaat daar door de evenwichtsstand, met zijn grootste snelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een harmonische trilling is de snelheid het grootst in de uiterste stand.",
        antwoord=False,
        uitleg="Daar staat het lichaam juist even stil voor het terugkeert. De snelheid is "
        "het grootst in de evenwichtsstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar is de versnelling van een harmonisch trillend lichaam het grootst?",
        opties=[
            "in de uiterste standen, waar de uitwijking maximaal is",
            "in de evenwichtsstand, waar de snelheid maximaal is",
            "halverwege tussen het evenwicht en de uiterste stand",
            "ze is tijdens de hele trilling even groot",
        ],
        antwoord=0,
        uitleg="De terugroepkracht is daar het grootst, en kracht en versnelling gaan samen. "
        "In de evenwichtsstand is de versnelling nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een beginfase van nul?",
        opties=[
            "de trilling vertrekt op t is nul uit de evenwichtsstand",
            "de trilling vertrekt op t is nul uit de uiterste stand",
            "de trilling heeft geen amplitude op t is nul",
            "de trilling staat op t is nul volledig stil",
        ],
        antwoord=0,
        uitleg="De sinus van nul is nul, dus is de uitwijking dan nul. Vertrekt ze uit de "
        "uiterste stand, dan is de beginfase een halve pi.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een harmonische trilling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de uitwijking is nul in de evenwichtsstand",
            "de snelheid is nul in de uiterste stand",
            "de versnelling is nul in de uiterste stand",
            "de periode hangt af van de amplitude",
        ],
        antwoord=[0, 1],
        uitleg="De versnelling is net maximaal in de uiterste stand. En bij een harmonische "
        "trilling hangt de periode niet af van de amplitude.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt de amplitude van een slinger met een kleine uitslag. Wat gebeurt er met de periode?",
        opties=[
            "ze blijft ongeveer gelijk",
            "ze wordt ongeveer twee keer zo groot",
            "ze wordt ongeveer twee keer zo klein",
            "ze wordt ongeveer vier keer zo groot",
        ],
        antwoord=0,
        uitleg="Bij kleine uitslagen hangt de periode alleen van de lengte en van g af. Net "
        "daarom was een slingeruurwerk zo nauwkeurig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden heb je samen nodig om een trillingsvergelijking op te stellen? Kruis alles aan wat juist is.",
        opties=[
            "de amplitude",
            "de periode of de frequentie",
            "de beginfase",
            "de massa van het lichaam",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uit de periode volgt de pulsatie, dus volstaat een van die twee. De massa "
        "hoeft niet in de vergelijking te staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een trilling met een hogere frequentie heeft een kleinere periode.",
        antwoord=True,
        uitleg="De twee zijn omgekeerd evenredig. Tien trillingen per seconde betekent een "
        "tiende van een seconde per trilling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de pulsatie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is twee pi maal de frequentie",
            "ze staat in radiaal per seconde",
            "ze is gelijk aan de periode",
            "ze wordt groter als de periode groter wordt",
        ],
        antwoord=[0, 1],
        uitleg="Ze wordt net kleiner als de periode groter wordt, want de periode staat in "
        "de noemer. En ze is iets heel anders dan de periode zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een trilling kan ook een negatieve waarde hebben.",
        antwoord=False,
        uitleg="De amplitude is de grootste uitwijking en blijft dus positief. De uitwijking "
        "zelf krijgt aan de ene kant van de evenwichtslijn wel een minteken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het faseverschil tussen twee harmonische trillingen?",
        opties=[
            "het verschil tussen hun fasen op hetzelfde tijdstip",
            "het verschil tussen hun amplitudes op hetzelfde tijdstip",
            "het verschil tussen hun periodes",
            "het verschil tussen hun uiterste standen",
        ],
        antwoord=0,
        uitleg="Het staat in radiaal, net als de fase zelf. Bij gelijke frequentie blijft "
        "dat verschil de hele tijd hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer trillen twee trillingen in fase?",
        opties=[
            "als hun faseverschil nul of een veelvoud van twee pi is",
            "als hun faseverschil pi is",
            "als hun amplitudes precies gelijk zijn",
            "als hun beginfase allebei nul is",
        ],
        antwoord=0,
        uitleg="Ze bereiken dan samen hun uiterste stand, aan dezelfde kant. Bij een "
        "faseverschil van pi zijn ze net in tegenfase.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je twee trillingen met een faseverschil van pi radiaal?",
        antwoord=["in tegenfase", "tegenfase", "tegengesteld in fase"],
        uitleg="De ene staat dan boven terwijl de andere onder staat. Bij een faseverschil "
        "van nul zijn ze in fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de terugroepkracht bij een massa-veersysteem?",
        opties=[
            "de kracht van de veer, naar de evenwichtsstand gericht",
            "de kracht van de veer, van de evenwichtsstand weg gericht",
            "het gewicht van de massa, naar beneden gericht",
            "de wrijving van de lucht, tegen de beweging in",
        ],
        antwoord=0,
        uitleg="Ze is recht evenredig met de uitwijking en altijd tegengesteld eraan. Net "
        "daardoor is de beweging harmonisch.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de constante k van een veer?",
        antwoord=["de krachtconstante", "krachtconstante", "elasticiteitsconstante"],
        uitleg="Ze staat in newton per meter en zegt hoe stijf de veer is. In de formule van "
        "de eigenfrequentie staat ze onder de wortel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de eigenfrequentie van een massa-veersysteem?",
        opties=[
            "één gedeeld door twee pi, maal de wortel van k gedeeld door m",
            "één gedeeld door twee pi, maal de wortel van m gedeeld door k",
            "twee pi maal de wortel van k gedeeld door m",
            "de wortel van k maal m, gedeeld door twee pi",
        ],
        antwoord=0,
        uitleg="Een stijvere veer trilt dus sneller en een grotere massa langzamer. Die "
        "formule staat op het examen in de bijlage.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de eigenfrequentie van een slinger af?",
        opties=[
            "van zijn lengte en van de valversnelling",
            "van zijn lengte en van de massa van de bol",
            "van de massa van de bol en van de valversnelling",
            "van de amplitude en van de massa van de bol",
        ],
        antwoord=0,
        uitleg="De massa van de bol doet er niet toe. In de formule staat de wortel van g "
        "gedeeld door de lengte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een langere slinger trilt langzamer dan een korte.",
        antwoord=True,
        uitleg="De lengte staat in de noemer onder de wortel, dus geeft een grotere lengte "
        "een kleinere frequentie. Daarom hangt een slingeruurwerk zo laag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hangt een dubbel zo zware massa aan dezelfde veer. Wat gebeurt er met de eigenfrequentie?",
        opties=[
            "ze wordt kleiner, met een factor wortel twee",
            "ze wordt groter, met een factor wortel twee",
            "ze wordt twee keer zo klein",
            "ze blijft precies dezelfde",
        ],
        antwoord=0,
        uitleg="De massa staat in de noemer onder de wortel. Een vier keer zo zware massa "
        "zou de frequentie halveren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een massa-veersysteem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een stijvere veer geeft een hogere eigenfrequentie",
            "een grotere massa geeft een lagere eigenfrequentie",
            "een grotere amplitude geeft een hogere eigenfrequentie",
            "de eigenfrequentie hangt af van de valversnelling",
        ],
        antwoord=[0, 1],
        uitleg="De amplitude doet er bij een harmonische trilling niet toe. En g staat wel "
        "in de formule van een slinger, niet in die van een veer.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gedempte harmonische trilling neemt vooral de frequentie af.",
        antwoord=False,
        uitleg="Het is de amplitude die afneemt, want wrijving haalt er bij elke beweging "
        "energie uit. De frequentie blijft daarbij bijna dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de uitwijking van een gedempte trilling in de tijd?",
        opties=[
            "als een sinus die tussen twee krimpende grenzen past",
            "als een sinus die tussen twee groeiende grenzen past",
            "als een rechte die naar de evenwichtslijn zakt",
            "als een sinus met een steeds grotere periode",
        ],
        antwoord=0,
        uitleg="Het trilt nog netjes heen en weer, maar elke slag is kleiner dan de vorige. "
        "Zo komt een schommel zonder duw tot stilstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gedempte trilling verdwijnt de energie van de trilling naar de omgeving.",
        antwoord=True,
        uitleg="Wrijving en luchtweerstand maken er warmte van. Het behoud van energie "
        "blijft dus gelden, ze zit alleen niet meer in de trilling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gedwongen trilling?",
        opties=[
            "een trilling die een uitwendige kracht blijft aandrijven",
            "een trilling die enkel op zijn eigen frequentie gebeurt",
            "een trilling die na één duw vrij blijft doorgaan",
            "een trilling die door wrijving wordt tegengehouden",
        ],
        antwoord=0,
        uitleg="Het lichaam neemt dan de frequentie van die kracht over. Laat je het vrij, "
        "dan trilt het op zijn eigen frequentie verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer treedt resonantie op?",
        opties=[
            "als de frequentie van de kracht de eigenfrequentie benadert",
            "als de frequentie van de kracht veel hoger is dan de eigenfrequentie",
            "als de kracht groter is dan de terugroepkracht van de veer",
            "als de demping van de trilling volledig is weggevallen",
        ],
        antwoord=0,
        uitleg="De amplitude kan dan heel groot worden met een kleine kracht. Elke duw komt "
        "precies op het juiste moment.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de frequentie waarmee een lichaam vrij trilt?",
        antwoord=["de eigenfrequentie", "eigenfrequentie", "eigen frequentie"],
        uitleg="Bij resonantie komt de aandrijvende frequentie daar dicht bij. Ze volgt uit "
        "de bouw van het lichaam zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden zijn resonantie? Kruis alles aan wat juist is.",
        opties=[
            "een schommel die je op het juiste ritme steeds hoger duwt",
            "een glas dat breekt bij een zuivere toon van de juiste hoogte",
            "een brug die door marcherende stappen hevig begint te trillen",
            "een slinger die na een tijd van zelf tot stilstand komt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste is demping, het omgekeerde verhaal. Soldaten mogen daarom op een "
        "brug niet in de maat stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet men dempers in een gebouw dat tegen aardbevingen moet kunnen?",
        opties=[
            "om de amplitude bij resonantie klein te houden",
            "om de eigenfrequentie van het gebouw hoger te maken",
            "om de trilling van de bodem helemaal tegen te houden",
            "om het gebouw zwaarder en dus stabieler te maken",
        ],
        antwoord=0,
        uitleg="Demping haalt energie uit de trilling, net zoals wrijving. De bodem zelf kan "
        "je niet stil krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij resonantie is de amplitude van de trilling net kleiner dan normaal.",
        antwoord=False,
        uitleg="Ze wordt juist veel groter, en daar zit het gevaar. Een kleine kracht kan op "
        "de juiste frequentie grote schade doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee trillingen hebben dezelfde frequentie en een faseverschil van een halve pi. Wat betekent dat?",
        opties=[
            "de ene is een kwart periode voor op de andere",
            "de ene is een halve periode voor op de andere",
            "de ene heeft een dubbel zo grote amplitude",
            "de ene heeft een dubbel zo grote periode",
        ],
        antwoord=0,
        uitleg="Een hele periode is twee pi, dus een halve pi is een kwart ervan. Staat de "
        "ene in de evenwichtsstand, dan staat de andere uiterst.",
    ),
]

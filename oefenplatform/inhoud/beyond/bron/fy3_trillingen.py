# -*- coding: utf-8 -*-
"""Harmonische trillingen — 🌍 Beyond, fysica.

Deel 1 gaat over de grootheden van een harmonische trilling: de amplitude, de
evenwichtslijn, de uitwijking, de periode, de frequentie en de pulsatie, en
over de trillingsvergelijking \(y(t) = A\sin(\omega t + \varphi)\) met haar
beginfase.
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
        uitleg=r"Ze staat in meter en krijgt het symbool \(A\). In de "
        r"trillingsvergelijking is ze de factor voor de sinus.",
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
        uitleg=r"Ze staat in seconde en krijgt het symbool \(T\). Het aantal per seconde "
        r"is de frequentie: \(f = \dfrac{1}{T}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trilling heeft een periode van \(0{,}25\) s. Welke frequentie heeft ze?",
        opties=[
            r"\(4{,}0\) Hz",
            r"\(0{,}25\) Hz",
            r"\(2{,}5\) Hz",
            r"\(40\) Hz",
        ],
        antwoord=0,
        uitleg=r"\(f = \dfrac{1}{T} = \dfrac{1}{0{,}25} = 4{,}0\) Hz. Er passen dus vier "
        r"trillingen in een seconde.",
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
            r"\(y = A\sin(\omega t + \varphi)\)",
            r"\(y = A\,\omega\,t + \varphi\)",
            r"\(y = \dfrac{A}{\sin(\omega t)}\)",
            r"\(y = \sin(A\,\omega\,t)\)",
        ],
        antwoord=0,
        uitleg=r"\(A\) is de amplitude, \(\omega\) de pulsatie en \(\varphi\) de "
        r"beginfase. Met die drie ligt de hele beweging vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de pulsatie van een trilling?",
        opties=[
            r"\(\omega = \dfrac{2\pi}{T}\)",
            r"\(\omega = \dfrac{T}{2\pi}\)",
            r"\(\omega = 2\pi T\)",
            r"\(\omega = \dfrac{A}{T}\)",
        ],
        antwoord=0,
        uitleg=r"Ze staat in rad/s en heet ook de hoeksnelheid. Je kan ze ook schrijven als "
        r"\(\omega = 2\pi f\).",
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
        uitleg=r"De massa staat er niet in, al bepaalt ze bij een veer wel \(\omega\). "
        r"Uit \(\omega\) volgen \(T\) en \(f\).",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een trilling staat in meter.",
        antwoord=True,
        uitleg=r"Ze is een uitwijking, dus een afstand. De beginfase \(\varphi\) staat "
        r"wel in radiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trilling heeft \(A = 5\) cm en \(\omega = 4\) rad/s, met \(\varphi = 0\). Welke uitwijking heeft ze na een halve periode?",
        opties=[
            r"nul, want \(\sin \pi = 0\)",
            r"\(5\) cm, de uitwijking is dan maximaal",
            r"\(2{,}5\) cm, de helft van de amplitude",
            r"\(-5\) cm, ze staat aan de andere kant",
        ],
        antwoord=0,
        uitleg=r"Na een halve periode is de fase \(\pi\), en \(\sin \pi = 0\). Het "
        r"lichaam gaat daar door de evenwichtsstand, met zijn grootste snelheid.",
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
        uitleg=r"\(\sin 0 = 0\), dus is de uitwijking dan nul. Vertrekt ze uit de "
        r"uiterste stand, dan is \(\varphi = \tfrac{\pi}{2}\).",
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
            r"ze is \(2\pi f\)",
            r"ze staat in rad/s",
            r"ze is gelijk aan \(T\)",
            r"ze wordt groter als \(T\) groter wordt",
        ],
        antwoord=[0, 1],
        uitleg=r"Ze wordt net kleiner als \(T\) groter wordt, want \(T\) staat in de "
        r"noemer van \(\omega = \dfrac{2\pi}{T}\).",
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
            r"als \(\Delta\varphi = 0\) of een veelvoud van \(2\pi\) is",
            r"als \(\Delta\varphi = \pi\) is",
            "als hun amplitudes precies gelijk zijn",
            "als hun beginfase allebei nul is",
        ],
        antwoord=0,
        uitleg=r"Ze bereiken dan samen hun uiterste stand, aan dezelfde kant. Bij "
        r"\(\Delta\varphi = \pi\) zijn ze net in tegenfase.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noem je twee trillingen met een faseverschil van \(\pi\) rad?",
        antwoord=["in tegenfase", "tegenfase", "tegengesteld in fase"],
        uitleg=r"De ene staat dan boven terwijl de andere onder staat. Bij "
        r"\(\Delta\varphi = 0\) zijn ze in fase.",
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
        uitleg=r"\[F = -k\,y\] Ze is recht evenredig met de uitwijking en altijd "
        r"tegengesteld eraan. Net daardoor is de beweging harmonisch.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noem je de constante \(k\) van een veer?",
        antwoord=["de krachtconstante", "krachtconstante", "elasticiteitsconstante"],
        uitleg=r"Ze staat in \(\text{N/m}\) en zegt hoe stijf de veer is. In de formule "
        r"van de eigenfrequentie staat ze onder de wortel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de eigenfrequentie van een massa-veersysteem?",
        opties=[
            r"\(f_{0} = \dfrac{1}{2\pi}\sqrt{\dfrac{k}{m}}\)",
            r"\(f_{0} = \dfrac{1}{2\pi}\sqrt{\dfrac{m}{k}}\)",
            r"\(f_{0} = 2\pi\sqrt{\dfrac{k}{m}}\)",
            r"\(f_{0} = \dfrac{\sqrt{k\,m}}{2\pi}\)",
        ],
        antwoord=0,
        uitleg=r"Een stijvere veer trilt dus sneller en een grotere massa langzamer. Die "
        r"formule staat op het examen in de bijlage.",
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
        uitleg=r"\[f_{0} = \dfrac{1}{2\pi}\sqrt{\dfrac{g}{\ell}}\] De massa van de bol "
        r"doet er niet toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Een langere slinger trilt langzamer dan een korte.",
        antwoord=True,
        uitleg=r"\(\ell\) staat in de noemer onder de wortel, dus geeft een grotere "
        r"lengte een kleinere frequentie. Daarom hangt een slingeruurwerk zo laag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hangt een dubbel zo zware massa aan dezelfde veer. Wat gebeurt er met de eigenfrequentie?",
        opties=[
            r"ze wordt kleiner, met een factor \(\sqrt{2}\)",
            r"ze wordt groter, met een factor \(\sqrt{2}\)",
            r"ze wordt twee keer zo klein",
            r"ze blijft precies dezelfde",
        ],
        antwoord=0,
        uitleg=r"\(m\) staat in de noemer onder de wortel. Een vier keer zo zware massa "
        r"zou \(f_{0}\) halveren.",
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
        uitleg=r"De amplitude doet er bij een harmonische trilling niet toe. En \(g\) "
        r"staat wel in de formule van een slinger, niet in die van een veer.",
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
        vraag=r"Twee trillingen hebben dezelfde frequentie en een faseverschil van \(\tfrac{\pi}{2}\). Wat betekent dat?",
        opties=[
            "de ene is een kwart periode voor op de andere",
            "de ene is een halve periode voor op de andere",
            "de ene heeft een dubbel zo grote amplitude",
            "de ene heeft een dubbel zo grote periode",
        ],
        antwoord=0,
        uitleg=r"Een hele periode is \(2\pi\), dus \(\tfrac{\pi}{2}\) is een kwart ervan. Staat de "
        "ene in de evenwichtsstand, dan staat de andere uiterst.",
    ),
]

# -*- coding: utf-8 -*-
"""Arbeid, energie en vermogen — 🌍 Beyond, fysica.

Deel 1 gaat over arbeid: wanneer een kracht arbeid verricht en wanneer niet,
het verschil tussen een constante en een niet-constante kracht, de arbeid als
oppervlakte onder een F(x)-grafiek, en het onderscheid tussen conservatieve en
niet-conservatieve krachten. Deel 2 gaat over energie: kinetische energie,
gravitationele en elastische potentiële energie, het arbeid-energietheorema,
het behoud van energie met en zonder wrijving, en het vermogen.

Het onderscheid conservatief of niet is het scharnier van dit thema. Bij een
conservatieve kracht kan je met potentiële energie werken en telt alleen begin
en einde; bij wrijving moet je de hele weg kennen, want de energie gaat als
warmte verloren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een kracht arbeid?",
        opties=[
            "als het aangrijpingspunt verplaatst wordt in de zin van de kracht",
            "als de kracht groot genoeg is, ook zonder verplaatsing",
            "als de kracht lang genoeg blijft duwen tegen het lichaam",
            "als de kracht loodrecht op de verplaatsing staat",
        ],
        antwoord=0,
        uitleg=r"\[W = F\,s\cos\alpha\] Duw je tegen een muur die niet wijkt, dan is "
        r"\(s = 0\) en dus \(W = 0\), hoe moe je ook wordt. Fysische arbeid is iets anders "
        r"dan inspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kracht van \(45\) N verplaatst een kist \(3{,}2\) m in dezelfde zin. Hoeveel arbeid is er verricht?",
        opties=[
            r"\(144\) J",
            r"\(14\) J",
            r"\(48\) J",
            r"\(1{,}4 \times 10^{3}\) J",
        ],
        antwoord=0,
        uitleg=r"\(W = F\,s\cos 0^\circ = 45 \times 3{,}2 = 144\) J.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je arbeid uit?",
        antwoord=["joule", "J", "de joule"],
        uitleg=r"\(1\ \text{J} = 1\ \text{N}\,\text{m}\). Het is ook de eenheid van energie, "
        r"want arbeid is een omzetting van energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kelner die een blad met glazen horizontaal draagt, verricht arbeid op dat blad.",
        antwoord=False,
        uitleg=r"Hij duwt het blad omhoog en beweegt het vooruit, dus \(\alpha = 90^\circ\) en "
        r"\(\cos 90^\circ = 0\). De arbeid van die kracht is dus nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een kracht geen arbeid? Kruis alles aan wat juist is.",
        opties=[
            "als er geen verplaatsing is",
            "als de kracht loodrecht op de verplaatsing staat",
            "als de kracht zelf nul is",
            "als de verplaatsing tegen de kracht in gaat",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"Gaat de verplaatsing tegen de kracht in, dan is \(\cos 180^\circ = -1\) en is "
        r"\(W\) negatief, dus niet nul. De zwaartekracht verricht geen arbeid als je "
        r"horizontaal schuift, want dan is \(\alpha = 90^\circ\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat lees je af uit de oppervlakte onder een \(F(x)\)-grafiek?",
        opties=[
            "de verrichte arbeid",
            "de snelheid van het lichaam",
            "het vermogen van de kracht",
            "de massa van het lichaam",
        ],
        antwoord=0,
        uitleg=r"Kracht maal afstand is arbeid, en dat is precies een oppervlakte: "
        r"\(W = \int F\,\mathrm{d}x\). Zo reken je ook met een kracht die onderweg "
        r"verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten zijn niet constant? Kruis alles aan wat juist is.",
        opties=[
            "de veerkracht",
            "de gravitatiekracht op grote afstandsverschillen",
            "de zwaartekracht vlak bij het aardoppervlak",
            "een duwkracht die je constant houdt",
        ],
        antwoord=[0, 1],
        uitleg=r"De veerkracht groeit met \(F = k\,x\) en de gravitatiekracht daalt met "
        r"\(\dfrac{1}{r^{2}}\). Voor hun arbeid neem je de oppervlakte onder de grafiek, "
        r"dus \(\int F\,\mathrm{d}x\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een conservatieve kracht?",
        opties=[
            "een kracht waarvan de arbeid niet van de gevolgde weg afhangt",
            "een kracht die altijd dezelfde grootte houdt",
            "een kracht die altijd arbeid aan een lichaam onttrekt",
            "een kracht die enkel bij hoge snelheid werkt",
        ],
        antwoord=0,
        uitleg="Alleen begin- en eindpunt tellen. Daarom kan je er een potentiële energie "
        "bij definiëren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten zijn conservatief? Kruis alles aan wat juist is.",
        opties=[
            "de zwaartekracht",
            "de veerkracht",
            "de wrijvingskracht",
            "de remkracht van een rem",
        ],
        antwoord=[0, 1],
        uitleg="Ook de gravitatiekracht en de coulombkracht zijn conservatief. Wrijving, "
        "spierkracht en motorkracht zijn dat niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een kracht waarvan de arbeid wél van de gevolgde weg afhangt?",
        antwoord=["niet-conservatief", "niet conservatief", "dissipatief"],
        uitleg="Wrijving is het schoolvoorbeeld: hoe langer de weg, hoe meer energie er als "
        "warmte verdwijnt. Daarom kan je er geen potentiële energie bij definiëren.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeid van de wrijvingskracht is altijd negatief.",
        antwoord=True,
        uitleg=r"Ze wijst tegen de beweging in, dus \(\cos 180^\circ = -1\) en onttrekt ze "
        r"energie aan het lichaam. Die energie komt als warmte terecht in het oppervlak en "
        r"het lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je tilt een doos van \(10\) kg \(1{,}5\) m hoog. Hoeveel arbeid lever je? Neem \(g = 9{,}81\ \text{N/kg}\).",
        opties=[
            r"\(147\) J",
            r"\(15\) J",
            r"\(98\) J",
            r"\(1{,}5 \times 10^{3}\) J",
        ],
        antwoord=0,
        uitleg=r"\(W = m\,g\,h = 10 \times 9{,}81 \times 1{,}5 = 147\) J. Die energie zit "
        r"daarna als potentiële energie in de doos.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kist schuift \(4{,}0\) m over een vloer met een wrijvingskracht van \(25\) N. Hoeveel arbeid verricht de wrijving?",
        opties=[
            r"\(-100\) J",
            r"\(+100\) J",
            r"\(-6{,}3\) J",
            r"\(-29\) J",
        ],
        antwoord=0,
        uitleg=r"\(W = F\,s\cos 180^\circ = -25 \times 4{,}0 = -100\) J. Die \(100\) J "
        r"verdwijnt als warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Arbeid kan negatief zijn.",
        antwoord=True,
        uitleg="Dat gebeurt als de kracht tegen de verplaatsing in wijst, zoals bij "
        "wrijving of bij remmen. De energie van het lichaam neemt dan af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel arbeid verricht de middelpuntzoekende kracht op een satelliet in een cirkelbaan?",
        opties=[
            "nul, want ze staat loodrecht op de beweging",
            "evenveel als de kinetische energie van de satelliet",
            "een negatieve arbeid, want ze trekt naar binnen",
            "dat hangt af van de massa van de satelliet",
        ],
        antwoord=0,
        uitleg=r"Met \(\alpha = 90^\circ\) is \(W = 0\). Daarom blijft \(\lvert v \rvert\) van "
        r"zo'n satelliet constant: een kracht loodrecht op de beweging verandert enkel de "
        r"richting.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kracht van \(20\) N duwt onder \(\alpha = 60^\circ\) met de verplaatsing. Hoeveel arbeid levert ze over \(5{,}0\) m?",
        opties=[
            r"\(50\) J",
            r"\(100\) J",
            r"\(87\) J",
            r"\(25\) J",
        ],
        antwoord=0,
        uitleg=r"Enkel de component langs de verplaatsing telt: "
        r"\(W = 20 \times 5{,}0 \times \cos 60^\circ = 20 \times 5{,}0 \times 0{,}5 = 50\) J.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over arbeid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "arbeid wordt uitgedrukt in joule",
            "arbeid is negatief als de kracht tegen de verplaatsing in werkt",
            r"bij een veranderlijke \(F\) reken je \(\int F\,\mathrm{d}x\)",
            "arbeid is een vector en heeft dus een richting",
        ],
        antwoord=[0, 1, 2],
        uitleg="Arbeid is een getal met een teken en geen vector. Dat teken zegt of de "
        "kracht energie toevoegt of wegneemt.",
    ),
    dict(
        type="waarofniet",
        vraag="De normaalkracht op een lichaam dat over een vlakke vloer schuift, verricht arbeid.",
        antwoord=False,
        uitleg="Ze staat loodrecht op de verplaatsing, dus is haar arbeid nul. Toch is ze "
        "een niet-conservatieve kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke arbeid verricht je als je met een boodschappentas een trap van 3 m oploopt, met een tas van 5 kg? Neem g gelijk aan 10 N/kg.",
        opties=[
            "150 J",
            "15 J",
            "50 J",
            "1,5 J",
        ],
        antwoord=0,
        uitleg="Enkel het hoogteverschil telt: 5 maal 10 maal 3 is 150 joule. Hoe lang de "
        "trap of hoe traag je gaat, verandert daar niets aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de oppervlakte onder een F(x)-grafiek?",
        antwoord=["arbeid", "de arbeid", "verrichte arbeid"],
        uitleg="Kracht maal afstand is arbeid, en dat is wat die oppervlakte voorstelt. Zo "
        "reken je ook met een kracht die onderweg verandert.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de kinetische energie \(E_{k}\) van een lichaam?",
        opties=[
            r"\(E_{k} = \tfrac{1}{2}m\,v^{2}\)",
            r"\(E_{k} = m\,v\)",
            r"\(E_{k} = m\,v^{2}\)",
            r"\(E_{k} = \tfrac{1}{2}m\,v\)",
        ],
        antwoord=0,
        uitleg=r"Door dat kwadraat heeft twee keer zo snel rijden vier keer zo veel energie. "
        r"Dat is waarom een botsing bij hoge snelheid zo veel zwaarder is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel kinetische energie heeft een auto van \(1{,}0 \times 10^{3}\) kg die \(20\) m/s rijdt?",
        opties=[
            r"\(2{,}0 \times 10^{5}\) J",
            r"\(2{,}0 \times 10^{4}\) J",
            r"\(4{,}0 \times 10^{5}\) J",
            r"\(1{,}0 \times 10^{4}\) J",
        ],
        antwoord=0,
        uitleg=r"\(E_{k} = \tfrac{1}{2} \times 1000 \times 400 = 2{,}0 \times 10^{5}\) J, "
        r"dus \(200\) kJ.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over kinetische en potentiële energie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(E_{k} = \tfrac{1}{2}m\,v^{2}\)",
            r"\(E_{p} = m\,g\,h\)",
            r"dubbele \(v\) geeft vier keer zoveel \(E_{k}\)",
            r"\(E_{p}\) hangt ook van \(v\) af",
        ],
        antwoord=[0, 1, 2],
        uitleg="Potentiële energie hangt alleen van de hoogte en de massa af. De snelheid "
        "zit volledig in de kinetische energie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe bereken je de gravitationele potentiële energie vlak bij het aardoppervlak?",
        antwoord=["m·g·h", "mgh", "m g h"],
        uitleg=r"\(E_{p} = m\,g\,h\). Welke hoogte je als nulpunt kiest, mag je zelf bepalen, "
        r"want alleen het verschil \(\Delta E_{p}\) telt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel potentiële energie heeft een steen van 2 kg op 15 m hoogte? Neem g gelijk aan 10 N/kg.",
        opties=[
            "300 J",
            "30 J",
            "150 J",
            "3000 J",
        ],
        antwoord=0,
        uitleg=r"\(E_{p} = m\,g\,h = 2 \times 10 \times 15 = 300\) J.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe snel raakt die steen de grond, als je de luchtweerstand verwaarloost?",
        opties=[
            "ongeveer 17 m/s",
            "ongeveer 30 m/s",
            "ongeveer 15 m/s",
            "ongeveer 300 m/s",
        ],
        antwoord=0,
        uitleg=r"Alle \(300\) J wordt kinetische energie: \(m\,g\,h = \tfrac{1}{2}m\,v^{2}\), "
        r"dus \(v = \sqrt{2gh} = \sqrt{300} \approx 17\) m/s. De massa valt weg.",
    ),
    dict(
        type="waarofniet",
        vraag="De potentiële energie van een veer is recht evenredig met haar uitrekking zelf.",
        antwoord=False,
        uitleg=r"Ze gaat met het kwádraat van de uitrekking: "
        r"\(E_{\text{veer}} = \tfrac{1}{2}k\,x^{2}\). Twee keer zo ver uitrekken slaat dus "
        r"vier keer zo veel energie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het arbeid-energietheorema?",
        opties=[
            r"\(W_{\text{tot}} = \Delta E_{k}\)",
            r"\(W_{\text{tot}} = E_{p}\)",
            r"\(W = 0\) voor elke kracht",
            r"\(W = \dfrac{E_{k}}{t}\)",
        ],
        antwoord=0,
        uitleg="Remt een lichaam af, dan is de totale arbeid negatief. Daarom kan je er de "
        "eindsnelheid mee berekenen zonder de tijd te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een slee van 20 kg glijdt zonder wrijving van een heuvel van 5 m hoog. Hoe snel is hij beneden? Neem g gelijk aan 10 N/kg.",
        opties=[
            "10 m/s",
            "5 m/s",
            "20 m/s",
            "50 m/s",
        ],
        antwoord=0,
        uitleg=r"Stel \(m\,g\,h = \tfrac{1}{2}m\,v^{2}\); de massa valt weg en er blijft "
        r"\(v = \sqrt{2gh} = \sqrt{2 \times 10 \times 5} = 10\) m/s over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij die berekening speelt de massa van de slee geen rol.",
        antwoord=True,
        uitleg="Ze staat links en rechts in de vergelijking en valt dus weg. Een zware en "
        "een lichte slee komen zonder wrijving even snel beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over vermogen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(P = \dfrac{W}{t}\)",
            r"het staat in watt",
            r"\(1\ \text{W} = 1\ \text{J/s}\)",
            r"het staat in joule",
        ],
        antwoord=[0, 1, 2],
        uitleg="Joule is de eenheid van arbeid en energie, niet van vermogen. Twee motoren "
        "kunnen dezelfde arbeid leveren en toch een ander vermogen hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievormen wisselen elkaar af bij een slingerende schommel? Kruis alles aan wat juist is.",
        opties=[
            "kinetische energie",
            "gravitationele potentiële energie",
            "elastische potentiële energie",
            "kernenergie",
        ],
        antwoord=[0, 1],
        uitleg="Op het hoogste punt is alles potentieel, op het laagste punt alles "
        "kinetisch. Door wrijving gaat er elke slinger een beetje als warmte weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is vermogen?",
        opties=[
            "de arbeid die per seconde verricht wordt",
            "de arbeid maal de verlopen tijd",
            "de kracht maal de massa van het lichaam",
            "de energie die een lichaam in totaal bevat",
        ],
        antwoord=0,
        uitleg=r"\(P = \dfrac{W}{t}\), in watt, en \(1\ \text{W} = 1\ \text{J/s}\). Twee "
        r"motoren kunnen dezelfde arbeid leveren en toch een ander vermogen hebben.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je vermogen uit?",
        antwoord=["watt", "W", "de watt"],
        uitleg="Eén watt is één joule per seconde. Een kilowattuur is dus geen vermogen maar "
        "een hoeveelheid energie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een lift levert \(6{,}0 \times 10^{4}\) J arbeid in \(20\) s. Hoe groot is zijn vermogen?",
        opties=[
            r"\(3{,}0 \times 10^{3}\) W",
            r"\(1{,}2 \times 10^{6}\) W",
            r"\(3{,}0 \times 10^{2}\) W",
            r"\(3{,}3 \times 10^{-4}\) W",
        ],
        antwoord=0,
        uitleg=r"\(P = \dfrac{W}{t} = \dfrac{6{,}0 \times 10^{4}}{20} = 3{,}0 \times "
        r"10^{3}\) W, dus \(3\) kW.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een doos sneller even hoog tilt, levert daardoor meer arbeid.",
        antwoord=False,
        uitleg="De arbeid hangt enkel af van de kracht en de hoogte, niet van de tijd. Wie "
        "het sneller doet, heeft wel een groter vermogen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel joule is één kilowattuur?",
        opties=[
            r"\(3{,}6 \times 10^{6}\) J",
            r"\(1{,}0 \times 10^{3}\) J",
            r"\(3{,}6 \times 10^{3}\) J",
            r"\(6{,}0 \times 10^{4}\) J",
        ],
        antwoord=0,
        uitleg=r"\(E = P\,t = 1000 \times 3600 = 3{,}6 \times 10^{6}\) J. Zo rekent de "
        r"elektriciteitsmeter thuis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal valt van 2 m hoog en stuitert tot 1,4 m. Wat is er met de rest van de energie gebeurd?",
        opties=[
            "ze is bij de botsing als warmte en geluid vrijgekomen",
            "ze is in de lucht boven de bal blijven hangen",
            "ze is in potentiële energie van de grond omgezet",
            "ze is gewoon verdwenen, want energie gaat verloren",
        ],
        antwoord=0,
        uitleg="De bal en de vloer vervormen even en worden daarbij warm. Energie gaat nooit "
        "verloren, ze verandert van vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesloten systeem zonder wrijving blijft de som van de kinetische en de potentiële energie gelijk.",
        antwoord=True,
        uitleg=r"Dat is het behoud van mechanische energie: \(E_{k} + E_{p}\) blijft "
        r"constant. Met wrijving klopt die som niet meer, want er verdwijnt energie als "
        r"warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist glijdt met wrijving een helling af. Hoe pas je het behoud van energie toe?",
        opties=[
            "de potentiële energie wordt kinetische energie plus warmte",
            "de potentiële energie wordt volledig kinetische energie",
            "de kinetische energie wordt potentiële energie plus warmte",
            "de energie blijft gelijk, want wrijving telt niet mee",
        ],
        antwoord=0,
        uitleg=r"Dan geldt \(E_{p} = E_{k} + Q\), met \(Q = \lvert W_{\text{wrijving}} \rvert\) "
        r"de energie die als warmte verdwijnt. Daarom komt de kist trager beneden dan "
        r"zonder wrijving.",
    ),
]

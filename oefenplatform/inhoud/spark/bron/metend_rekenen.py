# -*- coding: utf-8 -*-
"""De vragen voor "Metend rekenen" (✨ Spark, wiskunde).

De vakfiche zet hieronder: grootheden en eenheden (tijd, lengte, oppervlakte,
volume, massa), omzetten en afronden, omtrek van veelhoeken en van de cirkel,
oppervlakte van driehoeken, vierhoeken en cirkels, en oppervlakte én volume
van kubus, balk en cilinder.

Bij de cirkel rekenen we met π ≈ 3,14, en dat staat telkens in de vraag zelf.
Zo hoeft een kind niet te gokken met hoeveel cijfers er verwacht wordt.

Deel 1 gaat over eenheden en de gewone formules. Deel 2 vraagt samengestelde
figuren, ruimtefiguren en omgekeerd rekenen (van oppervlakte naar zijde).

Bij de vragen met een figuur staat achteraan een tekening tussen dubbele
accolades, bijvoorbeeld {{maat rechthoek 7x3}} of {{ruimte balk 5x3x2}}. Bij
het omzetten van eenheden staat de maatladder erbij, {{ladder oppervlakte}}.
Het platform tekent die zelf; de lijst staat in components/Tekeningen.tsx.
De maten in de markering zijn dezelfde als die in de vraag: verander je de
vraag, verander dan ook de tekening.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je wil de afstand tussen twee steden opschrijven. Welke eenheid past het best?",
        opties=["Kilometer", "Centimeter", "Milliliter"],
        antwoord=0,
        uitleg=r"Kilometer. Een geschikte eenheid kiezen scheelt veel nullen: \(120\) km leest makkelijker dan \(12\,000\,000\) cm.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel centimeter is \(1\) meter? {{ladder lengte}}",
        antwoord="100",
        uitleg=r"\(1\) m \(= 100\) cm. Elke stap op de maatladder is maal of gedeeld door \(10\), en van meter naar centimeter zijn het twee stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel meter is \(3{,}5\) km? {{ladder lengte}}",
        opties=[r"\(3500\) m", r"\(350\) m", r"\(35\) m"],
        antwoord=0,
        uitleg=r"\(1\) km \(= 1000\) m, dus \(3{,}5 \cdot 1000 = 3500\) m.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel minuten is \(2{,}5\) uur?",
        antwoord="150",
        uitleg=r"Een uur heeft \(60\) minuten: \(2{,}5 \cdot 60 = 150\) minuten. Let op, tijd gaat niet per tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel seconden zijn er in een kwartier?",
        opties=[r"\(900\)", r"\(150\)", r"\(1500\)"],
        antwoord=0,
        uitleg=r"Een kwartier is \(15\) minuten, en elke minuut heeft \(60\) seconden: \(15 \cdot 60 = 900\) s.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel gram is \(2{,}5\) kg? {{ladder massa}}",
        opties=[r"\(2500\) g", r"\(250\) g", r"\(25\,000\) g"],
        antwoord=0,
        uitleg=r"\(1\) kg \(= 1000\) g, dus \(2{,}5 \cdot 1000 = 2500\) g.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel milliliter gaat er in een halve liter?",
        opties=[r"\(500\) ml", r"\(50\) ml", r"\(5000\) ml"],
        antwoord=0,
        uitleg=r"\(1\) l \(= 1000\) ml, dus een halve liter is \(500\) ml.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de omtrek van een rechthoek van \(7\) cm bij \(3\) cm, in centimeter? {{maat rechthoek 7x3}}",
        antwoord="20",
        uitleg=r"\(\text{Omtrek} = 2 \cdot (\text{lengte} + \text{breedte}) = 2 \cdot (7 + 3) = 20\) cm. Je loopt één keer rond de figuur.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de oppervlakte van een rechthoek van \(7\) cm bij \(3\) cm, in \(\text{cm}^{2}\)? {{maat rechthoek 7x3}}",
        antwoord="21",
        uitleg=r"\(\text{Oppervlakte} = \text{lengte} \cdot \text{breedte} = 7 \cdot 3 = 21\,\text{cm}^{2}\). Let op de eenheid: oppervlakte staat in \(\text{cm}^{2}\), omtrek in cm.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vierkant heeft een zijde van \(6\) cm. Wat is zijn omtrek? {{maat vierkant 6}}",
        opties=[r"\(24\) cm", r"\(36\) cm", r"\(12\) cm"],
        antwoord=0,
        uitleg=r"Vier gelijke zijden: \(4 \cdot 6 = 24\) cm. Met \(6 \cdot 6 = 36\) krijg je de oppervlakte, en die staat in \(\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een driehoek heeft een basis van \(8\) cm en een hoogte van \(5\) cm. Wat is zijn oppervlakte? {{maat driehoek 8x5}}",
        opties=[r"\(20\,\text{cm}^{2}\)", r"\(40\,\text{cm}^{2}\)", r"\(13\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Oppervlakte \(\text{driehoek} = (\text{basis} \cdot \text{hoogte}) : 2 = (8 \cdot 5) : 2 = 20\,\text{cm}^{2}\). De helft van een rechthoek met dezelfde maten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een parallellogram heeft een basis van \(9\) cm en een hoogte van \(4\) cm. Wat is zijn oppervlakte? {{maat parallellogram 9x4}}",
        opties=[r"\(36\,\text{cm}^{2}\)", r"\(18\,\text{cm}^{2}\)", r"\(26\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Bij een parallellogram is het \(\text{basis} \cdot \text{hoogte} = 9 \cdot 4 = 36\,\text{cm}^{2}\), zonder delen door \(2\). En de hoogte is de loodrechte afstand, niet de schuine zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de formule voor de omtrek van een cirkel? {{cirkeldeel straal}}",
        opties=[r"\(2 \cdot \pi \cdot \text{straal}\)", r"\(\pi \cdot \text{straal} \cdot \text{straal}\)", r"\(\pi \cdot \text{straal}\)"],
        antwoord=0,
        uitleg=r"De omtrek is \(2 \cdot \pi \cdot \text{straal}\), of even goed \(\pi \cdot \text{diameter}\). Met \(\pi \cdot \text{straal}^{2}\) bereken je de oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een cirkel heeft een straal van \(5\) cm. Hoe groot is de omtrek? Neem \(\pi = 3{,}14\). {{maat cirkel straal 5}}",
        opties=[r"\(31{,}4\) cm", r"\(15{,}7\) cm", r"\(78{,}5\) cm"],
        antwoord=0,
        uitleg=r"\(\text{Omtrek} = 2 \cdot \pi \cdot \text{straal} = 2 \cdot 3{,}14 \cdot 5 = 31{,}4\) cm. Met \(78{,}5\) zou je de oppervlakte hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een cirkel heeft een straal van \(5\) cm. Hoe groot is de oppervlakte? Neem \(\pi = 3{,}14\). {{maat cirkel straal 5}}",
        opties=[r"\(78{,}5\,\text{cm}^{2}\)", r"\(31{,}4\,\text{cm}^{2}\)", r"\(15{,}7\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"\(\text{Oppervlakte} = \pi \cdot \text{straal}^{2} = 3{,}14 \cdot 25 = 78{,}5\,\text{cm}^{2}\). In de formule kwadrateer je de straal, je vermenigvuldigt niet met \(2\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het volume van een kubus met een ribbe van \(4\) cm, in \(\text{cm}^{3}\)? {{ruimte kubus 4}}",
        antwoord="64",
        uitleg=r"Volume \(\text{kubus} = \text{ribbe}^{3} = 4 \cdot 4 \cdot 4 = 64\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een balk is \(5\) cm bij \(3\) cm bij \(2\) cm. Wat is zijn volume? {{ruimte balk 5x3x2}}",
        opties=[r"\(30\,\text{cm}^{3}\)", r"\(60\,\text{cm}^{3}\)", r"\(10\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"Volume \(\text{balk} = \text{lengte} \cdot \text{breedte} \cdot \text{hoogte} = 5 \cdot 3 \cdot 2 = 30\,\text{cm}^{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(1\) liter is hetzelfde als \(1\,\text{dm}^{3}\).",
        antwoord=True,
        uitleg=r"Juist. Een kubus van \(1\) dm bij \(1\) dm bij \(1\) dm bevat precies \(1\) liter. En \(1\) ml is \(1\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(2{,}5\,\text{m}^{2}\) in \(\text{dm}^{2}\)? {{ladder oppervlakte}}",
        opties=[r"\(250\,\text{dm}^{2}\)", r"\(25\,\text{dm}^{2}\)", r"\(2500\,\text{dm}^{2}\)"],
        antwoord=0,
        uitleg=r"Bij oppervlakte gaat elke stap maal \(100\), niet maal \(10\): \(2{,}5 \cdot 100 = 250\,\text{dm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Rond \(12{,}467\) af tot op twee decimalen.",
        opties=[r"\(12{,}47\)", r"\(12{,}46\)", r"\(12{,}5\)"],
        antwoord=0,
        uitleg=r"Het derde decimaal is \(7\), dus het cijfer ervoor gaat één omhoog: \(12{,}47\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een vierkant heeft een oppervlakte van \(49\,\text{cm}^{2}\). Hoe lang is een zijde?",
        opties=[r"\(7\) cm", r"\(24{,}5\) cm", r"\(12{,}25\) cm"],
        antwoord=0,
        uitleg=r"\(\text{Zijde} \cdot \text{zijde} = 49\), dus de zijde is \(\sqrt{49} = 7\) cm. Hier gebruik je worteltrekken als omgekeerde van kwadrateren.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechthoek heeft een oppervlakte van \(48\,\text{cm}^{2}\) en een lengte van \(8\) cm. Hoe breed is hij?",
        opties=[r"\(6\) cm", r"\(40\) cm", r"\(16\) cm"],
        antwoord=0,
        uitleg=r"Oppervlakte : lengte = breedte, dus \(48 : 8 = 6\) cm.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trapezium heeft evenwijdige zijden van \(6\) cm en \(10\) cm en een hoogte van \(4\) cm. Wat is zijn oppervlakte? {{maat trapezium 6-10-4}}",
        opties=[r"\(32\,\text{cm}^{2}\)", r"\(40\,\text{cm}^{2}\)", r"\(64\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Oppervlakte trapezium = (som van de evenwijdige zijden) \(\cdot \text{hoogte} : 2 = (6 + 10) \cdot 4 : 2 = 32\,\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een ruit heeft diagonalen van \(8\) cm en \(6\) cm. Wat is zijn oppervlakte? {{maat ruit 8x6}}",
        opties=[r"\(24\,\text{cm}^{2}\)", r"\(48\,\text{cm}^{2}\)", r"\(14\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Oppervlakte \(\text{ruit} = (\text{diagonaal} \cdot \text{diagonaal}) : 2 = (8 \cdot 6) : 2 = 24\,\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een cirkel heeft een diameter van \(10\) cm. Hoe groot is de omtrek? Neem \(\pi = 3{,}14\). {{maat cirkel diameter 10}}",
        opties=[r"\(31{,}4\) cm", r"\(62{,}8\) cm", r"\(78{,}5\) cm"],
        antwoord=0,
        uitleg=r"\(\text{Omtrek} = \pi \cdot \text{diameter} = 3{,}14 \cdot 10 = 31{,}4\) cm. Let op of er een straal of een diameter gegeven is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oppervlakte van een kubus met een ribbe van \(3\) cm? {{ruimte kubus 3}}",
        opties=[r"\(54\,\text{cm}^{2}\)", r"\(27\,\text{cm}^{2}\)", r"\(9\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Een kubus heeft zes gelijke vierkanten: \(6 \cdot (3 \cdot 3) = 54\,\text{cm}^{2}\). Met \(27\) zou je het volume hebben, en dat staat in \(\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een balk is \(5\) cm bij \(4\) cm bij \(2\) cm. Wat is zijn totale oppervlakte? {{ruimte balk 5x4x2}}",
        opties=[r"\(76\,\text{cm}^{2}\)", r"\(40\,\text{cm}^{2}\)", r"\(38\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Drie paar vlakken: \(2 \cdot (5 \cdot 4) + 2 \cdot (5 \cdot 2) + 2 \cdot (4 \cdot 2) = 40 + 20 + 16 = 76\,\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een cilinder heeft een straal van \(3\) cm en een hoogte van \(10\) cm. Wat is zijn volume? Neem \(\pi = 3{,}14\). {{ruimte cilinder 3x10}}",
        opties=[r"\(282{,}6\,\text{cm}^{3}\)", r"\(94{,}2\,\text{cm}^{3}\)", r"\(188{,}4\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"Volume \(\text{cilinder} = \pi \cdot \text{straal}^{2} \cdot \text{hoogte} = 3{,}14 \cdot 9 \cdot 10 = 282{,}6\,\text{cm}^{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel liter gaat er in een kubus van \(2\) dm bij \(2\) dm bij \(2\) dm? {{ruimte kubus 2}}",
        antwoord="8",
        uitleg=r"\(2 \cdot 2 \cdot 2 = 8\,\text{dm}^{3}\), en \(1\,\text{dm}^{3}\) is \(1\) liter, dus \(8\) liter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een zwembad van \(10\) m bij \(5\) m staat \(1{,}5\) m vol water. Hoeveel liter is dat? {{ruimte balk 10x1,5x5}}",
        opties=[r"\(75\,000\) l", r"\(75\) l", r"\(7500\) l"],
        antwoord=0,
        uitleg=r"\(\text{Volume} = 10 \cdot 5 \cdot 1{,}5 = 75\,\text{m}^{3}\). Eén \(\text{m}^{3}\) is \(1000\) liter, dus \(75\,000\) liter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(3\,\text{m}^{2}\) in \(\text{cm}^{2}\)? {{ladder oppervlakte}}",
        opties=[r"\(30\,000\,\text{cm}^{2}\)", r"\(300\,\text{cm}^{2}\)", r"\(3000\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Van m naar cm is maal \(100\), dus bij oppervlakte maal \(100 \cdot 100 = 10\,000\). Dat geeft \(3 \cdot 10\,000 = 30\,000\,\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(2\,\text{m}^{3}\) in liter? {{ladder volume}}",
        opties=[r"\(2000\) l", r"\(200\) l", r"\(20\) l"],
        antwoord=0,
        uitleg=r"\(1\,\text{m}^{3}= 1000\,\text{dm}^{3}= 1000\) liter, dus \(2\,\text{m}^{3}= 2000\) liter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tuin van \(20\) m bij \(15\) m: hoeveel are is dat?",
        opties=[r"\(3\) are", r"\(30\) are", r"\(300\) are"],
        antwoord=0,
        uitleg=r"\(20 \cdot 15 = 300\,\text{m}^{2}\), en \(1\) are is \(100\,\text{m}^{2}\), dus \(3\) are. Een hectare is \(100\) are, ofwel \(10\,000\,\text{m}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een figuur bestaat uit een vierkant van \(6\) cm met daarop een halve cirkel met diameter \(6\) cm. Wat is de oppervlakte? Neem \(\pi = 3{,}14\). {{samengesteld halvecirkel 6}}",
        opties=[r"\(50{,}13\,\text{cm}^{2}\)", r"\(64{,}26\,\text{cm}^{2}\)", r"\(42{,}13\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Vierkant: \(6 \cdot 6 = 36\). Halve cirkel met straal \(3\): \((3{,}14 \cdot 9) : 2 = 14{,}13\). Samen \(50{,}13\,\text{cm}^{2}\). Bij samengestelde figuren splits je in stukken die je wél kent.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Uit een vierkant van \(10\) cm knip je in elke hoek een vierkantje van \(2\) cm. Wat blijft er over aan oppervlakte? {{samengesteld hoekjes 10 2}}",
        opties=[r"\(84\,\text{cm}^{2}\)", r"\(96\,\text{cm}^{2}\)", r"\(64\,\text{cm}^{2}\)"],
        antwoord=0,
        uitleg=r"Het grote vierkant is \(100\,\text{cm}^{2}\). Vier vierkantjes van \(2 \cdot 2 = 4\,\text{cm}^{2}\) geven samen \(16\,\text{cm}^{2}\). Blijft over: \(100 - 16 = 84\,\text{cm}^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een wandelpad van \(1{,}2\) km leg je af in \(15\) minuten. Hoeveel meter per minuut is dat?",
        opties=[r"\(80\) m", r"\(8\) m", r"\(800\) m"],
        antwoord=0,
        uitleg=r"\(1{,}2\) km is \(1200\) m, en \(1200 : 15 = 80\) meter per minuut. Zet altijd eerst alles in dezelfde eenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee rechthoeken met dezelfde omtrek hebben ook dezelfde oppervlakte.",
        antwoord=False,
        uitleg=r"Nee. Een rechthoek van \(1\) bij \(5\) en een van \(3\) bij \(3\) hebben allebei omtrek \(12\), maar de oppervlaktes zijn \(5\) en \(9\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt de zijde van een vierkant. Wat gebeurt er met de oppervlakte?",
        opties=["Ze wordt vier keer zo groot", "Ze wordt dubbel zo groot", "Ze blijft gelijk"],
        antwoord=0,
        uitleg=r"Een vierkant van \(3\) cm heeft oppervlakte \(9\,\text{cm}^{2}\), een van \(6\) cm heeft \(36\,\text{cm}^{2}\). Dat is vier keer zo veel, want allebei de afmetingen verdubbelen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een recept vraagt \(250\) ml melk. Hoeveel pakjes van \(1\) liter heb je nodig voor \(5\) keer het recept?",
        opties=[r"\(2\) pakjes", r"\(1\) pakje", r"\(5\) pakjes"],
        antwoord=0,
        uitleg=r"\(5 \cdot 250 = 1250\) ml, dus \(1{,}25\) liter. Eén pakje is te weinig, dus je hebt er \(2\) nodig. Hier rond je naar boven af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een plan heeft schaal \(1 : 200\). Een muur is \(4\) cm op het plan. Hoe lang is hij in het echt?",
        opties=[r"\(8\) m", r"\(80\) m", r"\(800\) m"],
        antwoord=0,
        uitleg=r"\(4 \cdot 200 = 800\) cm, en dat is \(8\) meter. Zet de uitkomst altijd om naar een eenheid die past bij wat je meet.",
    ),
]

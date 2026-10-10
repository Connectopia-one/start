# -*- coding: utf-8 -*-
"""Elektrische energie, potentiaal en spanning — 🌍 Beyond, fysica.

Deel 1 gaat over de arbeid van de elektrische kracht en over de elektrische
potentiële energie: hoe die verandert als een lading beweegt, en hoe ze samen
met de kinetische energie behouden blijft. Deel 2 gaat over de potentiaal en
de spanning: potentiaal als energie per eenheid van lading, het
potentiaalverschil tussen twee punten, de equipotentiaallijnen, en het
elektronvolt.

Het rode draadje is het verschil tussen energie en potentiaal. Energie hangt
af van de lading die je verplaatst, potentiaal niet: dat is een eigenschap van
het punt, net zoals veldsterkte dat is voor de kracht.

De formules staan in notatie, tussen \\( en \\): W = q U, V = Ep / q,
U = V_A - V_B, U = E d, q U = een half m v^2 en V = k q / r. Dat vroeg Enya
Vermeyen, leerkracht wiskunde en fysica, op 10 oktober 2026: zonder notatie
kan een leerkracht er in de les niets mee. Een leerling moet die symbolen
leren lezen, dus staan ze er ook in de vraag en niet enkel in de uitleg.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wanneer verricht een elektrische kracht arbeid \(W\)?",
        opties=[
            "als de lading verplaatst wordt in de zin van de kracht",
            "als de lading stil blijft liggen in het elektrisch veld",
            "als de lading loodrecht op de kracht verplaatst wordt",
            "als het veld van zin verandert zonder dat er iets beweegt",
        ],
        antwoord=0,
        uitleg=r"\(W=F\cdot d\), met \(d\) de verplaatsing in de zin van de kracht. "
        r"Beweegt de lading loodrecht op de kracht, dan is \(W=0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een lading van \(2\ \text{C}\) wordt over \(0{,}50\ \text{m}\) verplaatst door "
        r"een kracht van \(6{,}0\ \text{N}\) in dezelfde zin. Hoeveel arbeid is er verricht?",
        opties=[
            r"\(3{,}0\ \text{J}\)",
            r"\(12\ \text{J}\)",
            r"\(1{,}5\ \text{J}\)",
            r"\(24\ \text{J}\)",
        ],
        antwoord=0,
        uitleg=r"\(W=F\cdot d=6{,}0\cdot 0{,}50=3{,}0\ \text{J}\). De grootte van de lading "
        r"speelt hier geen rol meer, want die zit al in \(F\).",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je arbeid \(W\) en energie uit?",
        antwoord=["joule", "J", "de joule"],
        uitleg=r"Het symbool is \(\text{J}\): "
        r"\(1\ \text{J}=1\ \text{N}\cdot\text{m}=1\ \text{C}\cdot\text{V}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een positieve lading beweegt vanzelf van de positieve naar de negatieve plaat. Wat gebeurt er met haar energie?",
        opties=[
            "de potentiële energie daalt en de kinetische stijgt",
            "de potentiële energie stijgt en de kinetische daalt",
            "beide soorten energie stijgen samen even snel",
            "beide soorten energie blijven precies even groot",
        ],
        antwoord=0,
        uitleg=r"Het veld duwt de lading vooruit, dus wint ze snelheid. "
        r"\(E_{p}+E_{k}\) blijft wel gelijk, want er is geen wrijving in het spel.",
    ),
    dict(
        type="waarofniet",
        vraag="Om een positieve lading naar de positieve plaat te duwen, moet je zelf arbeid leveren.",
        antwoord=True,
        uitleg=r"Je gaat dan tegen de elektrische kracht in. Die arbeid komt als \(E_{p}\) "
        r"in de lading terecht, zoals een bal die je omhoog tilt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee kan je de elektrische potentiële energie van een lading het best vergelijken?",
        opties=[
            "met de hoogte-energie van een bal boven de grond",
            "met de warmte die een lamp tijdens het branden afgeeft",
            "met de snelheid van een auto op de autosnelweg",
            "met het gewicht van een voorwerp op een weegschaal",
        ],
        antwoord=0,
        uitleg="In beide gevallen zit de energie in de plaats waar het voorwerp staat. Laat "
        "je los, dan wordt ze kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de elektrische potentiële energie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze hangt af van de grootte van de lading zelf",
            "ze hangt af van de plaats in het elektrisch veld",
            "ze hangt af van de massa van het geladen deeltje",
            "ze hangt af van de snelheid waarmee de lading beweegt",
        ],
        antwoord=[0, 1],
        uitleg=r"Massa en snelheid horen bij \(E_{k}\). Er geldt \(E_{p}=q\cdot V\): de "
        r"lading zelf maal iets wat enkel van de plaats afhangt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een elektron vertrekt uit rust bij de negatieve plaat en gaat naar de positieve. Wat gebeurt er?",
        opties=[
            "het wordt versneld en komt met maximale snelheid aan",
            "het wordt afgeremd en komt juist tot stilstand",
            "het beweegt met een constante snelheid naar de plaat",
            "het blijft liggen, want een elektron voelt geen kracht",
        ],
        antwoord=0,
        uitleg="De negatieve plaat stoot het elektron af en de positieve trekt het aan. Al "
        "zijn potentiële energie wordt onderweg kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de snelheid \(v\) waarmee een lading uit rust bij de andere plaat aankomt?",
        opties=[
            r"met \(q\,U=\tfrac{1}{2}m\,v^{2}\)",
            r"met \(v=\dfrac{U}{d}\)",
            r"met \(v=E\cdot m\)",
            r"met \(v=\dfrac{q}{m}\)",
        ],
        antwoord=0,
        uitleg=r"Alle gewonnen energie \(q\,U\) zit in de beweging, dus "
        r"\(v=\sqrt{\dfrac{2q\,U}{m}}\). Dat werkt omdat er onderweg niets verloren gaat.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De arbeid \(W\) van de elektrische kracht hangt af van de weg die de lading aflegt.",
        antwoord=False,
        uitleg="Alleen begin- en eindpunt tellen, net als bij de zwaartekracht. Daarom kan "
        "je met potentiële energie rekenen zonder de baan te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een lading van \(4{,}0\ \text{mC}\) verliest \(0{,}80\ \text{J}\) potentiële "
        r"energie tussen twee punten. Welke spanning \(U\) staat er tussen die punten?",
        opties=[
            r"\(200\ \text{V}\)",
            r"\(3{,}2\ \text{V}\)",
            r"\(0{,}005\ \text{V}\)",
            r"\(20\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"\(U=\dfrac{W}{q}=\dfrac{0{,}80}{4{,}0\cdot 10^{-3}}=200\ \text{V}\). "
        r"Let op de omzetting van millicoulomb naar coulomb.",
    ),
    dict(
        type="invultekst",
        vraag="Welke energie heeft een deeltje door zijn beweging?",
        antwoord=["kinetische energie", "kinetische", "bewegingsenergie"],
        uitleg=r"\(E_{k}=\tfrac{1}{2}m\,v^{2}\). \(E_{p}\) hangt daarentegen af van de "
        r"plaats en niet van de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee platen staan \(2{,}0\ \text{cm}\) uit elkaar met \(E=5000\ \text{N/C}\) "
        r"ertussen. Welke spanning staat erover?",
        opties=[
            r"\(100\ \text{V}\)",
            r"\(250\ \text{V}\)",
            r"\(10\ \text{V}\)",
            r"\(2500\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"In een homogeen veld geldt \(U=E\cdot d=5000\cdot 0{,}020=100\ \text{V}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij de beweging van een lading in een elektrisch veld blijft \(E_{k}+E_{p}\) behouden.",
        antwoord=True,
        uitleg="Zolang er geen wrijving of botsingen zijn, gaat de ene energievorm volledig "
        "in de andere over. Dat is de wet van behoud van energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de potentiële energie van een negatieve lading die naar de negatieve plaat beweegt?",
        opties=[
            "ze stijgt, want de lading gaat tegen de kracht in",
            "ze daalt, want de lading gaat met de kracht mee",
            "ze blijft gelijk, want de lading is negatief geladen",
            "ze wordt nul zodra de lading de plaat bereikt",
        ],
        antwoord=0,
        uitleg="Een negatieve lading wordt door de negatieve plaat afgestoten. Beweegt ze "
        "er toch naartoe, dan moet iets anders die arbeid leveren, en haar potentiële "
        "energie stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke grootheden heb je nodig om \(v\) van een lading tussen twee platen te berekenen? Kruis alles aan wat juist is.",
        opties=[
            r"de spanning \(U\) tussen de platen",
            r"de massa \(m\) van het deeltje",
            r"de afstand \(d\) tussen de platen",
            r"de tijd \(t\) die het onderweg is",
        ],
        antwoord=[0, 1],
        uitleg=r"Uit \(q\,U=\tfrac{1}{2}m\,v^{2}\) volgt \(v\). De lading \(q\) heb je ook "
        r"nodig, maar \(d\) en \(t\) niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een elektron veel sneller dan een proton bij dezelfde spanning?",
        opties=[
            "het elektron heeft een veel kleinere massa",
            "het elektron heeft een veel grotere lading",
            "het elektron wordt door twee platen tegelijk geduwd",
            "het elektron verliest onderweg geen enkele energie",
        ],
        antwoord=0,
        uitleg=r"Beide krijgen dezelfde \(q\,U\), want \(|q|\) is even groot. Uit "
        r"\(v=\sqrt{\dfrac{2q\,U}{m}}\) volgt dat een kleinere \(m\) een hogere \(v\) geeft: "
        r"een elektron is ruim \(1800\) keer lichter dan een proton.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lading die loodrecht op de veldlijnen verplaatst wordt, verandert van potentiële energie.",
        antwoord=False,
        uitleg="Loodrecht op de veldlijnen verricht de elektrische kracht geen arbeid. Die "
        "richting volgt precies een equipotentiaallijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verband tussen de arbeid \(W\) van de elektrische kracht en \(E_{k}\)?",
        opties=[
            r"\(W=\Delta E_{k}\)",
            r"\(W=m\cdot v\)",
            r"\(W=2\,E_{k}\)",
            r"\(W\) en \(E_{k}\) hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg=r"Dat is de arbeid-energiestelling. Wat \(E_{p}\) verliest, komt als beweging "
        r"terug: \(-\Delta E_{p}=\Delta E_{k}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel joule is \(1\ \text{eV}\) ongeveer?",
        antwoord=["1,6·10⁻¹⁹ J", "1,6e-19", "1,6·10⁻¹⁹"],
        uitleg=r"\(1\ \text{eV}=e\cdot 1\ \text{V}=1{,}602\cdot 10^{-19}\ \text{J}\): de "
        r"energie die één elementaire lading wint bij één volt. \(e\) staat in de bijlage "
        r"die je op het examen krijgt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de elektrische potentiaal \(V\) in een punt?",
        opties=[
            r"\(V=\dfrac{E_{p}}{q}\)",
            r"\(V=\dfrac{F}{q}\)",
            r"\(V=\dfrac{E_{p}}{t}\)",
            r"\(V=q\)",
        ],
        antwoord=0,
        uitleg=r"Je deelt \(E_{p}\) door \(q\), net zoals je bij de veldsterkte \(F\) door "
        r"\(q\) deelt. Zo krijg je een eigenschap van het punt zelf, en niet van de lading "
        r"die je erin zet.",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je de elektrische potentiaal \(V\) uit?",
        antwoord=["volt", "V", "de volt"],
        uitleg=r"\(1\ \text{V}=1\ \text{J/C}\). Het potentiaalverschil tussen twee punten "
        r"heet de spanning, en staat in dezelfde eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de spanning \(U_{AB}\) tussen twee punten \(A\) en \(B\)?",
        opties=[
            r"\(U_{AB}=V_{A}-V_{B}\)",
            r"\(U_{AB}=V_{A}+V_{B}\)",
            r"\(U_{AB}=V_{A}\cdot V_{B}\)",
            r"\(U_{AB}=F_{A}-F_{B}\)",
        ],
        antwoord=0,
        uitleg=r"Daarom heet \(U\) ook het potentiaalverschil. Een spanning hoort dus altijd "
        r"bij twee punten, nooit bij één punt alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(V_{A}=120\ \text{V}\) en \(V_{B}=45\ \text{V}\). Hoe groot is \(U_{AB}\)?",
        opties=[
            r"\(75\ \text{V}\)",
            r"\(165\ \text{V}\)",
            r"\(45\ \text{V}\)",
            r"\(120\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"\(U_{AB}=V_{A}-V_{B}=120-45=75\ \text{V}\). Het teken zegt enkel welk punt "
        r"de hoogste potentiaal heeft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een lijn waarop de potentiaal overal dezelfde is?",
        antwoord=["equipotentiaallijn", "equipotentiaal", "een equipotentiaallijn"],
        uitleg="In de ruimte spreekt men van een equipotentiaaloppervlak. Verplaats je een "
        "lading erlangs, dan is de arbeid nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe staan de equipotentiaallijnen tegenover de veldlijnen?",
        opties=[
            "loodrecht op de veldlijnen",
            "evenwijdig met de veldlijnen",
            "onder een hoek van 45 graden erop",
            "er is geen vast verband tussen de twee",
        ],
        antwoord=0,
        uitleg="Langs een equipotentiaallijn verricht de kracht geen arbeid, en dat kan "
        "alleen als de verplaatsing loodrecht op de kracht staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zien de equipotentiaallijnen rond één puntlading eruit?",
        opties=[
            "als cirkels rond de lading heen",
            "als rechte lijnen door de lading heen",
            "als evenwijdige lijnen naast de lading",
            "als een spiraal die van de lading weg draait",
        ],
        antwoord=0,
        uitleg="De veldlijnen lopen daar stervormig naar buiten, dus staan de "
        "equipotentiaallijnen er als cirkels loodrecht op. Tussen twee platen zijn het "
        "rechte, evenwijdige lijnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lading die je langs een equipotentiaallijn verplaatst, kost geen arbeid.",
        antwoord=True,
        uitleg="De potentiaal verandert niet, dus de potentiële energie ook niet. Er is dus "
        "geen energie bij of af gegaan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een lading van \(5{,}0\ \text{mC}\) zit in een punt met \(V=40\ \text{V}\). "
        r"Hoe groot is \(E_{p}\) daar?",
        opties=[
            r"\(0{,}20\ \text{J}\)",
            r"\(8{,}0\ \text{J}\)",
            r"\(200\ \text{J}\)",
            r"\(1{,}25\cdot 10^{-4}\ \text{J}\)",
        ],
        antwoord=0,
        uitleg=r"\(E_{p}=q\cdot V=5{,}0\cdot 10^{-3}\cdot 40=0{,}20\ \text{J}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitspraken over \(V\) zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze hoort bij het punt, niet bij de lading",
            r"ze staat in \(\text{V}\)",
            r"ze staat in \(\text{N/C}\)",
            r"ze groeit mee met de proeflading \(q\)",
        ],
        antwoord=[0, 1],
        uitleg=r"\(\text{N/C}\) is de eenheid van \(E\). Zet je een dubbel zo grote lading in "
        r"hetzelfde punt, dan verdubbelt \(E_{p}=q\,V\) maar niet \(V\) zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kant op beweegt een positieve lading vanzelf?",
        opties=[
            "van een hoge naar een lage potentiaal",
            "van een lage naar een hoge potentiaal",
            "altijd naar het punt met de grootste lading",
            "altijd loodrecht op de veldlijnen weg",
        ],
        antwoord=0,
        uitleg="Ze volgt het veld, en dat wijst van hoge naar lage potentiaal. Een "
        "negatieve lading beweegt vanzelf net de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="De potentiaal van een punt hangt af van de lading die je erin zet.",
        antwoord=False,
        uitleg="De potentiaal wordt bepaald door de ladingen die het veld maken, niet door "
        "de proeflading. Alleen de energie van die proeflading hangt van haar grootte af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een elektron wint \(3{,}2\cdot 10^{-17}\ \text{J}\). Hoeveel elektronvolt is dat?",
        opties=[
            r"\(200\ \text{eV}\)",
            r"\(2{,}0\ \text{eV}\)",
            r"\(5{,}1\cdot 10^{-36}\ \text{eV}\)",
            r"\(3{,}2\cdot 10^{-17}\ \text{eV}\)",
        ],
        antwoord=0,
        uitleg=r"Delen door \(1{,}602\cdot 10^{-19}\): "
        r"\(\dfrac{3{,}2\cdot 10^{-17}}{1{,}602\cdot 10^{-19}}\approx 200\ \text{eV}\). "
        r"Omgekeerd vermenigvuldig je.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een elektron doorloopt een spanning van \(500\ \text{V}\). Hoeveel energie wint het?",
        opties=[
            r"\(500\ \text{eV}\)",
            r"\(500\ \text{J}\)",
            r"\(0{,}50\ \text{eV}\)",
            r"\(1{,}6\cdot 10^{-19}\ \text{eV}\)",
        ],
        antwoord=0,
        uitleg=r"\(W=q\,U\), en één elementaire lading door één volt is per afspraak "
        r"\(1\ \text{eV}\). In joule is dat \(500\cdot 1{,}602\cdot 10^{-19}=8{,}0\cdot "
        r"10^{-17}\ \text{J}\).",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil in potentiaal tussen twee punten, met één woord?",
        antwoord=["spanning", "de spanning", "potentiaalverschil"],
        uitleg=r"Het symbool is \(U\) en de eenheid \(\text{V}\). Een spanningsbron houdt "
        r"dat verschil in stand.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Tussen twee punten op hetzelfde equipotentiaaloppervlak geldt \(U=0\).",
        antwoord=True,
        uitleg="Hun potentialen zijn gelijk, dus is het verschil nul. Daarom loopt er "
        "tussen zulke punten ook geen stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom staat er in \(V=k\dfrac{q}{r}\) een \(r\) en geen \(r^{2}\)?",
        opties=[
            "potentiaal gaat over energie, en die telt de afstand maar één keer",
            r"\(V\) is altijd veel kleiner dan \(E\) in dat punt",
            r"\(V\) heeft geen zin, dus mag het kwadraat wegvallen",
            r"\(V\) wordt per seconde gemeten en \(E\) niet",
        ],
        antwoord=0,
        uitleg=r"\(F\) gaat met \(r^{2}\) en arbeid is kracht maal afstand, dus valt er één "
        r"\(r\) weg. Vandaar \(E=k\dfrac{|q|}{r^{2}}\) naast \(V=k\dfrac{q}{r}\). Let op: "
        r"\(V\) draagt wel het teken van \(q\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken gelden voor een homogeen veld? Kruis alles aan wat juist is.",
        opties=[
            r"\(U=E\cdot d\)",
            "de equipotentiaallijnen zijn evenwijdige rechten",
            r"\(V\) is overal tussen de platen even groot",
            r"\(E\) neemt af naarmate je verder van de plaat zit",
        ],
        antwoord=[0, 1],
        uitleg=r"\(E\) is overal gelijk, maar \(V\) niet: die daalt gelijkmatig van de ene "
        r"plaat naar de andere. Uit \(U=E\cdot d\) volgt ook \(E=\dfrac{U}{d}\), in "
        r"\(\text{V/m}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt een spanningsbron in een kring in stand?",
        opties=[
            "een potentiaalverschil tussen haar twee polen",
            "een gelijke potentiaal aan haar twee polen",
            "een gelijke lading op haar twee polen",
            "een constante stroomsterkte in elke tak",
        ],
        antwoord=0,
        uitleg="Zonder dat verschil zouden de ladingen meteen stilvallen. De bron duwt ze "
        "telkens opnieuw naar de pool met de hoogste potentiaal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(U=0\) betekent dat er geen lading aanwezig is.",
        antwoord=False,
        uitleg="Het betekent alleen dat de twee punten dezelfde potentiaal hebben. Er kan "
        "op beide plaatsen evenveel lading zitten.",
    ),
]

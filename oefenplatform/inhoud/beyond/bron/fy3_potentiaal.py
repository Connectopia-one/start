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
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een elektrische kracht arbeid?",
        opties=[
            "als de lading verplaatst wordt in de zin van de kracht",
            "als de lading stil blijft liggen in het elektrisch veld",
            "als de lading loodrecht op de kracht verplaatst wordt",
            "als het veld van zin verandert zonder dat er iets beweegt",
        ],
        antwoord=0,
        uitleg="Arbeid is kracht maal verplaatsing in de zin van die kracht. Beweegt de "
        "lading loodrecht op de kracht, dan is de arbeid nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lading van 2 C wordt over 0,5 m verplaatst door een kracht van 6 N in dezelfde zin. Hoeveel arbeid is er verricht?",
        opties=[
            "3 J",
            "12 J",
            "1,5 J",
            "24 J",
        ],
        antwoord=0,
        uitleg="Arbeid is kracht maal afstand: 6 maal 0,5 is 3 joule. De grootte van de "
        "lading speelt hier geen rol meer, want die zit al in de kracht.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je arbeid en energie uit?",
        antwoord=["joule", "J", "de joule"],
        uitleg="Het symbool is J. Eén joule is één newton maal één meter.",
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
        uitleg="Het veld duwt de lading vooruit, dus wint ze snelheid. De som van de twee "
        "soorten energie blijft wel gelijk, want er is geen wrijving in het spel.",
    ),
    dict(
        type="waarofniet",
        vraag="Om een positieve lading naar de positieve plaat te duwen, moet je zelf arbeid leveren.",
        antwoord=True,
        uitleg="Je gaat dan tegen de elektrische kracht in. Die arbeid komt als elektrische "
        "potentiële energie in de lading terecht, zoals een bal die je omhoog tilt.",
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
        uitleg="Massa en snelheid horen bij de kinetische energie. Potentiële energie is "
        "lading maal potentiaal, dus lading maal iets van de plaats.",
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
        vraag="Hoe bereken je de snelheid waarmee een lading uit rust bij de andere plaat aankomt?",
        opties=[
            "je stelt de gewonnen kinetische energie gelijk aan de verloren potentiële",
            "je deelt de spanning tussen de platen door de afstand ertussen",
            "je vermenigvuldigt de veldsterkte met de massa van het deeltje",
            "je deelt de lading van het deeltje door zijn eigen massa",
        ],
        antwoord=0,
        uitleg="Q maal U is gelijk aan een half m maal v kwadraat. Daaruit haal je v, en "
        "dat werkt omdat er onderweg geen energie verloren gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeid van de elektrische kracht hangt af van de weg die de lading aflegt.",
        antwoord=False,
        uitleg="Alleen begin- en eindpunt tellen, net als bij de zwaartekracht. Daarom kan "
        "je met potentiële energie rekenen zonder de baan te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lading van 4 mC verliest 0,8 J potentiële energie tussen twee punten. Welke spanning staat er tussen die punten?",
        opties=[
            "200 V",
            "3,2 V",
            "0,005 V",
            "20 V",
        ],
        antwoord=0,
        uitleg="Spanning is energie per eenheid van lading: 0,8 gedeeld door 0,004 is 200 "
        "volt. Let op de omzetting van millicoulomb naar coulomb.",
    ),
    dict(
        type="invultekst",
        vraag="Welke energie heeft een deeltje door zijn beweging?",
        antwoord=["kinetische energie", "kinetische", "bewegingsenergie"],
        uitleg="Ze is een half maal de massa maal het kwadraat van de snelheid. Potentiële "
        "energie hangt daarentegen af van de plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee platen staan 2 cm uit elkaar met een veldsterkte van 5000 N/C ertussen. Welke spanning staat erover?",
        opties=[
            "100 V",
            "250 V",
            "10 V",
            "2500 V",
        ],
        antwoord=0,
        uitleg="In een homogeen veld is de spanning de veldsterkte maal de afstand: 5000 "
        "maal 0,02 is 100 volt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de beweging van een lading in een elektrisch veld blijft de som van de kinetische en de potentiële energie behouden.",
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
        vraag="Welke grootheden heb je nodig om de maximale snelheid van een lading tussen twee platen te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de spanning tussen de twee platen",
            "de massa van het geladen deeltje",
            "de afstand tussen de twee platen",
            "de tijd die het deeltje onderweg is",
        ],
        antwoord=[0, 1],
        uitleg="Uit Q maal U is gelijk aan een half m maal v kwadraat volgt v. De afstand "
        "en de tijd heb je daarvoor niet nodig.",
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
        uitleg="Beide krijgen dezelfde energie, want hun lading is even groot. Een kleinere "
        "massa betekent bij dezelfde energie een veel hogere snelheid.",
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
        vraag="Wat is het verband tussen de arbeid van de elektrische kracht en de kinetische energie?",
        opties=[
            "de verrichte arbeid is gelijk aan de winst aan kinetische energie",
            "de verrichte arbeid is gelijk aan de massa maal de snelheid",
            "de verrichte arbeid is altijd het dubbele van die energie",
            "de verrichte arbeid heeft met die energie niets te maken",
        ],
        antwoord=0,
        uitleg="Dat is de arbeid-energiestelling. Wat de potentiële energie verliest, komt "
        "als beweging terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel joule is één elektronvolt ongeveer?",
        antwoord=["1,6·10⁻¹⁹ J", "1,6e-19", "1,6·10⁻¹⁹"],
        uitleg="Het is de energie die één elementaire lading wint bij één volt spanning. "
        "Daarom is het een handige eenheid voor deeltjes.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de elektrische potentiaal in een punt?",
        opties=[
            "de potentiële energie per eenheid van lading in dat punt",
            "de kracht per eenheid van lading in dat punt",
            "de energie die een lading er per seconde verliest",
            "de lading die in dat punt aanwezig is",
        ],
        antwoord=0,
        uitleg="Je deelt de potentiële energie door de lading, net zoals je bij de "
        "veldsterkte de kracht door de lading deelt. Zo krijg je een eigenschap van het "
        "punt zelf.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de elektrische potentiaal uit?",
        antwoord=["volt", "V", "de volt"],
        uitleg="Eén volt is één joule per coulomb. Het potentiaalverschil tussen twee "
        "punten heet de spanning, en staat in dezelfde eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de elektrische spanning tussen twee punten?",
        opties=[
            "het verschil tussen de potentialen van die twee punten",
            "de som van de potentialen van die twee punten",
            "de potentiaal van het punt met de grootste lading",
            "de kracht die tussen die twee punten werkt",
        ],
        antwoord=0,
        uitleg="Daarom heet ze ook het potentiaalverschil. Een spanning is dus altijd "
        "tussen twee punten, nooit in één punt alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Punt A ligt op 120 V en punt B op 45 V. Welke spanning staat er tussen A en B?",
        opties=[
            "75 V",
            "165 V",
            "45 V",
            "120 V",
        ],
        antwoord=0,
        uitleg="Je neemt het verschil: 120 min 45 is 75 volt. Het teken zegt enkel welke "
        "kant van de twee de hoogste potentiaal heeft.",
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
        vraag="Een lading van 5 mC zit in een punt met een potentiaal van 40 V. Hoeveel potentiële energie heeft ze daar?",
        opties=[
            "0,2 J",
            "8 J",
            "200 J",
            "0,000125 J",
        ],
        antwoord=0,
        uitleg="De energie is de lading maal de potentiaal: 0,005 maal 40 is 0,2 joule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over potentiaal zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is een eigenschap van het punt, niet van de lading",
            "ze wordt in volt uitgedrukt",
            "ze wordt in newton per coulomb uitgedrukt",
            "ze wordt groter naarmate de proeflading groter is",
        ],
        antwoord=[0, 1],
        uitleg="Newton per coulomb is de eenheid van veldsterkte. Zet je een dubbel zo "
        "grote lading in hetzelfde punt, dan verdubbelt haar energie maar niet de "
        "potentiaal.",
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
        vraag="Hoe reken je joule om naar elektronvolt?",
        opties=[
            "je deelt door 1,6·10⁻¹⁹",
            "je vermenigvuldigt met 1,6·10⁻¹⁹",
            "je deelt door 6,02·10²³",
            "je vermenigvuldigt met 9·10⁹",
        ],
        antwoord=0,
        uitleg="Eén elektronvolt is 1,6·10⁻¹⁹ joule, dus zitten er heel veel elektronvolt in "
        "één joule. De omgekeerde omzetting doe je door te vermenigvuldigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een elektron doorloopt een spanning van 500 V. Hoeveel energie wint het?",
        opties=[
            "500 eV",
            "500 J",
            "0,5 eV",
            "1,6·10⁻¹⁹ eV",
        ],
        antwoord=0,
        uitleg="Eén elementaire lading door één volt geeft precies één elektronvolt. "
        "Daarom is die eenheid in de deeltjesfysica zo handig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil in potentiaal tussen twee punten, met één woord?",
        antwoord=["spanning", "de spanning", "potentiaalverschil"],
        uitleg="Het symbool is U en de eenheid de volt. Een spanningsbron houdt dat "
        "verschil in stand.",
    ),
    dict(
        type="waarofniet",
        vraag="Tussen twee punten op hetzelfde equipotentiaaloppervlak staat een spanning van nul.",
        antwoord=True,
        uitleg="Hun potentialen zijn gelijk, dus is het verschil nul. Daarom loopt er "
        "tussen zulke punten ook geen stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit er in de formule voor potentiaal van een puntlading r en niet r kwadraat?",
        opties=[
            "potentiaal gaat over energie, en die telt de afstand maar één keer",
            "potentiaal is altijd veel kleiner dan de veldsterkte in dat punt",
            "potentiaal heeft geen zin, dus mag het kwadraat wegvallen",
            "potentiaal wordt per seconde gemeten en veldsterkte niet",
        ],
        antwoord=0,
        uitleg="De kracht gaat met r² en de arbeid is kracht maal afstand, dus valt er één "
        "r weg. Veldsterkte heeft r² in de noemer, potentiaal gewoon r.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken gelden voor een homogeen veld? Kruis alles aan wat juist is.",
        opties=[
            "de spanning is de veldsterkte maal de afstand",
            "de equipotentiaallijnen zijn evenwijdige rechten",
            "de potentiaal is overal tussen de platen even groot",
            "de veldsterkte neemt af naarmate je verder van de plaat zit",
        ],
        antwoord=[0, 1],
        uitleg="De veldsterkte is overal gelijk, maar de potentiaal niet: die daalt "
        "gelijkmatig van de ene plaat naar de andere.",
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
        vraag="Een spanning van nul volt betekent dat er geen lading aanwezig is.",
        antwoord=False,
        uitleg="Het betekent alleen dat de twee punten dezelfde potentiaal hebben. Er kan "
        "op beide plaatsen evenveel lading zitten.",
    ),
]

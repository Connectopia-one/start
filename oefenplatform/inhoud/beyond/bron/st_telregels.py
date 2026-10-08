# -*- coding: utf-8 -*-
"""De telregels: de productregel, de somregel en de complementregel.

Het begin van het onderdeel "Telproblemen, kansrekenen en statistiek", dat op
het examen zestig procent weegt. De vakfiche vraagt deze drie regels letterlijk
bij naam, en telkens in opgaven met context.

Deel 1 zijn de productregel en de somregel: wanneer je vermenigvuldigt en
wanneer je optelt.
Deel 2 is de complementregel en het combineren van de drie regels in één
opgave.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je de productregel?",
        opties=[
            "als je na elkaar een eerste en een tweede keuze maakt",
            "als je moet kiezen tussen een eerste of een tweede mogelijkheid",
            "als je wil tellen hoeveel gevallen juist niet aan de voorwaarde voldoen",
            "als de volgorde van de gekozen elementen geen enkel belang heeft",
        ],
        antwoord=0,
        uitleg="Het woordje en wijst op vermenigvuldigen, het woordje of op optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een menu heeft vier voorgerechten en zes hoofdgerechten. Hoeveel menu's van twee gangen zijn er?",
        opties=["vierentwintig", "tien", "twaalf", "dertig"],
        antwoord=0,
        uitleg="Vier maal zes is vierentwintig. Je kiest een voorgerecht én een hoofdgerecht, dus je vermenigvuldigt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school biedt drie talen en vijf sporten aan. Je kiest één activiteit, een taal of een sport. Hoeveel keuzes heb je?",
        opties=["acht", "vijftien", "twee", "vijf"],
        antwoord=0,
        uitleg="Drie plus vijf is acht. Je kiest een taal óf een sport, niet allebei, dus je telt op.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de somregel mogen de twee groepen elkaar niet overlappen.",
        antwoord=True,
        uitleg="Zit iemand in allebei de groepen, dan tel je die dubbel. Dan moet je de overlap er weer aftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel codes van drie cijfers bestaan er als elk cijfer van nul tot negen mag en herhaling toegelaten is?",
        opties=["duizend", "zevenhonderdtwintig", "driehonderd", "dertig"],
        antwoord=0,
        uitleg="Tien maal tien maal tien is duizend: voor elke plaats heb je opnieuw tien mogelijkheden.",
    ),
    dict(
        type="invultekst",
        vraag="Welk voegwoord in een opgave wijst meestal op vermenigvuldigen? Eén woord.",
        antwoord=["en"],
        uitleg="En betekent dat beide keuzes gemaakt worden, dus productregel. Of betekent één van de twee, dus somregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietsslot heeft vier ringen met telkens de cijfers nul tot negen. Hoeveel standen zijn er?",
        opties=["tienduizend", "vijfduizend", "vierduizend", "veertig"],
        antwoord=0,
        uitleg="Tien tot de vierde is tienduizend. Elke ring staat los van de andere.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de productregel moeten de twee keuzes evenveel mogelijkheden hebben.",
        antwoord=False,
        uitleg="Helemaal niet. Vier voorgerechten en zes hoofdgerechten geven gewoon vierentwintig menu's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nummerplaat bestaat uit drie letters gevolgd door drie cijfers. Hoeveel zijn er, met zesentwintig letters?",
        opties=[
            "zesentwintig tot de derde maal tien tot de derde",
            "zesentwintig maal drie plus tien maal drie",
            "zesentwintig plus tien, alles tot de derde macht",
            "zesentwintig tot de derde plus tien tot de derde",
        ],
        antwoord=0,
        uitleg="Drie letters én drie cijfers: je vermenigvuldigt de twee aantallen met elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas zitten twaalf meisjes en acht jongens. Hoeveel manieren zijn er om één leerling af te vaardigen?",
        opties=["twintig", "zesennegentig", "vier", "tweeëntwintig"],
        antwoord=0,
        uitleg="Twaalf plus acht is twintig. Eén leerling is een meisje óf een jongen, dus somregel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mogelijkheden zijn er voor een pincode van vier cijfers, cijfers mogen herhalen? Schrijf het getal.",
        antwoord=["10000", "10 000", "tienduizend"],
        uitleg="Tien mogelijkheden per plaats, vier plaatsen, dus tien tot de vierde.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de tweede keuze van de eerste afhangt, mag je nog altijd vermenigvuldigen zolang er voor de tweede keuze telkens even veel mogelijkheden zijn.",
        antwoord=True,
        uitleg="Dat is precies het hoorntje met twee verschillende bollen: tien smaken voor de eerste bol, en wat die ook is, negen voor de tweede. Dus tien maal negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ijssalon heeft tien smaken. Je neemt een hoorntje met twee bollen, en de volgorde telt. Hoeveel mogelijkheden, als dezelfde smaak twee keer mag?",
        opties=["honderd", "negentig", "vijfenveertig", "twintig"],
        antwoord=0,
        uitleg="Tien maal tien is honderd. Mocht dezelfde smaak niet twee keer mogen, dan was het tien maal negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is tien maal negen het antwoord als dezelfde smaak niet twee keer mag?",
        opties=[
            "omdat er voor de tweede bol één smaak wegvalt, namelijk die van de eerste",
            "omdat je de volgorde dan niet meer mag meetellen in je berekening",
            "omdat je daarna nog door twee moet delen om dubbels te vermijden",
            "omdat negen het grootste cijfer is dat in een telprobleem voorkomt",
        ],
        antwoord=0,
        uitleg="Bij elke volgende keuze kijk je opnieuw hoeveel er nog overblijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een restaurant heeft drie soepen, vijf hoofdgerechten en twee desserts. Hoeveel driegangenmenu's?",
        opties=["dertig", "tien", "vijftien", "twaalf"],
        antwoord=0,
        uitleg="Drie maal vijf maal twee is dertig. De productregel werkt voor zoveel keuzes als je wil.",
    ),
    dict(
        type="waarofniet",
        vraag="De productregel geldt alleen voor precies twee opeenvolgende keuzes.",
        antwoord=False,
        uitleg="Je mag zoveel factoren vermenigvuldigen als er keuzes zijn, bijvoorbeeld drie bij een driegangenmenu.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel menu's zijn er met vijf voorgerechten en vier hoofdgerechten? Schrijf het getal.",
        antwoord=["20", "twintig"],
        uitleg="Vijf maal vier is twintig. Je kiest er één van elk, dus productregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wachtwoord bestaat uit twee letters en daarna twee cijfers, alles mag herhalen. Hoeveel wachtwoorden met zesentwintig letters?",
        opties=["zesenzestigduizend zeshonderd", "zeshonderdzesentachtig", "zevenhonderdtwintig", "vijfhonderdtwintig"],
        antwoord=0,
        uitleg="Zesentwintig maal zesentwintig is zeshonderdzesenzeventig, maal honderd is zesenzestigduizend zeshonderd.",
    ),
    dict(
        type="waarofniet",
        vraag="Als twee groepen elkaar overlappen, mag je hun aantallen gewoon optellen.",
        antwoord=False,
        uitleg="Dan tel je de overlap twee keer. Je telt op en trekt daarna de overlap er één keer af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vijftien leerlingen volgen Frans, twaalf volgen Duits en vier volgen allebei. Hoeveel leerlingen volgen minstens één van de twee?",
        opties=["drieëntwintig", "zevenentwintig", "eenendertig", "negentien"],
        antwoord=0,
        uitleg="Vijftien plus twaalf is zevenentwintig, min de vier die je dubbel telde, geeft drieëntwintig.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de complementregel?",
        opties=[
            "het aantal gevallen dat voldoet is het totaal min het aantal dat niet voldoet",
            "het aantal gevallen dat voldoet is de som van twee deelgroepen",
            "het aantal gevallen dat voldoet is het product van twee opeenvolgende keuzes",
            "het aantal gevallen dat voldoet is altijd de helft van het totale aantal",
        ],
        antwoord=0,
        uitleg="Handig zodra het woordje minstens of ten minste in de opgave staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit drie keer met een munt. Hoeveel uitkomsten hebben minstens één keer kop?",
        opties=["zeven", "acht", "zes", "drie"],
        antwoord=0,
        uitleg="Er zijn acht uitkomsten in totaal, en één daarvan heeft geen enkele keer kop. Acht min één is zeven.",
    ),
    dict(
        type="waarofniet",
        vraag="Minstens één is meestal makkelijker te tellen via het tegengestelde geval.",
        antwoord=True,
        uitleg="Het tegengestelde van minstens één is er geen enkele, en dat is bijna altijd één geval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een code van vier cijfers mag niet uit vier gelijke cijfers bestaan. Hoeveel codes blijven er over?",
        opties=["negenduizend negenhonderdnegentig", "negenduizend", "negenduizend negenhonderd", "negenhonderdnegentig"],
        antwoord=0,
        uitleg="Tienduizend codes in totaal, waarvan er tien uit vier gelijke cijfers bestaan. Tienduizend min tien.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verzameling van alles wat niet aan de voorwaarde voldoet? Eén woord.",
        antwoord=["complement", "het complement"],
        uitleg="Het complement en de groep zelf vormen samen het totaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit twee dobbelstenen. Hoeveel worpen geven minstens één zes?",
        opties=["elf", "twaalf", "zes", "zesendertig"],
        antwoord=0,
        uitleg="Zesendertig worpen in totaal, vijfentwintig zonder zes. Zesendertig min vijfentwintig is elf.",
    ),
    dict(
        type="waarofniet",
        vraag="Het complement van hoogstens twee is minstens drie.",
        antwoord=True,
        uitleg="Hoogstens twee betekent nul, één of twee. Alles daarbuiten is drie of meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de complementregel bij minstens-vragen zo nuttig?",
        opties=[
            "omdat het tegengestelde geval vaak uit veel minder mogelijkheden bestaat",
            "omdat je bij minstens-vragen nooit met de productregel mag werken",
            "omdat je daarmee de volgorde van de keuzes niet hoeft te bekijken",
            "omdat het antwoord daardoor altijd een rond getal wordt",
        ],
        antwoord=0,
        uitleg="Minstens één keer kop in tien worpen uitrekenen is zwaar; geen enkele keer kop is één geval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas van vijfentwintig leerlingen: achttien hebben een fiets, zeven niet. Hoeveel hebben er een fiets, met de complementregel?",
        opties=[
            "vijfentwintig min zeven, dus achttien",
            "achttien plus zeven, dus vijfentwintig",
            "vijfentwintig min achttien, dus zeven",
            "achttien min zeven, dus elf",
        ],
        antwoord=0,
        uitleg="Het complement van wie een fiets heeft is wie er geen heeft, en samen vormen ze de klas.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel uitkomsten heeft het vier keer gooien van een munt? Schrijf het getal.",
        antwoord=["16", "zestien"],
        uitleg="Twee tot de vierde is zestien: voor elke worp twee mogelijkheden.",
    ),
    dict(
        type="waarofniet",
        vraag="De complementregel werkt alleen als je het totale aantal mogelijkheden kent.",
        antwoord=True,
        uitleg="Zonder het totaal kan je er niets van aftrekken. Dat totaal bereken je meestal met de productregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toets heeft tien waar-of-niet-waarvragen. Hoeveel manieren zijn er om ze allemaal in te vullen?",
        opties=["duizend vierentwintig", "twintig", "honderd", "vijfhonderdtwaalf"],
        antwoord=0,
        uitleg="Twee tot de tiende is duizend vierentwintig. Elke vraag heeft twee mogelijkheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel van die duizend vierentwintig invullingen hebben minstens één fout, als er één juiste sleutel is?",
        opties=["duizend drieëntwintig", "duizend vierentwintig", "duizend", "vijfhonderdtwaalf"],
        antwoord=0,
        uitleg="Precies één invulling is helemaal juist. Alle andere hebben minstens één fout.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag de complementregel alleen gebruiken als het woordje niet in de opgave staat.",
        antwoord=False,
        uitleg="Het is de vraagstelling die telt, niet het woord. Minstens één, hoogstens twee en op zijn vroegst vragen alle drie om het complement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietspad loopt via drie wegen naar het park en van daar via vier wegen naar school. Hoeveel routes?",
        opties=["twaalf", "zeven", "vier", "drie"],
        antwoord=0,
        uitleg="Drie maal vier is twaalf: eerst het ene stuk kiezen, dan het andere.",
    ),
    dict(
        type="invultekst",
        vraag="Een school biedt zes keuzevakken aan en je kiest er één. Hoeveel keuzes? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg="Eén keuze uit zes mogelijkheden is gewoon zes. Niet elke opgave vraagt een berekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mag twee van de drie regels combineren in één opgave. Hoe pak je dat aan?",
        opties=[
            "je splitst de opgave in stukken en kijkt per stuk of het en, of, of niet is",
            "je kiest de regel die het grootste antwoord geeft, want dat is het totaal",
            "je gebruikt altijd eerst de somregel en daarna pas de productregel",
            "je rekent met alle drie de regels en neemt daarna het gemiddelde",
        ],
        antwoord=0,
        uitleg="Opsplitsen in deelproblemen is een van de heuristieken die de fiche noemt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal mogelijkheden kan na toepassing van de complementregel groter worden.",
        antwoord=False,
        uitleg="Je trekt iets af van het totaal, dus het antwoord is altijd kleiner dan of gelijk aan het totaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een getal van drie cijfers mag niet met nul beginnen. Hoeveel zulke getallen bestaan er?",
        opties=["negenhonderd", "duizend", "zevenhonderdtwintig", "negenhonderdnegentig"],
        antwoord=0,
        uitleg="Negen keuzes voor het eerste cijfer, tien voor de twee andere: negen maal honderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vijftig mensen: dertig fietsen, vijfentwintig nemen de bus, tien doen allebei. Hoeveel doen geen van beide?",
        opties=["vijf", "vijftien", "tien", "twintig"],
        antwoord=0,
        uitleg="Dertig plus vijfentwintig min tien is vijfenveertig die minstens één van beide doen. Vijftig min vijfenveertig is vijf.",
    ),
]

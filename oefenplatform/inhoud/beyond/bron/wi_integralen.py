# -*- coding: utf-8 -*-
"""De bepaalde integraal en haar toepassingen.

Het tweede stuk van het onderdeel "Analyse: integralen" van fiche G2. De fiche
bouwt de bepaalde integraal op twee manieren op: als limiet van onder-, boven-
en Riemannsommen, en als georiënteerde oppervlakte. De hoofdstelling van de
integraalrekening verbindt die met de primitieven van het vorige thema.

Deel 1 is de bepaalde integraal zelf, met de sommen en de hoofdstelling.
Deel 2 zijn de toepassingen: oppervlakte tussen krommen, omwentelingslichamen,
booglengte en de contexten die de fiche noemt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een Riemannsom?",
        opties=[
            "de som van de oppervlakten van rechthoekjes onder een grafiek",
            "de som van alle functiewaarden op een gegeven interval",
            "het verschil tussen de hoogste en de laagste functiewaarde",
            "de som van de twee integratiegrenzen van de integraal",
        ],
        antwoord=0,
        uitleg="Je verdeelt het interval in smalle stukjes en benadert elk stukje door een rechthoekje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verhouden een ondersom, de werkelijke oppervlakte en een bovensom zich?",
        opties=[
            "de ondersom is het kleinst en de bovensom het grootst",
            "de bovensom is het kleinst en de ondersom het grootst",
            "ze zijn alle drie even groot bij elke verdeling",
            "de werkelijke oppervlakte ligt buiten die twee sommen",
        ],
        antwoord=0,
        uitleg="De ondersom gebruikt in elk stukje de laagste functiewaarde, de bovensom de hoogste. De echte oppervlakte ligt er tussenin.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot drie van het getal twee? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg="Dat is een rechthoek met breedte drie en hoogte twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer deelintervallen je gebruikt, hoe beter de benadering van de oppervlakte.",
        antwoord=True,
        uitleg="De rechthoekjes volgen de kromme dan nauwer. In de limiet vallen onder- en bovensom samen, en dat is net de integraal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de georiënteerde oppervlakte?",
        opties=[
            "een oppervlakte die onder de x-as negatief meetelt",
            "een oppervlakte die je altijd positief laat meetellen",
            "de oppervlakte tussen twee krommen onderling",
            "de oppervlakte van het grootste rechthoekje",
        ],
        antwoord=0,
        uitleg="Dat is wat de bepaalde integraal rechtstreeks berekent. Voor de werkelijke oppervlakte moet je de negatieve stukken apart nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een functie ligt op het hele interval onder de x-as. Wat weet je over haar bepaalde integraal daar?",
        opties=[
            "ze is negatief",
            "ze is positief",
            "ze is gelijk aan nul",
            "ze bestaat niet",
        ],
        antwoord=0,
        uitleg="De functiewaarden zijn negatief, dus ook de som van de rechthoekjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bepaalde integraal is altijd een positief getal.",
        antwoord=False,
        uitleg="Ze is georiënteerd: onder de as telt ze negatief, en ze kan zelfs nul worden als de stukken elkaar opheffen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van twee tot twee van om het even welke functie? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Onder- en bovengrens vallen samen, dus er is geen breedte en geen oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het gevolg van de hoofdstelling van de integraalrekening?",
        opties=[
            "de integraal van a tot b is de primitieve in b min de primitieve in a",
            "de integraal van a tot b is de functiewaarde in b min die in a",
            "de integraal van a tot b is de afgeleide in b min de afgeleide in a",
            "de integraal van a tot b is het gemiddelde van a en b",
        ],
        antwoord=0,
        uitleg="Daarmee hoef je geen rechthoekjes meer te tellen: een primitieve zoeken volstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je de twee grenzen van een bepaalde integraal verwisselt, wisselt het resultaat van teken.",
        antwoord=True,
        uitleg="In de hoofdstelling draai je dan de aftrekking om, en dat geeft het tegengestelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee komt de dx in een integraal overeen bij de Riemannsommen?",
        opties=[
            "met de breedte van de rechthoekjes",
            "met de hoogte van de rechthoekjes",
            "met het aantal rechthoekjes dat je neemt",
            "met de oppervlakte van één rechthoekje",
        ],
        antwoord=0,
        uitleg="De functiewaarde is de hoogte, de dx de breedte, en samen vormen ze de oppervlakte van één reepje.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot twee van drie x kwadraat? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg="De primitieve is x tot de derde. Acht min nul is acht.",
    ),
    dict(
        type="meerkeuze",
        vraag="De grafiek snijdt de x-as midden in het interval. Hoe bereken je dan de werkelijke oppervlakte?",
        opties=[
            "in de nulwaarde splitsen en de stukken positief optellen",
            "gewoon één integraal over het hele interval berekenen",
            "de integraal berekenen en daarna door twee delen",
            "alleen het stuk boven de x-as in rekening brengen",
        ],
        antwoord=0,
        uitleg="Anders heffen een positief en een negatief stuk elkaar op en krijg je een te kleine of zelfs een nul-uitkomst.",
    ),
    dict(
        type="waarofniet",
        vraag="De hoofdstelling van de integraalrekening geldt voor elke functie, ook voor functies met een sprong.",
        antwoord=False,
        uitleg="Ze geldt voor continue functies. Bij een sprong moet je het interval eerst opsplitsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de middelwaardestelling van de integraalrekening?",
        opties=[
            "er is een punt waar de functiewaarde gelijk is aan de gemiddelde waarde",
            "er is een punt waar de afgeleide gelijk is aan nul op dat interval",
            "de integraal is altijd gelijk aan het gemiddelde van de grenzen",
            "de oppervlakte is gelijk aan de hoogte in het midden van het interval",
        ],
        antwoord=0,
        uitleg="Er bestaat dus een rechthoek met dezelfde breedte en dezelfde oppervlakte als het gebied onder de kromme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de bovengrens van een bepaalde integraal voor?",
        opties=[
            "de rechterkant van het interval waarover je integreert",
            "de grootste functiewaarde op dat hele interval",
            "de hoogte van de hoogste rechthoek in de bovensom",
            "de bovenste van de twee krommen die je vergelijkt",
        ],
        antwoord=0,
        uitleg="De grenzen staan op de x-as, niet op de y-as. Dat verwarren leidt tot heel vreemde uitkomsten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ondersom is nooit groter dan de werkelijke oppervlakte.",
        antwoord=True,
        uitleg="Ze gebruikt in elk stukje de laagste functiewaarde, dus ze laat telkens een randje liggen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van één tot twee van één gedeeld door x kwadraat? Schrijf het antwoord als breuk.",
        antwoord=["1/2"],
        uitleg="De primitieve is min één gedeeld door x. Min een half min min één geeft een half.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom levert de limiet van Riemannsommen een exacte oppervlakte op?",
        opties=[
            "omdat onder- en bovensom naar hetzelfde getal kruipen",
            "omdat de rechthoekjes op den duur helemaal verdwijnen",
            "omdat je altijd de middelste functiewaarde neemt",
            "omdat de fout bij elke stap precies gehalveerd wordt",
        ],
        antwoord=0,
        uitleg="De werkelijke oppervlakte ligt er altijd tussen. Als de twee sommen samenvallen, is er maar één mogelijk getal over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noteer je kort dat je een primitieve in beide grenzen invult en aftrekt?",
        opties=[
            "met een rechte streep achter de primitieve en de grenzen erbij",
            "met een plusteken tussen de twee ingevulde waarden in",
            "met twee integraaltekens vlak naast elkaar geschreven",
            "met een absolutewaardeteken rond de hele primitieve functie",
        ],
        antwoord=0,
        uitleg="Die notatie houdt het rekenwerk overzichtelijk: eerst de primitieve, dan pas invullen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de oppervlakte tussen twee krommen?",
        opties=[
            "de integraal van de bovenste functie min de onderste",
            "de integraal van de ene plus de integraal van de andere",
            "het verschil van de twee oppervlakten, altijd positief gemaakt",
            "de integraal van het product van de twee functies",
        ],
        antwoord=0,
        uitleg="Het hoogteverschil tussen de twee krommen is de hoogte van elk reepje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grenzen gebruik je meestal bij de oppervlakte tussen twee krommen?",
        opties=[
            "de x-waarden van hun snijpunten",
            "de y-waarden van hun snijpunten",
            "de nulwaarden van de bovenste functie",
            "nul en de grootste functiewaarde",
        ],
        antwoord=0,
        uitleg="Daar sluit het gebied zich. Je vindt ze door de twee voorschriften aan elkaar gelijk te stellen.",
    ),
    dict(
        type="invultekst",
        vraag="Bij een omwentelingslichaam om de x-as neem je pi maal de integraal van f tot de hoeveelste macht? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Elke dunne schijf is een cirkel met straal f van x, en de oppervlakte van een cirkel is pi maal de straal in het kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de inhoud van een omwentelingslichaam kwadrateer je de functie onder het integraalteken.",
        antwoord=True,
        uitleg="De functiewaarde is de straal van de schijf, en in de oppervlakte van een cirkel staat die straal in het kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er onder de wortel in de formule voor de booglengte van een kromme?",
        opties=[
            "één plus de afgeleide in het kwadraat",
            "één plus de functie in het kwadraat",
            "de functie plus haar afgeleide, in het kwadraat",
            "één min de afgeleide in het kwadraat",
        ],
        antwoord=0,
        uitleg="Ze volgt uit Pythagoras op een heel klein stukje kromme: een horizontale dx en een verticale dy.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je integreert de snelheid van een wagen over een tijdsinterval. Wat krijg je?",
        opties=[
            "de verplaatsing in die tijd",
            "de versnelling in die tijd",
            "de gemiddelde snelheid in die tijd",
            "de maximale snelheid in die tijd",
        ],
        antwoord=0,
        uitleg="Snelheid maal tijd is afstand, en de integraal telt al die kleine stukjes op.",
    ),
    dict(
        type="waarofniet",
        vraag="De integraal van de snelheid geeft altijd de werkelijk afgelegde weg.",
        antwoord=False,
        uitleg="Rijdt de wagen een stuk achteruit, dan is de snelheid negatief en trekt de integraal dat af. Dan krijg je de verplaatsing, niet de afgelegde weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de oppervlakte onder de rechte y is twee, tussen nul en vijf? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg="Een rechthoek van vijf breed en twee hoog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je integreert het debiet van een kraan over de tijd. Wat krijg je?",
        opties=[
            "de totale hoeveelheid water",
            "de snelheid van het water",
            "de druk in de waterleiding",
            "de gemiddelde doorstroming",
        ],
        antwoord=0,
        uitleg="Debiet is liter per seconde. Maal de tijd en opgeteld geeft dat liters.",
    ),
    dict(
        type="waarofniet",
        vraag="De integraal van de marginale kost over een aantal stuks geeft de toename van de totale kost.",
        antwoord=True,
        uitleg="De marginale kost is de afgeleide van de totale kost, dus integreren brengt je terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de oppervlakte tussen y is x en y is x kwadraat, tussen hun twee snijpunten?",
        opties=[
            "een zesde",
            "een derde",
            "een half",
            "een twaalfde",
        ],
        antwoord=0,
        uitleg="De snijpunten liggen in nul en één, en op dat stuk ligt de rechte boven de parabool.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot één van x min x kwadraat? Schrijf het antwoord als breuk.",
        antwoord=["1/6"],
        uitleg="Een half min een derde is een zesde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer mag je op het examen ICT gebruiken bij een integraal?",
        opties=[
            "als de opgave dat met het icoon aangeeft, en ook dan toon je je werkwijze",
            "altijd, want het online rekentoestel staat de hele tijd ter beschikking",
            "nooit, want een integraal moet je altijd exact berekenen",
            "enkel bij een onbepaalde integraal, niet bij een bepaalde",
        ],
        antwoord=0,
        uitleg="Functioneel gebruik betekent: ICT ondersteunt het rekenwerk, maar je redenering en je tussenstappen schrijf je uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De inhoud van een omwentelingslichaam hangt af van de as waarrond je de kromme laat draaien.",
        antwoord=True,
        uitleg="Dezelfde kromme rond de x-as of rond de y-as geeft een heel ander lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je integreert een snelheid in meter per seconde over seconden. Welke eenheid heeft het resultaat?",
        opties=[
            "meter",
            "meter per seconde",
            "meter per seconde in het kwadraat",
            "seconde",
        ],
        antwoord=0,
        uitleg="De eenheden vermenigvuldigen mee: meter per seconde maal seconde geeft meter. Die controle vangt veel fouten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je integreert de versnelling over de tijd. Wat krijg je?",
        opties=[
            "de verandering van de snelheid",
            "de afgelegde weg in die tijd",
            "de gemiddelde versnelling",
            "de kracht op het voorwerp",
        ],
        antwoord=0,
        uitleg="Versnelling is de afgeleide van de snelheid, dus integreren brengt je één stap terug.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkelijke oppervlakte kan negatief zijn.",
        antwoord=False,
        uitleg="Een oppervlakte is nooit negatief. Alleen de georiënteerde oppervlakte, dus de integraal zelf, kan dat wel zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Twee grafieken lopen evenwijdig, de ene ligt overal drie hoger. Hoe groot is de oppervlakte ertussen over een interval van lengte vier? Schrijf het getal.",
        antwoord=["12", "twaalf"],
        uitleg="Het hoogteverschil is overal drie, dus het gebied is een rechthoek van vier op drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krommen kruisen elkaar midden in het interval. Wat doe je?",
        opties=[
            "splitsen in het snijpunt, want daar wisselen boven en onder van rol",
            "gewoon doorrekenen, want de integraal houdt daar zelf rekening mee",
            "de hele oppervlakte berekenen en daarna verdubbelen",
            "alleen het grootste van de twee stukken berekenen",
        ],
        antwoord=0,
        uitleg="Na het snijpunt is de andere kromme de bovenste, dus het verschil wisselt van teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je bij zo'n opgave eerst een schets?",
        opties=[
            "om te zien welke kromme boven ligt en waar ze elkaar snijden",
            "omdat de schets zelf als het antwoord geldt op het examen",
            "omdat je de oppervlakte van de schets kan aflezen",
            "omdat je anders geen primitieve kan berekenen",
        ],
        antwoord=0,
        uitleg="Zonder schets zet je de twee functies gemakkelijk in de verkeerde volgorde en krijg je een negatieve oppervlakte.",
    ),
]

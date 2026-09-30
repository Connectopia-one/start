# -*- coding: utf-8 -*-
"""De vragen voor "Rechten, vlakken en gelijkvormigheid".

Uit de bouwsteen Meetkunde en metend rekenen: de onderlinge ligging van rechten
en vlakken in de ruimte, het onderscheid tussen ruimtefiguren en vlakke
figuren, de tweedimensionale voorstelling van een driedimensionale figuur
(natuurlijk perspectief, cavalièreperspectief, de drie aanzichten en de
ontwikkeling), de verzamelingenbegrippen element, deelverzameling, doorsnede,
unie en verschil, en daarnaast de gelijkvormigheid: de gelijkvormigheidsfactor,
de schaal als verhouding, het effect van schaalverandering op lengte,
oppervlakte en volume, en de gelijkvormigheidskenmerken van driehoeken.

Deel 1 is de ruimte. Deel 2 is de gelijkvormigheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Twee rechten in de ruimte snijden elkaar niet en liggen niet in hetzelfde vlak. Hoe noem je ze?",
        opties=["kruisend", "evenwijdig", "samenvallend", "loodrecht"],
        antwoord=0,
        uitleg="Kruisende rechten bestaan alleen in de ruimte. In het vlak zijn twee rechten die elkaar niet snijden altijd evenwijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderlinge ligging bestaat wél voor twee rechten in de ruimte, maar niet voor twee rechten in één vlak?",
        opties=["kruisend", "snijdend", "evenwijdig", "samenvallend"],
        antwoord=0,
        uitleg="Wie in het vlak werkt, heeft aan evenwijdig, snijdend en samenvallend genoeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vlakken die elkaar niet snijden en niet samenvallen, zijn ...",
        opties=["evenwijdig", "kruisend", "loodrecht", "snijdend in één punt"],
        antwoord=0,
        uitleg="Twee vlakken kunnen niet kruisen: ze snijden elkaar in een rechte, vallen samen of zijn evenwijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van twee snijdende vlakken?",
        opties=["een rechte", "een punt", "een vlak", "een lijnstuk met twee eindpunten"],
        antwoord=0,
        uitleg="Twee muren van een kamer snijden elkaar in de hoeklijn, en die loopt van boven naar beneden door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ligging is mogelijk tussen een rechte en een vlak?",
        opties=[
            "de rechte ligt in het vlak, is er evenwijdig mee, snijdt het of staat er loodrecht op",
            "de rechte kruist het vlak, of valt ermee samen in twee punten",
            "de rechte snijdt het vlak altijd, behalve als ze even lang zijn",
            "de rechte staat altijd loodrecht op het vlak of valt ermee samen",
        ],
        antwoord=0,
        uitleg="Die vier mogelijkheden staan zo in de vakfiche opgesomd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke figuur is een ruimtefiguur en geen vlakke figuur?",
        opties=["een kegel", "een ruit", "een trapezium", "een regelmatige zeshoek"],
        antwoord=0,
        uitleg="Een kegel heeft een inhoud. De andere drie liggen plat en hebben enkel een oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ontwikkeling van een ruimtefiguur?",
        opties=[
            "het platte patroon dat je krijgt als je de figuur openvouwt",
            "de tekening van de figuur in cavalièreperspectief",
            "de schaduw die de figuur op een vlak werpt",
            "de doorsnede van de figuur met een horizontaal vlak",
        ],
        antwoord=0,
        uitleg="De ontwikkeling van een kubus bestaat uit zes vierkanten die je weer tot een kubus kan vouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie aanzichten noemt de vakfiche bij de projecties op drie vlakken?",
        opties=[
            "zijaanzicht, vooraanzicht en bovenaanzicht",
            "zijaanzicht, achteraanzicht en onderaanzicht",
            "vooraanzicht, bovenaanzicht en doorsnede",
            "perspectief, projectie en ontwikkeling",
        ],
        antwoord=0,
        uitleg="Met die drie aanzichten samen ligt de vorm van een figuur meestal vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het cavalièreperspectief?",
        opties=[
            "de zijvlakken lopen schuin weg, maar evenwijdige lijnen blijven evenwijdig",
            "alle lijnen lopen naar één verdwijnpunt aan de horizon",
            "de figuur wordt getekend zoals een fototoestel ze ziet",
            "er wordt enkel met stippellijnen gewerkt, zonder volle lijnen",
        ],
        antwoord=0,
        uitleg="Bij natuurlijk perspectief lopen de lijnen wél naar een verdwijnpunt, waardoor verre dingen kleiner lijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van de verzamelingen A en B?",
        opties=[
            "alle elementen die in A én in B zitten",
            "alle elementen die in A of in B zitten, of in allebei",
            "alle elementen van A die niet in B zitten",
            "alle elementen die in geen van beide zitten",
        ],
        antwoord=0,
        uitleg="De unie neemt alles samen, de doorsnede houdt enkel het gemeenschappelijke over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'A is een deelverzameling van B'?",
        opties=[
            "elk element van A zit ook in B",
            "A en B hebben minstens één element gemeen",
            "A en B hebben evenveel elementen",
            "A en B hebben geen enkel element gemeen",
        ],
        antwoord=0,
        uitleg="De natuurlijke getallen zijn een deelverzameling van de gehele getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil A zonder B?",
        opties=[
            "alle elementen van A die niet in B zitten",
            "alle elementen die in A of in B zitten",
            "alle elementen die in allebei zitten",
            "alle elementen van B die niet in A zitten",
        ],
        antwoord=0,
        uitleg="Het verschil is niet omkeerbaar: A zonder B is iets anders dan B zonder A.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel ribben heeft een balk?",
        opties=["twaalf", "acht", "zes", "vier"],
        antwoord=0,
        uitleg="Een balk heeft 8 hoekpunten, 12 ribben en 6 zijvlakken.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee kruisende rechten liggen nooit in hetzelfde vlak.",
        antwoord=True,
        uitleg="Zodra ze in één vlak liggen, snijden ze elkaar of zijn ze evenwijdig.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee vlakken kunnen elkaar in één punt snijden.",
        antwoord=False,
        uitleg="De doorsnede van twee snijdende vlakken is altijd een rechte.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij cavalièreperspectief blijven evenwijdige ribben evenwijdig getekend.",
        antwoord=True,
        uitleg="Dat is precies het verschil met natuurlijk perspectief, waar ze naar een verdwijnpunt lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="De unie van twee verzamelingen bevat alleen de elementen die ze gemeen hebben.",
        antwoord=False,
        uitleg="Dat is de doorsnede. De unie neemt alles van allebei samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je twee rechten in de ruimte die elkaar niet snijden en niet in één vlak liggen?",
        antwoord=["kruisend", "kruisende rechten"],
        uitleg="Denk aan een spoorlijn en een brug erboven die er schuin overheen loopt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel zijvlakken heeft een balk?",
        antwoord=["6", "zes"],
        uitleg="Telkens twee tegenover elkaar: boven en onder, links en rechts, voor en achter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het platte patroon dat je krijgt door een kubus open te vouwen?",
        antwoord=["ontwikkeling", "de ontwikkeling", "uitslag"],
        uitleg="Er bestaan elf verschillende ontwikkelingen van een kubus.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Twee figuren zijn gelijkvormig met factor 3. Wat gebeurt er met de lengtes?",
        opties=[
            "ze worden drie keer zo groot",
            "ze worden negen keer zo groot",
            "ze worden zevenentwintig keer zo groot",
            "ze blijven gelijk, alleen de vorm verandert",
        ],
        antwoord=0,
        uitleg="De gelijkvormigheidsfactor werkt rechtstreeks op de lengtes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee figuren zijn gelijkvormig met factor 3. Wat gebeurt er met de oppervlakte?",
        opties=[
            "ze wordt negen keer zo groot",
            "ze wordt drie keer zo groot",
            "ze wordt zes keer zo groot",
            "ze wordt zevenentwintig keer zo groot",
        ],
        antwoord=0,
        uitleg="Oppervlakte is lengte maal lengte, dus de factor werkt twee keer: 3 maal 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee lichamen zijn gelijkvormig met factor 2. Wat gebeurt er met het volume?",
        opties=[
            "het wordt acht keer zo groot",
            "het wordt twee keer zo groot",
            "het wordt vier keer zo groot",
            "het wordt zestien keer zo groot",
        ],
        antwoord=0,
        uitleg="Volume is lengte maal lengte maal lengte: 2 tot de derde is 8.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een maquette is op schaal 1 op 50. Een muur van 12 centimeter op de maquette is in het echt ...",
        opties=["6 meter", "60 centimeter", "60 meter", "1,2 meter"],
        antwoord=0,
        uitleg="12 maal 50 is 600 centimeter, dus 6 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een kaart met schaal 1 op 25 000 meet een weg 8 centimeter. Hoe lang is die weg in het echt?",
        opties=["2 kilometer", "200 meter", "20 kilometer", "25 kilometer"],
        antwoord=0,
        uitleg="8 maal 25 000 is 200 000 centimeter, dus 2000 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee driehoeken hebben twee gelijke hoeken. Wat besluit je?",
        opties=[
            "ze zijn gelijkvormig, want de derde hoek is dan ook gelijk",
            "ze zijn gelijk, want twee gelijke hoeken leggen de vorm en de grootte vast",
            "je kan niets besluiten zonder één gegeven zijde",
            "ze zijn alleen gelijkvormig als de derde hoek recht is",
        ],
        antwoord=0,
        uitleg="Dat is het kenmerk HH. Omdat de hoeken samen 180 graden geven, ligt de derde vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gelijkvormigheidskenmerk gebruik je bij twee driehoeken waarvan alle drie de zijdeverhoudingen gelijk zijn?",
        opties=["ZZZ", "ZHZ", "HH", "ZZR met een rechte hoek"],
        antwoord=0,
        uitleg="Drie evenredige zijden volstaan om gelijkvormigheid te besluiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het kenmerk ZHZ?",
        opties=[
            "twee zijden evenredig en de ingesloten hoek gelijk",
            "twee zijden evenredig en een willekeurige hoek gelijk",
            "twee hoeken gelijk en een zijde evenredig",
            "drie hoeken gelijk en één zijde gegeven",
        ],
        antwoord=0,
        uitleg="De hoek moet tussen die twee zijden liggen. Ligt hij ernaast, dan ligt de vorm niet vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een foto van 10 op 15 centimeter wordt vergroot tot 20 op 30 centimeter. Hoeveel keer groter is de oppervlakte?",
        opties=["vier keer", "twee keer", "zes keer", "acht keer"],
        antwoord=0,
        uitleg="De lengtefactor is 2, dus de oppervlaktefactor is 2 maal 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bol krijgt een dubbel zo grote straal. Hoeveel keer meer verf heb je nodig om hem te schilderen?",
        opties=["vier keer zoveel", "twee keer zoveel", "acht keer zoveel", "evenveel"],
        antwoord=0,
        uitleg="Verf gaat over oppervlakte, en die gaat met het kwadraat van de factor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reus zou drie keer zo groot zijn als een mens. Waarom zou dat mislopen?",
        opties=[
            "zijn gewicht wordt 27 keer groter, maar zijn botdoorsnede maar 9 keer",
            "zijn gewicht wordt 9 keer groter, maar zijn botdoorsnede 27 keer",
            "zijn gewicht en zijn botten groeien allebei 3 keer, dus er is geen probleem",
            "zijn gewicht wordt 3 keer groter en zijn botten 3 keer sterker",
        ],
        antwoord=0,
        uitleg="Volume groeit met de derde macht, doorsnede met de tweede. Daarom hebben olifanten veel dikkere poten dan muizen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft zijden 3, 4 en 5. Een gelijkvormige driehoek heeft als kleinste zijde 9. Hoe lang is zijn langste zijde?",
        opties=["15", "12", "20", "45"],
        antwoord=0,
        uitleg="De factor is 3, dus 5 maal 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn twee gelijkvormige figuren niet noodzakelijk even groot?",
        opties=[
            "omdat gelijkvormig enkel over de vorm gaat, niet over de afmetingen",
            "omdat gelijkvormige figuren altijd verschillende hoeken hebben",
            "omdat de factor altijd groter dan één moet zijn",
            "omdat gelijkvormig hetzelfde betekent als gelijk",
        ],
        antwoord=0,
        uitleg="Zijn ze bovendien even groot, dan is de factor 1 en heten ze gelijk of congruent.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gelijkvormigheidsfactor 4 wordt de oppervlakte zestien keer zo groot.",
        antwoord=True,
        uitleg="4 maal 4 is 16.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je alle zijden van een kubus verdubbelt, verdubbelt de inhoud.",
        antwoord=False,
        uitleg="De inhoud wordt acht keer zo groot: 2 tot de derde macht.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee driehoeken met dezelfde drie hoeken zijn altijd gelijkvormig.",
        antwoord=True,
        uitleg="Zelfs twee gelijke hoeken volstaan al, want de derde volgt vanzelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schaal van 1 op 100 betekent dat de tekening honderd keer groter is dan het voorwerp.",
        antwoord=False,
        uitleg="Het omgekeerde: het voorwerp is honderd keer groter dan de tekening.",
    ),
    dict(
        type="invultekst",
        vraag="Bij gelijkvormigheidsfactor 5, hoeveel keer zo groot wordt de oppervlakte?",
        antwoord=["25", "25 keer"],
        uitleg="De factor werkt twee keer bij een oppervlakte.",
    ),
    dict(
        type="invultekst",
        vraag="Bij gelijkvormigheidsfactor 3, hoeveel keer zo groot wordt het volume?",
        antwoord=["27", "27 keer"],
        uitleg="3 maal 3 maal 3.",
    ),
    dict(
        type="invultekst",
        vraag="Op schaal 1 op 200 is een gevel 7 centimeter. Hoeveel meter is dat in het echt?",
        antwoord=["14", "14 meter", "14 m"],
        uitleg="7 maal 200 is 1400 centimeter.",
    ),
]

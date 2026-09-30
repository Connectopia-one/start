# -*- coding: utf-8 -*-
"""De vragen voor "Tekenverloop, verloopschema en grafisch oplossen".

Nieuw geschreven voor dubbele finaliteit. Het overgenomen thema "Formules
omvormen en eerstegraadsvergelijkingen" raakt in zijn tweede deel al even aan
het grafisch oplossen van één vergelijking of ongelijkheid. De DF-fiche gaat
duidelijk verder en vraagt twee dingen die in het doorstroommateriaal nergens
staan: een tekenverloop en een verloopschema opstellen aan de hand van de
grafiek, en het verband tussen twee functies f en g — hun gemeenschappelijke
punten en hun onderlinge ligging. De oplossingenverzameling geef je als een
interval en stel je voor op een getallenas.

Deel 1 gaat over het teken en het verloop van één functie, deel 2 over twee
functies naast elkaar.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat toont een tekenverloop van een functie?",
        opties=[
            "waar de functiewaarde positief of negatief is",
            "waar de functie stijgt en waar ze weer daalt",
            "hoe groot de functiewaarden zijn",
            "waar de grafiek de y-as snijdt",
        ],
        antwoord=0,
        uitleg="Een tekenverloop gaat enkel over het teken: plus of min. Hoe groot de waarde is, staat er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont een verloopschema van een functie?",
        opties=[
            "waar de functie stijgt en waar ze daalt",
            "waar de functiewaarde positief is en waar ze negatief is",
            "hoeveel nulwaarden de functie heeft",
            "welke getallen tot het domein behoren",
        ],
        antwoord=0,
        uitleg="Een verloopschema gaat over de richting van de grafiek. Een tekenverloop gaat over de ligging ten opzichte van de x-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je in een tekenverloop precies onder de nulwaarde?",
        opties=[
            "een nul",
            "een plusteken",
            "een minteken",
            "een pijl naar boven",
        ],
        antwoord=0,
        uitleg="In de nulwaarde is de functiewaarde precies nul, dus daar staat geen plus en geen min.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke x is de functie f(x) = 2x − 6 negatief?",
        opties=["voor x kleiner dan 3", "voor x groter dan 3", "voor x kleiner dan 6", "voor geen enkele x"],
        antwoord=0,
        uitleg="De rechte stijgt en snijdt de x-as in 3, dus links van 3 ligt ze eronder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke x is de functie f(x) = −x + 4 positief?",
        opties=["voor x kleiner dan 4", "voor x groter dan 4", "voor x kleiner dan −4", "voor elke x"],
        antwoord=0,
        uitleg="Deze rechte daalt en snijdt de x-as in 4, dus links van 4 ligt ze erboven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het verloopschema van een rechte met een positieve richtingscoëfficiënt eruit?",
        opties=[
            "één pijl die over de hele getallenas omhoog wijst",
            "een pijl omhoog en daarna een pijl omlaag",
            "een pijl omlaag over de hele getallenas",
            "afwisselend een plus- en een minteken",
        ],
        antwoord=0,
        uitleg="Een rechte verandert nergens van richting: ze stijgt overal of ze daalt overal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is stijgen iets anders dan positief zijn?",
        opties=[
            "stijgen gaat over de richting, positief over de ligging",
            "stijgen gaat over de y-as, positief zijn over de x-as",
            "stijgen kan enkel bij rechten, positief zijn bij elke functie",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Een stijgende rechte begint vaak onder de x-as en is daar dus negatief terwijl ze al stijgt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stijgende grafiek heeft altijd een positieve functiewaarde.",
        antwoord=False,
        uitleg="Stijgen zegt hoe de grafiek loopt, niet waar ze ligt. Links van haar nulwaarde ligt ze onder de x-as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eerstegraadsfunctie waarvan de richtingscoëfficiënt niet nul is, heeft precies één nulwaarde.",
        antwoord=True,
        uitleg="Een schuine rechte snijdt de x-as in precies één punt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een constante functie zoals f(x) = 5 heeft een nulwaarde.",
        antwoord=False,
        uitleg="De grafiek is een horizontale rechte op hoogte 5 en raakt de x-as nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het tekenverloop van de functie f(x) = 5 eruit?",
        opties=[
            "overal een plusteken, zonder nulwaarde",
            "overal een minteken, zonder nulwaarde",
            "een plusteken links en een minteken rechts",
            "een nul in het midden en verder overal een plusteken",
        ],
        antwoord=0,
        uitleg="De hele grafiek ligt op hoogte 5, dus boven de x-as, en ze komt nergens op nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zet je de oplossing x groter dan 2 op een getallenas?",
        opties=[
            "een open bolletje op 2 en alles rechts ervan gearceerd",
            "een vol bolletje op 2 en alles rechts ervan gearceerd",
            "een open bolletje op 2 en alles links ervan gearceerd",
            "een vol bolletje op 2 en alles links ervan gearceerd",
        ],
        antwoord=0,
        uitleg="Een open bolletje betekent dat dat getal er net buiten valt. Bij groter dan of gelijk aan wordt het bolletje vol.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een getallenas duid je een grens die meetelt aan met een vol bolletje.",
        antwoord=True,
        uitleg="Vol bolletje betekent: dit getal hoort erbij. Het haakje van het interval sluit dan ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 'alle x groter dan 3' als interval?",
        opties=["]3, +∞[", "[3, +∞[", "]−∞, 3[", "[3, +∞]"],
        antwoord=0,
        uitleg="De 3 telt niet mee, dus daar staat het haakje open. Bij oneindig staat het haakje altijd open.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij f(x) ≥ 0 telt de nulwaarde zelf mee in de oplossing.",
        antwoord=True,
        uitleg="Het gelijkheidsteken staat erbij, dus het punt waar de grafiek de x-as raakt hoort erbij en het haakje sluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangt het antwoord bij een ongelijkheid af van of de rechte stijgt of daalt?",
        opties=[
            "omdat een stijgende rechte rechts van zijn nulwaarde positief is",
            "omdat een dalende rechte geen nulwaarde heeft",
            "omdat je bij een dalende rechte geen intervallen mag gebruiken",
            "omdat een stijgende rechte overal boven de x-as ligt",
        ],
        antwoord=0,
        uitleg="Teken altijd even de rechte. Dan zie je meteen aan welke kant van de nulwaarde ze boven de as ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het snijpunt met de y-as en de nulwaarde?",
        opties=[
            "het ene is f(0), het andere de x waarvoor f(x) nul is",
            "ze zijn altijd aan elkaar gelijk",
            "de nulwaarde is altijd nul",
            "het snijpunt met de y-as ligt altijd in de oorsprong",
        ],
        antwoord=0,
        uitleg="Bij het ene vul je nul in voor x, bij het andere stel je de functiewaarde gelijk aan nul. Dat zijn twee verschillende vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je van een grafiek af om een tekenverloop op te stellen?",
        opties=[
            "de nulwaarden, en aan welke kant de grafiek boven of onder de x-as ligt",
            "de hoogste en de laagste functiewaarde",
            "het snijpunt met de y-as en de richtingscoëfficiënt",
            "het domein en het bereik van de functie",
        ],
        antwoord=0,
        uitleg="De nulwaarden zijn de grenzen van het schema. Tussen twee grenzen houdt het teken zich gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het schema dat toont waar een functie positief en waar ze negatief is?",
        antwoord=["het tekenverloop", "tekenverloop"],
        uitleg="Het tekenverloop zet de nulwaarden als grenzen en daartussen een plus- of een minteken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het schema dat toont waar een functie stijgt en waar ze daalt?",
        antwoord=["het verloopschema", "verloopschema"],
        uitleg="Bij een rechte is dat één pijl, want een rechte verandert nergens van richting.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als je f(x) = g(x) oplost?",
        opties=[
            "je zoekt de gemeenschappelijke punten van de grafieken",
            "je zoekt waar allebei de grafieken de x-as snijden",
            "je zoekt het hoogste punt van beide grafieken",
            "je zoekt waar de twee grafieken evenwijdig lopen",
        ],
        antwoord=0,
        uitleg="In een gemeenschappelijk punt hebben de twee functies bij dezelfde x dezelfde functiewaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar snijden f(x) = x + 1 en g(x) = 3x − 5 elkaar?",
        opties=["in x = 3", "in x = 2", "in x = 4", "in x = 1"],
        antwoord=0,
        uitleg="x plus 1 is 3x min 5 geeft 6 is 2x, dus x is 3. De functiewaarde daar is 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent f(x) > g(x) op de grafiek?",
        opties=[
            "de grafiek van f ligt boven die van g",
            "de grafiek van f ligt onder die van g",
            "de grafiek van f stijgt sneller dan die van g",
            "de grafiek van f snijdt de x-as verder naar rechts",
        ],
        antwoord=0,
        uitleg="Voor elke x waar f een hogere waarde geeft, ligt haar grafiek hoger. Dat is de onderlinge ligging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je uit een grafiek af voor welke x geldt dat f(x) groter is dan g(x)?",
        opties=[
            "je kijkt aan welke kant van het snijpunt f hoger loopt",
            "je kijkt in welk stuk allebei de grafieken stijgen",
            "je kijkt waar de grafieken de y-as snijden",
            "je telt hoeveel snijpunten er met de x-as zijn",
        ],
        antwoord=0,
        uitleg="Het snijpunt is de grens. Aan de ene kant ligt f hoger, aan de andere kant g.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee grafieken kunnen elkaar snijden zonder dat een van beide de x-as snijdt.",
        antwoord=True,
        uitleg="Twee schuine rechten die allebei boven de x-as blijven in het getoonde stuk, snijden elkaar toch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossingenverzameling van f(x) ≤ g(x) als de twee grafieken elkaar snijden in x = 2 en f er links van lager ligt?",
        opties=["]−∞, 2]", "[2, +∞[", "]−∞, 2[", "]2, +∞["],
        antwoord=0,
        uitleg="Links van 2 ligt f lager, en in 2 zelf zijn ze gelijk. Het gelijkheidsteken maakt het haakje bij 2 dicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietsenwinkel heeft kosten K(x) = 300 + 20x en opbrengst O(x) = 50x. Vanaf hoeveel fietsen is er winst?",
        opties=["vanaf 11 fietsen", "vanaf 10 fietsen", "vanaf 6 fietsen", "vanaf 15 fietsen"],
        antwoord=0,
        uitleg="Bij 10 fietsen zijn kosten en opbrengst allebei 500 euro. Pas vanaf de elfde ligt de opbrengst erboven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waar kosten en opbrengst precies even groot zijn?",
        antwoord=["het break-evenpunt", "break-evenpunt", "het omslagpunt"],
        uitleg="Daar is de winst nul. Vanaf dat punt wordt ze positief.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een opgave van de vorm f(x) = g(x) hoort altijd precies één x-waarde.",
        antwoord=False,
        uitleg="Bij evenwijdige rechten is er geen enkele, en bij samenvallende rechten zijn er oneindig veel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek ligt tussen x = 1 en x = 4 onder de x-as en daarbuiten erboven. Voor welke x is f(x) kleiner dan nul?",
        opties=["]1, 4[", "[1, 4]", "]−∞, 1[", "]4, +∞["],
        antwoord=0,
        uitleg="Enkel tussen de twee nulwaarden ligt de grafiek eronder, en in 1 en 4 zelf is de functiewaarde precies nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je een snijpunt dat je van een grafiek hebt afgelezen liefst met een berekening?",
        opties=[
            "omdat je bij het aflezen makkelijk een half hokje verkeerd zit",
            "omdat een grafiek geen snijpunten mag tonen",
            "omdat een rekentoestel geen grafieken aanvaardt",
            "omdat een snijpunt altijd een geheel getal moet zijn",
        ],
        antwoord=0,
        uitleg="De grafiek geeft een goed beeld en een goede schatting. De berekening geeft het exacte getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mag een vraagstuk grafisch oplossen zonder de ongelijkheid zelf op te schrijven. Hoe pak je dat aan?",
        opties=[
            "je tekent de grafieken en leest af welke boven ligt",
            "je schat het antwoord en controleert het achteraf",
            "je berekent eerst de ongelijkheid en tekent dan pas",
            "je zoekt het antwoord in een tabel met vaste waarden",
        ],
        antwoord=0,
        uitleg="Elke situatie wordt een functie, en de vraag 'wanneer is dit voordeliger' wordt de vraag welke grafiek lager ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je best een hulpmiddel om de grafieken te tekenen?",
        opties=[
            "bij moeilijkere vraagstukken met lastige getallen",
            "altijd, ook bij een eenvoudige rechte",
            "nooit, een grafiek teken je altijd zelf",
            "enkel als er geen snijpunt is",
        ],
        antwoord=0,
        uitleg="Bij eenvoudige opgaven teken je zelf en lees je af. Bij lastiger getallen laat je de grafiek tekenen en lees je daar af.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee verschillende rechten kunnen elkaar in twee punten snijden.",
        antwoord=False,
        uitleg="Door twee punten gaat maar één rechte. Hebben twee rechten twee punten gemeen, dan vallen ze samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een snijpunt van twee grafieken in een woordprobleem?",
        opties=[
            "de situatie waarin de twee grootheden even groot zijn",
            "de situatie waarin een van de twee nul wordt",
            "het moment waarop de ene grootheid begint te stijgen",
            "het grootste verschil tussen de twee grootheden",
        ],
        antwoord=0,
        uitleg="Dat is bijvoorbeeld het moment waarop twee abonnementen evenveel kosten, of waarop kosten en opbrengst gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom helpt een grafiek bij een ongelijkheid?",
        opties=[
            "omdat je meteen ziet aan welke kant de oplossing ligt",
            "omdat je dan geen intervalnotatie meer nodig hebt",
            "omdat een grafiek exacter is dan rekenen",
            "omdat een ongelijkheid niet met rekenen op te lossen is",
        ],
        antwoord=0,
        uitleg="Wie enkel rekent, vergeet makkelijk het ongelijkheidsteken om te draaien. Op de grafiek zie je meteen of je antwoord kan kloppen.",
    ),
    dict(
        type="waarofniet",
        vraag="De oplossing van een ongelijkheid is meestal een heel stuk van de getallenas en niet één getal.",
        antwoord=True,
        uitleg="Daarom noteer je ze als een interval of arceer je ze op een getallenas.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het symbool ∞?",
        antwoord=["oneindig", "het oneindigteken"],
        uitleg="Bij oneindig staat het haakje van een interval altijd open, want oneindig is geen getal dat je kan bereiken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de punten die twee grafieken met elkaar gemeen hebben?",
        antwoord=["de snijpunten", "snijpunten", "gemeenschappelijke punten"],
        uitleg="De x-waarden van die punten zijn de oplossingen van f(x) is g(x).",
    ),
    dict(
        type="waarofniet",
        vraag="Als de grafiek van f overal boven die van g ligt, heeft f(x) = g(x) geen oplossing.",
        antwoord=True,
        uitleg="Ze hebben dan geen enkel punt gemeen, dus er is geen x waarvoor de twee functiewaarden gelijk zijn.",
    ),
]

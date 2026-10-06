# -*- coding: utf-8 -*-
"""De vragen voor "Nut, preferentie en de indifferentiecurve" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"het keuzegedrag van de consument": nut, preferentie en indifferentie, en het
voorstellen en analyseren van een indifferentiecurve en een indifferentiemap.
De budgetlijn en de optimale combinatie staan in [[ec_budget]].

Deel 1 gaat over nut: totaal nut en marginaal nut, de wet van het afnemende
grensnut, en wat preferentie en indifferentie betekenen.
Deel 2 gaat over de indifferentiecurve en de indifferentiemap: hun verloop,
hun helling, waarom ze elkaar nooit snijden, en hoe je eruit afleest wat een
consument verkiest.

Afspraak in dit thema: een curve wordt altijd in woorden beschreven, met de
goederen en de aantallen in de vraag zelf, zodat een vraag ook zonder tekening
te maken is.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is nut in de economie?",
        opties=[
            "De mate waarin een goed een behoefte voldoet",
            "De prijs die een consument voor een goed betaalt",
            "De winst die een bedrijf op een goed maakt",
            "Het gemak waarmee je een goed kan kopen",
        ],
        antwoord=0,
        uitleg="Nut is hoe goed een goed je behoefte voldoet. Het is persoonlijk: hetzelfde goed heeft voor de ene meer nut dan voor de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen totaal nut en marginaal nut?",
        opties=[
            "Totaal nut is dat van alle eenheden samen, marginaal nut dat van de laatste",
            "Totaal nut geldt voor iedereen samen, marginaal nut voor één persoon apart",
            "Totaal nut is in geld uitgedrukt, marginaal nut in stuks",
            "Totaal nut geldt voor een jaar, marginaal nut voor een dag",
        ],
        antwoord=0,
        uitleg="Marginaal nut of grensnut is wat die ene extra eenheid er nog bij doet. Tel je alle grensnutten op, dan krijg je het totale nut.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het nut van de laatste bijgekomen eenheid? Schrijf twee woorden.",
        antwoord=["marginaal nut", "marginale nut", "grensnut"],
        uitleg="Het marginale nut of grensnut is het extra nut van één eenheid meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van het afnemende grensnut?",
        opties=[
            "Elke extra eenheid van hetzelfde goed levert minder extra nut op",
            "Elke extra eenheid van hetzelfde goed wordt duurder om te kopen",
            "Het totale nut daalt zodra je meer van een goed koopt",
            "Het nut van een goed daalt als de prijs ervan stijgt",
        ],
        antwoord=0,
        uitleg="De eerste pannenkoek smaakt het best, de vijfde veel minder. Het totale nut stijgt nog wel, maar met steeds kleinere stapjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument drinkt op een warme dag glazen water. Het nut is 10, dan 7, dan 4, dan 1. Wat kan je besluiten? Duid alles aan wat juist is.",
        opties=[
            "Het grensnut daalt bij elk glas",
            "Het totale nut na vier glazen is 22",
            "Het totale nut stijgt nog altijd",
            "Het totale nut daalt vanaf het tweede glas",
        ],
        antwoord=[0, 1, 2],
        uitleg="10 plus 7 plus 4 plus 1 is 22. Het grensnut daalt, maar zolang het positief blijft, blijft het totale nut stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer bereikt het totale nut zijn maximum?",
        opties=[
            "Als het grensnut nul wordt",
            "Als het grensnut het hoogst is",
            "Als het grensnut begint te dalen",
            "Als het grensnut negatief wordt",
        ],
        antwoord=0,
        uitleg="Zolang het grensnut positief is, komt er nut bij. Wordt het nul, dan kan er niets meer bij: dat is het toppunt. Daarna, bij een negatief grensnut, daalt het totale nut weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dalend grensnut betekent dat het totale nut ook daalt.",
        antwoord=False,
        uitleg="Zolang het grensnut positief is, blijft het totale nut stijgen, alleen trager. Pas bij een negatief grensnut daalt het totale nut.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent preferentie?",
        opties=[
            "Een consument verkiest de ene combinatie boven de andere",
            "Een consument vindt twee goederencombinaties precies even goed",
            "Een consument koopt altijd hetzelfde merk",
            "Een consument kiest altijd het goedkoopste product",
        ],
        antwoord=0,
        uitleg="Preferentie is voorkeur: de ene combinatie geeft meer nut dan de andere. Zijn ze even goed, dan spreek je van indifferentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent indifferentie?",
        opties=[
            "Twee combinaties geven dezelfde consument evenveel nut",
            "Een consument heeft in geen van beide goederen enige interesse",
            "Twee goederen kosten precies dezelfde prijs",
            "Een consument kan geen van beide goederen betalen",
        ],
        antwoord=0,
        uitleg="Indifferent zijn betekent: het maakt je niet uit welke van de twee je krijgt, want ze geven je evenveel nut. Het heeft niets met prijs of met onverschilligheid te maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verkiezen van de ene combinatie boven de andere? Schrijf één woord.",
        antwoord=["preferentie", "voorkeur"],
        uitleg="Preferentie is de voorkeur van een consument. Ze wordt zichtbaar in de indifferentiemap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veronderstellingen maakt de theorie over de consument? Duid alles aan wat juist is.",
        opties=[
            "Hij kan zijn voorkeuren rangschikken",
            "Hij streeft naar een zo hoog mogelijk nut",
            "Hij houdt rekening met zijn budget",
            "Hij kent de productiekost van elk product",
        ],
        antwoord=[0, 1, 2],
        uitleg="De consument rangschikt, maximaliseert en blijft binnen zijn budget. Wat een product de producent kost, weet hij niet en hoeft hij ook niet te weten.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie 3 broden en 2 liter melk even goed vindt als 2 broden en 4 liter melk, is indifferent tussen die twee combinaties.",
        antwoord=True,
        uitleg="Even veel nut betekent indifferentie. Allebei de combinaties liggen op dezelfde indifferentiecurve.",
    ),
    dict(
        type="waarofniet",
        vraag="Nut is voor iedereen hetzelfde en kan je in euro uitdrukken.",
        antwoord=False,
        uitleg="Nut is persoonlijk en niet in een munt te meten. Daarom werkt de theorie liever met rangschikken: welke combinatie verkies je boven welke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vegetariër en een vleesliefhebber krijgen hetzelfde stuk vlees. Wat toont dat over nut?",
        opties=[
            "Hetzelfde goed kan voor twee mensen een ander nut hebben",
            "Nut hangt alleen af van de prijs die voor het goed betaald wordt",
            "Nut is voor iedereen gelijk zodra het goed hetzelfde is",
            "Nut hangt af van de hoeveelheid die er van het goed is",
        ],
        antwoord=0,
        uitleg="Nut is subjectief: het hangt af van de behoeften van de persoon, niet van het goed zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument eet pannenkoeken met een grensnut van 8, 6, 3 en daarna min 2. Wat zegt die laatste waarde?",
        opties=[
            "De vierde pannenkoek verlaagt zijn totale nut",
            "De vierde pannenkoek verhoogt zijn nut nog met 2",
            "Hij heeft bij de vierde pannenkoek evenveel nut als bij de derde",
            "Zijn totale nut na vier pannenkoeken is 19",
        ],
        antwoord=0,
        uitleg="Een negatief grensnut betekent dat die eenheid je nut doet dalen: je hebt er te veel van gehad. Het totale nut gaat van 17 naar 15.",
    ),
    dict(
        type="waarofniet",
        vraag="De wet van het afnemende grensnut geldt ook voor geld dat je bijkrijgt.",
        antwoord=True,
        uitleg="Honderd euro extra betekent voor wie weinig heeft veel meer dan voor wie al veel heeft. Dat is dezelfde gedachte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het nut van alle eenheden samen? Schrijf twee woorden.",
        antwoord=["totaal nut", "totale nut"],
        uitleg="Het totale nut is de som van alle grensnutten van de eenheden die je hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat de theorie ervan uit dat een consument zijn nut wil maximaliseren?",
        opties=[
            "Omdat het zijn keuzes redelijk goed verklaart",
            "Omdat elke consument in werkelijkheid altijd precies zo rekent",
            "Omdat de overheid dat van de consument verwacht",
            "Omdat het nut anders niet te berekenen valt",
        ],
        antwoord=0,
        uitleg="Het is een model. Mensen rekenen niet echt met nutscijfers, maar wie ervan uitgaat dat ze het beste proberen te halen uit wat ze hebben, voorspelt hun gedrag redelijk goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het grensnut kloppen? Duid alles aan wat juist is.",
        opties=[
            "Het daalt naarmate je meer van hetzelfde goed hebt",
            "Het kan negatief worden",
            "Het is nul wanneer het totale nut op zijn hoogst is",
            "Het is altijd gelijk aan de prijs van het goed",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het grensnut daalt, kan negatief worden en is nul in het toppunt van het totale nut. Met de prijs heeft het niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom betaalt iemand veel voor het eerste glas water in de woestijn en weinig voor het tiende?",
        opties=[
            "Omdat het grensnut van elk volgend glas daalt",
            "Omdat water in de woestijn duurder wordt geproduceerd",
            "Omdat het totale nut van water daalt bij elk glas",
            "Omdat de verkoper zijn prijs verlaagt na elk glas",
        ],
        antwoord=0,
        uitleg="Wat je bereid bent te betalen, hangt af van het nut van die ene extra eenheid. Dat verklaart meteen waarom de vraagcurve daalt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt een indifferentiecurve voor?",
        opties=[
            "Alle combinaties die dezelfde consument evenveel nut geven",
            "Alle combinaties van twee goederen die precies hetzelfde kosten",
            "De hoeveelheid die een consument van een goed koopt bij elke prijs",
            "De hoeveelheid die een producent van een goed aanbiedt bij elke prijs",
        ],
        antwoord=0,
        uitleg="Op één indifferentiecurve liggen alle combinaties met hetzelfde nut. De combinaties die evenveel kosten, liggen op de budgetlijn: dat is een andere lijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt een indifferentiecurve?",
        opties=[
            "Dalend en bol naar de oorsprong toe",
            "Stijgend en recht",
            "Dalend en recht",
            "Stijgend en bol naar de oorsprong toe",
        ],
        antwoord=0,
        uitleg="Ze daalt, want minder van het ene moet je goedmaken met meer van het andere. En ze is gebogen, omdat je steeds meer van het ene nodig hebt om één eenheid van het andere te vervangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom daalt een indifferentiecurve?",
        opties=[
            "Omdat minder van het ene goedgemaakt moet worden met meer van het andere",
            "Omdat de prijs van het ene goed daalt zodra het andere goed duurder wordt",
            "Omdat het inkomen van de consument daalt bij meer aankopen",
            "Omdat het grensnut van beide goederen samen daalt",
        ],
        antwoord=0,
        uitleg="Op één curve blijft het nut gelijk. Geef je iets op van het ene goed, dan moet er iets bij van het andere om op hetzelfde niveau te blijven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van alle indifferentiecurven van één consument? Schrijf één woord.",
        antwoord=["indifferentiemap", "indifferentiekaart"],
        uitleg="De indifferentiemap is een reeks curven onder elkaar. Elke curve staat voor een ander nutsniveau.",
    ),
    dict(
        type="waarofniet",
        vraag="In een indifferentiemap geeft de curve die het verst van de oorsprong ligt, het meeste nut.",
        antwoord=True,
        uitleg="Verder van de oorsprong betekent van allebei de goederen meer, en meer geeft meer nut. Daarom wil de consument zo ver mogelijk naar buiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee indifferentiecurven van dezelfde consument kunnen elkaar snijden.",
        antwoord=False,
        uitleg="Dan zou één combinatie tegelijk twee verschillende nutsniveaus hebben, en dat kan niet. Daarom snijden ze elkaar nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Punt A ligt op een hogere indifferentiecurve dan punt B. Wat betekent dat?",
        opties=[
            "De consument verkiest A boven B",
            "De consument verkiest B boven A",
            "De consument is indifferent tussen A en B",
            "A is goedkoper dan B",
        ],
        antwoord=0,
        uitleg="Hoger in de map betekent meer nut. De prijs zegt de map niet: daarvoor heb je de budgetlijn nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee punten liggen op dezelfde indifferentiecurve. Wat weet je dan? Duid alles aan wat juist is.",
        opties=[
            "Ze geven deze consument evenveel nut",
            "De consument is indifferent tussen de twee",
            "Van het ene is er meer en van het andere minder",
            "Ze kosten allebei precies evenveel geld voor deze consument",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gelijk nut, dus indifferent, en de ene hoeveelheid compenseert de andere. Of ze evenveel kosten, hangt van de prijzen af en lees je niet uit deze curve af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de helling van een indifferentiecurve?",
        opties=[
            "Hoeveel je van het ene wil opgeven voor één eenheid van het andere",
            "Hoeveel het ene goed kost ten opzichte van het andere goed",
            "Hoeveel een consument in totaal te besteden heeft",
            "Hoeveel nut de consument in totaal haalt",
        ],
        antwoord=0,
        uitleg="De helling is de ruilverhouding die de consument zelf aanvaardbaar vindt. De prijsverhouding staat in de helling van de budgetlijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een indifferentiecurve wordt vlakker naarmate je naar rechts gaat.",
        antwoord=True,
        uitleg="Hoe meer je van een goed al hebt, hoe minder je van het andere wil opgeven om er nog iets bij te krijgen. Daarom buigt de curve af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument heeft veel brood en weinig melk. Wat volgt daaruit?",
        opties=[
            "Hij geeft veel brood op voor één liter melk",
            "Hij wil heel veel melk opgeven voor één extra brood",
            "Hij wil van geen van beide iets opgeven",
            "Hij is indifferent tussen brood en melk",
        ],
        antwoord=0,
        uitleg="Van wat je al veel hebt, is het grensnut laag. Van wat schaars is in je mandje, is het grensnut hoog. Daarom ruil je makkelijk brood voor melk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verhouding waarin een consument twee goederen tegen elkaar wil ruilen? Schrijf twee woorden.",
        antwoord=["marginale substitutievoet", "marginale ruilvoet", "substitutievoet"],
        uitleg="De marginale substitutievoet is de helling van de indifferentiecurve: hoeveel van het ene je wil opgeven voor één eenheid van het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een indifferentiemap kloppen? Duid alles aan wat juist is.",
        opties=[
            "Elke curve hoort bij één nutsniveau",
            "Curven die verder van de oorsprong liggen, geven meer nut",
            "De curven snijden elkaar nooit",
            "Elke map geldt voor alle consumenten samen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een map toont de voorkeuren van één consument. Een andere persoon heeft een andere map, want nut is persoonlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tekent men een indifferentiecurve bol naar de oorsprong en niet als een rechte?",
        opties=[
            "Omdat de ruilverhouding verandert als je er al veel van hebt",
            "Omdat de prijzen van beide goederen voortdurend blijven veranderen",
            "Omdat het inkomen van de consument niet vastligt",
            "Omdat een rechte lijn te weinig combinaties zou tonen",
        ],
        antwoord=0,
        uitleg="Bij een rechte zou je altijd dezelfde ruil aanvaarden, hoeveel je er ook al van hebt. De afnemende ruilbereidheid buigt de curve.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een indifferentiemap alleen kan je afleiden welke combinatie een consument zal kopen.",
        antwoord=False,
        uitleg="De map zegt alleen wat hij liever heeft. Wat hij kán kopen, hangt van zijn budget en van de prijzen af. Daarvoor heb je ook de budgetlijn nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument krijgt van allebei de goederen één eenheid meer. Wat gebeurt er in de map?",
        opties=[
            "Hij komt op een hogere indifferentiecurve",
            "Hij komt op een lagere indifferentiecurve",
            "Hij blijft op dezelfde indifferentiecurve",
            "Hij verlaat de indifferentiemap",
        ],
        antwoord=0,
        uitleg="Meer van allebei betekent meer nut, dus een curve verder van de oorsprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je in een indifferentiemap wanneer een consument twee goederen als bijna gelijkwaardig ziet?",
        opties=[
            "De curven lopen bijna recht",
            "De curven lopen bijna verticaal",
            "De curven snijden elkaar",
            "Er is maar één curve in de map",
        ],
        antwoord=0,
        uitleg="Wie twee goederen altijd één op één wil ruilen, heeft een vaste ruilverhouding, en dan is de curve bijna een rechte lijn.",
    ),
    dict(
        type="invultekst",
        vraag="Wat blijft er gelijk langs één indifferentiecurve? Schrijf één woord.",
        antwoord=["nut", "het nut"],
        uitleg="Alle punten op dezelfde curve geven deze consument hetzelfde nut: daar komt de naam vandaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument staat voor twee combinaties: 4 boeken en 1 spel, of 1 boek en 4 spellen. Hij vindt ze even goed. Hoe teken je dat?",
        opties=[
            "Als twee punten op dezelfde dalende curve",
            "Als twee punten op dezelfde stijgende curve",
            "Als twee punten op twee verschillende curven",
            "Als twee punten op dezelfde budgetlijn",
        ],
        antwoord=0,
        uitleg="Even goed betekent hetzelfde nut, dus dezelfde curve. En omdat meer van het ene gepaard gaat met minder van het andere, daalt die curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tekent men deze curven met twee goederen in plaats van met alle producten samen?",
        opties=[
            "Omdat twee goederen in een vlak passen en dus te tekenen zijn",
            "Omdat een consument maar twee goederen tegelijkertijd kan kopen",
            "Omdat er maar twee soorten goederen bestaan",
            "Omdat meer goederen het nut zouden doen dalen",
        ],
        antwoord=0,
        uitleg="Twee goederen passen in een vlak, en dat maakt de redenering zichtbaar. De gedachte zelf geldt net zo goed voor tientallen producten.",
    ),
]

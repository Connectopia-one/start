# -*- coding: utf-8 -*-
"""Golven en hun eigenschappen — 🌍 Beyond, fysica.

Deel 1 gaat over wat een golf is en wat ze wel en niet vervoert, over
mechanische en elektromagnetische golven, over transversaal en longitudinaal,
en over de grootheden van een lopende golf: amplitude, periode, frequentie,
golflengte, golfgetal, pulsatie en golfsnelheid, met de golfvergelijking
\(y(x,t) = A\sin(\omega t - k\,x)\). Deel 2 gaat over de eigenschappen: het
principe van Huygens, weerkaatsing, breking met de wet van Snellius, buiging,
interferentie met haar constructieve en destructieve plekken, en de staande
golf met haar buiken en knopen.

De rode draad is dat een golf energie doorgeeft terwijl de deeltjes op hun
plaats blijven trillen. Omdat hier geen grafiek getekend kan worden, vragen de
vragen naar het verloop of naar de richting in woorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat vervoert een golf?",
        opties=[
            "energie, maar geen materie",
            "materie, maar geen energie",
            "zowel energie als materie",
            "massa, maar geen energie",
        ],
        antwoord=0,
        uitleg="Een kurk op het water danst op en neer, maar drijft niet mee. De deeltjes "
        "trillen op hun plaats en geven de beweging door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een mechanische en een elektromagnetische golf?",
        opties=[
            "een mechanische golf heeft een stof nodig om door te gaan",
            "een elektromagnetische golf heeft een stof nodig om door te gaan",
            "een mechanische golf gaat altijd sneller dan het licht",
            "een elektromagnetische golf vervoert geen energie",
        ],
        antwoord=0,
        uitleg="Geluid komt niet door het vacuüm van de ruimte, licht wel. Daarom is het in "
        "de ruimte volkomen stil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke golven zijn elektromagnetisch? Kruis alles aan wat juist is.",
        opties=[
            "zichtbaar licht",
            "radiogolven",
            "röntgenstraling",
            "geluid in de lucht",
        ],
        antwoord=[0, 1, 2],
        uitleg="Geluid is een mechanische golf en heeft lucht, water of een vaste stof "
        "nodig. De drie andere gaan ook door het vacuüm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een transversale golf?",
        opties=[
            "de deeltjes trillen dwars op de voortplantingsrichting",
            "de deeltjes trillen langs de voortplantingsrichting",
            "de deeltjes trillen alleen aan het begin van de golf",
            "de deeltjes bewegen met de golf mee vooruit",
        ],
        antwoord=0,
        uitleg="Een golf op een touw is zo. Bij een longitudinale golf trillen de deeltjes "
        "wel in de richting waarin de golf loopt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een golf waarbij de deeltjes langs de voortplantingsrichting trillen?",
        antwoord=["longitudinaal", "longitudinale", "een longitudinale golf"],
        uitleg="Geluid in de lucht is daarvan het voorbeeld: de lucht wordt samengeperst en "
        "weer uitgerekt. Dwars op de richting heet transversaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Geluid in de lucht is een longitudinale golf.",
        antwoord=True,
        uitleg="De lucht wordt afwisselend samengeperst en verdund, in de richting waarin "
        "het geluid loopt. Daarom kan geluid niet door het vacuüm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de golflengte van een lopende golf?",
        opties=[
            "de afstand tussen twee punten die in fase trillen",
            "de tijd tussen twee punten die in fase trillen",
            "de grootste uitwijking van een deeltje op de golf",
            "de afstand die de golf in één seconde aflegt",
        ],
        antwoord=0,
        uitleg=r"Ze staat in meter en krijgt het symbool \(\lambda\). De afstand die de "
        r"golf per seconde aflegt, is haar snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de snelheid van een golf?",
        opties=[
            r"\(v = \lambda\,f\)",
            r"\(v = \dfrac{\lambda}{f}\)",
            r"\(v = \lambda\,T\)",
            r"\(v = \dfrac{f}{\lambda}\)",
        ],
        antwoord=0,
        uitleg=r"Je kan ook \(v = \dfrac{\lambda}{T}\) schrijven, want dat is hetzelfde. "
        r"In één periode schuift de golf precies één golflengte op.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een golf heeft \(\lambda = 2{,}0\) m en \(f = 50\) Hz. Hoe snel loopt ze?",
        opties=[
            r"\(100\) m/s",
            r"\(25\) m/s",
            r"\(52\) m/s",
            r"\(0{,}04\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(v = \lambda\,f = 2{,}0 \times 50 = 100\) m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het golfgetal van een lopende golf?",
        opties=[
            r"\(k = \dfrac{2\pi}{\lambda}\)",
            r"\(k = \dfrac{2\pi}{T}\)",
            r"\(k = \dfrac{\lambda}{2\pi}\)",
            r"het aantal golven per seconde",
        ],
        antwoord=0,
        uitleg=r"Het staat in \(\text{rad/m}\) en krijgt het symbool \(k\). De pulsatie "
        r"\(\omega = \dfrac{2\pi}{T}\) is het tegenhangertje ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de golfvergelijking van een rechtslopende golf?",
        opties=[
            r"\(y = A\sin(\omega t - k\,x)\)",
            r"\(y = A\sin(\omega t + k\,x)\)",
            r"\(y = A\sin(k\,x - \omega t)\)",
            r"\(y = A\,\omega\,t - k\,x\)",
        ],
        antwoord=0,
        uitleg=r"Het minteken voor de \(x\) hoort bij een golf die naar rechts loopt. Een "
        r"plusteken geeft een linkslopende golf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens lees je uit de golfvergelijking? Kruis alles aan wat juist is.",
        opties=[
            "de amplitude van de golf",
            r"de pulsatie \(\omega\) en dus \(T\)",
            r"het golfgetal \(k\) en dus \(\lambda\)",
            "de stof waar de golf door loopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De stof staat er niet in, al bepaalt ze wel de snelheid. Uit de pulsatie en "
        "het golfgetal volgt die snelheid trouwens ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle deeltjes van een lopende golf beginnen op hetzelfde ogenblik te trillen.",
        antwoord=False,
        uitleg="De golf heeft tijd nodig om er te komen, namelijk de afstand gedeeld door de "
        "snelheid. Een deeltje verder van de bron begint dus later.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bron trilt al \(3{,}0\) s en een deeltje ligt \(10\) m verder. De golf loopt \(5{,}0\) m/s. Hoelang trilt dat deeltje al?",
        opties=[
            r"\(1{,}0\) s",
            r"\(2{,}0\) s",
            r"\(3{,}0\) s",
            r"\(5{,}0\) s",
        ],
        antwoord=0,
        uitleg=r"De golf doet \(\dfrac{10}{5{,}0} = 2{,}0\) s over die afstand, dus trilt "
        r"het deeltje \(3{,}0 - 2{,}0 = 1{,}0\) s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een golf loopt naar rechts. In welke richting beweegt een deeltje dat net voor een berg ligt?",
        opties=[
            "naar boven, want de berg schuift naar hem toe",
            "naar beneden, want de berg schuift van hem weg",
            "naar rechts, met de golf mee",
            "het blijft stil tot de berg er is",
        ],
        antwoord=0,
        uitleg="Een deeltje doet straks wat zijn buur aan de kant van de bron nu doet. Bij "
        "een rechtslopende golf is dat de buur links van hem.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle deeltjes op een lopende golf trillen met dezelfde frequentie.",
        antwoord=True,
        uitleg="Die frequentie komt van de bron en verandert onderweg niet. Hun fase "
        "verschilt wel, want ze beginnen op een ander moment.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de snelheid van een golf af?",
        opties=[
            "van de stof waar de golf door loopt",
            "van de amplitude van de golf",
            "van de frequentie van de bron alleen",
            "van de afstand tot de bron",
        ],
        antwoord=0,
        uitleg=r"Verhoog je \(f\), dan krimpt \(\lambda\) en blijft \(v\) gelijk. In "
        r"water loopt geluid veel sneller dan in lucht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een golf met een grotere amplitude loopt sneller.",
        antwoord=False,
        uitleg="De amplitude zegt alleen hoeveel energie de golf vervoert. De snelheid hangt "
        "van de stof af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een lopende golf zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de golf vervoert energie zonder materie mee te nemen",
            "de deeltjes trillen rond hun eigen evenwichtsstand",
            "de deeltjes schuiven met de golf mee naar voren",
            r"\(\lambda\) is gelijk aan \(A\)",
        ],
        antwoord=[0, 1],
        uitleg=r"\(\lambda\) is een afstand langs de golf, \(A\) een uitwijking dwars "
        r"erop. En de deeltjes blijven waar ze zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de richting waarin de deeltjes van een golf heen en weer gaan?",
        antwoord=["de trilrichting", "trilrichting", "trillingsrichting"],
        uitleg="Bij een transversale golf staat ze dwars op de voortplantingsrichting. Bij "
        "een longitudinale golf vallen de twee samen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt het principe van Huygens?",
        opties=[
            "elk punt van een golffront werkt zelf als een nieuwe bron",
            "elk golffront loopt altijd in een rechte lijn verder",
            "elke golf weerkaatst onder dezelfde hoek als ze invalt",
            "elke golf buigt af als ze een opening tegenkomt",
        ],
        antwoord=0,
        uitleg="Het nieuwe front is het gezamenlijke resultaat van al die kleine golfjes. "
        "Daarmee verklaar je weerkaatsing, breking en buiging.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het terugkaatsen van een golf op een wand, met een ander woord?",
        antwoord=["reflectie", "weerkaatsing", "de reflectie"],
        uitleg="De hoek waaronder ze terugkomt is gelijk aan de hoek waaronder ze invalt. "
        "Een echo is daarvan het voorbeeld bij geluid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verandert er bij breking van een golf? Kruis alles aan wat juist is.",
        opties=[
            "de snelheid van de golf",
            "de golflengte van de golf",
            "de richting van de golf",
            "de frequentie van de golf",
        ],
        antwoord=[0, 1, 2],
        uitleg="De frequentie komt van de bron en blijft dezelfde. Omdat de snelheid "
        "verandert en de frequentie niet, moet de golflengte mee veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de wet van Snellius?",
        opties=[
            r"\(\dfrac{\sin i}{\sin r} = \dfrac{n_{r}}{n_{i}}\)",
            r"\(\dfrac{\sin i}{\sin r} = \dfrac{n_{i}}{n_{r}}\)",
            r"\(\sin i \cdot \sin r = n_{i}\,n_{r}\)",
            r"\(\dfrac{i}{r} = \dfrac{n_{r}}{n_{i}}\)",
        ],
        antwoord=0,
        uitleg=r"Let op welke brekingsindex boven staat. De wet geldt voor de sinussen van "
        r"de hoeken, niet voor de hoeken zelf.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een brekingsindex van \(1{,}5\) betekent dat licht in die stof \(1{,}5\) keer sneller gaat dan in vacuüm.",
        antwoord=False,
        uitleg=r"Net \(1{,}5\) keer langzamer, want \(n = \dfrac{c}{v}\). Glas zit rond "
        r"\(1{,}5\) en water rond \(1{,}33\).",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de overgang naar een stof met een hogere brekingsindex buigt de straal naar de normaal toe.",
        antwoord=True,
        uitleg="De golf gaat daar langzamer, en dat draait het front. Van glas naar lucht "
        "buigt de straal net van de normaal weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het afbuigen van een golf achter een smalle opening?",
        antwoord=["buiging", "diffractie", "de buiging"],
        uitleg="Achter de opening loopt de golf ook de schaduw in. Dat is precies wat het "
        "principe van Huygens voorspelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen verklaar je met het principe van Huygens? Kruis alles aan wat juist is.",
        opties=[
            "de weerkaatsing van een golf op een wand",
            "de breking van een golf bij een andere stof",
            "de buiging van een golf achter een opening",
            "de demping van een golf door wrijving",
        ],
        antwoord=[0, 1, 2],
        uitleg="Demping is een verlies van energie en geen gevolg van het golffront. De "
        "buiging is het sterkst als de opening even groot is als de golflengte of kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen van golven noemt men samen? Kruis alles aan wat juist is.",
        opties=[
            "weerkaatsing of reflectie",
            "breking of refractie",
            "buiging of diffractie",
            "demping of wrijving",
        ],
        antwoord=[0, 1, 2],
        uitleg="Interferentie hoort er ook bij. Demping is geen eigenschap van een golf maar "
        "een verlies van energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is interferentie?",
        opties=[
            "twee golven die samen één nieuwe uitwijking geven",
            "twee golven die elkaar van richting doen veranderen",
            "een golf die op een wand terugkaatst",
            "een golf die achter een opening afbuigt",
        ],
        antwoord=0,
        uitleg="Je telt de uitwijkingen op punt per punt. Daarna lopen de twee golven "
        "gewoon verder zoals ze bezig waren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer treedt constructieve interferentie op?",
        opties=[
            "als de twee golven er in fase aankomen",
            "als de twee golven er in tegenfase aankomen",
            "als de twee golven een verschillende frequentie hebben",
            "als de ene golf een grotere snelheid heeft",
        ],
        antwoord=0,
        uitleg="De uitwijkingen tellen dan op tot een grotere amplitude. In tegenfase heffen "
        "ze elkaar juist op, en dat is destructief.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij destructieve interferentie kunnen twee golven elkaar volledig uitdoven.",
        antwoord=True,
        uitleg="Dat lukt als ze in tegenfase aankomen met dezelfde amplitude. Een "
        "koptelefoon met ruisonderdrukking werkt zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat twee bronnen coherent zijn?",
        opties=[
            "ze hebben dezelfde frequentie en een vast faseverschil",
            "ze hebben dezelfde amplitude en dezelfde plaats",
            "ze liggen precies even ver van de waarnemer",
            "ze zenden elk een golf in een andere stof uit",
        ],
        antwoord=0,
        uitleg="Alleen dan blijft het interferentiepatroon op zijn plaats staan. Anders "
        "verschuiven de lichte en donkere plekken voortdurend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat een staande golf?",
        opties=[
            "door interferentie van een golf met haar eigen weerkaatsing",
            "door twee golven met een heel verschillende frequentie",
            "door een golf die van stof verandert en breekt",
            "door een golf die achter een opening afbuigt",
        ],
        antwoord=0,
        uitleg="De heenlopende en de teruglopende golf vallen samen. Het patroon lijkt dan "
        "stil te staan, al blijven de deeltjes trillen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een punt van een staande golf dat helemaal niet trilt?",
        antwoord=["een knoop", "knoop", "knooppunt"],
        uitleg="Daar heffen de twee golven elkaar altijd op. Het punt dat juist het hevigst "
        "trilt, heet een buik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een staande golf zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een knoop trilt helemaal niet",
            "een buik trilt met de grootste amplitude",
            "de knopen schuiven langs het touw naar voren",
            "alle punten van de golf trillen in fase",
        ],
        antwoord=[0, 1],
        uitleg="De knopen blijven op hun plaats, en dat is net het kenmerk van een staande "
        "golf. Punten aan weerszijden van een knoop trillen in tegenfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke punten van een staande golf trillen in fase met elkaar?",
        opties=[
            "de punten tussen twee opeenvolgende knopen",
            "de punten aan weerszijden van dezelfde knoop",
            "alle punten van de hele staande golf",
            "enkel de knopen onder elkaar",
        ],
        antwoord=0,
        uitleg=r"Zij gaan samen omhoog en samen omlaag. Over een knoop heen is "
        r"\(\Delta\varphi = \pi\), dus tegenfase.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij breking verandert ook de frequentie van de golf.",
        antwoord=False,
        uitleg="De frequentie komt van de bron en blijft dezelfde. De snelheid en de "
        "golflengte veranderen wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijkt een rietje in een glas water geknikt?",
        opties=[
            "het licht breekt bij de overgang van water naar lucht",
            "het licht weerkaatst op het oppervlak van het water",
            "het licht buigt rond de rand van het glas",
            "het water maakt het rietje echt een beetje krom",
        ],
        antwoord=0,
        uitleg="De stralen veranderen daar van richting, dus zien we het stuk onder water "
        "verschoven. Het rietje zelf blijft recht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoor je een laag gebrom van een feest verder dan de hoge tonen?",
        opties=[
            "lage tonen hebben een grotere golflengte en buigen beter af",
            "lage tonen hebben een grotere snelheid in de lucht",
            "lage tonen hebben altijd een grotere amplitude",
            "hoge tonen worden door de lucht naar boven gebogen",
        ],
        antwoord=0,
        uitleg="Ze lopen gemakkelijker rond hoeken en door openingen. De buiging is sterk "
        "zodra de golflengte niet klein is tegenover het obstakel.",
    ),
]

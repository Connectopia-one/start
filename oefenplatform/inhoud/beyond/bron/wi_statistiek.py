# -*- coding: utf-8 -*-
"""Statistiek: de normale verdeling, steekproeven en de hypothesetoets.

Het derde stuk van het onderdeel "Telproblemen, kansrekenen en statistiek"
van fiche G2. Alles staat hier in opgaven met context, en het rekenwerk mag
met ICT: wat je zelf moet kunnen, is beoordelen of een model past en wat een
uitkomst betekent.

Deel 1 is de normale verdeling met de Gausskromme en de z-score.
Deel 2 zijn de steekproeven, het verschil tussen samenhang en oorzaak, en de
hypothesetoets.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet de grafiek van een normale verdeling \(N(\mu, \sigma^{2})\) eruit?",
        opties=[
            r"klokvormig en symmetrisch rond \(\mu\)",
            r"klokvormig maar met een lange staart naar rechts",
            r"een rechte die gelijkmatig stijgt tot aan \(\mu\)",
            r"een trapjeslijn met één stap per waarde",
        ],
        antwoord=0,
        uitleg=r"Die kromme heet de Gausskromme. Is een histogram duidelijk scheef, dan past het normale model niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat bepaalt waar de top van de Gausskromme ligt?",
        opties=[
            r"het gemiddelde \(\mu\)",
            r"de standaardafwijking \(\sigma\)",
            r"het aantal metingen \(n\)",
            r"de grootste meetwaarde",
        ],
        antwoord=0,
        uitleg=r"\(\mu\) schuift de kromme naar links of naar rechts. \(\sigma\) maakt haar breder of smaller.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een meting is precies gelijk aan \(\mu\). Welke z-score heeft ze? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"De z-score meet hoeveel standaardafwijkingen je van \(\mu\) af zit. Op \(\mu\) zelf is dat nul.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De standaardafwijking \(\sigma\) bepaalt hoe breed de Gausskromme is.",
        antwoord=True,
        uitleg=r"Een kleine \(\sigma\) geeft een smalle, hoge klok; een grote \(\sigma\) geeft een brede, platte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule geeft de z-score van een meting \(x\)?",
        opties=[
            r"\(z = \dfrac{x - \mu}{\sigma}\)",
            r"\(z = \dfrac{x - \sigma}{\mu}\)",
            r"\(z = (x - \mu) \cdot \sigma\)",
            r"\(z = \dfrac{x}{\mu}\)",
        ],
        antwoord=0,
        uitleg=r"Zo wordt elke verdeling omgezet naar de standaardnormale, en kan je metingen uit verschillende groepen vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is de totale oppervlakte onder een Gausskromme?",
        opties=[r"\(1\)", r"\(100\)", r"\(0\)", r"gelijk aan \(\mu\)"],
        antwoord=0,
        uitleg=r"Alle kans samen is \(1\). Een kans is dus een stuk van die oppervlakte.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een continue verdeling geldt \(P(X = a) = 0\) voor elke afzonderlijke waarde \(a\).",
        antwoord=True,
        uitleg=r"Een enkele waarde heeft geen breedte, dus ook geen oppervlakte. Daarom reken je altijd met intervallen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Welk gemiddelde \(\mu\) heeft de standaardnormale verdeling? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"Ze is de normale verdeling na omzetting naar z-scores, dus \(N(0, 1)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke standaardafwijking \(\sigma\) heeft de standaardnormale verdeling?",
        opties=[r"\(1\)", r"\(0\)", r"\(100\)", r"dezelfde als de oorspronkelijke"],
        antwoord=0,
        uitleg=r"Dus \(N(0, 1)\): één eenheid op de as is precies één standaardafwijking.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Ongeveer \(95\,\%\) van de metingen ligt binnen één standaardafwijking van \(\mu\).",
        antwoord=False,
        uitleg=r"Binnen \(\mu \pm \sigma\) ligt ongeveer \(68\,\%\). De \(95\,\%\) hoort bij \(\mu \pm 2\sigma\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel procent van de metingen ligt ongeveer binnen \(\mu \pm 2\sigma\)?",
        opties=[r"\(95\,\%\)", r"\(68\,\%\)", r"\(99\,\%\)", r"\(50\,\%\)"],
        antwoord=0,
        uitleg=r"Dat is de vuistregel: ongeveer \(68\,\%\), \(95\,\%\) en \(99{,}7\,\%\) bij één, twee en drie standaardafwijkingen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Er geldt \(\mu = 70\) en \(\sigma = 5\). Welke z-score heeft een meting van \(80\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(z = \dfrac{80 - 70}{5} = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe beoordeel je of de normale verdeling een geschikt model is voor je gegevens?",
        opties=[
            r"je kijkt of het histogram ongeveer klokvormig is",
            r"je kijkt of alle waarden positief zijn",
            r"je kijkt of er precies honderd metingen zijn",
            r"je kijkt of \(\mu\) groter is dan nul",
        ],
        antwoord=0,
        uitleg=r"Je kan er ook de dichtheidsfunctie met de geschatte parameters over tekenen en vergelijken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een z-score kan negatief zijn.",
        antwoord=True,
        uitleg=r"Dan ligt de meting onder \(\mu\). Het teken zegt aan welke kant ze zit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(z = -1{,}5\)?",
        opties=[
            r"de meting ligt \(1{,}5\) standaardafwijking onder \(\mu\)",
            r"de meting ligt \(1{,}5\) standaardafwijking boven \(\mu\)",
            r"de meting is \(1{,}5\) eenheid kleiner dan \(\mu\)",
            r"de kans op die meting is \(1{,}5\,\%\)",
        ],
        antwoord=0,
        uitleg=r"De z-score telt in standaardafwijkingen, niet in de eenheid van de meting zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarmee komt een kans bij een normale verdeling overeen?",
        opties=[
            r"met de oppervlakte onder de Gausskromme",
            r"met de hoogte van de Gausskromme in dat punt",
            r"met de z-score van de bijbehorende waarde",
            r"met de breedte van het interval op de x-as",
        ],
        antwoord=0,
        uitleg=r"De hoogte alleen zegt niets: pas een stuk oppervlakte geeft een kans.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De Gausskromme raakt links en rechts de horizontale as.",
        antwoord=False,
        uitleg=r"Ze nadert de as wel, maar bereikt haar nooit. Elke waarde blijft dus in principe mogelijk.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel procent van de metingen ligt links van \(\mu\) bij een normale verdeling? Schrijf het getal.",
        antwoord=["50", "vijftig"],
        uitleg=r"De kromme is symmetrisch om \(\mu\), dus de oppervlakte valt in twee gelijke helften uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee Gausskrommen hebben hetzelfde \(\mu\), maar de ene is smaller. Wat betekent dat?",
        opties=[
            r"bij de smalle liggen de metingen dichter bij \(\mu\)",
            r"bij de smalle liggen de metingen verder van \(\mu\)",
            r"de smalle hoort bij een grotere groep metingen",
            r"de smalle heeft een kleinere totale oppervlakte",
        ],
        antwoord=0,
        uitleg=r"Smaller betekent een kleinere \(\sigma\), dus minder spreiding. De oppervlakte blijft bij allebei \(1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen \(\mu\) van een populatie en \(\overline{x}\) van een steekproef?",
        opties=[
            r"\(\mu\) is de echte waarde, \(\overline{x}\) een schatting ervan",
            r"\(\mu\) is een schatting, \(\overline{x}\) de echte waarde",
            r"\(\mu\) gebruikt meer cijfers na de komma dan \(\overline{x}\)",
            r"er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg=r"Daarom krijgen ze ook een ander symbool. Je kent \(\mu\) meestal niet en schat het uit je steekproef.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is een steekproef representatief?",
        opties=[
            r"als ze op de belangrijke kenmerken op de populatie lijkt",
            r"als ze uit minstens honderd personen bestaat",
            r"als iedereen die meedeed dat vrijwillig deed",
            r"als ze op één plaats en in één keer verzameld is geweest",
        ],
        antwoord=0,
        uitleg=r"Grootte alleen helpt niet: een heel grote maar scheve steekproef blijft scheef.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is randomisatie bij een steekproef?",
        opties=[
            r"iedereen uit de populatie evenveel kans geven om gekozen te worden",
            r"de deelnemers zelf laten beslissen of ze meedoen",
            r"de gegevens achteraf in willekeurige volgorde zetten",
            r"een groep kiezen die het gemakkelijkst te bereiken valt, zonder loting",
        ],
        antwoord=0,
        uitleg=r"Dat is net wat een enkelvoudig aselecte steekproef doet, en het is de beste bescherming tegen vertekening.",
    ),
    dict(
        type="invultekst",
        vraag=r"Het significantieniveau is \(\alpha = 0{,}05\). Hoeveel procent is dat? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"Dat is de kans die je aanvaardt om \(H_{0}\) onterecht te verwerpen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een grotere aselecte steekproef geeft doorgaans een betrouwbaarder resultaat.",
        antwoord=True,
        uitleg=r"De steekproeffout wordt kleiner. Een niet-steekproeffout, zoals een slechte vraagstelling, wordt er niet kleiner van.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen een steekproeffout en een niet-steekproeffout?",
        opties=[
            r"de eerste komt door het toeval van de trekking, de tweede door de opzet",
            r"de eerste komt door de opzet, de tweede door het toeval van de trekking",
            r"de eerste kan je berekenen, de tweede komt alleen bij kleine groepen voor",
            r"de eerste gaat over de populatie, de tweede over de variabele",
        ],
        antwoord=0,
        uitleg=r"Toeval kan je inschatten en kleiner maken met meer deelnemers. Een fout in de opzet blijft ook bij duizend deelnemers bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een krant laat lezers online stemmen over een stelling. Welk probleem is dat?",
        opties=[
            r"vrijwillige respons, want wie zich sterk betrokken voelt, stemt vaker",
            r"een te kleine steekproef, want online doen er maar weinig mensen mee",
            r"randomisatie, want de volgorde van de antwoorden ligt vast",
            r"er is geen probleem, want iedereen kon meedoen",
        ],
        antwoord=0,
        uitleg=r"De groep die antwoordt, is niet toevallig samengesteld. Dat is een niet-steekproeffout, en meer stemmen lost dat niet op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als twee grootheden sterk samenhangen, is de ene de oorzaak van de andere.",
        antwoord=False,
        uitleg=r"Samenhang kan ook komen van een derde verborgen variabele, van omgekeerde oorzaak en gevolg, of gewoon van toeval.",
    ),
    dict(
        type="invultekst",
        vraag=r"De correlatiecoëfficiënt \(r\) ligt tussen twee getallen. Schrijf het kleinste.",
        antwoord=["-1", "min 1"],
        uitleg=r"Er geldt \(-1 \le r \le 1\). Het teken geeft de richting, de grootte de sterkte van het lineaire verband.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de zomer worden er meer ijsjes verkocht en gebeuren er meer verdrinkingen. Wat verklaart die samenhang?",
        opties=[
            r"een derde verborgen variabele, namelijk het warme weer",
            r"ijsjes eten maakt zwemmen gevaarlijker",
            r"verdrinkingen zetten mensen aan om meer ijsjes te kopen",
            r"er is geen samenhang, het is een rekenfout",
        ],
        antwoord=0,
        uitleg=r"Warm weer verhoogt allebei de aantallen. Dat is het klassieke voorbeeld van samenhang zonder oorzakelijk verband.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De nulhypothese \(H_{0}\) is de uitspraak die je met je onderzoek wil aantonen.",
        antwoord=False,
        uitleg=r"Het is net omgekeerd: \(H_{0}\) is wat je probeert te verwerpen. Wat je wil aantonen, staat in \(H_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de p-waarde?",
        opties=[
            r"de kans op zo'n resultaat of extremer, als \(H_{0}\) waar is",
            r"de kans dat \(H_{0}\) waar is, gegeven dit ene resultaat",
            r"de kans dat je onderzoek achteraf herhaalbaar blijkt te zijn",
            r"het aandeel van de hele populatie dat in de steekproef zit",
        ],
        antwoord=0,
        uitleg=r"Ze zegt niets over de kans dat de hypothese klopt, alleen hoe verrassend je resultaat zou zijn mocht ze kloppen.",
    ),
    dict(
        type="invultekst",
        vraag=r"De p-waarde is \(0{,}02\) en \(\alpha = 0{,}05\). Verwerp je \(H_{0}\)? Schrijf ja of nee.",
        antwoord=["ja"],
        uitleg=r"Er geldt \(p < \alpha\), dus het resultaat is te onwaarschijnlijk om nog bij \(H_{0}\) te passen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een type I-fout?",
        opties=[
            r"\(H_{0}\) verwerpen terwijl ze eigenlijk waar is",
            r"\(H_{0}\) behouden terwijl ze eigenlijk vals is",
            r"een rekenfout maken bij het bepalen van de p-waarde",
            r"de verkeerde alternatieve hypothese kiezen vooraf",
        ],
        antwoord=0,
        uitleg=r"De kans daarop is net \(\alpha\), dat je vooraf kiest. Een vals alarm, dus.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een type II-fout is \(H_{0}\) onterecht niet verwerpen.",
        antwoord=True,
        uitleg=r"Er was wel degelijk een effect, maar je onderzoek vond het niet. Dat gebeurt vaker bij een kleine steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer gebruik je een eenzijdige hypothesetoets?",
        opties=[
            r"als je vooraf een richting verwacht, bijvoorbeeld een stijging",
            r"als je steekproef uit maar één enkele groep mensen bestaat",
            r"als de verdeling achteraf niet symmetrisch blijkt te zijn",
            r"als je maar één keer kan meten in het hele onderzoek",
        ],
        antwoord=0,
        uitleg=r"Vermoed je alleen dat er iets verandert, zonder te weten in welke richting, dan toets je tweezijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat lees je af in een spreidingsdiagram?",
        opties=[
            r"of er een verband is tussen twee numerieke grootheden",
            r"hoe vaak elke afzonderlijke waarde voorkomt",
            r"hoeveel procent van de metingen boven \(\mu\) ligt",
            r"wat de standaardafwijking van de gegevens is",
        ],
        antwoord=0,
        uitleg=r"Elk punt is één waarneming met twee kenmerken. De vorm van de wolk verraadt het verband.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een correlatiecoëfficiënt \(r\) dicht bij \(0\) wijst op een sterk lineair verband.",
        antwoord=False,
        uitleg=r"Dicht bij \(0\) betekent net dat er nauwelijks lineair verband is. Sterk is ze als \(r\) dicht bij \(-1\) of \(1\) ligt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noemen we \(\alpha\), de kans die je vooraf aanvaardt om \(H_{0}\) onterecht te verwerpen? Schrijf het woord.",
        antwoord=["significantieniveau", "alfa"],
        uitleg=r"Meestal kiest men \(0{,}05\), soms \(0{,}01\) als een vals alarm duur uitvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een trendlijn in een spreidingsdiagram?",
        opties=[
            r"een rechte of kromme die het patroon in de puntenwolk samenvat",
            r"de lijn die alle punten van de puntenwolk met elkaar verbindt",
            r"de lijn waarop precies de helft van de punten ligt",
            r"de rand van het gebied waarbinnen alle punten liggen",
        ],
        antwoord=0,
        uitleg=r"Ze gaat meestal niet door de punten zelf, maar loopt er zo dicht mogelijk langs.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je verwerpt \(H_{0}\) niet. Wat besluit je?",
        opties=[
            r"er is onvoldoende bewijs tegen \(H_{0}\) gevonden",
            r"\(H_{0}\) is hiermee bewezen waar",
            r"het onderzoek is mislukt en moet overgedaan worden",
            r"de alternatieve hypothese is hiermee verworpen",
        ],
        antwoord=0,
        uitleg=r"Geen bewijs vinden is niet hetzelfde als bewijzen dat er niets is. Misschien was je steekproef gewoon te klein.",
    ),
]

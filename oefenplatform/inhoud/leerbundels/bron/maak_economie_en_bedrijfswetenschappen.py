# -*- coding: utf-8 -*-
"""De leerbundels voor economie en bedrijfswetenschappen op 🚀 Boost dubbele
finaliteit.

Gebaseerd op de vakfiche 2DU economie en bedrijfswetenschappen, geldig vanaf
1 januari 2027. Zestien thema's: vier over de consument en de producent, vier
over de onderneming en haar mensen, vier over het personeel en het loon, en
vier over verkopen, documenten en logistiek.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Economie en bedrijfswetenschappen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    BUNDELS[slug + "-boost-dubbele-finaliteit"] = b


# ───────────────────────── 1. Behoeften, schaarste en soorten goederen
zet("behoeften-schaarste-en-soorten-goederen",
    titel="Behoeften, schaarste en soorten goederen",
    onder="Waarom er gekozen moet worden, de soorten behoeften, het verschil tussen welvaart en welzijn, en de indelingen van goederen en diensten.",
    secties=[
        dict(kop="Het economisch probleem", blokken=[
            ("p", "<strong>Een behoefte is een gevoel van gemis</strong>: je mist iets en wil dat gemis "
                  "wegnemen. <strong>Schaarste is te weinig middelen voor alle behoeften</strong>, een tekort tegenover wat we willen, en "
                  "<strong>daarom moet er gekozen worden</strong>."),
            ("p", "<strong>Dat is het economisch probleem: de behoeften zijn onbeperkt, de middelen zijn "
                  "beperkt en het budget is begrensd.</strong> <strong>De consument moet kiezen omdat zijn "
                  "budget beperkt is</strong>: hij kan niet alles kopen wat hij nuttig vindt. Dat heet "
                  "<strong>het keuzeprobleem van de consument</strong>."),
            ("p", "<strong>Schaarste dwingt tot kiezen, geldt ook voor tijd en geldt voor elk land.</strong> "
                  "Ook wie veel geld heeft, heeft maar vierentwintig uur per dag. <strong>De consument kiest "
                  "volgens de economie voor het meeste nut</strong> binnen zijn budget."),
        ]),
        dict(kop="Soorten behoeften", blokken=[
            ("p", "<strong>De vakfiche deelt de behoeften op drie manieren in</strong>, en je moet ze alle "
                  "drie kunnen toepassen op een voorbeeld."),
            ("kader", tabel(["indeling", "het ene", "het andere"],
                            [["<strong>economisch of niet</strong>", "<strong>een economische behoefte kost geld</strong>: je hebt er een schaars goed of een dienst voor nodig", "<strong>vriendschap is niet-economisch</strong>: je kan ze niet kopen"],
                             ["<strong>primair of secundair</strong>", "<strong>primair is wat je nodig hebt om te leven</strong>: eten, drinken, onderdak", "<strong>secundair kan gemist worden</strong>: een reis, een spelconsole, een tweede wagen"],
                             ["<strong>individueel of collectief</strong>", "<strong>individueel is voor één persoon</strong>: jouw honger stil je met jouw brood", "<strong>collectief is voor iedereen samen</strong>: veiligheid, wegen, een brandweer"]])),
            ("p", "<strong>Een primaire behoefte is dus niet iets wat je kan missen</strong>, maar net het "
                  "omgekeerde. De prijs is geen indeling van behoeften."),
            ("p", "<strong>Welvaart gaat over hoeveel je kan kopen, welzijn over hoe goed je je "
                  "voelt.</strong> <strong>Welzijn is breder dan welvaart</strong>: gezondheid, vrije tijd, "
                  "veiligheid en relaties horen er ook bij. <strong>Wie meer welvaart heeft, heeft daarom nog "
                  "niet meer welzijn</strong>: meer kunnen kopen maakt iemand niet vanzelf gelukkiger of "
                  "gezonder."),
        ]),
        dict(kop="Soorten goederen", blokken=[
            ("p", "<strong>Een goed kan je vastnemen, een dienst niet</strong>: een goed is tastbaar, een "
                  "dienst is werk dat iemand voor je doet. <strong>Een knipbeurt bij de kapper is een "
                  "dienst</strong>: je krijgt geen voorwerp mee, wel het werk van de kapper."),
            ("kader", tabel(["indeling", "het ene", "het andere"],
                            [["<strong>economisch of vrij</strong>", "<strong>een economisch goed kost geld</strong>, want het is schaars", "<strong>een vrij goed is er gratis</strong>, zoals lucht: er is overvloed, genoeg voor iedereen"],
                             ["<strong>verbruiks- of gebruiksgoed</strong>", "<strong>een verbruiksgoed verdwijnt bij het gebruik</strong>: brood, benzine, papier", "<strong>een gebruiksgoed gebruik je keer op keer</strong>: een fiets, een koelkast"],
                             ["<strong>consumptie- of investeringsgoed</strong>", "<strong>een consumptiegoed stilt een behoefte</strong>", "<strong>een investeringsgoed dient om mee te produceren</strong>: een machine, een bestelwagen, een gebouw"],
                             ["<strong>individueel of collectief</strong>", "<strong>een brood eet één persoon op</strong>", "<strong>een dijk, de straatverlichting en het leger zijn er voor allen</strong>"]])),
            ("p", "<strong>Duurzaam betekent in de economie dat iets lang meegaat</strong>: een koelkast is "
                  "duurzaam, brood niet. Het heeft hier dus niets met milieu te maken. Verbruiksgoederen zijn op zodra je ze gebruikt, gebruiksgoederen gaan keer op keer mee, en investeringsgoederen, ook kapitaalgoederen genoemd, dienen om te produceren."),
            ("p", "<strong>Een collectief goed is er voor iedereen tegelijk</strong>: dat jij van een "
                  "straatlamp geniet, verhindert niemand anders. <strong>De overheid betaalt een zuiver "
                  "collectief goed omdat niemand het uit zichzelf zou betalen</strong>: je kan er toch "
                  "niemand van uitsluiten. <strong>Bij een quasi-collectief goed zorgt de overheid ervoor "
                  "terwijl je er wel individueel van geniet</strong>: onderwijs, openbaar vervoer."),
            ("p", "<strong>Een investeringsgoed dient om te produceren, een machine is er een, en het gaat "
                  "meestal jaren mee.</strong> Daarom schrijft een onderneming het over meerdere jaren af."),
        ]),
    ])


# ───────────────────────── 2. Nut, voorkeuren en de vraag van de consument
zet("nut-voorkeuren-en-de-vraag-van-de-consument",
    titel="Nut, voorkeuren en de vraag van de consument",
    onder="Het marginale nut dat afneemt, de indifferentiecurven die de voorkeuren tekenen, de budgetlijn, het optimum op het raakpunt, en hoe daar de vraagcurve uit volgt.",
    secties=[
        dict(kop="Nut en marginaal nut", blokken=[
            ("p", "<strong>Nut is de voldoening die iets geeft</strong>: hoe goed een goed of een dienst een "
                  "behoefte stilt. <strong>Het totale nut is alle nut samen</strong>, de som van het nut van "
                  "alle eenheden die je hebt."),
            ("p", "<strong>Het marginaal nut is het nut van één extra eenheid</strong>, en <strong>het neemt "
                  "af naarmate je er meer van hetzelfde krijgt</strong>: het eerste glas water bij dorst doet "
                  "veel meer dan het vijfde. <strong>Het kan zelfs nul worden</strong>, en dan geeft een extra "
                  "eenheid je niets meer."),
            ("p", "<strong>Het totale nut daalt daarom niet als je een eenheid bijkrijgt die je graag "
                  "hebt.</strong> Het totale nut stijgt; enkel het marginale nut van die eenheid is kleiner "
                  "dan dat van de vorige. Dat onderscheid is de kern van dit hoofdstuk."),
        ]),
        dict(kop="Voorkeuren en indifferentiecurven", blokken=[
            ("p", "<strong>Een preferentie is een voorkeur</strong>: de consument vindt de ene combinatie "
                  "beter dan de andere. <strong>Indifferentie is net geen voorkeur hebben</strong>: hij vindt "
                  "beide combinaties even goed."),
            ("p", "<strong>Een indifferentiecurve, ook een indifferentielijn, is de lijn van gelijk nut</strong>: alle combinaties van "
                  "twee goederen die evenveel nut geven. <strong>Elk punt erop geeft evenveel nut, ze loopt "
                  "dalend, en ze snijdt geen andere curve.</strong>"),
            ("fig", svg.indifferentiemap(),
             "Drie indifferentiecurven van dezelfde consument. Elke curve verder van de hoek is een hoger "
             "nutsniveau, en ze raken elkaar nergens."),
            ("p", "<strong>Ze loopt dalend</strong>, want meer van het ene betekent minder van het andere bij "
                  "gelijk nut. <strong>Ze is krom en niet recht omdat het ruilen lastiger wordt</strong>: hoe "
                  "minder je van iets hebt, hoe meer van het andere je ervoor wil in de plaats."),
            ("p", "<strong>Twee curven van dezelfde consument snijden elkaar nooit</strong>, want dan zou één "
                  "punt twee verschillende nutsniveaus hebben. <strong>Een curve die een hoger nut geeft, "
                  "ligt verder van de oorsprong</strong>, en <strong>alle curven samen vormen de "
                  "indifferentiemap of indifferentiekaart</strong>."),
        ]),
        dict(kop="De budgetlijn en het optimum", blokken=[
            ("p", "<strong>De budgetlijn, ook de budgetrechte, toont wat je net kan kopen</strong>: alle combinaties die je met je "
                  "volledige budget precies kan betalen. <strong>Waar ze ligt, hangt af van de grootte van "
                  "het budget en van de prijs van elk van de twee goederen.</strong> De voorkeuren zitten in "
                  "de indifferentiecurven, niet in de budgetlijn."),
            ("kader", tabel(["wat er verandert", "wat de budgetlijn doet"],
                            [["<strong>het budget stijgt, de prijzen blijven gelijk</strong>", "<strong>ze schuift parallel naar buiten</strong>: je kan van beide goederen meer kopen"],
                             ["<strong>het budget daalt</strong>", "<strong>ze schuift parallel naar binnen</strong>"],
                             ["<strong>één prijs stijgt</strong>", "<strong>ze kantelt</strong>: het snijpunt met de as van dát goed schuift naar binnen, het andere blijft staan"]])),
            ("p", "<strong>Het optimum ligt op het raakpunt</strong>, waar de budgetlijn een indifferentiecurve "
                  "net raakt. Dat is de hoogste curve die je met je budget nog haalt, en dat punt is de optimale goederencombinatie: de combinatie die het meeste nut geeft."),
            ("fig", svg.budgetlijn(),
             "De budgetlijn en de hoogste indifferentiecurve die ze nog raakt. Het raakpunt is de combinatie "
             "die de consument kiest."),
            ("p", "<strong>De consument kiest dus niet het punt op de allerhoogste curve</strong>: boven zijn "
                  "budgetlijn kan hij niet betalen. Hij kiest het hoogste punt dat hij nog net kan."),
            ("p", "<strong>Wordt een goed duurder, dan kantelt de budgetlijn, kan er minder van gekocht "
                  "worden en verschuift het optimum.</strong> Zijn voorkeuren blijven dezelfde; enkel wat hij "
                  "kan betalen verandert."),
        ]),
        dict(kop="Van optimum naar vraagcurve", blokken=[
            ("p", "<strong>De individuele vraag is wat één koper wil</strong>: de hoeveelheden die één "
                  "consument bij elke prijs wil kopen. <strong>Je vindt zijn vraagcurve door de prijs te "
                  "laten stijgen, telkens het nieuwe optimum te zoeken en die hoeveelheden uit te "
                  "zetten.</strong>"),
            ("p", "<strong>Op de assen van een vraagcurve staan de prijs en de hoeveelheid</strong>: de prijs "
                  "op de verticale as, de gevraagde hoeveelheid op de horizontale. <strong>Een vraagcurve "
                  "loopt dalend</strong>: hoe hoger de prijs, hoe minder er gevraagd wordt, want het budget "
                  "laat er minder van toe en de consument wijkt uit naar iets anders."),
            ("p", "<strong>Stijgt de prijs, dan stijgt de curve niet</strong>: de curve zelf beweegt niet, je "
                  "schuift erlángs naar een kleinere hoeveelheid. Dat verschil tussen een beweging lángs de "
                  "curve en een verschuiving ván de curve komt elk examen terug."),
            ("p", "<strong>De collectieve vraagcurve is de som van de individuele</strong>: je telt bij elke "
                  "prijs de gevraagde hoeveelheden van alle consumenten op. <strong>Ze loopt ook dalend en ze "
                  "geldt voor de hele markt</strong>; ze heet ook de marktvraag."),
        ]),
    ])


# ───────────────────────── 3. De productiefactoren en de productie
zet("de-productiefactoren-en-de-productie",
    titel="De productiefactoren en de productie",
    onder="De vier productiefactoren en wat ze opbrengen, de toegevoegde waarde en de bedrijfskolom, de totale en de marginale productie, de twee wetten van de meeropbrengsten en de volkomen concurrentie.",
    secties=[
        dict(kop="De vier productiefactoren", blokken=[
            ("p", "<strong>Een productiefactor is wat nodig is om te produceren.</strong> De vakfiche noemt "
                  "er vier: <strong>arbeid, kapitaal, natuur en ondernemerschap</strong>. Belastingen horen "
                  "er niet bij: die zijn een kost, geen factor."),
            ("kader", tabel(["factor", "wat het is", "wat het opbrengt"],
                            [["<strong>arbeid</strong>", "<strong>het werk van mensen</strong>, lichamelijk en geestelijk", "<strong>loon</strong>"],
                             ["<strong>kapitaal</strong>", "<strong>alles wat zelf gemaakt is om mee te produceren</strong>: een machine, een bedrijfsgebouw, een vrachtwagen", "<strong>rente</strong>"],
                             ["<strong>natuur</strong>", "<strong>wat de natuur geeft</strong>: grond, grondstoffen, water, delfstoffen, hout", "<strong>huur of pacht</strong>, ook grondrente genoemd"],
                             ["<strong>ondernemerschap</strong>", "<strong>de factoren samenbrengen en het risico dragen</strong>", "<strong>de winst</strong>"]])),
            ("p", "<strong>Een bestelwagen is kapitaal</strong>: hij is gemaakt om mee te werken, niet om op "
                  "te gebruiken. <strong>Ondernemerschap is niet hetzelfde als arbeid</strong>: een werknemer "
                  "levert arbeid tegen een loon dat vastligt, een ondernemer combineert de factoren en weet "
                  "niet vooraf wat eruit komt."),
            ("weetje", "De winst is de vergoeding van de ondernemer, en net daarom is ze onzeker. Loon, rente "
                       "en huur worden afgesproken; wat er na alle kosten overblijft, is wat het is."),
        ]),
        dict(kop="Toegevoegde waarde en de bedrijfskolom", blokken=[
            ("p", "<strong>De toegevoegde waarde is de omzet min de aankopen</strong>: wat een onderneming "
                  "zelf toevoegt aan wat ze inkocht. <strong>Voor één schakel is dat de verkoopprijs min de "
                  "inkoopprijs.</strong>"),
            ("p", "<strong>Een bedrijfskolom, ook een productiekolom, is de weg van grondstof tot eindproduct</strong>, met al zijn "
                  "schakels, elk met zijn eigen bewerking. <strong>De oerproducent komt eerst</strong>: de "
                  "landbouwer of de mijn levert de grondstof. <strong>De consument staat aan het einde, niet "
                  "aan het begin.</strong>"),
            ("kader", tabel(["schakel", "koopt aan", "verkoopt aan", "voegt toe"],
                            [["<strong>de landbouwer</strong>", "—", "0,30 euro", "<strong>0,30 euro</strong>"],
                             ["<strong>de maalderij</strong>", "0,30 euro", "0,55 euro", "<strong>0,25 euro</strong>"],
                             ["<strong>de bakker</strong>", "0,55 euro", "1,60 euro", "<strong>1,05 euro</strong>"],
                             ["<strong>de winkel</strong>", "1,60 euro", "2,80 euro", "<strong>1,20 euro</strong>"]])),
            ("p", "<strong>De toegevoegde waarden van alle schakels samen zijn de verkoopprijs voor de "
                  "klant</strong>: 0,30 plus 0,25 plus 1,05 plus 1,20 is <strong>2,80 euro</strong>, en dat "
                  "is precies de prijs in de winkel. Elke schakel legt zijn deel erbij."),
            ("p", "<strong>Een onderneming die enkel doorverkoopt, voegt wél waarde toe</strong>: de winkel "
                  "maakt het brood niet, maar ze zorgt voor het transport, de voorraad, de spreiding over de "
                  "dag en het advies. Daarvoor betaalt de klant mee."),
        ]),
        dict(kop="De totale en de marginale productie", blokken=[
            ("p", "<strong>De totale productie is alles wat geproduceerd is</strong> bij een bepaald aantal "
                  "werkers. <strong>De marginale productie is wat één extra werker erbij maakt.</strong> De lijn van het eerste is de totale productiecurve, die van het tweede de marginale productiecurve, en het marginale heet ook het marginaal product of de marginale meeropbrengst."),
            ("p", "<strong>De wet van de toenemende meeropbrengsten zegt dat elke extra werker méér "
                  "bijbrengt dan de vorige</strong>: door samen te werken en zich te specialiseren halen ze "
                  "meer uit elke kracht. <strong>De wet van de afnemende meeropbrengsten zegt dat elke extra "
                  "werker mínder bijbrengt</strong>: de machines en de ruimte blijven gelijk, dus men zit "
                  "elkaar op den duur in de weg."),
            ("fig", svg.productiecurven([2, 5, 7, 8, 6, 4, 2, 0, -3]),
             "Boven wat er in totaal gemaakt wordt, onder wat elke extra werker erbij brengt. De vierde "
             "werker brengt er het meeste bij, de achtste niets meer, de negende maakt het slechter."),
            ("p", "In die tekening brengt de eerste werker er 2 bij, de vierde 8 en de zevende nog 2. "
                  "<strong>De totale productie klimt dus van 2 naar 34, en 34 is haar hoogste punt</strong>, "
                  "bij zeven en bij acht werkers. <strong>De achtste brengt niets meer bij</strong>, en "
                  "<strong>met de negende zakt het totaal naar 31</strong>."),
            ("p", "<strong>De totale productie kan nog stijgen terwijl de marginale productie daalt</strong>: "
                  "na de vierde werker brengt elke volgende minder bij, maar hij brengt nog altijd iets bij, "
                  "dus het totaal groeit nog, enkel met kleinere stappen. <strong>De marginale productie kan "
                  "wel negatief worden</strong>, en dan daalt het totaal."),
            ("p", "<strong>Het hoogste punt van de totale productie ligt waar de marginale productie nul "
                  "is.</strong> Zodra het marginale onder nul zakt, daalt het totaal. <strong>Wat vast blijft "
                  "bij deze wetten, is het kapitaal</strong>: het aantal machines, de grootte van het gebouw, "
                  "de beschikbare ruimte. <strong>Het aantal werkers is net wat verandert.</strong> "
                  "<strong>De meeropbrengst daalt niet omdat de nieuwe werkers slechter zijn</strong>, wel "
                  "omdat de vaste factoren niet meegroeien."),
        ]),
        dict(kop="Winst en volkomen concurrentie", blokken=[
            ("p", "<strong>Een onderneming produceert volgens de economie om winst te maken.</strong> "
                  "<strong>Winstmaximalisatie, ook winstmaximalisering of de winst maximaliseren, is het streven naar de hoogste winst</strong>, en dat is niet de grootste "
                  "productie en niet de hoogste omzet: je kan heel veel verkopen en er toch op verliezen."),
            ("p", "<strong>Volkomen concurrentie betekent veel kopers en veel verkopers</strong>, die allemaal "
                  "hetzelfde verkopen aan de marktprijs. Dat is de marktvorm die deze vakfiche bespreekt; je leest ze ook als volledige of perfecte concurrentie. <strong>Eén onderneming kan de prijs dan niet zelf "
                  "bepalen</strong>: ze is te klein tegenover de markt en moet de marktprijs aanvaarden."),
            ("p", "<strong>In volkomen concurrentie verkoopt niet elke onderneming een ánder product</strong>, "
                  "maar juist hetzelfde. Daarom kiest de klant op prijs, en daarom kan niemand meer vragen dan "
                  "de markt."),
        ]),
    ])


# ───────────────────────── 4. De kosten van de producent
zet("de-kosten-van-de-producent",
    titel="De kosten van de producent",
    onder="Constante en variabele kosten, de totale kosten en hun curve, de gemiddelde en de marginale kosten, waarom de gemiddelde kosten de vorm van een u hebben en waar de marginale kosten ze snijden.",
    secties=[
        dict(kop="Constante, variabele en totale kosten", blokken=[
            ("p", "<strong>De totale constante kosten blijven altijd gelijk</strong>: de huur van een loods "
                  "betaal je of je nu honderd of duizend stuks maakt. <strong>De totale variabele kosten "
                  "volgen de productie</strong>: meer stuks betekent meer grondstof, meer energie, meer "
                  "verpakking."),
            ("kader", tabel(["afkorting", "waarvoor", "voorbeelden"],
                            [["<strong>TCK</strong>", "<strong>totale constante kosten</strong>", "de huur van het gebouw, de verzekering, de afschrijving van een machine"],
                             ["<strong>TVK</strong>", "<strong>totale variabele kosten</strong>", "de grondstoffen, de verpakking, de energie van de machine"],
                             ["<strong>TK</strong>", "<strong>totale kosten</strong>", "<strong>TK is TCK plus TVK</strong>"]])),
            ("p", "<strong>De totale constante kosten stijgen niet als je meer produceert</strong>: ze blijven "
                  "precies gelijk, en dat is net wat constant betekent. <strong>Zonder productie zijn de "
                  "totale variabele kosten nul</strong>, want je koopt geen grondstof voor stuks die je niet "
                  "maakt. <strong>Maar bij nul stuks zijn de totale kosten niet nul</strong>: de huur, de "
                  "verzekering en de afschrijving lopen door."),
            ("p", "<strong>De curve van de TCK loopt vlak</strong>, een horizontale lijn op hetzelfde bedrag. "
                  "<strong>De curve van de TVK begint in de oorsprong en stijgt</strong> met de productie. "
                  "<strong>De curve van de TK begint bij de constante kosten</strong> en loopt parallel met "
                  "de TVK: <strong>het verschil tussen die twee curven is altijd precies de constante "
                  "kost</strong>."),
            ("p", "<strong>De variabele kosten lopen niet altijd even snel op</strong>, en dat komt van de "
                  "meeropbrengst uit het vorige hoofdstuk: zolang die stijgt, kost elk extra stuk minder; "
                  "zodra ze daalt, kost elk extra stuk meer."),
        ]),
        dict(kop="Gemiddelde en marginale kosten", blokken=[
            ("p", "De vakfiche noemt naast de totale kosten nog drie kostenbegrippen: de gemiddelde constante kosten, de gemiddelde variabele kosten en de marginale kosten. <strong>De gemiddelde kosten zijn de kosten per stuk</strong>: <strong>GK is TK gedeeld "
                  "door het aantal stuks</strong>. <strong>De gemiddelde variabele kosten zijn TVK gedeeld "
                  "door het aantal stuks</strong>, en de gemiddelde constante kosten TCK gedeeld door het "
                  "aantal stuks. <strong>GK is de som van GCK en GVK.</strong>"),
            ("p", "<strong>De marginale kosten zijn de kost van één extra stuk</strong>: hoeveel de totale "
                  "kosten stijgen als je er één stuk bij maakt. De afkorting is MK."),
            ("p", "<strong>De gemiddelde constante kosten dalen bij elke extra eenheid</strong>: hetzelfde "
                  "bedrag wordt over meer stuks verdeeld. <strong>De huur zelf verandert niet, enkel het deel "
                  "per stuk wordt kleiner.</strong> Bij een huur van 1 200 euro is dat <strong>6 euro per "
                  "stuk bij 200 stuks en 2 euro bij 600 stuks</strong>."),
            ("kader", tabel(["stuks", "TK", "GK = TK ÷ stuks"],
                            [["200", "2 300 euro", "<strong>11,50 euro</strong>"],
                             ["300", "3 075 euro", "<strong>10,25 euro</strong>"],
                             ["400", "4 000 euro", "<strong>10,00 euro</strong>"],
                             ["500", "5 075 euro", "<strong>10,15 euro</strong>"],
                             ["600", "6 300 euro", "<strong>10,50 euro</strong>"]])),
            ("p", "<strong>De gemiddelde kosten dalen dus niet altijd</strong>: hier dalen ze tot 10 euro bij "
                  "400 stuks en stijgen ze daarna weer. <strong>Daarom heeft de curve van de gemiddelde "
                  "kosten de vorm van een u</strong>: eerst dalend doordat de vaste kosten over meer stuks "
                  "gespreid worden, dan stijgend doordat de meeropbrengsten afnemen en elk extra stuk meer "
                  "kost."),
            ("fig", svg.kostencurven(),
             "De gemiddelde totale kost, de gemiddelde variabele kost en de marginale kost. De marginale "
             "kost snijdt de gemiddelde totale kost in haar laagste punt."),
            ("p", "<strong>De marginale kosten dalen ook niet altijd</strong>: ook zij hebben de vorm van een "
                  "u, maar ze bereiken hun laagste punt eerder. <strong>De marginale kosten snijden de "
                  "gemiddelde kosten precies in het laagste punt van de gemiddelde kosten, in hun minimum.</strong> In de "
                  "tabel hierboven is dat bij 400 stuks: <strong>het 401ste stuk kost ongeveer 10 euro, en "
                  "10 euro is daar ook het gemiddelde</strong>."),
            ("weetje", "Dat snijpunt is geen toeval. Kost een extra stuk mínder dan het gemiddelde, dan trekt "
                       "het het gemiddelde naar beneden. Kost het méér, dan trekt het het gemiddelde omhoog. "
                       "Het gemiddelde is dus het laagst op het ogenblik dat de marginale kost er precies "
                       "gelijk aan is.")   ,
            ("p", "<strong>Dalende gemiddelde kosten betekenen dat elk stuk minder kost</strong>: bij dezelfde "
                  "verkoopprijs blijft er per stuk meer over. <strong>Samen met de opbrengsten zeggen de "
                  "kostencurven hoeveel produceren loont</strong>, en dat is de optimale productiegrootte uit "
                  "het volgende hoofdstuk."),
        ]),
    ])


# ───────────────────────── 5. Opbrengsten, optimale productiegrootte en aanbod
zet("opbrengsten-optimale-productiegrootte-en-aanbod",
    titel="Opbrengsten, optimale productiegrootte en aanbod",
    onder="De totale, gemiddelde en marginale opbrengst, de optimale productiegrootte waar MO gelijk is aan MK, het verschil tussen omzet en winst, en hoe de aanbodcurve uit de marginale kosten volgt.",
    secties=[
        dict(kop="De drie opbrengsten", blokken=[
            ("p", "De vakfiche noemt drie opbrengstbegrippen. <strong>De totale opbrengst is prijs maal aantal</strong>: de verkoopprijs maal het aantal "
                  "verkochte stuks. <strong>De gemiddelde opbrengst is de opbrengst per stuk</strong>, en "
                  "<strong>de marginale opbrengst is de opbrengst van één extra stuk</strong>."),
            ("p", "<strong>Bij volkomen concurrentie liggen die laatste twee allebei gelijk aan de "
                  "prijs</strong>: elk stuk, ook het extra stuk, gaat weg aan dezelfde marktprijs. "
                  "<strong>De gemiddelde opbrengst daalt er dus niet als je meer verkoopt</strong>: de prijs "
                  "staat vast, dus de opbrengst per stuk blijft dezelfde."),
            ("p", "<strong>Bij een vaste prijs is de curve van de totale opbrengsten een stijgende "
                  "rechte</strong>: elk extra stuk brengt hetzelfde bedrag op, dus de lijn klimt gelijkmatig. "
                  "<strong>Op de assen van een opbrengstencurve staan de euro's verticaal en de hoeveelheid horizontaal.</strong>"),
        ]),
        dict(kop="De optimale productiegrootte", blokken=[
            ("p", "<strong>De winst is de opbrengst min de kosten</strong>; is het verschil negatief, dan is "
                  "er verlies. <strong>De optimale productiegrootte is de hoeveelheid waarbij de winst het "
                  "grootst is</strong>, en <strong>ze ligt waar de marginale opbrengst gelijk is aan de "
                  "marginale kost</strong>."),
            ("p", "De reden is eenvoudig. <strong>Is de marginale opbrengst hoger dan de marginale kost, dan "
                  "moet je méér produceren</strong>: dat extra stuk voegt nog winst toe. <strong>Is de "
                  "marginale kost hoger, dan moet je minder produceren</strong>: dat stuk kost meer dan het "
                  "opbrengt en eet van de winst."),
            ("p", "Neem de onderneming uit het vorige hoofdstuk, met een huur van 1 200 euro, en een prijs "
                  "van 13 euro per stuk."),
            ("kader", tabel(["stuks", "TO", "TK", "winst"],
                            [["400", "5 200 euro", "4 000 euro", "1 200 euro"],
                             ["500", "6 500 euro", "5 075 euro", "1 425 euro"],
                             ["600", "7 800 euro", "6 300 euro", "<strong>1 500 euro</strong>"],
                             ["700", "9 100 euro", "7 675 euro", "1 425 euro"],
                             ["800", "10 400 euro", "9 200 euro", "1 200 euro"]])),
            ("p", "<strong>De winst is het grootst bij 600 stuks, en daar is ze 1 500 euro.</strong> "
                  "<strong>Het 601ste stuk kost ongeveer 13 euro en brengt ook 13 euro op</strong>: precies "
                  "het punt waar MO en MK gelijk zijn. <strong>Daar is het verschil tussen TO en TK ook het "
                  "grootst</strong>, en dat is dezelfde zaak in andere woorden."),
            ("p", "<strong>De winst is dus niet het grootst waar de productie het grootst is</strong>: bij 800 "
                  "stuks verkoopt deze onderneming meer en houdt ze minder over. <strong>Voorbij het optimum "
                  "daalt de winst</strong>, want elk stuk erbij kost meer dan het opbrengt."),
            ("p", "<strong>Je vindt het optimum op drie manieren</strong>: grafisch waar MO en MK snijden, "
                  "rekenkundig met een tabel zoals hierboven, of door te zoeken waar het verschil tussen TO "
                  "en TK het grootst is. <strong>De hoogste omzet is niet de hoogste winst</strong>, want de "
                  "kosten lopen mee op."),
            ("weetje", "Dat is ook het antwoord op de vraag waarom een onderneming met een hoge omzet toch "
                       "verlies kan maken. <strong>De omzet is alles wat binnenkomt, de winst is wat er na de "
                       "kosten overblijft</strong>; omzet en winst zijn geen twee woorden voor hetzelfde."),
        ]),
        dict(kop="Van optimum naar aanbodcurve", blokken=[
            ("p", "<strong>Stijgt de prijs, dan wordt de optimale productiegrootte groter</strong>: de "
                  "marginale opbrengst gaat omhoog, dus produceren loont langer. Bij dezelfde onderneming is "
                  "<strong>600 stuks het optimum bij 13 euro en 800 stuks bij 16 euro</strong>. "
                  "<strong>Daalt de prijs, dan wordt het optimum kleiner</strong>: het snijpunt met de "
                  "marginale kosten schuift naar links."),
            ("p", "<strong>Stijgen de kosten bij een gelijke prijs, dan wordt er minder gemaakt</strong>: de "
                  "marginale kostencurve schuift omhoog en snijdt de opbrengst eerder."),
            ("p", "<strong>De individuele aanbodcurve is wat één verkoper aanbiedt</strong> bij elke prijs, en "
                  "<strong>ze loopt stijgend</strong>: bij een hogere prijs loont het om ook de duurdere "
                  "extra stuks nog te maken. <strong>Ze loopt dus niet dalend zoals de vraagcurve.</strong>"),
            ("p", "<strong>De aanbodcurve is het stijgende stuk van de marginale kostencurve</strong>: bij "
                  "elke prijs produceert hij tot MO gelijk is aan MK, en dat punt ligt op het stijgende deel. "
                  "<strong>Wat hij aanbiedt, hangt af van de marktprijs, van zijn marginale kosten en van "
                  "zijn productiemogelijkheden</strong>; de voorkeuren van de klant zitten in de vraagcurve, "
                  "niet hier."),
            ("p", "<strong>De collectieve aanbodcurve, ook het collectief aanbod of het marktaanbod, is al het aanbod samen</strong>: bij elke prijs tel je "
                  "de aangeboden hoeveelheden van alle producenten op. <strong>Eén producent met hogere "
                  "kosten verandert de marktprijs niet</strong>; hij biedt enkel zelf minder aan."),
            ("fig", svg.marktevenwicht(),
             "De vraag en het aanbod komen op de markt samen in het evenwichtspunt E: daar is de gevraagde "
             "hoeveelheid gelijk aan de aangeboden hoeveelheid."),
        ]),
    ])


# ───────────────────────── 6. Soorten ondernemingen en hun verplichtingen
zet("soorten-ondernemingen-en-hun-verplichtingen",
    titel="Soorten ondernemingen en hun verplichtingen",
    onder="Natuurlijke en rechtspersonen, beperkte en onbeperkte aansprakelijkheid, de eenmanszaak tegenover de bv en de nv, en wat elk van hen aan oprichting, boekhouding en belasting moet doen.",
    secties=[
        dict(kop="Persoon en aansprakelijkheid", blokken=[
            ("p", "<strong>Een natuurlijk persoon is een mens</strong> van vlees en bloed, met rechten en "
                  "plichten. <strong>Een rechtspersoon is een eigen juridische figuur</strong>: een "
                  "vennootschap of een vzw. <strong>Hij heeft eigen bezit, kan zelf schulden hebben, kan "
                  "dagvaarden en gedagvaard worden en blijft bestaan los van zijn oprichters.</strong>"),
            ("p", "<strong>Onbeperkte aansprakelijkheid betekent dat ook je eigen bezit instaat</strong>: een "
                  "schuldeiser kan aan je woning of je spaargeld. <strong>Beperkte aansprakelijkheid betekent "
                  "dat enkel je inbreng instaat</strong>: je verliest maximaal wat je in de vennootschap "
                  "stopte. <strong>Het bezit dat buiten de onderneming valt, is het "
                  "privévermogen.</strong>"),
            ("p", "<strong>De eenmanszaak heeft geen eigen rechtspersoonlijkheid</strong>: de zaak en de "
                  "persoon zijn één. <strong>Daarom kan een schuldeiser er ook aan het privévermogen.</strong> "
                  "<strong>Een bv is geen natuurlijk persoon</strong> maar een rechtspersoon, met een eigen "
                  "vermogen los van de oprichters."),
        ]),
        dict(kop="De drie vormen vergeleken", blokken=[
            ("p", "<strong>Bv staat voor besloten vennootschap</strong>, besloten omdat de aandelen niet vrij "
                  "verhandeld worden. <strong>Nv staat voor naamloze vennootschap</strong>, naamloos omdat de "
                  "aandeelhouders niet in de naam staan."),
            ("p", "<strong>De vakfiche vergelijkt de ondernemingsvormen op de aansprakelijkheid, de administratie en de "
                  "fiscaliteit</strong>, en daarnaast ook op de oprichtingsakte, het kapitaal en de "
                  "overdraagbaarheid van de aandelen."),
            ("kader", tabel(["", "eenmanszaak", "bv", "nv"],
                            [["<strong>rechtspersoon</strong>", "nee", "ja", "ja"],
                             ["<strong>aansprakelijkheid</strong>", "<strong>onbeperkt</strong>", "beperkt tot de inbreng", "beperkt tot de inbreng"],
                             ["<strong>oprichtingsakte</strong>", "<strong>geen notaris nodig</strong>", "notariële akte", "notariële akte"],
                             ["<strong>minimumkapitaal</strong>", "geen", "<strong>geen vast bedrag</strong>", "<strong>een wettelijk minimum</strong>"],
                             ["<strong>aandelen</strong>", "—", "moeilijk overdraagbaar", "in principe vrij overdraagbaar"],
                             ["<strong>boekhouding</strong>", "vereenvoudigd mag, onder een omzetgrens", "dubbele boekhouding", "dubbele boekhouding"],
                             ["<strong>belasting op de winst</strong>", "<strong>personenbelasting</strong>", "vennootschapsbelasting", "vennootschapsbelasting"]])),
            ("p", "<strong>Eén oprichter volstaat, zowel voor een bv als voor een nv.</strong> Sinds de "
                  "hervorming van het vennootschapsrecht kan ook een nv alleen opgericht worden."),
            ("p", "<strong>Een bv heeft geen vast minimumkapitaal</strong>, wel een toereikend "
                  "aanvangsvermogen dat je in een financieel plan verantwoordt. <strong>De nv is de vennootschapsvorm die wel nog "
                  "een wettelijk minimumkapitaal heeft.</strong> Haar notariële akte heet ook een authentieke akte."),
            ("p", "<strong>Dat een bv besloten is, betekent dat aandelen er moeilijk weg gaan</strong>: de "
                  "overdracht is beperkt, meestal met de toestemming van de anderen, want de aandeelhouders "
                  "kiezen zelf wie erbij komt. <strong>De aandelen van een nv zijn in principe vrij "
                  "overdraagbaar</strong>, en daarom is de nv de vorm voor wie geld bij veel investeerders wil "
                  "ophalen."),
        ]),
        dict(kop="Kiezen tussen de vormen", blokken=[
            ("p", "<strong>Het voordeel van een eenmanszaak is dat ze snel opgericht is</strong>: geen "
                  "notaris, geen kapitaal, weinig formaliteiten. Je schrijft je in bij een ondernemingsloket "
                  "en vraagt een ondernemingsnummer aan. <strong>Daarom past ze bij wie alleen en klein wil "
                  "beginnen.</strong>"),
            ("p", "<strong>Haar grootste nadeel is dat je bezit instaat</strong>: de onbeperkte "
                  "aansprakelijkheid. <strong>Daarom kiest iemand voor een vorm met beperkte "
                  "aansprakelijkheid</strong>: gaat de zaak slecht, dan blijft het privévermogen in principe "
                  "buiten schot."),
            ("p", "<strong>De voordelen van een bv tegenover een eenmanszaak zijn de beperkte "
                  "aansprakelijkheid, de eigen rechtspersoon en het gemak om partners erbij te nemen.</strong> "
                  "<strong>De administratie is juist zwaarder</strong>: een dubbele boekhouding en een "
                  "jaarrekening."),
            ("p", "<strong>Een bv en een nv maken jaarlijks een jaarrekening op, leggen die neer bij de "
                  "Nationale Bank en betalen vennootschapsbelasting.</strong> <strong>Bij een eenmanszaak komt "
                  "de winst bij het inkomen van de zaakvoerder en valt ze onder de "
                  "personenbelasting.</strong>"),
            ("p", "<strong>Voor de schulden van een nv is de vennootschap zelf aansprakelijk</strong>; de "
                  "aandeelhouders riskeren enkel hun inbreng, en <strong>een aandeelhouder van een bv "
                  "verliest maximaal zijn inbreng</strong>. <strong>Een zaakvoerder van een bv is normaal niet "
                  "met zijn privévermogen aansprakelijk</strong>, tenzij hij een zware fout maakt of de "
                  "vennootschap te licht liet starten."),
            ("p", "<strong>Een nv verschilt van een bv in het minimumkapitaal, in de overdraagbaarheid van de "
                  "aandelen en in de naam van de vorm.</strong> <strong>In beide gevallen is de "
                  "aansprakelijkheid beperkt tot de inbreng</strong>; dat is net wat ze gemeen hebben."),
        ]),
    ])


# ───────────────────────── 7. De organisatiestructuur van een onderneming
zet("de-organisatiestructuur-van-een-onderneming",
    titel="De organisatiestructuur van een onderneming",
    onder="De vier structuren uit de vakfiche met hun voor- en nadelen, hoe je een organogram leest, en de drie pijlers van maatschappelijk verantwoord ondernemen.",
    secties=[
        dict(kop="Vier structuren", blokken=[
            ("p", "<strong>Een organisatiestructuur is hoe het werk verdeeld is</strong>: wie wat doet, wie "
                  "aan wie leiding geeft en hoe de afdelingen samenwerken. <strong>De vakfiche noemt vier "
                  "organisatiestructuren</strong>: de functionele, de lijn-, de lijnstaf- en de horizontale organisatie."),
            ("kader", tabel(["structuur", "wat ze is", "voordeel", "nadeel"],
                            [["<strong>functioneel</strong>", "<strong>per taak ingedeeld</strong>: aankoop, verkoop, boekhouding, elk met een eigen chef", "<strong>veel vakkennis</strong>: elke chef kent zijn vakgebied door en door", "<strong>tegenstrijdige orders</strong>: twee chefs kunnen iets anders vragen"],
                             ["<strong>lijn</strong>, de lijnstructuur", "<strong>één chef per persoon</strong>, de bevelen lopen in een rechte lijn van boven naar onder", "duidelijk wie beslist", "weinig specialisten aan de top"],
                             ["<strong>lijnstaf</strong>", "<strong>de lijn met adviseurs erbij</strong>", "vakkennis beschikbaar zonder de lijn te doorbreken", "de staf kost geld en beslist niet"],
                             ["<strong>horizontaal</strong>", "<strong>weinig niveaus</strong> tussen boven en onder, ook een platte organisatie genoemd", "<strong>snel beslissen</strong>", "veel verantwoordelijkheid op de werkvloer"]])),
            ("p", "<strong>In een functionele organisatie kan een medewerker meerdere chefs hebben</strong>: "
                  "elke functionele chef beslist over zijn vakgebied, en dat kan verwarring geven. "
                  "<strong>In een lijnorganisatie heeft iedereen precies één chef.</strong>"),
            ("p", "<strong>Een lijnorganisatie en een lijnstaforganisatie zijn niet hetzelfde</strong>: bij de "
                  "tweede komt er een adviserende staf naast de lijn. <strong>De staf geeft geen bevelen aan "
                  "de werkvloer</strong>, hij adviseert de lijn, en de lijnchefs beslissen. Die adviesgroep naast de lijn is de staf, of de stafdienst. Net dat "
                  "niet-bevelen is het kenmerk van deze vorm."),
            ("p", "<strong>Veel niveaus heeft als nadeel dat beslissen lang duurt</strong>: elke vraag moet "
                  "eerst de hele lijn omhoog en weer naar beneden. <strong>Daarbij raakt informatie onderweg "
                  "kwijt en voelen medewerkers zich ver van de top.</strong> Vakkennis is er juist veel; het "
                  "probleem zit in de afstand."),
            ("p", "<strong>Je kiest een structuur op de grootte van de zaak, op de aard van het werk en op "
                  "hoeveel specialisten er nodig zijn.</strong> Een kleine zaak heeft geen staf nodig; "
                  "<strong>een grote fabriek met specialisten past bij de functionele structuur</strong>, "
                  "waar elke specialist zijn eigen vakgebied leidt."),
        ]),
        dict(kop="Het organogram lezen", blokken=[
            ("p", "<strong>Een organogram, ook een organigram, is een schema van de zaak</strong>: het toont de afdelingen en wie "
                  "aan wie leiding geeft. <strong>Bovenaan staat de leiding</strong>, de directie of de "
                  "zaakvoerder."),
            ("fig", svg.organogram(["aankoop", "verkoop", "administratie|en boekhouding", "expeditie|en logistiek"],
                                   staf="kwaliteitszorg|(staf)"),
             "Een organogram met drie niveaus. De directie geeft leiding aan de vier afdelingen; de "
             "kwaliteitszorg hangt er met een stippellijn naast."),
            ("p", "<strong>Een verticale lijn is een gezagslijn</strong>: wie boven staat, geeft leiding aan "
                  "wie eronder hangt. <strong>Een stippellijn naar een vakje naast de lijn is een "
                  "adviesrelatie</strong>, en zo staat de staf erbij."),
            ("p", "<strong>Naast de afdelingen zie je dus de hiërarchie</strong>: wie aan wie verantwoording "
                  "geeft. <strong>Je leidt dat af door de lijn naar boven te volgen tot het eerste "
                  "vakje.</strong> <strong>Uit een organogram lees je wie leiding geeft aan wie, welke "
                  "afdelingen er zijn en hoeveel niveaus er zijn.</strong>"),
            ("p", "<strong>Een organogram zegt niet hoeveel omzet elke afdeling maakt</strong>: het toont de "
                  "structuur, geen cijfers. Die staan in de jaarrekening. <strong>Een plat organogram heeft "
                  "weinig niveaus</strong>, vaak maar twee of drie, van de zaakvoerder tot de werkvloer."),
        ]),
        dict(kop="Maatschappelijk verantwoord ondernemen", blokken=[
            ("p", "<strong>Maatschappelijk verantwoord ondernemen is rekening houden met allen</strong>: mens, "
                  "milieu en winst samen afwegen bij elke beslissing. <strong>MVO heeft drie pijlers: people, "
                  "planet en profit.</strong>"),
            ("kader", tabel(["pijler", "waarover het gaat", "voorbeeld"],
                            [["<strong>people</strong>", "<strong>de mensen</strong>: de werknemers, de klanten en de buurt rond de onderneming", "<strong>veilig werk geven</strong>, opleiding, gelijke kansen, een leefbaar loon"],
                             ["<strong>planet</strong>", "<strong>het milieu</strong>", "afval, energie, grondstoffen en uitstoot"],
                             ["<strong>profit</strong>", "<strong>de winst</strong>", "genoeg overhouden om te blijven bestaan en te investeren"]])),
            ("p", "<strong>Bij MVO weegt een onderneming die drie samen af.</strong> Een beslissing die goed "
                  "is voor één pijler en slecht voor de twee andere, is geen goede beslissing. <strong>Je "
                  "beoordeelt een organisatie dus op de drie pijlers naast elkaar.</strong>"),
            ("p", "<strong>MVO betekent niet dat een onderneming geen winst mag maken.</strong> Profit is een "
                  "van de drie pijlers; zonder winst bestaat de zaak niet lang, en dan is er ook voor de "
                  "mensen en voor het milieu niets meer te doen."),
        ]),
    ])


# ───────────────────────── 8. De afdelingen en hun samenwerking
zet("de-afdelingen-en-hun-samenwerking",
    titel="De afdelingen en hun samenwerking",
    onder="Wat elke afdeling doet, waarom de taken altijd bestaan ook zonder aparte afdeling, en hoe de informatie en de documenten tussen de afdelingen lopen bij één verkoop.",
    secties=[
        dict(kop="Wie doet wat", blokken=[
            ("p", "<strong>De vakfiche noemt zeven afdelingen</strong>, en je moet van elk kunnen zeggen wat "
                  "ze doet en wat ze niet doet."),
            ("kader", tabel(["afdeling", "wat ze doet"],
                            [["<strong>aankoop</strong>", "<strong>goederen inkopen</strong>: leveranciers zoeken, prijzen, levertijden en kwaliteit vergelijken en bestellen"],
                             ["<strong>verkoop</strong>", "<strong>klanten bedienen</strong>: offertes maken, bestellingen opnemen en klanten opvolgen"],
                             ["<strong>administratie en boekhouding</strong>", "<strong>de cijfers bijhouden</strong>: facturen boeken en opmaken, de btw-aangifte doen en de jaarrekening voorbereiden"],
                             ["<strong>marketing</strong>", "<strong>de markt bewerken</strong>: onderzoeken wat de klant wil en het product, de prijs, de plaats en de promotie bepalen"],
                             ["<strong>HR, human resources of de personeelsdienst</strong>", "<strong>het personeel</strong>: aanwerven, opleidingen regelen en de loonadministratie opvolgen"],
                             ["<strong>IT of informatica</strong>", "<strong>de techniek verzorgen</strong>: computers, netwerk, software en de beveiliging van de gegevens"],
                             ["<strong>expeditie en logistiek</strong>", "<strong>de goederenstroom</strong>: ontvangen, opslaan, picken, verzenden en het transport plannen"],
                             ["<strong>research and development</strong>", "<strong>nieuwe producten zoeken</strong>: onderzoek en ontwikkeling van nieuwe producten en betere werkwijzen"]])),
            ("p", "<strong>HR staat voor human resources</strong>, de mensen van de onderneming; HR volgt hun "
                  "instroom, doorstroom en uitstroom op. <strong>De IT-afdeling zorgt niet voor de "
                  "boekhouding</strong>: zij zorgt voor de systemen, de boekhouding gebruikt ze. <strong>De "
                  "facturen voor de klanten maakt de boekhouding</strong>, met de gegevens die de verkoop "
                  "doorgeeft. <strong>De reclamecampagne bedenkt de marketing</strong>; promotie is een van de "
                  "vier P's van de marketingmix."),
            ("p", "<strong>Een kleine zaak kan al die taken bij één of twee mensen leggen.</strong> De taken "
                  "bestaan altijd; of er een aparte afdeling voor is, hangt van de grootte af. <strong>Niet "
                  "elke onderneming heeft dus alle afdelingen apart</strong>: een zaak met drie werknemers "
                  "heeft geen eigen IT- of R&amp;D-afdeling. En een raad van bestuur is geen afdeling."),
        ]),
        dict(kop="Waarom ze elkaar nodig hebben", blokken=[
            ("p", "<strong>Afdelingen moeten samenwerken omdat het werk samenhangt</strong>: één verkoop raakt "
                  "de verkoop, de logistiek en de boekhouding. <strong>Geen enkele afdeling kan volledig op "
                  "haar eigen werken</strong>, want elke afdeling heeft gegevens van de andere nodig."),
            ("p", "<strong>Het doorgeven van informatie tussen afdelingen is communicatie of overleg</strong>, "
                  "en <strong>de reeks documenten die daarbij doorgaat, is de documentenstroom</strong>, ook de documentstroom of de informatiedoorstroming genoemd."),
            ("fig", svg.stappen(["de klant|bestelt", "verkoop neemt|de bestelling op",
                                 "logistiek pickt|en verzendt", "boekhouding|factureert"]),
             "Bij één verkoop lopen drie afdelingen achter elkaar: de verkoop, de logistiek en de "
             "boekhouding."),
            ("kader", tabel(["van", "naar", "wat er doorgaat"],
                            [["<strong>verkoop</strong>", "<strong>logistiek</strong>", "<strong>de bestelling</strong>, zodat de goederen gepickt en verzonden kunnen worden: bestelbonnen, leverbonnen en de afspraken over de levertijd"],
                             ["<strong>verkoop</strong>", "<strong>boekhouding</strong>", "<strong>de gegevens om te factureren</strong>: wie wat kocht, aan welke prijs en met welke korting"],
                             ["<strong>logistiek</strong>", "<strong>aankoop</strong>", "<strong>dat de voorraad laag is</strong>, want voorraadbeheer is werk voor de logistiek"],
                             ["<strong>marketing</strong>", "<strong>verkoop</strong>", "wat de klant wil en wat er in de actie zit, want dat bepaalt het verkoopgesprek"],
                             ["<strong>marketing</strong>", "<strong>R&amp;D</strong>", "wat de klant wil, want een product dat niemand wil, is ook technisch geen succes"],
                             ["<strong>alle afdelingen</strong>", "<strong>HR</strong>", "welke functies vrijkomen, welke prestaties geleverd zijn en welke opleidingen nodig zijn"]])),
            ("p", "<strong>Loonfiches lopen tussen HR en de boekhouding</strong>, niet tussen verkoop en "
                  "logistiek, en de klantenlijst is werk voor de verkoop, niet voor HR. <strong>IT werkt voor "
                  "alle afdelingen</strong>, want van het kassasysteem tot de boekhoudsoftware loopt alles "
                  "over hun netwerk. <strong>De boekhouding staat dus niet los van de rest</strong>: elke "
                  "aankoop, verkoop en loonbetaling komt bij haar terecht."),
            ("p", "<strong>Een fout in de aankoop kan de verkoop stilleggen</strong>: zonder goederen in huis "
                  "valt er niets te leveren. <strong>Weet de logistiek niet wat verkocht is, dan loopt de "
                  "levering mis</strong>, met verkeerde of te late leveringen en een ontevreden klant. "
                  "<strong>Slechte communicatie geeft fouten en vertraging</strong>: dubbel werk, verkeerde "
                  "leveringen en klachten."),
            ("p", "<strong>Daarom bespreekt een onderneming haar cijfers met alle chefs: om samen bij te "
                  "sturen.</strong> Elke afdeling ziet dan wat haar werk met het geheel doet. <strong>En een "
                  "goede samenwerking helpt de klant sneller</strong>: zijn bestelling raakt zonder omwegen "
                  "van de verkoop tot aan zijn deur."),
        ]),
    ])


# ───────────────────────── 9. Werving, selectie en de werkplek
zet("werving-selectie-en-de-werkplek",
    titel="Werving, selectie en de werkplek",
    onder="De vacature, het cv en de sollicitatiebrief, het verschil tussen een functiebeschrijving en een functieprofiel, de stappen van een selectieprocedure, en een werkplek die veilig, ergonomisch en hygiënisch is.",
    secties=[
        dict(kop="De vacature en het profiel", blokken=[
            ("p", "<strong>Een vacature is een open functie</strong>: een plaats die vrij is en waarvoor de "
                  "onderneming iemand zoekt. Het bericht waarin ze dat aankondigt, heet ook een vacature, of een vacaturebericht."),
            ("p", "<strong>Een functiebeschrijving zegt wat de job inhoudt</strong>: de taken, de "
                  "verantwoordelijkheden en de plaats in de organisatie. <strong>Een functieprofiel zegt wie "
                  "je ervoor zoekt.</strong> <strong>De beschrijving gaat dus over de job, het profiel over "
                  "de persoon.</strong>"),
            ("kader", tabel(["wat er in een vacature hoort", "waarom"],
                            [["<strong>de functiebeschrijving</strong>", "zodat een kandidaat weet wat hij zal doen"],
                             ["<strong>het gevraagde opleidingsniveau</strong>", "het diploma dat de job vraagt"],
                             ["<strong>de gevraagde ervaring</strong>", "<strong>ervaring is wat je al deed, het opleidingsniveau is het diploma</strong>: dat zijn twee verschillende dingen"],
                             ["<strong>de kennis en de vaardigheden</strong>", "<strong>een vaardigheid is iets dat je kan</strong>: een rekenblad gebruiken"],
                             ["<strong>de attitudes</strong>", "<strong>een attitude is een houding</strong>: punctueel zijn, vriendelijk blijven, kunnen samenwerken"],
                             ["<strong>het aanbod en de verloning</strong>", "<strong>dat hoort er net wel in</strong>, anders solliciteert niemand"]])),
            ("p", "<strong>Een onderneming stelt een duidelijk profiel op om beter te kunnen kiezen</strong>: "
                  "met een duidelijk profiel kan je elke kandidaat op dezelfde punten afwegen."),
        ]),
        dict(kop="Solliciteren en selecteren", blokken=[
            ("p", "<strong>Een cv is een overzicht van iemand</strong>: een curriculum vitae, je levensloop, met de opleiding, "
                  "de werkervaring en de vaardigheden, op één of twee bladzijden. <strong>Een cv hoort kort en "
                  "overzichtelijk te zijn</strong>, want wie tientallen cv's doorneemt, heeft er per cv maar "
                  "een minuut voor. <strong>Je rekeningnummer geef je pas als je aangeworven bent.</strong>"),
            ("p", "<strong>Een sollicitatiebrief is je motivatie op papier</strong>: waarom jij de job wil en "
                  "waarom je erbij past. <strong>Het gesprek waarin je jezelf voorstelt, is een "
                  "sollicitatiegesprek of een selectiegesprek.</strong>"),
            ("fig", svg.stappen(["de vacature|opstellen", "bekendmaken", "de cv's|screenen",
                                 "gesprekken|voeren"]),
             "De stappen van een eenvoudige selectieprocedure. De loonfiche komt pas maanden later, als "
             "iemand al in dienst is."),
            ("p", "<strong>De eerste stap is de vacature opstellen</strong>: eerst weten wie je zoekt, dan "
                  "pas bekendmaken. <strong>Na het bekijken van de cv's volgen de gesprekken</strong>: de "
                  "geselecteerde kandidaten worden uitgenodigd. <strong>Een cv beoordeel je op de "
                  "vacature</strong>: je legt het profiel van de vacature naast wat de kandidaat aanbiedt."),
        ]),
        dict(kop="De werkplek: veilig, ergonomisch, hygiënisch", blokken=[
            ("p", "<strong>De vakfiche beoordeelt een werkplek op veiligheid, op ergonomie en op "
                  "hygiëne</strong>. Die drie samen bepalen of iemand er gezond kan werken."),
            ("p", "<strong>Ergonomie is het aanpassen van de werkplek aan de mens</strong>: de werkplek past "
                  "zich aan het lichaam aan, niet omgekeerd. <strong>Een ergonomische werkplek heeft een "
                  "regelbare stoel, het scherm op ooghoogte en genoeg ruimte voor je benen.</strong>"),
            ("kader", tabel(["waarover", "hoe het hoort"],
                            [["<strong>het scherm</strong>", "<strong>op ooghoogte</strong>: de bovenkant ongeveer ter hoogte van je ogen, op armlengte afstand"],
                             ["<strong>de bureaustoel</strong>", "<strong>voeten plat op de grond</strong>, knieën ongeveer in een rechte hoek, rug tegen de steun"],
                             ["<strong>de houding</strong>", "<strong>afwisselen tussen zitten en staan</strong>, want lang in dezelfde houding zitten is wat de klachten geeft"],
                             ["<strong>het licht en de verlichting</strong>", "<strong>genoeg licht geeft minder fouten en minder moeite</strong>; slecht licht geeft vermoeide ogen en hoofdpijn"],
                             ["<strong>tillen</strong>", "<strong>door je knieën zakken</strong>, rug recht, last dicht bij je lichaam, en met je voeten meedraaien in plaats van met je rug"]])),
            ("p", "<strong>Een zware doos til je dus niet met een gebogen rug.</strong> En <strong>je wisselt "
                  "taken af op een werkdag om niet stijf te worden</strong>: afwisseling spaart je rug, je nek "
                  "en je ogen."),
            ("p", "<strong>Een hygiënische werkplek is schoon</strong>, zeker waar met voeding of met mensen "
                  "gewerkt wordt: <strong>een propere werktafel, handen wassen waar nodig en afval meteen "
                  "opruimen</strong>. De stoel hoort bij de ergonomie, niet bij de hygiëne."),
            ("p", "<strong>Een risicoanalyse is de gevaren opsporen</strong>: je gaat na wat er kan mislopen "
                  "en neemt vooraf maatregelen. <strong>Een veiligheidsschoen in een loods beschermt je "
                  "tenen</strong>, want een stalen neus houdt een vallende doos of een rolwagen tegen."),
            ("p", "<strong>Beschermingsmiddelen zijn niet vrijblijvend</strong>: de werkgever moet ze geven en "
                  "de werknemer moet ze gebruiken. <strong>Een arbeidsongeval of werkongeval is een ongeval dat tijdens het "
                  "werk gebeurt, en je meldt het meteen</strong>: de werkgever moet het aangeven bij de "
                  "arbeidsongevallenverzekering. <strong>Die verzekering is verplicht en moet in orde zijn "
                  "vóór de eerste werknemer begint.</strong>"),
        ]),
    ])


# ───────────────────────── 10. Aanwerving en de arbeidsovereenkomst
zet("aanwerving-en-de-arbeidsovereenkomst",
    titel="Aanwerving en de arbeidsovereenkomst",
    onder="De DIMONA-aangifte, wat een arbeidsovereenkomst is en waarom het gezag erin de kern is, de soorten overeenkomsten naar duur, omvang en soort werk, de verplichte vermeldingen en de rechten en plichten van beide partijen.",
    secties=[
        dict(kop="Wat er in orde moet zijn", blokken=[
            ("p", "<strong>Bij de aanwerving van personeel moeten drie dingen in orde zijn: de "
                  "DIMONA-aangifte, de arbeidsongevallenverzekering en een arbeidsovereenkomst.</strong>"),
            ("p", "<strong>Een DIMONA-aangifte is melden wie begint</strong>: de werkgever meldt elektronisch "
                  "aan de RSZ, de Rijksdienst voor Sociale Zekerheid, wie in dienst komt en wie uit dienst "
                  "gaat. <strong>Ze moet gebeuren vóór het werk begint</strong>, uiterlijk op het moment dat "
                  "de werknemer begint, niet erna."),
            ("p", "<strong>Zonder DIMONA-aangifte mag niemand beginnen werken.</strong> Dat is zwartwerk, met "
                  "zware boetes voor de werkgever. De RSZ stuurt daarna een afrekening van de bijdragen; je "
                  "factureert haar niets."),
        ]),
        dict(kop="Soorten arbeidsovereenkomsten", blokken=[
            ("p", "<strong>Een arbeidsovereenkomst is een contract met de baas</strong>: je werkt tegen loon "
                  "en onder het gezag van de werkgever. <strong>De vakfiche onderscheidt ze op de duur, op de "
                  "omvang van de prestaties en op het soort werk.</strong> De leeftijd bepaalt de soort "
                  "overeenkomst niet."),
            ("kader", tabel(["indeling", "soorten"],
                            [["<strong>naar duur</strong>", "<strong>van onbepaalde duur</strong> (zonder einddatum, een vast contract), <strong>van bepaalde duur</strong> (met een vaste einddatum, een tijdelijk contract), <strong>voor een duidelijk omschreven werk</strong> en de vervangingsovereenkomst"],
                             ["<strong>naar omvang</strong>", "<strong>voltijds</strong> (de volle werkweek, het aantal uren dat in die sector gebruikelijk is) en <strong>deeltijds</strong> (minder uren, bijvoorbeeld vier vijfde of de helft)"],
                             ["<strong>naar soort werk</strong>", "<strong>arbeider</strong> (vooral handenarbeid) en <strong>bediende</strong> (vooral hoofdarbeid), en de studentenovereenkomst met eigen regels"]])),
            ("p", "<strong>Een overeenkomst van bepaalde duur stopt op haar einddatum, zonder dat iemand moet "
                  "opzeggen.</strong> <strong>Bij een overeenkomst voor een duidelijk omschreven werk stopt ze "
                  "als het werk af is</strong>: niet een datum maar de opdracht bepaalt het einde."),
            ("p", "<strong>Een overeenkomst voor bepaalde duur moet schriftelijk zijn</strong>; staat ze niet "
                  "op papier, dan geldt ze als een overeenkomst van onbepaalde duur. <strong>Een overeenkomst "
                  "van onbepaalde duur moet niet altijd schriftelijk zijn</strong>, die kan ook mondeling, "
                  "maar schriftelijk is veel veiliger voor beide partijen. <strong>Een overeenkomst voor "
                  "studentenarbeid moet altijd schriftelijk zijn</strong>, en ze moet er zijn vóór de student "
                  "begint te werken."),
            ("p", "<strong>Verplicht in een schriftelijke overeenkomst: de identiteit van beide partijen, de "
                  "begindatum, de functie, de arbeidsduur en het loon.</strong> <strong>Over het loon staat er "
                  "hoeveel en wanneer</strong>: het bedrag, de eenheid per uur of per maand, en het ogenblik "
                  "van uitbetaling. <strong>Ontbreken die vermeldingen, dan is de werknemer beschermd</strong>: "
                  "ontbreekt de einddatum, dan geldt de overeenkomst vaak als van onbepaalde duur."),
        ]),
        dict(kop="Gezag, rechten en plichten", blokken=[
            ("p", "<strong>Het gezag van de werkgever betekent dat hij de opdrachten geeft</strong>: hij "
                  "bepaalt wat, waar en wanneer er gewerkt wordt. <strong>Net dat gezag onderscheidt een "
                  "werknemer van een zelfstandige</strong>; dat kenmerk heet ook de ondergeschiktheid. <strong>Een werknemer bepaalt dus niet zelf welke "
                  "taken hij doet</strong>; dat zou van hem een zelfstandige maken."),
            ("kader", tabel(["de werknemer", "de werkgever"],
                            [["<strong>het werk uitvoeren</strong>, zorgvuldig, op tijd en volgens de afspraken", "<strong>het loon betalen</strong>, en werk geven"],
                             ["<strong>de instructies volgen</strong>", "<strong>zorgen voor een veilige werkplek</strong> en de nodige beschermingsmiddelen geven"],
                             ["<strong>de discretieplicht of zwijgplicht</strong>: niets doorvertellen van wat hij over klanten of over de zaak hoort", "de werknemer behandelen volgens de wet en het arbeidsreglement"],
                             ["<strong>recht op loon voor zijn werk</strong>", "<strong>het loon berekenen</strong>, zelf of via een sociaal secretariaat"],
                             ["<strong>recht op jaarlijkse vakantie</strong>", "de vakantie toestaan en uitbetalen"],
                             ["<strong>recht op een veilige en gezonde werkplek</strong>", "het arbeidsongeval aangeven bij de verzekering"]])),
            ("p", "<strong>Een bedrijfswagen is geen recht</strong> maar een extra die in het contract moet "
                  "staan. <strong>En een werknemer mag niet zonder reden wegblijven</strong>: afwezig zijn "
                  "moet gerechtvaardigd zijn door ziekte, verlof of een wettelijke reden."),
            ("p", "<strong>Uit een arbeidsovereenkomst kan je dus de duur en het loon afleiden</strong>, en ook "
                  "het soort werk, de arbeidsduur en wanneer het loon uitbetaald wordt. Dat maakt haar het "
                  "eerste document dat je bovenhaalt als er over een afspraak onduidelijkheid is."),
        ]),
    ])


# ───────────────────────── 11. Schorsing en einde van de arbeidsovereenkomst
zet("schorsing-en-einde-van-de-arbeidsovereenkomst",
    titel="Schorsing en einde van de arbeidsovereenkomst",
    onder="Het verschil tussen een schorsing en een einde, de zeven schorsingsgronden, het gewaarborgd loon bij ziekte, de opzegtermijn en de opzegvergoeding, en wat er in een arbeidsreglement staat.",
    secties=[
        dict(kop="Schorsing: de overeenkomst loopt even niet", blokken=[
            ("p", "<strong>Een schorsing is dat de arbeidsovereenkomst even niet loopt</strong>: het contract "
                  "blijft bestaan, maar de prestaties en soms het loon vallen tijdelijk weg. <strong>Een "
                  "schorsing betekent dus niet dat de overeenkomst stopt</strong>: ze wordt enkel opgeschort, "
                  "en stoppen gebeurt met een opzegging. <strong>Zodra de reden wegvalt, wordt het werk "
                  "gewoon hervat.</strong>"),
            ("kader", tabel(["schorsingsgrond", "wat het is"],
                            [["<strong>ziekte en ongeval</strong>", "de werknemer is arbeidsongeschikt"],
                             ["<strong>zwangerschap en bevallingsverlof</strong>", "<strong>een periode voor en na de bevalling</strong> waarin niet gewerkt wordt"],
                             ["<strong>jaarlijkse vakantie</strong>", "<strong>ook dat is een schorsing</strong>: er wordt niet gewerkt, maar het contract loopt door"],
                             ["<strong>klein verlet</strong>, ook kort verzuim", "<strong>betaald verlof voor een gebeurtenis</strong>: een huwelijk, een geboorte of een begrafenis"],
                             ["<strong>verloren arbeidsuren</strong>", "<strong>uren die wegvallen</strong>, bijvoorbeeld door panne of door het weer"],
                             ["<strong>een dwingende reden van familiaal belang</strong>", "<strong>een noodgeval thuis</strong>: je mag van het werk weg, maar dat verlof is onbetaald"],
                             ["<strong>overmacht</strong>, in het Frans force majeure", "<strong>niemand kon het helpen</strong>: de oorzaak waar niemand iets aan kon doen: een brand, een overstroming, werken is onmogelijk buiten de wil van beide partijen"]])),
            ("p", "<strong>Klein verlet is betaald, geldt voor een gebeurtenis en duurt kort</strong>, meestal "
                  "één tot enkele dagen, per gebeurtenis vastgelegd."),
            ("p", "<strong>Wie ziek wordt, moet de werkgever verwittigen</strong>, meteen, en als het "
                  "reglement dat vraagt een attest bezorgen. <strong>Met een doktersattest bewijst hij dat hij "
                  "arbeidsongeschikt is</strong>, en voor hoe lang."),
            ("p", "<strong>Bij ziekte krijgt een werknemer wel loon.</strong> <strong>De eerste periode "
                  "betaalt de werkgever het gewaarborgd loon of gewaarborgd maandloon door</strong>; <strong>daarna neemt het "
                  "ziekenfonds over</strong> met een ziekte-uitkering. <strong>Ziekte is geen reden voor een "
                  "ontslag op staande voet.</strong>"),
        ]),
        dict(kop="Het einde van de overeenkomst", blokken=[
            ("p", "<strong>Een overeenkomst van onbepaalde duur eindigt normaal met een opzegtermijn</strong>, "
                  "of met een opzegvergoeding in plaats van die termijn. <strong>Beide partijen kunnen "
                  "opzeggen</strong>; de termijn is wel korter als de werknemer zelf opzegt."),
            ("p", "<strong>Een opzegtermijn is de tijd tot het einde</strong>: de periode die nog gewerkt "
                  "wordt na de opzegging. <strong>Ze begint te lopen op de maandag die volgt op de week van "
                  "de opzegging</strong>, en <strong>haar lengte wordt bepaald door de anciënniteit</strong>, "
                  "het aantal dienstjaren dat iemand al in dienst is: hoe langer in dienst, hoe langer de termijn."),
            ("p", "<strong>Een opzegging moet schriftelijk gebeuren</strong>, met de begindatum en de duur van "
                  "de termijn erin. <strong>Een werkgever die mondeling ontslaat, riskeert een vergoeding te "
                  "moeten betalen.</strong> <strong>De formaliteit is een schriftelijke brief</strong>, "
                  "aangetekend of met een ontvangstbewijs, zodat de datum vaststaat."),
            ("p", "<strong>Een opzegvergoeding, ook een verbrekingsvergoeding, is loon in plaats van de termijn</strong>: wil de werkgever dat "
                  "je meteen stopt, dan betaalt hij het loon van de termijn in één keer uit. <strong>Bij het "
                  "einde van een overeenkomst horen dus de formaliteiten, het begin en de duur van de termijn, "
                  "en de opzegvergoeding.</strong> Vakantie hoort bij de schorsing, niet bij het einde."),
        ]),
        dict(kop="Het arbeidsreglement", blokken=[
            ("p", "<strong>Een arbeidsreglement zijn de regels in de zaak</strong>: de afspraken die voor "
                  "iedereen in de onderneming gelden. <strong>Het geldt voor alle werknemers</strong>, in elke "
                  "functie. <strong>Het is wettelijk verplicht zodra er personeel in dienst is</strong>, en "
                  "<strong>elke werknemer moet er een exemplaar van krijgen</strong>, zodat niemand kan zeggen "
                  "dat hij de regels niet kende."),
            ("p", "<strong>Erin staan de arbeidsduur en de uurregeling, de ziekteregeling en de regeling van "
                  "de jaarlijkse vakantie.</strong> Daaruit haal je dus de werkuren, wanneer je vakantie kan "
                  "nemen en wat je moet doen bij ziekte: <strong>wie je verwittigt, binnen welke tijd, en of "
                  "er een attest nodig is</strong>."),
            ("p", "<strong>Cijfers over de omzet staan er niet in</strong>: het reglement gaat over de "
                  "afspraken, niet over de cijfers. Die horen in de jaarrekening."),
        ]),
    ])


# ───────────────────────── 12. De loonfiche en de loonberekening
zet("de-loonfiche-en-de-loonberekening",
    titel="De loonfiche en de loonberekening",
    onder="Van bruto naar netto in twee stappen, het verschil tussen de RSZ-bijdrage en de bedrijfsvoorheffing, de patronale bijdrage en de loonkost, de fiche 281.10 en de premies.",
    secties=[
        dict(kop="Bruto, netto en de twee afhoudingen", blokken=[
            ("p", "<strong>Een loonfiche is het overzicht van je loon</strong>: elke maand krijg je er een, "
                  "met alles wat van bruto naar netto gaat. <strong>Het brutoloon is het loon vóór de "
                  "afhoudingen</strong>, het bedrag dat in je contract staat. <strong>Het nettoloon is wat je "
                  "echt krijgt</strong>, het bedrag dat op je bankrekening komt. <strong>Op je rekening komt dus "
                  "het netto, niet het bruto</strong>, en <strong>het netto is altijd lager</strong>, want er "
                  "gaan altijd minstens twee dingen af."),
            ("kader", tabel(["afhouding", "waarnaar ze gaat", "wie houdt ze af"],
                            [["<strong>de werknemersbijdrage RSZ</strong>", "<strong>de sociale zekerheid</strong>: pensioen, ziekteverzekering, werkloosheid en gezinsbijslag", "<strong>de werkgever</strong>, die ze samen met zijn eigen bijdrage doorstort"],
                             ["<strong>de bedrijfsvoorheffing</strong>", "<strong>een voorschot op je belasting</strong>", "de werkgever, die ze doorstort aan de fiscus"]])),
            ("p", "<strong>De bedrijfsvoorheffing is geen deel van de RSZ-bijdrage</strong>: de RSZ-bijdrage "
                  "gaat naar de sociale zekerheid, de voorheffing is een voorschot op je belasting. Dat zijn "
                  "twee verschillende bestemmingen. <strong>De dienst die de sociale bijdragen int, is de "
                  "RSZ</strong>, de Rijksdienst voor Sociale Zekerheid. Naast die twee afhoudingen staat er soms nog een bijzondere bijdrage op je fiche."),
            ("p", "<strong>Op een loonfiche staan het brutoloon, de RSZ-bijdrage, de bedrijfsvoorheffing, het "
                  "nettoloon, de gewerkte dagen en eventuele premies.</strong> <strong>Je krijgt er elke maand "
                  "een om alles te kunnen nazien</strong>, en <strong>je hoort ze na te kijken</strong>: een "
                  "vergeten overuur of een verkeerd aantal dagen vind je enkel zo."),
        ]),
        dict(kop="De loonberekening stap voor stap", blokken=[
            ("p", "<strong>Het nettoloon volgt niet rechtstreeks uit het bruto</strong>: er zit een tussenstap "
                  "in, het belastbaar loon. <strong>Je neemt het brutoloon, trekt de RSZ-bijdrage af en trekt "
                  "daarna de bedrijfsvoorheffing af</strong>; wat dan overblijft, is het nettoloon."),
            ("fig", svg.stappen(["brutoloon|uren × uurloon", "min de RSZ|13,07 %",
                                 "belastbaar loon", "min de|bedrijfsvoorheffing", "nettoloon"]),
             "De vier stappen van een eenvoudige loonberekening. De bedrijfsvoorheffing wordt berekend op het "
             "belastbaar loon, niet op het bruto."),
            ("p", "<strong>De eerste stap is het brutoloon bepalen</strong>: uren maal uurloon, of het "
                  "maandloon uit het contract. <strong>Daarna trek je eerst de RSZ-bijdrage af</strong>, en op "
                  "wat overblijft wordt de bedrijfsvoorheffing berekend. <strong>Het belastbaar loon is dus "
                  "bruto min RSZ</strong>, en <strong>daarop wordt de voorheffing berekend</strong>."),
            ("p", "Neem een brutoloon van 2 400 euro per maand. <strong>De werknemersbijdrage RSZ is 13,07 "
                  "procent, dus 313,68 euro.</strong> <strong>Het belastbaar loon is dan 2 086,32 euro.</strong> "
                  "Stel dat de officiële tabel voor deze gezinssituatie 320 euro bedrijfsvoorheffing geeft, "
                  "dan is <strong>het nettoloon 1 766,32 euro</strong>."),
            ("kader", tabel(["stap", "bedrag"],
                            [["brutoloon", "2 400,00 euro"],
                             ["min de RSZ-bijdrage van 13,07 procent", "− 313,68 euro"],
                             ["<strong>belastbaar loon</strong>", "<strong>2 086,32 euro</strong>"],
                             ["min de bedrijfsvoorheffing (uit de tabel)", "− 320,00 euro"],
                             ["<strong>nettoloon</strong>", "<strong>1 766,32 euro</strong>"]])),
            ("p", "<strong>Twee werknemers met hetzelfde brutoloon kunnen een ander nettoloon hebben</strong>, "
                  "en dat komt van die laatste stap: <strong>de bedrijfsvoorheffing hangt af van de hoogte van "
                  "het loon, van je gezinssituatie en van het aantal kinderen ten laste</strong>. Daarom "
                  "bestaan er officiële tabellen voor elke situatie."),
            ("p", "<strong>Een patronale bijdrage is de RSZ van de werkgever</strong>: bovenop het brutoloon "
                  "betaalt hij zelf nog een bijdrage aan de RSZ. <strong>Die komt erbovenop en gaat niet van "
                  "jouw brutoloon af.</strong> <strong>Daarom kost een werknemer meer dan zijn "
                  "brutoloon</strong>, en spreekt men van de loonkost. Bij een patronale bijdrage van grofweg "
                  "een kwart is de loonkost van dit brutoloon ongeveer 3 000 euro, terwijl de werknemer er "
                  "1 766,32 euro van op zijn rekening ziet."),
        ]),
        dict(kop="De fiche 281.10 en de premies", blokken=[
            ("p", "<strong>De fiscale fiche met het nummer 281.10 is het jaaroverzicht van je loon</strong>: alles wat je dat "
                  "jaar verdiende en wat er werd ingehouden, op één blad. <strong>De werkgever of zijn sociaal "
                  "secretariaat bezorgt ze je</strong> in het begin van het volgende jaar."),
            ("p", "<strong>Erop staan het totale brutoloon van het jaar, de ingehouden bedrijfsvoorheffing en "
                  "de identiteit van de werknemer.</strong> De omzet van de zaak staat er niet op: de fiche "
                  "gaat over één werknemer. <strong>Je gebruikt ze voor je belastingaangifte</strong>, waar je "
                  "de bedragen invult bij je personenbelasting."),
            ("p", "<strong>De bedrijfsvoorheffing is een voorschot, geen eindafrekening</strong>: de "
                  "eindafrekening komt met het aanslagbiljet na je aangifte. <strong>Was de voorheffing te "
                  "hoog, dan krijg je geld terug.</strong> <strong>Wie voorheffing betaalde, moet dus nog "
                  "altijd een aangifte doen</strong>; daar wordt de voorheffing mee verrekend."),
            ("p", "<strong>Vakantiegeld is een extra bij de vakantie</strong>, een bedrag bovenop het gewone "
                  "loon, meestal in mei of juni. <strong>Een eindejaarspremie is een dertiende maand</strong>, "
                  "een extra loon in december, in veel sectoren verplicht."),
        ]),
    ])


# ───────────────────────── 13. De marketingmix
zet("de-marketingmix",
    titel="De marketingmix",
    onder="De vier P's en wat er in elke P hoort, waarom ze samen horen, de doelgroep, en dezelfde mix nog een keer bekeken vanuit de klant: de vier C's.",
    secties=[
        dict(kop="De vier P's", blokken=[
            ("p", "<strong>De marketingmix zijn de keuzes rond het verkopen</strong>: de keuzes over het "
                  "product, de prijs, de plaats en de promotie. <strong>Dat zijn de vier klassieke P's</strong>, "
                  "en het geheel ervan is de marketingmix."),
            ("kader", tabel(["P", "waarover ze gaat", "wat erin hoort"],
                            [["<strong>product</strong>", "<strong>wat je verkoopt</strong>", "<strong>de kwaliteit, de verpakking, het merk</strong> en de service erbij"],
                             ["<strong>prijs</strong>", "<strong>wat de klant betaalt</strong>", "de kortingen, de betalingsvoorwaarden en de prijsstrategie"],
                             ["<strong>plaats</strong>", "<strong>waar de klant het kan kopen</strong>, ook distributie genoemd", "<strong>de weg naar de klant</strong>: een eigen winkel, een groothandel, <strong>een webshop</strong> of een combinatie"],
                             ["<strong>promotie</strong>", "<strong>hoe je het product bekendmaakt</strong>", "<strong>de reclame, een advertentie, een actie in de winkel, een post op sociale media</strong>, beurzen"]])),
            ("p", "<strong>Een merk is de naam van een product</strong>, een naam of teken waaraan de klant "
                  "jouw product herkent, en het hoort bij de P van product. <strong>De verpakking hoort ook "
                  "bij het product, niet bij de promotie</strong>; <strong>de reclamespot hoort bij de "
                  "promotie, niet bij het product</strong>. Dat verschil is het makkelijkst te verwarren."),
            ("p", "<strong>De vier P's staan niet los van elkaar</strong>: ze horen samen. Een duur product in "
                  "een goedkope winkel met flauwe reclame verkoopt niet. <strong>Je herkent de onderdelen van een mix in een "
                  "voorbeeld door elke P erin te zoeken</strong>: wat is het product, wat is de prijs, waar "
                  "wordt het verkocht en hoe wordt het bekendgemaakt."),
            ("p", "<strong>Een doelgroep zijn de klanten die je wil</strong>, de groep mensen waar je product "
                  "voor bedoeld is. <strong>Dezelfde marketingmix past niet bij elke doelgroep</strong>: een "
                  "product voor jongeren vraagt een andere prijs, plaats en promotie dan een product voor "
                  "zestigplussers. <strong>Daarom moet een onderneming de markt onderzoeken</strong>: zonder "
                  "te weten wat de doelgroep vraagt, is elke keuze een gok."),
            ("p", "<strong>Een lage prijs is dus niet altijd de beste keuze</strong>: een te lage prijs kan de "
                  "klant doen twijfelen aan de kwaliteit. <strong>De marketingafdeling kiest welk product, aan "
                  "welke prijs en via welk kanaal</strong>; de boekhouding is werk voor de administratie."),
        ]),
        dict(kop="Dezelfde mix vanuit de klant: de vier C's", blokken=[
            ("p", "<strong>De vier C's kijken van de klant uit.</strong> Het is dezelfde mix, maar bekeken "
                  "door de ogen van de klant, en <strong>elke P heeft een C die hetzelfde zegt van de andere "
                  "kant</strong>."),
            ("kader", tabel(["C", "waarvoor ze staat", "welke P"],
                            [["<strong>customer</strong>", "<strong>de klant</strong>: niet wat jij wil verkopen, maar wat de klant nodig heeft", "het product"],
                             ["<strong>cost</strong>", "<strong>wat het kost</strong>: niet enkel de prijs, ook de tijd en de moeite die het de klant kost", "<strong>de prijs</strong>"],
                             ["<strong>convenience</strong>", "<strong>het gemak</strong>: hoe eenvoudig het voor de klant is om eraan te komen", "<strong>de plaats</strong>"],
                             ["<strong>communication</strong>", "<strong>de communicatie met de klant</strong>: de boodschap die je stuurt én het gesprek dat eruit komt", "<strong>de promotie</strong>"]])),
            ("p", "<strong>De prijs van de verkoper is de kost van de klant</strong>, en in die kost zitten "
                  "<strong>de prijs, de tijd die het hem kost en de moeite om er te komen</strong>. De winst "
                  "van de verkoper is geen kost voor de klant. <strong>Cash hoort niet bij de vier C's.</strong>"),
            ("p", "<strong>Communicatie is tweerichtingsverkeer, promotie vooral eenrichting</strong>: "
                  "promotie is zenden, bij communicatie hoort ook wat de klant terugzegt. <strong>Convenience "
                  "gaat over gemak, niet over goedkoop</strong>: de prijs zit in cost. <strong>Voor een "
                  "webshop betekent convenience een vlotte website, een snelle levering en makkelijk kunnen "
                  "terugsturen</strong>; de reclamespot hoort bij communicatie."),
            ("p", "<strong>De vier C's vervangen de vier P's niet</strong>: ze staan ernaast en helpen om de "
                  "mix vanuit de klant te bekijken. <strong>Men gebruikt ze omdat de klant zo centraal "
                  "staat</strong>: de P's kijken van de onderneming uit, de C's van de klant uit. <strong>Voor "
                  "de verkoper betekent dat eerst de vraag van de klant kennen</strong>: je begint bij de "
                  "behoefte en bouwt je aanbod daarrond."),
        ]),
    ])


# ───────────────────────── 14. Soorten klanten en het verkoopgesprek
zet("soorten-klanten-en-het-verkoopgesprek",
    titel="Soorten klanten en het verkoopgesprek",
    onder="Rationele en emotionele koopmotieven, hoe je met een stille, een twijfelende of een veeleisende klant omgaat, en de zes fasen van een verkoopgesprek van de aandacht tot de afsluiting.",
    secties=[
        dict(kop="Koopmotieven", blokken=[
            ("p", "<strong>Een koopmotief is de reden om te kopen</strong>: waarom iemand dit product wil "
                  "hebben. <strong>Een rationeel koopmotief is een verstandige reden</strong>, <strong>een "
                  "emotioneel koopmotief een gevoelsreden</strong>, een motief dat op gevoel berust, ook een gevoelsmatig motief genoemd."),
            ("kader", tabel(["rationeel", "emotioneel"],
                            [["<strong>de prijs</strong>", "<strong>status</strong>"],
                             ["<strong>de kwaliteit</strong>", "<strong>mode</strong>"],
                             ["<strong>de garantie</strong>", "<strong>erbij willen horen</strong>"],
                             ["het verbruik", "iets mooi vinden"]])),
            ("p", "<strong>Een klant kan meerdere koopmotieven tegelijk hebben</strong>: een wagen kan "
                  "tegelijk zuinig én mooi moeten zijn. <strong>Het is nuttig het motief te kennen omdat je "
                  "argumenten dan beter passen</strong>: wie om zuinigheid geeft, hoort iets anders dan wie om "
                  "design geeft. <strong>Een verkoper vertelt dus niet elke klant hetzelfde verhaal.</strong>"),
        ]),
        dict(kop="Soorten klanten", blokken=[
            ("p", "<strong>Niet elke klant wil op dezelfde manier aangepakt worden</strong>: een stille klant "
                  "en een veeleisende klant hebben een andere aanpak nodig."),
            ("kader", tabel(["soort klant", "wat je doet"],
                            [["<strong>de stille klant</strong>", "<strong>open vragen stellen</strong>: met een open vraag krijg je meer dan ja of nee terug"],
                             ["<strong>de twijfelende klant</strong>", "<strong>hij kan niet kiezen</strong>: help hem met twee of drie duidelijke opties in plaats van tien"],
                             ["<strong>de veeleisende klant</strong>", "<strong>rustig en duidelijk blijven</strong>: je neemt zijn vraag ernstig en zegt eerlijk wat kan en wat niet"],
                             ["<strong>de klant die veel weet</strong>", "<strong>zijn kennis erkennen</strong>: bouw op wat hij al weet en vul aan waar hij iets mist"],
                             ["<strong>wie enkel komt kijken</strong>", "<strong>je blijft beschikbaar</strong>: je laat hem rondkijken en zegt dat je er bent als hij iets wil weten"]])),
            ("p", "<strong>Een goede verkoper luistert meer dan hij praat</strong>, en in het begin van het "
                  "gesprek doet hij vooral dat: luisteren en vragen stellen. Zonder te weten wat de klant "
                  "zoekt, is elk argument een gok."),
            ("p", "<strong>Een verkoopgesprek observeren is nuttig om eruit te leren</strong>: je ziet wat "
                  "werkte en wat je zelf anders zou doen. <strong>Je beoordeelt het op drie dingen: is er "
                  "geluisterd, is de behoefte gevonden en zijn de bezwaren weerlegd.</strong> Druk zetten is "
                  "geen teken van een goed gesprek."),
        ]),
        dict(kop="De zes fasen van het gesprek", blokken=[
            ("fig", svg.stappen(["de aandacht|trekken", "de behoefte|ontwikkelen", "argumenten|geven",
                                 "bezwaren|weerleggen", "koopsignalen|ontdekken", "afsluiten"]),
             "De zes fasen die de vakfiche noemt. Boeken is werk voor de boekhouding en hoort niet in deze "
             "rij."),
            ("p", "<strong>De eerste fase is de aandacht krijgen</strong>: de aandacht van de klant trekken, "
                  "of hem aandacht geven. <strong>Daarna ontwikkel je de behoefte</strong>: je zoekt samen met "
                  "de klant wat hij echt nodig heeft. <strong>Daarom stel je eerst vragen</strong>; zonder "
                  "behoefte is er niets om argumenten op te bouwen."),
            ("p", "<strong>Een open vraag vraagt om uitleg</strong>: “waarvoor gaat u het gebruiken?” "
                  "geeft meer terug dan “wil u dit?”."),
            ("p", "<strong>Pas als je de behoefte kent, geef je argumenten</strong>, en dan argumenten die bij "
                  "die behoefte passen, niet bij alle producten. <strong>Argumenten geven vóór je de behoefte "
                  "kent, is praten over zaken waar de klant niets aan heeft.</strong>"),
            ("p", "<strong>Een bezwaar is een tegenargument</strong>: te duur, te groot, of hij wil er nog "
                  "over nadenken. <strong>Een bezwaar betekent vaak dat de klant geïnteresseerd is</strong>, "
                  "want wie helemaal niet wil kopen, neemt niet de moeite om tegen te spreken. <strong>Je hoort "
                  "een bezwaar dus niet te negeren</strong> maar te erkennen en er een eerlijk antwoord op te "
                  "geven: <strong>erkennen en antwoorden.</strong>"),
            ("p", "<strong>Bij het bezwaar dat iets te duur is, ga je de waarde uitleggen, toon je een alternatief "
                  "of vraag je waarmee hij vergelijkt</strong>: soms vergelijkt hij met iets dat veel minder "
                  "biedt."),
            ("p", "<strong>Een koopsignaal is het teken dat de klant wil kopen</strong>: hij vraagt naar de "
                  "levertijd, naar de garantie of naar de kleur die hij wil. <strong>Zie je een koopsignaal, "
                  "dan ga je naar de afsluiting</strong>: de klant is er klaar voor, en nog meer uitleg kan "
                  "nieuwe twijfel wekken. <strong>Wie te lang doorpraat na een koopsignaal, kan de verkoop "
                  "verliezen.</strong>"),
            ("p", "<strong>De laatste fase is de aankoop afsluiten</strong>: je maakt de afspraak concreet en "
                  "bevestigt wat er geleverd wordt. <strong>Bij een goede afsluiting bevestig je de afspraak, "
                  "regel je de levering en bedank je de klant.</strong> Druk zetten levert een klant op die "
                  "later afbelt."),
        ]),
    ])


# ───────────────────────── 15. Commerciële documenten en de documentenstroom
zet("commerciele-documenten-en-de-documentenstroom",
    titel="Commerciële documenten en de documentenstroom",
    onder="De zeven commerciële documenten en wie ze maakt, de volgorde waarin ze bij een aankoop komen, en hoe je een factuur controleert tegen de bestelbon en de leverbon.",
    secties=[
        dict(kop="De zeven documenten", blokken=[
            ("kader", tabel(["document", "wat het is", "van wie naar wie"],
                            [["<strong>de prijsaanvraag</strong>", "<strong>vragen wat iets kost</strong>, vaak bij meerdere leveranciers om te kunnen vergelijken", "<strong>klant → leverancier</strong>"],
                             ["<strong>de offerte</strong>", "<strong>een prijsvoorstel of prijsopgave</strong>, het antwoord op de prijsaanvraag", "leverancier → klant"],
                             ["<strong>de bestelbon</strong>", "<strong>de klant bestelt</strong>: schriftelijk wat hij wil, in welke aantallen en aan welke prijs", "<strong>klant → leverancier</strong>"],
                             ["<strong>de orderbevestiging</strong>", "<strong>de leverancier bevestigt</strong> dat de bestelling binnen is en wanneer hij levert", "leverancier → klant"],
                             ["<strong>de leverbon</strong> of leveringsbon", "<strong>wat er geleverd is</strong>: de lijst die met de goederen meekomt", "leverancier → klant"],
                             ["<strong>de factuur</strong>", "<strong>de vraag om te betalen</strong>, met de bedragen, de btw en de betalingsvoorwaarden", "leverancier → klant"],
                             ["<strong>de creditnota</strong>, ook kredietnota", "<strong>een factuur rechtzetten</strong>, bij een retour, een korting achteraf of een fout", "leverancier → klant"]])),
            ("p", "<strong>De leverbon gaat mee met de goederen</strong>, zodat de ontvanger meteen kan nagaan "
                  "of alles er is. <strong>Hij vermeldt niet altijd de prijzen</strong>: een leverbon noemt "
                  "vooral de aantallen, de bedragen staan op de factuur."),
            ("p", "<strong>De factuur maakt de verkoper</strong>: voor hem is het een verkoopfactuur, voor de "
                  "koper een aankoopfactuur. <strong>Een bestelbon en een factuur zijn dus niet hetzelfde "
                  "document</strong>: de bestelbon komt van de koper, de factuur van de verkoper."),
            ("p", "<strong>Verplicht op een factuur: de datum en het nummer, de gegevens van beide partijen, "
                  "de btw en het totaal, en de omschrijving van de goederen of diensten.</strong>"),
            ("p", "<strong>Een offerte bindt de leverancier aan zijn prijs zolang ze geldig is</strong>, en "
                  "daarom staat er een geldigheidsduur op. <strong>Het doel van een orderbevestiging is "
                  "zekerheid geven</strong>: de klant weet dat zijn bestelling aangekomen is en wanneer ze "
                  "komt. <strong>Van de klant naar de leverancier gaan de prijsaanvraag, de bestelbon en de "
                  "klacht bij een fout</strong>; de factuur komt de andere richting uit. De loonfiche is een "
                  "personeelsdocument en hoort hier niet bij."),
        ]),
        dict(kop="De documentenstroom", blokken=[
            ("p", "<strong>De documentenstroom of documentstroom is het overzicht van de volgorde van de papieren</strong>: welk document wanneer "
                  "gemaakt wordt, en door wie. <strong>In een schema zet je wie wat wanneer stuurt</strong>, "
                  "met pijlen tussen de klant, de leverancier en de betrokken afdelingen."),
            ("fig", svg.stappen(["prijsaanvraag", "offerte", "bestelbon", "order-|bevestiging",
                                 "leverbon", "factuur"]),
             "De documenten van een aankoop in hun orde. De prijsaanvraag staat vooraan, de factuur achteraan, "
             "tenzij er nog een creditnota volgt."),
            ("p", "<strong>De prijsaanvraag komt eerst</strong>: eerst weten wat het kost, dan pas bestellen. "
                  "<strong>De factuur komt als laatste</strong>, tenzij er nog een creditnota volgt omdat er "
                  "iets terug moet. <strong>De offerte volgt op de prijsaanvraag, de bestelbon op de offerte "
                  "en de factuur op de levering.</strong>"),
            ("p", "<strong>Bij een aankoop zijn drie afdelingen betrokken: de aankoop bestelt, de logistiek "
                  "ontvangt, de boekhouding boekt en betaalt.</strong> <strong>De boekhouding krijgt dus de "
                  "factuur van de leverancier</strong> en volgt de betaling op."),
            ("p", "<strong>De documentenstroom bij een verkoop is niet helemaal anders dan bij een "
                  "aankoop</strong>: het zijn dezelfde documenten, enkel je rol wisselt van koper naar "
                  "verkoper. Wie bij een aankoop de bestelbon maakt, krijgt hem bij een verkoop toegestuurd."),
        ]),
        dict(kop="Controleren en narekenen", blokken=[
            ("p", "<strong>Je vergelijkt de leverbon met de bestelbon om te zien of alles er is</strong>: wat "
                  "besteld werd, moet ook geleverd zijn, in dezelfde aantallen. Dat nagaan of twee documenten "
                  "met elkaar kloppen, heet <strong>controleren op onderlinge overeenstemming</strong>: nakijken en vergelijken."),
            ("p", "<strong>Een factuur controleer je tegen de bestelbon en de leverbon</strong>: zo zie je of "
                  "je betaalt voor wat je besteld hebt en ook gekregen hebt. <strong>Een factuur mag je dus "
                  "niet zonder controle boeken en betalen</strong>: een fout die je niet opmerkt, betaal je "
                  "zelf."),
            ("p", "<strong>Op een inkomende factuur controleer je de geleverde aantallen, de afgesproken "
                  "prijzen en de berekening van de btw</strong>, en of de kortingen uit de offerte er echt op "
                  "staan. <strong>Documenten narekenen is de bedragen nagaan</strong>: de aantallen maal de "
                  "prijzen, de kortingen, de btw en het totaal."),
            ("p", "<strong>Staat er een hoger bedrag op de factuur dan op de offerte, dan contacteer je de "
                  "leverancier</strong>: je vraagt uitleg en zo nodig een creditnota. <strong>Een goede "
                  "controle voorkomt dat je te veel betaalt</strong>, en ook dat je een levering betaalt die "
                  "nooit is aangekomen."),
            ("p", "<strong>Een correct opgesteld commercieel document heeft de juiste gegevens, een duidelijke "
                  "datum en een kloppende berekening</strong>, en een nummer, zodat je het later terugvindt. "
                  "<strong>Het doel van dat alles is kwaliteit afleveren</strong>: wie zijn documenten laat "
                  "kloppen, levert werk af waarop de klant kan bouwen."),
        ]),
    ])


# ───────────────────────── 16. Transport, expeditie en logistiek
zet("transport-expeditie-en-logistiek",
    titel="Transport, expeditie en logistiek",
    onder="De zes transportmodi met hun voor- en nadelen, waarop je ze vergelijkt, de taken van expeditie en logistiek, invoer, uitvoer en doorvoer, en de pakbon tegenover de CMR.",
    secties=[
        dict(kop="De zes transportmodi", blokken=[
            ("p", "<strong>Een transportmodus is een manier van vervoeren.</strong> De vakfiche noemt er zes."),
            ("kader", tabel(["modus", "sterk", "zwak"],
                            [["<strong>wegvervoer</strong>, met vrachtwagens", "<strong>tot aan de deur</strong>: een vrachtwagen kan tot bij de klant rijden", "<strong>de files</strong>, en een hogere uitstoot per ton dan spoor of water"],
                             ["<strong>spoorvervoer</strong>", "<strong>stoot per ton minder uit dan wegvervoer</strong>, veel lading in één keer", "stopt bij een terminal"],
                             ["<strong>binnenscheepvaart</strong> of binnenvaart, over water in het binnenland", "goedkoop en zuinig voor grote volumes", "traag, en enkel waar er water is"],
                             ["<strong>maritiem vervoer</strong>, over zee", "<strong>de grootste capaciteit</strong>: een containerschip neemt de lading van duizenden vrachtwagens mee, en goedkoop per ton", "<strong>het traagst van alle</strong>"],
                             ["<strong>luchtvracht</strong>", "<strong>het snelst over grote afstand</strong>, met het vliegtuig", "<strong>duur</strong>, dus vooral lichte, dringende of kostbare vracht"],
                             ["<strong>de pijpleiding</strong>", "<strong>vloeistof of gas</strong>, dag en nacht door zonder chauffeur", "enkel waar de leiding ligt, en enkel voor dat soort lading"]])),
            ("p", "<strong>Maritiem vervoer is dus niet de snelste manier</strong>: een zeeschip is het "
                  "traagst, maar het vervoert enorme volumes voor weinig geld. <strong>Luchtvracht is snel "
                  "maar duur</strong>, en <strong>voor een dringend klein pakje naar Japan kies je "
                  "luchtvracht</strong>: duur per kilo, maar in een dag ter plaatse."),
            ("p", "<strong>Je vergelijkt de modi op snelheid en kosten</strong>, en ook op bereikbaarheid, "
                  "capaciteit, de aard van het product en het milieueffect. <strong>De keuze van een "
                  "transportmiddel baseer je op hoe dringend het is, op wat het product nodig heeft en op wat "
                  "het mag kosten</strong>, en op of de bestemming wel per spoor of over water bereikbaar is. "
                  "<strong>Voor vers fruit uit Spanje is gekoeld wegvervoer de keuze</strong>: snel genoeg en "
                  "met koeling."),
            ("p", "<strong>Niet elke modus kan tot aan de deur leveren</strong>: een schip en een trein stoppen "
                  "bij een terminal, en de laatste kilometers gaan over de weg. <strong>Daarom gebruikt men "
                  "vaak meerdere modi na elkaar, elk voor wat hij best kan</strong>: een container komt per "
                  "schip aan en gaat met de trein of de vrachtwagen verder."),
        ]),
        dict(kop="De taken van expeditie en logistiek", blokken=[
            ("p", "<strong>De vakfiche noemt zeven taken: goederen ontvangen en opslaan, picken en verzenden, "
                  "het transport plannen, de voorraad beheren en de retour van goederen afhandelen.</strong> "
                  "Lonen zijn werk voor HR en de boekhouding."),
            ("p", "<strong>Picken of orderpicken is de goederen van een order in de loods uit de rekken halen</strong>, ze uithalen en samenbrengen. "
                  "<strong>Een retour zijn goederen die terugkomen</strong>: de klant stuurt terug wat hij "
                  "niet houdt, en de logistiek handelt dat af."),
            ("p", "<strong>Voorraadbeheer is weten wat je hebt</strong>, en op tijd bijbestellen zonder te "
                  "veel in de rekken te laten staan. <strong>Een te kleine voorraad kan een verkoop doen "
                  "mislopen</strong>, want wat je niet in huis hebt, kan je niet leveren. <strong>Maar een zo "
                  "groot mogelijke voorraad is niet het beste</strong>: voorraad kost plaats en geld en kan "
                  "verouderen. <strong>Te veel is even slecht als te weinig</strong>, en daar zit heel het "
                  "vak in."),
            ("p", "<strong>Een eenvoudige logistieke taak is een route opstellen</strong>, volumes en "
                  "gewichten berekenen of een retour afhandelen."),
            ("p", "<strong>Een goede logistiek is belangrijk voor de hele onderneming</strong>: de klant krijgt "
                  "zijn levering op tijd, de voorraad kost niet te veel en de verkoop kan haar beloftes "
                  "nakomen. De prijs van reclame heeft met de logistiek niets te maken."),
        ]),
        dict(kop="Over de grens, en de papieren erbij", blokken=[
            ("kader", tabel(["woord", "wat het is"],
                            [["<strong>invoer</strong>", "<strong>goederen binnenbrengen</strong>: ze komen uit het buitenland het land binnen"],
                             ["<strong>uitvoer</strong>", "<strong>goederen buitenbrengen</strong>: ze gaan van hier naar een ander land"],
                             ["<strong>doorvoer</strong>", "<strong>enkel passeren</strong>: de goederen gaan door het land zonder er verhandeld te worden"]])),
            ("p", "<strong>Een pakbon of paklijst zegt wat in de zending zit</strong>: de lijst van de inhoud, zodat de "
                  "ontvanger kan nakijken of alles er is. <strong>Een CMR is de vrachtbrief voor "
                  "internationaal wegvervoer</strong>, en hij regelt wie waarvoor aansprakelijk is tijdens het "
                  "transport."),
            ("p", "<strong>Een pakbon en een CMR zijn dus niet hetzelfde</strong>: de pakbon zegt wat erin zit, "
                  "de CMR is de vervoersovereenkomst. <strong>De CMR wordt ondertekend door drie partijen: de "
                  "afzender, de vervoerder en de bestemmeling.</strong> <strong>Erop staan de afzender en de "
                  "bestemmeling, de aard van de goederen en het gewicht van de zending</strong>, en de plaats "
                  "en datum van inlading en van levering."),
        ]),
    ])

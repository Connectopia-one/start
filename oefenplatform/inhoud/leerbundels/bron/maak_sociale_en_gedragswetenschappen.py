# -*- coding: utf-8 -*-
"""De leerbundels voor sociale en gedragswetenschappen op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche sociale en gedragswetenschappen 2DO, geldig vanaf
1 januari 2027. Die fiche geldt voor één richting: humane wetenschappen. Ze
weegt gedragswetenschappen 60 % en sociale wetenschappen 40 %, en de zestien
thema's volgen dat.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py
../../boost-doorstroom/sociale-en-gedragswetenschappen.json` doet daar het
voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, want een titel alleen is binnen een vak geen sleutel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Sociale en gedragswetenschappen"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. Ontwikkeling: groeien, rijpen en leren
zet("ontwikkeling-groeien-rijpen-en-leren",
    titel="Ontwikkeling: groeien, rijpen en leren",
    onder="Waaruit ontwikkeling bestaat, welke levensloopfasen een mens doorloopt, en wat nature, nurture en zelfbepaling eraan bijdragen.",
    secties=[
        dict(kop="Drie dingen tegelijk: groeien, rijpen en leren", blokken=[
            ("p", "Ontwikkeling is geen enkel woord voor één ding. Ze bestaat uit <strong>groeien, rijpen en "
                  "leren</strong>, en die drie lopen je hele leven door elkaar."),
            ("p", "<strong>Groeien</strong> is de zuiver lichamelijke toename: je wordt langer, zwaarder, groter. "
                  "Een baby die in een jaar <strong>twintig centimeter langer</strong> wordt, groeit. "
                  "<strong>Vijf centimeter langer worden</strong>, <strong>drie kilo bijkomen</strong> en "
                  "<strong>een grotere schoenmaat krijgen</strong> zijn alle drie groeien: er komt letterlijk "
                  "lichaam bij."),
            ("p", "<strong>Rijpen</strong> is wat vanzelf komt, zonder dat je het oefent. Het zit in je "
                  "lichaam ingebakken en wacht alleen op zijn moment. Een baby die zijn "
                  "<strong>eerste tandjes</strong> krijgt, rijpt: niemand heeft hem dat geleerd. Hetzelfde "
                  "geldt voor de puberteit of voor het ogenblik waarop de spieren sterk genoeg zijn om te "
                  "stappen."),
            ("p", "<strong>Leren</strong> is wat er door ervaring en oefening bij komt. Een kind dat "
                  "<strong>leert fietsen na veel vallen en opstaan</strong>, leert: zonder die uren op de "
                  "fiets gebeurt er niets."),
            ("kader", "Rijpen en leren hebben elkaar <strong>nodig</strong>. Je kan een kind niet leren "
                      "fietsen voor zijn evenwicht gerijpt is, en het rijpste evenwicht brengt niemand "
                      "vanzelf op een fiets. Het één opent de deur, het ander zet de stap."),
        ]),
        dict(kop="De negen levensloopfasen", blokken=[
            ("p", "De fiche onderscheidt <strong>negen levensloopfasen</strong>. Ze beginnen al vóór de "
                  "geboorte en lopen door tot het einde van het leven."),
            ("kader", tabel(["fase", "ongeveer"],
                            [["de <strong>prenatale fase</strong>", "vóór de geboorte, negen maanden"],
                             ["de <strong>babytijd</strong>", "0 tot 1 jaar"],
                             ["de <strong>peutertijd</strong>", "1 tot 3 jaar"],
                             ["de <strong>kleutertijd</strong>", "3 tot 6 jaar"],
                             ["de <strong>lagereschoolkindfase</strong>", "6 tot 12 jaar"],
                             ["de <strong>adolescentie</strong>", "12 tot ongeveer 20 jaar"],
                             ["de <strong>vroege volwassenheid</strong>", "20 tot 40 jaar"],
                             ["de <strong>middenvolwassenheid</strong>", "40 tot 65 jaar"],
                             ["de <strong>late volwassenheid</strong>", "vanaf ongeveer 65 jaar"]])),
            ("p", "De <strong>prenatale fase</strong> komt dus vóór de geboorte, en ze is meteen de fase die "
                  "in de levensloop <strong>het kortst duurt</strong>: negen maanden tegenover de tientallen "
                  "jaren van de volwassenheid."),
            ("p", "De <strong>kindertijd</strong> bundelt de <strong>peutertijd</strong>, de "
                  "<strong>kleutertijd</strong> en de <strong>lagereschoolkindfase</strong>. De "
                  "<strong>adolescentie</strong> is de fase tussen de kindertijd en de volwassenheid. Een "
                  "vrouw van <strong>72 die met pensioen is</strong>, zit in de <strong>late "
                  "volwassenheid</strong>."),
            ("p", "Men spreekt bewust van <strong>levensloopfasen en niet van leeftijdsgroepen</strong>, "
                  "<strong>omdat de grenzen verschuiven</strong>. De ene puber is op zijn elfde al volop "
                  "adolescent, de andere pas op zijn veertiende. Een leeftijd is een getal; een fase is een "
                  "stuk van een leven."),
            ("weetje", "Een <strong>peuter die bij alles nee zegt</strong>, zit midden in de "
                       "<strong>peutertijd</strong>. Dat nee is geen stoutheid maar ontwikkeling: het kind "
                       "ontdekt dat het een eigen wil heeft die los staat van die van zijn ouders."),
        ]),
        dict(kop="Ontwikkeling is een proces", blokken=[
            ("p", "Ontwikkeling <strong>stopt niet bij de volwassenheid</strong>. Ook een mens van veertig of "
                  "van tachtig verandert nog: in denken, in relaties, in wat hij belangrijk vindt. Dat is "
                  "precies waarom de fiche fasen tot in de late volwassenheid opsomt."),
            ("p", "Ontwikkeling is bovendien een <strong>proces</strong>, en daarvoor gelden drie dingen. Het "
                  "<strong>gebeurt stap na stap</strong>, <strong>elke stap bouwt op de vorige</strong>, en een "
                  "<strong>fase overslaan lukt moeilijk</strong>. Een kind kruipt voor het stapt, en stapt voor "
                  "het loopt."),
            ("p", "Ook de verhoudingen van het lichaam veranderen mee. De <strong>lichaamsverhoudingen van een "
                  "baby zijn niet dezelfde als die van een volwassene</strong>: het hoofd van een baby is in "
                  "verhouding veel groter, de benen veel korter. Groeien is dus niet gewoon alles evenveel "
                  "vergroten."),
            ("weetje", "Een <strong>adolescent die verschillende vriendengroepen uitprobeert</strong>, doet dat "
                       "<strong>omdat hij zoekt wie hij zelf is</strong>. Die zoektocht naar een eigen identiteit "
                       "is het werk van die fase."),
        ]),
        dict(kop="Nature, nurture en zelfbepaling", blokken=[
            ("p", "Waar komt die ontwikkeling vandaan? De fiche noemt drie factoren."),
            ("p", "<strong>Nature</strong> is <strong>de erfelijkheid</strong>: alles wat in je genen meekomt. "
                  "<strong>Je bloedgroep</strong>, <strong>je lichaamslengte als mogelijkheid</strong> en "
                  "<strong>een erfelijke aandoening</strong> horen bij nature. Let op dat woord "
                  "<em>mogelijkheid</em>: je genen bepalen hoe lang je zou kunnen worden, niet hoe lang je "
                  "wordt."),
            ("p", "<strong>Nurture</strong> is alles wat de omgeving aanbrengt: <strong>de school waar je "
                  "zit</strong>, <strong>de buurt waar je woont</strong>, <strong>de taal die thuis gesproken "
                  "wordt</strong>, de vrienden, het eten, de kansen."),
            ("p", "<strong>Zelfbepaling</strong> is de derde factor: de mens kiest ook zelf. Maar "
                  "<strong>zelfbepaling betekent niet dat je je ontwikkeling volledig zelf kiest</strong>. Je "
                  "kiest binnen wat nature en nurture je meegeven, en dat is iets anders dan vrij spel."),
            ("kader", "<strong>Nature en nurture werken samen.</strong> Een jongen die "
                      "<strong>muzikaal talent erft maar nooit oefent</strong>, mist <strong>de "
                      "oefening</strong>: de aanleg alleen levert niets op. Een <strong>tweeling die in twee "
                      "verschillende gezinnen opgroeit en sterk verschilt</strong>, toont <strong>het gewicht "
                      "van nurture</strong>: dezelfde genen, een ander resultaat. En een kind met een "
                      "spraakachterstand dat <strong>logopedie</strong> krijgt en de achterstand inhaalt, is "
                      "<strong>nurture</strong> aan het werk. In het Engels heet die wisselwerking kortweg "
                      "<strong>nature en nurture</strong>."),
        ]),
        dict(kop="De vijf ontwikkelingsdomeinen", blokken=[
            ("p", "Om overzicht te houden, verdeelt men de ontwikkeling in <strong>domeinen</strong>. De fiche "
                  "noemt er vijf: <strong>de fysieke</strong>, de cognitieve, <strong>de morele</strong>, de "
                  "socio-emotionele en <strong>de persoonlijkheidsontwikkeling</strong>. Die laatste is in de "
                  "fiche dus <strong>een eigen ontwikkelingsdomein</strong> en geen onderdeel van een ander."),
            ("kader", tabel(["domein", "waarover het gaat"],
                            [["de <strong>fysieke</strong> ontwikkeling", "het lichaam, de motoriek, de zintuigen"],
                             ["de <strong>cognitieve</strong> ontwikkeling", "<strong>het denken</strong>, het geheugen, de taal"],
                             ["de <strong>morele</strong> ontwikkeling", "<strong>goed en kwaad</strong>, waarden, geweten"],
                             ["de <strong>socio-emotionele</strong> ontwikkeling", "<strong>gevoelens en omgaan met anderen</strong>"],
                             ["de <strong>persoonlijkheids</strong>ontwikkeling", "wie iemand als persoon wordt"]])),
            ("p", "Die domeinen <strong>gaan niet los van elkaar vooruit</strong>. Een <strong>kleuter die leert "
                  "stappen en daardoor ook de keuken gaat verkennen</strong>, laat de "
                  "<strong>wisselwerking</strong> zien: een fysieke stap zet een cognitieve stap in gang."),
            ("p", "Waarom dan toch onderscheiden? <strong>Om gerichter te kijken.</strong> Wie weet welk domein "
                  "hij volgt, ziet meer dan wie alleen naar het kind in het algemeen kijkt. In de "
                  "<strong>late volwassenheid</strong> gaat <strong>het fysieke</strong> domein het duidelijkst "
                  "achteruit, terwijl het cognitieve op veel punten nog wint."),
            ("p", "De fiche vraagt ook om <strong>twee levensloopfasen binnen één domein met elkaar te "
                  "vergelijken</strong>: hoe denkt een kleuter tegenover een adolescent, hoe beweegt een baby "
                  "tegenover een oudere. Dat is een vergelijking in de breedte van één domein, niet een "
                  "opsomming van alles."),
        ]),
    ])


# ───────────────────────── 2. De fysieke ontwikkeling
zet("de-fysieke-ontwikkeling",
    titel="De fysieke ontwikkeling",
    onder="Hoe het lichaam groeit en van verhouding verandert, hoe de zintuigen scherper worden, en hoe een baby van reflexen naar gecontroleerde bewegingen gaat.",
    secties=[
        dict(kop="Lengte, gewicht en verhoudingen", blokken=[
            ("p", "De <strong>lichamelijke ontwikkeling</strong> gaat volgens de vakfiche over drie dingen: "
                  "<strong>lengte, gewicht en verhoudingen</strong>. De eerste twee zijn makkelijk te meten, "
                  "de derde zie je vooral als je kijkt."),
            ("p", "Dat <strong>de verhoudingen nog veranderen</strong>, zie je het best aan een baby: zijn "
                  "<strong>hoofd is in verhouding groot</strong>. Bij een pasgeborene is het hoofd ongeveer "
                  "<strong>een vierde van de lengte</strong>, bij een volwassene nog maar een achtste. Een "
                  "<strong>kleuter die minder mollig is dan een peuter</strong> laat hetzelfde zien: daar "
                  "veranderen <strong>de lichaamsverhoudingen</strong>, want de benen worden langer en het "
                  "babyvet verdwijnt."),
            ("p", "Daarom meet de arts bij elk consult de lengte en het gewicht: <strong>om de groeicurve te "
                  "volgen</strong>. Eén meting zegt weinig, de lijn over de tijd zegt veel. Op zo'n "
                  "<strong>groeicurve</strong> staan <strong>de lengte</strong>, <strong>het gewicht</strong> "
                  "en <strong>de leeftijd</strong> — de bloeddruk niet. Een plotse knik in de lijn vraagt "
                  "aandacht."),
            ("kader", "<strong>De prenatale fase is fysiek de belangrijkste</strong>, want "
                      "<strong>alle organen worden dan gevormd</strong>. In negen maanden ontstaat een heel "
                      "lichaam uit één cel; daarna groeit het vooral nog in omvang."),
        ]),
        dict(kop="Waar de groei het snelst gaat", blokken=[
            ("p", "Na de babytijd gaat de groei het snelst in <strong>de adolescentie</strong>. Die snelle "
                  "groei heet de <strong>groeispurt</strong>. Tussen de kleutertijd en de puberteit gaat het "
                  "trager en gelijkmatig."),
            ("p", "Bij de fysieke ontwikkeling in de adolescentie horen <strong>de groeispurt</strong>, "
                  "<strong>de geslachtsrijping</strong> en <strong>de verandering van de stem</strong>. Lezen "
                  "hoort daar niet bij: dat is cognitieve ontwikkeling."),
            ("p", "<strong>Jongens en meisjes groeien niet op hetzelfde moment.</strong> Meisjes beginnen "
                  "gemiddeld rond elf jaar, jongens rond dertien; de groeispurt komt bij meisjes dus zo'n "
                  "<strong>twee jaar vroeger</strong>. Daarom zijn meisjes in het eerste jaar secundair vaak "
                  "groter dan de jongens."),
            ("weetje", "Een <strong>kind van tien dat sport en daardoor een betere uithouding heeft</strong> "
                       "dan een kind dat stilzit, is een voorbeeld van <strong>nurture</strong>. Oefening is "
                       "omgeving: ook de fysieke ontwikkeling is niet enkel erfelijk."),
        ]),
        dict(kop="De zintuigen: de sensorische ontwikkeling", blokken=[
            ("p", "De ontwikkeling van de zintuigen heet de <strong>sensorische</strong> ontwikkeling: zien, "
                  "horen, ruiken, voelen en smaken. <strong>Scherper leren zien</strong>, <strong>stemmen "
                  "leren onderscheiden</strong> en <strong>smaken leren herkennen</strong> horen daarbij; "
                  "stappen en klimmen niet, dat is motoriek."),
            ("p", "Bij een pasgeborene werkt <strong>het zicht</strong> nog het minst scherp: hij ziet maar "
                  "twintig tot dertig centimeter ver. Horen en voelen werken al veel beter. <strong>Een baby "
                  "hoort trouwens al voor de geboorte geluiden van buiten</strong>: vanaf ongeveer de vijfde "
                  "maand werkt het gehoor, en daarom kent hij na de geboorte de stem van zijn moeder."),
            ("p", "Een <strong>baby van zes maanden steekt alles in de mond</strong> omdat <strong>hij "
                  "onderzoekt met zijn mond</strong>. De mond is in die fase zijn gevoeligste zintuig: zo "
                  "leert hij vorm en structuur kennen."),
            ("kader", "<strong>De sensorische en de motorische ontwikkeling hangen samen.</strong> Een "
                      "<strong>baby van vier maanden die grijpt naar wat hij ziet</strong>, laat zien hoe het "
                      "oog de hand stuurt. Die samenwerking van zintuigen en beweging heet "
                      "<strong>sensomotorisch</strong>. Piaget noemde het eerste stadium van het denken er "
                      "ook naar."),
        ]),
        dict(kop="Van reflex naar gecontroleerde beweging", blokken=[
            ("p", "Een <strong>reflex</strong> is <strong>een beweging zonder nadenken</strong>: ze gebeurt "
                  "vanzelf, zonder dat het kind het wil. Een pasgeborene heeft er verschillende: de "
                  "<strong>zuigreflex</strong>, de <strong>grijpreflex</strong> en de "
                  "<strong>zoekreflex</strong>, waarbij hij met zijn mond naar de tepel zoekt. Een "
                  "leesreflex bestaat niet."),
            ("p", "De <strong>grijpreflex</strong> is die waarbij een baby zijn vingers rond je vinger sluit. "
                  "Hij verdwijnt na een paar maanden en maakt plaats voor echt grijpen."),
            ("p", "<strong>Babyreflexen blijven niet het hele leven bestaan.</strong> De meeste verdwijnen in "
                  "het eerste jaar en maken plaats voor de <strong>gecontroleerde beweging</strong>: een "
                  "beweging die het kind zelf bestuurt. Een paar blijven wel, zoals de knipperreflex en de "
                  "hoestreflex."),
        ]),
        dict(kop="Grove en fijne motoriek", blokken=[
            ("kader", tabel(["motoriek", "welke spieren", "voorbeelden"],
                            [["de <strong>grove</strong> motoriek", "de grote spieren",
                              "<strong>klimmen</strong>, <strong>huppelen</strong>, <strong>een bal trappen</strong>, stappen, lopen, springen"],
                             ["de <strong>fijne</strong> motoriek", "de kleine spieren van de hand",
                              "<strong>een knoop dichtdoen</strong>, <strong>een blad omslaan</strong>, <strong>een veter knopen</strong>, schrijven"]])),
            ("p", "Een kind dat <strong>met een pen tussen drie vingers leert schrijven</strong>, oefent dus "
                  "<strong>de fijne motoriek</strong>. Die rijpt later dan de grove: <strong>de grove "
                  "motoriek ontwikkelt zich voor de fijne</strong>, want een kind stapt voor het kan knippen."),
            ("p", "Daarom oefenen kleuters zoveel met scheren, plakken en rijgen: <strong>om de fijne "
                  "motoriek te oefenen</strong>. Die oefening maakt de hand klaar om te leren schrijven; "
                  "zonder dat lukt het pennen moeilijk."),
            ("weetje", "<strong>Schrijven hoort bij de fysieke én de cognitieve ontwikkeling</strong>, want "
                       "<strong>de hand én het denken doen mee</strong>: de fijne motoriek vormt de letter, "
                       "het denken kiest het woord. Een mooi voorbeeld van wisselwerking tussen twee "
                       "domeinen."),
        ]),
        dict(kop="De orde ligt vast, het tempo niet", blokken=[
            ("p", "De motorische ontwikkeling volgt volgens de fiche twee vaste richtingen. Ze gaat "
                  "<strong>van hoofd naar voeten</strong>: een baby heft eerst het hoofd, dan de romp, dan "
                  "komt het zitten en pas daarna het stappen. En ze gaat <strong>van het midden naar "
                  "buiten</strong>, wat wil zeggen: <strong>eerst de romp, dan de handen</strong> — eerst de "
                  "grote spieren van romp en schouders, daarna de armen, de handen en pas dan de vingers."),
            ("p", "Een baby leert zich bewegen in deze orde: <strong>rollen, zitten, kruipen, stappen</strong>. "
                  "Die orde ligt vast door de rijping, het tempo niet. Sommige kinderen slaan het kruipen "
                  "over."),
            ("p", "<strong>Niet elk kind bereikt de mijlpalen op dezelfde leeftijd.</strong> Het ene kind "
                  "stapt op tien maanden, het andere op zestien, en allebei is gewoon. Enkel de volgorde is "
                  "bij iedereen dezelfde."),
            ("kader", "Een <strong>kind dat niet mag kruipen, mist oefening voor zijn motoriek</strong>. "
                      "Kruipen oefent de schouders en de samenwerking tussen links en rechts; daarom raadt "
                      "men het niet aan die fase over te slaan."),
        ]),
        dict(kop="Het lichaam blijft veranderen", blokken=[
            ("p", "<strong>De fysieke ontwikkeling loopt niet enkel in de kindertijd.</strong> Ze loopt door "
                  "de hele levensloop, en ook de achteruitgang in de late volwassenheid is fysieke "
                  "ontwikkeling."),
            ("p", "In de late volwassenheid <strong>worden de zintuigen minder scherp</strong>: het zicht en "
                  "het gehoor nemen af, en veel mensen hebben vanaf hun veertigste een leesbril nodig. De "
                  "motoriek <strong>wordt trager en minder vast</strong>: kracht, snelheid en evenwicht nemen "
                  "af. Bewegen blijft wel mogelijk, en oefening helpt."),
            ("weetje", "Een <strong>adolescent is tijdelijk onhandig na een groeispurt</strong> omdat "
                       "<strong>het lichaam te snel veranderde</strong>. De armen en benen zijn plots langer "
                       "en de besturing moet zich aanpassen. Dat gaat na een tijd vanzelf weer over."),
        ]),
    ])


# ───────────────────────── 3. De cognitieve ontwikkeling volgens Piaget
zet("de-cognitieve-ontwikkeling-volgens-piaget",
    titel="De cognitieve ontwikkeling volgens Piaget",
    onder="De vier stadia waarin het denken zich volgens Piaget ontwikkelt, met de kenmerken en de denkfouten van elk stadium.",
    secties=[
        dict(kop="Vier stadia", blokken=[
            ("p", "Piaget onderscheidt <strong>vier</strong> stadia in de cognitieve ontwikkeling. Ze komen "
                  "altijd in dezelfde orde, en elk stadium bouwt op het vorige. (Kohlberg, die je verderop "
                  "tegenkomt, had er drie — verwar de twee niet.)"),
            ("kader", tabel(["stadium", "ongeveer", "het denken"],
                            [["<strong>sensomotorisch</strong>", "0 tot 2 jaar", "met de zintuigen en de bewegingen"],
                             ["<strong>pre-operationeel</strong>", "2 tot 7 jaar", "met symbolen, maar nog niet logisch"],
                             ["<strong>concreet-operationeel</strong>", "7 tot 12 jaar", "logisch, over dingen die je kan zien"],
                             ["<strong>formeel-operationeel</strong>", "vanaf 12 jaar", "logisch, ook over wat je niet ziet"]])),
            ("p", "<strong>Het sensomotorisch stadium komt eerst</strong>, en het "
                  "<strong>formeel-operationeel stadium is het laatste</strong>. Formeel betekent daar dat "
                  "de vorm van het denken losstaat van de inhoud."),
        ]),
        dict(kop="Het sensomotorisch stadium: denken met zintuigen en bewegingen", blokken=[
            ("p", "Van de geboorte tot ongeveer twee jaar denkt het kind met wat het ziet, hoort, voelt en "
                  "doet. Drie kenmerken horen bij dit stadium: <strong>objectpermanentie</strong>, "
                  "<strong>persoonspermanentie</strong> en <strong>intentioneel handelen</strong>. "
                  "Hypothetisch denken hoort er niet bij; dat komt pas in het laatste stadium."),
            ("p", "<strong>Objectpermanentie</strong> is het weten dat iets blijft bestaan als je het niet "
                  "ziet. Rond acht maanden gaat een baby zoeken naar een bal die onder een doek verdween; "
                  "daarvoor niet. Een <strong>baby die niet zoekt naar een speeltje dat je wegstopt, mist "
                  "die objectpermanentie</strong> nog: wat hij niet ziet, bestaat voor hem niet."),
            ("p", "<strong>Persoonspermanentie</strong> is hetzelfde, maar voor mensen: het kind weet dat "
                  "<strong>mama blijft bestaan</strong> als ze de kamer uit is. Daarom begint de "
                  "scheidingsangst net rond die tijd: het kind weet dat mama ergens is, maar niet hier."),
            ("p", "<strong>Intentioneel handelen</strong> is iets doen met een doel. Een <strong>baby die een "
                  "rammelaar schudt om het geluid te horen</strong>, handelt intentioneel. Dat hoort bij het "
                  "einde van dit stadium."),
        ]),
        dict(kop="Het pre-operationeel stadium: symbolen, maar nog geen logica", blokken=[
            ("p", "Het <strong>pre-operationeel</strong> stadium (ook preoperationeel geschreven) hoort bij de "
                  "kleutertijd, ongeveer twee tot zeven jaar. Piaget noemt het zo omdat <strong>het logisch rekenen nog niet komt</strong>: "
                  "operaties zijn logische bewerkingen in het hoofd, en die komen pas in het volgende stadium."),
            ("p", "Wat er wel is, is het <strong>symbolisch denken</strong>: één ding staat voor een ander. "
                  "Een <strong>kleuter die een stok als zwaard gebruikt</strong>, denkt symbolisch. Datzelfde "
                  "vermogen maakt taal en doen-alsof-spel mogelijk."),
            ("p", "<strong>Fantasie en werkelijkheid zijn voor een kleuter niet altijd duidelijk "
                  "gescheiden.</strong> Een kleuter kan echt bang zijn van een monster onder het bed, en dat "
                  "hoort gewoon bij dit stadium."),
        ]),
        dict(kop="De denkfouten van de kleutertijd", blokken=[
            ("p", "Bij het pre-operationeel stadium horen een paar typische denkfouten: "
                  "<strong>animisme</strong>, <strong>centratie</strong> en <strong>magisch denken</strong>. "
                  "Abstract denken staat niet in dat rijtje: dat is geen fout, en het komt pas in het laatste "
                  "stadium."),
            ("kader", tabel(["denkfout", "wat ze is", "voorbeeld"],
                            [["<strong>animisme</strong>", "levenloze dingen gevoelens geven",
                              "<strong>de zon is boos</strong>, de pop heeft pijn, de auto is moe"],
                             ["<strong>magisch denken</strong>", "een verband leggen dat er niet is",
                              "<strong>het regent omdat ik stout was</strong>"],
                             ["<strong>centratie</strong>", "op één kenmerk letten en de rest vergeten",
                              "bij <strong>twee glazen water alleen naar de hoogte kijken</strong>"],
                             ["<strong>egocentrisme</strong>", "alleen het eigen standpunt kunnen innemen",
                              "hij denkt dat jij ziet wat hij ziet"]])),
            ("p", "<strong>Egocentrisme betekent bij Piaget niet dat een kleuter egoïstisch is.</strong> Het "
                  "is geen karaktertrek maar een denkgrens: hij kan zich nog niet voorstellen hoe iets er van "
                  "jouw plaats uitziet."),
            ("p", "<strong>Niet-reversibel denken</strong> betekent dat een kind <strong>een bewerking niet "
                  "kan terugdraaien</strong> in zijn hoofd. Een kleuter die het water terug overgiet, "
                  "begrijpt niet dat het dan weer gelijk is."),
            ("p", "De <strong>conservatienotie</strong> is het <strong>weten dat de hoeveelheid blijft</strong> "
                  "als de vorm verandert. Een kleuter heeft die notie nog niet: rol je <strong>een bol klei "
                  "uit tot een worst</strong>, dan zegt hij dat er nu meer klei is. Het is de klassieke proef "
                  "van Piaget — dezelfde klei, een andere vorm, en toch denkt hij meer."),
        ]),
        dict(kop="Het concreet-operationeel stadium: logica met dingen erbij", blokken=[
            ("p", "Het <strong>concreet-operationeel</strong> stadium hoort bij de lagereschoolkindfase, "
                  "ongeveer zeven tot twaalf jaar. Het kind denkt nu logisch, maar nog over dingen die het "
                  "kan zien of vastnemen."),
            ("p", "Kenmerkend zijn <strong>seriatie</strong>, <strong>classificatie</strong> en "
                  "<strong>reversibel denken</strong>. Magisch denken hoort niet in dat rijtje; dat is van de "
                  "kleutertijd."),
            ("kader", tabel(["begrip", "wat het is"],
                            [["<strong>seriatie</strong>", "<strong>op grootte sorteren</strong>: stokjes van klein naar groot leggen"],
                             ["<strong>classificatie</strong>", "verdelen in groepen volgens een kenmerk: alle rode blokken samen"],
                             ["<strong>reversibel denken</strong> (reversibiliteit)", "een bewerking in gedachten terugdraaien: wie weet dat 3 + 4 = 7, weet ook dat 7 − 4 = 3"],
                             ["<strong>decentreren</strong>", "<strong>op meer kenmerken letten</strong>, het tegengestelde van centratie: nu ziet het kind de hoogte én de breedte"],
                             ["<strong>transitieve interferentie</strong>", "uit twee vergelijkingen de derde afleiden"],
                             ["<strong>perspectief nemen</strong>", "kunnen uitleggen hoe iemand anders iets ziet"]])),
            ("p", "<strong>Transitieve interferentie</strong> herken je aan dit soort redenering: An is groter "
                  "dan Bo, Bo is groter dan Cis, dus An is groter dan Cis — zonder An en Cis naast elkaar te "
                  "zetten. En een <strong>kind dat kan uitleggen hoe zijn zus de kamer ziet</strong>, neemt "
                  "perspectief: het egocentrisme van de kleutertijd is voorbij."),
            ("p", "<strong>Aandacht voor de begin- en de eindtoestand hoort bij dit stadium</strong>, niet bij "
                  "het pre-operationele. Een kleuter ziet alleen hoe het nu is; een lagereschoolkind kan de "
                  "weg ernaartoe meedenken."),
            ("p", "De grens van dit stadium zit in het woord <em>concreet</em>. Een <strong>kind van negen kan "
                  "nog moeilijk denken over iets dat het nooit zag</strong>: een stelling als <em>stel dat de "
                  "zwaartekracht wegvalt</em> lukt nog niet. En een <strong>kind van elf dat breuken begrijpt "
                  "met stukken pizza maar niet zonder</strong>, zit nog in het "
                  "<strong>concreet-operationeel</strong> stadium: de logica werkt, maar ze heeft een "
                  "concreet beeld nodig. Daarom werkt materiaal zo goed in de lagere school."),
        ]),
        dict(kop="Het formeel-operationeel stadium: denken los van wat er ligt", blokken=[
            ("p", "Vanaf ongeveer twaalf jaar, in de adolescentie, komt het "
                  "<strong>formeel-operationeel</strong> stadium. Kenmerkend zijn <strong>abstract "
                  "denken</strong>, <strong>logisch redeneren</strong> en <strong>experimenteel "
                  "denken</strong>. Objectpermanentie hoort daar niet bij: dat is van een baby."),
            ("p", "<strong>Abstract denken</strong> is <strong>denken zonder iets te zien</strong>: over "
                  "rechtvaardigheid, over x in een vergelijking, over een land dat je nooit bezocht. "
                  "<strong>Hypothetisch denken is denken in als-dan</strong>: stel dat ik dit verander, wat "
                  "gebeurt er dan. Precies dat heb je nodig om een proef op te zetten."),
            ("p", "<strong>Experimenteel denken</strong> zie je bij een <strong>adolescent die een proef "
                  "opzet met één factor die hij verandert</strong>. Alles gelijk houden en één ding "
                  "veranderen is de kern van wetenschappelijk werken."),
            ("weetje", "Een <strong>adolescent kan over de toekomst piekeren en een kleuter niet</strong>, "
                       "omdat <strong>hij denkt over wat nog niet is</strong>. Hypothetisch denken opent de "
                       "toekomst, en dus ook de zorgen erover."),
            ("p", "<strong>Niet iedereen bereikt dit stadium volledig</strong>, en zeker niet in elk domein. "
                  "In een vak dat je niet kent, denk je vaak nog concreet."),
        ]),
        dict(kop="Waarom die stadia nuttig zijn", blokken=[
            ("p", "De fiche geeft er één reden voor: <strong>je weet wat een kind aankan</strong>. Wie weet "
                  "in welk stadium een kind denkt, kan zijn uitleg daarop afstemmen. Kinderen met elkaar "
                  "vergelijken is uitdrukkelijk niet het doel."),
        ]),
    ])


# ───────────────────────── 4. De morele ontwikkeling volgens Kohlberg
zet("de-morele-ontwikkeling-volgens-kohlberg",
    titel="De morele ontwikkeling volgens Kohlberg",
    onder="De drie stadia waarin het morele denken zich ontwikkelt, met de redenen die bij elk stadium horen en het dilemma waarmee Kohlberg ze opspoorde.",
    secties=[
        dict(kop="Waarover de morele ontwikkeling gaat", blokken=[
            ("p", "De morele ontwikkeling gaat over <strong>goed en kwaad</strong>: over wat je juist of "
                  "fout vindt, en vooral over <strong>waaróm</strong> je dat vindt."),
            ("p", "Dat <em>waarom</em> is bij Kohlberg de hele zaak. Hij kijkt naar <strong>de reden achter "
                  "het antwoord</strong>, niet naar de daad. Twee mensen kunnen precies hetzelfde doen om "
                  "een heel andere reden, en dan zitten ze in een ander stadium. <strong>Kohlberg vond dus "
                  "niet dat je het stadium afleest uit de daad</strong> — precies omgekeerd: de daad zegt "
                  "niets, de redenering erachter wel."),
            ("kader", "<strong>Twee mensen stelen niet.</strong> De een uit angst voor de politie, de ander "
                      "omdat hij eerlijkheid belangrijk vindt. Dezelfde daad, een andere reden: "
                      "<strong>ze zitten in een ander stadium</strong>. De eerste is pre-conventioneel, de "
                      "tweede post-conventioneel."),
            ("p", "<strong>De morele ontwikkeling staat niet los van de cognitieve ontwikkeling.</strong> "
                  "Ze hangen samen: je kan pas over een beginsel redeneren als je abstract kan denken. En "
                  "een <strong>peuter die nog niet weet dat slaan pijn doet bij een ander</strong>, mist "
                  "<strong>het perspectief nemen</strong>. Zonder je in een ander te verplaatsen, kan er "
                  "geen moreel oordeel ontstaan."),
        ]),
        dict(kop="Het moreel dilemma als meetlat", blokken=[
            ("p", "<strong>Kohlberg gebruikte verhaaltjes met een moeilijke keuze</strong> om het stadium te "
                  "bepalen. Zo'n verhaal heet een <strong>moreel dilemma</strong>."),
            ("p", "Drie dingen kenmerken een moreel dilemma: <strong>er is geen goed antwoord</strong>, "
                  "<strong>je moet je keuze uitleggen</strong> en <strong>beide keuzes kosten iets</strong>. "
                  "Elke keuze botst met iets dat je belangrijk vindt, en juist daarom toont de uitleg het "
                  "stadium."),
            ("p", "Het bekendste is het <strong>dilemma van Heinz</strong>: een man steelt een duur medicijn "
                  "voor zijn doodzieke vrouw. Kohlberg vraagt dan niet of de vrouw genezen is, maar "
                  "<strong>of het mag, en waarom</strong>. Het antwoord ja of nee zegt niets; de uitleg "
                  "erbij zegt alles."),
        ]),
        dict(kop="Drie stadia", blokken=[
            ("p", "Kohlberg onderscheidt <strong>drie</strong> stadia. (Piaget had er vier, maar die gingen "
                  "over het denken, niet over de moraal.) Het "
                  "<strong>pre-conventioneel</strong> stadium komt eerst, het "
                  "<strong>post-conventioneel</strong> stadium is het laatste."),
            ("kader", tabel(["stadium", "waar iemand naar kijkt", "typische reden"],
                            [["<strong>pre-conventioneel</strong>", "<strong>het gevolg voor zichzelf</strong>",
                              "ik word anders gestraft"],
                             ["<strong>conventioneel</strong>", "<strong>de regels en de groep</strong>",
                              "het staat zo in de wet"],
                             ["<strong>post-conventioneel</strong>", "een beginsel boven de regel",
                              "deze wet is onrechtvaardig"]])),
            ("p", "Over die drie stadia klopt het volgende: <strong>de orde ligt vast</strong>, <strong>een "
                  "stadium overslaan gaat niet</strong> en <strong>de reden telt, niet de daad</strong>. "
                  "<strong>Ze volgen elkaar vast op</strong>, net als bij Piaget: de orde ligt vast, het "
                  "tempo niet. De leeftijd zegt daarbij weinig — twee mensen van dertig kunnen in een ander "
                  "stadium zitten."),
            ("p", "<strong>Niet iedereen doorloopt de drie stadia volledig.</strong> Veel mensen blijven in "
                  "het conventionele stadium, en het post-conventionele bereikt lang niet iedereen."),
        ]),
        dict(kop="Het pre-conventionele stadium: straf en beloning", blokken=[
            ("p", "Kohlberg noemt dit stadium <strong>pre-conventioneel</strong> omdat <strong>de regels nog "
                  "niet meetellen</strong>. Conventies zijn afspraken en regels; in dit stadium kijkt het "
                  "kind enkel naar het gevolg voor zichzelf."),
            ("p", "Wat het gedrag stuurt, is <strong>straf en beloning</strong>: goed is wat beloond wordt, "
                  "fout is wat gestraft wordt. Het kind kijkt naar het gevolg, niet naar de regel. De "
                  "redenen die hier horen, klinken dan ook zo: <strong>ik word anders gestraft</strong>, "
                  "<strong>ik krijg er iets voor terug</strong>, <strong>ik wil geen last krijgen</strong>. "
                  "De wet noemen hoort niet in dat rijtje; dat is al conventioneel."),
            ("kader", tabel(["voorbeeld", "waarom pre-conventioneel"],
                            [["een kind steelt niet <strong>omdat het bang is voor straf</strong>",
                              "straf stuurt het gedrag, niet een regel of beginsel"],
                             ["een kleuter deelt zijn koek <strong>omdat hij er een snoepje voor krijgt</strong>",
                              "delen om er iets voor terug te krijgen is ruilen; de ander telt nog niet mee als persoon"],
                             ["een kind gehoorzaamt <strong>enkel als de juf kijkt</strong>",
                              "zonder toezicht is er geen gevolg, en dus geen reden om zich in te houden"]])),
            ("p", "Dit stadium hoort meestal bij <strong>de kindertijd</strong>, vooral bij kleuters en "
                  "jonge lagereschoolkinderen. Maar een volwassene kan er ook in terugvallen."),
            ("p", "<strong>Wie in dit stadium zit, kan zich moeilijk in een ander verplaatsen.</strong> Het "
                  "eigen gevolg staat voorop. Dat past bij het egocentrisme dat Piaget in dezelfde jaren "
                  "beschrijft."),
        ]),
        dict(kop="Het conventionele stadium: de regels en de groep", blokken=[
            ("p", "In het <strong>conventionele</strong> stadium kijkt iemand naar <strong>de regels en de "
                  "groep</strong>. Goed is wat de groep of de wet verwacht; de eigen voordelen tellen minder "
                  "mee. Conventies zijn afspraken, regels en gewoontes — vandaar de naam."),
            ("p", "De redenen klinken hier zo: <strong>het staat zo in de wet</strong>, <strong>zo hoort het "
                  "nu eenmaal</strong>, <strong>anders ben ik geen goede vriend</strong>. De wet, de gewoonte "
                  "en de verwachting van anderen dus — straf hoort bij het eerste stadium."),
            ("kader", tabel(["voorbeeld", "waarom conventioneel"],
                            [["een jongen rookt niet <strong>omdat zijn vrienden dat stom zouden vinden</strong>",
                              "wat de groep ervan vindt, geeft de doorslag"],
                             ["een meisje helpt haar zus <strong>omdat ze vindt dat je familie helpt</strong>",
                              "ze volgt de verwachting van haar rol: zo hoort het in een gezin"]])),
            ("p", "<strong>Veel volwassenen blijven in dit stadium</strong>, en daar is niets mis mee: de "
                  "regels en de wet volgen is voor de meeste mensen voldoende. Het is zelfs nuttig voor een "
                  "samenleving, want <strong>de meeste mensen volgen dan de regels</strong>, ook zonder "
                  "toezicht. Een samenleving werkt juist doordat mensen zich aan afspraken houden."),
        ]),
        dict(kop="Het post-conventionele stadium: beginselen boven de regel", blokken=[
            ("p", "In het <strong>post-conventionele</strong> stadium staan eigen beginselen boven de regel. "
                  "Kenmerkend is: <strong>eigen beginselen wegen zwaar</strong>, <strong>een regel kan je "
                  "afwegen</strong> en <strong>rechtvaardigheid gaat voor</strong>. Wie hier zit, weegt een "
                  "regel af tegen een beginsel als rechtvaardigheid of menselijke waardigheid."),
            ("p", "Zo klinken de uitspraken van dit stadium: <strong>een wet kan onrechtvaardig zijn</strong>, "
                  "<strong>menselijke waardigheid gaat voor</strong>, <strong>regels zijn afspraken die je "
                  "kan wegen</strong>. Iemand die <strong>betoogt tegen een wet die hij onrechtvaardig "
                  "vindt</strong>, zit in dit stadium: de wet wordt niet zomaar gevolgd maar afgewogen tegen "
                  "een hoger beginsel."),
            ("kader", "<strong>Dit stadium betekent niet dat je alle regels mag overtreden.</strong> Het "
                      "betekent dat je een regel kan afwegen tegen een beginsel, niet dat regels er niet "
                      "meer toe doen. Dat verschil is het halve antwoord op een examenvraag hierover."),
            ("p", "<strong>Dit stadium hoort niet bij een kind</strong>, want <strong>het vraagt abstract "
                  "denken</strong>. Over een beginsel redeneren vraagt het formeel-operationele denken van "
                  "Piaget, en dat komt pas vanaf de adolescentie. Een <strong>adolescent die de regels van "
                  "thuis in vraag begint te stellen</strong>, <strong>groeit naar een volgend "
                  "stadium</strong>: een regel bevragen hoort bij de overgang van het conventionele naar het "
                  "post-conventionele denken."),
            ("p", "<strong>Een volwassene kan in een lastige situatie terugvallen op een lager "
                  "stadium.</strong> Onder druk of angst gaat het eigen gevolg vaak weer voorop. Dat maakt "
                  "de theorie niet minder bruikbaar."),
        ]),
        dict(kop="De kritiek op Kohlberg", blokken=[
            ("p", "De theorie is bekritiseerd omdat <strong>ze rechtvaardigheid het zwaarst weegt</strong>. "
                  "Critici zoals Carol Gilligan vinden dat zorgen voor elkaar even zwaar weegt als "
                  "rechtvaardigheid, en dat wie vanuit zorg redeneert in Kohlbergs schema te laag "
                  "uitkomt."),
        ]),
    ])


# ───────────────────────── 5. De sociale ontwikkeling en de gehechtheid
zet("de-sociale-ontwikkeling-en-de-gehechtheid",
    titel="De sociale ontwikkeling en de gehechtheid",
    onder="De mijlpalen in het omgaan met anderen en met je eigen gevoelens, en de vier hechtingspatronen met hun gevolgen.",
    secties=[
        dict(kop="Twee kanten in één domein", blokken=[
            ("p", "De socio-emotionele ontwikkeling bestaat uit <strong>de sociale en de emotionele</strong> "
                  "ontwikkeling: omgaan met anderen, en omgaan met je eigen gevoelens."),
            ("p", "Bij de <strong>emotionele</strong> kant hoort <strong>leren omgaan met je "
                  "gevoelens</strong>: ze herkennen, benoemen en sturen. Dat loopt het hele leven door. Het "
                  "sturen heet <strong>emotieregulatie</strong>: <strong>je gevoel kunnen sturen</strong>, "
                  "en dat is niet hetzelfde als het onderdrukken — rustig worden, uitstellen, een andere "
                  "uitweg zoeken."),
            ("p", "<strong>Een baby van twee maanden kan zijn eigen gevoelens nog niet benoemen.</strong> "
                  "Hij voelt wel, maar heeft er geen woorden voor; benoemen komt pas met de taal, in de "
                  "peutertijd. En een <strong>peuter die een woedebui krijgt</strong>, laat zien dat "
                  "<strong>hij zijn gevoel nog niet kan sturen</strong>: het gevoel is er wel, de rem nog "
                  "niet. Die komt met de rijping van de hersenen."),
            ("kader", "De grootste stap in de emotieregulatie valt in <strong>de kleutertijd</strong>. Met "
                      "de taal komt het benoemen, en met het benoemen het sturen. Daarom helpt het een "
                      "kleuter zo om zijn gevoel voor hem te benoemen: <em>je bent boos omdat je toren "
                      "omviel</em>."),
            ("p", "<strong>De socio-emotionele ontwikkeling stopt niet na de adolescentie.</strong> Ze loopt "
                  "door: een relatie, ouder worden en afscheid nemen vragen allemaal nieuwe stappen."),
        ]),
        dict(kop="De mijlpalen van de sociale ontwikkeling", blokken=[
            ("p", "Een <strong>mijlpaal</strong> is <strong>een stap die de meeste kinderen zetten</strong>, "
                  "zoals de eerste glimlach of het samen spelen. De orde ligt vrij vast, de leeftijd niet: "
                  "<strong>mijlpalen komen bij het ene kind later dan bij het andere</strong>. De spreiding "
                  "is groot, dus één late mijlpaal zegt weinig; pas als er meerdere uitblijven, kijkt men "
                  "verder."),
            ("kader", tabel(["fase", "mijlpalen"],
                            [["de babytijd",
                              "<strong>de sociale glimlach</strong>, <strong>de eigen naam herkennen</strong>, <strong>de armpjes strekken om opgenomen te worden</strong>"],
                             ["de peutertijd", "<strong>parallel spel</strong>: naast elkaar spelen met eigen speelgoed"],
                             ["de kleutertijd",
                              "<strong>samen spelen met rollen</strong>, <strong>een vriendje kiezen</strong>, <strong>beurt leren afwachten</strong>"],
                             ["de adolescentie", "de <strong>peergroep</strong> wordt de belangrijkste groep"]])),
            ("p", "De <strong>sociale glimlach</strong> is de eerste glimlach naar een gezicht, rond zes "
                  "weken. Hij is <em>gericht aan iemand</em>; daarvoor lacht een baby ook, maar niet naar "
                  "iemand."),
            ("p", "<strong>Parallel spel</strong> komt vóór het samen spelen: twee peuters kijken naar "
                  "elkaar maar spelen nog apart. <strong>Een kleuter kan al echt samen spelen met een rol "
                  "voor elk kind</strong>: in de kleutertijd komt het doen-alsof-spel met rollen — "
                  "winkeltje, dokter, gezin."),
            ("p", "In de adolescentie wordt de <strong>peergroep</strong>, de leeftijdsgenoten, de "
                  "belangrijkste groep. Dat is niet omdat de ouders niet meer nodig zijn, maar omdat "
                  "<strong>de peergroep helpt bij het zoeken naar jezelf</strong>: spiegelen aan "
                  "leeftijdsgenoten hoort bij het vormen van een identiteit. Het gezin blijft belangrijk, "
                  "maar krijgt een andere plaats."),
        ]),
        dict(kop="Prosociaal en antisociaal gedrag", blokken=[
            ("p", "<strong>Prosociaal gedrag</strong> is <strong>gedrag dat anderen helpt</strong>: helpen, "
                  "delen, troosten. Een <strong>kind van acht dat een vriendje troost dat gevallen is</strong>, "
                  "laat prosociaal gedrag zien: het ziet het gevoel van een ander en doet er iets mee. Dat "
                  "vraagt perspectief nemen."),
            ("p", "Het tegengestelde is <strong>antisociaal</strong> gedrag: gedrag dat anderen schaadt. De "
                  "fiche ziet dat als een gevolg van mislukte socialisatie."),
            ("p", "Dat prosociale gedrag verklaart ook waarom <strong>de sociale ontwikkeling samenhangt met "
                  "het denken</strong>: <strong>je moet een ander kunnen begrijpen</strong>. Perspectief "
                  "nemen is een cognitieve stap, en zonder die stap blijft samenwerken moeilijk."),
        ]),
        dict(kop="Wat gehechtheid is", blokken=[
            ("p", "<strong>Gehechtheid</strong> is <strong>een duurzame band met een verzorger</strong>: een "
                  "band die blijft, ook als de verzorger even weg is. Ze ontstaat in het eerste levensjaar."),
            ("p", "Ze groeit vooral <strong>uit antwoorden op signalen</strong>. Een baby huilt en er komt "
                  "troost; die herhaling bouwt het vertrouwen op. Niet de klok dus, en niet de hoeveelheid "
                  "tijd, maar het antwoord."),
            ("p", "<strong>Een kind kan zich aan meer dan één persoon hechten</strong>: aan beide ouders, aan "
                  "grootouders, aan een vaste begeleider. Meestal is er wel één hoofdfiguur."),
            ("p", "Hechting is belangrijk voor de latere ontwikkeling omdat <strong>ze het beeld van "
                  "relaties vormt</strong>. Wie leert dat anderen betrouwbaar zijn, gaat later met dat beeld "
                  "een relatie in. Vastleggen doet ze niets: <strong>een hechtingspatroon ligt na het eerste "
                  "jaar niet voorgoed vast</strong>. Het is taai maar niet onveranderlijk, en een nieuwe "
                  "vaste band kan het beeld bijsturen."),
            ("weetje", "Klassiek onderzocht men hechting <strong>met een scheiding en hereniging</strong>: "
                       "de vreemde-situatieproef van Mary Ainsworth. Niet het weggaan maar "
                       "<strong>de hereniging</strong> zegt het meest over het patroon."),
        ]),
        dict(kop="Vier hechtingspatronen", blokken=[
            ("p", "Naast de veilige hechting onderscheidt de vakfiche <strong>drie</strong> vormen van "
                  "onveilige hechting: <strong>angstig-vermijdend</strong>, "
                  "<strong>angstig-ambivalent</strong> en <strong>gedesorganiseerd</strong> of "
                  "gedesoriënteerd. <em>Zelfstandig-vermijdend</em> bestaat niet als term; dat is een "
                  "verzonnen antwoord."),
            ("kader", tabel(["patroon", "wat je ziet", "waar het van komt"],
                            [["<strong>veilige hechting</strong>",
                              "het kind <strong>durft te verkennen</strong>: het speelt rustig, kijkt af en toe of mama er nog is en gaat verder",
                              "de verzorger reageerde voorspelbaar en warm"],
                             ["<strong>angstig-vermijdend</strong>",
                              "het kind <strong>negeert zijn moeder als ze terugkomt</strong>",
                              "het heeft geleerd dat vragen weinig oplevert; van binnen is er wel spanning"],
                             ["<strong>angstig-ambivalent</strong>",
                              "het wisselt tussen vastklampen en wegduwen: het wil troost en weert ze tegelijk af",
                              "de reactie was <strong>onvoorspelbaar</strong>: soms troost, soms niets"],
                             ["<strong>gedesorganiseerd</strong>",
                              "<strong>bevriezen en verwarring</strong> bij de terugkeer van de ouder",
                              "er is geen vaste strategie: de verzorger is tegelijk de bron van troost en van angst"]])),
            ("p", "Verkennen én terugkeren is dus het beeld van veilige hechting. Een <strong>veilig gehecht "
                  "kind durft verder weg te spelen omdat het weet dat het kan terugkeren</strong>: de veilige "
                  "haven maakt verkennen mogelijk. Angst is er wel, maar ze blokkeert niet."),
            ("p", "Wordt een <strong>baby soms getroost en soms genegeerd</strong>, dan ligt "
                  "<strong>angstig-ambivalent</strong> voor de hand. Onvoorspelbaarheid maakt een kind "
                  "waakzaam: het klampt zich vast om maar zeker te zijn."),
            ("p", "Wat een verzorger kan doen om veilige hechting te helpen, staat in drie woorden: "
                  "<strong>signalen opmerken</strong>, <strong>warm reageren</strong> en <strong>voorspelbaar "
                  "reageren</strong>. Altijd meteen ingrijpen hoort daar níét bij: dan laat je een kind niets "
                  "zelf oplossen."),
        ]),
        dict(kop="De gevolgen van een band", blokken=[
            ("p", "De fiche noemt drie gevolgen van hechting: <strong>scheidingsangst</strong>, "
                  "<strong>angst voor vreemden</strong> en <strong>veilig durven verkennen</strong>. "
                  "Stappen hoort er niet bij; dat is motoriek."),
            ("p", "<strong>Scheidingsangst</strong> is de angst van een baby als zijn verzorger weggaat. Ze "
                  "begint rond acht maanden en wordt in de peutertijd weer minder. De <strong>angst voor "
                  "vreemden</strong> komt <strong>rond acht maanden</strong>, samen met de "
                  "persoonspermanentie: het kind herkent nu wie vertrouwd is en wie niet."),
            ("kader", "<strong>Scheidingsangst wijst er níét op dat een kind onveilig gehecht is.</strong> "
                      "Juist omgekeerd: ze is een normaal gevolg van hechting. Het kind weet nu dat de "
                      "verzorger blijft bestaan, maar niet waar hij is — en dat is wat de angst maakt."),
        ]),
    ])


# ───────────────────────── 6. De psychosociale ontwikkeling volgens Erikson
zet("de-psychosociale-ontwikkeling-volgens-erikson",
    titel="De psychosociale ontwikkeling volgens Erikson",
    onder="De acht conflicten van een mensenleven, met hun twee polen, de kracht die uit elk conflict groeit, en hoe je een voorbeeld plaatst.",
    secties=[
        dict(kop="Acht conflicten, elk met twee polen", blokken=[
            ("p", "Erikson onderscheidt <strong>acht</strong> conflicten, één per levensloopfase, van de "
                  "babytijd tot de late volwassenheid. Hij hangt elke fase aan een levensloopfase omdat "
                  "<strong>elke leeftijd eigen eisen heeft</strong>: een peuter krijgt andere eisen dan een "
                  "scholier, en daaruit volgt telkens een andere spanning."),
            ("p", "Een <strong>conflict</strong> is bij Erikson <strong>een spanning tussen twee "
                  "polen</strong>: twee uitersten waartussen je het evenwicht zoekt, bijvoorbeeld "
                  "vertrouwen en wantrouwen."),
            ("kader", "<strong>Een conflict moet niet volledig naar één pool overhellen.</strong> Een beetje "
                      "wantrouwen is nuttig. Dat een conflict <em>opgelost</em> is, betekent dat "
                      "<strong>de goede pool het overwicht heeft</strong> — niet alles of niets. Er blijft "
                      "iets van de andere pool over, en dat is gezond."),
            ("p", "<strong>De acht fasen stoppen niet bij het einde van de puberteit.</strong> Ze lopen tot "
                  "het einde van het leven, en daarin verschilt Erikson van Freud, die wel bij de puberteit "
                  "stopte. En <strong>een niet opgelost conflict kan later nog bijgestuurd worden</strong>: "
                  "een latere ervaring kan een oude pool nog verschuiven. Het wordt alleen moeilijker."),
        ]),
        dict(kop="De acht fasen op een rij", blokken=[
            ("kader", tabel(["fase", "conflict", "kracht"],
                            [["de babytijd", "<strong>vertrouwen versus wantrouwen</strong>", "<strong>hoop</strong>"],
                             ["de peutertijd", "<strong>autonomie versus twijfel</strong> en schaamte", "<strong>wil</strong> of wilskracht"],
                             ["de kleutertijd", "<strong>initiatief versus schuld</strong>", "<strong>doelgerichtheid</strong>"],
                             ["het lagere schoolkind", "<strong>handvaardigheid versus minderwaardigheid</strong>", "<strong>competentie</strong>"],
                             ["de adolescentie", "<strong>identiteit versus identiteitsverwarring</strong>", "<strong>trouw</strong>"],
                             ["de vroege volwassenheid", "<strong>intimiteit versus isolatie</strong>", "<strong>liefde</strong>"],
                             ["de middenvolwassenheid", "<strong>generativiteit versus stagnatie</strong>", "<strong>zorg</strong>"],
                             ["de late volwassenheid", "<strong>integriteit versus wanhoop</strong> en weerzin", "<strong>wijsheid</strong>"]])),
            ("p", "Bij de <strong>eerste drie</strong> fasen horen dus de krachten <strong>hoop</strong>, "
                  "<strong>wil</strong> en <strong>doelgerichtheid</strong>; wijsheid komt pas bij de "
                  "laatste. En bij de <strong>laatste vier</strong> horen <strong>trouw</strong>, "
                  "<strong>liefde</strong>, <strong>zorg</strong> en wijsheid; hoop hoort bij de eerste "
                  "fase."),
            ("p", "De conflicten die <strong>vóór de adolescentie</strong> spelen, zijn de eerste drie: "
                  "<strong>vertrouwen versus wantrouwen</strong>, <strong>autonomie versus twijfel</strong> "
                  "en <strong>initiatief versus schuld</strong>. De conflicten die <strong>pas vanaf de "
                  "volwassenheid</strong> spelen, zijn de laatste drie: <strong>intimiteit versus "
                  "isolatie</strong>, <strong>generativiteit versus stagnatie</strong> en "
                  "<strong>integriteit versus wanhoop</strong>."),
        ]),
        dict(kop="De vier fasen van de kindertijd", blokken=[
            ("p", "In de <strong>babytijd</strong> gaat het om <strong>vertrouwen versus wantrouwen</strong>, "
                  "en de kracht die eruit groeit is <strong>hoop</strong>. Een <strong>baby die getroost "
                  "wordt als hij huilt</strong>, bereikt de pool <strong>vertrouwen</strong>: de wereld is "
                  "betrouwbaar."),
            ("p", "In de <strong>peutertijd</strong> speelt <strong>autonomie versus twijfel</strong> en "
                  "schaamte, met de <strong>wil</strong> als kracht. Een <strong>peuter die zelf zijn jas "
                  "wil aantrekken en boos wordt als het niet mag</strong>, zit precies in dat conflict. Wie "
                  "altijd geholpen wordt, krijgt twijfel en schaamte in plaats van autonomie; een peuter die "
                  "mag proberen, leert dat zijn eigen wil iets waard is."),
            ("p", "<strong>Initiatief versus schuld hoort bij de kleutertijd.</strong> De kleuter verzint "
                  "plannen en wil ze uitvoeren; lukt dat, dan groeit <strong>doelgerichtheid</strong>: een "
                  "plan maken en het durven uitvoeren. Een <strong>kleuter die een hut bouwt en niemand om "
                  "toestemming vraagt</strong>, neemt initiatief. Wordt hij daarvoor steeds berispt, dan "
                  "blijft er schuld over."),
            ("p", "Bij het <strong>lagere schoolkind</strong> gaat het om <strong>handvaardigheid versus "
                  "minderwaardigheid</strong>, met <strong>competentie</strong> als kracht: het gevoel dat "
                  "je iets kan. Het kind leert lezen, rekenen en sporten. Een <strong>kind dat op school "
                  "altijd faalt, loopt het risico op minderwaardigheid</strong> — de negatieve pool van deze "
                  "fase. Daarom telt een succeservaring op die leeftijd zo zwaar."),
        ]),
        dict(kop="Van adolescent tot oudere", blokken=[
            ("p", "In de <strong>adolescentie</strong> speelt <strong>identiteit versus "
                  "identiteitsverwarring</strong>, met <strong>trouw</strong> als kracht: trouw aan wie je "
                  "bent en aan wat je belangrijk vindt. Een <strong>jongere die verschillende stijlen, "
                  "groepen en meningen uitprobeert</strong>, zit in dat conflict; uitproberen hoort erbij, "
                  "want zo ontstaat een eigen identiteit. <strong>Identiteitsverwarring betekent dat iemand "
                  "niet weet wie hij wil zijn</strong>: geen eigen lijn, geen richting. Erikson noemde het "
                  "ook een identiteitscrisis."),
            ("p", "In de <strong>vroege volwassenheid</strong> volgt <strong>intimiteit versus "
                  "isolatie</strong>, met <strong>liefde</strong> als kracht: je durven verbinden zonder "
                  "jezelf te verliezen. <strong>Iemand van 28 die zich niet durft te binden in een "
                  "relatie</strong>, zit in dat conflict. Die fase hangt samen met de vorige, want "
                  "<strong>je moet eerst weten wie je bent</strong>: je kan je niet binden als je jezelf nog "
                  "zoekt."),
            ("p", "Daarna komt <strong>generativiteit versus stagnatie</strong>, met <strong>zorg</strong> "
                  "als kracht: aandacht voor wie na jou komt. Onder generativiteit valt "
                  "<strong>kinderen opvoeden</strong>, <strong>jonge collega's opleiden</strong> en "
                  "<strong>een vereniging dragen</strong> — iets doorgeven dus; sparen voor jezelf hoort er "
                  "niet bij. Een <strong>vrouw van 50 die op het werk jonge collega's opleidt</strong>, "
                  "bereikt de pool <strong>generativiteit</strong>. <strong>Stagnatie is de negatieve pool</strong>: "
                  "het gevoel dat er niets vooruitgaat en dat je niets nalaat."),
            ("p", "In de <strong>late volwassenheid</strong> staat <strong>integriteit versus wanhoop</strong> "
                  "en weerzin, met <strong>wijsheid</strong> als kracht: met afstand naar je eigen leven "
                  "kunnen kijken. <strong>Integriteit betekent hier niet dat je eerlijk bent tegenover "
                  "anderen</strong>, maar dat je met vrede terugkijkt op je leven, als een geheel dat klopt. "
                  "Een <strong>man van 80 die terugkijkt en vindt dat hij veel gemist heeft</strong>, "
                  "bereikt de pool <strong>wanhoop</strong>: het gevoel dat het te laat is om het nog anders "
                  "te doen."),
        ]),
        dict(kop="Wat je met een voorbeeld moet doen", blokken=[
            ("p", "De vakfiche vraagt bij een voorbeeld om <strong>de fase en de pool te benoemen</strong>. "
                  "Dat zijn drie vragen achter elkaar: welke fase speelt hier, welke pool wordt bereikt, en "
                  "is het conflict opgelost? Antwoord je alleen met een naam, dan heb je maar een derde van "
                  "de vraag beantwoord."),
        ]),
    ])


# ───────────────────────── 7. Persoonlijkheid, karakter en temperament
zet("persoonlijkheid-karakter-en-temperament",
    titel="Persoonlijkheid, karakter en temperament",
    onder="Waaruit een persoonlijkheid bestaat, welke soorten identiteit er zijn, de vijf trekken van het big five model en de vier temperamenten van Galenus.",
    secties=[
        dict(kop="Wat persoonlijkheid is", blokken=[
            ("p", "<strong>Persoonlijkheid</strong> is <strong>het geheel dat je uniek maakt</strong>: een "
                  "vast patroon in denken, voelen en doen, dat over tijd en plaats heen blijft."),
            ("p", "Volgens de vakfiche bestaat ze uit drie elementen: <strong>identiteit, karakter en "
                  "temperament</strong>. Identiteit is wie je bent, karakter hoe je doet, temperament je "
                  "grondtoon."),
            ("p", "Drie factoren beïnvloeden haar, en het zijn dezelfde drie als bij de ontwikkeling: "
                  "<strong>nature</strong>, nurture en zelfbepaling. Over die zelfbepaling klopt het "
                  "volgende: <strong>je maakt zelf keuzes</strong>, <strong>je kiest binnen je "
                  "mogelijkheden</strong> en <strong>ze staat naast nature en nurture</strong>. Het is dus "
                  "één factor van drie, geen vrije keuze over alles."),
            ("kader", "<strong>De persoonlijkheid ligt niet volledig vast bij de geboorte.</strong> Nature "
                      "geeft een aanleg, maar nurture en zelfbepaling doen er evenveel toe. Een "
                      "<strong>tweeling die apart opgevoed wordt en toch dezelfde hobby krijgt</strong>, "
                      "wijst wel <strong>het gewicht van nature</strong> aan: een verschillende omgeving en "
                      "toch hetzelfde resultaat."),
            ("p", "<strong>Persoonlijkheid en gedrag zijn niet hetzelfde.</strong> Gedrag is wat je op één "
                  "moment doet; persoonlijkheid is het patroon erachter. Dat persoonlijkheid "
                  "<strong>stabiel</strong> is, betekent dat <strong>ze grotendeels gelijk blijft</strong> — "
                  "grotendeels, niet volledig, want grote gebeurtenissen kunnen iemand duidelijk veranderen."),
            ("p", "De persoonlijkheid van een peuter is nog moeilijk te beschrijven omdat <strong>ze nog "
                  "volop in ontwikkeling is</strong>. Het temperament is al zichtbaar, maar karakter en "
                  "identiteit groeien nog jaren door."),
        ]),
        dict(kop="Persoonlijke en sociale identiteit", blokken=[
            ("p", "De identiteit valt in twee grote delen uiteen. Het verschil tussen beide: <strong>de een "
                  "onderscheidt, de ander verbindt</strong>. Persoonlijk is wat jou anders maakt, sociaal is "
                  "waar je bij hoort — en allebei horen ze bij één identiteit."),
            ("p", "<strong>De sociale identiteit gaat over de groepen waartoe je behoort</strong>: je "
                  "familie, je land, je vriendenkring. Ze valt uiteen in drie categorieën, en met de "
                  "persoonlijke identiteit erbij noemt de fiche er vier."),
            ("kader", tabel(["categorie", "waarover ze gaat", "voorbeeld"],
                            [["<strong>persoonlijke identiteit</strong>", "wat jou van anderen onderscheidt",
                              "je eigen smaak, je eigen manier van doen"],
                             ["<strong>culturele identiteit</strong>", "taal, streek, gewoontes, tradities en geloof",
                              "iemand noemt zichzelf <strong>een West-Vlaming</strong> of zegt dat hij <strong>moslim</strong> is"],
                             ["<strong>relationele identiteit</strong>", "je plaats tegenover anderen",
                              "iemand noemt zichzelf <strong>de oudste van drie</strong>; ook dochter, vriend, collega, buur"],
                             ["<strong>genderidentiteit</strong>", "het gevoel man, vrouw of iets anders te zijn",
                              "ze hoeft niet samen te vallen met het geslacht bij de geboorte"]])),
            ("p", "Over identiteit klopt het volgende: <strong>ze groeit in contact met anderen</strong>, "
                  "<strong>ze hangt samen met socialisatie</strong> en <strong>ze kan in de loop van een "
                  "leven verschuiven</strong>. Zonder anderen weet je niet wie je bent, en daarom valt "
                  "identiteit grotendeels onder nurture."),
            ("p", "<strong>Iemand kan meer dan één sociale identiteit tegelijk hebben</strong>: dochter, "
                  "student, Limburger en voetbalster tegelijk. Ze botsen soms, en dan ontstaat een "
                  "rollenconflict."),
            ("weetje", "De identiteit staat het sterkst op het spel in <strong>de adolescentie</strong>. "
                       "Erikson noemde die fase niet toevallig identiteit versus identiteitsverwarring."),
        ]),
        dict(kop="Karakter: het big five model", blokken=[
            ("p", "<strong>Karakter</strong> is <strong>de trekken die je gedrag kleuren</strong>, zoals "
                  "zorgvuldigheid of openheid. Het bekendste model telt er <strong>vijf</strong>: het "
                  "<strong>big five</strong> model. Intelligentie hoort er niet bij."),
            ("p", "<strong>Elke trek is een schaal met twee uitersten.</strong> Je bent niet extravert "
                  "<em>of</em> introvert, maar ergens tussen de twee, en dat geldt voor elke trek."),
            ("kader", tabel(["trek", "de tegenpool", "waaraan je ze herkent"],
                            [["<strong>extraversie</strong>", "<strong>introversie</strong>",
                              "iemand <strong>praat graag met vreemden en zoekt gezelschap</strong>; introvert is niet verlegen maar naar binnen gericht"],
                             ["<strong>vriendelijkheid</strong>", "<strong>afstandelijkheid</strong>",
                              "meegaand, hulpvaardig, geneigd tot vertrouwen"],
                             ["emotionele stabiliteit", "<strong>neuroticisme</strong>",
                              "iemand <strong>maakt zich snel zorgen en schrikt van kleine dingen</strong>; het zegt niets over of iemand aardig is"],
                             ["<strong>zorgvuldigheid</strong>", "onzorgvuldigheid",
                              "plannen, afwerken, op tijd komen"],
                             ["<strong>openheid</strong>", "<strong>geslotenheid</strong>",
                              "nieuwsgierig naar nieuwe ideeën en ervaringen"]])),
            ("p", "Let op de valstrik in een examenvraag: elke trek heeft <em>zijn eigen</em> tegenpool. "
                  "Extraversie en neuroticisme zijn twee verschillende trekken, geen uitersten van elkaar."),
            ("p", "Een persoonlijkheidstest geeft nooit een volledig beeld, want <strong>gedrag hangt ook "
                  "van de situatie af</strong>. Dezelfde persoon doet anders op het werk dan thuis; een trek "
                  "is een neiging, geen voorspelling."),
        ]),
        dict(kop="Temperament: de vier van Galenus", blokken=[
            ("p", "<strong>Temperament</strong> is <strong>de aangeboren grondtoon</strong>. Het is al bij "
                  "een baby zichtbaar: de een is rustig, de ander snel van streek. "
                  "<strong>Temperament is dus niet vooral aangeleerd</strong> maar vooral aangeboren, "
                  "terwijl karakter en identiteit wel in contact met de omgeving groeien."),
            ("p", "Daarin zit meteen het verschil tussen de twee: <strong>het ene is aangeboren, het andere "
                  "groeit</strong>. Temperament is de aanleg waarmee je begint, karakter wat ervan groeit in "
                  "je omgeving. Zo komt het ook dat <strong>twee kinderen uit hetzelfde gezin een heel "
                  "ander karakter hebben</strong>: <strong>aanleg en ervaring verschillen</strong>. Zelfs "
                  "binnen één gezin krijgt elk kind een andere plaats, andere vrienden en andere ervaringen."),
            ("p", "Galenus onderscheidt <strong>vier</strong> temperamenten."),
            ("kader", tabel(["temperament", "waaraan je het herkent"],
                            [["<strong>cholerisch</strong>", "<strong>fel, gedreven en snel kwaad</strong>: veel energie en een kort lontje"],
                             ["<strong>flegmatisch</strong>", "<strong>rustig en moeilijk uit zijn lood te slaan</strong>: traag op gang maar kalm en volhardend — het rustigste van de vier"],
                             ["<strong>melancholisch</strong>", "<strong>ernstig, gevoelig en veel nadenkend</strong>: zorgvuldig en diep, maar snel neerslachtig"],
                             ["<strong>sanguinisch</strong>", "<strong>vrolijk, spontaan en snel enthousiast</strong>: levendig en optimistisch, maar soms vlug afgeleid"]])),
            ("kader", "<strong>De vier temperamenten van Galenus zijn niet wetenschappelijk bewezen.</strong> "
                      "Het is een oud model uit de geneeskunde van de lichaamssappen. Het big five model is "
                      "wél onderbouwd. Je moet de vier kennen, maar niet geloven."),
        ]),
    ])


# ───────────────────────── 8. Het zelfconcept: zelfbeeld en zelfwaardering
zet("het-zelfconcept-zelfbeeld-en-zelfwaardering",
    titel="Het zelfconcept: zelfbeeld en zelfwaardering",
    onder="De vier delen van het zelfconcept, de vier soorten zelfbeeld, en hoe elk deel het gedrag stuurt.",
    secties=[
        dict(kop="Vier delen van één beeld", blokken=[
            ("p", "Het <strong>zelfconcept</strong> is het hele beeld dat je van jezelf hebt. Het bestaat "
                  "uit vier delen: <strong>het zelfbeeld</strong>, <strong>de zelfwaardering</strong>, "
                  "<strong>de self-efficacy</strong> en het <strong>body-image</strong>. Temperament hoort "
                  "daar níét bij; dat valt onder de persoonlijkheid."),
            ("kader", tabel(["deel", "wat het doet", "een vraag die erbij past"],
                            [["<strong>zelfbeeld</strong>", "<strong>beschrijft</strong> wat je denkt dat je bent",
                              "wie ben ik?"],
                             ["<strong>zelfwaardering</strong>", "<strong>beoordeelt</strong>: <strong>hoeveel je jezelf waard vindt</strong>",
                              "ben ik iets waard?"],
                             ["<strong>self-efficacy</strong>", "het <strong>geloof dat je een taak aankan</strong>: taakgebonden, dus per taak verschillend",
                              "kan ik dit?"],
                             ["<strong>body-image</strong>", "<strong>hoe je over je lichaam denkt</strong> en voelt",
                              "hoe zie ik eruit, in mijn eigen ogen?"]])),
            ("p", "Het <strong>zelfbeeld</strong> is dus <strong>wat je denkt dat je bent</strong>: ik ben "
                  "verlegen, ik ben goed in tekenen. Of je dat goed vindt, is al zelfwaardering. "
                  "<strong>Zelfwaardering en self-efficacy betekenen niet hetzelfde</strong>: zelfwaardering "
                  "gaat over je waarde als persoon, self-efficacy over of je een bepaalde taak aankan."),
            ("p", "<strong>Het zelfconcept ligt niet van jongs af vast.</strong> Het groeit in contact met "
                  "anderen en kan veranderen, al gaat dat traag. Waar het zelfbeeld van een kind vooral "
                  "vandaan komt? <strong>Uit reacties van anderen.</strong> Een kind leest in de ogen van "
                  "anderen wie het is, en daarom wegen opmerkingen van ouders en leerkrachten zo zwaar."),
        ]),
        dict(kop="Vier soorten zelfbeeld", blokken=[
            ("p", "De fiche noemt vier soorten zelfbeeld: <strong>positief</strong>, "
                  "<strong>negatief</strong>, <strong>vertekend</strong> en <strong>realistisch</strong>. "
                  "Een <em>geleend</em> zelfbeeld bestaat niet; dat is een verzonnen antwoord."),
            ("kader", tabel(["soort", "wat het is", "voorbeeld"],
                            [["<strong>positief zelfbeeld</strong>", "je denkt gunstig over jezelf",
                              "ik kan veel, ik hoor erbij"],
                             ["<strong>negatief zelfbeeld</strong>", "je denkt ongunstig over jezelf",
                              "een leerling die bij een moeilijke oefening <strong>snel opgeeft</strong>"],
                             ["<strong>vertekend zelfbeeld</strong>", "het beeld klopt niet met de werkelijkheid",
                              "iemand <strong>kan goed rekenen maar zegt dat hij er niets van kan</strong>, of denkt dat hij alles kan en bereidt zich niet voor"],
                             ["<strong>realistisch zelfbeeld</strong>", "het beeld klopt met de werkelijkheid",
                              "iemand <strong>weet waar hij goed in is en waar niet</strong>"]])),
            ("p", "<strong>Een vertekend zelfbeeld kan zowel onderschatting als overschatting zijn.</strong> "
                  "Beide kanten wijken af van de werkelijkheid, en allebei geven ze problemen: onderschatting "
                  "houdt je tegen, <strong>overschatting</strong> leidt tot te weinig voorbereiding en dus "
                  "tot ontgoocheling."),
            ("kader", "<strong>Een positief zelfbeeld is niet hetzelfde als een realistisch zelfbeeld.</strong> "
                      "Positief kan ook té positief zijn. Realistisch betekent dat het beeld "
                      "<em>klopt</em>, niet dat het gunstig is. Die twee door elkaar halen is de meest "
                      "gemaakte fout bij dit onderwerp."),
            ("p", "Over het zelfbeeld klopt verder: <strong>het beschrijft wie je denkt te zijn</strong>, "
                  "<strong>het stuurt je gedrag</strong> en <strong>het groeit in contact met anderen</strong>. "
                  "Dat het altijd met de werkelijkheid zou kloppen, klopt juist níét — het bestaan van een "
                  "vertekend zelfbeeld bewijst dat."),
            ("p", "Het zelfbeeld verandert het sterkst in <strong>de adolescentie</strong>: de jongere "
                  "vergelijkt zich volop met anderen en zoekt wie hij is, dus schommelt het beeld dan het "
                  "meest. <strong>Het zelfbeeld van een kleuter is vaak te positief</strong>: een kleuter "
                  "denkt dat hij alles kan, en pas in de lagere school gaat hij zich met anderen "
                  "vergelijken."),
        ]),
        dict(kop="Zelfwaardering en self-efficacy", blokken=[
            ("p", "Over <strong>zelfwaardering</strong> klopt: <strong>ze beoordeelt jezelf</strong>, "
                  "<strong>ze stuurt wat je durft</strong> en <strong>ze kan schommelen</strong>. Ze is "
                  "algemener dan de self-efficacy, die juist per taak verschilt. Een <strong>lage "
                  "zelfwaardering</strong> leidt tot <strong>minder durven proberen</strong>: wie zichzelf "
                  "weinig waard vindt, stelt zich minder bloot aan de kans om te falen. Een <strong>man van "
                  "60 die zichzelf waardevol vindt ondanks een mislukt project</strong>, laat een "
                  "<strong>stevige zelfwaardering</strong> zien: zijn waarde als persoon hangt niet aan één "
                  "resultaat."),
            ("p", "<strong>Self-efficacy</strong> is een begrip van Bandura. Erover klopt: <strong>het is "
                  "geloof dat je iets kan</strong>, <strong>het verschilt per taak</strong> en <strong>het "
                  "groeit door te slagen</strong>. <strong>Ze kan hoog zijn voor het ene vak en laag voor "
                  "het andere</strong>: iemand kan vol vertrouwen zijn in taal en bang voor wiskunde, hoog "
                  "voor koken en laag voor spreken in het openbaar."),
            ("p", "Drie bronnen voeden de self-efficacy, in die volgorde van gewicht: <strong>eerder zelf "
                  "geslaagd zijn</strong>, <strong>iemand anders zien slagen</strong> en "
                  "<strong>aanmoediging krijgen</strong>. Een <strong>leerling die een moeilijke oefening "
                  "aandurft omdat het vorige keer lukte</strong>, laat een <strong>hoge "
                  "self-efficacy</strong> zien."),
            ("kader", "Daaruit volgt meteen wat een leerkracht kan doen: <strong>kleine haalbare stappen "
                      "geven</strong>. Elke gelukte stap is een ervaring van slagen, en die voedt het "
                      "vertrouwen het sterkst. Om dezelfde reden prijs je een kind beter om zijn "
                      "<strong>inzet</strong> dan om zijn talent: <strong>inzet kan het zelf sturen</strong>, "
                      "en dus leert het dat het iets kan veranderen."),
            ("p", "<strong>Een hoge self-efficacy helpt om door te zetten bij tegenslag.</strong> Wie "
                  "gelooft dat het kan lukken, probeert langer door — dat is het grote nut ervan."),
        ]),
        dict(kop="Body-image", blokken=[
            ("p", "Het <strong>body-image</strong> is <strong>hoe je over je lichaam denkt</strong>. Het is "
                  "een beeld in je hoofd, en <strong>het klopt niet altijd met hoe je lichaam er werkelijk "
                  "uitziet</strong>. Het kan sterk vertekend zijn, en dat speelt onder meer bij "
                  "eetstoornissen: een <strong>jongere die nauwelijks eet omdat ze zichzelf te zwaar vindt "
                  "terwijl ze mager is</strong>, heeft een <strong>vertekend body-image</strong>."),
            ("p", "In de adolescentie staat het body-image onder druk omdat <strong>het lichaam snel "
                  "verandert</strong>, en daar komt het vergelijken met leeftijdsgenoten en met beelden "
                  "online nog bij. Zo beïnvloeden sociale media het zelfconcept: <strong>jongeren "
                  "vergelijken zich met beelden</strong>, en bewerkte beelden worden dan de maatstaf voor "
                  "het eigen lichaam."),
            ("p", "Ook hier zie je het gedrag mee veranderen: een <strong>jongere die zich niet meer laat "
                  "zien in de turnles</strong>, laat <strong>het body-image</strong> aan het werk zien. "
                  "Vaak hangt er ook zelfwaardering aan vast."),
        ]),
        dict(kop="Waarom de fiche telkens naar het gedrag vraagt", blokken=[
            ("p", "Bij elk deel van het zelfconcept vraagt de fiche naar de invloed op het gedrag, en de "
                  "reden is steeds dezelfde: <strong>het stuurt wat je doet</strong>. Het blijft niet in je "
                  "hoofd — wat je van jezelf denkt, bepaalt wat je probeert, wat je uit de weg gaat en wat "
                  "je volhoudt. Daarom hoort het zelfconcept bij persoonlijkheid en gedrag."),
        ]),
    ])


# ───────────────────────── 9. Emoties: componenten en functies
zet("emoties-componenten-en-functies",
    titel="Emoties: componenten en functies",
    onder="Wat een emotie is, uit welke drie componenten ze bestaat, welke drie functies ze heeft en hoe ze het gedrag en het denken stuurt.",
    secties=[
        dict(kop="Wat een emotie is", blokken=[
            ("p", "Een <strong>emotie</strong> is <strong>een kortdurende reactie</strong>. Ze komt op door "
                  "iets en gaat weer weg."),
            ("p", "Daarin zit het verschil met een stemming: <strong>een emotie duurt korter</strong>. Een "
                  "emotie komt en gaat, een stemming hangt over een dag heen en heeft vaak geen duidelijke "
                  "aanleiding. Of ze positief of negatief is, doet aan dat onderscheid niets."),
            ("p", "Over emoties klopt het volgende: <strong>ze komen op door iets</strong>, <strong>ze gaan "
                  "vanzelf weer weg</strong> en <strong>ze hebben drie componenten</strong>. Dat je elke "
                  "emotie zomaar kan sturen, klopt niet."),
            ("kader", "<strong>Niet alle emoties zijn onaangenaam</strong>, en er bestaan ook geen "
                      "<strong>goede en slechte emoties</strong>. Vreugde, verbazing en opluchting zijn "
                      "evengoed emoties. Ze zijn aangenaam of onaangenaam, niet goed of slecht — en ze "
                      "hebben allemaal een functie."),
            ("p", "De emoties die men vaak de <strong>basisemoties</strong> noemt, zijn "
                  "<strong>blijdschap</strong>, <strong>angst</strong>, <strong>woede</strong>, verdriet, "
                  "walging en verbazing. Trots staat daar niet bij: die is samengesteld en komt later."),
            ("p", "<strong>Een baby toont al emoties voor hij kan spreken</strong>: hij huilt, lacht en "
                  "schrikt. Benoemen is een stap verder dan voelen, en die komt pas met de taal. "
                  "<strong>Schaamte hoort niet bij de eerste emoties van een baby</strong>, want <strong>ze "
                  "vraagt een besef van jezelf</strong>: schaamte, trots en schuld komen pas als een kind "
                  "zichzelf kan zien door de ogen van een ander."),
            ("p", "<strong>Emoties kunnen cultuurgebonden zijn</strong>, en dat slaat op <strong>het tonen "
                  "ervan</strong>. De basisemoties zijn overal hetzelfde; hoe openlijk je ze toont, "
                  "verschilt sterk per cultuur."),
        ]),
        dict(kop="Drie componenten", blokken=[
            ("p", "De vakfiche onderscheidt drie componenten in elke emotie: <strong>de "
                  "fysiologische</strong>, <strong>de gedragscomponent</strong> en <strong>de "
                  "mentale</strong>. Een morele component staat er niet bij."),
            ("kader", tabel(["component", "waarover ze gaat", "bij het zien van een hond"],
                            [["<strong>de fysiologische</strong>", "<strong>wat je lichaam doet</strong>: een snellere hartslag, zweten, een rood hoofd",
                              "<strong>je hart klopt sneller</strong>"],
                             ["<strong>de gedragscomponent</strong>", "<strong>wat je zichtbaar doet</strong>: fronsen, weglopen, stil worden",
                              "<strong>je deinst achteruit</strong>"],
                             ["<strong>de mentale</strong>", "de gedachte of de beleving: hoe je de situatie inschat",
                              "<strong>je denkt dat hij je gaat bijten</strong>"]])),
            ("p", "<strong>De drie componenten treden meestal samen op.</strong> Je schrikt, je springt "
                  "achteruit en je denkt <em>gevaar</em>: alle drie tegelijk, en juist daarom is het één "
                  "emotie."),
            ("p", "Soms botsen ze wel. <strong>Iemand die lacht maar zich verdrietig voelt</strong>, laat "
                  "<strong>gedrag en mentaal</strong> uit elkaar lopen. Dat kan, maar het kost moeite om vol "
                  "te houden."),
            ("p", "<strong>De fysiologische component is niet bewust te sturen.</strong> Je hartslag gaat "
                  "vanzelf omhoog. Je kan wel je ademhaling sturen en zo het lichaam kalmeren — langs een "
                  "omweg dus."),
            ("weetje", "<strong>Angst en opwinding lijken lichamelijk op elkaar</strong> omdat <strong>het "
                       "lichaam bijna gelijk reageert</strong>: een snellere hartslag en meer spanning in "
                       "beide gevallen. <strong>De mentale component maakt het verschil</strong> — wat je "
                       "dénkt dat er aan de hand is."),
            ("p", "De fiche vraagt om de componenten in een voorbeeld te herkennen, en de reden is "
                  "praktisch: <strong>zo zie je hoe een emotie werkt</strong>. Door het lichaam, het gedrag "
                  "en de gedachte apart te benoemen, wordt een vage emotie hanteerbaar."),
        ]),
        dict(kop="Drie functies", blokken=[
            ("p", "<strong>Emoties hebben een nuttige functie.</strong> Ze zijn geen storing maar een "
                  "systeem. De fiche noemt er drie: <strong>aanpassen</strong>, "
                  "<strong>communiceren</strong> en <strong>waarschuwen</strong>."),
            ("kader", tabel(["functie", "wat ze doet", "voorbeeld"],
                            [["<strong>waarschuwen</strong>", "gevaar signaleren, sneller dan je kan nadenken",
                              "<strong>je schrikt van een auto en springt opzij</strong>"],
                             ["<strong>communiceren</strong>", "iets laten weten aan anderen",
                              "<strong>een baby huilt en zijn moeder komt</strong>"],
                             ["<strong>aanpassen</strong>", "je gedrag afstemmen op de situatie",
                              "<strong>iemand past zijn gedrag aan omdat hij merkt dat een collega boos is</strong>"]])),
            ("p", "<strong>Angst heeft vooral de functie waarschuwen</strong>: ze waarschuwt voor gevaar en "
                  "maakt het lichaam klaar om te vluchten of te vechten. Dat <strong>iemand die geen angst "
                  "voelt meer gevaar loopt</strong>, toont precies <strong>de waarschuwende functie</strong>: "
                  "zonder dat alarm merk je gevaar te laat."),
            ("p", "Huilen is het eerste communicatiemiddel van een baby en werkt lang voor de taal er is. "
                  "Ook later blijft dat zo: <strong>je gezicht verraadt vaak een emotie voor je iets "
                  "zegt</strong>, in een fractie van een seconde."),
            ("p", "Over de functie <strong>aanpassen</strong> klopt: <strong>een emotie stuurt je "
                  "gedrag</strong>, <strong>ze helpt reageren op een situatie</strong> en <strong>ze werkt "
                  "sneller dan nadenken</strong>. Ze geldt het hele leven: een volwassene reageert even goed "
                  "op een emotie als een kind."),
        ]),
        dict(kop="Wat emoties met het gedrag en het denken doen", blokken=[
            ("p", "Emoties hebben drie reële invloeden op het gedrag: <strong>ze sturen wat je doet</strong>, "
                  "<strong>ze versnellen een beslissing</strong> en <strong>ze kleuren wat je onthoudt</strong>. "
                  "Op je lengte hebben ze geen vat — let op dat soort afleiders in een vraag."),
            ("p", "<strong>Mensen beslissen onder sterke emoties vaak anders</strong>, want <strong>het "
                  "denken wordt gekleurd</strong>: boos of bang weeg je risico's anders af. Daarom raadt men "
                  "aan een beslissing te laten bezinken. Een <strong>leerling die slechter leert omdat hij "
                  "bang is voor de toets</strong>, laat <strong>de invloed op het denken</strong> zien: "
                  "sterke angst neemt ruimte in het werkgeheugen in, en daarom helpt een rustige "
                  "toetsomgeving echt."),
            ("p", "<strong>Een emotie onderdrukken is niet hetzelfde als ze reguleren.</strong> Onderdrukken "
                  "duwt ze weg en kost moeite; reguleren is ze erkennen en er iets mee doen. Wat helpt om "
                  "een sterke emotie te sturen, is <strong>ze eerst benoemen</strong>. Benoemen maakt een "
                  "emotie hanteerbaar — dat is ook waarom het kleuters zo helpt als je hun gevoel voor hen "
                  "benoemt."),
            ("kader", "Een <strong>kind dat leert dat het mag roepen maar niet slaan</strong>, leert "
                      "<strong>emoties sturen</strong>. Het gevoel mag er zijn, het gedrag heeft grenzen. "
                      "Dat is de kern van emotieregulatie, in één zin."),
            ("p", "De emotionele ontwikkeling hoort bij de socio-emotionele ontwikkeling omdat "
                  "<strong>emoties het contact sturen</strong>. Hoe je omgaat met je eigen gevoel en met dat "
                  "van een ander, bepaalt dat contact. Daarom is het ook nuttig om <strong>de emoties van "
                  "anderen te kunnen lezen</strong>: <strong>je kan je gedrag erop afstemmen</strong>. "
                  "Gedachten raden lukt er niet mee."),
        ]),
    ])


# ───────────────────────── 10. Motivatie en attributies
zet("motivatie-en-attributies",
    titel="Motivatie en attributies",
    onder="Intrinsieke en extrinsieke motivatie, vermijden en toenaderen, en hoe de verklaring die je voor een resultaat geeft je motivatie stuurt.",
    secties=[
        dict(kop="Motivatie van binnen en van buiten", blokken=[
            ("p", "<strong>Motivatie</strong> is <strong>wat je in beweging zet</strong>: de drijfveer achter "
                  "gedrag, de reden waarom je iets begint en volhoudt. Erover klopt: <strong>ze stuurt je "
                  "gedrag</strong>, <strong>ze kan van binnen komen</strong> en <strong>ze kan van buiten "
                  "komen</strong>. Ze verschilt sterk per persoon en per taak."),
            ("p", "De fiche noemt twee vormen: <strong>intrinsieke motivatie</strong> (<strong>motivatie van "
                  "binnenuit</strong>) en <strong>extrinsieke motivatie</strong>, van buitenaf. "
                  "<em>Erfelijke</em> motivatie bestaat niet als term."),
            ("kader", tabel(["vorm", "waar de drijfveer zit", "voorbeeld"],
                            [["<strong>intrinsieke</strong> motivatie", "van binnenuit: je doet het omdat je het zelf graag doet",
                              "een jongen <strong>oefent gitaar omdat hij het leuk vindt</strong>"],
                             ["<strong>extrinsieke</strong> motivatie", "van buitenaf: een cijfer, geld, een beloning, de goedkeuring van anderen",
                              "een meisje <strong>leert om een goed rapport te halen</strong>"]])),
            ("p", "<strong>Extrinsieke motivatie houdt niet langer stand dan intrinsieke</strong> — "
                  "omgekeerd zelfs: een beloning werkt zolang ze er is, maar wie iets graag doet, blijft ook "
                  "zonder beloning bezig."),
            ("p", "<strong>Toch is extrinsieke motivatie niet altijd slecht.</strong> Soms is ze nodig om te "
                  "starten met iets dat je niet graag doet. Intrinsiek is alleen duurzamer."),
            ("kader", "<strong>Een beloning kan de intrinsieke motivatie verzwakken.</strong> Wie betaald "
                      "wordt voor iets dat hij graag deed, gaat het soms minder graag doen. Dat heet het "
                      "<strong>ondermijningseffect</strong>."),
            ("p", "Hoe voedt een leerkracht de intrinsieke motivatie? Door <strong>keuze en zin te "
                  "geven</strong>: wie iets mag kiezen en snapt waarom het nuttig is, doet het liever uit "
                  "zichzelf. <strong>Straf werkt op lange termijn minder goed dan een beloning</strong> "
                  "omdat <strong>ze enkel leert wat niet mag</strong>. Straf stopt gedrag maar zegt niet "
                  "welk gedrag wél goed is, en daarom voedt ze vooral vermijding."),
        ]),
        dict(kop="Vermijden en toenaderen", blokken=[
            ("p", "Motivatie wijst twee richtingen uit: je gaat op iets af, of je gaat er juist vandaan. De "
                  "fiche noemt <strong>vermijdingsgedrag</strong> en <strong>toenaderingsgedrag</strong>, en "
                  "elk van die twee valt nog eens uiteen."),
            ("kader", tabel(["soort", "wat je doet", "voorbeeld"],
                            [["<strong>passief vermijden</strong>", "niets doen",
                              "een leerling <strong>stelt zijn taak uit en doet intussen niets</strong>"],
                             ["actief vermijden", "<strong>iets anders doen om de taak te ontlopen</strong>",
                              "plots de kamer opruimen vlak voor een examen"],
                             ["toenaderen: <strong>nastreven</strong>", "op een doel afgaan dat je nog niet hebt",
                              "iemand <strong>solliciteert voor een job die hij nog niet heeft</strong>"],
                             ["toenaderen: <strong>behouden</strong>", "houden wat je wel hebt",
                              "iemand <strong>traint om zijn plaats in de ploeg te houden</strong>"]])),
            ("p", "<strong>Vermijdingsgedrag</strong> is dus gedrag waarmee je iets uit de weg gaat, en "
                  "<strong>toenaderingsgedrag</strong> heeft de twee vormen <strong>nastreven en "
                  "behouden</strong>: nastreven wat je niet hebt, of behouden wat je wel hebt. Beide zijn "
                  "toenadering."),
            ("weetje", "Een <strong>leerling die niets aan zijn taak doet omdat hij bang is te falen</strong>, "
                       "vertoont <strong>vermijdingsgedrag</strong>. Door niets te doen kan hij de "
                       "mislukking niet aan zichzelf toeschrijven — en dat is precies waarom vermijden zo "
                       "aantrekkelijk is."),
        ]),
        dict(kop="Wat een attributie is", blokken=[
            ("p", "Een <strong>attributie</strong> is <strong>de verklaring die je geeft</strong>: hoe je "
                  "verklaart waarom iets lukte of mislukte. Erover klopt: <strong>ze verklaren slagen of "
                  "falen</strong>, <strong>ze sturen de motivatie</strong> en <strong>ze kunnen intern of "
                  "extern zijn</strong>. Een attributie is een verklaring, geen feit: ze kan er ver naast "
                  "zitten."),
            ("p", "<strong>Attributies staan niet los van de motivatie.</strong> Ze staan juist bij "
                  "motivatie in de fiche, en met reden: hoe je een mislukking verklaart, bepaalt of je "
                  "opnieuw probeert."),
            ("p", "De fiche onderscheidt ze op twee assen: <strong>interne attributie</strong> of "
                  "<strong>externe attributie</strong>, en daarnaast <strong>controleerbaar of niet</strong>."),
            ("kader", tabel(["as", "de twee kanten"],
                            [["waar de oorzaak ligt",
                              "<strong>intern</strong> (bij jezelf: ik had te weinig geoefend) of <strong>extern</strong> (<strong>buiten jezelf</strong>: de toets was te moeilijk, de leerkracht was streng, ik had pech)"],
                             ["of je ze kan sturen",
                              "<strong>controleerbaar</strong> (<strong>hoeveel je oefent</strong>, <strong>hoe je je voorbereidt</strong>, <strong>hoeveel tijd je uittrekt</strong>) of oncontroleerbaar (talent, geluk)"]])),
        ]),
        dict(kop="Welke attributie helpt, en welke niet", blokken=[
            ("p", "De beste combinatie voor de motivatie is <strong>intern en controleerbaar</strong>: wat "
                  "bij jou ligt én wat je kan sturen, kan je volgende keer anders doen. Een <strong>leerling "
                  "die zegt dat hij slaagde omdat hij hard studeerde</strong>, zit precies daar."),
            ("kader", tabel(["wat iemand zegt", "welke attributie", "wat ze doet met de motivatie"],
                            [["ik slaagde <strong>omdat ik hard studeerde</strong>", "<strong>intern en controleerbaar</strong>",
                              "de beste: volgende keer kan je het weer zo doen"],
                             ["ik faalde <strong>omdat de toets oneerlijk was</strong>", "<strong>extern</strong>",
                              "af en toe klopt dat ook, maar altijd extern verklaren blokkeert het leren"],
                             ["ik slaagde <strong>omdat de toets makkelijk was</strong>", "<strong>extern</strong>",
                              "zijn vertrouwen groeit niet, want het lag niet aan hem"],
                             ["ik <strong>ben dom</strong>, daarom faalde ik", "intern maar oncontroleerbaar",
                              "<strong>ze laat geen verbetering toe</strong>: als het aan je aard ligt, heeft proberen geen zin"],
                             ["<strong>ik heb er geen aanleg voor</strong>", "<strong>intern en oncontroleerbaar</strong>",
                              "aanleg ligt bij jou maar kan je niet sturen; oefening wel"]])),
            ("p", "<strong>Altijd extern verklaren helpt niet om bij te leren.</strong> Wie alles buiten "
                  "zichzelf legt, hoeft nooit iets te veranderen, en dan blijft het resultaat gelijk. Een "
                  "<strong>leerling die zijn succes aan geluk toeschrijft</strong>, ziet zijn self-efficacy "
                  "<strong>niet groeien</strong>: wie zijn succes niet aan zichzelf toeschrijft, leert er "
                  "niets uit over wat hij kan."),
            ("p", "<strong>Dezelfde gebeurtenis kan door twee mensen heel anders verklaard worden.</strong> "
                  "Twee leerlingen met hetzelfde cijfer: de een zegt pech, de ander te weinig geoefend. Dat "
                  "is het hele punt van de theorie."),
            ("p", "Hoe helpt een leerkracht iemand met een ongunstige attributie? Door <strong>te wijzen op "
                  "wat hij wel stuurt</strong>. De aandacht verleggen naar inzet en aanpak maakt verbetering "
                  "weer mogelijk."),
            ("p", "Attributies hangen samen met het zelfconcept omdat <strong>ze je zelfbeeld voeden</strong>. "
                  "Wie keer op keer zegt dat hij er geen aanleg voor heeft, bouwt dat in zijn zelfbeeld in."),
            ("p", "Bij een voorbeeld vraagt de fiche twee dingen: <strong>de attributie en haar "
                  "invloed</strong> — welke attributie het is, én wat ze doet met de motivatie van die "
                  "persoon. Alleen de naam geven is een half antwoord."),
        ]),
    ])


# ───────────────────────── 11. Cultuur en cultuuruitingen
zet("cultuur-en-cultuuruitingen",
    titel="Cultuur en cultuuruitingen",
    onder="Wat cultuur is in de sociale wetenschappen, de zeven cultuuruitingen, en hoe je met dat raster twee culturen naast elkaar zet.",
    secties=[
        dict(kop="Wat cultuur is", blokken=[
            ("p", "<strong>Cultuur</strong> is in de sociale wetenschappen <strong>alles wat een groep deelt "
                  "en doorgeeft</strong>. Dat is veel breder dan kunst: ook gewoontes, kennis, rituelen, "
                  "symbolen, taal en waarden en normen horen erbij."),
            ("p", "Over cultuur klopt: <strong>ze wordt aangeleerd</strong>, <strong>ze wordt "
                  "doorgegeven</strong> en <strong>ze verandert in de tijd</strong>. Dat culturen allemaal op "
                  "elkaar lijken, klopt juist niet: ze verschillen sterk."),
            ("p", "<strong>Cultuur is niet aangeboren.</strong> Je leert ze, door socialisatie, en juist "
                  "daarom kan ze veranderen en doorgegeven worden. Dat is ook waarom cultuur in de fiche "
                  "<em>onder</em> socialisatie staat: <strong>cultuur wordt zo doorgegeven</strong>. "
                  "Socialisatie is het doorgeven van waarden, normen en andere cultuuruitingen, en zonder "
                  "cultuur valt er niets door te geven."),
            ("p", "Dat cultuur <strong>een gedeeld geheel</strong> is, betekent dat <strong>een groep ze "
                  "samen deelt</strong>. Juist het delen maakt het cultuur; wat één persoon alleen doet, is "
                  "een gewoonte van die persoon."),
            ("p", "Een cultuur verandert in de loop van de tijd omdat <strong>mensen dingen overnemen</strong>. "
                  "Contact met andere groepen, nieuwe techniek en nieuwe ideeën doen een cultuur schuiven. "
                  "<strong>Culturen blijven dus niet onaangeroerd als mensen met elkaar in contact "
                  "komen</strong>: eten, muziek en woorden reizen mee, en een groep die gewoontes overneemt, "
                  "doet aan acculturatie."),
        ]),
        dict(kop="De zeven cultuuruitingen", blokken=[
            ("p", "De vakfiche noemt <strong>zeven</strong> cultuuruitingen. Samen beschrijven ze wat een "
                  "cultuur is."),
            ("kader", tabel(["uiting", "wat ertoe hoort", "voorbeeld"],
                            [["gebruiken en gewoontes", "hoe het hier hoort te gaan",
                              "<strong>op tijd komen</strong>; wat hier te laat heet, is elders op tijd"],
                             ["<strong>kennis</strong>", "<strong>wat een groep weet en doorgeeft</strong>, ook praktische kennis",
                              "hoe je iets kweekt, bouwt of bereidt"],
                             ["kunstuitingen", "het werk waarin een groep zich uitdrukt",
                              "<strong>muziek</strong>, <strong>schilderkunst</strong>, <strong>dans</strong>"],
                             ["<strong>rituelen</strong>", "een handeling met een vaste vorm en een betekenis erachter",
                              "<strong>een trouwfeest met een vast verloop</strong>, <strong>een begrafenis met een vaste volgorde</strong>"],
                             ["<strong>symbolen</strong>", "iets dat voor iets anders staat",
                              "<strong>een vlag</strong>, een logo, kledij van een groep"],
                             ["<strong>taal</strong>", "ze draagt de hele cultuur mee",
                              "wie de taal leert, leert ook de gewoontes en de waarden erachter"],
                             ["<strong>waarden en normen</strong>", "de kern: ze sturen het gedrag van iedereen in de groep",
                              "eerlijkheid, en de regel dat je niet liegt"]])),
            ("p", "Het verschil tussen een waarde en een norm: <strong>een waarde is een ideaal</strong>, "
                  "iets wat je belangrijk vindt, bijvoorbeeld eerlijkheid. De <strong>norm</strong> is de "
                  "regel die eruit volgt: je liegt niet. Uit de waarde respect volgt de norm dat je iemand "
                  "laat uitspreken."),
            ("p", "<strong>Rituelen</strong> markeren vaak de overgangen in een leven: geboorte, huwelijk, "
                  "dood. Een <strong>symbool</strong> staat voor iets anders — een land, een club of een "
                  "idee — en de betekenis spreekt enkel binnen die cultuur vanzelf."),
            ("kader", "<strong>Een gebaar betekent niet in elke cultuur hetzelfde.</strong> Een duim omhoog "
                      "betekent niet overal goedkeuring. Lees een gebaar dus altijd in zijn context."),
        ]),
        dict(kop="Culturen naast elkaar", blokken=[
            ("p", "De fiche noemt drie manieren om culturen te vergelijken: <strong>westers en "
                  "niet-westers</strong>, <strong>dominant en subcultuur</strong>, en de "
                  "<strong>jongerenculturen</strong>. Rijk en arm staat er niet bij."),
            ("p", "Vergelijken doe je <strong>met de cultuuruitingen</strong>: de zeven uitingen vormen het "
                  "raster — taal, rituelen, symbolen, waarden en normen, en zo verder. Dat is nuttig omdat "
                  "<strong>je dan punt per punt vergelijkt</strong>: zonder raster blijft een vergelijking "
                  "bij een indruk."),
            ("p", "<strong>Twee landen die allebei nieuwjaar vieren maar op een andere dag</strong>, laten "
                  "<strong>hetzelfde ritueel met een andere invulling</strong> zien. De functie is gelijk, de "
                  "vorm verschilt — precies wat zo'n vergelijking moet opleveren."),
            ("p", "<strong>Westers tegenover niet-westers is een grove indeling</strong>, want <strong>binnen "
                  "elke groep verschilt veel</strong>: Japan en Marokko zijn allebei niet-westers en lijken "
                  "amper op elkaar. Zo'n indeling is enkel een eerste houvast. Aan westerse culturen "
                  "schrijft men vaak de <strong>nadruk op het individu</strong>, op "
                  "<strong>zelfstandigheid</strong> en op <strong>prestatie</strong> toe; de nadruk op de "
                  "grootfamilie hoort eerder bij culturen waar de groep voorgaat."),
            ("kader", "<strong>Etnocentrisme</strong> is <strong>een cultuur beoordelen vanuit je "
                      "eigen</strong> cultuur: je eigen gewoontes als de normale nemen. Het staat tegenover "
                      "<strong>cultuurrelativisme</strong>, waarbij je een gewoonte in haar eigen context "
                      "bekijkt."),
            ("p", "Een <strong>cultuurschok</strong> is <strong>verwarring in een vreemde cultuur</strong>: "
                  "wat vanzelf sprak, klopt plots niet meer. Veel mensen maken dat mee bij een verhuis naar "
                  "een ander land."),
        ]),
        dict(kop="Dominante cultuur, subcultuur en jongerencultuur", blokken=[
            ("p", "Een <strong>dominante cultuur</strong> is <strong>de cultuur van de meerderheid</strong>. "
                  "Zij bepaalt de gangbare waarden en normen in een samenleving."),
            ("p", "Een <strong>subcultuur</strong> is <strong>een groep met eigen gewoontes</strong>: ze "
                  "deelt veel met de dominante cultuur maar heeft eigen symbolen, taal of gewoontes. Een "
                  "<strong>groep skaters met eigen kledij, taal en plekken</strong> is er een."),
            ("p", "Over subculturen klopt: <strong>ze hebben eigen symbolen</strong>, <strong>ze bestaan "
                  "binnen een grotere cultuur</strong> en <strong>je kan er zelf bij gaan horen</strong>. "
                  "Een eigen wet hebben ze niet: ze vallen onder dezelfde wetten als iedereen."),
            ("kader", "<strong>Een subcultuur staat niet altijd tegenover de dominante cultuur.</strong> Ze "
                      "kan er rustig naast bestaan zonder verzet. Alleen een <strong>tegencultuur</strong> "
                      "zet zich uitdrukkelijk af. En <strong>iemand kan tegelijk bij de dominante cultuur en "
                      "bij een subcultuur horen</strong> — dat is zelfs de regel: je deelt de taal en de "
                      "wetten, en daarnaast de gewoontes van je eigen groep."),
            ("p", "Een <strong>jongerencultuur</strong> is de cultuur van jongeren met eigen muziek en "
                  "kledij. Ze is vaak tijdelijk en verandert snel, en <strong>sneller dan de dominante "
                  "cultuur</strong>, omdat <strong>ze om onderscheid draait</strong>: zodra iedereen iets "
                  "overneemt, verliest het zijn onderscheidende kracht en zoekt de groep iets nieuws. Een "
                  "<strong>jongere die kledij draagt die zijn ouders lelijk vinden</strong>, "
                  "<strong>toont bij welke groep hij hoort</strong> — kledij is een symbool, en het verschil "
                  "met de ouders is net wat het bruikbaar maakt."),
        ]),
    ])


# ───────────────────────── 12. Socialisatie, enculturatie en acculturatie
zet("socialisatie-enculturatie-en-acculturatie",
    titel="Socialisatie, enculturatie en acculturatie",
    onder="Hoe cultuur wordt doorgegeven, via welke drie niveaus dat loopt, en welke drie vormen van socialisatie de fiche onderscheidt.",
    secties=[
        dict(kop="Wat socialisatie is", blokken=[
            ("p", "<strong>Socialisatie</strong> is <strong>cultuur leren en doorgeven</strong>. Wat er "
                  "doorgegeven wordt, zijn <strong>waarden</strong>, <strong>normen</strong> en "
                  "<strong>andere cultuuruitingen</strong>. Erfelijke aanleg hoort daar niet bij: die krijg "
                  "je mee bij de geboorte en wordt niet aangeleerd."),
            ("p", "Daarom staan cultuur en socialisatie in de fiche samen: <strong>socialisatie geeft "
                  "cultuur door</strong>. Cultuur is wát doorgegeven wordt, socialisatie is hóe dat "
                  "gebeurt."),
            ("p", "Over socialisatie klopt: <strong>ze duurt een leven lang</strong>, <strong>ze gaat via "
                  "meer dan één groep</strong> en <strong>ze geeft cultuur door</strong>. Ze is juist het "
                  "tegengestelde van erfelijk. <strong>Socialisatie stopt dus niet na de kindertijd</strong>: "
                  "een nieuwe job, een nieuw land of een nieuwe rol vraagt telkens nieuwe normen. "
                  "<strong>Iemand die naar een ander land verhuist en daar leert hoe het eraan toegaat</strong>, "
                  "beleeft <strong>socialisatie op latere leeftijd</strong> — en bovendien acculturatie."),
            ("p", "Een <strong>kind dat thuis leert dat je dankjewel zegt</strong>, maakt socialisatie mee "
                  "in haar eenvoudigste vorm: een norm wordt doorgegeven in het gezin."),
            ("kader", "<strong>Socialisatie en opvoeding zijn niet hetzelfde: socialisatie is "
                      "breder.</strong> Opvoeding is bewust en gericht; socialisatie gebeurt ook ongemerkt, "
                      "via vrienden, media en de buurt. En <strong>socialisatie is "
                      "tweerichtingsverkeer</strong>: <strong>ook jongeren geven iets door</strong>. "
                      "Kinderen leren hun ouders bijvoorbeeld werken met nieuwe toestellen."),
            ("p", "<strong>Een kind neemt niet alles over wat het via socialisatie meekrijgt.</strong> Het "
                  "kiest en weegt, zeker in de adolescentie. Daarom verandert een cultuur ook. En "
                  "<strong>socialisatie verschilt per gezin</strong>, want <strong>elk gezin heeft eigen "
                  "waarden</strong>: binnen dezelfde cultuur legt het ene gezin de nadruk op "
                  "zelfstandigheid, het andere op samen zijn."),
        ]),
        dict(kop="Wat socialisatie oplevert", blokken=[
            ("p", "Voor het individu levert socialisatie <strong>aanpassing aan de omgeving</strong> op: je "
                  "leert wat kan en wat niet, zodat je in je omgeving kan functioneren. De fiche noemt drie "
                  "gevolgen voor het individu: <strong>aanpassing aan de omgeving</strong>, "
                  "<strong>prosociaal gedrag</strong> en <strong>antisociaal gedrag</strong> — de aanpassing "
                  "zelf, met een gunstige en een ongunstige kant."),
            ("kader", tabel(["gedrag", "wat het is", "hoe het ontstaat"],
                            [["<strong>prosociaal gedrag</strong>", "<strong>gedrag dat anderen helpt</strong>: delen, helpen, troosten",
                              "een gevolg van <strong>geslaagde socialisatie</strong>: je weet wat de groep verwacht"],
                             ["<strong>antisociaal gedrag</strong>", "gedrag dat ingaat tegen de normen van een groep en anderen schaadt",
                              "het ligt dichterbij als de socialisatie mislukt"]])),
            ("p", "Voor de samenleving is het belang even groot: <strong>socialisatie zorgt ervoor dat een "
                  "cultuur blijft bestaan</strong>. Zonder doorgeven sterft een cultuur met haar dragers, en "
                  "<strong>anders verdwijnen de afspraken</strong>: een samenleving leeft van gedeelde "
                  "waarden en normen, en elke generatie moet ze opnieuw leren."),
        ]),
        dict(kop="Drie niveaus", blokken=[
            ("p", "De fiche onderscheidt <strong>drie</strong> niveaus van socialisatie: "
                  "<strong>primair</strong>, <strong>secundair</strong> en <strong>tertiair</strong>. Een "
                  "<em>finale</em> socialisatie bestaat niet als term."),
            ("kader", tabel(["niveau", "waar het speelt", "kenmerk"],
                            [["<strong>de primaire socialisatie</strong>", "in het gezin",
                              "de eerste en <strong>de diepste</strong>: ze legt de basis in de vroege kindertijd"],
                             ["<strong>de secundaire socialisatie</strong>", "op <strong>school</strong>, bij vrienden, op het werk",
                              "ze komt <strong>na het gezin</strong>; secundair betekent hier tweede in de tijd, niet tweederangs"],
                             ["<strong>de tertiaire socialisatie</strong>", "via <strong>de media</strong> en andere kanalen",
                              "<strong>ze vraagt geen rechtstreeks contact</strong> met mensen; daarin verschilt ze van de eerste twee"]])),
            ("p", "<strong>De primaire socialisatie is de diepste</strong>: wat je in je eerste jaren leert, "
                  "voelt later als vanzelfsprekend, en daarom weegt ze het zwaarst."),
            ("p", "<strong>De drie niveaus kunnen tegelijk werken.</strong> Een tiener krijgt thuis, op "
                  "school en via zijn gsm tegelijk boodschappen, en die spreken elkaar soms tegen. Precies "
                  "dat kan tot spanning leiden: <strong>de niveaus spreken elkaar tegen</strong>, en de "
                  "jongere moet daar zelf een weg in vinden."),
            ("weetje", "<strong>De rol van instituties verschuift</strong> doorheen de tijd. De kerk had "
                       "vroeger veel meer invloed, de media veel minder, en school duurt nu langer. Daarom "
                       "verschilt de socialisatie van een tiener nu van die van zijn grootouders: "
                       "<strong>de instituties zijn verschoven</strong>. De fiche noemt dat verandering in "
                       "tijd en ruimte, en vraagt je die verschuiving uit te leggen."),
        ]),
        dict(kop="Drie vormen", blokken=[
            ("p", "Naast de niveaus noemt de fiche drie <em>vormen</em> van socialisatie: "
                  "<strong>enculturatie</strong>, <strong>acculturatie</strong> en <strong>anticiperende "
                  "socialisatie</strong>. <em>Collectivisatie</em> hoort niet in deze lijst thuis."),
            ("kader", tabel(["vorm", "wat ze is", "voorbeeld"],
                            [["<strong>enculturatie</strong>", "opgroeien in je eigen cultuur, zonder dat je het merkt",
                              "een kind dat vanzelf de taal, de feesten en de gewoontes van thuis overneemt"],
                             ["<strong>acculturatie</strong>", "<strong>gewoontes overnemen</strong> van een andere cultuur",
                              "<strong>een gezin uit Marokko dat in België Sinterklaas mee viert</strong>"],
                             ["<strong>anticiperende socialisatie</strong>", "de normen van een rol overnemen voor je die rol hebt",
                              "<strong>een student die alles leest over een job die hij later wil doen</strong>, of <strong>een kind dat zijn oudere broer nadoet die naar het middelbaar gaat</strong>"]])),
            ("p", "<strong>Enculturatie en acculturatie betekenen niet hetzelfde.</strong> Enculturatie is "
                  "je eigen cultuur binnenkrijgen, acculturatie is een andere cultuur overnemen. En "
                  "acculturatie betekent niet dat de eigen cultuur verdwijnt: er komt iets bij."),
            ("p", "Over <strong>anticiperende socialisatie</strong> klopt: <strong>ze gaat over een "
                  "toekomstige rol</strong>, <strong>ze gebeurt voor de rol begint</strong> en <strong>ze "
                  "maakt de overgang makkelijker</strong>. Ze loopt net zo goed via vrienden, stages of "
                  "media; het gezin is er niet voor nodig."),
        ]),
    ])


# ───────────────────────── 13. Sociale instituties
zet("sociale-instituties",
    titel="Sociale instituties",
    onder="De negen instituties die waarden en normen doorgeven, op welk niveau van socialisatie elk ervan werkt, en hoe hun rol verschuift in tijd en ruimte.",
    secties=[
        dict(kop="Wat een sociale institutie is", blokken=[
            ("p", "Een <strong>sociale institutie</strong> is <strong>een vaste groep met een taak</strong>: "
                  "een duurzaam verband dat een rol speelt in de samenleving. Het gezin, de school en de "
                  "kerk zijn er alle drie een."),
            ("p", "Over instituties klopt: <strong>ze geven waarden en normen door</strong>, <strong>hun rol "
                  "verschuift in de tijd</strong> en <strong>ze werken op verschillende niveaus</strong>. "
                  "Hun invloed verschilt sterk: het gezin raakt diep, de media breed."),
            ("p", "De fiche noemt er <strong>negen</strong>, en vraagt bij elk het niveau van socialisatie "
                  "te bepalen. Waarom? <strong>Elke institutie werkt anders door.</strong> Het gezin raakt "
                  "je het diepst, de media het breedst, en het niveau zegt iets over die werking."),
            ("kader", tabel(["institutie", "niveau", "wat ze doorgeeft"],
                            [["<strong>het gezin</strong>", "<strong>primair</strong>", "<strong>de eerste waarden</strong> en normen"],
                             ["de <strong>familie</strong>", "primair en secundair", "gewoontes en kennis uit de ruimere kring"],
                             ["<strong>de school</strong>", "<strong>secundair</strong>", "kennis, én <strong>regels en samenwerken</strong>"],
                             ["<strong>de peergroep</strong>", "secundair", "normen over kledij, muziek en taal"],
                             ["<strong>de verenigingen</strong>", "secundair", "samenwerken, leiding nemen, inzet"],
                             ["<strong>de buurt</strong>", "secundair", "voorbeelden van wat normaal is"],
                             ["<strong>de massamedia</strong>", "<strong>tertiair</strong>", "beelden van hoe je hoort te zijn"],
                             ["<strong>het rechtssysteem</strong>", "tertiair", "de regels van een samenleving, met gezag"],
                             ["<strong>de religieuze instituties</strong>", "primair tot tertiair", "waarden, rituelen, een levensbeschouwing"]])),
            ("p", "<strong>Een institutie kan op meer dan één niveau werken.</strong> Een vereniging geeft "
                  "normen door in rechtstreeks contact én via haar kanalen online."),
        ]),
        dict(kop="Gezin, familie, school", blokken=[
            ("p", "Het <strong>gezin</strong> staat voor de <strong>primaire</strong> socialisatie: het is "
                  "de eerste groep waarin een kind komt. De invloed is groot omdat <strong>het eerst komt en "
                  "lang duurt</strong>: wat je in je eerste jaren leert, voelt later vanzelfsprekend, en "
                  "daarom gaat het diep. Over het gezin klopt verder: <strong>het staat voor de primaire "
                  "socialisatie</strong>, <strong>het geeft de eerste waarden door</strong> en <strong>zijn "
                  "vorm verandert in de tijd</strong> — alleenstaande ouders, nieuw samengestelde gezinnen, "
                  "en per cultuur weer anders."),
            ("p", "<strong>Gezin en familie zijn twee aparte instituties.</strong> Het gezin is wie "
                  "samenwoont; de <strong>familie</strong> is de ruimere kring: grootouders, tantes, neven "
                  "en nichten. Ze is breder dan het gezin omdat <strong>ze meer generaties omvat</strong>, en "
                  "in sommige culturen voeden die mee op. Een <strong>kind dat van zijn grootmoeder een "
                  "recept leert</strong>, krijgt dus iets mee van <strong>de familie</strong>."),
            ("p", "Op <strong>school</strong> leert een kind naast de leerstof vooral <strong>regels en "
                  "samenwerken</strong>: op tijd komen, je beurt afwachten, met anderen werken. Dat heet de "
                  "<strong>verborgen leerstof</strong>. <strong>Een school geeft dus niet enkel kennis "
                  "door</strong>: ze geeft ook normen mee over inzet, eerlijkheid en samenwerken, vaak "
                  "zonder dat er een les over gaat."),
            ("p", "Ook de rol van de school verandert: <strong>ze duurt langer en doet meer</strong>. "
                  "Kinderen zitten langer op school, en de school neemt ook taken over rond gezondheid en "
                  "welzijn."),
        ]),
        dict(kop="Peergroep, vereniging en buurt", blokken=[
            ("p", "Een <strong>peergroep</strong> is <strong>de groep leeftijdsgenoten</strong>: mensen van "
                  "ongeveer dezelfde leeftijd en met een vergelijkbare plaats. <strong>Ze weegt het zwaarst "
                  "in de adolescentie</strong>, niet in de babytijd — een baby heeft nog geen "
                  "leeftijdsgenoten om zich aan te spiegelen. Een <strong>jongere die van kledij verandert "
                  "om bij zijn vrienden te horen</strong>, laat de peergroep aan het werk zien."),
            ("p", "<strong>De invloed van de peergroep kan botsen met die van het gezin.</strong> Thuis geldt "
                  "iets anders dan in de vriendengroep, en die spanning hoort bij de adolescentie."),
            ("p", "<strong>Verenigingen</strong> zijn een eigen institutie: sportclub, jeugdbeweging, "
                  "muziekschool. Een <strong>kind dat in de jeugdbeweging leert samenwerken en leiding "
                  "nemen</strong>, krijgt dat van de vereniging mee."),
            ("p", "<strong>Een buurt heeft wél invloed op de socialisatie</strong> — ze staat uitdrukkelijk "
                  "in de lijst. Waar je opgroeit, bepaalt wie je tegenkomt en wat normaal lijkt. Voor een "
                  "jong kind is dat belangrijk omdat <strong>het er speelt en voorbeelden ziet</strong>."),
        ]),
        dict(kop="Media, recht en religie", blokken=[
            ("p", "De <strong>massamedia</strong> werken op het <strong>tertiaire</strong> niveau: ze "
                  "bereiken je <strong>zonder rechtstreeks contact</strong> met een persoon. Daarbij horen "
                  "<strong>de televisie</strong>, <strong>de krant</strong>, de radio, het internet en "
                  "<strong>de sociale media</strong>. De buurman hoort er niet bij: dat is rechtstreeks "
                  "contact, en dus secundair. Een <strong>jongere die online leest dat iets normaal is en "
                  "het overneemt</strong>, beleeft <strong>het tertiaire</strong> niveau."),
            ("p", "De invloed van sociale media weegt bij jongeren zwaar omdat <strong>ze er de hele dag mee "
                  "bezig zijn</strong>. Een kanaal dat de hele dag meeloopt, geeft veel beelden van hoe je "
                  "hoort te zijn."),
            ("p", "Het <strong>rechtssysteem</strong> geeft de regels van een samenleving door met gezag: "
                  "<strong>het maakt normen afdwingbaar</strong>. Een norm die iedereen moet volgen, wordt "
                  "een wet, en wie ze breekt, krijgt een sanctie. Het heet een institutie omdat <strong>het "
                  "duurzaam is en een taak heeft</strong> — dat is precies de definitie."),
            ("p", "<strong>De rol van religieuze instituties is in Vlaanderen kleiner geworden.</strong> De "
                  "kerk bepaalde vroeger het ritme van het jaar en de normen rond gezin en werk; dat is "
                  "sterk verschoven."),
        ]),
        dict(kop="Verandering in tijd en ruimte", blokken=[
            ("p", "Met <strong>verandering in tijd en ruimte</strong> bedoelt de fiche dat <strong>de rol "
                  "van een institutie verschilt per periode en per plaats</strong>. De kerk woog vroeger "
                  "zwaar en nu minder: dat is de tijd. En <strong>de familie weegt elders zwaarder</strong> "
                  "dan hier: dat is de ruimte."),
            ("kader", "<strong>De instituties geven niet altijd dezelfde boodschap door.</strong> Thuis, op "
                      "school en online gelden soms verschillende normen, en juist die botsing maakt "
                      "opgroeien lastig. Wat er dan gebeurt? <strong>De jongere moet zelf kiezen.</strong> "
                      "In die ruimte ontstaat zelfbepaling, en het is ook een van de redenen waarom een "
                      "cultuur verandert."),
        ]),
    ])


# ───────────────────────── 14. Sociale groepen en de typologie van Merton
zet("sociale-groepen-en-de-typologie-van-merton",
    titel="Sociale groepen en de typologie van Merton",
    onder="Primair tegenover secundair, formeel tegenover informeel, en de vier soorten die Merton onderscheidt.",
    secties=[
        dict(kop="Twee indelingen die je niet mag verwarren", blokken=[
            ("p", "Er zijn twee verschillende indelingen van groepen, en ze staan los van elkaar. Het "
                  "verschil tussen primair en formeel in één zin: <strong>het een gaat over de band</strong>. "
                  "Primair of secundair gaat over de band tussen de leden, formeel of informeel over de "
                  "regels."),
            ("kader", tabel(["indeling", "waar ze naar kijkt", "de twee kanten"],
                            [["primair of secundair", "de band tussen de leden",
                              "<strong>een kleine, hechte groep</strong> tegenover een grote, doelgerichte groep"],
                             ["formeel of informeel", "de regels en de rollen",
                              "<strong>een groep met vaste regels</strong> tegenover een groep die spontaan ontstaat"]])),
            ("p", "Daarom kan een groep <strong>tegelijk secundair en formeel</strong> zijn: een school is "
                  "allebei — groot en doelgericht, met vastgelegde regels en rollen. Een "
                  "<strong>vriendengroep die al jaren samen op reis gaat</strong> is dan weer "
                  "<strong>primair en informeel</strong>: hecht en persoonlijk, en zonder vastgelegde "
                  "regels."),
            ("p", "Over groepen in het algemeen klopt: <strong>een groep deelt iets</strong>, <strong>de "
                  "leden weten dat ze erbij horen</strong> en <strong>een groep kan formeel of informeel "
                  "zijn</strong>. Een leider is niet nodig: een vriendengroep draait zonder."),
            ("p", "Deze indelingen horen bij de sociale wetenschappen omdat <strong>ze ordenen hoe mensen "
                  "samenleven</strong>. Met zo'n indeling kan je een groep beschrijven en vergelijken, in "
                  "plaats van er een indruk van te geven."),
        ]),
        dict(kop="Primaire en secundaire groepen", blokken=[
            ("p", "Een <strong>primaire groep</strong> is <strong>een kleine, hechte groep</strong>: weinig "
                  "leden, persoonlijk contact en een sterke band. <strong>Het gezin</strong> is het "
                  "voorbeeld bij uitstek. <strong>Een primaire groep heeft dus niet veel leden</strong> — ze "
                  "is net klein, zodat persoonlijk contact met iedereen mogelijk blijft."),
            ("p", "Primair zijn bijvoorbeeld <strong>het gezin</strong>, <strong>een hechte "
                  "vriendenkring</strong> en <strong>een klein team dat jaren samenwerkt</strong>. De "
                  "klanten van een winkel niet: die kennen elkaar niet."),
            ("p", "Een <strong>secundaire groep</strong> is groot, heeft een doel en weinig persoonlijk "
                  "contact: een school, <strong>een bedrijf met tweehonderd werknemers</strong>, een "
                  "vakbond. Wat het contact daar kenmerkt: <strong>het draait om de taak</strong>. In een "
                  "primaire groep is de band zelf het doel."),
            ("p", "Een primaire groep weegt zwaarder in de socialisatie omdat <strong>het contact "
                  "persoonlijk is</strong>: wat iemand zegt die je graag ziet, raakt dieper dan een "
                  "algemene regel."),
            ("kader", "<strong>Binnen een secundaire groep kunnen primaire groepen ontstaan.</strong> "
                      "Collega's die vrienden worden, vormen een primaire groep binnen het bedrijf. En een "
                      "<strong>klas die een eigen groepsgevoel krijgt</strong>, is het omgekeerde geval: "
                      "<strong>een formele groep wordt ook primair</strong> — formeel samengesteld, maar het "
                      "contact maakt er ook een hechte groep van."),
        ]),
        dict(kop="Formele en informele groepen", blokken=[
            ("p", "Een <strong>formele groep</strong> is <strong>een groep met vaste regels</strong>: "
                  "afspraken, rollen en soms statuten liggen vast. Formeel zijn bijvoorbeeld <strong>een "
                  "sportclub met statuten</strong>, <strong>een school</strong> en <strong>een "
                  "vakbond</strong>."),
            ("p", "Een <strong>informele groep</strong> ontstaat spontaan, zonder vaste regels: een "
                  "vriendengroep, de mensen die samen pauze nemen, <strong>een groep buren die samen een "
                  "feest organiseert zonder statuten</strong>."),
            ("p", "<strong>In een informele groep liggen de rollen niet vooraf vast</strong> — daar groeien "
                  "ze vanzelf. In een formele groep liggen ze wél vast: voorzitter, secretaris, leerkracht, "
                  "leerling."),
        ]),
        dict(kop="De typologie van Merton", blokken=[
            ("p", "Merton onderscheidt <strong>vier</strong> soorten, en hij doet dat aan de hand van twee "
                  "vragen: <strong>is er persoonlijk contact, en is er een gedeeld gevoel?</strong> Is er "
                  "contact, is er een gedeeld gevoel, is er alleen een kenmerk, of is er niets dan de plaats."),
            ("kader", tabel(["soort", "contact", "gedeeld gevoel", "voorbeeld"],
                            [["<strong>de primaire groep</strong>", "ja", "ja", "het gezin, een hechte vriendenkring"],
                             ["<strong>de collectiviteit</strong>", "nee", "<strong>ja: gedeelde waarden</strong>",
                              "<strong>alle supporters van dezelfde ploeg</strong>, alle leden van een geloofsgemeenschap"],
                             ["<strong>de sociale categorie</strong>", "nee", "nee, alleen een kenmerk",
                              "<strong>alle mensen van zestien jaar in België</strong>, <strong>alle linkshandigen</strong>"],
                             ["<strong>het samenzijn</strong>", "nee", "nee, alleen de plaats",
                              "<strong>de mensen die samen in de lift staan</strong> of in een wachtzaal zitten"]])),
            ("p", "Van die vier hebben er <strong>drie geen persoonlijk contact</strong>: <strong>de "
                  "collectiviteit</strong>, <strong>de sociale categorie</strong> en <strong>het "
                  "samenzijn</strong>. Alleen de primaire groep heeft echt persoonlijk contact tussen de "
                  "leden, en zij heeft dan ook <strong>de sterkste band</strong>. De vier lopen af in "
                  "sterkte: primaire groep, collectiviteit, categorie, samenzijn."),
            ("p", "Let op dat die indeling iets anders is dan formeel en informeel: dat is een aparte "
                  "indeling, die hier niet in voorkomt."),
        ]),
        dict(kop="Waar de grenzen schuiven", blokken=[
            ("p", "Wat een <strong>collectiviteit</strong> wel heeft en een <strong>sociale categorie</strong> "
                  "niet, zijn <strong>gedeelde waarden</strong>. Beide delen een kenmerk, maar alleen de "
                  "collectiviteit deelt waarden en een gevoel van samenhoren. <strong>Een sociale categorie "
                  "heeft dus geen gevoel van samenhoren</strong>, en zodra dat er wél komt, verschuift de "
                  "categorie: <strong>een gedeeld gevoel ontstaat</strong> en de categorie wordt een "
                  "collectiviteit."),
            ("p", "<strong>Een collectiviteit blijft daarbij niet klein.</strong> Ze kan miljoenen leden "
                  "tellen, zoals alle gelovigen van een godsdienst. Het gedeelde gevoel telt, niet het "
                  "aantal."),
            ("p", "Over de typologie klopt: <strong>ze telt vier soorten</strong>, <strong>ze kijkt naar "
                  "contact en gevoel</strong> en <strong>een soort kan in een andere overgaan</strong>. Het "
                  "aantal leden is niet wat telt."),
            ("p", "<strong>Een samenzijn bestaat alleen zolang mensen op één plek zijn.</strong> Alleen de "
                  "plaats en het moment verbinden hen; zodra ze weg zijn, is de groep weg."),
            ("kader", "Waarom dit nuttig is: <strong>je kan de invloed van een groep beter inschatten</strong>. "
                      "Een primaire groep stuurt je gedrag veel sterker dan een samenzijn, en de indeling "
                      "maakt dat zichtbaar."),
        ]),
    ])


# ───────────────────────── 15. Sociale positie, sociale rol en rollenconflicten
zet("sociale-positie-sociale-rol-en-rollenconflicten",
    titel="Sociale positie, sociale rol en rollenconflicten",
    onder="Positie, rol en status, het verschil tussen toegewezen en verworven, en hoe een interne van een externe rollenconflict verschilt.",
    secties=[
        dict(kop="Positie, rol en status", blokken=[
            ("p", "Drie begrippen horen volgens de fiche samen: <strong>positie</strong>, "
                  "<strong>rol</strong> en <strong>status</strong>. Bij elke positie hoort een rol en een "
                  "status. Cultuur is een ander begrip en hoort niet in dit rijtje."),
            ("kader", tabel(["begrip", "wat het is", "bij de positie leerling"],
                            [["<strong>sociale positie</strong>", "<strong>de plaats die je inneemt</strong>",
                              "leerling zijn; ook dochter, collega, buur"],
                             ["<strong>sociale rol</strong>", "<strong>het verwachte gedrag</strong> bij die positie",
                              "op tijd komen, taken maken, luisteren"],
                             ["<strong>sociale status</strong>", "<strong>het aanzien</strong> dat die positie krijgt in een samenleving",
                              "hoeveel aanzien de positie leerling geniet"]])),
            ("p", "<strong>Een sociale positie en een sociale rol betekenen dus niet hetzelfde.</strong> De "
                  "positie is de plaats, de rol is wat men je daarin ziet doen."),
            ("p", "<strong>Iedereen heeft meer dan één sociale positie.</strong> Je bent tegelijk dochter, "
                  "leerling, collega en vriendin, en samen vormen die posities je plaats in de samenleving. "
                  "Over sociale posities klopt dan ook: <strong>je hebt er meerdere tegelijk</strong>, "
                  "<strong>sommige zijn toegewezen</strong> en <strong>sommige zijn tijdelijk</strong>. Dat "
                  "elke positie dezelfde status zou hebben, klopt juist niet — dat is het hele punt van "
                  "sociale status."),
        ]),
        dict(kop="Toegewezen of verworven, tijdelijk of levenslang", blokken=[
            ("p", "Een <strong>toegewezen positie</strong> is <strong>een positie die je niet kiest</strong>: "
                  "je geslacht, je leeftijd, in welk gezin je geboren bent. Je verkrijgt ze <strong>door "
                  "geboorte of leeftijd</strong>, zonder eigen inspanning. <strong>Dochter zijn</strong>, "
                  "<strong>jongste van het gezin zijn</strong> en <strong>zestien jaar zijn</strong> zijn "
                  "alle drie toegewezen."),
            ("p", "Een <strong>verworven</strong> positie behaal je zelf: door een opleiding, een job of een "
                  "keuze. <strong>Iemand die na jaren studeren arts wordt</strong>, heeft een "
                  "<strong>verworven</strong> positie: ze is het resultaat van een eigen inspanning."),
            ("p", "Die indeling is nuttig omdat <strong>ze toont wat je kan sturen</strong>: wat toegewezen "
                  "is, ligt vast; wat verworven is, hangt af van kansen en inzet."),
            ("p", "Daarnaast noemt de fiche een tweede paar: <strong>een positie kan tijdelijk of "
                  "levenslang zijn</strong>. Leerling ben je tijdelijk, <strong>zoon zijn</strong> is "
                  "levenslang — familiebanden verdwijnen niet."),
            ("kader", "De twee paren werken door elkaar. Iemand die <strong>voorzitter van een club wordt "
                      "voor twee jaar</strong>, heeft een positie die <strong>verworven en tijdelijk</strong> "
                      "is: hij kreeg ze door verkiezing, en voor een bepaalde periode."),
        ]),
        dict(kop="Rolverwachtingen", blokken=[
            ("p", "<strong>Een rol wordt bepaald door wat anderen van je verwachten.</strong> Die "
                  "<strong>rolverwachtingen</strong> komen van de groep; je kan ze invullen op je eigen "
                  "manier, maar ze liggen er wel. Dat <strong>een leerkracht geacht wordt eerlijk te "
                  "verbeteren</strong>, is zo'n <strong>rolverwachting</strong>."),
            ("p", "Het verschil tussen een rol en een rolverwachting: <strong>de verwachting komt van "
                  "anderen</strong>. De verwachtingen van de groep vormen samen de rol; hoe je ze invult, "
                  "blijft deels aan jou. <strong>Een positie staat dus niet los van de "
                  "rolverwachtingen</strong>: bij elke positie horen juist wel verwachtingen van de mensen "
                  "rond je."),
            ("p", "<strong>Een rolverwachting van de ene groep kan anders zijn dan die van de andere.</strong> "
                  "Wat de directie van een leerkracht verwacht, verschilt van wat de leerlingen verwachten, "
                  "en daaruit ontstaat een conflict."),
            ("weetje", "<strong>De rol bij een positie verandert in de loop van de tijd</strong>, want "
                       "<strong>de verwachtingen verschuiven</strong>. Wat men van een vader verwachtte in "
                       "1960 verschilt sterk van nu: de positie bleef, de rol schoof op."),
        ]),
        dict(kop="De rollenset", blokken=[
            ("p", "Een <strong>rollenset</strong> is <strong>alle rollen bij één positie</strong>. Bij de "
                  "positie leerkracht horen rollen <strong>tegenover de leerlingen</strong>, "
                  "<strong>tegenover de ouders</strong>, tegenover de collega's en <strong>tegenover de "
                  "directie</strong>."),
            ("p", "Let op: de rollenset hoort bij <em>één</em> positie. Vader zijn is een andere positie, "
                  "met een eigen set. Botsen twee rollen binnen dezelfde set, dan heet dat een intern "
                  "rollenconflict."),
        ]),
        dict(kop="Intern en extern rollenconflict", blokken=[
            ("p", "De fiche noemt twee soorten rollenconflicten: <strong>interne</strong> (<strong>binnen "
                  "één positie</strong>) en <strong>externe</strong>, tussen twee posities. "
                  "<em>Tijdelijke</em> rollenconflicten bestaan niet als term."),
            ("kader", tabel(["soort", "wat botst", "voorbeelden"],
                            [["<strong>intern rollenconflict</strong>", "twee verwachtingen <strong>binnen één positie</strong>",
                              "een <strong>verpleegkundige die tijd wil nemen voor een patiënt maar ook snel moet werken</strong>; een leerkracht die streng moet zijn voor de directie en begripvol voor de leerling"],
                             ["<strong>extern rollenconflict</strong>", "twee verschillende posities",
                              "een <strong>moeder die moet werken en tegelijk haar ziek kind verzorgen</strong>; <strong>student en werknemer tegelijk</strong>; <strong>ouder en mantelzorger tegelijk</strong>; een <strong>trainer die zijn eigen zoon op de bank moet zetten</strong>"]])),
            ("p", "Let bij zo'n vraag altijd op het aantal posities. Een leerkracht met twee moeilijke "
                  "klassen blijft in dezelfde positie: dat is intern, niet extern. Een "
                  "<strong>student die in het weekend werkt en daardoor niet kan studeren</strong>, heeft "
                  "twee posities die tegelijk tijd vragen: dat is <strong>extern</strong>."),
            ("kader", "<strong>Een rollenconflict betekent niet dat iemand ruzie heeft met een ander.</strong> "
                      "Het gaat over botsende verwachtingen, en vaak speelt het conflict volledig in één "
                      "persoon. Erover klopt: <strong>ze ontstaan uit botsende verwachtingen</strong>, "
                      "<strong>ze kunnen intern of extern zijn</strong> en <strong>ze spelen vaak in één "
                      "persoon</strong>."),
            ("p", "Wat kan iemand eraan doen? <strong>Prioriteiten stellen</strong>: kiezen wat voorgaat, "
                  "afspraken maken, of een rol tijdelijk afbouwen. Het conflict verdwijnt zelden vanzelf."),
            ("p", "<strong>Rollenconflicten komen vaker voor dan vroeger</strong> omdat <strong>mensen meer "
                  "posities hebben</strong>: werken, studeren, zorgen en vrijwilligerswerk lopen vaker door "
                  "elkaar dan een paar generaties geleden."),
            ("p", "De fiche vraagt om in een voorbeeld het rollenconflict te benoemen, en met een reden: "
                  "<strong>zo zie je welke posities botsen</strong>. Door de posities te benoemen wordt een "
                  "vage spanning een helder conflict. Oplossen is een volgende stap."),
        ]),
    ])


# ───────────────────────── 16. Sociale status en kansen in de samenleving
zet("sociale-status-en-kansen-in-de-samenleving",
    titel="Sociale status en kansen in de samenleving",
    onder="De zes factoren die status bepalen, hoe een sociale positie doorwerkt in onderwijs, werk, wonen en gezondheid, en wat sociale mobiliteit is.",
    secties=[
        dict(kop="Wat sociale status is", blokken=[
            ("p", "<strong>Sociale status</strong> is <strong>het aanzien van een positie</strong>: hoeveel "
                  "waardering een samenleving aan een positie geeft. Bij elke positie hoort zo'n status."),
            ("p", "Het is een <em>sociaal</em> begrip en geen persoonlijk gevoel, want <strong>anderen "
                  "kennen ze toe</strong>. Status bestaat doordat een samenleving aanzien geeft; "
                  "zelfwaardering is iets anders."),
            ("kader", "<strong>Een hoge status in de ene groep geldt niet automatisch in elke groep.</strong> "
                      "Wie in zijn sportclub veel aanzien heeft, kan op het werk net beginnen. Status hangt "
                      "aan een positie <em>binnen een groep</em>."),
        ]),
        dict(kop="De zes factoren", blokken=[
            ("p", "De fiche noemt <strong>zes</strong> factoren die de sociale status bepalen."),
            ("kader", tabel(["factor", "waarover ze gaat", "toegewezen of verworven"],
                            [["<strong>afkomst</strong>", "<strong>het gezin waarin je opgroeit</strong>, de familie en de omgeving waarin je begint", "toegewezen"],
                             ["<strong>beroep</strong>", "<strong>het werk dat iemand doet</strong>", "<strong>verworven</strong>"],
                             ["<strong>geslacht</strong>", "in veel samenlevingen nog altijd een verschil in aanzien en kansen", "toegewezen"],
                             ["inkomen en vermogen", "wat er maandelijks binnenkomt, en wat er al staat", "<strong>verworven</strong>"],
                             ["<strong>kenniskring</strong>", "<strong>de mensen die je kent</strong>: je netwerk", "eerder verworven"],
                             ["<strong>opleiding</strong>", "hoe lang en hoe ver je kon studeren", "<strong>verworven</strong>"]])),
            ("p", "<strong>Een beroep draagt in onze samenleving status met zich mee</strong>: chirurg, "
                  "poetshulp en advocaat krijgen niet hetzelfde aanzien, al is elk werk nodig. En "
                  "<strong>geslacht staat als statusfactor op de fiche</strong> — het is er een van de zes."),
            ("p", "<strong>Inkomen en vermogen staan samen als één factor</strong> omdat <strong>ze beide "
                  "over geld gaan</strong>: inkomen is wat er maandelijks binnenkomt, vermogen is wat er al "
                  "staat, en samen bepalen ze de financiële ruimte. Toch zijn ze onderscheidbaar: "
                  "<strong>twee mensen die hetzelfde werk doen waarvan de ene meer verdient</strong>, "
                  "verschillen in <strong>het inkomen</strong>, niet in beroep."),
            ("p", "De <strong>kenniskring</strong> is je netwerk: wie je kan bellen voor een job, een advies "
                  "of een kans. Wie veel mensen kent, hoort vaker van een kans dan wie niemand kent."),
        ]),
        dict(kop="Hoe de factoren samenwerken", blokken=[
            ("p", "Over de statusfactoren klopt: <strong>ze werken samen</strong>, <strong>sommige liggen "
                  "vast</strong> en <strong>ze verschuiven in de tijd</strong>. Ze versterken elkaar juist, "
                  "en dat is belangrijk om te zien."),
            ("p", "<strong>Opleiding en inkomen versterken elkaar</strong> omdat <strong>een diploma beter "
                  "werk opent</strong>: wie langer kon studeren, komt vaker in beter betaald werk terecht, "
                  "en zo duwt de ene factor de andere mee. <strong>Iemand die een masterdiploma haalt</strong>, "
                  "ziet <strong>de opleiding</strong> stijgen, en vaak ook het beroep en het inkomen erna."),
            ("p", "<strong>Niet alle factoren wegen overal even zwaar.</strong> Het gewicht verschilt per "
                  "samenleving en per tijd: in sommige culturen weegt afkomst veel zwaarder dan opleiding. "
                  "Een <strong>familie die al generaties bekend staat in de streek</strong>, haalt haar "
                  "aanzien uit <strong>de afkomst</strong> — de familienaam, niet iets wat die persoon zelf "
                  "behaalde."),
            ("p", "De factor die in een leven <strong>het minst verandert, is de afkomst</strong>: waar je "
                  "geboren bent, blijft. Beroep, opleiding en inkomen kan iemand in de loop van een leven "
                  "nog bijstellen."),
        ]),
        dict(kop="Wat een positie met je kansen doet", blokken=[
            ("p", "Met <strong>de impact van een sociale positie</strong> bedoelt de fiche dat <strong>ze je "
                  "kansen beïnvloedt</strong>: je positie opent of sluit deuren. Ze werkt door op drie "
                  "terreinen — <strong>onderwijs</strong>, <strong>werk</strong> en <strong>wonen</strong> — "
                  "en <strong>ook in de gezondheid</strong> van mensen: wie minder verdient, woont vaker "
                  "slechter, werkt zwaarder en leeft gemiddeld korter."),
            ("p", "<strong>Twee kinderen met dezelfde talenten krijgen niet altijd dezelfde kansen.</strong> "
                  "Hun startpositie verschilt: de taal die thuis gesproken wordt, geld voor bijles, een "
                  "netwerk voor een stage. Talent alleen beslist niet. Daarom klopt: <strong>de "
                  "startpositie weegt mee</strong>, <strong>onderwijs kan ze bijsturen</strong> en "
                  "<strong>kansen zijn niet voor iedereen gelijk</strong>."),
            ("p", "Sociale wetenschappers kijken daarom naar kansen en niet enkel naar inzet, want "
                  "<strong>inzet verklaart niet alles</strong>: twee mensen met dezelfde inzet komen vanuit "
                  "een andere positie niet even ver, en dat verschil is het onderzoeksveld."),
            ("kader", "<strong>Toch bepaalt een positie niet volledig hoe een leven verloopt.</strong> Ze "
                      "beïnvloedt de kansen, ze beslist niet alles: eigen keuzes, toeval en beleid spelen "
                      "mee. Dat onderscheid moet je in een antwoord maken."),
            ("p", "Een <strong>leerling die een richting kiest omdat zijn ouders dat deden</strong>, laat "
                  "<strong>zijn sociale positie</strong> aan het werk zien: de verwachtingen van de omgeving "
                  "sturen de keuze mee. De <strong>kenniskring</strong> werkt op dezelfde manier bij het "
                  "vinden van werk: <strong>ze brengt vacatures aan</strong>, want veel jobs komen via "
                  "iemand die iemand kent."),
        ]),
        dict(kop="Sociale overerving en sociale mobiliteit", blokken=[
            ("p", "<strong>Sociale overerving</strong> (of reproductie) is het doorgeven van een positie van "
                  "ouder naar kind: de positie van de ouders werkt door in die van het kind. Dat "
                  "<strong>wie uit een gezin zonder diploma's komt, minder vaak hoger studeert</strong>, is "
                  "er het schoolvoorbeeld van."),
            ("p", "<strong>Sociale mobiliteit</strong> is <strong>van positie veranderen</strong>: opklimmen "
                  "of afzakken op de maatschappelijke ladder, binnen één leven of over generaties. Stijgen "
                  "heet opwaartse mobiliteit — <strong>de eerste in het gezin met een diploma</strong> is "
                  "daar een voorbeeld van — en zakken heet neerwaartse. <strong>Mobiliteit gaat dus niet "
                  "enkel naar boven</strong>: wie zijn werk verliest of ziek wordt, kan een positie "
                  "verliezen."),
            ("p", "<strong>Een samenleving waarin de positie van je ouders je toekomst bepaalt, heeft lage "
                  "mobiliteit.</strong> Hoe sterker de positie wordt doorgegeven, hoe minder iemand van "
                  "plaats kan veranderen."),
            ("kader", tabel(["maatregel", "wat ze doet met de mobiliteit"],
                            [["<strong>gratis onderwijs</strong>", "verhoogt ze: de drempel om te studeren valt weg"],
                             ["<strong>een studiebeurs</strong>", "verhoogt ze: geld is minder een reden om te stoppen"],
                             ["<strong>een goed openbaar vervoer</strong>", "verhoogt ze: ook een verre school komt binnen bereik"],
                             ["<strong>een brede toegang tot school</strong>", "verkleint de impact van een zwakke startpositie"]])),
            ("p", "Onderwijs heet daarom een <strong>hefboom</strong> voor kansen: <strong>het kan een start "
                  "goedmaken</strong>. Een diploma kan een moeilijke startpositie deels compenseren, en "
                  "juist daarom weegt gelijke onderwijskans zo zwaar."),
            ("p", "Waarom is het nuttig je eigen sociale positie te leren zien? <strong>Je begrijpt je "
                  "kansen beter.</strong> Wie ziet welke voordelen en drempels hij meekreeg, kan gerichter "
                  "kiezen — en dat is het doel van dit thema."),
        ]),
    ])

# -*- coding: utf-8 -*-
"""De leerbundels voor aardrijkskunde op ✨ Spark-niveau.

Gebaseerd op de vakfiche aardrijkskunde 1ste graad A-stroom. Eén bundel per
thema, niet per deel: deel 1 en deel 2 van hetzelfde thema behandelen dezelfde
leerstof, alleen met andere vragen. Kim uploadt de bundel dus twee keer, één
keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/aardrijkskunde.json`
doet daar het voorwerk voor.

Over de kaarten. De dertien reliëfeenheden van de fiche staan op geen enkele
vrij te gebruiken kaart: wat in omloop is, draagt de namen van de landstreken,
en dat zijn andere namen. Daarom staat hier een schéma van de drie trappen
(svg.relieftrappen) in plaats van een kaart. Een schema kan niet scheef staan,
want er komt geen enkele grens aan te pas.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Aardrijkskunde"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────────────────────── 1. Een kaart lezen
BUNDELS["een-kaart-lezen"] = dict(
    vak=VAK, niveau=SPARK, titel="Een kaart lezen",
    onder="Wat er op een kaart hoort te staan, hoe je je oriënteert, en hoe je met de schaal en de hoogtelijnen rekent.",
    secties=[
        dict(kop="Wat er op een kaart hoort te staan", blokken=[
            ("p", "Krijg je een kaart in handen en wil je eerst weten waarover ze gaat, dan kijk je naar de "
                  "<strong>titel</strong>. Die zegt welk gebied je ziet en waarover de kaart gaat."),
            ("p", "Een goede kaart heeft er nog drie dingen bij. De <strong>legende</strong> legt uit wat de "
                  "tekens en de kleuren betekenen. De <strong>schaal</strong> zegt hoeveel keer het gebied "
                  "verkleind is. De <strong>noordpijl</strong> is het pijltje dat aanwijst waar het noorden ligt."),
            ("kader", "Titel, legende, schaal en noordpijl. Ontbreekt er een van de vier, dan kan je de kaart "
                      "wel bekijken maar er niet goed mee werken: je weet dan niet wat een kleur betekent, "
                      "hoe ver iets is, of welke kant je uit moet."),
            ("p", "Een kaart is niet hetzelfde als een <strong>luchtfoto</strong>. Op een luchtfoto zie je het "
                  "gebied zoals het er echt uitziet. Op een kaart zie je tékens die iets voorstellen: een blauwe "
                  "lijn is een rivier, een rood lijntje een weg. Daarom heeft een luchtfoto ook geen legende: er "
                  "valt niets uit te leggen, je ziet het gewoon. Een <strong>satellietbeeld</strong> is zoals een "
                  "luchtfoto, maar van veel hoger genomen. Kaart, luchtfoto en satellietbeeld tonen alle drie een "
                  "gebied van bovenaf gezien."),
            ("p", "Een <strong>plan</strong> is een kaart van een klein gebied, met veel details: een schoolplan, "
                  "een stadsplan. Hoe kleiner het gebied, hoe meer er op past."),
            ("weetje", "Kaart, luchtfoto en satellietbeeld tonen alle drie hetzelfde gebied, maar met andere "
                       "ogen. Wat je van de ene niet kan aflezen, staat soms wel op de andere."),
        ]),
        dict(kop="Je oriënteren", blokken=[
            ("p", "Jezelf <strong>oriënteren</strong> is weten welke kant je uit kijkt. De vier "
                  "<strong>hoofdwindstreken</strong> zijn noord, oost, zuid en west. Daartussen liggen de vier "
                  "tussenrichtingen: noordoost, zuidoost, zuidwest en noordwest. Het zuidwesten ligt dus tussen "
                  "het zuiden en het westen in."),
            ("fig", svg.windroos(), "De letter O staat bij het oosten. Sta je met je gezicht naar het noorden, "
                                    "dan ligt het zuiden achter je, het oosten rechts en het westen links."),
            ("p", "Een <strong>kompas</strong> gebruik je om te weten welke kant het noorden op ligt. De naald "
                  "wijst altijd naar het noorden, en met die ene richting kan je alle andere afleiden."),
            ("kader", "Op de meeste kaarten ligt het noorden bovenaan, maar niet op élke kaart. Daarom staat er "
                      "een noordpijl op: die vertelt je hoe deze kaart georiënteerd is. Kijk er altijd naar "
                      "voordat je zegt wat waar ligt."),
        ]),
        dict(kop="De schaal, en rekenen met afstanden", blokken=[
            ("p", "De <strong>schaal</strong> zegt hoeveel keer het gebied verkleind is. Bij een "
                  "<strong>breukschaal</strong> zoals 1 : 25 000 betekent dat: één centimeter op de kaart is "
                  "25 000 centimeter in het echt."),
            ("p", "Centimeter is een onhandige eenheid voor afstanden buiten, dus reken je die om. "
                  "25 000 centimeter is 250 meter. Eén centimeter op een kaart 1 : 25 000 is dus "
                  "<strong>250 meter</strong>. En op een kaart 1 : 100 000 is één centimeter "
                  "100 000 centimeter, dus 1000 meter, dus <strong>1 kilometer</strong>."),
            ("fig", tabel(["schaal", "1 cm op de kaart is"], [
                ["1 : 10 000", "100 meter"],
                ["1 : 25 000", "250 meter"],
                ["1 : 50 000", "500 meter"],
                ["1 : 100 000", "1 kilometer"],
                ["1 : 250 000", "2,5 kilometer"],
            ]), "Streep achter de 1 : … twee nullen weg en je hebt meters. Schrap er vijf en je hebt kilometers."),
            ("p", "Reken maar mee. Je meet 3 centimeter op een kaart 1 : 50 000. Eén centimeter is daar "
                  "500 meter, dus 3 centimeter is 1500 meter, en dat is <strong>1,5 kilometer</strong>. En meet "
                  "je 4 centimeter op een kaart 1 : 25 000, dan is dat 4 × 250 = 1000 meter, dus "
                  "<strong>1 kilometer</strong>."),
            ("p", "Om een afstand op een kaart uit te rekenen heb je dus twee dingen nodig: een "
                  "<strong>meetlat</strong> om te meten, en de <strong>schaal</strong> om om te rekenen."),
            ("fig", svg.schaalbalk(), "Een <strong>lijnschaal</strong> is een balkje met de echte afstand erbij "
                                      "geschreven. Handig als je de kaart vergroot of verkleint kopieert: het "
                                      "balkje schaalt mee, een breuk niet. Maar rekenen kan met allebei."),
            ("p", "Een weg die bochten maakt is langer dan hij op het eerste gezicht lijkt. Meet zo'n weg met "
                  "een <strong>touwtje</strong>: je legt het touwtje over alle bochten en meet het daarna in "
                  "één rechte lijn. De afstand <strong>in vogelvlucht</strong>, dus recht door de lucht, is "
                  "altijd korter dan de afstand langs de weg."),
            ("kader", "Hoe kleiner het getal achter de dubbele punt, hoe minder de kaart verkleint en hoe meer "
                      "details je ziet. Op 1 : 10 000 zie je van een dorp veel meer dan op 1 : 100 000. En "
                      "1 : 100 000 en 1 : 250 000 verkleinen allebei sterker dan 1 : 50 000."),
        ]),
        dict(kop="Hoogtelijnen en reliëf", blokken=[
            ("p", "Een <strong>hoogtelijn</strong> is een lijn door alle punten die even hoog liggen. De hoogte "
                  "wordt geteld vanaf de <strong>zeespiegel</strong>: die is het nulpunt, overal ter wereld "
                  "hetzelfde."),
            ("fig", svg.hoogtelijnen(), "Liggen de hoogtelijnen dicht bij elkaar, dan is de helling daar steil. "
                                        "Liggen ze ver uit elkaar, dan loopt het er flauw op."),
            ("p", "Twee hoogtelijnen op dezelfde kaart kunnen elkaar <strong>nooit</strong> kruisen. Als ze dat "
                  "wel deden, zou één punt tegelijk twee verschillende hoogtes hebben, en dat kan niet."),
            ("p", "Van een kaart met hoogtelijnen kan je dus drie dingen aflezen: hoe hoog een plaats boven de "
                  "zeespiegel ligt, hoe steil een helling is, en het <strong>hoogteverschil</strong> tussen twee "
                  "punten. Dat laatste is gewoon het verschil tussen hun hoogtes: van de lijn van 100 meter naar "
                  "die van 160 meter stijg je 60 meter."),
            ("p", "Het hoogst gelegen punt van een gebied heet het <strong>hoogtepunt</strong> van dat gebied."),
            ("fig", svg.reliefvormen(), "De reliëfvormen die de vakfiche noemt. Een vlakte ligt laag én vlak, "
                                        "een plateau is een <strong>hooggelegen</strong> gebied dat bovenaan "
                                        "vlak is, niet sterk golvend. Een berg is veel hoger en meestal ook "
                                        "steiler dan een heuvel."),
            ("p", "Ver weg lijken de lucht en de aarde elkaar te raken. Die denkbeeldige lijn heet de "
                  "<strong>horizonlijn</strong>. Ze is geen echte lijn: ze verschuift mee als je zelf verschuift."),
        ]),
    ],
    onthoud=[
        "Op een goede kaart staan een titel, een legende, een schaal en een noordpijl.",
        "Een luchtfoto toont het gebied zoals het echt is en heeft geen legende; een kaart toont tekens.",
        "Een plan is een kaart van een klein gebied met veel details.",
        "Hoofdwindstreken: noord, oost, zuid, west. Daartussen noordoost, zuidoost, zuidwest, noordwest.",
        "1 : 25 000 betekent 1 cm op de kaart = 250 m in het echt; 1 : 100 000 = 1 km.",
        "Afstand meten: een meetlat plus de schaal. Bochtige wegen meet je met een touwtje.",
        "Een hoogtelijn verbindt punten die even hoog liggen, geteld vanaf de zeespiegel.",
        "Lijnen dicht bijeen = steil; lijnen ver uiteen = flauw. Hoogtelijnen kruisen elkaar nooit.",
        "Reliëfvormen: vlakte (laag en vlak), plateau (hoog en vlak), heuvel, berg.",
        "De horizonlijn is de lijn in de verte waar lucht en aarde elkaar lijken te raken.",
    ],
)

# ───────────────────────────────────────── 2. Waar op aarde ben je?
BUNDELS["waar-op-aarde-ben-je"] = dict(
    vak=VAK, niveau=SPARK, titel="Waar op aarde ben je?",
    onder="Het gradennet, de werelddelen en de oceanen, en het verschil tussen absoluut en relatief situeren.",
    secties=[
        dict(kop="Het gradennet", blokken=[
            ("p", "Wil je aan iemand aan de andere kant van de wereld uitleggen waar jij precies woont, dan werkt "
                  "een straatnaam niet: dezelfde straatnaam komt in veel gemeenten voor. Wat wél werkt, is "
                  "<strong>een paar getallen die overal ter wereld hetzelfde betekenen</strong>. Daarvoor is het "
                  "gradennet gemaakt."),
            ("fig", svg.gradennet(), "De <strong>evenaar</strong> verdeelt de aarde in een noordelijk en een "
                                     "zuidelijk <strong>halfrond</strong>. De <strong>meridianen</strong> lopen "
                                     "van pool tot pool. De <strong>nulmeridiaan</strong> loopt door Greenwich, "
                                     "bij Londen."),
            ("p", "Alle meridianen zijn <strong>even lang</strong>, want ze lopen allemaal van de noordpool naar "
                  "de zuidpool. De breedtecirkels niet: die worden korter naarmate je dichter bij een pool komt. "
                  "De evenaar is de langste van allemaal."),
            ("fig", tabel(["lijn", "waar ze ligt"], [
                ["<strong>de evenaar</strong>", "op 0° breedte"],
                ["<strong>de keerkringen</strong>", "op 23,5° noorder- en zuiderbreedte"],
                ["<strong>de poolcirkels</strong>", "op 66,5° noorder- en zuiderbreedte"],
                ["<strong>de nulmeridiaan</strong>", "op 0° lengte, door Greenwich"],
                ["<strong>de datumlijn</strong>", "ongeveer tegenover de nulmeridiaan; daar verspringt de datum"],
            ]), "De vijf lijnen waarvan je de ligging uit het hoofd moet kennen."),
            ("kader", "<strong>Breedte</strong> loopt van 0° aan de evenaar tot 90° aan een pool, en nooit "
                      "verder. <strong>Lengte</strong> loopt van 0° in Greenwich tot 180° aan elke kant. Een "
                      "breedte van 180 graden bestaat dus niet."),
            ("p", "Het punt helemaal bovenaan de aardas heet de <strong>noordpool</strong>, het punt onderaan de "
                  "zuidpool."),
        ]),
        dict(kop="Werelddelen en oceanen", blokken=[
            ("p", "De aarde telt zeven <strong>werelddelen</strong>: Europa, Azië, Afrika, Noord-Amerika, "
                  "Zuid-Amerika, Oceanië en Antarctica. Ja, ook Antarctica: het is een werelddeel, ook al woont "
                  "er niemand vast. België ligt in <strong>Europa</strong>."),
            ("p", "De grote wateroppervlakken heten <strong>oceanen</strong>: de Grote of Stille Oceaan, de "
                  "Atlantische Oceaan, de Indische Oceaan, en verder nog de Noordelijke en de Zuidelijke "
                  "IJszee. De <strong>Atlantische Oceaan</strong> ligt tussen Europa en Amerika."),
            ("fig", bundel.foto("fotos/wereld-werelddelen-oceanen.png",
                                bron="Kaart: Willem1, Wikimedia Commons, CC BY-SA 2.5"),
             "De werelddelen en de oceanen. De <strong>evenaar</strong> snijdt dwars door "
             "<strong>Afrika</strong>: dat is het werelddeel dat voor een deel op het noordelijk en voor een "
             "deel op het zuidelijk halfrond ligt. Antarctica valt onder de onderrand van deze kaart weg, maar "
             "het is er wel degelijk een."),
            ("p", "Een <strong>globe</strong> is een bol waarop de aarde afgebeeld staat. Een bol is de enige "
                  "juiste vorm: leg je de aarde plat op papier, dan moet er ergens gerekt of geknepen worden. "
                  "Daardoor blijven de afmetingen van de werelddelen op een wereldkaart niet allemaal even juist "
                  "als op een globe. Groenland lijkt op veel kaarten reusachtig, en dat is het niet."),
            ("p", "Een boek vol kaarten van landen en werelddelen heet een <strong>atlas</strong>. Moet je de "
                  "ligging van een stad in Australië opzoeken, dan begin je achteraan, bij het "
                  "<strong>register</strong>: daar staat alfabetisch bij elke naam op welke bladzijde en in "
                  "welk vak ze te vinden is. Bladeren tot je ze ziet duurt veel langer."),
            ("weetje", "Op een <strong>satellietbeeld</strong> zie je het verschil tussen een stad en een bos "
                       "aan de <strong>kleur en het patroon van het oppervlak</strong>: grijze blokken met "
                       "rechte lijnen ertussen tegenover een donkergroene vlek zonder lijnen."),
        ]),
        dict(kop="Absoluut en relatief situeren", blokken=[
            ("p", "Een plaats <strong>situeren</strong> is zeggen waar ze ligt. Dat kan op twee manieren."),
            ("fig", tabel(["manier", "wat je zegt", "voorbeeld"], [
                ["<strong>absoluut</strong>", "met geografische coördinaten", "51° noorderbreedte, 4° oosterlengte"],
                ["<strong>relatief</strong>", "ten opzichte van iets anders", "ten noorden van de Maas, bij de Nederlandse grens"],
            ]), "Allebei zijn juist, en je mag ze allebei gebruiken. Ze vullen elkaar aan."),
            ("p", "De <strong>geografische breedte</strong> geeft aan hoe ver een plaats van de evenaar ligt. "
                  "Ligt ze erboven, dan spreken we van noorderbreedte; eronder van zuiderbreedte. De "
                  "<strong>geografische lengte</strong> geeft aan hoe ver ze van de nulmeridiaan ligt: "
                  "<strong>oosterlengte</strong> als ze ten oosten van Greenwich ligt, westerlengte als ze ten "
                  "westen ligt."),
            ("kader", "Bij coördinaten noem je <strong>eerst de breedte en daarna de lengte</strong>. "
                      "15° zuiderbreedte en 50° westerlengte betekent dus: onder de evenaar en ten westen van "
                      "Greenwich. Twee verschillende plaatsen kunnen nooit precies dezelfde coördinaten hebben — "
                      "dat is net de bedoeling van het stelsel."),
            ("p", "België ligt op ongeveer <strong>50 graden noorderbreedte</strong>. De fiche vraagt om plaatsen "
                  "in Europa en de wereld <strong>op 1 graad nauwkeurig</strong> te situeren: je antwoord mag "
                  "hoogstens één graad naast de juiste liggen."),
        ]),
        dict(kop="Referentiepunten en hulpmiddelen", blokken=[
            ("p", "Om iets te situeren gebruik je <strong>referentiepunten</strong>: vaste dingen waarvan "
                  "iedereen weet waar ze liggen. De fiche deelt ze in drie soorten in."),
            ("fig", tabel(["soort", "voorbeelden"], [
                ["<strong>sterrenkundig</strong>", "de evenaar, de keerkringen, de polen, de poolcirkels"],
                ["<strong>staatkundig</strong>", "de gemeente, de provincie, het land, het werelddeel"],
                ["<strong>topografisch</strong>", "de oceanen, de rivieren, de reliëfeenheden, de bergketens"],
            ]), "Sterrenkundig heeft met de stand van de aarde te maken, staatkundig met grenzen die mensen "
                "getrokken hebben, topografisch met wat er in het landschap zelf ligt."),
            ("p", "Wandel je in de Ardennen met een papieren kaart en wil je weten welke kant je uit kijkt, dan "
                  "gebruik je een <strong>kompas</strong>. Wil je je eigen positie tot op enkele meters kennen, "
                  "midden in een bos zonder herkenningspunten, dan gebruik je een "
                  "<strong>satellietnavigatiesysteem</strong>. Dat berekent je positie uit de signalen van "
                  "satellieten."),
            ("weetje", "Je kan je ook oriënteren zónder toestel: de stand van de zon zegt veel. Bij ons staat de "
                       "zon rond de middag in het zuiden. En op je kaart volg je gewoon de noordpijl."),
        ]),
    ],
    onthoud=[
        "De evenaar verdeelt de aarde in het noordelijk en het zuidelijk halfrond.",
        "Meridianen lopen van pool tot pool en zijn even lang; breedtecirkels worden korter naar de polen toe.",
        "De nulmeridiaan loopt door Greenwich; tegenover haar ligt de datumlijn.",
        "Keerkringen op 23,5°, poolcirkels op 66,5°. Breedte tot 90°, lengte tot 180°.",
        "Zeven werelddelen, Antarctica inbegrepen. België ligt in Europa; de evenaar snijdt door Afrika.",
        "De Atlantische Oceaan ligt tussen Europa en Amerika.",
        "Absoluut situeren = met coördinaten; relatief situeren = ten opzichte van iets anders.",
        "Bij coördinaten noem je eerst de breedte, dan de lengte. België ligt op ongeveer 50° N.",
        "Referentiepunten: sterrenkundig, staatkundig en topografisch.",
        "Kompas voor de richting, satellietnavigatie voor je eigen positie, atlas met register om op te zoeken.",
    ],
)

# ───────────────────────────────────────── 3. De lagen van een landschap
BUNDELS["de-lagen-van-een-landschap"] = dict(
    vak=VAK, niveau=SPARK, titel="De lagen van een landschap",
    onder="De natuurlijke lagen — reliëf, klimaat, water, bodem, ondergrond en vegetatie — en de lagen die de mens erbovenop legt.",
    secties=[
        dict(kop="Een landschap bestaat uit lagen", blokken=[
            ("p", "Twee streken kunnen er totaal anders uitzien. De aardrijkskunde verklaart dat door naar de "
                  "<strong>lagen</strong> te kijken waaruit een landschap is opgebouwd. Elke laag is iets anders, "
                  "en samen maken ze het landschap."),
            ("fig", svg.landschapslagen(), "De natuurlijke of <strong>fysischgeografische</strong> lagen links, "
                                           "de menselijke lagen rechts. De natuurlijke liggen er het langst; de "
                                           "menselijke kunnen op enkele jaren tijd sterk veranderen."),
            ("kader", "Natuurlijk zijn: het reliëf, het klimaat, het water, de bodem, de ondergrond en de "
                      "vegetatie. Van de mens zijn: het landgebruik, de bebouwing, de transportwegen en de "
                      "ontginning."),
        ]),
        dict(kop="Reliëf, klimaat en vegetatie", blokken=[
            ("p", "Het <strong>reliëf</strong> van een gebied zijn de <strong>hoogteverschillen</strong> erin. "
                  "Daar horen de <strong>reliëfelementen</strong> bij: de helling, het hoogteverschil en de "
                  "horizonlijn. Let op het onderscheid tussen een <strong>vlakte</strong> en een "
                  "<strong>plateau</strong>: allebei zijn ze vlak bovenaan, maar een plateau ligt "
                  "<strong>hoog</strong> en een vlakte laag. Een plateau is dus een <strong>hooggelegen</strong> gebied "
                  "dat bovenaan vlak is, en niet sterk golvend; een vlakte ligt laag. Ze liggen niet even hoog "
                  "boven de zeespiegel."),
            ("p", "Het <strong>klimaat</strong> beschrijft de fiche met drie woorden: <strong>warm</strong>, "
                  "<strong>gematigd</strong> en <strong>koud</strong>. Verwar het niet met het weer: het "
                  "<strong>weer</strong> is van nu, het <strong>klimaat</strong> is het gemiddelde over jaren."),
            ("p", "De natuurlijke <strong>vegetatie</strong> is wat er vanzelf zou groeien. De fiche onderscheidt "
                  "<strong>naaldbomen</strong>, <strong>loofbomen</strong> en <strong>grassen en mossen</strong>. "
                  "Loofbomen verliezen hun blad in de winter, naaldbomen meestal niet. In koude streken, waar de "
                  "zomer kort is, groeien er van nature vooral mossen en heel lage planten: voor een boom is het "
                  "groeiseizoen er te kort."),
        ]),
        dict(kop="Bodem, ondergrond en water", blokken=[
            ("p", "De <strong>bodem</strong> is de bovenste losse laag, die waarin planten hun wortels zetten. "
                  "De <strong>textuur</strong> van een bodem zegt uit hoe grove of fijne korrels hij bestaat."),
            ("fig", tabel(["bodemsoort", "korrels", "wat het water doet"], [
                ["<strong>zand</strong>", "grof, je voelt ze knerpen", "zakt er snel doorheen"],
                ["<strong>leem</strong>", "fijn, melig als bloem", "blijft een tijd hangen"],
                ["<strong>klei</strong>", "de fijnste van de drie", "wordt <strong>moeilijk doorgelaten</strong>, blijft het langst staan"],
            ]), "Klei houdt het water dus het langst vast. In de Kempen ligt een zandbodem: het regenwater zakt "
                "er snel weg, en dat merk je aan wat er groeit."),
            ("p", "Onder de bodem ligt de <strong>ondergrond</strong>. Die bestaat uit zand, leem, klei of uit "
                  "<strong>vast gesteente</strong> — <strong>kalksteen</strong> bijvoorbeeld, of zandsteen of "
                  "leisteen."),
            ("p", "Het <strong>water</strong> is een aparte laag, want het vormt en verandert de andere lagen "
                  "mee: het slijt het reliëf uit, het voert bodemdeeltjes aan en af, en het bepaalt wat er kan "
                  "groeien. Een natte bodem en een droge bodem laten dus niet dezelfde planten groeien."),
        ]),
        dict(kop="Wat de mens met de grond doet", blokken=[
            ("p", "Kijk je van een heuvel over een streek uit en zie je akkers, een dorp, een spoorlijn en een "
                  "fabriek, dan zie je <strong>hoe de mensen de grond gebruiken</strong>. Het geheel daarvan "
                  "heet het <strong>landgebruik</strong>."),
            ("p", "In de landbouw onderscheidt de fiche drie takken. <strong>Akkerbouw</strong> is gewassen telen "
                  "op het veld. <strong>Veeteelt</strong> is dieren houden voor vlees, melk of eieren. "
                  "<strong>Tuinbouw</strong> is teelt op kleinere percelen: groenten, fruitteelt, serreteelt. "
                  "Houdt een boer melkkoeien én teelt hij maïs, dan heet dat <strong>gemengde landbouw</strong>."),
            ("weetje", "Een <strong>serre</strong> maakt de teler minder afhankelijk van het weer buiten: hij "
                       "kiest er zelf de temperatuur en het licht, en kan dus vroeger of langer oogsten."),
            ("fig", tabel(["menselijke laag", "wat je ziet"], [
                ["<strong>bebouwing</strong>", "de huizen en gebouwen zelf, en hoe dicht ze bij elkaar staan"],
                ["<strong>lijninfrastructuur</strong>", "een autosnelweg, een spoorlijn, een hoogspanningsleiding"],
                ["<strong>nutsvoorzieningen</strong>", "leidingen en kabels voor water, gas en stroom"],
                ["<strong>ontginning</strong>", "grondstoffen uit de bodem of ondergrond halen"],
                ["<strong>recreatie en toerisme</strong>", "een camping, een skipiste, een provinciaal domein met wandelpaden"],
            ]), "De menselijke lagen die de vakfiche noemt, met waaraan je ze op het terrein herkent."),
            ("p", "Let op één woordenpaar dat makkelijk door elkaar loopt: een "
                  "<strong>woongebied</strong> en de <strong>bebouwing</strong> erin zijn niet precies "
                  "hetzelfde. Het woongebied is <strong>het gebied</strong>, de bebouwing is "
                  "<strong>wat erin staat</strong>."),
            ("p", "Met de <strong>verspreiding</strong> van de bebouwing bedoelen we of de huizen dicht bijeen "
                  "of verspreid staan. Staan er langs een gewestweg huizen in één rij aan beide kanten, "
                  "kilometers ver, dan heet dat <strong>lintbebouwing</strong>."),
            ("p", "Een put waaruit steen of zand gehaald wordt, heet een <strong>groeve</strong>."),
            ("kader", "Waarom staat een fabriek langs een kanaal en vlak bij een autosnelweg? Omdat grondstoffen "
                      "en producten er vlot aankomen en weggaan. En waarom staan er in een havengebied zo weinig "
                      "woningen? Omdat het er lawaaierig is en de grond voor de bedrijven dient. Ligging is "
                      "zelden toeval."),
            ("p", "Toerisme verandert het landschap wél, ook al blijven toeristen maar even: er komen "
                  "campings, hotels, parkings en liften voor terug, en die blijven staan."),
        ]),
    ],
    onthoud=[
        "Natuurlijke lagen: reliëf, klimaat, water, bodem, ondergrond, vegetatie.",
        "Menselijke lagen: landgebruik, bebouwing, transportwegen en nutsvoorzieningen, ontginning.",
        "Reliëf = de hoogteverschillen. Reliëfelementen: helling, hoogteverschil, horizonlijn.",
        "Een vlakte ligt laag en vlak, een plateau hoog en vlak.",
        "Weer is van nu, klimaat is het gemiddelde over jaren. Klimaat: warm, gematigd, koud.",
        "Vegetatie: naaldbomen, loofbomen, grassen en mossen. Loofbomen verliezen hun blad.",
        "Textuur = hoe grof of fijn de korrels zijn. Klei houdt water het langst vast, zand het kortst.",
        "Landbouw: akkerbouw, veeteelt, tuinbouw. Allebei samen is gemengde landbouw.",
        "Lijninfrastructuur: snelweg, spoorlijn, hoogspanningsleiding. Nutsvoorzieningen: water, gas, stroom.",
        "Lintbebouwing is een rij huizen langs een weg. Een groeve is een put waaruit steen of zand komt.",
    ],
)

# ───────────────────────────────────────── 4. Waarom landschappen verschillen
BUNDELS["waarom-landschappen-verschillen"] = dict(
    vak=VAK, niveau=SPARK, titel="Waarom landschappen verschillen",
    onder="De reliëfeenheden van België, de klimaat- en vegetatiezones van de wereld, en het samenspel dat een landschap maakt.",
    secties=[
        dict(kop="Het reliëf van België in drie trappen", blokken=[
            ("p", "Rijd je van de Belgische kust naar de Ardennen, dan gaat het landschap "
                  "<strong>geleidelijk omhoog</strong>. Niet met één sprong, maar in drie trappen. België kent "
                  "drie soorten reliëfeenheden: <strong>laagvlaktes</strong>, <strong>laagplateaus</strong> en "
                  "<strong>plateaus</strong>."),
            ("fig", svg.relieftrappen(), "Een schema, geen kaart: het toont de logica die je moet zien, namelijk "
                                         "dat het land klimt van het noordwesten naar het zuidoosten."),
            ("fig", tabel(["trap", "de eenheden van de fiche"], [
                ["<strong>laagvlaktes</strong>", "de Kempense Laagvlakte, de Laagvlakte van de Kust, de Vlaamse Laagvlakte"],
                ["<strong>laagplateaus</strong>", "het Haspengouws, het Henegouws, het Brabants en het Kempens Laagplateau"],
                ["<strong>plateaus en de eenheden van het zuiden</strong>",
                 "het Plateau van Herve, het Lotharings Plateau, de Fagne-Famennedepressie, het Plateau van de "
                 "Ardennen, het Plateau van de Hoge Venen, de Heuvelruggen van de Condroz"],
            ]), "Dertien namen. Ze staan hier op volgorde van laag naar hoog, want zo onthoud je ze het best."),
            ("p", "De <strong>polders</strong> liggen in de Laagvlakte van de Kust. Het hoogst gelegen is het "
                  "<strong>Plateau van de Ardennen</strong>, en het hoogste punt van het land, het "
                  "<strong>Signaal van Botrange</strong> op 694 meter, ligt op het Plateau van de Hoge "
                  "<strong>Venen</strong>."),
            ("kader", "Let op de <strong>Heuvelruggen van de Condroz</strong>. Een plateau is bovenaan vlak, "
                      "maar de Condroz niet: daar wisselen ruggen en dalen elkaar af, en dat is precies waarom "
                      "hij heuvelruggen heet."),
        ]),
        dict(kop="De klimaatzones en de vegetatiezones van de wereld", blokken=[
            ("p", "De fiche noemt drie <strong>klimaatzones</strong>: <strong>warm</strong>, "
                  "<strong>gematigd</strong> en <strong>koud</strong>. De warmste liggen "
                  "<strong>rond de evenaar</strong>, want daar valt het zonlicht het steilst in. Naar de polen "
                  "toe valt het steeds schuiner en wordt het kouder. België ligt in de "
                  "<strong>gematigde</strong> zone."),
            ("fig", bundel.foto("fotos/wereld-klimaatzones-kim.png"),
             "Op deze kaart staan <strong>vijf</strong> zones. Dat is geen andere indeling dan die van de fiche, "
             "maar een fijnere. Hieronder staat hoe de vijf op de drie vallen."),
            ("fig", tabel(["op de kaart", "wat het is bij ons"], [
                ["blauw, <strong>koude zone</strong>", "<strong>koud</strong> — rond de polen"],
                ["groen, <strong>gematigde zone</strong>", "<strong>gematigd</strong> — hier ligt België"],
                ["geel, <strong>warme zone</strong> en rood, <strong>natte zone</strong>",
                 "<strong>warm</strong> — rond de evenaar; de natte zone is het regenwoud"],
                ["oranje, <strong>droge zone</strong>",
                 "geen vierde trap: deze zone is <strong>niet</strong> uitgehaald om haar temperatuur maar om "
                 "haar <strong>neerslag</strong>. Ze ligt grotendeels in de warme zone, en met haar rand tegen "
                 "de gematigde aan"],
            ]), "De drie die jij moet kennen zijn koud, gematigd en warm. De kaart splitst de warme zone verder "
                "op en haalt er de droogste gebieden apart uit."),
            ("p", "Bij elke klimaatzone hoort een natuurlijke begroeiing. Dat zijn de "
                  "<strong>vegetatiezones</strong>."),
            ("fig", tabel(["vegetatiezone", "waar en hoe"], [
                ["<strong>toendra</strong>", "vlak bij de polen: mossen, korstmossen en heel lage planten"],
                ["<strong>taiga</strong>", "een brede gordel naaldbos in het noorden"],
                ["<strong>loofwoud</strong>", "de gematigde zone — hier ligt ook België"],
                ["<strong>steppe</strong>", "droge graslanden, met te weinig regen voor bos"],
                ["<strong>woestijn</strong>", "veel te weinig neerslag; daardoor groeit er bijna niets"],
                ["<strong>savanne</strong>", "grasvlakten met verspreide bomen, tussen de woestijn en het regenwoud"],
                ["<strong>tropisch regenwoud</strong>", "rond de evenaar: warm en nat het hele jaar door"],
            ]), "De zeven zones van de vakfiche, van de pool naar de evenaar."),
            ("fig", bundel.foto("fotos/wereld-vegetatiezones.png",
                                bron="Kaart: Vzb83, Wikimedia Commons, CC BY-SA 3.0"),
             "Deze kaart heeft een Engelse legende met méér zones dan de zeven van de fiche. Gebruik de sleutel "
             "hieronder om ze terug te brengen tot wat jij moet kennen."),
            ("fig", tabel(["zoals het in de legende staat", "dat is onze zone"], [
                ["<em>tundra</em>, <em>alpine tundra</em>, <em>ice sheet and polar desert</em>", "<strong>toendra</strong>"],
                ["<em>taiga</em>, <em>montane forests and grasslands</em>", "<strong>taiga</strong>"],
                ["<em>temperate broadleaf forest</em>, <em>subtropical evergreen forest</em>, <em>Mediterranean vegetation</em>", "<strong>loofwoud</strong>"],
                ["<em>temperate steppe and savanna</em>, <em>dry steppe and thorn forest</em>", "<strong>steppe</strong>"],
                ["<em>arid desert</em>, <em>semiarid desert</em>, <em>xeric shrubland</em>", "<strong>woestijn</strong>"],
                ["<em>grass savanna</em>, <em>tree savanna</em>, <em>dry forest and woodland savanna</em>", "<strong>savanne</strong>"],
                ["<em>tropical rainforest</em>, <em>monsoon forests and mosaic</em>", "<strong>tropisch regenwoud</strong>"],
            ]), "De achttien namen van de legende, teruggebracht tot de zeven die jij moet kennen. Zoek de kleur "
                "op de kaart, lees de Engelse naam in de legende, en kijk hier welke zone dat is."),
        ]),
        dict(kop="Waar de mensen wonen", blokken=[
            ("p", "De <strong>bevolkingsspreiding</strong> van de wereld zegt waar veel en waar weinig mensen "
                  "wonen. Het aantal inwoners per vierkante kilometer heet de "
                  "<strong>bevolkingsdichtheid</strong>."),
            ("fig", bundel.foto("fotos/wereld-bevolkingsdichtheid.png",
                                bron="Kaart: Petnog, Wikimedia Commons, CC BY 4.0, gegevens 2020"),
             "Donker is dichtbevolkt, licht is dunbevolkt."),
            ("p", "Van nature dunbevolkt zijn de <strong>woestijnen</strong> (te droog), de "
                  "<strong>hooggebergten</strong> (te koud en te steil) en de <strong>poolgebieden</strong> "
                  "(te koud). België hoort daar niet bij: het is juist een van de "
                  "<strong>dichtstbevolkte</strong> landen van Europa."),
        ]),
        dict(kop="Het samenspel van de lagen", blokken=[
            ("p", "In de Ardennen staan veel bossen, in Haspengouw liggen vooral akkers en boomgaarden. Dat komt "
                  "niet door één ding maar door het <strong>samenspel van reliëf, bodem en klimaat</strong>. De "
                  "lagen staan niet los van elkaar: ze beïnvloeden elkaar voortdurend."),
            ("p", "Klim je in een gebergte omhoog, dan groeit er steeds minder. Daar zie je de relatie tussen "
                  "<strong>reliëf, klimaat en vegetatie</strong>: hoger is kouder, en boven een bepaalde hoogte "
                  "is het te koud voor bomen. Die hoogte heet de <strong>boomgrens</strong>."),
            ("fig", tabel(["bodem", "wat de landbouw ermee doet"], [
                ["<strong>leem</strong>", "vruchtbaar en goed voor akkerbouw"],
                ["<strong>natte grond</strong>", "leent zich eerder voor weiland"],
                ["<strong>schrale zandgrond</strong>", "levert minder op per hectare"],
            ]), "Daarom liggen de akkers en de weiden niet zomaar ergens."),
            ("p", "Veel grote steden liggen aan een <strong>rivier</strong>, omdat water drinken, vervoer en "
                  "handel mogelijk maakte. En van twee dorpen die even ver van de stad liggen, groeit dat ene "
                  "veel sterker omdat het aan een <strong>spoorlijn</strong> ligt en het andere niet. Twee "
                  "landschappen met hetzelfde klimaat kunnen dus toch heel verschillend zijn, omdat de "
                  "<strong>andere lagen</strong> er anders zijn."),
            ("p", "Een <strong>natuurlijk landschap</strong> is een landschap dat de mens nauwelijks veranderd "
                  "heeft. Een landschap dat vrijwel volledig door mensen gevormd is, heet een "
                  "<strong>menselijk landschap</strong>. De <strong>polders</strong> zijn daar een mooi "
                  "voorbeeld van: zonder dijken en pompen lag daar water."),
        ]),
        dict(kop="Duurzaamheid en de vijf P's", blokken=[
            ("p", "<strong>Duurzaamheid</strong> betekent: voorzien in wat we nu nodig hebben zonder later "
                  "tekort te doen. Om erover na te denken gebruikt men het <strong>5P-model</strong>."),
            ("fig", svg.vijfp(), "De vijf P's. Vrede hoort erbij omdat er in een oorlog niets opgebouwd of "
                                 "beschermd wordt."),
            ("p", "Legt een gemeente een nieuw bos aan en beschermt ze een beekvallei, dan valt dat vooral onder "
                  "<strong>Planet</strong>. Betaalt een bedrijf zijn werknemers een eerlijk loon en zorgt het "
                  "voor veilige werkomstandigheden, dan valt dat vooral onder <strong>People</strong>. De P die "
                  "over samenwerkingsverbanden gaat, is <strong>Partnership</strong>."),
            ("kader", "De vijf P's hangen samen, en dat maakt het lastig: wat de ene vooruithelpt, kan de andere "
                      "tegelijk schaden. Daarom blijft duurzaamheid altijd een afweging. En een landschap dat "
                      "vandaag duurzaam beheerd wordt, blijft daarna niet vanzelf zo: het vraagt onderhoud."),
        ]),
    ],
    onthoud=[
        "België klimt van het noordwesten naar het zuidoosten: laagvlaktes, laagplateaus, plateaus.",
        "De polders liggen in de Laagvlakte van de Kust; het Plateau van de Ardennen ligt het hoogst.",
        "Het Signaal van Botrange (694 m) ligt op het Plateau van de Hoge Venen.",
        "De Heuvelruggen van de Condroz zijn niet vlak: ruggen en dalen wisselen elkaar af.",
        "Klimaatzones: warm, gematigd, koud. Het warmst is het rond de evenaar; België ligt gematigd.",
        "Zeven vegetatiezones: toendra, taiga, loofwoud, steppe, woestijn, savanne, tropisch regenwoud.",
        "Dunbevolkt van nature: woestijnen, hooggebergten en poolgebieden. België is dichtbevolkt.",
        "Bevolkingsdichtheid = het aantal inwoners per vierkante kilometer.",
        "De lagen beïnvloeden elkaar: reliëf, bodem en klimaat samen verklaren een landschap.",
        "De vijf P's: People, Planet, Prosperity, Peace, Partnership. Ze hangen samen.",
    ],
)

# ───────────────────────────────────────── 5. De aarde beweegt en slijt
BUNDELS["de-aarde-beweegt-en-slijt"] = dict(
    vak=VAK, niveau=SPARK, titel="De aarde beweegt en slijt",
    onder="Aardbevingen en vulkanen, en het trage werk van verwering, erosie en sedimentatie.",
    secties=[
        dict(kop="Aardbevingen", blokken=[
            ("p", "De aardkorst is geen geheel stuk: ze bestaat uit <strong>platen</strong> die traag bewegen. "
                  "Een <strong>aardbeving</strong> ontstaat door een <strong>plotse beweging</strong> van die "
                  "stukken aardkorst. Een scheur waarlangs ze bewegen heet een <strong>breuklijn</strong>."),
            ("p", "Een beving begint niet aan de oppervlakte maar in de diepte, op de plek waar de "
                  "aardkorst schiet. Die plek heet de <strong>haard</strong>. Het punt op het "
                  "aardoppervlak recht daarboven heet het <strong>epicentrum</strong>, en daar is de "
                  "schade meestal het grootst."),
            ("fig", svg.aardbeving(), "De haard in de diepte, het epicentrum er recht boven."),
            ("p", "Het toestel dat de trillingen opmeet en optekent, heet een <strong>seismograaf</strong>. "
                  "Een aardbeving duurt meestal maar <strong>enkele seconden</strong>, ze komt vaker voor "
                  "<strong>langs de randen van platen</strong>, en ze kan gebouwen doen instorten. Ook in "
                  "België komen af en toe <strong>lichte</strong> aardbevingen voor."),
            ("p", "Gebeurt een zware beving op zee, dan kan het water in beweging komen en als een reusachtige "
                  "vloedgolf de kust overspoelen. Zo'n golf heet een <strong>tsunami</strong>."),
            ("kader", "Je kan een aardbeving niet tegenhouden, maar je kan je er wel op voorbereiden: "
                      "<strong>gebouwen zo bouwen dat ze mee kunnen bewegen</strong>. Een stijf gebouw scheurt, "
                      "een gebouw dat meegeeft blijft staan."),
        ]),
        dict(kop="Vulkanen", blokken=[
            ("p", "Ligt er op een ochtend een laag grijze as over de velden en de daken, dan is er in de buurt "
                  "een <strong>vulkaan uitgebarsten</strong>. Bij een uitbarsting komen "
                  "<strong>lava</strong>, <strong>as</strong> en <strong>gassen</strong> naar buiten."),
            ("p", "Hetzelfde gesmolten gesteente heeft twee namen, en welke je gebruikt, hangt af van "
                  "waar het zit. Onder de grond heet het <strong>magma</strong>; komt het naar buiten, dan "
                  "noemen we het <strong>lava</strong>. De trechtervormige opening bovenaan de berg, waar "
                  "het uit komt, heet de <strong>krater</strong>."),
            ("fig", svg.vulkaan(), "Een doorsnede van een vulkaan, met het magma, de lava en de krater."),
            ("p", "Op korte termijn is een uitbarsting een ramp: huizen en akkers verdwijnen onder lava en as, "
                  "mensen moeten hun dorp in allerijl verlaten, en de lucht raakt gevuld met as en gassen. Op "
                  "lange termijn is er ook een keerzijde: de bodem wordt er "
                  "<strong>bijzonder vruchtbaar</strong>. Dat is meteen de reden waarom mensen tóch in de buurt "
                  "van een actieve vulkaan gaan wonen."),
            ("p", "In het jaar 79 werd <strong>Pompeii</strong> bedolven door de uitbarsting van de Vesuvius. "
                  "Op <strong>IJsland</strong> liggen zoveel vulkanen omdat het eiland op de "
                  "<strong>grens van twee platen</strong> ligt, precies waar magma omhoog kan."),
            ("weetje", "Niet alle vulkanen barsten regelmatig uit. Sommige slapen honderden jaren, andere zijn "
                       "uitgedoofd. Alleen de actieve zijn een blijvend gevaar."),
            ("p", "Een uitbarsting kan een landschap in enkele dagen sterker veranderen dan erosie in duizend "
                  "jaar. De aarde verandert dus op twee snelheden tegelijk: met schokken en heel geleidelijk."),
        ]),
        dict(kop="Verwering, erosie en sedimentatie", blokken=[
            ("p", "Aan een oude kerk brokkelen de stenen aan de buitenkant af. Dat is "
                  "<strong>verwering</strong>: de steen wordt <strong>ter plaatse</strong> afgebroken, zonder "
                  "dat hij weggevoerd wordt."),
            ("fig", svg.slijtage(), "Drie stappen die op elkaar volgen. Verwering breekt af, erosie voert weg, "
                                    "sedimentatie zet elders weer af."),
            ("p", "Bij <strong>vorstverwering</strong> dringt water in een barst in de rots, bevriest en zet "
                  "uit. IJs neemt meer plaats in dan water, dus de barst wordt opengeduwd en de rots springt "
                  "uiteen. En regenwater kan <strong>kalksteen</strong> langzaam <strong>oplossen</strong>: "
                  "daarom liggen er in kalkstreken zoals de Condroz zoveel <strong>grotten</strong>."),
            ("p", "<strong>Erosie</strong> is het wégvoeren. Dat kan door <strong>stromend water</strong>, door "
                  "<strong>wind</strong> en door <strong>bewegend ijs</strong>."),
            ("fig", svg.dalvormen(), "Een rivier snijdt zich in een plateau in en maakt een smal <strong>V-dal</strong>. "
                                     "Een gletsjer schuurt breed uit en laat een <strong>U-dal</strong> achter, "
                                     "herkenbaar aan de brede bodem en de steile wanden."),
            ("p", "<strong>Sedimentatie</strong> is het afzetten van meegevoerd materiaal op een andere plaats. "
                  "Een rivier zet het meeste af waar ze het <strong>traagst</strong> stroomt, niet waar ze het "
                  "snelst gaat: snel water houdt alles in beweging, traag water laat het vallen. Waar een rivier "
                  "uitmondt ontstaat zo een <strong>delta</strong>, een waaier van afzettingen. Ook een "
                  "<strong>zandbank</strong> en een <strong>duinengordel</strong> zijn door sedimentatie "
                  "ontstaan."),
            ("p", "Een heuvel van zand die door de wind is opgewaaid, heet een <strong>duin</strong>. In een "
                  "woestijn groeien er nauwelijks planten die het zand vasthouden, dus heeft de wind er vrij "
                  "spel en verplaatsen de duinen zich over de jaren heen. Ook de <strong>leembodem</strong> van "
                  "Haspengouw is duizenden jaren geleden door de <strong>wind</strong> aangevoerd."),
            ("kader", "Planten en bomen beschermen de bodem tegen erosie, want hun wortels houden de grond vast. "
                      "Ploegt een boer een helling van boven naar beneden, dan spoelt het water bij een zware bui "
                      "door de voren en neemt het grond mee. Ploegen langs de helling houdt het water tegen."),
            ("p", "Aan de kust breekt de zee stukken van de kustlijn af: dat heet <strong>kusterosie</strong>. "
                  "Verwering, erosie en sedimentatie werken meestal traag, maar niet zó traag dat je ze nooit "
                  "ziet: na één zware storm of één slagregen kan je het verschil met het blote oog vaststellen."),
        ]),
    ],
    onthoud=[
        "Een aardbeving ontstaat door plotse beweging van stukken aardkorst langs een breuklijn.",
        "De haard ligt in de diepte, het epicentrum is het punt recht erboven. Een seismograaf meet de trillingen.",
        "Een zeebeving kan een tsunami veroorzaken. Aardbevingsbestendig bouwen betekent: meebewegen.",
        "Magma zit onder de grond, lava stroomt erbovenop. De opening bovenaan heet de krater.",
        "Een uitbarsting geeft lava, as en gassen; op lange termijn wordt de bodem er heel vruchtbaar.",
        "Verwering breekt ter plaatse af, erosie voert weg, sedimentatie zet elders af.",
        "Vorstverwering: water bevriest in een barst en zet uit. Regenwater lost kalksteen op (grotten).",
        "Erosie gebeurt door stromend water, wind en bewegend ijs. Een rivier maakt een V-dal, een gletsjer een U-dal.",
        "Een rivier zet materiaal af waar ze het traagst stroomt: zo ontstaat een delta.",
        "Duin, zandbank en delta ontstaan door sedimentatie. De leem van Haspengouw is aangewaaid.",
    ],
)

# ───────────────────────────────────────── 6. Het weer en zijn uitschieters
BUNDELS["het-weer-en-zijn-uitschieters"] = dict(
    vak=VAK, niveau=SPARK, titel="Het weer en zijn uitschieters",
    onder="De weerelementen en hun meettoestellen, het klimatogram, en wat extreem weer met een landschap doet.",
    secties=[
        dict(kop="De weerelementen en hun toestellen", blokken=[
            ("p", "Zeg je dat het vandaag 9 graden is, dat het stevig waait en dat het regent, dan beschrijf je "
                  "<strong>het weer van vandaag</strong>. De fiche noemt drie <strong>weerelementen</strong>: "
                  "de <strong>temperatuur</strong>, de <strong>luchtdruk</strong> en de "
                  "<strong>neerslag</strong>, en daarbij hoort ook de wind."),
            ("fig", tabel(["wat je meet", "waarmee", "in welke eenheid"], [
                ["temperatuur", "een <strong>thermometer</strong>", "graden Celsius"],
                ["luchtdruk", "een <strong>barometer</strong>", "<strong>hectopascal</strong>"],
                ["neerslag", "een <strong>regenmeter</strong>", "<strong>millimeter</strong>"],
                ["windsnelheid", "een <strong>anemometer</strong>", "kilometer per uur, of Beaufort"],
            ]), "In België meten we de temperatuur in graden Celsius, niet in Fahrenheit."),
            ("p", "Eén millimeter neerslag is één liter water per vierkante meter. Viel er 12 millimeter regen, "
                  "dan kwam er dus <strong>12 liter</strong> op elke vierkante meter terecht."),
            ("p", "Een <strong>westenwind</strong> is een wind die <strong>uit</strong> het westen komt. Een "
                  "wind wordt altijd genoemd naar waar hij vandaan komt, niet naar waar hij heen gaat. De "
                  "schaal waarmee de windkracht in stappen van 0 tot 12 wordt aangegeven, is de schaal van "
                  "<strong>Beaufort</strong>."),
            ("weetje", "De thermometer van een weerstation staat in een wit kastje met spleetjes, een "
                       "weerhut. Het wit en de spleetjes houden de zon weg maar laten de lucht door, zodat je "
                       "de temperatuur van de lucht meet en niet die van de zon op het glas."),
        ]),
        dict(kop="Hoge en lage druk", blokken=[
            ("fig", svg.drukgebieden(), "Bij <strong>hoge druk</strong> zakt de lucht en lossen de wolken op. "
                                        "Bij <strong>lage druk</strong> stijgt de lucht, koelt af, en vormen "
                                        "zich wolken."),
            ("p", "Een <strong>hogedrukgebied</strong> brengt dus rustig en meestal droog weer. Een gebied met "
                  "lage luchtdruk heet een <strong>depressie</strong>: die voert wolken en regen aan. Daalt de "
                  "barometer sterk, dan mag je <strong>wolken, wind en kans op regen</strong> verwachten."),
            ("p", "Op een bergtop is het meestal kouder dan in het dal eronder, omdat de lucht hoger "
                  "<strong>dunner</strong> is en minder warmte vasthoudt."),
        ]),
        dict(kop="Het klimatogram", blokken=[
            ("p", "Een <strong>klimatogram</strong> is een grafiek met de temperatuur en de neerslag per maand. "
                  "De staafjes zijn de neerslag, de lijn is de temperatuur."),
            ("fig", svg.klimaatdiagram([3, 4, 7, 10, 14, 17, 19, 19, 16, 12, 7, 4],
                                       [76, 63, 70, 51, 62, 72, 74, 64, 59, 70, 76, 81],
                                       plaats="Ukkel, België"),
             "Het klimatogram van België: gespreide neerslag het hele jaar door, en een duidelijk warme zomer."),
            ("p", "Lopen de staafjes in juli en augustus heel hoog en zijn ze in januari bijna leeg, dan valt "
                  "daar <strong>de meeste neerslag in de zomer</strong>. En je kan uit één klimatogram ook "
                  "afleiden op welk <strong>halfrond</strong> de plaats ligt: is het warmst in juli, dan is het "
                  "het noordelijk halfrond; is het warmst in januari, dan het zuidelijk."),
            ("p", "<strong>Neerslag</strong> is niet alleen regen. Ook <strong>sneeuw</strong> en "
                  "<strong>hagel</strong> zijn vormen van neerslag."),
            ("kader", "Het weer van morgen kan niet tot op het uur nauwkeurig voorspeld worden. Een weerbericht "
                      "geeft kansen, geen zekerheden, en hoe verder vooruit, hoe minder zeker."),
        ]),
        dict(kop="Extreem weer", blokken=[
            ("p", "<strong>Extreem weer</strong> is weer dat <strong>sterk afwijkt van het gewone</strong>. Na "
                  "een nacht met heel veel regen staat een straat blank en is een stuk van een akker "
                  "weggespoeld: dan heeft extreem weer het landschap veranderd."),
            ("p", "Valt er in korte tijd heel veel regen op een droge, harde bodem, dan zakt het water niet weg "
                  "maar <strong>stroomt het over de grond weg</strong>. <strong>Verharde</strong> oppervlakken "
                  "zoals wegen en parkings doen hetzelfde, en vergroten dus de kans op wateroverlast. Een "
                  "overstroming laat sporen na: een laag <strong>slib</strong> op de velden, weggespoelde wegen "
                  "en bruggen, en uitgesleten <strong>geulen</strong> in de akkers."),
            ("fig", tabel(["maatregel tegen wateroverlast", "wat ze doet"], [
                ["een <strong>overstromingsgebied</strong> naast de rivier", "geeft het teveel aan water een plaats om te staan"],
                ["<strong>regenwater laten insijpelen</strong>", "het zakt in de grond in plaats van meteen af te vloeien"],
                ["<strong>beken meer ruimte geven</strong> om te kronkelen", "het water stroomt trager en piekt minder"],
            ]), "Alle drie komen ze op hetzelfde neer: water plaats en tijd geven in plaats van het weg te jagen."),
            ("p", "Een dorp aan de <strong>voet</strong> van een helling loopt onder en een dorp bovenop niet, "
                  "want het water stroomt van de helling naar beneden."),
            ("fig", tabel(["storm", "wat het is"], [
                ["<strong>storm</strong>", "vanaf windkracht <strong>9</strong> op de schaal van Beaufort"],
                ["<strong>orkaan</strong>", "een tropische wervelstorm boven warm zeewater"],
                ["<strong>tornado</strong>", "een smalle, draaiende luchtslurf onder een onweerswolk"],
                ["<strong>stormvloed</strong>", "water dat bij storm tegen de kust wordt opgestuwd"],
            ]), "Een orkaan bestrijkt een veel breder gebied dan een tornado; een tornado is smal maar hevig."),
            ("p", "Orkanen ontstaan enkel boven <strong>warm zeewater</strong>, omdat warm water veel damp en "
                  "energie levert. Het rustige midden van de storm heet het <strong>oog</strong>. Een "
                  "<strong>tornado</strong> ontstaat meestal uit een zware <strong>onweersbui</strong>."),
            ("p", "Een <strong>stormvloed</strong> is aan onze kust gevaarlijker als hij samenvalt met "
                  "<strong>springtij</strong>, omdat het water dan toch al hoger staat. Extreem weer komt ook in "
                  "België voor: een <strong>hagelbui</strong> kan in enkele minuten een hele oogst vernielen, en "
                  "een zware storm breekt bomen doormidden, doet er andere met wortel en al omwaaien en laat open "
                  "plekken in een bos achter."),
            ("kader", "Kondigt een weerbericht <strong>code oranje</strong> aan, dan wordt er gevaarlijk weer "
                      "verwacht. Geel is opletten, oranje is gevaarlijk, rood is zeer gevaarlijk."),
        ]),
    ],
    onthoud=[
        "Weerelementen: temperatuur, luchtdruk, neerslag (en wind). Weer is van nu, klimaat is het gemiddelde.",
        "Thermometer = temperatuur, barometer = luchtdruk in hectopascal, regenmeter = neerslag in millimeter, anemometer = wind.",
        "1 millimeter neerslag is 1 liter per vierkante meter.",
        "Een westenwind komt uit het westen. Windkracht 0 tot 12 op de schaal van Beaufort.",
        "Hoge druk: lucht zakt, rustig en droog. Lage druk of depressie: lucht stijgt, wolken en regen.",
        "Een klimatogram toont temperatuur (lijn) en neerslag (staafjes) per maand.",
        "Extreem weer wijkt sterk af van het gewone. Verharding vergroot de kans op wateroverlast.",
        "Storm vanaf windkracht 9. Een orkaan ontstaat boven warm zeewater en heeft een oog.",
        "Een tornado is smal en komt uit een onweersbui; een stormvloed stuwt zeewater tegen de kust.",
        "Code oranje betekent: er wordt gevaarlijk weer verwacht.",
    ],
)

# ───────────────────────────────────────── 7. Het klimaat verandert
BUNDELS["het-klimaat-verandert"] = dict(
    vak=VAK, niveau=SPARK, titel="Het klimaat verandert",
    onder="Fossiele brandstoffen en het broeikaseffect, wat er in ons landschap verandert, en wat eraan te doen is.",
    secties=[
        dict(kop="Fossiele brandstoffen en broeikasgassen", blokken=[
            ("p", "Steenkool, aardolie en aardgas krijgen samen één naam: <strong>fossiele brandstoffen</strong>. "
                  "Ze zijn ontstaan uit resten van planten en dieren van miljoenen jaren geleden. Daarom raken ze "
                  "op: er wordt er veel sneller van verbruikt dan er bij komt."),
            ("p", "Verbrand je fossiele brandstoffen, dan komt er <strong>koolstofdioxide</strong> vrij. Dat is "
                  "een <strong>broeikasgas</strong>, en het draagt het meest bij aan het versterkt "
                  "broeikaseffect. Andere broeikasgassen zijn <strong>methaan</strong> en "
                  "<strong>waterdamp</strong>. Het methaan komt vooral uit <strong>veeteelt, rijstvelden en "
                  "stortplaatsen</strong>."),
            ("p", "De laag gassen rond de aarde waarin het weer zich afspeelt, heet de "
                  "<strong>atmosfeer</strong> of dampkring."),
        ]),
        dict(kop="Het broeikaseffect", blokken=[
            ("fig", svg.broeikas(), "De zon warmt de aarde op. De aarde straalt die warmte terug. De "
                                    "broeikasgassen houden een deel ervan vast."),
            ("p", "Het <strong>broeikaseffect</strong> is dus niet iets slechts: zonder broeikaseffect zou het "
                  "op aarde gemiddeld <strong>ver onder nul</strong> zijn, en zou er hier niets leven. Het "
                  "bestond ook al lang voor er mensen waren."),
            ("p", "Het probleem is het <strong>versterkt</strong> broeikaseffect: er zitten "
                  "<strong>meer</strong> broeikasgassen in de lucht dan vroeger, dus ontsnapt er minder warmte "
                  "en wordt het warmer. Dat komt door wat wij doen: rijden met een benzine- of dieselwagen, "
                  "verwarmen met aardgas of stookolie, en bossen kappen en verbranden."),
            ("kader", "Bossen en oceanen heten <strong>koolstofputten</strong> omdat ze koolstofdioxide "
                      "<strong>uit</strong> de lucht opnemen. Kap je een bos, dan verlies je dus twee keer: de "
                      "koolstof die erin zat komt vrij, en de put die hem opnam verdwijnt."),
            ("p", "<strong>Hernieuwbare</strong> energiebronnen raken niet op: <strong>wind</strong>, "
                  "<strong>zon</strong> en <strong>waterkracht</strong>. Een windmolen stoot tijdens het "
                  "draaien geen koolstofdioxide uit, want er wordt <strong>niets verbrand</strong> om stroom te "
                  "maken. En een goed <strong>geïsoleerd</strong> huis helpt omdat er minder gestookt moet "
                  "worden."),
            ("weetje", "Het klimaat van de aarde is in het verleden wél al veranderd, ook zonder mensen. "
                       "Wetenschappers weten hoe warm het duizenden jaren geleden was uit "
                       "<strong>luchtbelletjes in diepe ijslagen</strong>: die belletjes zijn stukjes lucht van "
                       "toen. Wat nu anders is, is de snelheid."),
            ("p", "Verwar klimaatverandering niet met het weer van vandaag. Eén koude week zegt niets over het "
                  "klimaat, net zoals één warme dag niets bewijst. Klimaat gaat over gemiddelden over jaren."),
        ]),
        dict(kop="Wat er verandert", blokken=[
            ("p", "De gletsjers in de Alpen worden elk jaar korter: een gevolg van de "
                  "<strong>opwarming</strong> van het klimaat. De <strong>zeespiegel</strong> stijgt om drie "
                  "redenen tegelijk: water <strong>zet uit</strong> als het warmer wordt, <strong>ijs op het "
                  "land</strong> smelt en loopt naar zee, en de gletsjers in de bergen worden kleiner."),
            ("kader", "Smelt het <strong>drijvende</strong> zee-ijs rond de noordpool, dan stijgt de zeespiegel "
                      "daardoor <strong>niet</strong> sterk. Drijvend ijs verplaatst al evenveel water als het "
                      "zelf weegt. Alleen ijs dat op <strong>land</strong> ligt, voegt water toe."),
            ("p", "Voor België is zeespiegelstijging een probleem omdat de <strong>polders</strong> achter de "
                  "kust heel <strong>laag</strong> liggen. Een muur of dam die het land tegen het water "
                  "beschermt, heet een <strong>dijk</strong>."),
            ("fig", svg.kustdoorsnede(), "De polder ligt lager dan de zee. Het duin en de dijk houden het water "
                                          "tegen; stijgt de zee, dan moet die bescherming mee omhoog."),
            ("p", "In België merkt men <strong>drogere zomers</strong> met lage waterstanden, "
                  "<strong>hevigere buien</strong> die wateroverlast geven, en <strong>meer hittegolven</strong> "
                  "dan vroeger. Plant- en diersoorten schuiven op naar het noorden, omdat hun leefgebied "
                  "meeschuift met de warmte."),
            ("p", "Neemt de droogte toe, dan vallen beken droog en verandert de vegetatie. Wordt vruchtbaar land "
                  "stilaan woestijn, dan heet dat <strong>verwoestijning</strong>. Mensen die hun streek moeten "
                  "verlaten door aanhoudende droogte of door overstroming, noemt men "
                  "<strong>klimaatvluchtelingen</strong>. Een <strong>koraalrif</strong> is gevoelig voor "
                  "opwarming omdat warm water het koraal doet <strong>verbleken</strong> en afsterven."),
            ("p", "Klimaatverandering treft niet alle landen even hard. Landen met veel laagliggende kust of met "
                  "een al droog klimaat krijgen de zwaarste klappen, en dat zijn vaak niet de landen die het "
                  "meest uitstoten."),
        ]),
        dict(kop="Wat eraan te doen is", blokken=[
            ("p", "De <strong>uitstoot</strong> verminderen betekent: <strong>minder broeikasgassen in de lucht "
                  "brengen</strong>. Dat kan door woningen beter te <strong>isoleren</strong>, door stroom op te "
                  "wekken met <strong>wind en zon</strong>, en door vaker de <strong>trein of de fiets</strong> "
                  "te nemen. Meer <strong>bomen planten</strong> helpt ook, want bomen nemen koolstofdioxide op."),
            ("p", "Naast minder uitstoten is er ook <strong>adaptatie</strong>: je aanpassen aan een klimaat dat "
                  "al veranderd is. <strong>Ontharding</strong> is daar een voorbeeld van: verharding wegnemen "
                  "zodat water in de grond kan. Dat is meteen nuttig tegen hitte, want in een stad is het op een "
                  "zomerse dag warmer dan op het platteland eromheen: <strong>steen en asfalt houden de warmte "
                  "langer vast</strong>."),
            ("kader", "Klimaatverandering wordt een probleem genoemd dat geen land alleen oplost, omdat de "
                      "<strong>dampkring van de hele wereld gedeeld is</strong>. Wat in het ene land de lucht in "
                      "gaat, waait niet netjes binnen die grenzen. En wat je zelf doet telt wel degelijk mee: "
                      "de uitstoot van de hele wereld is niets anders dan de optelsom van alle gezinnen, "
                      "bedrijven en landen samen."),
            ("p", "Waarom helpt ontbossing in het Amazonegebied ons hier? Omdat dat bos veel koolstofdioxide "
                  "opneemt. Verdwijnt het, dan blijft er hier ook meer in de lucht hangen."),
        ]),
    ],
    onthoud=[
        "Fossiele brandstoffen: steenkool, aardolie, aardgas. Ze raken op en geven bij verbranding CO2.",
        "Broeikasgassen: koolstofdioxide, methaan, waterdamp. Methaan komt uit veeteelt, rijst en stortplaatsen.",
        "Het broeikaseffect houdt warmte vast; zonder dat effect zou het hier ver onder nul zijn.",
        "Versterkt broeikaseffect = meer broeikasgassen dan vroeger, dus minder warmte die ontsnapt.",
        "Bossen en oceanen zijn koolstofputten: ze nemen CO2 op.",
        "Hernieuwbaar: wind, zon, waterkracht. Er wordt niets verbrand, dus geen CO2 tijdens het opwekken.",
        "De zeespiegel stijgt doordat water uitzet én doordat ijs op het LAND smelt; drijvend zee-ijs telt niet.",
        "In België: drogere zomers, hevigere buien, meer hittegolven. Soorten schuiven op naar het noorden.",
        "Verwoestijning, klimaatvluchtelingen en koraalverbleking zijn gevolgen elders.",
        "Minder uitstoten (isoleren, wind en zon, trein en fiets) én adaptatie, zoals ontharding.",
    ],
)

# ───────────────────────────────────────── 8. De mens verandert het landschap
BUNDELS["de-mens-verandert-het-landschap"] = dict(
    vak=VAK, niveau=SPARK, titel="De mens verandert het landschap",
    onder="Infrastructuur, bebouwing, ontginning en landbouw, en wat verharding en ontharding met een gebied doen.",
    secties=[
        dict(kop="Infrastructuur", blokken=[
            ("p", "Staan er op een luchtfoto van vijftig jaar geleden velden en op de foto van vandaag huizen en "
                  "een rondweg, dan heeft <strong>de mens het landschap veranderd</strong>. Het aanleggen van "
                  "wegen, spoorlijnen, kanalen en leidingen heet samen het uitbouwen van "
                  "<strong>infrastructuur</strong>."),
            ("fig", tabel(["soort infrastructuur", "voorbeelden"], [
                ["<strong>transportinfrastructuur</strong>", "een autosnelweg aanleggen, een kanaal graven, een spoorlijn verdubbelen"],
                ["<strong>energie-infrastructuur</strong>", "een windmolenpark, een hoogspanningslijn, een elektriciteitscentrale"],
            ]), "De masten en kabels die stroom over lange afstanden vervoeren, vormen samen het "
                "<strong>hoogspanningsnet</strong>."),
            ("p", "<strong>Windmolens</strong> staan vaak aan de kust of op open vlakten, omdat het daar harder "
                  "en gelijkmatiger waait. Een <strong>autosnelweg</strong> door een natuurgebied snijdt het "
                  "leefgebied van dieren in stukken: wat vroeger één gebied was, zijn dan twee gebieden met een "
                  "barrière ertussen."),
            ("p", "Bij een nieuwe <strong>luchthaven</strong> krijgen de omwonenden <strong>geluidshinder</strong> "
                  "van opstijgende vliegtuigen. En <strong>industriegebieden</strong> liggen vaak langs een "
                  "kanaal omdat zware goederen over water goedkoop vervoerd worden."),
            ("fig", svg.haven(), "Een zeehaven: schepen, kranen, kaaien en opslag. Alles ligt er om goederen vlot "
                                  "van het water naar het land te krijgen, en omgekeerd."),
        ]),
        dict(kop="Bebouwing en ontginning", blokken=[
            ("p", "Een <strong>verkaveling</strong> is een stuk grond dat in bouwpercelen verdeeld wordt. De "
                  "oppervlakte bebouwing in België neemt toe terwijl de bevolking maar traag groeit, omdat er "
                  "<strong>steeds meer en kleinere gezinnen</strong> zijn: meer gezinnen betekent meer woningen, "
                  "ook bij evenveel mensen."),
            ("fig", svg.stadsplan(), "Een stad van bovenaf: een oude kern, een ring eromheen, woonwijken, en "
                                     "bedrijven aan de rand bij de grote wegen."),
            ("p", "De oudste dorpskernen van Vlaanderen liggen vaak op een <strong>lichte hoogte</strong>, "
                  "omdat het daar <strong>droger</strong> was dan in de vallei. Wie kon kiezen, bouwde niet met "
                  "zijn voeten in het water."),
            ("p", "<strong>Mijnbouw</strong> is delfstoffen uit de <strong>diepere</strong> ondergrond halen. De "
                  "kunstmatige heuvel van afvalgesteente naast een oude steenkoolmijn heet een "
                  "<strong>terril</strong>. Een <strong>groeve</strong> verandert het landschap doordat er een "
                  "<strong>diepe put</strong> ontstaat waar eerst grond lag. <strong>Ontginning van "
                  "hulpbronnen</strong> betekent: grondstoffen uit de aarde halen om te gebruiken."),
            ("p", "Ook <strong>toerisme</strong> tekent een landschap: appartementsgebouwen op de zeedijk, "
                  "skiliften op een berghelling, een pretpark met parkings errond. Aan de Belgische kust staat "
                  "bijna de hele zeedijk vol met <strong>hoogbouw</strong>."),
            ("kader", "Legt een gemeente een bedrijventerrein aan op oud landbouwgebied, dan veranderen twee "
                      "lagen tegelijk: het <strong>landgebruik</strong> en de <strong>bebouwing</strong>. Dat is "
                      "de handigste manier om zo'n ingreep te beschrijven: welke lagen gaan eraan?"),
        ]),
        dict(kop="Landbouw, bos en water", blokken=[
            ("p", "Verdwijnt er in een streek jaar na jaar een stuk bos voor akkers en wegen, dan heet dat "
                  "<strong>ontbossing</strong>. Op een helling heeft dat drie gevolgen tegelijk: de bodem "
                  "<strong>spoelt sneller weg</strong>, er wordt <strong>minder koolstofdioxide</strong> "
                  "opgenomen, en <strong>dieren verliezen hun leefgebied</strong>."),
            ("p", "Landbouwpercelen worden steeds <strong>groter</strong> gemaakt omdat grote machines er "
                  "efficiënter kunnen werken. Door percelen samen te voegen verdwijnen ook de "
                  "<strong>hagen en houtkanten</strong> ertussen, en net die waren schuilplaats voor vogels en "
                  "insecten."),
            ("p", "<strong>Irrigatie</strong> is land kunstmatig van water voorzien. Dat kan nadelen hebben: de "
                  "rivier of het <strong>grondwater</strong> raakt uitgeput, de bodem kan "
                  "<strong>verzilten</strong>, en verderop blijft er minder water over voor wie daar woont."),
            ("p", "<strong>Stadslandbouw</strong> is voedsel telen in of vlak bij de stad. Dat scheelt transport, "
                  "en het kan een stad <strong>koeler</strong> maken tijdens een hittegolf, want groen verdampt "
                  "water en beton niet."),
        ]),
        dict(kop="Verharding en ontharding", blokken=[
            ("p", "Het bedekken van grond met beton, asfalt of tegels heet <strong>verharding</strong>. "
                  "Landbouwgebied omzetten in bebouwing is daar een vorm van. "
                  "<strong>Ontharding</strong> is het omgekeerde: beton of tegels weghalen zodat de grond weer "
                  "open ligt. Verharding <strong>sluit</strong> de bodem af, ontharding <strong>opent</strong> "
                  "hem weer."),
            ("p", "Breekt een gemeente een betonnen schoolplein op en legt ze er gras en bomen aan, dan levert "
                  "dat drie dingen op: regenwater kan weer in de grond zakken, het is er op warme dagen koeler, "
                  "en er is meer plaats voor planten en dieren."),
            ("p", "Legt een bedrijf een <strong>wadi</strong> aan, een ondiepe kom waar regenwater in kan "
                  "zakken, dan valt dat vooral onder <strong>Planet</strong> van het 5P-model. En geeft een "
                  "nieuwe fabriek werk aan driehonderd mensen maar vervuilt ze de beek ernaast, dan doet ze "
                  "<strong>Prosperity vooruitgaan en Planet achteruit</strong>. Dat mag je gerust zo zeggen: "
                  "het model is er net om zo'n afweging zichtbaar te maken."),
            ("kader", "Twee dingen die vaak fout gezegd worden. Ten eerste: een menselijke ingreep heeft niet "
                      "<strong>enkel</strong> nadelen — een spoorlijn brengt ook werk en verplaatsing. Ten "
                      "tweede: een veranderd landschap kan wél hersteld worden, denk aan een oude groeve die een "
                      "natuurgebied wordt of een rechtgetrokken beek die weer mag kronkelen. Het duurt alleen "
                      "langer dan het afbreken."),
            ("p", "En de gevolgen stoppen niet aan de grens. Ontbossing in het <strong>Amazonegebied</strong> "
                  "raakt de hele wereld omdat dat bos veel koolstofdioxide opneemt, en wat wij hier invoeren, "
                  "wordt elders geteeld of gedolven."),
        ]),
    ],
    onthoud=[
        "Infrastructuur = wegen, spoorlijnen, kanalen en leidingen aanleggen.",
        "Energie-infrastructuur: windmolenpark, hoogspanningslijn, elektriciteitscentrale. Samen het hoogspanningsnet.",
        "Een verkaveling is grond die in bouwpercelen verdeeld wordt.",
        "Mijnbouw haalt delfstoffen uit de diepere ondergrond; de afvalheuvel ernaast is een terril.",
        "Oude dorpskernen liggen op een lichte hoogte, want daar was het droger.",
        "Ontbossing: de bodem spoelt weg, er wordt minder CO2 opgenomen, dieren verliezen hun leefgebied.",
        "Grotere percelen betekenen minder hagen en houtkanten.",
        "Irrigatie put grondwater uit, kan de bodem doen verzilten en laat verderop minder water over.",
        "Verharding sluit de bodem af, ontharding opent hem weer. Een wadi laat regenwater insijpelen.",
        "Een ingreep heeft zelden alleen nadelen, en een veranderd landschap kan hersteld worden.",
    ],
)

# ───────────────────────────────────────── 9. Onderzoeken met kaartlagen
BUNDELS["onderzoeken-met-kaartlagen"] = dict(
    vak=VAK, niveau=SPARK, titel="Onderzoeken met kaartlagen",
    onder="Werken in een kaartviewer, en hoe een geografisch onderzoek van vraag tot besluit verloopt.",
    secties=[
        dict(kop="Kaartlagen en de viewer", blokken=[
            ("p", "Wil je weten of er vroeger een beek liep waar nu een straat ligt, dan helpt het meest: "
                  "<strong>kaarten van dat gebied naast elkaar leggen</strong>. Een oude kaart, een nieuwe, een "
                  "luchtfoto van vroeger en een van vandaag."),
            ("p", "Een <strong>kaartlaag</strong> is <strong>één soort gegevens</strong> die je over de kaart "
                  "legt: de waterlopen, de bebouwing, de bodem, de hoogte. Een programma waarin je die lagen "
                  "kan bekijken, stapelen en meten, heet een <strong>GIS-viewer</strong>. "
                  "<strong>Geopunt</strong> is er zo een, met geografische informatie over Vlaanderen."),
            ("fig", svg.kaartlagen(), "Elke laag toont iets anders. Je zet ze aan of uit in het "
                                      "<strong>lagenpaneel</strong>, en wat op twee lagen samenvalt, valt "
                                      "meteen op."),
            ("fig", tabel(["gereedschap in de viewer", "waarvoor"], [
                ["de <strong>zoekbalk</strong>", "een adres vinden, coördinaten ingeven, naar een gemeente springen"],
                ["het <strong>lagenpaneel</strong>", "lagen aan- en uitzetten en op elkaar stapelen"],
                ["de <strong>transparantie</strong>", "een laag doorzichtig maken om te zien wat eronder ligt"],
                ["het <strong>meetgereedschap</strong>", "een afstand, een oppervlakte of de lengte van een weg meten"],
                ["de <strong>legende</strong>", "weten wat de kleuren van een laag betekenen"],
            ]), "Met het meetgereedschap heb je geen meetlat meer nodig: de viewer kent de schaal zelf."),
            ("p", "Zoeken met <strong>coördinaten</strong> in plaats van met een adres is handig als het gebied "
                  "<strong>geen adres heeft</strong>, bijvoorbeeld midden in een bos of op een akker."),
        ]),
        dict(kop="Lagen combineren", blokken=[
            ("p", "De kracht zit in het <strong>combineren</strong>. Zet je de laag met de waterlopen aan én de "
                  "laag met de bebouwing, dan kan je onderzoeken <strong>of er gebouwd is vlak bij het "
                  "water</strong>. Van een <strong>hoogtelaag</strong> lees je af hoe hoog een plaats boven de "
                  "zeespiegel ligt."),
            ("p", "Een kaartportaal zoals Geopunt bevat <strong>kaarten</strong>, "
                  "<strong>luchtfoto's</strong> en <strong>satellietbeelden</strong>. Een satellietbeeld toont "
                  "je iets wat op een gewone kaart niet staat: <strong>hoe het gebied er in werkelijkheid "
                  "uitziet</strong>. Twee luchtfoto's van verschillende jaren naast elkaar leggen, heet "
                  "beelden <strong>vergelijken</strong>."),
            ("kader", "Kijk bij elke laag <strong>van wanneer ze dateert</strong>. Een luchtfoto in een viewer "
                      "is niet automatisch van vandaag, en het landschap kan intussen veranderd zijn. Twee lagen "
                      "over elkaar leggen mág wel als ze niet even oud zijn — dat is net hoe je verandering "
                      "ziet — maar je moet het wéten."),
        ]),
        dict(kop="Een geografisch onderzoek in vier stappen", blokken=[
            ("p", "Wil je met kaarten uitzoeken waarom een bepaalde straat elk jaar onder water loopt, dan begin "
                  "je met een duidelijke <strong>onderzoeksvraag</strong>. Daarna pas kies je je lagen."),
            ("fig", tabel(["stap", "wat je doet"], [
                ["1. <strong>de vraag stellen</strong>", "één duidelijke onderzoeksvraag, en eventueel een hypothese"],
                ["2. <strong>lagen kiezen</strong>", "welke bronnen kunnen die vraag beantwoorden?"],
                ["3. <strong>analyseren</strong>", "bekijken wat de kaartlagen samen tonen"],
                ["4. <strong>besluiten</strong>", "het antwoord opschrijven, met waarop je je baseert"],
            ]), "Vraag, lagen, analyse, besluit. In die volgorde, want anders zoek je naar iets wat je nog niet "
                "gevraagd hebt."),
            ("p", "Een goede <strong>onderzoeksvraag</strong> is zo nauwkeurig mogelijk geformuleerd, gaat over "
                  "een <strong>afgebakend gebied</strong>, en is met de gekozen bronnen te beantwoorden. Het "
                  "gebied dat je bekijkt heet het <strong>onderzoeksgebied</strong>. Goede vragen zijn "
                  "bijvoorbeeld: ligt de wijk die onderloopt lager dan de rest? Is er sinds 1990 meer verhard in "
                  "deze gemeente? Liggen de boomgaarden op de leembodem?"),
            ("p", "Een <strong>hypothese</strong> is een <strong>verwacht antwoord dat je nog moet "
                  "nakijken</strong>: een vermoeden dat je vooraf opschrijft en daarna toetst. Wordt je "
                  "hypothese weerlegd, dan is je onderzoek daarom <strong>niet</strong> waardeloos — integendeel, "
                  "je weet nu iets wat je daarvoor niet wist. Je schrijft gewoon op wat je wél ziet en trekt "
                  "daaruit je besluit."),
            ("fig", tabel(["als je hypothese is …", "zet je deze laag of lagen aan"], [
                ["de overstroomde straat ligt lager dan de omgeving", "de <strong>hoogtelaag</strong>"],
                ["boomgaarden liggen vooral op leemgrond", "de <strong>bodemkaart</strong> én het <strong>landgebruik</strong>"],
                ["er is sinds 1990 meer verhard", "twee <strong>luchtfoto's</strong> van verschillende jaren"],
            ]), "Twee luchtfoto's van verschillende jaren zijn nodig omdat je dan de <strong>verandering</strong> "
                "ziet en niet alleen de toestand van vandaag."),
            ("kader", "Twee patronen die op de kaart samenvallen, <strong>bewijzen niet</strong> dat het ene het "
                      "andere veroorzaakt. Ze kunnen allebei door iets derds komen, of toevallig samenvallen. "
                      "Samenvallen is een aanwijzing, geen bewijs."),
            ("p", "In het <strong>besluit</strong> staan drie dingen: een antwoord op de onderzoeksvraag, waarop "
                  "je dat antwoord baseert, en of je hypothese klopte of niet. Vermeld altijd welke "
                  "<strong>bronnen</strong> je gebruikt hebt. Zie je dat een wijk die onderloopt in een oude "
                  "<strong>beekvallei</strong> ligt, dan is het beste besluit: de wijk ligt op een plek waar het "
                  "water van nature samenkomt."),
            ("p", "Meer lagen tegelijk aanzetten maakt je onderzoek <strong>niet</strong> beter: het maakt de "
                  "kaart onleesbaar. Kies de lagen die bij je vraag horen. En soms volstaat een kaartonderzoek "
                  "niet en moet je toch <strong>ter plaatse</strong> gaan kijken, want niet alles komt op een "
                  "kaart terecht."),
            ("weetje", "Meet je met het meetgereedschap dat een perceel <strong>0,8 hectare</strong> groot is, "
                       "dan is dat <strong>8000 vierkante meter</strong>: één hectare is 10 000 vierkante meter."),
        ]),
    ],
    onthoud=[
        "Een kaartlaag is één soort gegevens die je over de kaart legt; je zet ze aan in het lagenpaneel.",
        "Geopunt is een GIS-viewer met geografische informatie over Vlaanderen.",
        "Zoekbalk, lagenpaneel, transparantie, meetgereedschap en legende zijn je gereedschap.",
        "Een viewer meet zelf afstanden en oppervlaktes; een meetlat heb je niet nodig.",
        "Kijk altijd van wanneer een laag of luchtfoto dateert.",
        "Een onderzoek verloopt in vier stappen: vraag stellen, lagen kiezen, analyseren, besluiten.",
        "Een hypothese is een verwacht antwoord dat je nog moet nakijken. Weerlegd is niet waardeloos.",
        "Samenvallen op de kaart is een aanwijzing, geen bewijs van oorzaak en gevolg.",
        "In het besluit: het antwoord, waarop je het baseert, en of je hypothese klopte. Noem je bronnen.",
        "Eén hectare is 10 000 vierkante meter, dus 0,8 hectare is 8000 vierkante meter.",
    ],
)

# ───────────────────────────────────────── 10. Het landschap op het terrein
BUNDELS["het-landschap-op-het-terrein"] = dict(
    vak=VAK, niveau=SPARK, titel="Het landschap op het terrein",
    onder="Lokaliseren en oriënteren, het reliëf, de vegetatie en het landgebruik beschrijven, en de bodem onderzoeken.",
    secties=[
        dict(kop="Lokaliseren en oriënteren", blokken=[
            ("p", "Ga je met de klas een stuk landschap onderzoeken, dan doe je ter plaatse eerst één ding: "
                  "<strong>vaststellen waar je precies staat</strong>. Dat heet <strong>lokaliseren</strong>. "
                  "Daarvoor gebruik je een <strong>satellietnavigatiesysteem</strong>, een <strong>kaart</strong> "
                  "van het gebied en de <strong>coördinaten</strong> van het punt."),
            ("kader", "<strong>Lokaliseren</strong> en <strong>oriënteren</strong> zijn twee verschillende "
                      "dingen. Lokaliseren is <em>waar sta ik</em>, oriënteren is <em>welke kant kijk ik uit</em>. "
                      "Je hebt ze allebei nodig, en in die volgorde."),
            ("p", "Je kaart in de juiste richting leggen doe je zo: je <strong>draait de kaart tot de noordpijl "
                  "naar het noorden wijst</strong>. Dan komt alles op de kaart overeen met wat je voor je ziet. "
                  "Je kan je ook oriënteren aan een <strong>landschapselement</strong>: een kerktoren, een "
                  "watertoren, een lange bomenrij. Rond de middag staat de zon bij ons in het "
                  "<strong>zuiden</strong>."),
            ("p", "Twee dingen om op te letten. Een <strong>kompas</strong> werkt <strong>niet</strong> "
                  "betrouwbaar vlak naast een ijzeren hek of een auto: metaal trekt de naald scheef. En een "
                  "<strong>satellietnavigatiesysteem</strong> werkt niet overal even goed; in een gebouw of "
                  "onder dicht bladerdek verliest het de satellieten uit het oog."),
            ("p", "Wat neem je mee? Een <strong>kompas</strong>, een <strong>kaart</strong> van het gebied en "
                  "een <strong>schepje</strong> om de bodem te bekijken. Noteer ook het "
                  "<strong>tijdstip</strong> van je waarnemingen, want het landschap ligt er per seizoen en per "
                  "uur anders bij."),
        ]),
        dict(kop="Het reliëf beschrijven", blokken=[
            ("p", "Beschrijf je het <strong>reliëf</strong> van je onderzoeksgebied, dan noteer je de "
                  "<strong>helling</strong> van het terrein, de <strong>hoogteverschillen</strong> die je ziet, "
                  "en waar de <strong>horizonlijn</strong> ligt. Het verschil tussen het laagste en het hoogste "
                  "punt van je gebied heet het <strong>hoogteverschil</strong>."),
            ("p", "Sta je onderaan een helling, dan merk je dat de horizonlijn <strong>dichtbij</strong> ligt: "
                  "de helling neemt je zicht weg. Bovenop kijk je veel verder. En dat een helling steil is, stel "
                  "je vast aan je eigen benen: <strong>je moet zwaarder stappen om te klimmen</strong>."),
            ("fig", svg.transect(), "Een <strong>transect</strong> of doorsnede is een tekening van het terrein "
                                    "zoals je het van opzij zou zien. Je tekent wat je ziet, van links naar "
                                    "rechts, met de hoogte erbij."),
            ("p", "Maak op het terrein ook een <strong>schets</strong>, niet alleen een foto. Op een schets kies "
                  "je <strong>zelf wat belangrijk is</strong>: je laat weg wat niet ter zake doet en zet groot "
                  "wat wel telt. Een foto neemt alles even hard mee."),
            ("p", "Beschrijf je het landschap ten opzichte van een kerktoren, noteer dan "
                  "<strong>in welke richting en hoe ver</strong> hij ligt. Dat is relatief situeren, en zonder "
                  "richting én afstand zegt het weinig."),
        ]),
        dict(kop="Vegetatie, bebouwing en landgebruik", blokken=[
            ("p", "Sta je in je onderzoeksgebied en beschrijf je wat er groeit, wat er gebouwd staat en waar de "
                  "grond voor dient, dan beschrijf je de <strong>vegetatie, de bebouwing en het "
                  "landgebruik</strong>."),
            ("fig", tabel(["wat je bekijkt", "wat je noteert"], [
                ["<strong>vegetatie</strong>", "of er bomen, struiken of gras staan; loofbomen of naaldbomen; hoe dicht de begroeiing staat"],
                ["<strong>bebouwing</strong>", "wat voor gebouwen, hoeveel, hoe dicht bij elkaar"],
                ["<strong>landgebruik</strong>", "landbouw, wonen, industrie, recreatie, natuur"],
            ]), "Aan de bebouwing zie je vaak meteen hoe de grond gebruikt wordt: loodsen en parkings horen bij "
                "industrie, een rij huizen bij wonen."),
            ("p", "Zie je midden in een weide een rij <strong>knotwilgen</strong> langs een gracht, dan is dat "
                  "een <strong>landschapselement dat door de mens is aangeplant</strong>. Knotwilgen groeien niet "
                  "zomaar in een rij: iemand heeft ze gezet en ze jarenlang geknot."),
        ]),
        dict(kop="De bodem onderzoeken", blokken=[
            ("p", "Om de bodem te bekijken graaf je een klein <strong>kuiltje</strong>, zodat je de lagen onder "
                  "elkaar ziet zitten."),
            ("fig", svg.bodemprofiel(), "De lagen verschillen in kleur en in textuur. De bovenste laag is "
                                        "meestal donkerder dan de laag eronder, door de plantenresten erin."),
            ("p", "Je onderzoekt drie dingen: de <strong>textuur</strong> van de bodem, de <strong>kleur</strong> "
                  "van de lagen en hoe <strong>vochtig</strong> de bodem is. De kleur is nuttig omdat ze iets "
                  "zegt over het <strong>vocht en de humus</strong>: donker betekent veel plantenresten, grijzig "
                  "en gevlekt betekent nat."),
            ("fig", tabel(["proefje", "wat je voelt of ziet", "welk los gesteente"], [
                ["tussen je vingers wrijven", "het <strong>knerpt</strong> duidelijk", "<strong>zand</strong>"],
                ["tussen je vingers wrijven", "zacht en <strong>melig</strong>, bijna als bloem", "<strong>leem</strong>"],
                ["tot een dun draadje rollen", "het draadje <strong>blijft heel</strong>", "<strong>klei</strong>"],
                ["gewoon kijken", "<strong>korrels die je met het blote oog ziet liggen</strong>", "<strong>grind</strong>"],
            ]), "Een tabel waarmee je stap voor stap bepaalt met welk gesteente je te maken hebt, heet een "
                "<strong>determineertabel</strong>."),
            ("p", "Vind je in een weide een natte, grijzige bodem met <strong>riet</strong> errond, dan besluit "
                  "je: het <strong>grondwater staat hier hoog</strong>. Riet groeit niet op droge grond, en die "
                  "grijzige kleur krijgt een bodem door langdurige natheid."),
            ("kader", "Wie een terreinonderzoek doet, mag <strong>niet zomaar overal</strong> een put graven. "
                      "Vraag toestemming aan wie de grond beheert, en leg het kuiltje daarna weer dicht."),
        ]),
        dict(kop="Van waarneming naar verslag", blokken=[
            ("p", "Achteraf vergelijk je je waarnemingen met een <strong>kaart</strong>, om na te gaan of wat je "
                  "zag overeenkomt met wat de kaart toont. Klopt het niet, dan is dat op zich al een vondst: "
                  "misschien is de kaart ouder dan het landschap."),
            ("p", "In een <strong>verslag</strong> van een terreinonderzoek staat: <strong>waar en wanneer</strong> "
                  "je gekeken hebt, <strong>wat</strong> je waargenomen hebt, en welk <strong>besluit</strong> je "
                  "eruit trekt."),
            ("p", "Je kan een landschap <strong>niet</strong> volledig beschrijven zonder ooit ter plaatse te "
                  "gaan. Kleur, geur, geluid, hoe zwaar een helling stapt: dat staat op geen enkele kaart. "
                  "Daarom is je <strong>eigen leefomgeving</strong> een goed onderzoeksgebied om mee te "
                  "beginnen: je komt er vaak en je ziet de veranderingen zelf."),
            ("p", "De manieren om ter plaatse in het landschap te werken, noemt men samen "
                  "<strong>terreintechnieken</strong>."),
        ]),
    ],
    onthoud=[
        "Eerst lokaliseren (waar sta ik), dan oriënteren (welke kant kijk ik uit).",
        "Kaart oriënteren: draai de kaart tot de noordpijl naar het noorden wijst.",
        "Een kompas werkt niet naast metaal; satellietnavigatie werkt slecht binnen en onder dicht bladerdek.",
        "Rond de middag staat de zon bij ons in het zuiden.",
        "Reliëf beschrijven: helling, hoogteverschillen en de horizonlijn.",
        "Een transect of doorsnede is het terrein getekend zoals je het van opzij zou zien.",
        "Op een schets kies je zelf wat belangrijk is; een foto neemt alles even hard mee.",
        "Beschrijf vegetatie, bebouwing en landgebruik; noteer ook het tijdstip.",
        "Bodem: graaf een kuiltje, kijk naar textuur, kleur en vocht. Zand knerpt, leem is melig, klei rolt tot een draadje.",
        "In een verslag: waar en wanneer, wat je zag, en je besluit.",
    ],
)

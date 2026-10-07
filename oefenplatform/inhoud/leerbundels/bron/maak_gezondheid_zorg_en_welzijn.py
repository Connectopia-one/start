# -*- coding: utf-8 -*-
"""De leerbundels voor gezondheid, zorg en welzijn op 🚀 Boost dubbele
finaliteit.

Gebaseerd op de vakfiche 2DU gezondheid, zorg en welzijn, geldig vanaf
1 januari 2027. Zestien thema's: vier over waarnemen en het lichaam, vier over
gezondheid, ziekte en kwaliteit, vier over voeding, en vier over interieur- en
linnenzorg.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Gezondheid, zorg en welzijn"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    BUNDELS[slug + "-boost-dubbele-finaliteit"] = b


# ───────────────────────── 1. Waarnemen: van prikkel tot reactie
zet("waarnemen-van-prikkel-tot-reactie",
    titel="Waarnemen: van prikkel tot reactie",
    onder="De vier stappen van het waarnemingsproces, de vijf zintuigen en de vijf soorten receptoren, het verschil tussen een zenuw en een hormoon, en de huid, de neus en de tong van dichtbij.",
    secties=[
        dict(kop="Het waarnemingsproces", blokken=[
            ("p", "<strong>Een prikkel is een verandering</strong> in of buiten je lichaam die je lichaam kan "
                  "opmerken. Waarnemen verloopt daarna altijd in vier stappen."),
            ("fig", svg.stappen(["prikkel|de verandering", "receptor|vangt op",
                                 "conductor|geeft door", "effector|voert uit"]),
             "De vier stappen van het waarnemingsproces, van de prikkel tot de reactie."),
            ("kader", tabel(["stap", "wat het is"],
                            [["<strong>de prikkel</strong>", "<strong>de verandering</strong> zelf"],
                             ["<strong>de receptor</strong>", "<strong>de cel die de prikkel opvangt</strong> en omzet in een impuls"],
                             ["<strong>de conductor</strong>", "<strong>de zenuw of het hormoon</strong> die de boodschap geleidt: een zenuw elektrisch, een hormoon via het bloed"],
                             ["<strong>de effector</strong>", "<strong>een spier of een klier</strong> die de reactie uitvoert: een spier beweegt, een klier geeft een stof af"]])),
            ("p", "<strong>Een prikkel komt dus niet altijd van buiten het lichaam.</strong> <strong>Dorst, "
                  "honger en pijn in je buik zijn inwendige prikkels</strong>; <strong>lawaai, licht en kou "
                  "zijn uitwendige prikkels.</strong>"),
            ("p", "<strong>Een zenuw werkt sneller dan een hormoon</strong>: een zenuwimpuls is er bijna "
                  "meteen, <strong>een hormoon reist mee met het bloed</strong> en werkt langzamer, maar "
                  "langer en in heel het lichaam."),
            ("p", "<strong>Een endocriene klier geeft haar stof rechtstreeks af aan het bloed</strong>; "
                  "endocrien betekent naar binnen. <strong>Een exocriene klier geeft haar stof af via een "
                  "kanaal</strong>, zoals een zweetklier die zweet op de huid brengt. <strong>Een klier is "
                  "dus een orgaan dat een stof afgeeft</strong>, zoals zweet of speeksel."),
        ]),
        dict(kop="Zintuigen, receptoren en functies", blokken=[
            ("p", "<strong>De mens heeft vijf zintuigen: het oog, het oor, de huid, de neus en de "
                  "tong.</strong> <strong>De tong is dus wel degelijk een zintuig</strong>, het smaakzintuig, "
                  "met smaakknoppen in de papillen. De lever is een orgaan, geen zintuig."),
            ("kader", tabel(["soort receptor", "waarvoor"],
                            [["<strong>mechanoreceptoren</strong>", "druk, aanraking, trilling"],
                             ["<strong>thermoreceptoren</strong>", "<strong>warmte en koude</strong>, want thermo betekent warmte"],
                             ["<strong>chemoreceptoren</strong>", "stoffen: geur en smaak"],
                             ["<strong>fotoreceptoren</strong>", "licht, en die zitten enkel in het oog"],
                             ["<strong>nociceptoren</strong>", "<strong>pijn</strong>, de pijnreceptoren"]])),
            ("p", "Rekenreceptoren bestaan niet. <strong>De vijf functies van het waarnemen zijn de "
                  "functionele, de sociale, de emotionele, de communicatieve en de alarmerende "
                  "functie.</strong> <strong>De alarmerende functie waarschuwt voor gevaar</strong>: je ruikt "
                  "rook of hoort een claxon, en je lichaam reageert voor je erover nadenkt."),
        ]),
        dict(kop="De huid", blokken=[
            ("fig", svg.huidlagen(),
             "De drie lagen van de huid. De zweetklier ligt in de lederhuid en geeft haar zweet af op de "
             "opperhuid."),
            ("p", "<strong>Van buiten naar binnen: de opperhuid, de lederhuid en het onderhuids "
                  "vetweefsel.</strong> <strong>In de lederhuid zitten de zenuwuiteinden, de bloedvaten en de "
                  "klieren</strong>; <strong>in de opperhuid zitten geen bloedvaten</strong>, en daarom bloedt "
                  "een heel lichte schram niet. <strong>Het onderhuids vetweefsel isoleert</strong>: het houdt "
                  "de warmte binnen en vangt stoten op."),
            ("p", "<strong>In de huid zitten pijnreceptoren, mechanoreceptoren en thermoreceptoren</strong>; "
                  "fotoreceptoren zitten in het oog. <strong>De huid beschermt, regelt de warmte en voelt "
                  "aanraking.</strong> Speeksel komt van de speekselklieren in de mond, niet van de huid."),
        ]),
        dict(kop="De neus en de tong", blokken=[
            ("p", "<strong>De reukcellen zitten in het reukslijmvlies</strong>, bovenaan in de neusholte, met "
                  "reukhaartjes in het slijm. <strong>Een geurstof lost eerst op in het slijm</strong>: pas "
                  "dan raakt ze de reukhaartjes en ontstaat er een impuls. <strong>Een reukcel is zelf een "
                  "zenuwcel</strong>: ze vangt de prikkel op en geeft de impuls zelf door naar de hersenen."),
            ("p", "<strong>De smaakknoppen zitten in de papillen</strong>, de kleine bultjes op de tong. "
                  "<strong>De vijf basissmaken zijn zoet, zout, zuur, bitter en umami</strong>; <strong>umami "
                  "is de hartige smaak</strong> van bouillon, kaas of tomaat. Warm is geen smaak maar een "
                  "temperatuur."),
            ("p", "<strong>Je ruikt niet met de smaakknoppen</strong>: ruiken gebeurt met de reukcellen in de "
                  "neus, smaken met de smaakknoppen op de tong. <strong>Toch smaakt eten minder als je "
                  "verkouden bent</strong>, want smaak is grotendeels reuk: zit je neus dicht, dan valt dat "
                  "deel weg."),
        ]),
    ])


# ───────────────────────── 2. Het oog en het oor
zet("het-oog-en-het-oor",
    titel="Het oog en het oor",
    onder="De weg van het licht door het oog, de staafjes en de kegeltjes, de pupilreflex en het dieptezicht, en daarna de drie delen van het oor, decibel en hertz, en waarom gehoorschade blijvend is.",
    secties=[
        dict(kop="Het oog", blokken=[
            ("fig", svg.oogdoorsnede(),
             "Het licht valt eerst op het hoornvlies, gaat door de pupil en de lens, en komt op het netvlies "
             "terecht. De oogzenuw brengt de impuls naar de hersenen."),
            ("kader", tabel(["deel", "wat het doet"],
                            [["<strong>het hoornvlies</strong>", "<strong>waar het licht eerst op valt</strong>: het doorzichtige vliesje vooraan"],
                             ["<strong>de iris</strong>", "<strong>het gekleurde ringetje vooraan</strong> dat de pupil groter of kleiner maakt"],
                             ["<strong>de pupil</strong>", "<strong>de opening in de iris die licht doorlaat</strong>: hoe groter, hoe meer licht"],
                             ["<strong>de lens</strong>", "<strong>ze stelt scherp</strong>: ze buigt het licht zo dat het beeld scherp op het netvlies valt"],
                             ["<strong>het netvlies</strong>", "<strong>de binnenste laag achteraan</strong>, met de staafjes en de kegeltjes"],
                             ["<strong>de oogzenuw</strong>", "<strong>ze brengt de impuls naar de hersenen</strong>: de conductor"]])),
            ("p", "<strong>Het netvlies ligt achteraan, niet vooraan</strong>: vooraan zitten het hoornvlies, "
                  "de iris en de pupil. <strong>Aan de buitenkant van het oog zitten het ooglid, de wimpers en "
                  "de oogspieren.</strong>"),
            ("p", "<strong>De kegeltjes zien kleur, werken bij veel licht en maken het beeld scherp.</strong> "
                  "<strong>De staafjes zien in het donker</strong>: ze zijn gevoelig voor weinig licht, maar "
                  "<strong>ze zien geen kleur</strong>. Daarom zie je in het donker bijna geen kleur meer."),
            ("p", "<strong>Bij fel licht wordt de pupil kleiner</strong>, zodat er minder licht binnenvalt en "
                  "het oog zich beschermt. <strong>Dat is de pupilreflex</strong>, en die loopt via de "
                  "hersenstam, dus zonder dat je het wil."),
            ("p", "<strong>Het beeld staat omgekeerd op het netvlies</strong>, op zijn kop; de hersenen draaien "
                  "het weer recht. <strong>Het gezichtsveld is alles wat je ziet</strong> zonder je ogen te "
                  "bewegen. <strong>Twee ogen heb je nodig voor het dieptezicht</strong>: elk oog ziet een "
                  "iets ander beeld, en daaruit halen de hersenen de afstand. <strong>Met één oog schat je "
                  "afstanden dus minder goed in.</strong>"),
        ]),
        dict(kop="Het oor", blokken=[
            ("fig", svg.oordoorsnede(),
             "Het oor in drie delen. De trilling gaat van het trommelvel over de drie gehoorbeentjes naar het "
             "slakkenhuis, en pas daar wordt ze een impuls."),
            ("p", "<strong>Het oor bestaat uit drie delen: het buitenoor, het middenoor en het "
                  "binnenoor.</strong> <strong>Het buitenoor is de oorschelp met de gehoorgang</strong>; het "
                  "trommelvel sluit die af."),
            ("p", "<strong>Het trommelvel trilt mee</strong> met de geluidsgolven, en die trilling gaat verder "
                  "naar binnen. <strong>Het ligt tussen het buitenoor en het middenoor</strong>, niet in het "
                  "binnenoor."),
            ("p", "<strong>Het middenoor ligt achter het trommelvel, heeft drie gehoorbeentjes en is met de "
                  "keel verbonden.</strong> <strong>De hamer, het aambeeld en de stijgbeugel versterken de "
                  "trilling</strong> en geven ze door aan het binnenoor. <strong>De buis van Eustachius "
                  "verbindt het middenoor met de keel</strong> en houdt de druk aan beide kanten van het "
                  "trommelvel gelijk."),
            ("p", "<strong>Het orgaan van Corti zit in het slakkenhuis</strong> van het binnenoor, ook de "
                  "cochlea genoemd. <strong>Het maakt impulsen</strong>: de haarcellen zetten de trilling om "
                  "in impulsen voor de gehoorzenuw. <strong>Het binnenoor zorgt ook voor je evenwicht</strong>, "
                  "want naast het slakkenhuis liggen daar de halfcirkelvormige kanalen van het "
                  "evenwichtsorgaan."),
        ]),
        dict(kop="Decibel, hertz en je gehoor beschermen", blokken=[
            ("kader", tabel(["eenheid", "wat ze meet"],
                            [["<strong>decibel of dB</strong>", "<strong>de sterkte</strong>: hoe luid een geluid is"],
                             ["<strong>hertz of Hz</strong>", "<strong>de toonhoogte</strong>: het aantal trillingen per seconde, hoe hoger hoe hoger de toon"]])),
            ("p", "<strong>Meer hertz betekent dus geen luider geluid</strong> maar een hogere toon; luidheid "
                  "meet je in decibel. <strong>Een gesprek haalt ongeveer 60 decibel</strong>, en daar gebeurt "
                  "niets mee. <strong>Boven tachtig decibel kan lang luisteren je gehoor beschadigen</strong>, "
                  "en hoe luider het geluid, hoe korter je het veilig verdraagt."),
            ("p", "<strong>Te veel lawaai, muziek te luid zetten en lang in een fabriek werken beschadigen je "
                  "gehoor.</strong> <strong>Gehoorschade is blijvend omdat de haarcellen niet terug "
                  "groeien</strong>: de haarcellen in het orgaan van Corti herstellen niet, en wat weg is, "
                  "blijft weg. <strong>Op een festival beschermen oordopjes je gehoor</strong>: ze dempen het "
                  "geluid zonder dat je de muziek kwijt bent."),
        ]),
    ])


# ───────────────────────── 3. Spieren, beenderen en gewrichten
zet("spieren-beenderen-en-gewrichten",
    titel="Spieren, beenderen en gewrichten",
    onder="De drie spierweefsels en het verschil tussen willekeurig en onwillekeurig, rode en witte vezels, waarom spieren in paren werken, de botten van arm en been, en de delen van een gewricht.",
    secties=[
        dict(kop="Drie soorten spierweefsel", blokken=[
            ("kader", tabel(["spierweefsel", "waar", "willekeurig?"],
                            [["<strong>skeletspierweefsel</strong>", "aan de botten: arm, hand, been", "<strong>willekeurig</strong>: je stuurt ze zelf"],
                             ["<strong>hartspierweefsel</strong>", "het hart", "<strong>onwillekeurig</strong>: het hart klopt zonder dat je het wil"],
                             ["<strong>glad spierweefsel</strong>", "<strong>in de darmwand</strong>, in de bloedvaten en in de blaas", "<strong>onwillekeurig</strong>: je darmen werken door zonder dat je eraan denkt"]])),
            ("p", "Beenweefsel is bot en geen spier. <strong>Een willekeurige spier beweegt omdat jij het "
                  "wil</strong>; <strong>de hartspier is dus geen willekeurige spier</strong>, ze klopt je "
                  "hele leven zonder dat je eraan denkt."),
            ("p", "<strong>Een rode spiervezel houdt lang vol</strong>: ze werkt met zuurstof, denk aan lopen "
                  "over een lange afstand. <strong>Een witte spiervezel werkt kort en fel</strong>: veel "
                  "kracht in korte tijd, maar snel vermoeid."),
        ]),
        dict(kop="Hoe een spier werkt", blokken=[
            ("p", "<strong>Een skeletspier zit met een pees aan een bot vast.</strong> <strong>Een pees "
                  "verbindt een spier met een bot; een ligament verbindt twee botten.</strong> Dat is het "
                  "verschil dat het vaakst verward wordt."),
            ("p", "<strong>Bij de bouw van een skeletspier horen de spierbuik, de spiervezels en de "
                  "pezen.</strong> <strong>Een spiervezel is een spiercel</strong>, een langgerekte cel; veel "
                  "vezels samen vormen de spier."),
            ("p", "<strong>Trekt een spier samen, dan wordt ze korter</strong> en dikker, en trekt ze het bot "
                  "mee. <strong>Een spier kan trekken maar niet duwen</strong>, en daarom <strong>heb je twee "
                  "spieren nodig om een arm te buigen en te strekken</strong>."),
            ("fig", svg.spierpaar(),
             "Links buigt de biceps de arm terwijl de triceps ontspant; rechts strekt de triceps terwijl de "
             "biceps ontspant."),
            ("p", "<strong>De agonist is de spier die de beweging uitvoert, de antagonist doet het "
                  "omgekeerde.</strong> <strong>De antagonist ontspant</strong> terwijl de agonist trekt: "
                  "<strong>trokken ze even hard, dan bewoog er niets.</strong> <strong>De biceps buigt je arm, "
                  "de triceps strekt hem.</strong>"),
            ("p", "<strong>Je hebt spieren nodig om te bewegen, om warmte te maken en om rechtop te "
                  "staan.</strong> Bloed wordt in het beenmerg gemaakt, niet door de spieren. <strong>Een "
                  "spier heeft zuurstof en voeding nodig</strong>: het bloed brengt die aan en voert de "
                  "afvalstoffen af."),
        ]),
        dict(kop="Botten en gewrichten", blokken=[
            ("kader", tabel(["lichaamsdeel", "botten"],
                            [["<strong>de bovenarm</strong>", "<strong>het opperarmbeen</strong>, van de schouder tot de elleboog"],
                             ["<strong>de onderarm</strong>", "<strong>het spaakbeen en de ellepijp</strong>"],
                             ["<strong>het bovenbeen</strong>", "<strong>het dijbeen</strong>, van de heup tot de knie, het langste bot van je lichaam"],
                             ["<strong>het onderbeen</strong>", "<strong>het scheenbeen en het kuitbeen</strong>: het scheenbeen is het dikste, het kuitbeen ligt er dun naast"]])),
            ("p", "<strong>Een scharniergewricht buigt in één richting</strong>, zoals een deur: de elleboog "
                  "en de knie. <strong>Bij een kogelgewricht zit de kop in een kom en draait het alle kanten "
                  "op</strong>: de heup en de schouder. <strong>De knie is dus geen kogelgewricht.</strong> "
                  "<strong>Een kogelgewricht beweegt in meer richtingen dan een scharniergewricht.</strong>"),
            ("kader", tabel(["deel van het gewricht", "wat het doet"],
                            [["<strong>de gewrichtskop en de gewrichtskom</strong>", "de twee botuiteinden die in elkaar passen"],
                             ["<strong>het kraakbeen</strong>", "<strong>het vangt schokken op</strong>: een glad en veerkrachtig laagje op de botuiteinden"],
                             ["<strong>het gewrichtssmeer</strong>", "<strong>het vermindert de wrijving</strong>, zodat de botten soepel over elkaar glijden"],
                             ["<strong>het gewrichtskapsel</strong>", "<strong>het sluit het gewricht af</strong> en houdt het gewrichtssmeer binnen"],
                             ["<strong>de ligamenten of gewrichtsbanden</strong>", "<strong>ze houden de botten samen</strong> en het gewricht stabiel"]])),
        ]),
    ])


# ───────────────────────── 4. Het zenuwstelsel en de reflexen
zet("het-zenuwstelsel-en-de-reflexen",
    titel="Het zenuwstelsel en de reflexen",
    onder="Het centraal en het perifeer zenuwstelsel, wat elk deel van de hersenen doet, de bouw van een neuron, wat er in de synaps gebeurt, en het verschil tussen een reflex en een gewilde beweging.",
    secties=[
        dict(kop="Centraal en perifeer", blokken=[
            ("p", "<strong>Het centraal zenuwstelsel is het ruggenmerg samen met de grote en de kleine "
                  "hersenen.</strong> <strong>Het perifeer zenuwstelsel zijn alle zenuwen buiten de hersenen "
                  "en het ruggenmerg</strong>, en <strong>daar horen ook de hersenzenuwen bij</strong>, niet "
                  "bij het centrale."),
            ("kader", tabel(["deel", "wat het doet"],
                            [["<strong>de grote hersenen</strong>", "<strong>denken, taal en bewust voelen</strong>"],
                             ["<strong>de kleine hersenen</strong>", "<strong>ze regelen het evenwicht</strong> en de vloeiende, geoefende bewegingen"],
                             ["<strong>de hersenstam</strong>", "<strong>wat altijd door moet lopen</strong>: de ademhaling, de hartslag, het slikken"],
                             ["<strong>de hersenbalk</strong>", "<strong>ze verbindt de twee hersenhelften</strong>, de brug tussen links en rechts"]])),
            ("p", "<strong>Een sensibele zenuw brengt informatie binnen</strong>, van de receptor naar het "
                  "centraal zenuwstelsel. <strong>Een motorische zenuw stuurt de spier aan</strong>, van het "
                  "centrum naar de effector. <strong>Een gemengde zenuw doet beide</strong>: ze bevat zowel "
                  "sensibele als motorische vezels."),
        ]),
        dict(kop="Het neuron en de synaps", blokken=[
            ("fig", svg.neuron(),
             "Een zenuwcel. De dendrieten vangen op, het axon geleidt, en de eindknoppen geven door aan de "
             "volgende cel."),
            ("p", "<strong>Een zenuwcel heet ook een neuron</strong>, en <strong>bij haar bouw horen de "
                  "dendrieten, het cellichaam en het axon</strong>. <strong>De dendrieten vangen impulsen "
                  "op</strong> van andere cellen. <strong>Het axon geleidt de impuls</strong> van het "
                  "cellichaam naar de eindknop; <strong>het axon vangt dus niets op</strong>, het voert juist "
                  "weg."),
            ("p", "<strong>De myelineschede versnelt de impuls</strong>: die springt van knoop naar knoop en "
                  "gaat daardoor veel sneller. <strong>De onderbreking in de myelineschede is een knoop van "
                  "Ranvier</strong>, en <strong>de Schwann-cellen maken de myelineschede</strong>: elke cel "
                  "wikkelt zich rond een stuk van het axon."),
            ("p", "<strong>De synaps is de plaats waar twee neuronen de impuls doorgeven.</strong> <strong>Daar "
                  "gaat een stof over</strong>: de eindknop geeft een neurotransmitter af die de kleine spleet "
                  "oversteekt en het volgende neuron prikkelt. <strong>Een impuls springt dus niet "
                  "rechtstreeks over van cel naar cel.</strong>"),
            ("p", "<strong>In het neuron is het elektrisch, in de synaps chemisch, en het is dus een "
                  "samenwerking van de twee.</strong> Het bloed vervoert hormonen, geen impulsen."),
        ]),
        dict(kop="Reflex of gewilde beweging", blokken=[
            ("p", "<strong>Een reflex is een snelle reactie</strong>, een vaste reactie op een prikkel zonder "
                  "dat je beslist. <strong>Je denkt er niet bij na</strong>: de reactie is er al voor je "
                  "gewaarwording bewust wordt. <strong>Een reflex beschermt je lichaam tegen schade</strong>: "
                  "<strong>je trekt je hand van een hete plaat weg vóór je de pijn voelt.</strong>"),
            ("fig", svg.stappen(["receptor", "sensorisch|neuron", "schakel-|neuron",
                                 "motorisch|neuron", "effector"]),
             "De reflexboog: de weg die de impuls bij een reflex aflegt, via het ruggenmerg en niet via de "
             "grote hersenen."),
            ("p", "<strong>De reflexboog is de weg van de impuls</strong>: van de receptor naar het "
                  "sensorische neuron, het schakelneuron, het motorische neuron en de effector. <strong>Een "
                  "schakelneuron verbindt twee neuronen</strong> en ligt in het ruggenmerg tussen het "
                  "sensorische en het motorische neuron."),
            ("p", "<strong>Bij een reflex gaat de impuls dus niet eerst naar de grote hersenen</strong>: de "
                  "reflexboog loopt via het ruggenmerg of de hersenstam, en de hersenen merken het pas daarna. "
                  "<strong>De kniepeesreflex loopt via het ruggenmerg</strong>, en daardoor gaat het veel "
                  "sneller. <strong>De pupilreflex, de slikreflex en de speekselreflex lopen via de "
                  "hersenstam.</strong>"),
            ("p", "<strong>De kniepeesreflex, de slikreflex en de pupilreflex zijn reflexen</strong>; "
                  "<strong>schrijven is een gewilde beweging</strong>, want je beslist er zelf over. "
                  "<strong>Bij een gewilde beweging gaat de impuls eerst naar de grote hersenen</strong>, en "
                  "daar wordt de beweging beslist."),
            ("p", "<strong>Een bewuste gewaarwording komt tot stand in de grote hersenen</strong>: pas in het "
                  "juiste hersencentrum wordt de impuls een gewaarwording. <strong>Het zweten bij warmte, het "
                  "kloppen van je hart en de pupil die kleiner wordt, gebeuren onbewust</strong>; een boek "
                  "kiezen is een bewuste keuze."),
        ]),
    ])


# ───────────────────────── 5. Gezondheid in kaart: Gordon en het ICF
zet("gezondheid-in-kaart-gordon-en-het-icf",
    titel="Gezondheid in kaart: Gordon en het ICF",
    onder="De elf gezondheidspatronen van Gordon en wat er in elk patroon thuishoort, het ICF-schema met de gezondheidstoestand, het ik en de omgeving, en waarom je met een vast schema werkt.",
    secties=[
        dict(kop="De elf patronen van Gordon", blokken=[
            ("p", "<strong>De gezondheidspatronen van Gordon dienen om iemand te leren kennen</strong>: met "
                  "<strong>elf patronen</strong> breng je het totale functioneren van een persoon in kaart."),
            ("kader", tabel(["patroon", "waarover het gaat"],
                            [["<strong>gezondheidsbeleving en instandhouding</strong>", "<strong>hoe iemand zijn eigen gezondheid ziet</strong> en wat hij ervoor doet"],
                             ["<strong>voeding en stofwisseling</strong>", "<strong>wat iemand eet</strong> en drinkt, en wat het lichaam ermee doet"],
                             ["<strong>uitscheiding</strong>", "<strong>naar het toilet gaan</strong>: plassen, stoelgang en zweten"],
                             ["<strong>activiteiten</strong>", "bewegen, werken, vrije tijd"],
                             ["<strong>slaap en rust</strong>", "hoe iemand slaapt en uitrust"],
                             ["<strong>waarneming en cognitie</strong>", "<strong>zien, horen en onthouden</strong>: de zintuigen, het denken en het geheugen"],
                             ["<strong>zelfbeleving</strong>", "<strong>hoe iemand over zichzelf denkt</strong>: het zelfbeeld en de eigenwaarde"],
                             ["<strong>rol en relatie</strong>", "de plaats in het gezin, op school, in de groep"],
                             ["<strong>seksualiteit en voortplanting</strong>", "beleving en relaties"],
                             ["<strong>stressverwerking</strong>", "<strong>omgaan met een moeilijke periode</strong>: hoe iemand spanning en tegenslag aanpakt"],
                             ["<strong>waarden en levensopvatting</strong>", "<strong>het geloof en de overtuigingen</strong>: wat iemand belangrijk vindt in het leven"]])),
            ("p", "Winst en verlies hoort bij een boekhouding en is geen patroon van Gordon. <strong>Gordon "
                  "kijkt niet enkel naar het lichaam</strong>: de patronen gaan ook over relaties, zelfbeeld, "
                  "stress en waarden."),
            ("p", "<strong>De patronen hangen met elkaar samen</strong>: verandert er iets in één patroon, dan "
                  "voel je dat vaak in een ander. <strong>Slecht slapen beïnvloedt het patroon "
                  "activiteiten</strong>, want wie te weinig slaapt, beweegt en onderneemt doorgaans minder."),
            ("p", "<strong>Je gebruikt Gordon niet om een medische diagnose te stellen</strong>: een diagnose "
                  "stelt een arts. Gordon brengt het functioneren in kaart."),
        ]),
        dict(kop="Het ICF-schema", blokken=[
            ("p", "<strong>Het ICF-schema dient om het functioneren te bekijken</strong>, met de persoon en de "
                  "omgeving erbij."),
            ("fig", svg.icfschema(),
             "De gezondheidstoestand in drie delen, met het ik en de omgeving eronder. De pijlen lopen in twee "
             "richtingen."),
            ("kader", tabel(["deel", "de vraag erbij"],
                            [["<strong>lichaam</strong>", "<strong>hoe werkt het lichaam?</strong> De werking van de organen en de lichaamsfuncties"],
                             ["<strong>doen</strong>", "<strong>wat doet iemand zelf?</strong> De activiteiten: zich wassen, koken"],
                             ["<strong>samen</strong>", "<strong>doet iemand mee?</strong> Deelnemen aan de maatschappij: werken, school, vrije tijd"]])),
            ("p", "Geld hoort niet bij de gezondheidstoestand. <strong>Persoonlijke factoren horen bij het "
                  "ik</strong>: <strong>leeftijd en karakter</strong>, maar ook geslacht en achtergrond. "
                  "<strong>De individuele achtergrond is wat iemand meemaakte</strong>: zijn opleiding, zijn "
                  "ervaringen, zijn gewoonten."),
            ("p", "<strong>De omgeving is alles buiten de persoon</strong>: <strong>de woning, het gezin, de "
                  "school</strong>, de buurt, de diensten. Dat zijn de externe factoren. <strong>Persoonlijke "
                  "en externe factoren zijn dus niet hetzelfde</strong>: het karakter zit bij het ik, de "
                  "woonplaats in de omgeving."),
            ("p", "<strong>Het ICF kijkt ook naar de omgeving omdat die helpt of hindert</strong>: een lift of "
                  "een behulpzame buur helpt, een trap of lawaai hindert. <strong>Kan een kind in een rolstoel "
                  "niet in de klas omdat er een trap staat, dan is die trap een externe factor</strong>: het "
                  "lichaam van het kind is niet het probleem, het gebouw is het. <strong>Een aangepaste woning "
                  "kan het functioneren verbeteren</strong> zonder dat er aan het lichaam iets verandert."),
            ("p", "<strong>Het ICF kijkt niet alleen naar wat niet lukt</strong>: het brengt ook in kaart wat "
                  "wel lukt en wat de omgeving aan steun biedt. <strong>Gezondheidstoestand, ik en omgeving "
                  "hangen samen</strong> en beïnvloeden elkaar, en daarom staan ze in één schema."),
            ("p", "<strong>Het verschil met Gordon: Gordon werkt met elf patronen, het ICF met de "
                  "gezondheidstoestand, het ik en de omgeving.</strong> <strong>Met allebei kan je het "
                  "functioneren bekijken, een plan opstellen en de sterktes zien</strong>; een diagnose stellen "
                  "is werk van een arts."),
        ]),
        dict(kop="Waarom een vast schema", blokken=[
            ("p", "<strong>Een systematische aanpak zorgt dat je minder vergeet, sneller werkt en het kan "
                  "uitleggen.</strong> Een vaste werkwijze vervangt het kijken niet; ze zorgt dat je niets "
                  "overslaat."),
            ("p", "<strong>De eerste stap bij het oplossen van een probleem is het probleem benoemen</strong>: "
                  "eerst vaststellen wat er precies aan de hand is, pas daarna zoeken naar een oplossing."),
            ("p", "<strong>Je gebruikt een vast schema zoals dat van Gordon omdat je dan naar het geheel "
                  "kijkt.</strong> Zonder schema kijk je enkel naar wat opvalt en mis je de rest van het "
                  "functioneren."),
        ]),
    ])


# ───────────────────────── 6. Ziek zijn en eerste hulp
zet("ziek-zijn-en-eerste-hulp",
    titel="Ziek zijn en eerste hulp",
    onder="De symptomen van ziek zijn en de gezondheidsproblemen die bij jongeren vaak voorkomen, en daarna de vier stappen van eerste hulp, de noodnummers en wat je doet bij een bloeding, een brandwonde of een reanimatie.",
    secties=[
        dict(kop="Ziek zijn herkennen", blokken=[
            ("p", "<strong>Koorts, braken, misselijkheid, diarree, pijn en geen zin om te spelen zijn "
                  "symptomen van ziek zijn.</strong> <strong>Koorts is een hoge temperatuur</strong>: het "
                  "lichaam zet zijn temperatuur hoger om ziektekiemen te bestrijden."),
            ("p", "<strong>Vermoeidheid is een symptoom omdat het lichaam vecht</strong>: het gebruikt zijn "
                  "energie om beter te worden, dus er blijft minder over. <strong>Beperkt zijn in het "
                  "zelfstandig functioneren betekent dat het niet alleen lukt</strong>: wat iemand normaal "
                  "zelf doet, zoals zich wassen of aankleden, lukt tijdelijk niet meer."),
            ("p", "<strong>Voel je dat een kind ziek is, dan vraag je eerst hoe het voelt</strong>: eerst "
                  "kijken en vragen wat er is, zo weet je wat het kind nodig heeft. <strong>Bij diarree laat "
                  "je het veel drinken</strong>, want het lichaam verliest dan veel vocht. <strong>Bij koorts "
                  "heeft het lichaam rust en vocht nodig</strong>, geen beweging."),
        ]),
        dict(kop="Gezondheidsproblemen bij jongeren", blokken=[
            ("kader", tabel(["probleem", "wat helpt"],
                            [["<strong>slaaptekort</strong>", "<strong>op tijd gaan slapen</strong>: een vast uur en geen scherm het laatste uur voor het slapen"],
                             ["<strong>rugklachten</strong>", "<strong>een goede houding</strong>: rechtop zitten, de tas op twee schouders, regelmatig even rechtstaan"],
                             ["<strong>stress en faalangst</strong>", "<strong>op tijd beginnen leren</strong>: goed voorbereid zijn en erover praten nemen een groot deel van de spanning weg"],
                             ["<strong>overgewicht</strong>", "<strong>genoeg bewegen, gezond eten en water drinken</strong>; veel zitten is sedentair gedrag en werkt het net in de hand"],
                             ["<strong>gebitsproblemen</strong>", "<strong>twee keer per dag poetsen</strong>, weinig zoete dranken en jaarlijks naar de tandarts"],
                             ["<strong>allergie</strong>", "de uitlokker mijden: <strong>pollen, huisstofmijt en dierenhaar</strong> zijn de bekendste"],
                             ["<strong>een soa</strong>", "<strong>een condoom</strong> is de belangrijkste bescherming"]])),
            ("p", "Een gebroken arm is een ongeval en geen vaak voorkomend gezondheidsprobleem. <strong>Stress "
                  "hoort er bij jongeren niet gewoon bij</strong>: stress en faalangst staan in de fiche als "
                  "problemen die je kan voorkomen."),
            ("p", "<strong>Hooikoorts is de allergie voor pollen</strong>, voor het stuifmeel in de lente. "
                  "<strong>Soa staat voor seksueel overdraagbare aandoening.</strong>"),
        ]),
        dict(kop="Eerste hulp", blokken=[
            ("fig", svg.stappen(["zorg voor|veiligheid", "beoordeel het|slachtoffer",
                                 "roep|gespecialiseerde hulp", "geef verdere|eerste hulp"]),
             "De vier stappen van eerste hulp. Veiligheid eerst, anders word je zelf het tweede slachtoffer."),
            ("p", "<strong>De basisprincipes: blijf rustig, vermijd besmetting, zorg voor comfort</strong>, "
                  "blijf bij het slachtoffer, handel als hulpverlener, geef psychosociale hulp en denk aan de "
                  "reacties achteraf."),
            ("kader", tabel(["nummer", "waarvoor"],
                            [["<strong>112</strong>", "<strong>de ziekenwagen en de brandweer</strong>"],
                             ["<strong>101</strong>", "<strong>de politie</strong>"],
                             ["<strong>1733</strong>", "<strong>de huisarts</strong> of de huisartsenwachtpost, voor klachten die geen 112 vragen"],
                             ["<strong>70 245 245</strong>", "<strong>het antigifcentrum</strong>, bij een vergiftiging; bij levensgevaar bel je eerst 112"]])),
            ("kader", tabel(["situatie", "wat je doet"],
                            [["<strong>een zware bloeding</strong>", "<strong>de wonde dichtdrukken</strong> met een verband of je hand, en 112 bellen"],
                             ["<strong>iemand verslikt zich en kan nog hoesten</strong>", "<strong>je laat hem hoesten</strong>: hoesten is de sterkste manier om het voorwerp los te krijgen. Lukt dat niet meer, dan geef je slagen tussen de schouderbladen"],
                             ["<strong>een brandwonde</strong>", "<strong>koelen met lauw lopend water</strong>, tien tot twintig minuten. Geen ijs, geen zalf, geen blaar openmaken"],
                             ["<strong>een verstuiking</strong>", "<strong>koelen en rust</strong>, zodat de zwelling klein blijft"],
                             ["<strong>een ontwrichting</strong>", "<strong>het bot schoot uit de kom</strong>: laat het gewricht zoals het is en ga naar de spoed"]])),
            ("p", "<strong>Letsels aan botten, spieren en gewrichten zijn de botbreuk, de verstuiking, de "
                  "kneuzing en de ontwrichting.</strong> Een brandwonde is een wonde van de huid. <strong>Een "
                  "botbreuk heet ook een fractuur.</strong>"),
            ("p", "<strong>Bij reanimatie bel je 112, start je borstcompressies en zoek je een AED</strong>, "
                  "een automatische externe defibrillator. <strong>Je gaat door tot de ambulance er is</strong>, "
                  "want stoppen betekent dat het bloed niet meer rondgaat. <strong>Een AED is voor iedereen "
                  "bedoeld</strong>, niet enkel voor een dokter: het toestel legt zelf stap voor stap uit wat "
                  "je moet doen. Een bewusteloos slachtoffer krijgt nooit te drinken."),
            ("p", "<strong>Je mag een slachtoffer niet zomaar verplaatsen</strong>: verplaats alleen als er "
                  "gevaar is, want verplaatsen kan een letsel erger maken."),
        ]),
    ])


# ───────────────────────── 7. Gezondheid bevorderen: preventie, voeding en beweging
zet("gezondheid-bevorderen-preventie-voeding-en-beweging",
    titel="Gezondheid bevorderen: preventie, voeding en beweging",
    onder="De drie delen van gezondheidsbevordering, primaire, secundaire en tertiaire preventie, de voedingsdriehoek met haar drie uitgangspunten, de vier bewegingscategorieën, slaap en hygiëne.",
    secties=[
        dict(kop="Bevorderen, voorkomen, beschermen", blokken=[
            ("p", "<strong>Gezondheidsbevordering is de gezondheid versterken.</strong> Het gaat niet over "
                  "genezen maar over de gezondheid van mensen verbeteren en beschermen. <strong>Ze bestaat uit "
                  "ziektepreventie, gezondheidspromotie en gezondheidsbescherming.</strong> Een "
                  "ziekteverzekering betaalt de zorg en bevordert de gezondheid niet."),
            ("p", "<strong>Gezondheidsbescherming is de omgeving veilig maken</strong>: schoon drinkwater, "
                  "veilige voeding, een rookverbod. Regels die iedereen beschermen."),
            ("kader", tabel(["preventie", "wanneer", "voorbeeld"],
                            [["<strong>primair</strong>", "<strong>vóór de ziekte er is</strong>: voorkomen dat je ziek wordt", "<strong>een vaccinatie tegen mazelen</strong>, gezond eten, niet roken"],
                             ["<strong>secundair</strong>", "<strong>vroeg opsporen</strong>, als de ziekte nog goed te behandelen is", "<strong>een bevolkingsonderzoek naar kanker</strong>, bij mensen zonder klachten"],
                             ["<strong>tertiair</strong>", "<strong>de ziekte is er al</strong>: de gevolgen beperken", "herval en blijvende schade zo klein mogelijk houden"]])),
            ("p", "<strong>Je bevordert gezondheid op vier manieren: een gezonde leefomgeving maken, "
                  "vaardigheden aanleren, je gedrag aanpassen, en bewust en actief omgaan met je gezondheid en "
                  "die van anderen.</strong> <strong>Gezondheidsbevordering gaat dus niet alleen over "
                  "voeding</strong>: ook beweging, slaap, hygiëne en de leefomgeving horen erbij. <strong>Een "
                  "gezonde leefomgeving heeft wel degelijk met gezondheid te maken</strong>, ze is net een van "
                  "die vier manieren."),
        ]),
        dict(kop="De voedingsdriehoek", blokken=[
            ("fig", svg.voedingsdriehoek(),
             "De voedingsdriehoek staat op zijn kop: het breedste deel bovenaan is wat je het meest eet. De "
             "restgroep staat er helemaal buiten."),
            ("p", "<strong>De drie uitgangspunten: meer plantaardig dan dierlijk, zo weinig mogelijk lege "
                  "calorieën, en matig je consumptie.</strong> <strong>Lege calorieën zijn energie zonder "
                  "voeding</strong>: veel energie maar bijna geen vitaminen, mineralen of vezels, zoals in "
                  "snoep en frisdrank."),
            ("p", "<strong>Je eet en drinkt het meest water, groenten en fruit</strong>, daarna granen, noten "
                  "en peulvruchten, en hoogstens weinig dierlijke producten. <strong>De restgroep staat buiten "
                  "de driehoek</strong>: hoe minder, hoe beter. Snoep hoort daar thuis."),
        ]),
        dict(kop="Bewegen en slapen", blokken=[
            ("kader", tabel(["categorie", "wat het is"],
                            [["<strong>sedentair gedrag</strong>", "<strong>lang stil zitten</strong> of liggen terwijl je wakker bent, met bijna geen energieverbruik"],
                             ["<strong>licht intensief bewegen</strong>", "rondlopen, rustig fietsen, huishoudelijk werk"],
                             ["<strong>matig intensief bewegen</strong>", "<strong>stevig wandelen</strong>: je ademt sneller maar je kan nog praten"],
                             ["<strong>hoog intensief bewegen</strong>", "<strong>sprinten</strong>: je ademt zo snel dat praten niet meer lukt"]])),
            ("p", "<strong>Er zijn dus vier bewegingscategorieën</strong>; half intensief bestaat niet. "
                  "<strong>Sedentair gedrag is geen vorm van intensief bewegen</strong>, het is juist "
                  "stilzitten. <strong>De bewegingsdriehoek raadt vooral aan om minder lang stil te "
                  "zitten</strong>: zit zo weinig mogelijk stil en beweeg zo veel mogelijk, verspreid over de "
                  "hele dag."),
            ("p", "<strong>Slapen is belangrijk omdat het lichaam herstelt</strong>: in je slaap herstelt je "
                  "lichaam, groei je en verwerken je hersenen wat je die dag leerde. <strong>Hoeveel slaap "
                  "iemand nodig heeft, hangt af van de leeftijd, van het moment van inslapen en van de "
                  "kwaliteit van de slaap</strong>, en van individuele verschillen. Een kind heeft meer slaap "
                  "nodig dan een volwassene; de kleur van de kamer speelt geen rol."),
            ("p", "<strong>Slaaphygiëne zijn de gewoonten die zorgen dat je goed slaapt</strong>: <strong>elke "
                  "dag een vast uur, een donkere kamer en een koele kamer</strong>. Een scherm vlak voor het "
                  "slapen houdt je juist wakker."),
        ]),
        dict(kop="Persoonlijke hygiëne", blokken=[
            ("p", "<strong>Een goede persoonlijke hygiëne heeft wel degelijk invloed op je gezondheid</strong>: "
                  "ze houdt ziektekiemen weg en voorkomt huid- en mondproblemen."),
            ("p", "<strong>Mondhygiëne voorkomt gaatjes</strong>: tandplak veroorzaakt gaatjes en "
                  "tandvleesontsteking, en poetsen houdt dat tegen."),
            ("p", "<strong>Je wast je handen zeker vóór je gaat koken</strong> en voor het eten, na het toilet, "
                  "na het niezen en na het aaien van een dier. <strong>Correct wassen doe je over de palmen, "
                  "de rug, tussen de vingers, de duimen en de nagels</strong>, en daarna goed afdrogen."),
            ("p", "<strong>Wassen verwijdert het vuil en de kiemen; ontsmetten doodt de kiemen maar laat vuil "
                  "liggen.</strong> <strong>Je ontsmet dus enkel handen die er schoon uitzien</strong>: "
                  "<strong>op zichtbaar vuile handen werkt ontsmetten niet goed</strong>, want het vuil zit "
                  "tussen het product en de kiemen. Eerst wassen, dan eventueel ontsmetten."),
        ]),
    ])


# ───────────────────────── 8. Kwaliteitsbewust handelen
zet("kwaliteitsbewust-handelen",
    titel="Kwaliteitsbewust handelen",
    onder="De zeven factoren van kwaliteitsbewust handelen, het OVUR-schema en de 5S-methode, de gevarentekens en het etiket, ergonomie aan de werkpost, en de Ladder van Lansink met de afvalcategorieën.",
    secties=[
        dict(kop="De zeven factoren", blokken=[
            ("p", "<strong>Kwaliteitsbewust handelen heeft zeven factoren</strong>, en samen bepalen ze of je "
                  "werk kwaliteit heeft. <strong>Het gaat dus niet alleen over snelheid</strong>; snelheid "
                  "staat niet eens in het rijtje."),
            ("kader", tabel(["factor", "wat het betekent"],
                            [["<strong>respectvol</strong>", "<strong>respect tonen voor jezelf, voor anderen en voor het materiaal</strong>"],
                             ["<strong>belevingsgericht</strong>", "<strong>kijken wat de ander voelt</strong>: rekening houden met zijn gevoelens, noden, wensen en beperkingen"],
                             ["<strong>methodisch</strong>", "<strong>volgens een vast plan werken</strong>, in een vaste orde, zodat je niets vergeet"],
                             ["<strong>hygiënisch</strong>", "<strong>kiemen tegenhouden</strong>: zo werken dat ziektekiemen zich niet verspreiden"],
                             ["<strong>veilig</strong>", "gevaren herkennen en vermijden"],
                             ["<strong>ergonomisch</strong>", "<strong>werken zonder schade</strong>: het werk afstemmen op het lichaam"],
                             ["<strong>economisch</strong>", "<strong>zuinig omgaan met materiaal en tijd</strong>"]])),
            ("p", "<strong>Respect voor materiaal hoort er wel degelijk bij</strong>, het is een van de drie "
                  "richtingen. <strong>De belevingswereld van iemand bestaat uit zijn gevoelens, zijn noden "
                  "of behoeften, zijn wensen en zijn beperkingen.</strong>"),
            ("p", "<strong>De drie huishoudelijke taken zijn maaltijdzorg, interieurzorg en "
                  "linnenzorg.</strong>"),
        ]),
        dict(kop="OVUR en de 5S-methode", blokken=[
            ("fig", svg.stappen(["oriënteren|wat is de opdracht?", "voorbereiden|wat heb ik nodig?",
                                 "uitvoeren|volgens plan", "reflecteren|hoe ging het?"]),
             "Het OVUR-schema: oriënteren, voorbereiden, uitvoeren, reflecteren."),
            ("p", "<strong>De eerste stap van OVUR is oriënteren</strong>: wat is de opdracht precies? "
                  "<strong>Bij de R van OVUR blik je terug</strong>: ging het goed, wat zou je een volgende "
                  "keer anders doen? <strong>Het schema eindigt dus met reflecteren.</strong>"),
            ("p", "<strong>De 5S-methode dient om je werkpost te schikken</strong>: ze organiseert, inspecteert "
                  "en onderhoudt je werkplek."),
            ("kader", tabel(["S", "wat je doet", "waarvoor"],
                            [["<strong>scheiden</strong>", "wat je niet nodig hebt, gaat weg", "<strong>organiseren</strong>"],
                             ["<strong>schikken</strong>", "elk ding zijn vaste plaats", "<strong>organiseren</strong>"],
                             ["<strong>schoonmaken</strong>", "poetsen en tegelijk nakijken", "<strong>inspecteren</strong>"],
                             ["<strong>standaardiseren</strong>", "<strong>een vaste werkwijze maken</strong>, zodat iedereen het telkens op dezelfde manier doet", "<strong>onderhouden</strong>"],
                             ["<strong>standhouden</strong>", "het volhouden", "<strong>onderhouden</strong>"]])),
        ]),
        dict(kop="Veilig werken", blokken=[
            ("p", "<strong>Een gevarensymbool is een ruit met een rode rand</strong> en een zwart teken erin."),
            ("kader", tabel(["soort teken", "vorm", "betekenis"],
                            [["<strong>verbodsteken</strong>", "een rode cirkel met een streep erdoor", "<strong>iets mag niet</strong>"],
                             ["<strong>gebodsteken</strong>", "een blauwe cirkel", "<strong>iets is verplicht</strong>, bijvoorbeeld een veiligheidsbril dragen"],
                             ["<strong>waarschuwingsteken</strong>", "een gele driehoek", "let op, hier is gevaar"],
                             ["<strong>reddingsteken</strong>", "groen", "<strong>het wijst de nooduitgang</strong>, de verbanddoos of de AED"]])),
            ("p", "Rekentekens bestaan niet in de veiligheid. <strong>Van een etiket lees je het gebruik, de "
                  "dosering en de gevarensymbolen af</strong>, en ook de gevarenaanduidingen en de "
                  "veiligheidsaanduidingen."),
            ("p", "<strong>Ergonomie stemt het werk af op het lichaam</strong>, zodat je er geen klachten van "
                  "krijgt. <strong>Een zware doos til je met gebogen knieën</strong>: zak door je knieën, hou "
                  "je rug recht en de last dicht bij je lichaam. <strong>Ergonomisch handelen gaat niet alleen "
                  "over tillen</strong>, ook over je zithouding, je stahouding en de schikking van je "
                  "werkpost. <strong>Bij het inrichten van een werkpost hou je rekening met de "
                  "gebruiksfrequentie, de reikwijdte en de reikhoogte</strong> van wat je nodig hebt."),
        ]),
        dict(kop="Afval en de Ladder van Lansink", blokken=[
            ("p", "<strong>De Ladder van Lansink is een rangorde voor afval</strong>: ze zet de manieren om "
                  "met afval om te gaan op een rij, van de beste naar de slechtste."),
            ("fig", svg.ladder([("preventie", "afval voorkomen"),
                                ("hergebruik", "opnieuw gebruiken wat er is"),
                                ("recyclage", "de grondstof terugwinnen"),
                                ("verbranden", "met energierecuperatie"),
                                ("storten", "het laatste redmiddel")]),
             "De Ladder van Lansink. Bovenaan staat preventie: afval voorkomen is beter dan het verwerken."),
            ("p", "<strong>Bovenaan staat preventie</strong>: afval voorkomen is het beste, en pas daarna komen "
                  "hergebruiken, recycleren en verbranden."),
            ("kader", tabel(["categorie", "wat erin hoort"],
                            [["<strong>gft</strong>", "<strong>groenten-, fruit- en tuinafval</strong>: <strong>een bananenschil</strong>"],
                             ["<strong>pmd</strong>", "plastic flessen, metalen verpakkingen en drankkartons: <strong>een plastic fles</strong>"],
                             ["<strong>glas</strong>", "flessen en bokalen"],
                             ["<strong>papier en karton</strong>", "kranten, dozen"],
                             ["<strong>kga</strong>", "<strong>klein gevaarlijk afval</strong>: <strong>een batterij</strong>, verf, medicijnen"],
                             ["<strong>restafval</strong>", "wat in geen enkele andere zak past"]])),
            ("p", "Grijsafval bestaat niet als categorie, en <strong>een batterij hoort niet bij het "
                  "restafval</strong> maar bij het kga. <strong>Kostenbewust handelen is zuinig omgaan met "
                  "materiaal en tijd</strong>: economisch handelen let op de kosten van wat je gebruikt én van "
                  "de tijd die je besteedt."),
        ]),
    ])


# ───────────────────────── 9. Voedingsstoffen en een evenwichtig dagmenu
zet("voedingsstoffen-en-een-evenwichtig-dagmenu",
    titel="Voedingsstoffen en een evenwichtig dagmenu",
    onder="Het verschil tussen een voedingsmiddel en een voedingsstof, de zeven voedingsstoffen met hun functies, hoe een dagmenu eruitziet en welke voedingsfouten de fiche noemt.",
    secties=[
        dict(kop="Middel of stof", blokken=[
            ("p", "<strong>Een voedingsmiddel is wat je eet</strong>, zoals een boterham; <strong>de "
                  "voedingsstoffen zitten erin</strong>, zoals koolhydraten. <strong>Een middel bevat dus "
                  "stoffen</strong>, en <strong>meestal meerdere tegelijk</strong>: een boterham met kaas "
                  "bevat koolhydraten, eiwitten, vetten, vitaminen en water."),
            ("kader", tabel(["voedingsstof", "waarvoor", "waar je ze vindt"],
                            [["<strong>eiwitten</strong>", "<strong>ze bouwen het lichaam op</strong>: de bouwstenen van spieren, huid en organen", "<strong>vlees, vis, eieren</strong>, peulvruchten en noten"],
                             ["<strong>koolhydraten</strong>", "<strong>ze leveren het snelst energie</strong>: de brandstof die je lichaam het eerst gebruikt", "brood, pasta, rijst, aardappelen"],
                             ["<strong>vetten</strong>", "<strong>ze leveren veel energie en slaan ze op</strong>, en ze helpen bij het opnemen van sommige vitaminen", "olie, boter, noten, vette vis"],
                             ["<strong>vitaminen</strong>", "<strong>ze beschermen het lichaam</strong> en houden het afweersysteem op gang", "groenten en fruit"],
                             ["<strong>mineralen</strong>", "beschermen en in stand houden; <strong>ze leveren geen energie</strong>", "melkproducten, groenten, water"],
                             ["<strong>voedingsvezels</strong>", "<strong>ze helpen de darmen</strong>; ze leveren geen energie maar houden de darmen aan het werk", "volkoren producten, groenten, fruit"],
                             ["<strong>water</strong>", "<strong>je lichaam bestaat eruit</strong>, voor meer dan de helft, en het verliest elke dag vocht", "water, en alles wat vocht bevat"]])),
            ("p", "<strong>Er zijn dus zeven voedingsstoffen</strong>, en <strong>vier functies: energie "
                  "leveren, het lichaam opbouwen, het lichaam beschermen en het lichaam in stand "
                  "houden.</strong> Afkoelen hoort er niet bij."),
            ("p", "<strong>Water, vitaminen, mineralen en vezels leveren geen energie.</strong> <strong>Eiwitten, "
                  "vetten en koolhydraten zijn essentieel omdat het lichaam ze nodig heeft</strong>: ze leveren "
                  "samen de dagelijkse energie en de bouwstoffen, en zonder een van de drie loopt het mis. "
                  "<strong>Koolhydraten bouwen de spieren niet op</strong>: dat doen de eiwitten."),
        ]),
        dict(kop="Een dagmenu samenstellen", blokken=[
            ("p", "<strong>Een dagmenu bestaat uit het ontbijt, de lunch en het avondmaal, plus twee à drie "
                  "tussendoortjes.</strong> Een dessertbord is geen maaltijd op zich. <strong>Elke maaltijd "
                  "heeft haar eigen aandeel in de energie van de dag</strong>, en <strong>het ontbijt mag je "
                  "dus niet zomaar overslaan.</strong>"),
            ("p", "<strong>Hoeveel iemand eet, hangt af van de leeftijd, het geslacht, de groei en de mate van "
                  "fysieke activiteit.</strong> Wie groeit of veel beweegt, heeft meer energie nodig. "
                  "<strong>Een kind heeft dus andere hoeveelheden nodig dan een volwassene</strong>: de "
                  "aanbevolen dagelijkse hoeveelheden verschillen per leeftijdscategorie."),
            ("p", "<strong>Bij het samenstellen van een dagmenu hou je rekening met de voedingsdriehoek en met "
                  "de aanbevolen dagelijkse hoeveelheden</strong> voor die leeftijd. Dat zijn de twee "
                  "leidraden. <strong>Een gezond tussendoortje is een stuk fruit</strong>, groenten of een "
                  "handvol noten."),
            ("kader", tabel(["voedingsfout", "wat eraan scheelt"],
                            [["<strong>te grote porties</strong>", "meer energie dan je verbruikt"],
                             ["<strong>te weinig groenten</strong>", "te weinig vitaminen, mineralen en vezels"],
                             ["<strong>te veel alcohol</strong>", "lege calorieën en schade op termijn"],
                             ["<strong>een onregelmatig patroon</strong>", "<strong>elke dag op een ander uur eten</strong> maakt het moeilijker om evenwichtig te eten"],
                             ["<strong>te calorierijke voedingsmiddelen</strong>", "veel energie voor weinig voedingsstoffen"]])),
            ("p", "<strong>Een maaltijd met te veel frisdrank verbeter je door water te geven</strong>: "
                  "suikerhoudende dranken vervangen door water is de eenvoudigste verbetering. <strong>Pas je "
                  "een recept aan, dan hou je rekening met het aantal personen</strong> en maak je meteen "
                  "gezondere keuzes."),
            ("p", "<strong>Voor je een maaltijd bereidt, was je eerst je handen.</strong> Hygiënisch handelen "
                  "komt vóór je begint en loopt door terwijl je je werkpost schikt."),
        ]),
    ])


# ───────────────────────── 10. Voedselveiligheid en voedselhygiëne
zet("voedselveiligheid-en-voedselhygiene",
    titel="Voedselveiligheid en voedselhygiëne",
    onder="De vier levensvoorwaarden van micro-organismen, de drie soorten bederf, het verschil tussen een voedselinfectie en een voedselvergiftiging, kruisbesmetting, en de HACCP-richtlijnen van boodschap tot afwas.",
    secties=[
        dict(kop="Micro-organismen", blokken=[
            ("p", "<strong>Voedselveiligheid betekent eten zonder gevaar</strong>: dat je van het eten niet "
                  "ziek kan worden. <strong>Micro-organismen zijn kleine levende wezens</strong> die je niet "
                  "met het blote oog ziet, zoals bacteriën en schimmels."),
            ("p", "<strong>Ze hebben vier dingen nodig om te groeien: water, voedsel, zuurstof en een goede "
                  "temperatuur.</strong> Donker hoeft niet. <strong>Haal er één weg en de groei stopt</strong>, "
                  "en dat is precies wat bewaren doet: <strong>invriezen pakt de temperatuur aan</strong>. "
                  "<strong>Micro-organismen groeien goed bij kamertemperatuur</strong>, en daarom hoort "
                  "bederfbaar voedsel in de koelkast en niet op het aanrecht."),
            ("p", "<strong>Niet alle bacteriën zijn slecht</strong>: <strong>bacteriën maken yoghurt</strong>, "
                  "kaas en zuurkool, en in je darmen helpen ze bij de vertering. <strong>Schimmels bederven "
                  "voedsel</strong>: op brood of confituur maken ze het oneetbaar en soms giftig. <strong>Een "
                  "schimmel op confituur schep je er niet gewoon af</strong>: de draden zitten dieper dan je "
                  "ziet, dus de hele pot gaat weg."),
        ]),
        dict(kop="Drie soorten bederf", blokken=[
            ("kader", tabel(["soort bederf", "wat er gebeurt", "voorbeeld"],
                            [["<strong>fysisch</strong>", "<strong>van buitenaf</strong>", "<strong>uitdrogen</strong>, bevriezen, kneuzen"],
                             ["<strong>chemisch</strong>", "<strong>de stof zelf verandert</strong>", "<strong>vet dat ranzig wordt</strong> doordat het met zuurstof reageert"],
                             ["<strong>biologisch</strong>", "<strong>door micro- of macro-organismen</strong>", "<strong>bacteriën, schimmels en insecten</strong>; <strong>een muis</strong> of maden zijn macro-organismen, die zie je wel"]])),
            ("p", "<strong>Van bedorven voedsel word je misselijk</strong>, en je kan ook braken of diarree "
                  "krijgen, of een voedselinfectie of voedselvergiftiging oplopen. Je gezichtsvermogen heeft "
                  "er niets mee te maken."),
            ("p", "<strong>Bij een voedselvergiftiging zit de gifstof al in het eten en maakt die je "
                  "ziek</strong>; <strong>bij een voedselinfectie groeit de bacterie pas in je lichaam.</strong> "
                  "<strong>Voedselbederf kan je niet altijd zien of ruiken</strong>: sommige bacteriën "
                  "veranderen niets aan geur, kleur of smaak, en maken je toch ziek."),
        ]),
        dict(kop="Kruisbesmetting en HACCP", blokken=[
            ("p", "<strong>Kruisbesmetting is dat kiemen overgaan</strong> van het ene voedingsmiddel naar het "
                  "andere, vaak via je handen, een mes, een plank of een keukenhanddoek. <strong>Je voorkomt "
                  "het met aparte snijplanken</strong>: rauw vlees krijgt zijn eigen plank en mes, en je wast "
                  "je handen ertussen. <strong>Rauw vlees en rauwe groenten snij je dus niet op dezelfde "
                  "plank</strong>, want groenten worden soms rauw gegeten."),
            ("p", "<strong>Een snijplank van rauwe kip hergebruik je niet zonder wassen</strong>: op rauwe kip "
                  "zitten vaak salmonellabacteriën, en de plank gaat eerst in heet water met zeep."),
            ("p", "<strong>HACCP is een reeks richtlijnen</strong> die de gevaren bij de voedselbereiding "
                  "opspoort en afdekt, zodat er in geen enkele stap iets misgaat met de veiligheid."),
            ("fig", svg.stappen(["boodschappen|ontvangen", "bewaren", "hygiënisch|werken",
                                 "voedsel|bereiden", "afruimen en|afwassen"]),
             "HACCP loopt van het ontvangen van de boodschappen tot de afwas: elke stap heeft haar eigen "
             "regels."),
            ("p", "<strong>Bij het ontvangen van boodschappen controleer je de datum</strong>: kijk de "
                  "houdbaarheidsdatum en de verpakking na, en berg koele waren meteen op."),
            ("p", "<strong>Je werkt met propere handen omdat kiemen anders op het eten komen</strong>: je "
                  "handen zijn de snelste weg. <strong>Je wast ze vóór je begint, na rauw vlees en na het "
                  "toilet</strong>; na het afdrogen zijn ze net schoon, dus dan hoeft het niet opnieuw."),
            ("p", "<strong>Bij de persoonlijke hygiëne in de keuken horen een schorts dragen, de haren "
                  "samenbinden en de juwelen afleggen.</strong> Met je vingers proeven brengt juist kiemen in "
                  "het eten, en <strong>je proeft ook niet met de lepel waarmee je roert</strong>: via je mond "
                  "komen kiemen op de lepel en zo in de hele pot."),
            ("p", "<strong>Rauw vlees en groenten hou je apart</strong>, en <strong>restjes van gisteren warm "
                  "je door en door op</strong>, en maar één keer. <strong>Na het bereiden volgen het afruimen, "
                  "het afwassen en het schoonmaken</strong>: de laatste stappen van HACCP."),
        ]),
    ])


# ───────────────────────── 11. Voedsel bewaren
zet("voedsel-bewaren",
    titel="Voedsel bewaren",
    onder="De drie bewaarplaatsen, FIFO en FEFO, het verschil tussen THT en TGT, de zones van de koelkast, en de regels voor invriezen en ontdooien.",
    secties=[
        dict(kop="Waar en volgens welke regel", blokken=[
            ("p", "<strong>De drie bewaarplaatsen zijn de koelkast, de vriezer en een koele berging of "
                  "voorraadkast.</strong> In de wasmachine hoort geen voedsel."),
            ("p", "<strong>Een goede koele berging is donker, droog, koel en goed verlucht</strong>; warmte is "
                  "net wat je er niet wil. <strong>Daar bewaar je aardappelen</strong>, uien en conserven; vis, "
                  "gehakt en melkproducten horen in de koelkast. <strong>Een voorraadkast houdt de droge "
                  "waren</strong>: bloem, pasta, rijst en blikken blijven goed op een droge en donkere plaats."),
            ("p", "<strong>Je bewaart voedsel in de koelkast omdat kiemen er trager groeien</strong>: koude "
                  "haalt een levensvoorwaarde van micro-organismen weg, dus ze vermenigvuldigen trager."),
            ("kader", tabel(["principe", "wat het betekent"],
                            [["<strong>FIFO</strong>", "<strong>first in, first out: eerst in, eerst uit</strong>. Wat er het langst ligt, gebruik je eerst"],
                             ["<strong>FEFO</strong>", "<strong>first expired, first out: wat het eerst vervalt, gaat er het eerst uit</strong>. FEFO kijkt dus naar de vervaldatum en niet naar de datum van aankoop"]])),
            ("p", "<strong>Berg je nieuwe boodschappen op, dan zet je de oude vooraan.</strong> Zo gebruik je "
                  "vanzelf eerst wat er al stond, en dat is FIFO in de praktijk."),
            ("p", "<strong>Bij het bewaren hou je rekening met het voedingsmiddel, met de bewaarplaats en met "
                  "de houdbaarheidsdatum</strong>: wat het is, waar het hoort en tot wanneer het goed blijft."),
        ]),
        dict(kop="THT en TGT", blokken=[
            ("kader", tabel(["afkorting", "waarvoor", "na die datum"],
                            [["<strong>THT</strong>", "<strong>ten minste houdbaar tot</strong>, over de <strong>kwaliteit</strong>", "<strong>eerst kijken en ruiken</strong>: ziet en ruikt het goed, dan is het meestal nog bruikbaar"],
                             ["<strong>TGT</strong>", "<strong>te gebruiken tot</strong>, over de <strong>veiligheid</strong>", "<strong>weggooien</strong>, ook als het er goed uitziet"]])),
            ("p", "<strong>THT en TGT betekenen dus niet hetzelfde</strong>: THT gaat over kwaliteit, TGT over "
                  "veiligheid. <strong>Na de TGT-datum is een product niet meer veilig</strong>; dat is een "
                  "harde grens."),
        ]),
        dict(kop="De zones van de koelkast", blokken=[
            ("fig", svg.koelkastzones(),
             "De temperatuur is niet overal gelijk: koude lucht zakt, dus onderaan is het het koudst en in de "
             "deur het minst koud."),
            ("p", "<strong>De temperatuur in een koelkast is niet overal gelijk omdat koude lucht zakt</strong>: "
                  "koude lucht is zwaarder. <strong>De koudste plaats ligt onderaan, net boven de "
                  "groentelade</strong>, en <strong>daar horen rauw vlees, gehakt, vis en schaaldieren.</strong>"),
            ("p", "<strong>Groenten en fruit bewaar je in de groentelade</strong>, waar het iets minder koud is "
                  "en ze langer vers blijven. <strong>In de deur, de minst koude plaats, horen dranken, "
                  "sauzen, boter en eieren</strong>; rauw gehakt hoort er juist niet. <strong>Het glas staat "
                  "los hiervan: verse patisserie hoort in de koelkast</strong>, want ze bevat room en eieren. "
                  "<strong>Een geopende bokaal zet je in de koelkast</strong>: zodra ze open is, komt er lucht "
                  "bij en kunnen micro-organismen groeien."),
        ]),
        dict(kop="Invriezen en ontdooien", blokken=[
            ("p", "<strong>De voorwaarde om in te vriezen is dat het vers is.</strong> Invriezen stopt het "
                  "bederf, maar het maakt niets opnieuw vers. <strong>Ingevroren voedsel blijft dus niet "
                  "oneindig lang goed</strong>: <strong>diepvriesgroente blijft enkele maanden goed</strong>, "
                  "maar de kwaliteit gaat achteruit."),
            ("p", "<strong>Op een doos die de vriezer in gaat, schrijf je de inhoud, de datum en het aantal "
                  "personen.</strong> Zo weet je later wat het is, hoe lang het er al ligt en voor hoeveel "
                  "mensen het volstaat."),
            ("p", "<strong>Ontdooid voedsel vries je niet opnieuw in</strong>: bij het ontdooien groeien de "
                  "kiemen weer, en opnieuw invriezen haalt ze niet weg. <strong>Vlees ontdooi je het veiligst "
                  "in de koelkast</strong>, want daar blijft het koud terwijl het ontdooit."),
            ("p", "<strong>Restjes bewaar je in een afgesloten doos</strong>: zo blijven de kiemen buiten, de "
                  "geuren binnen en droogt het niet uit. Een gesloten doos koelt wel trager af, maar ze houdt "
                  "kiemen, geur en vocht waar ze horen."),
        ]),
    ])


# ───────────────────────── 12. Boodschappen doen en de tafel dekken
zet("boodschappen-doen-en-de-tafel-dekken",
    titel="Boodschappen doen en de tafel dekken",
    onder="De principes tegen voedselverspilling, milieubewust en economisch winkelen met een boodschappenlijst, en hoe je een tafel dekt voor een ontbijt en voor een warme maaltijd.",
    secties=[
        dict(kop="Minder verspillen", blokken=[
            ("p", "<strong>Voedselverspilling is eten weggooien dat nog goed was</strong>, en <strong>ze kost "
                  "ook geld</strong>: alles wat je weggooit, heb je eerst betaald."),
            ("kader", tabel(["principe", "waarom het werkt"],
                            [["<strong>maaltijden plannen</strong>", "<strong>wie weet wat hij gaat koken, koopt precies wat nodig is</strong> en gooit minder weg"],
                             ["<strong>je koelkast organiseren</strong>", "je ziet wat er staat, dus niets blijft achterin liggen"],
                             ["<strong>juiste porties serveren</strong>", "<strong>er blijft niets over</strong>; wat op het bord blijft liggen, gaat meestal de vuilnisbak in, en bijnemen kan altijd nog"],
                             ["<strong>je zintuigen gebruiken</strong>", "<strong>kijken en ruiken</strong>: veel voedsel is na de THT-datum nog prima"],
                             ["<strong>een creatieve kok zijn</strong>", "<strong>werken met restjes</strong>: van restjes groente maak je soep, van oud brood wentelteefjes"]])),
            ("p", "<strong>In het groot kopen helpt niet tegen verspilling</strong>, het leidt er juist toe als "
                  "je het niet op tijd opkrijgt. <strong>Grote porties serveren helpt evenmin.</strong> "
                  "<strong>Zonder plannen lukt het niet</strong>: maaltijden en aankopen zorgvuldig plannen "
                  "staat als eerste principe in het rijtje. <strong>Groenten die al wat langer liggen, maak je "
                  "tot soep</strong>, een ovenschotel of een wok."),
        ]),
        dict(kop="Winkelen", blokken=[
            ("p", "<strong>Je maakt een boodschappenlijst om gerichter te kopen</strong>: met een lijst koop je "
                  "wat je nodig hebt en minder wat je niet nodig hebt. <strong>Je houdt daarbij rekening met "
                  "wat je al in huis hebt, met het menu van de week en met het aantal personen.</strong>"),
            ("p", "<strong>Een koelbox houdt koude waren koel</strong> op de weg van de winkel naar huis, zodat "
                  "de koudeketen niet onderbroken wordt. <strong>Een eigen draagtas meenemen is een "
                  "milieubewuste keuze</strong>, net als <strong>seizoensgroenten kopen</strong>: groenten van "
                  "het seizoen en van dichtbij hebben minder transport en verwarming nodig, en zo weinig "
                  "mogelijk verpakking scheelt meteen afval."),
            ("p", "<strong>Economisch handelen is prijzen vergelijken, promoties gebruiken en niet te veel "
                  "kopen.</strong> <strong>Een promotie is niet altijd voordelig</strong>: drie halen, twee "
                  "betalen is geen besparing als het derde pak bederft."),
        ]),
        dict(kop="De tafel dekken", blokken=[
            ("p", "<strong>Je dekt de tafel mooi omdat het uitnodigt</strong>: een verzorgde tafel maakt van "
                  "eten een rustig en aangenaam moment, en daarom hoort het dekken bij de maaltijdzorg."),
            ("p", "<strong>Bij een gezin dek je het ontbijt of de broodlunch, de warme maaltijd en het "
                  "klassieke diner.</strong>"),
            ("fig", svg.gedektetafel(),
             "Een couvert voor een warme maaltijd. Het mes ligt rechts met de snijkant naar het bord, de vork "
             "links, het glas rechtsboven en het dessertbestek boven het bord."),
            ("kader", tabel(["onderdeel", "waar"],
                            [["<strong>het mes</strong>", "<strong>rechts van het bord</strong>, want je snijdt meestal met de rechterhand, en <strong>met de snijkant naar het bord</strong>, zodat ze niet naar je buur wijst"],
                             ["<strong>de vork</strong>", "<strong>links van het bord</strong>, tegenover het mes"],
                             ["<strong>het glas</strong>", "<strong>rechtsboven het bord</strong>, aan de kant van het mes, dus niet links"],
                             ["<strong>het dessertbestek</strong>", "<strong>boven het bord</strong>, klaar voor na de maaltijd"],
                             ["<strong>het servet</strong>", "<strong>op het bord of links ernaast</strong>, onder de vork"]])),
            ("p", "<strong>Voor een warme maaltijd dek je een bord, een mes, een vork en een glas.</strong> "
                  "<strong>Voor een ontbijt of een broodlunch volstaan een bord, een mes en een tas of "
                  "glas</strong>; een soeplepel hoort daar niet bij. <strong>Je dekt wat de maaltijd "
                  "vraagt</strong>, en niet meer: <strong>alles wat je dekt, moet je ook afwassen</strong>."),
            ("p", "<strong>Voor de gasten aanschuiven controleer je of alles proper is</strong>: propere "
                  "borden, proper bestek en een propere tafel, dat merkt iedereen meteen. <strong>Een propere "
                  "tafel, een nette schikking en een bloem of een kaars maken een tafel aantrekkelijk</strong>; "
                  "een vuile vaatdoek op tafel bederft meteen de hele indruk."),
        ]),
    ])


# ───────────────────────── 13. Interieurzorg: ruimtes, vuil en technieken
zet("interieurzorg-ruimtes-vuil-en-technieken",
    titel="Interieurzorg: ruimtes, vuil en technieken",
    onder="Wat interieurzorg omvat, de soorten ruimtes in een huis, waarvan de onderhoudsfrequentie afhangt, de soorten vuil met de techniek die erbij hoort, en de Sinner-cirkel.",
    secties=[
        dict(kop="Ruimtes en frequentie", blokken=[
            ("p", "<strong>Interieurzorg is de zorg voor de woon- en leefomgeving</strong>, en omvat "
                  "<strong>ruimtes onderhouden, voorwerpen reinigen, planten verzorgen</strong> en dieren. "
                  "Strijken hoort bij de linnenzorg."),
            ("p", "<strong>Reinigen en schoonmaken betekenen niet hetzelfde</strong>: <strong>je reinigt een "
                  "voorwerp en je maakt een ruimte schoon.</strong>"),
            ("kader", tabel(["soort ruimte", "welke"],
                            [["<strong>woonruimtes</strong>", "de woonkamer, de eetkamer"],
                             ["<strong>slaapruimtes</strong>", "de slaapkamers"],
                             ["<strong>sanitaire ruimtes</strong>", "de badkamer en het toilet"],
                             ["<strong>de keuken en de bijkeuken</strong>", "<strong>een eigen groep, geen sanitaire ruimte</strong>"],
                             ["<strong>verkeersruimtes</strong>", "<strong>de gang, de hal en de trap</strong>: je passeert er, je blijft er niet"],
                             ["<strong>bergruimtes</strong>", "<strong>de kelder</strong>, de zolder en de berging"]])),
            ("kader", tabel(["onderhoud", "wanneer"],
                            [["<strong>dagelijks</strong>", "<strong>de keuken</strong>, want waar met voedsel gewerkt wordt, is de graad van hygiëne hoog"],
                             ["<strong>periodiek</strong>", "<strong>wekelijks of maandelijks</strong>, en ook <strong>de grote schoonmaak</strong>: wat met een vaste tussenpoos terugkomt"],
                             ["<strong>specifiek</strong>", "<strong>bij een bijzondere reden</strong>, bijvoorbeeld na een feest of een ziekte"]])),
            ("p", "<strong>De onderhoudsfrequentie hangt af van het gebruiksdoel, de graad van hygiëne, de "
                  "bezettingsgraad en de poetsnorm van de bewoner.</strong> <strong>De bezettingsgraad is "
                  "hoeveel mensen er komen</strong>: hoe meer gebruik, hoe sneller vuil. <strong>De poetsnorm "
                  "is wat de bewoner proper vindt</strong>: de ene vindt een kamer al proper waar de andere "
                  "nog aan het poetsen gaat."),
            ("p", "<strong>De keuken en de sanitaire ruimtes vragen de hoogste graad van hygiëne</strong>, en "
                  "<strong>een badkamer vraagt dus vaker onderhoud dan een zolder.</strong>"),
        ]),
        dict(kop="Soorten vuil en technieken", blokken=[
            ("kader", tabel(["soort vuil", "wat het is", "welke techniek"],
                            [["<strong>droog vuil</strong>", "<strong>stof op een kast</strong>, kruimels, haren: het ligt los op het oppervlak", "<strong>droog schoonmaken</strong>"],
                             ["<strong>aangekleefd vuil</strong>", "<strong>licht gehecht</strong>, zoals een opgedroogde druppel op het aanrecht", "klam vochtig of nat"],
                             ["<strong>ingedrongen vuil</strong>", "<strong>sterk gehecht</strong>, diep in het materiaal, zoals een ingetrokken vetvlek", "nat schoonmaken, met product"],
                             ["<strong>onzichtbaar vuil</strong>", "<strong>bacteriën en virussen</strong>: je ziet het niet, maar het is er wel", "<strong>ontsmetten</strong>"]])),
            ("p", "<strong>Zichtbaar en onzichtbaar vuil zijn de twee hoofdgroepen</strong>: droog, aangekleefd "
                  "en ingedrongen vuil zijn het zichtbare. <strong>Onzichtbaar vuil is niet minder "
                  "gevaarlijk</strong>: net het vuil dat je niet ziet, de kiemen, maakt mensen ziek. Daarom "
                  "poets je ook een kraan die er proper uitziet."),
            ("p", "<strong>De vier technieken zijn droog, klam vochtig, nat schoonmaken en ontsmetten.</strong> "
                  "Opwarmen is geen schoonmaaktechniek. <strong>Klam vochtig schoonmaken doe je met een "
                  "vochtige doek</strong>, net vochtig genoeg om het vuil mee te nemen zonder het oppervlak "
                  "nat te maken. <strong>Droog vuil verwijder je niet met veel water</strong>: met water maak "
                  "je van los stof een vlek."),
            ("p", "<strong>Je ontsmet bij kans op kiemen</strong>, zoals op een snijplank of een toilet, en "
                  "<strong>pas nadat je hebt schoongemaakt</strong>: een ontsmettingsmiddel werkt niet door "
                  "een laag vuil heen."),
        ]),
        dict(kop="De Sinner-cirkel", blokken=[
            ("fig", svg.sinnercirkel(),
             "De vier factoren van de Sinner-cirkel. Samen vormen ze altijd het geheel."),
            ("p", "<strong>De vier factoren zijn tijd, chemie, temperatuur en de mechanische handeling</strong>, "
                  "dat laatste is wrijven, borstelen of draaien. <strong>Samen bepalen ze het "
                  "resultaat.</strong>"),
            ("p", "<strong>Je kan de ene factor door de andere vervangen</strong>: <strong>gebruik je minder "
                  "product, dan moet je harder wrijven</strong>, of langer laten inwerken, of warmer water "
                  "nemen. <strong>Warm water werkt beter dan koud omdat het vuil er sneller in oplost</strong>: "
                  "warmte maakt vet en vuil losser, dus je hebt minder product en minder wrijven nodig."),
            ("fig", svg.sinnercirkel(delen=[("tijd", 35), ("chemie", 10), ("temperatuur", 20),
                                            ("mechanische handeling", 35)]),
             "Dezelfde cirkel met weinig product: de drie andere factoren worden groter om het goed te maken."),
        ]),
    ])


# ───────────────────────── 14. Methodisch, veilig en duurzaam schoonmaken
zet("methodisch-veilig-en-duurzaam-schoonmaken",
    titel="Methodisch, veilig en duurzaam schoonmaken",
    onder="De werkvolgorde opruimen, schoonmaken en nazorg, de vier richtingen waarin je werkt, hoe je veilig met schoonmaakproducten omgaat, en wat duurzaam en economisch poetsen betekent.",
    secties=[
        dict(kop="De werkvolgorde", blokken=[
            ("fig", svg.stappen(["opruimen", "schoonmaken", "nazorg"]),
             "De werkvolgorde bij het onderhoud van het interieur."),
            ("p", "<strong>Je ruimt eerst op, want anders poets je rond de rommel heen.</strong> Een leeg "
                  "oppervlak maak je in één beweging schoon; rond spullen heen poetsen kost dubbel zoveel "
                  "tijd. <strong>Nazorg is het materiaal opbergen</strong>: je maakt het proper, droogt het af "
                  "en bergt het op, klaar voor de volgende keer. <strong>Nazorg is de derde en laatste "
                  "stap.</strong>"),
            ("p", "<strong>Bij een grote opruimactie bepaal je eerst de functie van de ruimte</strong>: "
                  "waarvoor dient ze? Daarna weet je wat er thuishoort. <strong>Dan kies je: houden, weggeven "
                  "of weggooien</strong>; verstoppen lost niets op. <strong>Daarna berg je op</strong>: wat je "
                  "houdt, krijgt een vaste plaats, anders ligt het er volgende week weer."),
            ("kader", tabel(["richting", "waarom"],
                            [["<strong>van boven naar beneden</strong>", "<strong>het vuil valt omlaag</strong>: wat je van de kast veegt, komt op de grond, en die doe je dus als laatste"],
                             ["<strong>van minder vuil naar vuil</strong>", "zo versleep je het vuilste vuil niet over de properste plekken"],
                             ["<strong>van droog naar nat</strong>", "eerst het droge vuil weg, dan pas water, anders maak je van stof een vlek"],
                             ["<strong>van binnen naar buiten</strong>", "zo eindig je bij de deur en loop je niet meer over wat net schoon is"]])),
            ("p", "<strong>Bij de basistaken van schoonmaken horen stof afnemen, de vloer reinigen en het "
                  "sanitair reinigen.</strong> De was sorteren hoort bij de linnenzorg."),
        ]),
        dict(kop="Veilig met producten", blokken=[
            ("p", "<strong>Bij het kiezen van een schoonmaakproduct let je op de gebruiksaanwijzing, de "
                  "gevarenpictogrammen en de veiligheidspictogrammen</strong>, en die drie staan op het "
                  "etiket. De kleur van de fles zegt niets. <strong>Je leest het etiket omdat je dan weet hoe "
                  "je het gebruikt</strong>: het geeft het gebruik, de dosering, de gevarenaanduidingen, de "
                  "gevarensymbolen en de veiligheidsaanduidingen."),
            ("p", "<strong>Twee schoonmaakproducten meng je nooit samen</strong>: dat kan een gevaarlijke "
                  "reactie geven, ook als beide apart veilig zijn. <strong>Bleekwater met een zuur product, "
                  "zoals een ontkalker, geeft chloorgas</strong>, en dat is meteen gevaarlijk om in te ademen."),
            ("kader", tabel(["situatie", "wat je doet"],
                            [["<strong>een huis met kinderen</strong>", "<strong>de producten hoog en op slot</strong> bewaren, buiten het bereik van kinderen, in de originele verpakking"],
                             ["<strong>overgieten in een drankfles</strong>", "<strong>nooit doen</strong>: zonder etiket weet niemand wat erin zit, en zo gebeuren de meeste vergiftigingen thuis"],
                             ["<strong>een bijtend product</strong>", "<strong>handschoenen dragen</strong>, en bij spatgevaar ook een veiligheidsbril"],
                             ["<strong>product op je huid</strong>", "<strong>overvloedig spoelen met lauw water</strong>; bij twijfel bel je het antigifcentrum"],
                             ["<strong>een sterk product gebruiken</strong>", "<strong>het raam openzetten en verluchten</strong>, want veel producten geven dampen af"]])),
        ]),
        dict(kop="Duurzaam en economisch", blokken=[
            ("p", "<strong>Duurzaam handel je door een product goed te doseren, een navulling te kopen en met "
                  "microvezeldoeken te werken.</strong> Elke keer nieuw materiaal kopen is net het "
                  "tegenovergestelde."),
            ("p", "<strong>Meer product gebruiken maakt niet properder</strong>: te veel product laat strepen "
                  "na, spoelt in het water en kost onnodig geld. <strong>Een navulverpakking spaart afval "
                  "uit</strong>, want je hergebruikt de fles en koopt enkel de inhoud bij. "
                  "<strong>Microvezeldoeken werken met minder product</strong>, want de vezels nemen het vuil "
                  "mechanisch mee."),
            ("p", "<strong>Een economisch product kies je door per gebruik te rekenen</strong>: een "
                  "geconcentreerd product lijkt duurder maar gaat veel langer mee. <strong>De dosering is de "
                  "hoeveelheid product die je moet gebruiken</strong>, en die staat op het etiket."),
        ]),
    ])


# ───────────────────────── 15. Zorg voor de woon- en leefomgeving
zet("zorg-voor-de-woon-en-leefomgeving",
    titel="Zorg voor de woon- en leefomgeving",
    onder="De vijf aandachtspunten van een gezonde woning, wat de binnenlucht vervuilt, welke temperatuur bij welke kamer past, het verschil tussen ventileren en verluchten, en het verzorgen van planten en dieren.",
    secties=[
        dict(kop="Wat een leefomgeving gezond maakt", blokken=[
            ("p", "Interieurzorg is meer dan poetsen. Je zorgt voor een ruimte waar mensen zich goed "
                  "voelen, en dat hangt van <strong>vijf aandachtspunten</strong> af: <strong>gezonde "
                  "lucht, een gepaste temperatuur, een goede vochtigheidsgraad, een aangenaam "
                  "geluidsniveau en geen verontreiniging</strong>. Hoe duur de meubels zijn, telt niet mee."),
            ("kader", tabel(["aandachtspunt", "waar het over gaat"],
                            [["<strong>gezonde lucht</strong>", "verse lucht die genoeg ververst wordt"],
                             ["<strong>een gepaste temperatuur</strong>", "warm genoeg om stil te zitten, koel genoeg om te slapen"],
                             ["<strong>een goede vochtigheidsgraad</strong>", "niet zo vochtig dat er schimmel groeit, niet zo droog dat je keel prikkelt"],
                             ["<strong>een aangenaam geluidsniveau</strong>", "geen aanhoudend lawaai waar je niet weg van kan"],
                             ["<strong>geen verontreiniging</strong>", "geen rook, dampen of schimmelsporen in de binnenlucht"]])),
            ("p", "<strong>Gezonde lucht is belangrijk omdat je ze de hele dag inademt.</strong> We brengen "
                  "het grootste deel van onze dag binnen door, op school, op het werk en thuis, dus de "
                  "binnenlucht bepaalt mee hoe je je voelt."),
            ("p", "<strong>Verontreiniging in huis zijn schadelijke stoffen in de binnenlucht.</strong> "
                  "Rook, dampen van producten, schimmelsporen en fijn stof hangen er rond zonder dat je ze "
                  "ziet; samen heet dat <strong>luchtverontreiniging</strong> binnenshuis. <strong>De lucht binnenshuis wordt vervuild door sigarettenrook, door dampen van "
                  "schoonmaak- en verzorgingsproducten, en door vocht en schimmel.</strong> Een open raam "
                  "doet net het omgekeerde: dat voert de vervuiling af."),
            ("weetje", "Sigarettenrook blijft niet alleen in de lucht hangen, maar ook in de gordijnen, de "
                       "zetel en het tapijt. Daarom ruik je nog dagen later dat er gerookt is."),
            ("p", "<strong>Lawaai is ongezond omdat het stress geeft.</strong> Aanhoudend geluid maakt je "
                  "prikkelbaar, je slaapt er slechter van, en als het hard genoeg is, beschadigt het op den "
                  "duur je gehoor. Een <strong>hoog geluidsniveau hoort dus niet bij een gezonde "
                  "leefomgeving</strong>; een aangenaam geluidsniveau is net een van de vijf aandachtspunten."),
        ]),
        dict(kop="Temperatuur en vocht", blokken=[
            ("p", "Niet elke kamer heeft dezelfde temperatuur nodig. Je kijkt naar wat er in die kamer "
                  "gebeurt: in een kamer waar je stilzit, moet het warmer zijn dan in een kamer waar je slaapt."),
            ("kader", tabel(["kamer", "temperatuur", "waarom"],
                            [["<strong>de woonkamer</strong>", "<strong>ongeveer twintig graden</strong>", "je zit er stil, dus je maakt zelf weinig warmte"],
                             ["<strong>de slaapkamer</strong>", "<strong>koeler dan de woonkamer</strong>", "in een koele kamer slaap je beter en dieper"],
                             ["<strong>de badkamer</strong>", "<strong>warmer dan de woonkamer</strong>", "je staat er nat en bloot, en dan koel je snel af"]])),
            ("p", "<strong>Een slaapkamer mag dus niet warmer zijn dan een woonkamer</strong>, zoals je "
                  "misschien zou denken. Het is net andersom."),
            ("p", "<strong>Bij een te hoge kamertemperatuur word je suf en moe.</strong> Te warm maakt je "
                  "loom, droogt de lucht uit en kost onnodig energie. <strong>Bij een te lage "
                  "kamertemperatuur word je sneller ziek</strong>: een koude woning geeft klachten aan de "
                  "luchtwegen, en op koude muren slaat vocht neer."),
            ("p", "<strong>De vochtigheidsgraad, of de luchtvochtigheid, is de hoeveelheid vocht in "
                  "de lucht.</strong> Ook die kan "
                  "te hoog of te laag zijn, en allebei zijn ze lastig."),
            ("kader", tabel(["het vocht", "wat je merkt"],
                            [["<strong>te veel vocht</strong>", "<strong>er groeit schimmel</strong> op de muren en in de voegen, en dat geeft klachten aan de luchtwegen"],
                             ["<strong>te weinig vocht</strong>", "<strong>je keel wordt droog</strong>; te droge lucht prikkelt ook je neus en je ogen"]])),
            ("p", "<strong>Een muur die altijd vochtig blijft, krijgt schimmel.</strong> Schimmel heeft "
                  "vocht nodig om te groeien, dus het middel ertegen is niet een product maar droge lucht: "
                  "ventileren en verluchten."),
        ]),
        dict(kop="Ventileren en verluchten", blokken=[
            ("p", "Deze twee woorden lijken op elkaar, maar ze betekenen niet hetzelfde. Het verschil zit "
                  "in de tijd: <strong>ventileren duurt altijd door, verluchten duurt enkele minuten</strong>."),
            ("kader", tabel(["", "ventileren", "verluchten"],
                            [["<strong>wat het is</strong>", "<strong>de lucht blijft voortdurend stromen</strong>", "<strong>het raam even wijd openzetten</strong>"],
                             ["<strong>hoe lang</strong>", "<strong>de hele dag door, dag en nacht</strong>", "<strong>enkele minuten</strong>"],
                             ["<strong>hoe je het doet</strong>", "met een rooster, een ventilatiesysteem of een kiepraam open", "ramen en deuren wijd open tegen elkaar"],
                             ["<strong>waarvoor</strong>", "vocht, geuren en schadelijke stoffen blijven afvoeren", "snel alle lucht in een kamer vervangen"]])),
            ("p", "<strong>Ventileren is noodzakelijk om vocht en schadelijke stoffen af te voeren.</strong> "
                  "Zonder ventilatie blijven vocht, geuren en stoffen in huis hangen, en <strong>wie nooit "
                  "verlucht, krijgt muffe, vochtige lucht</strong>, met schimmel en klachten als gevolg. "
                  "<strong>Ventileren hoeft niet alleen in de zomer</strong>: ook in de winter moet er "
                  "verse lucht binnenkomen, anders stapelt het vocht zich op. De verwarming verwarmt de "
                  "lucht wel, maar ververst ze niet."),
            ("p", "<strong>Je verlucht zeker na het douchen, na het koken en na het strijken.</strong> Die "
                  "drie brengen in korte tijd veel waterdamp in de lucht. Televisiekijken niet."),
            ("p", "<strong>Terwijl je verlucht, zet je de verwarming lager of helemaal uit</strong>, want anders stook je "
                  "rechtstreeks naar buiten. De warmte verdwijnt door het open raam, en dat kost energie en "
                  "geld. Omdat verluchten kort duurt, koelen de muren intussen niet af en is de kamer snel "
                  "weer op temperatuur."),
            ("weetje", "Kort en wijd open werkt beter dan lang op een kier. Bij een kier beweegt er weinig "
                       "lucht en koelen de muren traag af; bij een raam wijd open is de lucht in enkele "
                       "minuten vervangen terwijl de muren hun warmte houden."),
        ]),
        dict(kop="Planten en dieren", blokken=[
            ("p", "<strong>Bij de interieurzorg hoort naast poetsen ook het verzorgen van planten, het "
                  "verzorgen van dieren en het reinigen van voorwerpen.</strong> Ze staan uitdrukkelijk in "
                  "het takenpakket, want ook zij maken mee uit hoe een woning aanvoelt."),
            ("p", "<strong>Een kamerplant verzorg je door water te geven, voor genoeg licht te zorgen en "
                  "dode blaadjes weg te halen.</strong> Dat weghalen van dood blad hoort erbij, ook als de plant er verder goed bij staat. Elke dag verplanten hoort er niet bij: dat "
                  "beschadigt de wortels, en een plant verzet je hoogstens eens per jaar."),
            ("p", "<strong>Hoe vaak je water geeft, hangt van de plant af.</strong> De ene wil voortdurend "
                  "vochtige aarde, de andere droogt graag eerst helemaal op. Voel met je vinger aan de "
                  "aarde in plaats van een vast schema te volgen."),
            ("p", "<strong>Een huisdier verzorg je met dagelijks vers water en voeding</strong>, een propere "
                  "bak of kooi, en aandacht. Dat laatste is geen extra: een dier dat niets te doen heeft, "
                  "wordt onrustig of ziek."),
        ]),
    ])


# ───────────────────────── 16. Linnenzorg: sorteren, wassen en strijken
zet("linnenzorg-sorteren-wassen-en-strijken",
    titel="Linnenzorg: sorteren, wassen en strijken",
    onder="De taken van de linnenzorg, de vier vuilgraden, het verschil tussen het textieletiket en het onderhoudsetiket, de vijf groepen wassymbolen, de Sinner-cirkel, en de werkvolgorde van verzamelen tot strijken.",
    secties=[
        dict(kop="Wat linnenzorg is", blokken=[
            ("p", "<strong>Bij de linnenzorg horen het sorteren van de was, het wassen en drogen, de strijk "
                  "doen, klein verstelwerk en de was kastklaar maken.</strong> De tafel dekken hoort daar "
                  "niet bij: dat is maaltijdzorg."),
            ("p", "<strong>Klein verstelwerk</strong> is een losse knoop aanzetten, een zoom vastnaaien of "
                  "een naadje dichtmaken. Je doet het voor je iets opbergt, want een scheurtje dat je laat "
                  "liggen, wordt in de wasmachine groter."),
            ("p", "Hoe vuil een stuk is, bepaalt mee hoe je het wast. Daarvoor zijn er "
                  "<strong>vier gradaties van vuilgraad</strong>: <strong>licht bevuild, normaal bevuild, "
                  "sterk bevuild en zeer sterk bevuild</strong>. Half bevuild bestaat niet."),
            ("kader", tabel(["vuilgraad", "voorbeeld"],
                            [["<strong>licht bevuild</strong>", "een hemd dat je één dag droeg en dat alleen moet opfrissen"],
                             ["<strong>normaal bevuild</strong>", "gewoon dagelijks wasgoed: ondergoed, handdoeken, lakens"],
                             ["<strong>sterk bevuild</strong>", "<strong>een werkbroek met olie</strong>; olie en aarde dringen in de vezel"],
                             ["<strong>zeer sterk bevuild</strong>", "werkkledij uit de bouw of de keuken, met vet en modder"]])),
        ]),
        dict(kop="De etiketten lezen", blokken=[
            ("p", "In elk kledingstuk zitten twee etiketten, en ze zeggen iets heel anders. "
                  "<strong>Het textieletiket zegt uit welke stof het stuk gemaakt is</strong>: katoen, wol, "
                  "polyester. <strong>Het onderhoudsetiket, ook het wasetiket genoemd, zegt hoe je het moet "
                  "verzorgen</strong>, met "
                  "symbolen voor wassen, bleken, drogen en strijken. <strong>Ze zijn dus niet "
                  "hetzelfde.</strong>"),
            ("p", "De symbolen op het onderhoudsetiket vallen in <strong>vijf groepen onderhoudsbehandelingen</strong>: "
                  "<strong>wassen, bleken, drogen, strijken en professionele reiniging</strong>."),
            ("fig", svg.wassymbolen()),
            ("p", "<strong>Een doorstreept symbool betekent altijd dat het niet mag.</strong> Een kruis "
                  "door het strijkijzer betekent dus: dit stuk mag je niet strijken. <strong>Het getal in "
                  "het kuipje, het wasteken, is de hoogste temperatuur waarop je mag wassen</strong>; koeler mag altijd, "
                  "warmer nooit. <strong>Je mag dus niet elk kledingstuk op zestig graden wassen</strong>: "
                  "wol en zijde verdragen veel minder."),
            ("weetje", "De puntjes in het strijkijzer zeggen hoe heet het mag: één puntje voor de koelste "
                       "stand, drie voor de heetste. Een schroeiplek betekent dat je te warm stond."),
        ]),
        dict(kop="De Sinner-cirkel", blokken=[
            ("p", "<strong>Het resultaat van het wassen wordt bepaald door de Sinner-cirkel</strong>: "
                  "<strong>tijd, chemie, temperatuur en mechanische handeling</strong> samen. De cirkel is "
                  "altijd volledig. Haal je van de ene factor iets af, dan moet je het bij een andere "
                  "bijleggen, anders wordt het wasgoed minder proper."),
            ("fig", svg.sinnercirkel()),
            ("p", "<strong>Als je op een lagere temperatuur wast, heb je meer tijd nodig</strong>, of meer "
                  "product, of meer beweging. Daarom duurt een programma op dertig graden vaak langer dan "
                  "een programma op zestig: de machine vult de ontbrekende warmte aan met tijd."),
            ("kader", tabel(["de vier factoren", "een gewone was", "dezelfde was, kouder"],
                            [["<strong>temperatuur</strong>", "25 %", "<strong>10 %</strong>"],
                             ["<strong>tijd</strong>", "25 %", "<strong>40 %</strong>"],
                             ["<strong>chemie</strong>", "25 %", "<strong>30 %</strong>"],
                             ["<strong>mechanische handeling</strong>", "25 %", "<strong>20 %</strong>"],
                             ["<strong>samen</strong>", "<strong>100 %</strong>", "<strong>100 %</strong>"]])),
            ("p", "<strong>Zwaar bevuild wasgoed vraagt meer product of een hogere temperatuur</strong>, en "
                  "dat is net dezelfde redenering: meer vuil vraagt meer van minstens een van de vier factoren."),
            ("p", "<strong>Een overvolle trommel wast niet beter maar slechter.</strong> In een volle "
                  "trommel kan het wasgoed niet bewegen, en net die beweging is de mechanische handeling "
                  "van de Sinner-cirkel. <strong>Bij een overladen trommel steek je dus minder wasgoed in.</strong> Een trommel die je maar tot drie kwart vult, laat genoeg ruimte om alles te laten bewegen."),
        ]),
        dict(kop="De was doen, van begin tot eind", blokken=[
            ("p", "De was volgt een vaste werkvolgorde. <strong>Verzamelen en bewaren is de eerste "
                  "stap</strong>, en <strong>het strijken is de laatste</strong>."),
            ("fig", svg.stappen(["verzamelen|en bewaren", "sorteren", "controleren", "wassen"])),
            ("fig", svg.stappen(["drogen", "kastklaar|maken", "strijken|indien nodig"])),
            ("p", "<strong>Je sorteert wasgoed op de kleur, het soort textiel, de wastemperatuur en de "
                  "vuilgraad.</strong> Dat zijn de vier sorteercriteria; de prijs van een stuk doet er niet "
                  "toe. <strong>Op kleur sorteer je omdat kleuren afgeven</strong>: één rode sok kleurt een "
                  "hele witte was roze. <strong>Op vuilgraad sorteer je omdat het vuil overgaat</strong>: "
                  "zwaar bevuild wasgoed vuilt de rest van de lading mee."),
            ("p", "<strong>Na het sorteren komt het controleren</strong>, en dat gebeurt dus nog voor het "
                  "wassen. <strong>Je kijkt na of de zakken leeg zijn, of de ritsen dicht zijn en of er "
                  "vlekken zijn die je eerst moet behandelen.</strong> Een zakdoek of een papiertje dat "
                  "meedraait, ligt achteraf in snippers over heel de was."),
            ("p", "<strong>Het wasprogramma hangt af van het onderhoudsetiket.</strong> Dat geeft de "
                  "temperatuur en de toegelaten behandelingen, en daarop kies je het programma en het "
                  "toerental. <strong>Het toerental is de snelheid waarmee de machine het water uit de was "
                  "zwiert bij het centrifugeren.</strong> Hoe hoger het toerental, hoe droger de was uit de machine komt, maar "
                  "ook hoe meer kreuken erin zitten."),
            ("p", "<strong>Wat niet in de droogtrommel mag, hang je aan een droogrek.</strong> Wol en fijne "
                  "stoffen krimpen in de trommel, dus <strong>niet elk kledingstuk mag erin</strong>; een "
                  "doorstreept droogsymbool zegt dat meteen."),
            ("p", "<strong>De temperatuur van je strijkijzer kies je volgens het etiket.</strong> "
                  "<strong>Aan een goed gestreken stuk zie je geen kreuken, een nette vouwlijn en geen "
                  "glimplekken.</strong> Een glimplek of een schroeiplek betekent dat het strijkijzer te "
                  "heet stond voor die stof."),
        ]),
    ])

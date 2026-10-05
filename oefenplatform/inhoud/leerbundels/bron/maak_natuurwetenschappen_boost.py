# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche natuurwetenschappen van de 2de graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Er bestaan twee fiches voor
dit vak: een basisfiche voor economische en humane wetenschappen, en een
uitgebreide fiche voor moderne talen en Latijn. Alles uit de basisfiche staat
ook in de uitgebreide; deze bundels volgen dus de uitgebreide, met de extra
stukken herkenbaar in een apart kader of een aparte sectie.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De eenentwintig thema's volgen de weging van het examen: zeven over biologie,
zes over chemie, zes over fysica en twee over veilig werken en onderzoek.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/natuurwetenschappen.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-boost-doorstroom". Natuurwetenschappen bestaat
ook op ✨ Spark en op 🌍 Beyond, en daar klinken sommige thematitels bijna
gelijk.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Natuurwetenschappen"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Water en homeostase bij planten
BUNDELS["water-en-homeostase-bij-planten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Water en homeostase bij planten",
    onder="De waterhuishouding van een plant, de huidmondjes, de transportweefsels en de plantenhormonen.",
    secties=[
        dict(kop="Homeostase en het feedbacksysteem", blokken=[
            ("p", "Met <strong>homeostase</strong> bij een plant bedoelen we dat ze haar "
                  "<strong>inwendig milieu stabiel houdt terwijl de omgeving verandert</strong>. Het is "
                  "geen stilstand: er wordt voortdurend bijgestuurd."),
            ("p", "Dat bijsturen gebeurt met een <strong>feedbacksysteem</strong>: de plant gebruikt het "
                  "<strong>gevolg van een proces om dat proces zelf bij te sturen</strong>. Krijgt ze het "
                  "<strong>signaal</strong> dat ze te veel water verliest, dan "
                  "<strong>verslappen de sluitcellen en gaan de huidmondjes dicht</strong>."),
            ("p", "De <strong>omgevingsfactoren</strong> die de "
                  "<strong>waterhuishouding</strong> beïnvloeden zijn de "
                  "<strong>lichtsterkte</strong> die op de <strong>bladeren</strong> valt, de "
                  "<strong>temperatuur van de lucht</strong> rond de plant, en de "
                  "<strong>vochtigheidsgraad van de bodem en de lucht</strong>. De kleur van de "
                  "bloemblaadjes speelt daarin geen rol."),
            ("p", "De waterhuishouding bestaat uit <strong>drie stappen</strong>: "
                  "<strong>wateropname</strong>, <strong>watertransport</strong> en "
                  "<strong>transpiratie</strong>. Ze staat <strong>niet los van de fotosynthese</strong>: "
                  "langs dezelfde huidmondjes die water laten ontsnappen, moet ook het koolstofdioxide "
                  "binnen. En ze is een voorbeeld van homeostase, want de plant "
                  "<strong>stuurt opname en verlies bij zodat haar watergehalte binnen grenzen "
                  "blijft</strong>."),
        ]),
        dict(kop="Wateropname en turgor", blokken=[
            ("p", "Een plant neemt het grootste deel van haar water op met de "
                  "<strong>wortelharen</strong>, net achter de <strong>worteltop</strong>. Dat zijn lange, "
                  "dunne uitlopers van de huidcellen; ze vergroten het oppervlak waarmee de wortel opneemt. "
                  "Het water gaat naar binnen door <strong>osmose</strong>."),
            ("p", "De <strong>turgor</strong> is de <strong>druk van het vocht in de vacuole</strong>, "
                  "waardoor een plantencel <strong>stevig blijft staan</strong>. Die druk houdt een "
                  "niet-houtige plant rechtop. De <strong>celwand</strong> houdt de cel tegen als er veel "
                  "water in zit, en daarom barst een plantencel niet open in zuiver water."),
            ("p", "Een <strong>kamerplant die je een week niet begiet</strong> gaat "
                  "<strong>verwelken</strong>: de cellen <strong>verliezen hun turgor</strong> doordat de "
                  "<strong>vacuoles leeglopen</strong>. Leg je een plantencel in een sterk zoute oplossing, "
                  "dan trekt het celmembraan van de celwand weg, en dat heet "
                  "<strong>plasmolyse</strong>."),
        ]),
        dict(kop="Watertransport", blokken=[
            ("p", "Het water met de opgeloste zouten gaat van de wortel naar het blad door de "
                  "<strong>xyleemvaten</strong>, ook wel <strong>houtvaten</strong> genoemd. De suikers "
                  "uit het blad gaan naar de rest van de plant door het "
                  "<strong>floëem</strong> of de <strong>zeefvaten</strong>. "
                  "<strong>Houtvaten en zeefvaten liggen samen in vaatbundels</strong>."),
            ("p", "Water en assimilaten gaan dus <strong>niet door dezelfde vaten</strong>: elk heeft zijn "
                  "eigen transportweefsel. Het water gaat altijd naar boven, de assimilaten naar waar ze "
                  "nodig zijn, dus in twee richtingen."),
            ("p", tabel(["Kracht", "Wat ze doet"], [
                ["Worteldruk", "de druk waarmee de wortel water in de houtvaten duwt"],
                ["Transpiratiezuiging", "de zuigkracht die bovenaan ontstaat doordat er water uit de bladeren verdampt"],
                ["Capillariteit", "water kruipt vanzelf omhoog in een heel nauwe buis"],
                ["Cohesie", "de watermoleculen houden elkaar vast, zodat de kolom niet breekt"],
            ])),
            ("p", "De <strong>transpiratiezuiging</strong> is de motor van het transport. Worteldruk "
                  "alleen volstaat niet om water tot in de top van een boom te brengen."),
        ]),
        dict(kop="De huidmondjes", blokken=[
            ("p", "De <strong>huidmondjes</strong> liggen bij de meeste bladeren vooral aan de "
                  "<strong>onderkant van het blad</strong>. Elk huidmondje zit tussen twee "
                  "<strong>boonvormige sluitcellen</strong>, en die openen en sluiten het."),
            ("p", "<strong>Verliezen de sluitcellen hun turgor</strong>, dan "
                  "<strong>gaat het huidmondje dicht</strong>, <strong>daalt de verdamping</strong> door "
                  "dat blad, en wordt de <strong>opname van koolstofdioxide moeilijker</strong>. Dat is "
                  "precies de tegenstelling waarmee de plant zit: sluiten spaart water maar legt de "
                  "fotosynthese stil."),
            ("p", "Bij <strong>felle zon en grote droogte</strong> zet een plant haar huidmondjes dus "
                  "<strong>niet</strong> zo ver mogelijk open; ze sluit ze juist om water te sparen. Bij "
                  "genoeg water en veel licht gaan ze wel open."),
            ("p", "<strong>Transpiratie</strong> zorgt voor een <strong>zuigkracht die water omhoog "
                  "trekt</strong>, <strong>koelt het blad af</strong> bij warm weer, en gebeurt "
                  "<strong>vooral via de huidmondjes</strong>. Een plant verliest haar water dus niet via "
                  "de bloemen. Staat ze in <strong>heel vochtige lucht</strong>, dan "
                  "<strong>daalt</strong> haar transpiratie, want het verschil in vochtigheid met de "
                  "omgeving wordt kleiner."),
            ("p", "Bij <strong>volle fotosynthese</strong> ontsnapt er <strong>zuurstofgas</strong> door "
                  "de huidmondjes. <strong>Water verplaatst zich in de plant van de wortel naar het "
                  "blad</strong>, en nooit omgekeerd."),
            ("weetje", "Een grote boom kan op een warme dag honderden liters water verdampen. Bijna al het "
                       "water dat door de wortels binnenkomt, verlaat de plant weer als damp."),
        ]),
        dict(kop="De organen en de weefsels", blokken=[
            ("p", "Bij een plant onderscheid je <strong>vier organen</strong>: de "
                  "<strong>wortel</strong>, de <strong>stengel</strong>, het <strong>blad</strong> en de "
                  "<strong>bloem</strong>."),
            ("p", "Bij het <strong>huidweefsel</strong> horen de <strong>epidermis</strong>, de "
                  "<strong>cuticula</strong> of <strong>waslaag</strong>, en de <strong>bast</strong>. De "
                  "<strong>cuticula</strong> op een blad <strong>beperkt het waterverlies</strong>."),
            ("p", "Het <strong>vulweefsel</strong> of parenchym vult de ruimte tussen de vaten en slaat "
                  "stoffen op. In een blad bevat het <strong>wel degelijk veel bladgroenkorrels</strong>, "
                  "en juist daar gebeurt het grootste deel van de fotosynthese."),
        ]),
        dict(kop="Fotosynthese en de plantenhormonen", blokken=[
            ("p", "Voor de <strong>fotosynthese</strong> heeft een plant <strong>water</strong>, "
                  "<strong>koolstofdioxide</strong> en <strong>licht als energiebron</strong> nodig. Er "
                  "ontstaan <strong>glucose en zuurstofgas</strong>. Dat gebeurt in het organel dat "
                  "<strong>chloroplast</strong> heet."),
            ("p", "Een plant in het <strong>donker</strong> maakt dus <strong>niet</strong> even veel "
                  "glucose als een plant in het licht: zonder licht valt de fotosynthese stil. Bij "
                  "<strong>aanhoudende droogte</strong> legt een plant haar fotosynthese "
                  "<strong>grotendeels stil</strong>, want haar <strong>huidmondjes staan dicht</strong> en "
                  "er komt amper koolstofdioxide binnen."),
            ("p", "Een <strong>assimilaat</strong> is een <strong>suiker die de plant zelf maakt bij de "
                  "fotosynthese</strong>. Een <strong>fotoreceptor</strong> van een plant vangt de "
                  "<strong>prikkel licht</strong> op; daarmee merkt ze van welke kant het licht komt."),
            ("p", tabel(["Plantenhormoon", "Wat het doet"], [
                ["Auxine", "hoopt zich op aan de donkere kant en laat die kant sneller strekken"],
                ["Ethyleen", "brengt de rijping van vruchten op gang"],
                ["Abscisinezuur", "laat de huidmondjes sluiten bij droogte, helpt water sparen en speelt mee bij het verliezen van bladeren"],
            ])),
            ("p", "Daarom groeit een plant op de <strong>vensterbank duidelijk naar het raam toe</strong>: "
                  "het <strong>auxine</strong> hoopt zich op aan de <strong>donkere kant</strong> en laat "
                  "die kant <strong>sneller strekken</strong>, waardoor de stengel naar het licht buigt."),
        ]),
    ],
    onthoud=[
        "Homeostase: de plant houdt haar inwendig milieu stabiel terwijl de omgeving verandert.",
        "De waterhuishouding bestaat uit wateropname, watertransport en transpiratie.",
        "Wortelharen nemen water op door osmose; de turgor is de druk van het vocht in de vacuole.",
        "Water gaat door de xyleemvaten of houtvaten, suikers door het floëem of de zeefvaten.",
        "De transpiratiezuiging is de motor van het watertransport.",
        "Verliezen de sluitcellen hun turgor, dan gaat het huidmondje dicht en daalt de verdamping.",
        "Een plant heeft vier organen: wortel, stengel, blad en bloem.",
        "Fotosynthese: water, koolstofdioxide en licht geven glucose en zuurstofgas, in de chloroplast.",
        "Auxine hoopt zich op aan de donkere kant; ethyleen laat vruchten rijpen; abscisinezuur sluit de huidmondjes.",
    ],
)

# ───────────────────────── 2. Van prikkel tot reactie, en het oog
BUNDELS["van-prikkel-tot-reactie-en-het-oog-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Van prikkel tot reactie, en het oog",
    onder="De weg van prikkel naar reactie, de zintuigen, de bouw van het oog, en hoe een plant reageert.",
    secties=[
        dict(kop="De weg van prikkel tot reactie", blokken=[
            ("p", "De weg loopt altijd in dezelfde <strong>volgorde</strong>: "
                  "<strong>prikkel, receptor, conductor, effector</strong>, en dan de "
                  "<strong>reactie</strong>."),
            ("p", tabel(["Schakel", "Wat het doet", "Voorbeeld"], [
                ["Receptor", "vangt een prikkel op en zet hem om in een signaal", "een staafje in je oog"],
                ["Conductor", "geeft het signaal van de receptor naar de effector door", "een zenuw, het ruggenmerg, de hersenen"],
                ["Effector", "voert de reactie uit", "een spier of een klier"],
            ])),
            ("p", "Een <strong>uitwendige prikkel</strong> komt van buiten je lichaam: het "
                  "<strong>geluid van een toeterende auto</strong>, het <strong>licht van een felle "
                  "lamp</strong>, de <strong>kou van een ijskoude wind</strong>. Een "
                  "<strong>inwendige prikkel</strong> komt van binnen: <strong>dorst</strong> en "
                  "<strong>stress</strong>."),
            ("p", "Bij de mens <strong>verwerken de hersenen de binnenkomende signalen</strong> en "
                  "<strong>bepalen ze welke reactie volgt</strong>. Trek je je hand weg van een hete pan "
                  "nog voor je het beseft, dan is de <strong>effector de spier in je arm die "
                  "samentrekt</strong>."),
            ("p", "Een <strong>receptor is meestal maar voor één soort prikkel gevoelig</strong>. Zo weet "
                  "het lichaam <strong>meteen welke prikkel er binnenkomt</strong>."),
        ]),
        dict(kop="De zintuigen", blokken=[
            ("p", tabel(["Receptor", "Zintuig"], [
                ["Staafjes en kegeltjes", "het zicht"],
                ["Haarcellen in het oor", "het gehoor"],
                ["Zintuigcellen op de tong", "de smaakzin"],
                ["Zintuigcellen in de neus", "de reukzin"],
                ["Mechanoreceptoren in de huid", "de tastzin"],
            ])),
            ("p", "Ruik je dat er <strong>brood in de oven</strong> staat, dan gebruik je de "
                  "<strong>reukzin</strong>. <strong>Smaak en geur werken samen</strong>: wie "
                  "<strong>verkouden</strong> is, <strong>proeft minder</strong>."),
            ("p", "<strong>Mechanoreceptoren</strong> reageren op druk, trek en beweging. Een plant vangt "
                  "<strong>licht</strong> dus <strong>niet</strong> op met mechanoreceptoren, maar met een "
                  "<strong>fotoreceptor</strong>."),
        ]),
        dict(kop="Hoe een plant reageert", blokken=[
            ("p", "Een <strong>tropie</strong> is een <strong>groeibeweging in de richting van de prikkel "
                  "of er net van weg</strong>. Groeit een wortel <strong>naar beneden, de zwaartekracht "
                  "achterna</strong>, dan heet dat <strong>geotropie</strong>."),
            ("p", "Een <strong>nastie</strong> is een <strong>plantenbeweging waarvan de richting niet "
                  "door de richting van de prikkel bepaald wordt</strong>: een tulp die bij koude "
                  "dichtgaat."),
            ("p", "Het grote verschil tussen een plant en een dier: een "
                  "<strong>plant reageert traag met groei of beweging van delen</strong>, een "
                  "<strong>dier snel met spieren</strong>. Een prikkel leidt bij een plant dus "
                  "<strong>niet</strong> altijd tot een reactie die je binnen enkele seconden ziet."),
            ("p", "<strong>Plantenhormonen</strong> <strong>sturen de strekking van cellen in de "
                  "stengel</strong>, <strong>spelen mee bij de vorming van bijwortels en "
                  "zijscheuten</strong>, en <strong>regelen het rijpen van vruchten</strong>."),
            ("p", "<strong>Auxine</strong> hoopt zich op aan de <strong>donkere</strong> kant van de "
                  "stengel, dus niet aan de kant waar het licht op valt. Die donkere kant strekt sneller, "
                  "en daardoor buigt de stengel naar het licht toe."),
        ]),
        dict(kop="De bouw van het oog", blokken=[
            ("p", "De <strong>wand van de oogbol</strong> bestaat uit <strong>drie lagen</strong>, van "
                  "buiten naar binnen: het <strong>hard oogvlies</strong>, het "
                  "<strong>vaatvlies</strong> en het <strong>netvlies</strong>. Het "
                  "<strong>hoornvlies</strong> is het <strong>doorzichtige voorste deel van het harde "
                  "oogvlies</strong>."),
            ("p", "Bij het <strong>vaatvlies</strong> horen het <strong>straallichaam</strong>, de "
                  "<strong>iris met haar spieren</strong> en de <strong>lensbanden</strong>. De "
                  "<strong>iris</strong> regelt de <strong>hoeveelheid licht die door de pupil "
                  "binnenkomt</strong>; de <strong>pupil</strong> is de <strong>opening in het midden van "
                  "de iris</strong>."),
            ("p", "Het <strong>glasachtig lichaam</strong> is de <strong>doorzichtige gelei die de oogbol "
                  "vult en in vorm houdt</strong>. De <strong>voorste oogkamer</strong> ligt vóór de "
                  "ooglens en de <strong>achterste</strong> erachter, dus niet beide achter de lens."),
            ("p", "De <strong>oogzenuw</strong> brengt de signalen van het netvlies naar de hersenen."),
        ]),
        dict(kop="Het netvlies en het zien", blokken=[
            ("p", "<strong>Staafjes werken ook bij weinig licht</strong> maar zien geen kleur; "
                  "<strong>kegeltjes zorgen voor het zien van kleur</strong> en hebben veel licht nodig. "
                  "<strong>Beide liggen in het netvlies</strong>."),
            ("p", "De <strong>gele vlek</strong> is de plek op het netvlies waar je het "
                  "<strong>scherpst ziet</strong>. Op de <strong>blinde vlek</strong> zie je niets, want "
                  "daar <strong>verlaat de oogzenuw het oog</strong> en liggen er "
                  "<strong>geen lichtreceptoren</strong>."),
            ("p", "De <strong>bipolaire cellen</strong> en de <strong>ganglioncellen</strong> geven het "
                  "signaal van de <strong>lichtreceptoren</strong> door naar de oogzenuw. De "
                  "<strong>pigmentcellen</strong> achteraan in het netvlies <strong>slikken het licht dat "
                  "er doorheen gaat</strong>, zodat er niets weerkaatst."),
            ("p", "Het beeld dat op het netvlies valt, staat <strong>op zijn kop</strong> en niet rechtop. "
                  "En het <strong>netvlies levert het beeld niet helemaal af</strong>: de "
                  "<strong>hersenen verwerken het nog</strong>, draaien het om en vullen aan."),
            ("p", "Kom je <strong>uit het felle zonlicht een donkere kelder binnen</strong>, dan "
                  "<strong>wordt de pupil groter</strong>, <strong>nemen de staafjes het werk over van de "
                  "kegeltjes</strong>, en <strong>zie je eerst bijna geen kleuren meer</strong>."),
        ]),
        dict(kop="Accommodatie, bijziend en verziend", blokken=[
            ("p", "Bij <strong>accommodatie verandert de ooglens van vorm zodat het beeld scherp "
                  "wordt</strong>. Kijk je van ver weg naar iets <strong>vlakbij</strong>, dan wordt de "
                  "ooglens <strong>boller</strong>; voor ver weg wordt ze platter."),
            ("p", "Bij <strong>bijziendheid</strong> valt het <strong>beeld van veraf vóór het "
                  "netvlies</strong>, en een <strong>holle lens</strong> zet het scherp. Bij "
                  "<strong>verziendheid</strong> valt het erachter, en daar helpt een "
                  "<strong>bolle lens</strong>."),
            ("weetje", "Je blinde vlek merk je nooit op, omdat je hersenen het ontbrekende stukje "
                       "aanvullen met wat eromheen te zien is."),
        ]),
    ],
    onthoud=[
        "De volgorde is altijd: prikkel, receptor, conductor, effector, reactie.",
        "Een receptor is meestal maar voor één soort prikkel gevoelig.",
        "Smaak en geur werken samen: wie verkouden is, proeft minder.",
        "Een tropie groeit naar de prikkel toe of ervan weg; bij een nastie bepaalt de prikkel de richting niet.",
        "De wand van de oogbol, van buiten naar binnen: hard oogvlies, vaatvlies, netvlies.",
        "De iris regelt de hoeveelheid licht die door de pupil binnenkomt.",
        "Staafjes werken ook bij weinig licht, kegeltjes zorgen voor het zien van kleur.",
        "Op de gele vlek zie je het scherpst, op de blinde vlek zie je niets.",
        "Bijziend: beeld vóór het netvlies, holle lens. Verziend: beeld erachter, bolle lens.",
    ],
)

# ───────────────────────── 3. Het zenuwstelsel
BUNDELS["het-zenuwstelsel-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het zenuwstelsel",
    onder="De indeling van het zenuwstelsel, de bouw van een neuron, de actiepotentiaal, de synaps en de reflexen.",
    secties=[
        dict(kop="De indeling", blokken=[
            ("p", "Het <strong>centrale zenuwstelsel</strong> bestaat uit twee delen: de "
                  "<strong>hersenen</strong> en het <strong>ruggenmerg</strong>. Bij het "
                  "<strong>perifere zenuwstelsel</strong> horen de "
                  "<strong>hersenzenuwen</strong>, de <strong>ruggenmergzenuwen</strong> en de "
                  "<strong>grensstrengen</strong>."),
            ("p", "Een <strong>zenuw</strong> is <strong>een bundel uitlopers van veel zenuwcellen "
                  "samen</strong>. Een <strong>gemengde zenuw</strong> bevat "
                  "<strong>zowel sensorische als motorische vezels</strong>, dus niet alleen motorische."),
            ("p", "Het <strong>animale zenuwstelsel</strong> stuurt "
                  "<strong>bewegingen aan waarover je zelf beslist</strong>. Het "
                  "<strong>autonome</strong> deel doet de rest, en daar horen de "
                  "<strong>grensstrengen</strong> links en rechts van de wervelkolom bij, dus "
                  "<strong>niet</strong> bij het animale deel."),
            ("p", tabel(["Tak van het autonome stelsel", "Wat ze doet"], [
                ["Sympathisch zenuwstelsel", "zet het lichaam klaar voor inspanning of gevaar"],
                ["Parasympathisch zenuwstelsel", "vertraagt de hartslag en bevordert de spijsvertering"],
            ])),
            ("p", "Over het <strong>ruggenmerg</strong>: het <strong>ligt beschermd in het "
                  "wervelkanaal</strong>, het <strong>hoort bij het centrale zenuwstelsel</strong>, en "
                  "het <strong>kan zelf een reflex afhandelen zonder de hersenen</strong>."),
        ]),
        dict(kop="Het neuron", blokken=[
            ("p", "Bij een <strong>neuron</strong> horen de <strong>dendrieten</strong>, het "
                  "<strong>axon</strong> en het <strong>cellichaam met de celkern</strong>. De "
                  "<strong>dendrieten vangen signalen op en het axon geeft ze door</strong>. De "
                  "<strong>celkern ligt in het cellichaam</strong>, niet in het axon."),
            ("p", tabel(["Soort neuron", "Wat het doet"], [
                ["Sensorisch neuron", "brengt een signaal van een zintuig naar het centrale zenuwstelsel"],
                ["Motorisch neuron", "brengt een bevel naar een effector"],
                ["Schakelneuron", "verbindt de twee, en ligt meestal in het ruggenmerg of in de hersenen"],
            ])),
            ("p", "De <strong>effectoren</strong> waar een motorisch neuron naartoe gaat, zijn een "
                  "<strong>spier</strong>, een <strong>klier</strong> of het "
                  "<strong>hartspierweefsel</strong>."),
            ("p", "De <strong>myelineschede</strong> rond een axon <strong>isoleert het axon zodat de "
                  "impuls er sneller over gaat</strong>. De onderbreking waar de impuls als het ware "
                  "naartoe springt, is de <strong>knoop van Ranvier</strong>. Buiten het centrale "
                  "zenuwstelsel maken de <strong>cellen van Schwann</strong> die schede."),
            ("p", "Een <strong>gemyeliniseerde zenuwvezel</strong> is daardoor "
                  "<strong>sneller</strong>: de impuls <strong>springt van knoop tot knoop in plaats van "
                  "over de hele lengte te lopen</strong>."),
            ("p", "Het <strong>eindknopje</strong> is het <strong>uiteinde van een axon waar de "
                  "neurotransmitter vrijkomt</strong>."),
        ]),
        dict(kop="Rustpotentiaal en actiepotentiaal", blokken=[
            ("kader", "<p>Dit stuk staat enkel in de uitgebreide fiche, dus voor moderne talen en "
                      "Latijn.</p>"),
            ("p", "De <strong>rustpotentiaal</strong> is het <strong>spanningsverschil over het membraan "
                  "als er geen impuls is</strong>: binnen is het negatief tegenover buiten, ongeveer min 70 "
                  "millivolt."),
            ("p", "De stappen van een <strong>actiepotentiaal</strong> in orde: "
                  "<strong>rustpotentiaal, depolarisatie, repolarisatie, herstelfase</strong>. "
                  "<strong>Depolarisatie</strong> betekent dat het <strong>spanningsverschil over het "
                  "membraan kortstondig omslaat</strong>."),
            ("p", "Een <strong>prikkel onder de drempelwaarde levert geen impuls op</strong>. Wordt een "
                  "prikkel <strong>twee keer zo sterk</strong>, dan volgen er in één zenuwvezel "
                  "<strong>meer impulsen per seconde, elk even groot</strong>: de "
                  "<strong>amplitude van een actiepotentiaal wordt dus niet groter</strong> bij een "
                  "sterkere prikkel."),
            ("p", "<strong>Na een impuls is een neuron even niet in staat om opnieuw te vuren</strong>; "
                  "dat is de herstelfase. Daarom kan een zenuw niet onbeperkt snel achter elkaar vuren."),
        ]),
        dict(kop="De synaps", blokken=[
            ("p", "De <strong>synaptische spleet</strong> is de <strong>smalle ruimte tussen het "
                  "eindknopje van het ene neuron en het volgende neuron</strong>. De "
                  "<strong>neurotransmitter</strong> is de <strong>stof die daar vrijkomt om het signaal "
                  "over te dragen</strong>."),
            ("p", "In een <strong>synaps</strong> gebeurt dit: de <strong>impuls laat blaasjes met "
                  "neurotransmitter leeglopen</strong>, de <strong>neurotransmitter past op "
                  "membraanreceptoren aan de overkant</strong>, en het "
                  "<strong>signaal gaat er maar in één richting over</strong>. Dat laatste komt doordat "
                  "<strong>alleen het eindknopje blaasjes heeft en alleen de overkant receptoren</strong>."),
            ("p", "Een neurotransmitter werkt volgens het <strong>sleutel-slotprincipe</strong>: hij past "
                  "<strong>maar op bepaalde receptoren</strong>. En de impulsoverdracht is daarom "
                  "<strong>geen zuiver elektrisch proces</strong>: binnen een neuron is ze elektrisch, in "
                  "de synaps chemisch."),
            ("weetje", "Veel geneesmiddelen en drugs werken precies op die synaps: ze bootsen een "
                       "neurotransmitter na, of ze beletten dat hij weer opgeruimd wordt."),
        ]),
        dict(kop="Reflexen", blokken=[
            ("p", "Een <strong>terugtrekreflex</strong> legt deze weg af: "
                  "<strong>receptor, sensorisch neuron, schakelneuron in het ruggenmerg, motorisch neuron, "
                  "spier</strong>. De hele weg van receptor tot effector heet de "
                  "<strong>reflexboog</strong>."),
            ("p", "<strong>Reflexen</strong> zijn onder andere de <strong>pupilreflex bij fel "
                  "licht</strong>, de <strong>kniepeesreflex bij een tik onder de knieschijf</strong> en "
                  "het <strong>terugtrekken van je hand bij hitte</strong>. Een reflex is nuttig omdat het "
                  "<strong>lichaam op gevaar reageert nog voor je erover nadenkt</strong>."),
            ("p", "Je <strong>voelt pas pijn nadat je je hand al hebt weggetrokken</strong>: de "
                  "<strong>reflex loopt via het ruggenmerg</strong>, en het "
                  "<strong>pijnsignaal moet nog naar de hersenen</strong>. Bij een "
                  "<strong>gewilde beweging komen de grote hersenen er juist wel aan te pas</strong>."),
            ("p", "De <strong>toeschietreflex</strong> is het <strong>vrijkomen van melk uit de melkklier "
                  "wanneer de baby zuigt</strong>. Ook daar is de effector een klier en geen spier."),
        ]),
    ],
    onthoud=[
        "Het centrale zenuwstelsel bestaat uit de hersenen en het ruggenmerg.",
        "Het animale zenuwstelsel stuurt bewegingen waarover je zelf beslist; het autonome doet de rest.",
        "Dendrieten vangen signalen op, het axon geeft ze door.",
        "De myelineschede isoleert het axon; de impuls springt van knoop tot knoop van Ranvier.",
        "De rustpotentiaal is ongeveer min 70 millivolt: binnen negatief tegenover buiten.",
        "Een sterkere prikkel geeft meer impulsen per seconde, geen grotere amplitude.",
        "In een synaps gaat het signaal chemisch over, en maar in één richting.",
        "Reflexboog: receptor, sensorisch neuron, schakelneuron in het ruggenmerg, motorisch neuron, spier.",
    ],
)

# ───────────────────────── 4. Spieren, klieren en hormonen
BUNDELS["spieren-klieren-en-hormonen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Spieren, klieren en hormonen",
    onder="De drie soorten spierweefsel, de bouw van een spier, de klieren en de regeling van je bloedsuiker.",
    secties=[
        dict(kop="De drie soorten spierweefsel", blokken=[
            ("p", "Er zijn drie soorten: <strong>dwarsgestreept spierweefsel</strong>, "
                  "<strong>glad spierweefsel</strong> en <strong>hartspierweefsel</strong>."),
            ("p", "<strong>Willekeurige</strong> spieren, dus onder je wil, zijn bijvoorbeeld de "
                  "<strong>spier die je arm buigt</strong>, de <strong>spier die je been strekt</strong> en "
                  "de <strong>kauwspier in je kaak</strong>. Het "
                  "<strong>hartspierweefsel werkt onwillekeurig</strong>, ook al is het dwarsgestreept."),
            ("p", "Over <strong>glad spierweefsel</strong>: het <strong>ligt in de wand van organen en "
                  "bloedvaten</strong>, het <strong>werkt onwillekeurig</strong>, en het "
                  "<strong>trekt trager samen dan een skeletspier</strong>."),
            ("p", "Een <strong>spier kan niet duwen</strong>, alleen trekken: samentrekken en daarna weer "
                  "verslappen. Daarom werken spieren in paren. De <strong>agonist</strong> is de spier die "
                  "<strong>de beweging uitvoert</strong>, tegenover haar tegenspeler. Dat "
                  "<strong>de biceps en de triceps elkaars antagonist</strong> zijn, betekent dat "
                  "<strong>wanneer de ene samentrekt, de andere ontspant</strong>."),
        ]),
        dict(kop="De bouw van een spier", blokken=[
            ("p", "Van groot naar klein: <strong>spierbuik, spierbundel, spiervezel, "
                  "spierfibril</strong>. Een <strong>spiervezel heeft meer dan één celkern</strong>; ze "
                  "ontstaat doordat veel cellen samensmelten. Het "
                  "<strong>celmembraan van een spiervezel</strong> heet het "
                  "<strong>sarcolemma</strong>."),
            ("p", "Bij de <strong>microscopische bouw</strong> van een dwarsgestreepte spier horen de "
                  "<strong>Z-plaat</strong>, het <strong>actinefilament</strong> en het "
                  "<strong>myosinefilament</strong>. Het stukje spierfibril "
                  "<strong>tussen twee Z-platen</strong> is het <strong>sarcomeer</strong>, de "
                  "<strong>functionele eenheid</strong> van de spier."),
            ("p", "Trekt de spier samen, dan <strong>schuiven de actinefilamenten tussen de "
                  "myosinefilamenten</strong> en <strong>komen de Z-platen dichterbij</strong>. De "
                  "<strong>donkere banden</strong> in een dwarsgestreepte spier danken hun naam aan het "
                  "<strong>myosine</strong> dat daar ligt."),
            ("p", "Het bevel om samen te trekken komt aan doordat een "
                  "<strong>motorisch neuron via de motorische eindplaat een neurotransmitter "
                  "afgeeft</strong>. De <strong>motorische eindplaat</strong> is de plek waar het uiteinde "
                  "van een motorisch neuron op een spiervezel aankomt. Een "
                  "<strong>motorische eenheid</strong> is <strong>één motorisch neuron met alle "
                  "spiervezels die het aanstuurt</strong>."),
            ("p", "De <strong>spierspoeltjes meten hoe ver een spier uitgerekt is</strong>; op die "
                  "informatie werkt onder andere de kniepeesreflex."),
            ("p", "Een spier haalt haar energie <strong>uit de afbraak van glycogeen en glucose in de "
                  "spiervezel</strong>. Daarom heeft spierweefsel <strong>veel bloedvaten</strong> nodig: "
                  "het <strong>bloed brengt zuurstof en voedingsstoffen aan en voert afvalstoffen "
                  "af</strong>."),
        ]),
        dict(kop="Klieren", blokken=[
            ("p", "Het verschil: een <strong>endocriene klier geeft haar stof af aan het bloed</strong>, "
                  "een <strong>exocriene via een afvoerbuis</strong>. Een exocriene klier geeft haar "
                  "product dus <strong>niet</strong> rechtstreeks aan het bloed af."),
            ("p", "<strong>Exocriene klieren</strong> zijn onder andere de "
                  "<strong>traanklier</strong>, de <strong>zweetklier</strong> en de "
                  "<strong>talgklier</strong>. De <strong>alvleesklier is een gemengde klier</strong>: ze "
                  "geeft spijsverteringssappen af via een afvoerbuis én hormonen aan het bloed. De "
                  "<strong>thymus is geen exocriene klier</strong>; hij speelt een rol bij de afweer."),
            ("p", "Een <strong>klier is altijd een effector</strong>: ze voert een reactie uit nadat ze "
                  "een signaal kreeg."),
            ("p", tabel(["Klier", "Hormoon"], [
                ["Schildklier", "thyroxine"],
                ["Hypofyse", "onder andere het schildklierstimulerend hormoon"],
                ["Bijnier", "adrenaline en cortisol"],
                ["Alvleesklier", "insuline en glucagon"],
            ])),
            ("p", "De <strong>hypofyse</strong> is de klier <strong>onderaan de hersenen die veel andere "
                  "klieren aanstuurt</strong>. Het <strong>doelorgaan van het schildklierstimulerend "
                  "hormoon</strong> is de <strong>schildklier</strong>."),
        ]),
        dict(kop="Hoe hormonen werken", blokken=[
            ("p", "Het <strong>sleutel-slotprincipe</strong> bij hormonen betekent dat een "
                  "<strong>hormoon alleen op de membraanreceptor van zijn doelwitcel past</strong>. De "
                  "<strong>doelwitcel</strong> is dus de cel waarop een bepaald hormoon werkt. Een hormoon "
                  "komt met het bloed overal, maar werkt alleen daar."),
            ("p", "<strong>Hormonen werken trager dan zenuwen</strong>, maar hun effect houdt langer aan. "
                  "Zenuwen werken snel en gericht."),
            ("p", "<strong>Adrenaline</strong> bij <strong>stress</strong>: de "
                  "<strong>hartslag versnelt</strong>, er komt <strong>extra glucose vrij in het "
                  "bloed</strong>, en het <strong>lichaam wordt klaargezet voor inspanning</strong>. "
                  "<strong>Cortisol</strong> komt uit de <strong>bijnier</strong>."),
        ]),
        dict(kop="De regeling van je bloedsuiker", blokken=[
            ("p", "De <strong>bètacellen</strong> in de <strong>eilandjes van Langerhans</strong> maken "
                  "<strong>insuline</strong>. Stijgt je <strong>glucosegehalte na een maaltijd</strong>, "
                  "dan <strong>geven de bètacellen insuline af</strong>, <strong>slaat de lever glucose op "
                  "als glycogeen</strong>, en <strong>nemen de lichaamscellen meer glucose op</strong>."),
            ("p", "Wordt je glucosegehalte <strong>te laag</strong>, dan laat "
                  "<strong>glucagon de lever glycogeen afbreken</strong>. Zo wordt het "
                  "<strong>glucosegehalte in het bloed met een feedbacksysteem geregeld</strong>."),
            ("p", "Bij <strong>diabetes type 1</strong> <strong>maakt het lichaam zelf geen of te weinig "
                  "insuline meer aan</strong>. Iemand met <strong>onbehandelde diabetes</strong> heeft "
                  "vaak <strong>dorst en plast veel</strong>, omdat de "
                  "<strong>nieren de overtollige glucose afvoeren en daarbij veel water "
                  "meenemen</strong>."),
            ("weetje", "Insuline werd in 1921 voor het eerst uit een alvleesklier gezuiverd. Tot dan was "
                       "diabetes type 1 bij kinderen zo goed als altijd dodelijk."),
        ]),
    ],
    onthoud=[
        "Drie soorten spierweefsel: dwarsgestreept, glad en hartspierweefsel.",
        "Een spier kan niet duwen, alleen trekken; daarom werken spieren in paren.",
        "Van groot naar klein: spierbuik, spierbundel, spiervezel, spierfibril.",
        "Het sarcomeer ligt tussen twee Z-platen en is de functionele eenheid van de spier.",
        "Een endocriene klier geeft haar stof af aan het bloed, een exocriene via een afvoerbuis.",
        "Een hormoon past alleen op de membraanreceptor van zijn doelwitcel.",
        "Hormonen werken trager dan zenuwen, maar hun effect houdt langer aan.",
        "Stijgt het glucosegehalte, dan geven de bètacellen insuline af.",
        "Is het glucosegehalte te laag, dan laat glucagon de lever glycogeen afbreken.",
    ],
)

# ───────────────────────── 5. Voortplanting en de hormonale regeling
BUNDELS["voortplanting-en-de-hormonale-regeling-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Voortplanting en de hormonale regeling",
    onder="De twee voortplantingsstelsels, de menstruatiecyclus en het feedbacksysteem dat beide regelt.",
    secties=[
        dict(kop="Het vrouwelijk voortplantingsstelsel", blokken=[
            ("p", "Bij het <strong>vrouwelijk voortplantingsstelsel</strong> horen de "
                  "<strong>eierstok</strong>, de <strong>eileider met de eitrechter</strong> en de "
                  "<strong>baarmoeder</strong>. De <strong>bijbal</strong> hoort er niet bij, die is "
                  "van de man."),
            ("p", "Een <strong>eicel rijpt in een follikel in de eierstok</strong>. Het vrijkomen van "
                  "die eicel, rond het midden van de cyclus, is de <strong>eisprong</strong>. De eicel "
                  "wordt daarna <strong>niet</strong> door de baarmoeder opgevangen maar door de "
                  "<strong>eitrechter</strong>, en de <strong>bevruchting vindt normaal in de eileider "
                  "plaats</strong>."),
            ("p", "Uit de follikel ontstaat na de eisprong het <strong>geel lichaam</strong>. Dat maakt "
                  "vooral <strong>progesteron</strong> aan."),
            ("p", "De cel die ontstaat als een <strong>zaadcel en een eicel versmelten</strong>, heet de "
                  "<strong>zygote</strong>; dat versmelten zelf is de <strong>bevruchting</strong>."),
        ]),
        dict(kop="De menstruatiecyclus", blokken=[
            ("p", "De <strong>menstruatiecyclus begint op de eerste dag van de menstruatie</strong> en "
                  "duurt gemiddeld <strong>ongeveer 28 dagen</strong>."),
            ("p", tabel(["Wanneer", "Wat er gebeurt"], [
                ["Eerste helft", "het baarmoederslijmvlies wordt dikker en beter doorbloed"],
                ["Rond dag 14", "de eisprong; de lichaamstemperatuur ligt daarna gemiddeld iets hoger"],
                ["Tweede helft", "het geel lichaam houdt met progesteron het slijmvlies in stand"],
                ["Geen bevruchting", "het geel lichaam valt weg, het slijmvlies laat los"],
            ])),
            ("p", "De <strong>vruchtbare periode</strong> ligt <strong>in de dagen rond de "
                  "eisprong</strong>, niet de hele cyclus even sterk."),
            ("p", "Wordt de eicel <strong>niet bevrucht</strong>, dan <strong>valt het geel lichaam na "
                  "een tiental dagen weg</strong>, <strong>daalt het gehalte progesteron</strong> en "
                  "<strong>laat het baarmoederslijmvlies los, zodat de menstruatie begint</strong>. Dat "
                  "komt zo: <strong>zonder progesteron kan het dikke slijmvlies niet in stand "
                  "blijven</strong>."),
        ]),
        dict(kop="De hormonen van de cyclus", blokken=[
            ("p", "In de hormonale regeling van de cyclus spelen drie klieren mee: de "
                  "<strong>hypothalamus</strong>, de <strong>hypofyse</strong> en de "
                  "<strong>eierstok</strong>. De <strong>hypofyse ligt in de buurt van de hypothalamus, "
                  "onderaan de hersenen</strong>. De schildklier staat erbuiten."),
            ("p", tabel(["Hormoon", "Waar het vandaan komt", "Wat het doet"], [
                ["GnRH", "hypothalamus", "zet de hypofyse aan om FSH en LH te maken"],
                ["FSH", "hypofyse", "laat de follikel in de eierstok rijpen"],
                ["LH", "hypofyse", "een plotse piek brengt de eisprong op gang"],
                ["Oestrogeen", "eierstok", "laat het slijmvlies in de eerste helft aangroeien"],
                ["Progesteron", "geel lichaam", "houdt het slijmvlies in de tweede helft in stand"],
            ])),
            ("p", "<strong>Oestrogeen wordt dus niet door de hypofyse gemaakt</strong> maar door de "
                  "eierstok."),
        ]),
        dict(kop="Het mannelijk voortplantingsstelsel", blokken=[
            ("p", "Bij het <strong>mannelijk voortplantingsstelsel</strong> horen de "
                  "<strong>teelbal</strong>, de <strong>bijbal</strong> en de "
                  "<strong>zaadleider</strong>; de eitrechter hoort er niet bij. "
                  "<strong>Zaadcellen worden in de teelballen gevormd</strong>, en de "
                  "<strong>bijbal laat ze rijpen en bewaart ze</strong>."),
            ("p", "De <strong>teelballen liggen buiten de buikholte</strong> omdat de "
                  "<strong>zaadcelvorming beter verloopt bij een iets lagere temperatuur</strong>."),
            ("p", "Een <strong>zaadcel is klein en beweegt zich met een zweepstaart</strong>. De "
                  "<strong>zaadcelvorming verloopt doorlopend</strong>, dus "
                  "<strong>niet</strong> in cycli van ongeveer achtentwintig dagen zoals bij de vrouw."),
            ("p", tabel(["Cellen in de teelbal", "Wat ze doen"], [
                ["Cellen van Leydig", "maken testosteron aan"],
                ["Cellen van Sertoli", "voeden en begeleiden de rijpende zaadcellen"],
            ])),
            ("p", "Naast de zaadcelvorming zorgt <strong>testosteron voor de ontwikkeling van de "
                  "secundaire geslachtskenmerken</strong>."),
            ("p", "Bij de man stuurt <strong>LH de cellen van Leydig aan</strong> en <strong>FSH de "
                  "cellen van Sertoli</strong>; <strong>FSH stuurt dus niet vooral de cellen van Leydig "
                  "aan</strong>. Het hormoon dat de <strong>afgifte van FSH remt</strong>, is "
                  "<strong>inhibine</strong>; <strong>inhibine stimuleert de hypofyse dus niet</strong> "
                  "om meer FSH te maken."),
            ("p", "<strong>GnRH, FSH en LH</strong> spelen <strong>bij zowel man als vrouw</strong> een "
                  "rol; <strong>progesteron</strong> niet."),
        ]),
        dict(kop="Feedback", blokken=[
            ("p", "We noemen de regeling van de cyclus een <strong>feedbacksysteem</strong> omdat de "
                  "<strong>hormonen uit de eierstok de hypothalamus en de hypofyse op hun beurt "
                  "bijsturen</strong>. Zo'n systeem <strong>kan zowel remmen als stimuleren</strong>."),
            ("p", "Wordt bij de man het <strong>testosterongehalte te hoog</strong>, dan "
                  "<strong>geeft de hypothalamus minder GnRH af</strong>, <strong>geeft de hypofyse "
                  "minder LH af</strong> en <strong>maken de cellen van Leydig daarna minder "
                  "testosteron</strong>."),
            ("p", "In een schema van een feedbacksysteem betekent een <strong>pijl met een minteken van "
                  "de eierstok naar de hypofyse</strong> dat het <strong>hormoon uit de eierstok de "
                  "hypofyse afremt</strong>."),
            ("weetje", "Precies dat remmende verband is waar de pil op werkt: hij houdt de hormonen van "
                       "buitenaf op peil, zodat de hypofyse geen LH-piek meer geeft en de eisprong "
                       "uitblijft."),
        ]),
    ],
    onthoud=[
        "Een eicel rijpt in een follikel in de eierstok; de bevruchting gebeurt normaal in de eileider.",
        "Na de eisprong ontstaat uit de follikel het geel lichaam, dat vooral progesteron maakt.",
        "De menstruatiecyclus begint op de eerste dag van de menstruatie en duurt ongeveer 28 dagen.",
        "Zonder progesteron kan het dikke baarmoederslijmvlies niet in stand blijven.",
        "FSH laat de follikel rijpen, een plotse LH-piek brengt de eisprong op gang.",
        "Oestrogeen komt uit de eierstok, niet uit de hypofyse.",
        "Zaadcellen worden in de teelballen gevormd; de cellen van Leydig maken testosteron.",
        "Bij de man stuurt LH de cellen van Leydig aan en FSH de cellen van Sertoli.",
        "Een feedbacksysteem kan zowel remmen als stimuleren.",
    ],
)

# ───────────────────────── 6. Biodiversiteit en micro-organismen
BUNDELS["biodiversiteit-en-micro-organismen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Biodiversiteit en micro-organismen",
    onder="Hoe we het leven indelen, hoe micro-organismen leven en wat ze voor ons doen.",
    secties=[
        dict(kop="Het leven indelen", blokken=[
            ("kader", "<p>Het driedomeinensysteem, de prokaryoten en de tree of life staan enkel in de "
                      "uitgebreide fiche, dus voor moderne talen en Latijn.</p>"),
            ("p", "Het <strong>driedomeinensysteem</strong> bestaat uit <strong>archaea, bacteriën en "
                  "eukaryoten</strong>. Bij het <strong>vijfrijkensysteem</strong> horen het "
                  "<strong>plantenrijk</strong>, het <strong>dierenrijk</strong> en het "
                  "<strong>prokaryotenrijk</strong>, naast de schimmels en de protisten; een "
                  "<strong>virusrijk bestaat niet</strong>."),
            ("p", "Een indeling als het driedomeinensysteem is nuttig omdat ze <strong>toont hoe soorten "
                  "met elkaar verwant zijn</strong>. Ze zegt niets over wat de mens nuttig vindt."),
            ("p", "Een <strong>prokaryote cel heeft geen kernmembraan</strong>. Een organisme waarvan de "
                  "cel <strong>wél een echte kern met kernmembraan</strong> heeft, is een "
                  "<strong>eukaryoot</strong>. <strong>Schimmels zijn eukaryoot</strong>."),
            ("p", "<strong>Virussen staan niet in de tree of life</strong> omdat ze "
                  "<strong>geen eigen stofwisseling hebben en zich niet alleen vermeerderen</strong>."),
            ("p", "Een organisme dat <strong>eencellig is, geen kernmembraan heeft en zich door "
                  "celsplitsing vermeerdert</strong>, hoort <strong>bij de prokaryoten</strong>."),
        ]),
        dict(kop="Bacteriën, gisten en virussen", blokken=[
            ("p", "Bij de <strong>micro-organismen</strong> horen de <strong>bacteriën</strong>, de "
                  "<strong>gisten en schimmels</strong> en de <strong>protozoa en eencellige "
                  "algen</strong>. <strong>Mossen</strong> horen er niet bij, die zijn met het blote oog "
                  "te zien."),
            ("p", "Een <strong>bacterie heeft een celwand</strong> en <strong>vermeerdert zich door "
                  "celsplitsing, waarbij één cel in twee gelijke cellen deelt</strong>. Een "
                  "<strong>gistcel</strong> doet dat anders: bij <strong>knopvorming</strong> vormt ze "
                  "een <strong>kleine uitstulping die daarna loskomt</strong>."),
            ("p", "Een <strong>virus</strong> bestaat in zijn eenvoudigste vorm uit "
                  "<strong>genetisch materiaal met een eiwitmantel eromheen</strong>. Die eiwitjas rond "
                  "het erfelijk materiaal is dus de <strong>eiwitmantel</strong>. Een virus "
                  "<strong>vermeerdert zich doordat het een gastheercel nieuwe virusdeeltjes laat "
                  "maken</strong>."),
            ("p", "Een bacterie heeft als <strong>groeivoorwaarden voedsel, vocht en een geschikte "
                  "temperatuur</strong> nodig. Een <strong>bacteriekweek groeit niet van het begin af "
                  "even snel</strong>: eerst komt ze traag op gang, dan volgt een snelle fase, en "
                  "daarna valt de groei stil. Vormt een bacterie een <strong>spore</strong>, dan doet ze "
                  "dat <strong>om een periode met slechte omstandigheden te overleven</strong>."),
            ("p", tabel(["Woord", "Wat het betekent"], [
                ["Anaëroob", "het organisme kan leven zonder zuurstofgas"],
                ["Aëroob", "het heeft juist zuurstofgas nodig"],
                ["Autotroof", "het maakt zijn eigen energierijke stoffen, bijvoorbeeld uit licht"],
                ["Heterotroof", "het haalt zijn energierijke stoffen uit andere organismen"],
            ])),
            ("p", "Een <strong>autotroof organisme haalt zijn energierijke stoffen dus niet uit andere "
                  "organismen</strong>; dat doet een heterotroof organisme."),
        ]),
        dict(kop="Micro-organismen in de keuken", blokken=[
            ("p", "<strong>Bakkersgist laat brood rijzen</strong>. Micro-organismen spelen ook een rol "
                  "bij <strong>yoghurt</strong>, <strong>zuurkool</strong> en "
                  "<strong>schimmelkaas</strong>; bij <strong>gekookt water</strong> niet. "
                  "<strong>Melkzuurbacteriën maken melk zuur en dik, en zo ontstaat yoghurt</strong>."),
            ("p", "Een <strong>gist</strong> is geschikt om <strong>bier te brouwen</strong> omdat ze "
                  "<strong>suikers zonder zuurstofgas omzet in alcohol en koolstofdioxide</strong>."),
            ("p", tabel(["Bewaren", "Wat het doet"], [
                ["Pasteuriseren", "het product wordt kort verhit zodat de meeste micro-organismen sterven"],
                ["Drogen", "het water gaat eruit, zodat micro-organismen niet meer kunnen groeien"],
                ["Inmaken in zuur of zout", "de meeste micro-organismen kunnen in die omstandigheden niet groeien"],
                ["Invriezen", "de groei valt stil zolang het product koud blijft"],
            ])),
            ("weetje", "Pasteuriseren maakt melk dus niet steriel. Daarom moet ze in de koelkast en blijft "
                       "ze maar een week of zo goed."),
        ]),
        dict(kop="Ziekte en afweer", blokken=[
            ("p", "Een <strong>antibioticum werkt op bacteriën</strong>. Daarom werkt het "
                  "<strong>niet tegen griep: griep wordt veroorzaakt door een virus</strong>. Een "
                  "<strong>schimmelinfectie behandel je ook niet met een antibioticum</strong>, maar met "
                  "een <strong>antimycoticum</strong>."),
            ("p", "<strong>Antibioticaresistentie</strong> ontstaat doordat de "
                  "<strong>bacteriën die het middel overleven zich verder vermenigvuldigen</strong>."),
            ("p", "Een <strong>vaccin laat het afweersysteem oefenen, zodat je later sneller "
                  "reageert</strong>. Het doodt dus niet wat er nu in je lichaam zit."),
            ("p", "<strong>Handen wassen</strong> en andere hygiënemaatregelen zijn zo doeltreffend omdat "
                  "ze <strong>de weg waarlangs ziekteverwekkers zich verspreiden onderbreken</strong>. "
                  "Ze doden niet alle bacteriën en ze vervangen geen vaccinatie."),
        ]),
        dict(kop="Micro-organismen in de natuur en in ons lichaam", blokken=[
            ("p", "Micro-organismen <strong>breken dood materiaal af bij het composteren</strong>, ze "
                  "<strong>zuiveren water in een waterzuiveringsinstallatie</strong> en ze "
                  "<strong>helpen planten aan stikstof via mycorrhiza</strong>. Bladgroen hebben ze "
                  "daarbij niet nodig."),
            ("p", "De <strong>zelfzuiverende capaciteit van een waterloop komt wel van "
                  "micro-organismen</strong>, niet enkel van de stroming. Raakt het water "
                  "<strong>overbemest</strong>, dan krijg je <strong>eutrofiëring</strong>: "
                  "<strong>algen bloeien op en het zuurstofgehalte daalt</strong>."),
            ("p", "Het geheel van micro-organismen in je darm is je <strong>darmmicrobioom</strong>. Bij "
                  "een <strong>microbioomtransplantatie</strong> worden "
                  "<strong>darmbacteriën van een gezonde donor naar een patiënt overgebracht</strong>. "
                  "<strong>Probiotica</strong> zijn <strong>levende micro-organismen die je inneemt om je "
                  "microbioom te ondersteunen</strong>."),
            ("p", "Over het <strong>huidmicrobioom</strong>: het <strong>bestaat uit micro-organismen "
                  "die normaal op je huid leven</strong>, het <strong>houdt ziekteverwekkers mee op "
                  "afstand</strong> en het <strong>hoort bij een gezonde huid</strong>. Je moet het dus "
                  "<strong>niet zo volledig mogelijk wegwassen</strong>."),
        ]),
    ],
    onthoud=[
        "Het driedomeinensysteem bestaat uit archaea, bacteriën en eukaryoten.",
        "Een prokaryote cel heeft geen kernmembraan; een eukaryoot heeft een echte kern met kernmembraan.",
        "Virussen staan niet in de tree of life: ze hebben geen eigen stofwisseling.",
        "Een bacterie vermeerdert zich door celsplitsing, een gistcel door knopvorming.",
        "Gist zet suikers zonder zuurstofgas om in alcohol en koolstofdioxide.",
        "Pasteuriseren verhit kort zodat de meeste micro-organismen sterven, maar maakt melk niet steriel.",
        "Een antibioticum werkt op bacteriën, dus niet tegen griep: dat is een virus.",
        "Een vaccin laat het afweersysteem oefenen, zodat je later sneller reageert.",
        "Eutrofiëring: in overbemest water bloeien algen op en daalt het zuurstofgehalte.",
    ],
)

# ───────────────────────── 7. Gedrag, interactie en ecosystemen
BUNDELS["gedrag-interactie-en-ecosystemen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gedrag, interactie en ecosystemen",
    onder="Aangeboren en aangeleerd gedrag, de interacties tussen soorten, en hoe energie en materie door een ecosysteem gaan.",
    secties=[
        dict(kop="Aangeboren en aangeleerd gedrag", blokken=[
            ("p", "<strong>Aangeboren gedrag</strong> is <strong>gedrag dat een dier vertoont zonder het "
                  "ooit geleerd te hebben</strong>. <strong>Aangeleerd gedrag</strong> is er in "
                  "verschillende vormen: <strong>conditioneren</strong>, "
                  "<strong>trial-and-error</strong> en <strong>imitatie</strong>. "
                  "<strong>Baltsgedrag</strong> is geen aangeleerd gedrag."),
            ("p", tabel(["Vorm van leren", "Wat het is"], [
                ["Conditioneren", "een hond kwijlt bij het geluid van de voerbak, nog voor hij eten ziet"],
                ["Gewenning", "het dier stopt met reageren op een prikkel die telkens zonder gevolg blijft"],
                ["Inprenting", "gebeurt in een korte, vaste periode kort na de geboorte"],
                ["Trial-and-error", "het dier probeert tot iets lukt en houdt dat over"],
                ["Imitatie", "het dier kijkt het gedrag van een ander af"],
            ])),
        ]),
        dict(kop="Gedrag tussen dieren", blokken=[
            ("p", "<strong>Baltsgedrag</strong> heeft als functie <strong>een partner van dezelfde soort "
                  "aan te trekken en te overtuigen</strong>. <strong>Territoriumgedrag</strong> is het "
                  "gedrag waarbij een <strong>dier zijn eigen gebied afbakent en verdedigt</strong>. "
                  "<strong>Imponeergedrag is een vorm van conflictgedrag waarbij het meestal niet tot "
                  "een echt gevecht komt</strong>."),
            ("p", "De <strong>taakverdeling binnen een mierenkolonie</strong> is "
                  "<strong>gedrag dat de hele groep ten goede komt</strong>."),
            ("p", tabel(["Soort communicatie", "Voorbeeld"], [
                ["Chemische communicatie", "een mier die een geurspoor achterlaat"],
                ["Visuele communicatie", "de kleurenpracht van een pauwenstaart, de dans van een honingbij, het opzetten van de haren bij een kat"],
                ["Auditieve communicatie", "het blaffen van een hond bij de deur"],
            ])),
        ]),
        dict(kop="Interacties tussen soorten", blokken=[
            ("p", tabel(["Interactie", "Wie er voordeel of schade van heeft"], [
                ["Mutualisme", "beide organismen hebben voordeel bij hun samenleven"],
                ["Commensalisme", "het ene heeft voordeel, het andere merkt er niets van"],
                ["Parasitisme", "het ene heeft voordeel, het andere ondervindt er schade van"],
                ["Predatie", "het roofdier heeft voordeel, de prooi verliest"],
                ["Concurrentie", "beide soorten willen hetzelfde, bijvoorbeeld hetzelfde zaad op hetzelfde veld"],
                ["Antibiose", "het ene maakt een stof die een ander organisme remt of doodt"],
            ])),
            ("p", "Bij <strong>commensalisme hebben dus niet beide organismen even veel voordeel</strong>, "
                  "en bij <strong>predatie hebben niet beide organismen voordeel</strong>."),
            ("p", "Over <strong>symbiose</strong>: <strong>twee soorten leven nauw met elkaar "
                  "samen</strong>, <strong>mutualisme is er een vorm van</strong> en ze "
                  "<strong>kan voor één of voor beide partners voordelig zijn</strong>. Ze "
                  "<strong>bestaat niet alleen tussen dieren onderling</strong>."),
            ("p", "De aantallen van een <strong>prooi en een roofdier lopen met een vertraging achter "
                  "elkaar aan</strong>: <strong>veel prooi laat de roofdieren toenemen, en veel "
                  "roofdieren laten de prooi weer afnemen</strong>."),
            ("p", "Zo'n interactie raakt ook onze eigen gezondheid: "
                  "<strong>nuttige darmbacteriën houden ziekteverwekkers op afstand</strong>."),
        ]),
        dict(kop="Wat een ecosysteem is", blokken=[
            ("p", "Een <strong>ecosysteem</strong> is <strong>alle organismen in een gebied samen met "
                  "hun niet-levende omgeving</strong>."),
            ("p", "De <strong>abiotische factoren</strong> zijn de <strong>niet-levende factoren, zoals "
                  "licht, temperatuur en bodem</strong>: de <strong>temperatuur</strong>, de "
                  "<strong>hoeveelheid licht</strong> en de <strong>zuurtegraad van de bodem</strong> "
                  "horen erbij. <strong>Betreding, begrazing en bemesting zijn biotische "
                  "factoren</strong>, want daar komt een levend wezen aan te pas; de "
                  "<strong>begrazing door schapen</strong> is dus niet abiotisch."),
            ("p", tabel(["Rol in het ecosysteem", "Wat die groep doet"], [
                ["Producenten", "maken met fotosynthese energierijke stoffen uit energiearme"],
                ["Consumenten", "eten andere organismen; een consument van de eerste orde eet plantaardig materiaal"],
                ["Reducenten", "breken dood organisch materiaal af tot minerale stoffen"],
            ])),
            ("p", "Een <strong>consument van de eerste orde eet dus geen andere dieren</strong>."),
            ("p", "Een <strong>voedselweb is een betere voorstelling dan één voedselketen</strong> omdat "
                  "de <strong>meeste soorten van meer dan één soort eten en door meer dan één soort "
                  "gegeten worden</strong>."),
        ]),
        dict(kop="Energie en materie", blokken=[
            ("p", "De <strong>energie in een ecosysteem stroomt in één richting en gaat stap voor stap "
                  "als warmte verloren</strong>. Daarom zit er <strong>in een piramide van biomassa in "
                  "elke hogere schakel minder materie dan in de schakel eronder</strong>, en zijn er "
                  "<strong>veel meer planten dan toproofdieren</strong>: bij elke stap in de keten gaat "
                  "het grootste deel van de energie verloren."),
            ("p", "<strong>Celademhaling</strong> is het proces dat <strong>energierijke stoffen weer "
                  "omzet in energiearme en daarbij energie vrijmaakt</strong>."),
            ("p", "Bij de <strong>koolstofkringloop</strong> horen de <strong>fotosynthese van "
                  "planten</strong>, de <strong>celademhaling van planten en dieren</strong> en het "
                  "<strong>afbreken van dood materiaal door reducenten</strong>; het "
                  "<strong>verdampen van water uit de oceaan</strong> hoort bij de waterkringloop. Die "
                  "<strong>waterkringloop staat niet volledig los van de koolstofkringloop</strong>: ze "
                  "grijpen in elkaar. <strong>Reducenten maken de materiekringloop rond.</strong>"),
            ("p", "In de <strong>stikstofkringloop zetten bacteriën stikstof om in vormen die planten "
                  "kunnen opnemen</strong>."),
        ]),
        dict(kop="Verstoring en biodiversiteit", blokken=[
            ("p", "<strong>Biodiversiteit</strong> is belangrijk omdat <strong>hoe meer soorten, hoe "
                  "beter het systeem een verstoring kan opvangen</strong>."),
            ("p", "Krijgt een <strong>meer jarenlang te veel mest</strong> binnen, dan "
                  "<strong>vermeerderen de algen zich sterk</strong>, <strong>dringt er minder licht "
                  "door tot in de diepte</strong> en <strong>daalt het zuurstofgehalte wanneer de algen "
                  "afsterven</strong>. De <strong>biodiversiteit neemt daarbij niet toe</strong>, ze "
                  "gaat achteruit."),
            ("p", "<strong>Klimaatverandering</strong> doet <strong>soorten verschuiven of verdwijnen "
                  "omdat hun leefomstandigheden veranderen</strong>. Verliest een "
                  "<strong>bos door ziekte bijna al zijn bomen</strong>, dan "
                  "<strong>raken de voedselrelaties en de kringlopen verstoord, en verdwijnen veel "
                  "soorten mee</strong>."),
            ("weetje", "Wolven zijn in 1995 opnieuw in Yellowstone uitgezet. Omdat de elanden daarna "
                       "minder lang op dezelfde plek bleven grazen, groeiden de wilgen langs de rivieren "
                       "terug, en met hen de bevers en de vogels."),
        ]),
    ],
    onthoud=[
        "Aangeboren gedrag vertoont een dier zonder het ooit geleerd te hebben.",
        "Vormen van leren: conditioneren, gewenning, inprenting, trial-and-error en imitatie.",
        "Baltsgedrag trekt een partner van dezelfde soort aan; territoriumgedrag bakent een eigen gebied af.",
        "Mutualisme: beide hebben voordeel. Parasitisme: het ene voordeel, het andere schade.",
        "Commensalisme: het ene heeft voordeel, het andere merkt er niets van.",
        "Een ecosysteem is alle organismen in een gebied samen met hun niet-levende omgeving.",
        "Producenten maken energierijke stoffen, consumenten eten andere organismen, reducenten breken dood materiaal af.",
        "De energie stroomt in één richting en gaat stap voor stap als warmte verloren.",
        "Hoe meer soorten, hoe beter het systeem een verstoring kan opvangen.",
    ],
)

# ───────────────────────── 8. Mengsels en zuivere stoffen
BUNDELS["mengsels-en-zuivere-stoffen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Mengsels en zuivere stoffen",
    onder="Het verschil tussen een mengsel en een zuivere stof, de soorten mengsels en de technieken om ze te scheiden.",
    secties=[
        dict(kop="Zuivere stof of mengsel", blokken=[
            ("p", "Een <strong>zuivere stof</strong> is <strong>een stof die uit maar één soort deeltjes "
                  "bestaat</strong>. Over een zuivere stof geldt: ze <strong>heeft een vast "
                  "smeltpunt</strong>, ze <strong>heeft een vast kookpunt</strong> en ze "
                  "<strong>bestaat uit één soort deeltjes</strong>. Ze bestaat daarmee "
                  "<strong>niet altijd uit één soort atomen</strong>: water is een zuivere stof en toch "
                  "een verbinding van twee elementen."),
            ("p", "<strong>Lucht is dus geen zuivere stof</strong>, en <strong>water uit de kraan "
                  "evenmin</strong>: <strong>er zitten opgeloste zouten en gassen in</strong>."),
            ("p", "Verwarm je een mengsel en <strong>blijft de temperatuur tijdens het koken "
                  "stijgen</strong>, dan weet je dat het <strong>een mengsel is, want een zuivere stof "
                  "kookt bij één vaste temperatuur</strong>. Ook bij het smelten geldt dat: een "
                  "<strong>mengsel smelt niet bij één vaste temperatuur</strong> maar over een traject."),
            ("p", "Een <strong>bestanddeel van een mengsel behoudt zijn eigen "
                  "stofeigenschappen</strong>. In een <strong>heterogeen mengsel kan je de verschillende "
                  "bestanddelen onderscheiden</strong>, met het blote oog of met de microscoop; in een "
                  "homogeen mengsel niet."),
            ("p", "Een <strong>molecule</strong> verschilt van een atoom doordat ze "
                  "<strong>uit twee of meer atomen bestaat die aan elkaar gebonden zijn</strong>."),
        ]),
        dict(kop="De soorten mengsels", blokken=[
            ("p", tabel(["Soort mengsel", "Wat het is", "Voorbeeld"], [
                ["Oplossing", "een homogeen mengsel van een vaste stof in een vloeistof", "suiker in water"],
                ["Legering", "een homogeen mengsel van metalen", "messing, een legering van koper en zink"],
                ["Suspensie", "vaste deeltjes die zweven in een vloeistof", "krijt in water"],
                ["Emulsie", "twee vloeistoffen die niet in elkaar oplossen", "vinaigrette"],
                ["Aerosol", "heel fijne deeltjes of druppels in een gas", "rook en nevel"],
                ["Schuim", "gasbelletjes verdeeld in een vloeistof of in een vaste stof", "slagroom"],
            ])),
            ("p", "<strong>Homogeen</strong> zijn dus <strong>suiker in water</strong>, "
                  "<strong>lucht</strong> en <strong>messing</strong>; <strong>zand in water</strong> is "
                  "heterogeen. <strong>Heterogeen</strong> zijn <strong>slagroom</strong>, "
                  "<strong>vinaigrette</strong> en <strong>rook</strong>; <strong>zeewater</strong> is "
                  "homogeen."),
            ("p", "De <strong>aggregatietoestanden</strong> zijn <strong>vast, vloeibaar en gas</strong>."),
        ]),
        dict(kop="Stofeigenschappen", blokken=[
            ("p", "<strong>Stofeigenschappen</strong> zijn eigenschappen van de stof zelf, hoeveel je er "
                  "ook van hebt: het <strong>kookpunt</strong>, de <strong>oplosbaarheid</strong> en de "
                  "<strong>geleidbaarheid</strong>. De <strong>hoeveelheid die je in de pot hebt</strong> "
                  "is er geen."),
            ("p", "<strong>Massadichtheid</strong> is <strong>de massa van een stof per eenheid "
                  "volume</strong>, in kilogram per kubieke meter of in gram per kubieke centimeter."),
            ("p", "<strong>Scheidingstechnieken maken gebruik van een verschil in stofeigenschap tussen "
                  "de bestanddelen</strong>, en <strong>een scheidingstechniek verandert de bestanddelen "
                  "niet chemisch</strong>: na het scheiden heb je dezelfde stoffen, apart."),
        ]),
        dict(kop="Scheidingstechnieken", blokken=[
            ("p", tabel(["Techniek", "Waarop ze steunt", "Wanneer je ze gebruikt"], [
                ["Zeven", "een verschil in deeltjesgrootte", "grove van fijne vaste deeltjes scheiden"],
                ["Filtreren", "een verschil in deeltjesgrootte", "zand uit water halen"],
                ["Decanteren", "een verschil in massadichtheid; je giet de bovenste laag af", "een bezonken mengsel voorzichtig overgieten"],
                ["Centrifugeren", "zware deeltjes bezinken sneller door snel rond te draaien", "zwevende deeltjes die niet van zelf bezinken"],
                ["Destilleren", "een verschil in kookpunt", "zuiver water uit zeewater halen, alcohol en water scheiden"],
                ["Indampen", "het oplosmiddel laten verdampen", "keukenzout uit zout water terugwinnen"],
                ["Extraheren", "een stof lost in een bepaald oplosmiddel wel op en de rest niet", "één stof uit een mengsel halen"],
                ["Chromatografie", "de bestanddelen schuiven verschillend ver mee met een loopmiddel", "de kleurstoffen van een stift op een strook papier"],
                ["Adsorptie", "bepaalde stoffen hechten zich vast aan het oppervlak van een vaste stof", "water of lucht zuiveren met actieve kool"],
                ["Een magneet", "ijzer is magnetisch en zand niet", "ijzervijlsel uit zand halen"],
            ])),
            ("p", "Bij <strong>decanteren duw je het mengsel dus niet door een filter met fijne "
                  "poriën</strong>, je giet het af. Het <strong>kookpunt</strong> speelt mee bij "
                  "<strong>destilleren</strong>, bij <strong>indampen</strong> en bij het "
                  "<strong>scheiden van alcohol en water</strong>, niet bij zeven."),
            ("p", "Na het <strong>filtreren</strong> blijft het <strong>residu</strong> op de filter "
                  "achter en loopt het <strong>filtraat</strong> erdoor. Allebei "
                  "<strong>kunnen ze het bestanddeel zijn dat je nodig hebt</strong>, dus het "
                  "<strong>residu is niet altijd afval</strong>."),
            ("p", "<strong>Olie en water</strong> scheid je niet goed met filtreren, want de "
                  "<strong>druppeltjes zijn vloeibaar en gaan gewoon door de filter</strong>. Voor een "
                  "<strong>troebele vloeistof met zwevende deeltjes die niet bezinken</strong> komen "
                  "<strong>filtreren of centrifugeren</strong> het eerst in aanmerking."),
            ("weetje", "Een waterzuiveringsinstallatie gebruikt die technieken na elkaar: eerst zeven, "
                       "dan laten bezinken, dan bacteriën het werk laten doen, en als laatste stap soms "
                       "nog actieve kool."),
        ]),
    ],
    onthoud=[
        "Een zuivere stof bestaat uit één soort deeltjes en heeft een vast smeltpunt en kookpunt.",
        "Een mengsel kookt en smelt niet bij één vaste temperatuur.",
        "In een heterogeen mengsel kan je de bestanddelen onderscheiden, in een homogeen mengsel niet.",
        "Suiker in water, lucht en messing zijn homogeen; slagroom, vinaigrette en rook heterogeen.",
        "Massadichtheid is de massa van een stof per eenheid volume.",
        "Een scheidingstechniek gebruikt een verschil in stofeigenschap en verandert de bestanddelen niet chemisch.",
        "Filtreren steunt op deeltjesgrootte, destilleren op een verschil in kookpunt.",
        "Na het filtreren blijft het residu op de filter en loopt het filtraat erdoor.",
    ],
)

# ───────────────────────── 9. Enkelvoudige en samengestelde stoffen, en chemische reacties
BUNDELS["enkelvoudige-en-samengestelde-stoffen-en-chemische-reacties-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Enkelvoudige en samengestelde stoffen, en chemische reacties",
    onder="Symbolen en formules, de stoffen die je moet kennen, en hoe je een reactievergelijking kloppend maakt.",
    secties=[
        dict(kop="Enkelvoudig en samengesteld", blokken=[
            ("p", "Een <strong>enkelvoudige stof</strong> is <strong>een stof die uit maar één soort "
                  "atomen bestaat</strong>. <strong>Zuurstofgas</strong>, "
                  "<strong>waterstofgas</strong> en <strong>ozon</strong> zijn dus enkelvoudig; "
                  "<strong>koolstofdioxide</strong> is samengesteld, want de "
                  "<strong>formule CO2 bevat twee verschillende elementen</strong>."),
            ("p", "Naast de wetenschappelijke naam heeft een stof vaak een <strong>triviale "
                  "naam</strong>, de gebruiksnaam: <strong>keukenzout naast natriumchloride</strong>."),
        ]),
        dict(kop="Symbolen en formules", blokken=[
            ("p", tabel(["Element", "Symbool"], [
                ["natrium", "Na"],
                ["kalium", "K"],
                ["koolstof", "C"],
                ["koper", "Cu"],
                ["goud", "Au"],
                ["magnesium", "Mg"],
            ])),
            ("p", "In een formule staat de <strong>index</strong> klein achteraan en zegt hoeveel atomen "
                  "van dat element in één deeltje zitten; de <strong>coëfficiënt</strong> staat "
                  "vooraan en zegt hoeveel van die deeltjes je neemt. In "
                  "<strong>3 H2O</strong> is de <strong>index 2 en de coëfficiënt 3</strong>."),
            ("kader", "<p>Atomen tellen in <strong>2 H2SO4</strong>: per deeltje 2 waterstof, 1 zwavel "
                      "en 4 zuurstof, dat is 7 atomen. Twee van die deeltjes maakt "
                      "<strong>14</strong> atomen in totaal.</p>"),
        ]),
        dict(kop="Metalen en niet-metalen", blokken=[
            ("p", "Typisch voor <strong>metalen</strong>: ze <strong>geleiden elektriciteit goed</strong>, "
                  "ze <strong>geleiden warmte goed</strong> en ze zijn <strong>vervormbaar</strong>. Ze "
                  "zijn <strong>bij kamertemperatuur niet altijd een gas</strong>, integendeel: op "
                  "<strong>kwik</strong> na zijn ze allemaal vast."),
            ("p", "Over de <strong>niet-metalen</strong>: ze <strong>geleiden elektriciteit "
                  "slecht</strong>, <strong>veel ervan zijn bij kamertemperatuur een gas</strong> en ze "
                  "zijn <strong>meestal broos als ze vast zijn</strong>. Ze zijn dus "
                  "<strong>niet allemaal glanzend en goed vervormbaar</strong>."),
            ("p", tabel(["Stof", "Waaraan je ze herkent of waarvoor ze dient"], [
                ["Koper", "een glanzend, roodbruin metaal dat warmte en elektriciteit uitstekend geleidt"],
                ["Kwik", "het enige metaal dat bij kamertemperatuur vloeibaar is"],
                ["Zuurstofgas", "om te lassen, en in de gezondheidszorg bij ademnood"],
                ["Chloorgas", "een geelgroen gas"],
                ["Neon", "licht op wanneer er stroom door gaat, vandaar de lichtreclame"],
                ["Helium", "een edelgas dat zo goed als nergens mee reageert, daarom in ballonnen"],
            ])),
            ("p", "<strong>Edelgassen reageren dus niet gemakkelijk</strong> met andere stoffen; dat is "
                  "precies de reden dat men <strong>helium in ballonnen gebruikt en geen "
                  "waterstofgas</strong>."),
            ("p", "<strong>Grafiet en diamant</strong> zijn allebei uit koolstof opgebouwd en verschillen "
                  "toch zo sterk omdat de <strong>atomen in een andere structuur aan elkaar "
                  "zitten</strong>."),
            ("p", "<strong>Ozon</strong> is hoog in de atmosfeer nuttig, want daar houdt het "
                  "ultraviolet licht tegen. <strong>Vlak boven de grond is het dat niet</strong>: daar is "
                  "het schadelijk om in te ademen."),
        ]),
        dict(kop="Een chemische reactie", blokken=[
            ("p", "Een <strong>chemische reactie is iets anders dan het mengen van twee stoffen</strong>: "
                  "<strong>bij een reactie ontstaan er nieuwe stoffen met andere "
                  "eigenschappen</strong>."),
            ("p", "De <strong>reagentia</strong> zijn de <strong>stoffen die links van de pijl "
                  "staan</strong>, de <strong>reactieproducten</strong> die <strong>rechts van de "
                  "pijl</strong>."),
            ("p", tabel(["Soort reactie", "Wat er gebeurt"], [
                ["Synthese", "uit twee of meer stoffen ontstaat één nieuwe stof"],
                ["Analyse", "één stof valt uiteen, zoals water onder invloed van elektrische stroom in waterstofgas en zuurstofgas"],
            ])),
        ]),
        dict(kop="Behoud van massa en kloppend maken", blokken=[
            ("p", "De <strong>wet van behoud van massa</strong> zegt: de "
                  "<strong>totale massa voor en na een reactie is gelijk</strong>. Verbrand je "
                  "<strong>magnesium in een afgesloten vat</strong> en weeg je opnieuw, dan is de "
                  "<strong>totale massa in het vat gelijk gebleven</strong>. Bij een "
                  "<strong>verbranding in een open schaal lijkt de massa van het vaste overblijfsel soms "
                  "te dalen omdat er gassen ontsnappen</strong>."),
            ("p", "Je maakt een reactievergelijking kloppend door het "
                  "<strong>aantal atomen van elk element links en rechts gelijk te maken</strong>, "
                  "<strong>omdat atomen bij een reactie niet verdwijnen of ontstaan</strong>. Daarbij mag "
                  "je <strong>de index in een formule niet aanpassen</strong>, alleen de coëfficiënt "
                  "ervoor."),
            ("kader", "<p>H2 + O2 geeft H2O wordt kloppend als "
                      "<strong>2 H2 + O2 geeft 2 H2O</strong>: links 4 waterstof en 2 zuurstof, rechts "
                      "ook.</p>"),
            ("p", "In <strong>2 Mg + O2 geeft 2 MgO</strong> geldt: <strong>links en rechts staan twee "
                  "magnesiumatomen</strong>, <strong>links en rechts staan twee zuurstofatomen</strong> "
                  "en <strong>magnesium en zuurstofgas zijn de reagentia</strong>. Er ontstaat "
                  "<strong>maar één reactieproduct</strong>, geen twee."),
        ]),
        dict(kop="Energie bij een reactie", blokken=[
            ("p", "De hoeveelheid energie die bij een reactie opgenomen of afgestaan wordt, is de "
                  "<strong>reactie-energie</strong>."),
            ("p", tabel(["Soort reactie", "Wat je merkt"], [
                ["Exo-energetisch", "de reactie staat energie af aan de omgeving; het wordt warmer"],
                ["Endo-energetisch", "de reactie neemt energie op uit haar omgeving; het wordt kouder"],
            ])),
            ("p", "Voelt de <strong>beker duidelijk kouder aan</strong>, dan is de "
                  "<strong>reactie endo-energetisch en neemt ze warmte op</strong>. Een "
                  "<strong>reactie die licht uitzendt is niet endo-energetisch</strong> maar "
                  "exo-energetisch: ze geeft energie af."),
            ("p", "Bij een chemische reactie kunnen <strong>warmte</strong>, <strong>licht</strong> en "
                  "<strong>elektrische energie</strong> vrijkomen. <strong>Massa</strong> is geen vorm "
                  "van energie die vrijkomt; die blijft net bewaard."),
            ("p", "Op een <strong>energiediagram</strong> staan <strong>de energie en het verloop van de "
                  "reactie</strong> op de assen. Bij een <strong>exo-energetische reactie liggen de "
                  "reactieproducten lager dan de reagentia</strong>."),
            ("weetje", "Een handwarmer werkt op precies dat verschil: het knikje laat een "
                       "exo-energetische kristallisatie beginnen, en het zakje geeft die warmte een half "
                       "uur lang af."),
        ]),
    ],
    onthoud=[
        "Een enkelvoudige stof bestaat uit maar één soort atomen; CO2 is samengesteld.",
        "De index zegt hoeveel atomen in één deeltje zitten, de coëfficiënt hoeveel deeltjes je neemt.",
        "Metalen geleiden elektriciteit en warmte goed en zijn vervormbaar.",
        "Edelgassen reageren niet gemakkelijk; daarom gebruikt men helium in ballonnen.",
        "Bij een chemische reactie ontstaan nieuwe stoffen met andere eigenschappen.",
        "De reagentia staan links van de pijl, de reactieproducten rechts.",
        "Wet van behoud van massa: de totale massa voor en na een reactie is gelijk.",
        "Kloppend maken doe je met de coëfficiënten; de index in een formule pas je niet aan.",
        "Exo-energetisch: energie afgeven, het wordt warmer. Endo-energetisch: energie opnemen, het wordt kouder.",
    ],
)

# ───────────────────────── 10. De bouw van het atoom en het periodiek systeem
BUNDELS["de-bouw-van-het-atoom-en-het-periodiek-systeem-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De bouw van het atoom en het periodiek systeem",
    onder="De deeltjes in een atoom, het atoomnummer en het massagetal, en wat je uit het PSE kan aflezen.",
    secties=[
        dict(kop="De deeltjes in een atoom", blokken=[
            ("p", "Een atoom heeft een <strong>atoomkern</strong> met daarrond de "
                  "<strong>elektronen</strong>. In de kern zitten de <strong>protonen</strong> en de "
                  "<strong>neutronen</strong>; samen heten die de <strong>nucleonen</strong>."),
            ("p", tabel(["Deeltje", "Waar", "Lading"], [
                ["Proton", "in de kern", "positief"],
                ["Neutron", "in de kern", "niet geladen"],
                ["Elektron", "rond de kern", "negatief"],
            ])),
            ("p", "In een <strong>neutraal atoom</strong> zijn er <strong>evenveel protonen als "
                  "elektronen</strong>, en daarom heffen de ladingen elkaar precies op. Bijna de hele "
                  "<strong>massa zit in de kern</strong>: een elektron weegt bijna tweeduizend keer minder "
                  "dan een proton."),
            ("p", "Het <strong>atoomnummer</strong> is het <strong>aantal protonen</strong> en bepaalt "
                  "<strong>om welk element</strong> het gaat. Lees je atoomnummer 17, dan weet je meteen "
                  "dat de <strong>kern 17 protonen bevat</strong>, dat een "
                  "<strong>neutraal atoom 17 elektronen heeft</strong> en dat het element "
                  "<strong>op de zeventiende plaats in het PSE staat</strong>; over het aantal neutronen "
                  "zegt het niets. Het <strong>massagetal</strong> is het "
                  "<strong>aantal protonen plus neutronen</strong>. Het aantal "
                  "<strong>neutronen</strong> vind je dus door het <strong>atoomnummer van het massagetal "
                  "af te trekken</strong>: bij atoomnummer 11 en massagetal 23 zijn er 12 neutronen."),
            ("p", "<strong>Isotopen</strong> zijn atomen van <strong>hetzelfde element met een ander "
                  "aantal neutronen</strong>. Hun atoomnummer is gelijk, hun massagetal niet, en chemisch "
                  "gedragen ze zich hetzelfde."),
        ]),
        dict(kop="Ionen", blokken=[
            ("p", "Een <strong>ion</strong> is een atoom dat <strong>elektronen afgestaan of opgenomen "
                  "heeft</strong>. Het aantal protonen verandert daarbij niet, dus blijft het "
                  "<strong>hetzelfde element</strong>."),
            ("p", "<strong>Elektronen afstaan</strong> geeft een <strong>positief ion</strong>: er blijft "
                  "positieve lading over. <strong>Elektronen opnemen</strong> geeft een "
                  "<strong>negatief ion</strong>. Een deeltje met 12 protonen en 10 elektronen heeft dus "
                  "lading <strong>2 plus</strong>; een deeltje met 17 protonen en 18 elektronen is een "
                  "<strong>chloride-ion</strong> met lading 1 min."),
            ("p", "De <strong>symbolische voorstelling</strong> van een ion zegt dus twee dingen: "
                  "<strong>welk element</strong> het is, en <strong>hoeveel elektronen</strong> er af of "
                  "bij gekomen zijn. Hoeveel neutronen de kern bevat, lees je er niet uit af."),
        ]),
        dict(kop="Relatieve en absolute massa", blokken=[
            ("kader", "<p>Dit stuk staat enkel in de uitgebreide fiche, dus voor moderne talen en "
                      "Latijn.</p>"),
            ("p", "De <strong>relatieve atoommassa</strong> is de massa van een atoom "
                  "<strong>vergeleken met de atoommassa-eenheid u</strong>. Eén u is ongeveer de massa van "
                  "één proton of één neutron. Omdat het een verhouding is, heeft de relatieve massa "
                  "<strong>geen eenheid</strong>; je leest ze af in het periodiek systeem."),
            ("p", "De <strong>absolute massa</strong> is de <strong>echte massa</strong> van het atoom en "
                  "heeft wel een eenheid: de <strong>kilogram</strong>. Je vindt ze door de relatieve "
                  "massa te <strong>vermenigvuldigen met de waarde van één u in kilogram</strong>."),
        ]),
        dict(kop="Het periodiek systeem", blokken=[
            ("p", "Een <strong>periode</strong> is een <strong>horizontale rij</strong>; een "
                  "<strong>groep</strong> is een <strong>verticale kolom</strong>. Het "
                  "<strong>periodenummer</strong> geeft het <strong>aantal bezette schillen</strong>; het "
                  "<strong>groepsnummer</strong> van een hoofdgroep geeft het <strong>aantal "
                  "valentie-elektronen</strong>, de elektronen in de buitenste schil. Het aantal "
                  "valentie-elektronen van een <strong>hoofdgroepelement lees je dus af aan het "
                  "groepsnummer en niet aan het periodenummer</strong>."),
            ("p", "Een element in <strong>groep 2 en periode 4</strong> heeft dus "
                  "<strong>twee valentie-elektronen en vier bezette schillen</strong>. Omgekeerd kan je uit "
                  "die twee gegevens ook opzoeken welk element het is."),
            ("p", "Je vult de schillen van binnen naar buiten. In de <strong>eerste schil</strong> passen "
                  "<strong>2</strong> elektronen, in de <strong>tweede 8</strong>. De "
                  "<strong>elektronenconfiguratie</strong> van een natriumatoom, atoomnummer 11, "
                  "is dus <strong>2, 8, 1</strong>."),
            ("p", "<strong>Links en in het midden</strong> van het systeem staan de "
                  "<strong>metalen</strong>, <strong>rechtsboven</strong> de "
                  "<strong>niet-metalen</strong>, en in de <strong>laatste kolom</strong> de "
                  "<strong>edelgassen</strong>: <strong>helium</strong>, <strong>neon</strong>, "
                  "<strong>argon</strong> en nog drie zwaardere. <strong>Waterstof</strong> staat "
                  "vooraan en is er geen. Het <strong>metaalkarakter neemt naar rechts af</strong>, "
                  "en de <strong>elektronegativiteit</strong>, de gretigheid naar elektronen, neemt naar "
                  "rechts juist toe."),
        ]),
        dict(kop="Waarom elementen reageren", blokken=[
            ("p", "Een <strong>volle buitenste schil</strong> is de stabiele toestand. Die "
                  "<strong>bijzonder stabiele elektronenverdeling</strong> heet de "
                  "<strong>edelgasconfiguratie</strong>. Een atoom met zo'n volle schil is "
                  "<strong>weinig reactief</strong>, en daarom gaan de edelgassen bijna geen bindingen aan."),
            ("p", "Alle andere elementen zoeken de kortste weg naar die volle schil. "
                  "<strong>Groep 1</strong> heeft één valentie-elektron en <strong>staat dat af</strong>; "
                  "natrium houdt dan 2, 8 over, net de configuratie van neon. "
                  "<strong>Groep 2</strong> staat er twee af en wordt een ion met lading "
                  "<strong>2 plus</strong>."),
            ("p", "Een <strong>zuurstofatoom</strong> heeft zes valentie-elektronen. Het neemt "
                  "<strong>liever twee elektronen op dan er zes af te staan</strong>, want "
                  "<strong>twee opnemen vraagt veel minder dan zes afstaan om de volle schil te "
                  "bereiken</strong>, en daarom wordt zuurstof een ion met lading "
                  "<strong>2 min</strong>. Zo kan je uit de plaats in het systeem voorspellen welk ion een "
                  "element vormt."),
            ("p", "Elementen in <strong>dezelfde groep lijken sterk op elkaar</strong>, net omdat ze "
                  "evenveel valentie-elektronen hebben. Het chemische gedrag wordt immers helemaal door de "
                  "buitenste schil bepaald."),
            ("weetje", "Mendelejev liet in zijn eerste tabel plaatsen open voor elementen die nog niet "
                       "gevonden waren, en voorspelde hun eigenschappen. Toen ze later gevonden werden, "
                       "klopte zijn voorspelling verrassend goed."),
        ]),
    ],
    onthoud=[
        "In de kern zitten protonen en neutronen, samen de nucleonen; rond de kern de elektronen.",
        "Een neutraal atoom heeft evenveel protonen als elektronen.",
        "Atoomnummer = aantal protonen. Massagetal = protonen plus neutronen.",
        "Isotopen zijn atomen van hetzelfde element met een ander aantal neutronen.",
        "Elektronen afstaan geeft een positief ion, elektronen opnemen een negatief ion.",
        "De relatieve atoommassa heeft geen eenheid, de absolute massa wel: de kilogram.",
        "Periodenummer = aantal bezette schillen; groepsnummer van een hoofdgroep = aantal valentie-elektronen.",
        "In de eerste schil passen 2 elektronen, in de tweede 8: natrium is 2, 8, 1.",
        "Een volle buitenste schil, de edelgasconfiguratie, is de stabiele toestand.",
    ],
)

# ───────────────────────── 11. Chemische bindingen en roosters
BUNDELS["chemische-bindingen-en-roosters-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische bindingen en roosters",
    onder="De drie bindingstypes, de vier roostertypes, en de eigenschappen die daaruit volgen.",
    secties=[
        dict(kop="De drie bindingstypes", blokken=[
            ("p", tabel(["Binding", "Tussen", "Wat er gebeurt"], [
                ["Ionbinding", "metaal en niet-metaal", "elektronen worden echt overgedragen"],
                ["Atoombinding (covalent)", "twee niet-metalen", "elektronenparen worden gedeeld"],
                ["Metaalbinding", "metaal en metaal", "de buitenste elektronen vormen een elektronenzee"],
            ])),
            ("p", "Je bepaalt het bindingstype dus aan het <strong>metaal- of niet-metaalkarakter</strong> "
                  "van de elementen. Bij een <strong>ionbinding</strong> staat het metaal elektronen af en "
                  "neemt het niet-metaal ze op; de ionen die zo ontstaan trekken elkaar aan. Bij een "
                  "<strong>atoombinding</strong> wil geen van beide afstaan, dus delen ze."),
            ("p", "Dat natrium zijn elektron aan chloor geeft en niet omgekeerd, komt door de "
                  "<strong>elektronegativiteit</strong>: chloor trekt elektronen veel sterker aan dan "
                  "natrium. Hoe groter dat verschil, hoe meer de binding naar een ionbinding opschuift."),
        ]),
        dict(kop="De Lewisstructuur", blokken=[
            ("kader", "<p>De Lewisstructuur en het oxidatiegetal staan enkel in de uitgebreide fiche, dus "
                      "voor moderne talen en Latijn.</p>"),
            ("p", "Een <strong>Lewisstructuur</strong> tekent alleen de "
                  "<strong>valentie-elektronen</strong>. Een <strong>streepje tussen twee atomen</strong> "
                  "is een <strong>bindend elektronenpaar</strong>, een gedeeld paar. Een "
                  "<strong>streepje bij één atoom</strong> is een <strong>vrij elektronenpaar</strong>, "
                  "dat niet meedoet aan een binding."),
            ("p", "Eén gedeeld paar is een <strong>enkelvoudige binding</strong>, twee paren een "
                  "<strong>dubbele binding</strong> en drie paren een <strong>drievoudige binding</strong>. "
                  "Stikstof heeft vijf valentie-elektronen en heeft er dus drie nodig: de twee "
                  "stikstofatomen in een <strong>stikstofmolecule</strong> delen "
                  "<strong>drie elektronenparen</strong>. "
                  "<strong>Koolstof</strong> heeft er vier nodig en maakt daarom gewoonlijk "
                  "<strong>vier bindingen</strong>."),
            ("p", "Het <strong>oxidatiegetal</strong> is een hulpmiddel om te boekhouden, geen echte "
                  "lading. In een <strong>enkelvoudige stof is het nul</strong>; in een neutrale stof "
                  "tellen alle oxidatiegetallen samen tot <strong>nul</strong> op. "
                  "<strong>Zuurstof</strong> heeft meestal <strong>min twee</strong>, "
                  "<strong>waterstof plus een</strong>."),
            ("p", "<strong>Binair</strong> betekent twee en <strong>ternair</strong> drie. Een stof die "
                  "uit <strong>twee verschillende elementen</strong> bestaat, is dus "
                  "<strong>geen ternaire stof</strong> maar een binaire. Zie je de "
                  "<strong>brutoformule</strong> van een stof met een <strong>metaal en een "
                  "niet-metaal</strong> erin, dan kan je al voorspellen dat het een "
                  "<strong>ionverbinding</strong> is, <strong>opgebouwd uit een ionrooster van "
                  "ionen</strong>."),
            ("p", "Een <strong>formule-eenheid</strong> is de <strong>kleinste verhouding waarin de ionen "
                  "in een ionrooster voorkomen</strong>. Een ionrooster bestaat immers niet uit losse "
                  "moleculen maar uit een netwerk; NaCl zegt dus 'één natriumion per chloride-ion', niet "
                  "'één molecule'."),
        ]),
        dict(kop="De vier roostertypes", blokken=[
            ("p", tabel(["Rooster", "Voorbeeld", "Smeltpunt", "Geleidt"], [
                ["Ionrooster", "keukenzout", "hoog", "pas als het gesmolten of opgelost is"],
                ["Molecuulrooster", "water, koolstofdioxide, jood", "laag", "niet"],
                ["Atoomrooster", "diamant, kwarts", "zeer hoog", "niet (grafiet is de uitzondering)"],
                ["Metaalrooster", "koper, ijzer", "meestal hoog", "ook in vaste toestand"],
            ])),
            ("p", "Een <strong>ionrooster</strong> heeft een <strong>hoog smeltpunt</strong>, want de "
                  "aantrekking tussen de ionen is in alle richtingen sterk. Het is "
                  "<strong>breekbaar</strong>: schuif je de lagen een stukje op, dan komen gelijke ladingen "
                  "tegenover elkaar en stoten die elkaar af. Het geleidt <strong>pas als de ionen kunnen "
                  "bewegen</strong>, dus gesmolten of in water."),
            ("p", "Een <strong>molecuulrooster</strong> heeft een <strong>laag smelt- en kookpunt</strong>: "
                  "binnen de molecule zijn de bindingen sterk, maar <strong>tussen</strong> de moleculen is "
                  "de aantrekking zwak. Daarom zijn zuurstof, water en koolstofdioxide bij "
                  "kamertemperatuur gas of vloeistof terwijl keukenzout vast is."),
            ("p", "Een <strong>metaalrooster</strong> heeft een <strong>elektronenzee</strong>. Daardoor "
                  "<strong>geleidt</strong> een metaal warmte en elektriciteit goed, <strong>glanst</strong> "
                  "het, en <strong>plooit</strong> het in plaats van te breken: de lagen ionen kunnen over "
                  "elkaar schuiven zonder dat de binding stuk gaat."),
            ("p", "In een <strong>atoomrooster</strong> zit elk atoom met atoombindingen aan zijn buren "
                  "vast: één groot netwerk. Daarom is diamant zo hard en smelt het pas bij een enorme "
                  "temperatuur. Alle elektronen zitten vast in bindingen, dus geleidt het "
                  "<strong>niet</strong>."),
        ]),
        dict(kop="Diamant en grafiet", blokken=[
            ("p", "Diamant en grafiet bestaan <strong>allebei alleen uit koolstof</strong>. Het verschil "
                  "zit volledig in hoe die atomen geschikt zijn."),
            ("p", "In <strong>diamant</strong> maakt elk koolstofatoom <strong>vier</strong> bindingen in "
                  "een stevig driedimensionaal netwerk: heel hard, geen vrije elektronen, geen geleiding. "
                  "In <strong>grafiet</strong> maakt elk atoom maar <strong>drie</strong> bindingen in een "
                  "vlak. Het <strong>vierde elektron blijft vrij</strong>, en daarom "
                  "<strong>geleidt grafiet wel</strong>."),
            ("p", "De bindingen <strong>binnen een laag</strong> van grafiet zijn sterk, maar "
                  "<strong>tussen de lagen</strong> is de aantrekking zwak. De lagen glijden over elkaar, "
                  "en daarom voelt grafiet <strong>zacht</strong> aan en laat een potlood een streep na."),
            ("p", "<strong>Isolatoren</strong> geleiden niet, omdat er geen ladingen zijn die zich kunnen "
                  "verplaatsen: suiker, rubber, droog hout, glas. <strong>Geleiders</strong> hebben vrije "
                  "elektronen (metalen) of vrije ionen (een zoutoplossing, een gesmolten zout). "
                  "<strong>Suiker lost wel op in water maar geleidt niet</strong>, want "
                  "suikermoleculen blijven hele moleculen."),
            ("weetje", "Een stof die bij 801 graden smelt, breekbaar is en pas geleidt na smelten of "
                       "oplossen, kan je blind als een zout met een ionrooster aanwijzen. Dat is precies "
                       "het gedrag van keukenzout."),
        ]),
    ],
    onthoud=[
        "Ionbinding: tussen metaal en niet-metaal worden elektronen echt overgedragen.",
        "Atoombinding: twee niet-metalen delen elektronenparen. Metaalbinding: een elektronenzee.",
        "Hoe groter het verschil in elektronegativiteit, hoe meer de binding naar een ionbinding opschuift.",
        "In een Lewisstructuur is een streepje tussen twee atomen een bindend elektronenpaar.",
        "Het oxidatiegetal is nul in een enkelvoudige stof; zuurstof heeft meestal min twee.",
        "Een ionrooster heeft een hoog smeltpunt, is breekbaar en geleidt pas gesmolten of opgelost.",
        "Een molecuulrooster heeft een laag smelt- en kookpunt: tussen de moleculen is de aantrekking zwak.",
        "Grafiet geleidt wel, want het vierde elektron van elk koolstofatoom blijft vrij.",
    ],
)

# ───────────────────────── 12. Stoffen classificeren en benoemen
BUNDELS["stoffen-classificeren-en-benoemen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen classificeren en benoemen",
    onder="De anorganische stofklassen, de zuurresten, de alkanen en de triviale namen die je moet kennen.",
    secties=[
        dict(kop="De anorganische stofklassen", blokken=[
            ("p", tabel(["Stofklasse", "Waaraan je ze herkent", "Voorbeeld"], [
                ["Oxide", "een element samen met zuurstof, twee elementen", "calciumoxide, koolstofdioxide"],
                ["Hydroxide", "een metaal met een of meer OH-groepen: de hydroxidegroep OH", "natriumhydroxide, calciumhydroxide"],
                ["Zuur", "de formule begint met waterstof", "waterstofchloride, zwavelzuur"],
                ["Zout", "een metaalion met een zuurrest", "natriumchloride, calciumcarbonaat"],
            ])),
            ("p", "<strong>Binair</strong> betekent <strong>twee</strong> elementen, "
                  "<strong>ternair</strong> betekent <strong>drie</strong>. Zoutzuur is dus een "
                  "<strong>binair zuur</strong> (waterstof en chloor), net als "
                  "<strong>waterstofchloride</strong>, <strong>waterstofsulfide</strong> en "
                  "<strong>waterstoffluoride</strong>; zwavelzuur en salpeterzuur zijn "
                  "<strong>ternair</strong>, want ze bevatten ook zuurstof. Keukenzout is een binair zout, "
                  "calciumcarbonaat een ternair zout."),
            ("p", "Een <strong>oxide</strong> is altijd binair: één element plus zuurstof. Komt er een "
                  "derde element bij, dan is het geen oxide meer."),
            ("p", "Een <strong>ammoniumzout</strong> is een zout waarin het <strong>metaalion vervangen "
                  "is door een ammoniumion</strong>, NH4 plus. Dat ion gedraagt zich als een positief "
                  "metaalion. Ammoniumnitraat in kunstmest is een bekend voorbeeld."),
        ]),
        dict(kop="De zuurresten", blokken=[
            ("p", tabel(["Ion", "Formule", "Komt van"], [
                ["Nitraation", "NO3 min", "salpeterzuur"],
                ["Sulfaation", "SO4 twee min", "zwavelzuur"],
                ["Fosfaation", "PO4 drie min", "fosforzuur, het zuur in frisdrank van het colatype"],
                ["Carbonaation", "CO3 twee min, de carbonaatgroep", "koolzuur"],
                ["Chloraation", "ClO3 min", "chloorzuur"],
                ["Chloride-ion", "Cl min", "zoutzuur"],
                ["Sulfide-ion", "S twee min", "waterstofsulfide"],
            ])),
            ("p", "Let op het verschil tussen de <strong>ionen met zuurstof</strong> en de "
                  "<strong>ionen zonder</strong>. Het <strong>chloraation</strong> bevat zuurstof, het "
                  "<strong>chloride-ion</strong> niet; het <strong>sulfaation</strong> bevat zuurstof, het "
                  "<strong>sulfide-ion</strong> niet. Hetzelfde geldt voor broom en jood."),
            ("p", "In de <strong>stocknotatie</strong> zet je het <strong>oxidatiegetal van het metaal "
                  "tussen haakjes</strong>, met een <strong>Romeins cijfer</strong>: ijzer(III)chloride. "
                  "Dat gebruik je bij <strong>ionverbindingen</strong>. Bij "
                  "<strong>atoomverbindingen</strong> gebruik je de <strong>Griekse telwoorden</strong>: "
                  "koolstofdioxide, distikstofoxide."),
            ("p", "Een <strong>brutoformule</strong> telt alleen de atomen (C2H6); een "
                  "<strong>structuurformule</strong> toont ook de <strong>bindingen</strong> ertussen."),
        ]),
        dict(kop="De alkanen", blokken=[
            ("p", "<strong>Alkanen</strong> zijn organische stoffen die <strong>alleen uit koolstof en "
                  "waterstof</strong> bestaan. Het aantal <strong>koolstofatomen</strong> zit in de naam: butaan "
                  "heeft er <strong>vier</strong>, pentaan <strong>vijf</strong>, octaan "
                  "<strong>acht</strong> en decaan <strong>tien</strong>. Elk koolstofatoom maakt vier "
                  "bindingen en de rest wordt met "
                  "waterstof opgevuld; daarom heten ze ook de verzadigde koolwaterstoffen. Hun naam eindigt "
                  "op <strong>aan</strong>."),
            ("p", tabel(["Aantal C", "Naam", "Aantal C", "Naam"], [
                ["1", "methaan", "6", "hexaan"],
                ["2", "ethaan", "7", "heptaan"],
                ["3", "propaan", "8", "octaan"],
                ["4", "butaan", "9", "nonaan"],
                ["5", "pentaan", "10", "decaan"],
            ])),
            ("p", "De telwoorden zitten in de naam: <strong>but</strong> is vier, "
                  "<strong>pent</strong> vijf, <strong>oct</strong> acht, <strong>dec</strong> tien. Zo kan "
                  "je van naam naar formule en omgekeerd."),
        ]),
        dict(kop="De triviale namen", blokken=[
            ("p", tabel(["Triviale naam", "Welke stof", "Waarvoor"], [
                ["Water", "diwaterstofoxide", "overal"],
                ["Zoutzuur", "waterstofchloride in water", "ontkalker"],
                ["Zwavelzuur", "H2SO4", "autobatterij, industrie"],
                ["Salpeterzuur", "HNO3", "kunstmest, industrie"],
                ["Fosforzuur", "H3PO4", "cola, roest verwijderen, kunstmest"],
                ["Ammoniak", "NH3", "schoonmaak en kunstmest"],
                ["Keukenzout", "natriumchloride", "voeding, strooizout"],
                ["Bakpoeder", "natriumwaterstofcarbonaat", "deeg laten rijzen"],
                ["Bijtende soda", "natriumhydroxide", "ontstopper"],
                ["Ongebluste kalk", "calciumoxide", "bouw"],
                ["Gebluste kalk", "calciumhydroxide", "bouw, bodem ontzuren"],
                ["Koolzuurgas", "koolstofdioxide", "frisdrank, brandblusser"],
                ["Lachgas", "distikstofoxide", "vroeger verdoving"],
                ["Aardgas", "vooral methaan", "verwarmen en koken"],
            ])),
            ("p", "<strong>Koolzuurgas en koolzuur zijn niet hetzelfde</strong>: koolzuurgas is "
                  "koolstofdioxide, koolzuur ontstaat pas als dat gas <strong>in water oplost</strong>. "
                  "Ook <strong>koolstofdioxide en koolstofmonoxide</strong> verschillen: het eerste heeft "
                  "twee zuurstofatomen en ademen we uit, het tweede heeft er één en is levensgevaarlijk."),
            ("p", "<strong>Koolstofmonoxide</strong> is kleurloos en geurloos, en hecht veel sterker aan "
                  "je bloed dan zuurstof. Het bindt daar op de plaats waar zuurstof zou moeten zitten. Het "
                  "ontstaat bij <strong>onvolledige verbranding</strong>, bijvoorbeeld in een slecht "
                  "onderhouden geiser."),
            ("p", "<strong>Calciumcarbonaat</strong> is de bouwsteen van <strong>kalksteen, krijt en "
                  "marmer</strong>, en zit ook in eierschalen, schelpen en kalkaanslag. Carbonaten "
                  "<strong>schuimen op met zuur</strong>, want er komt koolstofdioxide vrij. Daarom "
                  "verdwijnt kalkaanslag met azijn."),
            ("p", "In een <strong>gasfles voor de barbecue</strong> zit <strong>propaan, butaan of een "
                  "mengsel</strong> van die twee: onder druk vloeibaar, en bij het verbranden schoon. "
                  "<strong>Ongebluste kalk</strong> wordt <strong>gebluste kalk</strong> als je er water "
                  "bij giet, en die reactie geeft veel warmte af."),
            ("weetje", "Bij heel bekende stoffen gebruiken we bijna altijd de triviale naam. Niemand "
                       "vraagt aan tafel om diwaterstofoxide."),
        ]),
    ],
    onthoud=[
        "Oxide: een element samen met zuurstof. Hydroxide: een metaal met een of meer OH-groepen.",
        "De formule van een zuur begint met waterstof; een zout is een metaalion met een zuurrest.",
        "Binair betekent twee elementen, ternair drie.",
        "Nitraat NO3 min, sulfaat SO4 twee min, fosfaat PO4 drie min, carbonaat CO3 twee min.",
        "Chloraat en sulfaat bevatten zuurstof, chloride en sulfide niet.",
        "Stocknotatie bij ionverbindingen, Griekse telwoorden bij atoomverbindingen.",
        "Alkanen bestaan alleen uit koolstof en waterstof; hun naam eindigt op aan.",
        "But is vier, pent vijf, oct acht, dec tien.",
        "Koolzuurgas is koolstofdioxide; koolzuur ontstaat pas als dat gas in water oplost.",
    ],
)

# ───────────────────────── 13. Stoffen in water, reacties en berekeningen
BUNDELS["stoffen-in-water-reacties-en-berekeningen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen in water, reacties en berekeningen",
    onder="Dissociëren en ioniseren, de pH-schaal, de neerslag- en neutralisatiereactie, en het rekenen met mol.",
    secties=[
        dict(kop="Polair, apolair en oplossen", blokken=[
            ("p", "Water is zelf een <strong>polaire</strong> stof, en <strong>gelijk lost op in "
                  "gelijk</strong>. Daarom lossen <strong>polaire stoffen goed op in water</strong> en "
                  "<strong>apolaire niet</strong>. Olie mengt niet met water: watermoleculen houden elkaar "
                  "met hun polaire kanten vast, en een apolaire oliemolecule past daar niet tussen."),
            ("p", "De typevoorbeelden van <strong>apolaire stoffen</strong> zijn de "
                  "<strong>enkelvoudige stoffen</strong> (zuurstofgas), "
                  "<strong>tetrachloormethaan</strong> en de <strong>alkanen</strong> zoals hexaan."),
            ("p", "Bij het oplossen worden de ionen omringd door watermoleculen, met hun negatieve kant "
                  "naar de positieve ionen en omgekeerd. Dat heet <strong>hydratatie</strong>, en zo "
                  "blijven de ionen gescheiden."),
        ]),
        dict(kop="Dissociëren of ioniseren?", blokken=[
            ("p", "<strong>Dissociëren</strong> doen <strong>zouten en hydroxiden</strong>: de ionen zaten "
                  "al in het rooster en <strong>komen los van elkaar</strong>. De "
                  "<strong>dissociatievergelijking</strong> van <strong>natriumchloride</strong> in water "
                  "schrijf je dus op als <strong>NaCl wordt Na plus en Cl min</strong>, met dezelfde "
                  "lading als in het rooster en niet als twee neutrale atomen."),
            ("p", "<strong>Ioniseren</strong> doen <strong>polaire moleculaire verbindingen</strong>, "
                  "vooral de <strong>zuren</strong>: in <strong>waterstofchloride</strong>, het gas HCl, "
                  "zitten geen ionen maar moleculen, en in "
                  "water <strong>valt de molecule uiteen in ionen die er nog niet waren</strong>, een "
                  "waterstofion en een chloride-ion."),
            ("p", "Een <strong>elektrolyt</strong> is een stof die in water geleidt doordat ze ionen "
                  "vormt: zouten, zuren en hydroxiden. Een <strong>niet-elektrolyt</strong> lost wel op "
                  "maar vormt geen ionen: <strong>suiker</strong> en alcohol. Oplossen en geleiden zijn dus "
                  "twee verschillende dingen."),
            ("p", "Een vast blokje keukenzout geleidt niet, een <strong>zoutoplossing</strong> wel: in de "
                  "oplossing kunnen de ionen zich <strong>verplaatsen</strong>, in het rooster zitten ze "
                  "vast. Een <strong>gesmolten zout</strong> geleidt om dezelfde reden, ook zonder water. "
                  "Een <strong>geleider</strong> geleidt goed, een <strong>isolator</strong> niet."),
        ]),
        dict(kop="Zuur, basisch en de pH", blokken=[
            ("p", "De <strong>pH-schaal</strong> loopt gewoonlijk van <strong>0 tot 14</strong>. "
                  "<strong>Onder 7 is zuur</strong>, <strong>7 is neutraal</strong>, "
                  "<strong>boven 7 is basisch</strong>. Elke eenheid verschil is een "
                  "<strong>factor tien</strong>: pH 3 is honderd keer zuurder dan pH 5."),
            ("p", "Een <strong>zuur ioniseert</strong> en geeft <strong>waterstofionen</strong> vrij; een "
                  "<strong>hydroxide dissocieert</strong> en geeft <strong>hydroxide-ionen</strong> vrij. "
                  "Los je natriumhydroxide op, dan komt de pH dus <strong>boven 7</strong>."),
            ("p", "Een <strong>zuur-base indicator</strong> verandert van <strong>kleur</strong> bij een "
                  "bepaalde pH; welke kleur bij welke waarde hoort, lees je af in een tabel. Wordt een "
                  "indicator <strong>rood</strong>, dan is de oplossing meestal <strong>zuur</strong>. Een "
                  "<strong>pH-meter</strong> geeft de waarde als <strong>getal</strong> en is veel "
                  "nauwkeuriger."),
        ]),
        dict(kop="Neerslag, neutralisatie en redox", blokken=[
            ("kader", "<p>De essentiële reactievergelijking en de redoxreacties met oxidatiegetallen staan "
                      "enkel in de uitgebreide fiche, dus voor moderne talen en Latijn.</p>"),
            ("p", "Bij een <strong>neerslagreactie</strong> ontstaat uit twee oplossingen een "
                  "<strong>vaste stof die niet oplost</strong> en naar de bodem zakt. Zilverionen bij "
                  "chloride-ionen geven een <strong>witte neerslag van zilverchloride</strong>. Of er "
                  "neerslag komt, kijk je na in een <strong>oplosbaarheidstabel</strong>."),
            ("p", "Bij een <strong>neutralisatiereactie</strong> tussen een zuur en een base ontstaat er "
                  "een <strong>zout en water</strong>, en de pH schuift naar <strong>7</strong> toe. De "
                  "<strong>essentiële reactievergelijking</strong> laat de ionen weg die niet meedoen, de "
                  "<strong>spectatorionen</strong>. Voor elke neutralisatie is dat dus: een "
                  "<strong>waterstofion en een hydroxide-ion vormen samen water</strong>."),
            ("p", "Bij een <strong>redoxreactie</strong> worden er elektronen overgedragen. "
                  "<strong>Oxidatie</strong> is <strong>elektronen afstaan</strong>, en het oxidatiegetal "
                  "<strong>stijgt</strong>; <strong>reductie</strong> is ze <strong>opnemen</strong>, en "
                  "het oxidatiegetal <strong>daalt</strong>. De <strong>oxidator neemt op</strong>, de "
                  "<strong>reductor staat af</strong>. Het ene gaat nooit zonder het andere, en er "
                  "verandert dus altijd minstens bij <strong>twee elementen</strong> een oxidatiegetal."),
            ("p", "Twee stoffen die je samengiet geven <strong>vaak niets</strong>: dan lossen alle "
                  "mogelijke combinaties goed op. Dat weet je vooraf uit de oplosbaarheidstabel."),
        ]),
        dict(kop="Rekenen met mol", blokken=[
            ("p", "Eén <strong>mol</strong> is altijd <strong>hetzelfde aantal deeltjes</strong>, ongeveer "
                  "<strong>6 maal 10 tot de 23</strong>. Dat getal heet het "
                  "<strong>getal van Avogadro</strong>."),
            ("p", tabel(["Wat je zoekt", "Hoe je rekent"], [
                ["massa", "stofhoeveelheid maal molaire massa"],
                ["stofhoeveelheid", "massa gedeeld door molaire massa"],
                ["molaire concentratie", "aantal mol gedeeld door volume in liter"],
                ["aantal deeltjes", "aantal mol maal het getal van Avogadro"],
            ])),
            ("p", "De <strong>molaire massa</strong> lees je af in het periodiek systeem, in "
                  "<strong>gram per mol</strong>; voor een molecule tel je de atomen samen. Water heeft "
                  "18 gram per mol, dus is <strong>2 mol water 36 gram</strong>, en "
                  "<strong>36 gram water 2 mol</strong>."),
            ("p", "De <strong>molaire concentratie</strong> zegt hoeveel mol er in één liter zit, in "
                  "<strong>mol per liter</strong>. Eén mol in een halve liter geeft dus "
                  "<strong>2 mol per liter</strong>."),
            ("p", "De <strong>coëfficiënten</strong> voor de formules in een reactievergelijking geven de "
                  "<strong>verhouding in mol</strong> waarin de stoffen reageren; dat heet de "
                  "<strong>stoichiometrische verhouding</strong>. Wil je grammen, dan reken je eerst van "
                  "mol naar massa. Bij een <strong>aflopende reactie</strong> gaat het door tot "
                  "<strong>één van de stoffen volledig opgebruikt</strong> is, en die bepaalt hoeveel "
                  "product je krijgt."),
            ("weetje", "Een mol koolstof weegt 12 gram en past in je hand. Toch zitten daar meer atomen in "
                       "dan er sterren in het zichtbare heelal staan."),
        ]),
    ],
    onthoud=[
        "Gelijk lost op in gelijk: polaire stoffen lossen goed op in water, apolaire niet.",
        "Zouten en hydroxiden dissociëren: de ionen zaten al in het rooster en komen los.",
        "Zuren ioniseren: de molecule valt uiteen in ionen die er nog niet waren.",
        "Een elektrolyt geleidt in water doordat ze ionen vormt; suiker is een niet-elektrolyt.",
        "Onder pH 7 is zuur, 7 is neutraal, boven 7 is basisch; elke eenheid is een factor tien.",
        "Bij een neutralisatie ontstaan uit een zuur en een base een zout en water.",
        "Oxidatie is elektronen afstaan, reductie is elektronen opnemen.",
        "Massa = stofhoeveelheid maal molaire massa.",
        "Molaire concentratie = aantal mol gedeeld door volume in liter.",
    ],
)

# ───────────────────────── 14. Rechtlijnige bewegingen
BUNDELS["rechtlijnige-bewegingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rechtlijnige bewegingen",
    onder="De ERB en de EVRB, het verschil tussen afgelegde weg en verplaatsing, en hoe je de drie grafieken leest.",
    secties=[
        dict(kop="Positie, weg en verplaatsing", blokken=[
            ("p", "Een <strong>puntmassa</strong> is een voorwerp waarvan je de "
                  "<strong>afmetingen verwaarloost</strong>: je doet alsof de hele massa in één punt zit. "
                  "Voor een auto op de snelweg is dat een prima benadering."),
            ("p", "De <strong>afgelegde weg</strong> is de <strong>hele baan</strong> die je volgt. De "
                  "<strong>verplaatsing</strong> gaat alleen <strong>van begin naar eind</strong>. Rijd je "
                  "10 kilometer naar het oosten en 10 kilometer terug, dan is de afgelegde weg "
                  "<strong>20 kilometer</strong> en de verplaatsing <strong>nul</strong>. De verplaatsing "
                  "is dus nooit groter dan de afgelegde weg."),
            ("p", "Een <strong>tijdstip</strong> is een moment op de klok; het "
                  "<strong>tijdsverloop</strong> is het <strong>verschil tussen twee tijdstippen</strong>."),
            ("p", "<strong>Verplaatsing, snelheid en versnelling</strong> zijn "
                  "<strong>vectoriële grootheden</strong>: je stelt ze voor met een pijl. De "
                  "<strong>vier kenmerken</strong> van een vector zijn de <strong>grootte</strong>, de "
                  "<strong>richting</strong>, de <strong>zin</strong> en het "
                  "<strong>aangrijpingspunt</strong>. Het tijdsverloop is geen vector, dat is gewoon een "
                  "getal met een eenheid."),
        ]),
        dict(kop="De eenparig rechtlijnige beweging", blokken=[
            ("p", "Bij een <strong>eenparig rechtlijnige beweging</strong> of <strong>ERB</strong> blijft "
                  "de <strong>snelheid onveranderd</strong> en is de <strong>baan een rechte lijn</strong>. "
                  "In elke seconde wordt dus dezelfde afstand afgelegd."),
            ("p", "De <strong>gemiddelde snelheid</strong> is de <strong>verplaatsing gedeeld door het "
                  "tijdsverloop</strong>. Rijd je 150 kilometer in 2 uur, dan is dat "
                  "<strong>75 kilometer per uur</strong>. Om van kilometer per uur naar "
                  "<strong>meter per seconde</strong> te gaan, deel je door <strong>3,6</strong>: 36 "
                  "kilometer per uur is 10 meter per seconde."),
            ("p", "De <strong>positiefunctie</strong> van een ERB telt bij de "
                  "<strong>beginpositie</strong> de verplaatsing op. Start je op 20 meter en rijd je met 5 "
                  "meter per seconde, dan zit je na 4 seconden op <strong>40 meter</strong>."),
            ("p", tabel(["Grafiek", "Bij een ERB", "Wat je eruit haalt"], [
                ["x(t)", "een rechte lijn", "de steilheid is de snelheid"],
                ["v(t)", "een vlakke rechte lijn", "de oppervlakte eronder is de verplaatsing"],
                ["a(t)", "ze ligt op de tijdas", "er is geen versnelling"],
            ])),
            ("p", "Een <strong>vlak stuk in een x(t)-grafiek</strong> betekent dezelfde positie op elk "
                  "tijdstip: de puntmassa <strong>staat stil</strong>, een <strong>rustpauze</strong>. Een "
                  "<strong>negatieve snelheid</strong> in een v(t)-grafiek betekent dat de beweging "
                  "<strong>tegengesteld aan de zin van de x-as</strong> gaat; hoe snel het gaat, lees je "
                  "aan de grootte."),
            ("p", "Zolang de puntmassa <strong>niet van zin verandert</strong>, zijn de afgelegde weg en "
                  "de verplaatsing <strong>gelijk</strong>."),
        ]),
        dict(kop="De eenparig veranderlijke rechtlijnige beweging", blokken=[
            ("p", "Bij een <strong>eenparig veranderlijke rechtlijnige beweging</strong> of "
                  "<strong>EVRB</strong> blijft de <strong>versnelling onveranderd</strong> en is de baan "
                  "een rechte lijn. De snelheid verandert dan in elke seconde evenveel."),
            ("p", "De <strong>versnelling</strong> is de <strong>verandering van de snelheid per "
                  "tijdseenheid</strong>. Haar symbool is <strong>a</strong> en haar eenheid "
                  "<strong>meter per seconde kwadraat</strong>: meter per seconde, en dat per seconde "
                  "opnieuw. Start je uit stilstand met 3 meter per seconde kwadraat, dan heb je na 4 "
                  "seconden <strong>12 meter per seconde</strong>."),
            ("p", tabel(["Grafiek", "Bij een EVRB", "Wat je eruit haalt"], [
                ["x(t)", "een kromme, want de steilheid verandert", "de steilheid op één punt is de ogenblikkelijke snelheid"],
                ["v(t)", "een schuine rechte", "de steilheid is de versnelling, de oppervlakte eronder de verplaatsing"],
                ["a(t)", "een vlakke rechte", "boven de tijdas positief, eronder negatief"],
            ])),
            ("p", "<strong>Versnellen of vertragen?</strong> Je kijkt naar de "
                  "<strong>grootte</strong> van de snelheid, niet naar het teken. Gaat die omhoog, dan is "
                  "het versnellen; gaat ze omlaag, dan is het vertragen. Van min 2 naar min 8 is dus ook "
                  "versnellen. Rijdt een auto vooruit en is de versnelling <strong>negatief</strong>, dan "
                  "<strong>vertraagt</strong> hij."),
            ("p", "Een v(t)-grafiek die van 20 meter per seconde naar nul daalt in 5 seconden geeft een "
                  "versnelling van <strong>min 4 meter per seconde kwadraat</strong>. De "
                  "<strong>oppervlakte onder die driehoek</strong> is de afgelegde weg: de helft van 20 "
                  "maal 5, dus <strong>50 meter</strong> remweg."),
            ("p", "Ligt de <strong>a(t)-grafiek op de tijdas</strong>, dan <strong>behoudt</strong> het "
                  "voorwerp zijn snelheid. Die mag ook nul zijn, maar rijdt het, dan rijdt het gewoon "
                  "verder."),
        ]),
        dict(kop="Inhalen en kruisen", blokken=[
            ("p", "Twee bewegingen samen leg je naast elkaar in <strong>één x(t)-grafiek</strong>. Het "
                  "<strong>snijpunt</strong> van de twee lijnen is het moment waarop ze op "
                  "<strong>hetzelfde tijdstip op dezelfde positie</strong> zijn: daar halen ze elkaar in "
                  "of kruisen ze."),
            ("p", "Vertrekken twee wandelaars op hetzelfde ogenblik vanuit dezelfde plaats met een "
                  "verschillende snelheid, dan krijg je <strong>twee rechten vanuit hetzelfde punt</strong>, "
                  "waarvan de snelste de <strong>steilste</strong> is. Ze lopen daarna alleen maar verder "
                  "uiteen."),
            ("p", "Van twee auto's met een v(t)-grafiek die vanuit nul stijgt, heeft de auto met de "
                  "<strong>steilste lijn de grootste versnelling</strong>. Zo vergelijk je bewegingen "
                  "zonder één getal te berekenen."),
            ("weetje", "Je kan de oppervlakte onder een v(t)-grafiek ook gewoon in vakjes tellen. Bij een "
                       "kromme lijn is dat vaak de snelste manier om toch een goede schatting van de "
                       "afgelegde weg te krijgen."),
        ]),
    ],
    onthoud=[
        "Een puntmassa is een voorwerp waarvan je de afmetingen verwaarloost.",
        "De afgelegde weg is de hele baan, de verplaatsing gaat alleen van begin naar eind.",
        "Een vector heeft vier kenmerken: grootte, richting, zin en aangrijpingspunt.",
        "ERB: de snelheid blijft onveranderd en de baan is een rechte lijn.",
        "Gemiddelde snelheid = verplaatsing gedeeld door tijdsverloop. Van kilometer per uur naar meter per seconde: delen door 3,6.",
        "EVRB: de versnelling blijft onveranderd; haar eenheid is meter per seconde kwadraat.",
        "In een v(t)-grafiek is de steilheid de versnelling en de oppervlakte eronder de verplaatsing.",
        "Versnellen of vertragen lees je aan de grootte van de snelheid, niet aan het teken.",
        "Het snijpunt van twee lijnen in een x(t)-grafiek is waar ze elkaar inhalen of kruisen.",
    ],
)

# ───────────────────────── 15. Vrije val, verticale worp en krachten
BUNDELS["vrije-val-verticale-worp-en-krachten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Vrije val, verticale worp en krachten",
    onder="De vrije val en de verticale worp, de soorten krachten, de krachtenbalans en de veerkracht.",
    secties=[
        dict(kop="Vrije val en verticale worp", blokken=[
            ("p", "Bij een <strong>vrije val</strong> werkt er <strong>alleen de zwaartekracht</strong> op "
                  "het voorwerp; de luchtweerstand verwaarloos je. Daardoor "
                  "<strong>valt elk voorwerp even snel</strong>, hoe zwaar het ook is: een steen en een "
                  "pluim samen. In lucht wint de steen alleen doordat de pluim veel meer weerstand "
                  "ondervindt."),
            ("p", "De <strong>valversnelling</strong> op aarde is ongeveer "
                  "<strong>9,81 meter per seconde kwadraat</strong>; op de maan maar 1,62. Elke seconde "
                  "komt er dus ongeveer 9,81 meter per seconde snelheid bij. Valt een steen uit stilstand, "
                  "dan heeft hij na 2 seconden ongeveer <strong>20 meter per seconde</strong> als je met 10 "
                  "rekent."),
            ("p", "Bij een <strong>verticale worp naar boven</strong> is de versnelling tijdens het "
                  "opgaan <strong>naar beneden</strong> gericht: de zwaartekracht werkt altijd naar "
                  "beneden, en daarom wordt de bal <strong>vertraagd</strong>. In het "
                  "<strong>hoogste punt</strong> is de <strong>snelheid nul</strong> maar blijft de "
                  "<strong>versnelling naar beneden</strong> gericht, en daarom gaat de bal onmiddellijk "
                  "weer naar beneden."),
            ("p", "Tijdens een vrije val <strong>blijft de versnelling gelijk</strong>; het is de "
                  "<strong>snelheid</strong> die steeds groter wordt. Gooi je een bal recht naar beneden in "
                  "plaats van hem te laten vallen, dan heeft hij alleen een "
                  "<strong>beginsnelheid</strong>, maar dezelfde versnelling."),
        ]),
        dict(kop="Krachten", blokken=[
            ("p", "Een <strong>kracht</strong> is een <strong>vectoriële grootheid</strong> met een "
                  "grootte, een richting, een zin en een aangrijpingspunt. De eenheid is de "
                  "<strong>newton</strong>: één newton doet een massa van één kilogram één meter per "
                  "seconde kwadraat versnellen."),
            ("p", tabel(["Soort kracht", "Waar ze van komt"], [
                ["Zwaartekracht", "de aarde trekt het voorwerp naar haar middelpunt"],
                ["Normaalkracht", "een oppervlak duwt loodrecht terug"],
                ["Wrijvingskracht", "tegenwerking bij schuiven of rollen"],
                ["Veerkracht", "een uitgerekte of ingedrukte veer"],
                ["Spankracht", "een gespannen koord of kabel"],
                ["Motorkracht", "een motor die duwt of trekt"],
            ])),
            ("p", "Een <strong>resulterende kracht</strong> die niet nul is, verandert de "
                  "<strong>bewegingstoestand</strong>, en dat kan op drie manieren: "
                  "<strong>versnellen</strong>, <strong>vertragen</strong> of <strong>van richting "
                  "veranderen</strong>. De massa van een voorwerp verandert niet door een kracht."),
            ("p", "Omgekeerd: een voorwerp dat <strong>stilstaat of met een constante snelheid in een "
                  "rechte lijn beweegt</strong>, heeft een <strong>resulterende kracht van nul</strong>. "
                  "Dat heet een <strong>krachtenbalans</strong>. Een boek op een tafel heeft de "
                  "zwaartekracht naar beneden en de normaalkracht naar boven, precies even groot."),
            ("p", "Een <strong>parachutist</strong> die met constante snelheid valt, heeft een "
                  "<strong>luchtweerstand die even groot is als de zwaartekracht</strong>. Die snelheid "
                  "heet de eindsnelheid. Een auto die <strong>remt</strong> heeft een resulterende kracht "
                  "<strong>tegengesteld aan de beweging</strong>. Een <strong>kist op een helling</strong> "
                  "die niet wegschuift, wordt tegengehouden door de "
                  "<strong>wrijvingskracht</strong>."),
            ("p", "Hangt een gewicht <strong>stil</strong> aan een koord, dan verricht geen enkele kracht "
                  "erop arbeid: er is immers <strong>geen verplaatsing</strong>."),
        ]),
        dict(kop="Krachten samenstellen", blokken=[
            ("p", "De <strong>resultante</strong> is de ene kracht die hetzelfde effect heeft als alle "
                  "krachten samen. Werken twee krachten in <strong>dezelfde richting en zin</strong>, dan "
                  "<strong>tel je hun groottes op</strong>: 30 en 40 newton geven "
                  "<strong>70 newton</strong>. Bij <strong>tegengestelde zin</strong> trek je ze van elkaar "
                  "af; gelijke groottes geven dan <strong>nul</strong>."),
            ("p", "Maken twee krachten een <strong>hoek van 90 graden</strong>, dan gebruik je de "
                  "<strong>stelling van Pythagoras</strong>: 30 en 40 newton geven "
                  "<strong>50 newton</strong>, want de wortel uit 900 plus 1600 is 50."),
        ]),
        dict(kop="Zwaartekracht, massa en gewicht", blokken=[
            ("p", "De <strong>zwaartekracht</strong> is de <strong>massa maal de "
                  "zwaarteveldsterkte</strong>. Op aarde is die sterkte ongeveer "
                  "<strong>9,81 newton per kilogram</strong>, op de maan 1,62. Een massa van 2 kilogram "
                  "heeft dus een zwaartekracht van <strong>20 newton</strong> als je met 10 rekent."),
            ("p", "<strong>Massa</strong> is de <strong>hoeveelheid materie</strong> en blijft overal "
                  "dezelfde, ook op de maan. <strong>Gewicht</strong> is een <strong>kracht</strong> en "
                  "meet je in <strong>newton</strong>, niet in kilogram; op de maan is je gewicht zes keer "
                  "kleiner. Een <strong>dynamometer</strong> meet een kracht rechtstreeks; het is in de "
                  "kern een veer met een schaal erop."),
            ("p", "De zwaartekracht is een <strong>veldkracht</strong>: ze werkt "
                  "<strong>zonder contact</strong>. Een normaalkracht of een wrijvingskracht heeft wel "
                  "contact nodig. Het <strong>zwaartepunt</strong> is het punt waarin je de hele "
                  "zwaartekracht laat aangrijpen; of een voorwerp omvalt, hangt af van waar dat punt zit."),
            ("p", "Zet je de gemeten zwaartekracht tegenover de massa in een grafiek, dan krijg je een "
                  "<strong>rechte door de oorsprong</strong>, want de twee zijn "
                  "<strong>recht evenredig</strong>. De <strong>steilheid</strong> van die rechte is de "
                  "<strong>zwaarteveldsterkte</strong>, en zo kan je uit meetresultaten afleiden op welk "
                  "hemellichaam gemeten is."),
            ("p", "Een astronaut die in een <strong>ruimtestation zweeft</strong> is "
                  "<strong>gewichtloos</strong>, maar niet massaloos: met zijn massa is "
                  "<strong>niets gebeurd</strong>, ze is <strong>net dezelfde als op aarde</strong>. Het station en de "
                  "astronaut vallen samen rond de aarde, en daarom voelt hij geen druk van een vloer."),
        ]),
        dict(kop="De veerkracht", blokken=[
            ("p", "De <strong>veerkracht</strong> is de <strong>veerconstante maal de "
                  "lengteverandering</strong>. De veerkracht is dus <strong>recht evenredig</strong> met "
                  "hoeveel de veer uitrekt, en de <strong>veerconstante</strong> zegt hoe stug de veer is. "
                  "Een <strong>grotere veerconstante</strong> betekent dat de veer bij dezelfde kracht "
                  "<strong>minder uitrekt</strong>."),
            ("p", "Rekt een veer 4 centimeter uit bij 20 newton, dan is de veerconstante "
                  "<strong>5 newton per centimeter</strong>. Met die constante voorspel je elke andere "
                  "uitrekking."),
            ("p", "Hangt een voorwerp <strong>stil</strong> aan een veer, dan is er een "
                  "<strong>krachtenbalans</strong>: de <strong>veerkracht is even groot als de "
                  "zwaartekracht</strong>. Een voorwerp van 5 kilogram geeft dus een veerkracht van "
                  "<strong>50 newton</strong> als je met 10 newton per kilogram rekent. Daarom kan je uit "
                  "de massa alleen de veerkracht berekenen."),
            ("weetje", "Een weegschaal in de winkel meet eigenlijk een kracht, geen massa. Ze rekent die "
                       "kracht voor jou om naar kilogram, en dat lukt alleen doordat de "
                       "zwaarteveldsterkte op aarde zo goed als overal gelijk is."),
        ]),
    ],
    onthoud=[
        "Bij een vrije val werkt alleen de zwaartekracht, en valt elk voorwerp even snel.",
        "De valversnelling op aarde is ongeveer 9,81 meter per seconde kwadraat.",
        "In het hoogste punt van een verticale worp is de snelheid nul, de versnelling blijft naar beneden.",
        "Een resulterende kracht die niet nul is, verandert de bewegingstoestand.",
        "Stilstaan of constante snelheid in een rechte lijn: resulterende kracht nul, een krachtenbalans.",
        "Bij een hoek van 90 graden gebruik je Pythagoras: 30 en 40 newton geven 50 newton.",
        "Zwaartekracht = massa maal zwaarteveldsterkte, op aarde ongeveer 9,81 newton per kilogram.",
        "Massa blijft overal dezelfde; gewicht is een kracht en meet je in newton.",
        "Veerkracht = veerconstante maal lengteverandering.",
    ],
)

# ───────────────────────── 16. Druk en de gaswetten
BUNDELS["druk-en-de-gaswetten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Druk en de gaswetten",
    onder="Druk op een oppervlak, de hydrostatische druk, het beginsel van Pascal en de gaswetten.",
    secties=[
        dict(kop="Druk op een oppervlak", blokken=[
            ("p", "De <strong>druk</strong> is de <strong>kracht gedeeld door de oppervlakte</strong>. De "
                  "SI-eenheid is de <strong>pascal</strong>: één newton per vierkante meter. Voor het weer "
                  "gebruiken we handiger eenheden: <strong>kilopascal, hectopascal, millibar en bar</strong>. "
                  "Eén bar is <strong>100 000 pascal</strong>, ongeveer de luchtdruk op zeeniveau, en dat "
                  "lees je in het weerbericht als 1000 hectopascal."),
            ("p", "Bij <strong>dezelfde kracht</strong> geeft een <strong>kleiner oppervlak een grotere "
                  "druk</strong>. Daarom snijdt een scherp mes beter dan een bot mes, en daarom dringt een "
                  "naald zo gemakkelijk binnen. Duw je met 200 newton op 0,5 vierkante meter, dan is de "
                  "druk <strong>400 pascal</strong>."),
            ("p", "Met <strong>sneeuwschoenen</strong> zak je minder diep weg: je gewicht verandert niet, "
                  "maar het <strong>zooloppervlak is groter</strong> en dus de druk kleiner. Een naaldhak "
                  "doet precies het omgekeerde. Bij <strong>dezelfde schoenmaat</strong> zakt de "
                  "<strong>zwaarste persoon</strong> het diepst, want zijn kracht op de modder is groter."),
            ("p", "Leg je dezelfde baksteen op zijn <strong>smalle kant</strong>, dan blijft de "
                  "<strong>kracht gelijk</strong> maar wordt de <strong>druk groter</strong>, want het "
                  "contactoppervlak is kleiner. De druk hangt dus af van de "
                  "<strong>kracht</strong>, van het <strong>oppervlak</strong> en daarmee ook van de "
                  "<strong>stand</strong> van het voorwerp, maar niet van de kleur."),
        ]),
        dict(kop="Druk in vloeistoffen", blokken=[
            ("p", "De <strong>hydrostatische druk</strong> ontstaat door het "
                  "<strong>gewicht van de vloeistof zelf</strong>. Ze hangt af van de "
                  "<strong>diepte</strong>, van de <strong>massadichtheid</strong> van de vloeistof en van "
                  "de <strong>zwaarteveldsterkte</strong>. Hoe breed of smal het vat is, maakt niets uit."),
            ("p", "Op <strong>tien meter diepte</strong> is de druk dus groter dan op twee meter: boven je "
                  "hoofd staat vijf keer zo veel water. Elke tien meter water voegt ongeveer "
                  "<strong>één bar</strong> toe. De <strong>totale druk</strong> is de "
                  "<strong>luchtdruk plus de hydrostatische druk</strong>: de atmosfeer duwt immers ook op "
                  "het wateroppervlak."),
            ("p", "Daarom moet je bij het <strong>duiken je oren klaren</strong>: de waterdruk duwt op je "
                  "trommelvlies terwijl er binnen nog de oude druk staat. Door te klaren laat je lucht in "
                  "je middenoor, zodat de druk aan beide kanten gelijk wordt."),
            ("p", "Het <strong>beginsel van Pascal</strong> zegt dat een "
                  "<strong>drukverandering zich in een vloeistof in alle richtingen voortplant</strong>. "
                  "Daarom werkt een <strong>hydraulische rem</strong>: je duwt op het pedaal en de druk "
                  "komt onverminderd bij alle vier de wielen aan. In een "
                  "<strong>hydraulische pers</strong> is de druk overal gelijk maar werkt ze op een "
                  "<strong>veel groter oppervlak</strong>, en kracht is druk maal oppervlakte: tien keer "
                  "meer oppervlak geeft tien keer meer kracht, over een tien keer kortere weg."),
            ("p", "Een <strong>barometer</strong> meet de <strong>luchtdruk</strong> buiten; een "
                  "<strong>manometer</strong> meet de druk van een gas of vloeistof in een "
                  "<strong>vat of leiding</strong>, zoals op een gasfles of een fietspomp. De luchtdruk "
                  "<strong>neemt af als je hoger komt</strong>, want er staat minder lucht boven je. "
                  "<strong>Overdruk</strong> is hoger dan de <strong>omgevingsdruk</strong>, "
                  "<strong>onderdruk</strong> lager; een zuignap werkt op onderdruk."),
        ]),
        dict(kop="Druk in gassen", blokken=[
            ("p", "Volgens het <strong>deeltjesmodel</strong> ontstaat de druk van een gas doordat de "
                  "deeltjes <strong>tegen de wand botsen</strong> en daar bij elke botsing op duwen. "
                  "Miljarden botsingen per seconde geven samen een gelijkmatige druk. Een gas oefent dus "
                  "druk uit <strong>in alle richtingen</strong>, ook naar boven."),
            ("p", "Pers je een gas in een <strong>kleiner volume</strong> bij gelijke temperatuur, dan "
                  "raakt elk deeltje de wand vaker en wordt de <strong>druk groter</strong>. Verwarm je een "
                  "gas in een <strong>gesloten stalen fles</strong>, dan gaan de deeltjes sneller bewegen, "
                  "botsen ze harder, en <strong>stijgt de druk</strong>. Daarom staat er op een spuitbus "
                  "dat je ze niet mag verwarmen."),
            ("p", "De <strong>temperatuurschaal</strong> die bij het absolute nulpunt begint, is de "
                  "<strong>kelvinschaal</strong>. Die begint bij het <strong>absolute nulpunt</strong>, bij "
                  "<strong>min 273,15 graden Celsius</strong>. Daar hebben de deeltjes "
                  "<strong>geen kinetische energie</strong> meer, zou de <strong>druk nul</strong> zijn, en "
                  "<strong>lager kan niet</strong>, want trager dan stil bestaat niet. Je telt "
                  "<strong>273</strong> bij de graden Celsius op: 27 graden is <strong>300 kelvin</strong>, "
                  "en 273 kelvin is <strong>0 graden</strong> Celsius."),
        ]),
        dict(kop="De gaswetten", blokken=[
            ("kader", "<p>De gaswetten en de kelvinschaal staan enkel in de uitgebreide fiche, dus voor "
                      "moderne talen en Latijn.</p>"),
            ("p", "De <strong>toestandsgrootheden</strong> van een gas zijn de <strong>druk</strong>, het "
                  "<strong>volume</strong>, de <strong>absolute temperatuur</strong> en de "
                  "<strong>stofhoeveelheid</strong>. Het vat waarin het gas zit, hoort daar niet bij."),
            ("p", tabel(["Proces", "Wat constant blijft", "Wat er dan geldt"], [
                ["Isotherm", "de temperatuur", "druk maal volume blijft gelijk"],
                ["Isobaar", "de druk", "volume en temperatuur zijn recht evenredig"],
                ["Isochoor", "het volume", "druk en temperatuur zijn recht evenredig"],
            ])),
            ("p", "Bij een <strong>isotherm</strong> proces is de grafiek van de druk tegenover het "
                  "volume een <strong>kromme die daalt</strong>: de twee zijn "
                  "<strong>omgekeerd evenredig</strong>, dus buigt de kromme naar de assen toe zonder ze te "
                  "raken. Een gas van 2 liter bij 1 bar dat tot 1 liter samengeperst wordt, komt op "
                  "<strong>2 bar</strong>."),
            ("p", "Bij een <strong>isochoor</strong> proces zijn druk en absolute temperatuur "
                  "<strong>recht evenredig</strong>: een gas van 300 kelvin bij 1 bar dat tot 600 kelvin "
                  "verwarmd wordt, komt op <strong>2 bar</strong>. In de gaswetten moet je de temperatuur "
                  "daarom <strong>altijd in kelvin</strong> invullen; met graden Celsius kom je bij nul "
                  "graden op een onmogelijke uitkomst."),
            ("p", "Een <strong>ballon in de koelkast</strong> loopt wat leeg: de deeltjes bewegen trager, "
                  "en omdat de ballon van vorm kan veranderen past het <strong>volume</strong> zich aan tot "
                  "de druk weer in balans is met de buitenlucht. Dat is een <strong>isobaar</strong> proces."),
            ("p", "Een <strong>ideaal gas</strong> volgt die wetten precies. Een "
                  "<strong>reëel gas</strong> wijkt af bij <strong>hoge druk of lage temperatuur</strong>: "
                  "dan gaan de deeltjes elkaar aantrekken en nemen ze zelf plaats in."),
            ("weetje", "Een fietsband wordt warm als je hem oppompt. Je perst de lucht samen en voert er "
                       "daarbij energie aan toe; de wrijving in de pomp speelt ook mee, maar is niet de "
                       "hoofdoorzaak."),
        ]),
    ],
    onthoud=[
        "Druk = kracht gedeeld door oppervlakte, in pascal: één newton per vierkante meter.",
        "Bij dezelfde kracht geeft een kleiner oppervlak een grotere druk.",
        "De hydrostatische druk hangt af van diepte, massadichtheid en zwaarteveldsterkte, niet van de breedte van het vat.",
        "Elke tien meter water voegt ongeveer één bar toe.",
        "Beginsel van Pascal: een drukverandering plant zich in een vloeistof in alle richtingen voort.",
        "Een barometer meet de luchtdruk, een manometer de druk in een vat of leiding.",
        "De kelvinschaal begint bij het absolute nulpunt, min 273,15 graden Celsius.",
        "Isotherm: druk maal volume blijft gelijk. Isochoor: druk en absolute temperatuur zijn recht evenredig.",
        "In de gaswetten vul je de temperatuur altijd in kelvin in.",
    ],
)

# ───────────────────────── 17. Arbeid, energie, vermogen en rendement
BUNDELS["arbeid-energie-vermogen-en-rendement-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Arbeid, energie, vermogen en rendement",
    onder="Wanneer een kracht arbeid verricht, de energievormen en hun formules, en hoe je vermogen en rendement berekent.",
    secties=[
        dict(kop="Arbeid", blokken=[
            ("kader", "<p>Arbeid staat enkel in de uitgebreide fiche, dus voor moderne talen en "
                      "Latijn.</p>"),
            ("p", "Een kracht verricht <strong>arbeid</strong> als het voorwerp zich "
                  "<strong>verplaatst</strong> terwijl die kracht erop werkt. Duw je tegen een muur die "
                  "niet beweegt, dan verricht je in de natuurkundige zin "
                  "<strong>geen arbeid</strong>. Hangt een <strong>gewicht stil aan een koord</strong>, "
                  "dan verricht de <strong>spankracht</strong> om dezelfde reden "
                  "<strong>geen arbeid, want er is geen verplaatsing</strong>. De eenheid is de <strong>joule</strong>: één newton over "
                  "één meter."),
            ("p", "Werkt de kracht <strong>in dezelfde zin</strong> als de verplaatsing, dan is de arbeid "
                  "<strong>positief</strong>; werkt ze <strong>tegengesteld</strong>, dan is de arbeid "
                  "<strong>negatief</strong> (de wrijvingskracht). Staat ze "
                  "<strong>loodrecht</strong> op de verplaatsing, dan verricht ze "
                  "<strong>geen arbeid</strong>: de cosinus van 90 graden is nul."),
            ("p", "Duw je een doos 3 meter ver met 40 newton in de zin van de beweging, dan is de arbeid "
                  "<strong>120 joule</strong>: kracht maal verplaatsing. Werkt de kracht onder een hoek, "
                  "dan komt er nog een cosinus bij."),
        ]),
        dict(kop="De energievormen", blokken=[
            ("p", "De <strong>energievormen</strong> zijn de <strong>gravitationele potentiële "
                  "energie</strong>, de <strong>elastische potentiële energie</strong>, de "
                  "<strong>kinetische energie</strong>, de <strong>chemische energie</strong>, de "
                  "<strong>thermische energie</strong> of warmte, de <strong>stralingsenergie</strong>, de "
                  "<strong>kernenergie</strong> en de <strong>elektrische energie</strong>. Wrijving is "
                  "geen energievorm maar een kracht die energie in warmte omzet."),
            ("p", tabel(["Energievorm", "Hoe je ze berekent", "Waarvan ze afhangt"], [
                ["Kinetische energie", "de helft van massa maal snelheid in het kwadraat", "massa en snelheid"],
                ["Gravitationele potentiële energie", "massa maal zwaarteveldsterkte maal hoogte", "massa, hoogte en de plaats"],
                ["Elastische potentiële energie", "de helft van veerconstante maal uitrekking in het kwadraat", "veerconstante en uitrekking"],
            ])),
            ("p", "Omdat de <strong>snelheid in het kwadraat</strong> staat, weegt die zwaar door: "
                  "<strong>twee keer zo snel is vier keer zo veel kinetische energie</strong>, en daarom "
                  "wordt de remweg bij dubbele snelheid veel meer dan dubbel zo lang. Een voorwerp van 2 "
                  "kilogram met 3 meter per seconde heeft <strong>9 joule</strong>. Bij de elastische "
                  "energie staat de uitrekking om dezelfde reden in het kwadraat."),
            ("p", "Energie meet je in <strong>joule</strong>, maar ook in "
                  "<strong>kilowattuur</strong> (je elektriciteitsfactuur) en in "
                  "<strong>kilocalorie</strong> (een voedingslabel). De newton is géén energie-eenheid, en "
                  "een <strong>kilowattuur is energie, geen vermogen</strong>."),
        ]),
        dict(kop="Energieomzettingen", blokken=[
            ("p", "De <strong>wet van behoud van energie</strong> zegt dat energie "
                  "<strong>niet kan verdwijnen</strong>, enkel <strong>van vorm veranderen</strong>. Wat je "
                  "aan de ene kant verliest, vind je ergens anders terug, vaak als warmte."),
            ("p", "Bij een <strong>vallende steen</strong> wordt gravitationele potentiële energie "
                  "kinetische energie. Bij een <strong>uitgerekte katapult</strong> sla je elastische "
                  "energie op, die bij het lossen kinetische energie wordt. In een "
                  "<strong>lamp</strong> wordt elektrische energie stralingsenergie en warmte."),
            ("p", "De <strong>energiebalans</strong> van een <strong>slingerende schommel</strong>: de "
                  "hoogte-energie is het grootst in het "
                  "<strong>hoogste punt</strong> en de kinetische energie het grootst in het "
                  "<strong>laagste punt</strong>. In het hoogste punt staat de schommel een ogenblik stil, "
                  "dus is zijn kinetische energie daar juist nul. <strong>Zonder wrijving blijft de som "
                  "van de twee gelijk.</strong>"),
            ("p", "Een bal van 1 kilogram die 5 meter valt heeft net voor de bodem "
                  "<strong>50 joule</strong> kinetische energie, als je met 10 newton per kilogram rekent "
                  "en de luchtweerstand verwaarloost: alle hoogte-energie is dan omgezet."),
            ("p", "<strong>Energiedissipatie</strong> is bruikbare energie die in een "
                  "<strong>minder bruikbare vorm</strong> omgezet wordt, meestal <strong>warmte</strong>. "
                  "De energie is er nog, maar je kan er weinig nuttigs meer mee doen. Daarom wordt een "
                  "<strong>rem warm</strong> bij een afdaling: de wrijvingskracht verricht negatieve arbeid "
                  "op de fiets, en die energie wordt warmte in de rem."),
            ("p", "Een <strong>stroomdiagram</strong> toont hoe de energie bij een omzetting over de "
                  "vormen verdeeld wordt; de breedte van de pijlen zegt hoeveel er naar welke vorm gaat. "
                  "Alles wat erin gaat, moet er ook weer uit komen."),
            ("p", tabel(["Systeem", "Wisselt uit met de omgeving"], [
                ["Open systeem", "energie én materie (een open kookpot)"],
                ["Gesloten systeem", "alleen energie (een pot met een deksel)"],
                ["Geïsoleerd systeem", "niets van beide (een thermos benadert dat)"],
            ])),
        ]),
        dict(kop="Vermogen en rendement", blokken=[
            ("p", "Het <strong>vermogen</strong> is de <strong>omgezette energie gedeeld door de "
                  "tijd</strong>, in <strong>watt</strong>: joule per seconde. Een motor die 400 joule "
                  "omzet in 5 seconden heeft een vermogen van <strong>80 watt</strong>. Een toestel met een "
                  "<strong>groter vermogen zet in dezelfde tijd meer energie om</strong>, en daarom kookt "
                  "een waterkoker van 2000 watt sneller dan een van 1000 watt."),
            ("p", "Omgekeerd: een toestel van <strong>2000 watt</strong> dat een <strong>half uur</strong> "
                  "aanstaat gebruikt <strong>1 kilowattuur</strong>. Je vermenigvuldigt het vermogen in "
                  "kilowatt met de tijd in uur, en zo rekent ook je elektriciteitsmeter."),
            ("p", "Het <strong>rendement</strong> is de <strong>nuttige energie gedeeld door de totale "
                  "energie</strong>, meestal in procent. Van 1000 joule met 250 joule nuttig is het "
                  "rendement <strong>25 procent</strong>. De <strong>ongewenste energie</strong> is de "
                  "<strong>totale min de nuttige</strong>."),
            ("p", "Een rendement <strong>boven honderd procent bestaat niet</strong>: er kan nooit meer "
                  "energie uit komen dan er in gaat. Een lamp die 100 joule krijgt en 5 joule licht geeft, "
                  "zet de overige <strong>95 joule in warmte</strong> om; bij een gloeilamp is dat het "
                  "grootste deel, en daarom heeft een <strong>ledlamp een veel beter rendement</strong>."),
            ("p", "Koken twee waterkokers dezelfde liter water, de ene op 2 en de andere op 4 minuten, dan "
                  "heeft de <strong>snelste het grootste vermogen</strong>: voor dezelfde energie in de "
                  "helft van de tijd heb je dubbel het vermogen nodig. Hun rendement kan daarnaast nog "
                  "verschillen."),
            ("weetje", "Ook bij een exotherme reactie moet je vaak eerst energie toevoeren om ze te "
                       "starten. Een gasvlam moet je aansteken; daarna houdt ze zichzelf gaande met de "
                       "warmte die ze zelf maakt."),
        ]),
    ],
    onthoud=[
        "Een kracht verricht arbeid als het voorwerp zich verplaatst terwijl die kracht erop werkt.",
        "Een kracht loodrecht op de verplaatsing verricht geen arbeid.",
        "Kinetische energie is de helft van massa maal snelheid in het kwadraat.",
        "Gravitationele potentiële energie is massa maal zwaarteveldsterkte maal hoogte.",
        "Een kilowattuur is energie, geen vermogen.",
        "Energie kan niet verdwijnen, enkel van vorm veranderen.",
        "Vermogen = omgezette energie gedeeld door de tijd, in watt.",
        "Rendement = nuttige energie gedeeld door totale energie; boven honderd procent bestaat niet.",
    ],
)

# ───────────────────────── 18. Warmte en faseovergangen
BUNDELS["warmte-en-faseovergangen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Warmte en faseovergangen",
    onder="Warmtetransport, het thermisch evenwicht, de merkbare en de latente warmte, en de faseovergangen.",
    secties=[
        dict(kop="Temperatuur en warmte", blokken=[
            ("p", "<strong>Temperatuur</strong> zegt hoe warm iets is en hangt samen met de "
                  "<strong>kinetische energie van de deeltjes</strong>: hoe sneller ze bewegen, hoe hoger "
                  "de temperatuur. <strong>Warmte</strong> is <strong>energie die overgaat</strong> en "
                  "meet je in <strong>joule</strong>. Het zijn dus twee verschillende dingen: een bad van "
                  "30 graden bevat veel meer warmte dan een kop thee van 60 graden."),
            ("p", "Warmte gaat <strong>altijd van warm naar koud</strong>. <strong>Koude bestaat niet</strong> "
                  "als iets dat overgaat: ze is alleen een gebrek aan warmte. Het "
                  "<strong>thermisch evenwicht</strong> is de toestand waarin beide voorwerpen "
                  "<strong>dezelfde temperatuur</strong> hebben; dan stopt de netto overdracht."),
            ("p", tabel(["Vorm van warmtetransport", "Hoe het werkt", "Stof nodig?"], [
                ["Geleiding", "de deeltjes geven hun beweging aan hun buren door", "ja"],
                ["Convectie of stroming", "de stof zelf verplaatst zich en neemt de warmte mee", "ja"],
                ["Straling", "de warmte gaat als golven door de ruimte", "neen"],
            ])),
            ("p", "<strong>Straling</strong> is de enige vorm die <strong>door het luchtledige</strong> "
                  "gaat; zo bereikt de warmte van de zon ons. In een "
                  "<strong>metalen staaf</strong> gaat de warmte door <strong>geleiding</strong>: de "
                  "deeltjes blijven op hun plaats en stoten hun buren aan, en in een metaal helpen de vrije "
                  "elektronen daarbij. Bij <strong>convectie</strong> stijgt warme lucht of warm water: "
                  "opwarmen doet een gas <strong>uitzetten</strong>, zijn massadichtheid zakt, en de "
                  "koudere lucht zakt eronder."),
            ("p", "<strong>Verdampen is een faseovergang</strong>, geen transportvorm. Let dus op het "
                  "verschil."),
        ]),
        dict(kop="Merkbare warmte", blokken=[
            ("p", "<strong>Merkbare warmte</strong> is de warmte die je <strong>merkt aan een "
                  "verandering van temperatuur</strong>. Je rekent ze als de "
                  "<strong>specifieke warmtecapaciteit maal de massa maal het temperatuurverschil</strong>."),
            ("p", "Een <strong>grote specifieke warmtecapaciteit</strong> betekent dat je "
                  "<strong>veel warmte nodig hebt om één kilogram één graad op te warmen</strong>. "
                  "<strong>Water</strong> heeft een heel grote warmtecapaciteit, ongeveer "
                  "<strong>4180 joule per kilogram per graad</strong>. Daarom warmt de zee veel langzamer "
                  "op dan het zand op het strand, en blijft ze in september nog warm terwijl de lucht al "
                  "afkoelt."),
            ("p", "Een stof met een <strong>kleine</strong> warmtecapaciteit warmt juist "
                  "<strong>snel op en koelt ook snel af</strong>. Verwarm je 2 kilogram water van 20 naar "
                  "30 graden, dan heb je <strong>83 600 joule</strong> nodig: 4180 maal 2 maal 10. De "
                  "benodigde warmte is <strong>recht evenredig met de massa</strong>, dus een hele liter "
                  "vraagt dubbel zo veel als een halve."),
            ("p", "Een <strong>tegelvloer voelt kouder aan dan een tapijt</strong> bij dezelfde "
                  "temperatuur, omdat de tegel de warmte van je voet veel "
                  "<strong>sneller wegleidt</strong>. Je voelt dus niet de temperatuur maar hoe snel je "
                  "warmte verliest."),
            ("p", "Een <strong>calorimeter</strong> of <strong>joulevat</strong> is zo goed geïsoleerd dat "
                  "je erin kan meten hoeveel warmte een stof opneemt of afgeeft. De "
                  "<strong>warmtebalans</strong> is een toepassing van de "
                  "<strong>wet van behoud van energie</strong>: wat het warme deel afgeeft, neemt het "
                  "koude deel op. Giet je een liter water van 80 graden bij een liter van 20 graden, dan "
                  "komt de eindtemperatuur op ongeveer <strong>50 graden</strong>, het gemiddelde."),
        ]),
        dict(kop="De faseovergangen", blokken=[
            ("p", tabel(["Overgang", "Van", "Naar", "Warmte"], [
                ["Smelten", "vast", "vloeibaar", "neemt op"],
                ["Stollen", "vloeibaar", "vast", "geeft af"],
                ["Verdampen", "vloeibaar", "gas", "neemt op"],
                ["Condenseren", "gas", "vloeibaar", "geeft af"],
                ["Sublimeren", "vast", "gas", "neemt op"],
                ["Desublimeren", "gas", "vast", "geeft af"],
            ])),
            ("p", "De overgangen naar een toestand met <strong>sterkere cohesiekrachten</strong> "
                  "(stollen, condenseren, desublimeren) <strong>geven warmte af</strong>; de andere drie "
                  "<strong>nemen warmte op</strong>. <strong>Cohesiekrachten</strong> zijn de krachten "
                  "waarmee de deeltjes van een stof elkaar vasthouden; hoe sterker ze zijn, hoe hoger het "
                  "smelt- en kookpunt."),
            ("p", "Bij het <strong>smelten</strong> komen de deeltjes <strong>los uit hun vaste plaats "
                  "maar blijven ze bij elkaar</strong>; in een vloeistof kunnen ze langs elkaar schuiven. "
                  "Pas bij <strong>verdampen</strong> laten ze elkaar echt los. "
                  "<strong>Droogijs</strong> sublimeert bij kamertemperatuur; <strong>rijm</strong> op een "
                  "koude ochtend ontstaat door desublimeren."),
            ("p", "Het <strong>smeltpunt en het stolpunt</strong> van een zuivere stof liggen bij "
                  "<strong>dezelfde temperatuur</strong>: alleen de richting verschilt. Water smelt en "
                  "stolt allebei bij nul graden."),
        ]),
        dict(kop="Latente warmte", blokken=[
            ("p", "Bij een <strong>faseovergang blijft de temperatuur gelijk</strong>. Alle toegevoerde "
                  "warmte gaat naar het <strong>verbreken of maken van de bindingen</strong> tussen de "
                  "deeltjes. Daarom heet ze <strong>latente</strong>, dus verborgen, warmte: je meet er "
                  "niets van op de thermometer."),
            ("p", "Daarom blijft ijs van nul graden <strong>op nul graden</strong> tot al het ijs "
                  "gesmolten is, en blijft kokend water op <strong>honderd graden</strong> hoe hard je ook "
                  "stookt; harder stoken maakt alleen dat het sneller leegkookt. In een "
                  "<strong>smeltcurve</strong> zie je dat als een <strong>vlak stuk</strong>, precies op "
                  "het smeltpunt."),
            ("p", "De <strong>latente warmte</strong> is de <strong>specifieke "
                  "faseovergangswarmte maal de massa</strong>. Er staat geen temperatuurverschil in, want "
                  "dat is tijdens een faseovergang nul. Om 0,5 kilogram ijs te smelten heb je dus "
                  "<strong>167 000 joule</strong> nodig, met 334 000 joule per kilogram."),
            ("p", "De <strong>verdampingswarmte van water is bijzonder groot</strong>: je hebt "
                  "<strong>meer warmte nodig om water bij honderd graden te laten verdampen dan om het "
                  "van nul naar honderd graden op te warmen</strong>. Daarom koelt "
                  "<strong>zweten</strong> zo goed: het verdampen haalt warmte uit je huid. En daarom "
                  "verbrand je je erger aan <strong>stoom</strong> dan aan water van honderd graden: bij "
                  "het <strong>condenseren</strong> op je huid komt de hele verdampingswarmte vrij."),
            ("p", "Een <strong>ijsblokje</strong> koelt je glas water af doordat het "
                  "<strong>warmte uit het water opneemt om te smelten</strong>, niet doordat het koude "
                  "afgeeft. En fruitboeren zetten bij nachtvorst water tussen de bomen, omdat het "
                  "<strong>stollen van dat water warmte afgeeft</strong>."),
            ("weetje", "Bij een warmtebalans met een faseovergang erin reken je de merkbare en de latente "
                       "warmte apart en telt ze daarna samen. Vergeet je het vlakke stuk, dan kom je altijd "
                       "te laag uit."),
        ]),
    ],
    onthoud=[
        "Temperatuur hangt samen met de kinetische energie van de deeltjes; warmte is energie die overgaat.",
        "Warmte gaat altijd van warm naar koud, tot het thermisch evenwicht.",
        "Geleiding en convectie hebben een stof nodig; straling gaat ook door het luchtledige.",
        "Merkbare warmte = specifieke warmtecapaciteit maal massa maal temperatuurverschil.",
        "Water heeft een heel grote warmtecapaciteit, ongeveer 4180 joule per kilogram per graad.",
        "Stollen, condenseren en desublimeren geven warmte af; smelten, verdampen en sublimeren nemen op.",
        "Bij een faseovergang blijft de temperatuur gelijk.",
        "Latente warmte = specifieke faseovergangswarmte maal de massa.",
        "Zweten koelt doordat het verdampen warmte uit je huid haalt.",
    ],
)

# ───────────────────────── 19. Elektriciteit en de wet van Ohm
BUNDELS["elektriciteit-en-de-wet-van-ohm-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Elektriciteit en de wet van Ohm",
    onder="Stroomsterkte, spanning en weerstand, het elektrisch vermogen, het Joule-effect en de veiligheid.",
    secties=[
        dict(kop="Stroomsterkte, spanning en weerstand", blokken=[
            ("p", tabel(["Grootheid", "Wat ze is", "Eenheid", "Meten met"], [
                ["Stroomsterkte", "de lading die per seconde voorbij een punt gaat", "ampère", "een ampèremeter"],
                ["Spanning", "het duwtje dat de lading in beweging zet", "volt", "een voltmeter"],
                ["Weerstand", "hoe sterk de kring de stroom tegenhoudt", "ohm", "een multimeter"],
            ])),
            ("p", "Eén <strong>ampère</strong> is één coulomb lading per seconde. Een "
                  "<strong>multimeter</strong> kan de drie grootheden meten, als je hem juist instelt; de "
                  "symbolen voor gelijkstroom en gelijkspanning staan erop. Een "
                  "<strong>barometer</strong> hoort niet in een stroomkring."),
            ("p", "De <strong>wet van Ohm</strong> zegt dat de <strong>weerstand de spanning gedeeld door "
                  "de stroomsterkte</strong> is. Je kan haar in elke richting gebruiken: 12 volt over 4 ohm "
                  "geeft <strong>3 ampère</strong>; 2 ampère door 5 ohm geeft "
                  "<strong>10 volt</strong>."),
            ("p", "Bij een <strong>vaste weerstand</strong> zijn spanning en stroomsterkte "
                  "<strong>recht evenredig</strong>: zet je ze in een grafiek, dan krijg je een "
                  "<strong>rechte door de oorsprong</strong>, en uit de steilheid haal je de weerstand. Bij "
                  "<strong>gelijke spanning</strong> zijn stroomsterkte en weerstand "
                  "<strong>omgekeerd evenredig</strong>: <strong>dubbele weerstand geeft halve "
                  "stroom</strong>. Zet je er een extra weerstand bij, dan brandt de lamp zwakker."),
        ]),
        dict(kop="Geleiders, isolatoren en de stroomkring", blokken=[
            ("p", "Een <strong>geleider</strong> heeft een <strong>kleine weerstand</strong>, en daardoor "
                  "loopt er bij dezelfde spanning <strong>meer stroom</strong>. Een "
                  "<strong>isolator</strong> heeft een <strong>heel grote weerstand</strong>. Daarom is de "
                  "kern van een draad koper en de mantel kunststof. <strong>Geleidbaarheid en weerstand "
                  "zijn tegengesteld</strong>: goed geleiden betekent een kleine weerstand. Een "
                  "<strong>groter geleidingsvermogen betekent dus een kleinere weerstand</strong>, geen "
                  "grotere. En een <strong>isolator heeft geen kleinere weerstand dan een "
                  "geleider</strong>, net het omgekeerde."),
            ("p", "<strong>Goede geleiders</strong> zijn koper en aluminium (vrije elektronen) en een "
                  "zoutoplossing (vrije ionen). <strong>Isolatoren</strong> zijn droog hout, rubber en "
                  "glas. Een <strong>lange, dunne draad</strong> heeft <strong>meer</strong> weerstand dan "
                  "een korte, dikke draad van dezelfde stof; daarom gebruikt men voor zware toestellen "
                  "dikkere draden."),
            ("p", "Een <strong>gelijkspanningsbron</strong> levert een spanning die "
                  "<strong>altijd dezelfde zin houdt</strong>, met een plus- en een minpool: een batterij. "
                  "Het stopcontact in huis levert wisselspanning. De "
                  "<strong>conventionele stroomzin</strong> loopt <strong>van plus naar min</strong>, de "
                  "<strong>werkelijke van min naar plus</strong>: de afspraak werd gemaakt voor men wist "
                  "dat elektronen negatief zijn."),
            ("p", "In een <strong>elektrisch schema</strong> heeft elk onderdeel zijn eigen symbool: een "
                  "gelijkspanningsbron, een al dan niet regelbare weerstand, een <strong>lamp</strong> "
                  "(gewoonlijk een rondje met een kruisje erin), een schakelaar, een ampèremeter en een "
                  "voltmeter. Zo kan iedereen hetzelfde schema lezen."),
        ]),
        dict(kop="Vermogen en het Joule-effect", blokken=[
            ("p", "Het <strong>vermogen</strong> van een elektrisch toestel zegt hoeveel "
                  "<strong>elektrische energie het per seconde omzet</strong>, in watt. Een toestel van "
                  "1000 watt dat twee uur aanstaat gebruikt <strong>2 kilowattuur</strong>. Bij "
                  "<strong>dezelfde spanning</strong> hoort een <strong>groter vermogen bij een grotere "
                  "stroom</strong>; daarom krijgt een elektrisch vuur een eigen, zwaardere kring."),
            ("p", "Van twee toestellen die <strong>hetzelfde werk doen</strong>, is het toestel met het "
                  "<strong>kleinste vermogen het zuinigst</strong>. Een ledlamp geeft met 7 watt zo veel "
                  "licht als een gloeilamp met 60 watt."),
            ("p", "Het <strong>Joule-effect</strong> is dat een <strong>geleider opwarmt doordat er stroom "
                  "door loopt</strong>: de elektronen botsen op de deeltjes van de geleider en geven daarbij "
                  "energie af. In een <strong>waterkoker is dat gewenst</strong>, in een "
                  "<strong>verlengsnoer ongewenst</strong>. Een <strong>te dun snoer</strong> heeft meer "
                  "weerstand en wordt dus heter; daarom staat er op een haspel hoeveel ampère hij mag "
                  "dragen."),
        ]),
        dict(kop="Risico's en veiligheid", blokken=[
            ("p", tabel(["Risico", "Wat er gebeurt"], [
                ["Kortsluiting", "de stroom vindt een weg met bijna geen weerstand en wordt heel groot"],
                ["Overbelasting", "te veel toestellen samen trekken meer stroom dan de draden dragen"],
                ["Brandgevaar", "door kortsluiting of overbelasting worden de draden heet"],
                ["Elektrocutie", "er loopt stroom door een menselijk lichaam"],
            ])),
            ("p", "Bij een <strong>kortsluiting</strong> schiet de stroomsterkte omhoog, omdat de "
                  "weerstand bijna nul is. Bij <strong>overbelasting</strong> trekken alle toestellen "
                  "samen te veel stroom; daarom slaat je zekering af als je de wasmachine en de oven samen "
                  "aanzet."),
            ("p", tabel(["Veiligheidsvoorziening", "Wat ze doet"], [
                ["Automatische zekering", "verbreekt de kring als de stroomsterkte te groot wordt"],
                ["Smeltveiligheid", "doet hetzelfde door een draadje te laten smelten"],
                ["Aarding met aarddraad", "voert stroom weg naar de grond als er spanning op een omhulsel komt"],
                ["Verliesstroomschakelaar", "slaat af als er stroom langs een onbedoelde weg wegloopt"],
                ["Dubbele isolatie", "een tweede isolatielaag, zodat het omhulsel nooit onder spanning komt"],
            ])),
            ("p", "Een <strong>verliesstroomschakelaar</strong> vergelijkt wat er in gaat met wat er "
                  "terugkomt, en slaat in milliseconden af als er stroom verdwijnt, bijvoorbeeld door een "
                  "mens. Een <strong>zekering</strong> kijkt naar de grootte van de stroom. Een "
                  "<strong>voltmeter</strong> meet alleen en beveiligt niets."),
            ("p", "Een <strong>dubbel geïsoleerd toestel</strong> heeft geen aarddraad nodig en draagt het "
                  "symbool van twee vierkanten in elkaar. Een <strong>aarddraad</strong> moet juist een "
                  "<strong>zo klein mogelijke weerstand</strong> hebben."),
            ("p", "Werk <strong>nooit met natte handen</strong> aan een elektrisch toestel: water "
                  "<strong>verlaagt de weerstand van je huid</strong>, dus loopt er bij dezelfde spanning "
                  "<strong>meer stroom</strong> door je lichaam. Een "
                  "<strong>hogere spanning</strong> is bij dezelfde weerstand gevaarlijker, want ze geeft "
                  "een grotere stroom. Daarom spreekt men van een "
                  "<strong>veiligheidsspanning</strong>: laag genoeg om dat gevaar klein te houden."),
            ("weetje", "Het is de stroom door je lichaam die schade doet, niet de spanning zelf. Een "
                       "statische schok van duizenden volt voelt onaangenaam maar is onschuldig, omdat er "
                       "bijna geen stroom bij hoort."),
        ]),
    ],
    onthoud=[
        "Stroomsterkte meet je in ampère, spanning in volt, weerstand in ohm.",
        "Wet van Ohm: weerstand = spanning gedeeld door stroomsterkte.",
        "Bij gelijke spanning geeft dubbele weerstand halve stroom.",
        "Een geleider heeft een kleine weerstand, een isolator een heel grote.",
        "De conventionele stroomzin loopt van plus naar min, de werkelijke van min naar plus.",
        "Joule-effect: een geleider warmt op doordat er stroom door loopt.",
        "Bij een kortsluiting is de weerstand bijna nul en schiet de stroomsterkte omhoog.",
        "Een verliesstroomschakelaar slaat af als er stroom langs een onbedoelde weg wegloopt.",
    ],
)

# ───────────────────────── 20. Veilig werken, meten en levensreddend handelen
BUNDELS["veilig-werken-meten-en-levensreddend-handelen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en levensreddend handelen",
    onder="De pictogrammen en de P- en H-zinnen, de meetinstrumenten, en eerste hulp bij hartstilstand, verdrinking en verslikking.",
    secties=[
        dict(kop="Veilig en duurzaam werken", blokken=[
            ("p", "Op een flesje met een chemische stof staan drie soorten informatie. Een "
                  "<strong>pictogram</strong> toont in één beeld wat het gevaar is: een "
                  "<strong>vlam</strong> betekent <strong>ontvlambaar</strong>, en voor een "
                  "<strong>sterk zuur</strong> verwacht je het pictogram voor "
                  "<strong>bijtende stoffen</strong>."),
            ("p", "De <strong>H-zinnen</strong> beschrijven het <strong>gevaar</strong> (H van hazard); "
                  "de <strong>P-zinnen</strong> zeggen welke <strong>voorzorgen</strong> je moet nemen "
                  "(P van precaution). Lees je H314, veroorzaakt ernstige brandwonden en oogletsel, dan "
                  "draag je <strong>handschoenen en een veiligheidsbril</strong>."),
            ("p", "Bij goed werken in het labo hoort: <strong>gemorste producten onmiddellijk "
                  "opkuisen</strong>, <strong>zuinig omgaan met chemische stoffen</strong>, "
                  "<strong>meetinstrumenten uitschakelen als je niet meet</strong> (dat spaart energie en "
                  "de batterij), <strong>hygiënisch werken met biologisch materiaal</strong> met "
                  "handschoenen, en <strong>voorzichtig met glaswerk</strong>. "
                  "<strong>Glasscherven</strong> ruim je op met een borstel en een blad, in de bak voor "
                  "<strong>scherp afval</strong>, nooit bij het gewone afval en nooit met je handen."),
            ("p", "Werk <strong>nooit met natte handen</strong> aan een elektrisch toestel, en lees de "
                  "<strong>handleiding en de onderhoudsvoorschriften</strong> van een toestel voor je het "
                  "gebruikt."),
        ]),
        dict(kop="Meten", blokken=[
            ("p", tabel(["Instrument", "Meet"], [
                ["Balans", "massa"],
                ["Chronometer", "tijd"],
                ["Thermometer", "temperatuur"],
                ["Dynamometer", "kracht"],
                ["pH-meter", "zuurtegraad"],
                ["Manometer", "druk"],
                ["Multimeter", "stroomsterkte, spanning en weerstand"],
                ["Calorimeter", "opgenomen of afgegeven warmte"],
            ])),
            ("p", "Het <strong>meetbereik</strong> van een instrument is de "
                  "<strong>kleinste en de grootste waarde</strong> die het kan meten. Meet je buiten dat "
                  "bereik, dan is het resultaat onbruikbaar of gaat het toestel stuk. Kies dus een "
                  "instrument met genoeg <strong>nauwkeurigheid</strong> voor je meting: voor "
                  "<strong>25 milliliter nauwkeurig afmeten</strong> neem je een "
                  "<strong>pipet</strong> of een maatkolf, niet een maatbeker, want die is om te mengen."),
            ("p", "Een <strong>meting is nooit helemaal exact</strong>, want elk instrument heeft een "
                  "beperkte nauwkeurigheid. Daarom schrijf je een resultaat in het juiste aantal "
                  "<strong>beduidende cijfers</strong>: meet je 1,2 meter, dan heb je er "
                  "<strong>twee</strong>, en 1,200 meter opschrijven suggereert een nauwkeurigheid die er "
                  "niet is. Meet je 325 gram op een balans die tot op een gram meet, dan schrijf je "
                  "precies <strong>325 gram</strong>."),
            ("p", "In de <strong>wetenschappelijke notatie</strong> schrijf je een getal als een "
                  "<strong>getal tussen 1 en 10 maal een macht van tien</strong>: 0,000045 meter wordt "
                  "4,5 maal tien tot de macht min vijf meter. En maak altijd eerst een "
                  "<strong>schatting</strong>: dan zie je een uitkomst van een verkeerde grootte meteen."),
            ("p", "Het voorvoegsel <strong>milli</strong> is een <strong>duizendste</strong>, "
                  "<strong>micro</strong> een miljoenste en <strong>nano</strong> een miljardste; "
                  "<strong>kilo</strong> is duizend en <strong>mega</strong> een miljoen. "
                  "<strong>2,5 kilometer is 2500 meter</strong>."),
        ]),
        dict(kop="Eerste hulp: de eerste stappen", blokken=[
            ("p", "Bij een slachtoffer dat <strong>niet reageert</strong> doe je altijd eerst hetzelfde: "
                  "<strong>roep om hulp</strong> en <strong>controleer of het normaal ademt</strong>. Eerst "
                  "kijken en roepen, dan pas handelen. Zo weet je of je moet reanimeren of in zijligging "
                  "moet leggen, en komt er al hulp onderweg."),
            ("p", "Het noodnummer in België en in heel Europa is <strong>112</strong>, en het is gratis. "
                  "Zet je telefoon op de luidspreker, zodat je handen vrij blijven."),
            ("p", "Reageert het slachtoffer <strong>niet</strong> maar ademt het <strong>wel "
                  "normaal</strong>, dan leg je het in <strong>stabiele zijligging</strong>: zo blijft de "
                  "<strong>luchtweg vrij</strong> en kan vocht uit de mond lopen. <strong>Op de rug</strong> "
                  "kan de <strong>tong of braaksel de luchtweg afsluiten</strong>, en daarom is de rug de "
                  "verkeerde houding."),
        ]),
        dict(kop="Hartstilstand", blokken=[
            ("p", "Bij een <strong>hartstilstand pompt het hart geen bloed meer rond</strong>. Je herkent "
                  "hem doordat het slachtoffer <strong>niet reageert</strong> en "
                  "<strong>niet of niet normaal ademt</strong>; een paar happende bewegingen zijn geen "
                  "normale ademhaling. Pijn in de arm kan een waarschuwing vooraf zijn, maar is zelf geen "
                  "hartstilstand."),
            ("p", "Zonder bloedcirculatie krijgen de hersenen geen zuurstof. Je moet dus "
                  "<strong>binnen enkele minuten met een reanimatie beginnen</strong>: eerst "
                  "<strong>hulp bellen</strong>, dan onmiddellijk <strong>hartmassage</strong>."),
            ("p", "Bij een <strong>hartmassage</strong> duw je <strong>midden op de borstkas</strong>, op "
                  "het onderste deel van het <strong>borstbeen</strong>, met de hiel van je hand en recht "
                  "naar beneden. Je duwt <strong>vijf tot zes centimeter</strong> diep en laat de borstkas "
                  "tussen twee duwbewegingen <strong>volledig terugkomen</strong>. Het tempo is ongeveer "
                  "<strong>honderd tot honderdtwintig</strong> duwbewegingen per minuut."),
            ("p", "Bij een <strong>reanimatie</strong> wissel je "
                  "<strong>dertig hartmassages af met twee beademingen</strong>. Kan je niet "
                  "beademen, dan blijf je toch doorduwen. Je gaat door tot de "
                  "<strong>hulpdiensten overnemen</strong> of het slachtoffer weer normaal ademt. Je mag "
                  "een <strong>reanimatie dus niet stoppen zodra je moe wordt</strong>: dan wissel je af "
                  "met iemand anders."),
        ]),
        dict(kop="Verdrinking en verslikking", blokken=[
            ("p", "Bij een <strong>verdrinking</strong> is het <strong>zuurstoftekort</strong> het "
                  "grootste gevaar: water in de luchtweg belet de opname van zuurstof. Zorg "
                  "<strong>eerst voor je eigen veiligheid</strong>, haal het slachtoffer "
                  "<strong>uit het water als dat veilig kan</strong>, en begin bij een slachtoffer dat niet "
                  "ademt met <strong>beademen</strong>. Reik liever iets aan of roep hulp dan dat je "
                  "zomaar het water in springt: een hulpverlener die zelf verdrinkt helpt niemand."),
            ("p", "Bij een <strong>verslikking</strong> zit er iets in de luchtweg. Kan de persoon nog "
                  "<strong>krachtig hoesten</strong>, dan <strong>moedig je het hoesten aan</strong> en "
                  "blijf je erbij: hoesten is de krachtigste manier om een voorwerp los te krijgen."),
            ("p", "Een <strong>ernstige verslikking</strong> herken je doordat de persoon "
                  "<strong>niet meer kan hoesten, spreken of goed ademen</strong>. Dan begin je "
                  "onmiddellijk met <strong>vijf rugslagen</strong>: slagen met de hiel van je hand "
                  "<strong>tussen de schouderbladen</strong>, terwijl de persoon voorover buigt zodat het "
                  "voorwerp naar buiten kan."),
            ("p", "Helpt dat niet, dan geef je <strong>vijf buikstoten</strong>: je staat achter de "
                  "persoon en trekt je vuist schuin naar boven, onder het borstbeen. Je blijft "
                  "<strong>rugslagen en buikstoten afwisselen</strong> tot het voorwerp loskomt. Verliest "
                  "de persoon het bewustzijn, dan begin je te <strong>reanimeren</strong>. Laat intussen "
                  "<strong>112</strong> bellen."),
            ("weetje", "Een leeftijd maakt verschil: bij een baby geef je geen buikstoten maar "
                       "borstcompressies, en de rugslagen zijn veel zachter. Een cursus eerste hulp laat je "
                       "dat op een pop oefenen, en dat is iets anders dan het lezen."),
        ]),
    ],
    onthoud=[
        "H-zinnen beschrijven het gevaar, P-zinnen de voorzorgen.",
        "Glasscherven gaan in de bak voor scherp afval, nooit met je handen.",
        "Het meetbereik is de kleinste en de grootste waarde die een instrument kan meten.",
        "Milli is een duizendste, micro een miljoenste, nano een miljardste; kilo is duizend.",
        "Reageert iemand niet: roep om hulp en controleer of het normaal ademt.",
        "Het noodnummer in België en in heel Europa is 112.",
        "Reageert het slachtoffer niet maar ademt het wel normaal: stabiele zijligging.",
        "Reanimatie: dertig hartmassages, vijf tot zes centimeter diep, afwisselen met twee beademingen.",
        "Ernstige verslikking: vijf rugslagen, dan vijf buikstoten, en blijven afwisselen.",
    ],
)

# ───────────────────────── 21. Grootheden, eenheden en wetenschappelijk onderzoek
BUNDELS["grootheden-eenheden-en-wetenschappelijk-onderzoek-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Grootheden, eenheden en wetenschappelijk onderzoek",
    onder="Grootheden en eenheden, de verbanden tussen grootheden, en de stappen van een onderzoek of een ontwerp.",
    secties=[
        dict(kop="Grootheden en eenheden", blokken=[
            ("p", "Een <strong>grootheid</strong> is <strong>wat je meet</strong>, een "
                  "<strong>eenheid</strong> is <strong>waarin je het uitdrukt</strong>: lengte is de "
                  "grootheid, de meter de eenheid. Een <strong>meetresultaat zonder eenheid zegt "
                  "niets</strong>: vijf kan vijf meter of vijf kilometer zijn."),
            ("p", tabel(["Grootheid", "SI-eenheid", "Grootheid", "Eenheid"], [
                ["lengte", "meter", "kracht", "newton"],
                ["massa", "kilogram", "energie", "joule"],
                ["tijd", "seconde", "vermogen", "watt"],
                ["temperatuur", "kelvin", "druk", "pascal"],
            ])),
            ("p", "De <strong>kilometer per uur</strong> is een afgeleide eenheid die veel gebruikt wordt, "
                  "maar in het SI-stelsel reken je snelheid in <strong>meter per seconde</strong>. En let "
                  "op: <strong>druk meet je in pascal</strong>, niet in newton; de newton alleen is de "
                  "eenheid van kracht."),
            ("p", "De voorvoegsels gaan van <strong>mega</strong> (een miljoen) en "
                  "<strong>kilo</strong> (duizend) over <strong>centi</strong> (een honderdste) en "
                  "<strong>milli</strong> (een duizendste) naar <strong>micro</strong> (een miljoenste) en "
                  "<strong>nano</strong> (een miljardste). Dus: <strong>0,25 kilogram is 250 gram</strong>, "
                  "<strong>45 centimeter is 0,45 meter</strong>, en <strong>2 microseconden is 2 maal tien "
                  "tot de macht min zes seconden</strong>."),
        ]),
        dict(kop="Nauwkeurig meten", blokken=[
            ("p", "De <strong>beduidende cijfers</strong> van een meetresultaat zijn de cijfers die je "
                  "echt gemeten hebt. Lees je met een <strong>meetlint 1,2 meter</strong> af, dan heeft "
                  "dat resultaat <strong>twee</strong> beduidende cijfers. Meet je met een "
                  "<strong>balans die tot op een gram nauwkeurig is</strong>, dan schrijf je "
                  "<strong>325 gram</strong> op, <strong>met drie beduidende cijfers</strong>: "
                  "<strong>325,00 gram ziet er nauwkeuriger uit dan je gemeten hebt</strong>, en "
                  "afronden tot 300 gram gooit informatie weg die je wel had."),
            ("p", "Een meting is nooit perfect. <strong>Toevallige meetfouten</strong> springen de ene "
                  "keer naar boven en de andere keer naar beneden. Daarom "
                  "<strong>herhaal je een meting een paar keer: om de invloed van toevallige meetfouten "
                  "kleiner te maken</strong>. Een <strong>systematische fout</strong> doet dat niet: die "
                  "schuift elke meting dezelfde kant op, bijvoorbeeld een weegschaal die niet op nul "
                  "stond, en die haal je er met herhalen niet uit."),
            ("p", "<strong>Maak eerst een schatting</strong> van je antwoord: <strong>zo merk je meteen "
                  "of je uitkomst een onzinnige grootte heeft</strong>. De echte berekening maak je "
                  "daarna nog altijd."),
        ]),
        dict(kop="Verbanden tussen grootheden", blokken=[
            ("p", tabel(["Verband", "Wat er geldt", "Grafiek"], [
                ["Recht evenredig", "de verhouding blijft gelijk", "een rechte door de oorsprong"],
                ["Lineair", "gelijkmatige toename, maar met een constante erbij", "een rechte, niet door de oorsprong"],
                ["Omgekeerd evenredig", "het product blijft gelijk", "een kromme die naar de assen buigt"],
                ["Kwadratisch", "twee keer meer geeft vier keer meer", "een parabool"],
            ])),
            ("p", "<strong>Recht evenredig is het bijzondere geval</strong> van lineair waarbij de rechte "
                  "<strong>door nul</strong> gaat. De lengte van een veer in functie van de kracht is "
                  "<strong>lineair maar niet recht evenredig</strong>: bij nul kracht heeft ze al een "
                  "lengte. Bij een <strong>kwadratisch</strong> verband, zoals de kinetische energie en de "
                  "snelheid, geeft verdubbelen <strong>vier keer</strong> zo veel."),
            ("p", "Je zet meetresultaten eerst in een <strong>tabel</strong>, met de eenheid in de "
                  "hoofding: zo zie je de paren bij elkaar. Pas daarna maak je de "
                  "<strong>grafiek</strong>, en daarin zie je het verband. Een "
                  "<strong>tabel geeft precieze waarden, een grafiek toont het verband</strong>, en uit "
                  "beide kan je gegevens halen."),
            ("p", "Je mag een <strong>formule omvormen</strong> zodat een andere grootheid alleen staat; "
                  "je doet dan aan beide kanten hetzelfde. Uit de wet van Ohm haal je zo zowel de spanning "
                  "als de stroomsterkte of de weerstand. Zie je in een grafiek dat de stroomsterkte "
                  "<strong>recht evenredig</strong> met de spanning stijgt, dan is de "
                  "<strong>weerstand constant</strong> gebleven, want de verhouding tussen de twee is "
                  "precies de weerstand."),
        ]),
        dict(kop="De wetenschappelijke methode", blokken=[
            ("p", "De stappen in orde: de <strong>probleemstelling afbakenen</strong>, een "
                  "<strong>onderzoeksvraag</strong> opstellen en een <strong>hypothese</strong> "
                  "formuleren, een <strong>onderzoeksplan</strong> maken, "
                  "<strong>data verzamelen</strong>, die <strong>analyseren</strong>, een "
                  "<strong>conclusie formuleren</strong> en tot slot "
                  "<strong>reflecteren en communiceren</strong>."),
            ("p", "De <strong>onderzoeksvraag</strong> is de vraag die je met je onderzoek wil "
                  "beantwoorden; ze moet nauwkeurig genoeg zijn om er echt op te kunnen antwoorden. De "
                  "<strong>hypothese</strong> is je <strong>onderbouwde verwachting</strong>. Blijkt ze "
                  "<strong>verkeerd</strong>, dan is het onderzoek <strong>niet mislukt</strong>: je weet "
                  "daarna meer dan ervoor."),
            ("p", "In het <strong>onderzoeksplan</strong> staat welke metingen je doet, met welk "
                  "materiaal en in welke orde. Daarom <strong>schrijf je je werkwijze op</strong>: zo kan "
                  "iemand anders je onderzoek <strong>herhalen</strong> en je resultaat nakijken, en "
                  "herhaalbaarheid is een kern van wetenschap."),
            ("p", "<strong>Verander maar één ding tegelijk</strong> en houd alle andere omstandigheden "
                  "gelijk; anders weet je achteraf niet welke verandering het gevolg veroorzaakte. Wil je "
                  "nagaan of plantjes sneller groeien met meer licht, dan neem je "
                  "<strong>dezelfde plantjes, dezelfde pot en grond</strong>, en laat je "
                  "<strong>alleen de lichtduur</strong> verschillen."),
            ("p", "<strong>Herhaal een meting</strong> een paar keer: het gemiddelde ligt dichter bij de "
                  "echte waarde, en een grote spreiding verraadt dat er iets niet klopt. Een "
                  "<strong>conclusie</strong> moet een <strong>antwoord geven op de onderzoeksvraag</strong> "
                  "en <strong>steunen op je gegevens</strong>. De gegevens beslissen, niet je verwachting; "
                  "<strong>gegevens aanpassen tot ze bij je hypothese passen</strong> is geen onderzoek "
                  "maar bedrog."),
            ("p", "In de <strong>reflectie</strong> zeg je wat goed liep, wat je anders zou doen en hoe "
                  "betrouwbaar je resultaat is. Daarna communiceer je je besluit."),
        ]),
        dict(kop="Een oplossing ontwerpen", blokken=[
            ("p", "Bij een ontwerp begin je met het <strong>probleem zo scherp mogelijk te "
                  "definiëren</strong>. Daarna geef je de <strong>criteria</strong> waaraan je oplossing "
                  "moet voldoen; zonder criteria kan je achteraf niet beoordelen of ze goed is."),
            ("p", "Is het probleem groot, dan <strong>splits je het op in deelproblemen</strong>: elk deel "
                  "is afzonderlijk makkelijker op te lossen, en samen vormen ze het geheel. Je "
                  "<strong>integreert</strong> de deeloplossingen in één totaaloplossing."),
            ("p", "Tot slot <strong>evalueer je je oplossing en stuur je ze bij</strong> waar nodig. Bijna "
                  "geen enkel ontwerp is in één keer goed."),
            ("p", "<strong>STEM</strong> staat voor <strong>wetenschappen, technologie, engineering en "
                  "wiskunde</strong> (de M van mathematics). Die vier werken samen aan "
                  "<strong>maatschappelijke uitdagingen</strong>, en die uitdagingen zijn precies de reden "
                  "waarom er nieuwe technieken en materialen ontwikkeld worden."),
            ("p", "Bij de ontwikkeling van een <strong>vaccin</strong> zag je dat samenspel: "
                  "<strong>wetenschappelijke kennis</strong> om het vaccin te ontwikkelen, "
                  "<strong>technologische kennis</strong> om het koel te bewaren en te vervoeren, en "
                  "<strong>wiskundige kennis</strong> om de verspreiding van het virus in kaart te brengen."),
            ("weetje", "Een gat in je gegevens is zelf een resultaat. Noteer ook wat je níét gevonden "
                       "hebt: zo weet de lezer wat je besluit wel en niet kan dekken."),
        ]),
    ],
    onthoud=[
        "Een grootheid is wat je meet, een eenheid is waarin je het uitdrukt.",
        "Druk meet je in pascal, niet in newton; de newton is de eenheid van kracht.",
        "Beduidende cijfers zijn de cijfers die je echt gemeten hebt.",
        "Herhalen verkleint de invloed van toevallige meetfouten; een systematische fout haal je er niet uit.",
        "Recht evenredig: een rechte door de oorsprong. Omgekeerd evenredig: het product blijft gelijk.",
        "Kwadratisch: twee keer meer geeft vier keer meer.",
        "Een hypothese is een onderbouwde verwachting; blijkt ze verkeerd, dan is het onderzoek niet mislukt.",
        "Verander maar één ding tegelijk en houd alle andere omstandigheden gelijk.",
        "Bij een ontwerp definieer je het probleem, stel je criteria op, en evalueer en stuur je bij.",
    ],
)

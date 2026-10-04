# -*- coding: utf-8 -*-
"""De leerbundels voor biologie op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche biologie van de 2de graad doorstroomfinaliteit,
geldig vanaf 1 januari 2027. Die fiche geldt enkel voor de studierichting
natuurwetenschappen: die legt haar wetenschappen af in drie aparte examens,
biologie, chemie en fysica, in plaats van één examen natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De twaalf thema's volgen de weging van het examen: vier over het waarnemen en
verwerken van prikkels (30 %), twee over de materie- en energiestromen (15 %),
en één voor elk van de andere koppen.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/biologie.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-biologie-boost-doorstroom". Veel van deze
leerstof staat ook in de bundels van natuurwetenschappen, op drie niveaus, en
daar klinken sommige thematitels bijna gelijk.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Biologie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Homeostase en waterhuishouding bij planten
BUNDELS["homeostase-en-waterhuishouding-bij-planten-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Homeostase en waterhuishouding bij planten",
    onder="Homeostase, de drie stappen van de waterhuishouding, de bouw van de plant, de fotosynthese en de prikkels bij planten.",
    secties=[
        dict(kop="Homeostase en het feedbacksysteem", blokken=[
            ("p", "<strong>Homeostase</strong> bij een plant betekent dat ze haar "
                  "<strong>inwendig milieu binnen nauwe grenzen houdt terwijl de omgeving "
                  "verandert</strong>. Dat is geen stilstand: er wordt voortdurend bijgestuurd."),
            ("p", "Dat bijsturen gebeurt met een <strong>feedbacksysteem</strong>: de plant "
                  "<strong>gebruikt het gevolg van een proces om dat proces zelf bij te sturen</strong>. "
                  "Verliest een blad te veel water, dan sluiten de huidmondjes en daalt het verlies weer."),
            ("p", "De <strong>omgevingsfactoren</strong> die de waterhuishouding beïnvloeden, zijn de "
                  "<strong>lichtsterkte</strong> die op de bladeren valt, de "
                  "<strong>temperatuur van de lucht</strong> rondom de plant en de "
                  "<strong>vochtigheidsgraad van de bodem en van de lucht</strong>. De kleur van de "
                  "bloemblaadjes speelt daarin geen rol."),
            ("p", "Die factoren zijn <strong>abiotisch</strong>, dat wil zeggen niet-levend. "
                  "Vocht, licht en temperatuur zijn abiotisch; andere planten en dieren zijn "
                  "<strong>biotisch</strong>."),
        ]),
        dict(kop="De drie stappen van de waterhuishouding", blokken=[
            ("p", "De waterhuishouding bestaat uit <strong>wateropname</strong>, "
                  "<strong>watertransport</strong> en <strong>transpiratie</strong>. De plant neemt water "
                  "op in de wortel, vervoert het naar boven en laat het als damp ontsnappen."),
            ("p", "De <strong>turgor</strong> is de <strong>druk van het vocht in de vacuole</strong>, "
                  "waardoor een plantencel stevig blijft staan. Bij een rijpe plantencel neemt de "
                  "<strong>centrale vacuole</strong> het grootste deel van het volume in; daarin zit het "
                  "vocht dat voor de turgor zorgt."),
            ("p", "Een <strong>kamerplant die te lang geen water kreeg, hangt slap</strong>: de "
                  "<strong>vacuolen zijn leeggelopen, waardoor de turgor wegvalt</strong>. Geef je water, "
                  "dan komt de turgor terug."),
            ("p", "<strong>Transpiratie</strong> is het <strong>verlies van water in de vorm van "
                  "waterdamp</strong>. Het vloeibare water in het blad wordt damp en ontsnapt door de "
                  "huidmondjes naar buiten."),
        ]),
        dict(kop="Huidmondjes, worteldruk en zuigkracht", blokken=[
            ("p", "Een <strong>huidmondje</strong> bestaat uit twee <strong>sluitcellen</strong>. Vullen "
                  "ze zich met water, dan bollen ze op en gaat de opening ertussen open. De meeste "
                  "huidmondjes liggen <strong>aan de onderkant van het blad</strong>, waar het koeler en "
                  "schaduwrijker is."),
            ("p", "Bij <strong>droogte sluit</strong> de plant haar huidmondjes, want zo verliest ze "
                  "minder water. Dan komt er echter ook nauwelijks koolstofdioxide binnen, en "
                  "<strong>valt de fotosynthese grotendeels stil</strong>. Een plant die haar huidmondjes "
                  "sluit, kan dus niet even goed verder fotosynthetiseren."),
            ("p", "Drie krachten brengen het water omhoog. De <strong>worteldruk</strong> is de druk "
                  "waarmee de wortel water de houtvaten in duwt. De "
                  "<strong>transpiratiezuiging</strong> is de zuigkracht die in het blad ontstaat doordat "
                  "daar water verdampt. En de <strong>capillariteit</strong> is het opstijgen van water in "
                  "heel nauwe buisjes. De <strong>zwaartekracht</strong> werkt juist tegen."),
            ("p", "Hoe <strong>warmer en droger de lucht</strong> rond een blad, hoe sterker de "
                  "transpiratie. Transpiratie is niet enkel verlies: ze "
                  "<strong>trekt water en mineralen mee omhoog en koelt het blad af</strong>."),
        ]),
        dict(kop="De bouw van de plant", blokken=[
            ("p", "Bij een bloeiende plant onderscheidt men vier <strong>organen</strong>: "
                  "<strong>wortel</strong>, <strong>stengel</strong>, <strong>blad</strong> en "
                  "<strong>bloem</strong>."),
            ("p", "Het <strong>huidweefsel</strong> bedekt de plant: de <strong>epidermis</strong>, de "
                  "<strong>cuticula</strong> of het waslaagje erbovenop, en de <strong>bast</strong>. De "
                  "cuticula is waterafstotend en beschermt tegen uitdroging; daarom glanst een blad vaak."),
            ("p", "Het <strong>xyleem</strong> of de <strong>houtvaten</strong> vervoeren "
                  "<strong>water en opgeloste mineralen vanuit de wortel</strong> naar boven. Het "
                  "<strong>floëem</strong> of de <strong>zeefvaten</strong> vervoeren de "
                  "<strong>suikers</strong> uit het blad. Dat gaat <strong>niet altijd naar "
                  "beneden</strong>: in het voorjaar gaat het net omhoog, van een wortelknol naar de "
                  "ontluikende knoppen."),
            ("p", "Xyleem en floëem liggen samen in één streng, de <strong>vaatbundel</strong>; in een "
                  "blad zie je die als een nerf. Het <strong>vulweefsel</strong> "
                  "<strong>vult de ruimte tussen de andere weefsels en slaat stoffen op</strong>."),
        ]),
        dict(kop="Fotosynthese", blokken=[
            ("p", "De reactievergelijking van de <strong>fotosynthese</strong>: "
                  "<strong>6 CO₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 O₂</strong>. Koolstofdioxide en water worden "
                  "met lichtenergie omgezet in glucose, en daarbij komt zuurstofgas vrij. Omgekeerd "
                  "gelezen is dat net de celademhaling."),
            ("p", "Dat gebeurt in de <strong>chloroplast</strong> of bladgroenkorrel, die het "
                  "<strong>chlorofyl</strong> bevat dat het licht opvangt. De glucose die ontstaat, heet "
                  "een <strong>assimilaat</strong>: een stof die de plant zelf opbouwt uit anorganische "
                  "grondstoffen."),
            ("p", "Een goede waterhuishouding is nodig voor de fotosynthese: <strong>water is zelf een "
                  "grondstof</strong>, <strong>open huidmondjes laten de koolstofdioxide binnen</strong>, "
                  "en <strong>het watertransport brengt mineralen naar het blad</strong>. De groene kleur "
                  "komt van het chlorofyl, niet van het water."),
        ]),
        dict(kop="Prikkels en hormonen bij planten", blokken=[
            ("p", "Een <strong>fotoreceptor</strong> is een <strong>structuur die licht opvangt en zo een "
                  "prikkel doorgeeft</strong>. Een plant heeft <strong>geen zenuwen en geen "
                  "hersenen</strong>: haar coördinatie verloopt met hormonen die traag door de plant "
                  "verspreid worden."),
            ("p", "Bij een <strong>tropie hangt de richting van de beweging af van de richting van de "
                  "prikkel</strong>: de plant groeit naar de prikkel toe of ervan weg. Bij een "
                  "<strong>nastie</strong> is de beweging altijd dezelfde, waar de prikkel ook vandaan "
                  "komt. Dat een wortel naar beneden groeit en een stengel naar boven, is "
                  "<strong>geotropie</strong>, en dus een tropie."),
            ("p", "<strong>Auxine</strong> zorgt voor <strong>celstrekking</strong>: het hoopt zich op aan "
                  "de schaduwzijde en laat de cellen daar sterker uitrekken, zodat de stengel naar het "
                  "licht buigt. <strong>Ethyleen</strong> is een gasvormig hormoon dat het "
                  "<strong>rijpen van vruchten</strong> versnelt. <strong>Abscisinezuur</strong> is het "
                  "stresshormoon: het <strong>laat de huidmondjes sluiten zodat de plant water "
                  "spaart</strong>."),
            ("p", "Plantenhormonen werken <strong>niet enkel in de bloem</strong>, maar overal: bij de "
                  "wortelgroei, de vorming van zijscheuten, het bladverlies, de celstrekking en de "
                  "waterhuishouding."),
        ]),
    ],
    onthoud=[
        "Homeostase is het inwendig milieu binnen nauwe grenzen houden; een feedbacksysteem gebruikt het gevolg van een proces om dat proces bij te sturen.",
        "De waterhuishouding heeft drie stappen: wateropname, watertransport en transpiratie.",
        "Turgor is de druk van het vocht in de vacuole; valt die weg, dan hangt de plant slap.",
        "Twee sluitcellen vormen een huidmondje; bij droogte gaat het dicht en valt de fotosynthese grotendeels stil.",
        "Worteldruk duwt, transpiratiezuiging trekt en capillariteit helpt; de zwaartekracht werkt tegen.",
        "Xyleem vervoert water en mineralen omhoog, floëem de suikers in twee richtingen.",
        "Fotosynthese: 6 CO₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 O₂, in de chloroplast.",
        "Bij een tropie bepaalt de richting van de prikkel de richting van de groei, bij een nastie niet.",
        "Auxine strekt cellen, ethyleen doet vruchten rijpen, abscisinezuur sluit de huidmondjes.",
    ],
)

# ───────────────────────── 2. Van prikkel tot reactie en het zenuwstelsel
BUNDELS["van-prikkel-tot-reactie-en-het-zenuwstelsel-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Van prikkel tot reactie en het zenuwstelsel",
    onder="De weg van prikkel naar reactie, de reflexen, het centrale en perifere zenuwstelsel, en het neuron tot in zijn onderdelen.",
    secties=[
        dict(kop="Van prikkel tot reactie", blokken=[
            ("p", "Een <strong>prikkel</strong> is een <strong>verandering in of rond het lichaam die een "
                  "reactie kan uitlokken</strong>. Licht, geluid en warmte zijn prikkels; de reactie komt "
                  "daarna."),
            ("p", "De weg loopt zo: <strong>receptor, sensorische zenuw, verwerking, motorische zenuw, "
                  "effector</strong>. Een <strong>receptor</strong> is een cel of structuur die een prikkel "
                  "opvangt; een <strong>sensorische zenuw</strong> voert prikkels "
                  "<strong>naar het centrale zenuwstelsel toe</strong>; een <strong>effector</strong> is "
                  "het orgaan of de cel die <strong>de reactie uitvoert</strong>."),
            ("p", "Bij ons zijn de effectoren vooral de <strong>spieren en de klieren</strong>: een "
                  "skeletspier in de arm, een zweetklier in de huid, de hartspier. Een tastreceptor in de "
                  "vingertop is géén effector maar staat aan het begin van de weg."),
            ("p", "Een receptor heeft een <strong>drempelwaarde</strong>: een "
                  "<strong>te zwakke prikkel levert geen signaal op</strong>, zodat het lichaam niet op elk "
                  "detail reageert. Pas boven die drempel ontstaat er een "
                  "<strong>zenuwimpuls</strong>, een elektrisch signaal dat langs de celmembraan loopt. Die "
                  "impuls heeft altijd dezelfde sterkte; de <strong>frequentie</strong> zegt hoe sterk de "
                  "prikkel was."),
            ("p", "In de huid staan <strong>tastreceptoren</strong>, "
                  "<strong>temperatuurreceptoren</strong> en <strong>pijnreceptoren</strong>; de "
                  "lichtreceptoren zitten in het netvlies. Er zijn ook "
                  "<strong>inwendige receptoren</strong>, bijvoorbeeld voor de bloeddruk, het "
                  "zuurstofgehalte of de rek van de maagwand."),
            ("p", "Dezelfde prikkel kan bij <strong>twee mensen tot een verschillende reactie</strong> "
                  "leiden, want de verwerking hangt af van ervaring, aandacht en gemoedstoestand."),
        ]),
        dict(kop="Reflexen", blokken=[
            ("p", "Een <strong>reflex verloopt snel en zonder dat je het eerst beslist</strong>. De "
                  "boodschap schakelt al in het <strong>ruggemerg of de hersenstam</strong> over, langs de "
                  "korte weg die de <strong>reflexboog</strong> heet."),
            ("p", "Raak je een <strong>hete pan</strong> aan, dan <strong>stuurt het ruggemerg de spier al "
                  "aan terwijl de boodschap nog naar de hersenen onderweg is</strong>. Dat is de "
                  "<strong>terugtrekreflex</strong>: je hand is weg voor je de pijn voelt."),
            ("p", "Andere reflexen die je moet kennen: de <strong>kniepeesreflex</strong>, die een arts met een "
                  "tikje onder de knieschijf test; de <strong>pupilreflex</strong>, waarbij je "
                  "<strong>pupillen kleiner worden als er plots veel licht op valt</strong>; en de "
                  "<strong>toeschietreflex</strong>, waarbij <strong>de melk begint te vloeien zodra een "
                  "baby aan de borst zuigt</strong>."),
            ("p", "Een reflex is <strong>niet altijd te onderdrukken</strong>. De pupilreflex blijft "
                  "buiten je wil; die kan je niet afleren, ook niet met oefening."),
            ("p", "Het verschil met een <strong>bewuste reactie</strong>: een reflex is "
                  "<strong>sneller</strong>, bij een bewuste reactie komen de <strong>grote hersenen</strong> "
                  "tussen, en een reflex <strong>schakelt over in het ruggemerg of de hersenstam</strong>. "
                  "Beide gebruiken wél zenuwcellen."),
            ("p", "Een hond die bij het <strong>rinkelen van zijn voerbak</strong> begint te kwijlen, toont "
                  "een <strong>geleerde reactie op een prikkel die eerst niets betekende</strong>. De "
                  "reactie verloopt automatisch, maar de koppeling is geleerd."),
        ]),
        dict(kop="Het centrale en het perifere zenuwstelsel", blokken=[
            ("p", "Het <strong>centrale zenuwstelsel</strong> bestaat uit de <strong>hersenen en het "
                  "ruggemerg</strong>: alles wat in de schedel en de wervelkolom beschut ligt. Het "
                  "<strong>perifere zenuwstelsel</strong> zijn alle zenuwen en zenuwknopen "
                  "<strong>buiten de hersenen en het ruggemerg</strong>."),
            ("p", "Bij de hersenen onderscheidt men de <strong>grote hersenen</strong>, de "
                  "<strong>kleine hersenen</strong> en de <strong>hersenstam</strong>. Het ruggemerg hoort "
                  "daar niet bij; dat ligt in de wervelkolom."),
            ("p", "De <strong>kleine hersenen</strong> zorgen voor het <strong>afstemmen van bewegingen en "
                  "het bewaren van het evenwicht</strong>. De <strong>hersenstam</strong> regelt de "
                  "<strong>ademhaling, de hartslag en de bloeddruk</strong>, ook als je slaapt. In de "
                  "<strong>grote hersenen</strong> gebeurt het <strong>bewuste denken, het plannen en het "
                  "leren</strong>."),
            ("p", "Het <strong>ruggemerg geleidt signalen tussen de hersenen en het lichaam</strong>, "
                  "<strong>schakelt reflexen over zonder omweg langs de hersenen</strong> en "
                  "<strong>ligt beschut in de wervelkolom</strong>. Een <strong>dwarse breuk</strong> laat "
                  "het gevoel en de beweging onder die hoogte <strong>wegvallen</strong>, want alle banen "
                  "lopen daar door."),
        ]),
        dict(kop="Het neuron", blokken=[
            ("p", "Een <strong>neuron</strong> heeft een <strong>cellichaam met de kern</strong>, "
                  "<strong>dendrieten</strong> en een <strong>axon met zijn eindknopjes</strong>. De "
                  "<strong>dendrieten</strong> zijn de <strong>korte uitlopers die signalen "
                  "opvangen</strong>. Een neuron heeft <strong>veel dendrieten en één axon</strong>, niet "
                  "omgekeerd; dat axon kan aan het einde in vele eindknopjes uitlopen."),
            ("p", "De <strong>myelineschede</strong> <strong>isoleert het axon zodat de impuls er sneller "
                  "langs gaat</strong>. De onderbrekingen erin heten de "
                  "<strong>knopen van Ranvier</strong>; bij elke knoop springt de impuls naar de volgende. "
                  "Door die sprongen gaat hij tientallen keren sneller dan langs een kaal axon. In het "
                  "perifere zenuwstelsel maakt de <strong>cel van Schwann</strong> die schede."),
            ("p", "Een ziekte die de myelineschede aantast, laat de "
                  "<strong>signalen trager doorgaan, waardoor bewegen en voelen moeilijker wordt</strong>."),
            ("p", "In een <strong>synaps</strong> <strong>geeft het eindknopje een stof af die aan een "
                  "receptor op de volgende cel bindt</strong>. Die structuur heet een "
                  "<strong>membraanreceptor</strong> en werkt als een slot waarop maar één sleutel past. "
                  "Het signaal gaat daardoor <strong>altijd in één richting</strong>, van het eindknopje "
                  "naar de volgende cel."),
            ("p", "Het <strong>zenuwstelsel werkt sneller dan het hormonale stelsel</strong>, maar het "
                  "<strong>effect van een hormoon houdt langer aan</strong>. Een impuls doet er "
                  "milliseconden over; een hormoon reist met het bloed en werkt minuten tot dagen door."),
        ]),
    ],
    onthoud=[
        "De weg van prikkel naar reactie: receptor, sensorische zenuw, verwerking, motorische zenuw, effector.",
        "Effectoren zijn spieren en klieren; een receptor staat aan het begin, niet aan het einde.",
        "Een receptor heeft een drempelwaarde; boven die drempel ontstaat een zenuwimpuls, en de frequentie zegt hoe sterk de prikkel was.",
        "Een reflex schakelt over in het ruggemerg of de hersenstam en verloopt dus sneller dan een bewuste reactie.",
        "Vier reflexen: terugtrekreflex, kniepeesreflex, pupilreflex en toeschietreflex.",
        "Centraal zenuwstelsel is hersenen plus ruggemerg; al de rest is perifeer.",
        "Kleine hersenen voor beweging en evenwicht, hersenstam voor ademhaling en hartslag, grote hersenen voor denken en leren.",
        "Een neuron heeft veel dendrieten en één axon; de myelineschede met de knopen van Ranvier laat de impuls springen.",
        "In een synaps gaat het signaal in één richting, van eindknopje naar membraanreceptor.",
        "Het zenuwstelsel werkt sneller, een hormoon werkt langer door.",
    ],
)

# ───────────────────────── 3. Het oog
BUNDELS["het-oog-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het oog",
    onder="De bouw van het oog, de weg van het licht, het netvlies, de accommodatie en de afwijkingen.",
    secties=[
        dict(kop="De weg van het licht", blokken=[
            ("p", "Het licht gaat door het oog in deze orde: <strong>hoornvlies, pupil, lens, glasachtig "
                  "lichaam, netvlies</strong>. Het <strong>hoornvlies</strong> is het doorzichtige voorste "
                  "stukje van de buitenste laag en buigt het licht al een eerste keer af."),
            ("p", "De <strong>pupil</strong> is de <strong>opening in het midden van de iris</strong>. Hij "
                  "ziet zwart omdat het licht dat erin valt niet meer terugkomt. De "
                  "<strong>iris</strong> of het regenboogvlies <strong>regelt de hoeveelheid licht</strong> "
                  "die binnenkomt; het is een ringvormig spiertje. De <strong>kleur van iemands ogen</strong> "
                  "is de kleur van de iris."),
            ("p", "De <strong>delen die het licht afbuigen</strong> zodat het op het netvlies samenkomt, "
                  "zijn het <strong>hoornvlies</strong>, het <strong>kamervocht</strong> en de "
                  "<strong>lens</strong>. De iris buigt niet; die laat licht enkel door of houdt het tegen."),
            ("p", "Het <strong>beeld dat op het netvlies valt, staat op zijn kop</strong>, zowel "
                  "boven-onder als links-rechts. De hersenen zetten het weer recht."),
        ]),
        dict(kop="De drie lagen en de vullingen", blokken=[
            ("p", "De wand van de oogbol heeft drie lagen, van buiten naar binnen: het "
                  "<strong>harde oogvlies</strong>, het <strong>vaatvlies</strong> en het "
                  "<strong>netvlies</strong>. Het glasachtig lichaam is geen laag maar de vulling."),
            ("p", "Het <strong>harde oogvlies</strong> of de <strong>sclera</strong> "
                  "<strong>geeft de oogbol zijn vorm en beschermt hem</strong>; het is het wit dat je naast "
                  "de iris ziet. Het <strong>vaatvlies</strong> "
                  "<strong>voorziet het netvlies van bloed en neemt strooilicht weg</strong>, want het ligt "
                  "vol bloedvaten en is donker gepigmenteerd."),
            ("p", "Het <strong>glasachtig lichaam</strong> is de doorzichtige gelei die "
                  "<strong>de ruimte achter de lens opvult</strong>. Het <strong>kamervocht</strong> zit in "
                  "de <strong>voorste oogkamer</strong>, tussen het hoornvlies en de lens, en voedt het "
                  "hoornvlies."),
            ("p", "Het <strong>hoornvlies heeft geen bloedvaten</strong>, want die "
                  "<strong>zouden het licht tegenhouden en het zicht wazig maken</strong>. Het haalt zijn "
                  "voeding uit het kamervocht en de tranen. <strong>Knipperen</strong> dient om het "
                  "<strong>tranenvocht gelijk over het hoornvlies te verdelen</strong>."),
            ("p", "Rond elke oogbol liggen zes <strong>uitwendige oogspieren</strong> die het oog "
                  "<strong>in zijn kas laten draaien</strong>, zodat beide ogen op hetzelfde punt gericht "
                  "blijven."),
        ]),
        dict(kop="Accommodatie", blokken=[
            ("p", "De <strong>lens is elastisch</strong> en kan haar vorm veranderen; ze is dus niet "
                  "onveranderlijk bolvormig. Dat veranderen heet <strong>accommodatie</strong>: het "
                  "kringspiertje rond de lens trekt samen, de lens wordt boller, en zo zie je iets dichtbij "
                  "scherp."),
            ("p", "Kijk je <strong>van je blad op naar de bomen in de verte</strong>, dan wordt de lens "
                  "<strong>platter, want voor ver kijken moet het licht minder gebogen worden</strong>. "
                  "Licht van ver valt bijna recht binnen."),
            ("p", "Het oog werkt als een <strong>camera</strong>: de pupil is het diafragma, de lens het "
                  "objectief en het netvlies de sensor. Een camera stelt wel scherp door de lens te "
                  "verschuiven, en het oog door haar van vorm te veranderen."),
        ]),
        dict(kop="Het netvlies", blokken=[
            ("p", "In het netvlies liggen twee soorten lichtgevoelige cellen: "
                  "<strong>staafjes</strong> en <strong>kegeltjes</strong>. De "
                  "<strong>staafjes werken ook bij weinig licht</strong>, "
                  "<strong>geven geen kleur door</strong> en <strong>liggen vooral buiten het midden</strong> "
                  "van het netvlies. In het <strong>halfduister</strong> zie je daarom nauwelijks kleuren."),
            ("p", "De <strong>kegeltjes</strong> laten je <strong>kleuren zien</strong>. Er zijn drie "
                  "soorten, elk gevoelig voor een ander deel van het licht."),
            ("p", "De <strong>gele vlek</strong> is de <strong>plaats met de meeste kegeltjes, waar je het "
                  "scherpst ziet</strong>; ze ligt recht tegenover de pupil. De "
                  "<strong>blinde vlek</strong> is de plaats <strong>waar de oogzenuw het netvlies verlaat "
                  "en er geen lichtgevoelige cellen zijn</strong>."),
            ("p", "Van die blinde vlek merk je niets, want <strong>het andere oog ziet dat stukje wel, en de "
                  "hersenen vullen de rest aan</strong>. De <strong>oogzenuw</strong> brengt de impulsen van "
                  "het netvlies naar de hersenen."),
            ("p", "Het omzetten van licht in een waarneming verloopt zo: het "
                  "<strong>licht valt op een staafje of kegeltje</strong>, "
                  "<strong>die cel wekt een zenuwimpuls op</strong>, en de "
                  "<strong>oogzenuw brengt de impuls naar de hersenen</strong>. Wat je ziet, ligt dus "
                  "<strong>niet al helemaal vast op het netvlies</strong>: de hersenen zetten het beeld "
                  "recht, vullen de blinde vlek aan en koppelen het aan wat je al kent."),
            ("p", "Met <strong>twee ogen</strong> zie je diepte, want <strong>elk oog ziet het voorwerp "
                  "vanuit een iets andere hoek en de hersenen leggen die beelden samen</strong>."),
        ]),
        dict(kop="Afwijkingen van het oog", blokken=[
            ("p", "Bij <strong>bijziendheid</strong> ziet iemand dichtbij scherp en ver weg wazig: de "
                  "<strong>oogbol is te lang of de lens buigt te sterk, dus valt het beeld voor het "
                  "netvlies</strong>. Een <strong>holle lens</strong>, die het licht wat uiteen laat gaan, "
                  "corrigeert dat."),
            ("p", "Bij <strong>verziendheid</strong> zie je <strong>ver weg scherp maar dichtbij "
                  "wazig</strong>: de oogbol is te kort of de lens te zwak, zodat het beeld pas achter het "
                  "netvlies samenkomt. Een bolle lens helpt."),
            ("p", "<strong>Ouderdomsverziendheid</strong>: de <strong>lens wordt met de jaren stijver, "
                  "waardoor accommoderen moeilijker wordt</strong>. Daarom houden mensen hun boek verder weg "
                  "of nemen ze een leesbril."),
            ("p", "Bij <strong>kleurenblindheid</strong> <strong>werken een of meer soorten kegeltjes niet "
                  "goed</strong>, vaak die voor rood of groen. Bij <strong>astigmatisme</strong> is het "
                  "<strong>hoornvlies of de lens onregelmatig gekromd, waardoor lijnen vervormen</strong>; "
                  "een cilindrische lens maakt dat weer gelijk."),
            ("p", "Een bril met de <strong>verkeerde sterkte beschadigt het netvlies niet</strong>. Je ziet "
                  "er wazig door en kan er hoofdpijn van krijgen, maar schade geeft het niet."),
        ]),
    ],
    onthoud=[
        "Het licht gaat door hoornvlies, pupil, lens, glasachtig lichaam naar het netvlies.",
        "De iris regelt hoeveel licht binnenkomt; hoornvlies, kamervocht en lens buigen het licht af.",
        "De wand heeft drie lagen: hard oogvlies voor de vorm, vaatvlies voor bloed en strooilicht, netvlies voor het zien.",
        "Accommodatie is de lens boller of platter maken: boller voor dichtbij, platter voor ver.",
        "Staafjes zien grijs bij weinig licht, kegeltjes zien kleur; de gele vlek heeft de meeste kegeltjes.",
        "In de blinde vlek verlaat de oogzenuw het netvlies, en daar zie je niets.",
        "Het beeld op het netvlies staat op zijn kop; de hersenen zetten het recht.",
        "Bijziend betekent oogbol te lang, beeld voor het netvlies, en een holle lens corrigeert dat.",
        "Verziend betekent oogbol te kort, beeld achter het netvlies, en een bolle lens corrigeert dat.",
    ],
)

# ───────────────────────── 4. Het oor en het evenwicht
BUNDELS["het-oor-en-het-evenwicht-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het oor en het evenwicht",
    onder="Het uitwendige, midden- en inwendige oor, het orgaan van Corti, de afwijkingen van het gehoor, en het evenwichtsorgaan.",
    secties=[
        dict(kop="De drie delen van het oor", blokken=[
            ("p", "Bij het oor onderscheidt men het <strong>uitwendige oor</strong>, het "
                  "<strong>middenoor</strong> en het <strong>inwendige oor</strong>. Het geluid gaat "
                  "achtereenvolgens door die drie, en elk deel geeft het op zijn eigen manier door."),
            ("p", "Het <strong>uitwendige oor</strong> bestaat uit de <strong>oorschelp</strong>, de "
                  "<strong>gehoorgang</strong> en het <strong>trommelvel</strong>. De oorschelp "
                  "<strong>vangt het geluid op en leidt het naar de gehoorgang</strong>; haar vorm helpt ook "
                  "om te horen uit welke richting een geluid komt."),
            ("p", "Het <strong>trommelvel</strong> is het dunne vel aan het einde van de gehoorgang dat "
                  "<strong>door het geluid in beweging komt</strong>, net als het vel van een trommel."),
            ("p", "In het <strong>middenoor</strong> liggen de drie <strong>gehoorbeentjes</strong>: "
                  "<strong>hamer, aambeeld en stijgbeugel</strong>, genoemd naar hun vorm. Ze "
                  "<strong>versterken de trilling van het trommelvel</strong>: ze werken als een "
                  "hefboomsysteem en brengen de trilling van een groot vel naar een klein venstertje, "
                  "zodat de druk veel groter wordt."),
            ("p", "De <strong>buis van Eustachius</strong> <strong>verbindt het middenoor met de "
                  "neus-keelholte om de druk gelijk te houden</strong>. Daarom helpt slikken of gapen als je "
                  "oren in een vliegtuig dichtzitten."),
        ]),
        dict(kop="Het inwendige oor en het orgaan van Corti", blokken=[
            ("p", "Het <strong>slakkenhuis</strong> of de <strong>cochlea</strong> is het spiraalvormige "
                  "deel van het inwendige oor waarin het gehoor zit. Het is een met "
                  "<strong>vloeistof</strong> gevulde buis, opgerold als een slakkenschelp. In het "
                  "slakkenhuis <strong>reist het geluid dus niet meer door de lucht</strong>: de stijgbeugel "
                  "duwt op een venstertje en zet de vloeistof in beweging."),
            ("p", "De <strong>haarcellen</strong> die het geluid in zenuwimpulsen omzetten, liggen "
                  "<strong>in het orgaan van Corti in het slakkenhuis</strong>. Ze buigen mee met de "
                  "vloeistofgolf."),
            ("p", "De volledige weg van het geluid: <strong>oorschelp, gehoorgang, trommelvel, "
                  "gehoorbeentjes, slakkenhuis, gehoorzenuw</strong>. Lucht trilt, dan een vel, dan "
                  "beentjes, dan vloeistof, dan een haarcel, dan een zenuw."),
            ("p", "Een <strong>hoge toon</strong> komt op een andere plaats in het slakkenhuis aan dan een "
                  "lage: het <strong>membraan is niet overal even stijf, dus komt elke toonhoogte elders in "
                  "trilling</strong>. Bij het begin is het smal en stijf, verderop breed en slap."),
            ("p", "De <strong>gehoorzenuw</strong> brengt de geluidsimpulsen naar de hersenen. "
                  "<strong>Horen gebeurt pas echt in de hersenen</strong> en niet al in het slakkenhuis: "
                  "daar wordt er spraak, muziek of lawaai van gemaakt."),
        ]),
        dict(kop="Als het gehoor hapert", blokken=[
            ("p", "<strong>Geleidingsslechthorendheid</strong> betekent dat het geluid niet goed tot in het "
                  "inwendige oor raakt. Oorzaken: een <strong>prop oorsmeer in de gehoorgang</strong>, een "
                  "<strong>gaatje in het trommelvel</strong> of <strong>vocht in het middenoor na een "
                  "ontsteking</strong>."),
            ("p", "<strong>Haarcellen die door hard geluid beschadigd zijn, groeien bij de mens niet meer "
                  "terug</strong>. Gehoorschade is dus blijvend, en oordopjes op een festival of in een "
                  "werkplaats zijn geen overdreven voorzichtigheid."),
            ("p", "Bij <strong>ouderdomsslechthorendheid</strong> gaan vooral de hoge tonen verloren: de "
                  "<strong>haarcellen voor hoge tonen staan vooraan in het slakkenhuis en krijgen alle "
                  "geluid te verwerken</strong>. Die cellen slijten dus het snelst."),
            ("p", "Een <strong>hoortoestel herstelt geen haarcellen</strong>; het versterkt enkel het "
                  "geluid, zodat de cellen die nog werken meer te verwerken krijgen."),
            ("p", "Het oor beschermt zich tegen hard geluid doordat <strong>kleine spiertjes in het "
                  "middenoor de keten van beentjes spannen zodat die minder doorgeeft</strong>. Die reflex "
                  "werkt pas na een fractie van een seconde en niet sterk genoeg, dus helpt hij bij een knal "
                  "of urenlang lawaai weinig."),
            ("p", "<strong>Oorsuizen</strong> of <strong>tinnitus</strong> is <strong>een geluid horen dat "
                  "er van buiten niet is</strong>, vaak na gehoorschade: beschadigde haarcellen of de "
                  "zenuwbaan geven signalen door zonder prikkel."),
        ]),
        dict(kop="Het evenwichtsorgaan", blokken=[
            ("p", "Naast het slakkenhuis ligt het <strong>evenwichtsorgaan</strong>, in hetzelfde benige "
                  "doosje in de schedel. Het heeft twee zintuiglijke taken: de <strong>positiezin</strong> en de "
                  "<strong>rotatiezin</strong>. De positiezin zegt hoe je hoofd staat, de rotatiezin of en "
                  "hoe het draait."),
            ("p", "Er zijn <strong>drie halfcirkelvormige kanaaltjes</strong> per oor, die "
                  "<strong>loodrecht op elkaar staan</strong>, zodat <strong>elke draairichting van het "
                  "hoofd opgevangen</strong> kan worden: knikken, kantelen en rondkijken."),
            ("p", "In die kanaaltjes zit <strong>vloeistof</strong>. Begint je hoofd te draaien, dan "
                  "<strong>blijft de vloeistof door haar traagheid achter en buigt de haarcellen om</strong>. "
                  "<strong>Traagheid</strong> is de neiging van materie om haar beweging te houden."),
            ("p", "Draai je een hele tijd rond en stop je plots, dan blijf je duizelig omdat de "
                  "<strong>vloeistof nog doordraait en dus een draai meldt die er niet meer is</strong>. Je "
                  "ogen zeggen stil en je oor zegt draaien."),
            ("p", "De <strong>positiezin</strong> meet de <strong>stand van je hoofd ten opzichte van de "
                  "zwaartekracht</strong>: in de zakjes van het evenwichtsorgaan liggen gewichtjes op de "
                  "haarcellen. De positiezin en de rotatiezin zitten dus in <strong>hetzelfde orgaan maar in "
                  "verschillende structuren</strong>: de zakjes met gewichtjes en de drie kanaaltjes."),
            ("p", "Het evenwichtsorgaan <strong>werkt ook met je ogen dicht</strong>. Je hersenen gebruiken "
                  "voor je evenwicht drie bronnen: de <strong>signalen van het evenwichtsorgaan</strong>, "
                  "<strong>wat je ogen zien</strong> en de <strong>rek in spieren en gewrichten</strong>. De "
                  "<strong>kleine hersenen leggen die samen en stemmen de beweging erop af</strong>; de "
                  "signalen gaan dus eerst langs het centrale zenuwstelsel en niet rechtstreeks naar de "
                  "spieren."),
            ("p", "Word je <strong>wagenziek bij het lezen in de auto</strong>, dan is dat omdat je "
                  "<strong>oor beweging meldt terwijl je ogen een stilstaand blad zien</strong>. In het "
                  "<strong>donker over een oneffen pad</strong> struikel je sneller, want "
                  "<strong>een van de drie bronnen valt weg</strong>. Een <strong>danser</strong> blijft "
                  "recht omdat de hersenen <strong>door oefening de signalen anders leren wegen</strong>."),
            ("p", "Een <strong>ontsteking in het inwendige oor</strong> kan <strong>zowel het gehoor als het "
                  "evenwicht aantasten</strong>, want beide liggen vlak bij elkaar en delen hun zenuw. De "
                  "haarcellen van het slakkenhuis en die van het evenwichtsorgaan werken ook op dezelfde "
                  "manier: ze <strong>vangen beweging van vloeistof op</strong>, "
                  "<strong>zetten die om in zenuwimpulsen</strong> en <strong>liggen beide in het inwendige "
                  "oor</strong>. Enkel die van het slakkenhuis gaan over toonhoogte."),
        ]),
    ],
    onthoud=[
        "Drie delen: uitwendig oor (oorschelp, gehoorgang, trommelvel), middenoor (hamer, aambeeld, stijgbeugel) en inwendig oor.",
        "De gehoorbeentjes versterken de trilling; de buis van Eustachius houdt de druk gelijk.",
        "In het slakkenhuis reist het geluid door vloeistof; de haarcellen van het orgaan van Corti zetten het om.",
        "Elke toonhoogte komt elders in het slakkenhuis in trilling, want het membraan is niet overal even stijf.",
        "Beschadigde haarcellen groeien niet terug, dus is gehoorschade blijvend.",
        "Het evenwichtsorgaan heeft een positiezin (zakjes met gewichtjes) en een rotatiezin (drie kanaaltjes).",
        "De vloeistof in de kanaaltjes blijft door haar traagheid achter, en net dat wordt gevoeld.",
        "Evenwicht komt van drie bronnen: oor, ogen en de rek in spieren en gewrichten, samengelegd door de kleine hersenen.",
    ],
)

# ───────────────────────── 5. De spieren en de klieren
BUNDELS["de-spieren-en-de-klieren-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De spieren en de klieren",
    onder="De drie soorten spierweefsel, de microscopische bouw van een spier, de klieren, de hormonen en de eilandjes van Langerhans.",
    secties=[
        dict(kop="De drie soorten spierweefsel", blokken=[
            ("p", "Bij de mens onderscheidt men <strong>skeletspierweefsel</strong>, "
                  "<strong>glad spierweefsel</strong> en <strong>hartspierweefsel</strong>. Pezen en "
                  "kraakbeen zijn geen spier."),
            ("p", "<strong>Skeletspierweefsel</strong> <strong>kan je met je wil aansturen</strong>, "
                  "<strong>ziet onder de microscoop gestreept uit</strong> en "
                  "<strong>hecht met pezen aan de botten vast</strong>. Een <strong>pees</strong> is stevig "
                  "bindweefsel zonder rekbaarheid, zodat de kracht helemaal naar het bot gaat."),
            ("p", "<strong>Glad spierweefsel</strong> komt onder meer voor in de "
                  "<strong>wand van de darmen en de bloedvaten</strong>, en werkt buiten je wil om. De "
                  "<strong>hartspier</strong> is <strong>gestreept zoals een skeletspier maar werkt buiten je "
                  "wil, en zijn cellen zijn met elkaar verbonden</strong>."),
            ("p", "Een spier <strong>kan enkel trekken, niet duwen</strong>. Daarom bestaat er voor elke "
                  "beweging een <strong>antagonistisch spierpaar</strong>: "
                  "<strong>twee spieren die tegengesteld werken</strong>, zoals de buiger en de strekker van "
                  "de arm."),
        ]),
        dict(kop="De microscopische bouw van een spier", blokken=[
            ("p", "Het <strong>sarcomeer</strong> is de <strong>kleinste eenheid die in een spiervezel "
                  "samentrekt, tussen twee Z-platen</strong>. Een spiervezel is een lange rij sarcomeren "
                  "achter elkaar. De <strong>Z-platen</strong> zijn de dwarse schotjes die een sarcomeer "
                  "<strong>aan beide kanten begrenzen</strong>."),
            ("p", "In een sarcomeer liggen twee soorten filamenten: de dunne "
                  "<strong>actinefilamenten</strong>, die aan de Z-platen hangen, en de dikke "
                  "<strong>myosinefilamenten</strong> in het midden."),
            ("p", "Een sarcomeer wordt korter doordat de "
                  "<strong>myosinefilamenten de actinefilamenten naar het midden toe trekken</strong>. De "
                  "<strong>filamenten worden zelf niet korter</strong>; ze schuiven alleen langs elkaar. "
                  "Daarom heet dit het <strong>schuiffilamentmodel</strong>."),
            ("p", "Onder de microscoop zie je een <strong>donkere band</strong> waar de "
                  "<strong>dikke myosinefilamenten liggen</strong>, want daar gaat minder licht door. In de "
                  "<strong>lichte band</strong> liggen <strong>enkel actinefilamenten</strong>. Bij een "
                  "samentrekking wordt net die <strong>lichte band smaller</strong>."),
            ("p", "Om samen te trekken heeft een spiervezel nodig: een "
                  "<strong>prikkel van een motorische zenuwcel</strong>, "
                  "<strong>energie uit de celademhaling</strong> en <strong>calciumionen in de cel</strong>. "
                  "Licht komt er niet bij te pas. De plaats waar een motorische zenuwcel een spiervezel "
                  "aanspreekt, heet de <strong>motorische eindplaat</strong>."),
            ("p", "Spierweefsel heeft <strong>veel mitochondriën</strong>, want "
                  "<strong>daar wordt de energie vrijgemaakt die een samentrekking kost</strong>. Bij "
                  "<strong>zwaar inspannen</strong> werkt een spier een tijdje door zonder genoeg zuurstof, "
                  "en dan <strong>vormt zich melkzuur</strong>: dat geeft het branderige gevoel."),
            ("p", "Houd je een <strong>boek stil in je uitgestrekte hand</strong> en begint je arm na een "
                  "tijd te trillen, dan is dat omdat de "
                  "<strong>spiervezels in ploegen werken en de overgangen bij vermoeidheid niet meer gelijk "
                  "vallen</strong>."),
        ]),
        dict(kop="Klieren en hormonen", blokken=[
            ("p", "Een <strong>klier zonder afvoergang geeft haar stof rechtstreeks aan het bloed af</strong>. "
                  "Klieren mét afvoergang, zoals de zweetklier, lozen naar buiten of in een holte."),
            ("p", "Een <strong>hormoon</strong> is een <strong>boodschapperstof die een klier aan het bloed "
                  "afgeeft</strong>. Het komt overal, maar werkt <strong>enkel op cellen die er de passende "
                  "receptor voor hebben</strong>. Daarom is een hormoon toch doelgericht."),
            ("p", "Klieren zonder afvoergang zijn onder andere de <strong>schildklier</strong>, de "
                  "<strong>bijnier</strong> en de <strong>eilandjes van Langerhans</strong> in de pancreas."),
            ("p", "Een <strong>hormoon werkt trager dan een zenuwimpuls</strong>: het moet met het bloed "
                  "meereizen en doet er seconden tot minuten over. Daarom werken de twee stelsels samen: "
                  "<strong>het zenuwstelsel reageert snel en kort, de hormonen houden de reactie langer "
                  "aan</strong>."),
            ("p", "De <strong>hypofyse</strong> is de dirigent van de klieren: ze "
                  "<strong>geeft hormonen af die andere klieren aanzetten of afremmen</strong>, onder andere "
                  "de schildklier en de geslachtsklieren. De <strong>schildklier</strong> in de hals regelt "
                  "met <strong>thyroxine</strong> de <strong>snelheid van de stofwisseling</strong>."),
            ("p", "Een klier kan <strong>tegelijk effector van het zenuwstelsel en zender van hormonen</strong> "
                  "zijn: de <strong>bijnier</strong> geeft op een zenuwsignaal "
                  "<strong>adrenaline</strong> af. Dat hormoon zet het lichaam bij schrik of gevaar in actie: "
                  "de <strong>hartslag versnelt</strong>, de <strong>pupillen worden groter</strong> en er "
                  "<strong>komt glucose uit de lever vrij</strong>. De spijsvertering gaat juist op een lager "
                  "pitje."),
        ]),
        dict(kop="De eilandjes van Langerhans", blokken=[
            ("p", "De <strong>eilandjes van Langerhans</strong> zijn de groepjes hormoonvormende cellen in "
                  "de pancreas. Ze liggen verspreid tussen het weefsel dat spijsverteringssappen maakt, en ze "
                  "regelen het <strong>bloedglucosegehalte</strong>."),
            ("p", "De <strong>bètacellen</strong> maken <strong>insuline</strong>. Insuline "
                  "<strong>laat de cellen glucose uit het bloed opnemen, zodat het bloedglucosegehalte "
                  "daalt</strong>, en laat de lever glucose opslaan."),
            ("p", "De <strong>alfacellen</strong> maken <strong>glucagon</strong>, dat het "
                  "<strong>bloedglucosegehalte laat stijgen</strong>: het geeft de lever het signaal om haar "
                  "voorraad af te breken. Insuline en glucagon <strong>werken dus tegengesteld</strong>."),
            ("p", "Eet je een <strong>boterham met confituur</strong>, dan "
                  "<strong>stijgt het bloedglucosegehalte, geven de bètacellen insuline af en daalt het "
                  "gehalte weer</strong>. Na een lange inspanning is het gehalte juist laag: dan "
                  "<strong>geven de alfacellen glucagon af en breekt de lever haar voorraad af</strong>."),
            ("p", "Zo'n <strong>feedbacksysteem met hormonen houdt een waarde in het lichaam binnen nauwe "
                  "grenzen</strong>, en dat is precies homeostase."),
            ("p", "Bij <strong>diabetes type 1</strong> <strong>maken de bètacellen geen of te weinig "
                  "insuline meer aan</strong>, vaak omdat het eigen afweersysteem ze beschadigd heeft. Daarom "
                  "moet de insuline van buiten toegediend worden."),
        ]),
    ],
    onthoud=[
        "Drie soorten spierweefsel: skelet (willekeurig, gestreept), glad (onwillekeurig) en hartspier (gestreept én onwillekeurig).",
        "Een spier kan enkel trekken; daarom hoort bij elke beweging een antagonistisch spierpaar.",
        "Een sarcomeer ligt tussen twee Z-platen; de myosine trekt de actine naar het midden en de filamenten schuiven langs elkaar.",
        "De lichte band bevat enkel actine en wordt bij een samentrekking smaller.",
        "Een spiervezel heeft een prikkel, energie en calcium nodig; bij zuurstofgebrek vormt zich melkzuur.",
        "Een klier zonder afvoergang geeft haar hormoon aan het bloed; het werkt enkel op cellen met de juiste receptor.",
        "Bètacellen maken insuline (gehalte daalt), alfacellen glucagon (gehalte stijgt).",
        "Bij diabetes type 1 maken de bètacellen geen insuline meer aan.",
        "Het zenuwstelsel reageert snel en kort, hormonen werken trager maar langer door.",
    ],
)

# ───────────────────────── 6. Voortplanting en de menstruatiecyclus
BUNDELS["voortplanting-en-de-menstruatiecyclus-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Voortplanting en de menstruatiecyclus",
    onder="Gameten en bevruchting, de zwangerschap en de placenta, de puberteit, en de menstruatiecyclus in haar drie fasen.",
    secties=[
        dict(kop="Gameten en bevruchting", blokken=[
            ("p", "De geslachtscellen van de mens heten <strong>gameten</strong>: de eicel en de zaadcel. "
                  "Een gameet heeft de <strong>helft van het aantal chromosomen van een gewone "
                  "lichaamscel</strong>: 23 in plaats van 46. Bij de bevruchting komen die twee helften "
                  "samen tot 46."),
            ("p", "De <strong>zaadcellen</strong> worden gevormd in de <strong>teelballen</strong>, in "
                  "kronkelige buisjes. Die liggen buiten de buikholte omdat de vorming een iets lagere "
                  "temperatuur vraagt."),
            ("p", "De <strong>eierstok</strong> laat <strong>eicellen rijpen</strong> en geeft "
                  "<strong>oestrogeen</strong> en <strong>progesteron</strong> af. Het innestelen gebeurt "
                  "niet daar maar in het baarmoederslijmvlies."),
            ("p", "De <strong>bevruchting</strong> vindt meestal plaats <strong>in de eileider</strong>. "
                  "<strong>Eén zaadcel volstaat</strong>: zodra er één binnen is, verandert de buitenlaag "
                  "van de eicel zodat er geen tweede meer door kan."),
            ("p", "De cel die ontstaat als zaadcel en eicel samensmelten, is de "
                  "<strong>zygote</strong>: de eerste cel van een nieuw individu, met 46 chromosomen. In de "
                  "dagen erna <strong>deelt ze zich herhaaldelijk en reist ze naar de baarmoeder om in te "
                  "nestelen</strong>. Die <strong>innesteling</strong> is het vastzetten van het celklompje "
                  "in het baarmoederslijmvlies, na ongeveer een week."),
            ("p", "Een kind lijkt op beide ouders omdat het "
                  "<strong>de helft van zijn chromosomen van elke ouder krijgt</strong>. De vorming van "
                  "gameten is daarom een bijzondere celdeling: het "
                  "<strong>aantal chromosomen wordt gehalveerd en elke gameet is uniek</strong>. Daarom "
                  "zijn broers en zussen niet gelijk."),
        ]),
        dict(kop="De zwangerschap", blokken=[
            ("p", "De <strong>placenta</strong> dient om <strong>stoffen uit te wisselen tussen het bloed "
                  "van de moeder en dat van het kind</strong>. De bloedbanen liggen er heel dicht bij "
                  "elkaar, maar het <strong>bloed vermengt zich niet</strong>: er zit een dunne wand tussen. "
                  "Dat is nodig, want de bloedgroepen kunnen verschillen."),
            ("p", "Door de placenta gaan <strong>zuurstof</strong>, <strong>voedingsstoffen</strong>, maar "
                  "ook <strong>alcohol en nicotine</strong>. Rode bloedcellen van de moeder zijn te groot en "
                  "blijven aan haar kant."),
            ("p", "De <strong>navelstreng</strong> verbindt het kind met de placenta. Daarin lopen twee "
                  "slagaders en een vene, zodat zuurstof en voeding heen en afvalstoffen terug gaan."),
            ("p", "Het <strong>vruchtwater</strong> <strong>beschermt het kind tegen stoten en houdt de "
                  "temperatuur gelijk</strong>; het werkt als een kussen. De zuurstof komt via de placenta."),
            ("p", "Een <strong>eeneiige tweeling</strong> komt uit één bevruchte eicel en heeft dus "
                  "<strong>hetzelfde erfelijk materiaal</strong>. Bij een twee-eiige tweeling zijn er twee "
                  "eicellen en twee zaadcellen; die twee verschillen zoals broers en zussen."),
        ]),
        dict(kop="De puberteit", blokken=[
            ("p", "Bij de <strong>puberteit</strong> beginnen de "
                  "<strong>geslachtsklieren hormonen af te geven</strong>, worden de "
                  "<strong>geslachtsorganen rijp</strong> en ontstaan er "
                  "<strong>secundaire geslachtskenmerken</strong>. Het aantal chromosomen in de "
                  "lichaamscellen blijft levenslang hetzelfde."),
            ("p", "Die hormonen worden door de <strong>hypofyse aangestuurd</strong>, niet door de "
                  "schildklier: zij zet de eierstokken en de teelballen aan het werk, en die maken dan zelf "
                  "<strong>oestrogeen</strong> of <strong>testosteron</strong>."),
        ]),
        dict(kop="De drie fasen van de menstruatiecyclus", blokken=[
            ("p", "De cyclus heeft drie fasen: de <strong>menstruatiefase</strong>, de "
                  "<strong>folliculaire fase</strong> en de <strong>luteale fase</strong>. Gemiddeld duurt "
                  "het geheel 28 dagen, maar <strong>24 tot 35 dagen komt vaak voor en is gewoon</strong>."),
            ("p", "Een <strong>follikel</strong> is het blaasje in de eierstok waarin een eicel rijpt: een "
                  "holte met vocht en cellen, en die cellen maken ook oestrogeen aan. In de "
                  "<strong>folliculaire fase rijpt een follikel en wordt het baarmoederslijmvlies opnieuw "
                  "opgebouwd</strong>, onder invloed van <strong>oestrogeen</strong>, het hormoon dat in de "
                  "eerste helft van de cyclus overheerst."),
            ("p", "De <strong>ovulatie</strong> of eisprong is het "
                  "<strong>vrijkomen van de eicel uit de eierstok</strong>: de rijpe follikel barst open. "
                  "Bij een cyclus van 28 dagen is dat rond dag veertien. De ovulatie "
                  "<strong>valt tussen de folliculaire en de luteale fase</strong> en is dus het keerpunt."),
            ("p", "Na de ovulatie blijft het <strong>geel lichaam</strong> over, dat "
                  "<strong>progesteron</strong> afgeeft. Progesteron "
                  "<strong>houdt het baarmoederslijmvlies dik en klaar</strong> voor een innesteling, en "
                  "remt tegelijk de rijping van een nieuwe follikel."),
            ("p", "<strong>Blijft een bevruchting uit, dan sterft het geel lichaam af en daalt het "
                  "progesteron</strong>. Daarom treedt er een <strong>menstruatie</strong> op: het "
                  "slijmvlies wordt niet meer in stand gehouden, laat los en verlaat met wat bloed de "
                  "baarmoeder."),
            ("p", "Is er <strong>wel een bevruchting en innesteling</strong>, dan "
                  "<strong>blijft het geel lichaam nog weken progesteron afgeven zodat het slijmvlies "
                  "behouden blijft</strong>. Het ingenestelde klompje geeft daarvoor zelf een hormoon af."),
        ]),
        dict(kop="Hoe de cyclus gestuurd wordt", blokken=[
            ("p", "De <strong>hypofyse</strong> stuurt de eierstok met twee hormonen aan: het ene "
                  "<strong>laat de follikel rijpen</strong>, het andere "
                  "<strong>lokt de ovulatie uit</strong>. Omgekeerd remmen of stimuleren de hormonen van de "
                  "eierstok de hypofyse weer: de twee <strong>beïnvloeden elkaar wederzijds</strong>. De "
                  "menstruatiecyclus is dus <strong>een proces dat door hormonen met terugkoppeling "
                  "geregeld wordt</strong>."),
            ("p", "Duurt een cyclus <strong>32 in plaats van 28 dagen</strong>, dan is meestal de "
                  "<strong>folliculaire fase langer, want die kan sterk in lengte verschillen</strong>. De "
                  "luteale fase ligt vrij vast rond veertien dagen, omdat het geel lichaam ongeveer zo lang "
                  "leeft."),
            ("p", "Rond de ovulatie kunnen deze tekens wijzen: een "
                  "<strong>lichte stijging van de lichaamstemperatuur</strong>, een "
                  "<strong>verandering van het baarmoederhalsslijm</strong> en "
                  "<strong>soms een lichte pijn in de onderbuik</strong>."),
            ("p", "De kans op zwangerschap is het grootst <strong>rond de ovulatie, want de eicel is maar "
                  "een korte tijd bevruchtbaar</strong>: ongeveer een dag, tegen enkele dagen voor "
                  "zaadcellen. Bij een <strong>onregelmatige cyclus</strong> is de kalender alleen "
                  "onvoldoende, want de <strong>folliculaire fase varieert, dus valt de ovulatie niet elke "
                  "maand op dezelfde dag</strong>."),
            ("p", "De <strong>gecombineerde anticonceptiepil</strong> werkt doordat de "
                  "<strong>hormonen erin de hypofyse remmen, zodat er geen ovulatie komt</strong>: door "
                  "voortdurend oestrogeen en progesteron aan te voeren, denkt de hypofyse dat de luteale "
                  "fase bezig is."),
            ("p", "De <strong>menopauze</strong> is het einde van de vruchtbare periode: de voorraad "
                  "follikels raakt op, het oestrogeen daalt en de cyclus stopt definitief."),
        ]),
    ],
    onthoud=[
        "Gameten hebben 23 chromosomen, een lichaamscel 46; bij de bevruchting komen de helften samen.",
        "De bevruchting gebeurt in de eileider; de zygote nestelt zich na ongeveer een week in het baarmoederslijmvlies in.",
        "In de placenta wisselen stoffen uit, maar het bloed van moeder en kind vermengt niet.",
        "Drie fasen: menstruatiefase, folliculaire fase (oestrogeen bouwt op) en luteale fase (progesteron houdt in stand).",
        "De ovulatie ligt tussen de twee fasen in, bij een cyclus van 28 dagen rond dag veertien.",
        "Na de ovulatie blijft het geel lichaam over; sterft het af, dan daalt het progesteron en volgt de menstruatie.",
        "De hypofyse stuurt de eierstok aan en de eierstok stuurt de hypofyse terug: terugkoppeling.",
        "De luteale fase duurt ongeveer veertien dagen; de folliculaire fase varieert in lengte.",
        "De pil remt de hypofyse, zodat er geen ovulatie komt.",
    ],
)

# ───────────────────────── 7. Biodiversiteit en micro-organismen
BUNDELS["biodiversiteit-en-micro-organismen-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Biodiversiteit en micro-organismen",
    onder="De drie niveaus van biodiversiteit, soorten en classificatie, de bedreigingen, en bacteriën, virussen en de afweer.",
    secties=[
        dict(kop="Wat biodiversiteit is", blokken=[
            ("p", "<strong>Biodiversiteit</strong> is de <strong>verscheidenheid aan leven, van genen over "
                  "soorten tot ecosystemen</strong>. Je kan ze dus op drie niveaus bekijken: de "
                  "<strong>variatie binnen een soort</strong>, het "
                  "<strong>aantal verschillende soorten</strong> en de "
                  "<strong>verscheidenheid aan ecosystemen</strong>."),
            ("p", "Twee organismen horen tot <strong>dezelfde soort</strong> als ze "
                  "<strong>zich onderling kunnen voortplanten en vruchtbare nakomelingen krijgen</strong>. "
                  "Een paard en een ezel krijgen wel een muil, maar die is onvruchtbaar: het zijn dus twee "
                  "soorten."),
            ("p", "<strong>Variatie binnen een soort</strong> is belangrijk, want "
                  "<strong>bij een ziekte of een verandering overleven er altijd nog individuen</strong>. "
                  "Zijn alle individuen gelijk, dan treft één ziekte ze allemaal."),
            ("p", "Een <strong>akker met één gewas</strong> heeft een <strong>lagere biodiversiteit</strong> "
                  "dan een hooiland met tientallen plantensoorten en de insecten die daarbij horen. Een "
                  "gebied met <strong>veel soorten herstelt sneller</strong> na een verstoring, want een "
                  "andere soort kan de rol overnemen van wie wegvalt."),
            ("p", "Een <strong>ecosysteemdienst</strong> is een <strong>nut dat de natuur de mens "
                  "levert</strong>, zoals bestuiving, waterzuivering of bodemleven dat afval opruimt."),
        ]),
        dict(kop="Soorten benoemen en indelen", blokken=[
            ("p", "<strong>Classificatie</strong> is het <strong>indelen van organismen in groepen volgens "
                  "hun verwantschap</strong>: van soort over geslacht en familie tot rijk. Levende rijken "
                  "zijn onder andere de <strong>bacteriën</strong>, de <strong>schimmels</strong>, de "
                  "<strong>planten en de dieren</strong> en de eencellige organismen. Mineralen leven niet "
                  "en horen er niet bij."),
            ("p", "<strong>Determineren</strong> is de soort opzoeken aan de hand van haar kenmerken. Een "
                  "<strong>determinatietabel</strong> stelt telkens een keuze tussen twee kenmerken; je moet "
                  "dus goed kijken en de juiste tak volgen."),
            ("p", "Elke soort krijgt een <strong>wetenschappelijke naam met twee delen</strong>, een "
                  "geslachtsnaam en een soortnaam, en die is <strong>overal ter wereld dezelfde</strong>. "
                  "Biologen gebruiken die omdat een <strong>volkse naam per streek en per taal "
                  "verschilt</strong>."),
        ]),
        dict(kop="Wat de biodiversiteit bedreigt", blokken=[
            ("p", "De grote menselijke oorzaken zijn het "
                  "<strong>verdwijnen en versnipperen van leefgebieden</strong>, "
                  "<strong>vervuiling van bodem, water en lucht</strong>, en het "
                  "<strong>binnenbrengen van soorten die er niet thuishoren</strong>. Een "
                  "<strong>invasieve soort</strong> of exoot komt van elders, heeft hier geen natuurlijke "
                  "vijanden en verdringt het inheemse leven."),
            ("p", "<strong>Versnipperen</strong> is schadelijk ook als de oppervlakte gelijk blijft, want "
                  "<strong>kleine groepen raken van elkaar gescheiden, waardoor de variatie in hun erfelijk "
                  "materiaal afneemt</strong>. Een <strong>ecoduct</strong> of natuurbrug "
                  "<strong>verbindt versnipperde gebieden weer met elkaar</strong>."),
            ("p", "Het <strong>uitsterven van soorten gebeurt vandaag veel sneller dan uit de natuurlijke "
                  "achtergrond te verwachten is</strong>, en de oorzaak daarvan is grotendeels menselijk."),
            ("p", "Wordt een <strong>vijver gedempt voor een parking</strong>, dan "
                  "<strong>verdwijnen de soorten die van water afhangen</strong>; niet elke soort kan "
                  "verhuizen. In je eigen tuin verhoog je de biodiversiteit door "
                  "<strong>inheemse planten te zetten die bloeien voor insecten</strong>, "
                  "<strong>een hoekje te laten verwilderen</strong> en "
                  "<strong>geen chemische bestrijdingsmiddelen te gebruiken</strong>."),
        ]),
        dict(kop="Bacteriën, virussen en schimmels", blokken=[
            ("p", "Een <strong>micro-organisme</strong> is een <strong>levend wezen dat te klein is om met "
                  "het blote oog te zien</strong>."),
            ("p", "Een <strong>bacterie</strong> <strong>bestaat uit één cel</strong>, "
                  "<strong>heeft geen echte celkern</strong> en <strong>kan zich zelf delen</strong>. Ze "
                  "<strong>deelt zich in twee, en in gunstige omstandigheden kan dat elk half uur</strong>: "
                  "uit één bacterie worden er in tien uur al miljoenen. Daarom bederft voedsel in de warmte "
                  "zo vlug, en daarom laat je geen <strong>restje soep een nacht op het aanrecht</strong> "
                  "staan."),
            ("p", "Een <strong>virus</strong> is geen gewoon levend wezen: het "
                  "<strong>heeft geen eigen stofwisseling en kan zich enkel in een gastheercel "
                  "vermeerderen</strong>. Het is weinig meer dan erfelijk materiaal in een jasje."),
            ("p", "<strong>Antibiotica werken tegen bacteriën en niet tegen virussen</strong>, want ze "
                  "grijpen in op iets dat enkel een bacterie heeft, zoals haar celwand. Bij een griep of een "
                  "verkoudheid helpen ze dus niet."),
            ("p", "<strong>Antibioticaresistentie</strong> betekent dat "
                  "<strong>bacteriën die tegen een antibioticum kunnen, overleven en zich "
                  "vermeerderen</strong>. Een <strong>kuur afmaken</strong> helpt dat voorkomen: stop je te "
                  "vroeg, dan blijven net de taaiste bacteriën over."),
            ("p", "De mens gebruikt micro-organismen voor het "
                  "<strong>maken van yoghurt en kaas</strong>, het "
                  "<strong>rijzen van brood en het brouwen van bier</strong>, en het "
                  "<strong>zuiveren van afvalwater</strong>. <strong>Gist</strong> is een eencellige "
                  "schimmel die suiker omzet en koolstofdioxide maakt, en dat gas blaast het deeg op."),
            ("p", "In een ecosysteem <strong>breken bacteriën en schimmels dood materiaal af en maken de "
                  "mineralen weer vrij</strong>. Zonder hen <strong>bleven die mineralen opgesloten</strong>. "
                  "Niet alle bacteriën zijn schadelijk: de meeste zijn onschuldig of zelfs nuttig, zoals de "
                  "darmbacteriën."),
        ]),
        dict(kop="Hoe het lichaam zich verweert", blokken=[
            ("p", "De eerste verdedigingslinie bestaat uit de <strong>onbeschadigde huid</strong>, het "
                  "<strong>zuur in de maag</strong> en het <strong>slijm in de luchtwegen</strong> met zijn "
                  "trilhaartjes. Het skelet speelt daarin geen rol."),
            ("p", "<strong>Witte bloedcellen</strong> <strong>eten indringers op of maken antistoffen tegen "
                  "ze</strong>. Een <strong>antistof</strong> past op één soort indringer, hecht zich eraan "
                  "en maakt hem onschadelijk of kenbaar voor de opruimers."),
            ("p", "Een <strong>vaccin</strong> <strong>laat het lichaam antistoffen en afweercellen aanmaken "
                  "zonder dat je ziek wordt</strong>: het toont het afweersysteem een onschadelijk stuk van "
                  "de ziekteverwekker. <strong>Na een ziekte ben je tegen diezelfde verwekker vaak een tijd "
                  "beschermd</strong>, want het afweersysteem houdt cellen over die hem herkennen."),
            ("p", "<strong>Handen wassen</strong> is doeltreffend omdat "
                  "<strong>zeep en water de micro-organismen van de huid halen, voor ze in het lichaam "
                  "raken</strong>. De meeste besmettingen gaan via de handen naar mond, neus of ogen."),
        ]),
    ],
    onthoud=[
        "Biodiversiteit kijkt naar drie niveaus: genen binnen een soort, het aantal soorten en de ecosystemen.",
        "Dezelfde soort betekent: onderling vruchtbare nakomelingen kunnen krijgen.",
        "De drie grote bedreigingen zijn verlies en versnippering van leefgebied, vervuiling en invasieve soorten.",
        "Elke soort heeft een wetenschappelijke naam van twee delen die overal ter wereld dezelfde is.",
        "Een bacterie is één cel zonder echte kern en deelt zich zelf; een virus heeft een gastheercel nodig.",
        "Antibiotica werken enkel tegen bacteriën; onnodig gebruik en een kuur niet afmaken leiden tot resistentie.",
        "Bacteriën en schimmels zijn reducenten: zij maken de mineralen uit dood materiaal weer vrij.",
        "Huid, maagzuur en slijmvliezen zijn de eerste afweer; witte bloedcellen en antistoffen de tweede.",
        "Een vaccin laat het lichaam antistoffen maken zonder dat je ziek wordt.",
    ],
)

# ───────────────────────── 8. Gedrag en interactie
BUNDELS["gedrag-en-interactie-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gedrag en interactie",
    onder="Aangeboren en geleerd gedrag, de vormen van leren, de relaties tussen soorten, en het leven in een groep.",
    secties=[
        dict(kop="Wat gedrag is", blokken=[
            ("p", "Een bioloog bedoelt met <strong>gedrag</strong>: <strong>alles wat een dier doet als "
                  "antwoord op prikkels van binnen of van buiten</strong>. Honger is een inwendige prikkel, "
                  "het geluid van een roofdier een uitwendige."),
            ("p", "<strong>Inwendige prikkels</strong> zijn bijvoorbeeld <strong>honger</strong>, "
                  "<strong>dorst</strong> en een <strong>hormoonspiegel die stijgt in het "
                  "broedseizoen</strong>."),
            ("p", "Een <strong>sleutelprikkel</strong> is een <strong>bepaalde prikkel die een vast "
                  "gedragspatroon in gang zet</strong>: een rode vlek op de snavel van een meeuw zet het "
                  "kuiken aan om te bedelen."),
            ("p", "Het <strong>dagritme</strong> of circadiaans ritme is het terugkerende ritme van ongeveer "
                  "een etmaal dat slapen, eten en actief zijn regelt. Het loopt ook door als het licht niet "
                  "verandert, want het dier heeft een eigen klok."),
            ("p", "Wie gedrag <strong>wetenschappelijk</strong> wil beschrijven, "
                  "<strong>let eerst op wat hij ziet en pas daarna op wat hij erover denkt</strong>. Eerst "
                  "observeren en noteren, dan verklaren. Wil je weten of "
                  "<strong>muizen een doolhof leren</strong>, dan "
                  "<strong>meet je de tijd per poging bij een groep muizen en kijk je of die daalt</strong>: "
                  "leren zie je aan een verbetering over herhaalde pogingen."),
        ]),
        dict(kop="Aangeboren gedrag", blokken=[
            ("p", "<strong>Aangeboren gedrag</strong> of instinctief gedrag "
                  "<strong>staat vanaf de geboorte vast</strong>, "
                  "<strong>verloopt bij alle dieren van die soort ongeveer gelijk</strong> en "
                  "<strong>moet niet geleerd worden</strong>. Het zit in het erfelijk materiaal."),
            ("p", "Het is nuttig voor een pasgeboren dier omdat het "
                  "<strong>meteen werkt, zonder dat er tijd is om iets te leren</strong>. Een kuiken dat moet "
                  "eten en vluchten heeft geen tijd om te oefenen. Het nadeel is dat zulk gedrag zich niet "
                  "aan iets nieuws aanpast."),
            ("p", "Een <strong>reflex is een vorm van aangeboren gedrag</strong>: hij ligt vast, verloopt bij "
                  "iedereen gelijk en wordt niet geleerd."),
        ]),
        dict(kop="Geleerd gedrag", blokken=[
            ("p", "<strong>Gewenning</strong>: een <strong>dier reageert steeds minder op een prikkel die "
                  "telkens zonder gevolg blijft</strong>. Vogels die eerst van een vogelverschrikker "
                  "schrikken, gaan er na een week vlak naast zitten."),
            ("p", "<strong>Conditionering</strong>: een dier <strong>koppelt een prikkel aan een "
                  "gevolg</strong>. Een hond die kwijlt bij het geluid van zijn bak, of die "
                  "<strong>gaat zitten zodra zijn baas een leeg koekjesdoosje laat ritselen</strong>: het "
                  "<strong>geluid is door herhaling aan een belonend gevolg gekoppeld geraakt</strong>."),
            ("p", "<strong>Leren door nadoen</strong>: een <strong>jong dier dat zijn moeder nadoet</strong>, "
                  "neemt over wat het ziet. Daarom eten jonge mezen wat hun ouders eten."),
            ("p", "<strong>Inprenting</strong>: een <strong>jong dier legt in een korte gevoelige periode "
                  "vast wie zijn ouder is</strong>. Pas uitgekomen eendenkuikens volgen wat ze eerst zien "
                  "bewegen, en dat venster gaat daarna niet meer open."),
            ("p", "Geleerd gedrag is een voordeel in een veranderende omgeving, want het "
                  "<strong>dier kan zijn gedrag bijstellen als de omstandigheden anders worden</strong>. Het "
                  "wordt echter <strong>niet erfelijk doorgegeven</strong>: jongen kunnen het wel van hun "
                  "ouders overnemen door te kijken en na te doen."),
            ("p", "Veel gedrag is <strong>deels aangeboren en deels geleerd</strong>. Bij de "
                  "<strong>zang van vogels</strong> ligt de grondvorm vast, maar de "
                  "<strong>uitvoering wordt van soortgenoten geleerd</strong>; daarom hebben sommige soorten "
                  "plaatselijke dialecten."),
        ]),
        dict(kop="Relaties tussen soorten", blokken=[
            ("p", "Een <strong>interactie</strong> is een <strong>wederzijdse invloed tussen twee "
                  "organismen</strong>, die voor elk van de twee voordelig, nadelig of onverschillig kan "
                  "uitvallen. Die combinaties geven de soorten relaties."),
            ("p", "<strong>Predatie</strong>: het <strong>ene organisme doodt en eet het andere</strong>. Er "
                  "is een prooi en een roofdier: nadelig voor de prooi, voordelig voor de jager."),
            ("p", "<strong>Competitie</strong> of concurrentie is de <strong>strijd om dezelfde beperkte "
                  "hulpbron</strong>, en werkt voor beide nadelig. <strong>Binnen een soort overlappen de "
                  "behoeften volledig</strong>, dus is de strijd daar het scherpst."),
            ("p", "<strong>Symbiose</strong> waarbij <strong>beide voordeel hebben</strong>: een bij en een "
                  "bloem, een korstmos met een alg en een schimmel, de darmbacteriën en wij. Ook een "
                  "<strong>eikel die door een gaai weggedragen wordt</strong> valt voor beide goed uit: de "
                  "gaai krijgt voedsel, de eik krijgt haar zaad ver van de moederboom."),
            ("p", "Een <strong>parasiet</strong> <strong>leeft op of in een ander en brengt het schade toe "
                  "zonder het meteen te doden</strong>, zoals een teek of een lintworm. Hij doodt zijn "
                  "gastheer meestal niet, want <strong>een dode gastheer levert geen voeding meer</strong>."),
            ("p", "<strong>Commensalisme</strong>: de <strong>een heeft voordeel, de ander ondervindt "
                  "niets</strong>. Een zeepok op de huid van een walvis reist mee en de walvis merkt het niet."),
            ("p", "<strong>Twee soorten die precies hetzelfde eten op dezelfde plaats</strong>, kunnen "
                  "<strong>moeilijk blijvend naast elkaar bestaan</strong>: volledige overlap geeft volledige "
                  "competitie. Eten twee vogelsoorten insecten in dezelfde bomen, maar de ene in de kruin en "
                  "de andere op de stam, dan <strong>blijft de competitie door het verschil in zoekplaats "
                  "beperkt</strong>."),
            ("p", "Stijgt het aantal prooien sterk, dan <strong>nemen de roofdieren met wat vertraging ook "
                  "toe, waarna de prooien weer dalen</strong>. Verdwijnt een roofdier uit een gebied, dan "
                  "<strong>groeit de prooipopulatie en vreet die haar voedselplanten kaal</strong>: het "
                  "effect werkt door tot ver in het ecosysteem."),
        ]),
        dict(kop="Leven in een groep", blokken=[
            ("p", "Voordelen van een groep: <strong>meer ogen zien een roofdier sneller aankomen</strong>, "
                  "<strong>samen jagen levert grotere prooien op</strong> en de "
                  "<strong>jongen kunnen samen beschermd worden</strong>."),
            ("p", "Nadelen: er is <strong>meer competitie om voedsel en ziekten verspreiden zich "
                  "sneller</strong>, en een grote groep is opvallender voor een roofdier. Daarom is er altijd "
                  "een evenwicht tussen voor- en nadeel."),
            ("p", "Een <strong>hiërarchie</strong> of rangorde is de ordening waarbij het ene dier voorrang "
                  "heeft op het andere. Dat <strong>spaart gevechten uit</strong>, want de uitkomst is al "
                  "bekend."),
            ("p", "Een dier verdedigt een <strong>territorium</strong> <strong>om voedsel, dekking en een "
                  "nestplaats te houden</strong> voor zichzelf en zijn jongen. Door het af te bakenen met "
                  "zang of geur hoeft het niet telkens te vechten."),
            ("p", "<strong>Communicatie</strong> tussen dieren kan <strong>met geluid, met geur en met "
                  "beweging</strong>. Een <strong>feromoon</strong> is een "
                  "<strong>geurstof waarmee soortgenoten elkaar iets doorgeven</strong>: mieren leggen er een "
                  "spoor mee en motten vinden er een partner mee."),
        ]),
    ],
    onthoud=[
        "Gedrag is alles wat een dier doet als antwoord op prikkels van binnen of van buiten.",
        "Aangeboren gedrag ligt vast en werkt meteen; geleerd gedrag past zich aan maar wordt niet erfelijk doorgegeven.",
        "Vormen van leren: gewenning, conditionering, nadoen en inprenting.",
        "Een sleutelprikkel zet een vast gedragspatroon in gang.",
        "Predatie: de een doodt de ander. Competitie: beide nadeel. Symbiose: beide voordeel.",
        "Een parasiet schaadt zonder te doden; bij commensalisme wint de een en merkt de ander niets.",
        "Soorten met dezelfde niche kunnen niet blijvend naast elkaar bestaan; een verschil in zoekplaats maakt dat wel mogelijk.",
        "Een groep geeft veiligheid en samen jagen, maar ook competitie en ziekte.",
        "Een hiërarchie en een territorium sparen gevechten uit.",
    ],
)

# ───────────────────────── 9. Materie- en energiestromen in een ecosysteem
BUNDELS["materie-en-energiestromen-in-een-ecosysteem-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Materie- en energiestromen in een ecosysteem",
    onder="Autotroof en heterotroof, fotosynthese en celademhaling, gisting en enzymen, voedselketens en de energiepiramide.",
    secties=[
        dict(kop="Autotroof en heterotroof", blokken=[
            ("p", "Een <strong>autotroof</strong> organisme <strong>maakt zijn eigen organische "
                  "stoffen</strong>; een <strong>heterotroof</strong> moet ze opnemen. Autotroof betekent "
                  "zelfvoedend: groene planten bouwen hun eigen glucose, dieren en schimmels halen die uit "
                  "hun voedsel."),
            ("p", "De energiebron van een groene plant is het <strong>zonlicht</strong>. Bij de fotosynthese "
                  "vangt het chlorofyl die lichtenergie op, en ze komt in de glucose terecht als chemische "
                  "energie."),
        ]),
        dict(kop="Fotosynthese en celademhaling", blokken=[
            ("p", "De <strong>grondstoffen van de fotosynthese</strong> zijn "
                  "<strong>koolstofdioxide en water</strong>. De plant haalt koolstofdioxide uit de lucht en "
                  "water uit de bodem, en bouwt daar met lichtenergie glucose van. Daarbij "
                  "<strong>komt zuurstofgas vrij</strong>, van het gesplitste water."),
            ("p", "De <strong>celademhaling</strong> levert <strong>energie voor de cel, plus "
                  "koolstofdioxide en water</strong>: glucose wordt met zuurstofgas afgebroken. Dat gebeurt "
                  "in het <strong>mitochondrion</strong>, het celorganel dat de energiecentrale van de cel is."),
            ("p", "De <strong>producten van het ene zijn de grondstoffen van het andere</strong>; de "
                  "<strong>fotosynthese slaat energie op en de celademhaling maakt ze vrij</strong>; en een "
                  "<strong>plantencel doet beide</strong>. Een dierlijke cel doet enkel celademhaling."),
            ("p", "Een <strong>plant doet dus wél celademhaling</strong>, ook zij heeft energie nodig. Bij "
                  "daglicht geeft ze netto zuurstofgas af en in het donker netto koolstofdioxide, want "
                  "<strong>bij licht overheerst de fotosynthese en in het donker valt ze weg</strong>."),
            ("p", "Zet je een <strong>waterplant in een buisje in het licht</strong> en meet je de "
                  "gasbelletjes, dan meet je het <strong>zuurstofgas dat bij de fotosynthese "
                  "vrijkomt</strong>. Verdubbel je de lichtsterkte en stijgt het aantal belletjes niet "
                  "verder, dan is een <strong>andere factor, zoals het koolstofdioxide, nu de beperkende "
                  "factor</strong>: het proces loopt maar zo snel als zijn krapste grondstof toelaat."),
        ]),
        dict(kop="Gisting, stofwisseling en enzymen", blokken=[
            ("p", "<strong>Gisting</strong> is de <strong>afbraak van glucose zonder zuurstofgas</strong>. "
                  "De glucose wordt maar gedeeltelijk afgebroken, dus levert gisting "
                  "<strong>per molecule veel minder energie</strong> op dan de celademhaling: er blijft nog "
                  "energie in de ethanol of het melkzuur zitten."),
            ("p", "<strong>Alcoholgisting</strong> door gist levert <strong>ethanol en "
                  "koolstofdioxide</strong> op. Daarom gebruikt men gist voor bier, wijn en brood."),
            ("p", "Bij een <strong>zware sprint</strong> <strong>schakelen de spieren bij zuurstofgebrek over "
                  "op melkzuurgisting</strong>, en dat melkzuur voelt branderig."),
            ("p", "De <strong>stofwisseling</strong> of het metabolisme is het "
                  "<strong>geheel van alle chemische omzettingen in een organisme</strong>, zowel het "
                  "opbouwen als het afbreken van stoffen."),
            ("p", "<strong>Koolhydraten</strong>, <strong>vetten</strong> en <strong>proteïnen</strong> in "
                  "ons voedsel leveren energie; mineralen en vitaminen zijn nodig maar leveren er geen. "
                  "<strong>Vetten leveren per gram meer energie dan koolhydraten</strong>, en daarom slaat "
                  "het lichaam zijn reserve vooral als vet op."),
            ("p", "Een <strong>enzym</strong> <strong>versnelt een bepaalde omzetting zonder er zelf bij op "
                  "te gaan</strong>; het is een biokatalysator die op één bepaalde stof past. Het werkt "
                  "<strong>het best binnen een nauw gebied van temperatuur en zuurtegraad</strong>; buiten "
                  "dat gebied verliest het zijn vorm."),
        ]),
        dict(kop="Voedselketens en voedselwebben", blokken=[
            ("p", "In een ecosysteem onderscheidt men <strong>producenten</strong>, "
                  "<strong>consumenten</strong> en <strong>reducenten</strong>. "
                  "<strong>Producenten</strong> maken zelf organische stof met licht: gras, algen, een eik. "
                  "Een schimmel kan dat niet en is dus een <strong>reducent</strong>: die "
                  "<strong>breekt dood organisch materiaal af</strong>."),
            ("p", "Een <strong>voedselketen</strong> is een <strong>rij organismen waarin elk het volgende "
                  "tot voedsel dient</strong>. De <strong>pijl wijst van het gegeten organisme naar wie het "
                  "eet</strong>, want hij volgt de stroom van stof en energie: gras, pijl, koe, pijl, mens."),
            ("p", "Een <strong>voedselweb</strong> geeft de werkelijkheid beter weer, want de "
                  "<strong>meeste dieren eten meer dan één soort</strong> en worden ook door meer dan één "
                  "soort gegeten. Een keten is één draad uit het web."),
            ("p", "Het <strong>trofisch niveau</strong> of voedselniveau is de plaats van een organisme in de keten: "
                  "producent, eerste consument, en zo verder. Een <strong>herbivoor</strong> voedt zich met "
                  "plantaardig materiaal en staat op het eerste consumentenniveau."),
        ]),
        dict(kop="De energiepiramide", blokken=[
            ("p", "Een <strong>energiepiramide</strong> wordt naar boven toe smaller, want "
                  "<strong>bij elke stap gaat het meeste verloren als warmte</strong> en voor de eigen "
                  "levensbehoeften. <strong>Ongeveer een tiende</strong> van de energie van een niveau komt "
                  "in het volgende terecht."),
            ("p", "Daarom zijn er <strong>zelden meer dan vier of vijf trofische niveaus</strong>: "
                  "<strong>na elke stap blijft er te weinig energie over</strong> voor een extra niveau."),
            ("p", "<strong>Materie gaat rond in kringlopen, energie stroomt er maar één keer door</strong>. "
                  "Koolstof en stikstof worden eindeloos hergebruikt, maar de zonne-energie verlaat het "
                  "ecosysteem als warmte en komt niet terug. Daarom heeft een ecosysteem "
                  "<strong>voortdurend nieuwe energie van buiten nodig</strong>."),
            ("p", "Een stuk land voedt meer mensen met graan dan met vlees, want "
                  "<strong>van graan naar vlees gaat veel energie verloren</strong>: eet je het graan zelf, "
                  "dan sla je een trofisch niveau over."),
            ("p", "Sommige <strong>giftige stoffen hopen zich op naar de top van een voedselketen toe</strong>: "
                  "een stof die het lichaam niet afbreekt, blijft bij elke stap achter in het vet."),
            ("p", "<strong>Biomassa</strong> is de <strong>totale massa levend materiaal in een gebied of op "
                  "een niveau</strong>; naar de top van de piramide neemt ze sterk af."),
            ("p", "Verdwijnen alle <strong>waterplanten uit een vijver</strong>, dan "
                  "<strong>vallen de producenten weg, en de consumenten erbij</strong>: zij zijn de ingang "
                  "van alle energie. En <strong>zonder reducenten</strong> zou een ecosysteem "
                  "<strong>niet blijven werken</strong>, hoeveel licht er ook valt: de mineralen bleven in "
                  "dood materiaal opgesloten."),
            ("p", "Een perceel met <strong>een mengsel van gewassen</strong> geeft "
                  "<strong>meer verschillende plantenresten, dus een rijker bodemleven</strong> dan een "
                  "perceel met alleen maïs."),
        ]),
    ],
    onthoud=[
        "Autotroof maakt zijn eigen organische stof, heterotroof moet ze opnemen.",
        "Fotosynthese slaat energie op in glucose, celademhaling maakt ze weer vrij in het mitochondrion.",
        "Een plant doet beide; een dierlijke cel enkel celademhaling.",
        "Gisting is afbraak zonder zuurstofgas en levert veel minder energie op.",
        "Een enzym versnelt één omzetting en werkt enkel binnen een nauw gebied van temperatuur en zuurtegraad.",
        "Producenten maken, consumenten eten, reducenten breken af; de pijl in een keten volgt de energie.",
        "Van elk niveau komt ongeveer een tiende in het volgende terecht, dus zijn er maar vier of vijf niveaus.",
        "Materie gaat rond in kringlopen, energie stroomt er één keer door en verdwijnt als warmte.",
    ],
)

# ───────────────────────── 10. Kringlopen, voedselrelaties en de mens
BUNDELS["kringlopen-voedselrelaties-en-de-mens-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Kringlopen, voedselrelaties en de mens",
    onder="De kringlopen van koolstof, water, stikstof en fosfor, het ecosysteem als geheel, de successie en de voetafdruk van de mens.",
    secties=[
        dict(kop="De koolstofkringloop", blokken=[
            ("p", "Dat koolstof een <strong>kringloop</strong> doorloopt, betekent dat "
                  "<strong>dezelfde koolstofatomen telkens hergebruikt worden</strong> in andere stoffen. "
                  "Materie verdwijnt niet: een atoom zit vandaag in de lucht, morgen in een blad."),
            ("p", "De grote stromen zijn: de <strong>fotosynthese haalt koolstofdioxide uit de "
                  "lucht</strong>, de <strong>celademhaling geeft koolstofdioxide af</strong>, en het "
                  "<strong>verbranden van steenkool en aardolie geeft koolstofdioxide af</strong>. Alleen de "
                  "fotosynthese brengt koolstof uit de lucht het leven in."),
            ("p", "<strong>Steenkool en aardolie zijn ontstaan uit resten van organismen van lang "
                  "geleden</strong>. Die koolstof zat miljoenen jaren opgesloten in de bodem."),
            ("p", "Het koolstofdioxidegehalte van de lucht stijgt omdat we "
                  "<strong>fossiele brandstoffen te snel verbranden</strong>: we voegen koolstof toe aan een "
                  "kring die ze niet zo snel kwijtraakt."),
            ("p", "Een <strong>groeiend bos legt koolstof vast</strong>: het hout dat erbij komt, is "
                  "opgeslagen koolstof. Wordt het gekapt en verbrand, dan komt die weer vrij."),
            ("p", "De mens grijpt in de kringloop in door "
                  "<strong>fossiele brandstoffen te verbranden</strong>, "
                  "<strong>bossen te kappen</strong> en <strong>veengebieden te draineren</strong>. Ploeg je "
                  "<strong>oud grasland om tot akker</strong>, dan "
                  "<strong>oxideert een deel van de bodemkoolstof en komt het als koolstofdioxide "
                  "vrij</strong>: ploegen brengt lucht bij de organische stof."),
        ]),
        dict(kop="De waterkringloop", blokken=[
            ("p", "De waterkringloop bestaat uit <strong>verdamping uit zeeën, meren en planten</strong>, "
                  "<strong>condensatie tot wolken</strong> en <strong>neerslag als regen of sneeuw</strong>. "
                  "Water verbrandt niet; het is zelf al een eindproduct van verbranding."),
            ("p", "Het verdampen van water via de bladeren van planten heet "
                  "<strong>transpiratie</strong>. In een bos gaat een groot deel van de neerslag zo terug de "
                  "lucht in."),
            ("p", "Bij een hevige regen staat er sneller water op een <strong>verharde straat</strong> dan "
                  "op een weide, want het <strong>water kan niet in de bodem dringen en loopt meteen "
                  "oppervlakkig weg</strong>. Een bodem met planten neemt water op en geeft het traag door."),
        ]),
        dict(kop="Stikstof en fosfor", blokken=[
            ("p", "Planten kunnen het <strong>stikstofgas uit de lucht niet rechtstreeks gebruiken</strong>, "
                  "want de <strong>binding in het stikstofgasmolecule is te sterk</strong>. Ze nemen stikstof "
                  "op als <strong>nitraat</strong> of ammonium uit de bodem."),
            ("p", "<strong>Bacteriën</strong> maken stikstofgas voor planten bruikbaar. Ze leven vrij in de "
                  "bodem of in <strong>knolletjes op de wortels van vlinderbloemigen</strong>: "
                  "<strong>klaver en bonen</strong> verrijken daardoor de bodem, en boeren zaaien ze als "
                  "groenbedekker."),
            ("p", "Planten nemen als mineraal onder andere <strong>nitraat</strong>, "
                  "<strong>fosfaat</strong> en <strong>kalium</strong> uit de bodem op. Glucose maakt de "
                  "plant zelf."),
            ("p", "Te veel stikstof in de natuur is een probleem omdat "
                  "<strong>snelgroeiende soorten de rest verdringen</strong>: brandnetel en gras varen er wel "
                  "bij, heide en veel bloemen niet."),
            ("p", "<strong>Eutrofiëring</strong> van een vijver: "
                  "<strong>overbemesting laat de algen woekeren en de zuurstof instorten</strong>. Een "
                  "algenlaag houdt het licht weg, de waterplanten sterven, de reducenten gebruiken de "
                  "zuurstof op, en dan <strong>sterven de vissen door een gebrek aan zuurstofgas</strong>."),
            ("p", "De <strong>kringloop van fosfor verloopt veel langzamer</strong> dan die van koolstof, "
                  "want <strong>fosfor heeft geen gasvorm in de lucht</strong>: het zit in gesteente en bodem "
                  "en komt traag vrij."),
            ("p", "Een <strong>gesloten kringloop op een boerderij</strong>, met mest van het eigen vee op "
                  "de eigen akkers, is gunstig omdat de <strong>mineralen op het bedrijf zelf blijven</strong> "
                  "en er minder aanvoer van buiten nodig is."),
        ]),
        dict(kop="Het ecosysteem als geheel", blokken=[
            ("p", "Een <strong>ecosysteem</strong> is <strong>alle organismen samen met hun "
                  "omgeving</strong>, dus ook de bodem, het water, het licht en het klimaat. Juist de "
                  "wisselwerking maakt het een systeem."),
            ("p", "<strong>Abiotische</strong> factoren zijn niet-levend: de <strong>temperatuur</strong>, de "
                  "<strong>zuurtegraad van de bodem</strong>, de <strong>lichtsterkte</strong>. Het aantal "
                  "roofdieren is een biotische factor."),
            ("p", "Een <strong>populatie</strong> zijn <strong>alle individuen van één soort die in "
                  "hetzelfde gebied leven</strong>. Alle populaties samen vormen de levensgemeenschap."),
            ("p", "De <strong>draagkracht</strong> is het <strong>aantal individuen dat een gebied blijvend "
                  "kan onderhouden</strong>. Een populatie die erboven uitgroeit, "
                  "<strong>daalt daarna weer</strong>: het voedsel raakt op en ziekten slaan toe."),
            ("p", "Of een populatie groeit of krimpt, hangt af van het "
                  "<strong>aantal geboorten</strong>, het <strong>aantal sterfgevallen</strong> en het "
                  "<strong>aantal dieren dat het gebied binnenkomt of verlaat</strong>."),
            ("p", "De <strong>ecologische niche</strong> is het <strong>geheel van omstandigheden en rollen "
                  "waarin een soort kan leven</strong>: niet enkel waar ze woont, maar ook wat ze eet, "
                  "wanneer ze actief is en wat ze verdraagt. <strong>Twee soorten met precies dezelfde niche "
                  "kunnen niet blijvend naast elkaar bestaan</strong>."),
            ("p", "Een <strong>indicatorsoort</strong> is een <strong>soort waarvan de aanwezigheid iets "
                  "zegt over de toestand van het milieu</strong>: korstmossen verdragen weinig "
                  "luchtvervuiling, kokerjuffers weinig watervervuiling. Wil je weten of een beek vervuild "
                  "is, dan is het verstandigst de <strong>waterdiertjes te bepalen en te vergelijken</strong> "
                  "met een lijst van indicatorsoorten: die vertellen over de maanden ervoor, niet enkel over "
                  "het ogenblik van de meting."),
        ]),
        dict(kop="Successie en beheer", blokken=[
            ("p", "<strong>Successie</strong> is het <strong>geleidelijk veranderen van een "
                  "levensgemeenschap</strong>: eerst pioniers op de kale bodem, dan grassen, dan struiken en "
                  "ten slotte bomen. Elke stap maakt de volgende mogelijk."),
            ("p", "<strong>Pioniersplanten</strong> groeien op kale bodem omdat ze "
                  "<strong>weinig voeding en veel licht verdragen</strong>; hun afgestorven resten vormen de "
                  "eerste humus."),
            ("p", "Een ecosysteem in een <strong>late fase van de successie is meestal stabieler</strong> dan "
                  "een jong ecosysteem: er zijn meer soorten en meer verbindingen in het voedselweb."),
            ("p", "Een <strong>natuurbeheerder die een heide wil behouden, moet er soms bomen "
                  "weghalen</strong>: zonder ingrijpen zet de successie door en wordt de heide bos."),
            ("p", "Laat een gemeente een <strong>beek weer kronkelen</strong> in plaats van recht door een "
                  "buis, dan <strong>houdt de beek meer water vast en meer leven</strong>: bochten, ondiepe "
                  "oevers en overstroombare weides geven leven een plaats en houden water op bij hevige regen."),
        ]),
        dict(kop="De voetafdruk van de mens", blokken=[
            ("p", "De <strong>ecologische voetafdruk</strong> is de maat voor het beslag dat iemands manier "
                  "van leven op de aarde legt: voeding, wonen, verplaatsen en spullen omgerekend naar "
                  "oppervlakte."),
            ("p", "Je verkleint haar door <strong>minder vlees te eten</strong>, "
                  "<strong>minder met het vliegtuig te reizen</strong> en "
                  "<strong>spullen langer te gebruiken en te herstellen</strong>. Een "
                  "<strong>plantaardig dieet heeft gemiddeld een kleinere voetafdruk</strong>, want vlees "
                  "komt een trofisch niveau hoger."),
            ("p", "Het beperken van de klimaatverandering is ook een zaak van biodiversiteit, want "
                  "<strong>soorten kunnen niet altijd meeverhuizen</strong> als hun klimaat verschuift. Een "
                  "soort op een bergtop of in een versnipperd landschap kan niet opschuiven."),
            ("p", "Verdwijnen de <strong>bijen</strong> uit een gebied, dan nemen de "
                  "<strong>planten die insecten nodig hebben, af</strong>: hun zaadzetting daalt en daarna "
                  "hun aantal."),
        ]),
    ],
    onthoud=[
        "Een kringloop betekent dat dezelfde atomen telkens hergebruikt worden; materie verdwijnt niet.",
        "Fotosynthese haalt koolstof uit de lucht, celademhaling en verbranding brengen ze terug.",
        "De waterkringloop is verdampen, condenseren en neerslaan; planten verdampen mee door transpiratie.",
        "Stikstofgas is te sterk gebonden voor planten; bacteriën maken er nitraat of ammonium van.",
        "Eutrofiëring: te veel mest, algen woekeren, de zuurstof stort in en de vissen sterven.",
        "Een populatie is één soort op één plaats; de draagkracht is wat een gebied blijvend kan onderhouden.",
        "Twee soorten met dezelfde niche kunnen niet blijvend naast elkaar bestaan.",
        "Successie gaat van pioniers naar bos; een late fase is stabieler, en beheer houdt een heide met opzet jong.",
        "De voetafdruk daalt vooral door minder vlees, minder vliegen en spullen langer gebruiken.",
    ],
)

# ───────────────────────── 11. Levensreddend handelen
BUNDELS["levensreddend-handelen-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Levensreddend handelen",
    onder="De eerste stappen bij een slachtoffer, reanimatie en de AED, en de andere noodsituaties.",
    secties=[
        dict(kop="De eerste stappen", blokken=[
            ("p", "Bij een ongeval doe je als eerste dit: <strong>kijken of de plaats veilig is</strong>, "
                  "voor jezelf en voor het slachtoffer. Een tweede slachtoffer helpt niemand. Zie je een "
                  "<strong>ongeval op de autosnelweg</strong>, dan zorg je dus eerst voor je "
                  "<strong>eigen veiligheid</strong>: stilstaan op een veilige plek, een hesje aan, de "
                  "knipperlichten aan."),
            ("p", "Het noodnummer voor een ziekenwagen is <strong>112</strong>, het Europese noodnummer voor "
                  "ziekenwagen en brandweer. Voor de politie alleen bestaat ook 101."),
            ("p", "Bij dat telefoontje vertel je <strong>waar je precies bent</strong>, "
                  "<strong>wat er gebeurd is</strong> en <strong>hoeveel slachtoffers er zijn en in welke "
                  "toestand</strong>. Wie schuld heeft, doet dan niet toe."),
            ("p", "Of iemand bij bewustzijn is, ga je na doordat je de "
                  "<strong>persoon aanspreekt en zacht aan de schouders schudt</strong>. Reageert er niets, "
                  "dan <strong>kijk je of het slachtoffer normaal ademt</strong>: hoofd lichtjes achterover, "
                  "naar de borstkas kijken en voelen of je adem op je wang voelt, tien seconden lang."),
            ("p", "Is iemand <strong>niet bij bewustzijn maar ademt hij normaal</strong>, dan "
                  "<strong>leg je de persoon in stabiele zijligging en bel je 112</strong>. In "
                  "<strong>stabiele zijligging</strong> ligt het slachtoffer op de zij met het hoofd lichtjes "
                  "achterover en de mond naar beneden, want <strong>op de rug kan de tong of braaksel de "
                  "luchtweg afsluiten</strong>."),
        ]),
        dict(kop="Reanimatie", blokken=[
            ("p", "Je start met reanimeren <strong>als het slachtoffer niet reageert en niet normaal "
                  "ademt</strong>. Dan stuwt het hart het bloed niet meer rond."),
            ("p", "Het ritme bij een volwassene is telkens <strong>30 borstcompressies en 2 "
                  "beademingen</strong>, met <strong>ongeveer 100 tot 120 compressies per minuut</strong>, "
                  "ongeveer twee per seconde."),
            ("p", "Je legt de hiel van je hand <strong>midden op het borstbeen</strong>, je andere hand "
                  "erbovenop, en duwt met gestrekte armen recht naar beneden, "
                  "<strong>ongeveer vijf centimeter diep</strong>. Daarna laat je de borstkas volledig "
                  "terugkomen."),
            ("p", "Je <strong>onderbreekt de hartmassage zo weinig mogelijk</strong>, want elke "
                  "onderbreking laat de bloeddruk wegzakken. Je gaat door tot de hulpdiensten er zijn of tot "
                  "het slachtoffer weer normaal ademt. <strong>Begint het weer normaal te ademen, dan leg je "
                  "het in stabiele zijligging</strong>."),
            ("p", "Sta je er <strong>alleen voor</strong>, dan <strong>bel je 112 met de luidspreker aan en "
                  "begin je te reanimeren</strong>: alarm en reanimatie moeten samengaan."),
            ("p", "<strong>Reanimeren verhoogt de kans om een hartstilstand te overleven aanzienlijk</strong>. "
                  "Elke minuut zonder hulp verkleint die kans sterk, dus beginnen is altijd beter dan "
                  "wachten, ook als je het niet perfect doet."),
        ]),
        dict(kop="De AED", blokken=[
            ("p", "<strong>AED</strong> staat voor <strong>automatische externe defibrillator</strong>. Het "
                  "toestel <strong>meet het hartritme en geeft enkel een schok als dat nodig is</strong>; het "
                  "beslist dus zelf."),
            ("p", "<strong>Iemand zonder opleiding mag een AED gebruiken.</strong> Het toestel spreekt je "
                  "stap voor stap toe, en hem niet gebruiken is het grootste risico."),
            ("p", "Bij het gebruik hoort: het <strong>toestel aanzetten en de aanwijzingen volgen</strong>, "
                  "de <strong>elektroden op de ontblote borstkas kleven</strong> en "
                  "<strong>niemand aanraken op het ogenblik van de schok</strong>. De hartmassage gaat door "
                  "tot het toestel vraagt om los te laten."),
        ]),
        dict(kop="Bloedingen, brandwonden en verstikking", blokken=[
            ("p", "Bij een <strong>hevige bloeding</strong> <strong>druk je met een propere doek stevig op "
                  "de wonde</strong>. Een afbindend verband wordt niet meer aangeraden. Je houdt het "
                  "gekwetste lichaamsdeel bij voorkeur <strong>hoger dan het hart</strong>."),
            ("p", "Een <strong>brandwond</strong> koel je <strong>20 minuten met lauw stromend "
                  "water</strong>: water eerst, de rest komt later. Je doet er "
                  "<strong>geen boter, tandpasta of zalf</strong> op, want vette stoffen houden de warmte "
                  "vast. Een <strong>blaar prik je niet open</strong>: die is een steriel dekseltje over de "
                  "wonde."),
            ("p", "Verslikt iemand zich en kan hij nog <strong>krachtig hoesten</strong>, dan "
                  "<strong>laat je hem doorhoesten en blijf je erbij</strong>. Lukt het hoesten niet meer, "
                  "dan geef je <strong>vijf slagen tussen de schouderbladen en daarna vijf "
                  "buikstoten</strong>, afwisselend tot het voorwerp eruit komt. Raakt de persoon buiten "
                  "bewustzijn, dan start je met reanimeren."),
        ]),
        dict(kop="Shock, breuken en andere noodsituaties", blokken=[
            ("p", "Tekens van <strong>shock</strong>: een <strong>bleke, klamme huid</strong>, een "
                  "<strong>snelle en zwakke pols</strong> en <strong>onrust, dorst of verwardheid</strong>. "
                  "De ademhaling wordt snel en oppervlakkig. Je <strong>geeft niets te drinken</strong>, "
                  "houdt het slachtoffer warm en belt 112."),
            ("p", "Bij een vermoedelijke <strong>botbreuk</strong> <strong>laat je de arm zo liggen als hij "
                  "ligt, steun je hem en bel je hulp</strong>. Rechttrekken kan zenuwen en bloedvaten "
                  "beschadigen. Bij een vermoeden van een <strong>nek- of rugwonde laat je het slachtoffer "
                  "liggen zoals het ligt, tenzij er onmiddellijk gevaar is</strong>, want verplaatsen kan het "
                  "ruggemerg beschadigen."),
            ("p", "Bij een <strong>epileptische aanval</strong> <strong>zorg je dat de persoon zich niet kan "
                  "stoten en leg je iets zachts onder het hoofd</strong>. Je houdt hem niet vast en steekt "
                  "niets tussen de tanden. Na de aanval leg je hem in zijligging."),
            ("p", "Bij een <strong>hittestuwing of hitteslag</strong> koel je de huid met "
                  "<strong>lauw water</strong> en niet met ijs: ijs trekt de bloedvaten samen en dan kan de "
                  "warmte er niet meer uit."),
            ("p", "Klaagt iemand over <strong>drukkende pijn in de borst die naar de arm uitstraalt</strong>, "
                  "dan <strong>bel je 112, laat je de persoon stil zitten en blijf je erbij</strong>. Dat kan "
                  "een hartinfarct zijn."),
            ("p", "In een eenvoudige <strong>verbanddoos</strong> horen <strong>steriele compressen</strong>, "
                  "een <strong>rol kleefpleister en een zwachtel</strong> en "
                  "<strong>wegwerphandschoenen</strong>. Een wonde spoel je met water, niet met alcohol. "
                  "Handschoenen <strong>beschermen zowel de helper als het slachtoffer</strong>."),
            ("p", "Het is nuttig dat zoveel mensen mogelijk kunnen reanimeren, want de "
                  "<strong>eerste minuten bepalen de kans om te overleven, en de hulpdiensten zijn er niet "
                  "meteen</strong>. Een omstaander overbrugt net die minuten."),
        ]),
    ],
    onthoud=[
        "Eerst veiligheid, dan aanspreken en schudden, dan kijken of het slachtoffer normaal ademt.",
        "Bewusteloos maar normale ademhaling: stabiele zijligging en 112.",
        "Niet reageren en niet normaal ademen: reanimeren, 30 compressies en 2 beademingen.",
        "100 tot 120 compressies per minuut, midden op het borstbeen, ongeveer vijf centimeter diep.",
        "Een AED geeft enkel een schok als het nodig is, en iedereen mag hem gebruiken.",
        "Bloeding: stevig op de wonde drukken en het lichaamsdeel hoger dan het hart houden.",
        "Brandwond: 20 minuten lauw stromend water, geen boter of zalf, en de blaar niet openprikken.",
        "Verstikking: laten hoesten; lukt dat niet, vijf slagen tussen de schouderbladen en vijf buikstoten.",
        "Shock of een vermoeden van nek- of rugwonde: niets te drinken geven, niet verplaatsen, 112 bellen.",
    ],
)

# ───────────────────────── 12. Wetenschappelijk onderzoek en STEM
BUNDELS["wetenschappelijk-onderzoek-en-stem-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Wetenschappelijk onderzoek en STEM",
    onder="De onderzoekscyclus, variabelen en controlegroep, de microscoop en het preparaat, veilig werken, tabellen en grafieken.",
    secties=[
        dict(kop="Van vraag tot besluit", blokken=[
            ("p", "Een goede <strong>onderzoeksvraag</strong> is een "
                  "<strong>vraag die je met een meting kan beantwoorden</strong>. Of iets mooi is, kan je "
                  "niet meten; hoeveel iets groeit, wel."),
            ("p", "Een <strong>hypothese</strong> is een <strong>beredeneerde verwachting die je kan "
                  "toetsen</strong>, en dus ook kan weerleggen. Dat ze onderuit gehaald kan worden, is net "
                  "haar kracht: een <strong>weerlegde hypothese is een resultaat</strong>, geen mislukking."),
            ("p", "Het verschil tussen een <strong>waarneming</strong> en een "
                  "<strong>gevolgtrekking</strong>: een <strong>waarneming is wat je vaststelt, een "
                  "gevolgtrekking wat je besluit</strong>. Het blad is geel is een waarneming; de plant krijgt "
                  "te weinig water is een gevolgtrekking, en die kan fout zijn."),
            ("p", "De <strong>meetresultaten</strong> noteer je meteen en onbewerkt, in een tabel met de "
                  "eenheden erbij. Pas daarna ga je rekenen en tekenen. Een onderzoeker die zijn "
                  "<strong>metingen aanpast omdat ze niet bij zijn hypothese passen, pleegt "
                  "wetenschappelijke fraude</strong>."),
            ("p", "In een <strong>verslag</strong> horen de <strong>onderzoeksvraag en de hypothese</strong>, "
                  "de <strong>werkwijze en het materiaal</strong>, en de "
                  "<strong>resultaten en het besluit</strong>. Een werkwijze is goed beschreven als "
                  "<strong>iemand anders je proef ermee kan overdoen</strong>; daarom horen hoeveelheden, "
                  "tijden en toestellen er precies in."),
        ]),
        dict(kop="Variabelen en controlegroep", blokken=[
            ("p", "De <strong>onafhankelijke variabele</strong> is de factor die je "
                  "<strong>bewust verandert</strong>, bijvoorbeeld de lichtsterkte. De "
                  "<strong>afhankelijke variabele</strong> is wat je meet: de lengte van de plant na enkele "
                  "weken."),
            ("p", "Alles behalve de variabele die je onderzoekt, houd je <strong>constant</strong>: de "
                  "<strong>hoeveelheid water</strong>, de <strong>soort potgrond</strong>, de "
                  "<strong>temperatuur</strong>. Anders weet je niet waar een verschil van komt."),
            ("p", "De <strong>controlegroep</strong> is de groep die <strong>de behandeling niet krijgt, "
                  "zodat je kan vergelijken</strong>. Zonder controlegroep "
                  "<strong>laat een proef geen betrouwbaar besluit toe</strong>: je weet niet wat er zonder "
                  "behandeling gebeurd zou zijn."),
            ("p", "Je <strong>herhaalt een meting</strong> om de <strong>invloed van toeval en meetfouten te "
                  "verkleinen</strong>, en je gebruikt <strong>meerdere planten per groep</strong> omdat "
                  "<strong>individuen verschillen en dat verschil met meer exemplaren wegvalt</strong>. Een "
                  "proef met twee planten laat dus geen besluit toe: "
                  "<strong>twee planten zijn te weinig om toeval uit te sluiten</strong>."),
            ("p", "Verandert er <strong>meer dan één ding tegelijk</strong>, bijvoorbeeld omdat de ene groep "
                  "ook warmer stond, dan <strong>weet je de oorzaak niet</strong>. Dat heet een "
                  "<strong>storende variabele</strong>. En een <strong>verband</strong> is nog "
                  "<strong>geen bewijs van oorzaak en gevolg</strong>: twee dingen kunnen samen veranderen "
                  "door een derde oorzaak."),
            ("p", "Komen <strong>twee groepen in de klas tot een ander besluit</strong>, dan "
                  "<strong>leg je de twee werkwijzen naast elkaar en zoek je waar ze verschilden</strong>."),
        ]),
        dict(kop="De microscoop", blokken=[
            ("p", "Met een <strong>lichtmicroscoop</strong> bekijk je "
                  "<strong>cellen en hun grootste celonderdelen</strong>. Voor virussen en moleculen is een "
                  "elektronenmicroscoop nodig."),
            ("p", "De <strong>totale vergroting</strong> is de <strong>vergroting van het oculair maal die "
                  "van het objectief</strong>. Een oculair van 10 keer met een objectief van 40 keer geeft "
                  "dus <strong>400</strong> keer."),
            ("p", "Je begint met het <strong>zwakste objectief</strong>, want dan is het "
                  "<strong>beeldveld het grootst en vind je je voorwerp makkelijker</strong>. "
                  "<strong>Hoe sterker de vergroting, hoe kleiner het stukje preparaat dat je ziet</strong>: "
                  "vergroting en beeldveld gaan tegen elkaar in."),
            ("p", "Een <strong>dekglaasje</strong> dient om het <strong>preparaat vlak te houden en "
                  "uitdrogen te voorkomen</strong>; het drukt het preparaat tot één laagje, zodat er maar "
                  "één scherptevlak is. Een <strong>kleurstof</strong> zoals methyleenblauw of jood geeft "
                  "<strong>contrast</strong>, want veel celonderdelen zijn doorzichtig."),
            ("p", "Zit er een <strong>luchtbel</strong> in je preparaat, dan bekijk je het best opnieuw: zo'n "
                  "bel is rond met een scherpe donkere rand en <strong>lijkt op een cel</strong>."),
        ]),
        dict(kop="Veilig werken", blokken=[
            ("p", "In een labo geldt: <strong>een bril en handschoenen dragen waar nodig</strong>, "
                  "<strong>niet eten of drinken</strong>, en <strong>lange haren vastmaken bij het werken met "
                  "een vlam</strong>. Op eigen initiatief stoffen mengen hoort nooit bij een proef."),
            ("p", "Een stof die je <strong>niet kan benoemen, laat je staan en je meldt het aan de "
                  "leraar</strong>. Ze kan bijtend of brandbaar zijn; je ruikt er niet aan."),
        ]),
        dict(kop="Gegevens weergeven en beoordelen", blokken=[
            ("p", "Op de <strong>horizontale as</strong> van een grafiek komt de "
                  "<strong>onafhankelijke variabele</strong>, die je zelf instelde; op de verticale as wat je "
                  "gemeten hebt. Bij elke as horen de <strong>naam van de grootheid</strong>, de "
                  "<strong>eenheid</strong> en een <strong>schaal met getallen</strong>."),
            ("p", "Een <strong>staafdiagram past bij losse categorieën</strong> en een "
                  "<strong>lijndiagram bij een grootheid die vloeiend verandert</strong>. Soorten vogels zijn "
                  "categorieën, een stijgende temperatuur is vloeiend."),
            ("p", "Een <strong>uitschieter</strong> is een meetpunt dat sterk van de rest afwijkt. Dat kan "
                  "een meetfout zijn of iets echt bijzonders: je laat hem staan en je zegt erbij dat hij er "
                  "is."),
            ("p", "Noteer je een lengte als <strong>4</strong>, dan <strong>ontbreekt de eenheid bij het "
                  "getal</strong> en betekent het niets. Een <strong>gemiddelde zegt meer dan één enkele "
                  "meting</strong>, want het vlakt toevallige afwijkingen uit; vermeld er best bij hoe sterk "
                  "de metingen onderling verschilden."),
            ("p", "Een wetenschappelijke uitspraak verschilt van een los vermoeden doordat "
                  "<strong>ze getoetst is en weerlegd kan worden</strong>. Niet wie het zegt is beslissend. "
                  "Lees je op een website dat een plant beter groeit met muziek, dan "
                  "<strong>kijk je of er een proef met controlegroep achter zit</strong> en hoe die opgezet "
                  "was. <strong>Wie een onderzoek financiert, kan een belang hebben bij de uitkomst</strong>, "
                  "en dat hoort bij de beoordeling."),
        ]),
        dict(kop="STEM", blokken=[
            ("p", "<strong>STEM</strong> staat voor <strong>wetenschappen, technologie, "
                  "ingenieurswetenschappen en wiskunde</strong>, samen rond een echt probleem."),
            ("p", "Wil een klas een oplossing ontwerpen om een vijver gezonder te maken, dan is de goede "
                  "eerste stap de <strong>huidige toestand meten, zodat je later kan vergelijken</strong>. "
                  "Meten, ontwerpen, uitvoeren, opnieuw meten: dat is de cyclus."),
            ("weetje", "Een gat in je gegevens is zelf een resultaat. Noteer ook wat je níét gevonden "
                       "hebt: zo weet de lezer wat je besluit wel en niet kan dekken."),
        ]),
    ],
    onthoud=[
        "Een onderzoeksvraag moet je met een meting kunnen beantwoorden; een hypothese moet je kunnen weerleggen.",
        "De onafhankelijke variabele verander je zelf, de afhankelijke meet je, de rest houd je constant.",
        "Zonder controlegroep weet je niet wat er zonder behandeling gebeurd zou zijn.",
        "Herhaal metingen en gebruik meerdere exemplaren, anders meet je toeval.",
        "Een verband is nog geen oorzaak; verandert er meer dan één ding, dan weet je de oorzaak niet.",
        "Totale vergroting is oculair maal objectief; begin altijd met het zwakste objectief.",
        "Een dekglaasje houdt het preparaat vlak, een kleurstof geeft contrast, en een luchtbel lijkt op een cel.",
        "Op de horizontale as de ingestelde grootheid, met naam, eenheid en schaal bij elke as.",
        "Een wetenschappelijke uitspraak is getoetst en weerlegbaar; wie betaalt, hoort bij de beoordeling.",
    ],
)

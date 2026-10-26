"""
Geschiedenis ✨ Spark in de vormen van het examen van de Examencommissie.

Kim op 26 oktober 2026: dit eerst op één vak toepassen, geschiedenis ✨ Spark,
en dan wie het echte examen al aflegde vragen wat ze ervan vinden.

Elk hoofdstuk krijgt er zes tot acht vragen bij in de nieuwe vormen: een
tabel, een keuzelijst, volgorde, koppelen, slepen naar kolommen, woorden in een
zin slepen, klikken op een prent, een open antwoord, tekenen en een casus. De
vragen die er al staan, blijven staan. De import zoekt elk hoofdstuk op zijn
titel en zet deze vragen erbij; zet "Bestaande vragen vervangen" dus NIET aan.

Hoe elke vorm in een bestand staat: zie lib/examenvormen.ts en lib/vraagvorm.ts.
De prenten van de klikvragen staan in public/examenvormen/.

Draaien: python3 inhoud/spark/bron/geschiedenis_examenvormen.py
"""

import json
import os

J, F = True, False
HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "geschiedenis-examenvormen.json")


def tabel(vraag, rijen, uitleg, kolommen=None):
    v = {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}
    if kolommen:
        v["kolommen"] = kolommen
    return v


def keuze(vraag, uitleg):
    return {"type": "keuzelijst", "vraag": vraag, "uitleg": uitleg}


def volgorde(vraag, stappen, uitleg):
    return {"type": "volgorde", "vraag": vraag, "opties": stappen, "uitleg": uitleg}


def koppel(vraag, paren, extra, uitleg):
    return {"type": "koppelen", "vraag": vraag, "paren": paren, "extra": extra, "uitleg": uitleg}


def sorteer(vraag, kolommen, items, uitleg):
    return {"type": "sorteren", "vraag": vraag, "kolommen": kolommen, "items": items, "uitleg": uitleg}


def sleep(vraag, extra, uitleg):
    return {"type": "sleepzin", "vraag": vraag, "extra": extra, "uitleg": uitleg}


def klik(vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"/examenvormen/{prent}", "zones": zones, "uitleg": uitleg}


def open_(vraag, voorbeeld, beginregels=None, uitleg=None):
    v = {"type": "open", "vraag": vraag, "antwoord": voorbeeld}
    if beginregels:
        v["opties"] = beginregels
    if uitleg:
        v["uitleg"] = uitleg
    return v


def teken(vraag, voorbeeld, uitleg=None):
    v = {"type": "tekenen", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def casus(tekst, vragen):
    return {"casus": tekst, "vragen": vragen}


PERIODES = [
    "Prehistorie",
    "Oude nabije oosten",
    "Klassieke oudheid",
    "Middeleeuwen",
    "Vroegmoderne tijd",
    "Moderne tijd",
    "Hedendaagse tijd",
]

H = {}

H["Het historisch referentiekader — deel 1"] = [
    volgorde(
        "Zet de zeven periodes van het westerse historisch referentiekader in de juiste volgorde, van de oudste naar de jongste.",
        PERIODES,
        "Prehistorie, oude nabije oosten, klassieke oudheid, middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd.",
    ),
    tabel(
        "Lees elke uitspraak over de tijdrekening. Is ze juist of fout?",
        [
            ("Het jaar 500 v.C. ligt verder in het verleden dan het jaar 200 v.C.", J),
            ("Na het jaar 1 v.C. komt het jaar 0.", F),
            ("De 5de eeuw na Christus loopt van 401 tot en met 500.", J),
            ("Het jaar 1453 ligt in de 14de eeuw.", F),
        ],
        "Voor Christus tel je terug: 500 v.C. is ouder dan 200 v.C. Een jaar 0 bestaat niet, na 1 v.C. komt meteen 1 n.C. En 1453 ligt in de 15de eeuw, die loopt van 1401 tot en met 1500.",
    ),
    sorteer(
        "In welk maatschappelijk domein hoort elke gebeurtenis?",
        ["Politiek", "Economisch", "Sociaal", "Cultureel"],
        [
            ["Een koning vaardigt een nieuwe wet uit", "Politiek"],
            ["Boeren verkopen hun graan op de markt", "Economisch"],
            ["Slaven hebben minder rechten dan vrije burgers", "Sociaal"],
            ["Een beeldhouwer maakt een beeld van een god", "Cultureel"],
            ["Twee steden voeren oorlog", "Politiek"],
            ["Er wordt een kanaal naar de akkers gegraven", "Economisch"],
        ],
        "Macht, wetten en oorlog zijn politiek. Handel, landbouw en geld zijn economisch. Groepen in de samenleving en hun verhoudingen zijn sociaal. Religie, kunst, wetenschap en taal zijn cultureel.",
    ),
    keuze(
        "Het jaar 1492 ligt in de [[*15de|14de|16de]] eeuw en in het [[*2de|1ste|3de]] millennium na Christus.",
        "De 15de eeuw loopt van 1401 tot en met 1500. Het 2de millennium loopt van 1001 tot en met 2000.",
    ),
    sleep(
        "Honderd jaar is een [[eeuw]] en duizend jaar is een [[millennium]]. Gebeurtenissen in de juiste volgorde zetten, heet [[chronologie]].",
        ["decennium", "generatie", "periodisering"],
        "Een decennium is tien jaar. Periodisering is de tijd in periodes indelen, niet de volgorde van gebeurtenissen.",
    ),
    klik(
        "Klik op de tijdlijn op de plaats van het jaar 476 n.C., het einde van het West-Romeinse Rijk.",
        "tijdlijn.svg",
        [[63.6, 25, 7.9, 55]],
        "476 ligt vlak vóór het middelste streepje tussen Christus en 1000 n.C.; dat streepje is 500 n.C. Dat jaar is het scharnierpunt tussen de klassieke oudheid en de middeleeuwen.",
    ),
    teken(
        "Teken een tijdlijn van 1000 v.C. tot 1000 n.C. Zet een streepje om de honderd jaar, en duid de plaats van Christus aan.",
        "Een rechte lijn met een pijl naar rechts. Links staat 1000 v.C., rechts 1000 n.C., en in het midden de geboorte van Christus. Ertussen staan twintig gelijke stukjes van honderd jaar, tien aan elke kant.",
    ),
]

H["Het historisch referentiekader — deel 2"] = [
    koppel(
        "Welke periode begint met elk scharnierpunt?",
        [
            ["De uitvinding van het schrift", "Oude nabije oosten"],
            ["De machtsverschuiving naar de Middellandse Zee", "Klassieke oudheid"],
            ["De ondergang van het West-Romeinse Rijk in 476", "Middeleeuwen"],
        ],
        ["Prehistorie"],
        "Het schrift sluit de prehistorie af. Als Griekenland en Rome de macht overnemen van het nabije oosten, begint de klassieke oudheid. Met 476 beginnen de middeleeuwen. De prehistorie begint met geen van deze drie.",
    ),
    tabel(
        "Lees elke uitspraak over de periodisering. Is ze juist of fout?",
        [
            ("Een scharnierpunt geldt voor de hele wereld tegelijk.", F),
            ("De indeling in zeven periodes is een afspraak onder historici.", J),
            ("Het jaar 476 betekende voor China het begin van de middeleeuwen.", F),
            ("De westerse periodisering is gemaakt vanuit de geschiedenis van Europa.", J),
        ],
        "Scharnierpunten zijn plaatsgebonden: in 476 veranderde er voor China niets. De indeling is een afspraak, gemaakt vanuit Europa, en geen natuurwet.",
    ),
    keuze(
        "Een verandering die traag en stap voor stap verloopt, is een [[*evolutie|revolutie]]. Een snelle en ingrijpende verandering is een [[*revolutie|evolutie]].",
        "Daarom noemen historici de overgang naar de landbouw soms allebei: ze veranderde alles, maar het duurde wel duizenden jaren.",
    ),
    klik(
        "Klik op de tijdlijn op de plaats waar het spijkerschrift ontstond, rond 3300 v.C.",
        "tijdlijn.svg",
        [[3.5, 25, 7.9, 55]],
        "3300 v.C. ligt helemaal links, twee kleine streepjes na het begin van de lijn en nog vóór 3000 v.C. Daar eindigt de prehistorie in Mesopotamië.",
    ),
    sleep(
        "Het spijkerschrift ontstond rond [[3300]] v.C. in [[Mesopotamië]]. Daarmee eindigt daar de [[prehistorie]].",
        ["476", "Griekenland", "klassieke oudheid"],
        "Het schrift is het scharnierpunt tussen de prehistorie en het oude nabije oosten. Mesopotamië was een van de eerste plaatsen waar men schreef.",
    ),
    open_(
        "Leg uit waarom de westerse indeling in zeven periodes niet op de hele wereld past. Geef een voorbeeld.",
        "De indeling is gemaakt vanuit de geschiedenis van Europa. De scharnierpunten zijn gebeurtenissen die in Europa alles veranderden, maar elders niet. Een voorbeeld: in 476 ging het West-Romeinse Rijk ten onder, maar voor China of Amerika veranderde er toen niets.",
    ),
]

H["De prehistorie — deel 1"] = [
    tabel(
        "Lees elke uitspraak over de jagers en verzamelaars. Is ze juist of fout?",
        [
            ("Ze trokken rond, achter de dieren en de seizoenen aan.", J),
            ("Ze aten uitsluitend vlees.", F),
            ("Ze maakten scherpe werktuigen uit vuursteen.", J),
            ("Ze woonden in grote steden.", F),
            ("De mens leefde het grootste deel van zijn bestaan zo.", J),
        ],
        "Jagers en verzamelaars aten ook vruchten, noten en wortels. Steden kwamen pas veel later, na de landbouw. Maar het grootste deel van zijn bestaan leefde de mens wel zo.",
    ),
    keuze(
        "De moderne mens ontstond in [[*Afrika|Europa|Azië]]. De eerste mensachtige die dat werelddeel verliet, was de Homo [[*erectus|sapiens|habilis]].",
        "De Homo erectus, de rechtopgaande mens, trok als eerste uit Afrika naar Azië en Europa. Homo sapiens, de verstandige mens, ontstond ook in Afrika, maar veel later.",
    ),
    koppel(
        "Koppel elk woord aan wat het betekent.",
        [
            ["Nomade", "Iemand die rondtrekt en nergens vast woont"],
            ["Vuistbijl", "Een stenen werktuig dat je in je hand houdt om te hakken en te snijden"],
            ["Vuursteen", "Een harde steen die scherpe randen geeft als je hem slaat"],
            ["Lascaux", "Een grot in Frankrijk met prehistorische schilderingen"],
        ],
        ["Een dorp op een vaste plaats met akkers errond"],
        "Een dorp op een vaste plaats hoort bij de landbouwers, niet bij de jagers en verzamelaars.",
    ),
    volgorde(
        "Zet deze gebeurtenissen in de juiste volgorde, van lang geleden naar minder lang geleden.",
        [
            "De eerste mensachtigen leven in Afrika",
            "De Homo erectus trekt weg uit Afrika",
            "Mensen schilderen dieren op de wanden van de grot van Lascaux",
            "In het Midden-Oosten beginnen de eerste mensen met landbouw",
        ],
        "De Homo erectus verliet Afrika bijna twee miljoen jaar geleden. De schilderingen van Lascaux zijn ongeveer 17.000 jaar oud, de eerste landbouw ongeveer 10.000 jaar.",
    ),
    sleep(
        "Met het [[vuur]] konden mensen zich warmen, wilde dieren wegjagen en hun voedsel [[koken]]. Gekookt voedsel is makkelijker te [[verteren]].",
        ["water", "verkopen", "bewaren in de koelkast"],
        "Gekookt of geroosterd voedsel is zachter en makkelijker te verteren. Zo kreeg de mens meer energie uit zijn eten.",
    ),
    open_(
        "Waarom trokken jagers en verzamelaars steeds rond? Leg uit in één of twee zinnen.",
        "Ze leefden van wat de natuur hun gaf. Als de dieren wegtrokken of de planten op een plaats op waren, moesten ze verder trekken om nieuw voedsel te vinden.",
    ),
]

H["De prehistorie — deel 2"] = [
    sorteer(
        "Hoort dit bij de jagers en verzamelaars of bij de eerste landbouwers?",
        ["Jagers en verzamelaars", "Eerste landbouwers"],
        [
            ["Rondtrekken met de seizoenen", "Jagers en verzamelaars"],
            ["Een voedseloverschot", "Eerste landbouwers"],
            ["Een vaste woonplaats", "Eerste landbouwers"],
            ["Een vuistbijl uit geslagen vuursteen", "Jagers en verzamelaars"],
            ["Een gepolijste stenen bijl", "Eerste landbouwers"],
            ["Tamme geiten en schapen", "Eerste landbouwers"],
        ],
        "Jagers en verzamelaars trokken rond en sloegen hun werktuigen uit vuursteen. De landbouwers woonden vast, hielden dieren, kenden een overschot en polijsten hun stenen bijlen in het neolithicum.",
    ),
    volgorde(
        "Zet deze stappen in de juiste volgorde, van oorzaak naar gevolg.",
        [
            "Mensen beginnen met landbouw",
            "Er is meer voedsel dan nodig: een overschot",
            "Niet iedereen moet nog boer zijn, mensen leggen zich toe op één beroep",
            "Er ontstaan handel en de eerste steden",
        ],
        "Zonder landbouw geen overschot, zonder overschot geen specialisatie, en zonder specialisatie geen steden.",
    ),
    keuze(
        "Het leven op een vaste woonplaats heet [[*sedentair|nomadisch]] leven. De periode waarin de landbouw ontstaat, heet het [[*neolithicum|paleolithicum]], de nieuwe steentijd.",
        "Nomaden trekken rond. Het paleolithicum is de oude steentijd, de tijd van de jagers en verzamelaars.",
    ),
    tabel(
        "Lees elke uitspraak over de agrarische revolutie. Is ze juist of fout?",
        [
            ("De landbouw begon het eerst in de Vruchtbare Sikkel, in het Midden-Oosten.", J),
            ("De landbouw ontstond overal op de wereld op hetzelfde moment.", F),
            ("Door de landbouw werden alle mensen even rijk.", F),
            ("Met het vaste wonen kwamen er ook nieuwe ziektes en meer ruzie over bezit.", J),
        ],
        "De landbouw ontstond op verschillende plaatsen op verschillende momenten. Ze bracht ook ongelijkheid: wie meer land of vee had, werd rijker.",
    ),
    casus(
        "Een archeologe graaft in de Vruchtbare Sikkel een dorp op. Ze vindt huizen van leem, voorraadpotten met graankorrels, botten van geiten en een gepolijste stenen bijl.",
        [
            tabel(
                "Welke besluiten mag ze uit deze vondsten trekken?",
                [
                    ("De bewoners woonden op een vaste plaats.", J),
                    ("De bewoners hielden graan in voorraad.", J),
                    ("De bewoners leefden enkel van de jacht.", F),
                    ("Het dorp is ouder dan de eerste landbouw.", F),
                ],
                "Leemhuizen en voorraadpotten wijzen op vast wonen en een overschot. Graan en geiten wijzen op landbouw en veeteelt, dus het dorp is niet ouder dan de landbouw.",
            ),
            keuze(
                "De gepolijste bijl wijst op het [[*neolithicum|paleolithicum]]. De voorraadpotten tonen dat er een [[*overschot|tekort]] aan voedsel was.",
                "Gepolijste werktuigen horen bij de nieuwe steentijd. Je bewaart enkel voedsel dat je niet meteen nodig hebt.",
            ),
        ],
    ),
    open_(
        "Waarom noemen historici de overgang naar de landbouw een revolutie, en tegelijk een evolutie?",
        "Een revolutie, omdat ze de manier van leven helemaal veranderde: mensen gingen vast wonen, er kwam een overschot, steden en ongelijkheid. Een evolutie, omdat die verandering traag ging, over duizenden jaren.",
    ),
]

H["Mesopotamië en Egypte — deel 1"] = [
    sorteer(
        "Hoort dit bij Mesopotamië, bij Egypte, of bij allebei?",
        ["Mesopotamië", "Egypte", "Allebei"],
        [
            ["Spijkerschrift", "Mesopotamië"],
            ["Hiërogliefen", "Egypte"],
            ["Ziggurat", "Mesopotamië"],
            ["Piramide", "Egypte"],
            ["Farao", "Egypte"],
            ["Irrigatielandbouw", "Allebei"],
            ["Eufraat en Tigris", "Mesopotamië"],
            ["Een rijk langs een rivier", "Allebei"],
        ],
        "Allebei lagen ze aan een rivier en bevloeiden ze hun akkers. Het spijkerschrift, de ziggurat en de Eufraat en de Tigris horen bij Mesopotamië; de hiërogliefen, de piramides en de farao bij Egypte.",
    ),
    tabel(
        "Lees elke uitspraak over het oude Egypte. Is ze juist of fout?",
        [
            ("De Nijl overstroomde elk jaar en liet vruchtbaar slib achter.", J),
            ("De farao werd gezien als een god of als een zoon van de goden.", J),
            ("De Egyptenaren schreven met spijkerschrift.", F),
            ("Egypte lag aan de Eufraat.", F),
        ],
        "Het spijkerschrift en de Eufraat horen bij Mesopotamië. Egypte schreef in hiërogliefen en leefde van de Nijl.",
    ),
    koppel(
        "Koppel elk woord aan wat het betekent.",
        [
            ["Farao", "De heerser van Egypte"],
            ["Ziggurat", "Een trapvormige tempeltoren in Mesopotamië"],
            ["Kleitablet", "Waarop men in Mesopotamië schreef"],
            ["Mummie", "Een lichaam dat bewaard werd voor het leven na de dood"],
        ],
        ["Een marktplein in een Romeinse stad"],
        "Een marktplein in een Romeinse stad is een forum. Dat hoort bij de Romeinen, niet bij Mesopotamië of Egypte.",
    ),
    keuze(
        "Mesopotamië betekent het land tussen de [[*rivieren|bergen|zeeën]]. Het lag in wat nu [[*Irak|Egypte|Griekenland]] is.",
        "Meso is tussen, potamos is rivier. Het land tussen de Eufraat en de Tigris ligt grotendeels in het huidige Irak.",
    ),
    sleep(
        "In Mesopotamië drukte men tekens in natte [[klei]]. In Egypte schreef men hiërogliefen op [[papyrus]], gemaakt van een plant die langs de [[Nijl]] groeide.",
        ["perkament", "Tigris", "steen"],
        "Klei voor het spijkerschrift, papyrus voor de hiërogliefen. Papyrus groeide langs de Nijl.",
    ),
    open_(
        "Waarom mummificeerden de Egyptenaren hun doden?",
        "Ze geloofden in een leven na de dood. Het lichaam moest daarvoor bewaard blijven, zodat de ziel het kon terugvinden. Daarom balsemden ze het en legden ze voorwerpen in het graf.",
    ),
]

H["Mesopotamië en Egypte — deel 2"] = [
    volgorde(
        "Zet de groepen van de Egyptische standenmaatschappij in de juiste volgorde, van bovenaan naar onderaan.",
        [
            "De farao",
            "Priesters en hoge ambtenaren",
            "Schrijvers en ambachtslieden",
            "Boeren en slaven",
        ],
        "Bovenaan stond de farao, onderaan de boeren en slaven. Die laatste groep was veruit de grootste.",
    ),
    tabel(
        "Lees elke uitspraak over het schrift. Is ze juist of fout?",
        [
            ("Het schrift werd in de eerste plaats uitgevonden om verhalen te bewaren.", F),
            ("De oudste kleitabletten zijn vooral boekhouding: graan, vee en wie wat bezat.", J),
            ("In deze rijken kon bijna iedereen lezen en schrijven.", F),
            ("Schrijvers hadden een gewaardeerd beroep.", J),
        ],
        "Het schrift ontstond om bezit en voorraden bij te houden. Lezen en schrijven was iets voor een kleine groep schrijvers, en dat gaf aanzien.",
    ),
    casus(
        "In 1799 vinden Franse soldaten bij de Egyptische stad Rosetta een steen. Er staat drie keer dezelfde tekst op: in hiërogliefen, in een ander Egyptisch schrift en in het Grieks.",
        [
            keuze(
                "Omdat geleerden het [[*Grieks|Egyptisch|spijkerschrift]] konden lezen, konden ze de [[*hiërogliefen|Griekse tekst|kleitabletten]] ontcijferen.",
                "De Griekse tekst kon men al lezen. Door de drie versies naast elkaar te leggen, vond men stap voor stap uit wat de hiërogliefen betekenden.",
            ),
            tabel(
                "Is elke uitspraak over de Steen van Rosetta juist of fout?",
                [
                    ("De steen is een primaire bron over het oude Egypte.", J),
                    ("Op de steen staat drie keer een andere tekst.", F),
                    ("Zonder de Griekse tekst was het veel moeilijker geweest om de hiërogliefen te lezen.", J),
                ],
                "Het is drie keer dezelfde tekst, in drie schriften. Net daarom was hij zo bruikbaar.",
            ),
        ],
    ),
    keuze(
        "Handel zonder munten heet [[*ruilhandel|groothandel|wereldhandel]]. Mesopotamië kon niet zonder handel, omdat er weinig [[*hout en metaal|graan|water]] was.",
        "Mesopotamië had vruchtbare grond, maar nauwelijks bomen, steen of metaal. Die ruilde men voor graan en textiel.",
    ),
    sleep(
        "In een [[tempeleconomie]] zamelt de tempel de oogst in, slaat ze op en verdeelt ze weer. Zo zaten de economische en de [[religieuze]] macht in dezelfde handen.",
        ["ruilhandel", "militaire"],
        "De tempel was pakhuis en verdeelcentrum tegelijk. Daardoor hadden de priesters ook economische macht.",
    ),
    open_(
        "Waarom vroeg irrigatielandbouw om samenwerking en een sterk bestuur?",
        "Kanalen en dijken graven en onderhouden kan één boer niet alleen. Veel mensen moesten samenwerken, en iemand moest dat werk regelen, het water verdelen en ruzies beslechten. Zo groeide er een bestuur.",
    ),
]

H["Het oude Griekenland — deel 1"] = [
    sorteer(
        "Hoort dit bij Athene of bij Sparta?",
        ["Athene", "Sparta"],
        [
            ["Democratie", "Athene"],
            ["Een strenge militaire opvoeding vanaf je zevende", "Sparta"],
            ["Een grote vloot en handel over zee", "Athene"],
            ["Heloten die het land bewerken", "Sparta"],
            ["Het Parthenon op de Akropolis", "Athene"],
            ["Een stadstaat in het binnenland die van landbouw leeft", "Sparta"],
        ],
        "Athene was maritiem en stedelijk, met een vloot, handel en de eerste democratie. Sparta lag in het binnenland, leefde van landbouw door heloten en voedde zijn jongens op tot soldaat.",
    ),
    tabel(
        "Lees elke uitspraak over het oude Griekenland. Is ze juist of fout?",
        [
            ("Alle Griekse stadstaten werden samen door één koning bestuurd.", F),
            ("De Grieken deelden dezelfde taal en dezelfde goden.", J),
            ("De Olympische Spelen werden gehouden in Athene.", F),
            ("In Athene mochten vrouwen en slaven niet meestemmen.", J),
        ],
        "Elke polis had haar eigen bestuur. De Spelen vonden plaats in Olympia, ter ere van Zeus. Meestemmen mochten in Athene enkel de vrije mannen die burger waren.",
    ),
    keuze(
        "Een Griekse stadstaat heet een [[*polis|forum|ziggurat]]. In Athene groeide de [[*democratie|monarchie|tirannie]], een bestuur waarin de burgers zelf beslisten.",
        "Demos is volk, kratos is macht. Een forum is Romeins en een ziggurat hoort bij Mesopotamië.",
    ),
    koppel(
        "Koppel elk woord aan wat het betekent.",
        [
            ["Zeus", "De oppergod van de Grieken"],
            ["Olympus", "De berg waarop de goden woonden"],
            ["Parthenon", "De tempel op de Akropolis van Athene"],
            ["Orakel", "Een plaats waar je de goden om raad vroeg"],
        ],
        ["Een raad van rijke en ervaren Romeinen"],
        "Een raad van rijke en ervaren Romeinen is de senaat. Die hoort bij Rome, niet bij Griekenland.",
    ),
    klik(
        "Klik op de Ionische zuil.",
        "zuilen.svg",
        [[64, 10, 28, 85]],
        "De Ionische zuil herken je aan de twee grote krullen bovenaan. De Dorische is sober en heeft geen voet. De Korintische heeft bladeren.",
    ),
    sleep(
        "Griekenland heeft veel [[bergen]] en eilanden. Daardoor ontstonden er veel aparte [[stadstaten]] in plaats van één groot rijk.",
        ["woestijnen", "keizerrijken"],
        "Bergen en zee scheidden de steden van elkaar. Elke stad groeide zo uit tot een eigen staatje.",
    ),
]

H["Het oude Griekenland — deel 2"] = [
    volgorde(
        "Zet deze vormen van bestuur in de volgorde waarin ze elkaar in Athene opvolgden.",
        ["Koningschap", "Oligarchie", "Tirannie", "Democratie"],
        "Eerst een koning, dan een kleine groep rijken, dan tirannen die alleen de macht grepen, en ten slotte de democratie.",
    ),
    koppel(
        "Wie vocht tegen wie?",
        [
            ["De Perzische oorlogen", "De Griekse stadstaten tegen het Perzische Rijk"],
            ["De Peloponnesische oorlog", "Athene tegen Sparta"],
        ],
        ["Rome tegen Carthago"],
        "Rome tegen Carthago, dat zijn de Punische oorlogen. Die horen bij het Romeinse Rijk.",
    ),
    volgorde(
        "Wie was de leraar van wie? Zet ze in volgorde, van de leraar naar de leerling.",
        ["Socrates", "Plato", "Aristoteles", "Alexander de Grote"],
        "Socrates was de leraar van Plato, Plato die van Aristoteles, en Aristoteles was de leraar van de jonge Alexander de Grote.",
    ),
    keuze(
        "De Dorische zuil is [[*sober|met krullen|met bladeren]]. De Korintische zuil heeft een kapiteel met [[*bladeren|krullen]].",
        "Dorisch is sober, Ionisch heeft krullen en Korintisch bladeren.",
    ),
    tabel(
        "Lees elke uitspraak. Is ze juist of fout?",
        [
            ("Athene was een directe democratie: de burgers stemden zelf, niet via verkozenen.", J),
            ("Na de Peloponnesische oorlog was Athene sterker dan ooit.", F),
            ("Een Spartaanse vrouw had meer vrijheid dan een Atheense vrouw.", J),
            ("Na de veroveringen van Alexander verdween de Griekse cultuur uit het oosten.", F),
        ],
        "Athene verloor de Peloponnesische oorlog en verzwakte. Na Alexander verspreidde de Griekse cultuur zich juist en vermengde ze zich met die van het oosten: het hellenisme.",
    ),
    sleep(
        "Alexander de Grote veroverde een rijk tot in [[India]]. De vermenging van de Griekse cultuur met die van het oosten heet het [[hellenisme]].",
        ["Rome", "christendom"],
        "Hellas is Griekenland. Het hellenisme verspreidde Griekse taal, kunst en wetenschap tot ver in Azië.",
    ),
    open_(
        "Waarom stichtten Grieken kolonies rond de Middellandse Zee? Geef twee redenen.",
        "Er was te weinig vruchtbare grond voor een groeiende bevolking. Daarnaast zochten ze nieuwe plaatsen om handel te drijven. Soms trokken ook mensen weg na ruzie of armoede in hun stad.",
        ["Reden 1:", "Reden 2:"],
    ),
]

H["Het Romeinse Rijk — deel 1"] = [
    volgorde(
        "Zet deze periodes van Rome in de juiste volgorde.",
        [
            "Rome wordt bestuurd door koningen",
            "Rome is een republiek met een senaat en consuls",
            "Augustus wordt de eerste keizer",
            "Het West-Romeinse Rijk gaat ten onder",
        ],
        "Eerst de koningstijd, dan de republiek, dan het keizerrijk vanaf Augustus, en in 476 het einde van het West-Romeinse Rijk.",
    ),
    tabel(
        "Lees elke uitspraak over Rome. Is ze juist of fout?",
        [
            ("Rome ligt aan de Tiber.", J),
            ("Julius Caesar was de eerste keizer van Rome.", F),
            ("De Romeinen spraken Latijn.", J),
            ("De Romeinen namen niets over van de Griekse cultuur.", F),
        ],
        "Julius Caesar werd vermoord voor hij keizer kon worden; Augustus was de eerste keizer. De Romeinen namen veel over van de Grieken: goden, bouwkunst en kunst.",
    ),
    koppel(
        "Koppel elk Romeins woord aan wat het betekent.",
        [
            ["Aquaduct", "Een waterleiding tot in de stad"],
            ["Forum", "Het marktplein en centrum van de stad"],
            ["Amfitheater", "De plaats waar gladiatoren vochten"],
            ["Senaat", "Een raad van rijke en ervaren mannen"],
        ],
        ["Een trapvormige tempeltoren"],
        "Een trapvormige tempeltoren is een ziggurat, uit Mesopotamië.",
    ),
    keuze(
        "Volgens de sage werd Rome gesticht door [[*Romulus|Augustus|Caesar]], die samen met zijn broer Remus door een [[*wolvin|adelaar|beer]] gezoogd werd.",
        "Romulus en Remus werden als baby in de Tiber gelegd. Een wolvin zou hen gered hebben. Rome is naar Romulus genoemd.",
    ),
    klik(
        "Volgens de sage werd Rome gesticht in 753 v.C. Klik op die plaats op de tijdlijn.",
        "tijdlijn.svg",
        [[44.3, 25, 7.9, 55]],
        "753 v.C. ligt tussen het lange streepje van 1000 v.C. en het middelste streepje van 500 v.C., ongeveer halfweg.",
    ),
    sleep(
        "De Romeinen noemden de Middellandse Zee [[mare nostrum]], onze zee. Over die zee en over hun [[wegen]] dreven ze handel in het hele rijk.",
        ["mare magnum", "kanalen"],
        "Mare nostrum toont hoe groot het rijk was: de Middellandse Zee lag er helemaal in.",
    ),
]

H["Het Romeinse Rijk — deel 2"] = [
    sorteer(
        "Hoort dit bij de Romeinse republiek of bij het keizerrijk?",
        ["Republiek", "Keizerrijk"],
        [
            ["Twee consuls, elk voor één jaar", "Republiek"],
            ["De Pax Romana", "Keizerrijk"],
            ["Augustus noemt zichzelf princeps", "Keizerrijk"],
            ["De volksvergadering kiest de bestuurders", "Republiek"],
            ["De keizerscultus", "Keizerrijk"],
            ["De Punische oorlogen tegen Carthago", "Republiek"],
        ],
        "De consuls, de volksvergadering en de Punische oorlogen horen bij de republiek. Met Augustus begint het keizerrijk, met de Pax Romana en de keizerscultus.",
    ),
    casus(
        "Na de Punische oorlogen komen er duizenden krijgsgevangenen als slaven naar Italië. Rijke Romeinen kopen het land van kleine boeren op en laten het door slaven bewerken.",
        [
            keuze(
                "Zo'n groot landgoed dat met slaven bewerkt werd, heet een [[*latifundium|forum|triumviraat]]. De kleine boeren trokken arm naar de [[*stad|kolonies|bergen]].",
                "De kleine boer kon niet op tegen gratis slavenarbeid. Velen trokken naar Rome en hadden daar geen werk.",
            ),
            tabel(
                "Is elk gevolg juist of fout?",
                [
                    ("De kloof tussen rijk en arm werd groter.", J),
                    ("De kleine boeren werden rijker door de slaven.", F),
                    ("De onrust in Rome nam toe.", J),
                ],
                "De rijken werden rijker en de kleine boeren armer. Die spanning hielp mee om de republiek te doen wankelen.",
            ),
        ],
    ),
    koppel(
        "Koppel elk begrip aan wat het betekent.",
        [
            ["Pax Romana", "Een lange periode van vrede in het rijk"],
            ["Triumviraat", "Een bondgenootschap van drie machtige mannen"],
            ["Keizerscultus", "De keizer vereren als een god"],
            ["Princeps", "De eerste burger, zo noemde Augustus zichzelf"],
        ],
        ["Een groot landgoed dat met slaven bewerkt werd"],
        "Een groot landgoed met slaven is een latifundium.",
    ),
    tabel(
        "Lees elke uitspraak over het einde van het rijk. Is ze juist of fout?",
        [
            ("In de 3de eeuw waren er invallen aan de grenzen en keizers die elkaar snel opvolgden.", J),
            ("Het rijk werd verdeeld in een West-Romeins en een Oost-Romeins Rijk.", J),
            ("Het Oost-Romeinse Rijk verdween samen met het West-Romeinse Rijk in 476.", F),
            ("De crisis van de 3de eeuw kwam door de verwoesting van Carthago.", F),
        ],
        "Het Oost-Romeinse Rijk bestond nog bijna duizend jaar, tot 1453. Carthago was al eeuwen eerder verwoest, in de Punische oorlogen.",
    ),
    sleep(
        "Het christendom werd eerst [[vervolgd]], maar groeide later uit tot de [[staatsgodsdienst]] van het rijk.",
        ["beloond", "keizerscultus"],
        "Christenen weigerden de keizer als god te vereren en werden daarom vervolgd. Aan het einde van de 4de eeuw werd het christendom de godsdienst van het rijk.",
    ),
    open_(
        "Waarom ging de Romeinse republiek uiteindelijk ten onder? Geef twee oorzaken.",
        "De kloof tussen rijk en arm werd groot, onder meer door de latifundia, en dat gaf onrust. Machtige generaals met hun eigen leger vochten onderling om de macht, zoals Caesar. Uiteindelijk nam Augustus alle macht in handen.",
        ["Oorzaak 1:", "Oorzaak 2:"],
    ),
]

MUNT = "Lien vindt bij het spitten in de tuin een oude munt. Er staat de kop van keizer Augustus op en een Latijnse tekst."

H["Bronnen, kunst en beeldvorming — deel 1"] = [
    sorteer(
        "Is elke bron over de Romeinen een primaire of een secundaire bron?",
        ["Primaire bron", "Secundaire bron"],
        [
            ["Een brief van een Romeinse soldaat aan zijn familie", "Primaire bron"],
            ["Je schoolboek over de Romeinen", "Secundaire bron"],
            ["Een Romeinse munt uit een opgraving", "Primaire bron"],
            ["Een documentaire van vorig jaar over Rome", "Secundaire bron"],
            ["Een grafsteen van een Romeinse burger", "Primaire bron"],
        ],
        "Een primaire bron komt uit de tijd zelf. Een secundaire bron is later gemaakt, over die tijd.",
    ),
    koppel(
        "Welke soort bron is het, naar haar vorm?",
        [
            ["Een potscherf uit een opgraving", "Materiële bron"],
            ["Een opgenomen gesprek met iemand die de oorlog meemaakte", "Mondelinge bron"],
            ["Een kleitablet met spijkerschrift", "Geschreven bron"],
            ["Een oude filmopname", "Audiovisuele bron"],
        ],
        ["Secundaire bron"],
        "Naar hun vorm zijn bronnen geschreven, mondeling, materieel of audiovisueel. Secundair zegt iets over wanneer de bron gemaakt is, niet over haar vorm.",
    ),
    casus(
        MUNT,
        [
            keuze(
                "De munt is een [[*primaire|secundaire]] bron, en naar haar vorm een [[*materiële|mondelinge|audiovisuele]] bron.",
                "De munt komt uit de tijd van Augustus zelf en is een voorwerp.",
            ),
            tabel(
                "Wat mag Lien uit de munt besluiten?",
                [
                    ("De munt is gemaakt toen Augustus keizer was, of later.", J),
                    ("De Romeinen kwamen ooit tot in de streek van Lien, of hun munten wel.", J),
                    ("Augustus heeft zelf in die tuin gestaan.", F),
                ],
                "Een munt reist met handelaars en soldaten mee. Ze toont dat Romeinse munten tot daar kwamen, niet dat de keizer er zelf was.",
            ),
        ],
    ),
    tabel(
        "Lees elke uitspraak. Is ze juist of fout?",
        [
            ("Een game kan nooit een bron zijn voor een historicus.", F),
            ("Wie een bron betaalt, kan invloed hebben op wat erin staat.", J),
            ("Het verleden en de geschiedenis zijn precies hetzelfde.", F),
            ("Een kunstwerk kan tonen wat mensen belangrijk vonden.", J),
        ],
        "Alles wat mensen maken, ook een game, kan iets vertellen over hun tijd. Het verleden is wat er gebeurde; de geschiedenis is het verhaal dat historici er met bronnen over maken.",
    ),
    sleep(
        "Iemand die een gebeurtenis met eigen ogen zag, is een [[ooggetuige]]. Iemand die in dezelfde tijd leefde maar er niet bij was, is een [[tijdgenoot]].",
        ["historicus", "archeoloog"],
        "Een historicus en een archeoloog bestuderen het verleden later; ze waren er zelf niet bij.",
    ),
    open_(
        "Waarom wil een historicus weten wie een bron gemaakt heeft?",
        "Wie de bron maakte, bepaalt mee wat erin staat. Die persoon had een eigen mening, belang of opdrachtgever. Als je dat weet, kan je beter inschatten hoe betrouwbaar de bron is.",
    ),
]

KADESJ = (
    "In 1274 v.C. vechten de Egyptenaren van farao Ramses II en de Hettieten bij Kadesj. "
    "Ramses laat op de muren van zijn tempels uithouwen dat hij een grote overwinning behaalde. "
    "In de teksten van de Hettieten staat dat zij gewonnen hebben."
)

H["Bronnen, kunst en beeldvorming — deel 2"] = [
    casus(
        KADESJ,
        [
            tabel(
                "Is elke uitspraak juist of fout?",
                [
                    ("Beide bronnen kunnen overdrijven.", J),
                    ("Omdat de bronnen elkaar tegenspreken, zijn ze waardeloos.", F),
                    ("Ramses liet zijn overwinning uithouwen om zijn macht te tonen.", J),
                    ("Een tempelmuur is altijd betrouwbaarder dan een kleitablet.", F),
                ],
                "Een bron die overdrijft, vertelt nog altijd veel: over hoe een heerser gezien wilde worden. Of een bron betrouwbaar is, hangt niet af van het materiaal.",
            ),
            keuze(
                "Dat beide partijen de overwinning claimen, is een voorbeeld van [[*meerdere perspectieven|continuïteit en verandering|oorzaak en gevolg]].",
                "Hetzelfde voorval, bekeken door twee betrokkenen, geeft twee heel verschillende verhalen.",
            ),
            open_(
                "Wat zou jij als historicus doen om te weten te komen wie de slag bij Kadesj echt gewonnen heeft?",
                "Andere bronnen zoeken die niet van Ramses of van de Hettieten komen, en kijken wat er na de slag gebeurde: wie hield het gebied, werd er een verdrag gesloten? Zo vergelijk je de bronnen en gebruik je bewijs in plaats van de claims van één kant.",
            ),
        ],
    ),
    koppel(
        "Koppel elke historische redeneerwijze aan een voorbeeld.",
        [
            ["Oorzaak en gevolg", "Door de landbouw ontstond een voedseloverschot"],
            ["Continuïteit en verandering", "De Romeinen namen de Griekse goden over, maar gaven ze andere namen"],
            ["Meerdere perspectieven", "Een slaaf en een keizer beleefden hetzelfde rijk heel anders"],
            ["Bewijs gebruiken", "Je steunt je besluit op wat in de bronnen staat"],
        ],
        ["Afgaan op je gevoel"],
        "Afgaan op je gevoel is geen historische redeneerwijze.",
    ),
    tabel(
        "Lees elke uitspraak. Is ze juist of fout?",
        [
            ("Een bron kan bruikbaar zijn en toch onbetrouwbaar.", J),
            ("Een onbetrouwbare bron is waardeloos voor een historicus.", F),
            ("Een bron die volledig klopt, kan toch onbruikbaar zijn voor jouw vraag.", J),
            ("Het beeld dat historici van het verleden hebben, verandert nooit.", F),
        ],
        "Bruikbaar gaat over je onderzoeksvraag, betrouwbaar over of de bron klopt. Nieuwe vondsten en nieuwe vragen kunnen het beeld van het verleden veranderen.",
    ),
    sleep(
        "De Griekse schrijver Herodotos noemde de Perzen [[barbaren]]: mensen die geen Grieks spraken. Dat hij zo keek, omdat hij een Griek was, heet [[standplaatsgebondenheid]].",
        ["burgers", "mythevorming"],
        "Iedereen kijkt vanuit zijn eigen tijd, plaats en groep. Daar moet je als historicus rekening mee houden, ook bij jezelf.",
    ),
]


def tel(vragen):
    """Telt de vragen, ook die in een casus."""
    n = 0
    for v in vragen:
        n += len(v["vragen"]) if "casus" in v else 1
    return n


def main():
    hoofdstukken = [{"titel": t, "niveau": "spark", "vragen": v} for t, v in H.items()]
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump({"hoofdstukken": hoofdstukken}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    totaal = sum(tel(v) for v in H.values())
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen -> {os.path.normpath(UIT)}")


if __name__ == "__main__":
    main()

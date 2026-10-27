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
        "Een archeoloog vindt in een Egyptisch graf een mummie, met voedsel, meubels en juwelen erbij. Wat vertelt die vondst over hoe de Egyptenaren over de dood dachten?",
        "Ze geloofden dat het leven na de dood verderging. De dode kreeg voedsel en spullen mee, omdat hij die in het hiernamaals nodig zou hebben. Het lichaam werd gebalsemd, zodat het bewaard bleef.",
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
        "Een Romeinse schrijver beschrijft de Germanen als wilde barbaren. Waarom moet je weten wie die tekst schreef, voor je hem gelooft?",
        "De schrijver was een Romein, en de Romeinen vochten tegen de Germanen. Hij kan hen slechter voorgesteld hebben dan ze waren, zodat Rome beter leek. Daarom zoek je ook andere bronnen, zoals wat archeologen bij de Germanen zelf vonden.",
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


# ---------------------------------------------------------------------------
# Vragen bij de prenten van Kim ("Geschiedenis in beeld", 26-10-2026).
# Die prenten zijn met AI nagemaakt, geen echte foto's en geen bronnen. Elke
# vraag zegt dat ("nagemaakte prent"), en geen vraag doet alsof je er iets uit
# kan bewijzen. Ze staan in public/examenvormen/beeld/; de twee prenten met
# nummers (prenten-steentijd, prenten-periodes) zijn er samengezet.
# ---------------------------------------------------------------------------


def met(prent, vraag):
    """Zet een prent boven een vraag."""
    vraag["afbeelding_url"] = f"/examenvormen/beeld/{prent}"
    return vraag


H["Het historisch referentiekader — deel 2"] += [
    met("prenten-periodes.webp", koppel(
        "Bekijk de zes nagemaakte prenten. Bij welke periode hoort elke prent?",
        [
            ["Prent 1", "Oude nabije oosten"],
            ["Prent 2", "Klassieke oudheid"],
            ["Prent 3", "Middeleeuwen"],
            ["Prent 4", "Vroegmoderne tijd"],
            ["Prent 5", "Moderne tijd"],
            ["Prent 6", "Hedendaagse tijd"],
        ],
        ["Prehistorie"],
        "1 is een ziggurat, een tempeltoren uit Mesopotamië. 2 is het Colosseum in Rome. 3 is een burcht met een gracht. 4 is een zeilschip zoals bij de ontdekkingsreizen rond 1500. 5 is een stoomlocomotief uit de 19de eeuw. 6 zijn de vlaggen van de Europese Unie, die na de Tweede Wereldoorlog ontstond. Bij de prehistorie hoort geen enkele prent.",
    )),
]

H["De prehistorie — deel 1"] += [
    met("grotschildering.webp", keuze(
        "Bekijk de nagemaakte prent. Op deze rotstekening staan [[*dieren|akkers|huizen]]. Zulke tekeningen maakten de jagers-verzamelaars van het [[*paleolithicum|neolithicum]].",
        "Op de wanden van grotten schilderden jagers-verzamelaars de dieren die ze kenden en waarop ze jaagden, zoals paarden en runderen. Akkers en vaste huizen komen pas in het neolithicum.",
    )),
    met("vuistbijl.webp", tabel(
        "Bekijk de nagemaakte prent van een vuistbijl. Is elke uitspraak juist of fout?",
        [
            ("Een vuistbijl is gemaakt van steen, meestal vuursteen.", J),
            ("Een vuistbijl had een lange houten steel.", F),
            ("Je hield een vuistbijl in je hand om mee te hakken, snijden en schrapen.", J),
            ("Een vuistbijl werd gegoten uit brons.", F),
            ("De vuistbijl hoort bij het paleolithicum.", J),
        ],
        "Een vuistbijl is een stuk vuursteen dat aan beide kanten bijgeslagen werd. Je hield hem in je vuist, vandaar de naam; een steel had hij niet. Brons kwam pas veel later.",
    )),
]

H["De prehistorie — deel 2"] += [
    met("prenten-steentijd.webp", sorteer(
        "Bekijk de vier nagemaakte prenten. Hoort elke prent bij het paleolithicum of bij het neolithicum?",
        ["Paleolithicum", "Neolithicum"],
        [
            ["Prent 1, een rotstekening", "Paleolithicum"],
            ["Prent 2, een vuistbijl", "Paleolithicum"],
            ["Prent 3, een pot van gebakken klei", "Neolithicum"],
            ["Prent 4, een graf van grote stenen", "Neolithicum"],
        ],
        "Rotstekeningen en vuistbijlen zijn van de jagers-verzamelaars van het paleolithicum. Potten van gebakken klei en hunebedden horen bij het neolithicum: wie op een vaste plaats woont, kan voorraden bewaren en grote graven bouwen.",
    )),
    casus(
        "Archeologen vonden de sporen van een dorp uit het neolithicum: paalgaten, resten van wanden en scherven. Daarop is deze prent gebaseerd. Ze is nagemaakt, geen echte foto.",
        [
            klik(
                "De wanden van deze huizen zijn gemaakt van gevlochten takken met leem erop. Klik op zo'n wand van leem.",
                "beeld/neolithisch-dorp.webp",
                [[33, 36, 18, 38], [10, 59, 24, 15], [77, 37, 21, 31]],
                "De lichte, gladde wanden onder de daken zijn van leem. De daken zijn van riet, de omheining vooraan is van gevlochten takken.",
            ),
            met("neolithisch-dorp.webp", tabel(
                "Wat zegt zo'n dorp over het leven in het neolithicum? Is elke uitspraak juist of fout?",
                [
                    ("De mensen bleven op een vaste plaats wonen.", J),
                    ("De huizen waren gebouwd met bakstenen en dakpannen.", F),
                    ("De mensen bouwden met hout, leem en riet uit hun omgeving.", J),
                    ("De bewoners trokken elke paar weken verder om te jagen.", F),
                ],
                "In het neolithicum gingen de mensen aan landbouw en veeteelt doen. Daarom bleven ze op één plaats wonen, in huizen van hout, leem en riet. Bakstenen en dakpannen kwamen veel later.",
            )),
        ],
    ),
]

H["Mesopotamië en Egypte — deel 1"] += [
    met("kleitablet.webp", sleep(
        "Bekijk de nagemaakte prent. Op dit tablet staat [[spijkerschrift]]. Met een [[rietstengel]] drukte men wigvormige tekens in natte [[klei]].",
        ["hiërogliefen", "papyrus", "beitel"],
        "Het spijkerschrift ontstond in Mesopotamië. Met een rietstengel drukte men tekens in natte klei. Hiërogliefen en papyrus horen bij Egypte.",
    )),
    met("ziggurat.webp", tabel(
        "Bekijk de nagemaakte prent van een ziggurat. Is elke uitspraak juist of fout?",
        [
            ("Een ziggurat is een tempeltoren in trappen.", J),
            ("Een ziggurat was het graf van een farao.", F),
            ("Een ziggurat stond in een stad in Mesopotamië.", J),
            ("Ziggurats werden gebouwd uit wit marmer.", F),
            ("Bovenaan stond een tempel voor de god van de stad.", J),
        ],
        "Een ziggurat is een tempeltoren in trappen uit Mesopotamië, gebouwd uit gedroogde en gebakken kleitegels. Bovenaan stond een tempel voor de god van de stad. Het graf van een farao is een piramide, in Egypte.",
    )),
]

H["Mesopotamië en Egypte — deel 2"] += [
    klik(
        "Bekijk de nagemaakte prent. Klik op het bouwwerk dat gebouwd werd als graf voor een farao.",
        "beeld/piramide-sfinx.webp",
        [[16, 4, 54, 56]],
        "De piramide is het graf van een farao. Het beeld ervoor, met het lichaam van een leeuw en het hoofd van een mens, is de sfinx. Die bewaakte het graf.",
    ),
    met("dodenmasker.webp", keuze(
        "Bekijk de nagemaakte prent. Zo'n gouden masker lag op het gezicht van de [[*mummie|beeltenis|sfinx]] van een farao. De Egyptenaren balsemden hun doden omdat ze geloofden in [[*een leven na de dood|een nieuw leven als dier|een einde zonder hiernamaals]].",
        "De Egyptenaren geloofden dat het leven na de dood verderging. Het lichaam moest daarvoor bewaard blijven, en daarom maakten ze er een mummie van. Een farao kreeg een kostbaar masker en grafgiften mee.",
    )),
]

H["Het oude Griekenland — deel 1"] += [
    met("parthenon.webp", keuze(
        "Bekijk de nagemaakte prent. Dit is het [[*Parthenon|Colosseum|Pantheon]]. Het staat op de Akropolis van [[*Athene|Sparta|Rome]] en was gewijd aan [[*Athena|Zeus|Poseidon]]. De zuilen zijn [[*Dorisch|Ionisch|Korintisch]].",
        "Het Parthenon op de Akropolis van Athene was gewijd aan Athena, de beschermgodin van de stad. De zuilen zijn Dorisch: eenvoudig, zonder voet en met een vlak kapiteel. Het Colosseum en het Pantheon staan in Rome.",
    )),
]

H["Het oude Griekenland — deel 2"] += [
    casus(
        "Op Griekse vazen en in Griekse beelden zie je vaak sporters. De twee prenten bij deze vragen zijn nagemaakt, geen foto's van echte vazen of beelden.",
        [
            met("griekse-vaas.webp", tabel(
                "Bekijk de prent van de vaas. Is elke uitspraak juist of fout?",
                [
                    ("De figuren zijn zwart geschilderd op een oranje ondergrond.", J),
                    ("Op de vaas zie je mensen die lopen.", J),
                    ("Op de vaas staan Romeinse gladiatoren.", F),
                    ("Zulke vazen vertellen iets over wat de Grieken belangrijk vonden.", J),
                    ("Op Griekse vazen staan nooit goden of verhalen.", F),
                ],
                "Op Griekse vazen staan sporters, mythologische verhalen en scènes uit het dagelijkse leven. Hier zijn het lopers, zwart op de oranje klei. Gladiatoren zijn Romeins.",
            )),
            met("discuswerper.webp", open_(
                "Bekijk de prent van het beeld. Welke sport beoefent deze man? Bij welk groot feest van de Grieken hoorde die sport, en ter ere van welke god?",
                "Hij gooit een discus. Discuswerpen hoorde bij de Olympische Spelen in Olympia, die ter ere van Zeus gehouden werden.",
            )),
        ],
    ),
]

H["Het Romeinse Rijk — deel 1"] += [
    met("colosseum.webp", sleep(
        "Bekijk de nagemaakte prent. Het Colosseum in [[Rome]] is een [[amfitheater]]. Het publiek keek er naar gevechten van [[gladiatoren]].",
        ["Athene", "tempel", "filosofen"],
        "Het Colosseum staat in Rome. Een amfitheater is rondom gebouwd, zodat iedereen zicht had op het midden, waar gladiatoren vochten.",
    )),
]

H["Het Romeinse Rijk — deel 2"] += [
    casus(
        "Rijke Romeinen woonden in een groot huis met in het midden een atrium, een open ruimte waar bezoekers ontvangen werden. De prent is nagemaakt, geen echte foto.",
        [
            klik(
                "Door een opening in het dak viel licht en regenwater in het atrium. Klik op die opening.",
                "beeld/romeins-atrium.webp",
                [[39, 4, 27, 13]],
                "Bovenaan in het midden zit het dak open. Het regenwater viel in het bekken eronder.",
            ),
            met("romeins-atrium.webp", tabel(
                "Wat leer je uit deze prent over het huis van een rijke Romein? Is elke uitspraak juist of fout?",
                [
                    ("Het huis had zuilen rond een open ruimte.", J),
                    ("De vloer was versierd met een mozaïek.", J),
                    ("Alle Romeinen woonden in zo'n huis.", F),
                    ("In het midden stond een bekken met water.", J),
                    ("Het huis was gebouwd uit riet en leem.", F),
                ],
                "Zuilen, een mozaïekvloer en een waterbekken passen bij het huis van een rijke familie. De meeste Romeinen woonden in een klein appartement in een huurblok.",
            )),
        ],
    ),
]

H["Bronnen, kunst en beeldvorming — deel 1"] += [
    met("hunebed.webp", tabel(
        "Onder deze prent van een hunebed staat: AI-reconstructie, geen echte foto. Is elke uitspraak juist of fout?",
        [
            ("De prent is een primaire bron over het neolithicum.", F),
            ("De prent is gemaakt in onze tijd.", J),
            ("Uit de prent weet je zeker hoe dit graf er toen uitzag.", F),
            ("De prent kan helpen om je een voorstelling te maken.", J),
        ],
        "Een primaire bron komt uit de tijd zelf. Deze prent is in onze tijd met een computer gemaakt, en kan fouten bevatten. Ze helpt je om je iets voor te stellen, maar ze bewijst niets.",
    )),
]

H["Bronnen, kunst en beeldvorming — deel 2"] += [
    met("stoomlocomotief.webp", open_(
        "Een klasgenoot gebruikt deze nagemaakte prent in een spreekbeurt als bewijs dat de eerste treinen er zo uitzagen. Wat zeg je tegen hem? Waar zoek je beter?",
        "Het is een prent die met AI gemaakt is, geen foto uit die tijd, dus ze kan fouten bevatten en bewijst niets. Beter zoek je echte foto's, tekeningen of beschrijvingen uit de 19de eeuw, of een trein in een museum. Kijk ook na wie de bron maakte en wanneer.",
    )),
]


# ---------------------------------------------------------------------------
# Stellingen met bronnen en kaarten (26-10-2026). Ouders van wie het echte
# examen geschiedenis aflegde, vonden dit het zwaarst: een stelling met een
# reeks bronnen, en per bron zeggen of ze de stelling bevestigt of nuanceert,
# met een argument. En kaarten herkennen. De bronnen zijn korte, eenvoudige
# beschrijvingen, geen letterlijke citaten. De kaarten tekent kaarten.py.
# ---------------------------------------------------------------------------

BN = ["Bevestigt", "Nuanceert"]


def stelling(tekst, bronnen, uitleg, argument, tegenvoorbeeld=None, zin=None):
    """
    Een casus met een stelling en genummerde bronnen. bronnen is een lijst van
    (tekst, "Bevestigt" of "Nuanceert"). Daarop volgen een tabel per bron, een
    keuzelijst voor het tegenvoorbeeld als dat gegeven is, en een open vraag.

    Met zin = (zin met [[woorden]], extra woorden) wordt het argument een zin
    om aan te vullen in plaats van een open vraag. Kim vond de open vraag op
    27-10-2026 te moeilijk voor ✨ Spark.
    """
    casustekst = f"Stelling: {tekst}\n\n" + "\n\n".join(f"Bron {i}. {b}" for i, (b, _) in enumerate(bronnen, 1))
    vragen = [
        tabel(
            "Bevestigt of nuanceert elke bron de stelling?",
            [(f"Bron {i}", oordeel) for i, (_, oordeel) in enumerate(bronnen, 1)],
            uitleg,
            kolommen=BN,
        )
    ]
    if tegenvoorbeeld:
        nummer, waarom = tegenvoorbeeld
        andere = [str(i) for i in range(1, len(bronnen) + 1) if i != nummer]
        vragen.append(keuze(
            f"Het duidelijkste tegenvoorbeeld voor de stelling staat in bron [[*{nummer}|{'|'.join(andere)}]].",
            waarom,
        ))
    if zin:
        vragen.append(sleep(zin[0], zin[1], argument))
        return casus(casustekst, vragen)
    vragen.append(open_(
        "Bevestig of nuanceer de stelling. Geef een argument en verwijs naar minstens twee bronnen.",
        argument,
        ["Ik bevestig / nuanceer de stelling, want", "Dat zie je in bron"],
    ))
    return casus(casustekst, vragen)


def kaart(prent, vraag):
    vraag["afbeelding_url"] = f"/examenvormen/kaarten/{prent}"
    return vraag


H["Mesopotamië en Egypte — deel 1"] += [
    kaart("oude-nabije-oosten.svg", koppel(
        "Bekijk de kaart. Welke rivier draagt elk nummer?",
        [["Rivier 1", "Nijl"], ["Rivier 2", "Eufraat"], ["Rivier 3", "Tigris"]],
        ["Jordaan", "Tiber"],
        "De Nijl stroomt door Egypte naar de Middellandse Zee. De Eufraat ligt in het westen van Mesopotamië, de Tigris in het oosten. Samen monden ze uit in de Perzische Golf.",
    )),
    klik(
        "Klik op de kaart op het gebied dat Mesopotamië heette.",
        "kaarten/oude-nabije-oosten.svg",
        [[60.0, 14.1, 18.7, 35.3]],
        "Mesopotamië betekent het land tussen de rivieren: het ligt tussen de Eufraat en de Tigris, in het huidige Irak.",
    ),
    stelling(
        "In Mesopotamië schreef men vooral verhalen op.",
        [
            ("De oudste kleitabletten uit de stad Uruk, van rond 3200 v.C., zijn lijsten met hoeveelheden graan, schapen en arbeiders.", "Nuanceert"),
            ("Tempels hielden met tekens op klei bij wie hoeveel graan of vee had binnengebracht.", "Nuanceert"),
            ("Later schreef men in spijkerschrift ook het lange verhaal van Gilgamesj op, een koning die op zoek gaat naar het eeuwige leven.", "Bevestigt"),
            ("Koning Hammurabi van Babylon liet rond 1750 v.C. zijn wetten op een grote stenen zuil uithouwen.", "Nuanceert"),
        ],
        "Alleen bron 3 gaat over een verhaal. De bronnen 1 en 2 tonen dat het schrift vooral diende om bij te houden wat er binnenkwam, en bron 4 gaat over wetten.",
        "Ik nuanceer de stelling. Er werden wel verhalen opgeschreven, zoals dat van Gilgamesj in bron 3. Maar de oudste tabletten in bron 1 en de tempels in bron 2 tonen dat men vooral bijhield hoeveel graan en vee er was. Ook wetten werden opgeschreven, zoals in bron 4.",
        (1, "Bron 1 toont dat de oudste teksten helemaal geen verhalen waren, maar lijsten van graan, schapen en arbeiders."),
    ),
]

H["Mesopotamië en Egypte — deel 2"] += [
    stelling(
        "De farao had alle macht in Egypte.",
        [
            ("Op de muren van tempels staat de farao veel groter afgebeeld dan alle andere mensen.", "Bevestigt"),
            ("De Egyptenaren zagen de farao als een zoon van de zonnegod Ra.", "Bevestigt"),
            ("Een papyrus vertelt dat de arbeiders die de graven van de farao bouwden, rond 1157 v.C. het werk neerlegden omdat hun graan te laat kwam.", "Nuanceert"),
            ("De priesters van de god Amon in Thebe werden zo rijk en machtig dat ze later zelf over het zuiden van Egypte heersten.", "Nuanceert"),
        ],
        "De bronnen 1 en 2 tonen hoe groot de farao gezien werd. Bron 3 toont dat zelfs gewone arbeiders druk konden zetten, en bron 4 dat de priesters macht naar zich toe trokken.",
        "Ik nuanceer de stelling. De farao had veel macht en werd als zoon van een god gezien, dat zie je in bron 1 en 2. Maar alle macht had hij niet: de arbeiders in bron 3 legden het werk neer, en de priesters in bron 4 werden zelf heersers.",
    ),
]

H["Het oude Griekenland — deel 1"] += [
    kaart("griekse-wereld.svg", koppel(
        "Bekijk de kaart. Welke plaats staat bij elke letter?",
        [["Plaats A", "Athene"], ["Plaats B", "Sparta"], ["Plaats C", "Olympia"]],
        ["Troje", "Rome"],
        "Athene ligt in Attika, aan de Egeïsche Zee. Sparta en Olympia liggen allebei op de Peloponnesos: Sparta in het zuiden, Olympia in het westen.",
    )),
    klik(
        "Klik op de kaart op de Peloponnesos, het schiereiland in het zuiden van Griekenland.",
        "kaarten/griekse-wereld-leeg.svg",
        [[13.5, 33.3, 40.4, 60.0]],
        "De Peloponnesos is het grote schiereiland onderaan, met Sparta en Olympia. Het is alleen met een smalle strook land met de rest van Griekenland verbonden.",
    ),
    stelling(
        # Eerst "In Athene mocht iedereen mee beslissen", maar dan bevestigen
        # bron 1 en 2 een stelling die gewoon fout is (Kim, 27-10-2026).
        "In Athene besliste het volk zelf over de stad.",
        [
            ("In de volksvergadering kon elke burger het woord nemen en mee stemmen over wetten en oorlog.", "Bevestigt"),
            ("Veel ambten werden door loting verdeeld, zodat elke burger eens aan de beurt kon komen.", "Bevestigt"),
            ("Alleen volwassen mannen van wie de ouders Atheners waren, waren burger. Vrouwen mochten niet stemmen.", "Nuanceert"),
            ("Slaven en vreemdelingen die in Athene woonden, mochten niet naar de volksvergadering.", "Nuanceert"),
        ],
        "De bronnen 1 en 2 tonen hoe burgers mee beslisten. De bronnen 3 en 4 tonen dat lang niet iedereen burger was.",
        "Burgers konden echt mee beslissen in de volksvergadering en via loting, zoals bron 1 en 2 tonen. Maar vrouwen, slaven en vreemdelingen waren geen burger en mochten niet stemmen, dat zie je in bron 3 en 4. Het grootste deel van de inwoners deed dus niet mee. Daarom nuanceer je de stelling.",
        zin=(
            "Ik [[nuanceer]] de stelling. Volgens bron 1 en 2 konden de [[burgers]] zelf stemmen en een ambt krijgen. Maar bron 3 en 4 tonen dat [[vrouwen]], slaven en vreemdelingen niet mochten meedoen.",
            ["bevestig", "koningen", "soldaten"],
        ),
    ),
]

H["Het oude Griekenland — deel 2"] += [
    stelling(
        "Athene en Sparta waren altijd vijanden.",
        [
            ("Van 431 tot 404 v.C. vochten Athene en Sparta tegen elkaar in de Peloponnesische Oorlog.", "Bevestigt"),
            ("In 480 v.C. vochten Atheners en Spartanen samen tegen de Perzen. Bij Salamis versloeg hun vloot de Perzische.", "Nuanceert"),
            ("Op de Olympische Spelen kwamen sporters uit alle Griekse stadstaten samen, ook uit Athene en Sparta. Tijdens de Spelen mocht er niet gevochten worden.", "Nuanceert"),
            ("De Atheense geschiedschrijver Thucydides schreef dat Sparta bang werd van de groeiende macht van Athene.", "Bevestigt"),
        ],
        "De bronnen 1 en 4 gaan over de strijd tussen beide steden. De bronnen 2 en 3 tonen momenten waarop ze samenwerkten of vrede hielden.",
        "Ik nuanceer de stelling. Ze waren vaak rivalen en voerden lang oorlog, dat zie je in bron 1 en 4. Maar tegen de Perzen vochten ze samen, zoals in bron 2, en op de Olympische Spelen kwamen ze vreedzaam samen, zoals in bron 3. Ze waren dus niet altijd vijanden.",
        (2, "Bron 2 toont een moment waarop Athene en Sparta samen tegen een gemeenschappelijke vijand vochten."),
    ),
]

H["Het Romeinse Rijk — deel 1"] += [
    kaart("romeinse-rijk.svg", koppel(
        "Bekijk de kaart. Welke stad staat bij elke letter?",
        [["Stad A", "Rome"], ["Stad B", "Carthago"], ["Stad C", "Constantinopel"], ["Stad D", "Alexandrië"]],
        ["Athene"],
        "Rome ligt in het midden van Italië. Carthago lag in Noord-Afrika, recht tegenover Sicilië. Constantinopel ligt tussen Europa en Azië, en Alexandrië aan de monding van de Nijl.",
    )),
    # Eerst een klikvraag op de zee, maar die zee is te grillig voor rechthoekige
    # klikvakken: Kim vond het lappendeken raar (27-10-2026). Nu een keuzelijst.
    kaart("romeinse-rijk.svg", keuze(
        "Bekijk de kaart. Alle steden liggen aan dezelfde zee. De Romeinen noemden die [[*Middellandse Zee|Zwarte Zee|Noordzee]] mare nostrum, wat [[*onze zee|de grote zee|de vreemde zee]] betekent.",
        "Mare nostrum is de Middellandse Zee. Alle steden op de kaart liggen eraan, en het Romeinse Rijk lag er helemaal rond.",
    )),
    stelling(
        "Het Romeinse Rijk werd groot alleen door oorlog.",
        [
            ("Julius Caesar veroverde met zijn legioenen tussen 58 en 50 v.C. heel Gallië.", "Bevestigt"),
            ("In drie Punische oorlogen versloeg Rome Carthago en nam het zijn gebieden over.", "Bevestigt"),
            ("In 133 v.C. liet de koning van Pergamon, in het huidige Turkije, zijn rijk bij testament na aan Rome.", "Nuanceert"),
            ("Steden en volken die zich aansloten, mochten vaak hun eigen bestuur houden en konden Romeins burger worden.", "Nuanceert"),
        ],
        "De bronnen 1 en 2 gaan over veroveringen. Bron 3 toont een gebied dat zonder oorlog bij Rome kwam, en bron 4 hoe Rome volken aan zich bond.",
        "Ik nuanceer de stelling. Rome veroverde veel met oorlog, zoals Gallië in bron 1 en Carthago in bron 2. Maar Pergamon kwam er zonder strijd bij, door een testament, zoals bron 3 toont. En volgens bron 4 konden volken burger worden, waardoor ze bij Rome wilden horen.",
        (3, "Bron 3 toont een rijk dat zonder enige oorlog bij Rome kwam: de koning liet het na in zijn testament."),
    ),
]

H["Het Romeinse Rijk — deel 2"] += [
    stelling(
        "In 476 hield het Romeinse Rijk op te bestaan.",
        [
            ("In 476 zette de Germaanse legeraanvoerder Odoaker de laatste keizer in het westen af.", "Bevestigt"),
            ("Het Oost-Romeinse Rijk, met Constantinopel als hoofdstad, bleef bestaan tot 1453.", "Nuanceert"),
            ("Het Latijn bleef nog eeuwenlang de taal van de Kerk en van geleerden. Het Frans, het Italiaans en het Spaans komen eruit voort.", "Nuanceert"),
            ("Het westen was al lang voor 476 verzwakt. In 410 plunderden de Visigoten de stad Rome.", "Nuanceert"),
        ],
        "Bron 1 geeft het jaar 476. Bron 2 toont dat het rijk in het oosten nog bijna duizend jaar bleef, bron 3 dat de Romeinse taal bleef, en bron 4 dat het einde in het westen al veel vroeger begon.",
        "Ik nuanceer de stelling. In het westen kwam in 476 wel een einde aan het rijk, zoals bron 1 toont. Maar in het oosten bleef het bestaan tot 1453, volgens bron 2. En veel van Rome leefde voort, zoals het Latijn in bron 3.",
        (2, "Bron 2 toont dat een deel van het Romeinse Rijk nog bijna duizend jaar na 476 bleef bestaan."),
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

# -*- coding: utf-8 -*-
"""De leerbundels voor kunstbeschouwing en filosofie op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche kunstbeschouwing en filosofie 2DO, geldig vanaf
1 januari 2027. Het vak valt in twee helften uiteen: kunstbeschouwing en
filosofie. De zestien thema's volgen die verdeling, zes en tien.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py
../../boost-doorstroom/kunstbeschouwing-en-filosofie.json` doet daar het
voorwerk voor, nadat je de html gebouwd hebt.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, want een titel alleen is binnen een vak geen sleutel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Kunstbeschouwing en filosofie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. Kunst als deel van een cultuur
zet("kunst-als-deel-van-een-cultuur",
    titel="Kunst als deel van een cultuur",
    onder="Cultuur in de enge en de brede betekenis, het verschil tussen een cultuuruiting en een kunstuiting, en de vijf criteria waarmee je beredeneert of iets kunst is.",
    secties=[
        dict(kop="Cultuur in twee betekenissen", blokken=[
            ("p", "Het woord cultuur betekent niet altijd hetzelfde, en daarom begint dit vak ermee. De "
                  "fiche onderscheidt een enge en een brede betekenis."),
            ("kader", tabel(["betekenis", "wat ze omvat", "voorbeelden"],
                            [["de <strong>enge</strong> betekenis", "<strong>kunst en wetenschap</strong>, en erfgoed: het verfijnde deel van een cultuur",
                              "<strong>een opera</strong>, <strong>een roman</strong>, <strong>een museumstuk</strong>"],
                             ["de <strong>brede</strong> betekenis", "<strong>alles wat mensen maken</strong>: alles wat niet puur natuur is",
                              "taal, eten, kleding, gewoontes, godsdienst, techniek én kunst"]])),
            ("p", "Volgens de brede betekenis horen dus <strong>een feestdag</strong>, <strong>een "
                  "eetgewoonte</strong> en <strong>een begroeting</strong> bij de cultuur. <strong>Koken "
                  "hoort erbij</strong>, want het is door mensen bedacht en doorgegeven, en "
                  "<strong>een taal</strong> ook: mensen hebben ze gevormd en geven ze door. Een "
                  "<strong>groep die elk jaar hetzelfde gerecht eet op een feestdag</strong>, houdt zo een "
                  "<strong>cultuuruiting</strong> in leven. Ook <strong>een reclamespot valt niet buiten "
                  "de cultuur</strong>: hij is door mensen gemaakt en zegt iets over een samenleving."),
            ("p", "<strong>Cultuur in de enge betekenis omvat de verkeersregels niet.</strong> Die horen bij "
                  "de brede betekenis; de enge blijft bij kunst, wetenschap en erfgoed. Een bushalte is ook "
                  "cultuur, maar in de brede zin."),
            ("p", "Het geheel van gewoontes dat een groep doorgeeft, heet <strong>cultuur</strong>: alles "
                  "wat een groep heeft gemaakt en overdraagt aan de volgende generatie."),
            ("kader", "Waarom dat onderscheid nuttig is: <strong>het voorkomt verwarring</strong>. Wie over "
                      "cultuur spreekt, bedoelt soms een museum en soms een hele leefwijze, en dat moet "
                      "duidelijk zijn voor je een gesprek begint."),
        ]),
        dict(kop="Natuur, cultuur en kunst", blokken=[
            ("p", "<strong>Natuur is geen cultuur</strong>, want <strong>geen mens maakte ze</strong>. "
                  "Cultuur is wat de mens eraan toevoegt: een berg is natuur, een pad op die berg is "
                  "cultuur. <strong>Een vulkaanuitbarsting</strong>, <strong>een zonsverduistering</strong> "
                  "en <strong>een getijdenwerking</strong> zijn dus geen cultuur; een volkslied wel."),
            ("p", "Tussen cultuur en kunst zit een duidelijke richting: <strong>elke kunstuiting is ook een "
                  "cultuuruiting</strong>, want kunst is door mensen gemaakt. Omgekeerd geldt het niet: "
                  "<strong>niet elke cultuuruiting is kunst</strong>. Een bushokje of een recept is geen "
                  "kunst."),
            ("p", "Een uiting die mensen maakten maar die geen kunst is, heet dus gewoon een "
                  "<strong>cultuuruiting</strong>. Wil je weten of ze ook als kunst geldt, dan onderzoek je "
                  "dat <strong>met de kunstcriteria</strong>."),
            ("weetje", "Een <strong>kerk uit de twaalfde eeuw</strong> is <strong>een kunst- én een "
                       "cultuuruiting</strong>: ze is gebouwd door mensen, dus cultuur, en ze wordt als "
                       "architectuur beschouwd, dus ook kunst."),
            ("p", "Daarom bestudeert kunstbeschouwing eerst het begrip cultuur: <strong>kunst zit in een "
                  "cultuur</strong>. Een kunstwerk is niet los te lezen van de cultuur waarin het ontstond."),
        ]),
        dict(kop="De vijf kunstcriteria", blokken=[
            ("p", "De fiche noemt <strong>vijf</strong> kunstcriteria. Ouderdom staat er niet bij: een nieuw "
                  "werk kan evengoed kunst zijn."),
            ("kader", tabel(["criterium", "wat het zegt", "de zwakke plek"],
                            [["<strong>economische waarde</strong>", "<strong>kunst is veel geld waard</strong>",
                              "ook rommel kan duur verkocht worden; de markt beslist niet wat kunst is"],
                             ["<strong>emotionele lading</strong>", "kunst raakt mensen: <strong>een werk laat mensen huilen</strong>",
                              "een reclamespot raakt je ook"],
                             ["<strong>esthetische waarde</strong>", "kunst is mooi",
                              "<strong>smaak verschilt</strong>, en veel moderne kunst wil juist niet mooi zijn"],
                             ["<strong>originaliteit</strong>", "kunst is vernieuwend",
                              "een kopie van een meesterwerk haalt dit criterium niet"],
                             ["<strong>vakmanschap</strong>", "<strong>kunst is een ambacht</strong>: technische beheersing",
                              "een traditioneel patroon is vakwerk maar niet vernieuwend"]])),
            ("p", "Bij <strong>vakmanschap</strong> horen vragen als <strong>welke techniek gebruikte "
                  "hij</strong>, <strong>hoe lang werkte hij eraan</strong> en <strong>hoe moeilijk is het "
                  "na te maken</strong>. De opbrengst hoort niet in dat rijtje; dat is de economische "
                  "waarde."),
            ("p", "Drie criteria kan je deels nameten, in geld of in techniek: <strong>de economische "
                  "waarde</strong>, <strong>het vakmanschap</strong> en <strong>de originaliteit</strong>. "
                  "Of iets mooi is, blijft een smaakoordeel. Daarom is <strong>de esthetische waarde</strong> "
                  "het moeilijkste criterium, en meteen ook het criterium dat <strong>het sterkst "
                  "verschuift met de tijd</strong>: de impressionisten werden eerst uitgelachen en hangen "
                  "nu overal."),
        ]),
        dict(kop="Hoe je de criteria gebruikt", blokken=[
            ("p", "<strong>Een werk moet niet alle vijf de criteria halen om kunst te zijn.</strong> De "
                  "criteria zijn argumenten in een gesprek, geen vijf voorwaarden, en vaak haalt een werk er "
                  "maar enkele. <strong>Ze geven dan ook geen sluitend antwoord</strong> op de vraag wat "
                  "kunst is: ze geven argumenten om het te beredeneren, en een sluitend antwoord bestaat "
                  "niet."),
            ("p", "Men gebruikt er meerdere naast elkaar omdat <strong>één criterium te smal is</strong>. "
                  "Wie enkel op schoonheid let, mist de maatschappijkritische kunst; wie enkel op geld let, "
                  "mist bijna alles. <strong>Een werk dat niemand mooi vindt, kan dus toch kunst zijn</strong>: "
                  "het kan vernieuwend zijn of hevige emoties oproepen."),
            ("kader", tabel(["voorbeeld", "het sterkste argument"],
                            [["<strong>een urinoir in een museum</strong>",
                              "<strong>de originaliteit</strong>: het werk van Duchamp vernieuwde het hele idee van kunst; van ambacht of schoonheid is er weinig te zien"],
                             ["<strong>een handgeweven tapijt uit een dorp</strong>",
                              "<strong>het vakmanschap</strong>: het weven vraagt jaren oefening, maar het patroon is traditioneel en dus niet vernieuwend"]])),
            ("p", "Daarom vraagt de fiche om een cultuuruiting met de criteria te analyseren: <strong>zo "
                  "beredeneer je een oordeel</strong>. Het gaat niet om gelijk krijgen maar om een "
                  "onderbouwd antwoord, en dat is wat het examen vraagt. Twisten <strong>twee mensen of "
                  "graffiti kunst is</strong>, dan helpt hen precies hetzelfde: <strong>de vijf criteria "
                  "doorlopen</strong>. Zo wordt een smaakruzie een gesprek met argumenten."),
        ]),
    ])


# ───────────────────────── 2. De kunstvormen
zet("de-kunstvormen",
    titel="De kunstvormen",
    onder="De vijf kunstvormen van de vakfiche, waaraan je elk ervan herkent, en hoe je een werk benoemt dat aan meer dan één vorm raakt.",
    secties=[
        dict(kop="Vijf kunstvormen", blokken=[
            ("p", "De vakfiche onderscheidt <strong>vijf</strong> kunstvormen. Er is geen rangorde: geen "
                  "enkele vorm staat boven een andere."),
            ("kader", tabel(["kunstvorm", "wat ertoe hoort", "voorbeelden"],
                            [["<strong>architectuur en design</strong>", "wat vormgegeven is én gebruikt wordt",
                              "<strong>een stadhuis uit de zestiende eeuw</strong>, <strong>een woonhuis van een architect</strong>, <strong>een affiche voor een festival</strong>, een stoel van een ontwerper"],
                             ["<strong>audiovisuele kunsten</strong>", "<strong>film</strong>, <strong>fotografie</strong> en <strong>videokunst</strong>",
                              "<strong>een kortfilm</strong>, <strong>een fotoreeks</strong>, <strong>een videoinstallatie</strong>"],
                             ["<strong>beeldende kunsten</strong>", "<strong>schilderkunst</strong>, <strong>beeldhouwkunst</strong>, <strong>tekenkunst</strong>",
                              "<strong>een olieverfdoek</strong>, <strong>een marmeren buste</strong>, <strong>een houtsnede</strong>, een fresco, een striptekening"],
                             ["<strong>literatuur</strong>", "de kunstvorm die <strong>met taal</strong> werkt",
                              "romans, verhalen, <strong>een gedicht</strong>, toneelteksten"],
                             ["<strong>podiumkunsten</strong>", "<strong>dans</strong>, <strong>theater</strong>, <strong>muziek</strong>",
                              "<strong>een concert</strong>, <strong>een toneelstuk</strong>, <strong>een dansvoorstelling</strong>, een ballet"]])),
            ("p", "<strong>Architectuur staat samen met design als één kunstvorm.</strong> Zo staat het op de "
                  "fiche, en met reden: beide geven vorm aan iets wat ook gebruikt wordt. Design hoort bij de "
                  "kunstvormen omdat <strong>het vorm geeft aan voorwerpen</strong>: een stoel of een affiche "
                  "kan vormgegeven zijn met dezelfde zorg als een schilderij. <strong>Een stoel van een "
                  "ontwerper valt dus niet buiten de kunstvormen</strong>; of die stoel ook kúnst is, "
                  "beredeneer je met de criteria."),
            ("p", "<strong>Fotografie hoort niet bij de beeldende kunsten</strong> maar bij de audiovisuele, "
                  "naast film en videokunst. En <strong>videokunst en film zijn niet precies dezelfde "
                  "zaak</strong>: ze staan als aparte onderdelen binnen dezelfde kunstvorm, want videokunst "
                  "is meestal voor een zaal bedoeld en niet voor een bioscoop. <strong>Een striptekening is "
                  "ook geen podiumkunst</strong>: ze hoort bij de beeldende kunsten, en met de tekst erbij "
                  "raakt ze aan de literatuur."),
        ]),
        dict(kop="Wat de vormen van elkaar onderscheidt", blokken=[
            ("p", "De scherpste scheidslijn loopt tussen wat blijft en wat voorbijgaat. <strong>De "
                  "beeldende kunsten</strong>, <strong>de architectuur</strong> en <strong>het design</strong> "
                  "laten een tastbaar werk na; een voorstelling is na het applaus voorbij. Wat de "
                  "podiumkunsten gemeen hebben, is dan ook dat <strong>ze in de tijd gebeuren</strong>: een "
                  "voorstelling duurt en is daarna voorbij, terwijl een schilderij blijft hangen."),
            ("p", "Daar hangt nog iets aan vast: de podiumkunst <strong>heeft een uitvoerder nodig naast de "
                  "maker</strong>. Een partituur of een toneeltekst wordt pas kunst als iemand ze uitvoert."),
            ("p", "<strong>De architectuur</strong> is de vorm die meebouwt aan de ruimte waarin mensen "
                  "leven: een gebouw is kunst die je binnengaat. Juist daarom krijgen <strong>beeldende "
                  "kunst en architectuur eigen richtvragen</strong> in de fiche — <strong>ze hebben eigen "
                  "middelen</strong>, en bijlage 1 en 2 geven voor elk een eigen lijst bouwstenen, "
                  "materialen en technieken."),
            ("p", "De indeling is nuttig omdat <strong>ze ordent wat je ziet</strong>: wie weet met welke "
                  "vorm hij te doen heeft, weet ook welke richtvragen hij kan stellen."),
        ]),
        dict(kop="Werken die aan meer dan één vorm raken", blokken=[
            ("p", "Over de kunstvormen klopt: <strong>ze overlappen soms</strong>, <strong>elke vorm heeft "
                  "eigen middelen</strong> en <strong>de fiche noemt er vijf</strong>."),
            ("p", "<strong>Eén werk kan tot meerdere kunstvormen horen.</strong> Een opera is muziek, "
                  "theater én vormgeving, en een film heeft ook literatuur nodig voor het scenario. Daarom "
                  "noemt men een film een <strong>samengestelde</strong> kunstvorm: <strong>meerdere kunsten "
                  "komen samen</strong> in één werk, wat de analyse rijker maakt."),
            ("p", "Het is dus soms moeilijk één vorm aan te wijzen, want <strong>de vormen lopen door "
                  "elkaar</strong>. Een installatie met beeld, geluid en voorwerpen raakt aan drie vormen "
                  "tegelijk, en dan benoem je er meerdere. De fiche laat dat uitdrukkelijk toe."),
            ("kader", tabel(["werk", "welke vorm of vormen"],
                            [["<strong>een bronzen ruiterbeeld op een plein</strong>",
                              "<strong>beeldende kunst</strong> (beeldhouwkunst); het plein zelf is architectuur"],
                             ["<strong>een fresco op een kerkmuur</strong>",
                              "<strong>de schilderkunst</strong>, dus beeldende kunst; de kerk eromheen is architectuur"],
                             ["<strong>een luisterspel op de radio</strong>",
                              "<strong>literatuur en muziek</strong>: een tekst gespeeld met geluid, zonder beeld"],
                             ["<strong>een geluidswerk zonder beeld in een museumzaal</strong>",
                              "<strong>bij de muziek</strong>, ook al staat er niemand op een podium; de fiche laat zulke grensgevallen toe"],
                             ["<strong>dansers die bewegen tussen de beelden van een kunstenaar</strong>",
                              "<strong>beeldende kunst en podiumkunst</strong>, twee vormen tegelijk"]])),
        ]),
        dict(kop="Waar de kunstvorm in de analyse staat", blokken=[
            ("p", "<strong>Een kunstvorm bepalen is een stap in de analyse</strong>, en wel de eerste "
                  "ordening. Daarna volgen <strong>de periode en de stroming</strong> — de fiche vraagt die "
                  "met bronmateriaal te bepalen — en daarna de inhoud en de context."),
        ]),
    ])


# ───────────────────────── 3. Kunst van de prehistorie tot de middeleeuwen
zet("kunst-van-de-prehistorie-tot-de-middeleeuwen",
    titel="Kunst van de prehistorie tot de middeleeuwen",
    onder="De periodes in de orde van de tijd: grotkunst, Egypte en het nabije Oosten, de Griekse en Romeinse oudheid, en de Romaanse en gotische middeleeuwen.",
    secties=[
        dict(kop="Waarom periodes", blokken=[
            ("p", "Periodes zijn nuttig omdat <strong>ze een werk in de tijd plaatsen</strong>. De fiche "
                  "vraagt om met bronmateriaal te bepalen tot welke periode en welke stroming een werk "
                  "hoort, en dat is de tweede stap in de analyse, na de kunstvorm."),
            ("p", "De periodes staan in de <strong>orde van de tijd</strong>: prehistorie, Egypte en nabije "
                  "Oosten, de klassieke oudheid, de middeleeuwen, en zo verder. Daarom staat de klassieke "
                  "oudheid tussen Egypte en de middeleeuwen: <strong>de fiche volgt de tijd</strong>. En "
                  "<strong>prehistorische kunst is dus niet jonger dan de Egyptische</strong> maar veel "
                  "ouder; ze staat vooraan."),
            ("kader", "Sta je voor een werk uit een periode die je niet kent, dan helpen drie vragen: "
                      "<strong>welk materiaal is gebruikt</strong>, <strong>welk onderwerp is "
                      "afgebeeld</strong> en <strong>welke techniek is gebruikt</strong>. Materiaal, "
                      "onderwerp en techniek brengen een werk thuis. De prijs zegt daar niets over."),
        ]),
        dict(kop="De prehistorie", blokken=[
            ("p", "De bekendste prehistorische schilderkunst vind je <strong>op grotwanden</strong>, in "
                  "<strong>grotten</strong> als Lascaux en Altamira — vandaar de namen grotschilderingen en "
                  "rotskunst. Opvallend: de kunst zat diep in de grot, niet bij de woonplek."),
            ("p", "Ze beeldde vooral <strong>dieren</strong> af: <strong>stieren</strong>, "
                  "<strong>paarden</strong>, <strong>herten</strong> en <strong>bizons</strong> zijn de "
                  "bekendste. Mensen komen er veel minder op voor."),
            ("p", "<strong>Van die periode is ook beeldhouwkunst bewaard</strong>: kleine beeldjes in "
                  "<strong>steen</strong>, <strong>been</strong> en <strong>ivoor</strong>, zoals de "
                  "vrouwenfiguurtjes die men venusbeeldjes noemt. Brons komt pas veel later, in de "
                  "bronstijd. Een <strong>beeldje van been met een menselijke vorm, duizenden jaren "
                  "oud</strong>, hoort dus bij <strong>de prehistorie</strong>: het materiaal, de kleine "
                  "vorm en het ontbreken van schrift wijzen alle drie die kant uit."),
            ("p", "Waarom men niet zeker weet waarvoor grotkunst diende? <strong>Er zijn geen teksten.</strong> "
                  "Schrift bestond nog niet, dus over de bedoeling kan men alleen redeneren, niet lezen."),
        ]),
        dict(kop="Egypte en het nabije Oosten", blokken=[
            ("p", "<strong>De kunst van het nabije Oosten staat niet los van die van Egypte</strong>: de "
                  "fiche noemt ze als één onderdeel, kunst van Egypte en nabije Oosten."),
            ("p", "De Egyptische kunst heeft drie kenmerken: <strong>strakke vaste regels</strong>, "
                  "<strong>veel aandacht voor het hiernamaals</strong> en <strong>figuren in een vast "
                  "schema</strong>. Dat ze duizenden jaren opvallend gelijk bleef, is net haar kenmerk."),
            ("p", "<strong>Ze diende vaak voor het graf en het hiernamaals</strong>: beelden, "
                  "wandschilderingen en voorwerpen gingen mee in het graf om de dode verder te helpen. "
                  "Daarom noemt men die kunst <strong>functioneel</strong>: <strong>ze diende een "
                  "doel</strong> — de dode begeleiden of de macht van de farao tonen. Schoonheid alleen was "
                  "niet de bedoeling. Het koningsgraf bij uitstek is de <strong>piramide</strong>; later "
                  "groef men de graven uit in de rotsen van de Vallei der Koningen."),
            ("p", "Een mens wordt doorgaans afgebeeld met het <strong>hoofd van de zijkant</strong>: hoofd "
                  "en benen van de zijkant, schouders en oog van voren. Elk lichaamsdeel krijgt zijn meest "
                  "kenbare kant. Die beeldtaal bleef zo lang gelijk omdat <strong>de regels heilig "
                  "waren</strong>: de vormen hoorden bij de godsdienst en de macht, en vernieuwing was er "
                  "niet de bedoeling."),
            ("p", "Van het nabije Oosten — Mesopotamië, Assyrië en Perzië — zijn vooral <strong>reliëfs van "
                  "paleizen</strong>, <strong>zegels in steen</strong> en <strong>beelden van "
                  "heersers</strong> bewaard. De Assyrische paleisreliëfs laten vooral <strong>de macht van "
                  "de koning</strong> zien: jachttaferelen en veldslagen waarin hij overwint. Kunst in "
                  "dienst van de macht."),
        ]),
        dict(kop="De klassieke oudheid: Grieks en Romeins", blokken=[
            ("p", "Met de klassieke oudheid bedoelt de fiche de <strong>Griekse en Romeinse</strong> kunst. "
                  "Romaans en gotisch zijn middeleeuws en horen hier niet bij — let op die twee woorden, ze "
                  "lijken op elkaar maar liggen eeuwen uit elkaar."),
            ("kader", tabel(["", "Grieks", "Romeins"],
                            [["waar het naar streeft", "<strong>een ideale verhouding</strong>: harmonie en evenwicht in het lichaam, volgens vaste maatverhoudingen",
                              "het levensechte portret: de mens zoals hij is"],
                             ["typische werken", "<strong>de tempel met zuilen</strong>, <strong>het marmeren atletenbeeld</strong>, <strong>de beschilderde vaas</strong>",
                              "<strong>een rondboog</strong>, <strong>een koepel</strong>, <strong>een aquaduct</strong>, de buste"],
                             ["techniek", "de zuil en de architraaf", "<strong>de rondboog</strong>, <strong>de koepel</strong> en <strong>het beton</strong>"]])),
            ("p", "<strong>De Romeinen namen veel over van de Griekse kunst.</strong> Ze kopieerden Griekse "
                  "beelden — veel Griekse werken kennen we enkel door hun kopieën — en namen bouwvormen "
                  "over, maar hun portretten zijn wel hun eigen vondst. Een <strong>marmeren buste van een "
                  "oude man met rimpels</strong> is dus <strong>Romeins</strong>: de Grieken maakten de mens "
                  "juist ideaal."),
            ("p", "De spitsboog hoort niet bij de Romeinen en het kruisribgewelf niet bij hen: die twee "
                  "komen pas in de gotiek."),
        ]),
        dict(kop="De middeleeuwen: Romaans en gotisch", blokken=[
            ("p", "De middeleeuwse kunst stond <strong>in dienst van de kerk</strong>, niet van de handel: "
                  "kerken, glasramen, beelden en handschriften voor de eredienst."),
            ("p", "Middeleeuwse figuren zijn vaak niet natuurgetrouw, en dat is geen onvermogen: <strong>de "
                  "boodschap woog zwaarder</strong>. Belangrijke figuren werden groter getekend, want het "
                  "verhaal en de rangorde kwamen voor de werkelijkheid."),
            ("p", "Binnen de middeleeuwen komt <strong>de gotiek na de Romaanse</strong> kunst, niet "
                  "ervoor: eerst Romaans met de rondboog, dan gotisch met de spitsboog. Romaans is de "
                  "vroege middeleeuwen, gotisch de late."),
            ("kader", tabel(["", "Romaans", "gotisch"],
                            [["de boogvorm", "<strong>de rondboog</strong>, overgenomen van de Romeinen — vandaar de naam", "<strong>de spitsboog</strong>"],
                             ["de muren", "<strong>dikke muren</strong>", "dunnere muren, want <strong>de last gaat naar pijlers</strong>"],
                             ["de vensters", "<strong>kleine vensters</strong>", "grote vensters en glasramen"],
                             ["de indruk", "<strong>zwaar en gesloten</strong>", "hoog en licht"]])),
            ("p", "<strong>Een gotische kerk heeft dus grotere vensters dan een Romaanse.</strong> "
                  "Spitsbogen, kruisribgewelven en luchtbogen brengen de last naar de pijlers, en dan mag de "
                  "muur open. Daarom kon de gotiek ook hoger bouwen: <strong>de last ging naar "
                  "pijlers</strong>, langs kruisribgewelven, luchtbogen en steunberen naar beneden."),
            ("p", "Wat die hoge kerken wilden uitdrukken, is <strong>het streven naar de hemel</strong>: "
                  "hoogte en licht moesten de gelovige naar boven richten, en daar diende het gekleurde glas "
                  "ook voor."),
            ("p", "Sta je voor <strong>een kerk met spitsbogen en luchtbogen</strong>, dan hoort ze "
                  "<strong>bij de gotiek</strong>. Die twee zijn de duidelijkste gotische kenmerken."),
        ]),
    ])


# ───────────────────────── 4. Kunststromingen van de renaissance tot vandaag
zet("kunststromingen-van-de-renaissance-tot-vandaag",
    titel="Kunststromingen van de renaissance tot vandaag",
    onder="De stromingen van de vroegmoderne, de moderne en de hedendaagse tijd, met de kenmerken waaraan je elk werk thuisbrengt.",
    secties=[
        dict(kop="Drie tijden, elk met hun stromingen", blokken=[
            ("p", "Na de middeleeuwen deelt de fiche de stromingen in drie tijden in. Ze volgen elkaar op in "
                  "de orde van de tijd, en dat is geen willekeur: <strong>elke stroming antwoordt op de "
                  "vorige</strong>. Het realisme reageert op de romantiek, het impressionisme op het "
                  "atelier. Zo hangt de hele rij aan elkaar."),
            ("kader", tabel(["tijd", "stromingen"],
                            [["de <strong>vroegmoderne</strong> tijd", "<strong>renaissance en barok</strong>"],
                             ["de <strong>moderne</strong> tijd", "<strong>romantiek en realisme</strong>, en daarna het impressionisme"],
                             ["de <strong>hedendaagse</strong> tijd", "<strong>popart</strong>, <strong>installatiekunst</strong>, multimediale kunst en <strong>conceptuele kunst</strong>"]])),
            ("p", "Renaissance en barok heten <strong>vroegmodern</strong> omdat <strong>ze tussen oud en "
                  "modern liggen</strong>: ze volgen op de middeleeuwen en komen voor de moderne tijd. De "
                  "romantiek hoort dus niet bij de vroegmoderne tijd, en het impressionisme niet bij de "
                  "hedendaagse."),
            ("p", "Een stroming kennen helpt bij het analyseren omdat <strong>je dan weet waarop te "
                  "letten</strong>: wie weet dat de barok beweging en licht zoekt, ziet die middelen "
                  "sneller in het werk zelf."),
        ]),
        dict(kop="Renaissance en barok", blokken=[
            ("p", "<strong>Renaissance</strong> betekent <strong>wedergeboorte</strong>, en wel van "
                  "<strong>de klassieke oudheid</strong>: van de Griekse en Romeinse vormen en "
                  "verhoudingen. <strong>Ze zette de mens weer centraal</strong> — het menselijk lichaam, "
                  "de verhoudingen en het portret kregen volop aandacht, en dat noemt men "
                  "<strong>humanisme</strong>: het zet de mens en zijn kunnen centraal."),
            ("p", "<strong>In de renaissance werden niet enkel heiligen en vorsten geportretteerd.</strong> "
                  "Ook rijke burgers lieten zich portretteren; het portret werd breder dan de kerk en het "
                  "hof."),
            ("p", "<strong>De barok komt na de renaissance</strong>, niet ervoor. Beide horen bij de "
                  "vroegmoderne tijd."),
            ("kader", tabel(["", "renaissance", "barok"],
                            [["de houding", "<strong>evenwicht en rust</strong>, symmetrie", "<strong>beweging en drama</strong>"],
                             ["de compositie", "strak, met <strong>lijnperspectief</strong>", "<strong>diagonale composities</strong>"],
                             ["het licht", "gelijkmatig", "<strong>sterk licht-donkercontrast</strong>"],
                             ["de rijkdom", "maat en verhouding", "<strong>overvloed en pracht</strong>, rijke stoffen en kleur"],
                             ["kunstenaars", "<strong>Leonardo da Vinci</strong>, <strong>Michelangelo</strong>, <strong>Rafaël</strong>", "<strong>Rubens</strong>"]])),
            ("p", "Het <strong>lijnperspectief</strong> is de techniek waarmee de renaissance diepte gaf "
                  "aan een schilderij: alle lijnen komen samen in één verdwijnpunt."),
            ("p", "De barok wil overtuigen, en gebruikt daarvoor <strong>licht en schaduw</strong>, "
                  "<strong>beweging in de compositie</strong> en <strong>rijke stoffen en kleur</strong>. "
                  "Strakke symmetrie hoort niet in dat rijtje; dat is renaissance. En de vlakke achtergrond "
                  "evenmin: die hoort eerder bij de middeleeuwen."),
            ("p", "<strong>De barok werd ook door de kerk gebruikt om te overtuigen.</strong> Na de "
                  "reformatie wilde de kerk met pracht en emotie de gelovigen raken, en dat paste bij de "
                  "barokke stijl."),
            ("p", "Twee werkjes om het te oefenen. Een <strong>schilderij met rust, symmetrie en een strak "
                  "perspectief</strong> is <strong>renaissance</strong>. Een <strong>schilderij met een "
                  "diagonale beweging en een hard lichtcontrast</strong> is <strong>barok</strong>; Rubens "
                  "is er het bekendste voorbeeld van."),
        ]),
        dict(kop="De moderne tijd: romantiek, realisme en impressionisme", blokken=[
            ("p", "De <strong>romantiek</strong> zocht haar onderwerpen <strong>in gevoel en natuur</strong>: "
                  "gevoel, verlangen, de woeste natuur, het verleden en het verre land. Niet de rede maar de "
                  "ziel. Een <strong>stormachtige zee met een klein schip, vol gevoel</strong>, is dus "
                  "romantiek: de overweldigende natuur met de kleine mens erin."),
            ("p", "<strong>Het realisme schilderde het gewone leven zoals het was</strong>: boeren, "
                  "arbeiders en armoede, zonder verfraaiing. Voor velen was dat een schok. Een "
                  "<strong>schilderij van zware veldarbeid zonder opsmuk</strong> is dan ook "
                  "<strong>realisme</strong>."),
            ("p", "Het <strong>impressionisme</strong> legt <strong>de indruk van een ogenblik</strong> "
                  "vast — naar het Franse <em>impression</em>. De kenmerken: <strong>losse "
                  "toetsen</strong>, <strong>licht en kleur</strong>, en <strong>werken in de open "
                  "lucht</strong>. Een strakke lijn stoorde daarbij."),
            ("kader", "<strong>De impressionisten werden bij hun eerste tentoonstellingen niet geprezen "
                      "maar uitgelachen</strong> en geweigerd. De naam impressionisme was eerst een "
                      "spotnaam. Dat is meteen het beste voorbeeld bij het criterium esthetische waarde: "
                      "wat mooi heet, verschuift."),
        ]),
        dict(kop="De hedendaagse tijd", blokken=[
            ("p", "Over de hedendaagse stromingen klopt: <strong>ze rekken het begrip kunst op</strong>, "
                  "<strong>ze gebruiken nieuwe dragers</strong> en <strong>ze vragen uitleg bij het "
                  "werk</strong>. Vaste regels zijn er juist niet meer; elke kunstenaar kiest zijn eigen "
                  "middelen."),
            ("kader", tabel(["stroming", "waaraan je ze herkent", "voorbeeld"],
                            [["<strong>popart</strong>", "ze haalt haar beelden <strong>uit de reclame</strong>, uit strips, blikjes en filmsterren",
                              "<strong>een blikje soep, honderd keer gezeefdrukt</strong>; Andy Warhol"],
                             ["<strong>installatiekunst</strong>", "<strong>ze vult een ruimte</strong>: de bezoeker stapt in het werk",
                              "<strong>een zaal vol voorwerpen waar je tussen wandelt</strong>"],
                             ["multimediale kunst", "ze combineert dragers: <strong>beeld</strong>, <strong>geluid</strong>, <strong>computer en licht</strong>",
                              "juist het combineren is haar kenmerk"],
                             ["<strong>conceptuele kunst</strong>", "<strong>het idee weegt zwaarder dan het voorwerp</strong>",
                              "het werk kan een tekst of een instructie zijn; soms blijft er bijna niets over"]])),
            ("p", "<strong>Hedendaagse kunst vraagt niet altijd groot vakmanschap.</strong> Bij conceptuele "
                  "kunst weegt het idee zwaarder dan het ambacht, en juist daarom is vakmanschap maar één "
                  "criterium van de vijf."),
        ]),
    ])


# ───────────────────────── 5. Samenlevingen, inhoud en context van een kunstuiting
zet("samenlevingen-inhoud-en-context-van-een-kunstuiting",
    titel="Samenlevingen, inhoud en context van een kunstuiting",
    onder="Westerse en niet-westerse kunst, de zeven functies van een kunstuiting, en hoe inhoud en context samen verklaren wat je ziet.",
    secties=[
        dict(kop="Kunst uit diverse samenlevingen", blokken=[
            ("p", "Bij diverse samenlevingen maakt de fiche één groot onderscheid: <strong>westers en "
                  "niet-westers</strong>. Je bekijkt kunst uit meerdere samenlevingen omdat <strong>kunst "
                  "niet enkel westers</strong> is: elke samenleving kent kunst, met eigen vormen, materialen "
                  "en bedoelingen."),
            ("p", "Als niet-westerse kunst noemt de fiche <strong>Arabische kunst</strong>, <strong>Afrikaanse "
                  "kunst</strong> en <strong>japonisme</strong>. Let op dat laatste woord: <strong>japonisme "
                  "is de Japanse invloed in het westen</strong>, geen Japanse stroming. Negentiende-eeuwse "
                  "westerse kunstenaars namen <strong>Japanse prenten als voorbeeld</strong> — vlakke kleur, "
                  "een afgesneden beeld — en die westerse stroming heet het japonisme."),
            ("kader", tabel(["richting", "waaraan je ze herkent"],
                            [["<strong>Arabische kunst</strong>",
                              "werkt vaak met <strong>patronen en kalligrafie</strong>: geometrische patronen, arabesken en schrift als versiering"],
                             ["<strong>Afrikaanse kunst</strong>",
                              "maskers en beelden, meestal gemaakt vóór een ritueel en niet voor een museumzaal"],
                             ["<strong>japonisme</strong>",
                              "<strong>westerse</strong> kunst die naar Japanse prenten keek: vlakke kleurvlakken, een hoog standpunt, een beeld dat durft af te snijden"]])),
            ("p", "Romaanse kunst staat niet in dat rijtje: die is <strong>westers en middeleeuws</strong>."),
        ]),
        dict(kop="De zeven functies van een kunstuiting", blokken=[
            ("p", "De fiche noemt <strong>zeven</strong> functies. Ze staan hier in de orde van het "
                  "alfabet, zoals op de fiche."),
            ("kader", tabel(["functie", "wat het werk doet", "voorbeeld"],
                            [["<strong>de decoratieve</strong> functie (decoratief)", "<strong>enkel versieren</strong>",
                              "een rand van bloemmotieven; <strong>dat maakt het geen mindere kunst</strong>"],
                             ["<strong>de economische</strong>", "geld opbrengen of waarde vasthouden",
                              "<strong>een kunstwerk verkocht voor miljoenen</strong>"],
                             ["<strong>de filosofische</strong>", "<strong>een vraag over het bestaan opwerpen</strong>",
                              "een stilleven met verwelkte bloemen: het gaat over de dood"],
                             ["<strong>de maatschappijkritische</strong>", "<strong>een misstand aanklagen</strong>",
                              "een oorlogsprent, een protestlied"],
                             ["<strong>de narratieve</strong> functie (narratief)", "<strong>een verhaal vertellen</strong>",
                              "een altaarstuk met het leven van een heilige, voor wie niet kon lezen"],
                             ["<strong>de ontspannende</strong>", "plezier geven",
                              "een film, een lied, een roman; <strong>ze staat wél bij de zeven</strong>"],
                             ["<strong>de politieke</strong>", "<strong>de macht van een heerser tonen</strong>",
                              "een ruiterportret, een paleisreliëf, een standbeeld op een plein"]])),
            ("p", "<strong>Eén kunstwerk kan meerdere functies hebben.</strong> Een glasraam versiert, "
                  "vertelt een verhaal én draagt een boodschap: drie functies tegelijk. En een functie zegt "
                  "niets over de waarde van een werk — <strong>een werk dat enkel versiert, is dus niet "
                  "ineens geen kunst</strong>."),
            ("p", "Drie functies dienen vooral de maker of de eigenaar: <strong>de economische</strong>, "
                  "<strong>de politieke</strong> en <strong>de decoratieve</strong>. Geld, macht en "
                  "verfraaiing zijn belangen van buiten het werk. <strong>De filosofische functie stelt juist "
                  "een vraag</strong> en dient niemands belang."),
            ("weetje", "Je vraagt naar de functie van een werk omdat je zo begrijpt <strong>waarvoor het "
                       "diende</strong>. Dat is een van de vier richtvragen: hoe en waarmee, wat, waarvoor, "
                       "en wie, waar en wanneer."),
        ]),
        dict(kop="De inhoud: het onderwerp en de functies", blokken=[
            ("p", "De inhoud van een kunstuiting bestaat volgens de fiche uit <strong>het onderwerp en de "
                  "functies</strong>. Materiaal en techniek horen daar niet bij: die vallen onder de "
                  "vormgeving."),
            ("p", "<strong>Het onderwerp is wat er te zien is</strong>: een landschap, een portret, een "
                  "bijbelverhaal, een stilleven. Het antwoordt op de vraag <strong>wat</strong>. "
                  "<strong>Het onderwerp en de functie zijn dus niet hetzelfde</strong>: een portret van een "
                  "koning heeft die koning als onderwerp, en het tonen van macht als functie."),
            ("p", "Over de inhoud klopt dus: <strong>het onderwerp is wat je ziet</strong>, <strong>de "
                  "functie is waarvoor het diende</strong>, en <strong>beide samen vormen de inhoud</strong>. "
                  "De titel kan helpen, maar is de inhoud niet — sommige werken hebben er zelfs geen."),
        ]),
        dict(kop="De context: vier elementen", blokken=[
            ("p", "De context bestaat uit vier elementen. Ze beantwoorden samen de richtvraag <strong>wie, "
                  "waar en wanneer</strong>."),
            ("kader", tabel(["element", "antwoordt op", "wat erbij hoort"],
                            [["<strong>de tijd</strong>", "<strong>wanneer</strong>",
                              "het jaar, de eeuw, de periode waarin het werk ontstond"],
                             ["<strong>de ruimte</strong>", "<strong>waar</strong>",
                              "het land, de streek, de stad, zelfs de plek waar het werk hing"],
                             ["<strong>de maatschappelijke context</strong>", "wat er speelde",
                              "<strong>de toestand van de samenleving</strong>: oorlog, godsdienst, politiek, economie"],
                             ["<strong>de persoonlijke context</strong>", "<strong>wie</strong> het maakte",
                              "<strong>het leven en de opvattingen van de kunstenaar</strong>: opleiding, geloof, ziekte, verlies"]])),
            ("p", "<strong>Zonder context kan een werk anders begrepen worden dan bedoeld.</strong> Een "
                  "spotprent zegt niets als je de gebeurtenis niet kent; de context maakt de boodschap "
                  "leesbaar. Daarom staat de context ook <strong>niet los van de inhoud</strong>: het zijn "
                  "aparte richtvragen, maar <strong>ze verklaren elkaar</strong>. Wie weet in welke tijd een "
                  "werk ontstond, begrijpt waarom de kunstenaar dat onderwerp koos."),
            ("kader", tabel(["wat je ziet", "welke context verklaart het"],
                            [["<strong>een werk uit 1915 met een verwoest landschap</strong>",
                              "<strong>de maatschappelijke</strong>: de Eerste Wereldoorlog woedde — al kan de maker het ook zelf meegemaakt hebben"],
                             ["<strong>een kunstenaar maakt een werk na het verlies van een kind</strong>",
                              "<strong>de persoonlijke</strong>: zijn eigen leven stuurt het werk"],
                             ["<strong>een Afrikaans masker in een Europees museum</strong>",
                              "de context <strong>is weggevallen</strong>: het masker werd voor een ritueel gemaakt en staat nu achter glas"]])),
            ("p", "De betekenis van een werk verandert in de loop van de tijd, omdat <strong>de kijker "
                  "verandert mee</strong>. Elke tijd leest een werk met zijn eigen ogen; het doek zelf blijft "
                  "hetzelfde."),
        ]),
    ])


# ───────────────────────── 6. Richtvragen en de middelen van vormgeving
zet("richtvragen-en-de-middelen-van-vormgeving",
    titel="Richtvragen en de middelen van vormgeving",
    onder="De vier richtvragen van de fiche, en de woordenlijsten uit bijlage 1 en 2: bouwstenen, materiaal en technieken voor de beeldende kunst en voor de architectuur.",
    secties=[
        dict(kop="De vier richtvragen", blokken=[
            ("p", "De fiche noemt <strong>vier</strong> richtvragen. Je analyseert er een kunstuiting mee uit "
                  "<strong>de beeldende kunst en de architectuur</strong>. Je beantwoordt ze in volgorde, want "
                  "zo <strong>ga je van zien naar begrijpen</strong>: eerst wat je ziet, dan wat het betekent, "
                  "dan waarvoor het diende, en ten slotte waar het thuishoort."),
            ("kader", tabel(["richtvraag", "waarover ze gaat"],
                            [["<strong>hoe en waarmee</strong>", "<strong>de middelen van vormgeving</strong>: de bouwstenen, het materiaal en de techniek uit de bijlagen"],
                             ["<strong>wat</strong>", "<strong>de inhoud</strong>, en in het bijzonder het onderwerp van de kunstuiting"],
                             ["<strong>waarvoor</strong>", "<strong>de functie</strong> van het werk"],
                             ["<strong>wie, waar en wanneer</strong>", "de context: de maker, de plaats en de tijd"]])),
            ("p", "<em>Hoeveel</em> staat er niet bij. En de middelen staan in een <strong>bijlage</strong> "
                  "omdat <strong>je ze op het examen mag gebruiken</strong>: het is de woordenlijst voor je "
                  "analyse, met <strong>een lijst per kunstvorm</strong>. Over de bijlagen klopt dus: "
                  "<strong>ze geven de woorden voor je analyse</strong>, <strong>er is een lijst per "
                  "kunstvorm</strong> en <strong>je gebruikt ze bij hoe en waarmee</strong>. Over periodes "
                  "zeggen ze niets; daarvoor kijk je naar de stromingen."),
        ]),
        dict(kop="Bijlage 1, de beeldende kunst: drie groepen middelen", blokken=[
            ("p", "Bijlage 1 verdeelt de middelen in <strong>drie</strong> groepen: <strong>bouwstenen, "
                  "materiaal en technieken</strong>. Vorm, kleur en licht zijn dus geen aparte groepen maar "
                  "<strong>bouwstenen binnen de eerste groep</strong>. En <strong>materiaal en techniek zijn "
                  "niet hetzelfde middel</strong>: materiaal is waarmee, techniek is hoe. Olieverf is "
                  "materiaal, een collage maken is een techniek."),
            ("kader", tabel(["groep", "wat erbij hoort"],
                            [["<strong>de bouwstenen</strong>",
                              "<strong>vorm</strong>, <strong>compositie</strong>, <strong>symmetrie</strong>, <strong>kleur</strong>, <strong>licht</strong> en <strong>ruimte</strong>"],
                             ["<strong>het materiaal</strong>",
                              "bij de schilderkunst olieverf, tempera, acryl; bij de beeldhouwkunst <strong>steen</strong>, <strong>klei</strong>, <strong>brons</strong>, hout, ivoor en moderne materialen"],
                             ["<strong>de technieken</strong>",
                              "tweedimensionaal: schilderen, tekenen, een <strong>fresco</strong> (schilderen op natte kalk aan de muur), een collage; driedimensionaal: <strong>hakken</strong>, <strong>boetseren</strong>, <strong>construeren</strong> en las- en kleeftechnieken"]])),
            ("p", "<strong>Een fresco is dus geen techniek van de beeldhouwkunst</strong> maar van de "
                  "schilderkunst, en <strong>olieverf hoort niet bij de beeldhouwkunst</strong>."),
        ]),
        dict(kop="De bouwstenen één voor één", blokken=[
            ("kader", tabel(["bouwsteen", "wat de bijlage eronder zet"],
                            [["<strong>vorm</strong>",
                              "<strong>hoekig</strong>, <strong>rond</strong>, vierkant, kegel, <strong>hol en bol</strong>, tweedimensionaal en driedimensionaal"],
                             ["<strong>compositie</strong>",
                              "de <strong>compositiegrondvorm</strong>: <strong>horizontaal</strong>, <strong>verticaal</strong>, <strong>diagonaal</strong> of <strong>een driehoek</strong> — de lijn waarlangs de figuren geschikt staan"],
                             ["<strong>symmetrie</strong>",
                              "<strong>symmetrisch en asymmetrisch</strong>, verspreid, overall en centraal"],
                             ["<strong>kleur</strong>",
                              "soorten (<strong>primair: rood, geel en blauw</strong>, daarna secundair en tertiair), contrasten en kleurgebruiken"],
                             ["<strong>licht</strong>",
                              "<strong>eigen schaduw</strong> (op het voorwerp zelf) tegenover <strong>slagschaduw</strong> (ernaast, op de grond of de muur)"],
                             ["<strong>ruimte</strong>",
                              "de drie dimensies <strong>hoogte, breedte en diepte</strong>, en daarnaast het <strong>perspectief</strong> als apart middel"]])),
            ("p", "Bij de kleur noemt de bijlage drie <strong>kleurcontrasten</strong>: <strong>licht-donker</strong>, "
                  "<strong>warm-koud</strong> en <strong>complementair</strong>. Primair en secundair zijn "
                  "soorten kleuren en geen contrast. Daarnaast staan vier <strong>kleurgebruiken</strong>: "
                  "cerebraal, <strong>impressief</strong>, <strong>expressief</strong> en "
                  "<strong>symbolisch</strong>. <strong>Symbolisch kleurgebruik</strong> betekent dat "
                  "<strong>de kleur voor iets staat</strong>: blauw voor Maria, rood voor het martelaarschap. "
                  "<strong>Expressief kleurgebruik</strong> toont vooral het gevoel van de maker: de kleur "
                  "volgt de emotie en niet de werkelijkheid."),
            ("p", "Bij het perspectief draait het om het standpunt. <strong>Het kikvorsperspectief</strong> "
                  "kijkt <strong>van heel laag naar boven</strong>, als een kikker in het gras: de figuren "
                  "torenen boven je uit. <strong>Het vogelperspectief</strong> kijkt <strong>van bovenaf naar "
                  "beneden</strong>."),
        ]),
        dict(kop="Bijlage 2, de architectuur", blokken=[
            ("p", "De architectuur heeft <strong>eigen middelen</strong>, dus een eigen bijlage. Sommige "
                  "woorden lijken op die van bijlage 1, maar ze zijn niet dezelfde: "
                  "<strong>horizontaal en verticaal</strong> gelden bij de beeldende kunst, en "
                  "<strong>verspreid en overall</strong> staan niet bij de architectuur."),
            ("kader", tabel(["middel", "wat de bijlage eronder zet"],
                            [["<strong>compositiegrondvorm</strong>",
                              "<strong>centraalbouw</strong> (rond om een midden) en <strong>langsbouw</strong> (langwerpig)"],
                             ["<strong>symmetrie</strong>",
                              "<strong>symmetrisch</strong>, <strong>asymmetrisch</strong>, <strong>statisch en dynamisch</strong>"],
                             ["<strong>kleur</strong>",
                              "<strong>monochroom</strong> (in één kleur) tegenover <strong>polychroom</strong> (<strong>in meerdere kleuren</strong>), zoals een gevel in gekleurde baksteen"],
                             ["<strong>ruimte</strong>",
                              "<strong>open, gesloten en omsloten</strong>: hoe open het gebouw naar zijn omgeving staat"],
                             ["<strong>licht</strong>",
                              "<strong>natuurlijk licht, lichtinval en reflectie</strong>. Het licht staat er dus wél bij: waar het binnenvalt, bepaalt hoe een ruimte voelt"],
                             ["<strong>structuur en textuur</strong>",
                              "opengewerkt, <strong>grof</strong>, ruw en <strong>gepolijst</strong>: hoe het oppervlak aanvoelt en oogt"],
                             ["<strong>technieken</strong> (de constructietechnieken)",
                              "<strong>een dragende constructie</strong>, <strong>een hangende constructie</strong> en <strong>skeletbouw</strong>"],
                             ["<strong>materiaal</strong>",
                              "natuurlijk: <strong>natuursteen en hout</strong>; niet-natuurlijk: baksteen, <strong>beton</strong>, glas en <strong>staal</strong>"]])),
            ("p", "<strong>Skeletbouw</strong> is de bouwtechniek die draagt met <strong>een geraamte "
                  "in plaats van met muren</strong>. Juist daardoor kan de wand helemaal uit glas bestaan. En let op het "
                  "materiaal: <strong>natuursteen en hout zijn wél natuurlijk</strong>; de niet-natuurlijke "
                  "zijn baksteen, beton, glas en staal, want die zijn door mensen gemaakt."),
        ]),
        dict(kop="De middelen benoemen bij een werk", blokken=[
            ("kader", tabel(["wat je ziet", "welk middel je benoemt"],
                            [["<strong>een driehoekige schikking van drie figuren</strong>",
                              "<strong>de compositie</strong>: de compositiegrondvorm is een driehoek, een veelgebruikte schikking in de renaissance"],
                             ["<strong>een gevel in één kleur, streng symmetrisch, met zuilen</strong>",
                              "<strong>kleur, symmetrie, vorm</strong>: monochroom, streng symmetrisch, en zuilen horen bij de vorm en de constructie"],
                             ["<strong>een kerk met veel licht door hoge glasramen</strong>",
                              "<strong>de lichtinval</strong>, uit bijlage 2 — bij een gotische kerk het sterkste middel"]])),
        ]),
    ])


# ───────────────────────── 7. De eigenheid van de filosofie
zet("de-eigenheid-van-de-filosofie",
    titel="De eigenheid van de filosofie",
    onder="Dagdagelijkse tegenover wetenschappelijke kennis, de indeling van de wetenschappen, en wat de filosofie binnen de menswetenschappen eigen maakt.",
    secties=[
        dict(kop="Twee soorten kennis", blokken=[
            ("kader", tabel(["soort kennis", "waar ze uit komt", "wat haar kenmerkt"],
                            [["<strong>dagdagelijkse kennis</strong>", "<strong>kennis uit ervaring</strong>: wat je zelf hoort, ziet en meemaakt",
                              "nuttig, maar <strong>niet systematisch gecontroleerd</strong>"],
                             ["<strong>wetenschappelijke kennis</strong>", "<strong>methodisch onderzoek</strong>",
                              "<strong>ze is controleerbaar</strong>: anderen kunnen ze nagaan en herhalen"]])),
            ("p", "<strong>Dagdagelijkse kennis kan fout zijn zonder dat je het merkt.</strong> Wie altijd "
                  "hetzelfde ziet, denkt snel dat het altijd zo is; de wetenschap zoekt juist de "
                  "tegenvoorbeelden. Maar <strong>dagdagelijkse kennis is niet altijd fout</strong> — ze is "
                  "vaak heel nuttig. Het verschil zit in de controle, niet in de waarheid."),
            ("p", "Zo klinkt dagdagelijkse kennis: <strong>mijn oma zegt dat het gaat regenen</strong>, "
                  "<strong>iedereen weet dat katten eigenwijs zijn</strong>, <strong>ik voel dat die les lang "
                  "duurt</strong>. Drie uitspraken uit ervaring en van horen zeggen. Verwijst een uitspraak "
                  "naar onderzoek, dan zit je bij de wetenschappelijke kennis."),
            ("p", "Wetenschappelijke kennis <strong>volgt een methode</strong>, <strong>is na te gaan door "
                  "anderen</strong> en <strong>wordt bijgesteld bij nieuw bewijs</strong>. Dat laatste is "
                  "geen zwakte maar haar kracht: ze staat open voor betere gegevens. Ze staat dus juist "
                  "<em>niet</em> voor altijd vast; een theorie die niets kan weerleggen, is geen wetenschap."),
        ]),
        dict(kop="Natuurwetenschappen en menswetenschappen", blokken=[
            ("p", "De fiche onderscheidt <strong>twee</strong> groepen: <strong>natuur- en "
                  "menswetenschappen</strong>. De menswetenschappen splitsen daarna nog eens in "
                  "<strong>gedrags- en cultuurwetenschappen</strong>."),
            ("kader", tabel(["groep", "welke vakken", "welke vragen"],
                            [["<strong>de natuurwetenschappen</strong>", "<strong>fysica</strong>, <strong>chemie</strong>, <strong>biologie</strong>",
                              "hoe de natuur werkt; <strong>hoe planten groeien</strong> is biologie, dus natuurwetenschap"],
                             ["<strong>de gedragswetenschappen</strong>", "<strong>psychologie</strong>, sociologie",
                              "<strong>waarom mensen zich zo gedragen</strong> en <strong>hoe groepen samenleven</strong>"],
                             ["<strong>de cultuurwetenschappen</strong>", "antropologie, geschiedenis",
                              "<strong>hoe culturen verschillen</strong>; <strong>een onderzoek naar gewoontes in een dorp</strong> hoort hier"]])),
            ("p", "Let op twee valstrikken. <strong>Psychologie is geen natuurwetenschap</strong> maar een "
                  "menswetenschap, en meer bepaald een gedragswetenschap. En <strong>de sociologie hoort bij "
                  "de menswetenschappen</strong>: ze onderzoekt mensen in groepen, niet de natuur."),
            ("p", "Onderzoek bij mensen is moeilijker dan bij stenen, want <strong>mensen reageren op het "
                  "onderzoek</strong>. Wie weet dat hij bekeken wordt, gedraagt zich anders; een steen doet "
                  "dat niet."),
            ("p", "Waarom onderscheidt de filosofie die soorten kennis? <strong>Om te weten wat je "
                  "weet.</strong> Hoe betrouwbaar je kennis is, is zelf een filosofische vraag: die heet de "
                  "kennisleer. En het onderscheid staat vooraan in het deel filosofie omdat <strong>je er de "
                  "plaats van de filosofie mee vindt</strong>. De fiche vraagt daarna uitdrukkelijk om "
                  "<strong>de eigenheid van de filosofie binnen de menswetenschappen</strong> uit te leggen — "
                  "filosofie hoort er dus bij, met een eigen manier van werken."),
        ]),
        dict(kop="Wat de filosofie eigen maakt", blokken=[
            ("p", "Bij de vraag wat de filosofie eigen maakt, verwacht de fiche één antwoord in twee delen: "
                  "<strong>haar vragen en haar methode</strong>. Fundamentele vragen, onderzocht met "
                  "argumenten in plaats van met metingen."),
            ("p", "Daarin verschilt ze van de andere menswetenschappen: <strong>ze doet geen metingen</strong>. "
                  "Ze werkt in de plaats daarvan met <strong>argumenten</strong>, en de fiche leert daarvoor "
                  "de AUB-methode aan. <strong>Een filosofische vraag kan je dus niet met een experiment "
                  "beslechten</strong>: niet-empirisch op te lossen is net haar kenmerk. <strong>Filosofie "
                  "kan geen laboratorium gebruiken omdat haar vragen niet meetbaar zijn</strong> — of iets "
                  "rechtvaardig is, meet geen toestel."),
            ("p", "Over de filosofie klopt dus: <strong>ze stelt fundamentele vragen</strong>, <strong>ze "
                  "werkt met argumenten</strong> en <strong>ze hoort bij de menswetenschappen</strong>."),
            ("kader", tabel(["de wetenschapper", "de filosoof"],
                            [["<strong>beschrijft hoe iets is</strong>", "<strong>vraagt naar wat zou moeten</strong>"],
                             ["<strong>meet hoeveel mensen eerlijk zijn</strong>", "vraagt <strong>wat eerlijkheid is</strong>"],
                             ["sluit af met een resultaat", "<strong>onderzoekt elk antwoord verder</strong>"]])),
            ("p", "Verwar die twee kolommen niet van plaats: het is <em>niet</em> de filosoof die onderzoekt "
                  "hoe iets is en de wetenschapper die vraagt wat zou moeten. En daarom blijft filosofie "
                  "nuttig náást de wetenschap: <strong>de wetenschap zegt niet wat goed is</strong>. Dat iets "
                  "kan, zegt niet dat het mag; over die vraag gaat de ethiek."),
            ("p", "Men noemt de filosofie soms de moeder van de wetenschappen omdat <strong>de vakken eruit "
                  "los kwamen</strong>: fysica, psychologie en biologie begonnen als filosofische vragen en "
                  "werden pas later eigen vakken."),
        ]),
        dict(kop="De verwondering", blokken=[
            ("p", "Het beginpunt van alle filosofie heet de <strong>verwondering</strong>. "
                  "<strong>Filosofische verwondering is je verbazen over het gewone</strong>: niet de komeet "
                  "verbaast de filosoof maar de stoel. Waarom is er iets en niet niets?"),
            ("p", "<strong>Verwondering begint bij het stilstaan bij het gewone</strong>: waarom bestaat tijd, "
                  "waarom is onrecht slecht, wat is een mens eigenlijk? Ze is noodzakelijk voor de filosofie, "
                  "want <strong>zonder vraag is er geen filosofie</strong>. Wie niets vreemd vindt, stelt "
                  "geen vragen, en dan komt het denken niet in beweging."),
            ("p", "Over de verwondering klopt dus: <strong>ze zet het denken in gang</strong>, <strong>ze "
                  "richt zich op het gewone</strong> en <strong>ze is nodig voor filosofie</strong>. Wat ze "
                  "niet doet, is antwoorden leveren: ze levert vragen, en dat is net haar rol."),
            ("p", "Bij het filosoferen horen drie houdingen: <strong>doorvragen</strong>, <strong>twijfelen "
                  "aan het vanzelfsprekende</strong> en <strong>je mening laten tegenspreken</strong>. Snel "
                  "willen afsluiten doet het tegenovergestelde. Daarom <strong>onderzoekt een filosoof een "
                  "antwoord dat hij vindt verder</strong>: elk antwoord roept nieuwe vragen op, en zo blijven "
                  "filosofische vragen open."),
            ("weetje", "<strong>Een kind dat vraagt waarom het moet delen, is een begin van filosofie.</strong> "
                       "Het is een vraag naar wat goed is, en dus ethiek. Kinderen filosoferen uit zichzelf."),
        ]),
    ])


# ───────────────────────── 8. De oorsprong van de westerse filosofie
zet("de-oorsprong-van-de-westerse-filosofie",
    titel="De oorsprong van de westerse filosofie",
    onder="Van mythe naar natuurfilosofie, waar en wanneer die stap gezet werd, en de vier natuurfilosofen met hun antwoord op dezelfde vraag.",
    secties=[
        dict(kop="Mythe en natuurfilosofie", blokken=[
            ("p", "Een <strong>mythe</strong> is <strong>een verhaal met goden</strong>: het verklaart met "
                  "goden en helden waarom de wereld is zoals ze is. <strong>De donder verklaarde de "
                  "mythologie door een god</strong> — een boze god slingert bliksems. Het antwoord ligt dus "
                  "bij een wil, niet bij een oorzaak in de natuur."),
            ("p", "Een mythische verklaring <strong>gebruikt goden</strong>, <strong>is niet te "
                  "weerleggen</strong> en <strong>wordt verteld en doorgegeven</strong>. Een mythe laat zich "
                  "niet testen, en juist daarom is ze geen filosofie en geen wetenschap. Dat betekent niet "
                  "dat <strong>een mythe geen enkele waarde heeft</strong>: ze geeft zin en samenhang aan een "
                  "gemeenschap. Ze is alleen geen filosofische of wetenschappelijke verklaring."),
            ("kader", tabel(["", "de mythe", "de natuurfilosofie"],
                            [["waar ze de oorzaak legt", "<strong>buiten de natuur</strong>, bij goden of bovennatuurlijke wezens",
                              "<strong>in de natuur zelf</strong>"],
                             ["hoe ze te werk gaat", "vertellen en doorgeven", "<strong>kijken en redeneren</strong>"],
                             ["of ze te weerleggen is", "<strong>neen</strong>", "ja, een ander kan een beter beginsel voorstellen"]])),
            ("p", "<strong>Mythologie en natuurfilosofie zoeken dus niet hetzelfde soort verklaring.</strong> "
                  "Daar zit precies het verschil, en daar zit het nieuwe aan de natuurfilosofie: "
                  "<strong>ze zoekt een oorzaak in de natuur</strong>. Voor het eerst zoekt men de verklaring "
                  "van de wereld in de wereld zelf, en dat is de stap naar filosofie. Je kan die stap op drie "
                  "manieren zeggen: <strong>van verhaal naar argument</strong>, <strong>van god naar "
                  "natuur</strong>, <strong>van geloven naar onderzoeken</strong>."),
            ("p", "<strong>Verklaart een volk een vulkaan met een boze berggod, dan is dat een mythe</strong>: "
                  "de oorzaak ligt bij de wil van een god, dus buiten de natuur."),
        ]),
        dict(kop="In tijd en ruimte", blokken=[
            ("p", "De fiche vraagt uitdrukkelijk om <strong>de westerse filosofie in tijd en ruimte te "
                  "situeren</strong>, en dat betekent: <strong>zeggen wanneer en waar ze ontstond</strong>. "
                  "Je verduidelijkt haar begin door haar van de mythologie en de natuurfilosofie te "
                  "onderscheiden."),
            ("p", "<strong>De westerse filosofie begon in Griekenland</strong>, in <strong>de zesde eeuw voor "
                  "Christus</strong>, in de Griekse steden van Klein-Azië. De bekendste is "
                  "<strong>Milete</strong>, dat <strong>aan de kust van Klein-Azië</strong> lag: een Griekse "
                  "havenstad in het huidige Turkije. Vandaar de naam Thales van Milete."),
            ("p", "Dat het juist in een havenstad gebeurde, is geen toeval: <strong>ideeën kwamen daar "
                  "samen</strong>. Handel bracht verhalen uit vele landen bijeen, en wie vreemde verhalen "
                  "hoort, gaat zijn eigen verhaal in vraag stellen."),
            ("p", "Men spreekt van <em>westerse</em> filosofie omdat <strong>er ook andere tradities "
                  "bestaan</strong>: ook India en China kennen oude filosofische tradities. Het woord plaatst "
                  "deze lijn, zonder haar boven de andere te zetten."),
            ("p", "De eerste groep heet <strong>natuurfilosofen</strong> omdat <strong>ze de natuur "
                  "verklaarden</strong>. Hun vraag ging over de physis, de natuur — daar komt ook het woord "
                  "fysica van. En hun vraag was: <strong>waaruit bestaat alles?</strong> Ze zochten de "
                  "<strong>oerstof</strong> of het <strong>grondbeginsel</strong> van de werkelijkheid."),
            ("p", "Over die natuurfilosofen klopt: <strong>ze zochten een oerstof</strong>, <strong>ze "
                  "redeneerden over de natuur</strong> en <strong>ze gaven verschillende antwoorden</strong>. "
                  "Een labo bestond nog niet."),
        ]),
        dict(kop="De vier natuurfilosofen", blokken=[
            ("p", "De fiche noemt <strong>vier</strong> natuurfilosofen: <strong>Thales</strong>, "
                  "<strong>Parmenides</strong>, <strong>Heraclitus</strong> en <strong>Pythagoras</strong>. "
                  "Ze leefden <strong>in de zesde eeuw voor Christus</strong> en de vijfde. Aristoteles komt "
                  "veel later en staat bij de mensvisies."),
            ("kader", tabel(["filosoof", "zijn antwoord", "waaraan je hem herkent"],
                            [["<strong>Thales van Milete</strong>", "de oerstof is <strong>water</strong>",
                              "omdat alles vochtig lijkt en leven water nodig heeft; <strong>de eerste westerse filosoof</strong>"],
                             ["<strong>Heraclitus</strong>", "<strong>alles verandert</strong>",
                              "<strong>de stromende rivier</strong>: panta rhei, je stapt nooit twee keer in dezelfde rivier"],
                             ["<strong>Parmenides</strong>", "<strong>verandering is schijn</strong>",
                              "het zijnde is één en onveranderlijk; wat we zien veranderen, bedriegt ons"],
                             ["<strong>Pythagoras</strong>", "alles ligt verankerd <strong>in getallen</strong>",
                              "zijn leer hangt samen met <strong>de muziek</strong>, <strong>de meetkunde</strong> en <strong>de verhoudingen</strong>"]])),
            ("p", "<strong>Thales heet de eerste westerse filosoof omdat hij het antwoord in de natuur "
                  "zocht.</strong> Hij liet de goden als verklaring vallen en zocht één natuurlijk beginsel; "
                  "dat maakt zijn stap zo groot. <strong>Pythagoras verbond de filosofie met de "
                  "wiskunde</strong>: voor hem was de werkelijkheid in getallen geschreven, en zijn naam "
                  "leeft nog in de stelling van Pythagoras."),
            ("p", "Tussen Heraclitus en Parmenides zit de scherpste tegenstelling: <strong>verandering tegen "
                  "rust</strong>. De een ziet alles stromen, de ander ziet het zijnde onveranderlijk, en die "
                  "twist werkt eeuwen door. <strong>Parmenides vond dus niet zoals Heraclitus dat alles "
                  "verandert</strong> — hij dacht precies het omgekeerde. Wie zegt dat niets ooit echt "
                  "verandert, sluit aan bij <strong>Parmenides</strong>; wie muziek verklaart uit "
                  "verhoudingen van snaarlengtes, bij <strong>Pythagoras</strong>."),
            ("p", "<strong>De vier gaven dus niet hetzelfde antwoord</strong>: water, getal, verandering, "
                  "onveranderlijkheid — vier antwoorden op dezelfde vraag. Over de vier samen klopt: "
                  "<strong>ze zijn Grieks</strong>, <strong>ze zochten één grondbeginsel</strong> en "
                  "<strong>ze lieten de mythe achter</strong>. Samenwerken deden ze niet; ze spraken elkaar "
                  "grondig tegen, en dat gesprek is net het begin van de filosofie."),
        ]),
    ])


# ───────────────────────── 9. Soorten vragen en de filosofische vraag
zet("soorten-vragen-en-de-filosofische-vraag",
    titel="Soorten vragen en de filosofische vraag",
    onder="Het verschil tussen een weetvraag, een meningsvraag en een denkvraag, en de vijf kenmerken waaraan je een filosofische vraag herkent.",
    secties=[
        dict(kop="Drie soorten vragen", blokken=[
            ("p", "De fiche onderscheidt er <strong>drie</strong>: een <strong>weetvraag</strong>, een "
                  "<strong>meningsvraag</strong> en een filosofische vraag, die de fiche ook "
                  "<strong>denkvraag</strong> noemt."),
            ("kader", tabel(["soort vraag", "waaraan je ze herkent", "voorbeelden"],
                            [["<strong>de weetvraag</strong>", "<strong>ze heeft één juist antwoord</strong>, dat je kan <strong>opzoeken of nameten</strong>",
                              "<strong>hoe hoog is de Everest</strong>, <strong>wanneer begon de oorlog</strong>, <strong>hoeveel inwoners heeft Gent</strong>, <strong>hoeveel mensen wonen in België</strong>"],
                             ["<strong>de meningsvraag</strong>", "<strong>ze vraagt naar wat iemand vindt</strong>, naar een smaak of voorkeur",
                              "<strong>wat is de leukste sport</strong>, <strong>welk boek vind je het mooist</strong>, <strong>welke film koos jij</strong>"],
                             ["<strong>de filosofische vraag of denkvraag</strong>", "<strong>ze vraagt om argumenten</strong> en is niet op te zoeken",
                              "<strong>wat is vrijheid</strong>, <strong>mag je altijd liegen</strong>, <strong>bestaat er een ziel</strong>, <strong>wat is tijd</strong>, <strong>mag een computer straffen uitspreken</strong>"]])),
            ("p", "<strong>Een weetvraag kan je dus wél opzoeken</strong>; dat is precies wat haar een "
                  "weetvraag maakt. En <strong>een filosofische vraag en een meningsvraag zijn niet "
                  "hetzelfde</strong>: bij een mening volstaat wat je vindt, bij een filosofische vraag moet "
                  "je je antwoord <strong>beargumenteren</strong>, en kan je antwoord weerlegd worden."),
            ("p", "Het onderscheid is nuttig omdat <strong>je er door weet hoe je een vraag aanpakt</strong>: "
                  "een weetvraag zoek je op, een meningsvraag beantwoord je zelf, een filosofische vraag "
                  "onderzoek je met argumenten."),
            ("p", "<strong>Een vraag kan van soort veranderen naargelang je ze formuleert.</strong> "
                  "<em>Hoe laat is het</em> is een weetvraag; <em>wat tijd eigenlijk is</em> is filosofisch. "
                  "Zo maak je van een weetvraag een filosofische vraag: <strong>vraag naar het begrip "
                  "zelf</strong>. Niet hoeveel mensen gelukkig zijn, maar wat geluk is. Let daarom op vragen "
                  "die diep klinken en het niet zijn: <strong>hoeveel soorten geluk men kent</strong> is "
                  "gewoon opzoekwerk."),
            ("p", "Oefen op twee grensgevallen. <strong>Een leerling die vraagt of straf nodig is om te "
                  "leren</strong>, stelt een filosofische vraag: ze gaat over wat goed is en vraagt om "
                  "argumenten."),
        ]),
        dict(kop="De vijf kenmerken van de filosofische vraag", blokken=[
            ("p", "Na het soort vraag bepalen, zet de fiche een tweede stap: <strong>de kenmerken "
                  "benoemen</strong>. Het zijn er <strong>vijf</strong>."),
            ("kader", tabel(["kenmerk", "wat het betekent"],
                            [["<strong>fundamenteel</strong>", "<strong>ze raakt de grond van de zaak</strong>, niet een detail: <strong>wat is kennis</strong>, wat is recht, wat is een mens"],
                             ["<strong>meerduidig</strong>", "<strong>ze kan op meerdere manieren begrepen worden</strong>: vrijheid kan over keuze, wet of verlangen gaan"],
                             ["<strong>niet-empirisch op te lossen</strong>", "<strong>geen meting beslist</strong>; je komt er met argumenten"],
                             ["<strong>open</strong>", "<strong>er is geen eindantwoord</strong>: elk antwoord roept nieuwe vragen op"],
                             ["<strong>universeel</strong>", "<strong>de vraag geldt voor iedereen</strong>, <strong>overal gesteld kan worden</strong>, in elke cultuur en elke tijd"]])),
            ("p", "<em>Meetbaar</em> staat er dus niet bij; dat is net het tegendeel. En <strong>een "
                  "filosofische vraag heeft geen één sluitend antwoord</strong>: ze is open. Dat betekent "
                  "niet dat elk antwoord even goed is — argumenten blijven wegen. <strong>Een filosofische "
                  "vraag moet ook fundamenteel zijn</strong>: een vraag over een detail is er geen."),
            ("p", "Drie kenmerken maken samen dat een vraag niet opzoekbaar is: <strong>niet-empirisch op te "
                  "lossen</strong>, <strong>open</strong> en <strong>meerduidig</strong>. Universeel zegt "
                  "enkel dat ze overal geldt. En omdat de vraag <strong>meerduidig</strong> is, moet je "
                  "<strong>eerst de begrippen verhelderen</strong>: wie over vrijheid spreekt, moet zeggen "
                  "welke vrijheid hij bedoelt, anders praten twee mensen langs elkaar."),
            ("p", "Over de vijf kenmerken klopt: <strong>ze horen samen bij één vraag</strong>, <strong>ze "
                  "helpen vragen te herkennen</strong> en <strong>ze staan alle vijf op de fiche</strong>. "
                  "Eén kenmerk volstaat niet: een meningsvraag is ook open, maar niet fundamenteel of "
                  "universeel."),
            ("p", "Neem de vraag <strong>mag een rechter een robot zijn</strong>. Ze is "
                  "<strong>fundamenteel</strong> (ze raakt de grond van de rechtvaardigheid), "
                  "<strong>niet-empirisch</strong> (niet te meten) en <strong>open</strong>."),
            ("weetje", "<strong>Openheid is geen zwakte van de filosofie</strong>, want <strong>het gesprek "
                       "blijft doorgaan</strong>. Zonder eindantwoord blijven mensen hun opvattingen toetsen, "
                       "en dat is net de winst."),
        ]),
    ])


# ───────────────────────── 10. De filosofische domeinen
zet("de-filosofische-domeinen",
    titel="De filosofische domeinen",
    onder="De zes domeinen van de fiche, de vragen die bij elk horen, en wat je doet met een vraag die in twee domeinen tegelijk thuishoort.",
    secties=[
        dict(kop="Zes domeinen", blokken=[
            ("p", "De fiche noemt <strong>zes</strong> filosofische domeinen. Men verdeelt de filosofie zo "
                  "<strong>om vragen te ordenen</strong>: een domein zegt waarover een vraag gaat, en dus "
                  "ook welke begrippen en welke denkers erbij horen. Er is <strong>geen rangorde</strong> — "
                  "geen enkel domein is belangrijker dan een ander."),
            ("kader", tabel(["domein", "waarover het gaat", "typische vragen"],
                            [["<strong>de antropologie</strong>", "<strong>vragen over de mens</strong> (de wijsgerige antropologie)",
                              "<strong>wat maakt een mens mens</strong>, <strong>verschilt hij van een dier</strong>, <strong>kan een robot een mens zijn</strong>"],
                             ["<strong>de esthetica</strong> (de esthetiek)", "<strong>vragen over schoonheid</strong>",
                              "<strong>wat maakt kunst mooi</strong>, <strong>moet kunst mooi zijn</strong>, <strong>heeft een kunstwerk een boodschap nodig</strong>, <strong>zit schoonheid in het oog van de kijker</strong>"],
                             ["<strong>de ethiek</strong>", "<strong>vragen over de goedheid</strong>, over goed handelen",
                              "<strong>mag je liegen om iemand te sparen</strong>, <strong>mag je dierproeven doen</strong>, <strong>is straf rechtvaardig</strong>"],
                             ["<strong>kennisleer</strong> (of kennistheorie) <strong>en logica</strong>", "samen: <strong>de vragen over de waarheid</strong>",
                              "<strong>wat is kennis</strong>, <strong>hoe weet je iets zeker</strong>, <strong>bedriegen je zintuigen je</strong>, <strong>kan ik zeker weten dat ik niet droom</strong>, <strong>is deze redenering geldig</strong>"],
                             ["<strong>de metafysica</strong>", "<strong>de bovenwereld</strong>: wat achter of boven het zichtbare ligt",
                              "<strong>bestaat er iets na de dood</strong>, <strong>bestaat er een god</strong>, <strong>wat is het zijnde</strong>"],
                             ["<strong>de natuurfilosofie</strong>", "<strong>vragen over de wereld zelf</strong>",
                              "<strong>waaruit bestaat de werkelijkheid</strong>, <strong>wat is ruimte</strong>, <strong>wat is tijd</strong>, <strong>waaruit bestaat materie</strong>"]])),
            ("p", "<strong>Meta</strong> betekent voorbij: de metafysica gaat voorbij wat je kan zien en "
                  "meten. <strong>Kennisleer en logica staan samen onder één noemer</strong>, want beide gaan "
                  "over de waarheid: de kennisleer vraagt wat kennis is en hoe betrouwbaar ze kan zijn, en "
                  "<strong>de logica toetst of een redenering klopt</strong> — of de stap van argument naar "
                  "conclusie geldig is, los van de inhoud. <strong>De vraag of een redenering geldig is, "
                  "hoort dus niet bij de esthetica.</strong>"),
            ("p", "Twee verwarringen om te vermijden. <strong>De natuurfilosofie is niet hetzelfde als de "
                  "natuurwetenschap</strong>: de wetenschap meet, de natuurfilosofie denkt na over de "
                  "begrippen die de wetenschap gebruikt. En <strong>of kunst mooi moet zijn, valt niet buiten "
                  "de esthetica</strong>: dat is juist een echte esthetische vraag, die rechtstreeks raakt "
                  "aan de kunstcriteria uit het eerste deel van dit vak."),
            ("p", "<strong>De natuurfilosofie verwijst het duidelijkst naar de eerste Griekse "
                  "filosofen</strong>: Thales, Heraclitus, Parmenides en Pythagoras zochten de grond van de "
                  "wereld. En de ethiek krijgt in de fiche een eigen hoofdstuk, met de ethische stromingen "
                  "en hun filosofen."),
        ]),
        dict(kop="Vragen die in meerdere domeinen thuishoren", blokken=[
            ("p", "<strong>Eén vraag kan tot meerdere domeinen horen.</strong> Dat is geen fout in de "
                  "indeling: de domeinen <strong>overlappen soms</strong>. Over de domeinen klopt dus: "
                  "<strong>ze ordenen de vragen</strong>, <strong>ze overlappen soms</strong> en <strong>de "
                  "fiche noemt er zes</strong>."),
            ("kader", tabel(["vraag", "welke domeinen"],
                            [["<strong>mag je een dier doden om een mens te genezen</strong>",
                              "<strong>ethiek én antropologie</strong>"],
                             ["<strong>hebben dieren rechten</strong>",
                              "<strong>ethiek en antropologie</strong>: wat een dier is, en wat wij mogen doen"],
                             ["<strong>heeft een mens een vrije wil</strong>",
                              "<strong>de antropologie</strong>, <strong>de metafysica</strong> en <strong>de ethiek</strong>: wat de mens is, of er meer is dan oorzaak en gevolg, en of je verantwoordelijk bent"],
                             ["<strong>moeten we de natuur beschermen om haarzelf</strong>",
                              "<strong>ethiek en natuurfilosofie</strong>: wat we moeten doen, en wat de natuur zelf is"]])),
            ("p", "Sommige domeinen gaan over <strong>wat zou moeten</strong> in plaats van wat is: "
                  "<strong>de ethiek</strong>, <strong>de esthetica</strong> en <strong>deels de "
                  "antropologie</strong> geven waardeoordelen. De logica onderzoekt enkel of een redenering "
                  "geldt."),
            ("p", "Een domein bepalen helpt bij het antwoorden, want <strong>je weet dan welke begrippen "
                  "gelden</strong>: elk domein heeft eigen begrippen en eigen denkers, en dat geeft je "
                  "houvast. Let wel: <strong>een domein bepalen is géén van de filosofische "
                  "vaardigheden</strong>. Die drie zijn een vraag stellen, argumenteren met de AUB-methode "
                  "en een tekst analyseren; de domeinen onderscheiden staat apart op de fiche."),
        ]),
    ])


# ───────────────────────── 11. De filosofische vaardigheden
zet("de-filosofische-vaardigheden",
    titel="De filosofische vaardigheden",
    onder="De drie vaardigheden van de fiche: zelf een filosofische vraag stellen, argumenteren met de AUB-methode, en een filosofische tekst analyseren in drie stappen.",
    secties=[
        dict(kop="Drie vaardigheden", blokken=[
            ("p", "De fiche vraagt <strong>drie</strong> vaardigheden: <strong>een vraag stellen</strong>, "
                  "<strong>argumenteren met AUB</strong> en <strong>een tekst analyseren</strong>. Citeren "
                  "mag, maar is geen aparte vaardigheid, en <strong>een domein bepalen hoort er ook niet "
                  "bij</strong>."),
            ("p", "<strong>De eerste vaardigheid is zelf een filosofische vraag stellen</strong> bij een "
                  "aangebracht thema. Neem het thema geld. Filosofisch zijn dan <strong>maakt geld "
                  "gelukkig</strong>, <strong>mag rijkdom onbeperkt zijn</strong> en <strong>is armoede "
                  "onrechtvaardig</strong>: fundamenteel en open. Hoeveel mensen arm zijn, is een weetvraag."),
            ("p", "Die drie vaardigheden komen ook terug bij lichaam en geest en bij mens en dier, want "
                  "<strong>je past ze toe op elk thema</strong>. De fiche vraagt bij elk thema een vraag, een "
                  "argument en een tekstanalyse; zo blijven de vaardigheden niet in de lucht hangen."),
        ]),
        dict(kop="De AUB-methode", blokken=[
            ("p", "De AUB-methode heeft <strong>drie</strong> stappen: <strong>argument, uitleg, "
                  "bijvoorbeeld</strong>. Ze heet zo omdat <strong>de letters een geheugensteun</strong> "
                  "zijn: de drie beginletters vormen samen een woord dat je onthoudt."),
            ("kader", tabel(["letter", "wat je doet", "zinaanzetten uit de bijlage"],
                            [["<strong>A</strong>", "<strong>je noemt je argument</strong>, de bewering zelf",
                              "<strong>mijn argument is dat …</strong>"],
                             ["<strong>U</strong>", "<strong>de uitleg</strong>: eerst <strong>waarom het zo is</strong>, dan <strong>waarom dat goed of slecht is</strong> (twee stappen)",
                              "<strong>want</strong>, <strong>omdat</strong>"],
                             ["<strong>B</strong>", "<strong>het voorbeeld</strong> dat je argument concreet maakt",
                              "<strong>stel je voor</strong>, <strong>het is onderzocht dat</strong>, <strong>een voorbeeld hiervan is</strong>"]])),
            ("p", "Een volledig argument heeft dus <strong>de bewering</strong>, <strong>de reden "
                  "erachter</strong> en <strong>een voorbeeld erbij</strong>. Een filosofennaam mag erbij, "
                  "maar hoort niet in de methode. <strong>Enkel een argument noemen volstaat niet, want de "
                  "ander begrijpt het niet</strong>: zonder uitleg en voorbeeld blijft het een bewering. Wie "
                  "zegt <em>dat is gewoon zo</em>, mist <strong>de uitleg en het voorbeeld</strong>, dus de U "
                  "en de B."),
            ("p", "<strong>De B mag een zelfbedacht voorbeeld zijn.</strong> De bijlage zegt het letterlijk: "
                  "gebruik je eigen fantasie of zoek informatie op het internet. <strong>Een voorbeeld moet "
                  "dus niet uit onderzoek komen.</strong>"),
            ("p", "Twee dingen die de methode <em>niet</em> doet. <strong>Ze geeft je niet het juiste "
                  "standpunt</strong>: ze geeft de vorm waarin je een standpunt verdedigt, en welk standpunt "
                  "je kiest blijft aan jou. En ze blijft niet bij de filosofie alleen: <strong>ze geldt ook "
                  "bij ethische vraagstukken</strong>, waar de fiche uitdrukkelijk om een argument volgens "
                  "AUB vraagt."),
            ("p", "Bij een filosofische positie vraagt de fiche <strong>argumenten voor en tegen</strong>. Je "
                  "moet ook argumenten tegen je eigen standpunt kunnen bedenken, want <strong>zo weet je wat "
                  "je weerlegt</strong>: een standpunt dat de tegenargumenten niet kent, staat zwak."),
        ]),
        dict(kop="Een filosofische tekst analyseren in drie stappen", blokken=[
            ("p", "Het stappenplan heeft <strong>drie</strong> stappen. Je leest de tekst dus <strong>niet "
                  "slechts één keer</strong>: minstens twee keer, en daarna volgt pas de reflectie."),
            ("kader", tabel(["stap", "wat je doet", "waarmee je afsluit"],
                            [["<strong>stap 1: globaal en oriënterend lezen</strong>",
                              "<strong>de tekst in zijn geheel lezen</strong> om de structuur te zien; je let op <strong>de indeling in alinea's</strong>, <strong>de signaalwoorden</strong> en <strong>de kernbegrippen die terugkomen</strong>",
                              "<strong>een kernzin per alinea</strong>"],
                             ["<strong>stap 2: grondig lezen</strong>",
                              "<strong>de tekst zorgvuldig opnieuw lezen</strong>: moeilijke zinnen <strong>ontleden</strong>, <strong>onbekende woorden opzoeken</strong>, vragen noteren en verbanden aanduiden — <strong>opsommingen</strong>, <strong>voorbeelden</strong>, en <strong>de stelling en de argumenten</strong>",
                              "<strong>een samenvatting in enkele zinnen</strong>"],
                             ["<strong>stap 3: reflectie</strong>",
                              "<strong>nadenken over wat je er zelf van vindt</strong>: <strong>welke kritiek heb ik</strong>, <strong>welke tegenvoorbeelden vind ik</strong>, <strong>hoe zou de auteur antwoorden</strong>",
                              "eventueel je eigen overtuiging bijstellen"]])),
            ("p", "Een <strong>signaalwoord</strong> is <strong>een woord dat een verband aangeeft</strong>: "
                  "daarom, toch, bovendien, kortom. Ze wijzen hoe de delen samenhangen."),
            ("p", "De samenvatting na stap 2 is de toets of je de tekst echt begrepen hebt: je moet achteraf "
                  "<strong>met eigen woorden kunnen uitleggen hoe de auteur zijn stelling verdedigt</strong>."),
            ("p", "<strong>Kritiek laat je in stap 3 zeker niet achterwege</strong>; de bijlage vraagt er "
                  "juist naar. Je vraagt <strong>hoe de auteur je kritiek zou beantwoorden</strong> omdat "
                  "<strong>je zo je eigen bezwaar toetst</strong>: misschien had hij het al voorzien, en dan "
                  "is je kritiek zwakker dan je dacht. En soms <strong>moet je je eigen overtuiging "
                  "bijstellen</strong> — ook dat staat er letterlijk."),
        ]),
    ])


# ───────────────────────── 12. Lichaam en geest
zet("lichaam-en-geest",
    titel="Lichaam en geest",
    onder="Monisme tegenover dualisme, de argumenten van beide kanten, en de drie filosofen van dit thema: Plato, Aristoteles en Descartes.",
    secties=[
        dict(kop="Twee mensvisies", blokken=[
            ("p", "De kernvraag van dit thema is <strong>hoe lichaam en geest samenhangen</strong>. Daarop "
                  "geven twee visies een ander antwoord — <strong>monisme en dualisme geven dus niet "
                  "hetzelfde antwoord</strong>, ze staan juist tegenover elkaar."),
            ("kader", tabel(["", "het monisme", "het dualisme"],
                            [["wat het zegt", "<strong>de mens is één geheel</strong> (monos is één); wie het geestelijke tot het lichamelijke herleidt, redeneert <strong>monistisch</strong>",
                              "<strong>lichaam en geest zijn apart</strong> (duo is twee); wie de ziel los van het lichaam laat bestaan, redeneert <strong>dualistisch</strong>"],
                             ["welk deel de fiche noemt", "<strong>enkel het lichaam</strong>", "<strong>lichaam en geest</strong>"],
                             ["kan de geest zonder lichaam", "neen", "<strong>ja</strong>: daarop steunt het idee van een ziel"],
                             ["typische uitspraak", "<strong>denken is een werking van het lichaam</strong>, <strong>zonder brein geen gedachten</strong>, <strong>liefde is enkel hersenwerking</strong>",
                              "<strong>mijn ziel leeft na de dood verder</strong>"],
                             ["sterkste argument", "<strong>een gekwetst brein verandert iemand</strong>",
                              "<strong>gedachten voelen niet stoffelijk</strong> aan: geen gewicht, geen kleur"]])),
            ("p", "<strong>Pijn is een probleem voor het dualisme</strong>, want daar <strong>raken lichaam "
                  "en geest elkaar</strong>: als het twee aparte dingen zijn, hoe kan een snee in je vinger "
                  "dan je gedachten storen?"),
            ("p", "Bij dit thema horen vragen als <strong>ben ik mijn brein</strong>, <strong>heb ik een "
                  "ziel</strong> en <strong>waar zitten gedachten</strong>. Het gewicht van een brein is een "
                  "weetvraag en hoort er niet bij."),
            ("p", "<strong>Hersenonderzoek heeft dit debat niet beslecht.</strong> We weten veel meer over "
                  "het brein, maar hoe gedachten ontstaan uit cellen blijft een open vraag. Het is dan ook "
                  "een filosofische en geen wetenschappelijke vraag, want <strong>geen meting beslecht "
                  "ze</strong>: een hersenscan toont activiteit, geen bewustzijn."),
            ("p", "Over dit debat klopt: <strong>het is eeuwenoud</strong>, <strong>het is nog niet "
                  "beslecht</strong> en <strong>het raakt aan de ziel</strong>. Het raakt bovendien aan de "
                  "ethiek, want <strong>de verantwoordelijkheid hangt ervan af</strong>: als je brein alles "
                  "beslist, blijft er van de vrije wil weinig over, en zonder vrije wil wankelt de "
                  "schuldvraag."),
            ("weetje", "De fiche vraagt bij dit thema ook <strong>zelf een filosofische vraag te "
                       "formuleren</strong>, een argument voor en tegen volgens de AUB-methode, en een "
                       "tekstanalyse met het stappenplan."),
        ]),
        dict(kop="Drie filosofen", blokken=[
            ("p", "De fiche noemt er <strong>drie</strong>: <strong>Plato</strong>, "
                  "<strong>Aristoteles</strong> en <strong>Descartes</strong>. Kant, Bentham en Mill staan "
                  "bij de ethiek. En <strong>ze leefden niet in dezelfde eeuw</strong>."),
            ("kader", tabel(["filosoof", "wanneer en waar", "wat hij dacht"],
                            [["<strong>Plato</strong>", "<strong>Athene</strong>, <strong>de vierde eeuw voor Christus</strong>",
                              "<strong>de ziel is gevangen in het lichaam</strong>: het lichaam is tijdelijk, <strong>de ziel onsterfelijk</strong>. Uitgesproken <strong>dualist</strong>"],
                             ["<strong>Aristoteles</strong>", "Athene, dezelfde eeuw; <strong>leerling van Plato</strong>",
                              "<strong>de ziel is de vorm van het lichaam</strong>: vorm en stof horen samen, dus <strong>zonder lichaam geen ziel</strong>. Staat <strong>het dichtst bij het monisme</strong>"],
                             ["<strong>René Descartes</strong>", "Frankrijk, <strong>de zeventiende eeuw</strong>",
                              "<strong>ik denk, dus ik ben</strong>; <strong>geest en stof zijn apart</strong>; <strong>ik twijfel eerst aan alles</strong>. <strong>Dualist</strong>"]])),
            ("p", "<strong>Descartes vond dus niet dat lichaam en geest hetzelfde zijn</strong>: hij "
                  "onderscheidde juist het denkende van het uitgebreide — de geest denkt, het lichaam neemt "
                  "ruimte in. <strong>Hij twijfelde eerst aan alles om een zeker beginpunt te vinden</strong>: "
                  "door alles in twijfel te trekken bleef één zekerheid over, namelijk dat hij twijfelde en "
                  "dus dacht. Maar <strong>één probleem bleef bij hem open: hoe geest en lichaam elkaar "
                  "raken</strong>. Als het twee aparte dingen zijn, hoe kan een beslissing dan je hand "
                  "bewegen? Dat heet het interactieprobleem."),
            ("p", "<strong>Plato en Descartes zijn dus de dualisten</strong>, elk om een andere reden, en "
                  "Aristoteles staat dichter bij het monisme. Wie zegt dat <strong>zonder lichaam geen ziel "
                  "kan bestaan, sluit aan bij Aristoteles</strong>; wie zegt dat zijn ziel verder leeft, bij "
                  "Plato of Descartes."),
            ("p", "De fiche vraagt deze filosofen <strong>in tijd en ruimte te plaatsen</strong> omdat "
                  "<strong>hun antwoord aan hun tijd hangt</strong>: Descartes dacht na de opkomst van de "
                  "wetenschap, Plato eeuwen ervoor, en dat verklaart veel van het verschil."),
        ]),
    ])


# ───────────────────────── 13. Mens en dier
zet("mens-en-dier",
    titel="Mens en dier",
    onder="De traditionele tweedeling en waarom ze onder druk staat, en de vier filosofen van dit thema: Aristoteles, Descartes, Darwin en Singer.",
    secties=[
        dict(kop="De traditionele tweedeling", blokken=[
            ("p", "De traditionele tweedeling zegt dat <strong>de mens boven het dier staat</strong>. "
                  "Eeuwenlang gold de mens als iets aparts, met de rede of de ziel als wat hem boven het dier "
                  "plaatst. De eigenschappen die de traditie enkel aan de mens toeschreef, zijn "
                  "<strong>de rede</strong>, <strong>de taal</strong> en <strong>de moraal</strong>. Honger "
                  "heeft elk dier; <strong>de rede</strong> gold als hét typisch menselijke vermogen."),
            ("p", "Die tweedeling heeft gevolgen voor wat we doen: <strong>ze rechtvaardigt "
                  "dierproeven</strong>, <strong>ze rechtvaardigt de veeteelt</strong> en <strong>ze "
                  "rechtvaardigt de jacht</strong>. Wie het dier lager plaatst, mag er meer mee doen. "
                  "<strong>Volgens die tweedeling hebben dieren dus geen rechten zoals mensen</strong>: het "
                  "dier gold eerder als bezit dan als rechthebbende."),
            ("p", "Maar <strong>de tweedeling staat onder druk, want dieren kunnen meer dan gedacht</strong>. "
                  "<strong>Ook dieren gebruiken werktuigen</strong>: kraaien buigen draad tot een haak, "
                  "chimpansees gebruiken stokken. Taal, werktuigen, rouw en samenwerking — wat men voor "
                  "menselijk hield, komt ook bij dieren voor. <strong>Taal gold als hét menselijke "
                  "kenmerk</strong>, tot bleek dat dieren ook tekens gebruiken. <strong>Onomstreden is de "
                  "tweedeling vandaag dus niet</strong>: de fiche zet haar naast de visies van Darwin en "
                  "Singer."),
            ("kader", tabel(["argument vóór een scherp onderscheid", "argumenten tegen een scherp onderscheid"],
                            [["<strong>enkel mensen bouwen een cultuur</strong>: kunst, wetenschap en geschiedenis zijn zonder weerga",
                              "<strong>dieren communiceren</strong>, <strong>dieren leren en geven door</strong>, <strong>dieren voelen pijn</strong>"]])),
            ("p", "Wie zegt dat het verschil <strong>gradueel</strong> is, bedoelt dat <strong>het een "
                  "verschil in graad</strong> is: mensen kunnen méér van hetzelfde, niet iets volkomen "
                  "anders. Darwin zette die gedachte in gang."),
            ("p", "De vraag <strong>wat mens van dier onderscheidt</strong> hoort bij "
                  "<strong>de antropologie</strong>, en ze is filosofisch en niet biologisch omdat "
                  "<strong>ze over betekenis gaat</strong>: de biologie beschrijft de verschillen, de "
                  "filosofie vraagt wat ze betekenen voor hoe we handelen. Ze raakt daarom aan de ethiek, "
                  "want <strong>ze bepaalt wat we mogen doen</strong>. Bij de dierenrechten staat één "
                  "vermogen centraal: <strong>het lijden</strong>."),
            ("p", "Over dit thema klopt: <strong>het is eeuwenoud</strong>, <strong>het raakt aan de "
                  "ethiek</strong> en <strong>de visies verschillen sterk</strong>. En de fiche vraagt er, "
                  "naast de visies, <strong>een vraag, een argument en een tekst</strong>: zelf een "
                  "filosofische vraag formuleren, argumenteren met AUB, en een tekst analyseren met het "
                  "stappenplan."),
        ]),
        dict(kop="Vier filosofen", blokken=[
            ("p", "De fiche noemt er <strong>vier</strong>: <strong>Aristoteles</strong>, "
                  "<strong>Descartes</strong>, <strong>Charles Darwin</strong> en <strong>Peter "
                  "Singer</strong>. <strong>Ze leefden niet in dezelfde periode</strong>, en "
                  "<strong>Aristoteles en Descartes komen ook bij lichaam en geest terug</strong> — hun "
                  "antwoord daar bepaalt mee wat ze over dieren zeggen."),
            ("kader", tabel(["filosoof", "wanneer en waar", "zijn visie"],
                            [["<strong>Aristoteles</strong>", "Athene, <strong>de vierde eeuw voor Christus</strong>",
                              "de mens is <strong>een redelijk dier</strong>: een dier dus, van dezelfde natuur, maar met rede"],
                             ["<strong>Descartes</strong>", "Frankrijk, de zeventiende eeuw",
                              "<strong>dieren zijn als machines</strong>: zonder denkende geest zijn ze ingewikkelde automaten. <strong>Hij trekt de scheiding bijzonder scherp</strong>"],
                             ["<strong>Charles Darwin</strong>", "<strong>Engeland</strong>, <strong>de negentiende eeuw</strong>",
                              "<strong>mens en dier zijn verwant</strong>: met <strong>de evolutietheorie</strong> wordt de mens een tak aan dezelfde boom, en <strong>het verschil wordt gradueel</strong>"],
                             ["<strong>Peter Singer</strong>", "Australië, <strong>hedendaags</strong> (geboren in 1946, werk over dierenrechten vanaf de jaren zeventig)",
                              "<strong>lijden is wat telt</strong>, <strong>de soort doet niet ter zake</strong>, <strong>dierenleed weegt echt mee</strong>"]])),
            ("p", "<strong>Aristoteles en Descartes geven dus niet hetzelfde antwoord</strong>: de ene noemt "
                  "de mens een dier mét rede, de andere zet dier en mens in twee werelden. <strong>Darwin en "
                  "Singer verkleinen de kloof</strong>, elk om een andere reden: Darwin door de verwantschap, "
                  "Singer door het lijden."),
            ("p", "Singer gebruikt voor het voortrekken van je eigen soort het woord "
                  "<strong>speciësisme</strong>: net als racisme of seksisme een onderscheid dat hij niet "
                  "gerechtvaardigd acht."),
            ("p", "Zo breng je een uitspraak thuis. <strong>Dierenleed weegt even zwaar als mensenleed</strong> "
                  "is <strong>Singer</strong>. <strong>Een dier voelt niets omdat het geen geest heeft</strong> "
                  "is <strong>Descartes</strong>. En de fiche plaatst deze filosofen in tijd en ruimte omdat "
                  "<strong>hun tijd hun antwoord verklaart</strong>: Singer kon bouwen op evolutiekennis die "
                  "Aristoteles niet had."),
        ]),
    ])


# ───────────────────────── 14. De ethische stromingen en hun filosofen
zet("de-ethische-stromingen-en-hun-filosofen",
    titel="De ethische stromingen en hun filosofen",
    onder="Gevolgenethiek tegenover plichtethiek, de bezwaren tegen elk van beide, en de vier filosofen: Kant, Bentham, Mill en Singer.",
    secties=[
        dict(kop="Twee stromingen", blokken=[
            ("p", "De fiche noemt <strong>twee</strong> ethische stromingen: <strong>gevolgenethiek en "
                  "plichtethiek</strong>. Ze vraagt uitdrukkelijk om <strong>te beargumenteren tot welke "
                  "stroming een gegeven voorbeeld hoort</strong>."),
            ("kader", tabel(["", "de gevolgenethiek", "de plichtethiek"],
                            [["waar ze naar kijkt", "<strong>naar het resultaat</strong>", "<strong>naar de regel zelf</strong>"],
                             ["andere naam", "<strong>het utilitarisme</strong> of utilisme (van utilis, nuttig); wie zo denkt is een <strong>gevolgenethicus</strong>", "de deontologische ethiek; wie zo denkt is een <strong>plichtethicus</strong>"],
                             ["haar kernzin", "<strong>het resultaat beslist</strong>, <strong>zo veel mogelijk welzijn</strong>, <strong>soms mag een regel wijken</strong>",
                              "<strong>de daad zelf telt</strong>, <strong>sommige regels gelden altijd</strong>, <strong>het resultaat is niet beslissend</strong>"],
                             ["bij een leugen om bestwil", "<strong>goed</strong>: het resultaat is goed, dus de daad is goed",
                              "<strong>fout</strong>: <strong>liegen blijft liegen</strong>, ook met een goed resultaat"]])),
            ("p", "<strong>De twee geven dus niet altijd hetzelfde antwoord.</strong> Juist bij een leugen om "
                  "bestwil lopen ze uiteen, en daarom is het onderscheid zo bruikbaar: <strong>je ziet waarop "
                  "iemand zich baseert</strong>. In een discussie praten mensen vaak langs elkaar omdat de "
                  "een naar regels kijkt en de ander naar gevolgen."),
            ("p", "Let op één misvatting: <strong>volgens de gevolgenethiek telt niet enkel de bedoeling van "
                  "de dader</strong>. Juist niet — de uitkomst telt, en een goede bedoeling met een slecht "
                  "gevolg blijft daar een slechte daad."),
            ("kader", tabel(["voorbeeld", "welke stroming"],
                            [["<strong>iemand liegt om een vriend te beschermen</strong>", "<strong>de gevolgenethiek</strong>"],
                             ["<strong>iemand houdt zijn belofte, ook al kost het hem veel</strong>", "<strong>de plichtethiek</strong>"],
                             ["<strong>een regering kiest de maatregel die het meeste mensen helpt</strong>",
                              "<strong>de gevolgenethiek</strong>: het grootste geluk voor het grootste aantal"],
                             ["<strong>een arts vertelt een patiënt de harde waarheid</strong>",
                              "<strong>de plichtethiek</strong>: eerlijkheid is een plicht, ook als het pijn doet"]])),
        ]),
        dict(kop="De bezwaren", blokken=[
            ("kader", tabel(["tegen de gevolgenethiek", "tegen de plichtethiek"],
                            [["<strong>gevolgen zijn niet te voorspellen</strong>, <strong>een minderheid kan erbij inschieten</strong>, <strong>ze kan elk middel goedpraten</strong>",
                              "<strong>ze is soms hardvochtig</strong>: wie nooit mag liegen, moet ook de vluchteling in zijn kelder verraden"]])),
            ("p", "Dat de gevolgenethiek niet naar mensen zou kijken, klopt niet: ze kijkt juist naar hun "
                  "welzijn samen. En daarom gebruiken mensen in de praktijk vaak <strong>beide</strong> "
                  "stromingen: <strong>elk antwoord heeft zijn grens</strong>. Wie enkel op regels let, wordt "
                  "hard; wie enkel op gevolgen let, praat te veel goed."),
        ]),
        dict(kop="Vier filosofen", blokken=[
            ("p", "<strong>Kant en Bentham horen niet tot dezelfde stroming</strong>: ze staan precies "
                  "tegenover elkaar. En <strong>de vier leefden niet in dezelfde eeuw</strong>."),
            ("kader", tabel(["filosoof", "wanneer en waar", "stroming en kerngedachte"],
                            [["<strong>Immanuel Kant</strong>", "<strong>Duitsland</strong> (Koningsbergen), <strong>de achttiende eeuw</strong>",
                              "<strong>de plichtethiek</strong>. Zijn toets bij een daad: <strong>mag iedereen dit doen?</strong> En: <strong>je mag een mens nooit louter als middel gebruiken</strong>"],
                             ["<strong>Jeremy Bentham</strong>", "<strong>Engeland</strong>, rond 1800",
                              "<strong>de gevolgenethiek</strong>. Van hem komt <strong>het grootste geluk voor het grootste aantal</strong>"],
                             ["<strong>John Stuart Mill</strong>", "Engeland, de negentiende eeuw",
                              "<strong>gevolgenethicus</strong>; <strong>hij bouwt op Bentham voort</strong> en voegt toe dat <strong>geluk ook kwaliteit heeft</strong>: niet elk genot weegt gelijk"],
                             ["<strong>Peter Singer</strong>", "Australië, <strong>hij leeft vandaag nog</strong> (geboren in 1946)",
                              "<strong>de gevolgenethiek</strong>: <strong>hij weegt het lijden af</strong>, en daarom telt bij hem ook dierenleed mee"]])),
            ("p", "<strong>Bentham en Mill zijn dus beide Engels</strong>, en Mill kende Benthams werk van "
                  "jongs af. <strong>Singer is de filosoof die in twee hoofdstukken van de fiche "
                  "terugkomt</strong>: bij mens en dier én bij de ethische stromingen. Zijn werk over "
                  "<strong>dierenrechten</strong> volgt rechtstreeks uit zijn ethiek."),
            ("p", "Zo breng je een uitspraak thuis. <strong>Je mag nooit martelen, ook niet om tien mensen "
                  "te redden</strong> is <strong>Kant</strong>: de regel geldt onvoorwaardelijk. <strong>We "
                  "moeten geld geven zolang het meer leed voorkomt dan het ons kost</strong> is "
                  "<strong>Singer</strong>, letterlijk zijn bekendste argument over armoede en hulp."),
            ("weetje", "Weten waar en wanneer een filosoof leefde is nuttig, want <strong>zijn tijd kleurt "
                       "zijn antwoord</strong>. Bentham dacht in een tijd van hervormingen, Kant in de eeuw "
                       "van de rede."),
        ]),
    ])


# ───────────────────────── 15. Begrippen uit de moraalfilosofie
zet("begrippen-uit-de-moraalfilosofie",
    titel="Begrippen uit de moraalfilosofie",
    onder="Waarden en normen, het moreel dilemma, goed en kwaad met het moreel relativisme, en het paar vrijheid en verantwoordelijkheid.",
    secties=[
        dict(kop="Waarden en normen", blokken=[
            ("p", "De fiche noemt bij de moraalfilosofie vier begrippen: <strong>het moreel "
                  "dilemma</strong>, <strong>waarden en normen</strong>, <strong>vrijheid en "
                  "verantwoordelijkheid</strong> en goed en kwaad. Monisme en dualisme horen bij de "
                  "antropologie, niet hier."),
            ("kader", tabel(["", "een waarde", "een norm"],
                            [["wat het is", "<strong>iets wat je belangrijk vindt</strong>", "<strong>een regel die uit een waarde volgt</strong>"],
                             ["wat ze zegt", "wat nastreefbaar is, <strong>het doel</strong>", "wat je dus moet doen, <strong>concreet</strong>"],
                             ["voorbeelden", "<strong>eerlijkheid</strong>, <strong>vrijheid</strong>, <strong>respect</strong>, solidariteit",
                              "<strong>je mag niet stelen</strong>, <strong>je laat anderen uitspreken</strong>"]])),
            ("p", "<strong>Een norm en een waarde betekenen dus niet hetzelfde</strong>: de waarde is het "
                  "doel, de norm de regel ernaartoe. <strong>Uit één waarde kunnen meerdere normen "
                  "voortkomen</strong>: uit eerlijkheid volgt niet stelen, niet liegen én niet bedriegen bij "
                  "een examen. Daarom kunnen <strong>twee culturen dezelfde waarde anders invullen: de "
                  "normen verschillen</strong>. Beide kunnen respect belangrijk vinden en toch andere regels "
                  "hebben over begroeten of kleding."),
            ("p", "Over normen klopt: <strong>ze volgen uit waarden</strong>, <strong>ze verschillen per "
                  "cultuur</strong> en <strong>ze zijn concreet</strong>. En waarden blijven nodig náást "
                  "normen, want <strong>ze geven de reden van de regel</strong>: wie enkel de regel kent, "
                  "weet niet waarom ze er is, en kan ze dus ook niet wegen in een dilemma."),
        ]),
        dict(kop="Het moreel dilemma", blokken=[
            ("p", "Een moreel dilemma is <strong>een keuze met twee opties die beide iets kosten</strong>: "
                  "welke kant je ook kiest, je schendt iets waardevols. <strong>Er botsen twee waarden met "
                  "elkaar</strong> — eerlijkheid tegen trouw, vrijheid tegen veiligheid — en die botsing "
                  "maakt het dilemma."),
            ("kader", tabel(["situatie", "welke waarden botsen"],
                            [["<strong>liegen of iemand kwetsen</strong>", "eerlijkheid tegen zorg voor de ander"],
                             ["<strong>een vriend verklikken of zwijgen</strong>", "<strong>eerlijkheid en trouw</strong>"],
                             ["<strong>één leven redden of vijf</strong>", "het ene leven tegen de vijf andere"],
                             ["<strong>een arts met één bed en twee patiënten</strong>", "wie hij ook kiest, hij laat de andere in de kou staan"],
                             ["<strong>een wet die roken in een café verbiedt</strong>", "<strong>vrijheid en gezondheid</strong>"]])),
            ("p", "Bij koffie of thee staat er niets moreel op het spel; dat is dus geen dilemma. Over een "
                  "moreel dilemma klopt: <strong>er is geen pijnloze keuze</strong>, <strong>twee waarden "
                  "botsen</strong> en <strong>je moet je keuze verantwoorden</strong>. <strong>Het lost zich "
                  "dus niet vanzelf op</strong>: je moet kiezen, en die keuze verantwoorden. Dat doe je "
                  "<strong>met argumenten volgens AUB</strong>, dus <strong>met een argument en een "
                  "voorbeeld</strong>."),
        ]),
        dict(kop="Goed en kwaad", blokken=[
            ("p", "Goed en kwaad is een filosofisch begrippenpaar omdat <strong>het om een maatstaf "
                  "vraagt</strong>: zodra je iets goed noemt, moet je zeggen waaraan je dat afmeet. "
                  "<strong>Wat als goed geldt, kan per cultuur verschillen</strong>; of er ook iets "
                  "universeel goed is, blijft een filosofische vraag."),
            ("p", "<strong>Het moreel relativisme</strong> zegt dat <strong>goed afhangt van de "
                  "cultuur</strong>: elke groep bepaalt zelf wat goed is. Het bezwaar daartegen is scherp: "
                  "<strong>je kan dan niets meer afkeuren</strong>. Als alles van de cultuur afhangt, is er "
                  "geen grond om slavernij of onrecht elders slecht te noemen."),
            ("p", "<strong>De vraag naar goed en kwaad is niet met onderzoek te beslechten</strong>: "
                  "onderzoek toont wat mensen vinden, niet wat goed is. Over goed en kwaad klopt dus: "
                  "<strong>ze vragen om argumenten</strong>, <strong>ze verschillen in normen per "
                  "cultuur</strong> en <strong>ze staan centraal in de ethiek</strong>."),
        ]),
        dict(kop="Vrijheid en verantwoordelijkheid", blokken=[
            ("p", "Die twee staan in de fiche naast elkaar, en niet toevallig: <strong>verantwoordelijkheid "
                  "veronderstelt vrijheid</strong>. <strong>Zonder keuze geen schuld</strong> — je bent "
                  "enkel verantwoordelijk voor wat je ook anders had kunnen doen. Wie niet kon kiezen, kan je "
                  "niets verwijten."),
            ("p", "<strong>Vrijheid is in de ethiek niet hetzelfde als doen wat je wil.</strong> Ze betekent "
                  "kunnen kiezen en die keuze verantwoorden, niet dat alles mag. Over vrijheid klopt: "
                  "<strong>ze maakt kiezen mogelijk</strong>, <strong>ze brengt verantwoordelijkheid "
                  "mee</strong> en <strong>ze kan beperkt zijn</strong> — de vrijheid van de ander begrenst "
                  "de jouwe."),
            ("kader", tabel(["geval", "wat met de verantwoordelijkheid gebeurt"],
                            [["<strong>iemand handelt onder bedreiging</strong>",
                              "<strong>ze wordt kleiner</strong>: zijn vrijheid was beperkt, en daarom weegt dwang in een rechtszaak mee"],
                             ["<strong>een kind van vier breekt iets met opzet</strong>",
                              "<strong>ze is beperkt</strong>: verantwoordelijkheid groeit met het vermogen gevolgen te overzien, en daarom kent het recht een leeftijdsgrens"]])),
            ("p", "Daar duikt het <strong>probleem van de vrije wil</strong> op: <strong>misschien kiezen we "
                  "niet echt</strong>. Als alles door brein en omstandigheden bepaald is, wankelt de hele "
                  "schuldvraag — en daar raakt dit hoofdstuk aan lichaam en geest."),
            ("weetje", "De fiche vraagt deze begrippen op echte vraagstukken toe te passen, want <strong>los "
                       "blijven ze te abstract</strong>. Pas bij een echte casus merk je hoe waarden botsen "
                       "en wat je argument waard is."),
        ]),
    ])


# ───────────────────────── 16. Ethische vraagstukken analyseren
zet("ethische-vraagstukken-analyseren",
    titel="Ethische vraagstukken analyseren",
    onder="De vijf vraagstukken van de fiche, de waarden die er botsen, hoe je een argument bij een stroming thuisbrengt, en wat een drogreden is.",
    secties=[
        dict(kop="Hoe je een vraagstuk aanpakt", blokken=[
            ("p", "<strong>De eerste stap is de botsende waarden benoemen.</strong> Zolang je niet weet welke "
                  "waarden botsen, weet je niet waarover de discussie echt gaat. Bij een ethisch vraagstuk "
                  "<strong>botsen vaak twee waarden die beide echt zijn</strong>; daarom is het een "
                  "vraagstuk en geen rekensom."),
            ("p", "De analyse heeft drie stappen: <strong>de waarden benoemen</strong>, <strong>de "
                  "argumenten van beide kanten zoeken</strong> en <strong>je eigen argument opbouwen</strong>. "
                  "Overtuigen is geen onderdeel van de opdracht. Je moet de tegenargumenten kennen, want "
                  "<strong>anders staat je eigen argument zwak</strong>: wie de bezwaren niet kent, kan ze "
                  "ook niet weerleggen."),
            ("p", "De fiche vraagt <strong>een argument volgens AUB</strong>, voor of tegen, en "
                  "<strong>een eigen standpunt met argumenten</strong>. Je maakt het concreet <strong>met een "
                  "voorbeeld</strong>, de B van bijvoorbeeld. Let op wat beoordeeld wordt: <strong>de "
                  "kwaliteit van je argument</strong>, je uitleg en je voorbeeld. Welk standpunt je "
                  "verdedigt, is aan jou."),
            ("p", "<strong>Een argument is sterker dan een mening omdat het een reden geeft</strong>: een "
                  "mening zegt wat je vindt, een argument waarom, en pas dan kan de ander erop ingaan. En "
                  "deze vraagstukken zijn filosofisch en niet juridisch omdat <strong>ze vragen wat zou "
                  "moeten</strong>: de wet zegt wat geldt, de ethiek vraagt of dat ook juist is."),
            ("p", "<strong>Een drogreden</strong> is <strong>een argument dat niet geldig is maar wel "
                  "overtuigend klinkt</strong>. De bekendste: <strong>dat doet toch iedereen</strong>, of "
                  "<strong>iedereen vindt dat toch</strong>. Dat veel mensen iets doen of vinden, zegt niet "
                  "dat het goed is; dat heet een beroep op de meerderheid."),
        ]),
        dict(kop="De vijf vraagstukken", blokken=[
            ("p", "De fiche noemt er <strong>vijf</strong>: <strong>anticonceptie</strong>, "
                  "<strong>genderdiversiteit</strong>, <strong>abortus</strong>, <strong>dierenrechten</strong> "
                  "en <strong>risicogedrag bij jongeren</strong>."),
            ("kader", tabel(["vraagstuk", "wat de fiche erbij noemt", "welke waarden botsen"],
                            [["<strong>anticonceptie</strong>", "onder meer een voorgestelde leeftijdsgrens",
                              "<strong>bescherming en zelfbeschikking</strong>: een jongere beschermen tegen een onomkeerbare keuze, tegenover zijn recht zelf te beslissen"],
                             ["<strong>genderdiversiteit</strong>", "<strong>genderidentiteit</strong>, <strong>gendergelijkheid</strong> en <strong>genderongelijkheid</strong>",
                              "gelijkheid en rechtvaardigheid; <strong>genderongelijkheid is ongelijke kansen door geslacht</strong>, met de loonkloof als bekendste voorbeeld"],
                             ["<strong>abortus</strong>", "—",
                              "<strong>de zelfbeschikking</strong> van de vrouw en <strong>de bescherming van het leven</strong> (de levensbescherming), <strong>allebei tegelijk</strong>"],
                             ["<strong>dierenrechten</strong>", "<strong>een verbod op dierenproeven</strong> en <strong>circusdieren</strong>",
                              "bij circusdieren <strong>dierenwelzijn en vrij ondernemen</strong>"],
                             ["<strong>risicogedrag bij jongeren</strong>", "<strong>alcoholgebruik</strong>, <strong>druggebruik</strong> en <strong>experimenteren met seks</strong>",
                              "<strong>de vrijheid van de jongere tegenover zijn bescherming</strong>"]])),
            ("p", "<strong>Zelfbeschikking</strong>, ook <strong>autonomie</strong> genoemd, is de waarde die "
                  "bij bijna elk vraagstuk terugkomt: zelf beslissen over je lichaam. <strong>Anticonceptie "
                  "verplichten raakt dus aan de lichamelijke zelfbeschikking</strong>, want verplichten "
                  "betekent ingrijpen in iemands lichaam zonder zijn toestemming."),
            ("p", "Twee misvattingen. <strong>Het abortusdebat is niet met één argument beslecht</strong>: "
                  "het is net een vraagstuk omdat beide kanten zwaarwegende waarden aanvoeren. En "
                  "<strong>genderidentiteit is niet wat anderen over iemand denken</strong>, maar hoe iemand "
                  "zichzelf ervaart. <strong>Gendergelijkheid betekent dat iedereen dezelfde kansen krijgt, "
                  "los van geslacht</strong>: in onderwijs, werk en loon."),
        ]),
        dict(kop="Een argument thuisbrengen bij een stroming", blokken=[
            ("p", "<strong>Of een argument bij de gevolgen- of de plichtethiek hoort, blijft niet buiten "
                  "beschouwing</strong>: de fiche vraagt juist om dat te beargumenteren. Let dus op de vorm "
                  "van de redenering, niet op het standpunt."),
            ("kader", tabel(["argument", "welke stroming", "waaraan je dat ziet"],
                            [["<strong>het leed weegt zwaarder dan de winst</strong> (tegen dierenproeven)",
                              "<strong>de gevolgenethiek</strong>", "er wordt <strong>afgewogen</strong>: hoeveel leed tegen hoeveel baat"],
                             ["<strong>een dier mag geen middel zijn</strong> (tegen dierenproeven)",
                              "<strong>de plichtethiek</strong>", "de daad zelf is fout, los van wat ze opbrengt"],
                             ["<strong>een leeftijdsgrens voorkomt meer schade</strong>",
                              "<strong>de gevolgenethiek</strong>", "er wordt gerekend met de schade die je voorkomt"]])),
            ("p", "<strong>De gevolgenethiek, het utilitarisme, is de stroming die leed tegen baat afweegt</strong>; Peter "
                  "Singer argumenteert zo over dierenleed. En <strong>bij de plichtethiek beslist de uitkomst "
                  "niét</strong> of een daad goed is — daar telt de daad zelf."),
            ("p", "Bij risicogedrag duikt nog een begrip op: <strong>paternalisme</strong>, "
                  "<strong>beslissen voor iemands eigen bestwil</strong>. Je beschermt iemand tegen zichzelf, "
                  "en het bezwaar is dat je hem zijn eigen keuze afneemt. De waarde die ervoor pleit jongeren "
                  "zelf te laten beslissen, is <strong>de vrijheid</strong> of de zelfbeschikking."),
            ("p", "Drie vragen helpen de analyse van risicogedrag vooruit: <strong>wie draagt de "
                  "schade</strong>, <strong>kon de jongere dit overzien</strong> en <strong>welke waarden "
                  "botsen hier</strong>. Verantwoordelijkheid weegt daarbij mee omdat <strong>ze groeit met "
                  "het overzicht</strong>: wie de gevolgen nog niet overziet, is minder verantwoordelijk, en "
                  "daarom kent het recht leeftijdsgrenzen."),
            ("p", "Over de vijf vraagstukken klopt ten slotte: <strong>er botsen waarden</strong>, "
                  "<strong>beide kanten hebben argumenten</strong> en <strong>je analyseert ze met de "
                  "stromingen</strong>. Juist dat er geen eenvoudig juist antwoord is, maakt ze tot "
                  "vraagstukken."),
        ]),
    ])

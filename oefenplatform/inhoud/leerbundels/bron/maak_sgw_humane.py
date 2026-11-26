# -*- coding: utf-8 -*-
"""Leerbundels, oefenbundels en uitlegbladen bij het politieke blok van
sociale en gedragswetenschappen 🌍 Beyond doorstroom, enkel voor humane
wetenschappen.

Gebaseerd op de vakfiche `Sociale_en_gedragswetenschappen_3DDO` (humane
wetenschappen), het deel politieke wetenschappen: politiek en democratie, de
Belgische staat, partijen en verkiezingen, participatie, het recht in de
samenleving en globalisering. Zes thema's, één bundel per thema, die Kim bij
deel 1, deel 2 en het pittige hoofdstuk oplaadt.

De afspraak blijft dezelfde als in `maak_sgw.py`: een bundel dekt elke vraag
van zijn hoofdstuk (`../../beyond/sociale-en-gedragswetenschappen.json`), met
dezelfde woorden als de vraag. Partijen worden neutraal beschreven, met de
ideologie waartoe ze gewoonlijk gerekend worden. De zetels van 2024 komen uit
de officiële uitslag van de FOD Binnenlandse Zaken.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Sociale en gedragswetenschappen"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

W = "130px"
WW = "200px"
WL = "260px"

BUNDELS = {}
OEFENBUNDELS = {}
UITLEGBLADEN = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een situatie: zeg niet alleen welk begrip het is, maar ook waaraan je het ziet.",
    "Lees bij twee begrippen die op elkaar lijken eerst nog eens wat ze onderscheidt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ═════════════════════════ 1. Politiek, democratie en de rechtstaat
S1 = "humane-wetenschappen-politiek-democratie-en-de-rechtstaat-beyond-doorstroom"
BUNDELS[S1] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: politiek, democratie en de rechtstaat",
    onder="Welke staats- en regeringsvormen er zijn, wat een directe en een indirecte democratie is, en de principes van een democratische rechtstaat.",
    secties=[
        dict(kop="Staats- en regeringsvormen", blokken=[
            ("p", "Wie heeft de macht in een land, en hoe kreeg die persoon of groep ze? Daarop "
                  "antwoorden de <strong>staats- en regeringsvormen</strong>. Veel namen komen uit het "
                  "Grieks, en de betekenis van dat Griekse woord helpt je om ze te onthouden."),
            ("p", tabel(["Vorm", "Wie heeft de macht?", "Woord om te onthouden"], [
                ["democratie", "het volk, rechtstreeks of via gekozen vertegenwoordigers", "demos = volk, kratos = macht"],
                ["dictatuur", "één persoon of één partij, zonder vrije verkiezingen", "oppositie wordt vaak onderdrukt"],
                ["monarchie", "een vorst als staatshoofd, die zijn plaats meestal erft", "koning, koningin, vorst"],
                ["republiek", "een staatshoofd dat zijn plaats niet erft, maar verkozen of aangeduid wordt", "meestal een president"],
                ["oligarchie", "een kleine groep, zoals rijke families of legerleiders", "oligos = weinig"],
                ["theocratie", "religieuze leiders, in naam van een god", "theos = god"],
            ])),
            ("kader", "<strong>Monarchie en republiek zeggen iets over het staatshoofd, niet over de "
                      "vrijheid.</strong> Een land kan tegelijk een monarchie en een democratie zijn: "
                      "België heeft een koning, maar het volk kiest het parlement en de koning heeft geen "
                      "eigen politieke macht. Omgekeerd is niet elke republiek een democratie: ook een "
                      "dictatuur kan zich republiek noemen."),
            ("p", "Herken de vorm in een situatie aan één vraag: <strong>bij wie ligt de macht, en hoe "
                  "kwam ze daar?</strong> Hogepriesters die wetten maken uit een godsdienst: theocratie. "
                  "Vijf rijke families zonder verkiezingen: oligarchie. Een president die om de vijf jaar "
                  "gekozen wordt: republiek."),
        ]),
        dict(kop="Directe en indirecte democratie", blokken=[
            ("p", tabel(["", "Directe democratie", "Indirecte democratie"], [
                ["andere naam", "rechtstreekse democratie", "representatieve democratie"],
                ["wie beslist?", "de burgers zelf", "gekozen vertegenwoordigers, in naam van de burgers"],
                ["voorbeeld", "een volksvergadering op het plein, een volksraadpleging", "het parlement in België"],
            ])),
            ("p", "<strong>Representeren</strong> betekent vertegenwoordigen. Bij de verkiezingen kies je "
                  "een volksvertegenwoordiger, en die stemt de volgende jaren in het parlement over de wetten."),
            ("kader", "<strong>Waarom grote landen bijna altijd indirect werken:</strong> met miljoenen "
                      "burgers is het niet haalbaar dat iedereen over elke wet meebeslist. Een "
                      "rechtstreekse stemming blijft wel mogelijk voor één vraag."),
        ]),
        dict(kop="De democratische rechtstaat", blokken=[
            ("p", "Een <strong>democratische rechtstaat</strong> is een democratie waarin ook de overheid "
                  "zich aan de wet moet houden. Niemand staat boven de wet, ook de regering niet: een burger "
                  "kan zelfs naar de rechter stappen tegen een beslissing van de overheid. Vijf principes:"),
            ("p", tabel(["Principe", "Wat het betekent"], [
                ["grondwet of constitutie", "de hoogste wet, met de grondrechten en de werking van de staat"],
                ["grondrechten", "de fundamentele rechten en vrijheden van iedereen"],
                ["meerderheidsprincipe", "het voorstel met de meeste stemmen wordt aangenomen, binnen de grenzen van de grondwet"],
                ["scheiding der machten", "wetten maken, uitvoeren en erover oordelen gebeurt door verschillende instellingen"],
                ["onafhankelijke en onpartijdige rechtspraak", "de rechter staat niet onder druk en kiest geen kant"],
            ])),
            ("p", tabel(["Macht", "Instelling", "Voorbeeld bij een rookverbod in de auto"], [
                ["wetgevende macht", "het parlement", "keurt de wet goed"],
                ["uitvoerende macht", "de regering", "de minister regelt de controles en een campagne"],
                ["rechterlijke macht", "de hoven en rechtbanken", "een rechter legt een boete op"],
            ])),
            ("kader", "<strong>De machten controleren elkaar</strong>, zodat niemand zijn macht kan "
                      "misbruiken. Het parlement stelt vragen aan een minister en kan de regering wegsturen. "
                      "Een president die rechters ontslaat omdat hun oordeel hem niet bevalt, schendt de "
                      "onafhankelijkheid van de rechterlijke macht. Verkiezingen alleen maken dus nog geen "
                      "volwaardige rechtstaat."),
            ("weetje", "<strong>Onafhankelijk en onpartijdig zijn niet hetzelfde.</strong> Onafhankelijk: de "
                       "rechter staat niet onder druk van een andere macht. Onpartijdig: hij kiest geen kant "
                       "en heeft geen belang in de zaak."),
            ("p", "De meerderheid beslist, maar mag de grondrechten van een minderheid <strong>niet</strong> "
                  "afschaffen. De grondrechten beschermen net ook wie in de minderheid is."),
        ]),
    ],
    onthoud=[
        "Democratie, dictatuur, monarchie, republiek, oligarchie, theocratie: vraag telkens bij wie de macht ligt.",
        "Monarchie en republiek gaan over het staatshoofd; een monarchie kan een democratie zijn.",
        "Direct: de burgers beslissen zelf. Indirect of representatief: ze kiezen vertegenwoordigers.",
        "Rechtstaat: grondwet, grondrechten, meerderheidsprincipe, scheiding der machten, onafhankelijke en onpartijdige rechtspraak.",
        "Parlement maakt, regering voert uit, hoven en rechtbanken oordelen. Ze controleren elkaar.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S1] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: politiek, democratie en de rechtstaat",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke vorm is het?",
             opdracht="Schrijf bij elke situatie de staats- of regeringsvorm.",
             oefeningen=[
                 ("rij", [("de wetten komen uit een godsdienst en religieuze leiders beslissen", "theocratie"),
                          ("een kleine groep legerleiders heeft alle macht", "oligarchie"),
                          ("de burgers kiezen om de vijf jaar een president", "republiek"),
                          ("één partij heeft alle macht en verbiedt de oppositie", "dictatuur")],
                  "Welke vorm?", WW),
                 ("waar", "Elke republiek is ook een democratie.", False),
                 ("open", "Leg uit hoe België tegelijk een monarchie en een democratie kan zijn.",
                  "België heeft een koning als staatshoofd, die zijn plaats erft: dat is de monarchie. "
                  "Maar het volk kiest het parlement en de koning heeft geen eigen politieke macht: dat is "
                  "de democratie.", 4),
             ]),
        dict(kop="Direct of indirect",
             opdracht="Zeg of het om een directe of een indirecte democratie gaat.",
             oefeningen=[
                 ("rij", [("de inwoners stemmen met opgestoken hand op het plein", "direct"),
                          ("je kiest een volksvertegenwoordiger voor vijf jaar", "indirect"),
                          ("het parlement keurt een nieuwe wet goed", "indirect"),
                          ("de burgers stemmen zelf over één vraag", "direct")],
                  "Direct of indirect?", W),
                 ("kort", "Een andere naam voor een indirecte democratie is een ... democratie.", "representatieve", WW),
                 ("open", "Waarom werken grote landen bijna altijd met een indirecte democratie?",
                  "Met miljoenen burgers is het praktisch onmogelijk dat iedereen over elke wet "
                  "meebeslist. Daarom kiezen de burgers vertegenwoordigers die in hun naam beslissen.", 3),
             ]),
        dict(kop="De drie machten",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Macht", "Instelling"],
                  [["wetgevende macht", None], ["uitvoerende macht", None], ["rechterlijke macht", None]],
                  "het parlement; de regering; de hoven en rechtbanken", WL),
                 ("rij", [("een minister regelt de controles op een nieuwe wet", "uitvoerende"),
                          ("een rechter legt een boete op", "rechterlijke"),
                          ("het parlement keurt een wet goed", "wetgevende")],
                  "Welke macht is aan het werk?", WW),
                 ("kies", "Welk voorbeeld toont dat de machten elkaar controleren?",
                  ["het parlement stelt vragen aan een minister",
                   "de regering ontslaat een rechter na een vonnis",
                   "een rechter schrijft zelf een nieuwe wet",
                   "de president schaft het parlement af"], 0),
             ]),
        dict(kop="De rechtstaat",
             opdracht="Lees de situatie en antwoord.",
             oefeningen=[
                 ("waar", "In een democratische rechtstaat mag de meerderheid de grondrechten van een minderheid afschaffen.", False),
                 ("waar", "In een rechtstaat moet ook de regering zich aan de wetten houden.", True),
                 ("open", "In Kastelland ontslaat de president drie rechters omdat ze tegen zijn wet "
                          "beslisten. Welk principe wordt geschonden, en waarom is dat gevaarlijk?",
                  "De onafhankelijkheid van de rechterlijke macht. Als rechters onder druk staan van de "
                  "president, kunnen ze hem niet meer controleren en kan hij zijn macht misbruiken.", 4),
                 ("open", "Wat is het verschil tussen een onafhankelijke en een onpartijdige rechter?",
                  "Onafhankelijk: hij staat niet onder druk van een andere macht, zoals de regering. "
                  "Onpartijdig: hij kiest geen kant en heeft geen belang in de zaak.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S1] = dict(reeksen=[
    dict(aanpak="Stel telkens de vraag: bij wie ligt de macht, en hoe kwam die persoon of groep eraan?",
         waarom=["Let op de president: een verkozen staatshoofd maakt een republiek, geen monarchie.",
                 "Een dictatuur kan zich ook republiek noemen. Republiek zegt iets over het staatshoofd, niet over vrije verkiezingen.",
                 "Noem beide kanten: het staatshoofd (koning) en wie de macht heeft (het volk via het parlement)."]),
    dict(aanpak="Kijk wie de beslissing neemt: de burgers zelf of iemand die ze gekozen hebben.",
         waarom=["Een wet in het parlement lijkt een beslissing van het volk, maar gekozen vertegenwoordigers nemen ze: indirect.",
                 None,
                 "Noem de reden: het aantal burgers maakt het praktisch onmogelijk."]),
    dict(aanpak="Maken, uitvoeren, oordelen: koppel het werkwoord aan de instelling.",
         waarom=[None, "Een minister voert uit, ook al lijkt een controle op een straf.",
                 "De andere voorbeelden nemen net het werk of de vrijheid van een andere macht af."]),
    dict(aanpak="Een rechtstaat beschermt ook wie in de minderheid is en zet niemand boven de wet.",
         waarom=["Het meerderheidsprincipe geldt binnen de grenzen van de grondwet.",
                 None,
                 "Noem het principe en het gevaar: geen controle meer, dus machtsmisbruik.",
                 "Onafhankelijk gaat over druk van buiten, onpartijdig over de houding van de rechter zelf."]),
])

# ═════════════════════════ 2. De Belgische staat en zijn bestuursniveaus
S2 = "humane-wetenschappen-de-belgische-staat-en-zijn-bestuursniveaus-beyond-doorstroom"
BUNDELS[S2] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: de Belgische staat en zijn bestuursniveaus",
    onder="Unitair, federaal en confederaal; de gemeenschappen en gewesten; de vier bestuursniveaus met hun organen, en de controleorganen.",
    secties=[
        dict(kop="Van unitair naar federaal", blokken=[
            ("p", tabel(["Staatsvorm", "Waar ligt de macht?"], [
                ["unitaire staat", "bij één centrale overheid die alle belangrijke beslissingen neemt"],
                ["federale staat", "verdeeld tussen een centrale overheid en deelstaten met elk eigen bevoegdheden"],
                ["confederale staat", "bij zelfstandige staten die enkel enkele taken samen doen, zoals defensie of een munt"],
            ])),
            ("p", "Van de meest naar de minst centrale macht: <strong>unitair, federaal, confederaal</strong>."),
            ("p", "België begon in 1830 als <strong>unitaire</strong> staat. Sinds <strong>1970</strong> waren er "
                  "<strong>zes staatshervormingen</strong>, en elke keer kregen de gemeenschappen en gewesten "
                  "meer bevoegdheden. Sinds <strong>1993</strong> staat in het eerste artikel van de grondwet "
                  "dat België een <strong>federale staat</strong> is."),
            ("kader", "<strong>Waarom?</strong> Door de tegenstellingen tussen Nederlandstaligen en "
                      "Franstaligen. Vlamingen wilden meer zelfbestuur voor hun taal en cultuur, Walen meer "
                      "economische zelfstandigheid. Federaal komt van <em>foedus</em>, verbond."),
        ]),
        dict(kop="Gemeenschappen en gewesten", blokken=[
            ("p", tabel(["", "Gemeenschappen", "Gewesten"], [
                ["gebaseerd op", "taal, dus op personen", "grondgebied"],
                ["welke?", "Vlaamse, Franse en Duitstalige Gemeenschap", "Vlaams, Waals en Brussels Hoofdstedelijk Gewest"],
                ["bevoegd voor", "onderwijs, cultuur, taalgebruik, een groot deel van welzijn en gezondheid", "economie, ruimtelijke ordening, milieu, wonen, landbouw, openbare werken"],
            ])),
            ("p", "De <strong>federale overheid</strong> blijft bevoegd voor wat het hele land aangaat: "
                  "defensie, justitie, buitenlandse zaken, financiën en de sociale zekerheid."),
            ("kader", "<strong>Vraag je af: gaat het over een persoon of over de grond?</strong> De eindtermen "
                      "van een school in Gent: onderwijs, dus de Vlaamse Gemeenschap. Een milieuvergunning "
                      "voor een fabriek in Namen: milieu, dus het Waals Gewest."),
            ("weetje", "Het Duitstalige gebied heeft een eigen gemeenschap maar geen eigen gewest: voor de "
                       "gewestbevoegdheden hoort het bij het Waals Gewest. In Vlaanderen zijn gemeenschap en "
                       "gewest samengevoegd: er is één Vlaams Parlement en één Vlaamse Regering."),
        ]),
        dict(kop="Vier bestuursniveaus en hun organen", blokken=[
            ("p", tabel(["Niveau", "Maakt de regels", "Voert uit", "Naam van de regel"], [
                ["federaal", "federaal parlement: Kamer (150 leden) en Senaat", "federale regering", "wet"],
                ["gemeenschappen en gewesten", "bv. Vlaams Parlement", "bv. Vlaamse Regering", "decreet (Brussel: ordonnantie)"],
                ["provincies", "provincieraad", "deputatie, met de gouverneur", ""],
                ["gemeenten", "gemeenteraad", "college van burgemeester en schepenen", ""],
            ])),
            ("p", "Een parlement heeft drie grote taken: <strong>regels maken</strong>, <strong>de regering "
                  "controleren</strong> en <strong>de begroting goedkeuren</strong>. Een kritische vraag aan een "
                  "minister is de controlefunctie. Verliest een regering het vertrouwen van de meerderheid, "
                  "dan kan het parlement ze wegsturen."),
            ("p", "Eén partij haalt in België bijna nooit alleen een meerderheid. Daarom vormen meerdere "
                  "partijen samen een <strong>coalitie</strong>. De partijen die niet in de regering zitten, "
                  "vormen de <strong>oppositie</strong>: ze controleren de regering en doen eigen voorstellen."),
        ]),
        dict(kop="De controleorganen", blokken=[
            ("p", tabel(["Orgaan", "Wat het doet", "Voorbeeld"], [
                ["Grondwettelijk Hof", "toetst wetten, decreten en ordonnanties aan de grondwet en de bevoegdheden, en kan ze vernietigen", "een decreet dat de vrijheid van onderwijs schendt"],
                ["Raad van State", "geeft advies over ontwerpen van regels en vernietigt onwettige beslissingen van een overheid", "een bouwvergunning die de regels niet volgde"],
                ["Hof van Cassatie", "kijkt of rechters de wet en de procedure juist toepasten, zonder de feiten opnieuw te beoordelen", "het hoogste hof van de gewone rechtbanken"],
            ])),
            ("kader", "<strong>Wet of beslissing?</strong> Gaat het over een wet of decreet: Grondwettelijk "
                      "Hof. Gaat het over een concrete beslissing van een overheid, zoals een vergunning: Raad "
                      "van State."),
        ]),
    ],
    onthoud=[
        "Unitair, federaal, confederaal: van meest naar minst centrale macht. België is federaal sinds 1993, na hervormingen sinds 1970.",
        "Gemeenschappen: taal en personen (onderwijs, cultuur). Gewesten: grondgebied (milieu, economie, wonen).",
        "Federaal: defensie, justitie, buitenlandse zaken, financiën, sociale zekerheid.",
        "Elk niveau heeft een orgaan dat regels maakt en een dat uitvoert. Vlaams Parlement maakt decreten.",
        "Grondwettelijk Hof: wetten en decreten. Raad van State: beslissingen van een overheid. Cassatie: de toepassing van het recht.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S2] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: de Belgische staat en zijn bestuursniveaus",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Unitair, federaal of confederaal",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["Staatsvorm", "Waar ligt de macht?"],
                  [["unitair", None], ["federaal", None], ["confederaal", None]],
                  "bij één centrale overheid; verdeeld tussen centrale overheid en deelstaten; bij zelfstandige staten die enkele taken samen doen", WL),
                 ("kort", "Sinds welk jaar staat in de grondwet dat België een federale staat is?", "1993", W),
                 ("waar", "België is een federale staat sinds de onafhankelijkheid in 1830.", False),
             ]),
        dict(kop="Gemeenschap, gewest of federaal",
             opdracht="Wie is bevoegd?",
             oefeningen=[
                 ("rij", [("de eindtermen van een school in Gent", "Vlaamse Gemeenschap"),
                          ("een milieuvergunning in Namen", "Waals Gewest"),
                          ("het leger", "federale overheid"),
                          ("een cultuurcentrum in Eupen", "Duitstalige Gemeenschap")],
                  "Wie is bevoegd?", WL),
                 ("open", "Leg uit waarom het Duitstalige gebied wel een gemeenschap heeft, maar geen gewest.",
                  "Gemeenschappen zijn gebaseerd op taal, en in dat gebied spreekt men Duits. Gewesten zijn "
                  "gebaseerd op grondgebied, en voor de gewestbevoegdheden hoort het gebied bij het Waals Gewest.", 3),
             ]),
        dict(kop="De organen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["Niveau", "Maakt de regels", "Voert uit"],
                  [["federaal", None, None], ["Vlaanderen", None, None], ["provincie", None, None], ["gemeente", None, None]],
                  "Kamer en Senaat, federale regering; Vlaams Parlement, Vlaamse Regering; provincieraad, deputatie met de gouverneur; gemeenteraad, college van burgemeester en schepenen", "180px"),
                 ("kort", "Hoe heet een regel van het Vlaams Parlement?", "een decreet", W),
                 ("kies", "Een parlementslid van de oppositie stelt een kritische vraag aan een minister. Welke taak van het parlement is dit?",
                  ["de controle op de regering", "regels maken", "de begroting goedkeuren", "recht spreken"], 0),
                 ("open", "Wat is het verschil tussen een coalitie en de oppositie?",
                  "Een coalitie is een groep partijen die samen een meerderheid vormen en regeren. De "
                  "oppositie zijn de partijen in het parlement die niet in de regering zitten; ze "
                  "controleren de regering.", 3),
             ]),
        dict(kop="De controleorganen",
             opdracht="Naar welk orgaan stap je?",
             oefeningen=[
                 ("rij", [("een decreet schendt de vrijheid van onderwijs", "Grondwettelijk Hof"),
                          ("de gemeente gaf een bouwvergunning zonder de regels te volgen", "Raad van State"),
                          ("een rechter paste de wet verkeerd toe", "Hof van Cassatie")],
                  "Welk orgaan?", WL),
                 ("waar", "Het Hof van Cassatie beoordeelt opnieuw of een verdachte de feiten echt gepleegd heeft.", False),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S2] = dict(reeksen=[
    dict(aanpak="Denk aan een schaal: hoe meer macht in het centrum, hoe unitairder.",
         waarom=[None, None, "België begon unitair. De federale staat kwam er stap voor stap, na 1970."]),
    dict(aanpak="Vraag je af: gaat het over personen (taal, school, cultuur) of over grond (milieu, wonen)?",
         waarom=["Eupen ligt in het Duitse taalgebied: cultuur is persoonsgebonden, dus de Duitstalige Gemeenschap.",
                 "Noem beide basissen: taal voor de gemeenschap, grondgebied voor het gewest."]),
    dict(aanpak="Elk niveau heeft twee organen: één dat regels maakt en één dat ze uitvoert.",
         waarom=[None, "Wet is federaal, decreet is Vlaams, ordonnantie is Brussels.",
                 "Vragen stellen is controleren. Regels maken en de begroting zijn de andere taken.",
                 "Noem bij beide wie erin zit en wat ze doen."]),
    dict(aanpak="Wet of decreet: Grondwettelijk Hof. Concrete beslissing van een overheid: Raad van State. Toepassing door een rechter: Cassatie.",
         waarom=[None, "Cassatie beoordeelt de feiten niet opnieuw, enkel of het recht juist werd toegepast."]),
])

# ═════════════════════════ 3. Ideologieën, partijen en verkiezingen
S3 = "humane-wetenschappen-ideologieen-partijen-en-verkiezingen-beyond-doorstroom"
BUNDELS[S3] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: ideologieën, partijen en verkiezingen",
    onder="Ideologieën en breuklijnen, de Vlaamse partijen en de links-rechtsas, hoe je een verkiezing analyseert, en de regeringsvorming.",
    secties=[
        dict(kop="Ideologieën en breuklijnen", blokken=[
            ("p", "Een <strong>ideologie</strong> is een samenhangend geheel van ideeën over hoe de samenleving "
                  "eruit moet zien. Een <strong>breuklijn</strong> is een blijvende tegenstelling in de "
                  "samenleving waarrond partijen ontstaan. België kent drie klassieke breuklijnen:"),
            ("p", tabel(["Breuklijn", "Tegenstelling", "Wat eruit groeide"], [
                ["levensbeschouwelijk", "kerk tegenover staat", "katholieke en liberale partijen"],
                ["sociaal-economisch", "arbeid tegenover kapitaal", "socialistische partijen en vakbonden"],
                ["communautair", "Nederlandstaligen tegenover Franstaligen", "Vlaams-nationale partijen, staatshervormingen, partijen per taalgroep"],
            ])),
            ("p", tabel(["Ideologie", "Kernidee"], [
                ["liberalisme", "vrijheid van het individu, beperkte rol voor de overheid in de economie"],
                ["socialisme en sociaaldemocratie", "gelijkheid en solidariteit, sterke overheid, sociale zekerheid, rechten van werknemers"],
                ["christendemocratie", "christelijke waarden, aandacht voor gezin, middenveld en verbondenheid"],
                ["ecologisme", "milieu, klimaat en toekomstige generaties centraal"],
                ["nationalisme", "het eigen volk of de eigen natie als belangrijkste gemeenschap, zoveel mogelijk zelf beslissen"],
            ])),
        ]),
        dict(kop="De Vlaamse partijen en de links-rechtsas", blokken=[
            ("p", tabel(["Partij", "Wordt gewoonlijk gerekend tot"], [
                ["Open Vld", "liberalisme"],
                ["Vooruit (vroeger sp.a, daarvoor BSP)", "sociaaldemocratie"],
                ["cd&v", "christendemocratie"],
                ["Groen", "ecologisme"],
                ["N-VA (centrumrechts) en Vlaams Belang (radicaal-rechts)", "Vlaams-nationalisme"],
                ["PVDA", "radicaal-links, met marxistische wortels"],
            ])),
            ("p", "Op de economische <strong>links-rechtsas</strong> gaat het over hoeveel de overheid moet "
                  "ingrijpen om welvaart te herverdelen. <strong>Links</strong>: meer herverdeling en een sterke "
                  "overheid. <strong>Rechts</strong>: meer vrije markt en minder belastingen. PVDA staat gewoonlijk "
                  "het verst links; Vooruit en Groen ook links; cd&v in het centrum; Open Vld, N-VA en Vlaams "
                  "Belang rechts."),
            ("kader", "<strong>De as is een vereenvoudiging.</strong> Een partij kan economisch eerder rechts "
                      "zijn en bij ethische thema's progressief, of omgekeerd."),
        ]),
        dict(kop="Een verkiezing analyseren", blokken=[
            ("p", tabel(["Criterium", "Vraag", "Voorbeelden"], [
                ["identificatie", "over welk bestuursniveau gaat het?", "gemeenteraad, provincieraad, Vlaams Parlement, Kamer, Europees Parlement"],
                ["actoren", "wie speelt mee?", "partijen, kiezers, media, belangenorganisaties zoals vakbonden en werkgeversorganisaties"],
                ["informatie", "waarmee vormen kiezers een mening?", "peilingen, campagne, debatten"],
                ["mechanismen", "welke regels gelden?", "kieswetgeving, stemprocedure, campagnefinanciering"],
                ["resultaat", "wie wint en verliest?", "politieke verschuivingen, regeringsvorming"],
            ])),
            ("p", "Een <strong>peiling</strong> is een schatting bij een steekproef van kiezers, een "
                  "momentopname met een foutenmarge. Ze kan kiezers beïnvloeden, maar is nooit de echte uitslag. "
                  "Regels over <strong>campagnefinanciering</strong> zorgen dat partijen met veel geld de "
                  "verkiezingen niet kunnen kopen."),
        ]),
        dict(kop="Van uitslag naar regering", blokken=[
            ("p", "Stemmen worden omgezet in <strong>zetels</strong>, en de zetels bepalen hoeveel gewicht een "
                  "partij heeft. In de Kamer van 150 zetels heb je minstens <strong>76</strong> zetels nodig "
                  "voor een meerderheid. Na de verkiezingen van 9 juni 2024 werd N-VA de grootste partij met 24 "
                  "zetels: ze had dus andere partijen nodig (bron: officiële uitslag, FOD Binnenlandse Zaken)."),
            ("p", "Na de verkiezingen onderhandelen partijen over een <strong>coalitie</strong> en een "
                  "<strong>regeerakkoord</strong>: de afspraken over wat de regering zal doen. De grootste partij "
                  "komt niet altijd in de regering; wie samen een meerderheid vindt, regeert."),
            ("kader", "<strong>Waarom duurt dat in België vaak lang?</strong> Een coalitie moet partijen "
                      "verzoenen die op de breuklijnen tegenover elkaar staan, en volgens de grondwet zitten er "
                      "in de federale regering Nederlandstalige én Franstalige partijen. Links en rechts samen in "
                      "een regering leidt vaak tot een compromis of uitstel."),
        ]),
    ],
    onthoud=[
        "Drie breuklijnen: kerk-staat (levensbeschouwelijk), arbeid-kapitaal (sociaal-economisch), taal (communautair).",
        "Liberalisme, socialisme, christendemocratie, ecologisme, nationalisme: ken het kernidee en een partij.",
        "Links: meer herverdeling. Rechts: meer vrije markt. De as is een vereenvoudiging.",
        "Verkiezing analyseren: identificatie, actoren, informatie, mechanismen, resultaat.",
        "Meerderheid in de Kamer: 76 van 150. Coalitie, regeerakkoord, oppositie.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S3] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: ideologieën, partijen en verkiezingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Breuklijnen",
             opdracht="Welke breuklijn zie je in het conflict?",
             oefeningen=[
                 ("rij", [("ruzie over subsidies voor katholieke scholen", "levensbeschouwelijk"),
                          ("werkgevers en vakbonden over de lonen", "sociaal-economisch"),
                          ("de taal in de gemeenten rond Brussel", "communautair")],
                  "Welke breuklijn?", WL),
                 ("kort", "Een blijvende tegenstelling waarrond partijen ontstaan, heet een ...", "breuklijn", WW),
             ]),
        dict(kop="Ideologieën en partijen",
             opdracht="Koppel en leg uit.",
             oefeningen=[
                 ("rij", [("Open Vld", "liberalisme"), ("Vooruit", "sociaaldemocratie"),
                          ("cd&v", "christendemocratie"), ("Groen", "ecologisme")],
                  "Tot welke ideologie wordt de partij gewoonlijk gerekend?", WW),
                 ("rij", [("lagere belastingen en vrij ondernemen", "liberalisme"),
                          ("hogere minimumlonen en sterke sociale zekerheid", "socialisme"),
                          ("meer zelfbestuur voor het eigen volk", "nationalisme")],
                  "Welke ideologie past bij dit standpunt?", WW),
                 ("waar", "Een partij staat bij elk thema op precies dezelfde plaats van de links-rechtsas.", False),
                 ("open", "Waar gaat de economische links-rechtsas over? Zeg wat links en wat rechts wil.",
                  "Over hoeveel de overheid moet ingrijpen om welvaart te herverdelen. Links wil meer "
                  "herverdeling en een sterke overheid, rechts meer vrije markt en minder belastingen.", 3),
             ]),
        dict(kop="Een verkiezing analyseren",
             opdracht="Bij welk criterium hoort dit?",
             oefeningen=[
                 ("rij", [("een debat tussen de lijsttrekkers op televisie", "informatie"),
                          ("een vakbond die haar leden de standpunten stuurt", "actoren"),
                          ("de regels over campagnegeld", "mechanismen"),
                          ("het gaat om de verkiezing van het Vlaams Parlement", "identificatie")],
                  "Welk criterium?", WW),
                 ("waar", "Een peiling is hetzelfde als de officiële uitslag.", False),
             ]),
        dict(kop="Van uitslag naar regering",
             opdracht="Reken en leg uit.",
             oefeningen=[
                 ("kort", "Hoeveel zetels heb je minstens nodig voor een meerderheid in een parlement van 150 zetels?", "76", W),
                 ("kort", "Partij A gaat van 12 naar 20 zetels. Hoeveel zetels wint ze?", "8", W),
                 ("waar", "De grootste partij komt in België altijd in de regering.", False),
                 ("open", "Leg uit waarom breuklijnen de regeringsvorming in België moeilijk maken.",
                  "Een coalitie moet partijen verzoenen die op de breuklijnen tegenover elkaar staan, "
                  "bijvoorbeeld links en rechts over belastingen. Bovendien moeten er Nederlandstalige en "
                  "Franstalige partijen in de federale regering zitten. Dat vraagt lange onderhandelingen en "
                  "compromissen.", 4),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S3] = dict(reeksen=[
    dict(aanpak="Zoek de twee kampen: kerk en staat, arbeid en kapitaal, of twee taalgroepen.",
         waarom=["Katholieke tegenover officiële scholen is kerk tegenover staat.", None]),
    dict(aanpak="Ken per ideologie één kernwoord: vrijheid, gelijkheid, christelijke waarden, milieu, eigen volk.",
         waarom=[None, None, "Een partij kan economisch rechts en ethisch progressief zijn.",
                 "Noem beide kanten van de as, niet enkel wat ze betekent."]),
    dict(aanpak="Wie speelt mee (actoren), wat hoort de kiezer (informatie), welke regels gelden (mechanismen), welk niveau (identificatie).",
         waarom=["Een debat is informatie, ook al organiseren media het.",
                 "Een peiling is een schatting vooraf bij een steekproef."]),
    dict(aanpak="Een meerderheid is meer dan de helft. Wie samen een meerderheid vindt, regeert.",
         waarom=["De helft van 150 is 75, dus minstens 76.", None,
                 "De grootste partij kan in de oppositie belanden.",
                 "Noem twee redenen: de breuklijnen en de twee taalgroepen in de regering."]),
])

# ═════════════════════════ 4. Participatie, kiesstelsel en kiesrecht
S4 = "humane-wetenschappen-participatie-kiesstelsel-en-kiesrecht-beyond-doorstroom"
BUNDELS[S4] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: participatie, kiesstelsel en kiesrecht",
    onder="Twee kiesstelsels, de evolutie van het kiesrecht in België, vormen van participatie en wat ze beïnvloedt, en het debat over de opkomstplicht.",
    secties=[
        dict(kop="Twee kiesstelsels", blokken=[
            ("p", "In een representatieve democratie geven burgers via verkiezingen een <strong>mandaat</strong> "
                  "aan vertegenwoordigers. Hoe de stemmen in zetels omgezet worden, hangt af van het kiesstelsel."),
            ("p", tabel(["", "Evenredige vertegenwoordiging", "Meerderheidsstelsel"], [
                ["hoe?", "procent stemmen ≈ procent zetels", "per district krijgt enkel de winnaar een zetel"],
                ["voorbeeld", "België", "Verenigd Koninkrijk"],
                ["voordeel", "meer stromingen krijgen een stem", "vaak een regering van één partij"],
                ["nadeel", "bijna altijd coalities, moeilijke regeringsvorming", "stemmen voor verliezers gaan verloren, kleine partijen benadeeld"],
            ])),
            ("kader", "<strong>Rekenvoorbeeld.</strong> Bij evenredige vertegenwoordiging krijgt een partij "
                      "met 10 procent van de stemmen ongeveer 15 van de 150 zetels. Bij een meerderheidsstelsel "
                      "kan een partij met een kwart van de stemmen nul zetels halen als ze nergens de grootste is."),
        ]),
        dict(kop="Het kiesrecht in België", blokken=[
            ("p", tabel(["Jaar", "Wat veranderde"], [
                ["1831", "cijnskiesrecht: enkel mannen die genoeg belasting (cijns) betaalden, mochten stemmen"],
                ["1893", "algemeen meervoudig stemrecht voor mannen vanaf 25 jaar, extra stemmen voor bezit, diploma of gezin; ook de opkomstplicht"],
                ["1919", "algemeen enkelvoudig stemrecht: elke man één stem"],
                ["1948", "vrouwen stemmen ook voor het parlement (voor de gemeenteraad al vanaf 1921)"],
                ["1981", "de stemleeftijd zakt van 21 naar 18 jaar"],
            ])),
            ("p", "Arbeiders betaalden te weinig belasting om te mogen stemmen. Na stakingen en acties kwam er "
                  "in 1893 het algemeen meervoudig stemrecht."),
            ("kader", "<strong>Opkomstplicht, geen stemplicht.</strong> Je moet naar het stembureau gaan, "
                      "maar je mag blanco of ongeldig stemmen. Wat je daar doet, is geheim en vrij."),
        ]),
        dict(kop="Vormen van participatie", blokken=[
            ("p", tabel(["Soort", "Voorbeelden"], [
                ["conventioneel (via de gewone kanalen)", "stemmen, kandidaat zijn, lid worden van een partij, een politicus contacteren"],
                ["niet-conventioneel (buiten de gewone kanalen)", "betogingen, boycots, petities"],
            ])),
            ("p", tabel(["Begrip", "Wat het is"], [
                ["referendum of volksraadpleging", "burgers stemmen over één vraag; in België vooral in gemeenten en niet bindend"],
                ["belangengroep", "een organisatie die de belangen van een groep verdedigt, zoals een vakbond; komt niet op bij verkiezingen"],
                ["sociale beweging", "een losser georganiseerde groep die actie voert, zoals de klimaatbeweging"],
                ["burgerinitiatief", "burgers nemen zelf het initiatief en brengen een voorstel bij de politiek"],
            ])),
            ("p", "Hoeveel iemand participeert, hangt af van <strong>scholingsgraad</strong>, "
                  "<strong>leeftijd</strong>, <strong>gezinssituatie</strong>, <strong>urbanisatie</strong> (stad of "
                  "platteland), het <strong>internet</strong> en de <strong>staatsvorm</strong>: in een dictatuur zijn "
                  "vrije verkiezingen en acties vaak verboden."),
        ]),
        dict(kop="Het debat over de opkomstplicht", blokken=[
            ("p", tabel(["Vóór afschaffen", "Tegen afschaffen"], [
                ["stemmen is een recht, geen plicht", "zonder plicht gaan vooral bepaalde groepen stemmen"],
                ["een stem uit vrije wil is meer waard", "zwakkere groepen worden dan minder gehoord"],
            ])),
        ]),
    ],
    onthoud=[
        "Evenredig: procent stemmen ≈ procent zetels (België). Meerderheid: per district enkel de winnaar (VK).",
        "1831 cijns, 1893 meervoudig + opkomstplicht, 1919 enkelvoudig, 1948 vrouwen, 1981 vanaf 18.",
        "Conventioneel via de gewone kanalen, niet-conventioneel erbuiten.",
        "Belangengroep, sociale beweging, burgerinitiatief, volksraadpleging.",
        "Factoren: scholing, leeftijd, gezin, urbanisatie, internet, staatsvorm.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S4] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: participatie, kiesstelsel en kiesrecht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Kiesstelsels",
             opdracht="Reken en vergelijk.",
             oefeningen=[
                 ("kort", "Bij evenredige vertegenwoordiging haalt een partij 20 procent van de stemmen. Hoeveel van de 150 zetels krijgt ze ongeveer?", "30", W),
                 ("kort", "In een meerderheidsstelsel wint een partij 3 van de 10 districten, met één zetel per district. Hoeveel zetels krijgt ze?", "3", W),
                 ("open", "Geef een voordeel en een nadeel van evenredige vertegenwoordiging.",
                  "Voordeel: meer stromingen krijgen een stem in het parlement. Nadeel: er zijn bijna altijd "
                  "coalities nodig, dus de regeringsvorming is moeilijker.", 3),
             ]),
        dict(kop="Het kiesrecht",
             opdracht="Vul het jaar in.",
             oefeningen=[
                 ("tabel", ["Wat veranderde", "Jaar"],
                  [["cijnskiesrecht", None], ["algemeen meervoudig stemrecht", None],
                   ["elke man één stem", None], ["vrouwen stemmen voor het parlement", None],
                   ["stemmen vanaf 18 jaar", None]],
                  "1831; 1893; 1919; 1948; 1981", W),
                 ("waar", "Bij de opkomstplicht ben je verplicht om op een partij of kandidaat te stemmen.", False),
             ]),
        dict(kop="Vormen van participatie",
             opdracht="Benoem de vorm.",
             oefeningen=[
                 ("rij", [("een petitie tekenen", "niet-conventioneel"), ("lid worden van een partij", "conventioneel"),
                          ("een boycot", "niet-conventioneel"), ("kandidaat zijn", "conventioneel")],
                  "Conventioneel of niet-conventioneel?", WW),
                 ("rij", [("een vakbond overlegt met de minister", "belangengroep"),
                          ("duizenden jongeren betogen voor het klimaat", "sociale beweging"),
                          ("buurtbewoners brengen een plan op de gemeenteraad", "burgerinitiatief")],
                  "Welke vorm?", WW),
                 ("rij", [("een hoogopgeleide stapt sneller naar een politicus", "scholingsgraad"),
                          ("een alleenstaande ouder heeft geen tijd voor vergaderingen", "gezinssituatie"),
                          ("in de stad zijn er meer acties en verenigingen", "urbanisatie")],
                  "Welke factor?", WW),
             ]),
        dict(kop="De opkomstplicht",
             opdracht="Argumenteer.",
             oefeningen=[
                 ("open", "Geef een argument vóór en een argument tegen het afschaffen van de opkomstplicht.",
                  "Vóór: stemmen is een recht en geen plicht, en een stem uit vrije wil is meer waard. "
                  "Tegen: zonder plicht gaan vooral bepaalde groepen stemmen, waardoor zwakkere groepen "
                  "minder gehoord worden.", 4),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S4] = dict(reeksen=[
    dict(aanpak="Evenredig: reken het percentage van het aantal zetels. Meerderheid: tel de gewonnen districten.",
         waarom=["20 procent van 150 is 30.", "Per gewonnen district één zetel; de rest van de stemmen telt niet mee.",
                 "Noem allebei; een voordeel alleen is maar de helft van het antwoord."]),
    dict(aanpak="Onthoud de vijf jaren als een rij: 1831, 1893, 1919, 1948, 1981.",
         waarom=[None, "Je moet enkel opkomen; blanco stemmen mag."]),
    dict(aanpak="Gaat het via de gewone politieke kanalen of erbuiten? En wie neemt het initiatief?",
         waarom=["Een petitie gaat buiten partij en verkiezing om, ook al is ze toegelaten.",
                 "Een vakbond is georganiseerd en verdedigt een groep; een beweging is losser.",
                 None]),
    dict(aanpak="Zet de twee kanten naast elkaar: vrijheid tegenover gelijke vertegenwoordiging.",
         waarom=[None]),
])

# ═════════════════════════ 5. Het recht in de samenleving
S5 = "humane-wetenschappen-het-recht-in-de-samenleving-beyond-doorstroom"
BUNDELS[S5] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: het recht in de samenleving",
    onder="De functies van justitie, de principes van rechtspraak, burgerlijk recht en strafrecht, de gerechtelijke piramide en actuele debatten.",
    secties=[
        dict(kop="Functies en principes", blokken=[
            ("p", tabel(["Functie van justitie", "Voorbeeld"], [
                ["conflictoplossing", "een rechter beslist in een ruzie tussen buren over een haag"],
                ["preventie", "een zware straf voor dronken rijden schrikt anderen af"],
                ["ordehandhaving", "de politie houdt een betoging in goede banen"],
                ["veiligheid", "een gevaarlijke dader wordt opgesloten om anderen te beschermen"],
            ])),
            ("p", tabel(["Principe van rechtspraak", "Wat het betekent"], [
                ["hoor en wederhoor", "elke partij kan haar verhaal doen en op de andere reageren"],
                ["vermoeden van onschuld", "je bent onschuldig tot je schuld bewezen is"],
                ["openbaarheid", "zittingen zijn in principe openbaar; soms met gesloten deuren, bv. om minderjarigen te beschermen"],
                ["onafhankelijkheid en onpartijdigheid", "geen bevelen van de regering, geen persoonlijk belang in de zaak"],
            ])),
            ("kader", "<strong>Een rechter die moet oordelen over zijn eigen schoonbroer</strong> laat zich "
                      "vervangen: hij heeft een persoonlijk belang en is dus niet onpartijdig."),
        ]),
        dict(kop="Burgerlijk recht en strafrecht", blokken=[
            ("p", tabel(["", "Burgerlijk recht", "Strafrecht"], [
                ["waarover?", "conflicten tussen burgers: contracten, huur, schadevergoeding", "misdrijven"],
                ["wie start?", "een burger", "het openbaar ministerie (het parket) vervolgt in naam van de samenleving"],
                ["voorbeeld", "de eigenaar betaalt de huurwaarborg niet terug", "een inbraak en diefstal"],
            ])),
            ("p", "In een strafzaak <strong>vervolgt</strong> het openbaar ministerie, <strong>verdedigt</strong> "
                  "de advocaat zijn cliënt, en <strong>beslist</strong> de rechter."),
            ("kader", "<strong>Eén feit, twee zaken.</strong> Wie iemand in elkaar slaat, kan gestraft worden "
                      "(strafrecht), en het slachtoffer kan daarnaast een schadevergoeding vragen (burgerlijk recht)."),
        ]),
        dict(kop="De gerechtelijke piramide", blokken=[
            ("p", "De <strong>materiële bevoegdheid</strong> zegt welke rechtbank een soort zaak behandelt. De "
                  "<strong>territoriale bevoegdheid</strong> zegt welke rechtbank van die soort, bijvoorbeeld die van "
                  "Gent of van Hasselt."),
            ("p", tabel(["Laag", "Rechtbank", "Behandelt bijvoorbeeld"], [
                ["onderaan", "vredegerecht", "kleinere burgerlijke geschillen, burenhinder, huur"],
                ["onderaan", "politierechtbank", "verkeersovertredingen en schade bij verkeersongevallen"],
                ["eerste aanleg", "burgerlijke rechtbank", "grotere burgerlijke geschillen"],
                ["eerste aanleg", "correctionele rechtbank", "wanbedrijven zoals diefstal, slagen en verwondingen"],
                ["eerste aanleg", "familierechtbank", "echtscheiding, verblijf van de kinderen, erfenissen"],
                ["eerste aanleg", "jeugdrechtbank", "minderjarigen; vooral maatregelen die opvoeden en herstellen"],
                ["eerste aanleg", "strafuitvoeringsrechtbank", "vervroegde vrijlating, enkelband"],
                ["eerste aanleg", "arbeidsrechtbank", "conflicten tussen werknemers en werkgevers, sociale zekerheid"],
                ["eerste aanleg", "ondernemingsrechtbank", "geschillen tussen ondernemingen, faillissementen"],
                ["beroep", "hof van beroep, arbeidshof", "de zaak opnieuw behandelen na een vonnis in eerste aanleg"],
                ["", "hof van assisen", "de zwaarste misdaden, zoals moord, met een volksjury"],
                ["bovenaan", "Hof van Cassatie", "nagaan of de wet juist werd toegepast, zonder de feiten opnieuw te beoordelen"],
            ])),
        ]),
        dict(kop="Actuele debatten", blokken=[
            ("p", tabel(["Begrip", "Waar het debat over gaat"], [
                ["volksjury bij assisen", "burgers krijgen een stem, maar leken kunnen sterker beïnvloed worden; er is debat over afschaffen"],
                ["alternatieve straffen", "werkstraf en enkelband buiten de gevangenis: moeten ze vaker?"],
                ["verjaring", "na een bepaalde tijd kan een misdrijf niet meer vervolgd worden, ook als een procedure lang aansleept"],
                ["uithandengeving", "bij zware feiten kan de jeugdrechter een minderjarige vanaf 16 jaar naar een gewone rechtbank sturen"],
                ["trial by media", "de media stellen iemand al schuldig voor, en het vermoeden van onschuld komt onder druk"],
            ])),
        ]),
    ],
    onthoud=[
        "Functies: conflictoplossing, preventie, ordehandhaving, veiligheid.",
        "Principes: hoor en wederhoor, vermoeden van onschuld, openbaarheid, onafhankelijkheid en onpartijdigheid.",
        "Burgerlijk recht: tussen burgers. Strafrecht: misdrijven, vervolgd door het openbaar ministerie.",
        "Piramide: vredegerecht en politierechtbank, rechtbanken van eerste aanleg, hoven, Hof van Cassatie.",
        "Debatten: volksjury, alternatieve straffen, verjaring, uithandengeving, trial by media.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S5] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: het recht in de samenleving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Functies en principes",
             opdracht="Benoem de functie of het principe.",
             oefeningen=[
                 ("rij", [("een zware straf moet anderen afschrikken", "preventie"),
                          ("de politie houdt een betoging rustig", "ordehandhaving"),
                          ("een rechter beslist in een ruzie over een contract", "conflictoplossing")],
                  "Welke functie?", WW),
                 ("rij", [("een verdachte wordt veroordeeld zonder dat hij iets mocht zeggen", "hoor en wederhoor"),
                          ("een krant noemt iemand al de dader voor het proces", "vermoeden van onschuld"),
                          ("de regering zegt hoe de rechter moet beslissen", "onafhankelijkheid")],
                  "Welk principe komt in gevaar?", WL),
             ]),
        dict(kop="Burgerlijk recht of strafrecht",
             opdracht="Benoem en leg uit.",
             oefeningen=[
                 ("rij", [("de huurwaarborg wordt niet terugbetaald", "burgerlijk"),
                          ("een inbraak met diefstal", "strafrecht"),
                          ("een ruzie over een haag op de grens", "burgerlijk")],
                  "Burgerlijk of strafrecht?", W),
                 ("open", "Leg met een voorbeeld uit hoe één feit zowel een strafzaak als een burgerlijke zaak kan opleveren.",
                  "Wie iemand in elkaar slaat, kan door het openbaar ministerie vervolgd en gestraft worden: "
                  "strafrecht. Het slachtoffer kan daarnaast een schadevergoeding vragen voor de kosten: "
                  "burgerlijk recht.", 4),
             ]),
        dict(kop="De gerechtelijke piramide",
             opdracht="Welke rechtbank is bevoegd?",
             oefeningen=[
                 ("rij", [("te snel rijden", "politierechtbank"), ("burenhinder", "vredegerecht"),
                          ("een echtscheiding", "familierechtbank"), ("een faillissement", "ondernemingsrechtbank")],
                  "Welke rechtbank?", WL),
                 ("rij", [("een onterecht ontslag", "arbeidsrechtbank"), ("een moord", "hof van assisen"),
                          ("een diefstal door een volwassene", "correctionele rechtbank"),
                          ("een diefstal door een vijftienjarige", "jeugdrechtbank")],
                  "Welke rechtbank?", WL),
                 ("open", "Wat is het verschil tussen de materiële en de territoriale bevoegdheid?",
                  "De materiële bevoegdheid zegt welke soort rechtbank een soort zaak behandelt. De "
                  "territoriale bevoegdheid zegt welke rechtbank van die soort, op welke plaats.", 3),
             ]),
        dict(kop="Actuele debatten",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het als de jeugdrechter een minderjarige naar een gewone rechtbank stuurt?", "uithandengeving", WW),
                 ("waar", "Een werkstraf en een enkelband zit je uit in de gevangenis.", False),
                 ("open", "Geef een argument vóór en een argument tegen de volksjury bij het hof van assisen.",
                  "Vóór: burgers krijgen zo een stem in de rechtspraak. Tegen: leken kunnen sterker "
                  "beïnvloed worden door emoties of door de media.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S5] = dict(reeksen=[
    dict(aanpak="Functies zijn wat justitie wil bereiken. Principes zijn de regels voor een eerlijke rechtspraak.",
         waarom=[None, "Een krant die iemand al de dader noemt, is trial by media."]),
    dict(aanpak="Is er een misdrijf? Dan strafrecht. Gaat het om een conflict tussen burgers? Dan burgerlijk recht.",
         waarom=[None, "Noem beide kanten: de straf voor de samenleving en de schadevergoeding voor het slachtoffer."]),
    dict(aanpak="Zoek eerst de soort zaak (verkeer, gezin, werk, onderneming, misdrijf) en dan de leeftijd van de dader.",
         waarom=[None, "Een minderjarige komt in principe voor de jeugdrechtbank, niet voor de correctionele rechtbank.",
                 "Materieel is de soort zaak, territoriaal de plaats."]),
    dict(aanpak="Bij elk debat: zeg wat het begrip is en wat de twee kanten zijn.",
         waarom=[None, "Het zijn alternatieve straffen: je voert ze uit buiten de gevangenis.", None]),
])

# ═════════════════════════ 6. Globalisering, de VN en de Europese Unie
S6 = "humane-wetenschappen-globalisering-de-vn-en-de-europese-unie-beyond-doorstroom"
BUNDELS[S6] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: globalisering, de VN en de Europese Unie",
    onder="Supranationale en internationale organisaties, mondiale thema's, de instellingen van de EU en hoe Europese wetten België raken.",
    secties=[
        dict(kop="Organisaties over de grenzen heen", blokken=[
            ("p", "Een <strong>supranationale</strong> organisatie staat boven de landen (supra = boven). Landen "
                  "staan er een deel van hun macht aan af en beslissen samen over sommige zaken. Ze doen dat omdat "
                  "samenwerken meer slagkracht geeft bij vrede, handel, gezondheid of klimaat."),
            ("p", tabel(["Organisatie", "Opdracht", "Om te onthouden"], [
                ["Verenigde Naties (VN)", "vrede en veiligheid in de wereld bewaren", "opgericht in 1945, na de Tweede Wereldoorlog; de Veiligheidsraad hoort erbij"],
                ["NAVO", "militair bondgenootschap: een aanval op één lid is een aanval op allen", "België is lid sinds 1949; hoofdkwartier in Brussel"],
                ["WHO", "de gezondheid wereldwijd bevorderen", "organisatie van de VN; advies tijdens de coronapandemie"],
                ["G7", "overleg van zeven rijke landen", "VS, Canada, Japan, Duitsland, Frankrijk, Italië, VK; de EU zit mee aan tafel"],
                ["Internationaal Strafhof", "personen berechten voor genocide, misdaden tegen de menselijkheid en oorlogsmisdaden", "in Den Haag"],
                ["Europees Hof van de Rechten van de Mens", "oordelen over staten die mensenrechten schenden", "in Straatsburg; een burger kan er klagen na de eigen rechter"],
            ])),
            ("kader", "<strong>Twee hoven niet verwarren.</strong> Het Internationaal Strafhof berecht "
                      "<strong>personen</strong>, het Europees Hof van de Rechten van de Mens oordeelt over "
                      "<strong>staten</strong>."),
        ]),
        dict(kop="Mondiale thema's", blokken=[
            ("p", "Klimaat, pandemieën, migratie en voedselveiligheid vragen een aanpak over de grenzen heen: "
                  "uitstoot in één land verwarmt de hele aarde, een virus reist mee met reizigers, mensen op de "
                  "vlucht trekken door verschillende landen en voedsel wordt over heel Europa verhandeld."),
            ("kader", "<strong>Mondiaal en lokaal hangen samen.</strong> Ook een gemeente kan iets doen aan een "
                      "mondiaal thema, bijvoorbeeld fietspaden aanleggen of gebouwen isoleren."),
        ]),
        dict(kop="De instellingen van de Europese Unie", blokken=[
            ("p", tabel(["Instelling", "Wie zit erin?", "Wat doet ze?"], [
                ["Europese Commissie", "één commissaris per lidstaat, die het belang van heel de EU dient", "stelt wetten voor (initiatiefrecht) en voert het beleid uit"],
                ["Europees Parlement", "rechtstreeks gekozen door de burgers, om de vijf jaar; grotere landen hebben meer zetels", "keurt samen met de Raad de wetten goed"],
                ["Raad van de Europese Unie", "de vakministers van de lidstaten", "keurt samen met het Parlement de wetten goed"],
                ["Europese Raad", "de staatshoofden en regeringsleiders", "bepaalt de grote lijnen; maakt geen wetten"],
            ])),
            ("p", "De gewone weg van een Europese wet: de <strong>Commissie stelt voor</strong>, het "
                  "<strong>Parlement en de Raad van de EU beslissen samen</strong>. Zo spreken de burgers (Parlement) "
                  "en de lidstaten (Raad) allebei mee. De meeste instellingen zetelen in Brussel; het Parlement "
                  "vergadert in Brussel en Straatsburg."),
            ("weetje", "<strong>Europese Raad en Raad van de EU lijken op elkaar</strong> maar zijn niet "
                       "hetzelfde: regeringsleiders tegenover vakministers."),
        ]),
        dict(kop="Europees recht en België", blokken=[
            ("p", tabel(["", "Verordening", "Richtlijn"], [
                ["wat?", "geldt meteen en op dezelfde manier in alle lidstaten", "legt een doel vast; elk land kiest zelf hoe"],
                ["voorbeeld", "één Europese regel voor heel de EU", "een grens voor fijn stof, waarna Vlaanderen maatregelen neemt"],
            ])),
            ("p", "Europees recht gaat <strong>voor</strong> op nationaal recht. Een Belgische rechter moet een "
                  "Belgische regel die ermee in strijd is, buiten toepassing laten."),
            ("p", "Voor de gezamenlijke militaire verdediging van de meeste Europese landen zorgt vooral de "
                  "<strong>NAVO</strong>, niet de EU."),
        ]),
    ],
    onthoud=[
        "Supranationaal: boven de landen, die een deel van hun macht afstaan.",
        "VN: vrede (1945). NAVO: militaire verdediging. WHO: gezondheid. G7: zeven rijke landen.",
        "Internationaal Strafhof: personen (Den Haag). Europees Hof van de Rechten van de Mens: staten (Straatsburg).",
        "Commissie stelt voor, Parlement en Raad van de EU beslissen samen, Europese Raad geeft de richting.",
        "Verordening geldt meteen, richtlijn moet worden omgezet. Europees recht gaat voor.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S6] = dict(
    vak=VAK, niveau=BEYOND, titel="Humane wetenschappen: globalisering, de VN en de Europese Unie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Internationale organisaties",
             opdracht="Welke organisatie?",
             oefeningen=[
                 ("rij", [("een land vraagt zijn bondgenoten om militaire hulp", "NAVO"),
                          ("een legerleider beschuldigd van genocide", "Internationaal Strafhof"),
                          ("een gevangene klaagt over overvolle cellen na de Belgische rechter", "Europees Hof van de Rechten van de Mens"),
                          ("advies tijdens een pandemie", "WHO")],
                  "Welke organisatie?", WL),
                 ("kort", "Hoe heet een organisatie boven de landen, waaraan landen een deel van hun macht afstaan?", "supranationaal", WW),
                 ("waar", "Het Europees Hof van de Rechten van de Mens en het Internationaal Strafhof zijn hetzelfde.", False),
             ]),
        dict(kop="De instellingen van de EU",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["Instelling", "Wie zit erin?"],
                  [["Europese Commissie", None], ["Europees Parlement", None],
                   ["Raad van de Europese Unie", None], ["Europese Raad", None]],
                  "één commissaris per lidstaat; rechtstreeks gekozen door de burgers; de vakministers; de staatshoofden en regeringsleiders", WL),
                 ("kies", "Welke twee instellingen keuren samen de Europese wetten goed?",
                  ["het Parlement en de Raad van de EU", "de Commissie en de Europese Raad",
                   "de NAVO en de VN", "de Europese Raad en het Parlement"], 0),
                 ("open", "Een nieuwe regel over verpakkingen: beschrijf de weg van voorstel tot wet.",
                  "De Europese Commissie stelt de regel voor. Daarna moeten het Europees Parlement en de "
                  "Raad van de Europese Unie allebei akkoord gaan. Pas dan wordt het een Europese wet.", 3),
             ]),
        dict(kop="Europees recht en België",
             opdracht="Verordening of richtlijn?",
             oefeningen=[
                 ("rij", [("een regel geldt meteen in alle lidstaten", "verordening"),
                          ("Europa legt een doel vast en elk land kiest hoe", "richtlijn"),
                          ("Vlaanderen moet maatregelen nemen tegen fijn stof", "richtlijn")],
                  "Verordening of richtlijn?", WW),
                 ("waar", "Een Belgische rechter moet rekening houden met het Europees recht.", True),
                 ("open", "Geef een voorbeeld van een mondiaal thema en wat een gemeente eraan kan doen.",
                  "Klimaat: uitstoot in één land verwarmt de hele aarde. Een gemeente kan fietspaden "
                  "aanleggen of gebouwen isoleren.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S6] = dict(reeksen=[
    dict(aanpak="Militair: NAVO. Personen berechten: Strafhof. Staten en mensenrechten: Europees Hof. Gezondheid: WHO.",
         waarom=["De gevangene klaagt over België, een staat: dus het Europees Hof.", None,
                 "Het ene oordeelt over staten in Straatsburg, het andere berecht personen in Den Haag."]),
    dict(aanpak="Leer de vier instellingen als twee paren: wie stelt voor en geeft richting, en wie beslist.",
         waarom=[None, "De Europese Raad maakt geen wetten.",
                 "Noem de drie instellingen in de juiste volgorde."]),
    dict(aanpak="Geldt het meteen? Verordening. Moet het land het zelf omzetten? Richtlijn.",
         waarom=[None, "Europees recht gaat voor op nationaal recht.", None]),
])

# -*- coding: utf-8 -*-
"""De leerbundels voor techniek op ✨ Spark-niveau.

Gebaseerd op de vakfiche techniek 1ste graad A-stroom (geldig 2027). Eén bundel
per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema behandelen
dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel dus twee
keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/techniek.json` doet daar
het voorwerk voor.

Elf thema's en geen tien, omdat de fiche drie rubrieken met heel verschillende
gewichten heeft: technische systemen weegt 82,5 %, algoritmen 10 % en
materialen en grondstoffen 7,5 %. De vijf systemen van de fiche (energie,
informatieverwerkend, constructie, transport, biotechnisch) staan er allemaal
apart in, en het technisch proces, het veilig werken en het meten en tekenen
horen er ook bij.

Over de pictogrammen. De officiële gevaarpictogrammen en de pictogrammen van
een gsm staan hier beschréven en niet getekend: nagetekende pictogrammen zijn
nooit precies dezelfde als die op de verpakking, en dan leert een kind het
verkeerde beeld. Wat ze betekenen staat er wel volledig in.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Techniek"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────────────────────── 1. Materialen en grondstoffen
BUNDELS["materialen-en-grondstoffen"] = dict(
    vak=VAK, niveau=SPARK, titel="Materialen en grondstoffen",
    onder="Van grondstof tot product, de soorten materialen, hun eigenschappen en de veiligheidspictogrammen.",
    secties=[
        dict(kop="Grondstof, materiaal, product", blokken=[
            ("p", "IJzererts, klei, zand, wol en aardolie horen allemaal bij dezelfde groep: het zijn "
                  "<strong>grondstoffen</strong>. Een grondstof haal je uit de natuur. Bewerk je haar, dan wordt "
                  "het een <strong>materiaal</strong>, en maak je daar iets van, dan heb je een "
                  "<strong>product</strong>."),
            ("fig", svg.stappen(["grondstof|klei", "materiaal|baksteen", "product|muur"]),
             "Klei komt uit de grond, een baksteen wordt eruit gebakken, en met bakstenen metsel je een muur. "
             "Zand is dus de grondstof en glas het materiaal, en niet omgekeerd."),
            ("kader", "Let op: <strong>staal is geen grondstof</strong>. Staal wordt gemaakt uit ijzererts, en "
                      "dat erts is de grondstof."),
        ]),
        dict(kop="Metaal of niet, ferro of non-ferro", blokken=[
            ("p", "Een <strong>enkelvoudig metaal</strong> bestaat uit één metaal: koper, aluminium, lood. Een "
                  "<strong>legering</strong> is een <strong>mengsel van metalen</strong>, ontstaan door ze samen "
                  "te smelten. <strong>Brons</strong>, <strong>messing</strong>, <strong>inox</strong> en "
                  "<strong>soldeertin</strong> zijn legeringen. Inox is de korte naam voor "
                  "<strong>roestvrij staal</strong>."),
            ("fig", tabel(["wat je wil weten", "welke proef", "wat je ziet"], [
                ["metaal of niet-metaal?", "<strong>de geleidingsproef</strong>: neem de stof op in een stroomkring",
                 "geleidt ze stroom, dan is het een metaal"],
                ["ferro of non-ferro?", "<strong>de magneetproef</strong>: houd er een magneet bij",
                 "trekt de magneet aan, dan is het een ferrometaal"],
            ]), "Twee proeven die twee <em>verschillende</em> vragen beantwoorden. Haal ze niet door elkaar: een "
                "magneet zegt niets over metaal of niet-metaal, en een lampje zegt niets over ferro of non-ferro."),
            ("p", "<strong>Ferrometalen</strong> bevatten ijzer. Ze worden door een magneet aangetrokken en ze "
                  "kunnen roesten. <strong>Non-ferrometalen</strong> bevatten geen ijzer: aluminium, koper en "
                  "lood bijvoorbeeld. Een magneet trekt aluminium dus <strong>niet</strong> aan."),
            ("p", "Naast de metalen staan de <strong>niet-metalen</strong>: hout, steen, glas, kunststof, leder, "
                  "textiel. En je kan materialen ook indelen naar hun herkomst. <strong>Natuurlijk</strong> is "
                  "wat de natuur maakt: hout, leder, wol, steen. <strong>Kunstmatig</strong> is wat de mens "
                  "maakt: kunststof en <strong>composiet</strong>."),
        ]),
        dict(kop="De eigenschappen van een materiaal", blokken=[
            ("p", "De fiche deelt de eigenschappen in <strong>groepen</strong> in. Je moet van een gegeven "
                  "eigenschap kunnen zeggen in welke groep ze thuishoort."),
            ("fig", tabel(["groep", "eigenschappen"], [
                ["<strong>mechanische</strong>", "hardheid, treksterkte, broosheid, taaiheid, elasticiteit"],
                ["<strong>fysische</strong>", "smeltpunt, warmtegeleiding, massadichtheid"],
                ["<strong>elektrische</strong>", "of het materiaal stroom geleidt"],
                ["<strong>magnetische</strong>", "of een magneet het aantrekt"],
                ["<strong>technologische</strong>", "vervormbaarheid, watervastheid, bewerkbaarheid, verwerkingstijd van een lijm"],
            ]), "Het <strong>smeltpunt</strong> is dus een fysische en géén mechanische eigenschap, en de "
                "<strong>verwerkingstijd van een lijm</strong> is technologisch en niet mechanisch."),
            ("fig", tabel(["eigenschap", "hoe je ze onderzoekt"], [
                ["<strong>elasticiteit</strong>", "je rekt het materiaal uit en kijkt of het terugveert"],
                ["<strong>massadichtheid</strong>", "met de <strong>onderdompelingsmethode</strong>"],
                ["<strong>elektrische geleiding</strong>", "je neemt het materiaal op in een <strong>stroomkring</strong>"],
                ["<strong>ferromagnetisme</strong>", "je houdt er een magneet bij"],
            ]), "De massadichtheid zegt hoeveel massa er in een bepaald volume van een stof zit."),
            ("p", "<strong>Broos</strong> betekent dat een materiaal makkelijk breekt; glas is broos. Het "
                  "tegenovergestelde is <strong>taai</strong>: een taai materiaal kan veel verdragen voor het "
                  "breekt."),
            ("kader", "Moet een onderdeel <strong>onbrandbaar</strong> zijn én tegen vocht kunnen, dan kies je "
                      "<strong>kunststof</strong> en geen hout: hout brandt en het neemt vocht op."),
        ]),
        dict(kop="De veiligheidspictogrammen", blokken=[
            ("p", "Op een verpakking met een gevaarlijke stof staan <strong>pictogrammen</strong>: een ruit met "
                  "een rode rand en een zwart teken erin. Elk gevaar heeft er een eigen."),
            ("fig", tabel(["pictogram", "wat het betekent"], [
                ["<strong>ontvlambaar</strong>", "de stof kan vlam vatten"],
                ["<strong>bijtend of corrosief</strong>", "de stof veroorzaakt <strong>brandwonden</strong> aan huid of ogen"],
                ["<strong>giftig</strong>", "de stof is giftig, ook in kleine hoeveelheid"],
                ["<strong>oxiderend</strong>", "de stof kan brand <strong>veroorzaken of erger maken</strong>"],
                ["<strong>gassen onder druk</strong>", "het pictogram met de <strong>gasfles</strong>"],
                ["<strong>gevaarlijk voor het aquatisch milieu</strong>", "schadelijk voor het water, de vissen en de planten erin"],
            ]), "Ze staan hier beschreven en niet getekend: een nagetekend pictogram lijkt nooit precies op dat "
                "van de verpakking, en dan leer je het verkeerde beeld. Kijk ze na op een echte fles."),
        ]),
    ],
    onthoud=[
        "Grondstof komt uit de natuur, materiaal is bewerkt, product is wat je ermee maakt. Klei → baksteen → muur.",
        "Staal is geen grondstof; ijzererts wel.",
        "Een legering is een mengsel van metalen: brons, messing, inox, soldeertin. Inox = roestvrij staal.",
        "De geleidingsproef zegt metaal of niet-metaal; de magneetproef zegt ferro of non-ferro.",
        "Ferro bevat ijzer, wordt aangetrokken en kan roesten. Aluminium, koper en lood zijn non-ferro.",
        "Natuurlijk: hout, leder, wol, steen. Kunstmatig: kunststof en composiet.",
        "Mechanisch: hardheid, treksterkte, broosheid, taaiheid. Fysisch: smeltpunt, warmtegeleiding, massadichtheid.",
        "Technologisch: vervormbaarheid, watervastheid, bewerkbaarheid, verwerkingstijd van een lijm.",
        "Broos breekt makkelijk, taai verdraagt veel. De onderdompelingsmethode meet de massadichtheid.",
        "Pictogrammen: ontvlambaar, bijtend, giftig, oxiderend, gassen onder druk, gevaarlijk voor het water.",
    ],
)

# ───────────────────────────────────────── 2. Energie in een technisch systeem
BUNDELS["energie-in-een-technisch-systeem"] = dict(
    vak=VAK, niveau=SPARK, titel="Energie in een technisch systeem",
    onder="De energievormen, wat een omzetting met energie doet, en het verschil tussen fossiel en hernieuwbaar.",
    secties=[
        dict(kop="De energievormen", blokken=[
            ("fig", tabel(["energievorm", "waar je ze vindt"], [
                ["<strong>bewegingsenergie</strong> of kinetische energie", "een fietser die snel rijdt, een draaiend wiel"],
                ["<strong>potentiële energie</strong>", "een steen boven op een kast, water achter een stuwdam"],
                ["<strong>chemische energie</strong>", "een batterij, steenkool, aardgas, voedsel"],
                ["<strong>stralingsenergie</strong>", "het licht van de zon op een zonnepaneel"],
                ["<strong>warmte</strong>", "een waterkoker, een verwarming"],
                ["<strong>elektrische energie</strong>", "de stroom uit het stopcontact"],
            ]), "Bewegingsenergie en kinetische energie zijn twee namen voor hetzelfde."),
        ]),
        dict(kop="Energieomzettingen", blokken=[
            ("p", "Een technisch systeem <strong>zet energie om</strong> van de ene vorm in de andere. Het kan "
                  "energie nooit <strong>uit het niets maken</strong>: wat eruit komt, moet er eerst in."),
            ("fig", tabel(["systeem", "van", "naar"], [
                ["een <strong>gloeilamp</strong>", "elektrische energie", "licht <em>en</em> warmte"],
                ["een <strong>windmolen</strong>", "bewegingsenergie", "elektrische energie"],
                ["een <strong>zonnepaneel</strong>", "stralingsenergie", "elektrische energie"],
                ["een <strong>waterkrachtcentrale</strong>", "de beweging van water", "elektrische energie"],
                ["een <strong>verbrandingsmotor</strong>", "chemische energie", "beweging <em>en</em> warmte"],
                ["een <strong>elektrische motor</strong>", "elektrische energie", "beweging"],
            ]), "Let op de laatste rij: een elektrische motor zet elektrische energie om in beweging, en niet "
                "omgekeerd. Wat beweging in elektriciteit omzet, is een generator."),
            ("p", "Bij elke omzetting komt er ook energie vrij die je <strong>niet kunt gebruiken</strong>. Dat "
                  "is de <strong>niet-nuttige energie</strong>. Bij een gloeilamp is de "
                  "<strong>warmte</strong> de niet-nuttige energie en het licht de nuttige; bij een leeslamp is "
                  "het licht dus wél de nuttige. Bij een boormachine is de "
                  "<strong>bewegingsenergie van de boor</strong> de nuttige energie, bij een waterkoker de "
                  "warmte. Er komt bij die waterkoker ook wat geluid vrij, en dat is niet-nuttig."),
            ("weetje", "Daarom wordt je gsm warm terwijl hij oplaadt: een deel van de energie wordt "
                       "<strong>warmte</strong> in plaats van lading. Geen enkel toestel zet alles nuttig om."),
        ]),
        dict(kop="Fossiel of hernieuwbaar", blokken=[
            ("p", "<strong>Fossiele brandstoffen</strong> zijn <strong>steenkool</strong>, "
                  "<strong>aardolie</strong> en <strong>aardgas</strong>. Ze zijn miljoenen jaren oud en komen "
                  "uit de grond. Ze ontstaan dus <strong>niet</strong> op een paar jaar tijd, en daarom raken "
                  "ze op."),
            ("p", "<strong>Hernieuwbare energie</strong> betekent dat de <strong>bron niet opraakt</strong>. De "
                  "fiche noemt <strong>de zon</strong>, <strong>de wind</strong>, <strong>het water</strong> en "
                  "<strong>aardwarmte</strong>, de warmte uit de diepe ondergrond. Je noemt ze ook "
                  "<strong>duurzame</strong> energie, omdat de bron ook voor de volgende generaties blijft "
                  "bestaan. Wind raakt dus niet op, hoeveel stroom je er ook mee maakt."),
            ("p", "Verbrand je fossiele brandstoffen, dan komt er <strong>CO2</strong> vrij, en dat is een "
                  "<strong>broeikasgas</strong>. Dat is de reden waarom het verbranden ervan voor "
                  "klimaatverandering zorgt. Bij het opwekken van stroom met een windmolen komt er geen CO2 "
                  "vrij, want er wordt niets verbrand."),
            ("kader", "Het <strong>broeikaseffect</strong> bestond al lang voor de mens fossiele brandstoffen "
                      "begon te gebruiken. Zonder dat effect zou het hier veel te koud zijn. Het probleem is "
                      "dat wij er gassen bij doen."),
            ("p", "Wind en zon hebben één duidelijk nadeel: ze <strong>leveren niet altijd evenveel</strong>. "
                  "Op een windstille avond draait geen molen. Wat je zelf kan doen om minder fossiele brandstof "
                  "te gebruiken: met de fiets gaan in plaats van met de auto, de verwarming een graad lager "
                  "zetten, en het licht uitdoen als je een kamer verlaat."),
        ]),
    ],
    onthoud=[
        "Energievormen: beweging (kinetisch), potentieel, chemisch, straling, warmte, elektrisch.",
        "Een technisch systeem zet energie om; het kan er nooit uit het niets bij maken.",
        "Gloeilamp: elektrisch → licht en warmte. Windmolen: beweging → elektrisch. Zonnepaneel: straling → elektrisch.",
        "Een elektrische motor zet elektriciteit om in beweging; een generator doet het omgekeerde.",
        "Niet-nuttige energie is wat vrijkomt maar je niet kan gebruiken, zoals de warmte van een gloeilamp.",
        "Fossiel: steenkool, aardolie, aardgas. Ze raken op en geven CO2 bij verbranding.",
        "Hernieuwbaar: zon, wind, water en aardwarmte. De bron raakt niet op.",
        "CO2 is een broeikasgas. Het broeikaseffect bestond al voor de mens.",
        "Nadeel van wind en zon: ze leveren niet altijd evenveel.",
    ],
)

# ───────────────────────────────────────── 3. De elektrische stroomkring
BUNDELS["de-elektrische-stroomkring"] = dict(
    vak=VAK, niveau=SPARK, titel="De elektrische stroomkring",
    onder="De componenten en hun symbolen, serie en parallel, de grootheden, en veilig werken met elektriciteit.",
    secties=[
        dict(kop="De componenten en hun symbolen", blokken=[
            ("p", "In een elektrisch <strong>schema</strong> teken je geen afbeelding van het onderdeel maar "
                  "een <strong>symbool</strong>. Iedereen ter wereld gebruikt dezelfde symbolen, dus iedereen "
                  "leest hetzelfde schema."),
            ("fig", svg.schemasymbolen(), "De componenten die de fiche noemt."),
            ("fig", tabel(["component", "wat hij doet"], [
                ["de <strong>spanningsbron</strong>", "levert de spanning; een <strong>batterij</strong> is een <strong>gelijkspanningsbron</strong>, een <strong>generator</strong> levert <strong>wisselspanning</strong>"],
                ["de <strong>geleider</strong> of draad", "verbindt de onderdelen met elkaar"],
                ["de <strong>schakelaar</strong>", "opent of sluit de kring"],
                ["de <strong>weerstand</strong>", "laat de stroom moeilijker doorlopen"],
                ["de <strong>zoemer</strong>", "zet elektrische stroom om in geluid"],
                ["de <strong>LED</strong>", "geeft licht, maar laat de stroom maar in <strong>één</strong> richting door"],
            ]), "Om een lampje te laten branden heb je drie dingen nodig: een spanningsbron, geleidende draden "
                "en het lampje zelf."),
            ("fig", svg.stroomkring(dicht=True), "Een <strong>gesloten</strong> kring: het lampje brandt. Staat de "
                                       "schakelaar <strong>open</strong>, dan is de kring onderbroken, loopt er "
                                       "geen stroom en brandt er niets."),
        ]),
        dict(kop="Serie, parallel en gemengd", blokken=[
            ("fig", svg.serie_parallel(), "In <strong>serie</strong> liggen de verbruikers achter elkaar in één "
                                          "kring. In <strong>parallel</strong> ligt elke verbruiker op zijn "
                                          "eigen tak."),
            ("p", "Draai je in een <strong>serieschakeling</strong> één lampje los, dan gaan ze "
                  "<strong>allemaal</strong> uit: de kring is onderbroken. In een "
                  "<strong>parallelschakeling</strong> blijven de andere branden. Daarom staan de lampjes van "
                  "een <strong>kerstboom</strong> in parallel: gaat er één stuk, dan branden de andere door."),
            ("p", "En daarom staan de twee schakelaars van een <strong>heggenschaar</strong> juist wél in "
                  "<strong>serie</strong>: pas als je ze allebei indrukt is de kring gesloten, en dus werkt de "
                  "schaar alleen met twee handen. Je handen kunnen dan niet bij het mes."),
            ("p", "Een schakeling die serie en parallel combineert, heet een <strong>gemengde</strong> "
                  "schakeling. Volgens de fiche kan je <strong>verbruikers</strong>, "
                  "<strong>schakelaars</strong> én <strong>spanningsbronnen</strong> in serie of in parallel "
                  "schakelen."),
        ]),
        dict(kop="De grootheden en het meten", blokken=[
            ("fig", tabel(["grootheid", "symbool", "eenheid"], [
                ["<strong>spanning</strong>", "U", "de <strong>volt</strong> (V)"],
                ["<strong>stroomsterkte</strong>", "I", "de <strong>ampère</strong> (A)"],
                ["<strong>weerstand</strong>", "R", "de <strong>ohm</strong> (Ω)"],
                ["<strong>vermogen</strong>", "P", "de <strong>watt</strong> (W)"],
            ]), "De weerstand wordt dus in ohm uitgedrukt en niet in ampère."),
            ("p", "Met een <strong>multimeter</strong> meet je die grootheden. Zet je hem in de stand "
                  "<strong>ampèremeter</strong>, dan meet je de <strong>stroomsterkte</strong>. Gebruik je hem "
                  "om de spanning te meten, dan noem je hem een <strong>voltmeter</strong>."),
            ("p", "Wil je met een lampje testen of een materiaal stroom geleidt, dan zet je het "
                  "<strong>materiaal in de kring</strong> en kijk je of het lampje brandt. Goede geleiders zijn "
                  "<strong>koper</strong>, <strong>aluminium</strong> en <strong>staal</strong>."),
        ]),
        dict(kop="Gevaren en veiligheid", blokken=[
            ("fig", tabel(["gevaar", "wat er gebeurt"], [
                ["<strong>kortsluiting</strong>", "de stroom vindt een te korte weg; het kan <strong>brand</strong> veroorzaken"],
                ["<strong>overbelasting</strong>", "er loopt <strong>meer stroom door een draad dan hij aankan</strong>"],
                ["<strong>elektrocutie</strong>", "je krijgt een <strong>stroomstoot door je lichaam</strong>"],
            ]), "Het pictogram met de <strong>bliksemschicht</strong> waarschuwt voor gevaar voor elektrische "
                "spanning."),
            ("fig", tabel(["veiligheidsvoorziening", "wat ze doet"], [
                ["de <strong>aarding</strong>", "de aardingsdraad leidt stroom veilig naar de grond weg"],
                ["de <strong>automatische zekering</strong>", "ze onderbreekt de kring bij te veel stroom"],
                ["de <strong>verliesstroomschakelaar</strong>", "ze schakelt uit zodra er stroom weglekt, bijvoorbeeld door een mens"],
                ["<strong>dubbele isolatie</strong>", "een tweede laag isolatie rond een toestel — geen gereedschap dus, maar een bouwwijze"],
            ]), "De drie voorzieningen die de fiche opsomt zijn de aarding, de automatische zekering en de "
                "verliesstroomschakelaar."),
            ("fig", tabel(["gereedschap", "waarvoor"], [
                ["de <strong>striptang</strong>", "het kunststof laagje van een draad halen"],
                ["de <strong>soldeerbout</strong>", "twee draden met <strong>tin</strong> verbinden"],
                ["het <strong>kroonsteentje</strong>", "twee draden met schroefjes op elkaar klemmen — het knipt niets door"],
                ["de <strong>zijsnijtang</strong>", "een draad doorknippen"],
            ]), ""),
        ]),
    ],
    onthoud=[
        "In een schema teken je symbolen, nooit een afbeelding van het onderdeel.",
        "Een batterij is een gelijkspanningsbron, een generator levert wisselspanning.",
        "Een LED laat de stroom maar in één richting door; een weerstand remt hem.",
        "In serie: één lampje stuk = allemaal uit. In parallel: de andere branden door.",
        "Kerstboom parallel; de twee schakelaars van een heggenschaar in serie, dus twee handen nodig.",
        "Spanning in volt (U), stroomsterkte in ampère (I), weerstand in ohm (R), vermogen in watt (P).",
        "Een multimeter meet; als ampèremeter meet hij stroomsterkte, als voltmeter de spanning.",
        "Gevaren: kortsluiting (brand), overbelasting (te veel stroom voor de draad), elektrocutie.",
        "Veiligheid: aarding, automatische zekering, verliesstroomschakelaar. Dubbele isolatie is een bouwwijze.",
        "Striptang strippen, soldeerbout verbinden met tin, kroonsteentje klemmen, zijsnijtang knippen.",
    ],
)

# ───────────────────────────────────────── 4. Informatieverwerkende systemen
BUNDELS["informatieverwerkende-systemen"] = dict(
    vak=VAK, niveau=SPARK, titel="Informatieverwerkende systemen",
    onder="Sensoren en actuatoren, het IPO-model, de pictogrammen op een toestel, en de logische poorten.",
    secties=[
        dict(kop="Sensoren en actuatoren", blokken=[
            ("p", "Een <strong>sensor</strong> <strong>meet</strong> iets in de omgeving en zet die verandering "
                  "om in een signaal voor het systeem. Een <strong>actuator</strong> <strong>voert iets "
                  "uit</strong>: bewegen, licht geven, geluid maken."),
            ("fig", tabel(["sensoren", "actuatoren"], [
                ["een lichtsensor", "een lamp"],
                ["een bewegingssensor", "een luidspreker"],
                ["een microfoon", "een zoemer"],
                ["een temperatuursensor", "een motor"],
            ]), "Een <strong>microfoon</strong> is dus een sensor en geen actuator: hij meet geluid. Een "
                "<strong>luidspreker</strong> maakt geluid en is wél een actuator."),
            ("p", "Gaat een <strong>straatlamp</strong> vanzelf aan zodra het donker wordt, dan zit er een "
                  "<strong>lichtsensor</strong> in. Gaat de deur van een winkel open zodra je ervoor komt "
                  "staan, dan is dat een <strong>bewegingssensor</strong>. Die plaats je het best "
                  "<strong>boven de deur, gericht naar wie eraan komt</strong>: dan ziet hij je aankomen en "
                  "staat de deur al open als je er bent."),
        ]),
        dict(kop="Het IPO-model", blokken=[
            ("fig", svg.ipo(), "<strong>I</strong>nput, <strong>P</strong>rocess, <strong>O</strong>utput — in "
                               "het Nederlands invoer, verwerking en uitvoer."),
            ("p", "Een <strong>druktoets</strong> hoort bij de <strong>invoer</strong>, een "
                  "<strong>processor</strong> bij de <strong>verwerking</strong>, en een "
                  "<strong>alarm dat afgaat</strong> bij de <strong>uitvoer</strong>. Sensoren staan dus altijd "
                  "vooraan, actuatoren achteraan."),
        ]),
        dict(kop="Pictogrammen op een toestel", blokken=[
            ("fig", tabel(["pictogram", "wat het betekent"], [
                ["de <strong>batterijstatus</strong>", "hoeveel stroom er nog in het toestel zit"],
                ["<strong>wifi</strong>, <strong>bluetooth</strong>, <strong>USB</strong>", "manieren om <strong>verbinding</strong> te maken"],
                ["de <strong>wolk</strong>", "je bestanden staan in de cloud, op een server, en niet alleen op je toestel"],
                ["de <strong>leeftijdspictogrammen</strong>", "vanaf welke leeftijd de inhoud geschikt is"],
                ["<strong>geweld, angst, grof taalgebruik</strong>", "ze zeggen <strong>welke inhoud</strong> er in een spel of een film zit"],
            ]), "Het wolkje betekent dus <em>niet</em> dat het toestel bijna leeg is; daarvoor is er het "
                "batterijteken."),
            ("p", "<strong>www</strong> staat voor <strong>world wide web</strong>."),
        ]),
        dict(kop="Binair en de logische poorten", blokken=[
            ("p", "Een computer werkt met de <strong>binaire code</strong>: er bestaan maar "
                  "<strong>twee</strong> waarden. Een <strong>1</strong> betekent <strong>aan</strong>, een "
                  "<strong>0</strong> betekent <strong>uit</strong>."),
            ("fig", svg.poorten(), "De drie poorten die de fiche noemt, elk met haar "
                                   "<strong>waarheidstabel</strong>: een tabel met alle mogelijke ingangen en "
                                   "de uitgang erbij. Een poort met twee ingangen heeft er "
                                   "<strong>vier</strong> rijen. Een logische poort heeft altijd precies "
                                   "<strong>één</strong> uitgang."),
            ("p", "In het Engels heet de EN-poort een <strong>AND</strong>-poort, de OF-poort een OR-poort en "
                  "de NIET-poort een NOT-poort."),
            ("fig", tabel(["wat je wil", "welke poort"], [
                ["een alarm dat afgaat als het donker is <strong>én</strong> er beweging is", "een <strong>EN</strong>-poort"],
                ["een bel die rinkelt als er op de voordeur <strong>óf</strong> op de achterdeur gedrukt wordt", "een <strong>OF</strong>-poort"],
                ["een lamp die brandt als het <strong>niet</strong> licht is", "een <strong>NIET</strong>-poort achter de lichtsensor"],
            ]), "Met een waarheidstabel kan je drie dingen: de uitgang bepalen bij gegeven ingangen, zien welke "
                "poort er gebruikt is, en alle mogelijke gevallen op een rij zetten."),
            ("kader", "De drie valkuilen. Een <strong>EN</strong>-poort met 1 en 0 geeft <strong>0</strong>, "
                      "want niet alle ingangen zijn 1. Een <strong>OF</strong>-poort met 1 en 0 geeft "
                      "<strong>1</strong>, want één ingang volstaat. En een OF-poort met twee nullen geeft "
                      "<strong>0</strong>."),
        ]),
    ],
    onthoud=[
        "Een sensor meet, een actuator doet. Een microfoon is een sensor, een luidspreker een actuator.",
        "IPO = input (invoer), process (verwerking), output (uitvoer). Druktoets in, processor verwerkt, alarm uit.",
        "Lichtsensor in een straatlamp, bewegingssensor bij een automatische deur.",
        "Binair: alleen 0 en 1. 1 is aan, 0 is uit.",
        "EN-poort: alleen 1 als álle ingangen 1 zijn. In het Engels AND.",
        "OF-poort: al 1 zodra één ingang 1 is. NIET-poort: draait het signaal om.",
        "Een waarheidstabel zet alle mogelijke ingangen met hun uitgang op een rij; twee ingangen = vier rijen.",
        "Een logische poort heeft altijd precies één uitgang.",
        "Wifi, bluetooth en USB gaan over verbinding; de batterijstatus over de lading; het wolkje over de cloud.",
    ],
)

# ───────────────────────────────────────── 5. Krachten en stevigheid in een constructie
BUNDELS["krachten-en-stevigheid-in-een-constructie"] = dict(
    vak=VAK, niveau=SPARK, titel="Krachten en stevigheid in een constructie",
    onder="De vier krachten, de materiaalkeuze die erbij hoort, en wat een constructie stabiel, sterk en stijf maakt.",
    secties=[
        dict(kop="De vier krachten", blokken=[
            ("fig", svg.krachtsoorten(), "De vier krachten die de fiche noemt. Van elke constructie moet je "
                                         "kunnen zeggen welke kracht er werkt."),
            ("fig", tabel(["situatie", "welke kracht"], [
                ["de ophangkabels van een brug", "<strong>trekkracht</strong>"],
                ["de pilaren van een brug", "<strong>drukkracht</strong>"],
                ["boeken op een tafelblad", "<strong>drukkracht</strong>"],
                ["een touw waaraan je trekt", "<strong>trekkracht</strong>"],
                ["een schroef vastdraaien met een schroevendraaier", "<strong>torsiekracht</strong>"],
                ["een plank op twee steunen met iets zwaars in het midden", "<strong>buigkracht</strong>"],
                ["een kraanarm die een last optilt", "<strong>buigkracht</strong>"],
                ["de twee kettingen van een schommel", "<strong>trekkracht</strong>"],
            ]), "Torsie is <strong>verdraaien</strong>, niet samendrukken. Samendrukken is druk."),
            ("p", "Krijgt een materiaal <strong>meer trekkracht dan het aankan</strong>, dan "
                  "<strong>scheurt of breekt</strong> het."),
        ]),
        dict(kop="Het juiste materiaal kiezen", blokken=[
            ("p", "<strong>Beton</strong> kan veel <strong>drukkracht</strong> verdragen maar weinig "
                  "<strong>trekkracht</strong>. Dat is meteen de reden waarom er staal in gewapend beton zit."),
            ("fig", tabel(["waarvoor", "welk materiaal"], [
                ["een kabel die veel trekkracht moet verdragen", "<strong>staal</strong>"],
                ["een zuil die veel gewicht moet dragen", "<strong>beton</strong>, <strong>staal</strong> of <strong>steen</strong>"],
                ["een onderdeel dat veel trekkracht moet opvangen", "géén <strong>glas</strong>: glas is broos"],
            ]), "Waar je op let bij het kiezen: de trekkracht die het materiaal moet opvangen, de drukkracht die "
                "het moet opvangen, en hoe zwaar het materiaal zélf is."),
            ("p", "Dat laatste verklaart waarom een <strong>fietsframe</strong> uit "
                  "<strong>buizen</strong> gemaakt is en niet uit massieve staven: buizen zijn "
                  "<strong>licht en toch sterk genoeg</strong>. Het materiaal in het midden van een staaf draagt "
                  "toch bijna niets mee."),
        ]),
        dict(kop="Stabiliteit, sterkte en stijfheid", blokken=[
            ("fig", tabel(["woord", "wat het betekent"], [
                ["<strong>stabiliteit</strong>", "de constructie blijft staan en valt niet om"],
                ["<strong>sterkte</strong>", "ze kan veel kracht verdragen zonder te breken"],
                ["<strong>stijfheid</strong>", "ze vervormt bijna niet onder belasting"],
            ]), "Drie verschillende dingen. Een constructie kan <strong>sterk</strong> zijn en toch "
                "<strong>omvallen</strong>, en stijfheid en sterkte betekenen dus niet hetzelfde."),
            ("p", "Stabieler maak je een constructie met een <strong>brede voet</strong>, een <strong>laag "
                  "zwaartepunt</strong> en <strong>schuine balken tussen de hoeken</strong>. Een "
                  "<strong>hoog</strong> zwaartepunt maakt haar juist minder stabiel. Daarom hebben hoge "
                  "gebouwen een brede en zware voet."),
        ]),
        dict(kop="Vormen die stevig maken", blokken=[
            ("p", "De <strong>driehoek</strong> is de vorm die in een constructie het best zijn vorm houdt. Als "
                  "de verbindingen vastzitten, <strong>vervormt hij niet</strong>. Je vindt hem in de "
                  "<strong>gebinten van een dak</strong> en in de <strong>armen van een kraan</strong>."),
            ("p", "Een <strong>rechthoek</strong> van vier losse balken kan juist makkelijk "
                  "<strong>scheeftrekken</strong>. Daarom zetten bouwers er <strong>schuine balken</strong> in: "
                  "zo ontstaan er driehoeken en vervormt het frame niet. Wiebelt een boekenrek heen en weer, dan "
                  "helpt een <strong>schuine lat achteraan tussen twee hoeken</strong> het best."),
            ("p", "De <strong>boog</strong> <strong>leidt het gewicht naar de zijkanten weg</strong>. Ze zit in "
                  "oude bruggen en in poorten, en ze kan een grote opening overspannen."),
            ("p", "<strong>Gewapend beton</strong> is beton met <strong>staven staal</strong> erin. Het staal "
                  "vangt de <strong>trekkracht</strong> op die beton niet aankan, dus gewapend beton verdraagt "
                  "meer trekkracht dan gewoon beton."),
            ("weetje", "Een <strong>golfplaat</strong> is steviger dan een vlakke plaat van dezelfde dikte, "
                       "omdat de <strong>plooien de plaat stijver maken</strong>. Vouw een blad papier tot een "
                       "harmonica en leg het over twee boeken: het draagt ineens wel iets."),
            ("p", "Een <strong>zuil</strong> vangt vooral een <strong>drukkracht</strong> op, en geen "
                  "trekkracht: het gewicht duwt er van boven op."),
        ]),
    ],
    onthoud=[
        "Vier krachten: druk (samenduwen), trek (uit elkaar trekken), torsie (verdraaien), buiging (doorbuigen).",
        "Ophangkabels: trek. Pilaren en zuilen: druk. Schroevendraaier: torsie. Kraanarm en plank: buiging.",
        "Beton verdraagt veel druk maar weinig trek. Staal is goed voor trek. Glas is broos.",
        "Een fietsframe is van buizen: licht en toch sterk genoeg.",
        "Stabiliteit = niet omvallen, sterkte = niet breken, stijfheid = niet vervormen. Drie verschillende dingen.",
        "Stabieler: brede voet, laag zwaartepunt, schuine balken. Een hoog zwaartepunt maakt onstabiel.",
        "De driehoek vervormt niet; de rechthoek trekt scheef tot je er een schuine balk in zet.",
        "De boog leidt het gewicht naar de zijkanten weg en overspant een grote opening.",
        "Gewapend beton = beton met staal erin; het staal vangt de trekkracht op.",
        "Een golfplaat is stijver dan een vlakke plaat: de plooien doen het werk.",
    ],
)

# ───────────────────────────────────────── 6. Verbinden, afwerken en veilig werken
BUNDELS["verbinden-afwerken-en-veilig-werken"] = dict(
    vak=VAK, niveau=SPARK, titel="Verbinden, afwerken en veilig werken",
    onder="Losse en vaste verbindingen, de afwerkingstechnieken, het gereedschap en de regels die je in de werkplaats volgt.",
    secties=[
        dict(kop="Verbindingen die los kunnen en verbindingen die dat niet kunnen", blokken=[
            ("fig", tabel(["verbinding", "wat het is", "los te maken?"], [
                ["een <strong>boutverbinding</strong>", "een <strong>bout</strong> door de stukken, met een <strong>moer</strong> erop", "ja, zonder iets kapot te maken"],
                ["<strong>schroef</strong>", "twee planken aan elkaar zonder lijm", "ja, je draait ze er weer uit"],
                ["<strong>klittenband</strong> of velcro", "twee haakjesbanden die aan elkaar blijven", "ja, telkens opnieuw"],
                ["een <strong>ritssluiting</strong>", "twee tandenrijen die in elkaar haken; ook dat is een verbinding", "ja, telkens opnieuw"],
                ["<strong>magneet</strong>", "twee delen die elkaar aantrekken", "ja"],
                ["een <strong>lasverbinding</strong>", "twee metalen delen samengesmolten", "nee"],
                ["een <strong>lijmverbinding</strong>", "twee delen aan elkaar geplakt", "nee, niet zonder schade"],
                ["een <strong>soldeerverbinding</strong>", "twee draden verbonden met gesmolten <strong>tin</strong>", "nee"],
            ]), "Een <strong>nagel</strong> gebruik je als het voorgoed vast mag; een "
                "<strong>schroef</strong> als je het later nog uit elkaar wil halen."),
            ("p", "Bij hout kent de fiche nog twee eigen verbindingen. Een "
                  "<strong>verstekverbinding</strong>: twee stukken die <strong>schuin afgezaagd</strong> tegen "
                  "elkaar komen, zoals in de hoek van een kader. En een <strong>deuvelverbinding</strong>: twee "
                  "stukken hout die met <strong>houten pinnetjes</strong> vastzitten."),
            ("p", "Een <strong>scharnier</strong> dient om een deel te laten <strong>draaien</strong>, en een "
                  "<strong>profiel</strong> verbindt delen en maakt het geheel <strong>stijver</strong>. Een "
                  "schroef, een bout, een nagel en een deuvel heten samen <strong>verbindingsproducten</strong>: "
                  "het aparte stukje dat de verbinding maakt."),
            ("kader", "Welke <strong>lijm</strong> je kiest, hangt af van drie dingen: welke materialen je aan "
                      "elkaar lijmt, of de verbinding <strong>nat</strong> kan worden, en hoeveel tijd je nog "
                      "hebt om te schikken. Dat laatste is de <strong>verwerkingstijd</strong>: hoe lang je de "
                      "stukken nog kunt verschuiven voor de lijm pakt."),
        ]),
        dict(kop="Afwerken", blokken=[
            ("p", "<strong>Schuren</strong> maakt hout <strong>glad</strong> voor je het schildert. Daarna komt "
                  "de afwerking: <strong>lakken</strong>, <strong>vernissen</strong>, <strong>oliën</strong>, "
                  "schilderen of <strong>beitsen</strong>."),
            ("p", "Hout wordt gevernist of gelakt <strong>om het te beschermen tegen vocht en slijtage</strong>. "
                  "<strong>Beitsen</strong> doet iets anders: het <strong>kleurt het hout</strong> en trekt erin, "
                  "zodat je de <strong>nerf nog ziet</strong>. Het legt dus géén dekkende laag over het hout — "
                  "dat doet verf."),
        ]),
        dict(kop="Gereedschap en machines", blokken=[
            ("p", "<strong>Handgereedschap</strong> bedien je met je eigen kracht: een hamer, een "
                  "schroevendraaier, een verfborstel. Een <strong>machine</strong> werkt met een "
                  "<strong>motor of een aandrijving</strong>. Een gat in hout maak je met een "
                  "<strong>boormachine</strong>."),
            ("p", "Gereedschap moet <strong>onderhouden</strong> worden, want dan blijft het "
                  "<strong>veilig en nauwkeurig</strong> werken. Een botte zaag glijdt weg, een losse steel "
                  "vliegt eraf."),
        ]),
        dict(kop="Persoonlijke beschermingsmiddelen", blokken=[
            ("p", "<strong>PBM</strong> staat voor <strong>persoonlijke beschermingsmiddelen</strong>: "
                  "gehoorbescherming, veiligheidsschoenen, een mondmasker, een veiligheidsbril, handschoenen."),
            ("fig", tabel(["pictogram", "wat het verplicht", "wanneer"], [
                ["een <strong>oorbeschermer</strong>", "gehoorbescherming verplicht", "in een lawaaierige werkplaats"],
                ["een <strong>bril</strong>", "veiligheidsbril verplicht", "bij het boren in steen, bij het zagen"],
                ["een <strong>schoen</strong>", "veiligheidsschoenen verplicht", "waar iets zwaars kan vallen"],
                ["een <strong>masker</strong>", "mondmasker verplicht", "bij stof of damp"],
            ]), "Een blauw rond pictogram betekent altijd: dit is <strong>verplicht</strong>."),
        ]),
        dict(kop="Veilig werken", blokken=[
            ("p", "Op een <strong>veiligheidsinstructiekaart</strong> staan de <strong>risico's van een "
                  "machine en hoe je ze voorkomt</strong>. Voor je een machine voor het eerst gebruikt, lees je "
                  "de <strong>handleiding</strong>."),
            ("fig", tabel(["op de veiligheidsinstructiekaart van een figuurzaag", ""], [
                ["draag <strong>oogbescherming</strong>", "er springen spaanders weg"],
                ["gebruik de <strong>stofafzuiging</strong>", "het zaagstof is schadelijk om in te ademen"],
                ["draag aangepaste <strong>gehoorbescherming</strong>", "de machine maakt aanhoudend lawaai"],
            ]), "Drie maatregelen die op die kaart staan."),
            ("fig", tabel(["wat je doet", "waarom"], [
                ["gemorste producten <strong>meteen</strong> opkuisen", "anders glijdt er iemand uit"],
                ["de <strong>stekker uittrekken</strong> voor je iets aan de machine doet", "ze kan niet meer aanslaan terwijl je eraan zit"],
                ["<strong>lang haar samenbinden</strong>", "het kan <strong>meegetrokken</strong> worden door draaiende delen"],
                ["<strong>geen ringen of juwelen</strong> aan een zaagmachine", "ze kunnen blijven haken"],
                ["<strong>nooit</strong> met natte handen aan een elektrisch toestel", "water geleidt; het duurt geen seconde"],
                ["een meetinstrument <strong>uitschakelen</strong> als je klaar bent", "de batterij loopt anders leeg"],
                ["het <strong>meetbereik</strong> nooit overschrijden", "ook niet even: je maakt het instrument stuk"],
            ]), "Het eerste wat je doet voor je aan een machine gaat sleutelen, is de "
                "<strong>stekker uittrekken</strong>."),
        ]),
    ],
    onthoud=[
        "Los te maken: bout en moer, schroef, klittenband, rits, magneet. Niet los: lassen, lijmen, solderen.",
        "Verstek = schuin afgezaagd tegen elkaar. Deuvel = met houten pinnetjes.",
        "Een scharnier laat draaien; een profiel verbindt en maakt stijver.",
        "Lijm kiezen: welke materialen, of het nat kan worden, en de verwerkingstijd.",
        "Schuren maakt glad. Lakken, vernissen en oliën beschermen tegen vocht en slijtage.",
        "Beitsen kleurt het hout en laat de nerf zien; het legt geen dekkende laag.",
        "Handgereedschap werkt op je eigen kracht, een machine op een motor of aandrijving.",
        "PBM = persoonlijke beschermingsmiddelen: bril, gehoorbescherming, schoenen, mondmasker.",
        "Op een veiligheidsinstructiekaart staan de risico's van een machine en hoe je ze voorkomt.",
        "Eerst de stekker uit. Lang haar samenbinden, geen juwelen, nooit natte handen.",
    ],
)

# ───────────────────────────────────────── 7. Meten, eenheden en modelvoorstellingen
BUNDELS["meten-eenheden-en-modelvoorstellingen"] = dict(
    vak=VAK, niveau=SPARK, titel="Meten, eenheden en modelvoorstellingen",
    onder="De meetinstrumenten, de grootheden en hun eenheden, de formules, en de tekeningen die een technicus maakt.",
    secties=[
        dict(kop="Meetinstrumenten", blokken=[
            ("fig", tabel(["wat je meet", "waarmee"], [
                ["een hoeveelheid vloeistof", "een <strong>maatbeker</strong>"],
                ["de dikte van een plaatje, nauwkeurig", "een <strong>schuifmaat</strong>"],
                ["de massa", "een <strong>weegschaal</strong>"],
                ["de temperatuur", "een <strong>thermometer</strong>"],
                ["spanning, stroom en weerstand", "een <strong>multimeter</strong>"],
                ["een lengte", "een <strong>meetlat</strong> of een <strong>rolmeter</strong>"],
            ]), "Een <strong>stappenplan</strong> is geen meetinstrument: het zegt in welke volgorde je werkt."),
        ]),
        dict(kop="Grootheden, symbolen en eenheden", blokken=[
            ("fig", tabel(["grootheid", "symbool", "SI-eenheid"], [
                ["lengte", "l", "de <strong>meter</strong> (m)"],
                ["massa", "<strong>m</strong>", "de <strong>kilogram</strong> (kg)"],
                ["oppervlakte", "<strong>A</strong>", "de vierkante meter (m²)"],
                ["omtrek", "<strong>P</strong>", "de meter (m)"],
                ["volume", "<strong>V</strong>", "de kubieke meter (m³)"],
                ["kracht", "F", "de <strong>newton</strong> (N)"],
                ["tijd", "t", "de seconde (s)"],
            ]), "Dit is bijlage 1 van de vakfiche. Het symbool van de massa is m, en dat van de oppervlakte A."),
            ("fig", tabel(["voorvoegsel", "betekent", "voorbeeld"], [
                ["<strong>kilo</strong>", "duizend keer groter", "1 kilometer = <strong>1000</strong> meter"],
                ["<strong>hecto</strong>", "<strong>honderd</strong> keer groter", "1 hectometer = 100 meter"],
                ["<strong>deca</strong>", "tien keer groter", "1 decameter = 10 meter"],
                ["<strong>deci</strong>", "tien keer <strong>kleiner</strong>", "1 decimeter = 0,1 meter"],
                ["<strong>centi</strong>", "honderd keer <strong>kleiner</strong>", "1 centimeter = <strong>10</strong> millimeter"],
                ["<strong>milli</strong>", "duizend keer <strong>kleiner</strong>", "1 millimeter = 0,001 meter"],
            ]), "Hecto betekent dus <strong>honderd</strong> en niet duizend. Kleiner maken doen deci, centi en "
                "milli."),
            ("weetje", "Eén <strong>kubieke decimeter</strong> is precies <strong>1 liter</strong>. Een kubus "
                       "van 10 op 10 op 10 centimeter houdt dus een literfles vol water."),
        ]),
        dict(kop="Formules", blokken=[
            ("fig", tabel(["wat je berekent", "formule"], [
                ["de <strong>oppervlakte van een rechthoek</strong>", "<strong>b · h</strong>"],
                ["de <strong>omtrek van een vierkant</strong>", "<strong>4 · z</strong>"],
                ["de oppervlakte van een vierkant", "z · z"],
                ["de omtrek van een cirkel", "2 · π · r"],
                ["het <strong>volume van een balk</strong>", "<strong>lengte · breedte · hoogte</strong>"],
                ["het volume van een bol", "4/3 · π · r³"],
            ]), "Dit is bijlage 2 van de vakfiche: de formules die je op het examen mag gebruiken. Je hoeft ze "
                "dus niet uit het hoofd te kennen, wel te kunnen kiezen."),
        ]),
        dict(kop="De functiedriehoek", blokken=[
            ("p", "Een <strong>functiedriehoek</strong> is een schema met vier dingen erin: de "
                  "<strong>functie</strong> (waarvoor dient het?), het <strong>materiaal</strong> (waarvan is "
                  "het gemaakt?), de <strong>bewerking</strong> (hoe is het gemaakt?) en de "
                  "<strong>vorm</strong> (hoe ziet het eruit?)."),
            ("kader", "Een functiedriehoek is dus <strong>geen</strong> tekening van een voorwerp in drie "
                      "aanzichten. Het is een schema waarmee je een voorwerp <em>beschrijft</em>."),
        ]),
        dict(kop="Tekeningen", blokken=[
            ("fig", tabel(["soort tekening", "wat het is"], [
                ["een <strong>conceptschets</strong>", "een eerste <strong>ruwe</strong> tekening van een idee — nog niet het definitieve ontwerp"],
                ["een <strong>detailontwerp</strong>", "een tekening van <strong>één onderdeel</strong>, groter getekend"],
                ["een <strong>werktekening</strong> of technische tekening", "de tekening waarmee gewerkt wordt; twee namen voor hetzelfde"],
                ["een <strong>ontvouwing</strong>", "het <strong>platte patroon</strong> dat je dichtvouwt tot het voorwerp"],
                ["een <strong>isometrisch perspectief</strong>", "een tekening waarin je het voorwerp <strong>ruimtelijk</strong> ziet"],
            ]), "Een technicus maakt eerst een schets, om te zien of het idee klopt voor er materiaal verloren "
                "gaat."),
            ("fig", svg.aanzichten(), "Hier staan er drie getekend. De vakfiche noemt er "
                                      "<strong>vier</strong>: het <strong>vooraanzicht</strong>, het "
                                      "<strong>bovenaanzicht</strong>, het <strong>zijaanzicht</strong> en het "
                                      "<strong>onderaanzicht</strong>. Dat laatste is wat je zou zien als je er "
                                      "van onderen naar kijkt."),
            ("p", "Op een <strong>werktekening</strong> vind je de <strong>maten van elk deel</strong>, de "
                  "<strong>aanzichten</strong> van het voorwerp en de <strong>schaal</strong> waarop getekend "
                  "is. Die maten staan meestal in <strong>millimeter</strong>. Toont een tekening het voorwerp "
                  "van voren, van boven en van opzij, dan is dat een werktekening met drie aanzichten."),
            ("fig", tabel(["schaal", "wat ze betekent"], [
                ["<strong>1:1</strong>", "de tekening is <strong>even groot</strong> als het voorwerp"],
                ["<strong>1:2</strong>", "de tekening is <strong>half zo groot</strong> als het voorwerp"],
                ["<strong>2:1</strong>", "de tekening is <strong>twee keer zo groot</strong> als het voorwerp"],
            ]), "De verhouding tussen de tekening en het echte voorwerp heet de <strong>schaal</strong>. Het "
                "eerste getal is de tekening, het tweede het voorwerp."),
        ]),
    ],
    onthoud=[
        "Maatbeker voor vloeistof, schuifmaat voor een kleine dikte, weegschaal, thermometer, multimeter.",
        "Symbolen: m voor massa, A voor oppervlakte, P voor omtrek, V voor volume, F voor kracht.",
        "SI-eenheden: meter, kilogram, newton. 1 km = 1000 m; 1 cm = 10 mm; 1 dm³ = 1 liter.",
        "Kilo duizend, hecto honderd, deca tien. Deci, centi en milli maken kleiner.",
        "Oppervlakte rechthoek = b · h. Omtrek vierkant = 4 · z. Volume balk = l · b · h.",
        "De functiedriehoek bevat functie, materiaal, bewerking en vorm; het is geen tekening.",
        "Conceptschets = eerste ruwe idee. Detailontwerp = één onderdeel, groter. Werktekening = technische tekening.",
        "Een ontvouwing is het platte patroon; isometrisch perspectief toont het voorwerp ruimtelijk.",
        "Vier aanzichten: voor, boven, zij en onder. Op een werktekening staan maten, aanzichten en schaal.",
        "1:1 even groot, 1:2 half zo groot, 2:1 dubbel zo groot.",
    ],
)

# ───────────────────────────────────────── 8. Transport en overbrengingen
BUNDELS["transport-en-overbrengingen"] = dict(
    vak=VAK, niveau=SPARK, titel="Transport en overbrengingen",
    onder="Drijver en volger, de zes overbrengingen van de fiche, en wat een overbrenging met snelheid en kracht doet.",
    secties=[
        dict(kop="Drijver en volger", blokken=[
            ("p", "Een <strong>transportsysteem</strong> is een systeem dat iets of iemand "
                  "<strong>verplaatst</strong>. Binnenin zit meestal een <strong>overbrenging</strong>: een "
                  "manier om een beweging door te geven."),
            ("p", "Het wiel dat de beweging <strong>geeft</strong>, heet de <strong>drijver</strong>. Het wiel "
                  "dat de beweging <strong>ontvangt</strong>, heet de <strong>volger</strong>. Verwissel ze "
                  "niet: de volger geeft niet, hij krijgt."),
            ("fig", tabel(["soort aandrijving", "wat het betekent", "voorbeeld"], [
                ["<strong>rechtstreeks</strong>", "de wielen raken elkaar zelf", "twee tandwielen die in elkaar grijpen"],
                ["<strong>onrechtstreeks</strong>", "er zit een <strong>riem of een ketting</strong> tussen", "de ketting van een fiets"],
            ]), "Een riemoverbrenging werkt dus juist tussen twee wielen die elkaar <em>niet</em> raken."),
        ]),
        dict(kop="De overbrengingen van de fiche", blokken=[
            ("fig", svg.overbrengingen(), "Vier ervan naast elkaar. <strong>Wrijvingswielen</strong> geven de "
                                          "beweging door doordat ze elkaar <strong>raken</strong>, en juist "
                                          "daarom kunnen ze <strong>slippen</strong>: ze houden elkaar alleen "
                                          "met wrijving vast."),
            ("fig", tabel(["overbrenging", "wat het is"], [
                ["<strong>tandwielen</strong>", "wielen met tanden die in elkaar grijpen; zo'n <strong>tandwieloverbrenging</strong> zit in een <strong>handmixer</strong>"],
                ["<strong>kettingen</strong>", "over twee tandwielen, zoals tussen de trappers en het achterwiel van een fiets"],
                ["<strong>riemen</strong>", "een band over twee wielen die elkaar niet raken"],
                ["<strong>wrijvingswielen</strong>", "wielen die elkaar raken; kunnen slippen"],
                ["<strong>katrollen</strong>", "een <strong>wiel met een groef waar een touw over loopt</strong>"],
                ["<strong>hefbomen</strong>", "een <strong>staaf die om een steunpunt draait</strong>"],
            ]), "De fiche noemt hefbomen, tandwielen, kettingen en wrijvingswielen uitdrukkelijk als "
                "overbrengingen, en katrollen en riemen horen er ook bij."),
            ("p", "Over een <strong>katrol</strong> loopt een touw of een kabel. Ze kan de "
                  "<strong>richting van een kracht veranderen</strong>, en met "
                  "<strong>meerdere</strong> katrollen hef je <strong>met minder kracht</strong>. Ze doet dus "
                  "meer dan alleen de richting van het touw veranderen."),
            ("fig", svg.hefboom(), "Een <strong>hefboom</strong> is een staaf die om een "
                                   "<strong>steunpunt</strong> draait. Een <strong>kruiwagen</strong> werkt "
                                   "zo. Gebruik je een <strong>langere arm</strong>, dan heb je "
                                   "<strong>minder kracht</strong> nodig, en til je een last op die je met je "
                                   "blote handen niet aankunt."),
            ("weetje", "Een <strong>ketting</strong> heeft één duidelijk voordeel boven een riem: hij "
                       "<strong>kan niet slippen</strong>. De schakels haken in de tanden."),
        ]),
        dict(kop="Snelheid, kracht en draaizin", blokken=[
            ("fig", tabel(["wat er gebeurt", "gevolg"], [
                ["een <strong>klein</strong> tandwiel drijft een <strong>groot</strong> aan", "het grote wiel draait <strong>trager</strong>"],
                ["een <strong>groot</strong> tandwiel drijft een <strong>klein</strong> aan", "het kleine wiel draait <strong>sneller</strong>"],
                ["twee <strong>even grote</strong> wielen met een riem", "ze draaien allebei <strong>even snel</strong>"],
            ]), "Hoe <strong>méér</strong> tanden een tandwiel heeft, hoe <strong>trager</strong> het draait bij "
                "dezelfde aandrijving. Niet sneller."),
            ("p", "Reken maar mee. Een tandwiel met <strong>10</strong> tanden drijft er een met "
                  "<strong>30</strong> aan. Gaat het kleine <strong>drie</strong> keer rond, dan zijn er "
                  "30 tanden gepasseerd, en dat is precies één omwenteling van het grote: het grote draait "
                  "<strong>één keer</strong> rond. Andersom: een tandwiel met <strong>40</strong> tanden drijft "
                  "er een met <strong>10</strong> aan. Eén omwenteling van het grote laat 40 tanden passeren, "
                  "dus het kleine draait <strong>vier keer</strong> rond."),
            ("p", "Een overbrenging kan de beweging <strong>versnellen</strong>, <strong>vertragen</strong> en "
                  "de <strong>richting</strong> ervan veranderen. Een overbrenging die de beweging trager maakt, "
                  "heet een <strong>vertraging</strong>. En meer snelheid gaat meestal "
                  "<strong>ten koste van kracht</strong>: je krijgt het een niet zonder het ander in te leveren."),
            ("kader", "De <strong>draaizin</strong>. Twee tandwielen die in elkaar grijpen, draaien in "
                      "<strong>tegengestelde</strong> zin. Twee wielen met een gewone, niet gekruiste riem "
                      "draaien in <strong>dezelfde</strong> zin. Laat je die riem <strong>kruisen</strong>, dan "
                      "draait de volger in de <strong>andere</strong> zin — en dat doen machines soms met opzet, "
                      "juist omdat de volger de andere kant op moet."),
            ("p", "Op een <strong>fiets</strong> zet je een <strong>licht verzet</strong> als je een helling "
                  "opfietst: je <strong>trapt lichter maar moet sneller trappen</strong>. Een "
                  "<strong>versnellingsbak</strong> doet hetzelfde in een auto: je kiest ermee tussen kracht en "
                  "snelheid, ze bevat tandwielen van verschillende grootte, en in een lage versnelling trek je "
                  "vlotter op."),
            ("p", "In de <strong>functiedriehoek</strong> van een transportsysteem staan de "
                  "<strong>functie</strong>, het <strong>materiaal</strong>, de <strong>bewerking</strong> en "
                  "de <strong>vorm</strong>."),
        ]),
    ],
    onthoud=[
        "De drijver geeft de beweging, de volger ontvangt ze.",
        "Rechtstreeks = de wielen raken elkaar. Onrechtstreeks = er zit een riem of ketting tussen.",
        "Overbrengingen: tandwielen, kettingen, riemen, wrijvingswielen, katrollen, hefbomen.",
        "Wrijvingswielen kunnen slippen; een ketting niet, want de schakels haken in de tanden.",
        "Een katrol verandert de richting van een kracht; met meerdere hef je met minder kracht.",
        "Een hefboom draait om een steunpunt; een langere arm vraagt minder kracht.",
        "Klein drijft groot = trager. Groot drijft klein = sneller. Meer tanden = trager.",
        "10 tanden drijft 30 aan: drie omwentelingen van het kleine = één van het grote.",
        "Tandwielen draaien tegengesteld; een gewone riem in dezelfde zin, een gekruiste riem omgekeerd.",
        "Meer snelheid gaat ten koste van kracht. Licht verzet: lichter trappen, sneller trappen.",
    ],
)

# ───────────────────────────────────────── 9. Biotechnische systemen
BUNDELS["biotechnische-systemen"] = dict(
    vak=VAK, niveau=SPARK, titel="Biotechnische systemen",
    onder="Micro-organismen die voor ons werken, de bewaartechnieken, het etiket en de verpakking.",
    secties=[
        dict(kop="Micro-organismen aan het werk", blokken=[
            ("p", "De vakfiche noemt drie <strong>micro-organismen</strong>: <strong>bacteriën</strong>, "
                  "<strong>schimmels</strong> en <strong>gisten</strong>. In een biotechnisch systeem laten we "
                  "ze <strong>voor ons werken</strong>."),
            ("fig", tabel(["wat er gebeurt", "wie het doet"], [
                ["brooddeeg <strong>rijst</strong>", "<strong>gist</strong>"],
                ["melk wordt <strong>yoghurt</strong>", "<strong>bacteriën</strong> zetten de melksuiker om"],
                ["melk wordt <strong>kaas</strong>", "ook daar komen micro-organismen aan te pas"],
                ["kool wordt <strong>zuurkool</strong>", "<strong>bacteriën fermenteren</strong> de kool"],
            ]), "<strong>Fermenteren</strong> is meteen ook een bewaartechniek: de micro-organismen doen het "
                "werk en maken het product tegelijk langer houdbaar."),
            ("p", "Over onze voeding waakt het <strong>FAVV</strong>, het <strong>Federaal Agentschap voor de "
                  "veiligheid van de voedselketen</strong>. Zijn taak is <strong>waken over de veiligheid van "
                  "ons voedsel</strong>, en het controleert daarvoor winkels, restaurants en "
                  "voedingsbedrijven."),
        ]),
        dict(kop="Bewaartechnieken", blokken=[
            ("fig", tabel(["techniek", "hoe het werkt"], [
                ["<strong>koelen</strong>", "de groei van bacteriën <strong>vertraagt</strong>"],
                ["<strong>invriezen</strong>", "de groei ligt zo goed als <strong>stil</strong>"],
                ["<strong>drogen</strong>", "zonder water kunnen bacteriën niet groeien"],
                ["<strong>pekelen</strong>", "bewaren in een <strong>zoute oplossing</strong>"],
                ["<strong>roken</strong>", "<strong>vlees</strong> of vis boven rook hangen: de rook <strong>remt bacteriën</strong> en geeft smaak"],
                ["<strong>vacuüm verpakken</strong>", "de lucht wordt er juist <strong>uit</strong> gehaald"],
                ["<strong>wecken</strong>", "voedsel wordt in een <strong>gesloten pot verhit</strong>"],
                ["<strong>fermenteren</strong>", "micro-organismen doen het werk"],
            ]), "<strong>Koelen en invriezen zijn niet hetzelfde</strong>: koelen remt, invriezen legt stil. "
                "Geen van beide <em>doodt</em> de bacteriën, dus ontdooid voedsel bederft weer gewoon."),
            ("fig", tabel(["bewaren met warmte", "wat het is"], [
                ["<strong>pasteuriseren</strong>", "kort verhitten tot onder het kookpunt"],
                ["<strong>steriliseren</strong>", "langer en heter verhitten"],
                ["<strong>UHT</strong>", "de melk is <strong>heel kort heel sterk verhit</strong>"],
            ]), "Drie technieken met warmte. UHT-melk blijft daardoor maanden goed zonder koelkast, tot je ze "
                "opent."),
        ]),
        dict(kop="Het etiket", blokken=[
            ("p", "Op het etiket van een voedingsmiddel moeten staan: de "
                  "<strong>ingrediëntenlijst</strong> (de lijst die alle bestanddelen opsomt), de "
                  "<strong>allergenen</strong> en de <strong>houdbaarheidsdatum</strong>. De "
                  "<strong>voedingswaarde</strong> staat erop zodat je weet <strong>hoeveel energie en stoffen "
                  "erin zitten</strong>. Een <strong>allergeen</strong> is een stof waar sommige mensen op "
                  "reageren."),
            ("kader", "Twee datums die niet hetzelfde betekenen. <strong>Ten minste houdbaar tot</strong>: "
                      "daarna kan de <strong>kwaliteit</strong> minder worden — het mag nog gegeten worden. "
                      "<strong>Te gebruiken tot</strong>: na die datum kan het product <strong>onveilig</strong> "
                      "zijn. Het eerste gaat over smaak, het tweede over gezondheid."),
        ]),
        dict(kop="De verpakking", blokken=[
            ("p", "Een verpakking doet drie dingen: het product <strong>beschermen bij het vervoer</strong>, "
                  "het <strong>langer houdbaar</strong> maken, en <strong>informatie doorgeven aan de "
                  "klant</strong>."),
            ("p", "Rode wijn zit in een <strong>donkere fles</strong> om een <strong>reactie met licht</strong> "
                  "tegen te gaan. Een <strong>plastic</strong> fles <strong>weegt minder</strong> dan een "
                  "glazen, dus het vervoer kost minder; het nadeel is dat ze <strong>meer afval in het "
                  "milieu</strong> geeft."),
            ("fig", tabel(["pictogram", "wat het betekent"], [
                ["<strong>pijlen die een driehoek vormen</strong>", "de verpakking is <strong>recycleerbaar</strong>"],
                ["een <strong>cijfer van 1 tot 7</strong> in het midden", "om welke <strong>soort kunststof</strong> het gaat"],
                ["een <strong>glas en een vork</strong>", "het materiaal is <strong>veilig voor voedsel</strong>"],
                ["het <strong>Groenpuntlogo</strong>", "het bedrijf betaalt mee voor de inzameling en verwerking — <em>niet</em> dat de verpakking van gerecycleerd materiaal is"],
                ["een <strong>doorstreepte vuilnisbak</strong>", "juist <strong>niet</strong> bij het huisvuil: apart inleveren"],
            ]), "Twee van deze vijf worden vaak verkeerd begrepen: het Groenpuntlogo en de doorstreepte "
                "vuilnisbak."),
            ("p", "<strong>Composteerbaar</strong> betekent dat de verpakking kan <strong>vergaan tot "
                  "compost</strong>. Een verpakking met <strong>statiegeld</strong> breng je terug naar de "
                  "winkel. En duurzaam omgaan met voedsel en verpakkingen doe je door "
                  "<strong>te kopen wat je echt nodig hebt</strong>, <strong>herbruikbare verpakkingen</strong> "
                  "te gebruiken en je <strong>afval goed te sorteren</strong>."),
        ]),
    ],
    onthoud=[
        "Micro-organismen: bacteriën, schimmels en gisten. Gist doet deeg rijzen, bacteriën maken yoghurt.",
        "Fermenteren laat micro-organismen het werk doen: zuurkool, yoghurt, kaas.",
        "Het FAVV waakt over de veiligheid van ons voedsel en controleert winkels, restaurants en bedrijven.",
        "Koelen remt, invriezen legt stil. Geen van beide doodt de bacteriën.",
        "Met warmte: pasteuriseren, steriliseren en UHT (heel kort heel sterk verhit).",
        "Drogen, pekelen, roken, vacuüm verpakken en wecken zijn de andere technieken.",
        "Op het etiket: ingrediëntenlijst, allergenen, houdbaarheidsdatum en voedingswaarde.",
        "Ten minste houdbaar tot = kwaliteit. Te gebruiken tot = veiligheid.",
        "Een verpakking beschermt, verlengt de houdbaarheid en geeft informatie.",
        "Driehoek van pijlen = recycleerbaar. Glas en vork = veilig voor voedsel. Doorstreepte bak = niet bij het huisvuil.",
    ],
)

# ───────────────────────────────────────── 10. Het technisch proces
BUNDELS["het-technisch-proces"] = dict(
    vak=VAK, niveau=SPARK, titel="Het technisch proces",
    onder="De vijf fasen van probleem tot evaluatie, probleemoplossend ontwerpen, en waarom STEM meer is dan techniek.",
    secties=[
        dict(kop="De vijf fasen", blokken=[
            ("p", "Het technisch proces heeft <strong>vijf</strong> fasen. Het begint altijd bij een "
                  "<strong>behoefte of een probleem</strong>, en het kan voor élk technisch systeem gebruikt "
                  "worden, niet alleen voor een constructiesysteem."),
            ("fig", svg.technischproces(), "De vijf fasen, en wat er gebeurt als het systeem niet voldoet."),
            ("fig", tabel(["fase", "wat er gebeurt"], [
                ["<strong>1</strong>", "je <strong>onderzoekt het probleem en de behoefte</strong>, en je legt de <strong>criteria</strong> vast"],
                ["<strong>2</strong>", "je <strong>ontwerpt en tekent</strong> het systeem"],
                ["<strong>3</strong>", "je <strong>maakt</strong> het technisch systeem"],
                ["<strong>4</strong>", "je <strong>neemt het in gebruik en test</strong> het"],
                ["<strong>5</strong>", "je <strong>evalueert</strong> en stuurt bij waar nodig"],
            ]), "In fase 5 ga je na of het systeem voldoet aan de opgestelde <strong>criteria</strong>. Een "
                "criterium is een <strong>eis waaraan je technisch systeem moet voldoen</strong>, en die stel je "
                "op in fase 1 — dus vóór het gemaakt is, nooit erna."),
            ("kader", "Voldoet je systeem niet, dan begin je <strong>niet</strong> helemaal opnieuw bij fase 1. "
                      "Je keert terug naar <strong>fase 2 of fase 3</strong>: het probleem en de criteria staan "
                      "immers al vast, alleen je ontwerp of je uitvoering klopt niet."),
        ]),
        dict(kop="Wat er in welke fase gebeurt", blokken=[
            ("p", "Bij de <strong>eerste fase</strong> horen: het <strong>probleem onderzoeken</strong>, een "
                  "<strong>behoefteonderzoek</strong> doen en de <strong>criteria vastleggen</strong>. Een "
                  "behoefteonderzoek is <strong>nagaan wat de gebruiker echt nodig heeft</strong> — niet wat jij "
                  "leuk vindt om te maken."),
            ("p", "Bij de <strong>ontwerpfase</strong> horen: een <strong>schets of een model</strong> maken, "
                  "het <strong>materiaal</strong> kiezen en het <strong>gereedschap</strong> kiezen. Je bepaalt "
                  "er ook welke <strong>verbindingstechnieken</strong> je gebruikt, welke "
                  "<strong>sensoren of actuatoren</strong> nodig zijn en welke "
                  "<strong>overbrengingen</strong> erin moeten komen."),
            ("p", "Het <strong>stappenplan</strong> om het systeem te maken, stel je <strong>vóór</strong> je "
                  "begint op en niet nadat het af is: zo weet je in welke <strong>volgorde</strong> je moet "
                  "werken. In de <strong>maakfase</strong> licht je toe hoe je <strong>veilig</strong> met het "
                  "gereedschap werkt. In de <strong>vierde</strong> fase neem je het systeem in gebruik of test "
                  "je het."),
        ]),
        dict(kop="Probleemoplossend ontwerpen", blokken=[
            ("p", "Bij <strong>probleemoplossend ontwerpen</strong> horen drie stappen: het probleem "
                  "<strong>duidelijk bepalen</strong>, <strong>criteria opstellen</strong> voor de oplossing, en "
                  "het probleem <strong>opsplitsen in deelproblemen</strong>. De allereerste stap is dus het "
                  "probleem <strong>duidelijk omschrijven</strong>."),
            ("p", "Opsplitsen in deelproblemen betekent dat je <strong>elk stuk apart aanpakt</strong>. "
                  "Achteraf voeg je de oplossingen weer samen, <strong>omdat ze samen het hele probleem moeten "
                  "oplossen</strong>."),
            ("p", "Soms hoef je helemaal niets nieuws te ontwerpen: het volstaat een "
                  "<strong>bestaand systeem aan te passen</strong>. En voldoet je oplossing niet aan de criteria, "
                  "dan <strong>stuur je ze bij</strong>: er wordt iets aan veranderd zodat ze beter voldoet. De "
                  "<strong>laatste</strong> stap is altijd <strong>testen en bijsturen</strong>."),
        ]),
        dict(kop="STEM", blokken=[
            ("fig", tabel(["letter", "waarvoor het staat", "in het Nederlands"], [
                ["<strong>S</strong>", "science", "wetenschappen"],
                ["<strong>T</strong>", "technology", "technologie"],
                ["<strong>E</strong>", "<strong>engineering</strong>", "ingenieurswerk, ontwerpen"],
                ["<strong>M</strong>", "<strong>mathematics</strong>", "wiskunde"],
            ]), "STEM gaat dus over vier disciplines samen en niet alleen over techniek."),
            ("p", "Waarom gebruik je bij een ontwerp kennis uit wetenschappen <em>én</em> wiskunde? Omdat een "
                  "goed ontwerp <strong>meer dan één invalshoek</strong> vraagt. Een ontwerp is niet goed als je "
                  "het probleem maar vanuit één vakgebied bekijkt."),
            ("weetje", "De <strong>coronacrisis</strong> is daar een schoolvoorbeeld van. Er was "
                       "<strong>wetenschappelijke</strong> kennis nodig om een vaccin te ontwikkelen, "
                       "<strong>wiskundige</strong> kennis om de verspreiding van het virus in kaart te brengen, "
                       "en <strong>technologische</strong> kennis om het vaccin koel te houden en te vervoeren."),
            ("p", "Er ontstaan steeds nieuwe technieken en materialen <strong>omdat de maatschappij voor nieuwe "
                  "uitdagingen staat</strong>: de <strong>klimaatverandering</strong>, een <strong>tekort aan "
                  "grondstoffen</strong> en de <strong>zorg voor een ouder wordende bevolking</strong>."),
        ]),
    ],
    onthoud=[
        "Vijf fasen: probleem onderzoeken, ontwerpen, maken, in gebruik nemen en testen, evalueren.",
        "Een criterium is een eis waaraan het systeem moet voldoen; je legt ze vast in fase 1.",
        "Voldoet het niet, dan keer je terug naar fase 2 of 3, niet naar fase 1.",
        "Een behoefteonderzoek gaat na wat de gebruiker echt nodig heeft.",
        "In de ontwerpfase: schets of model, materiaal, gereedschap, verbindingen, sensoren, overbrengingen.",
        "Het stappenplan maak je vóór je begint, zodat je de volgorde kent.",
        "Probleemoplossend ontwerpen: probleem bepalen, criteria opstellen, opsplitsen in deelproblemen.",
        "Soms volstaat het een bestaand systeem aan te passen. De laatste stap is testen en bijsturen.",
        "STEM = science, technology, engineering, mathematics. Vier disciplines, niet alleen techniek.",
        "Nieuwe uitdagingen: klimaatverandering, tekort aan grondstoffen, een ouder wordende bevolking.",
    ],
)

# ───────────────────────────────────────── 11. Algoritmen en computationeel denken
BUNDELS["algoritmen-en-computationeel-denken"] = dict(
    vak=VAK, niveau=SPARK, titel="Algoritmen en computationeel denken",
    onder="Wat een algoritme is, hoe je er een ontwerpt en test, en de vier principes van computationeel denken.",
    secties=[
        dict(kop="Wat is een algoritme?", blokken=[
            ("p", "Een <strong>algoritme</strong> is een <strong>stappenplan met instructies in een vaste "
                  "volgorde</strong>. Die volgorde ligt vast: je mag de stappen niet zomaar wisselen, en "
                  "ontbreekt er één stap, dan <strong>klopt het resultaat meestal niet meer</strong>."),
            ("p", "Een algoritme hoeft <strong>niet</strong> op een computer te draaien. Een "
                  "<strong>niet-digitaal</strong> algoritme voer je zonder computer uit: een "
                  "<strong>recept</strong> om een cake te bakken, een stappenplan om een boterham met choco te "
                  "smeren. Een <strong>digitaal</strong> algoritme wel: de code van een computerspel, of een "
                  "programma dat een lampje laat flikkeren."),
            ("p", "Met een algoritme kan je van alles laten doen: controleren of een getal een "
                  "<strong>priemgetal</strong> is, <strong>getallen sorteren</strong> van klein naar groot, een "
                  "<strong>rechthoek laten tekenen</strong> op het scherm. Het werkt voor "
                  "<strong>eenvoudige én ingewikkelde</strong> problemen."),
        ]),
        dict(kop="Een algoritme ontwerpen", blokken=[
            ("fig", svg.stappen(["probleemstelling|formuleren", "analyseren|met IPO",
                                 "algoritme|schrijven", "testen en|bijsturen"]),
             "De stappen die de fiche noemt. <strong>IPO</strong> staat hier voor "
             "<strong>input, process en output</strong>: voor je een algoritme schrijft, bekijk je "
             "<strong>wat erin gaat en wat eruit moet komen</strong>. De <strong>programmeertaal</strong> "
             "waarin je het daarna vertaalt, is volgens de fiche <strong>Scratch</strong>."),
            ("p", "Je <strong>test</strong> een algoritme uit <strong>om te zien of het echt doet wat je "
                  "wilde</strong>. Geeft het niet het juiste resultaat, dan <strong>stuur je het bij</strong>. "
                  "Testen is dus geen formaliteit achteraf maar een echte stap."),
            ("p", "Een <strong>flowchart</strong> is een schema met pijlen dat de stappen van een algoritme "
                  "toont. Het heet ook een <strong>stroomdiagram</strong>, en het dient om de oplossing "
                  "<strong>visueel voor te stellen</strong>."),
            ("fig", tabel(["vorm in een flowchart", "wat ze betekent"], [
                ["een <strong>afgeronde rechthoek</strong>", "het begin of het einde"],
                ["een <strong>parallellogram</strong>", "invoer of uitvoer"],
                ["een <strong>rechthoek</strong>", "een bewerking of een instructie"],
                ["een <strong>ruit</strong>", "een keuze: ja of nee"],
                ["een <strong>pijl</strong>", "de volgorde waarin je gaat"],
            ]), "Volgens de vakfiche vertaal je je algoritme daarna in <strong>Scratch</strong>."),
        ]),
        dict(kop="Computationeel denken", blokken=[
            ("p", "De vakfiche noemt <strong>vier</strong> principes van computationeel denken: "
                  "<strong>abstractie</strong>, <strong>decompositie</strong>, "
                  "<strong>patroonherkenning</strong> en <strong>het algoritme</strong> zelf. De eerste drie "
                  "helpen je een <strong>efficiënt</strong> algoritme te schrijven."),
            ("fig", tabel(["principe", "wat het is", "voorbeeld"], [
                ["<strong>abstractie</strong>", "<strong>details weglaten</strong> die er niet toe doen",
                 "leg je de weg naar school uit, dan laat je de <strong>kleur van de huizen</strong> weg"],
                ["<strong>decompositie</strong>", "een probleem in <strong>kleinere delen opsplitsen</strong>",
                 "bij een spel apart werken aan de beweging, de punten en het geluid"],
                ["<strong>patroonherkenning</strong>", "<strong>gelijkenissen</strong> tussen problemen zien",
                 "een spel met tien niveaus die sterk op elkaar lijken"],
            ]), "Abstractie betekent dus juist <strong>minder</strong> details, niet meer. Decompositie maakt "
                "een groot probleem overzichtelijker, en patroonherkenning laat je een oplossing "
                "<strong>hergebruiken</strong> die je al kent."),
            ("p", "Je gebruikt <strong>decompositie</strong> als een probleem <strong>te groot is voor één "
                  "keer</strong>, als verschillende delen <strong>los van elkaar</strong> werken, en als je "
                  "<strong>met meerdere mensen samen</strong> werkt."),
        ]),
        dict(kop="Fouten zoeken", blokken=[
            ("p", "Een <strong>bug</strong> is een <strong>fout in een programma</strong>. Het opsporen en "
                  "oplossen van zo'n fout heet <strong>debuggen</strong>."),
            ("p", "Moet een programma een vierkant tekenen maar maakt het er maar drie zijden van, dan "
                  "<strong>debug</strong> je het algoritme: je zoekt de stap die ontbreekt of fout staat."),
            ("kader", "Een fout vind je <strong>niet</strong> alleen door naar de code te kijken. Vaak zie je ze "
                      "pas door het algoritme <strong>uit te voeren</strong> en te vergelijken met wat je "
                      "verwachtte. Daarom is testen een eigen stap."),
            ("p", "<strong>Efficiënt</strong> betekent <strong>niet</strong> dat een algoritme zoveel mogelijk "
                  "stappen heeft, maar net zo weinig mogelijk. Een <strong>korter</strong> algoritme met "
                  "dezelfde uitkomst is meestal beter, omdat er <strong>minder fouten in kunnen "
                  "sluipen</strong>."),
        ]),
    ],
    onthoud=[
        "Een algoritme is een stappenplan met instructies in een vaste volgorde.",
        "Niet-digitaal: een recept, een stappenplan. Digitaal: de code van een spel, een programma.",
        "Een flowchart of stroomdiagram stelt de oplossing visueel voor, met pijlen tussen de stappen.",
        "Ontwerpen: probleemstelling formuleren, analyseren met IPO, schrijven, testen en bijsturen.",
        "IPO = input, process, output: wat gaat erin en wat moet eruit komen?",
        "Je vertaalt je algoritme volgens de fiche in Scratch.",
        "Vier principes: abstractie, decompositie, patroonherkenning en het algoritme.",
        "Abstractie = details weglaten. Decompositie = opsplitsen. Patroonherkenning = gelijkenissen zien.",
        "Een bug is een fout in een programma; die opsporen en oplossen heet debuggen.",
        "Efficiënt is zo weinig mogelijk stappen: in een korter algoritme sluipen minder fouten.",
    ],
)

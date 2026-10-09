# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij sociale en gedragswetenschappen 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus dezelfde pdf hangt bij allebei. Twintig bundels,
dezelfde twintig sleutels als in `maak_sgw.py`, met `oefenbundel-` ervoor.

De oefeningen zijn met opzet ándere vragen dan die op het scherm. Dit vak
bestaat bijna helemaal uit lijstjes en uit begrippen die op elkaar lijken, dus
de oefeningen zijn daarop gebouwd: een situatie bij het juiste begrip zetten, een
schema aanvullen, en in je eigen woorden zeggen waarom twee begrippen niet
hetzelfde zijn. Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/sociale-en-gedragswetenschappen.json`.

Eén waarschuwing, dezelfde als bij de vragen en de leerbundels: de fiche noemt
een veertigtal eigennamen. **Zet er geen naam bij die niet in de fiche staat, en
hang aan een naam geen onderzoek dat de fiche niet vermeldt.** Een verzonnen
experiment bij een echte onderzoeker leest als een feit, en dat is hier de
gevaarlijkste fout die je kan maken.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Sociale en gedragswetenschappen"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "130px"
WW = "200px"
WL = "260px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een situatie: zeg niet alleen welk begrip het is, maar ook waaraan je het ziet.",
    "Lees bij twee begrippen die op elkaar lijken eerst nog eens wat ze onderscheidt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-ontwikkelingspsychologie-de-begrippen-en-de-drie-basisvragen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkelingspsychologie: de begrippen en de drie basisvragen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Groeien, rijpen of leren",
             opdracht="Schrijf bij elk voorbeeld of het groei, rijping of leren is.",
             oefeningen=[
                 ("rij", [("een kind wordt tien centimeter langer", "groei"),
                          ("een baby kan plots zelf rechtop zitten", "rijping"),
                          ("een kind kent de tafels van buiten", "leren"),
                          ("de tanden komen door", "rijping")],
                  "Groei, rijping of leren?", WW),
                 ("rij", [("een tiener leert zwemmen", "leren"),
                          ("de voeten worden een maat groter", "groei"),
                          ("een kind begint te brabbelen", "rijping"),
                          ("een kind leert een gsm gebruiken", "leren")],
                  "Groei, rijping of leren?", WW),
                 ("open", "Groei en rijping gaan beide vanzelf. Leg in twee zinnen uit wat ze dan "
                          "toch onderscheidt.",
                  "Groei gaat over het lichaam dat groter of zwaarder wordt, dus over een verandering "
                  "in omvang. Rijping gaat over nieuwe mogelijkheden die zich openen volgens een "
                  "ingebouwd plan, zoals kunnen zitten of praten. Groei is meer van hetzelfde, "
                  "rijping is iets nieuws dat kan.", 4),
             ]),
        dict(kop="De negen levensloopfasen",
             opdracht="Vul de fase in die bij de leeftijd hoort.",
             oefeningen=[
                 ("tabel", ["Leeftijd", "Fase"],
                  [["van de bevruchting tot de geboorte", None],
                   ["ongeveer het eerste levensjaar", None],
                   ["ongeveer 1 tot 3 jaar", None],
                   ["ongeveer 3 tot 6 jaar", None],
                   ["ongeveer 6 tot 12 jaar", None]],
                  "prenatale fase; babytijd; peutertijd; vroege kindertijd of kleutertijd; "
                  "midden kindertijd of lagere schoolkindfase", W),
                 ("kort", "Hoeveel levensloopfasen noemt de fiche?", "negen", W),
                 ("waar", "De levensloopfasen stoppen bij het einde van de adolescentie, want daarna "
                          "ontwikkelt een mens niet meer.", False),
             ]),
        dict(kop="De vijf ontwikkelingsdomeinen",
             opdracht="Zet bij elk voorbeeld het domein waar het hoort.",
             oefeningen=[
                 ("rij", [("een kind leert op één been staan", "fysieke ontwikkeling"),
                          ("een kind onthoudt een rijtje van zeven cijfers", "cognitieve ontwikkeling"),
                          ("een kind zegt dat spieken niet eerlijk is", "morele ontwikkeling"),
                          ("een kind zegt zijn boosheid in woorden",
                           "socio-emotionele ontwikkeling")],
                  "Welk ontwikkelingsdomein?", WL),
                 ("rij", [("een tiener weet waar ze voor staat", "persoonlijkheidsontwikkeling"),
                          ("een kind leert een strik maken", "fysieke ontwikkeling"),
                          ("een kind wacht op zijn toer", "socio-emotionele ontwikkeling"),
                          ("een kind begrijpt dat water hetzelfde blijft in een andere beker",
                           "cognitieve ontwikkeling")],
                  "Welk ontwikkelingsdomein?", WL),
                 ("open", "Een kind spreekt moeilijk en durft daardoor niets te zeggen in de klas, "
                          "waardoor het weinig vrienden maakt. Welke twee domeinen werken hier in "
                          "elkaar, en in welke richting?",
                  "Het fysieke domein werkt door in het socio-emotionele: het moeilijk spreken is "
                  "fysiek, en het weinig vrienden maken is socio-emotioneel. Dat de domeinen niet "
                  "los van elkaar staan, is precies wat je hier ziet.", 4),
                 ("open", "De fiche vraagt ook om één domein door verschillende fasen heen te "
                          "volgen. Doe dat voor de morele ontwikkeling: beschrijf kort wat je bij een "
                          "kleuter, bij een kind van tien en bij een adolescent verwacht.",
                  "Bij een kleuter hangt goed en kwaad nog vast aan de straf of de beloning die erop "
                  "volgt. Bij een kind van tien gaat het om de regel en om wat hoort, zoals de "
                  "leerkracht of de ouders het zeggen. Bij een adolescent komt het eigen oordeel "
                  "erbij: hij kan een regel afwegen en ertegen ingaan als hij ze onrechtvaardig "
                  "vindt.", 6),
             ]),
        dict(kop="De drie basisvragen",
             opdracht="Lees de uitspraak en zeg over welke basisvraag ze gaat, en welke kant ze kiest.",
             oefeningen=[
                 ("kies", "Een onderzoeker zegt: een kind kan plots iets wat het de dag ervoor nog "
                          "niet kon, en daarna verandert er een hele tijd niets. Welke basisvraag?",
                  ["continu of discontinu, en hij kiest discontinu",
                   "continu of discontinu, en hij kiest continu",
                   "nature of nurture, en hij kiest nature",
                   "cultureel of universeel, en hij kiest cultureel"], 0),
                 ("kies", "Een onderzoeker zegt: baby's over de hele wereld kruipen eerst en stappen "
                          "daarna. Welke basisvraag, en welke kant?",
                  ["cultureel of universeel, en hij kiest universeel",
                   "cultureel of universeel, en hij kiest cultureel",
                   "continu of discontinu, en hij kiest continu",
                   "nature, nurture en zelfbepaling, en hij kiest nurture"], 0),
                 ("rij", [("zij heeft het muzikale van haar vader", "nature"),
                          ("zij zat van haar zesde in de muziekschool", "nurture"),
                          ("zij koos op haar vijftiende zelf voor drum", "zelfbepaling"),
                          ("hij groeide op in een huis vol boeken", "nurture")],
                  "Nature, nurture of zelfbepaling?", WW),
                 ("kort", "Hoeveel dingen zet de tweede basisvraag tegenover elkaar?", "drie", W),
                 ("waar", "De tweede basisvraag zet enkel de genen tegenover de omgeving.", False),
                 ("open", "Op welke leeftijd een kind geacht wordt zelf te beslissen, verschilt sterk "
                          "van samenleving tot samenleving. Welke basisvraag raakt dat, en welke kant "
                          "wijst het aan?",
                  "De derde basisvraag: is ontwikkeling cultureel bepaald of universeel? Dat de "
                  "leeftijd per samenleving verschilt, wijst op een culturele factor.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ontwikkeling-de-biologische-en-de-psychodynamische-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de biologische en de psychodynamische benadering",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Drie biologische theorieën",
             opdracht="Vul de tabel aan met de naam uit de fiche en de kern van de theorie.",
             oefeningen=[
                 ("tabel", ["Theorie", "Naam", "De kern"],
                  [["evolutionaire psychologie", None, None],
                   ["rijpingstheorie", None, None],
                   ["epigenetica", None, None]],
                  "Charles Darwin, gedrag dat onze voorouders hielp overleven is doorgegeven; "
                  "Arnold Gesell, ontwikkeling komt van binnenuit en volgt een vaste orde; "
                  "Conrad Waddington, de omgeving zet genen aan of uit zonder het DNA te veranderen", WW),
                 ("rij", [("baby's over de hele wereld schrikken van een plots hard geluid",
                           "evolutionaire psychologie"),
                          ("op welke leeftijd kinderen doorgaans beginnen te stappen",
                           "rijpingstheorie"),
                          ("zware stress tijdens een zwangerschap kan genen aan of uit zetten",
                           "epigenetica")],
                  "Welke theorie?", WL),
                 ("open", "Waarom mag je de drie biologische theorieën niet op één hoop gooien? "
                          "Gebruik de epigenetica en de rijpingstheorie in je antwoord.",
                  "Omdat ze de omgeving niet dezelfde plaats geven. De rijpingstheorie laat de "
                  "ontwikkeling van binnenuit komen in een vaste orde, dus de omgeving doet er weinig "
                  "toe. De epigenetica vertrekt wel bij de genen, maar laat de omgeving die genen aan "
                  "of uit zetten. Ze geven dus een ander antwoord op de basisvragen.", 5),
                 ("waar", "Bij de epigenetica verandert het DNA zelf.", False),
                 ("open", "Twee kinderen met dezelfde genen groeien in een ander gezin heel anders op. "
                          "Welke van de drie theorieën kan dat het best uitleggen, en waarom?",
                  "De epigenetica, want zij geeft de omgeving een rol: dezelfde genen kunnen in een "
                  "andere omgeving aan of uit gezet worden. De evolutionaire psychologie en de "
                  "rijpingstheorie krijgen dat verschil moeilijk uitgelegd.", 4),
             ]),
        dict(kop="Freud en Erikson naast elkaar",
             opdracht="Vul in.",
             oefeningen=[
                 ("tabel", ["", "Freud", "Erikson"],
                  [["naam van de theorie", None, None],
                   ["aantal fasen", None, None],
                   ["tot wanneer lopen de fasen?", None, None]],
                  "de psychoanalyse en de psychosociale ontwikkelingstheorie; 5 en 8; "
                  "bij Freud tot de adolescentie, bij Erikson tot in de late volwassenheid", W),
                 ("kort", "Hoe heet het lichaamsdeel waar bij Freud in elke fase het plezier op "
                          "gericht is?", "de erogene zone", WW),
                 ("kort", "Hoe heet het bij Freud als iemand met een stuk van zich in een vroegere "
                          "fase blijft hangen?", "een fixatie", WW),
                 ("open", "Bij Erikson hoort bij elke fase een crisis. Leg uit waarom een crisis bij "
                          "hem geen ramp is.",
                  "Een crisis is bij Erikson een vraag of een spanning die in die fase opgelost moet "
                  "worden om verder te kunnen. Het is dus een opdracht die bij die leeftijd hoort, en "
                  "ze hoort bij een gewone ontwikkeling. Loopt ze goed af, dan kom je bij de "
                  "positieve pool.", 5),
                 ("kies", "Welk bezwaar wordt het vaakst tegen de psychoanalyse van Freud ingebracht?",
                  ["wat ze beschrijft is moeilijk met onderzoek te meten, en ze steunt op zijn eigen "
                   "patiënten",
                   "ze werkt met te veel fasen om ze te kunnen onthouden",
                   "ze geeft de omgeving te veel gewicht tegenover de genen",
                   "ze loopt door tot in de late volwassenheid en is daardoor te breed"], 0),
             ]),
        dict(kop="De basisvragen op deze twee benaderingen",
             opdracht="Antwoord in een korte zin of met het juiste woord.",
             oefeningen=[
                 ("kort", "Antwoorden Freud en Erikson continu of discontinu op de eerste basisvraag?",
                  "discontinu", WW),
                 ("open", "Freud en Erikson antwoorden niet hetzelfde op de tweede basisvraag. Wat is "
                          "het verschil?",
                  "Erikson rekent de omgeving veel zwaarder mee: bij hem spelen de mensen rond het "
                  "kind en de samenleving een grote rol in hoe een crisis afloopt. Freud legt de motor "
                  "veel meer binnen in de persoon zelf.", 4),
                 ("open", "Wat hebben de biologische en de psychodynamische benadering met elkaar "
                          "gemeen?",
                  "Beide leggen het begin van de ontwikkeling in het individu zelf. Bij de biologische "
                  "benadering zit de motor in de genen en de rijping, bij de psychodynamische in de "
                  "krachten binnen in de persoon. Geen van de twee begint bij de omgeving.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ontwikkeling-de-behavioristische-en-de-cognitieve-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de behavioristische en de cognitieve benadering",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Klassieke conditionering",
             opdracht="Een hond krijgt telkens een lampje te zien voor hij zijn brokjes krijgt. Na een "
                      "tijd kwijlt hij al bij het lampje. Vul de vier begrippen in.",
             oefeningen=[
                 ("tabel", ["Begrip", "Wat het is in dit voorbeeld"],
                  [["ongeconditioneerde stimulus", None],
                   ["ongeconditioneerde reflex", None],
                   ["neutrale stimulus", None],
                   ["geconditioneerde stimulus", None],
                   ["geconditioneerde reflex", None]],
                  "de brokjes; het kwijlen bij de brokjes; het lampje voor het koppelen; "
                  "het lampje na het koppelen; het kwijlen bij het lampje alleen", WL),
                 ("open", "Hoe wordt een neutrale stimulus een geconditioneerde stimulus?",
                  "Door ze telkens samen met de ongeconditioneerde stimulus aan te bieden. Na vele "
                  "keren koppelen roept ze de reactie zelf op.", 3),
                 ("kort", "Waar staat de S voor in het S-R-schema, en waar de R?",
                  "stimulus of prikkel, en respons of reactie", WL),
                 ("waar", "Het Little Albert-experiment van Watson is een voorbeeld van operante "
                          "conditionering.", False),
             ]),
        dict(kop="De vier soorten gevolg",
             opdracht="Werk in twee stappen. Eerst: neemt het gedrag toe (bekrachtiging) of af (straf)? "
                      "Dan: komt er iets bij (positief) of gaat er iets weg (negatief)?",
             oefeningen=[
                 ("rij", [("een sticker voor wie opruimt", "positieve bekrachtiging"),
                          ("een week niet gamen na een ruzie", "negatieve straf"),
                          ("geen vaat in de week dat je al je taken maakt", "negatieve bekrachtiging"),
                          ("een standje als de hond op de zetel springt", "positieve straf")],
                  "Welk soort gevolg?", WL),
                 ("rij", [("je mama zet de muziek af als je begint te roepen", "negatieve straf"),
                          ("je krijgt een compliment na je spreekbeurt", "positieve bekrachtiging"),
                          ("de zeurtoon stopt zodra je je gordel omdoet", "negatieve bekrachtiging"),
                          ("je moet strafwerk maken na het spieken", "positieve straf")],
                  "Welk soort gevolg?", WL),
                 ("open", "Leg uit waarom negatieve bekrachtiging geen straf is, al staat er negatief "
                          "bij.",
                  "Negatief betekent hier wegnemen, niet onaangenaam. Bij negatieve bekrachtiging gaat "
                  "er iets onaangenaams weg, en daardoor neemt het gedrag toe. Dat is precies wat "
                  "bekrachtiging doet: gedrag doen toenemen. Straf doet gedrag afnemen.", 5),
                 ("kort", "Waar staat de C voor in het S-R-C-schema van Skinner?",
                  "consequentie of gevolg", WW),
             ]),
        dict(kop="Bandura en Piaget",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het leren door te kijken naar wat een ander doet?",
                  "modelleren of imitatieleren", WL),
                 ("open", "Waarom noemt de fiche Bandura een voorloper van de cognitieve benadering en "
                          "geen zuivere behaviorist?",
                  "Omdat bij hem leren ook gebeurt zonder dat het kind zelf bekrachtigd wordt: het "
                  "kijkt, slaat op en past later toe. Er gebeurt dus iets in het hoofd, en dat is "
                  "precies wat een zuiver behaviorist buiten beschouwing laat.", 4),
                 ("tabel", ["Stadium van Piaget", "Wat erin kan"],
                  [["sensomotorisch", None],
                   ["pre-operationeel", None],
                   ["concreet-operationeel", None],
                   ["formeel-operationeel", None]],
                  "leren via de zintuigen en de beweging; denken met beelden en woorden, nog niet "
                  "logisch; logisch denken over tastbare dingen; abstract denken over wat er niet is",
                  WL),
                 ("kies", "Een kleuter denkt dat een hoge smalle beker meer bevat dan een lage brede. "
                          "In welk stadium zit dat kind?",
                  ["pre-operationeel", "sensomotorisch", "concreet-operationeel",
                   "formeel-operationeel"], 0),
                 ("waar", "Volgens Piaget kan een kind een stadium overslaan als het snel leert.",
                  False),
             ]),
        dict(kop="Het geheugen",
             opdracht="Zet bij elk voorbeeld het juiste onderdeel van het langetermijngeheugen.",
             oefeningen=[
                 ("rij", [("weten waar je was toen je dat bericht kreeg", "episodisch"),
                          ("weten dat Brussel de hoofdstad van België is", "semantisch"),
                          ("kunnen fietsen zonder erbij na te denken", "procedureel"),
                          ("weten hoe je een strik maakt met je handen", "procedureel")],
                  "Episodisch, semantisch of procedureel?", WW),
                 ("tabel", ["Geheugen", "Wat het doet"],
                  [["sensorisch geheugen", None],
                   ["kortetermijngeheugen", None],
                   ["langetermijngeheugen", None]],
                  "vangt heel kort op wat je zintuigen binnenbrengen; houdt even vast waar je nu mee "
                  "bezig bent; bewaart wat blijft", WL),
                 ("open", "Welke twee onderdelen van het langetermijngeheugen zijn expliciet, en welk "
                          "is impliciet? Wat betekent dat verschil?",
                  "Het episodische en het semantische geheugen zijn expliciet: je kan zeggen wat erin "
                  "zit. Het procedurele geheugen is impliciet: je kan het doen zonder het te kunnen "
                  "uitleggen, zoals fietsen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ontwikkeling-de-humanistische-en-de-systemische-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de humanistische en de systemische benadering",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Maslow en Rogers",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Laag bij Maslow", "Wat ze vraagt"],
                  [["zelfontplooiing", None],
                   ["waardering en erkenning", None],
                   ["contact en verbondenheid", None],
                   ["veiligheid en zekerheid", None],
                   ["lichamelijke behoeften", None]],
                  "worden wie je kan worden; gezien en gewaardeerd worden; ergens bij horen; "
                  "weten waar je morgen woont; eten, drinken, slapen", WL),
                 ("open", "Een school zorgt eerst voor een ontbijt en een vaste structuur, en begint "
                          "pas daarna te werken aan motivatie. Waarom past dat bij Maslow?",
                  "Omdat bij Maslow de lagere behoeften eerst komen: wie honger heeft of zich onveilig "
                  "voelt, komt niet aan de hogere behoeften toe. Een ontbijt vult de lichamelijke "
                  "behoeften en een vaste structuur geeft veiligheid; daarna is er ruimte voor "
                  "waardering en zelfontplooiing.", 5),
                 ("open", "Welk bezwaar wordt tegen de vaste orde van Maslow ingebracht?",
                  "Dat die orde niet bij iedereen standhoudt: mensen zetten soms een hogere behoefte "
                  "voorop terwijl een lagere niet vervuld is, bijvoorbeeld iemand die hongerig verder "
                  "werkt aan iets wat hij belangrijk vindt.", 4),
                 ("kort", "Wat betekent client centered bij Rogers?",
                  "de persoon zelf staat in het midden", WL),
                 ("kies", "Welke drie houdingen horen bij Rogers?",
                  ["aanvaarden zoals iemand is, echt en open zijn, en meevoelen",
                   "belonen, straffen en negeren",
                   "observeren, meten en rapporteren",
                   "sturen, plannen en evalueren"], 0),
             ]),
        dict(kop="Bronfenbrenner",
             opdracht="Zet bij elk voorbeeld het systeem waar het hoort.",
             oefeningen=[
                 ("rij", [("het gezin en de klas", "microsysteem"),
                          ("de juf die met de ouders belt", "mesosysteem"),
                          ("de nachtdienst van een ouder", "exosysteem"),
                          ("de leerplicht", "macrosysteem")],
                  "Welk systeem?", WW),
                 ("rij", [("opgroeien met een smartphone", "chronosysteem"),
                          ("de voetbalclub waar het kind elke week naartoe gaat", "microsysteem"),
                          ("de waarden van een land", "macrosysteem"),
                          ("de trainer die met de leerkracht overlegt", "mesosysteem")],
                  "Welk systeem?", WW),
                 ("waar", "In het microsysteem zijn de interacties direct en in het exosysteem "
                          "indirect.", True),
                 ("open", "Leg met een voorbeeld uit dat de systemen door elkaar werken en niet één na "
                          "één.",
                  "Een wet uit het macrosysteem, bijvoorbeeld over nachtarbeid, verandert het werk van "
                  "een ouder in het exosysteem, en dat verandert hoe het gezin in het microsysteem "
                  "leeft. Eén verandering helemaal buiten het kind komt zo tot bij het kind.", 5),
             ]),
        dict(kop="Vygotsky",
             opdracht="Antwoord kort en vul aan.",
             oefeningen=[
                 ("tabel", ["Zone", "Wat het leren doet"],
                  [["comfortzone", None],
                   ["zone van de naaste ontwikkeling", None],
                   ["groeizone", None],
                   ["angstzone", None]],
                  "er valt niets bij te leren; hier zit de leerwinst, want je kan het met hulp; "
                  "hier gebeurt het leren, met steun; het leren valt stil", WL),
                 ("kort", "Hoe heet hulp die je stap voor stap weer afbouwt?", "scaffolding", WW),
                 ("open", "Waarom is een steiger een goed beeld voor scaffolding?",
                  "Omdat een steiger er staat zolang het gebouw hem nodig heeft en weggaat als het "
                  "zelf rechtstaat. Zo geef je eerst een voorbeeld, dan een half voorbeeld, en dan "
                  "niets meer. De hulp is bedoeld om te verdwijnen.", 4),
                 ("kort", "Hoe heet het proces waarin wat eerst samen met anderen gebeurt eigen denken "
                          "wordt?", "interiorisatie", WW),
                 ("kies", "Een kind telt eerst luidop met de juf en later in zijn hoofd. Welk begrip?",
                  ["het interiorisatieproces", "scaffolding", "de angstzone",
                   "het chronosysteem"], 0),
                 ("open", "Op de derde basisvraag antwoordt Vygotsky dat ontwikkeling eerder cultureel "
                          "bepaald is. Waar zie je dat al in de naam van zijn theorie?",
                  "Zijn theorie heet de sociaal-culturele theorie. Wat een kind leert en hoe het "
                  "leert, hangt bij hem af van de cultuur waarin het opgroeit en van de mensen om "
                  "zich heen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-prosociaal-gedrag-antisociaal-gedrag-en-sociale-cognitie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Prosociaal gedrag, antisociaal gedrag en sociale cognitie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Prosociaal of antisociaal",
             opdracht="Schrijf bij elk gedrag of het prosociaal of antisociaal is, en welke vorm uit "
                      "de lijst van de fiche het is.",
             oefeningen=[
                 ("rij", [("je laat een klasgenoot meelezen uit je boek", "prosociaal, delen"),
                          ("je maakt een bank op het plein stuk", "antisociaal, vandalisme"),
                          ("je gaat bij iemand zitten die huilt", "prosociaal, troosten"),
                          ("je zegt dat je thuis was terwijl je weg was",
                           "antisociaal, liegen en bedriegen")],
                  "Welke vorm?", WL),
                 ("rij", [("je neemt de taak van de groep op je", "prosociaal, verantwoordelijkheid "
                           "opnemen"),
                          ("je duwt iemand opzij in de rij", "antisociaal, agressie"),
                          ("de hele klas roept door de les", "antisociaal, ongepast groepsgedrag"),
                          ("jullie maken samen één verslag", "prosociaal, samenwerken")],
                  "Welke vorm?", WL),
                 ("open", "De fiche noemt bij de groep zowel positief als ongepast groepsgedrag. Wat "
                          "leert dat je over samen iets doen?",
                  "Dat samen iets doen op zich niets zegt over goed of slecht. Een groep kan samen "
                  "iets opbouwen en samen iets afbreken; het is het gedrag zelf dat beslist of het "
                  "prosociaal of antisociaal is.", 4),
                 ("open", "Iemand helpt een buurvrouw met haar boodschappen omdat hij hoopt dat zij "
                          "straks op zijn hond past. Is dat prosociaal gedrag? Leg uit.",
                  "Ja. De fiche kijkt naar het gedrag zelf en niet naar de reden erachter. Helpen "
                  "staat in de lijst van prosociaal gedrag, ook als er een eigen voordeel achter zit.",
                  4),
                 ("waar", "Agressie is gericht op spullen en vandalisme op personen.", False),
             ]),
        dict(kop="Attitude en attributie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Welke drie mentale processen rekent de fiche tot de sociale cognitie?",
                  "attitude, attributie en cognitieve dissonantie", WL),
                 ("open", "Iemand denkt heel milieubewust en neemt toch bijna altijd de auto. Wat zegt "
                          "dat over het verband tussen een attitude en gedrag?",
                  "Dat het verband niet absoluut is. Een attitude maakt bepaald gedrag "
                  "waarschijnlijker, maar ze beslist het niet: er spelen ook gewoonte, gemak en "
                  "omstandigheden mee.", 4),
                 ("rij", [("die chauffeur is gewoon onbeschoft", "interne of dispositionele attributie"),
                          ("er was file, daarom ben ik te laat", "externe of situationele attributie"),
                          ("zij haalde het omdat ze er hard voor werkte",
                           "interne of dispositionele attributie"),
                          ("hij viel omdat de vloer nat was", "externe of situationele attributie")],
                  "Welke attributie?", WL),
                 ("open", "Je bent zelf te laat en zegt: er was file. Een klasgenoot is te laat en je "
                          "denkt: die is ongeorganiseerd. Hoe heet dat, en wat gebeurt er precies?",
                  "Dat is de fundamentele attributiefout. Bij anderen leg je de oorzaak bij de "
                  "persoon, bij jezelf bij de situatie. Dezelfde gebeurtenis krijgt dus twee "
                  "verschillende verklaringen, al naargelang over wie het gaat.", 5),
             ]),
        dict(kop="Weiner en Dweck",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Dimensie van Weiner", "De vraag erachter"],
                  [["locus van controle", None],
                   ["stabiliteit", None],
                   ["controleerbaarheid", None]],
                  "ligt de oorzaak binnen of buiten de persoon?; blijft de oorzaak, of kan ze morgen "
                  "anders zijn?; kan iemand er zelf iets aan doen?", WL),
                 ("rij", [("ik ben niet goed in wiskunde, dat verandert toch nooit", "stabiliteit"),
                          ("ik had gewoon geluk met die vragen", "locus van controle"),
                          ("ik had kunnen leren, maar ik heb het niet gedaan", "controleerbaarheid")],
                  "Welke dimensie staat hier vooraan?", WW),
                 ("rij", [("dat kan ik niet, dat heb ik nooit gekund", "fixed mindset"),
                          ("dat kan ik nog niet, ik pak het anders aan", "growth mindset"),
                          ("een fout betekent dat ik het niet kan", "fixed mindset"),
                          ("een fout wijst me waar ik nog moet oefenen", "growth mindset")],
                  "Fixed of growth mindset?", WW),
                 ("open", "Welke attributie past bij een fixed mindset? Gebruik twee dimensies van "
                          "Weiner in je antwoord.",
                  "Een attributie die stabiel en oncontroleerbaar is. Wie denkt dat zijn kunnen "
                  "vastligt, ziet de oorzaak als iets blijvends en als iets waar hij zelf niets aan "
                  "kan doen. Dat is de brug tussen Dweck en Weiner.", 5),
                 ("waar", "Volgens Dweck heeft iemand in alle vakken dezelfde mindset.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-cognitieve-dissonantie-en-processen-in-een-groep-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Cognitieve dissonantie en processen in een groep",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Dissonantie verminderen",
             opdracht="Een man weet dat roken schadelijk is en rookt elke dag. Lees wat hij doet en "
                      "zeg welke van de drie manieren hij gebruikt.",
             oefeningen=[
                 ("rij", [("hij stopt met roken", "zijn gedrag veranderen"),
                          ("hij besluit dat het gevaar sterk overdreven wordt",
                           "zijn attitude veranderen"),
                          ("hij zegt: mijn opa rookte en werd negentig", "een cognitie toevoegen")],
                  "Welke manier?", WL),
                 ("kort", "Hoe heet het als je denken en je doen wél bij elkaar passen?",
                  "cognitieve consonantie", WW),
                 ("open", "Van de drie manieren is er één die mensen het minst vaak kiezen. Welke, en "
                          "waarom?",
                  "Je gedrag veranderen, want dat is meestal het moeilijkst. Het is makkelijker om je "
                  "houding aan te passen of er een gedachte bij te zetten die de spanning verzacht, "
                  "dan om echt te stoppen met wat je doet.", 4),
                 ("rij", [("wie voor een richting koos, vertelt wat er mis is met de andere",
                           "na het maken van een keuze"),
                          ("wie ja zei op een verzoek, vindt het achteraf redelijker",
                           "na het instemmen met een verzoek"),
                          ("wie veel moeite deed, vindt het achteraf waardevoller",
                           "na het leveren van inspanningen")],
                  "Welke situatie uit de fiche?", WL),
                 ("open", "Een klant twijfelt lang en koopt dan toch de duurste gsm. Daarna gaat hij "
                          "zelf argumenten zoeken waarom het de juiste keuze was. Leg uit wat er "
                          "gebeurt.",
                  "Er is cognitieve dissonantie na het maken van een keuze: hij gaf veel geld uit en "
                  "dat wringt met de twijfel die hij had. Door argumenten te zoeken voegt hij "
                  "cognities toe die de keuze goedmaken, en zo verdwijnt de spanning.", 5),
             ]),
        dict(kop="Tuckman",
             opdracht="Vul de Nederlandse en de Engelse naam in, in de juiste orde.",
             oefeningen=[
                 ("tabel", ["", "Nederlands", "Engels", "Wat er gebeurt"],
                  [["1", None, None, "de leden kennen elkaar nog niet"],
                   ["2", None, None, "er wordt uitgevochten wie welke plaats krijgt"],
                   ["3", None, None, "de groep maakt haar eigen afspraken"],
                   ["4", None, None, "de groep werkt vlot en haalt haar doelen"],
                   ["5", None, None, "de groep valt uiteen"]],
                  "oriëntatiefase forming; machtsfase storming; normeringsfase norming; "
                  "prestatiefase performing; afscheidsfase adjourning", W),
                 ("open", "Een leerkracht ziet in een nieuwe groep veel gekibbel en denkt dat het een "
                          "slechte groep is. Wat zou je haar zeggen, met Tuckman in de hand?",
                  "Dat de machtsfase of storming bij de ontwikkeling van een groep hoort en geen teken "
                  "is dat het een slechte groep is. Zonder dat botsen komen de afspraken van de "
                  "normeringsfase er niet. Eerst botsen, dan afspreken, dan presteren.", 5),
             ]),
        dict(kop="Wat een groep met een mens doet",
             opdracht="Zet bij elke situatie het juiste groepsproces.",
             oefeningen=[
                 ("rij", [("een gevorderde pianist speelt beter voor publiek", "sociale facilitatie"),
                          ("een beginner speelt slechter voor publiek", "sociale belemmering"),
                          ("in een groep van acht doet iemand minder omdat zijn aandeel niet opvalt",
                           "social loafing of sociaal parasiteren"),
                          ("de groep kiest een slecht plan om eensgezind te blijven", "groepsdenken")],
                  "Welk proces?", WL),
                 ("open", "Hetzelfde publiek maakt de ene beter en de andere slechter. Waar hangt dat "
                          "van af?",
                  "Van hoe goed de taak al zit. Bij een eenvoudige of goed ingeoefende taak werkt "
                  "publiek bevorderend: dat is sociale facilitatie. Bij een moeilijke of nieuwe taak "
                  "werkt het belemmerend: dat is sociale belemmering.", 4),
                 ("open", "Leg het verschil uit tussen social loafing en sociale belemmering.",
                  "Bij social loafing doe je minder omdat je in een groep werkt en je eigen bijdrage "
                  "niet opvalt: je levert minder inzet. Bij sociale belemmering doe je wel je best, "
                  "maar presteer je slechter door de druk van publiek. Het eerste is een kwestie van "
                  "inzet, het tweede van prestatie onder druk.", 5),
                 ("kort", "Hoe heten in de fiche de eigen groep en de andere groep?",
                  "de ingroup en de outgroup", WL),
                 ("kies", "Wat is een goede tegenzet tegen groepsdenken?",
                  ["iemand uitdrukkelijk de rol geven om tegen te spreken",
                   "de groep groter maken zodat er meer meningen zijn",
                   "pas beslissen als iedereen enthousiast is",
                   "de beslissing aan de leider alleen laten"], 0),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-sociale-beinvloeding-conformisme-inwilliging-en-gehoorzaamheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Drie niveaus van sociale druk",
             opdracht="Lees de situatie en zeg of het conformisme, inwilliging of gehoorzaamheid is. "
                      "Vraag je telkens af: vroeg iemand iets, en had die persoon gezag?",
             oefeningen=[
                 ("rij", [("niemand vraagt iets, maar je draagt wat de groep draagt", "conformisme"),
                          ("je vriend vraagt of je zijn verhuis komt helpen en je zegt ja",
                           "inwilliging"),
                          ("de directeur zegt dat de les buiten doorgaat en je gaat naar buiten",
                           "gehoorzaamheid"),
                          ("iedereen in de zaal staat op, dus jij ook", "conformisme")],
                  "Welk niveau?", WW),
                 ("rij", [("de politie vraagt je je identiteitskaart", "gehoorzaamheid"),
                          ("een verkoper vraagt of je een enquête wil invullen en je doet het",
                           "inwilliging"),
                          ("je zegt in de groep hetzelfde als iedereen om niet op te vallen",
                           "conformisme")],
                  "Welk niveau?", WW),
                 ("kort", "Welke drie vormen van weerstand bieden noemt de fiche?",
                  "onafhankelijkheid, assertiviteit en trotseren", WL),
                 ("open", "Leg in je eigen woorden uit hoe conformisme en inwilliging van elkaar "
                          "verschillen.",
                  "Bij conformisme vraagt niemand iets: je past je aan de groep aan omdat de groep er "
                  "is. Bij inwilliging is er wel een verzoek, en je zegt daarop ja. Het verschil zit "
                  "dus in de vraag die er wel of niet gesteld wordt.", 4),
             ]),
        dict(kop="Informatief of normatief",
             opdracht="Zeg of het informatief of normatief conformisme is, en waaraan je het ziet.",
             oefeningen=[
                 ("rij", [("je weet het niet en volgt de anderen, want zij zullen wel juist zijn",
                           "informatief"),
                          ("je weet het wel, maar zegt hetzelfde als de groep om erbij te horen",
                           "normatief"),
                          ("in een onduidelijke situatie schuiven de schattingen naar elkaar toe",
                           "informatief"),
                          ("in een duidelijke situatie ga je mee in een fout antwoord", "normatief")],
                  "Informatief of normatief?", WW),
                 ("open", "Bij welk van de twee verandert je overtuiging echt, en bij welk vaak alleen "
                          "je gedrag? Leg uit.",
                  "Bij informatief conformisme verandert je overtuiging echt: je gelooft dat de "
                  "anderen het beter weten en neemt hun antwoord over. Bij normatief conformisme "
                  "verandert vaak alleen je gedrag: je zegt in de groep hetzelfde en denkt alleen nog "
                  "het tegendeel.", 5),
             ]),
        dict(kop="Sherif, Asch, Darley en Latané",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["Onderzoek", "Was de situatie duidelijk?", "Welk conformisme?"],
                  [["Sherif, het lichtpuntje in de donkere kamer", None, None],
                   ["Asch, de lijnen van gelijke lengte", None, None]],
                  "bij Sherif onduidelijk, dus informatief conformisme; bij Asch duidelijk, dus "
                  "normatief conformisme", WW),
                 ("open", "Bewoog het lichtpuntje bij Sherif echt? Wat gebeurde er met de schattingen?",
                  "Nee, het puntje bewoog niet; het leek alleen zo. De schattingen van de deelnemers "
                  "schoven na een paar rondes in groep naar elkaar toe tot er één groepsnorm was, en "
                  "die hielden ze daarna ook alleen nog aan.", 5),
                 ("kort", "Hoe heet het effect van Darley en Latané?", "het omstandereffect", WW),
                 ("kies", "Wat voorspelt het omstandereffect?",
                  ["hoe meer omstaanders, hoe kleiner de kans dat iemand helpt",
                   "hoe meer omstaanders, hoe groter de kans dat iemand helpt",
                   "het aantal omstaanders maakt geen verschil",
                   "enkel bekenden van het slachtoffer helpen"], 0),
                 ("open", "Waarom werkt het om bij een ongeval één iemand aan te wijzen in plaats van "
                          "te roepen dat er iemand moet bellen?",
                  "Omdat de verantwoordelijkheid dan niet meer over de aanwezigen gespreid wordt. Wie "
                  "persoonlijk aangewezen is, kan niet meer denken dat een ander het wel doet, en dat "
                  "haalt het omstandereffect weg.", 5),
             ]),
        dict(kop="Vier beïnvloedingstechnieken",
             opdracht="Zet bij elk voorbeeld de techniek uit de fiche.",
             oefeningen=[
                 ("rij", [("eerst een enquête van één vraag, dan een gift gevraagd",
                           "voet-tussen-de-deur"),
                          ("eerst elke week helpen gevraagd, dan maar één zaterdag",
                           "deur-in-het-gezicht"),
                          ("een goedkope reis waar achteraf nog toeslagen op komen",
                           "zodra-de-bal-aan-het-rollen-is"),
                          ("en u krijgt er dit nog gratis bij", "dat-is-nog-niet-alles")],
                  "Welke techniek?", WL),
                 ("open", "Waarom werkt voet-tussen-de-deur volgens de theorie van de cognitieve "
                          "dissonantie?",
                  "Omdat wie één keer ja zei, zichzelf gaat zien als iemand die helpt. Nee zeggen op "
                  "het volgende verzoek past niet meer bij dat beeld, en dat zou spanning geven. Om "
                  "die spanning te vermijden zegt hij opnieuw ja.", 5),
                 ("open", "Deur-in-het-gezicht werkt om een andere reden. Welke?",
                  "Omdat het tweede verzoek klein lijkt naast het eerste. Door eerst iets overdreven "
                  "groot te vragen, komt het echte verzoek er heel redelijk uit.", 4),
             ]),
        dict(kop="Milgram en Zimbardo",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Wat onderzocht Milgram, en werd er iemand echt geschokt?",
                  "Milgram onderzocht gehoorzaamheid aan een gezagsfiguur. Er werd niemand echt "
                  "geschokt: de leerling in de andere kamer was een helper van de onderzoeker. Een "
                  "groot deel van de deelnemers ging toch door tot het hoogste niveau zolang de "
                  "onderzoeker zei dat ze moesten doorgaan.", 6),
                 ("kies", "Waarover gaat het Stanford gevangenisexperiment van Zimbardo in de eerste "
                          "plaats?",
                  ["over de kracht van de rol die iemand krijgt",
                   "over een bevel van een gezagsfiguur",
                   "over de druk van een groep in een onduidelijke situatie",
                   "over het omstandereffect bij een noodgeval"], 0),
                 ("waar", "Het onderzoek van Zimbardo liep volledig af zoals gepland.", False),
                 ("open", "Beide onderzoeken zijn ethisch zwaar bekritiseerd. Waarom, en wat betekent "
                          "dat voor onderzoek vandaag?",
                  "Omdat de deelnemers niet wisten waar ze aan begonnen en er niet onbeschadigd "
                  "uitkwamen. Daarom mag een onderzoek vandaag niet meer zo gebeuren: deelnemers "
                  "moeten vooraf weten waarvoor ze toestemmen en mogen er geen schade van "
                  "overhouden.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-persoonlijkheid-wat-ze-is-en-hoe-een-brein-reageert-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: wat ze is en hoe een brein reageert",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vijf elementen",
             opdracht="Zet bij elk gegeven het element van persoonlijkheid dat de fiche noemt.",
             oefeningen=[
                 ("rij", [("zij reageert van kleins af heel snel en heel sterk", "temperament"),
                          ("hij wil later iets doen waarmee hij mensen helpt", "motivatie"),
                          ("zij vindt van zichzelf dat ze niet creatief is", "zelfbeeld"),
                          ("hij is geneigd behulpzaam te zijn, in alle situaties",
                           "trekken of disposities")],
                  "Welk element?", WL),
                 ("open", "Leg het verschil uit tussen temperament en karakter.",
                  "Temperament is de aangeboren kant: hoe snel en hoe sterk iemand reageert, en dat "
                  "verandert weinig. Karakter is wat daar met de jaren bij groeit, onder invloed van "
                  "opvoeding en ervaring.", 4),
                 ("open", "Iemand met de trek vriendelijkheid is niet élk moment vriendelijk. Waarom "
                          "klopt dat met wat een trek is?",
                  "Omdat een trek geen gedrag is maar een neiging tot gedrag. Ze zegt wat iemand over "
                  "situaties heen geneigd is te doen, niet wat hij op elk moment doet.", 4),
                 ("kort", "Wat betekent het woord dispositie?", "geneigdheid", WW),
             ]),
        dict(kop="Cultuur",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Wat vergelijkt cross-cultureel onderzoek, en wat is de grote lijn van de "
                          "uitkomst?",
                  "Het vergelijkt dezelfde vragenlijst in verschillende landen. De grote lijn: de "
                  "trekken zelf worden in heel veel culturen teruggevonden, maar hoe hoog men "
                  "gemiddeld scoort en welke trek als een deugd geldt, verschilt.", 5),
                 ("tabel", ["Cultuur", "Wat vooraan staat"],
                  [["individualistische cultuur", None],
                   ["collectivistische cultuur", None]],
                  "het eigen doel en de eigen prestatie; de groep, de familie en de harmonie", WL),
                 ("open", "Dezelfde assertiviteit kan op de ene plaats een sterkte zijn en op de "
                          "andere onhoffelijk. Leg uit waarom.",
                  "Omdat cultuur mee bepaalt welke eigenschappen gewaardeerd worden. In een "
                  "individualistische cultuur past het om voor je eigen mening op te komen; in een "
                  "collectivistische cultuur kan datzelfde gedrag de harmonie van de groep storen.",
                  5),
                 ("waar", "Volgens de fiche vervangt cultuur de biologische kant van persoonlijkheid.",
                  False),
             ]),
        dict(kop="Gray: BIS en BAS",
             opdracht="Zet bij elk voorbeeld het systeem dat aan het werk is.",
             oefeningen=[
                 ("rij", [("hij ziet eerst wat er fout kan gaan", "BIS"),
                          ("zij gaat recht op de beloning af", "BAS"),
                          ("hij is erg gevoelig voor straf", "BIS"),
                          ("zij neemt makkelijk een risico", "BAS")],
                  "BIS of BAS?", W),
                 ("tabel", ["Systeem", "Voluit", "Waarop het reageert", "Wat het doet"],
                  [["BIS", None, None, None],
                   ["BAS", None, None, None]],
                  "Behavioral Inhibition System, op straf, gevaar en iets nieuws, het remt het gedrag "
                  "af; Behavioral Activation System, op beloning en op iets dat lokt, het zet het "
                  "gedrag aan", WW),
                 ("open", "Kan iemand beide systemen sterk hebben? Wat betekent dat dan?",
                  "Ja, de twee zijn geen tegenpolen op één lijn. Wie beide sterk heeft, wil er "
                  "tegelijk naartoe en deinst ervoor terug: hij wordt aangetrokken door de beloning en "
                  "voelt tegelijk de rem van het gevaar.", 5),
                 ("kort", "Hoe heet de theorie van Gray in de fiche?",
                  "de reinforcement sensitivity theory", WL),
             ]),
        dict(kop="Eysenck: arousal",
             opdracht="Antwoord kort en vul aan.",
             oefeningen=[
                 ("kort", "Wat betekent arousal?", "het prikkelingsniveau van de hersenen", WL),
                 ("tabel", ["", "Arousal in rust", "Wat iemand opzoekt"],
                  [["introvert", None, None],
                   ["extravert", None, None]],
                  "bij een introvert staat de arousal in rust al hoog, dus zoekt hij rust, een kleine "
                  "groep, een stille kamer; bij een extravert staat ze laag, dus zoekt hij drukte, "
                  "gezelschap en iets spannends", WW),
                 ("open", "De uitleg van Eysenck is omgekeerd aan wat je zou verwachten. Leg uit "
                          "waarom een extravert volgens hem drukte opzoekt.",
                  "Niet omdat hij graag onder mensen komt, maar omdat zijn brein in rust te weinig "
                  "geprikkeld is. Hij heeft meer prikkels nodig om op een aangenaam middenniveau te "
                  "komen, en die zoekt hij in drukte en gezelschap.", 5),
                 ("open", "Waarom is dezelfde drukke zaal voor de ene fijn en voor de andere slopend?",
                  "Omdat de zaal even luid is maar het brein anders staat. Bij een introvert staat de "
                  "arousal al hoog, dus komen de prikkels snel te veel aan; bij een extravert staat ze "
                  "laag, dus voelt het net goed.", 5),
                 ("waar", "Eysenck komt in dit vak twee keer voor: hier met de arousal en bij de "
                          "trekken met zijn PEN-model.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-persoonlijkheid-van-freud-over-bandura-naar-rogers-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: van Freud over Bandura naar Rogers",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Freud: niveaus en instanties",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("rij", [("waar je nu aan denkt", "het bewuste"),
                          ("je eigen adres, dat je kan ophalen", "het onder- of voorbewuste"),
                          ("wat weggedrukt is en toch meespeelt", "het onbewuste")],
                  "Welk bewustzijnsniveau?", WL),
                 ("kort", "Hoe heet het mechanisme waarmee iets in het onbewuste terechtkomt?",
                  "verdringing", WW),
                 ("open", "Waarom is voorbewust niet hetzelfde als onbewust?",
                  "Wat voorbewust is, kan je ophalen als je het zoekt; het is alleen niet waar je nu "
                  "aan denkt. Wat onbewust is, kan je niet rechtstreeks bereiken, en het werkt toch "
                  "mee in dromen, verspreken en symptomen.", 4),
                 ("tabel", ["Deel", "Andere naam", "Principe", "Wat het wil"],
                  [["het Es", None, None, None],
                   ["het Ich", None, None, None],
                   ["het Über-ich", None, None, None]],
                  "het Id, lustprincipe, nu en volledig; het Ego, realiteitsprincipe, wat haalbaar is "
                  "in de echte wereld; het Superego, moraliteitsprincipe, wat hoort", W),
                 ("rij", [("een stem die zegt: dat hoort niet", "het Über-ich"),
                          ("een stem die zegt: dit kan nu niet, straks wel", "het Ich"),
                          ("een stem die zegt: ik wil het nu", "het Es")],
                  "Welk deel spreekt?", WW),
                 ("kort", "Welke twee driften zitten volgens Freud in het Es?",
                  "de eros of levensdrift en de thanatos of doodsdrift", WL),
             ]),
        dict(kop="Bandura en Rotter",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Welke drie factoren beïnvloeden elkaar in het wederzijds determinisme?",
                  "cognities en eigenschappen, de omgeving en het gedrag", WL),
                 ("open", "Waarom is het woord wederzijds hier zo belangrijk? Geef een voorbeeld.",
                  "Omdat het niet in één richting gaat. Wie denkt dat hij slecht is in wiskunde steekt "
                  "zijn hand niet meer op, en doordat hij niets meer vraagt gaat het inderdaad "
                  "slechter, waardoor hij nog sterker gaat denken dat hij het niet kan. Gedrag, "
                  "omgeving en denken trekken aan elkaar.", 6),
                 ("open", "Iemand heeft een hoge zelfeffectiviteit voor zwemmen en een lage voor "
                          "spreken voor een groep. Wat zegt dat over het begrip?",
                  "Dat zelfeffectiviteit taakgebonden is: het is het geloof dat je een bepaalde taak "
                  "kan, en dat kan per taak verschillen. Het is dus iets anders dan zelfbeeld of "
                  "zelfwaarde, die over de persoon in zijn geheel gaan.", 5),
                 ("rij", [("wat mij overkomt, hangt grotendeels van mij af",
                           "interne locus of control"),
                          ("wat mij overkomt, hangt van geluk of van anderen af",
                           "externe locus of control")],
                  "Welke locus of control?", WL),
                 ("open", "Bij Weiner en bij Rotter komt de locus van controle voor. Wat is het "
                          "verschil?",
                  "Bij Weiner is het een dimensie van één attributie, voor dat ene geval: waar legt "
                  "iemand de oorzaak van dít voorval. Bij Rotter is het een vaste eigenschap van een "
                  "persoon, die je bij hem overal terugziet.", 5),
             ]),
        dict(kop="Maslow en Rogers",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe noemen Maslow en Rogers beide het worden wie je ten volle kan zijn?",
                  "zelfactualisatie", WW),
                 ("tabel", ["Begrip van Rogers", "Wat het is"],
                  [["het fenomenale veld", None],
                   ["het actuele zelf", None],
                   ["het ideale zelf", None],
                   ["congruentie", None],
                   ["incongruentie", None]],
                  "de wereld zoals die persoon ze zelf beleeft; wie iemand vindt dat hij nu is; "
                  "wie iemand zou willen zijn; die twee liggen dicht bij elkaar, dat geeft rust; "
                  "die twee liggen ver uit elkaar, dat geeft spanning", WL),
                 ("open", "Betekent congruentie dat het ideale zelf verdwijnt? Leg uit.",
                  "Nee. Het betekent dat de afstand tussen het actuele en het ideale zelf klein genoeg "
                  "is om ermee te leven. Een doel hebben hoort bij groeien; de spanning komt van een "
                  "beeld dat onbereikbaar ver ligt.", 4),
                 ("open", "Twee kinderen zaten in dezelfde klas en hebben een heel andere dag gehad. "
                          "Welk begrip van Rogers legt dat uit?",
                  "Het fenomenale veld: wat telt is niet de klas zoals een camera ze ziet, maar de "
                  "klas zoals elk van de twee ze beleefde.", 4),
                 ("kort", "Hoe heet de therapievorm van Rogers in de fiche?",
                  "client-centered therapy", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-persoonlijkheid-trekken-de-big-five-en-hexaco-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: trekken, de big five en HEXACO",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Allport",
             opdracht="Zet bij elk voorbeeld de soort trek.",
             oefeningen=[
                 ("rij", [("behulpzaam, ordelijk en nieuwsgierig", "centrale trekken"),
                          ("zenuwachtig worden van spreken voor een groep", "secundaire trek"),
                          ("een eigenschap die zowat het hele leven van iemand beheerst",
                           "cardinale trek")],
                  "Welke soort trek?", WW),
                 ("waar", "Volgens Allport heeft iedereen een cardinale trek.", False),
                 ("open", "Waarmee beschrijf je volgens Allport de meeste mensen, en waarom niet met "
                          "een cardinale trek?",
                  "Met hun centrale trekken: een handvol eigenschappen waarmee je iemand beschrijft. "
                  "Een cardinale trek is uitzonderlijk, want die beheerst zowat het hele leven van "
                  "iemand, en de meeste mensen hebben er geen.", 4),
             ]),
        dict(kop="PEN, Big Five en HEXACO",
             opdracht="Vul de modellen aan.",
             oefeningen=[
                 ("tabel", ["Letter", "Dimensie van Eysenck", "Hoog betekent"],
                  [["P", None, None],
                   ["E", None, None],
                   ["N", None, None]],
                  "psychoticisme, weinig geremd en op risico uit; extraversie, naar buiten gericht; "
                  "neuroticisme, snel en sterk reageren op spanning", WW),
                 ("tabel", ["De vijf factoren van Costa en McCrae", "Hoog betekent"],
                  [[None, None], [None, None], [None, None], [None, None], [None, None]],
                  "openheid voor ervaringen, nieuwsgierig en open voor ideeën; zorgvuldigheid, "
                  "ordelijk en plannend; extraversie, gezelschap opzoekend; vriendelijkheid, meegaand "
                  "en behulpzaam; emotionele stabiliteit versus neuroticisme, rustig blijven onder "
                  "spanning", WL),
                 ("open", "De vijfde factor heet emotionele stabiliteit versus neuroticisme. Waarom "
                          "blijft de Big Five dan vijf en niet zes?",
                  "Omdat het één lijn is met twee uiteinden: hoog is emotionele stabiliteit, laag is "
                  "neuroticisme. Het zijn geen twee aparte factoren, maar twee kanten van dezelfde "
                  "factor.", 4),
                 ("kort", "Wat is het verschil tussen de Big Five en HEXACO?",
                  "HEXACO heeft de integriteit erbij", WL),
                 ("kort", "Hoe heet de integriteit in het Engels?", "honesty-humility", WW),
                 ("open", "Waarom is die zesde factor erbij gekomen? Gebruik vriendelijkheid in je "
                          "antwoord.",
                  "Omdat hij gedrag voorspelt dat de vijf andere niet goed dekken, zoals bedrog en "
                  "misbruik maken van een ander. Iemand kan vriendelijk overkomen en toch laag op "
                  "integriteit scoren, en dat verschil zie je met de Big Five niet.", 5),
                 ("open", "Waar staan de zes letters van HEXACO voor in het Engels?",
                  "Honesty-humility, Emotionality, eXtraversion, Agreeableness, Conscientiousness en "
                  "Openness.", 4),
             ]),
        dict(kop="Door elkaar",
             opdracht="Zet bij elk gegeven het model waar het thuishoort.",
             oefeningen=[
                 ("rij", [("cardinale, centrale en secundaire trekken", "Allport"),
                          ("psychoticisme, extraversie, neuroticisme", "Eysenck, PEN"),
                          ("vijf factoren met emotionele stabiliteit als vijfde",
                           "Costa en McCrae, Big Five"),
                          ("zes factoren met de integriteit erbij", "Lee en Ashton, HEXACO")],
                  "Welk model?", WL),
                 ("open", "Waarom zijn vijf factoren genoeg voor een beschrijving waar Allport nog "
                          "honderden woorden voor nodig had?",
                  "Omdat een factor breder is dan een trek: hij bundelt een reeks trekken die in "
                  "onderzoek samen bewegen. Honderden losse woorden vallen daarmee in een klein aantal "
                  "groepen uiteen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-opvoeden-milieus-dimensies-stijlen-en-middelen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Opvoeden: milieus, dimensies, stijlen en middelen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Actoren en milieus",
             opdracht="Zet bij elk voorbeeld het opvoedingsmilieu.",
             oefeningen=[
                 ("rij", [("de grootouders waar het kind elke woensdag is", "primair milieu"),
                          ("de jeugdbeweging op zaterdag", "secundair milieu"),
                          ("de reclame tussen twee video's", "tertiair milieu"),
                          ("de muziekacademie", "secundair milieu")],
                  "Welk milieu?", WW),
                 ("open", "Wat onderscheidt een secundair van een tertiair milieu? Geef van elk een "
                          "voorbeeld.",
                  "In een secundair milieu gaat het kind ergens naartoe en is er iemand die opvoedt, "
                  "zoals een school of een club. Een tertiair milieu komt naar het kind toe en niemand "
                  "bedoelde het als opvoeding, zoals sociale media of reclame.", 5),
                 ("open", "De fiche zet het kind zelf bij de actoren. Waarom is dat geen detail?",
                  "Omdat het kind de opvoeding niet alleen ondergaat maar ze mee stuurt. Een kind dat "
                  "heftig reageert, krijgt een andere opvoeder tegenover zich dan een kind dat alles "
                  "laat gebeuren. Opvoeden gaat dus in twee richtingen.", 5),
             ]),
        dict(kop="De drie dimensies",
             opdracht="Zeg bij elke uitspraak welke dimensie je ziet.",
             oefeningen=[
                 ("rij", [("om tien uur ben je thuis", "gedragsmatige controle"),
                          ("als je nu gaat, doe je mij verdriet", "psychologische controle"),
                          ("vertel eens hoe dat voor jou was", "responsiviteit"),
                          ("ik wil weten waar je bent en met wie", "gedragsmatige controle")],
                  "Welke dimensie?", WL),
                 ("rij", [("ik zie dat je verdriet hebt, kom eens zitten", "responsiviteit"),
                          ("ik praat niet meer met je tot je het toegeeft",
                           "psychologische controle"),
                          ("deze regel geldt in dit huis", "gedragsmatige controle")],
                  "Welke dimensie?", WL),
                 ("open", "Beide soorten controle heten controle, en toch is er één meestal gunstig en "
                          "één meestal schadelijk. Leg uit.",
                  "Gedragsmatige controle stuurt wat een kind doet, met regels en toezicht, en is in "
                  "onderzoek meestal gunstig: een kind weet waar het aan toe is. Psychologische "
                  "controle stuurt wat een kind denkt en voelt, met schuldgevoel of met het intrekken "
                  "van liefde, en is meestal schadelijk, want ze raakt het kind in zijn eigenwaarde.",
                  6),
             ]),
        dict(kop="De vier stijlen",
             opdracht="Vul de tabel aan met hoog of laag, en zeg daarna welke stijl bij de uitspraak "
                      "hoort.",
             oefeningen=[
                 ("tabel", ["Stijl", "Responsiviteit", "Controle"],
                  [["autoritair", None, None],
                   ["democratisch-autoritatief", None, None],
                   ["permissief of toegeeflijk", None, None],
                   ["onverschillig of laissez-faire", None, None]],
                  "laag en hoog; hoog en hoog; hoog en laag; laag en laag", W),
                 ("rij", [("omdat ik het zeg", "autoritair"),
                          ("dit is de regel, en dit is waarom", "democratisch-autoritatief"),
                          ("doe maar wat je wil, ik ben er voor je", "permissief of toegeeflijk"),
                          ("zoek het zelf uit", "onverschillig of laissez-faire")],
                  "Welke stijl?", WL),
                 ("open", "Autoritair en autoritatief lijken op elkaar en zijn bijna tegengesteld. "
                          "Leg uit waarin.",
                  "Autoritair is streng zonder warmte: veel controle en weinig responsiviteit. "
                  "Autoritatief is streng met warmte en met uitleg: veel controle én veel "
                  "responsiviteit. Die tweede stijl pakt in onderzoek het best uit.", 5),
                 ("open", "Wat onderscheidt een permissieve van een onverschillige opvoeder?",
                  "De warmte. Een permissieve opvoeder is er wel voor het kind maar legt niets op; een "
                  "onverschillige opvoeder is er niet en legt ook niets op.", 4),
                 ("waar", "Volgens de fiche is een opvoedingsstijl een combinatie van "
                          "opvoedingsdimensies.", True),
             ]),
        dict(kop="De negen middelen",
             opdracht="Zet bij elk voorbeeld het opvoedingsmiddel uit de lijst.",
             oefeningen=[
                 ("rij", [("je zet zelf je gsm weg aan tafel", "voorbeeldgedrag of modelleren"),
                          ("elke avond tanden poetsen op hetzelfde moment", "gewoontevorming"),
                          ("je zegt waarom je geen suiker in de fles doet", "informatieoverdracht"),
                          ("een stickerkaart voor wie zijn kamer opruimt", "belonen")],
                  "Welk middel?", WL),
                 ("rij", [("je wijst naar de eendjes als de peuter begint te krijsen", "afleiden"),
                          ("vijf minuten op de stoel bij het hoekje", "negeren en time-out"),
                          ("je zegt: probeer het nog een keer, je bent er bijna",
                           "aanmoedigen of stimuleren"),
                          ("je zegt: in dit huis slaan we niet", "regels en grenzen stellen")],
                  "Welk middel?", WL),
                 ("open", "Twee van de negen middelen komen rechtstreeks uit de leertheorieën. Welke, "
                          "en uit welke theorie?",
                  "Belonen en straffen komen uit de operante conditionering van Skinner: gedrag wordt "
                  "gestuurd door het gevolg. Voorbeeldgedrag komt uit het observerend leren van "
                  "Bandura: een kind leert door te kijken naar wat een ander doet.", 5),
                 ("open", "Waarom staat afleiden in de lijst, al lijkt het niet veel op opvoeden?",
                  "Omdat het bij een jong kind vaak het meest werkzame middel van de negen is: "
                  "uitleggen komt bij een peuter nog niet aan, en de aandacht naar iets anders "
                  "brengen werkt wel.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-pedagogische-modellen-en-opvoeden-in-bijzondere-contexten-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Pedagogische modellen en opvoeden in bijzondere contexten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Visies",
             opdracht="Zet bij elke kern de visie uit de fiche.",
             oefeningen=[
                 ("rij", [("opvoeden tot deugd en tot de juiste verhouding tot anderen",
                           "de leer van Confucius"),
                          ("de rede vormen, van de schijn naar het inzicht", "de leer van Plato"),
                          ("kennis en geloof samen, en het karakter van het kind vormen",
                           "Al-Ghazali"),
                          ("het kind is geen kleine volwassene; volg zijn natuurlijke ontwikkeling",
                           "Rousseau")],
                  "Welke visie?", WL),
                 ("rij", [("opvoeden vanuit de basisbehoeften: verbonden zijn, iets kunnen, zelf "
                           "kiezen", "behoefteondersteunende opvoeding"),
                          ("gezag zonder machtsstrijd, met steun van anderen rond het kind",
                           "nieuwe autoriteit")],
                  "Welke hedendaagse visie?", WL),
                 ("open", "Nieuwe autoriteit is geen zachtere autoriteit. Leg uit waarin ze dan "
                          "verschilt van de autoritaire stijl.",
                  "De opvoeder geeft niet toe, maar hij verzet zich zonder het gevecht aan te gaan en "
                  "hij staat er niet alleen: hij zoekt steun bij anderen rond het kind. De autoritaire "
                  "stijl verwacht het van macht, en gaat de machtsstrijd dus juist wel aan.", 5),
             ]),
        dict(kop="Risico en bescherming",
             opdracht="Zet bij elk gegeven het niveau, en zeg of het een risicofactor of een "
                      "beschermende factor is.",
             oefeningen=[
                 ("rij", [("veel ruzie thuis", "micro, risicofactor"),
                          ("een leerkracht die het ziet", "meso, beschermende factor"),
                          ("armoede in de samenleving", "macro, risicofactor"),
                          ("een warme band met één ouder", "micro, beschermende factor")],
                  "Welk niveau, en welke soort?", WL),
                 ("rij", [("gepest worden op school", "meso, risicofactor"),
                          ("een toelage waar het gezin recht op heeft", "macro, beschermende factor"),
                          ("een lange wachtlijst voor hulp", "macro, risicofactor")],
                  "Welk niveau, en welke soort?", WL),
                 ("open", "Waarom is een risicofactor geen voorspelling?",
                  "Omdat het over kansen gaat en niet over wat er met dít kind zal gebeuren. Daarom "
                  "staat de beschermende factor er altijd naast: één stevige band of één goede "
                  "leerkracht kan veel risico opvangen.", 4),
             ]),
        dict(kop="Twee pedagogische modellen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het model van Bronfenbrenner, en uit hoeveel systemen bestaat het?",
                  "het bio-ecologisch model, vijf systemen", WL),
                 ("tabel", ["Kant van het balansmodel", "Wat erin zit"],
                  [["draaglast", None],
                   ["draagkracht", None]],
                  "alles wat weegt: ziekte, geldzorgen, een kind dat veel vraagt; alles wat je kan "
                  "dragen: gezondheid, een partner, familie die bijspringt, ervaring", WL),
                 ("open", "Twee gezinnen hebben precies dezelfde zorg en staan er heel anders in. Hoe "
                          "legt het balansmodel dat uit?",
                  "Het gaat niet om de last alleen maar om de verhouding tussen draaglast en "
                  "draagkracht. Het gezin met meer draagkracht, bijvoorbeeld familie die bijspringt, "
                  "houdt dezelfde last beter vol.", 5),
                 ("open", "Welke twee manieren om een opvoedingssituatie te verbeteren volgen uit het "
                          "balansmodel? Welke van de twee kan vaak alleen?",
                  "De last verlichten of de kracht versterken. Vaak is het tweede het enige dat kan, "
                  "want een ziekte of een beperking gaat niet weg; wél kan er hulp, ontlasting of "
                  "steun bij komen.", 5),
                 ("kort", "Van wie is het balansmodel?", "van Bakker en anderen", WW),
             ]),
        dict(kop="Bijzondere contexten",
             opdracht="Zet bij elk gegeven de context of de soort.",
             oefeningen=[
                 ("rij", [("dyslexie en dyscalculie", "leerstoornissen"),
                          ("ADHD en ASS", "ontwikkelingsstoornissen"),
                          ("slechtziend of slechthorend zijn", "zintuiglijke handicap"),
                          ("een combinatie van verschillende beperkingen", "meervoudige handicap")],
                  "Welke context of soort?", WL),
                 ("open", "Wat onderscheidt een leerstoornis van een ontwikkelingsstoornis?",
                  "Een leerstoornis zit op één schools domein: lezen bij dyslexie, rekenen bij "
                  "dyscalculie. Een ontwikkelingsstoornis raakt het functioneren veel breder, niet "
                  "alleen op school.", 4),
                 ("kort", "Waarvoor staat de afkorting VOS?",
                  "verontrustende opvoedingssituatie", WL),
                 ("open", "Waarom is kansarmoede ruimer dan weinig geld hebben?",
                  "Omdat ze over achterstand op meerdere terreinen tegelijk gaat: wonen, gezondheid, "
                  "werk en onderwijs. Die terreinen houden elkaar vast, en daardoor is kansarmoede "
                  "moeilijker te doorbreken dan een laag inkomen alleen.", 5),
             ]),
        dict(kop="Orthopedagogische modellen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent ortho in orthopedagogiek?", "recht of juist", WW),
                 ("tabel", ["Veld bij Schalock en Verdugo", "Waarover het gaat"],
                  [["onafhankelijkheid", None],
                   ["sociale participatie", None],
                   ["welbevinden", None]],
                  "zelf kunnen beslissen en zelf dingen doen; erbij horen, meedoen, relaties hebben; "
                  "zich goed voelen, lichamelijk en emotioneel", WL),
                 ("kort", "Waarvoor staan de vier letters van het model van Rink?",
                  "kind, opvoeder, scene of situatie, structuur", WL),
                 ("open", "Beide orthopedagogische modellen kijken naast de beperking. Waarom is dat "
                          "de kern van de orthopedagogiek?",
                  "Omdat een diagnose zegt wat iemand moeilijk heeft, en nog niets over wat zijn leven "
                  "goed maakt. De modellen vragen daarom niet wat er mankeert, maar hoe goed iemand "
                  "kan beslissen, meedoen en zich voelen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-communicatieve-vaardigheden-kaders-en-gesprekstechnieken-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Communicatieve vaardigheden: kaders en gesprekstechnieken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De empathische basishouding",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel onderdelen noemt de fiche bij de empathische basishouding?",
                  "zes", W),
                 ("rij", [("echt volgen wat de ander zegt en dat laten merken", "actief luisteren"),
                          ("niet meteen oordelen of een oplossing klaar hebben", "open houding"),
                          ("jezelf blijven en geen rol spelen", "echtheid"),
                          ("er zijn als er emotie komt", "emotionele beschikbaarheid")],
                  "Welk onderdeel?", WL),
                 ("rij", [("dat moet lastig zijn voor jou", "empathie"),
                          ("ach, arme jij", "medelijden")],
                  "Empathie of medelijden?", WW),
                 ("open", "Waarom is empathie niet hetzelfde als medelijden?",
                  "Bij empathie begrijp je hoe het voor de ander is; je hoeft het niet eens te zijn en "
                  "je zakt er zelf niet in weg. Bij medelijden kijk je op de ander neer of neem je zijn "
                  "verdriet over, en dan help je hem niet verder.", 5),
             ]),
        dict(kop="De vier stappen",
             opdracht="Een huisgenoot laat de afwas staan. Zet de vier stappen van verbindend "
                      "communiceren in de juiste orde en vul ze in.",
             oefeningen=[
                 ("tabel", ["Stap", "De vraag erachter", "Jouw zin"],
                  [["waarneming", None, None],
                   ["gevoel", None, None],
                   ["behoefte", None, None],
                   ["verzoek", None, None]],
                  "wat zie of hoor ik zonder oordeel: de afwas van drie dagen staat er nog; "
                  "wat voel ik: ik word daar moedeloos van; wat heb ik nodig: ik heb nodig dat we dat "
                  "samen dragen; wat vraag ik concreet: wil jij vanavond afwassen?", WW),
                 ("rij", [("de afwas staat er nog", "een waarneming"),
                          ("jij laat altijd alles staan", "een oordeel"),
                          ("er liggen vier handdoeken op de grond", "een waarneming"),
                          ("jij bent gewoon slordig", "een oordeel")],
                  "Een waarneming of een oordeel?", WW),
                 ("open", "Waarom is de eerste stap de moeilijkste?",
                  "Omdat een waarneming alleen mag zeggen wat een camera zou zien. De meeste mensen "
                  "zetten er meteen een oordeel in, zoals altijd of nooit, en daar begint de ruzie.",
                  4),
                 ("kort", "Welke vijf kenmerken geeft de fiche aan geweldloze communicatie?",
                  "direct, doeltreffend, emotioneel, empathisch en respectvol", WL),
                 ("waar", "Geweldloos betekent volgens die vijf kenmerken dat je het vaag en "
                          "voorzichtig zegt.", False),
             ]),
        dict(kop="De drie kaders",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("verbindend communiceren", "Marshall B. Rosenberg"),
                          ("de geen-verliesmethode", "Thomas Gordon")],
                  "Van wie?", WL),
                 ("open", "De geen-verliesmethode zoekt geen compromis. Wat zoekt ze dan, en wat moet "
                          "daarvoor eerst op tafel komen?",
                  "Ze zoekt een oplossing waarin beiden hun behoefte terugvinden, in plaats van een "
                  "oplossing waarin beiden iets opgeven. Daarvoor moet eerst op tafel komen wat elk "
                  "van de twee écht nodig heeft, en dat is zelden hetzelfde als wat elk van de twee "
                  "eist.", 5),
             ]),
        dict(kop="De LSD-methode",
             opdracht="Zet bij elke reactie de techniek.",
             oefeningen=[
                 ("rij", [("je zegt: het loopt niet", "papegaaien"),
                          ("dus het lukt op dit moment niet", "parafraseren"),
                          ("ik hoor dat je er moedeloos van wordt", "reflecteren"),
                          ("en wat deed je daarna?", "doorvragen")],
                  "Welke techniek?", WW),
                 ("open", "Wat onderscheidt reflecteren van parafraseren? Noem het kenmerk waaraan je "
                          "het ziet.",
                  "Reflecteren geeft het gevoel eronder terug, parafraseren de inhoud in je eigen "
                  "woorden. Je ziet het aan de woorden: in een reflectie staat een gevoelswoord, in "
                  "een parafrase niet.", 4),
                 ("rij", [("hoe is dat voor jou?", "open vraag"),
                          ("heb je het al gezegd?", "gesloten vraag"),
                          ("wat gebeurde er toen?", "open vraag"),
                          ("ben je daar boos om?", "gesloten vraag")],
                  "Open of gesloten vraag?", WW),
                 ("open", "Waarom staan de open vragen vooraan in een gesprek met een empathische "
                          "basishouding?",
                  "Omdat een gesloten vraag één woord oplevert en het gesprek stillegt. Een open vraag "
                  "laat de ander vertellen, en dan pas kan je volgen wat er echt speelt.", 4),
                 ("kort", "Welke twee soorten luisteren noemt de fiche?",
                  "non-verbaal en verbaal", WW),
             ]),
        dict(kop="Ik-boodschap en 4G",
             opdracht="Antwoord kort en schrijf zelf.",
             oefeningen=[
                 ("tabel", ["Een ik-boodschap", "Het 4G-model"],
                  [[None, None], [None, None], [None, None], [None, None]],
                  "ik-boodschap: het gedrag, het gevolg, het gevoel, een alternatief; "
                  "4G-model: gedrag, gevoel, gevolg, gewenst gedrag", WW),
                 ("open", "Waarom helpt het niet om de orde van die twee schema's van buiten te leren?",
                  "Omdat de fiche gevoel en gevolg in een verschillende orde zet. Wat je wél moet "
                  "kennen, is uit welke delen elk van de twee bestaat.", 4),
                 ("rij", [("jij luistert nooit", "een jij-boodschap"),
                          ("ik merk dat ik twee keer moet vragen", "een ik-boodschap")],
                  "Ik- of jij-boodschap?", WW),
                 ("open", "Schrijf zelf een ik-boodschap voor deze situatie: je groepsgenoot levert "
                          "zijn deel van de taak twee dagen te laat. Zet alle vier de onderdelen erin "
                          "en zet erbij welk onderdeel het is.",
                  "Een goed antwoord heeft alle vier de onderdelen, bijvoorbeeld: jouw deel kwam twee "
                  "dagen na de afspraak toe (gedrag), daardoor kon ik het geheel niet meer nalezen "
                  "(gevolg), en ik werd daar ongerust van (gevoel); kan je het volgende deel op de "
                  "afgesproken dag doorsturen (alternatief)?", 7),
                 ("open", "Zet de ik-boodschap, het 4G-model en de vier stappen van Rosenberg naast "
                          "elkaar. Welk patroon zie je drie keer terug?",
                  "Eerst het feit, dan wat het met je doet, dan de vraag. Alle drie beginnen bij wat "
                  "er gebeurde zonder oordeel, zeggen daarna wat dat bij jou doet, en eindigen met wat "
                  "je liever ziet.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-socialisatie-posities-rollen-en-vier-visies-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Socialisatie: posities, rollen en vier visies",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier begrippen",
             opdracht="Zet bij elk gegeven het sociologische begrip.",
             oefeningen=[
                 ("rij", [("leerling, moeder, trainer", "sociale positie"),
                          ("van een leerling verwacht men dat hij op tijd komt", "sociale rol"),
                          ("een arts geniet veel aanzien", "sociale status"),
                          ("een directeur die een beslissing neemt", "macht")],
                  "Welk begrip?", WW),
                 ("open", "Leg het verschil uit tussen een sociale positie en een sociale rol. Gebruik "
                          "de woorden hebben en spelen.",
                  "Een positie is de plaats die je in een geheel inneemt: die heb je. Een rol is wat "
                  "er bij die positie van je verwacht wordt: die speel je. Eén persoon heeft "
                  "verschillende posities tegelijk, en bij elke hoort een eigen rol.", 5),
                 ("open", "Een leerkracht is ook de mama van een leerling in haar eigen klas. Hoe heet "
                          "dat, en wat is het probleem?",
                  "Dat is een rolconflict: wat de ene positie van haar vraagt, botst met wat de andere "
                  "vraagt. Als leerkracht moet ze alle leerlingen gelijk behandelen, als mama wil ze "
                  "haar kind beschermen, en die twee gaan niet samen.", 5),
                 ("open", "Gaan status en macht altijd samen? Geef een voorbeeld.",
                  "Nee. Een geliefde leraar heeft veel status maar beslist niet over het budget; wie "
                  "over het budget beslist, heeft macht en soms weinig aanzien. Status gaat over "
                  "aanzien, macht over kunnen bepalen wat anderen doen.", 5),
             ]),
        dict(kop="Drie vormen van socialisatie",
             opdracht="Zet bij elk gegeven de vorm, en zeg bij welk opvoedingsmilieu ze hoort.",
             oefeningen=[
                 ("rij", [("leren praten in de eerste jaren thuis", "primaire socialisatie"),
                          ("leren omgaan met de regels van een club", "secundaire socialisatie"),
                          ("beelden van hoe je hoort te zijn uit reclame",
                           "tertiaire socialisatie"),
                          ("een plaats zoeken in een nieuwe klas", "secundaire socialisatie")],
                  "Welke vorm?", WL),
                 ("open", "Waarom legt de primaire socialisatie de basis voor al de rest?",
                  "Omdat ze een kind de taal en de eerste regels leert waarmee het de andere milieus "
                  "binnengaat. Zonder die basis kan het in de school of de club niet meedoen.", 4),
                 ("waar", "De drie vormen van socialisatie lopen gelijk met de drie "
                          "opvoedingsmilieus uit de pedagogiek.", True),
             ]),
        dict(kop="Vier visies",
             opdracht="Zet bij elke kern de juiste naam.",
             oefeningen=[
                 ("rij", [("instituties bestaan voor jij geboren bent en vormen je",
                           "Emile Durkheim"),
                          ("elk onderdeel van een samenleving heeft een functie in het geheel",
                           "Talcott Parsons"),
                          ("de werkelijkheid wordt gemaakt in de omgang tussen mensen, met taal",
                           "George Herbert Mead"),
                          ("de groep waarmee je je vergelijkt hoeft niet je eigen groep te zijn",
                           "Robert K. Merton")],
                  "Welke visie?", WL),
                 ("kort", "Hoe heet de visie van Mead, in drie woorden?",
                  "het symbolisch interactionisme", WL),
                 ("open", "Twee van de vier visies kijken van de samenleving naar de mens, en één "
                          "kijkt van de mens naar de samenleving. Welke, en leg uit.",
                  "Durkheim en Parsons kijken van de samenleving naar de mens: de instituties en de "
                  "functies van het geheel vormen het individu. Mead kijkt omgekeerd: in de gesprekken "
                  "en de omgang tussen mensen wordt de werkelijkheid en het beeld van jezelf gemaakt.",
                  6),
                 ("open", "Waarom is spel volgens Mead zo belangrijk voor een kind?",
                  "Omdat je volgens Mead jezelf leert kennen door de ogen van anderen. Wie vadertje en "
                  "moedertje speelt, oefent erin zich in de rol van een ander te zetten, en daarmee "
                  "bouwt het een beeld van wie het zelf is.", 5),
                 ("open", "Iemand heeft het objectief goed en voelt zich toch tekortgedaan. Hoe legt "
                          "Merton dat uit?",
                  "Met de referentiegroep: de groep waarmee iemand zich vergelijkt. Vergelijkt hij "
                  "zich met een groep die hoger ligt, dan voelt hij zich tekortgedaan, ook al gaat het "
                  "hem goed.", 5),
                 ("open", "Waarom is een referentiegroep niet hetzelfde als een ingroup?",
                  "Een ingroup is de groep waartoe je behoort. Een referentiegroep is de groep waaraan "
                  "je je spiegelt, en dat hoeft je eigen groep niet te zijn.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-sociale-stratificatie-en-de-verklaringsmodellen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale stratificatie en de verklaringsmodellen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier stratificatiesystemen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Systeem", "Hoe je laag bepaald wordt", "Kan je veranderen?"],
                  [["slavenmaatschappij", None, None],
                   ["kastenmaatschappij", None, None],
                   ["standenmaatschappij", None, None],
                   ["klassenmaatschappij", None, None]],
                  "een mens is iemands bezit, nee; je wordt in je kaste geboren, vaak religieus "
                  "onderbouwd, nee; geboorte en stand met eigen rechten per stand, nauwelijks; "
                  "je plaats in het economisch leven, ja in principe", WW),
                 ("open", "Kaste en stand lijken op elkaar. Wat is het verschil?",
                  "Een kaste ligt volledig vast en is religieus onderbouwd, dus ook met geld kom je er "
                  "niet uit. Een stand is wettelijk vastgelegd, met eigen rechten en plichten per "
                  "stand, en er was heel beperkt beweging mogelijk, bijvoorbeeld via de kerk of het "
                  "leger.", 5),
                 ("open", "Waarom is stratificatie geen kwestie van individueel verschil?",
                  "Omdat ze in de structuur van een samenleving zit. Ze gaat niet over wie slimmer of "
                  "harder werkt, maar over het feit dat er lagen bestaan waarin mensen geboren "
                  "worden.", 4),
                 ("kort", "Van welk Latijns woord komt stratificatie, en wat betekent het?",
                  "stratum, laag", WW),
             ]),
        dict(kop="Vijf verklaringsmodellen",
             opdracht="Zet bij elke kern de naam, en zet erbij of het model conflictsociologisch of "
                      "functionalistisch is.",
             oefeningen=[
                 ("rij", [("de ongelijkheid zit in het bezit van de productiemiddelen",
                           "Marx, conflictsociologisch"),
                          ("in klasse, status en partij samen", "Weber, conflictsociologisch"),
                          ("in gezag: wie mag bevelen", "Dahrendorf, conflictsociologisch"),
                          ("in economisch, cultureel en sociaal kapitaal",
                           "Bourdieu, conflictsociologisch")],
                  "Welk model, welk perspectief?", WL),
                 ("rij", [("ongelijkheid heeft een functie: ze beloont de moeilijke en belangrijke "
                           "posities", "Davis en Moore, functionalistisch")],
                  "Welk model, welk perspectief?", WL),
                 ("open", "Een manager zonder aandelen geeft leiding aan driehonderd mensen. Welk "
                          "model legt zijn klasse het best uit, en waarom lukt dat bij Marx niet?",
                  "Het model van Dahrendorf, met het gezag: hij mag bevelen, en dat bepaalt zijn "
                  "plaats. Bij Marx zou hij geen bezitter zijn en dus bij de arbeiders horen, en dat "
                  "klopt niet met zijn positie.", 5),
                 ("open", "Weber maakt van één lijn drie lijnen. Wat kan hij daardoor uitleggen wat "
                          "Marx niet kan?",
                  "Dat iemand rijk kan zijn met weinig aanzien, of veel aanzien met weinig geld. Bij "
                  "Marx is er één lijn, bezit of geen bezit; bij Weber zijn klasse, status en partij "
                  "drie aparte dingen die niet hoeven samen te lopen.", 5),
                 ("rij", [("een spaarrekening en een huis", "economisch kapitaal"),
                          ("thuis boeken en de taal van de school horen", "cultureel kapitaal"),
                          ("een oom die je aan een stage helpt", "sociaal kapitaal")],
                  "Welk kapitaal bij Bourdieu?", WW),
                 ("open", "Hoe legt Bourdieu met het cultureel kapitaal uit dat twee kinderen met "
                          "dezelfde verstandelijke mogelijkheden niet gelijk aan de school beginnen?",
                  "Omdat het ene kind de taal en de gewoonten van de school al van thuis meekreeg en "
                  "het andere niet. Dat cultureel kapitaal is geen geld, maar het wordt wel doorgegeven "
                  "en het geeft een voorsprong op school.", 5),
                 ("open", "Geef de twee tegenwerpingen tegen Davis en Moore.",
                  "Ten eerste zouden de best betaalde beroepen dan ook de nuttigste moeten zijn, en "
                  "dat klopt niet. Ten tweede kiest niet iedereen vrij: wie geen middelen heeft, komt "
                  "aan die lange opleiding niet toe.", 5),
             ]),
        dict(kop="Stratificatie vandaag",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Waarop is de EGP-klassenindeling van Goldthorpe gebaseerd?",
                  "op het beroep en de arbeidsverhouding", WL),
                 ("kort", "Uit welke drie gegevens bestaat de sociaal-economische status?",
                  "opleiding, beroep en inkomen", WL),
                 ("open", "Iemand met een hoog diploma en een laag loon heeft een andere SES dan "
                          "iemand met hetzelfde loon zonder diploma. Wat leert dat over het begrip?",
                  "Dat SES niet hetzelfde is als inkomen: inkomen is er maar één van de drie. "
                  "Opleiding en beroep wegen mee, en daardoor kan dezelfde verdienste een andere SES "
                  "geven.", 4),
                 ("open", "Waarom staat de SES in zowat elk sociaal onderzoek als achtergrondgegeven?",
                  "Omdat ze samenhangt met bijna alles: met gezondheid en levensverwachting, met "
                  "schoolresultaten, met wonen en met deelname aan het verenigingsleven. Wie dat "
                  "gegeven niet meeneemt, schrijft een verschil aan iets anders toe.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-sociale-mobiliteit-meritocratie-en-het-matheuseffect-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale mobiliteit, meritocratie en het matheüseffect",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier soorten mobiliteit",
             opdracht="Zet bij elk voorbeeld de soort of de soorten mobiliteit.",
             oefeningen=[
                 ("rij", [("van verpleegkundige naar leerkracht", "horizontale mobiliteit"),
                          ("van arbeider naar ploegbaas", "verticale mobiliteit"),
                          ("beginnen aan de kassa en eindigen als filiaalhouder",
                           "verticale en intragenerationele mobiliteit"),
                          ("de dochter van een poetsvrouw wordt arts",
                           "verticale en intergenerationele mobiliteit")],
                  "Welke soort?", WL),
                 ("open", "Intra en inter: wat betekent dat ene letterverschil hier?",
                  "Intra betekent binnen, inter betekent tussen. Intragenerationele mobiliteit blijft "
                  "bij één persoon en zijn eigen loopbaan; intergenerationele mobiliteit vergelijkt "
                  "twee generaties, dus ouder en kind.", 5),
                 ("waar", "De twee paren staan los van elkaar, zodat iemand verticale en "
                          "intragenerationele mobiliteit tegelijk kan maken.", True),
             ]),
        dict(kop="Factoren",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Inkomen en rijkdom of bezit staan apart in de lijst van de fiche. Waarom?",
                  "Inkomen is wat er binnenkomt, rijkdom of bezit is wat er al staat. Bezit kan geërfd "
                  "worden en geeft een buffer die een loon niet geeft, en daarom werken de twee niet "
                  "hetzelfde op mobiliteit.", 5),
                 ("open", "Huwelijk en echtscheiding kunnen in beide richtingen werken. Leg uit.",
                  "Een huwelijk kan een positie optrekken, en een scheiding kan er een doen zakken, "
                  "vaker bij vrouwen met kinderen. Dezelfde factor kan dus zowel opwaartse als "
                  "neerwaartse mobiliteit geven.", 5),
                 ("open", "Waarom staat leeftijd ook in de lijst?",
                  "Omdat wie op zijn vijftigste zijn werk verliest veel moeilijker terugkomt op niveau "
                  "dan wie dat op zijn vijfentwintigste overkomt. Dezelfde gebeurtenis geeft op een "
                  "andere leeftijd een ander gevolg.", 4),
             ]),
        dict(kop="Onderwijs en meritocratie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Onderwijs doet twee dingen tegelijk met ongelijkheid. Welke twee?",
                  "Het is de belangrijkste weg naar boven, want een diploma opent deuren die afkomst "
                  "sluit. En het geeft bestaande ongelijkheid door, want de richting waarin een kind "
                  "terechtkomt hangt mee samen met de opleiding van zijn ouders. Wie maar één van die "
                  "twee zegt, heeft de helft van het antwoord.", 6),
                 ("kort", "Van welk Latijns woord komt meritocratie, en wat betekent het?",
                  "meritum, verdienste", WW),
                 ("tabel", ["Voor meritocratie", "Tegen meritocratie"],
                  [[None, None], [None, None], [None, None]],
                  "voor: afkomst beslist niet meer, de juiste mensen komen op de juiste plaats, ze "
                  "moedigt inzet aan; tegen: talent en inzet zijn zelf ongelijk verdeeld bij de start, "
                  "wie het niet haalt krijgt de schuld, verdienste wordt gemeten met middelen die niet "
                  "iedereen heeft", WL),
                 ("open", "Wat is het zwaarste argument tegen meritocratie?",
                  "Dat ze de ongelijkheid verandert van een onrecht in iets dat je zelf verdiend hebt. "
                  "Wie het niet haalt, krijgt de schuld, en daardoor is de ongelijkheid veel "
                  "moeilijker aan te klagen.", 5),
             ]),
        dict(kop="Uitsluiting en het matheüseffect",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Leg de vicieuze cirkel uit tussen een lage sociale positie en sociale "
                          "uitsluiting.",
                  "Een lagere positie verhoogt de kans op uitsluiting: niet mee op reis, geen "
                  "lidmaatschap, geen netwerk. En de uitsluiting houdt die positie vast, want wie niet "
                  "meedoet bouwt geen netwerk op, en net dat netwerk helpt aan werk.", 5),
                 ("rij", [("studietoelagen en goedkoop hoger onderwijs",
                           "gezinnen die hun kind tot daar brengen"),
                          ("gesubsidieerde muziekschool", "wie de weg kent en het aanbod vindt"),
                          ("een belastingvoordeel voor pensioensparen", "wie geld kan wegzetten")],
                  "Wie heeft er in de praktijk het meest aan?", WL),
                 ("open", "Het matheüseffect gaat niet over wie recht heeft op een maatregel. Waar "
                          "gaat het dan over?",
                  "Over wie de maatregel in de praktijk weet te gebruiken. De maatregel staat open "
                  "voor iedereen, maar de voordelen komen vooral terecht bij wie al het best geplaatst "
                  "is. Daarom is een maatregel voor iedereen soms minder herverdelend dan ze lijkt.",
                  5),
                 ("kort", "Waar komt de naam matheüseffect van?",
                  "uit het evangelie van Matteüs", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mediatisering-en-de-functies-van-de-massamedia-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mediatisering en de functies van de massamedia",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Mediatisering",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("een politicus bouwt zijn boodschap op maat van een kort fragment",
                           "mediatisering"),
                          ("een club plant zijn wedstrijd op het uur dat de televisie wil",
                           "mediatisering"),
                          ("iemand kijkt elke avond twee uur televisie",
                           "veel media gebruiken, geen mediatisering")],
                  "Mediatisering of niet?", WL),
                 ("open", "Waarom is mediatisering niet hetzelfde als veel media gebruiken?",
                  "Omdat het gaat over de logica van de media die buiten de media gaat gelden: kort, "
                  "zichtbaar en met een beeld erbij. Andere domeinen gaan zich naar de media "
                  "gedragen, en dat is iets anders dan veel kijken.", 5),
                 ("kort", "Wat zijn massamedia?",
                  "media die een groot en onbekend publiek tegelijk bereiken", WL),
             ]),
        dict(kop="Functies voor het individu",
             opdracht="Zet bij elk voorbeeld de functie.",
             oefeningen=[
                 ("rij", [("het journaal", "informatieve functie"),
                          ("een documentaire over de hersenen", "educatieve functie"),
                          ("een spelprogramma", "ontspannende functie"),
                          ("een campagne tegen roken", "persuasieve functie")],
                  "Welke functie?", WL),
                 ("rij", [("een advertentie voor een gsm", "commerciële functie"),
                          ("een nieuwsquiz", "infotainment"),
                          ("een programma waarin je leert terwijl je lacht", "edutainment")],
                  "Welke functie of mengvorm?", WL),
                 ("open", "Persuasief en commercieel liggen dicht bij elkaar. Wat is het verschil? "
                          "Geef van elk een voorbeeld.",
                  "Bij een persuasieve functie willen ze je mening veranderen, bijvoorbeeld een "
                  "campagne tegen roken of een opiniestuk. Bij een commerciële functie willen ze je "
                  "iets verkopen, bijvoorbeeld een advertentie voor een gsm.", 5),
                 ("open", "Een documentaire over het klimaat kan drie functies tegelijk hebben. Welke, "
                          "en waarom?",
                  "De informatieve functie, want ze brengt je op de hoogte; de educatieve, want je "
                  "leert erbij; en de persuasieve, want ze wil je van een standpunt overtuigen. Eén "
                  "programma kan dus meerdere functies vervullen.", 5),
             ]),
        dict(kop="Functies voor de samenleving",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Deel van de politieke functie", "Wat de media doen"],
                  [["informerende functie", None],
                   ["woordvoerder- of spreekbuisfunctie", None],
                   ["onderzoeksfunctie", None],
                   ["commentaarfunctie", None],
                   ["controlerende of waakhondfunctie", None]],
                  "burgers de feiten geven die ze nodig hebben om te kiezen; groepen en meningen aan "
                  "het woord laten; zelf uitzoeken wat niet in de openbaarheid lag; de feiten wegen en "
                  "er een standpunt bij geven; de macht in het oog houden en rekenschap vragen", WL),
                 ("kort", "Welke vier functies voor de samenleving noemt de fiche?",
                  "de politieke functie, cultuuroverdracht, de vrijetijdsfunctie en de sociale functie",
                  WL),
                 ("open", "Dezelfde uitzending kan voor jou ontspanning zijn en voor de samenleving "
                          "cultuuroverdracht. Waarom is dat geen tegenspraak?",
                  "Omdat de fiche twee aparte lijsten heeft: functies voor het individu en functies "
                  "voor de samenleving. Je moet dus eerst lezen voor wie de functie geldt; dezelfde "
                  "uitzending kan op de twee lijsten een andere functie hebben.", 5),
                 ("open", "Informeren en onderzoeken liggen niet zo dicht bij elkaar als het lijkt. "
                          "Wat is het verschil?",
                  "Informeren is doorgeven wat er is. Onderzoeken is zelf opgraven wat iemand liever "
                  "verborgen hield, en dat vraagt eigen werk van de redactie.", 4),
             ]),
        dict(kop="De vierde macht",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Macht", "Wie", "Wat ze doet"],
                  [["wetgevende macht", None, None],
                   ["uitvoerende macht", None, None],
                   ["rechterlijke macht", None, None]],
                  "het parlement, maakt de wetten; de regering, voert de wetten uit; de rechtbanken, "
                  "spreken recht", WW),
                 ("waar", "De media zijn de vierde staatsmacht van een democratie.", False),
                 ("open", "Waarom zou het de functie van de media onmogelijk maken als je ze bij de "
                          "drie staatsmachten zou rekenen?",
                  "Omdat de media hun invloed juist hebben omdát ze onafhankelijk van de staat staan. "
                  "Wie ze bij de staatsmachten rekent, maakt ze deel van wat ze moeten controleren, en "
                  "dan blijft de controle op de macht in de handen van de macht zelf.", 5),
                 ("open", "Aan welke van de vijf politieke functies hangt de vierde macht vooral vast? "
                          "Leg uit.",
                  "Aan de controlerende of waakhondfunctie. Zonder media die durven onderzoeken en "
                  "rekenschap vragen, is er geen onafhankelijke controle op de drie andere machten.",
                  4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mediatheorieen-beeldvorming-en-persvrijheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mediatheorieën, beeldvorming en persvrijheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vijf mediatheorieën",
             opdracht="Zet bij elke kern de theorie, en de naam als de fiche er een geeft.",
             oefeningen=[
                 ("rij", [("de media spuiten een boodschap in een publiek dat die zonder meer opneemt",
                           "de injectienaaldtheorie"),
                          ("niet wat doen de media met mensen, maar wat doen mensen met de media",
                           "de functionalistische mediatheorie"),
                          ("de media bepalen waarover we praten, niet wat we vinden",
                           "de agendasettingtheorie, McCombs en Shaw"),
                          ("jarenlang kijken vormt je wereldbeeld",
                           "de cultivatietheorie, Gerbner")],
                  "Welke theorie?", WL),
                 ("rij", [("de hele samenleving neemt de logica van de media over",
                           "de mediatiseringstheorie, Stig Hjarvard")],
                  "Welke theorie?", WL),
                 ("kort", "Welke vier namen noemt de fiche bij de functionalistische mediatheorie?",
                  "Lasswell, Lazarsfeld, Merton en Wright", WL),
                 ("open", "Waarom is de injectienaaldtheorie toch belangrijk om te kennen, al is ze "
                          "achterhaald?",
                  "Omdat ze het vertrekpunt is waar de andere theorieën tegenin gaan. Mensen kiezen "
                  "zelf wat ze bekijken, praten met anderen en geloven niet wat niet bij hen past, en "
                  "precies dat laten de latere theorieën zien.", 5),
                 ("open", "Wat is de kantelvraag tussen de injectienaald en de functionalistische "
                          "theorie?",
                  "Of het publiek passief of actief is. Bij de injectienaald ondergaat het publiek de "
                  "boodschap; bij de functionalistische theorie kiest, gebruikt en haalt het eruit wat "
                  "het nodig heeft.", 5),
                 ("open", "Het nieuws gaat drie weken over de files, en plots vindt het land de files "
                          "een groot probleem. Welke theorie, en wat bepalen de media hier niet?",
                  "De agendasettingtheorie van McCombs en Shaw: de media bepalen de agenda, dus "
                  "waarover we praten. Wat je over de files vindt, bepalen ze daarmee niet.", 5),
                 ("open", "Agendasetting en cultivatie werken niet op dezelfde termijn. Leg uit.",
                  "Agendasetting werkt snel: een nieuwsgolf van drie weken verandert de agenda. "
                  "Cultivatie werkt langzaam: een wereldbeeld verandert door jaren kijken, niet door "
                  "één uitzending.", 5),
             ]),
        dict(kop="Beeldvorming",
             opdracht="Zet bij elk voorbeeld het mechanisme.",
             oefeningen=[
                 ("rij", [("een betoging als een protest of als een rel brengen", "framing"),
                          ("na een reeks over fraude lees je een bericht over een ondernemer anders",
                           "priming"),
                          ("van alles wat gebeurt, haalt maar een klein deel het journaal",
                           "het selectieproces"),
                          ("nabijheid, bekende namen en hoe uitzonderlijk iets is",
                           "de selectiecriteria")],
                  "Welk mechanisme?", WL),
                 ("rij", [("een hele groep beschrijven alsof allen hetzelfde zijn",
                           "stereotypering"),
                          ("mensen in groepen indelen om de wereld te kunnen overzien",
                           "sociale categorisering")],
                  "Welk mechanisme?", WL),
                 ("open", "Framing en priming worden vaak verward. Waar zit elk van de twee?",
                  "Framing zit in de boodschap zelf: het kader waarin ze verteld wordt. Priming zit in "
                  "wat eraan voorafging: een eerdere boodschap maakt de lezer klaar om wat erna komt "
                  "op een bepaalde manier te lezen.", 5),
                 ("open", "Wanneer wordt sociale categorisering een probleem?",
                  "Zodra er vaste eigenschappen aan die categorie gehangen worden. Dan is het een "
                  "stereotype, en dat kan uitlopen op vooroordeel en discriminatie. Het indelen zelf "
                  "is niet kwaadwillig: ons brein doet dat om de wereld te kunnen overzien.", 5),
             ]),
        dict(kop="Vrijheid en haar grenzen",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Vrijheid", "Van wie", "Wat ze beschermt"],
                  [["vrijheid van meningsuiting", None, None],
                   ["persvrijheid", None, None]],
                  "van iedereen, je mening mogen uiten en informatie mogen krijgen; van de pers, "
                  "zonder voorafgaande controle van de overheid kunnen berichten", WW),
                 ("open", "Waarom horen beide vrijheden in een democratie thuis?",
                  "Omdat een burger zonder vrije informatie niet kan weten waarover hij kiest, en "
                  "omdat niemand zonder vrije pers de macht kan controleren. Dat laatste is de "
                  "waakhondfunctie, en zonder persvrijheid bestaat ze niet.", 5),
                 ("rij", [("aanzetten tot haat of geweld", "een beperking"),
                          ("laster en eerroof", "een beperking"),
                          ("een kritisch artikel over een minister", "geen beperking"),
                          ("het privéleven van iemand die in het nieuws komt", "een beperking")],
                  "Een beperking van de persvrijheid of niet?", WL),
                 ("open", "Persvrijheid betekent geen voorafgaande controle, niet geen "
                          "verantwoordelijkheid. Leg dat verschil uit.",
                  "Een journalist mag publiceren zonder dat iemand hem op voorhand toelating geeft. "
                  "Achteraf kan hij wel voor de rechter verantwoording afleggen, bijvoorbeeld voor "
                  "laster. Het verschil tussen vooraf en achteraf is de kern van het begrip.", 5),
                 ("open", "Noem drie dingen die gebeuren in een land zonder persvrijheid.",
                  "De overheid beslist wat er verschijnt, journalisten worden bedreigd of opgesloten, "
                  "en websites worden afgesloten. Organisaties stellen daarom ranglijsten van "
                  "persvrijheid op.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-maatschappelijke-vraagstukken-en-de-redeneeractiviteiten-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Maatschappelijke vraagstukken en de redeneeractiviteiten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twaalf vraagstukken",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel maatschappelijke vraagstukken noemt de fiche?", "twaalf", W),
                 ("rij", [("mensen gaan minder in vaste verbanden en meer als individu door het "
                           "leven", "individualisering"),
                          ("steeds meer wordt geregeld volgens berekening, efficiëntie en regels",
                           "rationalisering"),
                          ("files, openbaar vervoer en het verplaatsen van goederen", "mobiliteit")],
                  "Welk vraagstuk?", WW),
                 ("open", "Mobiliteit staat in deze lijst én er was eerder een thema over sociale "
                          "mobiliteit. Wat is het verschil?",
                  "Hier betekent mobiliteit het verplaatsen van mensen en goederen: verkeer, files, "
                  "openbaar vervoer. Sociale mobiliteit gaat over stijgen en dalen op de sociale "
                  "ladder. Zelfde woord, een ander vraagstuk.", 5),
                 ("open", "Geef van rationalisering twee voorbeelden uit het dagelijks leven.",
                  "De wachtrij die een nummertje wordt, en de zorg die in minuten per handeling "
                  "gerekend wordt. In beide gevallen vervangt een berekening een gewoonte.", 4),
             ]),
        dict(kop="Vijf invalshoeken",
             opdracht="Het vraagstuk is het klimaat. Zet bij elk gegeven de invalshoek.",
             oefeningen=[
                 ("rij", [("de prijs van energie en de kost van een overstroming", "economisch"),
                          ("wie een slecht geïsoleerd huis huurt, voelt het eerst", "sociaal"),
                          ("vliegen als vanzelfsprekend of niet meer", "cultureel"),
                          ("een akkoord tussen landen", "politiek")],
                  "Welke invalshoek?", WW),
                 ("rij", [("een vonnis dat een staat tot maatregelen verplicht", "juridisch"),
                          ("de werkloosheid in een sector die verdwijnt", "economisch"),
                          ("de verhouding tussen een rijke en een arme buurt", "sociaal")],
                  "Welke invalshoek?", WW),
                 ("open", "Sociaal en cultureel liggen het dichtst bij elkaar. Waarover gaat elk van "
                          "de twee?",
                  "Sociaal gaat over mensen en hun verhoudingen: wie wordt geraakt, en hoe staan "
                  "groepen tegenover elkaar. Cultureel gaat over waarden, gewoonten en betekenis: wat "
                  "men normaal vindt.", 5),
                 ("open", "Wat onderscheidt de politieke van de juridische invalshoek?",
                  "Politiek is wat er beslist wordt en door wie. Juridisch is wat er in de wet staat "
                  "en wat een rechter daarmee doet.", 4),
             ]),
        dict(kop="De vier redeneeractiviteiten",
             opdracht="Zet de activiteiten in de juiste orde en zeg wat je bij elke stap doet.",
             oefeningen=[
                 ("tabel", ["", "Activiteit", "De vraag", "Wat je doet"],
                  [["1", None, None, None],
                   ["2", None, None, None],
                   ["3", None, None, None],
                   ["4", None, None, None]],
                  "1 een maatschappelijk probleem beschrijven, wat is er aan de hand, feiten en "
                  "cijfers; 2 een maatschappelijk probleem verklaren, waarom is het zo, oorzaken en "
                  "verbanden; 3 creatieve ideeën genereren, wat zou kunnen helpen, veel ideeën zonder "
                  "te schrappen; 4 oplossingen evalueren, zou het werken en kan het, de ideeën tegen "
                  "criteria afwegen", W),
                 ("rij", [("één op de vijf gezinnen in deze buurt heeft geen auto", "beschrijven"),
                          ("dat komt doordat de huurprijzen hier lager zijn", "verklaren"),
                          ("misschien kan er een buurtbus komen", "ideeën genereren"),
                          ("een buurtbus kost te veel voor te weinig ritten", "oplossingen evalueren")],
                  "Welke redeneeractiviteit?", WL),
                 ("open", "Waarom zijn stap 3 en stap 4 met opzet apart gehouden?",
                  "Omdat je in stap 3 niets mag afkeuren: wie meteen begint te oordelen, houdt twee "
                  "saaie ideeën over. Het wegen gebeurt pas in stap 4, als alle ideeën op tafel "
                  "liggen.", 5),
                 ("open", "Wat hoort er bij élke stap, en waarom kan een mening geen stap dragen?",
                  "Bij elke stap hoort redeneren met bewijs: elke bewering hangt aan iets waar iemand "
                  "ze aan kan nakijken, zoals een cijfer, een onderzoek, een wettekst of een "
                  "getuigenis. Een bewering zonder bewijs is een mening, en die mag in het gesprek "
                  "maar kan geen stap in het schema dragen.", 6),
             ]),
        dict(kop="Uitvoerbaarheid",
             opdracht="Zet bij elke vraag het criterium.",
             oefeningen=[
                 ("rij", [("kan het binnen een redelijke termijn?", "tijd"),
                          ("is er genoeg geld, personeel en kennis?", "middelen"),
                          ("mag dit, en raakt het niemands rechten?", "ethische principes"),
                          ("houdt het stand, en wat laat het na voor later?",
                           "duurzaamheidsprincipes")],
                  "Welk criterium?", WL),
                 ("open", "Een oplossing is snel en goedkoop en valt toch af. Noem de twee criteria "
                          "die dat kunnen doen, met telkens een reden.",
                  "De ethische principes: ze kan een groep onrecht doen, en dan mag ze niet. En de "
                  "duurzaamheidsprincipes: ze kan het probleem naar later doorschuiven, en dan lost ze "
                  "niets op.", 5),
                 ("open", "Waarom is uitvoerbaar niet hetzelfde als doeltreffend?",
                  "Een oplossing kan werken en toch onuitvoerbaar zijn, bijvoorbeeld omdat het geld "
                  "er niet is. En ze kan goed uitvoerbaar zijn en niets oplossen. In stap 4 weeg je "
                  "daarom beide vragen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-onderzoekscyclus-van-orienteren-tot-rapporteren-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De onderzoekscyclus van oriënteren tot rapporteren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier fasen",
             opdracht="Vul aan en zet bij elke bezigheid de fase.",
             oefeningen=[
                 ("tabel", ["", "Fase", "Wat je doet"],
                  [["1", None, None], ["2", None, None], ["3", None, None], ["4", None, None]],
                  "1 oriënteren, je thema verkennen en je onderzoeksvraag opstellen; 2 voorbereiden, "
                  "kiezen hoe je het aanpakt; 3 uitvoeren, de gegevens verzamelen en verwerken; "
                  "4 rapporteren, je besluit opschrijven en je werk zichtbaar maken", W),
                 ("rij", [("je leest wat er al over je thema bestaat", "oriënteren"),
                          ("je kiest je meetinstrument en je deelnemers", "voorbereiden"),
                          ("je neemt de interviews af", "uitvoeren"),
                          ("je schrijft je besluit en vermeldt je bronnen", "rapporteren")],
                  "Welke fase?", WW),
                 ("open", "Waarom hoort de onderzoeksvraag bij oriënteren en niet bij voorbereiden?",
                  "Omdat je eerst moet weten wát je wil weten en dan pas hóe je het gaat onderzoeken. "
                  "Wie de methode eerst kiest, buigt zijn vraag naar zijn methode.", 4),
                 ("open", "Waarom heet het een cyclus en niet een reeks?",
                  "Omdat het einde geen einde is: een besluit roept nieuwe vragen op, en daar begint "
                  "een volgend onderzoek. Rapporteren is dus ook het vertrekpunt voor wie na jou "
                  "komt.", 4),
             ]),
        dict(kop="Zes criteria toepassen",
             opdracht="Elke vraag hieronder faalt op één criterium. Schrijf op welk, en herschrijf de "
                      "vraag zodat ze wel kan.",
             oefeningen=[
                 ("rij", [("Zijn jongeren veel op hun gsm?", "niet open"),
                          ("Hoeveel lezen jongeren en wat vinden hun ouders daarvan?",
                           "niet enkelvoudig"),
                          ("Waarom is sociale media zo schadelijk voor kinderen?", "niet objectief"),
                          ("Hoe leven alle jongeren in Europa?", "niet haalbaar")],
                  "Op welk criterium faalt ze?", WW),
                 ("rij", [("Mag een kind een gsm hebben?", "niet onderzoekbaar"),
                          ("Hoeveel letters staan er in de schoolnaam van elke leerling?",
                           "niet relevant")],
                  "Op welk criterium faalt ze?", WW),
                 ("open", "Herschrijf de vraag „Zijn jongeren veel op hun gsm?” zodat ze aan "
                          "alle zes de criteria voldoet.",
                  "Bijvoorbeeld: hoeveel uur per dag gebruiken leerlingen van de derde graad in onze "
                  "school hun gsm? Die vraag is open, enkelvoudig, objectief, haalbaar in één school, "
                  "met gegevens te beantwoorden en relevant voor het schoolbeleid.", 5),
                 ("open", "Leg het verschil uit tussen niet objectief en niet onderzoekbaar.",
                  "Een niet objectieve vraag zit het antwoord al in: ze veronderstelt bijvoorbeeld dat "
                  "iets schadelijk is. Een niet onderzoekbare vraag kan met geen enkel gegeven "
                  "beslecht worden, want ze vraagt wat mág, en dat is een ethische vraag.", 5),
                 ("open", "Leg het verschil uit tussen haalbaar en onderzoekbaar.",
                  "Haalbaar gaat over jou: je tijd, je geld en je bereik. Onderzoekbaar gaat over de "
                  "vraag zelf: ook met onbeperkte middelen blijft een vraag naar wat mag "
                  "onbeantwoordbaar met gegevens.", 5),
                 ("kort", "Met welke drie woordjes begint vaak een gesloten vraag?",
                  "is, zijn of heeft", WW),
             ]),
        dict(kop="Soorten onderzoek",
             opdracht="Zet bij elk voorbeeld de twee soorten: waar de gegevens vandaan komen, en wat "
                      "voor gegevens het zijn.",
             oefeningen=[
                 ("rij", [("je verwerkt bestaande cijfers van Statbel",
                           "deskresearch, kwantitatief"),
                          ("je interviewt tien ouders over hoe ze het beleven",
                           "fieldresearch, kwalitatief"),
                          ("je laat tweehonderd leerlingen een enquête met gesloten vragen invullen",
                           "fieldresearch, kwantitatief"),
                          ("je leest tien bestaande interviews na op terugkerende thema's",
                           "deskresearch, kwalitatief")],
                  "Welke twee soorten?", WL),
                 ("open", "Waarom zijn er vier combinaties en niet twee soorten onderzoek?",
                  "Omdat de twee paren los van elkaar staan. Het eerste paar gaat over waar je je "
                  "gegevens haalt, het tweede over wat voor gegevens het zijn. Elke combinatie van de "
                  "twee bestaat.", 5),
                 ("open", "Wat levert kwantitatief onderzoek, en wat kwalitatief? Waarom combineren "
                          "veel onderzoekers de twee?",
                  "Kwantitatief levert breedte: je kan iets over een grote groep zeggen, maar niet "
                  "waarom iemand het doet. Kwalitatief levert diepte: je begrijpt waarom, maar je kan "
                  "het niet doortrekken naar iedereen. Daarom doen veel onderzoekers eerst gesprekken "
                  "om te weten wat er speelt, en dan een enquête om te weten hoe vaak het speelt.", 6),
                 ("open", "Waarom is deskresearch bijna altijd de eerste stap, ook als je een "
                          "veldonderzoek plant?",
                  "Omdat je niet zelf tweehonderd mensen wil bevragen over iets dat iemand vorig jaar "
                  "al uitzocht. Eerst nagaan wat er bestaat, spaart werk uit en maakt je eigen vraag "
                  "scherper.", 4),
             ]),
        dict(kop="Uitvoeren en rapporteren",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem drie zorgen die bij het uitvoeren horen als je met mensen werkt.",
                  "Je steekproef moet lijken op de groep waarover je iets wil zeggen; je vragen mogen "
                  "niet sturen; en je vraagt toestemming, zegt waarvoor de gegevens dienen en houdt ze "
                  "anoniem.", 5),
                 ("open", "Waarom horen de beperkingen van je onderzoek in je verslag?",
                  "Omdat een lezer moet kunnen nagaan hoever je besluit draagt. Wie zijn beperkingen "
                  "vermeldt, maakt zijn verslag sterker, niet zwakker: het wordt navolgbaar.", 4),
                 ("open", "Wie meer ijsjes eet, verdrinkt vaker. Wat is hier de fout, en wat is de "
                          "echte oorzaak?",
                  "De fout is een verband voor een oorzaak nemen. Het ijsje is de oorzaak niet; de "
                  "warme zomerdag doet beide stijgen. Twee dingen die samen bewegen kunnen beide door "
                  "een derde veroorzaakt zijn.", 5),
                 ("waar", "In het examendeel over de onderzoekscyclus kunnen alle leerinhouden van "
                          "sociale wetenschappen verwerkt zijn.", True),
             ]),
    ],
)

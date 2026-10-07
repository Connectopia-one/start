# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij ontwikkeling en pedagogisch handelen
🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere opgaven, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
situaties, andere kinderen en opdrachten die je enkel op papier kan maken — een
observatie herschrijven, een activiteit uitwerken, een gesprek op papier zetten.
Wie hier iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/ontwikkeling-en-pedagogisch-handelen.json` en
naast `maak_ontwikkeling_en_pedagogisch_handelen.py`.

Theorieën staan hier met de naam van hun bedenker en met de fasen zoals die
beschreven zijn. Er staat geen verzonnen citaat in de mond van een echte
auteur, en de kritiek op een theorie staat erbij waar die hoort.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Ontwikkeling en pedagogisch handelen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIVEAU = "-boost-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "110px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een situatie: schrijf eerst wat je ziet, en pas daarna wat je ervan denkt.",
    "Bij een oefening met fasen: zet de leeftijd of de orde erbij.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("welzijn-en-welbevinden",
    titel="Welzijn en welbevinden",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("hoe goed iemand zich in zijn vel voelt", "welbevinden"),
                          ("de omstandigheden waarin iemand leeft", "welzijn"),
                          ("het geld en de goederen die iemand heeft", "welvaart"),
                          ("het vertrouwen dat je iets kan", "zelfvertrouwen of competentie"),
                          ("het gevoel dat je erbij hoort", "verbondenheid"),
                          ("het gevoel dat je zelf mag kiezen", "autonomie")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Leg met een voorbeeld uit dat welvaart en welbevinden niet "
                          "hetzelfde zijn.",
                  "Een kind in een groot huis met alles wat het wil kan zich eenzaam en "
                  "ongelukkig voelen. Welvaart gaat over middelen, welbevinden over hoe je je "
                  "voelt.", 3),
             ]),
        dict(kop="De drie basisbehoeften",
             opdracht="Zet achter elke situatie welke basisbehoefte onder druk staat: "
                      "autonomie, competentie of verbondenheid.",
             oefeningen=[
                 ("rij", [("een kind dat nooit eens zelf mag kiezen", "autonomie"),
                          ("een kind dat altijd het laatst gekozen wordt", "verbondenheid"),
                          ("een kind dat elke taak te moeilijk vindt", "competentie"),
                          ("een kind dat van thuis uit alles moet", "autonomie"),
                          ("een nieuwe leerling die niemand kent", "verbondenheid"),
                          ("een kind dat voor elke toets faalt", "competentie")],
                  "Welke behoefte?", WL),
                 ("open", "Een kind in de buitenschoolse opvang doet nooit mee. Noem drie "
                          "dingen die je kan doen, zonder te dwingen.",
                  "Naast het kind gaan zitten en zelf beginnen, een keuze geven uit twee "
                  "dingen, een ander kind vragen om samen iets te doen, een activiteit kiezen "
                  "waar dat kind goed in is, en bij de ouders navragen wat het thuis graag "
                  "doet.", 4),
             ]),
        dict(kop="Maslow",
             opdracht="Zet de behoeften van Maslow in de juiste orde, van 1 onderaan tot 5 "
                      "bovenaan.",
             oefeningen=[
                 ("rij", [("eten, drinken en slapen", "1"),
                          ("veiligheid en zekerheid", "2"),
                          ("erbij horen en liefde", "3"),
                          ("waardering en erkenning", "4"),
                          ("jezelf kunnen zijn en ontwikkelen", "5"),
                          ("de naam van zijn model", "de piramide of behoeftehiërarchie")],
                  "Welke laag?", WL),
                 ("open", "Een kind komt zonder ontbijt naar school en kan zich niet "
                          "concentreren. Wat zegt het model van Maslow daarover, en wat is de "
                          "kritiek op dat model?",
                  "De onderste behoefte is niet vervuld, dus de hogere komen niet aan bod. De "
                  "kritiek is dat de lagen in de praktijk niet zo strikt op elkaar volgen: "
                  "mensen in armoede maken wel kunst en zoeken wel verbinding.", 4),
             ]),
    ])


# ============================================================
zet("wat-bepaalt-onze-gezondheid",
    titel="Wat bepaalt onze gezondheid",
    reeksen=[
        dict(kop="Determinanten",
             opdracht="Zet achter elk gegeven welk soort determinant het is: persoonlijk, "
                      "leefstijl, omgeving of zorgstelsel.",
             oefeningen=[
                 ("rij", [("je leeftijd en je geslacht", "persoonlijk"),
                          ("dagelijks roken", "leefstijl"),
                          ("een vochtige woning", "omgeving"),
                          ("een huisarts op wandelafstand", "zorgstelsel"),
                          ("een erfelijke aandoening", "persoonlijk"),
                          ("werkloosheid in het gezin", "omgeving")],
                  "Welke determinant?", WL),
                 ("open", "Welke determinanten kan iemand zelf veranderen, en welke niet?",
                  "De leefstijl is gedeeltelijk een eigen keuze. Leeftijd, geslacht en "
                  "erfelijkheid niet, en de omgeving en het zorgstelsel maar beperkt. Daarom "
                  "is enkel naar de leefstijl kijken onrechtvaardig.", 3),
             ]),
        dict(kop="De gezondheidskloof",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat bedoelt men met de sociale gradiënt in gezondheid?",
                  "Hoe lager iemands inkomen en opleiding, hoe slechter gemiddeld zijn "
                  "gezondheid en hoe korter zijn leven. Het is geen kloof tussen twee groepen "
                  "maar een trap die over alle lagen loopt.", 3),
                 ("open", "Waarom is gezonder eten voor een gezin met weinig geld niet enkel "
                          "een kwestie van willen?",
                  "Verse producten zijn duurder per calorie, een winkel met keuze is niet "
                  "altijd dichtbij, en wie twee jobs combineert heeft geen tijd om te koken.",
                  3),
                 ("open", "Noem twee maatregelen van de overheid die de gezondheidskloof "
                          "kleiner maken.",
                  "Gratis of goedkope preventieve zorg, de gezondheidscheque en de "
                  "maximumfactuur, gezonde maaltijden op school, rookverboden, veilige "
                  "fietspaden in elke wijk.", 3),
             ]),
        dict(kop="Gezondheidsbevordering",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("informeren en sensibiliseren", "een campagne"),
                          ("de omgeving aanpassen zodat gezond kiezen vanzelf gaat",
                           "structurele maatregelen"),
                          ("fruit op school aanbieden", "een structurele maatregel"),
                          ("een affiche over tandenpoetsen", "voorlichting"),
                          ("de gezonde keuze de gemakkelijkste maken", "de omgeving inrichten"),
                          ("de doelgroep laten meedenken over de aanpak", "participatie")],
                  "Vul aan.", WL),
                 ("open", "Waarom werkt een affiche over gezond eten in een school zonder "
                          "gezond aanbod niet?",
                  "Je vraagt iets wat ter plaatse niet kan. Zonder een aanbod dat de keuze "
                  "mogelijk maakt, legt een campagne de last volledig bij de leerling.", 3),
             ]),
    ])


# ============================================================
zet("ontwikkeling-de-basisbegrippen",
    titel="Ontwikkeling: de basisbegrippen",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("wat je meekrijgt bij je geboorte", "erfelijkheid of nature"),
                          ("wat de omgeving met je doet", "opvoeding of nurture"),
                          ("de ontwikkeling van groot naar klein, hoofd eerst",
                           "de cefalocaudale richting"),
                          ("de ontwikkeling van het midden naar buiten",
                           "de proximodistale richting"),
                          ("de periode waarin iets het best geleerd wordt",
                           "een gevoelige periode"),
                          ("de mijlpaal die bijna elk kind rond dezelfde leeftijd haalt",
                           "een ontwikkelingsmijlpaal")],
                  "Hoe noemen we dit?", WL),
                 ("rij", [("alle domeinen samen", "de totale ontwikkeling"),
                          ("de domeinen beïnvloeden elkaar", "de samenhang"),
                          ("elk kind in zijn eigen tempo", "het individuele tempo"),
                          ("de orde van de stappen ligt vast", "de vaste volgorde"),
                          ("de ontwikkeling gaat van eenvoudig naar ingewikkeld",
                           "de toenemende complexiteit"),
                          ("een stap terug na een nieuwe stap vooruit", "regressie")],
                  "Welk kenmerk?", WL),
             ]),
        dict(kop="De domeinen",
             opdracht="Zet achter elke mijlpaal het domein: motorisch, cognitief, "
                      "socio-emotioneel of taal.",
             oefeningen=[
                 ("rij", [("zelf de trap op kruipen", "motorisch"),
                          ("mama en papa zeggen", "taal"),
                          ("lachen naar een bekend gezicht", "socio-emotioneel"),
                          ("een blok in een rond gat passen", "cognitief"),
                          ("zijn naam schrijven", "motorisch en cognitief"),
                          ("op zijn toer wachten bij een spel", "socio-emotioneel")],
                  "Welk domein?", WL),
                 ("open", "Een kind van drie zegt nog bijna niets. Waarom kijk je dan ook naar "
                          "zijn gehoor en naar zijn contact met anderen?",
                  "De domeinen hangen samen. Wie slecht hoort, leert geen taal, en wie geen "
                  "contact maakt, heeft geen reden om te praten. Het is een vraag voor de arts "
                  "of het CLB, niet voor jou alleen.", 4),
             ]),
        dict(kop="Nature en nurture",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom is de vraag of erfelijkheid of opvoeding belangrijker is, "
                          "verkeerd gesteld?",
                  "Ze werken altijd samen. Een erfelijke aanleg komt alleen tot uiting in een "
                  "omgeving die dat toelaat, en dezelfde omgeving doet bij twee kinderen iets "
                  "anders.", 3),
                 ("open", "Twee broers groeien in hetzelfde gezin op en verschillen sterk. Hoe "
                          "kan dat?",
                  "Ze hebben niet dezelfde erfelijke aanleg en ook niet dezelfde omgeving: ze "
                  "hebben een andere plaats in de rij, andere vrienden, andere leerkrachten, "
                  "en de ouders reageren verschillend op hen.", 3),
             ]),
    ])


# ============================================================
zet("de-fysieke-en-motorische-ontwikkeling",
    titel="De fysieke en motorische ontwikkeling",
    reeksen=[
        dict(kop="Mijlpalen",
             opdracht="Zet achter elke mijlpaal de leeftijd waarop de meeste kinderen dat "
                      "kunnen.",
             oefeningen=[
                 ("rij", [("het hoofd rechthouden", "ongeveer 3 maanden"),
                          ("zelf rechtop zitten", "ongeveer 6 tot 8 maanden"),
                          ("de eerste stapjes", "ongeveer 12 tot 15 maanden"),
                          ("een toren van vier blokken", "ongeveer 2 jaar"),
                          ("op één been staan", "ongeveer 3 tot 4 jaar"),
                          ("met een schaar knippen langs een lijn", "ongeveer 5 jaar")],
                  "Welke leeftijd?", WL),
                 ("open", "Waarom staat er bij elke mijlpaal ongeveer?",
                  "Elk kind heeft zijn eigen tempo. Een kind dat drie maanden later stapt is "
                  "niet achter; de orde van de stappen telt meer dan de datum.", 3),
             ]),
        dict(kop="Grove en fijne motoriek",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("lopen, klimmen en springen", "grove motoriek"),
                          ("een veter knopen", "fijne motoriek"),
                          ("een bal gooien", "grove motoriek"),
                          ("een potlood vasthouden", "fijne motoriek"),
                          ("de greep met de hele hand", "de palmaire greep"),
                          ("de greep met duim en wijsvinger", "de pincetgreep")],
                  "Vul aan.", WL),
                 ("open", "Waarom komt de grove motoriek voor de fijne?",
                  "De ontwikkeling gaat van het midden naar buiten en van groot naar klein. "
                  "Een kind moet eerst zijn romp en zijn schouder beheersen voor het zijn "
                  "vingers kan sturen.", 3),
                 ("open", "Noem drie spelletjes die de fijne motoriek van een kleuter oefenen, "
                          "zonder werkblad.",
                  "Rijgen met grote kralen, kneden met deeg, knopen van een jas, scheuren en "
                  "plakken, met een pincet pompons sorteren, wasknijpers op een lijn zetten.",
                  4),
             ]),
        dict(kop="De groei",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de curve waarop de arts de groei uitzet", "de groeicurve"),
                          ("de lijn waarop de helft van de kinderen zit", "de P50"),
                          ("waarom de eigen lijn van een kind telt",
                           "je volgt het verloop, niet één punt"),
                          ("de periode van snelle groei in de puberteit", "de groeispurt"),
                          ("de leeftijd waarop meisjes gemiddeld eerder spurten",
                           "ongeveer 2 jaar eerder dan jongens"),
                          ("wat groeipijn in de benen vaak is", "een onschuldig verschijnsel")],
                  "Vul aan.", WL),
                 ("open", "Een kind zit al jaren op de P10 en groeit mooi mee. Een ander valt "
                          "van de P50 naar de P10. Welke van de twee is het signaal?",
                  "Het tweede. Een kind dat klein is maar zijn eigen lijn volgt, groeit "
                  "normaal; een kind dat van zijn lijn afwijkt, hoort bij de arts.", 3),
             ]),
    ])


# ============================================================
zet("het-denken-volgens-piaget",
    titel="Het denken volgens Piaget",
    reeksen=[
        dict(kop="De vier stadia",
             opdracht="Zet achter elk stadium de leeftijd en één kenmerk.",
             oefeningen=[
                 ("rij", [("het sensomotorische stadium", "0 tot 2 jaar"),
                          ("het pre-operationele stadium", "2 tot 7 jaar"),
                          ("het concreet-operationele stadium", "7 tot 12 jaar"),
                          ("het formeel-operationele stadium", "vanaf 12 jaar"),
                          ("het stadium waarin een kind leert dat iets blijft bestaan",
                           "het sensomotorische"),
                          ("het stadium waarin abstract redeneren lukt",
                           "het formeel-operationele")],
                  "Welk stadium of welke leeftijd?", WL),
                 ("rij", [("objectpermanentie", "het sensomotorische stadium"),
                          ("egocentrisch denken", "het pre-operationele stadium"),
                          ("conservatie van hoeveelheid", "het concreet-operationele stadium"),
                          ("hypothetisch denken", "het formeel-operationele stadium"),
                          ("animisme: de pop heeft pijn", "het pre-operationele stadium"),
                          ("sorteren en in de omgekeerde richting denken",
                           "het concreet-operationele stadium")],
                  "Bij welk stadium hoort dit?", WL),
             ]),
        dict(kop="Begrippen van Piaget",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het denkschema dat een kind al heeft", "het schema"),
                          ("het nieuwe in het bestaande schema passen", "assimilatie"),
                          ("het schema zelf aanpassen aan het nieuwe", "accommodatie"),
                          ("het evenwicht tussen die twee", "equilibratie"),
                          ("weten dat een hoeveelheid gelijk blijft", "conservatie"),
                          ("weten dat iets bestaat als je het niet ziet",
                           "objectpermanentie")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Een kind noemt elke viervoeter hond, ook een geit. Is dat "
                          "assimilatie of accommodatie? En wat gebeurt er als iemand zegt dat "
                          "het een geit is?",
                  "Dat is assimilatie: het nieuwe dier gaat in het bestaande schema hond. "
                  "Daarna volgt accommodatie: het kind maakt een nieuw schema voor geit.", 4),
             ]),
        dict(kop="De proefjes van Piaget",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Je giet water uit een breed glas in een hoog smal glas, waar een "
                          "kind van vier bij staat. Wat zegt het kind, en waarom?",
                  "Het zegt dat er nu meer water is, omdat het alleen naar de hoogte kijkt. "
                  "Het heeft de conservatie van volume nog niet, en kan nog niet aan twee "
                  "dingen tegelijk denken.", 4),
                 ("open", "Twee rijen van zeven knopen liggen even lang. Je spreidt de ene rij "
                          "uit. Wat antwoordt een kind van vijf op de vraag waar er meer "
                          "liggen?",
                  "Het zegt in de uitgespreide rij, want die is langer. De conservatie van "
                  "aantal komt pas rond zeven jaar.", 3),
                 ("open", "Wat is de belangrijkste kritiek op Piaget?",
                  "Hij onderschatte wat jonge kinderen al kunnen: met eenvoudiger "
                  "proefopstellingen blijken ze veel eerder iets te begrijpen. En de stadia "
                  "zijn minder strikt en minder leeftijdsgebonden dan hij dacht.", 4),
             ]),
    ])


# ============================================================
zet("kohlberg-en-erikson",
    titel="Kohlberg en Erikson",
    reeksen=[
        dict(kop="De zes niveaus van Kohlberg",
             opdracht="Zet achter elk antwoord op de vraag waarom je niet steelt, het niveau "
                      "van Kohlberg.",
             oefeningen=[
                 ("rij", [("omdat ik straf krijg", "1, gehoorzaamheid en straf"),
                          ("omdat ik er zelf niets aan heb", "2, eigenbelang en ruil"),
                          ("omdat mijn mama het erg zou vinden", "3, goede verhoudingen"),
                          ("omdat het tegen de wet is", "4, wet en orde"),
                          ("omdat we samen afgesproken hebben hoe we leven",
                           "5, sociaal contract"),
                          ("omdat eigendom van een mens iets is dat je respecteert",
                           "6, universele principes")],
                  "Welk niveau?", WL),
                 ("open", "Kohlberg verdeelde die zes niveaus in drie fasen. Welke zijn dat?",
                  "Het preconventionele niveau (1 en 2), het conventionele niveau (3 en 4) en "
                  "het postconventionele niveau (5 en 6).", 3),
                 ("open", "Wat is de belangrijkste kritiek op Kohlberg?",
                  "Hij onderzocht vooral jongens en beoordeelde een denken in regels hoger "
                  "dan een denken in zorg voor anderen. Carol Gilligan noemde dat een "
                  "eenzijdige maatstaf. En wat iemand zegt in een dilemma is niet wat hij in "
                  "het echt doet.", 4),
             ]),
        dict(kop="De acht fasen van Erikson",
             opdracht="Vul de tegenstelling en de leeftijd aan.",
             oefeningen=[
                 ("rij", [("0 tot 1 jaar", "basisvertrouwen tegenover basiswantrouwen"),
                          ("1 tot 3 jaar", "autonomie tegenover schaamte en twijfel"),
                          ("3 tot 6 jaar", "initiatief tegenover schuldgevoel"),
                          ("6 tot 12 jaar", "vlijt tegenover minderwaardigheid"),
                          ("12 tot 18 jaar", "identiteit tegenover rolverwarring"),
                          ("de jonge volwassene", "intimiteit tegenover isolement")],
                  "Welke tegenstelling?", WL),
                 ("rij", [("de volwassene op middelbare leeftijd",
                           "generativiteit tegenover stagnatie"),
                          ("de oudere", "integriteit tegenover wanhoop"),
                          ("de fase waarin een baby leert dat er voor hem gezorgd wordt",
                           "de eerste"),
                          ("de fase waarin een tiener zoekt wie hij is", "de vijfde"),
                          ("wat generativiteit betekent",
                           "iets doorgeven aan een volgende generatie"),
                          ("waarom Erikson het hele leven beschrijft",
                           "ontwikkeling stopt niet bij de volwassenheid")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Toepassen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Een peuter van twee wil zijn jas zelf aandoen en wordt woedend als "
                          "je helpt. Welke fase van Erikson is dat, en wat doe je?",
                  "De fase autonomie tegenover schaamte en twijfel. Je geeft hem de tijd en "
                  "een stuk dat hij wel kan, bijvoorbeeld de mouw, zodat hij het gevoel houdt "
                  "dat hij het zelf kan.", 4),
                 ("open", "Een jongere van zestien wisselt van vriendengroep, van kleren en "
                          "van muziek. Is dat zorgwekkend?",
                  "Nee, dat is de fase identiteit tegenover rolverwarring. Uitproberen hoort "
                  "erbij. Je blijft wel een vast punt waarop hij kan terugvallen.", 4),
             ]),
    ])


# ============================================================
zet("de-socio-emotionele-ontwikkeling",
    titel="De socio-emotionele ontwikkeling",
    reeksen=[
        dict(kop="Gehechtheid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de band tussen een kind en zijn verzorger", "de gehechtheid"),
                          ("de onderzoeker die daarover schreef", "John Bowlby"),
                          ("de onderzoekster van de vreemde situatie", "Mary Ainsworth"),
                          ("het kind dat protesteert en zich daarna laat troosten",
                           "veilig gehecht"),
                          ("het kind dat niet reageert op het weggaan",
                           "onveilig vermijdend gehecht"),
                          ("het kind dat ontroostbaar blijft", "onveilig afwerend gehecht")],
                  "Vul aan.", WL),
                 ("open", "Waarom is een kind dat huilt als zijn mama weggaat, juist een goed "
                          "teken?",
                  "Het laat zien dat er een band is en dat het kind het verschil tussen bekend "
                  "en onbekend ziet. Wat telt is of het zich daarna laat troosten.", 3),
                 ("open", "Een kind in de opvang kijkt elke keer naar jou voor het iets nieuws "
                          "aandurft. Hoe noem je dat, en wat doe je?",
                  "Dat is de veilige basis. Je blijft zichtbaar en je moedigt aan, zodat het "
                  "kind durft. Je duwt het niet weg en je neemt het ook niet over.", 4),
             ]),
        dict(kop="Van samen spelen tot vriendschap",
             opdracht="Zet de spelvormen in de orde waarin ze zich ontwikkelen, van 1 tot 5.",
             oefeningen=[
                 ("rij", [("alleen spelen, zonder de anderen te zien", "1"),
                          ("toekijken naar wat anderen doen", "2"),
                          ("naast elkaar spelen met hetzelfde materiaal", "3"),
                          ("samen spelen maar elk zijn eigen ding", "4"),
                          ("samen spelen met een gezamenlijk plan", "5"),
                          ("de naam van de onderzoekster van deze reeks", "Mildred Parten")],
                  "Welke stap?", WL),
                 ("open", "Twee kleuters zitten naast elkaar in de zandbak en praten niet. "
                          "Spelen ze samen?",
                  "Dat is parallel spel: ze spelen naast elkaar, niet samen. Dat is normaal "
                  "voor die leeftijd en geen teken dat er iets mis is.", 3),
             ]),
        dict(kop="De adolescentie",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom wordt de mening van vrienden in de adolescentie "
                          "belangrijker dan die van ouders?",
                  "De jongere bouwt een eigen identiteit op, los van thuis. De groep is de "
                  "spiegel waarin hij zich meet. De ouders blijven wel het vangnet voor de "
                  "grote dingen.", 3),
                 ("open", "Noem drie dingen waaraan je merkt dat een jongere het moeilijk "
                          "heeft, en zeg bij wie je terechtkan.",
                  "Zich terugtrekken, slechter slapen, plots slechtere resultaten, de "
                  "vriendengroep laten vallen, veel prikkelbaarder zijn. Je gaat naar de "
                  "leerlingenbegeleiding, het CLB of de huisarts, en bij acuut gevaar bel je "
                  "112 of de Zelfmoordlijn op 1813.", 4),
             ]),
    ])


# ============================================================
zet("de-volwassene-en-de-oudere",
    titel="De volwassene en de oudere",
    reeksen=[
        dict(kop="Levensfasen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("ongeveer 18 tot 25 jaar", "de jonge volwassenheid"),
                          ("ongeveer 25 tot 40 jaar", "de vroege volwassenheid"),
                          ("ongeveer 40 tot 65 jaar", "de middelbare leeftijd"),
                          ("vanaf 65 jaar", "de oudere volwassenheid"),
                          ("vanaf ongeveer 80 jaar", "de hoogbejaarde leeftijd"),
                          ("de overgang waarin veel tegelijk verandert",
                           "een levensfaseovergang")],
                  "Welke fase?", WL),
                 ("rij", [("samenwonen of trouwen", "een mijlpaal van de vroege volwassenheid"),
                          ("de kinderen die het huis uit gaan", "het lege nest"),
                          ("zorgen voor de ouders én voor de kinderen",
                           "de sandwichgeneratie"),
                          ("stoppen met werken", "het pensioen"),
                          ("het verlies van een partner", "een rouwproces"),
                          ("de rol van grootouder", "een nieuwe rol, geen verlies")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="Ouder worden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de huid wordt dunner en droger", "een normaal verouderingsproces"),
                          ("minder goed zien in het donker", "normaal"),
                          ("hoge tonen slechter horen", "normaal, presbyacusis"),
                          ("de spiermassa die afneemt", "normaal, sarcopenie"),
                          ("de naam van zijn soms vergeten woord", "normaal"),
                          ("de weg naar huis niet meer vinden", "niet normaal, laat nakijken")],
                  "Normaal of niet?", WL),
                 ("open", "Wat is het verschil tussen gewone vergeetachtigheid en dementie?",
                  "Vergeetachtigheid hindert het dagelijkse leven niet en de persoon merkt het "
                  "zelf. Bij dementie gaat ook het plannen, het oriënteren en het herkennen "
                  "achteruit, en lukt het alleen wonen niet meer. Het is de arts die dat "
                  "vaststelt.", 4),
                 ("open", "Noem drie manieren om iemand met dementie te helpen zonder zijn "
                          "waardigheid aan te tasten.",
                  "Niet overhoren of verbeteren, meegaan in zijn beleving, één vraag per keer "
                  "stellen, vaste gewoonten en vaste plaatsen houden, en laten doen wat hij "
                  "nog zelf kan.", 4),
             ]),
        dict(kop="Zorg en zelfstandigheid",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom is zo lang mogelijk thuis blijven wonen niet voor iedereen "
                          "het beste?",
                  "Thuis blijven bij groot isolement of onveiligheid kan slechter uitvallen "
                  "dan een plaats waar er contact en toezicht is. Het hangt af van wat de "
                  "persoon zelf wil en van wat er rond hem staat.", 3),
                 ("open", "Een man van 82 weigert hulp bij het wassen, terwijl het duidelijk "
                          "niet meer gaat. Wat doe je?",
                  "Je vraagt waarom en zoekt een vorm waar hij wel mee kan leven: een "
                  "mannelijke hulp, wassen aan de lavabo, zelf doen wat hij kan. Je dwingt "
                  "niet en je legt het vast, en je overlegt met het team en de familie.", 4),
             ]),
    ])


# ============================================================
zet("waarnemen-en-observeren",
    titel="Waarnemen en observeren",
    reeksen=[
        dict(kop="Waarnemen is niet neutraal",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een vast beeld van een hele groep", "een stereotype"),
                          ("de eerste indruk die alles verder kleurt", "het eerste-indrukeffect"),
                          ("één goede eigenschap die de rest meesleept", "het haloeffect"),
                          ("enkel zien wat je verwachting bevestigt",
                           "de bevestigingsneiging"),
                          ("iemand beoordelen door hem te vergelijken met de vorige",
                           "het contrasteffect"),
                          ("iemand die zich gedraagt zoals men verwacht",
                           "een zelfvervullende voorspelling")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Je hoort van een collega dat een kind lastig is, nog voor je het "
                          "gezien hebt. Wat is het risico?",
                  "Je gaat dat gedrag zoeken en vinden, en je reageert er anders op. Het kind "
                  "voelt dat en gedraagt zich ernaar. Begin dus zelf met kijken.", 3),
             ]),
        dict(kop="Feit of interpretatie",
             opdracht="Zet achter elke uitspraak of ze een feit of een interpretatie is.",
             oefeningen=[
                 ("rij", [("Lotte zit tien minuten alleen aan de tafel.", "feit"),
                          ("Lotte is verlegen.", "interpretatie"),
                          ("Sam duwt de blokken van de toren.", "feit"),
                          ("Sam is agressief.", "interpretatie"),
                          ("Jonas kijkt drie keer naar de deur.", "feit"),
                          ("Jonas mist zijn mama.", "interpretatie")],
                  "Feit of interpretatie?", WW),
                 ("open", "Herschrijf als een feit: Noor is lui vandaag.",
                  "Noor legde haar hoofd twee keer op de bank en begon niet aan de opdracht "
                  "in de eerste tien minuten.", 3),
                 ("open", "Herschrijf als een feit: Milan zoekt aandacht.",
                  "Milan stond vier keer op en kwam telkens naast mij staan tijdens de "
                  "opdracht.", 3),
                 ("open", "Waarom mag een interpretatie wél in een verslag, zolang je ze als "
                          "interpretatie schrijft?",
                  "Jouw beeld is nuttig voor het team. Maar het moet herkenbaar zijn als "
                  "jouw beeld, zodat een collega het kan nagaan: schrijf wat je zag en daarna "
                  "wat je vermoedt.", 3),
             ]),
        dict(kop="Soorten observatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("je kijkt mee terwijl je meedoet",
                           "participerende observatie"),
                          ("je kijkt van buitenaf", "niet-participerende observatie"),
                          ("je noteert alles wat er gebeurt", "een open observatie"),
                          ("je kruist op een lijst af wat je ziet", "een gerichte observatie"),
                          ("je kijkt elke vijf minuten even", "een tijdsteekproef"),
                          ("je noteert enkel een bepaald gedrag", "een gebeurtenissteekproef")],
                  "Welke soort?", WL),
                 ("open", "Je wil weten hoe vaak een kind samen speelt. Welke observatievorm "
                          "kies je, en waarom?",
                  "Een tijdsteekproef: je kijkt op vaste momenten en noteert wat het kind net "
                  "doet. Zo krijg je een eerlijk beeld van de hele dag en niet enkel van de "
                  "momenten die jou opvallen.", 4),
             ]),
    ])


# ============================================================
zet("rapporteren-en-respectvol-omgaan",
    titel="Rapporteren en respectvol omgaan",
    reeksen=[
        dict(kop="Een goed verslag",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "In een verslag staat wat je zag, met datum en uur.", True),
                 ("waar", "Een verslag mag een oordeel bevatten, zolang het als jouw indruk "
                          "staat.", True),
                 ("waar", "Je noteert ook wat goed ging, niet alleen de problemen.", True),
                 ("waar", "Een verslag is geschreven voor de collega die het leest, dus in "
                          "gewone taal.", True),
                 ("waar", "Wat in een verslag staat, mag je thuis vertellen aan je gezin.",
                  False),
                 ("waar", "De ouders hebben recht op inzage in het dossier van hun kind.",
                  True),
             ]),
        dict(kop="Herschrijven",
             opdracht="Herschrijf elke zin zodat ze bruikbaar is in een verslag.",
             oefeningen=[
                 ("open", "Het was weer een ramp met Wout vandaag.",
                  "Wout verliet drie keer de kring tijdens het verhaal en gooide om 10.15 uur "
                  "een bakje met stiften van de tafel.", 3),
                 ("open", "De mama van Yara werkt niet mee.",
                  "De mama van Yara antwoordde niet op de twee berichten van 3 en 5 oktober "
                  "over het oudergesprek.", 3),
                 ("open", "Dat kind is duidelijk niet opgevoed.",
                  "Die zin hoort niet in een verslag: ze beoordeelt het gezin en is niet na te "
                  "gaan. Schrijf wat je zag: Elias at met zijn handen en stond tijdens de "
                  "maaltijd vijf keer op.", 4),
                 ("open", "Waarom is dat laatste zo belangrijk?",
                  "Een verslag gaat mee in een dossier en wordt jaren later gelezen. Een "
                  "oordeel over een gezin blijft daar staan en bepaalt hoe anderen naar dat "
                  "kind kijken.", 3),
             ]),
        dict(kop="Beroepsgeheim en privacy",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Een buurvrouw vraagt in de winkel hoe het met een bewoner gaat. Wat "
                          "zeg je?",
                  "Je zegt dat je daar niets over kan zeggen, vriendelijk maar duidelijk, en "
                  "je verwijst naar de familie. Ook bevestigen dat iemand er woont, is al een "
                  "schending.", 3),
                 ("open", "Wanneer mag je het beroepsgeheim doorbreken?",
                  "Bij een ernstig en dringend gevaar voor de persoon of voor iemand anders, "
                  "en dan nog zo beperkt mogelijk en liefst in overleg met je "
                  "verantwoordelijke. Dat heet de noodtoestand.", 4),
                 ("open", "Mag je een foto van een kind uit de opvang op je eigen sociale "
                          "media zetten?",
                  "Nee. Daarvoor is de schriftelijke toestemming van de ouders nodig, en zelfs "
                  "dan hoort dat op het kanaal van de organisatie en niet op je eigen "
                  "profiel.", 3),
             ]),
    ])


# ============================================================
zet("gedrag-en-behoeften",
    titel="Gedrag en behoeften",
    reeksen=[
        dict(kop="Achter het gedrag",
             opdracht="Zet achter elk gedrag een mogelijke behoefte erachter.",
             oefeningen=[
                 ("rij", [("een kind dat de blokken van een ander omgooit",
                           "meespelen maar niet weten hoe"),
                          ("een kind dat bij elke opdracht zegt dat het niet kan",
                           "bevestiging en een haalbare stap"),
                          ("een kind dat de clown uithangt", "erbij horen, gezien worden"),
                          ("een kleuter die plots weer in zijn broek plast",
                           "veiligheid, bij een verandering thuis"),
                          ("een tiener die niets meer zegt", "rust, of iets wat te zwaar is"),
                          ("een bewoner die elke dag belt om niets", "contact en nabijheid")],
                  "Welke behoefte?", WL),
                 ("open", "Waarom helpt straffen weinig als het gedrag uit een behoefte komt?",
                  "De behoefte blijft. Het kind zoekt dan een andere manier, vaak een lastigere. "
                  "Je moet de behoefte zelf een plaats geven.", 3),
             ]),
        dict(kop="Grenzen stellen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de regel vooraf duidelijk zeggen", "voorspelbaarheid"),
                          ("dezelfde regel bij dezelfde situatie", "consequent zijn"),
                          ("het gedrag afkeuren, niet het kind", "scheiden van persoon en gedrag"),
                          ("een keuze geven binnen de grens", "autonomie binnen de regel"),
                          ("zeggen wat je wél wil zien", "positief formuleren"),
                          ("de regel samen met de groep maken", "participatie")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Herschrijf positief: niet lopen in de gang.",
                  "In de gang stappen we.", 2),
                 ("open", "Herschrijf positief: stop met roepen.",
                  "Praat met je binnenstem.", 2),
                 ("open", "Herschrijf als een keuze binnen de grens: je gaat nu opruimen.",
                  "Ruim je eerst de blokken op of eerst de boeken?", 2),
             ]),
        dict(kop="Een situatie aanpakken",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Twee kinderen vechten om dezelfde step. Wat doe je, stap voor stap?",
                  "Eerst de veiligheid: je gaat ertussen. Dan benoem je wat je ziet en wat "
                  "iedereen wil. Dan laat je hen zelf een oplossing zoeken, met een beurtrol "
                  "of een zandloper als ze het niet vinden. Achteraf kom je er kort op terug.",
                  5),
                 ("open", "Een kind weigert aan tafel te komen. Noem twee aanpakken die "
                          "werken en één die niet werkt.",
                  "Werkt: een verwittiging vooraf dat het bijna tijd is, en een keuze geven "
                  "over hoe het komt. Werkt niet: een machtsstrijd aangaan of het eten als "
                  "straf gebruiken.", 4),
             ]),
    ])


# ============================================================
zet("communiceren-en-actief-luisteren",
    titel="Communiceren en actief luisteren",
    reeksen=[
        dict(kop="Het model",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("wie de boodschap stuurt", "de zender"),
                          ("wie ze ontvangt", "de ontvanger"),
                          ("de weg waarlangs ze gaat", "het kanaal"),
                          ("de boodschap in woorden zetten", "coderen"),
                          ("de boodschap begrijpen", "decoderen"),
                          ("wat de ontvanger terugstuurt", "feedback")],
                  "Hoe noemen we dit?", WL),
                 ("rij", [("de woorden zelf", "verbale communicatie"),
                          ("de houding, de blik en de toon", "non-verbale communicatie"),
                          ("wat de zinnen zeggen", "de inhoud"),
                          ("wat de toon over jullie band zegt", "de relatie"),
                          ("de ruis die het verstoort", "storingen"),
                          ("wat telt als woorden en toon tegenstrijdig zijn",
                           "de toon, die wint bijna altijd")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Actief luisteren",
             opdracht="Zet achter elke reactie welke luistervaardigheid het is.",
             oefeningen=[
                 ("rij", [("Dus je bedoelt dat je je uitgesloten voelde?", "parafraseren"),
                          ("Je klinkt echt kwaad.", "gevoelsreflectie"),
                          ("Hm, ja. Vertel verder.", "aanmoedigen"),
                          ("Wat gebeurde er daarna?", "doorvragen"),
                          ("Even samenvatten: eerst dit, dan dat.", "samenvatten"),
                          ("Niets zeggen en wachten", "stilte laten")],
                  "Welke vaardigheid?", WL),
                 ("open", "Waarom is dat ken ik, bij mij was het ook zo geen goede reactie?",
                  "Je zet het gesprek op jezelf. De ander moest zijn verhaal vertellen en "
                  "mag nu naar jou luisteren.", 3),
                 ("open", "Een bewoner zegt dat ze er niets meer aan vindt. Schrijf twee "
                          "reacties op: een die het gesprek opent en een die het sluit.",
                  "Opent: U klinkt moedeloos. Wat is er veranderd? Sluit: Kom, zo erg is het "
                  "niet, morgen is er weer een dag. Bij zinnen die naar levensmoeheid "
                  "verwijzen, meld je het ook aan je verantwoordelijke.", 4),
             ]),
        dict(kop="Praten met wie moeilijk praat",
             opdracht="Schrijf bij elke situatie op wat je aanpast.",
             oefeningen=[
                 ("rij", [("een kind van twee", "korte zinnen, één opdracht, op ooghoogte"),
                          ("iemand die slecht hoort", "gezicht tonen, rustig, geen lawaai"),
                          ("iemand met dementie", "één vraag per keer, geen overhoring"),
                          ("iemand die onze taal pas leert", "eenvoudige woorden, tekenen, "
                           "nooit luider"),
                          ("een jongere die dichtklapt", "naast hem gaan zitten, niet "
                           "aandringen"),
                          ("iemand die kwaad is", "eerst het gevoel benoemen, dan de inhoud")],
                  "Wat pas je aan?", WL),
                 ("open", "Waarom is luider praten tegen wie onze taal pas leert geen oplossing?",
                  "Het probleem is niet het volume maar de woorden. Spreek trager, kies "
                  "eenvoudige woorden, gebruik je handen en een tekening, en ga na of het "
                  "aangekomen is.", 3),
             ]),
    ])


# ============================================================
zet("feedback-en-verbindend-communiceren",
    titel="Feedback en verbindend communiceren",
    reeksen=[
        dict(kop="De ik-boodschap",
             opdracht="Een ik-boodschap heeft vier delen: het gedrag, het gevolg, je gevoel en "
                      "je wens. Vul aan.",
             oefeningen=[
                 ("rij", [("wat je zag, zonder oordeel", "het gedrag"),
                          ("wat dat met het werk of de groep doet", "het gevolg"),
                          ("wat het met jou doet", "je gevoel"),
                          ("wat je graag anders ziet", "je wens"),
                          ("waarom je met ik begint", "je spreekt voor jezelf, niet over hem"),
                          ("waarom je altijd en nooit vermijdt",
                           "dat is een verwijt en niet na te gaan")],
                  "Welk deel?", WL),
                 ("open", "Herschrijf als ik-boodschap: je ruimt nooit iets op.",
                  "Ik zie dat het materiaal van vanmorgen nog op de tafel staat. Daardoor kan "
                  "de volgende groep niet beginnen en voel ik me gehaast. Ik zou graag dat je "
                  "na je activiteit opruimt.", 4),
                 ("open", "Herschrijf als ik-boodschap: je bent altijd te laat.",
                  "Je was deze week drie keer een kwartier later dan afgesproken. Daardoor "
                  "sta ik alleen bij het onthaal en dat is te zwaar. Ik wil graag dat je om "
                  "acht uur begint.", 4),
             ]),
        dict(kop="Feedback geven en krijgen",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Feedback gaat over gedrag, niet over iemands karakter.", True),
                 ("waar", "Feedback geef je zo snel mogelijk na het gedrag.", True),
                 ("waar", "Feedback geef je het best waar de hele groep bij is.", False),
                 ("waar", "Wie feedback krijgt, hoeft niet meteen te antwoorden.", True),
                 ("waar", "Positieve feedback is niet nodig, want dat gaat toch goed.", False),
                 ("waar", "Feedback is pas af als de ander kon zeggen hoe hij het ziet.",
                  True),
             ]),
        dict(kop="Verbindend communiceren",
             opdracht="De vier stappen van verbindende communicatie zijn observatie, gevoel, "
                      "behoefte en verzoek. Werk ze uit.",
             oefeningen=[
                 ("open", "Een collega onderbreekt je telkens in het teamoverleg. Werk de vier "
                          "stappen uit.",
                  "Observatie: in het overleg van vandaag werd ik drie keer onderbroken "
                  "voordat ik mijn zin afmaakte. Gevoel: ik voelde me daar ongemakkelijk bij. "
                  "Behoefte: ik heb nodig dat mijn inbreng gehoord wordt. Verzoek: wil je me "
                  "laten uitspreken en dan reageren?", 8),
                 ("open", "Wat is het verschil tussen een verzoek en een eis?",
                  "Bij een verzoek kan de ander ook nee zeggen, en dan zoek je verder. Bij een "
                  "eis volgt er een straf of verwijt op dat nee.", 3),
                 ("open", "Waarom is ik voel dat je me niet respecteert geen gevoel?",
                  "Na ik voel dat volgt een gedachte over de ander, geen gevoel. Een gevoel is "
                  "een woord zoals verdrietig, kwaad of onzeker.", 3),
             ]),
    ])


# ============================================================
zet("vrije-tijd-spel-en-expressie",
    titel="Vrije tijd, spel en expressie",
    reeksen=[
        dict(kop="Waarom spelen",
             opdracht="Zet achter elke spelvorm wat het kind erbij leert.",
             oefeningen=[
                 ("rij", [("met blokken bouwen", "ruimtelijk inzicht en fijne motoriek"),
                          ("winkeltje spelen", "taal, rollen en samenwerken"),
                          ("verstoppertje", "regels volgen en wachten"),
                          ("met water en zand", "oorzaak en gevolg, en zintuigen"),
                          ("een gezelschapsspel", "zijn toer afwachten en verliezen"),
                          ("vrij tekenen", "zichzelf uitdrukken")],
                  "Wat leert het kind?", WL),
                 ("open", "Waarom is vrij spel zonder opdracht ook leren?",
                  "Het kind kiest zelf, probeert, mislukt en probeert opnieuw. Dat is precies "
                  "hoe het denkt en zijn fantasie oefent, zonder dat iemand het resultaat "
                  "bepaalt.", 3),
             ]),
        dict(kop="Vrije tijd",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de tijd buiten school en zorg", "de vrije tijd"),
                          ("de vereniging die een aanbod doet", "de jeugdbeweging of de club"),
                          ("de opvang voor en na school", "de buitenschoolse opvang"),
                          ("het aanbod in de vakantie", "een kamp of een speelplein"),
                          ("de drempel van de kostprijs", "een financiële drempel"),
                          ("een korting voor wie het nodig heeft",
                           "een sociaal tarief of de UiTPAS")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Noem drie drempels die een kind uit een gezin met weinig geld "
                          "tegenhouden om naar een club te gaan, en één oplossing per "
                          "drempel.",
                  "De kostprijs, op te lossen met een sociaal tarief of de UiTPAS. Het "
                  "vervoer, op te lossen met samen rijden of een club in de buurt. Het "
                  "materiaal, op te lossen met een uitleendienst of tweedehands. En niet "
                  "weten wat er bestaat, op te lossen met iemand die mee gaat kijken.", 5),
             ]),
        dict(kop="Expressie",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("tekenen, kleuren en kleien", "beeldende expressie"),
                          ("zingen en met instrumenten spelen", "muzikale expressie"),
                          ("dansen en bewegen op muziek", "bewegingsexpressie"),
                          ("toneel en rollenspel", "dramatische expressie"),
                          ("vertellen en verzinnen", "verbale expressie"),
                          ("wat alle vormen gemeen hebben",
                           "er is geen juist of fout resultaat")],
                  "Welke vorm?", WL),
                 ("open", "Een kind tekent de lucht groen. Wat zeg je?",
                  "Je vraagt wat je ziet op de tekening en je laat het kind vertellen. Je "
                  "verbetert niet: bij expressie is er geen fout, en zodra je verbetert tekent "
                  "het kind nog wat jij wil zien.", 3),
                 ("open", "Waarom hang je het werk van álle kinderen op en niet enkel het "
                          "mooiste?",
                  "Expressie is geen wedstrijd. Wie nooit hangt, leert dat zijn werk niet "
                  "goed genoeg is en houdt op met proberen.", 3),
             ]),
    ])


# ============================================================
zet("spelvormen-en-speelgoed",
    titel="Spelvormen en speelgoed",
    reeksen=[
        dict(kop="Spelvormen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("rammelen, voelen en in de mond stoppen", "sensomotorisch spel"),
                          ("met blokken en duplo bouwen", "constructiespel"),
                          ("mama en papa spelen", "rollenspel of fantasiespel"),
                          ("een spel met afgesproken regels", "regelspel"),
                          ("tekenen en kleien", "creatief spel"),
                          ("ravotten en klimmen", "bewegingsspel")],
                  "Welke spelvorm?", WL),
                 ("rij", [("de spelvorm van een baby", "sensomotorisch spel"),
                          ("de spelvorm die rond 2 jaar begint", "fantasiespel"),
                          ("de spelvorm die regels vraagt en dus rond 4 jaar komt",
                           "regelspel"),
                          ("de spelvorm die een hele namiddag kan duren", "rollenspel"),
                          ("de spelvorm die het meest op later lijkt", "rollenspel"),
                          ("wat er met de oude spelvormen gebeurt",
                           "ze verdwijnen niet, ze blijven ernaast bestaan")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Speelgoed kiezen",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Het CE-merkteken betekent dat het speelgoed aan de Europese "
                          "veiligheidseisen voldoet.", True),
                 ("waar", "Het teken met 0 tot 3 jaar in een cirkel met een streep betekent "
                          "dat het niet geschikt is onder drie jaar.", True),
                 ("waar", "Speelgoed met veel mogelijkheden en weinig functies is vaak "
                          "waardevoller dan speelgoed dat alles zelf doet.", True),
                 ("waar", "Duurder speelgoed is pedagogisch beter.", False),
                 ("waar", "Een kartonnen doos is geen echt speelgoed.", False),
                 ("waar", "Kleine onderdeeltjes zijn onder drie jaar een verstikkingsrisico.",
                  True),
             ]),
        dict(kop="Een activiteit uitwerken",
             opdracht="Werk de activiteit volledig uit.",
             oefeningen=[
                 ("open", "Werk een activiteit van twintig minuten uit voor vijf kleuters van "
                          "vier jaar, met een kartonnen doos en wat je in een gewone opvang "
                          "vindt. Schrijf het doel, het materiaal, het verloop en wat je doet "
                          "als het misloopt.",
                  "Een goed antwoord heeft een doel dat bij vier jaar past (samen iets maken, "
                  "om de beurt gaan), een materiaallijst, een verloop in drie delen "
                  "(inleiding, kern, afronding met opruimen), en een plan B: wat als twee "
                  "kinderen vechten om de doos, of als het na vijf minuten gedaan is.", 12),
                 ("open", "Waarom hoort opruimen bij de activiteit en niet erna?",
                  "Het is deel van het spel en van wat het kind leert. Wie het als een straf "
                  "na het leuke zet, krijgt elke keer tegenstand.", 3),
             ]),
    ])


# ============================================================
zet("activiteiten-voor-volwassenen",
    titel="Activiteiten voor volwassenen",
    reeksen=[
        dict(kop="Waarom activiteiten",
             opdracht="Zet achter elk doel een activiteit die daarbij past.",
             oefeningen=[
                 ("rij", [("de fijne motoriek onderhouden", "bloemschikken of bakken"),
                          ("het geheugen aanspreken", "een quiz over vroeger"),
                          ("in beweging blijven", "zitgymnastiek of een wandeling"),
                          ("contact met anderen", "samen koffie en een gesprekstafel"),
                          ("iets betekenen voor anderen", "mee de tafel dekken of de plantjes"),
                          ("de zintuigen prikkelen", "geuren raden of muziek van toen")],
                  "Welke activiteit?", WL),
                 ("open", "Waarom is een activiteit waarbij iemand iets voor anderen doet, "
                          "vaak de meest waardevolle?",
                  "Dan is de persoon niet degene die vermaakt wordt maar degene die iets "
                  "bijdraagt. Dat raakt het gevoel van waarde en niet enkel de tijd.", 3),
             ]),
        dict(kop="Aanpassen aan wie er zit",
             opdracht="Schrijf bij elke situatie op wat je aanpast.",
             oefeningen=[
                 ("rij", [("iemand met beperkt zicht", "grote letters, veel licht, benoemen "
                           "wat er gebeurt"),
                          ("iemand met beperkt gehoor", "stille ruimte, gezicht tonen, "
                           "visuele steun"),
                          ("iemand in een rolstoel", "de tafelhoogte en de plaats aan de tafel"),
                          ("iemand met beginnende dementie",
                           "korte opdracht, geen competitie, geen overhoring"),
                          ("iemand die snel moe is", "kortere duur en de mogelijkheid te stoppen"),
                          ("iemand die niet mee wil doen", "laten toekijken, niets forceren")],
                  "Wat pas je aan?", WL),
                 ("open", "Waarom is een quiz over de actualiteit een slechte keuze voor een "
                          "groep met dementie?",
                  "Het confronteert hen met wat ze niet meer weten en dat geeft faalangst en "
                  "schaamte. Vragen over het verre verleden of over herkenbare liedjes werken "
                  "wel, want dat geheugen blijft langer.", 4),
             ]),
        dict(kop="Een activiteit uitwerken",
             opdracht="Werk de activiteit volledig uit.",
             oefeningen=[
                 ("open", "Werk een activiteit van drie kwartier uit voor acht bewoners van "
                          "een woonzorgcentrum, waarvan twee in een rolstoel en één met "
                          "beginnende dementie. Schrijf het doel, het materiaal, het verloop, "
                          "de aanpassingen per bewoner en hoe je afsluit.",
                  "Een goed antwoord kiest iets zonder winnaars en verliezers, bijvoorbeeld "
                  "samen soep maken of een gesprekstafel met voorwerpen van vroeger. Het "
                  "noemt de opstelling (een ronde tafel waar een rolstoel bij kan), de duur in "
                  "delen met een pauze, één aanpassing per bewoner, en een afsluiting waarin "
                  "iedereen iets zegt of iets mee naar de kamer neemt.", 12),
                 ("open", "Wat schrijf je achteraf op, en voor wie?",
                  "Wie meedeed, wat lukte en wat niet, en wat je volgende keer anders doet. "
                  "Voor je collega's en voor de opvolging van elke bewoner, in feiten en niet "
                  "in oordelen.", 3),
             ]),
    ])

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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-welzijn-en-welbevinden-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie woorden die op elkaar lijken en drie verschillende dingen betekenen. "
                   "Welvaart gaat over middelen, welzijn over de omstandigheden, welbevinden over "
                   "het gevoel van de persoon zelf. Daarnaast de drie basisbehoeften: autonomie, "
                   "competentie en verbondenheid.",
            waarom=[
                None,
                "Geef een voorbeeld waarin de twee uiteenlopen, en niet een waarin ze samengaan. "
                "Dat is net het punt: meer middelen helpen, maar ze beslissen niet. Omgekeerd kan "
                "een kind met weinig geld een hoog welbevinden hebben.",
            ],
        ),
        dict(
            aanpak="De drie basisbehoeften hebben elk hun eigen woord in de situatie. Mag ik zelf "
                   "kiezen is autonomie, kan ik dit is competentie, hoor ik erbij is "
                   "verbondenheid. Zoek dus niet wat het kind voelt maar wat het mist.",
            waarom=[
                "Let op de twee lijnen over autonomie: nooit zelf mogen kiezen en van thuis uit "
                "alles moeten. Het is dezelfde behoefte, één keer op school en één keer thuis. "
                "Daarom kan een kind dat thuis niets mag kiezen op school juist alles willen "
                "beslissen.",
                "Drie van de genoemde volstaan. Ze hebben alle hetzelfde kenmerk: je verandert "
                "de omstandigheden en niet het kind. Dwingen werkt hier nooit, want meedoen onder "
                "druk voelt niet als erbij horen.",
            ],
        ),
        dict(
            aanpak="De piramide van Maslow heeft vijf lagen, van lichamelijk onderaan tot "
                   "zelfontplooiing bovenaan. Ken de orde, maar ken ook de kritiek: op een examen "
                   "wordt bijna altijd allebei gevraagd.",
            waarom=[
                None,
                "Noem beide delen, want het antwoord is maar half zonder de kritiek. Het model "
                "helpt om te zien waarom een hongerig kind niet kan leren, maar de lagen volgen "
                "niet zo strikt op elkaar: mensen in moeilijke omstandigheden zoeken even hard "
                "naar verbinding en betekenis.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-wat-bepaalt-onze-gezondheid-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier soorten determinanten, en de toets is wie of wat eraan kan sleutelen. "
                   "Persoonlijk zit in de persoon en is meestal onveranderlijk, leefstijl is "
                   "gedrag, omgeving is alles errond, en het zorgstelsel gaat over de "
                   "beschikbaarheid van zorg.",
            waarom=[
                "Werkloosheid in het gezin staat bij omgeving en niet bij persoonlijk. Dat is "
                "belangrijk: het is geen eigenschap van het kind, en toch beïnvloedt het zijn "
                "gezondheid sterker dan de meeste eigen keuzes.",
                "Let op de laatste zin van het antwoord, want daar zit de kern van het hoofdstuk. "
                "Wie enkel naar de leefstijl kijkt, legt de hele verantwoordelijkheid bij de "
                "persoon terwijl drie van de vier determinanten buiten hem liggen.",
            ],
        ),
        dict(
            aanpak="De gezondheidskloof is geen kloof tussen arm en rijk maar een trap: bij elke "
                   "stap hoger in opleiding of inkomen leeft men gemiddeld langer. Antwoord bij "
                   "deze reeks dus altijd met meer dan de eigen keuze: met prijs, afstand, tijd "
                   "en omgeving.",
            waarom=[
                "Het woord gradiënt is hier het juiste woord: het gaat niet om twee groepen maar "
                "om een geleidelijk verloop. Ook wie het goed heeft, leeft gemiddeld korter dan "
                "wie het nóg beter heeft.",
                "Noem alle drie de redenen, want ze zijn van een andere soort: geld, afstand en "
                "tijd. Dat derde wordt het vaakst vergeten en weegt zwaar bij wie onregelmatige "
                "uren werkt.",
                "Twee volstaan. Twee Belgische maatregelen die je bij naam kan noemen, zijn de "
                "maximumfactuur, die begrenst wat een gezin per jaar aan zorg betaalt, en de "
                "regeling derdebetaler, waarbij je bij de huisarts enkel het eigen deel betaalt.",
            ],
        ),
        dict(
            aanpak="Houd twee soorten aanpak uit elkaar: een campagne of voorlichting spreekt de "
                   "persoon aan, een structurele maatregel verandert de omgeving. Het tweede werkt "
                   "beter, omdat het de gezonde keuze de gemakkelijkste maakt in plaats van de "
                   "moeilijkste.",
            waarom=[
                None,
                "Dit is het hele hoofdstuk in één voorbeeld. Een affiche zonder aanbod vraagt iets "
                "wat ter plaatse niet kan, en de leerling die het niet doet, krijgt dan nog het "
                "verwijt erbovenop.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ontwikkeling-de-basisbegrippen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De twee richtingen van de ontwikkeling zijn het lastigste van deze bundel. "
                   "Cefalocaudaal gaat van het hoofd naar de voeten: een baby houdt eerst zijn "
                   "hoofd recht en stapt veel later. Proximodistaal gaat van de romp naar buiten: "
                   "eerst de arm bewegen, dan grijpen met de hand, dan met twee vingers.",
            waarom=[
                "Reken het aan een baby na: eerst het hoofd, dan rollen, dan zitten, dan stappen. "
                "Dat is cefalocaudaal. En eerst met de hele arm zwaaien, dan met de hand grijpen, "
                "dan met duim en vinger een kruimel oppakken. Dat is proximodistaal.",
                "Let op regressie, want dat is geen achteruitgang maar iets normaals: een kind "
                "dat net leerde stappen, wil weer gedragen worden, en een kind dat naar school "
                "gaat, kan weer in bed plassen. Een stap vooruit kost veel, en dan valt iets "
                "anders even terug.",
            ],
        ),
        dict(
            aanpak="Vier domeinen, en één vraag per mijlpaal: gaat het over bewegen, over denken, "
                   "over voelen en omgaan met anderen, of over woorden? Let erop dat een mijlpaal "
                   "in twee domeinen kan vallen, zoals zijn naam schrijven.",
            waarom=[
                "Op zijn toer wachten staat bij socio-emotioneel en niet bij cognitief. Het kind "
                "begrijpt de regel misschien al veel eerder; het kunnen wachten is het "
                "moeilijke, en dat is zelfbeheersing.",
                "Let op de laatste zin van het antwoord: dit is een vraag voor de arts of het "
                "CLB. Je taak is opmerken en doorverwijzen, niet zelf een oorzaak vaststellen.",
            ],
        ),
        dict(
            aanpak="De laatste twee oefeningen hebben hetzelfde antwoord in twee vormen: "
                   "erfelijkheid en omgeving werken altijd samen. Antwoord dus nooit met een "
                   "percentage of met een van de twee, maar met de manier waarop ze op elkaar "
                   "ingrijpen.",
            waarom=[
                None,
                "Het sterkste deel van dit antwoord is dat twee kinderen in hetzelfde gezin niet "
                "dezelfde omgeving hebben. De oudste groeide op bij jongere ouders zonder "
                "broers, de jongste bij ervaren ouders met een grote broer erbij. Hetzelfde huis "
                "is dus niet dezelfde opvoeding.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-fysieke-en-motorische-ontwikkeling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de mijlpalen aan een paar vaste ankers: hoofd rechthouden rond drie "
                   "maanden, zitten rond een half jaar, stappen rond een jaar. Daartussen kan je "
                   "de rest inschatten. De orde van de stappen is wat telt; de leeftijd is een "
                   "gemiddelde.",
            waarom=[
                None,
                "Dit is de belangrijkste zin van de hele bundel. Een kind dat later stapt maar de "
                "stappen in de juiste orde zet, ontwikkelt normaal. Zorgwekkend is pas het "
                "overslaan van een stap of een stilstand.",
            ],
        ),
        dict(
            aanpak="Grove motoriek is de grote beweging met romp, armen en benen; fijne motoriek "
                   "is het werk van de handen en de vingers. De twee grepen horen bij de fijne: "
                   "eerst met de hele hand, veel later met duim en wijsvinger.",
            waarom=[
                "De palmaire greep komt rond een half jaar, de pincetgreep rond negen à twaalf "
                "maanden. Dat verschil is precies de proximodistale richting in actie: van de "
                "hele hand naar twee vingers.",
                None,
                "Drie van de genoemde volstaan, en let op de opdracht: zonder werkblad. Fijne "
                "motoriek oefen je het best met echte dingen die weerstand geven, zoals deeg, "
                "knopen en wasknijpers, en niet met een kleurplaat.",
            ],
        ),
        dict(
            aanpak="Bij de groei gaat het niet om één meting maar om een lijn. Een percentiel "
                   "zegt waar een kind staat tegenover andere kinderen van die leeftijd; het "
                   "verloop van de eigen lijn zegt of de groei goed gaat.",
            waarom=[
                "De P50 is de middelste lijn, dus de helft van de kinderen zit erboven en de "
                "helft eronder. Op de P10 zitten betekent dus niet achterstand: één kind op tien "
                "zit daar of lager, en dat zijn gewoon de kleinere kinderen.",
                "Dit is het hele hoofdstuk in één vraag. Een laag percentiel is geen probleem, "
                "een afbuiging van de eigen lijn wel. Daarom zet een arts elke meting uit op de "
                "curve en kijkt hij naar de richting en niet naar het punt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-denken-volgens-piaget-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier stadia met vier leeftijden en vier kenmerken. Onthoud ze aan hun "
                   "kernwoord: sensomotorisch is doen en objectpermanentie, pre-operationeel is "
                   "egocentrisch en fantasie, concreet-operationeel is logisch met echte dingen, "
                   "formeel-operationeel is denken over het mogelijke.",
            waarom=[
                None,
                "Let op animisme: dat een pop pijn kan hebben, is geen vergissing maar hoort bij "
                "het pre-operationele denken. En egocentrisch betekent hier niet egoïstisch maar "
                "dat het kind nog niet kan bedenken dat jij iets anders ziet dan het zelf.",
            ],
        ),
        dict(
            aanpak="De begrippen van Piaget horen bij elkaar in een beweging: je hebt een schema, "
                   "iets nieuws past erin (assimilatie) of past er niet in zodat het schema "
                   "verandert (accommodatie), en daartussen zoekt het kind evenwicht. Vraag je "
                   "dus telkens af of het schema zelf verandert.",
            waarom=[
                None,
                "Dit is het beste voorbeeld om de twee uit elkaar te houden. Zolang de geit een "
                "hond heet, verandert het schema niet en is het assimilatie; zodra er een nieuw "
                "schema ontstaat, is het accommodatie. Zo gebeurt leren volgens Piaget altijd in "
                "die twee stappen.",
            ],
        ),
        dict(
            aanpak="De proefjes vragen altijd hetzelfde: wat zegt het kind, en waarom zegt het "
                   "dat? Antwoord dus niet dat het fout is, maar leg uit op welk kenmerk het "
                   "kind let, meestal maar op één: de hoogte of de lengte. En ken de kritiek op "
                   "Piaget.",
            waarom=[
                None,
                "Reken mee met wat het kind doet: het telt niet maar kijkt naar de lengte van de "
                "rij. Wil je weten of het al conservatie heeft, dan laat je het eerst zelf tellen "
                "en vraag je het daarna opnieuw.",
                "Noem beide delen van de kritiek. Met eenvoudiger opstellingen, bijvoorbeeld met "
                "snoepjes in plaats van knopen, blijken kinderen veel eerder te slagen; Piaget "
                "mat dus ook of ze zijn vraag begrepen. En de stadia lopen vloeiender in elkaar "
                "over dan hij schreef.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kohlberg-en-erikson-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij Kohlberg telt niet wat iemand besluit maar waarom. De zes niveaus lopen "
                   "van buiten naar binnen: eerst om de straf, dan om het eigenbelang, dan om wat "
                   "anderen vinden, dan om de wet, en ten slotte om beginselen die boven de wet "
                   "staan. Zoek dus de reden in het antwoord.",
            waarom=[
                "Let op het verschil tussen niveau 4 en 5. Bij vier is de wet het laatste woord; "
                "bij vijf kan je bedenken dat een wet slecht is en veranderd hoort te worden, "
                "omdat ze maar een afspraak tussen mensen is.",
                "De drie fasen zijn de paren: preconventioneel voor de afspraak, conventioneel "
                "volgens de afspraak, postconventioneel boven de afspraak. Zo zijn de namen ook "
                "te onthouden.",
                "Noem alle drie de punten, want ze zijn van een andere soort. Het eerste gaat "
                "over wie hij onderzocht, het tweede over zijn maatstaf, en het derde is het "
                "scherpste: zeggen wat juist is en het ook doen, zijn twee verschillende dingen.",
            ],
        ),
        dict(
            aanpak="Erikson heeft acht fasen, en elke fase is een tegenstelling waartussen een "
                   "mens iets moet vinden. Leer ze in paren: de tegenstelling én de leeftijd. "
                   "Let erop dat de laatste drie over de volwassenheid gaan, want daarin "
                   "verschilt Erikson van Piaget.",
            waarom=[
                "Merk op dat elke tegenstelling twee kanten heeft en dat niet enkel de goede kant "
                "bestaat. Een kind heeft ook wat wantrouwen nodig, en een tiener wat verwarring; "
                "het gaat om het evenwicht en niet om het uitbannen van de tweede helft.",
                "De laatste twee fasen zijn wat Erikson eigen maakt: ontwikkeling stopt niet bij "
                "de volwassenheid. Generativiteit is iets doorgeven, aan kinderen, aan leerlingen "
                "of aan werk dat blijft; het tegendeel is stilstand.",
            ],
        ),
        dict(
            aanpak="Bij een toepassing wordt altijd twee dingen gevraagd: welke fase, en wat je "
                   "doet. Dat tweede moet bij de fase passen. Bij autonomie geef je ruimte binnen "
                   "grenzen, bij identiteit geef je rust en een vast punt om op terug te vallen.",
            waarom=[
                "Let op de vorm van het antwoord: je neemt het niet over en je laat het ook niet "
                "worstelen tot het huilt. Een stuk geven dat hij wel kan, is het midden, en "
                "precies dat is wat autonomie tegenover schaamte betekent.",
                "Het antwoord is nee, en de reden is dat uitproberen de taak van die fase is. "
                "Zorgwekkend wordt het pas bij iets anders: als de jongere zich volledig "
                "terugtrekt, of als hij in een groep terechtkomt die hem schaadt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-socio-emotionele-ontwikkeling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij gehechtheid telt niet of een kind huilt maar wat er daarna gebeurt. Een "
                   "veilig gehecht kind protesteert én laat zich troosten. De twee onveilige "
                   "vormen zijn de uitersten daarvan: het ene reageert niet, het andere blijft "
                   "ontroostbaar.",
            waarom=[
                "Houd de twee namen bij hun werk: Bowlby bedacht de theorie, Ainsworth bouwde de "
                "proef, de vreemde situatie. Die proef kijkt niet naar het weggaan maar naar het "
                "weerzien, en dat is het hele idee.",
                None,
                "Het begrip veilige basis is de kern van de hele bundel. Een kind durft de wereld "
                "in omdat het weet waar het kan terugkomen. Daarom is zichtbaar blijven meer "
                "waard dan aanmoedigen met woorden.",
            ],
        ),
        dict(
            aanpak="De spelvormen gaan van alleen naar samen, in vijf stappen. Zoek bij elke "
                   "omschrijving twee dingen: zien ze elkaar, en hebben ze een gezamenlijk plan? "
                   "Met die twee vragen zet je de hele rij in de juiste orde.",
            waarom=[
                None,
                "Dit is de nuttigste vraag van de bundel voor wie in de opvang staat. Parallel "
                "spel ziet uit als niet samen spelen, maar het is de gewone stap voor het echte "
                "samenspel. Ingrijpen is daar dus niet nodig.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over de adolescentie. Antwoord bij de tweede oefening "
                   "met zichtbare veranderingen en niet met gevoelens, en noem altijd ook waar je "
                   "terechtkan: in een opleiding zorg wordt dat tweede deel verwacht.",
            waarom=[
                "Let op de laatste zin: de ouders blijven het vangnet. Dat vrienden belangrijker "
                "worden, betekent niet dat de ouders niet meer tellen; voor de grote dingen "
                "komt een jongere nog altijd thuis.",
                "Drie van de genoemde volstaan. Wat ze gemeen hebben, is dat het veranderingen "
                "zijn tegenover hoe die jongere eerder was: niet stil zijn is het signaal, maar "
                "stiller worden dan anders. En het nummer van de Zelfmoordlijn, 1813, hoort erbij.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-volwassene-en-de-oudere-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De levensfasen hebben leeftijden met ongeveer ervoor, en bij elke fase hoort "
                   "een typische gebeurtenis. Let op de drie begrippen die vaak door elkaar lopen: "
                   "het lege nest, de sandwichgeneratie en het pensioen horen bij drie "
                   "verschillende momenten.",
            waarom=[
                None,
                "Merk op dat de laatste lijn er bewust tussen staat. Grootouder worden is geen "
                "verlies maar een nieuwe rol, terwijl de andere overgangen in deze rij wel iets "
                "wegnemen. Bij ouder worden hoort dus niet alleen verlies.",
            ],
        ),
        dict(
            aanpak="Houd normaal ouder worden en ziekte strikt uit elkaar. Trager worden, minder "
                   "scherp zien en horen en een woord kwijt zijn horen bij de leeftijd. De weg "
                   "niet meer vinden, mensen niet meer herkennen en niet meer kunnen plannen "
                   "horen daar niet bij.",
            waarom=[
                "Ken de twee vaktermen uit dit rijtje: presbyacusis is het ouderdomsslechthorend "
                "worden, dat bij de hoge tonen begint, en sarcopenie is het verlies van "
                "spiermassa. Dat tweede is deels tegen te gaan met beweging en met genoeg eiwit.",
                "Let op de laatste zin van het antwoord. Jij merkt op en meldt; de arts stelt "
                "vast. Een vermoeden van dementie uitspreken als een diagnose is niet aan een "
                "zorgkundige.",
                "Drie van de genoemde volstaan. Niet overhoren is de belangrijkste: vragen als "
                "weet je nog wie ik ben zetten de persoon voor een proef die hij niet kan halen, "
                "en dat voelt hij.",
            ],
        ),
        dict(
            aanpak="De twee laatste oefeningen gaan over hetzelfde spanningsveld: wat iemand zelf "
                   "wil tegenover wat veilig is. Antwoord in twee delen: wat je vraagt, en welke "
                   "vorm je zoekt die wel kan. Dwingen en zomaar laten zijn beide geen antwoord.",
            waarom=[
                "Thuis blijven wonen is een middel en geen doel. Het punt van deze vraag is dat "
                "je het afmeet aan wat de persoon wil en aan wat er rond hem staat, en niet aan "
                "de leuze dat thuis altijd het beste is.",
                "Let op de drie delen van het antwoord: je vraagt naar de reden, je zoekt een "
                "vorm die wel kan, en je legt het vast en overlegt. Wie enkel niet dwingt, laat "
                "de man ongewassen; wie enkel doorzet, schendt zijn autonomie.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-waarnemen-en-observeren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes vertekeningen, en ze hebben alle hetzelfde patroon: je ziet wat je al "
                   "verwacht. Houd het haloeffect en het eerste-indrukeffect uit elkaar: het "
                   "eerste gaat over één eigenschap die de rest meesleept, het tweede over het "
                   "moment waarop je iemand voor het eerst zag.",
            waarom=[
                "De zelfvervullende voorspelling is de gevaarlijkste van de zes, want daar "
                "verandert niet enkel jouw beeld maar het kind zelf. Het is ook de enige die "
                "gevolgen heeft die blijven.",
                "Let op de laatste zin: begin zelf met kijken. Een overdracht van een collega mag "
                "je niet negeren, maar je zet ze apart en gaat ze nadien na met wat je zelf zag.",
            ],
        ),
        dict(
            aanpak="Een feit is wat een camera zou zien: wie, wat, hoe vaak, hoe lang. Een "
                   "interpretatie is jouw verklaring ervan. Toets elke uitspraak met de vraag of "
                   "twee mensen onafhankelijk hetzelfde zouden opschrijven. Een woord als "
                   "verlegen, lui of agressief is altijd een interpretatie.",
            waarom=[
                "Vergelijk de paren twee aan twee: het is telkens hetzelfde kind, eerst als feit "
                "en dan als verklaring. Dat is ook wat er in een verslag misgaat: men schrijft de "
                "tweede zin en denkt de eerste gezien te hebben.",
                "Merk op hoe het herschreven feit eruitziet: een aantal en een tijdsduur. Zonder "
                "cijfer glipt er bijna altijd een oordeel binnen.",
                None,
                "Dit is de nuance die het hoofdstuk afmaakt. Je beeld mag en moet in een verslag, "
                "maar in twee stappen: eerst wat je zag, dan wat je vermoedt. Dan kan een collega "
                "jouw vermoeden nagaan in plaats van het over te nemen.",
            ],
        ),
        dict(
            aanpak="De observatievormen verschillen op twee punten: doe je zelf mee of niet, en "
                   "noteer je alles of enkel bepaalde dingen. De twee steekproeven kiezen hun "
                   "moment: een tijdsteekproef kijkt op vaste tijden, een gebeurtenissteekproef "
                   "wacht op een bepaald gedrag.",
            waarom=[
                None,
                "Let op de reden in het antwoord, want daar zitten de punten. Vaste momenten "
                "nemen de keuze uit jouw handen; kijk je wanneer het je opvalt, dan meet je je "
                "eigen aandacht en niet het gedrag van het kind.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-rapporteren-en-respectvol-omgaan-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes uitspraken over een verslag. Twee vragen geven alle antwoorden: kan een "
                   "collega hiermee verder, en blijft het binnen de kring van wie het nodig "
                   "heeft? Alles wat het verslag naar buiten brengt, is niet waar; alles wat het "
                   "navolgbaar maakt, wel.",
            waarom=[
                "Datum en uur lijken bijkomstig maar zijn het niet: pas met een tijdstip kan "
                "iemand een verband zien met de slaap, de maaltijd of een gesprek van die dag.",
                None,
                "Dat je ook het goede noteert, wordt het vaakst vergeten. Een dossier dat enkel "
                "problemen bevat, geeft jaren later een beeld van een kind dat nooit iets goed "
                "deed, en dat is geen eerlijk beeld.",
                None,
                "Niet waar, en dat geldt ook voor je eigen gezin en ook zonder naam te noemen. In "
                "een dorp of een school is een omschrijving even verklappend als een naam.",
                "Waar. Ouders hebben recht op inzage in het dossier van hun kind, en dat is ook "
                "een goede reden om te schrijven wat je kan verantwoorden: je schrijft altijd "
                "alsof de ouder het morgen leest.",
            ],
        ),
        dict(
            aanpak="Een zin wordt bruikbaar als je er drie dingen in zet: wie, wat precies, en "
                   "hoe vaak of wanneer. Haal elk waardewoord eruit. Gaat het over het gezin in "
                   "plaats van over het gedrag, dan hoort de zin er helemaal niet in.",
            waarom=[
                "Vergelijk met de oude zin: ramp zegt alleen hoe jij je voelde. Drie keer de "
                "kring verlaten en een tijdstip kan een collega nagaan en vergelijken met "
                "morgen.",
                "Let op dat de herschreven zin geen verwijt meer is. Niet antwoorden kan tien "
                "oorzaken hebben, en een van de redenen om feiten te schrijven is net dat je die "
                "ruimte openlaat.",
                "Deze derde is anders dan de vorige twee: hier is niet de formulering fout maar "
                "het onderwerp. Een oordeel over een gezin hoort niet in een dossier, hoe "
                "voorzichtig je het ook schrijft.",
                "Dit is de belangrijkste zin van de hele bundel. Een dossier blijft jaren bestaan "
                "en wordt gelezen door mensen die het kind nooit zagen. Wat jij vandaag schrijft, "
                "bepaalt hoe een hulpverlener binnen drie jaar naar dat kind kijkt.",
            ],
        ),
        dict(
            aanpak="Het beroepsgeheim is de regel, en de uitzonderingen zijn smal. Antwoord dus "
                   "altijd eerst met zwijgen en daarna met waar het wel hoort: de familie, je "
                   "verantwoordelijke, het team. Ook iets bevestigen is al delen.",
            waarom=[
                "Let op de laatste zin: ook bevestigen dat iemand er woont, is al een schending. "
                "Dat is de val in zo'n gesprek, want je zegt niets over de gezondheid en toch "
                "geef je iets weg.",
                "Ken de twee voorwaarden: ernstig én dringend gevaar, en dan nog zo beperkt "
                "mogelijk. Overleg met je verantwoordelijke hoort erbij; het is bijna nooit een "
                "beslissing die je alleen neemt.",
                "Let op het tweede deel van het antwoord, want daar wordt het vaakst tegen "
                "gezondigd: ook met toestemming hoort zo'n foto op het kanaal van de organisatie "
                "en niet op je eigen profiel, waar je hem niet meer onder controle hebt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gedrag-en-behoeften-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Achter lastig gedrag zit bijna altijd een behoefte die het kind niet kan "
                   "uitspreken. Vraag je dus niet af hoe je het gedrag stopt maar wat het kind "
                   "ermee probeert te krijgen: meedoen, gezien worden, rust of nabijheid.",
            waarom=[
                "Let op de kleuter die weer in zijn broek plast. Dat is regressie, en ze komt "
                "vaak na een verandering thuis: een verhuis, een broertje, een scheiding. Straffen "
                "maakt het daar altijd erger.",
                "Dit is de kern van het hoofdstuk. Straf neemt het gedrag weg en laat de behoefte "
                "staan, en dan komt ze in een andere vorm terug. Daarom werkt een straf soms één "
                "keer en daarna nooit meer.",
            ],
        ),
        dict(
            aanpak="Grenzen stellen draait om vorm en niet om streng of soepel. Vier dingen "
                   "werken: zeg de regel vooraf, blijf dezelfde, keur het gedrag af en niet het "
                   "kind, en geef een keuze binnen de grens. En zeg altijd wat je wél wil zien.",
            waarom=[
                None,
                "Positief formuleren werkt omdat een kind het beeld hoort dat je uitspreekt. Zeg "
                "je niet lopen, dan hoort het lopen; zeg je stappen, dan weet het wat het moet "
                "doen in plaats van wat het moet laten.",
                "Binnenstem is een woord dat kleuters echt gebruiken en begrijpen. Dat is het "
                "nut van positief formuleren: je geeft een handeling in plaats van een verbod.",
                "Let op dat de grens hier niet verdwijnt. Opruimen is niet de vraag; enkel de "
                "orde is een keuze. Dat is precies wat autonomie binnen de regel betekent.",
            ],
        ),
        dict(
            aanpak="Bij een conflict is de orde altijd dezelfde: eerst veiligheid, dan benoemen "
                   "wat je ziet, dan de kinderen zelf laten zoeken, en achteraf kort terugkomen. "
                   "De oplossing bedenken is niet jouw taak zolang zij het zelf nog kunnen.",
            waarom=[
                "Let op de laatste stap, die bijna altijd overgeslagen wordt. Achteraf kort "
                "terugkomen maakt het verschil tussen een opgelost conflict en een onderbroken "
                "ruzie.",
                "De aanpak die niet werkt, is het leerzaamste deel. Een machtsstrijd verlies je "
                "altijd, want een kind kan langer volhouden dan jij, en eten als straf of beloning "
                "gebruiken geeft problemen met eten die veel langer blijven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-communiceren-en-actief-luisteren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het model heeft zes onderdelen, van zender tot feedback. Daarnaast twee "
                   "lagen in elke boodschap: de inhoud, wat de woorden zeggen, en de relatie, wat "
                   "de toon over jullie band zegt. Bij een botsing tussen die twee wint de toon.",
            waarom=[
                "Merk op dat feedback bij het model hoort. Zonder iets terug is er geen "
                "communicatie maar een mededeling, en dan weet je nooit of de boodschap aankwam "
                "zoals je ze bedoelde.",
                "Dat de toon wint, kan je zelf nagaan: zeg goed gedaan met een zucht en niemand "
                "hoort een compliment. Daarom is non-verbale communicatie in de zorg even "
                "belangrijk als de woorden.",
            ],
        ),
        dict(
            aanpak="De luistervaardigheden verschillen in wat je teruggeeft: parafraseren geeft "
                   "de inhoud terug, gevoelsreflectie het gevoel, samenvatten de grote lijn. "
                   "Doorvragen en aanmoedigen brengen de ander verder, en stilte laten is ook een "
                   "vaardigheid.",
            waarom=[
                "Houd parafraseren en gevoelsreflectie uit elkaar: dus je bedoelt gaat over de "
                "inhoud, je klinkt kwaad over het gevoel. Dat tweede opent een gesprek vaak "
                "sneller, omdat het benoemt wat de ander zelf nog niet gezegd heeft.",
                "Dat het goedbedoeld is, maakt het niet beter. Door je eigen verhaal te geven, "
                "neem je het gesprek over, en de ander moet dan naar jou luisteren terwijl hij "
                "zelf iets wou kwijtgeraken.",
                "Let op de laatste zin van het antwoord. Een zin die naar levensmoeheid verwijst, "
                "houd je nooit voor jezelf: je blijft erbij, je sluit niets af met het komt wel "
                "goed, en je meldt het aan je verantwoordelijke.",
            ],
        ),
        dict(
            aanpak="Bij wie moeilijk praat, pas je de vorm aan en niet het volume. Elke situatie "
                   "heeft zijn eigen aanpassing, en twee ervan komen in elke les terug: één vraag "
                   "per keer, en nooit overhoren.",
            waarom=[
                "Let op de laatste twee lijnen: bij wie dichtklapt doe je minder, bij wie kwaad "
                "is doe je iets anders. Ingaan op de inhoud van een kwade boodschap werkt niet "
                "zolang het gevoel niet benoemd is.",
                "Dit is de les van het hele hoofdstuk: luider praten helpt enkel bij wie slecht "
                "hoort, en zelfs daar maar beperkt. Bij alle andere hindernissen verander je de "
                "woorden, het tempo en de hulpmiddelen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-feedback-en-verbindend-communiceren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een ik-boodschap heeft vier delen in een vaste orde: gedrag, gevolg, gevoel, "
                   "wens. Schrijf ze altijd alle vier op, want een boodschap zonder wens is een "
                   "klacht en een boodschap zonder gevolg klinkt als een gril. En haal altijd "
                   "en nooit eruit.",
            waarom=[
                "De laatste lijn is de belangrijkste: altijd en nooit maken van een opmerking een "
                "verwijt, en de ander gaat dan zoeken naar de ene keer dat het wel lukte. Een "
                "aantal of een datum kan hij niet weerleggen.",
                "Vergelijk met de oude zin: nooit iets opruimen is niet waar en niet na te gaan. "
                "Het materiaal van vanmorgen staat er wel, en daar kan een gesprek over gaan.",
                "Let op het aantal in deze versie: drie keer een kwartier. Daarmee gaat het "
                "gesprek over die drie keer en niet over wat voor iemand de collega is.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over feedback. Drie regels geven alle antwoorden: feedback gaat "
                   "over gedrag en niet over de persoon, ze komt snel en onder vier ogen, en ze "
                   "is tweerichting. Alles wat de ander in een hoek zet, is niet waar.",
            waarom=[
                None,
                "Snel is belangrijk omdat je dan nog over een concrete situatie kan spreken. Komt "
                "feedback een maand later, dan herinnert niemand zich de feiten en gaat het "
                "gesprek over karakters.",
                "Niet waar. Voor de groep is een vernedering, ook als de boodschap klopt, en de "
                "ander zal zich dan vooral verdedigen in plaats van te luisteren. Positieve "
                "feedback mag wel voor de groep.",
                "Waar, en dat is een nuttige regel voor wie feedback krijgt. Je mag zeggen dat je "
                "erover wil nadenken en er morgen op terugkomen; niets dwingt je tot een antwoord "
                "op het moment.",
                "Niet waar, en dit is de meest voorkomende fout in teams. Zonder positieve "
                "feedback weet niemand wat hij moet blijven doen, en wordt elke opmerking van de "
                "verantwoordelijke een slecht teken.",
                "Waar. Feedback is een gesprek en geen mededeling: misschien ken je de helft van "
                "de situatie niet, en net dat komt alleen boven als je vraagt hoe de ander het "
                "zag.",
            ],
        ),
        dict(
            aanpak="Verbindende communicatie heeft vier stappen: observatie, gevoel, behoefte, "
                   "verzoek. Ze lijkt op de ik-boodschap maar legt de nadruk op de behoefte "
                   "eronder. Twee valkuilen: een eis vermomd als verzoek, en een gedachte "
                   "vermomd als gevoel.",
            waarom=[
                "Let op de vorm van het verzoek: het is een vraag en geen opdracht. Wil je me "
                "laten uitspreken kan met nee beantwoord worden, en dan heb je een gesprek in "
                "plaats van een conflict.",
                "Dit is de scherpste toets van het hele hoofdstuk. Vraag je af wat er gebeurt bij "
                "een nee: zoek je verder, dan was het een verzoek; volgt er een verwijt of een "
                "straf, dan was het een eis in verpakking.",
                "Let op de woorden na ik voel dat: daar volgt bijna altijd een gedachte. Een "
                "gevoel kan je in één woord zeggen. Niet gerespecteerd voelen is een "
                "beoordeling van de ander; onzeker of kwaad is een gevoel van jezelf.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vrije-tijd-spel-en-expressie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij elke spelvorm hoort een ander soort leren: bouwen oefent inzicht en "
                   "handen, rollenspel oefent taal en samen, een regelspel oefent wachten en "
                   "verliezen. Zoek dus niet wat leuk is maar wat het kind erbij moet kunnen.",
            waarom=[
                "Let op het verschil tussen verstoppertje en een gezelschapsspel. Beide hebben "
                "regels, maar bij het tweede moet een kind ook kunnen verliezen, en dat is een "
                "stap verder.",
                "Dit is de belangrijkste zin van de bundel. Vrij spel is geen pauze tussen het "
                "leren: juist doordat niemand het resultaat bepaalt, kan het kind proberen en "
                "mislukken zonder gevolg.",
            ],
        ),
        dict(
            aanpak="Vrije tijd is een recht en geen luxe, en de drempels zijn vaak praktisch. "
                   "Noem bij elke drempel een oplossing, want daar zitten de punten, en denk "
                   "verder dan de prijs: vervoer, materiaal en het simpelweg niet weten zijn "
                   "even grote hindernissen.",
            waarom=[
                "De UiTPAS is de Vlaamse pas waarmee wie in armoede leeft korting krijgt op "
                "vrijetijdsactiviteiten in de deelnemende gemeenten. Dat is het concrete "
                "antwoord dat ze bij deze vraag willen horen.",
                "Let op de vierde drempel: niet weten wat er bestaat. Die wordt bijna altijd "
                "vergeten en is nochtans de goedkoopste om weg te nemen, want één keer samen "
                "meegaan volstaat.",
            ],
        ),
        dict(
            aanpak="Vijf vormen van expressie, en één gemeenschappelijk kenmerk: er is geen juist "
                   "of fout resultaat. Daar volgt de houding uit die in de laatste twee "
                   "oefeningen gevraagd wordt: vragen in plaats van verbeteren, en alles ophangen "
                   "in plaats van het mooiste.",
            waarom=[
                None,
                "Let op de tweede helft van het antwoord. Een kind dat verbeterd wordt, maakt de "
                "volgende tekening voor jou en niet voor zichzelf, en dan is het geen expressie "
                "meer.",
                "Dit is dezelfde gedachte in de praktijk. Wie nooit hangt, leert dat zijn werk "
                "niet goed genoeg is; wie altijd hangt omdat hij de beste is, leert dat het om "
                "het resultaat gaat. Beide missen waar expressie voor dient.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-spelvormen-en-speelgoed-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes spelvormen, en ze komen in een vaste orde: sensomotorisch bij een baby, "
                   "dan constructie en fantasie, en het regelspel pas als een kind regels kan "
                   "volgen. Onthoud dat ze elkaar niet opvolgen maar zich opstapelen.",
            waarom=[
                None,
                "De laatste lijn is het punt van deze reeks: de oude spelvormen verdwijnen niet. "
                "Een kind van zes bouwt nog, en een tiener die aan een spelconsole zit, speelt "
                "nog altijd een regelspel met een stuk rollenspel erin.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over speelgoed. Twee dingen beslissen: de veiligheid, met de "
                   "CE-aanduiding en het teken voor onder drie jaar, en de spelwaarde. Hoe meer "
                   "het speelgoed zelf doet, hoe minder het kind kan doen.",
            waarom=[
                "Let op wat CE wel en niet betekent: het is een veiligheidsaanduiding van de "
                "fabrikant en geen keurmerk van kwaliteit of van pedagogische waarde.",
                None,
                "Dit is de belangrijkste regel bij het kiezen van speelgoed: weinig functies, "
                "veel mogelijkheden. Blokken kunnen honderd dingen worden, een pratende pop blijft "
                "een pratende pop.",
                "Niet waar, en dat volgt uit de vorige. Prijs en spelwaarde hebben niets met "
                "elkaar te maken; het dure speelgoed heeft vaak juist meer elektronica en dus "
                "minder mogelijkheden.",
                "Niet waar, en dit is de bekendste van allemaal. Een doos kan een huis, een boot, "
                "een auto of een grot zijn, en dat is precies wat het kind erin legt.",
                "Waar, en de vuistregel is de wc-rol: wat erdoor past, is te klein voor een kind "
                "onder de drie. Vandaar ook het teken met de doorstreepte cirkel.",
            ],
        ),
        dict(
            aanpak="Een activiteit uitwerken vraagt altijd vijf delen: doel, materiaal, verloop "
                   "in drie stukken, de aanpassing waar nodig, en een plan B. Dat laatste wordt "
                   "het vaakst vergeten, en net daarop valt een activiteit in de praktijk stil.",
            waarom=[
                "Toets je eigen uitwerking aan de leeftijd: twintig minuten en vijf kleuters "
                "betekent korte stappen en veel beweging. En zet in je plan B twee gevallen: het "
                "loopt uit de hand, of het is na vijf minuten gedaan.",
                "Dit is dezelfde gedachte als bij het spel zelf. Opruimen in de activiteit zetten "
                "maakt er een deel van het spel van; erna zetten maakt het de prijs die het kind "
                "voor het plezier betaalt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-activiteiten-voor-volwassenen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij een activiteit begin je bij het doel en niet bij het idee. Elk doel heeft "
                   "zijn eigen soort activiteit: motoriek, geheugen, beweging, contact, betekenis "
                   "of zintuigen. Zoek dus eerst wat je wil bereiken en kies dan iets wat daarbij "
                   "past.",
            waarom=[
                "Let op de vijfde lijn, die anders is dan de andere: mee de tafel dekken is geen "
                "oefening maar een taak. Juist daarom werkt ze, want de persoon doet iets wat "
                "echt nodig is.",
                "Dit is de kern van het hoofdstuk. Vermaakt worden is passief; iets bijdragen "
                "raakt het gevoel van waarde. Daarom vragen zorgkundigen aan een bewoner liever "
                "om hulp dan dat ze hem bezighouden.",
            ],
        ),
        dict(
            aanpak="Aanpassen betekent de activiteit veranderen en niet de persoon. Vraag je bij "
                   "elke deelnemer af wat hem hindert: zien, horen, de hoogte van de tafel, de "
                   "duur of de druk om te presteren. En wie niet wil meedoen, mag toekijken.",
            waarom=[
                "Let op de laatste lijn: laten toekijken is ook een aanpassing. Meekijken van de "
                "zijkant is vaak de eerste stap, en wie geduld heeft, ziet die persoon de keer "
                "daarna meedoen.",
                "Noem beide delen van het antwoord: waarom de actualiteitsquiz schaadt, en wat "
                "wel werkt. Het verre geheugen en het muzikale geheugen blijven veel langer "
                "intact, en daarom werken liedjes en voorwerpen van vroeger.",
            ],
        ),
        dict(
            aanpak="Bij deze uitwerking komt er één ding bij tegenover de activiteiten voor "
                   "kinderen: de aanpassing per deelnemer. Noem ze met naam en al, en kies iets "
                   "zonder winnaars. En sluit altijd bewust af, want het einde blijft het meest "
                   "bij.",
            waarom=[
                "Toets je uitwerking op de drie deelnemers die in de opgave genoemd worden: twee "
                "rolstoelen vragen een ronde tafel en genoeg ruimte errond, en de bewoner met "
                "beginnende dementie vraagt een opdracht zonder prestatie. Een uitwerking die "
                "die drie niet noemt, is niet af.",
                "Let op de laatste woorden: in feiten en niet in oordelen. Dat is dezelfde regel "
                "als bij het rapporteren, en ze geldt ook voor een verslag over een namiddag "
                "met een gesprekstafel.",
            ],
        ),
    ],
)

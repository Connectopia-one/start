# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Nederlands 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere zinnen om te ontleden, andere teksten om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een zin
herschrijven, een oordeel verantwoorden). Wie hier iets bijschrijft, legt het
eerst naast `../../boost-doorstroom/nederlands.json`.

In elke bundel staat achteraan één reeks "Voor het echte leven". Die vraagt om
een gesprek voor te bereiden of na te bespreken, want spreken en gesprekken
wegen samen 40 % van het examen Nederlands 1 en dat leer je niet achter een
scherm. Kim vroeg daar uitdrukkelijk naar op 30 september 2026. Laat die reeks
staan.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Nederlands"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een zin die je moet herschrijven: schrijf de hele zin over, niet alleen het stuk dat verandert.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def echte_leven(opdracht, antwoord, regels=6):
    """De vaste slotreeks over spreken en gesprekken."""
    return dict(
        kop="Voor het echte leven",
        opdracht="Deze oefening maak je op papier, maar ze is pas af als je ze ook echt gedaan hebt.",
        oefeningen=[("open", opdracht, antwoord, regels)],
    )


# ============================================================
OEFENBUNDELS["oefenbundel-zender-ruis-en-de-zeven-tekstsoorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zender, ruis en de zeven tekstsoorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort?",
             opdracht="Schrijf bij elke tekst de tekstsoort: informatief, persuasief, opiniërend, "
                      "prescriptief, narratief, argumentatief of literair.",
             oefeningen=[
                 ("rij", [("de gebruiksaanwijzing van een wasmachine", "prescriptief"),
                          ("een reisverslag van drie weken Peru", "narratief"),
                          ("een encyclopedie-artikel over de Schelde", "informatief"),
                          ("een affiche die oproept om bloed te geven", "persuasief")],
                  "Welke tekstsoort?", WL),
                 ("rij", [("een opiniestuk met vier argumenten en een tegenargument", "argumentatief"),
                          ("een recensie van een restaurant met drie sterren", "opiniërend"),
                          ("een kortverhaal in een literair tijdschrift", "literair")],
                  "Welke tekstsoort?", WL),
             ]),
        dict(kop="Persuasief of argumentatief?",
             opdracht="Twee tekstsoorten willen je overtuigen. Duid aan welke het is.",
             oefeningen=[
                 ("kies", "Een reclamespot met een bekende voetballer en een pakkend liedje.",
                  ["persuasief", "argumentatief"], 0),
                 ("kies", "Een betoog dat met cijfers van Statbel aantoont dat de fietssnelwegen werken.",
                  ["persuasief", "argumentatief"], 1),
                 ("kies", "Een pleidooi van een advocaat dat vooral op medelijden speelt.",
                  ["persuasief", "argumentatief"], 0),
                 ("kies", "Een essay dat drie verklaringen naast elkaar legt en er één weerlegt.",
                  ["persuasief", "argumentatief"], 1),
             ]),
        dict(kop="Het communicatieschema invullen",
             opdracht="Vul in wat er ontbreekt bij deze situatie: een leerkracht mailt aan de ouders "
                      "van 2A dat de uitstap naar Technopolis verplaatst is naar 14 mei.",
             oefeningen=[
                 ("tabel", ["onderdeel", "wat het hier is"],
                  [["zender", None], ["ontvanger", None], ["boodschap", None],
                   ["kanaal", None], ["bedoeling", None]],
                  "zender: de leerkracht · ontvanger: de ouders van 2A · boodschap: de uitstap is "
                  "verplaatst naar 14 mei · kanaal: een mail · bedoeling: informeren", "260px"),
             ]),
        dict(kop="Waar zit de ruis?",
             opdracht="Schrijf bij elke situatie of de ruis bij de zender, bij het kanaal of bij "
                      "de ontvanger zit.",
             oefeningen=[
                 ("rij", [("de verbinding valt weg tijdens een videogesprek", "het kanaal"),
                          ("de spreker gebruikt vaktermen die niemand kent", "de zender"),
                          ("de luisteraar zit aan iets anders te denken", "de ontvanger"),
                          ("de mail belandt in de map ongewenst", "het kanaal")],
                  "Waar zit de ruis?", WW),
                 ("open", "Je stuurt een bericht waarin je iets grappig bedoelt, en de ander is "
                          "beledigd. Waar zit de ruis, en hoe had je ze kunnen voorkomen?",
                  "Meestal bij de zender: geschreven tekst draagt geen toon, dus ironie komt niet "
                  "over. Voorkomen kon door het anders te formuleren, door het niet te schrijven "
                  "maar te zeggen, of door duidelijk te maken dat het een grapje is.", 5),
             ]),
        dict(kop="Wat is de bedoeling?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een tekst kan maar één bedoeling tegelijk hebben.", False),
                 ("waar", "Het kanaal is het middel waarlangs de boodschap reist.", True),
                 ("waar", "Bij een expressieve tekst staat de zender zelf centraal.", True),
                 ("waar", "Een handleiding is narratief, want ze vertelt wat je doet.", False),
             ]),
        dict(kop="Zelf schrijven",
             opdracht="",
             oefeningen=[
                 ("open", "Schrijf over dezelfde gebeurtenis (de schoolbus had een uur vertraging) "
                          "twee keer twee zinnen: eerst informatief, dan opiniërend.",
                  "Informatief: de feiten, zonder oordeel. Bijvoorbeeld: 'De bus van lijn 45 reed "
                  "vanmorgen een uur later dan voorzien. De vervoersmaatschappij meldt een panne.' "
                  "Opiniërend: wat jij ervan vindt. Bijvoorbeeld: 'Een uur wachten in de regen "
                  "zonder één bericht: zo ga je niet om met wie op je rekent.'", 7),
                 ("open", "Leg uit waarom een reclamespot tegelijk persuasief én narratief kan zijn.",
                  "Omdat hij een verhaaltje vertelt om je te doen kijken, en dat verhaal in "
                  "dienst staat van het verkopen. Voor de tekstsoort kijk je naar het hoofddoel, "
                  "en dat is hier overtuigen.", 4),
             ]),
        echte_leven(
            "Bel deze week zelf naar een winkel, een club of een gemeentedienst met een echte vraag. "
            "Schrijf eerst op wat je gaat zeggen: je bedoeling in één zin, en de twee dingen die de "
            "ander zeker moet horen. Schrijf achteraf op wat er anders liep dan je gedacht had.",
            "Er is geen juist antwoord. Let er wel op of je je bedoeling in één zin kreeg, en of "
            "de ander doorvroeg omdat iets niet duidelijk was. Dat laatste is ruis, en meestal "
            "zit ze bij de zender.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-hoofdgedachte-alinea-en-structuuraanduiders-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Hoofdgedachte, alinea en structuuraanduiders",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk verband legt het signaalwoord?",
             opdracht="Schrijf bij elk woord welk verband het aankondigt: tegenstelling, oorzaak "
                      "en gevolg, opsomming, tijd, voorwaarde, doel of samenvatting.",
             oefeningen=[
                 ("rij", [("desondanks", "een tegenstelling"),
                          ("bijgevolg", "een oorzaak en gevolg"),
                          ("vervolgens", "een tijd"),
                          ("tenzij", "een voorwaarde")],
                  "Welk verband?", WL),
                 ("rij", [("opdat", "een doel"),
                          ("kortom", "een samenvatting"),
                          ("bovendien", "een opsomming"),
                          ("daarentegen", "een tegenstelling")],
                  "Welk verband?", WL),
             ]),
        dict(kop="Het juiste signaalwoord invullen",
             opdracht="Vul in elke zin een passend signaalwoord in. Er is vaak meer dan één "
                      "mogelijkheid; kies er één die het verband juist weergeeft.",
             oefeningen=[
                 ("kort", "De brug was afgesloten. ............ moesten we omrijden.",
                  "Daardoor, dus of bijgevolg", WW),
                 ("kort", "Hij traint elke dag, ............ wint hij nooit.",
                  "maar, toch of desondanks", WW),
                 ("kort", "We gaan door, ............ het blijft regenen.",
                  "tenzij", WW),
                 ("kort", "............: het plan werkt, maar het kost te veel.",
                  "Kortom, samengevat of concluderend", WW),
             ]),
        dict(kop="Hoofdgedachte of detail?",
             opdracht="Bij elke alinea staan twee zinnen. Duid de hoofdgedachte aan.",
             oefeningen=[
                 ("kies", "Een alinea over slaap bij jongeren:",
                  ["Jongeren slapen gemiddeld te kort, en dat weegt op hun concentratie.",
                   "In het onderzoek deden 412 leerlingen van vier scholen mee."], 0),
                 ("kies", "Een alinea over de vergrijzing:",
                  ["In 2005 was één op zeven Belgen ouder dan 65.",
                   "Een ouder wordende bevolking verandert de kosten van de gezondheidszorg."], 1),
                 ("kies", "Een alinea over taalvarianten:",
                  ["In Limburg zegt men 'gèr' waar men in Antwerpen 'graag' zegt.",
                   "Dialecten verdwijnen niet, ze verschuiven naar informele situaties."], 1),
             ]),
        dict(kop="De structuur van een tekst",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["tekstdeel", "wat er hoort te staan"],
                  [["inleiding", None], ["midden", None], ["slot", None]],
                  "inleiding: het onderwerp aankondigen en de lezer binnenhalen · midden: de "
                  "uitwerking, één hoofdgedachte per alinea · slot: samenvatten, besluiten of "
                  "vooruitkijken", "260px"),
                 ("open", "Wat is het verschil tussen een structuuraanduider en een signaalwoord?",
                  "Een signaalwoord legt een verband tussen zinnen of alinea's (want, maar, "
                  "daarna). Een structuuraanduider wijst de weg in de tekst als geheel: een titel, "
                  "een tussenkop, 'in wat volgt', 'ten slotte'. Ze doen dus allebei aan sturing, "
                  "maar op een ander niveau.", 6),
             ]),
        dict(kop="Alinea's afbakenen",
             opdracht="Duid aan of de stelling klopt.",
             oefeningen=[
                 ("waar", "Elke alinea behandelt in principe één hoofdgedachte.", True),
                 ("waar", "Een alinea van één zin mag nooit.", False),
                 ("waar", "De hoofdgedachte staat altijd in de eerste zin van de alinea.", False),
                 ("waar", "Een tussenkop is een structuuraanduider.", True),
             ]),
        dict(kop="Samenvatten",
             opdracht="",
             oefeningen=[
                 ("open", "Schrijf in één zin op wat een goede samenvatting wél en niet bevat.",
                  "Wel: de hoofdgedachten en het verband ertussen, in je eigen woorden. Niet: "
                  "voorbeelden, cijfers ter illustratie, herhalingen en je eigen mening.", 5),
                 ("open", "Waarom lees je een lange tekst eerst diagonaal voor je hem grondig "
                          "leest? Noem twee redenen.",
                  "Om te weten waarover hij gaat en hoe hij opgebouwd is, zodat je tijdens het "
                  "grondige lezen weet waar je bent. En om te beslissen of je hem wel helemaal "
                  "nodig hebt.", 5),
             ]),
        echte_leven(
            "Vertel deze week iemand in drie minuten een film of een boek na. Schrijf vooraf op "
            "papier je inleiding (één zin), je midden (drie hoofdgedachten) en je slot (één zin). "
            "Noteer achteraf waar de ander begon te vragen.",
            "Er is geen juist antwoord. Waar de ander vraagt, zat je structuur niet vast: meestal "
            "ontbrak een signaalwoord dat het verband legde, of sloeg je een hoofdgedachte over "
            "omdat ze voor jou vanzelfsprekend was.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-argumenteren-stelling-argumentsoort-en-drogreden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Argumenteren: stelling, argumentsoort en drogreden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Stelling of feit?",
             opdracht="Een stelling kan je betwisten, een feit kan je nakijken. Duid aan wat het is.",
             oefeningen=[
                 ("kies", "De Schelde is 350 kilometer lang.", ["een stelling", "een feit"], 1),
                 ("kies", "De gemeente zou de Schelde-oever moeten autovrij maken.",
                  ["een stelling", "een feit"], 0),
                 ("kies", "Op het dak van onze school liggen 96 zonnepanelen.",
                  ["een stelling", "een feit"], 1),
                 ("kies", "Zonnepanelen zijn de beste investering voor een gezin.",
                  ["een stelling", "een feit"], 0),
             ]),
        dict(kop="Welke soort argument?",
             opdracht="De fiche noemt vijf soorten: vergelijking, oorzaak en gevolg, "
                      "wetenschappelijk onderzoek, cijfers en statistieken, en autoriteit. "
                      "Schrijf de soort erbij.",
             oefeningen=[
                 ("rij", [("Acht op de tien leerlingen zegt te weinig te slapen.", "cijfers en statistieken"),
                          ("De Wereldgezondheidsorganisatie raadt dit af.", "autoriteit"),
                          ("In Finland werkt dit al vijftien jaar, dus het kan hier ook.", "vergelijking")],
                  "Welke soort?", WL),
                 ("rij", [("Door de nieuwe maatregel daalde het aantal ongevallen.", "oorzaak en gevolg"),
                          ("Uit een studie van de universiteit blijkt hetzelfde.", "wetenschappelijk onderzoek"),
                          ("Een arts zegt dat dit ongezond is.", "autoriteit")],
                  "Welke soort?", WL),
             ]),
        dict(kop="Welke drogreden?",
             opdracht="Schrijf de naam van de drogreden erbij.",
             oefeningen=[
                 ("rij", [("Je bent zestien, wat weet jij daar nu van?", "persoonlijke aanval"),
                          ("Iedereen doet het, dus het kan geen kwaad.", "beroep op de massa"),
                          ("Als we dit toelaten, mag straks alles.", "glijdende schaal")],
                  "Welke drogreden?", WL),
                 ("rij", [("Je bent dus voor volledige afschaffing? Dat is onzin.", "stroman"),
                          ("Deze film is de beste, want er is geen betere.", "cirkelredenering"),
                          ("Of je studeert rechten, of je wordt werkloos.", "vals dilemma")],
                  "Welke drogreden?", WL),
             ]),
        dict(kop="Weerleggen",
             opdracht="",
             oefeningen=[
                 ("open", "Iemand zegt: 'Die maatregel werkt niet, want mijn nonkel probeerde het "
                          "en bij hem hielp het niet.' Weerleg dat in twee zinnen, en noem wat er "
                          "misloopt in de redenering.",
                  "Eén geval bewijst niets over een maatregel: dat is een overhaaste "
                  "veralgemening. Wie wil weten of het werkt, kijkt naar een groep en vergelijkt "
                  "met een groep die de maatregel niet kreeg.", 6),
                 ("open", "Wat is het verschil tussen een tegenargument en een weerlegging?",
                  "Een tegenargument is een argument van de andere kant. Een weerlegging is wat "
                  "jij daartegenin brengt: je noemt het tegenargument eerst en laat dan zien "
                  "waarom het niet opgaat of minder zwaar weegt.", 5),
             ]),
        dict(kop="Een betoog opbouwen",
             opdracht="Duid aan of de stelling klopt.",
             oefeningen=[
                 ("waar", "Een goed betoog noemt ook het sterkste argument van de tegenpartij.", True),
                 ("waar", "Een beroep op een autoriteit is altijd een drogreden.", False),
                 ("waar", "Een autoriteitsargument is enkel sterk als de autoriteit deskundig is "
                          "in dít vakgebied.", True),
                 ("waar", "Wie meer argumenten opsomt, heeft altijd het sterkste betoog.", False),
             ]),
        dict(kop="Zelf schrijven",
             opdracht="",
             oefeningen=[
                 ("open", "Neem de stelling: 'Op school zou er geen huiswerk meer mogen zijn.' "
                          "Schrijf één argument op basis van wetenschappelijk onderzoek, één op "
                          "basis van oorzaak en gevolg, en één tegenargument met je weerlegging.",
                  "Bijvoorbeeld. Onderzoek: studies vinden in het lager onderwijs nauwelijks "
                  "effect van huiswerk op leerresultaten. Oorzaak en gevolg: door huiswerk telt "
                  "mee wie thuis geholpen kan worden, en daardoor groeit het verschil tussen "
                  "kinderen. Tegenargument: huiswerk leert plannen. Weerlegging: plannen kan je "
                  "ook op school leren, met begeleiding, en dan telt de thuissituatie niet mee.", 9),
             ]),
        echte_leven(
            "Verdedig deze week aan tafel eens een standpunt waar je het zélf niet mee eens bent. "
            "Schrijf vooraf twee argumenten op, en het tegenargument waar je het meest voor vreest. "
            "Noteer achteraf wat de ander zei dat je niet zag aankomen.",
            "Er is geen juist antwoord. Let erop of je overeind bleef zonder een persoonlijke "
            "aanval: zodra je iets zegt over wie de ander is in plaats van over wat hij beweert, "
            "ben je van het argument af.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-bronnen-wegen-objectief-gekleurd-of-nep-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Bronnen wegen: objectief, gekleurd of nep",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Objectief of gekleurd?",
             opdracht="Duid aan of de zin objectief of gekleurd is.",
             oefeningen=[
                 ("kies", "De gemeenteraad keurde het plan goed met 17 stemmen voor en 9 tegen.",
                  ["objectief", "gekleurd"], 0),
                 ("kies", "De gemeenteraad duwde het omstreden plan er vlotjes door.",
                  ["objectief", "gekleurd"], 1),
                 ("kies", "Een golf van klachten overspoelde de dienst.",
                  ["objectief", "gekleurd"], 1),
                 ("kies", "De dienst ontving in maart 214 klachten, tegenover 96 in februari.",
                  ["objectief", "gekleurd"], 0),
             ]),
        dict(kop="Herschrijven",
             opdracht="Schrijf elke zin objectief over. Haal het waardeoordeel eruit, houd de "
                      "feiten.",
             oefeningen=[
                 ("open", "'Het peperdure prestigeproject van de burgemeester kost de "
                          "belastingbetaler handenvol geld.'",
                  "Bijvoorbeeld: 'Het project kost 4,2 miljoen euro en wordt betaald met "
                  "gemeentemiddelen.' Weg zijn peperduur, prestigeproject, handenvol en de "
                  "suggestie dat het van de burgemeester persoonlijk is.", 4),
                 ("open", "'Eindelijk grijpt de politie in tegen die aso's op steps.'",
                  "Bijvoorbeeld: 'De politie controleerde op 12 en 13 april op het gebruik van "
                  "elektrische steps.' Weg zijn eindelijk, ingrijpen tegen en aso's.", 4),
             ]),
        dict(kop="Wat zegt dit over de betrouwbaarheid?",
             opdracht="Schrijf erbij of het een reden is om de bron méér of minder te vertrouwen, "
                      "en waarom.",
             oefeningen=[
                 ("rij", [("het artikel heeft een auteur met naam en functie", "meer"),
                          ("de cijfers komen van een genoemd onderzoek met jaartal", "meer"),
                          ("het adres eindigt op .co in plaats van .be", "minder"),
                          ("er staan veel spelfouten in", "minder")],
                  "Meer of minder?", W),
                 ("open", "Een artikel heeft geen auteur en geen datum. Bewijst dat dat het nep "
                          "is? Leg uit.",
                  "Nee. Het bewijst niets, het is een reden om verder te kijken. Veel "
                  "persberichten en overheidsteksten hebben geen persoonlijke auteur. Zoek dan "
                  "naar de organisatie erachter en naar een tweede bron die hetzelfde meldt.", 6),
             ]),
        dict(kop="Wie betaalt het onderzoek?",
             opdracht="",
             oefeningen=[
                 ("open", "Een onderzoek over de gezondheidseffecten van frisdrank is betaald door "
                          "een frisdrankfabrikant. Mag je het daarom weggooien? Leg uit.",
                  "Nee. Het is een reden om extra kritisch te lezen, niet om het te negeren. Kijk "
                  "naar de methode, naar wie het nagekeken heeft en naar of andere onderzoeken "
                  "hetzelfde vinden. Een deskundige kan tegelijk een belang hebben, en dan is hij "
                  "deskundig én partij.", 7),
                 ("open", "Noem drie dingen die je nakijkt voor je een bericht uit een groepschat "
                          "doorstuurt.",
                  "Wie is de oorspronkelijke bron? Wanneer is het geschreven, en is het nog "
                  "actueel? Meldt een tweede, onafhankelijke bron hetzelfde? Ook nuttig: is het "
                  "een echte kop of een bewerkte schermafbeelding, en past de foto wel bij dit "
                  "verhaal.", 6),
             ]),
        dict(kop="Feit, mening of aanname",
             opdracht="Schrijf bij elke zin wat het is.",
             oefeningen=[
                 ("rij", [("De trein van 7.42 uur had 12 minuten vertraging.", "een feit"),
                          ("De NMBS doet te weinig aan stiptheid.", "een mening"),
                          ("Iedereen wil toch gewoon op tijd op het werk zijn.", "een aanname")],
                  "Wat is het?", WW),
                 ("waar", "Een tekst die bronnen vermeldt, is daarom automatisch betrouwbaar.", False),
                 ("waar", "Een reclamespot mag gekleurd zijn: dat hoort bij de bedoeling.", True),
             ]),
        echte_leven(
            "Leg deze week aan iemand uit waarom je een bericht dat je kreeg niet vertrouwt. "
            "Gebruik twee criteria uit dit hoofdstuk en zeg ze hardop. Schrijf vooraf je twee "
            "criteria op, en achteraf wat de ander antwoordde.",
            "Er is geen juist antwoord. Let erop of je over de bron sprak en niet over de persoon "
            "die hem doorstuurde. Dat laatste is op de man spelen, en dan gaat het gesprek over "
            "iets anders.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-standaardtaal-tussentaal-en-register-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Standaardtaal, tussentaal en register",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke taalvariëteit?",
             opdracht="Schrijf erbij of het standaardtaal, tussentaal, dialect of jongerentaal is.",
             oefeningen=[
                 ("rij", [("'Ik heb dat gisteren gezien.'", "standaardtaal"),
                          ("'Ik heb da gisteren gezien, he.'", "tussentaal"),
                          ("'Ich hub dat gister gezeen.'", "dialect"),
                          ("'Da was echt wel lit.'", "jongerentaal")],
                  "Welke variëteit?", WW),
             ]),
        dict(kop="Formeel of informeel?",
             opdracht="Duid aan welk register bij de situatie past.",
             oefeningen=[
                 ("kies", "Een mail aan de directeur van je school.", ["formeel", "informeel"], 0),
                 ("kies", "Een bericht aan je beste vriend.", ["formeel", "informeel"], 1),
                 ("kies", "Een sollicitatiegesprek voor een vakantiejob.", ["formeel", "informeel"], 0),
                 ("kies", "Een gesprek met de trainer tijdens de rust.", ["formeel", "informeel"], 1),
             ]),
        dict(kop="Omzetten naar standaardtaal",
             opdracht="Schrijf elke zin in verzorgde standaardtaal over.",
             oefeningen=[
                 ("open", "'Kunde gij mij daar ne keer mee helpen?'",
                  "'Kan jij mij daar eens mee helpen?' of, formeler, 'Zou u mij daarbij kunnen "
                  "helpen?' Weg zijn kunde, gij en ne keer.", 3),
                 ("open", "'Ik zen der gisteren nog gewist mor het was zoe.'",
                  "'Ik ben er gisteren nog geweest, maar het was gesloten.'", 3),
                 ("open", "'Das echt nie oke wa dieje gast doet.'",
                  "'Wat die jongen doet, kan echt niet.'", 3),
             ]),
        dict(kop="Waarom kies je een register?",
             opdracht="",
             oefeningen=[
                 ("open", "Waarom is tussentaal niet gewoon 'fout Nederlands'? Leg uit in twee "
                          "zinnen.",
                  "Omdat ze in veel situaties gewoon werkt: onder vrienden, thuis, in een "
                  "informeel gesprek. Ze is niet fout maar ongepast zodra de situatie om "
                  "standaardtaal vraagt, bijvoorbeeld in een sollicitatie of een examen.", 5),
                 ("open", "Je schrijft een mail aan een onbekende dienst. Noem drie dingen die je "
                          "anders doet dan in een bericht aan een vriend.",
                  "Een aanspreking en een afsluiting, u in plaats van jij, volledige zinnen "
                  "zonder afkortingen en zonder emoji, en je zegt in de eerste zin waarover het "
                  "gaat.", 6),
                 ("waar", "Wie taalvariatie herkent, weet meteen iets over de zender en de "
                          "situatie.", True),
                 ("waar", "Standaardtaal is in elke situatie het beste register.", False),
             ]),
        dict(kop="Een mail herschrijven",
             opdracht="",
             oefeningen=[
                 ("open", "Herschrijf dit bericht als een verzorgde mail aan de gemeente: "
                          "'hey, kzat mij af te vragen of de sporthal open is op 3 mei want wij "
                          "willen daar iets doen met de klas, laat maar weten'",
                  "Bijvoorbeeld: 'Geachte mevrouw, meneer, met onze klas zouden we op 3 mei een "
                  "activiteit willen organiseren in de sporthal. Kan u mij laten weten of de zaal "
                  "die dag beschikbaar is? Alvast bedankt. Met vriendelijke groeten, ...' Let op "
                  "de aanspreking, u, volledige zinnen en een concrete vraag.", 9),
             ]),
        echte_leven(
            "Stel deze week dezelfde vraag aan twee mensen: aan een vriend, en aan een volwassene "
            "die je niet goed kent. Schrijf vooraf allebei de zinnen uit. Noteer achteraf wat er "
            "veranderde aan je woorden, je toon en je tempo.",
            "Er is geen juist antwoord. Meestal verandert veel meer dan de woorden alleen: je "
            "spreekt trager, je maakt je zinnen af, en je legt er een aanspreking en een reden "
            "bij. Dat samen is het register.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-woordsoorten-op-een-rij-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De woordsoorten op een rij",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke woordsoort?",
             opdracht="Schrijf bij elk onderstreept woord de woordsoort.",
             oefeningen=[
                 ("rij", [("De <u>hond</u> blaft.", "zelfstandig naamwoord"),
                          ("De hond blaft <u>luid</u>.", "bijwoord"),
                          ("Een <u>luide</u> hond.", "bijvoeglijk naamwoord"),
                          ("<u>Hij</u> blaft.", "persoonlijk voornaamwoord")],
                  "Welke woordsoort?", WL),
                 ("rij", [("Het boek ligt <u>op</u> tafel.", "voorzetsel"),
                          ("Ik kom, <u>maar</u> pas later.", "voegwoord"),
                          ("<u>Drie</u> honden.", "telwoord"),
                          ("<u>Au</u>, dat doet pijn.", "tussenwerpsel")],
                  "Welke woordsoort?", WL),
             ]),
        dict(kop="Bijvoeglijk naamwoord of bijwoord?",
             opdracht="Beide kunnen op dezelfde plaats staan. Duid aan wat het is. Vraag jezelf "
                      "af: zegt het woord iets over een naamwoord, of over het werkwoord?",
             oefeningen=[
                 ("kies", "Zij zingt <u>mooi</u>.",
                  ["bijvoeglijk naamwoord", "bijwoord"], 1),
                 ("kies", "Een <u>mooi</u> lied.",
                  ["bijvoeglijk naamwoord", "bijwoord"], 0),
                 ("kies", "Hij loopt <u>snel</u>.",
                  ["bijvoeglijk naamwoord", "bijwoord"], 1),
                 ("kies", "De <u>snelle</u> loper won.",
                  ["bijvoeglijk naamwoord", "bijwoord"], 0),
             ]),
        dict(kop="Soorten voornaamwoorden",
             opdracht="Schrijf erbij welk soort voornaamwoord het is.",
             oefeningen=[
                 ("rij", [("<u>mijn</u> fiets", "bezittelijk"),
                          ("<u>die</u> fiets daar", "aanwijzend"),
                          ("<u>welke</u> fiets?", "vragend"),
                          ("de fiets <u>die</u> stuk is", "betrekkelijk")],
                  "Welk soort?", WW),
                 ("rij", [("Hij wast <u>zich</u>.", "wederkerend"),
                          ("<u>Iemand</u> belde aan.", "onbepaald"),
                          ("Ik zag <u>haar</u>.", "persoonlijk")],
                  "Welk soort?", WW),
             ]),
        dict(kop="Lidwoord en telwoord",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["soort", "voorbeeld uit 'De tweede dag kochten we een boek'"],
                  [["lidwoord", None], ["telwoord", None], ["zelfstandig naamwoord", None]],
                  "lidwoord: de (bepaald) en een (onbepaald) · telwoord: tweede · zelfstandig "
                  "naamwoord: dag en boek", "230px"),
                 ("open", "Wat is het verschil tussen een bepaald en een onbepaald telwoord? Geef "
                          "van elk een voorbeeld.",
                  "Een bepaald telwoord noemt een precies aantal: veertien, drie. Een onbepaald "
                  "telwoord niet: veel, weinig, enkele. Die laatste zijn dus geen bijvoeglijke "
                  "naamwoorden maar telwoorden.", 4),
             ]),
        dict(kop="Zoek ze in de zin",
             opdracht="",
             oefeningen=[
                 ("open", "Zin: 'Gelukkig vond zij het oude boek gisteren onder haar bed.' "
                          "Schrijf van elk woord de woordsoort op.",
                  "gelukkig: bijwoord · vond: werkwoord · zij: persoonlijk voornaamwoord · het: "
                  "lidwoord · oude: bijvoeglijk naamwoord · boek: zelfstandig naamwoord · "
                  "gisteren: bijwoord · onder: voorzetsel · haar: bezittelijk voornaamwoord · "
                  "bed: zelfstandig naamwoord", 9),
                 ("waar", "Een woordsoort ligt vast: hetzelfde woord kan nooit van soort "
                          "veranderen.", False),
             ]),
        echte_leven(
            "Leg deze week aan iemand die jonger is dan jij uit wat een bijwoord is. Schrijf "
            "vooraf je uitleg in twee zinnen op, met één voorbeeld. Noteer achteraf welke vraag "
            "de ander stelde.",
            "Er is geen juist antwoord. Wie het niet kent, vraagt bijna altijd hetzelfde: waarom "
            "is 'mooi' de ene keer een bijwoord en de andere keer niet? Antwoord: kijk naar "
            "waarover het iets zegt, niet naar het woord zelf.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-werkwoorden-tijden-en-woordvorming-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Werkwoorden, tijden en woordvorming",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tijd?",
             opdracht="Schrijf bij elke zin de naam van de werkwoordstijd voluit.",
             oefeningen=[
                 ("rij", [("Ik fiets naar school.", "onvoltooid tegenwoordige tijd"),
                          ("Ik fietste naar school.", "onvoltooid verleden tijd"),
                          ("Ik heb gefietst.", "voltooid tegenwoordige tijd"),
                          ("Ik had gefietst.", "voltooid verleden tijd")],
                  "Welke tijd?", WL),
                 ("rij", [("Ik zal fietsen.", "onvoltooid tegenwoordige toekomende tijd"),
                          ("Ik zal gefietst hebben.", "voltooid tegenwoordige toekomende tijd")],
                  "Welke tijd?", WL),
             ]),
        dict(kop="De dt-regel",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("kort", "Hij ............ (worden) morgen achttien.", "wordt", W),
                 ("kort", "............ (vinden) jij dat ook?", "Vind", W),
                 ("kort", "Jij ............ (antwoorden) altijd te snel.", "antwoordt", W),
                 ("kort", "Het is al ............ (gebeuren).", "gebeurd", W),
                 ("kort", "Zij heeft het brood ............ (branden).", "gebrand", W),
                 ("kort", "De deur wordt ............ (verven).", "geverfd", W),
             ]),
        dict(kop="Sterk of zwak?",
             opdracht="Schrijf de verleden tijd en het voltooid deelwoord op, en duid aan of het "
                      "werkwoord sterk of zwak is.",
             oefeningen=[
                 ("rij", [("lopen", "liep, gelopen: sterk"),
                          ("werken", "werkte, gewerkt: zwak"),
                          ("zingen", "zong, gezongen: sterk"),
                          ("leren", "leerde, geleerd: zwak")],
                  "Verleden tijd, deelwoord, soort", WL),
             ]),
        dict(kop="Woordvorming",
             opdracht="Schrijf erbij of het een samenstelling, een afleiding of allebei is.",
             oefeningen=[
                 ("rij", [("boekenkast", "samenstelling"),
                          ("onvriendelijk", "afleiding"),
                          ("werkloosheid", "afleiding"),
                          ("tandartsbezoek", "samenstelling")],
                  "Wat is het?", WW),
                 ("open", "Leg uit waarom 'verkeersbord' een samenstelling is en 'bestuurder' een "
                          "afleiding.",
                  "Een samenstelling zet twee woorden die apart bestaan aan elkaar: verkeer en "
                  "bord. Een afleiding maakt een nieuw woord met een voor- of achtervoegsel dat "
                  "niet apart bestaat: besturen plus -der.", 5),
             ]),
        dict(kop="Bedrijvend of lijdend",
             opdracht="",
             oefeningen=[
                 ("open", "Zet in de lijdende vorm: 'De gemeente vernieuwt het fietspad.'",
                  "'Het fietspad wordt door de gemeente vernieuwd.'", 3),
                 ("open", "Zet in de bedrijvende vorm: 'De ruit werd door de bal gebroken.'",
                  "'De bal brak de ruit.'", 3),
                 ("waar", "In de lijdende vorm mag de handelende persoon wegvallen.", True),
                 ("waar", "Het voltooid deelwoord van een zwak werkwoord krijgt altijd een d.", False),
             ]),
        echte_leven(
            "Vertel deze week iemand iets wat er gisteren gebeurd is, en blijf de hele tijd in de "
            "verleden tijd. Schrijf vooraf drie zinnen uit. Noteer achteraf op welk moment je "
            "toch naar de tegenwoordige tijd sprong.",
            "Er is geen juist antwoord. Bijna iedereen springt: midden in een spannend stuk gaan "
            "vertellers vanzelf naar de tegenwoordige tijd, omdat het dan dichterbij lijkt. Dat "
            "is geen fout in een gesprek, maar in een schriftelijk verslag wel.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-zinsdelen-en-samengestelde-zinnen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zinsdelen en samengestelde zinnen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk zinsdeel?",
             opdracht="Schrijf bij elk onderstreept deel de naam van het zinsdeel.",
             oefeningen=[
                 ("rij", [("<u>Mijn zus</u> leest een boek.", "onderwerp"),
                          ("Mijn zus <u>leest</u> een boek.", "persoonsvorm"),
                          ("Mijn zus leest <u>een boek</u>.", "lijdend voorwerp"),
                          ("Zij geeft <u>haar broer</u> een boek.", "meewerkend voorwerp")],
                  "Welk zinsdeel?", WL),
                 ("rij", [("Zij leest <u>in de tuin</u>.", "bijwoordelijke bepaling"),
                          ("Hij is <u>leraar</u>.", "naamwoordelijk deel van het gezegde"),
                          ("Zij wacht <u>op de bus</u>.", "voorzetselvoorwerp")],
                  "Welk zinsdeel?", WL),
             ]),
        dict(kop="Zoek het onderwerp",
             opdracht="Onderstreep in gedachten de persoonsvorm en vraag daarna: wie of wat plus "
                      "de persoonsvorm? Schrijf het onderwerp op.",
             oefeningen=[
                 ("rij", [("Gisteren kwamen de eerste zwaluwen terug.", "de eerste zwaluwen"),
                          ("In de gang hangen drie schilderijen.", "drie schilderijen"),
                          ("Er staat iemand aan de deur.", "iemand"),
                          ("Morgen vertrekken wij vroeg.", "wij")],
                  "Het onderwerp", WW),
             ]),
        dict(kop="Hoofdzin of bijzin?",
             opdracht="Duid aan wat het onderstreepte stuk is.",
             oefeningen=[
                 ("kies", "<u>Ik blijf thuis</u> omdat het regent.", ["hoofdzin", "bijzin"], 0),
                 ("kies", "Ik blijf thuis <u>omdat het regent</u>.", ["hoofdzin", "bijzin"], 1),
                 ("kies", "<u>Hij zei</u> dat hij later kwam.", ["hoofdzin", "bijzin"], 0),
                 ("kies", "Het boek <u>dat op tafel lag</u>, is weg.", ["hoofdzin", "bijzin"], 1),
             ]),
        dict(kop="Nevenschikking of onderschikking?",
             opdracht="Schrijf erbij welk soort samengestelde zin het is.",
             oefeningen=[
                 ("rij", [("Ik wilde komen, maar de trein reed niet.", "nevenschikking"),
                          ("Ik kwam niet omdat de trein niet reed.", "onderschikking"),
                          ("Zij belde en hij nam op.", "nevenschikking"),
                          ("Zij belde toen hij al sliep.", "onderschikking")],
                  "Welk soort?", WW),
                 ("open", "Hoe herken je aan de plaats van de persoonsvorm of het een bijzin is?",
                  "In een bijzin schuift de persoonsvorm naar achter: 'omdat de trein niet reed'. "
                  "In een hoofdzin staat ze op de tweede plaats: 'de trein reed niet'.", 5),
             ]),
        dict(kop="Zinnen ombouwen",
             opdracht="",
             oefeningen=[
                 ("open", "Maak van deze twee zinnen één zin met een bijzin van oorzaak: 'De weg "
                          "was glad. De bus kwam te laat.'",
                  "'De bus kwam te laat omdat de weg glad was.' Of: 'Doordat de weg glad was, "
                  "kwam de bus te laat.'", 3),
                 ("open", "Maak van deze twee zinnen één zin met een betrekkelijke bijzin: 'Het "
                          "boek ligt op tafel. Het boek is van mij.'",
                  "'Het boek dat op tafel ligt, is van mij.'", 3),
                 ("waar", "Een samengestelde zin heeft altijd meer dan één persoonsvorm.", True),
                 ("waar", "Een bijzin kan op zichzelf staan als volledige zin.", False),
             ]),
        echte_leven(
            "Zoek deze week samen met iemand een heel lange zin in een krant of op een website, "
            "en ontleed hem hardop: waar staat de persoonsvorm, wie of wat is het onderwerp, waar "
            "begint de bijzin? Schrijf de zin hier over en noteer waar jullie het oneens waren.",
            "Er is geen juist antwoord. Het punt is dat je het hardop doet: zodra je het moet "
            "uitleggen, merk je zelf waar je twijfelt. Meestal is dat bij een zinsdeel dat ver "
            "van zijn werkwoord staat.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-spelling-leestekens-en-klanken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Spelling, leestekens en klanken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoofdletter of niet?",
             opdracht="Schrijf het woord juist over.",
             oefeningen=[
                 ("rij", [("de maand (december)", "december"),
                          ("de taal (frans)", "Frans"),
                          ("de dag (maandag)", "maandag"),
                          ("het land (noorwegen)", "Noorwegen")],
                  "Juiste schrijfwijze", W),
                 ("waar", "Namen van maanden en dagen krijgen in het Nederlands een hoofdletter.", False),
                 ("waar", "Namen van talen en volkeren krijgen wel een hoofdletter.", True),
             ]),
        dict(kop="Los, vast of met een streepje?",
             opdracht="Schrijf juist over.",
             oefeningen=[
                 ("rij", [("ten minste / tenminste (op zijn minst drie)", "ten minste"),
                          ("uit eindelijk", "uiteindelijk"),
                          ("zee slang", "zeeslang"),
                          ("na apen", "na-apen")],
                  "Juiste schrijfwijze", WW),
                 ("open", "Waarom krijgt 'na-apen' een streepje en 'zeeslang' niet?",
                  "Omdat er anders twee klinkers tegen elkaar komen te staan die je samen als één "
                  "klank zou lezen: naa. Het streepje houdt de klanken uit elkaar. Bij zeeslang "
                  "botst er niets.", 5),
             ]),
        dict(kop="Het juiste leesteken",
             opdracht="Schrijf de zin juist over, met de leestekens erin.",
             oefeningen=[
                 ("open", "kom je mee vroeg hij of blijf je hier",
                  "'Kom je mee,' vroeg hij, 'of blijf je hier?'", 3),
                 ("open", "we kochten brood kaas en fruit maar we vergaten de melk",
                  "We kochten brood, kaas en fruit, maar we vergaten de melk.", 3),
                 ("open", "de reden is simpel er was geen geld meer",
                  "De reden is simpel: er was geen geld meer.", 3),
             ]),
        dict(kop="Wat doet de puntkomma?",
             opdracht="",
             oefeningen=[
                 ("kies", "'Hij zweeg; zij wachtte.' Wat doet de puntkomma hier?",
                  ["twee losse zinnen scheiden die dicht bij elkaar horen",
                   "een opsomming aankondigen",
                   "een citaat inleiden"], 0),
                 ("kies", "'Er zijn drie redenen: tijd, geld en ruimte.' Wat doet de dubbelpunt?",
                  ["een tegenstelling maken",
                   "aankondigen wat er komt",
                   "een zin afsluiten"], 1),
             ]),
        dict(kop="Klinkers en medeklinkers",
             opdracht="",
             oefeningen=[
                 ("rij", [("Hoeveel lettergrepen heeft 'aardappel'?", "drie: aard-ap-pel"),
                          ("Hoeveel lettergrepen heeft 'gemakkelijk'?", "vier: ge-mak-ke-lijk")],
                  "Antwoord", WW),
                 ("open", "Waarom schrijf je 'lopen' met één p en 'stoppen' met twee?",
                  "In lopen is de o een lange klank in een open lettergreep: lo-pen. In stoppen is "
                  "de o kort, en dan verdubbelt de medeklinker om die korte klank te bewaren: "
                  "stop-pen.", 5),
                 ("waar", "Elke lettergreep bevat minstens één klinker.", True),
             ]),
        echte_leven(
            "Dicteer deze week aan iemand een stukje tekst van vijf zinnen, en laat die persoon "
            "daarna hetzelfde bij jou doen. Zeg de leestekens niet: die moet de ander zelf horen. "
            "Noteer welke leestekens misliepen.",
            "Er is geen juist antwoord. Wat bijna altijd misloopt, is de komma bij een bijzin en "
            "het onderscheid tussen een punt en een puntkomma. Dat hoor je aan de pauze, en dat "
            "is precies de reden om het hardop te doen.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-betekenis-beeldspraak-en-gevoelswaarde-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Betekenis, beeldspraak en gevoelswaarde",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vergelijking of metafoor?",
             opdracht="Bij een vergelijking staat er 'als' of 'zoals'. Bij een metafoor niet.",
             oefeningen=[
                 ("rij", [("Hij is zo sterk als een beer.", "vergelijking"),
                          ("Hij is een beer van een vent.", "metafoor"),
                          ("Haar stem is fluweel.", "metafoor"),
                          ("Haar stem klinkt als fluweel.", "vergelijking")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Welke stijlfiguur?",
             opdracht="Schrijf de naam erbij.",
             oefeningen=[
                 ("rij", [("De wind fluisterde door de bomen.", "personificatie"),
                          ("Ik heb het je duizend keer gezegd.", "overdrijving"),
                          ("Jullie zijn hier altijd zo stipt, zie ik.", "ironie"),
                          ("'Ik ga naar de kapper, want mijn haar zit in de knoop.'", "woordspeling")],
                  "Welke stijlfiguur of humorvorm?", WL),
                 ("rij", [("Hij is niet meer onder ons.", "eufemisme"),
                          ("Een liedje dat een bekende hit grappig nadoet.", "parodie")],
                  "Welke stijlfiguur of humorvorm?", WL),
             ]),
        dict(kop="Letterlijk of figuurlijk?",
             opdracht="",
             oefeningen=[
                 ("kies", "Hij heeft de boot gemist.", ["letterlijk", "figuurlijk", "allebei mogelijk"], 2),
                 ("kies", "Zij gooide de handdoek in de ring.", ["letterlijk", "figuurlijk", "allebei mogelijk"], 2),
                 ("open", "Leg uit wat 'de boot missen' figuurlijk betekent, zonder de "
                          "uitdrukking zelf te gebruiken.",
                  "Te laat zijn voor een kans die niet terugkomt.", 3),
             ]),
        dict(kop="Gevoelswaarde",
             opdracht="Schrijf erbij of het woord positief, negatief of neutraal klinkt.",
             oefeningen=[
                 ("rij", [("zuinig", "positief"),
                          ("gierig", "negatief"),
                          ("spaarzaam", "positief"),
                          ("krenterig", "negatief")],
                  "Gevoelswaarde", W),
                 ("open", "'Zuinig', 'spaarzaam' en 'gierig' betekenen ongeveer hetzelfde. "
                          "Waarom kies je toch niet zomaar één van de drie?",
                  "Omdat de gevoelswaarde verschilt. Zuinig en spaarzaam klinken als een deugd, "
                  "gierig als een gebrek. Wie een woord kiest, geeft er meteen een oordeel bij, "
                  "ook als de feiten dezelfde zijn.", 6),
             ]),
        dict(kop="Betekenis uit de context",
             opdracht="",
             oefeningen=[
                 ("open", "'De vergadering werd na een uur geschorst, omdat de gemoederen te hoog "
                          "opliepen.' Wat betekent 'geschorst' hier, en waaraan lees je dat af?",
                  "Tijdelijk stilgelegd. Je leest het af aan 'na een uur' en aan de reden: de "
                  "sfeer liep op, dus men onderbrak. Er staat niet dat ze afgelopen was.", 5),
                 ("open", "Noem twee dingen in een zin die je helpen de betekenis van een "
                          "onbekend woord te raden.",
                  "De rest van de zin (wat er logisch past), en de bouw van het woord zelf: een "
                  "voorvoegsel als on- of her-, of een stam die je herkent uit een ander woord.", 5),
                 ("waar", "Synoniemen zijn woorden die in élke zin door elkaar mogen.", False),
             ]),
        echte_leven(
            "Leg deze week aan iemand een uitdrukking uit zonder ze zelf te gebruiken, "
            "bijvoorbeeld 'ergens geen kaas van gegeten hebben'. Schrijf vooraf je uitleg op. "
            "Noteer achteraf of de ander ze kende, en of hij een andere uitleg had.",
            "Er is geen juist antwoord. Veel uitdrukkingen hebben streekgebonden of "
            "generatiegebonden varianten, en soms blijkt de ander er iets anders onder te "
            "verstaan. Dat is geen fout van een van beiden: betekenis leeft in gebruik.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-verhalen-ontleden-verteller-tijd-en-ruimte-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Verhalen ontleden: verteller, tijd en ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk vertelstandpunt?",
             opdracht="Schrijf erbij of het een ik-verteller, een personale of een alwetende "
                      "verteller is.",
             oefeningen=[
                 ("rij", [("'Ik zag de klink bewegen en mijn hart bonsde.'",
                           "belevende ik-verteller"),
                          ("'Toen wist ik nog niet dat het mijn laatste zomer was.'",
                           "vertellende ik-verteller"),
                          ("'Hij hoorde iets in de gang en bleef stokstijf staan.'",
                           "personele hij/zij-verteller"),
                          ("'Terwijl hij wachtte, besloot zij elders het tegenovergestelde.'",
                           "alwetende verteller")],
                  "Welk perspectief?", WL),
                 ("open", "Wat is kennisvoorsprong, en wat doet ze met de spanning?",
                  "De lezer weet iets wat het personage niet weet. Dat maakt spanning: je ziet "
                  "het misgaan aankomen en het personage niet. Het omgekeerde, een "
                  "kennisachterstand, maakt nieuwsgierigheid.", 5),
             ]),
        dict(kop="Rond of vlak?",
             opdracht="",
             oefeningen=[
                 ("kies", "Een personage dat in de loop van het verhaal van mening verandert en "
                          "twijfelt, is:", ["een vlak personage", "een rond personage"], 1),
                 ("kies", "De onverstoorbare butler die enkel deuren opent, is:",
                  ["een vlak personage", "een rond personage"], 0),
                 ("open", "Wat is een antiheld? Geef één kenmerk dat hem van een held "
                          "onderscheidt.",
                  "De hoofdpersoon die de eigenschappen van een klassieke held mist: hij is "
                  "bang, zwak, twijfelend of moreel dubieus. Hij blijft wel de hoofdpersoon, en "
                  "juist daardoor vaak geloofwaardiger.", 5),
             ]),
        dict(kop="Wat gebeurt er met de tijd?",
             opdracht="Schrijf erbij of het een flashback, een flashforward of een tijdsprong is.",
             oefeningen=[
                 ("rij", [("Midden in het gesprek volgt een hoofdstuk over hun eerste ontmoeting.",
                           "een flashback"),
                          ("'Dat was de laatste keer dat hij haar zag.'", "een flashforward"),
                          ("'Drie jaar later stond het huis er nog.'", "een tijdsprong")],
                  "Wat gebeurt er?", WL),
                 ("open", "Vijf bladzijden gaan over de twee seconden voor de klap. Wat zegt dat "
                          "over de verteltijd en de vertelde tijd, en wat doet de schrijver hier?",
                  "Veel verteltijd (je leest er lang over) voor heel weinig vertelde tijd (twee "
                  "seconden). Waar een schrijver zo vertraagt, legt hij de nadruk.", 5),
             ]),
        dict(kop="Ruimte en spanning",
             opdracht="",
             oefeningen=[
                 ("open", "De fiche onderscheidt vier soorten ruimte. Noem ze alle vier, met van "
                          "elk een voorbeeld.",
                  "De geografische ruimte is de plaats zelf: een zolder, een station, een dorp "
                  "aan zee. De sociale ruimte zegt iets over de stand van de personages: een "
                  "verpauperde achterbuurt. De symbolische ruimte staat voor iets anders: een "
                  "muur voor een scheiding. De sfeerscheppende ruimte roept een stemming op: een "
                  "donker bos in een griezelverhaal.", 7),
                 ("open", "Wat is een cliffhanger, en waar staat hij meestal?",
                  "Een onafgemaakt spannend moment op het einde van een hoofdstuk of aflevering, "
                  "dat je doet doorlezen of doorkijken.", 4),
                 ("waar", "Non-fictie kan nooit spannend verteld worden.", False),
             ]),
        dict(kop="Fictie of non-fictie",
             opdracht="Schrijf erbij wat het is.",
             oefeningen=[
                 ("rij", [("een handleiding van een boormachine", "non-fictie"),
                          ("een historische roman over 1302", "fictie"),
                          ("een biografie met bronvermelding", "non-fictie"),
                          ("een kortverhaal in een tijdschrift", "fictie")],
                  "Wat is het?", WW),
                 ("open", "Een historische roman gebruikt echte gebeurtenissen. Waarom blijft het "
                          "toch fictie?",
                  "Omdat de personages, de gesprekken en de gebeurtenissen in detail verzonnen "
                  "zijn. De echte geschiedenis is het decor, niet de inhoud. Non-fictie claimt "
                  "dat het zo gebeurd is en moet dat kunnen staven.", 5),
             ]),
        echte_leven(
            "Vertel deze week iemand een boek of een reeks na, zonder het einde te verklappen. "
            "Schrijf vooraf op wie je hoofdpersoon is, wat hij wil, en wie of wat hem tegenwerkt. "
            "Noteer achteraf waar de ander vroeg: 'en dan?'",
            "Er is geen juist antwoord. Waar de ander 'en dan?' vraagt, heb je de spanningsboog "
            "goed opgebouwd. Waar hij 'wacht, wie?' vraagt, heb je een personage ingevoerd zonder "
            "te zeggen wat het in het verhaal doet.", 8),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-poezie-drama-en-literaire-stromingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Poëzie, drama en literaire stromingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De bouw van een gedicht",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["begrip", "wat het is"],
                  [["versregel", None], ["strofe", None], ["rijmschema", None], ["refrein", None]],
                  "versregel: één regel van een gedicht, ook 'vers' genoemd · strofe: een groepje "
                  "regels, met wit eromheen · rijmschema: het patroon van de rijmklanken, "
                  "bijvoorbeeld abab · refrein: een regel of strofe die telkens terugkeert",
                  "260px"),
                 ("rij", [("Hoeveel versregels telt een sonnet?", "veertien"),
                          ("Uit hoeveel regels bestaat een haiku?", "drie"),
                          ("Hoeveel lettergrepen heeft een haiku?", "vijf, zeven, vijf")],
                  "Antwoord", WW),
             ]),
        dict(kop="Welke rijmsoort?",
             opdracht="Schrijf erbij welk rijm het is.",
             oefeningen=[
                 ("rij", [("huis, muis, kruis (aan het einde van de regel)", "eindrijm"),
                          ("'de kat kwam kalm kijken'", "alliteratie"),
                          ("'de maan zat traag in haar baan'", "assonantie"),
                          ("aabb", "gepaard rijm"),
                          ("abba", "omarmend rijm")],
                  "Welke rijmsoort of welk rijmschema?", WW),
                 ("open", "Wat is een enjambement, en wat doet het met de klemtoon?",
                  "De zin loopt door over het einde van de versregel heen: de regel breekt af "
                  "terwijl de zin nog niet af is. Die breuk legt nadruk op het woord er vlak voor "
                  "en er vlak na.", 5),
             ]),
        dict(kop="Drama",
             opdracht="",
             oefeningen=[
                 ("rij", [("de voorwerpen die de spelers gebruiken: een brief, een glas",
                           "de rekwisieten"),
                          ("de kleren die de spelers dragen", "de kostumering"),
                          ("de schmink waarmee een acteur er ouder uitziet", "de grime")],
                  "Hoe heet het?", WW),
                 ("open", "Bij een opvoeringsanalyse kijk je naar alles wat de tekst níét is. "
                          "Noem vier van die middelen.",
                  "Decor, belichting, ruimte, rekwisieten, mimiek, gebaren, kostumering, grime, "
                  "en muziek en geluid. Vier daarvan volstaan.", 5),
                 ("kies", "Een stuk waarin de hoofdpersoon door zijn eigen fout ten onder gaat, "
                          "noem je:", ["een komedie", "een tragedie", "een klucht"], 1),
             ]),
        dict(kop="Stromingen op een rij",
             opdracht="Schrijf bij elk kenmerk de stroming.",
             oefeningen=[
                 ("rij", [("de mens en de rede centraal, naar het voorbeeld van de oudheid",
                           "de renaissance"),
                          ("gevoel, natuur en verlangen naar het verre en het verleden",
                           "de romantiek"),
                          ("de werkelijkheid zo nuchter mogelijk tonen, ook het lelijke",
                           "het realisme")],
                  "Welke stroming?", WL),
                 ("open", "Waarom komt een stroming meestal als reactie op de vorige? Leg uit met "
                          "romantiek en realisme.",
                  "Omdat schrijvers reageren op wat hen te ver of te eenzijdig lijkt. De "
                  "romantiek zette gevoel en verbeelding voorop; het realisme vond dat wereldvreemd "
                  "en wilde het gewone leven tonen zoals het is.", 6),
             ]),
        dict(kop="Lezen en oordelen",
             opdracht="",
             oefeningen=[
                 ("waar", "Een gedicht heeft altijd rijm.", False),
                 ("waar", "Het lyrisch ik van een gedicht is altijd de dichter zelf.", False),
                 ("open", "Wat bedoelt men met het thema van een gedicht, en waarin verschilt dat "
                          "van het onderwerp?",
                  "Het onderwerp is waarover het gaat (een boom, een afscheid). Het thema is wat "
                  "het gedicht daarmee zegt: vergankelijkheid, eenzaamheid, hoop. Twee gedichten "
                  "over hetzelfde onderwerp kunnen een heel ander thema hebben.", 6),
             ]),
        echte_leven(
            "Lees deze week een gedicht hardop voor aan iemand, en laat die persoon er daarna een "
            "voor jou lezen. Schrijf vooraf op waar jij een pauze zal leggen. Noteer achteraf wat "
            "de ander eruit haalde dat jij er niet in zag.",
            "Er is geen juist antwoord. Wie hardop leest, hoort het metrum en de enjambementen "
            "vanzelf: waar je adem tekortkomt, loopt de zin over de regel heen. En twee lezers "
            "halen er bijna nooit precies hetzelfde thema uit.", 8),
    ],
)

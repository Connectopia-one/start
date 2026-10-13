# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij aardrijkskunde 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere landen om mee te rekenen, andere gevallen om in te delen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een schema
tekenen, een oordeel verantwoorden). Wie hier iets bijschrijft, legt het eerst
naast `../../boost-doorstroom/aardrijkskunde.json`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen. Het achtervoegsel houdt ze uit elkaar van een latere Boost dubbele
finaliteit.

Alle kengetallen in de rekenoefeningen zijn verzonnen maar nagerekend: de
natuurlijke aangroei is telkens het geboortecijfer min het sterftecijfer, en
de dichtheid het aantal inwoners gedeeld door de oppervlakte.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Aardrijkskunde"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-waar-ligt-het-en-hoe-weet-je-dat-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Waar ligt het, en hoe weet je dat?",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke lijn is het?",
             opdracht="Schrijf bij elke omschrijving de naam van de lijn of het punt.",
             oefeningen=[
                 ("rij", [("de breedtecirkel van 0°", "de evenaar"),
                          ("de meridiaan van 0°", "de nulmeridiaan"),
                          ("de breedtecirkel op 23,5° N", "de Kreeftskeerkring"),
                          ("de breedtecirkel op 66,5° Z", "de zuidpoolcirkel")],
                  "Hoe heet ze?", WW),
                 ("rij", [("de lijn rond 180° waar de datum verspringt", "de datumlijn"),
                          ("het punt op 90° noorderbreedte", "de noordpool"),
                          ("de breedtecirkel op 23,5° Z", "de Steenbokskeerkring")],
                  "Hoe heet ze?", WW),
             ]),
        dict(kop="Absoluut of relatief?",
             opdracht="Duid bij elke zin aan of er absoluut of relatief gesitueerd wordt.",
             oefeningen=[
                 ("kies", "Reykjavik ligt op 64° NB en 22° WL.", ["absoluut", "relatief"], 0),
                 ("kies", "De fabriek ligt aan het Albertkanaal, ten noorden van Hasselt.",
                  ["absoluut", "relatief"], 1),
                 ("kies", "Quito ligt vlak bij de evenaar, in het Andesgebergte.",
                  ["absoluut", "relatief"], 1),
                 ("kies", "Het schip bevindt zich op 12° ZB en 47° OL.", ["absoluut", "relatief"], 0),
             ]),
        dict(kop="Fysischgeografisch of sociaaleconomisch?",
             opdracht="Vul de tabel aan. Zet in de laatste kolom F of S.",
             oefeningen=[
                 ("tabel", ["element", "waarom", "F of S"],
                  [["de Rijn", None, None],
                   ["de Europese Unie", None, None],
                   ["de Alpen", None, None],
                   ["het analfabetisme in een land", None, None],
                   ["de gematigde klimaatzone", None, None],
                   ["de talen die er gesproken worden", None, None]],
                  "Rijn F (rivier), Europese Unie S (wereldblok), Alpen F (reliëfeenheid), "
                  "analfabetisme S, gematigde klimaatzone F, talen S.",
                  "220px"),
             ]),
        dict(kop="De drie afstanden",
             opdracht="Schrijf bij elke zin of het over de werkelijke, de ervaren of de mentale afstand gaat.",
             oefeningen=[
                 ("rij", [("Van hier naar Luik is het 100 kilometer.", "werkelijke"),
                          ("Die rit duurde een eeuwigheid door de file.", "ervaren"),
                          ("Ik dacht dat Marokko veel verder lag dan Turkije.", "mentale")],
                  "Welke afstand?", WW),
                 ("open", "Geef zelf een voorbeeld uit je eigen leven waarbij de ervaren afstand niet "
                          "overeenkwam met de werkelijke afstand. Leg uit hoe dat kwam.",
                  "Bijvoorbeeld: dezelfde weg naar school voelt korter met de fiets bij mooi weer dan "
                          "te voet in de regen. Comfort, drukte en het weer bepalen de ervaren afstand.", 4),
             ]),
        dict(kop="Het kaartbeeld beoordelen",
             opdracht="",
             oefeningen=[
                 ("open", "Een wereldkaart in een Australisch klaslokaal heeft het zuiden bovenaan. "
                          "Is die kaart fout? Verantwoord je antwoord.",
                  "Nee. Dat het noorden boven staat is een gewoonte, geen regel. De kaart klopt even goed; "
                          "ze voelt alleen vreemd omdat ze tegen onze mentale kaart ingaat.", 4),
                 ("open", "Leg uit waarom Groenland op veel wereldkaarten veel te groot lijkt.",
                  "Je kan een bol niet plat maken zonder vervorming. Veel kaarten houden de hoeken kloppend "
                          "en rekken daarvoor de gebieden bij de polen uit. Afrika is in werkelijkheid ongeveer "
                          "veertien keer zo groot als Groenland.", 4),
                 ("waar", "Er bestaat één wereldkaart die tegelijk de vormen, de oppervlakten en de "
                          "afstanden juist weergeeft.", False),
                 ("waar", "Wie een kaart maakt, kiest zelf welk gebied in het midden komt.", True),
             ]),
        dict(kop="Welke bron heb je nodig?",
             opdracht="Schrijf bij elke vraag welke bron je erbij neemt.",
             oefeningen=[
                 ("rij", [("In welke klimaatzone ligt Windhoek?", "een klimaatkaart of een klimatogram"),
                          ("In welke reliëfeenheid ligt Genk?", "een reliëfkaart of hoogtekaart"),
                          ("Welke vegetatiezone ligt rond de evenaar?", "een kaart van de plantengroei")],
                  "Welke bron?", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-waar-wonen-de-mensen-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Waar wonen de mensen?",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Bevolkingsdichtheid berekenen",
             opdracht="Reken uit. Schrijf de bewerking op en zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [("6 000 000 inwoners op 20 000 km²", "300 inw/km²"),
                          ("900 000 inwoners op 45 000 km²", "20 inw/km²"),
                          ("18 000 000 inwoners op 300 000 km²", "60 inw/km²"),
                          ("250 000 inwoners op 500 km²", "500 inw/km²")],
                  "Dichtheid?", W),
                 ("open", "Land A telt 80 miljoen inwoners op 9 miljoen km². Land B telt 11 miljoen "
                          "inwoners op 30 000 km². Welk land is het dichtst bevolkt? Reken het uit.",
                  "Land A: 80 000 000 : 9 000 000 is ongeveer 9 inw/km². Land B: 11 000 000 : 30 000 is "
                          "ongeveer 367 inw/km². Land B is veel dichter bevolkt, hoewel het veel minder "
                          "inwoners telt.", 5),
             ]),
        dict(kop="Waarom dun of dicht bevolkt?",
             opdracht="Vul in welke factor het sterkst meespeelt: klimaat, bodemkwaliteit of reliëf.",
             oefeningen=[
                 ("tabel", ["gebied", "dun of dicht", "welke factor"],
                  [["de Sahara", None, None],
                   ["het noorden van Canada", None, None],
                   ["de Nijlvallei", None, None],
                   ["het hooggebergte van de Andes", None, None],
                   ["de delta van de Ganges", None, None]],
                  "Sahara dun, klimaat (te droog). Noord-Canada dun, klimaat (te koud, bevroren bodem). "
                  "Nijlvallei dicht, water en bodemkwaliteit. Hooggebergte dun, reliëf. Ganges-delta "
                  "dicht, bodemkwaliteit (vruchtbaar slib) en klimaat.",
                  "150px"),
             ]),
        dict(kop="Wat zegt een dichtheid niet?",
             opdracht="",
             oefeningen=[
                 ("open", "Twee gemeenten hebben allebei 300 inwoners per km². In de ene wonen bijna alle "
                          "mensen in één dorpskern, in de andere wonen ze verspreid over het hele "
                          "grondgebied. Leg uit waarom dezelfde dichtheid toch een heel ander landschap kan "
                          "betekenen.",
                  "Dichtheid is een gemiddelde over de hele oppervlakte en zegt niets over het patroon "
                          "binnen dat gebied. Verspreide bewoning betekent meer wegen, meer versnippering en "
                          "meer autokilometers dan een compacte kern.", 5),
                 ("waar", "Een land met veel inwoners heeft daardoor een hoge bevolkingsdichtheid.", False),
                 ("waar", "Een dichtbevolkt gebied is daarom een rijk gebied.", False),
             ]),
        dict(kop="De Human Development Index",
             opdracht="",
             oefeningen=[
                 ("open", "Uit welke drie onderdelen is de HDI opgebouwd?",
                  "Levensverwachting (gezondheid), het aantal jaren onderwijs, en het gemiddelde inkomen "
                          "per inwoner.", 3),
                 ("kort", "Tussen welke twee getallen ligt een HDI-waarde altijd?", "tussen 0 en 1", WW),
                 ("kort", "Welke organisatie publiceert de HDI elk jaar?", "de Verenigde Naties", WW),
                 ("open", "Land C heeft een hoog inkomen per inwoner maar weinig scholen en ziekenhuizen. "
                          "Wat verwacht je van zijn HDI in vergelijking met een land met hetzelfde inkomen "
                          "maar goed onderwijs en goede zorg? Leg uit.",
                  "Lager. De HDI telt gezondheid en onderwijs mee naast het inkomen, dus een land dat enkel "
                          "op inkomen scoort, komt lager uit. Dat is precies waarom de HDI beter is dan het "
                          "inkomen alleen.", 5),
             ]),
        dict(kop="Een bron kritisch bekijken",
             opdracht="",
             oefeningen=[
                 ("open", "Je krijgt een wereldkaart van de HDI zonder jaartal en zonder bronvermelding. "
                          "Noem drie dingen die je wil weten voor je er iets uit besluit.",
                  "Van welk jaar de cijfers zijn, wie ze verzameld heeft, en welke klassen de legende "
                          "gebruikt. Door de klassen anders te kiezen ziet dezelfde kaart er heel anders uit.", 4),
                 ("open", "Waarom zegt een nationale HDI weinig over één bepaalde streek in dat land?",
                  "Het is een gemiddelde over het hele land. In veel landen scoort de hoofdstad veel hoger "
                          "dan het platteland, en dat verschil verdwijnt in dat ene cijfer.", 4),
                 ("waar", "Een land met een lage HDI is een land waar niemand rijk is.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-hoe-een-bevolking-verandert-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Hoe een bevolking verandert",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Natuurlijke aangroei berekenen",
             opdracht="Reken uit. Vergeet het teken niet: een min mag.",
             oefeningen=[
                 ("rij", [("geboorte 22 ‰, sterfte 7 ‰", "+15 ‰"),
                          ("geboorte 9 ‰, sterfte 12 ‰", "−3 ‰"),
                          ("geboorte 31 ‰, sterfte 8 ‰", "+23 ‰"),
                          ("geboorte 10 ‰, sterfte 10 ‰", "0 ‰")],
                  "Aangroei?", W),
                 ("rij", [("immigratie 40 000, emigratie 25 000", "+15 000"),
                          ("immigratie 12 000, emigratie 31 000", "−19 000")],
                  "Migratiesaldo?", W),
                 ("open", "Een land heeft een natuurlijke aangroei van −2 ‰ en een migratiesaldo van "
                          "+6 ‰. Groeit of krimpt de bevolking? Leg uit met een bewerking.",
                  "De totale groei is −2 + 6 = +4 ‰, dus de bevolking groeit. Dat de natuurlijke aangroei "
                          "negatief is, wordt meer dan goedgemaakt door de migratie.", 4),
             ]),
        dict(kop="Het histogram lezen",
             opdracht="",
             oefeningen=[
                 ("rij", [("brede basis, smalle top", "piramide, hoog geboortecijfer"),
                          ("smalle basis, brede top", "urn, sterke vergrijzing"),
                          ("overal ongeveer even breed", "klok, geboortecijfer al jaren stabiel")],
                  "Welke vorm, en wat betekent ze?", WL),
                 ("open", "In een histogram zit rond de leeftijd van 75 tot 80 jaar een duidelijke "
                          "inkeping. Noem twee mogelijke verklaringen.",
                  "Een oorlog of een crisis rond de geboortejaren van die groep, waardoor er toen veel "
                          "minder kinderen geboren werden. Of een beleid dat gezinnen toen beperkte. Zo'n "
                          "deuk schuift het hele leven mee omhoog.", 4),
                 ("open", "Waarom krijgt een land met veel immigratie bredere balken rond de twintig tot "
                          "veertig jaar?",
                  "Wie migreert, is meestal jongvolwassen: mensen trekken weg voor werk of studie. Die "
                          "leeftijdsgroepen worden daardoor groter.", 3),
             ]),
        dict(kop="In welke fase zit dit land?",
             opdracht="Schrijf de fase op, en schrijf erbij waarom.",
             oefeningen=[
                 ("tabel", ["land", "geboorte", "sterfte", "fase", "waarom"],
                  [["land A", "41 ‰", "37 ‰", None, None],
                   ["land B", "36 ‰", "10 ‰", None, None],
                   ["land C", "22 ‰", "9 ‰", None, None],
                   ["land D", "10 ‰", "9 ‰", None, None]],
                  "A fase 1 (beide hoog, nauwelijks groei). B fase 2 (sterfte gedaald, geboorte nog hoog, "
                  "snelle groei). C fase 3 (geboorte aan het dalen). D fase 4 (beide laag).",
                  "110px"),
             ]),
        dict(kop="Push of pull?",
             opdracht="Zet achter elke factor P voor push of T voor pull (trekken).",
             oefeningen=[
                 ("rij", [("aanhoudende droogte in de eigen streek", "push"),
                          ("familie die al in het nieuwe land woont", "pull"),
                          ("een gewapend conflict", "push"),
                          ("goed onderwijs voor de kinderen", "pull"),
                          ("werkloosheid in de eigen streek", "push"),
                          ("kans op werk elders", "pull")],
                  "Push of pull?", W),
                 ("open", "Leg uit waarom de meeste mensen die vluchten, in een buurland terechtkomen en "
                          "niet aan de andere kant van de wereld.",
                  "De reis is korter en goedkoper, de taal ligt vaak dichter bij de eigen taal, en er wonen "
                          "al bekenden. Een verre reis kost geld dat vluchtende mensen net niet hebben.", 4),
             ]),
        dict(kop="Vergrijzing, braindrain en braingain",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe noem je het vertrek van hoogopgeleide mensen uit een land?", "braindrain", WW),
                 ("kort", "En de aankomst ervan in een ander land?", "braingain", WW),
                 ("open", "Noem drie gevolgen van sterke vergrijzing voor een land.",
                  "Meer uitgaven aan pensioenen, meer vraag naar zorg voor ouderen, en minder mensen op de "
                          "arbeidsmarkt. Scholen komen juist leeg te staan.", 4),
                 ("waar", "Braindrain is voor het land van vertrek vooral een voordeel.", False),
                 ("waar", "Vergrijzing betekent dat het aantal inwoners van een land daalt.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stad-en-platteland-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Stad en platteland",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Economisch, cultureel of politiek?",
             opdracht="Schrijf bij elk kenmerk welk soort belang het aantoont.",
             oefeningen=[
                 ("rij", [("het hoofdkwartier van een internationale bank", "economisch"),
                          ("een universiteit met een groot onderzoekscentrum", "cultureel"),
                          ("de zetel van de regering", "politiek"),
                          ("een grote beurs voor de handel", "economisch"),
                          ("drie grote musea en een operahuis", "cultureel")],
                  "Welk belang?", WW),
                 ("open", "Brussel is niet de grootste stad van Europa en staat toch hoog in de "
                          "stedenhiërarchie. Leg uit waarom.",
                  "Door de Europese instellingen en de NAVO heeft het een groot politiek belang, en dat "
                          "trekt diplomaten, lobbyisten en internationale bedrijven aan. Hiërarchie gaat over "
                          "belang, niet over inwonersaantal.", 4),
             ]),
        dict(kop="Welke verandering is het?",
             opdracht="Kies uit: verstedelijking van het platteland, ontvolking, inbreiding, "
                      "veranderende mobiliteit, stadslandbouw.",
             oefeningen=[
                 ("rij", [("een moestuin op het dak van een parkeergarage", "stadslandbouw"),
                          ("drie nieuwe verkavelingen rond een dorpskern", "verstedelijking van het platteland"),
                          ("een leeg fabrieksterrein midden in de stad wordt volgebouwd", "inbreiding"),
                          ("een dorp waar de laatste school sluit", "ontvolking"),
                          ("een nieuwe fietssnelweg naar het centrum", "veranderende mobiliteit")],
                  "Welke verandering?", WL),
             ]),
        dict(kop="Segregatie of multiculturaliteit?",
             opdracht="",
             oefeningen=[
                 ("open", "Leg in je eigen woorden het verschil uit tussen sociale segregatie en "
                          "multiculturaliteit.",
                  "Multiculturaliteit gaat over wie er samen in een stad woont: mensen met verschillende "
                          "achtergronden en tradities. Segregatie gaat over de vraag of die groepen ook door "
                          "elkaar wonen. Een stad kan heel divers zijn en tegelijk sterk gescheiden.", 5),
                 ("open", "Wat is in West-Europese steden de belangrijkste motor achter sociale "
                          "segregatie?",
                  "Het verschil in woningprijs tussen wijken. Wie weinig kan betalen, belandt in de "
                          "goedkoopste woningen, en die liggen bij elkaar. Zo ontstaat scheiding zonder dat "
                          "iemand ze oplegt.", 4),
             ]),
        dict(kop="Verharding en hitte",
             opdracht="",
             oefeningen=[
                 ("open", "Een gemeente breekt een betonnen marktplein open en plant er twaalf bomen. "
                          "Noem twee problemen die ze daarmee aanpakt, en leg bij elk uit hoe dat werkt.",
                  "Het hitte-eilandeffect: bomen geven schaduw en verdampen water, en dat koelt. En het "
                          "wegstromen van regenwater: onverharde grond laat het water insijpelen, zodat het "
                          "grondwater aanvult en de riool niet overloopt.", 6),
                 ("kort", "Hoe heet het verschijnsel waarbij het in een stad warmer is dan op het "
                          "platteland eromheen?", "het hitte-eilandeffect", WL),
                 ("kort", "Hoe noem je het opdelen van de open ruimte in kleine losse stukken?",
                  "versnippering", WW),
                 ("waar", "Verstedelijking betekent alleen dat steden meer inwoners krijgen.", False),
             ]),
        dict(kop="Twee luchtfoto's vergelijken",
             opdracht="",
             oefeningen=[
                 ("open", "Je legt een luchtfoto van je gemeente uit 1975 naast een van vorig jaar. "
                          "Waaraan zie je verstedelijking, en waarop moet je letten bij het vergelijken?",
                  "Je ziet bebouwing en verharding toenemen ten koste van akkers en weiden. Let erop dat "
                          "beide foto's in hetzelfde seizoen en op dezelfde schaal genomen zijn, anders "
                          "vergelijk je appelen met peren.", 5),
                 ("open", "Een dorp krijgt er twintig jaar lang huizen bij, maar geen enkele nieuwe winkel "
                          "of school. Wat gebeurt er met dat dorp? Gebruik het woord woondorp.",
                  "Het wordt een woondorp: mensen wonen er maar werken, winkelen en gaan naar school "
                          "elders. De autoafhankelijkheid neemt toe en het pendelverkeer groeit.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grondstoffen-energie-en-industrie-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Grondstoffen, energie en industrie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Groeve of mijn, traditioneel of modern",
             opdracht="",
             oefeningen=[
                 ("rij", [("men graaft van bovenaf, in open lucht", "een groeve, dagbouw"),
                          ("men maakt schachten en gangen naar een diepe laag", "een mijn"),
                          ("mensen graven met eenvoudig gereedschap", "traditionele ontginning"),
                          ("zware machines verzetten veel tegelijk", "moderne ontginning")],
                  "Wat is dit?", WL),
                 ("open", "Waarom kiest een bedrijf voor dagbouw als de laag ondiep genoeg ligt? Noem twee "
                          "redenen, en noem ook één nadeel.",
                  "Het is goedkoper en veiliger dan ondergronds werken: geen schachten, geen "
                          "instortingsgevaar, en grote machines kunnen veel tegelijk verzetten. Het nadeel "
                          "is dat er een hele laag grond verdwijnt, dus het landschap verandert ingrijpender.", 5),
             ]),
        dict(kop="Hernieuwbaar of niet?",
             opdracht="Zet achter elke bron H of N.",
             oefeningen=[
                 ("rij", [("wind op de Noordzee", "H"),
                          ("aardgas", "N"),
                          ("uranium voor kernenergie", "N"),
                          ("waterkracht in een stuwdam", "H"),
                          ("steenkool", "N"),
                          ("zonlicht op een dak", "H")],
                  "H of N?", W),
                 ("open", "Een kerncentrale stoot bij de productie nauwelijks CO₂ uit. Waarom noemen we "
                          "kernenergie toch niet hernieuwbaar?",
                  "Hernieuwbaar gaat over de bron, niet over de uitstoot. Uranium moet ontgonnen worden en "
                          "raakt op, en er blijft radioactief afval over.", 4),
             ]),
        dict(kop="Waar zet je het neer?",
             opdracht="Schrijf bij elk geval welke factor de plaats bepaalt.",
             oefeningen=[
                 ("tabel", ["installatie", "waar", "welke factor"],
                  [["een windmolenpark", None, None],
                   ["een zonnepark", None, None],
                   ["een waterkrachtcentrale", None, None],
                   ["een chemisch bedrijf", None, None]],
                  "Windmolenpark: op zee of in open landschap, want daar waait het harder en constanter. "
                  "Zonnepark: waar veel zonuren zijn, want de opbrengst per paneel is er hoger. "
                  "Waterkrachtcentrale: in bergachtige streken met veel neerslag of smeltwater, want ze "
                  "heeft hoogteverschil en watertoevoer nodig. Chemisch bedrijf: aan een haven, want "
                  "grondstoffen komen per schip binnen.",
                  "180px"),
             ]),
        dict(kop="Geopolitiek, fysisch of sociaaleconomisch?",
             opdracht="Zet achter elke factor G, F of S.",
             oefeningen=[
                 ("rij", [("de stabiliteit van het land", "G"),
                          ("het reliëf van de streek", "F"),
                          ("de verloning van de werknemers", "S"),
                          ("de samenwerkingsverbanden met andere landen", "G"),
                          ("de grondstoffen in de bodem", "F"),
                          ("de afzetmarkt van het product", "S"),
                          ("de staatsvorm", "G"),
                          ("de Human Development Index", "S")],
                  "G, F of S?", W),
             ]),
        dict(kop="Industrialisatie, de-industrialisatie, reconversie",
             opdracht="",
             oefeningen=[
                 ("rij", [("de mijnen sluiten en het werk verdwijnt", "de-industrialisatie"),
                          ("op de oude mijnsite komt een wetenschapspark", "reconversie"),
                          ("er komen nieuwe fabrieken bij in de streek", "industrialisatie")],
                  "Welk begrip?", WW),
                 ("open", "Noem drie gevolgen voor een streek waar een grote fabriek sluit.",
                  "De werkloosheid stijgt in de omliggende gemeenten, jongeren trekken weg op zoek naar "
                          "werk, en er komt een groot terrein leeg te staan.", 4),
                 ("open", "Waarom liggen nieuwe bedrijventerreinen vaak bij een snelwegafrit buiten de "
                          "stad, en wat is daar het nadeel van?",
                  "De grond is er goedkoper en vrachtwagens geraken er vlot weg. Het nadeel is dat werk uit "
                          "de stadskernen wegtrekt en dat de open ruimte verder versnippert.", 5),
                 ("waar", "Een land met grote grondstofvoorraden is daardoor vanzelf welvarend.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-landbouw-handel-en-toerisme-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Landbouw, handel en toerisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waar groeit wat, en waarom?",
             opdracht="Schrijf bij elk gewas het klimaat dat het nodig heeft.",
             oefeningen=[
                 ("tabel", ["gewas", "waar vooral", "welk klimaat"],
                  [["rijst", None, None],
                   ["olijven", None, None],
                   ["cacao", None, None],
                   ["koffie", None, None]],
                  "Rijst: Zuid- en Oost-Azië, warm met veel neerslag in het groeiseizoen (moesson). "
                  "Olijven: rond de Middellandse Zee, droge warme zomer en zachte natte winter. "
                  "Cacao: West-Afrika, warm laagland van de tropen. "
                  "Koffie: tropische hooglanden, warm maar koeler door de hoogte.",
                  "170px"),
                 ("open", "Waarom is de zwarte aarde van Oekraïne zo geschikt voor graanteelt?",
                  "Ze is heel vruchtbaar en rijk aan humus en houdt water goed vast. Samen met het vlakke "
                          "reliëf maakt dat van die streek een van de graanschuren van de wereld.", 4),
             ]),
        dict(kop="Extensief of intensief?",
             opdracht="",
             oefeningen=[
                 ("rij", [("schapenteelt op duizenden hectare in Australië", "extensief"),
                          ("tomaten in verwarmde serres", "intensief"),
                          ("rijstterrassen die met de hand bewerkt worden", "intensief"),
                          ("graan op grote velden met weinig arbeid", "extensief")],
                  "Extensief of intensief?", WW),
                 ("open", "Leg het verschil uit tussen de opbrengst per hectare en de opbrengst per "
                          "werkende. Geef bij elk een voorbeeld.",
                  "Per hectare telt hoeveel één stuk grond opbrengt: rijstterrassen die met de hand "
                          "bewerkt worden, halen per hectare veel. Per werkende telt hoeveel één mens "
                          "opbrengt: daar wint moderne landbouw met machines het ruim.", 5),
             ]),
        dict(kop="Duurzaam of niet?",
             opdracht="Zet achter elke praktijk D of N, en schrijf er in één zin bij waarom.",
             oefeningen=[
                 ("tabel", ["praktijk", "D of N", "waarom"],
                  [["jaar na jaar hetzelfde gewas op hetzelfde perceel", None, None],
                   ["een groenbedekker inzaaien na de oogst", None, None],
                   ["recht van boven naar beneden ploegen op een helling", None, None],
                   ["hagen en houtkanten laten staan", None, None],
                   ["meer bemesten dan de teelt opneemt", None, None]],
                  "1 N: put de bodem uit, geen vruchtwisseling. 2 D: dekt de bodem, tegen erosie. "
                  "3 N: de regen spoelt de bovenlaag weg; ploeg dwars op de helling. 4 D: remt de wind "
                  "en geeft leefruimte. 5 N: het overschot belandt in het grond- en oppervlaktewater.",
                  "110px"),
                 ("kort", "Hoe noem je het wegspoelen van de vruchtbare bovenlaag?", "bodemerosie", WW),
                 ("kort", "Hoe noem je minder bedrijven die elk meer grond bewerken?", "schaalvergroting", WW),
             ]),
        dict(kop="Handel en diensten",
             opdracht="",
             oefeningen=[
                 ("rij", [("levert in grote hoeveelheden aan winkels", "groothandel"),
                          ("verkoopt rechtstreeks aan de consument", "kleinhandel"),
                          ("onderwijs, zorg, transport en toerisme samen", "de dienstensector")],
                  "Hoe heet dit?", WL),
                 ("open", "Waarom liggen grote distributiecentra langs autosnelwegen en niet in het "
                          "stadscentrum?",
                  "Ze hebben veel oppervlakte en veel vrachtverkeer nodig, en dat is in een stadscentrum "
                          "onbetaalbaar en onmogelijk. Online winkelen verschuift zo werk van de winkelstraat "
                          "naar de rand van het land.", 4),
             ]),
        dict(kop="Toerisme beoordelen",
             opdracht="",
             oefeningen=[
                 ("rij", [("veel zonuren en een kust met stranden", "fysisch"),
                          ("een stabiele politieke situatie", "geopolitiek"),
                          ("bergen die lang sneeuw houden", "fysisch"),
                          ("een hoge Human Development Index", "sociaaleconomisch")],
                  "Welke soort factor?", WL),
                 ("open", "Noem drie ruimtelijke gevolgen van massatoerisme voor een kuststreek.",
                  "Bebouwing die de duinen en de open ruimte opslorpt, druk op het drinkwater in het "
                          "hoogseizoen, en woningen die voor de eigen bewoners onbetaalbaar worden.", 4),
                 ("open", "Waarom is een streek die bijna volledig op toerisme draait, kwetsbaar?",
                  "Wie op één sector steunt, verliest bij een crisis alles tegelijk. Een epidemie, een "
                          "aanslag of een economische crisis in de herkomstlanden doet het inkomen van een "
                          "hele streek ineens wegvallen.", 4),
                 ("waar", "Een stad zonder strand kan geen toeristen aantrekken.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mondialisering-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Mondialisering",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De ketting van een product",
             opdracht="Zet de stappen van een gsm in de juiste orde, van 1 tot 5.",
             oefeningen=[
                 ("rij", [("de gsm wordt in een winkel in Europa verkocht", "5"),
                          ("kobalt en coltan worden ontgonnen in Congo", "1"),
                          ("de onderdelen worden in China in elkaar gezet", "3"),
                          ("de ertsen worden verwerkt tot metaal", "2"),
                          ("de toestellen gaan per containerschip de wereld rond", "4")],
                  "Welke stap?", W),
                 ("open", "Waarom liggen de winst en de vervuiling van zo'n ketting niet op dezelfde "
                          "plaats? Leg uit met de gsm als voorbeeld.",
                  "Het ontginnen en het assembleren gebeuren waar de lonen laag zijn en de regels minder "
                          "streng; daar blijft de vervuiling en het gevaarlijke werk. Het ontwerp, het merk en "
                          "de verkoop zitten in rijke landen, en daar zit ook het grootste deel van de winst.", 5),
             ]),
        dict(kop="Welke stroom is het?",
             opdracht="Goederen, kapitaal, mensen of informatie?",
             oefeningen=[
                 ("rij", [("containerschepen tussen Sjanghai en Antwerpen", "goederen"),
                          ("een bedrijf dat in het buitenland een fabriek bouwt", "kapitaal"),
                          ("arbeidsmigratie naar West-Europa", "mensen"),
                          ("zeekabels die het internet dragen", "informatie"),
                          ("geld dat migranten naar hun familie sturen", "kapitaal"),
                          ("toeristen naar de Spaanse kust", "mensen")],
                  "Welke stroom?", WW),
                 ("kort", "Hoe noem je het geld dat migranten naar hun familie in het thuisland sturen?",
                  "remittances (overmakingen)", WL),
             ]),
        dict(kop="Voor- of nadeel, en voor wie?",
             opdracht="Vul in.",
             oefeningen=[
                 ("tabel", ["gevolg van mondialisering", "voordeel voor", "nadeel voor"],
                  [["een fabriek verhuist naar een land met lagere lonen", None, None],
                   ["goederen worden goedkoper door wereldwijde concurrentie", None, None],
                   ["één wereldwijde crisis raakt alle landen tegelijk", None, None],
                   ["Engels wordt overal de tweede taal", None, None]],
                  "1 Voordeel voor het ontvangende land (werk, inkomen) en voor het bedrijf; nadeel voor de "
                  "werknemers die hun job verliezen. 2 Voordeel voor de koper; nadeel voor producenten die "
                  "niet aan die prijs kunnen werken. 3 Geen voordeel; nadeel voor iedereen, want de "
                  "verbondenheid maakt kwetsbaar. 4 Voordeel om elkaar te begrijpen; nadeel voor kleinere "
                  "talen en culturen die verdrukt raken.",
                  "150px"),
             ]),
        dict(kop="Mondialisering of niet?",
             opdracht="Zet er M bij als het een gevolg van mondialisering is, en N als het er niets "
                      "mee te maken heeft.",
             oefeningen=[
                 ("rij", [("dezelfde winkelketens in elke Europese stad", "M"),
                          ("de seizoenen in ons land", "N"),
                          ("aardbeien in de winter in de supermarkt", "M"),
                          ("het reliëf van de Ardennen", "N"),
                          ("een callcenter in India voor een Belgisch bedrijf", "M")],
                  "M of N?", W),
                 ("waar", "Mondialisering betekent dat alle landen even veel meegenieten van de "
                          "wereldhandel.", False),
                 ("waar", "Mondialisering is niet nieuw: de zijderoute en de scheepvaart waren er al "
                          "vroege vormen van.", True),
             ]),
        dict(kop="Wie beslist mee?",
             opdracht="",
             oefeningen=[
                 ("kies", "Welke reden legt het best uit waarom een multinational soms meer invloed heeft "
                          "op een streek dan de gemeente zelf?",
                  ["Het beslist over werk en investeringen waar duizenden mensen van leven.",
                   "Het bedrijf heeft meer personeel in dienst dan de gemeente ambtenaren heeft.",
                   "Een groot bedrijf mag de wetten van een land aanpassen als het daar gevestigd is.",
                   "Een gemeente mag zelf geen beslissingen nemen over haar bedrijventerreinen."], 0),
                 ("open", "Noem twee dingen die een land of een gemeente wél in de hand heeft tegenover "
                          "een groot internationaal bedrijf.",
                  "Ze bepaalt de regels waaraan het bedrijf zich op haar grond moet houden (milieu, "
                          "veiligheid, ruimtelijke ordening) en ze beslist of ze grond en vergunningen geeft. "
                          "Samenwerken met andere landen maakt die positie sterker.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-duurzaam-omgaan-met-de-ruimte-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Duurzaam omgaan met de ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke p is het?",
             opdracht="People, planet of profit?",
             oefeningen=[
                 ("rij", [("de werknemers krijgen een leefbaar loon", "people"),
                          ("de fabriek loost geen afvalwater in de beek", "planet"),
                          ("het bedrijf blijft op lange termijn rendabel", "profit"),
                          ("de buurt wordt gehoord bij het plan", "people"),
                          ("er blijft bodem over die water doorlaat", "planet")],
                  "Welke p?", WW),
                 ("open", "Waarom is een plan dat op één van de drie p's uitstekend scoort en op de twee "
                          "andere slecht, tóch niet duurzaam?",
                  "Duurzaam betekent dat de drie samen in evenwicht zijn. Een fabriek die veel winst maakt "
                          "maar de buurt ziek maakt, of een natuurplan dat mensen hun inkomen kost, houdt geen "
                          "stand: wat op één p misloopt, komt vroeg of laat op de andere terug.", 5),
             ]),
        dict(kop="Wat is het gevolg van verharding?",
             opdracht="Vul de gevolgen aan.",
             oefeningen=[
                 ("tabel", ["wat verhard wordt", "waar gaat het regenwater naartoe", "welk gevolg"],
                  [["een tuin wordt opgereden met klinkers", None, None],
                   ["een weide wordt een parking", None, None],
                   ["een beek wordt in een buis gelegd", None, None]],
                  "Het water kan niet in de bodem, loopt versneld naar de riool of de beek en zorgt "
                  "verderop voor wateroverlast. Tegelijk zakt het grondwater, want het wordt niet meer "
                  "aangevuld, en in de zomer warmt de verharde plek harder op.",
                  "160px"),
                 ("kort", "Hoe noem je het verschijnsel dat een stad warmer is dan het platteland eromheen?",
                  "het hitte-eilandeffect", WL),
                 ("kort", "Hoe noem je het versnipperen van open ruimte door gebouwen en wegen?",
                  "versnippering", WW),
             ]),
        dict(kop="Wie heeft er belang bij?",
             opdracht="Een gemeente wil een weide van tien hectare aan de rand van het dorp omvormen tot "
                      "bedrijventerrein. Schrijf bij elke partij wat ze wil, en waarom.",
             oefeningen=[
                 ("tabel", ["partij", "wil het plan wel of niet", "waarom"],
                  [["de eigenaar van de weide", None, None],
                   ["een bedrijf dat wil uitbreiden", None, None],
                   ["de buren van de weide", None, None],
                   ["een natuurvereniging", None, None],
                   ["het gemeentebestuur", None, None]],
                  "Eigenaar: wel, bouwgrond brengt veel meer op dan weiland. Bedrijf: wel, het heeft "
                  "ruimte en een goede ligging nodig. Buren: meestal niet, meer verkeer, lawaai en minder "
                  "groen. Natuurvereniging: niet, open ruimte en bodem die water doorlaat verdwijnen. "
                  "Gemeentebestuur: verdeeld, werk en inkomsten tegenover open ruimte en de tevredenheid "
                  "van de inwoners.",
                  "130px"),
                 ("open", "Bedenk één aanpassing aan het plan die het voor twee van die partijen beter "
                          "maakt zonder het voor de andere onmogelijk te maken.",
                  "Bijvoorbeeld: een leegstaand bedrijventerrein hergebruiken in plaats van de weide aan "
                          "te snijden, of, als de weide toch nodig is, een groene bufferstrook met bomen naar "
                          "de buren en waterdoorlatende parkeerplaatsen aanleggen. Het bedrijf kan nog bouwen, "
                          "de buren en de natuur verliezen minder.", 6),
             ]),
        dict(kop="Beoordeel de maatregel",
             opdracht="Zet achter elke maatregel D als hij duurzamer is en S als hij het probleem "
                      "verschuift.",
             oefeningen=[
                 ("rij", [("een oude fabrieksite hergebruiken in plaats van een nieuw terrein aan te snijden",
                           "D"),
                          ("afval naar een ander land verschepen", "S"),
                          ("waterdoorlatende klinkers op een parking leggen", "D"),
                          ("de fabriek verhuizen naar een land met minder strenge regels", "S"),
                          ("een kanaal gebruiken in plaats van vrachtwagens", "D")],
                  "D of S?", W),
                 ("waar", "Duurzaam betekent dat er niets meer mag veranderen in een landschap.", False),
                 ("waar", "Een windmolenpark op zee heeft ook nadelen, bijvoorbeeld voor de scheepvaart "
                          "en voor het leven op de zeebodem.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-versterkte-broeikaseffect-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Het versterkte broeikaseffect",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het natuurlijke effect",
             opdracht="",
             oefeningen=[
                 ("open", "Leg in drie stappen uit hoe het natuurlijke broeikaseffect werkt.",
                  "Zonlicht komt door de atmosfeer en warmt het aardoppervlak op. Het oppervlak straalt "
                          "die warmte terug als warmtestraling. Broeikasgassen houden een deel van die "
                          "warmtestraling tegen en stralen ze terug naar beneden, waardoor het aan het "
                          "oppervlak warmer blijft.", 6),
                 ("kort", "Hoe koud zou het gemiddeld op aarde zijn zonder broeikaseffect?",
                  "ongeveer -18 °C", WW),
                 ("waar", "Het natuurlijke broeikaseffect is schadelijk en moet verdwijnen.", False),
             ]),
        dict(kop="Welk gas, en waar komt het vandaan?",
             opdracht="",
             oefeningen=[
                 ("tabel", ["gas", "belangrijkste menselijke bron"],
                  [["koolstofdioxide (CO₂)", None],
                   ["methaan (CH₄)", None],
                   ["lachgas (N₂O)", None]],
                  "CO₂: het verbranden van steenkool, olie en aardgas, plus ontbossing. "
                  "Methaan: veeteelt (herkauwers), rijstteelt, stortplaatsen en gaslekken. "
                  "Lachgas: kunstmest en mest in de landbouw.",
                  "260px"),
                 ("kies", "Waterdamp is het sterkste broeikasgas. Waarom staat het toch niet bovenaan de "
                          "lijst van gassen die we moeten terugdringen?",
                  ["De hoeveelheid waterdamp volgt vanzelf de temperatuur en stoten wij niet "
                   "rechtstreeks uit.",
                   "Waterdamp houdt de warmtestraling van het aardoppervlak helemaal niet tegen en "
                   "speelt dus geen rol.",
                   "Er zit te weinig waterdamp in de lucht om enig verschil te maken voor de "
                   "temperatuur op aarde.",
                   "Waterdamp komt alleen boven de oceanen voor en blijft weg boven het land."], 0),
             ]),
        dict(kop="Terugkoppeling: versterkend of dempend?",
             opdracht="Zet achter elk geval V of D.",
             oefeningen=[
                 ("rij", [("zee-ijs smelt, de donkere zee neemt meer warmte op", "V"),
                          ("permafrost dooit en laat methaan vrij", "V"),
                          ("meer plantengroei neemt meer CO₂ op", "D"),
                          ("warmere lucht houdt meer waterdamp vast", "V")],
                  "V of D?", W),
                 ("open", "Leg uit wat albedo is en waarom smeltend zee-ijs de opwarming versnelt.",
                  "Albedo is hoeveel van het zonlicht een oppervlak terugkaatst. Sneeuw en ijs hebben een "
                          "hoog albedo en kaatsen het meeste licht terug; open zeewater is donker en heeft een "
                          "laag albedo, dus het neemt de warmte op. Smelt het ijs, dan wordt meer zonlicht "
                          "opgenomen, warmt het water verder op en smelt er nog meer ijs.", 6),
             ]),
        dict(kop="Gevolgen op hun plaats",
             opdracht="Schrijf bij elk gevolg één streek of land waar het nu al speelt.",
             oefeningen=[
                 ("tabel", ["gevolg", "waar", "waarom daar"],
                  [["zeespiegelstijging bedreigt het land", None, None],
                   ["gletsjers worden korter", None, None],
                   ["langere droogteperiodes", None, None],
                   ["de permafrost dooit", None, None]],
                  "Zeespiegel: laaggelegen kuststreken en eilandstaten, bijvoorbeeld Bangladesh of de "
                  "Malediven, want daar ligt het land amper boven zeeniveau. Gletsjers: de Alpen en de "
                  "Himalaya, want die halen hun ijs uit sneeuw die nu vaker als regen valt. Droogte: het "
                  "Middellandse Zeegebied en de Sahel, want daar was het neerslagtekort al groot. "
                  "Permafrost: Siberië, Alaska en Noord-Canada, want daar lag de bodem permanent bevroren.",
                  "140px"),
                 ("open", "Waarom treffen de gevolgen van de opwarming vaak het hardst de landen die er "
                          "het minst toe hebben bijgedragen?",
                  "Arme landen liggen vaker in streken die gevoelig zijn voor droogte, overstroming of "
                          "orkanen, en ze hebben minder geld voor dijken, irrigatie of verzekeringen. De "
                          "uitstoot per inwoner ligt er tegelijk veel lager dan in de rijke landen.", 5),
             ]),
        dict(kop="Milderen of aanpassen?",
             opdracht="Zet achter elke maatregel M (de oorzaak aanpakken) of A (je aanpassen aan de "
                      "gevolgen).",
             oefeningen=[
                 ("rij", [("dijken verhogen", "A"),
                          ("windmolens in plaats van een steenkoolcentrale", "M"),
                          ("droogtebestendige gewassen kweken", "A"),
                          ("minder vlees eten", "M"),
                          ("in de stad bomen planten tegen de hitte", "A"),
                          ("een huis isoleren", "M")],
                  "M of A?", W),
                 ("open", "Waarom hebben we allebei nodig, milderen én aanpassen?",
                  "Milderen alleen komt te laat voor de opwarming die er al is en die nog doorwerkt, dus "
                          "we moeten ons aan die gevolgen aanpassen. Aanpassen alleen laat de uitstoot doorgaan, "
                          "zodat de gevolgen blijven groeien tot we ons niet meer kunnen aanpassen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-geografisch-onderzoek-voeren-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Een geografisch onderzoek voeren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen in de juiste orde",
             opdracht="Nummer de stappen van een geografisch onderzoek van 1 tot 5.",
             oefeningen=[
                 ("rij", [("de gegevens verwerken in een kaart, grafiek of tabel", "3"),
                          ("een onderzoeksvraag opstellen", "1"),
                          ("besluiten en het antwoord formuleren", "4"),
                          ("gegevens verzamelen uit bronnen of veldwerk", "2"),
                          ("je werkwijze kritisch bekijken", "5")],
                  "Welke stap?", W),
                 ("open", "Waarom is de laatste stap, je eigen werkwijze bekijken, geen overbodige "
                          "formaliteit?",
                  "Daar ontdek je of je besluit wel draagt: of je bronnen recent en betrouwbaar waren, of "
                          "je genoeg metingen had, en of er een andere verklaring mogelijk is. Zonder die stap "
                          "presenteer je een toevalstreffer als een vaststelling.", 5),
             ]),
        dict(kop="Een bruikbare onderzoeksvraag",
             opdracht="Zet achter elke vraag G (goed) of S (slecht), en verbeter de slechte.",
             oefeningen=[
                 ("tabel", ["vraag", "G of S", "verbetering"],
                  [["Is aardrijkskunde interessant?", None, None],
                   ["Hoe verschilt de bevolkingsdichtheid in Limburg tussen 2000 en 2020?", None, None],
                   ["Waarom is alles vroeger beter?", None, None],
                   ["Welk verband is er tussen verharding en wateroverlast in onze gemeente?", None, None]],
                  "1 S: een mening, niet te onderzoeken. Beter: hoeveel leerlingen van onze school kiezen "
                  "een richting met aardrijkskunde? 2 G: afgebakend in ruimte en tijd, met meetbare "
                  "gegevens. 3 S: te vaag en niet meetbaar. Beter: hoe is de open ruimte in onze gemeente "
                  "veranderd tussen 1990 en 2020? 4 G: twee meetbare zaken, één gebied.",
                  "130px"),
             ]),
        dict(kop="Welke bron gebruik je?",
             opdracht="",
             oefeningen=[
                 ("rij", [("de bevolkingsdichtheid per gemeente", "Statbel of een statistiekdatabank"),
                          ("hoe een terrein er vijftig jaar geleden uitzag", "een oude luchtfoto"),
                          ("de hoogte van een punt in Vlaanderen", "Geopunt"),
                          ("hoeveel auto's er per uur passeren", "eigen veldwerk, zelf tellen")],
                  "Welke bron?", WL),
                 ("open", "Je vindt online een kaart zonder jaartal en zonder bronvermelding. Noem twee "
                          "redenen om ze niet te gebruiken.",
                  "Zonder jaartal weet je niet of ze de toestand van vandaag toont, en zonder "
                          "bronvermelding kan je niet nagaan wie ze gemaakt heeft en of de gegevens kloppen. "
                          "Een besluit dat op zo'n kaart steunt, kan je niet verdedigen.", 5),
             ]),
        dict(kop="Wat mag je besluiten?",
             opdracht="",
             oefeningen=[
                 ("kies", "In een gemeente steeg het aantal inwoners én het aantal fietsdiefstallen. "
                          "Welk besluit mag je trekken?",
                  ["Dat de twee samen stijgen; of het een het ander veroorzaakt, weet je hiermee niet.",
                   "Dat meer inwoners meer fietsdiefstallen veroorzaken in die gemeente.",
                   "Dat de fietsdiefstallen mensen naar de gemeente lokken om er te komen wonen.",
                   "Dat er uit twee reeksen cijfers naast elkaar nooit iets te besluiten valt."], 0),
                 ("waar", "Als twee gegevens samen stijgen, is de ene altijd de oorzaak van de andere.",
                  False),
                 ("open", "Je meet de temperatuur op één plek in de stad en op één plek op het platteland, "
                          "op één namiddag. Je vindt een verschil van 3 °C. Waarom mag je daaruit nog niet "
                          "besluiten dat de stad een hitte-eiland is? Noem twee redenen, en zeg hoe je het "
                          "beter zou aanpakken.",
                  "Eén meting op één dag kan toeval zijn (bewolking, wind, schaduw), en twee plekken zijn "
                          "te weinig om de hele stad en het hele platteland voor te stellen. Beter: meet op "
                          "meer punten, op meerdere dagen en op vaste uren, en gebruik toestellen die op "
                          "dezelfde manier staan opgesteld.", 7),
             ]),
        dict(kop="Schaal en afstand",
             opdracht="Reken uit. Schrijf de bewerking op.",
             oefeningen=[
                 ("rij", [("schaal 1 : 25 000, op de kaart 8 cm — in het echt?", "2 km"),
                          ("schaal 1 : 50 000, op de kaart 3 cm — in het echt?", "1,5 km"),
                          ("schaal 1 : 10 000, in het echt 700 m — op de kaart?", "7 cm"),
                          ("schaal 1 : 200 000, op de kaart 4,5 cm — in het echt?", "9 km")],
                  "Antwoord met eenheid", WW),
                 ("open", "Welke schaal kies je om de spreiding van bedrijven in één gemeente te "
                          "onderzoeken: 1 : 10 000 of 1 : 500 000? Leg uit.",
                  "1 : 10 000. Dat is een grote schaal: je ziet een klein gebied met veel detail, en dat "
                          "heb je nodig om afzonderlijke bedrijven te kunnen aanduiden. Op 1 : 500 000 valt de "
                          "hele gemeente samen tot een stip.", 5),
             ]),
    ],
)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-waar-ligt-het-en-hoe-weet-je-dat-boost"] = dict(
    reeksen=[
        dict(aanpak="Onthoud de getallen, dan ken je de lijnen: 0° de evenaar, 23,5° de keerkringen, 66,5° "
                    "de poolcirkels, 90° de polen.",
             waarom=[
                 "Let op het verschil tussen een breedtecirkel (horizontaal, parallel aan de evenaar) en "
                 "een meridiaan (verticaal, van pool tot pool).",
                 "Noord of zuid staat er altijd bij: 23,5° N is de Kreeftskeerkring, 23,5° Z de "
                 "Steenbokskeerkring. Zonder die letter is het antwoord onvolledig.",
             ]),
        dict(aanpak="Absoluut situeren doe je met coördinaten, relatief met een verwijzing naar iets anders. "
                    "Staan er graden, dan is het absoluut.",
             waarom=[None, None, None, None]),
        dict(aanpak="Fysischgeografisch gaat over de natuurlijke aarde (water, reliëf, klimaat, "
                    "plantengroei), sociaaleconomisch over wat mensen doen en hebben.",
             waarom=[
                 "Taal en analfabetisme lijken ver van de economie te staan, maar het zijn kenmerken van "
                 "mensen en dus sociaaleconomisch.",
             ]),
        dict(aanpak="De werkelijke afstand is te meten, de ervaren afstand is hoe lang het voelt, de mentale "
                    "afstand is hoe ver je dénkt dat iets ligt.",
             waarom=[
                 "De derde is de lastigste: een mentale afstand zit in je hoofd, en ze is vaak scheef "
                 "doordat je een land beter kent dan een ander.",
                 None,
             ]),
        dict(aanpak="Elke wereldkaart is een keuze. Vraag je bij een kaart altijd af wat er vervormd is en "
                    "wat er in het midden staat.",
             waarom=[
                 None,
                 "Noem het verschil met een cijfer erbij: Afrika is ongeveer veertien keer zo groot als "
                 "Groenland. Zonder cijfer blijft het een gevoel.",
                 "Een bol plat maken kan niet zonder iets te verliezen. Elke projectie kiest wat ze "
                 "kloppend houdt, en vervormt de rest.",
                 None,
             ]),
        dict(aanpak="Begin bij de vraag en kies dan de bron. Een vraag over temperatuur en neerslag vraagt "
                    "een klimaatbron, een vraag over hoogte een reliëfbron.",
             waarom=[
                 "Een klimaatkaart geeft de zone, een klimatogram de twaalf maanden van één plaats. Welke "
                 "je neemt, hangt af van hoe fijn je het wil weten.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-waar-wonen-de-mensen-boost"] = dict(
    reeksen=[
        dict(aanpak="Bevolkingsdichtheid is inwoners gedeeld door oppervlakte. Schrijf de bewerking op en "
                    "zet de eenheid inw/km² erbij, anders is het antwoord onvolledig.",
             waarom=[
                 None,
                 "Dit paar is het hele punt van de reeks: land A heeft zeven keer zoveel inwoners en is "
                 "veertig keer dunner bevolkt. Veel inwoners is niet hetzelfde als dicht bevolkt.",
             ]),
        dict(aanpak="Vraag je bij elk gebied af wat er ontbreekt: water, warmte, vlakke grond of vruchtbare "
                    "bodem. Dat ontbrekende is je antwoord.",
             waarom=[
                 "Vaak spelen er twee factoren samen, zoals in de Ganges-delta: vruchtbaar slib én genoeg "
                 "regen. Noem ze dan allebei.",
             ]),
        dict(aanpak="Een dichtheid is een gemiddelde. Vraag je altijd af wat er binnen dat gemiddelde "
                    "verborgen zit.",
             waarom=[
                 "Dit verschil heet het spreidingspatroon: een compacte kern tegenover verspreide bewoning. "
                 "Dezelfde dichtheid, een ander landschap.",
                 "Rusland en Canada hebben veel inwoners en een hele lage dichtheid. Het is een breuk, niet "
                 "een som.",
                 "Bangladesh is dichtbevolkt en arm, Australië dunbevolkt en rijk. Dichtheid zegt niets "
                 "over welvaart.",
             ]),
        dict(aanpak="De HDI meet welvaart op drie manieren tegelijk. Onthoud die drie, dan kan je elke vraag "
                    "erover beantwoorden.",
             waarom=[
                 None,
                 "Dat de waarde tussen 0 en 1 ligt, maakt landen vergelijkbaar: het is geen bedrag maar een "
                 "verhouding.",
                 None,
                 "Dit is waarom de HDI bestaat: een land kan rijk zijn en toch slecht scoren op gezondheid "
                 "en onderwijs. Het inkomen alleen verbergt dat.",
             ]),
        dict(aanpak="Vraag bij elke kaart of tabel drie dingen: van wanneer, van wie, en hoe de klassen "
                    "gekozen zijn.",
             waarom=[
                 "De keuze van de klassen in de legende is het minst opvallende en het meest bepalende: "
                 "dezelfde cijfers kunnen er heel anders uitzien.",
                 "Dit heet het probleem van het schaalniveau: wat op landniveau klopt, kan voor een streek "
                 "helemaal niet gelden.",
                 "Ook in een land met een lage HDI is er een rijke groep. Een gemiddelde zegt niets over de "
                 "spreiding.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-hoe-een-bevolking-verandert-boost"] = dict(
    reeksen=[
        dict(aanpak="Natuurlijke aangroei is geboorte min sterfte. Migratiesaldo is immigratie min "
                    "emigratie. De totale groei is die twee samen.",
             waarom=[
                 "Een negatief resultaat is een geldig antwoord: bij 9 ‰ geboorte en 12 ‰ sterfte krimpt de "
                 "bevolking op eigen kracht.",
                 None,
                 "Deze combinatie komt in West-Europa echt voor: de bevolking groeit er enkel nog door "
                 "migratie.",
             ]),
        dict(aanpak="Lees een histogram van onder naar boven: de basis zijn de kinderen, de top de "
                    "ouderen. De vorm vertelt de geschiedenis van een land.",
             waarom=[
                 None,
                 "Een deuk in een histogram is altijd een gebeurtenis uit het verleden, en ze schuift elk "
                 "jaar een jaar hoger op. Reken dus terug naar het geboortejaar.",
                 None,
             ]),
        dict(aanpak="De vier fasen volgen altijd dezelfde orde: eerst daalt de sterfte, pas later de "
                    "geboorte. Tussen die twee zit de snelle groei.",
             waarom=[
                 "Fase 2 is de fase van de bevolkingsexplosie, en net daarom: de sterfte is al gedaald en "
                 "de geboorte nog niet.",
             ]),
        dict(aanpak="Push duwt weg van de eigen plaats, pull trekt naar de nieuwe. Vraag je af waar de "
                    "factor zich bevindt.",
             waarom=[
                 None,
                 "Dat de meesten in een buurland blijven, is een van de meest misbegrepen cijfers van dit "
                 "hoofdstuk. Een verre reis kost geld dat men net niet heeft.",
             ]),
        dict(aanpak="Braindrain en braingain zijn twee kanten van dezelfde verhuizing. Zeg bij een gevolg "
                    "altijd voor wie het een gevolg is.",
             waarom=[
                 None, None,
                 "Noem ook wat er mínder wordt: scholen komen leeg te staan. Vergrijzing verschuift de "
                 "vraag, ze vergroot ze niet alleen.",
                 "Het land van vertrek verliest juist de mensen in wie het het meest geïnvesteerd heeft. "
                 "Het voordeel ligt bij het land van aankomst.",
                 "Vergrijzen betekent dat het aandeel ouderen stijgt. Dat kan samen met een groeiende "
                 "bevolking, bijvoorbeeld door migratie.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-stad-en-platteland-boost"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elk kenmerk af waar het over gaat: geld (economisch), kennis en kunst "
                    "(cultureel), of macht en bestuur (politiek).",
             waarom=[
                 None,
                 "Hiërarchie gaat over belang en bereik, niet over inwonersaantal. Daarom staat Brussel "
                 "hoger dan veel grotere steden.",
             ]),
        dict(aanpak="Elk van de vijf begrippen beschrijft een beweging in de ruimte. Zoek wat er precies "
                    "verschuift: mensen, bebouwing of verkeer.",
             waarom=[
                 "Let op het verschil tussen inbreiding (binnen de stad opvullen) en verstedelijking van "
                 "het platteland (buiten de stad bijbouwen). De eerste spaart open ruimte, de tweede niet.",
             ]),
        dict(aanpak="Diversiteit en scheiding zijn twee verschillende vragen: wie woont er, en wonen ze "
                    "door elkaar.",
             waarom=[
                 None,
                 "Dit is de kern: segregatie ontstaat in West-Europa vooral langs de woningprijs, zonder "
                 "dat iemand ze oplegt. Daarom is ze zo moeilijk terug te draaien.",
             ]),
        dict(aanpak="Verharding werkt op twee manieren tegelijk: ze houdt de warmte vast en ze houdt het "
                    "water buiten de bodem. Noem bij elk gevolg hoe het werkt.",
             waarom=[
                 "Zeg bij elk probleem hoe de oplossing werkt, niet enkel dat het helpt. Schaduw en "
                 "verdamping koelen, insijpeling vult het grondwater aan.",
                 None, None,
                 "Verstedelijking is ook dat het stedelijke léven en het bouwpatroon zich verspreiden, ook "
                 "waar het aantal inwoners gelijk blijft.",
             ]),
        dict(aanpak="Twee beelden vergelijken kan alleen als ze vergelijkbaar zijn: let op schaal, seizoen "
                    "en hoek voor je besluiten trekt.",
             waarom=[
                 None,
                 "Een woondorp is het eindpunt van bijbouwen zonder voorzieningen: wonen hier, al de rest "
                 "elders, en dus meer autokilometers.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-grondstoffen-energie-en-industrie-boost"] = dict(
    reeksen=[
        dict(aanpak="Twee vragen apart: hoe diep ligt de laag (groeve of mijn), en met welke middelen wordt "
                    "er gewerkt (traditioneel of modern).",
             waarom=[
                 None,
                 "Noem ook het nadeel: bij dagbouw verdwijnt een hele laag grond. Een antwoord dat enkel de "
                 "voordelen geeft, is maar half af.",
             ]),
        dict(aanpak="Hernieuwbaar betekent dat de bron zich op menselijke tijdschaal aanvult. Het gaat over "
                    "de bron, niet over de uitstoot.",
             waarom=[
                 "Uranium hoort bij de niet-hernieuwbare bronnen, ook al stoot een kerncentrale weinig CO₂ "
                 "uit. Dat is de valkuil van deze rij.",
                 None,
             ]),
        dict(aanpak="Elke installatie volgt haar eigen bron: wind waar het waait, zon waar het schijnt, "
                    "water waar het valt, chemie waar het aankomt.",
             waarom=[
                 "Zeg bij elke plaats het wáárom erbij. De plaats zonder reden is op een examen geen "
                 "antwoord.",
             ]),
        dict(aanpak="Geopolitiek gaat over de staat en haar verhoudingen, fysisch over de natuur, "
                    "sociaaleconomisch over mensen, werk en markt.",
             waarom=[
                 "De HDI is een kenmerk van de bevolking, dus sociaaleconomisch, al klinkt het als een "
                 "politiek cijfer.",
             ]),
        dict(aanpak="De drie begrippen volgen elkaar op in tijd: industrialisatie, dan de-industrialisatie, "
                    "dan reconversie van wat achterbleef.",
             waarom=[
                 "Reconversie is een nieuwe bestemming voor een oude site. Het is geen nieuwe industrie "
                 "maar een nieuw gebruik.",
                 None,
                 "Noem ook het nadeel: werk dat de stad verlaat en open ruimte die versnippert. Dat is "
                 "precies wat het ruimtelijk beleid wil afremmen.",
                 "Dit heet de grondstoffenval: inkomsten uit één grondstof kunnen een land juist afhankelijk "
                 "en kwetsbaar maken. Noorwegen en Congo tonen de twee uitersten.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-landbouw-handel-en-toerisme-boost"] = dict(
    reeksen=[
        dict(aanpak="Elk gewas vraagt een bepaalde combinatie van warmte, water en bodem. Zet die "
                    "combinatie erbij, niet enkel de streek.",
             waarom=[
                 "Let op koffie: tropisch maar in de hooglanden, dus warm én koeler door de hoogte. De "
                 "hoogte is hier even belangrijk als de breedteligging.",
                 None,
             ]),
        dict(aanpak="Intensief betekent veel inzet per hectare (arbeid, mest, water, kapitaal). Extensief "
                    "betekent veel grond en weinig inzet per hectare.",
             waarom=[
                 "Rijstterrassen met de hand bewerkt zijn intensief, niet traditioneel-dus-extensief. De "
                 "inzet per hectare beslist, niet de techniek.",
                 "Dit is waarom twee landen elk kunnen zeggen dat hun landbouw de beste is: ze meten een "
                 "andere opbrengst.",
             ]),
        dict(aanpak="Duurzaam is wat de bodem, het water en de biodiversiteit intact laat voor volgend jaar. "
                    "Zet bij elk antwoord in één zin waarom.",
             waarom=[
                 "Let op het ploegen in de helling: hetzelfde werk dwars op de helling is wél duurzaam. De "
                 "richting beslist, niet de handeling.",
                 None, None,
             ]),
        dict(aanpak="De handelsketen loopt van producent over groothandel naar kleinhandel. De "
                    "dienstensector is alles wat geen goederen maakt.",
             waarom=[
                 None,
                 "Zeg erbij wat er verschuift: werk van de winkelstraat naar de rand van het land. Dat is "
                 "het ruimtelijke gevolg van online winkelen.",
             ]),
        dict(aanpak="Toerisme hangt af van drie soorten factoren tegelijk: natuur, veiligheid en welvaart. "
                    "Bij de gevolgen denk je aan ruimte, water en wonen.",
             waarom=[
                 None,
                 "Noem bij de gevolgen ook het wonen: woningen die voor de eigen bewoners onbetaalbaar "
                 "worden, is het gevolg dat het langst nawerkt.",
                 "Dit heet monocultuur in de economie: steunen op één sector maakt een streek kwetsbaar "
                 "voor één crisis.",
                 "Stadstoerisme bestaat juist om geschiedenis, musea, winkelen en gastronomie. Brugge heeft "
                 "geen strand.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-mondialisering-boost"] = dict(
    reeksen=[
        dict(aanpak="Volg een product van de grond tot de winkel. Elke stap gebeurt op een andere plaats, en "
                    "dat is net waar mondialisering over gaat.",
             waarom=[
                 None,
                 "Dit is de kern van het hoofdstuk: de winst en de last liggen op verschillende plaatsen. "
                 "Noem bij elk deel van de ketting waar het gebeurt.",
             ]),
        dict(aanpak="Er zijn vier stromen: goederen, kapitaal, mensen en informatie. Vraag je af wat er "
                    "precies beweegt.",
             waarom=[
                 "Geld dat migranten naar huis sturen, is een kapitaalstroom, ook al reizen er mensen. Kijk "
                 "naar wat er beweegt, niet naar wie het stuurt.",
                 "Voor sommige landen zijn remittances een grotere inkomstenbron dan de uitvoer of de "
                 "ontwikkelingshulp.",
             ]),
        dict(aanpak="Vraag bij elk gevolg altijd: voordeel of nadeel, en voor wie. Bijna niets is voor "
                    "iedereen hetzelfde.",
             waarom=[
                 "Een antwoord zonder voor wie is geen antwoord. Dezelfde lage prijs is winst voor de koper "
                 "en verlies voor de producent.",
             ]),
        dict(aanpak="Mondialisering gaat over verbindingen die mensen leggen. Natuurlijke gegevens zoals "
                    "reliëf en seizoenen staan erbuiten.",
             waarom=[
                 "Aardbeien in de winter zijn een gevolg van mondialisering, de seizoenen zelf niet. Dat is "
                 "het verschil tussen een natuurlijk gegeven en een menselijke verbinding.",
                 "De winst is heel ongelijk verdeeld; dat is de voornaamste kritiek op de mondialisering.",
                 "Mondialisering is niet van vandaag: de zijderoute en de scheepvaart van de 16de eeuw zijn "
                 "vroege vormen. Wat nieuw is, is het tempo en de omvang.",
             ]),
        dict(aanpak="Macht gaat hier over afhankelijkheid: wie beslist over het werk waar duizenden mensen "
                    "van leven, heeft invloed zonder verkozen te zijn.",
             waarom=[
                 "Een bedrijf mag nooit de wetten van een land aanpassen. De invloed loopt via de "
                 "afhankelijkheid van werk en investeringen, niet via de wet.",
                 "Noem ook wat een overheid wél in de hand heeft: regels, vergunningen en samenwerking met "
                 "andere landen. Anders lijkt het alsof ze niets kan.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-duurzaam-omgaan-met-de-ruimte-boost"] = dict(
    reeksen=[
        dict(aanpak="People gaat over mensen, planet over de natuur, profit over het geld op lange termijn. "
                    "Zoek bij elk kenmerk wie of wat het beschermt.",
             waarom=[
                 "Let op profit: het gaat om rendabel blijven op lange termijn, niet om zoveel mogelijk "
                 "winst nu. Dat verschil is wat het duurzaam maakt.",
                 "Het sleutelwoord is evenwicht. Een plan dat op één p uitblinkt en op de andere faalt, "
                 "komt vroeg of laat terug als probleem.",
             ]),
        dict(aanpak="Verharding heeft drie gevolgen tegelijk: wateroverlast verderop, een zakkend "
                    "grondwaterpeil, en meer hitte. Noem ze alle drie.",
             waarom=[
                 "De twee watergevolgen lijken tegengesteld (te veel water en te weinig water) maar hebben "
                 "dezelfde oorzaak: het water loopt weg in plaats van in te sijpelen.",
                 None, None,
             ]),
        dict(aanpak="Zet bij een ruimtelijk plan altijd elke partij apart, met wat ze wil en waarom. Pas "
                    "dan kan je een aanpassing voorstellen die werkt.",
             waarom=[
                 "Het gemeentebestuur staat verdeeld; dat is een geldig antwoord. Een partij die twee "
                 "belangen tegelijk heeft, hoeft niet voor één kant gekozen te worden.",
                 "Een goed voorstel maakt het voor twee partijen beter zonder het voor de derde onmogelijk "
                 "te maken. Dat is wat een compromis is.",
             ]),
        dict(aanpak="Vraag je bij elke maatregel af of het probleem opgelost wordt of enkel verhuist naar "
                    "een ander land of een andere plek.",
             waarom=[
                 "Verschuiven is de valkuil: afval verschepen en een fabriek verhuizen laten de totale "
                 "vervuiling gelijk, ze verplaatsen ze enkel uit het zicht.",
                 "Duurzaam betekent niet dat niets mag veranderen, maar dat de verandering de bodem, het "
                 "water en de biodiversiteit niet ondermijnt.",
                 "Ook een duurzame keuze heeft nadelen. Ze afwegen is iets anders dan ze ontkennen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-versterkte-broeikaseffect-boost"] = dict(
    reeksen=[
        dict(aanpak="Leg het broeikaseffect altijd in drie stappen uit: zonlicht in, warmtestraling terug, "
                    "een deel vastgehouden. Zonder die derde stap klopt de uitleg niet.",
             waarom=[
                 "De broeikasgassen houden de wármtestraling van de aarde tegen, niet het binnenkomende "
                 "zonlicht. Dat is de stap die het vaakst mis gaat.",
                 None,
                 "Zonder het natuurlijke broeikaseffect zou de aarde onbewoonbaar koud zijn. Het probleem "
                 "is de versterking ervan, niet het effect zelf.",
             ]),
        dict(aanpak="Zet bij elk gas zijn voornaamste bron. Zo zie je ook meteen waar een maatregel moet "
                    "aangrijpen.",
             waarom=[
                 "Methaan houdt veel meer warmte vast dan CO₂ maar blijft korter in de lucht. Daarom "
                 "levert minder methaan snel resultaat op.",
                 "Waterdamp is een versterkend gevolg, geen oorzaak die wij rechtstreeks aansturen: hoe "
                 "warmer de lucht, hoe meer damp ze vasthoudt.",
             ]),
        dict(aanpak="Een versterkende terugkoppeling maakt het effect groter, een dempende kleiner. Vraag "
                    "je af of het gevolg de oorzaak voedt.",
             waarom=[
                 "Drie van de vier versterken. Dat is precies waarom de opwarming moeilijk te stoppen is "
                 "zodra ze op gang is.",
                 "Albedo is het sleutelwoord: wit kaatst terug, donker neemt op. Daarom is smeltend ijs "
                 "zowel een gevolg als een oorzaak.",
             ]),
        dict(aanpak="Zet bij elk gevolg een concrete streek. Een gevolg zonder plaats blijft een algemene "
                    "zin en levert geen punten op.",
             waarom=[
                 "Zeg bij elke streek waarom juist daar: amper boven zeeniveau, ijs uit sneeuw, een "
                 "neerslagtekort dat al groot was, een bodem die permanent bevroren lag.",
                 "Dit heet klimaatrechtvaardigheid: de uitstoot per inwoner en de kwetsbaarheid liggen niet "
                 "in dezelfde landen.",
             ]),
        dict(aanpak="Milderen pakt de oorzaak aan (minder uitstoot), aanpassen de gevolgen (leven met de "
                    "opwarming). Vraag je af waar de maatregel aangrijpt.",
             waarom=[
                 "Bomen planten tegen de hitte is aanpassen, al is het groen. Een maatregel die de uitstoot "
                 "niet verlaagt, is geen milderen.",
                 "Dit is het antwoord dat een examen wil: milderen komt te laat voor wat er al is, "
                 "aanpassen laat de oorzaak doorgaan. Dus allebei.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-een-geografisch-onderzoek-voeren-boost"] = dict(
    reeksen=[
        dict(aanpak="De vijf stappen zijn: vraag, gegevens, verwerken, besluiten, en je werkwijze bekijken. "
                    "Die orde is vast.",
             waarom=[
                 None,
                 "De laatste stap is waar je ontdekt of je besluit wel draagt. Zonder die stap kan een "
                 "toevalstreffer als vaststelling de deur uit.",
             ]),
        dict(aanpak="Een goede onderzoeksvraag is afgebakend in tijd en ruimte en vraagt naar iets "
                    "meetbaars. Mist er één van die drie, dan is ze onbruikbaar.",
             waarom=[
                 "Verbeter een slechte vraag echt, met een jaartal en een gebied erbij. Enkel zeggen dat ze "
                 "te vaag is, is een half antwoord.",
             ]),
        dict(aanpak="Kies de bron bij de vraag: cijfers bij een databank, het verleden bij een oude foto, "
                    "hoogte bij een kaartportaal, en wat niemand telde bij eigen veldwerk.",
             waarom=[
                 "Soms is veldwerk de enige weg: verkeerscijfers voor jouw straat op jouw uur bestaan "
                 "nergens, dus die tel je zelf.",
                 None,
             ]),
        dict(aanpak="Samen stijgen is nog geen oorzaak. En één meting is geen vaststelling. Dit zijn de "
                    "twee fouten waar deze reeks op mikt.",
             waarom=[
                 "Dat twee reeksen samen bewegen heet een correlatie. Er kan een oorzaak achter zitten, "
                 "maar het cijfer alleen zegt dat niet.",
                 None,
                 "Zeg er altijd bij hoe je het beter zou aanpakken: meer punten, meer dagen, vaste uren, "
                 "gelijk opgestelde toestellen. Daar zitten de punten.",
             ]),
        dict(aanpak="Vermenigvuldig de kaartafstand met de noemer van de schaal, en reken daarna om naar "
                    "meter of kilometer. 100 000 cm is 1 km.",
             waarom=[
                 "Let op de derde: daar moet je het omgekeerde doen, van werkelijkheid naar kaart. Zet 700 m "
                 "eerst in centimeter.",
                 "Grote schaal betekent klein gebied met veel detail, kleine schaal een groot gebied met "
                 "weinig detail. Dat klinkt omgekeerd, en net daar gaat het mis.",
             ]),
    ],
)

# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis 🌍 Beyond dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere gevallen om in te delen, andere bronnen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een oordeel
verantwoorden, een verband in eigen woorden opschrijven). Wie hier iets
bijschrijft, legt het eerst naast `../../beyond-dubbele-finaliteit/geschiedenis.json`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond-dubbele-finaliteit". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen. Het achtervoegsel houdt ze uit elkaar van Beyond
doorstroom en van Boost, die thema's met bijna dezelfde titel hebben.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Geschiedenis"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Bij een bron: noteer eerst wie ze maakte en wanneer, en pas daarna wat je ervan vindt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-het-historisch-referentiekader-tijd-ruimte-en-domeinen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het historisch referentiekader: tijd, ruimte en domeinen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In welke periode?",
             opdracht="Schrijf bij elke gebeurtenis de naam van de periode waarin ze thuishoort.",
             oefeningen=[
                 ("rij", [("de val van het West-Romeinse Rijk", "het einde van de klassieke oudheid"),
                          ("de eerste boekdruk met losse letters in Europa", "de vroegmoderne tijd"),
                          ("de val van de Berlijnse Muur", "de hedendaagse tijd")], "Welke periode?", WL),
                 ("rij", [("de Franse Revolutie", "het einde van de moderne tijd"),
                          ("de bouw van de piramides van Gizeh", "het oude nabije oosten"),
                          ("de stichting van de steden in Vlaanderen", "de middeleeuwen")],
                  "Welke periode?", WL),
             ]),
        dict(kop="Tijd of ruimte?",
             opdracht="Noteer bij elk begrip of het een structuurbegrip van de tijd of van de ruimte is.",
             oefeningen=[
                 ("rij", [("gelijktijdigheid", "tijd"), ("urbaan", "ruimte"), ("evolutie", "tijd"),
                          ("continentaal", "ruimte"), ("generatie", "tijd"), ("lokaal", "ruimte")],
                  "Tijd of ruimte?", "92px"),
             ]),
        dict(kop="Welk domein?",
             opdracht="Vul de tabel aan met het domein waarin de gebeurtenis in de eerste plaats thuishoort: "
                      "politiek, economisch, sociaal of cultureel.",
             oefeningen=[
                 ("tabel", ["Gebeurtenis", "Domein"], [
                     ["De invoering van het algemeen enkelvoudig stemrecht voor mannen in 1919", None],
                     ["De oprichting van de eerste spoorlijn Brussel-Mechelen", None],
                     ["Het ontstaan van de vakbonden", None],
                     ["De bouw van een nieuw museum voor moderne kunst", None],
                 ], "stemrecht: politiek · spoorlijn: economisch · vakbonden: sociaal · museum: cultureel", WW),
             ]),
        dict(kop="Continuïteit of verandering?",
             opdracht="Kruis aan wat van toepassing is.",
             oefeningen=[
                 ("kies", "Tussen 1850 en 1910 verdubbelt de bevolking van de Belgische steden.",
                  ["continuïteit", "verandering"], 1),
                 ("kies", "Het Belgische koningshuis bestaat sinds 1831 zonder onderbreking.",
                  ["continuïteit", "verandering"], 0),
                 ("kies", "Na 1960 verdwijnt de Belgische kolonie Congo van de wereldkaart.",
                  ["continuïteit", "verandering"], 1),
                 ("kies", "Het Nederlands blijft in Vlaanderen eeuwenlang de taal van het dagelijks leven.",
                  ["continuïteit", "verandering"], 0),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een periodisering is een indeling die achteraf gemaakt wordt.", True),
                 ("waar", "Een scharnierpunt is de overgang tussen twee periodes.", True),
                 ("waar", "Onze zeven periodes gelden voor de hele wereld.", False),
                 ("waar", "Een symbolische jaartal staat voor een verandering die langer duurde dan één jaar.", True),
                 ("waar", "De vier domeinen staan los van elkaar en beïnvloeden elkaar niet.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom 1789 als scharnierpunt gekozen is, en waarom dat een keuze is "
                          "en geen vaststelling.",
                  "In 1789 begint de Franse Revolutie, die het ancien régime politiek en sociaal omverwerpt. "
                  "Het is een keuze omdat de veranderingen al eerder begonnen en nog lang doorliepen: "
                  "iemand heeft achteraf beslist dat dit jaar het meest in het oog springt.", 4),
                 ("open", "Een gebeurtenis speelt in meerdere domeinen tegelijk. Geef een voorbeeld en "
                          "benoem minstens twee domeinen.",
                  "De industriële revolutie bijvoorbeeld: economisch door de fabrieken en de machines, "
                  "sociaal door het ontstaan van een arbeidersklasse, en ook politiek door de wetten die "
                  "er later kwamen. Een goede analyse benoemt de domeinen apart en legt hun verband.", 4),
                 ("open", "Waarom werkt een historicus met schaalniveaus (lokaal, regionaal, mondiaal)?",
                  "Omdat hetzelfde verhaal op elk niveau anders klinkt. Een staking in één mijn is lokaal, "
                  "de sociale strijd is nationaal, en de industrialisering is mondiaal. Wie maar één niveau "
                  "bekijkt, mist de verbanden.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kenmerken-van-samenlevingen-vergelijken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kenmerken van samenlevingen vergelijken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk kenmerk?",
             opdracht="Noteer bij elke uitspraak welk kenmerk van een samenleving ze beschrijft: "
                      "bestuur, economie, sociale verhoudingen of cultuur.",
             oefeningen=[
                 ("rij", [("drie standen met elk hun eigen rechten", "sociale verhoudingen"),
                          ("het grootste deel van de bevolking werkt op het land", "economie"),
                          ("de koning regeert zonder parlement", "bestuur")], "Welk kenmerk?", WL),
                 ("rij", [("de kerk bepaalt wat men mag denken en leren", "cultuur"),
                          ("de fabriek vervangt de werkplaats aan huis", "economie"),
                          ("burgers kiezen hun vertegenwoordigers", "bestuur")], "Welk kenmerk?", WL),
             ]),
        dict(kop="Ancien régime of negentiende eeuw?",
             opdracht="Kruis aan in welke samenleving het kenmerk thuishoort.",
             oefeningen=[
                 ("kies", "De adel betaalt geen belasting en heeft eigen rechtbanken.",
                  ["ancien régime", "negentiende eeuw"], 0),
                 ("kies", "Je plaats in de maatschappij hangt vooral af van je bezit.",
                  ["ancien régime", "negentiende eeuw"], 1),
                 ("kies", "De koning dankt zijn macht volgens de leer aan God.",
                  ["ancien régime", "negentiende eeuw"], 0),
                 ("kies", "Een grondwet legt de rechten van de burgers vast.",
                  ["ancien régime", "negentiende eeuw"], 1),
             ]),
        dict(kop="Vergelijken op papier",
             opdracht="Vul de tabel aan met korte omschrijvingen.",
             oefeningen=[
                 ("tabel", ["Kenmerk", "Ancien régime", "Na 1830 in België"], [
                     ["Wie bestuurt?", None, None],
                     ["Hoe krijg je je plaats?", None, None],
                     ["Wie mag stemmen?", None, None],
                 ], "Wie bestuurt: de vorst met absolute macht / een koning met een grondwet en een "
                    "parlement. Hoe krijg je je plaats: door geboorte in een stand / vooral door bezit en "
                    "opleiding. Wie mag stemmen: niemand kiest de vorst / de mannen die genoeg belasting "
                    "betalen, het cijnskiesrecht.", "155px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Twee samenlevingen vergelijken betekent zoeken naar overeenkomsten én verschillen.", True),
                 ("waar", "Een samenleving vergelijken kan enkel met een samenleving uit dezelfde tijd.", False),
                 ("waar", "Wie vergelijkt, moet eerst afspreken op welke kenmerken hij vergelijkt.", True),
                 ("waar", "Een vergelijking levert altijd een winnaar op.", False),
                 ("waar", "Een kenmerk kan in de ene samenleving ontbreken en in de andere centraal staan.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat een standenmaatschappij onderscheidt van een klassenmaatschappij.",
                  "In een standenmaatschappij hangt je plaats af van je geboorte, en elke stand heeft eigen "
                  "rechten en plichten die in de wet staan. In een klassenmaatschappij zijn alle burgers "
                  "voor de wet gelijk, maar bepaalt je bezit en je inkomen in de praktijk je positie. "
                  "Opklimmen is moeilijk, maar niet onmogelijk.", 5),
                 ("open", "Je wil de Belgische samenleving van 1850 vergelijken met die van vandaag. "
                          "Noem drie kenmerken waarop je vergelijkt en zeg waarom je die kiest.",
                  "Bijvoorbeeld het bestuur (wie mag stemmen), de economie (waar werken de mensen) en de "
                  "sociale verhoudingen (welke zekerheid is er bij ziekte of ouderdom). Die kenmerken "
                  "kiezen we omdat ze op beide momenten bestaan en omdat ze het dagelijks leven van gewone "
                  "mensen raken, zodat de vergelijking iets betekent.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-restauratie-en-revolutie-het-congres-van-wenen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Restauratie en revolutie: het Congres van Wenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de oude vorsten en grenzen herstellen na Napoleon", "restauratie"),
                          ("de macht zo verdelen dat geen land de baas is", "machtsevenwicht"),
                          ("vorsten die samen optreden tegen revoluties", "de Heilige Alliantie")],
                  "Welk begrip?", WL),
                 ("rij", [("het recht van een vorst dat van vader op zoon gaat", "legitimiteit"),
                          ("een bestuur waarin de vorst alle macht heeft", "absolutisme"),
                          ("de periode van Napoleons terugkeer in 1815", "de Honderd Dagen")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Wie zat er in Wenen?",
             opdracht="Noteer bij elke naam het land dat hij vertegenwoordigde.",
             oefeningen=[
                 ("rij", [("Metternich", "Oostenrijk"), ("Talleyrand", "Frankrijk"),
                          ("Castlereagh", "Groot-Brittannië")], "Welk land?", WW),
             ]),
        dict(kop="Beslissing of gevolg?",
             opdracht="Kruis aan of het een beslissing van het congres is of een gevolg ervan.",
             oefeningen=[
                 ("kies", "De Noordelijke en Zuidelijke Nederlanden worden één koninkrijk.",
                  ["beslissing", "gevolg"], 0),
                 ("kies", "In de Zuidelijke Nederlanden groeit ontevredenheid over Willem I.",
                  ["beslissing", "gevolg"], 1),
                 ("kies", "Pruisen krijgt gebied in het Rijnland.", ["beslissing", "gevolg"], 0),
                 ("kies", "Liberalen en nationalisten gaan in het geheim verder werken.",
                  ["beslissing", "gevolg"], 1),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het Congres van Wenen vergaderde in 1814 en 1815.", True),
                 ("waar", "De bevolking van de gebieden werd gevraagd wat ze wou.", False),
                 ("waar", "Frankrijk mocht als verslagen land meebeslissen aan de tafel.", True),
                 ("waar", "De restauratie kon de ideeën van de Franse Revolutie ongedaan maken.", False),
                 ("waar", "Het machtsevenwicht hield een grote Europese oorlog bijna honderd jaar tegen.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de restauratie op lange termijn mislukte.",
                  "De vorsten konden de grenzen en de tronen herstellen, maar niet de ideeën. Liberalisme "
                  "en nationalisme leefden bij de burgerij en bij de intellectuelen verder, en kwamen in "
                  "1830 en 1848 in golven van revoluties naar boven.", 4),
                 ("open", "Waarom lieten de grote mogendheden Frankrijk aan de onderhandelingstafel toe?",
                  "Omdat een vernederd Frankrijk een bron van nieuwe onrust zou zijn. Een Frankrijk dat "
                  "meebesliste, had belang bij het nieuwe evenwicht. Talleyrand kon daardoor ook de "
                  "tegenstellingen tussen de overwinnaars uitspelen.", 4),
                 ("open", "De Nederlanden werden samengevoegd als bufferstaat. Leg uit tegen wie, en "
                          "waarom dat botste met de werkelijkheid in het zuiden.",
                  "Als buffer tegen Frankrijk. Het botste omdat noord en zuid verschilden in taal, in "
                  "godsdienst en in economie, en omdat Willem I bestuurde zonder rekening te houden met "
                  "de katholieke en de liberale kritiek in het zuiden.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-liberalisme-en-nationalisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Liberalisme en nationalisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Liberaal of nationalistisch?",
             opdracht="Kruis aan welke ideologie uit de eis spreekt.",
             oefeningen=[
                 ("kies", "Een grondwet moet de macht van de koning beperken.",
                  ["liberalisme", "nationalisme"], 0),
                 ("kies", "Alle Duitstalige staten horen één rijk te vormen.",
                  ["liberalisme", "nationalisme"], 1),
                 ("kies", "De overheid moet zich niet met de economie bemoeien.",
                  ["liberalisme", "nationalisme"], 0),
                 ("kies", "Een volk met één taal en één geschiedenis heeft recht op een eigen staat.",
                  ["liberalisme", "nationalisme"], 1),
                 ("kies", "De drukpers moet vrij zijn.", ["liberalisme", "nationalisme"], 0),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("stemrecht enkel voor wie genoeg belasting betaalt", "cijnskiesrecht"),
                          ("wetgevende, uitvoerende en rechterlijke macht gescheiden", "de machtenscheiding"),
                          ("een vorst die gebonden is aan een grondwet", "een constitutionele monarchie")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Welke revolutiegolf?",
             opdracht="Noteer het jaar van de golf waarin de gebeurtenis thuishoort: 1830 of 1848.",
             oefeningen=[
                 ("rij", [("de Belgische opstand tegen Willem I", "1830"),
                          ("het Duitse parlement in Frankfurt", "1848"),
                          ("de val van koning Louis-Philippe in Frankrijk", "1848")], "Welk jaar?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het liberalisme van de negentiende eeuw wou stemrecht voor iedereen.", False),
                 ("waar", "Nationalisme kan een bestaand rijk doen uiteenvallen én staten doen samensmelten.", True),
                 ("waar", "De Italiaanse eenmaking kwam tot stand in de tweede helft van de negentiende eeuw.", True),
                 ("waar", "Liberalisme en nationalisme sloten elkaar in de negentiende eeuw altijd uit.", False),
                 ("waar", "Het nationalisme werd later ook gebruikt om andere volken te overheersen.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het liberalisme vooral een ideologie van de burgerij was.",
                  "De burgerij had bezit en opleiding, maar geen politieke macht: die lag bij de adel en de "
                  "vorst. Vrijheid van ondernemen, een grondwet en een parlement gaven haar precies wat ze "
                  "nodig had. Het cijnskiesrecht hield de arbeiders tegelijk buiten.", 5),
                 ("open", "Leg met een voorbeeld uit hoe nationalisme twee tegengestelde gevolgen kan hebben.",
                  "In Italië en Duitsland bracht het losse staten samen in één nieuwe staat. In het "
                  "Oostenrijkse en het Ottomaanse Rijk deed het die rijken juist uiteenvallen, omdat elk "
                  "volk zijn eigen staat opeiste.", 5),
                 ("open", "Waarom mislukten de revoluties van 1848 bijna overal, en wat bleef er toch van over?",
                  "De revolutionairen waren verdeeld: liberale burgers wilden een grondwet, arbeiders wilden "
                  "brood en werk, nationalisten wilden grenzen. De legers van de vorsten herstelden de orde. "
                  "Toch bleven de eisen leven, en veel staten voerden later alsnog grondwetten en "
                  "parlementen in.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-ontstaan-van-belgie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het ontstaan van België",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Grieven tegen Willem I",
             opdracht="Noteer bij elke klacht wie ze in de eerste plaats maakte: de katholieken, de "
                      "liberalen, of allebei.",
             oefeningen=[
                 ("rij", [("de koning benoemt de bisschoppen niet naar onze zin", "de katholieken"),
                          ("de koning bestuurt zonder het parlement te raadplegen", "de liberalen"),
                          ("het Nederlands wordt als enige bestuurstaal opgelegd", "allebei")],
                  "Wie klaagt?", WL),
                 ("rij", [("het onderwijs moet in handen van de kerk blijven", "de katholieken"),
                          ("de drukpers moet vrij zijn", "de liberalen"),
                          ("het zuiden is ondervertegenwoordigd in het bestuur", "allebei")],
                  "Wie klaagt?", WL),
             ]),
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer de gebeurtenissen van 1 tot 5, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Gebeurtenis"], [
                     [None, "het Nationaal Congres komt samen"],
                     [None, "de opvoering van De Stomme van Portici in Brussel"],
                     [None, "Leopold van Saksen-Coburg legt de eed af"],
                     [None, "de Septemberdagen in het Warandepark"],
                     [None, "de Tiendaagse Veldtocht"],
                 ], "1 = De Stomme van Portici (augustus 1830) · 2 = de Septemberdagen · 3 = het Nationaal "
                    "Congres · 4 = de eedaflegging van Leopold I (21 juli 1831) · 5 = de Tiendaagse "
                    "Veldtocht (augustus 1831)", "56px"),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de samenwerking van katholieken en liberalen tegen de koning", "het unionisme"),
                          ("de vergadering die de grondwet schreef", "het Nationaal Congres"),
                          ("de belofte dat België zich niet in oorlogen mengt", "de neutraliteit")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De Belgische grondwet van 1831 gold in haar tijd als een van de meest liberale van Europa.", True),
                 ("waar", "In 1831 mocht elke meerderjarige man stemmen.", False),
                 ("waar", "De grote mogendheden aanvaardden de Belgische onafhankelijkheid op de Conferentie van Londen.", True),
                 ("waar", "Nederland erkende België onmiddellijk in 1830.", False),
                 ("waar", "Het Frans werd de taal van het bestuur, het leger en de rechtbank.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de grote mogendheden België niet lieten verdwijnen, en welke "
                          "voorwaarde zij er aan verbonden.",
                  "Een onafhankelijk België paste in het machtsevenwicht van Wenen: het hield Frankrijk weg "
                  "van de Noordzeekust zonder dat één mogendheid het gebied kreeg. De voorwaarde was de "
                  "neutraliteit, gewaarborgd door de mogendheden zelf.", 5),
                 ("open", "Leg uit waarom het unionisme na enkele jaren uiteenviel.",
                  "Katholieken en liberalen waren verenigd door wat ze niet wilden, namelijk het bestuur van "
                  "Willem I. Zodra dat weg was, kwamen hun eigen tegenstellingen boven, vooral over het "
                  "onderwijs. Zo ontstonden de eerste politieke partijen.", 5),
                 ("open", "Waarom was de keuze voor het Frans als bestuurstaal een beslissing met gevolgen "
                          "voor meer dan een eeuw?",
                  "De meerderheid van de bevolking sprak Nederlands, maar wie vooruit wou in het bestuur, "
                  "het leger of de rechtbank had Frans nodig. Dat maakte van taal een sociale grens, en het "
                  "werd de voedingsbodem van de Vlaamse beweging en later van de taalwetten.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-eerste-en-de-tweede-industriele-revolutie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De eerste en de tweede industriële revolutie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eerste of tweede?",
             opdracht="Kruis aan bij welke industriële revolutie het hoort.",
             oefeningen=[
                 ("kies", "de stoommachine en de steenkool", ["eerste", "tweede"], 0),
                 ("kies", "elektriciteit en aardolie", ["eerste", "tweede"], 1),
                 ("kies", "de mechanische weefmachine in de textiel", ["eerste", "tweede"], 0),
                 ("kies", "de lopende band en de massaproductie", ["eerste", "tweede"], 1),
                 ("kies", "de chemische en de auto-industrie", ["eerste", "tweede"], 1),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("werken in je eigen huis voor een opdrachtgever", "huisnijverheid"),
                          ("de trek van het platteland naar de stad", "urbanisatie"),
                          ("geld dat in een onderneming gestoken wordt", "kapitaal")], "Welk begrip?", WL),
                 ("rij", [("één onderneming beheerst een hele markt", "een monopolie"),
                          ("het werk opsplitsen in kleine, herhaalde taken", "arbeidsverdeling"),
                          ("een bedrijf met aandelen in handen van vele eigenaars", "een naamloze vennootschap")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Vul de tabel aan",
             opdracht="Schrijf per domein kort op wat er veranderde.",
             oefeningen=[
                 ("tabel", ["Domein", "Wat verandert er?"], [
                     ["Economisch", None],
                     ["Sociaal", None],
                     ["Ruimtelijk", None],
                 ], "Economisch: van landbouw en huisnijverheid naar fabrieken, machines en massaproductie. "
                    "Sociaal: er ontstaan een industriële burgerij en een arbeidersklasse, met lange dagen "
                    "en kinderarbeid. Ruimtelijk: de bevolking trekt naar de steden en naar de "
                    "mijnstreken, de steden groeien snel en ongepland.", "300px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "België was na Groot-Brittannië een van de eerste geïndustrialiseerde landen op het vasteland.", True),
                 ("waar", "De industrialisering begon in Vlaanderen en kwam pas later naar Wallonië.", False),
                 ("waar", "De spoorweg maakte het vervoer van steenkool en grondstoffen veel goedkoper.", True),
                 ("waar", "De eerste industriële revolutie verliep in alle landen van Europa gelijktijdig.", False),
                 ("waar", "De uitvinding van het Bessemerprocedé maakte staal veel goedkoper.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de industrialisering in Groot-Brittannië het eerst begon.",
                  "Er was steenkool en ijzer in de buurt van elkaar, er was kapitaal uit de handel en de "
                  "koloniën, er was een grote markt en een bevolking die naar de steden kon trekken, en er "
                  "waren vervoerswegen over zee en over kanalen.", 5),
                 ("open", "Waarom noemt men het ontstaan van de fabriek een breuk in het dagelijks leven?",
                  "In de huisnijverheid bepaalde je zelf je ritme en werkte je bij je gezin. In de fabriek "
                  "bepaalt de machine en de klok het ritme, werk je op een vaste plaats onder toezicht, en "
                  "wordt je werk opgesplitst in kleine herhaalde taken.", 5),
                 ("open", "De tweede industriële revolutie wordt soms de revolutie van het laboratorium "
                          "genoemd. Leg uit waarom.",
                  "De eerste golf kwam vooral van praktische uitvinders en handige werktuigkundigen. De "
                  "tweede steunde op wetenschappelijk onderzoek: chemie, elektriciteit en materiaalkunde. "
                  "Grote ondernemingen richtten eigen onderzoekslabo's op.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ongelijkheden-klassenmaatschappij-en-sociale-strijd-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Ongelijkheden: klassenmaatschappij en sociale strijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de ellendige toestand waarin de arbeiders leefden", "het sociale vraagstuk"),
                          ("het werk neerleggen om eisen af te dwingen", "een staking"),
                          ("een vereniging van arbeiders die samen opkomen", "een vakbond")],
                  "Welk begrip?", WL),
                 ("rij", [("een onderzoek naar de levensomstandigheden van arbeiders", "een enquête"),
                          ("een kas waaruit je geld krijgt bij ziekte", "een mutualiteit"),
                          ("winkels waar leden samen goedkoper kopen", "een cooperatie")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Welke klasse?",
             opdracht="Noteer bij elke omschrijving de klasse: de industriële burgerij, de middenklasse "
                      "of de arbeidersklasse.",
             oefeningen=[
                 ("rij", [("bezit een fabriek en leeft van winst", "de industriële burgerij"),
                          ("werkt twaalf uur per dag voor een dagloon", "de arbeidersklasse"),
                          ("onderwijzer, bediende of winkelier", "de middenklasse")], "Welke klasse?", WL),
             ]),
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer de Belgische sociale maatregelen van 1 tot 4, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Maatregel"], [
                     [None, "algemeen enkelvoudig stemrecht voor mannen"],
                     [None, "het verbod op kinderarbeid onder twaalf jaar"],
                     [None, "de achturendag"],
                     [None, "de eerste arbeidersenquête na de onlusten van 1886"],
                 ], "1 = de arbeidersenquête (1886) · 2 = het verbod op kinderarbeid onder twaalf jaar "
                    "(1889) · 3 = het algemeen enkelvoudig stemrecht voor mannen (1919) · 4 = de "
                    "achturendag (1921)", "56px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In een klassenmaatschappij zijn alle burgers voor de wet gelijk.", True),
                 ("waar", "De eerste sociale wetten kwamen er pas na jaren van strijd en onrust.", True),
                 ("waar", "Kinderarbeid was in de negentiende eeuw van het begin af verboden.", False),
                 ("waar", "De onlusten van 1886 in Wallonië zetten het sociale vraagstuk op de politieke agenda.", True),
                 ("waar", "Stakingen waren in België altijd toegelaten.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het algemeen stemrecht een sleutel was voor de arbeiders.",
                  "Met het cijnskiesrecht konden alleen de rijken verkiezen, dus kwamen hun belangen in het "
                  "parlement terecht. Pas met stemrecht kon de arbeidersbeweging vertegenwoordigers sturen "
                  "en wetten laten maken over lonen, arbeidsduur en pensioen.", 5),
                 ("open", "Naast stakingen bouwden arbeiders ook eigen verenigingen. Noem er twee en zeg "
                          "waarvoor ze dienden.",
                  "Mutualiteiten of ziekenkassen, waaruit je een vergoeding kreeg bij ziekte of ongeval, en "
                  "cooperaties, waar leden samen goedkoper konden kopen en de winst terugvloeide. Later "
                  "kwamen daar ook scholingsinitiatieven en volkshuizen bij.", 5),
                 ("open", "Een fabrikant zei in 1870 dat hoge lonen de arbeider lui maken. Hoe lees je zo "
                          "een uitspraak als historicus?",
                  "Als een standpunt met een belang erachter, niet als een vaststelling. De fabrikant "
                  "verdedigt zijn loonkost. De uitspraak is wel een goede bron voor de manier waarop de "
                  "industriële burgerij over arbeiders dacht.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-marxisme-sociaaldemocratie-christendemocratie-en-migratie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Marxisme, sociaaldemocratie, christendemocratie en migratie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stroming?",
             opdracht="Noteer bij elke uitspraak de stroming: marxisme, sociaaldemocratie of christendemocratie.",
             oefeningen=[
                 ("rij", [("de geschiedenis is een strijd tussen klassen", "marxisme"),
                          ("hervormingen afdwingen via het parlement", "sociaaldemocratie"),
                          ("werkgevers en werknemers moeten samen overleggen", "christendemocratie")],
                  "Welke stroming?", WL),
                 ("rij", [("de arbeiders moeten de productiemiddelen overnemen", "marxisme"),
                          ("een rechtvaardig loon is een plicht van de werkgever", "christendemocratie"),
                          ("de revolutie is niet nodig, de democratie volstaat", "sociaaldemocratie")],
                  "Welke stroming?", WL),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de meerwaarde die de eigenaar uit het werk haalt", "uitbuiting"),
                          ("de pauselijke brief van 1891 over de arbeiders", "Rerum Novarum"),
                          ("mensen die hun land verlaten om elders te werken", "arbeidsmigranten")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Migratie naar België",
             opdracht="Noteer bij elke periode waar de arbeidsmigranten in de eerste plaats vandaan kwamen.",
             oefeningen=[
                 ("rij", [("kort na 1945, voor de steenkoolmijnen", "Italië"),
                          ("vanaf de jaren zestig, na nieuwe akkoorden", "Marokko en Turkije"),
                          ("in de negentiende eeuw, naar de Waalse industrie", "Vlaanderen")],
                  "Van waar?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Marx schreef samen met Engels het Communistisch Manifest.", True),
                 ("waar", "De christendemocratie wou de klassenstrijd en de revolutie.", False),
                 ("waar", "De sociaaldemocratie koos voor hervormingen binnen de democratie.", True),
                 ("waar", "Arbeidsmigratie naar België begon pas na 1945.", False),
                 ("waar", "Na de mijnramp van Marcinelle in 1956 veranderde de migratie naar België.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de drie stromingen alle drie een antwoord op dezelfde vraag waren.",
                  "Ze reageerden alle drie op de ellende die de industrialisering meebracht: het sociale "
                  "vraagstuk. Ze verschilden niet in de vaststelling, maar in de oplossing: revolutie, "
                  "hervorming via de democratie, of overleg vanuit een christelijke plicht.", 5),
                 ("open", "België sloot na 1945 akkoorden om mijnwerkers te laten komen. Leg uit waarom, "
                          "en wat dat betekende voor de mensen die kwamen.",
                  "De steenkoolproductie moest omhoog voor de heropbouw, en er waren te weinig Belgen die "
                  "nog in de mijn wilden werken. Wie kwam, kreeg zwaar en gevaarlijk werk, woonde vaak in "
                  "barakken bij de mijn, en bleef uiteindelijk met zijn gezin in België.", 6),
                 ("open", "Waarom is 'de gastarbeider' een woord dat de werkelijkheid slecht beschrijft?",
                  "Het woord gaat ervan uit dat iemand tijdelijk komt en weer vertrekt. In de praktijk "
                  "bleven de meeste mensen, haalden hun gezin over en bouwden hier hun leven op. Het woord "
                  "zegt dus vooral iets over wat men toen verwachtte.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-modern-imperialisme-en-de-wedloop-om-afrika-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Modern imperialisme en de wedloop om Afrika",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk motief?",
             opdracht="Noteer bij elk argument van toen het motief: economisch, politiek of ideologisch.",
             oefeningen=[
                 ("rij", [("wij hebben grondstoffen en nieuwe markten nodig", "economisch"),
                          ("een grote mogendheid moet koloniën hebben", "politiek"),
                          ("wij brengen beschaving en het ware geloof", "ideologisch")], "Welk motief?", WL),
                 ("rij", [("onze schepen hebben kolenstations langs de route nodig", "politiek"),
                          ("ons kapitaal brengt in de kolonie meer op", "economisch"),
                          ("de wetenschap bewijst dat ons volk hoger staat", "ideologisch")],
                  "Welk motief?", WL),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("gebied dat volledig door een ander land bestuurd wordt", "een kolonie"),
                          ("een eigen vorst die onder toezicht van een mogendheid blijft", "een protectoraat"),
                          ("de conferentie van 1884 en 1885 over Afrika", "de Conferentie van Berlijn")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Op de Conferentie van Berlijn zat geen enkele Afrikaanse vertegenwoordiger aan tafel.", True),
                 ("waar", "Rond 1914 was bijna heel Afrika in Europese handen.", True),
                 ("waar", "Ethiopië werd net als de andere gebieden gekoloniseerd.", False),
                 ("waar", "De rechte grenzen op de kaart van Afrika volgen de grenzen van de volkeren.", False),
                 ("waar", "Het modern imperialisme werd mogelijk door nieuwe techniek, zoals de stoomboot, "
                          "de telegraaf en geneesmiddelen tegen malaria.", True),
             ]),
        dict(kop="Bron beoordelen",
             opdracht="Lees de bron en antwoord kort.",
             oefeningen=[
                 ("open", "Een Europese krant van 1885 schrijft: 'Wij brengen de donkere gebieden licht en "
                          "orde.' Wat zegt die zin over de schrijver, en wat zegt ze niet?",
                  "Ze zegt dat de schrijver de kolonisatie als een beschavingsopdracht zag, en dat hij de "
                  "Afrikaanse samenlevingen als achterlijk beschouwde. Over het leven in die gebieden zelf "
                  "zegt ze niets betrouwbaars: het is een rechtvaardiging, geen vaststelling.", 5),
                 ("open", "Leg uit wat de uitdrukking 'de beschavingsmissie' verbergt.",
                  "Ze stelt de kolonisatie voor als een gunst aan de bevolking, terwijl de drijfveren vooral "
                  "economisch en politiek waren. Ze verbergt ook het geweld, de dwangarbeid en het verlies "
                  "van eigen bestuur.", 5),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de grenzen die in Berlijn op de kaart getrokken werden vandaag "
                          "nog gevolgen hebben.",
                  "Ze werden getekend zonder de volkeren te bekijken: één volk kwam in twee staten terecht, "
                  "en volkeren die niets met elkaar hadden in één staat. Na de onafhankelijkheid bleven die "
                  "grenzen bestaan, met conflicten en moeizame staatsvorming tot gevolg.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-congo-van-congo-vrijstaat-tot-belgisch-congo-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Congo: van Congo-Vrijstaat tot Belgisch Congo",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vrijstaat of kolonie?",
             opdracht="Kruis aan of het hoort bij de Congo-Vrijstaat (1885-1908) of bij Belgisch Congo "
                      "(1908-1960).",
             oefeningen=[
                 ("kies", "Het gebied is persoonlijk bezit van Leopold II.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 0),
                 ("kies", "Het gebied wordt bestuurd door de Belgische staat.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 1),
                 ("kies", "Rubber wordt met dwang en zware straffen geoogst.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 0),
                 ("kies", "De koloniale drie-eenheid van staat, kerk en bedrijven bestuurt het dagelijks leven.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 1),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("het leger van de Vrijstaat", "de Force Publique"),
                          ("de samenwerking van staat, kerk en grote bedrijven", "de koloniale drie-eenheid"),
                          ("bestuur via de bestaande plaatselijke hoofden", "indirect bestuur")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Leopold II heeft Congo nooit zelf bezocht.", True),
                 ("waar", "De internationale verontwaardiging over het geweld droeg bij tot de overname door België in 1908.", True),
                 ("waar", "In Belgisch Congo bestond er hoger onderwijs voor Congolezen van het begin af.", False),
                 ("waar", "Koper uit Katanga en later uranium waren belangrijk voor de Belgische economie.", True),
                 ("waar", "Congolezen konden onder Belgisch bestuur stemmen voor het Belgische parlement.", False),
             ]),
        dict(kop="Bron beoordelen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Een Belgisch schoolboek van 1950 toont Congo als een land dat België 'tot "
                          "ontwikkeling brengt'. Wat analyseer je, en wat besluit je?",
                  "Je analyseert de beeldvorming: de kolonisatie wordt voorgesteld als een weldaad, de "
                  "Congolezen als mensen zonder eigen geschiedenis. Je besluit dat het boek vooral een bron "
                  "is over wat men in België in 1950 aan kinderen leerde, niet over het leven in Congo.", 6),
                 ("open", "Waarom zijn verslagen van missionarissen en van reizigers belangrijke bronnen "
                          "over de Vrijstaat, en waarom lees je ze toch kritisch?",
                  "Belangrijk omdat zij ter plaatse waren en soms de enigen die het geweld opschreven. "
                  "Kritisch omdat zij elk hun eigen belang en hun eigen blik hadden: een missionaris wou "
                  "bekeren, een reiziger wou publiceren.", 6),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het koloniale onderwijsbeleid na 1960 een probleem werd.",
                  "Er was veel lager onderwijs, maar bijna geen hoger onderwijs voor Congolezen. Bij de "
                  "onafhankelijkheid waren er daardoor nauwelijks Congolese artsen, ingenieurs of hoge "
                  "ambtenaren, en moest een nieuwe staat bestuurd worden zonder opgeleide bestuurders.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-eerste-wereldoorlog-en-de-vrede-van-versailles-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Eerste Wereldoorlog en de Vrede van Versailles",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oorzaak of aanleiding?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "de moord op Frans Ferdinand in Sarajevo", ["oorzaak", "aanleiding"], 1),
                 ("kies", "de wapenwedloop tussen de grote mogendheden", ["oorzaak", "aanleiding"], 0),
                 ("kies", "het stelsel van bondgenootschappen", ["oorzaak", "aanleiding"], 0),
                 ("kies", "de spanningen op de Balkan", ["oorzaak", "aanleiding"], 0),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("een oorlog waarin het hele land wordt ingeschakeld", "een totale oorlog"),
                          ("vechten van stellingen in de grond, zonder vooruitgang", "de loopgravenoorlog"),
                          ("berichten die bewust de eigen zaak moeten steunen", "propaganda")],
                  "Welk begrip?", WL),
                 ("rij", [("het artikel dat Duitsland schuldig verklaarde", "het schuldartikel"),
                          ("geld dat de verliezer moet betalen aan de overwinnaars", "herstelbetalingen"),
                          ("de organisatie van 1920 die de vrede moest bewaren", "de Volkenbond")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Vul de tabel aan",
             opdracht="Schrijf per onderdeel van het verdrag van Versailles kort wat het betekende voor Duitsland.",
             oefeningen=[
                 ("tabel", ["Onderdeel", "Gevolg voor Duitsland"], [
                     ["Gebied", None],
                     ["Leger", None],
                     ["Geld", None],
                     ["Schuld", None],
                 ], "Gebied: verlies van Elzas-Lotharingen en van alle koloniën. Leger: een sterk beperkt "
                    "leger, geen zware wapens, het Rijnland gedemilitariseerd. Geld: zware "
                    "herstelbetalingen. Schuld: het schuldartikel legde de verantwoordelijkheid voor de "
                    "oorlog bij Duitsland.", "280px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het Duitse leger viel België binnen op 4 augustus 1914.", True),
                 ("waar", "België was volgens de verdragen neutraal.", True),
                 ("waar", "De oorlog was na enkele maanden beslist, zoals de generaals verwacht hadden.", False),
                 ("waar", "Duitsland mocht in Versailles meeonderhandelen over de voorwaarden.", False),
                 ("waar", "De Verenigde Staten zijn nooit lid geworden van de Volkenbond.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom men de Eerste Wereldoorlog een totale oorlog noemt.",
                  "Niet alleen de legers vochten: de fabrieken werden omgeschakeld naar oorlogsproductie, "
                  "vrouwen namen het werk over, de bevolking kreeg rantsoenering en propaganda, en de "
                  "burgerbevolking werd een doelwit. De hele samenleving stond in dienst van de oorlog.", 6),
                 ("open", "Leg uit waarom het verdrag van Versailles de vrede eerder bedreigde dan bewaarde.",
                  "Duitsland werd vernederd en kreeg de schuld en de rekening, maar bleef groot en sterk "
                  "genoeg om zich te verzetten. De Duitse bevolking voelde het als een dictaat, en die "
                  "wrok werd later door de nazi's gebruikt.", 6),
                 ("open", "Wat veranderde de oorlog aan de positie van vrouwen in België?",
                  "Vrouwen namen tijdens de oorlog werk over in fabrieken, in het bestuur en in de zorg, en "
                  "dat ondergroef het argument dat ze daar niet thuishoorden. Het stemrecht kwam er pas veel "
                  "later, maar de discussie erover was geopend.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-interbellum-de-opkomst-van-het-totalitarisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het interbellum: de opkomst van het totalitarisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk regime?",
             opdracht="Noteer bij elke omschrijving het regime: het fascisme in Italië, het "
                      "nationaalsocialisme in Duitsland of het communisme in de Sovjet-Unie.",
             oefeningen=[
                 ("rij", [("Mussolini en de mars op Rome", "het fascisme in Italië"),
                          ("de rassenleer en de Jodenvervolging", "het nationaalsocialisme in Duitsland"),
                          ("de vijfjarenplannen en de collectivisatie", "het communisme in de Sovjet-Unie")],
                  "Welk regime?", WL),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("een staat die het hele leven van de burger wil beheersen", "een totalitaire staat"),
                          ("de verering van de leider als onfeilbaar", "de leiderscultus"),
                          ("de overheid controleert vooraf wat er gepubliceerd wordt", "censuur")],
                  "Welk begrip?", WL),
                 ("rij", [("de beurskrach van 1929 en de jaren erna", "de crisis van de jaren dertig"),
                          ("de hyperinflatie die het Duitse spaargeld wegvaagde", "de inflatie van 1923"),
                          ("de politiek om Hitler tevreden te stellen met toegevingen", "de appeasement")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Hitler kwam in 1933 langs de grondwet aan de macht, als kanselier.", True),
                 ("waar", "De crisis van de jaren dertig maakte extreme partijen sterker.", True),
                 ("waar", "Een totalitaire staat laat vrije verkiezingen en meerdere partijen toe.", False),
                 ("waar", "De Volkenbond kon de aanvallen van Italië en Japan tegenhouden.", False),
                 ("waar", "Ook in België groeiden in de jaren dertig autoritaire partijen.", True),
             ]),
        dict(kop="Propaganda lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem drie middelen waarmee een totalitair regime de publieke opinie beheerste.",
                  "Censuur van kranten, boeken en films, één eigen jeugdbeweging en één partij, en "
                  "massamanifestaties met beelden van de leider. Daarnaast nieuwe media zoals radio en film, "
                  "en een geheime politie die tegenspraak onmogelijk maakte.", 5),
                 ("open", "Waarom is een propagandaposter een goede bron, maar niet voor de vraag hoe het "
                          "land er werkelijk aan toe was?",
                  "Een poster is gemaakt om te overtuigen, niet om te informeren. Hij is een uitstekende "
                  "bron voor wat het regime wilde laten zien en voor de beelden waarmee het werkte, maar "
                  "voor de werkelijke toestand heb je andere bronnen nodig.", 5),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit hoe de crisis en het verdrag van Versailles samen de opkomst van de "
                          "nazi's verklaren.",
                  "Versailles leverde de wrok en het verhaal van de vernedering, de crisis leverde de "
                  "massale werkloosheid en de angst. De nazi's beloofden werk, orde en herstel van de eer, "
                  "en wezen een vijand aan. Zonder die twee samen was hun doorbraak onwaarschijnlijk.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-tweede-wereldoorlog-en-de-holocaust-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Tweede Wereldoorlog en de Holocaust",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer van 1 tot 6, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Gebeurtenis"], [
                     [None, "de landing in Normandië"],
                     [None, "de Duitse inval in Polen"],
                     [None, "de Achttiendaagse Veldtocht in België"],
                     [None, "de Duitse inval in de Sovjet-Unie"],
                     [None, "de capitulatie van Duitsland"],
                     [None, "de aanval op Pearl Harbor"],
                 ], "1 = de inval in Polen (september 1939) · 2 = de Achttiendaagse Veldtocht (mei 1940) · "
                    "3 = de inval in de Sovjet-Unie (juni 1941) · 4 = Pearl Harbor (december 1941) · "
                    "5 = de landing in Normandië (juni 1944) · 6 = de capitulatie van Duitsland (mei 1945)",
                  "56px"),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de snelle aanval met tanks en vliegtuigen samen", "de blitzkrieg"),
                          ("de systematische moord op de Joden van Europa", "de Holocaust"),
                          ("wie met de bezetter samenwerkte", "een collaborateur")], "Welk begrip?", WL),
                 ("rij", [("wie zich tegen de bezetter verzette", "een verzetsman of verzetsvrouw"),
                          ("de afrekening met collaborateurs na de oorlog", "de repressie"),
                          ("het doorgangskamp in Mechelen", "de Dossinkazerne")], "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "België werd in mei 1940 binnengevallen, ondanks zijn neutraliteit.", True),
                 ("waar", "Vanuit de Dossinkazerne in Mechelen vertrokken transporten naar Auschwitz.", True),
                 ("waar", "De Holocaust was het werk van enkele mensen zonder medewerking van een administratie.", False),
                 ("waar", "Het verzet in België bestond onder meer uit sluikpers, hulp aan onderduikers en sabotage.", True),
                 ("waar", "Na de oorlog werden de nazileiders in Nürnberg berecht.", True),
             ]),
        dict(kop="Bron beoordelen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Een Belgische krant van 1942 verscheen onder toezicht van de bezetter. Voor "
                          "welke vraag is zo een krant juist de beste bron?",
                  "Voor de vraag wat de bezetter wilde laten lezen en hoe hij over het verzet en over de "
                  "Joden sprak. Voor de feiten zelf is ze onbetrouwbaar, want ze stond onder censuur.", 5),
                 ("open", "Waarom blijven ooggetuigenverslagen van overlevenden belangrijk, ook al werden ze "
                          "pas tientallen jaren later opgetekend?",
                  "Over precieze data en aantallen is het geheugen minder betrouwbaar, maar over de "
                  "beleving, de angst en het dagelijks overleven zijn ze onvervangbaar. Je legt ze naast "
                  "de administratieve bronnen, die het aantal en de organisatie vastleggen.", 6),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het ontkennen van de Holocaust geen mening is.",
                  "Een mening gaat over wat je van iets vindt. De Holocaust is een feit, vastgesteld met "
                  "duizenden bronnen: administratie, getuigenissen, de kampen zelf en de processen. "
                  "Ontkennen betekent vastgestelde feiten loochenen, en dat is in België bij wet strafbaar.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-china-van-keizerrijk-tot-wereldmacht-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="China: van keizerrijk tot wereldmacht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer van 1 tot 5, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Gebeurtenis"], [
                     [None, "Mao sticht de Volksrepubliek China"],
                     [None, "de Opiumoorlogen tegen Groot-Brittannië"],
                     [None, "de economische hervormingen van Deng Xiaoping"],
                     [None, "het einde van het keizerrijk"],
                     [None, "de Culturele Revolutie"],
                 ], "1 = de Opiumoorlogen (vanaf 1839) · 2 = het einde van het keizerrijk (1911-1912) · "
                    "3 = de Volksrepubliek (1949) · 4 = de Culturele Revolutie (vanaf 1966) · "
                    "5 = de hervormingen van Deng Xiaoping (vanaf 1978)", "56px"),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("verdragen die China opgelegde voorwaarden deden aanvaarden", "de ongelijke verdragen"),
                          ("de poging om China in enkele jaren te industrialiseren", "de Grote Sprong Voorwaarts"),
                          ("de campagne tegen het oude en tegen de critici van Mao", "de Culturele Revolutie")],
                  "Welk begrip?", WL),
                 ("rij", [("gebied waar buitenlandse investeerders eigen regels krijgen", "een speciale economische zone"),
                          ("de maatregel die gezinnen tot één kind beperkte", "de eenkindpolitiek"),
                          ("het oude bestuur met een keizer aan het hoofd", "het keizerrijk")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "China werd in de negentiende eeuw nooit volledig gekoloniseerd, maar wel in "
                          "invloedssferen verdeeld.", True),
                 ("waar", "De Grote Sprong Voorwaarts leidde tot een hongersnood met miljoenen doden.", True),
                 ("waar", "Deng Xiaoping voerde ook politieke democratie in.", False),
                 ("waar", "Hongkong werd in 1997 aan China teruggegeven.", True),
                 ("waar", "China is vandaag een van de grootste economieën van de wereld.", True),
             ]),
        dict(kop="Vergelijken op papier",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Onder Mao", "Na 1978"], [
                     ["Economie", None, None],
                     ["Band met het buitenland", None, None],
                 ], "Economie: volledig door de staat gepland, collectieve landbouw / markt toegelaten, "
                    "privé-ondernemingen, buitenlandse investeringen. Band met het buitenland: afgesloten en "
                    "wantrouwig / open voor handel, export en investeringen, maar politiek nog steeds één "
                    "partij.", "180px"),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de Opiumoorlogen in China 'de eeuw van de vernedering' inluidden.",
                  "China moest na de nederlagen verdragen aanvaarden die het zelf niet gekozen had: havens "
                  "openen, gebieden afstaan en buitenlanders eigen rechtspraak geven. Het keizerrijk bleek "
                  "militair en technisch achterop, en die vernedering werd later een vast onderdeel van het "
                  "Chinese zelfbeeld.", 6),
                 ("open", "Waarom noemt men de Chinese weg na 1978 soms een economische revolutie zonder "
                          "politieke revolutie?",
                  "De economie werd grondig hervormd met markt, privé-eigendom en buitenlandse "
                  "investeringen, waardoor honderden miljoenen mensen uit de armoede kwamen. Politiek bleef "
                  "één partij alle macht houden, zonder vrije verkiezingen of vrije pers.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-nieuwe-wereldorde-de-verenigde-naties-en-de-koude-oorlog-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oost of west?",
             opdracht="Kruis aan bij welk blok het hoort.",
             oefeningen=[
                 ("kies", "de NATO", ["het westen", "het oosten"], 0),
                 ("kies", "het Warschaupact", ["het westen", "het oosten"], 1),
                 ("kies", "het Marshallplan", ["het westen", "het oosten"], 0),
                 ("kies", "de Comecon", ["het westen", "het oosten"], 1),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("de politiek om de uitbreiding van het communisme tegen te houden", "de containment"),
                          ("de zekerheid dat een aanval de aanvaller zelf vernietigt", "de afschrikking"),
                          ("een conflict dat elders uitgevochten wordt tussen bondgenoten", "een proxyoorlog")],
                  "Welk begrip?", WL),
                 ("rij", [("het orgaan van de VN met vijf vaste leden", "de Veiligheidsraad"),
                          ("het recht van een vast lid om een beslissing tegen te houden", "het vetorecht"),
                          ("de periode van ontspanning in de jaren zeventig", "de detente")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De Verenigde Naties werden in 1945 opgericht in San Francisco.", True),
                 ("waar", "De Universele Verklaring van de Rechten van de Mens is van 1948.", True),
                 ("waar", "De Verenigde Staten en de Sovjet-Unie hebben elkaar nooit rechtstreeks bestreden "
                          "met hun eigen legers.", True),
                 ("waar", "De Veiligheidsraad kan beslissen zonder dat één vast lid het kan tegenhouden.", False),
                 ("waar", "De val van de Berlijnse Muur in 1989 was het begin van het einde van de Koude Oorlog.", True),
             ]),
        dict(kop="Welke crisis?",
             opdracht="Noteer bij elke omschrijving de naam van de crisis of het conflict.",
             oefeningen=[
                 ("rij", [("de blokkade van West-Berlijn en de luchtbrug", "de Berlijnse blokkade"),
                          ("Sovjetraketten op een eiland bij Florida", "de Cubacrisis"),
                          ("een jarenlange oorlog in Zuidoost-Azië met Amerikaanse troepen", "de Vietnamoorlog")],
                  "Welke crisis?", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom men spreekt van een koude oorlog en niet van een oorlog.",
                  "De twee supermachten vochten niet rechtstreeks tegen elkaar met hun legers. Ze streden met "
                  "wapenwedloop, spionage, propaganda, economische druk en oorlogen in andere landen. De "
                  "kernwapens maakten een rechtstreekse oorlog te gevaarlijk voor beide partijen.", 6),
                 ("open", "De VN hebben het vetorecht van vijf landen. Noem één voordeel en één nadeel.",
                  "Voordeel: de grote mogendheden bleven in de organisatie, want ze konden niet overstemd "
                  "worden, en dat hield het overleg in leven. Nadeel: de Veiligheidsraad raakt verlamd zodra "
                  "een vast lid zelf betrokken is bij een conflict.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-europese-eenmaking-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Europese eenmaking",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer van 1 tot 5, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap"], [
                     [None, "het Verdrag van Maastricht"],
                     [None, "de Europese Gemeenschap voor Kolen en Staal"],
                     [None, "de euro als contant geld in de winkel"],
                     [None, "het Verdrag van Rome en de EEG"],
                     [None, "de toetreding van tien nieuwe lidstaten, vooral uit Midden-Europa"],
                 ], "1 = de EGKS (1951-1952) · 2 = het Verdrag van Rome (1957) · 3 = het Verdrag van "
                    "Maastricht (1992) · 4 = de euro als contant geld (2002) · 5 = de grote uitbreiding "
                    "(2004)", "56px"),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("een gebied zonder invoerrechten tussen de leden", "een douane-unie"),
                          ("het vrij verkeer van goederen, personen, diensten en kapitaal", "de interne markt"),
                          ("het afschaffen van de controles aan de binnengrenzen", "de Schengenruimte")],
                  "Welk begrip?", WL),
                 ("rij", [("de enige rechtstreeks verkozen instelling van de Unie", "het Europees Parlement"),
                          ("de instelling die wetsvoorstellen doet", "de Europese Commissie"),
                          ("bevoegdheden samen uitoefenen in plaats van elk apart", "supranationaliteit")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "België was een van de zes stichtende landen.", True),
                 ("waar", "De samenwerking begon bij kolen en staal, de grondstoffen van de oorlogsindustrie.", True),
                 ("waar", "Alle lidstaten van de Europese Unie gebruiken de euro.", False),
                 ("waar", "Het Verenigd Koninkrijk heeft de Unie verlaten.", True),
                 ("waar", "Het Europees Parlement wordt door de regeringen benoemd.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de eenmaking juist met kolen en staal begon.",
                  "Kolen en staal waren de grondstoffen waarmee je wapens maakt. Door die productie samen te "
                  "beheren, kon geen van de landen in het geheim herbewapenen. Zo werd een nieuwe oorlog "
                  "tussen Frankrijk en Duitsland praktisch moeilijk, en groeide tegelijk de economische "
                  "samenwerking.", 6),
                 ("open", "Noem twee zaken die je als burger merkt van de Europese Unie, en leg per zaak uit "
                          "waardoor dat kan.",
                  "Je kan zonder paspoortcontrole naar Frankrijk reizen, door de Schengenruimte. Je betaalt "
                  "in Spanje met dezelfde munt, door de euro en de monetaire unie. Je kan ook in een ander "
                  "land studeren of werken, door het vrij verkeer van personen.", 6),
                 ("open", "Sommigen vinden dat de Unie te veel beslist boven de hoofden van de lidstaten. "
                          "Verklaar dat standpunt met het begrip supranationaliteit.",
                  "Supranationaliteit betekent dat landen bevoegdheden samen uitoefenen en dat Europese "
                  "regels voorgaan op nationale. Wie daar kritiek op heeft, vindt dat beslissingen te ver "
                  "van de kiezer genomen worden. Wie ervoor is, wijst erop dat sommige problemen enkel "
                  "samen op te lossen zijn.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-dekolonisatie-van-congo-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De dekolonisatie van Congo",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zet in de juiste orde",
             opdracht="Nummer van 1 tot 5, van vroeg naar laat.",
             oefeningen=[
                 ("tabel", ["Nummer", "Gebeurtenis"], [
                     [None, "de moord op Patrice Lumumba"],
                     [None, "de rellen in Leopoldstad"],
                     [None, "Mobutu grijpt de macht"],
                     [None, "de onafhankelijkheid van Congo"],
                     [None, "Katanga roept zijn afscheiding uit"],
                 ], "1 = de rellen in Leopoldstad (januari 1959) · 2 = de onafhankelijkheid (30 juni 1960) · "
                    "3 = de afscheiding van Katanga (juli 1960) · 4 = de moord op Lumumba (januari 1961) · "
                    "5 = Mobutu grijpt de macht (1965)", "56px"),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("het proces waarbij koloniën onafhankelijk worden", "de dekolonisatie"),
                          ("een gebied dat zich van de nieuwe staat wil losmaken", "een afscheiding"),
                          ("een bestuur waarin één man alle macht heeft", "een dictatuur")],
                  "Welk begrip?", WL),
                 ("rij", [("een onafhankelijkheid die economisch afhankelijk blijft", "neokolonialisme"),
                          ("de VN-troepen die naar Congo gestuurd werden", "een vredesmacht"),
                          ("de eerste premier van onafhankelijk Congo", "Patrice Lumumba")],
                  "Welk begrip of wie?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Congo werd onafhankelijk op 30 juni 1960.", True),
                 ("waar", "De onafhankelijkheid werd jaren vooraf grondig voorbereid.", False),
                 ("waar", "Katanga was rijk aan koper en was economisch het belangrijkste gebied.", True),
                 ("waar", "België had in 1960 duizenden Congolese universitair geschoolden klaar voor het bestuur.", False),
                 ("waar", "Een Belgische parlementaire onderzoekscommissie onderzocht later de betrokkenheid "
                          "bij de moord op Lumumba.", True),
             ]),
        dict(kop="Bron beoordelen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Op 30 juni 1960 hield Lumumba een toespraak waarin hij het koloniale onrecht "
                          "benoemde, tegen de verwachtingen van de plechtigheid in. Waarom is die toespraak "
                          "een belangrijke bron?",
                  "Omdat ze de Congolese stem zelf laat horen op het moment van de machtsoverdracht, en "
                  "omdat ze toont dat de Congolese leiders de kolonisatie heel anders beoordeelden dan de "
                  "Belgische regering. Ze maakt de spanning van dat moment zichtbaar.", 6),
                 ("open", "Een Belgische krant van juli 1960 schrijft over 'chaos in Congo'. Wat voeg je als "
                          "historicus aan die woordkeuze toe?",
                  "Je plaatst ze in haar context: de krant schreef voor een Belgisch publiek dat net zijn "
                  "kolonie verloor. Je vermeldt ook wat de krant weglaat, namelijk dat de nieuwe staat zonder "
                  "opgeleide bestuurders en met een afscheiding en buitenlandse belangen moest beginnen.", 6),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de onafhankelijkheid van Congo zo moeilijk begon.",
                  "De voorbereiding was te kort, er waren nauwelijks Congolese artsen, ingenieurs en hoge "
                  "ambtenaren, het leger kwam in opstand, Katanga scheidde zich af en buitenlandse "
                  "mijnbelangen speelden mee. De Koude Oorlog maakte van het conflict ook een strijd tussen "
                  "oost en west.", 7),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-belgie-na-1945-breuklijnen-federale-staat-en-emancipatie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="België na 1945: breuklijnen, federale staat en emancipatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke breuklijn?",
             opdracht="Noteer bij elk conflict de breuklijn: de sociaaleconomische, de filosofische of de "
                      "communautaire.",
             oefeningen=[
                 ("rij", [("de schoolstrijd over het katholiek en het officieel onderwijs", "de filosofische"),
                          ("de staking tegen de Eenheidswet", "de sociaaleconomische"),
                          ("de splitsing van de universiteit van Leuven", "de communautaire")],
                  "Welke breuklijn?", WL),
                 ("rij", [("de Koningskwestie over Leopold III", "de filosofische"),
                          ("het vastleggen van de taalgrens", "de communautaire"),
                          ("de onderhandelingen over lonen tussen vakbonden en werkgevers", "de sociaaleconomische")],
                  "Welke breuklijn?", WL),
             ]),
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("verenigingen voor school, zorg en vrije tijd per strekking", "de verzuiling"),
                          ("het akkoord van 1944 over sociale zekerheid", "het sociaal pact"),
                          ("de omvorming van België tot een staat met deelstaten", "de staatshervorming")],
                  "Welk begrip?", WL),
                 ("rij", [("de gewesten en de gemeenschappen samen", "de deelstaten"),
                          ("het stemrecht voor vrouwen bij de nationale verkiezingen", "het vrouwenstemrecht"),
                          ("de overgang van de steenkool naar andere bedrijvigheid", "de economische omschakeling")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Vrouwen kregen in 1948 stemrecht voor de nationale verkiezingen.", True),
                 ("waar", "De taalgrens werd in 1962 en 1963 bij wet vastgelegd.", True),
                 ("waar", "De verzuiling staat volledig los van de drie breuklijnen.", False),
                 ("waar", "België werd in één keer een federale staat.", False),
                 ("waar", "De sluiting van de Limburgse steenkoolmijnen was een zware economische omschakeling.", True),
             ]),
        dict(kop="Vul de tabel aan",
             opdracht="Schrijf per deelstaat kort waarvoor ze bevoegd is.",
             oefeningen=[
                 ("tabel", ["Deelstaat", "Waarvoor bevoegd?"], [
                     ["De gewesten", None],
                     ["De gemeenschappen", None],
                 ], "De gewesten: wat met het gebied te maken heeft, zoals economie, werk, mobiliteit, "
                    "leefmilieu en ruimtelijke ordening. De gemeenschappen: wat met de personen en hun taal "
                    "te maken heeft, zoals onderwijs, cultuur, welzijn en gezondheidszorg.", "300px"),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit hoe de drie breuklijnen de Belgische politiek van na 1945 verklaren.",
                  "Elke breuklijn leverde eigen conflicten: de Koningskwestie en de schoolstrijd op de "
                  "filosofische lijn, de stakingen en de sociale akkoorden op de sociaaleconomische, en de "
                  "taalkwestie en de staatshervormingen op de communautaire. Omdat de lijnen door elkaar "
                  "liepen, waren er altijd coalities nodig en compromissen.", 7),
                 ("open", "Waarom werd België stap voor stap federaal in plaats van in één keer?",
                  "Elke hervorming was een compromis tussen partijen die verschillende dingen wilden: meer "
                  "autonomie voor Vlaanderen, economische steun voor Wallonië en een eigen plaats voor "
                  "Brussel. Zo'n compromis lost niet alles op, dus kwam er telkens een volgende ronde.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kunst-en-cultuur-een-kunstwerk-analyseren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kunst en cultuur: een kunstwerk analyseren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stroming?",
             opdracht="Noteer bij elke omschrijving de kunststroming.",
             oefeningen=[
                 ("rij", [("gevoel, natuur en het verleden, tegen de koele rede in", "de romantiek"),
                          ("de werkelijkheid tonen zoals ze is, ook de armoede", "het realisme"),
                          ("licht en kleur weergeven zoals het oog ze op dat moment ziet", "het impressionisme")],
                  "Welke stroming?", WL),
                 ("rij", [("terug naar de strakke vormen van de oudheid", "het classicisme"),
                          ("de vorm loskoppelen van wat je in de werkelijkheid ziet", "de abstracte kunst"),
                          ("droombeelden en het onbewuste in beeld brengen", "het surrealisme")],
                  "Welke stroming?", WL),
             ]),
        dict(kop="Beschrijving of interpretatie?",
             opdracht="Kruis aan of de uitspraak over een schilderij een beschrijving is of al een interpretatie.",
             oefeningen=[
                 ("kies", "Op de voorgrond staan drie figuren in donkere kleding.",
                  ["beschrijving", "interpretatie"], 0),
                 ("kies", "De schilder wil de armoede aanklagen.", ["beschrijving", "interpretatie"], 1),
                 ("kies", "Het licht komt van links en valt op het gezicht in het midden.",
                  ["beschrijving", "interpretatie"], 0),
                 ("kies", "De bleke kleuren maken het tafereel troosteloos.",
                  ["beschrijving", "interpretatie"], 1),
             ]),
        dict(kop="Vier stappen",
             opdracht="Nummer de stappen van een kunstwerkanalyse van 1 tot 4.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap"], [
                     [None, "interpreteren: wat betekent het, voor wie was het bedoeld?"],
                     [None, "beschrijven: wat zie ik, zonder oordeel?"],
                     [None, "situeren: wie, wanneer, waar, welke stroming?"],
                     [None, "analyseren: hoe is het gemaakt, met welke middelen?"],
                 ], "1 = situeren · 2 = beschrijven · 3 = analyseren · 4 = interpreteren", "56px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een kunstwerk is ook een historische bron.", True),
                 ("waar", "Wie een kunstwerk analyseert, begint bij zijn eigen gevoel erover.", False),
                 ("waar", "De opdrachtgever van een werk bepaalde vaak mee wat erop kwam.", True),
                 ("waar", "Een kunstwerk zegt iets over de tijd waarin het gemaakt is.", True),
                 ("waar", "Een abstract werk kan geen historische betekenis hebben.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het belangrijk is om beschrijven en interpreteren apart te houden.",
                  "Een beschrijving kan iedereen controleren: ze staat op het werk. Een interpretatie is een "
                  "besluit dat je uit die beschrijving en uit de context afleidt. Wie de twee door elkaar "
                  "haalt, presenteert zijn eigen oordeel als een vaststelling.", 5),
                 ("open", "Een portret van een negentiende-eeuwse fabrikant toont hem met een fabriek op de "
                          "achtergrond. Wat leid je daaruit af?",
                  "Dat hij zijn positie aan zijn onderneming ontleende en dat ook wilde laten zien. Het "
                  "portret bevestigt het zelfbeeld van de industriële burgerij: niet afkomst maar bezit en "
                  "ondernemen geven aanzien.", 5),
                 ("open", "Waarom zegt de keuze van een stroming ook iets over de samenleving?",
                  "Een stroming komt op in een bepaalde tijd, als antwoord op wat eraan voorafging. De "
                  "romantiek reageerde op de koele rede van de verlichting, het realisme op de armoede van "
                  "de industriële steden. De kunst volgt dus de vragen van haar tijd.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-redeneren-met-bronnen-bruikbaarheid-en-betrouwbaarheid-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Redeneren met bronnen: bruikbaarheid en betrouwbaarheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Primair of secundair?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "een brief van een soldaat uit de loopgraven, 1916",
                  ["primaire bron", "secundaire bron"], 0),
                 ("kies", "een studie van een historicus uit 2015 over de loopgravenoorlog",
                  ["primaire bron", "secundaire bron"], 1),
                 ("kies", "een bevolkingsregister van de gemeente uit 1880",
                  ["primaire bron", "secundaire bron"], 0),
                 ("kies", "je handboek geschiedenis", ["primaire bron", "secundaire bron"], 1),
                 ("kies", "een werktuig uit een mijn, bewaard in een museum",
                  ["primaire bron", "secundaire bron"], 0),
             ]),
        dict(kop="Welk soort bron?",
             opdracht="Noteer bij elke bron de soort: schriftelijk, materieel, beeld of mondeling.",
             oefeningen=[
                 ("rij", [("een krantenartikel uit 1886", "schriftelijk"),
                          ("een stoommachine in een industrieel museum", "materieel"),
                          ("een foto van een fabriekshal", "beeld")], "Welke soort?", WW),
                 ("rij", [("het opgenomen gesprek met een oud-mijnwerker", "mondeling"),
                          ("een affiche voor een staking", "beeld"),
                          ("de notulen van de gemeenteraad", "schriftelijk")], "Welke soort?", WW),
             ]),
        dict(kop="Bruikbaar voor deze vraag?",
             opdracht="De onderzoeksvraag is: hoe woonden mijnwerkersgezinnen in Limburg rond 1950? "
                      "Kruis aan of de bron voor díé vraag bruikbaar is.",
             oefeningen=[
                 ("kies", "een huurcontract van een mijnwerkerswoning in Zwartberg, 1951",
                  ["bruikbaar", "niet bruikbaar"], 0),
                 ("kies", "een reportage over de Waalse staalindustrie in 1951",
                  ["bruikbaar", "niet bruikbaar"], 1),
                 ("kies", "foto's van de mijncité in Eisden, jaren vijftig",
                  ["bruikbaar", "niet bruikbaar"], 0),
                 ("kies", "een studie over de Limburgse mijnen in de achttiende eeuw",
                  ["bruikbaar", "niet bruikbaar"], 1),
             ]),
        dict(kop="Feit, mening of waardeoordeel?",
             opdracht="Noteer bij elke uitspraak wat het is.",
             oefeningen=[
                 ("rij", [("Congo werd onafhankelijk op 30 juni 1960.", "feit"),
                          ("De dekolonisatie werd veel te slecht voorbereid.", "waardeoordeel"),
                          ("Volgens mij was Lumumba de belangrijkste leider van zijn generatie.", "mening")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Vier vragen bij een bron",
             opdracht="Vul de tabel aan voor deze bron: een affiche van de Belgische regering uit 1915, "
                      "gedrukt in Londen, die mannen oproept om zich bij het leger te melden.",
             oefeningen=[
                 ("tabel", ["Vraag", "Antwoord"], [
                     ["Wie maakte ze?", None],
                     ["Wanneer?", None],
                     ["Voor wie?", None],
                     ["Met welk doel?", None],
                 ], "Wie: de Belgische regering, die in ballingschap zat. Wanneer: 1915, tijdens de oorlog. "
                    "Voor wie: Belgische mannen in het buitenland en in het niet-bezette gebied. Doel: "
                    "overtuigen om zich te melden, dus propaganda. Ze is onbetrouwbaar over de toestand aan "
                    "het front, maar een uitstekende bron over de boodschap van de regering.", "260px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een primaire bron is altijd betrouwbaarder dan een secundaire.", False),
                 ("waar", "Of een bron bruikbaar is, hangt af van de vraag die je stelt.", True),
                 ("waar", "Overnemen zonder de herkomst te vermelden heet plagiaat.", True),
                 ("waar", "Een website die bovenaan de zoekresultaten staat, is daardoor betrouwbaar.", False),
                 ("waar", "Eén bron is genoeg om een besluit te onderbouwen.", False),
                 ("waar", "Een foto is vandaag op zichzelf geen bewijs meer.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een krant uit 1942 stond onder censuur van de bezetter. Leg uit waarom ze "
                          "onbetrouwbaar én bruikbaar kan zijn.",
                  "Onbetrouwbaar voor de feiten, want de bezetter bepaalde wat erin stond. Bruikbaar voor de "
                  "vraag wat de bezetter wilde laten lezen en met welke woorden hij over het verzet sprak. "
                  "De bruikbaarheid hangt dus af van je onderzoeksvraag.", 6),
                 ("open", "Twee bronnen over dezelfde staking spreken elkaar tegen. Wat doe je?",
                  "Je zoekt per bron uit wie ze maakte en welk belang die had, je kijkt naar de afstand tot "
                  "de gebeurtenis, en je zoekt bronnen bij. De tegenspraak zelf is een aanwijzing dat er "
                  "iets uit te leggen valt, en in je besluit vermeld je wat je niet met zekerheid weet.", 6),
                 ("open", "Waarom vermeldt een historicus altijd waar hij zijn informatie haalde?",
                  "Zodat anderen zijn werk kunnen nagaan en controleren, en zodat duidelijk is welke bron "
                  "welke uitspraak draagt. Het is ook een kwestie van eerlijkheid: wie het niet doet, pleegt "
                  "plagiaat.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-beeldvorming-standplaatsgebondenheid-en-betekenisgeving-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Beeldvorming, standplaatsgebondenheid en betekenisgeving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrip en omschrijving",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("een vast en vereenvoudigd beeld van een hele groep", "een stereotype"),
                          ("een gebeurtenis vanuit verschillende standpunten bekijken", "multiperspectiviteit"),
                          ("Europa als maatstaf voor het hele verhaal nemen", "eurocentrisme")],
                  "Welk begrip?", WL),
                 ("rij", [("proberen te begrijpen waarom mensen toen zo handelden", "historische empathie"),
                          ("de waarde die een samenleving aan haar verleden geeft", "betekenisgeving"),
                          ("wat uit het verleden bewaard en doorgegeven wordt", "erfgoed")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar zie je betekenisgeving?",
             opdracht="Noteer bij elk voorbeeld wat de samenleving ermee uitdrukt.",
             oefeningen=[
                 ("kort", "11 november is in België een feestdag. Waarvoor staat die dag?",
                  "de wapenstilstand van 1918, het einde van de Eerste Wereldoorlog", WL),
                 ("kort", "Een straat wordt naar een verzetsvrouw genoemd. Wat zegt dat?",
                  "dat de samenleving haar daad vandaag belangrijk en navolgbaar vindt", WL),
                 ("kort", "Een gebouw krijgt de status van beschermd erfgoed. Wat zegt dat?",
                  "dat men vindt dat het bewaard en doorgegeven moet worden aan de volgende generaties", WL),
             ]),
        dict(kop="Geschiedenis of herinnering?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "een onderzoek naar het aantal slachtoffers van een bombardement",
                  ["geschiedenis", "herinnering"], 0),
                 ("kies", "een minuut stilte op de plaats van dat bombardement",
                  ["geschiedenis", "herinnering"], 1),
                 ("kies", "een studie over hoe een land zijn oorlogsverleden herdenkt",
                  ["geschiedenis", "herinnering"], 0),
                 ("kies", "een jaarlijkse optocht met fakkels ter nagedachtenis",
                  ["geschiedenis", "herinnering"], 1),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Ook een historicus van vandaag is standplaatsgebonden.", True),
                 ("waar", "Historische empathie betekent dat je goedkeurt wat mensen toen deden.", False),
                 ("waar", "Het beeld van een periode kan veranderen door nieuwe vragen en nieuwe bronnen.", True),
                 ("waar", "Een handboek is volledig en neutraal.", False),
                 ("waar", "Het ontkennen van de Holocaust is in België bij wet strafbaar.", True),
                 ("waar", "Wat een land herdenkt, blijft door de jaren altijd hetzelfde.", False),
             ]),
        dict(kop="Een omstreden standbeeld",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem twee mogelijke oplossingen voor een standbeeld dat onder vuur ligt, en geef "
                          "bij elk een voordeel.",
                  "Een bord met uitleg bij het beeld plaatsen: het beeld blijft staan als spoor van zijn "
                  "eigen tijd, maar krijgt context. Het beeld naar een museum verplaatsen: het blijft "
                  "bewaard en kan daar grondig uitgelegd worden, zonder dat het nog een eregroet lijkt op "
                  "het plein.", 6),
                 ("open", "Leg uit waarom zo'n discussie evenveel over het heden als over het verleden gaat.",
                  "Het beeld zelf verandert niet. Wat verandert, is hoe wij vandaag naar die persoon kijken "
                  "en wat wij in de openbare ruimte willen eren. Een monument zegt daarbij ook iets over de "
                  "tijd waarin het geplaatst werd.", 5),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Twee eerlijke ooggetuigen beschrijven dezelfde gebeurtenis anders. Leg uit hoe "
                          "dat kan zonder dat een van beide liegt.",
                  "Elk van hen stond op een andere plaats, zag een ander deel, en had een andere achtergrond "
                  "en een ander belang. Dat is standplaatsgebondenheid. Door beide verslagen naast elkaar te "
                  "leggen, krijg je een vollediger beeld dan met één ervan.", 6),
                 ("open", "Een Belgisch en een Congolees handboek beschrijven 1960 verschillend. Leg uit "
                          "waarin het verschil zit.",
                  "Niet in de feiten, maar in de nadruk en in de hoofdrollen: welk verhaal centraal staat, "
                  "wie als held of als schuldige verschijnt, en wat weggelaten wordt. Elk boek is geschreven "
                  "in een land met zijn eigen vragen over dat verleden.", 6),
                 ("open", "Waarom studeer je geschiedenis als ze de toekomst niet kan voorspellen?",
                  "Om te begrijpen hoe het heden geworden is wat het is: grenzen, instellingen, "
                  "ongelijkheden en gevoeligheden hebben een voorgeschiedenis. En om processen te herkennen "
                  "die opnieuw werken: hoe propaganda werkt, hoe een crisis een samenleving splijt, hoe "
                  "rechten verworven en weer verloren raken.", 6),
             ]),
    ],
)

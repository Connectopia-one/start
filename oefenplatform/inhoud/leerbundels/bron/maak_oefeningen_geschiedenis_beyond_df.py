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
                 ("rij", [("de Franse Revolutie", "het einde van de vroegmoderne tijd"),
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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-het-historisch-referentiekader-tijd-ruimte-en-domeinen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke gebeurtenis een jaartal dat je kent en kijk tussen welke twee "
                   "scharnierpunten het valt. De vroegmoderne tijd loopt van ongeveer 1500 tot 1789 "
                   "of 1815, de moderne tijd daarna tot 1945.",
            waarom=[
                "Let op de boekdruk met losse letters: rond 1450, dus aan het begin van de "
                "vroegmoderne tijd. Dat is zelf een van de scharnierpunten.",
                "Let op de Franse Revolutie: 1789 is het einde van de vroegmoderne tijd en het begin "
                "van de moderne tijd. Hetzelfde jaartal sluit de ene periode af en opent de andere.",
            ],
        ),
        dict(
            aanpak="Vraag je af of het begrip iets zegt over wanneer of over waar. Woorden op -aal "
                   "gaan bijna altijd over de ruimte.",
            waarom=[
                "Let op generatie: dat is een stuk tijd gemeten in mensenlevens, dus tijd. Urbaan "
                "betekent in de stad en lokaal ter plaatse, dus beide ruimte.",
            ],
        ),
        dict(
            aanpak="De vier domeinen zijn het politieke, het economische, het sociale en het "
                   "culturele. Zoek waar de kern van de gebeurtenis zit, niet alles wat ze raakt.",
            waarom=[
                "Let op het verschil tussen de spoorlijn en de vakbonden: een spoorlijn is in de "
                "eerste plaats economisch, een vakbond sociaal, ook al hebben beide ook politieke "
                "gevolgen.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: blijft iets hetzelfde of wordt het anders. Woorden als "
                   "eeuwenlang en zonder onderbreking wijzen op continuïteit, verdubbelt en "
                   "verdwijnt op verandering.",
            waarom=[
                None,
                None,
                None,
                "Let op dat continuïteit niet betekent dat niets veranderde. Het Nederlands van 1600 "
                "klinkt heel anders dan dat van nu, en toch bleef het de taal van het dagelijks "
                "leven.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over één idee: een periodisering maken historici achteraf, en "
                   "ze is altijd een keuze. Vraag je bij elke af of ze dat respecteert.",
            waarom=[
                None,
                None,
                "Niet waar: onze zeven periodes zijn vanuit Europa gemaakt. Voor China of de "
                "Islamwereld gebruikt men andere indelingen, en die zijn niet minder juist.",
                None,
                "Niet waar: de vier domeinen beïnvloeden elkaar voortdurend. Een economische crisis "
                "verandert de politiek, en een wet verandert het sociale leven.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg. Noem telkens dat een indeling of een "
                   "schaalniveau een keuze is, en wat die keuze oplevert.",
            waarom=[
                "Noem beide delen van de vraag: wat er in 1789 gebeurde en waarom het een keuze is. "
                "De veranderingen begonnen eerder en liepen langer door, dus iemand besloot achteraf "
                "dat dit jaar het meest in het oog springt.",
                "Noem minstens twee domeinen apart, zoals gevraagd, en leg hun verband. Enkel "
                "zeggen dat alles met alles te maken heeft, is geen analyse.",
                "Noem dat hetzelfde verhaal op elk niveau anders klinkt. Een staking in één mijn, de "
                "sociale strijd in een land en de industrialisering van de wereld zijn drie "
                "schaalniveaus van dezelfde geschiedenis.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kenmerken-van-samenlevingen-vergelijken-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier kenmerken om een samenleving te beschrijven: wie bestuurt, waarvan men "
                   "leeft, hoe de groepen tegenover elkaar staan, en wat men denkt en gelooft.",
            waarom=[
                "Let op het verschil tussen de eerste en de derde: standen met eigen rechten gaat "
                "over de verhouding tussen groepen, dus sociale verhoudingen, terwijl een koning "
                "zonder parlement over het bestuur gaat.",
                "Let op de kerk die bepaalt wat men mag denken: dat is cultuur, ook al heeft die "
                "kerk veel politieke macht. Het gevraagde kenmerk is wat er in de eerste plaats "
                "geregeld wordt.",
            ],
        ),
        dict(
            aanpak="Twee vragen helpen altijd: hangt je plaats af van je geboorte of van je bezit, "
                   "en staat de macht van de vorst boven of onder de wet.",
            waarom=[
                None,
                None,
                "Let op de leer van het droit divin: de vorst dankt zijn macht aan God en is dus aan "
                "niemand verantwoording schuldig. Precies dat idee verdwijnt met een grondwet.",
                None,
            ],
        ),
        dict(
            aanpak="Vergelijk altijd op dezelfde drie vragen: wie bestuurt, hoe krijg je je plaats, "
                   "en wie mag stemmen. Zo staan de twee samenlevingen echt naast elkaar.",
            waarom=[
                "Let op de laatste rij: in de negentiende eeuw mocht niet iedereen stemmen maar "
                "enkel wie genoeg belasting betaalde. Dat heet het cijnskiesrecht, en het is dus een "
                "halve stap en geen volledige.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over hoe je vergelijkt: op welke kenmerken, in welke tijd, en "
                   "met welk doel. Een vergelijking zoekt inzicht, geen winnaar.",
            waarom=[
                None,
                "Niet waar: je kan ook twee samenlevingen uit verschillende tijden vergelijken, "
                "zoals het ancien régime en vandaag. Dan heet het een diachrone vergelijking.",
                None,
                "Niet waar: een vergelijking levert overeenkomsten en verschillen op, geen rangorde. "
                "Wie een winnaar aanwijst, oordeelt met de maatstaf van zijn eigen tijd.",
                None,
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een onderscheid en een eigen keuze. Noem bij een "
                   "vergelijking altijd waarom je die kenmerken kiest.",
            waarom=[
                "Noem beide kanten: in een standenmaatschappij staat je plaats in de wet, in een "
                "klassenmaatschappij zijn allen gelijk voor de wet en beslist het bezit in de "
                "praktijk.",
                "Noem er drie, zoals gevraagd, en zeg bij elk waarom. Een kenmerk is bruikbaar als "
                "het op beide momenten bestaat; anders kan je het niet vergelijken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-restauratie-en-revolutie-het-congres-van-wenen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer elk begrip aan één beeld: de klok terugzetten, de weegschaal in evenwicht, "
                   "vorsten die elkaar steunen, en een recht dat van vader op zoon gaat.",
            waarom=[
                "Let op het verschil tussen restauratie en machtsevenwicht: het eerste gaat over "
                "terug naar vroeger, het tweede over de verdeling tussen de mogendheden. Op het "
                "congres gingen die twee hand in hand.",
                "Let op de Honderd Dagen: Napoleon kwam in 1815 terug terwijl het congres nog "
                "vergaderde, en werd bij Waterloo definitief verslagen. Legitimiteit was net het "
                "argument waarmee men zijn troon afwees.",
            ],
        ),
        dict(
            aanpak="Drie namen, drie landen. Metternich hoort bij Oostenrijk en leidde het congres, "
                   "en Talleyrand was de Franse onderhandelaar van de verslagen kant.",
            waarom=[
                "Let op dat Talleyrand voor Frankrijk sprak, dus voor het verslagen land. Dat hij "
                "toch mocht meebeslissen, is een van de merkwaardigste punten van het congres.",
            ],
        ),
        dict(
            aanpak="Een beslissing stond in de slotakte, een gevolg kwam later uit die beslissing "
                   "voort. Vraag je af of de diplomaten het zo opschreven.",
            waarom=[
                None,
                "Let op het verschil met de vorige: dat de twee Nederlanden samengevoegd werden, is "
                "een beslissing; dat het daar misliep, is een gevolg. Juist dat onderscheid is wat "
                "deze reeks toetst.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe het congres werkte, wat het niet "
                   "meenam, en wat het wel bereikte. Vraag je bij elke af welk van de drie.",
            waarom=[
                None,
                "Niet waar: niemand vroeg de bevolking iets. Men keek naar het evenwicht tussen de "
                "mogendheden, en precies daarom brak het nationalisme later overal door.",
                "Waar: Talleyrand kreeg een plaats aan de tafel. Vergelijk dat met 1919, toen "
                "Duitsland in Versailles niet mocht meeonderhandelen en het verdrag als een dictaat "
                "ervaren werd.",
                "Niet waar: de grenzen en de tronen kon men herstellen, de ideeën niet. Liberalisme "
                "en nationalisme leefden verder en kwamen in 1830 en 1848 naar boven.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg van een bedoeling of een mislukking. Noem "
                   "telkens wat men wou bereiken en waarop het botste.",
            waarom=[
                "Noem het onderscheid tussen grenzen en ideeën. Dat is de kern: men kon de kaart "
                "herstellen maar niet wat de mensen ondertussen dachten.",
                "Noem dat een vernederd Frankrijk gevaarlijk was. Een land dat meebeslist, heeft "
                "belang bij het resultaat, en dat is precies de redenering die in 1919 niet gevolgd "
                "werd.",
                "Noem tegen wie de buffer diende en noem minstens twee verschillen tussen noord en "
                "zuid. Taal, godsdienst en economie liggen alle drie voor de hand.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-liberalisme-en-nationalisme-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: gaat de eis over vrijheid van de enkeling tegenover de "
                   "overheid, of over een volk dat een eigen staat wil. Het eerste is liberaal, het "
                   "tweede nationalistisch.",
            waarom=[
                None,
                None,
                "Let op dat het liberalisme van de negentiende eeuw ook economisch bedoeld was: zo "
                "weinig overheid mogelijk, ook in de fabriek. Juist daaruit groeide later de sociale "
                "kwestie.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Drie begrippen die bij een grondwet horen: wie mag stemmen, hoe de macht "
                   "verdeeld is, en wat de vorst nog mag.",
            waarom=[
                "Let op dat een constitutionele monarchie niet hetzelfde is als een democratie. De "
                "vorst is gebonden aan een grondwet, maar met het cijnskiesrecht stemde maar een "
                "kleine minderheid.",
            ],
        ),
        dict(
            aanpak="Twee golven om vast te zetten: 1830 en 1848. België hoort bij de eerste, "
                   "Frankfurt en de val van Louis-Philippe bij de tweede.",
            waarom=[
                "Let op dat 1848 een veel bredere golf was dan 1830: bijna heel Europa, van Parijs "
                "tot Wenen en Boedapest. En bijna overal werd ze binnen het jaar neergeslagen.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe ver het liberalisme ging, dat "
                   "nationalisme twee kanten heeft, en dat het later ook tegen andere volken "
                   "gebruikt werd.",
            waarom=[
                "Niet waar: het liberalisme van die tijd wilde stemrecht voor wie bezit en opleiding "
                "had, niet voor iedereen. Algemeen stemrecht was een eis van de arbeidersbeweging, "
                "veel later.",
                None,
                None,
                "Niet waar: in de eerste helft van de negentiende eeuw trokken ze juist vaak samen "
                "op tegen de orde van Wenen. Pas later groeiden ze uit elkaar.",
                "Waar: hetzelfde idee dat een volk recht heeft op een eigen staat, werd aan het eind "
                "van de eeuw gebruikt om andere volken te overheersen. Dat is de weg naar het "
                "imperialisme.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een verband en een uitleg. Noem bij 1848 zowel waarom "
                   "het mislukte als wat er bleef, want beide worden gevraagd.",
            waarom=[
                "Noem wat de burgerij had en wat ze miste: bezit en opleiding wel, politieke macht "
                "niet. En noem het cijnskiesrecht, want dat hield de arbeiders bewust buiten.",
                "Noem één voorbeeld van elk, zoals gevraagd. Italië en Duitsland voor het samenbrengen, "
                "Oostenrijk-Hongarije en het Ottomaanse Rijk voor het uiteenvallen.",
                "Noem de verdeeldheid van de revolutionairen én wat er toch bleef. Grondwetten en "
                "parlementen kwamen er in veel staten alsnog, maar jaren later.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-ontstaan-van-belgie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke klacht af wie er het meest door geraakt werd: de kerk, de "
                   "burgerij, of allebei. De taalpolitiek en de ondervertegenwoordiging stoorden "
                   "beide groepen.",
            waarom=[
                "Let op dat de taalkwestie bij allebei thuishoort: de katholieken omdat hun "
                "geestelijken en scholen eronder leden, de liberalen omdat de Franstalige elite het "
                "bestuur niet meer in kon. Juist zulke gedeelde grieven maakten het unionisme "
                "mogelijk.",
                None,
            ],
        ),
        dict(
            aanpak="Zet de vijf stappen op een tijdlijn van augustus 1830 tot augustus 1831. Het "
                   "hele verhaal van opstand tot bijna-nederlaag duurt één jaar.",
            waarom=[
                "Let op dat de Tiendaagse Veldtocht na de eedaflegging van Leopold I komt: "
                "Nederland viel binnen toen België al een koning had. Frankrijk moest België toen "
                "komen helpen.",
            ],
        ),
        dict(
            aanpak="Drie begrippen die bij de nieuwe staat horen: een bondgenootschap, een "
                   "vergadering en een belofte aan het buitenland.",
            waarom=[
                "Let op de neutraliteit: die was geen Belgische keuze maar een voorwaarde van de "
                "mogendheden. In 1914 was juist de schending van die neutraliteit de reden dat "
                "Groot-Brittannië in de oorlog stapte.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe liberaal de grondwet was, wie mocht "
                   "stemmen, en hoe de erkenning verliep. Vraag je bij elke af welk van de drie.",
            waarom=[
                None,
                "Niet waar: in 1831 gold het cijnskiesrecht, dus mocht ongeveer één procent van de "
                "bevolking stemmen. Een liberale grondwet en een smal stemrecht gingen samen.",
                None,
                "Niet waar: Nederland erkende België pas in 1839, dus negen jaar later. Tot dan was "
                "de toestand officieel onbeslist.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg met gevolgen op lange termijn. Noem telkens "
                   "wat de beslissing opleverde en voor wie.",
            waarom=[
                "Noem ook de voorwaarde, want die wordt uitdrukkelijk gevraagd. België paste in het "
                "evenwicht van Wenen, en de prijs was de neutraliteit.",
                "Noem dat ze verenigd waren door wat ze niet wilden. Zodra Willem I weg was, kwam "
                "het onderwijs als twistpunt boven, en daaruit groeiden de eerste partijen.",
                "Noem dat taal zo een sociale grens werd. Wie vooruit wou, had Frans nodig, en dat "
                "is de voedingsbodem van de Vlaamse beweging en van de latere taalwetten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-eerste-en-de-tweede-industriele-revolutie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: welke energiebron zit erachter. Steenkool en stoom horen bij "
                   "de eerste, elektriciteit en aardolie bij de tweede.",
            waarom=[
                None,
                None,
                "Let op de textiel: dat is de sector waar de eerste revolutie begon, met de "
                "spinmachine en de mechanische weefmachine. De chemie en de auto horen bij de "
                "tweede.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Leer elk begrip aan één beeld: thuis werken voor een opdrachtgever, de trek naar "
                   "de stad, geld dat in een bedrijf gaat, en één bedrijf dat alles beheerst.",
            waarom=[
                None,
                "Let op de naamloze vennootschap: door aandelen kon men geld van veel mensen "
                "samenbrengen, en net dat maakte heel grote fabrieken en spoorwegen mogelijk.",
            ],
        ),
        dict(
            aanpak="Vul de drie domeinen apart in: wat veranderde aan het werk, aan de groepen, en "
                   "aan de plaats waar men woonde. Zo zie je dat de revolutie meer was dan machines.",
            waarom=[
                "Let op de ruimtelijke kolom: de steden groeiden sneller dan men kon bouwen, "
                "vandaar de beluiken en de slechte hygiëne. Dat is de verbinding tussen de "
                "economische verandering en het sociale vraagstuk.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: waar de industrialisering in België begon, "
                   "wat het vervoer deed, en dat het tempo per land verschilde.",
            waarom=[
                None,
                "Niet waar: de industrialisering begon in Wallonië, bij de steenkool van Henegouwen "
                "en Luik. Vlaanderen bleef langer landelijk, met Gent als uitzondering.",
                None,
                "Niet waar: elk land had zijn eigen tempo. Groot-Brittannië eerst, dan België, later "
                "Duitsland en Frankrijk, en nog later Oost-Europa.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een oorzaak en twee uitleggen. Noem bij de eerste "
                   "meerdere factoren samen, want dat is wat het antwoord sterk maakt.",
            waarom=[
                "Noem er meerdere, niet één. Steenkool en ijzer bij elkaar, kapitaal uit de handel, "
                "een grote markt en goede vervoerswegen: pas samen verklaren ze de voorsprong.",
                "Noem wat er verdween: het eigen ritme, het werken bij je gezin en het hele "
                "ambacht. In de plaats kwamen de klok, het toezicht en de opgesplitste taak.",
                "Noem het verschil in herkomst van de vernieuwing. De eerste golf kwam van "
                "praktische uitvinders, de tweede uit wetenschappelijk onderzoek en bedrijfslabo's.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ongelijkheden-klassenmaatschappij-en-sociale-strijd-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de begrippen in twee groepen: wat het probleem benoemt, en wat de arbeiders "
                   "ertegen opzetten. Staking en vakbond horen bij het tweede.",
            waarom=[
                None,
                "Let op het verschil tussen een mutualiteit en een cooperatie: de eerste keert geld "
                "uit bij ziekte, de tweede laat je goedkoper kopen. Allebei bestonden ze lang voor "
                "er sociale wetten waren.",
            ],
        ),
        dict(
            aanpak="Drie klassen, drie bronnen van inkomen: winst uit bezit, een loon voor "
                   "handenarbeid, en een wedde of een eigen zaak in het midden.",
            waarom=[
                "Let op de middenklasse: onderwijzers, bedienden en winkeliers hoorden bij geen van "
                "de twee uitersten. Juist die groep groeide sterk in de negentiende eeuw.",
            ],
        ),
        dict(
            aanpak="Vier maatregelen op een tijdlijn van 1886 tot 1921. Let erop dat de enquête "
                   "vooraf gaat aan de wetten: eerst onderzoek, dan wetgeving.",
            waarom=[
                "Let op hoe laat die data zijn: het verbod op kinderarbeid onder twaalf kwam in "
                "1889, bijna zestig jaar na de onafhankelijkheid. En de achturendag kwam er pas na "
                "de Eerste Wereldoorlog.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat gelijkheid voor de wet betekent, hoe de "
                   "eerste sociale wetten tot stand kwamen, en wat toegelaten was.",
            waarom=[
                "Waar, en let op het verschil met de praktijk: alle burgers waren gelijk voor de "
                "wet, maar wie geen bezit had, mocht niet stemmen en kon zijn recht moeilijk halen. "
                "Gelijkheid op papier is niet hetzelfde als gelijkheid in de praktijk.",
                None,
                "Niet waar: kinderarbeid was lang gewoon toegelaten en zelfs nodig voor het "
                "gezinsinkomen. Het verbod kwam er pas in 1889, en dan nog enkel onder de twaalf "
                "jaar.",
                None,
                "Niet waar: staken was lange tijd strafbaar, want het viel onder het verbod op "
                "samenspanning. Dat verbod werd pas in 1866 opgeheven, en ook daarna werd staken "
                "nog vaak vervolgd.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een verband, een opsomming en een bronkritiek. Zeg bij "
                   "een uitspraak van een tijdgenoot altijd welk belang erachter zit.",
            waarom=[
                "Noem het mechanisme: wie stemt, wordt vertegenwoordigd, en wie vertegenwoordigd "
                "wordt, krijgt wetten. Zonder stemrecht bleven de arbeiders afhankelijk van de "
                "goodwill van anderen.",
                "Noem er twee met hun doel, zoals gevraagd. De mutualiteit tegen het risico van "
                "ziekte, de cooperatie tegen de hoge prijzen.",
                "Noem dat het een standpunt is met een belang erachter, en zeg waarvoor de bron dan "
                "wél dient. Over de arbeiders zegt ze niets, over het denken van de fabrikanten "
                "veel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-marxisme-sociaaldemocratie-christendemocratie-en-migratie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie stromingen verschillen in de weg, niet in de vaststelling. Vraag je af "
                   "of de uitspraak revolutie, parlement of overleg voorstelt.",
            waarom=[
                None,
                "Let op dat marxisme en sociaaldemocratie dezelfde wortel hebben: het doel lag "
                "dicht bij elkaar, de weg niet. De christendemocratie wou geen klassenstrijd maar "
                "samenwerking tussen de klassen.",
            ],
        ),
        dict(
            aanpak="Drie begrippen van drie kanten: het marxistische, het christelijke en het "
                   "maatschappelijke. Leer bij Rerum Novarum het jaartal 1891.",
            waarom=[
                "Let op uitbuiting: bij Marx is dat geen scheldwoord maar een begrip, namelijk de "
                "meerwaarde die de eigenaar uit het werk haalt. Daarmee verklaarde hij waar de winst "
                "vandaan komt.",
            ],
        ),
        dict(
            aanpak="Migratie naar België kwam in golven: eerst binnen het land, dan uit Italië, dan "
                   "uit Marokko en Turkije. Zet de drie in die orde.",
            waarom=[
                "Let op de eerste golf: die was binnenlands. Vlamingen trokken in de negentiende eeuw "
                "naar de Waalse industrie, en die beweging wordt vaak vergeten in het verhaal over "
                "migratie.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wie wat schreef, wat de christendemocratie "
                   "wilde, en wanneer de migratie begon. Vraag je bij elke af welk van de drie.",
            waarom=[
                None,
                "Niet waar: de christendemocratie wou juist overleg tussen de klassen in plaats van "
                "strijd. Dat staat ook in Rerum Novarum: privébezit blijft, maar met een "
                "rechtvaardig loon.",
                None,
                "Niet waar: er was al veel eerder migratie, binnen België en uit het buitenland. De "
                "akkoorden van na 1945 zijn een nieuwe fase en geen begin.",
                "Waar: na de ramp in Marcinelle, waar 262 mijnwerkers omkwamen, van wie de meeste "
                "Italianen, stopte Italië met het sturen van werkkrachten. Daarna sloot België "
                "akkoorden met andere landen.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een verband, een oorzaak met gevolgen, en een kritiek op "
                   "een woord. Noem telkens wat de mensen zelf meemaakten.",
            waarom=[
                "Noem dat ze dezelfde vaststelling deelden en in de oplossing verschilden. Juist dat "
                "maakt ze drie antwoorden op één vraag.",
                "Noem beide kanten, zoals gevraagd: waarom België hen nodig had, en wat het voor hen "
                "betekende. Het zware werk, de barakken en het blijven horen er alle drie bij.",
                "Noem dat het woord een verwachting uitdrukt en geen werkelijkheid. De mensen "
                "bleven, haalden hun gezin over en bouwden hier hun leven op.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-modern-imperialisme-en-de-wedloop-om-afrika-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie soorten motieven: geld, macht en een idee over de eigen superioriteit. "
                   "Vraag je af wat men ermee wou winnen.",
            waarom=[
                None,
                "Let op de kolenstations: die dienden de vloot en dus de macht, niet de handel "
                "rechtstreeks. En een beroep op de wetenschap om de eigen superioriteit te bewijzen "
                "is ideologisch, hoe wetenschappelijk het ook klonk.",
            ],
        ),
        dict(
            aanpak="Let op het verschil tussen een kolonie en een protectoraat: in het eerste geval "
                   "bestuurt de mogendheid zelf, in het tweede blijft er een eigen vorst onder "
                   "toezicht.",
            waarom=[
                "Let op de Conferentie van Berlijn van 1884 en 1885: daar werden de spelregels van "
                "de wedloop afgesproken, onder meer dat je een gebied werkelijk moest bezetten om er "
                "aanspraak op te maken.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wie in Berlijn aan tafel zat, hoever de "
                   "verdeling ging, en wat de grenzen volgen. Vraag je bij elke af welk van de drie.",
            waarom=[
                "Waar, en dat is het kernpunt: over Afrika werd beslist zonder Afrikanen. Zo'n "
                "conferentie is zelf al een bron over de verhoudingen van die tijd.",
                None,
                "Niet waar: Ethiopië bleef onafhankelijk en versloeg Italië in 1896 bij Adwa. Pas in "
                "1936 werd het bezet, en dan maar voor enkele jaren. Liberia bleef ook buiten de "
                "verdeling.",
                "Niet waar: de grenzen werden met de lat getrokken, zonder rekening te houden met "
                "volkeren of talen. Juist daarom lopen ze zo vaak kaarsrecht.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je bij zo'n bron eerst af waarover ze wél iets zegt. Een "
                   "rechtvaardigingstekst is een goede bron over de denkwijze en een slechte over de "
                   "feiten.",
            waarom=[
                "Noem beide kanten, zoals gevraagd: over de schrijver en zijn tijd zegt de zin veel, "
                "over de Afrikaanse samenlevingen niets betrouwbaars.",
                "Noem wat de uitdrukking wegstopt: de economische en politieke drijfveren, en het "
                "geweld en de dwangarbeid. Een mooie naam voor een harde praktijk.",
            ],
        ),
        dict(
            aanpak="Deze vraag vraagt een gevolg op lange termijn. Noem het mechanisme en niet enkel "
                   "het eindpunt.",
            waarom=[
                "Noem beide gevolgen van die lijnen: één volk verdeeld over twee staten, en "
                "volkeren die niets met elkaar hadden in één staat. Dat de nieuwe staten die "
                "grenzen behielden, hoort erbij.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-congo-van-congo-vrijstaat-tot-belgisch-congo-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het verschil zit in de eigenaar: tot 1908 was Congo het persoonlijke bezit van "
                   "Leopold II, daarna een kolonie van de Belgische staat.",
            waarom=[
                None,
                None,
                "Let op de rubberquota: die horen bij de Vrijstaat. Het geweld dat ermee gepaard "
                "ging, bracht de internationale druk op gang die tot de overdracht van 1908 leidde.",
                "Let op de drie-eenheid: staat, kerk en grote bedrijven. Elk had zijn terrein, "
                "onderwijs en zorg bij de kerk, en samen regelden ze het dagelijks leven.",
            ],
        ),
        dict(
            aanpak="Drie begrippen om vast te zetten: het leger, de bestuursvorm en de manier van "
                   "besturen via plaatselijke hoofden.",
            waarom=[
                "Let op indirect bestuur: men regeerde via bestaande hoofden, en zette er hoofden af "
                "die niet meewerkten. Dat lijkt zacht maar maakte de controle juist diepgaander.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat Leopold II zelf deed, hoe de overdracht "
                   "kwam, en wat Congolezen wel en niet mochten. Vraag je bij elke af welk van de "
                   "drie.",
            waarom=[
                "Waar, en dat is opmerkelijk: hij bestuurde het gebied vijfentwintig jaar lang "
                "zonder er ooit een voet te zetten. Alles liep via rapporten en vertrouwelingen.",
                None,
                "Niet waar: hoger onderwijs voor Congolezen kwam er pas heel laat, in de jaren "
                "vijftig. Daarom waren er in 1960 nauwelijks Congolese universitair geschoolden.",
                None,
                "Niet waar: Congolezen hadden geen stemrecht voor het Belgische parlement en geen "
                "eigen parlement. Ze werden bestuurd zonder vertegenwoordiging.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke bron af wie ze maakte en met welk doel. Ook een bron met een "
                   "duidelijk belang kan heel bruikbaar zijn, maar voor een andere vraag.",
            waarom=[
                "Noem beide delen, zoals gevraagd. Over Congo zegt het schoolboek weinig, over het "
                "Belgische onderwijs van 1950 veel.",
                "Noem beide kanten: waarom de bron waardevol is en waarom je ze toch kritisch leest. "
                "Zonder die verslagen wisten we veel minder, en toch had elke schrijver zijn eigen "
                "doel.",
            ],
        ),
        dict(
            aanpak="Deze vraag vraagt een gevolg. Noem het verschil tussen lager en hoger onderwijs, "
                   "want daar zit de kern.",
            waarom=[
                "Noem dat er veel lager en bijna geen hoger onderwijs was. Een nieuwe staat zonder "
                "eigen artsen, ingenieurs en hoge ambtenaren start met een handicap, en die blijft "
                "jaren meespelen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-eerste-wereldoorlog-en-de-vrede-van-versailles-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een aanleiding is de vonk, een oorzaak is het kruit dat er al lag. Vraag je af "
                   "of iets jaren of dagen voor de oorlog speelde.",
            waarom=[
                "Let op dat de moord in Sarajevo de aanleiding is. Zonder de wapenwedloop, de "
                "bondgenootschappen en de spanningen op de Balkan was het bij een misdaad gebleven.",
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over de oorlog zelf en drie over de vrede "
                   "erna. Leer bij de Volkenbond het jaar 1920.",
            waarom=[
                "Let op het verschil tussen een totale oorlog en een loopgravenoorlog: het eerste "
                "gaat over wie er allemaal bij betrokken is, het tweede over de manier van vechten.",
                "Let op het schuldartikel: dat was het artikel dat in Duitsland het hardst "
                "aangevoeld werd, nog meer dan de herstelbetalingen. Daaruit groeide het woord "
                "dictaat van Versailles.",
            ],
        ),
        dict(
            aanpak="Versailles legde Duitsland vier dingen op: gebied, leger, geld en schuld. Leer ze "
                   "als vier vakjes, dan vergeet je er geen.",
            waarom=[
                "Let op dat Duitsland ook al zijn koloniën kwijtraakte, niet alleen gebied in "
                "Europa. Die koloniën werden onder de overwinnaars verdeeld als mandaatgebieden van "
                "de Volkenbond.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de inval in België, hoelang men dacht dat "
                   "de oorlog zou duren, en hoe de vrede tot stand kwam.",
            waarom=[
                None,
                "Waar, en juist die neutraliteit maakt de inval zo belangrijk: de schending was voor "
                "Groot-Brittannië de reden om in de oorlog te stappen.",
                "Niet waar: iedereen rekende op een korte oorlog, en het werd er een van meer dan "
                "vier jaar. Die verkeerde verwachting verklaart mee waarom men zo makkelijk begon.",
                "Niet waar: Duitsland mocht niet meeonderhandelen en kreeg de tekst voorgelegd. "
                "Vergelijk met het Congres van Wenen, waar het verslagen Frankrijk wel aan tafel "
                "zat.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg en een gevolg. Noem bij de totale oorlog "
                   "meerdere terreinen, en bij Versailles het mechanisme van de wrok.",
            waarom=[
                "Noem meerdere terreinen samen: de fabrieken, de vrouwen die het werk overnamen, de "
                "rantsoenering, de propaganda en de burgers als doelwit. Eén voorbeeld maakt het "
                "antwoord te smal.",
                "Noem de combinatie die het gevaarlijk maakte: vernederd en met de rekening, maar "
                "nog groot en sterk genoeg om zich te verzetten.",
                "Noem ook dat het stemrecht er pas veel later kwam. De oorlog veranderde vooral het "
                "argument, niet onmiddellijk de wet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-interbellum-de-opkomst-van-het-totalitarisme-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie regimes, drie kernwoorden: de mars op Rome bij Italië, de rassenleer bij "
                   "Duitsland, de vijfjarenplannen bij de Sovjet-Unie.",
            waarom=[
                "Let op dat de drie regimes veel gemeen hadden, zoals één partij en één leider, en "
                "toch elk hun eigen kern. Juist die kern vraagt deze reeks.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over hoe zo'n staat werkt, en drie over de "
                   "gebeurtenissen die hem mogelijk maakten.",
            waarom=[
                "Let op censuur: die gaat niet enkel over verbieden maar over vooraf controleren wat "
                "mag verschijnen. Dat verschil met achteraf straffen is wezenlijk.",
                "Let op de inflatie van 1923: die vaagde het spaargeld van de middenklasse weg, en "
                "dat was nog voor de crisis van 1929. Twee keer in tien jaar zijn spaargeld "
                "verliezen verklaart veel over het vertrouwen in de republiek.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe Hitler aan de macht kwam, wat de crisis "
                   "deed, en hoe zwak de Volkenbond was.",
            waarom=[
                "Waar, en dat is ongemakkelijk om vast te stellen: hij werd kanselier via de "
                "grondwet, na verkiezingen. De dictatuur kwam erna, met de noodmaatregelen en de "
                "Machtigingswet.",
                None,
                None,
                "Niet waar: de Volkenbond kon de aanval van Italië op Ethiopië en die van Japan op "
                "Mantsjoerije niet tegenhouden. Zonder leger bleef het bij sancties op papier.",
                "Waar: ook hier groeiden partijen als Rex en het VNV. Autoritaire antwoorden op de "
                "crisis waren geen Duits of Italiaans verschijnsel alleen.",
            ],
        ),
        dict(
            aanpak="Vraag je bij propaganda altijd af waarover ze wél iets zegt. Ze toont wat het "
                   "regime wilde laten zien, en dat is een echte historische vraag.",
            waarom=[
                "Noem er drie, zoals gevraagd, en noem ook de nieuwe media. Radio en film maakten "
                "het bereik van propaganda in de jaren dertig veel groter dan ooit tevoren.",
                "Noem beide kanten: waarvoor de poster een goede bron is en waarvoor niet. Dat is de "
                "kern van bronkritiek bij beeldmateriaal.",
            ],
        ),
        dict(
            aanpak="Deze vraag vraagt twee oorzaken samen. Zeg wat elk van de twee leverde, en dat "
                   "ze alleen samen genoeg verklaren.",
            waarom=[
                "Noem beide bijdragen apart: Versailles leverde de wrok, de crisis de werkloosheid "
                "en de angst. En noem dat de nazi's een vijand aanwezen; dat hoort bij hun "
                "doorbraak.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-tweede-wereldoorlog-en-de-holocaust-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de zes stappen op een tijdlijn van september 1939 tot mei 1945. Let erop dat "
                   "1941 het jaar is waarin de oorlog echt wereldwijd wordt.",
            waarom=[
                "Let op 1941: eerst de inval in de Sovjet-Unie in juni, dan Pearl Harbor in "
                "december. Vanaf dan staan de Sovjet-Unie en de Verenigde Staten erin, en dat "
                "beslist de oorlog.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over de oorlog en de vervolging, drie over "
                   "België en de nasleep.",
            waarom=[
                "Let op de blitzkrieg: tanks, vliegtuigen en snelheid samen, juist het tegendeel van "
                "de loopgraven van 14-18. Dat verklaart waarom België in achttien dagen verslagen "
                "was.",
                "Let op de repressie: dat is de afrekening na de oorlog, niet de onderdrukking "
                "tijdens de bezetting. Die dubbele betekenis van het woord leidt vaak tot "
                "verwarring.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat er in België gebeurde, hoe de "
                   "vervolging georganiseerd was, en wat er na de oorlog volgde.",
            waarom=[
                None,
                None,
                "Niet waar: de vervolging steunde op administratie, registers, treinen en "
                "ambtenaren. Juist die organisatie maakte haar op zo'n schaal mogelijk, en dat is "
                "ook wat de redeneerwijze over menselijke actoren bedoelt.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Vraag je bij elke bron af voor welke vraag ze de beste is. Een gecensureerde "
                   "krant en een late getuigenis zijn elk sterk op hun eigen punt.",
            waarom=[
                "Noem beide kanten: voor de feiten onbetrouwbaar, voor de taal en de bedoeling van "
                "de bezetter juist de beste bron die er is.",
                "Noem het onderscheid tussen data en beleving. Voor aantallen neem je de "
                "administratie, voor wat mensen meemaakten de getuigenissen; samen geven ze het "
                "volledige beeld.",
            ],
        ),
        dict(
            aanpak="Deze vraag vraagt het verschil tussen een feit en een mening. Noem de bronnen die "
                   "het feit vaststellen.",
            waarom=[
                "Noem de soorten bronnen: de eigen administratie van de daders, de getuigenissen, de "
                "kampen en de processen. En noem dat ontkennen in België bij wet strafbaar is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-china-van-keizerrijk-tot-wereldmacht-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf stappen over bijna honderdvijftig jaar: van de Opiumoorlogen tot de "
                   "hervormingen van 1978. Leer bij elk één jaartal.",
            waarom=[
                "Let op hoe dicht 1966 en 1978 op elkaar liggen: nauwelijks twaalf jaar tussen de "
                "Culturele Revolutie en het begin van de markthervormingen. Zo'n bocht in één "
                "mensenleven is uitzonderlijk.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over de tijd van de vernedering en van Mao, "
                   "drie over de hervormingen daarna.",
            waarom=[
                "Let op de Grote Sprong Voorwaarts en de Culturele Revolutie: de eerste was "
                "economisch bedoeld en liep uit op hongersnood, de tweede was een politieke "
                "campagne tegen het oude en tegen critici.",
                "Let op de speciale economische zones: daar gold de markt voordat ze in het hele "
                "land gold. Shenzhen groeide zo van een dorp tot een miljoenenstad.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe China overheerst werd, wat de "
                   "hervormingen wel en niet brachten, en waar het land vandaag staat.",
            waarom=[
                "Waar: China bleef formeel een keizerrijk met eigen regering, maar moest havens, "
                "gebieden en rechtspraak afstaan. Dat heet informeel imperialisme, en het verschilt "
                "van wat in Congo gebeurde.",
                None,
                "Niet waar: Deng hervormde de economie en niet het politieke stelsel. Dat verschil "
                "is precies waarom men van een economische revolutie zonder politieke revolutie "
                "spreekt.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Vergelijk de twee periodes op dezelfde twee punten: hoe de economie geregeld is, "
                   "en hoe het land tegenover het buitenland staat.",
            waarom=[
                "Let op de tweede rij: het land ging economisch open maar politiek niet. Juist die "
                "combinatie is wat China onderscheidt van de hervormingen in Oost-Europa.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een uitleg van een uitdrukking. Zeg telkens wat er "
                   "feitelijk gebeurde en waarom men die woorden gebruikt.",
            waarom=[
                "Noem concrete gevolgen van de verdragen: havens openen, gebied afstaan, eigen "
                "rechtspraak voor buitenlanders. En noem dat die vernedering tot vandaag in het "
                "Chinese zelfbeeld doorwerkt.",
                "Noem beide kanten, zoals de uitdrukking zelf doet. Economisch veranderde bijna "
                "alles, politiek bleef één partij alle macht houden.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-een-nieuwe-wereldorde-de-verenigde-naties-en-de-koude-oorlog-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee blokken, en bij elk een militair en een economisch verband. De NATO en het "
                   "Warschaupact zijn de legers, het Marshallplan en de Comecon het geld.",
            waarom=[
                None,
                None,
                "Let op het Marshallplan: dat was Amerikaans geld voor de heropbouw van "
                "West-Europa. België kreeg er ook uit, en de Sovjet-Unie verbood haar landen om "
                "mee te doen.",
                "Let op de Comecon: dat was het antwoord van het oosten op het Marshallplan, een "
                "eigen economische samenwerking tussen de communistische landen.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over hoe de twee blokken elkaar in het oog "
                   "hielden, en drie over de Verenigde Naties en de ontspanning.",
            waarom=[
                "Let op de afschrikking: het idee is dat juist de zekerheid van de eigen "
                "vernietiging een aanval tegenhoudt. Dat klinkt tegenstrijdig en het is precies "
                "waarom het nooit tot een rechtstreekse oorlog kwam.",
                "Let op het vetorecht: het ligt bij de vijf vaste leden van de Veiligheidsraad. Dat "
                "waren de overwinnaars van de Tweede Wereldoorlog, en dat is het nog altijd.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe de VN ontstonden, hoe de twee "
                   "supermachten elkaar bestreden, en hoe het eindigde.",
            waarom=[
                None,
                "Waar, en let op het jaartal: 1948, drie jaar na de oorlog en in de schaduw van wat "
                "er gebeurd was. De verklaring is een antwoord op die oorlog.",
                "Waar: ze streden in Korea, Vietnam, Afghanistan en elders, maar nooit leger tegen "
                "leger. Dat is wat een proxyoorlog is.",
                "Niet waar: elk vast lid kan alleen een beslissing tegenhouden. Juist dat verklaart "
                "waarom de Veiligheidsraad in de Koude Oorlog zo vaak verlamd stond.",
                None,
            ],
        ),
        dict(
            aanpak="Drie crisissen, elk met een eigen plaats op de kaart. Leer bij elk waar het was: "
                   "Berlijn, Cuba, Vietnam.",
            waarom=[
                "Let op de Cubacrisis: raketten op negentig mijl van Florida. Dat was het moment "
                "waarop de wereld het dichtst bij een kernoorlog stond, en daarna kwam de rode "
                "telefoon tussen Washington en Moskou.",
            ],
        ),
        dict(
            aanpak="De eerste vraag vraagt een uitleg van een naam, de tweede vraagt twee kanten van "
                   "dezelfde regel. Antwoord bij de tweede met een voordeel en een nadeel, zoals "
                   "gevraagd.",
            waarom=[
                "Noem de middelen waarmee ze wel streden, en noem de kernwapens als de reden dat "
                "het koud bleef. Zonder die reden is het antwoord niet volledig.",
                "Let op dat beide kanten waar zijn tegelijk. Het veto hield de grote landen binnen "
                "de organisatie en verlamt haar als een van die landen zelf partij is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-europese-eenmaking-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf stappen over vijftig jaar. Een handig anker: de EGKS begint zeven jaar na "
                   "de oorlog, de euro komt vijftig jaar later in je hand.",
            waarom=[
                "Let op het verschil tussen Maastricht in 1992 en de euro in 2002: het verdrag "
                "besliste de munt, de biljetten kwamen tien jaar later. Een afspraak en de "
                "uitvoering ervan liggen vaak jaren uit elkaar.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over de markt en de grenzen, drie over de "
                   "instellingen en hoe ze beslissen.",
            waarom=[
                "Let op het verschil tussen een douane-unie en de interne markt: de eerste gaat "
                "enkel over invoerrechten op goederen, de tweede ook over personen, diensten en "
                "kapitaal. De interne markt is dus veel ruimer.",
                "Let op de Europese Commissie en het Parlement: de Commissie stelt voor, het "
                "Parlement en de lidstaten beslissen. Enkel het Parlement kies jij zelf.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe het begon, wie meedoet, en hoe de "
                   "instellingen samengesteld zijn.",
            waarom=[
                "Waar: België, Nederland, Luxemburg, Frankrijk, Italië en West-Duitsland. De "
                "Benelux was er dus van het begin bij, en Brussel werd niet toevallig de "
                "hoofdstad van de instellingen.",
                None,
                "Niet waar: niet alle lidstaten gebruiken de euro. Denemarken, Zweden en Polen "
                "bijvoorbeeld hebben hun eigen munt gehouden.",
                None,
                "Niet waar: het Europees Parlement wordt rechtstreeks verkozen, sinds 1979, en jij "
                "mag daar vanaf achttien jaar zelf voor gaan stemmen.",
            ],
        ),
        dict(
            aanpak="Drie open vragen: een oorzaak, twee voorbeelden uit je eigen leven, en een "
                   "standpunt dat je moet uitleggen zonder het te moeten verdedigen.",
            waarom=[
                "Noem dat kolen en staal de grondstoffen van de wapenindustrie waren. Daar zit de "
                "hele gedachte in: wie samen de wapenfabriek beheert, kan niet in het geheim "
                "herbewapenen.",
                "Noem bij elk voorbeeld ook waardoor het kan, zoals gevraagd. Reizen zonder "
                "controle hoort bij Schengen, met dezelfde munt betalen bij de euro; dat is niet "
                "hetzelfde verdrag.",
                "Let erop dat een standpunt verklaren niet hetzelfde is als het delen. Zeg wat de "
                "critici bedoelen, en zeg ook wat de voorstanders ertegenover zetten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-dekolonisatie-van-congo-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf stappen in nauwelijks zes jaar. Let erop hoe snel het ging: anderhalf jaar "
                   "tussen de rellen en de onafhankelijkheid, en nog een half jaar tot de "
                   "afscheiding.",
            waarom=[
                "Let op dat de afscheiding van Katanga er amper twee weken na de onafhankelijkheid "
                "al was. Die snelheid zegt veel over hoe weinig de nieuwe staat voorbereid was.",
            ],
        ),
        dict(
            aanpak="Zes keer een begrip of een naam. De eerste rij gaat over wat er met de staat "
                   "gebeurde, de tweede over wie en wat erbij betrokken was.",
            waarom=[
                None,
                "Let op het neokolonialisme: de vlag verandert, de mijnen en de winsten blijven in "
                "buitenlandse handen. Dat begrip verklaart waarom men zegt dat Congo politiek "
                "onafhankelijk werd en economisch niet.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de datum en de voorbereiding, het belang "
                   "van Katanga, en wat België later zelf onderzocht.",
            waarom=[
                None,
                "Niet waar: de Belgische plannen spraken nog in 1955 over dertig jaar, en in "
                "januari 1960 werd op de rondetafelconferentie beslist dat het binnen zes maanden "
                "zou gebeuren. Die haast is een van de kernen van dit hoofdstuk.",
                None,
                "Niet waar: er waren maar een handvol Congolese universitair gediplomeerden, en "
                "geen enkele Congolese officier in het leger. Het hoger onderwijs was pas in de "
                "jaren vijftig opengegaan.",
                "Waar: die commissie werkte rond 2000 en besloot dat Belgische "
                "verantwoordelijken een morele verantwoordelijkheid droegen. Een land dat zijn "
                "eigen verleden onderzoekt is zelf ook een historisch feit.",
            ],
        ),
        dict(
            aanpak="Twee bronnen, en bij elk dezelfde vraag: wie schreef of sprak, voor wie, en wat "
                   "zie je daardoor wel en niet.",
            waarom=[
                "Noem dat het de Congolese stem zelf is, op het moment van de overdracht. Dat is "
                "wat deze bron uitzonderlijk maakt, want de meeste bronnen over Congo komen van "
                "Belgische hand.",
                "Noem zowel de context van de krant als wat ze weglaat. Een woord als chaos "
                "beschrijft niet enkel de toestand, het geeft er ook een schuld aan.",
            ],
        ),
        dict(
            aanpak="Deze vraag vraagt meerdere oorzaken samen. Noem er vier of vijf en zeg bij elk "
                   "kort wat het deed.",
            waarom=[
                "Noem zeker de korte voorbereiding, het gebrek aan opgeleide Congolezen, de "
                "muiterij in het leger, Katanga en de mijnbelangen. En noem de Koude Oorlog: "
                "beide supermachten zagen in Congo een kans, en dat maakte het conflict nog "
                "zwaarder.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-belgie-na-1945-breuklijnen-federale-staat-en-emancipatie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie breuklijnen, en bij elk conflict één vraag: gaat het over geloof en "
                   "onderwijs, over geld en werk, of over taal en gebied?",
            waarom=[
                "Let op de staking tegen de Eenheidswet van 1960 en 1961: die was "
                "sociaaleconomisch, maar liep in Wallonië veel heviger dan in Vlaanderen. Twee "
                "breuklijnen kunnen dus door elkaar lopen.",
                "Let op de Koningskwestie: de tegenstelling liep vooral tussen katholieken en "
                "vrijzinnigen, dus filosofisch, maar ook Vlaanderen en Wallonië stemden er heel "
                "verschillend over. Dat maakt ze een schoolvoorbeeld van hoe de lijnen kruisen.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in twee groepen: drie over hoe de samenleving zich organiseerde, "
                   "drie over de staat en de rechten.",
            waarom=[
                "Let op het sociaal pact van 1944: dat werd nog tijdens de oorlog voorbereid, in "
                "het geheim, tussen vakbonden en werkgevers. Daaruit groeide de sociale zekerheid "
                "zoals we die vandaag kennen.",
                "Let op het verschil tussen de gewesten en de gemeenschappen: samen zijn ze de "
                "deelstaten, maar ze zijn niet hetzelfde. De volgende reeks gaat daar verder op in.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de rechten die erbij kwamen, de taalgrens "
                   "en de staatshervormingen, en de economische omslag.",
            waarom=[
                "Waar, en let op het jaartal: 1948, dertig jaar na het algemeen enkelvoudig "
                "stemrecht voor mannen. Vrouwen mochten gemeentelijk al eerder stemmen, nationaal "
                "pas vanaf dan.",
                None,
                "Niet waar: de zuilen liepen juist langs de breuklijnen. Elke strekking had haar "
                "eigen scholen, ziekenfonds, vakbond en jeugdbeweging, en zo werd de verdeeldheid "
                "een deel van het dagelijks leven.",
                "Niet waar: er waren verschillende staatshervormingen, vanaf 1970, en de grondwet "
                "noemde België pas in 1993 een federale staat. Elke ronde was een compromis dat "
                "een volgende ronde opriep.",
                "Waar: Zwartberg sloot in 1966 met zwaar protest, en de laatste Limburgse mijn in "
                "1992. Duizenden gezinnen moesten ander werk zoeken.",
            ],
        ),
        dict(
            aanpak="Eén woord helpt je hier door de hele tabel: gewesten gaan over grond, "
                   "gemeenschappen over mensen.",
            waarom=[
                "Let op onderwijs en cultuur: die horen bij de gemeenschappen, niet bij de "
                "gewesten. Daarom beslist de Vlaamse Gemeenschap over jouw school, ook als je in "
                "Brussel woont.",
            ],
        ),
        dict(
            aanpak="Twee open vragen: de eerste vraagt de drie lijnen samen, de tweede vraagt "
                   "waarom het stap voor stap ging. Verbind in je antwoord telkens een lijn met een "
                   "concreet conflict.",
            waarom=[
                "Noem bij elke lijn minstens één conflict, zoals in de eerste reeks. En noem dat de "
                "lijnen door elkaar liepen; juist daarom waren er altijd coalities nodig.",
                "Noem dat een compromis telkens maar een deel oploste. Dat is de reden dat er "
                "verschillende hervormingen kwamen en dat de discussie vandaag niet gesloten is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kunst-en-cultuur-een-kunstwerk-analyseren-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes stromingen, elk met één kernwoord: gevoel, de werkelijkheid, het licht, de "
                   "oudheid, de vorm, de droom.",
            waarom=[
                "Let op het verschil tussen het realisme en het impressionisme: het realisme kiest "
                "een ander onderwerp, namelijk het gewone en het arme leven; het impressionisme "
                "kiest een andere manier van kijken, namelijk het licht van dat ene moment.",
                "Let op het classicisme en de romantiek: die staan tegenover elkaar. Het eerste "
                "zoekt de strakke vorm en de rede, het tweede het gevoel en de verbeelding.",
            ],
        ),
        dict(
            aanpak="Eén proef voor de hele reeks: kan iemand anders het op het werk nagaan? Dan is "
                   "het een beschrijving. Zodra er een bedoeling of een gevoel in zit, is het een "
                   "interpretatie.",
            waarom=[
                None,
                "Let op het woord wil: zodra je over de bedoeling van de schilder spreekt, leid je "
                "iets af. Dat kan een goede interpretatie zijn, maar het blijft een interpretatie.",
                None,
                "Let op troosteloos: de bleke kleuren kan je zien, troosteloos is wat jij eraan "
                "toevoegt. Het eerste deel van de zin is beschrijving, het tweede niet.",
            ],
        ),
        dict(
            aanpak="De vier stappen gaan van buiten naar binnen: eerst waar en wanneer, dan wat je "
                   "ziet, dan hoe het gemaakt is, en pas daarna wat het betekent.",
            waarom=[
                "Let erop dat interpreteren de laatste stap is en niet de eerste. Wie meteen "
                "begint bij wat hij voelt, kijkt daarna enkel nog naar wat zijn gevoel bevestigt.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: kunst als bron, de rol van de "
                   "opdrachtgever, en wat een werk over zijn tijd zegt.",
            waarom=[
                None,
                "Niet waar: je begint bij situeren en beschrijven. Je eigen gevoel mag er zijn, "
                "maar het komt na het kijken, niet ervoor.",
                "Waar: wie betaalde, bepaalde vaak het onderwerp, het formaat en zelfs wie er in "
                "beeld kwam. Daarom is de opdrachtgever een vraag die je bij elk werk stelt.",
                None,
                "Niet waar: ook een abstract werk is in een bepaalde tijd gemaakt en zegt iets over "
                "de vragen van die tijd. Cobra ontstond kort na de Tweede Wereldoorlog, en dat is "
                "aan die kunst te zien.",
            ],
        ),
        dict(
            aanpak="Drie open vragen: een methodevraag, een werk dat je moet lezen, en een vraag "
                   "over kunst en samenleving. Verbind bij de laatste twee altijd met de tijd.",
            waarom=[
                "Noem dat een beschrijving controleerbaar is en een interpretatie afgeleid. Dat "
                "onderscheid is dezelfde proef als in de tweede reeks.",
                "Noem wat de fabriek op de achtergrond doet: ze zegt waaraan hij zijn aanzien "
                "ontleent. Dat is precies hoe de negentiende-eeuwse burgerij zich wilde laten zien.",
                "Noem één voorbeeld van een stroming als antwoord op de vorige, zoals de romantiek "
                "op de verlichting. Met een voorbeeld is dit antwoord veel sterker.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-redeneren-met-bronnen-bruikbaarheid-en-betrouwbaarheid-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag voor de hele reeks: komt het uit de tijd zelf, of is het later over "
                   "die tijd geschreven? Het eerste is primair, het tweede secundair.",
            waarom=[
                None,
                None,
                None,
                "Let op je handboek: het is secundair, want het is vandaag geschreven over een ver "
                "verleden. De bronnen die erin afgedrukt staan, zijn wel primair.",
                "Let erop dat een voorwerp ook een bron is. Een werktuig komt uit de tijd zelf, dus "
                "het is primair, net als een brief.",
            ],
        ),
        dict(
            aanpak="Vier soorten: tekst, voorwerp, beeld en gesproken woord. Vraag je af in welke "
                   "vorm de bron tot bij jou komt.",
            waarom=[
                None,
                "Let op de affiche in de volgende rij en de foto hier: beide zijn beeldbronnen, ook "
                "al staat er tekst op een affiche. De vorm waarin ze werkt, is het beeld.",
            ],
        ),
        dict(
            aanpak="Hou de onderzoeksvraag naast elke bron: Limburg, mijnwerkersgezinnen, wonen, "
                   "rond 1950. Een bron die op één van die vier naast de kwestie valt, is niet "
                   "bruikbaar.",
            waarom=[
                None,
                "Niet bruikbaar, en let op waarom: het jaar klopt, maar het gaat over Wallonië en "
                "over staal in plaats van over Limburgse mijnwerkerswoningen. Het juiste jaartal "
                "maakt een bron nog niet bruikbaar.",
                None,
                "Niet bruikbaar: de achttiende eeuw ligt twee eeuwen naast je vraag. Hier is het de "
                "tijd die niet past, niet het onderwerp.",
            ],
        ),
        dict(
            aanpak="Drie uitspraken en drie soorten. Een feit kan je nagaan, een mening geeft "
                   "iemands kijk, een waardeoordeel spreekt goed of slecht uit.",
            waarom=[
                "Let op het verschil tussen een mening en een waardeoordeel: bij de tweede "
                "uitspraak zitten de woorden veel te slecht, en dat is een oordeel. De derde "
                "uitspraak zegt zelf volgens mij, en dat is een mening.",
            ],
        ),
        dict(
            aanpak="Vier vragen bij elke bron: wie, wanneer, voor wie, en met welk doel. Antwoord in "
                   "die orde, dan volgt het besluit over de betrouwbaarheid er zelf uit.",
            waarom=[
                "Noem dat de regering in ballingschap zat, in Londen. Dat verklaart waarom de "
                "affiche daar gedrukt werd en voor wie ze bedoeld was. En noem dat ze juist als "
                "propaganda een uitstekende bron is, voor de goede vraag.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: primair tegenover secundair, de "
                   "bruikbaarheid, en wat eerlijk werken betekent.",
            waarom=[
                "Niet waar: een ooggetuige kan zich vergissen, overdrijven of een belang hebben. "
                "Een latere historicus kan meer bronnen naast elkaar leggen. Primair en "
                "betrouwbaar zijn twee verschillende dingen.",
                None,
                None,
                "Niet waar: de orde van de zoekresultaten zegt niets over de juistheid. Je kijkt "
                "wie de site maakte, wanneer en met welk doel, net als bij elke andere bron.",
                "Niet waar: met één bron weet je enkel wat die ene bron zegt. Je legt er altijd "
                "andere naast, en dat heet kruisen.",
                "Waar: beelden kunnen bewerkt of door een computer gemaakt zijn. Daarom vraag je "
                "ook bij een foto waar ze vandaan komt en wie ze maakte.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over dezelfde kern: de bruikbaarheid hangt af van je vraag, de "
                   "tegenspraak is zelf informatie, en de herkomst hoort erbij.",
            waarom=[
                "Noem beide kanten apart: voor de feiten onbetrouwbaar, voor de boodschap van de "
                "bezetter juist waardevol. Dat verschil is de kern van dit hoofdstuk.",
                "Noem ook dat je in je besluit zegt wat je niet zeker weet. Dat hoort bij eerlijk "
                "werken, en het is wat een historicus anders doet dan een verteller.",
                "Noem beide redenen: de controleerbaarheid en de eerlijkheid. Enkel plagiaat noemen "
                "is een half antwoord.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-beeldvorming-standplaatsgebondenheid-en-betekenisgeving-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes begrippen in twee groepen: drie over valkuilen bij het kijken, drie over wat "
                   "een samenleving met haar verleden doet.",
            waarom=[
                "Let op het eurocentrisme: het gaat niet enkel over fouten maar over de maatstaf. "
                "Wie schrijft dat Congo in 1885 ontsloten werd, kijkt vanuit Europa; voor de "
                "Congolezen begon er iets anders.",
                "Let op de historische empathie: dat is proberen te begrijpen, niet meeleven en "
                "niet goedkeuren. Dat onderscheid komt verder in de bundel terug.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk voorbeeld af wie beslist en waarom. Een feestdag, een "
                   "straatnaam en een beschermd gebouw zijn alle drie keuzes van vandaag.",
            waarom=[
                None,
                "Let erop dat een straatnaam niets aan het verleden verandert maar wel iets over "
                "ons zegt: wij vinden die daad vandaag navolgbaar. Daarom kan een straatnaam ook "
                "opnieuw ter discussie komen.",
                None,
            ],
        ),
        dict(
            aanpak="Eén vraag voor de hele reeks: wordt er onderzocht, of wordt er herdacht? "
                   "Onderzoek naar een herdenking blijft geschiedenis.",
            waarom=[
                None,
                None,
                "Let op deze: er wordt wel over een herdenking gesproken, maar het is een studie. "
                "Wie onderzoekt hoe een land herdenkt, doet aan geschiedenis.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de plaats van de historicus zelf, hoe een "
                   "beeld verandert, en waar de grens van de discussie ligt.",
            waarom=[
                "Waar, en dat is belangrijk: ook de historicus van vandaag leeft in een tijd met "
                "eigen vragen. Daarom zegt hij waar hij staat en waar zijn bronnen vandaan komen.",
                "Niet waar: begrijpen waarom iemand zo handelde is niet hetzelfde als het "
                "goedvinden. Juist dat onderscheid maakt empathie bruikbaar bij een moeilijk "
                "verleden.",
                None,
                "Niet waar: een handboek maakt keuzes over wat erin komt en wat niet, en het is in "
                "een bepaald land en een bepaalde tijd geschreven. Ook jouw handboek is een bron.",
                "Waar: de negationismewet van 1995 maakt het ontkennen van de Holocaust strafbaar. "
                "Een vaststelling met bewijs is dus geen mening waarover je vrij discussieert.",
                "Niet waar: wat een land herdenkt verschuift. Denk aan hoe het koloniale verleden "
                "vandaag anders besproken wordt dan vijftig jaar geleden.",
            ],
        ),
        dict(
            aanpak="Twee vragen bij hetzelfde geval. Blijf bij de redenen en de gevolgen, en geef "
                   "bij de oplossingen telkens het voordeel dat gevraagd wordt.",
            waarom=[
                "Noem bij elke oplossing het voordeel, zoals gevraagd. Een derde mogelijkheid is "
                "een tweede werk ernaast dat de andere kant toont; ook dat is een verdedigbaar "
                "antwoord.",
                "Noem dat ook het plaatsen van een monument een keuze van zijn eigen tijd was. "
                "Daarmee zie je twee lagen: de tijd van de persoon en de tijd van het beeld.",
            ],
        ),
        dict(
            aanpak="Drie open vragen: twee over verschillende verhalen over hetzelfde, en één over "
                   "waarom dit vak nut heeft. Gebruik bij de eerste twee het begrip "
                   "standplaatsgebondenheid.",
            waarom=[
                "Noem dat geen van beide liegt en dat beide verslagen samen meer tonen. Dat is "
                "precies wat multiperspectiviteit oplevert.",
                "Noem dat het verschil niet in de feiten zit maar in de nadruk en de hoofdrollen. "
                "Dat is een scherper antwoord dan zeggen dat het ene boek fout zou zijn.",
                "Noem beide redenen: begrijpen hoe het heden geworden is, en processen herkennen "
                "die opnieuw werken. De tweede reden is wat dit vak buiten de school bruikbaar "
                "maakt.",
            ],
        ),
    ],
)

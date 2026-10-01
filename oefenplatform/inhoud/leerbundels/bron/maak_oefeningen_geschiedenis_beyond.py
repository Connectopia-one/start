# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere gevallen om in te delen, andere bronnen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een oordeel
verantwoorden, een verband in eigen woorden opschrijven). Wie hier iets
bijschrijft, legt het eerst naast `../../beyond/geschiedenis.json`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen. Het achtervoegsel houdt ze uit elkaar van Boost doorstroom, dat een
thema met precies dezelfde titel heeft.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Geschiedenis"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

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
OEFENBUNDELS["oefenbundel-het-historisch-referentiekader-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het historisch referentiekader",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In welke periode?",
             opdracht="Schrijf bij elke gebeurtenis de naam van de periode waarin ze thuishoort.",
             oefeningen=[
                 ("rij", [("de uitvinding van de boekdrukkunst door Gutenberg", "de vroegmoderne tijd"),
                          ("de bouw van het Colosseum in Rome", "de klassieke oudheid"),
                          ("de eerste maanlanding", "de hedendaagse tijd")], "Welke periode?", WL),
                 ("rij", [("de Belgische onafhankelijkheid", "de moderne tijd"),
                          ("de kruistochten", "de middeleeuwen"),
                          ("de spijkerschrifttabletten van Mesopotamië", "het oude nabije oosten")],
                  "Welke periode?", WL),
             ]),
        dict(kop="Tijd of ruimte?",
             opdracht="Noteer bij elk begrip of het een structuurbegrip van de tijd of van de ruimte is.",
             oefeningen=[
                 ("rij", [("chronologie", "tijd"), ("maritiem", "ruimte"), ("duur", "tijd"),
                          ("ruraal", "ruimte"), ("periodisering", "tijd"), ("mondiaal", "ruimte")],
                  "Tijd of ruimte?", "92px"),
             ]),
        dict(kop="Continuïteit of verandering?",
             opdracht="Kruis aan wat van toepassing is, en schrijf er in één woord bij in welk domein het speelt.",
             oefeningen=[
                 ("kies", "In West-Europa blijft het Latijn eeuwenlang de taal van de wetenschap.",
                  ["continuïteit", "verandering"], 0),
                 ("kies", "Tussen 1870 en 1914 verdwijnt de huisnijverheid uit grote delen van Vlaanderen.",
                  ["continuïteit", "verandering"], 1),
                 ("kies", "In 2002 vervangt de euro in twaalf landen de nationale munt.",
                  ["continuïteit", "verandering"], 1),
                 ("kies", "De Belgische grondwet van 1831 is tot vandaag nooit volledig vervangen.",
                  ["continuïteit", "verandering"], 0),
             ]),
        dict(kop="Vier domeinen",
             opdracht="Vul de tabel aan. Schrijf per gebeurtenis het domein waarin ze in de eerste plaats thuishoort.",
             oefeningen=[
                 ("tabel", ["Gebeurtenis", "Domein"], [
                     ["De invoering van de leerplicht in 1914", None],
                     ["De oprichting van de Nationale Bank", None],
                     ["De eerste vrouw in een Belgische regering", None],
                     ["De bouw van een nieuwe kathedraal", None],
                 ], "leerplicht: cultureel (onderwijs) · Nationale Bank: economisch · "
                    "eerste vrouwelijke minister: politiek · kathedraal: cultureel", WW),
             ]),
        dict(kop="Scharnierpunt of niet?",
             opdracht="Waar of niet waar? Kruis aan.",
             oefeningen=[
                 ("waar", "Een scharnierpunt vormt de overgang tussen twee periodes.", True),
                 ("waar", "Een periodisering wordt opgesteld terwijl de periode bezig is.", False),
                 ("waar", "Een symbolische begindatum staat voor een verandering die langer duurde.", True),
                 ("waar", "Scharnierpunten liggen altijd in het politieke domein.", False),
                 ("waar", "Wie in Europa een scharnierpunt aanwijst, doet dat ook voor de rest van de wereld.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de uitdrukking 'de donkere eeuwen' voor de middeleeuwen geen "
                          "neutrale naam is.",
                  "In de naam zit al een oordeel: donker betekent achterlijk of arm. Wie die naam gebruikt, "
                  "heeft het verleden al beoordeeld voor hij het onderzocht heeft, en meestal met de "
                  "maatstaf van zijn eigen tijd.", 3),
                 ("open", "China deelt zijn verleden in volgens dynastieën. Leg uit waarom dat niet "
                          "verkeerder of juister is dan onze zeven periodes.",
                  "Elke periodisering is een constructie achteraf, gebouwd op een selectie van kenmerken. "
                  "De Chinese indeling kiest andere kenmerken dan de onze, en toont daarmee wat men daar "
                  "belangrijk vond. Verkeerd is ze pas als ze de bronnen tegenspreekt.", 3),
                 ("open", "Een handboek behandelt de negentiende eeuw enkel aan de hand van Europese "
                          "staten. Welke beperking is dat, en wat zou je toevoegen?",
                  "Dat is een ruimtelijk beperkte blik, en vaak ook een etnocentrische. Je zou er de "
                  "samenlevingen van buiten Europa naast moeten zetten: China, Japan, de Afrikaanse en "
                  "Aziatische gebieden die in diezelfde eeuw gekoloniseerd werden.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-restauratie-revolutie-en-het-ontstaan-van-belgie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Restauratie, revolutie en het ontstaan van België",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wie of wat?",
             opdracht="Schrijf de naam of het begrip in het vakje.",
             oefeningen=[
                 ("rij", [("de Oostenrijkse kanselier die het Congres van Wenen leidde", "Metternich"),
                          ("de koning van het Verenigd Koninkrijk der Nederlanden", "Willem I"),
                          ("de Pruisische minister-president van de Duitse eenmaking", "Bismarck")],
                  "Wie?", W),
                 ("rij", [("het stemrecht enkel voor wie genoeg belasting betaalt", "cijnskiesrecht"),
                          ("katholieken en liberalen besturen samen", "unionisme"),
                          ("het herstel van de toestand van voor 1789", "restauratie")],
                  "Welk begrip?", WW),
             ]),
        dict(kop="Verbindend of ontbindend nationalisme?",
             opdracht="Kruis per geval aan welke soort het is.",
             oefeningen=[
                 ("kies", "De Italiaanse staatjes smelten samen tot één koninkrijk.",
                  ["verbindend", "ontbindend"], 0),
                 ("kies", "Griekenland maakt zich los uit het Ottomaanse Rijk.",
                  ["verbindend", "ontbindend"], 1),
                 ("kies", "De Duitse staten vormen samen een keizerrijk.",
                  ["verbindend", "ontbindend"], 0),
                 ("kies", "De zuidelijke provincies scheiden zich af van het koninkrijk der Nederlanden.",
                  ["verbindend", "ontbindend"], 1),
             ]),
        dict(kop="Een tijdlijn aanvullen",
             opdracht="Zet het juiste jaartal bij elke gebeurtenis.",
             oefeningen=[
                 ("tabel", ["Gebeurtenis", "Jaartal"], [
                     ["Het Congres van Wenen eindigt", None],
                     ["De Belgische opstand begint in Brussel", None],
                     ["De Belgische grondwet wordt afgekondigd", None],
                     ["Het Duitse Keizerrijk wordt uitgeroepen", None],
                 ], "Congres van Wenen: 1815 · Belgische opstand: 1830 · grondwet: 1831 · "
                    "Duitse Keizerrijk: 1871", "80px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het Congres van Wenen hield rekening met de taal van de bevolking.", False),
                 ("waar", "De grondwet van 1831 schreef de vrijheid van onderwijs in.", True),
                 ("waar", "Het Nederlands was in 1831 de taal van de Belgische rechtbanken.", False),
                 ("waar", "De Vlaamse beweging begon als een culturele beweging.", True),
                 ("waar", "De Duitse Bond was één staat met één regering.", False),
             ]),
        dict(kop="Grieven van het Zuiden",
             opdracht="Noteer in het vakje in welk domein het grief vooral thuishoort: politiek, cultureel of economisch.",
             oefeningen=[
                 ("rij", [("het Nederlands wordt opgelegd als bestuurstaal", "cultureel"),
                          ("het Zuiden krijgt te weinig zetels", "politiek"),
                          ("het Zuiden wil bescherming, het Noorden vrijhandel", "economisch")],
                  "Welk domein?", W),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom liberalisme en nationalisme in de eerste helft van de "
                          "negentiende eeuw vaak samen optrokken.",
                  "Allebei keerden ze zich tegen de orde van Wenen. De liberalen wilden een grondwet die "
                  "de macht van de vorst beperkt, de nationalisten wilden staten die met een volk "
                  "samenvallen. In allebei de gevallen moest de oude dynastie iets afstaan, en dus vonden "
                  "ze elkaar.", 4),
                 ("open", "Het Duitse Keizerrijk werd in de Spiegelzaal van Versailles uitgeroepen. "
                          "Waarom was die plaats een bewuste keuze?",
                  "Versailles was het paleis van de Franse koningen en Frankrijk was net verslagen. De "
                  "keuze van die zaal was dus een vernedering van de verliezer en een machtsvertoon. In "
                  "1919 werd dat omgekeerd: daar moest Duitsland het Verdrag van Versailles tekenen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-industrialisatie-en-de-sociale-kwestie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Industrialisatie en de sociale kwestie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eerste of tweede industriële revolutie?",
             opdracht="Noteer bij elk kenmerk of het bij de eerste of bij de tweede hoort.",
             oefeningen=[
                 ("rij", [("steenkool en stoom", "eerste"), ("elektriciteit", "tweede"),
                          ("de lopende band", "tweede"), ("het stoomschip", "eerste"),
                          ("de verbrandingsmotor", "tweede"), ("de spinmachine in textiel", "eerste")],
                  "Eerste of tweede?", "92px"),
             ]),
        dict(kop="In welke sector?",
             opdracht="Schrijf primair, secundair of tertiair in het vakje.",
             oefeningen=[
                 ("rij", [("steenkoolmijnbouw", "primair"), ("een staalfabriek", "secundair"),
                          ("een spoorwegmaatschappij", "tertiair"), ("akkerbouw", "primair"),
                          ("een weverij", "secundair")], "Welke sector?", "98px"),
             ]),
        dict(kop="Aanbod of vraag?",
             opdracht="Kruis aan of het om een aanbodfactor of een vraagfactor van de industrialisatie gaat.",
             oefeningen=[
                 ("kies", "Er zit steenkool in de bodem van Henegouwen en Luik.",
                  ["aanbodfactor", "vraagfactor"], 0),
                 ("kies", "De bevolking groeit en koopt meer goederen.",
                  ["aanbodfactor", "vraagfactor"], 1),
                 ("kies", "Banken durven in nieuwe fabrieken te investeren.",
                  ["aanbodfactor", "vraagfactor"], 0),
                 ("kies", "Er zijn vaklui met ervaring in textiel en metaal.",
                  ["aanbodfactor", "vraagfactor"], 0),
             ]),
        dict(kop="Drie antwoorden op de sociale kwestie",
             opdracht="Vul de tabel aan met het ontbrekende woord of de ontbrekende zin.",
             oefeningen=[
                 ("tabel", ["Stroming", "Wat ze wil", "Hoe ze het wil bereiken"], [
                     ["Marxisme", None, "door revolutie"],
                     ["Sociaaldemocratie", "een eerlijker verdeling van de welvaart", None],
                     ["Christendemocratie", None, "door overleg en wetgeving"],
                 ], "Marxisme: de arbeiders nemen de productiemiddelen in handen · "
                    "Sociaaldemocratie: langs verkiezingen en wetten · "
                    "Christendemocratie: privébezit blijft, maar met een rechtvaardig loon en bescherming",
                  WL),
             ]),
        dict(kop="Vakbond, coöperatie of mutualiteit?",
             opdracht="Schrijf in het vakje welke van de drie het is.",
             oefeningen=[
                 ("rij", [("samen sparen om bij ziekte een uitkering te krijgen", "mutualiteit"),
                          ("samen onderhandelen over het loon en zo nodig staken", "vakbond"),
                          ("samen een winkel uitbaten en de winst delen", "coöperatie")],
                  "Welke organisatie?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De Belgische grondwet van 1831 verbood kinderarbeid.", False),
                 ("waar", "Het algemeen meervoudig stemrecht kwam er in 1893 na een algemene staking.", True),
                 ("waar", "Bij het meervoudig stemrecht kon één man hoogstens drie stemmen uitbrengen.", True),
                 ("waar", "Tijdens de industrialisatie groeide het aandeel van de landbouw in de tewerkstelling.", False),
                 ("waar", "In de eerste industriële revolutie stond de fabriek dicht bij de steenkool.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat proletarisering is en geef er een voorbeeld bij.",
                  "Proletarisering is dat boeren en ambachtslui hun eigen werktuigen en grond verliezen en "
                  "loonarbeider worden. Voorbeeld: een thuiswever die zijn getouw niet meer kan laten "
                  "renderen tegen de fabrieksprijzen en in de fabriek in Gent gaat werken.", 4),
                 ("open", "Waarom bleven in België meer arbeiders op het platteland wonen dan in andere "
                          "industrielanden?",
                  "Door de goedkope werkmanskaarten op de trein. Een arbeider kon elke dag naar de fabriek "
                  "sporen en 's avonds thuiskomen, zodat hij zijn huisje en zijn lapje grond kon houden. "
                  "Daardoor verliep de plattelandsvlucht hier trager.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-modern-imperialisme-congo-en-china-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Modern imperialisme, Congo en China",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk motief?",
             opdracht="Noteer of het motief economisch, politiek of cultureel is.",
             oefeningen=[
                 ("rij", [("goedkope grondstoffen voor de eigen fabrieken", "economisch"),
                          ("prestige tegenover de andere mogendheden", "politiek"),
                          ("het idee dat men beschaving brengt", "cultureel"),
                          ("een vlootbasis op een strategisch punt", "politiek"),
                          ("nieuwe afzetmarkten voor eigen producten", "economisch")],
                  "Welk motief?", W),
             ]),
        dict(kop="Wat maakte het mogelijk?",
             opdracht="Schrijf bij elke zin het middel dat erbij hoort.",
             oefeningen=[
                 ("rij", [("beschermde Europeanen tegen malaria", "kinine"),
                          ("kon rivieren opvaren tot diep in het binnenland", "het stoomschip"),
                          ("gaf een beslissende voorsprong in een gevecht", "repeteergeweer of mitrailleur")],
                  "Welk middel?", WL),
             ]),
        dict(kop="Congo-Vrijstaat of Belgisch Congo?",
             opdracht="Kruis aan waar het bij hoort.",
             oefeningen=[
                 ("kies", "Het gebied is het persoonlijke bezit van Leopold II.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 0),
                 ("kies", "Staat, kerk en bedrijven besturen samen.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 1),
                 ("kies", "Dorpen moeten een vastgelegde hoeveelheid rubber leveren.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 0),
                 ("kies", "Het koper van Katanga en het uranium worden de grote uitvoerproducten.",
                  ["Congo-Vrijstaat", "Belgisch Congo"], 1),
             ]),
        dict(kop="Congo en China vergeleken",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Congo", "China"], [
                     ["Vorm van overheersing", None, None],
                     ["Blijft het een eigen staat?", None, None],
                 ], "Congo: volledige bezetting en rechtstreeks bestuur, geen eigen staat meer · "
                    "China: invloedssferen en ongelijke verdragen, blijft formeel een keizerrijk", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Tegen 1914 was vrijwel heel Afrika onder Europese mogendheden verdeeld.", True),
                 ("waar", "De Verenigde Staten hielden zich volledig buiten het imperialisme.", False),
                 ("waar", "Japan werd na 1868 zelf een koloniale macht.", True),
                 ("waar", "China werd volledig gekoloniseerd zoals Congo.", False),
                 ("waar", "Dat de blik op het koloniale verleden verandert, betekent dat de feiten veranderen.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom men spreekt van een wedloop om Afrika.",
                  "De mogendheden bezetten gebieden vooral uit schrik dat een ander het eerst zou doen. "
                  "Op de Conferentie van Berlijn werd afgesproken dat je een gebied werkelijk moest "
                  "bezetten en besturen om er aanspraak op te maken, en dat zette de wedloop nog aan.", 4),
                 ("open", "Een affiche uit 1900 noemt de kolonisatie een beschavingswerk. Wat kan je met "
                          "die bron doen, en wat niet?",
                  "Je kan er niet uit afleiden hoe het er in de kolonie werkelijk aan toeging. Je kan er "
                  "wel uit afleiden hoe men de kolonisatie in Europa wilde voorstellen, en welke "
                  "rechtvaardiging men nodig had. Als bron over beeldvorming is ze uitstekend.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-eerste-wereldoorlog-en-de-russische-revoluties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De Eerste Wereldoorlog en de Russische revoluties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Aanleiding of oorzaak?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "De moord op Frans Ferdinand in Sarajevo.", ["aanleiding", "diepere oorzaak"], 0),
                 ("kies", "De wedloop in bewapening tussen de grote mogendheden.",
                  ["aanleiding", "diepere oorzaak"], 1),
                 ("kies", "Het web van bondgenootschappen tussen de Europese staten.",
                  ["aanleiding", "diepere oorzaak"], 1),
                 ("kies", "Het nationalisme op de Balkan en elders in Europa.",
                  ["aanleiding", "diepere oorzaak"], 1),
             ]),
        dict(kop="Jaartal of datum",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("de wapenstilstand van de Eerste Wereldoorlog", "11 november 1918"),
                          ("de Oktoberrevolutie in Rusland", "1917"),
                          ("de oprichting van de Volkenbond", "1920")], "Wanneer?", WW),
             ]),
        dict(kop="Een totale oorlog",
             opdracht="Noteer bij elk gegeven hoe het toont dat dit een totale oorlog was.",
             oefeningen=[
                 ("rij", [("vrouwen in de munitiefabrieken", "de hele samenleving werd ingezet"),
                          ("affiches en gekleurde oorlogsberichten", "propaganda hield de steun vast"),
                          ("rantsoenering van voedsel", "de economie werd volledig op de oorlog gericht")],
                  "Wat toont het?", WL),
             ]),
        dict(kop="Versailles",
             opdracht="Vul de tabel aan met wat het verdrag Duitsland oplegde.",
             oefeningen=[
                 ("tabel", ["Domein", "Wat het verdrag oplegde"], [
                     ["Schuldvraag", None],
                     ["Geld", None],
                     ["Leger", None],
                     ["Grondgebied", None],
                 ], "Schuldvraag: Duitsland moest de schuld voor de oorlog erkennen · "
                    "Geld: herstelbetalingen · Leger: nog maar een klein leger · "
                    "Grondgebied: onder meer Elzas-Lotharingen terug naar Frankrijk", WL),
             ]),
        dict(kop="De Volkenbond beoordelen",
             opdracht="Waar of niet waar? Kruis aan.",
             oefeningen=[
                 ("waar", "De Verenigde Staten traden nooit tot de Volkenbond toe.", True),
                 ("waar", "De Volkenbond beschikte over een eigen leger.", False),
                 ("waar", "Beslissingen in de Volkenbond vroegen de instemming van iedereen.", True),
                 ("waar", "De Volkenbond werd opgericht om conflicten vreedzaam te beslechten.", True),
             ]),
        dict(kop="Rusland in 1917",
             opdracht="Zet de gebeurtenissen in de juiste volgorde door er 1, 2, 3 of 4 bij te schrijven.",
             oefeningen=[
                 ("rij", [("de Oktoberrevolutie", "4"), ("de troonsafstand van Nicolaas II", "2"),
                          ("nederlagen en honger aan het front", "1"),
                          ("de voorlopige regering verliest haar steun", "3")],
                  "Volgorde?", "58px"),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem één bedoeld en één onbedoeld gevolg van het Verdrag van Versailles.",
                  "Bedoeld: Duitsland militair en financieel klein houden zodat het geen nieuwe oorlog kon "
                  "beginnen. Onbedoeld: het verdrag werd in Duitsland als een dictaat ervaren en werd zo "
                  "een voedingsbodem voor extreme partijen.", 4),
                 ("open", "Leg uit waarom Lenins leus 'vrede, brood en land' precies aansloot bij wat "
                          "mensen in 1917 wilden.",
                  "Vrede sloeg op de oorlog die de voorlopige regering voortzette, brood op de "
                  "voedseltekorten in de steden, en land op de verdeling van de grond die steeds werd "
                  "uitgesteld. Elk van de drie was net waarop de voorlopige regering tekortschoot.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-interbellum-totalitarisme-en-crisis-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Interbellum: totalitarisme en crisis",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De crisis van 1929",
             opdracht="Noteer bij elk gegeven of het een oorzaak of een gevolg van de crisis is.",
             oefeningen=[
                 ("rij", [("aandelen kopen met geleend geld", "oorzaak"),
                          ("massale werkloosheid in Europa", "gevolg"),
                          ("overproductie in industrie en landbouw", "oorzaak"),
                          ("politieke radicalisering", "gevolg"),
                          ("een zeer ongelijke verdeling van de welvaart", "oorzaak")],
                  "Oorzaak of gevolg?", "98px"),
             ]),
        dict(kop="Drie totalitaire regimes",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Land", "Leider", "Jaar waarin hij de macht kreeg"], [
                     ["Italië", None, None],
                     ["Sovjet-Unie", None, None],
                     ["Duitsland", None, None],
                 ], "Italië: Mussolini, 1922 · Sovjet-Unie: Stalin, vanaf 1924 · Duitsland: Hitler, 1933",
                  W),
             ]),
        dict(kop="Kenmerk van een totalitaire staat?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Eén partij en één leider.", True),
                 ("waar", "Controle over pers, onderwijs en kunst.", True),
                 ("waar", "Een onafhankelijke rechterlijke macht.", False),
                 ("waar", "Een geheime politie die tegenstanders uitschakelt.", True),
                 ("waar", "Een regime gebruikt propaganda óf terreur, nooit allebei.", False),
             ]),
        dict(kop="Wat gebeurde waar?",
             opdracht="Schrijf het begrip of de naam in het vakje.",
             oefeningen=[
                 ("rij", [("het samenvoegen van boerderijen tot grote staatsbedrijven", "collectivisatie"),
                          ("strafkampen met dwangarbeid in de Sovjet-Unie", "de goelags"),
                          ("de leider als onfeilbaar voorstellen", "personencultus")],
                  "Welk begrip?", WW),
                 ("rij", [("de mars waarmee Mussolini in 1922 de macht kreeg", "de Mars op Rome"),
                          ("het gebouw dat in februari 1933 afbrandde", "de Rijksdag"),
                          ("de wet die Hitler zonder parlement liet regeren", "de Machtigingswet")],
                  "Wat of welke?", WL),
             ]),
        dict(kop="De weg naar 1939",
             opdracht="Zet de stappen in de juiste volgorde: schrijf 1 tot 5.",
             oefeningen=[
                 ("rij", [("de inval in Polen", "5"),
                          ("de herinvoering van de dienstplicht", "1"),
                          ("de inlijving van Oostenrijk", "3"),
                          ("de Conferentie van München", "4"),
                          ("troepen trekken het Rijnland binnen", "2")],
                  "Volgorde?", "58px"),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg met de redeneerwijze oorzaak en gevolg uit hoe de crisis van 1929 "
                          "bijdroeg tot de machtsovername van Hitler.",
                  "De crisis bracht massale werkloosheid en armoede in Duitsland. Mensen die hun werk en "
                  "hun spaargeld kwijt waren, verloren het vertrouwen in de bestaande partijen en werden "
                  "vatbaar voor een partij die orde, werk en herstel beloofde. Zo groeide de NSDAP van een "
                  "randpartij tot de grootste, en in januari 1933 werd Hitler rijkskanselier.", 5),
                 ("open", "Wat is het grote verschil tussen het Italiaanse fascisme en het "
                          "nationaalsocialisme?",
                  "Allebei zijn het totalitaire regimes met één partij, één leider en geen tegenspraak. "
                  "Bij het nationaalsocialisme staan daarbovenop de rassenleer en het antisemitisme "
                  "centraal, en die leiden tot vervolging en uiteindelijk tot vernietiging.", 4),
                 ("open", "Waarom wordt appeasement vandaag meestal als een vergissing gezien?",
                  "Frankrijk en Groot-Brittannië gaven toe om een oorlog te vermijden, maar elke toegeving "
                  "maakte Duitsland sterker en zelfzekerder. Na München volgde binnen het jaar de inval in "
                  "Polen. Wie met zijn kennis van nu oordeelt, moet er wel bij zeggen dat de herinnering "
                  "aan de loopgraven van 14-18 toen zwaar woog.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-tweede-wereldoorlog-en-de-holocaust-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De Tweede Wereldoorlog en de Holocaust",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee wereldoorlogen vergeleken",
             opdracht="Vul de tabel aan met een kort antwoord.",
             oefeningen=[
                 ("tabel", ["", "Eerste Wereldoorlog", "Tweede Wereldoorlog"], [
                     ["Manier van vechten", None, None],
                     ["Waar uitgevochten", None, None],
                     ["Burgers of militairen het zwaarst getroffen", None, None],
                 ], "Manier van vechten: loopgraven tegenover snelle bewegingsoorlog · "
                    "Waar: vooral Europa tegenover bijna de hele wereld · "
                    "Slachtoffers: vooral militairen tegenover vooral burgers", WW),
             ]),
        dict(kop="Keerpunt of niet?",
             opdracht="Kruis aan of het als een keerpunt van de oorlog geldt.",
             oefeningen=[
                 ("waar", "Stalingrad.", True),
                 ("waar", "El Alamein.", True),
                 ("waar", "De inval in Polen.", False),
                 ("waar", "Midway.", True),
                 ("waar", "Het Ardennenoffensief.", False),
             ]),
        dict(kop="Data invullen",
             opdracht="Schrijf de datum of het jaar in het vakje.",
             oefeningen=[
                 ("rij", [("de Duitse inval in België", "10 mei 1940"),
                          ("de landing in Normandië", "6 juni 1944"),
                          ("de Wannseeconferentie", "januari 1942")], "Wanneer?", WW),
             ]),
        dict(kop="Bezet België",
             opdracht="Noteer bij elk voorbeeld of het collaboratie of verzet is, en van welke soort.",
             oefeningen=[
                 ("rij", [("een sluikblad drukken en verspreiden", "verzet"),
                          ("vrijwillig naar het oostfront vertrekken", "militaire collaboratie"),
                          ("een fabriek die voor de bezetter produceert", "economische collaboratie"),
                          ("een onderduikadres zoeken voor een Joods kind", "verzet")],
                  "Wat is het?", WL),
             ]),
        dict(kop="De vervolging in stappen",
             opdracht="Zet in de juiste volgorde: schrijf 1, 2 of 3.",
             oefeningen=[
                 ("rij", [("de systematische vernietiging in kampen", "3"),
                          ("uitsluiting uit het openbare leven", "1"),
                          ("gedwongen samenleven in getto's", "2")], "Volgorde?", "58px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het begrip genocide bestond al voor de Tweede Wereldoorlog in het internationale recht.", False),
                 ("waar", "Uit de Dossinkazerne in Mechelen vertrokken treinen naar Auschwitz.", True),
                 ("waar", "Het naziregime vervolgde ook Roma en Sinti en mensen met een beperking.", True),
                 ("waar", "Collaboratie en verzet waren twee scherp gescheiden kampen waartussen niets lag.", False),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de Holocaust onder de definitie van genocide valt.",
                  "Genocide is het opzettelijk geheel of gedeeltelijk vernietigen van een nationale, "
                  "etnische, raciale of religieuze groep. Bij de Holocaust was het de uitdrukkelijke "
                  "bedoeling dat een hele bevolkingsgroep zou verdwijnen, en dat werd planmatig "
                  "georganiseerd, tot op de dienstregeling van de treinen.", 5),
                 ("open", "Waarom zijn getuigenissen van overlevenden nodig naast de cijfers?",
                  "Cijfers tonen de omvang maar niet de ervaring. Een getuigenis laat horen wat honger, "
                  "angst en verlies met een mens doen, en maakt dat een leerling zich iets kan "
                  "voorstellen bij een getal van zes miljoen. Nu de laatste getuigen wegvallen, moeten "
                  "onderwijs en archieven dat overnemen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-nieuwe-wereldorde-vn-koude-oorlog-en-europa-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een nieuwe wereldorde: VN, Koude Oorlog en Europa",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Volkenbond of Verenigde Naties?",
             opdracht="Noteer bij elk kenmerk welke van de twee het is.",
             oefeningen=[
                 ("rij", [("opgericht in 1920", "Volkenbond"), ("opgericht in 1945", "Verenigde Naties"),
                          ("de Verenigde Staten traden nooit toe", "Volkenbond"),
                          ("heeft een Veiligheidsraad met vetorecht", "Verenigde Naties")],
                  "Welke organisatie?", WW),
             ]),
        dict(kop="Sterkte of zwakte van de VN?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Alle landen kunnen er met elkaar spreken.", ["sterkte", "zwakte"], 0),
                 ("kies", "Eén vast lid kan alles met een veto tegenhouden.", ["sterkte", "zwakte"], 1),
                 ("kies", "Humanitaire hulp bij rampen en hongersnood.", ["sterkte", "zwakte"], 0),
                 ("kies", "Er is geen eigen staand leger.", ["sterkte", "zwakte"], 1),
             ]),
        dict(kop="De Koude Oorlog op een tijdlijn",
             opdracht="Schrijf het jaartal in het vakje.",
             oefeningen=[
                 ("rij", [("de blokkade van Berlijn begint", "1948"), ("de opstand in Hongarije", "1956"),
                          ("de bouw van de Berlijnse Muur", "1961"), ("de Cubacrisis", "1962")],
                  "Welk jaar?", "80px"),
                 ("rij", [("de Praagse Lente", "1968"), ("de val van de Berlijnse Muur", "1989"),
                          ("het einde van de Sovjet-Unie", "1991")], "Welk jaar?", "80px"),
             ]),
        dict(kop="De verdragen van Europa",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Verdrag", "Jaar", "Wat het bracht"], [
                     ["Verdrag van Rome", None, None],
                     ["Verdrag van Maastricht", None, None],
                     ["Verdrag van Lissabon", None, None],
                 ], "Rome 1957: de EEG en de gemeenschappelijke markt · "
                    "Maastricht 1992: de Europese Unie en de weg naar de euro · "
                    "Lissabon 2007: vaste voorzitter, meer macht voor het Parlement, bindende grondrechten",
                  WW),
             ]),
        dict(kop="Welke instelling?",
             opdracht="Schrijf de naam van de Europese instelling in het vakje.",
             oefeningen=[
                 ("rij", [("stelt de wetgeving voor", "de Europese Commissie"),
                          ("wordt rechtstreeks door de burgers verkozen", "het Europees Parlement"),
                          ("brengt de staatshoofden en regeringsleiders samen", "de Europese Raad"),
                          ("brengt de vakministers van de lidstaten samen", "de Raad van de Europese Unie")],
                  "Welke instelling?", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom men spreekt van een koude oorlog, hoewel er wel degelijk "
                          "gevochten werd.",
                  "De twee supermachten vochten nooit rechtstreeks tegen elkaar: dat zou een kernoorlog "
                  "betekend hebben. Ze botsten wel voortdurend via andere landen, in Korea, Vietnam, "
                  "Afghanistan en Angola, en daar vielen zeer veel slachtoffers.", 4),
                 ("open", "Wat is het verband tussen de Tweede Wereldoorlog en het begin van de Europese "
                          "eenmaking?",
                  "De eenmaking moest een nieuwe oorlog tussen buurlanden onmogelijk maken. Daarom bracht "
                  "men net kolen en staal, de grondstoffen van de oorlog, onder gezamenlijk beheer. Wie "
                  "zijn wapenindustrie deelt, kan zijn buur niet meer onverwacht aanvallen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dekolonisatie-en-de-wereld-van-vandaag-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Dekolonisatie en de wereld van vandaag",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oorzaak van de dekolonisatie?",
             opdracht="Kruis aan of het wel of niet tot de oorzaken hoort.",
             oefeningen=[
                 ("waar", "De Europese mogendheden kwamen verzwakt uit de Tweede Wereldoorlog.", True),
                 ("waar", "In de koloniën groeiden nationalistische bewegingen met opgeleide leiders.", True),
                 ("waar", "De koloniën vroegen zelf om strenger bestuur vanuit Europa.", False),
                 ("waar", "Het Handvest van de VN schreef het zelfbeschikkingsrecht van volkeren in.", True),
             ]),
        dict(kop="Begrippen",
             opdracht="Schrijf het begrip in het vakje.",
             oefeningen=[
                 ("rij", [("economische overheersing van een politiek onafhankelijk land", "neokolonialisme"),
                          ("landen die bij geen van beide blokken aansloten", "de niet-gebonden landen"),
                          ("opnieuw bekijken hoe wij over het koloniale verleden spreken", "dekolonisering van het denken")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Congo op een tijdlijn",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Gebeurtenis", "Jaar"], [
                     ["Rellen in Leopoldstad dwingen België tot een koerswijziging", None],
                     ["Congo wordt onafhankelijk", None],
                     ["Lumumba wordt vermoord", None],
                     ["Mobutu grijpt de macht", None],
                     ["Mobutu wordt verdreven", None],
                 ], "rellen: 1959 · onafhankelijkheid: 1960 · moord op Lumumba: 1961 · "
                    "Mobutu grijpt de macht: 1965 · Mobutu verdreven: 1997", "80px"),
             ]),
        dict(kop="Wie is wie?",
             opdracht="Schrijf de naam in het vakje.",
             oefeningen=[
                 ("rij", [("de eerste eerste minister van onafhankelijk Congo", "Patrice Lumumba"),
                          ("de generaal die het land Zaïre noemde", "Mobutu"),
                          ("de man die Mobutu in 1997 verdreef", "Laurent-Désiré Kabila")],
                  "Wie?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Alle Afrikaanse koloniën werden zonder geweld onafhankelijk.", False),
                 ("waar", "In 1960 werden zeventien Afrikaanse koloniën onafhankelijk.", True),
                 ("waar", "De Verenigde Naties stuurden in 1960 een vredesmacht naar Congo.", True),
                 ("waar", "Het oosten van Congo is sinds 1997 vrij van gewapende conflicten.", False),
                 ("waar", "Koning Filip drukte in 2020 zijn diepste spijt uit over het koloniale verleden.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg het verband uit tussen de dekolonisatie en de Koude Oorlog.",
                  "Elke nieuwe staat was een stem in de VN en een plek op de kaart. De twee supermachten "
                  "probeerden die staten naar hun kamp te trekken met geld, wapens en steun, en namen er "
                  "bij dat de leider die ze steunden geen democraat was. Mobutu in Zaïre is daar het "
                  "bekendste voorbeeld van.", 5),
                 ("open", "Welke rol speelde de Belgische overheid in het dekolonisatieproces van Congo? "
                          "Noem twee punten.",
                  "België bereidde de onafhankelijkheid nauwelijks voor: het plan-Van Bilsen van dertig "
                  "jaar werd weggehoond en uiteindelijk ging het in vijf maanden. Er waren bijna geen "
                  "Congolese universitair geschoolden. Daarnaast steunden Belgische bedrijven en militairen "
                  "de afscheiding van Katanga, en een parlementaire commissie besloot in 2001 tot een "
                  "morele verantwoordelijkheid van Belgische regeringsleden bij de dood van Lumumba.", 6),
                 ("open", "Waarom is de strijd om grondstoffen in Congo vandaag nog actueel?",
                  "Kobalt en coltan uit Congo zitten in gsm's, laptops en elektrische auto's. De rijkdom "
                  "van de ondergrond maakte het land in elke eeuw tot inzet: eerst rubber en ivoor, dan "
                  "koper en uranium, nu kobalt en coltan. In het oosten voeden die grondstoffen mee de "
                  "conflicten.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-belgie-na-1945-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="België na 1945",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Op welke breuklijn?",
             opdracht="Schrijf in het vakje: levensbeschouwelijk, sociaaleconomisch of communautair.",
             oefeningen=[
                 ("rij", [("de schoolstrijd", "levensbeschouwelijk"),
                          ("een staking voor hogere lonen", "sociaaleconomisch"),
                          ("Leuven Vlaams", "communautair"),
                          ("het debat over levensbeschouwing op school", "levensbeschouwelijk"),
                          ("de vraag naar een nieuwe staatshervorming", "communautair")],
                  "Welke breuklijn?", WW),
             ]),
        dict(kop="Federaal, gewest of gemeenschap?",
             opdracht="Noteer welk niveau bevoegd is.",
             oefeningen=[
                 ("rij", [("het onderwijs", "gemeenschap"), ("het leger", "federaal"),
                          ("de ruimtelijke ordening", "gewest"), ("justitie", "federaal"),
                          ("cultuur", "gemeenschap"), ("het leefmilieu", "gewest")],
                  "Welk niveau?", W),
             ]),
        dict(kop="Staatshervormingen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Jaar", "Wat ze bracht"], [
                     ["1970", None],
                     ["1993", None],
                     ["2011-2014", None],
                 ], "1970: de cultuurgemeenschappen en de taalgebieden in de grondwet · "
                    "1993: België wordt in artikel 1 een federale staat, rechtstreeks verkozen "
                    "deelparlementen · 2011-2014: kinderbijslag en delen van het arbeidsmarktbeleid naar "
                    "de deelstaten, splitsing van Brussel-Halle-Vilvoorde", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het sociaal pact van 1944 legde de grondslagen van de sociale zekerheid.", True),
                 ("waar", "De federale overheid kan een decreet van het Vlaams Parlement zomaar overrulen.", False),
                 ("waar", "In Vlaanderen zijn gewest en gemeenschap samengevoegd tot één parlement.", True),
                 ("waar", "De zuilorganisaties zijn vandaag uit België verdwenen.", False),
                 ("waar", "Bij de volksraadpleging over Leopold III stemde Vlaanderen anders dan Wallonië.", True),
             ]),
        dict(kop="Begrippen",
             opdracht="Schrijf het begrip in het vakje.",
             oefeningen=[
                 ("rij", [("een wet van het Vlaams Parlement", "een decreet"),
                          ("een wet van het Brussels Parlement", "een ordonnantie"),
                          ("de nadruk van uitkeren naar aan het werk helpen", "de actieve welvaartsstaat")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Beschrijf het verband tussen een breuklijn en een actueel maatschappelijk debat "
                          "naar keuze.",
                  "Voorbeeld: het debat over de betaalbaarheid van de pensioenen ligt op de "
                  "sociaaleconomische breuklijn. De vraag is immers wie de lasten draagt en wie de "
                  "opbrengst krijgt: wie langer moet werken, wie meer bijdraagt, en wie beschermd wordt. "
                  "Partijen aan de kant van de arbeid en aan de kant van het kapitaal geven daarop een "
                  "ander antwoord.", 5),
                 ("open", "Waarom hebben de Belgische staatshervormingen vooral met één breuklijn te maken?",
                  "Met de communautaire. Telkens de spanning tussen de taalgemeenschappen te hoog opliep, "
                  "kwam er een nieuwe ronde bevoegdheden over te hevelen. Sinds de splitsing van de "
                  "nationale partijen in de jaren zestig spreekt geen enkele partij nog kiezers in beide "
                  "landsdelen aan, waardoor die breuklijn zich telkens opnieuw laat voelen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-denken-kunst-en-emancipatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Denken, kunst en emancipatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Jaartallen van de emancipatie",
             opdracht="Schrijf het jaartal in het vakje.",
             oefeningen=[
                 ("rij", [("vrouwen stemmen voor het eerst bij nationale verkiezingen in België", "1948"),
                          ("de staking van de vrouwen van FN Herstal", "1966"),
                          ("de opstand in de Stonewall Inn in New York", "1969")], "Welk jaar?", "80px"),
                 ("rij", [("abortus gaat in België uit het strafrecht", "1990"),
                          ("België stelt het huwelijk open voor koppels van hetzelfde geslacht", "2003"),
                          ("de mars op Washington met de toespraak van Martin Luther King", "1963")],
                  "Welk jaar?", "80px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De loonkloof tussen mannen en vrouwen is in België volledig verdwenen.", False),
                 ("waar", "Tot 1976 was de man wettelijk het hoofd van het gezin.", True),
                 ("waar", "Alle leiders van de zwarte beweging in de VS kozen voor geweldloos verzet.", False),
                 ("waar", "De jongerencultuur van de jaren zestig had ook een politieke kant.", True),
             ]),
        dict(kop="Welke stroming?",
             opdracht="Schrijf de naam van de kunststroming in het vakje.",
             oefeningen=[
                 ("rij", [("beelden uit reclame en strips, felle kleuren, veel herhaling", "popart"),
                          ("spontane, bijna kinderlijke beelden, ontstaan in 1948", "Cobra"),
                          ("vormen die het oog laten denken dat er beweging in zit", "optical art"),
                          ("het idee telt meer dan het voorwerp", "conceptuele kunst")],
                  "Welke stroming?", WW),
             ]),
        dict(kop="Popart in detail",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Kunstenaar", "Waaraan je zijn werk herkent"], [
                     ["Andy Warhol", None],
                     ["Roy Lichtenstein", None],
                     ["Claes Oldenburg", None],
                 ], "Warhol: dezelfde beelden in reeksen herhaald met zeefdruk, zoals de soepblikken van "
                    "Campbell · Lichtenstein: vergrote stripbeelden met zichtbare drukstippen · "
                    "Oldenburg: reusachtige beelden van alledaagse voorwerpen", WL),
             ]),
        dict(kop="Beweging of partij?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Voert actie rond één thema en komt niet op bij verkiezingen.",
                  ["protestbeweging", "politieke partij"], 0),
                 ("kies", "Dient een lijst in en wil zetels in een parlement.",
                  ["protestbeweging", "politieke partij"], 1),
                 ("kies", "De klimaatmarsen van jongeren.", ["protestbeweging", "politieke partij"], 0),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de popart niet los te zien is van de tijd waarin ze ontstond.",
                  "De popart haalt haar beelden uit reclame, merken, strips en de supermarkt. Die wereld "
                  "bestond pas door de naoorlogse welvaart, de massaproductie en de televisiereclame. "
                  "Zonder die consumptiemaatschappij heeft de popart geen onderwerp, en ook haar ironie "
                  "zou nergens op slaan.", 5),
                 ("open", "Emancipatiebewegingen hebben vaak generaties nodig. Geef een voorbeeld en leg "
                          "uit.",
                  "Voorbeeld: tussen de eerste eisen voor vrouwenstemrecht in de negentiende eeuw en de "
                  "invoering ervan in België in 1948 liggen meer dan zestig jaar, en daarna duurde het nog "
                  "tot 1976 voor de man niet langer wettelijk hoofd van het gezin was. Een recht moet eerst "
                  "denkbaar worden, dan bespreekbaar, en pas daarna wordt het wet.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-redeneren-met-historische-bronnen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Redeneren met historische bronnen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Is dit een onderzoekbare vraag?",
             opdracht="Kruis aan. Een onderzoekbare vraag is afgebakend in tijd, ruimte en domein, en er bestaan bronnen voor.",
             oefeningen=[
                 ("waar", "Hoe veranderde het werk van vrouwen in de Gentse textielfabrieken tussen 1880 en 1900?", True),
                 ("waar", "Was de industriële revolutie goed of slecht?", False),
                 ("waar", "Welke argumenten gebruikten Belgische parlementsleden in 1908 voor de overname van Congo?", True),
                 ("waar", "Hoe leefden de mensen vroeger?", False),
             ]),
        dict(kop="Welke soort bron?",
             opdracht="Schrijf twee woorden: primair of secundair, en geschreven, mondeling, materieel of audiovisueel.",
             oefeningen=[
                 ("rij", [("een brief van een soldaat uit 1916", "primair, geschreven"),
                          ("een handboek over de oorlog uit 2020", "secundair, geschreven"),
                          ("opgegraven munten uit de 16de eeuw", "primair, materieel"),
                          ("een filmjournaal uit 1944", "primair, audiovisueel")],
                  "Welke soort?", WL),
             ]),
        dict(kop="Welk criterium?",
             opdracht="Noteer of de vraag over bruikbaarheid, betrouwbaarheid, representativiteit of presentatie gaat.",
             oefeningen=[
                 ("rij", [("Geeft de bron een antwoord op mijn vraag?", "bruikbaarheid"),
                          ("Had de maker er belang bij de zaken anders voor te stellen?", "betrouwbaarheid"),
                          ("Spreekt deze bron voor één mens of voor een hele groep?", "representativiteit"),
                          ("Is de foto bijgesneden voor ik ze te zien kreeg?", "presentatie")],
                  "Welk criterium?", WW),
             ]),
        dict(kop="Een bron ontleden",
             opdracht="Je krijgt een bron: een wervingsaffiche van een regering uit 1915 die jonge mannen oproept om dienst te nemen. Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Vraag", "Jouw antwoord"], [
                     ["Wie is het doelpubliek?", None],
                     ["Wat is de bedoeling?", None],
                     ["Waarvoor is deze bron bruikbaar?", None],
                     ["Waarvoor niet?", None],
                 ], "Doelpubliek: jonge mannen die nog niet in het leger zitten · Bedoeling: overtuigen en "
                    "tot handelen aanzetten · Bruikbaar voor: wat men in 1915 wilde laten geloven en hoe "
                    "men de oorlog voorstelde · Niet bruikbaar voor: hoe het er aan het front werkelijk "
                    "aan toeging", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een secundaire bron is altijd minder waard dan een primaire bron.", False),
                 ("waar", "Of een bron primair of secundair is, hangt mee af van de vraag die je stelt.", True),
                 ("waar", "Een bron die propaganda is, is onbruikbaar voor een historicus.", False),
                 ("waar", "Een bron die kort na de gebeurtenis gemaakt werd, is daarom betrouwbaar.", False),
                 ("waar", "Van arme en ongeletterde groepen zijn minder geschreven bronnen bewaard.", True),
             ]),
        dict(kop="Het stappenplan",
             opdracht="Zet de stappen in de juiste volgorde: schrijf 1 tot 4.",
             oefeningen=[
                 ("rij", [("elke bron interpreteren en beoordelen", "3"),
                          ("de context van elke bron verzamelen", "1"),
                          ("een beargumenteerd antwoord formuleren", "4"),
                          ("de inhoud van elke bron lezen of bekijken", "2")], "Volgorde?", "58px"),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Twee bronnen over dezelfde staking spreken elkaar tegen. Beschrijf stap voor "
                          "stap wat je doet.",
                  "Eerst zoek je van elke bron de maker, de datum en de bedoeling. Dan vraag je je af of "
                  "de maker er belang bij had het zo voor te stellen: een krant van de werkgevers en een "
                  "pamflet van de vakbond staan niet op dezelfde plek. Daarna kijk je waar ze het wél over "
                  "eens zijn, want dat staat steviger. Ten slotte verwoord je het verschil zelf: beide "
                  "zagen dezelfde staking, van een andere kant.", 6),
                 ("open", "Een foto van een betoging wordt zo bijgesneden dat enkel de drukste hoek te "
                          "zien is. Is er iets vervalst? Verklaar.",
                  "Niets op de foto is vervalst: alles wat je ziet, is er echt geweest. Toch klopt het "
                  "beeld niet meer, want de betoging lijkt veel groter dan ze was. Dat is een kwestie van "
                  "presentatie, en daarom vraag je bij elke afbeelding of je het hele kader ziet.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-beeldvorming-vergelijken-en-verleden-heden-toekomst-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Beeldvorming, vergelijken en verleden-heden-toekomst",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke redeneerwijze?",
             opdracht="Schrijf de naam van de redeneerwijze in het vakje.",
             oefeningen=[
                 ("rij", [("je legt uit waarom de crisis van 1929 tot de machtsovername bijdroeg",
                           "oorzaak en gevolg benoemen"),
                          ("je zegt dat ook gewone ambtenaren meewerkten", "menselijke actoren benoemen"),
                          ("je legt een verband met de wereld van vandaag", "actualiseren")],
                  "Welke redeneerwijze?", WL),
                 ("rij", [("je begrijpt een gebeurtenis vanuit haar eigen tijd", "historisch contextualiseren"),
                          ("je legt de kant van de kolonisator naast die van de gekoloniseerde",
                           "meerdere perspectieven hanteren"),
                          ("je zoekt wat al die eeuwen hetzelfde bleef", "continuïteit en verandering benoemen")],
                  "Welke redeneerwijze?", WL),
             ]),
        dict(kop="Bedoeld of onbedoeld gevolg?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Het Marshallplan hielp Europa heropbouwen.", ["bedoeld", "onbedoeld"], 0),
                 ("kies", "Het Marshallplan zette Europa stevig in het westerse kamp vast.",
                  ["bedoeld", "onbedoeld"], 1),
                 ("kies", "Het Verdrag van Versailles hield het Duitse leger klein.",
                  ["bedoeld", "onbedoeld"], 0),
                 ("kies", "Het Verdrag van Versailles werd een voedingsbodem voor extreme partijen.",
                  ["bedoeld", "onbedoeld"], 1),
             ]),
        dict(kop="Veralgemening, stereotypering of geen van beide?",
             opdracht="Noteer in het vakje.",
             oefeningen=[
                 ("rij", [("Afrikanen zijn van nature onwetend.", "stereotypering"),
                          ("Uit drie dagboeken blijkt dat alle soldaten bang waren.", "veralgemening"),
                          ("In 1961 bouwde de DDR de Berlijnse Muur.", "geen van beide")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Welk vergelijkingspunt?",
             opdracht="Noteer of het een politiek, sociaal, cultureel of economisch kenmerk is.",
             oefeningen=[
                 ("rij", [("slavernij", "sociaal"), ("de staatsvorm", "politiek"),
                          ("propaganda", "cultureel"), ("arbeidsorganisatie", "economisch"),
                          ("migratie", "sociaal"), ("levensbeschouwing", "cultureel")],
                  "Welke groep?", W),
             ]),
        dict(kop="Collectieve herinnering",
             opdracht="Kruis aan of het een aanwijzing is dat iets een collectieve herinnering is.",
             oefeningen=[
                 ("waar", "Er wordt jaarlijks op een vaste dag bij stilgestaan.", True),
                 ("waar", "Er staan monumenten voor in de openbare ruimte.", True),
                 ("waar", "Er bestaat precies één bron over.", False),
                 ("waar", "Een hele groep deelt er een gevoel en een betekenis over.", True),
             ]),
        dict(kop="De democratische rechtsstaat",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Jouw antwoord"], [
                     ["Noem twee principes van een democratische rechtsstaat.", None],
                     ["Noem één beperking in de praktijk.", None],
                     ["Noem twee manieren waarop jij zelf verantwoordelijkheid kan opnemen.", None],
                 ], "Principes: scheiding der machten met onafhankelijke rechters, vrije verkiezingen, "
                    "grondrechten die ook de overheid binden · Beperking: niet iedereen wordt even goed "
                    "vertegenwoordigd, of trage procedures · Verantwoordelijkheid: gaan stemmen, je "
                    "informeren, lid worden van een vereniging, een petitie tekenen, naar een "
                    "inspraakavond gaan", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom twee historici met dezelfde bronnen tot een verschillend beeld "
                          "kunnen komen.",
                  "Een beeld van het verleden is altijd een constructie: iemand selecteert bronnen, leidt "
                  "er informatie uit af, interpreteert en zoekt samenhang. Elk van die stappen is een "
                  "keuze, en die keuze hangt samen met de vraag die de historicus stelt en met zijn eigen "
                  "standplaats. Pas als een beeld de bronnen tegenspreekt, is er echt iets mis.", 5),
                 ("open", "Een fragment uit een schoolboek van 1960 noemt de lokale bevolking van een "
                          "kolonie onwetend en lui. Wat analyseer je, en wat besluit je?",
                  "Je analyseert de stereotypering: een vast en vereenvoudigd beeld van een hele groep. "
                  "Je besluit dat de zin niets betrouwbaars zegt over die bevolking, maar wel veel over "
                  "de maker en over wat men in België in 1960 aan kinderen leerde. Zulke beelden "
                  "rechtvaardigden de kolonisatie, en ze werken door in hoe een generatie naar Afrika "
                  "bleef kijken.", 6),
                 ("open", "Waarom bestudeer je het verleden als je over de toekomst wil nadenken?",
                  "Niet om te voorspellen, want dat kan geschiedenis niet. Wel om processen te herkennen "
                  "die vandaag opnieuw aan het werk zijn: hoe propaganda werkt, hoe een crisis een "
                  "samenleving splijt, hoe rechten verworven en weer verloren raken.", 4),
             ]),
    ],
)

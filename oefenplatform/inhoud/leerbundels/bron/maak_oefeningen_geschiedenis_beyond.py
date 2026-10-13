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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-het-historisch-referentiekader-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke gebeurtenis een jaartal dat je wel kent, en kijk dan tussen welke "
                   "twee scharnierpunten dat valt. De zeven periodes volgen op elkaar, dus hoef je "
                   "er maar één goed te hebben om de rest te plaatsen.",
            waarom=[
                "Let op de boekdrukkunst: rond 1450, dus vroegmoderne tijd. Dat is zelf een van de "
                "scharnierpunten, samen met 1492 en de val van Constantinopel in 1453.",
                "Let op de Belgische onafhankelijkheid: 1830, dus de moderne tijd en niet de "
                "hedendaagse. De hedendaagse tijd begint pas rond 1945.",
            ],
        ),
        dict(
            aanpak="Vraag je af of het begrip iets zegt over wanneer of over waar. De woorden op "
                   "-aal en -iem gaan bijna altijd over de ruimte.",
            waarom=[
                "Let op duur: dat gaat over hoe lang iets aanhoudt, dus tijd. Ruraal betekent "
                "landelijk en maritiem heeft met de zee te maken, dus beide ruimte.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: blijft iets hetzelfde of wordt het anders. Woorden als "
                   "eeuwenlang en nooit vervangen wijzen op continuïteit, woorden als verdwijnt en "
                   "vervangt op verandering.",
            waarom=[
                None,
                None,
                None,
                "Let op dat de grondwet wel vaak gewijzigd is, maar nooit helemaal vervangen. Dat ze "
                "intussen anders leest en toch dezelfde grondwet is, is precies wat continuïteit "
                "betekent.",
            ],
        ),
        dict(
            aanpak="De vier domeinen zijn het politieke, het economische, het sociale en het "
                   "culturele. Vraag je af waar de kern van de gebeurtenis zit, niet wat er allemaal "
                   "mee te maken heeft.",
            waarom=[
                "Let op dat bijna elke gebeurtenis in meerdere domeinen speelt. De leerplicht is ook "
                "sociaal en politiek, maar onderwijs hoort in de eerste plaats bij het culturele "
                "domein, en dat is wat gevraagd wordt.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over één idee: een periodisering is iets wat historici "
                   "achteraf maken. Vraag je bij elke af of ze dat respecteert.",
            waarom=[
                None,
                "Niet waar: een periodisering maak je achteraf. Wie in 1500 leefde, wist niet dat "
                "hij in de vroegmoderne tijd leefde.",
                None,
                "Niet waar: een scharnierpunt kan ook economisch of cultureel zijn, zoals de "
                "boekdrukkunst of de industriële revolutie. Enkel politieke scharnierpunten nemen is "
                "zelf al een keuze.",
                "Niet waar: wat voor Europa een breuk is, betekent elders vaak niets. Het jaar 1492 "
                "is een scharnierpunt vanuit Europa gezien, niet vanuit China.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een oordeel over een woordkeuze of over een blik. Zeg "
                   "telkens welk oordeel er al in de term of in de keuze verstopt zit.",
            waarom=[
                "Noem dat het oordeel al in het woord zit. Donker betekent achterlijk, en wie die "
                "naam gebruikt, meet de middeleeuwen met de maatstaf van zijn eigen tijd.",
                "Noem dat elke periodisering een constructie is. De Chinese indeling kiest andere "
                "kenmerken, en ze is pas fout als ze de bronnen tegenspreekt.",
                "Noem ook wat je zou toevoegen, want dat is uitdrukkelijk gevraagd. De blik is "
                "ruimtelijk beperkt en etnocentrisch, en de gekoloniseerde gebieden hoorden in "
                "dezelfde eeuw thuis.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-restauratie-revolutie-en-het-ontstaan-van-belgie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer bij elke naam één ding dat hij deed en bij elk begrip één voorbeeld. Dan "
                   "kan je hem altijd terugvinden, ook als de vraag anders gesteld is.",
            waarom=[
                "Let op het verschil tussen Metternich en Bismarck: de eerste verdedigde de oude orde "
                "op het Congres van Wenen van 1815, de tweede smeedde een halve eeuw later het "
                "Duitse Keizerrijk.",
                "Let op het unionisme: dat katholieken en liberalen samen bestuurden, was in 1830 "
                "uitzonderlijk, want in de rest van Europa stonden ze tegenover elkaar. Dat "
                "bondgenootschap tegen Willem I hield maar een vijftiental jaar.",
            ],
        ),
        dict(
            aanpak="Vraag je af of er iets samenkomt of iets wegbreekt. Smelten samen en vormen "
                   "samen zijn verbindend, zich losmaken en afscheiden zijn ontbindend.",
            waarom=[
                None,
                None,
                None,
                "Let op dat België uit ontbindend nationalisme ontstaan is, terwijl Italië en "
                "Duitsland uit verbindend nationalisme ontstonden. Dezelfde gedachte levert dus twee "
                "tegengestelde bewegingen op.",
            ],
        ),
        dict(
            aanpak="Vier jaartallen om vast te zetten: 1815, 1830, 1831 en 1871. Ze liggen in die "
                   "orde en de drie eerste volgen vlak op elkaar.",
            waarom=[
                "Let op het verschil tussen 1830 en 1831: de opstand is van september 1830, de "
                "grondwet van februari 1831. Een nieuwe staat heeft dus een paar maanden nodig om "
                "zijn spelregels op papier te krijgen.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat Wenen wel en niet meenam, wat de "
                   "grondwet van 1831 regelde, en hoe los de Duitse Bond was.",
            waarom=[
                "Niet waar: in Wenen keek men naar het evenwicht tussen de grote mogendheden, niet "
                "naar de taal of de wens van de bevolking. Precies daarom brak het nationalisme later "
                "overal door.",
                None,
                "Niet waar: het Frans was in 1831 de taal van het bestuur en de rechtbanken, ook in "
                "Vlaanderen. Dat werd pas in de twintigste eeuw stap voor stap gewijzigd.",
                None,
                "Niet waar: de Duitse Bond was een los verband van staten, zonder gezamenlijke "
                "regering. Pas in 1871 kwam er één keizerrijk.",
            ],
        ),
        dict(
            aanpak="Zoek bij elk grief de kern: gaat het over taal, over macht of over geld. Taal is "
                   "cultureel, zetels zijn politiek, handel is economisch.",
            waarom=[
                "Let op het laatste grief: het Zuiden was geïndustrialiseerd en wilde "
                "invoerrechten, het Noorden leefde van de handel en wilde vrijhandel. Dat is een "
                "economisch belangenconflict en geen ruzie over taal.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een verband of een bedoeling. Zeg telkens wie wat te "
                   "winnen had, of wat een plaats symboliseerde.",
            waarom=[
                "Noem dat beide zich tegen de orde van Wenen keerden. De liberalen wilden een "
                "grondwet, de nationalisten een eigen staat, en in beide gevallen moest de oude "
                "dynastie macht afstaan.",
                "Noem beide kanten: vernedering van de verliezer en machtsvertoon. En noem de "
                "omkering van 1919, want juist die terugkeer naar dezelfde zaal maakt het voorbeeld "
                "zo sterk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-industrialisatie-en-de-sociale-kwestie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: welke energiebron zit erachter. Steenkool en stoom horen bij "
                   "de eerste, elektriciteit en aardolie bij de tweede.",
            waarom=[
                "Let op het stoomschip: dat hoort bij de eerste, want het draait op steenkool. De "
                "verbrandingsmotor hoort bij de tweede, want die draait op aardolie.",
            ],
        ),
        dict(
            aanpak="De primaire sector haalt grondstoffen uit de natuur, de secundaire verwerkt ze, "
                   "de tertiaire levert diensten. Vraag je af wat er uit de poort komt: een "
                   "grondstof, een product of een dienst.",
            waarom=[
                "Let op de mijnbouw: die haalt een grondstof uit de bodem, dus primair, ook al staat "
                "er zware machinerie. En een spoorwegmaatschappij maakt niets, ze vervoert, dus "
                "tertiair.",
            ],
        ),
        dict(
            aanpak="Een aanbodfactor maakt produceren mogelijk, een vraagfactor zorgt dat er kopers "
                   "zijn. Vraag je dus af of het over de kant van de fabriek of over de kant van de "
                   "markt gaat.",
            waarom=[
                None,
                None,
                "Let op dat kapitaal een aanbodfactor is: het maakt het bouwen van een fabriek "
                "mogelijk. Grondstoffen, kapitaal, arbeid en kennis staan alle vier aan de "
                "aanbodkant.",
                None,
            ],
        ),
        dict(
            aanpak="De drie antwoorden verschillen in twee dingen: wie de productiemiddelen bezit, "
                   "en of de verandering via revolutie of via wetten komt.",
            waarom=[
                "Let op het verschil tussen marxisme en sociaaldemocratie: het doel lag dicht bij "
                "elkaar, de weg niet. De eerste via revolutie, de tweede via verkiezingen en wetten.",
            ],
        ),
        dict(
            aanpak="Elk van de drie had een eigen doel: samen sparen tegen ziekte, samen "
                   "onderhandelen over loon, samen goedkoper kopen. Zoek dat doel in de zin.",
            waarom=[
                "Let op de coöperatie: samen een winkel of bakkerij uitbaten, met de winst voor de "
                "leden. In België zijn uit die drie zuilen de ziekenfondsen, de vakbonden en de "
                "warenhuizen van de beweging gegroeid.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat de grondwet van 1831 wel en niet "
                   "regelde, hoe het stemrecht uitbreidde, en hoe de sectoren verschoven.",
            waarom=[
                "Niet waar: de grondwet van 1831 zei niets over kinderarbeid. De eerste echte "
                "kinderarbeidwet kwam er pas in 1889, dus bijna zestig jaar later.",
                None,
                "Waar: wie bezit of een diploma had, kreeg een of twee stemmen extra, met een "
                "maximum van drie. Het algemeen enkelvoudig stemrecht voor mannen kwam er pas in "
                "1919.",
                "Niet waar: het aandeel van de landbouw daalde juist, terwijl de industrie en later "
                "de diensten groeiden. Dat is de verschuiving van de primaire naar de secundaire "
                "sector.",
                None,
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een begrip met een voorbeeld, en een oorzaak. Noem "
                   "telkens het mechanisme en niet enkel het gevolg.",
            waarom=[
                "Noem ook een voorbeeld, zoals gevraagd. Proletarisering is het verlies van eigen "
                "werktuigen of grond, en de thuiswever die fabrieksarbeider wordt is het "
                "duidelijkste geval.",
                "Noem de werkmanskaarten op de trein. Daardoor kon een arbeider blijven wonen waar "
                "hij woonde, en daarom verliep de plattelandsvlucht in België trager dan elders.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-modern-imperialisme-congo-en-china-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie soorten motieven: geld, macht en een idee over de eigen beschaving. Vraag "
                   "je af wat men ermee wou winnen.",
            waarom=[
                "Let op het verschil tussen een vlootbasis en een afzetmarkt: de eerste dient de "
                "macht, de tweede de handel. Prestige is politiek, ook al kost het geld.",
            ],
        ),
        dict(
            aanpak="De middelen zijn technisch: een geneesmiddel, een vervoermiddel en een wapen. "
                   "Zoek bij elke zin wat ze mogelijk maakte.",
            waarom=[
                "Let op kinine: zonder dat middel tegen malaria bleven Europeanen aan de kust. Juist "
                "daarom kwam de verovering van het binnenland pas in de negentiende eeuw op gang.",
            ],
        ),
        dict(
            aanpak="Het verschil zit in wie de eigenaar is. Tot 1908 was Congo het persoonlijke "
                   "bezit van Leopold II, daarna een kolonie van de Belgische staat.",
            waarom=[
                None,
                "Let op het drieluik van Belgisch Congo: staat, kerk en grote bedrijven bestuurden "
                "samen. Dat heet de koloniale drie-eenheid.",
                "Let op de rubberquota: die horen bij de Vrijstaat. De gruwel die daaruit volgde, "
                "was precies waarom de internationale druk ontstond en Leopold II het gebied in 1908 "
                "aan België moest overdragen.",
                None,
            ],
        ),
        dict(
            aanpak="Vergelijk op twee punten: hoeveel gebied men bezette, en of het land formeel "
                   "zelfstandig bleef. Daarin verschillen Congo en China volledig.",
            waarom=[
                "Let op dat China formeel een keizerrijk bleef met zijn eigen regering, terwijl "
                "Congo helemaal geen eigen staat meer had. Toch was China door de ongelijke "
                "verdragen zijn soevereiniteit grotendeels kwijt, en dat heet informeel "
                "imperialisme.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe ver de verdeling van Afrika ging, wie "
                   "er allemaal aan meedeed, en het verschil tussen de feiten en onze blik erop.",
            waarom=[
                None,
                "Niet waar: de Verenigde Staten namen onder meer de Filipijnen en Puerto Rico, en "
                "oefenden grote invloed uit in Midden-Amerika. Imperialisme was niet enkel "
                "Europees.",
                "Waar: Japan moderniseerde na 1868 in snel tempo en bezette daarna onder meer Taiwan "
                "en Korea. Een land kan dus van bedreigd gebied tot koloniale macht worden.",
                "Niet waar: China werd niet gekoloniseerd maar in invloedssferen verdeeld, met "
                "ongelijke verdragen en havensteden onder vreemd gezag.",
                "Niet waar: de feiten blijven dezelfde, de vragen die men eraan stelt veranderen. "
                "Dat is het verschil tussen het verleden en de geschiedschrijving erover.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een uitleg en een bronkritiek. Zeg bij de bron altijd "
                   "eerst waarover ze wél iets zegt.",
            waarom=[
                "Noem de schrik voor elkaar en de afspraak van Berlijn. Dat je een gebied werkelijk "
                "moest bezetten om er aanspraak op te maken, is precies wat de wedloop aanjoeg.",
                "Noem beide kanten, zoals gevraagd. Over het leven in de kolonie zegt de affiche "
                "niets, over de beeldvorming in Europa alles; juist dat maakt haar een goede bron "
                "voor de juiste vraag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-eerste-wereldoorlog-en-de-russische-revoluties-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een aanleiding is de vonk, een diepere oorzaak is het kruit dat er al lag. Vraag "
                   "je af of iets jaren of dagen voor de oorlog speelde.",
            waarom=[
                "Let op dat de moord in Sarajevo de aanleiding is en niet de oorzaak. Zonder de "
                "bewapening, de bondgenootschappen en het nationalisme was die moord een misdaad "
                "gebleven en geen wereldoorlog geworden.",
                None,
                "Let op het web van bondgenootschappen: daardoor sleepte één conflict op de Balkan "
                "heel Europa mee. Dat mechanisme is wat men de kettingreactie van 1914 noemt.",
                None,
            ],
        ),
        dict(
            aanpak="Drie data om vast te zetten: 1917 voor de Russische revoluties, 11 november 1918 "
                   "voor de wapenstilstand, en 1920 voor de Volkenbond.",
            waarom=[
                "Let op het verschil tussen het Verdrag van Versailles en de Volkenbond: het verdrag "
                "is van 1919, de Volkenbond ging in 1920 van start. En de Oktoberrevolutie heet zo "
                "naar de oude Russische kalender; bij ons viel ze in november.",
            ],
        ),
        dict(
            aanpak="Totale oorlog betekent dat de hele samenleving meedoet, niet enkel het leger. "
                   "Zoek bij elk gegeven welk stuk van de samenleving ingezet werd.",
            waarom=[
                "Let op de drie kanten samen: mensen, meningen en economie. Een oorlog die ook de "
                "fabrieken, de voedselvoorziening en de pers inschakelt, raakt iedereen, en dat is "
                "precies wat het woord totaal bedoelt.",
            ],
        ),
        dict(
            aanpak="Versailles legde Duitsland vier dingen op: de schuld, het geld, het leger en het "
                   "grondgebied. Leer ze als vier vakjes, dan vergeet je er geen.",
            waarom=[
                "Let op het artikel over de schuld: juist dat werd in Duitsland het hardst "
                "aangevoeld, harder nog dan het geld. Daaruit groeide het woord dictaat van "
                "Versailles.",
            ],
        ),
        dict(
            aanpak="De Volkenbond beoordelen betekent naar zijn middelen kijken, niet naar zijn "
                   "bedoeling. De bedoeling was goed, de middelen waren zwak.",
            waarom=[
                "Waar: de Amerikaanse senaat weigerde het verdrag te bekrachtigen, dus bleef de "
                "Volkenbond zonder de machtigste staat van de wereld. Dat was een van zijn grootste "
                "zwaktes.",
                "Niet waar: de Volkenbond had geen eigen leger en kon enkel sancties afkondigen. "
                "Zonder dwangmiddel bleef elke beslissing afhankelijk van de goede wil van de "
                "leden.",
                "Waar, en dat was een tweede zwakte: elke beslissing vroeg eenparigheid, dus kon één "
                "land alles blokkeren. De Veiligheidsraad van de VN werkt daarom met een andere "
                "regel.",
                None,
            ],
        ),
        dict(
            aanpak="Zet de keten van 1917 in zijn logica: eerst de nood aan het front en in de "
                   "steden, dan de val van de tsaar, dan het falen van de voorlopige regering, dan "
                   "de Oktoberrevolutie.",
            waarom=[
                "Let op dat er in 1917 twee revoluties waren: in februari of maart viel de tsaar, in "
                "oktober of november namen de bolsjewieken de macht. Wie ze als één gebeurtenis "
                "ziet, mist de voorlopige regering ertussen.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een gevolg en een verband. Zeg bij een onbedoeld gevolg "
                   "altijd hoe het uit de bedoeling voortkwam.",
            waarom=[
                "Noem er één van elk, zoals gevraagd. Het bedoelde gevolg was Duitsland klein "
                "houden; het onbedoelde was dat juist de vernedering extreme partijen voedde.",
                "Noem alle drie de woorden apart en zeg waarop ze aansloten. Vrede op de oorlog, "
                "brood op de honger, land op de uitgestelde grondverdeling; juist drie punten waarop "
                "de voorlopige regering tekortschoot.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-interbellum-totalitarisme-en-crisis-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een oorzaak gaat vooraf aan de crash, een gevolg komt erna. Vraag je af of iets "
                   "de beurs kon doen crashen of pas na 1929 opduikt.",
            waarom=[
                "Let op aandelen kopen met geleend geld: dat blies de koersen op en is dus een "
                "oorzaak. Politieke radicalisering is een gevolg, en wel het gevolg dat de jaren "
                "dertig zou bepalen.",
            ],
        ),
        dict(
            aanpak="Drie regimes, drie namen, drie jaartallen. Zet ze naast elkaar, dan zie je dat "
                   "Italië het eerst was en Duitsland het laatst.",
            waarom=[
                "Let op dat Mussolini al in 1922 aan de macht kwam, elf jaar voor Hitler. Het "
                "fascisme was dus het model en niet de navolging.",
            ],
        ),
        dict(
            aanpak="Een totalitaire staat wil alles controleren: de partij, het nieuws, het "
                   "onderwijs en zelfs het denken. Vraag je bij elk kenmerk af of het die controle "
                   "versterkt of juist beperkt.",
            waarom=[
                None,
                None,
                "Niet waar: een onafhankelijke rechterlijke macht is juist het tegendeel van "
                "totalitair. In zo'n staat spreekt de rechter het vonnis dat het regime verwacht.",
                None,
                "Niet waar: propaganda en terreur gaan samen. De propaganda haalt de meelopers "
                "binnen, de terreur schakelt de rest uit.",
            ],
        ),
        dict(
            aanpak="Leer bij elk begrip het land waar het thuishoort. Collectivisatie en goelags "
                   "horen bij de Sovjet-Unie, de Mars op Rome bij Italië, de Machtigingswet bij "
                   "Duitsland.",
            waarom=[
                "Let op de collectivisatie: de boeren verloren hun grond aan staatsbedrijven, en het "
                "verzet daartegen kostte miljoenen mensen het leven, vooral door hongersnood.",
                "Let op de orde van de drie: de Rijksdagbrand van februari 1933 was de aanleiding "
                "voor de noodmaatregelen, en de Machtigingswet volgde in maart. Zo werd een "
                "verkiezingsuitslag in enkele weken een dictatuur.",
            ],
        ),
        dict(
            aanpak="Zet de vijf stappen op een tijdlijn van 1935 tot 1939. Elke stap gaat verder dan "
                   "de vorige, en geen enkele werd met geweld tegengehouden.",
            waarom=[
                "Let op de opbouw: dienstplicht in 1935, het Rijnland in 1936, Oostenrijk in de "
                "lente van 1938, München in de herfst van 1938, Polen in 1939. Dat elke stap "
                "onbeantwoord bleef, maakte de volgende makkelijker.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een verband, een vergelijking en een beoordeling. Zeg "
                   "bij een beoordeling ook wat de mensen van toen wisten.",
            waarom=[
                "Noem de keten en niet enkel het eindpunt. Werkloosheid en armoede, dan het verlies "
                "van vertrouwen in de bestaande partijen, dan de groei van de NSDAP, en in januari "
                "1933 het kanselierschap.",
                "Noem wat ze gemeen hebben en waar het verschil zit. Beide zijn totalitair, maar de "
                "rassenleer en het antisemitisme staan enkel bij het nationaalsocialisme centraal, en "
                "die leiden tot de vernietiging.",
                "Noem ook wat toen zwaar woog, want anders oordeel je enkel met de kennis van nu. "
                "Elke toegeving maakte Duitsland sterker, maar de herinnering aan de loopgraven "
                "maakte oorlog voor velen ondenkbaar.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-tweede-wereldoorlog-en-de-holocaust-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vergelijk de twee oorlogen op drie punten: hoe men vocht, waar men vocht en wie "
                   "het meest getroffen werd. Op alle drie verschillen ze sterk.",
            waarom=[
                "Let op de derde rij: in 14-18 waren de slachtoffers vooral militairen, in 40-45 "
                "vooral burgers. Dat verschil komt van de bombardementen op steden, de "
                "bezettingspolitiek en de genocide.",
            ],
        ),
        dict(
            aanpak="Een keerpunt is een slag waarna het initiatief van kant wisselt. Vraag je dus af "
                   "of de oorlog erna een andere richting nam.",
            waarom=[
                None,
                None,
                "Niet waar: de inval in Polen is het begin van de oorlog en dus geen keerpunt erin. "
                "Een begin kan geen keerpunt zijn.",
                "Waar: Midway is het keerpunt in de oorlog in de Stille Oceaan, zoals Stalingrad aan "
                "het oostfront en El Alamein in Noord-Afrika. Drie fronten, drie keerpunten, alle "
                "drie in 1942 of begin 1943.",
                "Niet waar: het Ardennenoffensief van de winter van 1944 was een laatste Duitse "
                "poging die mislukte. Het veranderde de richting van de oorlog niet meer.",
            ],
        ),
        dict(
            aanpak="Drie data om vast te zetten: 10 mei 1940 voor de inval in België, januari 1942 "
                   "voor Wannsee, 6 juni 1944 voor de landing.",
            waarom=[
                "Let op de Wannseeconferentie: daar werd in januari 1942 de organisatie van de "
                "vernietiging geregeld. De vervolging was toen al jaren bezig, dus is dat geen begin "
                "maar een beslissende stap.",
            ],
        ),
        dict(
            aanpak="Vraag je af wie er baat bij had: de bezetter of de bezette bevolking. En zeg bij "
                   "collaboratie ook van welke soort, want dat wordt uitdrukkelijk gevraagd.",
            waarom=[
                "Let op dat er verschillende soorten collaboratie bestonden: militair, economisch, "
                "politiek en bestuurlijk. Wie enkel collaboratie schrijft, geeft het antwoord maar "
                "half.",
            ],
        ),
        dict(
            aanpak="De vervolging ging in stappen: eerst uitsluiten, dan afzonderen, dan "
                   "vernietigen. Die orde is belangrijk, want elke stap maakte de volgende "
                   "mogelijk.",
            waarom=[
                "Let op dat de eerste stap wettelijk was en niet gewelddadig: beroepsverbod, "
                "registratie, uitsluiting uit scholen. Juist dat maakt het verhaal zo "
                "verontrustend.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wanneer het woord genocide ontstond, wat er "
                   "in België gebeurde, en dat de werkelijkheid grijzer was dan twee kampen.",
            waarom=[
                "Niet waar: het woord genocide is in 1944 bedacht door de jurist Raphael Lemkin, en "
                "het werd pas in 1948 in een verdrag van de VN vastgelegd. Het begrip komt dus uit "
                "de oorlog en ging er niet aan vooraf.",
                None,
                None,
                "Niet waar: tussen collaboratie en verzet lag een breed grijs gebied. De meeste "
                "mensen probeerden vooral te overleven, en veel keuzes werden pas achteraf "
                "beoordeeld.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een toepassing van een definitie en een afweging. Begin "
                   "bij de definitie zelf en pas ze dan toe.",
            waarom=[
                "Noem eerst de definitie en pas ze dan toe. Opzet en planmatige organisatie zijn de "
                "twee kernen; de dienstregeling van de treinen is daarvan het pijnlijkste bewijs.",
                "Noem wat cijfers niet kunnen. Ze tonen de omvang maar niet de ervaring, en nu de "
                "laatste getuigen wegvallen, moeten onderwijs en archieven dat overnemen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-een-nieuwe-wereldorde-vn-koude-oorlog-en-europa-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de twee naast elkaar: 1920 tegen 1945, zonder de Verenigde Staten tegen met "
                   "een Veiligheidsraad. De VN is uit de fouten van de Volkenbond geleerd.",
            waarom=[
                "Let op het vetorecht: dat bestond bij de Volkenbond niet, want daar moest iedereen "
                "het eens zijn. De VN gaf vijf landen een veto, en dat is een andere zwakte maar wel "
                "een werkbare.",
            ],
        ),
        dict(
            aanpak="Vraag je af of het kenmerk de VN helpt werken of juist blokkeert. Spreken en "
                   "helpen zijn sterktes, geen leger en een veto zijn zwaktes.",
            waarom=[
                None,
                "Let op dat het veto zowel een zwakte als de prijs van de deelname is: zonder dat "
                "recht waren de grote mogendheden nooit toegetreden. Precies dat hield de VN "
                "overeind waar de Volkenbond uiteenviel.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Zet de Koude Oorlog op één tijdlijn van 1948 tot 1991. De crisissen komen in "
                   "golven, met Berlijn aan het begin en Berlijn aan het einde.",
            waarom=[
                "Let op het verschil tussen 1948 en 1961: in 1948 was er de blokkade van Berlijn, in "
                "1961 de bouw van de Muur. Twee keer Berlijn, dertien jaar ertussen.",
                "Let op dat de Praagse Lente van 1968 neergeslagen werd en de val van de Muur van "
                "1989 niet. Datzelfde Oostblok reageerde in 1989 anders, en juist dat verschil "
                "maakte het einde mogelijk.",
            ],
        ),
        dict(
            aanpak="Drie verdragen, drie stappen: Rome voor de markt, Maastricht voor de Unie en de "
                   "euro, Lissabon voor de werking. Leer bij elk één kernwoord.",
            waarom=[
                "Let op dat Maastricht het woord Unie en de weg naar de euro bracht, terwijl de euro "
                "zelf pas in 2002 in de portefeuille zat. Een verdrag en de uitvoering ervan liggen "
                "vaak jaren uit elkaar.",
            ],
        ),
        dict(
            aanpak="Vier instellingen, vier rollen: voorstellen, verkiezen, de top, de ministers. De "
                   "twee met Raad in hun naam zijn het makkelijkst te verwarren.",
            waarom=[
                "Let op het verschil tussen de Europese Raad en de Raad van de Europese Unie: de "
                "eerste brengt de staatshoofden en regeringsleiders samen, de tweede de vakministers. "
                "Enkel het Parlement wordt rechtstreeks verkozen.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een uitleg van een naam en een verband. Zeg telkens wat "
                   "men wou vermijden.",
            waarom=[
                "Noem dat de supermachten nooit rechtstreeks tegen elkaar vochten, en noem er een "
                "paar van de oorlogen die wel gevoerd werden. Koud betekent niet zonder "
                "slachtoffers.",
                "Noem dat men juist kolen en staal koos. De grondstoffen van de oorlog onder "
                "gezamenlijk beheer brengen was geen economische maar een vredespolitieke keuze.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dekolonisatie-en-de-wereld-van-vandaag-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De oorzaken van de dekolonisatie liggen op twee plaatsen tegelijk: in Europa, "
                   "dat zwakker uit de oorlog kwam, en in de koloniën zelf, waar bewegingen "
                   "ontstonden.",
            waarom=[
                None,
                "Waar, en let op het detail: die leiders waren vaak in Europa opgeleid. De "
                "kolonisator leverde zo zelf de taal en de ideeën waarmee de onafhankelijkheid "
                "geëist werd.",
                "Niet waar: de beweging ging juist de andere kant op. Deze bewering draait oorzaak "
                "en gevolg om, en zulke omkeringen zijn een klassieke valstrik.",
                None,
            ],
        ),
        dict(
            aanpak="Drie begrippen die op elkaar lijken maar over iets anders gaan: economische "
                   "macht, politieke keuze, en onze eigen manier van spreken.",
            waarom=[
                "Let op neokolonialisme: het land is politiek vrij maar economisch afhankelijk, via "
                "leningen, prijzen en bedrijven. Daarom spreekt men van een nieuwe vorm en niet van "
                "een voortzetting.",
            ],
        ),
        dict(
            aanpak="Vijf jaartallen om vast te zetten: 1959, 1960, 1961, 1965 en 1997. Ze vertellen "
                   "samen het verhaal van een land dat zijn onafhankelijkheid nauwelijks kon "
                   "beleven.",
            waarom=[
                "Let op hoe dicht de eerste drie op elkaar volgen: de rellen in 1959, de "
                "onafhankelijkheid op 30 juni 1960, de moord op Lumumba in januari 1961. Binnen "
                "twee jaar was de eerste eerste minister dood.",
            ],
        ),
        dict(
            aanpak="Drie namen, drie rollen: de eerste regeringsleider, de man die 32 jaar bleef, en "
                   "wie hem verdreef. Leer bij elk één jaartal.",
            waarom=[
                "Let op dat Mobutu het land Zaïre noemde, en de rivier en de munt ook. Zo'n "
                "naamsverandering is zelf een politieke daad: ze hoort bij wat hij authenticiteit "
                "noemde.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe gewelddadig de dekolonisatie was, wat "
                   "er in 1960 gebeurde, en hoe de blik op het verleden verschoof.",
            waarom=[
                "Niet waar: Algerije, Kenia, Angola en Mozambique vochten lange en bloedige "
                "oorlogen. Dat sommige landen vreedzaam onafhankelijk werden, geldt dus niet voor "
                "alle.",
                "Waar: 1960 heet daarom het Afrikaanse jaar. Zeventien koloniën in twaalf maanden is "
                "een tempo dat niemand in Europa had voorzien.",
                None,
                "Niet waar: in het oosten van Congo woeden nog altijd gewapende conflicten, mede "
                "gevoed door de grondstoffen. De onafhankelijkheid maakte daar geen einde aan.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een verband, een rol en een actualiteit. Noem telkens "
                   "concrete feiten in plaats van een algemene zin.",
            waarom=[
                "Noem dat de supermachten elke nieuwe staat als een stem en een plek zagen. Dat ze "
                "daarbij dictators steunden, hoort er uitdrukkelijk bij; Mobutu is het bekendste "
                "voorbeeld.",
                "Noem er twee, zoals gevraagd. De onvoorbereide overgang in vijf maanden en de steun "
                "aan de afscheiding van Katanga zijn de twee die het sterkst gedocumenteerd zijn.",
                "Noem de keten over de eeuwen: eerst rubber en ivoor, dan koper en uranium, nu "
                "kobalt en coltan. Dat dezelfde ondergrond telkens opnieuw de inzet is, is het punt "
                "van de vraag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-belgie-na-1945-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie breuklijnen: over geloof en vrijzinnigheid, over arbeid en kapitaal, en "
                   "over de taalgemeenschappen. Zoek bij elk voorbeeld waarover de ruzie echt gaat.",
            waarom=[
                "Let op Leuven Vlaams: dat lijkt over onderwijs te gaan, maar de inzet was de taal "
                "van de universiteit en dus communautair. Waarover de ruzie gaat, is niet altijd "
                "wat er in de naam staat.",
            ],
        ),
        dict(
            aanpak="Vuistregel: de gemeenschappen gaan over mensen en cultuur, de gewesten over "
                   "grond en economie, en de rest blijft federaal. Vraag je af of de bevoegdheid "
                   "over personen of over plaatsen gaat.",
            waarom=[
                "Let op het paar onderwijs en cultuur tegenover ruimtelijke ordening en leefmilieu: "
                "de eerste twee gaan over mensen, dus gemeenschap, de laatste twee over grond, dus "
                "gewest. Leger en justitie zijn federaal gebleven.",
            ],
        ),
        dict(
            aanpak="Drie rondes om vast te zetten: 1970 de eerste, 1993 de federale staat, en de "
                   "zesde rond 2011 tot 2014. Leer bij elk één kernwoord.",
            waarom=[
                "Let op 1993: sinds die ronde zegt artikel 1 van de grondwet dat België een federale "
                "staat is, en worden de deelparlementen rechtstreeks verkozen. Dat is de grootste "
                "stap van de zes.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de sociale zekerheid, de verhouding tussen "
                   "de niveaus, en de zuilen. Vraag je bij elke af welk van de drie.",
            waarom=[
                None,
                "Niet waar: een decreet en een federale wet staan juridisch op gelijke hoogte. Er is "
                "geen hiërarchie tussen de niveaus, en bij een conflict beslist het Grondwettelijk "
                "Hof.",
                "Waar: in Vlaanderen zijn gewest en gemeenschap samengevoegd, in Wallonië en Brussel "
                "niet. Daarom is de Belgische structuur aan de twee kanten niet symmetrisch.",
                "Niet waar: de zuilen zijn afgezwakt maar niet verdwenen. Ziekenfondsen, vakbonden, "
                "scholennetten en ziekenhuizen dragen nog altijd hun herkomst mee.",
                "Waar: Vlaanderen stemde in meerderheid voor de terugkeer van Leopold III, Wallonië "
                "en Brussel tegen. Juist die verschillende uitslag maakte de koningskwestie tot een "
                "communautaire zaak.",
            ],
        ),
        dict(
            aanpak="Let op de namen van de wetten per niveau: een decreet in Vlaanderen en Wallonië, "
                   "een ordonnantie in Brussel, een wet federaal.",
            waarom=[
                "Let op de ordonnantie: Brussel heeft een eigen naam voor zijn regels, en dat hangt "
                "samen met zijn bijzondere positie als tweetalig gewest en hoofdstad.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een verband tussen een breuklijn en een debat. Noem de "
                   "breuklijn met haar naam en zeg wie tegenover wie staat.",
            waarom=[
                "Kies één debat en noem de breuklijn erbij. Welk debat je kiest maakt niet uit, "
                "zolang je kan zeggen wie tegenover wie staat en waarover.",
                "Noem de communautaire breuklijn en het mechanisme erachter. Dat de nationale "
                "partijen in de jaren zestig splitsten, is de reden dat geen partij nog kiezers in "
                "beide landsdelen moet overtuigen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-denken-kunst-en-emancipatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de jaartallen op één tijdlijn van 1948 tot 2003. Zo zie je dat de wettelijke "
                   "stappen vaak decennia na de eerste eisen komen.",
            waarom=[
                "Let op het verschil tussen 1948 en 1966: in 1948 kwam het stemrecht, en bijna twintig "
                "jaar later moesten vrouwen bij FN Herstal nog staken voor gelijk loon voor gelijk "
                "werk. Een politiek recht is dus niet hetzelfde als een economische gelijkheid.",
                "Let op dat 1990 de abortuswet is: niet alles toegelaten, maar uit het strafrecht "
                "onder voorwaarden. En 1963 ligt vóór de twee andere; de mars op Washington "
                "beïnvloedde de hele westerse wereld.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoever de gelijkheid vandaag staat, wat de "
                   "wet vroeger zei, en dat een beweging nooit uit één stem bestaat.",
            waarom=[
                "Niet waar: er blijft een loonkloof, vooral door deeltijds werk, de keuze van "
                "sectoren en de loopbaanonderbreking na de geboorte van een kind. Gelijk loon voor "
                "gelijk werk staat wel in de wet.",
                "Waar: pas met de wet van 1976 verdween de man als wettelijk hoofd van het gezin. "
                "Tot dan had hij onder meer het laatste woord over de woonplaats.",
                "Niet waar: naast Martin Luther King stonden stemmen als Malcolm X en de Black "
                "Panthers, die geweldloosheid niet als enige weg zagen. Een beweging is bijna altijd "
                "verdeeld over haar middelen.",
                None,
            ],
        ),
        dict(
            aanpak="Leer elke stroming aan één beeld: reclamebeelden bij popart, spontane vlekken "
                   "bij Cobra, bedrog van het oog bij optical art, en het idee alleen bij "
                   "conceptuele kunst.",
            waarom=[
                "Let op dat Cobra uit 1948 komt en de naam een samentrekking is van Kopenhagen, "
                "Brussel en Amsterdam. Bij conceptuele kunst kan het werk zelfs enkel uit een "
                "instructie bestaan.",
            ],
        ),
        dict(
            aanpak="Drie kunstenaars, drie handelsmerken: de reeks, de drukstip, en het reuzenformaat. "
                   "Leer bij elk één werk.",
            waarom=[
                "Let op wat ze gemeen hebben: alle drie halen ze hun beeld uit de "
                "consumptiemaatschappij. Het verschil zit in de techniek, niet in het onderwerp.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: dient die groep een lijst in bij verkiezingen. Zo niet, dan is "
                   "het een beweging, hoe groot ze ook is.",
            waarom=[
                None,
                None,
                "Let op dat een beweging wel invloed op de politiek heeft zonder zelf op te komen. De "
                "klimaatmarsen zetten het thema hoog op de agenda zonder ooit één zetel te vragen.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een verband met de tijd. Noem bij de kunst de wereld die "
                   "ze toont, en bij de emancipatie concrete jaartallen.",
            waarom=[
                "Noem de naoorlogse welvaart en de massaproductie. Zonder reclame, merken en "
                "supermarkten heeft de popart geen onderwerp, en zou ook haar ironie nergens op "
                "slaan.",
                "Kies één voorbeeld en zet er jaartallen bij. Dat een recht eerst denkbaar, dan "
                "bespreekbaar en pas daarna wet wordt, is wat de vraag met generaties bedoelt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-redeneren-met-historische-bronnen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een onderzoekbare vraag is afgebakend in tijd, ruimte en domein, en je kan ze "
                   "met bronnen beantwoorden. Vraag je dus af of de vraag een jaartal, een plaats en "
                   "een onderwerp heeft.",
            waarom=[
                None,
                "Niet onderzoekbaar: goed of slecht is een waardeoordeel en geen vraag die bronnen "
                "kunnen beantwoorden. Je kan wel onderzoeken hoe de levensverwachting of het loon "
                "van een bepaalde groep veranderde.",
                None,
                "Niet onderzoekbaar: vroeger is geen tijd en de mensen is geen groep. Zonder "
                "afbakening weet je niet welke bronnen je zou moeten zoeken.",
            ],
        ),
        dict(
            aanpak="Twee vragen per bron: komt ze uit de tijd zelf of erna, en in welke vorm is ze "
                   "bewaard. Je antwoord bestaat dus altijd uit twee woorden.",
            waarom=[
                "Let op het filmjournaal uit 1944: dat is een primaire bron ondanks de montage en de "
                "propaganda. Primair gaat over de tijd van ontstaan, niet over de betrouwbaarheid.",
            ],
        ),
        dict(
            aanpak="Vier criteria, vier verschillende vragen. Bruikbaarheid gaat over jouw vraag, "
                   "betrouwbaarheid over de maker, representativiteit over de groep, presentatie "
                   "over wie je de bron aanreikte.",
            waarom=[
                "Let op het verschil tussen betrouwbaarheid en representativiteit: een dagboek kan "
                "volkomen eerlijk zijn en toch maar voor één mens spreken. Eerlijk en "
                "representatief zijn twee aparte vragen.",
            ],
        ),
        dict(
            aanpak="Vraag je bij een affiche altijd eerst wie ze moest overtuigen. Daaruit volgen "
                   "haar bedoeling en waarvoor ze wel en niet bruikbaar is.",
            waarom=[
                "Let op de laatste twee vakjes: dat is de kern van bronkritiek. Een wervingsaffiche "
                "is een uitstekende bron over de beeldvorming en een slechte bron over het front "
                "zelf.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: dat primair niet beter betekent, dat de "
                   "vraag beslist hoe je een bron noemt, en dat propaganda ook een bron is.",
            waarom=[
                "Niet waar: een goede studie van 2020 kan veel betrouwbaarder zijn dan een pamflet "
                "uit 1916. Primair en secundair zeggen iets over de afstand tot de gebeurtenis, niet "
                "over de kwaliteit.",
                "Waar: een handboek uit 1960 is secundair over de oorlog en primair over hoe men in "
                "1960 over de oorlog sprak. Dezelfde bron, twee vragen, twee antwoorden.",
                "Niet waar: propaganda is een eersteklas bron, maar voor een andere vraag. Ze zegt "
                "weinig over de feiten en veel over wat men wilde laten geloven.",
                "Niet waar: vlak na de gebeurtenis kan iemand juist het meeste belang hebben om het "
                "zo voor te stellen. Nabijheid in tijd is geen bewijs van betrouwbaarheid.",
                None,
            ],
        ),
        dict(
            aanpak="Het stappenplan gaat van buiten naar binnen: eerst de context, dan de inhoud, "
                   "dan het oordeel, dan je eigen antwoord. Het oordeel komt nooit vóór het lezen.",
            waarom=[
                "Let op dat de context vooraan staat. Weet je niet wie de bron maakte en wanneer, "
                "dan kan je de inhoud niet goed interpreteren.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een werkwijze en een oordeel. Noem bij tegenspraak altijd "
                   "wat de twee bronnen wél delen.",
            waarom=[
                "Noem de stappen in orde en eindig bij wat ze samen opleveren. Twee tegenstrijdige "
                "bronnen zijn geen probleem maar twee perspectieven op dezelfde gebeurtenis.",
                "Noem dat niets vervalst is en toch het beeld niet klopt. Juist daarom is presentatie "
                "een apart criterium naast betrouwbaarheid.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-beeldvorming-vergelijken-en-verleden-heden-toekomst-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer elke redeneerwijze aan het woord dat ze typeert: waarom, wie, vandaag, in "
                   "hun eigen tijd, van twee kanten, en wat bleef hetzelfde.",
            waarom=[
                None,
                "Let op historisch contextualiseren: je begrijpt een daad vanuit de tijd zelf, maar "
                "begrijpen is niet goedkeuren. Dat verschil is precies waarom deze redeneerwijze "
                "nodig is.",
            ],
        ),
        dict(
            aanpak="Een bedoeld gevolg stond in het plan, een onbedoeld gevolg kwam erbij. Vraag je "
                   "af of de makers het zo gewild hebben.",
            waarom=[
                None,
                "Let op dat ook een onbedoeld gevolg goed kan uitkomen voor wie het plan maakte. "
                "Onbedoeld betekent niet ongewenst, enkel dat het niet het uitgesproken doel was.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Een veralgemening trekt uit te weinig gevallen een algemene conclusie, een "
                   "stereotypering plakt een vast beeld op een hele groep. Een feit met een jaartal "
                   "is geen van beide.",
            waarom=[
                "Let op het verschil: de eerste zin spreekt over een aard en is dus stereotyperend, "
                "de tweede trekt uit drie dagboeken een conclusie over allen en is dus "
                "veralgemenend. De derde noemt gewoon een feit.",
            ],
        ),
        dict(
            aanpak="Vier domeinen om te vergelijken: politiek, sociaal, economisch en cultureel. "
                   "Vraag je af of het over macht, over groepen, over werk en geld, of over "
                   "denken gaat.",
            waarom=[
                "Let op slavernij en migratie: beide gaan over de verhouding tussen "
                "bevolkingsgroepen, dus sociaal, ook al hebben ze zware economische kanten. Het "
                "gevraagde domein is telkens het hoofddomein.",
            ],
        ),
        dict(
            aanpak="Een collectieve herinnering is iets wat een hele groep samen betekenis geeft. "
                   "Zoek dus naar tekens van dat samen: een herdenking, een monument, een gedeeld "
                   "gevoel.",
            waarom=[
                None,
                None,
                "Geen aanwijzing: het aantal bronnen zegt niets over de collectieve herinnering. Van "
                "veel goed gedocumenteerde gebeurtenissen bestaat geen enkele herdenking.",
                None,
            ],
        ),
        dict(
            aanpak="Drie vakjes met drie verschillende soorten antwoord: de principes, waar het in "
                   "de praktijk wringt, en wat je zelf kan doen. Maak het laatste vakje concreet.",
            waarom=[
                "Let op dat de beperking niet betekent dat het systeem faalt. Een trage procedure is "
                "vaak de prijs van zorgvuldigheid, en juist daarom hoort de derde kolom erbij: wie "
                "iets wil veranderen, kan dat.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een oordeel over de geschiedschrijving zelf. Noem telkens "
                   "dat een beeld een constructie is en waar de grens ligt.",
            waarom=[
                "Noem de keten van keuzes: selecteren, interpreteren, samenhang zoeken. En noem de "
                "grens: een beeld dat de bronnen tegenspreekt, is wel fout.",
                "Noem beide delen, zoals gevraagd. Over de bevolking zegt die zin niets, over de "
                "maker en over het Belgische onderwijs van 1960 veel, en juist die beelden "
                "rechtvaardigden de kolonisatie.",
                "Noem dat het niet om voorspellen gaat. Je leert processen herkennen, en dat is iets "
                "anders dan weten wat er komt.",
            ],
        ),
    ],
)

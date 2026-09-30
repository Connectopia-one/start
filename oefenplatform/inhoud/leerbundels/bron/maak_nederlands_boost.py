# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor Nederlands op 🚀 Boost doorstroom-niveau.

Gebaseerd op de twee vakfiches Nederlands van de 2de graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Nederlands 1 gaat over
spreken, schrijven en interactie, Nederlands 2 over lezen, luisteren,
literatuur en taalbeschouwing. Allebei gelden ze voor economische
wetenschappen, humane wetenschappen, natuurwetenschappen en Latijn.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/nederlands.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, zodat het uploadscherm en dekking.py ze niet met een gelijknamig
hoofdstuk van ✨ Spark verwarren. De oefenbundels dragen daarbovenop het
voorvoegsel "oefenbundel-".

In elke bundel staat achteraan hetzelfde kader: spreken en gesprekken voeren
wegen samen 40 % van het examen Nederlands 1 en zijn precies het stuk dat je
niet achter een scherm leert. Kim vroeg daar uitdrukkelijk om op 30 september
2026. De opdracht in dat kader is telkens een andere, en hoort bij het thema
van de bundel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Nederlands"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def gesprek(opdracht):
    """Het vaste slotkader over oefenen in het echte leven."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je wat je moet <em>kennen</em>. Maar op het examen Nederlands 1 "
              "wegen <strong>spreken</strong> (10 %) en <strong>gesprekken</strong> (30 %) samen "
              "<strong>40 %</strong>, en dat leer je niet achter een scherm. Je leert het door het te doen, "
              "met echte mensen, die terugpraten, je onderbreken en niet altijd begrijpen wat je bedoelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en vraag daarna "
                  "aan de andere of je boodschap aankwam. Dat laatste is de helft van de oefening."),
    ])


# ───────────────────────── 1. Zender, ruis en de zeven tekstsoorten
BUNDELS["zender-ruis-en-de-zeven-tekstsoorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zender, ruis en de zeven tekstsoorten",
    onder="Het communicatiemodel met zijn acht elementen, en de zeven soorten teksten die je moet kunnen herkennen.",
    secties=[
        dict(kop="Het communicatiemodel", blokken=[
            ("p", "Elke tekst, elk filmpje en elk gesprek is een <strong>boodschap</strong> die iemand naar "
                  "iemand stuurt. Het <strong>communicatiemodel</strong> zet daar acht woorden op, en met die "
                  "acht kan je bijna elke tekst uit elkaar halen: <strong>zender</strong>, "
                  "<strong>boodschap</strong>, <strong>ontvanger</strong>, <strong>kanaal</strong>, "
                  "<strong>context</strong>, <strong>doel</strong>, <strong>effect</strong> en "
                  "<strong>ruis</strong>."),
            ("p", tabel(["Element", "Vraag die je stelt", "Voorbeeld"], [
                ["zender", "Wie stuurt dit?", "het bedrijf achter een reclamefilmpje"],
                ["boodschap", "Wat wordt er gezegd?", "dat je tien minuten later zal zijn"],
                ["ontvanger", "Voor wie is het bedoeld?", "je leerkracht"],
                ["kanaal", "Langs welke weg?", "een telefoongesprek, een mail, een blog"],
                ["context", "In welke situatie?", "je bus heeft vertraging"],
                ["doel", "Wat wil de zender bereiken?", "je laten stoppen met roken"],
                ["effect", "Wat gebeurt er echt?", "jij vindt het filmpje vooral grappig"],
                ["ruis", "Wat stoort onderweg?", "lawaai, een slechte verbinding, vermoeidheid"],
            ])),
            ("p", "Let op het verschil tussen <strong>doel</strong> en <strong>effect</strong>. Het doel is wat "
                  "de zender <em>wil</em>, het effect is wat er <em>werkelijk</em> gebeurt bij de ontvanger. "
                  "Die twee zijn zelden precies hetzelfde, en daarom staan ze apart in het model. Een "
                  "antirookfilmpje dat jou vooral doet lachen, heeft zijn doel gemist: het effect wijkt af "
                  "van het doel."),
            ("p", "Ook <strong>context</strong> staat er niet zomaar bij. Dezelfde zin betekent iets anders in "
                  "een andere situatie. 'Doe de deur dicht' klinkt anders van een vriend dan van een "
                  "directeur, en anders in de klas dan thuis. De context is de omringende situatie: de plaats, "
                  "het moment en de relatie tussen zender en ontvanger. Verwar hem niet met het kanaal, dat de "
                  "<em>drager</em> is."),
            ("kader", "Stuur je dezelfde boodschap eerst als spraakbericht en daarna als mail, dan verandert er "
                      "maar één ding: het <strong>kanaal</strong>. Zender, boodschap en ontvanger blijven "
                      "gelijk."),
        ]),
        dict(kop="Ruis: intern en extern", blokken=[
            ("p", "<strong>Ruis</strong> is alles wat maakt dat de boodschap niet of verkeerd aankomt. Ze zit "
                  "niet altijd buiten de mensen. Bij <strong>miscommunicatie</strong> kan de storing zowel bij "
                  "de zender als bij de ontvanger liggen."),
            ("p", "<strong>Externe ruis</strong> komt van buitenaf: lawaai op straat tijdens een gesprek, een "
                  "slechte verbinding bij een videogesprek, een vlek over de tekst van een brief, vreemde "
                  "tekens in een bericht. <strong>Interne ruis</strong> zit in de zender of de ontvanger zelf: "
                  "je bent moe en hoort maar de helft, je gedachten dwalen af, of je weet te weinig over het "
                  "onderwerp om te volgen. Het is dus <em>niet</em> waar dat ruis altijd buiten de zender en "
                  "de ontvanger zit."),
            ("weetje", "Ook op een scherm bestaat non-verbale communicatie. Wie een heel bericht in "
                       "<strong>hoofdletters</strong> typt, komt over als schreeuwerig en storend, ook al "
                       "bedoelde hij het niet zo. Dat is ruis die de zender zelf veroorzaakt."),
        ]),
        dict(kop="Wie is de zender, en wat wil hij?", blokken=[
            ("p", "De <strong>zender</strong> is wie de boodschap de wereld in stuurt, niet wie je op het "
                  "scherm ziet. Bij een reclamefilmpje is de zender het bedrijf dat het product wil verkopen, "
                  "ook al zie je alleen acteurs."),
            ("p", "Wat de zender wil, bepaalt wat hij weglaat. Een <strong>publireportage</strong> over een "
                  "sportdrank ziet eruit als een gewoon artikel, maar het echte doel is je het drankje laten "
                  "kopen. Een filmpje dat uitlegt hoe je brood bakt, wil je stap voor stap iets leren doen. "
                  "Dat er nergens een <strong>auteur</strong> vermeld staat, is altijd een reden om aan de "
                  "betrouwbaarheid te twijfelen: zonder zender kan je niet nagaan of die deskundig is of wat "
                  "hij met het bericht wil."),
            ("p", "Wil je het communicatiemodel op een tekst toepassen, stel dan deze vragen: <em>Wie is de "
                  "zender? Voor wie is de tekst bedoeld? Via welk kanaal is hij verspreid? Wat is het doel?</em> "
                  "Hoeveel strofen of alinea's de tekst telt, hoort daar níét bij: dat gaat over vorm, niet "
                  "over communicatie."),
        ]),
        dict(kop="De zeven tekstsoorten", blokken=[
            ("p", "Op het examen moet je zeven soorten lees- en luisterteksten kunnen herkennen. Je kijkt "
                  "daarvoor naar het <strong>hoofddoel</strong> van de zender, niet naar de vorm."),
            ("p", tabel(["Tekstsoort", "Wil vooral", "Voorbeelden"], [
                ["informatief", "informatie geven", "krantenartikel, stukje uit een leerboek, interview, reportage"],
                ["persuasief", "overtuigen of beïnvloeden", "reclamefilmpje, folder van een politieke partij, campagne tegen te snel rijden, propaganda, nepnieuws, publireportage"],
                ["opiniërend", "een mening geven", "recensie, hotelbeoordeling, reactie op een forum, productreview, protestlied"],
                ["prescriptief", "instructies geven", "handleiding, recept, bijsluiter, instructiefilmpje, schoolreglement, veiligheidsvoorschriften"],
                ["narratief", "een verhaal vertellen", "videoblog, reisverslag, true crime podcast, verhalend gedicht"],
                ["argumentatief", "een standpunt opbouwen", "pleidooi, betoog, debat"],
                ["literair", "raken, met esthetische waarde", "kortverhaal, strip, gedicht, lied, stand-upcomedy"],
            ])),
            ("p", "Drie ervan lijken sterk op elkaar. Een <strong>opiniërende</strong> tekst geeft vooral een "
                  "oordeel. Een <strong>argumentatieve</strong> tekst bouwt dat oordeel op met argumenten, "
                  "tegenargumenten en een conclusie: daar is de opbouw de kern. Een <strong>persuasieve</strong> "
                  "tekst wil je vooral beïnvloeden, desnoods zonder sterke argumenten, met beelden, muziek en "
                  "gevoel."),
            ("kader", "Eén tekst kan tot meer dan één soort behoren. Een reclamespot kan een verhaal vertellen "
                      "én willen verkopen. Je kijkt dan naar het hoofddoel."),
            ("p", "Twee valstrikken. Een <strong>publireportage</strong> reken je niet bij de informatieve "
                  "teksten: de vorm is informatief, het doel is verkopen, dus is hij persuasief. En een "
                  "<strong>satirische nieuwssite</strong> is evenmin informatief: het doel is je laten lachen "
                  "en iets aan de kaak stellen, niet je informeren. Omgekeerd kan een <strong>strip</strong> "
                  "wel degelijk een literaire tekst zijn: literatuur zit niet alleen in romans."),
        ]),
        gesprek("bel zelf naar een winkel, een club of een gemeentedienst om iets te vragen, in plaats van "
                "het op te zoeken of te mailen."),
    ],
    onthoud=[
        "Het communicatiemodel telt acht elementen: zender, boodschap, ontvanger, kanaal, context, doel, effect en ruis.",
        "Doel is wat de zender wil, effect is wat er werkelijk gebeurt. Die twee lopen vaak uit elkaar.",
        "Interne ruis zit in de mensen zelf (moe, verstrooid), externe ruis komt van buitenaf (lawaai, slechte verbinding).",
        "De zeven tekstsoorten: informatief, persuasief, opiniërend, prescriptief, narratief, argumentatief en literair.",
        "Opiniërend geeft een oordeel, argumentatief bouwt het op, persuasief wil beïnvloeden. Kijk naar het hoofddoel.",
        "Een publireportage en een satirisch nieuwsbericht lenen de vorm van informatie, maar hebben een ander doel.",
    ],
)

# ───────────────────────── 2. Hoofdgedachte, alinea en structuuraanduiders
BUNDELS["hoofdgedachte-alinea-en-structuuraanduiders-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Hoofdgedachte, alinea en structuuraanduiders",
    onder="Wat een tekst zegt, hoe hij opgebouwd is, en aan welke woordjes je zijn gedachtegang herkent.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie begrippen die je uit elkaar moet houden, want op het examen wordt er apart naar "
                  "gevraagd."),
            ("p", tabel(["Begrip", "Hoe lang", "Voorbeeld"], [
                ["onderwerp", "één of enkele woorden", "sport"],
                ["hoofdgedachte", "één zin", "Jongeren moeten meer sporten."],
                ["hoofdpunten", "meerdere elementen", "Sport is goed voor je lichaam. Sport doet je mentaal deugd."],
            ])),
            ("p", "Het <strong>onderwerp</strong> zeg je in één of enkele woorden: waarover gaat deze tekst? "
                  "De <strong>hoofdgedachte</strong> past in één zin: wat is de belangrijkste boodschap? De "
                  "<strong>hoofdpunten</strong> zijn alle inhoudelijke elementen die die hoofdgedachte "
                  "ondersteunen. Pas op: het onderwerp van een tekst en zijn <strong>titel</strong> zijn niet "
                  "altijd hetzelfde. Een titel wil vaak vooral je aandacht trekken; 'Het einde van de stilte' "
                  "kan gewoon over lawaaihinder gaan."),
            ("p", "Een voorbeeld. <em>'Steeds meer scholen schaffen de smartphone af. Leerkrachten zien "
                  "rustigere speeltijden. Ook de resultaten gaan erop vooruit. Het verbod werkt dus.'</em> Het "
                  "onderwerp is: smartphones op school. De hoofdgedachte is de laatste zin: een "
                  "smartphoneverbod heeft een goed effect. De drie zinnen ervoor zijn hoofdpunten."),
            ("p", "Daarnaast moet je uit één of meerdere teksten <strong>relevante informatie selecteren</strong>. "
                  "Relevant betekent: dienstig voor jouw vraag. Wat mooi of opvallend is maar de vraag niet "
                  "beantwoordt, laat je liggen, ook als het uit de langste tekst komt. Dat is hetzelfde als "
                  "<strong>hoofd- en bijzaken</strong> scheiden."),
        ]),
        dict(kop="De IMS-structuur, alinea's en lay-out", blokken=[
            ("p", "Elke goed gestructureerde tekst, gesproken of geschreven, heeft drie delen. Die afkorting "
                  "leer je: <strong>IMS</strong> staat voor <strong>inleiding, midden en slot</strong>. In de "
                  "<strong>inleiding</strong> zet de schrijver het onderwerp neer en wekt hij je "
                  "belangstelling. In het <strong>slot</strong> vind je meestal het <strong>besluit</strong>."),
            ("p", "Een <strong>alinea</strong> is een tekstdeel dat één deelonderwerp behandelt en dat begint "
                  "met een witregel of een insprong. Omdat er per alinea in principe één deelonderwerp staat, "
                  "kan je een tekst vaak samenvatten door per alinea één zin te schrijven. "
                  "<strong>Tussentitels</strong> verdelen een lange tekst in herkenbare stukken, zodat je de "
                  "structuur al ziet voor je alles gelezen hebt."),
            ("p", "Alinea's, tussentitels en witruimte horen bij de <strong>lay-out</strong>: hoe de tekst "
                  "eruitziet. De hoofdgedachte hoort daar niet bij, want dat is inhoud. Als je snel wil zien "
                  "waarover een tekst gaat, gebruik je de <strong>visuele hulpmiddelen</strong>: de titel en "
                  "de tussentitels, de vetgedrukte woorden, en de foto of de grafiek erbij. De breedte van de "
                  "marge zegt niets."),
        ]),
        dict(kop="Notities nemen", blokken=[
            ("p", "Bij een lees- of luistertekst neem je <strong>notities</strong>. Ze moeten aansluiten bij de "
                  "inhoud en duidelijk genoeg zijn om er later mee te werken, bijvoorbeeld om een samenvatting "
                  "te maken of een vraag te beantwoorden. <strong>Volledige zinnen hoeven niet</strong>, en bij "
                  "een luistertekst kan het ook niet: je moet mee met het tempo. Gebruik "
                  "<strong>telegramstijl</strong>, <strong>afkortingen</strong> en <strong>symbolen</strong>."),
            ("p", "Je kan notities ordenen in een <strong>schema</strong>, een <strong>tabel</strong> of een "
                  "<strong>mindmap</strong>. Een rijmschema is geen manier om notities te ordenen: dat "
                  "beschrijft hoe de rijmklanken in een gedicht lopen."),
        ]),
        dict(kop="Structuuraanduiders: verwijswoorden en signaalwoorden", blokken=[
            ("p", "<strong>Structuuraanduiders</strong> zijn woorden, geen titels of witregels. Het zijn "
                  "<strong>verwijswoorden</strong> zoals <em>zij, hem, deze, die, hun</em> en "
                  "<strong>signaalwoorden</strong> zoals <em>maar, ten eerste, tot slot, dus, want, hoewel, "
                  "als</em>."),
            ("p", "Een <strong>verwijswoord</strong> wijst terug naar iets dat eerder stond, zodat je het niet "
                  "hoeft te herhalen. In <em>'De leerlingen kregen hun rapport. Zij waren behoorlijk "
                  "zenuwachtig'</em> verwijst 'zij' naar de leerlingen. Een verwijswoord kan ook naar een hele "
                  "vorige zin verwijzen: <em>'Hij kwam niet opdagen. Dat viel tegen.'</em> Let op: "
                  "<em>hoewel</em> is géén verwijswoord maar een signaalwoord, want het legt een verband."),
            ("p", "<strong>Signaalwoorden</strong> verraden de gedachtegang. Aan <em>maar</em> zie je dat er "
                  "een bocht komt, aan <em>dus</em> dat er een besluit volgt. Zo kan je de redenering van een "
                  "schrijver reconstrueren, ook als de inhoud moeilijk is. Ze staan trouwens lang niet altijd "
                  "vooraan in de zin: <em>'Hij was immers ziek'</em>, <em>'Dat is echter niet zeker'</em>."),
            ("p", tabel(["Verband", "Signaalwoorden", "Voorbeeld"], [
                ["opsomming", "ten eerste, ten tweede, ten slotte, bovendien", "In een instructie staan de stappen in volgorde."],
                ["tegenstelling", "maar, daarentegen, echter, toch", "Het regende. Toch gingen we."],
                ["reden of oorzaak", "want, omdat, immers", "Hij kwam niet. Hij was immers ziek."],
                ["gevolg", "dus, daarom, daardoor", "Het vroor. Daardoor lagen de wegen glad."],
                ["voorwaarde", "als, indien, mits, tenzij", "Mits je op tijd bent, mag je mee."],
                ["toegeving", "hoewel, ondanks, niettemin", "Hoewel het stortregende, gingen we wandelen."],
                ["doel", "opdat, zodat, om te", "Opdat iedereen mee kon, huurden we een bus."],
                ["voorbeeld", "bijvoorbeeld, zoals", "Fruit, zoals appels en peren."],
                ["evenredigheid", "naarmate, hoe ... hoe ...", "Naarmate de avond vorderde, werd het stiller."],
                ["besluit of samenvatting", "kortom, samengevat, al met al", "Kortom, het verbod werkt."],
            ])),
            ("kader", "Let op de valstrik met <strong>bovendien</strong>: dat voegt iets toe in dezelfde "
                      "richting. Het is dus géén tegenstelling en géén besluit."),
            ("p", "Een tekst <em>zonder</em> signaalwoorden kan best een duidelijke structuur hebben: die zit "
                  "ook in de volgorde, de alinea's en de tussentitels. Signaalwoorden maken de structuur "
                  "alleen zichtbaarder."),
        ]),
        gesprek("vertel iemand in drie minuten een film of een boek na, met een duidelijke inleiding, een "
                "midden en een slot."),
    ],
    onthoud=[
        "Onderwerp: enkele woorden. Hoofdgedachte: één zin. Hoofdpunten: wat die hoofdgedachte ondersteunt.",
        "IMS staat voor inleiding, midden en slot. Het besluit staat meestal in het slot.",
        "Eén alinea behandelt in principe één deelonderwerp. Alinea's, tussentitels en witruimte zijn lay-out.",
        "Notities mogen telegramstijl zijn, met afkortingen en symbolen, in een schema, tabel of mindmap.",
        "Structuuraanduiders zijn verwijswoorden (zij, deze, hun) en signaalwoorden (maar, dus, hoewel).",
        "Leer per verband de signaalwoorden: hoewel = toegeving, mits = voorwaarde, opdat = doel, naarmate = evenredigheid.",
    ],
)

# ───────────────────────── 3. Argumenteren
BUNDELS["argumenteren-stelling-argumentsoort-en-drogreden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Argumenteren: stelling, argumentsoort en drogreden",
    onder="Feiten en meningen scheiden, een betoog opbouwen, en redeneringen herkennen die alleen maar goed klinken.",
    secties=[
        dict(kop="Feit of mening", blokken=[
            ("p", "Een <strong>feit</strong> kan je nagaan: er bestaat een bron die uitsluitsel geeft. "
                  "<em>'De film duurt honderdtweeënveertig minuten'</em> en <em>'De temperatuur lag gisteren "
                  "zes graden boven het gemiddelde'</em> zijn feiten. Een <strong>mening</strong> geeft een "
                  "oordeel: <em>'De film duurt veel te lang'</em>, <em>'Het is schandalig dat dit mag'</em>."),
            ("p", "Naast een feit en een mening staat de <strong>aanname</strong>: iets wat de schrijver "
                  "als vanzelfsprekend veronderstelt zonder het te zeggen. <em>'Iedereen wil toch gewoon op "
                  "tijd op het werk zijn'</em> is geen feit en niet echt een mening, maar een aanname waarop "
                  "de rest van de redenering steunt. Wie kritisch leest, haalt die aannames naar boven, want "
                  "daar zit vaak het zwakke punt."),
            ("p", "Een mening wordt <strong>geen</strong> feit doordat veel mensen het ermee eens zijn. Hoeveel "
                  "mensen iets vinden, verandert niets aan de vraag of het nagegaan kan worden. Dát veel mensen "
                  "iets vinden, is trouwens zelf wél een feit."),
            ("p", "Je herkent een mening aan <strong>waardewoorden</strong> (schitterend, belachelijk, lelijk, "
                  "schandalig), aan uitroeptekens middenin de tekst, en aan formuleringen als <em>volgens mij</em>, "
                  "<em>ik vind</em> of <em>zou moeten</em>. Een jaartal of een meting is daarentegen gewoon een "
                  "gegeven. Waarom dat onderscheid telt als je wil overtuigen? Omdat je lezer anders niet weet "
                  "wat hij kan nagaan, en een mening die als feit gepresenteerd wordt oneerlijk aanvoelt."),
        ]),
        dict(kop="De bouwstenen van een betoog", blokken=[
            ("p", "De <strong>stelling</strong> is de bewering waarover de discussie gaat. Een goede stelling "
                  "is <strong>discutabel</strong>: je kan er redelijkerwijs voor of tegen zijn. "
                  "<em>'Huiswerk moet worden afgeschaft'</em> kan dienen als stelling voor een debat; "
                  "<em>'Onze school telt achthonderd leerlingen'</em> niet, want dat is een feit."),
            ("p", "Het <strong>standpunt</strong> is de kant die jij kiest tegenover die stelling: "
                  "<em>'Ik ben daartegen.'</em> Stelling en standpunt zijn dus niet hetzelfde: de stelling staat "
                  "ter discussie, het standpunt is jouw positie."),
            ("p", "Een <strong>argument</strong> is de reden die je geeft om je standpunt te steunen. Een "
                  "<strong>tegenargument</strong> is een reden die tégen de stelling pleit. De "
                  "<strong>conclusie</strong> is wat je op het einde uit je argumenten afleidt; ze mag niet meer "
                  "beweren dan de argumenten dragen."),
            ("kader", "Een sterk betoog <strong>noemt</strong> de tegenargumenten en <strong>weerlegt</strong> "
                      "ze. Weerleggen is het tegenargument eerst eerlijk noemen en er dan een reden tegenover "
                      "zetten. Wie de tegenargumenten verzwijgt, komt zwakker over, niet sterker."),
            ("p", "De opbouw van een argumentatieve tekst is dus: een duidelijke stelling, argumenten die haar "
                  "steunen, een weerlegging van de tegenargumenten, en een conclusie. Een rijmschema hoort daar "
                  "niet bij."),
        ]),
        dict(kop="Soorten argumentatie", blokken=[
            ("p", "Een argument kan op verschillende manieren steunen. De vakfiche noemt er vijf, en je moet ze "
                  "kunnen herkennen."),
            ("p", tabel(["Soort", "Voorbeeldzin", "Waar let je op"], [
                ["vergelijking", "In Finland werkt dit al vijftien jaar, dus het kan hier ook.",
                 "Zijn de twee gevallen echt vergelijkbaar?"],
                ["oorzaak en gevolg", "Door de nieuwe maatregel daalde het aantal ongevallen.",
                 "Is het verband aangetoond, of alleen verondersteld?"],
                ["wetenschappelijk onderzoek", "Uit een studie van de universiteit blijkt dat ...",
                 "Wie deed het onderzoek, bij hoeveel mensen?"],
                ["cijfers en statistieken", "Acht op de tien leerlingen zegt te weinig te slapen.",
                 "Hoeveel mensen zijn bevraagd, en door wie?"],
                ["autoriteit", "Een arts zegt dat dit ongezond is.",
                 "Spreekt de deskundige binnen zijn eigen vakgebied?"],
            ])),
            ("p", "Een beroep op een autoriteit is dus <strong>niet</strong> altijd een drogreden. Een arts over "
                  "gezondheid is een geldig argument; dezelfde arts over belastingtarieven niet. En een argument "
                  "op basis van <strong>oorzaak en gevolg</strong> is evenmin per definitie fout: het wordt pas "
                  "een drogreden als je een verband verzint dat er niet is. Een argument moet trouwens niet "
                  "altijd met cijfers onderbouwd zijn; cijfers zijn maar één van de vijf soorten."),
            ("p", "Je maakt een argument sterker door te noemen waar je gegeven vandaan komt, je cijfers "
                  "controleerbaar te maken en het sterkste tegenargument te weerleggen. Een groter lettertype "
                  "verandert niets aan de redenering."),
        ]),
        dict(kop="Drogredenen", blokken=[
            ("p", "Een <strong>drogreden</strong> is een redenering die overtuigend klinkt maar niet deugt. Je "
                  "moet ze in je eigen tekst vermijden en in die van anderen herkennen."),
            ("p", tabel(["Drogreden", "Klinkt als", "Wat er mis is"], [
                ["persoonlijke aanval", "Jij hebt nooit gewerkt, dus over lonen moet jij zwijgen.",
                 "de persoon wordt aangevallen in plaats van zijn argument"],
                ["beroep op de massa", "Iedereen in onze klas doet het, dus het kan geen kwaad.",
                 "dat velen iets doen, bewijst niet dat het goed is"],
                ["cirkelredenering", "Dit boek is goed, want het is een goed boek.",
                 "de stelling wordt als argument voor zichzelf gebruikt"],
                ["vals dilemma", "Of we verbieden alle auto's, of we laten het klimaat stikken.",
                 "twee uitersten, alsof er niets tussenin ligt"],
                ["stroman", "Jij wil dus dat niemand nog iets mag.",
                 "de mening van de tegenstander wordt verdraaid tot iets wat makkelijk te weerleggen is"],
                ["overhaaste veralgemening", "Mijn overgrootvader rookte tot zijn 95ste, dus roken is niet ongezond.",
                 "uit één geval wordt een algemene regel gemaakt"],
                ["glijdende schaal", "Als we dit ene uitzonderingetje toestaan, eindigt het met totale chaos.",
                 "één kleine stap zou onvermijdelijk tot een ramp leiden, zonder bewijs"],
                ["autoriteit buiten zijn vak", "Een bekende voetballer zegt dat dit gezond is.",
                 "de deskundige spreekt over iets anders dan zijn vakgebied"],
            ])),
            ("p", "Eén valstrik komt zo vaak voor dat ze een eigen zin verdient: <em>'Sinds de nieuwe "
                  "burgemeester er is, regent het meer. Hij is dus de oorzaak.'</em> Dat twee dingen na elkaar "
                  "gebeuren, bewijst niet dat het ene het andere veroorzaakt. Volgorde in de tijd is geen "
                  "oorzaak."),
            ("p", "Als je een argumentatieve tekst <strong>beoordeelt</strong>, weeg je dus de redenering zelf: "
                  "dragen de argumenten de conclusie, en zijn de gegevens betrouwbaar? Niet of de tekst mooi "
                  "opgemaakt is, of de schrijver bekend is, of hoeveel alinea's er staan."),
        ]),
        gesprek("verdedig aan tafel een standpunt waar je het zelf niet helemaal mee eens bent, met twee "
                "argumenten en een weerlegging."),
    ],
    onthoud=[
        "Een feit kan je nagaan, een mening niet. Veel bijval maakt van een mening nog geen feit.",
        "Stelling = de bewering die ter discussie staat. Standpunt = de kant die jij kiest.",
        "Een betoog: stelling, argumenten, weerlegging van tegenargumenten, conclusie.",
        "Vijf soorten argumentatie: vergelijking, oorzaak en gevolg, onderzoek, cijfers, autoriteit.",
        "Een autoriteitsargument is geldig binnen het vakgebied van de deskundige, daarbuiten niet.",
        "Ken de drogredenen: persoonlijke aanval, beroep op de massa, cirkelredenering, vals dilemma, stroman, overhaaste veralgemening, glijdende schaal.",
        "Na elkaar gebeuren is niet hetzelfde als door elkaar veroorzaakt worden.",
    ],
)

# ───────────────────────── 4. Bronnen wegen
BUNDELS["bronnen-wegen-objectief-gekleurd-of-nep-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Bronnen wegen: objectief, gekleurd of nep",
    onder="Is deze tekst betrouwbaar, correct en bruikbaar? En hoe kleurt een schrijver zonder te liegen?",
    secties=[
        dict(kop="Drie verschillende vragen", blokken=[
            ("p", "De vakfiche vraagt of een tekst <strong>betrouwbaar</strong>, <strong>correct</strong> én "
                  "<strong>bruikbaar</strong> is. Dat zijn drie verschillende dingen. Bruikbaar betekent: geeft "
                  "hij een antwoord op de vraag die jij hebt. Een perfect correcte tekst kan voor jouw opdracht "
                  "volstrekt nutteloos zijn."),
        ]),
        dict(kop="De criteria op een rij", blokken=[
            ("p", "De <strong>eerste</strong> vraag is altijd: <strong>wie is de zender?</strong> Zonder zender "
                  "kan je niets wegen, geen deskundigheid, geen bedoeling, geen belang."),
            ("p", tabel(["Criterium", "Wat je vraagt"], [
                ["zender", "Wie schreef dit? Is die deskundig in dit onderwerp?"],
                ["bedoeling", "Wat wil de zender bereiken? Wat laat hij daarom weg?"],
                ["bronnen", "Waarop steunt de tekst zelf? Bestaan die bronnen, en zeggen ze dat ook echt?"],
                ["objectief of subjectief", "Staan er waardewoorden, uitroeptekens, 'ik vind'?"],
                ["opvattingen en waardeoordelen", "Welke overtuigingen, welke aannames neemt de schrijver als vanzelfsprekend aan?"],
                ["actualiteit", "Hoe oud is de informatie? Cijfers, prijzen en wetten verouderen snel."],
                ["kanaal", "Passeerde dit een redactie, of gaat het rond in een groepschat?"],
                ["spelling", "Veel spelfouten wijzen erop dat er geen eindredactie overheen ging."],
                ["dubbele bodems", "Zit er symboliek of ironie in? Is het letterlijk bedoeld?"],
                ["framing", "Welke invalshoek is gekozen, en wat valt daardoor buiten beeld?"],
            ])),
            ("p", "<strong>Deskundig</strong> betekent: echte kennis van zaken over dít onderwerp. "
                  "<strong>Deskundigheid</strong> geldt dus per vakgebied. En een deskundige kan tegelijk een "
                  "<strong>belang</strong> hebben bij wat hij vertelt: een onderzoeker die betaald wordt door de "
                  "sector waarover hij publiceert, is deskundig én partij. Daarom is het nuttig te weten wie een "
                  "onderzoek betaald heeft. Dat maakt het niet meteen waardeloos, maar het is een reden om extra "
                  "kritisch te lezen. Een tekst van een deskundige is dus niet automatisch objectief, en een "
                  "tekst die bronnen vermeldt is niet automatisch betrouwbaar."),
            ("p", "Vind je een artikel <strong>zonder auteur en zonder datum</strong>, dan bewijst dat niets, "
                  "maar je kan zender noch actualiteit wegen. Dan zoek je de informatie elders na. En wat een "
                  "zender <strong>weglaat</strong>, verraadt vaak meer dan wat hij opschrijft: een frisdrankmerk "
                  "dat een lange tekst over 'bewust bewegen' publiceert, zwijgt waarschijnlijk over suiker."),
            ("weetje", "Een <strong>dubbele bodem</strong> is een verborgen betekenis onder de letterlijke "
                       "tekst. Wie die mist, leest een recensie als <em>'Kortom, een meesterwerk, als je van "
                       "drie uur stilstaande beelden houdt'</em> precies verkeerd. De lof wordt in de tweede "
                       "helft van de zin onderuitgehaald: dat is <strong>ironie</strong>."),
        ]),
        dict(kop="Teksten die zich voordoen als iets anders", blokken=[
            ("p", "Drie soorten lenen de vorm van het nieuws. Een <strong>publireportage</strong> is betaalde "
                  "reclame in de vorm van een artikel; ze is lastiger te herkennen dan een gewone spot, want bij "
                  "een spot weet je dat het reclame is. Let op het kleine woordje 'advertorial'. Een "
                  "<strong>satirisch nieuwsbericht</strong> wil je laten lachen en iets aan de kaak stellen; het "
                  "wil je niet misleiden, maar losgeknipt van zijn bron gaat het wel mis. En "
                  "<strong>nepnieuws</strong> is verzonnen informatie die zich voordoet als echt nieuws."),
            ("p", "Nepnieuws herken je meestal aan drie dingen samen: er staat <strong>geen auteur</strong> bij, "
                  "het circuleert <strong>alleen via sociale media</strong>, en de <strong>kop belooft veel "
                  "meer</strong> dan de tekst waarmaakt. Een verwijzing naar een studie mét naam en jaartal is "
                  "juist een teken van onderbouwing, al moet je die studie nog altijd nagaan."),
            ("p", "<strong>Propaganda</strong> ten slotte is een eenzijdige, meestal politieke tekst die je met "
                  "opzet maar één kant van een zaak toont. Ook dat is persuasief."),
            ("kader", "Een <strong>influencer</strong> die een product toont zonder te zeggen dat hij ervoor "
                      "betaald wordt, maakt precies één criterium onbruikbaar: je kent de "
                      "<strong>bedoeling van de zender</strong> niet. Daarom bestaat de verplichting om zo'n "
                      "samenwerking te vermelden."),
        ]),
        dict(kop="Framing: kleuren zonder te liegen", blokken=[
            ("p", "<strong>Framing</strong> is een onderwerp in een bepaald kader zetten door je woordkeuze en "
                  "je invalshoek. Het woord komt van <em>frame</em>, kader: je zet een kader rond de feiten en "
                  "laat de rest buiten beeld. Wie framet, <strong>liegt niet</strong>. Framing werkt net omdat "
                  "alles wat er staat waar kan zijn."),
            ("p", "Twee kranten berichten over dezelfde betoging. De ene kop luidt <em>'Duizenden op straat "
                  "voor het klimaat'</em>, de andere <em>'Klimaatbetoging legt centrum lam'</em>. Allebei "
                  "kloppen ze. De ene kiest de deelnemers als invalshoek, de andere de hinder. Dezelfde "
                  "gebeurtenis kan dus in twee <em>betrouwbare</em> kranten heel verschillend geframed worden. "
                  "Daarom loont het om meerdere bronnen te lezen. Spreken twee betrouwbare bronnen elkaar tegen, "
                  "zoek dan een derde en vergelijk hoe ze aan hun gegevens komen; vaak meten ze iets anders of "
                  "over een andere periode."),
            ("p", "De talige middelen om subjectiviteit uit te drukken zijn <strong>beeldspraak</strong>, de "
                  "<strong>connotatie</strong> van woorden en <strong>modaliteit</strong>. De bladspiegel hoort "
                  "daar niet bij, dat is vormgeving."),
            ("p", "<strong>Connotatie</strong> is de gevoelswaarde die aan een woord kleeft naast zijn "
                  "letterlijke betekenis: 'goedkoop' en 'voordelig' betekenen hetzelfde, maar het eerste klinkt "
                  "negatiever. Een <strong>eufemisme</strong> verzacht ('prijsaanpassing' voor "
                  "'prijsverhoging'), een <strong>dysfemisme</strong> doet het omgekeerde ('belastinggeld "
                  "verkwisten' voor 'overheidsuitgaven'). In een kop kleuren woorden als "
                  "<em>schandalig</em>, <em>eindelijk</em> en <em>zogenaamd</em> het bericht; <em>dinsdag</em> "
                  "is gewoon een gegeven."),
            ("p", "<strong>Modaliteit</strong> zit in kleine woordjes. <em>'Zwijg eens even!'</em> komt anders "
                  "over dan <em>'Zwijg!'</em>: het woordje <em>eens</em> maakt het bevel zachter, zonder de "
                  "inhoud te veranderen. Zulke woordjes heten <strong>modale partikels</strong>."),
            ("p", "Ook <strong>beeldspraak</strong> kleurt. De <strong>metafoor</strong> in "
                  "<em>'Een golf van klachten overspoelde de dienst'</em> laat de klachten aanvoelen als een natuurramp, zonder één cijfer te noemen."),
        ]),
        gesprek("leg aan iemand uit waarom je een bericht dat je kreeg niet vertrouwt, met minstens twee "
                "criteria uit dit hoofdstuk."),
    ],
    onthoud=[
        "Betrouwbaar, correct en bruikbaar zijn drie verschillende vragen.",
        "Begin altijd bij de zender: wie is het, is die deskundig, en wat wil die bereiken?",
        "Bronvermelding of deskundigheid maakt een tekst nog niet objectief. Wat weggelaten wordt, telt mee.",
        "Publireportage, satire en nepnieuws lenen alle drie de vorm van het nieuws, met een ander doel.",
        "Framing liegt niet: ze kiest woorden en invalshoek. Twee betrouwbare kranten kunnen verschillend framen.",
        "Subjectiviteit uit je met beeldspraak, connotatie en modaliteit. Eufemisme verzacht, dysfemisme verscherpt.",
    ],
)

# ───────────────────────── 5. Standaardtaal, tussentaal en register
BUNDELS["standaardtaal-tussentaal-en-register-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Standaardtaal, tussentaal en register",
    onder="Welke taal past bij welke situatie, en wat je taalgebruik over jou vertelt.",
    secties=[
        dict(kop="De drie registers", blokken=[
            ("p", "Het <strong>register</strong> is de toon en de woordkeuze die je aan de situatie aanpast. Er "
                  "zijn er drie: <strong>formeel</strong>, <strong>neutraal</strong> en "
                  "<strong>informeel</strong>. Geen van drie is beter dan de andere; ze passen elk bij een "
                  "andere situatie. Het register dat je kiest, hangt af van je <strong>ontvanger</strong> en van "
                  "de <strong>situatie</strong>."),
            ("p", tabel(["Register", "Voorbeeldzin", "Wanneer"], [
                ["formeel", "Zou u mij vriendelijk willen meedelen wanneer de les aanvangt?", "sollicitatie, klacht, onbekende instantie"],
                ["neutraal", "Kan je me laten weten wanneer de les begint?", "bijna overal bruikbaar"],
                ["informeel", "Hey, wanneer start die les eigenlijk?", "vrienden, familie, groepschat"],
            ])),
            ("p", "Bij een <strong>sollicitatiemail</strong> kies je de formele kant: je kent de ontvanger niet "
                  "en er staat iets op het spel. Daar hoort ook bij dat je de ontvanger met <strong>u</strong> "
                  "aanspreekt, in volledige zinnen schrijft zonder afkortingen, en afsluit met iets als "
                  "<em>Met vriendelijke groeten</em>. Smileys horen daar niet. Een formele brief sluit je "
                  "<strong>niet</strong> af met <em>groetjes</em>, <em>ciao</em> of <em>dikke kus</em>."),
            ("p", "Ken je de naam van je contactpersoon niet, dan schrijf je <em>Geachte heer of mevrouw</em>, "
                  "niet <em>Hallo allemaal</em>. En je blijft in <strong>één</strong> register: "
                  "<em>'Beste directeur, ik kom morgen ni naar school want ik ben ziek. Ciao!'</em> valt "
                  "helemaal uit de toon na die eerste woorden."),
        ]),
        dict(kop="Beleefdheidsconventies", blokken=[
            ("p", "<strong>Beleefdheidsconventies</strong> zijn de ongeschreven omgangsregels die bepalen wat "
                  "beleefd is: iemand laten uitspreken, groeten voor je iets vraagt, bedanken. Ze verschillen "
                  "per cultuur."),
            ("p", "Je spreekt een volwassene met wie je <strong>geen nauwe band</strong> hebt aan met "
                  "<strong>u</strong>. Het gaat dus om de afstand in de relatie, niet louter om leeftijd: een "
                  "oom van veertig spreek je met <em>je</em> aan, een onbekende arts van dertig met <em>u</em>."),
            ("p", "Wie het verkeerde register kiest, kan <strong>onbeleefd overkomen zonder dat te willen</strong>. "
                  "Het gaat vaak niet om wat je zegt maar om hoe. In een klachtenmail zet je daarom beter geen "
                  "rij uitroeptekens: die komen boos over en duwen de ontvanger in het defensief. Leestekens "
                  "zijn ook toon."),
            ("p", "En je let in een sollicitatiemail zoveel meer op je spelling dan in een appje omdat de "
                  "ontvanger er een <strong>beeld van jou</strong> uit opmaakt. Je taalgebruik maakt deel uit "
                  "van de indruk die je nalaat."),
            ("kader", "De fiche vraagt dat je communicatie <strong>helder, gepast, correct en vlot</strong> is. "
                      "Dat zijn vier aparte eisen. <em>Correct</em> gaat over spelling en grammatica, "
                      "<em>gepast</em> over het register: past het bij de ontvanger en de situatie?"),
            ("p", "Om je taal aan je ontvanger aan te passen, moet je weten <strong>wie</strong> die ontvanger "
                  "is, welke <strong>relatie</strong> je met hem hebt, en via welk <strong>kanaal</strong> je "
                  "schrijft. Hoeveel alinea's je nodig hebt, volgt uit je inhoud en heeft daar niets mee te "
                  "maken."),
        ]),
        dict(kop="Taalvariëteiten", blokken=[
            ("p", "<strong>Standaardtaal</strong> is de variëteit die in het hele taalgebied als gepast geldt in "
                  "formele situaties. Ze is een afspraak, geen natuurwet, en ze maakt communicatie mogelijk over "
                  "de streken heen. Op je examen, in een sollicitatiebrief en in een krantenartikel wordt ze "
                  "verwacht."),
            ("p", "Daarnaast onderscheidt de fiche vier soorten variëteiten: <strong>nationale</strong>, "
                  "<strong>regionale</strong>, <strong>sociale</strong> en <strong>situationele</strong>."),
            ("p", tabel(["Variëteit", "Loopt langs", "Voorbeeld"], [
                ["nationale", "de landsgrens", "in Nederland 'pinpas', in Vlaanderen 'bankkaart'"],
                ["regionale", "de streek", "een West-Vlaams en een Limburgs dialect"],
                ["sociale", "de groep waartoe je hoort", "jongerentaal, vakjargon"],
                ["situationele", "de gelegenheid", "je praat anders op café dan op een begrafenis"],
            ])),
            ("p", "<strong>Dialect</strong> is een regionale variëteit en hoort bij één streek. Hoe verder twee "
                  "streken uit elkaar liggen, hoe groter het verschil: een West-Vlaming en een Limburger die "
                  "elk hun dialect spreken, verstaan elkaar nauwelijks. Net daarvoor dient de standaardtaal."),
            ("p", "<strong>Tussentaal</strong> zit tussen dialect en standaardtaal in. Veel Vlamingen zeggen "
                  "<em>ge</em> en <em>gij</em> waar de standaardtaal <em>je</em> en <em>jij</em> heeft: dat is "
                  "een tussentalige variant. Tussentaal en dialect zijn <strong>niet</strong> hetzelfde: een "
                  "dialect kan elders onverstaanbaar zijn, tussentaal wordt over heel Vlaanderen begrepen."),
            ("p", "<strong>Jargon</strong> is de vaktaal van een beroepsgroep. <em>'De patiënt vertoont dyspneu "
                  "bij inspanning'</em> is medisch jargon: binnen de groep efficiënt, erbuiten een drempel. "
                  "<strong>Jongerentaal</strong> wordt sterk beïnvloed door andere talen, zoals het Engels, het "
                  "Marokkaans en het Surinaams. Ze is geen slecht Nederlands; ze hoort alleen niet thuis in een "
                  "sollicitatiegesprek, waar ze ongepast overkomt."),
            ("kader", "Variëteiten zijn <strong>niet fout</strong>. Ze zijn gebonden aan een situatie. "
                      "Standaardtaal is niet de enige correcte vorm van Nederlands; ze is wel de vorm die op een "
                      "examen verwacht wordt."),
            ("p", "Waarom je <strong>taalvariatie</strong> bij het lezen moet herkennen? Omdat de gekozen variëteit iets verraadt over de "
                  "zender en zijn publiek. Een tekst vol jongerentaal mikt op een ander publiek dan een tekst in "
                  "strak formele standaardtaal."),
        ]),
        dict(kop="Non-verbale communicatie", blokken=[
            ("p", "Tot de <strong>non-verbale communicatie</strong> rekent de fiche: "
                  "<strong>lichaamstaal</strong>, <strong>mimiek</strong>, <strong>oogcontact</strong>, "
                  "<strong>houding</strong>, <strong>afstand</strong> en <strong>bewegingen</strong>; "
                  "<strong>intonatie</strong>, <strong>articulatie</strong>, <strong>tempo</strong> en "
                  "<strong>volume</strong>; <strong>kleding en uiterlijk</strong>; en op een scherm zelfs "
                  "<strong>emoji's</strong>. Spelling hoort er niet bij: dat is verbaal."),
            ("p", "Die signalen zijn <strong>cultuurgebonden</strong>. Ze hebben geen vaste betekenis; ze "
                  "krijgen die van de cultuur waarin je ze gebruikt. In sommige culturen is je ogen neerslaan "
                  "een teken van respect, terwijl kinderen in de Vlaamse cultuur net leren dat ze hun "
                  "gesprekspartner moeten aankijken. Dezelfde blik betekent dus in de ene cultuur respect en in "
                  "de andere brutaliteit. Zulke verschillen leiden makkelijk tot misverstanden."),
            ("p", "Je taalgebruik is een <strong>deel van je identiteit</strong> en beïnvloedt het beeld dat "
                  "anderen van je hebben. En omgekeerd: jij oordeelt ook over anderen op basis van hoe ze "
                  "praten. Inzicht daarin maakt je milder."),
        ]),
        gesprek("stel dezelfde vraag twee keer hardop: één keer aan een vriend, één keer aan een onbekende "
                "volwassene. Let op wat er verandert aan je woorden én aan je houding."),
    ],
    onthoud=[
        "Drie registers: formeel, neutraal en informeel. Blijf binnen één register in dezelfde tekst.",
        "U gebruik je bij een volwassene met wie je geen nauwe band hebt. Het gaat om afstand, niet om leeftijd.",
        "Helder, gepast, correct en vlot zijn vier aparte eisen. Gepast gaat over het register.",
        "Vier variëteiten: nationale, regionale, sociale en situationele. Dialect is regionaal, jargon sociaal.",
        "Tussentaal zit tussen dialect en standaardtaal in en is niet hetzelfde als dialect.",
        "Non-verbale communicatie is cultuurgebonden: dezelfde blik betekent elders iets anders.",
    ],
)

# ───────────────────────── 6. De woordsoorten op een rij
BUNDELS["de-woordsoorten-op-een-rij-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De woordsoorten op een rij",
    onder="Elf woordsoorten, en de acht soorten voornaamwoorden die op elkaar lijken.",
    secties=[
        dict(kop="Waarom woordsoorten?", blokken=[
            ("p", "Woordsoorten zijn geen doel op zich. Je hebt ze nodig omdat "
                  "<strong>spellingregels vaak van de woordsoort afhangen</strong>: of je 'de gekleurde muur' "
                  "of 'de muur is gekleurd' schrijft, hangt af van hoe het woord gebruikt wordt. En je hebt ze "
                  "nodig om over taal te kunnen praten."),
            ("kader", "Eén woord kan tot meerdere woordsoorten behoren, afhankelijk van zijn plaats in de zin. "
                      "Kijk dus altijd naar wat een woord <em>doet</em>, niet naar hoe het eruitziet."),
        ]),
        dict(kop="De woordsoorten buiten het voornaamwoord", blokken=[
            ("p", tabel(["Woordsoort", "Wat het doet", "Voorbeeld"], [
                ["zelfstandig naamwoord", "benoemt een persoon, dier, ding of begrip", "de vrijheid, het paard, een idee"],
                ["bijvoeglijk naamwoord", "zegt iets over een zelfstandig naamwoord", "de <b>oude</b> molen"],
                ["werkwoord", "zegt wat er gebeurt of is", "draaien, zijn, worden"],
                ["lidwoord", "staat voor een zelfstandig naamwoord", "de, het, een, geen"],
                ["telwoord", "noemt een aantal", "veertien (bepaald), veel (onbepaald)"],
                ["voorzetsel", "geeft een verhouding aan", "op, onder, tussen, na, door"],
                ["voegwoord", "verbindt zinnen of zinsdelen", "en, maar, of, want, omdat"],
                ["bijwoord", "zegt iets over een werkwoord, een zin of een ander woord", "snel, gisteren, daar, nauwelijks"],
                ["tussenwerpsel", "drukt een gevoel of geluid uit", "oei, och, hé"],
                ["voornaamwoord", "vervangt of bepaalt een naamwoord", "ik, deze, die, zich"],
            ])),
            ("p", "Een <strong>zelfstandig naamwoord</strong> herken je aan het lidwoord dat je ervoor kan "
                  "zetten. Er zijn drie soorten <strong>lidwoorden</strong>: <strong>bepaald</strong> (de, "
                  "het), <strong>onbepaald</strong> (een) en <strong>ontkennend</strong> (geen). Een bepaald "
                  "lidwoord wijst naar iets bekends: <em>'Ik zag de hond'</em> veronderstelt dat je weet welke. "
                  "<em>'Ik zag een hond'</em> laat het open. Dat <em>geen</em> een lidwoord is, verbaast veel "
                  "mensen: het is gewoon de ontkenning van <em>een</em>. Zonder lidwoorden klinkt een zin als "
                  "telegramstijl: <em>'kat sliep op mat'</em>."),
            ("p", "Het lastigste onderscheid is dat tussen <strong>bijvoeglijk naamwoord</strong> en "
                  "<strong>bijwoord</strong>. Een bijvoeglijk naamwoord zegt iets over een zelfstandig "
                  "naamwoord, <em>nooit</em> over een werkwoord. In <em>'Hij loopt snel'</em> zegt 'snel' iets "
                  "over het werkwoord, dus is het een bijwoord; in <em>'de snelle loper'</em> is hetzelfde "
                  "woord bijvoeglijk. Hetzelfde geldt voor <em>'Gelukkig regende het niet'</em>: daar zegt "
                  "'gelukkig' iets over de hele zin, dus bijwoord. In <em>'een gelukkig kind'</em> is het "
                  "bijvoeglijk."),
            ("p", "<strong>Telwoorden</strong> zijn er ook in twee soorten. <em>Veertien</em> is bepaald: het "
                  "noemt een precies aantal. <em>Veel</em>, <em>weinig</em> en <em>enkele</em> zijn onbepaald. "
                  "Het is dus niet zo dat 'drie' een telwoord is en 'veel' een bijvoeglijk naamwoord: allebei "
                  "zijn het telwoorden."),
            ("p", "Een <strong>voorzetsel</strong> geeft een verhouding aan in plaats, tijd of richting: "
                  "<em>'De sleutel lag onder de mat'</em>, <em>'Ik wacht op de bus'</em>. Een "
                  "<strong>voegwoord</strong> verbindt: nevenschikkend zijn <em>en, maar, of, want, dus</em>, "
                  "onderschikkend <em>omdat, hoewel, als, dat</em>. Een <strong>tussenwerpsel</strong> staat "
                  "los van de zinsbouw: haal <em>oei</em> of <em>hé</em> weg en de zin blijft gewoon staan."),
        ]),
        dict(kop="De acht soorten voornaamwoorden", blokken=[
            ("p", "De vakfiche noemt er acht: <strong>persoonlijk</strong>, <strong>bezittelijk</strong>, "
                  "<strong>aanwijzend</strong>, <strong>vragend</strong>, <strong>betrekkelijk</strong>, "
                  "<strong>onbepaald</strong>, <strong>wederkerend</strong> en <strong>wederkerig</strong>. "
                  "'Bijwoordelijk' staat er niet bij."),
            ("p", tabel(["Soort", "Voorbeelden", "Herken je aan"], [
                ["persoonlijk", "ik, jij, hij, hem, wij, ons", "het vervangt een persoon"],
                ["bezittelijk", "mijn, jouw, zijn, hun", "het zegt bij wie iets hoort"],
                ["aanwijzend", "deze, dit, die, dat, zulke", "het wijst iets aan"],
                ["vragend", "wie, wat, welke", "het begint een vraag"],
                ["betrekkelijk", "die, dat, wie", "het verwijst terug én begint een bijzin"],
                ["onbepaald", "iemand, niemand, iedereen, alles, men", "geen bepaalde persoon of zaak"],
                ["wederkerend", "zich, me, je, ons", "de handeling keert terug naar het onderwerp"],
                ["wederkerig", "elkaar, mekaar", "over en weer, tussen minstens twee"],
            ])),
            ("p", "<strong>Wederkerend of wederkerig?</strong> <em>'Ze wasten zich'</em> betekent: elk "
                  "zichzelf. <em>'Ze wasten elkaar'</em> betekent: de een de ander. Die twee zijn dus "
                  "<strong>niet</strong> uitwisselbaar; <em>'Ze sloegen elkaar'</em> zegt iets heel anders dan "
                  "<em>'Ze sloegen zich'</em>. In de eerste en tweede persoon zien wederkerende voornaamwoorden "
                  "eruit als persoonlijke (<em>me</em>, <em>je</em>, <em>ons</em>), dus kijk naar wat ze doen, "
                  "niet naar hun vorm."),
            ("p", "<strong>Betrekkelijk of aanwijzend?</strong> In <em>'Het boek dat ik gisteren las, was "
                  "spannend'</em> verwijst 'dat' terug naar 'het boek' én begint het een bijzin. Dat dubbele "
                  "werk doet alleen een betrekkelijk voornaamwoord. En <strong>vragend of betrekkelijk?</strong> "
                  "In <em>'Wie heeft dat raam opengezet?'</em> begint 'wie' een vraag, dus is het vragend."),
            ("p", "<strong>Onbepaald.</strong> <em>Men</em> is <strong>geen</strong> persoonlijk maar een "
                  "onbepaald voornaamwoord, net als <em>iemand</em>, <em>niemand</em>, <em>iedereen</em> en "
                  "<em>alles</em>. In <em>'Er staat iemand aan de deur'</em> gaat het om een persoon die niet "
                  "nader bepaald wordt."),
            ("p", "<strong>Zelfstandig of bijvoeglijk gebruikt?</strong> In <em>'Mijn fiets staat buiten'</em> "
                  "staat het voornaamwoord bij een naamwoord: bijvoeglijk gebruikt. In <em>'De mijne staat "
                  "buiten'</em> vervangt het dat naamwoord: zelfstandig gebruikt. Hetzelfde bij "
                  "<em>'Die van mij is groter'</em>: 'die' staat daar alleen en vervangt bijvoorbeeld 'fiets'."),
            ("p", "Persoonlijke voornaamwoorden hebben <strong>twee vormen</strong>: een onderwerpsvorm (hij, "
                  "zij, wij) en een andere vorm (hem, haar, ons). Daarom schrijf je <em>'Ik zag hem "
                  "gisteren'</em> en niet <em>'Ik zag hij'</em>: het voornaamwoord is daar geen onderwerp."),
            ("kader", "Verwijswoorden in een tekst zijn meestal voornaamwoorden, precies omdat een "
                      "voornaamwoord een naamwoord vervangt dat eerder stond. Zo hoef je 'de burgemeester van "
                      "onze gemeente' niet in elke zin te herhalen."),
        ]),
        gesprek("leg aan iemand die jonger is dan jij uit wat een bijwoord is, met twee eigen voorbeelden en "
                "zonder dit blad erbij."),
    ],
    onthoud=[
        "Kijk naar wat een woord doet in de zin, niet naar hoe het eruitziet: hetzelfde woord kan bijwoord of bijvoeglijk naamwoord zijn.",
        "Drie lidwoorden: bepaald (de, het), onbepaald (een) en ontkennend (geen).",
        "Veel en weinig zijn onbepaalde telwoorden, geen bijvoeglijke naamwoorden.",
        "Een tussenwerpsel staat los van de zinsbouw.",
        "Acht soorten voornaamwoorden: persoonlijk, bezittelijk, aanwijzend, vragend, betrekkelijk, onbepaald, wederkerend en wederkerig.",
        "Wederkerend (zich) keert terug naar het onderwerp; wederkerig (elkaar) gaat over en weer.",
        "Men is onbepaald, niet persoonlijk. En een betrekkelijk voornaamwoord begint altijd een bijzin.",
    ],
)

# ───────────────────────── 7. Werkwoorden, tijden en woordvorming
BUNDELS["werkwoorden-tijden-en-woordvorming-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Werkwoorden, tijden en woordvorming",
    onder="De soorten werkwoorden, de zes tijden, en hoe het Nederlands nieuwe woorden maakt.",
    secties=[
        dict(kop="De persoonsvorm vinden", blokken=[
            ("p", "De <strong>persoonsvorm</strong> is het werkwoord dat in persoon en getal met het onderwerp "
                  "meegaat. Je vindt hem door de zin <strong>in een andere tijd te zetten</strong>: het "
                  "werkwoord dat verandert, is de persoonsvorm. <em>'Hij heeft gelopen'</em> wordt <em>'Hij had "
                  "gelopen'</em>: alleen 'heeft' verandert."),
            ("p", "In <strong>elke deelzin</strong> staat precies één persoonsvorm. Een samengestelde zin heeft "
                  "er dus meerdere: één per hoofdzin en één per bijzin."),
        ]),
        dict(kop="Drie soorten werkwoorden", blokken=[
            ("p", "Een <strong>zelfstandig werkwoord</strong> draagt de betekenis van de zin. In <em>'Ik heb "
                  "het boek helemaal uitgelezen'</em> is dat 'uitgelezen'; 'heb' is daar alleen "
                  "<strong>hulpwerkwoord</strong>, het helpt de voltooide tijd vormen. In <em>'Hij heeft een "
                  "fiets'</em> is datzelfde 'heeft' wél zelfstandig werkwoord."),
            ("p", "Een <strong>koppelwerkwoord</strong> koppelt het onderwerp aan een woord dat iets over dat "
                  "onderwerp zegt: <em>'Zij wordt verpleegkundige'</em>. De koppelwerkwoorden zijn "
                  "<em>zijn, worden, blijven, blijken, lijken, schijnen, heten, dunken</em> en "
                  "<em>voorkomen</em>. <em>Lopen</em> hoort er niet bij."),
        ]),
        dict(kop="De zes werkwoordstijden en de imperatief", blokken=[
            ("p", tabel(["Tijd", "Voorbeeld", "Herken je aan"], [
                ["onvoltooid tegenwoordige tijd", "Wij werken", "geen deelwoord, nu"],
                ["voltooid tegenwoordige tijd", "Wij hebben gewerkt", "deelwoord + hulpwerkwoord in de tegenwoordige tijd"],
                ["onvoltooid verleden tijd", "Wij werkten", "geen deelwoord, verleden"],
                ["voltooid verleden tijd", "Ik had gelopen", "deelwoord + hulpwerkwoord in de verleden tijd"],
                ["onvoltooid toekomende tijd", "Zij zal morgen komen", "zullen + infinitief, geen deelwoord"],
                ["voltooid toekomende tijd", "Zij zal gekomen zijn", "zullen + deelwoord"],
            ])),
            ("p", "Daarnaast is er de <strong>imperatief</strong>, de <strong>gebiedende wijs</strong>: "
                  "<em>'Kom hier'</em>, <em>'Let op'</em>. Hij heeft geen onderwerp bij zich. De imperatief is "
                  "dus <em>niet</em> de aanvoegende wijs, en een 'gebiedende toekomende tijd' bestaat niet."),
            ("p", "De <strong>infinitief</strong> is de vorm zonder persoon en zonder tijd: <em>lopen</em>, "
                  "<em>werken</em>. Dat is de vorm die in het woordenboek staat. De <strong>stam</strong> krijg "
                  "je door <em>-en</em> van de infinitief te halen: <em>wandelen</em> wordt <em>wandel</em>. De "
                  "stam is dus <strong>niet</strong> hetzelfde als de infinitief. Wat achter de stam komt, is "
                  "de <strong>uitgang</strong>; die draagt de persoon en het getal."),
        ]),
        dict(kop="Congruentie en de dt-regel", blokken=[
            ("p", "<strong>Congruentie</strong> is de overeenkomst tussen onderwerp en persoonsvorm. "
                  "<em>'De doos met oude boeken staan in de gang'</em> is fout: het onderwerp is 'de doos', "
                  "enkelvoud, niet 'boeken'."),
            ("p", "Bij de <strong>derde persoon enkelvoud</strong> komt er een <strong>-t</strong> bij de stam. "
                  "Eindigt de stam al op een d, dan zie je er twee: <em>word</em> + <em>t</em> wordt "
                  "<em>wordt</em>. Bij <em>ik word</em> komt er niets bij. En bij <strong>inversie</strong>, "
                  "als <em>je</em> of <em>jij</em> achter de persoonsvorm staat, valt de -t weg: "
                  "<em>'Word jij daar niet moe van?'</em>"),
            ("p", "Het <strong>voltooid deelwoord</strong> van een <strong>zwak</strong> werkwoord eindigt op "
                  "-d of -t: <em>gewerkt</em>, <em>gehoord</em>, <em>gebeld</em>. <strong>Sterke</strong> "
                  "werkwoorden veranderen van klinker: <em>gelopen</em>, <em>gezongen</em>, <em>gevonden</em>. "
                  "Let op het verschil tussen <em>'Er is iets gebeurd'</em> (deelwoord) en <em>'Er gebeurt "
                  "iets'</em> (persoonsvorm): allebei van hetzelfde werkwoord, maar niet dezelfde regel."),
        ]),
        dict(kop="Samenstellen en afleiden", blokken=[
            ("p", "Een <strong>samenstelling</strong> zet twee (of meer) bestaande woorden aan elkaar: "
                  "<em>boekenkast</em>, <em>tafelpoot</em>, <em>voetbalveld</em>, <em>regenjas</em>, "
                  "<em>deurklink</em>. Allebei de delen kunnen los bestaan. <em>Schoonmaakbedrijf</em> bestaat "
                  "zelfs uit <strong>drie</strong> woorden."),
            ("p", "Een <strong>afleiding</strong> gebruikt een <strong>voorvoegsel</strong> of een "
                  "<strong>achtervoegsel</strong> bij een bestaand woord: <em>on-</em> plus <em>vriendelijk</em>, "
                  "<em>her-</em> plus <em>lezen</em>, <em>schoon</em> plus <em>-heid</em>, <em>lees</em> plus "
                  "<em>-baar</em>, <em>ont-</em> plus <em>dekken</em>. Zo'n voor- of achtervoegsel kan "
                  "<strong>niet alleen staan</strong>, en dat is precies het verschil met een samenstelling. "
                  "<em>Onmogelijk</em> is dus een afleiding, geen samenstelling. En "
                  "<em>vriendelijkheid</em> is twee keer afgeleid: vriend wordt vriendelijk, vriendelijk wordt "
                  "vriendelijkheid. Er komt geen tweede woord bij."),
            ("p", "Soms staat er een <strong>tussenklank</strong> tussen de twee delen van een samenstelling, "
                  "zoals de <em>-en-</em> in <em>pannenkoek</em>. Hij hoort bij geen van beide woorden apart en "
                  "lijmt ze aan elkaar. In <em>tafelpoot</em>, <em>schoolbord</em> en <em>raamkozijn</em> zit "
                  "geen tussenklank: daar plakken de delen rechtstreeks aan elkaar."),
        ]),
        dict(kop="Meervoud, verkleinwoord, verbuiging en vervoeging", blokken=[
            ("p", "De meeste <strong>meervouden</strong> eindigen op -en of -s, maar niet alle: "
                  "<em>musea</em>, <em>kinderen</em>, <em>eieren</em>. Een handvol woorden verandert van "
                  "klinker: <em>lid</em> wordt <em>leden</em>, <em>schip</em> wordt <em>schepen</em>, "
                  "<em>stad</em> wordt <em>steden</em>. En <em>pad</em> wordt <em>paden</em>. Een meervoud op "
                  "-s krijgt nooit nog eens -en erbij."),
            ("p", "Bij een <strong>verkleinwoord</strong> op <em>-ing</em> wordt de g een k: <em>koning</em> "
                  "wordt <em>koninkje</em>, en zo ook <em>woninkje</em> en <em>leerlingetje</em>."),
            ("p", "<strong>Verbuiging</strong> is de vormverandering van naamwoorden en bijvoeglijke "
                  "naamwoorden: <em>'een mooi huis'</em> maar <em>'het mooie huis'</em>. "
                  "<strong>Vervoeging</strong> is hetzelfde, maar dan bij werkwoorden: ik werk, jij werkt, wij "
                  "werkten. Telkens dezelfde stam, telkens een andere vorm."),
            ("weetje", "Woorden met een <strong>veranderlijk woordbeeld</strong> wisselen van letter in een "
                       "andere vorm: <em>huis</em> wordt <em>huizen</em>, <em>brief</em> wordt "
                       "<em>brieven</em>, <em>graf</em> wordt <em>graven</em>. Bij <em>boek</em> blijft de k "
                       "gewoon staan."),
        ]),
        gesprek("vertel iemand iets wat gisteren gebeurd is, en let erop dat je consequent in de verleden "
                "tijd blijft. Vraag achteraf of je ergens omsloeg."),
    ],
    onthoud=[
        "De persoonsvorm vind je door de zin in een andere tijd te zetten. Eén per deelzin.",
        "Zelfstandig werkwoord draagt de betekenis, hulpwerkwoord helpt een tijd vormen, koppelwerkwoord koppelt.",
        "Zes tijden plus de imperatief. Zullen + infinitief = onvoltooid toekomende tijd.",
        "Stam = infinitief min -en. Derde persoon enkelvoud krijgt stam + t, ook als de stam al op d eindigt.",
        "Bij inversie met je of jij valt de -t weg: word jij.",
        "Samenstelling: twee echte woorden. Afleiding: een voor- of achtervoegsel dat niet alleen kan staan.",
        "Verbuiging hoort bij naamwoorden, vervoeging bij werkwoorden.",
    ],
)

# ───────────────────────── 8. Zinsdelen en samengestelde zinnen
BUNDELS["zinsdelen-en-samengestelde-zinnen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zinsdelen en samengestelde zinnen",
    onder="De zin uit elkaar halen, en het verschil tussen actief en passief, enkelvoudig en samengesteld.",
    secties=[
        dict(kop="De zinsdelen", blokken=[
            ("p", "Een <strong>zinsdeel</strong> bestaat lang niet altijd uit één woord: <em>'de hond van de "
                  "buren'</em> is één zinsdeel van vijf woorden. Je verplaatst een zinsdeel altijd in zijn "
                  "geheel, en daaraan merk je waar het begint en eindigt: <em>'De hele nacht blaft de hond van "
                  "de buren.'</em>"),
            ("p", tabel(["Zinsdeel", "Vraag", "Voorbeeld"], [
                ["onderwerp", "wie of wat + persoonsvorm?", "<b>De postbode</b> bracht mijn oma een pakje."],
                ["persoonsvorm", "welk werkwoord verandert van tijd?", "De postbode <b>bracht</b> ..."],
                ["werkwoordelijk gezegde", "wat gebeurt er?", "Hij <b>loopt</b>."],
                ["naamwoordelijk gezegde", "koppelwerkwoord + naamwoordelijk deel", "Zij <b>is verpleegkundige</b>."],
                ["lijdend voorwerp", "wie of wat + persoonsvorm + onderwerp?", "De postbode bracht mijn oma <b>een pakje</b>."],
                ["meewerkend voorwerp", "kan je er 'aan' of 'voor' voor zetten?", "Hij geeft <b>zijn beste vriend</b> een boek."],
                ["voorzetselvoorwerp", "ligt het voorzetsel vast bij het werkwoord?", "Hij wacht <b>op de trein</b>."],
                ["handelend voorwerp", "wie doet het echt, in een lijdende zin?", "De brief werd <b>door de directeur</b> ondertekend."],
                ["bijwoordelijke bepaling", "waar, wanneer, hoe, waarom?", "<b>Gisteren</b> fietste ze <b>door de regen</b> <b>naar school</b>."],
            ])),
            ("p", "Het <strong>onderwerp</strong> vind je met <em>wie of wat + persoonsvorm</em>. Let op dat je "
                  "het hele zinsdeel neemt, niet alleen het kernwoord. Het <strong>lijdend voorwerp</strong> "
                  "vind je met <em>wie of wat + persoonsvorm + onderwerp</em>: wie of wat bracht de postbode? "
                  "Een pakje. Het heet zo omdat het de handeling <em>lijdt</em>; in de lijdende vorm wordt het "
                  "het onderwerp."),
            ("p", "Het <strong>meewerkend voorwerp</strong> herken je aan de proef met <em>aan</em> of "
                  "<em>voor</em>: hij geeft een boek <em>aan</em> zijn beste vriend. Het "
                  "<strong>voorzetselvoorwerp</strong> herken je eraan dat het voorzetsel <strong>vastligt bij "
                  "het werkwoord</strong>: je wacht <em>óp</em> iets, je rekent <em>óp</em> iemand, je twijfelt "
                  "<em>áán</em> iets. In <em>'hij zit op de bank'</em> kan het voorzetsel wél wisselen (naast, "
                  "onder), en dan is het een bijwoordelijke bepaling."),
            ("p", "Een <strong>bijwoordelijke bepaling</strong> is meestal <strong>weglaatbaar</strong>. Ze is "
                  "dus niet verplicht: <em>'Gisteren fietste ze naar school'</em> blijft een zin zonder "
                  "'gisteren'. Het enige zinsdeel dat nooit ontbreekt in een Nederlandse mededelende zin is de "
                  "<strong>persoonsvorm</strong>: zonder persoonsvorm heb je geen zin maar een woordgroep."),
            ("p", "Bij een <strong>koppelwerkwoord</strong> hoort het naamwoordelijke deel bij het gezegde. In "
                  "<em>'De kinderen zijn moe'</em> is 'zijn moe' samen het <strong>naamwoordelijk "
                  "gezegde</strong>. Het verschil met een werkwoordelijk gezegde: bij een werkwoordelijk "
                  "gezegde <em>gebeurt</em> er iets, bij een naamwoordelijk gezegde wordt er iets <em>over het "
                  "onderwerp gezegd</em>."),
        ]),
        dict(kop="Actief en passief", blokken=[
            ("p", "In de <strong>bedrijvende vorm</strong> doet het onderwerp de handeling: <em>'De hond bijt "
                  "de postbode.'</em> In de <strong>lijdende vorm</strong> wordt het lijdend voorwerp het "
                  "onderwerp, en verschijnt de echte uitvoerder in een <strong>door-groep</strong>, het "
                  "handelend voorwerp: <em>'De postbode wordt door de hond gebeten.'</em>"),
            ("p", "Zet je <em>'De gemeente heeft het plein heraangelegd'</em> in de lijdende vorm, dan krijg je "
                  "<em>'Het plein is door de gemeente heraangelegd.'</em> De inhoud blijft, de nadruk "
                  "verschuift."),
            ("p", "Een lijdende zin kan het <strong>handelend voorwerp weglaten</strong>, want het onderwerp is "
                  "al bezet. <em>'De ramen werden gelapt'</em> is een volledige zin. Precies daarom gebruiken "
                  "ambtelijke teksten de lijdende vorm zo graag: <em>'Uw aanvraag werd afgewezen'</em> verzwijgt "
                  "wie besliste. Het maakt zulke teksten ook moeilijker leesbaar, en dat is wat de fiche bedoelt "
                  "met <em>passiefconstructies die een tekst moeilijker maken</em>."),
        ]),
        dict(kop="Soorten zinnen", blokken=[
            ("p", "Naar <strong>bedoeling</strong> onderscheid je: <strong>mededelende</strong>, "
                  "<strong>vragende</strong>, <strong>bevelende</strong> en <strong>uitroepende</strong> "
                  "zinnen. Daarnaast is een zin <strong>bevestigend</strong> of <strong>ontkennend</strong>."),
            ("p", "<em>'Kom onmiddellijk hier!'</em> is een <strong>bevelende</strong> zin: de persoonsvorm "
                  "staat in de gebiedende wijs en er is geen onderwerp. Het uitroepteken maakt er nog geen "
                  "uitroepende zin van. <em>'Wat is dat mooi!'</em> is wél uitroepend: de zin begint met een "
                  "vraagwoord maar vraagt niets, hij drukt verwondering uit. En niet elke vraagzin begint met "
                  "een vraagwoord: <em>'Ga jij mee?'</em> begint met de persoonsvorm."),
        ]),
        dict(kop="Enkelvoudig, samengesteld, neven- en onderschikkend", blokken=[
            ("p", "Tel de <strong>persoonsvormen</strong>. Eén betekent <strong>enkelvoudig</strong>, meer dan "
                  "één betekent <strong>samengesteld</strong>. <em>'De hond van de buren blaft de hele "
                  "nacht'</em> is enkelvoudig. <em>'Ik blijf thuis omdat het regent'</em>, <em>'Hij belde aan en "
                  "zij deed open'</em> en <em>'Toen ik binnenkwam, was iedereen al weg'</em> zijn samengesteld."),
            ("p", "Bij <strong>nevenschikking</strong> koppel je twee gelijkwaardige hoofdzinnen, met "
                  "<em>en, maar, of, want, dus</em>. Bij <strong>onderschikking</strong> hangt de ene zin van "
                  "de andere af: <em>omdat, hoewel, als, dat, toen</em>. <em>'Omdat het regende'</em> kan niet "
                  "alleen staan; zo'n zin heeft een hoofdzin nodig."),
            ("p", "Je herkent een <strong>bijzin</strong> aan het onderschikkend voegwoord vooraan en aan de "
                  "persoonsvorm achteraan: <em>'Hoewel hij doodmoe was, ging hij toch trainen.'</em> In een "
                  "<strong>hoofdzin</strong> staat de persoonsvorm op de <strong>tweede plaats</strong>; in een "
                  "bijzin schuift hij juist naar achteren."),
            ("kader", "<strong>Inversie</strong> betekent dat het onderwerp achter de persoonsvorm komt te "
                      "staan. Dat gebeurt zodra er iets anders dan het onderwerp vooraan staat: <em>'Morgen ga "
                      "ik naar de markt'</em>, niet <em>'Morgen ik ga'</em>. De persoonsvorm blijft immers op "
                      "plaats twee."),
        ]),
        gesprek("vraag iemand een lange zin uit te spreken en probeer hem samen te ontleden: onderwerp, "
                "persoonsvorm, en wat er verder in zit."),
    ],
    onthoud=[
        "Een zinsdeel verplaats je in zijn geheel. Zo weet je waar het begint en eindigt.",
        "Onderwerp: wie of wat + persoonsvorm. Lijdend voorwerp: dezelfde vraag, maar met het onderwerp erbij.",
        "Meewerkend voorwerp: er kan 'aan' of 'voor' voor. Voorzetselvoorwerp: het voorzetsel ligt vast bij het werkwoord.",
        "De bijwoordelijke bepaling is meestal weglaatbaar. Alleen de persoonsvorm ontbreekt nooit.",
        "In de lijdende vorm wordt het lijdend voorwerp onderwerp en komt de uitvoerder in een door-groep.",
        "Tel de persoonsvormen: één = enkelvoudig, meer = samengesteld.",
        "Hoofdzin: persoonsvorm op plaats twee. Bijzin: persoonsvorm achteraan. Inversie: onderwerp achter de persoonsvorm.",
    ],
)

# ───────────────────────── 9. Spelling, leestekens en klanken
BUNDELS["spelling-leestekens-en-klanken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Spelling, leestekens en klanken",
    onder="Hoofdletters, werkwoordspelling, de tekens boven en naast de letters, en wat je hoort tegenover wat je ziet.",
    secties=[
        dict(kop="Veranderlijk woordbeeld", blokken=[
            ("p", "Een woord met een <strong>veranderlijk woordbeeld</strong> krijgt andere letters in een "
                  "andere vorm. De s wordt een z, de f wordt een v: <em>huis</em> wordt <em>huizen</em>, "
                  "<em>brief</em> wordt <em>brieven</em>, <em>graf</em> wordt <em>graven</em>. Bij "
                  "<em>boek</em> blijft de k gewoon staan. Je hoort het verschil, en je schrijft het ook."),
        ]),
        dict(kop="Hoofdletters", blokken=[
            ("p", tabel(["Wel een hoofdletter", "Geen hoofdletter"], [
                ["talen: Nederlands, Frans, Spaans", "dagen: maandag, woensdag"],
                ["landen en streken: België, de Ardennen", "maanden: januari, juni"],
                ["plaatsnamen: Madrid, Hasselt", "seizoenen: lente, winter"],
                ["feestdagen: Kerstmis, Pasen", "beroepen: dokter, leerkracht"],
            ])),
            ("p", "Namen van <strong>talen</strong> krijgen dus wél een hoofdletter, want ze zijn afgeleid van "
                  "een aardrijkskundige naam. Namen van <strong>dagen en maanden</strong> krijgen er géén. "
                  "<em>'In januari leert hij Spaans in Madrid'</em> en <em>'Met Pasen gaan we naar de "
                  "Ardennen'</em> zijn dus allebei juist geschreven."),
        ]),
        dict(kop="Diakritische tekens en uitspraaktekens", blokken=[
            ("p", "<strong>Diakritische tekens</strong> veranderen de letter zelf niet; ze zeggen hoe je hem "
                  "moet lezen. De drie belangrijkste zijn het <strong>trema</strong>, het "
                  "<strong>koppelteken</strong> en de <strong>apostrof</strong>."),
            ("p", "Een <strong>trema</strong> zegt: begin hier een nieuwe klank. Zonder trema zou je "
                  "<em>ruïne</em> lezen als 'rui'. Zo ook <em>reünie</em>, <em>zeeën</em> en "
                  "<em>geëerd</em> (ge-eerd). Maar dat geldt alleen <strong>binnen één woorddeel</strong>. "
                  "Tussen twee delen van een <strong>samenstelling</strong> gebruik je een "
                  "<strong>koppelteken</strong>, om klinkerbotsing te vermijden: <em>zee-eend</em>, "
                  "<em>na-apen</em>, <em>auto-ongeval</em>."),
            ("p", "Een <strong>apostrof</strong> houdt de klank van een klinker open (<em>Anna's fiets</em>: "
                  "zonder apostrof zou je 'Annas' lezen met een korte a) of vervangt weggelaten letters. "
                  "<em>'s morgens</em> is de juiste schrijfwijze, met de apostrof vooraan en een spatie erna: "
                  "hij vervangt de weggelaten letters van het oude <em>des</em>."),
            ("p", "Een <strong>accentteken</strong> is een <strong>uitspraakteken</strong>: het legt nadruk. "
                  "<em>'Ik heb één boek'</em> betekent iets anders dan <em>'Ik heb een boek'</em>."),
        ]),
        dict(kop="Werkwoordspelling", blokken=[
            ("p", "Bij de <strong>derde persoon enkelvoud</strong> komt er een -t bij de stam, ook als die al "
                  "op een d eindigt: <em>'Hij wordt morgen zestien jaar'</em>. Staat <em>je</em> of "
                  "<em>jij</em> achter de persoonsvorm, dan valt die -t weg: <em>'Word jij daar niet moe "
                  "van?'</em>"),
            ("p", "Het <strong>voltooid deelwoord</strong> volgt het hele werkwoord, niet de klank. "
                  "<em>'Er is iets gebeurd'</em> (van gebeuren, dus -d) tegenover <em>'Er gebeurt iets'</em> "
                  "(persoonsvorm, stam + t). En na <em>heb</em> staat altijd een deelwoord: <em>'Ik heb me "
                  "verheugd'</em>, nooit 'verheugt'."),
            ("p", "In de <strong>verleden tijd</strong> komt er -de of -te bij de stam. Eindigt de stam op een "
                  "medeklinker uit 't kofschip, dan wordt het -te; anders -de. Eindigt de stam al op een d, dan "
                  "krijg je er twee: <em>bereid</em> + <em>de</em> wordt <em>'ik bereidde'</em>. En let op "
                  "<em>verhuizen</em>: de stam eindigt op een z, die niet in 't kofschip zit, dus komt er -de "
                  "bij. Aan het einde van een lettergreep schrijf je die z als s: <em>verhuisde</em>."),
        ]),
        dict(kop="De leestekens", blokken=[
            ("p", "De vakfiche noemt deze <strong>interpunctietekens</strong>: de <strong>punt</strong>, de "
                  "<strong>komma</strong>, het <strong>vraagteken</strong>, het <strong>uitroepteken</strong>, "
                  "de <strong>dubbele punt</strong>, de <strong>spatie</strong>, het "
                  "<strong>aanhalingsteken</strong>, het <strong>beletselteken</strong> en het "
                  "<strong>gedachtestreepje</strong>. Een accentteken staat er niet bij: dat is een "
                  "uitspraakteken."),
            ("p", "Ja, ook de <strong>spatie</strong> staat in die lijst. Een spatie te veel of te weinig "
                  "verandert 'een bejaardentehuis' in iets anders."),
            ("p", "Een <strong>komma</strong> kan de betekenis van een zin veranderen: vergelijk <em>'We eten, "
                  "oma'</em> met <em>'We eten oma'</em>. Ze scheidt ook de bijzin van de hoofdzin: <em>'Toen de "
                  "bel ging, stond iedereen op'</em> en <em>'Hoewel het goot, gingen we toch buiten spelen'</em>. "
                  "Staat de bijzin vooraan, dan komt er een komma voor de hoofdzin begint."),
            ("p", "De <strong>dubbele punt</strong> kondigt aan: een opsomming, een verklaring of een citaat. "
                  "Er mag dus nooit niets op volgen. <strong>Aanhalingstekens</strong> zet je rond de "
                  "<em>letterlijke</em> woorden van iemand anders: <em>Hij zei: “Ik kom morgen.”</em> Verander "
                  "je er iets aan, dan mogen ze er niet meer staan."),
            ("p", "Het <strong>beletselteken</strong> (drie puntjes) laat een zin onafgemaakt of geeft "
                  "aarzeling weer. Het <strong>gedachtestreepje</strong> is langer dan een koppelteken en zet "
                  "een tussenzin of een onderbreking apart, zonder haakjes."),
            ("p", "Een <strong>vraagteken</strong> hoort alleen achter een echte vraag. Achter een "
                  "<strong>indirecte</strong> vraag komt een punt: <em>'Hij vroeg of ik meekwam.'</em> Er wordt "
                  "daar niets gevraagd; er wordt verteld dát er iets gevraagd werd."),
        ]),
        dict(kop="Klanken: wat je hoort tegenover wat je ziet", blokken=[
            ("p", "Het Nederlands heeft zes <strong>klinkerletters</strong>: a, e, i, o, u en y. Alle andere "
                  "letters zijn <strong>medeklinkers</strong>."),
            ("p", "Klinkers zijn <strong>lang</strong> of <strong>kort</strong>. In <em>maan</em> staat een "
                  "lange aa, in <em>man</em> een korte a; in <em>boot</em> een lange oo, in <em>bot</em> een "
                  "korte o. Allebei die lettergrepen zijn gesloten, en daarom moet de lange klank met twee "
                  "letters geschreven worden."),
            ("p", "Een lettergreep is <strong>open</strong> als ze op een klinker eindigt (<em>lo-pen</em>, "
                  "<em>ta-fel</em>) en <strong>gesloten</strong> als ze op een medeklinker eindigt "
                  "(<em>stop-pen</em>, <em>man</em>). Daarop staan twee regels. In een open lettergreep "
                  "schrijf je een lange klank met één letter: <em>lo-pen</em>, niet 'loopen'. En na een korte "
                  "klank <strong>verdubbelt</strong> de medeklinker, zodat de lettergreep gesloten blijft en "
                  "de klank kort: <em>stop-pen</em>, <em>man-nen</em>, <em>bak-ker</em>. Schrijf je "
                  "'stopen', dan lees je vanzelf een lange o."),
            ("p", "Daarnaast is er de <strong>doffe klank</strong>: de onbeklemtoonde e, zoals in <em>de</em> "
                  "en in de laatste lettergreep van <em>lopen</em>. Hij draagt nooit de klemtoon, en daarom "
                  "hoor je hem amper terwijl hij bijna overal zit."),
            ("p", "Het onderscheid tussen <strong>klankbeeld</strong> en <strong>schriftbeeld</strong> is: hoe "
                  "een woord <em>klinkt</em> tegenover hoe je het <em>schrijft</em>. In <em>maan</em> hoor je "
                  "drie klanken maar zie je vier letters; in <em>hij</em> hoor je er twee en zie je er drie."),
            ("p", "<strong>Intonatie</strong> ten slotte geeft betekenis en gevoel mee aan dezelfde woorden. "
                  "<em>'Je komt mee'</em> kan een mededeling, een vraag of een bevel zijn; alleen de toon maakt "
                  "het verschil. Je maakt er hoorbaar een vraag van door de toon aan het einde omhoog te laten "
                  "gaan. In geschreven taal moet een vraagteken dat werk overnemen."),
        ]),
        gesprek("dicteer iemand een kort stukje tekst en laat het daarna omgekeerd doen. Bespreek samen waar "
                "jullie twijfelden."),
    ],
    onthoud=[
        "Veranderlijk woordbeeld: huis-huizen, brief-brieven, graf-graven.",
        "Talen, landen en feestdagen krijgen een hoofdletter; dagen en maanden niet.",
        "Trema binnen één woorddeel (zeeën), koppelteken tussen twee delen van een samenstelling (zee-eend).",
        "Derde persoon enkelvoud: stam + t, ook bij een stam op d. Bij inversie met je of jij valt de t weg.",
        "De spatie staat óók in de lijst van interpunctietekens.",
        "Aanhalingstekens alleen rond letterlijke woorden. Achter een indirecte vraag komt een punt.",
        "Zes klinkerletters. Lang, kort en dof. Klankbeeld is niet hetzelfde als schriftbeeld.",
    ],
)

# ───────────────────────── 10. Betekenis, beeldspraak en gevoelswaarde
BUNDELS["betekenis-beeldspraak-en-gevoelswaarde-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Betekenis, beeldspraak en gevoelswaarde",
    onder="Synoniemen en homoniemen, beelden en uitdrukkingen, humor, en woorden die al een oordeel meedragen.",
    secties=[
        dict(kop="Betekenisrelaties", blokken=[
            ("p", "<strong>Synoniemen</strong> betekenen ongeveer hetzelfde. Ongeveer, want ze verschillen vaak "
                  "in register of gevoelswaarde: <em>beginnen</em>, <em>starten</em>, <em>aanvangen</em> en "
                  "<em>van wal steken</em> zijn synoniemen, maar 'aanvangen' klinkt formeel en 'van wal steken' "
                  "beeldend."),
            ("p", "<strong>Antoniemen</strong> zijn het tegengestelde: licht en donker, stijgen en dalen, "
                  "<em>zuinig</em> en <em>verkwistend</em>, <em>tijdelijk</em> en <em>blijvend</em>. Let op: "
                  "<em>spaarzaam</em> is géén antoniem van zuinig maar een synoniem, en <em>kortstondig</em>, "
                  "<em>voorlopig</em> en <em>vluchtig</em> betekenen ongeveer hetzelfde als tijdelijk."),
            ("p", "<strong>Homoniemen</strong> zien er hetzelfde uit maar betekenen iets anders: de "
                  "<em>bank</em> om op te zitten en de <em>bank</em> met geld; het <em>slot</em> van een deur, "
                  "een kasteel of het einde van een verhaal; <em>kussen</em> als ding en als werkwoord. Alleen "
                  "de <strong>context</strong> maakt duidelijk welke betekenis geldt, en precies daarom zijn "
                  "homoniemen zo bruikbaar voor woordspelingen."),
        ]),
        dict(kop="Letterlijk en figuurlijk", blokken=[
            ("p", "<em>'Het regent pijpenstelen'</em> gebruik je niet letterlijk: er vallen geen pijpenstelen "
                  "uit de lucht. In <em>'Geduld is de sleutel tot succes'</em> staat geen echte sleutel; het "
                  "woord staat er als beeld voor wat een deur opent."),
            ("p", "Een <strong>uitdrukking</strong> is een vaste woordgroep die je in je eigen zin inpast: "
                  "<em>in het oog springen</em>, <em>de kat uit de boom kijken</em> (eerst afwachten hoe iets "
                  "loopt), <em>de pijp aan Maarten geven</em>. Haar betekenis volgt <strong>niet</strong> uit "
                  "de losse woorden, en daarom leer je ze als geheel en kan je ze meestal niet letterlijk "
                  "vertalen: het Engels zegt <em>'it's raining cats and dogs'</em> waar wij pijpenstelen zien."),
            ("p", "Een <strong>spreekwoord</strong> is een <strong>volledige zin</strong> met een levensles "
                  "erin, die je niet verandert: <em>'Wie het kleine niet eert, is het grote niet weerd'</em>, "
                  "<em>'Hoge bomen vangen veel wind'</em>. Dat is het verschil met een uitdrukking."),
        ]),
        dict(kop="Beeldspraak", blokken=[
            ("p", "Bij een <strong>vergelijking</strong> staat er een woordje als <em>als</em> of "
                  "<em>zoals</em>: <em>'Hij is zo sterk als een beer.'</em> Bij een <strong>metafoor</strong> "
                  "valt dat woordje weg en wordt het beeld de zaak zelf: <em>'Hij is een beer'</em>, "
                  "<em>'Zij is een engel'</em>, <em>'een zee van tijd'</em>. Bij een "
                  "<strong>personificatie</strong> krijgt een ding of een dier menselijke eigenschappen: "
                  "<em>'De wind fluisterde door de bomen'</em>, de zon lacht, de stad slaapt."),
            ("p", "Beeldspraak doet iets met je gevoel wat een cijfer niet doet. <em>'Een zee van tijd'</em> "
                  "laat de hoeveelheid aanvoelen als iets eindeloos. Daarom is beeldspraak ook een van de "
                  "middelen waarmee een schrijver <strong>subjectief</strong> wordt."),
            ("kader", "Niet elke zin met sterke woorden is beeldspraak. <em>'De hond blafte luid naar de "
                      "postbode'</em> bedoelt precies wat er staat."),
        ]),
        dict(kop="Humor in taal", blokken=[
            ("p", "De vakfiche noemt drie vormen: <strong>ironie</strong>, <strong>taalhumor</strong> en "
                  "<strong>parodie</strong>. Daarnaast staan bij de semantiek nog <strong>overdrijving</strong> "
                  "en <strong>woordspeling</strong>."),
            ("p", "Bij <strong>ironie</strong> zeg je het <strong>omgekeerde</strong> van wat je bedoelt, en "
                  "reken je erop dat de ander dat doorheeft: naar buiten kijken waar het giet en zeggen "
                  "<em>'Wat een prachtig weertje.'</em> In geschreven tekst hoor je de toon niet; daar herken je "
                  "ironie aan het verschil tussen wat er staat en wat je uit de context weet. Wie die context "
                  "niet kent, mist ze, en daarom loopt ironie op sociale media zo vaak verkeerd af."),
            ("p", "Een <strong>overdrijving</strong> versterkt het gevoel, niet het feit: <em>'Ik heb je dat "
                  "al duizend keer gezegd.'</em> Ze maakt een tekst subjectiever, en daarom zie je ze vaak in "
                  "reclame en columns en zelden in een informatieve tekst."),
            ("p", "Een <strong>woordspeling</strong> speelt met de dubbele betekenis van een woord. Ze leunt "
                  "vaak op homoniemen, en werkt daarom <strong>zelden in een andere taal</strong>: ze hangt "
                  "vast aan de klank en de betekenissen van precies dat woord. <strong>Taalhumor</strong> is "
                  "breder: humor die uit de taal zelf komt en niet uit de situatie. Een <strong>parodie</strong> "
                  "is een grappige nabootsing van een bekende stijl of een bekend werk; ze leunt op herkenning."),
            ("p", "Let op: een <strong>personificatie</strong> is beeldspraak, geen humor. De fiche zet die "
                  "twee in aparte lijstjes."),
        ]),
        dict(kop="Gevoelswaarde en herkomst", blokken=[
            ("p", "De <strong>gevoelswaarde</strong> of <strong>connotatie</strong> van een woord is wat het "
                  "oproept naast zijn letterlijke betekenis. <em>Goedkoop</em> en <em>voordelig</em> betekenen "
                  "ongeveer hetzelfde, maar 'goedkoop' suggereert ook slechte kwaliteit."),
            ("p", tabel(["Neutraal", "Verzacht (eufemisme)", "Verscherpt (dysfemisme)"], [
                ["ontslagen", "herstructurering", "op straat gezet"],
                ["prijsverhoging", "prijsaanpassing", "graaien"],
                ["betrokken burger", "—", "bemoeial"],
                ["volhardend", "—", "koppig"],
                ["gul", "—", "spilzuchtig"],
            ])),
            ("p", "Een <strong>eufemisme</strong> verzacht iets onaangenaams; een <strong>dysfemisme</strong> "
                  "doet het omgekeerde. Een columnist die een nieuwe wet <em>'een gedrocht'</em> noemt, kiest "
                  "een woord met een sterk negatieve gevoelswaarde: het feit blijft staan, het oordeel zit "
                  "volledig in de woordkeuze."),
            ("p", "Naar <strong>herkomst</strong> zijn woorden <strong>inheems</strong> of "
                  "<strong>leenwoord</strong>. Inheemse woorden horen van oudsher bij de taal: <em>huis</em>, "
                  "<em>water</em>, <em>moeder</em>, <em>boom</em>. Leenwoorden zijn uit een andere taal "
                  "overgenomen: <em>computer</em> uit het Engels, <em>paraplu</em> uit het Frans, "
                  "<em>sowieso</em> uit het Duits."),
            ("p", "Ken je een woord niet, dan leid je de betekenis af uit de <strong>context</strong>, je "
                  "<strong>voorkennis</strong> en de <strong>bouw</strong> van het woord. Zie je <em>on-</em> "
                  "vooraan of <em>-baar</em> achteraan, dan weet je al iets. En soms helpt je kennis van het "
                  "Frans of het Engels."),
        ]),
        gesprek("leg een Nederlandse uitdrukking uit aan iemand die ze niet kent, zonder ze te gebruiken in "
                "je uitleg."),
    ],
    onthoud=[
        "Synoniem = ongeveer hetzelfde, antoniem = tegengesteld, homoniem = zelfde vorm, andere betekenis.",
        "Een uitdrukking pas je in je eigen zin in; een spreekwoord is een volledige zin met een les.",
        "Vergelijking heeft 'als' of 'zoals', een metafoor niet. Personificatie geeft dingen menselijke trekken.",
        "Ironie zegt het omgekeerde. Een woordspeling leunt op homoniemen en overleeft geen vertaling.",
        "Connotatie is de gevoelswaarde naast de letterlijke betekenis. Eufemisme verzacht, dysfemisme verscherpt.",
        "Inheemse woorden horen van oudsher bij de taal; leenwoorden komen uit een andere taal.",
    ],
)

# ───────────────────────── 11. Verhalen ontleden
BUNDELS["verhalen-ontleden-verteller-tijd-en-ruimte-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Verhalen ontleden: verteller, tijd en ruimte",
    onder="Personages, spanning, tijd, ruimte en vertelperspectief: de begrippen om over een verhaal te praten.",
    secties=[
        dict(kop="Fictie en non-fictie", blokken=[
            ("p", "<strong>Fictie</strong> is verzonnen; <strong>non-fictie</strong> doet uitspraken over de "
                  "werkelijkheid en kan dus juist of fout zijn. Een <strong>historische roman</strong> gaat "
                  "over echte gebeurtenissen en blijft toch fictie, want de personages en de gesprekken zijn "
                  "bedacht. Een biografie, een reportage en een handleiding zijn non-fictie, een sprookje niet."),
            ("p", "Non-fictie kan wel degelijk spannend zijn: een true crime podcast of een reportage over een "
                  "ramp gebruikt dezelfde middelen als een roman."),
            ("p", "De <strong>verhaallijn</strong> is het geheel van gebeurtenissen dat het verhaal draagt. Een "
                  "verhaal kan meerdere verhaallijnen hebben die elkaar afwisselen en op het einde samenkomen."),
        ]),
        dict(kop="Personages", blokken=[
            ("p", "De <strong>protagonist</strong> is de hoofdpersoon; het woord komt uit het Griekse theater "
                  "en betekent 'de eerste speler'. De <strong>antagonist</strong> werkt hem tegen. Dat hoeft "
                  "geen persoon te zijn: ook de natuur of een ziekte kan die rol spelen. In een verhaal waarin "
                  "een rechercheur een seriemoordenaar zoekt, is de moordenaar de antagonist."),
            ("p", "Een <strong>held</strong> heeft de klassieke heldeneigenschappen. Een "
                  "<strong>antiheld</strong> heeft ze niet: hij is bang, twijfelt of maakt verkeerde keuzes, en "
                  "draagt toch het verhaal. Lezers vinden hem vaak geloofwaardiger, omdat hij twijfels en "
                  "gebreken heeft zoals zij. Een held zonder zwaktes is makkelijk te bewonderen en moeilijk te "
                  "herkennen."),
            ("p", "Een <strong>rond personage</strong> heeft meerdere, soms tegenstrijdige eigenschappen, "
                  "verandert in de loop van het verhaal, en je leert ook zijn binnenkant kennen. Een "
                  "<strong>vlak personage</strong> blijft zichzelf van begin tot eind: de knecht die de grappige "
                  "sukkel blijft. Rond of vlak gaat over <strong>diepte</strong>, niet over belang: ook een "
                  "bijfiguur kan rond zijn, en een hoofdpersoon kan vlak blijven. Vlakke personages zijn geen "
                  "fout; ze houden het verhaal overzichtelijk."),
        ]),
        dict(kop="Spanningsopbouw", blokken=[
            ("p", "De <strong>spanningsboog</strong> is het verloop van de spanning van begin tot ontknoping. "
                  "Ze loopt op naar de <strong>climax</strong>, het hoogtepunt, en zakt daarna weer. Een "
                  "<strong>cliffhanger</strong> is een hoofdstuk of aflevering die afbreekt op het spannendste "
                  "moment, en houdt de spanning tussendoor omhoog."),
            ("p", "<strong>Kennisvoorsprong</strong> betekent dat de <em>lezer meer weet dan het "
                  "personage</em>: jij ziet de moordenaar achter de deur staan en zij niet. Daardoor wordt elke "
                  "gewone handeling plots spannend, en wil je bijna roepen dat ze zich moet omdraaien. "
                  "<strong>Kennisachterstand</strong> is het omgekeerde: de lezer weet <em>minder</em> dan een "
                  "personage, en leest verder om te weten te komen wat dat personage allang weet."),
            ("p", "Het <strong>genre</strong> van een tekst is de soort waartoe hij hoort, met de verwachtingen "
                  "die daarbij horen. Bij een detective verwacht je een misdaad en een oplossing; wie die "
                  "verwachting breekt, doet dat met opzet."),
        ]),
        dict(kop="Tijd in een verhaal", blokken=[
            ("p", "<strong>Chronologisch</strong> vertellen is: in de volgorde waarin de gebeurtenissen "
                  "plaatsvonden. Drie dingen doorbreken die volgorde. Een <strong>flashback</strong> blikt "
                  "terug naar iets van vóór het verhaalheden. Een <strong>flashforward</strong> wijst vooruit "
                  "naar wat nog komen moet. Een <strong>tijdsprong</strong> slaat een stuk tijd gewoon over: "
                  "<em>'Drie jaar later'</em>."),
            ("p", "<strong>Verteltijd</strong> is hoe lang je erover leest; <strong>vertelde tijd</strong> is "
                  "hoeveel tijd er in het verhaal voorbijgaat. Die twee zijn bijna nooit even lang. Twintig "
                  "bladzijden over één nacht: veel verteltijd, weinig vertelde tijd. <em>'Twintig jaar gingen "
                  "voorbij'</em> in één zin: veel vertelde tijd in heel weinig verteltijd, en dus blijkbaar niet "
                  "belangrijk voor het verhaal. Waar een schrijver vertraagt of versnelt, zie je waar hij de "
                  "nadruk legt."),
        ]),
        dict(kop="Ruimte", blokken=[
            ("p", "De fiche onderscheidt vier soorten ruimte. De <strong>geografische</strong> ruimte is de "
                  "plaats zelf. De <strong>sociale</strong> ruimte zegt iets over de stand van de personages: "
                  "een verpauperde achterbuurt. De <strong>symbolische</strong> ruimte staat voor iets anders: "
                  "een muur voor een scheiding, een brug, een eiland, een kelder. De "
                  "<strong>sfeerscheppende</strong> ruimte roept vooral een stemming op: een donker bos in een "
                  "griezelverhaal."),
            ("kader", "Dezelfde plaats kan tegelijk geografisch (een stad), sociaal (arm) en sfeerscheppend "
                      "(somber) zijn. Je kiest dus de soort die in die zin het meeste doet."),
        ]),
        dict(kop="Het vertelperspectief", blokken=[
            ("p", tabel(["Perspectief", "Voorbeeldzin", "Weet"], [
                ["belevende ik-verteller", "Ik zag de klink bewegen en mijn hart bonsde.", "alleen wat hij nu meemaakt"],
                ["vertellende ik-verteller", "Toen wist ik nog niet dat het mijn laatste zomer was.", "kent de afloop al"],
                ["personele hij/zij-verteller", "Hij hoorde iets in de gang en bleef stokstijf staan.", "alleen wat dat ene personage weet"],
                ["alwetende verteller", "Terwijl hij wachtte, besloot zij elders het tegenovergestelde.", "alles, van iedereen"],
            ])),
            ("p", "Een <strong>ik-verteller</strong> weet <strong>niet</strong> wat de anderen denken. Hij kan "
                  "alleen gissen, en dat maakt hem onbetrouwbaar op een manier die schrijvers graag uitbuiten. "
                  "Bij een <strong>personele</strong> verteller lees je 'hij' en 'zij', maar zie en weet je "
                  "alleen wat dat ene personage ziet en weet: je kijkt mee over zijn schouder. Een "
                  "<strong>alwetende</strong> verteller staat buiten het verhaal en kan in het hoofd van "
                  "iedereen kijken; zo kan een schrijver kennisvoorsprong opbouwen, of twee verhaallijnen naast "
                  "elkaar leggen die de personages niet van elkaar kennen."),
        ]),
        dict(kop="Prozagenres", blokken=[
            ("p", "Bij de <strong>fictiegenres</strong> noemt de fiche onder meer: <strong>roman</strong>, <strong>kortverhaal</strong>, "
                  "<strong>sprookje</strong>, <strong>mythe</strong>, <strong>sciencefiction</strong>, "
                  "<strong>crimefiction</strong>, <strong>detective</strong>, <strong>graphic novel</strong>, "
                  "<strong>historische roman</strong>, <strong>gothic novel</strong>, "
                  "<strong>avonturenroman</strong>, <strong>oorlogsroman</strong>, <strong>fabel</strong>, "
                  "<strong>sage</strong>, <strong>legende</strong> en <strong>dierenepiek</strong>."),
            ("p", "Een <strong>fabel</strong> vertelt over dieren die zich als mensen gedragen en eindigt met "
                  "een les, de <strong>moraal</strong>: de vos en de raaf, de haas en de schildpad."),
        ]),
        gesprek("vertel iemand een boek of een film na zonder het einde te verklappen, en let erop dat je de "
                "spanning erin houdt."),
    ],
    onthoud=[
        "Fictie is verzonnen; een historische roman blijft fictie. Non-fictie kan evengoed spannend zijn.",
        "Protagonist en antagonist. Een antiheld is de hoofdpersoon zonder heldeneigenschappen.",
        "Rond personage: meerdere eigenschappen, groeit. Vlak personage: blijft zichzelf.",
        "Kennisvoorsprong: de lezer weet meer dan het personage. Kennisachterstand: minder.",
        "Flashback, flashforward en tijdsprong doorbreken de chronologie.",
        "Verteltijd is hoe lang je leest, vertelde tijd hoeveel tijd er voorbijgaat.",
        "Vier soorten ruimte: geografisch, sociaal, symbolisch en sfeerscheppend.",
        "Vier vertelperspectieven: belevende ik, vertellende ik, personeel en alwetend.",
    ],
)

# ───────────────────────── 12. Poëzie, drama en literaire stromingen
BUNDELS["poezie-drama-en-literaire-stromingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Poëzie, drama en literaire stromingen",
    onder="Dichtvormen en rijm, het toneel op de planken, en de drie stromingen die je moet kunnen toepassen.",
    secties=[
        dict(kop="Dichtvormen", blokken=[
            ("p", tabel(["Vorm", "Kenmerk"], [
                ["haiku", "drie regels, vijf-zeven-vijf lettergrepen, geen rijm, meestal een natuurbeeld"],
                ["limerick", "vijf regels, rijmschema aabba, grappig, met de clou op het einde"],
                ["ballade", "een verhalend gedicht, vaak met een refrein"],
                ["naamdicht of acrostichon", "de beginletters van de regels vormen samen een woord"],
                ["vrij vers", "geen vast rijm en geen vaste maat"],
                ["sonnet", "veertien versregels, meestal een octaaf van acht en een sextet van zes"],
                ["minneliederen", "middeleeuwse liederen over de liefde"],
            ])),
            ("p", "Let op de valstrik: een <strong>klucht</strong> is geen dichtvorm maar een toneelvorm."),
        ]),
        dict(kop="Rijm, ritme en strofen", blokken=[
            ("p", "<strong>Eindrijm</strong> is rijm aan het einde van de versregels; <strong>volrijm</strong> "
                  "is rijm waarbij de hele klank vanaf de beklemtoonde klinker gelijk is. Daarnaast zijn er "
                  "drie <strong>rijmschema's</strong>: <strong>gepaard</strong> rijm is aabb, "
                  "<strong>gekruist</strong> rijm is abab (het rijm springt telkens een regel over), en "
                  "<strong>omarmend</strong> rijm is abba (de buitenste twee regels sluiten de binnenste in, "
                  "als armen eromheen). 'Blank rijm' staat niet in de lijst van de fiche."),
            ("p", "<strong>Alliteratie</strong> is dezelfde <em>beginmedeklinker</em> in woorden vlak na "
                  "elkaar: <em>ruisend riet</em>, <em>tussen twee torens</em>. <strong>Assonantie</strong> is "
                  "de tegenhanger: dezelfde <em>klinkerklank</em> in woorden vlak na elkaar. Allebei maken ze "
                  "een regel hoorbaar, ook zonder eindrijm."),
            ("p", "Bij het <strong>ritme</strong> hoort het <strong>enjambement</strong>: een zin die doorloopt "
                  "over het einde van de versregel heen. De regel breekt af waar de zin nog niet af is, en die <strong>breuk</strong> "
                  "legt nadruk op het woord er vlak voor en er vlak na. Je oog valt van de regel af terwijl de zin "
                  "doorloopt; die kleine aarzeling is het effect."),
            ("p", "Een <strong>vers</strong> is één regel, een <strong>strofe</strong> een groepje regels. In "
                  "de poëzie betekent 'vers' dus niet hetzelfde als in het dagelijks taalgebruik, waar het vaak "
                  "het hele gedicht aanduidt. De strofevormen: een <strong>terzine</strong> telt drie regels, "
                  "een <strong>kwatrijn</strong> vier, een <strong>sextet</strong> zes en een "
                  "<strong>octaaf</strong> acht. Twee kwatrijnen vormen samen het octaaf van een sonnet; twee "
                  "terzinen samen het sextet. Een <strong>refrein</strong> is een regel of strofe die telkens "
                  "terugkeert."),
            ("p", "De <strong>stijlfiguren</strong> die de fiche noemt zijn: <strong>beeldspraak</strong>, "
                  "<strong>vergelijking</strong>, <strong>metafoor</strong>, <strong>woordspeling</strong>, "
                  "<strong>herhaling</strong>, <strong>personificatie</strong> en <strong>overdrijving</strong>. "
                  "Het enjambement staat er niet bij: dat hoort onder ritme."),
        ]),
        dict(kop="Drama", blokken=[
            ("p", "Vier subgenres. Een <strong>tragedie</strong> loopt slecht af voor de hoofdpersoon, die ten "
                  "onder gaat, vaak door een eigenschap die hem eerst juist groot maakte. Een "
                  "<strong>komedie</strong> loopt goed af, hoe veel er onderweg ook misgaat. Een "
                  "<strong>klucht</strong> is een kort toneelstuk met grove, volkse humor, vol misverstanden, "
                  "verkleedpartijen en herkenbare types. <strong>Muziektheater</strong> is toneel waarin "
                  "gezongen wordt, zoals een musical of een opera."),
            ("p", "Bij een <strong>opvoeringsanalyse</strong> kijk je juist naar alles wat de tekst "
                  "<em>niet</em> is: <strong>decor</strong>, <strong>belichting</strong>, "
                  "<strong>ruimte</strong>, <strong>rekwisieten</strong>, <strong>mimiek</strong>, "
                  "<strong>gebaren</strong>, <strong>kostumering</strong>, <strong>grime</strong>, "
                  "<strong>muziek en geluid</strong>."),
            ("p", "<strong>Rekwisieten</strong> zijn de voorwerpen die de spelers gebruiken: een brief, een "
                  "glas, een wapen. De kleren heten <strong>kostumering</strong>, en de schmink waarmee een "
                  "acteur er ouder of anders uitziet is de <strong>grime</strong>. Samen bepalen die twee hoe "
                  "een personage er van ver uitziet, en ze zeggen iets over zijn stand, zijn tijd en zijn "
                  "karakter nog voor hij iets gezegd heeft."),
            ("p", "<strong>Belichting</strong> stuurt de aandacht en bepaalt de sfeer: één lichtbundel op één "
                  "speler zegt 'kijk hier', en koud blauw licht zegt iets anders dan warm geel. "
                  "<strong>Mimiek</strong> is belangrijk omdat een gezicht iets anders kan zeggen dan de "
                  "woorden: een personage dat <em>'het gaat prima'</em> zegt met angst op zijn gezicht, vertelt "
                  "je twee dingen tegelijk."),
        ]),
        dict(kop="Drie literaire stromingen", blokken=[
            ("p", "De fiche vraagt dat je de kenmerken van drie stromingen op een tekst kan toepassen: de "
                  "<strong>middeleeuwen</strong>, de <strong>romantiek</strong> en het "
                  "<strong>realisme</strong>. De barok staat er niet bij."),
            ("p", tabel(["Stroming", "Kenmerken", "Herken je aan"], [
                ["middeleeuwen", "getallensymboliek, dubbele gelaagdheid, hoofse liefde", "drie, zeven en twaalf duiken niet toevallig op"],
                ["romantiek", "gevoel, verbeelding, het verlangende individu", "dromerig verlangen, natuur, het verre en het verleden"],
                ["realisme", "de werkelijkheid zoals ze is", "sociale wantoestanden, zoals kinderarbeid"],
            ])),
            ("p", "<strong>Getallensymboliek</strong> is de betekenis die middeleeuwse teksten aan bepaalde "
                  "getallen geven. <strong>Dubbele gelaagdheid</strong> betekent dat er onder het verhaal een "
                  "tweede betekenis ligt: een tekst over de belegering en verovering van een kasteel kan een "
                  "metafoor zijn voor de manier waarop een meisje het hof wordt gemaakt. Wie alleen de "
                  "bovenlaag leest, mist de helft. De <strong>hoofse liefde</strong> hoort ook bij de "
                  "middeleeuwen, niet bij de romantiek: de ridder vereert zijn dame van op afstand en probeert "
                  "haar met daden te verdienen."),
            ("p", "De <strong>realistische</strong> literatuur confronteerde haar lezers met de "
                  "<strong>wantoestanden in de maatschappij</strong>, zoals kinderarbeid. Dat is precies "
                  "waarom de fiche vraagt of je kan uitleggen in welke mate een tekst relevant is voor jouw "
                  "leefwereld, voor onze samenleving, of voor de samenleving waarin hij ontstond: een verhaal "
                  "over kinderarbeid uit 1880 leest anders als je weet dat het toen echt gebeurde. En daarom is "
                  "het nuttig te weten in welke tijd een tekst ontstond: de stroming verklaart waarom hij "
                  "eruitziet zoals hij eruitziet."),
        ]),
        gesprek("lees een gedicht hardop voor aan iemand en vraag daarna wat hij eruit haalde. Vergelijk dat "
                "met wat jij eruit haalde."),
    ],
    onthoud=[
        "Een sonnet telt veertien regels: een octaaf van acht en een sextet van zes.",
        "Gepaard rijm aabb, gekruist abab, omarmend abba.",
        "Alliteratie herhaalt de beginmedeklinker, assonantie de klinkerklank.",
        "Terzine 3, kwatrijn 4, sextet 6, octaaf 8. Een vers is één regel, een strofe een groepje.",
        "Enjambement hoort bij ritme, niet bij de stijlfiguren.",
        "Vier subgenres van drama: tragedie, komedie, klucht en muziektheater.",
        "Opvoeringsanalyse gaat over alles buiten de tekst: decor, licht, geluid, rekwisieten, kostumering, grime, mimiek.",
        "Drie stromingen: middeleeuwen (getallensymboliek, hoofse liefde), romantiek (gevoel), realisme (wantoestanden).",
    ],
)

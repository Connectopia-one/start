# -*- coding: utf-8 -*-
"""Uitdaging Natuurwetenschappen 🚀 Boost dubbele finaliteit (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die
biologie, chemie en fysica door elkaar halen. Casussen, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen, vijf
klikvragen op twee zelf getekende prenten en een open onderzoeksvraag. Geen
nieuwe leerstof: alles staat in de hoofdstukken van Natuurwetenschappen Boost
dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_natuurwetenschappen.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Natuurwetenschappen"
BESTAND = "boost-df-natuurwetenschappen-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/natuurwetenschappen-boost-df-uitdaging"
CURVE = "opwarmcurve-ijs.svg"
SCHEMA = "feedback-temperatuur.svg"
# klikvakken: zie maak_prenten_boost_df_natuurwetenschappen.py
STUK_B = [17.8, 14.5, 13.5, 69.4]
STUK_C = [31.2, 14.5, 13.5, 69.4]
STUK_D = [44.8, 14.5, 33.8, 69.4]
VAK_2 = [22.4, 23.3, 16.0, 51.2]
VAK_4 = [61.2, 23.3, 16.0, 51.2]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # De opwarmcurve van ijs (prent)
    klik("Bekijk de opwarmcurve. Klik op het stuk waar het ijs smelt.",
         CURVE, [STUK_B],
         "Bij nul graden blijft de temperatuur een tijd gelijk: alle warmte gaat dan naar het smelten. Dat is het vlakke stuk B."),
    klik("Klik in dezelfde curve op het stuk waar er alleen vloeibaar water opwarmt.",
         CURVE, [STUK_C],
         "Na het smelten is alles water. Tussen nul en honderd graden stijgt de temperatuur weer: dat is stuk C."),
    klik("Klik op het stuk waarvoor de brander de meeste warmte moet leveren.",
         CURVE, [STUK_D],
         "De brander geeft elke minuut evenveel warmte. Stuk D duurt het langst (tien minuten): verdampen vraagt veel meer warmte dan opwarmen of smelten."),
    met_prent(CURVE, tabel(
        "Klopt dit over de opwarmcurve?",
        [
            ("In stuk B zijn er tegelijk ijs en water aanwezig.", J),
            ("In stuk D stijgt de inwendige energie van het water niet.", F),
            ("In stuk E is alles waterdamp.", J),
            ("Het smeltpunt van deze stof ligt bij honderd graden.", F),
        ],
        "Tijdens het smelten zijn beide fasen er. Ook als de temperatuur gelijk blijft, krijgen de deeltjes energie: de inwendige energie stijgt. Na het verdampen warmt enkel nog damp op. Het smeltpunt van water is nul graden, honderd graden is het kookpunt.")),
    met_prent(CURVE, inv(
        "De brander levert elke minuut \\(20\\) kilojoule. Hoeveel kilojoule gaat er in totaal naar het smelten van het ijs? Geef enkel het getal.",
        "80",
        "Het smelten duurt van minuut 2 tot minuut 6, dus vier minuten. Vier maal 20 kilojoule is 80 kilojoule.")),

    # Het schema van de temperatuurregeling (prent)
    klik("Bekijk het schema. Klik op het vak met de receptor.",
         SCHEMA, [VAK_2],
         "De receptor vangt de prikkel op. Hier zijn dat de zintuigcellen in je huid die warmte voelen."),
    klik("Klik in hetzelfde schema op het vak met de effector.",
         SCHEMA, [VAK_4],
         "De effector voert het bevel uit. De zweetklieren maken zweet, en dat zweet koelt je af."),
    met_prent(SCHEMA, keuze(
        "Vak 3 is de [[*conductor|receptor|effector]]. De pijl van vak 5 terug naar vak 1 toont dat dit [[*negatieve|positieve]] feedback is.",
        "Zenuwen en hersenen geven het signaal door en verwerken het: dat is de conductor. Omdat de reactie de temperatuur terugbrengt naar de normwaarde, is het negatieve feedback.")),
    met_prent(SCHEMA, mk(
        "Waarom koelt verdampend zweet je af?",
        ["Het water haalt voor het verdampen warmte uit je huid.", "Zweet is altijd kouder dan de lucht rondom je lichaam.", "Het zout in het zweet neemt de warmte op en houdt ze vast.", "De zweetklieren zelf maken je bloed minder warm vanbinnen."],
        0,
        "Verdampen vraagt warmte. Die warmte komt van je huid, dus je lichaam verliest energie en koelt af.")),

    # Casus: de glucosespiegel
    casus(
        "Sam eet om half één een bord pasta. Een uur later is het glucosegehalte in het bloed gestegen. Om vier uur, na de sportles, is het weer gedaald.",
        [
            keuze(
                "Na de maaltijd maakt de alvleesklier meer [[*insuline|glucagon|adrenaline]]. Daardoor slaat de lever glucose op en [[*daalt|stijgt]] het gehalte in het bloed.",
                "Insuline laat het glucosegehalte dalen. De lever slaat de glucose op, zodat het gehalte terug naar de normwaarde gaat."),
            mk("Wat doet het lichaam om vier uur, als het glucosegehalte te laag wordt?",
               ["De lever geeft opgeslagen glucose weer af aan het bloed.", "De alvleesklier maakt nog meer insuline om glucose aan te maken.", "De spieren slaan nog extra glucose op voor de volgende les.", "Het bloed haalt glucose uit de lucht die Sam inademt tijdens het sporten."],
               0,
               "Bij te weinig glucose geeft de lever haar voorraad af. Insuline zou het gehalte net verder doen dalen."),
        ],
    ),

    # Micro-organismen
    sorteer(
        "Is dit een bacterie, een virus of een schimmel?",
        ["Bacterie", "Virus", "Schimmel"],
        [
            ["bakkersgist", "Schimmel"],
            ["een bacteriofaag", "Virus"],
            ["melkzuurbacteriën in yoghurt", "Bacterie"],
            ["de groene laag op oud brood", "Schimmel"],
            ["heeft een eiwitmantel rond zijn erfelijk materiaal", "Virus"],
            ["staafvormige cel die zich door deling vermenigvuldigt", "Bacterie"],
        ],
        "Gist en broodschimmel zijn schimmels. Een faag is een virus dat bacteriën aanvalt. Een virus is een eiwitmantel rond erfelijk materiaal. Bacteriën zijn kleine cellen die zich delen."),
    koppel(
        "Welke bewaringstechniek past bij elke uitleg?",
        [
            ["het water uit het product halen", "drogen"],
            ["het product kort verhitten en daarna afkoelen", "pasteuriseren"],
            ["de groei van micro-organismen vertragen door kou", "koelen"],
            ["het product in een zure vloeistof leggen", "inmaken in azijn"],
        ],
        ["fermenteren", "ontdooien"],
        "Micro-organismen hebben water, een geschikte temperatuur en een niet te zure omgeving nodig. Elke techniek neemt een van die voorwaarden weg."),
    mk("Waarom helpt een antibioticum niet tegen griep?",
       ["Griep komt door een virus, en antibiotica werken enkel op bacteriën.", "Griep komt door een schimmel en daar bestaat enkel een vaccin tegen.", "Een antibioticum werkt pas na een week en dan is de griep al voorbij.", "Het griepvirus maakt zelf een antibioticum aan en wordt zo beschermd."],
       0,
       "Een antibioticum doodt bacteriën of remt hun groei. Een virus is geen cel en heeft daar geen last van."),

    # Voortplanting
    volgorde(
        "Zet deze gebeurtenissen van een menstruatiecyclus in de juiste volgorde, van dag 1.",
        ["de menstruatie begint", "een follikel rijpt in de eierstok", "de eisprong", "het geel lichaam maakt progesteron", "het geel lichaam verdwijnt en een nieuwe cyclus begint"],
        "De cyclus begint met de menstruatie. Dan rijpt een follikel, rond dag 14 is er de eisprong, het geel lichaam houdt het slijmvlies dik en verdwijnt als er geen bevruchting is."),
    tabel(
        "Welk orgaan maakt dit hormoon?",
        [
            ("FSH", "Hypofyse"),
            ("oestrogeen", "Eierstok"),
            ("testosteron", "Teelbal"),
            ("progesteron", "Eierstok"),
        ],
        "De hypofyse maakt FSH en LH. De eierstok maakt oestrogeen en, via het geel lichaam, progesteron. De teelballen maken testosteron.",
        kolommen=["Hypofyse", "Eierstok", "Teelbal"]),
    sleep(
        "Na de eisprong wordt de eicel opgevangen door de [[eileider]]. Komt ze daar een zaadcel tegen, dan kan er een [[bevruchting]] gebeuren. Daarna nestelt het embryo zich in het [[baarmoederslijmvlies]].",
        ["teelbal", "hypofyse"],
        "De eileider vangt de eicel op en daar gebeurt de bevruchting. In de baarmoeder nestelt het embryo zich in het slijmvlies."),

    # Mengsels en stoffen
    sorteer(
        "Is dit een zuivere stof of een mengsel?",
        ["Zuivere stof", "Mengsel"],
        [
            ["gedestilleerd water", "Zuivere stof"],
            ["brons", "Mengsel"],
            ["zuurstofgas", "Zuivere stof"],
            ["zeewater", "Mengsel"],
            ["keukenzout", "Zuivere stof"],
            ["melk", "Mengsel"],
        ],
        "Een zuivere stof bestaat uit één soort deeltjes. Brons is een legering, zeewater bevat zout en water, melk is een mengsel van water, vet en eiwitten."),
    casus(
        "Lotte krijgt een beker troebel water met zand, opgelost zout en een beetje olie die bovenaan drijft. Ze wil uiteindelijk zuiver water overhouden.",
        [
            volgorde(
                "In welke volgorde scheidt Lotte het mengsel het best?",
                ["de olie bovenaan afgieten (decanteren)", "het zand eruit halen met een filter", "het zoute water destilleren"],
                "Eerst haal je weg wat je makkelijk ziet: de olie drijft en kan je afgieten. Het zand houdt een filter tegen. Opgelost zout gaat door de filter, daarom destilleer je op het einde."),
            mk("Op welk verschil in stofeigenschap steunt het destilleren?",
               ["een verschil in kookpunt", "een verschil in deeltjesgrootte", "een verschil in kleur van de stoffen", "een verschil in magnetische eigenschap"],
               0,
               "Water kookt bij honderd graden, zout pas bij veel hogere temperatuur. Het water verdampt en wordt weer vloeibaar in de koeler."),
        ],
    ),

    # Formules, reacties en atomen
    tabel(
        "Is dit een enkelvoudige stof of een samengestelde stof?",
        [
            ("\\(\\mathrm{O_2}\\)", "Enkelvoudig"),
            ("\\(\\mathrm{CO_2}\\)", "Samengesteld"),
            ("\\(\\mathrm{Fe}\\)", "Enkelvoudig"),
            ("\\(\\mathrm{NaCl}\\)", "Samengesteld"),
            ("\\(\\mathrm{N_2}\\)", "Enkelvoudig"),
        ],
        "Een enkelvoudige stof bevat één soort atomen, een samengestelde stof minstens twee soorten.",
        kolommen=["Enkelvoudig", "Samengesteld"]),
    inv("Hoeveel atomen bevat één molecule \\(\\mathrm{C_6H_{12}O_6}\\)? Geef enkel het getal.",
        "24",
        "Zes koolstofatomen, twaalf waterstofatomen en zes zuurstofatomen: samen 24 atomen."),
    inv("Bij een verbranding reageert \\(12\\) gram koolstof met \\(32\\) gram zuurstofgas. Hoeveel gram koolstofdioxide ontstaat er? Geef enkel het getal.",
        "44",
        "Volgens de wet van behoud van massa is de massa van de reactieproducten gelijk aan die van de uitgangsstoffen: 12 plus 32 is 44 gram."),
    keuze(
        "Een kaars die brandt, geeft warmte af: dat is een [[*exo-energetische|endo-energetische]] reactie. Een reactie waarbij één stof uiteenvalt in meerdere stoffen heet een [[*analyse|synthese]].",
        "Exo-energetisch betekent dat de reactie energie afgeeft aan de omgeving. Bij een analyse valt een stof uiteen, bij een synthese ontstaat er een nieuwe stof uit meerdere stoffen."),
    tabel(
        "Een atoom natrium heeft atoomnummer \\(11\\) en massagetal \\(23\\). Vul de aantallen in.",
        [
            ("protonen", "11"),
            ("elektronen in het neutrale atoom", "11"),
            ("neutronen", "12"),
            ("elektronen op de buitenste schil", "1"),
        ],
        "Het atoomnummer geeft het aantal protonen, en in een neutraal atoom evenveel elektronen. Neutronen: 23 min 11 is 12. Natrium staat in groep 1, dus één elektron op de buitenste schil.",
        kolommen=["1", "11", "12", "23"]),
    mk("Waarom vormt natrium gemakkelijk een ion met lading plus één?",
       ["Het geeft zijn ene buitenste elektron af en houdt een volle schil.", "Het neemt één proton op uit de omgeving en wordt daardoor positief.", "Het verliest een neutron, waardoor de kern positiever geladen wordt.", "Het neemt zeven elektronen op tot de buitenste schil helemaal vol is."],
       0,
       "Eén elektron afgeven vraagt veel minder dan er zeven opnemen. Met één elektron minder dan protonen is het ion positief."),
    tabel(
        "Klopt dit over atomen en het periodiek systeem?",
        [
            ("Isotopen van een element hebben een verschillend aantal neutronen.", J),
            ("Edelgassen staan in groep 18 en reageren bijna niet.", J),
            ("Elementen in dezelfde periode hebben evenveel valentie-elektronen.", F),
            ("De massa van een atoom zit bijna helemaal in de elektronen.", F),
        ],
        "Isotopen verschillen enkel in neutronen. Edelgassen hebben een volle buitenste schil. Evenveel valentie-elektronen heb je in dezelfde groep, niet in dezelfde periode. Protonen en neutronen in de kern zijn veel zwaarder dan elektronen."),

    # Energie, vermogen en rendement
    casus(
        "Een elektrische step heeft een motor van \\(250\\) watt. Van elke \\(100\\) joule elektrische energie wordt \\(75\\) joule bewegingsenergie, de rest wordt warmte.",
        [
            inv("Wat is het rendement van de motor, in procent? Geef enkel het getal.",
                "75",
                "Rendement is nuttige energie gedeeld door opgenomen energie: 75 gedeeld door 100 is 0,75 of 75 procent."),
            inv("Hoeveel joule elektrische energie neemt de motor op als hij \\(10\\) seconden op vol vermogen draait? Geef enkel het getal.",
                ["2500", "2 500", "2.500"],
                "Energie is vermogen maal tijd: 250 watt maal 10 seconden is 2500 joule."),
        ],
    ),
    koppel(
        "Welke energieomzetting gebeurt er?",
        [
            ["een zonnepaneel", "stralingsenergie wordt elektrische energie"],
            ["een broodrooster", "elektrische energie wordt warmte"],
            ["een appel die van de boom valt", "potentiële energie wordt kinetische energie"],
            ["een batterij in een zaklamp", "chemische energie wordt elektrische energie"],
        ],
        ["kinetische energie wordt chemische energie"],
        "Elk toestel zet één energievorm om in een andere. De totale hoeveelheid energie blijft gelijk."),

    # Kracht en druk
    tabel(
        "Twee krachten werken op hetzelfde punt. Hoe groot is de resulterende kracht, in newton?",
        [
            ("\\(30\\) N naar rechts en \\(20\\) N naar rechts", "50"),
            ("\\(30\\) N naar rechts en \\(20\\) N naar links", "10"),
            ("\\(25\\) N naar boven en \\(25\\) N naar beneden", "0"),
        ],
        "Krachten met dezelfde richting en zin tel je op. Met tegengestelde zin trek je ze van elkaar af. Even grote tegengestelde krachten heffen elkaar op.",
        kolommen=["0", "10", "50"]),
    inv("Een kist van \\(800\\) newton staat op een oppervlak van \\(0{,}4\\) vierkante meter. Hoe groot is de druk op de vloer, in pascal? Geef enkel het getal.",
        ["2000", "2 000", "2.000"],
        "Druk is kracht gedeeld door oppervlakte: 800 gedeeld door 0,4 is 2000 pascal."),

    # Elektriciteit
    casus(
        "Een lamp is aangesloten op een spanning van \\(12\\) volt. Er loopt een stroom van \\(0{,}5\\) ampère door.",
        [
            inv("Hoe groot is de weerstand van de lamp, in ohm? Geef enkel het getal.",
                "24",
                "Volgens de wet van Ohm is de weerstand de spanning gedeeld door de stroomsterkte: 12 gedeeld door 0,5 is 24 ohm."),
            inv("Hoe groot is het vermogen van de lamp, in watt? Geef enkel het getal.",
                "6",
                "Vermogen is spanning maal stroomsterkte: 12 maal 0,5 is 6 watt."),
        ],
    ),
    tabel(
        "Is dit veilig of onveilig in de omgang met elektriciteit?",
        [
            ("een kapotte kabel nog even gebruiken met wat plakband errond", "Onveilig"),
            ("de stekker uittrekken voor je een toestel schoonmaakt", "Veilig"),
            ("vijf toestellen met een groot vermogen op één verdeeldoos", "Onveilig"),
            ("een toestel met een aarding in een stopcontact met aarding", "Veilig"),
        ],
        "Een beschadigde kabel kan elektrocutie geven. Te veel toestellen op één verdeeldoos geeft overbelasting. Een aarding leidt lekstroom veilig weg.",
        kolommen=["Veilig", "Onveilig"]),

    # Veilig werken en levensreddend handelen
    volgorde(
        "Iemand zakt in elkaar, reageert niet en ademt niet normaal. Zet de eerste stappen in de juiste volgorde.",
        ["kijk of de omgeving veilig is", "spreek het slachtoffer aan en schud zacht", "bel 112", "start met borstcompressies"],
        "Eerst je eigen veiligheid. Dan kijk je of het slachtoffer reageert. Ademt het niet normaal, dan bel je 112 en begin je meteen te reanimeren."),

    # Grootheden en onderzoek
    tabel(
        "Zet om naar de basiseenheid.",
        [
            ("\\(3\\) kilometer in meter", "3000"),
            ("\\(250\\) milligram in gram", "0,25"),
            ("\\(2\\) megajoule in joule", "2 000 000"),
        ],
        "Kilo is duizend, milli is een duizendste en mega is een miljoen.",
        kolommen=["0,25", "3000", "2 000 000"]),
    mk("Hoe schrijf je \\(0{,}00042\\) meter in de wetenschappelijke notatie?",
       ["\\(4{,}2 \\cdot 10^{-4}\\) m", "\\(4{,}2 \\cdot 10^{4}\\) m", "\\(42 \\cdot 10^{-5}\\) m", "\\(0{,}42 \\cdot 10^{-3}\\) m"],
       0,
       "In de wetenschappelijke notatie staat er een getal tussen 1 en 10 vooraan. De komma schuift vier plaatsen naar rechts, dus de exponent is min vier."),
    tabel(
        "Is dit verband recht evenredig of omgekeerd evenredig?",
        [
            ("de prijs van appels en het aantal kilogram dat je koopt", "Recht evenredig"),
            ("het aantal arbeiders en de tijd om een muur te bouwen", "Omgekeerd evenredig"),
            ("de afstand die je fietst bij een constante snelheid en de tijd", "Recht evenredig"),
            ("de snelheid en de tijd om een vaste afstand af te leggen", "Omgekeerd evenredig"),
        ],
        "Bij recht evenredig blijft het quotiënt gelijk: dubbel zoveel geeft dubbel zoveel. Bij omgekeerd evenredig blijft het product gelijk: dubbel zoveel geeft de helft.",
        kolommen=["Recht evenredig", "Omgekeerd evenredig"]),
    open_("Je wil onderzoeken of de dikte van een laag isolatie invloed heeft op hoe snel warm water in een beker afkoelt. Schrijf een hypothese en zeg welke grootheid je verandert, welke je meet en welke je gelijk houdt.",
          "Hypothese: hoe dikker de isolatie, hoe trager het water afkoelt. Ik verander de dikte van de isolatie. Ik meet de temperatuur van het water na tien minuten. Ik houd de hoeveelheid water, de begintemperatuur, de soort beker en de kamertemperatuur gelijk.",
          "Een goede hypothese kan je testen. Verander maar één grootheid tegelijk, anders weet je niet wat het verschil veroorzaakt."),
]

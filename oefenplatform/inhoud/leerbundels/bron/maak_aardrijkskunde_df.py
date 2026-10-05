# -*- coding: utf-8 -*-
"""De leerbundels van aardrijkskunde voor 🚀 Boost dubbele finaliteit.

    python3 bron/maak_aardrijkskunde_df.py

Tien bundels, één per thema van `inhoud/boost-dubbele-finaliteit/aardrijkskunde.json`.

De rubrieken van deze fiche zijn dezelfde als bij doorstroom en de gewichten
ook, dus de bundels van doorstroom liggen hier aan de basis. Wat deze fiche
niet vraagt, gaat eruit: de Human Development Index, het vruchtbaarheidscijfer,
het migratiesaldo, het demografisch transitiemodel met zijn fasen, de
hiërarchie van steden, inbreiding, stadslandbouw, protectionisme en vrijhandel,
outsourcing, reconversie, bodemerosie en bodemdegradatie, de stralingsbalans,
het albedo en de verspreiding van tropische ziektes.

In de plaats komt wat ze wél zet: de ontwikkelingsgraad zonder index, de
bevolkingsdichtheid uit bronnen lezen, de scholingsgraad als sociaaleconomische
factor, en de koolstofcyclus tussen de vier sferen. Onderaan dit bestand loopt
een controle over alle bundels die daarop toekijkt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag.
"""
import copy

import bundel
import maak_aardrijkskunde_boost as doorstroom

tabel = bundel.tabel

VAK = "Aardrijkskunde"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIEUW = "-boost-dubbele-finaliteit"

VERBODEN = [
    "human development",
    "hdi",
    "vruchtbaarheidscijfer",
    "migratiesaldo",
    "demografische transitie",
    "transitiemodel",
    "bevolkingsstructuur",
    "hiërarchie",
    "inbreiding",
    "stadslandbouw",
    "outsourcing",
    "uitbesteding",
    "delokalisatie",
    "protectionisme",
    "vrijhandel",
    "reconversie",
    "bodemerosie",
    "bodemdegradatie",
    "stralingsbalans",
    "albedo",
    "tropische ziekte",
    "de vakfiche",
    "de fiche",
    "deze fiche",
    "de leerstof",
]

# De tien thema's, in de volgorde van de fiche.
ORDE = [
    "waar-ligt-het-en-hoe-weet-je-dat",
    "waar-wonen-de-mensen",
    "hoe-een-bevolking-verandert",
    "stad-en-platteland",
    "grondstoffen-energie-en-industrie",
    "landbouw-handel-en-toerisme",
    "mondialisering",
    "duurzaam-omgaan-met-de-ruimte",
    "het-versterkte-broeikaseffect",
    "een-geografisch-onderzoek-voeren",
]


def tekst_van(blok) -> str:
    return " ".join(str(d) for d in blok[1:])


# ─────────────────────────────────────────────────────────────
# De nieuwe secties.
# ─────────────────────────────────────────────────────────────
ONTWIKKELINGSGRAAD = dict(
    kop="De ontwikkelingsgraad",
    blokken=[
        ("p", "De <strong>ontwikkelingsgraad</strong> vat samen hoe goed het met de mensen in "
              "een land gaat: hoe lang ze gemiddeld leven, hoeveel jaar ze naar school gaan, en "
              "hoeveel welvaart er is. Het is dus meer dan geld alleen: een land kan rijk zijn "
              "aan olie en toch weinig scholen en ziekenhuizen hebben."),
        ("p", "Waarom de ontwikkelingsgraad tussen landen verschilt, heeft nooit één oorzaak. "
              "Kolonisatie, oorlog, bestuur, schulden, grondstoffen en onderwijsbeleid grijpen in "
              "elkaar. Grondstoffen maken een land ook niet vanzelf welvarend: wat het met zijn "
              "inkomsten doet, telt evenveel als wat het in de grond heeft. Japan en Zuid-Korea "
              "hebben weinig grondstoffen en toch veel welvaart."),
        ("kader", "Tussen de bevolkingsdichtheid en de ontwikkelingsgraad bestaat géén vast "
                  "verband. Nederland is dichtbevolkt en welvarend, Bangladesh is dichtbevolkt "
                  "en arm, Canada is dunbevolkt en welvarend. De twee meten verschillende dingen."),
        ("p", "Een gemiddelde over een heel land verbergt bovendien de verschillen binnen dat "
              "land: in veel landen gaat het in de hoofdstad veel beter dan op het platteland. "
              "Een lage ontwikkelingsgraad betekent dus niet dat niemand er rijk is; de "
              "ongelijkheid is er vaak juist groot. Onthoud dat de verbetering van de "
              "ontwikkelingsgraad een belangrijke stap is naar een duurzame wereld."),
    ],
)

DICHTHEID_LEZEN = dict(
    kop="De dichtheid uit bronnen lezen",
    blokken=[
        ("p", "Je leest de bevolkingsdichtheid af van <strong>thematische kaarten</strong> en "
              "<strong>tabellen</strong>. Op een kaart koppelt de legende elke kleur aan een "
              "aantal inwoners per vierkante kilometer; uit een tabel met inwoners en oppervlakte "
              "reken je ze zelf uit. Het totale aantal inwoners van een land staat niet op zo'n "
              "kaart, en hoeveel inwoners er jaarlijks bijkomen ook niet: daarvoor heb je twee "
              "tijdstippen nodig, of de kengetallen van de bevolking."),
        ("p", "Zet je de dichtheid in <strong>klassen</strong> op een kaart in plaats van bij elk "
              "gebied het exacte getal te schrijven, dan zie je het <strong>patroon</strong> in "
              "één oogopslag. Nauwkeuriger worden de cijfers er niet van. Pas op: wie de grenzen "
              "tussen de klassen verschuift, verschuift ook de kleurvlekken. Twee kaarten van "
              "dezelfde dichtheid kunnen er dus heel anders uitzien, en daarom lees je altijd "
              "eerst de legende."),
        ("weetje", "Een <strong>satellietbeeld van de aarde bij nacht</strong> is ook een bron "
                   "over bevolking. Licht komt van steden, wegen en havens, dus de lichtvlekken "
                   "verraden waar mensen samenwonen. Hoe vruchtbaar of hoe nat een streek is, zie "
                   "je er niet aan."),
        ("p", "Vergelijk je twee kaarten van hetzelfde gebied, dan let je eerst op het "
              "<strong>jaartal</strong> en op de <strong>klassen van de legende</strong>. Zonder "
              "hetzelfde jaartal en dezelfde klassen vergelijk je appels met peren. De gekozen "
              "kleur en het formaat van de afdruk veranderen de cijfers niet."),
    ],
)

DICHTHEID_VERANDERT = dict(
    kop="Wat de dichtheid doet veranderen",
    blokken=[
        ("p", "Een bevolkingsdichtheid staat niet vast. Mensen <strong>wegtrekken</strong> doen "
              "vooral drie omstandigheden: een <strong>oorlog</strong> die jaren aansleept, "
              "<strong>droogte</strong> waardoor de oogst mislukt, en <strong>armoede</strong> "
              "zonder uitzicht op werk. Dat zijn pushfactoren: ze duwen mensen weg. Door de "
              "klimaatverandering komt er een vierde bij: een streek waar het drinkwater opraakt, "
              "loopt leeg, want zonder water lukken landbouw en wonen niet meer."),
        ("kader", "Armoede duwt mensen niet altijd weg. Verhuizen kost geld, papieren en "
                  "contacten, dus wie het armst is, blijft vaak net achter, terwijl mensen met "
                  "iets meer middelen vertrekken."),
        ("p", "Een streek met <strong>vruchtbare</strong> grond blijft meestal dichtbevolkt, ook "
              "zonder industrie: waar de landbouw veel mensen kan voeden, blijven er veel mensen "
              "wonen. De Nijlvallei en de delta van de Ganges zijn daar voorbeelden van. "
              "Omgekeerd kan een streek dunbevolkt blijven terwijl er veel grondstoffen in de "
              "grond zitten: moderne ontginning vraagt machines, niet veel handen, en dus liggen "
              "er in Noord-Australië en Siberië grote mijnen in een vrijwel leeg landschap."),
        ("p", "Ook een <strong>politieke beslissing</strong> verandert een dichtheid. Wie een "
              "haven, een luchthaven of een hoofdstad op een bepaalde plaats zet, trekt daar "
              "mensen naartoe: Brasilia werd zo in het binnenland uit het niets gebouwd. En een "
              "oorlog kan de dichtheid van een streek in enkele jaren sterk doen zakken, want "
              "mensen vluchten weg en komen niet altijd terug."),
    ],
)

VERLOOP_LEZEN = dict(
    kop="Het verloop van de cijfers lezen",
    blokken=[
        ("p", "Je legt het verloop van het geboorte- en het sterftecijfer van een land uit met "
              "<strong>grafieken</strong> en <strong>tabellen</strong>. Een lijngrafiek zet de "
              "twee cijfers naast elkaar en laat zien waar het gat tussen beide wijder of smaller "
              "wordt. Dat gat is precies de natuurlijke aangroei."),
        ("p", "Drie beelden komen vaak terug. Liggen <strong>beide cijfers hoog</strong>, dan "
              "blijft de bevolking ongeveer gelijk: er worden veel kinderen geboren, maar er "
              "sterven ook veel mensen. <strong>Daalt het sterftecijfer snel terwijl het "
              "geboortecijfer hoog blijft</strong>, dan groeit de bevolking snel; dat gebeurt als "
              "voeding, drinkwater en gezondheidszorg beter worden, want gewoonten rond kinderen "
              "krijgen veranderen veel trager. Liggen <strong>beide cijfers laag</strong> en leven "
              "mensen lang, dan groeit de bevolking weer traag, maar met veel meer ouderen."),
        ("kader", "Een geboortecijfer van 34 ‰ naast een sterftecijfer van 9 ‰ geeft een "
                  "natuurlijke aangroei van 25 per duizend, dus bijna drie procent per jaar. Zo'n "
                  "land heeft een brede basis in zijn leeftijdshistogram."),
        ("p", "Twee landen waarvan de bevolking even traag groeit, hebben daarom nog niet dezelfde "
              "<strong>leeftijdsopbouw</strong>. Traag groeien kan met veel kinderen en veel "
              "sterfgevallen, of met weinig kinderen en veel ouderen. In het histogram zien die "
              "twee er helemaal anders uit."),
    ],
)


# ─────────────────────────────────────────────────────────────
# De ingrepen, bundel per bundel.
#   onder          : de ondertitel vervangen
#   kop            : een sectiekop hernoemen
#   schrap-sectie  : een hele sectie weg
#   sectie-achteraan: een nieuwe sectie onderaan
#   schrap-blok    : één blok weg, gezocht op een stukje tekst
#   vervang-blok   : één blok vervangen door een of meer nieuwe
#   onthoud        : een regel uit het onthoudlijstje vervangen of (None) schrappen
# Elk haakje moet precies één keer raken, anders stopt het script.
# ─────────────────────────────────────────────────────────────
INGREPEN = [
    # ── Waar wonen de mensen? Geen index voor ontwikkeling.
    ("waar-wonen-de-mensen", "onder", None,
     "Bevolkingsdichtheid, de factoren die ze sturen, en de ontwikkelingsgraad van een land."),
    ("waar-wonen-de-mensen", "schrap-sectie", "Ontwikkelingsgraad en de HDI", None),
    ("waar-wonen-de-mensen", "schrap-sectie", "De HDI lezen en nuanceren", None),
    ("waar-wonen-de-mensen", "sectie-achteraan", None, ONTWIKKELINGSGRAAD),
    ("waar-wonen-de-mensen", "sectie-achteraan", None, DICHTHEID_LEZEN),
    ("waar-wonen-de-mensen", "sectie-achteraan", None, DICHTHEID_VERANDERT),
    ("waar-wonen-de-mensen", "onthoud", "De HDI van de Verenigde Naties combineert",
     "De ontwikkelingsgraad vat levensverwachting, onderwijs en welvaart samen."),
    ("waar-wonen-de-mensen", "onthoud", "De gewone HDI werkt met gemiddelden",
     "Een gemiddelde over een heel land verbergt de verschillen binnen dat land."),
    ("waar-wonen-de-mensen", "onthoud", "Tussen dichtheid en HDI bestaat geen vast verband.",
     "Tussen dichtheid en ontwikkelingsgraad bestaat geen vast verband."),

    # ── Hoe een bevolking verandert. Vijf kengetallen, geen transitiemodel.
    ("hoe-een-bevolking-verandert", "onder", None,
     "De kengetallen, het leeftijdshistogram, het verloop van de cijfers, en waarom mensen migreren."),
    ("hoe-een-bevolking-verandert", "vervang-blok", "Het <strong>migratiesaldo</strong>", [
        ("p", "<strong>Emigratie</strong> is vertrekken, <strong>immigratie</strong> is "
              "aankomen; dezelfde persoon is emigrant in het land dat hij verlaat en immigrant in "
              "het land waar hij aankomt. Wie uit een land emigreert, immigreert dus in een "
              "ander. Voor de wereld samen heffen aankomst en vertrek elkaar op; alleen per land "
              "blijft er een verschil over."),
    ]),
    ("hoe-een-bevolking-verandert", "schrap-blok", "<strong>vruchtbaarheidscijfer</strong>", None),
    ("hoe-een-bevolking-verandert", "vervang-blok", "De <strong>totale groei</strong>", [
        ("kader", "De <strong>totale groei</strong> van een land is de natuurlijke aangroei plus "
                  "wie erbij komt en min wie vertrekt. Daarom kan een land met een negatieve "
                  "natuurlijke aangroei toch groeien: in verschillende West-Europese landen komt "
                  "de groei vandaag bijna helemaal van immigratie."),
    ]),
    ("hoe-een-bevolking-verandert", "schrap-sectie", "De demografische transitie", None),
    ("hoe-een-bevolking-verandert", "vervang-blok", "De <strong>demografische processen</strong>", [
        ("p", "De <strong>demografische processen</strong> zijn de bevolkingsevolutie, de "
              "vergrijzing, de immigratie en de emigratie. <strong>Vergrijzing</strong> betekent "
              "dat het <em>aandeel</em> ouderen toeneemt, niet dat het aantal inwoners daalt. Ze "
              "komt van een dalend geboortecijfer en een stijgende levensverwachting samen, en "
              "zet pensioenen, zorg en arbeidsmarkt onder druk terwijl scholen juist leeg komen "
              "te staan."),
    ]),
    ("hoe-een-bevolking-verandert", "vervang-blok", "het geboortebeleid, de welvaart en", [
        ("p", "De <strong>beïnvloedende factoren</strong> zijn het klimaat en de "
              "klimaatverandering, het reliëf, de bodemkwaliteit, de politieke situatie, de "
              "oorlogssituatie, het geboortebeleid, de welvaart en het welzijn, en armoede. Een "
              "geboortecijfer blijft laag wanneer vrouwen lang naar school gaan en werken, "
              "wanneer beleid grote gezinnen ontmoedigt, en wanneer huisvesting en kinderopvang "
              "duur zijn. Hoge kindersterfte en een landbouweconomie duwen het juist omhoog: dan "
              "zijn kinderen handen op het veld en een zekerheid voor later."),
    ]),
    ("hoe-een-bevolking-verandert", "vervang-blok", "Een land met een negatief migratiesaldo", [
        ("p", "Vertrekken er veel jonge, opgeleide mensen uit een land en komen er weinig bij, "
              "dan veroudert dat land én verliest het kennis. De achterblijvende bevolking wordt "
              "gemiddeld ouder, en het land mist net de mensen die het nodig heeft."),
    ]),
    ("hoe-een-bevolking-verandert", "sectie-achteraan", None, VERLOOP_LEZEN),
    ("hoe-een-bevolking-verandert", "onthoud", "migratiesaldo = immigratie min emigratie",
     "Natuurlijke aangroei = geboortecijfer min sterftecijfer."),
    ("hoe-een-bevolking-verandert", "onthoud", "Totale groei = natuurlijke aangroei",
     "Totale groei = natuurlijke aangroei plus wie erbij komt, min wie vertrekt."),
    ("hoe-een-bevolking-verandert", "onthoud", "Vruchtbaarheidscijfer =",
     "De vijf kengetallen: geboortecijfer, sterftecijfer, natuurlijke aangroei, immigratie en emigratie."),
    ("hoe-een-bevolking-verandert", "onthoud", "In fase 2 van de demografische transitie",
     "Daalt de sterfte terwijl de geboorten hoog blijven, dan groeit een bevolking het snelst."),

    # ── Stad en platteland. Geen hiërarchie, geen inbreiding, geen stadslandbouw.
    ("stad-en-platteland", "onder", None,
     "Waarom mensen wonen waar ze wonen, wat er in de stad verandert, en hoe verstedelijking het landschap verandert."),
    ("stad-en-platteland", "schrap-sectie", "De hiërarchie van steden", None),
    ("stad-en-platteland", "vervang-blok", "de oorlogssituatie, de welvaart en het welzijn, en", [
        ("p", "De <strong>beïnvloedende factoren</strong> zijn het klimaat en de "
              "klimaatverandering, het reliëf, de bodemkwaliteit, de politieke situatie, de "
              "oorlogssituatie, de welvaart en het welzijn, en armoede. Armoede werkt trouwens in "
              "twee richtingen: in de stad is er meer kans op werk, maar het wonen is er duurder, "
              "en daarom komen armere gezinnen vaak in de goedkoopste, oudste wijken van de stad "
              "terecht."),
    ]),
    ("stad-en-platteland", "kop", "Vijf veranderingen in het landschap",
     "Vier veranderingen in het landschap"),
    ("stad-en-platteland", "vervang-blok", "De fiche noemt vijf landschapsveranderingen.", [
        ("p", "Er zijn vier landschapsveranderingen. De eerste is de <strong>verstedelijking van "
              "het platteland</strong>: nieuwe verkavelingen rond de dorpskern, winkelcentra en "
              "bedrijven langs de invalswegen, bebouwing op wat vroeger akkerland was. "
              "Verstedelijking is dus meer dan steden die inwoners krijgen. Een dorp dat er drie "
              "verkavelingen bij krijgt zonder één nieuwe winkel, wordt een woondorp waar men "
              "voor alles wegrijdt."),
    ]),
    ("stad-en-platteland", "vervang-blok", "De derde is <strong>inbreiding", [
        ("p", "De derde is de <strong>groei van de steden</strong>. Een stad die groeit, zet zich "
              "uit aan de rand, met nieuwe wijken op wat akkerland was, meer verharding en meer "
              "verkeer naar het centrum. Bouwen op open plekken en oude bedrijfsterreinen "
              "<em>binnen</em> de stad spaart die open ruimte buiten de stad en houdt de "
              "voorzieningen dicht bij de mensen, wat autokilometers scheelt. Open ruimte is in "
              "Vlaanderen schaars geworden, en daarom kiezen veel steden vandaag voor die weg."),
    ]),
    ("stad-en-platteland", "schrap-blok", "De vijfde is <strong>stadslandbouw", None),
    ("stad-en-platteland", "vervang-blok", "hiërarchie van de stad verandert zo'n plein niets", [
        ("p", "Een gemeente die een betonnen plein openbreekt en er bomen plant, pakt precies die "
              "twee problemen aan: meer schaduw en verdamping tegen de hitte, en water dat weer "
              "in de bodem trekt. Aan de sociale segregatie of aan de ontvolking van het "
              "platteland eromheen verandert zo'n plein niets."),
    ]),
    ("stad-en-platteland", "onthoud", "De stedenhiërarchie hangt af",
     "Verstedelijking van het platteland is meer dan steden die inwoners krijgen."),
    ("stad-en-platteland", "onthoud", "De criteria voor die hiërarchie", None),
    ("stad-en-platteland", "onthoud", "Inbreiding is bouwen binnen de bestaande stad",
     "Bouwen binnen de bestaande stad spaart de open ruimte aan de rand."),
    ("stad-en-platteland", "onthoud", "veranderende mobiliteit en stadslandbouw",
     "De vier landschapsveranderingen: verstedelijking en ontvolking van het platteland, groei van de steden, veranderende mobiliteit."),
]

INGREPEN += [
    # ── Grondstoffen, energie en industrie. Scholingsgraad in plaats van een index.
    ("grondstoffen-energie-en-industrie", "vervang-blok", "De fiche deelt de factoren in drie groepen in.", [
        ("p", "De factoren die het industriële proces <strong>beïnvloeden</strong>, vallen in drie "
              "groepen uiteen. De <strong>geopolitieke</strong> "
              "factoren zijn de staatsvorm, de stabiliteit en de samenwerkingsverbanden. Die "
              "bepalen of een bedrijf er durft te investeren en of het vlot kan uitvoeren: een "
              "land dat lid is van een groot handelsblok voert makkelijker uit naar de andere "
              "leden, want invoerrechten en veel controles vallen weg. Raakt een land in oorlog, "
              "dan valt ook de ontginning terug, want investeerders en werknemers vertrekken en "
              "de havens en pijpleidingen werken niet meer."),
    ]),
    ("grondstoffen-energie-en-industrie", "vervang-blok", "factoren zijn de Human Development Index, de", [
        ("p", "De <strong>fysische</strong> factoren zijn het klimaat en de klimaatverandering, "
              "het reliëf en de grondstoffen. De <strong>sociaaleconomische</strong> factoren "
              "zijn de <strong>scholingsgraad</strong>, de verloning, vraag en aanbod, en de "
              "afzetmarkt. De scholingsgraad is het opleidingsniveau van de mensen in een streek: "
              "een bedrijf dat ingenieurs of technici nodig heeft, zoekt een plaats waar die te "
              "vinden zijn."),
    ]),
    ("grondstoffen-energie-en-industrie", "vervang-blok", "<th style=\"border:1px solid", [
        ("p", tabel(["geopolitiek", "fysisch", "sociaaleconomisch"],
                    [["staatsvorm", "klimaat en klimaatverandering", "scholingsgraad"],
                     ["stabiliteit", "reliëf", "verloning"],
                     ["samenwerkingsverbanden", "grondstoffen", "vraag en aanbod, afzetmarkt"]])),
    ]),
    ("grondstoffen-energie-en-industrie", "vervang-blok", "Bedrijven verplaatsen productie naar het buitenland", [
        ("p", "Bedrijven verplaatsen productie naar het buitenland omdat lonen, belastingen en "
              "regels daar vaak lager liggen. Lagere lonen zijn wel niet de <em>enige</em> reden: "
              "ook de nabijheid van de afzetmarkt, de milieuregels en de beschikbaarheid van "
              "geschoold personeel wegen mee. En de prijs per stuk zakt als je op één plaats veel "
              "tegelijk maakt, want de kosten van een fabriek en van machines worden dan over "
              "meer stuks verdeeld."),
    ]),
    ("grondstoffen-energie-en-industrie", "vervang-blok", "<strong>Reconversie</strong> is de derde stap", [
        ("p", "Verdwijnt de industrie uit een streek, dan laat ze een gat achter dat je in de "
              "ruimte ziet: leegstaande hallen, verlaten spoorlijnen en terreinen waar de bodem "
              "vervuild is. Thor Park in Genk, op de oude mijnsite van Waterschei, laat zien hoe "
              "zo'n terrein daarna een heel andere bestemming kan krijgen, met een "
              "wetenschapspark en een campus."),
    ]),
    ("grondstoffen-energie-en-industrie", "onthoud", "Outsourcing of uitbesteding",
     "De scholingsgraad is het opleidingsniveau van de mensen in een streek."),
    ("grondstoffen-energie-en-industrie", "onthoud", "Na de-industrialisatie krijgt het oude terrein",
     "Bij de-industrialisatie verdwijnt de fabrieksactiviteit uit een streek, met het werk erbij."),

    # ── Landbouw, handel en toerisme. Ontbossing en schaalvergroting, geen erosie.
    ("landbouw-handel-en-toerisme", "vervang-blok", "Bij de landbouw noemt de fiche bij de fysische factoren", [
        ("p", "Bij de factoren die het landbouwproces <strong>beïnvloeden</strong>, komen bij de "
              "fysische factoren uitdrukkelijk ook de "
              "<strong>bodemkwaliteit en de ondergrond</strong>, naast klimaat en reliëf. Of een "
              "gewas ergens kan groeien, hangt mee af van de ondergrond onder de bouwvoor: op een "
              "ondoorlaatbare laag blijft het water staan, op zand zakt het meteen weg. De "
              "geopolitieke en sociaaleconomische factoren zijn dezelfde als bij de industrie. "
              "Politieke stabiliteit telt zwaar: oorlog legt velden braak, vernielt opslag en "
              "verstoort de handel, en daarom leidt een conflict in een graanland tot hogere "
              "voedselprijzen ver daarbuiten."),
    ]),
    ("landbouw-handel-en-toerisme", "vervang-blok", "<strong>Bodemerosie</strong> treedt sneller op", [
        ("p", "Twee gevolgen van de landbouw voor de ruimte staan op je lijst. "
              "<strong>Ontbossing</strong> is het kappen van bos om er landbouwgrond of weiland "
              "van te maken. In een tropisch bos zit het meeste voedsel in de bomen zelf, niet in "
              "de grond: is het bos weg, dan is de vruchtbare laag na een paar oogsten uitgeput "
              "en trekt men verder. <strong>Schaalvergroting</strong> is het samenvoegen van "
              "percelen tot grote velden, met minder bedrijven en grotere machines; hagen, "
              "houtkanten en veldwegen verdwijnen daarbij."),
    ]),
    ("landbouw-handel-en-toerisme", "vervang-blok", "factor is de Human Development Index", [
        ("p", "De <strong>geopolitieke</strong> factoren zijn de stabiliteit, de staatsvorm en de "
              "samenwerkingsverbanden: die bepalen of mensen er veilig en zonder visum geraken. "
              "Politieke onrust doet het aantal toeristen meestal binnen de week dalen, en het "
              "herstel duurt jaren. De <strong>sociaaleconomische</strong> factoren zijn de "
              "<strong>scholingsgraad</strong> en de <strong>welvaart</strong>: gidsen, "
              "hotelpersoneel en reisleiders met talenkennis, en wegen, water en zorg maken een "
              "bestemming bruikbaar."),
    ]),
    ("landbouw-handel-en-toerisme", "onthoud", "Bodemerosie spoelt de vruchtbare bovenlaag weg",
     "Ontbossing en schaalvergroting zijn de twee gevolgen van de landbouw voor de ruimte."),

    # ── Mondialisering. Geen protectionisme, geen vrijhandel, geen outsourcing.
    ("mondialisering", "vervang-blok", "De fiche noemt zes samenwerkingsverbanden.", [
        ("p", "Er zijn zes samenwerkingsverbanden om te kennen. De <strong>Europese Unie</strong> "
              "is een samenwerkingsverband van Europese landen met een gemeenschappelijke markt, "
              "gezamenlijke regels en voor een deel een gezamenlijke munt; over het leger van "
              "haar lidstaten gaat ze niet. De <strong>Verenigde Naties</strong> werden na de "
              "Tweede Wereldoorlog opgericht om oorlog te voorkomen en verenigen bijna alle "
              "landen ter wereld; daarnaast werken ze rond ontwikkeling, gezondheid, "
              "vluchtelingen en klimaat."),
    ]),
    ("mondialisering", "vervang-blok", "<strong>Vrijhandel</strong> haalt drempels weg", [
        ("p", "Mondialisering kan ook <strong>spanningen tussen landen</strong> vergroten. Wie "
              "veel uitvoert, heeft zijn klanten nodig; wie grondstoffen levert, heeft de "
              "afnemer nodig. Daardoor wordt handel soms een politiek drukmiddel: een land dat "
              "gas, graan of zeldzame metalen levert, kan die kraan dichtdraaien om iets gedaan "
              "te krijgen. Zulke afhankelijkheid werkt in twee richtingen, en net daarom is ze "
              "een spanning en geen eenvoudig machtsmiddel."),
    ]),
    ("mondialisering", "vervang-blok", "<strong>Outsourcing</strong> is werk uitbesteden", [
        ("p", "<strong>Migratiebewegingen</strong> en <strong>ontvolking</strong> horen er ook "
              "bij. Trekken de jongeren van een streek naar de steden en naar het buitenland, dan "
              "loopt die streek leeg: in delen van Zuid-Europa staan hele dorpen leeg. Wie "
              "migreert, stuurt vaak wel geld naar familie in het land van herkomst, en dat geld "
              "weegt voor sommige landen zwaarder dan alle ontwikkelingshulp samen."),
    ]),
    ("mondialisering", "onthoud", "Vrijhandel haalt drempels weg",
     "Zes samenwerkingsverbanden: EU, VN, G8, G20, Mercosur en NAVO."),

    # ── Duurzaam omgaan met de ruimte.
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "Een land met een hoge Human Development Index heeft dus niet", [
        ("p", "Tegelijk stijgt met welvaart ook het verbruik, en juist dat spanningsveld is de "
              "kern van het debat. Een welvarend land heeft dus niet vanzelf een kleine "
              "<strong>ecologische voetafdruk</strong>; vaak is het omgekeerde waar. De "
              "ecologische voetafdruk is de oppervlakte aarde die nodig is om iemands verbruik te "
              "dekken en zijn afval te verwerken. Leefden alle mensen zoals de gemiddelde "
              "West-Europeaan, dan was er meer dan één aarde nodig."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "hergebruik van een leegstaand gebouw, inbreiding", [
        ("p", "<strong>Duurzaam ruimtegebruik</strong> betekent met dezelfde oppervlakte méér "
              "doen, in plaats van telkens nieuwe ruimte aan te snijden: hergebruik van een "
              "leegstaand gebouw, bouwen op een oud bedrijfsterrein, een terrein met meerdere "
              "functies. Nieuwe grond aansnijden is altijd de duurste keuze voor de planeet. "
              "Duurzaamheid en economische groei sluiten elkaar daarbij niet uit: hergebruik, "
              "isolatie, hernieuwbare energie en kringloop leveren ook werk en omzet op. De "
              "spanning is echt, maar ze is geen wet."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "De fiche somt vijf gevolgen van verstedelijking", [
        ("p", "Verstedelijking heeft vijf gevolgen voor het leefmilieu: "
              "<strong>versnippering</strong> van de open ruimte, de gevolgen van "
              "<strong>verharding</strong>, het <strong>hitte-eilandeffect</strong>, "
              "<strong>luchtvervuiling</strong> en <strong>verkeersdrukte</strong>."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "noemt de fiche drie begrippen", [
        ("p", "Bij grondstofontginning, energieproductie en industrie horen twee begrippen: "
              "<strong>industrialisatie</strong> (er komt fabrieksactiviteit bij, met werk en met "
              "ruimtebeslag) en <strong>de-industrialisatie</strong> (die verdwijnt weer, en het "
              "werk ermee)."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "Reconversie is duurzamer dan een nieuw terrein", [
        ("p", "Bouwen op een oud bedrijfsterrein is duurzamer dan een nieuw terrein aansnijden, "
              "want de grond werd al gebruikt en er gaat geen open ruimte verloren. Goedkoper is "
              "het niet noodzakelijk: een oude fabriekssite kan vervuilde grond bevatten, want "
              "zware metalen, olie en oplosmiddelen blijven decennia in de bodem. Die grond moet "
              "eerst <strong>gesaneerd</strong> worden, en die kost is een van de redenen waarom "
              "zo'n site soms jaren leeg blijft liggen. Kiest een gemeente tussen een verkaveling "
              "op akkerland en het opknappen van zo'n site, dan is de site de duurzamere keuze."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "vervang-blok", "Bij de landbouw noemt de fiche <strong>bodemerosie</strong>", [
        ("p", "Bij de landbouw gaat het om <strong>ontbossing</strong> en "
              "<strong>schaalvergroting</strong>. Ontbossing voor landbouwgrond laat koolstof "
              "vrij die in het bos en de bosbodem opgeslagen zat, bovenop het verlies aan "
              "biodiversiteit. En akkerbouw op een pas ontbost tropisch perceel levert na enkele "
              "jaren veel minder op, want de vruchtbare laag is er dun en raakt snel uitgeput. "
              "Schaalvergroting maakt de velden groter en de bedrijven minder talrijk, en veegt "
              "hagen, houtkanten en veldwegen uit het landschap."),
    ]),
    ("duurzaam-omgaan-met-de-ruimte", "onthoud", "Een hoge HDI betekent niet vanzelf",
     "Veel welvaart betekent niet vanzelf een kleine ecologische voetafdruk."),
    ("duurzaam-omgaan-met-de-ruimte", "onthoud", "Reconversie is duurzamer dan een nieuw terrein",
     "Bouwen op een oud bedrijfsterrein is duurzamer dan nieuwe grond aansnijden, maar niet noodzakelijk goedkoper."),
]

INGREPEN += [
    # ── Het versterkte broeikaseffect. Geen stralingsbalans en geen albedo.
    ("het-versterkte-broeikaseffect", "onder", None,
     "De vier sferen en de koolstofcyclus, de broeikasgassen, en de oorzaken en gevolgen van de opwarming."),
    ("het-versterkte-broeikaseffect", "kop", "Broeikasgassen en de stralingsbalans",
     "De broeikasgassen"),
    ("het-versterkte-broeikaseffect", "vervang-blok", "De <strong>broeikasgassen</strong> uit de fiche", [
        ("p", "De <strong>broeikasgassen</strong> zijn waterdamp (H₂O), koolstofdioxide (CO₂), "
              "methaan (CH₄) en lachgas (N₂O). Zuurstof en stikstofgas vormen samen het grootste "
              "deel van de lucht maar werken niet als broeikasgas."),
    ]),
    ("het-versterkte-broeikaseffect", "vervang-blok", "De <strong>stralingsbalans</strong> is de verhouding", [
        ("p", "Broeikasgassen laten zonlicht vlot binnen, maar houden een deel van de "
              "warmtestraling die de aarde teruggeeft in de atmosfeer vast en sturen die opnieuw "
              "naar beneden. Blijft er zo meer warmte binnen dan er weggaat, dan warmt de aarde "
              "op tot het weer in evenwicht is."),
        ("p", "Daar zit de <strong>koolstofcyclus</strong> of <strong>koolstofkringloop</strong> "
              "middenin. Verbranden we fossiele "
              "brandstoffen, dan verhuist koolstof die miljoenen jaren in de geosfeer lag in "
              "enkele eeuwen naar de atmosfeer. Een bos dat gekapt en verbrand wordt, doet "
              "hetzelfde met de koolstof die in de stammen, de takken en de bodem lag. Hoe meer "
              "koolstof in de lucht, hoe sterker het broeikaseffect."),
    ]),
    ("het-versterkte-broeikaseffect", "schrap-blok", "Het tweede sleutelbegrip is het", None),
    ("het-versterkte-broeikaseffect", "schrap-blok", "laag albedo", None),
    ("het-versterkte-broeikaseffect", "vervang-blok", "Smelt zee-ijs, dan komt er donkerder water bloot", [
        ("p", "Smelt zee-ijs, dan komt er donkerder water bloot dat meer warmte opneemt. Meer "
              "opwarming geeft dus nog minder ijs. Zo'n zichzelf versterkende lus heet een "
              "<strong>terugkoppeling</strong> in het <strong>klimaatsysteem</strong>: een "
              "gevolg dat zijn eigen oorzaak versterkt of verzwakt. Daardoor is dat systeem zo "
              "moeilijk voorspelbaar. Dooiende <strong>permafrost</strong> is er nog zo een: in "
              "de bevroren bodem van Siberië en Canada zit enorm veel organisch materiaal, en "
              "ontdooit die, dan begint het te rotten en komen er methaan en CO₂ vrij die er "
              "duizenden jaren in opgesloten zaten."),
    ]),
    ("het-versterkte-broeikaseffect", "vervang-blok", "De fiche somt vijf gevolgen op.", [
        ("p", "Er zijn vier gevolgen. Het eerste is de <strong>zeespiegelstijging</strong>, met "
              "twee oorzaken tegelijk: water zet uit als het warmer wordt, en het "
              "<strong>landijs</strong> van Groenland, Antarctica en de gletsjers voegt water toe "
              "dat eerst op land lag. Drijvend <strong>zee-ijs</strong> telt daarin níét mee: dat "
              "verplaatst al evenveel water als het weegt, dus het smelten ervan verandert het "
              "peil niet. Laaggelegen kustgebieden, delta's zoals die van de Ganges en de Nijl, "
              "en eilandstaten in de Stille Oceaan lopen het grootste risico, en net daar wonen "
              "heel veel mensen dicht op elkaar."),
    ]),
    ("het-versterkte-broeikaseffect", "vervang-blok", "Het vijfde is de <strong>verspreiding van tropische", [
        ("p", "In het hooggebergte krimpen de <strong>gletsjers</strong>. Een gletsjer is een "
              "waterreservoir dat in de zomer traag leegloopt; verdwijnt hij, dan valt dat "
              "zomerdebiet weg, net wanneer landbouw en drinkwater het hardst nodig zijn. Ook "
              "dichter bij huis is de opwarming een waterprobleem: drogere zomers en hevigere "
              "buien tegelijk."),
    ]),
    ("het-versterkte-broeikaseffect", "vervang-blok", "dan een bergland met een hoge HDI", [
        ("p", "De opwarming treft niet elk land even hard: ligging, reliëf en welvaart bepalen "
              "mee hoe kwetsbaar een land is. Een laaggelegen deltastaat met weinig middelen "
              "loopt veel meer risico dan een bergland dat zich kan beschermen. En het zijn niet "
              "de landen met de hoogste uitstoot per inwoner die het hardst getroffen worden: "
              "meestal is het omgekeerd. Landen met een lagere ontwikkelingsgraad stoten per "
              "inwoner veel minder uit en hebben tegelijk het minste geld om zich te beschermen. "
              "Dat is de kern van wat men klimaatrechtvaardigheid noemt."),
    ]),
    ("het-versterkte-broeikaseffect", "onthoud", "Het albedo is het weerkaatsingsvermogen",
     "De koolstofcyclus verbindt de geosfeer, de biosfeer, de atmosfeer en de hydrosfeer."),
    ("het-versterkte-broeikaseffect", "onthoud", "Smeltend ijs verlaagt het albedo",
     "Een terugkoppeling is een gevolg dat zijn eigen oorzaak versterkt of verzwakt."),
    ("het-versterkte-broeikaseffect", "onthoud", "Vijf gevolgen: zeespiegelstijging",
     "Vier gevolgen: zeespiegelstijging, verschuivende klimaatzones en leefgebieden, extreme weerfenomenen."),

    # ── Een geografisch onderzoek voeren. Alleen de verwijzingen gaan eruit.
    ("een-geografisch-onderzoek-voeren", "vervang-blok", "Volgens de fiche kan je onderzoek over vier", [
        ("p", "Je onderzoek kan over vier thema's gaan: <strong>mobiliteit</strong> (files, lawaai "
              "en geluidshinder, luchtvervuiling en luchtkwaliteit), "
              "<strong>waterproblematieken</strong> (watertekort of waterschaarste, "
              "overstromingen), <strong>veranderend landgebruik</strong> (schaalvergroting, "
              "verstedelijking, aanpassingen voor duurzaamheid) en "
              "<strong>klimaatverandering</strong> in het landschap. Telkens onderzoek je "
              "oorzaken én gevolgen."),
    ]),
    ("een-geografisch-onderzoek-voeren", "vervang-blok", "De <strong>geografische hulpbronnen</strong> uit de fiche", [
        ("p", "De <strong>geografische hulpbronnen</strong> zijn onder meer een atlas, kaarten, "
              "satellietbeelden, foto's en luchtfoto's, tekeningen en schetsen, teksten, figuren, "
              "determineertabellen, cijfergegevens, grafieken, leeftijdshistogrammen, "
              "klimatogrammen, tabellen en diagrammen. Op het examen krijg je zelf een algemene "
              "wereldatlas mee, dus loont het om er thuis mee te oefenen."),
    ]),
    ("een-geografisch-onderzoek-voeren", "vervang-blok", "Die laatste stap vraagt de fiche uitdrukkelijk", [
        ("p", "Die laatste stap wordt uitdrukkelijk van je gevraagd: leg uit hoe de voorstelling "
              "van de gegevens op digitale kaarten je geholpen heeft, én wat de beperkingen "
              "waren. Een bron kritisch bekijken hoort bij het onderzoek zelf; wie zegt wat zijn "
              "bron niet kan tonen, laat zien dat hij ze begrijpt. Dat is het verschil tussen een "
              "kaart aflezen en met een kaart onderzoeken."),
    ]),
    ("een-geografisch-onderzoek-voeren", "vervang-blok", "In de fiche staat dat álle te kennen inhoud", [
        ("weetje", "Álle te kennen inhoud kan in dit deel van het examen verwerkt zijn. Onderzoek "
                   "is dus geen apart stukje theorie, maar de manier waarop de rest getoetst "
                   "wordt."),
    ]),
]


def pas_toe(bundels: dict):
    for kort, soort, waar, inhoud in INGREPEN:
        if kort not in bundels:
            raise SystemExit(f"Onbekende bundel in INGREPEN: {kort}")
        b = bundels[kort]
        if soort == "onder":
            b["onder"] = inhoud
        elif soort == "kop":
            raak = [s for s in b["secties"] if s["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} secties heten {waar!r}, verwacht 1")
            raak[0]["kop"] = inhoud
        elif soort == "schrap-sectie":
            raak = [i for i, s in enumerate(b["secties"]) if s["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} secties heten {waar!r}, verwacht 1")
            b["secties"].pop(raak[0])
        elif soort == "sectie-achteraan":
            b["secties"].append(copy.deepcopy(inhoud))
        elif soort in ("schrap-blok", "vervang-blok"):
            raak = [
                (i, j)
                for i, s in enumerate(b["secties"])
                for j, bl in enumerate(s["blokken"])
                if waar in tekst_van(bl)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} blokken met {waar!r}, verwacht 1")
            i, j = raak[0]
            if soort == "schrap-blok":
                b["secties"][i]["blokken"].pop(j)
            else:
                b["secties"][i]["blokken"][j:j + 1] = list(inhoud)
        elif soort == "onthoud":
            raak = [i for i, r in enumerate(b["onthoud"]) if waar in r]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} onthoudregels met {waar!r}, verwacht 1")
            if inhoud is None:
                b["onthoud"].pop(raak[0])
            else:
                b["onthoud"][raak[0]] = inhoud
        else:
            raise SystemExit(f"Onbekende ingreep: {soort}")


def bouw() -> dict:
    uit = {}
    for kort in ORDE:
        if kort not in doorstroom.BUNDELS:
            raise SystemExit(f"Onbekende doorstroombundel: {kort}")
        b = copy.deepcopy(doorstroom.BUNDELS[kort])
        b["niveau"] = DF
        uit[kort] = b
    pas_toe(uit)

    for kort, b in uit.items():
        alles = " ".join(
            [b["titel"], b["onder"]]
            + [s["kop"] for s in b["secties"]]
            + [tekst_van(bl) for s in b["secties"] for bl in s["blokken"]]
            + b.get("onthoud", [])
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{kort} gebruikt nog {woord!r}, dat staat niet op deze fiche")
        if not b.get("onthoud"):
            raise SystemExit(f"{kort} heeft geen onthoudlijstje")

    return {kort + NIEUW: uit[kort] for kort in ORDE}


BUNDELS = bouw()

if __name__ == "__main__":
    for sleutel, b in BUNDELS.items():
        bundel.schrijf(b, sleutel)
        print(" ", sleutel)

# -*- coding: utf-8 -*-
"""Uitdaging Aardrijkskunde 🚀 Boost doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een bevolkingspiramide en het model van de demografische
transitie om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, rekenvragen en een korte schrijfopdracht. Geen nieuwe
leerstof: alles staat in de hoofdstukken van Aardrijkskunde Boost doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_aardrijkskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Aardrijkskunde"
BESTAND = "boost-aardrijkskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/aardrijkskunde-boost-uitdaging"
PIR = "piramide-land-x.svg"
TRANS = "demografische-transitie.svg"

# klikvakken uit maak_prenten_boost_aardrijkskunde.py
RIJ = {"0-9": [22.0, 79.7, 56.0, 7.8], "50-59": [11.4, 40.6, 77.1, 7.8], "80+": [30.6, 17.2, 38.7, 7.8]}
FASE = {1: [9.0, 16.7, 21.0, 70.0], 2: [30.0, 16.7, 21.0, 70.0], 3: [51.0, 16.7, 21.0, 70.0], 4: [72.0, 16.7, 21.0, 70.0]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Piramide (prent)
    klik("Bekijk de bevolkingspiramide. Klik op de leeftijdsgroep met het grootste aandeel van de bevolking.",
         PIR, [RIJ["50-59"]],
         "De groep van 50 tot 59 jaar heeft de langste balken: ruim 7 % mannen en 7 % vrouwen. Dat zijn de kinderen van een vroegere geboortegolf."),
    klik("Klik op de leeftijdsgroep waar duidelijk meer vrouwen dan mannen zijn.",
         PIR, [RIJ["80+"]],
         "Bij de 80-plussers is de vrouwenbalk veel langer: vrouwen leven gemiddeld langer dan mannen."),
    met_prent(PIR, tabel(
        "Lees de piramide van land X. Welke uitspraak klopt?",
        [
            ("Er worden minder kinderen geboren dan dertig jaar geleden.", J),
            ("Het land vergrijst.", J),
            ("De piramide heeft de vorm van een brede driehoek, typisch voor een jong land.", F),
            ("Meer dan de helft van de bevolking is jonger dan 20 jaar.", F),
        ],
        "De basis is smaller dan de middengroepen en er zijn veel ouderen. Een jong land heeft een brede basis die naar boven smal wordt.")),
    met_prent(PIR, mk(
        "Welk probleem krijgt land X de komende jaren waarschijnlijk?",
        ["Meer kosten voor pensioenen en zorg.", "Een tekort aan plaatsen in kleuterscholen.", "Te veel jongeren die werk zoeken.", "Een snelle stijging van het geboortecijfer."],
        0,
        "Als de grote groep van 50 tot 69 jaar ouder wordt, stijgen de uitgaven voor pensioenen en gezondheidszorg.")),

    # Demografische transitie (prent)
    klik("Bekijk het model. Klik op de fase waarin het sterftecijfer sterk daalt, terwijl het geboortecijfer hoog blijft.",
         TRANS, [FASE[2]],
         "In fase 2 dalen de sterftecijfers door betere voeding, hygiëne en geneeskunde. De geboortecijfers blijven nog hoog."),
    klik("Klik op de fase waarin vooral het geboortecijfer sterk daalt.",
         TRANS, [FASE[3]],
         "In fase 3 krijgen gezinnen minder kinderen: door verstedelijking, onderwijs voor meisjes en anticonceptie."),
    klik("Klik op de fase waarin beide cijfers laag zijn en dicht bij elkaar liggen.",
         TRANS, [FASE[4]],
         "In fase 4 zijn geboorte- en sterftecijfer laag. De bevolking groeit nog nauwelijks, zoals in België."),
    met_prent(TRANS, keuze(
        "De natuurlijke aangroei is het verschil tussen [[*geboortecijfer en sterftecijfer|immigratie en emigratie]]. In fase 1 is de natuurlijke aangroei [[*klein|zeer groot]] omdat beide cijfers hoog zijn.",
        "Natuurlijke aangroei = geboortecijfer − sterftecijfer. Als beide hoog en ongeveer gelijk zijn, groeit de bevolking nauwelijks.")),

    # Situeren
    tabel(
        "Op welk continent ligt dit land?",
        [
            ("Nigeria", "Afrika"),
            ("Indonesië", "Azië"),
            ("Brazilië", "Zuid-Amerika"),
            ("Canada", "Noord-Amerika"),
        ],
        "Nigeria ligt in West-Afrika, Indonesië in Zuidoost-Azië, Brazilië in Zuid-Amerika en Canada in Noord-Amerika.",
        kolommen=["Afrika", "Azië", "Noord-Amerika", "Zuid-Amerika"]),
    tabel(
        "Op welk halfrond ligt deze plaats: noordelijk of zuidelijk?",
        [
            ("41° NB en 2° OL", "Noordelijk"),
            ("34° ZB en 18° OL", "Zuidelijk"),
            ("23° ZB en 43° WL", "Zuidelijk"),
            ("51° NB en 4° OL", "Noordelijk"),
        ],
        "NB staat voor noorderbreedte, ZB voor zuiderbreedte. De lengte (OL of WL) zegt niets over noord of zuid.",
        kolommen=["Noordelijk", "Zuidelijk"]),
    keuze(
        "De afstand die je echt aflegt in kilometer is de [[*werkelijke afstand|mentale afstand]]. Hoe ver je denkt dat iets ligt, is de [[*mentale afstand|werkelijke afstand]].",
        "Een mentale afstand kan groter of kleiner lijken dan de werkelijke, bijvoorbeeld door hoe goed je een plaats kent."),

    # Bevolking
    sorteer(
        "Is dit een push- of een pullfactor voor migratie?",
        ["Pushfactor", "Pullfactor"],
        [
            ["Oorlog in het eigen land", "Pushfactor"],
            ["Werk in een ander land", "Pullfactor"],
            ["Langdurige droogte", "Pushfactor"],
            ["Goede scholen en ziekenhuizen", "Pullfactor"],
        ],
        "Pushfactoren duwen mensen weg uit hun land. Pullfactoren trekken ze aan naar een ander land."),
    inv("Een stad heeft 120 000 inwoners. Er worden 1800 kinderen geboren in een jaar. Wat is het geboortecijfer in promille?",
        ["15"],
        "1800 / 120 000 · 1000 = 15 ‰."),
    tabel(
        "Waar wonen de mensen? Dichtbevolkt of dunbevolkt?",
        [
            ("De Gangesvlakte in India", "Dichtbevolkt"),
            ("De Sahara", "Dunbevolkt"),
            ("Het noorden van Canada", "Dunbevolkt"),
            ("Nederland en België", "Dichtbevolkt"),
        ],
        "Vruchtbare vlakten en rijke regio's zijn dichtbevolkt. Woestijnen en zeer koude gebieden zijn dunbevolkt.",
        kolommen=["Dichtbevolkt", "Dunbevolkt"]),
    mk("Wat is de bevolkingsdichtheid van een gebied van 500 km² met 150 000 inwoners?",
       ["300 inwoners per km²", "3000 inwoners per km²", "30 inwoners per km²", "75 inwoners per km²"],
       0,
       "150 000 / 500 = 300 inwoners per km²."),

    # Stad en platteland
    keuze(
        "Bouwen op open plekken binnen de bestaande stad heet [[*inbreiding|uitbreiding|versnippering]]. Een oude fabriek ombouwen tot appartementen is een [[*functiewijziging|ontvolking]].",
        "Inbreiding spaart de open ruimte rond de stad. Bij functiewijziging krijgt een gebouw een nieuwe bestemming."),
    tabel(
        "Welk stedelijk verschijnsel wordt hier beschreven?",
        [
            ("In de stad is het 's zomers meetbaar warmer dan op het platteland.", "Hitte-eiland"),
            ("Wegen en bebouwing delen de open ruimte op in kleine stukken.", "Versnippering"),
            ("Rijke en arme gezinnen wonen in aparte wijken.", "Sociale segregatie"),
        ],
        "Verharding houdt warmte vast, versnippering knipt de natuur in stukken en segregatie volgt vaak de woningprijzen.",
        kolommen=["Hitte-eiland", "Versnippering", "Sociale segregatie"]),
    mk("Wat is een sloppenwijk?",
       ["Een wijk met zelfgebouwde, armoedige woningen zonder goede voorzieningen.", "Een nieuwe villawijk aan de rand van een rijke stad, met grote tuinen en garages.", "Een historische binnenstad met musea, pleinen en elke dag veel toeristen.", "Een industrieterrein langs een kanaal met grote fabrieken en loodsen."],
       0,
       "In veel steden in het Zuiden bouwen migranten van het platteland zelf woningen, vaak zonder water, riolering of elektriciteit."),

    # Grondstoffen en energie
    sorteer(
        "Is dit een hernieuwbare of een niet-hernieuwbare energiebron?",
        ["Hernieuwbaar", "Niet-hernieuwbaar"],
        [
            ["zonne-energie", "Hernieuwbaar"],
            ["aardgas", "Niet-hernieuwbaar"],
            ["windenergie", "Hernieuwbaar"],
            ["steenkool", "Niet-hernieuwbaar"],
            ["waterkracht", "Hernieuwbaar"],
            ["aardolie", "Niet-hernieuwbaar"],
        ],
        "Fossiele brandstoffen raken op. Zon, wind en water vernieuwen zich voortdurend."),
    tabel(
        "Tot welke economische sector hoort dit?",
        [
            ("Een boer die tarwe teelt", "Primaire sector"),
            ("Een fabriek die auto's maakt", "Secundaire sector"),
            ("Een kapper", "Tertiaire sector"),
            ("Een mijn die koper ontgint", "Primaire sector"),
        ],
        "De primaire sector haalt grondstoffen uit de natuur, de secundaire verwerkt ze en de tertiaire levert diensten.",
        kolommen=["Primaire sector", "Secundaire sector", "Tertiaire sector"]),
    keuze(
        "Een fabriek die zich vestigt dicht bij een haven doet dat vaak om de [[*transportkosten|lonen|belastingen op inkomen]] te beperken. Zo spaart het bedrijf op het vervoer van [[*grondstoffen en goederen|toeristen]].",
        "Bedrijven kiezen hun plaats onder meer op basis van vervoer, grondstoffen, arbeid en afzetmarkt. Een haven ligt vlak bij de aanvoer over zee."),

    # Landbouw, handel en toerisme
    tabel(
        "Intensieve of extensieve landbouw?",
        [
            ("Veel kunstmest en machines op een klein stuk grond", "Intensief"),
            ("Grote kuddes vee op uitgestrekte graslanden", "Extensief"),
            ("Serres met tomaten in het Westland", "Intensief"),
        ],
        "Intensieve landbouw haalt veel opbrengst uit weinig grond met veel arbeid of kapitaal. Extensieve landbouw gebruikt veel grond met weinig input.",
        kolommen=["Intensief", "Extensief"]),
    mk("Wat is een nadeel van massatoerisme voor een bestemming?",
       ["Drukte, afval en stijgende huurprijzen voor de bewoners.", "Er komen nooit nieuwe banen bij voor de lokale bevolking.", "Er komt helemaal geen geld binnen in de regio of het dorp.", "De lokale cultuur wordt vanzelf beter beschermd."],
       0,
       "Toerisme brengt geld en banen, maar ook drukte, vervuiling en duurdere woningen voor de inwoners."),

    # Mondialisering
    keuze(
        "Een smartphone wordt ontworpen in de VS, gemaakt in China en verkocht in Europa. Dat is een voorbeeld van [[*mondialisering|verstedelijking|ontvolking]]. Daardoor hangen landen [[*sterker|minder sterk]] van elkaar af.",
        "Door goedkoop transport en internet verspreiden bedrijven hun productie over de wereld."),
    sorteer(
        "Is dit een voordeel of een nadeel van mondialisering?",
        ["Voordeel", "Nadeel"],
        [
            ["Goedkopere producten voor consumenten", "Voordeel"],
            ["Banen verdwijnen naar lageloonlanden", "Nadeel"],
            ["Meer uitwisseling van kennis en cultuur", "Voordeel"],
            ["Meer CO₂-uitstoot door transport", "Nadeel"],
        ],
        "Mondialisering brengt kansen en risico's mee, voor mensen en voor het milieu."),

    # Duurzaamheid en klimaat
    tabel(
        "Klopt dit over het versterkte broeikaseffect?",
        [
            ("Verbranding van fossiele brandstoffen stoot CO₂ uit.", J),
            ("Ontbossing versterkt het broeikaseffect.", J),
            ("Het broeikaseffect is volledig door de mens gemaakt.", F),
            ("Een stijgende zeespiegel is een gevolg van de opwarming.", J),
        ],
        "Er is een natuurlijk broeikaseffect dat de aarde leefbaar houdt. De mens versterkt het met extra broeikasgassen."),
    koppel(
        "Koppel het broeikasgas aan een belangrijke bron.",
        [
            ["koolstofdioxide (CO₂)", "auto's en fabrieken"],
            ["methaan (CH₄)", "veeteelt en rijstvelden"],
            ["lachgas (N₂O)", "kunstmest in de landbouw"],
        ],
        ["zonnepanelen"],
        "Elk broeikasgas heeft zijn eigen bronnen. Zonnepanelen stoten tijdens gebruik geen broeikasgassen uit."),
    keuze(
        "Fietsen in plaats van met de auto naar school gaan is een [[*duurzamere manier om je te verplaatsen|vorm van massatoerisme|vorm van versnippering]]. Het verkleint je [[*ecologische voetafdruk|bevolkingsdichtheid]].",
        "Duurzaam omgaan met de ruimte betekent dat ook toekomstige generaties nog goed kunnen leven."),

    # Onderzoek
    volgorde(
        "Zet de stappen van een geografisch onderzoek in de juiste volgorde.",
        ["Onderzoeksvraag stellen", "Hypothese opschrijven", "Informatie verzamelen", "Gegevens verwerken in kaarten en grafieken", "Besluit formuleren", "Rapporteren"],
        "Eerst weet je wat je wil weten en wat je verwacht, dan zoek je informatie, verwerk je die, trek je een besluit en rapporteer je."),

    # Extra
    inv("Een land heeft een geboortecijfer van 12 ‰ en een sterftecijfer van 9 ‰. Hoeveel bedraagt de natuurlijke aangroei in ‰?",
        ["3"],
        "12 − 9 = 3 ‰."),
    mk("Waarom zijn veel steden ontstaan aan rivieren of kusten?",
       ["Water zorgde voor drinkwater, vervoer en handel.", "Daar was het altijd warmer dan in het binnenland.", "Er waren daar nooit overstromingen of stormen.", "De grond was daar het goedkoopst om te kopen."],
       0,
       "Rivieren en havens waren belangrijk voor transport en handel, en ze leverden water."),
    tabel(
        "Welk onderdeel van Geopunt gebruik je hiervoor?",
        [
            ("Een adres of gemeente opzoeken", "Zoekbalk"),
            ("De oppervlakte van een bedrijventerrein bepalen", "Meetgereedschap"),
            ("Weten wat een kleur op de kaart betekent", "Legende"),
        ],
        "Met de zoekbalk vind je een plaats, met het meetgereedschap bepaal je afstanden en oppervlakten, en de legende verklaart kleuren en symbolen.",
        kolommen=["Zoekbalk", "Meetgereedschap", "Legende"]),
    keuze(
        "Een land waar de meeste mensen in de landbouw werken, heeft vaak een [[*brede basis|smalle basis]] in de bevolkingspiramide, omdat er [[*veel|weinig]] kinderen geboren worden.",
        "In landbouwsamenlevingen helpen kinderen mee en is de kindersterfte vaak hoger: gezinnen zijn groter."),
    sleep(
        "Mensen die een land binnenkomen om er te wonen, heten [[immigranten]]. Mensen die vertrekken, heten [[emigranten]].",
        ["toeristen", "pendelaars"],
        "Immigratie is inwijking, emigratie is uitwijking."),

    mk("Waarom verhuizen veel fabrieken uit Europa naar landen in Azië?",
       ["Omdat de lonen en andere kosten daar lager liggen.", "Omdat er in Europa geen grondstoffen meer te koop zijn.", "Omdat transport over zee vandaag helemaal gratis is geworden.", "Omdat Europese klanten geen producten uit Europa willen."],
       0,
       "Bedrijven zoeken plaatsen waar ze goedkoper kunnen produceren. Dat heet delokalisatie en hoort bij mondialisering."),
    tabel(
        "Gevolg van de opwarming van de aarde: waar of niet waar?",
        [
            ("Gletsjers en ijskappen smelten.", J),
            ("Er komen meer periodes van extreme hitte en droogte.", J),
            ("Laaggelegen kustgebieden lopen meer risico op overstromingen.", J),
            ("De hoeveelheid CO₂ in de lucht daalt vanzelf.", F),
        ],
        "Door de opwarming smelt ijs, stijgt de zeespiegel en komt extreem weer vaker voor. CO₂ daalt niet vanzelf: daar zijn maatregelen voor nodig."),
    koppel(
        "Koppel de vorm van landbouw aan een voorbeeld.",
        [
            ["zelfvoorzieningslandbouw", "een gezin teelt maïs voor eigen gebruik"],
            ["akkerbouw", "graan of aardappelen telen op grote velden"],
            ["tuinbouw", "groenten, fruit en bloemen, vaak in serres"],
        ],
        ["een vissersboot op zee"],
        "Zelfvoorziening is voor eigen gebruik, akkerbouw teelt gewassen op het veld en tuinbouw richt zich op groenten, fruit en sierteelt. Visserij is geen landbouw."),
    volgorde(
        "Zet de onderdelen van een productieketen van een chocoladereep in volgorde.",
        ["Cacaoboer oogst de bonen", "Bonen worden per schip vervoerd", "Fabriek maakt chocolade", "Winkel verkoopt de reep"],
        "Eerst de primaire sector (oogst), dan transport, dan de secundaire sector (fabriek) en tot slot de tertiaire sector (winkel)."),
    keuze(
        "De verwachting die je vooraf opschrijft en met je onderzoek wil toetsen, heet een [[*hypothese|legende|besluit]]. Een onderzoek is ook geslaagd als die verwachting [[*niet blijkt te kloppen|altijd juist blijkt]].",
        "Een hypothese toets je. Ook een verworpen hypothese levert kennis op, zolang je besluit op je gegevens steunt."),
    # Schrijfopdracht
    open_("Je gemeente vergrijst sterk. Schrijf in 4 à 6 zinnen welke gevolgen dat heeft en welke twee maatregelen de gemeente kan nemen.",
          "Als de bevolking vergrijst, zijn er meer ouderen en minder jongeren. Er is meer nood aan zorg, woonzorgcentra en aangepaste woningen. Er zijn ook minder mensen die werken en belastingen betalen. De gemeente kan meer aangepaste woningen en zorgdiensten voorzien, zodat ouderen langer thuis kunnen wonen. Ze kan ook jonge gezinnen aantrekken met betaalbare woningen en goede scholen.",
          "Een goed antwoord noemt minstens twee gevolgen (zorg, pensioenen, minder werkenden, andere woningen) en twee passende maatregelen."),
]

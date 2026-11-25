# -*- coding: utf-8 -*-
"""Uitdaging Aardrijkskunde 🌍 Beyond (25 november 2026), in de vormen van het
examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen, van het heelal en de atmosfeer tot platentektoniek, gesteenten,
klimaatverandering en ruimtegebruik. Casussen, tabellen, keuzelijsten,
slepen, koppelen, sorteren, volgorde, vijf klikvragen op twee zelf getekende
prenten en een open vraag. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Aardrijkskunde Beyond.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_aardrijkskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Aardrijkskunde"
BESTAND = "beyond-aardrijkskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/aardrijkskunde-beyond-uitdaging"
PLATEN = "doorsnede-platen.svg"
WEER = "weerkaart-depressie.svg"
# klikvakken: zie maak_prenten_beyond_aardrijkskunde.py
PLEK_A = [8.0, 9.1, 14.0, 58.9]
PLEK_B = [33.0, 9.1, 14.0, 58.9]
PLEK_C = [62.0, 9.1, 14.0, 58.9]
KOUDFRONT = [21.0, 59.7, 24.0, 39.5]
HOOG = [75.0, 14.5, 24.0, 32.3]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Doorsnede door de lithosfeer (prent)
    klik("Bekijk de doorsnede. Klik op de plek waar een mantelpluim midden op een plaat een vulkaaneiland laat ontstaan.",
         PLATEN, [PLEK_A],
         "Bij A stijgt magma op ver van elke plaatgrens: een hotspot. Schuift de plaat verder, dan ontstaat er een rij eilanden."),
    klik("Klik op de plek waar twee platen uit elkaar gaan en er nieuwe oceaanbodem ontstaat.",
         PLATEN, [PLEK_B],
         "Bij B welt magma op tussen twee platen die uit elkaar schuiven: een divergente plaatgrens met een oceanische rug."),
    klik("Klik op de plek waar een oceanische plaat onder een continentale plaat duikt.",
         PLATEN, [PLEK_C],
         "Bij C duikt de zwaardere oceanische plaat onder het continent: een subductiezone, met een diepe trog aan de oceaankant."),
    met_prent(PLATEN, mk(
        "Welk gebergte is een voorbeeld van wat er bij D ontstaat?",
        ["de Alpen, tussen twee botsende continenten", "de Andes, een kustgebergte met vulkanen", "de Ardennen, gevormd door de Hercynische plooiing", "IJsland, op een rug en een hotspot"],
        1,
        "Boven een subductiezone ontstaat een kustgebergte met vulkanen, zoals de Andes langs de Grote Oceaan.")),
    met_prent(PLATEN, tabel(
        "Klopt dit over de doorsnede?",
        [
            ("Bij B komt er nieuwe oceanische korst bij.", J),
            ("De aarde wordt groter doordat er bij B korst bijkomt.", F),
            ("De continentale korst is gemiddeld ouder dan de oceanische korst.", J),
            ("De vulkaan bij A ligt op een plaatgrens.", F),
        ],
        "Wat bij een rug bijkomt, verdwijnt in een subductiezone: de aarde groeit niet. Oceanische korst wordt telkens weer opgeslokt, daarom is ze jonger. A is een hotspot, midden op een plaat.")),

    # Weerkaart (prent)
    klik("Bekijk de weerkaart. Klik op het koufront.",
         WEER, [KOUDFRONT],
         "Een koufront teken je met driehoekjes in de richting waarin het front trekt. Het warmtefront heeft halve bolletjes."),
    klik("Klik op het gebied waar je vandaag het meest kans hebt op droog en rustig weer.",
         WEER, [HOOG],
         "In een hogedrukgebied daalt de lucht. Dalende lucht warmt op en wolken lossen op: daar is het meestal droog."),
    met_prent(WEER, keuze(
        "Rond de L op het noordelijk halfrond draait de wind [[*tegen de klok in|met de klok mee]]. In het centrum van de L [[*stijgt|daalt]] de lucht.",
        "Door de corioliskracht buigt de wind op het noordelijk halfrond naar rechts af. Rond een lagedrukgebied draait hij zo tegen de klok in, en in het centrum stijgt de lucht op.")),
    met_prent(WEER, mk(
        "Waar op deze kaart waait de wind het hardst?",
        ["waar de isobaren ver uit elkaar liggen", "waar de isobaren dicht bij elkaar liggen", "precies in het centrum van de H", "overal even hard, want de druk is overal gelijk"],
        1,
        "Hoe dichter de isobaren bij elkaar liggen, hoe groter het drukverschil over een korte afstand en hoe harder de wind.")),
    met_prent(WEER, tabel(
        "Klopt dit over de fronten op de kaart?",
        [
            ("Een koufront geeft meestal kortere maar hevigere buien dan een warmtefront.", J),
            ("Een front is de grens tussen twee luchtsoorten.", J),
            ("De neerslag valt vooral rond het centrum van de H.", F),
        ],
        "De neerslagzones liggen langs de fronten rond het lagedrukgebied, niet bij de H.")),

    # Casus: de sterrenhemel
    casus(
        "Op een heldere nacht kijkt Mila door een telescoop naar een ster op ongeveer 4 lichtjaar van ons en naar de Andromedanevel, een sterrenstelsel op ongeveer 2,5 miljoen lichtjaar.",
        [
            keuze(
                "Een lichtjaar is een maat voor [[*afstand|tijd|helderheid]]. Het licht van die ster vertrok ongeveer [[*4 jaar|4 dagen|4 uur]] geleden.",
                "Een lichtjaar is de afstand die licht in één jaar aflegt. Licht van 4 lichtjaar ver doet er 4 jaar over."),
            mk("Waarom kijkt Mila eigenlijk in het verleden?",
               ["Omdat het licht er lang over deed om hier te komen.", "Omdat sterren niet meer bestaan zodra je ze ziet.", "Omdat een telescoop de tijd vertraagt.", "Omdat de aarde elke nacht verder van de sterren wegdraait."],
               0,
               "Ze ziet het sterrenstelsel zoals het 2,5 miljoen jaar geleden was, toen het licht vertrok."),
            volgorde(
                "Rangschik deze hemelstructuren van klein naar groot.",
                ["het zonnestelsel", "de Melkweg", "de Lokale Groep", "een supercluster"],
                "Ons zonnestelsel ligt in de Melkweg. Die hoort met de Andromedanevel bij de Lokale Groep, en die maakt deel uit van een supercluster."),
        ],
    ),

    # Casus: de zee bij Oostende
    casus(
        "Een gezin wil op het strand van Oostende een zandkasteel bouwen. Het is volle maan.",
        [
            mk("Wat veroorzaakt het verschil tussen hoog- en laagwater?",
               ["de wind die het water naar het strand blaast", "de aantrekking van de maan en de zon", "de draaiing van de aarde rond de zon", "het smelten van ijs op de polen"],
               1,
               "De getijden komen door de aantrekkingskracht van vooral de maan, en ook van de zon."),
            keuze(
                "Bij volle maan staan zon, aarde en maan op één lijn. Dan is het [[*springtij|doodtij]] en is het verschil tussen hoog- en laagwater [[*groter|kleiner]] dan gewoonlijk.",
                "Als zon en maan op één lijn trekken, versterken ze elkaar: springtij, bij volle en bij nieuwe maan."),
            tabel(
                "Klopt dit over de maan en verduisteringen?",
                [
                    ("Een zonsverduistering kan enkel bij nieuwe maan.", J),
                    ("Na volle maan volgt eerste kwartier.", F),
                    ("De maan draait van west naar oost rond de aarde.", J),
                ],
                "Bij een zonsverduistering staat de maan tussen zon en aarde: nieuwe maan. Na volle maan volgt laatste kwartier."),
        ],
    ),

    # Casus: zonnetijd
    casus(
        "Op de nulmeridiaan staat de zon om 12 uur zonnetijd op haar hoogste punt. Reken enkel met de zonnetijd, zonder tijdzones.",
        [
            inv("Hoe laat is het dan op 75° westerlengte? Geef enkel het uur als getal.",
                "7",
                "De aarde draait 15 graden per uur. 75 gedeeld door 15 is 5 uur. In het westen is het vroeger: 12 min 5 is 7 uur."),
            mk("In welke richting draait de aarde om haar as?",
               ["van oost naar west", "van west naar oost", "van noord naar zuid", "dat wisselt met de seizoenen"],
               1,
               "De aarde draait van west naar oost. Daarom komt de zon in het oosten op en is het in het oosten vroeger middag."),
            mk("Waar loopt de datumgrens ongeveer?",
               ["langs de nulmeridiaan door Greenwich", "langs de 180ste meridiaan", "langs de evenaar", "langs de keerkring van de Kreeft"],
               1,
               "De datumgrens ligt ongeveer aan de andere kant van de aarde, langs de 180ste meridiaan."),
        ],
    ),

    # Casus: een klimatogram
    casus(
        "Een klimatogram toont: de warmste maand is juli met 26 °C, de koudste januari met 10 °C. In juni, juli en augustus valt er bijna geen regen. In de winter valt er wel veel.",
        [
            mk("Welk klimaat beschrijft dit klimatogram?",
               ["een tropisch regenwoudklimaat", "een mediterraan klimaat", "een toendraklimaat", "een gematigd zeeklimaat zoals in Ukkel"],
               1,
               "Droge, warme zomers en zachte, natte winters: een mediterraan klimaat."),
            keuze(
                "De warmste maand valt in juli, dus deze plaats ligt op het [[*noordelijk|zuidelijk]] halfrond.",
                "Op het zuidelijk halfrond vallen de warmste maanden in december en januari."),
            tabel(
                "Klopt dit over klimaat en zeestromen?",
                [
                    ("De Noord-Atlantische Drift houdt onze winters zacht.", J),
                    ("De Humboldtstroom is een warme zeestroom.", F),
                    ("Bij opwelling komt koud, voedselrijk diepwater naar boven.", J),
                ],
                "De Humboldtstroom langs Zuid-Amerika is koud, met opwelling en veel vis."),
        ],
    ),

    # Casus: een groeiende stad
    casus(
        "Een stad groeit eerst snel door mensen van het platteland. Later trekken gezinnen naar de rand. Nog later verliest het hele stedelijk gebied inwoners. Vandaag komen er weer vooral jonge mensen in het centrum wonen.",
        [
            volgorde(
                "Zet deze fasen van verstedelijking in de volgorde van de tekst.",
                ["urbanisatie", "suburbanisatie", "desurbanisatie", "re-urbanisatie"],
                "Eerst trekken mensen naar de stad, dan naar de rand, dan verliest het stedelijk gebied inwoners en tot slot keert de beweging naar het centrum terug."),
            mk("Waarom is het in het centrum van die stad in de zomer warmer dan erbuiten?",
               ["door het stedelijk hitte-eiland", "door de Noord-Atlantische Drift", "door het gat in de ozonlaag", "door een warmtefront dat blijft hangen"],
               0,
               "Stenen en asfalt houden warmte vast, er is weinig groen en verkeer geeft warmte af. Zo is de stad warmer dan haar omgeving."),
            tabel(
                "Past deze keuze bij duurzaam ruimtegebruik?",
                [
                    ("Een leegstaand fabrieksgebouw ombouwen tot woningen", J),
                    ("Een nieuwe verkaveling op een akker ver van bus en trein", F),
                    ("Wonen, winkels en werk in één wijk mengen", J),
                    ("Ruimte voor water voorzien in een nieuwe wijk", J),
                ],
                "Omgevingsdenken gebruikt eerst wat er al is. Verweving brengt functies samen. Water bufferen helpt bij hevige buien. Bouwen ver van openbaar vervoer versnippert de open ruimte."),
        ],
    ),

    # Losse vragen door elkaar
    volgorde(
        "Zet de lagen van de atmosfeer van de grond naar de ruimte.",
        ["troposfeer", "stratosfeer", "mesosfeer", "thermosfeer", "exosfeer"],
        "Het weer speelt zich af in de troposfeer. In de stratosfeer ligt de ozonlaag."),
    koppel(
        "Tot welke groep hoort elk gesteente?",
        [
            ["basalt", "magmatisch"],
            ["conglomeraat", "sedimentair"],
            ["marmer", "metamorf"],
            ["zandsteen", "sedimentair"],
        ],
        ["fossiel", "mineraal"],
        "Basalt is gestolde lava. Conglomeraat en zandsteen zijn verkitte afzettingen. Marmer ontstaat uit kalksteen onder hoge druk en temperatuur."),
    sorteer(
        "Is dit fysische of chemische verwering?",
        ["Fysische verwering", "Chemische verwering"],
        [
            ["Water bevriest in een spleet en breekt de rots open.", "Fysische verwering"],
            ["Regenwater lost kalksteen op en vormt een grot.", "Chemische verwering"],
            ["Een rots in de woestijn barst door grote temperatuurverschillen.", "Fysische verwering"],
            ["IJzer in een gesteente roest en het gesteente brokkelt af.", "Chemische verwering"],
        ],
        "Bij fysische verwering breekt gesteente zonder dat de stof verandert. Bij chemische verwering verandert de stof zelf, zoals bij karst of roest."),
    mk("Je bekijkt een wand met horizontale gesteentelagen. Welke laag is de oudste?",
       ["de bovenste laag, want die zie je het eerst", "de dikste laag, want die had het meest tijd", "de onderste, als niets de lagen verstoorde", "de laag met de meeste fossielen erin"],
       2,
       "Volgens de wet van de superpositie ligt de oudste laag onderaan, zolang de lagen niet geplooid of omgekeerd zijn."),
    tabel(
        "Is dit mitigatie of adaptatie?",
        [
            ("Zonnepanelen plaatsen in plaats van een kolencentrale", "Mitigatie"),
            ("Dijken verhogen tegen de stijgende zeespiegel", "Adaptatie"),
            ("Meer bomen in de stad tegen hittegolven", "Adaptatie"),
            ("Minder vliegen om de uitstoot te beperken", "Mitigatie"),
        ],
        "Mitigatie pakt de oorzaak aan: minder uitstoot. Adaptatie past zich aan de gevolgen aan.",
        kolommen=["Mitigatie", "Adaptatie"]),
    mk("Zee-ijs smelt, en het donkere water eronder neemt meer zonlicht op. Wat voor terugkoppeling is dat?",
       ["een negatieve, want ze remt de opwarming af", "een positieve, want ze versterkt de opwarming", "geen, want zee-ijs heeft geen invloed op het klimaat", "een negatieve, want er komt meer water in de zee"],
       1,
       "Wit ijs weerkaatst veel zonlicht (een hoog albedo). Donker water slorpt het op en warmt verder op: een positieve terugkoppeling."),
    keuze(
        "Een rivier in de bergen schuurt een [[*V-dal|U-dal|vlakbodemdal]] uit. Een gletsjer maakt een [[*U-dal|V-dal|vlakbodemdal]].",
        "Een rivier snijdt diep in: V-vorm. Een gletsjer schuurt het hele dal breed uit: U-vorm."),
    mk("Waarom verklaren de Milanković-cycli de opwarming van de laatste honderd jaar niet?",
       ["Omdat ze over tienduizenden jaren werken.", "Omdat de baan van de aarde nooit verandert.", "Omdat ze enkel de maan beïnvloeden.", "Omdat ze alleen op het zuidelijk halfrond gelden."],
       0,
       "Schommelingen in de baan en de as van de aarde spelen over tienduizenden jaren. De huidige opwarming gaat veel sneller en komt door het versterkte broeikaseffect."),
    tabel(
        "Klopt dit over de seizoenen?",
        [
            ("We hebben seizoenen omdat de aardas scheef staat.", J),
            ("In onze zomer staat de aarde het dichtst bij de zon.", F),
            ("Op 21 maart staat de zon zenitaal boven de evenaar.", J),
        ],
        "De afstand tot de zon verklaart de seizoenen niet. Door de schuine as krijgt elk halfrond om beurten de zon hoger en langer."),
    sleep(
        "Boven de oceaan [[verdampt]] water. Stijgende lucht koelt af en de waterdamp [[condenseert]] tot wolken. Daarna valt er [[neerslag]] en het water stroomt via [[rivieren]] terug naar zee.",
        ["sublimeert", "verweert"],
        "Dat is de hydrologische cyclus, de kringloop van het water."),
    mk("Een beving van dezelfde magnitude treft twee landen. Waarom vallen er in het armste land vaak meer doden?",
       ["Omdat de beving daar een hogere magnitude heeft.", "Omdat gebouwen er zwakker zijn en hulp trager komt.", "Omdat arme landen altijd precies op een plaatgrens liggen.", "Omdat er in arme landen meer naschokken zijn."],
       1,
       "De magnitude hangt niet af van het land. Wel de bouwkwaliteit, de voorbereiding en hoe snel er hulp komt."),
    inv("Een vulkaan stoot zoveel as en zwavel uit dat het zonlicht minder doordringt. Wordt het daarna op aarde een jaar of langer warmer of kouder? Antwoord met één woord.",
        ["kouder", "koeler"],
        "Asdeeltjes en zwaveldruppeltjes hoog in de atmosfeer houden zonlicht tegen. De aarde koelt een jaar of langer wat af."),
    tabel(
        "Klopt dit over de zon?",
        [
            ("De energie van de zon komt vrij in haar kern.", J),
            ("Poollicht ontstaat als deeltjes van de zon op gas hoog in onze atmosfeer botsen.", J),
            ("Een protuberans is een donkere vlek op het zonsoppervlak.", F),
        ],
        "Een protuberans is een boog van gas boven het zonsoppervlak. Donkere vlekken zijn zonnevlekken."),
    keuze(
        "Bij een transforme plaatgrens schuiven twee platen [[*langs elkaar|uit elkaar|naar elkaar toe]]. Daar ontstaan vooral [[*aardbevingen|oceanische ruggen|hotspots]].",
        "Platen die langs elkaar schuiven, haken vast en schieten dan plots los: aardbevingen."),
    open_("Je gemeente wil een nieuwe woonwijk bouwen. Geef twee keuzes die volgens het duurzaam ruimtegebruik verstandig zijn, en leg uit waarom.",
          "Bouw op een plek die al in gebruik is, zoals een oude fabriekssite, zodat de open ruimte niet versnippert. Kies een plek dicht bij bus of trein en voorzie groen en ruimte voor water tegen hitte en wateroverlast.",
          "Denk aan omgevingsdenken, nabijheid van voorzieningen en vervoer, verweving en ruimte voor water en groen."),
]

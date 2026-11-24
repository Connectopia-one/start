"""Kenmerken van samenlevingen vergelijken — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = []

VRAGEN = [
    # --- vier soorten kenmerken
    sorteer(
        "Bij welk soort kenmerken hoort elk voorbeeld?",
        ["Politiek", "Economisch", "Sociaal", "Cultureel"],
        [
            ["kolonialisme", "Politiek"],
            ["mensenrechten", "Politiek"],
            ["de productiemethoden in een fabriek", "Economisch"],
            ["migratie en minderheden", "Sociaal"],
            ["emancipatie van een onderdrukte groep", "Sociaal"],
            ["wetenschappen en technologie", "Cultureel"],
            ["een mens- en wereldbeeld", "Cultureel"],
        ],
        "Kolonialisme en mensenrechten gaan over macht en bestuur. Migratie en emancipatie gaan over groepen. Wetenschap en wereldbeeld gaan over denken.",
    ),
    tabel(
        "Welke uitspraken over de vier soorten kenmerken kloppen?",
        [
            ("Een transportrevolutie kan ook de productie veranderen.", J),
            ("Een kenmerk hoort voor altijd bij één periode en verdwijnt nooit.", F),
            ("Industrialisering kan sociale gevolgen hebben, zoals een arbeidersklasse.", J),
            ("Wie politiek vergelijkt, mag de economie nooit vermelden.", F),
        ],
        "De vier soorten hangen samen. Een kenmerk kan in de ene periode aanwezig zijn en in de andere niet.",
    ),
    keuze(
        "Een consumptiemaatschappij is een [[*economisch|cultureel|politiek]] kenmerk. Propaganda is een [[*cultureel|economisch|sociaal]] kenmerk. Een gelaagde samenleving is een [[*sociaal|politiek|cultureel]] kenmerk.",
        "Kopen en verkopen is economisch, beïnvloeden van het denken cultureel, de verhouding tussen groepen sociaal.",
    ),
    # --- begrippen voor bestuur en economie
    koppel(
        "Welk begrip past bij elke beschrijving?",
        [
            ["De overheid wil ook het gezin, de jeugd en de vrije tijd beheersen.", "Totalitaire staat"],
            ["Eén man of één partij heeft alle macht, maar laat het privéleven grotendeels gerust.", "Dictatuur"],
            ["Ook de regering moet zich aan de wet houden.", "Rechtsstaat"],
            ["De meeste mensen werken in de diensten, niet in de fabriek.", "Postindustriële samenleving"],
        ],
        ["Kapitalisme"],
        "Een dictatuur houdt de macht vast. Een totalitaire staat wil daarnaast ook het denken beheersen.",
    ),
    mk(
        "Een verkozen meerderheid zet de rechters af en laat de oppositie opsluiten. Wat leer je daaruit?",
        [
            "Verkozen is niet vanzelf een rechtsstaat",
            "Elke verkiezing maakt een land totalitair",
            "Een rechtsstaat heeft geen verkiezingen nodig",
            "De oppositie hoort niet bij de democratie",
        ],
        0,
        "Wie zich boven de wet plaatst, haalt de bescherming van de minderheid weg, ook al is hij verkozen.",
    ),
    tabel(
        "Supranationaal of intergouvernementeel?",
        [
            ("De organisatie kan een beslissing opleggen aan een lidstaat die tegen stemde.", "Supranationaal"),
            ("Elke regering houdt haar vetorecht.", "Intergouvernementeel"),
            ("De regeringen beslissen samen, en wie niet wil, doet niet mee.", "Intergouvernementeel"),
            ("Een gemeenschappelijke regel geldt in alle lidstaten tegelijk.", "Supranationaal"),
        ],
        "Supranationaal staat boven de staten en kan opleggen. Intergouvernementeel is samenwerken tussen regeringen, met een veto.",
        kolommen=["Supranationaal", "Intergouvernementeel"],
    ),
    inv(
        "Een land raakt economisch steeds sterker verbonden met landen over de hele wereld. Welk begrip past daarbij? (één woord)",
        ["mondialisering", "globalisering"],
        "Mondialisering: economieën over de hele wereld raken meer met elkaar verbonden.",
    ),
    sleep(
        "Een propagandaminister zet de eigen natie tegenover de vijand en spreekt over [[wij]] en [[zij]]. Dat heet wij-zij-denken. Het hoort bij de [[culturele]] kenmerken, want het gaat over het wereldbeeld.",
        ["jullie", "economische", "ons"],
        "Wij-zij-denken plaatst de eigen groep tegenover een andere groep.",
    ),
    # --- hoe vergelijken
    mk(
        "Een leerling vergelijkt het bestuur van het Romeinse Rijk met de kunst van de Franse Revolutie. Wat loopt er mis?",
        [
            "Hij stelt niet dezelfde vraag aan beide samenlevingen",
            "Je mag geen samenlevingen uit twee periodes vergelijken",
            "Kunst hoort bij geen enkel soort kenmerk",
            "Hij had ook het weer moeten vergelijken",
        ],
        0,
        "Vergelijken doe je per domein en met dezelfde vraag voor beide.",
    ),
    koppel(
        "Welke vraag stel je voor elk domein als je twee samenlevingen vergelijkt?",
        [
            ["Wie beslist, en op welke grond?", "Politiek"],
            ["Waarvan leven de mensen?", "Economisch"],
            ["Welke groepen zijn er, en wie staat waar?", "Sociaal"],
            ["Wat gelooft men, en wat leert men?", "Cultureel"],
        ],
        ["Geografisch"],
        "Vier domeinen, vier vragen. Geografisch is geen maatschappelijk domein.",
    ),
    tabel(
        "Een leerling schrijft een vergelijking. Is elke zin in orde?",
        [
            ("In beide samenlevingen had één partij alle macht.", J),
            ("De ene samenleving was gewoon beter dan de andere.", F),
            ("In de ene samenleving werkte men vooral in de landbouw, in de andere in de fabriek.", J),
            ("De eerste had een parlement, want zo noemen wij een vergadering van wijzen.", F),
        ],
        "Gelijkenissen en verschillen benoemen is vergelijken. Een waardeoordeel of een begrip uit onze tijd opleggen is het niet.",
    ),
    mk(
        "Waarom spreek je beter niet over een parlement in het oude Egypte?",
        [
            "Het is een begrip uit een andere tijd",
            "Egypte had helemaal geen bestuur of farao",
            "Een parlement is een economisch begrip",
            "Over het oude Egypte zijn geen bronnen",
        ],
        0,
        "Een begrip uit onze tijd zegt meer over ons dan over Egypte. Gebruik de begrippen die bij die samenleving horen.",
    ),
    volgorde(
        "Zet de stappen van een goede vergelijking in de juiste volgorde.",
        [
            "Kies de vraag die je wil beantwoorden",
            "Kies de kenmerken die bij die vraag passen",
            "Zoek voor beide samenlevingen dezelfde kenmerken op",
            "Benoem gelijkenissen en verschillen",
            "Verklaar ze, zonder te oordelen wie beter was",
        ],
        "Je hoeft niet altijd alle vier de soorten kenmerken te gebruiken: kies wat bij je vraag past.",
    ),
    mk(
        "Je vergelijkt twee samenlevingen uit dezelfde periode, met een heel ander bestuur. Wat toont dat?",
        [
            "Eén tijd kan heel verschillende samenlevingen dragen",
            "Een van de twee besturen moet verkeerd beschreven zijn",
            "In één periode is er altijd maar één soort bestuur",
            "Vergelijken lukt alleen tussen twee verschillende periodes",
        ],
        0,
        "Dat is net de winst van een vergelijking binnen dezelfde periode.",
    ),
    # --- drie uitgewerkte vergelijkingen
    casus(
        "Je vergelijkt een standenmaatschappij met een klassenmaatschappij.",
        [
            mk(
                "Waarvan hangt je plaats af in een standenmaatschappij?",
                ["van je geboorte", "van je diploma's", "van je bezit en je loon", "van je stemgedrag"],
                0,
                "Adel, geestelijkheid of derde stand: dat lag vast bij je geboorte.",
            ),
            mk(
                "Waarvan hangt je plaats af in een klassenmaatschappij?",
                ["van je bezit", "van de stand waarin je vader zat", "van je geloof en je kerk", "van de streek waar je geboren bent"],
                0,
                "Fabriekseigenaar of arbeider: het bezit bepaalt de klasse.",
            ),
            mk(
                "Wat is een gelijkenis tussen beide?",
                ["Ze zijn allebei gelaagd", "In beide is iedereen voor de wet gelijk", "In beide beslist enkel de geboorte", "Ze bestaan nergens ter wereld nog"],
                0,
                "Beide samenlevingen zijn gelaagd, alleen de grond van de ongelijkheid verschilt.",
            ),
        ],
    ),
    tabel(
        "Slavernij in de vroegmoderne tijd en fabrieksarbeid in de 19de eeuw. Klopt elke uitspraak?",
        [
            ("Beide zijn vormen van zware uitbuiting.", J),
            ("Een slaaf is het bezit van iemand anders.", J),
            ("Een fabrieksarbeider was ook het bezit van de fabrikant.", F),
            ("De arbeidsovereenkomst was in de praktijk gelijkwaardig.", F),
        ],
        "Een arbeider sloot een overeenkomst die hij kon opzeggen. Ze was ongelijk, maar ze bestond.",
    ),
    mk(
        "Wat is een duidelijk verschil tussen het moderne imperialisme en dat uit de vroegmoderne tijd?",
        [
            "Nu bezette men ook het binnenland",
            "Vroeger veroverde men alles, nu enkel kleine eilanden",
            "Het moderne imperialisme ging alleen over godsdienst",
            "In de vroegmoderne tijd waren er nog geen schepen",
        ],
        0,
        "Het moderne imperialisme trok het binnenland in en bestuurde het.",
    ),
    tabel(
        "China onder Mao en China vandaag. Gelijkenis of verschil?",
        [
            ("Eén partij heeft de macht in handen.", "Gelijkenis"),
            ("De economie laat privébedrijven en winst toe.", "Verschil"),
            ("De staat controleert de pers.", "Gelijkenis"),
            ("China handelt met de hele wereld.", "Verschil"),
        ],
        "De economie veranderde grondig, maar de partij bleef aan de macht.",
        kolommen=["Gelijkenis", "Verschil"],
    ),
    # --- intercultureel contact
    sorteer(
        "Welke aard van contact beschrijft elke situatie?",
        ["Uitbuiting", "Cultuurvermenging", "Cultuurdominantie"],
        [
            ["Een koloniale firma laat dwangarbeiders rubber oogsten voor eigen winst.", "Uitbuiting"],
            ["Uit Afrikaanse ritmes en Europese instrumenten groeit een nieuwe muziekstijl.", "Cultuurvermenging"],
            ["Op school mag enkel de taal van de kolonisator gesproken worden.", "Cultuurdominantie"],
            ["Twee keukens groeien samen tot nieuwe gerechten.", "Cultuurvermenging"],
            ["Missionarissen verbieden de eigen godsdienst en leggen de hunne op.", "Cultuurdominantie"],
        ],
        "Uitbuiting draait om voordeel ten koste van de ander, vermenging om iets nieuws, dominantie om opleggen.",
    ),
    tabel(
        "Welke uitspraken over intercultureel contact kloppen?",
        [
            ("Ook onder dwang kan er cultuurvermenging ontstaan.", J),
            ("Wederzijdse impact betekent dat enkel de zwakste samenleving verandert.", F),
            ("Na een contact kunnen twee groepen een vertekend beeld van elkaar hebben.", J),
            ("Een vreedzaam contact kan nooit tot vermenging leiden.", F),
        ],
        "Bij wederzijdse impact veranderen beide samenlevingen. Vreedzame handel leidt net vaak tot vermenging.",
    ),
    keuze(
        "Na een contact zien twee groepen elkaar op een bepaalde manier: dat is de wederzijdse [[*perceptie|impact|dominantie]]. Veranderen beide samenlevingen erdoor, dan spreek je van wederzijdse [[*impact|perceptie|uitbuiting]].",
        "Perceptie is het beeld, impact is de verandering.",
    ),
    mk(
        "Europese reizigers beschrijven een Afrikaans volk als wild, en dat volk ziet de Europeanen als hebzuchtig. Welk begrip past?",
        [
            "Wederzijdse perceptie",
            "Cultuurvermenging",
            "Wederzijdse impact",
            "Een postindustriële samenleving",
        ],
        0,
        "Het gaat om het beeld dat beide groepen van elkaar hebben.",
    ),
    open_(
        "Een vriend zegt: \"De Europese samenlevingen van de 19de eeuw waren gewoon beter dan de Afrikaanse.\" Leg uit waarom dat geen vergelijking is, en hoe je het wel aanpakt.",
        "Wie zegt wie beter was, geeft een waardeoordeel, geen vergelijking. Je kiest een vraag, legt per domein dezelfde kenmerken naast elkaar, benoemt gelijkenissen en verschillen en verklaart ze. Je gebruikt de begrippen die bij elke samenleving horen.",
    ),
    mk(
        "Je wil een samenleving uit de oudheid vergelijken met een uit de moderne tijd. Welke kenmerken kies je het best?",
        [
            "De staatsvorm en de arbeidsorganisatie",
            "De consumptiemaatschappij en de mondialisering",
            "De postindustriële diensten en de internetcultuur",
            "Het aantal fabrieken en spoorwegen",
        ],
        0,
        "Kies kenmerken die in beide samenlevingen bestaan, anders steunt de vergelijking nergens op.",
    ),
    tabel(
        "Een totalitaire staat en een dictatuur. Klopt elke uitspraak?",
        [
            ("In beide heeft een kleine groep of één man de macht.", J),
            ("Een totalitaire staat wil ook het denken van de mensen sturen.", J),
            ("Een dictatuur is altijd totalitair.", F),
            ("Een totalitaire staat laat de jeugdbeweging vrij.", F),
        ],
        "Elke totalitaire staat is een dictatuur, maar niet elke dictatuur is totalitair.",
    ),
    inv(
        "Hoe noem je een samenleving waarin mensen met verschillende culturen samenleven? (één woord, zonder 'samenleving')",
        ["multicultureel", "multiculturele"],
        "Een multiculturele samenleving is een cultureel kenmerk.",
    ),
    sleep(
        "Bij een vergelijking benoem je zowel [[gelijkenissen]] als [[verschillen]], en je [[verklaart]] ze. Je [[beoordeelt]] niet welke samenleving de betere was.",
        ["meningen", "telt", "kiest"],
        "Drie regels houden een vergelijking eerlijk.",
    ),
    mk(
        "Welk kenmerk is in de ene periode aanwezig en in de andere niet?",
        [
            "Een consumptiemaatschappij",
            "Dat mensen in groepen samenleven en werken",
            "Dat er gezinnen bestaan",
            "Dat mensen eten nodig hebben",
        ],
        0,
        "Massaproductie en reclame horen bij de 20ste eeuw. De andere zijn er altijd.",
    ),
]

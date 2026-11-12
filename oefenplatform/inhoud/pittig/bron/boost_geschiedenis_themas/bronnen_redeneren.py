"""Redeneren met historische bronnen — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="bronvormen.svg", zelf=True,
         wat="Vier vakjes zonder naam: A muntstuk en scherf, B brief, C filmstrook, D microfoon met tekstballon.",
         vragen="koppelvraag: welke vorm van bron"),
    dict(bestand="stappenplan.svg", zelf=True,
         wat="Vier genummerde stappen met pijlen ertussen.",
         vragen="klikvraag: in welke stap interpreteer je"),
    dict(bestand="tapijt-van-bayeux.webp", zelf=False,
         wat="Een stuk uit het tapijt van Bayeux met de Slag bij Hastings (1066), bijvoorbeeld ruiters die aanvallen.",
         waar="Wikimedia Commons, zoek op 'Bayeux Tapestry Hastings' (publiek domein).",
         vragen="tabelvraag over betrouwbaarheid"),
]

VRAGEN = [
    mk(
        "Waarom stelt een historicus eerst een vraag en zoekt hij pas daarna bronnen?",
        [
            "Zonder vraag weet je niet waarnaar je in een bron moet kijken",
            "Archieven laten enkel wie een vraag heeft binnen in de leeszaal",
            "Bronnen veranderen van inhoud naargelang de vraag die je stelt",
            "Een vraag stellen gaat sneller dan bronnen zoeken in een archief",
        ],
        0,
        "Dezelfde kloosterrekening geeft een ander antwoord aan wie naar voeding vraagt dan aan wie naar arbeid vraagt.",
    ),
    tabel(
        "Wanneer is een historische vraag onderzoekbaar? Klopt elke uitspraak?",
        [
            ("Ze is afgebakend in tijd.", J),
            ("Ze is afgebakend in ruimte.", J),
            ("Ze is afgebakend binnen maatschappelijke domeinen.", J),
            ("Er bestaan bruikbare bronnen over.", J),
            ("Het antwoord past op één bladzijde.", F),
        ],
        "Tijd, ruimte, domein, het bestaan van bronnen en hun bruikbaarheid. De lengte van het antwoord speelt geen rol.",
    ),
    mk(
        "Wat ontbreekt vooral aan de vraag 'Welke rol speelden de Arabieren in de internationale handel?'",
        [
            "Een afbakening in tijd",
            "Een afbakening in ruimte",
            "Een afbakening binnen een maatschappelijk domein",
            "Een vraagwoord",
        ],
        0,
        "Over welke eeuw gaat het? Handel is al een economisch domein, en de ruimte staat er ook in.",
    ),
    sorteer(
        "Hoort dit bij de eerste stap van de bronnenanalyse of niet?",
        ["Stap 1", "Niet in stap 1"],
        [
            ["de bron situeren in tijd, ruimte en domein", "Stap 1"],
            ["bepalen welke soort bron het is", "Stap 1"],
            ["de maker contextualiseren", "Stap 1"],
            ["het doelpubliek bepalen", "Stap 1"],
            ["uitzoeken wat de bron vandaag waard is", "Niet in stap 1"],
        ],
        "In stap 1 verzamel je informatie over de context. Wat een bron vandaag als voorwerp waard is, hoort in geen enkele stap.",
    ),
    mk(
        "Je vindt een brief zonder datum en zonder bekende maker. Wat doe je?",
        [
            "Je noteert dat die gegevens ontbreken, de brief kan nog bruikbaar zijn",
            "Je gooit de brief meteen weg, want hij is waardeloos",
            "Je vult zelf een datum in die het best past bij je vraag",
            "Je doet alsof de brief van een bekende ooggetuige komt",
        ],
        0,
        "Ook vaststellen wat ontbreekt hoort bij stap 1. De bron kan bruikbaar blijven, als je weet dat dat gat er is.",
    ),
    sorteer(
        "Is dit een primaire of een secundaire bron over de Franse Revolutie?",
        ["Primair", "Secundair"],
        [
            ["een dagboek uit 1789", "Primair"],
            ["een pamflet dat in 1790 in Parijs verspreid werd", "Primair"],
            ["een geschiedenisboek over 1789", "Secundair"],
            ["een documentaire uit 2019", "Secundair"],
        ],
        "Primair komt uit de tijd zelf, secundair is er later over gemaakt.",
    ),
    tabel(
        "Klopt elke uitspraak over primaire en secundaire bronnen?",
        [
            ("Een primaire bron is automatisch beter.", F),
            ("Een boek van een historicus is automatisch betrouwbaarder dan een ooggetuigenverslag.", F),
            ("Je beoordeelt elke bron apart.", J),
        ],
        "Primair of secundair zegt nog niets over de kwaliteit. Je beoordeelt elke bron apart.",
    ),
    dict(
        **koppel(
            "Bekijk de vier vakjes. Welke vorm van bron staat er in elk vakje?",
            [["A", "materiële bron"], ["B", "geschreven bron"], ["C", "audiovisuele bron"], ["D", "mondelinge bron"]],
            ["denkbeeldige bron"],
            "Een muntstuk of scherf is materieel, een brief geschreven, een film audiovisueel en een getuigenis mondeling. Een denkbeeldige bron bestaat niet: een bron is altijd iets wat echt bewaard bleef.",
        ),
        afbeelding_url="/examenvormen/geschiedenis-boost/bronvormen.svg",
    ),
    mk(
        "Waarom zijn archeologische bronnen zo belangrijk voor periodes met weinig geschriften?",
        [
            "Ze vertellen over het dagelijkse leven van mensen die zelf niet schreven",
            "Ze zijn altijd ouder en dus betrouwbaarder dan een geschreven tekst",
            "Ze zijn de enige bronnen die een historicus mag aanraken",
            "Ze vertellen precies wat de mensen toen dachten en geloofden",
        ],
        0,
        "Wie niet schreef, liet toch voorwerpen, gebouwen en scherven na.",
    ),
    mk(
        "Wat is het verschil tussen een ooggetuige en een tijdgenoot?",
        [
            "Een ooggetuige zag het zelf, een tijdgenoot leefde enkel in dezelfde tijd",
            "Een tijdgenoot zag het zelf, een ooggetuige hoorde het van iemand anders",
            "Er is geen verschil, het zijn twee woorden voor hetzelfde",
            "Een ooggetuige schrijft altijd later dan een tijdgenoot",
        ],
        0,
        "Een tijdgenoot was er daarom nog niet bij.",
    ),
    tabel(
        "Wat wil je over de maker van een bron weten? Klopt elke uitspraak?",
        [
            ("wie het is: naam, beroep, afkomst", J),
            ("welke maatschappelijke positie hij innam", J),
            ("wie de opdracht gaf en met welk doel", J),
            ("hoeveel de bron vandaag op een veiling opbrengt", F),
        ],
        "Maker, positie en opdrachtgever bepalen mee wat er verteld en verzwegen wordt.",
    ),
    mk(
        "Met welke regels houd je rekening bij digitale bronnen?",
        [
            "Herkomst vermelden, auteursrecht respecteren en letten op privacy",
            "Enkel bronnen gebruiken die meer dan honderd jaar oud zijn",
            "Elke foto mag je vrij gebruiken zodra hij op het internet staat",
            "Digitale bronnen hoef je nooit te vermelden",
        ],
        0,
        "Ethische, sociale en legale regels: herkomst, auteursrecht en privacy bij recent materiaal.",
    ),
    inv(
        "Hoe noem je het dat wie iets vertelt, dat doet vanuit zijn eigen plaats, tijd en belangen? Antwoord met één woord.",
        ["standplaatsgebondenheid", "de standplaatsgebondenheid"],
        "Standplaatsgebondenheid. Een Spaanse en een Nederlandse bron over Alva zijn het schoolvoorbeeld.",
    ),
    mk(
        "Een bron is duidelijk vanuit één kant geschreven. Wat betekent dat voor jouw onderzoek?",
        [
            "Ze blijft nuttig: je leert er de blik van de maker uit kennen",
            "Ze is waardeloos en je laat ze best helemaal weg",
            "Ze is net de meest betrouwbare, want de maker was erbij betrokken",
            "Je mag ze enkel gebruiken als niemand anders erover schreef",
        ],
        0,
        "Een standpunt maakt een bron niet waardeloos. Integendeel, het vertelt je iets over de maker.",
    ),
    mk(
        "Twee bronnen spreken elkaar tegen. Wat doe je?",
        [
            "Je vergelijkt hun context, inhoud en betrouwbaarheid: het verschil is informatie",
            "Je maakt er zo snel mogelijk één verhaal van en laat de rest weg",
            "Je kiest de bron die het langst is, want die vertelt het meest",
            "Je besluit dat de gebeurtenis waarschijnlijk nooit heeft plaatsgevonden",
        ],
        0,
        "Juist dat verschil is informatie. Je zoekt gelijkenissen en verschillen.",
    ),
    mk(
        "Waarvan hangt de bruikbaarheid van een bron af?",
        [
            "Van jouw historische vraag",
            "Van de ouderdom van de bron",
            "Van het aantal bladzijden",
            "Van de bekendheid van de maker",
        ],
        0,
        "Een betrouwbare bron over een ander onderwerp is voor jouw vraag onbruikbaar.",
    ),
    tabel(
        "Je vraag is: wat aten de monniken van een klooster? Je vindt de rekeningen van het klooster, met aankopen van vis, brood en bier, maar zonder het vlees van de eigen boerderij. Klopt elke uitspraak?",
        [
            ("De rekeningen geven rechtstreekse informatie over je vraag.", J),
            ("Ze geven maar een gedeeltelijk antwoord.", J),
            ("Omdat ze maar een deel beantwoorden, zijn ze waardeloos.", F),
            ("Je legt ze best naast andere bronnen.", J),
        ],
        "Een bron die maar een deel beantwoordt, is nog niet waardeloos: je legt hem naast andere.",
    ),
    tabel(
        "Welke elementen uit de historische context kunnen de betrouwbaarheid van een bron beïnvloeden? Klopt elke uitspraak?",
        [
            ("De maker hing af van de persoon over wie hij schreef.", J),
            ("Er heerste censuur.", J),
            ("De bron werd pas lang na de feiten opgeschreven.", J),
            ("De tekst is erg lang.", F),
        ],
        "Afhankelijkheid, censuur en afstand in de tijd. De lengte van de tekst zegt niets.",
    ),
    koppel(
        "Welk begrip om een bron kritisch te lezen past bij elke beschrijving?",
        [
            ["uit één of enkele gevallen een besluit over het geheel trekken", "Veralgemening"],
            ["een vast, te eenvoudig beeld van een hele groep mensen", "Stereotype"],
            ["een mening die al vaststaat voor men de feiten bekeek", "Vooroordeel"],
        ],
        ["Anachronisme"],
        "Drie manieren waarop een bron de werkelijkheid te eenvoudig voorstelt.",
    ),
    mk(
        "Wat doe je in de laatste stap, als je een beargumenteerd antwoord formuleert?",
        [
            "Je kiest informatie uit de bronnen en staaft je antwoord met argumenten",
            "Je vat elke bron apart samen, de een na de ander",
            "Je schrijft je eigen mening op, zonder de bronnen te gebruiken",
            "Je kopieert de langste bron, want die is het volledigst",
        ],
        0,
        "Een samenvatting van elke bron is nog geen antwoord.",
    ),
    mk(
        "Waarom volstaat één bron niet voor een goed antwoord?",
        [
            "Elke bron is onvolledig en vanuit één plaats gemaakt, samen dekken ze elkaars blinde vlekken",
            "Eén bron is altijd vervalst",
            "Leerkrachten willen nu eenmaal altijd minstens drie bronnen",
            "Eén bron kan nooit over een gebeurtenis gaan",
        ],
        0,
        "Wat twee onafhankelijke bronnen allebei zeggen, staat sterker dan wat er in één staat.",
    ),
    met_prent(
        "tapijt-van-bayeux.webp",
        tabel(
            "Dit stuk uit een borduurwerk over de Slag bij Hastings (1066) werd gemaakt in opdracht van een halfbroer van de overwinnaar. Klopt elke uitspraak?",
            [
                ("De opdrachtgever hoorde bij de winnende kant.", J),
                ("Je legt het best naast andere bronnen over de slag.", J),
                ("Omdat het zo groot en zo mooi is, is het betrouwbaar.", F),
                ("Omdat het van één kant komt, is het waardeloos.", F),
            ],
            "Grootte of schoonheid zegt niets over betrouwbaarheid, en een standpunt maakt een bron niet waardeloos.",
        ),
    ),
    mk(
        "Je onderzoekt hoe bloedig de Slag bij Hastings verliep. Wat weegt het zwaarst?",
        [
            "De bronnen samen, na vergelijking en weging van hun betrouwbaarheid",
            "Een lofdicht van een tijdgenoot op de overwinnaar",
            "De oudste bron, wat die ook zegt",
            "Het verslag met de grootste aantallen doden",
        ],
        0,
        "Een lofdicht op de overwinnaar overdrijft met opzet.",
    ),
    mk(
        "Kan er op een historische vraag meer dan één goed antwoord bestaan?",
        [
            "Ja, zolang elk antwoord door de bronnen gedragen wordt",
            "Nee, er is altijd precies één juist antwoord",
            "Ja, elke mening is evenveel waard, ook zonder bronnen",
            "Nee, enkel historici mogen een antwoord geven",
        ],
        0,
        "Of Karel de Grote de vader van Europa is, hangt af van wat je onder Europa verstaat. Wat telt, is of je antwoord door de bronnen gedragen wordt.",
    ),
    koppel(
        "Welke historische redeneerwijze past bij elke beschrijving?",
        [
            ["een verband leggen tussen het verleden en vandaag", "Actualiseren"],
            ["iets begrijpen vanuit de tijd waarin het thuishoort", "Historisch contextualiseren"],
            ["aangeven welke mensen zelf iets in gang zetten", "Agency benoemen"],
            ["elke uitspraak staven met informatie uit een bron", "Bewijs gebruiken"],
        ],
        ["Periodiseren"],
        "Zonder bron is een uitspraak een mening. Het verleden overkwam mensen niet alleen, ze maakten het ook.",
    ),
    mk(
        "Columbus zocht een weg naar Azië en veroorzaakte de kolonisatie van Amerika. Wat voor gevolg is die kolonisatie?",
        ["Een onbedoeld gevolg", "Een bedoeld gevolg", "Een oorzaak", "Een continuïteit"],
        0,
        "Een onbedoeld gevolg nastreefde niemand, maar het kwam er toch.",
    ),
    mk(
        "Wat betekent meerdere perspectieven hanteren?",
        [
            "Verschillende standpunten kennen en tegen elkaar afwegen",
            "Elk standpunt is evenveel waard, dus je hoeft niet te kiezen",
            "Altijd het standpunt van de winnaar volgen",
            "Enkel standpunten van vandaag gebruiken",
        ],
        0,
        "Het betekent niet dat elk standpunt evenveel waard is, wel dat je ze kent en weegt.",
    ),
    klik(
        "Bekijk het stappenplan. In welke stap leg je uit hoe de context en het standpunt van de maker de inhoud bepalen? Klik op die stap.",
        "stappenplan.svg", [[51.0, 15.0, 22.0, 70.0]],
        "Dat is stap 3: daarin interpreteer je de bronnen.",
    ),
    casus(
        "Een kroniekschrijver die leefde van het geld van een graaf, schrijft over een opstand: 'Alle wevers zijn oproerig en lui. Ze kwamen in opstand omdat ze niet wilden werken.'",
        [
            mk(
                "Wat loopt er mis in de eerste zin? (meerdere antwoorden)",
                ["Hij trekt een besluit over alle wevers", "Hij plakt een vast etiket op een hele groep", "Hij plaatst iets in de verkeerde tijd", "Hij deelt de tijd verkeerd in perioden in"],
                [0, 1],
                "Het woordje 'alle' spreekt over de hele groep, en de luie, oproerige wever is een vast, te eenvoudig beeld. Over tijd zegt de zin niets.",
            ),
            open_(
                "Kan je deze bron toch gebruiken? Leg uit in twee of drie zinnen.",
                "Ja, maar niet om te weten waarom de wevers echt in opstand kwamen. De maker hing af van de graaf, dus de bron toont vooral hoe de kant van de graaf naar de opstand keek. Ik leg ze naast een bron van de wevers zelf.",
                "Een goed antwoord noemt de afhankelijkheid van de maker en zegt waarvoor de bron wél bruikbaar is.",
            ),
        ],
    ),
]

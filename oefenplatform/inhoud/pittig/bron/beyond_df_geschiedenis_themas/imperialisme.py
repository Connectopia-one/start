"""Modern imperialisme en de wedloop om Afrika — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="afrika-1914.webp", zelf=False,
         wat="Kaart van Afrika in 1914, met de koloniën per mogendheid in een eigen kleur.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="klikvragen op de zelfstandige staten en op Congo, tabel over de verdeling"),
]

VRAGEN = [
    # --- wat is het
    koppel(
        "Welke vorm van overheersing hoort bij elke situatie?",
        [
            ["Een Europees land bestuurt het gebied zelf, met eigen ambtenaren.", "Kolonie"],
            ["De plaatselijke vorst blijft, maar een Europese mogendheid beslist.", "Protectoraat"],
            ["Eén mogendheid beheerst de handel, maar bestuurt het land niet.", "Invloedssfeer"],
        ],
        ["Bufferstaat", "Republiek"],
        "Een kolonie wordt rechtstreeks bestuurd, een protectoraat houdt zijn vorst onder toezicht, in een invloedssfeer gaat het om de handel.",
    ),
    mk(
        "Wat was nieuw aan het imperialisme na 1870, vergeleken met de Europese aanwezigheid in Afrika daarvoor?",
        [
            "Hele gebieden werden bezet en door Europa bestuurd",
            "Europa had voor het eerst enkele kustposten voor de handel",
            "Afrikaanse vorsten bestuurden voor het eerst Europese steden",
            "Europese landen stopten met handel drijven in Afrika",
        ],
        0,
        "Vroeger ging het vooral om kustposten voor de handel. Rond 1870 had Europa het binnenland nog niet.",
    ),
    # --- oorzaken
    sorteer(
        "Welke oorzaak van het imperialisme hoort bij welke soort?",
        ["Economisch", "Politiek", "Ideologisch", "Techniek"],
        [
            ["rubber en palmolie voor de fabrieken", "Economisch"],
            ["markten voor fabrieksgoederen", "Economisch"],
            ["niet achterblijven bij de rivalen", "Politiek"],
            ["kolonies als bewijs van prestige", "Politiek"],
            ["de beschavingsmissie", "Ideologisch"],
            ["kinine tegen malaria", "Techniek"],
            ["repeteergeweren", "Techniek"],
        ],
        "Grondstoffen en markten zijn economisch, prestige politiek, de beschavingsmissie ideologisch. Kinine en geweren maakten het binnenland bereikbaar.",
    ),
    mk(
        "Welk verband is er tussen de tweede industriële revolutie en het modern imperialisme?",
        [
            "De nieuwe nijverheid had grondstoffen en markten nodig",
            "De tweede industriële revolutie begon in de kolonies zelf",
            "Door de industrie had Europa geen grondstoffen meer nodig",
            "De fabrieken in Europa werden allemaal naar Afrika verplaatst",
        ],
        0,
        "Rubber, erts en palmolie voor de fabriek, markten voor de producten en plaats om kapitaal te beleggen.",
    ),
    tabel(
        "Een leerling zegt: \"Het imperialisme ging alleen om geld.\" Welke gegevens nuanceren dat?",
        [
            ("Kolonies golden als bewijs van macht en prestige.", J),
            ("Soms kostten bestuur en leger meer dan ze opbrachten.", J),
            ("Het nationalisme voedde het imperialisme mee.", J),
            ("Europa had grondstoffen nodig voor zijn fabrieken.", F),
        ],
        "Grondstoffen passen net bij de economische uitleg. Prestige, nationalisme en het feit dat kolonies soms verlies maakten, tonen dat het om meer ging.",
    ),
    casus(
        "Lees de bron. Een Europese schrijver, 1890: \"Het is de plicht van de beschaafde volken om de andere volken te leiden. Wij brengen hen scholen, geloof en orde. Dat is een zware last, maar wij dragen haar.\"",
        [
            inv(
                "Hoe noem je de gedachte in deze bron?",
                ["de beschavingsmissie", "beschavingsmissie", "civilisatiemissie", "de civilisatiemissie"],
                "De beschavingsmissie: de gedachte dat Europa de plicht had andere volken te beschaven.",
            ),
            mk(
                "Hoe lees je deze bron het best als historicus?",
                [
                    "Als rechtvaardiging van de overheersing",
                    "Als betrouwbare beschrijving van de Afrikaanse volken",
                    "Als bewijs dat de kolonies vrijwillig ontstonden",
                    "Als verslag van een Afrikaanse vorst",
                ],
                0,
                "De bron zegt meer over het denken van de schrijver en zijn tijd dan over de volken waarover hij schrijft.",
            ),
            tabel(
                "Welke uitspraken over de missionarissen kloppen?",
                [
                    ("Ze richtten scholen en hospitalen op.", J),
                    ("Ze waren deel van het koloniale gezag.", J),
                    ("Soms waren zij de enigen die misbruiken aanklaagden.", J),
                    ("Ze stonden volledig buiten het koloniale bestuur.", F),
                ],
                "Missionarissen speelden een dubbele rol: deel van het gezag, maar soms ook aanklagers.",
            ),
        ],
    ),
    mk(
        "Waarom werd Egypte na 1869 zo belangrijk voor de mogendheden?",
        [
            "Het Suezkanaal verkortte de zeeweg naar Azië",
            "Egypte had de grootste rubberplantages van Afrika",
            "De Conferentie van Berlijn vond in Caïro plaats",
            "Egypte was het enige land met kinine tegen malaria",
        ],
        0,
        "De route naar Indië werd een belang dat met vloot en steunpunten verdedigd werd.",
    ),
    # --- Berlijn
    tabel(
        "Wat gebeurde er op de Conferentie van Berlijn van 1884-1885?",
        [
            ("Bismarck zat de conferentie voor.", J),
            ("De regel van de effectieve bezetting werd afgesproken.", J),
            ("Afrikaanse vorsten tekenden mee de afspraken.", F),
            ("Leopold II kreeg het Congobekken als persoonlijk bezit.", J),
        ],
        "Over Afrika werd beslist zonder één Afrikaan aan tafel.",
    ),
    mk(
        "Waarom versnelde de regel van de effectieve bezetting de verdeling van Afrika?",
        [
            "Wie een gebied wilde, moest er snel echt aanwezig zijn",
            "De regel verbood elke mogendheid om nog gebied te bezetten",
            "De regel gaf alle gebieden automatisch aan Groot-Brittannië",
            "De regel liet de Afrikanen zelf hun grenzen bepalen",
        ],
        0,
        "Een kaart claimen volstond niet meer. Elke mogendheid haastte zich om gebied echt te bezetten.",
    ),
    klik(
        "Bekijk de kaart van Afrika in 1914. Klik op een van de twee staten die zelfstandig bleven.",
        "afrika-1914.webp",
        [[71, 31.5, 18, 14.5], [16.5, 39.5, 5, 6]],
        "Ethiopië in het oosten en Liberia in het westen, de witte vlakken. Ethiopië versloeg in 1896 bij Adwa een Italiaans leger.",
    ),
    klik(
        "Klik op de kaart op het gebied dat in Berlijn aan Leopold II werd toegewezen.",
        "afrika-1914.webp",
        [[50.5, 44.5, 17.5, 22]],
        "Het Congobekken, in het midden van Afrika. In 1914 was het al een Belgische kolonie.",
    ),
    met_prent("afrika-1914.webp", tabel(
        "Bekijk de kaart opnieuw. Welke uitspraken kun je met de kaart en je kennis staven?",
        [
            ("Frankrijk en Groot-Brittannië hadden de grootste stukken.", J),
            ("Veel grenzen zijn rechte lijnen.", J),
            ("De grenzen volgden de woongebieden van de volken.", F),
            ("Duitsland had ook kolonies in Afrika.", J),
        ],
        "Rechte lijnen wijzen op grenzen die in Europa met een lat getrokken werden, niet door de volken zelf.",
    )),
    mk(
        "De Ethiopische overwinning bij Adwa in 1896 kwam in Europa aan als een schok. Waarom?",
        [
            "Europeanen hielden zich voor onoverwinnelijk",
            "Ethiopië was in 1896 een Italiaanse kolonie",
            "Italië had nog nooit een leger naar Afrika gestuurd",
            "De slag vond plaats in een Europese hoofdstad",
        ],
        0,
        "Een Afrikaans leger dat een Europees invasieleger verslaat, ondergroef het superioriteitsdenken.",
    ),
    tabel(
        "Welke vormen van verzet waren er in de kolonies?",
        [
            ("Gewapende opstanden tegen de koloniale legers", J),
            ("Weigeren om te werken of belasting te betalen", J),
            ("Een klacht bij de Verenigde Naties", F),
            ("Politieke eisen", J),
        ],
        "De Verenigde Naties bestonden nog niet. Verzet kon wel met wapens, met weigeren of met politieke eisen.",
    ),
    # --- gevolgen
    mk(
        "Waarom is een land dat vroeger een kolonie was, vaak kwetsbaar?",
        [
            "De economie draaide op de uitvoer van enkele grondstoffen",
            "Het had te veel eigen fabrieken die niets verkochten",
            "Het kreeg na 1960 helemaal nieuwe grenzen",
            "Het had nooit grondstoffen gehad",
        ],
        0,
        "Wie van enkele grondstoffen leeft, zit vast als de prijs daalt. Verwerken gebeurde in Europa, daar lag de winst.",
    ),
    tabel(
        "Welke gevolgen van het imperialisme merk je vandaag nog?",
        [
            ("Grenzen lopen dwars door gebieden van één volk.", J),
            ("Na 1960 zijn de grenzen niet opnieuw getekend.", J),
            ("Alle Afrikaanse landen hebben een grote eigen industrie.", F),
        ],
        "De lat op de kaart in Europa bepaalt nog altijd veel grenzen.",
    ),
    casus(
        "In 1897 bouwde men op de wereldtentoonstelling in Tervuren een 'Congolees dorp'. Er werden Congolezen naartoe gebracht, die bezoekers konden bekijken. Een aantal van hen stierf hier.",
        [
            mk(
                "Wat was de functie van zo'n menselijke tentoonstelling?",
                [
                    "De koloniale beeldvorming een vertoning maken",
                    "De Congolezen een vakantie in Europa aanbieden",
                    "Wetenschappelijk onderzoek naar de landbouw doen",
                    "Bewijzen dat Congo zelfstandig moest worden",
                ],
                0,
                "Het publiek kreeg een beeld van 'de ander' als vreemd en minder beschaafd. Zo werd de beschavingsmissie aanschouwelijk.",
            ),
            tabel(
                "Wat zegt deze gebeurtenis over de periode?",
                [
                    ("Het superioriteitsdenken was wijdverspreid.", J),
                    ("Mensen uit de kolonies werden als bezienswaardigheid behandeld.", J),
                    ("Alle Belgen waren tegen de kolonie.", F),
                ],
                "Het grote publiek kwam kijken. Dat toont hoe gewoon dat denken toen was.",
            ),
        ],
    ),
    tabel(
        "Welke botsingen tussen mogendheden kwamen uit de wedloop om Afrika?",
        [
            ("Frankrijk en Groot-Brittannië bij Fashoda in 1898", J),
            ("Duitsland en Frankrijk, tweemaal over Marokko", J),
            ("België en Ethiopië bij Adwa", F),
        ],
        "Bij Adwa vocht Italië tegen Ethiopië. Fashoda en Marokko maakten de mogendheden rivalen.",
    ),
    mk(
        "Hoe hangt het imperialisme samen met de Eerste Wereldoorlog?",
        [
            "De wedloop om gebied maakte de mogendheden rivalen",
            "De Afrikaanse staten verklaarden Europa de oorlog",
            "De Conferentie van Berlijn verplichtte tot oorlog",
            "Na 1914 werden alle kolonies meteen onafhankelijk",
        ],
        0,
        "Fashoda en Marokko voedden mee de bondgenootschappen van 1914.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["Het Suezkanaal opent", "De Conferentie van Berlijn", "Ethiopië verslaat Italië bij Adwa", "Fashoda", "Bijna heel Afrika is verdeeld"],
        "1869, 1884-1885, 1896, 1898 en 1914.",
    ),
    keuze(
        "Het imperialisme situeer je in het [[*economische|religieuze|artistieke]] domein, met grondstoffen en markten, en in het [[*politieke|culturele|sportieve]] domein, met macht en bestuur over gebied.",
        "Grondstoffen en markten zijn economisch, macht over gebied is politiek.",
    ),
    open_(
        "Leg uit waarom het imperialisme na 1870 zo snel ging. Gebruik minstens drie oorzaken uit verschillende domeinen.",
        "Economisch: de tweede industriële revolutie vroeg grondstoffen zoals rubber en erts, en markten voor fabrieksgoederen. Politiek: mogendheden wilden niet achterblijven, kolonies waren een teken van prestige, en het nationalisme voedde dat. Ideologisch: de beschavingsmissie rechtvaardigde de overheersing. Techniek: stoomschepen, kinine en repeteergeweren maakten het binnenland bereikbaar. In Berlijn versnelde de regel van de effectieve bezetting de verdeling.",
    ),
    open_(
        "Een kaart van Afrika uit 1914 toont rechte grenzen. Leg uit wat dat zegt over hoe die grenzen ontstonden, en welk gevolg dat vandaag heeft.",
        "De rechte grenzen werden in Europa met een lat op een kaart getrokken, zonder Afrikanen aan tafel en zonder te kijken naar wie er woonde. Daardoor lopen veel grenzen dwars door gebieden van één volk. Na 1960 werden ze niet opnieuw getekend, wat tot vandaag spanningen kan geven.",
    ),
    sleep(
        "In een [[protectoraat]] bleef het plaatselijke bestuur op papier bestaan, maar de beslissingen vielen elders. In een [[kolonie]] bestuurde de vreemde staat het gebied zelf.",
        ["invloedssfeer", "bufferstaat"],
        "Het verschil zit in wie bestuurt: de eigen vorst onder toezicht, of de vreemde staat zelf.",
    ),
    mk(
        "Wie verdiende meestal aan een kolonie, als de staat er zelf geld op verloor?",
        [
            "De bedrijven",
            "De Afrikaanse arbeiders op de plantages",
            "De missionarissen in de scholen",
            "De Verenigde Naties",
        ],
        0,
        "Bestuur en leger kostten de staat soms meer dan ze opbrachten. De winst ging naar bedrijven.",
    ),
    tabel(
        "Welke uitvindingen maakten het binnenland van Afrika voor Europeanen bereikbaar?",
        [
            ("Stoomschepen op de rivieren", J),
            ("Kinine tegen malaria", J),
            ("Repeteergeweren", J),
            ("Het vliegtuig", F),
        ],
        "Stoom, geneesmiddelen en geweren uit de tweede industriële revolutie. Vliegtuigen speelden toen nog geen rol.",
    ),
    keuze(
        "In 1914 was bijna heel Afrika in Europese handen, behalve [[*Ethiopië|Egypte|Congo]] en [[*Liberia|Marokko|Algerije]].",
        "Twee staten bleven zelfstandig. Ethiopië versloeg in 1896 zelfs een Italiaans leger.",
    ),
]

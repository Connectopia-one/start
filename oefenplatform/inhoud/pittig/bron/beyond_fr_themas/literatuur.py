"""Literaire teksten en literatuurbeleving — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez ce fragment de nouvelle.\n\n"
    "Il pleuvait depuis trois jours sur le petit port. Marc attendait devant la fenêtre, les mains dans les poches. "
    "Son père était parti en mer le lundi ; il devait rentrer le mercredi. On était vendredi. "
    "Soudain, une lumière apparut au loin. Marc courut vers le quai, le cœur battant comme un tambour. "
    "Le bateau entra lentement dans le port. Sur le pont, un homme leva la main."
)

TEKST2 = (
    "Lisez ce poème (de la rédaction).\n\n"
    "Le soir descend sur la ville,\n"
    "les rues deviennent silencieuses,\n"
    "et la lune, comme une lampe tranquille,\n"
    "veille sur les maisons heureuses.\n\n"
    "Demain, le bruit reviendra,\n"
    "les voitures, les cris, la foule,\n"
    "mais ce soir, personne ne voit\n"
    "le temps qui doucement s'écoule."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Waarom is Marc ongerust?",
                ["Zijn vader is twee dagen te laat", "Het regent al drie dagen", "Hij heeft zijn sleutels verloren", "Hij moet naar school in de regen"],
                0,
                "Il devait rentrer le mercredi. On était vendredi.",
            ),
            tabel(
                "Imparfait of passé simple in het fragment?",
                [
                    ("Il pleuvait", "Imparfait"),
                    ("Marc attendait", "Imparfait"),
                    ("une lumière apparut", "Passé simple"),
                    ("Marc courut", "Passé simple"),
                ],
                "Imparfait voor het decor, passé simple voor de gebeurtenissen.",
                kolommen=["Imparfait", "Passé simple"],
            ),
            mk(
                "Welk beeld gebruikt « le cœur battant comme un tambour »?",
                ["Een vergelijking", "Een opsomming", "Een vraag", "Een herhaling"],
                0,
                "Comme verraadt een vergelijking: het hart klopt hard.",
            ),
            keuze(
                "Het einde van het fragment is [[*open|helemaal duidelijk]]: we weten niet zeker wie de man is.",
                "Un homme leva la main: de lezer vult zelf in.",
            ),
            inv(
                "Hoeveel dagen regende het al? Schrijf het getal.",
                ["3", "drie"],
                "Depuis trois jours.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            inv(
                "Hoeveel strofen heeft dit gedicht? Schrijf het getal.",
                ["2", "twee"],
                "Twee groepjes van vier versregels.",
            ),
            mk(
                "Welke stijlfiguur staat in « la lune, comme une lampe tranquille »?",
                ["Een vergelijking", "Een opsomming", "Een retorische vraag", "Een overdrijving"],
                0,
                "Comme vergelijkt de maan met een lamp.",
            ),
            mk(
                "Wat staat tegenover elkaar in de twee strofen?",
                ["De stille avond en de drukke dag", "De warme zomer en de koude winter", "De grote stad en het rustige platteland", "Een oude man en een jonge vrouw"],
                0,
                "Ce soir is stil; demain komt het lawaai terug.",
            ),
            keuze(
                "« Les voitures, les cris, la foule » is een [[*opsomming|vergelijking]].",
                "Drie zelfstandige naamwoorden na elkaar.",
            ),
        ],
    ),
    koppel(
        "Koppel elk Frans literair woord aan zijn betekenis.",
        [
            ("une nouvelle", "een kortverhaal"),
            ("une strophe", "een groepje versregels"),
            ("le dénouement", "de ontknoping"),
            ("l'intrigue", "de verhaallijn"),
        ],
        ["de uitgeverij"],
        "La maison d'édition is de uitgeverij.",
    ),
    sorteer(
        "Positief of negatief oordeel over een boek?",
        ["Positief", "Negatief"],
        [
            ("captivant", "Positief"),
            ("décevant", "Negatief"),
            ("émouvant", "Positief"),
            ("ennuyeux", "Negatief"),
            ("passionnant", "Positief"),
        ],
        "Décevant is ontgoochelend, ennuyeux saai.",
    ),
    tabel(
        "Klopt deze betekenis in het Frans?",
        [
            ("un roman – een roman", J),
            ("la couverture – de kaft", J),
            ("un personnage – een persoonlijkheid", F),
            ("la BD – een strip", J),
        ],
        "Un personnage is een figuur in het verhaal.",
    ),
    mk(
        "« Je n'ai pas pu lâcher ce roman. » Wat zegt de lezer?",
        ["Het was meeslepend", "Het boek was te zwaar", "Hij heeft het niet uitgelezen", "Hij mocht het niet lenen"],
        0,
        "Lâcher: loslaten, wegleggen.",
    ),
    mk(
        "Hoe onderbouw je best « Ce personnage m'a touché »?",
        ["Met een citaat", "Door het hele boek na te vertellen", "Door de kaft te beschrijven", "Door de prijs te vermelden"],
        0,
        "Een mening wordt sterk met een passage uit de tekst.",
    ),
    mk(
        "Welke zin is literatuurbeleving en geen samenvatting?",
        ["Ce qui m'a frappé, c'est sa solitude.", "Le héros part en voyage en Italie.", "Le livre a deux cents pages en tout.", "L'histoire se passe en 1920 à Paris."],
        0,
        "Ce qui m'a frappé geeft je eigen reactie.",
    ),
    mk(
        "In welke tijd spreek je meestal over de inhoud van een boek?",
        ["Le présent", "Le passé simple", "Le futur", "Le plus-que-parfait"],
        0,
        "Dans ce roman, le héros découvre… De tegenwoordige tijd is gebruikelijk.",
    ),
    keuze(
        "« Une bonne nouvelle » betekent hier [[*goed nieuws|een goed kortverhaal]].",
        "Une nouvelle kan beide betekenen; het lidwoord en bonne wijzen op nieuws.",
    ),
    keuze(
        "Bij literatuurbeleving [[*mag|mag niet]] je zeggen dat je een boek niet goed vond, als je uitlegt waarom.",
        "Een onderbouwde negatieve mening is ook beleving.",
    ),
    keuze(
        "Een strip of een lied [[*kan|kan niet]] dienen om literatuurbeleving te tonen.",
        "Ook daar zitten beelden, personages en gevoelens in.",
    ),
    inv(
        "Vul aan met één Frans woord: « Le héros de l'histoire est le ___ principal. »",
        ["personnage"],
        "Le personnage principal.",
    ),
    inv(
        "Vul aan met één Frans woord: « Ce poème compte quatre ___ de quatre vers. » (strofen)",
        ["strophes"],
        "Une strophe.",
    ),
    mk(
        "Wat is « un résumé »?",
        ["Een korte samenvatting", "Een kritische recensie", "Een lijst met personages", "Een hoofdstuk uit het boek"],
        0,
        "Un résumé vertelt het verhaal kort na, zonder mening.",
    ),
    tabel(
        "Is dit een literaire tekst?",
        [
            ("une chanson de Stromae", J),
            ("une notice de médicament", F),
            ("une bande dessinée de Tintin", J),
            ("un horaire de train", F),
        ],
        "Een liedje en een strip zijn literair; een bijsluiter en een dienstregeling niet.",
    ),
    volgorde(
        "Zet de delen van een verhaal in de gewone volgorde.",
        ["la situation initiale", "l'élément perturbateur", "les péripéties", "le dénouement"],
        "Beginsituatie, verstoring, verwikkelingen, ontknoping.",
    ),
    mk(
        "« Il entra. Le feu brûlait encore dans la cheminée. » Wat doet de imparfait « brûlait »?",
        ["Het decor schetsen", "Een plotse actie geven", "Iets in de toekomst zeggen", "Een bevel geven"],
        0,
        "De imparfait beschrijft wat er al was.",
    ),
    tabel(
        "Klopt dit over een literaire tekst?",
        [
            ("Je moet elk woord kennen om de tekst te beleven.", F),
            ("Notities helpen je passages terug te vinden.", J),
            ("Je mag een Frans citaat in het Frans laten staan.", J),
        ],
        "Je kan een onbekend woord overslaan of afleiden.",
    ),
    mk(
        "« Ce roman est ennuyeux. » Wat vindt de lezer?",
        ["Saai", "Spannend", "Ontroerend", "Grappig"],
        0,
        "Ennuyeux: saai.",
    ),
    keuze(
        "« L'élément perturbateur » is het moment waarop [[*iets de rust verstoort|het verhaal eindigt]].",
        "Perturber: verstoren.",
    ),
    sleep(
        "In een gedicht heet een versregel un [[vers]], een groepje regels une [[strophe]], en de dichter un [[poète]].",
        ["roman", "chapitre"],
        "Le poème, le poète.",
    ),
    open_(
        "Schrijf in het Frans twee zinnen over een boek, strip of lied dat je raakte, en waarom.",
        "La chanson « Papaoutai » de Stromae m'a beaucoup touché. Elle parle d'un enfant qui cherche son père, et la musique joyeuse contraste avec ce thème triste.",
    ),
]

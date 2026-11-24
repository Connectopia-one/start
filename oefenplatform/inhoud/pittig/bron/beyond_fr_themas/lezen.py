"""Een Franse tekst analyseren — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le texte.\n\n"
    "(1) De plus en plus d'écoles belges interdisent le téléphone portable pendant les récréations. "
    "(2) Selon les directeurs, les élèves se parlent davantage et le harcèlement diminue. "
    "(3) Pourtant, une étude menée auprès de 900 élèves montre que leurs notes ne se sont pas améliorées. "
    "(4) Certains parents regrettent, en outre, de ne plus pouvoir joindre leurs enfants. "
    "(5) Les chercheurs concluent donc que l'interdiction n'est pas une solution miracle, même si elle rend les pauses plus conviviales."
)

TEKST2 = (
    "Lisez la lettre.\n\n"
    "Madame, Monsieur,\n"
    "Le 3 mars, j'ai acheté un aspirateur dans votre magasin de Namur. Au bout de deux semaines, il ne fonctionnait plus. "
    "Votre vendeur m'a dit que la réparation coûterait 60 euros. Or, l'appareil est encore sous garantie. "
    "Je vous demande donc de le réparer gratuitement ou de me rembourser. "
    "Faute de réponse dans les dix jours, je m'adresserai à une association de consommateurs.\n"
    "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.\n"
    "Julie Lambert"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Wat is de hoofdgedachte van deze tekst?",
                ["Een gsm-verbod is geen wondermiddel", "Een gsm-verbod geeft altijd betere punten", "Ouders willen allemaal een gsm-verbod", "Pesten verdwijnt helemaal door het verbod"],
                0,
                "Zin 5 vat samen, met het signaalwoord donc.",
            ),
            mk(
                "Welk verband legt « pourtant » in zin 3?",
                ["Een tegenstelling", "Een gevolg van zin 2", "Een voorbeeld bij zin 2", "Een opsomming"],
                0,
                "Pourtant: nochtans.",
            ),
            tabel(
                "Staat dit in de tekst over het gsm-verbod?",
                [
                    ("De punten van de leerlingen stegen.", F),
                    ("Volgens de directeurs praten leerlingen meer met elkaar.", J),
                    ("Sommige ouders kunnen hun kind niet meer bereiken.", J),
                    ("Alle Belgische scholen hebben een verbod.", F),
                ],
                "De plus en plus d'écoles is niet alle scholen.",
            ),
            keuze(
                "« En outre » in zin 4 betekent [[*bovendien|daarentegen]].",
                "En outre voegt iets toe.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Wat vraagt Julie aan de winkel?",
                ["Gratis herstellen of terugbetalen", "Een nieuw toestel met korting", "Een excuusbrief van de verkoper", "Een bon voor een volgende aankoop"],
                0,
                "Réparer gratuitement ou me rembourser.",
            ),
            keuze(
                "« Or » in « Or, l'appareil est encore sous garantie » betekent hier [[*welnu, maar|of]].",
                "Or leidt een tegenargument in; ou betekent of.",
            ),
            inv(
                "Binnen hoeveel dagen wil Julie een antwoord? Schrijf het getal.",
                ["10", "tien"],
                "Dans les dix jours.",
            ),
            mk(
                "Wat doet Julie als ze geen antwoord krijgt?",
                ["Klacht bij een consumentenvereniging", "Dan toch maar de 60 euro betalen", "Een ander toestel kopen in een andere winkel", "Naar de politie gaan met de factuur"],
                0,
                "Faute de réponse: bij gebrek aan antwoord.",
            ),
            mk(
                "Wat voor brief is dit?",
                ["Een formele klachtenbrief", "Een informele brief aan een vriendin", "Een advertentie van de winkel", "Een uitnodiging"],
                0,
                "Madame, Monsieur en Veuillez agréer … zijn vaste formules.",
            ),
        ],
    ),
    mk(
        "Lees: « Malgré la pluie, le match a eu lieu. » Wat gebeurde er met de wedstrijd?",
        ["Hij ging door", "Hij werd uitgesteld", "Hij werd stilgelegd", "Hij werd afgelast"],
        0,
        "Malgré: ondanks; avoir lieu: plaatsvinden.",
    ),
    mk(
        "Lees: « Les billets ne sont pas remboursables, sauf si le spectacle est annulé. » Wanneer krijg je je geld terug?",
        ["Als de voorstelling niet doorgaat", "Als je zelf niet kan komen", "Altijd binnen een termijn van veertien dagen", "In geen enkel geval"],
        0,
        "Sauf si: behalve als.",
    ),
    mk(
        "Lees: « Paul et sa sœur jouent du piano, mais celle-ci prend des cours. » Wie volgt les?",
        ["De zus", "Paul", "Allebei", "Geen van beiden"],
        0,
        "Celle-ci verwijst naar het laatst genoemde vrouwelijke woord: sa sœur.",
    ),
    mk(
        "Lees: « Il n'a guère changé depuis l'an dernier. » Wat zegt deze zin?",
        ["Hij is nauwelijks veranderd", "Hij is erg veranderd", "Hij is nooit veranderd geweest", "Hij is ziek geworden"],
        0,
        "Ne … guère: nauwelijks.",
    ),
    keuze(
        "Lees: « Il est inutile d'apporter à manger ; le repas est offert. » Eten meebrengen is [[*niet nodig|verboden]].",
        "Inutile: nutteloos, niet nodig.",
    ),
    keuze(
        "Lees: « Elle a dû rater son train. » De spreker is [[*vrij zeker|helemaal niet zeker]] dat ze haar trein miste.",
        "Devoir in de passé composé drukt hier een waarschijnlijke veronderstelling uit.",
    ),
    tabel(
        "Welk verband legt dit Franse signaalwoord?",
        [
            ("cependant", "Tegenstelling"),
            ("par conséquent", "Gevolg"),
            ("notamment", "Voorbeeld"),
            ("car", "Reden"),
        ],
        "Car: want; notamment: onder meer.",
        kolommen=["Tegenstelling", "Gevolg", "Voorbeeld", "Reden"],
    ),
    koppel(
        "Koppel elk Frans woord aan zijn betekenis.",
        [
            ("faute de", "bij gebrek aan"),
            ("en revanche", "daarentegen"),
            ("bien que", "hoewel"),
            ("afin de", "om te"),
        ],
        ["daarom"],
        "Zulke woordjes sturen hoe je de rest van de zin leest.",
    ),
    mk(
        "Lees: « Tous les élèves qui ont échoué n'avaient pas séché les cours. » Wat volgt hieruit?",
        ["Niet alle gebuisden spijbelden", "Alle gebuisde leerlingen hadden gespijbeld", "Geen enkele leerling was gebuisd", "Wie spijbelde, slaagde toch"],
        0,
        "Tous … ne … pas: niet allemaal.",
    ),
    mk(
        "Lees: « Le vol a été retardé. Cela nous a fait rater la correspondance. » Waar verwijst cela naar?",
        ["Naar de vertraging", "Naar de aansluitende vlucht", "Naar de drukke luchthaven", "Naar de andere passagiers"],
        0,
        "Cela vat de vorige zin samen.",
    ),
    inv(
        "Lees: « Les candidatures doivent nous parvenir au plus tard le 15 mai. » Wat is de laatste dag? Schrijf dag en maand, bv. 1/1.",
        ["15/5", "15 mei", "15/05", "15-5", "15 mai"],
        "Au plus tard: ten laatste.",
    ),
    mk(
        "Lees: « Ce produit est inoffensif. » Hoe leid je de betekenis van inoffensif af?",
        ["Uit in- plus offensif", "Uit in, dat binnen of erin betekent", "Uit het Engelse woord office", "Uit offrir, dat aanbieden betekent"],
        0,
        "In- maakt een woord ontkennend.",
    ),
    tabel(
        "Klopt dit over het lezen van een Franse tekst?",
        [
            ("De titel en de tussentitels helpen je het onderwerp te vinden.", J),
            ("Een voorbeeld is meestal de hoofdgedachte.", F),
            ("Donc kondigt vaak een besluit aan.", J),
            ("Je mag een antwoord geven dat de tekst tegenspreekt.", F),
        ],
        "Je antwoord komt altijd uit de tekst.",
    ),
    keuze(
        "Lees: « Seuls quelques spectateurs sont venus. » Er kwamen [[*maar weinig|heel veel]] toeschouwers.",
        "Seuls quelques: slechts enkele.",
    ),
    mk(
        "Lees: « Le port du casque est obligatoire. » Wat betekent dat?",
        ["Een helm is verplicht", "Een helm is verboden", "Een helm wordt aangeraden", "Een helm is te koop"],
        0,
        "Obligatoire: verplicht.",
    ),
    mk(
        "Lees: « Je ne mange jamais de viande, sauf à Noël. » Wanneer eet de spreker vlees?",
        ["Alleen met Kerstmis", "Elke dag een beetje", "Nooit, ook niet met Kerstmis", "Enkel in het weekend"],
        0,
        "Sauf: behalve.",
    ),
    keuze(
        "Lees: « Il faut réserver à l'avance. » Reserveren is [[*nodig|verboden]].",
        "Il faut: het is nodig.",
    ),
    inv(
        "Lees: « Le magasin ouvre ses portes à 9 h et les ferme à 18 h. » Hoeveel uur is de winkel open? Schrijf het getal.",
        ["9", "negen"],
        "Van 9 tot 18 uur.",
    ),
    volgorde(
        "Zet de signaalwoorden in de volgorde waarin ze in een stappenplan staan.",
        ["d'abord", "ensuite", "puis", "enfin"],
        "Eerst, daarna, dan, ten slotte.",
    ),
    sleep(
        "Het woord [[pourtant]] kondigt een tegenstelling aan, [[donc]] een gevolg en [[car]] een reden.",
        ["ainsi", "malgré"],
        "Signaalwoorden dragen de samenhang.",
    ),
    open_(
        "Lees: « Bien que le tourisme rapporte de l'argent à l'île, il menace ses réserves d'eau. » Leg in het Nederlands uit wat de schrijver zegt.",
        "Toerisme brengt geld op voor het eiland, maar het bedreigt ook de watervoorraad. Bien que geeft eerst het voordeel toe en zet daar het nadeel tegenover.",
    ),
]

"""Schrijven en schriftelijke interactie — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le mail.\n\n"
    "Objet : demande d'informations – stage d'été\n\n"
    "Madame,\n"
    "Suite à votre annonce sur le site de l'office du tourisme, je me permets de vous écrire. "
    "J'ai 18 ans et je cherche un stage d'été de quatre semaines. Pourriez-vous m'indiquer les dates exactes et les horaires ? "
    "Je voudrais aussi savoir si le logement est compris.\n"
    "Je vous remercie d'avance de votre réponse.\n"
    "Veuillez agréer, Madame, mes salutations distinguées.\n"
    "Lucas Peeters"
)

TEKST2 = (
    "Lisez le message d'un client et la réponse.\n\n"
    "Client : « Ma commande n° 4521 n'est toujours pas arrivée. C'est inadmissible ! »\n"
    "Réponse : « Bonjour Monsieur, je comprends votre mécontentement et je vous prie de nous excuser pour ce retard. "
    "Votre colis a été envoyé hier ; vous le recevrez au plus tard jeudi. Je reste à votre disposition pour toute question. Cordialement, Sarah »"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Vraagt Lucas dit in zijn mail?",
                [
                    ("de juiste data van de stage", J),
                    ("de werkuren", J),
                    ("of er een loon is", F),
                    ("of het verblijf inbegrepen is", J),
                ],
                "Dates, horaires, logement compris.",
            ),
            mk(
                "Waarom begint de mail met « Suite à votre annonce »?",
                ["Hij zegt meteen waarom hij schrijft", "Hij stelt zich eerst uitgebreid voor", "Hij klaagt over de inhoud van de advertentie", "Hij sluit de mail daarmee al meteen af"],
                0,
                "Suite à: naar aanleiding van.",
            ),
            keuze(
                "Het woord « Objet » staat boven [[*de onderwerpregel|de handtekening]].",
                "Objet: het onderwerp van de mail.",
            ),
            mk(
                "Welke zin uit de mail is een conditionnel de politesse?",
                ["Je voudrais aussi savoir…", "J'ai 18 ans.", "Je cherche un stage d'été.", "Je vous remercie d'avance."],
                0,
                "Voudrais is hoffelijker dan veux.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Hoe begint Sarah haar antwoord op de boze klant?",
                ["Met begrip en excuses", "Met een tegenaanval", "Met een korting van 50 %", "Met een vraag naar zijn adres"],
                0,
                "Je comprends votre mécontentement et je vous prie de nous excuser.",
            ),
            inv(
                "Wanneer krijgt de klant zijn pakje ten laatste? Antwoord in het Frans.",
                ["jeudi", "Jeudi"],
                "Au plus tard jeudi.",
            ),
            keuze(
                "Sarah [[*beantwoordt|negeert]] de vraag van de klant: ze zegt waar het pakje is.",
                "Bij interactie speel je in op wat de ander schreef.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van het schrijfproces in de juiste volgorde.",
        ["het doel en de lezer bepalen", "een schrijfplan met kernwoorden maken", "de tekst in alinea's schrijven", "de tekst nalezen"],
        "Plannen, schrijven, nalezen.",
    ),
    sorteer(
        "Past dit in een formele mail of in een berichtje aan een vriend?",
        ["Formele mail", "Berichtje aan een vriend"],
        [
            ("Je vous écris au sujet de…", "Formele mail"),
            ("Coucou, t'es dispo samedi ?", "Berichtje aan een vriend"),
            ("Je vous remercie d'avance.", "Formele mail"),
            ("À plus !", "Berichtje aan een vriend"),
            ("Dans l'attente de votre réponse,", "Formele mail"),
        ],
        "Kies één register en houd het aan.",
    ),
    koppel(
        "Koppel de Franse formule aan haar functie in een mail.",
        [
            ("Suite à votre message,", "openen met de aanleiding"),
            ("Pour conclure,", "het slot aankondigen"),
            ("Je vous prie de m'excuser.", "excuses aanbieden"),
            ("Pourriez-vous préciser ?", "om uitleg vragen"),
        ],
        ["een vriend groeten"],
        "Elke formule heeft een vaste plaats in de mail.",
    ),
    mk(
        "Welke onderwerpregel is het duidelijkst?",
        ["Objet : cours de tennis", "Objet : une petite question pour vous", "Objet : bonjour et bonne journée", "Objet : urgent, à lire tout de suite !!!"],
        0,
        "De lezer moet meteen weten waarover het gaat.",
    ),
    mk(
        "Je schrijft aan een onbekende mevrouw. Hoe begin je?",
        ["Madame,", "Salut Madame !", "Coucou,", "Chère amie,"],
        0,
        "Madame, met een komma, dan een nieuwe regel.",
    ),
    mk(
        "Je kent het woord « aspirateur » niet. Wat doe je best?",
        ["Het omschrijven", "De zin weglaten", "Het Nederlandse woord schrijven", "Een ander onderwerp kiezen"],
        0,
        "Bv. la machine qui nettoie le sol.",
    ),
    mk(
        "Welke slotzin past onder een vraag aan een bedrijf?",
        ["Je vous remercie d'avance.", "Gros bisous et à bientôt !", "Salut, à plus tard, mon pote !", "Réponds-moi vite, hein, sinon tant pis !"],
        0,
        "Bedanken voor een antwoord dat nog moet komen.",
    ),
    tabel(
        "Juist of fout in een Franse brief?",
        [
            ("Na de aanhef komt een komma en dan een nieuwe regel.", J),
            ("Je begint met een lange inleiding over jezelf.", F),
            ("Elke alinea draagt één gedachte.", J),
            ("Je wisselt tu en vous af om afwisseling te brengen.", F),
        ],
        "De lezer wil snel weten waarom je schrijft; kies één aanspreekvorm.",
    ),
    tabel(
        "Tu-vorm of vous-vorm?",
        [
            ("Je t'écris pour…", "tu"),
            ("Je vous écris pour…", "vous"),
            ("ton adresse", "tu"),
            ("votre adresse", "vous"),
        ],
        "Ton hoort bij tu, votre bij vous.",
        kolommen=["tu", "vous"],
    ),
    keuze(
        "« Pourriez-vous préciser ? » gebruik je als je iets [[*niet goed begreep|helemaal begreep]].",
        "Préciser: verduidelijken.",
    ),
    keuze(
        "« Je reste à votre disposition » betekent dat je [[*beschikbaar blijft voor vragen|het gesprek afsluit]].",
        "Een vriendelijke slotzin in een zakelijke mail.",
    ),
    keuze(
        "Een spellingcontrole ziet de fout in « ma mère » voor « ma mer » [[*niet altijd|altijd]].",
        "Mer is ook een bestaand woord.",
    ),
    inv(
        "Vul aan met één Frans woord: « Je vous ___ d'avance de votre aide. »",
        ["remercie"],
        "Je vous remercie d'avance.",
    ),
    inv(
        "Vul aan met één Frans woord: « Pour ___, je voudrais vous rappeler la date limite. » (om af te sluiten)",
        ["conclure", "terminer", "finir"],
        "Pour conclure, pour terminer.",
    ),
    mk(
        "Welke titel past boven een blog over een uitwisseling met Québec?",
        ["Mes deux semaines à Québec", "Qu'est-ce que la Francophonie ?", "Recette de la poutine", "Horaires des vols"],
        0,
        "De titel zegt kort waarover het blog gaat.",
    ),
    mk(
        "« Je vous serais reconnaissant de me répondre avant vendredi. » Wat doet deze zin?",
        ["Hoffelijk een termijn vragen", "Bedanken voor een gekregen antwoord", "Een officiële klacht indienen", "Een gemaakte afspraak afzeggen"],
        0,
        "Reconnaissant: dankbaar.",
    ),
    mk(
        "Waarop let je NIET bij het nalezen van een formele mail?",
        ["Of hij lang genoeg oogt", "Of de toon gepast is", "Of de boodschap helder is", "Of tu en vous juist zijn"],
        0,
        "Lengte is geen doel; helder en gepast wel.",
    ),
    sleep(
        "Een formele mail begint met [[Madame]], en eindigt met [[Cordialement]]. In de onderwerpregel staat [[Objet]].",
        ["Salut", "Bisous"],
        "Aanhef, slot en onderwerp horen bij de lay-out.",
    ),
    open_(
        "Schrijf in het Frans een korte formele mail (3 à 4 zinnen) aan een camping: je wil weten of er nog plaats is van 10 tot 17 juli voor twee tenten.",
        "Objet : réservation juillet. Madame, Monsieur, je me permets de vous écrire pour savoir s'il vous reste de la place du 10 au 17 juillet pour deux tentes. Pourriez-vous aussi m'indiquer le prix ? Je vous remercie d'avance. Veuillez agréer mes salutations distinguées.",
    ),
    mk(
        "Je antwoordt een vriendin die schreef dat ze ziek is. Welke zin speelt in op haar bericht?",
        ["J'espère que tu vas vite te sentir mieux !", "Voici les horaires du cinéma de samedi.", "Je vous prie d'agréer mes salutations.", "Mon chien s'appelle Max et il a trois ans."],
        0,
        "Bij interactie reageer je eerst op wat de ander schreef.",
    ),
    keuze(
        "Een nieuwe alinea begin je best bij [[*een nieuwe gedachte|elke nieuwe zin]].",
        "Eén alinea, één gedachte.",
    ),
    tabel(
        "Hoort deze zin in een klachtenmail aan een winkel?",
        [
            ("J'ai acheté un casque le 3 mars.", J),
            ("Il ne fonctionne plus depuis une semaine.", J),
            ("T'es nul, mec !", F),
            ("Je souhaiterais un échange ou un remboursement.", J),
        ],
        "Feiten, probleem en een beleefde vraag; geen scheldwoorden.",
    ),
    inv(
        "Vul aan met één Frans woord: « Je vous ___ de m'excuser pour ce retard. » (hoffelijke vraag)",
        ["prie"],
        "Je vous prie de m'excuser.",
    ),
]

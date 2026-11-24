"""Woordvelden school, werk, reizen en samenleving — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez l'article.\n\n"
    "Selon un sondage publié lundi, six jeunes sur dix trouvent un emploi dans les six mois après leurs études. "
    "Pourtant, le taux de chômage des moins de 25 ans reste élevé. "
    "Beaucoup d'étudiants font un stage pour se préparer à l'entretien d'embauche. "
    "Avec la hausse des prix, leur pouvoir d'achat est en baisse : un sur trois travaille le week-end pour payer son loyer."
)

TEKST2 = (
    "Lisez le message de la SNCF.\n\n"
    "« En raison d'une panne de signalisation, le TGV de 14 h 12 pour Marseille partira avec 40 minutes de retard, voie 7. "
    "Les voyageurs avec un aller-retour peuvent demander un remboursement au guichet. "
    "Sur l'autoroute A7, de nombreux bouchons sont signalés. Nous vous remercions de votre patience. »"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in het artikel?",
                [
                    ("De cijfers komen uit een opiniepeiling.", J),
                    ("Zes op tien jongeren vinden snel werk.", J),
                    ("De werkloosheid bij jongeren is laag.", F),
                    ("De koopkracht van studenten daalt.", J),
                ],
                "Un sondage; six sur dix; le taux de chômage reste élevé; pouvoir d'achat en baisse.",
            ),
            mk(
                "Waarom werkt één op drie studenten in het weekend?",
                ["om de huur te betalen", "om een stage te vinden", "omdat ze hun jaar overdoen", "omdat de school dicht is"],
                0,
                "Pour payer son loyer.",
            ),
            keuze(
                "« Un entretien d'embauche » is een [[*sollicitatiegesprek|ontslag]].",
                "Embaucher: aanwerven.",
            ),
            inv(
                "Welk Frans woord uit de tekst betekent stijging?",
                ["hausse", "la hausse", "une hausse"],
                "La hausse des prix.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Waarom vertrekt de TGV later?",
                ["door een defect aan de seinen", "door een betoging op het perron", "door files op de autosnelweg", "door te veel reizigers"],
                0,
                "Une panne de signalisation.",
            ),
            tabel(
                "Klopt dit volgens het bericht?",
                [
                    ("De trein vertrekt van spoor 7.", J),
                    ("De vertraging is veertig minuten.", J),
                    ("Wie een heen-en-terugticket heeft, kan geld terugvragen.", J),
                    ("Op de A7 rijdt het verkeer vlot.", F),
                ],
                "Voie 7, 40 minutes de retard, remboursement au guichet, de nombreux bouchons.",
            ),
            keuze(
                "Het geld terugvragen doe je aan [[*het loket|het perron]].",
                "Au guichet.",
            ),
        ],
    ),
    sorteer(
        "Hoort dit woord bij school of bij werk?",
        ["School", "Werk"],
        [
            ("un bulletin", "School"),
            ("une récréation", "School"),
            ("une offre d'emploi", "Werk"),
            ("le salaire", "Werk"),
            ("redoubler", "School"),
            ("un cadre", "Werk"),
        ],
        "Twee woordvelden uit krantentaal.",
    ),
    koppel(
        "Koppel het Franse woord uit een krantenartikel aan de betekenis.",
        [
            ("une manifestation", "een betoging"),
            ("un sondage", "een opiniepeiling"),
            ("une élection", "een verkiezing"),
            ("une enquête", "een onderzoek"),
        ],
        ["een file"],
        "Politiek en maatschappij.",
    ),
    tabel(
        "Gaat het woord over het milieu of over technologie?",
        [
            ("les déchets", "milieu"),
            ("télécharger", "technologie"),
            ("le réchauffement", "milieu"),
            ("un ordinateur portable", "technologie"),
        ],
        "Twee woordvelden uit deel 2.",
        kolommen=["milieu", "technologie"],
    ),
    volgorde(
        "Zet de Franse scholen in de volgorde waarin een leerling ze doorloopt.",
        ["l'école primaire", "le collège", "le lycée", "l'université"],
        "Lager, eerste jaren secundair, laatste jaren secundair, hoger onderwijs.",
    ),
    mk(
        "« Il a passé son examen hier, mais il ne connaît pas encore le résultat. » Wat weten we?",
        ["Hij heeft het examen afgelegd", "Hij is geslaagd voor het examen", "Hij is gebuisd voor het examen", "Hij heeft het examen uitgesteld"],
        0,
        "Passer un examen: afleggen; réussir: slagen.",
    ),
    mk(
        "Wat staat er op je loonbrief als « salaire brut »?",
        ["het loon vóór afhoudingen", "het loon dat op je rekening komt", "de belasting die je betaalt", "de premie aan het eind van het jaar"],
        0,
        "Brut: vóór afhoudingen; net: wat overblijft.",
    ),
    mk(
        "Welke zin gaat over het milieu?",
        ["Il faut lutter contre le gaspillage.", "Le TGV pour Lyon part de la voie 3, quai B.", "J'ai un entretien d'embauche lundi matin à 9 h.", "Le taux de chômage des jeunes est en baisse."],
        0,
        "Le gaspillage alimentaire: voedselverspilling.",
    ),
    mk(
        "Een journalist schrijft « l'ours polaire est une espèce menacée ». Wat bedoelt hij?",
        ["Het dier kan uitsterven", "Het dier is gevaarlijk voor mensen", "Het dier is een huisdier geworden", "Het dier leeft enkel in dierentuinen"],
        0,
        "Menacé: bedreigd.",
    ),
    mk(
        "« Ma voiture est tombée en panne. » Wat is er gebeurd?",
        ["De auto doet het niet meer", "De auto is gisteren gestolen", "De auto staat vast in de file", "De auto is pas nieuw gekocht"],
        0,
        "Être ou tomber en panne: stuk zijn.",
    ),
    keuze(
        "« Le développement durable » betekent [[*duurzame ontwikkeling|langdurige ontwikkeling]].",
        "Durable: duurzaam.",
    ),
    keuze(
        "In Frankrijk zijn « les soldes » [[*vastgelegde koopjesperiodes|gratis producten]].",
        "Twee keer per jaar, op vaste data.",
    ),
    keuze(
        "Een « aller simple » is een [[*enkele reis|heen-en-terugticket]].",
        "Aller simple tegenover aller-retour.",
    ),
    keuze(
        "Wie « au chômage » is, [[*heeft geen werk|is met vakantie]].",
        "Le chômage: de werkloosheid.",
    ),
    tabel(
        "Juist of fout over deze woorden uit krantentaal?",
        [
            ("Un réseau is een netwerk.", J),
            ("Une baisse is een stijging.", F),
            ("Les réseaux sociaux zijn sociale media.", J),
            ("Une facture is een rekening.", J),
        ],
        "Une baisse is een daling.",
    ),
    inv(
        "Vul aan met één Frans woord: « Avant de monter dans le train, il faut ___ son billet. » (afstempelen)",
        ["composter"],
        "Composter son billet.",
    ),
    inv(
        "Vul aan met één Frans woord: « Il a raté son année ; il doit ___. » (een jaar overdoen)",
        ["redoubler"],
        "Redoubler.",
    ),
    inv(
        "Vul aan met één Frans woord: « Nous trions nos ___ pour protéger l'environnement. » (afval)",
        ["déchets"],
        "Les déchets.",
    ),
    sleep(
        "Je cherche du travail. J'ai lu une [[offre d'emploi]] et j'envoie mon [[curriculum vitae]]. La semaine prochaine, j'ai un [[entretien d'embauche]].",
        ["bouchon", "sondage"],
        "Woorden bij het zoeken van werk.",
    ),
    open_(
        "Schrijf in het Frans twee zinnen voor een schoolkrant: wat jouw school doet tegen afval of verspilling.",
        "Dans notre école, nous trions les déchets dans trois poubelles. À la cantine, on lutte contre le gaspillage alimentaire avec des portions plus petites.",
    ),
    mk(
        "Wat betekent « une matière » op een Frans rapport?",
        ["een schoolvak", "een examenpunt", "een speeltijd", "een klasgroep"],
        0,
        "Une matière: les mathématiques, le français…",
    ),
    mk(
        "Wat is « le quai » in een station?",
        ["het perron", "het loket", "het treinticket", "de vertraging"],
        0,
        "Le quai: waar je wacht; la voie: het spoor.",
    ),
    keuze(
        "« Un bouchon » in een verkeersbericht is een [[*file|kurk]].",
        "In het verkeer betekent un bouchon een file.",
    ),
    tabel(
        "Juist of fout bij een treinreis?",
        [
            ("Le guichet is het loket.", J),
            ("La voie is het spoor.", J),
            ("Un billet is een rekening.", F),
        ],
        "Un billet: een ticket.",
    ),
]

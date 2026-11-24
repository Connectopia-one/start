"""Zinsbouw, indirecte rede en passieve zin — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez l'article.\n\n"
    "Le nouveau pont de Namur a été inauguré hier par la ministre. Il a été construit en deux ans. "
    "Pourtant, tout le monde n'est pas content : des habitants se demandent si le bruit va augmenter. "
    "Un voisin a déclaré qu'il n'avait jamais été consulté. "
    "La ministre a répondu que des murs antibruit seraient installés le mois suivant. "
    "Les travaux ne sont donc pas encore terminés."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat de zin uit het artikel in de actieve of de passieve vorm?",
                [
                    ("Le pont a été inauguré par la ministre.", "passief"),
                    ("Il a été construit en deux ans.", "passief"),
                    ("Un voisin a déclaré…", "actief"),
                    ("La ministre a répondu…", "actief"),
                ],
                "Passief: être + deelwoord, eventueel met par.",
                kolommen=["actief", "passief"],
            ),
            mk(
                "Wat zei de buurman letterlijk?",
                ["« Je n'ai jamais été consulté. »", "« Il n'avait jamais été consulté. »", "« Je ne serai jamais consulté. »", "« Vous n'avez pas été consultés. »"],
                0,
                "Plus-que-parfait in de indirecte rede komt van een passé composé; il wordt je.",
            ),
            keuze(
                "« Se demandent si le bruit va augmenter » is een [[*indirecte vraag|uitroepende zin]].",
                "Een vraag in een bijzin met si, zonder vraagteken.",
            ),
            mk(
                "Wat betekent « le mois suivant » in de indirecte rede?",
                ["de maand daarna", "deze maand nog", "de vorige maand", "elke maand opnieuw"],
                0,
                "Le mois prochain schuift naar le mois suivant.",
            ),
            inv(
                "Welk voorzetsel van drie letters staat voor de handelende persoon in de eerste zin?",
                ["par"],
                "Inauguré par la ministre.",
            ),
        ],
    ),
    tabel(
        "Welk soort zin is dit?",
        [
            ("Ferme la porte !", "bevelend"),
            ("Quel beau paysage !", "uitroepend"),
            ("Est-ce que tu viens ?", "vragend"),
            ("Il fait froid.", "mededelend"),
        ],
        "Bevel, uitroep, vraag of mededeling.",
        kolommen=["mededelend", "vragend", "bevelend", "uitroepend"],
    ),
    tabel(
        "Welk zinsdeel is dit stuk in « Marie offre des fleurs à sa mère »?",
        [
            ("Marie", "onderwerp"),
            ("offre", "persoonsvorm"),
            ("des fleurs", "COD"),
            ("à sa mère", "COI"),
        ],
        "Wie? doet wat? wat? aan wie?",
        kolommen=["onderwerp", "persoonsvorm", "COD", "COI"],
    ),
    sorteer(
        "Is dit voegwoord nevenschikkend of onderschikkend?",
        ["Nevenschikkend", "Onderschikkend"],
        [
            ("mais", "Nevenschikkend"),
            ("parce que", "Onderschikkend"),
            ("donc", "Nevenschikkend"),
            ("quand", "Onderschikkend"),
            ("car", "Nevenschikkend"),
            ("pour que", "Onderschikkend"),
        ],
        "Nevenschikkend: et, ou, mais, donc, or, ni, car.",
    ),
    koppel(
        "Koppel het tijdwoord in de directe rede aan de vorm in de indirecte rede na een inleiding in het verleden.",
        [
            ("demain", "le lendemain"),
            ("hier", "la veille"),
            ("aujourd'hui", "ce jour-là"),
            ("maintenant", "à ce moment-là"),
        ],
        ["la semaine passée"],
        "Tijdwoorden schuiven mee.",
    ),
    volgorde(
        "Zet de woorden in de juiste volgorde: ik heb haar nooit gezien.",
        ["Je", "ne", "l'ai", "jamais", "vue"],
        "Ne en jamais rond het hulpwerkwoord; vue volgt l' (haar).",
    ),
    mk(
        "Hoe zet je « Où habites-tu ? » om in de indirecte rede?",
        ["Il me demande où j'habite.", "Il me demande si j'habite.", "Il me demande où habites-tu.", "Il me demande est-ce que j'habite."],
        0,
        "Vraagwoord blijft; geen omkering in de bijzin.",
    ),
    mk(
        "« Je suis fatigué », dit Paul hier. Hoe zet je dat om?",
        ["Paul a dit qu'il était fatigué.", "Paul a dit qu'il est fatigué hier.", "Paul a dit que je suis fatigué.", "Paul a dit qu'il serait fatigué."],
        0,
        "Inleiding in het verleden: présent → imparfait.",
    ),
    mk(
        "Wat is de passieve vorm van « La police a arrêté deux voleurs »?",
        ["Deux voleurs ont été arrêtés par la police.", "Deux voleurs ont arrêté la police.", "Deux voleurs sont arrêtés à la police.", "La police a été arrêtée hier par deux voleurs."],
        0,
        "Het COD wordt onderwerp; deelwoord volgt voleurs.",
    ),
    mk(
        "Hoe zeg je « Er werd een fiets gestolen » in gewoon gesproken Frans?",
        ["On a volé un vélo.", "Un vélo a été volé par on.", "Il a volé un vélo à on.", "Un vélo est volant."],
        0,
        "In spreektaal gebruik je vaak on in plaats van een passieve zin.",
    ),
    mk(
        "Wat betekent « Il ne mange que des légumes »?",
        ["Hij eet alleen groenten", "Hij eet geen groenten", "Hij eet nooit groenten", "Hij eet niet meer groenten"],
        0,
        "Ne … que: slechts, alleen.",
    ),
    mk(
        "Welke vraag in schrijftaal is juist?",
        ["Quand partez-vous ?", "Quand vous partez-vous ?", "Quand partez vous-vous ?", "Quand est-ce partez-vous ?"],
        0,
        "Vraagwoord + omkering met een streepje.",
    ),
    keuze(
        "Op « Tu n'aimes pas le chocolat ? » antwoord je bevestigend met « [[*Si|Oui]], j'adore ça ! »",
        "Na een ontkennende vraag: si.",
    ),
    keuze(
        "« Elle n'a [[*rien|personne]] dit pendant le cours. » Ze zei niets.",
        "Ne … rien: niets.",
    ),
    keuze(
        "« Cette maison a été [[*construite|construit]] en 1900. »",
        "Passief: het deelwoord volgt het onderwerp.",
    ),
    keuze(
        "« Je reste à la maison [[*car|pour que]] je suis malade. »",
        "Car (want) + indicatif; pour que vraagt een subjonctif.",
    ),
    keuze(
        "In « J'ai [[*souvent|souvant]] voyagé » staat het bijwoord tussen hulpwerkwoord en deelwoord.",
        "Souvent, met -ent.",
    ),
    tabel(
        "Juist of fout over Franse zinsbouw?",
        [
            ("In een indirecte vraag staat geen vraagteken.", J),
            ("Est-ce que wordt in een indirecte vraag si.", J),
            ("Na pour que volgt een indicatif.", F),
            ("Een zin kan tegelijk vragend en ontkennend zijn.", J),
        ],
        "Na pour que volgt een subjonctif.",
    ),
    inv(
        "Zet om met één woord: « Je viendrai demain. » → Elle a dit qu'elle ___ le lendemain.",
        ["viendrait"],
        "Futur → conditionnel.",
    ),
    inv(
        "Vul in met één woord: « Il m'a demandé ___ j'avais faim. » (of)",
        ["si"],
        "Indirecte ja-neevraag: si.",
    ),
    sleep(
        "Il m'a demandé [[ce que]] je faisais et [[si]] je venais. Je lui ai dit [[que]] j'étudiais.",
        ["est-ce que", "qu'est-ce que"],
        "Qu'est-ce que → ce que; est-ce que → si; mededeling → que.",
    ),
    open_(
        "Zet om in de indirecte rede, beginnend met « Elle m'a dit que… »: « Je pars en vacances demain et je t'enverrai une carte. »",
        "Elle m'a dit qu'elle partait en vacances le lendemain et qu'elle m'enverrait une carte.",
    ),
    mk(
        "Welke ontkenning betekent « niemand »?",
        ["ne … personne", "ne … rien du tout", "ne … plus", "ne … jamais"],
        0,
        "Personne: niemand.",
    ),
    keuze(
        "« Qu'est-ce que tu fais ? » wordt in de indirecte rede « Il demande [[*ce que|qu'est-ce que]] tu fais. »",
        "Qu'est-ce que → ce que.",
    ),
    keuze(
        "« Viens-tu ce soir ? » is [[*formeler|minder formeel]] dan « Tu viens ce soir ? ».",
        "De omkering hoort bij schrijftaal.",
    ),
    tabel(
        "Juist of fout: staat deze zin in de passieve vorm?",
        [
            ("La décision sera prise demain.", J),
            ("Les élèves prennent le bus.", F),
            ("Trois personnes ont été blessées.", J),
        ],
        "Passief: être + deelwoord, het onderwerp ondergaat de handeling.",
    ),
]

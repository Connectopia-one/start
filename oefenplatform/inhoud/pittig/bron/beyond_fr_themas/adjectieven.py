"""Bijvoeglijke naamwoorden, bijwoorden en vergelijken — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez la critique d'un restaurant.\n\n"
    "« Le Petit Jardin est un ancien café transformé en restaurant. La salle est belle et lumineuse, "
    "les serveuses sont souriantes et sérieuses. Le plat du jour était délicieux, mais le dessert était moins bon que l'entrée. "
    "On mange mieux ici qu'au restaurant d'en face, et les prix sont aussi bas qu'à la cantine. "
    "Néanmoins, on attend longtemps. C'est peut-être le meilleur restaurant du quartier. »"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in de recensie?",
                [
                    ("Het restaurant was vroeger een café.", J),
                    ("Het dessert was lekkerder dan het voorgerecht.", F),
                    ("De prijzen zijn even laag als in de schoolkantine.", J),
                    ("Je moet er lang wachten.", J),
                ],
                "Un ancien café; moins bon que l'entrée; aussi bas qu'à la cantine; on attend longtemps.",
            ),
            mk(
                "Waarom staat er « mieux » en niet « meilleur » in « on mange mieux ici »?",
                ["het hoort bij het werkwoord manger", "het hoort bij het woord restaurant", "het staat in het meervoud", "het is een overtreffende trap"],
                0,
                "Mieux is de vergrotende trap van het bijwoord bien.",
            ),
            keuze(
                "« Un ancien café » betekent hier [[*een vroeger café|een heel oud café]].",
                "Ancien vóór het naamwoord: vroeger.",
            ),
            mk(
                "Wat betekent « néanmoins » in de tekst?",
                ["nochtans", "daarom", "bovendien", "ten slotte"],
                0,
                "Néanmoins: nochtans, toch.",
            ),
            inv(
                "Welk woord uit de tekst is de vrouwelijke meervoudsvorm van « sérieux »?",
                ["sérieuses"],
                "-eux wordt -euse, met -s in het meervoud.",
            ),
        ],
    ),
    tabel(
        "Wat is de vrouwelijke vorm?",
        [
            ("actif", "active"),
            ("heureux", "heureuse"),
            ("long", "longue"),
            ("nouveau", "nouvelle"),
        ],
        "Elk patroon heeft zijn eigen uitgang.",
        kolommen=["active", "heureuse", "longue", "nouvelle"],
    ),
    tabel(
        "Staat het bijvoeglijk naamwoord vóór of achter het naamwoord?",
        [
            ("petit bij maison", "vóór"),
            ("rouge bij voiture", "achter"),
            ("jeune bij garçon", "vóór"),
            ("intéressant bij film", "achter"),
        ],
        "Korte, veelgebruikte woorden zoals petit, jeune staan vóór; kleuren en langere woorden achter.",
        kolommen=["vóór", "achter"],
    ),
    sorteer(
        "Is dit een bijvoeglijk naamwoord of een bijwoord?",
        ["Bijvoeglijk naamwoord", "Bijwoord"],
        [
            ("lent", "Bijvoeglijk naamwoord"),
            ("lentement", "Bijwoord"),
            ("bon", "Bijvoeglijk naamwoord"),
            ("bien", "Bijwoord"),
            ("souvent", "Bijwoord"),
            ("meilleur", "Bijvoeglijk naamwoord"),
        ],
        "Een bijwoord hoort bij een werkwoord, een bijvoeglijk naamwoord bij een naamwoord.",
    ),
    koppel(
        "Koppel het bijvoeglijk naamwoord aan zijn bijwoord.",
        [
            ("doux", "doucement"),
            ("heureux", "heureusement"),
            ("rapide", "rapidement"),
            ("vrai", "vraiment"),
        ],
        ["lentement"],
        "Meestal vrouwelijke vorm + -ment; na een klinker gewoon -ment.",
    ),
    volgorde(
        "Zet van weinig naar veel: hoe vaak gebeurt het?",
        ["jamais", "rarement", "quelquefois", "souvent", "toujours"],
        "Bijwoorden van frequentie.",
    ),
    mk(
        "Welke zin is juist voor « een mooie oude kerk »?",
        ["une belle vieille église", "une église belle vieille", "une beau vieux église", "une belle église vieil"],
        0,
        "Beau en vieux staan vóór het naamwoord en worden vrouwelijk.",
    ),
    mk(
        "Hoe zeg je « een oude man » met vieux vóór een klinker?",
        ["un vieil homme", "un vieux homme", "un vieille homme", "un vieu homme"],
        0,
        "Vieux wordt vieil vóór een klinker of stomme h, net als bel en nouvel.",
    ),
    mk(
        "Welke vorm past: « Ces chemises sont ___. » (lichtgroen)",
        ["vert clair", "vertes claires", "verts clairs", "verte claire"],
        0,
        "Een samengestelde kleur blijft onveranderd.",
    ),
    mk(
        "Welke zin vergelijkt juist?",
        ["Ce livre est meilleur que le film.", "Ce livre est plus bon que le film.", "Ce livre est mieux que le film.", "Ce livre est plus meilleur que le film."],
        0,
        "Bon wordt meilleur; plus bon bestaat niet.",
    ),
    mk(
        "Hoe zeg je « de hoogste berg van Europa »?",
        ["la plus haute montagne d'Europe", "la plus haute montagne en Europe", "la haute plus montagne d'Europe", "le plus haut montagne d'Europe"],
        0,
        "Na een overtreffende trap: de of du.",
    ),
    mk(
        "Welke betekenis heeft « un pauvre garçon »?",
        ["een zielige jongen", "een arme jongen zonder geld", "een kleine jongen", "een domme jongen"],
        0,
        "Pauvre vóór het naamwoord: zielig; achter: zonder geld.",
    ),
    keuze(
        "« Mes parents sont [[*contents|contentes]]. » Er is een vader en een moeder.",
        "Gemengde groep: mannelijk meervoud.",
    ),
    keuze(
        "« Elle parle [[*bien|bon]] français. »",
        "Bien hoort bij parler.",
    ),
    keuze(
        "« Ce sont de [[*beaux|beaus]] jardins. »",
        "Beau wordt beaux.",
    ),
    keuze(
        "« Une fille [[*sportive|sportif]] fait du sport tous les jours. »",
        "-f wordt -ve.",
    ),
    keuze(
        "« Paul court [[*aussi vite que|aussi vite comme]] Marc. »",
        "Aussi … que: even … als.",
    ),
    tabel(
        "Juist of fout over Franse bijvoeglijke naamwoorden?",
        [
            ("Jeune blijft in het vrouwelijk jeune.", J),
            ("Bon wordt in het vrouwelijk bonne.", J),
            ("Kleuren staan in het Frans vóór het naamwoord.", F),
            ("Na être komt het bijvoeglijk naamwoord overeen met het onderwerp.", J),
        ],
        "Kleuren staan achter het naamwoord.",
    ),
    inv(
        "Maak het bijwoord van « sérieux »: « Il travaille ___. »",
        ["sérieusement"],
        "Sérieuse + -ment.",
    ),
    inv(
        "Vul in met één woord: « Elle chante ___ que sa sœur. » (beter)",
        ["mieux"],
        "Bij chanter: mieux.",
    ),
    inv(
        "Vul in met één woord: « C'est la ___ idée de la journée ! » (beste)",
        ["meilleure"],
        "Idée is vrouwelijk: la meilleure.",
    ),
    sleep(
        "Notre [[nouvelle]] maison est [[plus]] grande [[que]] l'ancienne.",
        ["nouveau", "comme"],
        "Bijvoeglijk naamwoord en vergrotende trap.",
    ),
    open_(
        "Vergelijk in het Frans twee steden die je kent in twee zinnen. Gebruik plus … que of moins … que en een bijvoeglijk naamwoord.",
        "Bruxelles est plus grande que Gand. Mais Gand est moins chère et plus calme que Bruxelles.",
    ),
    mk(
        "Welk woord past: « Il est ___ fatigué ce soir. » (echt)",
        ["vraiment", "vrai", "vraie", "vraisemblable"],
        0,
        "Een bijwoord bij een bijvoeglijk naamwoord: vraiment.",
    ),
    keuze(
        "« Les [[*meilleurs|mieux]] joueurs de l'équipe » zijn de beste spelers.",
        "Bij een naamwoord: meilleur(s).",
    ),
    tabel(
        "Welke vorm van beau past?",
        [
            ("un ___ garçon", "beau"),
            ("un ___ arbre", "bel"),
            ("une ___ fleur", "belle"),
        ],
        "Bel vóór een mannelijk woord met een klinker.",
        kolommen=["beau", "bel", "belle"],
    ),
]

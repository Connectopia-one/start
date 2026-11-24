"""Voornaamwoorden — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le dialogue.\n\n"
    "Emma : Tu as vu Hugo à la fête ?\n"
    "Léa : Oui, je l'ai vu, mais je ne lui ai pas parlé.\n"
    "Emma : Et les photos, tu les as envoyées à tes parents ?\n"
    "Léa : Oui, je les leur ai envoyées hier.\n"
    "Emma : Tu vas encore à Bruxelles ce week-end ?\n"
    "Léa : Non, j'y suis allée la semaine passée. Mais j'ai acheté des chocolats là-bas. Tu en veux ?\n"
    "Emma : Avec plaisir ! C'est la boîte dont tu m'as parlé ?"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Waarvoor staat het voornaamwoord in de dialoog?",
                [
                    ("l' in « je l'ai vu »", "Hugo"),
                    ("lui in « je ne lui ai pas parlé »", "Hugo"),
                    ("les in « je les leur ai envoyées »", "les photos"),
                    ("leur in « je les leur ai envoyées »", "tes parents"),
                ],
                "L' en les zijn COD, lui en leur COI.",
                kolommen=["Hugo", "les photos", "tes parents"],
            ),
            mk(
                "Waarvoor staat y in « j'y suis allée »?",
                ["à Bruxelles", "à la fête", "les chocolats", "la semaine passée"],
                0,
                "Y vervangt een plaats.",
            ),
            mk(
                "Waarvoor staat en in « Tu en veux ? »?",
                ["des chocolats", "à Bruxelles", "les photos", "à tes parents"],
                0,
                "En vervangt een woord met des.",
            ),
            keuze(
                "In « la boîte dont tu m'as parlé » staat dont omdat je [[*parle de quelque chose|parle à quelqu'un]].",
                "Parler de: dont.",
            ),
        ],
    ),
    volgorde(
        "Zet de woorden in de juiste volgorde: « Il ___ ___ donne. » met les clés aan zijn zus.",
        ["Il", "les", "lui", "donne"],
        "Le, la, les vóór lui, leur.",
    ),
    tabel(
        "COD of COI?",
        [
            ("Je la regarde.", "COD"),
            ("Je lui téléphone.", "COI"),
            ("Il les attend.", "COD"),
            ("Nous leur répondons.", "COI"),
        ],
        "Téléphoner à, répondre à vragen een COI.",
        kolommen=["COD", "COI"],
    ),
    tabel(
        "Qui, que, dont of où?",
        [
            ("le garçon ___ chante", "qui"),
            ("la chanson ___ j'écoute", "que"),
            ("le livre ___ j'ai besoin", "dont"),
            ("le jour ___ il est arrivé", "où"),
        ],
        "Onderwerp qui, lijdend voorwerp que, met de dont, plaats of tijd où.",
        kolommen=["qui", "que", "dont", "où"],
    ),
    koppel(
        "Koppel de vorm van celui aan het naamwoord dat hij vervangt.",
        [
            ("celui de Marc", "le vélo"),
            ("celle de Marc", "la veste"),
            ("ceux de Marc", "les livres"),
            ("celles de Marc", "les chaussures"),
        ],
        ["le mien"],
        "Celui, celle, ceux, celles volgen geslacht en getal.",
    ),
    mk(
        "Welk bevel is juist?",
        ["Dis-moi la vérité !", "Me dis la vérité !", "Dis-me la vérité !", "Ne dis-moi pas la vérité !"],
        0,
        "Bevestigend: achter het werkwoord, me wordt moi.",
    ),
    mk(
        "Hoe maak je « Donne-le-moi ! » ontkennend?",
        ["Ne me le donne pas !", "Ne donne-le-moi pas !", "Ne le me donne pas !", "Donne-le-moi pas !"],
        0,
        "Ontkennend: voornaamwoorden weer vóór het werkwoord, me vóór le.",
    ),
    mk(
        "Vervang « à mon examen » in « Je pense à mon examen. »",
        ["J'y pense.", "J'en pense.", "Je lui pense.", "Je le pense."],
        0,
        "Penser à + ding: y.",
    ),
    mk(
        "Vervang « sœurs » in « Elle a trois sœurs. »",
        ["Elle en a trois.", "Elle les a trois.", "Elle y a trois.", "Elle leur a trois."],
        0,
        "Bij een hoeveelheid: en.",
    ),
    mk(
        "Welke zin met een tonique is juist?",
        ["Je pars avec eux.", "Je pars avec ils.", "Je pars avec les.", "Je pars avec leur."],
        0,
        "Na een voorzetsel: moi, toi, lui, elle, nous, vous, eux, elles.",
    ),
    mk(
        "« Ce n'est pas ton stylo, c'est ___. » (van mij)",
        ["le mien", "mon", "moi", "la mienne"],
        0,
        "Stylo is mannelijk: le mien.",
    ),
    mk(
        "Welke betekenis heeft « ce qui » in « Dis-moi ce qui ne va pas »?",
        ["wat, als onderwerp", "wie, als onderwerp", "wat, als lijdend voorwerp", "waar, als plaats"],
        0,
        "Ce qui is onderwerp van va.",
    ),
    keuze(
        "« [[*Personne|Chacun]] n'est venu à la fête. » Er was niemand.",
        "Personne ne: niemand.",
    ),
    keuze(
        "« De [[*quoi|qui]] parles-tu ? » Het gaat over een film.",
        "Quoi voor dingen, qui voor personen.",
    ),
    keuze(
        "« Elle [[*s'|se]]habille vite. »",
        "Se wordt s' voor een klinker.",
    ),
    keuze(
        "« Je ne comprends pas [[*ce que|ce qui]] tu veux. »",
        "Tu veux iets: lijdend voorwerp, dus ce que.",
    ),
    keuze(
        "« C'est [[*lui|il]] qui a gagné. »",
        "Na c'est: de tonique.",
    ),
    tabel(
        "Juist of fout over de plaats van het voornaamwoord?",
        [
            ("In « je vais le faire » staat le vóór de infinitief.", J),
            ("In de passé composé staat het voornaamwoord vóór avoir of être.", J),
            ("In « Prends-en ! » staat en achter het bevel.", J),
            ("In « Ne le prends pas » staat le achter het werkwoord.", F),
        ],
        "In een ontkennend bevel staat het voornaamwoord vóór het werkwoord.",
    ),
    inv(
        "Vervang en schrijf de hele zin: « J'ai vu tes amis. » → « Je ___ ai vus. » Geef het ontbrekende woord.",
        ["les"],
        "Tes amis: COD meervoud.",
    ),
    inv(
        "Vul in met één woord: « Voilà le restaurant ___ nous avons mangé. »",
        ["où"],
        "Plaats: où.",
    ),
    inv(
        "Vul in met één woord: « C'est le film ___ tout le monde parle. »",
        ["dont"],
        "Parler de: dont.",
    ),
    inv(
        "Vervang met twee woorden in de juiste orde: « Il donne du pain aux canards. » → « Il ___ ___ donne. »",
        ["leur en"],
        "Leur vóór en.",
    ),
    sleep(
        "Mon frère a un vélo. Il [[le]] prête souvent à ses amis. Il [[leur]] fait confiance. Moi, je préfère garder [[le mien]].",
        ["lui", "la mienne"],
        "COD, COI en bezittelijk voornaamwoord.",
    ),
    open_(
        "Beantwoord in het Frans met een voornaamwoord: « Tu as écrit à ta grand-mère ? » en « Tu vas à la plage demain ? »",
        "Oui, je lui ai écrit hier. Non, je n'y vais pas demain.",
    ),
    sorteer(
        "Vervang je dit door y of door en?",
        ["y", "en"],
        [
            ("à Paris", "y"),
            ("du café", "en"),
            ("à mon avenir", "y"),
            ("de l'école", "en"),
            ("des pommes", "en"),
            ("dans le jardin", "y"),
        ],
        "Plaats of à + ding: y; de + ding of hoeveelheid: en.",
    ),
    keuze(
        "« Qui » in « l'homme qui parle » is het [[*onderwerp|lijdend voorwerp]] van parle.",
        "Qui als betrekkelijk voornaamwoord is het onderwerp.",
    ),
    mk(
        "Welke wederkerende vorm is juist bij « nous »?",
        ["Nous nous levons tôt.", "Nous se levons tôt.", "Nous nous lève tôt.", "Nous levons nous tôt."],
        0,
        "Het voornaamwoord volgt de persoon: nous nous.",
    ),
]

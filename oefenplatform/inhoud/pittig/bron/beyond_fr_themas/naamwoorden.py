"""Zelfstandige naamwoorden, lidwoorden en determinanten — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le petit texte.\n\n"
    "Ce week-end, je suis allée au marché avec ma sœur. Nous avons acheté du fromage, de la salade et beaucoup de fraises. "
    "Il n'y avait plus de pain, alors nous sommes passées à la boulangerie. "
    "Ensuite, nous avons rencontré quelques amis de mon frère devant cet hôtel près de la gare. "
    "Chaque samedi, ils jouent au football dans le parc."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Waarom staat er « de pain » en niet « du pain » in de tekst?",
                ["het staat na een ontkenning", "pain is vrouwelijk", "het staat na een hoeveelheid", "pain begint met een medeklinker"],
                0,
                "Il n'y avait plus de pain: na ne … plus wordt du gewoon de.",
            ),
            mk(
                "Waarom staat er « beaucoup de fraises » en niet « beaucoup des fraises »?",
                ["na een hoeveelheid komt de", "fraises is mannelijk", "het staat na een ontkenning", "er volgt een bijvoeglijk naamwoord"],
                0,
                "Beaucoup de, un peu de, trop de.",
            ),
            keuze(
                "In « cet hôtel » staat cet omdat hôtel [[*met een stomme h begint|vrouwelijk is]].",
                "Cet voor een mannelijk woord met klinker of stomme h.",
            ),
            tabel(
                "Welk soort bepaler is dit in de tekst?",
                [
                    ("du fromage", "deelaanduidend"),
                    ("quelques amis", "onbepaald"),
                    ("cet hôtel", "aanwijzend"),
                    ("chaque samedi", "onbepaald"),
                    ("de la salade", "deelaanduidend"),
                ],
                "Du/de la: onbepaalde hoeveelheid; quelques, chaque: onbepaald; cet: aanwijzend.",
                kolommen=["deelaanduidend", "onbepaald", "aanwijzend"],
            ),
            inv(
                "Welke samentrekking van à + le staat in de laatste zin? Eén woord.",
                ["au"],
                "Ils jouent au football: à + le = au.",
            ),
        ],
    ),
    sorteer(
        "Is dit naamwoord mannelijk of vrouwelijk?",
        ["Mannelijk", "Vrouwelijk"],
        [
            ("système", "Mannelijk"),
            ("musée", "Mannelijk"),
            ("question", "Vrouwelijk"),
            ("lycée", "Mannelijk"),
            ("solution", "Vrouwelijk"),
            ("problème", "Mannelijk"),
        ],
        "Een -e op het einde maakt een woord niet vanzelf vrouwelijk.",
    ),
    tabel(
        "Welke vorm van à + lidwoord past?",
        [
            ("Je vais ___ cinéma.", "au"),
            ("Il parle ___ enfants.", "aux"),
            ("Elle va ___ piscine.", "à la"),
            ("Nous allons ___ hôpital.", "à l'"),
        ],
        "Au, aux, à la en à l' voor een klinker of stomme h.",
        kolommen=["au", "aux", "à la", "à l'"],
    ),
    tabel(
        "Welke vorm van quel past?",
        [
            ("___ âge as-tu ?", "quel"),
            ("___ heure est-il ?", "quelle"),
            ("___ films aimes-tu ?", "quels"),
            ("___ langues parles-tu ?", "quelles"),
        ],
        "Quel volgt geslacht en getal van het naamwoord.",
        kolommen=["quel", "quelle", "quels", "quelles"],
    ),
    koppel(
        "Koppel het land aan het juiste voorzetsel voor « naar ».",
        [
            ("le Japon", "au Japon"),
            ("la France", "en France"),
            ("les Pays-Bas", "aux Pays-Bas"),
            ("Paris", "à Paris"),
        ],
        ["du Japon"],
        "Mannelijk land au, vrouwelijk en, meervoud aux, stad à.",
    ),
    mk(
        "Welke zin met een bijvoeglijk naamwoord vóór het meervoud is juist?",
        ["Elle a de jolies robes.", "Elle a des jolies robes.", "Elle a du jolies robes.", "Elle a les jolie robes."],
        0,
        "Bijvoeglijk naamwoord vóór een meervoud: des wordt de.",
    ),
    mk(
        "Welke ontkennende zin met café is juist?",
        ["Je ne bois pas de café.", "Je ne bois pas du café.", "Je ne bois pas des café.", "Je ne bois pas de la café."],
        0,
        "Na pas wordt du gewoon de.",
    ),
    mk(
        "Hoe zeg je « zijn school » als het gaat over de school van Léa?",
        ["son école", "sa école", "ses école", "leur écoles"],
        0,
        "École is vrouwelijk maar begint met een klinker: son.",
    ),
    mk(
        "Hoe zeg je « hun huis » als het gaat over Paul en Marie?",
        ["leur maison", "leurs maison", "sa maison", "ses maison"],
        0,
        "Eén bezit, meerdere bezitters: leur.",
    ),
    mk(
        "Welke zin met chaque of tous is fout?",
        ["Chaque élèves a un livre.", "Chaque élève a un livre.", "Tous les élèves ont un livre.", "Quelques élèves ont un livre."],
        0,
        "Na chaque komt altijd het enkelvoud.",
    ),
    mk(
        "Wat is het meervoud van « un travail »?",
        ["des travaux", "des travails", "des travailles", "des travailx"],
        0,
        "Travail wordt travaux.",
    ),
    mk(
        "Welk lidwoord past in « Elle boit ___ eau minérale »?",
        ["de l'", "du", "de la", "des"],
        0,
        "Eau begint met een klinker: de l'eau.",
    ),
    keuze(
        "In « je viens [[*des|de les]] États-Unis » trek je de + les samen.",
        "De + les = des.",
    ),
    keuze(
        "« Un kilo [[*de|des]] pommes » is juist.",
        "Na een hoeveelheid: de.",
    ),
    keuze(
        "« [[*Cette|Cet]] semaine, je travaille beaucoup. »",
        "Semaine is vrouwelijk: cette.",
    ),
    keuze(
        "« Il a perdu [[*ses|leurs]] clés », zegt Marc over zichzelf.",
        "Eén bezitter, meervoudig bezit: ses.",
    ),
    keuze(
        "« J'habite [[*en|au]] Belgique. »",
        "La Belgique is vrouwelijk: en.",
    ),
    tabel(
        "Juist of fout over Franse naamwoorden?",
        [
            ("Un animal wordt in het meervoud des animaux.", J),
            ("Un cheveu wordt in het meervoud des cheveus.", F),
            ("Le wordt l' voor een stomme h.", J),
            ("Ma wordt mon voor een vrouwelijk woord met een klinker.", J),
        ],
        "Cheveu wordt cheveux.",
    ),
    inv(
        "Vul de juiste aanwijzende bepaler in: « ___ enfants sont très sages. »",
        ["ces", "Ces"],
        "Meervoud: ces.",
    ),
    inv(
        "Vul het juiste lidwoord in: « Il y a ___ monde dans la rue ? Non, il n'y a pas ___ monde. » Geef het tweede woord.",
        ["de"],
        "Na pas: de monde.",
    ),
    inv(
        "Wat is het meervoud van « un journal »? Geef enkel het naamwoord.",
        ["journaux"],
        "-al wordt -aux.",
    ),
    sleep(
        "Le matin, je bois [[du]] thé et je mange [[de la]] confiture. Je ne mange jamais [[d']]œufs.",
        ["des", "le"],
        "Deelaanduidend lidwoord en de na een ontkenning.",
    ),
    open_(
        "Schrijf in het Frans twee zinnen over wat er in jouw koelkast staat en wat er niet meer is. Gebruik een deelaanduidend lidwoord en een ontkenning.",
        "Dans mon frigo, il y a du lait, de la crème et des yaourts. Il n'y a plus de beurre.",
    ),
    mk(
        "Waarom schrijf je « mon amie » en niet « ma amie »?",
        ["omdat amie met een klinker begint", "omdat amie een mannelijk woord is", "omdat het hier om een meervoud gaat", "omdat het over een jongen gaat"],
        0,
        "Ma wordt mon voor een klinker.",
    ),
    keuze(
        "« Je mange [[*de la|du]] viande », want viande is vrouwelijk.",
        "Deelaanduidend lidwoord: de la bij een vrouwelijk woord.",
    ),
    tabel(
        "Ce, cet of cette?",
        [
            ("___ livre", "ce"),
            ("___ arbre", "cet"),
            ("___ fille", "cette"),
            ("___ homme", "cet"),
        ],
        "Cet voor een mannelijk woord met klinker of stomme h.",
        kolommen=["ce", "cet", "cette"],
    ),
]

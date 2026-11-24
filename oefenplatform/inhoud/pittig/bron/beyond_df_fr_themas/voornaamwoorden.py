"""Voornaamwoorden en betrekkelijke bijzinnen — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le dialogue.\n\n« — Tu connais la fille qui parle avec Paul ?\n— Oui, je la connais. C'est Emma, l'amie dont je t'ai parlé.\n"
        "— Elle habite où ?\n— À Liège, la ville où je suis né. J'y vais souvent.\n— Tu as des photos d'elle ?\n— Oui, j'en ai beaucoup. Regarde, celle-ci est de cet été. »",
        [
            keuze("In « la fille qui parle » is qui het [[*onderwerp|lijdend voorwerp]] van de bijzin.", "Qui doet iets: zij spreekt."),
            keuze("« je la connais » : la vervangt [[*la fille|Paul|la ville]].", "Lijdend voorwerp, vrouwelijk."),
            keuze("« l'amie dont je t'ai parlé » : dont staat er omdat het [[*parler de|parler à]] is.", "Dont vervangt de + iets."),
            keuze("« J'y vais souvent » : y vervangt [[*een plaats|een hoeveelheid]].", "Y = à Liège."),
            keuze("« j'en ai beaucoup » : en vervangt [[*des photos|Emma|Liège]].", "En vervangt een hoeveelheid."),
        ],
    ),
    tabel("Qui, que, dont of où?", [
        ("le garçon ___ chante", "qui"), ("le film ___ j'ai vu", "que"), ("le livre ___ je parle", "dont"), ("la ville ___ j'habite", "où"),
    ], "Qui onderwerp, que lijdend voorwerp, dont na de, où plaats.", kolommen=["qui", "que", "dont", "où"]),
    tabel("Le, la, les, lui of leur?", [
        ("Je vois Marie. → Je ___ vois.", "la"), ("Je parle à Marie. → Je ___ parle.", "lui"),
        ("Je téléphone à mes parents. → Je ___ téléphone.", "leur"), ("Je lis les livres. → Je ___ lis.", "les"),
    ], "Lijdend voorwerp le, la, les; meewerkend voorwerp lui, leur.", kolommen=["la", "les", "lui", "leur"]),
    koppel("Koppel elk onderwerp aan zijn beklemtoonde vorm.", [
        ["je", "moi"], ["tu", "toi"], ["ils", "eux"], ["nous", "nous"],
    ], ["eles"], "Moi, toi, lui, elle, nous, vous, eux, elles."),
    koppel("Koppel elk bezittelijk voornaamwoord aan zijn betekenis.", [
        ["le mien", "het mijne"], ["le tien", "het jouwe"], ["le sien", "het zijne of hare"], ["les nôtres", "de onze"],
    ], ["de hunne van mij"], "Les leurs is de hunne."),
    mk("« Tu me donnes le stylo ? » « Oui, je ___ donne. » Wat past?",
       ["te le", "le te", "lui le", "le toi"], 0, "Te staat voor le."),
    mk("« Tu donnes le cadeau à Marie ? » « Oui, je ___ donne. » Wat past?",
       ["le lui", "lui le", "la lui", "le leur"], 0, "Le voor lui."),
    mk("Hoe zeg je « Ik zie hem niet »?",
       ["Je ne le vois pas.", "Je ne vois le pas.", "Je le ne vois pas.", "Je ne vois pas le lui."], 0,
       "Ne, voornaamwoord, werkwoord, pas."),
    mk("« Ce n'est pas ma voiture, c'est ___ de mon père. » Wat past?",
       ["celle", "celui", "ceux", "cela"], 0, "Voiture is vrouwelijk: celle."),
    mk("« ___ est-ce que tu fais ce soir ? » Wat past?",
       ["Qu'", "Qui", "Quoi", "Dont"], 0, "Qu'est-ce que vraagt naar een ding."),
    mk("« Avec ___ tu écris ? » Je vraagt naar het schrijfgerief. Wat past?",
       ["quoi", "que", "qui est-ce", "dont"], 0, "Na een voorzetsel: quoi."),
    mk("« Je ne sais pas ___ tu veux. » Wat past?",
       ["ce que", "ce qui", "que ce", "dont"], 0, "Ce que als lijdend voorwerp."),
    inv("Vul in: « Tu penses à ton examen ? » « Oui, j'___ pense souvent. » Eén letter.", ["y"], "Penser à iets: y."),
    inv("Vul in: « Tu veux du gâteau ? » « Oui, j'___ veux bien. » Eén woord.", ["en"], "Partitief: en."),
    inv("Vul in: « Elle part avec ___. » (met hen, mannelijk) Eén woord.", ["eux"], "Na een voorzetsel: eux."),
    inv("Vul in: « Regarde-___ ! » (kijk naar mij) Eén woord.", ["moi"], "Bij een bevel wordt me moi."),
    keuze("« L'homme [[*qui|qu']] est là est mon oncle. »", "Qui wordt nooit qu'."),
    keuze("« Ne [[*lui|à lui]] dis pas mon secret ! »", "In een verbod staat het voornaamwoord vooraan."),
    keuze("« Je ne vois [[*personne|chacun]] dans la rue. »", "Ne ... personne: niemand."),
    keuze("« [[*Chacun|Personne]] apporte quelque chose à manger. »", "Chacun: ieder."),
    keuze("« Ce livre-ci est à moi, [[*celui-là|celle-là]] est à toi. »", "Livre is mannelijk."),
    keuze("« C'est l'amie à [[*qui|que]] j'écris. »", "Na een voorzetsel bij een persoon: qui."),
    tabel("Is de zin juist (voornaamwoorden)?", [
        ("Je les lui donne.", J), ("Je lui les donne.", F), ("Donne-moi le sel.", J), ("Moi, je pense que oui.", J),
    ], "Le, la, les voor lui en leur; bij een bevel achteraan."),
    volgorde("Zet de woorden in de juiste volgorde: « pas / le / je / vois / ne »", [
        "je", "ne", "le", "vois", "pas",
    ], "Ne eerst, dan het voornaamwoord, dan het werkwoord."),
    sleep("Le film [[que]] j'ai vu hier est celui [[dont]] tout le monde parle.",
          ["qui", "où"], "Que als lijdend voorwerp; dont bij parler de."),
    open_("Leg in het Nederlands uit wanneer je « lui » gebruikt en wanneer « le ».",
          "Le vervangt een lijdend voorwerp zonder voorzetsel; lui vervangt een persoon na à, een meewerkend voorwerp.",
          "Je le vois, je lui parle."),
]

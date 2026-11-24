"""Woordvelden kunst, geschiedenis en de samenleving — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis l'affiche.\n\n« MUSÉE DE LA VILLE – Nouvelle exposition : « L'Empire romain »\n"
        "Venez voir des sculptures, des pièces de monnaie et des tableaux du premier siècle. Notre guide vous parle des empereurs, des batailles et de la vie quotidienne à Rome. "
        "Prix d'entrée : 8 euros, gratuit pour les enfants de moins de 12 ans. Tout l'argent de la boutique va à une association caritative. "
        "Nous cherchons des bénévoles pour le week-end ! »",
        [
            keuze("De tentoonstelling gaat over [[*het Romeinse Rijk|de Franse Revolutie|het oude Griekenland]].", "L'Empire romain."),
            keuze("« des tableaux » zijn hier [[*schilderijen|borden in de klas]].", "Un tableau in de kunst: een schilderij."),
            mk("Wat gebeurt er met het geld van de museumwinkel?",
               ["Het gaat naar een goed doel.", "Het betaalt de gids van de tentoonstelling.", "Het gaat naar de Romeinse keizer.", "Het betaalt de inkom van de kinderen."], 0,
               "Une association caritative."),
            keuze("Kinderen onder 12 betalen [[*niets|8 euro|de helft]].", "Gratuit."),
            keuze("Het museum zoekt [[*vrijwilligers|kunstenaars|klanten]] voor het weekend.", "Des bénévoles."),
        ],
    ),
    sorteer("Hoort het bij geschiedenis of bij de politiek van vandaag?", ["geschiedenis", "politiek vandaag"], [
        ["l'Empire romain", "geschiedenis"], ["une élection", "politiek vandaag"], ["une ancienne bataille", "geschiedenis"],
        ["le premier ministre", "politiek vandaag"], ["un vieux traité de paix", "geschiedenis"], ["le conseil communal", "politiek vandaag"],
    ], "Oude rijken en veldslagen tegenover verkiezingen en ministers."),
    koppel("Koppel elk Frans woord over boeken aan zijn betekenis.", [
        ["un roman", "een roman"], ["un chapitre", "een hoofdstuk"], ["un auteur", "een schrijver"], ["une biographie", "een levensverhaal"],
    ], ["een Romein"], "Un Romain is een Romein."),
    koppel("Koppel elk Frans woord uit recht en samenleving aan zijn betekenis.", [
        ["un juge", "een rechter"], ["un réfugié", "een vluchteling"], ["un syndicat", "een vakbond"], ["un citoyen", "een burger"],
    ], ["een handelsbeurs"], "Un salon is een handelsbeurs."),
    mk("« Les acteurs ___ la pièce chaque soir avant la première. » Wat past?",
       ["répètent", "élisent", "manifestent", "votent"], 0, "Répéter: repeteren."),
    mk("Wie leidt een orkest?",
       ["le chef d'orchestre", "le compositeur de la musique", "l'auteur de la pièce", "le public dans la salle"], 0, "De dirigent."),
    mk("« 51 % des gens ont voté oui. » Hoe noem je die 51 %?",
       ["la majorité", "la minorité du groupe", "les médias", "les sondages"], 0, "Meer dan de helft: de meerderheid."),
    mk("Een schrijver vertelt over zijn eigen leven. Hoe heet dat boek?",
       ["une autobiographie", "une biographie", "un roman de fiction", "une nouvelle sur la vie"], 0, "Over je eigen leven."),
    mk("« Le dix-neuvième siècle » zijn de jaren ...",
       ["1800 tot 1899", "1900 tot en met 1999", "1700 tot 1799", "1900 tot 1919"], 0, "De negentiende eeuw."),
    mk("Hoe zeg je « Wij hebben gestemd bij de verkiezingen »?",
       ["Nous avons voté aux élections.", "Nous avons élu aux votes.", "Nous avons manifesté aux élections.", "Nous avons voté les citoyens."], 0,
       "Voter: stemmen; une élection: een verkiezing."),
    inv("Hoe zeg je armoede in het Frans? Twee woorden.", ["la pauvreté", "la pauvrete"], "La pauvreté."),
    inv("Hoe zeg je keizer in het Frans? Eén woord, zonder lidwoord.", ["empereur"], "L'empereur."),
    inv("Hoe zeg je tentoonstelling in het Frans? Eén woord, zonder lidwoord.", ["exposition"], "Une exposition."),
    inv("Hoe zeg je rechtbank in het Frans? Eén woord, zonder lidwoord.", ["tribunal"], "Un tribunal."),
    keuze("« Le [[*public|auteur]] a applaudi pendant dix minutes après le concert. »", "Het publiek klapt."),
    keuze("« La Joconde est un célèbre [[*chef-d'œuvre|répétition]]. »", "Een meesterwerk."),
    keuze("« Des milliers de personnes ont [[*manifesté|répété]] contre la nouvelle loi. »", "Manifester: betogen."),
    keuze("« C'est mon [[*ancienne|vieille ancienne]] école : j'y allais quand j'étais petit. »", "Ancien vooraan: vroeger."),
    keuze("« Il fait du [[*bénévolat|syndicat]] dans une association. »", "Vrijwilligerswerk."),
    keuze("« L'[[*égalité|inégalité]] entre hommes et femmes est un droit de l'homme. »", "Gelijkheid."),
    tabel("Is deze zin juist (kunst en samenleving)?", [
        ("Le tableau est dans une salle du musée.", J), ("Un chef d'orchestre écrit la musique.", F),
        ("Tout le monde a les mêmes droits de l'homme.", J), ("La minorité, c'est plus de la moitié.", F),
    ], "Un compositeur schrijft muziek; de minderheid is minder dan de helft."),
    tabel("Hoort dit bij het theater?", [
        ("la scène", J), ("le public", J), ("une bouilloire", F), ("un traité", F),
    ], "Podium en publiek; een waterkoker en een verdrag niet."),
    sleep("L'[[auteur]] a écrit son premier [[roman]] à vingt ans. Il a douze [[chapitres]].",
          ["juge", "scène"], "Auteur, roman, chapitres."),
    volgorde("Zet deze periodes in de juiste volgorde, van oud naar recent.", [
        "l'Empire romain", "le seizième siècle", "le dix-neuvième siècle", "le vingt et unième siècle",
    ], "Van de oudheid naar vandaag."),
    mk("Wat doet un bénévole?",
       ["helpen zonder loon", "betogen voor een hoger loon", "een wet maken in het parlement", "een boek over iemands leven schrijven"], 0,
       "Een vrijwilliger."),
    open_("Leg in het Nederlands uit waarom « un roman » een valse vriend kan zijn voor iemand die aan Romeinen denkt.",
          "Un roman is een boek, een roman; een Romein is un Romain.",
          "Let op het verschil in schrijfwijze."),
]

"""Woordvelden gezondheid, natuur en milieu — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le message d'Ella.\n\nMonsieur Martin,\n\nJe suis désolée, mais je ne peux pas venir à l'école aujourd'hui. J'ai mal à la gorge, de la toux et de la fièvre. "
        "Ce matin, je suis allée chez mon médecin généraliste. Il m'a donné une ordonnance et il m'a dit de prendre soin de moi pendant trois jours. "
        "J'apporterai un certificat médical à mon retour.\n\nCordialement,\nElla",
        [
            keuze("Ella heeft [[*keelpijn|buikpijn|hoofdpijn]], hoest en koorts.", "Mal à la gorge."),
            keuze("Ella ging naar [[*haar huisarts|het ziekenhuis|de apotheek]].", "Le médecin généraliste."),
            mk("Wat kreeg Ella van de dokter?",
               ["een voorschrift voor medicijnen", "een pleister voor haar zere hand", "een afspraak in het ziekenhuis", "een briefje voor de sportles"], 0,
               "Une ordonnance."),
            keuze("« prendre soin de soi » betekent [[*goed voor jezelf zorgen|veel sporten]].", "Prends soin de toi."),
            keuze("Ella brengt later [[*een doktersattest|haar huiswerk]] mee naar school.", "Un certificat médical."),
        ],
    ),
    sorteer("Hoort het bij gezondheid of bij het milieu?", ["gezondheid", "milieu"], [
        ["la toux", "gezondheid"], ["la pollution", "milieu"], ["un bilan de santé", "gezondheid"],
        ["les émissions", "milieu"], ["une ordonnance", "gezondheid"], ["le gaspillage", "milieu"],
    ], "Klachten en dokterswoorden tegenover vervuiling, uitstoot en verspilling."),
    sorteer("Dier of boom?", ["dier", "boom"], [
        ["un hérisson", "dier"], ["un érable", "boom"], ["un hibou", "dier"], ["un conifère", "boom"], ["un écureuil", "dier"],
    ], "Egel, uil en eekhoorn zijn dieren; esdoorn en naaldboom bomen."),
    koppel("Koppel elk Frans woord over natuurrampen aan zijn betekenis.", [
        ["la sécheresse", "de droogte"], ["une inondation", "een overstroming"], ["une canicule", "een hittegolf"], ["un séisme", "een aardbeving"],
    ], ["een briesje"], "Une brise is een briesje."),
    koppel("Koppel elke Franse uitdrukking over gezondheid aan haar betekenis.", [
        ["avoir le moral à zéro", "zich slecht voelen"], ["prendre du poids", "bijkomen"], ["guérir", "genezen"], ["être stressé", "gespannen zijn"],
    ], ["verdwijnen"], "Verdwijnen is disparaître."),
    mk("Hoe zeg je « Ik heb hoofdpijn » in het Frans?",
       ["J'ai mal à la tête.", "J'ai une douleur dans ma tête.", "J'ai la tête malade.", "Ma tête a un mal."], 0,
       "Avoir mal à + lichaamsdeel."),
    mk("« Après dix kilomètres de course, j'étais complètement ___. » Wat past?",
       ["épuisé", "fier et seul", "bondé", "durable"], 0, "Épuisé: uitgeput."),
    mk("Je snijdt in je vinger. Wat heb je nodig?",
       ["un pansement", "une ordonnance pour des pilules", "une empreinte carbone", "une alimentation équilibrée"], 0, "Un pansement: een pleister."),
    mk("« Le dodo a ___ il y a longtemps. » Wat past?",
       ["disparu", "guéri", "recyclé", "pris du poids"], 0, "Disparaître: verdwijnen, uitsterven."),
    mk("Welke energie is hernieuwbaar?",
       ["le vent", "l'essence de la station", "le charbon d'une mine", "le gaz sous la terre"], 0, "Wind raakt niet op."),
    mk("Op een bord in het park staat « Ne jetez pas vos déchets par terre. » Wat mag je niet doen?",
       ["afval op de grond gooien", "de dieren in het park voederen", "de bomen omhakken", "op het gras lopen"], 0, "Les déchets: het afval."),
    inv("Hoe zeg je ziekenwagen in het Frans? Eén woord, zonder lidwoord.", ["ambulance"], "Une ambulance."),
    inv("Hoe zeg je duurzaam in het Frans? Eén woord.", ["durable"], "Le développement durable."),
    inv("Hoe zeg je beek in het Frans? Eén woord, zonder lidwoord.", ["ruisseau"], "Un ruisseau."),
    inv("Hoe zeg je uil in het Frans? Eén woord, zonder lidwoord.", ["hibou"], "Un hibou."),
    keuze("« Il fait beau aujourd'hui, mais le [[*climat|temps]] de l'Espagne est plus chaud que celui de la Belgique sur l'année. »",
          "Le climat is het gemiddelde over jaren."),
    keuze("« L'ours polaire est une [[*espèce|espèces]] menacée. »", "Une espèce menacée."),
    keuze("« Elle est complètement [[*guérie|recyclée]] après son opération. »", "Guérir: genezen."),
    keuze("« Le sapin est un [[*conifère|arbre qui perd ses feuilles]] : il reste vert toute l'année. »", "Un conifère blijft groen."),
    keuze("« Cette année, la [[*récolte|toux]] de pommes est très bonne. »", "Une récolte: een oogst."),
    keuze("« Je paie [[*en espèces|en espèce menacée]]. » Ik betaal contant.", "En espèces: contant."),
    tabel("Is deze zin juist (gezondheid en natuur)?", [
        ("J'ai de la fièvre et de la toux.", J), ("J'ai mal dans ma ventre douleur.", F),
        ("Nous devons planter plus d'arbres.", J), ("La pollution est très durable pour la planète.", F),
    ], "J'ai mal au ventre; vervuiling is nooit duurzaam."),
    tabel("Is dit goed voor het milieu?", [
        ("recycler les bouteilles", J), ("abattre les forêts", F), ("utiliser les énergies renouvelables", J), ("le gaspillage", F),
    ], "Recyclen en hernieuwbare energie helpen; kappen en verspilling niet."),
    inv("Hoe zeg je de oogst in het Frans? Twee woorden.", ["la récolte", "la recolte"], "La récolte."),
    sleep("La santé [[mentale]] concerne ton esprit, la santé [[physique]] concerne ton corps.",
          ["durable", "sauvage"], "Mentaal tegenover lichamelijk."),
    open_("Geef in het Frans twee dingen die je kan doen om je empreinte carbone kleiner te maken.",
          "Je vais à l'école à vélo et je recycle mes déchets.",
          "Minder uitstoot: fietsen, recyclen, minder verspillen."),
]

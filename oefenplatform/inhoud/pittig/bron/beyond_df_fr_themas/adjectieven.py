"""Bijvoeglijke naamwoorden, bijwoorden en voorzetsels — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis l'annonce.\n\n« À vendre : une belle petite maison blanche, près de la gare. Le jardin est plus grand que celui des voisins. "
        "C'est la maison la moins chère du quartier ! La cuisine est vieille, mais elle fonctionne vraiment bien. "
        "Grâce à la gare, vous allez rapidement en ville en train. Visite chez nous, le samedi. »",
        [
            keuze("« une belle petite maison blanche » : blanche staat [[*achter|voor]] het naamwoord omdat het een kleur is.", "Kleuren staan achteraan."),
            keuze("« plus grand que » is een [[*comparatif|superlatif]].", "Plus ... que."),
            keuze("« la moins chère du quartier » is een [[*superlatif|comparatif]].", "Lidwoord + moins + de."),
            keuze("« Grâce à la gare » betekent [[*dankzij het station|ondanks het station]].", "Grâce à iets goeds."),
            keuze("« rapidement » is een [[*bijwoord|bijvoeglijk naamwoord]].", "Rapide + -ment."),
        ],
    ),
    tabel("Is de vrouwelijke vorm juist?", [
        ("heureux → heureuse", J), ("blanc → blanque", F), ("sportif → sportive", J), ("vieux → vieuse", F),
    ], "Blanc → blanche; vieux → vieille."),
    sorteer("Staat het bijvoeglijk naamwoord meestal voor of achter het naamwoord?", ["voor", "achter"], [
        ["petit", "voor"], ["rouge", "achter"], ["jeune", "voor"], ["intéressant", "achter"], ["joli", "voor"], ["français", "achter"],
    ], "Korte woorden zoals petit, jeune en joli gaan voorop; kleuren en lange woorden erachter."),
    koppel("Koppel elk bijvoeglijk naamwoord aan zijn bijwoord.", [
        ["lent", "lentement"], ["doux", "doucement"], ["vrai", "vraiment"], ["bon", "bien"],
    ], ["bonnement"], "Bon geeft bien."),
    koppel("Koppel elk voorzetsel aan zijn betekenis.", [
        ["malgré", "ondanks"], ["sous", "onder"], ["entre", "tussen"], ["pendant", "tijdens"],
    ], ["sinds"], "Sinds is depuis."),
    mk("« Ce film est ___ que l'autre. » Hij is beter. Wat past?",
       ["meilleur", "plus bon", "mieux", "le meilleur film"], 0, "Bon wordt meilleur."),
    mk("« Elle chante ___ que sa sœur. » Ze zingt beter. Wat past?",
       ["mieux", "meilleur", "plus bien", "meilleure"], 0, "Bij een werkwoord: mieux."),
    mk("« Mon frère est ___ grand que moi. » Ze zijn even groot. Wat past?",
       ["aussi", "autant", "plus", "moins"], 0, "Aussi ... que bij een bijvoeglijk naamwoord."),
    mk("« Il est en retard ___ la neige. » Wat past?",
       ["à cause de", "grâce à", "pour que la", "pendant que"], 0, "Iets slechts: à cause de."),
    mk("« Nous allons ___ Portugal cet été. » Wat past?",
       ["au", "en", "à", "aux"], 0, "Le Portugal is mannelijk: au."),
    mk("Hoe zeg je « Ik ga met de fiets naar school »?",
       ["Je vais à l'école à vélo.", "Je vais à l'école en vélo.", "Je vais à l'école par vélo.", "Je vais à l'école sur vélo."], 0,
       "Je zit erop: à vélo."),
    inv("Vul in: « C'est la ___ belle ville du pays. » Eén woord.", ["plus"], "La plus belle."),
    inv("Maak een bijwoord van « heureux ». Eén woord.", ["heureusement"], "Heureuse + -ment."),
    inv("Vul in: « Le chat dort ___ la table. » (onder) Eén woord.", ["sous"], "Sous: onder."),
    inv("Vul in: « J'habite ___ Belgique. » Eén woord.", ["en"], "La Belgique is vrouwelijk."),
    keuze("« Des garçons [[*heureux|heureuxs]]. »", "Woorden op -x veranderen niet in het meervoud."),
    keuze("« Les équipes [[*nationales|nationaux]]. »", "Vrouwelijk meervoud: -ales."),
    keuze("« Elle a des yeux [[*bleu clair|bleus clairs]]. »", "Een kleur van twee woorden verandert niet."),
    keuze("« J'ai [[*bien|bon]] dormi. »", "Bijwoord voor het deelwoord."),
    keuze("« Il mange [[*beaucoup|très]]. »", "Beaucoup bij een werkwoord."),
    keuze("« Mes amies sont [[*très|beaucoup]] contentes. »", "Très bij een bijvoeglijk naamwoord."),
    tabel("Is de zin juist (vergelijking en bijwoorden)?", [
        ("Il est moins rapide que moi.", J), ("C'est le plus bon gâteau.", F),
        ("Elles parlent lentement.", J), ("Le père et la mère sont contentes.", F),
    ], "Le meilleur gâteau; een gemengde groep is mannelijk: contents."),
    tabel("Is dit een plaatsvoorzetsel?", [
        ("derrière", J), ("pendant", F), ("sur", J), ("depuis", F),
    ], "Achter en op geven een plaats; tijdens en sinds een tijd."),
    sleep("J'ai [[envie de]] partir en vacances, mais j'ai [[besoin d']] argent.",
          ["envie à", "besoin à"], "Avoir envie de, avoir besoin de."),
    inv("Vul in: « Mes clés sont ___ mon lit. » (op) Eén woord.", ["sur"], "Sur: op; sous: onder."),
    open_("Leg in het Nederlands het verschil uit tussen « un ancien élève » en « un meuble ancien ».",
          "Vooraan betekent ancien vroeger (een oud-leerling), achteraan betekent het oud (een antiek meubel).",
          "De plaats verandert de betekenis."),
]

"""Woordvelden wetenschap, techniek en taal — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le message du club de l'école.\n\n« Club sciences et sport – cette semaine\n"
        "Lundi : nous faisons une expérience au labo. Apportez votre ordinateur portable, mais vérifiez que la batterie est rechargée !\n"
        "Mercredi : match de foot contre l'école Saint-Joseph sur le grand terrain. Notre entraîneur sera là.\n"
        "Vendredi : jeux de société au local du club. Après, on prend un pot ensemble. »",
        [
            keuze("Op maandag doen ze een [[*proef in het labo|ervaring opdoen op het veld]].", "Une expérience: een proef."),
            keuze("Je moet nakijken of je batterij [[*opgeladen|uitgeschakeld]] is.", "Rechargée."),
            keuze("« Notre entraîneur » is [[*onze trainer|onze scheidsrechter|onze doelman]].", "S'entraîner: trainen."),
            keuze("« prendre un pot » betekent [[*iets gaan drinken|een pot kopen]].", "Prendre un pot."),
            mk("Wat doen ze op vrijdag?",
               ["gezelschapsspellen spelen", "een proef in het labo met hun laptop", "voetballen tegen een andere school", "een wandeltocht maken in het bos"], 0,
               "Jeux de société."),
        ],
    ),
    sorteer("Typisch Belgisch Frans of gewoon Frans uit Frankrijk?", ["België", "Frankrijk"], [
        ["septante", "België"], ["soixante-dix", "Frankrijk"], ["nonante", "België"], ["quatre-vingt-dix", "Frankrijk"],
        ["le dîner (middagmaal)", "België"], ["le déjeuner (middagmaal)", "Frankrijk"],
    ], "Septante, nonante en le dîner voor het middagmaal zijn Belgisch."),
    koppel("Koppel elke Franse valse vriend aan zijn echte betekenis.", [
        ["la journée", "de dag"], ["actuellement", "momenteel"], ["une pile", "een batterij"], ["la location", "de huur"],
    ], ["eigenlijk"], "Eigenlijk is en fait."),
    koppel("Koppel elk computerwoord aan zijn betekenis.", [
        ["le clavier", "het toetsenbord"], ["la souris", "de muis"], ["un logiciel", "software"], ["un écran tactile", "een aanraakscherm"],
    ], ["een pan"], "Une casserole is een pan."),
    mk("Hoe zeg je « Mijn auto is stuk »?",
       ["Ma voiture est en panne.", "Ma voiture est en pile.", "Ma voiture est une casserole.", "Ma voiture a une panne de pied."], 0,
       "En panne: defect."),
    mk("« N'oublie pas d'___ le fichier avant de fermer l'ordinateur ! » Wat past?",
       ["enregistrer", "télécharger vers", "s'entraîner", "recharger"], 0, "Enregistrer: opslaan."),
    mk("Wat is het tegengestelde van « possible »?",
       ["impossible", "inpossible", "dépossible", "nonpossible"], 0, "Voor p wordt in- im-."),
    mk("Wat betekent « relire » ?",
       ["opnieuw lezen", "niet meer lezen", "voorlezen aan iemand", "slecht lezen"], 0, "Re-: opnieuw."),
    mk("Van welk werkwoord komt « la construction »?",
       ["construire", "conduire", "constater", "consommation"], 0, "Construire geeft la construction."),
    mk("Welk woord is spreektaal voor « un livre »?",
       ["un bouquin", "un roman", "un chapitre", "un logiciel"], 0, "Un bouquin is familier."),
    inv("Vul in: « Un ___ de passe ». (wachtwoord) Eén woord.", ["mot"], "Un mot de passe."),
    inv("Hoe zeg je scheidsrechter in het Frans? Eén woord, zonder lidwoord.", ["arbitre"], "Un arbitre."),
    inv("Hoe zeg je ploeg in het Frans? Eén woord, zonder lidwoord.", ["équipe"], "Une équipe."),
    inv("Maak een woord voor iemand die werkt, met het achtervoegsel -eur. Eén woord.", ["travailleur"], "Travailler geeft un travailleur."),
    keuze("« Thé [[*ou|où]] café ? »", "Ou is of; où is waar."),
    keuze("« [[*Où|Ou]] habites-tu ? »", "Où: waar."),
    keuze("« Une maisonn[[*ette|asse]] est une petite maison. »", "-ette maakt kleiner."),
    keuze("« Je fais [[*du|de la]] vélo le samedi. »", "Faire du vélo."),
    keuze("« Les chercheurs font de la [[*recherche|recherches de pile]] sur le climat. »", "La recherche: onderzoek."),
    tabel("Is deze zin juist (taal en techniek)?", [
        ("Actuellement, je travaille à Namur.", J), ("Je dois recharger mon téléphone.", J),
        ("Un arbitre est le gardien de l'équipe.", F), ("Une pile est un grand plat.", F),
    ], "Un arbitre is de scheidsrechter; une pile is een batterij of een stapel."),
    tabel("Is dit een synoniem van « grand »?", [
        ("vaste", J), ("petit", F), ("énorme", J), ("minuscule", F),
    ], "Een synoniem heeft bijna dezelfde betekenis."),
    sleep("Pour te connecter, tu as besoin d'un [[mot de passe]]. Ensuite, tu peux [[télécharger]] le fichier.",
          ["arbitre", "terrain"], "Un mot de passe; télécharger: downloaden."),
    open_("Leg in het Nederlands uit waarom « la journée » een valse vriend is.",
          "Het lijkt op journaal of reis, maar het betekent de dag.",
          "La journée: de hele dag."),
    inv("Schrijf 90 zoals men het in België zegt. Eén woord.", ["nonante"], "In Frankrijk: quatre-vingt-dix."),
    keuze("« Je vais faire [[*de la|du]] natation. »", "Faire de la natation."),
    keuze("« vert », « verre » en « vers » zijn [[*homophones|synonymes]].", "Ze klinken gelijk, maar betekenen iets anders."),
]

"""Woordvelden school, werk, geld en verkeer — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis l'offre d'emploi.\n\n« OFFRE D'EMPLOI – Vendeur ou vendeuse (temps partiel, 20 heures par semaine)\n"
        "Notre librairie au centre-ville cherche quelqu'un pour aider les clients, travailler à la caisse et ranger les rayons. "
        "Compétences : vous êtes aimable, vous parlez français et néerlandais, et vous aimez travailler en équipe. Pas besoin de diplôme. "
        "Salaire : 12 euros de l'heure, et une réduction de 20 % sur tous les livres. "
        "Envoyez votre CV et une lettre de motivation avant la date limite du 15 juin. »",
        [
            keuze("Het gaat om een [[*deeltijdse|voltijdse]] job.", "Temps partiel."),
            keuze("« travailler à la caisse » betekent werken aan [[*de kassa|het rek|de deur]].", "La caisse: de kassa."),
            mk("Wat moet je hebben om te mogen solliciteren?",
               ["geen diploma", "een universitair diploma", "een rijbewijs voor de bestelwagen", "drie jaar ervaring in een boekhandel"], 0,
               "Pas besoin de diplôme."),
            keuze("Personeel krijgt [[*korting|rente|een lening]] op alle boeken.", "Une réduction."),
            inv("Tot welke datum kan je solliciteren? Schrijf de dag en de maand in het Nederlands, bv. 3 mei.", ["15 juni"],
                "La date limite du 15 juin."),
        ],
    ),
    sorteer("Hoort het bij school of bij het verkeer?", ["school", "verkeer"], [
        ["un horaire", "school"], ["un rond-point", "verkeer"], ["un bulletin", "school"],
        ["un piéton", "verkeer"], ["les devoirs", "school"], ["un embouteillage", "verkeer"],
    ], "Rooster, rapport en huiswerk tegenover rotonde, voetganger en file."),
    koppel("Koppel elk Frans woord over winkelen aan zijn betekenis.", [
        ["un ticket de caisse", "een kassabon"], ["une recette", "een recept om te koken"], ["rembourser", "terugbetalen"], ["une bonne affaire", "een koopje"],
    ], ["de btw"], "La TVA is de btw."),
    koppel("Koppel elk Frans verkeerswoord aan zijn betekenis.", [
        ["l'essence", "benzine"], ["un camion", "een vrachtwagen"], ["une autoroute", "een snelweg"], ["le trottoir", "het voetpad"],
    ], ["een bestelwagen"], "Een bestelwagen is une camionnette."),
    mk("« Je ne peux pas me ___ un nouveau téléphone. C'est trop cher. » Wat past?",
       ["permettre", "rembourser", "postuler", "licencier"], 0, "Se permettre: kunnen betalen."),
    mk("« Elle a ___ son examen, donc elle a son diplôme. » Wat past?",
       ["réussi", "passé sans réussir", "échoué", "pris des notes pour"], 0, "Réussir: slagen. Passer is afleggen."),
    mk("Tom verloor zijn job omdat de fabriek sloot. Hoe zeg je dat?",
       ["Il a été licencié.", "Il a eu une promotion.", "Il a postulé pour un emploi.", "Il a respecté la date limite."], 0,
       "Licencié: ontslagen."),
    mk("Waar steek je veilig over als voetganger?",
       ["sur le passage pour piétons", "sur l'autoroute", "midden op le rond-point", "tussen de auto's in un embouteillage"], 0, "Een zebrapad."),
    mk("Je reed te snel en de politie houdt je tegen. Wat krijg je?",
       ["une amende", "une réduction", "un remboursement", "une bonne affaire"], 0, "Une amende: een boete."),
    mk("« Je prends le train pour Bruxelles chaque jour pour travailler. » Wat doet deze persoon?",
       ["pendelen", "solliciteren", "vakantiewerk doen", "stage lopen"], 0, "Faire la navette."),
    inv("Hoe zeg je klant in het Frans? Eén woord, zonder lidwoord.", ["client", "cliente"], "Un client."),
    inv("Hoe zeg je vak op school in het Frans? Eén woord, zonder lidwoord.", ["matière"], "Une matière."),
    inv("Hoe zeg je voetganger in het Frans? Eén woord, zonder lidwoord.", ["piéton"], "Un piéton."),
    inv("Hoe zeg je file in het verkeer in het Frans? Eén woord, zonder lidwoord.", ["embouteillage", "bouchon"], "Un embouteillage."),
    keuze("« Demain, je [[*passe|réussis]] un examen de maths. J'espère réussir ! »", "Passer un examen: afleggen."),
    keuze("« Mon [[*collègue|camarade de classe]] au bureau m'aide avec l'ordinateur. »", "Een collega op het werk."),
    keuze("« Je peux payer [[*par carte|en carte par]] ? » « Bien sûr. »", "Payer par carte; contant is en espèces."),
    keuze("« Nous étions dans un embouteillage à l'heure de [[*pointe|récréation]]. »", "L'heure de pointe: het spitsuur."),
    keuze("« Les prix sont TVA [[*comprise|remboursée]]. »", "TVA comprise: btw inbegrepen."),
    tabel("Is deze zin juist (school, werk en geld)?", [
        ("Je dois respecter la date limite.", J), ("Il a été licencié, donc il a une promotion.", F),
        ("Il a payé en espèces.", J), ("Je postule pour un emploi.", J),
    ], "Licencié is ontslagen, geen promotie."),
    tabel("Is dit een beroep?", [
        ("un plombier", J), ("une récréation", F), ("un infirmier", J), ("un horaire", F),
    ], "Loodgieter en verpleger zijn beroepen."),
    inv("Vul in: « Je cherche un ___ d'été. » (een vakantiejob) Eén woord.", ["job", "emploi", "travail"], "Un job d'été."),
    volgorde("Zet de stappen om een job te vinden in de juiste volgorde.", [
        "une offre d'emploi vinden", "je CV en een lettre de motivation sturen", "un entretien hebben", "de job krijgen",
    ], "Eerst zoeken, dan solliciteren, dan het gesprek."),
    sleep("J'ai acheté cette veste pendant [[les soldes]]. C'était une vraie [[bonne affaire]] : seulement dix euros !",
          ["une amende", "un prêt"], "Les soldes: de koopjes; une bonne affaire: een koopje."),
    open_("Leg in het Nederlands uit waarom « passer un examen » een valse vriend is.",
          "Het lijkt op slagen, maar het betekent een examen afleggen. Slagen is réussir.",
          "Een klassieke valse vriend."),
    mk("Wat is « un stage »?",
       ["een stage", "een vaste job", "een werkloosheidsuitkering", "een collega op het werk"], 0, "Un stagiaire doet een stage."),
]

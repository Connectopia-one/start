"""Woordvelden: school, werk en de professionele wereld — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen met de woorden uit het gewone hoofdstuk: school en rapport,
beroepen, stage en studentenjob, computer en internet, sport en vrije tijd,
aangevuld met enkele vragen uit Frans Beyond dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import school as _s, wetenschap as _w

T1 = ("Lis le bulletin.\n\n"
      "« Bulletin du deuxième trimestre — Français : 12/20. Mathématiques : 9/20. Sciences : 15/20. "
      "Néerlandais : 17/20. Éducation physique : 16/20.\n"
      "Remarque du titulaire : Bon trimestre, mais attention aux maths. Il faut faire tous les devoirs. »")

T2 = ("Lis l'offre.\n\n"
      "« Supermarché Bio cherche étudiant(e) pour les vacances de Pâques. Tâches : ranger les rayons et aider à la caisse. "
      "Horaire : de 9 h à 15 h, du lundi au vendredi. Salaire : 11 euros de l'heure. Expérience non exigée. "
      "Envoyez votre CV et une petite lettre par mail. Entretien la semaine du 10 mars. »")

VRAGEN = [_s.VRAGEN[i] for i in (10, 11, 15, 21, 22)] + [_w.VRAGEN[i] for i in (10, 12, 17, 24)] + [
    casus(T1, [
        inv("Wat is het beste cijfer op dit rapport? Schrijf als 17/20.", ["17/20", "17"],
            "Néerlandais : 17/20."),
        keuze("Het zwakste vak is [[*wiskunde|Frans|wetenschappen]].",
              "Mathématiques : 9/20."),
        keuze("« Remarque du titulaire » is [[*de opmerking van de klastitularis|het cijfer van de leraar|de handtekening van de ouders]].",
              "Une remarque: een opmerking. Een cijfer is une note."),
        tabel("Klopt dit volgens het rapport?",
              [("Het rapport gaat over het tweede trimester.", J), ("De titularis vraagt om alle taken te maken.", J), ("De leerling haalde voor elk vak meer dan de helft.", F)],
              "Voor wiskunde: 9 op 20."),
    ]),
    casus(T2, [
        mk("Wat zoekt de supermarkt?",
           ["een student voor de paasvakantie", "een kassier met veel ervaring", "een leraar voor de zomer", "een klant voor biologische producten"], 0,
           "Cherche étudiant(e) pour les vacances de Pâques."),
        inv("Hoeveel uur werk je per dag? Schrijf enkel het getal.", ["6", "zes"],
            "Van 9 tot 15 uur is zes uur."),
        inv("Hoeveel euro verdien je op één dag? Schrijf enkel het getal.", ["66"],
            "Zes uur maal 11 euro is 66 euro."),
        keuze("« Expérience non exigée » betekent dat ervaring [[*niet nodig is|verplicht is|betaald wordt]].",
              "Exiger: eisen."),
        keuze("« Envoyez votre CV » betekent [[*stuur je cv|vul je cv in|lees je cv]].",
              "Envoyer: sturen. Invullen is remplir."),
    ]),
    tabel("Is dit een beroep?",
          [("un coiffeur", J), ("une infirmière", J), ("un bureau", F), ("un cuisinier", J)],
          "Un bureau is een bureau of een kantoor."),
    keuze("Een vrouw die verkoopt is une [[*vendeuse|vendeur|vendeure]].",
          "Un vendeur, une vendeuse."),
    keuze("« Je voudrais devenir [[*boulanger|un boulanger|le boulanger]]. »",
          "Na devenir en être komt de beroepsnaam zonder lidwoord."),
    keuze("« Il est au [[*chômage|travail]] » betekent dat hij werkloos is.",
          "Un ouvrier is een arbeider; au chômage is werkloos."),
    koppel("Koppel elk woord uit de professionele wereld aan zijn betekenis.",
           [("un salaire", "het loon"), ("un contrat", "het contract"), ("un entretien", "het sollicitatiegesprek"), ("un stage", "de stage")], ["het rapport"],
           "Het rapport is le bulletin."),
    tabel("Klopt dit over computer en internet?",
          [("se connecter: inloggen", J), ("un écran: een scherm", J), ("un courriel: een telefoongesprek", F), ("un ordinateur: een computer", J)],
          "Un courriel is een mail."),
    sorteer("Jouer of faire?", ["jouer", "faire"],
            [("___ au basket", "jouer"), ("___ du vélo", "faire"), ("___ de la guitare", "jouer"), ("___ de la natation", "faire")],
            "Jouer à een sport of spel, jouer de een instrument; faire du vélo, faire de la natation."),
    keuze("« J'aime [[*nager|nage|nagé]]. »",
          "Na aimer komt de infinitief."),
    keuze("« Je suis en [[*quatrième|quatre]] année. »",
          "Être en + rangtelwoord + année."),
    mk("Je solliciteert met een mail voor een studentenjob. Wat zet je er zeker in?",
       ["wanneer je kan werken", "het loon van je ouders", "je punten van vorig jaar", "je mening over de winkel"], 0,
       "Wie je bent, wanneer je kan werken en waarom je de job wil."),
    tabel("Hoort het bij school?",
          [("un devoir", J), ("un cours", J), ("un loyer", F), ("une interrogation", J)],
          "Un loyer is de huurprijs; une interrogation is een overhoring."),
    keuze("« Un match » en « une équipe » horen bij [[*sport|muziek|school]]: een wedstrijd en een ploeg.",
          "Un joueur is een speler, un entraîneur een trainer."),
]

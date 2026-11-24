"""Een Franse tekst begrijpen — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Korte teksten uit het dagelijkse leven met vragen naar onderwerp, hoofdgedachte,
details en verwijswoorden. Een deel van de leesvragen komt uit Frans Beyond
dubbele finaliteit (zelfde soort teksten), aangevuld met eigen teksten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import lezen as _l

T1 = ("Lis le message de l'école.\n\n"
      "« Chers élèves de quatrième, le stage en entreprise commence le lundi 3 février et dure deux semaines. "
      "Vous travaillez de 8 h 30 à 16 h 30, mais le mercredi, vous terminez à midi. "
      "N'oubliez pas votre carnet de stage : votre responsable le signe chaque vendredi. "
      "Si vous êtes malade, téléphonez d'abord à l'entreprise, ensuite à l'école. "
      "Le dernier jour, vous présentez votre stage en classe. Bon travail ! »")

T2 = ("Lis l'annonce.\n\n"
      "« Le camping Les Pins cherche un ou une jeune pour juillet et août. Tu as 16 ans ou plus ? "
      "Tu parles néerlandais et un peu de français ? Tu aides à l'accueil le matin et au bar l'après-midi. "
      "Tu travailles cinq jours par semaine, jamais le lundi. Logement gratuit sur le camping, repas compris. "
      "Envoie un petit message avec ta photo avant le 30 avril. »")

VRAGEN = [_l.VRAGEN[i] for i in (0, 1, 2, 3, 5, 8, 9, 13, 16)] + [
    casus(T1, [
        mk("Wat is het onderwerp van het bericht?",
           ["de afspraken voor de stage", "een uitstap met de klas", "de punten van het rapport", "een vergadering voor ouders"], 0,
           "Le stage en entreprise: de stage in een bedrijf."),
        inv("Hoe lang duurt de stage? Schrijf het aantal weken als getal.", ["2", "twee"],
            "Dure deux semaines: duurt twee weken."),
        tabel("Klopt dit volgens het bericht?",
              [("Op woensdag stop je om twaalf uur.", J), ("Je verantwoordelijke tekent je stageboekje elke vrijdag.", J), ("Ben je ziek, dan bel je eerst de school.", F), ("Op de laatste dag stel je je stage voor in de klas.", J)],
              "D'abord à l'entreprise, ensuite à l'école: eerst het bedrijf, dan de school."),
        keuze("« le » in « votre responsable le signe » verwijst naar [[*het stageboekje|de vrijdag|het bedrijf]].",
              "Le vervangt le carnet de stage."),
        keuze("« Vous terminez à midi » betekent dat je om twaalf uur [[*stopt|begint|eet]].",
              "Terminer: eindigen, stoppen."),
    ]),
    casus(T2, [
        mk("Voor wie is deze advertentie bedoeld?",
           ["een jongere die vakantiewerk zoekt", "een gezin dat wil komen kamperen", "een kok die een restaurant opent", "een leerling die Nederlands wil leren"], 0,
           "Le camping cherche un ou une jeune: de camping zoekt een jongere."),
        tabel("Klopt dit volgens de advertentie?",
              [("Je moet minstens zestien jaar zijn.", J), ("Je werkt 's morgens aan het onthaal.", J), ("Je werkt elke dag, ook op maandag.", F), ("Je slaapt gratis op de camping.", J)],
              "Jamais le lundi: nooit op maandag."),
        keuze("« repas compris » betekent dat de maaltijden [[*inbegrepen zijn|extra betaald worden|niet mogen]].",
              "Compris: inbegrepen."),
        inv("Tot welke datum kan je reageren? Schrijf als dag en maand in cijfers, zoals 30/4.", ["30/4", "30/04", "30 april", "30-4"],
            "Avant le 30 avril."),
        mk("Wat stuur je mee met je bericht?",
           ["een foto van jezelf", "een brief van je school", "je rapport van vorig jaar", "een bewijs dat je kan zwemmen"], 0,
           "Envoie un petit message avec ta photo."),
    ]),
    mk("Lees: « Nous avons attendu le bus pendant une heure, alors nous sommes rentrés à pied. » Wat gebeurde er?",
       ["Ze zijn te voet naar huis gegaan.", "Ze hebben een uur op de bus gezeten.", "De bus heeft hen thuis afgezet.", "Ze zijn met de fiets naar huis gereden."], 0,
       "Rentrer à pied: te voet naar huis gaan. Alors geeft het gevolg."),
    inv("Lees: « Le magasin ouvre à 9 h 30 et ferme deux heures plus tard pour le repas de midi. » Om hoe laat sluit de winkel voor het middagmaal? Schrijf als 11.30.", ["11.30", "11:30", "11u30", "11 h 30"],
        "9.30 plus twee uur is 11.30."),
    tabel("Lees: « Ma sœur adore le sport. Elle joue au foot le mardi et elle nage le samedi. Moi, je préfère la musique. » Klopt dit?",
          [("De zus voetbalt op dinsdag.", J), ("De schrijver zwemt op zaterdag.", F), ("De schrijver houdt meer van muziek.", J)],
          "Elle nage le samedi: zij, de zus, zwemt."),
]

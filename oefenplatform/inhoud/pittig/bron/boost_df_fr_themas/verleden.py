"""Passé composé, imparfait en passé récent — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over de verleden tijden uit Frans Beyond dubbele finaliteit (zonder de
deelwoorden en gebruiken die hier niet in de leerstof staan), aangevuld met eigen
vragen over het verslag van een stage of een weekend."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import verleden as _v

T1 = ("Lis le rapport de stage de Lucas.\n\n"
      "« Pendant mon stage, je travaillais dans un garage. Chaque matin, je nettoyais les outils et j'aidais le mécanicien. "
      "Le troisième jour, un client est arrivé avec une voiture en panne. Le patron m'a montré comment changer un pneu. "
      "Le dernier jour, nous sommes allés manger une pizza avec toute l'équipe. Je viens de recevoir mon évaluation : 16 sur 20 ! »")

VRAGEN = [_v.VRAGEN[i] for i in (0, 1, 4, 5, 6, 7, 8, 9, 11, 13, 14, 17, 18, 19, 22, 25)] + [
    casus(T1, [
        keuze("« je nettoyais les outils » staat in de imparfait, want het gebeurde [[*elke dag|één keer]].",
              "Chaque matin: gewoonte."),
        keuze("« un client est arrivé » staat in de passé composé, want het is [[*één gebeurtenis|een gewoonte]].",
              "Le troisième jour: één keer."),
        keuze("« Je viens de recevoir » betekent dat hij zijn evaluatie [[*net gekregen heeft|morgen krijgt]].",
              "Venir de + infinitief: de passé récent."),
        keuze("« nous sommes allés » krijgt -s omdat [[*het onderwerp meervoud is en aller met être gaat|het lijdend voorwerp meervoud is]].",
              "Met être past het deelwoord zich aan het onderwerp aan."),
    ]),
    keuze("« Hier, nous [[*avons fait|sommes faits]] nos devoirs. »",
          "Faire gaat met avoir."),
    keuze("« Je suis [[*née|né]] en 2010 », schrijft Lisa.",
          "Met être: een e voor een meisje."),
    keuze("« Quand j'étais petit, nous [[*habitions|avons habité]] à la campagne. »",
          "Een toestand van vroeger: imparfait."),
    keuze("« Nous [[*regardions|avons regardé]] la télévision quand le téléphone [[*a sonné|sonnait]]. »",
          "De bezigheid in de imparfait, wat erin valt in de passé composé."),
    keuze("« Elle vient [[*d'|de]] arriver. »",
          "De wordt d' voor een klinker."),
    tabel("Imparfait of passé composé in een verslag over je stage?",
          [("wat je elke dag deed", "imparfait"), ("hoe het weer was", "imparfait"), ("wat er die ene vrijdag gebeurde", "passé composé"), ("wanneer je stage begon", "passé composé")],
          "Gewoonte en decor in de imparfait, losse gebeurtenissen in de passé composé.",
          kolommen=["imparfait", "passé composé"]),
]

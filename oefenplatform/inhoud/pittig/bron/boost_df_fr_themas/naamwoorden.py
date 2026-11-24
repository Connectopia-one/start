"""Zelfstandige naamwoorden, lidwoorden en determinanten — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over lidwoorden, meervoud, aanwijzende, bezittelijke en vragende woorden
en getallen uit Frans Beyond dubbele finaliteit (zelfde leerstof), aangevuld met
eigen vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import determinanten as _d

VRAGEN = [_d.VRAGEN[i] for i in (0, 1, 2, 3, 4, 6, 8, 10, 11, 12, 14, 18, 19, 20, 22, 23, 24)] + [
    casus("Lis le message de Tom.\n\n« Salut Max ! Ce soir, je vais au match avec mon père et ma cousine. "
          "Nous n'avons pas de billets, mais mon oncle travaille au stade. Après, nous allons manger des frites et boire du coca. "
          "Tu viens avec nous ? Quelle heure te va ? »", [
        keuze("« au match » is samengetrokken uit [[*à + le|à + la|de + le]].",
              "À + le wordt au."),
        keuze("« Nous n'avons pas [[*de|des]] billets » : na een ontkenning wordt des de.",
              "Pas de billets."),
        keuze("Tom schrijft « ma cousine » omdat [[*cousine vrouwelijk is|Tom een meisje is]].",
              "Het geslacht van het bezit telt."),
        keuze("« du coca » is een [[*deelaanduidend lidwoord|bepaald lidwoord|aanwijzend woord]].",
              "Een onbepaalde hoeveelheid: du."),
    ]),
    tabel("Is het meervoud juist?",
          [("un journal → des journaux", J), ("un gâteau → des gâteaux", J), ("un bureau → des bureaus", F), ("un ami → des amis", J)],
          "Op -eau krijgt een x: des bureaux."),
    keuze("« J'aime [[*le|du]] chocolat, et maintenant je mange [[*du|le]] chocolat. »",
          "Le in het algemeen, du voor een deel."),
    keuze("« Je n'aime pas [[*le|de]] café. »",
          "Na een ontkenning blijft het bepaald lidwoord staan."),
    keuze("« [[*Cet|Ce]] homme est mon voisin. »",
          "Voor een stille h wordt ce cet."),
    keuze("« Paul cherche [[*sa|son]] clé et Marie cherche [[*son|sa]] sac. »",
          "Son en sa volgen het woord dat erna komt: une clé, un sac."),
]

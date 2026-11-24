"""Voornaamwoorden: sujet, COD, COI en de wederkerende — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen over onderwerp, lijdend en meewerkend voorwerp, wederkerende
werkwoorden, y en en, met enkele vragen uit Frans Beyond dubbele finaliteit
(zonder de betrekkelijke en aanwijzende voornaamwoorden, die hier niet horen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import voornaamwoorden as _v

T1 = ("Lis le dialogue.\n\n"
      "« — Tu as vu Sarah ce matin ?\n— Oui, je l'ai vue à la gare. Je lui ai donné ton livre.\n"
      "— Merci ! Et tes parents, tu leur as téléphoné ?\n— Pas encore. Je les appelle ce soir.\n"
      "— Tu vas au marché demain ?\n— Oui, j'y vais avec ma sœur. Il nous faut des pommes : on en achète trois kilos. »")

VRAGEN = [_v.VRAGEN[i] for i in (2, 5, 6, 7, 12, 13, 15, 22, 23, 25)] + [
    casus(T1, [
        keuze("« l' » in « je l'ai vue » verwijst naar [[*Sarah|de gare|het boek]].",
              "L' vervangt Sarah, een lijdend voorwerp."),
        keuze("« lui » in « je lui ai donné » betekent [[*aan haar|haar|aan hen]].",
              "Lui: aan hem of aan haar, hier aan Sarah."),
        keuze("« leur » in « tu leur as téléphoné » verwijst naar [[*de ouders|Sarah|de zus]].",
              "Téléphoner à quelqu'un: leur vervangt à + meer personen."),
        keuze("« y » in « j'y vais » vervangt [[*au marché|ma sœur|demain]].",
              "Y vervangt een plaats."),
        keuze("« en » in « on en achète trois kilos » vervangt [[*des pommes|le marché|ma sœur]].",
              "En vervangt een hoeveelheid."),
    ]),
    tabel("Welk onderwerpsvoornaamwoord vervangt het?",
          [("Marie et moi", "nous"), ("mon frère et ma sœur", "ils"), ("Lisa et Emma", "elles"), ("toi et ton ami", "vous")],
          "Eén mannelijk woord erbij maakt ils.",
          kolommen=["nous", "vous", "ils", "elles"]),
    keuze("« En Belgique, [[*on|nous]] parle trois langues. »",
          "On: men, met dezelfde vorm als il."),
    tabel("COD of COI?",
          [("Je regarde la télé.", "COD"), ("J'écris à ma grand-mère.", "COI"), ("Il aide son ami.", "COD"), ("Elle téléphone à son père.", "COI")],
          "Een COI staat na à; een COD zonder voorzetsel.",
          kolommen=["COD", "COI"]),
    keuze("« Tu connais mon frère ? — Oui, je [[*le|lui]] connais. »",
          "Connaître iemand: COD, dus le."),
    keuze("« Tu parles à tes cousins ? — Oui, je [[*leur|les|leurs]] parle. »",
          "Leur vervangt à + meer personen en krijgt nooit een s."),
    keuze("« Tu peux [[*m'|me]] aider ? »",
          "Me wordt m' voor een klinker."),
    keuze("« Elle [[*me|moi]] donne son numéro. »",
          "Me is hier een meewerkend voorwerp: aan mij."),
    volgorde("Zet de woorden in de juiste volgorde: « le / lui / je / donne »",
             ["je", "le", "lui", "donne"],
             "COD voor COI, allebei voor het werkwoord."),
    keuze("« Donne-[[*le|lui]]-moi ! » betekent geef het me.",
          "In een bevestigend bevel staan de voornaamwoorden achter het werkwoord."),
    tabel("Is de vorm van het wederkerend werkwoord juist?",
          [("je me lave", J), ("nous levons", F), ("tu t'appelles", J), ("ils se parlent", J)],
          "In de wij-vorm: nous nous levons."),
    keuze("« Il lave la voiture » : hij wast [[*iets anders|zichzelf]]. « Il se lave » : hij wast [[*zichzelf|iets anders]].",
          "Se maakt het wederkerend."),
    keuze("« On [[*se|nous]] voit demain ! » betekent we zien elkaar morgen.",
          "Een wederkerend werkwoord kan ook elkaar betekenen."),
    keuze("« Tu as des sœurs ? — Oui, j'[[*en|y]] ai deux. »",
          "En vervangt des sœurs."),
    tabel("Is het verwijswoord juist gebruikt?",
          [("J'en ai assez.", J), ("On y va !", J), ("Je y vais.", F), ("Il en parle souvent.", J)],
          "Voor een klinker wordt je j': j'y vais."),
    keuze("Het onderwerp mag in het Frans [[*nooit wegvallen|soms wegvallen]]: je parle, nooit enkel parle.",
          "Anders dan in het Spaans of het Latijn."),
]

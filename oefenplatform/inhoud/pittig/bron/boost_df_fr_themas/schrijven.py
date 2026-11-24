"""Schrijven, schriftelijke interactie en leesbeleving — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over mails, berichten, zoekertjes en verslagen uit Frans Beyond dubbele
finaliteit, aangevuld met eigen vragen over de beoordelingsrijen en over wat je
schrijft bij een literaire tekst."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import schrijven as _s

T1 = ("Lis le message de Jonas sur le stage.\n\n"
      "« Le mois passé, j'ai fait mon stage dans une boulangerie. D'abord, j'ai appris à faire des croissants. "
      "Ensuite, j'ai aidé au magasin. Les clients étaient gentils, mais je devais me lever à cinq heures ! "
      "Enfin, le dernier jour, mon patron m'a donné un cadeau. À mon avis, c'était un très bon stage parce que j'ai beaucoup appris. »")

VRAGEN = [_s.VRAGEN[i] for i in (0, 1, 2, 3, 5, 7, 10, 11, 12, 13, 17, 18, 23, 24, 25)] + [
    casus(T1, [
        keuze("Jonas schrijft over zijn stage vooral in de [[*verleden tijden|toekomende tijd]].",
              "J'ai fait, j'ai appris, étaient: passé composé en imparfait."),
        sleep("De woorden [[D'abord]], [[Ensuite]] en [[Enfin]] maken de orde van zijn verhaal duidelijk.",
              ["Parce que", "Mais"], "Eerst, daarna, tot slot."),
        keuze("« À mon avis » kondigt [[*zijn mening|een feit|een vraag]] aan.",
              "À mon avis: naar mijn mening."),
        keuze("Hij geeft een reden voor zijn mening met [[*parce que|d'abord|mais]].",
              "Parce que j'ai beaucoup appris."),
        tabel("Klopt dit volgens het bericht van Jonas?",
              [("Jonas deed zijn stage in een bakkerij.", J), ("Hij moest om vijf uur opstaan.", J), ("De klanten waren onvriendelijk.", F)],
              "Les clients étaient gentils: vriendelijk."),
    ]),
    tabel("Hoort dit in een zoekertje om je gsm te verkopen?",
          [("wat je verkoopt en in welke staat", J), ("de prijs", J), ("hoe iemand je kan bereiken", J), ("je mening over andere merken", F)],
          "Een zoekertje geeft de gegevens die een koper nodig heeft."),
    keuze("Je legt in een mail uit hoe je een gerecht maakt. Voor de stappen gebruik je de [[*impératif|imparfait|passé composé]], zoals « coupez » en « ajoutez ».",
          "De gebiedende wijs zegt de ander wat te doen."),
    mk("Je schrijft een bericht van 150 woorden terwijl de opdracht 80 woorden vraagt. Welke beoordelingsrij verlies je?",
       ["taakvoltooiing", "spelling en leestekens", "tekstopbouw en lay-out", "register en beleefdheid"], 0,
       "Je respecteert de opgegeven lengte niet, dus de taak is niet goed uitgevoerd."),
    tabel("Is dit een zin over je leesbeleving bij een literaire tekst?",
          [("Ce texte me touche.", J), ("Ce passage me fait penser à mon enfance.", J), ("Le texte a trente lignes.", F), ("Je m'identifie au personnage principal.", J)],
          "Het aantal regels zegt niets over wat de tekst bij je oproept."),
    keuze("Bij een opdracht over je leesbeleving [[*mag je ook schrijven dat de tekst je niet raakt, als je uitlegt waarom|moet je het ene juiste gevoel vinden]].",
          "Het gaat om jouw ervaring, duidelijk verwoord."),
    inv("Vul in: « Tournez à ___ » (links). Eén woord.", ["gauche"],
        "À gauche: links; à droite: rechts."),
]

"""Woordvelden: mens, familie, gevoelens en gezondheid — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen met de woorden uit het gewone hoofdstuk, in zinnen en korte teksten:
familie, persoonsgegevens, gevoelens, lichaamsdelen en bij de dokter."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import gezondheid as _g

T1 = ("Lis le message de Nora.\n\n"
      "« Salut Inès ! Je ne viens pas à l'école aujourd'hui. Je me suis réveillée avec de la fièvre et j'ai mal à la gorge. "
      "Ma mère a pris un rendez-vous chez le médecin à 11 h. Je suis triste, parce que je rate la fête de ce soir. "
      "Tu peux me dire ce que nous avons comme devoirs ? Bisous, Nora »")

T2 = ("Lis le texte.\n\n"
      "« Je m'appelle Hugo. J'habite avec ma mère et mon beau-père. J'ai une demi-sœur, Lina, qui a six ans : "
      "c'est la cadette. Mon père habite à Liège avec sa nouvelle femme. Le week-end, je vais chez lui. "
      "Mes grands-parents sont très gentils : ma grand-mère fait toujours une tarte quand nous venons. »")

VRAGEN = [_g.VRAGEN[i] for i in (5, 11)] + [
    casus(T1, [
        mk("Waarom komt Nora niet naar school?",
           ["Ze is ziek.", "Ze moet naar een feest.", "Haar moeder is ziek.", "Ze heeft haar bus gemist."], 0,
           "De la fièvre et mal à la gorge: koorts en keelpijn."),
        tabel("Klopt dit volgens het bericht van Nora?",
              [("Nora heeft keelpijn.", J), ("Ze heeft om 11 uur een afspraak bij de dokter.", J), ("Ze is blij dat ze het feest mist.", F), ("Ze vraagt welke taken er zijn.", J)],
              "Je suis triste: ze is verdrietig."),
        keuze("« Je me suis réveillée » betekent [[*ik ben wakker geworden|ik heb me gewassen|ik ben gaan slapen]].",
              "Se réveiller: wakker worden."),
        inv("Welk Frans woord in het bericht betekent 'koorts'?", ["fièvre", "fievre", "la fièvre"],
            "Avoir de la fièvre: koorts hebben."),
        keuze("Nora is [[*verdrietig|boos|bang]], want ze mist het feest.",
              "Triste: verdrietig."),
    ]),
    casus(T2, [
        keuze("Lina is de [[*jongste|oudste]] van de kinderen.",
              "La cadette: de jongste; l'aîné(e): de oudste."),
        tabel("Klopt dit volgens de tekst?",
              [("Hugo woont bij zijn moeder.", J), ("Zijn vader woont in Luik.", J), ("Lina is de dochter van zijn vader en zijn nieuwe vrouw.", F), ("Hugo gaat in het weekend naar zijn vader.", J)],
              "Hugo woont met zijn moeder en stiefvader; Lina is zijn halfzus in dat gezin."),
        keuze("« Mon beau-père » is de [[*nieuwe man van zijn moeder|vader van zijn vader|broer van zijn moeder]].",
              "Beau-père: stiefvader."),
        keuze("« chez lui » betekent [[*bij hem thuis|bij zijn grootouders|naar school]].",
              "Lui verwijst naar de vader."),
    ]),
    koppel("Koppel elk familielid aan zijn betekenis.",
           [("la tante", "de tante"), ("l'oncle", "de oom"), ("le cousin", "de neef"), ("les grands-parents", "de grootouders")], ["de buur"],
           "Le voisin, de buur, is geen familie."),
    keuze("« J'ai un frère [[*plus jeune|plus vieux]] que moi » betekent dat je broer jonger is.",
          "Plus jeune que: jonger dan."),
    tabel("Welk gegeven vul je in bij welk Frans woord op een formulier?",
          [("Dubois", "nom"), ("Camille", "prénom"), ("14/03/2010", "date de naissance"), ("belge", "nationalité")],
          "Nom is de familienaam, prénom de voornaam.",
          kolommen=["nom", "prénom", "date de naissance", "nationalité"]),
    keuze("Een Belg zegt: « Je suis [[*belge|Belge|belgique]]. »",
          "Een nationaliteit is een bijvoeglijk naamwoord met een kleine letter."),
    tabel("Gebruikt het Frans hier avoir waar wij 'zijn' zeggen?",
          [("honger hebben: avoir faim", J), ("bang zijn: avoir peur", J), ("het koud hebben: avoir froid", J), ("moe zijn: être fatigué", F)],
          "Avoir faim, avoir soif, avoir peur, avoir froid, avoir chaud; maar être fatigué."),
    sorteer("Positief of negatief gevoel?", ["positief", "negatief"],
            [("content", "positief"), ("triste", "negatief"), ("en colère", "negatief"), ("heureux", "positief"), ("inquiet", "negatief")],
            "Inquiet: ongerust."),
    keuze("Een vrouw schrijft: « Je suis [[*fatiguée|fatigué]]. »",
          "De extra e voor een vrouw hoor je niet, maar je schrijft ze wel."),
    tabel("Klopt de vertaling?",
          [("J'ai mal au ventre: ik heb buikpijn.", J), ("J'ai mal aux dents: ik heb oorpijn.", F), ("J'ai mal à la tête: ik heb hoofdpijn.", J), ("J'ai mal au dos: ik heb rugpijn.", J)],
          "Une dent is een tand: mal aux dents is tandpijn."),
    keuze("« J'ai mal [[*au|à le]] pied. » « J'ai mal [[*à la|au]] jambe. » « J'ai mal [[*aux|à les]] yeux. »",
          "À + le wordt au, à + les wordt aux, à la blijft."),
    inv("Schrijf het meervoud van « un œil ». Twee woorden.", ["les yeux", "des yeux"],
        "Un œil, des yeux: onregelmatig."),
    koppel("Koppel elk lichaamsdeel aan zijn betekenis.",
           [("l'épaule", "de schouder"), ("le genou", "de knie"), ("la main", "de hand"), ("le dos", "de rug")], ["de enkel"],
           "La cheville is de enkel."),
    volgorde("Zet het gesprek bij de dokter in een logische volgorde.",
             ["Bonjour, qu'est-ce qui ne va pas ?", "J'ai mal au ventre depuis deux jours.", "Vous avez de la fièvre ?", "Non. — Voici une ordonnance pour la pharmacie."],
             "Groeten, klacht, vraag, voorschrift."),
    mk("Je belt een dokterspraktijk. Welke zin past?",
       ["Je voudrais prendre un rendez-vous, s'il vous plaît.", "Donne-moi vite un rendez-vous pour demain, d'accord ?", "Je veux voir le docteur maintenant, tout de suite, merci.", "Salut, tu as encore un peu de temps libre cette semaine ?"], 0,
       "Je voudrais is hoffelijk en past bij vous."),
    keuze("Voor een antibioticum heb je [[*een voorschrift|geen voorschrift]] van de dokter nodig: « une ordonnance ».",
          "Paracetamol kan zonder, een antibioticum niet."),
    keuze("« Je ne me [[*sens|sent]] pas bien. »",
          "Se sentir: je me sens, il se sent."),
    sleep("Ik ben ziek: je suis [[malade]]. Bij de apotheek koop je een [[médicament]].",
          ["ordonnance", "colère"], "Malade: ziek; un médicament: een geneesmiddel."),
    keuze("« Il a peur [[*du|de le]] chien. »",
          "De + le wordt du."),
    tabel("Klopt dit over l'aîné en le cadet?",
          [("L'aîné is het oudste kind.", J), ("Le cadet is het jongste kind.", J), ("Een enig kind heeft een aîné en een cadet.", F)],
          "Een enig kind heeft geen broers of zussen."),
    inv("Vul in: « Avoir ___ » betekent dorst hebben. Eén woord.", ["soif"],
        "Avoir soif, zonder lidwoord."),
]

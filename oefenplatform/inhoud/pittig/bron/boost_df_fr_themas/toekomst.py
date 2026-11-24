"""Futur proche, futur simple en de conditionnel de politesse — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over de toekomende tijden en de hoffelijke vorm uit Frans Beyond dubbele
finaliteit (zonder de andere gebruiken van de conditionnel, die hier niet in de
leerstof staan), aangevuld met eigen vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import toekomst as _t

T1 = ("Lis le mail d'Emma.\n\n"
      "« Madame,\n\nJe vais commencer mon stage dans votre magasin le lundi 3 mars. "
      "Je prendrai le bus de 7 h 30 et j'arriverai vers 8 h 15. Pourriez-vous me dire quels vêtements je dois porter ? "
      "Je voudrais aussi savoir où je pourrai manger à midi.\n\nMerci d'avance.\n\nCordialement,\nEmma Claes »")

VRAGEN = [_t.VRAGEN[i] for i in (1, 2, 4, 6, 7, 9, 11, 12, 13, 14, 15, 18, 19, 21, 23, 24)] + [
    casus(T1, [
        keuze("« Je vais commencer » is een [[*futur proche|futur simple|conditionnel]].",
              "Aller + infinitief."),
        keuze("« Je prendrai » is de futur simple van [[*prendre|pouvoir|partir]]: de e van -re valt weg.",
              "Prendre wordt je prendrai."),
        keuze("Emma schrijft « Pourriez-vous » en « Je voudrais » om [[*hoffelijk te vragen|over het verleden te vertellen]].",
              "De conditionnel de politesse, samen met vous."),
        tabel("Klopt dit volgens de mail?",
              [("Emma begint haar stage op een maandag.", J), ("Ze komt met de bus.", J), ("Ze vraagt waar ze 's middags kan eten.", J), ("Ze vraagt hoeveel ze verdient.", F)],
              "Ze vraagt naar de kleren en de plaats om te eten."),
    ]),
    keuze("« Je ne [[*vais pas|vas pas]] venir ce soir. »",
          "Ne ... pas rond aller."),
    keuze("« Demain, je [[*serai|serais]] à l'école à huit heures. »",
          "Futur simple: je serai. Je serais is conditionnel."),
    tabel("Vraagt de tijdsbepaling een toekomende tijd?",
          [("demain", J), ("dans trois jours", J), ("il y a trois jours", F), ("la semaine prochaine", J)],
          "Il y a trois jours is drie dagen geleden."),
    keuze("« L'été prochain, nous [[*irons|sommes allés]] en Espagne. » « L'été dernier, nous [[*sommes allés|irons]] en Italie. »",
          "Prochain kijkt vooruit, dernier terug."),
    keuze("« J'[[*aimerais|aime]] savoir si le poste est encore libre », schrijf je hoffelijk aan een werkgever.",
          "J'aimerais is de conditionnel van aimer."),
    keuze("Een weerbericht over morgen staat meestal in de [[*futur simple|imparfait]]: « il pleuvra ».",
          "Morgen kijkt vooruit."),
    tabel("Futur proche of futur simple?",
          [("je vais partir", "futur proche"), ("je partirai", "futur simple"), ("il va pleuvoir", "futur proche"), ("nous ferons", "futur simple")],
          "Aller + infinitief is de futur proche.",
          kolommen=["futur proche", "futur simple"]),
    keuze("In de futur proche vervoeg je [[*enkel aller|allebei de werkwoorden]]: je vais manger.",
          "Het tweede werkwoord blijft een infinitief."),
    mk("Welke zin past het best in een mail aan een onbekende werkgever?",
       ["Je voudrais savoir si le poste est encore libre.", "Je veux savoir tout de suite si le poste est libre.", "Dis-moi vite si le poste est encore libre, merci.", "Le poste est encore libre ou pas, alors, dis-moi ?"], 0,
       "Hoffelijk met je voudrais."),
    keuze("« Maintenant, je [[*travaille|travaillerai]]. Demain, je [[*travaillerai|travaille]] aussi. »",
          "Maintenant vraagt een présent, demain een toekomende tijd."),
]

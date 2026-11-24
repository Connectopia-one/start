"""Woordvelden: tijd, weer, reizen en vervoer — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen met de woorden uit het gewone hoofdstuk: agenda, seizoenen, het uur,
de weg vragen, het weerbericht, de trein, landen en nationaliteiten, aangevuld
met enkele vragen uit Frans Beyond dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import cultuur as _c, lezen as _l

T1 = ("Lis le message à la gare.\n\n"
      "« Attention : le train de 8 h 12 vers Liège a un retard de quinze minutes. "
      "Les voyageurs pour Hasselt doivent changer à Landen. Le train part de la voie 4 et pas de la voie 2. "
      "Le prochain train direct vers Liège part à 9 h 12. Nous nous excusons pour ce retard. »")

T2 = ("Lis la météo.\n\n"
      "« Ce week-end, il fera beau samedi, avec du soleil et 22 degrés. Dimanche, le temps change : "
      "il pleuvra l'après-midi et il y aura beaucoup de vent à la côte. Lundi, il fera plus froid, avec 12 degrés. »")

VRAGEN = [_c.VRAGEN[i] for i in (2, 5, 6, 7, 11)] + [
    casus(T1, [
        inv("Hoe laat vertrekt de trein van 8.12 uur nu echt? Schrijf als 8.27.", ["8.27", "8:27", "8u27", "8 h 27"],
            "8.12 plus vijftien minuten vertraging."),
        keuze("Wie naar Hasselt moet, [[*stapt over in Landen|blijft zitten tot Luik|neemt de trein van 9.12]].",
              "Changer à Landen: overstappen in Landen."),
        keuze("De trein vertrekt van [[*spoor 4|spoor 2]].",
              "La voie 4 et pas de la voie 2."),
        keuze("« un retard » is een [[*vertraging|vertrek|spoor]].",
              "Le train a un retard de quinze minutes."),
    ]),
    casus(T2, [
        tabel("Klopt dit volgens het weerbericht?",
              [("Zaterdag wordt het zonnig.", J), ("Zondagnamiddag regent het.", J), ("Maandag wordt het warmer.", F), ("Aan de kust waait het zondag hard.", J)],
              "Il fera plus froid: het wordt kouder."),
        inv("Hoeveel graden scheelt het tussen zaterdag en maandag? Schrijf enkel het getal.", ["10", "tien"],
            "22 min 12 is 10 graden."),
        keuze("« il pleuvra » betekent [[*het zal regenen|het regent nu|het heeft geregend]].",
              "Pleuvoir in de futur simple."),
    ]),
    keuze("« Il est neuf heures [[*moins le quart|et quart]] » is kwart voor negen.",
          "Moins le quart: kwart voor; et quart: kwart na."),
    inv("Schrijf in cijfers: « Il est trois heures et demie de l'après-midi. » Schrijf als 15.30.", ["15.30", "15:30", "15u30", "15 h 30"],
        "Trois heures et demie: half vier."),
    koppel("Koppel elk seizoen aan zijn Franse naam.",
           [("de lente", "le printemps"), ("de zomer", "l'été"), ("de herfst", "l'automne"), ("de winter", "l'hiver")], ["l'anniversaire"],
           "Un anniversaire is een verjaardag."),
    keuze("« Midi » is [[*twaalf uur 's middags|middernacht]] en « minuit » is [[*middernacht|twaalf uur 's middags]].",
          "Twee woorden die je snel verwart."),
    tabel("Klopt de vertaling van deze plaatsaanduiding?",
          [("derrière l'église: achter de kerk", J), ("en face de la poste: tegenover de post", J), ("tout droit: naar rechts", F), ("au bout de la rue: aan het einde van de straat", J)],
          "Tout droit is rechtdoor, à droite naar rechts."),
    keuze("« Le chat dort [[*sous|sur]] la table » betekent dat de kat onder de tafel slaapt.",
          "Sous: onder; sur: op."),
    sorteer("Zegt het woord waar of wanneer?", ["waar", "wanneer"],
            [("entre", "waar"), ("pendant", "wanneer"), ("derrière", "waar"), ("depuis", "wanneer")],
            "Pendant en depuis gaan over tijd."),
    tabel("Is dit een uitdrukking over het weer?",
          [("il fait beau", J), ("il neige", J), ("il y a du vent", J), ("il est tard", F)],
          "Il est tard: het is laat."),
    tabel("À of en?",
          [("___ vélo", "à"), ("___ voiture", "en"), ("___ pied", "à"), ("___ train", "en")],
          "Waar je in zit: en; waar je op zit of te voet: à.",
          kolommen=["à", "en"]),
    keuze("« J'habite [[*en|à|au]] France, [[*à|en]] Lyon. »",
          "En bij een vrouwelijk land, à bij een stad."),
    keuze("« Mateo vient [[*d'|de la]] Italie. »",
          "Venir de, voor een klinker d'."),
    tabel("Schrijf je het met een hoofdletter?",
          [("la Belgique", J), ("belge (nationaliteit)", F), ("lundi", F), ("la France", J)],
          "Landen met een hoofdletter; nationaliteiten, dagen en maanden klein."),
    keuze("« Je vais [[*prendre|aller]] le bus. »",
          "Prendre le bus, le train, l'avion."),
    mk("Iemand vraagt: « La gare, c'est loin ? » Welk antwoord past?",
       ["Non, c'est à cinq minutes à pied.", "Oui, il fait très beau aujourd'hui.", "Non, le train a vingt minutes de retard.", "Oui, j'ai mon billet dans mon sac à dos."], 0,
       "Loin: ver. Het antwoord zegt hoe ver het is."),
    keuze("Dagen en maanden schrijf je in het Frans [[*met een kleine letter|met een hoofdletter]]: lundi, janvier.",
          "Anders dan in het Engels."),
    volgorde("Zet deze dagen in de juiste volgorde.",
             ["lundi", "mardi", "mercredi", "jeudi", "vendredi"],
             "Maandag tot vrijdag."),
    keuze("« Bon [[*anniversaire|fête]] ! » zeg je op iemands verjaardag.",
          "Bonne fête zeg je op een naamdag."),
    inv("Lees: « Le bus part à 7 h 50 et le trajet dure vingt-cinq minutes. » Hoe laat kom je aan? Schrijf als 8.15.", ["8.15", "8:15", "8u15", "8 h 15"],
        "7.50 plus 25 minuten is 8.15."),
]

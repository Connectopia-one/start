"""De Franstalige wereld: omgangsvormen en gewoontes — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen over beleefdheid, tu en vous, de bise, gewoontes aan tafel en de
Franstalige landen, aangevuld met vragen uit Frans Beyond dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import cultuur as _c

T1 = ("Lis le message de Clara, une Française qui fait un stage à Namur.\n\n"
      "« Ici, en Belgique, c'est un peu différent de chez moi. Les gens disent septante et nonante, "
      "et pas soixante-dix ou quatre-vingt-dix. Au bureau, tout le monde se fait la bise le matin, même les hommes. "
      "On mange à midi et le repas du soir est souvent plus léger. "
      "Les magasins restent ouverts entre midi et deux heures, ce qui est pratique ! "
      "Mais quand je parle à un client, je dis toujours vous, comme en France. »")

VRAGEN = [_c.VRAGEN[i] for i in (1, 8, 9, 10, 14, 18, 19, 20, 21, 23)] + [
    casus(T1, [
        mk("Waarover gaat het bericht van Clara?",
           ["verschillen tussen België en Frankrijk", "haar werk als verkoopster in een Franse winkel", "een reis door Zwitserland", "de school van haar broer in Namen"], 0,
           "C'est un peu différent de chez moi: het is wat anders dan bij haar thuis."),
        tabel("Klopt dit volgens het bericht van Clara?",
              [("In België zegt men nonante voor negentig.", J), ("Op het kantoor geven ook mannen elkaar de bise.", J), ("Tegen een klant zegt Clara tu.", F), ("In Namen blijven de winkels 's middags open.", J)],
              "Quand je parle à un client, je dis toujours vous."),
        keuze("Clara vindt het [[*handig|lastig]] dat de winkels 's middags open blijven.",
              "Ce qui est pratique: wat handig is."),
        inv("Hoe zegt men 70 in België? Schrijf het Franse woord.", ["septante"],
            "Septante, in Frankrijk soixante-dix."),
        keuze("« le repas du soir est souvent plus léger » betekent dat het avondmaal vaak [[*lichter|later|groter]] is.",
              "Léger: licht."),
    ]),
    tabel("Tu of vous?",
          [("je beste vriend", "tu"), ("een klant die even oud is als jij", "vous"), ("je stagebegeleider die je niet kent", "vous"), ("je jongere neef", "tu")],
          "Tegen een klant blijf je bij vous, ook als hij jouw leeftijd heeft.",
          kolommen=["tu", "vous"]),
    koppel("Welke reactie past bij de situatie?",
           [("Iemand zegt: « Je suis désolé, je suis en retard. »", "Ce n'est pas grave."), ("Je gaat aan tafel.", "Bon appétit !"), ("Je ziet je vriend morgen terug.", "À demain !"), ("Je botst per ongeluk tegen iemand.", "Pardon !")], ["Enchanté !"],
           "Enchanté zeg je bij een eerste kennismaking."),
    mk("Je vraagt in een Franse winkel naar een maat. Welke zin is het beleefdst?",
       ["Bonjour madame, vous avez ce pull en M ?", "Salut, t'as ce pull en M ou pas, toi ?", "Je veux ce pull en M, vite, s'il te plaît.", "Hé, donne-moi ce pull en M maintenant !"], 0,
       "Eerst bonjour, dan je vraag met vous."),
    sorteer("Zeg je dit tegen een vriend of tegen een onbekende volwassene?", ["vriend", "onbekende"],
            [("Salut !", "vriend"), ("Bonjour, monsieur.", "onbekende"), ("S'il vous plaît.", "onbekende"), ("Coucou, ça va ?", "vriend")],
            "Salut en coucou zijn informeel; monsieur en s'il vous plaît formeel."),
    keuze("Tegen iemand die je met vous aanspreekt, zeg je [[*s'il vous plaît|s'il te plaît]].",
          "Je kiest de vorm die past bij hoe je de persoon aanspreekt."),
    tabel("Klopt dit over België en het Frans?",
          [("België heeft drie officiële talen.", J), ("Brussel is officieel tweetalig.", J), ("In Wallonië spreekt men een andere taal dan Frans.", F), ("De Belgische nationale feestdag is op 21 juli.", J)],
          "Frans, Nederlands en Duits zijn officieel."),
    inv("Hoe zegt men 90 in België? Schrijf het Franse woord.", ["nonante"],
        "Nonante, in Frankrijk quatre-vingt-dix."),
    keuze("In een Franse maaltijd komt de kaas [[*voor het dessert|na het dessert|bij het voorgerecht]].",
          "Le fromage vient avant le dessert."),
    mk("Je komt om 12.30 uur aan bij een klein winkeltje in een Franse straat. De deur is dicht. Wat is de meest waarschijnlijke reden?",
       ["Veel winkels sluiten tussen twaalf en twee uur.", "In Frankrijk zijn de winkels op elke dag gesloten.", "Franse winkels openen pas om vier uur 's middags.", "Je moet eerst bellen voor je binnen mag gaan."], 0,
       "Les magasins ferment entre midi et deux heures."),
    tabel("Is dit een sociocultureel aspect waarover een examentekst kan gaan?",
          [("eetgewoonten", J), ("lichaamstaal", J), ("sociale verhoudingen", J), ("de spelling van een werkwoord", F)],
          "Spelling hoort bij taal, niet bij cultuur."),
    keuze("Bij een eerste kennismaking zeg je [[*Enchanté|À demain|Bonne nuit]].",
          "Enchanté: aangenaam."),
    tabel("Klopt dit over de bise?",
          [("Je geeft ze aan vrienden en familie.", J), ("In Franstalig België geven ook mannen elkaar de bise.", J), ("Je geeft ze aan een klant die je voor het eerst ziet.", F)],
          "Tegen een onbekende klant geef je een hand of zeg je enkel bonjour."),
    mk("Je schrijft een mail aan een onbekende werkgever. Welke afsluiting past?",
       ["Cordialement,", "Bisous !", "À plus !", "Salut et à bientôt !"], 0,
       "Cordialement is formeel; de rest is voor vrienden."),
    keuze("Wie in het Frans de verkeerde toon kiest, kan [[*onvriendelijk klinken|nooit begrepen worden]], ook als elk woord juist is.",
          "Register en beleefdheid horen bij de boodschap."),
    open_("Een Vlaamse leerling begint in een Franse bakkerij met « Je veux une baguette ». Waarom klinkt dat onvriendelijk en hoe zegt hij het beter?",
          "Hij begint zonder te groeten en zegt je veux, ik wil. Beter is: « Bonjour madame, je voudrais une baguette, s'il vous plaît. »",
          "Eerst bonjour, dan je voudrais en s'il vous plaît."),
]

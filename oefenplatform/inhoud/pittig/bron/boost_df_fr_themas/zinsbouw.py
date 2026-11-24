"""Zinsbouw, zinsdelen, voegwoorden en de overeenkomst — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over soorten zinnen, zinsdelen, voegwoorden en overeenkomst uit Frans
Beyond dubbele finaliteit (zonder bijzinnen met qui en wenszinnen, die hier niet
in de leerstof staan), aangevuld met eigen vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import zinsbouw as _z

VRAGEN = [_z.VRAGEN[i] for i in (0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 25)] + [
    tabel("Is dit een juiste manier om « kom je? » te vragen?",
          [("Tu viens ?", J), ("Est-ce que tu viens ?", J), ("Viens-tu ?", J), ("Tu est-ce que viens ?", F)],
          "Met je stem, met est-ce que of met de omgekeerde orde."),
    koppel("Koppel elke ontkenning aan haar betekenis.",
           [("ne ... pas", "niet"), ("ne ... jamais", "nooit"), ("ne ... rien", "niets"), ("ne ... plus", "niet meer")], ["niemand"],
           "Vier ontkenningen in twee stukken."),
    keuze("« Hier, je [[*n'ai pas|ai ne pas]] mangé. »",
          "In de passé composé staat de ontkenning rond het hulpwerkwoord."),
    sorteer("Nevenschikkend of onderschikkend voegwoord?", ["nevenschikkend", "onderschikkend"],
            [("et", "nevenschikkend"), ("mais", "nevenschikkend"), ("parce que", "onderschikkend"), ("quand", "onderschikkend"), ("donc", "nevenschikkend"), ("si", "onderschikkend")],
            "Parce que, quand en si maken van het tweede stuk een bijzin."),
    keuze("« Pourquoi tu restes ? — [[*Parce qu'|Pour que]] il pleut. »",
          "Op pourquoi antwoord je met parce que."),
    keuze("« Les filles sont [[*arrivées|arrivé|arrivés]] hier. »",
          "Met être past het deelwoord zich aan: vrouwelijk meervoud."),
    tabel("Enkelvoudige of samengestelde zin?",
          [("Je reste à la maison.", "enkelvoudig"), ("Je reste à la maison parce qu'il pleut.", "samengesteld"), ("Il pleut, donc je prends le bus.", "samengesteld"), ("Nous allons au cinéma ce soir.", "enkelvoudig")],
          "Een samengestelde zin heeft meer dan één persoonsvorm.",
          kolommen=["enkelvoudig", "samengesteld"]),
    keuze("In « Je donne mon numéro à Lila » is « mon numéro » het [[*lijdend voorwerp|meewerkend voorwerp|onderwerp]].",
          "Wat geef ik? Mon numéro, zonder voorzetsel."),
]

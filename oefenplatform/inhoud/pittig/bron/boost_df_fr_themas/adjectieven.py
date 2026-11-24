"""Bijvoeglijke naamwoorden, bijwoorden en de trappen — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over overeenkomst, plaats, vergelijking, bijwoorden en voorzetsels uit Frans
Beyond dubbele finaliteit (zonder wat hier niet in de leerstof staat), aangevuld met
eigen vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import adjectieven as _a

T1 = ("Lis l'avis sur deux hôtels.\n\n"
      "« L'hôtel du Lac est plus cher que l'hôtel du Parc, mais les chambres sont plus grandes et plus calmes. "
      "Le petit-déjeuner est vraiment délicieux. À l'hôtel du Parc, le personnel parle lentement et gentiment, "
      "mais le wifi marche rarement. Pour moi, l'hôtel du Lac est le meilleur hôtel de la ville. »")

VRAGEN = [_a.VRAGEN[i] for i in (1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 18, 19, 20, 21, 22)] + [
    casus(T1, [
        keuze("Het hôtel du Parc is [[*goedkoper|duurder]] dan het hôtel du Lac.",
              "Le Lac est plus cher que le Parc."),
        tabel("Klopt dit volgens de beoordeling?",
              [("De kamers van het hôtel du Lac zijn groter.", J), ("In het hôtel du Parc werkt de wifi vaak.", F), ("De schrijver vindt het hôtel du Lac het beste.", J)],
              "Rarement: zelden."),
        sleep("In de tekst zijn [[lentement]] en [[gentiment]] bijwoorden op -ment.",
              ["délicieux", "calmes"], "Ze zeggen hoe het personeel spreekt."),
        keuze("« le meilleur hôtel » is de [[*overtreffende trap|vergrotende trap]] van bon.",
              "Bon, meilleur, le meilleur."),
    ]),
    keuze("« C'est une [[*petite|petit]] maison avec un jardin [[*vert|verte]]. »",
          "Maison is vrouwelijk, jardin mannelijk."),
    keuze("« Mes cousines sont [[*sportives|sportifs|sportive]]. »",
          "Sportif wordt sportive, in het meervoud sportives."),
    keuze("« C'est une [[*belle|beau]] journée. »",
          "Beau staat vooraan en wordt belle in het vrouwelijk."),
    keuze("« Ma sœur est plus [[*âgée|âgé]] que moi. »",
          "Ook in een vergelijking past het bijvoeglijk naamwoord zich aan."),
    keuze("« Il est plus grand [[*que|de]] moi. »",
          "Een vergelijking met que."),
    sorteer("Hoe vaak?", ["vaak", "zelden of nooit"],
            [("souvent", "vaak"), ("toujours", "vaak"), ("rarement", "zelden of nooit"), ("jamais", "zelden of nooit")],
            "Toujours: altijd; jamais: nooit."),
    keuze("« Je vais [[*souvent|souvente]] à la piscine. »",
          "Een bijwoord verandert niet van vorm."),
    keuze("« Tu as fini ? — Non, pas [[*encore|jamais]]. »",
          "Pas encore: nog niet."),
    keuze("« Je vais [[*chez|à]] Lila ce soir. »",
          "Chez: bij iemand thuis."),
]

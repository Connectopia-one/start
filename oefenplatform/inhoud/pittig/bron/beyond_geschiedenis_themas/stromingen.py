"""Denkstromingen en kunststromingen van de 19de en 20ste eeuw — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

_KUNST = "Wikimedia Commons, zoek op de titel en de schilder. Publiek domein (de maker is meer dan 70 jaar dood). Neem liefst de versie van Google Art Project of van het museum zelf."

PRENTEN = [
    dict(bestand="abolitie-medaillon.webp", zelf=False,
         wat="Het medaillon van Josiah Wedgwood uit 1787: een geknielde man in ketenen met de tekst 'Am I not a man and a brother?'.",
         waar="Wikimedia Commons, zoek op 'Am I not a man and a brother medallion'. Publiek domein.",
         vragen="bronvraag: abolitionistische ideeën herkennen"),
    dict(bestand="slavenschip-brookes.webp", zelf=False,
         wat="De bekende tekening van het slavenschip Brookes (1788): bovenaanzicht van het schip vol mensen naast elkaar.",
         waar="Wikimedia Commons, zoek op 'Slave ship Brookes 1788'. Publiek domein.",
         vragen="bronvraag over doel en doelpubliek van de abolitionisten"),
    dict(bestand="eugenetica-boom.webp", zelf=False,
         wat="Het logo van het tweede internationale eugeneticacongres van 1921: een boom met wortels zoals 'biology', 'genetics' en de tekst 'Eugenics is the self direction of human evolution'.",
         waar="Wikimedia Commons, zoek op 'Eugenics congress logo 1921'. Publiek domein.",
         vragen="bronvraag: hoe eugenetica zich als wetenschap voorstelt"),
    dict(bestand="romantiek-friedrich.webp", zelf=False,
         wat="Caspar David Friedrich, 'Wandelaar boven de nevelzee' (1818).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="realisme-courbet.webp", zelf=False,
         wat="Gustave Courbet, 'De steenkappers' (1849). Het origineel ging verloren in 1945, een zwart-witfoto of kleurenreproductie is goed.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="impressionisme-monet.webp", zelf=False,
         wat="Claude Monet, 'Impressie, opkomende zon' (1872).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="kubisme-gris.webp", zelf=False,
         wat="Juan Gris, 'Portret van Pablo Picasso' (1912). Werk van Picasso zelf is nog niet vrij, dat van Gris wel.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="expressionisme-munch.webp", zelf=False,
         wat="Edvard Munch, 'De schreeuw' (1893), de geschilderde versie.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="artnouveau-mucha.webp", zelf=False,
         wat="Een affiche van Alfons Mucha, bijvoorbeeld 'Job' (1896) of 'Gismonda' (1894).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="abstract-kandinsky.webp", zelf=False,
         wat="Wassily Kandinsky, 'Compositie VII' (1913).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="abstract-mondriaan.webp", zelf=False,
         wat="Piet Mondriaan, 'Compositie met rood, geel en blauw' (een versie uit 1921 tot 1930).",
         waar=_KUNST, vragen="abstracte kunst vergelijken met Kandinsky"),
]
# Surrealisme: Magritte, Dalí en Ernst zijn nog niet vrij. Die werken komen er als beschrijving in tekst, zoals bij popart.

VRAGEN = []

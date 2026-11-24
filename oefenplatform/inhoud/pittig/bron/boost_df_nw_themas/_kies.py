"""Neemt pittige vragen van natuurwetenschappen Boost doorstroom over (met hun prenten) en past woorden aan waar nodig."""
import copy
import json


def kies(vragen, nummers, vervang=None):
    uit = [copy.deepcopy(vragen[i]) for i in nummers]
    if vervang:
        tekst = json.dumps(uit, ensure_ascii=False)
        for oud, nieuw in vervang.items():
            tekst = tekst.replace(oud, nieuw)
        uit = json.loads(tekst)
    return uit

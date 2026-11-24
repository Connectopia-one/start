"""Neemt pittige vragen van Beyond doorstroom over, zonder de weggelaten nummers."""
import copy


def kies(vragen, weg=(), enkel=None):
    nummers = enkel if enkel is not None else [i for i in range(len(vragen)) if i not in set(weg)]
    return [copy.deepcopy(vragen[i]) for i in nummers]

# -*- coding: utf-8 -*-
"""Korte schrijfwijze voor Ready-vragen."""


def mk(vraag, opties, antwoord, uitleg, reken=None, prent=None):
    d = dict(type="meerkeuze", vraag=vraag, opties=opties, antwoord=antwoord, uitleg=uitleg)
    if reken is not None: d["reken"] = reken
    if prent: d["afbeelding_pad"] = prent
    return d


def inv(vraag, antwoord, uitleg, reken=None, prent=None):
    d = dict(type="invultekst", vraag=vraag, antwoord=antwoord, uitleg=uitleg)
    if reken is not None: d["reken"] = reken
    if prent: d["afbeelding_pad"] = prent
    return d


def wn(vraag, antwoord, uitleg, prent=None):
    d = dict(type="waarofniet", vraag=vraag, antwoord=antwoord, uitleg=uitleg)
    if prent: d["afbeelding_pad"] = prent
    return d


def sorteer(vraag, items, kolommen, uitleg):
    """items: lijst (tekst, kolomindex)."""
    return dict(type="sorteren", vraag=vraag, opties=[t for t, _ in items],
                antwoord={"juist": [k for _, k in items], "kolommen": kolommen}, uitleg=uitleg)

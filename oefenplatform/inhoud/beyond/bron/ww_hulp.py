# -*- coding: utf-8 -*-
"""Korte schrijfwijze voor de thema's van welzijnswetenschappen (ww_*.py).

M = meerkeuze (antwoord is een nummer, of een lijst als er meer juist zijn),
W = waar of niet waar, I = invultekst (hoogstens drie woorden).
Het resultaat is precies hetzelfde woordenboek als dict(type=...) elders.
"""


def M(vraag, opties, antwoord, uitleg):
    return dict(type="meerkeuze", vraag=vraag, opties=opties, antwoord=antwoord, uitleg=uitleg)


def W(vraag, antwoord, uitleg):
    return dict(type="waarofniet", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def I(vraag, antwoord, uitleg):
    return dict(type="invultekst", vraag=vraag, antwoord=antwoord, uitleg=uitleg)

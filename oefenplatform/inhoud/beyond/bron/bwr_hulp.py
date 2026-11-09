# -*- coding: utf-8 -*-
"""Korte schrijfwijze voor de vragen van bedrijfswetenschappen en recht.

M: meerkeuze (antwoord = index, of lijst van indexen bij meerdere juiste)
W: waar of niet waar
I: invulvraag (lijst van aanvaarde antwoorden, elk hoogstens drie woorden)
"""


def M(vraag, opties, antwoord, uitleg):
    return dict(type="meerkeuze", vraag=vraag, opties=list(opties), antwoord=antwoord, uitleg=uitleg)


def W(vraag, antwoord, uitleg):
    return dict(type="waarofniet", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def I(vraag, antwoord, uitleg):
    return dict(type="invultekst", vraag=vraag, antwoord=list(antwoord), uitleg=uitleg)

# -*- coding: utf-8 -*-
"""Korte schrijfwijze voor de vragen van Duits (zie bouw_duits.py)."""


def M(vraag, opties, antwoord, uitleg):
    """Meerkeuze. Antwoord is een getal, of een lijst bij meer juiste antwoorden."""
    return dict(type="meerkeuze", vraag=vraag, opties=opties, antwoord=antwoord, uitleg=uitleg)


def W(vraag, antwoord, uitleg):
    """Waar of niet waar."""
    return dict(type="waarofniet", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def I(vraag, antwoord, uitleg):
    """Invullen. Antwoord is een lijst van goede antwoorden (hoogstens drie woorden)."""
    return dict(type="invultekst", vraag=vraag, antwoord=antwoord, uitleg=uitleg)

# -*- coding: utf-8 -*-
r"""Hoe lang is een stuk tekst op het scherm, als er een formule in staat?

    from notatie import zichtbaar

De gokcontroles hieronder en in de bouwscripts tellen letters: staat het juiste
antwoord er duidelijk langer dan de andere, dan kan een kind het eruit kiezen
zonder de leerstof te kennen.

Sinds de vragen van wiskunde in echte notatie staan (zie
oefenplatform/lib/wiskunde.ts), telt die telling verkeerd. \(5\sqrt{2}\) is
veertien tekens in het bronbestand en drie op het scherm. Zonder deze stap zou
elke optie met een formule erin "de langste" lijken, en dan slaat de controle
alarm op vragen die net goed zijn.

Dit is een benadering, geen exacte breedte: de naam van een commando blijft
staan (\sqrt wordt sqrt) zodat een grote formule nog altijd langer weegt dan
een kleine. Dat volstaat, want de opties van één vraag gebruiken bijna altijd
dezelfde commando's.
"""
import re

MARKERING = re.compile(r"\\[()\[\]]")   # \( \) \[ \]
COMMANDO = re.compile(r"\\([a-zA-Z]+)")  # \sqrt, \log, \cdot ...


def zichtbaar(tekst: str) -> str:
    """De tekst zoals een kind ze ziet, zonder de LaTeX-markering errond."""
    tekst = MARKERING.sub("", tekst)
    tekst = COMMANDO.sub(r"\1", tekst)
    return tekst.replace("{", "").replace("}", "")


def zonder_notatie(tekst: str) -> str:
    r"""De tekst zonder enige LaTeX, ook zonder de namen van de commando's.

    `zichtbaar` laat die namen met opzet staan, want daar weegt een grote
    formule mee. Voor wie woorden telt, zoals de dekkingscontrole van de
    leerbundels, zijn ze juist ruis: \tfrac{R}{2} is geen woord "tfracr2".
    """
    tekst = MARKERING.sub(" ", tekst)
    tekst = COMMANDO.sub(" ", tekst)
    return tekst.replace("{", " ").replace("}", " ")

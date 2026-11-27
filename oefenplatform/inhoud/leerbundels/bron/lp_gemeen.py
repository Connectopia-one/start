# -*- coding: utf-8 -*-
"""Gedeelde stijl voor de Launchpad-bundels (1ste en 2de leerjaar, Kim 27/11).
Nog grotere letters en schrijflijnen dan Ready: kinderen van 6 en 7 schrijven groot.
Gebruikt de maakfunctie van Ready, met een eigen lettergrootte."""
import ready_gemeen
from ready_gemeen import tabel, svg, DARK, ORANJE, PAARS, GROEN  # noqa: F401

LP = "🪁 Launchpad — 1ste en 2de leerjaar"
ready_gemeen.GROOT = ("body{font-size:15pt;line-height:1.75}table{font-size:13.5pt}figcaption{font-size:12pt}"
                      ".oef .vraagtekst,.rij .cel{font-size:14.5pt}.hoe li,.opdracht{font-size:13pt}"
                      ".lijn{height:64px}.vakje{height:44px;min-width:110px !important}.rij .cel{line-height:3}"
                      ".oef{break-inside:avoid}.keuze{font-size:14pt;margin-right:18px}")
ready_gemeen.READYJSON = ready_gemeen.HIER.parent.parent / "launchpad"
HOE = ["Schrijf met potlood, dan kan je gerust iets uitgommen.",
       "Lees de opdracht samen met een volwassene als dat nodig is.",
       "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."]
ON = "{aantal} oefeningen op papier, met een antwoordblad achteraan."


def maak(naam, vakmap, leer, oefen, module=None, **kw):
    # Een rij met __ in de opgave wordt een rij met hokjes in de opgave zelf.
    for r in oefen["reeksen"]:
        r["oefeningen"] = [("invulwoord",) + tuple(o[1:3]) if o[0] == "rij" and any("__" in a for a, _ in o[1]) else o
                           for o in r["oefeningen"]]
    if module:
        ready_gemeen.met_prenten(leer, oefen, module)
    ready_gemeen.maak(naam, vakmap, leer, oefen, **kw)


def stippen(n, kleur=ORANJE, per=5):
    """n stippen in rijtjes van 5, zoals op een rekenrek."""
    r = 11; d = []
    for i in range(n):
        x = 16 + (i % 10) * 26 + (8 if i % 10 >= 5 else 0); y = 16 + (i // 10) * 26
        d.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{kleur}" stroke="{DARK}" stroke-width="1.5"/>')
    rijen = (n + 9) // 10
    return svg(282, 8 + rijen * 26, "".join(d), 330)


def munt(w, briefje=False):
    if briefje:
        return svg(110, 60, f'<rect x="3" y="3" width="104" height="54" rx="6" fill="#e8f0dc" stroke="{DARK}" stroke-width="2"/>'
                             f'<text x="55" y="38" font-size="20" font-weight="700" text-anchor="middle" fill="{DARK}">€ {w}</text>', 90)
    return svg(64, 64, f'<circle cx="32" cy="32" r="28" fill="#f2d98a" stroke="#a07b1f" stroke-width="3"/>'
                       f'<text x="32" y="39" font-size="18" font-weight="700" text-anchor="middle" fill="#5a4410">€{w}</text>', 54)

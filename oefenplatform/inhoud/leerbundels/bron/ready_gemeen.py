# -*- coding: utf-8 -*-
"""Gedeelde stijl en maakfunctie voor de Ready-bundels (3de en 4de leerjaar).
Ready is voor kinderen van 8 en 9: grotere letters, hogere schrijflijnen en
grotere vakjes, want de fijne motoriek is nog volop in ontwikkeling (Kim, 26/11)."""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel, oefenbundel

GROOT = ("body{font-size:13.5pt;line-height:1.7}table{font-size:12pt}figcaption{font-size:11pt}"
         ".oef .vraagtekst,.rij .cel{font-size:13pt}.hoe li,.opdracht{font-size:12pt}"
         ".lijn{height:54px}.vakje{height:38px;min-width:120px !important}.rij .cel{line-height:2.8}")
# Ruitjes van 1 cm in tekenvakken: om onder elkaar te cijferen en om figuren te tekenen.
RUITJES = (".tekenvak{background-image:linear-gradient(#d9d4c7 1px,transparent 1px),"
           "linear-gradient(90deg,#d9d4c7 1px,transparent 1px);background-size:10mm 10mm}")
READY = "🎒 Ready — 3de en 4de leerjaar"
DARK, ORANJE, PAARS, GROEN = "#2f4a22", "#c4622d", "#7a5aa6", "#6f9a4a"
tabel = bundel.tabel
_basis = (bundel.CSS, oefenbundel.OEFEN_CSS)


def svg(b, h, inhoud, breed=None):
    return f'<svg viewBox="0 0 {b} {h}" width="{breed or b}" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">{inhoud}</svg>'


# Grotere tekeningen in de oefenbundel (kompasroos, stroomkring, plant): voor de
# wereldoriëntatie-bundels van Ready, waar de kinderen in de tekening schrijven.
GROTE_FIGUREN = ".figcel .tekening{height:auto;min-height:96px}.figcel svg{max-height:230px;max-width:320px}"


def maak(naam, vakmap, leer, oefen, ruitjes=False, grote_figuren=False):
    import math  # noqa: F401
    bundel.CSS = _basis[0] + GROOT
    oefenbundel.OEFEN_CSS = _basis[1] + GROOT + (RUITJES if ruitjes else "") + (GROTE_FIGUREN if grote_figuren else "")
    for maker, b, basis, n in ((bundel, leer, HIER.parent, naam),
                               (oefenbundel, oefen, HIER.parent.parent / "oefenbundels", "oefenbundel-" + naam)):
        tijdelijk = "ready-" + n
        maker.schrijf(b, tijdelijk)
        subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True, capture_output=True)
        doel = basis / vakmap / f"{n}.pdf"
        doel.write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
        print("  ", doel.relative_to(HIER.parent.parent))

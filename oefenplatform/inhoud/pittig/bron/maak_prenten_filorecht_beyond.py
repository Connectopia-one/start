"""Tekent de prenten voor de pittige vragen filosofie en recht 🌍 Beyond doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_filorecht_beyond.py

Elk thema in beyond_filorecht_themas/ kan een lijst PRENTEN_EIGEN hebben:
dicts met naam (bestandsnaam zonder .svg), titel en eigen (een functie die de
SVG-stukken teruggeeft). Alles is eigen tekenwerk, dus Kim hoeft niets te
zoeken. De klikvakken staan in hetzelfde themabestand, zodat vraag en prent
nooit uit elkaar lopen.
"""
import importlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from beyond_filorecht_themas import prentmaat as pm  # noqa: E402
import beyond_filorecht as basis  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "filosofie-recht-beyond"
FONT = 'font-family="Arial, sans-serif"'


def teken(g):
    d = [f'<rect width="{pm.B}" height="{pm.H}" fill="#fffdf7"/>', *g["eigen"]()]
    if g.get("titel"):
        d.append(pm.s_tekst(pm.B / 2, 36, g["titel"], 22, vet=True))
    svg = "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pm.B} {pm.H}" width="{pm.B}" height="{pm.H}" {FONT}>', *d, "</svg>"])
    (UIT / f"{g['naam']}.svg").write_text(svg + "\n", encoding="utf-8")


def main():
    UIT.mkdir(parents=True, exist_ok=True)
    n = 0
    for naam, _ in basis.THEMAS:
        mod = importlib.import_module(f"beyond_filorecht_themas.{naam}")
        for g in getattr(mod, "PRENTEN_EIGEN", []):
            teken(g)
            n += 1
    print(f"{n} prenten in {UIT}")


if __name__ == "__main__":
    main()

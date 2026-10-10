# -*- coding: utf-8 -*-
"""Maakt katex-inline.css: de opmaak van KaTeX met de lettertypes erin.

    python3 maak_katex_css.py

Waarom dit bestaat: een bundel wordt een pdf door chromium het html-bestand
hiernaast te laten openen en af te drukken (zie pdf.js). Chromium opent dat
bestand als file://, en een lettertype dat zo'n pagina van schijf probeert te
halen, wordt geweigerd. Daarom staan de lettertypes niet naast het css-bestand
maar erin, als data-url.

Enkel de woff2-bestanden gaan mee: chromium kan die allemaal, en de ttf- en
woff-varianten ernaast zouden het bestand verdrievoudigen zonder dat er één
teken bij komt.

Draai dit opnieuw na een `npm install katex@...` met een ander versienummer.
Het resultaat is ongeveer 360 KB en staat in de repo, zodat je niet eerst
node_modules nodig hebt om een bundel te kunnen maken.

Zie oefenplatform/lib/wiskunde.ts voor hoe je een formule schrijft.
"""
import base64
import json
import pathlib
import re

HIER = pathlib.Path(__file__).parent
KATEX = HIER.parents[2] / "node_modules" / "katex" / "dist"
DOEL = HIER / "katex-inline.css"


def met_lettertypes(css: str) -> str:
    """Zet elke verwijzing naar een woff2-bestand om in een data-url."""

    def vervang(m: re.Match) -> str:
        stukken = []
        for url, soort in re.findall(
            r'url\(([^)]+)\)\s*format\("([^"]+)"\)', m.group(0)
        ):
            if soort != "woff2":
                continue
            data = base64.b64encode((KATEX / url.strip("\"'")).read_bytes()).decode()
            stukken.append(f'url("data:font/woff2;base64,{data}") format("woff2")')
        return "src:" + ",".join(stukken) if stukken else m.group(0)

    return re.sub(r"src:url\([^;}]*", vervang, css)


def main():
    if not KATEX.exists():
        raise SystemExit(
            f"KaTeX niet gevonden in {KATEX}.\n"
            "Draai eerst `npm install` in de map oefenplatform."
        )
    versie = json.loads((KATEX.parent / "package.json").read_text(encoding="utf-8"))[
        "version"
    ]
    css = met_lettertypes((KATEX / "katex.min.css").read_text(encoding="utf-8"))
    DOEL.write_text(
        f"/* KaTeX {versie}, met de lettertypes erin.\n"
        "   Gemaakt door maak_katex_css.py; pas dat bestand aan, niet dit.\n"
        "   Zie oefenplatform/lib/wiskunde.ts voor waarom formules bestaan. */\n"
        + css,
        encoding="utf-8",
    )
    print(f"{DOEL.name}: KaTeX {versie}, {round(DOEL.stat().st_size / 1024)} KB")


if __name__ == "__main__":
    main()

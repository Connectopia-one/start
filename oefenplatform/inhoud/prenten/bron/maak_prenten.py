#!/usr/bin/env python3
"""
Zet de prenten klaar die bóven de vragen van een hoofdstuk komen te staan.

Kim op 29 september 2026, over de taalvakken: "op het examencommissie moeten ze
ook beelden beschrijven in de taalvakken, hier krijg je dan een foto of prent
en moet je beschrijven wat je ziet ... zoals de teksten begrijpend lezen zijn
maar dan met een prent."

Een geschreven beschrijving kan het platform niet nakijken, maar dezelfde
woordenschat (er is en er zijn, links en rechts, kleuren, aantallen, wie wat
doet) valt wel met meerkeuze te toetsen. De prent blijft dan boven de vragen
staan, net als de leestekst bij begrijpend lezen.

Gebruik:

    python3 inhoud/prenten/bron/maak_prenten.py <vakslug> <map met prenten>

De bestandsnaam is de titel van het hoofdstuk, bijvoorbeeld
"Een prent beschrijven.png". Die naam wordt op dezelfde manier vereenvoudigd
als de hoofdstuktitel in het platform, dus het hoofdstuk vindt zijn prent zelf;
er hoeft niets in de databank en Kim hoeft geen SQL te draaien.

Anders dan bij de legpuzzel blijft een prent hier **1200 px** breed. Een kind
moet er de slak op een steen en het lieveheersbeestje op kunnen zien; op 900 px
verdwijnen die in de ruis.
"""

import re
import sys
import unicodedata
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parents[3]  # oefenplatform/
DOEL = HIER / "public" / "prenten"
LIJST = HIER / "inhoud" / "prenten.ts"
MAXBREEDTE = 1200


def slug(tekst: str) -> str:
    """Zelfde vereenvoudiging als lib/slug.ts, zodat de sleutels gelijklopen."""
    zonder = unicodedata.normalize("NFD", tekst)
    zonder = "".join(t for t in zonder if unicodedata.category(t) != "Mn")
    zonder = zonder.lower()
    zonder = re.sub(r"[^a-z0-9]+", "-", zonder)
    return zonder.strip("-")


def zet_klaar(vak: str, map_in: Path) -> None:
    uit = DOEL / vak
    uit.mkdir(parents=True, exist_ok=True)
    gedaan = 0
    for pad in sorted(map_in.iterdir()):
        if pad.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        naam = slug(pad.stem)
        beeld = Image.open(pad).convert("RGB")
        if beeld.width > MAXBREEDTE:
            hoogte = round(beeld.height * MAXBREEDTE / beeld.width)
            beeld = beeld.resize((MAXBREEDTE, hoogte), Image.LANCZOS)
        beeld.save(uit / f"{naam}.webp", "WEBP", quality=86, method=6)
        print(f"  {pad.name}  ->  {vak}/{naam}.webp  ({beeld.width}x{beeld.height})")
        gedaan += 1
    print(f"{gedaan} prent(en) klaargezet voor {vak}")


def maak_lijst() -> None:
    """Schrijft inhoud/prenten.ts met alles wat in public/prenten staat."""
    rijen = {}
    for pad in sorted(DOEL.rglob("*.webp")):
        vak = pad.parent.name
        with Image.open(pad) as beeld:
            breedte, hoogte = beeld.size
        rijen[f"{vak}/{pad.stem}"] = (f"/prenten/{vak}/{pad.name}", breedte, hoogte)

    regels = [
        "/*",
        "  Gemaakt door inhoud/prenten/bron/maak_prenten.py — niet met de hand",
        "  aanpassen.",
        "",
        "  De prent die boven de vragen van een hoofdstuk staat, voor de vakken",
        '  waar je moet beschrijven wat je ziet. De sleutel is "<vak>/<hoofdstuk>",',
        "  allebei vereenvoudigd zoals lib/slug.ts het doet. Staat een hoofdstuk",
        "  hier niet in, dan staat er gewoon geen prent boven de vragen.",
        "*/",
        "",
        "export const PRENTEN: Record<",
        "  string,",
        "  { url: string; breedte: number; hoogte: number }",
        "> = {",
    ]
    for sleutel, (url, breedte, hoogte) in sorted(rijen.items()):
        regels.append(f'  "{sleutel}": {{')
        regels.append(f'    url: "{url}",')
        regels.append(f"    breedte: {breedte},")
        regels.append(f"    hoogte: {hoogte},")
        regels.append("  },")
    regels.append("};")
    regels.append("")
    LIJST.write_text("\n".join(regels), encoding="utf-8")
    print(f"{len(rijen)} prent(en) in inhoud/prenten.ts")


def main() -> None:
    if len(sys.argv) == 3:
        map_in = Path(sys.argv[2])
        if not map_in.is_dir():
            sys.exit(f"{map_in} is geen map")
        zet_klaar(sys.argv[1], map_in)
    elif len(sys.argv) != 1:
        sys.exit(__doc__)
    maak_lijst()


if __name__ == "__main__":
    main()

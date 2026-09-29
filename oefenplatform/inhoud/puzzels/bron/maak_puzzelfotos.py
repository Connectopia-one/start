#!/usr/bin/env python3
"""
Zet prenten klaar voor de legpuzzel op de eindhalte.

Kim maakte op 29 september 2026 een prent per hoofdstuk. De tekeningen uit de
leerbundels werken wel als puzzel, maar het zijn schema's: een stukje van een
rooster ziet er precies hetzelfde uit als het stukje ernaast. Met een echte
prent wordt het pas een puzzel.

Gebruik:

    python3 inhoud/puzzels/bron/maak_puzzelfotos.py <vakslug> <map met prenten>

De bestandsnaam van een prent is de titel van het hoofdstuk, bijvoorbeeld
"Rekenen en breuken.png" of "Rekenen en breuken - pittig.png". Die naam wordt
op dezelfde manier vereenvoudigd als de hoofdstuktitel in het platform, dus de
puzzel vindt zichzelf; er hoeft niets in de databank.

Het script verkleint elke prent tot hoogstens 900 px breed en bewaart ze als
webp. Een prent van ChatGPT weegt al gauw 1,5 MB; zo blijft het onder de
100 kB en blijft de tak licht genoeg om mee te werken.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parents[3]  # oefenplatform/
DOEL = HIER / "public" / "puzzels"
LIJST = HIER / "inhoud" / "puzzelfotos.ts"
MAXBREEDTE = 900


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
        beeld.save(uit / f"{naam}.webp", "WEBP", quality=82, method=6)
        print(f"  {pad.name}  ->  {vak}/{naam}.webp  ({beeld.width}x{beeld.height})")
        gedaan += 1
    print(f"{gedaan} prent(en) klaargezet voor {vak}")


def maak_lijst() -> None:
    """Schrijft inhoud/puzzelfotos.ts met alles wat in public/puzzels staat."""
    rijen = {}
    for pad in sorted(DOEL.rglob("*.webp")):
        vak = pad.parent.name
        with Image.open(pad) as beeld:
            verhouding = round(beeld.width / beeld.height, 4)
        rijen[f"{vak}/{pad.stem}"] = {
            "url": f"/puzzels/{vak}/{pad.name}",
            "verhouding": verhouding,
        }

    regels = [
        "/*",
        "  Gemaakt door inhoud/puzzels/bron/maak_puzzelfotos.py — niet met de hand",
        "  aanpassen.",
        "",
        "  De prenten voor de legpuzzel op de eindhalte, per hoofdstuk. De sleutel is",
        '  "<vak>/<hoofdstuk>", allebei vereenvoudigd zoals lib/slug.ts het doet. Staat',
        "  een hoofdstuk hier niet in, dan valt de puzzel terug op een tekening uit de",
        "  leerbundel.",
        "*/",
        "",
        "export const PUZZELFOTOS: Record<string, { url: string; verhouding: number }> =",
        "  {",
    ]
    # Met de hand opgemaakt in de stijl van prettier (sleutels van een object
    # zonder aanhalingstekens), anders schrijft prettier het bestand elke keer
    # opnieuw en staat er telkens een diff die niets betekent.
    for sleutel, rij in rijen.items():
        regels += [
            f'    "{sleutel}": {{',
            f'      url: "{rij["url"]}",',
            f'      verhouding: {rij["verhouding"]},',
            "    },",
        ]
    regels += [
        "  };",
        "",
    ]
    LIJST.write_text("\n".join(regels), encoding="utf-8")
    print(f"{len(rijen)} prent(en) in inhoud/puzzelfotos.ts")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        zet_klaar(sys.argv[1], Path(sys.argv[2]))
    elif len(sys.argv) != 1:
        print(__doc__)
        raise SystemExit(1)
    maak_lijst()

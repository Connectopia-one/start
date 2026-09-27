# -*- coding: utf-8 -*-
"""Pakt de pdf's samen in zips: één per vak en per categorie, en één met alles.

    python3 maak_zips.py

Waarom: op /beheer/leerstof kies je een vak en sleep je alle pdf's van dat vak
in één keer naar binnen. Daarvoor moeten ze wel op je eigen computer staan, en
ze stuk voor stuk downloaden is een avond werk.

Waarom per vak, en niet alleen alles samen: Kim vroeg dat op 27 september 2026,
zodat ze een vak al kan opladen terwijl er aan het volgende gewerkt wordt.

Waarom óók per categorie: vanaf ✨ Spark heeft hetzelfde vak bundels in twee
categorieën. Wie Spark aan het opladen is, wil de bundels van 🌱 Start er niet
bij, want die staan er al. `wiskunde-spark.zip` bevat dus enkel Spark.

De categorie staat in de bundel zelf (de sleutel `niveau`), niet in de
bestandsnaam: bij lang niet elke bundel staat ze in de naam, en raden op een
naam gaat vroeg of laat mis. Daarom leest dit script de maak_*.py-bestanden in,
net zoals maak_alles.py dat doet.

In elke zip zit per vak een map, ook in een zip van één vak. Zo kan je twee
zips naast elkaar uitpakken zonder dat de bestanden door elkaar lopen.

De zips worden opnieuw gemaakt door maak_alles.py, zodat ze nooit achterlopen
op de pdf's ernaast.
"""
import importlib, pathlib, re, sys, unicodedata, zipfile

HIER = pathlib.Path(__file__).parent
WORTEL = HIER.parent.parent                      # inhoud/
sys.path.insert(0, str(HIER))

SOORTEN = [
    ("leerbundels", WORTEL / "leerbundels", "BUNDELS", "alle-leerbundels.zip"),
    ("oefenbundels", WORTEL / "oefenbundels", "OEFENBUNDELS", "alle-oefenbundels.zip"),
]

# De sleutel `niveau` is een hele zin ("✨ Spark — 1ste en 2de middelbaar").
# Hieruit halen we het korte woord dat in de bestandsnaam van de zip komt.
NIVEAUWOORDEN = ["basis", "start", "spark", "boost", "beyond"]


def slug(naam):
    plat = unicodedata.normalize("NFKD", naam).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plat.lower()).strip("-")


def niveau_van(bundeldict):
    """Het korte woord van de categorie. Staat er niets, dan is het 🌱 Start:
    dat is de standaard in bundel.py en oefenbundel.py."""
    tekst = bundeldict.get("niveau", "").lower()
    for woord in NIVEAUWOORDEN:
        if woord in tekst:
            return woord
    return "start"


def lees_niveaus(sleutel):
    """Geeft {bestandsnaam zonder .pdf: niveau} voor alle bundels van dit soort."""
    uit = {}
    for pad in sorted(HIER.glob("maak_*.py")):
        if pad.name in ("maak_alles.py", "maak_zips.py"):
            continue
        mod = importlib.import_module(pad.stem)
        for naam, b in getattr(mod, sleutel, {}).items():
            uit[naam] = niveau_van(b)
    return uit


def _schrijf(doel, pdfs):
    with zipfile.ZipFile(doel, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pdfs:
            z.write(p, f"{p.parent.name}/{p.name}")
    return doel.stat().st_size / 1024 / 1024


def maak(map_, sleutel, zipnaam):
    """Eén zip per vak en per categorie, plus één met alles erin."""
    niveaus = lees_niveaus(sleutel)
    # bron/ staat vol met tussenbestanden en hoort er niet in
    vakken = sorted(m for m in map_.iterdir() if m.is_dir() and m.name != "bron")
    regels = []
    alles = []
    gemaakt = set()

    for vak in vakken:
        pdfs = sorted(vak.glob("*.pdf"))
        if not pdfs:
            continue
        alles += pdfs
        per_niveau = {}
        for p in pdfs:
            per_niveau.setdefault(niveaus.get(p.stem, "start"), []).append(p)
        for niveau, lijst in sorted(per_niveau.items()):
            doel = map_ / f"{vak.name}-{niveau}.zip"
            mb = _schrijf(doel, lijst)
            gemaakt.add(doel.name)
            regels.append(f"{map_.name}/{doel.name}: {len(lijst)} pdf, {mb:.1f} MB")

    if alles:
        mb = _schrijf(map_ / zipnaam, alles)
        gemaakt.add(zipnaam)
        regels.append(f"{map_.name}/{zipnaam}: {len(alles)} pdf, {mb:.1f} MB")

    # Zips van een vorige indeling (wiskunde.zip zonder categorie) laten liggen
    # zou betekenen dat iemand een verouderde zip downloadt zonder het te zien.
    for oud in map_.glob("*.zip"):
        if oud.name not in gemaakt:
            oud.unlink()
            regels.append(f"{map_.name}/{oud.name}: weggehaald, oude indeling")
    return regels


def main():
    for naam, map_, sleutel, zipnaam in SOORTEN:
        if not map_.exists():
            continue
        regels = maak(map_, sleutel, zipnaam)
        if not regels:
            print(f"{naam}: niets gevonden")
        for r in regels:
            print(" ", r)


if __name__ == "__main__":
    main()

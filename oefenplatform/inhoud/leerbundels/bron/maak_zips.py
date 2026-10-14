# -*- coding: utf-8 -*-
"""Pakt de pdf's samen in zips: één per vak en één per richting.

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

# De laatste kolom: ook één zip per categorie, met alle vakken van die
# categorie samen, elk vak in zijn eigen map. Kim vroeg dat op 14 oktober 2026
# voor alle drie de soorten: "van elke richting alle vakken (...) zodat ik
# gewoon kan uitpakken per richting en dan per vak, want zo moet ik ze
# uploaden." Zo past één download precies op één avond opladen.
#
# De kolom ervoor is de naam van de zip met álles erin. Die staat op None:
# alle-leerbundels.zip woog 92 MB, en zo'n zip is niet bruikbaar om mee op te
# laden (je moet er dan zelf per vak uit gaan vissen). De zips per richting
# hebben ze vervangen.
SOORTEN = [
    ("leerbundels", WORTEL / "leerbundels", "BUNDELS", None, True),
    ("oefenbundels", WORTEL / "oefenbundels", "OEFENBUNDELS", None, True),
    ("uitlegbladen", WORTEL / "uitlegbladen", "UITLEGBLADEN", None, True),
]

# De sleutel `niveau` is een hele zin ("✨ Spark — 1ste en 2de middelbaar").
# Hieruit halen we het korte woord dat in de bestandsnaam van de zip komt.
# Het langste woord eerst: "boost doorstroom" mag niet als "boost" gelezen
# worden. In de zipnaam komt het met koppeltekens, zoals de categorie heet in
# lib/niveaus.ts.
NIVEAUWOORDEN = [
    ("boost doorstroom", "boost-doorstroom"),
    ("boost dubbele finaliteit", "boost-dubbele-finaliteit"),
    ("beyond dubbele finaliteit", "beyond-dubbele-finaliteit"),
    ("beyond doorstroom", "beyond-doorstroom"),
    ("basis", "basis"),
    ("start", "start"),
    ("spark", "spark"),
    # De oudste bundels van 🌍 Beyond zeggen enkel "Beyond" in hun
    # niveauzin, zonder "doorstroom". Toch horen ze daar: het oefenplatform
    # kent geen categorie "beyond", enkel beyond-doorstroom en
    # beyond-dubbele-finaliteit (lib/niveaus.ts). Zonder deze regel viel
    # doorstroom uiteen in twee zips, een met elf vakken en een met drie, en
    # moest Kim per document gaan zoeken bij welke richting het hoorde.
    ("beyond", "beyond-doorstroom"),
]


def slug(naam):
    plat = unicodedata.normalize("NFKD", naam).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plat.lower()).strip("-")


def niveau_van(bundeldict):
    """Het korte woord van de categorie. Staat er niets, dan is het 🌱 Start:
    dat is de standaard in bundel.py en oefenbundel.py."""
    tekst = bundeldict.get("niveau", "").lower()
    for woord, kort in NIVEAUWOORDEN:
        if woord in tekst:
            return kort
    return "start"


def lees_niveaus(sleutel):
    """Geeft {bestandsnaam zonder .pdf: niveau} voor alle bundels van dit soort."""
    uit = {}
    for pad in sorted(HIER.glob("maak_*.py")):
        if pad.name in ("maak_alles.py", "maak_zips.py"):
            continue
        mod = importlib.import_module(pad.stem)
        for naam, b in getattr(mod, sleutel, {}).items():
            if sleutel == "UITLEGBLADEN":
                # Een uitlegblad heeft zelf geen vak en geen categorie: het
                # erft ze van de oefenbundel waar het bij hoort.
                naam = naam.replace("oefenbundel-", "uitlegblad-")
                b = mod.OEFENBUNDELS[naam.replace("uitlegblad-", "oefenbundel-")]
            uit[naam] = niveau_van(b)
    return uit


def _schrijf(doel, pdfs):
    with zipfile.ZipFile(doel, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pdfs:
            z.write(p, f"{p.parent.name}/{p.name}")
    return doel.stat().st_size / 1024 / 1024


def maak(map_, sleutel, zipnaam, samen_per_niveau=False):
    """Eén zip per vak en per categorie, plus één met alles erin."""
    niveaus = lees_niveaus(sleutel)
    # bron/ staat vol met tussenbestanden en hoort er niet in
    vakken = sorted(m for m in map_.iterdir() if m.is_dir() and m.name != "bron")
    regels = []
    alles = []
    wezen = []
    gemaakt = set()
    alles_per_niveau = {}

    for vak in vakken:
        pdfs = sorted(vak.glob("*.pdf"))
        if not pdfs:
            continue
        per_niveau = {}
        for p in pdfs:
            # Een pdf die in geen enkele maak_*.py voorkomt, is blijven liggen na
            # een hernoeming. Vroeger belandde die stil in de zip van 🌱 Start,
            # en kreeg een ouder dus een verouderde bundel mee zonder het te
            # zien. Nu laten we hem eruit en zeggen we het.
            if p.stem not in niveaus:
                wezen.append(f"{map_.name}/{vak.name}/{p.name}")
                continue
            alles.append(p)
            per_niveau.setdefault(niveaus[p.stem], []).append(p)
            alles_per_niveau.setdefault(niveaus[p.stem], []).append(p)
        for niveau, lijst in sorted(per_niveau.items()):
            doel = map_ / f"{vak.name}-{niveau}.zip"
            mb = _schrijf(doel, lijst)
            gemaakt.add(doel.name)
            regels.append(f"{map_.name}/{doel.name}: {len(lijst)} pdf, {mb:.1f} MB")

    if samen_per_niveau:
        for niveau, lijst in sorted(alles_per_niveau.items()):
            doel = map_ / f"alle-vakken-{niveau}.zip"
            mb = _schrijf(doel, lijst)
            gemaakt.add(doel.name)
            regels.append(f"{map_.name}/{doel.name}: {len(lijst)} pdf, {mb:.1f} MB")

    if alles and zipnaam:
        mb = _schrijf(map_ / zipnaam, alles)
        gemaakt.add(zipnaam)
        regels.append(f"{map_.name}/{zipnaam}: {len(alles)} pdf, {mb:.1f} MB")

    # Zips van een vorige indeling (wiskunde.zip zonder categorie) laten liggen
    # zou betekenen dat iemand een verouderde zip downloadt zonder het te zien.
    for oud in map_.glob("*.zip"):
        if oud.name not in gemaakt:
            oud.unlink()
            regels.append(f"{map_.name}/{oud.name}: weggehaald, oude indeling")

    for w in wezen:
        regels.append(f"LET OP {w}: hoort bij geen enkele bundel, niet mee ingepakt")
    return regels


def main():
    for naam, map_, sleutel, zipnaam, samen in SOORTEN:
        if not map_.exists():
            continue
        regels = maak(map_, sleutel, zipnaam, samen)
        if not regels:
            print(f"{naam}: niets gevonden")
        for r in regels:
            print(" ", r)


if __name__ == "__main__":
    main()

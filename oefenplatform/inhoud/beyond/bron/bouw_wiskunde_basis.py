# -*- coding: utf-8 -*-
"""Zet de themabestanden `wb3_*.py` samen in ../wiskunde-basis.json.

    python3 bron/bouw_wiskunde_basis.py

🌍 Beyond, derde graad. Kim op 9 november 2026: "Ik zou wiskunde al heel
graag in orde maken." Van de vakfiche 2027_wiskunde_3DO_Basis, geldig van
1 januari tot en met 31 december 2027, voor Latijn-moderne talen, moderne
talen en humane wetenschappen. Gelezen op Kims usb-stick
(E:\\vakfiches examencommissie\\3 doorstroom humane wetenschappen).

Het examen duurt 150 minuten, digitaal, enkel gesloten vragen, zonder
giscorrectie. Gewichten: analyse 65 %, kansrekenen en statistiek 35 %.
Daarom acht thema's analyse en drie thema's kansrekenen en statistiek.

Welzijnswetenschappen volgt de fiche 2027_wiskunde_3DO_WEL. Die is woord voor
woord dezelfde, behalve dat tweedegraadsfuncties en het algebraïsch oplossen
van tweedegraadsvergelijkingen ontbreken (analyse 60 %, kansrekenen en
statistiek 40 %). Die twee thema's staan daarom apart, zodat een leerling
welzijnswetenschappen ze kan overslaan.

Wat de fiche niet vraagt, staat er niet in: geen logaritmische functies, geen
limieten van functies buiten het informele limietbegrip, geen afgeleiden
berekenen met rekenregels, geen telproblemen, geen hypothesetoetsen. Die
horen bij wiskunde gevorderd of bij de fiche van bedrijfswetenschappen.

Bij wiskunde geen meerkeuze met meerdere juiste antwoorden (Kim, 23
september 2026). Elk thema is een bestand met DEEL1 en DEEL2 van twintig
vragen, en wordt hier twee hoofdstukken "<thema> — deel 1" en "— deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parents[1]))

from notatie import sluitend, zichtbaar  # noqa: E402  (pad moet eerst klaarstaan)
DOEL = HIER.parent / "wiskunde-basis.json"

# De volgorde volgt de drie fiches: eerst G1, de analyse van functies, dan G2
# met de integralen, de complexe getallen en de kansrekening, en ten slotte G3
# met de algebra, de ruimtemeetkunde en het programmeren. Binnen G1 loopt ze
# van het rekengereedschap naar het functieonderzoek.
THEMAS = [
    ("wb3_machten", "Machtswortels, machten en logaritmen"),
    ("wb3_grafisch", "Grafisch onderzoek van een functie"),
    ("wb3_tweedegraad", "Tweedegraadsfuncties"),
    ("wb3_tweedegraadsvgl", "Tweedegraadsvergelijkingen algebraïsch oplossen"),
    ("wb3_exponentieel", "Exponentiële functies en groeimodellen"),
    ("wb3_sinus", "De sinusfunctie en de goniometrische cirkel"),
    ("wb3_vergelijkingen", "Vergelijkingen grafisch oplossen"),
    ("wb3_afgeleiden", "Afgeleiden: helling en raaklijn"),
    ("wb3_rijen", "Rekenkundige en meetkundige rijen"),
    ("wb3_kansen", "Kansrekenen met kansbomen en kruistabellen"),
    ("wb3_steekproeven", "Steekproeven, samenhang en causaliteit"),
    ("wb3_normaal", "De normale verdeling"),
]

# Enkel voor bedrijfswetenschappen. De titel begint met "Bedrijfswetenschappen: ",
# en daardoor laat de keuze "Ik leer voor" (inhoud/vaknoten.ts, weglaten) deze
# hoofdstukken weg bij een andere richting en bij welzijnswetenschappen.
BED = "Bedrijfswetenschappen: "
THEMAS += [
    ("wbb_ongelijkheden", BED + "ongelijkheden oplossen"),
    ("wbb_expgonio", BED + "exponentiële en goniometrische vergelijkingen"),
    ("wbb_rekenregels", BED + "afgeleiden berekenen met rekenregels"),
    ("wbb_verloop", BED + "verloop van een functie en optimaliseren"),
    ("wbb_integralen", BED + "integralen en oppervlakte"),
    ("wbb_matrices", BED + "matrices, grafen en stelsels"),
    ("wbb_toetsen", BED + "hypothesetoetsen en correlatie"),
]


def controleer(titel: str, nummer: int, vraag: dict):
    plek = f"{titel}: vraag {nummer}"
    soort = vraag["type"]
    if soort == "meerkeuze":
        opties = vraag["opties"]
        if len(opties) < 3:
            raise SystemExit(f"{plek} heeft maar {len(opties)} opties")
        if len(set(opties)) != len(opties):
            raise SystemExit(f"{plek} heeft twee gelijke opties")
        antwoord = vraag["antwoord"]
        nummers = antwoord if isinstance(antwoord, list) else [antwoord]
        if isinstance(antwoord, list) and len(set(nummers)) < 2:
            raise SystemExit(f"{plek} moet minstens twee juiste antwoorden hebben")
        if len(set(nummers)) != len(nummers):
            raise SystemExit(f"{plek} noemt hetzelfde antwoord twee keer")
        if any(not isinstance(a, int) or not 0 <= a < len(opties) for a in nummers):
            raise SystemExit(f"{plek} wijst een optie aan die niet bestaat")
    elif soort == "waarofniet":
        if not isinstance(vraag["antwoord"], bool):
            raise SystemExit(f"{plek} is waar of niet waar en heeft geen boolean")
    elif soort == "invultekst":
        antwoord = vraag["antwoord"]
        antwoorden = antwoord if isinstance(antwoord, list) else [antwoord]
        if not antwoorden:
            raise SystemExit(f"{plek} heeft geen ingevuld antwoord")
        for a in antwoorden:
            if not isinstance(a, str) or not a.strip():
                raise SystemExit(f"{plek} heeft geen ingevuld antwoord")
            if len(a.split()) > 3:
                raise SystemExit(f"{plek} heeft een te lang invulantwoord: {a!r}")
    else:
        raise SystemExit(f"{plek} heeft een onbekend type: {soort}")
    if not vraag.get("uitleg"):
        raise SystemExit(f"{plek} heeft geen uitleg")


def gokpatronen(titel: str, vragen: list) -> list:
    """Kan je scoren zonder de leerstof te kennen?"""
    meldingen = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        # Op schermbreedte geteld, niet op bronbestand: zie notatie.py.
        lengtes = [len(zichtbaar(o)) for o in v["opties"]]
        # "Geen van deze antwoorden" is bijna altijd de langste optie, en die
        # lengte zegt niets over de inhoud. Zulke opties blijven hier buiten.
        vrij = [i for i, o in enumerate(v["opties"]) if not sluitend(o)]
        juist = [i for i in antw if i in vrij]
        anders = [lengtes[i] for i in vrij if i not in antw]
        if juist and anders and min(lengtes[i] for i in juist) > max(anders) + 5:
            langst += 1
    if mk and langst > 0.4 * len(mk):
        meldingen.append(
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord duidelijk de langste optie. Maak de andere opties langer."
        )
    return meldingen


def evenwicht_waar(hoofdstukken: list) -> list:
    """Waar en niet waar moeten elkaar per hoofdstuk in evenwicht houden."""
    meldingen = []
    per_thema = {}
    for h in hoofdstukken:
        for v in h["vragen"]:
            if v["type"] == "waarofniet":
                per_thema.setdefault(h["titel"], []).append(v["antwoord"])
    for thema, antwoorden in per_thema.items():
        waar = sum(1 for a in antwoorden if a)
        if not (0.35 <= waar / len(antwoorden) <= 0.65):
            meldingen.append(
                f"{thema}: {waar} van de {len(antwoorden)} waar/niet-waar-vragen is waar. "
                f"Dat is te scheef om niet te kunnen gokken."
            )
    return meldingen


def hoofdstukken_van(modulenaam: str, thema: str) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        if len(vragen) != 20:
            raise SystemExit(f"{titel} heeft {len(vragen)} vragen, verwacht 20")
        for i, vraag in enumerate(vragen, start=1):
            controleer(titel, i, vraag)
        uit.append(
            {"titel": titel, "niveau": "beyond-doorstroom", "gratis": False, "vragen": vragen}
        )
    return uit


def main():
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        if not (HIER / f"{modulenaam}.py").exists():
            print(f"  {thema}: nog niet geschreven, overgeslagen")
            continue
        nieuw = hoofdstukken_van(modulenaam, thema)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    gezien = {}
    meerkeuze = meerdere = 0
    for h in hoofdstukken:
        for v in h["vragen"]:
            tekst = " ".join(v["vraag"].lower().split())
            if tekst in gezien:
                raise SystemExit(
                    f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}"
                )
            gezien[tekst] = h["titel"]
            if v["type"] == "meerkeuze":
                meerkeuze += 1
                if isinstance(v["antwoord"], list):
                    meerdere += 1

    for h in hoofdstukken:
        for melding in gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    # Kim, 23 september 2026: bij wiskunde geen meerkeuze met meerdere juiste
    # antwoorden. Een som heeft één uitkomst; wie er twee laat aankruisen,
    # toetst het lezen van de opgave en niet het rekenen.
    if meerdere:
        raise SystemExit(
            f"{meerdere} meerkeuzevragen hebben meerdere juiste antwoorden; bij wiskunde mag dat niet"
        )
    print(f"\n{meerkeuze} meerkeuzevragen, allemaal met één juist antwoord.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()

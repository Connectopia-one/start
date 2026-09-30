# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../wiskunde.json.

    python3 bron/bouw_wiskunde.py

Boost dubbele finaliteit, tweede graad. Eén fiche voor bedrijf en organisatie
en voor maatschappij en welzijn, en ze heet gewoon **wiskunde**: geen
gevorderd en geen basis, want dubbele finaliteit splitst niet. Het is dus een
eigen vak naast wiskunde gevorderd van doorstroom.

Vijf bouwstenen, met heel andere gewichten dan bij doorstroom:

    relaties en verandering          40 %  ->  5 thema's
    meetkunde en metend rekenen      30 %  ->  4 thema's
    getallenleer                     15 %  ->  2 thema's
    data en onzekerheid            12,5 %  ->  2 thema's
    telproblemen                    2,5 %  ->  1 thema (samen met probleemoplossend denken)

**Logica en bewijzen bestaat hier niet.** Bij doorstroom is dat 10 % van het
examen, met waarheidstabellen, kwantoren en een bewijzenlijst. Op de DF-fiche
staat er geen woord over. Dat thema valt dus weg.

Negen thema's komen uit de doorstroombron. Vier zijn hier nieuw geschreven,
want de doorstroomversie dekt iets anders:

  * **Goniometrie.** Doorstroom heeft sinusregel, cosinusregel en vectoren.
    De DF-fiche vraagt enkel sinus, cosinus en tangens in een *rechthoekige*
    driehoek, plus de grondformule.
  * **Stelsels.** Doorstroom behandelt stelsels samen met
    tweedegraadsvergelijkingen. Die laatste staan niet op de DF-fiche; de
    stelsels wel, en uitgebreider: algebraïsch én grafisch, met bepaald,
    strijdig en onbepaald.
  * **Grafisch oplossen.** De DF-fiche legt het verband tussen f(x) = 0 en de
    nulwaarde, tussen f(x) > 0 en de ligging van de grafiek, en tussen
    f(x) = g(x) en de snijpunten. Bij doorstroom zit dat verspreid.
  * **Misleiding.** De doorstroomversie gaat voor de helft over een
    puntenwolk, correlatie en regressie. Die staan niet op de DF-fiche; de
    lijst misleidingen wel, en die is er lang.

**Bij wiskunde geen meerkeuze met meerdere juiste antwoorden**, net als bij
doorstroom. Een som heeft één uitkomst.

Vragen uit de doorstroommodules kunnen hier één voor één vervangen worden via
`df_wiskunde_vervangingen.py`: de sleutel is de letterlijke vraagtekst, en
staat ze er niet meer, dan stopt het script.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
DOORSTROOM = HIER.parent.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "wiskunde.json"

import df_wiskunde_vervangingen as vervang  # noqa: E402

# De volgorde loopt van het gereedschap naar de toepassing: eerst hoe je een
# opgave aanpakt, dan de getallen, dan de meetkunde, dan de algebra en de
# functies, en ten slotte tellen, meten en cijfers wegen.
THEMAS = [
    ("wi_problemen", "Een opgave aanpakken: van context naar wiskunde"),
    ("wi_reele", "Reële getallen, wortels en machten"),
    ("wi_ordenen", "Ordenen, afronden en intervallen"),
    ("wi_ruimte", "Rechten, vlakken en gelijkvormigheid"),
    ("wi_pythagoras", "Pythagoras en de rechthoekige driehoek"),
    ("widf_goniometrie", "De rechthoekige driehoek oplossen en toepassen"),
    ("wi_formules", "Formules omvormen en eerstegraadsvergelijkingen"),
    ("widf_stelsels", "Stelsels van twee eerstegraadsvergelijkingen"),
    ("wi_functies", "Functies en de rechte"),
    ("widf_grafisch", "Tekenverloop, verloopschema en grafisch oplossen"),
    ("wi_tellen", "Telproblemen met boom- en venndiagram"),
    ("wi_statistiek", "Statistiek: voorstellingen, centrum en spreiding"),
    ("widf_misleiding", "Misleiding met cijfers en grafieken"),
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
        lengtes = [len(o) for o in v["opties"]]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + 5:
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


def hoofdstukken_van(modulenaam: str, thema: str, nog_te_vervangen: dict) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, oude in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        vragen = []
        for vraag in oude:
            sleutel = " ".join(vraag["vraag"].split())
            vragen.append(nog_te_vervangen.pop(sleutel) if sleutel in nog_te_vervangen else vraag)
        if len(vragen) != 20:
            raise SystemExit(f"{titel} heeft {len(vragen)} vragen, verwacht 20")
        for i, vraag in enumerate(vragen, start=1):
            controleer(titel, i, vraag)
        uit.append(
            {"titel": titel, "niveau": "boost-dubbele-finaliteit", "gratis": False, "vragen": vragen}
        )
    return uit


def main():
    nog_te_vervangen = dict(vervang.VERVANGINGEN)
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        nieuw = hoofdstukken_van(modulenaam, thema, nog_te_vervangen)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    if nog_te_vervangen:
        raise SystemExit(
            "Deze te vervangen vragen staan niet (meer) in de doorstroombestanden:\n  "
            + "\n  ".join(nog_te_vervangen)
        )

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

# -*- coding: utf-8 -*-
"""Zet de themabestanden `ch3_*.py` samen in ../chemie.json.

    python3 bron/bouw_chemie.py

🌍 Beyond, derde graad. De vakfiche chemie van de doorstroomfinaliteit noemt
bovenaan zelf twee studierichtingen: Latijn-wiskunde met extra wetenschappen en
wetenschappen-wiskunde. Die twee leggen hun wetenschappen af in drie aparte
examens, biologie, chemie en fysica, in plaats van één examen
natuurwetenschappen. Vandaar een eigen vak naast natuurwetenschappen.

Hoe de drieëntwintig thema's volgen uit de fiche. Achteraan weegt ze haar zes
onderdelen zelf: toepassingen van chemisch evenwicht (zuurbase en redox) 30 %,
opbouw en eigenschappen van stoffen 25 %, chemisch rekenen met de dynamiek en
het evenwicht 20 %, organische reacties 10 %, wetenschappelijk onderzoek en
STEM 10 %, en kunststoffen met nanomaterialen en duurzame chemie 5 %. Die
verhouding geeft zes thema's voor de toepassingen, zes voor de opbouw, vier
voor het rekenen, twee voor de organische reacties en twee voor het onderzoek.
Het laatste onderdeel weegt maar 5 %, maar beslaat in de fiche drie koppen met
veel aparte begrippen; kunststoffen, nanomaterialen en duurzame chemie krijgen
daarom elk een eigen thema in plaats van samen één. Elk thema valt samen met
een kop of een duidelijk blok uit de fiche zelf, zodat er niets tussen valt.

Het niveau ligt een stuk hoger dan dat van natuurwetenschappen in dezelfde
graad: waar die het bij de hoofdlijn houdt, vraagt deze de vier kwantumgetallen,
het sterisch getal met het hybridisatietype, de snelheidsvergelijking met de
orde van een reactie, het verloop van een titratiecurve en de bouw van een
galvanische cel. De vragen gaan dus dieper, en geen enkele vraag is uit
natuurwetenschappen of uit chemie van 🚀 Boost overgenomen.

Drie afspraken van de fiche staan hier overgenomen. Eén: veilig en duurzaam
werken wordt op het examen niet uitgevoerd maar uitgelegd, dus vragen de
vragen daarover naar het waarom van een handeling. Twee: de tabel met
normpotentialen, het periodiek systeem en de formules staan in een bijlage die
het kind op het examen krijgt, dus hoeft het die niet van buiten te kennen,
maar moet het ze wel kunnen gebruiken; de vragen geven de nodige waarden mee.
Drie: structuurformules tekenen kan hier niet, dus wordt er naar de bouw in
woorden of in een brutoformule gevraagd.

Elk thema is een bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Dit script maakt daar twee hoofdstukken van, "<thema> — deel 1" en
"<thema> — deel 2", en schrijft het importbestand van nul af aan.

Dezelfde bewaking als bij de andere vakken: twintig vragen per deel, geen
woordelijke dubbels in het hele vak, minstens drie opties per meerkeuzevraag,
20 a 30 % vragen met meerdere juiste antwoorden, en geen raadbare patronen
(het juiste antwoord dat altijd de langste is, of waar dat te vaak waar is).
"""

import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "chemie.json"

# De volgorde volgt de fiche van voor naar achter.
THEMAS = [
    ("ch3_anorganisch", "Anorganische stoffen: stofklassen en naamgeving"),
    ("ch3_organisch", "Organische stoffen: stofklassen en naamgeving"),
    ("ch3_isomerie", "Isomerie en chiraliteit"),
    ("ch3_atoom", "Atoombouw, orbitalen en het periodiek systeem"),
    ("ch3_binding", "Atoombinding en lewisstructuren"),
    ("ch3_eigenschappen", "Ruimtelijke structuur, polariteit en intermoleculaire krachten"),
    ("ch3_rekenen", "Chemisch rekenen: mol, molaire massa en concentratie"),
    ("ch3_stoichiometrie", "Stoichiometrie, overmaat en de algemene gaswet"),
    ("ch3_snelheid", "Reactiesnelheid, botsingsmodel en energiediagram"),
    ("ch3_evenwicht", "Chemisch evenwicht en de wet van Le Chatelier"),
    ("ch3_zuren", "Zuren en basen en het doorgeven van protonen"),
    ("ch3_ph", "pH, pOH en rekenen met zuren en basen"),
    ("ch3_buffers", "Buffers en zuurbasetitraties"),
    ("ch3_redox", "Oxidatiegetallen en redoxreacties"),
    ("ch3_cellen", "Galvanische cellen en elektrolyse"),
    ("ch3_corrosie", "Toepassingen van redox: batterijen, galvaniseren en corrosie"),
    ("ch3_reactietypes", "Organische reacties: substitutie en het radicalaire mechanisme"),
    ("ch3_additie", "Organische reacties: additie, eliminatie en condensatie"),
    ("ch3_kunststoffen", "Kunststoffen: polymeren en hun eigenschappen"),
    ("ch3_nano", "Nanomaterialen"),
    ("ch3_duurzaam", "Duurzame chemie en de circulaire economie"),
    ("ch3_veilig", "Veilig werken, meetinstrumenten en beduidende cijfers"),
    ("ch3_onderzoek", "Wetenschappelijk onderzoek, ontwerpen en STEM"),
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
    """Waar en niet waar moeten elkaar per hoofdstuk in evenwicht houden.

    Per hóófdstuk, niet per thema. Een kind maakt één hoofdstuk in één keer,
    dus daar moet het gokken niet lonen. `inhoud/controleer_patronen.py` kijkt
    op diezelfde manier; stonden die twee niet gelijk, dan kwam een scheef
    hoofdstuk hier door en pas veel later daar boven water.
    """
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

    if meerkeuze:
        deel = meerdere / meerkeuze
        if not 0.20 <= deel <= 0.30:
            raise SystemExit(
                f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 20 à 30 %"
            )
        print(
            f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden."
        )

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()

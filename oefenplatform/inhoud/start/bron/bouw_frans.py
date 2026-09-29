# -*- coding: utf-8 -*-
"""Schrijft ../frans.json uit frans.py.

    python3 inhoud/start/bron/bouw_frans.py

Frans is de achtste vakdiscipline van de minimumdoelen van het lager onderwijs
en het laatste vak dat bij 🌱 Start nog ontbrak. Zeven hoofdstukken van twintig
vragen, alleen de schriftelijke kant.

Wat er nagekeken wordt voor er iets weggeschreven wordt:

  * elk hoofdstuk heeft precies twintig vragen;
  * geen vraag staat twee keer, en geen enkele vraag staat al ergens anders in
    ditzelfde niveau (dus ook niet bij Engels of Nederlands 🌱 Start);
  * elk meerkeuzeantwoord wijst naar een bestaande optie, er staan er minstens
    drie, en geen twee dezelfde;
  * elke vraag heeft uitleg;
  * het juiste antwoord is niet stelselmatig de langste optie (hoogstens vier
    op de tien), en waar en niet-waar houden elkaar in evenwicht (tussen 35 en
    65 procent waar) — dezelfde grenzen als inhoud/controleer_patronen.py;
  * bij het leeshoofdstuk staat elk woord tussen *sterretjes* in de
    woordenlijst en omgekeerd.

De harde regeleinden uit de leestekst worden hier weggehaald: een alinea wordt
één lange regel en een lege regel blijft de scheiding tussen alinea's, zodat er
in de databank niets staat dat van de bladbreedte van een editor afhangt.
"""
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "frans.json"
INHOUD = HIER.parent.parent
NIVEAU = "start"
PER_HOOFDSTUK = 20

SPELING = 6
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65


def sleutel(vraag):
    return re.sub(r"[^a-z0-9]+", " ", str(vraag).lower()).strip()


def alinea_per_regel(tekst):
    stukken = [re.sub(r"\s+", " ", s).strip() for s in re.split(r"\n\s*\n", tekst)]
    return "\n\n".join(s for s in stukken if s)


def elders():
    """Elke vraag die al ergens anders in dit niveau staat, met waar ze staat."""
    gevonden = {}
    for pad in sorted(INHOUD.glob("*/*.json")):
        # Ons eigen bestand overslaan, anders vindt een tweede keer bouwen al
        # zijn eigen vragen terug en lijkt alles dubbel te staan.
        if pad.resolve() == DOEL.resolve():
            continue
        try:
            data = json.loads(pad.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for h in data.get("hoofdstukken", []):
            if (h.get("niveau") or pad.parent.name) != NIVEAU:
                continue
            for v in h.get("vragen", []):
                gevonden.setdefault(sleutel(v.get("vraag", "")), f"{pad.name} / {h.get('titel')}")
    return gevonden


def gokpatronen(titel, vragen):
    """Kan je scoren zonder Frans te kennen?

    Twee patronen sluipen er bij het schrijven vanzelf in: het juiste antwoord
    is de langste optie, want net dat antwoord vraagt uitleg; en waar en
    niet-waar houden elkaar niet in evenwicht, zodat het loont om overal
    hetzelfde te antwoorden.
    """
    fouten = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        opties = v.get("opties") or [""]
        juist = len(opties[v["antwoord"]])
        anders = [len(o) for i, o in enumerate(opties) if i != v["antwoord"]]
        if anders and juist > max(anders) + SPELING:
            langst += 1
    if mk and langst > GRENS_LANGSTE * len(mk):
        fouten.append(
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord de langste optie. Maak de andere opties langer."
        )
    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    if wn and not (WAAR_ONDER <= sum(1 for a in wn if a) / len(wn) <= WAAR_BOVEN):
        fouten.append(
            f"{titel}: {sum(1 for a in wn if a)} van de {len(wn)} waar/niet-waar-vragen is waar."
        )
    return fouten


def leesvelden(titel, tekst, woordenlijst):
    """De leestekst en zijn woordenlijst, met de kruiscontrole ertussen."""
    fouten = []
    gemarkeerd = set(re.findall(r"\*([^*]+)\*", tekst))
    uitgelegd = {w for w, _ in woordenlijst}
    for woord in sorted(gemarkeerd - uitgelegd):
        fouten.append(f"{titel}: *{woord}* staat in de tekst maar niet in de woordenlijst")
    for woord in sorted(uitgelegd - gemarkeerd):
        fouten.append(f"{titel}: {woord} staat in de woordenlijst maar niet tussen sterretjes")
    velden = {
        "leestekst": alinea_per_regel(tekst).replace("*", ""),
        "woordenlijst": [{"woord": w, "uitleg": u} for w, u in woordenlijst],
    }
    return velden, fouten


def main():
    import frans

    fouten = []
    gezien = {}
    ergens_anders = elders()
    hoofdstukken = []

    for titel, vragen, tekst, woordenlijst in frans.HOOFDSTUKKEN:
        if len(vragen) != PER_HOOFDSTUK:
            fouten.append(f"{titel}: {len(vragen)} vragen in plaats van {PER_HOOFDSTUK}")

        for v in vragen:
            kop = f'{titel} / "{v["vraag"][:55]}"'
            s = sleutel(v["vraag"])
            if s in gezien:
                fouten.append(f"{kop}: staat ook in {gezien[s]}")
            elif s in ergens_anders:
                fouten.append(f"{kop}: staat al in {ergens_anders[s]}")
            gezien[s] = titel

            if not v.get("uitleg"):
                fouten.append(f"{kop}: geen uitleg")

            if v["type"] == "meerkeuze":
                opties = v.get("opties") or []
                if len(opties) < 3:
                    fouten.append(f"{kop}: minder dan drie opties")
                if len(set(opties)) != len(opties):
                    fouten.append(f"{kop}: twee keer dezelfde optie")
                if not isinstance(v["antwoord"], int) or not 0 <= v["antwoord"] < len(opties):
                    fouten.append(f"{kop}: antwoord wijst niet naar een optie")
            elif v["type"] == "waarofniet":
                if not isinstance(v["antwoord"], bool):
                    fouten.append(f"{kop}: waar of niet waar vraagt true of false")
                if v.get("opties"):
                    fouten.append(f"{kop}: waar of niet waar heeft geen opties")
            elif v["type"] == "invultekst":
                # Eén antwoord, of een lijstje als meerdere schrijfwijzen
                # mogen: het platform rekent ze allemaal juist.
                antwoorden = (
                    v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
                )
                if not antwoorden or not all(
                    isinstance(a, str) and a.strip() for a in antwoorden
                ):
                    fouten.append(f"{kop}: invulantwoord ontbreekt")
                if v.get("opties"):
                    fouten.append(f"{kop}: een invulvraag heeft geen opties")
            else:
                fouten.append(f"{kop}: onbekend type {v['type']}")

        fouten += gokpatronen(titel, vragen)

        hoofdstuk = {"titel": titel, "niveau": NIVEAU, "gratis": False, "vragen": vragen}
        if tekst is not None:
            velden, leesfouten = leesvelden(titel, tekst, woordenlijst or [])
            hoofdstuk.update(velden)
            fouten += leesfouten
        hoofdstukken.append(hoofdstuk)

    if fouten:
        for f in fouten:
            print("FOUT:", f)
        return 1

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"geschreven: {DOEL.name} — {len(hoofdstukken)} hoofdstukken, {totaal} vragen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

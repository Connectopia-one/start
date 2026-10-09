# -*- coding: utf-8 -*-
"""Zet de themabestanden `se_*.py` samen in ../samenleving-en-economie.json.

    python3 bron/bouw_samenleving.py

🌍 Beyond, derde graad doorstroomfinaliteit. De fiche
`2027_samenleving_en_economie_3DODU` is de breedste van alle fiches die wij
tot nu toe hebben gezien. Bladzijde 1 noemt acht studierichtingen van de
doorstroomfinaliteit — bedrijfswetenschappen, economie-wiskunde, humane
wetenschappen, Latijn-moderne talen, Latijn-wiskunde-wetenschappen, moderne
talen, welzijnswetenschappen en wetenschappen-wiskunde — én twee van de
dubbele finaliteit: commerciële organisatie en algemene vorming. Lees dat
altijd af op bladzijde 1 in plaats van het te gokken.

Kim vroeg dit vak op 9 oktober 2026, samen met sociale en gedragswetenschappen
en filosofie en recht, omdat die drie "echt apart zijn" voor
welzijnswetenschappen. Van de drie is deze fiche het nuttigst voor de meeste
kinderen, want ze geldt voor bijna iedereen in doorstroom. Daarom is ze eerst
gemaakt.

De gewichtentabel achteraan de fiche verdeelt het examen in negen blokken.
Hier staat wat elk blok weegt en hoeveel thema's het bij ons krijgt:

    ik ben wie ik ben                                  5   %  ->  1 thema
    ik leef samen met anderen                         12,5 %  ->  2 thema's
    ik reageer correct in een noodsituatie             7,5 %  ->  2 thema's
    ik maak deel uit van een sociaal rechtvaardige
        samenleving                                   10   %  ->  2 thema's
    ik begrijp de prijsvorming op de markt            10   %  ->  2 thema's
    ik ga werken                                      15   %  ->  3 thema's
    ik beheer mijn financiën                          15   %  ->  3 thema's
    ik ben verzekerd                                   7,5 %  ->  1 thema
    ik ben digitaal vaardig                           17,5 %  ->  4 thema's

Samen twintig thema's, veertig hoofdstukken, achthonderd vragen.

Drie dingen die deze fiche anders maakt dan de andere:

  1. **Het examen duurt maar negentig minuten en is volledig digitaal.** De
     fiche noemt invulvragen, sleepvragen, dropdownvragen en meerkeuzevragen.
     Dat ligt dicht bij wat ons platform al doet, dus de vraagvormen hier
     mogen gerust op het examen lijken.

  2. **Het digitale deel vraagt géén computerwerk.** De fiche zegt met
     zoveel woorden: "Je werkt niet met de programma's zelf, maar krijgt
     schermafdrukken uit Windows 10 en MS Office 365." Daarom zijn de vier
     Office-thema's hier vragen over wat een knop doet en waar iets staat,
     en niet opdrachten om zelf iets te maken.

  3. **De eerste hulp staat er met de stappen in de juiste volgorde.** Zes
     basisprincipes, vier stappen in eerste hulp, zes stappen reanimatie, en
     vier noodnummers (101 politie, 112 ziekenwagen en brandweer,
     070 245 245 antigifcentrum, 1733 huisarts). Die getallen staan letterlijk
     in de fiche; verzin er geen bij.

Werkt verder als elk ander bouwscript: elk thema is een bestand met een lijst
DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "samenleving-en-economie.json"

# De volgorde volgt de fiche van voor naar achter, zodat een kind de
# hoofdstukken in dezelfde orde terugvindt als in zijn cursus.
THEMAS = [
    ("se_identiteit", "Identiteit: de lagen, de factoren en het wereldbeeld"),
    ("se_diversiteit", "Samenleven in diversiteit"),
    ("se_omgang", "Respectvol samenleven: communicatie, grenzen en samenwerken"),
    ("se_eerstehulp", "Ongevallen herkennen en eerste hulp geven"),
    ("se_reanimatie", "Een hartstilstand, reanimatie en de AED"),
    ("se_overheid", "De inkomsten en de uitgaven van de overheid"),
    ("se_sociaal", "Sociale zekerheid, uitkeringen en herverdeling"),
    ("se_markt", "Vraag, aanbod en het marktevenwicht"),
    ("se_ingrijpen", "Verschuivingen op de markt en de overheid die ingrijpt"),
    ("se_contract", "De arbeidsovereenkomst en het arbeidsreglement"),
    ("se_loon", "Van brutoloon naar nettoloon"),
    ("se_werkvloer", "Welzijn op het werk en waar je met vragen terechtkan"),
    ("se_aankoop", "De totale aankoopkost en het consumentenkrediet"),
    ("se_budget", "Het persoonlijk budget en je administratie"),
    ("se_sparen", "Sparen, beleggen en de invloed van inflatie"),
    ("se_verzekering", "Verzekeringen, een schadegeval en de polis"),
    ("se_word", "Tekstverwerking met Word"),
    ("se_excel", "Het rekenblad Excel"),
    ("se_powerpoint", "Presenteren met PowerPoint"),
    ("se_digiregels", "Veilig en correct online: recht, phishing en netiquette"),
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
        if isinstance(antwoord, list) and len(nummers) == len(opties):
            raise SystemExit(f"{plek} heeft alle opties juist; dan valt er niets te kiezen")
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
    mk = [v for v in vragen if v["type"] == "meerkeuze" and not isinstance(v["antwoord"], list)]
    langst = 0
    for v in mk:
        a = v["antwoord"]
        lengtes = [len(o) for o in v["opties"]]
        anders = [lengtes[i] for i in range(len(lengtes)) if i != a]
        if anders and lengtes[a] > max(anders) + 5:
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
    meerkeuze = meerdere = invul = waarofniet = 0
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
            invul += v["type"] == "invultekst"
            waarofniet += v["type"] == "waarofniet"

    for h in hoofdstukken:
        for melding in gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    if meerkeuze:
        deel = meerdere / meerkeuze
        if not 0.10 <= deel <= 0.25:
            raise SystemExit(
                f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 10 à 25 %"
            )
        print(
            f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden."
        )
    print(f"{meerkeuze} meerkeuzevragen, {waarofniet} waar of niet waar, {invul} invulvragen.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()

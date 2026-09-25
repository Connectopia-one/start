# -*- coding: utf-8 -*-
"""Schrijft ../nederlands-begrijpend-lezen.json uit begrijpend_lezen.py.

    python3 inhoud/start/bron/bouw_begrijpend_lezen.py

Dezelfde bouwer dient voor ✨ Spark; die geeft zijn eigen module mee:

    python3 inhoud/start/bron/bouw_begrijpend_lezen.py spark

Wat er nagekeken wordt voor er iets weggeschreven wordt:
  * geen vraag twee keer;
  * elk meerkeuze-antwoord wijst naar een bestaande optie, en bij een lijstje
    antwoorden staan er minstens twee in;
  * elk invulantwoord staat letterlijk in de tekst, tenzij vrij=True;
  * elk woord tussen sterretjes staat in de woordenlijst, en elk woord uit de
    woordenlijst staat tussen sterretjes in de tekst;
  * elke vraag heeft uitleg;
  * het juiste antwoord is niet stelselmatig de langste optie (wie altijd de
    langste aanklikt, mag niet meer dan vier op de tien juist hebben);
  * waar en niet-waar houden elkaar in evenwicht, anders loont het om altijd
    hetzelfde te antwoorden.

De harde regeleinden uit het bronbestand worden hier weggehaald: een alinea
wordt één lange regel, en een lege regel blijft de scheiding tussen alinea's.
Zo staat er in de databank niets dat van de bladbreedte van een editor afhangt.
"""
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent


def alinea_per_regel(tekst):
    stukken = [re.sub(r"\s+", " ", s).strip() for s in re.split(r"\n\s*\n", tekst)]
    return "\n\n".join(s for s in stukken if s)


def zonder_sterretjes(tekst):
    return tekst.replace("*", "")


def sleutel(vraag):
    return re.sub(r"[^a-z0-9]+", " ", vraag.lower()).strip()


def normaliseer(tekst):
    """Zoals het platform een invulantwoord vergelijkt: zonder hoofdletters,
    zonder leestekens en zonder accenten."""
    tekst = tekst.lower()
    vervang = str.maketrans("àáâäãåèéêëìíîïòóôöõùúûüçñ", "aaaaaaeeeeiiiiooooouuuucn")
    tekst = tekst.translate(vervang)
    return re.sub(r"[^a-z0-9]+", " ", tekst).strip()


def controleer(hoofdstukken):
    fouten = []
    gezien = {}
    for h in hoofdstukken:
        titel = h["titel"]
        tekst = alinea_per_regel(h["tekst"])
        kaal = normaliseer(zonder_sterretjes(tekst))

        gemarkeerd = {w.lower() for w in re.findall(r"\*([^*\n]+)\*", tekst)}
        uit_lijst = {w.lower() for w, _ in h["woorden"]}
        for w in sorted(gemarkeerd - uit_lijst):
            fouten.append(f"{titel}: *{w}* staat in de tekst maar niet in de woordenlijst")
        for w in sorted(uit_lijst - gemarkeerd):
            fouten.append(f"{titel}: '{w}' staat in de woordenlijst maar niet tussen sterretjes")
        for w, uitleg in h["woorden"]:
            if len(uitleg.split()) < 3:
                fouten.append(f"{titel}: de uitleg bij '{w}' is te kort")

        mk = [v for v in h["vragen"] if v["type"] == "meerkeuze"]
        langst = 0
        for v in mk:
            antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
            lengtes = [len(o) for o in (v.get("opties") or [""])]
            anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
            if anders and min(lengtes[i] for i in antw) > max(anders):
                langst += 1
        if mk and langst > 0.4 * len(mk):
            fouten.append(
                f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
                f"antwoord de langste optie. Maak de andere opties langer."
            )

        wn = [v["antwoord"] for v in h["vragen"] if v["type"] == "waarofniet"]
        if wn and not (0.35 <= sum(1 for a in wn if a) / len(wn) <= 0.65):
            fouten.append(
                f"{titel}: {sum(1 for a in wn if a)} van de {len(wn)} waar/niet-waar-vragen "
                f"is waar. Dat is te scheef om niet te kunnen gokken."
            )

        if len(h["vragen"]) < 20:
            fouten.append(f"{titel}: maar {len(h['vragen'])} vragen")

        for v in h["vragen"]:
            s = sleutel(v["vraag"])
            if s in gezien:
                fouten.append(f"twee keer dezelfde vraag: {v['vraag']}")
            gezien[s] = titel

            if not v.get("uitleg"):
                fouten.append(f"{titel}: geen uitleg bij: {v['vraag']}")

            if v["type"] == "meerkeuze":
                opties = v.get("opties") or []
                if len(opties) < 3:
                    fouten.append(f"{titel}: te weinig opties bij: {v['vraag']}")
                if len(set(opties)) != len(opties):
                    fouten.append(f"{titel}: twee keer dezelfde optie bij: {v['vraag']}")
                antw = v["antwoord"]
                nummers = antw if isinstance(antw, list) else [antw]
                if isinstance(antw, list) and len(antw) < 2:
                    fouten.append(f"{titel}: een lijstje met één antwoord bij: {v['vraag']}")
                for n in nummers:
                    if not isinstance(n, int) or not 0 <= n < len(opties):
                        fouten.append(f"{titel}: antwoord {n} bestaat niet bij: {v['vraag']}")
            elif v["type"] == "waarofniet":
                if not isinstance(v["antwoord"], bool):
                    fouten.append(f"{titel}: waarofniet zonder true/false: {v['vraag']}")
            elif v["type"] == "invultekst":
                antw = str(v["antwoord"])
                if not v.get("vrij") and normaliseer(antw) not in kaal:
                    fouten.append(
                        f"{titel}: het antwoord '{antw}' staat niet letterlijk in de tekst"
                    )
            else:
                fouten.append(f"{titel}: onbekend vraagtype {v['type']}")
    return fouten


def main():
    welk = sys.argv[1] if len(sys.argv) > 1 else "start"
    if welk == "spark":
        sys.path.insert(0, str(HIER.parent.parent / "spark" / "bron"))
        import begrijpend_lezen_spark as bron  # noqa: E402
        doel = HIER.parent.parent / "spark" / "nederlands-begrijpend-lezen.json"
        niveau = "spark"
    else:
        sys.path.insert(0, str(HIER))
        import begrijpend_lezen as bron  # noqa: E402
        doel = HIER.parent / "nederlands-begrijpend-lezen.json"
        niveau = "start"

    fouten = controleer(bron.HOOFDSTUKKEN)
    if fouten:
        print(f"{len(fouten)} probleem(en):")
        for f in fouten:
            print(" -", f)
        sys.exit(1)

    uit = {"hoofdstukken": []}
    for h in bron.HOOFDSTUKKEN:
        uit["hoofdstukken"].append({
            "titel": h["titel"],
            "niveau": niveau,
            "leestekst": alinea_per_regel(h["tekst"]),
            "woordenlijst": [{"woord": w, "uitleg": u} for w, u in h["woorden"]],
            "vragen": [
                {k: v for k, v in vraag.items() if k != "vrij"}
                for vraag in h["vragen"]
            ],
        })

    doel.write_text(json.dumps(uit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    aantal = sum(len(h["vragen"]) for h in uit["hoofdstukken"])
    print(f"{doel.name}: {len(uit['hoofdstukken'])} hoofdstukken, {aantal} vragen")


if __name__ == "__main__":
    main()

"""Zoekt vragen die het antwoord van een andere vraag in hetzelfde hoofdstuk verklappen.

Voor elke vraag halen we de kern van het juiste antwoord op (jaartallen, namen,
het juiste woord) en kijken of die in de tekst of de uitleg van een andere vraag
staat, terwijl de foute keuzes van de vraag zelf ze niet bevatten.
Gebruik: python3 pittig/bron/verklappers.py pittig/beyond-geschiedenis-pittig.json [hoofdstuktitel-deel]
"""
import json, re, sys

STOP = set("""De Het Een In Op Bij Voor Na Van Met En Of Om Te Tot Dat Die Dit Deze Zo Ze Hij Zij Wie Wat Waar
Welke Waarom Hoe Klik Zet Lees Juist Fout Is Geen Kenmerk Ja Nee Er Als Ook Maar Toen Niet Eerst Daarna Elk Elke
Mag Want Omdat Door Uit Aan Over Onder Tussen Sinds Tegen Zonder Alle Veel Twee Drie Vier Vijf""".split())

def plat(vragen):
    for v in vragen:
        if "casus" in v:
            for w in v["vragen"]:
                yield w, v["casus"]
        else:
            yield v, ""

def kern(v):
    """(juiste stukken, foute stukken) als tekst."""
    t = v.get("type")
    goed, fout = [], []
    if t == "meerkeuze":
        a = v["antwoord"]; a = a if isinstance(a, list) else [a]
        for i, o in enumerate(v["opties"]):
            (goed if i in a else fout).append(o)
    elif t == "invultekst":
        a = v["antwoord"]; goed += a if isinstance(a, list) else [a]
    elif t == "keuzelijst":
        for grp in re.findall(r"\[\[(.*?)\]\]", v["vraag"]):
            for o in grp.split("|"):
                (goed if o.startswith("*") else fout).append(o.lstrip("*"))
    elif t == "sleepzin":
        goed += re.findall(r"\[\[(.*?)\]\]", v["vraag"]); fout += v.get("extra", [])
    elif t == "koppelen":
        goed += [p[1] for p in v["paren"]]; fout += v.get("extra", [])
    return goed, fout

def tokens(s):
    jaren = set(re.findall(r"\b1[0-9]{3}\b|\b20[0-9]{2}\b", s))
    namen = {w for w in re.findall(r"(?<![.!?:]\s)(?<!^)\b[A-ZÉ][\wëéèïöü'-]{2,}", s) if w not in STOP}
    woorden = {w.lower() for w in re.findall(r"\b[\wëéèïöü-]{7,}\b", s)}
    return jaren | namen, woorden

def zichtbaar(v, casus):
    stuk = [v.get("vraag", ""), casus]
    if v.get("type") == "meerkeuze":
        stuk += v["opties"]
    if v.get("type") in ("tabel",):
        stuk += [r if isinstance(r, str) else r[0] for r in v.get("rijen", [])]
    if v.get("type") in ("sorteren",):
        stuk += [i[0] for i in v.get("items", [])]
    if v.get("type") in ("volgorde",):
        stuk += v.get("opties", [])
    if v.get("type") == "koppelen":
        stuk += [p[0] for p in v["paren"]]
    vraag = re.sub(r"\[\[(.*?)\]\]", " ", " ".join(stuk))
    return vraag, v.get("uitleg", "") or ""

def main():
    d = json.load(open(sys.argv[1]))
    filt = sys.argv[2] if len(sys.argv) > 2 else ""
    totaal = 0
    for h in d["hoofdstukken"]:
        if filt not in h["titel"]:
            continue
        lijst = list(plat(h["vragen"]))
        for i, (v, c) in enumerate(lijst):
            goed, fout = kern(v)
            if not goed:
                continue
            gs, gw = tokens(" ".join(goed))
            fs, fw = tokens(" ".join(fout) + " " + v.get("vraag", "") + " " + c)
            sterk = gs - fs
            if v["type"] == "meerkeuze":
                # bij meerkeuze tellen enkel jaartallen; namen in de juiste optie zijn te vaak gewone woorden
                sterk = {x for x in sterk if x.isdigit()}
            for j, (w, c2) in enumerate(lijst):
                if j == i:
                    continue
                vraag, uitleg = zichtbaar(w, c2 if c2 != c else "")
                for waar, tekst in (("vraag", vraag), ("uitleg", uitleg)):
                    hits = [x for x in sterk if re.search(r"\b" + re.escape(x) + r"\b", tekst)]
                    vol = [g for g in goed if len(g) > 3 and g.lower() not in " ".join(fout).lower()
                           and re.search(r"\b" + re.escape(g.lower()) + r"\b", tekst.lower())]
                    if hits or vol:
                        totaal += 1
                        print(f"[{h['titel']}] v{i+1} ({v['type']}) ← {waar} v{j+1}: {sorted(set(hits)|set(vol))}")
                        print(f"     V: {v.get('vraag','')[:110]}")
                        print(f"     {waar}: {tekst[:160]}")
    print(totaal, "mogelijke verklappers")

if __name__ == "__main__":
    main()

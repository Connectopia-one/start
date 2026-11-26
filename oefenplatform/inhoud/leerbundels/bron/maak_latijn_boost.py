# -*- coding: utf-8 -*-
"""Leerbundels, oefenbundels en uitlegbladen bij Latijn 🚀 Boost doorstroom.

Gebaseerd op de vakfiche `2027_Latijn_2DO`. Elk hoofdstuk van het vak is één
opgelegde tekst (of een lectuurtekst, of de oefening op een ongeziene tekst).
De bundels lezen de hoofdstukken rechtstreeks uit
`../../boost-doorstroom/bron/latijn/`, zodat tekst, woorden en uitleg nooit
uiteenlopen met wat er online staat.

- Leerbundel: waar gaat het over, de tekst zelf (zonder sterretjes), de
  woorden bij de tekst, en de uitleg bij de vragen van het hoofdstuk, met
  dezelfde woorden (zo dekt de bundel elke vraag).
- Oefenbundel: andere oefeningen dan online. Woorden opzoeken, zinnen uit de
  tekst vertalen (het antwoord komt uit de vertaling in de uitleg), juist of
  fout, en een schrijfopdracht.
- Uitlegblad: per reeks de aanpak, per oefening het waarom.
"""
import sys, pathlib, re, importlib, html as _html
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel

LAT = HIER.parent.parent / "boost-doorstroom" / "bron" / "latijn"
sys.path.insert(0, str(LAT))

VAK = "Latijn"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel
W = "200px"

BUNDELS = {}
OEFENBUNDELS = {}
UITLEGBLADEN = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Leg de tekst uit je leerbundel naast je. Op het examen mag je ook een woordenboek gebruiken.",
    "Vertaal eerst het werkwoord, zoek dan het onderwerp en daarna de rest van de zin.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def e(s):
    return _html.escape(s, quote=False)


def papier(t):
    """De inleiding is geschreven voor het scherm (tik op een woord); op papier staan de woorden in de tabel."""
    t = re.sub(r"^Waar gaat het over\? ", "", t)
    t = t.replace("Lees eerst de tekst, tik op een onderstreept woord voor de betekenis.", "Lees eerst de tekst. De moeilijke woorden staan in de tabel na de tekst.")
    t = t.replace("Tik op een onderstreept woord voor de betekenis.", "De moeilijke woorden staan in de tabel na de tekst.")
    t = t.replace("hier helpen de onderstreepte woorden je op weg", "hier helpt de tabel met woorden je op weg")
    return t


def kale_vraag(v):
    """Een keuzevraag met [[*juist|fout]] wordt een zin met het juiste antwoord ingevuld."""
    return re.sub(r"\[\[([^\]]*)\]\]", lambda m: next(x[1:] for x in m.group(1).split("|") if x.startswith("*")), v)


def vertaalparen(M, tekst):
    """Stukjes 'Latijn: vertaling.' uit de uitleg, waarvan het Latijn echt in de tekst staat."""
    plat = re.sub(r"[^a-z ]", "", tekst.lower())
    paren, gezien = [], set()
    for v in M.VRAGEN:
        for m in re.finditer(r"(?:^|(?<=\. ))([A-Z][^:]{10,170}?): ([^.]{6,220}\.)", v.get("uitleg", "")):
            lat, nl = m.group(1).strip(), m.group(2).strip()
            sleutel = re.sub(r"[^a-z ]", "", lat.lower())
            woorden = sleutel.split()
            if len(woorden) < 3 or " ".join(woorden[:3]) not in plat or sleutel in gezien:
                continue
            gezien.add(sleutel)
            paren.append((lat, nl))
    return paren


def uitlegpunten(M):
    punten = []
    for v in M.VRAGEN:
        if v["type"] == "open":
            continue
        u = v.get("uitleg", "").strip()
        if u and u not in punten:
            punten.append(u)
    return punten


mods = sorted((p.stem for p in LAT.glob("[a-z][0-9]*.py")), key=lambda m: (int(m[1:3]), m))
for m in mods:
    M = importlib.import_module(m)
    latijn = not m.startswith("l")
    sl = slug(M.TITEL) + "-boost-doorstroom"
    tekst = "\n\n".join(M.ALINEAS)
    alineas = []
    for a in M.ALINEAS:
        if len(a) < 60 and not a.startswith("("):
            alineas.append(("p", f"<strong>{e(a)}</strong>"))
        else:
            alineas.append(("p", (f'<span lang="la"><em>{e(a)}</em></span>' if latijn else e(a))))
    woorden = [[f"<em>{e(w['woord'])}</em>" if latijn else e(w["woord"]), e(w["uitleg"])] for w in M.WOORDEN]
    punten = uitlegpunten(M)
    BUNDELS[sl] = dict(
        vak=VAK, niveau=BOOST, titel=M.TITEL,
        # Een lange tekst past niet op één blad: laat die sectie gewoon doorlopen
        # in plaats van ze naar een nieuw blad te duwen (dan blijft blad 1 leeg).
        extra_css="section { break-inside: auto; } section p, section tr { break-inside: avoid; }",
        onder=("De Latijnse tekst met de woorden erbij, en de uitleg bij alles wat je erover moet kunnen."
               if latijn else "De tekst bij de lectuuropdracht, met de woorden erbij en de uitleg bij de vragen."),
        secties=[
            dict(kop="De tekst", blokken=[("p", e(papier(M.INLEIDING)))] + alineas
                 + [("kader", "<p><strong>Bron.</strong> " + e(M.BRON) + "</p>")]),
            dict(kop="Woorden bij de tekst", blokken=[("p", tabel(["Woord", "Betekenis"], woorden))]),
            dict(kop="Wat moet je over deze tekst weten?", blokken=[
                ("p", "<ul>" + "".join(f"<li>{e(p)}</li>" for p in punten) + "</ul>")]),
        ],
        onthoud=[e(p.split(". ")[0].rstrip(".") + ".") for p in punten if len(p) > 30][:5],
    )

    # ── oefenbundel
    reeksen, uitleg = [], []
    wl = M.WOORDEN[:12]
    if wl:
        rijen = [wl[i:i + 4] for i in range(0, len(wl), 4)]
        reeksen.append(dict(kop="Woorden", opdracht="Wat betekent het woord in de tekst?",
                            oefeningen=[("rij", [(f"<em>{e(w['woord'])}</em>" if latijn else e(w["woord"]), e(w["uitleg"])) for w in r], None, W) for r in rijen]))
        uitleg.append(dict(aanpak="Zoek het woord op in de tekst en lees de zin errond. Een woord krijgt zijn betekenis pas in zijn zin.",
                           waarom=[None] * len(rijen)))
    if latijn:
        paren = vertaalparen(M, tekst)[:6]
        if paren:
            reeksen.append(dict(kop="Vertalen", opdracht="Vertaal in goed Nederlands.",
                                oefeningen=[("open", f"<em>{e(l)}</em>", e(n), 2) for l, n in paren]))
            uitleg.append(dict(aanpak="Zoek eerst de persoonsvorm, dan het onderwerp. Kijk naar de uitgangen: die zeggen welke rol een woord speelt in de zin.",
                               waarom=[None] * len(paren)))
    waar = []
    for v in M.VRAGEN:
        if v["type"] == "tabel":
            for st, a in zip(v["rijen"], v["antwoord"]):
                waar.append((st, a, v.get("uitleg", "")))
    if waar:
        waar = waar[:8]
        reeksen.append(dict(kop="Juist of fout?", opdracht="Klopt dit volgens de tekst?",
                            oefeningen=[("waar", e(s), a) for s, a, _ in waar]))
        uitleg.append(dict(aanpak="Zoek de plaats in de tekst waar het over gaat. Klopt één stukje van de zin niet, dan is heel de zin fout.",
                           waarom=[None if a else e(u) for s, a, u in waar]))
    keuzes = [v for v in M.VRAGEN if v["type"] == "keuzelijst"][:4]
    if keuzes:
        reeksen.append(dict(kop="Grammatica en stijl", opdracht="Leg uit in je eigen woorden.",
                            oefeningen=[("open", "Wat zie je in deze zin, en hoe vertaal je ze? " + e(re.split(r"\[\[", v["vraag"])[0].strip().rstrip(":")), e(v["uitleg"]), 2) for v in keuzes]))
        uitleg.append(dict(aanpak="Benoem eerst de vorm (naamval, tijd, wijs), dan pas de vertaling.",
                           waarom=[e(kale_vraag(v["vraag"])) for v in keuzes]))
    opens = [v for v in M.VRAGEN if v["type"] == "open"]
    if opens:
        v = opens[0]
        reeksen.append(dict(kop="Schrijven", opdracht="Antwoord in een paar zinnen.",
                            oefeningen=[("open", e(v["vraag"]), e(v["antwoord"]), 5)]))
        uitleg.append(dict(aanpak=e(v.get("uitleg", "Gebruik de tekst om je antwoord te staven.")), waarom=[None]))
    OEFENBUNDELS["oefenbundel-" + sl] = dict(
        vak=VAK, niveau=BOOST, titel=M.TITEL,
        onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=reeksen)
    UITLEGBLADEN["oefenbundel-" + sl] = dict(reeksen=uitleg)

if __name__ == "__main__":
    for k, b in BUNDELS.items():
        print(k, sum(len(r["oefeningen"]) for r in OEFENBUNDELS["oefenbundel-" + k]["reeksen"]))

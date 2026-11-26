# -*- coding: utf-8 -*-
"""Gedeelde stijl en maakfunctie voor de Ready-bundels (3de en 4de leerjaar).
Ready is voor kinderen van 8 en 9: grotere letters, hogere schrijflijnen en
grotere vakjes, want de fijne motoriek is nog volop in ontwikkeling (Kim, 26/11)."""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel, oefenbundel

GROOT = ("body{font-size:13.5pt;line-height:1.7}table{font-size:12pt}figcaption{font-size:11pt}"
         ".oef .vraagtekst,.rij .cel{font-size:13pt}.hoe li,.opdracht{font-size:12pt}"
         ".lijn{height:54px}.vakje{height:38px;min-width:120px !important}.rij .cel{line-height:2.8}"
         ".oef{break-inside:avoid}")
# Ruitjes van 1 cm in tekenvakken: om onder elkaar te cijferen en om figuren te tekenen.
RUITJES = (".tekenvak{background-image:linear-gradient(#d9d4c7 1px,transparent 1px),"
           "linear-gradient(90deg,#d9d4c7 1px,transparent 1px);background-size:10mm 10mm}")
READY = "🎒 Ready — 3de en 4de leerjaar"
DARK, ORANJE, PAARS, GROEN = "#2f4a22", "#c4622d", "#7a5aa6", "#6f9a4a"
tabel = bundel.tabel
_basis = (bundel.CSS, oefenbundel.OEFEN_CSS)


def svg(b, h, inhoud, breed=None):
    return f'<svg viewBox="0 0 {b} {h}" width="{breed or b}" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">{inhoud}</svg>'


# Grotere tekeningen in de oefenbundel (kompasroos, stroomkring, plant): voor de
# wereldoriëntatie-bundels van Ready, waar de kinderen in de tekening schrijven.
GROTE_FIGUREN = ".figcel .tekening{height:auto;min-height:96px}.figcel svg{max-height:230px;max-width:320px}"


def maak(naam, vakmap, leer, oefen, ruitjes=False, grote_figuren=False):
    import math  # noqa: F401
    bundel.CSS = _basis[0] + GROOT
    oefenbundel.OEFEN_CSS = _basis[1] + GROOT + (RUITJES if ruitjes else "") + (GROTE_FIGUREN if grote_figuren else "")
    for maker, b, basis, n in ((bundel, leer, HIER.parent, naam),
                               (oefenbundel, oefen, HIER.parent.parent / "oefenbundels", "oefenbundel-" + naam)):
        tijdelijk = "ready-" + n
        maker.schrijf(b, tijdelijk)
        subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True, capture_output=True)
        doel = basis / vakmap / f"{n}.pdf"
        doel.write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
        print("  ", doel.relative_to(HIER.parent.parent))


# ------------------------------------------------------------------ prenten in de bundels
# Kim, 26/11: "de bundels zou ik ook allemaal direct met prenten doen". De prenten
# zijn dezelfde als bij de prentvragen op het scherm (vraag 21 tot 24 van elk deel,
# ../../ready/bron/prent.py). De leerbundel krijgt een stukje "Kijk en leer", de
# oefenbundel een reeks "Kijk goed naar de prent" met de prentvragen op papier.
import base64, json, random
PUBLIEK = HIER.parent.parent.parent / "public"
READYJSON = HIER.parent.parent / "ready"


def _bronnen():
    f = PUBLIEK / "examenvormen" / "ready" / "BRONNEN.txt"
    uit = {}
    for lijn in f.read_text(encoding="utf-8").splitlines()[1:] if f.exists() else []:
        if ": " in lijn:
            k, v = lijn.split(": ", 1); uit[k] = v
    return uit


def prent_html(pad, hoog="52mm"):
    p = PUBLIEK / pad.lstrip("/")
    mime = "image/svg+xml" if p.suffix == ".svg" else "image/webp"
    img = (f'<img src="data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}" '
           f'style="max-height:{hoog};max-width:100%;display:block;margin:4px auto" alt="">')
    bron = _bronnen().get(p.name)
    if bron:
        kort = bron.split(", http")[0]
        img += f'<span style="display:block;font-size:8pt;color:#6b7260;text-align:center">Prent: {kort} (Wikimedia Commons)</span>' if "commons" in bron else \
               f'<span style="display:block;font-size:8pt;color:#6b7260;text-align:center">Kaart: Natural Earth (publiek domein)</span>'
    return img


def _prentvragen(module):
    data = json.loads((READYJSON / (module.replace("_", "-") + ".json")).read_text(encoding="utf-8"))
    return [[v for v in h["vragen"] if v.get("afbeelding_pad")] for h in data["hoofdstukken"]]


def met_prenten(leer, oefen, module):
    """Voegt de prenten van een Ready-hoofdstuk toe aan de leer- en de oefenbundel."""
    delen = _prentvragen(module)
    if not any(delen):
        return
    # Leerbundel: per deel de eerste twee prenten, met de uitleg eronder.
    cellen = []
    for vragen in delen:
        gezien = set()
        for v in vragen:
            if v["afbeelding_pad"] in gezien or len(gezien) == 2: continue
            gezien.add(v["afbeelding_pad"])
            cellen.append(f'<div style="flex:1 1 45%;border:1px solid #e4ded0;border-radius:12px;padding:8px;break-inside:avoid">'
                          f'{prent_html(v["afbeelding_pad"], "48mm")}<div style="margin-top:6px">{v["uitleg"]}</div></div>')
    leer["secties"].append(dict(kop="Kijk en leer", blokken=[
        ("p", '<div style="display:flex;flex-wrap:wrap;gap:10px">' + "".join(cellen) + "</div>")]))
    # Oefenbundel: alle prentvragen, de prent telkens boven de vraag.
    oef = []
    for vragen in delen:
        for v in vragen:
            # De prent hoort bij de vraag zelf, zodat ze nooit op een andere bladzijde belandt.
            vraag = f'<div>{prent_html(v["afbeelding_pad"], "60mm")}</div>{v["vraag"]}'
            if v["type"] == "waarofniet":
                oef.append(("waar", vraag, v["antwoord"]))
            elif v["type"] == "meerkeuze":
                opties = list(v["opties"]); juist = opties[v["antwoord"]]
                random.Random(v["vraag"]).shuffle(opties)
                oef.append(("kies", vraag, opties, opties.index(juist)))
            else:
                a = v["antwoord"]
                oef.append(("kort", vraag, a[0] if isinstance(a, list) else a, "150px"))
    oefen["reeksen"].append(dict(kop="Kijk goed naar de prent", oefeningen=oef))

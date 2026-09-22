# -*- coding: utf-8 -*-
"""
Bouwt van een bundel-beschrijving een html-bestand in de huisstijl.

Een bundel is een gewone dict:

    BUNDEL = dict(
        vak="Wiskunde",
        titel="Bewerkingen",
        onder="Een zin die zegt waarover het gaat.",
        secties=[
            dict(kop="Optellen", blokken=[
                ("p", "gewone tekst, html mag"),
                ("fig", "<svg .../>", "onderschrift"),
                ("weetje", "tekst in het amberkader"),
                ("kader", "<p>vrije html in een wit kader</p>"),
            ]),
        ],
        onthoud=["korte zin", "nog een"],
    )

Daarna:  schrijf(BUNDEL, "bewerkingen")
"""
import pathlib, html as _html

HIER = pathlib.Path(__file__).parent
CSS = HIER.joinpath("stijl.css").read_text(encoding="utf-8")
NIVEAU = "🌱 Start — 5de en 6de leerjaar"

def _blok(b):
    soort = b[0]
    if soort == "p":
        return f"<p>{b[1]}</p>"
    if soort == "fig":
        onderschrift = f'<figcaption>{b[2]}</figcaption>' if len(b) > 2 and b[2] else ""
        return f"<figure>{b[1]}{onderschrift}</figure>"
    if soort == "weetje":
        return f'<div class="weetje"><b>💡 Weetje.</b> {b[1]}</div>'
    if soort == "kader":
        return f'<div class="kader">{b[1]}</div>'
    raise ValueError("onbekend blok: " + soort)

def render(bundel):
    secties = []
    for i, s in enumerate(bundel["secties"], 1):
        inhoud = "".join(_blok(b) for b in s["blokken"])
        secties.append(
            f'<section><h2><span class="nr">{i}</span> {s["kop"]}</h2>{inhoud}</section>'
        )

    onthoud = ""
    if bundel.get("onthoud"):
        punten = "".join(f"<li>{p}</li>" for p in bundel["onthoud"])
        onthoud = f'<div class="onthoud"><h2>Onthoud dit</h2><ul>{punten}</ul></div>'

    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Leerbundel — {_html.escape(bundel["titel"])}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<div class="kop">
  <div class="vak">{bundel["vak"]} · {bundel.get("niveau", NIVEAU)}</div>
  <h1>{bundel["titel"]}</h1>
  <p class="onder">{bundel["onder"]}</p>
</div>

{"".join(secties)}
{onthoud}

<div class="voet">
  <span>Connectopia vzw · oefenplatform.connectopia.one</span>
  <span>Leerbundel — {bundel["vak"]}, {bundel["titel"]}</span>
</div>

</body>
</html>
"""

def schrijf(bundel, bestandsnaam):
    pad = HIER / (bestandsnaam + ".html")
    pad.write_text(render(bundel), encoding="utf-8")
    print("geschreven:", pad.name)
    return pad


def tabel(kop, rijen, breed=None):
    """Een eenvoudige tabel in de huisstijl, als html."""
    th = "".join(
        f'<th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 9px;'
        f'color:#234539;font-weight:600;text-align:left;">{k}</th>' for k in kop)
    tr = "".join(
        "<tr>" + "".join(
            f'<td style="border:1px solid #e4ded0;padding:6px 9px;color:#23291f;">{c}</td>' for c in rij
        ) + "</tr>" for rij in rijen)
    return (f'<table style="width:{breed or "100%"};border-collapse:collapse;'
            f"font-family:'IBM Plex Sans',sans-serif;font-size:10.5pt;text-align:left;\">"
            f"<tr>{th}</tr>{tr}</table>")


def foto(pad, breedte="100%", bron=None, hoogte=None):
    """
    Zet een echte foto in een bundel. Het bestand gaat als base64 mee in de
    html, zodat de pdf later nergens meer naar hoeft te zoeken.

    pad    — het beeldbestand (jpg of png)
    bron   — de bronvermelding, bijvoorbeeld "Foto: naam, CC BY-SA 4.0".
             Laat die nooit weg bij beeld van iemand anders.
    """
    import base64, mimetypes
    p = pathlib.Path(pad)
    soort = mimetypes.guess_type(p.name)[0] or "image/jpeg"
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    stijl = f"width:{breedte};max-width:100%;border-radius:10px;border:1px solid #e4ded0;"
    if hoogte:
        stijl += f"height:{hoogte};object-fit:cover;"
    img = f'<img src="data:{soort};base64,{data}" style="{stijl}" alt="">'
    if bron:
        img += (f'<span style="display:block;margin-top:4px;font-size:8pt;color:#6b7260;'
                f'text-align:right;">{bron}</span>')
    return img

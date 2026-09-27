# -*- coding: utf-8 -*-
"""
Bouwt van een oefenbundel-beschrijving een html-bestand in dezelfde huisstijl
als de leerbundels.

Het verschil met bundel.py: een leerbundel legt uit, een oefenbundel laat
oefenen. Er staat dus plaats om te schrijven, de oefeningen zijn doorlopend
genummerd, en achteraan staat een antwoordblad op een eigen blad, zodat je het
eraf kan scheuren voor je de bundel aan een kind geeft.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Wie de bundel invult en daarna online oefent, moet twee keer denken en
niet twee keer hetzelfde antwoord opschrijven.

Een oefenbundel is een gewone dict:

    OEFENBUNDEL = dict(
        vak="Wiskunde",
        titel="Rekenen en breuken",
        onder="Een zin die zegt waarover het gaat.",
        hoe=["regel in het kadertje bovenaan", "nog een regel"],
        reeksen=[
            dict(kop="Breuken lezen", opdracht="Wat je moet doen.", oefeningen=[
                ("kort", "348 + 156 =", "504"),
                ("rij", [("7 x 8", "56"), ("9 x 6", "54")]),
                ("fig", [(svg.breukfiguur("strook", 3, 4), "3/4")], "onderschrift"),
                ("open", "Een vraag in woorden.", "het antwoord", 2),
                ("kies", "Welke is het grootst?", ["2/3", "3/5"], 0),
                ("waar", "Een stelling.", True),
                ("tabel", ["breuk", "procent"], [["1/2", None]], "1/2 = 50%"),
                ("tekst", "<p>Een zin die niet genummerd wordt.</p>"),
            ]),
        ],
    )

Daarna:  schrijf(OEFENBUNDEL, "rekenen-en-breuken-oefeningen")
"""
import pathlib, html as _html

HIER = pathlib.Path(__file__).parent
CSS = HIER.joinpath("stijl.css").read_text(encoding="utf-8")
OEFEN_CSS = HIER.joinpath("oefen.css").read_text(encoding="utf-8")
NIVEAU = "🌱 Start — 5de en 6de leerjaar"

LETTERS = "abcdefghijklmnop"


def _vak(breed="70px"):
    """Het lege vakje waarin het kind zijn antwoord schrijft."""
    return f'<span class="vakje" style="min-width:{breed}"></span>'


def _lijnen(aantal):
    return "".join('<div class="lijn"></div>' for _ in range(aantal))


def _oefening(o, nr):
    """Geeft (html, antwoord-html) terug. nr is None bij een blok zonder nummer."""
    soort = o[0]
    bol = f'<span class="nr">{nr}</span>' if nr else ""

    if soort == "tekst":
        return f'<div class="tussen">{o[1]}</div>', None

    if soort == "kort":
        body = f'<span class="vraagtekst">{o[1]}</span> {_vak()}'
        return f'<div class="oef">{bol}<div class="body">{body}</div></div>', _html.escape(o[2])

    if soort == "rij":
        cellen = "".join(
            f'<div class="cel"><span class="letter">{LETTERS[i]})</span> '
            f'<span class="som">{som}</span> {_vak("58px")}</div>'
            for i, (som, _) in enumerate(o[1])
        )
        antw = " · ".join(f"{LETTERS[i]}) {_html.escape(a)}" for i, (_, a) in enumerate(o[1]))
        return f'<div class="oef">{bol}<div class="body"><div class="rij">{cellen}</div></div></div>', antw

    if soort == "fig":
        onderschrift = o[2] if len(o) > 2 and o[2] else ""
        cellen = "".join(
            f'<div class="figcel"><span class="letter">{LETTERS[i]})</span>'
            f'<div class="tekening">{tek}</div>{_vak("62px")}</div>'
            for i, (tek, _) in enumerate(o[1])
        )
        # De opdracht staat boven de tekeningen: een kind dat eerst de figuur
        # ziet, begint te schrijven voor het gelezen heeft wat er gevraagd is.
        rand = f'<div class="figboven">{onderschrift}</div>' if onderschrift else ""
        antw = " · ".join(f"{LETTERS[i]}) {_html.escape(a)}" for i, (_, a) in enumerate(o[1]))
        return f'<div class="oef">{bol}<div class="body">{rand}<div class="figrij">{cellen}</div></div></div>', antw

    if soort == "kleur":
        # Een kleuropdracht krijgt geen antwoordvakje: het antwoord is de
        # tekening zelf. De opdracht staat boven de figuur, want anders kleurt
        # een kind eerst en leest het daarna.
        cellen = "".join(
            f'<div class="figcel"><span class="letter">{LETTERS[i]})</span> '
            f'<span class="kleuropdracht">{opdracht}</span>'
            f'<div class="tekening">{tek}</div></div>'
            for i, (tek, opdracht, _) in enumerate(o[1])
        )
        antw = " · ".join(f"{LETTERS[i]}) {_html.escape(a)}" for i, (_, _, a) in enumerate(o[1]))
        return f'<div class="oef">{bol}<div class="body"><div class="figrij">{cellen}</div></div></div>', antw

    if soort == "open":
        regels = o[3] if len(o) > 3 else 2
        body = f'<span class="vraagtekst">{o[1]}</span>{_lijnen(regels)}'
        return f'<div class="oef">{bol}<div class="body">{body}</div></div>', _html.escape(o[2])

    if soort == "kies":
        keuzes = "".join(
            f'<span class="keuze"><span class="bolletje"></span>{_html.escape(k)}</span>' for k in o[2]
        )
        body = f'<span class="vraagtekst">{o[1]}</span><div class="keuzes">{keuzes}</div>'
        return f'<div class="oef">{bol}<div class="body">{body}</div></div>', _html.escape(o[2][o[3]])

    if soort == "waar":
        keuzes = ('<span class="keuze"><span class="bolletje"></span>waar</span>'
                  '<span class="keuze"><span class="bolletje"></span>niet waar</span>')
        body = f'<span class="vraagtekst">{o[1]}</span><div class="keuzes">{keuzes}</div>'
        return f'<div class="oef">{bol}<div class="body">{body}</div></div>', "waar" if o[2] else "niet waar"

    if soort == "tabel":
        koppen, rijen = o[1], o[2]
        leeg = _vak("56px")
        th = "".join(f"<th>{k}</th>" for k in koppen)
        tr = "".join(
            "<tr>" + "".join(f"<td>{leeg if c is None else c}</td>" for c in rij) + "</tr>"
            for rij in rijen
        )
        tabel = f'<table class="invul"><tr>{th}</tr>{tr}</table>'
        return f'<div class="oef">{bol}<div class="body">{tabel}</div></div>', o[3]

    raise ValueError("onbekende oefening: " + soort)


def render(bundel):
    nr = 0
    reeksen_html = []
    antwoordblokken = []

    for i, r in enumerate(bundel["reeksen"], 1):
        regels = []
        antwoorden = []
        for o in r["oefeningen"]:
            if o[0] == "tekst":
                html, _ = _oefening(o, None)
                regels.append(html)
                continue
            nr += 1
            html, antw = _oefening(o, nr)
            regels.append(html)
            antwoorden.append(f'<li><span class="anr">{nr}</span> {antw}</li>')

        opdracht = f'<p class="opdracht">{r["opdracht"]}</p>' if r.get("opdracht") else ""
        reeksen_html.append(
            f'<section class="reeks"><h2><span class="nr">{i}</span> {r["kop"]}</h2>'
            f'{opdracht}{"".join(regels)}</section>'
        )
        antwoordblokken.append(
            f'<div class="antwreeks"><h3>{i}. {r["kop"]}</h3><ul>{"".join(antwoorden)}</ul></div>'
        )

    # {aantal} in de ondertitel wordt het werkelijke aantal oefeningen.
    onder = bundel["onder"].replace("{aantal}", str(nr))

    hoe = ""
    if bundel.get("hoe"):
        punten = "".join(f"<li>{p}</li>" for p in bundel["hoe"])
        hoe = f'<div class="hoe"><ul>{punten}</ul></div>'

    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Oefenbundel — {_html.escape(bundel["titel"])}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}{OEFEN_CSS}</style>
</head>
<body>

<div class="kop">
  <div class="vak">{bundel["vak"]} · {bundel.get("niveau", NIVEAU)} · Oefenbundel</div>
  <h1>{bundel["titel"]}</h1>
  <p class="onder">{onder}</p>
  <div class="naamregel">
    <span>Naam <span class="vakje" style="min-width:180px"></span></span>
    <span>Datum <span class="vakje" style="min-width:110px"></span></span>
  </div>
</div>

{hoe}
{"".join(reeksen_html)}

<div class="antwoorden">
  <div class="kop">
    <div class="vak">{bundel["vak"]} · Oefenbundel {bundel["titel"]}</div>
    <h1>Antwoorden</h1>
    <p class="onder">Dit blad is voor wie meekijkt. Scheur het eraf voor je de bundel geeft.</p>
  </div>
  <div class="antwlijst">{"".join(antwoordblokken)}</div>
  <p class="nakijken">Een fout antwoord is het interessantste stuk van de bundel: vraag hoe je
  kind eraan kwam voor je zegt wat juist is. Vaak zit de vergissing één stap eerder dan je denkt.</p>
</div>

<div class="voet">
  <span>Connectopia vzw · oefenplatform.connectopia.one</span>
  <span>Oefenbundel — {bundel["vak"]}, {bundel["titel"]}</span>
</div>

</body>
</html>
"""


def schrijf(bundel, bestandsnaam):
    pad = HIER / (bestandsnaam + ".html")
    pad.write_text(render(bundel), encoding="utf-8")
    print("geschreven:", pad.name)
    return pad

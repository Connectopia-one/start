# -*- coding: utf-8 -*-
"""Bouwt het uitlegblad dat bij een oefenbundel hoort.

Waarom dit bestaat. Febe, een tester die zich op de Examencommissie
voorbereidt, schreef op 12 oktober 2026 dat ze bij de oefeningen graag zou
weten waarom een antwoord juist is. Kim wou daarvoor geen enkele bestaande
bundel opnieuw maken: "ik zou ook de uitleg van de oefenbundel apart doen, die
kan ik gewoon extra opladen". Dus komt er per hoofdstuk een apart blad naast de
bundel, met dezelfde nummers.

Het blad bestaat uit twee soorten uitleg:

- per reeks een **aanpak**: hoe je aan zo'n oefening begint, in gewone taal;
- per oefening een **waarom**, waar het antwoord op zich niet genoeg zegt.

Bij veel oefeningen staat de uitleg al in het antwoord zelf ("16, want een
derde van 24 is 8, dus 24 min 8"). Daar hoeft niets bij; een waarom van None
laat het blad die oefening gewoon overslaan. Zo blijft het blad kort en staat
er geen uitleg die niets toevoegt.

De nummers komen **uit de oefenbundel zelf**, niet uit dit bestand opnieuw.
Anders verschuift het blad zodra er een oefening bijkomt, en wijst het kind in
zijn bundel naar nummer 14 terwijl het blad 13 bedoelt. Klopt het aantal niet,
dan stopt dit script met een melding in plaats van een blad te schrijven dat
ernaast zit.

De beschrijving staat naast de oefenbundel, in hetzelfde maak_-bestand:

    UITLEGBLADEN["oefenbundel-rekenen-en-breuken"] = dict(
        reeksen=[
            dict(aanpak="Hoe je aan deze reeks begint.",
                 waarom=[None, "Waarom bij oefening 2.", ...]),
            ...
        ],
    )

Daarna:  schrijf(UITLEGBLAD, OEFENBUNDEL, "uitlegblad-rekenen-en-breuken")
"""
import pathlib
import html as _html

from oefenbundel import LETTERS, formules_veilig

HIER = pathlib.Path(__file__).parent
CSS = HIER.joinpath("stijl.css").read_text(encoding="utf-8")
OEFEN_CSS = HIER.joinpath("oefen.css").read_text(encoding="utf-8")

EIGEN_CSS = """
/* Het uitlegblad is om te lézen, niet om in te schrijven: één kolom, en de
   uitleg mag ruim staan. */
.uitleg { margin-bottom: 16px; }
.uitleg h2 { break-after: avoid; }
.uitleg li { break-inside: avoid; }
.aanpak {
  margin: 0 0 10px;
  padding: 9px 12px;
  background: #faf7f0;
  border: 1px solid var(--border);
  border-radius: 10px;
  font-size: 10.5pt;
}
.uitleglijst { margin: 0; padding: 0; list-style: none; }
/* Het nummer staat in een eigen kolom. Met een negatieve text-indent botste
   het op een breuk: die is twee regels hoog en schuift dan over het cijfer. */
.uitleglijst li {
  display: flex;
  gap: 6px;
  font-size: 10.5pt;
  margin-bottom: 9px;
  /* Ruim, want een breuk met een echte streep is hoger dan een letter en zou
     anders tegen de regel erboven plakken. */
  line-height: 1.8;
}
.uitleglijst .anr { flex: 0 0 22px; text-indent: 0; }
.uitleglijst .inhoud { flex: 1; min-width: 0; }
.uitleglijst .vraagje { display: block; color: var(--ink-dim); }
.uitleglijst .antw { display: block; font-weight: 600; }
.uitleglijst .waarom { display: block; }
"""


def _antwoord(o):
    """Het antwoord van een oefening, precies zoals het antwoordblad het geeft."""
    soort = o[0]
    if soort == "tekst":
        return None
    if soort in ("kort", "open", "teken"):
        return o[2]
    if soort in ("rij", "fig"):
        return " · ".join(f"{LETTERS[i]}) {a}" for i, (_, a) in enumerate(o[1]))
    if soort == "kleur":
        return " · ".join(f"{LETTERS[i]}) {a}" for i, (_, _, a) in enumerate(o[1]))
    if soort == "kies":
        return o[2][o[3]]
    if soort == "waar":
        return "waar" if o[2] else "niet waar"
    if soort == "tabel":
        return o[3]
    raise ValueError("onbekende oefening: " + soort)


def _vraagje(o):
    """Een korte echo van de vraag, zodat het blad ook los te lezen is.

    Bij een rij of een figuur staat de vraag in de tekening of in de rij zelf;
    daar is de opdracht boven de reeks het enige wat we kunnen herhalen, en die
    staat al bovenaan. Dan geven we niets.
    """
    soort = o[0]
    if soort in ("kort", "open", "teken", "kies", "waar"):
        return o[1]
    if soort in ("rij", "fig"):
        return o[2] if len(o) > 2 and o[2] else ""
    return ""


def render(blad, bundel):
    """Het html van het uitlegblad. `bundel` is de oefenbundel ernaast."""
    reeksen = blad["reeksen"]
    if len(reeksen) != len(bundel["reeksen"]):
        raise SystemExit(
            f"{bundel['titel']}: het uitlegblad heeft {len(reeksen)} reeksen, "
            f"de oefenbundel {len(bundel['reeksen'])}")

    nr = 0
    blokken = []
    for i, (r, u) in enumerate(zip(bundel["reeksen"], reeksen), 1):
        genummerd = [o for o in r["oefeningen"] if o[0] != "tekst"]
        waaroms = u.get("waarom") or [None] * len(genummerd)
        if len(waaroms) != len(genummerd):
            raise SystemExit(
                f"{bundel['titel']}, reeks {i} ({r['kop']}): het uitlegblad heeft "
                f"{len(waaroms)} regels, de reeks {len(genummerd)} oefeningen")

        regels = []
        for o, waarom in zip(genummerd, waaroms):
            nr += 1
            vraag = _vraagje(o)
            kop = f'<span class="vraagje">{vraag}</span>' if vraag else ""
            tekst = f'<span class="antw">{_antwoord(o)}</span>'
            staart = f'<span class="waarom">{waarom}</span>' if waarom else ""
            regels.append(f'<li><span class="anr">{nr}</span>'
                          f'<span class="inhoud">{kop}{tekst}{staart}</span></li>')

        aanpak = f'<p class="aanpak">{u["aanpak"]}</p>' if u.get("aanpak") else ""
        blokken.append(
            f'<section class="uitleg"><h2><span class="nr">{i}</span> {r["kop"]}</h2>'
            f'{aanpak}<ul class="uitleglijst">{"".join(regels)}</ul></section>')

    titel = bundel["titel"]
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Uitleg bij de oefenbundel — {_html.escape(titel)}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<link href="katex-inline.css" rel="stylesheet">
<style>
.katex {{ white-space: nowrap; }}
.katex-display .katex {{ white-space: normal; }}
</style>
<style>{CSS}{OEFEN_CSS}{EIGEN_CSS}</style>
</head>
<body>

<div class="kop">
  <div class="vak">{bundel["vak"]} · {bundel.get("niveau", "🌱 Start — 5de en 6de leerjaar")} · Uitleg bij de oefenbundel</div>
  <h1>{titel}</h1>
  <p class="onder">Bij elke oefening het antwoord en waarom het juist is. De nummers zijn
  dezelfde als in de oefenbundel.</p>
</div>

<div class="hoe"><ul>
  <li>Dit blad is bedoeld om <strong>samen na te lezen</strong>, nadat je kind de bundel
  gemaakt heeft. Het hoort niet bij de bundel die je kind krijgt.</li>
  <li>Begin bij een fout antwoord met de vraag <strong>hoe je kind eraan kwam</strong>.
  Vaak zit de vergissing één stap eerder dan je denkt, en dan lees je hier samen die stap na.</li>
  <li>Staat er bij een oefening geen uitleg, dan zegt het antwoord zelf al genoeg.</li>
</ul></div>

{"".join(blokken)}

<div class="voet">
  <span>Connectopia vzw · oefenplatform.connectopia.one</span>
  <span>Uitleg bij de oefenbundel — {bundel["vak"]}, {titel}</span>
</div>

</body>
</html>
"""


def schrijf(blad, bundel, bestandsnaam):
    pad = HIER / (bestandsnaam + ".html")
    pad.write_text(formules_veilig(render(blad, bundel)), encoding="utf-8")
    print("geschreven:", pad.name)
    return pad

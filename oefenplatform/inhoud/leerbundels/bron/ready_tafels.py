# -*- coding: utf-8 -*-
"""Leer- en oefenbundel bij het Ready-proefhoofdstuk "Tafels en delen"
(3de en 4de leerjaar, 26 november 2026). De vragen op het scherm staan in
../../ready/bron/wiskunde_tafels.py; de oefenbundel vraagt andere dingen.

    python3 ready_tafels.py
"""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel, oefenbundel

tabel = bundel.tabel
# Ready is voor kinderen van 8 en 9: grotere letters dan in Start.
GROOT = ("body{font-size:13.5pt;line-height:1.7}table{font-size:12pt}figcaption{font-size:11pt}"
         ".oef .vraagtekst,.rij .cel{font-size:13pt}.hoe li,.opdracht{font-size:12pt}")
bundel.CSS += GROOT
oefenbundel.OEFEN_CSS += GROOT
READY = "🚀 Ready — 3de en 4de leerjaar"
NAAM = "tafels-en-delen-ready"
DARK, ORANJE, PAARS = "#2f4a22", "#c4622d", "#7a5aa6"


def _svg(b, h, inhoud):
    return f'<svg viewBox="0 0 {b} {h}" width="{b}" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">{inhoud}</svg>'


def groepjes(aantal, per, kleur=ORANJE):
    """aantal rondjes-groepjes met elk per bolletjes."""
    d, x = [], 10
    for g in range(aantal):
        w = 26 + per * 18
        d.append(f'<rect x="{x}" y="10" width="{w}" height="44" rx="18" fill="none" stroke="{DARK}" stroke-width="2"/>')
        for i in range(per):
            d.append(f'<circle cx="{x + 22 + i * 18}" cy="32" r="7" fill="{kleur}"/>')
        x += w + 14
    return _svg(x, 64, "".join(d))


def verdelen_rest():
    """14 bolletjes in groepjes van 4: 3 groepjes en 2 over."""
    d, x = [], 10
    for g in range(3):
        d.append(f'<rect x="{x}" y="10" width="98" height="44" rx="18" fill="none" stroke="{DARK}" stroke-width="2"/>')
        for i in range(4):
            d.append(f'<circle cx="{x + 22 + i * 18}" cy="32" r="7" fill="{PAARS}"/>')
        x += 112
    for i in range(2):
        d.append(f'<circle cx="{x + 14 + i * 18}" cy="32" r="7" fill="#d8d2c2" stroke="{ORANJE}" stroke-width="2"/>')
    d.append(f'<text x="{x + 6}" y="64" font-size="12" fill="{ORANJE}" font-weight="700">rest</text>')
    return _svg(x + 60, 72, "".join(d))


def tafelrooster(leeg=False):
    kop = ["×"] + [str(i) for i in range(1, 11)]
    rijen = [[f"<strong>{r}</strong>"] + ["" if leeg else str(r * k) for k in range(1, 11)] for r in range(1, 11)]
    return tabel(kop, rijen, "100%")


BUNDEL = dict(
    vak="Wiskunde", niveau=READY, titel="Tafels en delen",
    onder="Vermenigvuldigen, de tafels tot 10, delen met en zonder rest, delers, veelvouden en deelbaar door.",
    secties=[
        dict(kop="Vermenigvuldigen is groepjes maken", blokken=[
            ("fig", groepjes(4, 3), "4 groepjes van 3: 3 + 3 + 3 + 3 = 12, korter 4 × 3 = 12"),
            ("p", "Je mag de getallen <strong>wisselen</strong>: 4 × 3 is evenveel als 3 × 4. Allebei 12."),
            ("kader", "<strong>Handige trucjes</strong><br>× 1: het getal blijft hetzelfde (8 × 1 = 8).<br>"
                      "× 0: altijd 0 (0 × 9 = 0).<br>× 10: zet een nul achter het getal (7 × 10 = 70).<br>"
                      "× 2 is het dubbele. Ken je 4 × 6 = 24, dan is 8 × 6 het dubbele: 48.<br>"
                      "× 9: reken × 10 en haal er één keer het getal af (6 × 9 = 60 − 6 = 54)."),
        ]),
        dict(kop="De tafels van 1 tot 10", blokken=[
            ("p", "Zoek de rij van het eerste getal en de kolom van het tweede. Waar ze elkaar kruisen, staat de uitkomst."),
            ("fig", tafelrooster()),
            ("weetje", "De tafel van 5 eindigt afwisselend op 5 en op 0. De tafel van 2 bestaat alleen uit even getallen."),
        ]),
        dict(kop="Delen is eerlijk verdelen", blokken=[
            ("p", "12 snoepjes eerlijk verdelen over 3 kinderen: elk kind krijgt 4. Je schrijft <strong>12 : 3 = 4</strong>."),
            ("p", "Bij elke deling hoort een vermenigvuldiging. 12 : 3 = 4, want <strong>4 × 3 = 12</strong>. Zo kijk je een deling na."),
        ]),
        dict(kop="Delen met een rest", blokken=[
            ("fig", verdelen_rest(), "14 : 4 = 3 rest 2"),
            ("p", "Soms gaat het niet precies. 14 : 4: er passen 3 groepjes van 4 in (dat is 12), en er blijven er 2 over. "
                  "Je schrijft <strong>14 : 4 = 3 rest 2</strong>."),
            ("p", "De rest is <strong>altijd kleiner</strong> dan het getal waardoor je deelt. Zou er 4 of meer overblijven, "
                  "dan kan je nog een groepje maken."),
        ]),
        dict(kop="Delers, veelvouden en deelbaar door", blokken=[
            ("p", "Een <strong>deler</strong> past precies in een getal: 3 is een deler van 12. "
                  "Een <strong>veelvoud</strong> krijg je door te vermenigvuldigen: 12 is een veelvoud van 3."),
            ("fig", tabel(["Deelbaar door", "Als het getal eindigt op", "Voorbeeld"], [
                ["2", "0, 2, 4, 6 of 8", "34, 70, 106"], ["5", "0 of 5", "45, 80"], ["10", "0", "70, 430"],
                ["100", "00", "300, 3 400"], ["1 000", "000", "2 000, 15 000"]], "100%")),
        ]),
    ],
    onthoud=[
        "4 × 3 = 4 groepjes van 3. Wisselen mag.",
        "× 1 blijft hetzelfde, × 0 is 0, × 10 zet een nul erachter.",
        "Bij elke deling hoort een vermenigvuldiging: 12 : 3 = 4, want 4 × 3 = 12.",
        "De rest is altijd kleiner dan het getal waardoor je deelt.",
        "Deelbaar door 2: eindigt op 0, 2, 4, 6 of 8. Door 5: op 0 of 5. Door 10: op 0.",
    ])

W = "70px"
OEFEN = dict(
    vak="Wiskunde", niveau=READY, titel="Tafels en delen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=["Schrijf met potlood, dan kan je gerust iets uitgommen.",
         "Schrijf bij een vraagstuk altijd je tussenstappen op, ook als je het antwoord al in je hoofd weet.",
         "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."],
    reeksen=[
        dict(kop="Groepjes", oefeningen=[
            ("open", "Teken 3 groepjes van 5 bolletjes. Schrijf er de optelling en de vermenigvuldiging bij.", "5 + 5 + 5 = 15 en 3 × 5 = 15", 3),
            ("rij", [("2 × 6 = 6 × ...", "2"), ("7 × 4 = 4 × ...", "7"), ("9 × 3 = ... × 9", "3")], "Vul aan.", W),
        ]),
        dict(kop="Tafels", opdracht="Reken uit.", oefeningen=[
            ("rij", [("3 × 7", "21"), ("8 × 6", "48"), ("9 × 4", "36"), ("5 × 9", "45"), ("7 × 7", "49"), ("6 × 3", "18")], "", W),
            ("rij", [("4 × 8", "32"), ("10 × 6", "60"), ("0 × 7", "0"), ("1 × 9", "9"), ("8 × 8", "64"), ("9 × 7", "63")], "", W),
            ("rij", [("... × 6 = 42", "7"), ("8 × ... = 72", "9"), ("... × 5 = 40", "8"), ("3 × ... = 27", "9")], "Welk getal ontbreekt?", W),
        ]),
        dict(kop="De tafelkaart", oefeningen=[
            ("open", "Vul de rij van 7 en de rij van 8 volledig in: 7, 14, ... tot 70 en 8, 16, ... tot 80.",
             "7, 14, 21, 28, 35, 42, 49, 56, 63, 70 / 8, 16, 24, 32, 40, 48, 56, 64, 72, 80", 3),
        ]),
        dict(kop="Delen", opdracht="Reken uit en schrijf de vermenigvuldiging erbij om na te kijken.", oefeningen=[
            ("rij", [("24 : 6", "4 (4 × 6 = 24)"), ("45 : 9", "5 (5 × 9 = 45)"), ("63 : 7", "9 (9 × 7 = 63)"), ("32 : 4", "8 (8 × 4 = 32)")], "", "130px"),
            ("rij", [("17 : 5", "3 rest 2"), ("29 : 4", "7 rest 1"), ("50 : 8", "6 rest 2"), ("38 : 6", "6 rest 2")], "Deel met rest.", "110px"),
        ]),
        dict(kop="Delers en deelbaar door", oefeningen=[
            ("open", "Schrijf alle delers van 18 op.", "1, 2, 3, 6, 9, 18", 1),
            ("open", "Schrijf de eerste vijf veelvouden van 6 op.", "6, 12, 18, 24, 30", 1),
            ("rij", [("85", "ja"), ("120", "ja"), ("63", "nee"), ("4 010", "ja")], "Deelbaar door 5? Schrijf ja of nee.", W),
            ("rij", [("700", "ja"), ("1 050", "nee"), ("9 000", "ja"), ("2 300", "ja")], "Deelbaar door 100? Schrijf ja of nee.", W),
            ("waar", "Elk getal dat deelbaar is door 10, is ook deelbaar door 5.", True),
            ("waar", "Bij een deling door 6 kan de rest 7 zijn.", False),
        ]),
        dict(kop="Vraagstukken", opdracht="Schrijf je tussenstappen op en zet de eenheid erbij.", oefeningen=[
            ("open", "Een fiets heeft 2 wielen. Hoeveel wielen hebben 9 fietsen?", "9 × 2 = 18 wielen", 2),
            ("open", "Een klas van 24 leerlingen maakt groepjes van 4. Hoeveel groepjes zijn er?", "24 : 4 = 6 groepjes", 2),
            ("open", "Opa koopt 3 zakken met elk 8 appels. Hij eet er 5 op. Hoeveel appels blijven er over?", "3 × 8 = 24; 24 − 5 = 19 appels", 3),
            ("open", "31 kinderen gaan met de bus. In een minibusje passen 8 kinderen. Hoeveel busjes zijn er nodig?",
             "31 : 8 = 3 rest 7; ook die 7 moeten mee, dus 4 busjes", 3),
            ("open", "Een pak koekjes kost 4 euro. Mama betaalt met een briefje van 20 euro voor 3 pakken. Hoeveel krijgt ze terug?",
             "3 × 4 = 12 euro; 20 − 12 = 8 euro terug", 3),
        ]),
    ])


def maak():
    for maker, b, basis, naam in ((bundel, BUNDEL, HIER.parent, NAAM),
                                  (oefenbundel, OEFEN, HIER.parent.parent / "oefenbundels", "oefenbundel-" + NAAM)):
        tijdelijk = "ready-" + naam
        maker.schrijf(b, tijdelijk)
        subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True)
        doel = basis / "wiskunde" / f"{naam}.pdf"
        doel.write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
        print("  ", doel.relative_to(HIER.parent.parent))


if __name__ == "__main__":
    maak()

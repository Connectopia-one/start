# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundel bij het gratis proefhoofdstuk Rekenen en breuken.

Proefstuk voor een nieuwe soort materiaal: waar de leerbundel de theorie geeft,
geeft deze bundel oefeningen om op papier te maken, met achteraan een
antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan de 37 vragen van het
hoofdstuk op het scherm. Dezelfde leerstof, dezelfde woorden, andere getallen
en andere situaties, zodat je kind twee keer nadenkt en niet twee keer
hetzelfde antwoord opschrijft. Wie hier iets bijschrijft, kijkt dus eerst
`../../start/wiskunde-rekenen-en-breuken.json` na.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, oefenbundel

OEFENBUNDELS = {}

OEFENBUNDELS["oefenbundel-rekenen-en-breuken"] = dict(
    vak="Wiskunde", titel="Rekenen en breuken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Breuken lezen en schrijven",
             opdracht="Kijk goed naar de tekening voor je iets opschrijft.",
             oefeningen=[
                 ("fig", [
                     (svg.breukfiguur("strook", 3, 4), "3/4"),
                     (svg.breukfiguur("cirkel", 5, 6), "5/6"),
                     (svg.breukfiguur("raster", 40, 100), "40/100, of vereenvoudigd 2/5"),
                 ], "Welk deel is gekleurd? Schrijf het als breuk."),
                 ("kleur", [
                     (svg.breukfiguur("strook", 0, 5), "kleur 2/5", "2 van de 5 vakjes gekleurd"),
                     (svg.breukfiguur("cirkel", 0, 8), "kleur 3/8", "3 van de 8 punten gekleurd"),
                 ]),
                 ("rij", [
                     ("In de breuk 7/9 heet de 9 de", "noemer"),
                     ("en de 7 heet de", "teller"),
                 ]),
                 ("open", "Zet deze breuken van klein naar groot: 1/8 &nbsp; 1/2 &nbsp; 1/6 &nbsp; 1/3",
                  "1/8, 1/6, 1/3, 1/2", 1),
                 ("waar", "3/5 en 6/10 zijn evenveel waard.", True),
                 ("waar", "Hoe groter de noemer, hoe groter elk stukje.", False),
             ]),

        dict(kop="Gelijke breuken en vereenvoudigen",
             opdracht="Teller en noemer allebei door hetzelfde getal: dat verandert de waarde niet.",
             oefeningen=[
                 ("rij", [
                     ("1/3 = …/9", "3"),
                     ("3/5 = 6/…", "10"),
                     ("1/2 = 7/…", "14"),
                     ("2/7 = …/21", "6"),
                 ]),
                 ("rij", [
                     ("9/12 =", "3/4"),
                     ("20/25 =", "4/5"),
                     ("14/21 =", "2/3"),
                     ("15/45 =", "1/3"),
                     ("18/24 =", "3/4"),
                     ("30/100 =", "3/10"),
                 ]),
                 ("kies", "Welke breuk hoort niet bij de andere drie?",
                  ["2/6", "3/9", "3/8", "4/12"], 2),
                 ("open", "Lotte zegt dat 4/6 hetzelfde is als 2/3. Heeft ze gelijk? Schrijf erbij "
                          "hoe je het weet.",
                  "Ja. Deel teller en noemer allebei door 2: 4 : 2 = 2 en 6 : 2 = 3, dus 4/6 = 2/3.", 2),
             ]),

        dict(kop="Rekenen met breuken",
             opdracht="Bij optellen en aftrekken met dezelfde noemer verandert die noemer niet.",
             oefeningen=[
                 ("rij", [
                     ("2/7 + 3/7 =", "5/7"),
                     ("5/9 + 1/9 =", "6/9, of 2/3"),
                     ("7/10 − 3/10 =", "4/10, of 2/5"),
                     ("3/8 + 4/8 =", "7/8"),
                     ("11/12 − 5/12 =", "6/12, of 1/2"),
                     ("5/6 − 5/6 =", "0"),
                 ]),
                 ("rij", [
                     ("1/6 van 42 =", "7"),
                     ("3/5 van 40 =", "24"),
                     ("7/8 van 32 =", "28"),
                     ("2/9 van 63 =", "14"),
                     ("3/4 van 36 =", "27"),
                     ("5/6 van 54 =", "45"),
                 ]),
                 ("open", "In een klas van 24 kinderen draagt 1/3 een bril. Hoeveel kinderen dragen "
                          "er géén bril?",
                  "16. Een derde van 24 is 8 kinderen met een bril, dus 24 − 8 = 16 zonder.", 2),
                 ("open", "Je leest een boek van 120 bladzijden en je bent op bladzijde 90. Welk "
                          "deel van het boek heb je gelezen? Schrijf je antwoord zo eenvoudig mogelijk.",
                  "3/4. Je las 90 van de 120 bladzijden, en 90/120 wordt 3/4 als je allebei door 30 "
                  "deelt.", 2),
             ]),

        dict(kop="Breuk, kommagetal en procent",
             opdracht="Drie manieren om hetzelfde te zeggen.",
             oefeningen=[
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [["1/2", "0,5", "50 %"],
                   ["1/4", None, None],
                   ["3/4", None, None],
                   [None, "0,2", None],
                   [None, None, "10 %"]],
                  "1/4 = 0,25 = 25 % · 3/4 = 0,75 = 75 % · 1/5 = 0,2 = 20 % · 1/10 = 0,1 = 10 %"),
                 ("kies", "Wat is het grootst?", ["0,7", "3/4", "even groot"], 1),
                 ("waar", "50 % van een getal is hetzelfde als de helft ervan.", True),
                 ("rij", [
                     ("10 % van 350 =", "35"),
                     ("25 % van 80 =", "20"),
                     ("50 % van 124 =", "62"),
                     ("75 % van 40 =", "30"),
                     ("20 % van 45 =", "9"),
                     ("5 % van 300 =", "15"),
                 ]),
                 ("open", "Een boek van 18 euro krijgt 50 % korting. Hoeveel betaal je?",
                  "9 euro. De helft van 18 is 9.", 1),
                 ("open", "In een doos van 20 koeken zitten er 5 met chocolade. Hoeveel procent van "
                          "de koeken heeft chocolade?",
                  "25 %. 5 van de 20 is 1/4, en 1/4 is 25 %.", 2),
             ]),

        dict(kop="Hoofdrekenen en de juiste volgorde",
             opdracht="Maal en deel gaan voor plus en min. Haakjes gaan voor alles.",
             oefeningen=[
                 ("rij", [
                     ("256 + 137 =", "393"),
                     ("703 − 248 =", "455"),
                     ("15 × 6 =", "90"),
                     ("132 : 11 =", "12"),
                     ("25 × 8 =", "200"),
                     ("1 000 − 472 =", "528"),
                 ]),
                 ("rij", [
                     ("6 + 4 × 3 =", "18"),
                     ("(6 + 4) × 3 =", "30"),
                     ("20 − 2 × 5 =", "10"),
                     ("3 × (8 − 5) =", "9"),
                     ("5 × 4 + 6 =", "26"),
                     ("5 × (4 + 6) =", "50"),
                 ]),
                 ("waar", "Je mag 7 + 3 × 2 gewoon van links naar rechts uitrekenen.", False),
                 ("rij", [
                     ("3,4 + 2,75 =", "6,15"),
                     ("8,5 − 1,25 =", "7,25"),
                     ("0,5 × 16 =", "8"),
                     ("9,6 : 3 =", "3,2"),
                     ("1,5 × 4 =", "6"),
                     ("7,2 + 0,85 =", "8,05"),
                 ]),
                 ("open", "Reken handig uit: 4 × 17 × 25. Schrijf erbij welke twee getallen je "
                          "eerst samen nam.",
                  "1 700. Eerst 4 × 25 = 100, en dan 100 × 17.", 2),
             ]),

        dict(kop="Afronden en zelf denken",
             opdracht="Bij de laatste twee bestaat er meer dan één goed antwoord.",
             oefeningen=[
                 ("rij", [
                     ("3 748 op het tiental =", "3 750"),
                     ("3 748 op het honderdtal =", "3 700"),
                     ("3 748 op het duizendtal =", "4 000"),
                     ("2 950 op het honderdtal =", "3 000"),
                 ]),
                 ("open", "Een touw van 4,5 meter wordt in stukken van 75 cm geknipt. Hoeveel "
                          "stukken krijg je?",
                  "6 stukken. 4,5 meter is 450 cm, en 450 : 75 = 6.", 2),
                 ("open", "Vier vrienden verdelen 3 pizza's eerlijk. Hoeveel pizza krijgt elk? "
                          "Schrijf je antwoord als breuk.",
                  "3/4 pizza. Snijd elke pizza in vieren: dat zijn 12 stukken voor 4 kinderen, "
                  "dus 3 stukken elk.", 2),
                 ("open", "Verzin zelf twee sommen waarvan het antwoord 3/4 is, en die niet op "
                          "elkaar lijken.",
                  "Alles wat 3/4 oplevert is goed, bijvoorbeeld 1/4 + 2/4, of 6/8 vereenvoudigd, "
                  "of 75 % van 1, of 1 − 1/4.", 3),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)

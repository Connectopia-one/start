"""Licht en geluid — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Bolle lens met constructiestralen -------------------------------------------------
LE = Prent("bolle-lens", "Een kaars voor een bolle lens", "optische as met een bolle lens in het midden, brandpunten F links en rechts op 150 px, punten 2F op 300 px; een kaars als pijl op 375 px links van de lens; vier mogelijke beeldplaatsen rechts: A tussen F en 2F omgekeerd, B voorbij 2F omgekeerd, C links rechtop vergroot, D precies op 2F omgekeerd")
AY, LX, FF = 330, 500, 150
LE.lijn(40, AY, 960, AY, DONKER, 2)
LE.ellips(LX, AY, 18, 200, "#dfeef4", BLAUW, 3)
for k, dx in (("F", -FF), ("F", FF), ("2F", -2 * FF), ("2F", 2 * FF)):
    LE.cirkel(LX + dx, AY, 6, DONKER, DONKER, 1)
    LE.tekst(LX + dx, AY - 16, k, 18, vet=True)
VX, VH = LX - 375, 100
LE.pijl(VX, AY, VX, AY - VH, ROOD, 6)
LE.tekst(VX, AY - VH - 16, "kaars", 16)
# echt beeld: 1/b = 1/f - 1/v -> b = 250, vergroting 250/375 = 0,67
BX, BH = LX + 250, VH * 250 / 375
OPT = {"A": (BX, BH), "B": (LX + 400, 110), "C": (LX - 470, -150), "D": (LX + 300, VH)}
LLE = {}
for k, (x, h) in OPT.items():
    if h > 0:
        LE.pijl(x, AY, x, AY + h, PAARS, 5)
        LLE[k] = (x + 30, AY + h + 20)
    else:
        LE.pijl(x, AY, x, AY + h, PAARS, 5)
        LLE[k] = (x + 30, AY + h - 10)
    LE.letter(*LLE[k], k)
ZLE = {k: [Prent.zone(x - 22, AY + min(0, h) - 5, 44, abs(h) + 10), Prent.rond(*LLE[k], 22)] for k, (x, h) in OPT.items()}

# Vier geluiden op een oscilloscoop -------------------------------------------------
OS = Prent("vier-geluiden", "Vier geluiden op het scherm van een oscilloscoop", "vier vakjes met dezelfde tijdschaal; A: 2 trillingen, amplitude 40; B: 4 trillingen, amplitude 40; C: 2 trillingen, amplitude 80; D: 2 trillingen met een grillige vorm, amplitude 40")
VAK = {"A": (60, 80), "B": (520, 80), "C": (60, 360), "D": (520, 360)}
W, H = 420, 240
for k, (x0, y0) in VAK.items():
    OS.rect(x0, y0, W, H, "#f4f8f0", DONKER, 10, 2)
    OS.lijn(x0 + 10, y0 + H / 2, x0 + W - 10, y0 + H / 2, GRIJS, 1, stippel=True)
    n, a = {"A": (2, 40), "B": (4, 40), "C": (2, 80), "D": (2, 40)}[k]
    pts = []
    for i in range(301):
        t = i / 300
        if k == "D":
            y = a * (0.75 * math.sin(2 * math.pi * n * t) + 0.35 * math.sin(2 * math.pi * 3 * n * t) + 0.2 * math.sin(2 * math.pi * 5 * n * t)) / 1.0
        else:
            y = a * math.sin(2 * math.pi * n * t)
        pts.append((x0 + 20 + t * (W - 40), y0 + H / 2 - y))
    OS.pad("M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts), "none", BLAUW, 3)
    OS.letter(x0 + 28, y0 + 28, k)
ZOS = {k: [Prent.zone(x0, y0, W, H)] for k, (x0, y0) in VAK.items()}

VRAGEN = [
    klik(
        "Klik op het beeld dat de lens van de kaars maakt.",
        LE.bestand, ZLE["A"],
        "De straal evenwijdig aan de as gaat door F, de straal door het midden gaat rechtdoor; ze snijden tussen F en 2F.",
    ),
    met_prent(LE.bestand, tabel(
        "Klopt dit voor het beeld van de kaars?",
        [
            ("Het is reëel.", J),
            ("Het staat rechtop.", F),
            ("Het is kleiner dan de kaars.", J),
        ],
        "Staat het voorwerp verder dan 2F, dan is het beeld reëel, omgekeerd en kleiner.",
    )),
    met_prent(LE.bestand, mk(
        "Je schuift de kaars tot tussen F en de lens. Welk beeld krijg je dan?",
        ["Een virtueel, rechtopstaand, groter beeld", "Een reëel, omgekeerd en kleiner beeld op een scherm", "Een reëel, omgekeerd en groter beeld achter 2F", "Geen beeld"],
        0,
        "Zo werkt een vergrootglas.",
    )),
    klik(
        "Klik op het beeld dat je zou krijgen als de kaars precies op 2F links stond.",
        LE.bestand, ZLE["D"],
        "Op 2F is het beeld even groot en omgekeerd, ook op 2F.",
    ),
    met_prent(LE.bestand, inv(
        "De brandpuntsafstand is 10 cm en de kaars staat 25 cm van de lens. Hoe ver achter de lens ontstaat het beeld, in cm?",
        ["16,7", "16,67", "17", "16,7 cm", "50/3"],
        "1/b = 1/10 − 1/25 = 3/50, dus b ≈ 16,7 cm.",
    )),
    klik(
        "Welk geluid klinkt het hoogst?",
        OS.bestand, ZOS["B"],
        "Meer trillingen in dezelfde tijd betekent een hogere frequentie.",
    ),
    klik(
        "Welk geluid klinkt het luidst?",
        OS.bestand, ZOS["C"],
        "Een grotere amplitude geeft een luider geluid.",
    ),
    klik(
        "Welk geluid heeft dezelfde toonhoogte en sterkte als A maar een andere klankkleur?",
        OS.bestand, ZOS["D"],
        "Zelfde periode en uitwijking, andere vorm door boventonen.",
    ),
    met_prent(OS.bestand, mk(
        "De tijdschaal is 1 ms per breedte van een vakje. Welke frequentie heeft geluid A?",
        ["2000 Hz", "500 Hz", "2 Hz", "200 Hz"],
        0,
        "Twee trillingen in 1 ms: T = 0,5 ms, f = 2000 Hz.",
    )),
    mk(
        "Een onweer is 1,7 km ver. Na hoeveel tijd hoor je de donder? Neem 340 m/s.",
        ["5,0 s", "0,5 s", "1,7 s", "50 s"],
        0,
        "t = d / v = 1700 / 340 = 5,0 s.",
    ),
    mk(
        "Een vleermuis hoort de echo van een muur 0,020 s na haar kreet. Hoe ver is de muur? Neem 340 m/s.",
        ["3,4 m", "6,8 m", "17 m", "0,34 m"],
        0,
        "Het geluid gaat heen en terug: d = 340 · 0,020 / 2.",
    ),
    inv(
        "Een snaar heeft een grondtoon van 330 Hz. Welke frequentie heeft de tweede harmonische, in Hz?",
        ["660", "660 Hz"],
        "f₂ = 2 · f₁.",
    ),
    mk(
        "Een geluid stijgt van 50 dB naar 70 dB. Hoeveel keer zo intens wordt het?",
        ["100 keer", "20 keer", "2 keer", "1,4 keer"],
        0,
        "Elke 10 dB is tien keer zo intens: 10 · 10.",
    ),
    mk(
        "Je staat 2 m van een luidspreker en stapt achteruit tot 6 m. Hoe verandert de intensiteit?",
        ["Ze wordt 9 keer zo klein", "Ze wordt 3 keer zo klein", "Ze wordt 6 keer zo klein", "Ze blijft overal even groot"],
        0,
        "De intensiteit daalt met het kwadraat van de afstand: (6/2)² = 9.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een ambulance die nadert klinkt hoger dan wanneer ze stilstaat.", J),
            ("Geluid gaat in koude lucht sneller dan in warme.", F),
            ("Een foton van blauw licht heeft meer energie dan een van rood licht.", J),
            ("Een vlakke spiegel geeft een beeld dat je op een scherm kan opvangen.", F),
        ],
        "Hogere frequentie, meer foton-energie: E = h · f.",
    ),
    volgorde(
        "Zet deze stralingen van grote naar kleine golflengte.",
        ["radiogolven", "infrarood", "zichtbaar licht", "röntgenstraling"],
        "Hoe kleiner de golflengte, hoe groter de frequentie en de energie.",
    ),
    sorteer(
        "Is deze straling ioniserend of niet?",
        ["Ioniserend", "Niet ioniserend"],
        [
            ("gammastraling", "Ioniserend"),
            ("röntgenstraling", "Ioniserend"),
            ("microgolven", "Niet ioniserend"),
            ("radiogolven", "Niet ioniserend"),
            ("infrarood", "Niet ioniserend"),
        ],
        "Pas vanaf hoogenergetisch uv kan een foton een elektron losslaan.",
    ),
    koppel(
        "Koppel elke toepassing aan de straling of het geluid dat ze gebruikt.",
        [
            ("echografie van een baby", "ultrasoon geluid"),
            ("nachtkijker", "infrarood"),
            ("bagagescanner", "röntgenstraling"),
            ("magnetron", "microgolven"),
        ],
        ["infrasoon geluid"],
        "Elke toepassing kiest de golf die door het juiste materiaal dringt of erin opgaat.",
    ),
    mk(
        "Welk foton heeft de meeste energie?",
        ["Een foton van uv-straling", "Een foton van groen licht", "Een foton van infrarood", "Een foton van een radiogolf"],
        0,
        "Uv heeft hier de hoogste frequentie.",
    ),
    inv(
        "Hoeveel keer meer energie heeft een foton met dubbele frequentie?",
        ["2", "2 keer", "twee", "dubbel"],
        "E = h · f is recht evenredig met f.",
    ),
    casus(
        "Bij een zonsverduistering schuift de maan voor de zon. Op een deel van de aarde valt de kernschaduw, eromheen de bijschaduw.",
        [
            keuze(
                "In de kernschaduw is de zon [[*helemaal|maar voor een deel]] bedekt.",
                "Daar komt geen licht van de bron meer toe.",
            ),
            keuze(
                "In de bijschaduw zie je een [[*gedeeltelijke|volledige]] verduistering.",
                "Een stuk van de zon is nog zichtbaar.",
            ),
            mk(
                "Waarom ontstaat er een bijschaduw?",
                ["De zon is geen puntbron", "Licht buigt rond de maan", "De maan geeft zelf licht", "De aarde draait"],
                0,
                "Een uitgebreide bron geeft een kern- en een bijschaduw.",
            ),
        ],
    ),
    mk(
        "Waarom zie je jezelf wel in een spiegel maar niet in een wit blad papier?",
        ["Papier kaatst het licht diffuus terug", "Papier slorpt al het licht dat erop valt op", "Papier breekt het licht naar de normaal toe", "Papier laat het meeste licht gewoon door"],
        0,
        "Een ruw oppervlak stuurt de stralen alle kanten op.",
    ),
    keuze(
        "In de proef van Young ontstaat een donkere streep waar de golven van beide spleten [[*in tegenfase|in fase]] aankomen.",
        "Daar doven ze elkaar uit.",
    ),
    mk(
        "Waarom gebruiken mensen oordopjes die alle tonen even sterk dempen in plaats van gewone schuimdopjes?",
        ["Muziek blijft dan natuurlijk klinken", "Ze laten vooral de hoge tonen sterker door", "Ze dempen enkel de bassen van de muziek", "Ze maken het geluid in je oor net luider"],
        0,
        "Ze verlagen het niveau zonder de klankkleur te verknoeien.",
    ),
    mk(
        "Waarom loopt geluid in staal sneller dan in lucht?",
        ["De deeltjes hangen steviger aan elkaar", "Staal is warmer dan lucht", "Staal heeft minder deeltjes per liter", "Geluid is in staal een transversale golf"],
        0,
        "Stevig gebonden deeltjes geven de beweging vlugger door.",
    ),
    inv(
        "Geluid loopt 340 m/s. Hoe ver is een onweer als je de donder 9,0 s na de bliksem hoort, in km?",
        ["3,1", "3,06", "3", "3,1 km"],
        "d = 340 · 9,0 = 3060 m ≈ 3,1 km.",
    ),
    sleep(
        "Geluid onder 20 Hz heet [[infrasoon]], boven 20 000 Hz [[ultrasoon]]. Vanaf ongeveer [[80]] dB loop je kans op gehoorschade.",
        ["120", "supersoon"],
        "Rond 120 dB ligt de pijndrempel.",
    ),
    open_(
        "Leg uit waarom je de grondtoon van een snaar hoger krijgt als je ze korter maakt.",
        "Bij de grondtoon past een halve golflengte op de snaar. Een kortere snaar geeft dus een kleinere golflengte. De golfsnelheid op de snaar blijft gelijk, dus wordt de frequentie f = v / λ groter: de toon gaat omhoog.",
    ),
]

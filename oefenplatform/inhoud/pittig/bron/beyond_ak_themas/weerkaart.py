"""Het weer in Europa — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Depressie met fronten -----------------------------------------------------
DP = Prent("depressie-fronten", "Een depressie met haar fronten, van bovenaf (noord is boven)", "lagedrukkern met warmtefront naar het oosten en koufront naar het zuidwesten; punten A, B, C")
LX, LY = 360, 200
for r in (50, 100, 150):
    DP.ellips(LX + 40, LY + 40, r * 1.5, r, "none", "#9bb4c8", 1)
DP.tekst(LX, LY + 12, "L", 36, kleur=BLAUW, vet=True)
# warmtefront: van de kern naar het zuidoosten
WF = [(LX + 30, LY + 40), (520, 260), (640, 330), (760, 380)]
DP.pad("M" + " L ".join(f"{x} {y}" for x, y in WF), "none", ROOD, 4)
for (x1, y1), (x2, y2) in zip(WF, WF[1:]):
    for t in (0.35, 0.75):
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        a = math.atan2(y2 - y1, x2 - x1)
        nx, ny = math.sin(a), -math.cos(a)
        DP.pad(f"M{x - 12 * math.cos(a):.0f} {y - 12 * math.sin(a):.0f} A 12 12 0 0 1 {x + 12 * math.cos(a):.0f} {y + 12 * math.sin(a):.0f} Z", ROOD, "none")
# koufront: van de kern naar het zuidwesten
KF = [(LX + 10, LY + 50), (330, 300), (270, 420), (200, 540)]
DP.pad("M" + " L ".join(f"{x} {y}" for x, y in KF), "none", BLAUW, 4)
for (x1, y1), (x2, y2) in zip(KF, KF[1:]):
    for t in (0.35, 0.75):
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        a = math.atan2(y2 - y1, x2 - x1)
        nx, ny = -math.sin(a), math.cos(a)
        p1 = (x - 12 * math.cos(a), y - 12 * math.sin(a)); p2 = (x + 12 * math.cos(a), y + 12 * math.sin(a))
        tip = (x - 18 * nx, y - 18 * ny)
        DP.svg(f'<polygon points="{p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f} {tip[0]:.0f},{tip[1]:.0f}" fill="{BLAUW}"/>')
DP.pijl(560, 520, 720, 520, DONKER, 3)
DP.tekst(640, 505, "verplaatsing", 15)
PT = {"A": (720, 220), "B": (470, 420), "C": (150, 330)}
for k, (x, y) in PT.items():
    DP.letter(x, y, k)
ZDP = {"A": [Prent.rond(720, 220, 60)], "B": [Prent.rond(470, 420, 60)], "C": [Prent.rond(150, 330, 60)],
       "WF": [Prent.zone(500, 240, 280, 160)], "KF": [Prent.zone(190, 290, 160, 260)]}

# Luchtsoorten naar België ----------------------------------------------
LS = Prent("luchtsoorten-belgie", "Waar komt de lucht vandaan?", "België in het midden met vier aanvoerpijlen 1 tot 4")
BX, BY = 500, 330
LS.rect(BX - 40, BY - 25, 80, 50, "#f2e3a0", DONKER, 6)
LS.tekst(BX, BY + 6, "België", 16, vet=True)
LS.ellips(160, 330, 120, 200, "#cfe3f1", "none")
LS.tekst(160, 330, "oceaan", 18)
LS.pijl(500, 70, 500, BY - 35, "#5b7fa6", 6)
LS.pijl(880, 330, BX + 50, BY, "#7a8a9a", 6)
LS.pijl(500, 600, 500, BY + 35, ORANJE, 6)
LS.pijl(260, 230, BX - 50, BY - 10, BLAUW, 6)
LS.tekst(500, 60, "uit het poolgebied", 15)
LS.tekst(880, 310, "uit Rusland", 15, "end")
LS.tekst(500, 625, "uit de Sahara", 15)
NR = {"1": (530, 150), "2": (760, 300), "3": (530, 500), "4": (330, 230)}
for k, (x, y) in NR.items():
    LS.letter(x, y, k)
ZLS = {"1": [Prent.zone(470, 70, 60, 220), Prent.rond(*NR["1"], 26)], "2": [Prent.zone(550, 300, 340, 60), Prent.rond(*NR["2"], 26)],
       "3": [Prent.zone(470, 370, 60, 230), Prent.rond(*NR["3"], 26)], "4": [Prent.zone(260, 200, 200, 80), Prent.rond(*NR["4"], 26)]}

VRAGEN = [
    klik(
        "Klik op de warme sector.",
        DP.bestand, ZDP["B"],
        "Tussen het warmtefront en het koufront.",
    ),
    klik(
        "Klik op het warmtefront.",
        DP.bestand, ZDP["WF"],
        "Rode halve cirkels: warme lucht schuift traag over koude lucht.",
    ),
    klik(
        "Klik op het koufront.",
        DP.bestand, ZDP["KF"],
        "Blauwe driehoekjes: koude lucht duikt onder de warme.",
    ),
    met_prent(DP.bestand, tabel(
        "De depressie trekt naar het oosten. Wat komt er de volgende uren bij plaats A?",
        [
            ("eerst hoge sluierwolken", J),
            ("daarna langdurige, gelijkmatige regen", J),
            ("meteen een felle bui en opklaringen", F),
            ("later een zachtere, vochtige periode", J),
        ],
        "Eerst het warmtefront, dan de warme sector, dan het koufront.",
    )),
    met_prent(DP.bestand, keuze(
        "Bij plaats C is het koufront al voorbij. Het is er [[*frisser met buien en opklaringen|zachter en de hele dag grijs|windstil en mistig]].",
        "Achter een koufront komt koudere lucht met buien.",
    )),
    klik(
        "Klik op de aanvoer die bij ons een hittegolf kan brengen.",
        LS.bestand, ZLS["3"],
        "Continentaal tropische lucht: heet en droog, van boven Spanje en de Sahara.",
    ),
    klik(
        "Klik op de aanvoer die in de winter droge, strenge vorst brengt.",
        LS.bestand, ZLS["2"],
        "Continentaal polaire lucht uit het oosten.",
    ),
    met_prent(LS.bestand, tabel(
        "Kijk naar de pijlen. Welke luchtsoort komt er telkens?",
        [
            ("pijl 1", "Arctisch"),
            ("pijl 2", "Continentaal polair"),
            ("pijl 3", "Continentaal tropisch"),
            ("pijl 4", "Maritiem polair"),
        ],
        "Herkomst geeft de temperatuur, de weg over zee of land de vochtigheid.",
        kolommen=["Arctisch", "Maritiem polair", "Continentaal polair", "Continentaal tropisch"],
    )),
    tabel(
        "Warmtefront of koufront?",
        [
            ("flauwe helling van het frontvlak", "Warmtefront"),
            ("korte, hevige buien en soms onweer", "Koufront"),
            ("langdurige, gelijkmatige regen", "Warmtefront"),
            ("de wind draait en wordt plots krachtiger", "Koufront"),
            ("hoge sluierwolken lang op voorhand", "Warmtefront"),
        ],
        "Bij een koufront wordt de warme lucht steil opgetild.",
        kolommen=["Warmtefront", "Koufront"],
    ),
    volgorde(
        "Zet de doortocht van een depressie in de juiste volgorde.",
        [
            "Hoge sluierwolken verschijnen",
            "Het warmtefront brengt lange regen",
            "In de warme sector is het tijdelijk zachter",
            "Het koufront brengt een felle bui",
            "Frissere lucht met opklaringen",
        ],
        "Zo trekt een depressie van west naar oost over ons.",
    ),
    tabel(
        "Klopt dit over een occlusiefront?",
        [
            ("Het koufront heeft het warmtefront ingehaald.", J),
            ("De warme lucht is van de grond getild.", J),
            ("Het ontstaat in het begin van het leven van een depressie.", F),
        ],
        "Een occlusie hoort bij een oudere depressie.",
    ),
    tabel(
        "Maritiem of continentaal?",
        [
            ("lucht die lang over de oceaan trok", "Maritiem"),
            ("droge lucht die over Rusland kwam", "Continentaal"),
            ("lucht die veel vocht meebrengt", "Maritiem"),
            ("lucht die in de winter strenge vorst geeft", "Continentaal"),
        ],
        "Over land neemt lucht geen vocht op.",
        kolommen=["Maritiem", "Continentaal"],
    ),
    casus(
        "Het is januari. Boven Scandinavië ligt een krachtig hogedrukgebied, boven de Middellandse Zee een depressie.",
        [
            keuze(
                "Rond het hogedrukgebied draait de wind met de klok mee. Bij ons waait er dan een [[*oostenwind|westenwind|zuidwestenwind]].",
                "De wind komt uit Rusland.",
            ),
            tabel(
                "Wat verwacht je in België?",
                [
                    ("droog weer", J),
                    ("strenge vorst", J),
                    ("zachte, natte zeelucht", F),
                ],
                "Continentaal polaire lucht is koud en droog.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over isobaren op een weerkaart?",
        [
            ("Dicht bij elkaar betekent harde wind.", J),
            ("De wind waait bijna evenwijdig aan de isobaren.", J),
            ("De wind waait loodrecht door de isobaren naar het centrum.", F),
            ("Een H staat voor een hogedrukkern.", J),
        ],
        "Het corioliseffect buigt de wind af, zodat hij bijna langs de isobaren waait.",
    ),
    mk(
        "Waarom is een voorspelling voor volgende week minder betrouwbaar dan een voor morgen?",
        [
            "Kleine fouten in de begintoestand groeien aan",
            "Weerballonnen meten maar om de zeven dagen opnieuw de lucht",
            "De straalstroom ligt elke week op een andere vaste plaats",
            "Fronten bewegen telkens sneller naarmate de week vordert",
        ],
        0,
        "De atmosfeer is een chaotisch systeem.",
    ),
    tabel(
        "Waar liggen de neerslagzones op een weerkaart vooral?",
        [
            ("langs de fronten", J),
            ("in de kern van een hogedrukgebied", F),
            ("in de warme sector bij een warmtefront", J),
            ("rond een depressie", J),
        ],
        "Waar lucht opgetild wordt, condenseert ze.",
    ),
    tabel(
        "Klopt dit over de straalstroom en ons weer?",
        [
            ("Hij stuurt de baan van de depressies.", J),
            ("Golft hij sterk, dan kan hetzelfde weer weken blijven.", J),
            ("Hij waait vlak boven de grond.", F),
        ],
        "Hij waait op ongeveer tien kilometer hoogte.",
    ),
    sleep(
        "Depressies ontstaan op het [[polaire front]], waar koude poollucht en warme subtropische lucht elkaar raken. Ze trekken met de [[westenwind]] van west naar oost. Daarom is ons weer zo [[wisselvallig]].",
        ["subtropisch maximum", "passaat", "stabiel"],
        "België ligt in de baan van de depressies.",
    ),
    keuze(
        "Trekt een depressie noordelijk van ons voorbij, dan draait de wind van zuidwest naar [[*west en noordwest|oost en noordoost|zuid en zuidoost]].",
        "Voor het front zuidwest, na het koufront noordwest.",
    ),
    tabel(
        "Arctisch, polair of tropisch?",
        [
            ("de koudste lucht, van boven het poolijs", "Arctisch"),
            ("frisse lucht van hoge breedten", "Polair"),
            ("warme lucht uit het zuiden", "Tropisch"),
        ],
        "Herkomst bepaalt de temperatuur.",
        kolommen=["Arctisch", "Polair", "Tropisch"],
    ),
    met_prent(DP.bestand, tabel(
        "Kijk naar de kaart. Klopt dit?",
        [
            ("Het warmtefront heeft rode halve cirkels.", J),
            ("Het koufront heeft blauwe driehoekjes.", J),
            ("De symbolen wijzen in de richting waarin het front trekt.", J),
            ("De depressie trekt naar het westen.", F),
        ],
        "Depressies trekken bij ons van west naar oost.",
    )),
    met_prent(LS.bestand, keuze(
        "Pijl 4 brengt maritiem polaire lucht: [[*fris en vochtig|heet en droog|ijskoud en droog]].",
        "Ze trok over de oceaan en nam vocht op.",
    )),
    klik(
        "Klik op de plaats waar het koufront al voorbij is.",
        DP.bestand, ZDP["C"],
        "Het front trekt naar het oosten, dus de plaats ten westen ervan heeft het al gehad.",
    ),
    keuze(
        "Op een weerkaart staat een A voor een [[*anticycloon|depressie|occlusie]].",
        "A en H betekenen allebei hogedruk.",
    ),
    tabel(
        "Een depressie ligt ten westen van Ierland en trekt naar het oosten. Wat verwacht je de komende dag bij ons?",
        [
            ("toenemende wind", J),
            ("regen van het warmtefront", J),
            ("een week lang droog en windstil weer", F),
        ],
        "De depressie komt met haar fronten naar ons toe.",
    ),
    inv(
        "Hoeveel soorten fronten zie je op een gewone weerkaart: warmtefront, koufront en nog één? Schrijf het totale aantal.",
        ["3", "drie"],
        "Warmtefront, koufront en occlusiefront.",
    ),
    tabel(
        "Welke gegevens lees je af van deze lijnen op een weerkaart?",
        [
            ("isobaren", "Luchtdruk"),
            ("isothermen", "Temperatuur"),
            ("isohyeten", "Neerslag"),
        ],
        "Iso betekent gelijk.",
        kolommen=["Luchtdruk", "Temperatuur", "Neerslag"],
    ),
    keuze(
        "Na de doortocht van een koufront wordt het meestal [[*frisser|zachter|mistiger]].",
        "Achter het koufront komt koudere lucht.",
    ),
    open_(
        "Leg uit waarom een koufront kortere maar hevigere neerslag geeft dan een warmtefront.",
        "Bij een koufront duwt de zware koude lucht zich onder de warme lucht. Die wordt steil en snel opgetild, zodat er hoge stapelwolken ontstaan met felle buien en soms onweer. Bij een warmtefront klimt de warme lucht traag over een flauwe helling, wat lange, gelijkmatige regen geeft.",
    ),
]

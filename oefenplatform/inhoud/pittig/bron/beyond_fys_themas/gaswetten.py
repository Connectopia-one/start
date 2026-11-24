"""De gaswetten en de algemene gaswet — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Drie grafieken --------------------------------------------------------------
DG = Prent("drie-gasgrafieken", "Drie grafieken van een vaste hoeveelheid gas", "drie kleine grafieken: P een dalende kromme van p tegen V, Q een rechte door de oorsprong van V tegen T in kelvin, R een stijgende rechte van p tegen θ in graden celsius die verlengd de as snijdt bij −273 °C")
for i, (k, xl, yl) in enumerate((("P", "V", "p"), ("Q", "T (K)", "V"), ("R", "θ (°C)", "p"))):
    x0 = 60 + i * 320
    ox, oy = x0 + 40, 470
    DG.rect(x0, 90, 290, 430, "#ffffff", DONKER, 14, 2)
    if k == "R":
        ox = x0 + 150
        DG.lijn(x0 + 20, oy, x0 + 275, oy, DONKER, 2)
    else:
        DG.lijn(ox, oy, x0 + 275, oy, DONKER, 2)
    DG.lijn(ox, oy, ox, 120, DONKER, 2)
    DG.tekst(x0 + 262, oy + 30, xl, 18, anker="end")
    DG.tekst(ox - 10, 118, yl, 18, anker="end")
    if k == "P":
        pts = [(ox + 20 + j * 6, oy - 6000 / (20 + j * 6)) for j in range(0, 36)]
        DG.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", BLAUW, 4)
    elif k == "Q":
        DG.lijn(ox, oy, ox + 220, oy - 300, BLAUW, 4)
    else:
        DG.lijn(ox, oy - 160, ox + 110, oy - 300, BLAUW, 4)
        DG.lijn(x0 + 30, oy, ox, oy - 160, BLAUW, 2, stippel=True)
        DG.tekst(x0 + 30, oy + 26, "−273", 16)
        DG.tekst(ox, oy + 26, "0", 16)
    DG.letter(x0 + 145, 580, k)
ZDG = {k: [Prent.zone(60 + i * 320, 90, 290, 430), Prent.rond(60 + i * 320 + 145, 580, 26)] for i, k in enumerate("PQR")}

# Cilinders met een zuiger ---------------------------------------------------------
CZ = Prent("cilinders-zuiger", "Een gas in een cilinder met zuiger: begintoestand en drie mogelijke eindtoestanden", "links de begintoestand: 3,0 L bij 300 K en 100 kPa; daarnaast drie cilinders A (1,5 L), B (6,0 L) en C (3,0 L); een schaal in liter")
LIT = 50  # pixels per liter
BODEM = 560


def cilinder(p, x, v, kleur):
    p.rect(x - 60, BODEM - 6.6 * LIT, 120, 6.6 * LIT, "#ffffff", DONKER, 4, 3)
    p.rect(x - 57, BODEM - v * LIT, 114, v * LIT - 3, kleur, "none", 0, 0)
    p.rect(x - 58, BODEM - v * LIT - 14, 116, 14, GRIJS, DONKER, 2, 2)
    p.lijn(x, BODEM - v * LIT - 14, x, BODEM - 6.6 * LIT - 30, DONKER, 4)


cilinder(CZ, 140, 3.0, "#dbe8f4")
CZ.tekst(140, 600, "begin: 3,0 L, 300 K, 100 kPa", 16, vet=True)
for k, x, v in (("A", 420, 1.5), ("B", 620, 6.0), ("C", 820, 3.0)):
    cilinder(CZ, x, v, "#f6e1c8")
    CZ.letter(x, 600, k)
for lv in range(0, 7):
    CZ.lijn(940, BODEM - lv * LIT, 955, BODEM - lv * LIT, DONKER, 2)
    CZ.tekst(965, BODEM - lv * LIT + 6, f"{lv} L", 14, anker="start")
CZ.lijn(940, BODEM, 940, BODEM - 6 * LIT, DONKER, 2)
ZCZ = {k: [Prent.zone(x - 62, BODEM - 6.6 * LIT - 30, 124, 6.6 * LIT + 30), Prent.rond(x, 600, 24)] for k, x in (("A", 420), ("B", 620), ("C", 820))}

VRAGEN = [
    klik(
        "Klik op de grafiek van een isotherm proces.",
        DG.bestand, ZDG["P"],
        "Bij constante temperatuur is p · V constant: een dalende kromme.",
    ),
    klik(
        "Klik op de grafiek van een isobaar proces.",
        DG.bestand, ZDG["Q"],
        "Bij constante druk is V recht evenredig met T in kelvin: een rechte door de oorsprong.",
    ),
    met_prent(DG.bestand, tabel(
        "Welk proces hoort bij deze grafiek?",
        [
            ("P", "Isotherm"),
            ("Q", "Isobaar"),
            ("R", "Isochoor"),
        ],
        "R toont p tegen θ: bij constant volume stijgt de druk lineair met de temperatuur.",
        kolommen=["Isotherm", "Isobaar", "Isochoor"],
    )),
    met_prent(DG.bestand, mk(
        "Waarom gaat de rechte van R niet door het nulpunt van de θ-as?",
        [
            "De druk is pas nul bij −273 °C",
            "Het gas lekt een beetje weg",
            "Bij 0 °C bevriest het gas altijd",
            "De meting is slecht uitgevoerd",
        ],
        0,
        "Recht evenredig geldt met T in kelvin; in °C is de nulwaarde verschoven naar −273.",
    )),
    klik(
        "Klik op de eindtoestand na verwarmen tot 600 K bij gelijke druk.",
        CZ.bestand, ZCZ["B"],
        "V / T constant: de temperatuur verdubbelt, dus het volume ook: 6,0 L.",
    ),
    klik(
        "Klik op de eindtoestand na samenpersen tot 200 kPa bij gelijke temperatuur.",
        CZ.bestand, ZCZ["A"],
        "p · V constant: dubbele druk, half volume: 1,5 L.",
    ),
    met_prent(CZ.bestand, mk(
        "C is ontstaan door het gas bij vastgezette zuiger te verwarmen tot 600 K. Welke druk heeft het nu?",
        ["200 kPa", "100 kPa", "50 kPa", "300 kPa"],
        0,
        "Isochoor: p / T constant, dus dubbele T geeft dubbele druk.",
    )),
    met_prent(CZ.bestand, keuze(
        "In A bewegen de deeltjes gemiddeld [[*even snel als|sneller dan|trager dan]] in de begintoestand.",
        "Isotherm: de temperatuur, en dus de gemiddelde kinetische energie, is dezelfde.",
    )),
    inv(
        "Een gas van 3,0 L bij 27 °C wordt bij gelijke druk verwarmd tot 127 °C. Welk volume krijgt het, in L?",
        ["4", "4,0", "4 L", "4,0 L"],
        "In kelvin: 300 K en 400 K. V₂ = 3,0 · 400 / 300 = 4,0 L.",
    ),
    inv(
        "Een gas van 8,0 L bij 150 kPa zet bij gelijke temperatuur uit tot 12 L. Welke druk heeft het dan, in kPa?",
        ["100", "100 kPa"],
        "p₂ = p₁ · V₁ / V₂ = 150 · 8,0 / 12 = 100 kPa.",
    ),
    inv(
        "Een gas gaat van 2,0 L bij 300 K en 100 kPa naar 450 K en 150 kPa. Welk volume krijgt het, in L?",
        ["2", "2,0", "2 L", "2,0 L"],
        "V₂ = V₁ · (p₁ / p₂) · (T₂ / T₁) = 2,0 · (100 / 150) · (450 / 300) = 2,0 L.",
    ),
    inv(
        "Een fietsband staat op 2,0 bar bij 7 °C. In de zon wordt hij 42 °C. Welke druk krijgt hij bij gelijk volume, in bar?",
        ["2,25", "2,25 bar", "2.25", "2,3"],
        "280 K en 315 K: p₂ = 2,0 · 315 / 280 = 2,25 bar.",
    ),
    inv(
        "Hoeveel kelvin is −23 °C?",
        ["250", "250 K"],
        "T = θ + 273 = −23 + 273 = 250 K.",
    ),
    mk(
        "Je verdubbelt de temperatuur in kelvin en halveert het volume. Wat gebeurt er met de druk?",
        ["Ze wordt 4 keer zo groot", "Ze blijft gelijk", "Ze wordt 2 keer zo groot", "Ze wordt de helft"],
        0,
        "p = n · R · T / V: × 2 en nog eens × 2.",
    ),
    mk(
        "Hoeveel mol gas zit er in 0,0249 m³ bij 300 K en 200 kPa? Neem R = 8,31 J/(mol·K).",
        ["2,0 mol", "0,50 mol", "20 mol", "1,0 mol"],
        0,
        "n = p · V / (R · T) = 200 000 · 0,0249 / (8,31 · 300) ≈ 2,0 mol.",
    ),
    mk(
        "Welk volume nemen 2,0 mol van een ideaal gas in bij normomstandigheden?",
        ["44,8 L", "22,4 L", "11,2 L", "2,0 L"],
        0,
        "Eén mol neemt 22,4 L in, dus twee mol 44,8 L.",
    ),
    mk(
        "Welk gas neemt bij normomstandigheden per mol het grootste volume in?",
        ["Ze nemen allemaal evenveel in", "Waterstof, want het is het lichtst", "Koolstofdioxide, want het is het zwaarst", "Zuurstof, want het komt het meest voor"],
        0,
        "Voor elk ideaal gas: 22,4 L per mol, los van de massa van de deeltjes.",
    ),
    mk(
        "Een luchtbel van 1,0 cm³ op 30 m diepte (4,0 bar) stijgt naar het oppervlak (1,0 bar). Hoe groot wordt hij bij gelijke temperatuur?",
        ["4,0 cm³", "0,25 cm³", "1,0 cm³", "30 cm³"],
        0,
        "p · V constant: vier keer minder druk, vier keer meer volume.",
    ),
    casus(
        "Een weerballon bevat 2,0 L gas bij 100 kPa en 27 °C. Hoog in de lucht is de druk 50 kPa en de temperatuur −33 °C.",
        [
            keuze(
                "Alleen door de lagere druk zou het volume [[*groter|kleiner]] worden.",
                "p · V constant: minder druk, meer volume.",
            ),
            keuze(
                "Alleen door de lagere temperatuur zou het volume [[groter|*kleiner]] worden.",
                "V / T constant bij gelijke druk.",
            ),
            inv(
                "Welk volume heeft de ballon hoog in de lucht, in L?",
                ["3,2", "3,2 L", "3.2"],
                "300 K en 240 K: V₂ = 2,0 · (100 / 50) · (240 / 300) = 3,2 L.",
            ),
        ],
    ),
    tabel(
        "Welk soort proces is dit ongeveer?",
        [
            ("een ballon zet uit als hij in de zon ligt", "Isobaar"),
            ("een gesloten spuitbus warmt op", "Isochoor"),
            ("je duwt langzaam een fietspomp in met de opening dicht", "Isotherm"),
        ],
        "Kijk welke grootheid gelijk blijft: p, V of T.",
        kolommen=["Isotherm", "Isobaar", "Isochoor"],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("In de gaswetten mag je de temperatuur in °C invullen.", F),
            ("Een reëel gas gedraagt zich het meest ideaal bij hoge druk en lage temperatuur.", F),
            ("Gelijke volumes gas bij dezelfde p en T bevatten evenveel deeltjes.", J),
            ("Meer gas in een vat bij gelijke V en T geeft een hogere druk.", J),
        ],
        "Altijd in kelvin; ideaal gedrag bij lage druk en hoge temperatuur.",
    ),
    koppel(
        "Koppel elk proces aan de grootheid die gelijk blijft.",
        [
            ("isotherm", "de temperatuur"),
            ("isobaar", "de druk"),
            ("isochoor", "het volume"),
        ],
        ["de massa per deeltje"],
        "Iso betekent gelijk.",
    ),
    sorteer(
        "Stijgt of daalt de druk van het gas?",
        ["Stijgt", "Daalt"],
        [
            ("je verwarmt het gas in een gesloten vat", "Stijgt"),
            ("je trekt de zuiger uit bij gelijke temperatuur", "Daalt"),
            ("je pompt extra gas in het vat", "Stijgt"),
            ("je koelt het gesloten vat af", "Daalt"),
        ],
        "Meer of hardere botsingen tegen de wand geven meer druk.",
    ),
    volgorde(
        "Zet de stappen om een vraag met de algemene gaswet op te lossen in volgorde.",
        [
            "Alle temperaturen omzetten naar kelvin",
            "De gegevens van toestand 1 en 2 noteren",
            "p₁ · V₁ / T₁ = p₂ · V₂ / T₂ opschrijven",
            "Oplossen naar de onbekende",
        ],
        "Druk en volume mogen in dezelfde eenheid links en rechts staan.",
    ),
    mk(
        "Waarom wijkt een reëel gas bij hoge druk af van de ideale gaswet?",
        [
            "De deeltjes hebben dan merkbaar volume",
            "De deeltjes bewegen dan helemaal niet meer",
            "Bij hoge druk is de temperatuur altijd nul kelvin",
            "De gasconstante R is dan een ander getal",
        ],
        0,
        "Dicht opeen tellen hun eigen volume en hun onderlinge aantrekking wel mee.",
    ),
    keuze(
        "De temperatuur van een gas is een maat voor de gemiddelde [[*kinetische energie|massa|lading]] van zijn deeltjes.",
        "Verwarmen betekent dat de deeltjes sneller bewegen.",
    ),
    sleep(
        "Bij een [[isotherm]] proces blijft p · V gelijk. In de ideale gaswet p · V = n · R · T is R de [[gasconstante]]. Temperaturen vul je in in [[kelvin]].",
        ["graden celsius", "isochoor"],
        "R = 8,31 J/(mol·K).",
    ),
    open_(
        "Leg met het deeltjesmodel uit waarom een spuitbus kan ontploffen als hij in de zon ligt.",
        "In de zon warmt het gas op en bewegen de deeltjes sneller. Het volume van de bus blijft gelijk, dus botsen de deeltjes vaker en harder tegen de wand. De druk stijgt recht evenredig met de temperatuur in kelvin, tot de wand het niet meer houdt.",
    ),
]

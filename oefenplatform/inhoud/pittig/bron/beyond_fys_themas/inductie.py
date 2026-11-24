"""Elektromagnetische inductie — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Flux in de tijd ------------------------------------------------------------------
FT = Prent("flux-tijd", "De flux door een spoel van 100 windingen", "grafiek van de flux in mWb tegen de tijd in s: A stijgt van 0 naar 4 tussen 0 en 0,2 s, B blijft 4 tot 0,5 s, C daalt naar 0 tussen 0,5 en 0,6 s, D stijgt langzaam naar 2 tussen 0,6 en 1,0 s")
X, Y = assen(FT, 0, 1.0, 0, 5, "t (s)", "Φ (mWb)", 0.1, 1, links=130, rechts=900)
PTS = [(0, 0), (0.2, 4), (0.5, 4), (0.6, 0), (1.0, 2)]
FT.pad("M " + " L ".join(f"{X(t):.1f} {Y(f):.1f}" for t, f in PTS), "none", BLAUW, 4)
SEG = {"A": (0.1, 2, -36, -10), "B": (0.35, 4, 0, -34), "C": (0.55, 2, 36, -6), "D": (0.8, 1, -10, -36)}
for k, (t, f, dx, dy) in SEG.items():
    FT.letter(X(t) + dx, Y(f) + dy, k)
ZF = {
    k: [Prent.zone(X(a) - 6, Y(max(fa, fb)) - 16, X(b) - X(a) + 12, abs(Y(fa) - Y(fb)) + 32), Prent.rond(X(SEG[k][0]) + SEG[k][2], Y(SEG[k][1]) + SEG[k][3], 24)]
    for k, ((a, fa), (b, fb)) in zip("ABCD", zip(PTS, PTS[1:]))
}

# Magneet naar een spoel ---------------------------------------------------------
MS = Prent("magneet-naar-spoel", "Een magneet beweegt met zijn noordpool naar een gesloten spoel", "links een staafmagneet met de noordpool rechts, een pijl naar rechts; rechts een spoel met de uiteinden X (naar de magneet) en Y, aangesloten op een stroommeter")
MS.rect(80, 300, 120, 60, BLAUW, DONKER, 4, 2)
MS.rect(200, 300, 120, 60, ROOD, DONKER, 4, 2)
MS.tekst(140, 340, "Z", 26, kleur="#ffffff", vet=True)
MS.tekst(260, 340, "N", 26, kleur="#ffffff", vet=True)
MS.pijl(150, 260, 290, 260, DONKER, 4)
MS.tekst(220, 240, "beweging", 18)
for x in range(500, 761, 32):
    MS.ellips(x, 330, 18, 80, "none", "#b5b5b5", 2)
    MS.pad(f"M {x} 250 A 18 80 0 0 1 {x} 410", "none", DONKER, 3)
MS.lijn(500, 410, 500, 520, DONKER, 3)
MS.lijn(756, 250, 756, 180, DONKER, 3)
MS.lijn(756, 180, 900, 180, DONKER, 3)
MS.lijn(900, 180, 900, 470, DONKER, 3)
MS.lijn(500, 520, 900, 520, DONKER, 3)
MS.cirkel(900, 470, 34, "#ffffff", DONKER, 3)
MS.tekst(900, 480, "A", 26, vet=True)
MS.lijn(900, 504, 900, 520, DONKER, 3)
MS.letter(440, 330, "X")
MS.letter(820, 330, "Y")
ZMX = [Prent.rond(440, 330, 30)]
ZMY = [Prent.rond(820, 330, 30)]

VRAGEN = [
    klik(
        "Klik op het stuk van de grafiek waar de inductiespanning het grootst is.",
        FT.bestand, ZF["C"],
        "U = −N · ΔΦ / Δt: daar verandert de flux het snelst (4 mWb in 0,1 s).",
    ),
    klik(
        "Klik op het stuk waar er geen inductiespanning is.",
        FT.bestand, ZF["B"],
        "De flux blijft gelijk, dus ΔΦ = 0.",
    ),
    met_prent(FT.bestand, inv(
        "Hoe groot is de inductiespanning in stuk A, in volt (zonder teken)?",
        ["2", "2,0", "2 V", "2,0 V"],
        "N · ΔΦ / Δt = 100 · 0,0040 Wb / 0,20 s = 2,0 V.",
    )),
    met_prent(FT.bestand, inv(
        "Hoe groot is de inductiespanning in stuk C, in volt (zonder teken)?",
        ["4", "4,0", "4 V", "4,0 V"],
        "100 · 0,0040 Wb / 0,10 s = 4,0 V.",
    )),
    met_prent(FT.bestand, tabel(
        "Hoe groot is de inductiespanning in dit stuk (zonder teken)?",
        [
            ("A", "2,0 V"),
            ("B", "0 V"),
            ("D", "0,5 V"),
        ],
        "In D: 100 · 0,0020 / 0,40 = 0,5 V.",
        kolommen=["0 V", "0,5 V", "2,0 V"],
    )),
    met_prent(FT.bestand, keuze(
        "De spanning in stuk A en die in stuk C hebben [[*een tegengesteld|hetzelfde]] teken.",
        "In A stijgt de flux, in C daalt ze.",
    )),
    klik(
        "Klik op het uiteinde van de spoel dat tijdens de beweging een noordpool wordt.",
        MS.bestand, ZMX,
        "Wet van Lenz: de spoel werkt de nadering tegen en duwt met een noordpool terug.",
    ),
    met_prent(MS.bestand, mk(
        "Je trekt de magneet weer weg. Wat doet de spoel dan?",
        [
            "X wordt een zuidpool en trekt terug",
            "X blijft een noordpool en duwt verder",
            "Er loopt geen stroom meer, ook niet even",
            "Y wordt een noordpool die de magneet aantrekt",
        ],
        0,
        "De spoel werkt nu het weggaan tegen.",
    )),
    met_prent(MS.bestand, tabel(
        "Wat doet de naald van de stroommeter?",
        [
            ("je duwt de magneet sneller in de spoel", "Grotere uitwijking"),
            ("de magneet ligt stil in de spoel", "Geen uitwijking"),
            ("je duwt de zuidpool in plaats van de noordpool erin", "Andere kant"),
        ],
        "Alleen een verandering van flux wekt spanning op; sneller is meer.",
        kolommen=["Grotere uitwijking", "Geen uitwijking", "Andere kant"],
    )),
    met_prent(MS.bestand, keuze(
        "Knip je de draad naar de meter door, dan voel je bij het induwen [[*geen|wel een]] tegenkracht.",
        "Zonder gesloten kring loopt er geen inductiestroom, en dan is er ook geen tegenwerkende pool.",
    )),
    inv(
        "Een winding van 0,050 m² staat in een veld van 0,40 T; de normaal maakt 60° met het veld. Hoe groot is Φ, in mWb? (cos 60° = 0,50)",
        ["10", "10 mWb"],
        "Φ = B · A · cos α = 0,40 · 0,050 · 0,50 = 0,010 Wb.",
    ),
    inv(
        "Een spoel van 500 windingen: de flux daalt in 0,020 s van 6,0 mWb naar 0. Hoe groot is de inductiespanning, in volt (zonder teken)?",
        ["150", "150 V"],
        "500 · 0,0060 / 0,020 = 150 V.",
    ),
    inv(
        "Hoeveel windingen heeft een spoel nodig om 6,0 V te leveren als de flux met 0,030 Wb per seconde verandert?",
        ["200"],
        "N = U / (ΔΦ / Δt) = 6,0 / 0,030 = 200.",
    ),
    mk(
        "Een winding staat loodrecht op het veld en draait een kwartslag tot ze evenwijdig met de veldlijnen ligt. Wat gebeurt er met Φ?",
        ["Van B · A naar 0", "Van 0 naar B · A", "Ze blijft B · A", "Van B · A naar 2 · B · A"],
        0,
        "Evenwijdig met de veldlijnen gaat er geen enkele veldlijn meer door de winding.",
    ),
    inv(
        "Een transformator heeft 1000 windingen primair en 50 secundair. Welke spanning geeft hij bij 230 V, in volt?",
        ["11,5", "11,5 V", "11.5"],
        "U₂ / U₁ = N₂ / N₁: 230 · 50 / 1000 = 11,5 V.",
    ),
    mk(
        "Een transformator met 1150 windingen primair moet 12 V maken uit 230 V. Hoeveel windingen heeft de secundaire spoel?",
        ["60", "22", "96", "600"],
        0,
        "N₂ = N₁ · U₂ / U₁ = 1150 · 12 / 230 = 60.",
    ),
    inv(
        "Een ideale transformator maakt 12 V uit 240 V. De secundaire stroom is 2,0 A. Hoe groot is de primaire stroom, in ampère?",
        ["0,1", "0,10", "0,1 A", "0,10 A", "0.1"],
        "U₁ · I₁ = U₂ · I₂: I₁ = 12 · 2,0 / 240 = 0,10 A.",
    ),
    mk(
        "Hoeveel keer kleiner is de stroom in een lijn op 400 kV dan op 10 kV, bij hetzelfde vermogen?",
        ["40 keer", "4 keer", "390 keer", "1600 keer"],
        0,
        "P = U · I: bij 40 keer de spanning is de stroom 40 keer kleiner.",
    ),
    keuze(
        "Een optransformator heeft secundair [[*meer|minder]] windingen dan primair.",
        "U₂ / U₁ = N₂ / N₁.",
    ),
    casus(
        "Een rechthoekige winding draait met een vaste snelheid rond in een homogeen magnetisch veld.",
        [
            mk(
                "Op welk ogenblik is de inductiespanning nul?",
                [
                    "Als het vlak loodrecht op het veld staat",
                    "Als het vlak evenwijdig met het veld ligt",
                    "Altijd, want het veld is homogeen",
                    "Nooit, want de winding draait altijd",
                ],
                0,
                "Dan is Φ maximaal en verandert ze even niet.",
            ),
            mk(
                "Op welk ogenblik is de inductiespanning het grootst?",
                [
                    "Als het vlak evenwijdig met het veld ligt",
                    "Als het vlak precies loodrecht op het veld staat",
                    "Halverwege, als het vlak onder 45° met het veld staat",
                    "Op elk ogenblik van de toer is ze even groot",
                ],
                0,
                "Dan is Φ nul, maar verandert ze het snelst.",
            ),
            keuze(
                "Draait de winding twee keer zo snel, dan wordt de spanning [[*groter en wisselt ze sneller|alleen sneller wisselend]].",
                "De flux verandert dan in de helft van de tijd evenveel.",
            ),
        ],
    ),
    sorteer(
        "Berust dit toestel op elektromagnetische inductie?",
        ["Inductie", "Geen inductie"],
        [
            ("een fietsdynamo", "Inductie"),
            ("een inductiekookplaat", "Inductie"),
            ("een gloeilamp", "Geen inductie"),
            ("een elektromagnetische rem", "Inductie"),
            ("een batterij", "Geen inductie"),
        ],
        "Inductie vraagt altijd een veranderende flux.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een transformator werkt ook op een batterij.", F),
            ("De kern van een transformator bestaat uit geïsoleerde plaatjes tegen wervelstromen.", J),
            ("Een spoel zonder gesloten kring krijgt geen inductiespanning.", F),
            ("Een inductiekookplaat warmt de pan op via wervelstromen in de pan zelf.", J),
        ],
        "Zonder gesloten kring is er wel spanning, maar geen stroom.",
    ),
    koppel(
        "Koppel elk toestel aan hoe het inductie gebruikt.",
        [
            ("pick-up van een elektrische gitaar", "een trillende snaar verandert de flux"),
            ("detectielus in het wegdek", "het metaal van een wagen verandert de flux"),
            ("draadloze oplader", "een spoel in de lader wekt stroom op in de telefoon"),
            ("elektromagnetische rem", "wervelstromen werken het draaien tegen"),
        ],
        ["een batterij levert gelijkspanning"],
        "Telkens verandert de flux door een spoel of een stuk metaal.",
    ),
    volgorde(
        "Zet in volgorde hoe een fietsdynamo het lampje doet branden.",
        [
            "Het wiel draait het dopje van de dynamo rond",
            "De magneet in de dynamo draait",
            "De flux door de spoel verandert",
            "Er ontstaat een inductiespanning",
            "Er loopt stroom door het lampje",
        ],
        "Hoe sneller je fietst, hoe sneller de flux verandert.",
    ),
    mk(
        "Wat zou er gebeuren als een inductiestroom zijn oorzaak versterkte in plaats van tegenwerkte?",
        [
            "Je kreeg energie uit het niets",
            "Er zou nooit nog een stroom lopen",
            "De magneet zou meteen ophouden met werken",
            "De spanning zou altijd precies nul blijven",
        ],
        0,
        "Daarom volgt de wet van Lenz uit het behoud van energie.",
    ),
    mk(
        "Een koperen plaat valt tussen de polen van een sterke magneet en vertraagt. Waarom?",
        [
            "Wervelstromen werken de beweging tegen",
            "De magneet trekt het koper sterk aan",
            "Het koper wordt elektrisch geladen door de lucht",
            "Koper is ferromagnetisch en blijft dus kleven",
        ],
        0,
        "Koper is niet ferromagnetisch; de remming komt van de inductiestromen.",
    ),
    sleep(
        "De flux Φ = B · A · cos α druk je uit in [[weber]]. Een inductiespanning ontstaat alleen bij een [[verandering]] van de flux. De inductiestroom werkt zijn oorzaak [[tegen]].",
        ["tesla", "versterkt"],
        "Faraday geeft de grootte, Lenz de zin.",
    ),
    open_(
        "Leg uit waarom een transformator niet werkt op gelijkspanning.",
        "Bij gelijkspanning loopt er een constante stroom door de primaire spoel, dus is het veld in de kern constant. De flux door de secundaire spoel verandert dan niet, en zonder fluxverandering is er geen inductiespanning.",
    ),
]

"""Voortplanting en de hormonale regeling — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Hormonen en temperatuur tijdens de cyclus -------------------------------
def X(d):
    return 110 + (d - 1) * 26
def Y(h):                      # hormoonpaneel: 0..100 -> 410..90
    return 410 - h * 3.2
def T(t):                      # temperatuurpaneel: 36,4..37,0 -> 590..470
    return 590 - (t - 36.4) * 200
CYC = Prent("cyclus-hormonen", "Hormonen en lichaamstemperatuur tijdens één cyclus", "grafiek van FSH, LH, oestrogeen en progesteron over 28 dagen, met de basistemperatuur eronder")
CYC.lijn(X(1), 410, X(28), 410, DONKER, 2)
CYC.lijn(X(1), 590, X(28), 590, DONKER, 2)
CYC.lijn(X(1), 90, X(1), 410, DONKER, 2)
CYC.lijn(X(1), 460, X(1), 590, DONKER, 2)
for d in (1, 7, 14, 21, 28):
    CYC.tekst(X(d), 612, f"dag {d}", 15)
CYC.tekst(X(1) - 8, 82, "hormoongehalte", 15, "start")
CYC.tekst(X(1) - 8, 452, "temperatuur (°C)", 15, "start")
for t in (36.5, 36.9):
    CYC.tekst(X(1) - 10, T(t) + 5, f"{t}".replace(".", ","), 14, "end")
LIJNEN = {
    "FSH": (BLAUW, [(1, 18), (4, 28), (8, 16), (12, 18), (14, 38), (16, 14), (22, 10), (28, 16)]),
    "LH": (ORANJE, [(1, 12), (10, 14), (12.5, 30), (14, 95), (15.5, 25), (18, 12), (28, 12)]),
    "oestrogeen": (PAARS, [(1, 10), (6, 18), (10, 45), (13, 62), (15, 30), (18, 32), (21, 40), (25, 25), (28, 12)]),
    "progesteron": (GROEN, [(1, 5), (13, 6), (15, 14), (18, 50), (21, 66), (24, 50), (27, 12), (28, 6)]),
}
for i, (naam, (kleur, pts)) in enumerate(LIJNEN.items()):
    CYC.pad("M" + " L ".join(f"{X(d):.1f} {Y(h):.1f}" for d, h in pts), "none", kleur, 4)
    CYC.lijn(X(28) + 25, 120 + i * 34, X(28) + 55, 120 + i * 34, kleur, 5)
    CYC.tekst(X(28) + 62, 126 + i * 34, naam, 16, "start")
temp = [(1, 36.55), (13, 36.5), (14, 36.45), (15, 36.75), (16, 36.85), (26, 36.85), (28, 36.55)]
CYC.pad("M" + " L ".join(f"{X(d):.1f} {T(t):.1f}" for d, t in temp), "none", ROOD, 4)
Z_LHPIEK = Prent.zone(X(13), Y(100), X(15) - X(13), Y(60) - Y(100))
Z_PROGTOP = Prent.zone(X(19), Y(72), X(23) - X(19), Y(55) - Y(72))
Z_OESTTOP = Prent.zone(X(11.5), Y(70), X(14) - X(11.5), Y(54) - Y(70))
Z_TSPRONG = Prent.zone(X(13.5), T(36.95), X(16) - X(13.5), T(36.4) - T(36.95))
Z_FSHBEGIN = Prent.zone(X(2), Y(35), X(6.5) - X(2), Y(20) - Y(35))

# Het vrouwelijk stelsel, zonder namen -----------------------------------
VR = Prent("vrouwelijk-stelsel", "Het vrouwelijk voortplantingsstelsel, vooraanzicht", "schema met eierstokken, eitrechters, eileiders, baarmoeder en vagina")
VR.pad("M420 220 Q 500 200 580 220 L 560 400 Q 500 430 440 400 Z", "#f3c9c0")       # baarmoeder
VR.pad("M420 235 Q 330 180 250 250", "none", "#c97a6c", 14)                         # eileider links
VR.pad("M580 235 Q 670 180 750 250", "none", "#c97a6c", 14)                         # eileider rechts
VR.pad("M250 250 l -40 -10 M250 250 l -45 15 M250 250 l -30 35 M250 250 l -5 40", "none", "#c97a6c", 6)
VR.pad("M750 250 l 40 -10 M750 250 l 45 15 M750 250 l 30 35 M750 250 l 5 40", "none", "#c97a6c", 6)
VR.ellips(270, 330, 45, 28, "#f7e2b0")
VR.ellips(730, 330, 45, 28, "#f7e2b0")
VR.rect(475, 415, 50, 130, "#f3c9c0", DONKER, 10)                                    # vagina
Z_EIERSTOK = [Prent.rond(270, 330, 48), Prent.rond(730, 330, 48)]
Z_EILEIDER = [Prent.zone(300, 180, 115, 60), Prent.zone(585, 180, 115, 60)]
Z_TRECHTER = [Prent.zone(195, 222, 70, 62), Prent.zone(735, 222, 70, 62)]
Z_BAARMOEDER = Prent.zone(425, 215, 150, 200)

VRAGEN = [
    klik(
        "Klik op de plek waar een eicel rijpt in een follikel.",
        VR.bestand, Z_EIERSTOK,
        "De follikel met de rijpende eicel ligt in de eierstok.",
    ),
    klik(
        "Klik op de plek waar de bevruchting normaal gebeurt.",
        VR.bestand, Z_EILEIDER,
        "De zaadcel bereikt de eicel meestal in het bovenste deel van de eileider.",
    ),
    klik(
        "Klik op het deel dat de eicel na de eisprong opvangt.",
        VR.bestand, Z_TRECHTER,
        "De eitrechter vangt de eicel op. Niet de baarmoeder.",
    ),
    klik(
        "Klik op het orgaan waarin een bevruchte eicel zich nestelt.",
        VR.bestand, [Z_BAARMOEDER],
        "De bevruchte eicel nestelt zich in het baarmoederslijmvlies.",
    ),
    klik(
        "Klik op de piek die de eisprong uitlokt.",
        CYC.bestand, [Z_LHPIEK],
        "Rond dag 14 schiet LH omhoog. Die piek laat de rijpe follikel openbarsten.",
    ),
    klik(
        "Klik op de top van het hormoon dat het geel lichaam vooral maakt.",
        CYC.bestand, [Z_PROGTOP],
        "Het geel lichaam maakt vooral progesteron, met een top rond dag 21.",
    ),
    klik(
        "Klik op de plek waar je achteraf kan zien dat de eisprong geweest is.",
        CYC.bestand, [Z_TSPRONG],
        "Progesteron laat de basistemperatuur een paar tienden van een graad stijgen.",
    ),
    klik(
        "Klik op de top van het hormoon dat het baarmoederslijmvlies in de eerste helft laat aangroeien.",
        CYC.bestand, [Z_OESTTOP],
        "Oestrogeen uit de eierstok bouwt het slijmvlies op en helpt de LH-piek uitlokken.",
    ),
    klik(
        "Klik op het stuk van een curve dat in het begin van de cyclus een follikel laat rijpen.",
        CYC.bestand, [Z_FSHBEGIN],
        "FSH, het follikelstimulerend hormoon, zet de rijping in gang.",
    ),
    met_prent(CYC.bestand, tabel(
        "Kijk naar de grafiek van de hormonen. Klopt dit?",
        [
            ("Op het einde van de cyclus daalt het progesteron.", J),
            ("De temperatuur ligt in de tweede helft hoger.", J),
            ("LH blijft de hele cyclus even hoog.", F),
            ("Na dag 14 vormt de follikel het geel lichaam.", J),
            ("Progesteron piekt al voor de eisprong.", F),
        ],
        "Valt het geel lichaam weg, dan daalt het progesteron en volgt de menstruatie.",
    )),
    volgorde(
        "Zet de gebeurtenissen van één cyclus zonder bevruchting in de juiste volgorde.",
        [
            "Menstruatie",
            "Een follikel rijpt onder invloed van FSH",
            "Eisprong na de LH-piek",
            "Het geel lichaam maakt progesteron",
            "Het geel lichaam valt weg",
        ],
        "Zonder bevruchting verdwijnt het geel lichaam na een tiental dagen.",
    ),
    sorteer(
        "Hoort dit bij het vrouwelijk of het mannelijk stelsel?",
        ["Vrouwelijk", "Mannelijk"],
        [
            ["de eitrechter", "Vrouwelijk"],
            ["de baarmoeder", "Vrouwelijk"],
            ["de follikel", "Vrouwelijk"],
            ["de bijbal", "Mannelijk"],
            ["de zaadleider", "Mannelijk"],
            ["de cellen van Leydig", "Mannelijk"],
        ],
        "De cellen van Leydig liggen tussen de zaadbuisjes in de teelbal.",
    ),
    koppel(
        "Koppel elk hormoon aan de plaats waar het gemaakt wordt.",
        [
            ("GnRH", "hypothalamus"),
            ("FSH", "hypofyse"),
            ("oestrogeen", "eierstok"),
            ("testosteron", "cellen van Leydig"),
            ("inhibine", "cellen van Sertoli"),
        ],
        ["schildklier"],
        "De schildklier staat buiten de regeling van de voortplanting.",
    ),
    casus(
        "Een schema van de man toont: hypothalamus → GnRH → hypofyse → LH → cellen van Leydig → testosteron. Van testosteron loopt een pijl met een minteken terug naar de hypothalamus en de hypofyse.",
        [
            mk(
                "Wat betekent het minteken op die pijl?",
                [
                    "Testosteron remt de hypothalamus en de hypofyse",
                    "Testosteron stimuleert de hypofyse om meer LH te maken",
                    "De hypofyse maakt testosteron als er te weinig is",
                    "Er komt geen testosteron in het bloed terecht",
                ],
                0,
                "Een minteken staat voor een remmende invloed.",
            ),
            tabel(
                "Wat gebeurt er als het testosterongehalte te hoog wordt?",
                [
                    ("De hypothalamus geeft minder GnRH af.", J),
                    ("De hypofyse geeft minder LH af.", J),
                    ("De cellen van Leydig maken daarna meer testosteron.", F),
                ],
                "Zo daalt het gehalte weer: een feedbacksysteem.",
            ),
            keuze(
                "Bij de man werkt FSH vooral op de [[*cellen van Sertoli|cellen van Leydig|bijbal]].",
                "LH zet de cellen van Leydig aan, FSH werkt vooral op de cellen van Sertoli.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over man en vrouw?",
        [
            ("GnRH, FSH en LH komen bij beide geslachten voor.", J),
            ("De man maakt doorlopend zaadcellen, zonder cyclus.", J),
            ("Progesteron is het belangrijkste mannelijke hormoon.", F),
            ("De hypofyse ligt onderaan de hersenen, vlak bij de hypothalamus.", J),
            ("Inhibine zet de hypofyse aan om meer FSH te maken.", F),
        ],
        "Testosteron is het belangrijkste mannelijke geslachtshormoon. Inhibine remt.",
    ),
    mk(
        "Waarom liggen de teelballen in de balzak, buiten de buikholte?",
        [
            "Zaadcellen vormen zich beter iets koeler",
            "Zo kunnen ze makkelijker testosteron uitscheiden",
            "In de buikholte is er geen plaats voor zaadbuisjes",
            "Zo komen de zaadcellen sneller in de bijbal terecht",
        ],
        0,
        "In de balzak ligt de temperatuur een paar graden lager.",
    ),
    tabel(
        "Eicel of zaadcel?",
        [
            ("groot, met een voorraad voedingsstoffen", "Eicel"),
            ("beweegt met een zweepstaart", "Zaadcel"),
            ("rijpt in een follikel", "Eicel"),
            ("wordt beweeglijk in de bijbal", "Zaadcel"),
        ],
        "Een zaadcel is bijna niets anders dan een kern met een staart.",
        kolommen=["Eicel", "Zaadcel"],
    ),
    sleep(
        "Bij de [[bevruchting]] versmelten de kernen van een zaadcel en een eicel tot een [[zygote]]. Die deelt terwijl ze door de [[eileider]] naar de baarmoeder reist.",
        ["eierstok", "follikel", "bijbal"],
        "De zygote is de eerste cel van een nieuw organisme.",
    ),
    mk(
        "Waarom ligt de vruchtbare periode in de dagen rond de eisprong, en niet enkel op die ene dag?",
        [
            "Zaadcellen overleven enkele dagen in het lichaam",
            "De eicel overleeft ongeveer een maand in de eileider",
            "Er komen telkens verschillende eicellen na elkaar vrij",
            "De eisprong duurt zelf ongeveer een volle week lang",
        ],
        0,
        "Zaadcellen overleven enkele dagen, de eicel ongeveer een dag.",
    ),
    keuze(
        "Vlak voor de eisprong werkt oestrogeen [[*stimulerend|remmend|niet]] op de hypofyse, en dat geeft de LH-piek.",
        "Een feedbacksysteem kan zowel remmen als stimuleren.",
    ),
    tabel(
        "Klopt dit over testosteron?",
        [
            ("Het zorgt voor de baardgroei in de puberteit.", J),
            ("Het maakt de stem zwaarder.", J),
            ("Het wordt in de bijbal gemaakt.", F),
            ("Het remt bij een te hoog gehalte de hypofyse.", J),
        ],
        "Testosteron komt uit de cellen van Leydig in de teelbal.",
    ),
    mk(
        "Een jongen vraagt waar zijn zaadcellen precies ontstaan. Wat antwoord je?",
        ["In de teelbal", "In de bijbal, waar ze ook rijpen", "In de zaadleider naar buiten", "In de hypofyse onder de hersenen"],
        0,
        "De bijbal laat de zaadcellen daarna rijpen en bewaart ze.",
    ),
    tabel(
        "Klopt dit over het geel lichaam?",
        [
            ("Het ontstaat uit de lege follikel.", J),
            ("Het maakt vooral progesteron.", J),
            ("Het ligt in de baarmoeder.", F),
            ("Zonder bevruchting valt het na een tiental dagen weg.", J),
            ("Het vangt de eicel op na de eisprong.", F),
        ],
        "Het geel lichaam ligt in de eierstok. De eitrechter vangt de eicel op.",
    ),
    keuze(
        "Dag 1 van de cyclus is de eerste dag van [[*de menstruatie|de eisprong|de LH-piek]].",
        "Een gemiddelde cyclus duurt ongeveer 28 dagen.",
    ),
    koppel(
        "Koppel elk deel van het mannelijk stelsel aan zijn taak.",
        [
            ("teelbal", "zaadcellen vormen"),
            ("bijbal", "zaadcellen laten rijpen en bewaren"),
            ("zaadleider", "zaadcellen naar buiten voeren"),
            ("cellen van Sertoli", "rijpende zaadcellen voeden"),
        ],
        ["eicel opvangen"],
        "De eitrechter vangt de eicel op, bij de vrouw.",
    ),
    tabel(
        "Remt of stimuleert dit hormoon?",
        [
            ("inhibine op de hypofyse", "Remt"),
            ("GnRH op de hypofyse", "Stimuleert"),
            ("testosteron bij een te hoog gehalte op de hypofyse", "Remt"),
            ("LH op de cellen van Leydig", "Stimuleert"),
        ],
        "Een feedbacksysteem houdt de gehaltes zo binnen grenzen.",
        kolommen=["Remt", "Stimuleert"],
    ),
    mk(
        "Een eicel komt vrij maar wordt niet bevrucht. Wat gebeurt er met het baarmoederslijmvlies?",
        [
            "Het laat los en wordt afgevoerd",
            "Het blijft maandenlang dik staan",
            "Het verhuist naar de eileider",
            "Het wordt omgebouwd tot een follikel",
        ],
        0,
        "Zonder progesteron laat het slijmvlies los. Dat is de menstruatie.",
    ),
    open_(
        "Leg uit waarom de menstruatie begint als de eicel niet bevrucht wordt. Gebruik de woorden geel lichaam, progesteron en baarmoederslijmvlies.",
        "Zonder bevruchting valt het geel lichaam na een tiental dagen weg. Daardoor daalt het progesteron. Zonder progesteron kan het dikke baarmoederslijmvlies niet in stand blijven: de bovenste lagen sterven af en worden met bloed afgevoerd. Dat is de menstruatie.",
    ),
]

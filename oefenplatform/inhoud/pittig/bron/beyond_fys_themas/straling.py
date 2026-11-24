"""Kernenergie en ioniserende straling — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Drie stralen in een magnetisch veld ------------------------------------------------
MV = Prent("stralen-magneetveld", "Straling uit een bron vliegt door een magnetisch veld", "een loden blok met bron links; een veld dat het blad in wijst (kruisjes); drie banen naar rechts: A buigt licht naar boven, B gaat rechtdoor, C buigt sterk naar beneden")
for i in range(8):
    for j in range(5):
        x, y = 330 + i * 80, 130 + j * 90
        MV.tekst(x, y + 8, "×", 26, kleur=GRIJS)
MV.tekst(650, 92, "magnetisch veld het blad in", 18)
MV.rect(70, 270, 130, 100, "#6b6f76", DONKER, 8, 2)
MV.cirkel(190, 320, 10, GEEL, DONKER, 2)
MV.lijn(200, 320, 280, 320, DONKER, 3)
MV.pad("M 280 320 Q 600 300 920 200", "none", ROOD, 4)
MV.lijn(280, 320, 920, 320, ORANJE, 4)
MV.pad("M 280 320 Q 430 340 520 560", "none", BLAUW, 4)
LMV = {"A": (920, 170), "B": (940, 290), "C": (545, 575)}
for k, p in LMV.items():
    MV.letter(*p, k)
ZMV = {"A": [Prent.rond(760, 255, 40), Prent.rond(*LMV["A"], 24)], "B": [Prent.rond(760, 320, 30), Prent.rond(*LMV["B"], 24)], "C": [Prent.rond(470, 440, 40), Prent.rond(*LMV["C"], 24)]}

# Doordringend vermogen ---------------------------------------------------------------
DV = Prent("doordringend", "Drie soorten straling vliegen op drie schermen af", "links een bron; drie stralen A, B en C naar rechts; een blad papier, een plaatje aluminium van enkele mm en een dikke loden plaat; straal A stopt in de loden plaat (zwakker erachter), straal B stopt in het aluminium, straal C stopt aan het papier")
DV.cirkel(100, 330, 30, GEEL, DONKER, 2)
DV.tekst(100, 390, "bron", 18)
SCH = [("papier", 360, 6, "#f4efe0"), ("aluminium", 560, 24, "#c9ccd1"), ("lood", 770, 70, "#6b6f76")]
for naam, x, b, kl in SCH:
    DV.rect(x, 110, b, 440, kl, DONKER, 2, 2)
    DV.tekst(x + b / 2, 585, naam, 18, vet=True)
STRA = {"A": (230, 900, ROOD), "B": (330, 560, BLAUW), "C": (430, 360, ORANJE)}
for k, (y, x2, kl) in STRA.items():
    DV.lijn(130, 330 + (y - 330) * 0.1, 130 + 0, 330 + (y - 330) * 0.1, kl, 1)
    if k == "A":
        DV.pijl(160, y, 770, y, kl, 5)
        DV.lijn(840, y, 940, y, kl, 2, stippel=True)
    else:
        DV.pijl(160, y, x2, y, kl, 5)
    DV.letter(190, y - 28, k)
ZDV = {k: [Prent.zone(160, y - 22, x2 - 160, 44), Prent.rond(190, y - 28, 22)] for k, (y, x2, kl) in STRA.items()}

VRAGEN = [
    klik(
        "Klik op de baan van de alfastraling.",
        MV.bestand, ZMV["A"],
        "Positief geladen en zwaar: ze buigt naar de ene kant, maar weinig.",
    ),
    klik(
        "Klik op de baan van de bèta-min-straling.",
        MV.bestand, ZMV["C"],
        "Negatief geladen en heel licht: ze buigt sterk naar de andere kant.",
    ),
    met_prent(MV.bestand, mk(
        "Waarom gaat baan B rechtdoor?",
        ["Gammastraling heeft geen lading", "Gammastraling gaat te snel om af te buigen", "Gammastraling is te zwaar om af te buigen", "Het veld is in het midden van de bundel nul"],
        0,
        "Op een deeltje zonder lading werkt geen lorentzkracht.",
    )),
    met_prent(MV.bestand, keuze(
        "Keer je het veld om, dan buigt de alfastraling [[*naar beneden|nog steeds naar boven]].",
        "De lorentzkracht keert om met het veld.",
    )),
    klik(
        "Klik op de straling met het grootste ioniserend vermogen.",
        DV.bestand, ZDV["C"],
        "Alfastraling geeft haar energie op korte afstand af en raakt niet voorbij papier.",
    ),
    klik(
        "Klik op de bètastraling.",
        DV.bestand, ZDV["B"],
        "Bèta gaat door papier maar stopt in enkele mm aluminium.",
    ),
    met_prent(DV.bestand, tabel(
        "Welke straling is dit?",
        [
            ("A", "Gamma"),
            ("B", "Bèta"),
            ("C", "Alfa"),
        ],
        "Hoe kleiner het ioniserend vermogen, hoe groter het doordringend vermogen.",
        kolommen=["Alfa", "Bèta", "Gamma"],
    )),
    met_prent(DV.bestand, mk(
        "Een alfabron ligt op tafel. Wanneer is ze het gevaarlijkst?",
        ["Als je de stof inslikt of inademt", "Als je er op 1 m van staat", "Als je achter een blad papier staat", "Als je er een uur naast slaapt"],
        0,
        "Van buitenaf houdt je huid alfa tegen; binnenin raakt ze levend weefsel.",
    )),
    mk(
        "Hoeveel energie komt vrij als 2,0 g massa volledig in energie omgezet wordt? Neem c = 3,0 · 10⁸ m/s.",
        ["1,8 · 10¹⁴ J", "6,0 · 10⁵ J", "1,8 · 10¹⁷ J", "9,0 · 10¹³ J"],
        0,
        "E = m · c² = 0,0020 · 9,0 · 10¹⁶.",
    ),
    mk(
        "Een kern heeft een bindingsenergie van 1600 MeV en A = 200. Hoe groot is de specifieke bindingsenergie?",
        ["8,0 MeV", "320 000 MeV", "0,13 MeV", "1400 MeV"],
        0,
        "Eb / A = 1600 / 200.",
    ),
    keuze(
        "Kern X heeft 7,6 MeV per nucleon, kern Y 8,7 MeV per nucleon. Kern [[*Y|X]] is het stabielst.",
        "Een grotere specifieke bindingsenergie betekent stevigere nucleonen.",
    ),
    keuze(
        "Een losse kern weegt [[*minder dan|meer dan|evenveel als]] de som van zijn losse protonen en neutronen.",
        "Dat verschil is het massadefect.",
    ),
    inv(
        "Een persoon krijgt een geabsorbeerde dosis van 2,0 mGy alfastraling, met stralingsweegfactor 20. Hoe groot is de equivalente dosis, in mSv?",
        ["40", "40 mSv"],
        "H = wR · D = 20 · 2,0.",
    ),
    mk(
        "Een weefsel van 2,0 kg neemt 0,010 J stralingsenergie op. Hoe groot is de geabsorbeerde dosis?",
        ["5,0 mGy", "20 mGy", "0,020 Gy", "200 Gy"],
        0,
        "D = E / m = 0,010 / 2,0 = 0,0050 Gy.",
    ),
    casus(
        "In een kerncentrale splijt uranium-235 nadat het een neutron opvangt. Bij elke splijting komen twee of drie nieuwe neutronen vrij.",
        [
            mk(
                "Waarom kan zo een kettingreactie ontstaan?",
                ["Elke splijting levert neutronen voor nieuwe", "Het uranium wordt bij elke splijting warmer", "De regelstaven maken voortdurend extra neutronen", "Het koelwater splijt mee met het uranium"],
                0,
                "Eén splijting kan er zo meerdere veroorzaken.",
            ),
            keuze(
                "Om de reactor af te remmen schuift men de regelstaven [[*dieper|minder diep]] in de kern.",
                "Ze vangen neutronen weg.",
            ),
            keuze(
                "De splijtingsproducten hebben samen [[*een grotere|een kleinere]] specifieke bindingsenergie dan uranium.",
                "Daarom komt er energie vrij.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Doorstraald voedsel wordt zelf radioactief.", F),
            ("Bij besmetting zit de radioactieve stof op of in je lichaam.", J),
            ("De zon haalt haar energie uit kernsplijting.", F),
            ("Afstand houden verlaagt de dosis van een gammabron.", J),
        ],
        "De zon werkt met kernfusie van waterstof tot helium.",
    ),
    sorteer(
        "Is dit kernsplijting of kernfusie?",
        ["Kernsplijting", "Kernfusie"],
        [
            ("een gewone kerncentrale in België", "Kernsplijting"),
            ("de energie van de zon", "Kernfusie"),
            ("uranium-235 dat in twee stukken valt", "Kernsplijting"),
            ("twee waterstofkernen die helium vormen", "Kernfusie"),
        ],
        "Zware kernen splijten, lichte kernen versmelten.",
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("activiteit", "becquerel"),
            ("geabsorbeerde dosis", "gray"),
            ("equivalente dosis", "sievert"),
            ("bindingsenergie van een kern", "MeV"),
        ],
        ["candela"],
        "Gray is J/kg; sievert houdt ook rekening met de soort straling.",
    ),
    koppel(
        "Koppel elke maatregel aan het gevaar dat ze tegengaat.",
        [
            ("jodiumpil", "radioactief jodium in de schildklier"),
            ("loden schort bij een röntgenfoto", "bestraling van de rest van het lichaam"),
            ("handschoenen in een labo", "besmetting van de huid"),
            ("radonmeting in de kelder", "inademen van radongas"),
        ],
        ["kosmische straling in een vliegtuig"],
        "Afstand, tijd, afscherming en geen besmetting toelaten.",
    ),
    mk(
        "Welk radioactief afval komt in categorie C terecht?",
        ["Hoogactief, warmteproducerend afval", "Beschermkledij uit een ziekenhuis of labo", "Kortlevend laagactief en middelactief afval", "Gereedschap uit een labo"],
        0,
        "Daarvoor zoekt België nog een berging diep in de grond.",
    ),
    mk(
        "Waarom kiest men voor een PET-scan een stof met een korte halveringstijd?",
        ["Zo is de straling snel weer weg", "Zo is de stof een stuk goedkoper om te maken", "Zo zie je het orgaan langer op het scherm", "Zo dringt de straling dieper door in het lichaam"],
        0,
        "De dosis voor de patiënt blijft zo laag.",
    ),
    mk(
        "Hoe vermijd je best een inwendige besmetting in een labo met radioactieve stoffen?",
        ["Niet eten of drinken in het labo", "Snel werken en dan buiten gaan", "Een loden schort dragen", "Een dosismeter op je jas dragen"],
        0,
        "Inwendige besmetting komt van inslikken of inademen.",
    ),
    inv(
        "Een orgaan krijgt een equivalente dosis van 10 mSv. De weefselweegfactor is 0,12. Hoe groot is de bijdrage tot de effectieve dosis, in mSv?",
        ["1,2", "1,2 mSv"],
        "E = wT · H = 0,12 · 10.",
    ),
    keuze(
        "Een kerncentrale op kernfusie geeft [[*veel minder|veel meer]] langlevend afval dan een op kernsplijting.",
        "Fusie maakt vooral helium.",
    ),
    mk(
        "Waarom kan ioniserende straling kanker veroorzaken?",
        ["Ze kan het DNA in een cel beschadigen", "Ze maakt het weefsel radioactief", "Ze verwarmt het lichaam te sterk", "Ze haalt water uit de cellen"],
        0,
        "Een beschadigde cel kan muteren en ongeremd gaan delen.",
    ),
    volgorde(
        "Zet deze stralingen van groot naar klein ioniserend vermogen.",
        ["alfastraling", "bètastraling", "gammastraling"],
        "Het doordringend vermogen loopt net omgekeerd.",
    ),
    sleep(
        "Alfastraling stopt al bij een blad [[papier]], bètastraling bij enkele mm [[aluminium]], en gammastraling verzwak je met een dikke laag [[lood]].",
        ["glas", "plastic"],
        "Hoe groter het doordringend vermogen, hoe dikker de afscherming.",
    ),
    open_(
        "Leg het verschil uit tussen bestraling en besmetting, en zeg bij welk van de twee je zelf straling blijft geven.",
        "Bij bestraling sta je in de buurt van een bron en vangt je lichaam straling op, maar de radioactieve stof komt niet op of in je. Stap je weg, dan stopt het. Bij besmetting zit de radioactieve stof op je huid of in je lichaam. Dan blijf je bestraald worden en kan je zelf andere mensen bestralen tot de stof weg of vervallen is.",
    ),
]

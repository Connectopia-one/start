"""De filosofische domeinen — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_domeinen: antropologie, esthetica, ethiek,
kennisleer en logica, metafysica en natuurfilosofie, en vragen thuisbrengen.
Met zes zelfgetekende zinnebeelden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ORANJE, LICHTGROEN, GROEN, PAARS

ZD = Prent("zes-zinnebeelden-domeinen", "Zes zinnebeelden", "zes vakjes met een tekening, letters A tot F")
VAK = [("A", 60, 70), ("B", 370, 70), ("C", 680, 70), ("D", 60, 345), ("E", 370, 345), ("F", 680, 345)]
for t, x, y in VAK:
    ZD.rect(x, y, 260, 230, "#ffffff", DONKER, 14, 3)
    ZD.letter(x + 230, y + 200, t)
# A: weegschaal
ZD.lijn(190, 100, 190, 250, DONKER, 5); ZD.lijn(110, 130, 270, 130, DONKER, 5); ZD.rect(150, 245, 80, 12, GRIJS, DONKER, 3)
for cx in (110, 270):
    ZD.lijn(cx, 130, cx - 30, 190, DONKER, 2); ZD.lijn(cx, 130, cx + 30, 190, DONKER, 2)
    ZD.pad(f"M {cx-35} 190 Q {cx} 215 {cx+35} 190 Z", GEEL, DONKER, 2)
# B: schilderij in een lijst op een ezel
ZD.lijn(460, 270, 500, 110, DONKER, 4); ZD.lijn(540, 270, 500, 110, DONKER, 4)
ZD.rect(430, 110, 140, 110, "#c9a24a", DONKER, 4, 3); ZD.rect(445, 125, 110, 80, "#cfe3f0", DONKER, 0, 2)
ZD.cirkel(525, 150, 14, GEEL, DONKER, 1); ZD.pad("M 445 205 L 480 160 L 510 205 Z", LICHTGROEN, DONKER, 1)
# C: silhouet van een mens
ZD.cirkel(810, 120, 30, GRIJS, DONKER, 3); ZD.pad("M 760 260 Q 760 165 810 160 Q 860 165 860 260 Z", GRIJS, DONKER, 3)
# D: aarde met boom
ZD.cirkel(190, 460, 75, "#9ec7e6", DONKER, 3); ZD.pad("M 140 430 q 30 -20 50 5 q 20 25 -10 45 q -35 5 -40 -50 Z", LICHTGROEN, DONKER, 2)
ZD.pad("M 205 470 q 25 -15 40 5 q 0 30 -30 30 Z", LICHTGROEN, DONKER, 2)
# E: vergrootglas boven een redenering met pijlen
ZD.cirkel(450, 430, 22, "#ffffff", DONKER, 3); ZD.cirkel(545, 430, 22, "#ffffff", DONKER, 3)
ZD.pijl(474, 430, 520, 430, DONKER, 3); ZD.pijl(545, 455, 545, 500, DONKER, 3); ZD.rect(515, 500, 60, 30, GEEL, DONKER, 6, 2)
ZD.cirkel(470, 500, 30, "none", BLAUW, 5); ZD.lijn(448, 522, 420, 550, BLAUW, 7)
# F: wolk met sterren en een trap die erachter verdwijnt
ZD.pad("M 730 470 q -10 -50 40 -50 q 10 -40 60 -25 q 50 -20 60 30 q 40 10 20 45 Z", "#ffffff", DONKER, 3)
for sx, sy in ((760, 390), (900, 385), (830, 375)):
    ZD.tekst(sx, sy, "✦", 26, kleur=PAARS)
for i in range(4):
    ZD.rect(770 + i * 25, 545 - i * 20, 25, 20 + i * 20, GRIJS, DONKER, 0, 1)
U = "zes-zinnebeelden-domeinen.svg"
Z = {t: [Prent.zone(x, y, 260, 230)] for t, x, y in VAK}

VRAAGJES = ("Lees de vragen die een klas op het bord schreef.\n\n"
            "1. Mag je een hond opsluiten in een kleine kooi?\n"
            "2. Kan een kunstwerk lelijk en toch goed zijn?\n"
            "3. Hoe weet je dat je herinnering klopt?\n"
            "4. Is er iets dat altijd bestaat, ook als er niemand meer is?")

VRAGEN = [
    klik("Bekijk de zes zinnebeelden. Klik op het zinnebeeld dat het best past bij de ethiek.", U, Z["A"], "De weegschaal: wegen wat goed en kwaad is."),
    klik("Klik op het zinnebeeld dat het best past bij de vraag: 'Is schoonheid in het oog van de kijker?'", U, Z["B"], "Een vraag uit de esthetica."),
    klik("Klik op het zinnebeeld dat het best past bij de vraag: 'Waaruit bestaat de wereld?'", U, Z["D"], "Natuurfilosofie: vragen over de wereld zelf."),
    klik("Klik op het zinnebeeld dat het best past bij de vraag naar wat voorbij het zichtbare ligt.", U, Z["F"], "Meta betekent voorbij: de metafysica."),
    casus(VRAAGJES, [
        tabel("Bij welk domein hoort de vraag het best?",
              [("vraag 1", "ethiek"), ("vraag 2", "esthetica"), ("vraag 3", "kennisleer"), ("vraag 4", "metafysica")],
              "Goed handelen, schoonheid, weten en wat achter het zichtbare ligt.", ["ethiek", "esthetica", "kennisleer", "metafysica"]),
        keuze("Vraag 1 raakt ook aan wat een dier is. Daarom hoort ze ook bij de [[*antropologie|logica|esthetica]], waar je mens en dier vergelijkt.", "Eén vraag kan in twee domeinen thuishoren."),
        mk("Waarom hoort vraag 3 niet bij de natuurfilosofie?",
           ["ze gaat over je weten", "ze gaat over de natuur van de hersenen en dus over de wereld", "ze gaat over wat er na de dood met je herinneringen gebeurt", "ze vraagt welk kunstwerk je het best onthoudt"],
           0, "De kennisleer vraagt hoe betrouwbaar kennis is."),
    ]),
    koppel("Koppel het domein aan het grote woord waarover het gaat.",
           [("antropologie", "de mens"), ("esthetica", "de schoonheid"), ("ethiek", "de goedheid"), ("kennisleer en logica", "de waarheid"), ("metafysica", "de bovenwereld"), ("natuurfilosofie", "de wereld")],
           ["de geschiedenis"], "Zes domeinen, zes grote woorden."),
    sorteer("Bij welk domein hoort de vraag?", ["antropologie", "natuurfilosofie", "logica"],
            [("Wat maakt dat jij dezelfde persoon blijft als vroeger?", "antropologie"), ("Heeft de ruimte een einde?", "natuurfilosofie"), ("Volgt deze conclusie echt uit de argumenten?", "logica"), ("Wat is tijd?", "natuurfilosofie"), ("Is een mens meer dan zijn lichaam?", "antropologie")],
            "Logica kijkt of een redenering geldig is."),
    mk("Wat is het verschil tussen de natuurfilosofie en de natuurwetenschap?",
       ["de ene denkt na, de andere meet", "de natuurfilosofie is gewoon een oudere naam voor fysica", "de natuurwetenschap stelt geen enkele vraag over de wereld", "er is geen verschil, enkel een andere naam voor hetzelfde vak"],
       0, "De natuurfilosofie denkt na over de begrippen die de wetenschap gebruikt."),
    tabel("Klopt dit over de domeinen?",
          [("Er zijn zes domeinen.", J), ("De ethiek is het belangrijkste domein.", F), ("Kennisleer en logica staan samen.", J), ("Een vraag hoort altijd bij precies één domein.", F)],
          "Er is geen rangorde, en domeinen overlappen soms."),
    keuze("Thales vroeg waaruit alles bestaat. Dat is een vraag uit de [[*natuurfilosofie|ethiek|esthetica]].", "De oudste filosofische vraag."),
    keuze("'Mag een kunstenaar een dier gebruiken in zijn kunstwerk?' raakt de esthetica én de [[*ethiek|logica|natuurfilosofie]].", "Wat mag, is een ethische vraag."),
    sleep("De [[ethiek]] vraagt wat goed handelen is. De [[esthetica]] vraagt wat schoonheid is. De [[kennisleer]] vraagt wat je zeker kan weten.",
          ["antropologie", "logica"], "Elk domein heeft eigen begrippen."),
    mk("Welke vraag hoort NIET bij de antropologie?",
       ["is deze redenering geldig?", "wat maakt een mens tot een mens en geen dier of robot?", "heeft een mens een ziel die blijft na zijn lichaam?", "in welke zin verschilt een mens van een slimme aap?"],
       0, "Geldig redeneren hoort bij de logica."),
    tabel("Geeft dit domein een waardeoordeel over wat zou moeten?",
          [("ethiek", J), ("esthetica", J), ("logica", F), ("natuurfilosofie", F)],
          "Ethiek en esthetica zeggen wat goed of mooi is."),
    inv("'Bedriegen mijn ogen mij als ik een stok in water geknakt zie?' Bij welk domein hoort die vraag? Eén woord.", ["kennisleer", "de kennisleer", "kennistheorie"], "Het gaat over de betrouwbaarheid van je zintuigen."),
    keuze("'Heeft een mens een vrije wil?' raakt de antropologie en de [[*metafysica|esthetica|logica]].", "Is er meer dan oorzaak en gevolg?"),
    mk("Waarom helpt het om eerst het domein van een vraag te bepalen?",
       ["je weet welke begrippen erbij horen", "dan weet je meteen welk antwoord juist is en welk fout", "dan hoef je geen argumenten meer te zoeken bij je antwoord", "dan kan je de vraag gewoon opzoeken in een boek"],
       0, "Elk domein heeft eigen begrippen en denkers."),
    sorteer("Ethiek of esthetica?", ["ethiek", "esthetica"],
            [("Moet je een gevonden portefeuille teruggeven?", "ethiek"), ("Is een urinoir in een museum kunst?", "esthetica"), ("Mag je dieren eten?", "ethiek"), ("Moet een gebouw mooi zijn of vooral nuttig?", "esthetica")],
            "Goed handelen tegenover schoonheid."),
    tabel("Hoort deze vraag bij de metafysica?",
          [("Bestaat er een god?", J), ("Bestaat er leven na de dood?", J), ("Hoe oud is het heelal?", F), ("Is er meer dan wat je kan zien?", J)],
          "De leeftijd van het heelal is een weetvraag voor de wetenschap."),
    keuze("'Moeten we de natuur beschermen om de natuur zelf?' Wat we moeten doen, is ethiek. Wat de natuur is, is [[*natuurfilosofie|antropologie|logica]].", "Twee domeinen in één vraag."),
    inv("Hoeveel filosofische domeinen zijn er? Schrijf het getal.", ["6", "zes"], "Kennisleer en logica tellen samen als één."),
    klik("Klik op het zinnebeeld dat het best past bij de vraag: 'Verschilt een mens echt van een dier?'", U, Z["C"], "Vragen over de mens horen bij de antropologie."),
    klik("Klik op het zinnebeeld dat het best past bij de logica: volgt de conclusie uit de argumenten?", U, Z["E"], "Stap voor stap nagaan of een redenering klopt."),
    keuze("Het woordje meta in metafysica betekent [[*voorbij|binnen|klein]].", "Voorbij wat je kan zien en meten."),
    tabel("Hoort deze vraag bij de kennisleer of de logica?",
          [("Kan je iets weten zonder het te zien?", J), ("Is een boom mooier dan een huis?", F), ("Is deze redenering geldig?", J), ("Mag je stelen als je honger hebt?", F)],
          "Kennisleer en logica gaan over de waarheid."),
    mk("'Hebben dieren rechten?' Welke twee domeinen raakt die vraag?",
       ["ethiek en antropologie", "esthetica en logica, want het gaat om mooi en geldig redeneren", "metafysica en kennisleer, want het gaat om wat je kan weten", "natuurfilosofie en esthetica, want dieren horen bij de natuur"],
       0, "Wat een dier is, en wat we mogen doen."),
    keuze("Een domein bepalen is [[*geen|wel een]] van de filosofische vaardigheden.", "De vaardigheden zijn vragen stellen, argumenteren en een tekst analyseren."),
    open_("Bedenk een vraag over sociale media die bij twee domeinen tegelijk hoort. Leg uit welke domeinen en waarom.",
          "Bijvoorbeeld: 'Mag je een foto van een vriend posten zonder te vragen?' Dat is ethiek (mag het?) en antropologie (wat betekent privacy voor een mens?). Of: 'Toont een gefilterde foto de waarheid?' Dat is kennisleer en esthetica."),
]

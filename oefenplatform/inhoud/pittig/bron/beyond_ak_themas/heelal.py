"""Het heelal: ontstaan en afstanden — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Tijdlijn heelal -------------------------------------------------------
TL = Prent("tijdlijn-heelal", "Tijdlijn van het heelal, in miljard jaar na de oerknal", "tijdlijn van 0 tot 13,8 miljard jaar met momenten A tot D")
X0, X1, Y = 100, 900, 330
def TX(t): return X0 + t / 13.8 * (X1 - X0)
TL.lijn(X0, Y, X1, Y, DONKER, 4)
for t in range(0, 14, 2):
    TL.lijn(TX(t), Y - 8, TX(t), Y + 8, DONKER, 2)
    TL.tekst(TX(t), Y + 34, str(t), 16)
TL.lijn(TX(13.8), Y - 14, TX(13.8), Y + 14, DONKER, 3)

MOM = {"A": (0, -1), "B": (0.4, 1), "C": (9.2, -1), "D": (13.8, 1)}
for k, (t, kant) in MOM.items():
    y2 = Y - 110 if kant < 0 else Y + 120
    TL.lijn(TX(t), Y, TX(t), y2 + (20 if kant < 0 else -20), GRIJS, 2, stippel=True)
    TL.cirkel(TX(t), Y, 9, ORANJE, DONKER)
    TL.letter(TX(t), y2, k)
ZTL = {k: [Prent.rond(TX(t), Y - 110 if kant < 0 else Y + 120, 28)] + ([] if t < 1 else [Prent.rond(TX(t), Y, 20)]) for k, (t, kant) in MOM.items()}

# Melkweg van bovenaf ----------------------------------------------------
MW = Prent("melkweg-bovenaf", "Het Melkwegstelsel van bovenaf gezien (vereenvoudigd)", "spiraalstelsel met punten A, B en C")
CX, CY = 500, 350
MW.cirkel(CX, CY, 250, "#f2f0ea", "none")
for arm in range(2):
    pts = []
    for i in range(80):
        th = i * 0.09 + arm * math.pi
        r = 30 + i * 2.8
        pts.append((CX + r * math.cos(th), CY + r * math.sin(th) * 0.95))
    MW.pad("M" + " L ".join(f"{a:.0f} {b:.0f}" for a, b in pts), "none", "#9aa6c4", 26)
MW.ellips(CX, CY, 60, 45, "#e8d9a8", DONKER, 2)
pos = {"A": (CX, CY), "B": (CX + 230 * math.cos(4.1), CY + 230 * math.sin(4.1) * 0.95), "C": (CX + (30 + 45 * 2.8) * math.cos(45 * 0.09 + math.pi), CY + (30 + 45 * 2.8) * math.sin(45 * 0.09 + math.pi) * 0.95)}
for k, (x, y) in pos.items():
    MW.cirkel(x, y, 8, ROOD if k == "C" else ORANJE, DONKER)
    MW.letter(x + 34, y - 26, k)
MW.tekst(860, 600, "doorsnede ongeveer 100 000 lichtjaar", 16, "end")
ZMW = {k: [Prent.rond(x, y, 30), Prent.rond(x + 34, y - 26, 26)] for k, (x, y) in pos.items()}

VRAGEN = [
    klik(
        "Klik op het moment waarop ons zonnestelsel ontstond.",
        TL.bestand, ZTL["C"],
        "13,8 - 4,6 = 9,2 miljard jaar na de oerknal.",
    ),
    klik(
        "Klik op het moment van nu.",
        TL.bestand, ZTL["D"],
        "Het heelal is ongeveer 13,8 miljard jaar oud.",
    ),
    met_prent(TL.bestand, tabel(
        "Kijk naar de tijdlijn. Klopt dit?",
        [
            ("Tussen A en C ligt ongeveer twee derde van de geschiedenis van het heelal.", J),
            ("Het zonnestelsel bestaat ongeveer een derde van de tijd sinds de oerknal.", J),
            ("De eerste sterren ontstonden na het zonnestelsel.", F),
            ("Bij A ontstonden ruimte en tijd zelf.", J),
        ],
        "Eerst atomen, dan sterren en stelsels, en veel later ons zonnestelsel.",
    )),
    klik(
        "Klik op de plaats van ons zonnestelsel.",
        MW.bestand, ZMW["C"],
        "De zon ligt in een spiraalarm, de Orionarm, een eind van het centrum.",
    ),
    met_prent(MW.bestand, tabel(
        "Kijk naar de Melkweg. Klopt dit?",
        [
            ("A ligt in het centrum van de Melkweg.", J),
            ("Van C naar A is het ongeveer 26 000 lichtjaar.", J),
            ("Ons zonnestelsel ligt precies in het centrum.", F),
            ("De Melkweg is een spiraalstelsel.", J),
        ],
        "De zon ligt ongeveer 26 000 lichtjaar van het centrum.",
    )),
    volgorde(
        "Zet in de juiste volgorde, van vroeg naar laat.",
        [
            "Het hete, dichte begin van ruimte en tijd",
            "De eerste atomen vormen zich",
            "Het heelal wordt doorzichtig voor licht",
            "Gas klontert samen tot de eerste sterren",
            "Ons zonnestelsel ontstaat",
        ],
        "Atomen moesten er eerst zijn voor licht vrij kon reizen, sterren kwamen later.",
    ),
    tabel(
        "Big crunch, big rip of big chill?",
        [
            ("de zwaartekracht wint en alles stort weer in", "Big crunch"),
            ("de versnelde uitdijing scheurt zelfs atomen uiteen", "Big rip"),
            ("de sterren raken uitgeput en alles koelt af", "Big chill"),
        ],
        "Drie scenario's voor de toekomst van het heelal.",
        kolommen=["Big crunch", "Big rip", "Big chill"],
    ),
    tabel(
        "Pleit dit voor een uitdijend heelal?",
        [
            ("het licht van verre stelsels is naar het rood verschoven", J),
            ("verre stelsels verwijderen zich sneller dan nabije", J),
            ("de achtergrondstraling komt uit alle richtingen", J),
            ("de zon komt elke dag op in het oosten", F),
        ],
        "De opkomst van de zon komt door de draaiing van de aarde.",
    ),
    mk(
        "Een sterrenstelsel beweegt van ons weg. Wat gebeurt er met zijn licht?",
        [
            "De golven worden uitgerekt en verschuiven naar het rood",
            "De golven worden samengedrukt en verschuiven naar het blauw",
            "Het licht wordt feller omdat de afstand groter wordt",
            "Het licht valt helemaal weg uit het zichtbare deel",
        ],
        0,
        "Langere golflengten liggen aan de rode kant: roodverschuiving.",
    ),
    tabel(
        "Klopt dit over de oerknal?",
        [
            ("Het was een ontploffing in een lege ruimte die er al was.", F),
            ("De ruimte zelf rekt sindsdien overal tegelijk uit.", J),
            ("Er is een middelpunt in het heelal waar het gebeurde.", F),
            ("Het heelal is sindsdien afgekoeld.", J),
        ],
        "De oerknal is het begin van ruimte en tijd zelf.",
    ),
    inv(
        "De kosmische achtergrondstraling vertrok toen het heelal ongeveer 380 000 jaar oud was. Hoeveel duizend jaar is dat?",
        ["380"],
        "380 000 jaar is 380 duizend jaar: een oogwenk vergeleken met 13,8 miljard.",
    ),
    tabel(
        "Welke afstandsmaat past het best?",
        [
            ("van de aarde tot de maan", "Lichtseconde"),
            ("van de aarde tot de zon", "Lichtminuut"),
            ("van de zon tot Neptunus", "Astronomische eenheid"),
            ("tot een ander sterrenstelsel", "Lichtjaar"),
        ],
        "Kies een maat zodat het getal niet onhandelbaar groot of klein wordt.",
        kolommen=["Lichtseconde", "Lichtminuut", "Astronomische eenheid", "Lichtjaar"],
    ),
    inv(
        "Jupiter staat ongeveer 5 AE van de zon. Hoeveel miljoen kilometer is dat ongeveer? Neem 150 miljoen km per AE.",
        ["750"],
        "5 · 150 = 750 miljoen km.",
    ),
    inv(
        "Hoeveel kilometer legt licht af in 10 seconden? Neem 300 000 km per seconde.",
        ["3000000", "3 000 000"],
        "10 · 300 000 = 3 000 000 km.",
    ),
    volgorde(
        "Zet het adres van de aarde in volgorde, van klein naar groot.",
        [
            "Het zonnestelsel",
            "De Orionarm",
            "Het Melkwegstelsel",
            "De Lokale Groep",
            "De Lokale Supercluster",
        ],
        "Telkens een grotere eenheid die de vorige bevat.",
    ),
    tabel(
        "Ligt dit binnen of buiten ons zonnestelsel?",
        [
            ("de Kuipergordel", "Binnen"),
            ("de Andromedanevel", "Buiten"),
            ("de Oortwolk", "Binnen"),
            ("een ster op 4,2 lichtjaar", "Buiten"),
        ],
        "Kuipergordel en Oortwolk horen nog bij de zon.",
        kolommen=["Binnen", "Buiten"],
    ),
    casus(
        "Een telescoop fotografeert een sterrenstelsel op 10 miljoen lichtjaar. Op de foto zie je veel jonge, blauwe sterren.",
        [
            tabel(
                "Klopt dit?",
                [
                    ("Het licht was 10 miljoen jaar onderweg.", J),
                    ("Je ziet het stelsel zoals het vandaag is.", F),
                    ("Het stelsel ligt buiten de Melkweg.", J),
                ],
                "Kijken in de verte is kijken in het verleden.",
            ),
            keuze(
                "Uitgedrukt in AE zou die afstand een [[*onhandelbaar groot|heel klein|handig]] getal geven.",
                "Daarom gebruik je voor stelsels het lichtjaar.",
            ),
        ],
    ),
    sleep(
        "Een [[lichtjaar]] is geen tijd maar een afstand: zo ver gaat licht in een jaar. Dat is ongeveer [[9 460 miljard]] kilometer. De zon staat ongeveer 8 [[lichtminuten]] van ons.",
        ["lichtuur", "150 miljoen", "lichtjaren"],
        "Licht gaat bijna 300 000 km per seconde.",
    ),
    tabel(
        "Klopt dit over de leeftijden?",
        [
            ("Het heelal is ongeveer 13,8 miljard jaar oud.", J),
            ("De aarde is ongeveer 4,6 miljard jaar oud.", J),
            ("De aarde is ouder dan de zon.", F),
            ("Zware elementen als ijzer bestonden al bij de oerknal.", F),
        ],
        "Zon en aarde zijn even oud. IJzer werd pas in sterren gemaakt.",
    ),
    inv(
        "Een ruimtesonde staat op 2 lichturen. Je stuurt een bericht en zij antwoordt meteen. Na hoeveel uur heb je haar antwoord?",
        ["4"],
        "2 uur heen en 2 uur terug.",
    ),
    koppel(
        "Koppel elk begrip aan zijn uitleg.",
        [
            ("cluster", "een groep sterrenstelsels die samenhangt door de zwaartekracht"),
            ("supercluster", "een groep van clusters"),
            ("sterrenstelsel", "miljarden sterren samen, zoals de Melkweg"),
            ("planetenstelsel", "één ster met planeten eromheen"),
        ],
        ["een groep planeten zonder ster"],
        "Van klein naar groot: planetenstelsel, sterrenstelsel, cluster, supercluster.",
    ),
    keuze(
        "De naam Big Bang was eerst een [[*spotnaam|eretitel|wetenschappelijke formule]] van tegenstanders van de theorie.",
        "Nadien werd het gewoon de gangbare naam.",
    ),
    met_prent(TL.bestand, keuze(
        "Punt B, kort na de oerknal, stelt de vorming van de [[*eerste sterren|zon en de aarde|zware elementen in de aardkorst]] voor.",
        "Het zonnestelsel kwam pas veel later, bij C.",
    )),
    klik(
        "Klik op het centrum van het stelsel.",
        MW.bestand, ZMW["A"],
        "In het centrum zit een dichte, bolle kern.",
    ),
    tabel(
        "Klopt dit over kijken in de ruimte?",
        [
            ("Hoe verder je kijkt, hoe verder je terugkijkt in de tijd.", J),
            ("Het licht van de maan is ongeveer een seconde onderweg.", J),
            ("Een ster die je ziet, bestaat zeker vandaag nog.", F),
        ],
        "Je ziet een ster zoals ze was toen het licht vertrok.",
    ),
    inv(
        "De Melkweg is ongeveer 100 000 lichtjaar breed. Hoeveel jaar doet licht erover om van de ene rand naar de andere te gaan?",
        ["100000", "100 000"],
        "Een lichtjaar is de afstand die licht in een jaar aflegt.",
    ),
    keuze(
        "Volgens de wet van [[*Hubble|Newton|Ohm]] verwijdert een stelsel zich sneller naarmate het verder staat.",
        "Dat verwacht je als de ruimte overal tegelijk uitrekt.",
    ),
    tabel(
        "Klopt dit over de Lokale Groep?",
        [
            ("De Melkweg hoort erbij.", J),
            ("De Andromedanevel hoort erbij.", J),
            ("Ze bevat enkele tientallen stelsels.", J),
            ("Ze is groter dan de Lokale Supercluster.", F),
        ],
        "De Lokale Groep is een deel van de Lokale Supercluster.",
    ),
    open_(
        "Leg uit waarom de kosmische achtergrondstraling een sterk bewijs is voor de oerknal.",
        "Ze komt uit alle richtingen en is bijna overal even sterk. Dat past bij een begin dat overal tegelijk gebeurde. Het is licht van het moment dat het heelal doorzichtig werd, uitgerekt tot microgolven doordat de ruimte sindsdien uitdijde.",
    ),
]

"""Situeren, kaarten en observatie — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Gradennet --------------------------------------------------------------
GN = Prent("gradennet-vier-punten", "Een stuk gradennet", "gradennet van 30° WL tot 30° OL en 30° NB tot 70° NB met punten A tot D")
L0, R0, T0, B0 = 140, 900, 80, 560
def GX(lon): return L0 + (lon + 30) / 60 * (R0 - L0)
def GY(lat): return B0 - (lat - 30) / 40 * (B0 - T0)
GN.rect(L0, T0, R0 - L0, B0 - T0, "#eef5fa", DONKER, 0)
for lon in range(-30, 31, 10):
    GN.lijn(GX(lon), T0, GX(lon), B0, DONKER if lon == 0 else "#9bb4c8", 3 if lon == 0 else 1)
    GN.tekst(GX(lon), B0 + 28, (f"{abs(lon)}° " + ("WL" if lon < 0 else "OL")) if lon else "0°", 16)
for lat in range(30, 71, 10):
    GN.lijn(L0, GY(lat), R0, GY(lat), "#9bb4c8", 1)
    GN.tekst(L0 - 12, GY(lat) + 5, f"{lat}° NB", 16, "end")
PNT = {"A": (5, 50), "B": (-20, 40), "C": (20, 60), "D": (-5, 50)}
for k, (lo, la) in PNT.items():
    GN.cirkel(GX(lo), GY(la), 9, ORANJE, DONKER)
    GN.letter(GX(lo) + 32, GY(la) - 26, k)
ZGN = {k: [Prent.rond(GX(lo), GY(la), 24), Prent.rond(GX(lo) + 32, GY(la) - 26, 24)] for k, (lo, la) in PNT.items()}

# Poolshoogte ------------------------------------------------------------
PH = Prent("poolshoogte", "De poolster boven de horizon", "waarnemer met horizon, poolster en de punten A, B, C")
OX, OY = 500, 470
PH.lijn(80, OY, 920, OY, DONKER, 3)
PH.tekst(90, OY + 30, "horizon, kant van het noorden", 18, "start")
PH.cirkel(OX, OY - 22, 12, GROEN, DONKER)
PH.lijn(OX, OY - 10, OX, OY, DONKER, 3)
hoek = 51
SX, SY = OX + 360 * math.cos(math.radians(180 - hoek)), OY - 360 * math.sin(math.radians(180 - hoek))
PH.lijn(OX, OY - 22, SX, SY, GRIJS, 2, stippel=True)
PH.tekst(SX, SY - 22, "★", 40, kleur="#c9a227")
PH.tekst(SX - 60, SY + 5, "poolster", 18)
PH.pad(f"M{OX - 130} {OY} A 130 130 0 0 1 {OX + 130 * math.cos(math.radians(180 - hoek)):.0f} {OY - 130 * math.sin(math.radians(180 - hoek)):.0f}", "none", ORANJE, 4)
PH.lijn(OX, OY - 22, OX, 70, GRIJS, 2, stippel=True)
PH.letter(OX - 170, OY - 70, "A")
PH.letter(OX + 30, 90, "B")
PH.letter(SX + 10, SY + 50, "C")
ZPH = {"A": [Prent.zone(OX - 160, OY - 120, 130, 120), Prent.rond(OX - 170, OY - 70, 26)],
       "B": [Prent.zone(OX - 30, 60, 90, 70), Prent.rond(OX + 30, 90, 26)],
       "C": [Prent.rond(SX, SY - 30, 40), Prent.rond(SX + 10, SY + 50, 26)]}

VRAGEN = [
    klik(
        "Klik op de plaats op 50° noorderbreedte en 5° oosterlengte.",
        GN.bestand, ZGN["A"],
        "Op de parallel van 50° NB, een halve vak rechts van de nulmeridiaan.",
    ),
    klik(
        "Klik op de plaats die het verst ten westen van Greenwich ligt.",
        GN.bestand, ZGN["B"],
        "B ligt op 20° WL, verder west dan D op 5° WL.",
    ),
    met_prent(GN.bestand, tabel(
        "Kijk naar het gradennet. Welke coördinaten horen bij welk punt?",
        [
            ("60° NB, 20° OL", "C"),
            ("40° NB, 20° WL", "B"),
            ("50° NB, 5° WL", "D"),
        ],
        "Eerst de breedte op de parallel, dan de lengte op de meridiaan.",
        kolommen=["A", "B", "C", "D"],
    )),
    met_prent(GN.bestand, tabel(
        "Kijk naar het gradennet. Klopt dit?",
        [
            ("A en D liggen op dezelfde parallel.", J),
            ("A en D liggen op dezelfde meridiaan.", F),
            ("C ligt het dichtst bij de noordpool.", J),
            ("B ligt ten zuiden van de evenaar.", F),
        ],
        "Alle punten liggen op het noordelijk halfrond, want ze hebben NB.",
    )),
    klik(
        "Klik op de hoek die even groot is als de breedteligging van de waarnemer.",
        PH.bestand, ZPH["A"],
        "De poolshoogte, de hoek tussen horizon en poolster, is gelijk aan de breedte.",
    ),
    klik(
        "Klik op het zenit.",
        PH.bestand, ZPH["B"],
        "Het zenit ligt recht boven de waarnemer.",
    ),
    met_prent(PH.bestand, tabel(
        "Kijk naar de tekening: de hoek is 51°. Klopt dit?",
        [
            ("De waarnemer staat ongeveer in België.", J),
            ("Op de evenaar zou de poolster aan de horizon staan.", J),
            ("Op de noordpool zou de poolster in het zenit staan.", J),
            ("De waarnemer staat op het zuidelijk halfrond.", F),
        ],
        "Poolshoogte = breedteligging. Op het zuidelijk halfrond zie je de poolster niet.",
    )),
    tabel(
        "Absoluut of relatief situeren?",
        [
            ("50° 51' NB, 4° 21' OL", "Absoluut"),
            ("aan de monding van de Schelde", "Relatief"),
            ("ten noorden van de Alpen", "Relatief"),
            ("op 12° OL en 42° NB", "Absoluut"),
        ],
        "Absoluut met coördinaten, relatief ten opzichte van iets anders.",
        kolommen=["Absoluut", "Relatief"],
    ),
    tabel(
        "Fysischgeografisch of sociaalgeografisch element?",
        [
            ("een gebergte", "Fysischgeografisch"),
            ("een taalgrens", "Sociaalgeografisch"),
            ("een woestijnklimaat", "Fysischgeografisch"),
            ("een havenstad", "Sociaalgeografisch"),
        ],
        "Natuurlijke elementen zijn fysischgeografisch, menselijke sociaalgeografisch.",
        kolommen=["Fysischgeografisch", "Sociaalgeografisch"],
    ),
    inv(
        "Hoeveel minuten telt een halve graad?",
        ["30"],
        "Een graad heeft 60 minuten, dus een halve graad 30.",
    ),
    inv(
        "Je stapt 10 minuten breedte naar het noorden. Hoeveel kilometer is dat ongeveer? Neem 1,85 km per minuut.",
        ["18,5", "18.5"],
        "10 · 1,85 = 18,5 km.",
    ),
    tabel(
        "Meridiaan of parallel?",
        [
            ("loopt van pool tot pool", "Meridiaan"),
            ("wordt korter naar de polen toe", "Parallel"),
            ("geeft de lengte aan", "Meridiaan"),
            ("de evenaar is er één van", "Parallel"),
        ],
        "Meridianen zijn halve grootcirkels, parallellen cirkels evenwijdig aan de evenaar.",
        kolommen=["Meridiaan", "Parallel"],
    ),
    koppel(
        "Koppel elke hulpbron aan wat je ermee onderzoekt.",
        [
            ("klimatogram", "temperatuur en neerslag per maand"),
            ("leeftijdshistogram", "de leeftijdsopbouw van een bevolking"),
            ("determineertabel", "een gesteente op naam brengen"),
            ("satellietbeeld in valse kleuren", "gezonde vegetatie opsporen"),
        ],
        ["de luchtdruk van één dag"],
        "Voor de luchtdruk gebruik je een weerkaart met isobaren.",
    ),
    tabel(
        "Kaart A heeft schaal 1/10 000, kaart B 1/1 000 000. Klopt dit?",
        [
            ("Kaart A heeft de grootste schaal.", J),
            ("Kaart B toont het grootste gebied op hetzelfde blad.", J),
            ("Op kaart A zie je het meeste detail.", J),
            ("1 cm op kaart B is 100 m in werkelijkheid.", F),
        ],
        "Op B is 1 cm 1 000 000 cm, dus 10 km.",
    ),
    inv(
        "Op een kaart met schaal 1/50 000 meet je 4 cm. Hoeveel kilometer is dat in werkelijkheid?",
        ["2"],
        "4 · 50 000 = 200 000 cm = 2 km.",
    ),
    koppel(
        "Koppel elke lijn aan wat ze verbindt.",
        [
            ("isotherm", "plaatsen met dezelfde temperatuur"),
            ("isobaar", "plaatsen met dezelfde luchtdruk"),
            ("isohyeet", "plaatsen met dezelfde neerslag"),
        ],
        ["plaatsen met dezelfde lengte"],
        "Plaatsen met dezelfde lengte liggen op een meridiaan.",
    ),
    tabel(
        "Ster, planeet of maan?",
        [
            ("straalt zelf licht uit door kernfusie", "Ster"),
            ("draait rond een planeet", "Maan"),
            ("weerkaatst het licht van de zon en draait rond de zon", "Planeet"),
            ("de zon", "Ster"),
        ],
        "Enkel een ster straalt zelf.",
        kolommen=["Ster", "Planeet", "Maan"],
    ),
    casus(
        "Ilias kijkt op een heldere avond naar de hemel. Hij ziet veel twinkelende puntjes en één fel puntje dat niet twinkelt. Een week later staat dat felle puntje op een andere plaats tussen de rest.",
        [
            keuze(
                "Het felle puntje is waarschijnlijk een [[*planeet|ster|maan]].",
                "Planeten flikkeren nauwelijks en verschuiven tussen de sterren.",
            ),
            tabel(
                "Klopt dit over wat Ilias ziet?",
                [
                    ("De twinkelende puntjes zijn sterren buiten ons zonnestelsel.", J),
                    ("Het felle puntje straalt zelf licht uit.", F),
                    ("De poolster lijkt stil te staan terwijl andere sterren rond haar draaien.", J),
                ],
                "Ons zonnestelsel heeft maar één ster: de zon.",
            ),
        ],
    ),
    tabel(
        "Optische telescoop of radiotelescoop?",
        [
            ("werkt ook bij bewolkt weer", "Radiotelescoop"),
            ("bundelt zichtbaar licht", "Optische telescoop"),
            ("staat liefst hoog, droog en ver van steden", "Optische telescoop"),
            ("vangt radiogolven op van hemellichamen", "Radiotelescoop"),
        ],
        "Radiogolven gaan door wolken. Licht wordt gestoord door lucht, waterdamp en lichtvervuiling.",
        kolommen=["Optische telescoop", "Radiotelescoop"],
    ),
    mk(
        "Waarom heeft een gps-toestel een vierde satelliet nodig?",
        [
            "Om de klokfout weg te rekenen en de hoogte te bepalen",
            "Omdat drie satellieten nooit tegelijk boven je kunnen staan",
            "Om de satellietbeelden in valse kleuren om te zetten naar echte",
            "Omdat elke satelliet alleen de breedte of alleen de lengte geeft",
        ],
        0,
        "Drie satellieten geven de plaats op het oppervlak. De vierde regelt de klok en de hoogte.",
    ),
    tabel(
        "Welke sferen werken hier vooral samen?",
        [
            ("regen die een helling uitspoelt", "Atmosfeer en geosfeer"),
            ("plankton dat in zee drijft", "Biosfeer en hydrosfeer"),
            ("wortels die een rots doen barsten", "Biosfeer en geosfeer"),
            ("wind die golven maakt op zee", "Atmosfeer en hydrosfeer"),
        ],
        "Het systeem aarde bestaat uit vier sferen die op elkaar inwerken.",
        kolommen=["Atmosfeer en geosfeer", "Biosfeer en hydrosfeer", "Biosfeer en geosfeer", "Atmosfeer en hydrosfeer"],
    ),
    tabel(
        "Klopt dit over satellieten?",
        [
            ("Ze helpen om het weer te voorspellen.", J),
            ("Ze volgen bosbranden op.", J),
            ("Ze meten rechtstreeks de dikte van de aardkorst.", F),
            ("Ze zorgen voor communicatie over lange afstand.", J),
        ],
        "De korst onderzoek je met seismische metingen op aarde.",
    ),
    inv(
        "Je staat in Madrid, op ongeveer 40° noorderbreedte. Hoeveel graden boven de horizon staat de poolster daar?",
        ["40"],
        "De poolshoogte is gelijk aan de breedteligging.",
    ),
    keuze(
        "Het punt recht onder de waarnemer, tegenover het zenit, heet het [[*nadir|meridiaan|azimut]].",
        "Zenit boven, nadir onder.",
    ),
    klik(
        "Klik op de ster die bijna in het verlengde van de aardas staat.",
        PH.bestand, ZPH["C"],
        "De poolster lijkt stil te staan omdat ze bijna boven de noordpool staat.",
    ),
    inv(
        "Hoeveel graden lengte liggen er in totaal rond de aarde?",
        ["360"],
        "180° oost en 180° west samen.",
    ),
    tabel(
        "Klopt dit over een satellietbeeld in valse kleuren?",
        [
            ("Infrarood wordt in een zichtbare kleur omgezet.", J),
            ("Gezonde vegetatie springt er vaak rood uit.", J),
            ("De kleuren zijn dezelfde als wat je met het oog ziet.", F),
        ],
        "Valse kleuren tonen ook golflengten die het oog niet ziet.",
    ),
    keuze(
        "Op het examen mag je de [[*atlas|gsm|rekenmachine met kaarten]] gebruiken om gegevens op te zoeken.",
        "Situeren is een vaardigheid: je zoekt op en gebruikt de gegevens.",
    ),
    open_(
        "Leg uit waarom een grote optische telescoop vaak hoog op een droge berg ver van steden staat.",
        "Hoog in de bergen zit er minder lucht en waterdamp boven de telescoop, zodat het beeld minder trilt en minder licht wordt opgeslorpt. Droge lucht geeft vaker heldere nachten. Ver van steden is er geen lichtvervuiling.",
    ),
]

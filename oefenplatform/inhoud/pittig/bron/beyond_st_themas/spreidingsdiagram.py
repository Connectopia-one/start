r"""Spreidingsdiagram, correlatie en trendlijn — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen en vier eigen puntenwolken,
zoals op het digitale examen."""
import random
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Vier puntenwolken A tot D -------------------------------------------------------------
VW = Prent("vier-puntenwolken", "Vier puntenwolken", "vier spreidingsdiagrammen: A sterk dalend rond een rechte, B een omgekeerde U, C stijgend met veel spreiding, D sterk stijgend rond een rechte")
RNG = random.Random(2411)
VAKKEN = {"A": (90, 70), "B": (530, 70), "C": (90, 350), "D": (530, 350)}
BR, HO = 380, 230


def wolk(letter, f, ruis):
    x0, y0 = VAKKEN[letter]
    VW.rect(x0, y0, BR, HO, "#ffffff", DONKER, 0, 2)
    VW.letter(x0 - 40, y0 + 20, letter)
    for i in range(28):
        t = (i + RNG.random()) / 28
        v = f(t) + RNG.uniform(-ruis, ruis)
        v = min(0.95, max(0.05, v))
        VW.cirkel(x0 + 15 + t * (BR - 30), y0 + HO - v * HO, 6, "#5f7f4a", DONKER, 1)


wolk("A", lambda t: 0.9 - 0.8 * t, 0.06)
wolk("B", lambda t: 0.15 + 3.0 * t * (1 - t), 0.05)
wolk("C", lambda t: 0.3 + 0.4 * t, 0.22)
wolk("D", lambda t: 0.1 + 0.8 * t, 0.05)


def vak(letter):
    x0, y0 = VAKKEN[letter]
    return [Prent.zone(x0 - 60, y0 - 10, BR + 70, HO + 20)]


VRAGEN = [
    klik("Klik op de puntenwolk met r ongeveer gelijk aan −0,95.", VW.bestand, vak("A"),
         "Sterk en dalend: de punten liggen dicht rond een dalende rechte."),
    klik("Klik op de puntenwolk waarbij r dicht bij 0 ligt, hoewel er wel een duidelijk verband is.", VW.bestand, vak("B"),
         "Een kwadratisch verband: r meet enkel lineaire samenhang."),
    klik("Klik op de puntenwolk die het best past bij een matige positieve samenhang.", VW.bestand, vak("C"),
         "Stijgend, maar met veel spreiding rond de trend."),
    klik("Klik op de puntenwolk waarbij een stijgende trendlijn de punten het best voorspelt.", VW.bestand, vak("D"),
         "De punten liggen dicht rond een stijgende rechte."),
    met_prent(VW.bestand, tabel("Welk soort verband toont deze puntenwolk?", [
        ("A", "lineair"),
        ("B", "kwadratisch"),
        ("D", "lineair"),
    ], "A en D volgen een rechte, B een parabool.", kolommen=["lineair", "kwadratisch"])),
    met_prent(VW.bestand, keuze("Bij wolk B is een correlatiecoëfficiënt [[*geen goede maat|een goede maat]] voor de samenhang.",
              "Het verband is niet rechtlijnig.")),
    tabel("Welke samenhang hoort bij deze r volgens het formularium?", [
        ("r = 0,82", "sterk"),
        ("r = −0,45", "matig"),
        ("r = 0,12", "zwak"),
        ("r = −0,76", "sterk"),
    ], "Tot 0,3 zwak, van 0,3 tot 0,7 matig, boven 0,7 sterk (in absolute waarde).",
       kolommen=["zwak", "matig", "sterk"]),
    casus(
        "Een leerkracht noteert bij 30 leerlingen het aantal uren studie (x) en het punt op een toets (y). "
        "De rekenapp geeft als trendlijn y = 3,5x + 42 en r = 0,68. Er werd gestudeerd tussen 1 en 8 uur.",
        [
            keuze("De onafhankelijke variabele is [[*het aantal uren studie|het punt op de toets]].",
                  "Die zet je op de horizontale as."),
            inv("Welk punt voorspelt de trendlijn bij 4 uur studie?", ["56"],
                "3,5 · 4 + 42 = 56."),
            keuze("De 3,5 betekent: per extra uur studie stijgt het voorspelde punt met [[*3,5|42|0,68]] punten.",
                  "De richtingscoëfficiënt."),
            keuze("Volgens het formularium is r = 0,68 een [[*matige|sterke|zwakke]] positieve samenhang.",
                  "Tussen 0,3 en 0,7."),
            mk("Mag je met deze trendlijn het punt voorspellen bij 20 uur studie?",
               ["nee, dat ligt ver buiten het meetbereik",
                "ja, want de lijn loopt gewoon verder",
                "ja, want r is groter dan 0,5 en dus betrouwbaar",
                "nee, want r moet precies 1 zijn"], 0,
               "Buiten 1 tot 8 uur weet je niet of het verband blijft gelden (en 112 punten kan niet)."),
        ],
    ),
    sorteer("Recht evenredig of enkel lineair?", ["recht evenredig", "lineair, niet recht evenredig"], [
        ["y = 4x", "recht evenredig"],
        ["y = 2x + 7", "lineair, niet recht evenredig"],
        ["kostprijs van brood: 3 euro per brood", "recht evenredig"],
        ["taxirit: 5 euro instap plus 2 euro per km", "lineair, niet recht evenredig"],
    ], "Recht evenredig: een rechte door de oorsprong."),
    keuze("Bij een omgekeerd evenredig verband blijft [[*het product x · y|de som x + y|het verschil y − x]] constant.",
          "Verdubbelt x, dan halveert y."),
    inv("Bij een omgekeerd evenredig verband is y = 12 als x = 3. Hoeveel is y als x = 6?", ["6"],
        "x · y = 36, dus y = 36 / 6 = 6."),
    mk("In een stad stijgen het aantal brandweerwagens bij een brand en de schade samen. Wat is de beste verklaring?",
       ["de grootte van de brand bepaalt beide",
        "brandweerwagens veroorzaken de schade aan het huis",
        "de schade roept automatisch meer wagens op",
        "het is toeval, er is geen enkele samenhang"], 0,
       "Een derde factor: grote branden geven veel schade én veel wagens."),
    tabel("Klopt dit over de correlatiecoëfficiënt r?", [
        ("het teken geeft de richting van het verband", J),
        ("r = 1,3 kan bij een heel sterk verband", F),
        ("r = −0,9 wijst op een sterkere samenhang dan r = 0,5", J),
        ("een sterke r bewijst een oorzakelijk verband", F),
    ], "r ligt tussen −1 en 1; de grootte zonder teken geeft de sterkte."),
    koppel("Koppel de vorm van de puntenwolk aan het verband.", [
        ["een rechte door de oorsprong", "recht evenredig"],
        ["een dalende kromme die de assen niet raakt", "omgekeerd evenredig"],
        ["een U-vorm", "kwadratisch"],
    ], ["exponentieel dalend tot nul"], "Kijk naar de vorm, niet alleen naar stijgen of dalen."),
    volgorde("Zet de stappen van een onderzoek naar samenhang in de juiste volgorde.", [
        "onafhankelijke en afhankelijke variabele kiezen",
        "metingen verzamelen",
        "met ICT een spreidingsdiagram maken",
        "met ICT r en de trendlijn bepalen",
    ], "Eerst het diagram bekijken, dan pas r berekenen."),
    sleep("Een trendlijn gebruik je enkel om te voorspellen [[binnen]] het meetbereik. Een sterke samenhang is nog geen [[oorzakelijk]] verband.",
          ["buiten", "lineair"], "Twee klassieke valkuilen."),
    inv("Een trendlijn is y = −1,5x + 30. Hoeveel daalt y als x met 4 stijgt?", ["6"],
        "1,5 · 4 = 6."),
    keuze("Bij die trendlijn is r [[*negatief|positief|precies 0]].",
          "Een dalende trendlijn hoort bij een negatieve samenhang."),
    mk("Een punt ligt ver van de rest van de puntenwolk. Wat is de beste eerste stap?",
       ["nagaan of het een meetfout of een echt geval is",
        "het punt meteen weglaten uit alle verzamelde gegevens",
        "een nieuwe trendlijn tekenen door dat punt",
        "r verdubbelen om het punt te compenseren"], 0,
       "Een uitschieter kan r sterk beïnvloeden, maar weglaten mag enkel met een goede reden."),
    met_prent(VW.bestand, keuze("Wolk A en wolk D hebben ongeveer [[*even sterke|heel verschillende]] samenhang, maar een tegengesteld teken van r.",
              "Allebei dicht rond een rechte; A daalt, D stijgt.")),
    tabel("Welke variabele hoort op de horizontale as?", [
        ("temperatuur en aantal verkochte ijsjes", "temperatuur"),
        ("aantal verkochte ijsjes en reclamebudget", "reclamebudget"),
        ("leeftijd van een auto en zijn verkoopwaarde", "leeftijd"),
    ], "De onafhankelijke variabele staat horizontaal.",
       kolommen=["temperatuur", "reclamebudget", "leeftijd"]),
    inv("Een trendlijn is y = 0,8x + 12. Welke y voorspelt ze bij x = 25?", ["32"],
        "0,8 · 25 + 12 = 32."),
    keuze("Volgens het formularium is r = −0,25 een [[*zwakke|matige|sterke]] negatieve samenhang.",
          "Tussen 0 en 0,3 in absolute waarde."),
    mk("Twee puntenwolken hebben allebei r = 0,8. Wat weet je zeker?",
       ["beide hebben een sterke positieve samenhang",
        "de puntenwolken zien er identiek uit",
        "beide hebben dezelfde trendlijn y = 0,8x",
        "in beide is x de oorzaak van y"], 0,
       "Dezelfde r kan bij heel verschillende wolken horen."),
    inv("Hoeveel punten telt een spreidingsdiagram van 45 leerlingen, waarbij je bij elke leerling lengte en gewicht meet?", ["45"],
        "Eén punt per leerling."),
    open_("Een onderzoek vindt bij kinderen van 6 tot 12 jaar r = 0,8 tussen schoenmaat en leesscore. Iemand besluit dat grote voeten helpen bij lezen. Leg uit wat er mis is.",
          "Samenhang is geen oorzaak. De leeftijd is een derde factor: oudere kinderen hebben grotere voeten en lezen beter. Schoenmaat zelf veroorzaakt niets."),
]

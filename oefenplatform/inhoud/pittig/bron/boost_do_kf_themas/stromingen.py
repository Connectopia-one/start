"""Kunststromingen van de renaissance tot vandaag — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_stromingen: renaissance en barok, romantiek,
realisme en impressionisme, en de hedendaagse popart, installatiekunst,
multimediale en conceptuele kunst. Met vier zelfgetekende schilderijtjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, ROOD, LICHTGROEN, ORANJE

VS = Prent("vier-schilderijtjes", "Vier werken in een museum", "vier ingekaderde werken, letters A tot D")
KADERS = [("A", 60, 80), ("B", 520, 80), ("C", 60, 350), ("D", 520, 350)]
for t, x, y in KADERS:
    VS.rect(x - 12, y - 12, 444, 224, "#b08d57", DONKER, 4, 3)
    VS.rect(x, y, 420, 200, "#ffffff", DONKER, 0, 2)
# A: symmetrisch, lijnperspectief naar een verdwijnpunt (renaissance)
x, y = 60, 80
VS.rect(x, y, 420, 200, "#f2ead6", DONKER, 0, 2)
for dx in (0, 70, 140, 280, 350, 420):
    VS.lijn(x + dx, y + 200, x + 210, y + 90, GRIJS, 2)
VS.rect(x + 175, y + 55, 70, 70, "#ffffff", DONKER, 0, 2); VS.pad(f"M {x+175} {y+55} A 35 35 0 0 1 {x+245} {y+55}", "#9ec7e6", DONKER, 2)
VS.cirkel(x + 210, y + 110, 12, ROOD, DONKER, 2); VS.rect(x + 200, y + 122, 20, 40, ROOD, DONKER, 4, 2)
# B: diagonaal, hard licht-donker (barok)
x, y = 520, 80
VS.rect(x, y, 420, 200, "#2b2118", DONKER, 0, 2)
VS.pad(f"M {x} {y+200} L {x+420} {y} L {x+420} {y+60} L {x+60} {y+200} Z", "#f3d27a", "none", 0)
VS.cirkel(x + 170, y + 120, 16, "#f3dcc2", DONKER, 2); VS.lijn(x + 170, y + 136, x + 230, y + 180, ROOD, 10)
VS.cirkel(x + 290, y + 60, 14, "#f3dcc2", DONKER, 2); VS.lijn(x + 290, y + 74, x + 240, y + 130, BLAUW, 10)
# C: losse kleurtoetsen, licht op water (impressionisme)
x, y = 60, 350
VS.rect(x, y, 420, 200, "#cfe6f2", DONKER, 0, 2)
import random
rnd = random.Random(7)
for _ in range(160):
    xx, yy = x + 5 + rnd.random() * 405, y + 5 + rnd.random() * 185
    kl = rnd.choice(["#9ec7e6", "#f3d27a", "#a8c98a", "#e8a1a1", "#ffffff"])
    VS.svg(f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="9" ry="4" fill="{kl}" opacity="0.9"/>')
VS.cirkel(x + 320, y + 60, 26, "#f3a95a", "none", 0)
# D: herhaalde blikjes (popart)
x, y = 520, 350
for r in range(2):
    for k in range(5):
        bx, by = x + 52 + k * 72, y + 15 + r * 92
        VS.rect(bx, by, 56, 80, "#ffffff", DONKER, 4, 2)
        VS.rect(bx, by, 56, 32, ROOD, DONKER, 4, 2)
        VS.tekst(bx + 28, by + 58, "SOUP", 13, vet=True)
LET = {t: (x + 25, y + 25) for t, x, y in KADERS}
for t, (lx, ly) in LET.items():
    VS.letter(lx, ly, t)
U = "vier-schilderijtjes.svg"
Z = {t: [Prent.zone(x - 12, y - 12, 444, 224)] for t, x, y in KADERS}

VRAGEN = [
    klik("Bekijk de vier werken. Klik op het werk uit de renaissance.", U, Z["A"], "Rust, symmetrie en een lijnperspectief naar één verdwijnpunt."),
    klik("Klik op het barokke werk.", U, Z["B"], "Een diagonaal en een hard licht-donkercontrast."),
    klik("Klik op het impressionistische werk.", U, Z["C"], "Losse toetsen, licht en kleur: de indruk van een ogenblik."),
    klik("Klik op het werk uit de popart.", U, Z["D"], "Een massabeeld uit de winkel, herhaald."),
    volgorde("Zet de stromingen in de juiste volgorde, van oud naar jong.",
             ["renaissance", "barok", "romantiek", "realisme", "impressionisme", "popart"],
             "Elke stroming antwoordt op de vorige."),
    sorteer("Renaissance of barok?", ["renaissance", "barok"],
            [("evenwicht en rust", "renaissance"), ("beweging en drama", "barok"), ("lijnperspectief", "renaissance"), ("diagonale composities", "barok"), ("Leonardo da Vinci", "renaissance"), ("Rubens", "barok")],
            "De renaissance zoekt rust, de barok wil overtuigen."),
    sorteer("Welke moderne stroming?", ["romantiek", "realisme", "impressionisme"],
            [("een stormachtige zee met een klein schip", "romantiek"), ("zware veldarbeid zonder opsmuk", "realisme"), ("een zonsopgang in losse toetsen", "impressionisme"), ("verlangen naar een ver land", "romantiek"), ("arbeiders in een fabriek, zoals ze zijn", "realisme")],
            "Gevoel, het gewone leven, of de indruk van een ogenblik."),
    sorteer("Welke hedendaagse stroming?", ["popart", "installatiekunst", "conceptuele kunst", "multimediale kunst"],
            [("strips en reclamebeelden in het museum", "popart"), ("een zaal vol voorwerpen waar je tussen wandelt", "installatiekunst"), ("een instructie op een muur is het hele werk", "conceptuele kunst"), ("beeld, geluid en computer door elkaar", "multimediale kunst")],
            "Hedendaagse stromingen rekken het begrip kunst op."),
    keuze("Renaissance betekent [[*wedergeboorte|vernieuwing van de kerk|nieuwe kunst]]: van de klassieke oudheid.", "De Griekse en Romeinse vormen keren terug."),
    mk("Waarom paste de barok bij de kerk na de reformatie?",
       ["de kerk wilde gelovigen raken met pracht en emotie", "de kerk wilde zo goedkoop mogelijk nieuwe kerken bouwen", "de kerk verbood toen elke vorm van schilderkunst in kerken", "de kerk wilde enkel nog portretten van burgers"],
       0, "De barok wil overtuigen."),
    inv("Welk begrip zet de mens en zijn kunnen centraal in de renaissance? Eén woord.", ["humanisme", "het humanisme"], "Het humanisme."),
    tabel("Klopt dit over de stromingen?",
          [("De barok komt na de renaissance.", J), ("De impressionisten werden meteen geprezen.", F), ("Het realisme verfraaide het gewone leven.", F), ("Bij conceptuele kunst weegt het idee het zwaarst.", J)],
          "De naam impressionisme was eerst een spotnaam."),
    keuze("Het woord impressionisme komt van het Franse impression: [[*indruk|druk|uitdrukking]].", "De indruk van een ogenblik."),
    mk("Een kunstenaar hangt enkel een getypte tekst aan de muur: 'Stel je een blauwe kamer voor.' Welke stroming?",
       ["conceptuele kunst", "barok met veel drama en licht", "realisme van het gewone leven", "renaissance met perspectief"],
       0, "Het idee is de kunst, niet het voorwerp."),
    keuze("De popart haalt haar beelden vooral uit [[*de reclame en de strips|de Bijbel en de mythologie|de woeste natuur]].", "Massabeelden naar het museum."),
    mk("Waarom vraagt hedendaagse kunst vaak uitleg bij het werk?",
       ["het idee zit niet altijd zichtbaar in het voorwerp", "de kunstenaars schrijven graag lange teksten bij alles", "de werken zijn altijd heel oud en beschadigd", "er bestaan geen musea meer voor hedendaagse kunst"],
       0, "Hedendaagse stromingen stellen vragen aan de kijker."),
    koppel("Koppel de kunstenaar aan de stroming.",
           [("Michelangelo", "renaissance"), ("Rubens", "barok"), ("Andy Warhol", "popart")],
           ["gotiek"],
           "Warhol is de bekendste naam van de popart."),
    keuze("Bij installatiekunst hoort [[*de ruimte zelf|enkel het kader|de prijs]] bij het kunstwerk.", "De bezoeker stapt in het werk."),
    tabel("Hoort het bij de barok?",
          [("sterk licht-donkercontrast", J), ("overvloed en pracht", J), ("strakke symmetrie en rust", F), ("sterke emotie in de gezichten", J)],
          "Rust en symmetrie horen bij de renaissance."),
    mk("Het realisme schokte veel mensen. Waarom?",
       ["het toonde boeren en armoede zonder verfraaiing", "het gebruikte felle kleuren uit de reclame en de strips", "het liet het onderwerp van het schilderij helemaal weg", "het hing de schilderijen buiten in de regen op straat"],
       0, "Het gewone leven werd een onderwerp."),
    keuze("Hedendaagse kunst vraagt [[*niet altijd|altijd]] groot vakmanschap.", "Bij conceptuele kunst weegt het idee zwaarder."),
    sleep("De renaissance en de barok horen bij de [[vroegmoderne]] tijd. Romantiek, realisme en impressionisme horen bij de [[moderne]] tijd. Popart hoort bij de [[hedendaagse]] tijd.",
          ["middeleeuwse", "klassieke"], "Drie tijdvakken."),
    mk("Waarom helpt het om een stroming te kennen bij het analyseren?",
       ["je weet beter waarop je moet letten", "je hoeft het werk dan niet meer te bekijken", "je weet dan meteen de prijs van het werk", "je kent dan de naam van elke kunstenaar"],
       0, "Wie weet dat barok beweging zoekt, ziet die sneller."),
    keuze("Een romantisch schilderij toont vaak [[*de overweldigende natuur en een kleine mens|een blikje soep|een fabriek zoals ze is]].", "Gevoel, natuur en verlangen."),
    open_("Vergelijk de renaissance en de barok. Noem voor elk twee kenmerken.",
          "De renaissance zoekt rust en evenwicht en gebruikt het lijnperspectief. De barok zoekt beweging en drama, met diagonalen en een sterk licht-donkercontrast."),
    inv("Hoe heet de stroming die het gewone leven schildert zoals het is, zonder verfraaiing? Eén woord.", ["realisme", "het realisme"], "Het realisme."),
    keuze("In de renaissance lieten [[*ook rijke burgers|enkel heiligen|enkel vorsten]] zich portretteren.", "Het portret werd breder dan kerk en hof."),
    tabel("Is het een hedendaagse stroming?",
          [("popart", J), ("installatiekunst", J), ("romantiek", F), ("multimediale kunst", J), ("barok", F)],
          "Romantiek is modern, barok vroegmodern."),
    keuze("Het lijnperspectief laat alle lijnen samenkomen in [[*één verdwijnpunt|de hoeken van het doek|het midden van elke figuur]].", "Zo krijgt een vlak doek diepte."),
    mk("Een werk combineert videobeelden, muziek en lichteffecten die op de bezoeker reageren. Welke stroming?",
       ["multimediale kunst", "renaissance met lijnperspectief", "romantiek over de woeste natuur", "barok vol beweging en pracht"],
       0, "Ze combineert dragers: beeld, geluid, computer en licht."),
]

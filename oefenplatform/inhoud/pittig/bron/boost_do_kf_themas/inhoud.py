"""Samenlevingen, inhoud en context van een kunstuiting — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_inhoud: westerse en niet-westerse kunst
(Arabische en Afrikaanse kunst, japonisme), het onderwerp en de zeven
functies, en de context (tijd, ruimte, maatschappij, persoonlijke context).
Met vier zelfgetekende werken met een andere functie."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, ROOD, LICHTGROEN, ORANJE

FW = Prent("vier-functies", "Vier werken", "vier werken in een kader, letters A tot D")
KD = [("A", 60, 80), ("B", 520, 80), ("C", 60, 350), ("D", 520, 350)]
for t, x, y in KD:
    FW.rect(x, y, 420, 220, "#ffffff", DONKER, 6, 3)
# A: protestaffiche: fabriek met rook en een doodshoofdwolk
x, y = 60, 80
FW.rect(x + 60, y + 120, 120, 80, GRIJS, DONKER, 0, 2); FW.rect(x + 140, y + 70, 25, 50, GRIJS, DONKER, 0, 2)
for i in range(4):
    FW.cirkel(x + 160 + i * 40, y + 55 - i * 8, 22, "#555555", DONKER, 1)
FW.rect(x + 230, y + 120, 150, 70, ROOD, DONKER, 4, 2); FW.tekst(x + 305, y + 165, "STOP !", 30, kleur="#ffffff", vet=True)
# B: ruiterportret van een koning met kroon
x, y = 520, 80
BRUIN = "#8a6a4a"
for lx in (150, 175, 245, 270):
    FW.lijn(x + lx, y + 160, x + lx + (5 if lx < 200 else -5), y + 208, BRUIN, 9)
FW.ellips(x + 210, y + 145, 85, 32, BRUIN, DONKER, 3)
FW.pad(f"M {x+275} {y+135} L {x+305} {y+85} L {x+325} {y+95} L {x+300} {y+145} Z", BRUIN, DONKER, 3)
FW.ellips(x + 330, y + 88, 24, 13, BRUIN, DONKER, 3)
FW.pad(f"M {x+126} {y+140} Q {x+100} {y+160} {x+110} {y+195}", "none", DONKER, 5)
FW.rect(x + 192, y + 75, 34, 50, BLAUW, DONKER, 6, 2); FW.lijn(x + 200, y + 125, x + 195, y + 160, BLAUW, 8)
FW.cirkel(x + 209, y + 60, 15, "#f3dcc2", DONKER, 2)
FW.pad(f"M {x+194} {y+48} L {x+198} {y+32} L {x+209} {y+42} L {x+220} {y+32} L {x+224} {y+48} Z", GEEL, DONKER, 2)
# C: strip in vier vakjes
x, y = 60, 350
for k in range(4):
    FW.rect(x + 15 + k * 100, y + 30, 90, 160, "#fbf6ea", DONKER, 2, 2)
    FW.cirkel(x + 60 + k * 100, y + 110, 14, "#f3dcc2", DONKER, 2)
    FW.lijn(x + 60 + k * 100, y + 124, x + 60 + k * 100, y + 165, DONKER, 4)
    FW.pad(f"M {x+30+k*100} {y+45} h 60 v 30 h -40 l -8 10 v -10 h -12 Z", "#ffffff", DONKER, 2)
# D: behangpatroon
x, y = 520, 350
for r in range(4):
    for k in range(6):
        FW.cirkel(x + 85 + k * 60, y + 40 + r * 52, 14, LICHTGROEN if (r + k) % 2 == 0 else ORANJE, DONKER, 1)
        FW.pad(f"M {x+85+k*60} {y+26+r*52} l 6 -10 l 6 10", "none", DONKER, 1)
for t, x, y in KD:
    FW.letter(x + 25, y + 25, t)
U = "vier-functies.svg"
Z = {t: [Prent.zone(x, y, 420, 220)] for t, x, y in KD}

MASKER = ("Lees de tekst.\n\n"
          "In een Brussels museum hangt een houten masker uit Congo, gemaakt rond 1900. Het werd gedragen bij een ritueel "
          "voor de oogst, met muziek en dans. Rond 1910 kwam het naar België. Vandaag hangt het achter glas, met een bordje erbij. "
          "Een bezoeker vindt het vooral mooi en vraagt zich af wat het waard is.")

VRAGEN = [
    klik("Bekijk de vier werken. Klik op het werk met een maatschappijkritische functie.", U, Z["A"], "De affiche klaagt de vervuiling aan."),
    klik("Klik op het werk met vooral een politieke functie.", U, Z["B"], "Een koning te paard: kunst die macht toont."),
    klik("Klik op het werk met vooral een narratieve functie.", U, Z["C"], "Een strip vertelt een verhaal in vakjes."),
    klik("Klik op het werk met vooral een decoratieve functie.", U, Z["D"], "Een patroon dat versiert."),
    casus(MASKER, [
        keuze("Het masker is [[*Afrikaanse|Arabische|westerse]] kunst.", "Het komt uit Congo."),
        mk("Wat is er met de context van het masker gebeurd?",
           ["het ritueel en de plek zijn weggevallen", "het masker is van materiaal veranderd", "het onderwerp van het masker is veranderd", "er is niets veranderd aan de context"],
           0, "Het werd gemaakt voor een oogstritueel en hangt nu achter glas."),
        sorteer("Welk deel van de context?", ["tijd", "ruimte", "maatschappelijke context"],
                [("rond 1900", "tijd"), ("in Congo, bij een dorpsfeest", "ruimte"), ("een ritueel voor de oogst", "maatschappelijke context")],
                "Wanneer, waar, en wat er in de samenleving speelde."),
        keuze("De bezoeker die vraagt wat het masker waard is, denkt aan de [[*economische|narratieve|filosofische]] functie.", "Kunst is ook handel."),
    ]),
    tabel("Is dit een van de zeven functies?",
          [("de ontspannende", J), ("de wetenschappelijke", F), ("de filosofische", J), ("de economische", J), ("de sportieve", F)],
          "Decoratief, economisch, filosofisch, maatschappijkritisch, narratief, ontspannend en politiek."),
    koppel("Koppel het werk aan de functie.",
           [("een stilleven met verwelkte bloemen en een schedel", "filosofisch"), ("een komische film voor de zomer", "ontspannend"), ("een standbeeld van een generaal op een plein", "politiek"), ("een schilderij dat voor miljoenen geveild wordt", "economisch")],
           ["wetenschappelijk"],
           "Eén werk kan ook meerdere functies hebben."),
    mk("Een portret van een koning. Wat is het onderwerp en wat de functie?",
       ["onderwerp: de koning; functie: zijn macht tonen", "onderwerp: zijn macht; functie: de koning tonen", "onderwerp en functie zijn hier precies hetzelfde", "onderwerp: de schilder; functie: geld verdienen"],
       0, "Het onderwerp is wat je ziet, de functie waarvoor het diende."),
    sorteer("Westers of niet-westers?", ["westers", "niet-westers"],
            [("een gotisch glasraam", "westers"), ("Arabische kalligrafie op een tegel", "niet-westers"), ("een Afrikaans masker", "niet-westers"), ("een renaissancefresco", "westers")],
            "Arabische en Afrikaanse kunst zijn niet-westers."),
    keuze("Het japonisme is [[*een westerse stroming die Japanse prenten als voorbeeld nam|een Japanse stroming uit de middeleeuwen|kunst die in Japan verboden was]].", "Vlakke kleur en een afgesneden beeld."),
    tabel("Hoort het typisch bij Arabische kunst?",
          [("geometrische patronen", J), ("kalligrafie als versiering", J), ("arabesken", J), ("grotschilderingen van stieren", F)],
          "Grotschilderingen zijn prehistorisch."),
    sorteer("Welke richtvraag?", ["hoe en waarmee", "wat", "waarvoor", "wie, waar en wanneer"],
            [("Welk materiaal gebruikte de maker?", "hoe en waarmee"), ("Wat is er te zien?", "wat"), ("Diende het om een verhaal te vertellen?", "waarvoor"), ("In welke stad hing het?", "wie, waar en wanneer")],
            "De functie hoort bij waarvoor, de context bij wie, waar en wanneer."),
    mk("Een schilderij uit 1916 toont een verwoest dorp. Welke context verklaart het onderwerp het best?",
       ["de maatschappelijke: de Eerste Wereldoorlog", "de persoonlijke: de kleur die de schilder het liefst had", "de ruimte: het museum waar het nu hangt", "de economische waarde van het schilderij vandaag"],
       0, "De oorlog woedde toen het werk ontstond."),
    keuze("Een kunstenaar schildert donkere werken na de dood van zijn vrouw. Dat is de [[*persoonlijke|maatschappelijke|ruimtelijke]] context.", "Zijn eigen leven stuurt het werk."),
    tabel("Klopt dit over inhoud en context?",
          [("Eén kunstwerk kan meerdere functies hebben.", J), ("Een werk dat enkel versiert, is geen kunst.", F), ("Onderwerp en functie zijn hetzelfde.", F), ("De betekenis van een werk kan veranderen in de tijd.", J)],
          "De decoratieve functie staat gewoon bij de zeven."),
    mk("Waarom vertelde veel kerkelijke kunst in de middeleeuwen een verhaal in beelden?",
       ["veel mensen konden niet lezen", "verf was goedkoper dan perkament en inkt", "de kerk verbood alle boeken", "de kunstenaars hielden niet van schrijven"],
       0, "De narratieve functie."),
    keuze("Het land, de stad of de plek waar een werk hing, hoort bij de [[*ruimte|tijd|persoonlijke context]].", "De ruimte antwoordt op waar."),
    mk("Een kunstenaar schildert in 1940 een kapotte stad. Waarom helpt dat jaartal?",
       ["de context verklaart de keuze van het onderwerp", "het jaartal bepaalt de prijs van het schilderij", "het jaartal zegt welke verf de schilder gebruikte", "het jaartal is altijd het belangrijkste onderwerp"],
       0, "Inhoud en context verklaren elkaar."),
    keuze("Een spotprent zonder kennis van de gebeurtenis zegt weinig: de [[*context|kleur|compositie]] maakt de boodschap leesbaar.", "Zonder context kan je een werk verkeerd begrijpen."),
    sleep("De inhoud van een werk is het [[onderwerp]] plus de [[functies]]. De context bestaat uit tijd, [[ruimte]], de maatschappij en de persoonlijke context van de kunstenaar.",
          ["materiaal", "techniek"], "Materiaal en techniek horen bij de vormgeving."),
    mk("Een protestlied tegen oorlog. Welke functie staat voorop?",
       ["de maatschappijkritische", "de decoratieve", "de economische", "de politieke van een heerser"],
       0, "De kunstenaar houdt de samenleving een spiegel voor."),
    open_("Kies een werk dat je kent en benoem het onderwerp en twee functies.",
          "Een schilderij van een veldslag met de koning vooraan. Onderwerp: de veldslag. Functies: politiek, want het toont de macht van de koning, en narratief, want het vertelt wat er gebeurde."),
    keuze("Je bekijkt kunst uit meerdere samenlevingen, omdat [[*elke samenleving kunst kent|enkel westerse kunst echt telt|Afrikaanse kunst ouder is]].", "Met eigen vormen, materialen en bedoelingen."),
    inv("Hoeveel functies van een kunstuiting staan er in de lijst? Schrijf het getal.", ["7", "zeven"], "Zeven functies."),
    tabel("Hoort de vraag bij de context?",
          [("Wie maakte het?", J), ("Waar werd het gemaakt?", J), ("Met welk materiaal?", F), ("Wanneer ontstond het?", J)],
          "Materiaal hoort bij hoe en waarmee."),
    mk("Een tegel met een herhaald sterrenpatroon in een moskee. Welke functie staat voorop?",
       ["de decoratieve", "de politieke van een koning", "de maatschappijkritische", "de economische van de handel"],
       0, "Arabische kunst werkt veel met versierende patronen."),
    keuze("Een werk dat een vraag over de dood of de zin van het leven oproept, heeft een [[*filosofische|decoratieve|economische]] functie.", "Het zet de kijker aan het denken."),
]

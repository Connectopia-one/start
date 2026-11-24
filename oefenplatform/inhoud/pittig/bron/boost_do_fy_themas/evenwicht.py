"""Archimedeskracht, moment en evenwicht — pittig (🚀 Boost doorstroom, fysica).

Eigen vragen strikt binnen fy_evenwicht, met een zelfgetekende lat met draaipunt om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER

# Lat met draaipunt: elke 100 px is 0,20 m ------------------------------------
LAT = Prent("lat-draaipunt", "Lat met draaipunt", "horizontale lat op een draaipunt in het midden, met een gewicht van 60 N links en letters op de rechterhelft")
LAT.rect(90, 290, 820, 20, "#e8c99a", DONKER, 6)
LAT.pad("M 500 310 L 460 390 L 540 390 Z", GRIJS, DONKER, 2)
LAT.lijn(380, 420, 1000, 420, DONKER, 0)
for i, x in enumerate(range(100, 901, 100)):
    LAT.lijn(x, 280, x, 320, DONKER, 2)
    LAT.tekst(x, 270, f"{abs(x - 500) // 100 * 0.2:.1f}".replace(".", ",") + " m" if x != 500 else "0", 16)
LAT.lijn(200, 310, 200, 380, DONKER, 2)
LAT.rect(165, 380, 70, 60, ORANJE, DONKER, 6)
LAT.tekst(200, 418, "60 N", 18, kleur="#ffffff", vet=True)
for x, t in [(300, "A"), (400, "B"), (600, "C"), (700, "D"), (800, "E"), (900, "F")]:
    LAT.letter(x, 200, t)
U = "lat-draaipunt.svg"
Z = {t: Prent.zone(x - 45, 150, 90, 190) for x, t in [(300, "A"), (400, "B"), (600, "C"), (700, "D"), (800, "E"), (900, "F")]}

VRAGEN = [
    klik("Het gewicht van 60 N hangt op 0,60 m links van het draaipunt. Klik op de plaats waar je 90 N moet hangen om de lat in evenwicht te brengen.", U, [Z["D"]],
         "60 · 0,60 = 36 Nm, dus d = 36 / 90 = 0,40 m rechts."),
    klik("Klik op de plaats waar je 180 N moet hangen voor evenwicht met het gewicht van 60 N.", U, [Z["C"]],
         "36 Nm / 180 N = 0,20 m rechts van het draaipunt."),
    klik("Klik op de plaats waar een kracht van 45 N naar beneden de lat in evenwicht houdt.", U, [Z["F"]],
         "36 / 45 = 0,80 m: helemaal aan het rechteruiteinde."),
    casus("Een houten blok van 2,0 kg met een volume van 0,0025 m³ wordt in water gelegd. Neem g = 10 N/kg en ρ water = 1000 kg/m³.", [
        inv("Hoe groot is de zwaartekracht op het blok, in newton?", ["20", "20 N"],
            "Fz = m · g = 2,0 · 10 = 20 N."),
        inv("Hoe groot zou de archimedeskracht zijn als het blok helemaal onder water zat, in newton?", ["25", "25 N"],
            "FA = 1000 · 10 · 0,0025 = 25 N."),
        mk("Wat doet het blok als je het loslaat onder water?",
           ["het stijgt en gaat drijven", "het zinkt naar de bodem", "het zweeft op dezelfde diepte", "het draait rond zijn zwaartepunt"], 0,
           "De archimedeskracht van 25 N is groter dan de zwaartekracht van 20 N."),
        inv("Welk volume zit er onder water als het blok drijft, in m³?", ["0,0020", "0,002", "0.002", "0.0020"],
            "Bij drijven is FA = Fz = 20 N, dus Vond = 20 / (1000 · 10) = 0,0020 m³."),
    ]),
    sorteer("Zinkt, zweeft of stijgt het voorwerp in water (1000 kg/m³)?", ["zinkt", "zweeft", "stijgt"],
            [("een blok ijzer van 7900 kg/m³", "zinkt"), ("een kurk van 240 kg/m³", "stijgt"), ("een vis met een gemiddelde massadichtheid van 1000 kg/m³", "zweeft"), ("een steen van 2600 kg/m³", "zinkt"), ("een stuk hout van 700 kg/m³", "stijgt")],
            "Vergelijk de massadichtheid van het voorwerp met die van water."),
    tabel("Een ei zinkt in kraantjeswater en drijft in zeer zout water. Klopt dit?",
          [("Zout water heeft een grotere massadichtheid.", J), ("In zout water is de archimedeskracht bij hetzelfde ondergedompelde volume groter.", J), ("Het ei wordt lichter in zout water.", F)],
          "De zwaartekracht op het ei verandert niet; ρ van de vloeistof wel."),
    inv("Een steen van 30 N wijst in water 18 N aan op een dynamometer. Wat is het volume van de steen in liter, met g = 10 N/kg?", ["1,2", "1.2", "1,2 L"],
        "FA = 12 N, dus V = 12 / (1000 · 10) = 0,0012 m³ = 1,2 L."),
    mk("Een ballon met helium stijgt in de lucht. Waarom?",
       ["De archimedeskracht van de lucht is groter dan zijn gewicht.", "Helium heeft geen massa en wordt niet aangetrokken.", "De zwaartekracht werkt niet op gassen in een ballon.", "De druk van het helium in de ballon duwt hem van de grond weg."], 0,
       "Ook een gas geeft een archimedeskracht: de ballon duwt meer lucht weg dan hij zelf weegt."),
    tabel("Klopt dit over het moment van een kracht?",
          [("Een kracht van 50 N loodrecht op 0,30 m geeft 15 Nm.", J), ("Een kracht langs de arm geeft geen moment.", J), ("Bij 30° is het moment de helft van dat bij 90°.", J), ("Een moment van 15 Nm is 15 J.", F)],
          "M = F · d · sin α; sin 30° = 0,5; het moment drukt men uit in Nm, niet in J."),
    inv("Je duwt met 20 N op een deurklink, 0,80 m van de scharnieren, onder een hoek van 30° met de deur. Hoe groot is het moment in Nm?", ["8", "8,0", "8 Nm"],
        "M = 20 · 0,80 · sin 30° = 20 · 0,80 · 0,5 = 8,0 Nm."),
    casus("Een balk van 4,0 m en 200 N ligt op twee steunpunten aan de uiteinden. In het midden staat een kist van 600 N.", [
        inv("Hoe groot is de som van de twee steunkrachten, in newton?", ["800", "800 N"],
            "Translatie-evenwicht: de steunkrachten dragen samen 200 + 600 = 800 N."),
        inv("Hoe groot is elke steunkracht, in newton?", ["400", "400 N"],
            "Alles ligt symmetrisch, dus elk steunpunt draagt de helft."),
        tabel("Je schuift de kist naar het linker steunpunt. Klopt dit?",
              [("De linker steunkracht wordt groter.", J), ("De som van de steunkrachten blijft 800 N.", J), ("De rechter steunkracht wordt groter.", F)],
              "Het totaal verandert niet, maar het steunpunt het dichtst bij de kist draagt meer."),
    ]),
    keuze("Je opent een deur het makkelijkst door te duwen [[*ver van de scharnieren|dicht bij de scharnieren|op de scharnieren]].",
          "Een grotere krachtarm geeft bij dezelfde kracht een groter moment."),
    sorteer("Maakt dit een voorwerp stabieler of minder stabiel?", ["stabieler", "minder stabiel"],
            [("een lager zwaartepunt", "stabieler"), ("een breder steunvlak", "stabieler"), ("zware bagage bovenop het dak", "minder stabiel"), ("een smaller steunvlak", "minder stabiel")],
            "Het zwaartepunt moet boven het steunvlak blijven; laag en breed is het stabielst."),
    sleep("Bij statisch evenwicht is de som van alle [[krachten]] nul, zodat het voorwerp niet verschuift, en de som van alle [[momenten]] nul, zodat het niet [[draait]].",
          ["massa's", "versnelt"], "Translatie- en rotatie-evenwicht samen."),
    mk("Een kind van 25 kg zit op 1,6 m van het draaipunt van een wip. Waar moet een volwassene van 80 kg zitten?",
       ["op 0,50 m", "op 1,6 m", "op 5,1 m", "op 0,80 m"], 0,
       "25 · 1,6 = 80 · d, dus d = 40 / 80 = 0,50 m. De g valt weg aan beide kanten."),
    tabel("Klopt dit over de archimedeskracht?",
          [("Ze werkt ook op een voorwerp in een gas.", J), ("Ze hangt af van de massa van het voorwerp.", F), ("Een half ondergedompeld voorwerp krijgt de helft van de kracht bij volledig onderdompelen.", J)],
          "Enkel ρ van de vloeistof of het gas, g en het ondergedompelde volume tellen."),
    inv("Een kracht van 50 N werkt onder 90° op een sleutel en geeft 15 Nm. Hoe lang is de krachtarm in centimeter?", ["30", "30 cm"],
        "d = M / F = 15 / 50 = 0,30 m = 30 cm."),
    koppel("Welke situatie hoort bij welke toestand?",
           [("FA > Fz bij volledig onderdompelen", "stijgen"), ("FA < Fz bij volledig onderdompelen", "zinken"), ("FA = Fz, volledig onder water", "zweven"), ("FA = Fz, deels boven water", "drijven")],
           [], "De krachtenbalans tussen archimedeskracht en zwaartekracht beslist."),
    mk("Twee kinderen trekken met 40 N aan elk uiteinde van een lat, in tegengestelde zin en loodrecht op de lat. Wat gebeurt er?",
       ["De lat begint te draaien.", "De lat blijft in volledig evenwicht.", "De lat schuift in de zin van één kind.", "De lat versnelt langs haar lengte."], 0,
       "De som van de krachten is nul, maar de momenten tellen op: geen rotatie-evenwicht."),
    inv("Hoe groot is de archimedeskracht op een volledig ondergedompeld blok van 3,0 L in olie met ρ = 800 kg/m³, met g = 10 N/kg, in newton?", ["24", "24 N"],
        "FA = 800 · 10 · 0,0030 = 24 N."),
    tabel("Een duikboot stijgt naar de oppervlakte. Klopt dit?",
          [("Ze perst water uit haar tanks.", J), ("Haar volume wordt daarbij veel groter.", F), ("Haar zwaartekracht wordt kleiner dan de archimedeskracht.", J)],
          "Minder water in de tanks betekent minder massa bij hetzelfde volume."),
    volgorde("Rangschik de momenten van klein naar groot.",
             ["10 N op 0,20 m", "20 N op 0,20 m", "10 N op 0,50 m", "30 N op 0,40 m"],
             "Telkens loodrecht: 2, 4, 5 en 12 Nm."),
    mk("Waarom heeft een kraan op een werf een zwaar tegengewicht?",
       ["om het moment van de last op te heffen", "om de last sneller omhoog te trekken", "om de archimedeskracht van de lucht te vergroten", "om de massa van de last kleiner te maken"], 0,
       "Het tegengewicht geeft een moment in de andere zin, zodat de kraan niet kantelt."),
    keuze("Een kracht die door het draaipunt gaat, geeft een moment van [[*0 Nm|F · d Nm|1 Nm]].",
          "De krachtarm is dan nul."),
    inv("Een plank van 2,0 m draait rond haar linker uiteinde. Rechts trekt een koord loodrecht omhoog. In het midden werkt de zwaartekracht van 100 N. Hoe groot moet de kracht in het koord zijn, in newton?", ["50", "50 N"],
        "100 · 1,0 = F · 2,0, dus F = 50 N."),
]

"""Woordvelden: mens, gezondheid en het dagelijkse leven — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_dagelijks: familie, gevoelens, gezondheid en
lichaamsdelen, eten, kleding, de woning, de dagelijkse bezigheden en
materialen. Met een zelfgetekend lichaam en een huis in doorsnede."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, GEEL, ORANJE, BLAUW

HUID = "#f3dcc2"
LI = Prent("lichaam-letters", "Le corps", "een figuur met letters A tot F bij lichaamsdelen")
LI.cirkel(500, 120, 50, HUID, DONKER, 3)
LI.rect(475, 168, 50, 30, HUID, DONKER, 4, 3)
LI.rect(420, 195, 160, 190, BLAUW, DONKER, 18, 3)
LI.lijn(425, 210, 340, 380, DONKER, 16); LI.lijn(575, 210, 660, 380, DONKER, 16)
LI.cirkel(335, 395, 16, HUID, DONKER, 3); LI.cirkel(665, 395, 16, HUID, DONKER, 3)
LI.rect(430, 380, 60, 200, GRIJS, DONKER, 8, 3); LI.rect(510, 380, 60, 200, GRIJS, DONKER, 8, 3)
LI.rect(415, 580, 80, 25, DONKER, DONKER, 8, 2); LI.rect(505, 580, 80, 25, DONKER, DONKER, 8, 2)
PL = {"A": (430, 205), "B": (338, 362), "C": (460, 480), "D": (540, 565), "E": (500, 185), "F": (620, 290)}
PUNT = {"A": (440, 210), "B": (345, 370), "C": (460, 480), "D": (540, 570), "E": (500, 185), "F": (615, 290)}
LBL = {"A": (360, 190), "B": (260, 360), "C": (360, 480), "D": (650, 560), "E": (630, 170), "F": (720, 290)}
for t in PL:
    LI.lijn(*LBL[t], *PUNT[t], DONKER, 2)
    LI.letter(*LBL[t], t)
U1 = "lichaam-letters.svg"
Z1 = {t: [Prent.rond(*LBL[t], 30), Prent.rond(*PUNT[t], 30)] for t in PL}

HS = Prent("huis-doorsnede", "Une maison", "een huis in doorsnede met vier ruimtes, letters A tot D")
HS.pad("M 200 230 L 500 70 L 800 230 Z", ORANJE, DONKER, 3)
HS.rect(200, 230, 600, 360, "#ffffff", DONKER, 0, 4)
HS.lijn(200, 410, 800, 410, DONKER, 4); HS.lijn(500, 230, 500, 590, DONKER, 4)
HS.lijn(200, 590, 800, 590, DONKER, 4)
HS.rect(240, 330, 180, 60, BLAUW, DONKER, 6, 2); HS.rect(240, 300, 40, 40, "#ffffff", DONKER, 6, 2)   # bed
HS.rect(540, 340, 60, 70, GRIJS, DONKER, 2, 2); HS.cirkel(570, 330, 18, "#ffffff", DONKER, 2)          # wc
HS.rect(620, 350, 150, 58, "#9ec7e6", DONKER, 20, 2); HS.lijn(760, 350, 760, 300, DONKER, 4); HS.lijn(760, 300, 735, 300, DONKER, 4); HS.cirkel(730, 305, 9, GRIJS, DONKER, 2)  # bad
HS.rect(240, 500, 200, 90, LICHTGROEN, DONKER, 14, 2)                                                 # zetel
HS.rect(560, 520, 200, 70, GRIJS, DONKER, 2, 2); HS.cirkel(610, 515, 14, DONKER, DONKER, 1); HS.cirkel(660, 515, 14, DONKER, DONKER, 1)  # fornuis
HS.rect(690, 440, 70, 50, GRIJS, DONKER, 2, 2)
LETS = {"A": (330, 260), "B": (650, 260), "C": (330, 440), "D": (650, 440)}
for t, (x, y) in LETS.items():
    HS.letter(x, y, t)
U2 = "huis-doorsnede.svg"
Z2 = {"A": [Prent.zone(200, 230, 300, 180)], "B": [Prent.zone(500, 230, 300, 180)], "C": [Prent.zone(200, 410, 300, 180)], "D": [Prent.zone(500, 410, 300, 180)]}

DOKTER = ("Lees het gesprek bij de dokter.\n\n"
          "« — Bonjour, Madame. Qu'est-ce qui ne va pas ?\n"
          "— Depuis trois jours, j'ai mal à la gorge et j'ai de la fièvre. La nuit, je tousse beaucoup et je suis très fatiguée.\n"
          "— Vous avez pris quelque chose ?\n"
          "— Seulement du thé chaud avec du miel.\n"
          "— Bon. Je vous fais une ordonnance. Prenez ce médicament trois fois par jour, après les repas, et restez au lit deux jours. »")

VRAGEN = [
    klik("Bekijk de figuur. Klik op la cheville.", U1, Z1["D"], "La cheville is de enkel."),
    klik("Klik op le poignet.", U1, Z1["B"], "Le poignet is de pols."),
    klik("Klik op l'épaule.", U1, Z1["A"], "L'épaule is de schouder."),
    klik("Klik op le genou.", U1, Z1["C"], "Le genou is de knie."),
    klik("Klik op le cou.", U1, Z1["E"], "Le cou is de hals."),
    klik("Bekijk het huis. Klik op la salle de bains.", U2, Z2["B"], "Het bad en het toilet staan in de badkamer."),
    klik("Klik op la cuisine.", U2, Z2["D"], "Het fornuis staat in de keuken."),
    casus(DOKTER, [
        tabel("Heeft de vrouw dit?",
              [("keelpijn", J), ("koorts", J), ("buikpijn", F), ("een hoest", J)],
              "Mal à la gorge, de la fièvre, je tousse. Over haar buik zegt ze niets."),
        inv("Sinds hoeveel dagen is ze ziek? Schrijf het cijfer.", ["3"], "Depuis trois jours: sinds drie dagen."),
        keuze("'Une ordonnance' is [[*een voorschrift|een afspraak|een ziekenhuis]].", "Daarmee haal je het geneesmiddel bij de apotheek."),
        mk("Wanneer moet ze het geneesmiddel nemen?",
           ["drie keer per dag, na het eten", "drie keer per dag, vóór het eten van 's middags", "één keer per dag, 's avonds in bed", "twee dagen lang enkel 's nachts"],
           0, "Trois fois par jour, après les repas."),
        keuze("'Je suis très fatiguée': ze is [[*heel moe|heel boos|heel blij]].", "Fatigué: moe."),
    ]),
    sorteer("Hoe zeg je het in het Frans?", ["avoir", "être"],
            [("honger hebben: … faim", "avoir"), ("bang zijn: … peur", "avoir"), ("blij zijn: … content", "être"), ("vijftien jaar zijn: … quinze ans", "avoir"), ("moe zijn: … fatigué", "être"), ("zich schamen: … honte", "avoir")],
            "Honger, dorst, angst, schaamte en je leeftijd heb je in het Frans."),
    koppel("Koppel het familielid aan de uitleg.",
           [("une nièce", "de dochter van je broer of zus"), ("une cousine", "de dochter van je oom of tante"), ("une belle-mère", "de moeder van je partner of de nieuwe partner van je vader"), ("un petit-fils", "de zoon van je zoon of dochter")],
           ["de zus van je moeder"],
           "Beau- en belle- betekenen aangetrouwd."),
    sorteer("Welk woordveld?", ["kleding", "materiaal", "kamer"],
            [("une jupe", "kleding"), ("le cuir", "materiaal"), ("le grenier", "kamer"), ("une chemise", "kleding"), ("le bois", "materiaal"), ("la cave", "kamer")],
            "Le cuir is leer, le grenier de zolder."),
    keuze("Hij heeft zijn been gebroken: Il s'est cassé [[*la|sa]] jambe.", "Bij lichaamsdelen gebruikt het Frans het lidwoord."),
    mk("'Des chaussures marron' — waarom krijgt marron geen s?",
       ["marron is de naam van een ding en blijft onveranderd", "chaussures is een mannelijk woord in het Frans, dus geen s", "kleuren krijgen in het Frans nooit een s in het meervoud", "na des valt de s van een kleur altijd weg"],
       0, "Zoals orange: des murs orange."),
    tabel("Klopt dit over het dagelijkse leven?",
          [("Les cheveux zijn haren.", J), ("Faire la vaisselle is de was doen.", F), ("Le rez-de-chaussée is het gelijkvloers.", J), ("Une serviette kan een handdoek zijn.", J)],
          "Faire la vaisselle is de afwas doen; de was is la lessive."),
    volgorde("Zet de ochtend van Lina in de juiste volgorde.",
             ["Elle se réveille.", "Elle se lève.", "Elle se douche.", "Elle s'habille.", "Elle prend son petit déjeuner."],
             "Wakker worden, opstaan, douchen, aankleden, ontbijten."),
    inv("Vul in: Nous nous … à sept heures. Vorm van se lever.", ["levons"], "Nous nous levons: zonder accent, de klemtoon valt op -ons."),
    mk("Wat betekent 'Ne t'inquiète pas' ?",
       ["maak je geen zorgen", "wees niet zo boos op mij", "ga nog niet naar bed", "vergeet het niet"],
       0, "S'inquiéter: zich zorgen maken."),
    keuze("Elle est [[*en pleine forme|malade|enrhumée]]: ze voelt zich uitstekend.", "En pleine forme: in topvorm."),
    sleep("Op de markt: J'achète un kilo de [[pommes]], du [[pain]] et un pot de [[confiture]].",
          ["chaise", "jupe"], "Fruit, brood en confituur."),
    open_("Beschrijf in het Frans in twee zinnen wat je vanmorgen gedaan hebt.",
          "Je me suis levé à sept heures. Ensuite, j'ai pris une douche et j'ai mangé une tartine."),
    inv("Vul in: J'ai mal … dents. Eén woord.", ["aux"], "À + les = aux: j'ai mal aux dents."),
    tabel("Is dit een kledingstuk?",
          [("un pantalon", J), ("une robe", J), ("une poêle", F), ("un canapé", F)],
          "Une poêle is een pan, un canapé een zetel."),
    keuze("Het juist gespelde Franse woord is [[*appartement|apartement|appartment]].", "Dubbele p, één t."),
    mk("Je moeder roept: 'Range ta chambre !' Wat moet je doen?",
       ["je kamer opruimen", "je kamer verven in een nieuwe kleur", "in je kamer blijven tot het eten", "je kamer afsluiten met de sleutel"],
       0, "Ranger: op zijn plaats zetten."),
    keuze("Le premier étage is [[*de verdieping boven het gelijkvloers|het gelijkvloers|de kelder]].", "Het gelijkvloers is le rez-de-chaussée."),
    sorteer("Hoort dit bij het ontbijt of bij het warme eten?", ["ontbijt", "warm eten"],
            [("le pain", "ontbijt"), ("la confiture", "ontbijt"), ("le poulet", "warm eten"), ("les légumes", "warm eten")],
            "Le poulet is kip."),
]

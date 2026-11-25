"""Zelfstandige naamwoorden, lidwoorden en determinanten — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_naamwoorden: geslacht en meervoud, de vier
soorten lidwoorden, de na een hoeveelheid, een ontkenning en voor een
bijvoeglijk naamwoord, lidwoorden bij lichaamsdelen en landen, de
determinanten en de telwoorden. Met een zelfgetekend boodschappenlijstje."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GEEL

BL = Prent("boodschappenlijst", "La liste de courses de Chloé", "een lijstje met zes regels, letters A tot F")
BL.rect(240, 55, 520, 570, "#fffbe6", DONKER, 8, 3)
for y in range(150, 600, 70):
    BL.lijn(260, y + 15, 740, y + 15, "#e4e1d6", 2)
RG = [("A", 150, "un kilo de pommes"), ("B", 220, "trois bouteilles d'eau"), ("C", 290, "beaucoup des tomates"),
      ("D", 360, "du fromage de chèvre"), ("E", 430, "de belles fraises"), ("F", 500, "pas de viande cette fois")]
for t, y, r in RG:
    BL.letter(290, y - 7, t)
    BL.tekst(330, y, r, 26, "start")
BL.tekst(500, 105, "Courses du samedi", 26, vet=True)
U = "boodschappenlijst.svg"
Z = {t: [Prent.zone(255, y - 40, 490, 60)] for t, y, _ in RG}

VRAGEN = [
    klik("Chloé maakte één fout in haar lijstje. Klik op die regel.", U, Z["C"], "Na beaucoup komt de zonder lidwoord: beaucoup de tomates."),
    klik("Klik op de regel met een deelaanduidend lidwoord.", U, Z["D"], "Du fromage: een onbepaalde hoeveelheid kaas."),
    klik("Klik op de regel waar des de wordt omdat er een bijvoeglijk naamwoord vóór het meervoud staat.", U, Z["E"], "De belles fraises, niet des belles fraises."),
    klik("Klik op de regel waar het lidwoord verdwijnt door een ontkenning.", U, Z["F"], "Pas de viande: na pas wordt du, de la en des gewoon de."),
    sorteer("Welk soort lidwoord?", ["bepaald", "onbepaald", "deelaanduidend", "samengetrokken"],
            [("les", "bepaald"), ("l'", "bepaald"), ("des (bij un livre)", "onbepaald"), ("de la", "deelaanduidend"), ("au", "samengetrokken"), ("aux", "samengetrokken")],
            "De la is deelaanduidend; au is à + le."),
    tabel("Is het meervoud juist?",
          [("des journaux", J), ("des chevals", F), ("des yeux", J), ("des jeux", J), ("des gâteaus", F)],
          "Un cheval wordt des chevaux, un gâteau des gâteaux."),
    sleep("Op vakantie: Nous allons [[au]] Canada et ensuite [[aux]] États-Unis. Après, nous rentrons [[en]] Belgique.",
          ["à la", "du"], "Au bij een mannelijk land, aux bij een meervoud, en bij een vrouwelijk land."),
    mk("Welke zin over de auto is juist?",
       ["Il n'a pas de voiture.", "Il n'a pas une voiture rouge en ce moment.", "Il n'a pas des voitures chez lui.", "Il n'a pas du temps pour sa voiture."],
       0, "Na pas wordt un, des en du gewoon de."),
    keuze("Ce n'est pas [[*du|de]] café, c'est du thé.", "Na être blijft het lidwoord staan."),
    inv("Zet in het meervoud: un animal. Twee woorden.", ["des animaux"], "-al wordt -aux."),
    keuze("Hij steekt zijn hand op: Il lève [[*la|sa|une]] main.", "Bij lichaamsdelen het bepaald lidwoord."),
    tabel("Mannelijk of vrouwelijk?",
          [("problème", "mannelijk"), ("musée", "mannelijk"), ("maison", "vrouwelijk"), ("système", "mannelijk"), ("fois", "vrouwelijk")],
          "Niet elk woord op -e is vrouwelijk.", ["mannelijk", "vrouwelijk"]),
    sorteer("Welk aanwijzend determinant?", ["ce", "cet", "cette", "ces"],
            [("… livre", "ce"), ("… hôtel", "cet"), ("… école", "cette"), ("… enfants", "ces"), ("… garçon", "ce"), ("… ami", "cet")],
            "Cet voor een mannelijk woord met een klinker of stomme h."),
    keuze("Mijn school: [[*mon|ma|mes]] école.", "Voor een klinker wordt ma mon."),
    keuze("'Paul et sa sœur': Paul en [[*zijn|haar|hun]] zus.", "Sa hoort bij sœur; de eigenaar is Paul."),
    sorteer("Leur of leurs?", ["leur", "leurs"],
            [("Les enfants rangent … chambre (één kamer samen).", "leur"), ("Les élèves prennent … livres.", "leurs"), ("Je … parle souvent.", "leur"), ("Mes voisins vendent … voitures.", "leurs")],
            "Leur voor een werkwoord krijgt nooit een s."),
    sorteer("Quel, quelle, quels of quelles?", ["quel", "quelle", "quels", "quelles"],
            [("… âge as-tu ?", "quel"), ("… heure est-il ?", "quelle"), ("… sports aimes-tu ?", "quels"), ("… langues parles-tu ?", "quelles")],
            "Quel past zich aan het naamwoord aan."),
    keuze("[[*Tout le monde est|Tout le monde sont]] là.", "Tout le monde is enkelvoud."),
    inv("Vul in: … les semaines, je vais à la piscine. Eén woord.", ["Toutes", "toutes"], "Semaines is vrouwelijk meervoud."),
    tabel("Is het rangtelwoord juist gespeld?",
          [("neuvième", J), ("neufième", F), ("cinquième", J), ("unième", F)],
          "Neuf wordt neuv-, cinq krijgt een u; bij één zeg je premier."),
    tabel("Klopt de datum?",
          [("le 1er mai", J), ("le 2e mai", F), ("le 15 août", J), ("le premier janvier", J)],
          "Enkel de eerste van de maand krijgt een rangtelwoord."),
    inv("Hoe zeg je 'voor de tweede keer'? Vul in: pour la … fois.", ["deuxième", "seconde"], "Fois is vrouwelijk: la deuxième fois."),
    mk("Je leest: 'les livres de la bibliothèque'. Waaraan zie je dat het om meerdere boeken gaat?",
       ["aan het lidwoord les", "aan het woord bibliothèque", "aan het woord de la", "je kan het niet zien"],
       0, "In het Frans zit het getal vaak alleen in het woordje vooraan."),
    sorteer("Welke betekenis?", ["enkele", "verschillende", "elke"],
            [("quelques", "enkele"), ("plusieurs", "verschillende"), ("chaque", "elke")],
            "Na chaque volgt altijd een enkelvoud."),
    keuze("Ik drink water: Je bois [[*de l'|du|des]] eau.", "Eau is vrouwelijk en begint met een klinker."),
    tabel("Is het lidwoord juist?",
          [("la France", J), ("le Canada", J), ("la Mexique", F), ("le héros", J)],
          "Le Mexique is mannelijk; bij een aangeblazen h blijft le staan."),
    open_("Schrijf in het Frans wat er in je koelkast staat: drie dingen, met een deelaanduidend lidwoord of een hoeveelheid.",
          "Il y a du lait, de la confiture et un kilo de tomates."),
    inv("Vul in: … homme est mon oncle. Aanwijzend determinant.", ["Cet", "cet"], "Homme is mannelijk met een stomme h: cet."),
    mk("Je staat in een winkel en zegt: 'Je prends ce pull-ci, pas ce pull-là.' Wat bedoel je?",
       ["deze trui hier, niet die daar", "die trui daar, niet deze trui hier", "alle truien uit de winkel", "geen enkele trui"],
       0, "Ci is dichtbij, là verderaf."),
    keuze("Je vais [[*à la|au|aux]] piscine.", "Piscine is vrouwelijk: à la blijft staan."),
]

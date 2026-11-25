"""Bijvoeglijke naamwoorden, bijwoorden en de trappen — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_adjectieven: de vormen en de plaats van het
bijvoeglijk naamwoord, de overeenkomst, bijwoorden (frequent en op -ment) en
de trappen van vergelijking (plus, moins, aussi, meilleur, mieux, pire).
Met drie zelfgetekende rugzakken om te vergelijken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ROOD, LICHTGROEN

RZ = Prent("drie-rugzakken", "Trois sacs à dos", "drie rugzakken van verschillende grootte met een prijs en een gewicht, letters A tot C")
ZAK = [("A", 210, 120, 300, ROOD, "45 €", "1,2 kg", "20 l"), ("B", 500, 85, 220, BLAUW, "60 €", "0,8 kg", "15 l"), ("C", 790, 150, 380, LICHTGROEN, "45 €", "1,9 kg", "35 l")]
for t, x, b, h, kl, prijs, gew, vol in ZAK:
    top = 470 - h
    RZ.rect(x - b / 2, top, b, h, kl, DONKER, 30, 3)
    RZ.rect(x - b / 3, top + h * 0.45, b * 2 / 3, h * 0.35, kl, DONKER, 14, 2)
    RZ.pad(f"M {x - 30} {top} Q {x} {top - 40} {x + 30} {top}", "none", DONKER, 5)
    RZ.tekst(x, 520, prijs, 26, vet=True)
    RZ.tekst(x, 555, gew, 22)
    RZ.tekst(x, 588, vol, 22)
    RZ.letter(x - b / 2 - 10, top - 10, t)
RZ.tekst(60, 520, "prix", 18, "start"); RZ.tekst(60, 555, "poids", 18, "start"); RZ.tekst(60, 588, "volume", 18, "start")
U = "drie-rugzakken.svg"
Z = {t: [Prent.zone(x - 150, 470 - h - 50, 300, h + 140)] for t, x, b, h, *_ in ZAK}

VRAGEN = [
    klik("Bekijk de rugzakken. Klik op le sac le plus léger.", U, Z["B"], "Léger: licht. 0,8 kg is het lichtst."),
    klik("Klik op le sac le plus grand.", U, Z["C"], "35 liter is de grootste."),
    klik("Klik op le sac le plus cher.", U, Z["B"], "Cher: duur. 60 euro."),
    tabel("Klopt dit over de rugzakken?",
          [("Le sac A est aussi cher que le sac C.", J), ("Le sac C est moins lourd que le sac A.", F), ("Le sac B est plus petit que le sac A.", J), ("Le sac A est plus léger que le sac B.", F)],
          "A en C kosten allebei 45 euro; C weegt meer dan A."),
    sorteer("Welke vrouwelijke vorm?", ["-euse", "-ve", "-elle", "-che"],
            [("sérieux", "-euse"), ("actif", "-ve"), ("nouveau", "-elle"), ("blanc", "-che"), ("dangereux", "-euse"), ("neuf", "-ve")],
            "Sérieuse, active, nouvelle, blanche, dangereuse, neuve."),
    sleep("Een advertentie: À vendre : un [[vieil]] appartement avec une [[belle]] vue et une [[nouvelle]] cuisine.",
          ["vieux", "beau"], "Vieil voor een klinker; vue en cuisine zijn vrouwelijk."),
    mk("'C'est un grand homme.' Wat betekent dat?",
       ["het is een belangrijke man", "het is een heel lange man", "het is een heel oude man", "het is een man met grote voeten"],
       0, "Un homme grand is lang; un grand homme is belangrijk."),
    tabel("Klopt de overeenkomst?",
          [("Elles sont contentes.", J), ("La porte est ouvert.", F), ("Mes sœurs et mon frère sont partis.", J), ("Des yeux marrons.", F), ("Des robes vertes.", J)],
          "La porte est ouverte; marron blijft onveranderd."),
    keuze("Mes amies semblent [[*fatiguées|fatigué|fatigués]].", "Na sembler komt het overeen met het onderwerp: vrouwelijk meervoud."),
    inv("Vul in: des chants … (van national).", ["nationaux"], "Mannelijk meervoud van -al: -aux."),
    sorteer("Vóór of achter het naamwoord?", ["vóór", "achter"],
            [("petit", "vóór"), ("rouge", "achter"), ("bon", "vóór"), ("intéressant", "achter"), ("jeune", "vóór"), ("français", "achter")],
            "Een klein groepje korte woorden gaat vooraan."),
    sorteer("Maak het bijwoord.", ["-ment na de vrouwelijke vorm", "onregelmatig"],
            [("lent → lentement", "-ment na de vrouwelijke vorm"), ("doux → doucement", "-ment na de vrouwelijke vorm"), ("bon → bien", "onregelmatig"), ("mauvais → mal", "onregelmatig"), ("heureux → heureusement", "-ment na de vrouwelijke vorm")],
            "Via de vrouwelijke vorm, behalve bien en mal."),
    inv("Maak het bijwoord van 'sérieux': il travaille … .", ["sérieusement"], "Sérieuse + ment."),
    keuze("Il a [[*souvent voyagé|voyagé souvent|souvent a voyagé]] en Espagne.", "Een kort bijwoord tussen hulpwerkwoord en deelwoord."),
    volgorde("Zet van nooit naar altijd.",
             ["jamais", "rarement", "parfois", "souvent", "toujours"],
             "Rarement is zelden, parfois soms."),
    sorteer("Meilleur of mieux?", ["meilleur(e)", "mieux"],
            [("Elle danse … que moi.", "mieux"), ("C'est le … gâteau.", "meilleur(e)"), ("Il parle … français maintenant.", "mieux"), ("Ta note est … que la mienne.", "meilleur(e)")],
            "Mieux bij een werkwoord, meilleur bij een naamwoord."),
    keuze("Ce film est [[*pire|plus bon|meilleur]] que le livre : il est vraiment mauvais.", "Pire hoort bij mauvais."),
    mk("Welke zin vergelijkt een hoeveelheid?",
       ["J'ai moins de devoirs que toi.", "Je suis moins grand que ton frère.", "Je cours moins vite que toi.", "Je suis aussi grand que ta sœur."],
       0, "Bij een hoeveelheid komt de: plus de, moins de, autant de."),
    inv("Vul in: Paris est … grande ville de France. Twee woorden: de grootste.", ["la plus"], "Overtreffende trap: la plus grande."),
    keuze("Elle est [[*aussi|autant|aussi de]] sportive que son frère.", "Aussi bij een eigenschap, autant de bij een hoeveelheid."),
    tabel("Is de vorm juist?",
          [("un bel arbre", J), ("un nouveau ami", F), ("de vieux livres", J), ("heureuxs", F)],
          "Un nouvel ami; heureux blijft heureux."),
    mk("Elle chante doucement. Wat is doucement?",
       ["een bijwoord", "een bijvoeglijk naamwoord", "een werkwoord", "een naamwoord"],
       0, "Het zegt hoe ze zingt en verandert nooit."),
    keuze("Une histoire [[*heureuse|heureux|heureuxe]].", "-eux wordt -euse."),
    tabel("Klopt dit over bijwoorden en trappen?",
          [("Een bijwoord verandert nooit van vorm.", J), ("Plus bon bestaat in het Frans.", F), ("Le plus bij een werkwoord blijft altijd le.", J), ("Na aussi komt comme.", F)],
          "Na aussi komt que."),
    open_("Vergelijk in het Frans twee mensen uit je familie in twee zinnen. Gebruik plus … que en meilleur of mieux.",
          "Mon frère est plus grand que moi. Mais je joue mieux au tennis que lui."),
    keuze("Un garçon calme, une fille [[*calme|calmee|calmé]].", "Wat al op -e eindigt, verandert niet."),
    mk("'Les murs de la chambre sont blancs.' Waaraan zie je dat blancs bij murs hoort?",
       ["aan de mannelijke meervoudsuitgang", "aan het woord chambre dat ervoor staat", "aan het lidwoord la voor chambre", "aan de hoofdletter van het woord Les"],
       0, "Chambre is vrouwelijk enkelvoud; blancs is mannelijk meervoud, zoals murs."),
    inv("Vul in: Ce sont les … chaussures du magasin, de duurste. Twee woorden.", ["plus chères"], "Chaussures is vrouwelijk meervoud: les plus chères."),
    keuze("Il travaille [[*bien|bon]] : son patron est content.", "Bien hoort bij een werkwoord."),
    sleep("Over de rugzakken: Le sac B est [[plus]] léger [[que]] le sac A, mais il est [[moins]] grand.",
          ["comme", "autant"], "Plus … que, moins … que."),
]

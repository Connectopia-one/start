# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van wiskunde 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Dezelfde leerstof, dezelfde woorden, andere getallen en andere
situaties, zodat je kind twee keer nadenkt en niet twee keer hetzelfde antwoord
opschrijft. Wie hier iets bijschrijft, legt het dus eerst naast de vragen in
`../../start/wiskunde*.json`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, oefenbundel, uitlegblad, bundel

B = bundel.breuk   # B(3, 4) is een breuk met een echte streep

OEFENBUNDELS = {}

OEFENBUNDELS["oefenbundel-rekenen-en-breuken"] = dict(
    vak="Wiskunde", titel="Rekenen en breuken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Breuken lezen en schrijven",
             opdracht="Kijk goed naar de tekening voor je iets opschrijft.",
             oefeningen=[
                 ("fig", [
                     (svg.breukfiguur("strook", 3, 4), f"{B(3, 4)}"),
                     (svg.breukfiguur("cirkel", 5, 6), f"{B(5, 6)}"),
                     (svg.breukfiguur("raster", 40, 100), f"{B(40, 100)}, of vereenvoudigd {B(2, 5)}"),
                 ], "Welk deel is gekleurd? Schrijf het als breuk."),
                 ("kleur", [
                     (svg.breukfiguur("strook", 0, 5), f"kleur {B(2, 5)}", r"\(2\) van de \(5\) vakjes gekleurd"),
                     (svg.breukfiguur("cirkel", 0, 8), f"kleur {B(3, 8)}", r"\(3\) van de \(8\) punten gekleurd"),
                 ]),
                 ("rij", [
                     (f"In de breuk {B(7, 9)} heet de 9 de", "noemer"),
                     (r"en de \(7\) heet de", "teller"),
                 ]),
                 ("open", f"Zet deze breuken van klein naar groot: {B(1, 8)} &nbsp; {B(1, 2)} &nbsp; {B(1, 6)} &nbsp; {B(1, 3)}",
                  f"{B(1, 8)}, {B(1, 6)}, {B(1, 3)}, {B(1, 2)}", 1),
                 ("waar", f"{B(3, 5)} en {B(6, 10)} zijn evenveel waard.", True),
                 ("waar", "Hoe groter de noemer, hoe groter elk stukje.", False),
             ]),

        dict(kop="Gelijke breuken en vereenvoudigen",
             opdracht="Teller en noemer allebei door hetzelfde getal: dat verandert de waarde niet.",
             oefeningen=[
                 ("rij", [
                     (f"{B(1, 3)} = {B('…', 9)}", r"\(3\)"),
                     (f"{B(3, 5)} = {B(6, '…')}", r"\(10\)"),
                     (f"{B(1, 2)} = {B(7, '…')}", r"\(14\)"),
                     (f"{B(2, 7)} = {B('…', 21)}", r"\(6\)"),
                 ]),
                 ("rij", [
                     (f"{B(9, 12)} =", f"{B(3, 4)}"),
                     (f"{B(20, 25)} =", f"{B(4, 5)}"),
                     (f"{B(14, 21)} =", f"{B(2, 3)}"),
                     (f"{B(15, 45)} =", f"{B(1, 3)}"),
                     (f"{B(18, 24)} =", f"{B(3, 4)}"),
                     (f"{B(30, 100)} =", f"{B(3, 10)}"),
                 ]),
                 ("kies", "Welke breuk hoort niet bij de andere drie?",
                  [f"{B(2, 6)}", f"{B(3, 9)}", f"{B(3, 8)}", f"{B(4, 12)}"], 2),
                 ("open", f"Lotte zegt dat {B(4, 6)} hetzelfde is als {B(2, 3)}. Heeft ze gelijk? Schrijf erbij "
                          "hoe je het weet.",
                  f"Ja. Deel teller en noemer allebei door 2: 4 : 2 = 2 en 6 : 2 = 3, dus {B(4, 6)} = {B(2, 3)}.", 2),
             ]),

        dict(kop="Rekenen met breuken",
             opdracht="Bij optellen en aftrekken met dezelfde noemer verandert die noemer niet.",
             oefeningen=[
                 ("rij", [
                     (f"{B(2, 7)} + {B(3, 7)} =", f"{B(5, 7)}"),
                     (f"{B(5, 9)} + {B(1, 9)} =", f"{B(6, 9)}, of {B(2, 3)}"),
                     (f"{B(7, 10)} − {B(3, 10)} =", f"{B(4, 10)}, of {B(2, 5)}"),
                     (f"{B(3, 8)} + {B(4, 8)} =", f"{B(7, 8)}"),
                     (f"{B(11, 12)} − {B(5, 12)} =", f"{B(6, 12)}, of {B(1, 2)}"),
                     (f"{B(5, 6)} − {B(5, 6)} =", r"\(0\)"),
                 ]),
                 ("rij", [
                     (f"{B(1, 6)} van 42 =", r"\(7\)"),
                     (f"{B(3, 5)} van 40 =", r"\(24\)"),
                     (f"{B(7, 8)} van 32 =", r"\(28\)"),
                     (f"{B(2, 9)} van 63 =", r"\(14\)"),
                     (f"{B(3, 4)} van 36 =", r"\(27\)"),
                     (f"{B(5, 6)} van 54 =", r"\(45\)"),
                 ]),
                 ("open", f"In een klas van 24 kinderen draagt {B(1, 3)} een bril. Hoeveel kinderen dragen "
                          "er géén bril?",
                  r"\(16\). Een derde van \(24\) is \(8\) kinderen met een bril, dus \(24 - 8 = 16\) zonder.", 2),
                 ("open", r"Je leest een boek van \(120\) bladzijden en je bent op bladzijde 90. Welk "
                          "deel van het boek heb je gelezen? Schrijf je antwoord zo eenvoudig mogelijk.",
                  f"{B(3, 4)}. Je las 90 van de 120 bladzijden, en {B(90, 120)} wordt {B(3, 4)} als je allebei door 30 "
                  "deelt.", 2),
             ]),

        dict(kop="Breuk, kommagetal en procent",
             opdracht="Drie manieren om hetzelfde te zeggen.",
             oefeningen=[
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [[f"{B(1, 2)}", r"\(0{,}5\)", r"\(50\,\%\)"],
                   [f"{B(1, 4)}", None, None],
                   [f"{B(3, 4)}", None, None],
                   [None, r"\(0{,}2\)", None],
                   [None, None, r"\(10\,\%\)"]],
                  f"{B(1, 4)} = 0,25 = 25 % · {B(3, 4)} = 0,75 = 75 % · {B(1, 5)} = 0,2 = 20 % · {B(1, 10)} = 0,1 = 10 %"),
                 ("kies", "Wat is het grootst?", [r"\(0{,}7\)", f"{B(3, 4)}", "even groot"], 1),
                 ("waar", r"\(50\,\%\) van een getal is hetzelfde als de helft ervan.", True),
                 ("rij", [
                     (r"\(10\,\%\) van \(350\) =", r"\(35\)"),
                     (r"\(25\,\%\) van \(80\) =", r"\(20\)"),
                     (r"\(50\,\%\) van \(124\) =", r"\(62\)"),
                     (r"\(75\,\%\) van \(40\) =", r"\(30\)"),
                     (r"\(20\,\%\) van \(45\) =", r"\(9\)"),
                     (r"\(5\,\%\) van \(300\) =", r"\(15\)"),
                 ]),
                 ("open", r"Een boek van \(18\) euro krijgt \(50\,\%\) korting. Hoeveel betaal je?",
                  r"\(9\) euro. De helft van \(18\) is \(9\).", 1),
                 ("open", r"In een doos van \(20\) koeken zitten er \(5\) met chocolade. Hoeveel procent van "
                          "de koeken heeft chocolade?",
                  f"25 %. 5 van de 20 is {B(1, 4)}, en dat is 25 %.", 2),
             ]),

        dict(kop="Hoofdrekenen en de juiste volgorde",
             opdracht="Maal en deel gaan voor plus en min. Haakjes gaan voor alles.",
             oefeningen=[
                 ("rij", [
                     (r"\(256 + 137\) =", r"\(393\)"),
                     (r"\(703 - 248\) =", r"\(455\)"),
                     (r"\(15 \cdot 6\) =", r"\(90\)"),
                     (r"\(132 : 11\) =", r"\(12\)"),
                     (r"\(25 \cdot 8\) =", r"\(200\)"),
                     (r"\(1\,000 - 472\) =", r"\(528\)"),
                 ]),
                 ("rij", [
                     (r"\(6 + 4 \cdot 3\) =", r"\(18\)"),
                     (r"\((6 + 4) \cdot 3\) =", r"\(30\)"),
                     (r"\(20 - 2 \cdot 5\) =", r"\(10\)"),
                     (r"\(3 \cdot (8 - 5)\) =", r"\(9\)"),
                     (r"\(5 \cdot 4 + 6\) =", r"\(26\)"),
                     (r"\(5 \cdot (4 + 6)\) =", r"\(50\)"),
                 ]),
                 ("waar", r"Je mag \(7 + 3 \cdot 2\) gewoon van links naar rechts uitrekenen.", False),
                 ("rij", [
                     (r"\(3{,}4 + 2{,}75\) =", r"\(6{,}15\)"),
                     (r"\(8{,}5 - 1{,}25\) =", r"\(7{,}25\)"),
                     (r"\(0{,}5 \cdot 16\) =", r"\(8\)"),
                     (r"\(9{,}6 : 3\) =", r"\(3{,}2\)"),
                     (r"\(1{,}5 \cdot 4\) =", r"\(6\)"),
                     (r"\(7{,}2 + 0{,}85\) =", r"\(8{,}05\)"),
                 ]),
                 ("open", r"Reken handig uit: \(4 \cdot 17 \cdot 25\). Schrijf erbij welke twee getallen je "
                          "eerst samen nam.",
                  r"\(1\,700\). Eerst \(4 \cdot 25 = 100\), en dan \(100 \cdot 17\).", 2),
             ]),

        dict(kop="Afronden en zelf denken",
             opdracht="Bij de laatste twee bestaat er meer dan één goed antwoord.",
             oefeningen=[
                 ("rij", [
                     (r"\(3\,748\) op het tiental =", r"\(3\,750\)"),
                     (r"\(3\,748\) op het honderdtal =", r"\(3\,700\)"),
                     (r"\(3\,748\) op het duizendtal =", r"\(4\,000\)"),
                     (r"\(2\,950\) op het honderdtal =", r"\(3\,000\)"),
                 ]),
                 ("open", r"Een touw van \(4{,}5\) meter wordt in stukken van \(75\) cm geknipt. Hoeveel "
                          "stukken krijg je?",
                  r"\(6\) stukken. \(4{,}5\) meter is \(450\) cm, en \(450 : 75 = 6\).", 2),
                 ("open", r"Vier vrienden verdelen \(3\) pizza's eerlijk. Hoeveel pizza krijgt elk? "
                          "Schrijf je antwoord als breuk.",
                  f"{B(3, 4)} pizza. Snijd elke pizza in vieren: dat zijn 12 stukken voor 4 kinderen, "
                  r"dus \(3\) stukken elk.", 2),
                 ("open", f"Verzin zelf twee sommen waarvan het antwoord {B(3, 4)} is, en die niet op "
                          "elkaar lijken.",
                  f"Alles wat {B(3, 4)} oplevert is goed, bijvoorbeeld {B(1, 4)} + {B(2, 4)}, of {B(6, 8)} vereenvoudigd, "
                  f"of 75 % van 1, of 1 − {B(1, 4)}.", 3),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-getallenkennis"] = dict(
    vak="Wiskunde", titel="Getallenkennis",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Waar staat een cijfer voor",
             opdracht="Waar een cijfer staat, bepaalt wat het waard is.",
             oefeningen=[
                 ("rij", [
                     (r"de \(8\) in \(6\,843\) =", r"\(800\), of \(8\) honderdtallen"),
                     (r"de \(2\) in \(25\,906\) =", r"\(20\,000\), of \(2\) tienduizendtallen"),
                     (r"de \(4\) in \(940\,217\) =", r"\(40\,000\), of \(4\) tienduizendtallen"),
                     (r"de \(9\) in \(3\,095\) =", r"\(90\), of \(9\) tientallen"),
                 ]),
                 ("rij", [
                     (r"tientallen in \(3\,600\) =", r"\(360\)"),
                     (r"duizendtallen in \(82\,000\) =", r"\(82\)"),
                     (r"honderdtallen in \(5\,300\) =", r"\(53\)"),
                     (r"tienduizendtallen in \(240\,000\) =", r"\(24\)"),
                 ]),
                 ("kort", "Schrijf vier miljoen zeshonderdduizend in cijfers:", r"\(4\,600\,000\)"),
                 ("open", r"Schrijf \(1\,250\,000\) voluit in woorden.",
                  "een miljoen tweehonderdvijftigduizend", 1),
                 ("open", r"Zet van klein naar groot: \(92\,040\) &nbsp; \(9\,240\) &nbsp; \(92\,400\) &nbsp; \(9\,024\)",
                  r"\(9\,024\), \(9\,240\), \(92\,040\), \(92\,400\)", 1),
                 ("waar", r"In het getal \(5\,050\) zijn de twee vijven evenveel waard.", False),
             ]),

        dict(kop="Kommagetallen en afronden",
             opdracht="Bij afronden kijk je naar het cijfer rechts van de plaats waarop je afrondt.",
             oefeningen=[
                 ("rij", [
                     (r"\(0{,}45\) &nbsp;&nbsp; \(0{,}5\)", "&lt;"),
                     (r"\(2{,}08\) &nbsp;&nbsp; \(2{,}8\)", "&lt;"),
                     (r"\(3{,}60\) &nbsp;&nbsp; \(3{,}6\)", "="),
                     (r"\(0{,}9\) &nbsp;&nbsp; \(0{,}89\)", "&gt;"),
                 ], "Zet in het vakje het juiste teken: &lt;, &gt; of =."),
                 ("rij", [
                     (r"\(4\,382\) op het honderdtal =", r"\(4\,400\)"),
                     (r"\(4\,382\) op het duizendtal =", r"\(4\,000\)"),
                     (r"\(7{,}68\) op één cijfer na de komma =", r"\(7{,}7\)"),
                     (r"\(12{,}45\) op het geheel getal =", r"\(12\)"),
                 ]),
                 ("open", r"Schrijf drie getallen op die tussen \(2{,}7\) en \(2{,}8\) liggen.",
                  r"Alles tussen \(2{,}7\) en \(2{,}8\) is goed, bijvoorbeeld \(2{,}71\), \(2{,}75\) en \(2{,}79\).", 1),
                 ("rij", [
                     (r"\(3{,}6 \cdot 10\) =", r"\(36\)"),
                     (r"\(0{,}45 \cdot 100\) =", r"\(45\)"),
                     (r"\(82 : 10\) =", r"\(8{,}2\)"),
                     (r"\(5 : 100\) =", r"\(0{,}05\)"),
                     (r"\(1{,}2 \cdot 1\,000\) =", r"\(1\,200\)"),
                     (r"\(940 : 1\,000\) =", r"\(0{,}94\)"),
                 ]),
                 ("waar", r"Als je een getal door \(10\) deelt, schuift de komma één plaats naar links.",
                  True),
             ]),

        dict(kop="Deelbaar of niet",
             opdracht="Je hoeft niet te delen om het te weten: kijk naar het laatste cijfer of tel "
                      "de cijfers op.",
             oefeningen=[
                 ("kies", r"Welk van deze getallen is deelbaar door \(6\)?",
                  [r"\(142\)", r"\(234\)", r"\(355\)", r"\(428\)"], 1),
                 ("rij", [
                     (r"\(316\)", r"ja, \(316 : 4 = 79\)"),
                     (r"\(522\)", "nee"),
                     (r"\(1\,000\)", r"ja, \(1\,000 : 4 = 250\)"),
                     (r"\(738\)", "nee"),
                 ], r"Deelbaar door \(4\)? Schrijf ja of nee."),
                 ("kies", "Welk van deze getallen is een priemgetal?",
                  [r"\(21\)", r"\(27\)", r"\(29\)", r"\(33\)"], 2),
                 ("open", r"Schrijf alle delers van \(24\) op.", r"\(1\), \(2\), \(3\), \(4\), \(6\), \(8\), \(12\) en \(24\)", 1),
                 ("waar", r"Elk getal dat deelbaar is door \(3\), is ook deelbaar door \(6\).", False),
             ]),

        dict(kop="Getallen onder nul",
             opdracht="Hoe verder links op de getallenlijn, hoe kleiner.",
             oefeningen=[
                 ("open", r"Zet van klein naar groot: \(-3\) &nbsp; \(5\) &nbsp; \(-12\) &nbsp; \(0\) &nbsp; \(-1\)",
                  r"\(-12\), \(-3\), \(-1\), \(0\), \(5\)", 1),
                 ("rij", [
                     (r"\(-4 + 7\) =", r"\(3\)"),
                     (r"\(2 - 9\) =", r"\(-7\)"),
                     (r"\(-5 + 5\) =", r"\(0\)"),
                     (r"\(-10 + 4\) =", r"\(-6\)"),
                 ]),
                 ("waar", r"\(-20\) is kleiner dan \(-2\).", True),
                 ("open", r"In Hasselt is het \(3^{\circ}\text{C}\), in Moskou \(-11^{\circ}\text{C}\). Hoeveel graden verschil is dat?",
                  r"\(14\) graden. Van \(-11\) naar \(0\) is \(11\) graden, en van \(0\) naar \(3\) nog eens \(3\).", 2),
             ]),

        dict(kop="Rijen en patronen",
             opdracht="Zoek eerst wat er telkens met het getal gebeurt.",
             oefeningen=[
                 ("rij", [
                     (r"\(5\), \(10\), \(20\), \(40\), …", r"\(80\), telkens maal \(2\)"),
                     (r"\(100\), \(91\), \(82\), \(73\), …", r"\(64\), telkens \(9\) eraf"),
                     (r"\(1\), \(4\), \(9\), \(16\), …", r"\(25\), de kwadraten"),
                     (r"\(2\), \(5\), \(11\), \(23\), …", r"\(47\), telkens maal \(2\) plus \(1\)"),
                 ]),
                 ("open", r"Wat is de regel van deze rij: \(3\), \(7\), \(11\), \(15\), \(19\)?",
                  r"Er komt telkens \(4\) bij.", 1),
                 ("open", "Verzin zelf een rij van vijf getallen, en schrijf de regel eronder.",
                  "Alles mag, zolang de regel klopt voor elke stap van de rij.", 2),
             ]),

        dict(kop="Alles door elkaar",
             opdracht="Hier komt alles van hierboven samen.",
             oefeningen=[
                 ("open", r"Een stadion heeft \(24\,500\) plaatsen en er zijn er \(18\,750\) verkocht. "
                          "Hoeveel plaatsen blijven er over?",
                  r"\(5\,750\) plaatsen. \(24\,500 - 18\,750 = 5\,750\).", 2),
                 ("rij", [
                     (r"\(24\,500\) op het duizendtal =", r"\(25\,000\)"),
                     (r"\(24\,500\) op het tienduizendtal =", r"\(20\,000\)"),
                 ]),
                 ("kies", "Welk getal is het grootst?", [r"\(0{,}9\)", r"\(0{,}89\)", r"\(0{,}891\)", r"\(0{,}8909\)"], 0),
                 ("open", r"Zoek een getal tussen \(30\) en \(60\) dat deelbaar is door \(3\) én door \(5\).",
                  r"\(45\). Wie door \(3\) én door \(5\) deelbaar is, is deelbaar door \(15\), en tussen \(30\) en \(60\) "
                  r"is dat alleen \(45\).", 2),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-bewerkingen"] = dict(
    vak="Wiskunde", titel="Bewerkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Optellen en aftrekken",
             opdracht="Schrijf gerust je tussenstappen op, ook als je uit het hoofd rekent.",
             oefeningen=[
                 ("rij", [
                     (r"\(465 + 289\) =", r"\(754\)"),
                     (r"\(1\,000 - 638\) =", r"\(362\)"),
                     (r"\(2\,340 + 1\,875\) =", r"\(4\,215\)"),
                     (r"\(5\,000 - 2\,745\) =", r"\(2\,255\)"),
                     (r"\(604 - 398\) =", r"\(206\)"),
                     (r"\(1\,250 + 750\) =", r"\(2\,000\)"),
                 ]),
                 ("open", r"Reken handig uit: \(87 + 96 + 13\). Schrijf erbij welke twee getallen je "
                          "eerst samen nam.",
                  r"\(196\). Eerst \(87 + 13 = 100\), en dan \(100 + 96\).", 2),
                 ("waar", r"Bij \(250 + 380 + 50\) mag je eerst \(250 + 50\) uitrekenen.", True),
             ]),

        dict(kop="Maal en gedeeld",
             opdracht="Zoek eerst of er een handige weg is voor je begint te cijferen.",
             oefeningen=[
                 ("rij", [
                     (r"\(7 \cdot 8\) =", r"\(56\)"),
                     (r"\(8 \cdot 8\) =", r"\(64\)"),
                     (r"\(12 \cdot 7\) =", r"\(84\)"),
                     (r"\(11 \cdot 12\) =", r"\(132\)"),
                     (r"\(13 \cdot 13\) =", r"\(169\)"),
                     (r"\(15 \cdot 4\) =", r"\(60\)"),
                 ]),
                 ("rij", [
                     (r"\(48 \cdot 5\) =", r"\(240\)"),
                     (r"\(25 \cdot 16\) =", r"\(400\)"),
                     (r"\(35 \cdot 20\) =", r"\(700\)"),
                     (r"\(684 : 6\) =", r"\(114\)"),
                     (r"\(1\,512 : 8\) =", r"\(189\)"),
                     (r"\(936 : 9\) =", r"\(104\)"),
                 ]),
                 ("rij", [
                     (r"\(4 \cdot 99\) =", r"\(396\)"),
                     (r"\(50 \cdot 18\) =", r"\(900\)"),
                     (r"\(125 \cdot 8\) =", r"\(1\,000\)"),
                     (r"\(19 \cdot 6\) =", r"\(114\)"),
                 ], "Deze kan je handig uitrekenen. Probeer het zonder te cijferen."),
                 ("waar", r"Bij \(6 \cdot 4 \cdot 5\) mag je eerst \(4 \cdot 5\) uitrekenen.", True),
                 ("waar", r"Bij \(60 : 6 : 2\) maakt het niet uit welke deling je eerst doet.", False),
                 ("open", r"Een doos bevat \(24\) potloden. Hoeveel potloden zitten er in \(15\) dozen?",
                  r"\(360\) potloden. \(24 \cdot 15 = 360\).", 2),
                 ("open", r"Een bus heeft \(52\) zitplaatsen. Hoeveel bussen heb je nodig voor "
                          r"\(210\) kinderen?",
                  r"\(5\) bussen. \(4\) bussen nemen er \(208\) mee, dus de laatste \(2\) kinderen hebben er nog "
                  "een nodig.", 2),
             ]),

        dict(kop="De juiste volgorde",
             opdracht="Haakjes eerst, dan maal en gedeeld, dan plus en min.",
             oefeningen=[
                 ("rij", [
                     (r"\(8 + 5 \cdot 3\) =", r"\(23\)"),
                     (r"\((8 + 5) \cdot 3\) =", r"\(39\)"),
                     (r"\(30 - 4 \cdot 6\) =", r"\(6\)"),
                     (r"\(4 \cdot (9 - 2)\) =", r"\(28\)"),
                     (r"\(7 \cdot 3 + 7\) =", r"\(28\)"),
                     (r"\(7 \cdot (3 + 7)\) =", r"\(70\)"),
                 ]),
                 ("waar", "Maal en gedeeld reken je altijd vóór wat tussen haakjes staat.", False),
                 ("open", r"Zet haakjes in \(12 + 8 : 4\) zodat het antwoord \(5\) is.",
                  r"\((12 + 8) : 4 = 5\). Zonder haakjes is het antwoord \(14\).", 1),
             ]),

        dict(kop="Breuken en procenten in een som",
             opdracht="Een deel van een getal nemen is ook rekenen.",
             oefeningen=[
                 ("rij", [
                     (f"{B(2, 5)} van 45 =", r"\(18\)"),
                     (f"{B(5, 8)} van 48 =", r"\(30\)"),
                     (f"{B(1, 5)} + {B(3, 5)} =", f"{B(4, 5)}"),
                     (f"{B(7, 9)} &minus; {B(4, 9)} =", f"{B(3, 9)}, of {B(1, 3)}"),
                     (f"{B(3, 10)} + {B(4, 10)} =", f"{B(7, 10)}"),
                     (f"{B(5, 6)} &minus; {B(1, 6)} =", f"{B(4, 6)}, of {B(2, 3)}"),
                 ]),
                 ("rij", [
                     (r"\(15\,\%\) van \(400\) =", r"\(60\)"),
                     (r"\(30\,\%\) van \(90\) =", r"\(27\)"),
                     (r"\(5\,\%\) van \(240\) =", r"\(12\)"),
                     (r"\(40\,\%\) van \(150\) =", r"\(60\)"),
                 ]),
                 ("open", r"In een klas van \(25\) kinderen doet \(40\,\%\) aan sport. Hoeveel kinderen "
                          "zijn dat?",
                  f"10 kinderen. 40 % is {B(4, 10)}, en {B(4, 10)} van 25 is 10.", 2),
             ]),

        dict(kop="Kommagetallen",
             opdracht="Zet de komma's netjes onder elkaar als je cijfert.",
             oefeningen=[
                 ("rij", [
                     (r"\(3{,}75 + 2{,}5\) =", r"\(6{,}25\)"),
                     (r"\(10 - 3{,}4\) =", r"\(6{,}6\)"),
                     (r"\(0{,}25 \cdot 60\) =", r"\(15\)"),
                     (r"\(7{,}2 : 6\) =", r"\(1{,}2\)"),
                     (r"\(1{,}25 \cdot 8\) =", r"\(10\)"),
                     (r"\(4{,}8 + 0{,}95\) =", r"\(5{,}75\)"),
                 ]),
                 ("open", r"Drie flessen kosten samen \(7{,}35\) euro. Wat kost één fles?",
                  r"\(2{,}45\) euro. \(7{,}35 : 3 = 2{,}45\).", 2),
                 ("open", r"Je betaalt met \(20\) euro voor iets van \(13{,}45\) euro. Hoeveel krijg je terug?",
                  r"\(6{,}55\) euro.", 2),
             ]),

        dict(kop="Vraagstukken",
             opdracht="Schrijf eerst op wat je zoekt, dan pas de som.",
             oefeningen=[
                 ("open", r"Een pakje koeken kost \(1{,}85\) euro. Hoeveel kosten \(6\) pakjes?",
                  r"\(11{,}10\) euro. \(1{,}85 \cdot 6 = 11{,}10\).", 2),
                 ("open", r"Een fietser rijdt \(18\) km per uur. Hoeveel kilometer legt hij af in "
                          r"\(2{,}5\) uur?",
                  r"\(45\) km. \(18 \cdot 2 = 36\), plus een half uur is \(9\), samen \(45\).", 2),
                 ("open", r"Een fietser legt elke dag \(12\) km af. Na hoeveel dagen heeft hij "
                          r"\(156\) km gereden?",
                  r"\(13\) dagen. \(156 : 12 = 13\).", 2),
                 ("open", r"Verzin zelf een som met haakjes waarvan het antwoord \(100\) is.",
                  r"Alles wat klopt is goed, bijvoorbeeld \((12 + 13) \cdot 4\) of \((50 - 30) \cdot 5\).", 2),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-meten-en-metend-rekenen"] = dict(
    vak="Wiskunde", titel="Meten en metend rekenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Lengte omzetten",
             opdracht="Elke stap op de ladder is keer tien of gedeeld door tien.",
             oefeningen=[
                 ("rij", [
                     (r"\(4{,}2\) m = … cm", r"\(420\)"),
                     (r"\(65\) mm = … cm", r"\(6{,}5\)"),
                     (r"\(3\) km = … m", r"\(3\,000\)"),
                     (r"\(250\) cm = … m", r"\(2{,}5\)"),
                     (r"\(7\) dm = … cm", r"\(70\)"),
                     (r"\(1\,500\) m = … km", r"\(1{,}5\)"),
                 ]),
                 ("kies", "Welke eenheid past het best bij de dikte van een boek?",
                  ["millimeter", "centimeter", "meter", "kilometer"], 1),
                 ("waar", "Een millimeter is tien keer kleiner dan een centimeter.", True),
             ]),

        dict(kop="Omtrek en oppervlakte",
             opdracht="Omtrek is wat je errond legt, oppervlakte is wat je ermee bedekt.",
             oefeningen=[
                 ("rij", [
                     (r"omtrek vierkant, zijde \(9\) cm =", r"\(36\) cm"),
                     (r"omtrek rechthoek \(11\) cm bij \(5\) cm =", r"\(32\) cm"),
                     (r"oppervlakte vierkant, zijde \(7\) cm =", r"\(49\,\text{cm}^{2}\)"),
                     (r"oppervlakte rechthoek \(12\) cm bij \(4\) cm =", r"\(48\,\text{cm}^{2}\)"),
                 ]),
                 ("open", r"Een tuin is \(8\) m lang en \(6\) m breed. Hoeveel meter draad heb je nodig om "
                          "er een hek rond te zetten?",
                  r"\(28\) m. Dat is de omtrek: \(8 + 6 + 8 + 6\).", 2),
                 ("open", "Diezelfde tuin wil je helemaal vol gras leggen. Hoeveel vierkante meter "
                          "gras heb je nodig?",
                  r"\(48\,\text{m}^{2}\). Dat is de oppervlakte: \(8 \cdot 6\).", 2),
                 ("open", r"Een rechthoek heeft een omtrek van \(30\) cm en is \(9\) cm lang. Hoe breed is hij?",
                  r"\(6\) cm. De helft van \(30\) is \(15\), dat is lengte plus breedte samen, en \(15 - 9 = 6\).", 2),
                 ("waar", "Twee rechthoeken met dezelfde omtrek hebben altijd dezelfde oppervlakte.",
                  False),
             ]),

        dict(kop="Inhoud en massa",
             opdracht="Ook hier gaat het per stap keer tien of gedeeld door tien.",
             oefeningen=[
                 ("rij", [
                     (r"\(2\) l = … ml", r"\(2\,000\)"),
                     (r"\(400\) ml = … l", r"\(0{,}4\)"),
                     (r"\(1\) l = … cl", r"\(100\)"),
                     (r"\(3{,}5\) kg = … g", r"\(3\,500\)"),
                     (r"\(250\) g = … kg", r"\(0{,}25\)"),
                     (r"\(5\) g = … mg", r"\(5\,000\)"),
                 ]),
                 ("kies", "Welke massa is het lichtst?",
                  [r"\(0{,}5\) kg", r"\(750\) g", r"\(400\) g", r"\(1\,200\) mg"], 3),
                 ("open", r"Een kuip bevat \(12\) liter. Je schept er telkens \(750\) ml uit. Hoeveel keer "
                          "kan je scheppen?",
                  r"\(16\) keer. \(12\) liter is \(12\,000\) ml, en \(12\,000 : 750 = 16\).", 2),
                 ("open", r"Een kubus heeft een ribbe van \(5\) cm. Wat is de inhoud?",
                  r"\(125\,\text{cm}^{3}\). \(5 \cdot 5 \cdot 5 = 125\).", 2),
             ]),

        dict(kop="Tijd",
             opdracht="Reken bij een klok in stukken: eerst tot het volgende hele uur.",
             oefeningen=[
                 ("rij", [
                     (r"\(4\) uur = … minuten", r"\(240\)"),
                     (r"\(1{,}5\) uur = … minuten", r"\(90\)"),
                     (r"\(300\) seconden = … minuten", r"\(5\)"),
                     (r"\(2\) dagen = … uren", r"\(48\)"),
                     ("een half uur = … seconden", r"\(1\,800\)"),
                     (r"\(1\) week = … uren", r"\(168\)"),
                 ]),
                 ("open", r"Een zwemles begint om 16.40 u en duurt \(1\) uur en \(25\) minuten. Hoe laat is "
                          "ze gedaan?",
                  r"18.05 u. Van 16.40 u naar 17.40 u is een uur, en \(25\) minuten later is het 18.05 u.",
                  2),
                 ("open", r"Je trein vertrekt om 7.55 u en de reis duurt \(2\) uur en \(40\) minuten. Hoe "
                          "laat kom je aan?",
                  "10.35 u.", 2),
                 ("waar", "Om 14.30 u is het half drie in de namiddag.", True),
             ]),

        dict(kop="Temperatuur en alles door elkaar",
             opdracht="Bij temperatuur kan je onder nul terechtkomen.",
             oefeningen=[
                 ("rij", [
                     (r"\(6^{\circ}\text{C}\) en het wordt \(9\) graden kouder", r"\(-3^{\circ}\text{C}\)"),
                     (r"\(-5^{\circ}\text{C}\) en het wordt \(8\) graden warmer", r"\(3^{\circ}\text{C}\)"),
                     (r"het verschil tussen \(12^{\circ}\text{C}\) en \(-4^{\circ}\text{C}\)", r"\(16\) graden"),
                 ]),
                 ("kies", "Welke temperatuur is het warmst?",
                  [r"\(-2^{\circ}\text{C}\)", r"\(0^{\circ}\text{C}\)", r"\(-7^{\circ}\text{C}\)", r"\(-15^{\circ}\text{C}\)"], 1),
                 ("waar", "Een vierkante meter is honderd vierkante centimeter.", False),
                 ("open", r"Voor één taart heb je \(0{,}25\) kg boter nodig. Je maakt drie taarten. "
                          "Hoeveel gram boter is dat samen?",
                  r"\(750\) g. \(0{,}25\) kg is \(250\) g, en \(250 \cdot 3 = 750\).", 2),
                 ("open", r"Een rol behangpapier is \(10\) m lang. Je knipt er stukken van \(240\) cm uit. "
                          "Hoeveel stukken krijg je, en hoeveel blijft er over?",
                  r"\(4\) stukken, en er blijft \(40\) cm over. \(10\) m is \(1\,000\) cm, en \(4 \cdot 240 = 960\).", 2),
                 ("open", "Verzin zelf een vraag over meten waarbij je iets moet omrekenen, en "
                          "schrijf het antwoord eronder.",
                  "Alles mag, zolang de omrekening klopt.", 3),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-meetkunde"] = dict(
    vak="Wiskunde", titel="Meetkunde",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Hoeken",
             opdracht=r"Een rechte hoek is \(90^{\circ}\), alles daaronder is scherp, alles daarboven stomp.",
             oefeningen=[
                 ("fig", [
                     (svg.hoek(35), "scherp"),
                     (svg.hoek(90), "recht"),
                     (svg.hoek(145), "stomp"),
                     (svg.hoek(180), "gestrekt"),
                 ], "Schrijf onder elke hoek hoe hij heet: scherp, recht, stomp of gestrekt."),
                 ("rij", [
                     (r"Twee hoeken van een driehoek zijn \(60^{\circ}\) en \(70^{\circ}\). De derde is", r"\(50^{\circ}\)"),
                     (r"Drie hoeken van een vierhoek zijn \(90^{\circ}\), \(90^{\circ}\) en \(100^{\circ}\). De vierde is", r"\(80^{\circ}\)"),
                     ("Een kwartdraai is", r"\(90^{\circ}\)"),
                     ("Drie kwartdraaien zijn", r"\(270^{\circ}\)"),
                 ]),
                 ("teken", "Teken zelf een scherpe hoek en een stompe hoek. Schrijf er telkens bij "
                           "hoeveel graden hij ongeveer is.",
                  r"Alles onder \(90^{\circ}\) is scherp, alles tussen \(90^{\circ}\) en \(180^{\circ}\) is stomp.", 50),
                 ("waar", "Een stompe hoek is groter dan een rechte hoek.", True),
             ]),

        dict(kop="Vlakke figuren",
             opdracht="Kijk naar de zijden: hoeveel er zijn, en of ze even lang zijn.",
             oefeningen=[
                 ("fig", [
                     (svg.vorm("ruit"), "een ruit"),
                     (svg.vorm("trapezium"), "een trapezium"),
                     (svg.vorm("vijfhoek"), "een vijfhoek"),
                     (svg.vorm("zeshoek"), "een zeshoek"),
                 ], "Schrijf de naam onder elke figuur."),
                 ("rij", [
                     ("zijden van een vijfhoek:", r"\(5\)"),
                     ("zijden van een achthoek:", r"\(8\)"),
                     ("hoekpunten van een zeshoek:", r"\(6\)"),
                     ("even lange zijden van een gelijkbenige driehoek:", r"\(2\)"),
                 ]),
                 ("teken", r"Teken een rechthoek van \(6\) cm bij \(4\) cm. Schrijf de omtrek en de "
                           "oppervlakte eronder.",
                  r"omtrek \(20\) cm, oppervlakte \(24\,\text{cm}^{2}\)", 60),
                 ("open", "Hoeveel symmetrieassen heeft een vierkant? En een rechthoek die geen "
                          "vierkant is?",
                  r"Een vierkant heeft er \(4\), een gewone rechthoek \(2\).", 2),
                 ("waar", "Elke ruit is een vierkant.", False),
             ]),

        dict(kop="De cirkel",
             opdracht="De straal gaat van het midden tot de rand, de diameter van rand tot rand "
                      "dwars door het midden.",
             oefeningen=[
                 ("rij", [
                     (r"straal \(7\) cm, dus diameter", r"\(14\) cm"),
                     (r"diameter \(18\) cm, dus straal", r"\(9\) cm"),
                     (r"straal \(2{,}5\) cm, dus diameter", r"\(5\) cm"),
                     (r"diameter \(30\) cm, dus straal", r"\(15\) cm"),
                 ]),
                 ("teken", r"Teken met je passer een cirkel met een straal van \(3\) cm. Teken de "
                           "diameter erin en schrijf erbij hoe lang die is.",
                  r"De diameter is \(6\) cm, twee keer de straal.", 65),
                 ("waar", "De diameter is altijd twee keer zo lang als de straal.", True),
             ]),

        dict(kop="Ruimtefiguren",
             opdracht="Een ruimtefiguur heeft vlakken, ribben en hoekpunten.",
             oefeningen=[
                 ("fig", [
                     (svg.ruimtefiguur("balk"), "een balk"),
                     (svg.ruimtefiguur("kegel"), "een kegel"),
                     (svg.ruimtefiguur("cilinder"), "een cilinder"),
                     (svg.ruimtefiguur("bol"), "een bol"),
                 ], "Schrijf de naam onder elke figuur."),
                 ("tabel", ["figuur", "vlakken", "ribben", "hoekpunten"],
                  [["piramide met een driehoekig grondvlak", None, None, None],
                   ["prisma met een driehoekig grondvlak", None, None, None]],
                  r"piramide met een driehoekig grondvlak: \(4\) vlakken, \(6\) ribben, \(4\) hoekpunten &middot; "
                  r"prisma met een driehoekig grondvlak: \(5\) vlakken, \(9\) ribben, \(6\) hoekpunten"),
                 ("open", r"Een kubus heeft een ribbe van \(4\) cm. Hoe lang zijn alle ribben samen?",
                  r"\(48\) cm. Een kubus heeft \(12\) ribben, en \(12 \cdot 4 = 48\).", 2),
                 ("waar", "Een cilinder heeft geen enkel hoekpunt.", True),
             ]),

        dict(kop="Spiegelen en verschuiven",
             opdracht="Bij allebei blijft de figuur even groot.",
             oefeningen=[
                 ("open", "Wat verandert er bij een spiegeling, en wat blijft hetzelfde?",
                  "De vorm en de grootte blijven hetzelfde, maar de figuur ligt omgekeerd, zoals "
                  "in een spiegel.", 2),
                 ("open", "Noem twee dingen bij je thuis die een symmetrieas hebben.",
                  "Alles wat in twee gelijke helften te vouwen is, bijvoorbeeld een deur, een bord "
                  "of een vlinder op een prent.", 2),
                 ("waar", "Bij een verschuiving draait de figuur mee.", False),
             ]),

        dict(kop="Alles door elkaar",
             opdracht="Hier komt alles van hierboven samen.",
             oefeningen=[
                 ("kies", "Welke figuur heeft geen enkele symmetrieas?",
                  ["een gelijkzijdige driehoek", "een rechthoek", "een ruit",
                   "een driehoek met drie verschillende zijden"], 3),
                 ("open", r"Een vierkant heeft een omtrek van \(36\) cm. Hoe lang is één zijde, en hoe "
                          "groot is de oppervlakte?",
                  r"Een zijde is \(9\) cm, want \(36 : 4 = 9\). De oppervlakte is \(9 \cdot 9 = 81\,\text{cm}^{2}\).", 2),
                 ("open", "Beschrijf een figuur zo nauwkeurig dat iemand anders hem kan tekenen "
                          "zonder hem te zien.",
                  "Goed is wat de ander écht kan natekenen: de soort figuur, hoeveel zijden, hoe "
                  "lang, en welke hoeken.", 3),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-kansrekenen-en-statistiek"] = dict(
    vak="Wiskunde", titel="Kansrekenen en statistiek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Hoe groot is de kans",
             opdracht="Een kans schrijf je als het aantal goede uitkomsten op het totaal.",
             oefeningen=[
                 ("tekst", r"<p>In een zak zitten <b>\(4\) rode, \(6\) blauwe en \(2\) groene knikkers</b>. "
                           "Je trekt er één uit zonder te kijken.</p>"),
                 ("rij", [
                     ("knikkers in totaal:", r"\(12\)"),
                     ("kans op rood:", r"\(4\) op \(12\), of \(1\) op \(3\)"),
                     ("kans op blauw:", r"\(6\) op \(12\), of \(1\) op \(2\)"),
                     ("kans op groen:", r"\(2\) op \(12\), of \(1\) op \(6\)"),
                     ("kans op geel:", r"\(0\), er zit geen gele in"),
                     ("kans op niet-groen:", r"\(10\) op \(12\), of \(5\) op \(6\)"),
                 ]),
                 ("kies", "Welke van deze gebeurtenissen is het waarschijnlijkst?",
                  ["kop gooien met een munt", "een groene knikker trekken uit die zak",
                   "een gele knikker trekken uit die zak"], 0),
                 ("waar", r"Een kans van \(1\) betekent dat iets zeker gebeurt.", True),
                 ("open", r"Je gooit \(40\) keer met een munt. Hoe vaak verwacht je ongeveer munt? "
                          "Leg uit waarom het toch anders kan uitvallen.",
                  r"Ongeveer \(20\) keer. Het is maar een verwachting: elke worp staat los van de "
                  r"vorige, dus \(17\) of \(23\) keer kan evengoed.", 3),
             ]),

        dict(kop="Gemiddelde, middelste en meest",
             opdracht="Het gemiddelde tel je op en deel je door het aantal getallen.",
             oefeningen=[
                 ("rij", [
                     (r"gemiddelde van \(5\), \(9\) en \(13\) =", r"\(9\)"),
                     (r"gemiddelde van \(12\), \(14\), \(16\) en \(18\) =", r"\(15\)"),
                     (r"gemiddelde van \(20\) en \(34\) =", r"\(27\)"),
                     (r"gemiddelde van \(3\), \(3\), \(4\) en \(10\) =", r"\(5\)"),
                 ]),
                 ("tekst", r"<p>De punten van Sam waren <b>\(11\), \(13\), \(15\), \(15\) en \(16\)</b> op \(20\).</p>"),
                 ("rij", [
                     ("zijn gemiddelde:", r"\(14\)"),
                     ("het getal dat het vaakst voorkomt:", r"\(15\)"),
                     ("het middelste getal:", r"\(15\)"),
                 ]),
                 ("waar", "Het gemiddelde is altijd een van de getallen uit de rij.", False),
                 ("open", r"Verzin zelf vier getallen met een gemiddelde van \(10\).",
                  r"Alles waarvan de som \(40\) is, bijvoorbeeld \(8\), \(9\), \(11\) en \(12\).", 2),
             ]),

        dict(kop="Grafieken en tabellen",
             opdracht="Elke grafiek is goed in iets anders.",
             oefeningen=[
                 ("kies", "Je wil tonen hoe de temperatuur in de loop van een dag verandert. "
                          "Welke grafiek kies je?",
                  ["een staafdiagram", "een lijngrafiek", "een cirkeldiagram"], 1),
                 ("tekst", "<p>In een klas werd gevraagd welke sport de kinderen doen: "
                           r"<b>voetbal \(9\), dansen \(6\), turnen \(5\), zwemmen \(4\)</b>.</p>"),
                 ("rij", [
                     ("hoeveel kinderen deden mee:", r"\(24\)"),
                     ("de populairste sport:", "voetbal"),
                     ("hoeveel meer voetbal dan zwemmen:", r"\(5\)"),
                     ("welk deel koos dansen:", f"6 op 24, of {B(1, 4)}"),
                 ]),
                 ("waar", "In een cirkeldiagram vormen alle delen samen het geheel.", True),
             ]),

        dict(kop="Alles door elkaar",
             opdracht="Lees eerst goed wat er gevraagd wordt.",
             oefeningen=[
                 ("open", r"Van \(40\) kinderen komen er \(14\) met de fiets. Hoeveel procent is dat?",
                  r"\(35\,\%\). \(14\) van de \(40\) is hetzelfde als \(35\) van de \(100\).", 2),
                 ("open", r"De gemiddelde temperatuur van vier dagen was \(12\) graden. Drie van die "
                          r"dagen waren \(10\), \(11\) en \(15\) graden. Hoe warm was de vierde dag?",
                  r"\(12\) graden. Vier dagen met gemiddeld \(12\) is samen \(48\), en \(48 - 36 = 12\).", 3),
                 ("waar", r"Als de helft van de kinderen een fiets heeft, is dat \(25\,\%\).", False),
                 ("kies", r"In een zak zitten \(7\) witte en \(3\) zwarte ballen. Welke uitspraak klopt?",
                  ["je trekt zeker een witte", "wit is waarschijnlijker dan zwart",
                   "zwart is waarschijnlijker dan wit", "allebei even waarschijnlijk"], 1),
             ]),
    ],
)


OEFENBUNDELS["oefenbundel-vraagstukken-en-problemen-oplossen"] = dict(
    vak="Wiskunde", titel="Vraagstukken en problemen oplossen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Sla een oefening die niet lukt gewoon over en kom er op het einde op terug.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint, dan is de "
        "verleiding weg.",
    ],
    reeksen=[
        dict(kop="Lees eerst wat er gevraagd wordt",
             opdracht="Schrijf eerst op wat je zoekt. Pas daarna reken je.",
             oefeningen=[
                 ("open", r"Op een schoolfeest staan \(8\) lange tafels en aan elke tafel passen "
                          r"\(14\) kinderen. Er komen \(105\) kinderen. Hoeveel plaatsen blijven er leeg?",
                  r"\(7\) plaatsen. \(8 \cdot 14 = 112\) plaatsen, en \(112 - 105 = 7\).", 3),
                 ("open", r"Een zwembadje wordt gevuld met \(25\) liter per minuut. Na hoeveel minuten "
                          r"zit er \(600\) liter in?",
                  r"\(24\) minuten. \(600 : 25 = 24\).", 2),
                 ("open", r"Een doos weegt leeg \(350\) g. Er gaan \(12\) blikjes van \(200\) g in. Hoeveel "
                          "weegt de volle doos in kilogram?",
                  r"\(2{,}75\) kg. De blikjes wegen \(12 \cdot 200 = 2\,400\) g, plus \(350\) g is \(2\,750\) g.", 3),
                 ("waar", "Een schatting vooraf helpt je zien of je antwoord klopt.", True),
             ]),

        dict(kop="Twee stappen",
             opdracht="Bij deze vraagstukken moet je eerst iets anders uitrekenen.",
             oefeningen=[
                 ("open", r"Een klas van \(26\) kinderen gaat op uitstap. De bus kost \(180\) euro en elk "
                          r"kind betaalt \(3\) euro inkom. Wat kost de uitstap samen?",
                  r"\(258\) euro. De inkom is \(26 \cdot 3 = 78\) euro, plus \(180\) euro voor de bus.", 3),
                 ("open", r"Je koopt \(4\) schriften van \(2{,}75\) euro en een map van \(5{,}50\) euro. Hoeveel "
                          "betaal je samen?",
                  r"\(16{,}50\) euro. De schriften kosten \(4 \cdot 2{,}75 = 11\) euro.", 3),
                 ("open", r"Een zak hondenbrokken van \(15\) kg zou \(5\) weken meegaan als de hond "
                          r"\(400\) g per dag krijgt. Klopt dat? Reken het na.",
                  r"Het klopt ongeveer, en de zak gaat zelfs iets langer mee: \(5\) weken is \(35\) dagen, "
                  r"en \(35 \cdot 400\) g = \(14\,000\) g, dus \(14\) kg van de \(15\).", 3),
                 ("waar", r"Een antwoord van \(3{,}5\) kinderen kan kloppen.", False),
             ]),

        dict(kop="Verhoudingen",
             opdracht="Zoek eerst hoeveel er bij één hoort.",
             oefeningen=[
                 ("open", r"\(6\) broodjes kosten \(9\) euro. Wat kosten \(10\) broodjes?",
                  r"\(15\) euro. Eén broodje kost \(9 : 6 = 1{,}50\) euro.", 2),
                 ("open", r"Een recept voor \(4\) personen vraagt \(300\) g bloem. Hoeveel bloem heb je "
                          r"nodig voor \(6\) personen?",
                  r"\(450\) g. Voor één persoon is dat \(75\) g.", 2),
                 ("waar", r"Als \(2\) potten verf genoeg zijn voor \(5\) muren, zijn \(4\) potten genoeg voor "
                          r"\(10\) muren.", True),
                 ("open", r"Op een kaart met schaal \(1\) op \(50\,000\) liggen twee dorpen \(4\) cm uit elkaar. "
                          "Hoeveel kilometer is dat in het echt?",
                  r"\(2\) km. \(4 \cdot 50\,000 = 200\,000\) cm, en dat is \(2\,000\) m of \(2\) km.", 3),
             ]),

        dict(kop="Zelf een plan maken",
             opdracht="Hier is meer dan één weg naar het antwoord.",
             oefeningen=[
                 ("open", r"Je houdt een pannenkoekenverkoop. Eén pannenkoek kost jou \(0{,}40\) euro om "
                          r"te maken en je verkoopt hem voor \(1\) euro. Hoeveel pannenkoeken moet je "
                          r"verkopen om \(90\) euro winst te maken?",
                  r"\(150\) pannenkoeken. Je verdient \(0{,}60\) euro per pannenkoek, en \(90 : 0{,}60 = 150\).", 3),
                 ("open", "Schrijf op welke stappen je bij de vorige oefening gezet hebt.",
                  "Eerst de winst per pannenkoek, dan de totale winst delen door die winst per "
                  r"stuk. Wie eerst uitrekende hoeveel \(150\) pannenkoeken opbrengen, is er ook.", 3),
                 ("open", "Verzin zelf een vraagstuk in twee stappen en schrijf het antwoord "
                          "eronder.",
                  "Goed is een vraagstuk waarbij je iets moet uitrekenen voor je aan het "
                  "gevraagde toekomt.", 4),
             ]),
    ],
)




# ════════════════════════════════════════════════════════════════════
# De uitlegbladen: per oefening het antwoord en waarom het juist is.
# Zie uitlegblad.py. De nummers komen uit de oefenbundel hierboven,
# dus een waarom-lijst moet even lang zijn als haar reeks.
# Staat er None, dan zegt het antwoord zelf al genoeg.
# ════════════════════════════════════════════════════════════════════

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-rekenen-en-breuken"] = dict(
    reeksen=[
        dict(aanpak="Doe het altijd in deze twee stappen. Kijk eerst in <strong>hoeveel gelijke "
                    "stukken</strong> het geheel verdeeld is: dat getal komt onder de streep en "
                    "heet de noemer. Tel dan <strong>hoeveel stukken gekleurd</strong> zijn: dat "
                    "komt boven de streep en heet de teller. Wie met de teller begint, vergeet "
                    "vaak de lege stukken mee te tellen.",
             waarom=[
                 f"Bij c) zijn er \\(100\\) vakjes en \\(40\\) gekleurd. {B(40, 100)} mag blijven "
                 f"staan, maar deel teller en noemer allebei door \\(20\\) en je krijgt {B(2, 5)}: "
                 "precies evenveel, korter geschreven.",
                 "Kleuren is hetzelfde denken, maar omgekeerd. De noemer zegt hoeveel vakjes er "
                 "in totaal zijn, de teller hoeveel je er inkleurt. Welke vakjes je kiest, maakt "
                 "niet uit.",
                 "Noemer komt van <em>noemen</em>: hij noemt de soort stukken, negenden hier. "
                 "De teller <em>telt</em> hoeveel van die stukken je hebt.",
                 "Staat er boven elke breuk een \\(1\\), dan is de breuk met de "
                 "<strong>grootste</strong> noemer de kleinste. In achtsten is hetzelfde geheel "
                 "in meer stukken verdeeld, dus is elk stuk kleiner.",
                 "Teller en noemer zijn allebei maal \\(2\\) gegaan. Dat verandert de waarde "
                 "niet, alleen de maat van de stukken: dubbel zoveel stukken die elk half zo "
                 "groot zijn.",
                 "Net omgekeerd: hoe meer stukken je van hetzelfde geheel maakt, hoe kleiner elk "
                 "stuk. Denk aan een pizza in vier of in acht.",
             ]),
        dict(aanpak="Vereenvoudigen is teller en noemer <strong>allebei door hetzelfde getal "
                    "delen</strong>. Zoek een getal waar ze samen door kunnen: probeer \\(2\\), "
                    "dan \\(3\\), dan \\(5\\). Lukt het niet meer, dan is de breuk zo eenvoudig "
                    "als ze kan zijn. Voor een gelijke breuk zoeken werkt het net zo, maar dan "
                    "mag je ook maal doen.",
             waarom=[
                 "Kijk wat er met de noemer gebeurde en doe precies hetzelfde met de teller. "
                 "Bij a) gaat \\(3\\) naar \\(9\\), dus maal \\(3\\); dan wordt de teller "
                 "\\(1\\) ook maal \\(3\\).",
                 "Hier gaat het de andere kant op: delen. Zie je niet meteen door welk getal, "
                 "deel dan twee keer door \\(2\\) of \\(3\\) in plaats van in één keer. "
                 f"{B(18, 24)} door \\(2\\) is {B(9, 12)}, en dan door \\(3\\) is {B(3, 4)}.",
                 f"De drie andere worden allemaal {B(1, 3)} als je vereenvoudigt. {B(3, 8)} kan "
                 "niet vereenvoudigd worden: \\(3\\) en \\(8\\) hebben geen enkele deler samen.",
                 None,
             ]),
        dict(aanpak="Hebben twee breuken <strong>dezelfde noemer</strong>, dan tel je gewoon de "
                    "tellers op of trek je ze af, en de noemer blijft staan. Je telt stukken van "
                    "dezelfde maat. Een breuk <em>van</em> een getal nemen is iets anders: eerst "
                    "<strong>delen</strong> door de noemer, dan <strong>maal</strong> de teller.",
             waarom=[
                 "Bij b), c) en e) mag het antwoord vereenvoudigd worden, maar het moet niet: "
                 f"{B(6, 9)} en {B(2, 3)} zijn allebei juist. Bij f) haal je alles er weer af, "
                 "en dan blijft er niets over: \\(0\\).",
                 "Twee stappen, altijd in deze volgorde. Bij b) eerst \\(40 : 5 = 8\\), dat is "
                 f"{B(1, 5)} van \\(40\\); dan \\(8 \\cdot 3 = 24\\). Wie eerst maal doet, komt "
                 "bij grote getallen snel vast te zitten.",
                 "Let op wat er gevraagd wordt: niet hoeveel kinderen een bril dragen, maar "
                 "hoeveel er géén dragen. Dat is één stap meer dan de breuk zelf.",
                 None,
             ]),
        dict(aanpak="Breuk, kommagetal en procent zijn <strong>drie namen voor hetzelfde</strong>. "
                    "Van breuk naar kommagetal: teller gedeeld door noemer. Van kommagetal naar "
                    "procent: maal \\(100\\). Bij een procent van een getal zoek je eerst een "
                    "handig stuk: \\(10\\,\\%\\) is delen door \\(10\\), \\(50\\,\\%\\) is de "
                    "helft, \\(25\\,\\%\\) is de helft van de helft.",
             waarom=[
                 "De onderste twee rijen gaan de andere kant op: daar staat het kommagetal of het "
                 f"procent al, en moet je de breuk zoeken. \\(0{{,}}2\\) is {B(2, 10)}, en dat "
                 f"vereenvoudigd {B(1, 5)}.",
                 f"{B(3, 4)} is \\(0{{,}}75\\) en dat is meer dan \\(0{{,}}7\\). Zet ze altijd "
                 "eerst in dezelfde vorm voor je vergelijkt; naast elkaar gelegd lijken \\(0{,}7\\) "
                 "en een breuk anders onvergelijkbaar.",
                 "Allebei betekenen ze: door twee. Dat is het handigste procent om te kennen, "
                 "want je hebt er geen rekenwerk voor nodig.",
                 "Zoek bij elk van deze eerst \\(10\\,\\%\\), dus het getal door \\(10\\). Bij e) "
                 "is \\(10\\,\\%\\) van \\(45\\) gelijk aan \\(4{,}5\\), en \\(20\\,\\%\\) is dus "
                 "het dubbele: \\(9\\). Bij f) is \\(5\\,\\%\\) de helft van \\(10\\,\\%\\).",
                 None,
                 None,
             ]),
        dict(aanpak="Er is één vaste volgorde: <strong>haakjes eerst</strong>, dan "
                    "<strong>maal en delen</strong>, en pas daarna <strong>plus en min</strong>. "
                    "Staan er alleen maal en delen, of alleen plus en min, dan werk je van links "
                    "naar rechts. Zet in gedachten haakjes om het stuk dat eerst moet, dan zie je "
                    "het staan.",
             waarom=[
                 "Deze zes zijn hoofdrekenwerk zonder valkuil. Bij e) is \\(25 \\cdot 8\\) "
                 "makkelijker als je het leest als \\(25 \\cdot 4 \\cdot 2\\): \\(100\\) maal "
                 "\\(2\\).",
                 "Vergelijk a) met b) en e) met f): dezelfde getallen, alleen de haakjes "
                 "verschillen, en het antwoord is helemaal anders. Dat is precies waarvoor "
                 "haakjes dienen.",
                 "Maal gaat voor plus, dus eerst \\(3 \\cdot 2 = 6\\) en dan \\(7 + 6 = 13\\). "
                 "Van links naar rechts zou \\(20\\) geven, en dat is fout.",
                 "Met komma's verandert de volgorde niet, alleen het rekenen. Zet bij plus en min "
                 "de komma's onder elkaar; bij maal en delen door \\(10\\), \\(100\\) of "
                 "\\(1\\,000\\) schuift de komma.",
                 None,
             ]),
        dict(aanpak="Afronden doe je door te kijken naar het cijfer <strong>rechts van de "
                    "plaats</strong> waarop je afrondt: is dat \\(5\\) of meer, dan ga je naar "
                    "boven, anders naar beneden. Bij de laatste twee oefeningen is er meer dan "
                    "één goed antwoord; daar telt vooral of je kan uitleggen hoe je eraan komt.",
             waarom=[
                 "Kijk telkens naar één cijfer, en niet naar het hele staartje. Bij b) rond je af "
                 "op het honderdtal, dus kijk je naar de \\(4\\) van de tientallen: dat is minder "
                 "dan \\(5\\), dus naar beneden, \\(3\\,700\\). De \\(8\\) erachter doet niet mee.",
                 "Eerst dezelfde eenheid, dan pas delen. Meters en centimeters door elkaar is de "
                 "meest gemaakte fout bij dit soort vraagjes.",
                 None,
                 "Hier is geen enkel antwoord fout zolang het "
                 f"{B(3, 4)} oplevert. Vraag je kind er twee die er echt anders uitzien: een som "
                 "met breuken en een met een procent, bijvoorbeeld.",
             ]),
    ],
)


UITLEGBLADEN["oefenbundel-getallenkennis"] = dict(
    reeksen=[
        dict(aanpak="Een cijfer is niet hetzelfde als een getal. Wat een cijfer waard is, hangt "
                    "af van de <strong>plaats</strong> waar het staat: eenheden, tientallen, "
                    "honderdtallen, duizendtallen. Schrijf een lang getal gerust even in groepjes "
                    "van drie, zoals \(6\,843\): dan zie je de plaatsen in één oogopslag.",
             waarom=[
                 "Tel de plaatsen van rechts naar links: eenheden, tientallen, honderdtallen, "
                 "duizendtallen. De \(8\) in \(6\,843\) staat op de derde plaats, dus "
                 "\(8\) honderdtallen, dus \(800\).",
                 "Let op het verschil met de vorige oefening. Hier wordt niet gevraagd wat één "
                 "cijfer waard is, maar hoeveel tientallen er in het <em>hele</em> getal zitten. "
                 "Dat is het getal gedeeld door \(10\): \(3\,600 : 10 = 360\).",
                 "Zet eerst het miljoen neer en leg de duizendtallen erbij: \(4\,000\,000\) "
                 "plus \(600\,000\). In groepjes van drie schrijven houdt het aantal nullen "
                 "overzichtelijk.",
                 None,
                 "Kijk eerst <strong>hoeveel cijfers</strong> elk getal heeft: een getal van vier "
                 "cijfers is altijd kleiner dan een van vijf. Pas bij evenveel cijfers vergelijk "
                 "je cijfer per cijfer van links naar rechts.",
                 "De eerste vijf staat bij de duizendtallen en is \(5\,000\) waard, de tweede "
                 "staat bij de tientallen en is \(50\) waard. Honderd keer zoveel.",
             ]),
        dict(aanpak="Vergelijk kommagetallen plaats per plaats, niet op lengte. Vul in gedachten "
                    "nullen aan tot ze even lang zijn: \(0{,}5\) is \(0{,}50\), en dan zie je "
                    "meteen dat \(0{,}45\) kleiner is. Afronden doe je door te kijken naar het "
                    "cijfer <strong>rechts van de plaats</strong> waarop je afrondt: \(5\) of "
                    "meer gaat naar boven.",
             waarom=[
                 "Meer cijfers achter de komma betekent niet een groter getal. Vul aan tot ze "
                 "even lang zijn: bij a) \(0{,}45\) tegenover \(0{,}50\), bij b) "
                 "\(2{,}08\) tegenover \(2{,}80\). Bij c) verandert een nul achteraan niets.",
                 "Kijk telkens naar één cijfer. Bij d) rond je af op een geheel getal, dus kijk "
                 "je naar de \(4\) van de tienden: minder dan \(5\), dus naar beneden, "
                 "\(12\). De \(5\) daarachter doet niet mee.",
                 None,
                 "De komma schuift: maal \(10\) is één plaats naar rechts, maal \(100\) twee "
                 "plaatsen, en delen is dezelfde beweging naar links. Tel de nullen, dat is het "
                 "aantal plaatsen.",
                 None,
             ]),
        dict(aanpak="Je hoeft niet te delen om te weten of iets deelbaar is. Door \(2\): het "
                    "laatste cijfer is even. Door \(5\): het eindigt op \(0\) of \(5\). "
                    "Door \(3\): de som van de cijfers is deelbaar door \(3\). Door \(4\): "
                    "de laatste twee cijfers samen zijn deelbaar door \(4\). Door \(6\): de "
                    "regel van \(2\) én die van \(3\), allebei.",
             waarom=[
                 "\(234\) is even, dus deelbaar door \(2\), en \(2 + 3 + 4 = 9\), dus ook "
                 "deelbaar door \(3\). Allebei, dus deelbaar door \(6\).",
                 "Kijk enkel naar de laatste twee cijfers. Bij a) is dat \(16\), en \(16\) "
                 "kan door \(4\). Bij b) is dat \(22\), en dat kan niet, al is \(522\) wel "
                 "even.",
                 "Een priemgetal heeft precies twee delers: \(1\) en zichzelf. \(21\) is "
                 "\(3 \cdot 7\), \(27\) is \(3 \cdot 9\) en \(33\) is \(3 \cdot 11\). "
                 "Bij \(29\) lukt het met geen enkel getal.",
                 "Zoek ze in paren, dan vergeet je er geen: \(1\) en \(24\), \(2\) en "
                 "\(12\), \(3\) en \(8\), \(4\) en \(6\). Je stopt waar de twee "
                 "getallen van een paar elkaar kruisen.",
                 "Omgekeerd klopt het wel: wie door \(6\) kan, kan altijd door \(3\). Maar "
                 "\(9\) is deelbaar door \(3\) en niet door \(6\), want \(9\) is oneven.",
             ]),
        dict(aanpak="Teken in gedachten een getallenlijn met nul in het midden. Hoe verder naar "
                    "<strong>links</strong>, hoe kleiner. Bij getallen onder nul betekent een "
                    "groter cijfer dus een kleiner getal: \(-12\) ligt verder links dan "
                    "\(-3\).",
             waarom=[
                 "Zet eerst de getallen onder nul, van het grootste cijfer naar het kleinste, en "
                 "daarna nul en de getallen erboven.",
                 "Lees het als stappen op de lijn. Bij a) sta je op \(-4\) en zet je \(7\) "
                 "stappen naar rechts: je komt op \(3\) uit. Bij b) sta je op \(2\) en ga je "
                 "\(9\) naar links, dus voorbij nul.",
                 "\(-20\) ligt verder naar links dan \(-2\), dus is het kleiner. Dat voelt "
                 "vreemd, want \(20\) is wél groter dan \(2\).",
                 None,
             ]),
        dict(aanpak="Kijk eerst naar het <strong>verschil</strong> tussen twee getallen die na "
                    "elkaar komen. Blijft dat verschil gelijk, dan gaat er telkens evenveel bij "
                    "of af. Wordt het verschil almaar groter, kijk dan of er telkens maal gedaan "
                    "wordt. Lukt geen van beide, probeer dan maal en er nog iets bij.",
             waarom=[
                 "Bij d) verdubbelt het verschil telkens: van \(2\) naar \(5\) is \(3\), "
                 "van \(5\) naar \(11\) is \(6\), van \(11\) naar \(23\) is \(12\). "
                 "Dat wijst op maal \(2\), en er komt telkens \(1\) bij.",
                 None,
                 "Hier bestaat geen fout antwoord, zolang de regel voor <em>elke</em> stap van de "
                 "rij klopt. Laat je kind de regel hardop zeggen en ze samen natellen.",
             ]),
        dict(aanpak="Deze oefeningen halen uit alle reeksen hierboven tegelijk. Lees de vraag "
                    "twee keer en zoek eerst welk stuk leerstof eronder zit, voor je begint te "
                    "rekenen.",
             waarom=[
                 None,
                 "Bij b) rond je af op het tienduizendtal, dus kijk je naar de \(4\) van de "
                 "duizendtallen: minder dan \(5\), dus naar beneden. Dat a) naar boven ging, "
                 "verandert daar niets aan: je rondt telkens het oorspronkelijke getal af en "
                 "nooit je eigen afronding.",
                 "Vul aan tot ze even lang zijn: \(0{,}9000\) tegenover \(0{,}8900\), "
                 "\(0{,}8910\) en \(0{,}8909\). Meer cijfers achter de komma maakt een getal "
                 "niet groter.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-bewerkingen"] = dict(
    reeksen=[
        dict(aanpak="Bij optellen mag je de getallen in een andere volgorde zetten als dat "
                    "handiger uitkomt. Zoek twee die samen een <strong>rond getal</strong> geven. "
                    "Cijfer je toch, zet dan de eenheden onder de eenheden en de tientallen onder "
                    "de tientallen.",
             waarom=[
                 "Bij b) en d) staat er een rond getal vooraan. Tel dan <em>aan</em> in plaats "
                 "van af te trekken: van \\(638\\) naar \\(640\\) is \\(2\\), en van \\(640\\) "
                 "naar \\(1\\,000\\) is \\(360\\), samen \\(362\\).",
                 None,
                 "Optellen mag in elke volgorde. \\(250\\) en \\(50\\) geven samen \\(300\\), en "
                 "dan blijft er maar één som over.",
             ]),
        dict(aanpak="Zoek eerst een handige weg. Maal \\(5\\) is maal \\(10\\) en dan de helft. "
                    "Maal \\(99\\) is maal \\(100\\) en er eentje af. Bij delen helpt het om het "
                    "getal in stukken te hakken: \\(684\\) is \\(600\\) plus \\(84\\).",
             waarom=[
                 None,
                 "Bij a) is maal \\(5\\) hetzelfde als maal \\(10\\) en dan de helft: \\(480\\) "
                 "wordt \\(240\\). Bij d) hak je \\(684\\) in \\(600\\) en \\(84\\): "
                 "\\(100\\) plus \\(14\\) is \\(114\\).",
                 "a) \\(4 \\cdot 100 = 400\\), en er gaat vier keer één af. b) maal \\(50\\) is "
                 "de helft van maal \\(100\\). c) \\(125 \\cdot 8 = 1\\,000\\): die is het waard "
                 "om te onthouden. d) maal \\(20\\) en er zes af.",
                 "Maal mag in elke volgorde. \\(4 \\cdot 5 = 20\\), en dan nog maal \\(6\\).",
                 "Delen mag dat net niet. Van links naar rechts: \\(60 : 6 = 10\\), dan "
                 "\\(: 2 = 5\\). Doe je eerst \\(6 : 2 = 3\\), dan krijg je \\(60 : 3 = 20\\), en "
                 "dat is iets heel anders.",
                 None,
                 "Hier moet je naar <strong>boven</strong> afronden, ook al zegt de deling "
                 "\\(4\\) met rest \\(2\\). Twee kinderen kan je niet thuislaten, dus er moet een "
                 "vijfde bus komen.",
             ]),
        dict(aanpak="Haakjes eerst, dan maal en gedeeld, dan plus en min. Zet in gedachten "
                    "haakjes om het stuk dat eerst moet, dan valt de som vanzelf in twee stappen "
                    "uiteen.",
             waarom=[
                 "Vergelijk a) met b) en e) met f): dezelfde getallen, alleen de haakjes "
                 "verschillen, en het antwoord is helemaal anders.",
                 "Net omgekeerd: haakjes gaan vóór alles. Maal en gedeeld gaan enkel voor op plus "
                 "en min.",
                 "Zonder haakjes doe je eerst \\(8 : 4 = 2\\) en dan \\(12 + 2 = 14\\). Zet je de "
                 "haakjes rond \\(12 + 8\\), dan deel je \\(20\\) door \\(4\\).",
             ]),
        dict(aanpak="Een breuk <em>van</em> een getal: eerst <strong>delen</strong> door de "
                    "noemer, dan <strong>maal</strong> de teller. Optellen en aftrekken met "
                    "dezelfde noemer: tellers samen, noemer blijft staan. Bij een procent bouw je "
                    "op vanaf \\(10\\,\\%\\), dat is het getal door \\(10\\).",
             waarom=[
                 "Bij a) eerst \\(45 : 5 = 9\\), dan \\(9 \\cdot 2 = 18\\). Bij d) en f) mag je "
                 "het antwoord vereenvoudigen, maar het moet niet.",
                 "Bouw op vanaf \\(10\\,\\%\\). Bij a) is \\(10\\,\\%\\) van \\(400\\) gelijk aan "
                 "\\(40\\) en \\(5\\,\\%\\) is \\(20\\), samen \\(60\\). Bij d) is "
                 "\\(40\\,\\%\\) vier keer \\(10\\,\\%\\).",
                 None,
             ]),
        dict(aanpak="Zet bij plus en min de komma's recht onder elkaar en vul achteraan nullen "
                    "aan tot de twee getallen even lang zijn. Bij maal en gedeeld hoeft dat niet: "
                    "reken zonder komma en zet ze op het einde terug.",
             waarom=[
                 "Bij b) schrijf je \\(10\\) als \\(10{,}0\\). Bij c) is maal \\(0{,}25\\) "
                 "hetzelfde als delen door \\(4\\). Bij e) is \\(1{,}25\\) precies een achtste "
                 "van \\(10\\), dus maal \\(8\\) geeft \\(10\\).",
                 None,
                 "Terugtellen gaat vlotter dan aftrekken: van \\(13{,}45\\) naar \\(14\\) is "
                 "\\(0{,}55\\), en van \\(14\\) naar \\(20\\) is \\(6\\). Samen \\(6{,}55\\).",
             ]),
        dict(aanpak="Schrijf eerst in woorden op wát je zoekt, en pas daarna de som. Kijk op het "
                    "einde of je antwoord redelijk is: een fietser die \\(450\\) km op een dag "
                    "doet, klopt niet.",
             waarom=[
                 None,
                 "Een half uur is de helft van \\(18\\), dus \\(9\\). Reken de hele uren en het "
                 "halve apart uit; dat gaat vlotter dan maal \\(2{,}5\\) in één keer.",
                 None,
                 "Alles mag, zolang de haakjes echt nodig zijn. Een som als \\(100 + 0\\) telt "
                 "niet mee: daar doen de haakjes niets.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-meten-en-metend-rekenen"] = dict(
    reeksen=[
        dict(aanpak="Zet de ladder in je hoofd: km, hm, dam, m, dm, cm, mm. Elke stap naar "
                    "beneden is maal \\(10\\), elke stap naar boven is gedeeld door \\(10\\). "
                    "Tel dus eerst de stappen, en pas daarna reken je.",
             waarom=[
                 "Van m naar cm zijn het twee stappen naar beneden, dus twee keer maal "
                 "\\(10\\), samen maal \\(100\\): \\(4{,}2\\) wordt \\(420\\). Naar boven "
                 "deel je, en dan komt er een komma in.",
                 "Een boek meet je in centimeter: een dik boek is een centimeter of drie. "
                 "Millimeter is te fijn om een boek in uit te drukken, meter veel te groot.",
                 "Een centimeter is tien millimeter, dus een millimeter is het tiende deel "
                 "van een centimeter.",
             ]),
        dict(aanpak="Omtrek is de lengte van de rand: tel alle zijden op, en het antwoord "
                    "staat in cm of m. Oppervlakte is lengte maal breedte, en het antwoord "
                    "staat in <strong>vierkante</strong> cm of m. Teken het figuurtje erbij; "
                    "dan zie je meteen welke van de twee je nodig hebt.",
             waarom=[
                 "Bij een rechthoek telt elke zijde twee keer mee: \\(11 + 5 + 11 + 5\\), of "
                 "korter \\(2 \\cdot (11 + 5)\\). Bij een vierkant is de omtrek vier keer de "
                 "zijde.",
                 None,
                 None,
                 "Lengte en breedte samen zijn de <strong>helft</strong> van de omtrek. Dat is "
                 "de stap die vaak wordt overgeslagen: eerst delen door \\(2\\), en pas daarna "
                 "de lengte eraf.",
                 "Neem een rechthoek van \\(1\\) bij \\(7\\) en een van \\(4\\) bij \\(4\\): "
                 "allebei een omtrek van \\(16\\), maar de oppervlakte is \\(7\\) tegenover "
                 "\\(16\\). Hoe meer een rechthoek op een vierkant lijkt, hoe groter zijn "
                 "oppervlakte bij dezelfde omtrek.",
             ]),
        dict(aanpak="Voor liter en gram geldt dezelfde ladder als voor meter: <em>kilo</em> is "
                    "duizend keer zoveel, <em>milli</em> is duizend keer minder. Zet bij "
                    "vergelijken eerst alles in dezelfde eenheid, anders vergelijk je de "
                    "getallen in plaats van de hoeveelheden.",
             waarom=[
                 "Van l naar ml zijn het drie stappen, dus maal \\(1\\,000\\); van g naar mg "
                 "ook. Van l naar cl zijn het er maar twee, dus maal \\(100\\).",
                 "Zet eerst alles in gram: \\(500\\) g, \\(750\\) g, \\(400\\) g en "
                 "\\(1{,}2\\) g. Het getal met de grootste cijfers is hier dus net het lichtste.",
                 None,
                 "De inhoud van een kubus is ribbe maal ribbe maal ribbe: drie keer, want een "
                 "kubus heeft lengte, breedte én hoogte. Daarom staat er een kleine \\(3\\) "
                 "bij cm.",
             ]),
        dict(aanpak="Tijd gaat niet per tien maar per zestig: een uur is \\(60\\) minuten, een "
                    "minuut \\(60\\) seconden. Reken bij een klok daarom in twee stukken: "
                    "eerst tot het volgende hele uur, en dan de rest erbij.",
             waarom=[
                 "Bij e) is een half uur \\(30\\) minuten, en elke minuut telt \\(60\\) "
                 "seconden: \\(30 \\cdot 60 = 1\\,800\\). Bij f) reken je \\(7\\) dagen maal "
                 "\\(24\\) uur.",
                 None,
                 "Van 7.55 u naar 8.00 u is \\(5\\) minuten. Dan nog \\(2\\) uur tot 10.00 u, "
                 "en de \\(35\\) minuten die overblijven brengen je op 10.35 u.",
                 "Half drie betekent een half uur <em>vóór</em> drie, niet erna. In het "
                 "Nederlands telt een half uur vooruit naar het volgende uur.",
             ]),
        dict(aanpak="Teken bij temperatuur een lijn met nul in het midden; dan zie je of je er "
                    "overheen gaat. Bij alles door elkaar is de eerste vraag altijd dezelfde: "
                    "staat alles al in dezelfde eenheid?",
             waarom=[
                 "Bij c) tel je de twee stukken op: van \\(-4\\) naar \\(0\\) is \\(4\\) graden "
                 "en van \\(0\\) naar \\(12\\) is er \\(12\\), samen \\(16\\).",
                 "Nul is hier het warmst, want alle andere liggen eronder. Bij minusgetallen "
                 "geldt: hoe groter het getal na het minteken, hoe kouder.",
                 "Een vierkante meter is een vierkant van \\(100\\) cm bij \\(100\\) cm, dus "
                 "\\(10\\,000\\) vierkante centimeter. Bij oppervlakte is elke stap maal "
                 "honderd in plaats van maal tien.",
                 None,
                 "Hier rond je naar <strong>beneden</strong> af, anders dan bij een vraag over "
                 "bussen of dozen: een vijfde stuk van \\(240\\) cm zit er niet meer in. De "
                 "\\(40\\) cm die overblijft hoort bij het antwoord.",
                 "Een goede vraag heeft twee eenheden in zich, bijvoorbeeld gram en kilogram. "
                 "Laat je kind het antwoord ook zelf narekenen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-meetkunde"] = dict(
    reeksen=[
        dict(aanpak="Vergelijk elke hoek met de hoek van een blad papier: die is precies "
                    "\\(90^{\\circ}\\). Past de hoek daarbinnen, dan is hij scherp; is hij "
                    "wijder, dan is hij stomp. Een gestrekte hoek is gewoon een rechte lijn, "
                    "\\(180^{\\circ}\\).",
             waarom=[
                 None,
                 "De hoeken van een driehoek zijn samen \\(180^{\\circ}\\), die van een "
                 "vierhoek samen \\(360^{\\circ}\\). Je trekt dus af van \\(180\\) of van "
                 "\\(360\\). Een hele draai is \\(360^{\\circ}\\), dus een kwartdraai is "
                 "\\(90^{\\circ}\\).",
                 None,
                 "Stomp betekent groter dan \\(90^{\\circ}\\), maar kleiner dan "
                 "\\(180^{\\circ}\\).",
             ]),
        dict(aanpak="Tel eerst de zijden: dat geeft de naam. Kijk daarna of de zijden even lang "
                    "zijn en of de hoeken recht zijn; dát maakt het verschil tussen een ruit, "
                    "een rechthoek en een vierkant.",
             waarom=[
                 "Een ruit heeft vier even lange zijden, maar geen rechte hoeken. Een trapezium "
                 "heeft precies twee evenwijdige zijden.",
                 None,
                 None,
                 "Vouw de figuur in gedachten dubbel. Bij een vierkant lukt dat vier keer: twee "
                 "keer door het midden en twee keer over een diagonaal. Bij een rechthoek lukt "
                 "de diagonaal niet, want de twee helften passen dan niet op elkaar.",
                 "Omgekeerd klopt het wél: elk vierkant is een ruit, want zijn vier zijden zijn "
                 "even lang. Maar een ruit heeft niet altijd rechte hoeken.",
             ]),
        dict(aanpak="Straal en diameter schelen maar één rekenstap: maal twee of gedeeld door "
                    "twee. Op je passer zet je de <strong>straal</strong>, want dat is de "
                    "afstand tussen de punt en het potlood.",
             waarom=[
                 "Twee keer de straal is de diameter, de helft van de diameter is de straal. "
                 "Bij c) blijft er een komma staan, en dat mag.",
                 None,
                 "Dat geldt voor elke cirkel, hoe groot of klein ook. Daarom staat er altijd "
                 "bij of een getal de straal of de diameter is.",
             ]),
        dict(aanpak="Vlakken zijn de kanten die je kan aanraken, ribben zijn de lijnen waar twee "
                    "vlakken samenkomen, hoekpunten zijn de puntjes. Tel bij een piramide of een "
                    "prisma eerst het grondvlak en daarna de rest; zo vergeet je er geen.",
             waarom=[
                 "Een balk heeft zes rechthoekige vlakken, een kegel een rond grondvlak en een "
                 "punt, een cilinder twee ronde vlakken, en een bol heeft er maar één, dat "
                 "helemaal rond is.",
                 "Bij de piramide: het driehoekige grondvlak plus drie zijvlakken is \\(4\\). "
                 "Bij het prisma: twee driehoeken plus drie rechthoeken is \\(5\\), met "
                 "\\(9\\) ribben en \\(6\\) hoekpunten.",
                 None,
                 "Een cilinder heeft wel twee randen, maar die lopen rond: er is nergens een "
                 "punt waar lijnen samenkomen.",
             ]),
        dict(aanpak="Leg bij spiegelen een denkbeeldige spiegel op de as en kijk wat er met "
                    "links en rechts gebeurt. Bij verschuiven gaat de hele figuur in dezelfde "
                    "richting mee, zonder te draaien en zonder te spiegelen.",
             waarom=[
                 None,
                 None,
                 "Verschuiven is enkel opschuiven. Draaien is een aparte beweging; die heet een "
                 "rotatie.",
             ]),
        dict(aanpak="Lees de vraag twee keer en kijk welk stuk meetkunde erin zit: een hoek, een "
                    "figuur, een omtrek of een spiegeling. Pak daarna de aanpak van die reeks "
                    "er weer bij.",
             waarom=[
                 "Een gelijkzijdige driehoek heeft er drie, een rechthoek twee, een ruit twee. "
                 "Alleen een driehoek met drie verschillende zijden is nergens dubbel te vouwen.",
                 None,
                 "Laat je kind de beschrijving voorlezen terwijl jij tekent zonder te kijken. "
                 "Wat jij dan niet kan tekenen, ontbreekt in de beschrijving: dat is meteen de "
                 "verbetering.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-kansrekenen-en-statistiek"] = dict(
    reeksen=[
        dict(aanpak="Een kans is altijd een breuk: bovenaan wat je wil, onderaan alles wat kan. "
                    "Tel dus eerst het totaal, en pas daarna het aantal dat meetelt. Een kans "
                    "ligt tussen \\(0\\) (kan niet) en \\(1\\) (zeker).",
             waarom=[
                 "Bij f) hoef je de kleuren niet apart te tellen: alles wat niet groen is, zijn "
                 "de vier rode plus de zes blauwe. Of korter: \\(12 - 2\\).",
                 "Bij een munt is het \\(1\\) op \\(2\\), bij groen \\(2\\) op \\(12\\), en geel "
                 "kan niet. Zet de kansen in dezelfde vorm naast elkaar, dan zie je het meteen.",
                 "Kans \\(0\\) betekent dat het niet kan, kans \\(1\\) dat het zeker gebeurt. "
                 "Alles daartussen schrijf je als een breuk of een procent.",
                 None,
             ]),
        dict(aanpak="Drie dingen die vaak door elkaar lopen. Het <strong>gemiddelde</strong> "
                    "reken je uit: alles optellen en delen door het aantal. Het "
                    "<strong>middelste</strong> getal vind je door eerst te sorteren. Het getal "
                    "dat het <strong>vaakst</strong> voorkomt tel je gewoon.",
             waarom=[
                 "Bij d) zie je goed waarom het gemiddelde niet hetzelfde is als het middelste: "
                 "dat ene grote getal \\(10\\) trekt het gemiddelde omhoog, terwijl drie van de "
                 "vier getallen eronder blijven.",
                 None,
                 "Reken na met \\(5\\), \\(9\\) en \\(13\\): daar is het gemiddelde \\(9\\), en "
                 "dat staat er wél bij. Maar bij \\(10\\) en \\(11\\) is het gemiddelde "
                 "\\(10{,}5\\), en dat getal staat er niet bij.",
                 None,
             ]),
        dict(aanpak="Een lijngrafiek toont een verloop in de tijd, een staafdiagram vergelijkt "
                    "groepen naast elkaar, en een cirkeldiagram toont delen van één geheel. Lees "
                    "bij een grafiek altijd eerst wat er op de twee assen staat.",
             waarom=[
                 "Temperatuur verandert geleidelijk, en een lijn laat dat verloop zien. Met een "
                 "staaf per uur zou je de getallen wel kloppen, maar niet zien wanneer het "
                 "steeg of daalde.",
                 "Bij d) is \\(6\\) van de \\(24\\) precies een vierde. Deel teller en noemer "
                 "door \\(6\\), dan staat er het stuk dat je herkent.",
                 None,
             ]),
        dict(aanpak="Zoek bij elke vraag eerst wát er gevraagd wordt: een deel van een geheel "
                    "(dan is het een procent of een kans), of iets terugrekenen uit een "
                    "gemiddelde. Een procent is altijd <em>per honderd</em>.",
             waarom=[
                 None,
                 "Hier reken je terug. Het gemiddelde maal het aantal dagen geeft de som van "
                 "alle dagen samen, en daar trek je af wat je al kent.",
                 "De helft is \\(50\\,\\%\\), want \\(50\\) van de \\(100\\). "
                 "\\(25\\,\\%\\) is een vierde.",
                 "Er zijn meer witte dan zwarte, dus wit is waarschijnlijker. Maar zeker is het "
                 "nooit: er zitten er ook drie zwarte in.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-vraagstukken-en-problemen-oplossen"] = dict(
    reeksen=[
        dict(aanpak="Lees het vraagstuk twee keer: één keer om te weten waarover het gaat, en "
                    "één keer met een potlood om de getallen én de vraag te onderstrepen. "
                    "Schrijf daarna in je eigen woorden op wat je zoekt; vaak staat de som er "
                    "dan al.",
             waarom=[
                 "De valkuil zit hier in de vraag: er wordt niet gevraagd hoeveel plaatsen er "
                 "zijn, maar hoeveel er overblijven. Daarom horen er twee bewerkingen bij: "
                 "eerst maal, dan min.",
                 None,
                 "Let op de eenheid: er wordt naar kilogram gevraagd terwijl alles in gram "
                 "staat. Reken alles eerst in gram uit en zet pas op het einde om.",
                 "Schatten is geen extra werk maar een controle. Wie vooraf denkt &#8220;het "
                 "wordt ongeveer honderd&#8221;, ziet meteen dat \\(1\\,000\\) niet kan kloppen.",
             ]),
        dict(aanpak="Bij een vraagstuk in twee stappen staat het antwoord van de eerste stap "
                    "nergens in de tekst: dat moet je zelf maken. Schrijf die tussenstap altijd "
                    "op mét het woord erbij (&#8220;de schriften kosten samen …&#8221;), anders "
                    "raak je hem onderweg kwijt.",
             waarom=[
                 None,
                 None,
                 "Hier moet je antwoorden met ja of nee <em>én</em> met een getal. Reken eerst "
                 "uit hoeveel de hond in vijf weken opeet, en vergelijk dat met wat er in de "
                 "zak zit.",
                 "Bij kinderen, bussen en dozen kan er geen half antwoord uitkomen. Komt er toch "
                 "een half uit, dan is er iets fout gelopen, of moet er afgerond worden, en dan "
                 "is de vraag naar welke kant.",
             ]),
        dict(aanpak="Zoek bij een verhouding eerst wat er bij <strong>één</strong> hoort: één "
                    "broodje, één persoon, één pot. Daarna maal het aantal dat gevraagd wordt. "
                    "Dat is één stap meer, maar het werkt altijd, ook met lastige getallen.",
             waarom=[
                 None,
                 None,
                 "Alles gaat hier maal twee: dubbel zoveel verf voor dubbel zoveel muren. Dat "
                 "mag enkel zolang alles even groot blijft; waren die tien muren twee keer zo "
                 "breed, dan klopt het niet meer.",
                 "Schaal \\(1\\) op \\(50\\,000\\) wil zeggen dat \\(1\\) cm op de kaart "
                 "\\(50\\,000\\) cm in het echt is. Het lastige stuk zit op het einde: van cm "
                 "naar km zijn het vijf stappen op de ladder.",
             ]),
        dict(aanpak="Hier is er niet één juiste weg. Laat je kind eerst zelf beginnen en vraag "
                    "achteraf hoe het eraan kwam; dat is meer waard dan het kortste pad. Een "
                    "plan opschrijven, al is het in drie regels, maakt een fout ook makkelijker "
                    "terug te vinden.",
             waarom=[
                 None,
                 "Vraag je kind hardop te vertellen wat het gedaan heeft. Wie de stappen kan "
                 "benoemen, kan ze ook op een volgend vraagstuk toepassen; wie enkel het "
                 "antwoord heeft, begint de volgende keer weer van nul.",
                 "Een vraagstuk in twee stappen herken je hieraan: het antwoord van de eerste "
                 "som staat nergens in de tekst. Lukt het meteen met één bewerking, dan is het "
                 "er maar één.",
             ]),
    ],
)

if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        if naam in UITLEGBLADEN:
            uitlegblad.schrijf(UITLEGBLADEN[naam], b, naam.replace("oefenbundel-", "uitlegblad-"))

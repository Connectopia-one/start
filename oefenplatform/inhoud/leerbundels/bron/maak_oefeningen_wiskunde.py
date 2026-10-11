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
import svg, oefenbundel, bundel

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
                  r"Alles tussen \(2{,}7\) en \(2{,}8\) is goed, bijvoorbeeld \(2{,}71 \cdot 2{,}75 \cdot 2{,}79\).", 1),
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


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)

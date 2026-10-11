# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij statistiek 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen, andere situaties, en opdrachten die je enkel op papier
kan maken (een hypothesepaar opschrijven, een boxplot tekenen, een besluit in
een volle zin formuleren). Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/statistiek.json` en naast de leerbundel van hetzelfde thema in
`maak_statistiek.py`.

Elke uitkomst in het antwoordblad is met Python nagerekend, niet uit het hoofd
opgeschreven. Bij een kans of een standaardafwijking staat er altijd bij op
hoeveel decimalen er afgerond is, want 0,2508 en 0,251 zijn niet hetzelfde
antwoord.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Statistiek"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

W = "95px"
WW = "150px"
WL = "230px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf eerst op wat je berekent, dan de getallen, en pas dan de uitkomst.",
    "Rond pas op het einde af, en op het aantal decimalen dat de opgave vraagt.",
    "Een rekenmachine mag. Het antwoordblad zit achteraan; scheur het eraf voor je begint.",
]

# ============================================================ 1
OEFENBUNDELS["oefenbundel-problemen-oplossen-en-ict-gebruiken-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Problemen oplossen en ICT gebruiken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vraagstuk of probleem",
             opdracht="Schrijf vraagstuk als de opgave zelf al zegt welke werkwijze je moet "
                      "gebruiken, en probleem als je die zelf moet kiezen.",
             oefeningen=[
                 ("rij", [(r"Bereken C(\(14\), \(4\)).", "vraagstuk"),
                          ("Bereken het gemiddelde van deze twintig getallen.", "vraagstuk")],
                  "Vraagstuk of probleem?", WW),
                 ("kort", r"Hoeveel mensen moet je bevragen om tot op \(3\) procent nauwkeurig "
                          "te zijn?", "probleem", WW),
                 ("kort", "Is deze dieetpil werkzaam? Je krijgt de cijfers van de proef.",
                  "probleem", WW),
                 ("open", "Leg in je eigen woorden uit waarom twee leerlingen bij een probleem "
                          "een ander pad mogen nemen en toch allebei alle punten kunnen halen.",
                  "Bij een probleem kiest de leerling zelf de strategie. Zolang de aanpak klopt, "
                  "de stappen navolgbaar zijn en het antwoord juist is, maakt het niet uit of je "
                  "eerst een tabel maakte of eerst alle gevallen opsomde.", 4),
             ]),
        dict(kop="Welke stap van de vier?",
             opdracht="Schrijf begrijpen, plan maken, uitvoeren of reflecteren.",
             oefeningen=[
                 ("kort", "Je onderstreept in de opgave wat er gevraagd wordt.", "begrijpen", WW),
                 ("kort", "Je beslist dat je dit met een combinatie gaat doen.", "plan maken", WW),
                 ("kort", "Je tikt de getallen in de kansrekenmachine.", "uitvoeren", WW),
                 ("kort", "Je kijkt of je kans wel tussen nul en één ligt.", "reflecteren", WW),
             ]),
        dict(kop="Kan dit antwoord kloppen?",
             opdracht="Omcirkel het juiste en schrijf er in één woord bij waarom.",
             oefeningen=[
                 ("kies", r"Je vindt als kans \(1{,}25\).", ["dat kan", "dat kan niet"], 1),
                 ("kies", r"Je vindt als \(p\)-waarde min \(0{,}03\).", ["dat kan", "dat kan niet"], 1),
                 ("kies", r"Je vindt als standaardafwijking \(0\).",
                  ["dat kan, als alle waarden gelijk zijn", "dat kan niet"], 0),
                 ("kies", r"Je vindt als correlatiecoëfficiënt r gelijk aan \(1{,}4\).",
                  ["dat kan", "dat kan niet"], 1),
             ]),
        dict(kop="Demathematiseren",
             opdracht="Zet je wiskundige uitkomst om in een antwoord op de vraag.",
             oefeningen=[
                 ("kort", r"Je rekent uit dat je steekproef \(148{,}3\) mensen groot moet zijn. "
                          "Hoeveel mensen bevraag je?", r"\(149\)", W),
                 ("kort", r"Je rekent uit dat je \(7{,}2\) dozen nodig hebt. Hoeveel koop je?", r"\(8\)", W),
                 ("open", r"Je vindt dat de kans op minstens één defect stuk \(0{,}271\) is. "
                          "Schrijf dat in een volle zin voor iemand die geen statistiek kent.",
                  "In ongeveer zevenentwintig van de honderd zendingen zit er minstens één defect "
                  "stuk. Of: de kans is ruim één op vier.", 3),
             ]),
        dict(kop="Welke heuristiek?",
             opdracht="Schrijf schets of tabel, opsommen, patroon zoeken, of gissen en testen.",
             oefeningen=[
                 ("kort", "Je schrijft alle zes de volgordes van drie letters op.", "opsommen", WW),
                 ("kort", r"Je rekent het geval \(n\) is \(2\) en \(n\) is \(3\) uit om de formule te zien.",
                  "patroon zoeken", WW),
                 ("open", "Noem één voordeel van alle mogelijkheden opsommen bij een klein "
                          "telprobleem, zelfs als je de formule al kent.",
                  "Je kan er je formule mee controleren: komt het opsommen op hetzelfde getal uit, "
                  "dan heb je de juiste telregel gekozen.", 3),
             ]),
    ],
)

# ============================================================ 2
OEFENBUNDELS["oefenbundel-de-telregels-product-som-en-complement-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De telregels: product, som en complement",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke regel?",
             opdracht="Schrijf product, som of complement.",
             oefeningen=[
                 ("rij", [("een voorgerecht én een dessert kiezen", "product"),
                          ("één taal óf één sport kiezen", "som")],
                  "Welke telregel?", "110px"),
                 ("kort", "de kans op minstens één zes bij vier worpen", "complement", "110px"),
                 ("kort", "een code van drie letters gevolgd door twee cijfers", "product", "110px"),
             ]),
        dict(kop="De productregel",
             opdracht="Bereken het aantal mogelijkheden. Schrijf je vermenigvuldiging erbij.",
             oefeningen=[
                 ("kort", r"Een menu met \(4\) voorgerechten, \(3\) hoofdgerechten en \(2\) desserts. "
                          "Hoeveel driegangenmenu's?", r"\(24\), want \(4 \cdot 3 \cdot 2\)", W),
                 ("kort", r"Een code van \(3\) letters \((26)\) gevolgd door \(2\) cijfers (\(0\) tot \(9\)), "
                          "herhaling mag. Hoeveel codes?", r"\(1\,757\,600\), want \(26^{3} \cdot 10^{2}\)", WW),
                 ("kort", r"Een hoorntje met \(2\) bollen uit \(8\) smaken, de volgorde telt en "
                          "tweemaal dezelfde smaak mag niet. Hoeveel hoorntjes?", r"\(56\), want \(8 \cdot 7\)", W),
                 ("kort", r"Een pincode van \(4\) cijfers die niet met een nul mag beginnen. "
                          "Hoeveel pincodes?", r"\(9000\), want \(9 \cdot 10 \cdot 10 \cdot 10\)", W),
                 ("open", "Bij het hoorntje hangt de tweede keuze van de eerste af. Leg uit "
                          "waarom je toch mag vermenigvuldigen.",
                  "Omdat er voor de tweede bol altijd precies zeven smaken overblijven, welke "
                  "eerste bol je ook nam. Zolang het aantal mogelijkheden van de tweede keuze "
                  "telkens hetzelfde is, mag je vermenigvuldigen.", 4),
             ]),
        dict(kop="De somregel",
             opdracht="Bereken, en let op overlapping.",
             oefeningen=[
                 ("kort", r"Een klas heeft \(14\) meisjes en \(9\) jongens. Je vaardigt één leerling af. "
                          "Hoeveel keuzes?", r"\(23\)", W),
                 ("kort", "Twintig leerlingen voetballen, veertien zwemmen, zes doen allebei. "
                          "Hoeveel sporten er minstens één van de twee?", r"\(28\), want \(20 + 14 - 6\)", WW),
                 ("waar", "Bij de somregel mag je de twee aantallen altijd gewoon optellen.", False),
             ]),
        dict(kop="De complementregel",
             opdracht="Reken met het tegengestelde geval. Rond kansen af op drie decimalen.",
             oefeningen=[
                 ("kort", "De kans op minstens één zes bij vier worpen met een dobbelsteen.",
                  r"\(0{,}518\) (precies \(\tfrac{671}{1296}\))", W),
                 ("kort", "De kans op minstens één keer kop bij vijf keer munten opgooien.",
                  r"\(0{,}969\) (precies \(\tfrac{31}{32}\))", W),
                 ("kort", r"\(10\) procent van de stukken is defect. De kans op minstens één defect "
                          "stuk in een zending van drie.", r"\(0{,}271\)", W),
                 ("open", "Leg uit waarom je bij een minstens-vraag bijna altijd met het "
                          "complement rekent.",
                  "Minstens één betekent één, twee, drie … tot alles, dus heel veel gevallen apart. "
                  "Het tegengestelde is één enkel geval: géén. Dat reken je in één keer uit en "
                  "trek je van één af.", 4),
             ]),
    ],
)

# ============================================================ 3
OEFENBUNDELS["oefenbundel-faculteit-en-combinaties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Faculteit en combinaties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Faculteit",
             opdracht="Bereken.",
             oefeningen=[
                 ("rij", [(r"\(4\)!", r"\(24\)"), (r"\(6\)!", r"\(720\)"), (r"\(0\)!", r"\(1\)")], "Bereken.", W),
                 ("rij", [(r"\(7!\)", r"\(5040\)"), (r"\(8!\)", r"\(40\,320\)"), (r"\(\dfrac{8!}{7!}\)", r"\(8\)")],
                  "Bereken.", W),
                 ("open", r"Waarom spreken we af dat \(0\)! gelijk is aan één?",
                  "Anders klopt de formule van de combinaties niet meer in de randgevallen. "
                  r"C(\(n\), \(0\)) moet één zijn, want er is precies één manier om niets te kiezen, en in "
                  r"de formule staat dan \(0\)! in de noemer.", 4),
             ]),
        dict(kop="Combinaties berekenen",
             opdracht="Bereken met de formule uit het formularium. Schrijf je uitwerking erbij.",
             oefeningen=[
                 ("rij", [(r"C(\(8\), \(2\))", r"\(28\)"), (r"C(\(9\), \(3\))", r"\(84\)"), (r"C(\(6\), \(4\))", r"\(15\)")],
                  "Bereken.", W),
                 ("rij", [(r"C(\(15\), \(2\))", r"\(105\)"), (r"C(\(12\), \(4\))", r"\(495\)"), (r"C(\(10\), \(7\))", r"\(120\)")],
                  "Bereken.", W),
                 ("kort", r"C(\(11\), \(8\)). Gebruik de eigenschap C(\(n\), \(p\)) = C(\(n\), \(n - p\)).",
                  r"\(165\), want C(\(11\), \(8\)) = C(\(11\), \(3\))", W),
                 ("kort", r"C(\(20\), \(3\)).", r"\(1140\)", W),
             ]),
        dict(kop="Volgorde of niet",
             opdracht="Schrijf combinatie of productregel, en bereken daarna.",
             oefeningen=[
                 ("kort", "Uit tien leerlingen een jury van drie kiezen.", r"combinatie, C(\(10\), \(3\)) = \(120\)", WW),
                 ("kort", "Uit tien leerlingen een voorzitter, een secretaris en een "
                          "penningmeester kiezen.", r"productregel, \(10 \cdot 9 \cdot 8 = 720\)", WW),
                 ("kort", "Twaalf mensen geven elkaar één keer een hand. Hoeveel handdrukken?",
                  r"combinatie, C(\(12\), \(2\)) = \(66\)", WW),
                 ("kort", r"Zes van de \(49\) getallen van de Lotto aankruisen.",
                  r"combinatie, C(\(49\), \(6\)) = \(13\,983\,816\)", WW),
             ]),
        dict(kop="De klassieke fout",
             opdracht="Zoek de fout en zet ze recht.",
             oefeningen=[
                 ("open", "Iemand moet uit negen spelers er vier kiezen en schrijft op: "
                          r"\(9 \cdot 8 \cdot 7 \cdot 6 = 3024\). Wat ging er mis, en wat is het juiste antwoord?",
                  r"Hij vergat door \(4\)! te delen, dus hij telde elk viertal \(24\) keer. Het juiste "
                  r"antwoord is \(3024 : 24\), dus C(\(9\), \(4\)) = \(126\).", 4),
                 ("waar", r"C(\(n\), \(p\)) is altijd een geheel getal, ook al staat er een breuk in de "
                          "formule.", True),
             ]),
    ],
)

# ============================================================ 4
OEFENBUNDELS["oefenbundel-kansvariabelen-en-de-binomiale-verdeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansvariabelen en de binomiale verdeling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Is het binomiaal?",
             opdracht="Schrijf ja of nee, en bij nee waarom niet.",
             oefeningen=[
                 ("kort", "twintig keer een munt opgooien, aantal keer kop", "ja", "90px"),
                 ("kort", "drie kaarten trekken zonder terugleggen, aantal harten",
                  "nee, de kans verandert na elke trekking", "90px"),
                 ("kort", r"honderd stukken controleren, elk \(3\,\%\) kans op defect", "ja", "90px"),
                 ("kort", "de lengte van vijftig leerlingen meten",
                  "nee, dat is geen aantal successen maar een meting", "90px"),
                 ("open", "Noem de vier voorwaarden waaraan een binomiale situatie moet voldoen.",
                  r"Een vast aantal pogingen \(n\), elke poging heeft maar twee uitkomsten, de kans \(p\) "
                  "op succes blijft bij elke poging gelijk, en de pogingen zijn onafhankelijk van "
                  "elkaar.", 4),
             ]),
        dict(kop="Kansen berekenen",
             opdracht="Reken uit met de kansrekenmachine. Rond af op drie decimalen.",
             oefeningen=[
                 ("kort", r"\(X \sim B(10; 0{,}4)\). Bereken \(P(X = 4)\).", r"\(0{,}251\,(0{,}2508)\)", W),
                 ("kort", r"\(X \sim B(12; 0{,}25)\). Bereken \(P(X = 3)\).", r"\(0{,}258\,(0{,}2581)\)", W),
                 ("kort", r"\(X \sim B(8; 0{,}5)\). Bereken \(P(X = 4)\).", r"\(0{,}273\,(0{,}2734)\)", W),
                 ("kort", r"\(X \sim B(20; 0{,}1)\). Bereken \(P(X = 0)\).", r"\(0{,}122\,(0{,}1216)\)", W),
                 ("kort", "Zes keer met een dobbelsteen: precies twee zessen.",
                  r"\(0{,}201\), met \(n = 6\) en \(p = \tfrac{1}{6}\)", W),
                 ("kort", r"\(X \sim B(5; 0{,}2)\). Bereken \(P(X \geq 1)\).",
                  r"\(0{,}672\), want \(1 - 0{,}8^{5}\)", W),
                 ("kort", r"\(X \sim B(10; 0{,}5)\). Bereken \(P(X \leq 3)\).", r"\(0{,}172\)", W),
             ]),
        dict(kop="Lezen en opschrijven",
             opdracht="Schrijf in symbolen of in woorden.",
             oefeningen=[
                 ("kort", "Schrijf in symbolen: vijftien onafhankelijke proeven die elk in "
                          r"\(80\) procent van de gevallen lukken.", r"\(X \sim B(15; 0{,}8)\)", WW),
                 ("open", r"Wat betekent \(P(X \geq 8)\) in woorden, als X het aantal juiste antwoorden "
                          "op twintig vragen is?",
                  "De kans dat je acht of meer vragen juist hebt.", 2),
                 ("waar", "Bij een binomiale verdeling mag je naar de kans op precies één waarde "
                          "vragen.", True),
             ]),
    ],
)

# ============================================================ 5
OEFENBUNDELS["oefenbundel-verwachtingswaarde-variantie-en-standaardafwijking-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verwachtingswaarde, variantie en standaardafwijking",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Bij een binomiale verdeling",
             opdracht=r"Bereken E(X), Var(X) en \(\sigma\). Rond \(\sigma\) af op twee decimalen.",
             oefeningen=[
                 ("tabel", ["X", "E(X)", "Var(X)", r"\(\sigma\)"],
                  [[r"\(B(10; 0{,}4)\)", None, None, None],
                   [r"\(B(20; 0{,}3)\)", None, None, None],
                   [r"\(B(50; 0{,}2)\)", None, None, None],
                   [r"\(B(8; 0{,}25)\)", None, None, None]],
                  r"\(B(10; 0{,}4)\): \(4 \cdot 2{,}4 \cdot 1{,}55\) — \(B(20; 0{,}3)\): \(6 \cdot 4{,}2 \cdot 2{,}05\) — "
                  r"\(B(50; 0{,}2)\): \(10 \cdot 8 \cdot 2{,}83\) — \(B(8; 0{,}25)\): \(2 \cdot 1{,}5 \cdot 1{,}22\)", "62px"),
                 ("kort", r"\(B(100; 0{,}6)\). Bereken \(\sigma\) op twee decimalen.", r"\(4{,}90\,(4{,}899)\)", W),
                 ("kort", r"\(B(12; 0{,}5)\). Bereken Var(X).", r"\(3\)", W),
             ]),
        dict(kop="Bij een tabel",
             opdracht=r"X heeft deze kansverdeling. Bereken E(X), Var(X) en \(\sigma\).",
             oefeningen=[
                 ("tekst", r"<p>X: \(0\) met kans \(0{,}1 \cdot 1\) met kans \(0{,}2 \cdot 2\) met kans \(0{,}4\) · "
                           r"\(3\) met kans \(0{,}3\)</p>"),
                 ("kort", "Bereken E(X).", r"\(1{,}9\)", W),
                 ("kort", "Bereken Var(X).", r"\(0{,}89\)", W),
                 ("kort", r"Bereken \(\sigma\) op twee decimalen.", r"\(0{,}94\,(0{,}9434)\)", W),
                 ("waar", r"De som van alle kansen in zo'n tabel moet één zijn.", True),
             ]),
        dict(kop="Begrijpen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Twee binomiale verdelingen hebben dezelfde E(X) maar een heel "
                          r"verschillende \(\sigma\). Wat zie je daarvan in de tekening?",
                  "De twee verdelingen liggen rond hetzelfde midden, maar de ene is smal en hoog "
                  r"en de andere breed en laag. Een grote \(\sigma\) betekent dat de uitkomsten verder "
                  "van het gemiddelde af kunnen liggen.", 4),
                 ("open", "Waarom kan de variantie nooit negatief zijn?",
                  "Je telt afwijkingen in het kwadraat op, en een kwadraat is nooit negatief. "
                  "Nul kan wel: dan liggen alle waarden op het gemiddelde.", 3),
                 ("kort", r"Wat is de eenheid van \(\sigma\), als X een aantal is?",
                  "hetzelfde aantal, dus dezelfde eenheid als X (de variantie staat in het kwadraat)", WL),
             ]),
    ],
)

# ============================================================ 6
OEFENBUNDELS["oefenbundel-de-normale-verdeling-en-standaardiseren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De normale verdeling en standaardiseren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Standaardiseren",
             opdracht=r"Bereken \(z\) met de formule \(z = \dfrac{x - \mu}{\sigma}\). "
                      "Rond af op twee decimalen.",
             oefeningen=[
                 ("tabel", ["x", "mu", r"\(\sigma\)", "z"],
                  [[r"\(85\)", r"\(70\)", r"\(10\)", None],
                   [r"\(162\)", r"\(170\)", r"\(8\)", None],
                   [r"\(520\)", r"\(500\)", r"\(25\)", None],
                   [r"\(37{,}8\)", r"\(37\)", r"\(0{,}5\)", None],
                   [r"\(12\)", r"\(15\)", r"\(2{,}5\)", None]],
                  r"\(1{,}50\) — \(-1{,}00\) — \(0{,}80\) — \(1{,}60\) — \(-1{,}20\)", "62px"),
                 ("open", r"Wat betekent een z-waarde van \(-1{,}20\) in woorden?",
                  r"Die waarde ligt \(1{,}20\) standaardafwijkingen onder het gemiddelde.", 3),
                 ("kort", "Welke letter gebruikt het formularium voor een standaardnormaal "
                          "verdeelde kansvariabele?", r"Z, met Z ~ \(N(0; 1)\)", WW),
             ]),
        dict(kop="De vuistregel 68 — 95 — 99,7",
             opdracht="Gebruik de vuistregel. Antwoorden in procent.",
             oefeningen=[
                 ("kort", r"Hoeveel procent ligt tussen \(\mu\) − \(\sigma\) en \(\mu\) + \(\sigma\)?", r"ongeveer \(68\,\%\)", W),
                 ("kort", r"Hoeveel procent ligt tussen \(\mu\) \(- 2\) \(\sigma\) en \(\mu\) + \(2\) \(\sigma\)?", r"ongeveer \(95\,\%\)", W),
                 ("kort", r"Hoeveel procent ligt bóven \(\mu\) + \(2\) \(\sigma\)?",
                  r"ongeveer \(2{,}5\,\%\), want de \(5\,\%\) die overblijft verdeelt zich over twee staarten", WL),
                 ("kort", r"De lengte van mannen is \(N(178; 7)\). Tussen welke twee lengtes ligt "
                          r"ongeveer \(95\) procent?", r"tussen \(164\) en \(192\) cm", WW),
             ]),
        dict(kop="Kansen opzoeken",
             opdracht="Reken uit met de kansrekenmachine. Rond af op vier decimalen.",
             oefeningen=[
                 ("rij", [(r"P(Z &lt; \(1{,}5\))", r"\(0{,}9332\)"), (r"P(Z &gt; \(2\))", r"\(0{,}0228\)")],
                  "Bereken.", "80px"),
                 ("rij", [(r"P(Z &lt; \(-1\))", r"\(0{,}1587\)"), (r"P(\(-1\) &lt; Z &lt; \(1\))", r"\(0{,}6827\)")],
                  "Bereken.", "80px"),
                 ("kort", r"\(X \sim N(170; 8)\). Bereken P(X &gt; \(180\)).", r"\(0{,}1056\)", W),
                 ("kort", r"\(X \sim N(100; 15)\). Bereken P(X &lt; \(85\)).", r"\(0{,}1587\)", W),
                 ("kort", r"\(X \sim N(500; 25)\). Bereken P(\(475\) &lt; X &lt; \(525\)).",
                  r"\(0{,}6827\), precies de vuistregel van \(68\,\%\)", WW),
                 ("kort", r"\(X \sim N(170; 8)\). Welke lengte heeft \(10\) procent boven zich? "
                          "Eén decimaal.", r"\(180{,}3\) cm", W),
             ]),
        dict(kop="Begrijpen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom is \(P(X = 170)\) bij een normale verdeling gelijk aan nul?",
                  r"Een normale verdeling is continu: er liggen oneindig veel waarden rond \(170\). De "
                  "oppervlakte boven één enkel punt is nul, dus vraag je altijd een stuk, "
                  r"bijvoorbeeld tussen \(169{,}5\) en \(170{,}5\).", 4),
                 ("waar", r"Twee normale verdelingen met dezelfde \(\mu\) maar een verschillende \(\sigma\) "
                          "liggen rond hetzelfde midden.", True),
             ]),
    ],
)

# ============================================================ 7
OEFENBUNDELS["oefenbundel-populatie-steekproef-en-de-steekproevenverdeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Populatie, steekproef en de steekproevenverdeling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Populatie of steekproef",
             opdracht="Schrijf populatie of steekproef, en zet het juiste symbool erbij "
                      r"(\(\mu\) of \(\bar{x}\)).",
             oefeningen=[
                 ("kort", r"Alle \(1200\) leerlingen van de school.", r"populatie, \(\mu\)", WW),
                 ("kort", r"De \(60\) leerlingen die je bevraagd hebt.", r"steekproef, \(\bar{x}\)", WW),
                 ("kort", r"Het gemiddelde dat je uit je \(60\) antwoorden berekent.",
                  r"een steekproefgemiddelde, \(\bar{x}\)", WW),
                 ("open", r"Waarom gaan \(H_{0}\) en \(H_{1}\) altijd over de populatie en nooit over je "
                          "steekproef?",
                  "Het gemiddelde van je steekproef ken je al, je hebt het zelf berekend. Je toetst "
                  "juist een bewering over het getal dat je níet kent, dat van de hele populatie.", 4),
             ]),
        dict(kop="Welke steekproef?",
             opdracht="Schrijf aselect, systematisch, gestratificeerd of gelegenheidssteekproef.",
             oefeningen=[
                 ("kort", "Je trekt vijftig namen uit de volledige lijst, elke naam even veel kans.",
                  "aselect", WW),
                 ("kort", "Je neemt elke tiende naam uit de alfabetische lijst.", "systematisch", WW),
                 ("kort", "Je neemt uit elk leerjaar evenveel leerlingen.", "gestratificeerd", WW),
                 ("kort", "Je bevraagt wie er toevallig op de speelplaats staat.",
                  "gelegenheidssteekproef, en die is niet representatief", WL),
             ]),
        dict(kop="De steekproevenverdeling",
             opdracht="Bereken de standaardafwijking van het steekproefgemiddelde: "
                      r"\(\sigma : \sqrt{n}\).",
             oefeningen=[
                 ("tabel", [r"\(\sigma\)", "n", r"\(\sigma\) van \(\bar{x}\)"],
                  [[r"\(12\)", r"\(36\)", None], [r"\(15\)", r"\(100\)", None], [r"\(20\)", r"\(25\)", None], [r"\(8\)", r"\(64\)", None]],
                  r"\(2\) — \(1{,}5\) — \(4\) — \(1\)", "62px"),
                 ("kort", r"Je verviervoudigt \(n\). Wat gebeurt er met die standaardafwijking?",
                  r"ze wordt gehalveerd, want \(\sqrt{4}\) is \(2\)", WL),
                 ("waar", r"Bij een gemiddelde mag je de normale benadering gebruiken zodra \(n\) "
                          "minstens dertig is.", True),
                 ("open", "Leg uit waarom een groter gemiddelde uit een grotere steekproef "
                          "betrouwbaarder is.",
                  r"Hoe groter \(n\), hoe kleiner \(\sigma : \sqrt{n}\), dus hoe dichter de "
                  "steekproefgemiddelden rond het echte populatiegemiddelde liggen. Een toevallige "
                  "uitschieter weegt minder zwaar door.", 4),
             ]),
    ],
)

# ============================================================ 8
OEFENBUNDELS["oefenbundel-hypothesen-opstellen-h0-h1-en-de-richting-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel=r"Hypothesen opstellen: H0, H1 en de richting",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop=r"\(H_{0}\) en \(H_{1}\) opschrijven",
             opdracht=r"Schrijf \(H_{0}\) en \(H_{1}\) in symbolen. Gebruik \(\mu\) bij een gemiddelde en \(p\) bij een "
                      "proportie.",
             oefeningen=[
                 ("open", r"Een fabrikant beweert dat zijn zakken \(500\) gram wegen. Jij vermoedt "
                          "dat ze te licht zijn.",
                  r"\(H_{0}\): \(\mu\) = \(500\) en \(H_{1}\): \(\mu\) &lt; \(500\). Linkszijdig.", 3),
                 ("open", r"Een school zegt dat \(60\) procent slaagt. Jij vermoedt dat het "
                          "anders ligt, maar je weet niet in welke richting.",
                  r"\(H_{0}\): \(p = 0{,}60\) en \(H_{1}\): \(p\) is verschillend van \(0{,}60\). Tweezijdig.", 3),
                 ("open", r"Een nieuwe methode zou het gemiddelde punt boven \(65\) tillen.",
                  r"\(H_{0}\): \(\mu\) = \(65\) en \(H_{1}\): \(\mu\) &gt; \(65\). Rechtszijdig.", 3),
             ]),
        dict(kop="Eenzijdig of tweezijdig",
             opdracht="Schrijf linkszijdig, rechtszijdig of tweezijdig.",
             oefeningen=[
                 ("rij", [(r"\(H_{1}\): \(\mu\) &gt; \(20\)", "rechtszijdig"), (r"\(H_{1}\): \(p < 0{,}3\)", "linkszijdig")],
                  "Welke richting?", "115px"),
                 ("kort", r"\(H_{1}\): \(\mu\) is verschillend van \(100\)", "tweezijdig", "115px"),
                 ("kort", "Je wil aantonen dat een middel schádelijk is, niet dat het anders is.",
                  "eenzijdig, want je kijkt maar naar één kant", WL),
             ]),
        dict(kop="Zoek de fout",
             opdracht="Elk van deze paren is fout. Schrijf op waarom en zet het recht.",
             oefeningen=[
                 ("open", r"\(H_{0}\): \(\mu\) &gt; \(100\) en \(H_{1}\): \(\mu\) &lt; \(100\)",
                  r"In \(H_{0}\) moet altijd een gelijkheid staan. Juist is \(H_{0}\): \(\mu\) = \(100\) en \(H_{1}\): \(\mu\) &lt; \(100\).", 3),
                 ("open", r"\(H_{0}\): \(\mu\) = \(50\) en \(H_{1}\): \(\mu\) &gt; \(60\)",
                  r"De twee dekken niet alle mogelijkheden en gebruiken een ander getal: wat als \(\mu\) "
                  r"vijfenvijftig is? Juist is \(H_{0}\): \(\mu\) = \(50\) en \(H_{1}\): \(\mu\) &gt; \(50\).", 3),
                 ("open", r"\(H_{0}\): \(\bar{x}\) = \(20\) en \(H_{1}\): \(\bar{x}\) &gt; \(20\)",
                  "Dat is een hypothese over je eigen steekproef, en die ken je al. Het moet over "
                  r"de populatie gaan: \(H_{0}\): \(\mu\) = \(20\) en \(H_{1}\): \(\mu\) &gt; \(20\).", 3),
             ]),
        dict(kop="De voorwaarden",
             opdracht="Mag je verder rekenen? Schrijf ja of nee, met het getal erbij.",
             oefeningen=[
                 ("kort", r"Een gemiddelde met \(n\) gelijk aan \(45\).", r"ja, \(45\) is minstens \(30\)", WW),
                 ("kort", r"Een proportie met \(n\) gelijk aan \(100\) en \(p\) gelijk aan \(0{,}60\).",
                  r"ja: \(n\) is \(100\), \(n \cdot p\) is \(60\) en \(n \cdot (1 - p)\) is \(40\)", WL),
                 ("kort", r"Een proportie met \(n\) gelijk aan \(50\) en \(p\) gelijk aan \(0{,}08\).",
                  r"nee, \(n \cdot p\) is \(4\) en dat haalt de drempel van tien niet", WL),
             ]),
    ],
)

# ============================================================ 9
OEFENBUNDELS[r"oefenbundel-de-p-waarde-het-significantieniveau-en-de-twee-fouten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel=r"De p-waarde, het significantieniveau en de twee fouten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop=r"Van z naar een \(p\)-waarde",
             opdracht=r"Bereken de \(p\)-waarde. Rond af op vier decimalen.",
             oefeningen=[
                 ("tabel", ["toets", "z", r"\(p\)-waarde"],
                  [["rechtszijdig", r"\(2{,}00\)", None],
                   ["linkszijdig", r"\(-2{,}50\)", None],
                   ["rechtszijdig", r"\(1{,}20\)", None],
                   ["tweezijdig", r"\(2{,}00\)", None]],
                  r"\(0{,}0228\) — \(0{,}0062\) — \(0{,}1151\) — \(0{,}0455\)", "70px"),
                 ("open", r"Waarom is de tweezijdige \(p\)-waarde het dubbele van de eenzijdige?",
                  "Bij een tweezijdige toets tellen allebei de staarten mee, en bij een "
                  "symmetrische verdeling zijn die even groot.", 3),
             ]),
        dict(kop="Een toets helemaal uitrekenen",
             opdracht=r"Schrijf de vier stappen op: hypothesen, voorwaarden, z en \(p\), besluit.",
             oefeningen=[
                 ("tekst", r"<p>\(H_{0}\) zegt \(\mu\) = \(70\). Je meet \(\bar{x}\) gelijk aan \(68\), bij "
                           r"\(n = 49\) en \(\sigma\) = \(6\). Je toetst linkszijdig, met \(\alpha\) = \(0{,}05\).</p>"),
                 ("kort", "Bereken de standaardafwijking van het steekproefgemiddelde.",
                  r"\(6 : 7\), dus \(0{,}857\) (op drie decimalen)", WW),
                 ("kort", "Bereken z op twee decimalen.", r"\(-2{,}33\)", W),
                 ("kort", r"Bereken de \(p\)-waarde op vier decimalen.", r"\(0{,}0098\)", W),
                 ("open", "Schrijf je besluit in een volle zin.",
                  r"Omdat \(0{,}0098\) kleiner is dan \(0{,}05\), verwerp ik \(H_{0}\). Er is een significante "
                  r"aanwijzing dat het gemiddelde lager ligt dan \(70\).", 3),
             ]),
        dict(kop="Besluiten",
             opdracht="Verwerpen of niet verwerpen? Schrijf het besluit en waarom.",
             oefeningen=[
                 ("rij", [(r"\(p = 0{,}0548\) bij \(\alpha\) = \(0{,}05\)", "niet verwerpen"),
                          (r"\(p = 0{,}0098\) bij \(\alpha\) = \(0{,}05\)", "verwerpen")],
                  "Wat besluit je?", "130px"),
                 ("kort", r"\(p = 0{,}0359\) bij \(\alpha\) = \(0{,}01\)",
                  r"niet verwerpen: \(0{,}0359\) is groter dan \(0{,}01\)", WL),
                 ("kies", r"Je verwerpt \(H_{0}\) niet. Wat heb je aangetoond?",
                  [r"dat \(H_{0}\) waar is", r"niets over \(H_{0}\), je hebt enkel te weinig bewijs tegen \(H_{0}\)"], 1),
             ]),
        dict(kop="De twee fouten",
             opdracht="Schrijf fout van de eerste soort of fout van de tweede soort.",
             oefeningen=[
                 ("kort", r"Je verwerpt \(H_{0}\) terwijl \(H_{0}\) in werkelijkheid waar is.",
                  "fout van de eerste soort", WW),
                 ("kort", r"Je verwerpt \(H_{0}\) niet terwijl \(H_{1}\) in werkelijkheid waar is.",
                  "fout van de tweede soort", WW),
                 ("kort", r"Een gezonde patiënt krijgt te horen dat hij ziek is (\(H_{0}\): gezond).",
                  "fout van de eerste soort", WW),
                 ("open", r"Je verlaagt \(\alpha\) van \(0{,}05\) naar \(0{,}01\). Wat gebeurt er met de kans op "
                          "elk van de twee fouten?",
                  r"De kans op een fout van de eerste soort daalt naar \(0{,}01\), maar de kans op een "
                  "fout van de tweede soort stijgt: je verwerpt minder snel, dus je mist vaker een "
                  "echt verschil.", 4),
             ]),
    ],
)

# ============================================================ 10
OEFENBUNDELS["oefenbundel-betrouwbaarheidsinterval-en-foutenmarge-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Betrouwbaarheidsinterval en foutenmarge",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een interval voor een gemiddelde",
             opdracht=r"Bereken het betrouwbaarheidsinterval van \(95\) procent: \(\bar{x}\) "
                      r"plus en min \(1{,}96 \cdot \sigma : \sqrt{n}\). Twee decimalen.",
             oefeningen=[
                 ("tabel", [r"\(\bar{x}\)", r"\(\sigma\)", "n", "marge", "van", "tot"],
                  [[r"\(52\)", r"\(10\)", r"\(100\)", None, None, None],
                   [r"\(170\)", r"\(8\)", r"\(64\)", None, None, None],
                   [r"\(23{,}4\)", r"\(4{,}2\)", r"\(49\)", None, None, None]],
                  r"\(1{,}96\) → \(50{,}04\) tot \(53{,}96\) — \(1{,}96\) → \(168{,}04\) tot \(171{,}96\) — \(1{,}18\) → \(22{,}22\) tot \(24{,}58\)",
                  "52px"),
                 ("open", "Schrijf het eerste interval in een volle zin, zoals in een krant.",
                  "We zijn er voor vijfennegentig procent zeker van dat het echte gemiddelde van de "
                  r"hele groep tussen \(50{,}04\) en \(53{,}96\) ligt.", 3),
             ]),
        dict(kop="Een interval voor een proportie",
             opdracht=r"Bereken met \(\hat{p} \pm 1{,}96 \sqrt{\dfrac{\hat{p}(1 - \hat{p})}{n}}\). "
                      r"Vier decimalen.",
             oefeningen=[
                 ("kort", r"\(p\) met een dakje is \(0{,}52\) bij \(n = 400\). Bereken de marge.", r"\(0{,}0490\)", W),
                 ("kort", "Geef het interval van de vorige oefening.", r"\(0{,}4710\) tot \(0{,}5690\)", WW),
                 ("kort", r"\(p\) met een dakje is \(0{,}40\) bij \(n = 1000\). Bereken de marge.", r"\(0{,}0304\)", W),
                 ("open", r"Een partij haalt \(52\) procent in een peiling van \(400\) mensen. Mag de "
                          "krant schrijven dat ze een meerderheid heeft?",
                  r"Nee. Het interval loopt van \(47{,}1\) tot \(56{,}9\) procent, en \(50\) procent ligt daar "
                  "binnen. De peiling sluit dus niet uit dat de partij onder de helft zit.", 4),
             ]),
        dict(kop="De foutenmarge",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", r"Je wil de marge halveren. Met hoeveel moet \(n\) vermenigvuldigd worden?",
                  "met vier", W),
                 ("kort", r"Hoeveel mensen heb je nodig voor een marge van \(3\) procent bij "
                          r"\(p = 0{,}5\)? Rond naar boven af.", r"\(1068\) (\(1067{,}1\) naar boven)", WW),
                 ("waar", r"Een interval van \(99\) procent is breder dan een interval van "
                          r"\(95\) procent.", True),
                 ("open", "Waarom wordt een interval breder als je zekerder wil zijn?",
                  "Je neemt een grotere z-waarde, dus een grotere marge. Meer zekerheid koop je met "
                  "een vagere uitspraak; de enige manier om allebei te verbeteren is een grotere "
                  "steekproef.", 4),
             ]),
    ],
)

# ============================================================ 11
OEFENBUNDELS["oefenbundel-spreidingsdiagrammen-trendlijn-en-correlatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Spreidingsdiagrammen, trendlijn en correlatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een spreidingsdiagram tekenen",
             opdracht="Zet de onafhankelijke variabele horizontaal en de afhankelijke verticaal. "
                      "Zet getallen op allebei de assen.",
             oefeningen=[
                 ("tekst", r"<p>Uren studie (x): \(1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6\) &nbsp;&nbsp; "
                           r"punt op tien (y): \(3 \cdot 5 \cdot 4 \cdot 7 \cdot 8 \cdot 9\)</p>"),
                 ("teken", "Teken het spreidingsdiagram van deze zes punten.",
                  r"Zes punten die duidelijk stijgen: (\(1\);\(3\)) (\(2\);\(5\)) (\(3\);\(4\)) (\(4\);\(7\)) (\(5\);\(8\)) (\(6\);\(9\)). "
                  "Uren horizontaal, punt verticaal, met een schaal op allebei de assen.", 70),
                 ("kort", "Is het verband positief of negatief?", "positief", W),
                 ("kort", r"De trendlijn is \(y = 1{,}20x + 1{,}80\). Wat voorspelt ze voor \(7\) uur studie?",
                  r"\(1{,}20 \cdot 7 + 1{,}80 = 10{,}2\), en dat kan niet op tien: buiten je gegevens mag je niet "
                  "zomaar doortrekken", WL),
                 ("kort", r"Wat betekent de \(1{,}20\) in die trendlijn?",
                  r"elk uur studie extra geeft gemiddeld \(1{,}20\) punt meer", WL),
             ]),
        dict(kop="De correlatiecoëfficiënt lezen",
             opdracht="Schrijf sterk positief, zwak, of sterk negatief, en of een trendlijn hier "
                      "zinvol is.",
             oefeningen=[
                 ("rij", [(r"\(r = 0{,}95\)", "sterk positief"), (r"\(r = -0{,}99\)", "sterk negatief")],
                  "Hoe lees je dit?", "120px"),
                 ("kort", r"\(r = 0{,}12\)", "zwak, een trendlijn is hier weinig zinvol", WL),
                 ("kort", r"\(r = -0{,}04\)", "zo goed als geen lineair verband", WL),
                 ("kies", "Welke waarde kan r nooit hebben?", [r"\(-1\)", r"\(0\)", r"\(1{,}4\)", r"\(0{,}77\)"], 2),
             ]),
        dict(kop="Verband is geen oorzaak",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "In een stad stijgen zowel het ijsverbruik als het aantal "
                          r"verdrinkingen. r is \(0{,}88\). Mag je besluiten dat ijs eten gevaarlijk is?",
                  "Nee. Allebei de cijfers stijgen met de warmte: dat is een derde oorzaak. Een "
                  "sterke correlatie toont samenhang, geen oorzakelijk verband.", 4),
                 ("open", r"r is \(0{,}05\), maar in het spreidingsdiagram zie je een duidelijke boog. "
                          "Kan dat?",
                  "Ja. r meet enkel een líneair verband. Een kromme samenhang kan een r dicht bij "
                  "nul geven, en daarom kijk je altijd eerst naar de tekening.", 4),
                 ("waar", "Eén uitschieter kan r flink doen veranderen.", True),
             ]),
    ],
)

# ============================================================ 12
OEFENBUNDELS["oefenbundel-kansen-berekenen-met-de-kansrekenmachine-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansen berekenen met de kansrekenmachine",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk stuk vraag je?",
             opdracht="Schrijf linkerstaart, rechterstaart of tussen twee grenzen.",
             oefeningen=[
                 ("rij", [(r"\(P(X \leq 7)\)", "linkerstaart"), (r"\(P(X \geq 12)\)", "rechterstaart")],
                  "Welk stuk?", "130px"),
                 ("kort", r"P(\(45\) &lt; X &lt; \(75\))", "tussen twee grenzen", "130px"),
                 ("kort", "De waarde die vijfentwintig procent boven zich heeft.",
                  "de omgekeerde vraag: je geeft de kans en vraagt de grens", WL),
             ]),
        dict(kop="Binomiale kansen",
             opdracht="Kies de binomiale verdeling. Rond af op vier decimalen.",
             oefeningen=[
                 ("tabel", ["opgave", r"\(n\) en \(p\)", "antwoord"],
                  [[r"\(X \sim B(16; 0{,}5)\), \(P(X = 10)\)", None, None],
                   [r"\(X \sim B(30; 0{,}2)\), \(P(X = 8)\)", None, None],
                   [r"\(X \sim B(16; 0{,}5)\), \(P(X \geq 12)\)", None, None],
                   [r"\(X \sim B(30; 0{,}2)\), \(P(X \leq 4)\)", None, None]],
                  r"\(0{,}1222\) — \(0{,}1106\) — \(0{,}0384\) — \(0{,}2552\)", "70px"),
                 ("kort", r"Veertig stukken, \(35\,\%\) kans op een fout, precies veertien fouten.",
                  r"\(n = 40\), \(p = 0{,}35\), van \(14\) tot \(14\) → \(0{,}1313\)", WL),
             ]),
        dict(kop="Normale kansen",
             opdracht=r"Kies de normale verdeling. \(X \sim N(60; 12)\). Rond af op vier decimalen.",
             oefeningen=[
                 ("kort", r"P(X &gt; \(75\))", r"\(0{,}1056\)", W),
                 ("kort", r"P(\(45\) &lt; X &lt; \(75\))", r"\(0{,}7887\)", W),
                 ("kort", r"Welke waarde heeft \(25\) procent boven zich? Eén decimaal.", r"\(68{,}1\)", W),
                 ("kort", r"\(P(X = 60)\)",
                  "nul; bij een continue verdeling vraag je nooit één exacte waarde", WL),
             ]),
        dict(kop=r"Van z naar een \(p\)-waarde",
             opdracht=r"Werk met Z ~ \(N(0; 1)\). Vier decimalen.",
             oefeningen=[
                 ("rij", [(r"rechtszijdig, \(z = 1{,}70\)", r"\(0{,}0446\)"), (r"tweezijdig, \(z = 2{,}50\)", r"\(0{,}0124\)")],
                  r"Bereken de \(p\)-waarde.", "80px"),
                 ("kort", r"linkszijdig, \(z = -1{,}80\)", r"\(0{,}0359\)", W),
             ]),
        dict(kop="Controleer jezelf",
             opdracht="Wat ging er waarschijnlijk mis?",
             oefeningen=[
                 ("open", r"Je vindt bij een rechtszijdige toets een \(p\)-waarde van \(0{,}9772\).",
                  r"Je nam de linkerstaart in plaats van de rechter. De \(p\)-waarde is \(1 - 0{,}9772\), "
                  r"dus \(0{,}0228\).", 3),
                 ("open", "Je vindt bij een normale verdeling een kans van nul.",
                  "Je vroeg de kans op één exacte waarde in plaats van op een stuk.", 2),
             ]),
    ],
)

# ============================================================ 13
OEFENBUNDELS["oefenbundel-frequentietabellen-en-gegevens-groeperen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Frequentietabellen en gegevens groeperen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een frequentietabel invullen",
             opdracht=r"Twintig leerlingen maakten een toets op tien. De punten: \(5 \cdot 6 \cdot 6 \cdot 6\) · "
                      r"\(7 \cdot 7 \cdot 7 \cdot 7 \cdot 7 \cdot 8 \cdot 8 \cdot 8 \cdot 8 \cdot 9 \cdot 9 \cdot 9 \cdot 10 \cdot 10 \cdot 10 \cdot 10\). "
                      "Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["punt", "absolute frequentie", "relatieve frequentie", "cumulatieve frequentie"],
                  [[r"\(5\)", None, None, None], [r"\(6\)", None, None, None], [r"\(7\)", None, None, None],
                   [r"\(8\)", None, None, None], [r"\(9\)", None, None, None], [r"\(10\)", None, None, None]],
                  r"\(5\): \(1 \cdot 5\,\% \cdot 1\) — \(6\): \(3 \cdot 15\,\% \cdot 4\) — \(7\): \(5 \cdot 25\,\% \cdot 9\) — \(8\): \(4 \cdot 20\,\% \cdot 13\) — "
                  r"\(9\): \(3 \cdot 15\,\% \cdot 16\) — \(10\): \(4 \cdot 20\,\% \cdot 20\)", "56px"),
                 ("kort", r"Hoeveel leerlingen haalden ten hoogste \(7\)?", r"\(9\)", W),
                 ("kort", r"Hoeveel procent haalde meer dan \(8\)?", r"\(35\,\%\), want \(3 + 4\) van de \(20\)", WW),
                 ("kort", "Bereken het gemiddelde op twee decimalen.",
                  r"\(7{,}85\), want de som is \(157\) en \(157 : 20\)", WW),
             ]),
        dict(kop="Controleren",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Waar moeten alle relatieve frequenties samen op uitkomen?",
                  r"op \(1\), dus op \(100\,\%\)", WW),
                 ("kort", "Waar moet de laatste cumulatieve frequentie op uitkomen?",
                  r"op het totale aantal, hier \(20\)", WW),
                 ("waar", "Een relatieve frequentie kan groter zijn dan één.", False),
             ]),
        dict(kop="Gegevens groeperen",
             opdracht=r"Twintig lengtes in cm: \(152 \cdot 158 \cdot 161 \cdot 163 \cdot 165 \cdot 166 \cdot 168 \cdot 169\) · "
                      r"\(170 \cdot 171 \cdot 172 \cdot 174 \cdot 175 \cdot 177 \cdot 178 \cdot 180 \cdot 181 \cdot 185 \cdot 188 \cdot 192\).",
             oefeningen=[
                 ("tabel", ["klasse", "frequentie", "klassenmidden"],
                  [[r"[\(150\), \(160\)[", None, None], [r"[\(160\), \(170\)[", None, None],
                   [r"[\(170\), \(180\)[", None, None], [r"[\(180\), \(190\)[", None, None],
                   [r"[\(190\), \(200\)[", None, None]],
                  r"\(2 \cdot 155\) — \(6 \cdot 165\) — \(7 \cdot 175\) — \(4 \cdot 185\) — \(1 \cdot 195\)", "60px"),
                 ("kort", "Schat het gemiddelde met de klassenmiddens.",
                  r"\(173\) cm (het echte gemiddelde is \(172{,}25\))", WW),
                 ("open", "Waarom is dat geschatte gemiddelde niet precies het echte?",
                  "Je doet alsof elke waarde in het midden van haar klasse ligt. Dat klopt niet "
                  "exact, dus je verliest een beetje nauwkeurigheid in ruil voor overzicht.", 4),
                 ("waar", "Bij een histogram raken de staven elkaar, want de variabele is "
                          "continu.", True),
             ]),
    ],
)

# ============================================================ 14
OEFENBUNDELS["oefenbundel-de-juiste-grafische-voorstelling-kiezen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De juiste grafische voorstelling kiezen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke voorstelling?",
             opdracht="Kies uit staafdiagram, lijndiagram, dotplot, histogram, "
                      "spreidingsdiagram en boxplot.",
             oefeningen=[
                 ("kort", "Het aantal leerlingen per studierichting.", "staafdiagram", WW),
                 ("kort", "Het aantal geboortes per maand over tien jaar.", "lijndiagram", WW),
                 ("kort", "De lengte van duizend leerlingen in klassen.", "histogram", WW),
                 ("kort", "Het verband tussen slaapuren en het punt op een toets.",
                  "spreidingsdiagram", WW),
                 ("kort", "Vier klassen vergelijken op mediaan en spreiding.", "boxplot", WW),
                 ("kort", "De punten van één klas van twintig leerlingen, één stip per punt.",
                  "dotplot", WW),
             ]),
        dict(kop="Misleidende grafieken",
             opdracht="Zoek wat er misleidt en schrijf op hoe je het zou tekenen.",
             oefeningen=[
                 ("open", r"Een staafdiagram waarvan de verticale as bij \(95\) begint in plaats van "
                          r"bij \(0\). Twee staven, \(97\) en \(99\).",
                  "Een verschil van twee op honderd lijkt zo een verdubbeling. Laat de as bij nul "
                  "beginnen, of zet de waarden duidelijk boven de staven en meld de afgeknipte as.", 4),
                 ("open", r"Een cirkeldiagram waarvan de stukken samen \(112\) procent zijn.",
                  r"De stukken van een cirkeldiagram moeten samen \(100\) procent zijn. Hier zijn "
                  "waarschijnlijk categorieën geteld die elkaar overlappen; dan hoort het een "
                  "staafdiagram te zijn.", 4),
                 ("kort", "Welke voorstelling staat níet bij de zes van de vakfiche?",
                  "het cirkeldiagram", WW),
             ]),
        dict(kop="Lezen wat je ziet",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een histogram heeft een lange staart aan de rechterkant. Hoe noem je "
                          "die vorm, en wat weet je dan over gemiddelde en mediaan?",
                  "Rechtsscheef of scheef naar rechts, dus asymmetrisch. Het gemiddelde wordt door "
                  "de staart omhoog getrokken en ligt dan hoger dan de mediaan.", 4),
                 ("waar", "Een boxplot laat zien hoeveel gegevens er in de dataset zitten.", False),
                 ("open", "Waarom zet je bij een uitschieter de waarden boven de staven?",
                  "Omdat de kleine staven dan onleesbaar klein worden naast de grote. Met de "
                  "getallen erbij kan de lezer ze toch vergelijken.", 3),
             ]),
    ],
)

# ============================================================ 15
OEFENBUNDELS["oefenbundel-centrummaten-gemiddelde-mediaan-en-modus-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Centrummaten: gemiddelde, mediaan en modus",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie berekenen",
             opdracht="Bereken het gemiddelde, de mediaan en de modus.",
             oefeningen=[
                 ("tabel", ["reeks", "gemiddelde", "mediaan", "modus"],
                  [[r"\(4\), \(7\), \(7\), \(9\), \(13\)", None, None, None],
                   [r"\(3\), \(5\), \(8\), \(10\)", None, None, None],
                   [r"\(12\), \(15\), \(15\), \(18\), \(20\), \(100\)", None, None, None]],
                  r"\(8 \cdot 7 \cdot 7\) — \(6{,}5 \cdot 6{,}5\) · geen modus — \(30 \cdot 16{,}5 \cdot 15\)", "60px"),
                 ("open", "Bij de derde reeks liggen het gemiddelde en de mediaan ver uit elkaar. "
                          "Welke van de twee zou je rapporteren, en waarom?",
                  r"De mediaan. De \(100\) is een uitschieter die het gemiddelde naar \(30\) tilt, terwijl "
                  r"vijf van de zes waarden onder de \(21\) liggen. De mediaan is robuust.", 4),
             ]),
        dict(kop="Een gewogen gemiddelde",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", r"Drie toetsen op \(20\) (elk gewicht \(1\)): \(14\), \(16\) en \(12\). Het examen "
                          r"(gewicht \(2\)): \(15\). Wat is het gewogen gemiddelde?",
                  r"\(14{,}4\), want \((14 + 16 + 12 + 2 \cdot 15) : 5\)", WW),
                 ("open", "Waarom is het gewone gemiddelde van die vier cijfers hier fout?",
                  "Omdat het examen dubbel telt. Het gewone gemiddelde zou alle vier even zwaar "
                  r"laten wegen en geeft \(14{,}25\) in plaats van \(14{,}4\).", 3),
             ]),
        dict(kop="Uit een frequentietabel",
             opdracht=r"Dertig leerlingen gaven een punt van \(1\) tot \(5\). De frequenties: "
                      r"\(2 \cdot 5 \cdot 8 \cdot 9 \cdot 6\).",
             oefeningen=[
                 ("kort", "Bereken het gemiddelde op twee decimalen.",
                  r"\(3{,}40\), want de som is \(102\) en \(102 : 30\)", WW),
                 ("kort", "Wat is de mediaan?",
                  r"\(3{,}5\): de vijftiende waarde is \(3\) en de zestiende is \(4\)", WW),
                 ("kort", "Wat is de modus?", r"\(4\), met de grootste frequentie \(9\)", WW),
             ]),
        dict(kop="Begrijpen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "De modus is altijd één getal.", False),
                 ("waar", "Het gemiddelde hoeft zelf niet in de dataset voor te komen.", True),
                 ("kort", "Welke centrummaat kan je gebruiken bij kleuren van auto's?",
                  "enkel de modus, want kleuren kan je niet optellen of rangschikken", WL),
             ]),
    ],
)

# ============================================================ 16
OEFENBUNDELS["oefenbundel-spreidingsmaten-en-de-boxplot-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Spreidingsmaten en de boxplot",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vijf getallen",
             opdracht=r"Reeks A: \(2 \cdot 4 \cdot 5 \cdot 7 \cdot 8 \cdot 11 \cdot 12 \cdot 15 \cdot 18 \cdot 21\).",
             oefeningen=[
                 ("tabel", ["minimum", "Q1", "mediaan", "Q3", "maximum"],
                  [[None, None, None, None, None]],
                  r"\(2 \cdot 5 \cdot 9{,}5 \cdot 15 \cdot 21\)", "56px"),
                 ("kort", "Bereken de variatiebreedte.", r"\(19\)", W),
                 ("kort", "Bereken de interkwartielafstand.", r"\(10\)", W),
                 ("teken", "Teken de boxplot van reeks A. Zet een getallenas eronder.",
                  r"Een doos van \(5\) tot \(15\) met de streep op \(9{,}5\), snorharen tot \(2\) en tot \(21\), en een "
                  "as met getallen eronder.", 55),
             ]),
        dict(kop="Uitschieters",
             opdracht=r"Reeks B: \(6 \cdot 7 \cdot 7 \cdot 8 \cdot 9 \cdot 9 \cdot 10 \cdot 12 \cdot 14 \cdot 30\).",
             oefeningen=[
                 ("kort", r"Bereken \(Q_{1}\), de mediaan en \(Q_{3}\).", r"\(7 \cdot 9 \cdot 12\)", WW),
                 ("kort", "Bereken de interkwartielafstand.", r"\(5\)", W),
                 ("kort", r"Bereken de bovengrens voor uitschieters: \(Q_{3}\) plus anderhalve "
                          "interkwartielafstand.", r"\(19{,}5\)", W),
                 ("kort", r"Is de \(30\) een uitschieter?", r"ja, \(30\) is groter dan \(19{,}5\)", WW),
                 ("open", "Welke spreidingsmaat kies je hier, en waarom?",
                  "De interkwartielafstand: die is robuust en kijkt enkel naar de middelste helft. "
                  r"De standaardafwijking zou door de \(30\) flink opgeblazen worden.", 4),
             ]),
        dict(kop="Begrijpen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "De variatiebreedte kan negatief zijn.", False),
                 ("waar", "De modus is een spreidingsmaat.", False),
                 ("kort", "Twee klassen hebben dezelfde mediaan, de ene een interkwartielafstand "
                          r"van \(2\) en de andere van \(8\). Wat besluit je?",
                  "bij de tweede klas liggen de resultaten veel verder uit elkaar", WL),
                 ("open", "Twee boxplots naast elkaar: wat zie je in één oogopslag?",
                  "Het centrum (de mediaan), de spreiding (de breedte van de doos) en de "
                  "uitschieters van allebei de groepen, naast elkaar op dezelfde as.", 3),
             ]),
    ],
)

# ============================================================ 17
OEFENBUNDELS["oefenbundel-een-dataset-doorrekenen-met-het-rekenblad-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een dataset doorrekenen met het rekenblad",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een reeks doorrekenen",
             opdracht=r"Reeks: \(20 \cdot 22 \cdot 25 \cdot 27 \cdot 31 \cdot 35\). Zet ze in één kolom en vraag de "
                      "kengetallen. Rond af op twee decimalen.",
             oefeningen=[
                 ("tabel", ["gemiddelde", "mediaan", "Q1", "Q3", "s"],
                  [[None, None, None, None, None]],
                  r"\(26{,}67 \cdot 26 \cdot 22 \cdot 31 \cdot 5{,}61\)", "56px"),
                 ("kort", "Bereken de variatiebreedte.", r"\(15\)", W),
                 ("kort", "Bereken de interkwartielafstand.", r"\(9\)", W),
                 ("kort", r"De app geeft ook \(5{,}12\). Wat is dat getal?",
                  r"de populatiestandaardafwijking \(\sigma\); in dit vak werk je met s", WL),
             ]),
        dict(kop=r"s of \(\sigma\)",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", r"Bij \(10 \cdot 12 \cdot 14 \cdot 16 \cdot 18\) geeft de app \(3{,}16\) en \(2{,}83\). Welke is s?",
                  r"\(3{,}16\); \(2{,}83\) is \(\sigma\)", WW),
                 ("open", r"Waarom is s altijd iets groter dan \(\sigma\) bij dezelfde getallen?",
                  r"Bij s deel je door \(n - 1\) in plaats van door \(n\). Je deelt dus door een kleiner "
                  "getal, en dat maakt de uitkomst groter.", 3),
                 ("kort", "Welke van de twee neem je in dit vak?",
                  "s, want je werkt met steekproeven", WW),
             ]),
        dict(kop="Twee kolommen",
             opdracht="Je zet x en y in twee kolommen en vraagt een spreidingsdiagram met "
                      "lineaire trendlijn.",
             oefeningen=[
                 ("kort", "Mag de ene kolom langer zijn dan de andere?",
                  "nee, elk paar hoort bij elkaar, dus de kolommen moeten even lang zijn", WL),
                 ("kort", r"De app geeft \(y = 1{,}30x + 20{,}47\). Wat voorspelt ze bij x gelijk aan \(20\)?",
                  r"\(46{,}47\)", W),
                 ("kort", "Je verwisselt de twee kolommen. Verandert r?",
                  "nee, r blijft dezelfde; de trendlijn verandert wel", WL),
                 ("waar", "Een trendlijn mag je zomaar ver buiten je gegevens doortrekken.", False),
             ]),
    ],
)

# ============================================================ 18
OEFENBUNDELS["oefenbundel-een-statistisch-onderzoek-met-de-rekenapps-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een statistisch onderzoek met de rekenapps",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen op een rij",
             opdracht=r"Zet de stappen in de juiste volgorde door er \(1\) tot \(5\) bij te schrijven.",
             oefeningen=[
                 ("tabel", ["stap", "nummer"],
                  [["de gegevens verkennen met een grafiek en kengetallen", None],
                   ["een onderzoeksvraag formuleren", None],
                   ["besluiten en het antwoord in woorden opschrijven", None],
                   ["toetsen of schatten met de rekenapps", None],
                   ["gegevens verzamelen", None]],
                  r"verkennen \(3\) · onderzoeksvraag \(1\) · besluiten \(5\) · toetsen of schatten \(4\) · "
                  r"verzamelen \(2\)", "56px"),
                 ("open", "Welke stap wordt het vaakst overgeslagen, en wat loopt er dan mis?",
                  "Het verkennen. Zonder grafiek zie je een uitschieter of een scheve verdeling "
                  "niet, en dan reken je met een gemiddelde dat de dataset niet beschrijft.", 4),
             ]),
        dict(kop="Een onderzoek uitwerken",
             opdracht=r"Een school beweert dat \(60\) procent van haar leerlingen fietst. Je "
                      "bevraagt er honderd en er fietsen er achtenvijftig.",
             oefeningen=[
                 ("kort", r"Schrijf \(H_{0}\) en \(H_{1}\) op. Je vermoedt dat het er minder zijn.",
                  r"\(H_{0}\): \(p = 0{,}60\) en \(H_{1}\): \(p < 0{,}60\)", WW),
                 ("kort", "Is de proportievoorwaarde voldaan?",
                  r"ja: \(n\) is \(100\), \(n \cdot p\) is \(60\) en \(n \cdot (1 - p)\) is \(40\)", WL),
                 ("kort", r"Bereken \(p\) met een dakje.", r"\(0{,}58\)", W),
                 ("open", r"Je vindt een \(p\)-waarde van \(0{,}3415\) bij \(\alpha\) = \(0{,}05\). Schrijf je besluit "
                          "in een volle zin.",
                  r"Omdat \(0{,}3415\) groter is dan \(0{,}05\), verwerp ik \(H_{0}\) niet. Er is te weinig bewijs om "
                  r"te besluiten dat minder dan \(60\) procent fietst. Dat betekent niet dat de "
                  "school gelijk heeft.", 4),
             ]),
        dict(kop="Wat mag je besluiten?",
             opdracht="Schrijf mag of mag niet, met één zin erbij.",
             oefeningen=[
                 ("kort", r"Je vindt \(r = 0{,}78\) en besluit dat het ene het andere veroorzaakt.",
                  "mag niet: samenhang is geen oorzaak", WL),
                 ("kort", r"Je vindt \(r = 0{,}15\) en tekent toch een trendlijn om te voorspellen.",
                  r"mag niet: bij zo'n zwakke samenhang is een trendlijn weinig zinvol", WL),
                 ("kort", "Je bevroeg enkel je eigen vrienden en veralgemeent naar de school.",
                  "mag niet: dat is geen representatieve steekproef", WL),
                 ("open", "Waarom staat in het verslag altijd hoe groot je steekproef was?",
                  "Omdat de lezer anders niet kan inschatten hoe betrouwbaar je uitkomst is. Bij "
                  r"een kleine \(n\) is de foutenmarge groot, ook al staat er een mooi getal.", 4),
             ]),
    ],
)

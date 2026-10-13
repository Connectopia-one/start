# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels voor fysica op 🚀 Boost doorstroom-niveau.

Eén oefenbundel per thema, met andere opgaven dan de vragen op het scherm en
met een antwoordblad achteraan. Geschreven náást de vakfiche fysica van de
2de graad doorstroomfinaliteit én náást de leerbundel van hetzelfde thema, in
[maak_fysica_boost].

De bundelsleutels beginnen met "oefenbundel-" en eindigen op
"-fysica-boost-doorstroom".

De constanten die een kind op het examen krijgt, staan ook hier bij de opgave
of bij de reeks: g = 9,81 N/kg, de massadichtheid van water 1000 kg/m³, de
luchtdruk 1013 hPa, c van water 4186 J/(kg.K) en R = 8,31 J/(mol.K). Andere
waarden staan altijd in de opgave zelf, zodat een kind geen tabellenboek naast
het blad hoeft te leggen.

De tweede wet van Newton staat niet op de fiche, dus F = m.a komt in geen
enkele opgave voor, en er zijn geen formules voor de eenparig veranderlijke
beweging: daar gaat het om grafieken lezen en om Δv/Δt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Fysica"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf eerst de formule op, dan de getallen, en zet de eenheid bij je antwoord.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

REKEN = HOE + [r"Reken met \(g = 9{,}81\) N/kg, tenzij de opgave iets anders zegt."]

# ============================================================
OEFENBUNDELS["oefenbundel-grootheden-eenheden-en-nauwkeurig-meten-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Grootheden, eenheden en nauwkeurig meten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke eenheid?",
             opdracht="Schrijf de SI-eenheid van elke grootheid, met haar symbool.",
             oefeningen=[
                 ("rij", [("kracht", "newton (N)"),
                          ("druk", "pascal (Pa)"),
                          ("vermogen", "watt (W)")], "SI-eenheid", WW),
                 ("rij", [("weerstand", r"ohm (\(\Omega\))"),
                          ("warmte", "joule (J)"),
                          ("absolute temperatuur", "kelvin (K)")], "SI-eenheid", WW),
                 ("rij", [("massadichtheid", r"kg/\(\text{m}^{3}\)"),
                          ("versnelling", r"\(\text{m/s}^{2}\)"),
                          ("moment van een kracht", "newtonmeter (Nm)")], "SI-eenheid", WW),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Schrijf de waarde als een macht van tien.",
             oefeningen=[
                 ("rij", [("mega", r"\(10^{6}\)"), ("hecto", r"\(10^{2}\)"), ("deci", r"\(10^{-1}\)")], "Waarde", W),
                 ("rij", [("micro", r"\(10^{-6}\)"), ("nano", r"\(10^{-9}\)"), ("deca", r"\(10^{1}\)")], "Waarde", W),
             ]),
        dict(kop="Reken om",
             opdracht="Reken om naar de eenheid die gevraagd wordt.",
             oefeningen=[
                 ("rij", [(r"\(3{,}2\) km naar m", r"\(3200\) m"),
                          (r"\(85\) mm naar m", r"\(0{,}085\) m"),
                          (r"\(0{,}75\) ton naar kg", r"\(750\) kg")], "Antwoord", WW),
                 ("rij", [(r"\(250\) L naar \(\text{m}^{3}\)", r"\(0{,}25\,\text{m}^{3}\)"),
                          (r"\(54\) km/h naar m/s", r"\(15\) m/s"),
                          (r"\(12\) m/s naar km/h", r"\(43{,}2\) km/h")], "Antwoord", WW),
                 ("rij", [(r"\(2{,}5\) min naar s", r"\(150\) s"),
                          (r"\(37^{\circ}\text{C}\) naar K", r"\(310\) K"),
                          (r"\(150\) K naar °C", r"\(-123^{\circ}\text{C}\)")], "Antwoord", WW),
             ]),
        dict(kop="Wetenschappelijke notatie en beduidende cijfers",
             opdracht="Schrijf het getal in de wetenschappelijke notatie, of geef het aantal beduidende cijfers.",
             oefeningen=[
                 ("rij", [(r"\(0{,}0072\) m", r"\(7\),\(2 \times 10^{-3}\) m"),
                          (r"\(154\,000\) N", r"\(1\),\(54 \times 10^{5}\) N"),
                          (r"\(0{,}000019\) s", r"\(1\),\(9 \times 10^{-5}\) s")], "Notatie", WW),
                 ("rij", [(r"\(0{,}0340\) kg", r"\(3\) beduidende cijfers"),
                          (r"\(12{,}50\) m", r"\(4\) beduidende cijfers"),
                          (r"\(7000\) kg (zo geschreven)", r"\(1\) beduidend cijfer")], "Hoeveel?", WW),
             ]),
        dict(kop="Vector of niet?",
             opdracht="Kruis aan of de grootheid een vector is.",
             oefeningen=[
                 ("waar", "De verplaatsing is een vectoriële grootheid.", True),
                 ("waar", "De temperatuur is een vectoriële grootheid.", False),
                 ("waar", "De versnelling is een vectoriële grootheid.", True),
                 ("waar", "De druk is een vectoriële grootheid.", False),
             ]),
        dict(kop="Welk verband?",
             opdracht="Schrijf recht evenredig, lineair, omgekeerd evenredig of kwadratisch.",
             oefeningen=[
                 ("kort", "De grafiek is een rechte door de oorsprong.", "recht evenredig", WL),
                 ("kort", "Het product van de twee grootheden blijft gelijk.", "omgekeerd evenredig", WL),
                 ("kort", "De grafiek is een rechte die de y-as boven de oorsprong snijdt.", "lineair", WL),
                 ("kort", "Verdubbelt x, dan wordt y vier keer zo groot.", "kwadratisch", WL),
             ]),
        dict(kop="Formules omvormen en schatten",
             opdracht="Vorm om of beantwoord in één zin.",
             oefeningen=[
                 ("kort", r"Maak in \(p = F / A\) de kracht F vrij.", r"\(F = p \cdot A\)", W),
                 ("kort", r"Maak in \(F_{v} = k \cdot \Delta l\) de veerconstante k vrij.", r"\(k = F_{v} / \Delta l\)", W),
                 ("open", r"Een leerling berekent de massa van een fles water van \(1{,}5\) L en komt op \(15\) kg. "
                          "Leg uit hoe een schatting die fout meteen verraadt.",
                  r"Water heeft een massadichtheid van \(1000\) kg/\(\text{m}^{3}\), dus weegt één liter ongeveer één kilogram. "
                  r"Een fles van \(1{,}5\) L weegt dus ongeveer \(1{,}5\) kg; \(15\) kg is tien keer te veel, dus is er met een "
                  "factor tien iets misgegaan.", 4),
                 ("open", r"Je wil een volume van \(0{,}75\) L afmeten. Je hebt een maatcilinder van \(100\) mL met "
                          r"streepjes per \(1\) mL en een maatcilinder van \(1\) L met streepjes per \(10\) mL. "
                          "Welke kies je, en waarom?",
                  r"De cilinder van \(1\) L: in die van \(100\) mL past \(0{,}75\) L niet, dus ligt de waarde buiten het "
                  "meetbereik. Je kiest eerst op meetbereik en daarna op nauwkeurigheid.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-eenparig-rechtlijnige-beweging-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Eenparig rechtlijnige beweging",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Afgelegde weg of verplaatsing?",
             opdracht="Schrijf de afgelegde weg en de verplaatsing, met hun teken.",
             oefeningen=[
                 ("kort", r"Een loper loopt twee ronden van \(400\) m op een piste.",
                  r"\(\Delta s = 800\) m en \(\Delta x = 0\) m", WL),
                 ("kort", r"Iemand wandelt van \(x_{0} = 15\) m naar \(x = 70\) m in de positieve zin.",
                  r"\(\Delta s = 55\) m en \(\Delta x\) = +\(55\) m", WL),
                 ("kort", r"Een fietser rijdt van \(x_{0} = 90\) m naar \(x = 40\) m.",
                  r"\(\Delta s = 50\) m en \(\Delta x = -50\) m", WL),
                 ("kort", r"Iemand loopt \(30\) m vooruit en daarna \(12\) m terug.",
                  r"\(\Delta s = 42\) m en \(\Delta x\) = +\(18\) m", WL),
             ]),
        dict(kop="Reken de snelheid",
             opdracht=r"Bereken met \(v_{g} = \Delta x / \Delta t\). Zet de eenheid bij je antwoord.",
             oefeningen=[
                 ("rij", [(r"\(240\) km in \(3{,}0\) h", r"\(80\) km/h"),
                          (r"\(90\) m in \(6{,}0\) s", r"\(15\) m/s"),
                          (r"\(45\) km in een kwartier", r"\(180\) km/h")], "vg", WW),
                 ("rij", [(r"\(12\) m/s gedurende \(8{,}0\) s", r"\(96\) m"),
                          (r"\(20\) m/s gedurende \(2{,}0\) min", r"\(2400\) m"),
                          (r"\(5{,}0\) m/s over \(125\) m", r"\(25\) s")], "Antwoord", WW),
             ]),
        dict(kop="De positiefunctie",
             opdracht="Lees uit de positiefunctie af wat gevraagd wordt. x in meter, t in seconde.",
             oefeningen=[
                 ("rij", [(r"\(x = 15 + 4 \cdot t\), de beginpositie", r"\(15\) m"),
                          (r"\(x = 15 + 4 \cdot t\), de snelheid", r"\(4\) m/s"),
                          (r"\(x = 60 - 6 \cdot t\), de snelheid", r"\(-6\) m/s")], "Antwoord", WW),
                 ("kort", r"Na hoeveel seconden is het voorwerp met \(x = 60 - 6 \cdot t\) in de oorsprong?",
                  r"na \(10\) s", W),
                 ("kort", r"Schrijf de positiefunctie van een voorwerp dat op \(8\) m vertrekt met \(3\) m/s in de positieve zin.",
                  r"\(x = 8 + 3 \cdot t\)", WW),
             ]),
        dict(kop="Grafieken lezen",
             opdracht="Antwoord in één woord of één getal.",
             oefeningen=[
                 ("kort", "Wat stelt de steilheid van een x(t)-grafiek voor?", "de snelheid", WW),
                 ("kort", "Wat stelt de oppervlakte onder een v(t)-grafiek voor?", "de verplaatsing", WW),
                 ("kort", "Wat doet een voorwerp waarvan de x(t)-grafiek horizontaal loopt?", "het staat stil", WW),
                 ("kort", "Hoe ziet de v(t)-grafiek van een ERB eruit?", "een horizontale lijn", WW),
                 ("kort", r"Een v(t)-lijn ligt op \(-5\) m/s gedurende \(4{,}0\) s. Hoe groot is \(\Delta x\)?", r"\(-20\) m", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een ERB is de gemiddelde snelheid gelijk aan de ogenblikkelijke snelheid.", True),
                 ("waar", "Een afgelegde weg kan negatief zijn.", False),
                 ("waar", "Uit een v(t)-grafiek kan je de beginpositie aflezen.", False),
                 ("waar", "Een snijpunt van twee rechten in een x(t)-grafiek betekent dat de twee voorwerpen daar op dezelfde plaats zijn.", True),
             ]),
        dict(kop="Inhalen en kruisen",
             opdracht="Reken uit en schrijf je werkwijze op.",
             oefeningen=[
                 ("open", r"Een wandelaar vertrekt om \(8\) uur met \(4{,}0\) km/h. Een fietser vertrekt om \(9\) uur op "
                          r"dezelfde plaats met \(16\) km/h. Na hoeveel tijd haalt de fietser hem in?",
                  r"Na één uur heeft de wandelaar \(4{,}0\) km voorsprong. De fietser loopt \(16 - 4{,}0 = 12\) km/h in, "
                  r"dus duurt het \(4{,}0 / 12 = 0{,}33\) h, dus ongeveer \(20\) minuten.", 5),
                 ("open", r"Twee treinen rijden naar elkaar toe, \(180\) km van elkaar, met \(100\) km/h en \(80\) km/h. "
                          "Na hoeveel tijd kruisen ze, en hoeveel kilometer heeft de snelste dan afgelegd?",
                  r"Samen naderen ze met \(100 + 80 = 180\) km/h, dus kruisen ze na \(1{,}0\) h. De snelste heeft dan "
                  r"\(100\) km afgelegd.", 5),
                 ("open", "Leg uit waarom je bij twee voorwerpen die dezelfde kant op rijden hun snelheden "
                          "van elkaar aftrekt, en bij twee voorwerpen die naar elkaar toe rijden optelt.",
                  "Bij dezelfde zin wordt de afstand tussen de twee elke seconde kleiner met het verschil van "
                  "hun snelheden. Rijden ze naar elkaar toe, dan nadert elk van de twee, dus krimpt de afstand "
                  "met de som van hun snelheden.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-versnelde-beweging-vrije-val-en-verticale-worp-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Versnelde beweging, vrije val en verticale worp",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=REKEN,
    reeksen=[
        dict(kop="Reken de gemiddelde versnelling",
             opdracht=r"Bereken met \(a_{g} = \Delta v / \Delta t\). Let op het teken.",
             oefeningen=[
                 ("rij", [(r"van \(0\) naar \(15\) m/s in \(3{,}0\) s", r"\(5{,}0\ \text{m/s}^{2}\)"),
                          (r"van \(8{,}0\) naar \(20\) m/s in \(4{,}0\) s", r"\(3{,}0\ \text{m/s}^{2}\)"),
                          (r"van \(25\) naar \(5{,}0\) m/s in \(5{,}0\) s", r"\(-4{,}0\ \text{m/s}^{2}\)")], "ag", WW),
                 ("rij", [(r"van \(12\) naar \(0\) m/s in \(6{,}0\) s", r"\(-2{,}0\ \text{m/s}^{2}\)"),
                          (r"van \(0\) naar \(30\) m/s in \(12\) s", r"\(2{,}5\ \text{m/s}^{2}\)"),
                          (r"van \(9{,}0\) naar \(9{,}0\) m/s in \(4{,}0\) s", r"\(0\ \text{m/s}^{2}\)")], "ag", WW),
             ]),
        dict(kop="Welke beweging?",
             opdracht="Schrijf ERB, eenparig versneld of eenparig vertraagd.",
             oefeningen=[
                 ("kort", "De v(t)-grafiek is een horizontale lijn boven nul.", "ERB", WW),
                 ("kort", "De v(t)-grafiek is een stijgende rechte.", "eenparig versneld", WW),
                 ("kort", "De x(t)-grafiek is een kromme die steeds vlakker wordt.", "eenparig vertraagd", WW),
                 ("kort", "De a(t)-grafiek is een horizontale lijn onder nul en de snelheid is positief.",
                  "eenparig vertraagd", WW),
             ]),
        dict(kop="De vrije val",
             opdracht=r"Reken met \(g = 9{,}81\ \text{m/s}^{2}\). Rond af op twee beduidende cijfers.",
             oefeningen=[
                 ("rij", [(r"snelheid na \(1{,}0\) s", r"\(9{,}8\) m/s"),
                          (r"snelheid na \(2{,}5\) s", r"\(25\) m/s"),
                          (r"snelheid na \(4{,}0\) s", r"\(39\) m/s")], "v (vanuit rust)", WW),
                 ("kort", "Hoeveel m/s komt er bij een vrije val elke seconde bij de snelheid?", r"\(9{,}81\) m/s", W),
                 ("kort", "Hoe groot is de versnelling van een bal op het hoogste punt van een worp naar boven?",
                  r"\(9{,}81\ \text{m/s}^{2}\), naar beneden", WW),
                 ("kort", r"Je gooit een bal met \(20\) m/s recht omhoog. Na hoeveel tijd is hij op zijn hoogste punt?",
                  r"ongeveer \(2{,}0\) s", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een negatieve versnelling betekent altijd dat het voorwerp vertraagt.", False),
                 ("waar", "Een voorwerp met een snelheid van nul kan toch een versnelling hebben.", True),
                 ("waar", "Bij een vrije val neemt de afgelegde weg elke seconde met evenveel toe.", False),
                 ("waar", r"Zonder luchtweerstand vallen een kogel van \(1\) kg en een van \(5\) kg even snel.", True),
                 ("waar", "Bij een worp naar boven keert de zin van de versnelling om op het hoogste punt.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Een parachutist valt eerst sneller en sneller, maar bereikt daarna een constante "
                          "snelheid. Leg uit met de krachten erop.",
                  "De zwaartekracht blijft gelijk, maar de luchtweerstand groeit met de snelheid. Zodra de "
                  "luchtweerstand even groot is als de zwaartekracht, is de resulterende kracht nul en "
                  "verandert de snelheid niet meer.", 5),
                 ("open", "Leg uit waarom snelheid en versnelling bij een vertragende beweging dezelfde "
                          "richting hebben, maar een tegengestelde zin.",
                  "Ze liggen op dezelfde rechte, dus hebben ze dezelfde richting. Omdat de snelheid kleiner "
                  "wordt, moet de versnelling de andere kant op wijzen dan de beweging.", 4),
                 ("open", "Een leerling zegt: op het hoogste punt van een worp naar boven werkt er geen "
                          "zwaartekracht meer, want de bal staat stil. Leg uit waarom dat niet klopt.",
                  "De bal staat daar maar één ogenblik stil. De zwaartekracht blijft werken, dus is de "
                  r"versnelling er \(9{,}81\ \text{m/s}^{2}\) naar beneden. Daarom valt de bal een ogenblik later ook weer.", 5),
                 ("open", "Leg uit waarom in de echte lucht een pluim trager valt dan een steen, terwijl een "
                          "lichte en een zware kogel wel even snel vallen.",
                  "De valversnelling is voor alles dezelfde. Een pluim heeft veel luchtweerstand ten opzichte "
                  "van haar kleine gewicht, dus valt ze trager. Bij twee kogels is de luchtweerstand ten "
                  "opzichte van hun gewicht zo klein dat je ze niet merkt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-krachten-krachtenbalans-en-zwaartekracht-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Krachten, krachtenbalans en zwaartekracht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=REKEN,
    reeksen=[
        dict(kop="Krachten samenstellen",
             opdracht="Bereken de grootte van de resultante en schrijf in welke zin ze wijst.",
             oefeningen=[
                 ("rij", [(r"\(90\) N en \(60\) N, dezelfde zin", r"\(150\) N"),
                          (r"\(90\) N en \(60\) N, tegengesteld", r"\(30\) N, zin van de \(90\) N"),
                          (r"\(45\) N en \(45\) N, tegengesteld", r"\(0\) N")], "Resultante", WL),
                 ("rij", [(r"\(200\) N en \(140\) N, tegengesteld", r"\(60\) N, zin van de \(200\) N"),
                          (r"\(35\) N en \(35\) N, dezelfde zin", r"\(70\) N"),
                          (r"\(120\) N, \(80\) N en \(50\) N, alle drie dezelfde zin", r"\(250\) N")], "Resultante", WL),
             ]),
        dict(kop="De zwaartekracht",
             opdracht=r"Bereken met \(F_{z} = m \cdot g\) en \(g = 9{,}81\) N/kg. Rond af op drie beduidende cijfers.",
             oefeningen=[
                 ("rij", [(r"\(m = 3{,}0\) kg", r"\(29{,}4\) N"),
                          (r"\(m = 12\) kg", r"\(118\) N"),
                          (r"\(m = 0{,}50\) kg", r"\(4{,}91\) N")], "Fz", WW),
                 ("kort", r"Een voorwerp ondervindt een zwaartekracht van \(98{,}1\) N. Hoe groot is zijn massa?",
                  r"\(10\) kg", W),
                 ("kort", r"Hoe groot is de zwaartekracht op \(2{,}0\) kg op de maan, met \(g = 1{,}62\) N/kg?",
                  r"\(3{,}24\) N", W),
             ]),
        dict(kop="De veerkracht",
             opdracht=r"Bereken met \(F_{v} = k \cdot \Delta l\). Reken de lengteverandering eerst om naar meter.",
             oefeningen=[
                 ("rij", [(r"\(20\) N rekt \(5{,}0\) cm uit", r"\(k = 400\) N/m"),
                          (r"\(k = 150\) N/m, \(F = 30\) N", r"\(\Delta l = 20\) cm"),
                          (r"\(k = 500\) N/m, \(\Delta l = 3{,}0\) cm", r"\(F = 15\) N")], "Antwoord", WW),
                 ("kort", r"Een massa van \(1{,}5\) kg hangt aan een veer met \(k = 200\) N/m. Hoeveel centimeter rekt ze uit?",
                  r"ongeveer \(7{,}4\) cm", WW),
                 ("kort", "Twee veren krijgen dezelfde massa. Veer A rekt verder uit. Welke heeft de grootste k?",
                  "veer B", W),
             ]),
        dict(kop="De wrijvingskracht",
             opdracht=r"Bereken met \(F_{w} = \mu \cdot F_{n}\). Op een horizontale vloer is \(F_{n}\) gelijk aan \(F_{z}\).",
             oefeningen=[
                 ("rij", [(r"\(m = 10\) kg, \(\mu = 0{,}40\)", r"\(39{,}2\) N"),
                          (r"\(m = 25\) kg, \(\mu = 0{,}20\)", r"\(49{,}1\) N"),
                          (r"\(F_{n} = 500\) N, \(\mu = 0{,}30\)", r"\(150\) N")], "Fw", WW),
                 ("kort", r"\(F_{w} = 60\) N en \(F_{n} = 200\) N. Hoe groot is \(\mu\)?", r"\(0{,}30\)", W),
                 ("kort", "Wat is de eenheid van de wrijvingscoëfficiënt?", "ze heeft er geen", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De massa van een voorwerp wordt kleiner op de maan.", False),
                 ("waar", "Een voorwerp dat met constante snelheid rechtdoor beweegt, heeft een resulterende kracht van nul.", True),
                 ("waar", "Het zwaartepunt van een voorwerp ligt altijd binnen het voorwerp zelf.", False),
                 ("waar", "De wrijvingscoëfficiënt hangt af van de massa van het voorwerp.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit wat het verschil is tussen de massa en het gewicht van een lichaam, en "
                          "wat er op de maan verandert.",
                  "De massa is een hoeveelheid materie, in kilogram, en verandert niet van plaats tot plaats. "
                  "Het gewicht is de kracht waarmee het lichaam op zijn steun duwt, in newton. Op de maan is "
                  "g ongeveer zes keer kleiner, dus wordt het gewicht zes keer kleiner en de massa niet.", 6),
                 ("open", "Een boek ligt stil op een tafel. Noem de twee krachten die erop werken en leg uit "
                          "waarom het blijft liggen.",
                  "De zwaartekracht van de aarde op het boek, naar beneden, en de normaalkracht van de tafel "
                  "op het boek, loodrecht naar boven. Die twee zijn even groot, dus is de resulterende kracht "
                  "nul en verandert de snelheid niet.", 5),
                 ("open", "Een slee wordt met een koord onder een hoek naar voren getrokken. Leg uit in welke "
                          "twee componenten je die kracht ontbindt en wat elke component doet.",
                  "Je ontbindt ze in een horizontale en een verticale component. De horizontale trekt de slee "
                  "vooruit, de verticale tilt hem een beetje op en vermindert zo de normaalkracht, en daardoor "
                  "ook de wrijvingskracht.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-archimedeskracht-moment-en-evenwicht-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Archimedeskracht, moment en evenwicht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=REKEN + [r"De massadichtheid van water is \(1000\) kg/\(\text{m}^{3}\)."],
    reeksen=[
        dict(kop="De archimedeskracht",
             opdracht=r"Bereken met \(F_{A} = \rho \cdot g \cdot V_{\text{ond}}\). Het voorwerp zit volledig onder water.",
             oefeningen=[
                 ("rij", [(r"\(V = 0{,}0010\,\text{m}^{3}\)", r"\(9{,}81\) N"),
                          (r"\(V = 0{,}0040\,\text{m}^{3}\)", r"\(39{,}2\) N"),
                          (r"\(V = 0{,}010\,\text{m}^{3}\)", r"\(98{,}1\) N")], "FA", WW),
                 ("kort", r"Een blok van \(0{,}0060\,\text{m}^{3}\) drijft met de helft onder water. Hoe groot is \(F_{A}\)?",
                  r"\(29{,}4\) N", W),
                 ("kort", r"Een steen weegt in de lucht \(60\) N en onder water \(44\) N. Hoe groot is \(F_{A}\)?",
                  r"\(16\) N", W),
             ]),
        dict(kop="Zinken, zweven of drijven?",
             opdracht="Vergelijk met de massadichtheid van water en schrijf wat er gebeurt.",
             oefeningen=[
                 ("rij", [(r"\(\rho = 1300\) kg/\(\text{m}^{3}\)", "het zinkt"),
                          (r"\(\rho = 1000\) kg/\(\text{m}^{3}\)", "het zweeft"),
                          (r"\(\rho = 700\) kg/\(\text{m}^{3}\)", "het drijft")], "Wat gebeurt er?", WW),
                 ("rij", [(r"kurk, \(\rho = 240\) kg/\(\text{m}^{3}\)", "het drijft"),
                          (r"ijzer, \(\rho = 7870\) kg/\(\text{m}^{3}\)", "het zinkt"),
                          (r"ijs, \(\rho = 917\) kg/\(\text{m}^{3}\)", "het drijft")], "Wat gebeurt er?", WW),
             ]),
        dict(kop="Het moment van een kracht",
             opdracht=r"Bereken met \(M = F \cdot d \cdot \sin \alpha\).",
             oefeningen=[
                 ("rij", [(r"\(50\) N loodrecht op \(0{,}40\) m", r"\(20\) Nm"),
                          (r"\(30\) N loodrecht op \(1{,}2\) m", r"\(36\) Nm"),
                          (r"\(80\) N onder \(30^{\circ}\) op \(0{,}50\) m", r"\(20\) Nm")], "M", WW),
                 ("kort", r"\(M = 48\) Nm en de kracht staat loodrecht op een arm van \(0{,}60\) m. Hoe groot is F?",
                  r"\(80\) N", W),
                 ("kort", "Bij welke hoek tussen de kracht en de arm is het moment het grootst?", r"\(90^{\circ}\)", W),
                 ("kort", "Hoe groot is het moment van een kracht die door het draaipunt gaat?", r"\(0\) Nm", W),
             ]),
        dict(kop="De wip in evenwicht",
             opdracht="Gebruik de krachtmomentenbalans: links en rechts even grote momenten.",
             oefeningen=[
                 ("kort", r"Links \(20\) kg op \(1{,}5\) m. Rechts \(30\) kg: op welke afstand?", r"\(1{,}0\) m", W),
                 ("kort", r"Links \(40\) kg op \(0{,}90\) m. Rechts \(24\) kg: op welke afstand?", r"\(1{,}5\) m", W),
                 ("kort", r"Links \(25\) kg op \(1{,}2\) m, rechts op \(1{,}0\) m. Welke massa rechts?", r"\(30\) kg", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Hoe dieper een voorwerp dat volledig onder water zit, hoe groter de archimedeskracht erop.", False),
                 ("waar", "De archimedeskracht is even groot als de zwaartekracht op de weggeduwde vloeistof.", True),
                 ("waar", "Het moment van een kracht wordt in joule uitgedrukt.", False),
                 ("waar", "Als de som van alle krachten op een voorwerp nul is, kan het toch nog draaien.", True),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom een stalen schip drijft terwijl een stalen bout zinkt.",
                  "Het schip is hol en zit binnenin vol lucht, dus is zijn gemiddelde massadichtheid kleiner "
                  r"dan \(1000\) kg/\(\text{m}^{3}\). Het duwt zoveel water weg dat de archimedeskracht even groot wordt als zijn "
                  r"zwaartekracht. Bij een bout is er geen lucht, dus is \(\rho\) veel groter dan die van water.", 6),
                 ("open", "Leg uit wat een duikboot doet om te zinken, en waarom dat werkt.",
                  "Ze laat water in haar tanks. Haar massa stijgt dus, en daarmee de zwaartekracht, terwijl "
                  "haar volume gelijk blijft en de archimedeskracht dus niet verandert. Dan haalt de "
                  "zwaartekracht het van de archimedeskracht en zinkt ze.", 5),
                 ("open", "Noem de twee voorwaarden voor statisch evenwicht en leg uit waarom één van de twee "
                          "niet volstaat.",
                  "De som van alle krachten moet nul zijn, het translatie-evenwicht, en de som van alle "
                  "momenten moet nul zijn, het rotatie-evenwicht. Twee gelijke en tegengestelde krachten op "
                  "verschillende plaatsen heffen elkaar op als kracht, maar laten het voorwerp wel draaien.", 6),
                 ("open", "Leg uit waarom een bus met passagiers op het bovendek minder stabiel staat.",
                  "Het zwaartepunt ligt hoger. De bus moet dan minder ver kantelen voor het zwaartepunt buiten "
                  "zijn steunvlak komt, en vanaf dat ogenblik doet het moment van de zwaartekracht hem "
                  "omvallen in plaats van terugvallen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-druk-bij-vaste-stoffen-en-in-vloeistoffen-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Druk bij vaste stoffen en in vloeistoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=REKEN + [r"De massadichtheid van water is \(1000\) kg/\(\text{m}^{3}\) en de luchtdruk \(1013\) hPa."],
    reeksen=[
        dict(kop="Reken de druk",
             opdracht=r"Bereken met \(p = F / A\).",
             oefeningen=[
                 ("rij", [(r"\(400\) N op \(0{,}20\,\text{m}^{2}\)", r"\(2000\) Pa"),
                          (r"\(150\) N op \(0{,}050\,\text{m}^{2}\)", r"\(3000\) Pa"),
                          (r"\(60\) N op \(0{,}0020\,\text{m}^{2}\)", r"\(30\,000\) Pa")], "p", WW),
                 ("kort", r"Een blok van \(180\) N staat op een vierkant van \(0{,}30\) m bij \(0{,}30\) m. Hoe groot is p?",
                  r"\(2000\) Pa", W),
                 ("kort", r"\(p = 5000\) Pa en \(A = 0{,}040\,\text{m}^{2}\). Hoe groot is F?", r"\(200\) N", W),
                 ("kort", r"\(F = 300\) N en \(p = 1500\) Pa. Hoe groot is A?", r"\(0{,}20\,\text{m}^{2}\)", W),
             ]),
        dict(kop="Eenheden van druk",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [(r"\(2\) bar naar Pa", r"\(200\,000\) Pa"),
                          (r"\(1013\) hPa naar Pa", r"\(101\,300\) Pa"),
                          (r"\(4500\) Pa naar kPa", r"\(4{,}5\) kPa")], "Antwoord", WW),
                 ("rij", [(r"\(1\) mbar naar Pa", r"\(100\) Pa"),
                          (r"\(0{,}50\) bar naar hPa", r"\(500\) hPa"),
                          (r"\(25\) kPa naar Pa", r"\(25\,000\) Pa")], "Antwoord", WW),
             ]),
        dict(kop="De hydrostatische druk",
             opdracht=r"Bereken met \(p = \rho \cdot g \cdot h\). Rond af op twee beduidende cijfers.",
             oefeningen=[
                 ("rij", [(r"\(1{,}0\) m diep in water", r"\(9{,}8\) kPa"),
                          (r"\(4{,}0\) m diep in water", r"\(39\) kPa"),
                          (r"\(20\) m diep in water", r"\(200\) kPa")], "p", WW),
                 ("kort", r"Hoe groot is de hydrostatische druk \(3{,}0\) m diep in olie met \(\rho = 900\) kg/\(\text{m}^{3}\)?",
                  r"ongeveer \(26\) kPa", WW),
                 ("kort", r"Een manometer geeft \(3\) bar overdruk aan. Hoe groot is de totale druk ongeveer?",
                  r"ongeveer \(4\) bar", WW),
             ]),
        dict(kop="Veel of weinig druk?",
             opdracht="Schrijf of het voorwerp gemaakt is om de druk groot of klein te maken.",
             oefeningen=[
                 ("rij", [("een punaise", "groot"),
                          ("een brede ski", "klein"),
                          ("een scherp mes", "groot")], "Druk", W),
                 ("rij", [("een plank onder een kraanpoot", "klein"),
                          ("een naald", "groot"),
                          ("dubbele wielen op een vrachtwagen", "klein")], "Druk", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Druk is een vectoriële grootheid.", False),
                 ("waar", "Een millibar en een hectopascal zijn even grote eenheden.", True),
                 ("waar", "De hydrostatische druk op dezelfde diepte is in een smalle buis even groot als in een breed vat.", True),
                 ("waar", "De luchtdruk wordt hoger als je een berg opklimt.", False),
                 ("waar", "Een hydraulische pers levert meer energie dan je er in stopt.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom je met sneeuwschoenen minder diep in de sneeuw zakt dan op naaldhakken.",
                  "Je gewicht blijft gelijk, dus de kracht op de sneeuw ook. Sneeuwschoenen hebben een veel "
                  r"groter zooloppervlak, en in \(p = F / A\) staat A in de noemer, dus wordt de druk veel kleiner. "
                  "Een naaldhak heeft een piepklein oppervlak en dus een enorme druk.", 6),
                 ("open", "Leg uit waarom je je oren moet klaren als je duikt.",
                  "De hydrostatische druk op het trommelvlies groeit met de diepte, terwijl de druk in je oor "
                  "gelijk blijft. Klaren laat lucht door de buis van Eustachius, zodat de druk aan beide kanten "
                  "van het trommelvlies weer even groot is.", 5),
                 ("open", "Leg met het beginsel van Pascal uit hoe een hydraulische pers met een kleine kracht "
                          "een grote kracht kan leveren, en waarom dat geen energie bijmaakt.",
                  "Een drukverandering plant zich in heel de vloeistof voort, dus is de druk bij beide zuigers "
                  r"gelijk. Uit \(F = p \cdot A\) volgt dat de grotere zuiger een grotere kracht geeft. Maar die zuiger "
                  r"komt even veel minder ver, dus blijft de arbeid \(F \cdot \Delta x\) dezelfde.", 6),
                 ("open", "Leg uit waarom er water uit een gaatje in de zijkant van een volle emmer spuit.",
                  "De druk in een vloeistof werkt in alle richtingen, dus ook op de zijwand. Op de hoogte van "
                  "het gaatje duwt de hydrostatische druk het water naar buiten.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-gassen-temperatuur-en-de-gaswetten-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gassen, temperatuur en de gaswetten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE + [r"Vul de temperatuur in de gaswetten altijd in kelvin in. \(R = 8{,}31\) J/(mol.K)."],
    reeksen=[
        dict(kop="Celsius en kelvin",
             opdracht=r"Reken om met \(T = \theta + 273{,}15\). Rond af op een eenheid.",
             oefeningen=[
                 ("rij", [(r"\(20^{\circ}\text{C}\) naar K", r"\(293\) K"),
                          (r"\(-40^{\circ}\text{C}\) naar K", r"\(233\) K"),
                          (r"\(100^{\circ}\text{C}\) naar K", r"\(373\) K")], "Antwoord", WW),
                 ("rij", [(r"\(350\) K naar °C", r"\(77^{\circ}\text{C}\)"),
                          (r"\(273\) K naar °C", r"\(0^{\circ}\text{C}\)"),
                          (r"\(0\) K naar °C", r"\(-273^{\circ}\text{C}\)")], "Antwoord", WW),
             ]),
        dict(kop="Welk proces?",
             opdracht="Schrijf isotherm, isobaar of isochoor, en de wet die erbij hoort.",
             oefeningen=[
                 ("kort", "De temperatuur blijft gelijk.", r"isotherm, \(p \cdot V = \text{constant}\)", WL),
                 ("kort", "De druk blijft gelijk.", r"isobaar, \(V / T = \text{constant}\)", WL),
                 ("kort", "Het volume blijft gelijk.", r"isochoor, \(p / T = \text{constant}\)", WL),
             ]),
        dict(kop="Reken met de gaswetten",
             opdracht="Zoek de ontbrekende waarde. De stofhoeveelheid blijft gelijk.",
             oefeningen=[
                 ("rij", [(r"\(6{,}0\) L bij \(1{,}0\) bar naar \(2{,}0\) L, isotherm", r"\(3{,}0\) bar"),
                          (r"\(2{,}0\) L bij \(3{,}0\) bar naar \(1{,}0\) bar, isotherm", r"\(6{,}0\) L"),
                          (r"\(8{,}0\) L bij \(2{,}0\) bar naar \(4{,}0\) bar, isotherm", r"\(4{,}0\) L")], "Antwoord", WW),
                 ("rij", [(r"\(3{,}0\) L bij \(300\) K naar \(600\) K, isobaar", r"\(6{,}0\) L"),
                          (r"\(5{,}0\) L bij \(400\) K naar \(200\) K, isobaar", r"\(2{,}5\) L"),
                          (r"\(2{,}0\) bar bij \(250\) K naar \(500\) K, isochoor", r"\(4{,}0\) bar")], "Antwoord", WW),
                 ("kort", r"Een gas van \(1{,}0\) L bij \(2{,}0\) bar en \(300\) K gaat naar \(2{,}0\) L bij \(3{,}0\) bar. Wat is de nieuwe T?",
                  r"\(900\) K", WW),
             ]),
        dict(kop="Grafieken van een gas",
             opdracht="Schrijf hoe de grafiek eruitziet.",
             oefeningen=[
                 ("kort", "Een p(V)-grafiek bij constante temperatuur.", "een dalende kromme", WW),
                 ("kort", "Een V(T)-grafiek bij constante druk, met T in kelvin.",
                  "een rechte door de oorsprong", WW),
                 ("kort", "Een p(T)-grafiek bij constant volume, met T in kelvin.",
                  "een rechte door de oorsprong", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In de gaswetten mag je de temperatuur in graden Celsius invullen.", False),
                 ("waar", r"Een temperatuursverschil van \(15^{\circ}\text{C}\) is hetzelfde als een verschil van \(15\) K.", True),
                 ("waar", "De gasconstante R is voor elk gas een andere waarde.", False),
                 ("waar", "Bij het absolute nulpunt is de druk van een ideaal gas nul.", True),
                 ("waar", "De druk van een gas hangt niet af van het aantal deeltjes in het vat.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met het deeltjesmodel.",
             oefeningen=[
                 ("open", "Leg met het deeltjesmodel uit waarom de druk in een gesloten vat stijgt als je het gas opwarmt.",
                  "Een hogere temperatuur betekent dat de deeltjes gemiddeld sneller bewegen. Ze botsen dan "
                  "harder en vaker tegen de wand, en elke botsing duwt even tegen de wand. Samen geeft dat een "
                  r"grotere druk. Het volume blijft gelijk, dus geldt \(p / T = \text{constant}\).", 6),
                 ("open", "Leg uit waarom een spuitbus niet in de zon mag liggen.",
                  r"Het volume van de bus staat vast, dus geldt \(p / T = \text{constant}\): wordt de bus warmer, dan "
                  "stijgt de druk mee. Boven een bepaalde druk kan de bus barsten. Daarom staat er dat ze niet "
                  r"boven \(50^{\circ}\text{C}\) mag komen.", 5),
                 ("open", "Leg uit wat het absolute nulpunt betekent voor de deeltjes van een ideaal gas, en "
                          "waarom het niet lager kan.",
                  r"Bij \(0\) K staan de deeltjes in het model stil: hun kinetische energie is nul, dus zijn ook de "
                  "druk en het volume van een ideaal gas nul. Lager kan niet, want deeltjes kunnen niet "
                  "langzamer bewegen dan stil.", 5),
                 ("open", "Leg uit waarom de luchtdruk kleiner wordt als je hoger komt in de atmosfeer.",
                  "De luchtdruk komt van het gewicht van alle lucht boven je. Hoe hoger je komt, hoe minder "
                  "lucht er nog boven je zit, dus hoe kleiner die druk.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-arbeid-energie-vermogen-en-rendement-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Arbeid, energie, vermogen en rendement",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=REKEN,
    reeksen=[
        dict(kop="Positieve, negatieve of geen arbeid?",
             opdracht="Schrijf positief, negatief of geen arbeid.",
             oefeningen=[
                 ("kort", "Je duwt een kar vooruit in de zin van de beweging.", "positief", WW),
                 ("kort", "De wrijvingskracht op een schuivende kist.", "negatief", WW),
                 ("kort", "De normaalkracht op een kist die over een vlakke vloer schuift.", "geen arbeid", WW),
                 ("kort", "De zwaartekracht op een voorwerp dat je optilt.", "negatief", WW),
             ]),
        dict(kop="Reken de arbeid",
             opdracht=r"Bereken met \(W = F \cdot \Delta x \cdot \cos \alpha\).",
             oefeningen=[
                 ("rij", [(r"\(60\) N over \(5{,}0\) m, in de zin", r"\(300\) J"),
                          (r"\(40\) N over \(12\) m, in de zin", r"\(480\) J"),
                          (r"\(100\) N over \(3{,}0\) m, onder \(60^{\circ}\)", r"\(150\) J")], "W", WW),
                 ("kort", r"\(W = 250\) J over \(10\) m in de zin van de beweging. Hoe groot is F?", r"\(25\) N", W),
                 ("kort", r"Hoeveel arbeid verricht een kracht van \(80\) N die loodrecht op de verplaatsing staat?",
                  r"\(0\) J", W),
             ]),
        dict(kop="Kinetische en potentiële energie",
             opdracht=r"Bereken met \(E_{k} = m \cdot v^{2} / 2\) en \(E_{p,gr} = m \cdot g \cdot h\).",
             oefeningen=[
                 ("rij", [(r"\(m = 2{,}0\) kg, \(v = 10\) m/s", r"\(100\) J"),
                          (r"\(m = 1000\) kg, \(v = 30\) m/s", r"\(450\) kJ"),
                          (r"\(m = 0{,}50\) kg, \(v = 4{,}0\) m/s", r"\(4{,}0\) J")], "Ek", WW),
                 ("rij", [(r"\(m = 4{,}0\) kg, \(h = 2{,}5\) m", r"\(98{,}1\) J"),
                          (r"\(m = 70\) kg, \(h = 10\) m", r"\(6{,}87\) kJ"),
                          (r"\(m = 0{,}20\) kg, \(h = 1{,}5\) m", r"\(2{,}94\) J")], r"\(E_{p,gr}\)", WW),
                 ("kort", r"Een veer met \(k = 400\) N/m is \(0{,}10\) m ingedrukt. Hoe groot is \(E_{p,el}\)?", r"\(2{,}0\) J", W),
             ]),
        dict(kop="Vermogen en rendement",
             opdracht=r"Bereken met \(P = |\Delta E| / \Delta t\) en \(\eta = E_{\text{nuttig}} / E_{\text{totaal}}\).",
             oefeningen=[
                 ("rij", [(r"\(36\) kJ in \(30\) s", r"\(1{,}2\) kW"),
                          (r"\(600\) J in \(4{,}0\) s", r"\(150\) W"),
                          (r"\(2{,}0\) kW gedurende \(10\) s", r"\(20\) kJ")], "Antwoord", WW),
                 ("rij", [(r"\(120\) J in, \(30\) J nuttig", r"\(25\,\%\)"),
                          (r"\(500\) J in, \(400\) J warmte", r"\(20\,\%\)"),
                          (r"\(80\) J in, \(60\) J nuttig", r"\(75\,\%\)")], "η", WW),
                 ("kort", r"Een motor heeft een rendement van \(40\,\%\) en krijgt \(1500\) J. Hoeveel nuttige energie levert hij?",
                  r"\(600\) J", W),
             ]),
        dict(kop="Welke omzetting?",
             opdracht="Schrijf van welke energievorm naar welke.",
             oefeningen=[
                 ("rij", [("een bal valt van een muur", r"\(E_{p,gr}\) naar \(E_{k}\)"),
                          ("een ingedrukte veer schiet los", r"\(E_{p,el}\) naar \(E_{k}\)"),
                          ("een waterkoker warmt water op", "elektrisch naar thermisch")], "Omzetting", WL),
                 ("rij", [("een batterij doet een lampje branden", "chemisch naar elektrisch en licht"),
                          ("een plant doet fotosynthese", "straling naar chemisch"),
                          ("een bal die je omhoog gooit", r"\(E_{k}\) naar \(E_{p,gr}\)")], "Omzetting", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een auto die twee keer zo snel rijdt, heeft twee keer zoveel kinetische energie.", False),
                 ("waar", "Een kilowattuur is een eenheid van vermogen.", False),
                 ("waar", r"Een rendement van meer dan \(100\,\%\) kan niet bestaan.", True),
                 ("waar", "Een voorwerp dat stilstaat, kan toch potentiële energie hebben.", True),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom je geen arbeid verricht op een doos die je horizontaal door een "
                          "kamer draagt, al voelt het zwaar aan.",
                  "De kracht waarmee je de doos omhoog houdt is verticaal, en de verplaatsing is horizontaal. "
                  r"De hoek is dus \(90^{\circ}\) en \(\cos 90^{\circ}\) is nul, dus is W nul. Je spieren verbruiken wel energie, maar "
                  "dat is geen arbeid op de doos.", 5),
                 ("open", "Leg uit wat energiedissipatie is en waarom de energie daarbij niet verdwijnt.",
                  "Bij een omzetting gaat een deel van de bruikbare energie naar een minder bruikbare vorm, "
                  "meestal warmte. Die energie bestaat nog, maar is zo verspreid in de omgeving dat je ze niet "
                  "meer nuttig kan gebruiken. De wet van behoud van energie blijft dus gelden.", 5),
                 ("open", "Leg uit waarom een remweg bij een dubbele snelheid vier keer zo lang is.",
                  r"In \(E_{k} = m \cdot v^{2} / 2\) staat de snelheid in het kwadraat, dus heeft een auto bij een dubbele "
                  "snelheid vier keer zoveel kinetische energie. De remkracht moet die hele energie wegnemen "
                  r"met \(W = F \cdot \Delta x\), dus is bij dezelfde remkracht een vier keer langere weg nodig.", 6),
                 ("open", "Leg uit waarom het joule-effect in een gloeilamp gewenst is en in een laadkabel niet.",
                  "In een gloeilamp wordt de draad zo heet dat hij licht geeft, dus daar is de opwarming net de "
                  "bedoeling. In een laadkabel levert die warmte niets op: ze is verlies, en bij te veel stroom "
                  "zelfs brandgevaarlijk.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-warmte-faseovergangen-en-de-warmtebalans-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Warmte, faseovergangen en de warmtebalans",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE + [r"De specifieke warmtecapaciteit van water is \(4186\) J/(kg.K)."],
    reeksen=[
        dict(kop="Welke faseovergang?",
             opdracht="Schrijf de naam van de faseovergang, en of er warmte nodig is of vrijkomt.",
             oefeningen=[
                 ("rij", [("vast naar vloeibaar", "smelten, warmte nodig"),
                          ("vloeibaar naar vast", "stollen, warmte komt vrij"),
                          ("vloeibaar naar gas", "verdampen, warmte nodig")], "Overgang", WL),
                 ("rij", [("gas naar vloeibaar", "condenseren, warmte komt vrij"),
                          ("vast naar gas", "sublimeren, warmte nodig"),
                          ("gas naar vast", "desublimeren, warmte komt vrij")], "Overgang", WL),
             ]),
        dict(kop="Welke vorm van warmtetransport?",
             opdracht="Schrijf geleiding, convectie of straling.",
             oefeningen=[
                 ("rij", [("de warmte van de zon door de ruimte", "straling"),
                          ("een metalen steel die heet wordt", "geleiding"),
                          ("warme lucht die naar het plafond stijgt", "convectie")], "Transport", WW),
                 ("rij", [("water in een pan dat gaat circuleren", "convectie"),
                          ("de warmte van een haardvuur op je gezicht", "straling"),
                          ("een houten tafel die langzaam opwarmt", "geleiding")], "Transport", WW),
             ]),
        dict(kop="Reken de merkbare warmte",
             opdracht=r"Bereken met \(Q = c \cdot m \cdot \Delta T\).",
             oefeningen=[
                 ("rij", [(r"\(1{,}0\) kg water, \(20\) K", r"\(83{,}7\) kJ"),
                          (r"\(0{,}50\) kg water, \(60\) K", r"\(126\) kJ"),
                          (r"\(3{,}0\) kg water, \(5{,}0\) K", r"\(62{,}8\) kJ")], "Q", WW),
                 ("kort", r"Een voorwerp van \(2{,}0\) kg met \(c = 450\) J/(kg.K) krijgt \(18\) kJ. Hoeveel stijgt zijn T?",
                  r"\(20\) K", W),
                 ("kort", r"Een voorwerp heeft \(C = 800\) J/K en warmt \(15\) K op. Hoeveel warmte kostte dat?",
                  r"\(12\) kJ", W),
             ]),
        dict(kop="Reken de latente warmte",
             opdracht=r"Bereken met \(Q = l \cdot m\). De waarden staan bij de opgave.",
             oefeningen=[
                 ("rij", [(r"\(0{,}40\) kg ijs smelten, \(l_{s} = 334\) kJ/kg", r"\(134\) kJ"),
                          (r"\(1{,}0\) kg water verdampen, \(l_{v} = 2260\) kJ/kg", r"\(2260\) kJ"),
                          (r"\(0{,}25\) kg lood smelten, \(l_{s} = 24{,}5\) kJ/kg", r"\(6{,}1\) kJ")], "Q", WW),
                 ("kort", r"Hoeveel warmte komt vrij als \(0{,}20\) kg water van \(100^{\circ}\text{C}\) condenseert, met \(l_{v} = 2260\) kJ/kg?",
                  r"\(452\) kJ", WW),
             ]),
        dict(kop="De warmtebalans",
             opdracht="Reken uit in een geïsoleerd vat.",
             oefeningen=[
                 ("kort", r"\(0{,}20\) kg water van \(70^{\circ}\text{C}\) bij \(0{,}20\) kg water van \(30^{\circ}\text{C}\). Welke eindtemperatuur?",
                  r"\(50^{\circ}\text{C}\)", W),
                 ("kort", r"\(0{,}10\) kg water van \(90^{\circ}\text{C}\) bij \(0{,}30\) kg water van \(10^{\circ}\text{C}\). Welke eindtemperatuur?",
                  r"\(30^{\circ}\text{C}\)", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Tijdens een faseovergang blijft de temperatuur van de stof gelijk.", True),
                 ("waar", r"Water kan enkel verdampen bij \(100^{\circ}\text{C}\).", False),
                 ("waar", "Een stof met een kleine specifieke warmtecapaciteit warmt traag op.", False),
                 ("waar", "Twee voorwerpen in thermisch evenwicht hebben dezelfde temperatuur.", True),
                 ("waar", "Een groot voorwerp heeft altijd een hogere temperatuur dan een klein voorwerp.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met het deeltjesmodel.",
             oefeningen=[
                 ("open", r"Leg uit waarom de temperatuur gelijk blijft terwijl ijs van \(0^{\circ}\text{C}\) smelt.",
                  "Alle toegevoerde warmte gaat naar het losmaken van de deeltjes uit hun vast verband, dus "
                  "naar de inwendige potentiële energie. De gemiddelde snelheid van de deeltjes verandert niet, "
                  "en de temperatuur hoort net bij die gemiddelde kinetische energie. In een curve zie je "
                  "daarom een plateau.", 6),
                 ("open", "Leg uit waarom metaal kouder aanvoelt dan hout bij dezelfde temperatuur.",
                  "Metaal geleidt warmte goed, dus voert het de warmte van je hand snel weg en voelt het koud. "
                  "Hout geleidt slecht, dus blijft de warmte bij je hand en voelt het niet koud. De temperatuur "
                  "van de twee is wel dezelfde.", 5),
                 ("open", "Leg uit waarom verdampende alcohol op je hand koud aanvoelt.",
                  "Verdampen is een faseovergang die latente warmte nodig heeft. De alcohol haalt die warmte "
                  "uit je hand, dus koelt je hand af. Zweten werkt op dezelfde manier.", 4),
                 ("open", "Leg uit waarom de zee lang koel blijft in de lente en lang warm in de herfst.",
                  r"Water heeft een grote specifieke warmtecapaciteit, \(4186\) J/(kg.K), dus is er veel warmte "
                  "nodig per kilogram per kelvin. Daardoor warmt de zee traag op en koelt ze ook traag af. "
                  "Zand of lucht, met een kleinere c, volgen de buitentemperatuur veel sneller.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektrische-stroom-spanning-en-weerstand-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Elektrische stroom, spanning en weerstand",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De wet van Ohm",
             opdracht=r"Bereken met \(R = U / I\). Zet de eenheid bij je antwoord.",
             oefeningen=[
                 ("rij", [(r"\(U = 12\) V, \(I = 0{,}40\) A", r"\(R = 30\) \(\Omega\)"),
                          (r"\(U = 230\) V, \(I = 2{,}0\) A", r"\(R = 115\) \(\Omega\)"),
                          (r"\(U = 9{,}0\) V, \(I = 0{,}30\) A", r"\(R = 30\) \(\Omega\)")], "Antwoord", WW),
                 ("rij", [(r"\(U = 6{,}0\) V, \(R = 20\) \(\Omega\)", r"\(I = 0{,}30\) A"),
                          (r"\(U = 230\) V, \(R = 460\) \(\Omega\)", r"\(I = 0{,}50\) A"),
                          (r"\(I = 0{,}25\) A, \(R = 80\) \(\Omega\)", r"\(U = 20\) V")], "Antwoord", WW),
             ]),
        dict(kop="Serie of parallel?",
             opdracht="Bereken de substitutieweerstand.",
             oefeningen=[
                 ("rij", [(r"\(20\) \(\Omega\) en \(40\) \(\Omega\) in serie", r"\(60\) \(\Omega\)"),
                          (r"\(20\) \(\Omega\) en \(40\) \(\Omega\) parallel", r"\(13{,}3\) \(\Omega\)"),
                          (r"\(100\) \(\Omega\) en \(100\) \(\Omega\) parallel", r"\(50\) \(\Omega\)")], "Rs", WW),
                 ("rij", [(r"drie keer \(90\) \(\Omega\) parallel", r"\(30\) \(\Omega\)"),
                          (r"\(10\) \(\Omega\), \(20\) \(\Omega\) en \(30\) \(\Omega\) in serie", r"\(60\) \(\Omega\)"),
                          (r"\(12\) \(\Omega\) en \(24\) \(\Omega\) parallel", r"\(8{,}0\) \(\Omega\)")], "Rs", WW),
                 ("kort", r"\(5{,}0\) \(\Omega\) in serie met twee keer \(10\) \(\Omega\) parallel. Hoe groot is Rs?", r"\(10\) \(\Omega\)", W),
             ]),
        dict(kop="Door de schakeling rekenen",
             opdracht="Reken stap voor stap uit.",
             oefeningen=[
                 ("kort", r"Over \(30\) \(\Omega\) en \(60\) \(\Omega\) in serie staat \(18\) V. Hoe groot is I?", r"\(0{,}20\) A", W),
                 ("kort", r"In diezelfde schakeling: hoe groot is de spanning over de \(60\) \(\Omega\)?", r"\(12\) V", W),
                 ("kort", r"Twee lampen van elk \(100\) \(\Omega\) staan parallel op \(230\) V. Hoe groot is de totale stroom?",
                  r"\(4{,}6\) A", W),
                 ("kort", r"Een toestel op \(230\) V trekt \(1{,}5\) A. Hoe groot is zijn vermogen?", r"\(345\) W", W),
             ]),
        dict(kop="Meten en veiligheid",
             opdracht="Antwoord in één woord of één korte zin.",
             oefeningen=[
                 ("kort", "Hoe sluit je een ampèremeter aan?", "in serie", WW),
                 ("kort", "Hoe sluit je een voltmeter aan?", "parallel", WW),
                 ("kort", "Welke stand van een multimeter meet gelijkspanning?", "DCV", W),
                 ("kort", "Welk veiligheidsaspect legt de kring af bij een te grote stroom?",
                  "de automatische zekering", WL),
                 ("kort", "Welk veiligheidsaspect merkt dat er stroom wegloopt die niet terugkomt?",
                  "de verliesstroomschakelaar", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De elektronen in een draad bewegen in de conventionele stroomzin.", False),
                 ("waar", "In een serieschakeling is de som van de spanningen gelijk aan de bronspanning.", True),
                 ("waar", "De substitutieweerstand van een parallelschakeling is kleiner dan de kleinste weerstand.", True),
                 ("waar", "Een isolator heeft een kleine weerstand.", False),
                 ("waar", "De stopcontacten in een huis staan in serie geschakeld.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom een kerstboomsnoer in serie helemaal uitgaat als één lampje stuk is, "
                          "en waarom dat bij een parallelsnoer niet gebeurt.",
                  "In serie is er maar één weg voor de stroom. Valt één lampje weg, dan is de kring onderbroken "
                  "en loopt er nergens stroom. Parallel heeft elke lamp haar eigen tak, dus blijft de stroom "
                  "door de andere takken lopen.", 6),
                 ("open", "Leg uit waarom een kortsluiting gevaarlijk is, met de wet van Ohm erbij.",
                  r"Bij een kortsluiting is de weerstand in de kring heel klein geworden. Uit \(I = U / R\) volgt "
                  "dan een heel grote stroom. Door het joule-effect worden de draden daardoor snel heet, met "
                  "brandgevaar.", 5),
                 ("open", "Leg uit waarom je een elektrisch toestel nooit met natte handen bedient.",
                  "Water verlaagt de weerstand van je huid sterk. Bij dezelfde spanning loopt er dan volgens "
                  r"\(I = U / R\) veel meer stroom door je lichaam, en dat is net wat elektrocutie gevaarlijk maakt.", 5),
                 ("open", "Leg uit wat een aarddraad doet en waarom hij een mens beschermt.",
                  "Komt er door een defect stroom op de metalen kast van een toestel, dan leidt de aarddraad "
                  "die naar de aarde. Die weg heeft een veel kleinere weerstand dan een mens, dus gaat de "
                  "stroom daarlangs en niet door wie de kast aanraakt. Samen met een zekering of een "
                  "verliesstroomschakelaar wordt de kring dan afgelegd.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-licht-weerkaatsing-breking-en-lenzen-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Licht: weerkaatsing, breking en lenzen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Ondoorschijnend, doorschijnend of doorzichtig?",
             opdracht="Schrijf welk van de drie.",
             oefeningen=[
                 ("rij", [("helder vensterglas", "doorzichtig"),
                          ("matglas", "doorschijnend"),
                          ("een houten plank", "ondoorschijnend")], "Welk?", WW),
                 ("rij", [("een blad papier", "doorschijnend"),
                          ("een metalen plaat", "ondoorschijnend"),
                          ("stil helder water", "doorzichtig")], "Welk?", WW),
             ]),
        dict(kop="De terugkaatsingswetten",
             opdracht="Antwoord in één woord of één getal.",
             oefeningen=[
                 ("kort", r"Een straal valt onder een invalshoek van \(40^{\circ}\). Hoe groot is de weerkaatsingshoek?",
                  r"\(40^{\circ}\)", W),
                 ("kort", r"Een straal valt onder \(25^{\circ}\) met het spiegeloppervlak. Hoe groot is de invalshoek?",
                  r"\(65^{\circ}\)", W),
                 ("kort", "Ten opzichte van welke lijn meet je de invalshoek?", "de normaal", WW),
                 ("kort", "Hoe noemt men het punt waar de invallende straal de spiegel raakt?",
                  "het invalspunt", WW),
                 ("kort", "Welke weerkaatsing krijg je op een ruw oppervlak?", "diffuse weerkaatsing", WL),
             ]),
        dict(kop="Het beeld in een vlakke spiegel",
             opdracht="Schrijf de aard, de stand en de grootte, of reken de afstand.",
             oefeningen=[
                 ("kort", "Wat is de aard van het beeld in een vlakke spiegel?", "virtueel", WW),
                 ("kort", "Wat is de stand en de grootte van dat beeld?",
                  "rechtopstaand en even groot", WL),
                 ("kort", r"Je staat \(1{,}5\) m voor een vlakke spiegel. Hoe ver staat je beeld van jou?", r"\(3{,}0\) m", W),
                 ("kort", "Hoe noemt men een beeld dat je wel op een scherm kan opvangen?", "een reëel beeld", WW),
             ]),
        dict(kop="Schaduw en verduistering",
             opdracht="Antwoord in één korte zin.",
             oefeningen=[
                 ("kort", "In welk deel van de schaduw komt geen licht van de bron?", "de kernschaduw", WW),
                 ("kort", "Welk hemellichaam staat ertussen bij een zonsverduistering?", "de maan", W),
                 ("kort", "Welk hemellichaam staat ertussen bij een maansverduistering?", "de aarde", W),
                 ("kort", "Geeft een kleine of een grote lichtbron de scherpste schaduw?", "een kleine", W),
             ]),
        dict(kop="Breking",
             opdracht="Schrijf hoe de straal buigt, en of de hoek groter of kleiner wordt.",
             oefeningen=[
                 ("kort", "Van lucht schuin in water.", "naar de normaal toe, hoek kleiner", WL),
                 ("kort", "Van glas schuin in lucht.", "van de normaal weg, hoek groter", WL),
                 ("kort", "Loodrecht op het grensvlak tussen lucht en water.", "rechtdoor, geen breking", WL),
             ]),
        dict(kop="De dunne bolle lens",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("parallel met de optische as", "gaat door het brandpunt"),
                          ("door het optisch middelpunt", "gaat rechtdoor"),
                          ("door het brandpunt vóór de lens", "gaat parallel verder")], "Na de lens", WL),
                 ("kort", "Een voorwerp staat verder dan twee keer de brandpuntsafstand. Welk beeld?",
                  "reëel, omgekeerd, kleiner", WL),
                 ("kort", "Een voorwerp staat tussen de lens en het brandpunt. Welk beeld?",
                  "virtueel, rechtopstaand, groter", WL),
                 ("kort", r"Een voorwerp is \(2{,}0\) cm groot en het beeld \(6{,}0\) cm. Hoe groot is de vergrotingsfactor?",
                  r"\(3\)", W),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom je je spiegelbeeld niet ziet in een ruw vel papier, terwijl de "
                          "terugkaatsingswetten daar ook gelden.",
                  "In elk punt van het papier geldt de wet wel, maar het oppervlak is onregelmatig, dus staat "
                  "de normaal in elk punt een andere kant op. De stralen kaatsen daardoor in alle richtingen "
                  "terug, een diffuse weerkaatsing, en komen nergens samen tot een beeld.", 6),
                 ("open", "Leg uit waarom de bodem van een zwembad minder diep lijkt dan hij is.",
                  "De stralen van de bodem buigen bij het verlaten van het water van de normaal weg, want ze "
                  "gaan van een optisch dichtere naar een optisch ijlere stof. Je oog volgt die gebroken "
                  "stralen rechtdoor door en komt zo uit op een punt hoger dan de echte bodem. Dat heet de "
                  "schijnbare verhoging.", 6),
                 ("open", "Leg uit waarom een loep een vergroot beeld geeft en waarom dat beeld virtueel is.",
                  "Je houdt het voorwerp tussen de lens en het brandpunt. De gebroken stralen lopen dan uit "
                  "elkaar en komen nergens echt samen, ze lijken enkel uit één punt te komen. Daarom is het "
                  "beeld virtueel, rechtopstaand en groter, en kan je het niet op een scherm opvangen.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meten-en-onderzoek-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en onderzoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Goede of slechte werkwijze?",
             opdracht="Schrijf goed of slecht, en in één woord waarom.",
             oefeningen=[
                 ("kort", "Een multimeter op de weerstandsstand laten staan na het meten.",
                  "slecht, zet hem uit", WL),
                 ("kort", "Een handleiding lezen voor je een toestel gebruikt.", "goed", WL),
                 ("kort", "Een elektrisch toestel bedienen met natte handen.", "slecht, elektrocutie", WL),
                 ("kort", r"Een stroom van \(2\) A meten op het kleinste meetbereik.",
                  "slecht, overbelasting", WL),
                 ("kort", "Restvloeistof volgens het etiket verwerken.", "goed", WL),
             ]),
        dict(kop="Welk meetinstrument?",
             opdracht="Schrijf de naam van het instrument.",
             oefeningen=[
                 ("rij", [("een kracht", "dynamometer"),
                          ("een massa", "balans"),
                          ("een volume vloeistof", "maatcilinder")], "Instrument", WW),
                 ("rij", [("de luchtdruk", "barometer"),
                          ("de druk in een gasvat", "manometer"),
                          ("een temperatuur", "thermometer")], "Instrument", WW),
                 ("rij", [(r"een tijdsduur van \(2\) s", "chronometer"),
                          ("een spanning", "voltmeter of multimeter"),
                          ("een stroomsterkte", "ampèremeter of multimeter")], "Instrument", WL),
             ]),
        dict(kop="Nauwkeurig aflezen",
             opdracht="Antwoord in één woord of één korte zin.",
             oefeningen=[
                 ("kort", "Hoe noemt men de afleesfout als je schuin op een instrument kijkt?",
                  "een parallaxfout", WW),
                 ("kort", "Hoe noemt men de holle kromming van water in een smalle buis?", "de meniscus", WW),
                 ("kort", "Waar lees je het peil van water in een maatcilinder af?",
                  "onderaan de meniscus", WL),
                 ("kort", "Waarom staat er een maximale waarde op een dynamometer?",
                  "meer rekt de veer blijvend uit", WL),
             ]),
        dict(kop="De stappen van een onderzoek",
             opdracht=r"Zet deze zes stappen in de juiste volgorde: schrijf \(1\) bij de stap die eerst komt en \(6\) bij de laatste.",
             oefeningen=[
                 ("rij", [("data waarnemen en verzamelen", r"\(4\)"),
                          ("de probleemstelling afbakenen", r"\(1\)"),
                          ("een conclusie formuleren", r"\(5\)")], "Cijfer", W),
                 ("rij", [("een onderzoeksplan opstellen", r"\(3\)"),
                          ("een onderzoeksvraag en hypothese opstellen", r"\(2\)"),
                          ("reflecteren over je methode", r"\(6\)")], "Cijfer", W),
             ]),
        dict(kop="De criteria voor een onderzoeksvraag",
             opdracht="Welk criterium schendt deze vraag? Kies uit open, enkelvoudig, objectief, haalbaar, onderzoekbaar.",
             oefeningen=[
                 ("kort", "Valt een koffiefilter naar beneden als je hem loslaat?", "open", WW),
                 ("kort", "Hoe groot is de valversnelling in België?", "onderzoekbaar", WW),
                 ("kort", "Waarom is zonne-energie de beste keuze?", "objectief", WW),
                 ("kort", "Hoe hangt de druk in de kern van de zon af van haar massa?", "haalbaar", WW),
                 ("kort", "Hoe hangt de valtijd af van het aantal filters en van de hoogte van het lokaal?",
                  "enkelvoudig", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een hypothese die verworpen wordt, maakt je onderzoek waardeloos.", False),
                 ("waar", "Bij het analyseren mag je metingen weglaten die niet in je hypothese passen.", False),
                 ("waar", "Een conclusie moet antwoord geven op de onderzoeksvraag.", True),
                 ("waar", "Een instrument met fijnere streepjes is altijd de beste keuze.", False),
                 ("waar", "De M van STEM staat voor wiskunde.", True),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", "Je onderzoekt hoe snel water afkoelt in drie verschillende bekers. Noem drie dingen "
                          "die je gelijk houdt, en leg uit waarom.",
                  "De begintemperatuur, de hoeveelheid water en de temperatuur van het lokaal, en je meet ook "
                  "op dezelfde tijdstippen. Enkel wat je onderzoekt mag verschillen, hier het soort beker. "
                  "Verandert er meer dan één ding, dan weet je niet waardoor het verschil komt.", 6),
                 ("open", "Leg uit waarom je bij een multimeter op het grootste meetbereik begint.",
                  "Op een te klein bereik kan het instrument overbelast raken en stuk gaan. Je begint dus ruim "
                  "en gaat daarna een stand fijner, tot je een goed leesbare waarde hebt.", 4),
                 ("open", "Noem de vier disciplines van STEM en geef bij elk een voorbeeld uit de coronacrisis.",
                  "Wetenschappen voor het ontwikkelen van het vaccin, technologie om het te maken en koel te "
                  "houden, ingenieurswetenschappen voor de productielijnen en de koelketen, en wiskunde om de "
                  "verspreiding van het virus in kaart te brengen.", 6),
                 ("open", "Leg uit waarom je een meting herhaalt en het gemiddelde neemt.",
                  "Elke meting heeft een toevallige afleesfout. Door te herhalen en het gemiddelde te nemen, "
                  "vallen die fouten deels tegen elkaar weg en komt je resultaat dichter bij de echte waarde.", 4),
             ]),
    ],
)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-grootheden-eenheden-en-nauwkeurig-meten-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet bij elke grootheid de eenheid én haar symbool. Veel eenheden dragen de naam van "
                    "een natuurkundige, en die schrijf je met een kleine letter, het symbool met een "
                    "hoofdletter.",
             waarom=[
                 None, None,
                 "Let op het laatste: een moment is een kracht maal een arm, dus staat het in newtonmeter. "
                 "Dezelfde eenheid als arbeid, maar een heel andere grootheid.",
             ]),
        dict(aanpak="Leer de voorvoegsels als machten van tien. Van mega tot nano is het hetzelfde rijtje "
                    "dat in elke omrekening terugkomt.",
             waarom=[None, None]),
        dict(aanpak="Zet eerst om naar de SI-eenheid en reken daarna. Voor km/h naar m/s deel je door "
                    "\\(3{,}6\\), omgekeerd vermenigvuldig je ermee.",
             waarom=[
                 None, None,
                 "Voor kelvin tel je \\(273\\) bij de graden Celsius op, of je trekt ze er weer af. Een "
                 "temperatuurverschil is in beide eenheden hetzelfde getal.",
             ]),
        dict(aanpak="In de wetenschappelijke notatie staat er één cijfer voor de komma. Beduidende cijfers "
                    "tel je van het eerste cijfer dat niet nul is tot het laatste opgeschreven cijfer.",
             waarom=[
                 None,
                 "Let op het verschil tussen \\(12{,}50\\) en \\(7000\\): de nullen na de komma zijn "
                 "gemeten, de nullen voor de komma niet. Wil je zeggen dat \\(7000\\) kg nauwkeurig is, "
                 "dan schrijf je \\(7{,}000 \\times 10^{3}\\) kg.",
             ]),
        dict(aanpak="Een vector heeft een grootte én een richting en zin. Kan je het antwoord met één getal "
                    "geven, dan is het geen vector.",
             waarom=[
                 None, None, None,
                 "Druk werkt in alle richtingen even hard, dus heeft ze geen zin. Daarom is ze een scalair, "
                 "ook al wordt ze door een kracht veroorzaakt.",
             ]),
        dict(aanpak="Kijk naar de grafiek of naar wat er met y gebeurt als x verdubbelt. Een rechte door de "
                    "oorsprong is recht evenredig, een rechte ernaast is enkel lineair.",
             waarom=[
                 None, None,
                 "Dit onderscheid wordt vaak over het hoofd gezien: lineair is het ruimere geval, recht "
                 "evenredig het bijzondere geval dat door de oorsprong gaat.",
                 None,
             ]),
        dict(aanpak="Omvormen is op elke stap hetzelfde doen aan beide kanten van het gelijkheidsteken. "
                    "Controleer je antwoord altijd met een schatting en met de eenheden.",
             waarom=[
                 None, None,
                 "Zo'n schatting kost je drie seconden en vindt juist de fouten die een rekenmachine niet "
                 "ziet: een komma of een factor duizend verkeerd.",
                 "Meetbereik komt vóór nauwkeurigheid. Een fijne schaalverdeling helpt je niets als je "
                 "volume er niet in past.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-eenparig-rechtlijnige-beweging-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De afgelegde weg is alles wat je stapte, de verplaatsing enkel het verschil tussen "
                    "begin en eind. Daarom kan de verplaatsing negatief of nul zijn en de weg nooit.",
             waarom=[
                 "Twee ronden brengen je terug waar je begon, dus is de verplaatsing nul terwijl je "
                 "\\(800\\) m liep. Dat is het duidelijkste voorbeeld van het verschil.",
                 None,
                 "Het minteken zegt enkel dat de beweging tegen de positieve zin in gaat, niet dat er "
                 "minder afstand is afgelegd.",
                 None,
             ]),
        dict(aanpak="Eén formule in drie gedaanten: v = Δx : Δt, Δx = v · Δt en Δt = Δx : v. Zet de tijd "
                    "altijd eerst in dezelfde eenheid als de snelheid.",
             waarom=[
                 "Een kwartier is \\(0{,}25\\) h, dus \\(45 : 0{,}25 = 180\\) km/h. Reken je met minuten, "
                 "dan zit je er zestig keer naast.",
                 None,
             ]),
        dict(aanpak="Lees een positiefunctie als x = beginpositie + snelheid · t. Het getal vooraan is waar "
                    "het voorwerp vertrok, het getal bij t hoe snel het gaat.",
             waarom=[
                 "Een minteken bij t betekent dat het voorwerp naar de oorsprong toe beweegt. De snelheid "
                 "is dan negatief, niet de positie.",
                 None, None,
             ]),
        dict(aanpak="Twee grafieken, twee betekenissen: in een x(t)-grafiek lees je de snelheid uit de "
                    "steilheid, in een v(t)-grafiek de verplaatsing uit de oppervlakte.",
             waarom=[
                 None, None, None, None,
                 "Een oppervlakte onder de tijdas telt negatief, dus is de verplaatsing hier \\(-20\\) m. "
                 "Het voorwerp is dus twintig meter achteruitgegaan.",
             ]),
        dict(aanpak="Elke uitspraak gaat over één eigenschap van een ERB. Vraag je af of je het uit de "
                    "grafiek of uit de formule kan nagaan.",
             waarom=[
                 None,
                 "Een afgelegde weg telt elke meter mee, welke kant je ook op gaat. Enkel de verplaatsing "
                 "kan negatief zijn.",
                 "Een v(t)-grafiek zegt enkel hoe snel het voorwerp gaat, niet waar het vertrok. Twee "
                 "voorwerpen met een heel andere beginpositie hebben dezelfde v(t)-grafiek.",
                 None,
             ]),
        dict(aanpak="Werk met de nadersnelheid: dezelfde zin geeft het verschil, naar elkaar toe de som. "
                    "Reken daarna de afstand gedeeld door die snelheid.",
             waarom=[
                 "Let op de voorsprong: de wandelaar is al een uur onderweg, dus reken je eerst uit "
                 "hoeveel kilometer dat is.",
                 None,
                 "Deze gedachte spaart je het opstellen van twee positiefuncties. Werkt een vraagstuk niet, "
                 "dan kan je altijd nog terugvallen op de twee functies gelijkstellen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-versnelde-beweging-vrije-val-en-verticale-worp-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Versnelling is de verandering van de snelheid per seconde: a = Δv : Δt. Wordt de "
                    "snelheid kleiner, dan is Δv negatief en dus ook a.",
             waarom=[
                 None,
                 "De laatste is leerrijk: een snelheid die niet verandert geeft een versnelling van nul, "
                 "ook al beweegt het voorwerp wel degelijk.",
             ]),
        dict(aanpak="Kijk naar de v(t)-grafiek: horizontaal is ERB, stijgend is versneld, dalend is "
                    "vertraagd. Een x(t)-grafiek die vlakker wordt, hoort bij een snelheid die daalt.",
             waarom=[
                 None, None, None,
                 "Hier moet je de twee samen lezen: een negatieve versnelling bij een positieve snelheid "
                 "vertraagt. Het teken van a alleen zegt het niet.",
             ]),
        dict(aanpak="Een vrije val is een eenparig versnelde beweging met a = g. Elke seconde komt er "
                    "\\(9{,}81\\) m/s bij, ongeacht de massa.",
             waarom=[
                 None, None,
                 "Op het hoogste punt is de snelheid nul, maar de versnelling niet. Dat is de vraag die "
                 "hierover het vaakst fout gaat.",
                 "Je rekent \\(20 : 9{,}81\\), dus ongeveer twee seconden. Naar beneden duurt het weer even "
                 "lang.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen snelheid en versnelling. Het zijn twee "
                    "verschillende grootheden die onafhankelijk van elkaar nul kunnen zijn.",
             waarom=[
                 "Een negatieve versnelling vertraagt enkel een voorwerp dat vooruit gaat. Beweegt het al "
                 "in de negatieve zin, dan gaat het juist sneller.",
                 None,
                 "De snelheid groeit elke seconde, dus leg je elke seconde méér weg af. De afgelegde weg "
                 "groeit met het kwadraat van de tijd.",
                 None,
                 "De zwaartekracht wijst heel de worp door naar beneden, dus blijft de versnelling "
                 "dezelfde. Enkel de zin van de snelheid keert om.",
             ]),
        dict(aanpak="Antwoord met de krachten of met de twee grootheden apart. Een goede uitleg zegt wat er "
                    "gelijk blijft en wat er verandert.",
             waarom=[
                 None, None,
                 "De fout zit in het verwarren van snelheid met kracht. Zonder snelheid kan er nog altijd "
                 "een kracht en dus een versnelling zijn.",
                 "De sleutel is de verhouding van luchtweerstand tot gewicht, niet de massa zelf. In vacuüm "
                 "valt een pluim even snel als een steen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-krachten-krachtenbalans-en-zwaartekracht-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Liggen twee krachten op dezelfde rechte, dan tel je op bij dezelfde zin en trek je af "
                    "bij tegengestelde zin. Zeg er altijd bij welke kant de resultante op wijst.",
             waarom=[
                 "Bij twee gelijke en tegengestelde krachten is de resultante nul. Dat is precies de "
                 "voorwaarde voor evenwicht.",
                 None,
             ]),
        dict(aanpak="De zwaartekracht is massa maal g. Zoek je de massa, dan deel je de kracht door g.",
             waarom=[
                 None, None,
                 "Dezelfde massa, een andere g, dus een andere kracht. De massa zelf verandert niet door "
                 "van plaats te veranderen.",
             ]),
        dict(aanpak="De veerkracht is k maal de uitrekking, met Δl in meter. Een veerconstante in newton "
                    "per meter zegt hoeveel newton je nodig hebt voor één meter uitrekking.",
             waarom=[
                 "Vijf centimeter is \\(0{,}05\\) m, dus \\(20 : 0{,}05 = 400\\) N/m. Vergeet je de "
                 "omrekening, dan zit je er honderd keer naast.",
                 None,
                 "Een stijvere veer rekt minder uit bij dezelfde kracht. Een grote k betekent dus een "
                 "harde veer, niet een lange uitrekking.",
             ]),
        dict(aanpak="De wrijvingskracht is de coëfficiënt maal de normaalkracht. Op een horizontale vloer "
                    "is die normaalkracht gelijk aan de zwaartekracht, dus reken je eerst m maal g.",
             waarom=[
                 None, None,
                 "De coëfficiënt is een verhouding van twee krachten, dus vallen de newtons weg. Daarom "
                 "staat er nooit een eenheid bij.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen massa en kracht, en tussen snelheid en "
                    "versnelling.",
             waarom=[
                 "Enkel het gewicht wordt kleiner, want g is er kleiner. Je massa neem je overal mee.",
                 None,
                 "Bij een ring of een hoefijzer ligt het zwaartepunt in de lege ruimte ernaast. Het is een "
                 "rekenpunt, geen stukje materie.",
                 "In de formule staat de massa niet; die zit al in de normaalkracht. De coëfficiënt hangt "
                 "enkel af van welke twee materialen over elkaar schuiven.",
             ]),
        dict(aanpak="Noem bij elke uitleg de krachten met hun naam, zeg waar ze op aangrijpen en welke kant "
                    "ze op wijzen. Zeg daarna wat de resultante doet.",
             waarom=[
                 None,
                 "Die twee krachten zijn even groot, maar het zijn geen reactiekrachten van elkaar: ze "
                 "grijpen allebei op het boek aan. De reactie op de normaalkracht is de kracht van het boek "
                 "op de tafel.",
                 "Hier zit het mooie detail: trekken onder een hoek vermindert de wrijving. Een slee "
                 "optillen helpt dus ook al trek je hem daarmee niet vooruit.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-archimedeskracht-moment-en-evenwicht-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De archimedeskracht hangt enkel af van het weggeduwde volume, niet van het voorwerp "
                    "zelf. Voor water is \\(\\rho \\cdot g\\) ongeveer \\(9810\\) N per kubieke meter.",
             waarom=[
                 None,
                 "Drijft het voorwerp maar half, dan reken je met de helft van het volume. Enkel het deel "
                 "onder water duwt water weg.",
                 "Dit is de tweede manier om \\(F_{A}\\) te vinden: het schijnbare gewichtsverlies. Beide "
                 "wegen moeten hetzelfde getal geven.",
             ]),
        dict(aanpak="Vergelijk de massadichtheid van het voorwerp met die van de vloeistof. Groter betekent "
                    "zinken, gelijk zweven, kleiner drijven.",
             waarom=[
                 None,
                 "IJs is net iets lichter dan water, en daarom drijft het. Zonder dat kleine verschil zou "
                 "een vijver van onderaf dichtvriezen.",
             ]),
        dict(aanpak="Een moment is kracht maal arm maal de sinus van de hoek. Staat de kracht loodrecht, "
                    "dan is de sinus één en valt hij weg.",
             waarom=[
                 "Bij \\(30^{\\circ}\\) is de sinus \\(0{,}5\\), dus blijft er van \\(80 \\cdot 0{,}50\\) "
                 "maar de helft over: \\(20\\) Nm.",
                 None, None,
                 "Gaat de kracht door het draaipunt, dan is de arm nul. Duwen op de scharnierkant van een "
                 "deur doet ze dus niet opengaan.",
             ]),
        dict(aanpak="Een wip is in evenwicht als het moment links gelijk is aan het moment rechts. Je mag "
                    "met de massa's rekenen, want g staat aan beide kanten.",
             waarom=[
                 "Reken \\(20 \\cdot 1{,}5 = 30\\), dus \\(30 : 30 = 1{,}0\\) m. De zwaarste moet altijd "
                 "dichter bij het draaipunt.",
                 None, None,
             ]),
        dict(aanpak="Let op het onderscheid tussen een kracht en een moment, en op wat er wel en niet van "
                    "de diepte afhangt.",
             waarom=[
                 "De archimedeskracht hangt enkel af van het weggeduwde volume, dus blijft ze onderaan even "
                 "groot. De druk in de vloeistof stijgt wel met de diepte.",
                 None,
                 "Een moment staat in newtonmeter. Joule is dezelfde combinatie van eenheden, maar hoort "
                 "bij arbeid en energie, en dat is een andere grootheid.",
                 "Dat is net waarom er twee voorwaarden zijn. Twee tegengestelde krachten op een andere "
                 "plaats laten het voorwerp draaien zonder het te verplaatsen.",
             ]),
        dict(aanpak="Werk in je uitleg telkens met de twee krachten of met de twee evenwichten. Zeg wat "
                    "gelijk blijft en wat verandert.",
             waarom=[
                 None,
                 "Let op wat er niet verandert: het volume en dus de archimedeskracht. Enkel de massa "
                 "verandert, en dat volstaat om te zinken.",
                 None,
                 "Dit verklaart ook waarom een rallywagen laag ligt en een verhuiswagen traag door een "
                 "bocht moet. Stabiliteit is een zaak van zwaartepunt en steunvlak.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-druk-bij-vaste-stoffen-en-in-vloeistoffen-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Druk is kracht per oppervlakte: p = F : A. Zorg dat A in vierkante meter staat, anders "
                    "klopt je pascal niet.",
             waarom=[
                 None,
                 "Reken eerst de oppervlakte uit: \\(0{,}30 \\cdot 0{,}30 = 0{,}09\\,\\text{m}^{2}\\). Dat "
                 "is de stap die hier vaak vergeten wordt.",
                 None, None,
             ]),
        dict(aanpak="Leg de drie eenheden naast elkaar: \\(1\\) bar is \\(100\\,000\\) Pa, \\(1\\) hPa is "
                    "\\(100\\) Pa, \\(1\\) kPa is \\(1000\\) Pa.",
             waarom=[
                 "De normale luchtdruk van \\(1013\\) hPa is dus ongeveer \\(1\\) bar. Dat is een handig "
                 "houvast bij elke drukvraag.",
                 None,
             ]),
        dict(aanpak="De hydrostatische druk is \\(\\rho \\cdot g \\cdot h\\) en hangt enkel af van de "
                    "diepte en de vloeistof, niet van de vorm van het vat.",
             waarom=[
                 "Tien meter water geeft ongeveer \\(1\\) bar. Daarmee kan je elke diepte in je hoofd "
                 "schatten.",
                 None,
                 "Een manometer meet de óverdruk, dus boven op de luchtdruk van ongeveer \\(1\\) bar. "
                 "Daarom staat er bij een autopneu altijd overdruk bedoeld.",
             ]),
        dict(aanpak="In p = F : A staat de oppervlakte in de noemer. Wil je veel druk, maak het oppervlak "
                    "klein; wil je weinig druk, maak het groot.",
             waarom=[None, None]),
        dict(aanpak="Let op het verschil tussen druk en kracht, en op de richting waarin druk werkt.",
             waarom=[
                 "Druk werkt in alle richtingen even hard, dus heeft ze geen zin en is ze een scalair. De "
                 "kracht die ze op een wand uitoefent, is wel een vector.",
                 None,
                 "Enkel de diepte telt, niet de hoeveelheid water. Dat is de hydrostatische paradox.",
                 "Hoger betekent minder lucht boven je, dus een lagere druk. Daarom koken aardappelen in de "
                 "bergen trager.",
                 "Een pers vergroot de kracht, niet de energie. De grote zuiger komt even veel minder ver, "
                 "dus blijft de arbeid gelijk.",
             ]),
        dict(aanpak="Zeg in je uitleg welke grootheid gelijk blijft en welke verandert, en noem de formule "
                    "waarin dat zichtbaar wordt.",
             waarom=[
                 None, None,
                 "Dit is de kern van elke hefboom of pers: je wint kracht en verliest weg. Energie maak je "
                 "nooit bij.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-gassen-temperatuur-en-de-gaswetten-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Van Celsius naar kelvin tel je \\(273\\) op, omgekeerd trek je \\(273\\) af. In de "
                    "gaswetten reken je altijd in kelvin.",
             waarom=[
                 None,
                 "Onder \\(0\\) K kan je niet gaan, want \\(0\\) K is het absolute nulpunt. Daarom bestaan "
                 "er geen negatieve kelvins.",
             ]),
        dict(aanpak="De naam van het proces zegt welke grootheid gelijk blijft: iso-therm de temperatuur, "
                    "iso-baar de druk, iso-choor het volume. De wet volgt uit wat er dan nog kan veranderen.",
             waarom=[None, None, None]),
        dict(aanpak="Zet de gegevens in twee kolommen, voor en na, en gebruik de wet waarin de gelijke "
                    "grootheid wegvalt. Weet je er drie van de vier, dan vind je de vierde.",
             waarom=[
                 "Isotherm betekent dat het product gelijk blijft: halveert het volume, dan verdubbelt de "
                 "druk.",
                 None,
                 "Hier verandert er niets gelijk, dus gebruik je de algemene wet \\(pV/T\\) = constant. "
                 "Volume en druk gaan beide maal drie en maal twee, dus ook T.",
             ]),
        dict(aanpak="Een omgekeerd evenredig verband geeft een dalende kromme, een recht evenredig verband "
                    "een rechte door de oorsprong. Daarom is de kelvin zo handig.",
             waarom=[
                 None, None,
                 "Juist die twee rechten gaan door de oorsprong omdat de kelvin bij het absolute nulpunt "
                 "begint. In graden Celsius zou de rechte de as elders snijden.",
             ]),
        dict(aanpak="Kijk bij elke uitspraak welke grootheid er bedoeld wordt en of ze een nulpunt heeft "
                    "dat echt nul betekent.",
             waarom=[
                 "In een verhouding mag je geen Celsius invullen, want \\(0^{\\circ}\\text{C}\\) is niet "
                 "nul graden warmte. Dat is de fout die hier het vaakst gemaakt wordt.",
                 "Een verschil is in beide schalen hetzelfde getal, want de graden zijn even groot. Enkel "
                 "het nulpunt ligt anders.",
                 "R is voor alle ideale gassen \\(8{,}31\\) J/(mol.K). Dat is net wat ideaal betekent.",
                 None,
                 "Meer deeltjes in hetzelfde vat betekent meer botsingen tegen de wand en dus meer druk. "
                 "Daarom staat n in de ideale gaswet.",
             ]),
        dict(aanpak="Vertaal elke vraag naar deeltjes: hoe snel ze bewegen, hoe vaak ze botsen en hoe hard. "
                    "Noem daarna de wet die het in formulevorm zegt.",
             waarom=[
                 None, None,
                 "Stilstaande deeltjes is de ondergrens van het model. Daarom is \\(0\\) K niet gewoon "
                 "koud maar echt het laagste punt.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-arbeid-energie-vermogen-en-rendement-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk naar de hoek tussen de kracht en de verplaatsing: dezelfde zin geeft positieve "
                    "arbeid, tegengestelde zin negatieve, en loodrecht geen arbeid.",
             waarom=[
                 None, None,
                 "De normaalkracht staat loodrecht op de beweging, dus verricht ze nooit arbeid op een "
                 "vlakke vloer.",
                 "De zwaartekracht wijst naar beneden en de verplaatsing naar boven, dus is haar arbeid "
                 "negatief. De potentiële energie neemt juist daardoor toe.",
             ]),
        dict(aanpak="Arbeid is kracht maal weg maal de cosinus van de hoek. Staat de kracht in de zin van "
                    "de beweging, dan is de cosinus één.",
             waarom=[
                 "Bij \\(60^{\\circ}\\) is de cosinus \\(0{,}5\\), dus blijft er van \\(100 \\cdot 3{,}0\\) "
                 "de helft over.",
                 None,
                 "De cosinus van \\(90^{\\circ}\\) is nul, dus is de arbeid nul hoe groot de kracht ook is.",
             ]),
        dict(aanpak="Drie formules, elk met hun eigen afhankelijkheid: \\(E_{k}\\) met het kwadraat van de "
                    "snelheid, \\(E_{p,gr}\\) met de hoogte, \\(E_{p,el}\\) met het kwadraat van de "
                    "indrukking.",
             waarom=[
                 "Let op het kwadraat: \\(1000\\) kg aan \\(30\\) m/s geeft \\(450\\) kJ. Snelheid weegt "
                 "veel zwaarder door dan massa.",
                 None,
                 "Voor een veer geldt \\(E_{p,el} = k \\cdot \\Delta l^{2} / 2\\), dus \\(400 \\cdot "
                 "0{,}01 : 2 = 2{,}0\\) J.",
             ]),
        dict(aanpak="Vermogen is energie per seconde, rendement is nuttige energie gedeeld door de "
                    "toegevoerde. Een rendement zet je om in procent.",
             waarom=[
                 None,
                 "Bij de tweede moet je eerst de nuttige energie vinden: \\(500 - 400 = 100\\) J, dus "
                 "\\(20\\,\\%\\). Wat niet nuttig is, is verlies.",
                 None,
             ]),
        dict(aanpak="Zeg bij een omzetting telkens van welke vorm naar welke. Vaak zijn er meerdere "
                    "tegelijk, en dan is het verlies de warmte.",
             waarom=[None, None]),
        dict(aanpak="Let op het verschil tussen energie en vermogen, en op de kwadraten in de formules.",
             waarom=[
                 "Vier keer, niet twee keer, want de snelheid staat in het kwadraat. Dat is de belangrijkste "
                 "formule van heel dit hoofdstuk.",
                 "Een kilowattuur is een vermogen maal een tijd, dus een energie. Daarom staat het op je "
                 "elektriciteitsfactuur.",
                 None, None,
             ]),
        dict(aanpak="Noem in je uitleg de formule waarin je het ziet, en zeg welke grootheid gelijk blijft.",
             waarom=[
                 None, None,
                 "Dit is de reden achter elke snelheidscampagne. Tien kilometer per uur sneller betekent "
                 "niet een beetje maar veel meer energie om kwijt te raken.",
                 "Hetzelfde verschijnsel is de ene keer het doel en de andere keer verlies. Dat onderscheid "
                 "maakt de toepassing, niet de fysica.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-warmte-faseovergangen-en-de-warmtebalans-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zes namen op een rij: smelten en stollen, verdampen en condenseren, sublimeren en "
                    "desublimeren. Ga je naar een lossere fase, dan is er warmte nodig; omgekeerd komt ze vrij.",
             waarom=[
                 None,
                 "Sublimeren zie je bij droogijs en bij rijp dat verdwijnt zonder te smelten. Desublimeren "
                 "is net het ontstaan van die rijp.",
             ]),
        dict(aanpak="Drie manieren: geleiding door een vaste stof, convectie door een stromende vloeistof "
                    "of gas, straling zonder tussenstof.",
             waarom=[
                 "Straling is de enige die door het vacuüm van de ruimte kan. Daarom is dat hier het "
                 "antwoord.",
                 None,
             ]),
        dict(aanpak="Merkbare warmte is \\(c \\cdot m \\cdot \\Delta T\\): de temperatuur verandert wel. "
                    "Voor water is c \\(4186\\) J per kilogram per kelvin.",
             waarom=[
                 None, None,
                 "De warmtecapaciteit C is al c maal m, dus hoef je de massa niet meer te kennen: "
                 "\\(800 \\cdot 15 = 12\\) kJ.",
             ]),
        dict(aanpak="Latente warmte is \\(l \\cdot m\\), zonder temperatuurverschil: hier verandert de fase "
                    "en niet de temperatuur.",
             waarom=[
                 "Vergelijk de twee getallen: één kilogram water verdampen kost \\(2260\\) kJ, veel meer "
                 "dan ijs smelten. Daarom is stoom zo gevaarlijk.",
                 None,
             ]),
        dict(aanpak="In een geïsoleerd vat geldt dat de warmte die het ene water afgeeft gelijk is aan wat "
                    "het andere opneemt. Bij gelijke massa's ligt de eindtemperatuur juist in het midden.",
             waarom=[
                 None,
                 "Hier zijn de massa's niet gelijk, dus ligt de eindtemperatuur dichter bij de grootste "
                 "massa. Reken met de verhouding van de massa's.",
             ]),
        dict(aanpak="Let op het verschil tussen temperatuur en warmte, en tussen opwarmen en een "
                    "faseovergang.",
             waarom=[
                 None,
                 "Water verdampt bij elke temperatuur aan het oppervlak, maar kóókt pas bij "
                 "\\(100^{\\circ}\\text{C}\\). Daarom droogt de was ook in de winter.",
                 "Een kleine c betekent dat er weinig warmte nodig is per kelvin, dus warmt de stof juist "
                 "snel op. Een metalen pan is zo.",
                 None,
                 "Temperatuur en hoeveelheid warmte zijn twee verschillende dingen. Een bad van "
                 "\\(40^{\\circ}\\text{C}\\) bevat veel meer warmte dan een vlam, maar is niet warmer.",
             ]),
        dict(aanpak="Vertaal elke vraag naar de deeltjes: hun gemiddelde snelheid is de temperatuur, hun "
                    "onderlinge verband de potentiële energie.",
             waarom=[
                 None,
                 "Dit is een goed voorbeeld van hoe je gevoel je bedriegt: je voelt hoe snel warmte "
                 "wegstroomt, niet de temperatuur zelf.",
                 None,
                 "Dezelfde grote c van water verklaart ook waarom de kust een zachter klimaat heeft dan het "
                 "binnenland.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-elektrische-stroom-spanning-en-weerstand-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Eén formule in drie gedaanten: R = U : I, I = U : R en U = R · I. Schrijf telkens op "
                    "wat je kent en wat je zoekt.",
             waarom=[None, None]),
        dict(aanpak="In serie tel je de weerstanden gewoon op. Parallel tel je de omgekeerden op, en het "
                    "resultaat is altijd kleiner dan de kleinste weerstand.",
             waarom=[
                 "Bij \\(20\\) en \\(40\\) parallel reken je \\(1/20 + 1/40 = 3/40\\), dus \\(40/3 = "
                 "13{,}3\\ \\Omega\\). Twee gelijke weerstanden parallel geven altijd precies de helft.",
                 "Drie gelijke weerstanden parallel geven een derde: \\(90 : 3 = 30\\ \\Omega\\). Dat is een "
                 "snelle controle op je rekenwerk.",
                 "Werk van binnen naar buiten: eerst de twee parallel tot \\(5{,}0\\ \\Omega\\), dan de "
                 "serie erbij. Zo pak je elke samengestelde schakeling aan.",
             ]),
        dict(aanpak="Werk in stappen: eerst de substitutieweerstand, dan de stroom uit de bron, dan per "
                    "weerstand de spanning. In serie is de stroom overal gelijk, parallel de spanning.",
             waarom=[
                 None,
                 "Over de grootste weerstand staat de grootste spanning: \\(60 \\cdot 0{,}20 = 12\\) V. "
                 "Samen met de \\(6\\) V over de andere is dat de \\(18\\) V van de bron.",
                 "Elke lamp trekt \\(2{,}3\\) A, dus samen \\(4{,}6\\) A. Parallel tel je de stromen op.",
                 "Vermogen is spanning maal stroom. Daarmee kan je nagaan of een kring een zekering van "
                 "\\(16\\) A aankan.",
             ]),
        dict(aanpak="Een ampèremeter meet de stroom die er door gaat en staat dus in serie; een voltmeter "
                    "meet een verschil tussen twee punten en staat dus parallel.",
             waarom=[
                 None, None, None,
                 "Een zekering beschermt de leiding tegen een te grote stroom, dus tegen brand.",
                 "Een verliesstroomschakelaar beschermt de mens: loopt er stroom door een lichaam naar de "
                 "aarde, dan komt er minder terug dan er vertrok en slaat hij af.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen stroom, spanning en weerstand, en tussen "
                    "serie en parallel.",
             waarom=[
                 "De afgesproken stroomzin loopt van plus naar min, de elektronen juist omgekeerd. Dat is "
                 "een historische afspraak van voor men de elektronen kende.",
                 None, None,
                 "Een isolator laat de stroom net niet door, dus heeft hij een hele grote weerstand.",
                 "Stopcontacten staan parallel, elk op \\(230\\) V. Stonden ze in serie, dan zou één "
                 "uitgetrokken stekker heel het huis uitschakelen.",
             ]),
        dict(aanpak="Noem in je uitleg de weg die de stroom neemt en de formule waarin je het ziet. Bij een "
                    "veiligheidsvraag zeg je ook wat er beschermd wordt.",
             waarom=[
                 None, None,
                 "Dezelfde spanning, een veel kleinere weerstand, dus veel meer stroom. Het is de stroom "
                 "door je lichaam die gevaarlijk is, niet de spanning zelf.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-licht-weerkaatsing-breking-en-lenzen-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie woorden met een scherp onderscheid: doorzichtig laat het beeld door, "
                    "doorschijnend enkel het licht, ondoorschijnend niets.",
             waarom=[
                 None,
                 "Papier is doorschijnend: hou het voor een lamp en je ziet licht maar geen vorm. Dat is "
                 "precies het verschil met glas.",
             ]),
        dict(aanpak="De invalshoek en de weerkaatsingshoek zijn gelijk, en je meet ze altijd vanaf de "
                    "normaal, de loodlijn op het oppervlak.",
             waarom=[
                 None,
                 "Hier staat de hoek met het oppervlak gegeven, dus reken je \\(90 - 25 = 65^{\\circ}\\). "
                 "Dat is de klassieke valkuil van deze reeks.",
                 None, None, None,
             ]),
        dict(aanpak="Het beeld in een vlakke spiegel staat even ver achter de spiegel als het voorwerp "
                    "ervoor, is even groot en virtueel.",
             waarom=[
                 "Virtueel betekent dat de stralen daar niet echt samenkomen; ze lijken er enkel uit te "
                 "komen. Daarom kan je het niet op een scherm vangen.",
                 None,
                 "Je staat \\(1{,}5\\) m voor de spiegel en je beeld \\(1{,}5\\) m erachter, dus samen "
                 "\\(3{,}0\\) m. Daarom moet je scherpstellen op drie meter.",
                 None,
             ]),
        dict(aanpak="Schaduw ontstaat omdat licht rechtdoor gaat. Een kleine bron geeft enkel kernschaduw, "
                    "een grote bron ook een halfschaduw.",
             waarom=[
                 None, None, None,
                 "Hoe kleiner de bron, hoe smaller de halfschaduw. Daarom geeft een laserpunt een "
                 "vlijmscherpe schaduw en een bewolkte hemel bijna geen.",
             ]),
        dict(aanpak="Naar een dichtere stof buigt de straal naar de normaal toe, naar een ijlere stof van "
                    "de normaal weg. Loodrecht invallen geeft geen breking.",
             waarom=[
                 None, None,
                 "Bij loodrechte inval is er geen hoek om te veranderen. De straal gaat gewoon rechtdoor, "
                 "al wordt hij wel trager.",
             ]),
        dict(aanpak="Drie hoofdstralen: parallel gaat door het brandpunt, door het middelpunt gaat "
                    "rechtdoor, door het brandpunt gaat parallel verder. Met twee ervan vind je het beeld.",
             waarom=[
                 None, None,
                 "Dit is het geval van de loep: binnen het brandpunt wordt het beeld virtueel, "
                 "rechtopstaand en groter.",
                 "De vergrotingsfactor is de beeldgrootte gedeeld door de voorwerpgrootte, dus \\(6{,}0 : "
                 "2{,}0 = 3\\). Ze heeft geen eenheid.",
             ]),
        dict(aanpak="Zeg in je uitleg wat er met de stralen gebeurt en waar ze samenkomen of schijnen "
                    "samen te komen. Dat laatste bepaalt of het beeld reëel of virtueel is.",
             waarom=[
                 None,
                 "Dit is dezelfde breking als bij het geknikte potlood in een glas water. Je oog gaat er "
                 "altijd van uit dat licht rechtdoor kwam.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meten-en-onderzoek-fysica-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elke werkwijze af wat er in het slechtste geval stukgaat: het toestel, de "
                    "meting of jij.",
             waarom=[
                 "Op de weerstandsstand loopt er stroom uit het eigen batterijtje, dus is die leeg voor je "
                 "hem weer nodig hebt.",
                 None, None,
                 "Begin altijd op het grootste bereik en ga dan fijner. Een te klein bereik kan het "
                 "instrument beschadigen.",
                 None,
             ]),
        dict(aanpak="Zet bij elke grootheid het instrument. Let op het paar barometer en manometer: de ene "
                    "meet de luchtdruk, de andere een druk in een vat.",
             waarom=[None, None, None]),
        dict(aanpak="Nauwkeurig aflezen is vooral goed kijken: recht op de schaal, en bij een vloeistof "
                    "onderaan de meniscus.",
             waarom=[
                 None, None, None,
                 "Boven het maximum rekt de veer blijvend uit, en dan wijst het toestel voorgoed fout aan. "
                 "Dat heet overrekking.",
             ]),
        dict(aanpak="De zes stappen hebben een vaste orde: eerst het probleem, dan de vraag en de "
                    "hypothese, dan het plan, dan meten, dan besluiten, en ten slotte terugkijken.",
             waarom=[
                 None,
                 "De hypothese komt vóór het plan, want je plan moet net die hypothese kunnen toetsen.",
             ]),
        dict(aanpak="Loop de vijf criteria af: kan je er ja of nee op antwoorden (open), gaat ze over één "
                    "ding (enkelvoudig), zit er een oordeel in (objectief), kan jij ze uitvoeren "
                    "(haalbaar), en moet je ervoor meten of enkel opzoeken (onderzoekbaar).",
             waarom=[
                 None,
                 "Dit getal kan je opzoeken, dus is er niets te onderzoeken. Een onderzoeksvraag vraagt om "
                 "een meting of een verband.",
                 "Het woord beste legt een oordeel vast. Vervang het door iets wat je kan meten.",
                 "Niemand kan in de kern van de zon meten, dus is de vraag niet haalbaar in een schoollabo.",
                 "Hier zitten twee onderzoeken in één vraag. Splits ze, anders weet je achteraf niet "
                 "waardoor het verschil komt.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen een resultaat dat je niet verwachtte en "
                    "een fout in je werk.",
             waarom=[
                 None,
                 "Een meting weglaten omdat ze je niet past, is vervalsing. Een afwijkende meting mag je "
                 "enkel weglaten als je weet wat er misliep, en dan schrijf je dat op.",
                 None,
                 "Fijnere streepjes helpen niets als je waarde buiten het bereik valt. Meetbereik komt "
                 "eerst, nauwkeurigheid daarna.",
                 None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en noem telkens wat je gelijk houdt en wat je laat variëren.",
             waarom=[
                 "Dit is de kern van elk experiment: één variabele veranderen en de rest constant houden. "
                 "Anders kan je het verschil niet toeschrijven.",
                 None, None,
                 "Herhalen helpt enkel tegen toevallige fouten. Een systematische fout, zoals een "
                 "verkeerd genulde balans, blijft ook na honderd metingen bestaan.",
             ]),
    ],
)

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

REKEN = HOE + ["Reken met g = 9,81 N/kg, tenzij de opgave iets anders zegt."]

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
                 ("rij", [("weerstand", "ohm (Ω)"),
                          ("warmte", "joule (J)"),
                          ("absolute temperatuur", "kelvin (K)")], "SI-eenheid", WW),
                 ("rij", [("massadichtheid", "kg/m³"),
                          ("versnelling", "m/s²"),
                          ("moment van een kracht", "newtonmeter (Nm)")], "SI-eenheid", WW),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Schrijf de waarde als een macht van tien.",
             oefeningen=[
                 ("rij", [("mega", "10⁶"), ("hecto", "10²"), ("deci", "10⁻¹")], "Waarde", W),
                 ("rij", [("micro", "10⁻⁶"), ("nano", "10⁻⁹"), ("deca", "10¹")], "Waarde", W),
             ]),
        dict(kop="Reken om",
             opdracht="Reken om naar de eenheid die gevraagd wordt.",
             oefeningen=[
                 ("rij", [("3,2 km naar m", "3200 m"),
                          ("85 mm naar m", "0,085 m"),
                          ("0,75 ton naar kg", "750 kg")], "Antwoord", WW),
                 ("rij", [("250 L naar m³", "0,25 m³"),
                          ("54 km/h naar m/s", "15 m/s"),
                          ("12 m/s naar km/h", "43,2 km/h")], "Antwoord", WW),
                 ("rij", [("2,5 min naar s", "150 s"),
                          ("37 °C naar K", "310 K"),
                          ("150 K naar °C", "−123 °C")], "Antwoord", WW),
             ]),
        dict(kop="Wetenschappelijke notatie en beduidende cijfers",
             opdracht="Schrijf het getal in de wetenschappelijke notatie, of geef het aantal beduidende cijfers.",
             oefeningen=[
                 ("rij", [("0,0072 m", "7,2.10⁻³ m"),
                          ("154 000 N", "1,54.10⁵ N"),
                          ("0,000019 s", "1,9.10⁻⁵ s")], "Notatie", WW),
                 ("rij", [("0,0340 kg", "3 beduidende cijfers"),
                          ("12,50 m", "4 beduidende cijfers"),
                          ("7000 kg (zo geschreven)", "1 beduidend cijfer")], "Hoeveel?", WW),
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
                 ("kort", "Maak in p = F / A de kracht F vrij.", "F = p . A", W),
                 ("kort", "Maak in Fv = k . Δl de veerconstante k vrij.", "k = Fv / Δl", W),
                 ("open", "Een leerling berekent de massa van een fles water van 1,5 L en komt op 15 kg. "
                          "Leg uit hoe een schatting die fout meteen verraadt.",
                  "Water heeft een massadichtheid van 1000 kg/m³, dus weegt één liter ongeveer één kilogram. "
                  "Een fles van 1,5 L weegt dus ongeveer 1,5 kg; 15 kg is tien keer te veel, dus is er met een "
                  "factor tien iets misgegaan.", 4),
                 ("open", "Je wil een volume van 0,75 L afmeten. Je hebt een maatcilinder van 100 mL met "
                          "streepjes per 1 mL en een maatcilinder van 1 L met streepjes per 10 mL. "
                          "Welke kies je, en waarom?",
                  "De cilinder van 1 L: in die van 100 mL past 0,75 L niet, dus ligt de waarde buiten het "
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
                 ("kort", "Een loper loopt twee ronden van 400 m op een piste.",
                  "Δs = 800 m en Δx = 0 m", WL),
                 ("kort", "Iemand wandelt van x₀ = 15 m naar x = 70 m in de positieve zin.",
                  "Δs = 55 m en Δx = +55 m", WL),
                 ("kort", "Een fietser rijdt van x₀ = 90 m naar x = 40 m.",
                  "Δs = 50 m en Δx = −50 m", WL),
                 ("kort", "Iemand loopt 30 m vooruit en daarna 12 m terug.",
                  "Δs = 42 m en Δx = +18 m", WL),
             ]),
        dict(kop="Reken de snelheid",
             opdracht="Bereken met vg = Δx / Δt. Zet de eenheid bij je antwoord.",
             oefeningen=[
                 ("rij", [("240 km in 3,0 h", "80 km/h"),
                          ("90 m in 6,0 s", "15 m/s"),
                          ("45 km in een kwartier", "180 km/h")], "vg", WW),
                 ("rij", [("12 m/s gedurende 8,0 s", "96 m"),
                          ("20 m/s gedurende 2,0 min", "2400 m"),
                          ("5,0 m/s over 125 m", "25 s")], "Antwoord", WW),
             ]),
        dict(kop="De positiefunctie",
             opdracht="Lees uit de positiefunctie af wat gevraagd wordt. x in meter, t in seconde.",
             oefeningen=[
                 ("rij", [("x = 15 + 4.t, de beginpositie", "15 m"),
                          ("x = 15 + 4.t, de snelheid", "4 m/s"),
                          ("x = 60 − 6.t, de snelheid", "−6 m/s")], "Antwoord", WW),
                 ("kort", "Na hoeveel seconden is het voorwerp met x = 60 − 6.t in de oorsprong?",
                  "na 10 s", W),
                 ("kort", "Schrijf de positiefunctie van een voorwerp dat op 8 m vertrekt met 3 m/s in de positieve zin.",
                  "x = 8 + 3.t", WW),
             ]),
        dict(kop="Grafieken lezen",
             opdracht="Antwoord in één woord of één getal.",
             oefeningen=[
                 ("kort", "Wat stelt de steilheid van een x(t)-grafiek voor?", "de snelheid", WW),
                 ("kort", "Wat stelt de oppervlakte onder een v(t)-grafiek voor?", "de verplaatsing", WW),
                 ("kort", "Wat doet een voorwerp waarvan de x(t)-grafiek horizontaal loopt?", "het staat stil", WW),
                 ("kort", "Hoe ziet de v(t)-grafiek van een ERB eruit?", "een horizontale lijn", WW),
                 ("kort", "Een v(t)-lijn ligt op −5 m/s gedurende 4,0 s. Hoe groot is Δx?", "−20 m", W),
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
                 ("open", "Een wandelaar vertrekt om 8 uur met 4,0 km/h. Een fietser vertrekt om 9 uur op "
                          "dezelfde plaats met 16 km/h. Na hoeveel tijd haalt de fietser hem in?",
                  "Na één uur heeft de wandelaar 4,0 km voorsprong. De fietser loopt 16 − 4,0 = 12 km/h in, "
                  "dus duurt het 4,0 / 12 = 0,33 h, dus ongeveer 20 minuten.", 5),
                 ("open", "Twee treinen rijden naar elkaar toe, 180 km van elkaar, met 100 km/h en 80 km/h. "
                          "Na hoeveel tijd kruisen ze, en hoeveel kilometer heeft de snelste dan afgelegd?",
                  "Samen naderen ze met 100 + 80 = 180 km/h, dus kruisen ze na 1,0 h. De snelste heeft dan "
                  "100 km afgelegd.", 5),
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
             opdracht="Bereken met ag = Δv / Δt. Let op het teken.",
             oefeningen=[
                 ("rij", [("van 0 naar 15 m/s in 3,0 s", "5,0 m/s²"),
                          ("van 8,0 naar 20 m/s in 4,0 s", "3,0 m/s²"),
                          ("van 25 naar 5,0 m/s in 5,0 s", "−4,0 m/s²")], "ag", WW),
                 ("rij", [("van 12 naar 0 m/s in 6,0 s", "−2,0 m/s²"),
                          ("van 0 naar 30 m/s in 12 s", "2,5 m/s²"),
                          ("van 9,0 naar 9,0 m/s in 4,0 s", "0 m/s²")], "ag", WW),
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
             opdracht="Reken met g = 9,81 m/s². Rond af op twee beduidende cijfers.",
             oefeningen=[
                 ("rij", [("snelheid na 1,0 s", "9,8 m/s"),
                          ("snelheid na 2,5 s", "25 m/s"),
                          ("snelheid na 4,0 s", "39 m/s")], "v (vanuit rust)", WW),
                 ("kort", "Hoeveel m/s komt er bij een vrije val elke seconde bij de snelheid?", "9,81 m/s", W),
                 ("kort", "Hoe groot is de versnelling van een bal op het hoogste punt van een worp naar boven?",
                  "9,81 m/s², naar beneden", WW),
                 ("kort", "Je gooit een bal met 20 m/s recht omhoog. Na hoeveel tijd is hij op zijn hoogste punt?",
                  "ongeveer 2,0 s", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een negatieve versnelling betekent altijd dat het voorwerp vertraagt.", False),
                 ("waar", "Een voorwerp met een snelheid van nul kan toch een versnelling hebben.", True),
                 ("waar", "Bij een vrije val neemt de afgelegde weg elke seconde met evenveel toe.", False),
                 ("waar", "Zonder luchtweerstand vallen een kogel van 1 kg en een van 5 kg even snel.", True),
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
                  "versnelling er 9,81 m/s² naar beneden. Daarom valt de bal een ogenblik later ook weer.", 5),
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
                 ("rij", [("90 N en 60 N, dezelfde zin", "150 N"),
                          ("90 N en 60 N, tegengesteld", "30 N, zin van de 90 N"),
                          ("45 N en 45 N, tegengesteld", "0 N")], "Resultante", WL),
                 ("rij", [("200 N en 140 N, tegengesteld", "60 N, zin van de 200 N"),
                          ("35 N en 35 N, dezelfde zin", "70 N"),
                          ("120 N, 80 N en 50 N, alle drie dezelfde zin", "250 N")], "Resultante", WL),
             ]),
        dict(kop="De zwaartekracht",
             opdracht="Bereken met Fz = m . g en g = 9,81 N/kg. Rond af op drie beduidende cijfers.",
             oefeningen=[
                 ("rij", [("m = 3,0 kg", "29,4 N"),
                          ("m = 12 kg", "118 N"),
                          ("m = 0,50 kg", "4,91 N")], "Fz", WW),
                 ("kort", "Een voorwerp ondervindt een zwaartekracht van 98,1 N. Hoe groot is zijn massa?",
                  "10 kg", W),
                 ("kort", "Hoe groot is de zwaartekracht op 2,0 kg op de maan, met g = 1,62 N/kg?",
                  "3,24 N", W),
             ]),
        dict(kop="De veerkracht",
             opdracht="Bereken met Fv = k . Δl. Reken de lengteverandering eerst om naar meter.",
             oefeningen=[
                 ("rij", [("20 N rekt 5,0 cm uit", "k = 400 N/m"),
                          ("k = 150 N/m, F = 30 N", "Δl = 20 cm"),
                          ("k = 500 N/m, Δl = 3,0 cm", "F = 15 N")], "Antwoord", WW),
                 ("kort", "Een massa van 1,5 kg hangt aan een veer met k = 200 N/m. Hoeveel centimeter rekt ze uit?",
                  "ongeveer 7,4 cm", WW),
                 ("kort", "Twee veren krijgen dezelfde massa. Veer A rekt verder uit. Welke heeft de grootste k?",
                  "veer B", W),
             ]),
        dict(kop="De wrijvingskracht",
             opdracht="Bereken met Fw = μ . Fn. Op een horizontale vloer is Fn gelijk aan Fz.",
             oefeningen=[
                 ("rij", [("m = 10 kg, μ = 0,40", "39,2 N"),
                          ("m = 25 kg, μ = 0,20", "49,1 N"),
                          ("Fn = 500 N, μ = 0,30", "150 N")], "Fw", WW),
                 ("kort", "Fw = 60 N en Fn = 200 N. Hoe groot is μ?", "0,30", W),
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
    hoe=REKEN + ["De massadichtheid van water is 1000 kg/m³."],
    reeksen=[
        dict(kop="De archimedeskracht",
             opdracht="Bereken met FA = ρ . g . Vond. Het voorwerp zit volledig onder water.",
             oefeningen=[
                 ("rij", [("V = 0,0010 m³", "9,81 N"),
                          ("V = 0,0040 m³", "39,2 N"),
                          ("V = 0,010 m³", "98,1 N")], "FA", WW),
                 ("kort", "Een blok van 0,0060 m³ drijft met de helft onder water. Hoe groot is FA?",
                  "29,4 N", W),
                 ("kort", "Een steen weegt in de lucht 60 N en onder water 44 N. Hoe groot is FA?",
                  "16 N", W),
             ]),
        dict(kop="Zinken, zweven of drijven?",
             opdracht="Vergelijk met de massadichtheid van water en schrijf wat er gebeurt.",
             oefeningen=[
                 ("rij", [("ρ = 1300 kg/m³", "het zinkt"),
                          ("ρ = 1000 kg/m³", "het zweeft"),
                          ("ρ = 700 kg/m³", "het drijft")], "Wat gebeurt er?", WW),
                 ("rij", [("kurk, ρ = 240 kg/m³", "het drijft"),
                          ("ijzer, ρ = 7870 kg/m³", "het zinkt"),
                          ("ijs, ρ = 917 kg/m³", "het drijft")], "Wat gebeurt er?", WW),
             ]),
        dict(kop="Het moment van een kracht",
             opdracht="Bereken met M = F . d . sin α.",
             oefeningen=[
                 ("rij", [("50 N loodrecht op 0,40 m", "20 Nm"),
                          ("30 N loodrecht op 1,2 m", "36 Nm"),
                          ("80 N onder 30° op 0,50 m", "20 Nm")], "M", WW),
                 ("kort", "M = 48 Nm en de kracht staat loodrecht op een arm van 0,60 m. Hoe groot is F?",
                  "80 N", W),
                 ("kort", "Bij welke hoek tussen de kracht en de arm is het moment het grootst?", "90°", W),
                 ("kort", "Hoe groot is het moment van een kracht die door het draaipunt gaat?", "0 Nm", W),
             ]),
        dict(kop="De wip in evenwicht",
             opdracht="Gebruik de krachtmomentenbalans: links en rechts even grote momenten.",
             oefeningen=[
                 ("kort", "Links 20 kg op 1,5 m. Rechts 30 kg: op welke afstand?", "1,0 m", W),
                 ("kort", "Links 40 kg op 0,90 m. Rechts 24 kg: op welke afstand?", "1,5 m", W),
                 ("kort", "Links 25 kg op 1,2 m, rechts op 1,0 m. Welke massa rechts?", "30 kg", W),
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
                  "dan 1000 kg/m³. Het duwt zoveel water weg dat de archimedeskracht even groot wordt als zijn "
                  "zwaartekracht. Bij een bout is er geen lucht, dus is ρ veel groter dan die van water.", 6),
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
    hoe=REKEN + ["De massadichtheid van water is 1000 kg/m³ en de luchtdruk 1013 hPa."],
    reeksen=[
        dict(kop="Reken de druk",
             opdracht="Bereken met p = F / A.",
             oefeningen=[
                 ("rij", [("400 N op 0,20 m²", "2000 Pa"),
                          ("150 N op 0,050 m²", "3000 Pa"),
                          ("60 N op 0,0020 m²", "30 000 Pa")], "p", WW),
                 ("kort", "Een blok van 180 N staat op een vierkant van 0,30 m bij 0,30 m. Hoe groot is p?",
                  "2000 Pa", W),
                 ("kort", "p = 5000 Pa en A = 0,040 m². Hoe groot is F?", "200 N", W),
                 ("kort", "F = 300 N en p = 1500 Pa. Hoe groot is A?", "0,20 m²", W),
             ]),
        dict(kop="Eenheden van druk",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [("2 bar naar Pa", "200 000 Pa"),
                          ("1013 hPa naar Pa", "101 300 Pa"),
                          ("4500 Pa naar kPa", "4,5 kPa")], "Antwoord", WW),
                 ("rij", [("1 mbar naar Pa", "100 Pa"),
                          ("0,50 bar naar hPa", "500 hPa"),
                          ("25 kPa naar Pa", "25 000 Pa")], "Antwoord", WW),
             ]),
        dict(kop="De hydrostatische druk",
             opdracht="Bereken met p = ρ . g . h. Rond af op twee beduidende cijfers.",
             oefeningen=[
                 ("rij", [("1,0 m diep in water", "9,8 kPa"),
                          ("4,0 m diep in water", "39 kPa"),
                          ("20 m diep in water", "200 kPa")], "p", WW),
                 ("kort", "Hoe groot is de hydrostatische druk 3,0 m diep in olie met ρ = 900 kg/m³?",
                  "ongeveer 26 kPa", WW),
                 ("kort", "Een manometer geeft 3 bar overdruk aan. Hoe groot is de totale druk ongeveer?",
                  "ongeveer 4 bar", WW),
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
                  "groter zooloppervlak, en in p = F / A staat A in de noemer, dus wordt de druk veel kleiner. "
                  "Een naaldhak heeft een piepklein oppervlak en dus een enorme druk.", 6),
                 ("open", "Leg uit waarom je je oren moet klaren als je duikt.",
                  "De hydrostatische druk op het trommelvlies groeit met de diepte, terwijl de druk in je oor "
                  "gelijk blijft. Klaren laat lucht door de buis van Eustachius, zodat de druk aan beide kanten "
                  "van het trommelvlies weer even groot is.", 5),
                 ("open", "Leg met het beginsel van Pascal uit hoe een hydraulische pers met een kleine kracht "
                          "een grote kracht kan leveren, en waarom dat geen energie bijmaakt.",
                  "Een drukverandering plant zich in heel de vloeistof voort, dus is de druk bij beide zuigers "
                  "gelijk. Uit F = p . A volgt dat de grotere zuiger een grotere kracht geeft. Maar die zuiger "
                  "komt even veel minder ver, dus blijft de arbeid F . Δx dezelfde.", 6),
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
    hoe=HOE + ["Vul de temperatuur in de gaswetten altijd in kelvin in. R = 8,31 J/(mol.K)."],
    reeksen=[
        dict(kop="Celsius en kelvin",
             opdracht="Reken om met T = θ + 273,15. Rond af op een eenheid.",
             oefeningen=[
                 ("rij", [("20 °C naar K", "293 K"),
                          ("−40 °C naar K", "233 K"),
                          ("100 °C naar K", "373 K")], "Antwoord", WW),
                 ("rij", [("350 K naar °C", "77 °C"),
                          ("273 K naar °C", "0 °C"),
                          ("0 K naar °C", "−273 °C")], "Antwoord", WW),
             ]),
        dict(kop="Welk proces?",
             opdracht="Schrijf isotherm, isobaar of isochoor, en de wet die erbij hoort.",
             oefeningen=[
                 ("kort", "De temperatuur blijft gelijk.", "isotherm, p . V = constant", WL),
                 ("kort", "De druk blijft gelijk.", "isobaar, V / T = constant", WL),
                 ("kort", "Het volume blijft gelijk.", "isochoor, p / T = constant", WL),
             ]),
        dict(kop="Reken met de gaswetten",
             opdracht="Zoek de ontbrekende waarde. De stofhoeveelheid blijft gelijk.",
             oefeningen=[
                 ("rij", [("6,0 L bij 1,0 bar naar 2,0 L, isotherm", "3,0 bar"),
                          ("2,0 L bij 3,0 bar naar 1,0 bar, isotherm", "6,0 L"),
                          ("8,0 L bij 2,0 bar naar 4,0 bar, isotherm", "4,0 L")], "Antwoord", WW),
                 ("rij", [("3,0 L bij 300 K naar 600 K, isobaar", "6,0 L"),
                          ("5,0 L bij 400 K naar 200 K, isobaar", "2,5 L"),
                          ("2,0 bar bij 250 K naar 500 K, isochoor", "4,0 bar")], "Antwoord", WW),
                 ("kort", "Een gas van 1,0 L bij 2,0 bar en 300 K gaat naar 2,0 L bij 3,0 bar. Wat is de nieuwe T?",
                  "900 K", WW),
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
                 ("waar", "Een temperatuursverschil van 15 °C is hetzelfde als een verschil van 15 K.", True),
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
                  "grotere druk. Het volume blijft gelijk, dus geldt p / T = constant.", 6),
                 ("open", "Leg uit waarom een spuitbus niet in de zon mag liggen.",
                  "Het volume van de bus staat vast, dus geldt p / T = constant: wordt de bus warmer, dan "
                  "stijgt de druk mee. Boven een bepaalde druk kan de bus barsten. Daarom staat er dat ze niet "
                  "boven 50 °C mag komen.", 5),
                 ("open", "Leg uit wat het absolute nulpunt betekent voor de deeltjes van een ideaal gas, en "
                          "waarom het niet lager kan.",
                  "Bij 0 K staan de deeltjes in het model stil: hun kinetische energie is nul, dus zijn ook de "
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
             opdracht="Bereken met W = F . Δx . cos α.",
             oefeningen=[
                 ("rij", [("60 N over 5,0 m, in de zin", "300 J"),
                          ("40 N over 12 m, in de zin", "480 J"),
                          ("100 N over 3,0 m, onder 60°", "150 J")], "W", WW),
                 ("kort", "W = 250 J over 10 m in de zin van de beweging. Hoe groot is F?", "25 N", W),
                 ("kort", "Hoeveel arbeid verricht een kracht van 80 N die loodrecht op de verplaatsing staat?",
                  "0 J", W),
             ]),
        dict(kop="Kinetische en potentiële energie",
             opdracht="Bereken met Ek = m . v² / 2 en Ep,gr = m . g . h.",
             oefeningen=[
                 ("rij", [("m = 2,0 kg, v = 10 m/s", "100 J"),
                          ("m = 1000 kg, v = 30 m/s", "450 kJ"),
                          ("m = 0,50 kg, v = 4,0 m/s", "4,0 J")], "Ek", WW),
                 ("rij", [("m = 4,0 kg, h = 2,5 m", "98,1 J"),
                          ("m = 70 kg, h = 10 m", "6,87 kJ"),
                          ("m = 0,20 kg, h = 1,5 m", "2,94 J")], "Ep,gr", WW),
                 ("kort", "Een veer met k = 400 N/m is 0,10 m ingedrukt. Hoe groot is Ep,el?", "2,0 J", W),
             ]),
        dict(kop="Vermogen en rendement",
             opdracht="Bereken met P = |ΔE| / Δt en η = Enuttig / Etotaal.",
             oefeningen=[
                 ("rij", [("36 kJ in 30 s", "1,2 kW"),
                          ("600 J in 4,0 s", "150 W"),
                          ("2,0 kW gedurende 10 s", "20 kJ")], "Antwoord", WW),
                 ("rij", [("120 J in, 30 J nuttig", "25 %"),
                          ("500 J in, 400 J warmte", "20 %"),
                          ("80 J in, 60 J nuttig", "75 %")], "η", WW),
                 ("kort", "Een motor heeft een rendement van 40 % en krijgt 1500 J. Hoeveel nuttige energie levert hij?",
                  "600 J", W),
             ]),
        dict(kop="Welke omzetting?",
             opdracht="Schrijf van welke energievorm naar welke.",
             oefeningen=[
                 ("rij", [("een bal valt van een muur", "Ep,gr naar Ek"),
                          ("een ingedrukte veer schiet los", "Ep,el naar Ek"),
                          ("een waterkoker warmt water op", "elektrisch naar thermisch")], "Omzetting", WL),
                 ("rij", [("een batterij doet een lampje branden", "chemisch naar elektrisch en licht"),
                          ("een plant doet fotosynthese", "straling naar chemisch"),
                          ("een bal die je omhoog gooit", "Ek naar Ep,gr")], "Omzetting", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een auto die twee keer zo snel rijdt, heeft twee keer zoveel kinetische energie.", False),
                 ("waar", "Een kilowattuur is een eenheid van vermogen.", False),
                 ("waar", "Een rendement van meer dan 100 % kan niet bestaan.", True),
                 ("waar", "Een voorwerp dat stilstaat, kan toch potentiële energie hebben.", True),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met de juiste begrippen.",
             oefeningen=[
                 ("open", "Leg uit waarom je geen arbeid verricht op een doos die je horizontaal door een "
                          "kamer draagt, al voelt het zwaar aan.",
                  "De kracht waarmee je de doos omhoog houdt is verticaal, en de verplaatsing is horizontaal. "
                  "De hoek is dus 90° en cos 90° is nul, dus is W nul. Je spieren verbruiken wel energie, maar "
                  "dat is geen arbeid op de doos.", 5),
                 ("open", "Leg uit wat energiedissipatie is en waarom de energie daarbij niet verdwijnt.",
                  "Bij een omzetting gaat een deel van de bruikbare energie naar een minder bruikbare vorm, "
                  "meestal warmte. Die energie bestaat nog, maar is zo verspreid in de omgeving dat je ze niet "
                  "meer nuttig kan gebruiken. De wet van behoud van energie blijft dus gelden.", 5),
                 ("open", "Leg uit waarom een remweg bij een dubbele snelheid vier keer zo lang is.",
                  "In Ek = m . v² / 2 staat de snelheid in het kwadraat, dus heeft een auto bij een dubbele "
                  "snelheid vier keer zoveel kinetische energie. De remkracht moet die hele energie wegnemen "
                  "met W = F . Δx, dus is bij dezelfde remkracht een vier keer langere weg nodig.", 6),
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
    hoe=HOE + ["De specifieke warmtecapaciteit van water is 4186 J/(kg.K)."],
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
             opdracht="Bereken met Q = c . m . ΔT.",
             oefeningen=[
                 ("rij", [("1,0 kg water, 20 K", "83,7 kJ"),
                          ("0,50 kg water, 60 K", "126 kJ"),
                          ("3,0 kg water, 5,0 K", "62,8 kJ")], "Q", WW),
                 ("kort", "Een voorwerp van 2,0 kg met c = 450 J/(kg.K) krijgt 18 kJ. Hoeveel stijgt zijn T?",
                  "20 K", W),
                 ("kort", "Een voorwerp heeft C = 800 J/K en warmt 15 K op. Hoeveel warmte kostte dat?",
                  "12 kJ", W),
             ]),
        dict(kop="Reken de latente warmte",
             opdracht="Bereken met Q = l . m. De waarden staan bij de opgave.",
             oefeningen=[
                 ("rij", [("0,40 kg ijs smelten, ls = 334 kJ/kg", "134 kJ"),
                          ("1,0 kg water verdampen, lv = 2260 kJ/kg", "2260 kJ"),
                          ("0,25 kg lood smelten, ls = 24,5 kJ/kg", "6,1 kJ")], "Q", WW),
                 ("kort", "Hoeveel warmte komt vrij als 0,20 kg water van 100 °C condenseert, met lv = 2260 kJ/kg?",
                  "452 kJ", WW),
             ]),
        dict(kop="De warmtebalans",
             opdracht="Reken uit in een geïsoleerd vat.",
             oefeningen=[
                 ("kort", "0,20 kg water van 70 °C bij 0,20 kg water van 30 °C. Welke eindtemperatuur?",
                  "50 °C", W),
                 ("kort", "0,10 kg water van 90 °C bij 0,30 kg water van 10 °C. Welke eindtemperatuur?",
                  "30 °C", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Tijdens een faseovergang blijft de temperatuur van de stof gelijk.", True),
                 ("waar", "Water kan enkel verdampen bij 100 °C.", False),
                 ("waar", "Een stof met een kleine specifieke warmtecapaciteit warmt traag op.", False),
                 ("waar", "Twee voorwerpen in thermisch evenwicht hebben dezelfde temperatuur.", True),
                 ("waar", "Een groot voorwerp heeft altijd een hogere temperatuur dan een klein voorwerp.", False),
             ]),
        dict(kop="Leg uit",
             opdracht="Schrijf je uitleg met het deeltjesmodel.",
             oefeningen=[
                 ("open", "Leg uit waarom de temperatuur gelijk blijft terwijl ijs van 0 °C smelt.",
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
                  "Water heeft een grote specifieke warmtecapaciteit, 4186 J/(kg.K), dus is er veel warmte "
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
             opdracht="Bereken met R = U / I. Zet de eenheid bij je antwoord.",
             oefeningen=[
                 ("rij", [("U = 12 V, I = 0,40 A", "R = 30 Ω"),
                          ("U = 230 V, I = 2,0 A", "R = 115 Ω"),
                          ("U = 9,0 V, I = 0,30 A", "R = 30 Ω")], "Antwoord", WW),
                 ("rij", [("U = 6,0 V, R = 20 Ω", "I = 0,30 A"),
                          ("U = 230 V, R = 460 Ω", "I = 0,50 A"),
                          ("I = 0,25 A, R = 80 Ω", "U = 20 V")], "Antwoord", WW),
             ]),
        dict(kop="Serie of parallel?",
             opdracht="Bereken de substitutieweerstand.",
             oefeningen=[
                 ("rij", [("20 Ω en 40 Ω in serie", "60 Ω"),
                          ("20 Ω en 40 Ω parallel", "13,3 Ω"),
                          ("100 Ω en 100 Ω parallel", "50 Ω")], "Rs", WW),
                 ("rij", [("drie keer 90 Ω parallel", "30 Ω"),
                          ("10 Ω, 20 Ω en 30 Ω in serie", "60 Ω"),
                          ("12 Ω en 24 Ω parallel", "8,0 Ω")], "Rs", WW),
                 ("kort", "5,0 Ω in serie met twee keer 10 Ω parallel. Hoe groot is Rs?", "10 Ω", W),
             ]),
        dict(kop="Door de schakeling rekenen",
             opdracht="Reken stap voor stap uit.",
             oefeningen=[
                 ("kort", "Over 30 Ω en 60 Ω in serie staat 18 V. Hoe groot is I?", "0,20 A", W),
                 ("kort", "In diezelfde schakeling: hoe groot is de spanning over de 60 Ω?", "12 V", W),
                 ("kort", "Twee lampen van elk 100 Ω staan parallel op 230 V. Hoe groot is de totale stroom?",
                  "4,6 A", W),
                 ("kort", "Een toestel op 230 V trekt 1,5 A. Hoe groot is zijn vermogen?", "345 W", W),
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
                  "Bij een kortsluiting is de weerstand in de kring heel klein geworden. Uit I = U / R volgt "
                  "dan een heel grote stroom. Door het joule-effect worden de draden daardoor snel heet, met "
                  "brandgevaar.", 5),
                 ("open", "Leg uit waarom je een elektrisch toestel nooit met natte handen bedient.",
                  "Water verlaagt de weerstand van je huid sterk. Bij dezelfde spanning loopt er dan volgens "
                  "I = U / R veel meer stroom door je lichaam, en dat is net wat elektrocutie gevaarlijk maakt.", 5),
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
                 ("kort", "Een straal valt onder een invalshoek van 40°. Hoe groot is de weerkaatsingshoek?",
                  "40°", W),
                 ("kort", "Een straal valt onder 25° met het spiegeloppervlak. Hoe groot is de invalshoek?",
                  "65°", W),
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
                 ("kort", "Je staat 1,5 m voor een vlakke spiegel. Hoe ver staat je beeld van jou?", "3,0 m", W),
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
                 ("kort", "Een voorwerp is 2,0 cm groot en het beeld 6,0 cm. Hoe groot is de vergrotingsfactor?",
                  "3", W),
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
                 ("kort", "Een stroom van 2 A meten op het kleinste meetbereik.",
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
                 ("rij", [("een tijdsduur van 2 s", "chronometer"),
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
             opdracht="Zet deze zes stappen in de juiste volgorde: schrijf 1 bij de stap die eerst komt en 6 bij de laatste.",
             oefeningen=[
                 ("rij", [("data waarnemen en verzamelen", "4"),
                          ("de probleemstelling afbakenen", "1"),
                          ("een conclusie formuleren", "5")], "Cijfer", W),
                 ("rij", [("een onderzoeksplan opstellen", "3"),
                          ("een onderzoeksvraag en hypothese opstellen", "2"),
                          ("reflecteren over je methode", "6")], "Cijfer", W),
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

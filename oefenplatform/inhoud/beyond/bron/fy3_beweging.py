# -*- coding: utf-8 -*-
"""Rechtlijnige beweging: ERB en EVRB — 🌍 Beyond, fysica.

Deel 1 gaat over de eenparig rechtlijnige beweging en over het lezen van de
drie bewegingsgrafieken: wat de steilheid van een x(t)-grafiek betekent, wat
de oppervlakte onder een v(t)-grafiek voorstelt, en het verschil tussen
afgelegde weg en verplaatsing, en tussen gemiddelde en ogenblikkelijke
snelheid. Deel 2 gaat over de eenparig veranderlijke beweging: versnellen en
vertragen, de formules met en zonder beginsnelheid, de vrije val, de
verticale worp en inhaalproblemen.

De fiche vraagt om grafieken op te stellen; dat kan hier niet, dus vragen de
vragen naar het verloop van zo'n grafiek in woorden en naar wat je eruit
afleest.

De formules staan in gewone wiskundige notatie, tussen \\( en \\). Daarom
staan de teksten hier in rauwe strings: r"\\(v = v_{0} + a\\,t\\)".
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent een eenparig rechtlijnige beweging in formules?",
        opties=[
            r"\(\vec{v}\) blijft constant, dus \(a = 0\)",
            r"\(a\) blijft constant, dus \(\vec{v}\) groeit",
            r"\(x\) blijft constant, dus \(v = 0\)",
            r"\(v\) groeit met \(t^{2}\), dus \(a\) groeit",
        ],
        antwoord=0,
        uitleg=r"Met \(a = 0\) is ook \(\sum \vec{F} = \vec{0}\): dat is de eerste wet van "
        r"Newton. De plaats volgt dan \(x = x_{0} + v\,t\).",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de afkorting ERB?",
        antwoord=["eenparig rechtlijnige beweging", "eenparig rechtlijnig", "ERB"],
        uitleg=r"De snelheid blijft constant in grootte én in zin, dus \(x = x_{0} + v\,t\). "
        r"Verandert \(v\) gelijkmatig, dan heb je een EVRB met \(v = v_{0} + a\,t\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet de \(x(t)\)-grafiek van een ERB eruit?",
        opties=[
            "een rechte met een constante helling",
            "een rechte die evenwijdig met de tijdas loopt",
            "een parabool die steeds steiler wordt",
            "een kromme die naar een vaste waarde buigt",
        ],
        antwoord=0,
        uitleg=r"De helling is \(\dfrac{\Delta x}{\Delta t} = v\). Bij een EVRB krijg je de "
        r"parabool \(x = x_{0} + v_{0}\,t + \tfrac{1}{2}a\,t^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt \(\dfrac{\Delta x}{\Delta t}\) voor op een \(x(t)\)-grafiek?",
        opties=[
            r"\(v\), de snelheid op dat stuk",
            r"\(a\), de versnelling op dat stuk",
            r"\(s\), de afgelegde weg tot dan",
            r"\(F\), de kracht op het lichaam",
        ],
        antwoord=0,
        uitleg=r"Plaats per tijd is snelheid. Op een \(v(t)\)-grafiek geeft "
        r"\(\dfrac{\Delta v}{\Delta t}\) op dezelfde manier \(a\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt de oppervlakte onder een \(v(t)\)-grafiek voor?",
        opties=[
            r"de verplaatsing \(\Delta x\)",
            r"de versnelling \(a\)",
            r"de kracht \(F\)",
            r"de tijdsduur \(\Delta t\)",
        ],
        antwoord=0,
        uitleg=r"Snelheid maal tijd is afstand: \(\Delta x = v\,\Delta t\) voor elk smal "
        r"stukje. Ligt een stuk onder de as, dan telt het negatief mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Afgelegde weg en verplaatsing zijn altijd even groot.",
        antwoord=False,
        uitleg=r"De verplaatsing is \(\Delta x = x_{\text{eind}} - x_{\text{begin}}\); wie "
        r"heen en weer loopt, heeft \(\Delta x = 0\) maar wel een weg afgelegd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fietser rijdt \(4{,}5\) km naar het noorden en daarna \(1{,}5\) km terug. Hoe groot zijn de weg \(s\) en de verplaatsing \(\Delta x\)?",
        opties=[
            r"\(s = 6{,}0\) km en \(\Delta x = 3{,}0\) km",
            r"\(s = 3{,}0\) km en \(\Delta x = 6{,}0\) km",
            r"\(s = 6{,}0\) km en \(\Delta x = 6{,}0\) km",
            r"\(s = 4{,}5\) km en \(\Delta x = 1{,}5\) km",
        ],
        antwoord=0,
        uitleg=r"De weg telt elke meter mee: \(4{,}5 + 1{,}5 = 6{,}0\) km. De verplaatsing is "
        r"het verschil: \(4{,}5 - 1{,}5 = 3{,}0\) km naar het noorden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen \(v_{\text{gem}}\) en de ogenblikkelijke snelheid \(v\)?",
        opties=[
            r"\(v_{\text{gem}}\) geldt over een traject, \(v\) op één ogenblik",
            r"\(v_{\text{gem}}\) is altijd kleiner dan \(v\) op dat ogenblik",
            r"\(v_{\text{gem}}\) hoort bij een ERB en \(v\) bij een EVRB",
            r"\(v_{\text{gem}}\) staat in km/h en \(v\) in m/s",
        ],
        antwoord=0,
        uitleg=r"\(v_{\text{gem}} = \dfrac{\Delta x}{\Delta t}\) over het hele traject, "
        r"terwijl \(v\) die verhouding is voor een heel klein tijdsinterval. Dat is wat je "
        r"op een snelheidsmeter leest. Bij een ERB vallen de twee samen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel meter per seconde is \(108\) km/h?",
        antwoord=["30", "30 m/s", "dertig"],
        uitleg=r"Deel door \(3{,}6\): \(\dfrac{108}{3{,}6} = 30\) m/s. Omgekeerd "
        r"vermenigvuldig je met \(3{,}6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een auto legt \(243\) km af in \(2\) h \(30\) min. Hoe groot is \(v_{\text{gem}}\)?",
        opties=[
            r"\(97{,}2\) km/h",
            r"\(121{,}5\) km/h",
            r"\(81{,}0\) km/h",
            r"\(48{,}6\) km/h",
        ],
        antwoord=0,
        uitleg=r"\(v_{\text{gem}} = \dfrac{243\ \text{km}}{2{,}5\ \text{h}} = 97{,}2\) km/h, "
        r"of \(27\) m/s. Hoe hard hij onderweg reed, weet je daarmee niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De \(a(t)\)-grafiek van een ERB valt samen met de tijdas.",
        antwoord=True,
        uitleg=r"Daar is \(a = \dfrac{\Delta v}{\Delta t} = 0\), dus loopt de lijn op hoogte "
        r"nul. Bij een EVRB loopt ze horizontaal op een andere hoogte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitspraken over een \(x(t)\)-grafiek zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"de helling is de snelheid \(v\)",
            "een horizontaal stuk betekent stilstand",
            "een dalend stuk betekent terugkeren",
            r"de oppervlakte eronder is \(\Delta x\)",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"De oppervlakte onder een \(v(t)\)-grafiek is de verplaatsing, niet die onder "
        r"een \(x(t)\)-grafiek. Daar lees je \(x\) rechtstreeks op de verticale as af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een snelheid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze heeft een grootte, een richting en een zin",
            r"ze wordt voorgesteld door een vector \(\vec{v}\)",
            "ze is altijd positief, hoe het lichaam ook beweegt",
            r"ze wordt uitgedrukt in \(\text{m/s}^{2}\)",
        ],
        antwoord=[0, 1],
        uitleg=r"Beweegt een lichaam tegen de zin van de \(x\)-as, dan is \(v\) langs die as "
        r"negatief. \(\text{m/s}^{2}\) is de eenheid van versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een \(x(t)\)-grafiek loopt eerst stijgend en daarna dalend. Wat doet het lichaam?",
        opties=[
            "het keert onderweg om en komt terug",
            "het versnelt eerst en vertraagt dan",
            "het staat eerst stil en vertrekt dan",
            "het beweegt de hele tijd dezelfde kant op",
        ],
        antwoord=0,
        uitleg=r"De helling wisselt van teken, dus ook \(v\). Op het hoogste punt van de "
        r"grafiek is \(v = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een snelheid langs de \(x\)-as kan nooit negatief zijn.",
        antwoord=False,
        uitleg=r"Het teken zegt de zin van de beweging langs die as. Alleen de grootte "
        r"\(\lvert v \rvert\) blijft altijd positief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke gegevens heb je nodig voor \(v_{\text{gem}}\)? Kruis alles aan wat juist is.",
        opties=[
            r"de afgelegde weg \(s\)",
            r"de tijdsduur \(\Delta t\)",
            r"de massa \(m\) van het lichaam",
            r"de versnelling \(a\)",
        ],
        antwoord=[0, 1],
        uitleg=r"Je rekent \(v_{\text{gem}} = \dfrac{s}{\Delta t}\). De massa en de "
        r"versnelling doen daar niets toe.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee fietsers vertrekken samen met \(4{,}5\) m/s en \(7{,}0\) m/s. Hoe ver liggen ze na \(40\) s uit elkaar?",
        opties=[
            r"\(100\) m",
            r"\(460\) m",
            r"\(280\) m",
            r"\(40\) m",
        ],
        antwoord=0,
        uitleg=r"Reken met het verschil: \(\Delta v = 7{,}0 - 4{,}5 = 2{,}5\) m/s, dus "
        r"\(2{,}5 \times 40 = 100\) m. Je kan ook \(280 - 180\) nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trein rijdt met \(27\) m/s. Hoe ver komt hij in \(3\) min \(20\) s?",
        opties=[
            r"\(5{,}4 \times 10^{3}\) m",
            r"\(1{,}6 \times 10^{3}\) m",
            r"\(8{,}1 \times 10^{2}\) m",
            r"\(9{,}0 \times 10^{1}\) m",
        ],
        antwoord=0,
        uitleg=r"Zet de tijd eerst om: \(3\) min \(20\) s is \(200\) s, en "
        r"\(27 \times 200 = 5400\) m. Dat is \(5{,}4\) km.",
    ),
    dict(
        type="invultekst",
        vraag=r"Welke grootheid lees je af uit de oppervlakte onder een \(v(t)\)-grafiek?",
        antwoord=["de verplaatsing", "verplaatsing", "de afgelegde weg"],
        uitleg=r"Snelheid maal tijd is afstand. De helling van diezelfde grafiek geeft "
        r"\(a\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een ERB zijn \(v_{\text{gem}}\) en de ogenblikkelijke snelheid even groot.",
        antwoord=True,
        uitleg=r"De snelheid verandert niet, dus kan het gemiddelde niet anders uitvallen. "
        r"Bij een EVRB lopen de twee wel uiteen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een eenparig veranderlijke rechtlijnige beweging zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(a\) blijft dezelfde",
            r"de \(v(t)\)-grafiek is een rechte",
            r"de \(x(t)\)-grafiek is een parabool",
            r"\(v\) blijft dezelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"Een constante \(v\) hoort bij een ERB. Hier verandert \(v\) elke seconde "
        r"met dezelfde hoeveelheid: \(v = v_{0} + a\,t\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet de \(v(t)\)-grafiek van een EVRB eruit?",
        opties=[
            "een schuine rechte",
            "een horizontale rechte",
            "een parabool die opent naar boven",
            "een kromme die afvlakt naar een grens",
        ],
        antwoord=0,
        uitleg=r"De helling van die rechte is \(a\). De \(x(t)\)-grafiek is dan de parabool "
        r"\(x = x_{0} + v_{0}\,t + \tfrac{1}{2}a\,t^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een auto gaat in \(8{,}0\) s van \(12\) m/s naar \(30\) m/s. Hoe groot is \(a\)?",
        opties=[
            r"\(2{,}25\ \text{m/s}^{2}\)",
            r"\(3{,}75\ \text{m/s}^{2}\)",
            r"\(0{,}44\ \text{m/s}^{2}\)",
            r"\(18{,}0\ \text{m/s}^{2}\)",
        ],
        antwoord=0,
        uitleg=r"\(a = \dfrac{\Delta v}{\Delta t} = \dfrac{30 - 12}{8{,}0} = 2{,}25\ "
        r"\text{m/s}^{2}\). Let op dat je de beginsnelheid eerst aftrekt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fietser remt van \(10\) m/s tot stilstand in \(5{,}0\) s. Hoe groot is \(a\)?",
        opties=[
            r"\(-2{,}0\ \text{m/s}^{2}\)",
            r"\(+2{,}0\ \text{m/s}^{2}\)",
            r"\(-50\ \text{m/s}^{2}\)",
            r"\(-0{,}5\ \text{m/s}^{2}\)",
        ],
        antwoord=0,
        uitleg=r"\(a = \dfrac{0 - 10}{5{,}0} = -2{,}0\ \text{m/s}^{2}\). Het minteken zegt "
        r"dat \(\vec{a}\) tegen de bewegingszin in wijst; men noemt dat een vertraging.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een negatieve \(a\) betekent altijd dat het lichaam vertraagt.",
        antwoord=False,
        uitleg=r"Ze betekent dat \(\vec{a}\) tegen de zin van de as in wijst. Is \(v\) ook "
        r"negatief, dan versnelt het lichaam juist.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een wagen vertrekt uit rust met \(2{,}5\ \text{m/s}^{2}\). Hoe ver komt hij in \(6{,}0\) s?",
        opties=[
            r"\(45\) m",
            r"\(15\) m",
            r"\(90\) m",
            r"\(7{,}5\) m",
        ],
        antwoord=0,
        uitleg=r"Met \(v_{0} = 0\) wordt \(x = \tfrac{1}{2}a\,t^{2} = 0{,}5 \times 2{,}5 "
        r"\times 36 = 45\) m. Vergeet die factor een half niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde wagen: hoe snel rijdt hij na die \(6{,}0\) s?",
        opties=[
            r"\(15\) m/s",
            r"\(45\) m/s",
            r"\(7{,}5\) m/s",
            r"\(2{,}5\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(v = a\,t = 2{,}5 \times 6{,}0 = 15\) m/s. Zijn gemiddelde over die rit was "
        r"maar \(\dfrac{0 + 15}{2} = 7{,}5\) m/s.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de valversnelling op aarde ongeveer?",
        antwoord=["9,81 m/s²", "9,81", "ongeveer 10"],
        uitleg=r"Men rekent met \(g = 9{,}81\ \text{m/s}^{2}\), of afgerond met \(10\). Op de "
        r"maan is \(g\) zes keer kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe snel valt een steen na \(3{,}0\) s vrije val? Neem \(g = 9{,}81\ \text{m/s}^{2}\).",
        opties=[
            r"\(29{,}4\) m/s",
            r"\(44{,}1\) m/s",
            r"\(9{,}81\) m/s",
            r"\(3{,}27\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(v = g\,t = 9{,}81 \times 3{,}0 = 29{,}4\) m/s. De gevallen hoogte is "
        r"intussen \(\tfrac{1}{2}g\,t^{2} = 44{,}1\) m.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe diep is een put als een steen er \(2{,}0\) s over doet? Neem \(g = 9{,}81\ \text{m/s}^{2}\).",
        opties=[
            r"\(19{,}6\) m",
            r"\(39{,}2\) m",
            r"\(9{,}81\) m",
            r"\(4{,}91\) m",
        ],
        antwoord=0,
        uitleg=r"\(h = \tfrac{1}{2}g\,t^{2} = 0{,}5 \times 9{,}81 \times 4{,}0 = 19{,}6\) m. "
        r"Het geluid van de plons doet er ook nog even over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vrije val hangt de valtijd af van de massa van het voorwerp.",
        antwoord=False,
        uitleg=r"Zonder luchtweerstand geeft \(m\,g = m\,a\) altijd \(a = g\): de massa valt "
        r"links en rechts weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal recht omhoog. Wat gebeurt er in het hoogste punt?",
        opties=[
            r"\(v = 0\) maar \(a = g\) omlaag",
            r"\(v = 0\) en \(a = 0\)",
            r"\(a = 0\) maar \(v \neq 0\)",
            r"\(\vec{a}\) keert daar van zin om",
        ],
        antwoord=0,
        uitleg=r"De zwaartekracht blijft ook daar werken, dus blijft \(a = 9{,}81\ "
        r"\text{m/s}^{2}\) omlaag. Daarom valt de bal meteen weer terug.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit een bal met \(24\) m/s recht omhoog. Hoe lang duurt het tot het hoogste punt? Neem \(g = 9{,}81\ \text{m/s}^{2}\).",
        opties=[
            r"\(2{,}45\) s",
            r"\(4{,}89\) s",
            r"\(1{,}22\) s",
            r"\(24{,}5\) s",
        ],
        antwoord=0,
        uitleg=r"Zet \(v = v_{0} - g\,t = 0\), dus \(t = \dfrac{24}{9{,}81} = 2{,}45\) s. De "
        r"hele vlucht duurt \(4{,}89\) s, want het terugvallen duurt even lang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bewegingen zijn een EVRB? Kruis alles aan wat juist is.",
        opties=[
            "een vrije val zonder luchtweerstand",
            "een auto die gelijkmatig optrekt",
            "een fietser met constante snelheid",
            "een kind op een draaimolen",
        ],
        antwoord=[0, 1],
        uitleg=r"Bij een draaimolen verandert de richting voortdurend, dus is de beweging "
        r"niet rechtlijnig. Een constante \(v\) hoort bij een ERB.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een auto rijdt \(22\) m/s en remt met \(4{,}0\ \text{m/s}^{2}\). Hoe lang is zijn remweg?",
        opties=[
            r"\(60{,}5\) m",
            r"\(121\) m",
            r"\(5{,}5\) m",
            r"\(30{,}3\) m",
        ],
        antwoord=0,
        uitleg=r"Gebruik \(v^{2} = v_{0}^{2} + 2a\,\Delta x\) met \(v = 0\): "
        r"\(\Delta x = \dfrac{v_{0}^{2}}{2a} = \dfrac{484}{8{,}0} = 60{,}5\) m.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dubbele snelheid is de remweg vier keer zo lang.",
        antwoord=True,
        uitleg=r"In \(\Delta x = \dfrac{v_{0}^{2}}{2a}\) staat \(v_{0}\) in het kwadraat. "
        r"Daarom is een kleine snelheidsverhoging in de bebouwde kom zo gevaarlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een wagen rijdt met \(25\) m/s voorbij een stilstaande motor, die meteen vertrekt met \(4{,}0\ \text{m/s}^{2}\). Wanneer haalt de motor hem in?",
        opties=[
            r"na \(12{,}5\) s",
            r"na \(6{,}25\) s",
            r"na \(25{,}0\) s",
            r"na \(2{,}50\) s",
        ],
        antwoord=0,
        uitleg=r"Stel de twee plaatsen gelijk: \(25\,t = \tfrac{1}{2} \times 4{,}0 \times "
        r"t^{2}\), dus \(t = \dfrac{2 v}{a} = 12{,}5\) s. Beide hebben dan \(312{,}5\) m "
        r"afgelegd, en de motor rijdt op dat ogenblik \(50\) m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een vrije val zonder luchtweerstand zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(a\) blijft de hele val even groot",
            r"\(v\) groeit recht evenredig met \(t\)",
            r"de hoogte groeit met \(t^{2}\)",
            "een zwaarder voorwerp valt sneller",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"Zonder luchtweerstand vallen een steen en een pluim even snel: in \(v = g\,t\) "
        r"en \(h = \tfrac{1}{2}g\,t^{2}\) staat geen massa.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De oppervlakte onder een \(a(t)\)-grafiek geeft \(\Delta v\).",
        antwoord=True,
        uitleg=r"\(\Delta v = a\,\Delta t\), net zoals \(\Delta x = v\,\Delta t\). Zo hangen "
        r"de drie grafieken met elkaar samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een beweging waarbij enkel de zwaartekracht werkt en de beginsnelheid nul is?",
        antwoord=["vrije val", "een vrije val", "val"],
        uitleg=r"Ze is een EVRB met \(a = g = 9{,}81\ \text{m/s}^{2}\). Gooi je het voorwerp "
        r"eerst omhoog, dan spreek je van een verticale worp.",
    ),
]

# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde gevorderd 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen, andere situaties, en opdrachten die je enkel op papier
kan maken (een tabel aanvullen, een redenering uitschrijven, een schets maken).
Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/wiskunde-gevorderd.json` én naast de leerbundel, want de
oefenbundel is de tweede dekkingscontrole op de theorie.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen. Het achtervoegsel houdt ze uit elkaar van wiskunde gevorderd van
🚀 Boost doorstroom, dat precies dezelfde vaknaam draagt.

Wiskunde staat hier in echte notatie, tussen \( en \), net als in de vragen en
in de leerbundels. Zie oefenplatform/lib/wiskunde.ts. De omzetting gebeurt
thema per thema; alle 22 thema's zijn om.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Wiskunde gevorderd"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf je tussenstappen op. Een antwoord zonder berekening is niet na te kijken, ook niet door jezelf.",
    "Zet bij elk antwoord de eenheid, als er een is. Een getal zonder eenheid is in een vraagstuk zelden een antwoord.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


# ============================================================
OEFENBUNDELS["oefenbundel-machtswortels-machten-en-logaritmen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Machtswortels, machten en logaritmen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Machten met een gehele exponent",
             opdracht="Reken uit. Schrijf een negatieve exponent eerst om naar een breuk.",
             oefeningen=[
                 ("rij", [(r"\(3^{0}\)", r"\(1\)"), (r"\(5^{-2}\)", r"\(\tfrac{1}{25}\)"),
                          (r"\(\left(\tfrac{2}{3}\right)^{-3}\)", r"\(\tfrac{27}{8}\)"),
                          (r"\(\left(-2\right)^{-4}\)", r"\(\tfrac{1}{16}\)")],
                  "Reken uit.", W),
                 ("rij", [(r"\(a^{3}\cdot a^{5}\)", r"\(a^{8}\)"),
                          (r"\(\dfrac{a^{7}b^{-2}}{a^{3}b^{-5}}\)", r"\(a^{4}b^{3}\)"),
                          (r"\(\left(2a^{3}\right)^{4}\)", r"\(16a^{12}\)"),
                          (r"\(\dfrac{\left(3a^{2}\right)^{3}}{9a^{4}}\)", r"\(3a^{2}\)")],
                  "Vereenvoudig. Laat geen negatieve exponenten staan.", WL),
                 ("kort", r"Los op: \(5^{x}\cdot 5^{2x-1}=5^{8}\).", r"\(3x-1=8\), dus \(x=3\)", WW),
             ]),
        dict(kop="Rationale exponenten",
             opdracht="Schrijf eerst wat de exponent betekent en reken dan pas uit.",
             oefeningen=[
                 ("rij", [(r"\(9^{1/2}\)", r"\(3\)"), (r"\(64^{1/3}\)", r"\(4\)"),
                          (r"\(16^{3/4}\)", r"\(8\)"), (r"\(125^{2/3}\)", r"\(25\)")],
                  "Reken uit.", W),
                 ("rij", [(r"\(\sqrt[3]{a}\cdot\sqrt[4]{a}\)", r"\(a^{7/12}\)"),
                          (r"\(\dfrac{\sqrt{a^{3}}}{\sqrt[3]{a}}\)", r"\(a^{7/6}\)"),
                          (r"\(\left(a^{2/3}\right)^{3/4}\)", r"\(a^{1/2}\)"),
                          (r"\(\sqrt[5]{a^{10}b^{5}}\)", r"\(a^{2}b\)")],
                  "Schrijf als één macht van \\(a\\), met \\(a>0\\) en \\(b>0\\).", WL),
                 ("kort", r"Los op: \(x^{2/5}=4\).", r"\(x=4^{5/2}=32\)", WW),
                 ("open", r"Leg uit waarom \(8^{2/3}=4\). Noem beide stappen bij naam.",
                  r"Eerst de derdemachtswortel: \(\sqrt[3]{8}=2\); daarna kwadrateren: \(2^{2}=4\). De noemer van de exponent is de wortelexponent, de teller de macht.", 3),
                 ("waar", r"\(\sqrt[4]{-16}\) bestaat in \(\mathbb{R}\).", False),
                 ("waar", r"\(\sqrt[3]{-27}=-3\).", True),
                 ("waar", r"\(\sqrt{x^{2}}=x\) voor elke \(x\in\mathbb{R}\).", False),
             ]),
        dict(kop="Wortels vereenvoudigen",
             opdracht="Haal de volkomen machten uit de wortel, of maak de noemer rationaal.",
             oefeningen=[
                 ("rij", [(r"\(\sqrt{12}\)", r"\(2\sqrt{3}\)"),
                          (r"\(\sqrt{47}\)", "blijft staan, geen volkomen factor"),
                          (r"\(\sqrt[3]{24}\)", r"\(2\sqrt[3]{3}\)"),
                          (r"\(\sqrt{20}+\sqrt{45}\)", r"\(5\sqrt{5}\)")],
                  "Schrijf zo eenvoudig mogelijk.", WL),
                 ("rij", [(r"\(\dfrac{1}{\sqrt{5}}\)", r"\(\dfrac{\sqrt{5}}{5}\)"),
                          (r"\(\dfrac{4}{\sqrt{3}+1}\)", r"\(2\left(\sqrt{3}-1\right)\)")],
                  "Maak de noemer rationaal.", WL),
                 ("kort", r"Voor welke \(x\) bestaat \(\sqrt[6]{5-x}\) in \(\mathbb{R}\)?", r"\(x\leq 5\)", WW),
                 ("open", r"Toon met \(a=4\) en \(b=9\) aan dat \(\sqrt{a+b}\neq\sqrt{a}+\sqrt{b}\).",
                  r"\(\sqrt{13}\approx 3{,}6\), maar \(2+3=5\). Een wortel verdeelt zich over een product en een quotiënt, niet over een som.", 2),
             ]),
        dict(kop="Logaritmen uitrekenen",
             opdracht="Denk telkens: tot welke macht moet ik het grondtal verheffen?",
             oefeningen=[
                 ("rij", [(r"\(\log_{3}27\)", r"\(3\)"), (r"\(\log 1000\)", r"\(3\)"),
                          (r"\(\log_{7}1\)", r"\(0\)"), (r"\(\log_{2}\tfrac{1}{2}\)", r"\(-1\)")],
                  "Reken uit.", W),
                 ("rij", [(r"\(\log_{1/3}9\)", r"\(-2\)"), (r"\(\ln e^{5}\)", r"\(5\)"),
                          (r"\(e^{3\ln 2}\)", r"\(8\)"), (r"\(\log_{3}4\cdot\log_{4}81\)", r"\(4\)")],
                  "Reken uit zonder rekenapp.", WW),
                 ("tabel", ["Uitdrukking", "Als één logaritme geschreven"],
                  [[r"\(\log 3+\log 4\)", None],
                   [r"\(\log 20-\log 5\)", None],
                   [r"\(3\log 2\)", None],
                   [r"\(2\log x+\tfrac{1}{2}\log y\)", None]],
                  r"\(\log 12\); \(\log 4\); \(\log 8\); \(\log\left(x^{2}\sqrt{y}\right)\)", "260px"),
                 ("open", r"Ontbind \(\log_{a}\dfrac{x^{2}}{y^{3}\sqrt{z}}\) in losse logaritmen.",
                  r"\(2\log_{a}x-3\log_{a}y-\tfrac{1}{2}\log_{a}z\).", 2),
                 ("open", r"Leg uit waarom \(1\) geen grondtal van een logaritme kan zijn.",
                  r"\(1^{x}=1\) voor elke \(x\). Je zou dus van geen enkel ander getal de logaritme kunnen nemen, en van \(1\) zou elke exponent een antwoord zijn.", 3),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht="Noteer bij elke logaritmische vergelijking eerst het domein, en controleer je oplossing daar achteraf aan.",
             oefeningen=[
                 ("kort", r"Los op: \(\log_{2}(3x-1)=4\).", r"\(3x-1=16\), dus \(x=\tfrac{17}{3}\)", WW),
                 ("kort", r"Los op: \(2^{x}=15\). Geef een exacte vorm.", r"\(x=\dfrac{\ln 15}{\ln 2}\approx 3{,}91\)", WW),
                 ("open", r"Los op: \(\log_{3}x+\log_{3}(x-6)=3\). Schrijf ook waarom je één van de twee wortels weggooit.",
                  r"\(x(x-6)=27\), dus \(x^{2}-6x-27=0\) en \(x=9\) of \(x=-3\). Het domein vraagt \(x>6\), dus enkel \(x=9\).", 4),
                 ("open", r"Los op: \(3^{2x}-4\cdot 3^{x}+3=0\) met een hulponbekende.",
                  r"Stel \(t=3^{x}\): \(t^{2}-4t+3=0\) geeft \(t=1\) of \(t=3\), dus \(x=0\) of \(x=1\).", 4),
                 ("kies", r"Welke vergelijking heb je een logaritme voor nodig?",
                  [r"\(x^{2}=9\)", r"\(2x-6=0\)", r"\(5^{x}=30\)", r"\(\sqrt{x}=4\)"], 2),
             ]),
        dict(kop="Toepassingen",
             opdracht="Schrijf eerst de vergelijking op, en reken dan pas.",
             oefeningen=[
                 ("open", r"Een spaarrekening groeit met \(3\%\) per jaar. Na hoeveel volle jaren staat er anderhalve keer zoveel op?",
                  r"\(1{,}03^{n}\geq 1{,}5\), dus \(n\geq\dfrac{\ln 1{,}5}{\ln 1{,}03}\approx 13{,}7\): na 14 jaar.", 4),
                 ("open", r"De halveringstijd van een stof is 8 dagen. Welk deel is er na 30 dagen nog over?",
                  r"\(\left(\tfrac{1}{2}\right)^{30/8}\approx 0{,}075\), dus ongeveer \(7{,}5\%\).", 4),
                 ("kort", r"Het geluidsniveau is \(L=10\log\dfrac{I}{I_{0}}\). Met hoeveel decibel stijgt \(L\) als \(I\) verdubbelt?", r"\(10\log 2\approx 3\) dB", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veeltermen-deelbaarheid-en-horner-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veeltermen, deelbaarheid en Horner",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De reststelling",
             opdracht="Gebruik de reststelling: vul in, en je kent de rest zonder te delen.",
             oefeningen=[
                 ("rij", [(r"\(\left(x^{3}+x-2\right):(x-1)\)", r"\(0\)"),
                          (r"\(\left(x^{2}+3x+5\right):(x-2)\)", r"\(15\)"),
                          (r"\(\left(x^{3}-1\right):(x+1)\)", r"\(-2\)"),
                          (r"\(\left(2x^{2}-x+4\right):(x-3)\)", r"\(19\)")],
                  "Wat is de rest?", WW),
                 ("kort", r"Voor welke \(k\) is \(x^{3}-kx+6\) deelbaar door \(x-3\)?", r"\(27-3k+6=0\), dus \(k=11\)", WW),
                 ("open", r"Schrijf op hoe je in één regel nagaat of \(x+2\) een deler is van een veelterm \(P\).",
                  r"Bereken \(P(-2)\). Is dat \(0\), dan is \(x+2\) een deler.", 2),
             ]),
        dict(kop="Horner",
             opdracht="Vul in. Let goed op het teken van het getal dat je links in het schema zet.",
             oefeningen=[
                 ("tabel", ["Deler", "Getal links in het schema"],
                  [[r"\(x-4\)", None], [r"\(x+5\)", None], [r"\(x-1\)", None], [r"\(2x-1\)", None]],
                  r"\(4\); \(-5\); \(1\); \(\tfrac{1}{2}\)", "200px"),
                 ("kort", r"Hoeveel getallen zet je bovenaan het schema voor \(x^{4}-3x+1\)?", r"\(5\)", W),
                 ("open", r"Een derdegraadsveelterm mist de term in \(x^{2}\). Wat schrijf je op die plaats in het schema, en waarom?",
                  r"Een \(0\). Elke graad moet een plaats krijgen, anders schuiven de coëfficiënten op en klopt het schema niet meer.", 3),
                 ("open", r"Deel \(x^{3}-4x^{2}+x+6\) door \(x-3\) met Horner. Geef het quotiënt en de rest.",
                  r"Quotiënt \(x^{2}-x-2\), rest \(0\). De volledige ontbinding is \((x-3)(x-2)(x+1)\).", 4),
                 ("waar", r"Het laatste getal onderaan het schema van Horner is de rest van de deling.", True),
                 ("waar", r"Met Horner kan je ook delen door \(x^{2}-1\).", False),
             ]),
        dict(kop="Graden tellen",
             opdracht="Vul de tabel aan. Je hoeft niet te delen om het antwoord te kennen.",
             oefeningen=[
                 ("tabel", ["Graad deeltal", "Graad deler", "Graad quotiënt", "Graad rest hoogstens"],
                  [[r"\(6\)", r"\(2\)", None, None], [r"\(4\)", r"\(1\)", None, None], [r"\(5\)", r"\(3\)", None, None]],
                  r"\(4\) en \(1\); \(3\) en \(0\); \(2\) en \(2\)", "140px"),
                 ("open", r"Je deelt \(A\) door \(B\) en vindt quotiënt \(Q\) en rest \(R\). Schrijf het verband op dat je gebruikt om je deling te controleren.",
                  r"\(A=B\cdot Q+R\), met \(\deg R<\deg B\).", 2),
             ]),
        dict(kop="Ontbinden in factoren",
             opdracht="Kies zelf de methode: afzonderen, samennemen, een merkwaardig product, of een nulwaarde zoeken.",
             oefeningen=[
                 ("rij", [(r"\(x^{2}-25\)", r"\((x-5)(x+5)\)"),
                          (r"\(x^{2}+6x+9\)", r"\((x+3)^{2}\)"),
                          (r"\(4x^{3}-8x^{2}\)", r"\(4x^{2}(x-2)\)"),
                          (r"\(x^{2}-7x+10\)", r"\((x-2)(x-5)\)")],
                  "Ontbind in factoren.", WL),
                 ("rij", [(r"\(9x^{2}-16\)", r"\((3x-4)(3x+4)\)"),
                          (r"\(x^{3}+27\)", r"\((x+3)\left(x^{2}-3x+9\right)\)"),
                          (r"\(2x^{2}+x-6\)", r"\((x+2)(2x-3)\)"),
                          (r"\(x^{4}-81\)", r"\((x-3)(x+3)\left(x^{2}+9\right)\)")],
                  "Ontbind zo ver mogelijk in \\(\\mathbb{R}\\).", WL),
                 ("open", r"Ontbind \(x^{3}-1\) volledig in \(\mathbb{R}\). Schrijf je stappen op.",
                  r"\(P(1)=0\), dus \(x-1\) is een deler. Horner geeft \(x^{2}+x+1\), met \(D=1-4=-3<0\), dus daar stopt het: \((x-1)\left(x^{2}+x+1\right)\).", 4),
                 ("open", r"Ontbind \(2x^{3}+x^{2}-13x+6\) volledig. Begin bij de delers van de constante term.",
                  r"\(P(2)=0\), dus \(x-2\) is een deler. Horner geeft \(2x^{2}+5x-3=(x+3)(2x-1)\), dus \((x-2)(x+3)(2x-1)\).", 5),
                 ("kies", r"Hoeveel reële nulwaarden heeft \(x^{4}+4\)?",
                  [r"geen", r"\(2\)", r"\(3\)", r"\(4\)"], 0),
                 ("kort", r"Hoeveel is de som van de nulwaarden van \(2x^{2}-10x+8\)?", r"\(-\tfrac{b}{a}=5\)", WW),
                 ("waar", r"Elke veelterm van oneven graad heeft minstens één reële nulwaarde.", True),
                 ("waar", r"Bij \(D=0\) raakt de parabool de \(x\)-as.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vergelijkingen-en-ongelijkheden-oplossen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vergelijkingen en ongelijkheden oplossen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Bestaansvoorwaarden",
             opdracht="Schrijf voor elke uitdrukking op wat \\(x\\) mág zijn.",
             oefeningen=[
                 ("tabel", ["Uitdrukking", "Bestaansvoorwaarde"],
                  [[r"\(\sqrt{x+4}\)", None], [r"\(\log(x-1)\)", None],
                   [r"\(\dfrac{1}{x-3}\)", None], [r"\(\sqrt[3]{x}\)", None],
                   [r"\(\dfrac{\sqrt{x}}{x-2}\)", None]],
                  r"\(x\geq -4\); \(x>1\); \(x\neq 3\); geen voorwaarde; \(x\geq 0\) en \(x\neq 2\)", "280px"),
             ]),
        dict(kop="Vergelijkingen",
             opdracht="Los op. Controleer bij een wortel- of logaritmevergelijking elke oplossing in de oorspronkelijke vergelijking.",
             oefeningen=[
                 ("rij", [(r"\(3x-12=0\)", r"\(x=4\)"), (r"\(x^{2}=16\)", r"\(x=4\) of \(x=-4\)"),
                          (r"\(2^{x}=16\)", r"\(x=4\)"), (r"\(5^{2x}=5^{x+3}\)", r"\(x=3\)")],
                  "Los op.", WW),
                 ("rij", [(r"\(|2x-1|=7\)", r"\(x=4\) of \(x=-3\)"),
                          (r"\(x^{4}-5x^{2}+4=0\)", r"\(x=\pm 1\) en \(x=\pm 2\)"),
                          (r"\(\log_{3}(x-2)=2\)", r"\(x=11\)"),
                          (r"\(3^{x}=7\)", r"\(x=\dfrac{\ln 7}{\ln 3}\approx 1{,}77\)")],
                  "Los op.", WL),
                 ("open", r"Los op: \(\sqrt{x+6}=x\). Schrijf ook op welke oplossing wegvalt en waarom.",
                  r"Kwadrateren geeft \(x^{2}-x-6=0\), dus \(x=3\) of \(x=-2\). \(x=-2\) valt weg: een vierkantswortel kan niet negatief zijn. De oplossing is \(x=3\).", 5),
                 ("open", r"Los op: \(\log_{2}x+\log_{2}(x-4)=5\). Vergeet het domein niet.",
                  r"\(x(x-4)=32\), dus \(x^{2}-4x-32=0\) en \(x=8\) of \(x=-4\). Het domein vraagt \(x>4\), dus enkel \(x=8\).", 5),
                 ("kort", r"Voor welke \(m\) heeft \(x^{2}-6x+m=0\) precies één oplossing?", r"\(D=36-4m=0\), dus \(m=9\)", WW),
                 ("waar", r"Kwadrateren kan oplossingen bijmaken die in de oorspronkelijke vergelijking niet kloppen.", True),
                 ("waar", r"Beide leden delen door een uitdrukking met \(x\) in, is altijd veilig.", False),
             ]),
        dict(kop="De discriminant",
             opdracht="Bereken de discriminant en zeg hoeveel reële oplossingen er zijn.",
             oefeningen=[
                 ("tabel", ["Vergelijking", "Discriminant", "Aantal reële oplossingen"],
                  [[r"\(x^{2}-4x+4=0\)", None, None],
                   [r"\(x^{2}+x+3=0\)", None, None],
                   [r"\(2x^{2}-5x+2=0\)", None, None],
                   [r"\(-x^{2}+2x+8=0\)", None, None]],
                  r"\(0\) en één; \(-11\) en geen; \(9\) en twee; \(36\) en twee", "160px"),
             ]),
        dict(kop="Ongelijkheden",
             opdracht="Breng alles naar één lid, zoek de nulwaarden en maak een tekenschema.",
             oefeningen=[
                 ("rij", [(r"\(4x-8>0\)", r"\(x>2\)"),
                          (r"\(-2x+6>0\)", r"\(x<3\)"),
                          (r"\(x^{2}-1<0\)", r"\(-1<x<1\)"),
                          (r"\(x^{2}-6x+8>0\)", r"\(x<2\) of \(x>4\)")],
                  "Los op.", WL),
                 ("rij", [(r"\(x^{2}\leq 2x\)", r"\(\left[0,2\right]\)"),
                          (r"\((x+1)(x-3)\geq 0\)", r"\(x\leq -1\) of \(x\geq 3\)"),
                          (r"\(\dfrac{x+2}{x-1}>0\)", r"\(x<-2\) of \(x>1\)"),
                          (r"\(-x^{2}+4\geq 0\)", r"\(\left[-2,2\right]\)")],
                  "Los op en schrijf het antwoord als interval.", WL),
                 ("open", r"Leg uit waarom je bij \(-2x+6>0\) het ongelijkheidsteken moet omdraaien.",
                  r"Je houdt \(-2x>-6\) over en deelt door \(-2\). Delen door een negatief getal draait het teken om, dus \(x<3\).", 3),
                 ("open", r"Waarom hoort \(x=1\) niet bij de oplossing van \(\dfrac{x+2}{x-1}\geq 0\), ook al staat er \(\geq\)?",
                  r"In \(x=1\) is de noemer \(0\) en bestaat de breuk niet. De nulwaarde van de teller mag er wel bij, die van de noemer nooit.", 3),
                 ("kies", r"Wat is de oplossing van \(x^{2}+4>0\)?",
                  [r"geen enkele \(x\)", r"alleen \(x>0\)", r"elke \(x\in\mathbb{R}\)", r"\(-2<x<2\)"], 2),
                 ("waar", r"Een ongelijkheid heeft hoogstens twee oplossingen.", False),
                 ("waar", r"Bij \(f(x)\geq g(x)\) horen de snijpunten bij de oplossing.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-functie-aflezen-van-haar-grafiek-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een functie aflezen van haar grafiek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Domein en bereik",
             opdracht="Schrijf het domein op. Denk aan noemers die nul worden en aan wortels.",
             oefeningen=[
                 ("tabel", ["Functie", "Domein"],
                  [[r"\(f(x)=\dfrac{1}{x+2}\)", None], [r"\(f(x)=\sqrt{x-1}\)", None],
                   [r"\(f(x)=x^{2}-3x\)", None], [r"\(f(x)=\ln x\)", None],
                   [r"\(f(x)=\dfrac{\sqrt{x+1}}{x-4}\)", None]],
                  r"\(\mathbb{R}\setminus\{-2\}\); \(\left[1,+\infty\right[\); \(\mathbb{R}\); \(\left]0,+\infty\right[\); \(x\geq -1\) en \(x\neq 4\)", "280px"),
                 ("kort", r"Wat is \(\text{ber}\,f\) voor \(f(x)=x^{2}+1\)?", r"\(\left[1,+\infty\right[\)", WW),
                 ("open", r"Een model geeft de hoogte van een zonnebloem in functie van het aantal dagen na het zaaien. Wat is het praktisch domein, en waarom is dat kleiner dan het wiskundige?",
                  r"Van \(0\) dagen tot het moment dat de plant uitgegroeid is. Een negatieve tijd bestaat niet in de context, ook al vult het voorschrift ze gewoon in.", 3),
             ]),
        dict(kop="Even, oneven of geen van beide",
             opdracht="Reken \\(f(-x)\\) uit en vergelijk met \\(f(x)\\).",
             oefeningen=[
                 ("tabel", ["Functie", "Even, oneven of geen van beide"],
                  [[r"\(f(x)=x^{2}\)", None], [r"\(f(x)=x^{3}\)", None],
                   [r"\(f(x)=x^{2}+x\)", None], [r"\(f(x)=\cos x\)", None],
                   [r"\(f(x)=\dfrac{1}{x}\)", None]],
                  "even; oneven; geen van beide; even; oneven", "240px"),
                 ("waar", r"Een grafiek die symmetrisch ligt om de oorsprong hoort bij een even functie.", False),
             ]),
        dict(kop="Het verloop in woorden",
             opdracht="Vul het juiste woord in: toenemende stijging, afnemende stijging, buigpunt, plaatselijk maximum.",
             oefeningen=[
                 ("rij", [("de grafiek stijgt en wordt almaar steiler", "toenemende stijging"),
                          ("de grafiek stijgt, maar minder en minder steil", "afnemende stijging"),
                          ("hol gaat over in bol", "buigpunt"),
                          ("de hoogste waarde in een stukje van de grafiek", "plaatselijk maximum")],
                  "Welk woord hoort erbij?", WL),
                 ("open", r"Leg het verschil uit tussen een plaatselijk en een absoluut maximum.",
                  r"Een plaatselijk maximum is de hoogste waarde in zijn eigen omgeving; verderop kan de grafiek nog hoger gaan. Een absoluut maximum is de hoogste waarde op het hele domein.", 3),
             ]),
        dict(kop="Asymptoten",
             opdracht="Zoek de horizontale en de verticale asymptoot. Kijk naar de hoogste graden en naar de noemer.",
             oefeningen=[
                 ("tabel", ["Functie", "Horizontale asymptoot", "Verticale asymptoot"],
                  [[r"\(f(x)=\dfrac{3x-2}{x+1}\)", None, None],
                   [r"\(f(x)=\dfrac{5}{x-4}\)", None, None],
                   [r"\(f(x)=\dfrac{x^{2}}{x-1}\)", None, None]],
                  r"\(y=3\) en \(x=-1\); \(y=0\) en \(x=4\); geen horizontale (de teller is van hogere graad) en \(x=1\)", "160px"),
                 ("waar", r"Elke functie heeft minstens één asymptoot.", False),
             ]),
        dict(kop="De inverse functie",
             opdracht="Zoek het voorschrift van de inverse: verwissel \\(x\\) en \\(y\\), en los op naar \\(y\\).",
             oefeningen=[
                 ("rij", [(r"\(f(x)=x+7\)", r"\(f^{-1}(x)=x-7\)"), (r"\(f(x)=3x\)", r"\(f^{-1}(x)=\tfrac{x}{3}\)"),
                          (r"\(f(x)=2x-4\)", r"\(f^{-1}(x)=\tfrac{x+4}{2}\)"), (r"\(f(x)=\tfrac{1}{x}\)", r"\(f^{-1}(x)=\tfrac{1}{x}\)")],
                  "Wat is de inverse?", WL),
                 ("kort", r"Wat is de inverse van \(f(x)=\dfrac{x-5}{4}\)?", r"\(f^{-1}(x)=4x+5\)", WW),
                 ("kort", r"Wat is de inverse van \(f(x)=e^{x}\)?", r"\(f^{-1}(x)=\ln x\)", WW),
                 ("kies", r"Welke functie is niet inverteerbaar op heel haar domein?",
                  [r"\(f(x)=3x+1\)", r"\(f(x)=x^{2}\)", r"\(f(x)=\ln x\)", r"\(f(x)=2^{x}\)"], 1),
                 ("open", r"Een punt van een grafiek is \((5,0)\). Welk punt hoort daarbij op de grafiek van \(f^{-1}\), en waarom?",
                  r"Het punt \((0,5)\). Bij spiegelen om \(y=x\) wisselen de twee coördinaten van plaats.", 2),
                 ("waar", r"Er geldt \(\text{dom}\,f^{-1}=\text{ber}\,f\).", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tweedegraadsfuncties-en-transformaties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tweedegraadsfuncties en transformaties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De parabool onderzoeken",
             opdracht="Vul de tabel aan voor elke tweedegraadsfunctie.",
             oefeningen=[
                 ("tabel", ["Functie", "Top", "Nulwaarden", "Dal of berg"],
                  [[r"\(f(x)=x^{2}-4x+3\)", None, None, None],
                   [r"\(f(x)=-x^{2}+6x-8\)", None, None, None],
                   [r"\(f(x)=x^{2}+2x+5\)", None, None, None],
                   [r"\(f(x)=2x^{2}-8x+6\)", None, None, None]],
                  r"\((2,-1)\), \(1\) en \(3\), dal; \((3,1)\), \(2\) en \(4\), berg; \((-1,4)\), geen reële nulwaarden, dal; \((2,-2)\), \(1\) en \(3\), dal",
                  "150px"),
                 ("kort", r"Welke vergelijking heeft de symmetrieas van een parabool met top \((-3,7)\)?", r"\(x=-3\)", WW),
                 ("kort", r"Wat is \(\text{ber}\,f\) voor \(f(x)=-x^{2}+6x-8\)?", r"\(\left]-\infty,1\right]\)", WW),
             ]),
        dict(kop="De topvorm",
             opdracht="Lees de top af, of schrijf het voorschrift in topvorm.",
             oefeningen=[
                 ("rij", [(r"\(f(x)=(x-5)^{2}+2\)", r"\((5,2)\)"),
                          (r"\(f(x)=3(x+1)^{2}-4\)", r"\((-1,-4)\)"),
                          (r"\(f(x)=-2(x-3)^{2}\)", r"\((3,0)\)"),
                          (r"\(f(x)=(x+4)^{2}-1\)", r"\((-4,-1)\)")],
                  "Wat is de top?", WW),
                 ("kort", r"Schrijf \(f(x)=x^{2}-8x+11\) in topvorm.", r"\((x-4)^{2}-5\)", WW),
                 ("open", r"Een parabool heeft top \((2,1)\) en gaat door \((3,4)\). Zoek haar voorschrift.",
                  r"Vertrek van \(y=a(x-2)^{2}+1\). Vul \((3,4)\) in: \(a+1=4\), dus \(a=3\) en \(y=3(x-2)^{2}+1\).", 4),
                 ("kort", r"Voor welke \(m\) raakt \(y=x^{2}+4x+m\) de \(x\)-as?", r"\(D=16-4m=0\), dus \(m=4\)", WW),
             ]),
        dict(kop="Transformaties benoemen",
             opdracht="Schrijf op welke transformatie je van \\(x^{2}\\) naar de gegeven functie brengt.",
             oefeningen=[
                 ("rij", [(r"\(x^{2}+6\)", r"\(6\) omhoog"), (r"\((x-7)^{2}\)", r"\(7\) naar rechts"),
                          (r"\((x+2)^{2}\)", r"\(2\) naar links"), (r"\(-x^{2}\)", r"spiegeling om de \(x\)-as")],
                  "Welke transformatie?", WL),
                 ("open", r"Welke drie stappen brengen je van \(x^{2}\) naar \(-3(x+2)^{2}+5\)? Zet ze in volgorde.",
                  r"Twee naar links, verticaal uitrekken met \(3\) en spiegelen om de \(x\)-as, en dan \(5\) omhoog. De top komt op \((-2,5)\) en het is een bergparabool.", 4),
                 ("kies", r"Welke transformatie laat de nulwaarden van een functie op hun plaats?",
                  [r"\(f(x-2)\)", r"\(3f(x)\)", r"\(f(x)+3\)", r"\(f(x+1)\)"], 1),
                 ("waar", r"De grafiek van \(3x^{2}\) is breder dan die van \(x^{2}\).", False),
                 ("waar", r"Een verticale verschuiving laat de symmetrieas van een parabool op haar plaats.", True),
                 ("waar", r"\(f(-x)\) is een spiegeling om de \(y\)-as.", True),
             ]),
        dict(kop="Een parabool in een context",
             opdracht="Werk uit en schrijf je redenering op.",
             oefeningen=[
                 ("open", r"Een bal wordt opgegooid. Zijn hoogte in meter na \(t\) seconden is \(h(t)=-5t^{2}+20t\). Op welk ogenblik is hij het hoogst, en hoe hoog komt hij?",
                  r"De top ligt bij \(t=\dfrac{-20}{-10}=2\) seconden, en \(h(2)=-20+40=20\) meter.", 5),
                 ("open", r"Wanneer komt die bal weer op de grond? Schrijf op hoe je dat vindt.",
                  r"Stel \(h(t)=0\): \(-5t(t-4)=0\), dus \(t=0\) of \(t=4\). Na vier seconden is hij terug op de grond.", 4),
                 ("open", r"Een rechthoekige weide tegen een muur krijgt \(40\) m draad voor drie zijden. Welke afmetingen geven de grootste oppervlakte?",
                  r"Met breedte \(x\) is de diepte \(\dfrac{40-2x}{2}=20-x\), dus \(O(x)=x(20-x)=-x^{2}+20x\). De top ligt bij \(x=10\): \(10\) m bij \(10\) m, met \(100\) m².", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-exponentiele-en-logaritmische-functies-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Exponentiële en logaritmische functies",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De grafieken",
             opdracht="Vul in. Kijk eerst naar het grondtal.",
             oefeningen=[
                 ("tabel", ["Functie", "Stijgend of dalend", "Horizontale asymptoot"],
                  [[r"\(f(x)=3^{x}\)", None, None], [r"\(f(x)=0{,}4^{x}\)", None, None],
                   [r"\(f(x)=2^{x}+3\)", None, None], [r"\(f(x)=-2^{x}\)", None, None]],
                  r"stijgend, \(y=0\); dalend, \(y=0\); stijgend, \(y=3\); dalend, \(y=0\)", "180px"),
                 ("kort", r"Door welk punt op de \(y\)-as gaat elke grafiek van \(f(x)=a^{x}\)?", r"\((0,1)\)", WW),
                 ("kort", r"De grafiek van \(f(x)=a^{x}\) gaat door \((1,7)\). Hoeveel is \(a\)?", r"\(7\)", W),
                 ("waar", r"De grafiek van een exponentiële functie snijdt haar horizontale asymptoot.", False),
                 ("open", r"Geef \(\text{dom}\,f\) en \(\text{ber}\,f\) van \(f(x)=3\cdot 2^{x}-6\), en haar asymptoot. Leg uit waar de \(-6\) in terugkomt.",
                  r"\(\text{dom}\,f=\mathbb{R}\). De grafiek van \(2^{x}\) wordt eerst met \(3\) uitgerekt, dus het bereik is nog \(\left]0,+\infty\right[\), en daarna \(6\) omlaag geschoven. Dus \(\text{ber}\,f=\left]-6,+\infty\right[\) en de asymptoot is \(y=-6\). De \(-6\) staat buiten de macht en werkt dus op de functiewaarde.", 4),
             ]),
        dict(kop="Logaritmen uitrekenen",
             opdracht="Zonder rekentoestel. Schrijf telkens de macht op die je zoekt.",
             oefeningen=[
                 ("rij", [(r"\(\log_{2}32\)", r"\(5\)"), (r"\(\log_{3}\tfrac{1}{9}\)", r"\(-2\)"),
                          (r"\(\log_{1/2}8\)", r"\(-3\)"), (r"\(\ln e^{4}\)", r"\(4\)"),
                          (r"\(\log_{5}1\)", r"\(0\)"), (r"\(\log_{9}3\)", r"\(\tfrac{1}{2}\)")],
                  "Reken uit.", W),
                 ("open", r"Bepaal \(\text{dom}\,f\) voor \(f(x)=\log_{3}(x^{2}-9)\).",
                  r"Het argument moet strikt positief zijn: \(x^{2}-9>0\), dus \(x<-3\) of \(x>3\). Dus \(\text{dom}\,f=\left]-\infty,-3\right[\cup\left]3,+\infty\right[\).", 3),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht="Schrijf eerst de bestaansvoorwaarden op als er een logaritme in staat.",
             oefeningen=[
                 ("rij", [(r"\(2^{x}=32\)", r"\(x=5\)"), (r"\(3^{x+1}=81\)", r"\(x=3\)"),
                          (r"\(5^{2x}=125\)", r"\(x=\tfrac{3}{2}\)"), (r"\(\log_{2}x=6\)", r"\(x=64\)")],
                  "Los op.", WW),
                 ("open", r"Los op: \(2^{x}=7\). Geef het antwoord eerst exact, daarna tot op twee cijfers na de komma.",
                  r"\(x=\log_{2}7=\dfrac{\ln 7}{\ln 2}\approx 2{,}81\).", 3),
                 ("open", r"Los op: \(\log_{2}x+\log_{2}(x-6)=4\). Vergeet de bestaansvoorwaarden niet.",
                  r"Bestaansvoorwaarden: \(x>0\) én \(x-6>0\), dus \(x>6\). Samennemen geeft \(\log_{2}\left(x(x-6)\right)=4\), dus \(x^{2}-6x=16\) en \(x^{2}-6x-16=0\). Dat geeft \(x=8\) of \(x=-2\). Alleen \(x=8\) voldoet aan \(x>6\).", 5),
                 ("open", r"Los op: \(4^{x}-5\cdot 2^{x}+4=0\). Tip: stel \(t=2^{x}\).",
                  r"\(4^{x}=(2^{2})^{x}=(2^{x})^{2}=t^{2}\), dus \(t^{2}-5t+4=0\) met \(t=1\) of \(t=4\). Dan is \(2^{x}=1\), dus \(x=0\), of \(2^{x}=4\), dus \(x=2\).", 5),
             ]),
        dict(kop="Groeifactoren",
             opdracht="Vul de tabel aan. Een groeifactor is nooit negatief.",
             oefeningen=[
                 ("tabel", ["Situatie", "Groeifactor"],
                  [[r"\(6\%\) groei per jaar", None], [r"\(15\%\) daling per jaar", None],
                   [r"van \(80\) naar \(100\)", None], [r"het aantal verdubbelt", None],
                   [r"maandfactor \(1{,}02\), per jaar", None]],
                  r"\(1{,}06\); \(0{,}85\); \(1{,}25\); \(2\); \(1{,}02^{12}\approx 1{,}27\)", "160px"),
                 ("rij", [(r"\(1{,}08\)", r"\(8\%\) erbij"), (r"\(0{,}95\)", r"\(5\%\) eraf"),
                          (r"\(1{,}5\)", r"\(50\%\) erbij"), (r"\(1\)", "er verandert niets")],
                  "Hoeveel procent?", WW),
             ]),
        dict(kop="Lineair of exponentieel",
             opdracht="Kijk naar het verschil én naar de factor tussen twee opeenvolgende getallen.",
             oefeningen=[
                 ("rij", [(r"\(5,\ 10,\ 20,\ 40\)", "exponentieel"), (r"\(5,\ 10,\ 15,\ 20\)", "lineair"),
                          (r"\(100,\ 90,\ 81,\ 72{,}9\)", "exponentieel"), (r"\(100,\ 90,\ 80,\ 70\)", "lineair")],
                  "Lineair of exponentieel?", WW),
                 ("open", "Je spaart elke maand vijftig euro op een spaarpot zonder intrest. Welk model past, en waarom?",
                  r"Een lineair model, \(f(x)=50x+b\): er komt elke maand hetzelfde bedrag bij, dus een vast verschil en geen vaste factor.", 3),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Schrijf eerst het model op, dan pas de berekening. Rond af zoals gevraagd.",
             oefeningen=[
                 ("open", r"Een bedrag van \(1000\) euro staat op een rekening met \(4\%\) samengestelde intrest. Schrijf het model op en bereken het saldo na \(3\) jaar, tot op de cent.",
                  r"Model: \(K(t)=1000\cdot 1{,}04^{t}\). Dan is \(K(3)=1000\cdot 1{,}04^{3}=1000\cdot 1{,}124864\), dus \(1124{,}86\) euro.", 4),
                 ("open", r"Hoeveel jaar duurt het voor datzelfde bedrag verdubbeld is? Werk met een logaritme en rond af op één cijfer na de komma.",
                  r"Je lost \(1{,}04^{t}=2\) op, dus \(t=\dfrac{\ln 2}{\ln 1{,}04}\approx 17{,}7\) jaar. De vuistregel \(\tfrac{100}{4}=25\) zit er ver naast.", 4),
                 ("open", r"Een stof heeft een halveringstijd van \(8\) jaar. Welk deel blijft er over na \(24\) jaar? En na \(20\) jaar? Geef het tweede antwoord tot op drie cijfers na de komma.",
                  r"Na \(24\) jaar zijn dat drie halveringstijden: \(\left(\tfrac{1}{2}\right)^{3}=\tfrac{1}{8}\). Na \(20\) jaar is dat \(\tfrac{20}{8}=2{,}5\) halveringstijden, dus \(\left(\tfrac{1}{2}\right)^{2{,}5}\approx 0{,}177\).", 4),
                 ("open", r"Een bacteriecultuur telt \(400\) cellen en groeit met \(12\%\) per uur. Na hoeveel volle uren zijn er meer dan \(5000\) cellen?",
                  r"Model: \(N(t)=400\cdot 1{,}12^{t}\). Je lost \(400\cdot 1{,}12^{t}>5000\) op, dus \(1{,}12^{t}>12{,}5\) en \(t>\dfrac{\ln 12{,}5}{\ln 1{,}12}\approx 22{,}3\). Vanaf \(23\) volle uren.", 5),
                 ("open", r"Een auto van \(24\,000\) euro verliest elk jaar \(18\%\) van zijn waarde. Na hoeveel jaar is hij minder dan \(10\,000\) euro waard?",
                  r"Model: \(W(t)=24000\cdot 0{,}82^{t}\). Je lost \(0{,}82^{t}<\tfrac{10000}{24000}=\tfrac{5}{12}\) op. Omdat \(\ln 0{,}82<0\) draait het ongelijkheidsteken om: \(t>\dfrac{\ln\tfrac{5}{12}}{\ln 0{,}82}\approx 4{,}4\). Vanaf het vijfde jaar.", 5),
                 ("open", r"Een aantal groeit met \(10\%\) en daalt daarna met \(10\%\). Zit je terug op het begin? Reken na.",
                  r"Nee. \(1{,}1\cdot 0{,}9=0{,}99\), dus je houdt \(99\%\) over en verliest \(1\%\).", 3),
                 ("kies", r"Hoe bereken je na hoeveel jaar een bedrag met groeifactor \(1{,}03\) verdubbeld is?",
                  [r"\(\tfrac{100}{3}\)", r"met een logaritme: \(t=\tfrac{\ln 2}{\ln 1{,}03}\)", r"\(\tfrac{2}{1{,}03}\)", r"\(1{,}03\cdot 2\)"], 1),
             ]),
    ],
)
# ============================================================
OEFENBUNDELS["oefenbundel-goniometrische-functies-en-goniometrie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Goniometrische functies en goniometrie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Graden en radialen",
             opdracht=r"Zet om. Vertrek telkens van \(\pi\) radialen \(= 180^\circ\).",
             oefeningen=[
                 ("rij", [(r"\(45^\circ\)", r"\(\dfrac{\pi}{4}\)"),
                          (r"\(120^\circ\)", r"\(\dfrac{2\pi}{3}\)"),
                          (r"\(\dfrac{\pi}{6}\) rad", r"\(30^\circ\)"),
                          (r"\(\dfrac{3\pi}{2}\) rad", r"\(270^\circ\)")],
                  "Zet om.", WW),
                 ("rij", [(r"\(15^\circ\)", r"\(\dfrac{\pi}{12}\)"),
                          (r"\(300^\circ\)", r"\(\dfrac{5\pi}{3}\)"),
                          (r"\(\dfrac{5\pi}{4}\) rad", r"\(225^\circ\)")],
                  "Zet om.", WW),
             ]),
        dict(kop="Driehoeken oplossen",
             opdracht="Schrijf eerst welke regel je gebruikt, en pas daarna de berekening.",
             oefeningen=[
                 ("tabel", ["Wat je kent van de driehoek", "Welke regel"],
                  [[r"zijde \(a\) en de hoeken \(\widehat{A}\) en \(\widehat{B}\)", None],
                   [r"de zijden \(b\) en \(c\) en de hoek ertussen", None],
                   ["de drie zijden", None], ["twee hoeken", None]],
                  "sinusregel; cosinusregel; cosinusregel; de hoekensom, en dan de sinusregel", "260px"),
                 ("open", r"Een driehoek heeft zijden van \(4\) cm en \(7\) cm met een hoek van \(60^\circ\) ertussen. Bereken de derde zijde.",
                  r"\(a^{2} = 16 + 49 - 2 \cdot 4 \cdot 7 \cdot \cos 60^\circ = 65 - 28 = 37\), dus "
                  r"\(a = \sqrt{37} \approx 6{,}1\) cm.", 4),
                 ("open", r"In een driehoek is \(a = 8\), \(b = 5\) en \(c = 7\). Bereken \(\widehat{A}\).",
                  r"\(\cos A = \dfrac{25 + 49 - 64}{2 \cdot 5 \cdot 7} = \dfrac{10}{70} \approx 0{,}143\), "
                  r"dus \(\widehat{A} \approx 81{,}8^\circ\).", 4),
                 ("waar", r"De cosinusregel wordt \(a^{2} = b^{2} + c^{2}\) als de hoek recht is.", True),
             ]),
        dict(kop="De goniometrische cirkel",
             opdracht=r"Vul in. De cosinus is de \(x\)-coördinaat, de sinus de \(y\)-coördinaat.",
             oefeningen=[
                 ("tabel", ["Hoek", "Sinus", "Cosinus"],
                  [[r"\(0^\circ\)", None, None], [r"\(30^\circ\)", None, None],
                   [r"\(90^\circ\)", None, None], [r"\(180^\circ\)", None, None],
                   [r"\(270^\circ\)", None, None]],
                  r"\(0\) en \(1\); \(\tfrac{1}{2}\) en \(\tfrac{\sqrt{3}}{2}\); \(1\) en \(0\); "
                  r"\(0\) en \(-1\); \(-1\) en \(0\)", "140px"),
                 ("kies", "Twee hoeken zijn supplementair. Wat geldt dan?",
                  ["dezelfde sinus, tegengestelde cosinus", "dezelfde cosinus, tegengestelde sinus",
                   "allebei dezelfde", "de sinus van de ene is de cosinus van de andere"], 0),
             ]),
        dict(kop="Rekenen met de grondformule",
             opdracht=r"Gebruik \(\sin^{2}x + \cos^{2}x = 1\).",
             oefeningen=[
                 ("kort", r"\(\sin x = \tfrac{3}{5}\) en \(x\) ligt in het eerste kwadrant. Hoeveel is \(\cos x\)?",
                  r"\(\cos x = \tfrac{4}{5}\).", WW),
                 ("kort", r"\(\cos x = -\tfrac{12}{13}\) en \(x\) ligt in het tweede kwadrant. Hoeveel is \(\sin x\)?",
                  r"\(\sin x = \tfrac{5}{13}\).", WW),
                 ("kort", r"Hoeveel is \(\tan x\) als \(\sin x = \tfrac{3}{5}\) en \(\cos x = \tfrac{4}{5}\)?",
                  r"\(\tan x = \tfrac{3}{4}\).", WW),
                 ("open", r"Toon aan dat \(\sin 2x\) nooit gelijk is aan \(2\sin x\), behalve in bijzondere gevallen.",
                  r"\(\sin 2x = 2\sin x\cos x\), dus de twee zijn alleen gelijk als \(\cos x = 1\) "
                  r"of \(\sin x = 0\). Voor \(x = \tfrac{\pi}{2}\) staat er links \(0\) en rechts \(2\).", 4),
             ]),
        dict(kop="De algemene sinusfunctie",
             opdracht=r"Lees af uit het voorschrift. De periode is \(\dfrac{2\pi}{b}\).",
             oefeningen=[
                 ("tabel", ["Functie", "Amplitude", "Periode", "Evenwichtslijn"],
                  [[r"\(y = 4\sin x\)", None, None, None],
                   [r"\(y = \sin 4x\)", None, None, None],
                   [r"\(y = 2\sin x + 3\)", None, None, None],
                   [r"\(y = -3\sin 2x - 1\)", None, None, None]],
                  r"\(4\), \(2\pi\), \(y = 0\); \(1\), \(\tfrac{\pi}{2}\), \(y = 0\); \(2\), "
                  r"\(2\pi\), \(y = 3\); \(3\), \(\pi\), \(y = -1\)", "130px"),
                 ("open", r"Het water aan de kust staat tussen \(1\) m en \(5\) m diep en herhaalt zich om de \(12\) uur. Schrijf een sinusmodel op en zeg wat elk getal betekent.",
                  r"\(y = 2\sin\!\left(\dfrac{2\pi t}{12}\right) + 3\). De amplitude \(2\) is het "
                  r"halve verschil, de \(3\) is het gemiddelde peil en \(12\) is de periode in uren.", 4),
                 ("kort", r"Wat is het bereik van \(y = -3\sin 2x - 1\)?",
                  r"\([-4,\ 2]\).", WW),
             ]),
        dict(kop="Formules",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"\(\sin 2x\)", r"\(2\sin x\cos x\)"),
                          (r"\(\cos 2x\)", r"\(\cos^{2}x - \sin^{2}x\)"),
                          (r"\(\sin(-x)\)", r"\(-\sin x\)")],
                  "Schrijf de formule uit.", WW),
                 ("open", r"Leg uit waarom \(\cos 2x \neq 2\cos x\).",
                  r"Een goniometrisch getal is geen factor die je buiten haalt. Vul \(x = 0\) in: "
                  r"links staat \(1\), rechts \(2\).", 3),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(\sin\alpha\) kan groter zijn dan \(1\).", False),
                 ("waar", r"\(\pi\) radialen is \(180^\circ\).", True),
                 ("waar", "De amplitude van een sinusfunctie kan negatief zijn.", False),
                 ("waar", r"\(\tan\alpha\) blijft altijd tussen \(-1\) en \(1\).", False),
                 ("waar", r"De grafiek van \(y = \sin x\) is symmetrisch om de oorsprong.", True),
                 ("waar", "Een identiteit bewijs je door er een paar hoeken in te vullen.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-limieten-continuiteit-en-asymptoten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Limieten, continuïteit en asymptoten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Limieten berekenen",
             opdracht="Vul eerst in. Krijg je een onbepaaldheid, schrijf dan eerst om.",
             oefeningen=[
                 ("rij", [(r"\(\lim\limits_{x \to 4} (2x - 3)\)", r"\(5\)"),
                          (r"\(\lim\limits_{x \to 3} \dfrac{x^{2} - 9}{x - 3}\)", r"\(6\)"),
                          (r"\(\lim\limits_{x \to +\infty} \dfrac{5x^{2}}{x^{2} + 1}\)", r"\(5\)"),
                          (r"\(\lim\limits_{x \to +\infty} \dfrac{3x + 2}{x^{3}}\)", r"\(0\)")],
                  "Bereken de limiet.", W),
                 ("rij", [(r"\(\lim\limits_{x \to 1} \dfrac{x^{2} - 1}{x - 1}\)", r"\(2\)"),
                          (r"\(\lim\limits_{x \to -\infty} \dfrac{x^{3} + 2}{x^{2}}\)", r"\(-\infty\)"),
                          (r"\(\lim\limits_{x \to 0^{+}} \dfrac{1}{x}\)", r"\(+\infty\)")],
                  "Bereken de limiet.", W),
                 ("open", r"Leg uit waarom \(\lim\limits_{x \to 0} \dfrac{1}{x}\) niet bestaat en \(\lim\limits_{x \to 0} \dfrac{1}{x^{2}}\) wel.",
                  r"Bij \(\dfrac{1}{x}\) gaat de linkerlimiet naar \(-\infty\) en de rechter naar "
                  r"\(+\infty\); ze verschillen. Bij het kwadraat is de noemer langs beide kanten "
                  r"positief, dus allebei naar \(+\infty\).", 4),
             ]),
        dict(kop="Onbepaaldheden herkennen",
             opdracht="Vul aan: is het een onbepaaldheid, en welke aanpak past?",
             oefeningen=[
                 ("tabel", ["Vorm", "Onbepaaldheid?", "Wat je doet"],
                  [[r"\(\dfrac{0}{0}\)", None, None], [r"\(\dfrac{2}{0}\)", None, None],
                   [r"\(\dfrac{\infty}{\infty}\)", None, None], [r"\(0 \cdot \infty\)", None, None]],
                  "ja, ontbinden of l'Hôpital; nee, dat is een pool; ja, hoogste graden afwegen of "
                  "l'Hôpital; ja, eerst omvormen tot een breuk", "210px"),
             ]),
        dict(kop="Met de regel van de l'Hôpital",
             opdracht="Leid teller en noemer apart af, en vul dan pas in.",
             oefeningen=[
                 ("kort", r"\(\lim\limits_{x \to 0} \dfrac{\sin x}{x}\)",
                  r"\(\lim\limits_{x \to 0} \dfrac{\cos x}{1} = 1\).", WW),
                 ("kort", r"\(\lim\limits_{x \to 2} \dfrac{x^{2} - 4}{x^{2} - 3x + 2}\)",
                  r"\(\dfrac{2x}{2x - 3} = \dfrac{4}{1} = 4\).", WW),
                 ("kort", r"\(\lim\limits_{x \to +\infty} \dfrac{\ln x}{x}\)",
                  r"\(\dfrac{1/x}{1} \to 0\).", WW),
             ]),
        dict(kop="Continuïteit",
             opdracht="Zeg of de functie continu is in het gegeven punt, en waarom.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = x^{2} + 1\) in \(0\)", "ja, een veeltermfunctie is overal continu"),
                          (r"\(f(x) = \dfrac{1}{x}\) in \(0\)", "nee, ze bestaat daar niet"),
                          (r"\(f(x) = |x|\) in \(0\)", "ja, continu, al is er een knik"),
                          (r"\(f(x) = \sqrt{x}\) in \(4\)", "ja")],
                  "Continu?", WL),
                 ("open", r"Noem de drie voorwaarden waaraan \(f\) moet voldoen om continu te zijn in \(a\).",
                  r"\(\lim\limits_{x \to a} f(x)\) bestaat, \(f(a)\) bestaat, en ze zijn aan elkaar gelijk.", 3),
             ]),
        dict(kop="Asymptoten zoeken",
             opdracht="Vul de tabel aan. Een rechte die er niet is, laat je leeg.",
             oefeningen=[
                 ("tabel", ["Functie", "Verticale asymptoot", "Horizontale of schuine asymptoot"],
                  [[r"\(\dfrac{1}{x - 4}\)", None, None],
                   [r"\(\dfrac{2x + 1}{x - 3}\)", None, None],
                   [r"\(\dfrac{x^{2} + 1}{x}\)", None, None],
                   [r"\(\dfrac{x^{2} - 1}{x + 2}\)", None, None]],
                  r"\(x = 4\) en \(y = 0\); \(x = 3\) en \(y = 2\); \(x = 0\) en \(y = x\); "
                  r"\(x = -2\) en \(y = x - 2\)", "200px"),
                 ("open", r"Wanneer heeft een rationale functie een schuine asymptoot? Leg ook uit hoe je ze vindt met een euclidische deling.",
                  r"Als de graad van de teller precies één hoger is dan die van de noemer. Je deelt "
                  r"uit; het quotiënt is de vergelijking van de asymptoot, want de rest gedeeld "
                  r"door de noemer kruipt naar nul.", 4),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De regel van de l'Hôpital mag je toepassen op \(\dfrac{2}{0}\).", False),
                 ("waar", "Een grafiek mag haar horizontale asymptoot snijden.", True),
                 ("waar", "Een gewone parabool heeft een horizontale asymptoot.", False),
                 ("waar", r"Een functie moet in \(a\) gedefinieerd zijn om daar een limiet te hebben.", False),
                 ("waar", "Een functie die afleidbaar is in een punt, is daar ook continu.", True),
                 ("waar", "Een verticale asymptoot kan je grafiek snijden.", False),
                 ("waar", "Asymptoten teken je als stippellijnen.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-afgeleiden-en-het-verloop-van-een-functie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Afgeleiden en het verloop van een functie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Afleiden",
             opdracht="Leid af. Noteer bij een product, een quotiënt of een samenstelling welke regel je gebruikt.",
             oefeningen=[
                 ("rij", [(r"\(x^{5}\)", r"\(5x^{4}\)"),
                          (r"\(7x - 3\)", r"\(7\)"),
                          (r"\(\sin x\)", r"\(\cos x\)"),
                          (r"\(\cos x\)", r"\(-\sin x\)")],
                  "Leid af.", WW),
                 ("rij", [(r"\(e^{x}\)", r"\(e^{x}\)"),
                          (r"\(\ln x\)", r"\(\dfrac{1}{x}\)"),
                          (r"\(x^{2}\sin x\)", r"\(2x\sin x + x^{2}\cos x\)"),
                          (r"\(\left(2x + 1\right)^{3}\)", r"\(6\left(2x + 1\right)^{2}\)")],
                  "Leid af.", WL),
             ]),
        dict(kop="Product, quotiënt en ketting",
             opdracht="Leid af en schrijf erbij welke regel je gebruikt.",
             oefeningen=[
                 ("rij", [(r"\(\dfrac{x}{x + 1}\)", r"\(\dfrac{1}{\left(x+1\right)^{2}}\)"),
                          (r"\(\sqrt{x}\)", r"\(\dfrac{1}{2\sqrt{x}}\)"),
                          (r"\(\sin 3x\)", r"\(3\cos 3x\)")],
                  "Leid af.", WL),
                 ("open", r"Toon met \(f(x) = x \cdot x\) aan dat de afgeleide van een product niet het product van de afgeleiden is.",
                  r"\(x \cdot x = x^{2}\), met afgeleide \(2x\). Het product van de afgeleiden zou "
                  r"\(1 \cdot 1 = 1\) zijn. Daarom bestaat de productregel.", 3),
             ]),
        dict(kop="De raaklijn",
             opdracht="Stel de vergelijking van de raaklijn op. Schrijf eerst de helling, dan het raakpunt.",
             oefeningen=[
                 ("open", r"Stel de raaklijn op aan \(f(x) = x^{2}\) in \(x = -2\).",
                  r"\(f'(x) = 2x\), dus de helling is \(-4\). Het raakpunt is \((-2,\ 4)\). "
                  r"Invullen: \(4 = 8 + q\), dus \(q = -4\). De raaklijn is \(y = -4x - 4\).", 4),
                 ("kort", r"Wat stelt \(s'(t)\) voor als \(s(t)\) de afgelegde weg is?",
                  "de snelheid op dat ogenblik", WL),
                 ("kort", r"Hoeveel is de gemiddelde verandering van \(x^{2}\) tussen \(2\) en \(4\)?",
                  r"\(6\)", W),
                 ("kort", r"Hoeveel is \(f'(1)\) voor \(f(x) = x^{3} - 3x\)?",
                  r"\(0\)", W),
             ]),
        dict(kop="Het verloop onderzoeken",
             opdracht="Bereken de afgeleide, zoek haar nulwaarden en maak een tekenschema.",
             oefeningen=[
                 ("open", r"Onderzoek het verloop van \(f(x) = x^{3} - 12x\): zoek de extrema en zeg bij elk of het een maximum of een minimum is.",
                  r"\(f'(x) = 3x^{2} - 12\), nul in \(-2\) en \(2\). \(f''(x) = 6x\) is negatief in "
                  r"\(-2\), dus daar een maximum, en positief in \(2\), dus daar een minimum.", 5),
                 ("tabel", ["Wat geldt", "Wat besluit je"],
                  [[r"\(f'(x) > 0\) op een interval", None],
                   [r"\(f'(a) = 0\) en \(f'\) wisselt van min naar plus", None],
                   [r"\(f''(x) > 0\) op een interval", None],
                   [r"\(f''(a) = 0\) en \(f''\) wisselt van teken", None]],
                  "de functie stijgt; een minimum; de grafiek is hol; een buigpunt", "240px"),
             ]),
        dict(kop="Een extremumprobleem",
             opdracht="Kies zelf een veranderlijke, stel het voorschrift op, en vergeet het praktisch domein niet.",
             oefeningen=[
                 ("open", r"Je hebt \(40\) m omheining voor een rechthoekige moestuin. Welke afmetingen geven de grootste oppervlakte?",
                  r"Noem de breedte \(x\). De lengte is \(20 - x\), dus "
                  r"\(O(x) = 20x - x^{2}\). \(O'(x) = 20 - 2x\) is nul in \(x = 10\). Een vierkant "
                  r"van \(10\) op \(10\) m, met \(100\ \text{m}^{2}\).", 5),
                 ("open", "Waarom moet je bij zo'n opgave nagaan of je oplossing in het praktisch domein ligt?",
                  r"Een negatieve of te grote lengte is wiskundig misschien een oplossing, maar "
                  r"past niet in de opgave. Hier moet \(x\) tussen \(0\) en \(20\) liggen.", 3),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Elk punt waar \(f'(x) = 0\) is een extremum.", False),
                 ("waar", "Een functie kan een maximum bereiken in een punt waar ze niet afleidbaar is.", True),
                 ("waar", r"\(\left(e^{x}\right)' = x\,e^{x-1}\).", False),
                 ("waar", r"In een buigpunt is \(f'\) altijd nul.", False),
                 ("waar", r"Als \(f' > 0\) en \(f'' < 0\), dan stijgt de functie steeds trager.", True),
                 ("waar", r"De stelling van Rolle eist \(f(a) = f(b)\).", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-rijen-en-hun-limiet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rijen en hun limiet",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rekenkundig of meetkundig",
             opdracht=r"Kijk naar \(u_{n+1} - u_{n}\) én naar \(\dfrac{u_{n+1}}{u_{n}}\).",
             oefeningen=[
                 ("tabel", ["Rij", "Soort", r"\(d\) of \(q\)"],
                  [[r"\(2,\ 9,\ 16,\ 23,\ \dots\)", None, None],
                   [r"\(3,\ 12,\ 48,\ 192,\ \dots\)", None, None],
                   [r"\(100,\ 50,\ 25,\ 12{,}5,\ \dots\)", None, None],
                   [r"\(20,\ 17,\ 14,\ 11,\ \dots\)", None, None],
                   [r"\(5,\ -10,\ 20,\ -40,\ \dots\)", None, None]],
                  r"rekenkundig, \(d = 7\); meetkundig, \(q = 4\); meetkundig, "
                  r"\(q = \tfrac{1}{2}\); rekenkundig, \(d = -3\); meetkundig, \(q = -2\)",
                  "160px"),
             ]),
        dict(kop="Het expliciete voorschrift",
             opdracht=r"Gebruik \(u_{n} = u_{1} + (n-1)\,d\) of \(u_{n} = u_{1} \cdot q^{\,n-1}\), "
                      r"en werk uit tot er geen haakjes meer staan.",
             oefeningen=[
                 ("rij", [(r"\(2,\ 9,\ 16,\ 23,\ \dots\)", r"\(u_{n} = 7n - 5\)"),
                          (r"\(3,\ 12,\ 48,\ \dots\)", r"\(u_{n} = 3 \cdot 4^{\,n-1}\)"),
                          (r"\(20,\ 17,\ 14,\ \dots\)", r"\(u_{n} = 23 - 3n\)"),
                          (r"\(1,\ \tfrac{1}{2},\ \tfrac{1}{4},\ \dots\)",
                           r"\(u_{n} = \left(\tfrac{1}{2}\right)^{\,n-1}\)")],
                  r"Schrijf het expliciete voorschrift \(u_{n}\).", WL),
             ]),
        dict(kop="Termen berekenen",
             opdracht="Schrijf eerst de formule op die je gebruikt, en vul dan pas in.",
             oefeningen=[
                 ("kort", r"\(u_{1} = 5\) en \(d = 3\). Hoeveel is \(u_{20}\)?", r"\(62\)", W),
                 ("kort", r"\(u_{1} = 3\) en \(q = 2\). Hoeveel is \(u_{6}\)?", r"\(96\)", W),
                 ("kort", r"\(u_{n} = 4n - 1\). Hoeveel is \(u_{12}\)?", r"\(47\)", W),
                 ("kort", r"\(u_{1} = 64\) en \(q = \tfrac{1}{2}\). Hoeveel is \(u_{7}\)?",
                  r"\(1\)", W),
             ]),
        dict(kop="Sommen berekenen",
             opdracht=r"Zoek eerst \(u_{n}\) of het aantal termen, en vul dan de somformule in.",
             oefeningen=[
                 ("kort", r"Hoeveel is \(1 + 2 + 3 + \dots + 100\)?", r"\(5050\)", W),
                 ("kort", r"Hoeveel is \(2 + 4 + 6 + \dots + 50\)?", r"\(650\)", W),
                 ("kort", r"\(u_{1} = 5\) en \(d = 3\). Hoeveel is \(S_{10}\)?", r"\(185\)", W),
                 ("kort", r"\(u_{1} = 3\) en \(q = 2\). Hoeveel is \(S_{6}\)?", r"\(189\)", W),
             ]),
        dict(kop="Terugrekenen",
             opdracht="Hier is het gevraagde getal niet de term maar het vaste getal zelf. "
                      "Stel een vergelijking op.",
             oefeningen=[
                 ("kort", r"Rekenkundig: \(u_{3} = 11\) en \(u_{7} = 27\). Hoeveel is \(d\)?",
                  r"\(d = \dfrac{27 - 11}{4} = 4\)", WW),
                 ("kort", r"Meetkundig: \(u_{2} = 6\) en \(u_{5} = 162\). Hoeveel is \(q\)?",
                  r"\(q^{3} = 27\), dus \(q = 3\)", WW),
                 ("kort", r"\(u_{1} = 4\) en \(d = 5\). Vanaf welke \(n\) is \(u_{n} > 100\)?",
                  r"\(5n - 1 > 100\), dus vanaf \(n = 21\)", WW),
             ]),
        dict(kop="Limieten",
             opdracht="Schrijf de limiet op, of noteer dat ze niet bestaat.",
             oefeningen=[
                 ("rij", [(r"\(\lim\limits_{n \to +\infty} \dfrac{2}{n}\)", r"\(0\)"),
                          (r"\(\lim\limits_{n \to +\infty} \dfrac{3n - 1}{n}\)", r"\(3\)"),
                          (r"\(\lim\limits_{n \to +\infty} \dfrac{5n^{2} + n}{n^{2}}\)", r"\(5\)"),
                          (r"\(\lim\limits_{n \to +\infty} 3^{\,n}\)", r"\(+\infty\)"),
                          (r"\(\lim\limits_{n \to +\infty} (-1)^{n}\)", "bestaat niet")],
                  "Hoeveel is de limiet?", WW),
             ]),
        dict(kop="De oneindige meetkundige som",
             opdracht=r"Ga eerst na of \(|q| < 1\). Bereken de som dan met "
                      r"\(S = \dfrac{u_{1}}{1 - q}\).",
             oefeningen=[
                 ("tabel", ["Rij", "Bestaat de som?", "Zo ja, hoeveel"],
                  [[r"\(1,\ \tfrac{1}{3},\ \tfrac{1}{9},\ \dots\)", None, None],
                   [r"\(2,\ 1,\ \tfrac{1}{2},\ \dots\)", None, None],
                   [r"\(1,\ 2,\ 4,\ 8,\ \dots\)", None, None],
                   [r"\(9,\ -3,\ 1,\ \dots\)", None, None]],
                  r"ja, \(\tfrac{3}{2}\); ja, \(4\); nee, \(|q| = 2\); ja, \(\tfrac{27}{4}\)",
                  "160px"),
                 ("kort", r"Schrijf \(0{,}363636\dots\) als een breuk.",
                  r"\(\dfrac{36/100}{1 - 1/100} = \dfrac{4}{11}\)", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", r"De punten \((n,\ u_{n})\) van een rekenkundige rij liggen op een rechte.", True),
                 ("waar", r"Een divergente rij kan naar \(+\infty\) gaan.", True),
                 ("waar", r"Een rekenkundige rij met \(d = 3\) convergeert.", False),
                 ("waar", "Elke oneindige meetkundige rij heeft een eindige som.", False),
                 ("waar", r"Bij \(q = 1\) is een meetkundige rij constant.", True),
                 ("waar", r"Een meetkundige rij met \(q < 0\) is alternerend.", True),
                 ("waar", r"De formule \(S_{n} = u_{1} \cdot \dfrac{1 - q^{\,n}}{1 - q}\) werkt ook als \(q = 1\).", False),
                 ("waar", r"Het getal \(0{,}999\dots\) is net iets kleiner dan \(1\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de formule of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom je bij \(u_{10}\) van een rekenkundige rij negen keer "
                          r"\(d\) optelt en niet tien keer.",
                  r"\(u_{1}\) staat er al. Van de eerste naar de tiende term zet je negen stappen, "
                  r"dus \(u_{10} = u_{1} + 9d\).", 3),
                 ("open", r"Een bal valt van twee meter en stuitert telkens tot \(60\%\) van de "
                          r"vorige hoogte. Kan je de totale hoogte van alle sprongen berekenen? Leg uit.",
                  r"Ja. De sprongen vormen een meetkundige rij met \(q = 0{,}6\), en omdat "
                  r"\(|q| < 1\) bestaat de oneindige som. Oneindig veel sprongen geven samen een "
                  r"eindige hoogte.", 3),
                 ("open", r"Leg uit waarom \(\lim\limits_{n \to +\infty} \dfrac{3n - 1}{n} = 3\) "
                          r"en niet \(+\infty\), hoewel teller en noemer allebei onbeperkt groeien.",
                  r"Splits op: \(\dfrac{3n-1}{n} = 3 - \dfrac{1}{n}\). De tweede term kruipt naar "
                  r"nul, dus blijft \(3\) over. Het gaat om de verhouding, niet om de grootte.", 3),
                 ("open", "Leg uit waarom je bij een rij alleen over de limiet op oneindig spreekt.",
                  r"Een rij is alleen gedefinieerd voor \(n \in \mathbb{N}\). Tussen \(u_{3}\) en "
                  r"\(u_{4}\) ligt niets, dus er is geen tussenwaarde om naartoe te kruipen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-primitieven-en-de-onbepaalde-integraal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Primitieven en de onbepaalde integraal",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Basisprimitieven",
             opdracht=r"Zoek een primitieve. Vergeet \(+\,C\) niet, en controleer door af te leiden.",
             oefeningen=[
                 ("rij", [(r"\(\int x^{4}\,dx\)", r"\(\dfrac{x^{5}}{5} + C\)"),
                          (r"\(\int 6\,dx\)", r"\(6x + C\)"),
                          (r"\(\int \sin x\,dx\)", r"\(-\cos x + C\)"),
                          (r"\(\int \dfrac{1}{x}\,dx\)", r"\(\ln|x| + C\)"),
                          (r"\(\int e^{x}\,dx\)", r"\(e^{x} + C\)"),
                          (r"\(\int \cos x\,dx\)", r"\(\sin x + C\)")],
                  "Geef een primitieve.", WL),
             ]),
        dict(kop="Lineariteit",
             opdracht="Splits de integrand en haal constanten buiten het integraalteken.",
             oefeningen=[
                 ("rij", [(r"\(\int (4x + 3)\,dx\)", r"\(2x^{2} + 3x + C\)"),
                          (r"\(\int 6x^{2}\,dx\)", r"\(2x^{3} + C\)"),
                          (r"\(\int \left(x - \cos x\right)dx\)",
                           r"\(\dfrac{x^{2}}{2} - \sin x + C\)"),
                          (r"\(\int 5\,e^{x}\,dx\)", r"\(5\,e^{x} + C\)")],
                  "Geef een primitieve.", WL),
             ]),
        dict(kop="Eerst herschrijven",
             opdracht=r"Schrijf de integrand eerst als een macht of als een som, en integreer dan pas.",
             oefeningen=[
                 ("kort", r"\(\int \dfrac{1}{x^{2}}\,dx\)", r"\(-\dfrac{1}{x} + C\)", WW),
                 ("kort", r"\(\int \sqrt{x}\,dx\)", r"\(\dfrac{2}{3}x\sqrt{x} + C\)", WW),
                 ("kort", r"\(\int \dfrac{3}{x}\,dx\)", r"\(3\ln|x| + C\)", WW),
                 ("kort", r"\(\int \dfrac{x^{2} + 1}{x}\,dx\)",
                  r"\(\dfrac{x^{2}}{2} + \ln|x| + C\)", WW),
             ]),
        dict(kop="Welke methode",
             opdracht="Kruis aan welke methode het eerst past: onmiddellijk, splitsen, "
                      "substitutie of partiële integratie.",
             oefeningen=[
                 ("tabel", ["Integraal", "Methode"],
                  [[r"\(\int \left(3x^{2} - 4x\right)dx\)", None],
                   [r"\(\int x\sin x\,dx\)", None],
                   [r"\(\int 2x\,e^{x^{2}}\,dx\)", None],
                   [r"\(\int \cos x\,dx\)", None],
                   [r"\(\int \dfrac{3x^{2}}{x^{3} + 5}\,dx\)", None]],
                  "splitsen; partiële integratie; substitutie; onmiddellijk; substitutie",
                  "230px"),
             ]),
        dict(kop="Substitutie",
             opdracht=r"Zoek de binnenste functie \(u\) waarvan de afgeleide er ook staat.",
             oefeningen=[
                 ("kort", r"\(\int 2x\,e^{x^{2}}\,dx\)", r"\(e^{x^{2}} + C\)", WW),
                 ("kort", r"\(\int \dfrac{2x}{x^{2} + 1}\,dx\)", r"\(\ln\left(x^{2}+1\right) + C\)", WW),
                 ("kort", r"\(\int (x + 1)^{5}\,dx\)", r"\(\dfrac{(x+1)^{6}}{6} + C\)", WW),
             ]),
        dict(kop="Partiële integratie",
             opdracht=r"Gebruik \(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\), en kies \(u\) zo dat "
                      r"\(u'\) eenvoudiger wordt.",
             oefeningen=[
                 ("kort", r"\(\int x\,e^{x}\,dx\)", r"\(x\,e^{x} - e^{x} + C\)", WL),
                 ("kort", r"\(\int x\cos x\,dx\)", r"\(x\sin x + \cos x + C\)", WL),
             ]),
        dict(kop="Bepaalde integralen",
             opdracht="Zoek een primitieve, vul de twee grenzen in en trek af.",
             oefeningen=[
                 ("rij", [(r"\(\int_{0}^{3} 2x\,dx\)", r"\(9\)"),
                          (r"\(\int_{1}^{2} x^{2}\,dx\)", r"\(\dfrac{7}{3}\)"),
                          (r"\(\int_{0}^{\pi/2} \cos x\,dx\)", r"\(1\)"),
                          (r"\(\int_{5}^{5} f(x)\,dx\)", r"\(0\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="Met e en met π",
             opdracht="Dezelfde werkwijze, maar nu met grenzen die zelf een getal als e of pi zijn.",
             oefeningen=[
                 ("kort", r"\(\int_{0}^{\pi} \sin x\,dx\)", r"\(2\)", W),
                 ("kort", r"\(\int_{1}^{e} \dfrac{1}{x}\,dx\)", r"\(1\)", W),
                 ("kort", r"\(\int_{0}^{1} e^{x}\,dx\)", r"\(e - 1\)", W),
             ]),
        dict(kop="Waar of niet waar: primitieven",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Twee primitieven van dezelfde functie hebben dezelfde afgeleide.", True),
                 ("waar", r"Een factor met een \(x\) erin mag je voor het integraalteken zetten.", False),
                 ("waar", "Na een substitutie in een bepaalde integraal mag je de oude grenzen laten staan.", False),
                 ("waar", r"\(\int \sin x\,dx = -\cos x + C\).", True),
             ]),
        dict(kop="Waar of niet waar: methodes",
             opdracht="Nog vier uitspraken, over de regels en de methodes.",
             oefeningen=[
                 ("waar", "Elke continue functie heeft een primitieve.", True),
                 ("waar", r"\(\int x^{-1}\,dx = \dfrac{x^{0}}{0} + C\).", False),
                 ("waar", "Partiële integratie volgt uit de productregel voor afgeleiden.", True),
                 ("waar", "Een integraal met een wortel erin kan je nooit met substitutie oplossen.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom \(\int x^{n}\,dx = \dfrac{x^{\,n+1}}{n+1} + C\) niet "
                          r"werkt voor \(n = -1\).",
                  r"Je zou delen door \(n + 1 = 0\). Net die ene integraal geeft \(\ln|x| + C\).", 3),
                 ("open", "Wat moet er in de integrand staan voor je een substitutie kan uitvoeren?",
                  r"Een binnenste functie waarvan ook de afgeleide in de integrand staat. Zonder "
                  r"die afgeleide kan je \(dx\) niet omzetten naar \(du\).", 3),
                 ("open", r"Leg uit waarom je bij een bepaalde integraal geen \(+\,C\) schrijft.",
                  r"\(\left(F(b) + C\right) - \left(F(a) + C\right) = F(b) - F(a)\): dezelfde "
                  r"constante komt er in de bovengrens bij en in de ondergrens weer af.", 3),
                 ("open", "Hoe controleer je of je primitieve klopt, en waarom is dat een echte controle?",
                  r"Leid je antwoord af; je moet de integrand terugkrijgen. Afleiden is eenduidig, "
                  r"terwijl opnieuw integreren vaak dezelfde fout herhaalt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-bepaalde-integraal-en-haar-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De bepaalde integraal en haar toepassingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Riemannsommen",
             opdracht="Vul in. Denk aan de laagste en de hoogste functiewaarde per stukje.",
             oefeningen=[
                 ("tabel", ["Som", "Welke functiewaarde per stukje", "Groter of kleiner"],
                  [["ondersom", None, None], ["bovensom", None, None]],
                  "de laagste, dus kleiner; de hoogste, dus groter", "200px"),
                 ("kort", r"Waarmee komt de \(dx\) overeen bij de rechthoekjes?",
                  "met hun breedte", WW),
             ]),
        dict(kop="Snel uitrekenen",
             opdracht="Zoek een primitieve, vul de grenzen in en trek af.",
             oefeningen=[
                 ("rij", [(r"\(\int_{0}^{4} 3\,dx\)", r"\(12\)"),
                          (r"\(\int_{1}^{3} x\,dx\)", r"\(4\)"),
                          (r"\(\int_{0}^{2} x^{3}\,dx\)", r"\(4\)"),
                          (r"\(\int_{1}^{4} \dfrac{1}{\sqrt{x}}\,dx\)", r"\(2\)"),
                          (r"\(\int_{0}^{\pi/2} \sin x\,dx\)", r"\(1\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="Met de hoofdstelling",
             opdracht=r"Schrijf eerst \(\left[F(x)\right]_{a}^{b}\) op, en vul dan pas in.",
             oefeningen=[
                 ("kort", r"\(\int_{0}^{1} e^{2x}\,dx\)", r"\(\dfrac{e^{2} - 1}{2}\)", WW),
                 ("kort", r"\(\int_{1}^{e} \dfrac{\ln x}{x}\,dx\)", r"\(\dfrac{1}{2}\)", WW),
                 ("kort", r"\(\int_{-1}^{1} x^{2}\,dx\)", r"\(\dfrac{2}{3}\)", WW),
                 ("kort", r"\(\int_{0}^{1} \dfrac{2x}{x^{2} + 1}\,dx\)", r"\(\ln 2\)", WW),
             ]),
        dict(kop="Georiënteerd of werkelijk",
             opdracht="Reken de integraal uit, en kijk daarna of dat ook de werkelijke oppervlakte is.",
             oefeningen=[
                 ("kort", r"\(\int_{-1}^{1} x^{3}\,dx\)", r"\(0\)", W),
                 ("kort", r"\(\int_{0}^{2\pi} \sin x\,dx\)", r"\(0\)", W),
                 ("kort", r"De werkelijke oppervlakte tussen \(y = x^{3}\) en de x-as op \([-1,\ 1]\)",
                  r"\(2 \cdot \tfrac{1}{4} = \tfrac{1}{2}\)", WW),
             ]),
        dict(kop="Oppervlakte tussen twee krommen",
             opdracht="Maak eerst een schets, zoek de snijpunten, en integreer de bovenste min de onderste.",
             oefeningen=[
                 ("kort", r"Tussen \(y = 2x\) en \(y = x^{2}\), tussen hun snijpunten",
                  r"snijpunten \(0\) en \(2\); \(4 - \tfrac{8}{3} = \tfrac{4}{3}\)", WL),
                 ("kort", r"Tussen \(y = x\) en \(y = x^{3}\) op \([0,\ 1]\)",
                  r"\(\tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}\)", WL),
             ]),
        dict(kop="Omwenteling en booglengte",
             opdracht=r"Gebruik \(V = \pi\int_{a}^{b} f(x)^{2}dx\) en "
                      r"\(L = \int_{a}^{b}\sqrt{1 + f'(x)^{2}}\,dx\).",
             oefeningen=[
                 ("kort", r"Inhoud als \(y = x\) op \([0,\ 1]\) om de x-as draait",
                  r"\(\pi\int_{0}^{1} x^{2}dx = \dfrac{\pi}{3}\)", WL),
                 ("kort", r"Inhoud als \(y = 2\) op \([0,\ 3]\) om de x-as draait",
                  r"\(\pi\int_{0}^{3} 4\,dx = 12\pi\)", WL),
                 ("kort", r"Schrijf de booglengte-integraal op van \(y = x^{2}\) op \([0,\ 1]\)",
                  r"\(\int_{0}^{1}\sqrt{1 + 4x^{2}}\,dx\)", WL),
             ]),
        dict(kop="Toepassingen",
             opdracht="Schrijf telkens op wat je integreert, en controleer de eenheid van je antwoord.",
             oefeningen=[
                 ("tabel", ["Wat je integreert", "Wat je krijgt"],
                  [["de snelheid over de tijd", None], ["de versnelling over de tijd", None],
                   ["het debiet van een kraan over de tijd", None],
                   ["de marginale kost over een aantal stuks", None]],
                  "de verplaatsing; de verandering van de snelheid; de totale hoeveelheid water; "
                  "de toename van de totale kost", "280px"),
                 ("kort", r"Een kraan geeft \(0{,}5\) liter per seconde, \(40\) s lang. Hoeveel liter?",
                  r"\(20\) l", WW),
                 ("kort", r"\(v(t) = 3t\) m/s. Welke verplaatsing tussen \(t = 0\) en \(t = 4\) s?",
                  r"\(\left[1{,}5\,t^{2}\right]_{0}^{4} = 24\) m", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Een ondersom is nooit groter dan de werkelijke oppervlakte.", True),
                 ("waar", "Hoe meer deelintervallen je neemt, hoe beter de benadering.", True),
                 ("waar", "Een werkelijke oppervlakte kan negatief zijn.", False),
                 ("waar", r"\(\int_{b}^{a} f(x)\,dx = -\int_{a}^{b} f(x)\,dx\).", True),
                 ("waar", "De hoofdstelling geldt ook voor een functie met een sprong.", False),
                 ("waar", "De bovengrens van een integraal is de grootste functiewaarde.", False),
                 ("waar", "De inhoud van een omwentelingslichaam hangt af van de as waarrond je draait.", True),
                 ("waar", r"\(\int_{a}^{a} f(x)\,dx = f(a)\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", "Leg uit waarom de limiet van Riemannsommen een exacte oppervlakte geeft.",
                  "De werkelijke oppervlakte ligt altijd tussen de onder- en de bovensom. Kruipen "
                  "die twee naar hetzelfde getal, dan blijft er maar één mogelijkheid over.", 3),
                 ("open", r"Een wagen rijdt eerst vooruit en daarna een stuk achteruit. Geeft "
                          r"\(\int v\,dt\) de afgelegde weg? Leg uit.",
                  "Nee, de verplaatsing. Achteruit is de snelheid negatief, en die trekt de "
                  "integraal af. Voor de afgelegde weg neem je de stukken positief.", 3),
                 ("open", "Waarom maak je eerst een schets bij een oppervlakte tussen twee krommen?",
                  "Om te zien welke kromme boven ligt en waar ze elkaar snijden. Zonder schets zet "
                  "je de twee in de verkeerde volgorde en krijg je een negatieve uitkomst.", 3),
                 ("open", "Leg uit waarom je bij een omwentelingslichaam de functie kwadrateert.",
                  r"Elke dunne schijf is een cirkel met straal \(f(x)\), en de oppervlakte van een "
                  r"cirkel is \(\pi r^{2}\). Die straal staat dus in het kwadraat.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-complexe-getallen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Complexe getallen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Machten van i",
             opdracht=r"Reken uit. De machten van \(i\) herhalen zich om de vier.",
             oefeningen=[
                 ("rij", [(r"\(i^{5}\)", r"\(i\)"), (r"\(i^{6}\)", r"\(-1\)"),
                          (r"\(i^{7}\)", r"\(-i\)"), (r"\(i^{8}\)", r"\(1\)"),
                          (r"\(i^{11}\)", r"\(-i\)")],
                  "Reken uit.", W),
             ]),
        dict(kop="Optellen en vermenigvuldigen",
             opdracht=r"Werk uit en schrijf het antwoord als \(a + bi\).",
             oefeningen=[
                 ("rij", [(r"\(\left(4 + i\right) + \left(2 - 3i\right)\)", r"\(6 - 2i\)"),
                          (r"\(\left(2 - i\right) - \left(1 + 2i\right)\)", r"\(1 - 3i\)"),
                          (r"\(\overline{5 - 2i}\)", r"\(5 + 2i\)"),
                          (r"\(\left(2 - i\right)^{2}\)", r"\(3 - 4i\)")],
                  "Reken uit.", WL),
             ]),
        dict(kop="Delen door een complex getal",
             opdracht="Vermenigvuldig teller en noemer met de toegevoegde van de noemer.",
             oefeningen=[
                 ("kort", r"\(\dfrac{1}{2 + i}\)", r"\(\dfrac{2}{5} - \dfrac{1}{5}i\)", WW),
                 ("kort", r"\(\dfrac{3 + i}{1 - i}\)", r"\(1 + 2i\)", WW),
                 ("kort", r"\(\dfrac{i}{1 + i}\)", r"\(\dfrac{1}{2} + \dfrac{1}{2}i\)", WW),
             ]),
        dict(kop="Modulus en argument",
             opdracht="Vul de tabel aan. Een modulus is een afstand en dus nooit negatief.",
             oefeningen=[
                 ("tabel", ["Getal", "Modulus", "Argument in graden"],
                  [[r"\(3\)", None, None], [r"\(-2\)", None, None],
                   [r"\(4i\)", None, None], [r"\(1 + i\)", None, None],
                   [r"\(-i\)", None, None]],
                  r"\(3\) en \(0^\circ\); \(2\) en \(180^\circ\); \(4\) en \(90^\circ\); "
                  r"\(\sqrt{2}\) en \(45^\circ\); \(1\) en \(270^\circ\)", "150px"),
                 ("kort", r"\(|6 - 8i|\)", r"\(10\)", W),
                 ("kort", r"\(|-5 + 12i|\)", r"\(13\)", W),
             ]),
        dict(kop="Wat de bewerkingen in het vlak doen",
             opdracht="Antwoord in één zin, met de draai of de spiegeling erbij.",
             oefeningen=[
                 ("kort", r"Wat doet een vermenigvuldiging met \(i\) met een punt?",
                  "het draait een kwart slag rond de oorsprong", WL),
                 ("kort", r"Wat doet \(z \mapsto \overline{z}\) met een punt?",
                  "het spiegelt om de reële as", WL),
             ]),
        dict(kop="Goniometrische vorm en de Moivre",
             opdracht=r"Werk met \(r\) en \(\theta\). Bij machten gebruik je de formule van de Moivre.",
             oefeningen=[
                 ("tabel", ["Bewerking", "Met de moduli", "Met de argumenten"],
                  [["vermenigvuldigen", None, None], ["delen", None, None],
                   [r"tot de macht \(n\)", None, None]],
                  r"vermenigvuldigen en optellen; delen en aftrekken; tot de macht \(n\) en met "
                  r"\(n\) vermenigvuldigen", "180px"),
                 ("kort", r"Schrijf \(1 + i\) in goniometrische vorm.",
                  r"\(\sqrt{2}\left(\cos 45^\circ + i\sin 45^\circ\right)\)", WL),
                 ("kort", r"Bereken \(\left(1 + i\right)^{8}\) met de Moivre.",
                  r"\(\left(\sqrt{2}\right)^{8} = 16\) en \(8 \cdot 45^\circ = 360^\circ\), dus \(16\)", WL),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht=r"Los op in \(\mathbb{C}\). Vergeet de tweede oplossing niet.",
             oefeningen=[
                 ("kort", r"\(x^{2} + 9 = 0\)", r"\(x = 3i\) of \(x = -3i\)", WW),
                 ("kort", r"\(x^{2} - 4x + 13 = 0\)", r"\(x = 2 \pm 3i\)", WW),
                 ("kort", r"Hoeveel oplossingen heeft \(z^{5} = 1\) in \(\mathbb{C}\)?", r"\(5\)", W),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Je kan twee complexe getallen van klein naar groot ordenen.", False),
                 ("waar", "Elk reëel getal is ook een complex getal.", True),
                 ("waar", r"\(i^{3} = -i\).", True),
                 ("waar", r"\(|z_{1} \cdot z_{2}| = |z_{1}| + |z_{2}|\).", False),
                 ("waar", "Het toegevoegde nemen spiegelt het punt om de reële as.", True),
                 ("waar", r"Een tweedegraadsvergelijking met \(D < 0\) heeft geen oplossingen in \(\mathbb{C}\).", False),
                 ("waar", r"\(z \cdot \overline{z}\) is altijd een reëel getal.", True),
                 ("waar", r"De modulus van \(-3\) is \(-3\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom \(z \cdot \overline{z}\) altijd een reëel getal is.",
                  r"De gemengde termen vallen tegen elkaar weg; wat overblijft is "
                  r"\(a^{2} + b^{2} = |z|^{2}\), en dat is reëel en niet negatief.", 3),
                 ("open", "Waarom vermenigvuldig je bij het delen teller en noemer met de "
                          "toegevoegde van de noemer?",
                  r"Omdat de noemer dan \(|z|^{2}\) wordt, dus reëel. Met een reële noemer kan je "
                  r"gewoon verder rekenen.", 3),
                 ("open", r"Waar liggen de \(n\) oplossingen van \(z^{n} = a\) in het vlak van "
                          r"Gauss? Beschrijf het.",
                  "Op één cirkel rond de oorsprong, gelijkmatig over de omtrek verdeeld. Ze vormen "
                  "de hoekpunten van een regelmatige veelhoek.", 3),
                 ("open", "Waarom is de goniometrische vorm handiger dan de cartesische bij "
                          "machtsverheffen?",
                  r"Met de Moivre verhef je enkel \(r\) tot de macht \(n\) en vermenigvuldig je "
                  r"\(\theta\) met \(n\). In cartesische vorm moet je alle haakjes uitwerken.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-telproblemen-en-het-binomium-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Telproblemen en het binomium",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk telprobleem",
             opdracht="Schrijf bij elke situatie op of het een permutatie, een variatie of een "
                      "combinatie is.",
             oefeningen=[
                 ("rij", [("zes atleten over goud, zilver en brons", "variatie, de volgorde telt"),
                          ("vier leden kiezen uit een club van twintig", "combinatie"),
                          ("zeven boeken op een rij zetten", "permutatie"),
                          ("een pincode van vier cijfers", "herhalingsvariatie"),
                          ("de letters van KOKOS herschikken", "herhalingspermutatie")],
                  "Welk telprobleem?", WL),
             ]),
        dict(kop="Faculteit en combinaties",
             opdracht="Reken uit. Vereenvoudig eerst de breuk met faculteiten.",
             oefeningen=[
                 ("rij", [(r"\(4!\)", r"\(24\)"), (r"\(\dfrac{6!}{4!}\)", r"\(30\)"),
                          (r"\(\binom{6}{2}\)", r"\(15\)"), (r"\(\binom{5}{3}\)", r"\(10\)"),
                          (r"\(\binom{7}{0}\)", r"\(1\)")],
                  "Reken uit.", W),
             ]),
        dict(kop="Variaties en herhalingen",
             opdracht="Schrijf eerst op welke formule je gebruikt, en reken dan pas uit.",
             oefeningen=[
                 ("kort", r"\(V_{6}^{3}\)", r"\(6 \cdot 5 \cdot 4 = 120\)", WW),
                 ("kort", "Hoeveel codes van drie letters bestaan er, uit een alfabet van 26?",
                  r"\(26^{3} = 17\,576\)", WW),
                 ("kort", "Op hoeveel manieren verdeel je goud, zilver en brons onder acht atleten?",
                  r"\(8 \cdot 7 \cdot 6 = 336\)", WW),
                 ("kort", "Hoeveel verschillende woorden maak je met de letters van KOKOS?",
                  r"\(\dfrac{5!}{2!\,2!} = 30\)", WW),
             ]),
        dict(kop="De telregels toepassen",
             opdracht="Zeg er telkens bij of je de somregel, de productregel of de complementregel "
                      "gebruikt.",
             oefeningen=[
                 ("kort", "Een menu heeft vier voorgerechten, zes hoofdgerechten en drie desserts. "
                          "Hoeveel menu's?",
                  r"productregel: \(4 \cdot 6 \cdot 3 = 72\)", WL),
                 ("kort", "Je neemt één hoofdgerecht uit zes óf één slaatje uit vier. Hoeveel keuzes?",
                  r"somregel: \(6 + 4 = 10\)", WL),
                 ("kort", "Acht mensen geven elkaar allemaal één keer een hand. Hoeveel handdrukken?",
                  r"\(\binom{8}{2} = 28\)", WL),
                 ("kort", "Hoeveel pincodes van vier cijfers bevatten minstens één nul?",
                  r"complementregel: \(10^{4} - 9^{4} = 3439\)", WL),
             ]),
        dict(kop="De driehoek van Pascal",
             opdracht="Vul de rijen aan. Elk getal is de som van de twee schuin erboven.",
             oefeningen=[
                 ("tabel", ["Rijnummer", "De rij", "Som van de rij"],
                  [[r"\(n = 3\)", None, None], [r"\(n = 4\)", None, None],
                   [r"\(n = 5\)", None, None]],
                  r"\(1\ 3\ 3\ 1\) en \(8\); \(1\ 4\ 6\ 4\ 1\) en \(16\); "
                  r"\(1\ 5\ 10\ 10\ 5\ 1\) en \(32\)", "200px"),
                 ("kort", r"\(\binom{7}{2}\)", r"\(21\)", W),
                 ("kort", r"\(\sum_{k=0}^{6} \binom{6}{k}\)", r"\(2^{6} = 64\)", WW),
             ]),
        dict(kop="Het binomium uitwerken",
             opdracht="Gebruik de juiste rij van de driehoek van Pascal.",
             oefeningen=[
                 ("kort", r"\(\left(a + b\right)^{4}\)",
                  r"\(a^{4} + 4a^{3}b + 6a^{2}b^{2} + 4ab^{3} + b^{4}\)", WL),
                 ("kort", r"\(\left(x - 2\right)^{3}\)", r"\(x^{3} - 6x^{2} + 12x - 8\)", WL),
                 ("kort", r"\(\left(1 + x\right)^{5}\)",
                  r"\(1 + 5x + 10x^{2} + 10x^{3} + 5x^{4} + x^{5}\)", WL),
             ]),
        dict(kop="Eén term aflezen",
             opdracht=r"Gebruik de algemene term \(\binom{n}{k} a^{\,n-k} b^{k}\); werk niet alles uit.",
             oefeningen=[
                 ("kort", r"De coëfficiënt van \(x^{3}\) in \(\left(1 + x\right)^{5}\)", r"\(10\)", W),
                 ("kort", r"Het aantal termen van \(\left(a + b\right)^{7}\)", r"\(8\)", W),
                 ("kort", r"De coëfficiënt van \(a^{2}b^{3}\) in \(\left(a + b\right)^{5}\)",
                  r"\(\binom{5}{3} = 10\)", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", r"Bij \(\left(a - b\right)^{n}\) wisselen de tekens van term tot term.", True),
                 ("waar", r"\(\binom{n}{p} = \binom{n}{n-p}\).", True),
                 ("waar", r"\(0! = 0\).", False),
                 ("waar", "Bij een combinatie telt de volgorde mee.", False),
                 ("waar", r"De som van rij \(n\) van de driehoek van Pascal is \(2^{n}\).", True),
                 ("waar", r"\(\left(a + b\right)^{2} = a^{2} + b^{2}\).", False),
                 ("waar", "Bij een herhalingsvariatie mag een element meer dan één keer voorkomen.", True),
                 ("waar", r"Bij dezelfde \(n\) en \(p\) zijn er meer combinaties dan variaties.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom er bij dezelfde \(n\) en \(p\) altijd minder combinaties "
                          r"dan variaties zijn.",
                  r"Bij een combinatie vallen alle \(p!\) volgordes van dezelfde keuze samen, dus "
                  r"\(\binom{n}{p} = \dfrac{V_{n}^{p}}{p!}\).", 3),
                 ("open", "Leg uit waarom elke rij van de driehoek van Pascal symmetrisch is.",
                  r"\(p\) elementen kiezen is hetzelfde als \(n - p\) elementen weglaten. Elke keuze "
                  r"hoort bij precies één groep die je niet kiest.", 3),
                 ("open", "Wanneer gebruik je de somregel en wanneer de productregel?",
                  "De somregel bij keuzes die elkaar uitsluiten, dus of-of. De productregel bij "
                  "keuzes die na elkaar komen, dus en-en.", 3),
                 ("open", r"Leg uit waarom \(\binom{n}{0} = 1\).",
                  "Er is precies één manier om niets te kiezen: de lege keuze. Daarom staat er aan "
                  "het begin van elke rij een één.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kansrekenen-en-kansverdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansrekenen en kansverdelingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eenvoudige kansen",
             opdracht=r"Gebruik de wet van Laplace. Schrijf elke kans als een vereenvoudigde breuk.",
             oefeningen=[
                 ("rij", [(r"\(P(\text{getal groter dan } 4)\) bij één worp met een dobbelsteen", r"\(\tfrac{1}{3}\)"),
                          (r"\(P(\text{aas})\) uit een spel van \(52\) kaarten", r"\(\tfrac{1}{13}\)"),
                          (r"\(P(\text{zwarte kaart})\) uit een spel van \(52\)", r"\(\tfrac{1}{2}\)"),
                          (r"\(P(\text{priemgetal})\) bij één worp met een dobbelsteen", r"\(\tfrac{1}{2}\), want \(2\), \(3\) en \(5\)"),
                          (r"\(P(\text{klaveren aas})\) uit een spel van \(52\)", r"\(\tfrac{1}{52}\)")],
                  r"Hoe groot is de kans?", WW),
             ]),
        dict(kop="Welke berekening hoort erbij",
             opdracht=r"Kruis de juiste berekening aan.",
             oefeningen=[
                 ("kies", r"Je gooit twee keer met een dobbelsteen. Welke berekening geeft \(P(\text{twee keer een zes})\)?",
                  [r"\(\tfrac{1}{6} \cdot \tfrac{1}{6}\)", r"\(\tfrac{1}{6} + \tfrac{1}{6}\)",
                   r"\(2 \cdot \tfrac{1}{6}\)", r"\(\tfrac{1}{6} - \tfrac{1}{36}\)"], 0),
                 ("kies", r"Je trekt één kaart. Welke berekening geeft \(P(\text{harten of ruiten})\)?",
                  [r"\(\tfrac{1}{4} + \tfrac{1}{4}\)", r"\(\tfrac{1}{4} \cdot \tfrac{1}{4}\)",
                   r"\(\tfrac{1}{4} + \tfrac{1}{4} - \tfrac{1}{16}\)", r"\(1 - \tfrac{1}{4}\)"], 0),
             ]),
        dict(kop="Somregel en complementregel",
             opdracht=r"Reken uit. Schrijf je antwoord als een kommagetal.",
             oefeningen=[
                 ("kort", r"\(P(A) = 0{,}45\). Bereken \(P(\overline{A})\).", r"\(0{,}55\)", W),
                 ("kort", r"\(P(A) = 0{,}6\), \(P(B) = 0{,}5\) en \(P(A \cap B) = 0{,}2\). Bereken \(P(A \cup B)\).", r"\(0{,}9\)", W),
                 ("kort", r"\(A\) en \(B\) sluiten elkaar uit, \(P(A) = 0{,}3\) en \(P(B) = 0{,}25\). Bereken \(P(A \cup B)\).", r"\(0{,}55\)", W),
                 ("kort", r"\(P(X = 0) = 0{,}12\). Bereken \(P(X \ge 1)\).", r"\(0{,}88\)", W),
             ]),
        dict(kop="Lezen uit een kruistabel",
             opdracht=r"Tweehonderd leerlingen, verdeeld naar geslacht en of ze een bril dragen. Vul eerst de totalen aan.",
             oefeningen=[
                 ("tabel", ["Groep", "bril", "geen bril", "totaal"],
                  [["jongens", "30", "70", None],
                   ["meisjes", "45", "55", None],
                   ["totaal", None, None, None]],
                  r"jongens \(100\), meisjes \(100\); bril \(75\), geen bril \(125\), totaal \(200\)", "120px"),
             ]),
        dict(kop="Kansen uit die kruistabel",
             opdracht=r"Let goed op waardoor je deelt.",
             oefeningen=[
                 ("kort", r"Bereken \(P(\text{bril})\).", r"\(\tfrac{75}{200} = 0{,}375\)", WW),
                 ("kort", r"Bereken \(P(\text{bril} \mid \text{meisje})\).", r"\(\tfrac{45}{100} = 0{,}45\)", WW),
                 ("kies", r"Zijn een bril dragen en een meisje zijn onafhankelijk?",
                  [r"ja, want beide groepen tellen \(100\) leerlingen",
                   r"nee, want \(P(\text{bril} \mid \text{meisje}) \neq P(\text{bril})\)",
                   r"ja, want het totaal is \(200\)",
                   r"dat kan je uit een kruistabel niet afleiden"], 1),
             ]),
        dict(kop="Onafhankelijk of niet",
             opdracht=r"Schrijf ja of nee, en bij nee waarom niet.",
             oefeningen=[
                 ("tabel", ["Situatie", "Onafhankelijk?"],
                  [["twee worpen met dezelfde dobbelsteen", None],
                   ["twee kaarten trekken zonder terugleggen", None],
                   ["twee kaarten trekken met terugleggen", None],
                   ["het weer van vandaag en het weer van morgen", None]],
                  "ja; nee, de eerste kaart verandert wat er nog in het spel zit; ja; nee, twee opeenvolgende dagen hangen samen",
                  "230px"),
             ]),
        dict(kop="Waar of niet waar: kansen",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"Er geldt altijd \(P(A \cup B) = P(A) + P(B)\).", False),
                 ("waar", r"Als \(P(A) = 1\), dan gebeurt \(A\) zeker.", True),
                 ("waar", r"\(P(A \mid B)\) en \(P(B \mid A)\) zijn altijd gelijk.", False),
                 ("waar", r"In een kansboom tellen de kansen op de takken uit één knoop samen tot \(1\).", True),
             ]),
        dict(kop="Kansbomen",
             opdracht=r"Teken de boom erbij en schrijf elke tak met haar kans.",
             oefeningen=[
                 ("open", r"Een zak bevat \(4\) groene en \(6\) oranje knikkers. Je trekt er twee zonder terugleggen. Bereken \(P(\text{twee keer groen})\).",
                  r"Eerste laag \(\tfrac{4}{10}\) en \(\tfrac{6}{10}\); na een groene blijven er \(3\) groene van de \(9\) over. Dus \(\tfrac{4}{10} \cdot \tfrac{3}{9} = \tfrac{12}{90} = \tfrac{2}{15}\).", 6),
                 ("open", r"Bereken bij diezelfde zak \(P(\text{precies één groene})\).",
                  r"Twee paden: \(\tfrac{4}{10} \cdot \tfrac{6}{9} = \tfrac{24}{90}\) en \(\tfrac{6}{10} \cdot \tfrac{4}{9} = \tfrac{24}{90}\). Samen \(\tfrac{48}{90} = \tfrac{8}{15}\).", 4),
             ]),
        dict(kop="Met de complementregel",
             opdracht=r"Reken eerst de tegengestelde gebeurtenis uit.",
             oefeningen=[
                 ("open", r"Je gooit vier keer met een munt. Bereken \(P(\text{minstens één keer munt})\) met de complementregel.",
                  r"\(P(X = 0) = \left(\tfrac{1}{2}\right)^{4} = \tfrac{1}{16}\), dus \(P(X \ge 1) = 1 - \tfrac{1}{16} = \tfrac{15}{16}\).", 3),
             ]),
        dict(kop="Binomiaal of niet",
             opdracht=r"Kruis aan of de situatie binomiaal verdeeld is, en zo niet welke voorwaarde ontbreekt.",
             oefeningen=[
                 ("tabel", ["Situatie", "Binomiaal?"],
                  [["het aantal zessen in dertig worpen met een dobbelsteen", None],
                   ["het aantal rode ballen bij vijf trekkingen zonder terugleggen uit een zak van tien", None],
                   ["het aantal worpen tot je de eerste zes gooit", None],
                   ["het aantal defecte stukken bij tachtig stukken met foutkans nul komma nul twee", None]],
                  r"ja; nee, \(p\) verandert per trekking; nee, \(n\) ligt niet vast; ja", "250px"),
             ]),
        dict(kop="De binomiale kansformule",
             opdracht=r"Schrijf de formule op met de juiste getallen ingevuld. Uitrekenen hoeft niet.",
             oefeningen=[
                 ("rij", [(r"\(n = 8\), \(p = 0{,}3\), \(P(X = 2)\)", r"\(\binom{8}{2}\,0{,}3^{2}\,0{,}7^{6}\)"),
                          (r"\(n = 12\), \(p = 0{,}25\), \(P(X = 5)\)", r"\(\binom{12}{5}\,0{,}25^{5}\,0{,}75^{7}\)"),
                          (r"\(n = 6\), \(p = 0{,}5\), \(P(X = 0)\)", r"\(0{,}5^{6} = \tfrac{1}{64}\)"),
                          (r"\(n = 9\), \(p = 0{,}4\), \(P(X = 9)\)", r"\(0{,}4^{9}\)")],
                  r"Welke uitdrukking hoort erbij?", WL),
                 ("kort", r"\(n = 5\) en \(p = 0{,}5\). Bereken \(P(X = 5)\) als breuk.", r"\(\tfrac{1}{32}\)", W),
                 ("kort", r"Bereken \(\binom{7}{3}\).", r"\(35\)", W),
             ]),
        dict(kop="Verwachtingswaarde en standaardafwijking",
             opdracht=r"Vul aan. Rond \(\sigma\) af op één cijfer na de komma.",
             oefeningen=[
                 ("tabel", ["n", "p", "E(X)", "σ"],
                  [["60", "1/6", None, None],
                   ["100", "0,2", None, None],
                   ["40", "0,5", None, None],
                   ["200", "0,05", None, None]],
                  r"\(10\) en \(2{,}9\); \(20\) en \(4\); \(20\) en \(3{,}2\); \(10\) en \(3{,}1\)", "120px"),
                 ("kort", r"Bij welke \(p\) is \(\sigma\) het grootst, als \(n\) vastligt?", r"\(p = 0{,}5\)", W),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de formule of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom je bij \(u_{10}\) van een rekenkundige rij negen keer "
                          r"\(d\) optelt en niet tien keer.",
                  r"\(u_{1}\) staat er al. Van de eerste naar de tiende term zet je negen stappen, "
                  r"dus \(u_{10} = u_{1} + 9d\).", 3),
                 ("open", r"Een bal valt van twee meter en stuitert telkens tot \(60\%\) van de "
                          r"vorige hoogte. Kan je de totale hoogte van alle sprongen berekenen? Leg uit.",
                  r"Ja. De sprongen vormen een meetkundige rij met \(q = 0{,}6\), en omdat "
                  r"\(|q| < 1\) bestaat de oneindige som. Oneindig veel sprongen geven samen een "
                  r"eindige hoogte.", 3),
                 ("open", r"Leg uit waarom \(\lim\limits_{n \to +\infty} \dfrac{3n - 1}{n} = 3\) "
                          r"en niet \(+\infty\), hoewel teller en noemer allebei onbeperkt groeien.",
                  r"Splits op: \(\dfrac{3n-1}{n} = 3 - \dfrac{1}{n}\). De tweede term kruipt naar "
                  r"nul, dus blijft \(3\) over. Het gaat om de verhouding, niet om de grootte.", 3),
                 ("open", "Leg uit waarom je bij een rij alleen over de limiet op oneindig spreekt.",
                  r"Een rij is alleen gedefinieerd voor \(n \in \mathbb{N}\). Tussen \(u_{3}\) en "
                  r"\(u_{4}\) ligt niets, dus er is geen tussenwaarde om naartoe te kruipen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-primitieven-en-de-onbepaalde-integraal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Primitieven en de onbepaalde integraal",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Basisprimitieven",
             opdracht=r"Zoek een primitieve. Vergeet \(+\,C\) niet, en controleer door af te leiden.",
             oefeningen=[
                 ("rij", [(r"\(\int x^{4}\,dx\)", r"\(\dfrac{x^{5}}{5} + C\)"),
                          (r"\(\int 6\,dx\)", r"\(6x + C\)"),
                          (r"\(\int \sin x\,dx\)", r"\(-\cos x + C\)"),
                          (r"\(\int \dfrac{1}{x}\,dx\)", r"\(\ln|x| + C\)"),
                          (r"\(\int e^{x}\,dx\)", r"\(e^{x} + C\)"),
                          (r"\(\int \cos x\,dx\)", r"\(\sin x + C\)")],
                  "Geef een primitieve.", WL),
             ]),
        dict(kop="Lineariteit",
             opdracht="Splits de integrand en haal constanten buiten het integraalteken.",
             oefeningen=[
                 ("rij", [(r"\(\int (4x + 3)\,dx\)", r"\(2x^{2} + 3x + C\)"),
                          (r"\(\int 6x^{2}\,dx\)", r"\(2x^{3} + C\)"),
                          (r"\(\int \left(x - \cos x\right)dx\)",
                           r"\(\dfrac{x^{2}}{2} - \sin x + C\)"),
                          (r"\(\int 5\,e^{x}\,dx\)", r"\(5\,e^{x} + C\)")],
                  "Geef een primitieve.", WL),
             ]),
        dict(kop="Eerst herschrijven",
             opdracht=r"Schrijf de integrand eerst als een macht of als een som, en integreer dan pas.",
             oefeningen=[
                 ("kort", r"\(\int \dfrac{1}{x^{2}}\,dx\)", r"\(-\dfrac{1}{x} + C\)", WW),
                 ("kort", r"\(\int \sqrt{x}\,dx\)", r"\(\dfrac{2}{3}x\sqrt{x} + C\)", WW),
                 ("kort", r"\(\int \dfrac{3}{x}\,dx\)", r"\(3\ln|x| + C\)", WW),
                 ("kort", r"\(\int \dfrac{x^{2} + 1}{x}\,dx\)",
                  r"\(\dfrac{x^{2}}{2} + \ln|x| + C\)", WW),
             ]),
        dict(kop="Welke methode",
             opdracht="Kruis aan welke methode het eerst past: onmiddellijk, splitsen, "
                      "substitutie of partiële integratie.",
             oefeningen=[
                 ("tabel", ["Integraal", "Methode"],
                  [[r"\(\int \left(3x^{2} - 4x\right)dx\)", None],
                   [r"\(\int x\sin x\,dx\)", None],
                   [r"\(\int 2x\,e^{x^{2}}\,dx\)", None],
                   [r"\(\int \cos x\,dx\)", None],
                   [r"\(\int \dfrac{3x^{2}}{x^{3} + 5}\,dx\)", None]],
                  "splitsen; partiële integratie; substitutie; onmiddellijk; substitutie",
                  "230px"),
             ]),
        dict(kop="Substitutie",
             opdracht=r"Zoek de binnenste functie \(u\) waarvan de afgeleide er ook staat.",
             oefeningen=[
                 ("kort", r"\(\int 2x\,e^{x^{2}}\,dx\)", r"\(e^{x^{2}} + C\)", WW),
                 ("kort", r"\(\int \dfrac{2x}{x^{2} + 1}\,dx\)", r"\(\ln\left(x^{2}+1\right) + C\)", WW),
                 ("kort", r"\(\int (x + 1)^{5}\,dx\)", r"\(\dfrac{(x+1)^{6}}{6} + C\)", WW),
             ]),
        dict(kop="Partiële integratie",
             opdracht=r"Gebruik \(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\), en kies \(u\) zo dat "
                      r"\(u'\) eenvoudiger wordt.",
             oefeningen=[
                 ("kort", r"\(\int x\,e^{x}\,dx\)", r"\(x\,e^{x} - e^{x} + C\)", WL),
                 ("kort", r"\(\int x\cos x\,dx\)", r"\(x\sin x + \cos x + C\)", WL),
             ]),
        dict(kop="Bepaalde integralen",
             opdracht="Zoek een primitieve, vul de twee grenzen in en trek af.",
             oefeningen=[
                 ("rij", [(r"\(\int_{0}^{3} 2x\,dx\)", r"\(9\)"),
                          (r"\(\int_{1}^{2} x^{2}\,dx\)", r"\(\dfrac{7}{3}\)"),
                          (r"\(\int_{0}^{\pi/2} \cos x\,dx\)", r"\(1\)"),
                          (r"\(\int_{5}^{5} f(x)\,dx\)", r"\(0\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="Met e en met π",
             opdracht="Dezelfde werkwijze, maar nu met grenzen die zelf een getal als e of pi zijn.",
             oefeningen=[
                 ("kort", r"\(\int_{0}^{\pi} \sin x\,dx\)", r"\(2\)", W),
                 ("kort", r"\(\int_{1}^{e} \dfrac{1}{x}\,dx\)", r"\(1\)", W),
                 ("kort", r"\(\int_{0}^{1} e^{x}\,dx\)", r"\(e - 1\)", W),
             ]),
        dict(kop="Waar of niet waar: primitieven",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Twee primitieven van dezelfde functie hebben dezelfde afgeleide.", True),
                 ("waar", r"Een factor met een \(x\) erin mag je voor het integraalteken zetten.", False),
                 ("waar", "Na een substitutie in een bepaalde integraal mag je de oude grenzen laten staan.", False),
                 ("waar", r"\(\int \sin x\,dx = -\cos x + C\).", True),
             ]),
        dict(kop="Waar of niet waar: methodes",
             opdracht="Nog vier uitspraken, over de regels en de methodes.",
             oefeningen=[
                 ("waar", "Elke continue functie heeft een primitieve.", True),
                 ("waar", r"\(\int x^{-1}\,dx = \dfrac{x^{0}}{0} + C\).", False),
                 ("waar", "Partiële integratie volgt uit de productregel voor afgeleiden.", True),
                 ("waar", "Een integraal met een wortel erin kan je nooit met substitutie oplossen.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom \(\int x^{n}\,dx = \dfrac{x^{\,n+1}}{n+1} + C\) niet "
                          r"werkt voor \(n = -1\).",
                  r"Je zou delen door \(n + 1 = 0\). Net die ene integraal geeft \(\ln|x| + C\).", 3),
                 ("open", "Wat moet er in de integrand staan voor je een substitutie kan uitvoeren?",
                  r"Een binnenste functie waarvan ook de afgeleide in de integrand staat. Zonder "
                  r"die afgeleide kan je \(dx\) niet omzetten naar \(du\).", 3),
                 ("open", r"Leg uit waarom je bij een bepaalde integraal geen \(+\,C\) schrijft.",
                  r"\(\left(F(b) + C\right) - \left(F(a) + C\right) = F(b) - F(a)\): dezelfde "
                  r"constante komt er in de bovengrens bij en in de ondergrens weer af.", 3),
                 ("open", "Hoe controleer je of je primitieve klopt, en waarom is dat een echte controle?",
                  r"Leid je antwoord af; je moet de integrand terugkrijgen. Afleiden is eenduidig, "
                  r"terwijl opnieuw integreren vaak dezelfde fout herhaalt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-bepaalde-integraal-en-haar-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De bepaalde integraal en haar toepassingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Riemannsommen",
             opdracht="Vul in. Denk aan de laagste en de hoogste functiewaarde per stukje.",
             oefeningen=[
                 ("tabel", ["Som", "Welke functiewaarde per stukje", "Groter of kleiner"],
                  [["ondersom", None, None], ["bovensom", None, None]],
                  "de laagste, dus kleiner; de hoogste, dus groter", "200px"),
                 ("kort", r"Waarmee komt de \(dx\) overeen bij de rechthoekjes?",
                  "met hun breedte", WW),
             ]),
        dict(kop="Snel uitrekenen",
             opdracht="Zoek een primitieve, vul de grenzen in en trek af.",
             oefeningen=[
                 ("rij", [(r"\(\int_{0}^{4} 3\,dx\)", r"\(12\)"),
                          (r"\(\int_{1}^{3} x\,dx\)", r"\(4\)"),
                          (r"\(\int_{0}^{2} x^{3}\,dx\)", r"\(4\)"),
                          (r"\(\int_{1}^{4} \dfrac{1}{\sqrt{x}}\,dx\)", r"\(2\)"),
                          (r"\(\int_{0}^{\pi/2} \sin x\,dx\)", r"\(1\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="Met de hoofdstelling",
             opdracht=r"Schrijf eerst \(\left[F(x)\right]_{a}^{b}\) op, en vul dan pas in.",
             oefeningen=[
                 ("kort", r"\(\int_{0}^{1} e^{2x}\,dx\)", r"\(\dfrac{e^{2} - 1}{2}\)", WW),
                 ("kort", r"\(\int_{1}^{e} \dfrac{\ln x}{x}\,dx\)", r"\(\dfrac{1}{2}\)", WW),
                 ("kort", r"\(\int_{-1}^{1} x^{2}\,dx\)", r"\(\dfrac{2}{3}\)", WW),
                 ("kort", r"\(\int_{0}^{1} \dfrac{2x}{x^{2} + 1}\,dx\)", r"\(\ln 2\)", WW),
             ]),
        dict(kop="Georiënteerd of werkelijk",
             opdracht="Reken de integraal uit, en kijk daarna of dat ook de werkelijke oppervlakte is.",
             oefeningen=[
                 ("kort", r"\(\int_{-1}^{1} x^{3}\,dx\)", r"\(0\)", W),
                 ("kort", r"\(\int_{0}^{2\pi} \sin x\,dx\)", r"\(0\)", W),
                 ("kort", r"De werkelijke oppervlakte tussen \(y = x^{3}\) en de x-as op \([-1,\ 1]\)",
                  r"\(2 \cdot \tfrac{1}{4} = \tfrac{1}{2}\)", WW),
             ]),
        dict(kop="Oppervlakte tussen twee krommen",
             opdracht="Maak eerst een schets, zoek de snijpunten, en integreer de bovenste min de onderste.",
             oefeningen=[
                 ("kort", r"Tussen \(y = 2x\) en \(y = x^{2}\), tussen hun snijpunten",
                  r"snijpunten \(0\) en \(2\); \(4 - \tfrac{8}{3} = \tfrac{4}{3}\)", WL),
                 ("kort", r"Tussen \(y = x\) en \(y = x^{3}\) op \([0,\ 1]\)",
                  r"\(\tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}\)", WL),
             ]),
        dict(kop="Omwenteling en booglengte",
             opdracht=r"Gebruik \(V = \pi\int_{a}^{b} f(x)^{2}dx\) en "
                      r"\(L = \int_{a}^{b}\sqrt{1 + f'(x)^{2}}\,dx\).",
             oefeningen=[
                 ("kort", r"Inhoud als \(y = x\) op \([0,\ 1]\) om de x-as draait",
                  r"\(\pi\int_{0}^{1} x^{2}dx = \dfrac{\pi}{3}\)", WL),
                 ("kort", r"Inhoud als \(y = 2\) op \([0,\ 3]\) om de x-as draait",
                  r"\(\pi\int_{0}^{3} 4\,dx = 12\pi\)", WL),
                 ("kort", r"Schrijf de booglengte-integraal op van \(y = x^{2}\) op \([0,\ 1]\)",
                  r"\(\int_{0}^{1}\sqrt{1 + 4x^{2}}\,dx\)", WL),
             ]),
        dict(kop="Toepassingen",
             opdracht="Schrijf telkens op wat je integreert, en controleer de eenheid van je antwoord.",
             oefeningen=[
                 ("tabel", ["Wat je integreert", "Wat je krijgt"],
                  [["de snelheid over de tijd", None], ["de versnelling over de tijd", None],
                   ["het debiet van een kraan over de tijd", None],
                   ["de marginale kost over een aantal stuks", None]],
                  "de verplaatsing; de verandering van de snelheid; de totale hoeveelheid water; "
                  "de toename van de totale kost", "280px"),
                 ("kort", r"Een kraan geeft \(0{,}5\) liter per seconde, \(40\) s lang. Hoeveel liter?",
                  r"\(20\) l", WW),
                 ("kort", r"\(v(t) = 3t\) m/s. Welke verplaatsing tussen \(t = 0\) en \(t = 4\) s?",
                  r"\(\left[1{,}5\,t^{2}\right]_{0}^{4} = 24\) m", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Een ondersom is nooit groter dan de werkelijke oppervlakte.", True),
                 ("waar", "Hoe meer deelintervallen je neemt, hoe beter de benadering.", True),
                 ("waar", "Een werkelijke oppervlakte kan negatief zijn.", False),
                 ("waar", r"\(\int_{b}^{a} f(x)\,dx = -\int_{a}^{b} f(x)\,dx\).", True),
                 ("waar", "De hoofdstelling geldt ook voor een functie met een sprong.", False),
                 ("waar", "De bovengrens van een integraal is de grootste functiewaarde.", False),
                 ("waar", "De inhoud van een omwentelingslichaam hangt af van de as waarrond je draait.", True),
                 ("waar", r"\(\int_{a}^{a} f(x)\,dx = f(a)\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel of de voorwaarde die je gebruikt.",
             oefeningen=[
                 ("open", "Leg uit waarom de limiet van Riemannsommen een exacte oppervlakte geeft.",
                  "De werkelijke oppervlakte ligt altijd tussen de onder- en de bovensom. Kruipen "
                  "die twee naar hetzelfde getal, dan blijft er maar één mogelijkheid over.", 3),
                 ("open", r"Een wagen rijdt eerst vooruit en daarna een stuk achteruit. Geeft "
                          r"\(\int v\,dt\) de afgelegde weg? Leg uit.",
                  "Nee, de verplaatsing. Achteruit is de snelheid negatief, en die trekt de "
                  "integraal af. Voor de afgelegde weg neem je de stukken positief.", 3),
                 ("open", "Waarom maak je eerst een schets bij een oppervlakte tussen twee krommen?",
                  "Om te zien welke kromme boven ligt en waar ze elkaar snijden. Zonder schets zet "
                  "je de twee in de verkeerde volgorde en krijg je een negatieve uitkomst.", 3),
                 ("open", "Leg uit waarom je bij een omwentelingslichaam de functie kwadrateert.",
                  r"Elke dunne schijf is een cirkel met straal \(f(x)\), en de oppervlakte van een "
                  r"cirkel is \(\pi r^{2}\). Die straal staat dus in het kwadraat.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-complexe-getallen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Complexe getallen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Machten van i",
             opdracht=r"Reken uit. De machten van \(i\) herhalen zich om de vier.",
             oefeningen=[
                 ("rij", [(r"\(i^{5}\)", r"\(i\)"), (r"\(i^{6}\)", r"\(-1\)"),
                          (r"\(i^{7}\)", r"\(-i\)"), (r"\(i^{8}\)", r"\(1\)"),
                          (r"\(i^{11}\)", r"\(-i\)")],
                  "Reken uit.", W),
             ]),
        dict(kop="Optellen en vermenigvuldigen",
             opdracht=r"Werk uit en schrijf het antwoord als \(a + bi\).",
             oefeningen=[
                 ("rij", [(r"\(\left(4 + i\right) + \left(2 - 3i\right)\)", r"\(6 - 2i\)"),
                          (r"\(\left(2 - i\right) - \left(1 + 2i\right)\)", r"\(1 - 3i\)"),
                          (r"\(\overline{5 - 2i}\)", r"\(5 + 2i\)"),
                          (r"\(\left(2 - i\right)^{2}\)", r"\(3 - 4i\)")],
                  "Reken uit.", WL),
             ]),
        dict(kop="Delen door een complex getal",
             opdracht="Vermenigvuldig teller en noemer met de toegevoegde van de noemer.",
             oefeningen=[
                 ("kort", r"\(\dfrac{1}{2 + i}\)", r"\(\dfrac{2}{5} - \dfrac{1}{5}i\)", WW),
                 ("kort", r"\(\dfrac{3 + i}{1 - i}\)", r"\(1 + 2i\)", WW),
                 ("kort", r"\(\dfrac{i}{1 + i}\)", r"\(\dfrac{1}{2} + \dfrac{1}{2}i\)", WW),
             ]),
        dict(kop="Modulus en argument",
             opdracht="Vul de tabel aan. Een modulus is een afstand en dus nooit negatief.",
             oefeningen=[
                 ("tabel", ["Getal", "Modulus", "Argument in graden"],
                  [[r"\(3\)", None, None], [r"\(-2\)", None, None],
                   [r"\(4i\)", None, None], [r"\(1 + i\)", None, None],
                   [r"\(-i\)", None, None]],
                  r"\(3\) en \(0^\circ\); \(2\) en \(180^\circ\); \(4\) en \(90^\circ\); "
                  r"\(\sqrt{2}\) en \(45^\circ\); \(1\) en \(270^\circ\)", "150px"),
                 ("kort", r"\(|6 - 8i|\)", r"\(10\)", W),
                 ("kort", r"\(|-5 + 12i|\)", r"\(13\)", W),
             ]),
        dict(kop="Wat de bewerkingen in het vlak doen",
             opdracht="Antwoord in één zin, met de draai of de spiegeling erbij.",
             oefeningen=[
                 ("kort", r"Wat doet een vermenigvuldiging met \(i\) met een punt?",
                  "het draait een kwart slag rond de oorsprong", WL),
                 ("kort", r"Wat doet \(z \mapsto \overline{z}\) met een punt?",
                  "het spiegelt om de reële as", WL),
             ]),
        dict(kop="Goniometrische vorm en de Moivre",
             opdracht=r"Werk met \(r\) en \(\theta\). Bij machten gebruik je de formule van de Moivre.",
             oefeningen=[
                 ("tabel", ["Bewerking", "Met de moduli", "Met de argumenten"],
                  [["vermenigvuldigen", None, None], ["delen", None, None],
                   [r"tot de macht \(n\)", None, None]],
                  r"vermenigvuldigen en optellen; delen en aftrekken; tot de macht \(n\) en met "
                  r"\(n\) vermenigvuldigen", "180px"),
                 ("kort", r"Schrijf \(1 + i\) in goniometrische vorm.",
                  r"\(\sqrt{2}\left(\cos 45^\circ + i\sin 45^\circ\right)\)", WL),
                 ("kort", r"Bereken \(\left(1 + i\right)^{8}\) met de Moivre.",
                  r"\(\left(\sqrt{2}\right)^{8} = 16\) en \(8 \cdot 45^\circ = 360^\circ\), dus \(16\)", WL),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht=r"Los op in \(\mathbb{C}\). Vergeet de tweede oplossing niet.",
             oefeningen=[
                 ("kort", r"\(x^{2} + 9 = 0\)", r"\(x = 3i\) of \(x = -3i\)", WW),
                 ("kort", r"\(x^{2} - 4x + 13 = 0\)", r"\(x = 2 \pm 3i\)", WW),
                 ("kort", r"Hoeveel oplossingen heeft \(z^{5} = 1\) in \(\mathbb{C}\)?", r"\(5\)", W),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", "Je kan twee complexe getallen van klein naar groot ordenen.", False),
                 ("waar", "Elk reëel getal is ook een complex getal.", True),
                 ("waar", r"\(i^{3} = -i\).", True),
                 ("waar", r"\(|z_{1} \cdot z_{2}| = |z_{1}| + |z_{2}|\).", False),
                 ("waar", "Het toegevoegde nemen spiegelt het punt om de reële as.", True),
                 ("waar", r"Een tweedegraadsvergelijking met \(D < 0\) heeft geen oplossingen in \(\mathbb{C}\).", False),
                 ("waar", r"\(z \cdot \overline{z}\) is altijd een reëel getal.", True),
                 ("waar", r"De modulus van \(-3\) is \(-3\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom \(z \cdot \overline{z}\) altijd een reëel getal is.",
                  r"De gemengde termen vallen tegen elkaar weg; wat overblijft is "
                  r"\(a^{2} + b^{2} = |z|^{2}\), en dat is reëel en niet negatief.", 3),
                 ("open", "Waarom vermenigvuldig je bij het delen teller en noemer met de "
                          "toegevoegde van de noemer?",
                  r"Omdat de noemer dan \(|z|^{2}\) wordt, dus reëel. Met een reële noemer kan je "
                  r"gewoon verder rekenen.", 3),
                 ("open", r"Waar liggen de \(n\) oplossingen van \(z^{n} = a\) in het vlak van "
                          r"Gauss? Beschrijf het.",
                  "Op één cirkel rond de oorsprong, gelijkmatig over de omtrek verdeeld. Ze vormen "
                  "de hoekpunten van een regelmatige veelhoek.", 3),
                 ("open", "Waarom is de goniometrische vorm handiger dan de cartesische bij "
                          "machtsverheffen?",
                  r"Met de Moivre verhef je enkel \(r\) tot de macht \(n\) en vermenigvuldig je "
                  r"\(\theta\) met \(n\). In cartesische vorm moet je alle haakjes uitwerken.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-telproblemen-en-het-binomium-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Telproblemen en het binomium",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk telprobleem",
             opdracht="Schrijf bij elke situatie op of het een permutatie, een variatie of een "
                      "combinatie is.",
             oefeningen=[
                 ("rij", [("zes atleten over goud, zilver en brons", "variatie, de volgorde telt"),
                          ("vier leden kiezen uit een club van twintig", "combinatie"),
                          ("zeven boeken op een rij zetten", "permutatie"),
                          ("een pincode van vier cijfers", "herhalingsvariatie"),
                          ("de letters van KOKOS herschikken", "herhalingspermutatie")],
                  "Welk telprobleem?", WL),
             ]),
        dict(kop="Faculteit en combinaties",
             opdracht="Reken uit. Vereenvoudig eerst de breuk met faculteiten.",
             oefeningen=[
                 ("rij", [(r"\(4!\)", r"\(24\)"), (r"\(\dfrac{6!}{4!}\)", r"\(30\)"),
                          (r"\(\binom{6}{2}\)", r"\(15\)"), (r"\(\binom{5}{3}\)", r"\(10\)"),
                          (r"\(\binom{7}{0}\)", r"\(1\)")],
                  "Reken uit.", W),
             ]),
        dict(kop="Variaties en herhalingen",
             opdracht="Schrijf eerst op welke formule je gebruikt, en reken dan pas uit.",
             oefeningen=[
                 ("kort", r"\(V_{6}^{3}\)", r"\(6 \cdot 5 \cdot 4 = 120\)", WW),
                 ("kort", "Hoeveel codes van drie letters bestaan er, uit een alfabet van 26?",
                  r"\(26^{3} = 17\,576\)", WW),
                 ("kort", "Op hoeveel manieren verdeel je goud, zilver en brons onder acht atleten?",
                  r"\(8 \cdot 7 \cdot 6 = 336\)", WW),
                 ("kort", "Hoeveel verschillende woorden maak je met de letters van KOKOS?",
                  r"\(\dfrac{5!}{2!\,2!} = 30\)", WW),
             ]),
        dict(kop="De telregels toepassen",
             opdracht="Zeg er telkens bij of je de somregel, de productregel of de complementregel "
                      "gebruikt.",
             oefeningen=[
                 ("kort", "Een menu heeft vier voorgerechten, zes hoofdgerechten en drie desserts. "
                          "Hoeveel menu's?",
                  r"productregel: \(4 \cdot 6 \cdot 3 = 72\)", WL),
                 ("kort", "Je neemt één hoofdgerecht uit zes óf één slaatje uit vier. Hoeveel keuzes?",
                  r"somregel: \(6 + 4 = 10\)", WL),
                 ("kort", "Acht mensen geven elkaar allemaal één keer een hand. Hoeveel handdrukken?",
                  r"\(\binom{8}{2} = 28\)", WL),
                 ("kort", "Hoeveel pincodes van vier cijfers bevatten minstens één nul?",
                  r"complementregel: \(10^{4} - 9^{4} = 3439\)", WL),
             ]),
        dict(kop="De driehoek van Pascal",
             opdracht="Vul de rijen aan. Elk getal is de som van de twee schuin erboven.",
             oefeningen=[
                 ("tabel", ["Rijnummer", "De rij", "Som van de rij"],
                  [[r"\(n = 3\)", None, None], [r"\(n = 4\)", None, None],
                   [r"\(n = 5\)", None, None]],
                  r"\(1\ 3\ 3\ 1\) en \(8\); \(1\ 4\ 6\ 4\ 1\) en \(16\); "
                  r"\(1\ 5\ 10\ 10\ 5\ 1\) en \(32\)", "200px"),
                 ("kort", r"\(\binom{7}{2}\)", r"\(21\)", W),
                 ("kort", r"\(\sum_{k=0}^{6} \binom{6}{k}\)", r"\(2^{6} = 64\)", WW),
             ]),
        dict(kop="Het binomium uitwerken",
             opdracht="Gebruik de juiste rij van de driehoek van Pascal.",
             oefeningen=[
                 ("kort", r"\(\left(a + b\right)^{4}\)",
                  r"\(a^{4} + 4a^{3}b + 6a^{2}b^{2} + 4ab^{3} + b^{4}\)", WL),
                 ("kort", r"\(\left(x - 2\right)^{3}\)", r"\(x^{3} - 6x^{2} + 12x - 8\)", WL),
                 ("kort", r"\(\left(1 + x\right)^{5}\)",
                  r"\(1 + 5x + 10x^{2} + 10x^{3} + 5x^{4} + x^{5}\)", WL),
             ]),
        dict(kop="Eén term aflezen",
             opdracht=r"Gebruik de algemene term \(\binom{n}{k} a^{\,n-k} b^{k}\); werk niet alles uit.",
             oefeningen=[
                 ("kort", r"De coëfficiënt van \(x^{3}\) in \(\left(1 + x\right)^{5}\)", r"\(10\)", W),
                 ("kort", r"Het aantal termen van \(\left(a + b\right)^{7}\)", r"\(8\)", W),
                 ("kort", r"De coëfficiënt van \(a^{2}b^{3}\) in \(\left(a + b\right)^{5}\)",
                  r"\(\binom{5}{3} = 10\)", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Zet een kruisje, en verbeter in gedachten wat niet klopt.",
             oefeningen=[
                 ("waar", r"Bij \(\left(a - b\right)^{n}\) wisselen de tekens van term tot term.", True),
                 ("waar", r"\(\binom{n}{p} = \binom{n}{n-p}\).", True),
                 ("waar", r"\(0! = 0\).", False),
                 ("waar", "Bij een combinatie telt de volgorde mee.", False),
                 ("waar", r"De som van rij \(n\) van de driehoek van Pascal is \(2^{n}\).", True),
                 ("waar", r"\(\left(a + b\right)^{2} = a^{2} + b^{2}\).", False),
                 ("waar", "Bij een herhalingsvariatie mag een element meer dan één keer voorkomen.", True),
                 ("waar", r"Bij dezelfde \(n\) en \(p\) zijn er meer combinaties dan variaties.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf in volle zinnen, en noem de regel die je gebruikt.",
             oefeningen=[
                 ("open", r"Leg uit waarom er bij dezelfde \(n\) en \(p\) altijd minder combinaties "
                          r"dan variaties zijn.",
                  r"Bij een combinatie vallen alle \(p!\) volgordes van dezelfde keuze samen, dus "
                  r"\(\binom{n}{p} = \dfrac{V_{n}^{p}}{p!}\).", 3),
                 ("open", "Leg uit waarom elke rij van de driehoek van Pascal symmetrisch is.",
                  r"\(p\) elementen kiezen is hetzelfde als \(n - p\) elementen weglaten. Elke keuze "
                  r"hoort bij precies één groep die je niet kiest.", 3),
                 ("open", "Wanneer gebruik je de somregel en wanneer de productregel?",
                  "De somregel bij keuzes die elkaar uitsluiten, dus of-of. De productregel bij "
                  "keuzes die na elkaar komen, dus en-en.", 3),
                 ("open", r"Leg uit waarom \(\binom{n}{0} = 1\).",
                  "Er is precies één manier om niets te kiezen: de lege keuze. Daarom staat er aan "
                  "het begin van elke rij een één.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kansrekenen-en-kansverdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansrekenen en kansverdelingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eenvoudige kansen",
             opdracht=r"Gebruik de wet van Laplace. Schrijf elke kans als een vereenvoudigde breuk.",
             oefeningen=[
                 ("rij", [(r"\(P(\text{getal groter dan } 4)\) bij één worp met een dobbelsteen", r"\(\tfrac{1}{3}\)"),
                          (r"\(P(\text{aas})\) uit een spel van \(52\) kaarten", r"\(\tfrac{1}{13}\)"),
                          (r"\(P(\text{zwarte kaart})\) uit een spel van \(52\)", r"\(\tfrac{1}{2}\)"),
                          (r"\(P(\text{priemgetal})\) bij één worp met een dobbelsteen", r"\(\tfrac{1}{2}\), want \(2\), \(3\) en \(5\)"),
                          (r"\(P(\text{klaveren aas})\) uit een spel van \(52\)", r"\(\tfrac{1}{52}\)")],
                  r"Hoe groot is de kans?", WW),
             ]),
        dict(kop="Welke berekening hoort erbij",
             opdracht=r"Kruis de juiste berekening aan.",
             oefeningen=[
                 ("kies", r"Je gooit twee keer met een dobbelsteen. Welke berekening geeft \(P(\text{twee keer een zes})\)?",
                  [r"\(\tfrac{1}{6} \cdot \tfrac{1}{6}\)", r"\(\tfrac{1}{6} + \tfrac{1}{6}\)",
                   r"\(2 \cdot \tfrac{1}{6}\)", r"\(\tfrac{1}{6} - \tfrac{1}{36}\)"], 0),
                 ("kies", r"Je trekt één kaart. Welke berekening geeft \(P(\text{harten of ruiten})\)?",
                  [r"\(\tfrac{1}{4} + \tfrac{1}{4}\)", r"\(\tfrac{1}{4} \cdot \tfrac{1}{4}\)",
                   r"\(\tfrac{1}{4} + \tfrac{1}{4} - \tfrac{1}{16}\)", r"\(1 - \tfrac{1}{4}\)"], 0),
             ]),
        dict(kop="Somregel en complementregel",
             opdracht=r"Reken uit. Schrijf je antwoord als een kommagetal.",
             oefeningen=[
                 ("kort", r"\(P(A) = 0{,}45\). Bereken \(P(\overline{A})\).", r"\(0{,}55\)", W),
                 ("kort", r"\(P(A) = 0{,}6\), \(P(B) = 0{,}5\) en \(P(A \cap B) = 0{,}2\). Bereken \(P(A \cup B)\).", r"\(0{,}9\)", W),
                 ("kort", r"\(A\) en \(B\) sluiten elkaar uit, \(P(A) = 0{,}3\) en \(P(B) = 0{,}25\). Bereken \(P(A \cup B)\).", r"\(0{,}55\)", W),
                 ("kort", r"\(P(X = 0) = 0{,}12\). Bereken \(P(X \ge 1)\).", r"\(0{,}88\)", W),
             ]),
        dict(kop="Lezen uit een kruistabel",
             opdracht=r"Tweehonderd leerlingen, verdeeld naar geslacht en of ze een bril dragen. Vul eerst de totalen aan.",
             oefeningen=[
                 ("tabel", ["Groep", "bril", "geen bril", "totaal"],
                  [["jongens", "30", "70", None],
                   ["meisjes", "45", "55", None],
                   ["totaal", None, None, None]],
                  r"jongens \(100\), meisjes \(100\); bril \(75\), geen bril \(125\), totaal \(200\)", "120px"),
             ]),
        dict(kop="Kansen uit die kruistabel",
             opdracht=r"Let goed op waardoor je deelt.",
             oefeningen=[
                 ("kort", r"Bereken \(P(\text{bril})\).", r"\(\tfrac{75}{200} = 0{,}375\)", WW),
                 ("kort", r"Bereken \(P(\text{bril} \mid \text{meisje})\).", r"\(\tfrac{45}{100} = 0{,}45\)", WW),
                 ("kies", r"Zijn een bril dragen en een meisje zijn onafhankelijk?",
                  [r"ja, want beide groepen tellen \(100\) leerlingen",
                   r"nee, want \(P(\text{bril} \mid \text{meisje}) \neq P(\text{bril})\)",
                   r"ja, want het totaal is \(200\)",
                   r"dat kan je uit een kruistabel niet afleiden"], 1),
             ]),
        dict(kop="Onafhankelijk of niet",
             opdracht=r"Schrijf ja of nee, en bij nee waarom niet.",
             oefeningen=[
                 ("tabel", ["Situatie", "Onafhankelijk?"],
                  [["twee worpen met dezelfde dobbelsteen", None],
                   ["twee kaarten trekken zonder terugleggen", None],
                   ["twee kaarten trekken met terugleggen", None],
                   ["het weer van vandaag en het weer van morgen", None]],
                  "ja; nee, de eerste kaart verandert wat er nog in het spel zit; ja; nee, twee opeenvolgende dagen hangen samen",
                  "230px"),
             ]),
        dict(kop="Waar of niet waar: kansen",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"Er geldt altijd \(P(A \cup B) = P(A) + P(B)\).", False),
                 ("waar", r"Als \(P(A) = 1\), dan gebeurt \(A\) zeker.", True),
                 ("waar", r"\(P(A \mid B)\) en \(P(B \mid A)\) zijn altijd gelijk.", False),
                 ("waar", r"In een kansboom tellen de kansen op de takken uit één knoop samen tot \(1\).", True),
             ]),
        dict(kop="Kansbomen",
             opdracht=r"Teken de boom erbij en schrijf elke tak met haar kans.",
             oefeningen=[
                 ("open", r"Een zak bevat \(4\) groene en \(6\) oranje knikkers. Je trekt er twee zonder terugleggen. Bereken \(P(\text{twee keer groen})\).",
                  r"Eerste laag \(\tfrac{4}{10}\) en \(\tfrac{6}{10}\); na een groene blijven er \(3\) groene van de \(9\) over. Dus \(\tfrac{4}{10} \cdot \tfrac{3}{9} = \tfrac{12}{90} = \tfrac{2}{15}\).", 6),
                 ("open", r"Bereken bij diezelfde zak \(P(\text{precies één groene})\).",
                  r"Twee paden: \(\tfrac{4}{10} \cdot \tfrac{6}{9} = \tfrac{24}{90}\) en \(\tfrac{6}{10} \cdot \tfrac{4}{9} = \tfrac{24}{90}\). Samen \(\tfrac{48}{90} = \tfrac{8}{15}\).", 4),
             ]),
        dict(kop="Met de complementregel",
             opdracht=r"Reken eerst de tegengestelde gebeurtenis uit.",
             oefeningen=[
                 ("open", r"Je gooit vier keer met een munt. Bereken \(P(\text{minstens één keer munt})\) met de complementregel.",
                  r"\(P(X = 0) = \left(\tfrac{1}{2}\right)^{4} = \tfrac{1}{16}\), dus \(P(X \ge 1) = 1 - \tfrac{1}{16} = \tfrac{15}{16}\).", 3),
             ]),
        dict(kop="Binomiaal of niet",
             opdracht=r"Kruis aan of de situatie binomiaal verdeeld is, en zo niet welke voorwaarde ontbreekt.",
             oefeningen=[
                 ("tabel", ["Situatie", "Binomiaal?"],
                  [["het aantal zessen in dertig worpen met een dobbelsteen", None],
                   ["het aantal rode ballen bij vijf trekkingen zonder terugleggen uit een zak van tien", None],
                   ["het aantal worpen tot je de eerste zes gooit", None],
                   ["het aantal defecte stukken bij tachtig stukken met foutkans nul komma nul twee", None]],
                  r"ja; nee, \(p\) verandert per trekking; nee, \(n\) ligt niet vast; ja", "250px"),
             ]),
        dict(kop="De binomiale kansformule",
             opdracht=r"Schrijf de formule op met de juiste getallen ingevuld. Uitrekenen hoeft niet.",
             oefeningen=[
                 ("rij", [(r"\(n = 8\), \(p = 0{,}3\), \(P(X = 2)\)", r"\(\binom{8}{2}\,0{,}3^{2}\,0{,}7^{6}\)"),
                          (r"\(n = 12\), \(p = 0{,}25\), \(P(X = 5)\)", r"\(\binom{12}{5}\,0{,}25^{5}\,0{,}75^{7}\)"),
                          (r"\(n = 6\), \(p = 0{,}5\), \(P(X = 0)\)", r"\(0{,}5^{6} = \tfrac{1}{64}\)"),
                          (r"\(n = 9\), \(p = 0{,}4\), \(P(X = 9)\)", r"\(0{,}4^{9}\)")],
                  r"Welke uitdrukking hoort erbij?", WL),
                 ("kort", r"\(n = 5\) en \(p = 0{,}5\). Bereken \(P(X = 5)\) als breuk.", r"\(\tfrac{1}{32}\)", W),
                 ("kort", r"Bereken \(\binom{7}{3}\).", r"\(35\)", W),
             ]),
        dict(kop="Verwachtingswaarde en standaardafwijking",
             opdracht=r"Vul aan. Rond \(\sigma\) af op één cijfer na de komma.",
             oefeningen=[
                 ("tabel", ["n", "p", "E(X)", "σ"],
                  [["60", "1/6", None, None],
                   ["100", "0,2", None, None],
                   ["40", "0,5", None, None],
                   ["200", "0,05", None, None]],
                  r"\(10\) en \(2{,}9\); \(20\) en \(4\); \(20\) en \(3{,}2\); \(10\) en \(3{,}1\)", "120px"),
                 ("kort", r"Bij welke \(p\) is \(\sigma\) het grootst, als \(n\) vastligt?", r"\(p = 0{,}5\)", W),
             ]),
        dict(kop="Wat zegt dit resultaat?",
             opdracht=r"Kruis de juiste uitleg aan.",
             oefeningen=[
                 ("kies", r"Bij \(X \sim \text{Bin}(20;\ 0{,}5)\) vind je \(P(X = 10) \approx 0{,}18\). Wat betekent dat?",
                  [r"tien is de meest waarschijnlijke uitkomst, maar komt in ongeveer één op vijf reeksen voor",
                   r"in ongeveer één op vijf reeksen krijg je minstens tien successen",
                   r"in ongeveer één op vijf reeksen krijg je hoogstens tien successen",
                   r"de uitkomst ligt met zekerheid tussen negen en elf successen"], 0),
                 ("kies", r"Een test heeft \(40\) meerkeuzevragen met telkens \(4\) opties, en je gokt alles. Hoeveel is \(E(X)\)?",
                  [r"\(10\)", r"\(4\)", r"\(20\)", r"\(40\)"], 0),
                 ("kies", r"Bij diezelfde test is \(\sigma = \sqrt{40 \cdot 0{,}25 \cdot 0{,}75}\). Hoeveel is dat ongeveer?",
                  [r"\(2{,}7\)", r"\(7{,}5\)", r"\(1{,}6\)", r"\(10\)"], 0),
             ]),
        dict(kop="Waar of niet waar: verdelingen",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"Bij \(X \sim \text{Bin}(n, p)\) kan \(X\) de waarde \(n + 1\) aannemen.", False),
                 ("waar", r"\(E(X)\) van een binomiale verdeling is altijd een geheel getal.", False),
                 ("waar", r"Een continue kansvariabele kan elke waarde in een interval aannemen.", True),
                 ("waar", r"De variantie is de standaardafwijking in het kwadraat.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht=r"Schrijf in volle zinnen.",
             oefeningen=[
                 ("open", r"Leg uit waarom twee trekkingen zonder terugleggen niet onafhankelijk zijn, en wat er verandert mét terugleggen.",
                  r"Zonder terugleggen verandert de eerste trekking de inhoud, dus \(P(A \mid B) \neq P(A)\) en mag je de kansen niet zomaar vermenigvuldigen. Mét terugleggen is de inhoud bij elke trekking dezelfde, dus \(P(A \cap B) = P(A) \cdot P(B)\).", 4),
                 ("open", r"Een machine maakt stukken met foutkans \(p = 0{,}02\). Bij \(50\) stukken is \(E(X) = 1\). Waarom betekent dat niet dat er altijd precies één fout stuk zal zijn?",
                  r"\(E(X)\) is het gemiddelde op lange termijn, geen voorspelling van één reeks. Met \(\sigma = \sqrt{50 \cdot 0{,}02 \cdot 0{,}98} \approx 0{,}99\) is nul of twee fouten net zo gewoon.", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht=r"Schrijf in volle zinnen, met je berekening erbij.",
             oefeningen=[
                 ("open", r"Je mag kiezen tussen \(100\) worpen met \(p = 0{,}5\) en \(400\) worpen met \(p = 0{,}125\). Beide geven \(E(X) = 50\). Bij welke van de twee ligt het resultaat gemiddeld het dichtst bij \(50\)? Reken \(\sigma\) uit.",
                  r"Links \(\sigma = \sqrt{100 \cdot 0{,}5 \cdot 0{,}5} = 5\), rechts \(\sigma = \sqrt{400 \cdot 0{,}125 \cdot 0{,}875} \approx 6{,}6\). Bij de eerste liggen de uitkomsten dus dichter bij \(50\).", 5),
                 ("open", r"Waarom mag je \(P(A \mid B)\) niet berekenen door door het totaal te delen? Gebruik een voorbeeld.",
                  r"Bij een voorwaardelijke kans is \(B\) al gebeurd, dus je deelt door \(P(B)\) en niet door alles. Van \(200\) leerlingen dragen er \(45\) van de \(100\) meisjes een bril: \(P(\text{bril} \mid \text{meisje}) = \tfrac{45}{100}\), niet \(\tfrac{45}{200}\).", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-statistiek-normale-verdeling-en-hypothesetoets-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Statistiek: normale verdeling en hypothesetoets",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De z-score",
             opdracht=r"Bereken \(z = \dfrac{x - \mu}{\sigma}\).",
             oefeningen=[
                 ("tabel", ["μ", "σ", "meting x", "z-score"],
                  [["100", "15", "130", None], ["50", "4", "46", None],
                   ["20", "5", "20", None], ["64", "8", "84", None]],
                  r"\(2\); \(-1\); \(0\); \(2{,}5\)", "120px"),
             ]),
        dict(kop="Terugrekenen vanaf een z-score",
             opdracht=r"Vul de ontbrekende grootheid in.",
             oefeningen=[
                 ("kort", r"\(\mu = 60\), \(\sigma = 4\) en \(z = 1{,}5\). Bereken \(x\).", r"\(x = 66\)", W),
                 ("kort", r"\(\mu = 500\), \(\sigma = 100\) en \(z = -0{,}8\). Bereken \(x\).", r"\(x = 420\)", W),
                 ("kort", r"\(x = 35\), \(\mu = 30\) en \(z = 2{,}5\). Bereken \(\sigma\).", r"\(\sigma = 2\)", W),
             ]),
        dict(kop="Scores vergelijken",
             opdracht=r"Reken bij elke meting de z-score uit en vergelijk pas daarna.",
             oefeningen=[
                 ("open", r"Twee leerlingen halen \(70\,\%\): de ene in een klas met \(\mu = 60\) en \(\sigma = 5\), de andere in een klas met \(\mu = 65\) en \(\sigma = 10\). Wie scoorde relatief beter?",
                  r"De eerste: \(z = \dfrac{70-60}{5} = 2\) tegenover \(z = \dfrac{70-65}{10} = 0{,}5\). De z-score maakt scores uit verschillende groepen vergelijkbaar.", 4),
             ]),
        dict(kop="Tijden vergelijken",
             opdracht=r"Bij een tijd is een lagere waarde beter. Let daarop bij je besluit.",
             oefeningen=[
                 ("open", r"Een loper doet \(11{,}2\) s op de \(100\) m, waar \(\mu = 12{,}0\) en \(\sigma = 0{,}5\). Een zwemster doet \(31{,}0\) s op de \(50\) m, waar \(\mu = 33{,}0\) en \(\sigma = 1{,}6\). Wie presteert relatief beter?",
                  r"\(z = \dfrac{11{,}2-12{,}0}{0{,}5} = -1{,}6\) en \(z = \dfrac{31{,}0-33{,}0}{1{,}6} = -1{,}25\). Bij een tijd is lager beter, dus de loper staat verder van het gemiddelde in de goede richting.", 5),
             ]),
        dict(kop="De vuistregel",
             opdracht=r"Vul in. Ken de drie percentages uit het hoofd.",
             oefeningen=[
                 ("tabel", ["Binnen hoeveel standaardafwijkingen", "Ongeveer welk deel"],
                  [["één", None], ["twee", None], ["drie", None]],
                  r"\(68\,\%\); \(95\,\%\); \(99{,}7\,\%\)", "230px"),
                 ("kort", r"Hoeveel procent ligt buiten \(\mu \pm 2\sigma\)?", r"\(5\,\%\)", W),
                 ("kort", r"Hoeveel procent ligt tussen \(\mu\) en \(\mu + \sigma\)?", r"\(34\,\%\)", W),
             ]),
        dict(kop="Kansen schatten met de vuistregel",
             opdracht=r"De lengte van volwassen mannen is bij benadering \(N(\mu = 178, \sigma = 7)\), in centimeter.",
             oefeningen=[
                 ("kort", r"Tussen welke twee lengtes ligt ongeveer \(95\,\%\)?", r"\(164\) cm en \(192\) cm", WW),
                 ("kort", r"Hoeveel procent is groter dan \(185\) cm?", r"ongeveer \(16\,\%\)", WW),
                 ("kort", r"Hoeveel procent is kleiner dan \(164\) cm?", r"ongeveer \(2{,}5\,\%\)", WW),
             ]),
        dict(kop="Waar of niet waar: de normale verdeling",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"De totale oppervlakte onder een Gausskromme hangt af van \(\sigma\).", False),
                 ("waar", r"Een z-score heeft geen eenheid.", True),
                 ("waar", r"Bij \(N(0, 1)\) ligt de top in \(x = 0\).", True),
                 ("waar", r"Een duidelijk scheef histogram past goed bij het normale model.", False),
             ]),
        dict(kop="Steekproeven beoordelen",
             opdracht=r"Schrijf bij elke opzet op welk probleem er is, of dat er geen is.",
             oefeningen=[
                 ("open", r"Een sportblad vraagt zijn lezers online of de gemeente meer geld aan sport moet besteden. Wat is hier mis?",
                  r"Vrijwillige respons én een vertekende groep: lezers van een sportblad zijn geen doorsnede. Meer stemmen lost dat niet op; het is een niet-steekproeffout.", 4),
             ]),
        dict(kop="Twee soorten fouten uitleggen",
             opdracht=r"Schrijf in volle zinnen.",
             oefeningen=[
                 ("open", r"Leg het verschil uit tussen een steekproeffout en een niet-steekproeffout, met bij elk hoe je ze kleiner maakt.",
                  r"Een steekproeffout komt door het toeval van de trekking en wordt kleiner met meer deelnemers. Een niet-steekproeffout zit in de opzet en blijft ook bij duizend deelnemers bestaan; die los je alleen op door de opzet te verbeteren.", 5),
                 ("waar", r"Een grotere steekproef maakt een scheve opzet weer recht.", False),
             ]),
        dict(kop="Welke fout is het",
             opdracht=r"Schrijf bij elke rij steekproeffout of niet-steekproeffout.",
             oefeningen=[
                 ("tabel", ["Situatie", "Welke fout?"],
                  [["je trok honderd namen uit het bevolkingsregister en kreeg toevallig wat meer vrouwen", None],
                   ["je vraagt het enkel aan wie 's morgens in het station staat", None],
                   ["je vraag is zo geformuleerd dat ja het vriendelijkste antwoord lijkt", None],
                   ["je trok tweeduizend namen en het gemiddelde wijkt een beetje af", None]],
                  "steekproeffout; niet-steekproeffout; niet-steekproeffout; steekproeffout", "200px"),
             ]),
        dict(kop="Samenhang lezen",
             opdracht=r"Kruis aan of vul in.",
             oefeningen=[
                 ("kies", r"In een puntenwolk lopen de punten duidelijk van linksboven naar rechtsonder. Welke \(r\) past daarbij?",
                  [r"\(-0{,}9\)", r"\(0{,}9\)", r"\(0{,}1\)", r"\(1{,}4\)"], 0),
                 ("kies", r"Welke waarde kan \(r\) nooit aannemen?",
                  [r"\(1{,}2\)", r"\(-1\)", r"\(0\)", r"\(0{,}95\)"], 0),
                 ("kort", r"Je vindt \(r = -0{,}05\). Is er een sterk lineair verband? Ja of nee.", r"nee", W),
             ]),
        dict(kop="Samenhang is geen oorzaak",
             opdracht=r"Zoek telkens de verborgen variabele.",
             oefeningen=[
                 ("open", r"In gemeenten met meer ooievaars worden meer kinderen geboren. Verklaar die samenhang zonder oorzakelijk verband.",
                  r"Een derde verborgen variabele: landelijke gemeenten hebben zowel meer ooievaarsnesten als meer jonge gezinnen. Samenhang is geen oorzaak.", 4),
             ]),
        dict(kop="Nog een verborgen variabele",
             opdracht=r"Zoek wat allebei de grootheden omhoog duwt.",
             oefeningen=[
                 ("open", r"Bij branden waar meer brandweerwagens komen, is er meer schade. Waarom bewijst dat niet dat brandweerwagens schade veroorzaken?",
                  r"De grootte van de brand is de verborgen variabele: hoe groter de brand, hoe meer wagens er komen én hoe meer schade er is.", 4),
             ]),
        dict(kop="Hypothesen en p-waarden",
             opdracht=r"Vul aan en kruis het juiste besluit aan.",
             oefeningen=[
                 ("tabel", ["Begrip", "Wat het betekent"],
                  [["nulhypothese \\(H_{0}\\)", None], ["p-waarde", None], ["type I-fout", None], ["type II-fout", None]],
                  r"wat je probeert te verwerpen; de kans op zo'n resultaat of extremer als \(H_{0}\) waar is; verwerpen terwijl ze waar is; onterecht niet verwerpen",
                  "300px"),
                 ("kies", r"Er geldt \(p = 0{,}08\) en \(\alpha = 0{,}05\). Wat besluit je?",
                  [r"je verwerpt \(H_{0}\)", r"je houdt \(H_{0}\) aan, er is onvoldoende bewijs",
                   r"je bewijst dat \(H_{0}\) waar is", r"je kiest een ander significantieniveau"], 1),
                 ("kies", r"Er geldt \(p = 0{,}003\) en \(\alpha = 0{,}01\). Wat besluit je?",
                  [r"je verwerpt \(H_{0}\)", r"je houdt \(H_{0}\) aan",
                   r"je bewijst dat \(H_{1}\) waar is", r"je verhoogt \(\alpha\) tot \(0{,}05\)"], 0),
             ]),
        dict(kop="Doordenker: veel toetsen tegelijk",
             opdracht=r"Denk eerst na over hoeveel valse alarmen je sowieso verwacht.",
             oefeningen=[
                 ("open", r"Je toetst honderd verschillende hypothesen met \(\alpha = 0{,}05\) en vindt er vijf significant. Waarom is dat op zichzelf geen bewijs?",
                  r"Bij \(\alpha = 0{,}05\) verwacht je al ongeveer vijf valse alarmen op honderd toetsen, ook als er nergens een echt effect is. Wie veel toetst, moet de drempel strenger zetten of de vondst opnieuw onderzoeken.", 5),
             ]),
        dict(kop="Uitleggen",
             opdracht=r"Schrijf in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom is geen bewijs vinden niet hetzelfde als bewijzen dat er niets is?",
                  r"Een toets die niets vindt, kan ook te weinig deelnemers hebben gehad. Je besluit dan enkel dat er onvoldoende bewijs tegen \(H_{0}\) is.", 4),
             ]),
        dict(kop="Waarom de z-score",
             opdracht=r"Schrijf in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom zegt \(z = 2\) meer dan de mededeling dat een meting twee punten boven het gemiddelde ligt?",
                  r"Twee punten is veel in een groep met \(\sigma = 1\) en weinig in een groep met \(\sigma = 20\). De z-score rekent in standaardafwijkingen en is daardoor over groepen heen vergelijkbaar.", 4),
             ]),
        dict(kop="Doordenker: een medische test",
             opdracht=r"Reken eerst, besluit daarna.",
             oefeningen=[
                 ("open", r"Een test is positief bij \(99\,\%\) van de zieken en bij \(2\,\%\) van de gezonden. Eén op duizend mensen is ziek. Waarom is een positieve test toch meestal vals alarm? Reken met tienduizend mensen.",
                  r"Van \(10\,000\) mensen zijn er \(10\) ziek, waarvan er ongeveer \(10\) positief testen. Van de \(9990\) gezonden testen er ongeveer \(200\) positief. Dus van de \(210\) positieven zijn er maar \(10\) echt ziek, ongeveer \(5\,\%\).", 7),
             ]),
        dict(kop="Waar of niet waar: toetsen",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"De p-waarde is de kans dat \(H_{0}\) waar is.", False),
                 ("waar", r"De kans op een type I-fout is \(\alpha\).", True),
                 ("waar", r"Een eenzijdige toets gebruik je als je vooraf een richting verwacht.", True),
                 ("waar", r"Een kleiner significantieniveau maakt een type II-fout minder waarschijnlijk.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-matrices-en-hun-bewerkingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Matrices en hun bewerkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Dimensies",
             opdracht=r"Vul in. Eerst het aantal rijen, dan het aantal kolommen.",
             oefeningen=[
                 ("tabel", ["Bewerking", "Kan het?", "Dimensie van het resultaat"],
                  [[r"\(3 \times 2\) plus \(3 \times 2\)", None, None],
                   [r"\(2 \times 3\) maal \(3 \times 5\)", None, None],
                   [r"\(2 \times 3\) maal \(2 \times 3\)", None, None],
                   [r"\(4 \times 1\) getransponeerd", None, None]],
                  r"ja, \(3 \times 2\); ja, \(2 \times 5\); nee; ja, \(1 \times 4\)", "190px"),
                 ("kort", r"Hoeveel elementen heeft een matrix van \(3 \times 7\)?", r"\(21\)", W),
                 ("kort", r"Hoeveel rijen heeft een kolommatrix met \(6\) elementen?", r"\(6\)", W),
             ]),
        dict(kop="Optellen en met een getal vermenigvuldigen",
             opdracht=r"Neem \(A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\) en \(B = \begin{pmatrix} 0 & 5 \\ -1 & 2 \end{pmatrix}\).",
             oefeningen=[
                 ("open", r"Bereken \(A + B\).",
                  r"\(\begin{pmatrix} 1 & 7 \\ 2 & 6 \end{pmatrix}\)", 3),
                 ("open", r"Bereken \(3A - B\).",
                  r"\(3A = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}\), dus \(3A - B = \begin{pmatrix} 3 & 1 \\ 10 & 10 \end{pmatrix}\)", 4),
             ]),
        dict(kop="Waar of niet waar: bewerkingen",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"Er geldt \((A + B)^{T} = A^{T} + B^{T}\).", True),
                 ("waar", r"Er geldt \((A \cdot B)^{T} = A^{T} \cdot B^{T}\).", False),
                 ("waar", r"Er geldt \(A \cdot I = A\) voor elke vierkante matrix \(A\).", True),
                 ("waar", r"Je kan elke twee matrices bij elkaar optellen.", False),
             ]),
        dict(kop="Matrices vermenigvuldigen",
             opdracht=r"Neem opnieuw \(A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\) en \(B = \begin{pmatrix} 0 & 5 \\ -1 & 2 \end{pmatrix}\). Reken elk element uit als een rij tegen een kolom.",
             oefeningen=[
                 ("open", r"Bereken \(A \cdot B\).",
                  r"\(\begin{pmatrix} -2 & 9 \\ -4 & 23 \end{pmatrix}\)", 5),
                 ("open", r"Bereken \(\begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & -1 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 0 & 4 \\ 1 & -2 \end{pmatrix}\).",
                  r"\(\begin{pmatrix} 4 & -3 \\ 5 & 9 \end{pmatrix}\)", 6),
             ]),
        dict(kop="Bijzondere matrices",
             opdracht=r"Schrijf bij elke omschrijving de naam.",
             oefeningen=[
                 ("rij", [(r"elk element is nul", r"de nulmatrix \(O\)"),
                          (r"enen op de hoofddiagonaal, elders nullen", r"de eenheidsmatrix \(I\)"),
                          (r"evenveel rijen als kolommen", r"een vierkante matrix"),
                          (r"\(A = A^{T}\)", r"een symmetrische matrix"),
                          (r"vierkant, en alles buiten de hoofddiagonaal is nul", r"een diagonaalmatrix")],
                  r"Welke matrix?", WL),
             ]),
        dict(kop="Transponeren",
             opdracht=r"Geef telkens de gevraagde dimensie.",
             oefeningen=[
                 ("rij", [(r"\(A^{T}\) als \(A\) van \(2 \times 7\) is", r"\(7 \times 2\)"),
                          (r"\((A \cdot B)^{T}\) als \(A\) is \(3 \times 4\) en \(B\) is \(4 \times 2\)", r"\(2 \times 3\)"),
                          (r"\(A^{T} \cdot A\) als \(A\) van \(5 \times 2\) is", r"\(2 \times 2\)"),
                          (r"het aantal rijen van \(A^{T}\) als \(A\) van \(6 \times 1\) is", r"\(1\)")],
                  r"Welke dimensie?", WW),
             ]),
        dict(kop="Determinanten van orde twee",
             opdracht=r"Reken uit, of leid het antwoord af uit een eigenschap.",
             oefeningen=[
                 ("rij", [(r"\(\det\begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}\)", r"\(5\)"),
                          (r"\(\det\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\)", r"\(0\)"),
                          (r"\(\det\begin{pmatrix} 5 & -1 \\ 3 & 2 \end{pmatrix}\)", r"\(13\)"),
                          (r"\(\det I_{2}\)", r"\(1\)"),
                          (r"\(\det A\) als \(A\) twee gelijke rijen heeft", r"\(0\)")],
                  r"Wat is de determinant?", WW),
             ]),
        dict(kop="De inverse van orde twee",
             opdracht=r"Er geldt \(A^{-1} = \dfrac{1}{\det A} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\).",
             oefeningen=[
                 ("kort", r"Bereken \(\det\begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}\).", r"\(10\)", W),
                 ("open", r"Bereken de inverse van \(\begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}\) en controleer met \(A \cdot A^{-1} = I\).",
                  r"\(A^{-1} = \tfrac{1}{10}\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 0{,}6 & -0{,}7 \\ -0{,}2 & 0{,}4 \end{pmatrix}\). Het product met \(A\) geeft \(I_{2}\).", 6),
                 ("kies", r"Welke matrix heeft geen inverse?",
                  [r"\(\begin{pmatrix} 2 & 6 \\ 1 & 3 \end{pmatrix}\)", r"\(\begin{pmatrix} 2 & 6 \\ 1 & 4 \end{pmatrix}\)",
                   r"\(\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}\)", r"\(\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}\)"], 0),
             ]),
        dict(kop="Waar of niet waar: determinant en rang",
             opdracht=r"Omcirkel waar of niet waar.",
             oefeningen=[
                 ("waar", r"Er geldt \(\det A^{T} = \det A\).", True),
                 ("waar", r"Een matrix van \(2 \times 3\) heeft een determinant.", False),
                 ("waar", r"\(\text{rang}(A)\) kan groter zijn dan het aantal rijen van \(A\).", False),
                 ("waar", r"Een matrix heeft maar één rijcanonieke vorm.", True),
             ]),
        dict(kop="De rang",
             opdracht=r"Vul in of reken uit.",
             oefeningen=[
                 ("kort", r"Bereken \(\text{rang}(I_{4})\).", r"\(4\)", W),
                 ("kort", r"Bereken \(\text{rang}(O)\).", r"\(0\)", W),
                 ("kort", r"\(A\) is van orde \(3\) en \(\det A = 0\). Wat weet je over \(\text{rang}(A)\)?", r"kleiner dan \(3\)", WW),
                 ("open", r"Bepaal de rang van \(\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{pmatrix}\) met rijoperaties.",
                  r"\(R_{2} = 2 \cdot R_{1}\), dus die rij valt weg. Er blijven twee rijen over die niet nul zijn: \(\text{rang}(A) = 2\). De matrix is dus niet inverteerbaar.", 6),
             ]),
        dict(kop="Een matrixproduct met betekenis",
             opdracht=r"Schrijf de matrices eerst op, reken daarna.",
             oefeningen=[
                 ("open", r"Een bakker verkoopt broden aan \(3\) euro en koffiekoeken aan \(1{,}50\) euro. Klant 1 koopt \(2\) broden en \(4\) koeken, klant 2 koopt \(1\) brood en \(8\) koeken. Schrijf dit als \(A \cdot P\) en reken de twee totalen uit.",
                  r"\(A = \begin{pmatrix} 2 & 4 \\ 1 & 8 \end{pmatrix}\) en \(P = \begin{pmatrix} 3 \\ 1{,}5 \end{pmatrix}\), dus \(A \cdot P = \begin{pmatrix} 12 \\ 15 \end{pmatrix}\): \(12\) euro en \(15\) euro.", 6),
                 ("open", r"Leg uit waarom \(\det A = 0\) betekent dat \(A\) geen inverse heeft.",
                  r"\(\det A = 0\) betekent dat de rijen van elkaar afhangen; de matrix verliest informatie en de bewerking is niet ongedaan te maken. De rang is dan kleiner dan de orde.", 4),
             ]),
        dict(kop="Rijoperaties",
             opdracht=r"Schrijf ze in notatie op.",
             oefeningen=[
                 ("open", r"Noem de drie elementaire rijoperaties en zeg welke bewerking niet mag.",
                  r"\(R_{i} \leftrightarrow R_{j}\), \(R_{i} \to k \cdot R_{i}\) met \(k \neq 0\), en \(R_{i} \to R_{i} + k \cdot R_{j}\). Vermenigvuldigen met \(0\) mag niet.", 4),
             ]),
        dict(kop="Doordenker: de volgorde telt",
             opdracht=r"Reken allebei de producten uit en vergelijk.",
             oefeningen=[
                 ("open", r"Toon met \(A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\) en \(B = \begin{pmatrix} 0 & 5 \\ -1 & 2 \end{pmatrix}\) dat \(A \cdot B \neq B \cdot A\).",
                  r"\(A \cdot B = \begin{pmatrix} -2 & 9 \\ -4 & 23 \end{pmatrix}\) en \(B \cdot A = \begin{pmatrix} 15 & 20 \\ 5 & 6 \end{pmatrix}\). De twee verschillen, dus het product is niet commutatief.", 7),
             ]),
        dict(kop="Doordenker: drie uitspraken in één",
             opdracht=r"Leg elk van de drie apart uit.",
             oefeningen=[
                 ("open", r"Een matrix \(A\) van orde \(3\) heeft twee rijen die elkaars dubbel zijn. Wat weet je over \(\det A\), over \(\text{rang}(A)\) en over \(A^{-1}\)?",
                  r"\(\det A = 0\), want twee rijen hangen van elkaar af. \(\text{rang}(A) \le 2\), want één rij geeft geen nieuwe informatie. En \(A^{-1}\) bestaat niet, want dat vraagt \(\det A \neq 0\).", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stelsels-oplossen-en-matrixmodellen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stelsels oplossen en matrixmodellen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van stelsel naar matrix en terug",
             opdracht="Schrijf de gevraagde vorm volledig uit.",
             oefeningen=[
                 ("open", r"Schrijf de uitgebreide coëfficiëntenmatrix van \(\left\{\begin{array}{l} 2x + 3y = 7 \\ x - y = 1 \end{array}\right.\)",
                  r"\(\left(\begin{array}{cc|c} 2 & 3 & 7 \\ 1 & -1 & 1 \end{array}\right)\)", 3),
                 ("open", r"Schrijf het stelsel dat hoort bij \(\left(\begin{array}{cc|c} 1 & -4 & 2 \\ 0 & 3 & 9 \end{array}\right)\)",
                  r"\(x - 4y = 2\) en \(3y = 9\). Daaruit volgt \(y = 3\) en \(x = 14\).", 3),
             ]),
        dict(kop="Welke rijoperatie mag?",
             opdracht="Kruis aan of de bewerking toegelaten is.",
             oefeningen=[
                 ("tabel", ["Rijoperatie", "Mag het?"],
                  [[r"\(R_{1} \leftrightarrow R_{3}\)", None],
                   [r"\(R_{2} \to -5 \cdot R_{2}\)", None],
                   [r"\(R_{1} \to R_{1} + 2 \cdot R_{3}\)", None],
                   [r"\(R_{3} \to 0 \cdot R_{3}\)", None]],
                  "ja; ja; ja; nee, dan verdwijnt er een vergelijking", "150px"),
             ]),
        dict(kop="Bepaald, onbepaald of strijdig",
             opdracht=r"Hierin is \(n\) het aantal onbekenden. Vul de laatste kolom aan.",
             oefeningen=[
                 ("tabel", [r"\(n\)", r"\(\text{rang}(A)\)", r"\(\text{rang}(A \mid B)\)", "Soort stelsel"],
                  [["2", "1", "2", None], ["4", "3", "3", None], ["3", "3", "3", None],
                   ["5", "4", "5", None], ["4", "2", "2", None]],
                  "strijdig; onbepaald; bepaald; strijdig; onbepaald", "150px"),
             ]),
        dict(kop="Hoeveel vrijheidsgraden?",
             opdracht=r"Reken telkens \(n - \text{rang}(A)\) uit.",
             oefeningen=[
                 ("rij", [(r"\(n = 3\) en \(\text{rang}(A) = 1\)", "2"),
                          (r"\(n = 5\) en \(\text{rang}(A) = 2\)", "3"),
                          (r"\(n = 4\) en \(\text{rang}(A) = 4\)", "0"),
                          (r"\(n = 6\) en \(\text{rang}(A) = 2\)", "4")],
                  "Aantal vrijheidsgraden", W),
             ]),
        dict(kop="Twee rechten in beeld",
             opdracht="Schrijf op welk soort stelsel bij elke stand hoort.",
             oefeningen=[
                 ("rij", [("de twee rechten snijden elkaar in één punt", "bepaald"),
                          ("de twee rechten vallen samen", "onbepaald"),
                          ("de twee rechten lopen evenwijdig en vallen niet samen", "strijdig")],
                  "Welk soort stelsel?", WW),
             ]),
        dict(kop="Lees de rijcanonieke vorm",
             opdracht="Schrijf per matrix op wat ze over de oplossingen zegt.",
             oefeningen=[
                 ("kort", r"\(\left(\begin{array}{cc|c} 1 & 0 & 3 \\ 0 & 1 & -2 \end{array}\right)\)",
                  r"\(x = 3\) en \(y = -2\)", WL),
                 ("kort", r"\(\left(\begin{array}{ccc|c} 1 & 0 & 2 & 5 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right)\)",
                  "oneindig veel oplossingen, met één vrijheidsgraad", WL),
                 ("kort", r"\(\left(\begin{array}{ccc|c} 1 & 0 & 2 & 5 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & 0 & 7 \end{array}\right)\)",
                  r"geen oplossing, het stelsel is strijdig en \(V = \emptyset\)", WL),
             ]),
        dict(kop="Twee vergelijkingen oplossen",
             opdracht="Werk met rijoperaties en schrijf je stappen op.",
             oefeningen=[
                 ("open", r"Los op: \(\left\{\begin{array}{l} x + 2y = 8 \\ 3x - y = 3 \end{array}\right.\)",
                  r"\(R_{2} \to R_{2} - 3 \cdot R_{1}\) geeft \(-7y = -21\), dus \(y = 3\) en \(x = 2\). Het stelsel is bepaald.", 5),
                 ("open", r"Los op: \(\left\{\begin{array}{l} 2x - y = 4 \\ 4x - 2y = 7 \end{array}\right.\)",
                  r"\(R_{2} \to R_{2} - 2 \cdot R_{1}\) geeft \(\left(\begin{array}{cc|c} 0 & 0 & -1 \end{array}\right)\), dus \(0 = -1\). Het stelsel is strijdig en \(V = \emptyset\); de twee rechten zijn evenwijdig.", 5),
             ]),
        dict(kop="Drie vergelijkingen oplossen",
             opdracht="Neem de tijd en schrijf elke rijoperatie op.",
             oefeningen=[
                 ("open", r"Los op: \(\left\{\begin{array}{l} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{array}\right.\)",
                  r"\(x = 1\), \(y = 2\) en \(z = 3\). Het stelsel is bepaald. Proef: \(1 + 2 + 3 = 6\), \(2 - 2 + 3 = 3\) en \(1 + 4 - 3 = 2\).", 8),
             ]),
        dict(kop="Waar of niet waar: stelsels",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een stelsel met evenveel vergelijkingen als onbekenden is altijd bepaald.", False),
                 ("waar", "Twee rijen verwisselen verandert de oplossingenverzameling niet.", True),
                 ("waar", r"Een rij \(\left(\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right)\) maakt een stelsel strijdig.", False),
                 ("waar", r"Is \(\det A \neq 0\), dan heeft \(A \cdot X = B\) precies één oplossing.", True),
             ]),
        dict(kop="Oplossen met de inverse",
             opdracht="Reken uit en schrijf je tussenstappen op.",
             oefeningen=[
                 ("open", r"Gegeven \(A = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}\) en \(B = \begin{pmatrix} 5 \\ 8 \end{pmatrix}\). Bereken \(\det A\), dan \(A^{-1}\) en dan \(X = A^{-1} \cdot B\).",
                  r"\(\det A = 4 - 3 = 1\), dus \(A^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}\) en \(X = \begin{pmatrix} 2 \\ 1 \end{pmatrix}\). Proef: \(2 \cdot 2 + 1 = 5\) en \(3 \cdot 2 + 2 = 8\).", 6),
                 ("open", r"Waarom kan je \(X = A^{-1} \cdot B\) niet gebruiken als \(\det A = 0\)?",
                  r"Dan bestaat \(A^{-1}\) niet. Het stelsel is dan onbepaald of strijdig, en je lost het met rijoperaties op.", 3),
             ]),
        dict(kop="Een stelsel uit een context",
             opdracht="Stel eerst het stelsel op, los daarna pas op.",
             oefeningen=[
                 ("open", "Drie koffies en twee thees kosten samen elf euro. Eén koffie en vier thees kosten samen twaalf euro. Hoeveel kost één koffie?",
                  r"\(3k + 2t = 11\) en \(k + 4t = 12\) geven \(t = 2{,}5\) en \(k = 2\). Een koffie kost twee euro.", 6),
                 ("open", "Een winkel noteert twee bestellingen van dezelfde artikelen, en de tweede is precies het dubbel van de eerste. Kan je daar de prijs per artikel uit halen?",
                  "Nee. De tweede rij geeft geen nieuwe informatie en valt in de rijcanonieke vorm weg, dus de rang is te klein en het stelsel is onbepaald.", 4),
             ]),
        dict(kop="Rekenen met een overgangsmatrix",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", r"Schrijf de formule voor de toestand na \(k\) stappen.", r"\(X_{k} = T^{k} \cdot X_{0}\)", WL),
                 ("kort", r"Tot welke macht verhef je \(T\) voor de toestand na \(12\) stappen?", "12", W),
                 ("kort", r"Hoeveel rijen heeft \(T\) bij een model met \(3\) toestanden?", "3", W),
             ]),
        dict(kop="Een Markov-matrix nakijken",
             opdracht=r"Werk met \(T = \begin{pmatrix} 0{,}7 & 0{,}2 \\ 0{,}3 & 0{,}8 \end{pmatrix}\).",
             oefeningen=[
                 ("open", r"Is \(T\) een Markov-matrix? Reken de kolommen na.",
                  r"Ja. De eerste kolom geeft \(0{,}7 + 0{,}3 = 1\) en de tweede \(0{,}2 + 0{,}8 = 1\).", 3),
                 ("open", r"Bereken \(X_{1} = T \cdot X_{0}\) met \(X_{0} = \begin{pmatrix} 100 \\ 100 \end{pmatrix}\).",
                  r"\(X_{1} = \begin{pmatrix} 90 \\ 110 \end{pmatrix}\), want \(0{,}7 \cdot 100 + 0{,}2 \cdot 100 = 90\) en \(0{,}3 \cdot 100 + 0{,}8 \cdot 100 = 110\).", 5),
             ]),
        dict(kop="Waar of niet waar: overgangsmatrices",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een overgangsmatrix heeft evenveel rijen als kolommen.", True),
                 ("waar", r"In een Markov-matrix mag een kolom optellen tot \(1{,}2\).", False),
             ]),
        dict(kop="De graaf en zijn matrix",
             opdracht=r"Een graaf heeft de knopen \(P\), \(Q\) en \(R\), met een verbinding tussen \(P\) en \(Q\) en een tussen \(Q\) en \(R\).",
             oefeningen=[
                 ("open", r"Schrijf de verbindingsmatrix van die graaf op, in de volgorde \(P\), \(Q\), \(R\).",
                  r"\(M = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}\)", 5),
                 ("open", r"Hoeveel wegen van lengte \(2\) lopen er van \(P\) naar \(R\)? Reken het na met \(M^{2}\).",
                  r"Eén, via \(Q\). In \(M^{2}\) staat op die plaats \(0 \cdot 0 + 1 \cdot 1 + 0 \cdot 0 = 1\).", 5),
             ]),
        dict(kop="Waar of niet waar: grafen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Het kwadraat van een verbindingsmatrix telt de wegen van lengte \(2\).", True),
                 ("waar", r"Een graaf met vijf knopen geeft een verbindingsmatrix van orde \(4\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom mag je een rij wel met \(-3\) vermenigvuldigen en niet met \(0\)?",
                  r"Bij \(-3\) kan je de stap omkeren door weer door \(-3\) te delen, dus de oplossingen blijven dezelfde. Bij \(0\) wordt de hele vergelijking \(0 = 0\) en ben je de informatie kwijt.", 4),
                 ("open", "Waarom volstaat evenveel vergelijkingen als onbekenden niet om te besluiten dat een stelsel bepaald is?",
                  r"Omdat twee vergelijkingen hetzelfde kunnen zeggen. Dan telt die rij maar één keer mee en is \(\text{rang}(A)\) kleiner dan \(n\).", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je besluit op.",
             oefeningen=[
                 ("open", r"Een stelsel met drie onbekenden heeft \(\text{rang}(A) = \text{rang}(A \mid B) = 2\). Je voegt een vierde vergelijking toe en allebei de rangen worden \(3\). Wat verandert er aan de oplossingen?",
                  "Eerst waren er oneindig veel, met één vrijheidsgraad. Nu is er precies één, want de nieuwe vergelijking gaf echt nieuwe informatie.", 5),
                 ("open", r"Voor een bepaalde \(X\) geldt \(T \cdot X = X\). Wat is dan \(T^{20} \cdot X\)? Leg uit.",
                  r"Dat blijft \(X\). Elke vermenigvuldiging met \(T\) geeft \(X\) terug, dus ook na twintig keer. \(X\) is een evenwichtstoestand.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-algebraische-structuren-en-groepen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Algebraïsche structuren en groepen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vier eigenschappen",
             opdracht="Schrijf bij elke omschrijving de naam van de eigenschap.",
             oefeningen=[
                 ("rij", [(r"het resultaat ligt altijd weer in \(G\)", "intern"),
                          ("de haakjes mogen verschuiven", "associatief"),
                          (r"er is een \(e\) met \(a \ast e = a\)", "het neutraal element"),
                          (r"elke \(a\) heeft een partner die \(e\) geeft", "het invers element")],
                  "Welke eigenschap?", WL),
             ]),
        dict(kop="In symbolen",
             opdracht=r"Schrijf elke eigenschap met \(\ast\), \(e\) en \(a^{-1}\).",
             oefeningen=[
                 ("rij", [("intern", r"\(a \ast b \in G\)"),
                          ("associatief", r"\(a \ast (b \ast c) = (a \ast b) \ast c\)"),
                          ("commutatief", r"\(a \ast b = b \ast a\)"),
                          ("invers element", r"\(a \ast a^{-1} = a^{-1} \ast a = e\)")],
                  "In symbolen", "350px"),
             ]),
        dict(kop="Groep of geen groep",
             opdracht="Kruis aan. Is het geen groep, schrijf dan wat er ontbreekt.",
             oefeningen=[
                 ("tabel", ["Verzameling met bewerking", "Groep?", "Zo nee, wat ontbreekt"],
                  [[r"\((\mathbb{Z}, +)\)", None, None],
                   [r"\((\mathbb{N}, +)\)", None, None],
                   [r"\((\mathbb{Z}, \cdot)\)", None, None],
                   [r"\((\mathbb{R}_{0}, \cdot)\)", None, None],
                   ["de oneven gehele getallen met de optelling", None, None],
                   [r"\((\mathbb{R}, \cdot)\)", None, None]],
                  "ja; nee, het invers element; nee, het invers element; ja; nee, de bewerking is niet intern; nee, nul heeft geen invers element", "190px"),
             ]),
        dict(kop="Waarom het geen groep is",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", r"Welke eigenschap ontbreekt er bij \((\mathbb{N}, +)\)?", "het invers element", WL),
                 ("kort", r"Geef een tegenvoorbeeld dat toont dat de deling niet intern is in \(\mathbb{Z}\).",
                  r"\(1 : 2 = 0{,}5\), en dat ligt niet in \(\mathbb{Z}\)", WL),
                 ("kort", "Welk reëel getal heeft geen invers element voor de vermenigvuldiging?", "nul", W),
             ]),
        dict(kop="Het neutraal element",
             opdracht=r"Schrijf telkens \(e\) op.",
             oefeningen=[
                 ("rij", [(r"\((\mathbb{Z}, +)\)", r"\(0\)"),
                          (r"\((\mathbb{R}, \cdot)\)", r"\(1\)"),
                          ("de matrices van orde 2 met de optelling", r"de nulmatrix \(O\)"),
                          ("de matrices van orde 2 met de vermenigvuldiging", r"de eenheidsmatrix \(I\)")],
                  r"Wat is \(e\)?", WW),
             ]),
        dict(kop="Het invers element",
             opdracht="Schrijf telkens het invers element op.",
             oefeningen=[
                 ("rij", [(r"\(7\) in \((\mathbb{Z}, +)\)", r"\(-7\)"),
                          (r"\(4\) in \((\mathbb{R}_{0}, \cdot)\)", r"\(\tfrac{1}{4}\)"),
                          (r"\(e\) in om het even welke groep", r"\(e\) zelf"),
                          (r"\(a^{-1}\) in om het even welke groep", r"\(a\)")],
                  "Het invers element", WW),
             ]),
        dict(kop="Waar of niet waar: groepen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\((\mathbb{Q}, +)\) is een groep.", True),
                 ("waar", "Elke eindige groep is commutatief.", False),
                 ("waar", r"In \((\mathbb{R}_{0}, \cdot)\) is \(1\) het neutraal element.", True),
                 ("waar", "Een oneindige verzameling kan nooit een groep vormen.", False),
             ]),
        dict(kop="Hoe groot wordt de tabel",
             opdracht="Vul aan. De kopregel en de kopkolom tellen niet mee.",
             oefeningen=[
                 ("tabel", ["Aantal elementen", "Aantal rijen", "Aantal vakjes"],
                  [["3", None, None], ["4", None, None], ["7", None, None]],
                  "3 en 9; 4 en 16; 7 en 49", "150px"),
             ]),
        dict(kop="Lezen in de tabel",
             opdracht="Schrijf bij elke waarneming je besluit.",
             oefeningen=[
                 ("rij", [("de tabel is symmetrisch om de hoofddiagonaal", "de groep is commutatief"),
                          ("de rij van een element herhaalt de kopregel", r"dat element is \(e\)"),
                          (r"op de hoofddiagonaal staat overal \(e\)", "elk element is zijn eigen invers"),
                          ("een element komt twee keer voor in één rij", "dan is het geen groep")],
                  "Wat besluit je?", WL),
             ]),
        dict(kop="Een Cayley-tabel opstellen",
             opdracht=r"Werk met \(\{0, 1, 2\}\) en de optelling modulo \(3\): je telt op en houdt enkel de rest na deling door \(3\) over.",
             oefeningen=[
                 ("open", "Teken het rooster zelf en vul de volledige tabel in.",
                  r"Rij \(0\): \(0, 1, 2\). Rij \(1\): \(1, 2, 0\). Rij \(2\): \(2, 0, 1\). Elke rij is de vorige één plaats opgeschoven.", 8),
                 ("open", "Is die groep commutatief? Waaraan zie je dat in jouw tabel?",
                  "Ja. De tabel is symmetrisch om de hoofddiagonaal.", 3),
             ]),
        dict(kop="Rekenen met inversen",
             opdracht="Schrijf telkens zo eenvoudig mogelijk.",
             oefeningen=[
                 ("kort", r"\((a^{-1})^{-1}\)", r"\(a\)", W),
                 ("kort", r"\((a \ast b)^{-1}\)", r"\(b^{-1} \ast a^{-1}\)", WW),
                 ("kort", r"\((a \ast b \ast c)^{-1}\)", r"\(c^{-1} \ast b^{-1} \ast a^{-1}\)", WL),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht="Let op de kant waar je bewerkt.",
             oefeningen=[
                 ("open", r"Los \(a \ast x = b\) op. Zeg ook aan welke kant je bewerkt en waarom.",
                  r"Links met \(a^{-1}\), want \(a\) staat links. Je krijgt \(x = a^{-1} \ast b\).", 4),
                 ("open", r"Los \(x \ast a \ast b = c\) op.",
                  r"Rechts met \(b^{-1}\) en daarna rechts met \(a^{-1}\): \(x = c \ast b^{-1} \ast a^{-1}\).", 5),
             ]),
        dict(kop="Waar of niet waar: tabel en inversen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\((a \ast b)^{-1} = a^{-1} \ast b^{-1}\) geldt in elke groep.", False),
                 ("waar", "In elke rij van de Cayley-tabel van een groep komt elk element precies één keer voor.", True),
                 ("waar", "Een groep kan twee verschillende neutrale elementen hebben.", False),
                 ("waar", r"In een commutatieve groep geldt \((a \ast b)^{-1} = a^{-1} \ast b^{-1}\).", True),
             ]),
        dict(kop="Bewijzen",
             opdracht="Schrijf het bewijs volledig uit.",
             oefeningen=[
                 ("open", r"Bewijs dat het neutraal element \(e\) uniek is.",
                  r"Veronderstel twee neutrale elementen \(e\) en \(e'\). Omdat \(e'\) neutraal is, geldt \(e \ast e' = e\). Omdat \(e\) neutraal is, geldt \(e \ast e' = e'\). Dus \(e = e'\).", 7),
                 ("open", r"Bewijs dat \((a \ast b)^{-1} = b^{-1} \ast a^{-1}\).",
                  r"Reken \((a \ast b) \ast (b^{-1} \ast a^{-1})\) uit. Eerst valt \(b \ast b^{-1} = e\) weg, dan \(a \ast a^{-1} = e\). Het resultaat is \(e\), dus is \(b^{-1} \ast a^{-1}\) het invers element van \(a \ast b\).", 7),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom kan je met een Cayley-tabel niet aantonen dat \((\mathbb{Z}, +)\) een groep is?",
                  "Omdat die groep oneindig is: de tabel zou oneindig veel rijen en kolommen hebben.", 3),
                 ("open", "Waarom is de kant waar je bewerkt belangrijk in een groep die niet commutatief is?",
                  r"Omdat \(a^{-1} \ast b\) en \(b \ast a^{-1}\) dan verschillende elementen zijn.", 3),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je besluit op.",
             oefeningen=[
                 ("open", r"In een groep staat op de hele hoofddiagonaal van de tabel \(e\). Wat weet je dan over die groep?",
                  r"Elk element is zijn eigen invers, dus \(a \ast a = e\). De groep is dan ook commutatief: uit \(a \ast b = (a \ast b)^{-1} = b^{-1} \ast a^{-1} = b \ast a\) volgt dat.", 6),
                 ("open", r"In een groep geldt \(a \ast b = a \ast c\). Mag je besluiten dat \(b = c\)? En geldt hetzelfde in \((\mathbb{Z}, \cdot)\)?",
                  r"In een groep wel: bewerk links met \(a^{-1}\). In \((\mathbb{Z}, \cdot)\) niet, want \(0 \cdot 2 = 0 \cdot 3\) terwijl \(2 \neq 3\); \(0\) heeft daar geen invers element.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-punten-vectoren-en-afstanden-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Punten, vectoren en afstanden in de ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van A naar B",
             opdracht=r"Vul aan. Denk eraan: \(\overrightarrow{AB}\) is eindpunt min beginpunt.",
             oefeningen=[
                 ("tabel", [r"\(A\)", r"\(B\)", r"\(\overrightarrow{AB}\)", r"\(\|\overrightarrow{AB}\|\)"],
                  [[r"\((1, 2, 2)\)", r"\((4, 6, 14)\)", None, None],
                   [r"\((0, 0, 0)\)", r"\((6, 8, 0)\)", None, None],
                   [r"\((2, 1, 3)\)", r"\((2, 1, 8)\)", None, None],
                   [r"\((1, -1, 2)\)", r"\((3, 1, 1)\)", None, None]],
                  "(3, 4, 12) en 13; (6, 8, 0) en 10; (0, 0, 5) en 5; (2, 2, −1) en 3", "130px"),
             ]),
        dict(kop="Optellen en aftrekken",
             opdracht="Reken coördinaat per coördinaat.",
             oefeningen=[
                 ("rij", [(r"\((1, 2, 3) + (4, 0, -1)\)", r"\((5, 2, 2)\)"),
                          (r"\((2, -1, 0) - (1, 1, 1)\)", r"\((1, -2, -1)\)"),
                          (r"\((3, 3, 3) - (3, 3, 3)\)", r"\(\vec{0}\)"),
                          (r"\((1, 0, 2) + (0, 5, -2)\)", r"\((1, 5, 0)\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="Met een getal vermenigvuldigen",
             opdracht="Elke coördinaat afzonderlijk.",
             oefeningen=[
                 ("rij", [(r"\(3 \cdot (2, -1, 0)\)", r"\((6, -3, 0)\)"),
                          (r"\(-1 \cdot (1, -2, 5)\)", r"\((-1, 2, -5)\)"),
                          (r"\(\tfrac{1}{2} \cdot (4, 6, -8)\)", r"\((2, 3, -4)\)"),
                          (r"\(-2 \cdot (0, 1, 3)\)", r"\((0, -2, -6)\)")],
                  "Reken uit.", WW),
             ]),
        dict(kop="De norm berekenen",
             opdracht=r"Gebruik \(\|\vec{v}\| = \sqrt{v_{1}^{2} + v_{2}^{2} + v_{3}^{2}}\).",
             oefeningen=[
                 ("rij", [(r"\(\vec{v}(3, 0, 4)\)", r"\(5\)"),
                          (r"\(\vec{v}(1, 2, 2)\)", r"\(3\)"),
                          (r"\(\vec{v}(0, 0, -7)\)", r"\(7\)"),
                          (r"\(\vec{v}(6, 6, 7)\)", r"\(11\)")],
                  r"\(\|\vec{v}\|\)", W),
             ]),
        dict(kop="Waar of niet waar: vectoren",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(\|\vec{v}\|\) kan negatief zijn.", False),
                 ("waar", r"Er geldt \(\overrightarrow{BA} = -\overrightarrow{AB}\).", True),
                 ("waar", "Twee pijlen met dezelfde coördinaten maar een ander beginpunt zijn verschillende vrije vectoren.", False),
                 ("waar", "Elke rechte heeft oneindig veel richtingsvectoren.", True),
             ]),
        dict(kop="Een vector ontbinden",
             opdracht=r"Werk met de eenheidsvectoren \(\vec{e_{x}}\), \(\vec{e_{y}}\) en \(\vec{e_{z}}\).",
             oefeningen=[
                 ("kort", r"Schrijf \(\vec{v}(3, -2, 5)\) als som van vectoren langs de assen.",
                  r"\(3\vec{e_{x}} - 2\vec{e_{y}} + 5\vec{e_{z}}\)", WL),
                 ("kort", r"Welke vector hoort bij \(4\vec{e_{x}} - \vec{e_{z}}\)?", r"\((4, 0, -1)\)", WW),
             ]),
        dict(kop="Het scalair product",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\((1, 2, 2) \cdot (2, 1, 0)\)", r"\(4\)"),
                          (r"\((1, 0, 0) \cdot (0, 1, 0)\)", r"\(0\)"),
                          (r"\((1, 1, 0) \cdot (-2, 0, 0)\)", r"\(-2\)"),
                          (r"\((2, -1, 3) \cdot (1, 4, 1)\)", r"\(1\)")],
                  "Reken uit.", W),
             ]),
        dict(kop="Scherp, recht of stomp",
             opdracht="Reken het scalair product uit en zeg wat je eruit besluit.",
             oefeningen=[
                 ("tabel", ["Twee vectoren", r"\(\vec{u} \cdot \vec{v}\)", "Scherp, recht of stomp"],
                  [[r"\((2, 1, 1)\) en \((1, 1, 1)\)", None, None],
                   [r"\((1, -1, 0)\) en \((1, 1, 0)\)", None, None],
                   [r"\((2, 0, 0)\) en \((-3, 1, 1)\)", None, None],
                   [r"\((0, 4, 0)\) en \((1, 0, 5)\)", None, None]],
                  "4 en scherp; 0 en recht; −6 en stomp; 0 en recht", "150px"),
             ]),
        dict(kop="Loodrecht, evenwijdig of geen van beide",
             opdracht="Kijk eerst of de ene een veelvoud van de andere is, reken dan het scalair product uit.",
             oefeningen=[
                 ("tabel", ["Twee vectoren", "Loodrecht, evenwijdig of geen van beide"],
                  [[r"\((1, 2, 3)\) en \((2, 4, 6)\)", None],
                   [r"\((1, 0, 0)\) en \((0, 0, 5)\)", None],
                   [r"\((1, 1, 1)\) en \((1, 2, 3)\)", None],
                   [r"\((2, -1, 0)\) en \((-4, 2, 0)\)", None]],
                  "evenwijdig; loodrecht; geen van beide; evenwijdig", "200px"),
             ]),
        dict(kop="Een onbekende coördinaat zoeken",
             opdracht="Stel een vergelijking op en los ze op.",
             oefeningen=[
                 ("open", r"Voor welke \(a\) staat \(\vec{u}(a, 2, -1)\) loodrecht op \(\vec{v}(3, 1, 4)\)?",
                  r"\(3a + 2 - 4 = 0\), dus \(3a = 2\) en \(a = \tfrac{2}{3}\).", 5),
                 ("open", r"Voor welke \(b\) is \(\vec{u}(2, b, 6)\) evenwijdig met \(\vec{v}(1, 3, 3)\)?",
                  r"Uit \(2 = k \cdot 1\) volgt \(k = 2\). Dan klopt \(6 = 2 \cdot 3\), en \(b = 2 \cdot 3 = 6\).", 5),
             ]),
        dict(kop="De hoek berekenen",
             opdracht=r"Gebruik \(\cos \theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \cdot \|\vec{v}\|}\).",
             oefeningen=[
                 ("open", r"Bereken de hoek tussen \(\vec{u}(1, 0, 0)\) en \(\vec{v}(1, 1, 0)\).",
                  r"\(\vec{u} \cdot \vec{v} = 1\), \(\|\vec{u}\| = 1\) en \(\|\vec{v}\| = \sqrt{2}\). Dus \(\cos \theta = \tfrac{1}{\sqrt{2}}\) en \(\theta = 45^{\circ}\).", 6),
                 ("open", r"Bereken de hoek tussen \(\vec{u}(1, 1, 0)\) en \(\vec{v}(-1, 0, 0)\).",
                  r"\(\vec{u} \cdot \vec{v} = -1\), \(\|\vec{u}\| = \sqrt{2}\) en \(\|\vec{v}\| = 1\). Dus \(\cos \theta = -\tfrac{1}{\sqrt{2}}\) en \(\theta = 135^{\circ}\).", 6),
             ]),
        dict(kop="Afstanden",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", r"\(|AB|\) met \(A(1, 2, 3)\) en \(B(1, 2, 8)\)", r"\(5\)", W),
                 ("kort", r"de afstand van \(P(2, 3, 6)\) tot de oorsprong", r"\(7\)", W),
                 ("kort", r"\(|AB|\) met \(A(0, 1, 2)\) en \(B(1, 5, 10)\)", r"\(9\)", W),
             ]),
        dict(kop="Middens en zwaartepunten",
             opdracht="Neem telkens het gemiddelde van de coördinaten.",
             oefeningen=[
                 ("rij", [(r"het midden van \((2, 4, 6)\) en \((6, 8, 10)\)", r"\((4, 6, 8)\)"),
                          (r"het zwaartepunt van \((0, 0, 0)\), \((3, 0, 0)\) en \((0, 3, 0)\)", r"\((1, 1, 0)\)"),
                          (r"het midden van \((0, 0, 0)\) en \((4, 4, 4)\)", r"\((2, 2, 2)\)"),
                          (r"het zwaartepunt van het viervlak \((0,0,0)\), \((4,0,0)\), \((0,4,0)\), \((0,0,4)\)", r"\((1, 1, 1)\)")],
                  "Bereken.", WW),
             ]),
        dict(kop="Waar of niet waar: scalair product",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Er geldt \(\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}\).", True),
                 ("waar", r"Er geldt \(\vec{v} \cdot \vec{v} = \|\vec{v}\|\).", False),
                 ("waar", r"Is \(\vec{u} \cdot \vec{v} > 0\), dan is de hoek tussen de twee vectoren scherp.", True),
                 ("waar", "Het scalair product van twee vectoren is zelf een vector.", False),
             ]),
        dict(kop="Uit een context",
             opdracht="Teken er gerust een schets bij.",
             oefeningen=[
                 ("open", "Een voorwerp wordt met twee krachten getrokken: vier newton naar het oosten en drie newton naar het noorden. Hoe groot is de resulterende kracht, en waarom tel je de getallen niet gewoon op?",
                  r"Vijf newton, want \(\sqrt{16 + 9} = 5\). Je telt de vectoren op, niet de getallen; zeven zou alleen kloppen als de krachten dezelfde kant op wezen.", 5),
                 ("open", r"Een drone vertrekt in de oorsprong, vliegt naar \(A(30, 40, 0)\) en daarna naar \(B(30, 40, 120)\). Hoe lang is zijn weg, en hoe ver ligt \(B\) van de oorsprong?",
                  r"De weg is \(50 + 120 = 170\) meter. De afstand is \(\sqrt{900 + 1600 + 14400} = \sqrt{16900} = 130\) meter.", 6),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom moet het assenstelsel orthonormaal zijn voor \(\|\vec{v}\| = \sqrt{v_{1}^{2} + v_{2}^{2} + v_{3}^{2}}\)?",
                  "Die formule is de stelling van Pythagoras, en die geldt alleen als de assen loodrecht op elkaar staan en de eenheden even lang zijn.", 4),
                 ("open", "Waarom is het scalair product een goed criterium voor loodrechte stand?",
                  r"Omdat \(\vec{u} \cdot \vec{v} = \|\vec{u}\| \cdot \|\vec{v}\| \cdot \cos \theta\) en \(\cos 90^{\circ} = 0\). Zijn de twee vectoren niet nul, dan kan het product alleen nul worden door die cosinus.", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je redenering op.",
             oefeningen=[
                 ("open", r"Toon met de coördinaten aan dat \(\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}\).",
                  r"De eerste coördinaat geeft \((x_{B} - x_{A}) + (x_{C} - x_{B}) = x_{C} - x_{A}\), en net zo voor de twee andere. De tussenstop valt weg.", 6),
                 ("open", r"Voor welke \(t\) geldt \(\|(t, t, t)\| = 3\)?",
                  r"\(\sqrt{3t^{2}} = |t|\sqrt{3} = 3\), dus \(|t| = \sqrt{3}\). Er zijn twee oplossingen: \(t = \sqrt{3}\) en \(t = -\sqrt{3}\).", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-rechten-en-vlakken-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rechten en vlakken in de ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat heb je nodig",
             opdracht="Vul in wat je minstens moet kennen om de vergelijking op te stellen.",
             oefeningen=[
                 ("tabel", ["Wat je wil opstellen", "Wat je nodig hebt"],
                  [["de vergelijking van een rechte", None],
                   ["de parametrische vergelijkingen van een vlak", None],
                   ["de cartesische vergelijking van een vlak", None]],
                  "een punt en een richtingsvector; een punt en twee niet-evenwijdige richtingsvectoren; een punt en een normaalvector",
                  "320px"),
             ]),
        dict(kop="Hoeveel van elk",
             opdracht="Schrijf telkens het cijfer op.",
             oefeningen=[
                 ("rij", [("cartesische vergelijkingen van een rechte in de ruimte", r"\(2\)"),
                          ("cartesische vergelijkingen van een rechte in het vlak", r"\(1\)"),
                          ("parameters in de vergelijkingen van een vlak", r"\(2\)"),
                          ("punten die niet op één rechte liggen om een vlak vast te leggen", r"\(3\)")],
                  "Hoeveel?", W),
             ]),
        dict(kop="Een rechte opstellen",
             opdracht="Schrijf de drie parametrische vergelijkingen volledig uit.",
             oefeningen=[
                 ("open", r"De rechte door \(A(1, 2, 3)\) met richtingsvector \(\vec{v}(2, -1, 4)\).",
                  r"\(x = 1 + 2t\), \(y = 2 - t\) en \(z = 3 + 4t\).", 5),
                 ("open", r"De rechte door \(A(0, 1, 2)\) en \(B(3, 1, -2)\).",
                  r"\(\overrightarrow{AB} = (3, 0, -4)\), dus \(x = 3t\), \(y = 1\) en \(z = 2 - 4t\).", 5),
             ]),
        dict(kop="Normaalvectoren aflezen",
             opdracht=r"Lees \(\vec{n}\) af uit de cartesische vergelijking.",
             oefeningen=[
                 ("rij", [(r"\(x + 2y - 3z + 1 = 0\)", r"\((1, 2, -3)\)"),
                          (r"\(z = 0\)", r"\((0, 0, 1)\)"),
                          (r"\(2x - y = 4\)", r"\((2, -1, 0)\)"),
                          (r"\(x + y + z = 0\)", r"\((1, 1, 1)\)")],
                  r"\(\vec{n}\)", WW),
             ]),
        dict(kop="Een vlak opstellen",
             opdracht=r"Werk met \(ax + by + cz + d = 0\): \(\vec{n}\) geeft \(a\), \(b\) en \(c\), het punt bepaalt \(d\).",
             oefeningen=[
                 ("open", r"Het vlak door \(P(1, 2, -1)\) met \(\vec{n}(3, 0, 2)\).",
                  r"\(3x + 2z + d = 0\) met \(3 \cdot 1 + 2 \cdot (-1) + d = 0\), dus \(d = -1\) en \(3x + 2z - 1 = 0\).", 5),
                 ("open", r"Het vlak door de oorsprong met \(\vec{n}(1, -2, 2)\).",
                  r"\(x - 2y + 2z = 0\). Omdat het vlak door de oorsprong gaat, is \(d = 0\).", 4),
             ]),
        dict(kop="Ligt het punt in het vlak?",
             opdracht=r"Vul de coördinaten in \(\alpha: 2x - y + z - 3 = 0\) in. Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [(r"\(A(1, 1, 2)\)", "ja"),
                          (r"\(B(0, 1, 0)\)", "nee"),
                          (r"\(C(1, 0, 0)\)", "nee"),
                          (r"\(D(2, 2, 1)\)", "ja")],
                  "Ja of nee?", W),
             ]),
        dict(kop="Waar of niet waar: vergelijkingen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een rechte in de ruimte heeft één cartesische vergelijking.", False),
                 ("waar", r"In \(ax + by + cz + d = 0\) is \((a, b, c)\) een normaalvector van het vlak.", True),
                 ("waar", "Drie punten op eenzelfde rechte bepalen één vlak.", False),
                 ("waar", "De parametrische vergelijkingen van een vlak bevatten twee parameters.", True),
             ]),
        dict(kop="Onderlinge ligging",
             opdracht="Vul in welke liggingen mogelijk zijn.",
             oefeningen=[
                 ("tabel", ["Wat je vergelijkt", "Mogelijke liggingen"],
                  [["twee rechten in de ruimte", None], ["een rechte en een vlak", None], ["twee vlakken", None]],
                  "samenvallend, evenwijdig, snijdend of kruisend; in het vlak, evenwijdig ernaast, of snijdend; samenvallend, evenwijdig, of snijdend volgens een rechte",
                  "330px"),
             ]),
        dict(kop="Twee vlakken vergelijken",
             opdracht=r"Vergelijk eerst \(\vec{n_{1}}\) en \(\vec{n_{2}}\), kijk daarna naar \(d\).",
             oefeningen=[
                 ("tabel", ["De twee vlakken", "Samenvallend, evenwijdig of snijdend"],
                  [[r"\(x + y + z = 1\) en \(2x + 2y + 2z = 2\)", None],
                   [r"\(x + y + z = 1\) en \(2x + 2y + 2z = 5\)", None],
                   [r"\(x + y + z = 1\) en \(x - y = 0\)", None],
                   [r"\(z = 0\) en \(z = 4\)", None]],
                  "samenvallend; evenwijdig; snijdend volgens een rechte; evenwijdig", "220px"),
             ]),
        dict(kop="Een rechte bij een vlak",
             opdracht=r"Het vlak heeft \(\vec{n}(1, 2, 2)\). Wat doet de rechte met richtingsvector \(\vec{v}\)?",
             oefeningen=[
                 ("rij", [(r"\(\vec{v}(2, -2, 1)\)", "evenwijdig met het vlak"),
                          (r"\(\vec{v}(2, 4, 4)\)", "loodrecht op het vlak"),
                          (r"\(\vec{v}(1, 0, 0)\)", "ze snijdt het vlak schuin")],
                  "Wat doet ze?", WL),
             ]),
        dict(kop="Afstand van een punt tot een vlak",
             opdracht=r"Werk met \(\alpha: 2x - y + 2z - 3 = 0\) en \(d(P, \alpha) = \dfrac{|a x_{P} + b y_{P} + c z_{P} + d|}{\sqrt{a^{2} + b^{2} + c^{2}}}\).",
             oefeningen=[
                 ("kort", r"\(P(2, 0, 0)\)", r"\(\tfrac{1}{3}\)", W),
                 ("kort", r"de oorsprong", r"\(1\)", W),
                 ("kort", r"\(P(3, 0, 3)\)", r"\(3\)", W),
             ]),
        dict(kop="De hoek tussen twee vlakken",
             opdracht=r"Reken met de normaalvectoren en neem de scherpe hoek.",
             oefeningen=[
                 ("open", r"De hoek tussen \(\alpha: x = 0\) en \(\beta: x + y = 0\).",
                  r"\(\vec{n_{1}}(1, 0, 0)\) en \(\vec{n_{2}}(1, 1, 0)\) geven \(\cos \theta = \tfrac{1}{\sqrt{2}}\), dus \(\theta = 45^{\circ}\).", 6),
                 ("open", r"De hoek tussen \(\alpha: z = 0\) en \(\beta: z = 5\).",
                  r"Allebei \(\vec{n}(0, 0, 1)\), dus \(\cos \theta = 1\) en \(\theta = 0^{\circ}\). De vlakken zijn evenwijdig.", 5),
             ]),
        dict(kop="Waar of niet waar: ligging",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Twee evenwijdige rechten liggen altijd in eenzelfde vlak.", True),
                 ("waar", "Twee vlakken die niet evenwijdig zijn, kunnen elkaar in één punt snijden.", False),
                 ("waar", r"Een rechte met \(\vec{v} \perp \vec{n}\) staat loodrecht op het vlak.", False),
                 ("waar", "Twee rechten die elkaar niet snijden, kunnen kruisend zijn.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom stel je de determinant van orde \(3\) gelijk aan \(0\) als je de cartesische vergelijking van een vlak opstelt?",
                  "Een determinant die niet nul is, betekent dat de drie vectoren de hele ruimte opspannen. Nul betekent net dat ze in eenzelfde vlak liggen, en dat is wat je wil.", 4),
                 ("open", "Leg uit wat kruisende rechten zijn en waarom dat alleen in de ruimte bestaat.",
                  "Ze zijn niet evenwijdig en hebben toch geen snijpunt, want ze liggen niet in eenzelfde vlak. In het vlak snijden twee niet-evenwijdige rechten elkaar altijd.", 4),
                 ("open", "Waarom heeft een rechte in de ruimte twee cartesische vergelijkingen en in het vlak maar één?",
                  "In de ruimte is een rechte de doorsnede van twee vlakken, en elk vlak levert één vergelijking. In het vlak legt één vergelijking de rechte al volledig vast.", 4),
             ]),
        dict(kop="Uit een context",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een hellend dakvlak en de verticale gevel eronder. Hoe bereken je de hoek tussen die twee vlakken, en welke hoek is dat net niet?",
                  "Als de scherpe hoek tussen hun normaalvectoren. Dat is niet de hellingshoek van het dak met de horizontale grond: dat is een andere hoek.", 4),
                 ("open", "Twee luchtwegen lopen op verschillende hoogte boven elkaar en zijn niet evenwijdig. Hoe heet die ligging, en is de afstand tussen de twee rechten nul?",
                  "Ze kruisen. De afstand is niet nul, want ze hebben geen punt gemeen; het is de kortste loodrechte afstand tussen de twee rechten.", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je redenering op.",
             oefeningen=[
                 ("open", r"Van een rechte geldt \(\vec{v} \perp \vec{n}\) van een vlak. Ligt ze dan in dat vlak?",
                  "Niet noodzakelijk: ze is evenwijdig met het vlak. Pas als ook één punt van de rechte in het vlak ligt, ligt ze er helemaal in.", 5),
                 ("open", r"Toon aan dat \(\alpha: x + y + z = 1\) en \(\beta: 2x + 2y + 2z = 8\) evenwijdig zijn, en bereken hun afstand.",
                  r"\(\vec{n_{2}} = 2 \cdot \vec{n_{1}}\), dus ze zijn evenwijdig. Neem \(P(1, 0, 0)\) op \(\alpha\): \(d = \dfrac{|2 - 8|}{\sqrt{12}} = \dfrac{6}{2\sqrt{3}} = \sqrt{3} \approx 1{,}73\).", 7),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-programmeren-algoritmen-en-structuren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Programmeren: algoritmen en structuren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De bouwstenen",
             opdracht="Schrijf bij elke omschrijving de naam van de bouwsteen.",
             oefeningen=[
                 ("rij", [("een naam waarachter een waarde zit die kan veranderen", "een variabele"),
                          ("een waarde die tijdens het programma niet verandert", "een constante"),
                          ("code die alleen loopt als iets waar is", "een conditie"),
                          ("hetzelfde stuk code herhalen", "een iteratie")],
                  "Welke bouwsteen?", WL),
                 ("kort", "Hoe heet een stuk code dat je een naam geeft en hergebruikt?", "een functie", WW),
             ]),
        dict(kop="Het juiste sleutelwoord",
             opdracht="Schrijf het sleutelwoord op dat je in Python gebruikt.",
             oefeningen=[
                 ("rij", [("een stuk code alleen laten lopen als iets waar is", r"\(\texttt{if}\)"),
                          ("over alle elementen van een rij lopen", r"\(\texttt{for}\)"),
                          ("een functie schrijven", r"\(\texttt{def}\)"),
                          ("teruggeven wat een functie uitrekent", r"\(\texttt{return}\)")],
                  "Welk sleutelwoord?", W),
             ]),
        dict(kop="De juiste datastructuur",
             opdracht="Kies de datastructuur die het best past.",
             oefeningen=[
                 ("tabel", ["Wat je wil bewaren", "Datastructuur"],
                  [["de namen van de leerlingen, op volgorde, nog aan te passen", None],
                   ["bij elke leerling zijn punt", None],
                   ["alle verschillende voornamen, zonder dubbels", None],
                   ["de coördinaten van een punt, die vastliggen", None]],
                  "een list; een dictionary; een set; een tuple", "230px"),
             ]),
        dict(kop="Wat blijft er over in een set?",
             opdracht="Je steekt deze lijst in een set. Hoeveel elementen telt die set?",
             oefeningen=[
                 ("rij", [(r"\(\texttt{[2, 5, 5, 7, 7, 7]}\)", r"\(3\)"),
                          (r"\(\texttt{[1, 2, 3, 4]}\)", r"\(4\)"),
                          (r"\(\texttt{[9, 9, 9, 9]}\)", r"\(1\)"),
                          (r"\(\texttt{[0, 1, 0, 1, 2]}\)", r"\(3\)")],
                  "Hoeveel?", W),
             ]),
        dict(kop="Waar of niet waar: datastructuren",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Een \(\texttt{tuple}\) kan je achteraf nog wijzigen.", False),
                 ("waar", r"Een \(\texttt{list}\) bewaart de volgorde van de elementen.", True),
                 ("waar", r"In een \(\texttt{set}\) kan hetzelfde element twee keer staan.", False),
                 ("waar", "Een string is een rij tekens.", True),
             ]),
        dict(kop="Algoritmische technieken",
             opdracht="Schrijf bij elke omschrijving de techniek.",
             oefeningen=[
                 ("rij", [("een functie die zichzelf oproept", "recursie"),
                          ("opsplitsen en de deeloplossingen samenvoegen", "verdeel-en-heers"),
                          ("tussenresultaten bewaren om ze niet twee keer te berekenen", "dynamisch programmeren"),
                          ("in een gesorteerde lijst telkens de helft wegnemen", "verdeel-en-heers")],
                  "Welke techniek?", WL),
             ]),
        dict(kop="Recursie opschrijven",
             opdracht="Schrijf de formule op, met het stopgeval erbij.",
             oefeningen=[
                 ("open", "De faculteit.",
                  r"\(n! = n \cdot (n-1)!\), met \(0! = 1\) als stopgeval.", 4),
                 ("open", "De rij van Fibonacci.",
                  r"\(F(n) = F(n-1) + F(n-2)\), met \(F(0) = 0\) en \(F(1) = 1\).", 4),
             ]),
        dict(kop="Reken de recursie uit",
             opdracht=r"Werk met \(n! = n \cdot (n-1)!\) en \(F(n) = F(n-1) + F(n-2)\).",
             oefeningen=[
                 ("rij", [(r"\(4!\)", r"\(24\)"),
                          (r"\(6!\)", r"\(720\)"),
                          (r"\(F(5)\)", r"\(5\)"),
                          (r"\(F(8)\)", r"\(21\)")],
                  "Hoeveel?", W),
             ]),
        dict(kop="Hoeveel stappen om te zoeken?",
             opdracht="Je zoekt in een gesorteerde rij en gooit elke stap de helft weg. Hoeveel stappen heb je hoogstens nodig?",
             oefeningen=[
                 ("rij", [(r"\(8\) getallen", r"\(3\)"),
                          (r"\(16\) getallen", r"\(4\)"),
                          (r"\(64\) getallen", r"\(6\)"),
                          (r"\(1024\) getallen", r"\(10\)")],
                  "Hoeveel stappen?", W),
             ]),
        dict(kop="Dynamisch programmeren",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Welke oproepen heeft een programma nodig om \(F(4)\) recursief uit te rekenen, en welke waarden berekent het meer dan één keer?",
                  r"\(F(4)\) roept \(F(3)\) en \(F(2)\) op, \(F(3)\) roept \(F(2)\) en \(F(1)\) op, en \(F(2)\) roept telkens \(F(1)\) en \(F(0)\) op. Zo bereken je \(F(2)\) twee keer en \(F(1)\) drie keer.", 5),
                 ("open", "Dynamisch programmeren kost meer geheugen. Wat levert het op, en wanneer is dat de moeite?",
                  "Het wint tijd, want je berekent niets twee keer. Bij een probleem waar dezelfde deelberekening vaak terugkomt, zoals de rij van Fibonacci, scheelt dat enorm.", 4),
             ]),
        dict(kop="Correctheid en eindigheid",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg het verschil uit tussen de correctheid en de eindigheid van een algoritme.",
                  "Correct betekent dat het voor elke toegelaten invoer het juiste antwoord geeft. Eindig betekent dat het na een eindig aantal stappen stopt. Een programma kan correct geredeneerd zijn en toch eeuwig blijven lopen.", 4),
                 ("open", "Hoe beargumenteer je de eindigheid van een lus, en hoe die van een recursieve functie?",
                  "Bij een lus toon je dat de voorwaarde ooit vals wordt. Bij recursie toon je dat je het stopgeval altijd bereikt.", 4),
             ]),
        dict(kop="Waar of niet waar: algoritmen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een algoritme is pas een algoritme als het in Python geschreven staat.", False),
                 ("waar", "Twee algoritmen die hetzelfde antwoord geven, zijn ook even snel.", False),
                 ("waar", "Een algoritme is eindig als het na een eindig aantal stappen stopt.", True),
                 ("waar", "Je test je programma ook met randgevallen, omdat fouten zich daar verstoppen.", True),
             ]),
        dict(kop="Bibliotheken en bestanden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["Bibliotheek", "Waarvoor je ze gebruikt"],
                  [[r"\(\texttt{matplotlib}\)", None], [r"\(\texttt{numpy}\)", None], [r"\(\texttt{random}\)", None]],
                  "grafieken tekenen; vlot met grote rijen getallen rekenen; toevalsgetallen genereren", "280px"),
                 ("kort", "Welk soort bestand lees je naast een gewoon tekstbestand in en schrijf je weg?",
                  "een CSV-bestand", WW),
             ]),
        dict(kop="Groeigedrag",
             opdracht=r"Vul in hoeveel stappen je ongeveer doet bij \(n = 1000\).",
             oefeningen=[
                 ("tabel", ["Groeigedrag", r"Ongeveer hoeveel stappen bij \(n = 1000\)"],
                  [[r"\(O(\log n)\)", None], [r"\(O(n)\)", None], [r"\(O(n^{2})\)", None]],
                  r"ongeveer \(10\); ongeveer \(1000\); ongeveer \(1\,000\,000\)", "230px"),
             ]),
        dict(kop="De Riemannsom",
             opdracht="Schrijf je berekening volledig uit.",
             oefeningen=[
                 ("open", r"Schrijf de benadering van \(\int_{a}^{b} f(x) \, dx\) op als een som, en zeg wat \(\Delta x\) is.",
                  r"\(\int_{a}^{b} f(x) \, dx \approx \sum_{i=1}^{n} f(x_{i}) \cdot \Delta x\), met \(\Delta x = \dfrac{b-a}{n}\), de breedte van één strook.", 5),
                 ("open", r"Je verdeelt \([0, 4]\) in \(8\) stroken. Hoe breed is elke strook, en wat gebeurt er met de benadering als je \(n\) verdubbelt?",
                  r"\(\Delta x = \dfrac{4 - 0}{8} = 0{,}5\). Verdubbel je \(n\), dan worden de stroken half zo smal en wordt de benadering beter.", 5),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom geef je variabelen een zinvolle naam, en waarvoor dient commentaar in je code?",
                  "Allebei om je code leesbaar te houden voor jezelf en voor anderen, en dat telt mee in de beoordeling. Commentaar wordt niet mee uitgevoerd; ze staat er alleen voor wie de code leest.", 4),
                 ("open", "Noem de vier stappen waarin je een oplossing uitwerkt, en leg uit waarom je niet meteen begint te typen.",
                  "Analyseren, een algoritme ontwerpen, programmeren, en testen en debuggen. Meteen beginnen typen zonder het probleem te analyseren kost je achteraf meer tijd dan het wint.", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je redenering op.",
             oefeningen=[
                 ("open", "Een lijst van een miljoen namen is niet gesorteerd en je moet er één naam in terugvinden. Mag je hier halveren?",
                  "Nee: halveren werkt alleen op een gesorteerde rij. Je loopt de lijst dan van voor naar achter door, of je sorteert ze eerst als je nog vaak moet zoeken.", 5),
                 ("open", r"Twee programma's geven hetzelfde antwoord. Het ene doet \(O(n)\) stappen, het andere \(O(n^{2})\). Bij \(n = 10\) merk je nauwelijks verschil. Hoe komt dat, en wanneer wel?",
                  r"Bij \(n = 10\) is dat \(10\) tegenover \(100\) stappen, en dat duurt allebei niets. Bij \(n = 1000\) wordt het \(1000\) tegenover \(1\,000\,000\), en dan wordt het tweede onbruikbaar.", 5),
             ]),
    ],
)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-machtswortels-machten-en-logaritmen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet een negatieve exponent eerst om in een breuk, en pas dan de rekenregels toe. "
                   "Bij een breuk met een negatieve exponent keer je de breuk om.",
            waarom=[
                "Let op het laatste: min 2 tot de vierde is positief, want de exponent is even. Had er "
                "min 2 tot de derde gestaan, dan was het antwoord negatief.",
                "Let op de tweede: een negatieve exponent in de noemer wordt positief in de teller. "
                "b tot de min 2 gedeeld door b tot de min 5 geeft b tot de derde.",
                "Let erop dat je de exponenten optelt tot één exponent: x plus 2x min 1 is 3x min 1. "
                "Pas als de grondtallen gelijk zijn, mag je de exponenten gelijkstellen.",
            ],
        ),
        dict(
            aanpak="Lees een rationale exponent als twee bewerkingen: de noemer is de wortelexponent, "
                   "de teller de macht. Neem altijd eerst de wortel, dan blijven de getallen klein.",
            waarom=[
                "Let erop dat je bij 16 tot de drie vierde eerst de vierdemachtswortel neemt, dus 2, en "
                "dan tot de derde verheft. Omgekeerd zou je met 4096 moeten werken.",
                "Let op de laatste: de vijfdemachtswortel van a tot de tiende maal b tot de vijfde geeft "
                "a kwadraat maal b. Elke exponent wordt door 5 gedeeld.",
                "Let erop dat je de exponent omkeert: uit x tot de twee vijfde volgt x gelijk aan 4 tot "
                "de vijf halve, en dat is 32.",
                "Noem beide stappen bij naam, zoals de vraag vraagt: eerst de derdemachtswortel, dan "
                "het kwadraat.",
                "Niet waar: een even wortel van een negatief getal bestaat niet in R. Geen enkel reëel "
                "getal tot de vierde geeft min 16.",
                None,
                "Niet waar: de wortel van x kwadraat is de absolute waarde van x. Voor x gelijk aan min "
                "3 geeft het 3 en niet min 3.",
            ],
        ),
        dict(
            aanpak="Zoek in de wortel een volkomen macht en haal die eruit. Bij een noemer met een "
                   "wortel vermenigvuldig je met de toegevoegde vorm.",
            waarom=[
                "Let op het laatste: beide wortels worden eerst vereenvoudigd tot 2 wortel 5 en 3 "
                "wortel 5. Pas dan kan je optellen, want nu zijn het gelijke termen.",
                "Let op de tweede: je vermenigvuldigt teller en noemer met wortel 3 min 1. De noemer "
                "wordt dan 3 min 1, dus 2.",
                "Let erop dat een even wortelexponent eist dat wat eronder staat niet negatief is: 5 "
                "min x groter dan of gelijk aan 0.",
                "Let erop dat één tegenvoorbeeld genoeg is. En noem de regel die wel geldt: een wortel "
                "verdeelt zich over een product en een quotiënt.",
            ],
        ),
        dict(
            aanpak="Lees een logaritme als een vraag: tot welke macht moet ik het grondtal verheffen om "
                   "dit getal te krijgen? Bij log zonder grondtal is het 10, bij ln is het e.",
            waarom=[
                None,
                "Let op het eerste: een grondtal kleiner dan 1 geeft een negatieve uitkomst, want een "
                "derde tot de min 2 is 9. En let op het laatste: de twee logaritmen schakelen aan "
                "elkaar tot log met grondtal 3 van 81.",
                "Let erop dat een som van logaritmen een product wordt en een verschil een quotiënt. "
                "Een factor vooraan wordt een exponent, en een half wordt een wortel.",
                "Let erop dat de noemer met een minteken komt: de drie machten van y geven min 3 en de "
                "wortel van z geeft min een half.",
                "Noem de reden: 1 tot de macht x blijft altijd 1. Daarom levert de vraag geen enkel "
                "antwoord op, behalve voor het getal 1 zelf, en dan oneindig veel.",
            ],
        ),
        dict(
            aanpak="Bij een logaritmische vergelijking schrijf je eerst het domein op, want wat onder de "
                   "logaritme staat moet positief zijn. Bij een exponentiële vergelijking neem je de "
                   "logaritme van beide leden.",
            waarom=[
                None,
                "Let erop dat je een exacte vorm mag laten staan: ln 15 gedeeld door ln 2. Pas daarna "
                "mag je benaderen.",
                "Noem het domein als reden: x moet groter zijn dan 6, dus min 3 valt weg. Daarom is het "
                "domein opschrijven geen formaliteit.",
                "Let erop dat 3 tot de 2x gelijk is aan het kwadraat van 3 tot de x. Daarom werkt de "
                "hulponbekende t, en vergeet niet terug te keren naar x.",
                "Let erop dat enkel bij een onbekende in de exponent een logaritme nodig is. De drie "
                "andere los je op met een wortel of met gewone bewerkingen.",
            ],
        ),
        dict(
            aanpak="Schrijf bij een toepassing eerst de vergelijking op met de groeifactor erin, en "
                   "reken dan pas. Bij volle jaren rond je naar boven af.",
            waarom=[
                "Let erop dat je naar boven afrondt: na 13 jaar is het nog geen anderhalve keer zoveel. "
                "De groeifactor is 1,03 en niet 0,03.",
                "Let erop dat de exponent het aantal halveringstijden is: 30 gedeeld door 8, dus 3,75. "
                "Een halve halveringstijd bestaat in deze formule gewoon.",
                "Let erop dat het antwoord niet van de beginwaarde afhangt: verdubbelen geeft altijd 10 "
                "log 2, ongeveer 3 decibel. Dat is wat een logaritmische schaal doet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veeltermen-deelbaarheid-en-horner-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De reststelling zegt: de rest van een deling door x min a is P(a). Vul dus het "
                   "getal in waarvoor de deler nul wordt, en je hoeft niet te delen.",
            waarom=[
                "Let op het teken: bij x plus 1 vul je min 1 in. Daar gaat het het vaakst mis.",
                "Let erop dat deelbaar betekent dat de rest nul is. Je stelt dus P(3) gelijk aan nul en "
                "lost naar k op.",
                "Let erop dat je P van min 2 moet berekenen en niet P van 2. De deler x plus 2 wordt nul "
                "bij min 2.",
            ],
        ),
        dict(
            aanpak="Zet links in het schema het getal waarvoor de deler nul wordt, en bovenaan alle "
                   "coëfficiënten, ook de nullen. Het laatste getal onderaan is de rest.",
            waarom=[
                "Let op de laatste rij: bij 2x min 1 wordt de deler nul bij een half. Het teken keert "
                "dus om en de coëfficiënt vooraan telt mee.",
                "Let erop dat een vierdegraadsveelterm vijf coëfficiënten heeft, van graad 4 tot graad "
                "0. Hier moeten er dus twee nullen tussen.",
                "Noem de reden: elke graad krijgt een plaats. Zonder die nul schuiven de coëfficiënten "
                "op en klopt het hele schema niet meer.",
                "Let erop dat de rest nul is, dus x min 3 is een deler. Daarna ontbind je het quotiënt "
                "verder, en zo krijg je de volledige ontbinding.",
                None,
                "Niet waar: Horner werkt enkel bij een deler van de vorm x min a. Voor een deler van de "
                "tweede graad doe je de staartdeling.",
            ],
        ),
        dict(
            aanpak="Twee regels volstaan: de graad van het quotiënt is de graad van het deeltal min die "
                   "van de deler, en de rest heeft een graad die strikt lager is dan de deler.",
            waarom=[
                "Let op de laatste rij: de rest mag hier tot graad 2 gaan, want de deler is van graad "
                "3. Hoogstens betekent dat ze ook lager kan zijn.",
                "Let erop dat je ook de voorwaarde op de graad van de rest vermeldt. Zonder die "
                "voorwaarde zou de deling niet uniek zijn.",
            ],
        ),
        dict(
            aanpak="Zoek altijd eerst een gemeenschappelijke factor, dan een merkwaardig product, en pas "
                   "als dat niet lukt een nulwaarde onder de delers van de constante term.",
            waarom=[
                "Let op het verschil tussen de eerste twee: een verschil van kwadraten geeft twee "
                "factoren, een volkomen kwadraat geeft er één die je kwadrateert.",
                "Let op de som van derde machten bij x derde plus 27, en op x vierde min 81: daar blijft "
                "x kwadraat plus 9 staan, want een som van kwadraten ontbindt niet in R.",
                "Let erop dat je bij de tweede factor de discriminant nakijkt: die is min 3, dus "
                "negatief, en daar stopt het ontbinden in R.",
                "Let erop dat je de delers van 6 probeert: 1, 2, 3, 6 en hun tegengestelden. Bij x "
                "gelijk aan 2 is de rest nul, en daarna ontbind je de tweedegraadsfactor.",
                "Let erop dat x vierde plus 4 nooit nul wordt: een vierde macht is nooit negatief, dus "
                "er komt altijd minstens 4 uit.",
                "Let erop dat je de som van de nulwaarden zonder te rekenen vindt: min b gedeeld door a, "
                "dus 10 gedeeld door 2.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vergelijkingen-en-ongelijkheden-oplossen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie dingen kunnen misgaan: een even wortel van een negatief getal, een logaritme "
                   "van nul of minder, en een noemer die nul wordt. Zoek die drie, en anders is er geen "
                   "voorwaarde.",
            waarom=[
                "Let op het verschil tussen de eerste twee: onder een wortel mag 0 staan, onder een "
                "logaritme niet. En een derdemachtswortel heeft geen voorwaarde, want die bestaat ook "
                "voor negatieve getallen.",
            ],
        ),
        dict(
            aanpak="Kijk eerst waar de onbekende staat. Staat ze in de exponent, dan heb je een "
                   "logaritme nodig; staat ze onder een wortel of een logaritme, dan moet je achteraf "
                   "elke oplossing controleren.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: bij x kwadraat gelijk aan 16 zijn er "
                "twee oplossingen, bij 2 tot de x gelijk aan 16 maar één. Een exponentiële functie "
                "neemt elke waarde juist één keer aan.",
                "Let erop dat de absolute waarde twee gevallen geeft, en dat x vierde min 5 x kwadraat "
                "plus 4 een bikwadratische vergelijking is: stel t gelijk aan x kwadraat en vergeet niet "
                "terug te keren.",
                None,
                "Let erop dat je het domein al vóór het rekenen opschrijft: zowel x als x min 4 moet "
                "positief zijn, dus x groter dan 4.",
                None,
                None,
                "Niet waar: wat je wegdeelt, kan nul zijn, en dan verlies je een oplossing. Breng alles "
                "naar één lid en ontbind in factoren.",
            ],
        ),
        dict(
            aanpak="Reken b kwadraat min 4ac uit. Positief geeft twee oplossingen, nul geeft er één, "
                   "negatief geen enkele in R.",
            waarom=[
                "Let op de eerste rij: een discriminant gelijk aan nul betekent niet geen oplossing maar "
                "juist één, want x kwadraat min 4x plus 4 is het kwadraat van x min 2.",
            ],
        ),
        dict(
            aanpak="Bij een ongelijkheid gaat het om tekens, niet om één getal: breng alles naar één "
                   "lid, zoek de nulwaarden en zet ze op een as met het teken van elk stuk ertussen.",
            waarom=[
                "Let op het laatste: de nulwaarden 2 en 4 verdelen de as in drie stukken, en het "
                "middelste valt weg. Het antwoord bestaat dus uit twee stukken.",
                "Let op de derde: bij een breuk hoort de nulwaarde van de noemer er nooit bij, ook niet "
                "bij groter dan of gelijk aan.",
                None,
                None,
                "Let erop dat x kwadraat plus 4 altijd minstens 4 is, dus de ongelijkheid geldt overal. "
                "Zoeken naar nulwaarden levert hier niets op, want er zijn er geen.",
                "Niet waar: de oplossing van een ongelijkheid is bijna altijd een interval, dus "
                "oneindig veel getallen. Hoogstens twee is de regel voor een vierkantsvergelijking.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-een-functie-aflezen-van-haar-grafiek-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het domein zijn alle x-waarden die je mag invullen. Zoek dus de noemers die nul "
                   "worden en wat onder een even wortel of in een logaritme staat.",
            waarom=[
                "Let op de laatste rij: daar gelden twee voorwaarden samen, en bij de logaritme is 0 zelf "
                "uitgesloten, vandaar het open interval.",
                "Let erop dat het bereik over de y-waarden gaat: een kwadraat is nooit negatief, dus de "
                "kleinste waarde is 1.",
                None,
            ],
        ),
        dict(
            aanpak="Vul min x in. Komt dezelfde functie eruit, dan is ze even; komt min f(x) eruit, dan "
                   "is ze oneven; komt er iets anders uit, dan is ze geen van beide.",
            waarom=[
                "Let op de derde rij: x kwadraat plus x is geen van beide, want het kwadraat blijft "
                "gelijk en de x keert van teken. Eén term die niet meewerkt, is al genoeg.",
                "Niet waar: symmetrie om de oorsprong hoort bij een oneven functie. Een even functie is "
                "symmetrisch om de y-as.",
            ],
        ),
        dict(
            aanpak="Stijgen of dalen zegt welke richting de grafiek uitgaat, hol of bol zegt hoe ze "
                   "buigt. Pas de twee samen geven het verloop.",
            waarom=[
                "Let erop dat de eerste twee allebei stijgen: het verschil zit enkel in hol of bol, dus "
                "in hoe snel de stijging verandert.",
                None,
            ],
        ),
        dict(
            aanpak="Een verticale asymptoot zoek je waar de noemer nul wordt. Voor de horizontale "
                   "vergelijk je de graad van teller en noemer.",
            waarom=[
                "Let op de drie gevallen: gelijke graden geven de verhouding van de coëfficiënten, een "
                "kleinere teller geeft y gelijk aan 0, en een grotere teller geeft geen horizontale "
                "asymptoot.",
                "Niet waar: een veelterm zoals x kwadraat heeft er geen enkele. Asymptoten hoor je bij "
                "breuken, wortels, exponentiële en logaritmische functies te verwachten.",
            ],
        ),
        dict(
            aanpak="De inverse draait de bewerking om. Schrijf y gelijk aan het voorschrift, verwissel x "
                   "en y, en los op naar y.",
            waarom=[
                "Let op de laatste: 1 gedeeld door x is haar eigen inverse. Dat komt doordat haar "
                "grafiek al symmetrisch ligt om de rechte y gelijk aan x.",
                None,
                None,
                "Let erop dat x kwadraat twee x-waarden op dezelfde y-waarde stuurt, bijvoorbeeld 3 en "
                "min 3 op 9. Enkel op de positieve helft is ze inverteerbaar.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tweedegraadsfuncties-en-transformaties-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De x van de top is min b gedeeld door 2a, en die vul je in om de y te vinden. Het "
                   "teken van a zegt of het een dal of een berg is.",
            waarom=[
                "Let op de derde rij: de discriminant is negatief, dus er zijn geen nulwaarden, maar de "
                "top bestaat wel. Een parabool zonder nulwaarden ligt volledig boven of volledig onder "
                "de as.",
                None,
                "Let erop dat het bereik bij een bergparabool naar beneden open staat: de top is de "
                "hoogste waarde, dus alles tot en met 1.",
            ],
        ),
        dict(
            aanpak="In de topvorm a maal het kwadraat van x min p, plus q, lees je de top meteen af als "
                   "(p, q). Let op het teken: x plus 4 betekent p gelijk aan min 4.",
            waarom=[
                "Let op de derde en de vierde: bij x plus 4 is de x van de top min 4, en een factor "
                "vooraan verandert de top niet.",
                "Let erop dat je de helft van 8 kwadrateert: x kwadraat min 8x wordt het kwadraat van x "
                "min 4, min 16. Samen met de 11 geeft dat min 5.",
                None,
                "Let erop dat raken betekent juist één snijpunt, dus discriminant nul. Twee snijpunten "
                "zou een positieve discriminant geven.",
            ],
        ),
        dict(
            aanpak="Wat binnen de haakjes bij de x staat, werkt horizontaal en omgekeerd aan wat je "
                   "verwacht; wat erbuiten staat, werkt verticaal en gewoon zoals je leest.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: min 7 binnen de haakjes schuift naar "
                "rechts en plus 2 naar links. Horizontaal gaat het dus tegen je gevoel in.",
                "Let erop dat de volgorde telt: eerst wat in de haakjes staat, dan het uitrekken en het "
                "spiegelen, en pas daarna het verschuiven omhoog.",
                "Let erop dat een nulwaarde een plaats op de x-as is: 3 maal nul blijft nul, dus "
                "verticaal uitrekken verandert er niets aan. Verschuiven wel.",
                "Niet waar: een factor groter dan 1 maakt de parabool smaller. Breder wordt ze bij een "
                "factor tussen 0 en 1.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Zet eerst op wat de top en wat de nulwaarden betekenen in de context. Het hoogste "
                   "punt vraagt de top, terug op de grond vraagt de nulwaarden.",
            waarom=[
                None,
                "Let erop dat je ontbindt in plaats van de discriminant te gebruiken: min 5t maal t min "
                "4 geeft de twee tijden meteen. En t gelijk aan 0 is het ogenblik van het opgooien.",
                "Let erop dat er maar drie zijden draad krijgen: de muur vormt de vierde. Daarom staat "
                "er 2x in plaats van 4x, en komt er een vierkant uit.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-exponentiele-en-logaritmische-functies-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een grondtal groter dan 1 geeft een stijgende grafiek, een grondtal tussen 0 en 1 "
                   "een dalende. De asymptoot ligt op y gelijk aan 0, tenzij er een getal buiten de "
                   "macht bij komt.",
            waarom=[
                "Let op de laatste twee rijen: plus 3 schuift de asymptoot mee naar y gelijk aan 3, maar "
                "het minteken vooraan spiegelt enkel en laat de asymptoot op haar plaats.",
                "Let erop dat elk grondtal tot de macht 0 gelijk is aan 1. Daarom gaan al die grafieken "
                "door hetzelfde punt.",
                None,
                "Niet waar: de grafiek komt er altijd dichter bij, maar raakt ze nooit. Een macht van "
                "een positief grondtal wordt nooit nul.",
                "Let erop dat de factor 3 het bereik niet verandert, want 3 maal iets positiefs blijft "
                "positief. Enkel het verschuiven met min 6 verlegt de ondergrens.",
            ],
        ),
        dict(
            aanpak="Lees elke logaritme als een vraag: tot welke macht moet het grondtal om dit getal te "
                   "geven? Zo heb je geen rekentoestel nodig.",
            waarom=[
                "Let op de derde en de zesde: een grondtal kleiner dan 1 geeft een negatieve uitkomst, "
                "en een wortel geeft een halve exponent.",
                "Let erop dat het argument een hele uitdrukking is: je lost dus eerst de ongelijkheid x "
                "kwadraat min 9 groter dan 0 op, en dat geeft twee stukken.",
            ],
        ),
        dict(
            aanpak="Kan je beide leden als een macht van hetzelfde grondtal schrijven, dan stel je de "
                   "exponenten gelijk. Kan dat niet, dan neem je de logaritme.",
            waarom=[
                "Let erop dat je bij 5 tot de 2x gelijk aan 125 de exponenten gelijkstelt: 2x gelijk aan "
                "3, dus anderhalf. Een niet-geheel antwoord is hier gewoon juist.",
                "Let erop dat je de exacte vorm eerst opschrijft en pas daarna benadert. Een afgerond "
                "getal in een verdere berekening sleept zijn fout mee.",
                "Let erop dat je de bestaansvoorwaarden vóór het rekenen opschrijft: zo zie je meteen "
                "dat min 2 geen oplossing kan zijn.",
                "Let erop dat 4 tot de x het kwadraat is van 2 tot de x. Daarom werkt de hulponbekende "
                "t, en vergeet de laatste stap niet: van t terug naar x.",
            ],
        ),
        dict(
            aanpak="Een groeifactor is 1 plus het groeipercentage, of 1 min het dalingspercentage. Bij "
                   "een andere tijdseenheid verhef je de factor tot het aantal perioden.",
            waarom=[
                "Let op de laatste rij: je telt de maandpercentages niet op maar verheft de factor tot "
                "de twaalfde. Daarom komt er ruim 27 procent uit en niet 24.",
                "Let erop dat de factor 1 geen groei betekent: het aantal blijft precies gelijk.",
            ],
        ),
        dict(
            aanpak="Reken twee keer: trek twee opeenvolgende getallen van elkaar af, en deel ze ook door "
                   "elkaar. Een vast verschil is lineair, een vaste factor exponentieel.",
            waarom=[
                "Let op de derde rij: de verschillen zijn 10, 9 en 8,1, maar de factor is telkens 0,9. "
                "Een dalende reeks kan dus even goed exponentieel zijn.",
                None,
            ],
        ),
        dict(
            aanpak="Schrijf eerst het model op in de vorm beginwaarde maal groeifactor tot de macht t, "
                   "en reken dan pas. Vraagt de vraag naar een tijd, dan heb je een logaritme nodig.",
            waarom=[
                None,
                "Let erop dat de verdubbelingstijd niet van het bedrag afhangt: duizend of honderdduizend "
                "euro verdubbelt in dezelfde tijd. En de vuistregel 100 gedeeld door het percentage zit "
                "er hier ver naast.",
                "Let erop dat de exponent niet geheel hoeft te zijn: 2,5 halveringstijden kan je gewoon "
                "invullen, want de formule geldt ook tussen twee halveringen.",
                "Let erop dat je naar boven afrondt: na 22 uur zit je er nog onder, dus het antwoord is "
                "23 volle uren.",
                "Let erop dat de logaritme van 0,82 negatief is, dus het ongelijkheidsteken draait om. "
                "Dat is bij een dalend model de klassieke valkuil.",
                "Let erop dat 10 procent eraf niet hetzelfde is als 10 procent erbij ongedaan maken: het "
                "tweede percentage rekent op een groter getal. Je verliest dus 1 procent.",
                "Let erop dat de onbekende in de exponent staat, en dat vraagt altijd een logaritme. De "
                "andere drie zijn rekenregels die hier niet bestaan.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-goniometrische-functies-en-goniometrie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Van graden naar radialen vermenigvuldig je met pi gedeeld door 180, en omgekeerd met "
                   "180 gedeeld door pi. Laat pi in het antwoord staan en vereenvoudig de breuk.",
            waarom=[
                "Let erop dat je de breuk vereenvoudigt: 120 maal pi gedeeld door 180 wordt 2 pi gedeeld "
                "door 3. Een onvereenvoudigde breuk is hier geen net antwoord.",
                None,
            ],
        ),
        dict(
            aanpak="Kijk eerst wat je kent. Twee zijden met de hoek ertussen, of de drie zijden, vraagt "
                   "de cosinusregel; alle andere gevallen de sinusregel.",
            waarom=[
                "Let op de laatste rij: met enkel twee hoeken ken je de vorm van de driehoek maar niet "
                "haar grootte. Je hebt dus minstens één zijde nodig.",
                "Let erop dat de cosinus van 60 graden gelijk is aan een half, dus de correctieterm is "
                "28 en niet 56. Zonder die term zou je de stelling van Pythagoras gebruiken, en de hoek "
                "is hier niet recht.",
                "Let erop dat de zijde tegenover de gezochte hoek alleen staat in de formule: a kwadraat "
                "wordt afgetrokken, b en c worden opgeteld.",
                None,
            ],
        ),
        dict(
            aanpak="Zet de hoek op de cirkel en lees het punt af. De x-coördinaat is de cosinus, de "
                   "y-coördinaat de sinus.",
            waarom=[
                "Let op de kolomorde: hier wordt eerst de sinus gevraagd. Bij 0 graden is de sinus 0 en "
                "de cosinus 1, en bij 90 graden net omgekeerd.",
                "Let erop dat twee supplementaire hoeken op dezelfde hoogte liggen maar aan weerszijden "
                "van de y-as. Daarom is de sinus gelijk en de cosinus tegengesteld.",
            ],
        ),
        dict(
            aanpak="Uit de grondformule volgt de ene uit de andere, maar het teken komt uit het "
                   "kwadrant. Bepaal dus eerst waar de hoek ligt.",
            waarom=[
                None,
                "Let erop dat de sinus in het tweede kwadrant positief is, ook al is de cosinus er "
                "negatief. Het kwadrant beslist over het teken, de grondformule enkel over het getal.",
                "Let erop dat de tangens de sinus gedeeld door de cosinus is: de vijfden vallen tegen "
                "elkaar weg.",
                "Let erop dat één tegenvoorbeeld al genoeg is om te besluiten. En noem de juiste formule: "
                "sin 2x is 2 sin x cos x.",
            ],
        ),
        dict(
            aanpak="Het getal vóór de sinus is de amplitude, het getal bij de x bepaalt de periode, en "
                   "het losse getal achteraan schuift de evenwichtslijn.",
            waarom=[
                "Let op het verschil tussen de eerste twee rijen: 4 sin x verandert de amplitude, sin 4x "
                "de periode. En een minteken vooraan spiegelt de grafiek maar maakt de amplitude niet "
                "negatief.",
                "Let erop dat je de amplitude uit het halve verschil haalt, 5 min 1 gedeeld door 2, en "
                "de evenwichtslijn uit het gemiddelde.",
                "Let erop dat het bereik rond de evenwichtslijn min 1 ligt, met 3 naar boven en 3 naar "
                "beneden.",
            ],
        ),
        dict(
            aanpak="Deze formules moet je kennen. Leer ze met hun naam erbij: de "
                   "verdubbelingsformules en de tekenregels voor een tegengestelde hoek.",
            waarom=[
                "Let erop dat cos 2x een verschil van kwadraten is, geen product. Die twee verwar je "
                "makkelijk met elkaar.",
                None,
            ],
        ),
        dict(
            aanpak="Kijk telkens naar de cirkel. De sinus en de cosinus zijn coördinaten op een cirkel "
                   "met straal 1, en dus nooit groter dan 1 of kleiner dan min 1.",
            waarom=[
                None,
                None,
                "Niet waar: de amplitude is een afstand, dus altijd positief. Bij min 3 sin x is ze 3; "
                "het minteken spiegelt alleen.",
                "Niet waar: de tangens kan elke waarde aannemen en loopt naar oneindig bij 90 graden. "
                "Enkel de sinus en de cosinus blijven tussen min 1 en 1.",
                None,
                "Niet waar: een identiteit moet voor élke hoek gelden, dus je moet ze uitwerken. Een "
                "paar hoeken invullen kan ze enkel ontkrachten, niet bewijzen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-limieten-continuiteit-en-asymptoten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vul eerst gewoon in. Komt er een getal uit, dan ben je klaar; komt er nul gedeeld "
                   "door nul uit, dan ontbind je eerst; gaat x naar oneindig, dan vergelijk je de "
                   "hoogste graden.",
            waarom=[
                "Let op de tweede: ontbinden geeft x plus 3, en dan vul je 3 in. Zonder ontbinden lijkt "
                "de limiet niet te bestaan, terwijl ze gewoon 6 is.",
                "Let erop dat je bij de tweede op het teken let: een derde graad gedeeld door een tweede "
                "graad gedraagt zich als x, en x gaat hier naar min oneindig.",
                "Let erop dat het verschil in het teken van de noemer zit. Dat is precies waarom je bij "
                "een pool de linker- en de rechterlimiet apart bekijkt.",
            ],
        ),
        dict(
            aanpak="Een onbepaaldheid is een vorm waar je niets uit kan afleiden. Nul gedeeld door nul "
                   "en oneindig gedeeld door oneindig zijn er twee; een getal gedeeld door nul is er "
                   "geen.",
            waarom=[
                "Let op de tweede rij: 2 gedeeld door 0 is geen onbepaaldheid maar een pool, en de "
                "limiet is daar plus of min oneindig. Enkel het teken moet je nog bekijken.",
            ],
        ),
        dict(
            aanpak="Leid teller en noemer apart af, niet als een quotiënt. Vul daarna opnieuw in, en "
                   "herhaal als er weer een onbepaaldheid staat.",
            waarom=[
                "Let erop dat dit het klassieke voorbeeld is: de limiet is 1, dus dicht bij nul is de "
                "sinus van x bijna gelijk aan x zelf.",
                "Let erop dat je na het afleiden mag invullen zonder nog te ontbinden. Je mag hier ook "
                "ontbinden: dan staat er x plus 2 gedeeld door x min 1, ook 4.",
                "Let erop wat dit zegt: de logaritme groeit trager dan x. Daarom gaat de breuk naar nul "
                "en niet naar 1.",
            ],
        ),
        dict(
            aanpak="Continu betekent dat je de grafiek daar kan tekenen zonder je pen op te heffen. Een "
                   "knik mag dus, een gat of een sprong niet.",
            waarom=[
                "Let op de derde rij: de absolute waarde heeft een knik in nul maar geen gat, dus ze is "
                "er continu. Niet afleidbaar en niet continu zijn twee verschillende dingen.",
                None,
            ],
        ),
        dict(
            aanpak="Verticaal zoek je waar de noemer nul wordt. Voor de rest vergelijk je de graden: "
                   "gelijk geeft horizontaal, teller één hoger geeft schuin.",
            waarom=[
                "Let op de laatste twee rijen: daar is de teller één graad hoger, dus de asymptoot is "
                "schuin. Je vindt haar door uit te delen, en bij de laatste is dat x min 2, niet x.",
                None,
            ],
        ),
        dict(
            aanpak="Hou twee dingen apart: wat de functie doet in een punt, en wat ze doet in de buurt "
                   "van dat punt. Een limiet gaat altijd over de buurt.",
            waarom=[
                "Niet waar: 2 gedeeld door 0 is geen onbepaaldheid. De regel geldt enkel bij nul "
                "gedeeld door nul of oneindig gedeeld door oneindig.",
                "Let erop dat een asymptoot geen verbod is maar een richting op lange termijn. Ze mag "
                "dus best gesneden worden.",
                "Niet waar: een parabool blijft stijgen, dus haar limiet is oneindig en geen getal.",
                "Niet waar: de limiet gaat over de buurt van a, niet over a zelf. Daarom bestaat de "
                "limiet van de sinus van x gedeeld door x in nul, al bestaat de functie er niet.",
                "Let erop dat het omgekeerde niet geldt: de absolute waarde is continu in nul maar daar "
                "niet afleidbaar.",
                "Niet waar: bij een verticale asymptoot bestaat de functie daar niet, dus er valt niets "
                "te snijden. Dat is het verschil met een horizontale.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-afgeleiden-en-het-verloop-van-een-functie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk eerst naar de bouw van het voorschrift. Een som leid je term per term af, een "
                   "product en een quotiënt hebben hun eigen regel, en iets binnen iets anders vraagt de "
                   "kettingregel.",
            waarom=[
                "Let erop dat de afgeleide van een rechte het getal vóór de x is: de min 3 verdwijnt, "
                "want een constante verandert niet.",
                "Let op de derde: de productregel geeft twee termen. En bij de vierde haal je met de "
                "kettingregel de factor 2 naar buiten: 3 maal het kwadraat maal 2 geeft 6.",
            ],
        ),
        dict(
            aanpak="Schrijf de regel die je gebruikt er telkens bij. Zo zie je zelf waar een "
                   "rekenfout zit, en kan je ze gericht verbeteren.",
            waarom=[
                "Let erop dat bij de eerste de teller van de quotiëntregel netjes vereenvoudigt: x plus "
                "1 min x geeft 1. De noemer blijft gekwadrateerd staan.",
                "Let erop dat één tegenvoorbeeld de regel onderuit haalt. Daarom bestaat de productregel "
                "met zijn twee termen.",
            ],
        ),
        dict(
            aanpak="Een raaklijn heb je met twee dingen: de helling, dat is de afgeleide in dat punt, en "
                   "het raakpunt zelf. Vul die in de vergelijking van een rechte in.",
            waarom=[
                "Let erop dat je de y van het raakpunt uit f haalt en niet uit de afgeleide: 4 en niet "
                "min 4.",
                "Let erop dat een afgeleide altijd een verandering per eenheid is. Bij een weg in "
                "functie van de tijd is dat dus een snelheid.",
                "Let op het verschil met een afgeleide: de gemiddelde verandering is het verschil van de "
                "functiewaarden gedeeld door het verschil van de x-waarden, dus 16 min 4 gedeeld door 2.",
                "Let erop dat 3 x kwadraat min 3 nul wordt in 1. Dat betekent dat de grafiek daar "
                "horizontaal loopt.",
            ],
        ),
        dict(
            aanpak="Het teken van de eerste afgeleide zegt of de functie stijgt of daalt, dat van de "
                   "tweede of ze hol of bol is. Zet beide in een tekenschema onder elkaar.",
            waarom=[
                "Let erop dat je met de tweede afgeleide ook meteen weet welk extremum het is: negatief "
                "geeft een maximum, positief een minimum. Dat spaart een tekenschema uit.",
                "Let erop dat de laatste rij een tekenwissel eist: f dubbel priem gelijk aan nul alleen "
                "is niet genoeg voor een buigpunt.",
            ],
        ),
        dict(
            aanpak="Zet eerst de oppervlakte of het volume in één onbekende, met de gegeven voorwaarde "
                   "erin verwerkt. Leid dan af en zoek de nulwaarde.",
            waarom=[
                "Let erop dat de omtrek 40 geeft dat breedte plus lengte 20 is, niet 40. Daar gaat het "
                "het vaakst mis.",
                None,
            ],
        ),
        dict(
            aanpak="Hou de eerste en de tweede afgeleide goed uit elkaar: de eerste gaat over stijgen en "
                   "dalen, de tweede over hol en bol.",
            waarom=[
                "Niet waar: bij x tot de derde is de afgeleide nul in 0, maar de functie blijft stijgen. "
                "Dat is een buigpunt met een horizontale raaklijn.",
                "Let erop dat een hoekpunt ook een maximum kan zijn, zoals de top van min de absolute "
                "waarde van x. De afgeleide bestaat daar niet, de top wel.",
                "Niet waar: de afgeleide van e tot de x is e tot de x. De regel met de exponent vooraan "
                "geldt voor x tot de n, waar de onbekende het grondtal is.",
                "Niet waar: in een buigpunt is f dubbel priem nul. De eerste afgeleide mag daar elke "
                "waarde hebben.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-rijen-en-hun-limiet-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Reken twee keer: trek twee opeenvolgende termen van elkaar af, en deel ze ook door "
                   "elkaar. Een vast verschil is rekenkundig, een vaste factor meetkundig.",
            waarom=[
                "Let op de laatste rij: een negatieve factor mag, en dan springt de rij heen en weer "
                "rond nul. Ook dat is meetkundig.",
            ],
        ),
        dict(
            aanpak="Vul het eerste getal en het vaste getal in de formule in, en werk de haakjes dan "
                   "helemaal uit tot er een nette vorm staat.",
            waarom=[
                "Let erop dat je bij een rekenkundige rij uitwerkt tot de vorm zonder haakjes: 2 plus 7 "
                "maal n min 1 wordt 7n min 5. Bij een meetkundige rij blijft de exponent n min 1 staan.",
            ],
        ),
        dict(
            aanpak="Hou in het oog dat de teller van de exponent of van de factor altijd n min 1 is. Je "
                   "zet dus één stap minder dan het nummer van de term.",
            waarom=[
                "Let erop dat je 19 keer 3 optelt en niet 20 keer. De eerste term staat er immers al.",
                "Let erop dat de exponent 5 is en niet 6: 3 maal 2 tot de vijfde.",
                None,
                "Let erop dat de rij halveert, dus van 64 kom je in zes stappen bij 1. Een rij mag ook "
                "dalen en toch meetkundig zijn.",
            ],
        ),
        dict(
            aanpak="Voor een som heb je drie dingen nodig: de eerste term, de laatste term of het vaste "
                   "getal, en het aantal termen. Tel dat aantal eerst zorgvuldig.",
            waarom=[
                "Let erop dat dit het trucje van Gauss is: 100 maal 101 gedeeld door 2. Je paart de "
                "eerste met de laatste term, en elk paar geeft 101.",
                "Let erop dat er 25 termen zijn en niet 50: je telt enkel de even getallen. Het aantal "
                "termen fout tellen is hier de klassieke fout.",
                None,
                "Let erop dat je bij een meetkundige som de andere formule neemt: 3 maal 2 tot de zesde "
                "min 1, gedeeld door 2 min 1.",
            ],
        ),
        dict(
            aanpak="Hier is de onbekende het vaste getal zelf. Zet de twee gegeven termen in de formule "
                   "en los de vergelijking op.",
            waarom=[
                "Let erop dat je door 4 deelt, want van de derde naar de zevende term zet je vier "
                "stappen. Denk altijd in stappen en niet in termen.",
                "Let erop dat je de derde macht van q zoekt, want van de tweede naar de vijfde term zijn "
                "er drie stappen.",
                "Let erop dat je naar boven afrondt naar een geheel nummer: bij n gelijk aan 20 is de "
                "term precies 99, dus pas vanaf 21 zit je erboven.",
            ],
        ),
        dict(
            aanpak="Bij een breuk vergelijk je de hoogste graden van teller en noemer. Bij een macht "
                   "kijk je naar het grondtal.",
            waarom=[
                "Let op het laatste: min 1 tot de n springt tussen 1 en min 1 en komt nergens tot rust, "
                "dus de limiet bestaat niet. Dat is iets anders dan naar oneindig gaan.",
            ],
        ),
        dict(
            aanpak="Een oneindige meetkundige som bestaat enkel als de absolute waarde van q kleiner is "
                   "dan 1. Kijk dus eerst naar q, en reken pas daarna.",
            waarom=[
                "Let op de laatste rij: q is min een derde, en de absolute waarde daarvan is kleiner dan "
                "1, dus de som bestaat. In de noemer staat dan 1 plus een derde.",
                "Let erop dat je de herhalende groep als eerste term neemt, 36 honderdsten, en dat q "
                "één honderdste is. Zo wordt elk repeterend decimaal getal een breuk.",
            ],
        ),
        dict(
            aanpak="Hou drie woorden uit elkaar: convergent betekent naar één getal, divergent betekent "
                   "niet naar één getal, en alternerend betekent heen en weer van teken.",
            waarom=[
                None,
                None,
                "Niet waar: met een vast verschil van 3 groeit de rij onbeperkt. Alleen een rij die naar "
                "één getal kruipt, convergeert.",
                "Niet waar: enkel als de absolute waarde van q kleiner is dan 1. Bij q gelijk aan 2 "
                "groeit de som onbeperkt.",
                None,
                None,
                "Niet waar: bij q gelijk aan 1 staat er nul in de noemer. Dan is de som gewoon n maal de "
                "eerste term.",
                "Niet waar: het is precies gelijk aan 1. De oneindige som 9 tienden gedeeld door 1 min "
                "een tiende geeft exact 1.",
            ],
        ),
        dict(
            aanpak="Schrijf bij een uitlegvraag eerst de formule of de voorwaarde op die je gebruikt, en "
                   "leg daarna in woorden uit waarom ze hier past.",
            waarom=[
                None,
                "Let erop dat de voorwaarde op q het hele antwoord draagt: bij 0,6 bestaat de som, bij "
                "een factor groter dan 1 niet. Oneindig veel termen mag, oneindig groot niet.",
                "Let erop dat een limiet over een verhouding gaat en niet over de grootte. Teller en "
                "noemer groeien allebei, maar hun verhouding komt tot rust.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-primitieven-en-de-onbepaalde-integraal-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Integreren is afleiden achterstevoren. Vraag je dus telkens: welke functie heeft dit "
                   "als afgeleide? En zet de plus C erbij.",
            waarom=[
                "Let op het teken bij de sinus: de primitieve is min de cosinus, want afleiden van de "
                "cosinus geeft een minteken. En let op de absolute waarde bij 1 gedeeld door x.",
            ],
        ),
        dict(
            aanpak="Een som mag je term per term integreren, en een getal vooraan mag je buiten het "
                   "integraalteken laten staan. Eén plus C achteraan volstaat.",
            waarom=[
                "Let erop dat één enkele plus C genoeg is: de constanten van de losse termen vallen "
                "samen tot één getal.",
            ],
        ),
        dict(
            aanpak="Schrijf de integrand eerst als een macht van x, ook als er een wortel of een breuk "
                   "staat. Dan past de gewone regel weer.",
            waarom=[
                "Let erop dat 1 gedeeld door x kwadraat gelijk is aan x tot de min 2, en de primitieve "
                "dus x tot de min 1 gedeeld door min 1. Vandaar het minteken.",
                "Let erop dat de wortel x tot de helft is, dus de primitieve x tot de drie halve "
                "gedeeld door drie halve.",
                None,
                "Let erop dat je de breuk eerst splitst in x en 1 gedeeld door x. Een breuk met een som "
                "in de teller mag je splitsen, met een som in de noemer niet.",
            ],
        ),
        dict(
            aanpak="Kijk naar de bouw. Een som splits je, een product van twee verschillende soorten "
                   "vraagt partiële integratie, en staat de afgeleide van de binnenste functie er ook, "
                   "dan is het substitutie.",
            waarom=[
                "Let op de derde en de vijfde rij: daar staat de afgeleide van wat binnenin zit er "
                "gewoon bij, dus substitutie. Bij x sin x is dat niet zo, en dan heb je de partiële "
                "integratie nodig.",
            ],
        ),
        dict(
            aanpak="Noem de binnenste functie u, reken du uit, en vervang alles in de integraal. Er mag "
                   "geen x meer overblijven.",
            waarom=[
                "Let erop dat de 2x er juist staat om du te vormen. Zonder die factor was deze "
                "integraal niet elementair op te lossen.",
                None,
                "Let erop dat de afgeleide van x plus 1 gelijk is aan 1, dus hier heb je geen extra "
                "factor nodig. Je mag ook gewoon uitwerken, maar dat is veel meer rekenwerk.",
            ],
        ),
        dict(
            aanpak="Kies u zo dat de afgeleide ervan eenvoudiger wordt, en v prime zo dat je het "
                   "makkelijk kan integreren. Bij x maal iets is x bijna altijd de goede keuze voor u.",
            waarom=[
                None,
                "Let op het teken: de tweede integraal wordt min de integraal van de sinus, en dat geeft "
                "plus de cosinus. Twee mintekens die elkaar opheffen is hier de valkuil.",
            ],
        ),
        dict(
            aanpak="Zoek een primitieve, zet ze tussen vierkante haken met de grenzen erbij, en reken "
                   "dan de bovengrens min de ondergrens uit.",
            waarom=[
                "Let op de laatste: als de twee grenzen gelijk zijn, is de integraal nul. Er is dan geen "
                "stukje om oppervlakte op te meten.",
            ],
        ),
        dict(
            aanpak="Dezelfde werkwijze, maar laat e en pi als symbool staan tot op het einde. Afronden "
                   "doe je alleen als het gevraagd wordt.",
            waarom=[
                "Let erop dat je min de cosinus invult: min de cosinus van pi is plus 1, en min de "
                "cosinus van 0 is min 1. Samen 2.",
                "Let erop dat de natuurlijke logaritme van e gelijk is aan 1 en die van 1 gelijk aan 0. "
                "Daar komt het ronde antwoord uit.",
                None,
            ],
        ),
        dict(
            aanpak="Hou in het oog wat een constante is en wat niet. De plus C mag alleen weg bij een "
                   "bepaalde integraal.",
            waarom=[
                "Let erop dat ze allebei dezelfde afgeleide hebben, maar verschillen door een vaste "
                "waarde. Daarom staat die plus C er.",
                "Niet waar: enkel een getal mag buiten. Een factor met x erin hoort bij de integrand.",
                "Niet waar: met de nieuwe veranderlijke horen ook nieuwe grenzen. Anders moet je eerst "
                "terugkeren naar x.",
                None,
            ],
        ),
        dict(
            aanpak="Elke methode komt uit een afleidingsregel. Weet je waar ze vandaan komt, dan weet je "
                   "ook wanneer ze mag.",
            waarom=[
                "Let erop dat een primitieve bestaan en ze kunnen opschrijven twee verschillende dingen "
                "zijn: bij e tot de min x kwadraat bestaat ze, maar ze is niet elementair.",
                "Niet waar: je zou door nul delen. Dat is precies het geval waar de logaritme "
                "tussenkomt.",
                None,
                "Niet waar: een wortel is vaak juist een goede kandidaat voor substitutie, zoals bij de "
                "wortel van 2x plus 1.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag eerst de regel of de voorwaarde, en leg daarna in woorden "
                   "uit waarom ze hier beslist.",
            waarom=[
                None,
                None,
                "Let erop dat de constante zich wegstreept doordat je aftrekt. Dat is de reden, niet "
                "een afspraak.",
                "Let erop dat afleiden een onafhankelijke controle is: je gebruikt een andere regel dan "
                "bij het integreren, en dus herhaal je dezelfde fout niet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-bepaalde-integraal-en-haar-toepassingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zie de oppervlakte als een reeks rechthoekjes. Neem je per stukje de laagste "
                   "waarde, dan blijf je eronder; neem je de hoogste, dan ga je erover.",
            waarom=[
                "Let erop dat de werkelijke oppervlakte altijd tussen de twee ligt. Dat is precies "
                "waarom de limiet van beide hetzelfde getal moet geven.",
                "Let erop dat dx de breedte van een rechthoekje is en f(x) de hoogte. Het product is "
                "dus een oppervlakte, en de integraal telt ze op.",
            ],
        ),
        dict(
            aanpak="Zoek een primitieve, vul de bovengrens in, vul de ondergrens in en trek af. Hier "
                   "geen plus C.",
            waarom=[
                "Let op de vierde: 1 gedeeld door de wortel van x is x tot de min een half, en de "
                "primitieve is 2 maal de wortel van x.",
            ],
        ),
        dict(
            aanpak="Schrijf eerst de primitieve tussen haken met de grenzen erbij. Zo maak je bij het "
                   "aftrekken geen tekenfout.",
            waarom=[
                "Let erop dat de kettingregel achterstevoren een factor een half geeft: de primitieve "
                "van e tot de 2x is e tot de 2x gedeeld door 2.",
                "Let erop dat dit een substitutie is met u gelijk aan de logaritme van x: de 1 gedeeld "
                "door x is net haar afgeleide.",
                "Let erop dat je ook hier gewoon de twee grenzen invult: min een derde van min 1 geeft "
                "plus een derde, en samen twee derde.",
                None,
            ],
        ),
        dict(
            aanpak="Een integraal telt een stuk onder de as negatief mee. Vraagt de opgave de werkelijke "
                   "oppervlakte, dan reken je de stukken apart en neem je ze allemaal positief.",
            waarom=[
                "Let erop dat de nul niet betekent dat er geen oppervlakte is: het stuk links van de as "
                "ligt onder de as en heft het rechtse op.",
                "Let erop dat de sinus over een volle periode even veel boven als onder de as ligt. De "
                "werkelijke oppervlakte is hier 4.",
                "Let erop dat je de helft uitrekent en verdubbelt, omdat de twee stukken even groot "
                "zijn. Dat is korter dan twee aparte integralen.",
            ],
        ),
        dict(
            aanpak="Zoek eerst de snijpunten, dat zijn je grenzen. Integreer dan de bovenste functie min "
                   "de onderste, in die orde.",
            waarom=[
                "Let erop dat op dat stuk de rechte boven de parabool ligt, dus 2x min x kwadraat. "
                "Omgekeerd zou je min vier derde krijgen.",
                None,
            ],
        ),
        dict(
            aanpak="Bij een omwentelingslichaam staat de functie in het kwadraat en komt er een pi "
                   "voor. Bij een booglengte staat de afgeleide onder een wortel.",
            waarom=[
                "Let erop dat het antwoord klopt met de formule voor een kegel: een derde maal pi maal "
                "r kwadraat maal h, met r en h gelijk aan 1.",
                "Let erop dat een constante functie een cilinder geeft: pi maal 4 maal 3, dus 12 pi.",
                "Let erop dat enkel het opschrijven gevraagd wordt. Deze integraal uitrekenen vraagt "
                "een techniek die hier niet aan de orde is.",
            ],
        ),
        dict(
            aanpak="Een integraal telt altijd op over de tijd of over het aantal. Kijk naar de eenheden: "
                   "wat je integreert maal waarover je integreert geeft de eenheid van je antwoord.",
            waarom=[
                "Let erop dat de eenheden het antwoord geven: meter per seconde maal seconde is meter, "
                "en liter per seconde maal seconde is liter.",
                None,
                "Let erop dat de snelheid hier toeneemt, dus je mag niet gewoon snelheid maal tijd "
                "nemen. De primitieve van 3t is anderhalf t kwadraat.",
            ],
        ),
        dict(
            aanpak="Hou twee dingen uit elkaar: wat de integraal uitrekent, en wat de opgave vraagt. Een "
                   "georiënteerde oppervlakte kan negatief zijn, een werkelijke niet.",
            waarom=[
                None,
                None,
                "Let erop dat een oppervlakte een grootte is. De integraal kan negatief zijn, de "
                "oppervlakte zelf niet.",
                "Let erop dat de grenzen omwisselen het teken omkeert. Dat is de afspraak die de "
                "rekenregels laat kloppen.",
                "Niet waar: de hoofdstelling vraagt een continue functie. Bij een sprong moet je de "
                "stukken apart nemen.",
                "Niet waar: de bovengrens is de grootste x-waarde en niet de grootste functiewaarde. "
                "Grens en waarde zijn hier makkelijk te verwarren.",
                None,
                "Niet waar: met twee gelijke grenzen is de integraal nul. Er is geen breedte, dus geen "
                "oppervlakte.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag eerst de formule of de voorwaarde, en zeg daarna wat ze in "
                   "deze situatie betekent.",
            waarom=[
                None,
                "Let erop dat verplaatsing en afgelegde weg twee verschillende dingen zijn. Voor de weg "
                "integreer je de absolute waarde van de snelheid.",
                "Let erop dat een negatieve uitkomst bijna altijd betekent dat je de twee functies hebt "
                "verwisseld. De schets voorkomt dat.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-complexe-getallen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Deel de exponent door 4 en kijk naar de rest. Rest 0 geeft 1, rest 1 geeft i, rest 2 "
                   "geeft min 1 en rest 3 geeft min i.",
            waarom=[
                "Let erop dat je met de rest werkt en niet met de exponent zelf: 11 gedeeld door 4 laat "
                "rest 3, dus min i.",
            ],
        ),
        dict(
            aanpak="Reken met i zoals met een letter, en vervang op het einde i kwadraat door min 1. "
                   "Groepeer dan het reële en het imaginaire deel.",
            waarom=[
                "Let op de laatste: het kwadraat van 2 min i geeft 4 min 4i plus i kwadraat, en i "
                "kwadraat is min 1. Daarom komt er 3 min 4i uit en niet 5 min 4i.",
            ],
        ),
        dict(
            aanpak="Vermenigvuldig teller en noemer met de toegevoegde van de noemer. De noemer wordt "
                   "dan een gewoon getal, en de rest is eenvoudig rekenen.",
            waarom=[
                "Let erop dat de noemer 2 kwadraat plus 1 kwadraat wordt, dus 5. Je hoeft die "
                "haakjes niet uit te werken: de som van de kwadraten volstaat.",
                None,
                "Let erop dat de toegevoegde van 1 plus i gelijk is aan 1 min i, en dat de noemer dan 2 "
                "wordt.",
            ],
        ),
        dict(
            aanpak="Zet het getal als een punt in het vlak. De modulus is de afstand tot de oorsprong, "
                   "het argument de hoek met de positieve x-as.",
            waarom=[
                "Let op de tweede rij: de modulus van min 2 is 2, want een afstand is nooit negatief. "
                "Enkel het argument, 180 graden, zegt dat het getal links ligt.",
                "Let erop dat je de wortel van 36 plus 64 neemt, dus de wortel van 100. De tekens spelen "
                "geen rol, want alles wordt gekwadrateerd.",
                None,
            ],
        ),
        dict(
            aanpak="Elke bewerking met complexe getallen is ook een beweging in het vlak. Denk in "
                   "draaien en spiegelen, niet alleen in rekenen.",
            waarom=[
                "Let erop dat vier keer met i vermenigvuldigen je weer op hetzelfde punt brengt. Dat is "
                "dezelfde reden waarom de machten van i zich om de vier herhalen.",
                None,
            ],
        ),
        dict(
            aanpak="In goniometrische vorm werk je met de modulus en het argument apart. De moduli "
                   "vermenigvuldig of deel je, de argumenten tel je op of trek je af.",
            waarom=[
                "Let erop dat de twee kolommen verschillende bewerkingen krijgen: de moduli worden "
                "vermenigvuldigd en de argumenten opgeteld. Dat is net de reden waarom de Moivre werkt.",
                None,
                "Let erop dat 8 maal 45 graden precies 360 graden geeft, dus het resultaat is zuiver "
                "reëel. In cartesische vorm zou je vier keer moeten kwadrateren.",
            ],
        ),
        dict(
            aanpak="In C heeft elke vierkantsvergelijking twee oplossingen. Bij een negatieve "
                   "discriminant schrijf je de wortel ervan met een i erbij.",
            waarom=[
                "Let erop dat er twee oplossingen zijn: 3i en min 3i. Vergeet de tweede niet, net zoals "
                "bij een gewone vierkantsvergelijking.",
                "Let erop dat de discriminant min 36 is, en dat de wortel daarvan 6i is. Gedeeld door 2 "
                "geeft dat plus of min 3i.",
                "Let erop dat een vergelijking van graad n in C precies n oplossingen heeft. Ze liggen "
                "hier gelijkmatig op de eenheidscirkel.",
            ],
        ),
        dict(
            aanpak="Hou in het oog dat C een vlak is en geen rechte. Rekenen kan je ermee, ordenen niet.",
            waarom=[
                "Let erop dat complexe getallen punten in een vlak zijn. Kleiner en groter hebben daar "
                "geen betekenis; enkel hun modulus kan je vergelijken.",
                None,
                None,
                "Niet waar: de moduli worden vermenigvuldigd en niet opgeteld. Enkel de argumenten "
                "worden opgeteld.",
                None,
                "Niet waar: een negatieve discriminant geeft juist twee complexe oplossingen. In R zijn "
                "er geen, in C altijd twee.",
                None,
                "Niet waar: de modulus van min 3 is 3. Een afstand is nooit negatief.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag eerst de formule of de eigenschap, en zeg daarna wat ze in "
                   "het vlak van Gauss betekent.",
            waarom=[
                None,
                "Let erop dat dit dezelfde truc is als het rationaal maken van een noemer met een "
                "wortel. Het doel is een noemer zonder i.",
                "Let erop dat de n oplossingen een regelmatige veelhoek vormen: ze liggen op dezelfde "
                "afstand van de oorsprong en de hoeken liggen op gelijke afstand van elkaar.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-telproblemen-en-het-binomium-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Stel je twee vragen: telt de volgorde mee, en mag een element herhaald worden? Die "
                   "twee antwoorden bepalen de formule.",
            waarom=[
                "Let op het verschil tussen de eerste twee: bij goud, zilver en brons telt de volgorde "
                "mee, bij vier leden kiezen niet. Dat ene verschil kiest de formule.",
            ],
        ),
        dict(
            aanpak="Vereenvoudig een breuk met faculteiten voor je rekent: 6 faculteit gedeeld door 4 "
                   "faculteit is gewoon 6 maal 5. Zo hou je de getallen klein.",
            waarom=[
                "Let op de laatste: n boven 0 is altijd 1. Er is precies één manier om niets te kiezen.",
            ],
        ),
        dict(
            aanpak="Schrijf de formule eerst op. Bij een variatie neem je aflopende factoren, bij een "
                   "herhaling het aantal mogelijkheden tot de macht van het aantal plaatsen.",
            waarom=[
                None,
                "Let erop dat een letter hier opnieuw mag gebruikt worden, dus 26 tot de derde. Mocht "
                "dat niet mogen, dan was het 26 maal 25 maal 24.",
                None,
                "Let erop dat je deelt door 2 faculteit voor de twee K's en nog eens voor de twee O's. "
                "Zonder dat delen tel je dezelfde woorden meermaals.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de keuzes na elkaar komen of elkaar uitsluiten. Na elkaar is "
                   "vermenigvuldigen, of-of is optellen, en minstens één vraagt bijna altijd de "
                   "complementregel.",
            waarom=[
                "Let op het verschil met de volgende oefening: hier kies je drie gangen na elkaar, dus "
                "vermenigvuldigen.",
                "Let erop dat je hier optelt en niet vermenigvuldigt: je neemt het één of het ander, "
                "niet beide.",
                "Let erop dat een handdruk tussen twee mensen één keer telt, dus de volgorde doet niet "
                "mee. Daarom een combinatie en niet 8 maal 7.",
                "Let erop dat je eerst alle codes telt en daarna de codes zonder nul aftrekt. Minstens "
                "één rechtstreeks tellen zou veel ingewikkelder zijn.",
            ],
        ),
        dict(
            aanpak="Elk getal in de driehoek is de som van de twee getallen schuin erboven. De rij "
                   "begint en eindigt altijd met een 1.",
            waarom=[
                "Let erop dat de som van rij n gelijk is aan 2 tot de n. Een goede controle van je "
                "uitgewerkte rij.",
                "Let erop dat je dit ook uit de driehoek kan lezen: het derde getal van rij 7.",
                None,
            ],
        ),
        dict(
            aanpak="Neem de rij van de driehoek die bij de exponent hoort, en let op het teken bij een "
                   "verschil: dat wisselt van term tot term.",
            waarom=[
                None,
                "Let erop dat de min 2 elke keer tot een hogere macht gaat: min 2, plus 4, min 8. "
                "Daarom staat er 6, 12 en 8 en wisselen de tekens.",
                None,
            ],
        ),
        dict(
            aanpak="Je hoeft niet alles uit te werken. Met de algemene term vind je één term meteen: "
                   "kies k zo dat de exponent klopt.",
            waarom=[
                "Let erop dat je enkel 5 boven 3 nodig hebt. Het hele binomium uitwerken is hier verloren "
                "werk.",
                "Let erop dat er altijd één term meer is dan de exponent, want k loopt van 0 tot n.",
                None,
            ],
        ),
        dict(
            aanpak="Hou volgorde en herhaling goed uit elkaar. Dat ene verschil zit achter bijna elke "
                   "uitspraak in deze reeks.",
            waarom=[
                None,
                "Let erop dat p kiezen hetzelfde is als n min p weglaten. Daarom is elke rij van de "
                "driehoek symmetrisch.",
                "Niet waar: 0 faculteit is gelijk aan 1. Dat is nodig om de formules te laten kloppen, "
                "en het past bij de lege keuze.",
                None,
                None,
                "Niet waar: er staat ook een dubbel product, dus 2ab ertussen. Dat is het merkwaardige "
                "product, en rij 2 van de driehoek is 1 2 1.",
                None,
                "Niet waar: het is net omgekeerd. Elke combinatie komt overeen met p faculteit "
                "variaties, dus er zijn er minder.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag de regel of de formule, en leg daarna uit welk telprobleem "
                   "erachter zit.",
            waarom=[
                "Let erop dat de deling door p faculteit het hele antwoord is: elke groep kan je op p "
                "faculteit manieren ordenen, en die gelden samen als één combinatie.",
                None,
                "Let erop dat of-of en en-en de twee woorden zijn om op te letten. Lees de opgave daarop "
                "na voor je rekent.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kansrekenen-en-kansverdelingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Tel hoeveel gunstige uitkomsten er zijn en deel door het totaal. Vereenvoudig de "
                   "breuk pas op het einde.",
            waarom=[
                "Let op de vierde: 1 is geen priemgetal, dus enkel 2, 3 en 5 tellen mee. En let erop "
                "dat een spel 52 kaarten heeft met 4 azen, dus 1 op 13.",
            ],
        ),
        dict(
            aanpak="Lees of de twee gebeurtenissen samen moeten gebeuren of elkaar uitsluiten. Samen is "
                   "vermenigvuldigen, of-of is optellen.",
            waarom=[
                "Let erop dat twee worpen na elkaar komen, dus je vermenigvuldigt. Optellen zou een kans "
                "groter maken dan één van de twee, en dat kan niet.",
                "Let erop dat harten en ruiten elkaar uitsluiten: een kaart kan niet beide zijn. Daarom "
                "hoeft er niets afgetrokken te worden.",
            ],
        ),
        dict(
            aanpak="Twee formules volstaan: de kans op het tegengestelde is 1 min de kans, en bij een "
                   "vereniging trek je de doorsnede er één keer af.",
            waarom=[
                None,
                "Let erop dat je de doorsnede aftrekt, anders tel je de gevallen die in beide zitten "
                "dubbel. Zonder die 0,2 kwam er 1,1 uit, en dat kan geen kans zijn.",
                "Let erop dat de doorsnede hier nul is, want de gebeurtenissen sluiten elkaar uit. "
                "Daarom mag je gewoon optellen.",
                "Let erop dat minstens één het tegengestelde is van geen enkele. Daarom werkt de "
                "complementregel hier.",
            ],
        ),
        dict(
            aanpak="Vul eerst de rijen en de kolommen van de tabel aan tot alle totalen kloppen. Reken "
                   "pas daarna kansen.",
            waarom=[
                "Let erop dat het totaal van de rijen en dat van de kolommen hetzelfde moet geven, hier "
                "200. Dat is je controle dat de tabel klopt.",
            ],
        ),
        dict(
            aanpak="Kijk telkens door wat je deelt. Een gewone kans deelt door het grote totaal, een "
                   "voorwaardelijke kans door het totaal van die ene groep.",
            waarom=[
                None,
                "Let erop dat je door 100 deelt en niet door 200: je kijkt enkel binnen de groep "
                "meisjes. Dat is het hele verschil tussen de twee vorige oefeningen.",
                "Let erop dat je de twee kansen vergelijkt, 0,45 tegenover 0,375. Gelijke "
                "groepsgroottes zeggen niets over onafhankelijkheid.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de eerste gebeurtenis de kansen van de tweede verandert. Verandert ze "
                   "niets, dan zijn ze onafhankelijk.",
            waarom=[
                "Let op de tweede en de derde rij: alleen het terugleggen maakt het verschil. Zonder "
                "terugleggen is er na de eerste kaart één kaart minder in het spel.",
            ],
        ),
        dict(
            aanpak="Een kans ligt altijd tussen 0 en 1, en de kansen op de takken uit één knoop tellen "
                   "samen tot 1. Gebruik dat als controle.",
            waarom=[
                "Niet waar: dat geldt enkel als de gebeurtenissen elkaar uitsluiten. Anders moet de "
                "doorsnede eraf.",
                None,
                "Niet waar: de noemer is verschillend. Elke arts is een mens, maar niet elke mens is "
                "arts.",
                None,
            ],
        ),
        dict(
            aanpak="Teken de boom met twee lagen. Langs een pad vermenigvuldig je, en verschillende "
                   "paden naar dezelfde uitkomst tel je op.",
            waarom=[
                "Let erop dat de tweede laag andere kansen heeft: er zijn nog 3 groene van de 9 over. "
                "Zonder terugleggen verandert de noemer dus ook.",
                "Let erop dat er twee paden naar precies één groene leiden, groen dan oranje en oranje "
                "dan groen. Eén pad vergeten halveert je antwoord.",
            ],
        ),
        dict(
            aanpak="Bij minstens één reken je het tegengestelde uit, dus geen enkele, en trek je dat van "
                   "1 af. Dat is bijna altijd korter.",
            waarom=[
                "Let erop dat het tegengestelde van minstens één keer munt is: vier keer kop. Dat is "
                "één geval in plaats van vier gevallen samen te tellen.",
            ],
        ),
        dict(
            aanpak="Een binomiale verdeling vraagt vier dingen: een vast aantal pogingen, telkens twee "
                   "uitkomsten, een vaste kans en onafhankelijke pogingen.",
            waarom=[
                "Let op de tweede en de derde rij: bij de ene verandert de kans per trekking, bij de "
                "andere ligt het aantal pogingen niet vast. Telkens valt er één voorwaarde weg.",
            ],
        ),
        dict(
            aanpak="In de formule staan drie stukken: het aantal manieren, de kans op succes tot de "
                   "macht k, en de kans op mislukking tot de macht n min k.",
            waarom=[
                "Let op de derde en de vierde: bij alles of niets is de binomiaalcoëfficiënt gelijk aan "
                "1, dus er blijft één macht over.",
                "Let erop dat dit vijf keer kop op een rij is, dus een half tot de vijfde.",
                None,
            ],
        ),
        dict(
            aanpak="De verwachtingswaarde is n maal p. De standaardafwijking is de wortel van n maal p "
                   "maal 1 min p.",
            waarom=[
                "Let erop dat je bij sigma de wortel neemt van het product van drie factoren. Vergeet de "
                "laatste factor 1 min p niet.",
                "Let erop dat p maal 1 min p het grootst is in het midden. Bij een eerlijke kans is de "
                "onzekerheid dus het grootst.",
            ],
        ),
        dict(
            aanpak="Lees goed of er gelijk aan, minstens of hoogstens staat. Dat ene woord verandert de "
                   "hele betekenis van een kans.",
            waarom=[
                "Let erop dat 0,18 bij precies tien hoort en niet bij minstens tien. Zelfs de meest "
                "waarschijnlijke uitkomst heeft hier een kleine kans.",
                "Let erop dat gokken bij vier opties een kans van een kwart geeft, dus 40 maal een "
                "kwart.",
                None,
            ],
        ),
        dict(
            aanpak="Hou in het oog wat een binomiale verdeling kan en wat niet: ze telt successen, dus "
                   "een geheel getal van 0 tot n.",
            waarom=[
                "Niet waar: X loopt van 0 tot n. Meer successen dan pogingen kan niet.",
                "Niet waar: bij n gelijk aan 5 en p gelijk aan 0,3 is E gelijk aan 1,5. Een gemiddelde "
                "hoeft geen mogelijke uitkomst te zijn.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag eerst de regel, en zeg daarna wat ze in deze situatie "
                   "betekent.",
            waarom=[
                None,
                "Let erop dat sigma ongeveer 1 is, dus nul of twee fouten liggen binnen één "
                "standaardafwijking. Een verwachtingswaarde is een gemiddelde, geen voorspelling.",
            ],
        ),
        dict(
            aanpak="Reken bij een vergelijking altijd beide gevallen uit in plaats van te schatten. "
                   "Dezelfde verwachtingswaarde zegt niets over de spreiding.",
            waarom=[
                "Let erop dat de spreiding niet enkel van n afhangt: meer worpen met een kleinere kans "
                "geeft hier juist een grotere sigma.",
                "Let erop dat het verschil in de noemer zit: 100 tegenover 200. Dat is dezelfde fout als "
                "in de kruistabel hierboven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-statistiek-normale-verdeling-en-hypothesetoets-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Trek het gemiddelde van de meting af en deel door de standaardafwijking. Het teken "
                   "zegt of de meting boven of onder het gemiddelde ligt.",
            waarom=[
                "Let op de derde rij: een meting die gelijk is aan het gemiddelde geeft z gelijk aan 0. "
                "En een negatieve z betekent gewoon onder het gemiddelde.",
            ],
        ),
        dict(
            aanpak="Hier is de z-score gegeven. Werk de formule om: x is het gemiddelde plus z maal "
                   "sigma, en sigma is het verschil gedeeld door z.",
            waarom=[
                None,
                "Let op het minteken: min 0,8 maal 100 geeft min 80, dus de meting ligt onder het "
                "gemiddelde.",
                "Let erop dat je hier naar sigma zoekt: 5 gedeeld door 2,5. Kijk dus eerst wat ontbreekt "
                "voor je de formule gebruikt.",
            ],
        ),
        dict(
            aanpak="Reken altijd eerst beide z-scores uit. Dezelfde ruwe score kan in de ene groep "
                   "uitzonderlijk zijn en in de andere gewoon.",
            waarom=[
                "Let erop dat de twee 70 procent niet hetzelfde waard zijn: in een klas met een kleine "
                "spreiding valt dezelfde score veel meer op.",
            ],
        ),
        dict(
            aanpak="Reken de z-scores uit en bedenk daarna wat goed is in deze context. Bij een tijd is "
                   "een negatieve z-score het gunstige geval.",
            waarom=[
                "Let erop dat je de z-scores vergelijkt op afstand van het gemiddelde en niet op teken: "
                "min 1,6 ligt verder van nul dan min 1,25, en dat is hier beter.",
            ],
        ),
        dict(
            aanpak="Ken de drie percentages uit het hoofd: ongeveer 68, 95 en 99,7 procent. Daarmee "
                   "schat je bijna elke vraag zonder tabel.",
            waarom=[
                "Let erop dat de percentages binnen een of twee sigma liggen, niet erbuiten. De "
                "oppervlakte onder de kromme is altijd 100 procent in totaal.",
                "Let erop dat de 5 procent over beide staarten samen gaat, dus 2,5 procent per kant.",
                "Let erop dat de 68 procent symmetrisch verdeeld is: 34 procent aan elke kant van het "
                "gemiddelde.",
            ],
        ),
        dict(
            aanpak="Reken eerst de grenzen uit met het gemiddelde plus of min een, twee of drie sigma. "
                   "Pas dan lees je het percentage af.",
            waarom=[
                None,
                "Let erop dat 185 precies één sigma boven het gemiddelde ligt. Boven één sigma zit de "
                "helft van de 32 procent die buiten de 68 procent valt, dus 16 procent.",
                "Let erop dat 164 twee sigma onder het gemiddelde ligt, dus de helft van de 5 procent.",
            ],
        ),
        dict(
            aanpak="De Gausskromme is een kansverdeling: de oppervlakte eronder is altijd 1. Sigma "
                   "verandert haar vorm, niet haar oppervlakte.",
            waarom=[
                "Niet waar: de oppervlakte is altijd 1. Een grotere sigma maakt de kromme breder en "
                "platter, maar de oppervlakte blijft gelijk.",
                "Let erop dat de eenheden zich wegdelen: centimeter gedeeld door centimeter. Daarom kan "
                "je z-scores van lengtes en van tijden vergelijken.",
                None,
                "Niet waar: het normale model veronderstelt een symmetrische verdeling. Bij een duidelijk "
                "scheef histogram passen de percentages niet.",
            ],
        ),
        dict(
            aanpak="Kijk niet naar het aantal deelnemers maar naar hoe ze gekozen zijn. Wie zich zelf "
                   "aanmeldt, vormt bijna nooit een doorsnede.",
            waarom=[
                "Let erop dat meer antwoorden hier niet helpen: de scheefheid zit in wie antwoordt, niet "
                "in hoeveel er antwoorden.",
            ],
        ),
        dict(
            aanpak="Hou de twee soorten fouten uit elkaar met één vraag: helpt een grotere steekproef? "
                   "Zo ja, dan is het toeval; zo nee, dan zit het in de opzet.",
            waarom=[
                None,
                "Niet waar: een grotere scheve steekproef geeft gewoon een preciezer fout antwoord. Dat "
                "is precies het verschil met een steekproeffout.",
            ],
        ),
        dict(
            aanpak="Vraag je af waar de afwijking vandaan komt: uit het toeval van de trekking, of uit "
                   "hoe de vraag of de groep gekozen is.",
            waarom=[
                "Let op de eerste en de laatste rij: daar is de trekking eerlijk en blijft er enkel "
                "toeval over. In de twee andere zit het probleem in de opzet.",
            ],
        ),
        dict(
            aanpak="De correlatiecoëfficiënt ligt altijd tussen min 1 en 1. Het teken geeft de richting, "
                   "de grootte de sterkte.",
            waarom=[
                "Let erop dat dalende punten een negatieve r geven. De sterkte zit in het getal, de "
                "richting in het teken.",
                "Let erop dat r nooit buiten min 1 en 1 kan liggen. Een waarde daarbuiten is altijd een "
                "rekenfout.",
                "Let erop dat min 0,05 bijna nul is, dus er is geen lineair verband. Een ander soort "
                "verband is daarmee niet uitgesloten.",
            ],
        ),
        dict(
            aanpak="Zoek bij een vreemde samenhang altijd naar een derde grootheid die de twee andere "
                   "samen omhoog of omlaag duwt.",
            waarom=[
                "Let erop dat je de verborgen variabele met naam noemt. Alleen zeggen dat samenhang geen "
                "oorzaak is, legt niets uit.",
            ],
        ),
        dict(
            aanpak="Dezelfde aanpak als hierboven: zoek wat de twee grootheden samen bepaalt, en zeg wat "
                   "het is.",
            waarom=[
                "Let erop dat de richting hier omgekeerd ligt dan ze lijkt: de brand bepaalt het aantal "
                "wagens, niet omgekeerd.",
            ],
        ),
        dict(
            aanpak="Een toets bewijst nooit iets. Je vergelijkt de p-waarde met het significantieniveau "
                   "en besluit of je de nulhypothese verwerpt of aanhoudt.",
            waarom=[
                "Let erop dat een p-waarde over de gegevens gaat en niet over de hypothese: het is de "
                "kans op zo'n resultaat als H nul waar is.",
                "Let erop dat 0,08 groter is dan 0,05, dus je verwerpt niet. Aanhouden is niet hetzelfde "
                "als bewijzen dat ze waar is.",
                "Let erop dat 0,003 kleiner is dan 0,01, dus je verwerpt. Ook dan bewijs je niets, je "
                "besluit enkel dat het bewijs sterk genoeg is.",
            ],
        ),
        dict(
            aanpak="Reken eerst hoeveel valse alarmen je bij dat significantieniveau verwacht. Vergelijk "
                   "dat daarna met je vondst.",
            waarom=[
                "Let erop dat 5 procent van 100 juist 5 is. Wie genoeg toetst, vindt altijd iets; "
                "daarom moet een vondst opnieuw onderzocht worden.",
            ],
        ),
        dict(
            aanpak="Schrijf het besluit altijd voorzichtig: onvoldoende bewijs tegen de nulhypothese, en "
                   "niet dat er niets is.",
            waarom=[
                "Let erop dat een kleine steekproef een echt effect kan missen. Niets vinden en er is "
                "niets zijn twee verschillende besluiten.",
            ],
        ),
        dict(
            aanpak="Denk bij deze vraag aan de spreiding. Dezelfde afstand van het gemiddelde betekent "
                   "iets heel anders in een brede dan in een smalle verdeling.",
            waarom=[
                "Let erop dat de z-score in standaardafwijkingen rekent en dus geen eenheid heeft. Dat "
                "maakt hem over groepen heen vergelijkbaar.",
            ],
        ),
        dict(
            aanpak="Reken met een groot rond aantal mensen in plaats van met kansen. Zet de zieken en de "
                   "gezonden apart en tel de positieven in beide groepen.",
            waarom=[
                "Let erop dat de gezonde groep veel groter is: 2 procent van 9990 is al 200 mensen, "
                "tegen 10 echte zieken. Een lage ziektekans maakt het valse alarm dus de regel.",
            ],
        ),
        dict(
            aanpak="Hou in het oog waar elke kans over gaat. Alfa en de p-waarde gaan over de gegevens, "
                   "nooit over de kans dat een hypothese waar is.",
            waarom=[
                "Niet waar: de p-waarde gaat over de gegevens, niet over de hypothese. Het is de kans op "
                "zo'n resultaat als H nul waar is.",
                None,
                None,
                "Niet waar: het is net omgekeerd. Een strenger niveau maakt een type I-fout minder "
                "waarschijnlijk, maar een type II-fout juist waarschijnlijker.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-matrices-en-hun-bewerkingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Noem een matrix altijd eerst bij haar dimensie, rijen maal kolommen. Optellen vraagt "
                   "dezelfde dimensie, vermenigvuldigen vraagt dat de binnenste getallen gelijk zijn.",
            waarom=[
                "Let op de tweede en de derde rij: bij een product moeten de binnenste getallen gelijk "
                "zijn, en het resultaat krijgt de buitenste. Bij 2 bij 3 maal 2 bij 3 past dat niet.",
                None,
                "Let erop dat een kolommatrix één kolom heeft, dus de elementen staan onder elkaar. Haar "
                "dimensie is 6 bij 1.",
            ],
        ),
        dict(
            aanpak="Optellen en met een getal vermenigvuldigen doe je element per element. Werk de "
                   "factor eerst uit en tel daarna op.",
            waarom=[
                None,
                "Let erop dat je de 3 op élk element van A toepast, ook op de negatieve. En let op het "
                "teken bij min min 1, dat geeft plus 1.",
            ],
        ),
        dict(
            aanpak="Matrixrekenen lijkt op gewoon rekenen, met twee uitzonderingen: de volgorde telt, en "
                   "de dimensies moeten passen.",
            waarom=[
                None,
                "Niet waar: bij een product keert de orde om, dus B getransponeerd maal A "
                "getransponeerd. Anders kloppen de dimensies zelfs niet.",
                None,
                "Niet waar: enkel matrices met dezelfde dimensie. Een matrix van 2 bij 3 en een van 3 "
                "bij 2 kan je niet optellen.",
            ],
        ),
        dict(
            aanpak="Elk element is een rij van de eerste matrix tegen een kolom van de tweede: "
                   "vermenigvuldig paar per paar en tel op.",
            waarom=[
                "Let erop dat het element linksboven uit de eerste rij en de eerste kolom komt: 1 maal 0 "
                "plus 2 maal min 1 geeft min 2. Werk per plaats en niet per matrix.",
                "Let erop dat de dimensies hier 2 bij 3 en 3 bij 2 zijn, dus het resultaat is 2 bij 2. "
                "Controleer dat eerst, dan weet je hoeveel elementen je moet uitrekenen.",
            ],
        ),
        dict(
            aanpak="Leer deze namen samen met hun voorwaarde. Vierkant hoort bij drie van de vijf, en "
                   "dat vergeten is de klassieke fout.",
            waarom=[
                "Let erop dat de nulmatrix elke dimensie kan hebben, maar de eenheidsmatrix en de "
                "diagonaalmatrix vierkant moeten zijn.",
            ],
        ),
        dict(
            aanpak="Transponeren verwisselt de rijen en de kolommen, dus ook de twee getallen van de "
                   "dimensie.",
            waarom=[
                "Let op de tweede: bij een getransponeerd product keert ook de orde om, dus het "
                "resultaat is 2 bij 3. En let op de laatste: het aantal rijen van A getransponeerd is "
                "het aantal kolommen van A.",
            ],
        ),
        dict(
            aanpak="De determinant van orde twee is a maal d min b maal c. Eén eigenschap spaart je "
                   "rekenwerk: bij twee afhankelijke rijen is ze nul.",
            waarom=[
                "Let op de tweede en de laatste: daar hoef je niet te rekenen. Twee rijen die van elkaar "
                "afhangen geven altijd nul.",
            ],
        ),
        dict(
            aanpak="Reken eerst de determinant uit. Is ze nul, dan bestaat de inverse niet; anders "
                   "verwissel je a en d, keer je de tekens van b en c om en deel je door de "
                   "determinant.",
            waarom=[
                None,
                "Let erop dat enkel b en c van teken wisselen, en dat a en d van plaats verwisselen. Dat "
                "is de hele formule, maar de plaatsen verwarren is makkelijk.",
                "Let erop dat de tweede rij hier het dubbel is van de eerste, dus de determinant is nul. "
                "Bij de drie andere is ze dat niet.",
            ],
        ),
        dict(
            aanpak="Hou in het oog dat een determinant enkel bij een vierkante matrix bestaat, en dat de "
                   "rang nooit groter is dan het kleinste van rijen en kolommen.",
            waarom=[
                None,
                "Niet waar: een determinant bestaat enkel bij een vierkante matrix. Bij 2 bij 3 valt er "
                "niets te berekenen.",
                "Niet waar: de rang is nooit groter dan het aantal rijen, en ook niet dan het aantal "
                "kolommen.",
                "Let erop dat de rijcanonieke vorm uniek is, ook al kan je er langs verschillende wegen "
                "komen. Daarom is de rang eenduidig.",
            ],
        ),
        dict(
            aanpak="De rang is het aantal rijen dat echt nieuwe informatie geeft. Veeg de matrix uit met "
                   "rijoperaties en tel de rijen die niet nul zijn.",
            waarom=[
                None,
                "Let erop dat de nulmatrix rang 0 heeft: geen enkele rij geeft informatie. Dat is de "
                "enige matrix met rang nul.",
                "Let erop dat de determinant nul precies betekent dat niet alle rijen onafhankelijk "
                "zijn. Hoeveel er wegvallen, zegt ze niet.",
                "Let erop dat de tweede rij het dubbel is van de eerste, dus ze valt weg. Je hoeft de "
                "matrix niet helemaal te vegen om dat te zien.",
            ],
        ),
        dict(
            aanpak="Zet de aantallen in de ene matrix en de prijzen in de andere. De dimensies zeggen "
                   "zelf in welke orde het product moet staan.",
            waarom=[
                "Let erop dat het product 2 bij 2 maal 2 bij 1 is, dus 2 bij 1: één totaal per klant. De "
                "andere orde zou niet eens kunnen.",
                None,
            ],
        ),
        dict(
            aanpak="Noteer elke rijoperatie met de pijl erbij. Zo kan je je stappen later controleren en "
                   "ze ook terugdraaien.",
            waarom=[
                "Let erop dat de factor bij het vermenigvuldigen niet nul mag zijn: met nul wis je de "
                "rij en verlies je informatie.",
            ],
        ),
        dict(
            aanpak="Reken bij deze vraag beide producten volledig uit. Eén verschil in één element is al "
                   "genoeg om het besluit te dragen.",
            waarom=[
                "Let erop dat zelfs de dimensies van de twee producten niet altijd gelijk zijn. Hier wel, "
                "maar de getallen verschillen volledig.",
            ],
        ),
        dict(
            aanpak="Beantwoord de drie delen los van elkaar, en zeg bij elk welke eigenschap je "
                   "gebruikt. Ze hangen alle drie aan dezelfde vaststelling.",
            waarom=[
                "Let erop dat de drie antwoorden één oorzaak hebben: twee afhankelijke rijen. Daaruit "
                "volgen de determinant nul, de lagere rang en het ontbreken van de inverse.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-stelsels-oplossen-en-matrixmodellen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="In de uitgebreide matrix staan de coëfficiënten links van de streep en de rechterlid "
                   "ernaast. Elke rij is één vergelijking.",
            waarom=[
                "Let erop dat een ontbrekende onbekende een nul krijgt en dat je de tekens meeneemt: x "
                "min y geeft min 1.",
                "Let erop dat je van onder naar boven terugrekent: eerst y uit de tweede rij, dan x. Dat "
                "is de laatste stap van elke oplossing.",
            ],
        ),
        dict(
            aanpak="Drie rijoperaties mogen: rijen verwisselen, een rij met een getal verschillend van "
                   "nul vermenigvuldigen, en bij een rij een veelvoud van een andere optellen.",
            waarom=[
                "Let op de laatste rij: met nul vermenigvuldigen wist de vergelijking. Een negatief "
                "getal mag wel, want die stap kan je terugdraaien.",
            ],
        ),
        dict(
            aanpak="Vergelijk de twee rangen. Verschillen ze, dan is het stelsel strijdig; zijn ze gelijk "
                   "aan n, dan bepaald; zijn ze gelijk maar kleiner dan n, dan onbepaald.",
            waarom=[
                "Let erop dat je eerst de twee rangen vergelijkt en pas daarna met n: verschillende "
                "rangen betekent altijd strijdig, wat n ook is.",
            ],
        ),
        dict(
            aanpak="Het aantal vrijheidsgraden is n min de rang. Dat is het aantal onbekenden dat je "
                   "zelf mag kiezen.",
            waarom=[
                "Let op de derde: nul vrijheidsgraden betekent precies één oplossing. Het is dus geen "
                "teken dat er geen oplossing is.",
            ],
        ),
        dict(
            aanpak="Zet de twee vergelijkingen om in rechten. Snijden ze, dan is er één oplossing; vallen "
                   "ze samen, dan oneindig veel; lopen ze evenwijdig, dan geen enkele.",
            waarom=[
                "Let erop dat samenvallen en evenwijdig lopen allebei geen snijpunt in de gewone zin "
                "geven, maar wel een heel ander besluit.",
            ],
        ),
        dict(
            aanpak="Lees de laatste rij altijd eerst. Nullen met een nul erachter geven een "
                   "vrijheidsgraad, nullen met een getal erachter maken het stelsel strijdig.",
            waarom=[
                None,
                "Let erop dat een rij met alleen nullen geen tegenspraak is maar een vergelijking die "
                "wegvalt. Daarom blijft er een vrijheidsgraad over.",
                "Let erop dat de laatste rij hier 0 is gelijk aan 7 zegt, en dat kan nooit. Juist dat "
                "ene getal maakt het verschil met de vorige oefening.",
            ],
        ),
        dict(
            aanpak="Veeg de eerste onbekende weg uit de tweede rij, en reken dan terug. Schrijf elke "
                   "rijoperatie op, dan kan je je stappen nakijken.",
            waarom=[
                None,
                "Let erop dat de twee vergelijkingen hier dezelfde linkerleden hebben maar een ander "
                "rechterlid. Dat geeft 0 is gelijk aan min 1, dus er is geen oplossing.",
            ],
        ),
        dict(
            aanpak="Werk van boven naar onder tot er een driehoek staat, en reken dan van onder naar "
                   "boven terug. Doe altijd de proef in alle drie de vergelijkingen.",
            waarom=[
                "Let erop dat je de proef in alle drie de vergelijkingen doet. Bij drie onbekenden sluipt "
                "er makkelijk een tekenfout in, en de proef vindt die.",
            ],
        ),
        dict(
            aanpak="Hou de twee rangen in het oog. Bijna elke uitspraak over stelsels gaat over de rang "
                   "en niet over het aantal vergelijkingen.",
            waarom=[
                "Niet waar: twee vergelijkingen kunnen hetzelfde zeggen. Dan is de rang kleiner dan n en "
                "is het stelsel onbepaald of strijdig.",
                None,
                "Niet waar: een rij met alleen nullen, ook achter de streep, valt gewoon weg. Strijdig "
                "wordt het pas als er achter de streep een ander getal staat.",
                None,
            ],
        ),
        dict(
            aanpak="Reken eerst de determinant uit. Is ze verschillend van nul, dan kan je de inverse "
                   "gebruiken; anders moet je vegen.",
            waarom=[
                "Let erop dat de determinant hier 1 is, dus je hoeft niet te delen. Doe altijd de proef "
                "door X in het oorspronkelijke stelsel te vullen.",
                None,
            ],
        ),
        dict(
            aanpak="Kies eerst je onbekenden en noem ze bij naam. Schrijf dan per gegeven één "
                   "vergelijking op, en los pas daarna op.",
            waarom=[
                None,
                "Let erop dat een dubbele bestelling geen nieuwe informatie geeft. Je hebt twee echt "
                "verschillende bestellingen nodig om twee prijzen te vinden.",
            ],
        ),
        dict(
            aanpak="Een overgangsmatrix brengt je één stap verder. Voor k stappen verhef je de matrix "
                   "tot de macht k, en pas dan vermenigvuldig je met de begintoestand.",
            waarom=[
                "Let erop dat de macht op T staat en niet op X. De begintoestand vermenigvuldig je maar "
                "één keer.",
                None,
                "Let erop dat een overgangsmatrix altijd vierkant is: elke toestand krijgt een rij én "
                "een kolom.",
            ],
        ),
        dict(
            aanpak="Een Markov-matrix controleer je per kolom: elke kolom moet samen 1 geven, en geen "
                   "enkel element mag negatief zijn.",
            waarom=[
                "Let erop dat je per kolom telt en niet per rij. Elke kolom zegt waar alles uit die ene "
                "toestand naartoe gaat, en dat is samen het geheel.",
                "Let erop dat het totaal gelijk blijft: 90 plus 110 is nog altijd 200. Dat is een goede "
                "controle bij elk Markov-model.",
            ],
        ),
        dict(
            aanpak="Hou de twee voorwaarden in het oog: vierkant, en elke kolom samen precies 1.",
            waarom=[
                None,
                "Niet waar: een kolom moet precies 1 geven. Meer dan 1 zou betekenen dat er meer "
                "vertrekt dan er is.",
            ],
        ),
        dict(
            aanpak="Zet de knopen in dezelfde volgorde op de rijen en de kolommen. Een verbinding geeft "
                   "een 1 op twee plaatsen, want ze loopt in beide richtingen.",
            waarom=[
                "Let erop dat de matrix symmetrisch is en dat er nullen op de diagonaal staan: geen "
                "knoop is met zichzelf verbonden.",
                "Let erop dat één element van het product al het antwoord geeft. Je hoeft niet de hele "
                "matrix in het kwadraat te zetten.",
            ],
        ),
        dict(
            aanpak="Onthou het verband: de macht van de matrix is de lengte van de weg, en de orde is "
                   "het aantal knopen.",
            waarom=[
                None,
                "Niet waar: vijf knopen geven een matrix van orde 5. Elke knoop krijgt een eigen rij en "
                "kolom.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag de rijoperatie of de rang die het antwoord draagt, en leg "
                   "daarna in woorden uit waarom.",
            waarom=[
                "Let erop dat de reden omkeerbaarheid is: wat je kan terugdraaien, verandert de "
                "oplossingen niet.",
                None,
            ],
        ),
        dict(
            aanpak="Denk bij deze twee in rangen en in wat een vermenigvuldiging met T doet. Reken niets "
                   "uit wat je kan beredeneren.",
            waarom=[
                "Let erop dat een vierde vergelijking enkel helpt als ze de rang doet stijgen. Een "
                "vergelijking die niets nieuws zegt, verandert niets.",
                "Let erop dat je hier niets hoeft uit te rekenen: T maal X geeft X, dus elke verdere "
                "stap geeft opnieuw X. Dat heet een evenwichtstoestand.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-algebraische-structuren-en-groepen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Loop de vier eigenschappen altijd in dezelfde orde af: intern, associatief, "
                   "neutraal element, invers element. Dan vergeet je er geen.",
            waarom=[
                "Let erop dat intern over de verzameling gaat en associatief over de haakjes. Die twee "
                "woorden verwar je makkelijk.",
            ],
        ),
        dict(
            aanpak="Schrijf elke eigenschap met het sterretje in plaats van met plus of maal. Zo zie je "
                   "dat ze over elke bewerking gaat.",
            waarom=[
                "Let erop dat bij het invers element beide kanten staan: a maal a omgekeerd én "
                "omgekeerd. In een groep die niet commutatief is, moet dat allebei gelden.",
            ],
        ),
        dict(
            aanpak="Ga per rij de vier eigenschappen na. Eén eigenschap die ontbreekt, is al genoeg om "
                   "te besluiten dat het geen groep is.",
            waarom=[
                "Let op de vijfde rij: oneven plus oneven geeft even, dus de bewerking is niet eens "
                "intern. Daar struikelt het al bij de eerste eigenschap.",
            ],
        ),
        dict(
            aanpak="Zoek bij elke vraag één tegenvoorbeeld. Eén getal dat niet past, is genoeg bewijs.",
            waarom=[
                "Let erop dat de natuurlijke getallen wel een neutraal element hebben, de nul. Enkel het "
                "invers element ontbreekt, want min 3 is geen natuurlijk getal.",
                None,
                "Let erop dat nul het enige reële getal is zonder invers element: er bestaat geen getal "
                "dat met nul vermenigvuldigd 1 geeft.",
            ],
        ),
        dict(
            aanpak="Het neutraal element is het element dat niets verandert. Bij een optelling is dat "
                   "nul, bij een vermenigvuldiging 1.",
            waarom=[
                "Let erop dat ook bij matrices dezelfde logica geldt: de nulmatrix bij het optellen en "
                "de eenheidsmatrix bij het vermenigvuldigen.",
            ],
        ),
        dict(
            aanpak="Het invers element is wat je nodig hebt om bij e te komen. Bij een optelling is dat "
                   "het tegengestelde, bij een vermenigvuldiging het omgekeerde.",
            waarom=[
                "Let op de laatste twee: e is zijn eigen invers, en het invers van het invers is het "
                "element zelf. Die twee gelden in élke groep.",
            ],
        ),
        dict(
            aanpak="Let erop dat de grootte van de verzameling niets zegt. Enkel de vier eigenschappen "
                   "beslissen of het een groep is.",
            waarom=[
                None,
                "Niet waar: de matrices van orde 2 met een determinant verschillend van nul vormen een "
                "groep die niet commutatief is. Eindig en commutatief zijn twee aparte dingen.",
                None,
                "Niet waar: de gehele getallen met de optelling vormen een oneindige groep. Oneindig zijn "
                "is geen bezwaar.",
            ],
        ),
        dict(
            aanpak="De tabel is vierkant: zoveel rijen en kolommen als er elementen zijn. Het aantal "
                   "vakjes is dus het aantal elementen in het kwadraat.",
            waarom=[
                "Let erop dat de kopregel en de kopkolom niet meetellen. Bij 7 elementen zijn er dus 49 "
                "vakjes en niet 64.",
            ],
        ),
        dict(
            aanpak="Een Cayley-tabel verraadt de eigenschappen in haar vorm. Kijk naar de diagonaal, "
                   "naar de symmetrie en naar wat zich in een rij herhaalt.",
            waarom=[
                "Let op de laatste: in een groep komt elk element precies één keer per rij voor. Een "
                "element dat twee keer staat, sluit een groep dus uit.",
            ],
        ),
        dict(
            aanpak="Tel gewoon op en hou de rest na deling door 3 over. Zo komt 2 plus 2 op 1 uit, want "
                   "4 laat rest 1.",
            waarom=[
                "Let erop dat elke rij een plaats opschuift. Dat patroon is een goede controle dat je "
                "nergens een rest fout berekend hebt.",
                None,
            ],
        ),
        dict(
            aanpak="Bij het inverse van een product keert de orde om. Schrijf de factoren achterstevoren "
                   "en zet bij elk het invers.",
            waarom=[
                None,
                "Let erop dat de orde omkeert: eerst b omgekeerd en dan a omgekeerd. Dat is de regel die "
                "het vaakst fout gaat.",
                "Let erop dat de orde ook bij drie factoren volledig omkeert, dus van achter naar voor.",
            ],
        ),
        dict(
            aanpak="Bewerk aan de kant waar het element staat. Staat a links, dan bewerk je links; "
                   "staat het rechts, dan rechts.",
            waarom=[
                None,
                "Let erop dat je van buiten naar binnen werkt: eerst b weg, dan a. En alles gebeurt aan "
                "de rechterkant, want daar staan ze.",
            ],
        ),
        dict(
            aanpak="Hou in het oog dat de orde telt, tenzij de groep commutatief is. Dat onderscheid "
                   "zit achter bijna elke uitspraak hier.",
            waarom=[
                "Niet waar: de orde keert om, dus b omgekeerd eerst. Enkel in een commutatieve groep "
                "mag je ze omwisselen.",
                None,
                "Niet waar: het neutraal element is uniek. Dat is precies wat het bewijs hieronder "
                "aantoont.",
                "Let erop dat dit mag omdat de groep commutatief is. Vergelijk met de eerste uitspraak "
                "van deze reeks: dezelfde formule, maar daar zonder die voorwaarde.",
            ],
        ),
        dict(
            aanpak="Vertrek bij een bewijs van de definitie en werk met de eigenschappen. Bij "
                   "uniciteit veronderstel je twee elementen en toon je dat ze gelijk zijn.",
            waarom=[
                "Let erop dat je dezelfde uitdrukking twee keer anders leest: één keer met e neutraal en "
                "één keer met e prime neutraal. Daaruit volgt meteen dat ze gelijk zijn.",
                "Let erop dat je enkel moet nagaan dat het product e geeft. Dat is per definitie wat een "
                "invers element is.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag de eigenschap of de voorwaarde die het antwoord draagt, en "
                   "zeg daarna in woorden waarom.",
            waarom=[
                "Let erop dat een Cayley-tabel enkel bij een eindige groep bestaat. Voor een oneindige "
                "groep bewijs je de eigenschappen met letters.",
                None,
            ],
        ),
        dict(
            aanpak="Denk bij deze twee in de eigenschappen en niet in getallen. Eén eigenschap kan al "
                   "een andere opleveren.",
            waarom=[
                "Let erop dat de commutativiteit hier een gevolg is en geen bijkomende aanname: ze volgt "
                "uit het feit dat elk element zijn eigen invers is.",
                "Let erop dat de nul in de gehele getallen geen invers element heeft. Daarom mag je daar "
                "niet schrappen, en in een groep wel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-punten-vectoren-en-afstanden-in-de-ruimte-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Trek de coördinaten van het beginpunt van die van het eindpunt af, in die orde. De "
                   "norm reken je daarna met de stelling van Pythagoras in drie richtingen.",
            waarom=[
                "Let op de derde rij: twee coördinaten blijven gelijk, dus de vector loopt zuiver langs "
                "de z-as. En let op de tekens bij de laatste: min 1 min min 1 geeft 2.",
            ],
        ),
        dict(
            aanpak="Vectoren tel je op en trek je af per coördinaat. De eerste bij de eerste, de tweede "
                   "bij de tweede, de derde bij de derde.",
            waarom=[
                "Let erop dat twee gelijke vectoren aftrekken de nulvector geeft, en niet het getal nul. "
                "Een vector blijft een vector.",
            ],
        ),
        dict(
            aanpak="Een getal maal een vector werkt op elke coördinaat. Een negatief getal keert de "
                   "richting om.",
            waarom=[
                "Let erop dat min 1 maal een vector alle tekens omkeert: dat is de tegengestelde vector, "
                "met dezelfde lengte.",
            ],
        ),
        dict(
            aanpak="Kwadrateer de drie coördinaten, tel ze op en neem de wortel. De tekens spelen geen "
                   "rol, want alles wordt gekwadrateerd.",
            waarom=[
                "Let erop dat de nullen niets bijdragen, en dat een negatieve coördinaat dezelfde norm "
                "geeft als haar tegengestelde.",
            ],
        ),
        dict(
            aanpak="Hou in het oog dat een vector enkel een richting, een zin en een lengte is. Waar ze "
                   "begint, doet voor een vrije vector niet mee.",
            waarom=[
                "Niet waar: een norm is een lengte, dus nooit negatief. Ze is nul enkel voor de "
                "nulvector.",
                None,
                "Niet waar: dezelfde coördinaten betekent dezelfde vrije vector. Enkel het beginpunt "
                "verschilt, en dat hoort niet bij de vector.",
                "Let erop dat elk veelvoud van een richtingsvector ook een richtingsvector is. Daarom "
                "zijn er oneindig veel.",
            ],
        ),
        dict(
            aanpak="De coördinaten zijn de getallen vóór de eenheidsvectoren. Een ontbrekende as "
                   "betekent een nul op die plaats.",
            waarom=[
                None,
                "Let erop dat de y-coördinaat nul is, want er staat geen e y in de som. Een ontbrekende "
                "term is een nul en niet een 1.",
            ],
        ),
        dict(
            aanpak="Vermenigvuldig de overeenkomstige coördinaten en tel de drie producten op. Het "
                   "resultaat is een getal, geen vector.",
            waarom=[
                "Let op de laatste: 2 min 4 plus 3 geeft 1. Let goed op de tekens, want één fout teken "
                "verandert het besluit over de hoek.",
            ],
        ),
        dict(
            aanpak="Het teken van het scalair product beslist: positief geeft een scherpe hoek, nul een "
                   "rechte, negatief een stompe.",
            waarom=[
                "Let erop dat het teken alleen genoeg is: je hoeft de hoek niet uit te rekenen om te "
                "weten of ze scherp of stomp is.",
            ],
        ),
        dict(
            aanpak="Kijk eerst of de ene vector een veelvoud is van de andere, dan zijn ze evenwijdig. "
                   "Is dat niet zo, reken dan het scalair product uit.",
            waarom=[
                "Let op de laatste rij: min 4, 2, 0 is min 2 maal de eerste vector. Een negatieve factor "
                "maakt ze evenwijdig met tegengestelde zin, maar nog altijd evenwijdig.",
            ],
        ),
        dict(
            aanpak="Zet de voorwaarde om in een vergelijking: loodrecht geeft scalair product nul, "
                   "evenwijdig geeft een veelvoud.",
            waarom=[
                None,
                "Let erop dat je de factor k eerst uit één coördinaat haalt en dan nakijkt of ze overal "
                "klopt. Eén coördinaat die niet past, maakt ze niet evenwijdig.",
            ],
        ),
        dict(
            aanpak="Reken eerst het scalair product en de twee normen uit, en vul dan de formule in. Een "
                   "negatieve cosinus hoort bij een stompe hoek.",
            waarom=[
                None,
                "Let erop dat de cosinus hier negatief is, dus de hoek is stomp. Vergeleken met de "
                "vorige oefening is enkel het teken anders, en dat geeft 135 in plaats van 45 graden.",
            ],
        ),
        dict(
            aanpak="Een afstand tussen twee punten is de norm van de vector ertussen. Bij de oorsprong "
                   "zijn dat gewoon de coördinaten van het punt.",
            waarom=[
                "Let erop dat twee coördinaten gelijk zijn, dus er blijft één verschil over. De afstand "
                "is dan gewoon dat verschil.",
                None,
                "Let erop dat 1, 16 en 64 samen 81 geven. Mooie ronde uitkomsten zijn hier een teken dat "
                "je goed gerekend hebt.",
            ],
        ),
        dict(
            aanpak="Een midden is het gemiddelde van twee punten, een zwaartepunt het gemiddelde van "
                   "alle hoekpunten. Tel op en deel door het aantal.",
            waarom=[
                "Let erop dat je bij een driehoek door 3 deelt en bij een viervlak door 4. Het aantal "
                "punten bepaalt de noemer.",
            ],
        ),
        dict(
            aanpak="Hou in het oog wat een scalair product oplevert: een getal. Dat is de reden achter "
                   "bijna elke uitspraak hier.",
            waarom=[
                None,
                "Niet waar: v maal v geeft de norm in het kwadraat. Je moet er dus nog de wortel van "
                "nemen.",
                None,
                "Niet waar: het resultaat is een getal, vandaar de naam scalair. Het vectorieel product "
                "geeft wel een vector.",
            ],
        ),
        dict(
            aanpak="Zet de gegevens eerst als vectoren en reken dan. Krachten en wegen in verschillende "
                   "richtingen tel je als vectoren op, niet als getallen.",
            waarom=[
                "Let erop dat de twee krachten loodrecht op elkaar staan, dus Pythagoras geeft 5. Enkel "
                "bij dezelfde richting zou 7 kloppen.",
                "Let erop dat de weg en de afstand twee verschillende dingen zijn: de weg is de som van "
                "de stukken, de afstand de rechte lijn naar het eindpunt.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag de formule of de voorwaarde, en zeg daarna waarom ze hier "
                   "nodig is.",
            waarom=[
                "Let erop dat de formule niets anders is dan Pythagoras. Scheve assen of ongelijke "
                "eenheden breken dus het hele rekenwerk.",
                None,
            ],
        ),
        dict(
            aanpak="Werk bij deze twee met letters in plaats van met getallen. Dan geldt je besluit voor "
                   "elk punt en niet enkel voor dit voorbeeld.",
            waarom=[
                None,
                "Let erop dat er twee oplossingen zijn: de norm werkt met kwadraten, dus het teken van t "
                "doet niet mee. Eén oplossing opschrijven is hier onvolledig.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-rechten-en-vlakken-in-de-ruimte-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een rechte heeft één richting nodig, een vlak twee. Werk je met een normaalvector, "
                   "dan volstaat er één, want die staat loodrecht op het hele vlak.",
            waarom=[
                "Let op de tweede rij: de twee richtingsvectoren mogen niet evenwijdig zijn, anders "
                "beschrijven ze samen maar één richting en krijg je geen vlak.",
            ],
        ),
        dict(
            aanpak="Onthou het verband met de ruimte: elke vergelijking neemt één vrijheidsgraad weg. "
                   "Een vlak houdt er twee over, een rechte één.",
            waarom=[
                "Let op de eerste twee: in het vlak volstaat één vergelijking, in de ruimte heb je er "
                "twee nodig, want een rechte is daar de doorsnede van twee vlakken.",
            ],
        ),
        dict(
            aanpak="Zet het punt als vast deel en de richtingsvector maal t erachter, per coördinaat. "
                   "Werk je met twee punten, dan reken je eerst de vector ertussen uit.",
            waarom=[
                None,
                "Let erop dat de tweede coördinaat van de richtingsvector nul is, dus y blijft gelijk "
                "aan 1. Een vergelijking zonder t is geen fout.",
            ],
        ),
        dict(
            aanpak="De getallen vóór x, y en z vormen samen de normaalvector. Een ontbrekende "
                   "veranderlijke geeft een nul op die plaats.",
            waarom=[
                "Let op de tweede en de derde: een ontbrekende veranderlijke betekent een nul in de "
                "normaalvector, en de losse term d speelt er geen rol in.",
            ],
        ),
        dict(
            aanpak="Vul de normaalvector in als a, b en c, en gebruik het punt om d te vinden. Doe de "
                   "proef door het punt opnieuw in te vullen.",
            waarom=[
                "Let erop dat de y wegvalt, want b is nul. Reken d met het punt uit en niet op het zicht.",
                "Let erop dat een vlak door de oorsprong altijd d gelijk aan nul heeft. Dat is een "
                "handige controle.",
            ],
        ),
        dict(
            aanpak="Vul de drie coördinaten in de vergelijking in. Komt er nul uit, dan ligt het punt in "
                   "het vlak.",
            waarom=[
                "Let erop dat je elke coördinaat op haar eigen plaats zet. Eén coördinaat verwisselen "
                "geeft meteen een fout besluit.",
            ],
        ),
        dict(
            aanpak="Hou in het oog hoeveel gegevens elk voorwerp nodig heeft. Dat zit achter bijna elke "
                   "uitspraak hier.",
            waarom=[
                "Niet waar: in de ruimte heeft een rechte er twee nodig. Eén vergelijking beschrijft "
                "daar een vlak.",
                None,
                "Niet waar: drie punten op één rechte liggen in oneindig veel vlakken. Ze moeten niet op "
                "één rechte liggen.",
                None,
            ],
        ),
        dict(
            aanpak="Zet per geval alle mogelijkheden op een rij voor je er één kiest. Kruisend bestaat "
                   "enkel bij twee rechten in de ruimte.",
            waarom=[
                "Let erop dat twee vlakken elkaar nooit in één punt snijden: hun doorsnede is een rechte "
                "of ze zijn evenwijdig.",
            ],
        ),
        dict(
            aanpak="Vergelijk eerst de twee normaalvectoren. Zijn ze veelvouden van elkaar, kijk dan "
                   "naar d om samenvallend van evenwijdig te onderscheiden.",
            waarom=[
                "Let op de eerste twee rijen: dezelfde normaalvectoren, maar de ene vergelijking is het "
                "dubbel van de andere en de andere niet. Juist dat ene getal beslist.",
            ],
        ),
        dict(
            aanpak="Vergelijk de richtingsvector met de normaalvector. Scalair product nul geeft "
                   "evenwijdig, een veelvoud geeft loodrecht, en anders snijdt ze schuin.",
            waarom=[
                "Let op de eerste twee: een scalair product van nul betekent evenwijdig met het vlak, "
                "niet loodrecht erop. Dat is precies omgekeerd aan wat je zou verwachten.",
            ],
        ),
        dict(
            aanpak="Vul het punt in de vergelijking in, neem de absolute waarde, en deel door de norm "
                   "van de normaalvector.",
            waarom=[
                None,
                "Let erop dat de teller hier enkel de losse term is, met de absolute waarde erom. Een "
                "afstand is nooit negatief.",
                "Let erop dat de noemer altijd 3 is bij dit vlak: hij hangt enkel van de normaalvector "
                "af en niet van het punt.",
            ],
        ),
        dict(
            aanpak="De hoek tussen twee vlakken is de hoek tussen hun normaalvectoren. Neem de absolute "
                   "waarde, zodat je altijd de scherpe hoek krijgt.",
            waarom=[
                None,
                "Let erop dat een hoek van nul graden betekent dat de vlakken evenwijdig zijn. Dat de "
                "vlakken niet samenvallen, verandert die hoek niet.",
            ],
        ),
        dict(
            aanpak="Hou in het oog wat er in de ruimte bij komt tegenover het vlak. Kruisende rechten "
                   "zijn het enige geval dat in het vlak niet bestaat.",
            waarom=[
                None,
                "Niet waar: twee niet-evenwijdige vlakken snijden elkaar volgens een rechte. Eén punt "
                "kan alleen bij drie vlakken.",
                "Niet waar: de richtingsvector loodrecht op de normaalvector betekent evenwijdig met het "
                "vlak. Loodrecht erop zou een veelvoud van de normaalvector vragen.",
                None,
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag de eigenschap of het aantal vrijheidsgraden dat het "
                   "antwoord draagt, en leg daarna in woorden uit waarom.",
            waarom=[
                None,
                "Let erop dat het tweede deel van de vraag het belangrijkste is: in het vlak kan dit "
                "geval niet bestaan, want twee niet-evenwijdige rechten snijden er altijd.",
                None,
            ],
        ),
        dict(
            aanpak="Zet de situatie eerst om in vlakken en rechten met hun vectoren. Zeg daarna pas wat "
                   "je berekent, en ook wat het niet is.",
            waarom=[
                "Let erop dat de vraag ook wil weten welke hoek het níet is. De hellingshoek van het dak "
                "meet je tegenover de horizontale grond, niet tegenover de gevel.",
                "Let erop dat geen snijpunt niet betekent dat de afstand nul is. Bij kruisende rechten "
                "meet je de kortste loodrechte afstand.",
            ],
        ),
        dict(
            aanpak="Denk bij deze twee eerst in vectoren en pas daarna in getallen. De normaalvectoren "
                   "beslissen over de ligging, een punt pas over de afstand.",
            waarom=[
                "Let erop dat je ook een punt nodig hebt: loodrecht op de normaalvector maakt de rechte "
                "evenwijdig, niet liggend in het vlak.",
                "Let erop dat je een punt op het ene vlak kiest en de formule met het ándere vlak "
                "gebruikt. En let op de noemer: de wortel van 12 hoort bij de tweede vergelijking.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-programmeren-algoritmen-en-structuren-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer deze vier namen met een voorbeeld erbij. Een conditie kiest, een iteratie "
                   "herhaalt; dat is het verschil dat het vaakst gevraagd wordt.",
            waarom=[
                "Let op het verschil tussen een variabele en een constante: niet de soort waarde maakt "
                "het verschil, maar of ze nog verandert.",
                "Let erop dat een functie ook een eigen naam heeft en opnieuw opgeroepen kan worden. Dat "
                "is net wat haar nuttig maakt.",
            ],
        ),
        dict(
            aanpak="Elk sleutelwoord hoort bij één bouwsteen. Koppel ze twee aan twee: if bij kiezen, "
                   "for bij herhalen, def bij een functie, return bij haar antwoord.",
            waarom=[
                "Let op de laatste twee: def maakt de functie, return geeft het resultaat terug. Een "
                "functie zonder return rekent iets uit en geeft niets.",
            ],
        ),
        dict(
            aanpak="Stel je twee vragen: telt de volgorde, en mag het veranderen? Daarmee kies je tussen "
                   "een list, een tuple, een set en een dictionary.",
            waarom=[
                "Let op de laatste twee rijen: een set laat geen dubbels toe, en een tuple kan je niet "
                "meer wijzigen. Juist die eigenschap maakt ze hier de beste keuze.",
            ],
        ),
        dict(
            aanpak="Een set houdt elke waarde maar één keer. Tel dus hoeveel verschillende waarden er in "
                   "de lijst staan.",
            waarom=[
                "Let op de derde rij: vier keer hetzelfde getal geeft één element. En let erop dat de "
                "volgorde in een set geen rol speelt.",
            ],
        ),
        dict(
            aanpak="Hou per structuur twee dingen in het oog: de volgorde en of ze aanpasbaar is. "
                   "Daarmee beantwoord je bijna elke uitspraak.",
            waarom=[
                "Niet waar: een tuple ligt vast. Wil je nog wijzigen, dan heb je een list nodig.",
                None,
                "Niet waar: in een set staat elk element precies één keer. Een tweede keer toevoegen "
                "verandert niets.",
                None,
            ],
        ),
        dict(
            aanpak="Leer deze vier technieken met hun kernwoord: zichzelf oproepen, opsplitsen, "
                   "bewaren, halveren.",
            waarom=[
                "Let erop dat halveren ook verdeel-en-heers is: je gooit elke stap de helft weg en lost "
                "verder in de andere helft op.",
            ],
        ),
        dict(
            aanpak="Een recursieve formule bestaat altijd uit twee delen: de stap die terugverwijst, en "
                   "het stopgeval. Zonder het stopgeval stopt het programma nooit.",
            waarom=[
                "Let erop dat het stopgeval 0 faculteit gelijk aan 1 is, en niet 1 faculteit. Anders "
                "werkt de formule niet voor nul.",
                "Let erop dat Fibonacci twee stopgevallen nodig heeft, want de formule kijkt twee "
                "stappen terug.",
            ],
        ),
        dict(
            aanpak="Reken de rij van onder op in plaats van van boven af. Dan hou je de tussenresultaten "
                   "bij en hoef je niets twee keer te doen.",
            waarom=[
                "Let erop dat de rij van Fibonacci veel trager groeit dan de faculteit: 6 faculteit is "
                "al 720, terwijl F van 8 maar 21 is.",
            ],
        ),
        dict(
            aanpak="Elke stap halveert de rij. Tel dus hoeveel keer je door 2 kan delen tot er één "
                   "getal overblijft; dat is de logaritme met grondtal 2.",
            waarom=[
                "Let erop dat 1024 getallen maar 10 stappen vragen. Dat is precies waarom halveren zo "
                "veel sneller is dan één voor één doorlopen.",
            ],
        ),
        dict(
            aanpak="Schrijf de boom van oproepen eerst uit. Dan zie je zelf welke waarden meer dan één "
                   "keer berekend worden.",
            waarom=[
                "Let erop dat je de oproepen echt uitschrijft: zo zie je dat F van 1 drie keer berekend "
                "wordt, en dat is precies de verspilling.",
                None,
            ],
        ),
        dict(
            aanpak="Hou de twee woorden uit elkaar: correct gaat over het antwoord, eindig over het "
                   "stoppen. Een programma heeft ze allebei nodig.",
            waarom=[
                "Let erop dat de twee onafhankelijk zijn: een algoritme kan juist redeneren en toch "
                "eeuwig blijven lopen.",
                None,
            ],
        ),
        dict(
            aanpak="Een algoritme is een werkwijze, niet een taal. Dat idee zit achter bijna elke "
                   "uitspraak in deze reeks.",
            waarom=[
                "Niet waar: een algoritme is een werkwijze in eindig veel stappen. Je kan ze ook in "
                "woorden of in een schema zetten.",
                "Niet waar: hetzelfde antwoord kan je op een snelle en op een trage manier vinden. Kijk "
                "naar de laatste doordenker van deze bundel.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Elke bibliotheek doet één soort werk. Koppel de naam aan die taak en je hoeft niets "
                   "van buiten te leren.",
            waarom=[
                None,
                "Let erop dat een CSV-bestand gewoon tekst is met komma's ertussen. Daarom kan je het "
                "met een rekenblad openen en met een programma inlezen.",
            ],
        ),
        dict(
            aanpak="Vul n in de formule in en reken. Bij een logaritme met grondtal 2 is dat ongeveer "
                   "10 bij duizend.",
            waarom=[
                "Let erop dat het verschil enorm is: 10 tegenover een miljoen bij hetzelfde aantal "
                "gegevens. Daarom kijk je naar het groeigedrag en niet naar de klok.",
            ],
        ),
        dict(
            aanpak="Een Riemannsom telt stroken op: hoogte maal breedte, en dat n keer. Schrijf eerst op "
                   "wat delta x is.",
            waarom=[
                None,
                "Let erop dat smallere stroken de benadering beter maken, niet slechter. Dat is het idee "
                "achter de integraal: de limiet voor n naar oneindig.",
            ],
        ),
        dict(
            aanpak="Noem bij een uitlegvraag ook waarom het telt voor wie je code leest. Leesbaarheid is "
                   "een deel van de beoordeling en geen opsmuk.",
            waarom=[
                None,
                "Let erop dat testen en debuggen er echt bij horen: zonder die vierde stap weet je niet "
                "of je programma werkt.",
            ],
        ),
        dict(
            aanpak="Denk bij deze twee aan de voorwaarde en aan het groeigedrag. Een techniek werkt "
                   "alleen als haar voorwaarde klopt.",
            waarom=[
                "Let erop dat halveren een gesorteerde rij veronderstelt. Sorteren kost zelf tijd, dus "
                "dat is pas de moeite als je vaak moet zoeken.",
                "Let erop dat je de twee bij een klein en bij een groot aantal vergelijkt. Bij kleine "
                "aantallen zie je het verschil niet, en dat maakt een trage aanpak verraderlijk.",
            ],
        ),
    ],
)

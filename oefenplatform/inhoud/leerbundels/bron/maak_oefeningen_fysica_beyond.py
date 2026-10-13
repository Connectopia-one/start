# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij fysica 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
stof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen om mee te rekenen, andere situaties om te beoordelen,
en opdrachten die je enkel op papier kan maken (een formule omvormen, een
tabel aanvullen, een stap uitleggen). Wie hier iets bijschrijft, legt het
eerst naast `../../beyond/fysica.json` en naast de leerbundel van hetzelfde
thema in `maak_fysica_beyond.py`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.

De waarden die een opgave nodig heeft (g, k, h, een specifieke warmte) staan
telkens bij de opgave zelf, zodat er geen formularium naast het blad moet
liggen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Fysica"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

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

# ============================================================
OEFENBUNDELS["oefenbundel-elektrische-lading-geleiders-en-influentie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrische lading, geleiders en influentie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Geleider of isolator",
             opdracht="Schrijf geleider of isolator.",
             oefeningen=[
                 ("rij", [("koperdraad", "geleider"), ("droog hout", "isolator"),
                          ("zout water", "geleider")],
                  "Geleider of isolator?", WW),
                 ("rij", [("rubber", "isolator"), ("aluminiumfolie", "geleider"),
                          ("glas", "isolator")],
                  "Geleider of isolator?", WW),
                 ("open", "Leg uit waarom een metaal geleidt en glas niet.",
                  "In een metaal zitten vrije elektronen die niet aan één atoom vastzitten en dus "
                  "door het hele stuk kunnen bewegen. In glas zit elk elektron vast aan zijn eigen "
                  "atoom, dus kan de lading er niet doorheen.", 5),
             ]),
        dict(kop="Aantrekken of afstoten",
             opdracht="Schrijf aantrekken of afstoten.",
             oefeningen=[
                 ("rij", [("twee negatieve ladingen", "afstoten"),
                          ("een positieve en een negatieve", "aantrekken"),
                          ("twee positieve ladingen", "afstoten")],
                  "Wat gebeurt er?", WW),
             ]),
        dict(kop="Eenheden omzetten",
             opdracht=r"Schrijf elke lading in coulomb, in de vorm \(a\cdot 10^{n}\ \text{C}\).",
             oefeningen=[
                 ("rij", [(r"\(7\ \text{nC}\)", r"\(7\cdot 10^{-9}\ \text{C}\)"),
                          (r"\(2{,}5\ \mu\text{C}\)", r"\(2{,}5\cdot 10^{-6}\ \text{C}\)"),
                          (r"\(40\ \text{pC}\)", r"\(4{,}0\cdot 10^{-11}\ \text{C}\)"),
                          (r"\(0{,}8\ \text{mC}\)", r"\(8\cdot 10^{-4}\ \text{C}\)")],
                  "Hoeveel coulomb?", WW),
             ]),
        dict(kop="Rekenen met Q = n · e",
             opdracht=r"Reken uit met \(e=1{,}602\cdot 10^{-19}\ \text{C}\). Schrijf eerst de formule op.",
             oefeningen=[
                 ("kort", r"Een voorwerp mist \(5{,}0\cdot 10^{12}\) elektronen. Hoe groot is \(Q\)?",
                  r"\(Q=+8{,}0\cdot 10^{-7}\ \text{C}\): "
                  r"\(5{,}0\cdot 10^{12}\cdot 1{,}602\cdot 10^{-19}\ \text{C}\), en missen betekent positief.", WL),
                 ("kort", r"Hoeveel elektronen horen bij \(Q=-3{,}2\cdot 10^{-17}\ \text{C}\)?",
                  r"\(n=\dfrac{3{,}2\cdot 10^{-17}}{1{,}602\cdot 10^{-19}}\approx 2{,}0\cdot 10^{2}\) elektronen te veel.", WL),
                 ("kort", r"Hoeveel elektronen te veel zitten er op een bol met \(Q=-1{,}0\ \mu\text{C}\)?",
                  r"\(n=\dfrac{1{,}0\cdot 10^{-6}}{1{,}602\cdot 10^{-19}}\approx 6{,}2\cdot 10^{12}\) elektronen.", WL),
                 ("open", r"Kan een voorwerp een lading van \(2{,}5\cdot 10^{-19}\ \text{C}\) dragen? Leg uit met \(Q=n\cdot e\).",
                  r"Nee. \(n=\dfrac{2{,}5\cdot 10^{-19}}{1{,}602\cdot 10^{-19}}\approx 1{,}56\), en dat is geen geheel getal. "
                  r"Lading is gekwantiseerd: ze komt in hele pakjes \(e\), dus enkel gehele veelvouden bestaan.", 5),
             ]),
        dict(kop="Lading verdelen",
             opdracht="Gebruik telkens dat de totale lading behouden blijft.",
             oefeningen=[
                 ("open", r"Een bol met \(+4\ \text{nC}\) en een even grote bol met \(-2\ \text{nC}\) raken elkaar aan en worden weer gescheiden. Welke lading draagt elk nu? Leg uit.",
                  r"Elk \(+1\ \text{nC}\). De som blijft \(+4-2=+2\ \text{nC}\), en twee even grote bollen "
                  r"verdelen dat gelijk. Lading verdwijnt niet, ze verschuift.", 5),
                 ("open", r"Bol A draagt \(+9\ \text{nC}\). Je raakt er de even grote neutrale bol B mee aan en scheidt ze weer. Daarna raak je met B de even grote neutrale bol C aan. Welke lading draagt elke bol op het einde?",
                  r"Na het eerste contact: A en B elk \(+4{,}5\ \text{nC}\). Na het tweede: B en C elk "
                  r"\(+2{,}25\ \text{nC}\), terwijl A op \(+4{,}5\ \text{nC}\) blijft. De som is nog altijd "
                  r"\(4{,}5+2{,}25+2{,}25=+9\ \text{nC}\), en dat is een goede controle.", 7),
                 ("tabel", ["Stap", r"\(Q_{A}\)", r"\(Q_{B}\)"],
                  [["in het begin", r"\(+12\ \text{nC}\)", r"\(0\)"],
                   ["na één contact", None, None],
                   ["na een tweede contact", None, None]],
                  r"na één contact elk \(+6\ \text{nC}\); een tweede contact verandert niets meer, "
                  r"want ze dragen dan al evenveel", "150px"),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij het wrijven van twee stoffen ontstaat er nieuwe lading.", False),
                 ("waar", "Alle lading van een geladen geleider zit op het buitenoppervlak.", True),
                 ("waar", "Bij influentie moet het geladen voorwerp het andere aanraken.", False),
                 ("waar", "Een geladen ballon trekt een neutraal papiertje aan.", True),
                 ("waar", r"Een neutraal voorwerp bevat helemaal geen lading.", False),
             ]),
        dict(kop="Influentie stap voor stap",
             opdracht="Vul in welk teken de bol draagt na elke stap.",
             oefeningen=[
                 ("tabel", ["Stap", "Teken van de bol in totaal"],
                  [["de neutrale bol staat alleen", None],
                   ["je houdt er een negatieve staaf bij", None],
                   ["je aardt de bol, de staaf blijft erbij", None],
                   ["je haalt de aarding weg, dan de staaf", None]],
                  r"neutraal; nog altijd neutraal, de lading is enkel verschoven; positief, want de "
                  r"weggeduwde elektronen lopen naar de aarde; positief, nu gelijkmatig verdeeld", "210px"),
                 ("open", "Leg uit waarom laden door influentie het tegengestelde teken geeft en laden door contact hetzelfde teken.",
                  "Bij contact vloeit er lading van het geladen voorwerp naar het andere, dus dragen ze "
                  "achteraf dezelfde soort. Bij influentie met aarding duwt de staaf de gelijknamige "
                  "lading weg naar de aarde; wat achterblijft is de tegengestelde soort.", 6),
                 ("kies", "Je brengt een negatieve staaf bij een elektroscoop zonder ze aan te raken. Wat zie je?",
                  ["de blaadjes blijven samen, want de bol blijft neutraal",
                   "de blaadjes wijken uit, en vallen weer samen als je de staaf weghaalt",
                   "de blaadjes wijken uit en blijven zo staan",
                   "de blaadjes bewegen alleen als je de staaf aanraakt"], 1),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je wrijft een ballon op je trui en houdt hem tegen de muur. Hij blijft hangen. Leg uit in twee stappen.",
                  "Eerst: door het wrijven gaan er elektronen van de trui naar de ballon, dus wordt "
                  "de ballon negatief geladen. Dan: die lading polariseert de moleculen in de muur, "
                  "de dichtste kant wordt lichtpositief, en de aantrekking houdt de ballon vast.", 7),
                 ("open", "Waarom raak je bij het uitstappen uit een auto soms een schokje op?",
                  "Door de wrijving van je kleren op de zetel raak je geladen. Zodra je het metalen "
                  "koetswerk aanraakt, kan die lading in één keer wegvloeien, en dat voel je als een "
                  "schokje.", 5),
                 ("open", "Waarom zet men een brandstoftank aan de aarde voor men hem vult?",
                  "Het stromen van de brandstof laadt de tank op. Een aardverbinding laat die lading "
                  "wegvloeien, zodat er geen vonk kan overslaan bij de dampen.", 5),
                 ("open", "Een elektroscoop staat op een vochtige dag na een halve minuut weer met gesloten blaadjes. Leg uit waarom, en wat je eraan kan doen.",
                  "Waterdamp in de lucht geleidt, dus lekt de lading langzaam weg naar de omgeving en "
                  "vallen de blaadjes samen. In een droge ruimte, of met een droger toestel onder de "
                  "stolp, blijft de lading veel langer staan.", 6),
             ]),
    ],
)
# ============================================================
OEFENBUNDELS["oefenbundel-de-wet-van-coulomb-en-het-elektrisch-veld-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De wet van Coulomb en het elektrisch veld",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeveel keer groter of kleiner",
             opdracht=r"De kracht was \(12\ \text{N}\). Schrijf de nieuwe kracht.",
             oefeningen=[
                 ("rij", [(r"\(r\) wordt \(2r\)", r"\(3\ \text{N}\)"),
                          (r"\(r\) wordt \(\tfrac{r}{2}\)", r"\(48\ \text{N}\)"),
                          (r"\(r\) wordt \(3r\)", r"\(1{,}3\ \text{N}\)")],
                  "Welke kracht nu?", WW),
                 ("rij", [(r"\(q_{1}\) wordt \(2q_{1}\)", r"\(24\ \text{N}\)"),
                          ("beide ladingen verdubbelen", r"\(48\ \text{N}\)"),
                          (r"\(q_{1}\) wordt \(\tfrac{q_{1}}{3}\)", r"\(4\ \text{N}\)")],
                  "Welke kracht nu?", WW),
                 ("open", r"Leg uit waarom \(r\) halveren de kracht vier keer zo groot maakt.",
                  r"\(r\) staat in het kwadraat in de noemer: halveren geeft "
                  r"\(\left(\tfrac{r}{2}\right)^{2}=\tfrac{r^{2}}{4}\), dus maal vier.", 5),
             ]),
        dict(kop="Rekenen met de wet van Coulomb",
             opdracht=r"Neem \(k=8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\). Schrijf eerst de formule op, zet de ladingen in coulomb en kwadrateer \(r\).",
             oefeningen=[
                 ("open", r"Bereken \(F\) tussen \(q_{1}=4{,}0\ \mu\text{C}\) en \(q_{2}=-6{,}0\ \mu\text{C}\) "
                  r"op \(r=0{,}20\ \text{m}\). Trekken ze aan of stoten ze af?",
                  r"Invullen geeft \[F=8{,}99\cdot 10^{9}\cdot"
                  r"\dfrac{4{,}0\cdot 10^{-6}\cdot 6{,}0\cdot 10^{-6}}{0{,}20^{2}}\approx 5{,}4\ \text{N}\] "
                  r"De ladingen zijn ongelijknamig, dus trekken ze elkaar aan.", 5),
                 ("open", r"Twee even grote ladingen \(q\) op \(r=0{,}50\ \text{m}\) stoten elkaar af met "
                  r"\(F=9{,}0\cdot 10^{-3}\ \text{N}\). Hoe groot is \(q\)?",
                  r"Vorm om: \[q^{2}=\dfrac{F\cdot r^{2}}{k}=\dfrac{9{,}0\cdot 10^{-3}\cdot 0{,}25}"
                  r"{8{,}99\cdot 10^{9}}\approx 2{,}50\cdot 10^{-13}\] Dus "
                  r"\(q\approx 5{,}0\cdot 10^{-7}\ \text{C}=0{,}50\ \mu\text{C}\). Ze stoten af, dus zijn "
                  r"ze gelijknamig; het teken zelf volgt hier niet uit.", 5),
                 ("open", r"Op \(r=0{,}30\ \text{m}\) van \(q=-2{,}0\ \mu\text{C}\): bereken \(E\) en zeg welke kant "
                  r"\(\vec{E}\) op wijst.",
                  r"Met \(E=k\dfrac{|q|}{r^{2}}\): \[E=8{,}99\cdot 10^{9}\cdot"
                  r"\dfrac{2{,}0\cdot 10^{-6}}{0{,}090}\approx 2{,}0\cdot 10^{5}\ \text{N/C}\] "
                  r"De lading is negatief, dus \(\vec{E}\) wijst naar de lading toe.", 5),
             ]),
        dict(kop="Twee ladingen tegelijk",
             opdracht="Teken eerst de twee krachtpijlen, en reken dan pas.",
             oefeningen=[
                 ("open", r"\(q_{1}=+3{,}0\ \mu\text{C}\) staat in \(x=0\) en \(q_{2}=+3{,}0\ \mu\text{C}\) in "
                  r"\(x=0{,}40\ \text{m}\). Bereken de resulterende kracht op \(q_{3}=+1{,}0\ \mu\text{C}\) in "
                  r"\(x=0{,}10\ \text{m}\).",
                  r"Van \(q_{1}\), op \(0{,}10\ \text{m}\): \(F_{1}=8{,}99\cdot 10^{9}\cdot"
                  r"\dfrac{3{,}0\cdot 10^{-12}}{0{,}010}\approx 2{,}70\ \text{N}\) naar rechts. "
                  r"Van \(q_{2}\), op \(0{,}30\ \text{m}\): \(F_{2}\approx 0{,}30\ \text{N}\) naar links. "
                  r"Ze liggen op één lijn, dus \(F=2{,}70-0{,}30\approx 2{,}4\ \text{N}\) naar rechts.", 8),
                 ("open", r"Twee positieve ladingen \(q\) en \(4q\) staan op afstand \(d\). Op welke plaats tussen "
                  r"de twee is \(E=0\)? Reken het uit in functie van \(d\).",
                  r"Noem \(x\) de afstand tot \(q\). Dan is "
                  r"\(k\dfrac{q}{x^{2}}=k\dfrac{4q}{(d-x)^{2}}\), dus \((d-x)^{2}=4x^{2}\) en \(d-x=2x\). "
                  r"Daaruit volgt \(x=\tfrac{d}{3}\), dus dicht bij de kleinste lading.", 8),
                 ("kies", r"Twee ladingen staan in twee hoekpunten van een vierkant. Waarom tel je de krachten op een derde lading niet gewoon op?",
                  [r"omdat \(\vec{F}_{1}\) en \(\vec{F}_{2}\) een andere richting hebben",
                   "omdat de twee krachten altijd even groot zijn",
                   "omdat de afstand tot beide ladingen dezelfde is",
                   "omdat ladingen in een vierkant niet op elkaar inwerken"], 0),
             ]),
        dict(kop="De veldsterkte",
             opdracht=r"Reken uit met \(E=\dfrac{F}{q}\).",
             oefeningen=[
                 ("kort", r"\(E=400\ \text{N/C}\). Welke kracht werkt op \(q=2\ \text{mC}\)?",
                  r"\(F=400\cdot 2\cdot 10^{-3}=0{,}8\ \text{N}\)", WW),
                 ("kort", r"Op \(q=4\ \mu\text{C}\) werkt \(F=0{,}2\ \text{N}\). Hoe groot is \(E\)?",
                  r"\(E=\dfrac{0{,}2}{4\cdot 10^{-6}}=5{,}0\cdot 10^{4}\ \text{N/C}\)", WW),
                 ("kort", r"In welke eenheid staat \(E\)? Geef beide schrijfwijzen.",
                  r"\(\text{N/C}\), en dat is hetzelfde als \(\text{V/m}\)", WW),
             ]),
        dict(kop="Veldlijnen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("rond één positieve puntlading", "een radiaal veld"),
                          ("tussen twee geladen platen", "een homogeen veld"),
                          ("tussen een positieve en een negatieve lading", "een dipoolveld")],
                  "Welk patroon?", WL),
                 ("waar", "Veldlijnen kunnen elkaar snijden als de ladingen groot genoeg zijn.", False),
                 ("waar", "Veldlijnen lopen van de positieve naar de negatieve lading.", True),
                 ("waar", "Dicht bij elkaar liggende veldlijnen betekenen een sterk veld.", True),
                 ("waar", r"In een homogeen veld is \(F\) op een gegeven lading overal even groot.", True),
                 ("waar", r"Binnen in een geladen holle geleider geldt \(E=0\).", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom is een vliegtuig een veilige plaats bij bliksem?",
                  r"Het metalen omhulsel werkt als een kooi van Faraday: de lading blijft aan de "
                  r"buitenkant en binnenin is \(E=0\).", 5),
                 ("open", "Drie gelijke positieve ladingen staan op één rechte, op gelijke afstand. Welke kracht voelt de middelste? Leg uit.",
                  r"Geen enkele, \(\vec{F}=\vec{0}\): de twee buitenste trekken even hard en in "
                  r"tegengestelde zin.", 5),
                 ("open", "De wet van Coulomb en de gravitatiewet lijken sterk op elkaar. Noem één gelijkenis en één verschil.",
                  r"Gelijkenis: \(F=k\,\dfrac{|q_{1}q_{2}|}{r^{2}}\) en \(F=G\,\dfrac{m_{1}m_{2}}{r^{2}}\) "
                  r"hebben allebei \(r^{2}\) onder. Verschil: gravitatie trekt altijd aan, de "
                  r"coulombkracht kan ook afstoten.", 5),
                 ("open", r"Een leerling berekent \(F\) tussen twee ladingen van \(3\ \mu\text{C}\) op "
                  r"\(20\ \text{cm}\) en krijgt \(4{,}0\cdot 10^{-3}\ \text{N}\). Zoek zijn twee fouten.",
                  r"Hij rekende in cm in plaats van in m, en kwadrateerde \(r\) niet: "
                  r"\(F\approx 2{,}0\ \text{N}\).", 5),
             ]),
    ],
)
# ============================================================
OEFENBUNDELS["oefenbundel-elektrische-energie-potentiaal-en-spanning-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrische energie, potentiaal en spanning",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Symbolen en eenheden",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["grootheid", "symbool", "eenheid"],
                  [["arbeid of energie", None, None], ["lading", None, None],
                   ["spanning", None, None], ["potentiaal", None, None],
                   ["veldsterkte", None, None]],
                  r"arbeid of energie: \(W\) of \(E\), \(\text{J}\) · lading: \(q\), \(\text{C}\) · "
                  r"spanning: \(U\), \(\text{V}\) · potentiaal: \(V\), \(\text{V}\) · "
                  r"veldsterkte: \(E\), \(\text{N/C}\)", WW),
             ]),
        dict(kop=r"Rekenen met \(W=q\,U\)",
             opdracht=r"Schrijf eerst de formule op en zet elke lading in coulomb.",
             oefeningen=[
                 ("kort", r"Een lading van \(3{,}0\ \text{C}\) doorloopt \(12\ \text{V}\). Welke energie komt vrij?",
                  r"\(W=q\,U=3{,}0\cdot 12=36\ \text{J}\).", W),
                 ("kort", r"Over \(9{,}0\ \text{V}\) komt \(45\ \text{J}\) vrij. Welke lading is gepasseerd?",
                  r"\(q=\dfrac{W}{U}=\dfrac{45}{9{,}0}=5{,}0\ \text{C}\).", W),
                 ("kort", r"Een lading van \(0{,}50\ \text{C}\) geeft \(110\ \text{J}\) af. Over welke spanning ging ze?",
                  r"\(U=\dfrac{W}{q}=\dfrac{110}{0{,}50}=220\ \text{V}\).", W),
                 ("kort", r"Een lading van \(250\ \mu\text{C}\) doorloopt \(400\ \text{V}\). Hoeveel energie wint ze?",
                  r"\(W=250\cdot 10^{-6}\cdot 400=0{,}10\ \text{J}\).", W),
                 ("kort", r"Een lading van \(2{,}0\ \text{mC}\) zit in een punt met \(V=75\ \text{V}\). Hoe groot is \(E_{p}\)?",
                  r"\(E_{p}=q\,V=2{,}0\cdot 10^{-3}\cdot 75=0{,}15\ \text{J}\).", W),
             ]),
        dict(kop="Potentiaal, spanning en veld",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"de energie per eenheid van lading in een punt", "de potentiaal"),
                          (r"het verschil in potentiaal tussen twee punten", "de spanning"),
                          (r"de kracht per eenheid van lading in een punt", "de veldsterkte")],
                  "Hoe heet dat?", WL),
                 ("kort", r"\(V_{A}=80\ \text{V}\) en \(V_{B}=-20\ \text{V}\). Hoe groot is \(U_{AB}\)?",
                  r"\(U_{AB}=80-(-20)=100\ \text{V}\).", W),
                 ("kort", r"Twee platen staan \(5{,}0\ \text{cm}\) uit elkaar, met \(U=250\ \text{V}\). Hoe groot is \(E\)?",
                  r"\(E=\dfrac{U}{d}=\dfrac{250}{0{,}050}=5{,}0\cdot 10^{3}\ \text{V/m}\).", W),
                 ("waar", r"Een spanning hoort bij twee punten, een potentiaal bij één punt.", True),
                 ("waar", r"Een positieve lading beweegt vanzelf van lage naar hoge potentiaal.", False),
                 ("waar", r"Het nulpunt van \(V\) kies je zelf, bijvoorbeeld de aarde.", True),
                 ("waar", r"\(V\) in een punt wordt groter als je er een grotere proeflading in zet.", False),
             ]),
        dict(kop="Snelheid uit een spanning",
             opdracht=r"Gebruik \(q\,U=\tfrac{1}{2}m\,v^{2}\). Neem \(e=1{,}602\cdot 10^{-19}\ \text{C}\), "
                      r"\(m_{e}=9{,}11\cdot 10^{-31}\ \text{kg}\) en \(m_{p}=1{,}67\cdot 10^{-27}\ \text{kg}\).",
             oefeningen=[
                 ("open", r"Een elektron vertrekt uit rust en doorloopt \(250\ \text{V}\). Bereken \(v\).",
                  r"\(v=\sqrt{\dfrac{2\cdot 1{,}602\cdot 10^{-19}\cdot 250}{9{,}11\cdot 10^{-31}}}"
                  r"\approx 9{,}4\cdot 10^{6}\ \text{m/s}\).", 5),
                 ("open", r"Een proton doorloopt dezelfde \(250\ \text{V}\). Bereken \(v\) en vergelijk.",
                  r"\(v\approx 2{,}2\cdot 10^{5}\ \text{m/s}\): ruim \(42\) keer trager, want "
                  r"\(\sqrt{m_{p}/m_{e}}\approx 42\). De energie is wel even groot.", 5),
                 ("open", r"Een alfadeeltje \((q=2e,\ m=6{,}64\cdot 10^{-27}\ \text{kg})\) doorloopt "
                  r"\(1{,}0\ \text{kV}\). Hoeveel energie wint het, in \(\text{eV}\) en in \(\text{J}\)?",
                  r"\(2000\ \text{eV}\), want \(q=2e\). In joule: "
                  r"\(2000\cdot 1{,}602\cdot 10^{-19}=3{,}2\cdot 10^{-16}\ \text{J}\).", 5),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Teken of schrijf eerst op wat je weet, en reken dan pas.",
             oefeningen=[
                 ("open", r"Twee platen staan \(4{,}0\ \text{cm}\) uit elkaar met \(U=200\ \text{V}\). "
                  r"Bereken \(E\), en daarna de kracht op een elektron ertussen.",
                  r"\(E=\dfrac{200}{0{,}040}=5{,}0\cdot 10^{3}\ \text{V/m}\), en daarmee "
                  r"\(F=E\,q\approx 8{,}0\cdot 10^{-16}\ \text{N}\).", 6),
                 ("open", r"Een lading \(q_{1}=+2{,}0\ \text{nC}\) staat in \(x=0\) en \(q_{2}=-2{,}0\ \text{nC}\) "
                  r"in \(x=0{,}20\ \text{m}\). Hoe groot is \(V\) in het midden?",
                  r"Potentiaal telt als gewoon getal op, met teken. Beide liggen op \(0{,}10\ \text{m}\), "
                  r"dus \(V=k\dfrac{+2{,}0\cdot 10^{-9}}{0{,}10}+k\dfrac{-2{,}0\cdot 10^{-9}}{0{,}10}=0\). "
                  r"Het veld is daar wel niet nul.", 6),
                 ("open", r"Een stofdeeltje met \(m=3{,}0\cdot 10^{-15}\ \text{kg}\) zweeft stil tussen twee "
                  r"horizontale platen op \(2{,}0\ \text{cm}\) met \(U=600\ \text{V}\). Hoe groot is zijn lading?",
                  r"Stil zweven betekent \(E\,q=m\,g\). Met \(E=\dfrac{600}{0{,}020}=3{,}0\cdot 10^{4}\ \text{V/m}\) "
                  r"volgt \(q=\dfrac{3{,}0\cdot 10^{-15}\cdot 9{,}81}{3{,}0\cdot 10^{4}}\approx "
                  r"9{,}8\cdot 10^{-19}\ \text{C}\), ongeveer zes elementaire ladingen.", 6),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom kost het geen arbeid om een lading langs een equipotentiaallijn te verplaatsen?",
                  r"\(V\) verandert niet, dus \(E_{p}=q\,V\) ook niet, dus \(W=0\). De verplaatsing staat "
                  r"daar ook loodrecht op de kracht.", 5),
                 ("open", "Waarom is een vogel op een hoogspanningsdraad niet in gevaar?",
                  r"Zijn twee pootjes zitten op bijna hetzelfde punt van de draad, dus \(U\) ertussen is "
                  r"bijna nul. Zonder spanningsverschil loopt er geen stroom door hem.", 5),
                 ("open", "Waarom vervoert men elektriciteit over grote afstand bij een heel hoge spanning?",
                  r"Bij een hoge \(U\) volstaat een kleine \(I\) voor hetzelfde vermogen, en de verliezen "
                  r"in de kabels gaan met \(I^{2}\).", 5),
                 ("open", r"Een leerling zegt: waar \(V=0\) is, is ook \(E=0\). Waarom klopt dat niet?",
                  r"Midden tussen twee tegengestelde ladingen is \(V=0\) maar wijzen beide velden dezelfde "
                  r"kant op, dus is \(E\) daar juist het grootst. \(V\) is een getal, \(E\) een vector.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektrodynamica-stroom-weerstand-en-schakelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrodynamica: stroom, weerstand en schakelingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop=r"De wet van Ohm",
             opdracht=r"Vul aan met \(U=R\,I\).",
             oefeningen=[
                 ("rij", [(r"\(U=12\ \text{V}\), \(R=4{,}0\ \Omega\)", r"\(I=3{,}0\ \text{A}\)"),
                          (r"\(U=9{,}0\ \text{V}\), \(I=0{,}30\ \text{A}\)", r"\(R=30\ \Omega\)"),
                          (r"\(R=220\ \Omega\), \(I=0{,}050\ \text{A}\)", r"\(U=11\ \text{V}\)")],
                  "Wat ontbreekt?", WW),
                 ("rij", [(r"\(U=230\ \text{V}\), \(R=46\ \Omega\)", r"\(I=5{,}0\ \text{A}\)"),
                          (r"\(U=1{,}5\ \text{V}\), \(I=0{,}25\ \text{A}\)", r"\(R=6{,}0\ \Omega\)"),
                          (r"\(R=100\ \Omega\), \(I=0{,}12\ \text{A}\)", r"\(U=12\ \text{V}\)")],
                  "Wat ontbreekt?", WW),
                 ("kort", r"Door een draad gaat \(60\ \text{C}\) in \(20\ \text{s}\). Hoe groot is \(I\)?",
                  r"\(I=\dfrac{\Delta q}{\Delta t}=\dfrac{60}{20}=3{,}0\ \text{A}\).", W),
                 ("kort", r"Hoeveel lading passeert er in \(5{,}0\ \text{min}\) bij \(I=0{,}40\ \text{A}\)?",
                  r"\(\Delta q=I\,\Delta t=0{,}40\cdot 300=120\ \text{C}\).", W),
             ]),
        dict(kop=r"Vervangingsweerstand",
             opdracht=r"Reken \(R_{v}\) uit. Schrijf erbij of het serie of parallel is.",
             oefeningen=[
                 ("kort", r"\(6{,}0\ \Omega\) en \(12\ \Omega\) in serie.",
                  r"\(R_{v}=6{,}0+12=18\ \Omega\).", W),
                 ("kort", r"Diezelfde twee in parallel.",
                  r"\(R_{v}=\dfrac{6{,}0\cdot 12}{18}=4{,}0\ \Omega\).", W),
                 ("kort", r"Drie weerstanden van elk \(30\ \Omega\) in parallel.",
                  r"\(R_{v}=\dfrac{30}{3}=10\ \Omega\).", W),
                 ("kort", r"\(R_{v}=8{,}0\ \Omega\) en \(R_{1}=24\ \Omega\) staan parallel. Hoe groot is \(R_{2}\)?",
                  r"\(\dfrac{1}{R_{2}}=\dfrac{1}{8{,}0}-\dfrac{1}{24}=\dfrac{2}{24}\), dus "
                  r"\(R_{2}=12\ \Omega\).", W),
                 ("open", r"Leg uit waarom \(R_{v}\) bij parallel altijd kleiner is dan de kleinste weerstand.",
                  r"Elke extra tak geeft de stroom een extra weg, dus loopt er bij dezelfde \(U\) in "
                  r"totaal meer stroom. Meer \(I\) bij dezelfde \(U\) betekent een kleinere \(R\).", 5),
             ]),
        dict(kop="Serie of parallel",
             opdracht="Schrijf serie of parallel.",
             oefeningen=[
                 ("rij", [(r"\(I\) is overal dezelfde", "serie"),
                          (r"\(U\) is over elke tak dezelfde", "parallel"),
                          (r"\(R_{v}=R_{1}+R_{2}\)", "serie")],
                  "Serie of parallel?", WW),
                 ("rij", [(r"de stromen van de takken tellen op", "parallel"),
                          ("één lamp stuk en alles valt uit", "serie"),
                          ("één lamp stuk en de rest blijft branden", "parallel")],
                  "Serie of parallel?", WW),
             ]),
        dict(kop="Een schakeling doorrekenen",
             opdracht="Reken stap voor stap en controleer je antwoord op het einde.",
             oefeningen=[
                 ("open", r"\(4{,}0\ \Omega\), \(6{,}0\ \Omega\) en \(10\ \Omega\) staan in serie op "
                  r"\(40\ \text{V}\). Bereken \(I\) en de drie deelspanningen.",
                  r"\(R_{v}=20\ \Omega\), dus \(I=2{,}0\ \text{A}\). De deelspanningen zijn "
                  r"\(8{,}0\), \(12\) en \(20\ \text{V}\), samen weer \(40\ \text{V}\).", 6),
                 ("open", r"\(20\ \Omega\) en \(30\ \Omega\) staan parallel op \(60\ \text{V}\). Bereken "
                  r"beide takstromen, de hoofdstroom en \(R_{v}\).",
                  r"\(I_{1}=3{,}0\ \text{A}\) en \(I_{2}=2{,}0\ \text{A}\), samen \(5{,}0\ \text{A}\). "
                  r"\(R_{v}=\dfrac{60}{5{,}0}=12\ \Omega\), wat klopt met \(\dfrac{20\cdot 30}{50}\).", 6),
                 ("open", r"\(5{,}0\ \Omega\) staat in serie met twee parallelle weerstanden van "
                  r"\(12\ \Omega\) en \(24\ \Omega\), op \(30\ \text{V}\). Bereken \(R_{v}\), \(I\) en de "
                  r"spanning over het parallelle stuk.",
                  r"\(R_{\text{par}}=\dfrac{12\cdot 24}{36}=8{,}0\ \Omega\), dus \(R_{v}=13\ \Omega\) en "
                  r"\(I\approx 2{,}3\ \text{A}\). Over het parallelle stuk staat "
                  r"\(8{,}0\cdot 2{,}3\approx 18{,}5\ \text{V}\).", 7),
             ]),
        dict(kop=r"Vermogen en energie",
             opdracht=r"Reken uit met \(P=U\,I\).",
             oefeningen=[
                 ("kort", r"Een toestel op \(230\ \text{V}\) trekt \(2{,}0\ \text{A}\). Welk vermogen?",
                  r"\(P=230\cdot 2{,}0=460\ \text{W}\).", W),
                 ("kort", r"Een lamp van \(60\ \text{W}\) hangt op \(230\ \text{V}\). Welke stroom?",
                  r"\(I=\dfrac{60}{230}\approx 0{,}26\ \text{A}\).", W),
                 ("kort", r"Een toestel van \(1500\ \text{W}\) draait \(2{,}0\ \text{h}\). Hoeveel kWh?",
                  r"\(E=1{,}5\cdot 2{,}0=3{,}0\ \text{kWh}\).", W),
                 ("kort", r"Door een weerstand van \(15\ \Omega\) loopt \(2{,}0\ \text{A}\). Hoeveel warmte per seconde?",
                  r"\(P=R\,I^{2}=15\cdot 4{,}0=60\ \text{W}\), dus \(60\ \text{J}\) per seconde.", W),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom worden de lampjes van een oude kerstslinger zwakker als je er een bijsteekt?",
                  r"Ze staan in serie. Een lampje erbij maakt \(R_{v}\) groter, dus daalt \(I\), en "
                  r"moet de bronspanning over meer lampjes verdeeld worden.", 5),
                 ("open", "Waarom staan de stopcontacten in een huis parallel en niet in serie?",
                  r"Zo staat op elk stopcontact dezelfde \(230\ \text{V}\), en blijft de rest werken "
                  r"als één toestel uitvalt.", 5),
                 ("open", r"Waarom neemt men voor een grote stroom een dikkere kabel?",
                  r"De warmte is \(P=R\,I^{2}\), en \(R=\rho\dfrac{\ell}{A}\). Een grotere doorsnede "
                  r"\(A\) geeft een kleinere \(R\), dus minder warmte bij dezelfde stroom.", 5),
                 ("open", r"Waarom heeft een ampèremeter een heel kleine en een voltmeter een heel grote eigen weerstand?",
                  r"De ampèremeter staat in serie, dus telt zijn \(R\) bij die van de kring en zou hij "
                  r"de stroom verkleinen. De voltmeter staat parallel, dus zou een kleine \(R\) stroom "
                  r"wegtrekken bij het onderdeel.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-magneten-en-het-magnetisch-veld-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Magneten en het magnetisch veld",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Polen en stoffen",
             opdracht="Vul de twee rijtjes aan.",
             oefeningen=[
                 ("rij", [("noordpool bij noordpool", "afstoten"),
                          ("noordpool bij zuidpool", "aantrekken"),
                          ("zuidpool bij zuidpool", "afstoten")],
                  "Aantrekken of afstoten?", WW),
                 ("rij", [("twee spoelen, noordpool naar noordpool", "afstoten"),
                          ("de noordpool van een kompasnaald bij de zuidpool van een magneet", "aantrekken")],
                  "Aantrekken of afstoten?", WW),
                 ("rij", [("ijzer", "ja"), ("koper", "nee"), ("nikkel", "ja")],
                  "Trekt een magneet het aan?", WW),
                 ("rij", [("aluminium", "nee"), ("kobalt", "ja"), ("glas", "nee")],
                  "Trekt een magneet het aan?", WW),
             ]),
        dict(kop="Eenheden en begrippen",
             opdracht=r"Zet om en antwoord kort. Eén tesla is \(10^{4}\) gauss.",
             oefeningen=[
                 ("rij", [(r"\(5{,}0\ \text{mT}\) in tesla", r"\(5{,}0\cdot 10^{-3}\ \text{T}\)"),
                          (r"\(5\cdot 10^{-5}\ \text{T}\) in microtesla", r"\(50\ \mu\text{T}\)")],
                  "Zet om.", WL),
                 ("rij", [(r"\(0{,}25\ \text{T}\) in millitesla", r"\(250\ \text{mT}\)"),
                          (r"\(1{,}5\ \text{T}\) in gauss", r"\(1{,}5\cdot 10^{4}\ \text{G}\)")],
                  "Zet om.", WL),
                 ("rij", [("de gebiedjes waarin de elementaire magneetjes gelijk staan", "weissgebieden"),
                          ("de eenheid van magnetische inductie", "tesla")],
                  "Hoe heet dat?", WL),
                 ("rij", [("de regel voor de zin van het veld van een stroomdraad", "de rechterhandregel"),
                          ("het aantal veldlijnen door een oppervlak", "de flux")],
                  "Hoe heet dat?", WL),
                 ("rij", [(r"het symbool \(\mu_{0}\)", "de permeabiliteit van het vacuüm"),
                          ("de temperatuur waarboven ijzer niet magnetisch blijft", "de curietemperatuur")],
                  "Hoe heet dat?", WL),
             ]),
        dict(kop="Het veld van een rechte draad",
             opdracht=r"Gebruik \(B = \dfrac{\mu_{0}I}{2\pi r}\) met "
                      r"\(\mu_{0} = 4\pi\cdot 10^{-7}\ \text{T}\cdot\text{m/A}\). "
                      r"Je mag rekenen met \(\dfrac{\mu_{0}}{2\pi} = 2\cdot 10^{-7}\).",
             oefeningen=[
                 ("kort", r"Door een rechte draad loopt \(I = 5{,}0\ \text{A}\). Hoe groot is "
                          r"\(B\) op \(r = 0{,}10\ \text{m}\) van de draad?",
                  r"\(B = 2\cdot 10^{-7}\cdot\dfrac{5{,}0}{0{,}10} = 1{,}0\cdot 10^{-5}\ \text{T}\)", W),
                 ("kort", r"Zelfde draad, maar \(I = 10\ \text{A}\) en \(r = 0{,}050\ \text{m}\). "
                          r"Hoe groot is \(B\)?",
                  r"\(B = 2\cdot 10^{-7}\cdot\dfrac{10}{0{,}050} = 4{,}0\cdot 10^{-5}\ \text{T}\)", W),
                 ("kort", r"Op \(2{,}0\ \text{cm}\) van een draad meet je "
                          r"\(B = 1{,}0\cdot 10^{-4}\ \text{T}\). Welke stroom loopt erdoor?",
                  r"\(I = \dfrac{B\,r}{2\cdot 10^{-7}} = 10\ \text{A}\)", W),
                 ("kort", r"Een hoogspanningsdraad voert \(100\ \text{A}\). Op welke afstand is "
                          r"zijn veld even sterk als dat van de aarde, \(5{,}0\cdot 10^{-5}\ \text{T}\)?",
                  r"\(r = \dfrac{2\cdot 10^{-7}\cdot 100}{5{,}0\cdot 10^{-5}} = 0{,}40\ \text{m}\)", W),
                 ("rij", [(r"de stroom maal 3, de afstand gelijk", r"\(B\) maal 3"),
                          (r"de afstand maal 4, de stroom gelijk", r"\(B\) gedeeld door 4")],
                  r"Wat gebeurt er met \(B\)?", WL),
                 ("rij", [(r"de stroom maal 2 en de afstand maal 2", r"\(B\) blijft gelijk"),
                          (r"de stroom maal 6 en de afstand maal 2", r"\(B\) maal 3")],
                  r"Wat gebeurt er met \(B\)?", WL),
                 ("open", r"Een draad geeft op \(0{,}10\ \text{m}\) een veld van "
                          r"\(8{,}0\ \mu\text{T}\). Je verdrievoudigt de stroom en gaat tegelijk "
                          r"op \(0{,}60\ \text{m}\) staan. Hoe groot is \(B\) dan? Reken met de "
                          r"verhouding, niet met de formule.",
                  r"\(B \sim \dfrac{I}{r}\): de stroom maal 3 geeft maal 3, de afstand maal 6 "
                  r"geeft gedeeld door 6, samen maal \(\tfrac{1}{2}\). Dus "
                  r"\(B = 4{,}0\ \mu\text{T}\).", 5),
             ]),
        dict(kop="Het veld in een spoel",
             opdracht=r"Gebruik \(B = \mu_{0}\dfrac{N}{\ell}I\) met "
                      r"\(\mu_{0} = 4\pi\cdot 10^{-7}\ \text{T}\cdot\text{m/A}\).",
             oefeningen=[
                 ("kort", r"Een spoel van \(0{,}25\ \text{m}\) heeft \(500\) windingen en voert "
                          r"\(2{,}0\ \text{A}\). Hoe groot is \(B\) binnenin?",
                  r"\(N/\ell = 2000\ \text{m}^{-1}\), dus "
                  r"\(B = 5{,}0\cdot 10^{-3}\ \text{T}\)", W),
                 ("kort", r"Een spoel van \(0{,}40\ \text{m}\) met \(200\) windingen voert "
                          r"\(1{,}5\ \text{A}\). Hoe groot is \(B\)?",
                  r"\(N/\ell = 500\ \text{m}^{-1}\), dus "
                  r"\(B = 9{,}4\cdot 10^{-4}\ \text{T}\)", W),
                 ("kort", r"Welke stroom heb je nodig voor \(B = 20\ \text{mT}\) in een spoel "
                          r"van \(0{,}50\ \text{m}\) met \(1000\) windingen?",
                  r"\(I = \dfrac{B}{\mu_{0}\,N/\ell} = 8{,}0\ \text{A}\)", W),
                 ("kort", r"Hoeveel windingen per meter heb je nodig voor \(B = 10\ \text{mT}\) "
                          r"bij \(I = 4{,}0\ \text{A}\)?",
                  r"\(N/\ell = B/(\mu_{0}I) = 2{,}0\cdot 10^{3}\) per meter", W),
                 ("open", r"Twee spoelen voeren dezelfde stroom. De eerste heeft \(300\) "
                          r"windingen over \(0{,}30\ \text{m}\), de tweede \(300\) windingen over "
                          r"\(0{,}15\ \text{m}\). Welke maakt het sterkste veld, en hoeveel keer?",
                  r"Enkel \(N/\ell\) verschilt: \(1000\) tegen \(2000\) windingen per meter. De "
                  r"tweede maakt dus een twee keer zo sterk veld.", 5),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een magneet in twee breken geeft een losse noordpool en een losse zuidpool.", False),
                 ("waar", "De magnetische veldlijnen lopen buiten de magneet van noord naar zuid.", True),
                 ("waar", "De geografische noordpool van de aarde ligt bij de magnetische zuidpool.", True),
                 ("waar", "Een rechte stroomdraad maakt rechte veldlijnen langs de draad.", False),
                 ("waar", "Een spoel met stroom gedraagt zich als een staafmagneet.", True),
                 ("waar", r"Het veld van een rechte draad daalt met het kwadraat van de afstand.", False),
                 ("waar", r"In de formule voor het veld in een spoel staat geen afstand tot de as.", True),
                 ("waar", r"Eén tesla is een kleine eenheid: een koelkastmagneet zit rond \(1\ \text{T}\).", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom je een stuk ijzer kan magnetiseren en een stuk koper niet.",
                  "In ijzer zitten weissgebieden met elementaire magneetjes die je in dezelfde "
                  "richting kan zetten. Koper heeft die gebiedjes niet, dus valt er niets te "
                  "richten.", 5),
                 ("open", "Een kompasnaald wijst naar het noorden. Hoe komt dat, en wat gebeurt er met een magneet in de buurt?",
                  "De aarde heeft zelf een magnetisch veld, en de naald draait zich in dat veld. Een "
                  "magneet dichtbij maakt een veel sterker veld ter plaatse, dus wijst de naald dan "
                  "naar de magneet.", 5),
                 ("open", "Hoe maak je het veld van een elektromagneet sterker? Noem drie manieren.",
                  "Meer stroom door de spoel, meer wikkelingen per meter, en een kern van zacht "
                  "ijzer in de spoel.", 5),
                 ("open", r"Het veld van een puntlading gaat met \(\dfrac{1}{r^{2}}\), dat van een "
                          r"rechte stroomdraad met \(\dfrac{1}{r}\). Leg uit waarom dat niet "
                          r"dezelfde macht is.",
                  r"Een puntlading straalt in alle richtingen van de ruimte uit, dus spreidt haar "
                  r"veld zich over een bol met oppervlakte \(4\pi r^{2}\). Een lange draad is "
                  r"lang in één richting, dus spreidt het veld zich enkel rondom uit, over een "
                  r"cilinder met omtrek \(2\pi r\). Eén richting minder betekent één macht van "
                  r"\(r\) minder.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-magnetische-kracht-op-een-stroom-en-op-een-lading-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De magnetische kracht op een stroom en op een lading",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De laplacekracht op een draad",
             opdracht=r"Gebruik \(F = B\,I\,\ell\,\sin\alpha\). Waar geen hoek staat, ligt de "
                      r"draad loodrecht op het veld.",
             oefeningen=[
                 ("kort", r"\(B = 0{,}40\ \text{T}\), \(I = 3{,}0\ \text{A}\), "
                          r"\(\ell = 0{,}20\ \text{m}\). Hoe groot is \(F\)?",
                  r"\(F = 0{,}40\cdot 3{,}0\cdot 0{,}20 = 0{,}24\ \text{N}\)", W),
                 ("kort", r"\(F = 0{,}60\ \text{N}\), \(I = 5{,}0\ \text{A}\), "
                          r"\(\ell = 0{,}30\ \text{m}\). Hoe groot is \(B\)?",
                  r"\(B = \dfrac{0{,}60}{5{,}0\cdot 0{,}30} = 0{,}40\ \text{T}\)", W),
                 ("kort", r"\(B = 0{,}50\ \text{T}\), \(\ell = 0{,}40\ \text{m}\), "
                          r"\(F = 1{,}0\ \text{N}\). Hoe groot is \(I\)?",
                  r"\(I = \dfrac{1{,}0}{0{,}50\cdot 0{,}40} = 5{,}0\ \text{A}\)", W),
                 ("kort", r"Een draad van \(25\ \text{cm}\) in een veld van "
                          r"\(0{,}60\ \text{T}\) voelt \(0{,}45\ \text{N}\). Welke stroom loopt "
                          r"erdoor?",
                  r"\(I = \dfrac{0{,}45}{0{,}60\cdot 0{,}25} = 3{,}0\ \text{A}\)", W),
                 ("kort", r"\(B = 0{,}25\ \text{T}\), \(I = 4{,}0\ \text{A}\), "
                          r"\(\ell = 0{,}60\ \text{m}\), maar nu onder \(30^{\circ}\). Hoe groot "
                          r"is \(F\)?",
                  r"\(F = 0{,}25\cdot 4{,}0\cdot 0{,}60\cdot 0{,}50 = 0{,}30\ \text{N}\)", W),
                 ("kort", r"\(B = 0{,}80\ \text{T}\), \(I = 2{,}5\ \text{A}\), "
                          r"\(\ell = 0{,}12\ \text{m}\), onder \(45^{\circ}\). Hoe groot is "
                          r"\(F\)?",
                  r"\(F = 0{,}24\cdot \sin 45^{\circ} = 0{,}17\ \text{N}\)", W),
             ]),
        dict(kop="De lorentzkracht op een lading",
             opdracht=r"Gebruik \(F = q\,v\,B\,\sin\alpha\). De elementaire lading is "
                      r"\(e = 1{,}6\cdot 10^{-19}\ \text{C}\).",
             oefeningen=[
                 ("kort", r"\(q = 2{,}0\cdot 10^{-6}\ \text{C}\), "
                          r"\(v = 3{,}0\cdot 10^{5}\ \text{m/s}\), \(B = 0{,}20\ \text{T}\), "
                          r"loodrecht. Hoe groot is \(F\)?",
                  r"\(F = 2{,}0\cdot 10^{-6}\cdot 3{,}0\cdot 10^{5}\cdot 0{,}20 = "
                  r"0{,}12\ \text{N}\)", W),
                 ("kort", r"Een elektron vliegt met \(2{,}0\cdot 10^{6}\ \text{m/s}\) loodrecht "
                          r"door een veld van \(0{,}50\ \text{T}\). Hoe groot is \(F\)?",
                  r"\(F = 1{,}6\cdot 10^{-19}\cdot 2{,}0\cdot 10^{6}\cdot 0{,}50 = "
                  r"1{,}6\cdot 10^{-13}\ \text{N}\)", W),
                 ("kort", r"Een proton vliegt met \(4{,}0\cdot 10^{5}\ \text{m/s}\) loodrecht "
                          r"door een veld van \(0{,}30\ \text{T}\). Hoe groot is \(F\)?",
                  r"\(F = 1{,}9\cdot 10^{-14}\ \text{N}\)", W),
                 ("kort", r"Een lading voelt \(0{,}080\ \text{N}\) bij "
                          r"\(v = 200\ \text{m/s}\) loodrecht in \(B = 0{,}40\ \text{T}\). Hoe "
                          r"groot is \(q\)?",
                  r"\(q = \dfrac{0{,}080}{200\cdot 0{,}40} = 1{,}0\ \text{mC}\)", W),
                 ("open", "Een elektron beweegt precies langs de veldlijnen. Welke kracht voelt "
                          "het? Leg uit.",
                  r"Geen enkele: \(\sin 0^{\circ} = 0\). De magnetische kracht werkt alleen op "
                  r"het stuk van de snelheid dat dwars op het veld staat, en dat is hier nul.", 5),
             ]),
        dict(kop="De cirkelbaan",
             opdracht=r"Gebruik \(r = \dfrac{m\,v}{q\,B}\) en \(T = \dfrac{2\pi m}{q\,B}\). "
                      r"Een proton weegt \(1{,}67\cdot 10^{-27}\ \text{kg}\), een elektron "
                      r"\(9{,}11\cdot 10^{-31}\ \text{kg}\).",
             oefeningen=[
                 ("kort", r"Een proton met \(v = 2{,}0\cdot 10^{6}\ \text{m/s}\) komt loodrecht "
                          r"in een veld van \(0{,}50\ \text{T}\). Hoe groot is \(r\)?",
                  r"\(r = \dfrac{1{,}67\cdot 10^{-27}\cdot 2{,}0\cdot 10^{6}}"
                  r"{1{,}6\cdot 10^{-19}\cdot 0{,}50} = 4{,}2\ \text{cm}\)", W),
                 ("kort", r"Een elektron met \(v = 1{,}0\cdot 10^{7}\ \text{m/s}\) in een veld "
                          r"van \(0{,}020\ \text{T}\). Hoe groot is \(r\)?",
                  r"\(r = 2{,}8\cdot 10^{-3}\ \text{m}\), dus \(2{,}8\ \text{mm}\)", W),
                 ("kort", r"Hoe lang doet het proton van de eerste opgave over één ronde?",
                  r"\(T = \dfrac{2\pi\cdot 1{,}67\cdot 10^{-27}}{1{,}6\cdot 10^{-19}\cdot 0{,}50} "
                  r"= 1{,}3\cdot 10^{-7}\ \text{s}\)", W),
                 ("kort", r"Twee ionen met dezelfde lading en snelheid maken bochten met straal "
                          r"\(12\ \text{cm}\) en \(18\ \text{cm}\). Hoe verhouden hun massa's "
                          r"zich?",
                  r"\(r \sim m\), dus \(m_{1}:m_{2} = 2:3\)", W),
                 ("open", r"Een deeltje komt schuin, onder \(60^{\circ}\) met de veldlijnen, een "
                          r"homogeen veld binnen. Beschrijf zijn baan en leg uit waarom ze er zo "
                          r"uitziet.",
                  r"Het stuk van de snelheid langs het veld loopt gewoon door, het stuk dwars "
                  r"erop maakt een cirkel. Samen geeft dat een schroeflijn.", 6),
             ]),
        dict(kop="Hoe verandert het?",
             opdracht="Vul de rijtjes aan. Alles wat niet genoemd wordt, blijft gelijk.",
             oefeningen=[
                 ("rij", [(r"de stroom maal 2", r"\(F\) maal 2"),
                          (r"de hoek van \(90^{\circ}\) naar \(30^{\circ}\)", r"\(F\) maal \(0{,}50\)")],
                  r"Wat gebeurt er met de laplacekracht \(F\)?", WL),
                 ("rij", [(r"\(B\) maal 3 en \(\ell\) maal 2", r"\(F\) maal 6"),
                          (r"de draad evenwijdig met het veld", r"\(F\) wordt nul")],
                  r"Wat gebeurt er met de laplacekracht \(F\)?", WL),
                 ("rij", [(r"de snelheid maal 2", r"\(r\) maal 2"),
                          (r"\(B\) maal 4", r"\(r\) gedeeld door 4")],
                  r"Wat gebeurt er met de straal \(r\)?", WL),
                 ("rij", [(r"de massa maal 2", r"\(r\) maal 2"),
                          (r"de snelheid maal 2 én \(B\) maal 2", r"\(r\) blijft gelijk")],
                  r"Wat gebeurt er met de straal \(r\)?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De magnetische kracht staat loodrecht op het veld én op de stroom.", True),
                 ("waar", "Een stilstaande lading in een magnetisch veld voelt een kracht.", False),
                 ("waar", "De magnetische kracht verandert de grootte van de snelheid van een lading.", False),
                 ("waar", "Een lading dwars op een homogeen veld beschrijft een cirkel.", True),
                 ("waar", "Twee parallelle draden met stroom in dezelfde zin trekken elkaar aan.", True),
                 ("waar", r"In \(F = B\,I\,\ell\,\sin\alpha\) staat ook de weerstand van de draad.", False),
                 ("waar", r"De omlooptijd \(T = \dfrac{2\pi m}{qB}\) hangt niet van de snelheid af.", True),
             ]),
        dict(kop="Toepassingen en uitleg",
             opdracht="Antwoord kort, en bij de laatste drie in volle zinnen.",
             oefeningen=[
                 ("rij", [("scheidt ionen volgens hun massa", "een massaspectrometer"),
                          ("zet elektrische energie om in beweging", "een elektromotor")],
                  "Welk toestel?", WL),
                 ("rij", [("meet de sterkte van een magnetisch veld", "een hallsensor"),
                          ("versnelt deeltjes in een spiraal", "een cyclotron")],
                  "Welk toestel?", WL),
                 ("open", "Waarom verandert de magnetische kracht de snelheid van een lading niet in grootte?",
                  r"Ze staat loodrecht op de snelheid, dus \(W = F\,d\,\cos 90^{\circ} = 0\). "
                  r"Zonder arbeid verandert de kinetische energie niet, en dus de snelheid niet "
                  r"in grootte; alleen de richting draait.", 5),
                 ("open", "Leg uit hoe een elektromotor draait.",
                  "Door de wikkeling loopt stroom in een magnetisch veld, dus werken er op de twee "
                  "zijden van de lus krachten in tegengestelde zin. Dat koppel doet de as draaien; "
                  "een collector keert de stroom elke halve omwenteling om.", 6),
                 ("open", r"In een cyclotron krijgt een deeltje bij elke ronde een duw. Waarom mag "
                          r"die duw altijd op hetzelfde ritme komen, ook al gaat het deeltje "
                          r"steeds sneller?",
                  r"In \(T = \dfrac{2\pi m}{q\,B}\) staat geen snelheid: een sneller deeltje maakt "
                  r"een ruimere bocht, maar doet over één ronde even lang.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektromagnetische-inductie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektromagnetische inductie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Komt er spanning?",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("een magneet stilhouden in een spoel", "nee"),
                          ("een magneet uit een spoel trekken", "ja"),
                          ("een spoel in een veld groter maken", "ja")],
                  "Inductiespanning?", WW),
                 ("rij", [("een spoel in een homogeen veld laten liggen", "nee"),
                          ("een spoel in een veld ronddraaien", "ja"),
                          ("de stroom in een naburige spoel opdrijven", "ja")],
                  "Inductiespanning?", WW),
             ]),
        dict(kop="Rekenen met de flux",
             opdracht=r"Gebruik \(\Phi = B\,A\,\cos\alpha\), met \(\alpha\) de hoek tussen het "
                      r"veld en de normaal op het vlak. Waar geen hoek staat, is de winding "
                      r"loodrecht op het veld.",
             oefeningen=[
                 ("kort", r"\(B = 0{,}50\ \text{T}\) en \(A = 0{,}20\ \text{m}^{2}\). Hoe groot "
                          r"is \(\Phi\)?",
                  r"\(\Phi = 0{,}50\cdot 0{,}20 = 0{,}10\ \text{Wb}\)", W),
                 ("kort", r"\(B = 0{,}80\ \text{T}\), \(A = 0{,}050\ \text{m}^{2}\), maar nu "
                          r"onder \(\alpha = 60^{\circ}\). Hoe groot is \(\Phi\)?",
                  r"\(\Phi = 0{,}80\cdot 0{,}050\cdot 0{,}50 = 0{,}020\ \text{Wb}\)", W),
                 ("kort", r"\(\Phi = 0{,}012\ \text{Wb}\) door een winding van "
                          r"\(0{,}030\ \text{m}^{2}\). Hoe groot is \(B\)?",
                  r"\(B = \dfrac{0{,}012}{0{,}030} = 0{,}40\ \text{T}\)", W),
                 ("kort", r"Hoe groot moet \(A\) zijn voor \(\Phi = 0{,}015\ \text{Wb}\) in een "
                          r"veld van \(0{,}30\ \text{T}\)?",
                  r"\(A = \dfrac{0{,}015}{0{,}30} = 0{,}050\ \text{m}^{2}\)", W),
                 ("open", r"Een winding ligt plat in een veld, dus evenwijdig met de veldlijnen. "
                          r"Hoe groot is \(\Phi\), en waarom?",
                  r"Nul. De hoek met de normaal is dan \(90^{\circ}\) en "
                  r"\(\cos 90^{\circ} = 0\): er gaat geen enkele veldlijn door de winding heen, "
                  r"ze scheren er allemaal langs.", 5),
             ]),
        dict(kop="Rekenen met de wet van Faraday",
             opdracht=r"Gebruik \(U = N\,\dfrac{\Delta\Phi}{\Delta t}\). Het minteken van Lenz "
                      r"laten we hier weg; het gaat om de grootte.",
             oefeningen=[
                 ("kort", r"De flux gaat in één lus in \(0{,}40\ \text{s}\) van "
                          r"\(0{,}80\ \text{Wb}\) naar nul. Hoe groot is \(U\)?",
                  r"\(U = \dfrac{0{,}80}{0{,}40} = 2{,}0\ \text{V}\)", W),
                 ("kort", r"Dezelfde fluxverandering, maar in een spoel van \(50\) windingen. "
                          r"Hoe groot is \(U\) nu?",
                  r"\(U = 50\cdot 2{,}0 = 100\ \text{V}\)", W),
                 ("kort", r"\(N = 400\), \(\Delta\Phi = 0{,}0030\ \text{Wb}\), "
                          r"\(\Delta t = 0{,}020\ \text{s}\). Hoe groot is \(U\)?",
                  r"\(U = 400\cdot\dfrac{0{,}0030}{0{,}020} = 60\ \text{V}\)", W),
                 ("kort", r"\(N = 250\) en \(U = 5{,}0\ \text{V}\) gedurende "
                          r"\(0{,}10\ \text{s}\). Hoe groot was \(\Delta\Phi\)?",
                  r"\(\Delta\Phi = \dfrac{5{,}0\cdot 0{,}10}{250} = "
                  r"2{,}0\cdot 10^{-3}\ \text{Wb}\)", W),
                 ("kort", r"Een spoel van \(150\) windingen en \(A = 0{,}0040\ \text{m}^{2}\) "
                          r"staat loodrecht in een veld dat in \(0{,}050\ \text{s}\) van nul naar "
                          r"\(0{,}60\ \text{T}\) gaat. Hoe groot is \(U\)?",
                  r"\(\Delta\Phi = 0{,}60\cdot 0{,}0040 = 2{,}4\cdot 10^{-3}\ \text{Wb}\), dus "
                  r"\(U = 150\cdot\dfrac{2{,}4\cdot 10^{-3}}{0{,}050} = 7{,}2\ \text{V}\)", W),
                 ("rij", [(r"het aantal windingen maal 2", r"\(U\) maal 2"),
                          (r"dezelfde verandering in de helft van de tijd", r"\(U\) maal 2")],
                  r"Wat gebeurt er met \(U\)?", WL),
                 ("rij", [(r"\(\Delta\Phi\) maal 3", r"\(U\) maal 3"),
                          (r"de flux blijft een tijdlang gelijk", r"\(U\) wordt nul")],
                  r"Wat gebeurt er met \(U\)?", WL),
             ]),
        dict(kop="De transformator",
             opdracht=r"Gebruik \(\dfrac{U_{1}}{U_{2}} = \dfrac{N_{1}}{N_{2}}\) en, voor een "
                      r"ideale transformator, \(U_{1}I_{1} = U_{2}I_{2}\).",
             oefeningen=[
                 ("kort", r"\(U_{1} = 230\ \text{V}\), \(N_{1} = 1150\), \(N_{2} = 60\). Hoe "
                          r"groot is \(U_{2}\)?",
                  r"\(U_{2} = 230\cdot\dfrac{60}{1150} = 12\ \text{V}\)", W),
                 ("kort", r"Hoeveel windingen secundair heb je nodig om van "
                          r"\(230\ \text{V}\) naar \(46\ \text{V}\) te gaan, met \(1000\) "
                          r"primair?",
                  r"\(N_{2} = 1000\cdot\dfrac{46}{230} = 200\)", W),
                 ("kort", r"Een laadblokje maakt van \(230\ \text{V}\) een spanning van "
                          r"\(5{,}0\ \text{V}\), met \(2300\) windingen primair. Hoeveel "
                          r"secundair?",
                  r"\(N_{2} = 2300\cdot\dfrac{5{,}0}{230} = 50\)", W),
                 ("kort", r"Een ideale transformator levert \(12\ \text{V}\) en "
                          r"\(2{,}0\ \text{A}\) secundair, met \(230\ \text{V}\) primair. Hoe "
                          r"groot is \(I_{1}\)?",
                  r"\(P = 12\cdot 2{,}0 = 24\ \text{W}\), dus "
                  r"\(I_{1} = \dfrac{24}{230} = 0{,}10\ \text{A}\)", W),
                 ("open", r"Waarom wordt stroom over grote afstanden op hoogspanning vervoerd? "
                          r"Gebruik \(P = U\,I\) en \(P_{\text{verlies}} = R\,I^{2}\) in je "
                          r"antwoord.",
                  r"Hetzelfde vermogen bij een hogere spanning betekent een kleinere stroom, want "
                  r"\(P = U\,I\). Het verlies in de kabels is \(R\,I^{2}\), dus met het kwadraat "
                  r"van die stroom: tien keer minder stroom is honderd keer minder verlies.", 5),
             ]),
        dict(kop="Begrippen en waar of niet waar",
             opdracht="Antwoord kort, en kruis daarna aan.",
             oefeningen=[
                 ("rij", [("de zin van de inductiestroom werkt de verandering tegen", "de wet van Lenz"),
                          ("de kringstromen in een massief stuk metaal", "wervelstromen")],
                  "Hoe heet dat?", WL),
                 ("rij", [("zet beweging om in elektrische energie", "een generator"),
                          ("verandert de spanning van wisselspanning", "een transformator")],
                  "Welk toestel?", WL),
                 ("rij", [(r"de eenheid van \(\Phi\)", "de weber"),
                          (r"de grootheid met symbool \(\Phi\)", "de magnetische flux")],
                  "Hoe heet dat?", WL),
                 ("waar", "Een inductiespanning ontstaat alleen bij een veránderende flux.", True),
                 ("waar", "Hoe sneller de verandering, hoe groter de inductiespanning.", True),
                 ("waar", "Een transformator werkt ook op gelijkspanning.", False),
                 ("waar", "De wet van Lenz volgt uit het behoud van energie.", True),
                 ("waar", r"In \(U = -N\dfrac{\Delta\Phi}{\Delta t}\) staat ook de flux zelf.", False),
                 ("waar", "Op een fluxgrafiek is de inductiespanning de helling, niet de hoogte.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een magneet die je in een koperen buis laat vallen, zakt heel langzaam. Leg uit.",
                  "De vallende magneet verandert de flux door de buis, dus ontstaan er "
                  "wervelstromen. Volgens de wet van Lenz werken die de beweging tegen, en dus "
                  "remmen ze de magneet af.", 5),
                 ("open", "Waarom zou een inductiestroom die de verandering versterkt in plaats van tegenwerkt onmogelijk zijn?",
                  "Dan zou de verandering zichzelf versterken en zou er energie uit het niets "
                  "blijven komen. Dat botst met het behoud van energie.", 5),
                 ("open", "Leg uit waarom een inductiekookplaat een pan verwarmt maar de plaat zelf nauwelijks.",
                  "De spoel onder de plaat maakt een snel wisselend magnetisch veld. In de metalen "
                  "bodem van de pan wekt dat wervelstromen op, en die verwarmen die bodem; het "
                  "glas van de plaat geleidt geen stroom en blijft koel.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-statica-krachten-moment-en-evenwicht-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Statica: krachten, moment en evenwicht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zwaartekracht, wrijving en veerkracht",
             opdracht=r"Gebruik \(F_{z} = m\,g\), \(F_{w} = \mu\,F_{N}\) en "
                      r"\(F = k\,\Delta\ell\). Neem \(g = 9{,}81\ \text{N/kg}\), tenzij er iets "
                      r"anders staat.",
             oefeningen=[
                 ("kort", r"Hoe groot is \(F_{z}\) op \(m = 12\ \text{kg}\)?",
                  r"\(F_{z} = 12\cdot 9{,}81 = 118\ \text{N}\)", W),
                 ("kort", r"Een kist van \(45\ \text{kg}\) staat op een vlakke vloer met "
                          r"\(\mu = 0{,}25\). Welke kracht doet haar schuiven? Neem "
                          r"\(g = 10\ \text{N/kg}\).",
                  r"\(F_{N} = 450\ \text{N}\), dus "
                  r"\(F_{w} = 0{,}25\cdot 450 = 113\ \text{N}\)", W),
                 ("kort", r"Een veer met \(k = 80\ \text{N/m}\) wordt \(15\ \text{cm}\) "
                          r"uitgerekt. Welke kracht levert ze?",
                  r"\(F = 80\cdot 0{,}15 = 12\ \text{N}\)", W),
                 ("kort", r"Een veer rekt \(4{,}0\ \text{cm}\) uit onder een kracht van "
                          r"\(6{,}0\ \text{N}\). Hoe groot is \(k\)?",
                  r"\(k = \dfrac{6{,}0}{0{,}040} = 150\ \text{N/m}\)", W),
                 ("kort", r"Een blok van \(8{,}0\ \text{kg}\) ligt op een helling van "
                          r"\(30^{\circ}\). Hoe groot is de component langs het vlak? Neem "
                          r"\(g = 10\ \text{N/kg}\).",
                  r"\(F_{z}\sin 30^{\circ} = 80\cdot 0{,}50 = 40\ \text{N}\)", W),
             ]),
        dict(kop="Krachten samenstellen",
             opdracht=r"Bij een rechte hoek gebruik je Pythagoras: "
                      r"\(F = \sqrt{F_{1}^{2} + F_{2}^{2}}\).",
             oefeningen=[
                 ("rij", [(r"\(30\ \text{N}\) en \(40\ \text{N}\) in dezelfde zin", r"\(70\ \text{N}\)"),
                          (r"\(30\ \text{N}\) en \(40\ \text{N}\) in tegengestelde zin", r"\(10\ \text{N}\)"),
                          (r"\(30\ \text{N}\) en \(40\ \text{N}\) loodrecht op elkaar", r"\(50\ \text{N}\)")],
                  "Welke resultante?", WW),
                 ("rij", [(r"\(9{,}0\ \text{N}\) en \(12\ \text{N}\) loodrecht", r"\(15\ \text{N}\)"),
                          (r"\(5{,}0\ \text{N}\) en \(12\ \text{N}\) loodrecht", r"\(13\ \text{N}\)")],
                  "Welke resultante?", WW),
                 ("open", "Leg uit waarom je twee krachten die niet op één lijn liggen niet gewoon mag optellen.",
                  "Een kracht is een vector: ze heeft ook een richting. Je moet ze dus als vectoren "
                  "samenstellen, met de parallellogramregel of met Pythagoras bij een rechte "
                  "hoek.", 5),
             ]),
        dict(kop="Het moment van een kracht",
             opdracht=r"Gebruik \(M = F\,d\,\sin\alpha\). Waar geen hoek staat, werkt de kracht "
                      r"loodrecht.",
             oefeningen=[
                 ("kort", r"\(F = 40\ \text{N}\) op \(d = 0{,}30\ \text{m}\). Hoe groot is "
                          r"\(M\)?",
                  r"\(M = 40\cdot 0{,}30 = 12\ \text{N}\cdot\text{m}\)", W),
                 ("kort", r"Je wil \(M = 30\ \text{N}\cdot\text{m}\) met \(d = 0{,}50\ \text{m}\). "
                          r"Welke kracht heb je nodig?",
                  r"\(F = \dfrac{30}{0{,}50} = 60\ \text{N}\)", W),
                 ("kort", r"\(F = 25\ \text{N}\) geeft \(M = 5{,}0\ \text{N}\cdot\text{m}\). Hoe "
                          r"lang is de arm?",
                  r"\(d = \dfrac{5{,}0}{25} = 0{,}20\ \text{m}\)", W),
                 ("kort", r"\(F = 60\ \text{N}\) op \(d = 0{,}40\ \text{m}\), maar onder "
                          r"\(\alpha = 30^{\circ}\) met de stang. Hoe groot is \(M\)?",
                  r"\(M = 60\cdot 0{,}40\cdot 0{,}50 = 12\ \text{N}\cdot\text{m}\)", W),
                 ("kort", r"Dezelfde kracht en afstand, maar onder \(\alpha = 90^{\circ}\). Hoe "
                          r"groot is \(M\) nu?",
                  r"\(M = 60\cdot 0{,}40 = 24\ \text{N}\cdot\text{m}\), het dubbele", W),
                 ("open", r"Een kracht werkt precies langs de stang, dus \(\alpha = 0^{\circ}\). "
                          r"Hoe groot is het moment, en wat betekent dat voor een deur?",
                  r"Nul, want \(\sin 0^{\circ} = 0\): de werklijn gaat door het draaipunt en de "
                  r"arm is nul. Duw je een deur recht naar de scharnieren toe, dan gaat ze niet "
                  r"open, hoe hard je ook duwt.", 5),
             ]),
        dict(kop="De wipplank en de hefboom",
             opdracht=r"In rotatie-evenwicht is \(\sum M = 0\): de momenten linksom en rechtsom "
                      r"zijn even groot.",
             oefeningen=[
                 ("kort", r"Links \(300\ \text{N}\) op \(1{,}2\ \text{m}\). Rechts "
                          r"\(450\ \text{N}\). Op welke afstand zit die?",
                  r"\(d = \dfrac{300\cdot 1{,}2}{450} = 0{,}80\ \text{m}\)", WW),
                 ("kort", r"Links \(500\ \text{N}\) op \(0{,}90\ \text{m}\). Rechts zit iemand op "
                          r"\(1{,}5\ \text{m}\). Welk gewicht?",
                  r"\(F = \dfrac{500\cdot 0{,}90}{1{,}5} = 300\ \text{N}\)", WW),
                 ("kort", r"Een kind van \(25\ \text{kg}\) zit op \(1{,}8\ \text{m}\). Waar moet "
                          r"een kind van \(30\ \text{kg}\) zitten?",
                  r"\(d = \dfrac{25\cdot 1{,}8}{30} = 1{,}5\ \text{m}\)", WW),
                 ("open", r"Een plank van \(4{,}0\ \text{m}\) rust op twee steunen aan de "
                          r"uiteinden. Een last van \(600\ \text{N}\) staat op \(1{,}0\ \text{m}\) "
                          r"van de linkersteun. Hoeveel draagt elke steun? Neem de momenten rond "
                          r"de rechtersteun.",
                  r"Rond rechts: \(F_{\text{links}}\cdot 4{,}0 = 600\cdot 3{,}0\), dus "
                  r"\(F_{\text{links}} = 450\ \text{N}\). De rest, \(150\ \text{N}\), draagt de "
                  r"rechtersteun.", 6),
             ]),
        dict(kop="Evenwicht of niet",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een voorwerp in evenwicht staat altijd stil.", False),
                 ("waar", r"Voor evenwicht moet \(\sum F = 0\) zijn.", True),
                 ("waar", r"Voor evenwicht moet ook \(\sum M = 0\) zijn.", True),
                 ("waar", "Op een voorwerp dat op een tafel ligt, werkt alleen de zwaartekracht.", False),
                 ("waar", r"In \(M = F\,d\,\sin\alpha\) is het moment het grootst bij \(\alpha = 90^{\circ}\).", True),
                 ("waar", "Het zwaartepunt moet buiten het steunvlak liggen om niet te kantelen.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom gaat een deur makkelijker open aan de kruk dan vlak bij de scharnieren?",
                  r"\(M = F\,d\): aan de kruk is \(d\) veel groter, dus volstaat een veel "
                  r"kleinere kracht voor hetzelfde moment.", 5),
                 ("open", "Waarom staat een piramide stabieler dan een hoge smalle toren?",
                  "Het zwaartepunt ligt laag en het steunvlak is breed, dus moet je hem heel ver "
                  "kantelen voor het zwaartepunt buiten dat steunvlak komt.", 5),
                 ("open", r"Waarom staat er aan de achterste arm van een torenkraan een zwaar "
                          r"blok?",
                  r"Om het moment van de last aan de voorkant tegen te werken. Samen moeten de "
                  r"momenten rond de mast nul zijn, anders kantelt de kraan.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-wetten-van-newton-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De wetten van Newton",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke wet?",
             opdracht="Schrijf eerste, tweede of derde.",
             oefeningen=[
                 ("rij", [(r"\(F = m\,a\)", "tweede"), ("actie en reactie", "derde"),
                          ("zonder resultante blijft de snelheid gelijk", "eerste")],
                  "Welke wet van Newton?", WW),
                 ("rij", [("een bal blijft rollen op een glad vlak", "eerste"),
                          ("een raket duwt gas weg en gaat vooruit", "derde"),
                          ("dezelfde kracht versnelt een lichte kar meer", "tweede")],
                  "Welke wet van Newton?", WW),
             ]),
        dict(kop="Rekenen met F = m · a",
             opdracht=r"Gebruik \(F_{\text{res}} = m\,a\). Waar een gewicht gevraagd wordt, "
                      r"geldt \(F_{z} = m\,g\) met \(g = 9{,}81\ \text{N/kg}\).",
             oefeningen=[
                 ("rij", [(r"\(m = 4{,}0\ \text{kg}\), \(a = 3{,}0\ \text{m/s}^{2}\)",
                           r"\(F = 12\ \text{N}\)"),
                          (r"\(F = 50\ \text{N}\), \(m = 10\ \text{kg}\)",
                           r"\(a = 5{,}0\ \text{m/s}^{2}\)"),
                          (r"\(F = 18\ \text{N}\), \(a = 6{,}0\ \text{m/s}^{2}\)",
                           r"\(m = 3{,}0\ \text{kg}\)")],
                  "Wat ontbreekt?", WL),
                 ("kort", r"Een kar van \(800\ \text{kg}\) versnelt met "
                          r"\(2{,}5\ \text{m/s}^{2}\). Welke resultante werkt erop?",
                  r"\(F = 800\cdot 2{,}5 = 2000\ \text{N}\)", W),
                 ("kort", r"Hoe groot is het gewicht van \(15\ \text{kg}\) op aarde?",
                  r"\(F_{z} = 15\cdot 9{,}81 = 147\ \text{N}\)", W),
                 ("kort", r"Een slee van \(25\ \text{kg}\) wordt met \(90\ \text{N}\) getrokken "
                          r"en voelt \(15\ \text{N}\) wrijving. Hoe groot is \(a\)?",
                  r"\(F_{\text{res}} = 75\ \text{N}\), dus "
                  r"\(a = \dfrac{75}{25} = 3{,}0\ \text{m/s}^{2}\)", W),
                 ("kort", r"Een fietser van \(70\ \text{kg}\) gaat van \(0\) naar "
                          r"\(8{,}0\ \text{m/s}\) in \(4{,}0\ \text{s}\). Welke resultante is "
                          r"daarvoor nodig?",
                  r"\(a = \dfrac{8{,}0}{4{,}0} = 2{,}0\ \text{m/s}^{2}\), dus "
                  r"\(F = 70\cdot 2{,}0 = 140\ \text{N}\)", W),
                 ("kort", r"Een wagen van \(1200\ \text{kg}\) remt van \(20\ \text{m/s}\) naar "
                          r"stilstand in \(5{,}0\ \text{s}\). Hoe groot is de remkracht?",
                  r"\(a = \dfrac{-20}{5{,}0} = -4{,}0\ \text{m/s}^{2}\), dus "
                  r"\(F = 4800\ \text{N}\) tegen de rijrichting in", W),
             ]),
        dict(kop="Hoe verandert het?",
             opdracht=r"Vul aan voor \(a = \dfrac{F}{m}\).",
             oefeningen=[
                 ("rij", [("de kracht maal 3", r"\(a\) maal 3"),
                          ("de massa maal 2", r"\(a\) gedeeld door 2")],
                  r"Wat gebeurt er met \(a\)?", WL),
                 ("rij", [("de kracht maal 4 en de massa maal 2", r"\(a\) maal 2"),
                          ("de resulterende kracht wordt nul", r"\(a\) wordt nul")],
                  r"Wat gebeurt er met \(a\)?", WL),
             ]),
        dict(kop="Massa of gewicht",
             opdracht="Schrijf massa of gewicht.",
             oefeningen=[
                 ("rij", [("staat in kilogram", "massa"), ("staat in newton", "gewicht"),
                          ("is op de maan kleiner dan op aarde", "gewicht")],
                  "Massa of gewicht?", WW),
                 ("rij", [("is de maat van de traagheid", "massa"),
                          ("is een kracht", "gewicht")],
                  "Massa of gewicht?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Zonder resultante kracht staat een lichaam altijd stil.", False),
                 ("waar", "Actie en reactie werken op twee verschillende lichamen.", True),
                 ("waar", "Actie en reactie heffen elkaar op, dus kan niets bewegen.", False),
                 ("waar", "Bij dezelfde kracht versnelt een grotere massa minder.", True),
                 ("waar", r"In \(a = \dfrac{F}{m}\) staat de massa in de teller.", False),
                 ("waar", "Afremmen is ook een versnelling, maar met een tegengestelde zin.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom schiet je naar voren als een bus plots remt?",
                  "Je lichaam had de snelheid van de bus en houdt die volgens de eerste wet, want er "
                  "werkt geen kracht op jou die je mee afremt. De bus vertraagt wel, en dus schuif "
                  "je naar voren ten opzichte van de bus.", 5),
                 ("open", "Actie en reactie zijn even groot en tegengesteld. Leg uit waarom een raket toch vooruit komt.",
                  "De twee krachten werken op verschillende lichamen: de raket duwt het gas naar "
                  "achter en het gas duwt de raket naar voor. Op de raket zelf blijft dus één kracht "
                  "over, en die versnelt hem.", 5),
                 ("open", "Een lift versnelt naar boven. Waarom voel je je zwaarder?",
                  "De vloer moet je gewicht dragen én je versnellen, dus duwt ze harder dan je "
                  "gewicht. Die grotere kracht van de vloer voel je als zwaarder zijn.", 5),
                 ("open", r"Een steen en een veertje vallen in een luchtledige buis even snel. "
                          r"Leg uit met \(F = m\,a\).",
                  r"Zonder lucht werkt enkel de zwaartekracht, dus \(m\,g = m\,a\). De massa "
                  r"staat aan allebei de kanten en valt weg: \(a = g\), hoe zwaar het voorwerp "
                  r"ook is.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-rechtlijnige-beweging-erb-en-evrb-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rechtlijnige beweging: ERB en EVRB",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="ERB of EVRB",
             opdracht="Schrijf ERB of EVRB.",
             oefeningen=[
                 ("rij", [("de snelheid blijft gelijk", "ERB"),
                          (r"de versnelling is constant en niet \(0\)", "EVRB"),
                          ("een steen die vrij valt", "EVRB")],
                  "ERB of EVRB?", WW),
                 ("rij", [("een auto met de cruisecontrol aan", "ERB"),
                          ("een trein die optrekt", "EVRB"),
                          ("een fietser die gelijkmatig remt", "EVRB")],
                  "ERB of EVRB?", WW),
                 ("kies", "Welke grafiek hoort bij een EVRB?",
                  [r"een \(v(t)\) die schuin stijgt",
                   r"een \(v(t)\) die horizontaal loopt",
                   r"een \(x(t)\) die een rechte is",
                   r"een \(a(t)\) die op de tijdas ligt"], 0),
             ]),
        dict(kop="Rekenen aan een ERB",
             opdracht=r"Gebruik \(v = \dfrac{\Delta x}{\Delta t}\) en \(x = x_{0} + v\,t\).",
             oefeningen=[
                 ("rij", [(r"\(v = 15\) m/s, \(t = 8{,}0\) s", r"\(x = 120\) m"),
                          (r"\(x = 300\) m, \(t = 12\) s", r"\(v = 25\) m/s"),
                          (r"\(x = 90\) m, \(v = 6{,}0\) m/s", r"\(t = 15\) s")],
                  "Wat ontbreekt?", WW),
                 ("kort", r"Hoeveel meter per seconde is \(54\) km/h?",
                  r"\(15\) m/s, want je deelt door \(3{,}6\).", W),
                 ("kort", r"Hoeveel kilometer per uur is \(12\) m/s?",
                  r"\(43{,}2\) km/h, want je vermenigvuldigt met \(3{,}6\).", W),
                 ("kort", r"Een wandelaar loopt \(1{,}2\) km heen en \(1{,}2\) km terug in \(30\) min. Hoe groot zijn \(s\) en \(\Delta x\)?",
                  r"\(s = 2{,}4\) km, dus \(1{,}33\) m/s gemiddeld; \(\Delta x = 0\).", WL),
             ]),
        dict(kop="Rekenen aan een EVRB",
             opdracht=r"Gebruik \(v = v_{0} + a\,t\), \(x = v_{0}t + \tfrac{1}{2}a\,t^{2}\) of \(v^{2} = v_{0}^{2} + 2a\,\Delta x\).",
             oefeningen=[
                 ("kort", r"Uit rust met \(a = 3{,}0\ \text{m/s}^{2}\): welke \(v\) na \(6{,}0\) s?",
                  r"\(18\) m/s, want \(v = a\,t\).", W),
                 ("kort", r"Dezelfde wagen: welke afstand legde hij in die \(6{,}0\) s af?",
                  r"\(54\) m, want \(\tfrac{1}{2} \times 3{,}0 \times 36\).", WW),
                 ("kort", r"Van \(20\) m/s naar stilstand in \(4{,}0\) s. Hoe groot is \(a\)?",
                  r"\(-5{,}0\ \text{m/s}^{2}\), uit \(\dfrac{0-20}{4{,}0}\).", WW),
                 ("kort", r"Een auto met \(30\) m/s remt met \(5{,}0\ \text{m/s}^{2}\). Hoe lang is de remweg?",
                  r"\(90\) m, uit \(\dfrac{v_{0}^{2}}{2a} = \dfrac{900}{10}\).", WW),
                 ("kort", r"Een fietser gaat van \(2{,}0\) m/s naar \(8{,}0\) m/s over \(30\) m. Hoe groot is \(a\)?",
                  r"\(1{,}0\ \text{m/s}^{2}\), uit \(\dfrac{64-4}{2 \times 30}\).", WW),
             ]),
        dict(kop="De vrije val en de verticale worp",
             opdracht=r"Neem \(g = 9{,}81\ \text{m/s}^{2}\) en verwaarloos de luchtweerstand.",
             oefeningen=[
                 ("kort", r"Een steen valt \(2{,}5\) s vrij. Hoe diep is hij gevallen?",
                  r"\(30{,}7\) m, want \(\tfrac{1}{2}g\,t^{2}\).", WW),
                 ("kort", r"Hoe snel valt die steen na die \(2{,}5\) s?",
                  r"\(24{,}5\) m/s, want \(v = g\,t\).", WW),
                 ("kort", r"Van welke hoogte valt een voorwerp dat met \(30\) m/s neerkomt?",
                  r"\(45{,}9\) m, uit \(\dfrac{v^{2}}{2g}\).", WW),
                 ("kort", r"Je gooit een bal met \(15\) m/s recht omhoog. Hoe hoog komt hij?",
                  r"\(11{,}5\) m, uit \(\dfrac{v_{0}^{2}}{2g}\).", WW),
                 ("kort", r"Je verdubbelt de valtijd van een steen. Hoeveel keer dieper valt hij?",
                  r"vier keer, want \(t\) staat in het kwadraat in \(h = \tfrac{1}{2}g\,t^{2}\).", WW),
             ]),
        dict(kop="Grafieken lezen",
             opdracht="Vul aan wat je uit de grafiek afleest.",
             oefeningen=[
                 ("rij", [(r"de helling van een \(x(t)\)-grafiek", r"\(v\)"),
                          (r"de helling van een \(v(t)\)-grafiek", r"\(a\)"),
                          (r"de oppervlakte onder een \(v(t)\)-grafiek", r"\(\Delta x\)")],
                  "Wat lees je eruit?", WL),
                 ("rij", [(r"een rechte in een \(x(t)\)-grafiek", "ERB"),
                          (r"een schuine rechte in een \(v(t)\)-grafiek", "EVRB"),
                          (r"een horizontale lijn in een \(v(t)\)-grafiek", "ERB")],
                  "Welke beweging?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Een negatieve \(a\) betekent altijd vertragen.", False),
                 ("waar", r"Bij een ERB is \(a = 0\).", True),
                 ("waar", "Bij een vrije val hangt de versnelling van de massa af.", False),
                 ("waar", r"De oppervlakte onder een \(a(t)\)-grafiek geeft \(\Delta v\).", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een auto rijdt achteruit en wordt sneller. Is de versnelling positief of negatief? Leg uit.",
                  r"Dat hangt af van de zin die je positief rekent. Reken je vooruit positief, dan is "
                  r"\(v\) negatief en \(a\) ook, want \(v\) wordt nog negatiever. Een negatieve \(a\) "
                  r"betekent dus niet automatisch vertragen.", 7),
                 ("open", "Twee ballen met een verschillende massa vallen samen in vacuüm. Wie komt eerst? Leg uit.",
                  r"Ze komen samen aan. Uit \(m\,g = m\,a\) volgt \(a = g\) voor allebei: de massa "
                  r"valt links en rechts weg. In lucht verstoort de wrijving dat.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-horizontale-worp-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De horizontale worp",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee bewegingen apart",
             opdracht="Schrijf horizontaal of verticaal.",
             oefeningen=[
                 ("rij", [(r"eenparig, met \(a = 0\)", "horizontaal"),
                          (r"eenparig veranderlijk, met \(a = g\)", "verticaal"),
                          ("bepaalt de valtijd", "verticaal")],
                  "Welke richting?", WW),
                 ("rij", [("bepaalt samen met de valtijd de dracht", "horizontaal"),
                          (r"begint met snelheid \(0\)", "verticaal"),
                          ("de snelheid blijft de hele worp gelijk", "horizontaal")],
                  "Welke richting?", WW),
             ]),
        dict(kop="Rekenen aan een worp",
             opdracht=r"Reken eerst de valtijd uit met \(t = \sqrt{\dfrac{2h}{g}}\). Neem \(g = 10\ \text{m/s}^{2}\), tenzij het anders staat.",
             oefeningen=[
                 ("kort", r"Een bal rolt van een tafel van \(1{,}25\) m hoog. Hoe lang valt hij?",
                  r"\(0{,}50\) s, uit \(\sqrt{\dfrac{2{,}5}{10}}\).", WW),
                 ("kort", r"Diezelfde bal had \(4{,}0\) m/s horizontaal. Hoe ver van de tafel landt hij?",
                  r"\(2{,}0\) m, want \(x = v_{0}\,t\).", W),
                 ("kort", r"Een steen wordt horizontaal weggegooid en valt \(2{,}0\) s. Van welke hoogte?",
                  r"\(20\) m, uit \(\tfrac{1}{2}g\,t^{2}\).", WW),
                 ("kort", r"Welke \(v_{y}\) heeft die steen na \(2{,}0\) s?",
                  r"\(20\) m/s, want \(v_{y} = g\,t\).", W),
                 ("kort", r"Die steen vertrok met \(12\) m/s. Hoe groot is \(v\) bij het neerkomen?",
                  r"\(23{,}3\) m/s, uit \(\sqrt{12^{2} + 20^{2}}\).", WW),
                 ("kort", r"Een pijl vertrekt horizontaal op \(1{,}6\) m hoogte met \(55\) m/s. Neem \(g = 9{,}81\ \text{m/s}^{2}\). Hoe ver komt hij?",
                  r"\(31{,}4\) m, want \(t = 0{,}571\) s.", WW),
             ]),
        dict(kop="Omgekeerd rekenen",
             opdracht=r"Hier ken je de dracht of de valtijd en zoek je \(v_{0}\) of \(h\). Neem \(g = 10\ \text{m/s}^{2}\), tenzij het anders staat.",
             oefeningen=[
                 ("kort", r"Een bal komt van \(45\) m hoogte \(60\) m verder neer. Hoe groot was \(v_{0}\)?",
                  r"\(20\) m/s, want \(t = 3{,}0\) s.", WW),
                 ("kort", r"Een kogel met \(8{,}0\) m/s landt \(4{,}0\) m verder. Van welke hoogte vertrok hij?",
                  r"\(1{,}25\) m, want \(t = 0{,}50\) s.", WW),
                 ("kort", r"Hoe hoog moet een tafel staan opdat de val \(1{,}0\) s duurt? Neem \(g = 9{,}81\ \text{m/s}^{2}\).",
                  r"\(4{,}91\) m, uit \(h = \tfrac{1}{2}g\,t^{2}\).", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De valtijd van een horizontale worp hangt af van \(v_{0}\).", False),
                 ("waar", "De baan van een horizontale worp is een parabool.", True),
                 ("waar", "Harder gooien geeft een grotere dracht.", True),
                 ("waar", r"\(v_{x}\) neemt tijdens de worp af door \(g\).", False),
             ]),
        dict(kop="Vergelijken",
             opdracht="Vul aan en kruis daarna het juiste antwoord aan.",
             oefeningen=[
                 ("rij", [("een bal die valt en een die je horizontaal weggooit, van dezelfde hoogte", "samen"),
                          ("twee ballen horizontaal weg van dezelfde hoogte, de ene harder", "samen")],
                  "Wie landt eerst?", WL),
                 ("kies", r"Je verdubbelt \(v_{0}\) én de hoogte. Wat gebeurt er met de dracht?",
                  [r"ze wordt \(2\sqrt{2}\) keer zo groot",
                   "ze wordt twee keer zo groot",
                   "ze wordt vier keer zo groot",
                   r"ze wordt \(\sqrt{2}\) keer zo groot"], 0),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Leg uit waarom de valtijd niet van \(v_{0}\) afhangt.",
                  r"De twee bewegingen zijn onafhankelijk. Verticaal begint de worp met "
                  r"\(v_{0y} = 0\) en werkt enkel \(g\), dus geldt \(t = \sqrt{\dfrac{2h}{g}}\): "
                  r"daar staat geen \(v_{0}\) in.", 5),
                 ("open", "Je verdubbelt de hoogte van de tafel. Wordt de dracht twee keer groter? Leg uit.",
                  r"Nee, maar \(\sqrt{2}\) keer, dus ongeveer \(1{,}4\) keer. In "
                  r"\(x = v_{0}\sqrt{\dfrac{2h}{g}}\) staat \(h\) onder een wortel.", 5),
                 ("open", "Een vliegtuig lost recht boven een doel een pakket. Valt het op het doel? Leg uit.",
                  r"Nee, het valt verderop. Het pakket houdt \(v_{x} = v_{0}\) van het "
                  r"vliegtuig en beschrijft een parabool; de piloot moet daarvóór lossen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-gravitatiekracht-en-de-cirkelbeweging-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gravitatiekracht en de cirkelbeweging",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeveel keer groter of kleiner",
             opdracht=r"De gravitatiekracht was \(60\) N. Schrijf de nieuwe kracht op, met \(F = G\dfrac{m_{1}m_{2}}{r^{2}}\) in gedachten.",
             oefeningen=[
                 ("rij", [(r"\(r\) verdubbelt", r"\(15\) N"),
                          (r"\(m_{1}\) verdubbelt", r"\(120\) N"),
                          (r"\(r\) wordt drie keer groter", r"\(6{,}7\) N")],
                  "Welke kracht nu?", WW),
                 ("rij", [(r"\(m_{1}\) en \(m_{2}\) verdubbelen", r"\(240\) N"),
                          (r"\(r\) halveert", r"\(240\) N"),
                          (r"\(m_{1}\) halveert", r"\(30\) N")],
                  "Welke kracht nu?", WW),
             ]),
        dict(kop="Rekenen aan een cirkelbeweging",
             opdracht=r"Gebruik \(v = \dfrac{2\pi r}{T}\), \(a_{c} = \dfrac{v^{2}}{r} = \omega^{2}r\) en \(F_{c} = m\,a_{c}\).",
             oefeningen=[
                 ("kort", r"Een punt draait op \(r = 0{,}50\) m met \(T = \pi\) s. Hoe groot is \(v\)?",
                  r"\(1{,}0\) m/s, want \(\dfrac{2\pi \times 0{,}50}{\pi}\).", WW),
                 ("kort", r"\(v = 4{,}0\) m/s op een cirkel met \(r = 2{,}0\) m. Hoe groot is \(a_{c}\)?",
                  r"\(8{,}0\ \text{m/s}^{2}\), want \(\dfrac{16}{2{,}0}\).", WW),
                 ("kort", r"\(m = 3{,}0\) kg, \(v = 4{,}0\) m/s, \(r = 2{,}0\) m. Hoe groot is \(F_{c}\)?",
                  r"\(24\) N, want \(3{,}0 \times 8{,}0\).", W),
                 ("kort", r"Een rad draait \(2{,}0\) keer per seconde rond. Hoe groot zijn \(T\) en \(\omega\)?",
                  r"\(T = 0{,}50\) s en \(\omega = 4\pi = 12{,}6\) rad/s.", WW),
                 ("kort", r"Een kind zit op \(1{,}8\) m van het midden van een draaimolen met \(\omega = 1{,}2\) rad/s. Hoe groot is \(a_{c}\)?",
                  r"\(2{,}6\ \text{m/s}^{2}\), want \(\omega^{2}r\).", WW),
             ]),
        dict(kop="Rekenen met de gravitatiewet",
             opdracht=r"Neem \(G = 6{,}67 \times 10^{-11}\ \text{N}\,\text{m}^{2}\text{/kg}^{2}\). Schrijf je antwoord in de wetenschappelijke schrijfwijze.",
             oefeningen=[
                 ("kort", r"Twee massa's van \(1{,}0 \times 10^{3}\) kg staan \(2{,}0\) m uit elkaar. Hoe groot is \(F\)?",
                  r"\(1{,}7 \times 10^{-5}\) N, uit \(G\dfrac{m_{1}m_{2}}{r^{2}}\).", WL),
                 ("kort", r"Een planeet heeft \(M = 6{,}0 \times 10^{24}\) kg en \(R = 6{,}4 \times 10^{6}\) m. Hoe groot is \(g\) aan haar oppervlak?",
                  r"\(9{,}8\ \text{m/s}^{2}\), uit \(\dfrac{GM}{R^{2}}\).", WW),
                 ("kort", r"Een maan draait op \(r = 4{,}0 \times 10^{8}\) m rond die planeet. Hoe groot is haar baansnelheid?",
                  r"\(1{,}0 \times 10^{3}\) m/s, uit \(\sqrt{\dfrac{GM}{r}}\).", WW),
                 ("kort", r"Hoe lang doet die maan over één omloop?",
                  r"\(2{,}5 \times 10^{6}\) s, of ongeveer \(29\) dagen.", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Bij een ECB blijft \(\lvert v \rvert\) constant.", True),
                 ("waar", r"Bij een ECB is \(a = 0\).", False),
                 ("waar", r"\(F_{c}\) wijst naar het middelpunt van de cirkel.", True),
                 ("waar", "Een satelliet in een baan om de aarde ondervindt geen zwaartekracht.", False),
                 ("waar", "Hoe verder een planeet van de zon, hoe langer haar omlooptijd.", True),
             ]),
        dict(kop="Wie levert de kracht?",
             opdracht=r"Schrijf op welke kracht de rol van \(F_{c}\) speelt.",
             oefeningen=[
                 ("rij", [("de maan rond de aarde", "de gravitatiekracht"),
                          ("een auto in een bocht", "de wrijving van de wielen")],
                  "Welke kracht?", WL),
                 ("rij", [("een bal aan een touw rondzwaaien", "de spankracht van het touw"),
                          ("een elektron rond een kern", "de coulombkracht")],
                  "Welke kracht?", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een ECB heeft een constante snelheid in grootte en tóch een versnelling. Leg dat uit.",
                  r"Versnelling is de verandering van \(\vec{v}\), niet alleen van haar grootte. "
                  r"De richting draait voortdurend, en die verandering is "
                  r"\(a_{c} = \dfrac{v^{2}}{r}\), naar het middelpunt gericht.", 5),
                 ("open", "Waarom voelt een astronaut zich gewichtloos, terwijl de zwaartekracht er bijna even groot is als op aarde?",
                  r"Het station en de astronaut vallen samen rond de aarde: de zwaartekracht "
                  r"dient volledig als \(F_{c}\). Er is dus geen vloer die tegen hem duwt, en net "
                  r"die tegenkracht voel je normaal als gewicht.", 5),
                 ("open", "Waarom slipt een auto in een bocht makkelijker bij regen?",
                  r"De bocht vraagt \(F_{c} = \dfrac{m\,v^{2}}{r}\), en die moet van de wrijving "
                  r"komen. Bij regen is die wrijving kleiner, dus volstaat ze niet meer bij "
                  r"dezelfde snelheid.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-arbeid-energie-en-vermogen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Arbeid, energie en vermogen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Arbeid rekenen",
             opdracht=r"Gebruik \(W = F\,s\cos\alpha\). Let op het teken.",
             oefeningen=[
                 ("rij", [(r"\(F = 25\) N, \(s = 4\) m", r"\(W = 100\) J"),
                          (r"\(W = 60\) J, \(s = 3\) m", r"\(F = 20\) N"),
                          (r"\(F = 12\) N, \(W = 72\) J", r"\(s = 6\) m")],
                  "Wat ontbreekt?", WW),
                 ("kort", r"Je duwt een kast \(5{,}0\) m vooruit met \(80\) N. Hoe groot is \(W\)?",
                  r"\(400\) J, want \(80 \times 5{,}0\).", W),
                 ("kort", r"Je houdt een boek van \(20\) N een minuut stil in je hand. Hoe groot is \(W\)?",
                  r"\(0\) J, want \(s = 0\).", WW),
                 ("kort", r"Een kracht van \(20\) N onder \(60^\circ\) trekt een slee \(5{,}0\) m ver. Hoe groot is \(W\)?",
                  r"\(50\) J, want \(20 \times 5{,}0 \times \cos 60^\circ\).", WW),
                 ("kort", r"Een kist schuift \(4{,}0\) m met een wrijvingskracht van \(25\) N. Hoe groot is de arbeid van de wrijving?",
                  r"\(-100\) J; de kracht staat tegen de verplaatsing in.", WW),
             ]),
        dict(kop="Energievormen",
             opdracht=r"Gebruik \(E_{k} = \tfrac{1}{2}m\,v^{2}\), \(E_{p} = m\,g\,h\) en \(E_{\text{veer}} = \tfrac{1}{2}k\,x^{2}\), met \(g = 10\ \text{N/kg}\).",
             oefeningen=[
                 ("kort", r"\(m = 2{,}0\) kg op \(5{,}0\) m hoogte. Hoe groot is \(E_{p}\)?",
                  r"\(100\) J, want \(2{,}0 \times 10 \times 5{,}0\).", W),
                 ("kort", r"\(m = 4{,}0\) kg met \(v = 3{,}0\) m/s. Hoe groot is \(E_{k}\)?",
                  r"\(18\) J, want \(\tfrac{1}{2} \times 4{,}0 \times 9{,}0\).", W),
                 ("kort", r"Een veer met \(k = 200\) N/m wordt \(0{,}10\) m uitgerekt. Hoe groot is \(E_{\text{veer}}\)?",
                  r"\(1{,}0\) J, want \(\tfrac{1}{2} \times 200 \times 0{,}010\).", WW),
                 ("kort", r"Een auto van \(1{,}2 \times 10^{3}\) kg rijdt \(25\) m/s. Hoe groot is \(E_{k}\)?",
                  r"\(3{,}75 \times 10^{5}\) J, dus ongeveer \(375\) kJ.", WW),
                 ("kort", r"Hoe verandert \(E_{k}\) als \(v\) verdubbelt?",
                  r"Vier keer zo groot, want \(v\) staat in het kwadraat.", WL),
             ]),
        dict(kop="Behoud van energie",
             opdracht=r"Neem \(g = 10\ \text{N/kg}\) en verwaarloos de wrijving.",
             oefeningen=[
                 ("kort", r"Een bal van \(1{,}0\) kg valt van \(20\) m. Hoe groot is \(v\) bij de grond?",
                  r"\(20\) m/s, uit \(v = \sqrt{2gh} = \sqrt{400}\).", WW),
                 ("kort", r"Een slee glijdt van een heuvel van \(8{,}0\) m. Hoe groot is \(v\) beneden?",
                  r"\(12{,}6\) m/s, uit \(\sqrt{160}\); de massa valt weg.", WW),
                 ("kort", r"Een wagentje met \(v = 6{,}0\) m/s rijdt een helling op. Hoe hoog raakt het?",
                  r"\(1{,}8\) m, uit \(h = \dfrac{v^{2}}{2g}\).", WW),
                 ("open", "Een slinger zwaait heen en weer. Beschrijf hoe de energie onderweg verandert.",
                  r"In de uiterste standen staat hij stil en is alles \(E_{p}\). Onderweg naar het "
                  r"midden zet die om in \(E_{k}\): in het laagste punt is de snelheid maximaal en "
                  r"\(E_{p}\) minimaal. De som blijft gelijk zolang er geen wrijving is.", 6),
             ]),
        dict(kop="Het arbeid-energietheorema",
             opdracht=r"Gebruik \(W_{\text{tot}} = \Delta E_{k}\).",
             oefeningen=[
                 ("kort", r"Een kar van \(3{,}0\) kg vertrekt uit rust en krijgt \(150\) J arbeid. Hoe groot is \(v\)?",
                  r"\(10\) m/s, uit \(\tfrac{1}{2} \times 3{,}0 \times v^{2} = 150\).", WW),
                 ("kort", r"Een auto van \(1{,}0 \times 10^{3}\) kg remt van \(20\) m/s tot stilstand. Hoe groot is \(W_{\text{tot}}\)?",
                  r"\(-2{,}0 \times 10^{5}\) J; de arbeid is negatief.", WW),
                 ("kort", r"Die auto staat stil na \(50\) m. Hoe groot is de remkracht?",
                  r"\(4{,}0 \times 10^{3}\) N, uit \(\dfrac{2{,}0 \times 10^{5}}{50}\).", WW),
             ]),
        dict(kop="Vermogen en rendement",
             opdracht=r"Gebruik \(P = \dfrac{W}{t}\).",
             oefeningen=[
                 ("rij", [(r"\(W = 900\) J in \(3{,}0\) s", r"\(300\) W"),
                          (r"\(P = 500\) W, \(t = 20\) s", r"\(W = 10^{4}\) J"),
                          (r"\(W = 1{,}2\) kJ, \(P = 300\) W", r"\(t = 4{,}0\) s")],
                  "Wat ontbreekt?", WW),
                 ("kort", r"Een lift tilt \(1{,}5 \times 10^{4}\) N over \(12\) m in \(30\) s. Hoe groot is \(P\)?",
                  r"\(6{,}0 \times 10^{3}\) W, want \(W = 1{,}8 \times 10^{5}\) J.", WW),
                 ("kort", r"Een motor krijgt \(1000\) J en levert \(250\) J nuttige arbeid. Hoe groot is het rendement?",
                  r"\(25\ \%\), want \(\dfrac{250}{1000}\).", W),
                 ("kort", r"Hoeveel joule is \(1\) kWh?",
                  r"\(3{,}6 \times 10^{6}\) J, want \(1000 \times 3600\).", WW),
                 ("kort", r"Een fietser levert \(150\) W gedurende \(10\) minuten. Hoe groot is \(W\)?",
                  r"\(9{,}0 \times 10^{4}\) J, want \(150 \times 600\).", WW),
                 ("kort", r"Een lamp van \(60\) W brandt \(5{,}0\) uur. Hoeveel kWh verbruikt ze?",
                  r"\(0{,}30\) kWh, want \(0{,}060 \times 5{,}0\).", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een kracht loodrecht op de beweging verricht geen arbeid.", True),
                 ("waar", "Het rendement van een echte machine kan 100 % zijn.", False),
                 ("waar", "De zwaartekracht is een conservatieve kracht.", True),
                 ("waar", "De arbeid van de wrijvingskracht hangt niet van de gevolgde weg af.", False),
                 ("waar", r"De oppervlakte onder een \(F(x)\)-grafiek is de verrichte arbeid.", True),
                 ("waar", r"Wie een doos sneller even hoog tilt, verricht daardoor meer arbeid.", False),
                 ("waar", r"Een joule is hetzelfde als een newtonmeter.", True),
                 ("waar", r"Een kilowattuur is een eenheid van vermogen.", False),
             ]),
        dict(kop="Arbeid of geen arbeid",
             opdracht="Schrijf op of er arbeid verricht wordt, en waarom.",
             oefeningen=[
                 ("rij", [("een kelner draagt een blad horizontaal", "geen arbeid, loodrecht"),
                          ("de normaalkracht op een schuivende kist", "geen arbeid, loodrecht"),
                          ("je duwt tegen een muur die niet wijkt", r"geen arbeid, \(s = 0\)")],
                  "Arbeid of niet?", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je draagt een boodschappentas horizontaal over 20 m. Verricht je arbeid op de tas? Leg uit.",
                  r"Op de tas niet: je kracht wijst naar boven en de verplaatsing is horizontaal, "
                  r"dus is \(\alpha = 90^\circ\) en \(\cos\alpha = 0\). Je spieren verbruiken wel "
                  r"energie, maar dat is iets anders dan arbeid op de tas.", 5),
                 ("open", "Leg uit wat een conservatieve kracht is, met een voorbeeld.",
                  r"Een kracht waarvan de arbeid alleen van het begin- en eindpunt afhangt en niet "
                  r"van de weg ertussen. De zwaartekracht is er een: of je recht omhoog klimt of "
                  r"via een lange helling, de arbeid is dezelfde.", 5),
                 ("open", r"Waarom reken je bij een veerkracht met \(\int F\,\mathrm{d}x\) en niet met \(F\,s\)?",
                  r"De veerkracht \(F = k\,x\) verandert onderweg, dus er is geen vaste \(F\) om "
                  r"mee te vermenigvuldigen. De arbeid is dan de oppervlakte onder de "
                  r"\(F(x)\)-grafiek, en die reken je met een integraal.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-gaswetten-en-de-algemene-gaswet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gaswetten en de algemene gaswet",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk proces?",
             opdracht="Schrijf isotherm, isobaar of isochoor.",
             oefeningen=[
                 ("rij", [(r"\(T\) blijft gelijk", "isotherm"),
                          (r"\(p\) blijft gelijk", "isobaar"),
                          (r"\(V\) blijft gelijk", "isochoor")],
                  "Welk proces?", WW),
                 ("rij", [("een gesloten metalen vat verwarmen", "isochoor"),
                          ("een ballon in de zon leggen", "isobaar"),
                          ("een spuit traag indrukken bij kamertemperatuur", "isotherm")],
                  "Welk proces?", WW),
                 ("rij", [(r"\(p\,V = \text{cte}\)", "isotherm"),
                          (r"\(\dfrac{V}{T} = \text{cte}\)", "isobaar"),
                          (r"\(\dfrac{p}{T} = \text{cte}\)", "isochoor")],
                  "Bij welk proces hoort deze wet?", WW),
             ]),
        dict(kop="Temperatuur omrekenen",
             opdracht=r"Gebruik \(T(\text{K}) = \theta(^\circ\text{C}) + 273\).",
             oefeningen=[
                 ("rij", [(r"\(27\ ^\circ\text{C}\)", r"\(300\) K"),
                          (r"\(-73\ ^\circ\text{C}\)", r"\(200\) K"),
                          (r"\(127\ ^\circ\text{C}\)", r"\(400\) K")],
                  "Hoeveel kelvin?", WW),
                 ("rij", [(r"\(500\) K", r"\(227\ ^\circ\text{C}\)"),
                          (r"\(273\) K", r"\(0\ ^\circ\text{C}\)"),
                          (r"\(350\) K", r"\(77\ ^\circ\text{C}\)")],
                  "Hoeveel graden celsius?", WW),
             ]),
        dict(kop="Rekenen met de drie gaswetten",
             opdracht="Reken uit. Vul de temperatuur altijd in kelvin in.",
             oefeningen=[
                 ("kort", r"Isotherm: \(3{,}0\) L bij \(100\) kPa wordt samengeperst tot \(1{,}0\) L. Welke druk?",
                  r"\(300\) kPa, uit \(p_{1}V_{1} = p_{2}V_{2}\).", WW),
                 ("kort", r"Isobaar: \(2{,}0\) L bij \(300\) K wordt opgewarmd tot \(450\) K. Welk volume?",
                  r"\(3{,}0\) L, uit \(\dfrac{V_{1}}{T_{1}} = \dfrac{V_{2}}{T_{2}}\).", WW),
                 ("kort", r"Isochoor: \(200\) kPa bij \(250\) K wordt opgewarmd tot \(500\) K. Welke druk?",
                  r"\(400\) kPa, uit \(\dfrac{p_{1}}{T_{1}} = \dfrac{p_{2}}{T_{2}}\).", WW),
                 ("kort", r"Isotherm: \(500\) mL bij \(2{,}0\) bar wordt samengeperst tot \(4{,}0\) bar. Welk volume?",
                  r"\(250\) mL; de druk verdubbelt, dus het volume halveert.", WW),
                 ("kort", r"Isobaar: \(1{,}5\) L bij \(27\ ^\circ\text{C}\) wordt tot \(127\ ^\circ\text{C}\) verwarmd. Welk volume?",
                  r"\(2{,}0\) L, uit \(\dfrac{1{,}5 \times 400}{300}\).", WW),
             ]),
        dict(kop="De algemene en de ideale gaswet",
             opdracht=r"Gebruik \(\dfrac{p\,V}{T} = \text{cte}\) en \(p\,V = n\,R\,T\) met \(R = 8{,}31\).",
             oefeningen=[
                 ("kort", r"Van \(2{,}0\) L bij \(100\) kPa en \(300\) K naar \(400\) K bij \(200\) kPa. Welk volume?",
                  r"\(1{,}33\) L, uit \(\dfrac{100 \times 2{,}0 \times 400}{300 \times 200}\).", WW),
                 ("kort", r"Van \(4{,}0\) L bij \(200\) kPa en \(400\) K naar \(2{,}0\) L bij \(300\) K. Welke druk?",
                  r"\(300\) kPa, uit \(\dfrac{200 \times 4{,}0 \times 300}{400 \times 2{,}0}\).", WW),
                 ("kort", r"Hoeveel mol zit er in \(0{,}025\ \text{m}^{3}\) bij \(300\) K en \(100\) kPa?",
                  r"\(1{,}0\) mol, uit \(n = \dfrac{p\,V}{R\,T}\).", WW),
                 ("kort", r"Welk volume neemt \(2{,}0\) mol gas in bij \(300\) K en \(100\) kPa?",
                  r"\(0{,}050\ \text{m}^{3}\), dus \(50\) L.", WW),
                 ("kort", r"Hoeveel liter neemt \(1\) mol in bij normomstandigheden?",
                  r"\(22{,}4\) L, bij \(0\ ^\circ\text{C}\) en \(101{,}3\) kPa.", WW),
             ]),
        dict(kop="Welke grafiek hoort erbij?",
             opdracht="Schrijf op welke vorm de grafiek heeft.",
             oefeningen=[
                 ("rij", [(r"\(p(V)\) bij constante \(T\)", "een dalende hyperbool"),
                          (r"\(V(T)\) bij constante \(p\)", "een rechte door de oorsprong"),
                          (r"\(p(T)\) bij constante \(V\)", "een rechte door de oorsprong")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Wat gebeurt er dan?",
             opdracht="Schrijf op wat de derde grootheid doet.",
             oefeningen=[
                 ("rij", [(r"\(p\) verdubbelt bij constante \(T\)", r"\(V\) halveert"),
                          (r"\(T\) verdubbelt bij constante \(p\)", r"\(V\) verdubbelt"),
                          (r"\(V\) halveert bij constante \(T\)", r"\(p\) verdubbelt")],
                  "En dan?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In de gaswetten mag je de temperatuur in graden celsius invullen.", False),
                 ("waar", r"Bij constante \(T\) zijn \(p\) en \(V\) omgekeerd evenredig.", True),
                 ("waar", "Bij een ideaal gas verwaarloost men het eigen volume van de moleculen.", True),
                 ("waar", "De druk van een gas komt van de botsingen van de moleculen op de wand.", True),
                 ("waar", r"Bij \(0\) K beweegt een gasmolecule nog even snel als bij kamertemperatuur.", False),
                 ("waar", r"De gasconstante \(R\) heeft voor elk gas dezelfde waarde.", True),
                 ("waar", "Een reëel gas wijkt het meest van de ideale gaswet af bij hoge temperatuur en lage druk.", False),
                 ("waar", r"In \(p\,V = n\,R\,T\) vul je \(V\) in kubieke meter in.", True),
                 ("waar", "Bij een isobaar proces blijft het volume constant.", False),
                 ("waar", "Eén mol van een zwaar gas neemt bij normomstandigheden meer plaats in dan één mol van een licht gas.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg met het deeltjesmodel uit waarom de druk stijgt als je een gas verwarmt bij constant volume.",
                  "Bij een hogere temperatuur bewegen de moleculen sneller. Ze botsen dus vaker en "
                  "harder op de wand, en die botsingen samen zijn net de druk.", 5),
                 ("open", "Waarom staat er op een spuitbus dat je ze niet in het vuur mag gooien?",
                  r"Het volume staat vast, dus stijgt de druk mee met \(T\). Boven een zekere "
                  r"druk houdt de bus het niet en ontploft ze.", 5),
                 ("open", "Waarom gebruik je in de gaswetten kelvin en niet celsius?",
                  "De wetten zijn verhoudingen, en die gelden enkel vanaf een echt nulpunt. De "
                  "celsiusschaal heeft haar nul bij het smeltpunt van water, dus zou een "
                  "verdubbeling van de temperatuur daar niets betekenen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-warmteleer-temperatuur-warmte-en-faseovergangen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Warmteleer: temperatuur, warmte en faseovergangen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke faseovergang?",
             opdracht="Schrijf de naam van de overgang.",
             oefeningen=[
                 ("rij", [("vast naar vloeibaar", "smelten"), ("gas naar vloeistof", "condenseren"),
                          ("vast naar gas", "sublimeren")],
                  "Welke overgang?", WW),
                 ("rij", [("vloeibaar naar vast", "stollen"), ("vloeistof naar gas", "verdampen"),
                          ("gas naar vast", "rijpen")],
                  "Welke overgang?", WW),
             ]),
        dict(kop="Warmte opnemen of afgeven",
             opdracht="Schrijf opnemen of afgeven.",
             oefeningen=[
                 ("rij", [("smelten", "opnemen"), ("stollen", "afgeven"), ("verdampen", "opnemen")],
                  "Warmte opnemen of afgeven?", WW),
                 ("rij", [("condenseren", "afgeven"), ("sublimeren", "opnemen"), ("rijpen", "afgeven")],
                  "Warmte opnemen of afgeven?", WW),
             ]),
        dict(kop=r"Rekenen met \(Q = c\,m\,\Delta T\)",
             opdracht=r"Neem \(c_{\text{water}} = 4186\ \text{J/(kg}\cdot\text{K)}\).",
             oefeningen=[
                 ("kort", r"Hoeveel warmte heb je nodig om \(3{,}0\) kg water \(20\) K op te warmen?",
                  r"\(2{,}51 \times 10^{5}\) J, want \(4186 \times 3{,}0 \times 20\).", WW),
                 ("kort", r"\(0{,}50\) kg water krijgt \(4{,}186 \times 10^{4}\) J. Hoeveel stijgt \(T\)?",
                  r"\(20\) K, uit \(\Delta T = \dfrac{Q}{c\,m}\).", WW),
                 ("kort", r"Hoeveel warmte vraagt \(1{,}0\) kg ijzer \(10\) K opwarmen? Neem \(c = 450\).",
                  r"\(4{,}5 \times 10^{3}\) J, want \(450 \times 1{,}0 \times 10\).", WW),
                 ("kort", r"Een blok van \(2{,}0\) kg met \(c = 900\) krijgt \(36\) kJ. Hoeveel stijgt \(T\)?",
                  r"\(20\) K, uit \(\dfrac{36000}{900 \times 2{,}0}\).", WW),
                 ("kort", r"Welke \(c\) heeft een stof als \(0{,}50\) kg \(8{,}0\) kJ nodig heeft voor \(20\) K?",
                  r"\(800\ \text{J/(kg}\cdot\text{K)}\), uit \(c = \dfrac{Q}{m\,\Delta T}\).", WW),
             ]),
        dict(kop=r"Rekenen met \(Q = l\,m\)",
             opdracht=r"Voor water: \(l_{\text{smelten}} = 334\) kJ/kg en \(l_{\text{verdampen}} = 2256\) kJ/kg.",
             oefeningen=[
                 ("kort", r"Hoeveel warmte vraagt het smelten van \(2{,}0\) kg ijs van \(0\ ^\circ\text{C}\)?",
                  r"\(668\) kJ, want \(334 \times 2{,}0\).", W),
                 ("kort", r"Hoeveel warmte vraagt het verdampen van \(0{,}50\) kg water van \(100\ ^\circ\text{C}\)?",
                  r"\(1128\) kJ, want \(2256 \times 0{,}50\).", W),
                 ("kort", r"Hoeveel ijs van \(0\ ^\circ\text{C}\) smelt er met \(167\) kJ?",
                  r"\(0{,}50\) kg, uit \(m = \dfrac{Q}{l}\).", WW),
                 ("kort", r"Hoeveel warmte geeft \(1{,}0\) kg water af bij het stollen tot ijs?",
                  r"\(334\) kJ; stollen is de omgekeerde weg van smelten.", WW),
             ]),
        dict(kop="In twee stappen",
             opdracht=r"Eerst opwarmen met \(Q = c\,m\,\Delta T\), dan de faseovergang met \(Q = l\,m\). Tel op.",
             oefeningen=[
                 ("kort", r"\(1{,}0\) kg water van \(80\) naar \(100\ ^\circ\text{C}\) brengen en volledig laten verdampen. Hoeveel warmte?",
                  r"\(2340\) kJ: \(84\) kJ opwarmen en \(2256\) kJ verdampen.", WL),
                 ("kort", r"\(0{,}20\) kg ijs van \(0\ ^\circ\text{C}\) smelten en het water tot \(20\ ^\circ\text{C}\) brengen. Hoeveel warmte?",
                  r"\(84\) kJ: \(67\) kJ smelten en \(17\) kJ opwarmen.", WL),
             ]),
        dict(kop="De curve lezen",
             opdracht="Schrijf op wat er op dat stuk van de verwarmingscurve gebeurt.",
             oefeningen=[
                 ("rij", [("een stijgend stuk", "de stof warmt op"),
                          ("een vlak stuk", "een faseovergang"),
                          ("een tweede vlak stuk", "de tweede faseovergang")],
                  "Wat gebeurt er?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Warmte en temperatuur zijn hetzelfde.", False),
                 ("waar", "Warmte stroomt spontaan van warm naar koud.", True),
                 ("waar", r"Water heeft een hoge \(c\) in vergelijking met metalen.", True),
                 ("waar", "Bij een lagere luchtdruk kookt water bij een hogere temperatuur.", False),
                 ("waar", r"Een stijging van \(10\) K is even groot als een stijging van \(10\ ^\circ\text{C}\).", True),
                 ("waar", r"Een voorwerp van \(1000\) K bevat altijd meer warmte dan een voorwerp van \(300\) K.", False),
                 ("waar", r"In \(Q = l\,m\) staat geen \(\Delta T\), want de temperatuur verandert niet.", True),
                 ("waar", "Een mengsel heeft net als een zuivere stof één scherp smeltpunt.", False),
                 ("waar", "Een calorimeter moet zo goed mogelijk geïsoleerd zijn.", True),
                 ("waar", "Sublimeren is de overgang van gas rechtstreeks naar vast.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de temperatuur tijdens het smelten niet stijgt.",
                  "Alle toegevoerde warmte gaat naar het losmaken van de deeltjes uit het rooster, "
                  "niet naar het sneller doen bewegen ervan. Pas als alles vloeibaar is, stijgt de "
                  "temperatuur weer.", 4),
                 ("open", "Waarom koelt zweten je af?",
                  "Het verdampen van water vraagt veel warmte, en die haalt het zweet uit je huid. "
                  "Je huid verliest dus energie en koelt af.", 4),
                 ("open", "Wat houdt het vacuüm in een thermosfles tegen, en wat de spiegelende wand?",
                  "Het vacuüm heeft geen deeltjes, dus kan er geen warmte geleid of gestroomd "
                  "worden. De spiegelende wand kaatst de warmtestraling terug, en dat is de derde "
                  "weg die anders overblijft.", 4),
                 ("open", "Waarom werkt zout op een besneeuwde weg niet bij strenge vorst?",
                  "Zout verlaagt het smeltpunt van het ijs, dus smelt het ook onder nul graden. Bij "
                  "strenge vorst zakt de temperatuur onder het verlaagde smeltpunt, en dan bevriest "
                  "de pekel toch.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-harmonische-trillingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Harmonische trillingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Periode en frequentie",
             opdracht=r"Gebruik \(f = \dfrac{1}{T}\).",
             oefeningen=[
                 ("rij", [(r"\(T = 0{,}5\) s", r"\(f = 2\) Hz"),
                          (r"\(f = 50\) Hz", r"\(T = 0{,}02\) s"),
                          (r"\(T = 0{,}2\) s", r"\(f = 5\) Hz")],
                  "Wat ontbreekt?", WW),
                 ("rij", [(r"\(f = 4\) Hz", r"\(T = 0{,}25\) s"),
                          (r"\(T = 2\) s", r"\(f = 0{,}5\) Hz"),
                          (r"\(f = 10\) Hz", r"\(T = 0{,}1\) s")],
                  "Wat ontbreekt?", WW),
             ]),
        dict(kop="Pulsatie",
             opdracht=r"Gebruik \(\omega = \dfrac{2\pi}{T} = 2\pi f\). Neem \(\pi = 3{,}14\).",
             oefeningen=[
                 ("rij", [(r"\(T = 2{,}0\) s", r"\(\omega = 3{,}14\) rad/s"),
                          (r"\(f = 5{,}0\) Hz", r"\(\omega = 31{,}4\) rad/s"),
                          (r"\(\omega = 6{,}28\) rad/s", r"\(T = 1{,}0\) s")],
                  "Wat ontbreekt?", WL),
             ]),
        dict(kop="Uit de trillingsvergelijking lezen",
             opdracht=r"Er geldt \(y = 0{,}04\sin(10\,t)\). Antwoord met eenheid.",
             oefeningen=[
                 ("kort", r"Hoe groot is \(A\)?", r"\(0{,}04\) m, dus \(4\) cm.", W),
                 ("kort", r"Hoe groot is \(\omega\)?", r"\(10\) rad/s.", W),
                 ("kort", r"Hoe groot is \(\varphi\)?",
                  r"\(0\) rad; ze vertrekt uit het evenwicht.", WW),
                 ("kort", r"Hoe groot is \(T\)? Neem \(\pi = 3{,}14\).",
                  r"\(0{,}63\) s, uit \(T = \dfrac{2\pi}{\omega}\).", WW),
                 ("kort", r"Hoe groot is de uitwijking na een halve periode?",
                  r"\(0\) m, want de fase is dan \(\pi\) en \(\sin \pi = 0\).", WW),
             ]),
        dict(kop="De eigenfrequentie",
             opdracht="Schrijf hoger, lager of gelijk.",
             oefeningen=[
                 ("rij", [("een stijvere veer bij dezelfde massa", "hoger"),
                          ("een grotere massa aan dezelfde veer", "lager"),
                          ("een grotere amplitude bij dezelfde veer", "gelijk")],
                  "Eigenfrequentie?", WW),
                 ("rij", [("een langere slinger", "lager"),
                          ("een zwaardere bol aan dezelfde slinger", "gelijk"),
                          ("dezelfde slinger op de maan", "lager")],
                  "Eigenfrequentie?", WW),
                 ("rij", [(r"\(m\) wordt vier keer zo groot", r"\(f_{0}\) halveert"),
                          (r"\(k\) wordt vier keer zo groot", r"\(f_{0}\) verdubbelt"),
                          (r"\(m\) verdubbelt", r"\(f_{0}\) deelt door \(\sqrt{2}\)")],
                  r"Wat doet \(f_{0}\)?", WL),
             ]),
        dict(kop="Waar staat wat maximaal?",
             opdracht="Schrijf in het evenwicht of in de uiterste stand.",
             oefeningen=[
                 ("rij", [("de snelheid is maximaal", "in het evenwicht"),
                          ("de versnelling is maximaal", "in de uiterste stand"),
                          ("de uitwijking is nul", "in het evenwicht")],
                  "Waar?", WL),
                 ("rij", [("de terugroepkracht is nul", "in het evenwicht"),
                          ("de snelheid is nul", "in de uiterste stand"),
                          (r"\(y\) is gelijk aan \(A\)", "in de uiterste stand")],
                  "Waar?", WL),
             ]),
        dict(kop="In fase of in tegenfase",
             opdracht="Schrijf in fase, in tegenfase of geen van beide.",
             oefeningen=[
                 ("rij", [(r"\(\Delta\varphi = 0\)", "in fase"),
                          (r"\(\Delta\varphi = \pi\)", "in tegenfase"),
                          (r"\(\Delta\varphi = \tfrac{\pi}{2}\)", "geen van beide")],
                  "Hoe trillen ze?", WL),
             ]),
        dict(kop="Welke eenheid?",
             opdracht="Schrijf de eenheid van de grootheid op.",
             oefeningen=[
                 ("rij", [(r"\(A\)", "meter"), (r"\(T\)", "seconde"),
                          (r"\(\omega\)", "radiaal per seconde")],
                  "Welke eenheid?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De amplitude van een trilling kan negatief zijn.", False),
                 ("waar", r"Twee trillingen met \(\Delta\varphi = \pi\) zijn in tegenfase.", True),
                 ("waar", "Bij een gedempte trilling neemt vooral de frequentie snel af.", False),
                 ("waar", "Bij resonantie kan een kleine kracht een grote amplitude geven.", True),
                 ("waar", "De periode van een harmonische trilling hangt af van de amplitude.", False),
                 ("waar", r"De pulsatie \(\omega\) staat in radiaal per seconde.", True),
                 ("waar", "De eigenfrequentie van een slinger hangt af van de massa van de bol.", False),
                 ("waar", r"In \(y = A\sin(\omega t + \varphi)\) staat de massa van het lichaam niet.", True),
                 ("waar", "Bij een gedwongen trilling neemt het lichaam de frequentie van de kracht over.", True),
                 ("waar", r"De beginfase \(\varphi\) staat in meter.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat resonantie is en geef één voorbeeld.",
                  "Resonantie treedt op als de frequentie van een aandrijvende kracht de "
                  "eigenfrequentie van het lichaam benadert; dan loopt de amplitude sterk op. Een "
                  "schommel die je telkens op het juiste ogenblik duwt, gaat zo steeds hoger.", 4),
                 ("open", "Waarom zet men dempers in een gebouw dat tegen aardbevingen moet kunnen?",
                  "Een aardbeving kan het gebouw op zijn eigenfrequentie aandrijven, en dan wordt de "
                  "amplitude gevaarlijk groot. Dempers halen energie uit de trilling, zodat die "
                  "amplitude beperkt blijft.", 4),
                 ("open", "Waarom was een slingeruurwerk nauwkeurig, ook bij een kleinere uitslag?",
                  r"Bij een kleine uitslag hangt de periode alleen van \(\ell\) en \(g\) af, niet "
                  r"van de amplitude. Een kleinere uitslag verandert het ritme dus bijna niet.", 4),
                 ("open", "Wat gebeurt er met de energie van een gedempte trilling?",
                  "Wrijving en luchtweerstand maken er warmte van, die naar de omgeving verdwijnt. "
                  "Het behoud van energie blijft gelden; de energie zit alleen niet meer in de "
                  "trilling.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-golven-en-hun-eigenschappen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Golven en hun eigenschappen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop=r"Rekenen met \(v = \lambda\,f\)",
             opdracht="Reken uit. Schrijf de eenheid erbij.",
             oefeningen=[
                 ("rij", [(r"\(\lambda = 4\) m, \(f = 25\) Hz", r"\(v = 100\) m/s"),
                          (r"\(v = 340\) m/s, \(f = 170\) Hz", r"\(\lambda = 2\) m"),
                          (r"\(v = 12\) m/s, \(\lambda = 3\) m", r"\(f = 4\) Hz")],
                  "Wat ontbreekt?", WL),
                 ("kort", r"Geluid loopt \(340\) m/s. Welke golflengte hoort bij \(1700\) Hz?",
                  r"\(0{,}20\) m, uit \(\lambda = \dfrac{v}{f}\).", WW),
                 ("kort", r"Licht loopt \(3{,}0 \times 10^{8}\) m/s. Welke frequentie hoort bij \(\lambda = 600\) nm?",
                  r"\(5{,}0 \times 10^{14}\) Hz, uit \(\dfrac{3{,}0 \times 10^{8}}{6{,}0 \times 10^{-7}}\).", WL),
                 ("kort", r"Een golf heeft \(T = 0{,}20\) s en \(\lambda = 1{,}5\) m. Hoe snel loopt ze?",
                  r"\(7{,}5\) m/s, uit \(v = \dfrac{\lambda}{T}\).", WW),
             ]),
        dict(kop="Golfgetal en pulsatie",
             opdracht=r"Gebruik \(k = \dfrac{2\pi}{\lambda}\) en \(\omega = \dfrac{2\pi}{T}\). Neem \(\pi = 3{,}14\).",
             oefeningen=[
                 ("rij", [(r"\(\lambda = 2{,}0\) m", r"\(k = 3{,}14\) rad/m"),
                          (r"\(T = 0{,}50\) s", r"\(\omega = 12{,}6\) rad/s"),
                          (r"\(k = 6{,}28\) rad/m", r"\(\lambda = 1{,}0\) m")],
                  "Wat ontbreekt?", WL),
                 ("kort", r"Uit \(y = 0{,}02\sin(20\,t - 4\,x)\): hoe groot zijn \(A\), \(\omega\) en \(k\)?",
                  r"\(A = 0{,}02\) m, \(\omega = 20\) rad/s, \(k = 4\) rad/m.", WL),
             ]),
        dict(kop="Transversaal of longitudinaal",
             opdracht="Schrijf transversaal of longitudinaal.",
             oefeningen=[
                 ("rij", [("geluid in de lucht", "longitudinaal"), ("licht", "transversaal"),
                          ("een golf op een touw", "transversaal")],
                  "Welk soort golf?", WW),
             ]),
        dict(kop="Welke eigenschap?",
             opdracht="Schrijf reflectie, refractie, diffractie of interferentie.",
             oefeningen=[
                 ("rij", [("een echo tegen een rotswand", "reflectie"),
                          ("een rietje dat geknikt lijkt in water", "refractie"),
                          ("geluid dat rond een hoek komt", "diffractie")],
                  "Welke eigenschap?", WW),
                 ("rij", [("twee golven die elkaar uitdoven", "interferentie"),
                          ("een golf die langzamer gaat in een andere stof", "refractie"),
                          ("een staande golf op een snaar", "interferentie")],
                  "Welke eigenschap?", WW),
             ]),
        dict(kop="Wat verandert bij breking?",
             opdracht="Schrijf verandert of blijft gelijk.",
             oefeningen=[
                 ("rij", [(r"de frequentie \(f\)", "blijft gelijk"),
                          (r"de golflengte \(\lambda\)", "verandert"),
                          (r"de snelheid \(v\)", "verandert")],
                  "Bij breking?", WW),
                 ("kort", r"Licht gaat van lucht naar glas met \(n = 1{,}5\). Hoe snel loopt het in dat glas?",
                  r"\(2{,}0 \times 10^{8}\) m/s, uit \(v = \dfrac{c}{n}\).", WW),
                 ("kort", r"Buigt de straal dan naar de normaal toe of ervan weg?",
                  r"Naar de normaal toe; \(n\) is er groter.", WW),
                 ("kort", r"Een golf loopt in stof 1 met \(2{,}4 \times 10^{8}\) m/s en in stof 2 met \(2{,}0 \times 10^{8}\) m/s. Welke brekingsindex heeft stof 2?",
                  r"\(n = 1{,}5\), uit \(n = \dfrac{3{,}0 \times 10^{8}}{2{,}0 \times 10^{8}}\).", WL),
                 ("kort", r"Licht valt onder \(30^\circ\) op water. Is \(\sin r\) groter of kleiner dan \(\sin i\)?",
                  r"Kleiner: \(\sin r = \dfrac{\sin 30^\circ}{1{,}33} \approx 0{,}38\).", WL),
             ]),
        dict(kop="Interferentie en staande golven",
             opdracht="Vul aan of reken uit.",
             oefeningen=[
                 ("rij", [("twee golven, top op top", "versterking"),
                          ("twee golven, top op dal", "uitdoving"),
                          (r"faseverschil \(\pi\)", "uitdoving")],
                  "Versterking of uitdoving?", WW),
                 ("kort", r"Een snaar van \(0{,}60\) m trilt in haar grondtoon. Hoe groot is \(\lambda\)?",
                  r"\(1{,}20\) m; de snaar is een halve golflengte lang.", WW),
                 ("kort", "Hoeveel knopen telt die snaar in haar grondtoon?",
                  "Twee, één aan elk uiteinde.", WW),
                 ("kort", r"Tussen twee knopen ligt \(0{,}25\) m. Hoe groot is \(\lambda\)?",
                  r"\(0{,}50\) m; tussen twee knopen ligt een halve golflengte.", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een golf vervoert energie zonder materie te verplaatsen.", True),
                 ("waar", "Een golf met een grotere amplitude loopt sneller.", False),
                 ("waar", "Een knoop van een staande golf trilt helemaal niet.", True),
                 ("waar", "Alle deeltjes van een lopende golf beginnen samen te trillen.", False),
                 ("waar", r"In \(y = A\sin(\omega t - k\,x)\) hoort het minteken bij een rechtslopende golf.", True),
                 ("waar", "Bij breking verandert ook de frequentie van de golf.", False),
                 ("waar", "Twee coherente bronnen hebben dezelfde frequentie en een vast faseverschil.", True),
                 ("waar", "Geluid kan door het vacuüm van de ruimte lopen.", False),
                 ("waar", "Een golf buigt af achter een smalle opening.", True),
                 ("waar", "De afstand tussen twee knopen is één hele golflengte.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Een bron trilt \(5{,}0\) s en de golf loopt \(4{,}0\) m/s. Hoelang trilt een punt op \(12\) m?",
                  r"\(2{,}0\) s. De golf had \(\dfrac{12}{4{,}0} = 3{,}0\) s nodig om er te "
                  r"komen, en dus trilt het deeltje \(5{,}0 - 3{,}0\) s.", 4),
                 ("open", "Leg uit waarom je het gebrom van een feest verder hoort dan de hoge tonen.",
                  r"Lage tonen hebben een grote \(\lambda\) en buigen daardoor veel beter af rond "
                  r"huizen en hoeken. Hoge tonen met een kleine \(\lambda\) worden tegengehouden.", 4),
                 ("open", "Wat zegt het principe van Huygens, en wat verklaar je ermee?",
                  "Elk punt van een golffront werkt zelf als een nieuwe bron van golfjes. Daarmee "
                  "verklaar je weerkaatsing, breking en buiging in één keer.", 4),
                 ("open", "Hoe ontstaat een staande golf, en wat is een knoop?",
                  "Een staande golf ontstaat door interferentie van een golf met haar eigen "
                  "weerkaatsing. Een knoop is een punt waar de twee golven elkaar altijd "
                  "opheffen, dus waar niets beweegt.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-licht-geluid-en-het-elektromagnetisch-spectrum-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Licht, geluid en het elektromagnetisch spectrum",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het spectrum ordenen",
             opdracht="Schrijf de nummers 1 tot 7 van de laagste naar de hoogste frequentie.",
             oefeningen=[
                 ("tabel", ["straling", "plaats 1 tot 7"],
                  [["gammastraling", None], ["radiogolven", None], ["infrarood", None],
                   ["röntgenstraling", None], ["microgolven", None], ["zichtbaar licht", None],
                   ["uv-straling", None]],
                  "radiogolven 1 · microgolven 2 · infrarood 3 · zichtbaar licht 4 · "
                  "uv-straling 5 · röntgenstraling 6 · gammastraling 7", W),
             ]),
        dict(kop="Ioniserend of niet",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("gammastraling", "ja"), ("microgolven", "nee"), ("röntgenstraling", "ja")],
                  "Ioniserend?", WW),
                 ("rij", [("radiogolven", "nee"), ("harde uv-straling", "ja"), ("infrarood", "nee")],
                  "Ioniserend?", WW),
             ]),
        dict(kop="Rekenen aan licht",
             opdracht=r"Neem \(c = 3{,}00 \times 10^{8}\) m/s en \(h = 6{,}63 \times 10^{-34}\) J·s.",
             oefeningen=[
                 ("rij", [(r"\(\lambda = 3{,}0\) m", r"\(f = 1{,}0 \times 10^{8}\) Hz"),
                          (r"\(f = 1{,}0 \times 10^{15}\) Hz", r"\(\lambda = 3{,}0 \times 10^{-7}\) m"),
                          (r"\(\lambda = 6{,}0 \times 10^{-7}\) m", r"\(f = 5{,}0 \times 10^{14}\) Hz")],
                  "Wat ontbreekt?", WL),
                 ("kort", r"Hoe groot is de energie van een foton met \(f = 5{,}0 \times 10^{14}\) Hz?",
                  r"\(E = h\,f = 3{,}3 \times 10^{-19}\) J.", WL),
                 ("kort", r"Een zender werkt op \(100\) MHz. Hoe groot is \(\lambda\)?",
                  r"\(3{,}0\) m, uit \(\lambda = \dfrac{c}{f}\).", WW),
                 ("kort", "Wat heeft de grootste energie per foton: infrarood of röntgen?",
                  r"Röntgen, want \(f\) is er veel groter en \(E = h\,f\).", WW),
             ]),
        dict(kop="Lenzen en spiegels",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("het beeld in een vlakke spiegel", "virtueel, rechtop, even groot"),
                          (r"een voorwerp verder dan \(2f\) bij een bolle lens", "reëel, omgekeerd, kleiner"),
                          (r"een voorwerp binnen \(f\) bij een bolle lens", "virtueel, rechtop, groter")],
                  "Welk beeld?", WL),
                 ("kort", r"Een bolle lens heeft \(f = 12\) cm. Waar ligt het punt op \(2f\)?",
                  r"Op \(24\) cm van de lens.", WW),
                 ("kort", "Welk toestel zet een voorwerp binnen de brandpuntsafstand?",
                  "Een vergrootglas; het geeft een virtueel, groter beeld.", WL),
             ]),
        dict(kop="Waar of niet waar: licht",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Alle elektromagnetische golven lopen in vacuüm even snel.", True),
                 ("waar", "Een virtueel beeld kan je op een scherm opvangen.", False),
                 ("waar", "Bij een ruw oppervlak kaatsen de stralen alle kanten op.", True),
                 ("waar", "Microgolven zijn ioniserend.", False),
                 ("waar", "De proef van Young toont aan dat licht uit deeltjes bestaat.", False),
             ]),
        dict(kop="Rekenen aan geluid",
             opdracht=r"Neem \(v = 340\) m/s in lucht.",
             oefeningen=[
                 ("kort", r"Je hoort de donder \(9{,}0\) s na de bliksem. Hoe ver is het onweer?",
                  r"\(3060\) m, uit \(d = v\,t\).", WW),
                 ("kort", r"Een echo komt \(2{,}0\) s later terug van een wand. Hoe ver staat die?",
                  r"\(340\) m; het geluid legde \(680\) m af, heen en terug.", WL),
                 ("kort", r"Een toon heeft \(f = 170\) Hz. Hoe groot is \(\lambda\) in lucht?",
                  r"\(2{,}0\) m, uit \(\lambda = \dfrac{v}{f}\).", WW),
                 ("kort", r"Een toon heeft \(\lambda = 0{,}25\) m. Hoe groot is \(f\)?",
                  r"\(1360\) Hz, uit \(f = \dfrac{v}{\lambda}\).", WW),
                 ("kort", r"Een snaar heeft \(f_{1} = 150\) Hz. Hoe groot is \(f_{4}\)?",
                  r"\(600\) Hz, want \(f_{n} = n\,f_{1}\).", WW),
             ]),
        dict(kop="Decibel en gehoor",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de gehoordrempel van een mens", r"\(0\) dB"),
                          ("de gevaargrens voor het gehoor", r"\(80\) dB"),
                          ("het hoorbare gebied", r"\(20\) tot \(20\,000\) Hz")],
                  "Welke waarde?", WL),
                 ("kort", r"Een geluid gaat van \(50\) dB naar \(80\) dB. Hoeveel keer zo intens wordt het?",
                  r"\(10^{3}\), dus duizend keer.", WL),
                 ("kort", r"Hoeveel dB komt erbij als \(I\) honderd keer zo groot wordt?",
                  r"\(20\) dB, want elke \(10\) dB is een factor \(10\).", WL),
                 ("kort", r"Je gaat drie keer zo dicht bij een luidspreker staan. Hoeveel keer zo groot wordt \(I\)?",
                  r"Negen keer, want \(I \sim \dfrac{1}{r^{2}}\).", WW),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit hoe blijvende gehoorschade in het binnenoor ontstaat.",
                  "De trilhaartjes op de haarcellen breken af door te hard of te lang geluid. "
                  "Ze groeien niet terug, dus is de schade blijvend.", 3),
                 ("open", "Wat is het dopplereffect, en verandert de bron daarbij iets aan zijn toon?",
                  "De waargenomen frequentie verschilt als bron en waarnemer naar of van elkaar "
                  "bewegen. De bron zendt onveranderd dezelfde frequentie uit; alleen de golven "
                  "komen bij de waarnemer dichter op elkaar of verder uiteen.", 3),
                 ("open", "Waarom hoor je een verschil tussen een viool en een fluit op dezelfde toon?",
                  "De grondfrequentie is dezelfde, maar de harmonischen erboven hebben een "
                  "andere sterkteverdeling. Dat verschil in de vorm van het patroon is de "
                  "klankkleur of het timbre.", 3),
                 ("open", "Waarom dragen radiogolven verder rond gebouwen dan microgolven?",
                  r"Radiogolven hebben een veel grotere \(\lambda\) en buigen daardoor beter af "
                  r"rond obstakels. Buiging lukt het best als de opening of het obstakel even "
                  r"groot is als \(\lambda\) of kleiner.", 3),
             ]),
        dict(kop="Waar of niet waar: geluid",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Geluid loopt sneller in staal dan in lucht.", True),
                 ("waar", "Bij het dopplereffect verandert de frequentie die de bron uitzendt.", False),
                 ("waar", r"Infrasoon geluid ligt onder \(20\) Hz.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kwantumfysica-het-foto-elektrisch-effect-en-dualiteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kwantumfysica: het foto-elektrisch effect en dualiteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Komen er elektronen los?",
             opdracht=r"Het metaal heeft \(f_{0} = 5 \times 10^{14}\) Hz. Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [(r"licht van \(7 \times 10^{14}\) Hz", "ja"),
                          (r"licht van \(3 \times 10^{14}\) Hz", "nee"),
                          (r"heel fel licht van \(3 \times 10^{14}\) Hz", "nee")],
                  "Komen er elektronen los?", WW),
                 ("rij", [(r"zwak licht van \(6 \times 10^{14}\) Hz", "ja"),
                          (r"licht van \(5 \times 10^{14}\) Hz", "ja"),
                          ("heel fel infrarood", "nee")],
                  "Komen er elektronen los?", WW),
             ]),
        dict(kop=r"Rekenen met \(E = h\,f\)",
             opdracht=r"Neem \(h = 6{,}63 \times 10^{-34}\) J·s.",
             oefeningen=[
                 ("kort", r"Hoe groot is \(E\) van een foton met \(f = 4 \times 10^{14}\) Hz?",
                  r"\(2{,}7 \times 10^{-19}\) J.", WL),
                 ("kort", r"Hoe groot is \(E\) van een foton met \(f = 1 \times 10^{15}\) Hz?",
                  r"\(6{,}6 \times 10^{-19}\) J.", WL),
                 ("kort", r"Een metaal heeft \(f_{0} = 5 \times 10^{14}\) Hz. Hoe groot is de uittree-arbeid \(W\)?",
                  r"\(W = h\,f_{0} = 3{,}3 \times 10^{-19}\) J.", WL),
                 ("kort", r"Licht van \(8 \times 10^{14}\) Hz valt op datzelfde metaal. Hoe groot is \(E_{k}\)?",
                  r"\(E_{k} = h\,f - W = 5{,}3 \times 10^{-19} - 3{,}3 \times 10^{-19} "
                  r"= 2{,}0 \times 10^{-19}\) J.", WL),
                 ("kort", "Welk foton is energierijker: rood of blauw licht?",
                  r"Blauw, want het heeft een hogere \(f\) en een kleinere \(\lambda\).", WL),
             ]),
        dict(kop="Frequentie of intensiteit",
             opdracht="Schrijf de frequentie of de intensiteit.",
             oefeningen=[
                 ("rij", [("beslist of er elektronen loskomen", "de frequentie"),
                          ("beslist hoeveel elektronen er loskomen", "de intensiteit"),
                          ("beslist hoeveel energie elk elektron meekrijgt", "de frequentie")],
                  "Wat beslist dat?", WL),
             ]),
        dict(kop="Golf of deeltje",
             opdracht="Schrijf golfmodel of deeltjesmodel.",
             oefeningen=[
                 ("rij", [("interferentie bij de proef van Young", "golfmodel"),
                          ("het foto-elektrisch effect", "deeltjesmodel"),
                          ("breking bij de overgang naar glas", "golfmodel")],
                  "Welk model?", WW),
                 ("rij", [("de drempelfrequentie van een metaal", "deeltjesmodel"),
                          ("buiging rond een smalle opening", "golfmodel"),
                          ("de energie van één foton", "deeltjesmodel")],
                  "Welk model?", WW),
             ]),
        dict(kop=r"De golflengte \(\lambda = \dfrac{h}{m\,v}\)",
             opdracht=r"Neem \(h = 6{,}63 \times 10^{-34}\) J·s.",
             oefeningen=[
                 ("kort", r"Een elektron heeft \(m\,v = 2{,}0 \times 10^{-24}\) kg·m/s. Hoe groot is \(\lambda\)?",
                  r"\(3{,}3 \times 10^{-10}\) m, ongeveer de grootte van een atoom.", WL),
                 ("kort", r"Een bal van \(0{,}40\) kg loopt \(5{,}0\) m/s. Hoe groot is \(\lambda\)?",
                  r"\(3{,}3 \times 10^{-34}\) m.", WL),
                 ("kort", "Waarom meet niemand die laatste golflengte ooit?",
                  "Ze is onvoorstelbaar veel kleiner dan een atoom.", WL),
             ]),
        dict(kop="Hoe heet dat?",
             opdracht="Schrijf het begrip.",
             oefeningen=[
                 ("rij", [("het gebied waar een elektron met grote kans zit", "een orbitaal"),
                          ("de laagste frequentie waarbij iets loskomt", "de drempelfrequentie"),
                          ("de vergelijking die de golffunctie geeft", "die van Schrödinger")],
                  "Hoe heet dat?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Eén elektron kan de energie van meerdere fotonen samen opnemen.", False),
                 ("waar", "Davisson en Germer lieten het golfkarakter van elektronen zien.", True),
                 ("waar", "Het onzekerheidsbeginsel komt door de beperkingen van onze meettoestellen.", False),
                 ("waar", "De golffunctie geeft de kans om een deeltje op een plaats te vinden.", True),
                 ("waar", "Van een elektron in een atoom kan je een baan tekenen zoals van een planeet.", False),
                 ("waar", "Boven de drempelfrequentie geeft meer intensiteit meer elektronen.", True),
                 ("waar", r"Een foton met een kleinere \(\lambda\) draagt minder energie.", False),
                 ("waar", r"De helling van de grafiek van \(E_{k}\) tegen \(f\) is \(h\).", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom verklaart het klassieke golfmodel het foto-elektrisch effect niet?",
                  "Volgens dat model zou fel rood licht na wat wachten genoeg energie "
                  "aanbrengen. In werkelijkheid komt er met rood licht nooit één elektron los, "
                  "want elk elektron krijgt precies één foton en dat moet op zich genoeg "
                  "energie hebben.", 4),
                 ("open", "Waarom merken we het golfkarakter van een voetbal niet?",
                  r"Zijn massa is zo groot dat \(\lambda = \dfrac{h}{m\,v}\) onvoorstelbaar "
                  r"klein wordt. Bij een elektron is ze van de orde van een atoom, en daar zie "
                  r"je het effect dus wel.", 4),
                 ("open", "Je vuurt elektronen één per één door twee spleten. Wat zie je, en waarom is dat merkwaardig?",
                  "Na lang wachten staat er toch een patroon van strepen. Merkwaardig is dat "
                  "elk elektron als één stip aankomt, dus als deeltje, en dat ze samen toch het "
                  "patroon van een golf vormen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-atoomkern-radioactief-verval-en-halveringstijd-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De atoomkern, radioactief verval en halveringstijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Protonen en neutronen tellen",
             opdracht=r"Vul de tabel aan met \(N = A - Z\).",
             oefeningen=[
                 ("tabel", ["nuclide", r"\(A\)", r"\(Z\)", r"\(N\)"],
                  [["natrium-23", "23", "11", None], ["lood-207", "207", "82", None],
                   ["koolstof-14", "14", "6", None], ["uranium-235", "235", "92", None],
                   ["radium-226", "226", "88", None]],
                  "natrium-23: 12 · lood-207: 125 · koolstof-14: 8 · uranium-235: 143 · "
                  "radium-226: 138", W),
             ]),
        dict(kop="Welk verval?",
             opdracht="Schrijf alfa, bèta-min, bèta-plus of gamma.",
             oefeningen=[
                 ("rij", [("er vertrekt een heliumkern", "alfa"),
                          ("een neutron wordt een proton", "bèta-min"),
                          (r"\(A\) en \(Z\) blijven gelijk", "gamma")],
                  "Welk verval?", WW),
                 ("rij", [("er vertrekt een positron", "bèta-plus"),
                          (r"\(A\) daalt met vier, \(Z\) met twee", "alfa"),
                          (r"\(Z\) stijgt met één, \(A\) blijft gelijk", "bèta-min")],
                  "Welk verval?", WW),
             ]),
        dict(kop="Na het verval",
             opdracht=r"Schrijf het nieuwe \(A\) en \(Z\).",
             oefeningen=[
                 ("rij", [(r"\(A = 238\), \(Z = 92\), alfa", r"\(A = 234\), \(Z = 90\)"),
                          (r"\(A = 14\), \(Z = 6\), bèta-min", r"\(A = 14\), \(Z = 7\)")],
                  "Wat krijg je?", WL),
                 ("rij", [(r"\(A = 210\), \(Z = 84\), alfa", r"\(A = 206\), \(Z = 82\)"),
                          (r"\(A = 60\), \(Z = 27\), gamma", r"\(A = 60\), \(Z = 27\)")],
                  "Wat krijg je?", WL),
                 ("kort", r"Radium-226 (\(Z = 88\)) doet alfaverval. Welk nuclide ontstaat er, en met welk \(Z\)?",
                  r"Radon-222, met \(Z = 86\).", WL),
             ]),
        dict(kop="Halveringstijd",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", r"\(T_{1/2} = 6\) dagen. Welk deel is er na \(18\) dagen nog over?",
                  r"\(\tfrac{1}{8}\), want dat zijn drie halveringen.", WW),
                 ("kort", r"\(T_{1/2} = 4\) jaar. Na hoeveel jaar is er nog \(\tfrac{1}{16}\) over?",
                  r"\(16\) jaar, want dat zijn vier halveringen.", WW),
                 ("kort", r"Na hoeveel halveringstijden is er nog \(\tfrac{1}{32}\) over?",
                  r"Vijf, want \(\left(\tfrac{1}{2}\right)^{5} = \tfrac{1}{32}\).", WW),
                 ("kort", r"Koolstof-14 heeft \(T_{1/2} = 5730\) jaar. Hoe oud is hout met nog \(\tfrac{1}{4}\)?",
                  r"\(11\,460\) jaar, dus twee halveringstijden.", WL),
             ]),
        dict(kop=r"Activiteit en \(\lambda\)",
             opdracht=r"Gebruik \(A = \lambda\,N\) en \(\lambda = \dfrac{0{,}693}{T_{1/2}}\).",
             oefeningen=[
                 ("kort", r"Een bron van \(1600\) Bq heeft \(T_{1/2} = 3\) uur. Hoe groot is \(A\) na \(9\) uur?",
                  r"\(200\) Bq, want \(1600 : 8\).", WW),
                 ("kort", r"\(T_{1/2} = 10\) dagen. Hoe groot is \(\lambda\) per dag?",
                  r"\(\lambda = 0{,}0693\) per dag.", WW),
                 ("kort", r"Een bron heeft \(N = 1{,}0 \times 10^{18}\) kernen en \(\lambda = 2{,}0 \times 10^{-9}\) per s. Hoe groot is \(A\)?",
                  r"\(A = \lambda\,N = 2{,}0 \times 10^{9}\) Bq.", WL),
                 ("kort", r"Twee bronnen hebben evenveel kernen. Welke heeft de grootste \(A\)?",
                  r"Die met de kortste \(T_{1/2}\), want haar \(\lambda\) is groter.", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Na twee halveringstijden is een bron volledig vervallen.", False),
                 ("waar", "Je kan het verval van een radionuclide versnellen door te verwarmen.", False),
                 ("waar", "De activiteit van een bron staat in becquerel.", True),
                 ("waar", "Bij gammaverval verandert de kern in een ander element.", False),
                 ("waar", r"Twee isotopen van hetzelfde element hebben hetzelfde \(Z\).", True),
                 ("waar", r"Bij bèta-min-verval blijft \(A\) gelijk.", True),
                 ("waar", r"Een kortere halveringstijd geeft een kleinere \(\lambda\).", False),
                 ("waar", "De activiteit is recht evenredig met het aantal kernen.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom zijn zware kernen pas stabiel met meer neutronen dan protonen?",
                  "De protonen stoten elkaar over de hele kern af met de coulombkracht. Extra "
                  "neutronen voegen wel kernkracht toe maar geen extra afstoting, en houden de "
                  "kern zo samen.", 4),
                 ("open", "Leg uit waarop de koolstof-14-methode berust.",
                  "Een levend organisme vult zijn voorraad koolstof-14 aan uit de lucht. Na de "
                  "dood stopt dat, en daalt het gehalte met een vaste halveringstijd; uit wat "
                  "er nog over is, volgt de ouderdom.", 4),
                 ("open", "Waarom daalt de activiteit van een bron even snel als haar aantal kernen?",
                  r"Omdat \(A = \lambda\,N\) en \(\lambda\) niet verandert. \(A\) is dus recht "
                  r"evenredig met \(N\), en beide halveren na elke halveringstijd.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kernenergie-straling-en-haar-effecten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kernenergie, straling en haar effecten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat houdt wat tegen?",
             opdracht="Schrijf alfa, bèta of gamma.",
             oefeningen=[
                 ("rij", [("een blad papier", "alfa"), ("een plaatje aluminium", "bèta"),
                          ("een dikke laag lood", "gamma")],
                  "Welke straling houdt het tegen?", WW),
                 ("rij", [("het grootste ioniserend vermogen", "alfa"),
                          ("het grootste doordringend vermogen", "gamma"),
                          ("buigt niet af in een magnetisch veld", "gamma")],
                  "Welke straling?", WW),
             ]),
        dict(kop=r"Rekenen met \(E = m\,c^{2}\)",
             opdracht=r"Neem \(c = 3 \times 10^{8}\) m/s.",
             oefeningen=[
                 ("kort", r"Hoeveel energie zit er in \(2\) g massa?",
                  r"\(1{,}8 \times 10^{14}\) J, want \(0{,}002 \times 9 \times 10^{16}\).", WL),
                 ("kort", r"Hoeveel energie zit er in \(0{,}50\) kg massa?",
                  r"\(4{,}5 \times 10^{16}\) J.", WL),
                 ("kort", r"Bij een reactie verdwijnt \(1{,}0 \times 10^{-6}\) kg massa. Hoeveel energie komt vrij?",
                  r"\(9 \times 10^{10}\) J.", WL),
                 ("kort", r"Een kern heeft \(\Delta m\) en \(A = 56\). Hoe bereken je \(\dfrac{E_{b}}{A}\)?",
                  r"Eerst \(E_{b} = \Delta m\,c^{2}\), dan delen door \(56\).", WL),
             ]),
        dict(kop="Dosis",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de energie van de straling per kilogram weefsel", "de geabsorbeerde dosis"),
                          ("de eenheid daarvan", "gray")],
                  "Hoe heet dat?", WL),
                 ("rij", [(r"\(H = w_{R} \cdot D\)", "de equivalente dosis"),
                          (r"met \(w_{T}\) erbij", "de effectieve dosis")],
                  "Hoe heet dat?", WL),
                 ("kort", r"Een weefsel krijgt \(D = 0{,}20\) Gy gammastraling, met \(w_{R} = 1\). Hoe groot is \(H\)?",
                  r"\(H = 0{,}20\) Sv.", WL),
                 ("kort", r"Dezelfde \(D\) maar alfastraling, met \(w_{R} = 20\). Hoe groot is \(H\) nu?",
                  r"\(H = 4{,}0\) Sv, dus twintig keer zoveel.", WL),
             ]),
        dict(kop="Splijting, fusie en de centrale",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("een zware kern valt uiteen", "splijting"),
                          ("twee lichte kernen worden één", "fusie"),
                          ("de energie van de zon", "fusie")],
                  "Splijting of fusie?", WW),
                 ("rij", [("een gewone kerncentrale op uranium", "splijting"),
                          ("waterstof wordt helium", "fusie"),
                          ("wordt met regelstaven in de hand gehouden", "splijting")],
                  "Splijting of fusie?", WW),
                 ("kort", r"Waarom levert geen van beide energie bij ijzer-56?",
                  r"Daar ligt de top van \(\dfrac{E_{b}}{A}\): verder omhoog kan niet.", WL),
                 ("rij", [("remt de neutronen af", "de moderator"),
                          ("slorpt neutronen op en regelt zo de reactie", "de regelstaven"),
                          ("voert de warmte naar de stoomturbine", "het koelwater")],
                  "Welk onderdeel van de centrale?", WW),
                 ("rij", [("elke splijting maakt nieuwe neutronen die weer splijten", "de kettingreactie"),
                          ("de kleinste massa waarin die reactie zich in stand houdt", "de kritische massa")],
                  "Hoe heet dat?", WL),
                 ("kort", r"Een centrale haalt een rendement van \(33\) %. Hoeveel elektrische energie krijg je uit \(900\) MW warmte?",
                  r"\(300\) MW; de rest gaat als warmte weg.", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een kerncentrale op splijting stoot bij het opwekken van stroom CO₂ uit.", False),
                 ("waar", "Doorstraald voedsel wordt zelf radioactief.", False),
                 ("waar", "Voor hoogactief afval van categorie C ligt in België al een bergingsplaats vast.", False),
                 ("waar", "Bij een kernproces blijft de totale massa van de deeltjes precies gelijk.", False),
                 ("waar", "Natuurlijke straling komt onder meer van radon uit de bodem.", True),
                 ("waar", r"In hoogactief afval zitten kernen met een \(T_{1/2}\) van duizenden jaren.", True),
                 ("waar", r"Een kern met een grotere \(\tfrac{E_{b}}{A}\) is stabieler.", True),
                 ("waar", "Alfastraling is van buiten het lichaam het gevaarlijkst.", False),
                 ("waar", r"\(1\) Gy is \(1\) J per kilogram.", True),
                 ("waar", "De effectieve dosis houdt rekening met het bestraalde weefsel.", True),
                 ("waar", "Gammastraling buigt af in een elektrisch veld.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem de drie manieren om je tegen ioniserende straling te beschermen.",
                  "Afstand: de intensiteit daalt met het kwadraat van de afstand. Tijd: hoe "
                  "korter je in de buurt blijft, hoe kleiner de dosis. Afscherming: lood of "
                  "beton tussen jou en de bron zwakt de straling af.", 4),
                 ("open", "Waarom deelt men bij een kernongeval jodiumpillen uit?",
                  "De schildklier neemt jodium op. Door ze met gewoon jodium te vullen, kan ze "
                  "geen radioactief jodium meer opnemen, en blijft de dosis daar laag.", 4),
                 ("open", "Waarom heeft alfastraling een veel hogere stralingsweegfactor dan gamma?",
                  "Alfastraling geeft al haar energie in een heel klein gebied af, dus komen "
                  "alle ionisaties op dezelfde paar cellen terecht. Dat doet veel meer schade "
                  "dan dezelfde energie die over een groot volume verdeeld wordt.", 4),
                 ("open", "Leg uit wat het verschil is tussen bestraling en besmetting.",
                  "Bij bestraling blijft de bron buiten je lichaam en stopt het zodra je "
                  "weggaat. Bij besmetting zit de radioactieve stof op of in je lichaam, en "
                  "blijft ze stralen tot ze verwijderd of vervallen is.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meetinstrumenten-en-meetonzekerheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig werken, meetinstrumenten en meetonzekerheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk instrument?",
             opdracht="Schrijf de naam van het toestel.",
             oefeningen=[
                 ("rij", [("een kracht", "een dynamometer"), ("een tijdsduur", "een chronometer"),
                          ("een geluidsniveau", "een decibelmeter")],
                  "Waarmee meet je dat?", WL),
                 ("rij", [("een spanning", "een multimeter of voltmeter"),
                          ("een stroom", "een multimeter of ampèremeter"),
                          ("een temperatuur", "een thermometer")],
                  "Waarmee meet je dat?", WL),
             ]),
        dict(kop="Eenheden omrekenen",
             opdracht="Reken om en schrijf de eenheid erbij.",
             oefeningen=[
                 ("rij", [(r"\(3{,}5\ \text{mA}\) in ampère", r"\(0{,}0035\ \text{A}\)"),
                          (r"\(2{,}2\ \text{k}\Omega\) in ohm", r"\(2200\ \Omega\)"),
                          (r"\(90\ \text{km/h}\) in \(\text{m/s}\)", r"\(25\ \text{m/s}\)")],
                  "Hoeveel?", WW),
                 ("rij", [(r"\(0{,}25\ \text{M}\Omega\) in ohm", r"\(250\,000\ \Omega\)"),
                          (r"\(15\ \text{m/s}\) in \(\text{km/h}\)", r"\(54\ \text{km/h}\)"),
                          (r"\(470\ \mu\text{F}\) in farad", r"\(0{,}000470\ \text{F}\)")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Schrijf de macht van tien.",
             oefeningen=[
                 ("rij", [("milli", r"\(10^{-3}\)"), ("micro", r"\(10^{-6}\)"),
                          ("nano", r"\(10^{-9}\)")],
                  "Welke factor?", WW),
                 ("rij", [("kilo", r"\(10^{3}\)"), ("mega", r"\(10^{6}\)"),
                          ("centi", r"\(10^{-2}\)")],
                  "Welke factor?", WW),
             ]),
        dict(kop="Beduidende cijfers",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"\(0{,}0340\ \text{m}\)", "drie"), (r"\(1200\ \text{g}\)", "twee"),
                          (r"\(5{,}07\ \text{s}\)", "drie")],
                  "Hoeveel beduidende cijfers?", WW),
                 ("kort", r"Je telt \(3{,}4\ \text{m}\) en \(2{,}15\ \text{m}\) op. Hoe schrijf je het antwoord?",
                  r"\(5{,}6\ \text{m}\), met één cijfer na de komma, want de slechtste meting bepaalt dat.", WL),
                 ("kort", r"Een lat meet tot op \(1\ \text{mm}\). Mag je \(12{,}437\ \text{cm}\) noteren?",
                  r"Nee, hoogstens \(12{,}4\ \text{cm}\): verder meet de lat niet.", WL),
                 ("rij", [(r"\(0{,}0000067\)", r"\(6{,}7 \times 10^{-6}\)"),
                          (r"\(32\,000\)", r"\(3{,}2 \times 10^{4}\)"),
                          (r"\(0{,}00045\)", r"\(4{,}5 \times 10^{-4}\)")],
                  "Hoe schrijf je dat in wetenschappelijke notatie?", WW),
                 ("kort", r"Waarom zegt \(4{,}50 \times 10^{-4}\) iets anders dan \(4{,}5 \times 10^{-4}\)?",
                  r"Er staan drie beduidende cijfers in plaats van twee, dus is er fijner gemeten.", WL),
             ]),
        dict(kop="Het juiste bereik",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"een stroom van \(25\ \text{A}\) met een meter tot \(10\ \text{A}\)",
                           "nee, buiten het meetbereik"),
                          (r"een massa van \(3\ \text{g}\) op een weegschaal die tot op \(1\ \text{g}\) gaat",
                           "nee, veel te grof"),
                          (r"een lokaal van \(6\ \text{m}\) met een rolmeter van \(8\ \text{m}\)",
                           "ja, dat past ruim")],
                  "Mag je zo meten?", WL),
                 ("rij", [(r"een val van ongeveer \(0{,}5\ \text{s}\)", r"\(0{,}01\ \text{s}\) of fijner"),
                          ("de lengte van een lokaal", r"\(1\ \text{cm}\) volstaat ruim")],
                  "Welke nauwkeurigheid heb je nodig?", WL),
             ]),
        dict(kop="Grafieken en verbanden",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("een rechte door de oorsprong", "recht evenredig"),
                          ("een kromme die daalt en de assen nadert", "omgekeerd evenredig"),
                          ("een parabool door de oorsprong", "kwadratisch")],
                  "Welk verband?", WW),
                 ("rij", [(r"\(y = k\,x\)", "recht evenredig"),
                          (r"\(y = \dfrac{k}{x}\)", "omgekeerd evenredig"),
                          (r"\(y = k\,x + q\)", "lineair")],
                  "Welk verband?", WW),
                 ("kort", r"Uit \(F = m\,a\): hoe schrijf je \(m\) in functie van de rest?",
                  r"\(m = \dfrac{F}{a}\).", WL),
             ]),
        dict(kop="Waar of niet waar: meten en noteren",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een nauwkeuriger meetinstrument is altijd de beste keuze.", False),
                 ("waar", "Een antwoord zonder eenheid is in de fysica even goed.", False),
                 ("waar", "Een meetinstrument uitschakelen als je niet meet, hoort bij duurzaam werken.", True),
                 ("waar", "In de wetenschappelijke notatie staat er één cijfer voor de komma.", True),
                 ("waar", "Je mag elektrische toestellen met natte handen bedienen als de spanning laag is.", False),
             ]),
        dict(kop="Waar of niet waar: aflezen en opruimen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een analoge meter lees je het best van opzij af.", False),
                 ("waar", r"Bij een omgekeerd evenredig verband blijft \(x\,y\) constant.", True),
                 ("waar", "Lege batterijen horen bij het klein gevaarlijk afval.", True),
             ]),
        dict(kop="Waar zit de fout?",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", r"Een leerling leest \(500\) af op de \(\text{mA}\)-stand en noteert \(500\ \text{A}\). Wat ging er mis?",
                  r"Het voorvoegsel is weggevallen: \(500\ \text{mA} = 0{,}5\ \text{A}\).", WL),
                 ("kort", r"Na \(2{,}5 + 1{,}25\) staat er \(3{,}75\ \text{m}\). Wat is er fout?",
                  r"Eén cijfer na de komma volstaat, dus \(3{,}8\ \text{m}\).", WL),
                 ("kort", r"Een meter geeft \(230\), zonder meer. Waarom is dat onbruikbaar?",
                  r"Zonder eenheid weet niemand of het volt, ohm of iets anders is.", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom zet je een spanningsbron op de laagste stand voor je hem aansluit?",
                  "Dan kan je de spanning rustig opdrijven zonder dat er bij een verkeerde "
                  "schakeling iets doorbrandt.", 3),
                 ("open", "Waarom meet je een snelle beweging liever met een sensor dan met een handchronometer?",
                  "Je reactietijd geeft een fout van wel een tiende seconde, bij een halve "
                  "seconde al een vijfde ervan.", 3),
                 ("open", "Een toestel wijst een waarde aan die niet kan kloppen. Wat doe je?",
                  "Je neemt ze niet over: eerst bereik, aansluiting en stand nagaan, dan "
                  "opnieuw meten.", 3),
                 ("open", "Leg uit wat de parallaxfout is en hoe je ze vermijdt.",
                  "De naald hangt boven de schaal, dus geeft schuin kijken een andere waarde. "
                  "Kijk recht van boven.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen op orde",
             opdracht="Schrijf de nummers 1 tot 6 in de juiste volgorde.",
             oefeningen=[
                 ("tabel", ["stap", "plaats 1 tot 6"],
                  [["een conclusie formuleren", None], ["een onderzoeksvraag opstellen", None],
                   ["het probleem afbakenen", None], ["de data verwerken", None],
                   ["een hypothese opstellen", None], ["metingen uitvoeren", None]],
                  "het probleem afbakenen 1 · een onderzoeksvraag opstellen 2 · een hypothese "
                  "opstellen 3 · metingen uitvoeren 4 · de data verwerken 5 · een conclusie "
                  "formuleren 6", W),
             ]),
        dict(kop="Bruikbaar of niet",
             opdracht="Schrijf bruikbaar of te breed.",
             oefeningen=[
                 ("rij", [("Hoe hangt de valtijd af van de hoogte?", "bruikbaar"),
                          ("Hoe werkt de natuurkunde?", "te breed")],
                  "Bruikbare onderzoeksvraag?", WL),
                 ("rij", [("Wat is energie?", "te breed"),
                          ("Hoe hangt de weerstand van een draad af van zijn lengte?", "bruikbaar")],
                  "Bruikbare onderzoeksvraag?", WL),
             ]),
        dict(kop="Welke variabele?",
             opdracht="Schrijf onafhankelijk, afhankelijk of constant.",
             oefeningen=[
                 ("rij", [("de hoogte die jij kiest", "onafhankelijk"),
                          ("de valtijd die je meet", "afhankelijk"),
                          ("de massa van de bal, altijd dezelfde", "constant")],
                  "Welke variabele?", WW),
                 ("rij", [("de lengte van de draad die jij instelt", "onafhankelijk"),
                          ("de weerstand die de multimeter aanwijst", "afhankelijk"),
                          ("de dikte van de draad, overal dezelfde", "constant")],
                  "Welke variabele?", WW),
                 ("kort", r"Je meet de valtijd \(t\) vanaf hoogtes \(h\). Welke grafiek teken je?",
                  r"\(t(h)\): de hoogte op de horizontale as, de valtijd op de verticale.", WL),
             ]),
        dict(kop="Hoort het in het verslag?",
             opdracht="Schrijf hoort erin of hoeft niet.",
             oefeningen=[
                 ("rij", [("welke instrumenten je gebruikt hebt", "hoort erin"),
                          ("de meetwaarden met hun eenheid", "hoort erin"),
                          ("hoe laat je begonnen bent", "hoeft niet")],
                  "Hoort het in het verslag?", WL),
                 ("rij", [("welke grootheden je constant gehouden hebt", "hoort erin"),
                          ("een meting die je weggelaten hebt, met de reden", "hoort erin")],
                  "Hoort het in het verslag?", WL),
             ]),
        dict(kop="Waar of niet waar: onderzoeken",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een meting die je hypothese tegenspreekt, is een geldig resultaat.", True),
                 ("waar", "Een conclusie mag verder gaan dan wat je gemeten hebt.", False),
                 ("waar", "In een proef verander je het best meerdere grootheden tegelijk, dat gaat sneller.", False),
                 ("waar", "Een onderzoek moet herhaalbaar zijn: iemand anders moet met jouw plan hetzelfde vinden.", True),
                 ("waar", "Bij een STEM-opdracht volstaat het om één discipline grondig in te zetten.", False),
             ]),
        dict(kop="Waar of niet waar: ontwerpen",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een hypothese stel je op nadat je gemeten hebt.", False),
                 ("waar", "Een criterium moet meetbaar zijn.", True),
                 ("waar", "Bij een ontwerp volstaat het soms om een bestaand systeem aan te passen.", True),
             ]),
        dict(kop="Ontwerpen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de eisen waaraan je oplossing moet voldoen", "de criteria"),
                          ("de kleinere stukken van een groot probleem", "de deelproblemen"),
                          ("waarin je alle deeloplossingen samenbrengt", "de totaaloplossing")],
                  "Hoe heet dat?", WL),
                 ("rij", [(r"de tas weegt minder dan \(2\ \text{kg}\)", "criterium"),
                          ("de tas ziet er sportief uit", "mening"),
                          (r"het drankje blijft onder \(8\ ^\circ\text{C}\)", "criterium")],
                  "Criterium of mening?", WW),
                 ("open", r"Je ontwerpt een zonneoven die water tot \(60\ ^\circ\text{C}\) moet brengen. Schrijf twee criteria op.",
                  r"Bijvoorbeeld: het water haalt binnen twee uur \(60\ ^\circ\text{C}\), en de oven "
                  r"is te bouwen met materiaal uit de winkel voor minder dan twintig euro.", 4),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom herhaal je een meting meerdere keren?",
                  "Elke meting heeft een toevallige afwijking. Door te herhalen en het gemiddelde "
                  "te nemen vallen die grotendeels weg, en blijft het werkelijke verband over.", 3),
                 ("open", "Waarom moet een hypothese weerlegd kunnen worden?",
                  "Een verwachting die nooit fout kan zijn, kan je met geen enkele proef nagaan. "
                  "Juist doordat de meting ze kan tegenspreken, leer je er iets uit.", 3),
                 ("open", "Waarvoor staan de letters van STEM, en waarom bekijk je een probleem vanuit al die hoeken?",
                  "Wetenschappen, technologie, techniek en wiskunde. Elk vak brengt een stuk van de "
                  "oplossing aan: de wetenschap het waarom, de techniek het bouwen en de wiskunde "
                  "het rekenwerk.", 3),
                 ("open", "Waarom is een onderzoek naar zonnepanelen ook een maatschappelijke zaak?",
                  "De keuzes die eruit volgen raken ieders energie en kosten. Zulke uitdagingen "
                  "zijn net een reden om nieuwe technieken en materialen te ontwikkelen.", 3),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-elektrische-lading-geleiders-en-influentie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Stel bij elke stof één vraag: kan er lading in bewegen. Metalen hebben vrije "
                   "elektronen, een zoutoplossing heeft vrije ionen, en al de rest houdt zijn "
                   "lading vast.",
            waarom=[
                "Let op zout water: dat geleidt niet door elektronen maar door ionen die zelf "
                "verplaatsen. Zuiver water geleidt bijna niet, dus het zout doet het werk.",
                None,
                "Noem waar de ladingdrager zit. In een metaal horen de buitenste elektronen bij het "
                "hele stuk en niet bij één atoom, dus kunnen ze door het rooster lopen. In glas zit "
                "elk elektron vast aan zijn eigen atoom.",
            ],
        ),
        dict(
            aanpak="Gelijknamig stoot af, ongelijknamig trekt aan. Twee keer hetzelfde teken geeft "
                   "dus altijd afstoting, wat de grootte ook is.",
            waarom=[
                None,
            ],
        ),
        dict(
            aanpak="Leer de voorvoegsels als machten van tien: m is tien tot de min drie, micro min "
                   "zes, n min negen en p min twaalf. Zet daarna het getal in de vorm met één cijfer "
                   "voor de komma.",
            waarom=[
                "Let op 40 pC: dat wordt niet 40 maal tien tot de min twaalf maar 4,0 maal tien tot "
                "de min elf, want in de wetenschappelijke notatie staat er één cijfer voor de komma.",
            ],
        ),
        dict(
            aanpak="Elke lading is een geheel aantal elementaire ladingen. Schrijf Q is n maal e op "
                   "en vorm om naar wat gevraagd wordt; let daarna op het teken.",
            waarom=[
                "Let op het teken: elektronen missen betekent dat het negatieve deel weg is, dus "
                "blijft er positieve lading over. Het getal zelf verandert niet, enkel het teken.",
                "Let op dat een aantal elektronen altijd een geheel getal is. Kom je op 199,75 uit, "
                "dan rond je af op 200, want een deel van een elektron bestaat niet.",
                None,
                "Noem dat de uitkomst geen geheel getal is. Lading is gekwantiseerd, dus ze komt in "
                "hele pakjes e; dat is net de reden dat de waarde van e met zo veel cijfers gekend "
                "is.",
            ],
        ),
        dict(
            aanpak="Bij aanraken geldt maar één regel: de totale lading blijft gelijk, en twee even "
                   "grote bollen verdelen ze gelijk. Tel dus eerst de som en deel die daarna.",
            waarom=[
                "Let op dat de som genomen wordt met de tekens erbij: plus vier en min twee geven "
                "plus twee, en gedeeld door twee geeft dat plus één nanocoulomb elk.",
                "Let op dat A niet meer verandert nadat ze gescheiden zijn. Elke keer deel je enkel "
                "wat de twee bollen die elkaar nú aanraken samen dragen, en de som van de drie "
                "blijft plus negen nanocoulomb.",
                "Let op de tweede kolom: twee bollen die al evenveel dragen, wisselen bij een nieuw "
                "contact niets meer uit. Een tweede aanraking verandert dus niets.",
            ],
        ),
        dict(
            aanpak="Bij elke bewering gaat het over hetzelfde onderscheid: lading verschuiven is "
                   "niet hetzelfde als lading maken. Vraag je af of er iets nieuw ontstaat of enkel "
                   "verhuist.",
            waarom=[
                "Niet waar: bij wrijven verhuizen elektronen van de ene stof naar de andere. De ene "
                "wordt even negatief als de andere positief, dus de totale lading blijft nul.",
                None,
                "Niet waar: influentie werkt juist op afstand, zonder contact. Raak je aan, dan heet "
                "het laden door contact en krijg je hetzelfde teken.",
                None,
                "Niet waar: neutraal betekent even veel positieve als negatieve lading, niet geen "
                "lading. Juist daarom kan een neutraal voorwerp gepolariseerd worden.",
            ],
        ),
        dict(
            aanpak="Volg bij influentie de elektronen stap voor stap, en vraag je bij elke stap af "
                   "of er lading weg kan. Zonder aarding verschuift ze enkel; met aarding verdwijnt "
                   "ze echt.",
            waarom=[
                "Let op de tweede stap: de bol is nog altijd neutraal, ook al is de lading nu "
                "ongelijk verdeeld. Pas bij de aarding gaat er echt lading weg.",
                "Noem het verschil in één zin per geval. Bij contact vloeit lading over, dus "
                "hetzelfde teken; bij influentie met aarding wordt de gelijknamige lading "
                "weggeduwd, dus blijft het tegengestelde teken achter.",
                "Let op dat de blaadjes weer samenvallen: zonder aanraken is er niets weggevloeid, "
                "dus was de bol nooit echt geladen. De blaadjes blijven enkel uitstaan als je "
                "tussendoor geaard hebt.",
            ],
        ),
        dict(
            aanpak="Een goede uitleg heeft twee stappen: eerst hoe het voorwerp geladen raakt, dan "
                   "wat die lading met zijn omgeving doet. Schrijf ze apart, want er staan vaak twee "
                   "punten op.",
            waarom=[
                "Noem beide stappen. Eerst het wrijven dat elektronen verplaatst, dan de "
                "polarisatie van de muur: die wordt niet geladen, zijn moleculen draaien enkel, en "
                "de dichtste kant wordt lichtpositief.",
                None,
                "Noem dat het de stromende brandstof zelf is die laadt, door wrijving tegen de "
                "leiding. Zonder aarding kan die lading enkel weg via een vonk, en dampen van "
                "brandstof ontsteken daarmee.",
                "Noem ook de oplossing, want die is uitdrukkelijk gevraagd. Vochtige lucht geleidt, "
                "dus lekt de lading weg; droger maken of een betere isolatie helpt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-wet-van-coulomb-en-het-elektrisch-veld-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk waar de grootheid in de formule staat. De afstand staat in het kwadraat "
                   "onder de breuk, de ladingen staan gewoon boven, dus gedragen ze zich anders.",
            waarom=[
                "Let op de derde: de afstand drie keer zo groot geeft negen keer kleiner, dus twaalf "
                "gedeeld door negen is ongeveer 1,3 newton. Niet drie keer kleiner.",
                "Let op de tweede: verdubbelen beide ladingen, dan gaat de kracht maal twee en nog "
                "eens maal twee, dus maal vier.",
                "Noem het kwadraat uitdrukkelijk. De halve afstand in het kwadraat is een kwart van "
                "de afstand in het kwadraat, en een kwart in de noemer geeft maal vier.",
            ],
        ),
        dict(
            aanpak="Werk altijd in dezelfde orde: formule opschrijven, ladingen in coulomb zetten, "
                   "de afstand in meter kwadrateren, dan pas rekenen. Het teken van de ladingen "
                   "gebruik je enkel om te zeggen of ze aantrekken of afstoten.",
            waarom=[
                "Let op dat je met de absolute waarden rekent. De tekens zeggen enkel dat het hier "
                "om aantrekking gaat; ze mogen niet in de breuk terechtkomen, anders krijg je een "
                "negatieve kracht die niets betekent.",
                "Let op de wortel op het einde: je vindt eerst q in het kwadraat, en dan nog de "
                "wortel. Uit afstoting volgt dat de ladingen gelijknamig zijn, maar niet of ze beide "
                "positief of beide negatief zijn.",
                "Let op de richting. Voor de grootte neem je de absolute waarde van q, en het teken "
                "beslist pas daarna waar het veld naartoe wijst: naar een negatieve lading toe, van "
                "een positieve weg.",
            ],
        ),
        dict(
            aanpak="Twee ladingen tegelijk betekent twee krachten die je als pijlen optelt. Teken "
                   "dus eerst, want daaruit zie je of je de getallen moet aftrekken of optellen.",
            waarom=[
                "Let op dat de twee krachten hier tegengesteld gericht zijn, dus trek je ze af. De "
                "dichtste lading levert veel meer dan de verste, want de afstand staat in het "
                "kwadraat.",
                "Let op dat de k en de q wegvallen: je houdt enkel de verhouding van de kwadraten "
                "over. Het nulpunt ligt altijd dichter bij de kleinste lading, en dat is een goede "
                "controle op je uitkomst.",
                "Krachten zijn vectoren: staan ze niet op één lijn, dan moet je ontbinden in "
                "componenten. Enkel op één rechte mag je de getallen gewoon optellen of aftrekken.",
            ],
        ),
        dict(
            aanpak="E is de kracht per eenheid lading. Met F is E maal q kan je in beide richtingen "
                   "werken; zet de lading eerst in coulomb.",
            waarom=[
                "Let op de omzetting: 2 mC is twee maal tien tot de min drie coulomb. Vergeet je "
                "die, dan zit je er duizend keer naast.",
                None,
                "Noem beide schrijfwijzen. Newton per coulomb en volt per meter zijn dezelfde "
                "eenheid; de tweede gebruik je bij platen en spanning, de eerste bij een kracht op "
                "een lading.",
            ],
        ),
        dict(
            aanpak="Veldlijnen zijn een tekening van de richting van de kracht op een positieve "
                   "proeflading. Uit die ene afspraak volgen alle regels in deze reeks.",
            waarom=[
                "Let op het homogene veld tussen twee platen: daar lopen de lijnen parallel en op "
                "gelijke afstand, dus is het veld overal even sterk. Rond één puntlading lopen ze "
                "radiaal en wordt het veld zwakker naar buiten.",
                "Niet waar: in één punt heeft het veld maar één richting. Zouden twee lijnen er "
                "snijden, dan zou het veld daar twee richtingen hebben, en dat kan niet.",
                None,
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Deze vragen vragen een reden, niet een getal. Zeg telkens welke eigenschap van "
                   "het veld of van de formule je gebruikt.",
            waarom=[
                "Noem de kooi van Faraday. De lading blijft aan de buitenkant van het metaal en "
                "binnenin is het veld nul; dat je in een vliegtuig zit, verandert daar niets aan.",
                "Let op dat het antwoord nul is omdat de twee krachten even groot en tegengesteld "
                "zijn, niet omdat er geen kracht werkt. De middelste lading voelt beide buren wel.",
                "Noem één van elk, zoals gevraagd. Beide krachten nemen af met het kwadraat van de "
                "afstand, maar gravitatie kent enkel aantrekking en de coulombkracht beide tekens.",
                "Zoek beide fouten, want er staan er twee. De centimeter die niet omgezet werd, en "
                "de afstand die niet gekwadrateerd werd; samen verklaren die het verschil tussen "
                "zijn uitkomst en ongeveer twee newton.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektrische-energie-potentiaal-en-spanning-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Hou de symbolen uit elkaar voor je begint te rekenen: V is de potentiaal in één "
                   "punt, U het verschil tussen twee punten, en E is hier de veldsterkte en niet de "
                   "energie.",
            waarom=[
                "Let op de dubbele betekenis van E: in deze tabel staat E voor de veldsterkte in "
                "newton per coulomb, maar in andere formules staat E voor energie in joule. Enkel de "
                "eenheid maakt duidelijk welke van de twee bedoeld is.",
            ],
        ),
        dict(
            aanpak="W is q maal U, met de lading in coulomb en de spanning in volt. Vorm de formule "
                   "eerst om naar de gevraagde grootheid, en vul dan pas in.",
            waarom=[
                None,
                None,
                None,
                "Let op de omzetting: 250 microcoulomb is 250 maal tien tot de min zes coulomb. Zet "
                "die stap apart op papier, want dat is de fout die hier het vaakst gemaakt wordt.",
                "Let op het verschil tussen deze vraag en de vorige. Met een potentiaal in één punt "
                "reken je de energie in dat punt, dus Ep is q maal V; met een spanning reken je de "
                "energie die vrijkomt op de weg tussen twee punten.",
            ],
        ),
        dict(
            aanpak="Elke grootheid is hier per eenheid van lading: de potentiaal is de energie per "
                   "lading, de veldsterkte de kracht per lading. Zeg bij elke definitie dus ook per "
                   "wat.",
            waarom=[
                None,
                "Let op het dubbele minteken: tachtig min min twintig is honderd. Een negatieve "
                "potentiaal is gewoon een getal onder nul en geen fout.",
                "Let op de centimeters: vijf centimeter is 0,050 meter. U gedeeld door d geeft volt "
                "per meter, en dat is dezelfde eenheid als newton per coulomb.",
                None,
                "Niet waar: een positieve lading beweegt vanzelf van hoge naar lage potentiaal, net "
                "zoals een steen vanzelf naar beneden valt. Een negatieve lading doet het omgekeerde.",
                None,
                "Niet waar: de potentiaal in een punt is een eigenschap van het veld, niet van de "
                "lading die je erin zet. Wat wel groter wordt, is de energie van die lading.",
            ],
        ),
        dict(
            aanpak="De energie die het deeltje wint, wordt kinetische energie: q maal U is een half "
                   "m v kwadraat. Vorm om naar v en reken pas op het einde de wortel.",
            waarom=[
                "Let op de factor twee die uit het een half komt: v is de wortel uit twee q U "
                "gedeeld door m. Vergeet je die twee, dan zit je er een factor 1,4 naast.",
                "Noem dat de energie dezelfde is en enkel de massa verschilt. Een proton is ongeveer "
                "1836 keer zwaarder, en de snelheid gaat met de wortel daarvan, dus ongeveer 43 keer "
                "trager.",
                "Let op dat de lading van een alfadeeltje twee keer de elementaire lading is, dus "
                "wint het bij dezelfde spanning dubbel zo veel energie. In elektronvolt kan je het "
                "zonder rekenen zien: twee keer duizend volt is tweeduizend elektronvolt.",
            ],
        ),
        dict(
            aanpak="Schrijf bij een vraagstuk eerst op wat gegeven is en welke formule de twee "
                   "verbindt. Vaak heb je er twee nodig: eerst het veld, dan de kracht.",
            waarom=[
                "Let op de twee stappen: eerst E is U gedeeld door d, dan F is E maal q met de "
                "elementaire lading. Die tweede stap vergeten is de klassieke fout hier.",
                "Let op dat de potentiaal als een gewoon getal optelt, met zijn teken erbij. Plus en "
                "min heffen elkaar op, dus V is nul, terwijl het veld daar juist maximaal is: dat "
                "zijn twee verschillende dingen.",
                "Let op de voorwaarde die in het woord stil zit: zweeft het deeltje stil, dan is de "
                "elektrische kracht precies gelijk aan het gewicht. Die ene gelijkheid geeft je de "
                "hele oplossing.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen gaan over het verschil tussen een potentiaalverschil en een "
                   "potentiaal, en tussen een getal en een vector. Zeg telkens welk van de twee je "
                   "gebruikt.",
            waarom=[
                "Noem dat V niet verandert. Op een equipotentiaallijn is het potentiaalverschil nul, "
                "dus is de arbeid nul; de kracht staat er loodrecht op, en loodrecht op de "
                "verplaatsing levert geen arbeid.",
                "Noem dat het om het verschil tussen zijn pootjes gaat. Dat de draad zelf op "
                "duizenden volt staat, maakt niets uit; zou de vogel ook de grond of een tweede "
                "draad raken, dan was er wel een groot verschil.",
                "Noem dat het verlies met de stroom in het kwadraat gaat. Bij hetzelfde vermogen "
                "geeft een hoge spanning een kleine stroom, en de helft minder stroom betekent vier "
                "keer minder verlies.",
                "Noem dat V een getal is en E een vector. Twee tegengestelde potentialen tellen weg "
                "tot nul, maar twee velden die dezelfde kant op wijzen tellen op.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektrodynamica-stroom-weerstand-en-schakelingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="U is R maal I, en I is de lading per seconde. Zet de tijd altijd in seconden en "
                   "de stroom in ampère voor je invult.",
            waarom=[
                None,
                None,
                "Let op dat de stroom de lading per seconde is, dus coulomb gedeeld door seconden. "
                "Eén ampère is precies één coulomb per seconde, en dat is de hele definitie.",
                "Let op de minuten: vijf minuten is 300 seconden. Werk je met minuten, dan is je "
                "antwoord zestig keer te klein.",
            ],
        ),
        dict(
            aanpak="In serie tel je de weerstanden gewoon op. Parallel tel je de omgekeerden op, en "
                   "bij twee weerstanden mag je het product gedeeld door de som gebruiken.",
            waarom=[
                None,
                "Let op dat het product gedeeld door de som enkel bij twee weerstanden mag. Bij drie "
                "moet je met de omgekeerden werken.",
                "Let op de snelle regel: n gelijke weerstanden parallel geven de weerstand gedeeld "
                "door n. Dat is hetzelfde als drie keer een dertigste optellen.",
                "Let op dat je hier met de omgekeerden moet werken en niet gewoon aftrekken. Eén "
                "gedeeld door acht min één gedeeld door vierentwintig geeft twee vierentwintigsten, "
                "en dan nog omkeren.",
                "Noem dat elke tak een extra weg is. Bij dezelfde spanning loopt er in totaal meer "
                "stroom dan door de kleinste tak alleen, en meer stroom bij dezelfde spanning "
                "betekent een kleinere weerstand.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke eigenschap af wat dezelfde blijft: in serie de stroom, "
                   "parallel de spanning. Uit die twee volgen alle andere kenmerken.",
            waarom=[
                None,
                "Let op het verschil tussen de twee laatste: in serie onderbreekt één stuk de hele "
                "kring, parallel heeft elke tak zijn eigen weg. Dat is precies waarom een huis "
                "parallel geschakeld is.",
            ],
        ),
        dict(
            aanpak="Reken altijd in dezelfde orde: eerst de vervangingsweerstand, dan de "
                   "hoofdstroom, dan pas de deelspanningen. Controleer op het einde of de "
                   "deelspanningen samen de bronspanning geven.",
            waarom=[
                "Let op de controle op het einde: acht plus twaalf plus twintig is veertig volt, dus "
                "precies de bronspanning. In serie moet die som altijd kloppen.",
                "Let op de controle: de twee takstromen samen geven de hoofdstroom, en de "
                "vervangingsweerstand uit die hoofdstroom moet kloppen met het product gedeeld door "
                "de som.",
                "Let op de orde: eerst het parallelle stuk tot één weerstand herleiden, en dan pas "
                "optellen bij de weerstand in serie. Over het parallelle stuk staat de spanning die "
                "bij diezelfde hoofdstroom hoort.",
            ],
        ),
        dict(
            aanpak="P is U maal I, en met de wet van Ohm erbij ook R maal I kwadraat of U kwadraat "
                   "gedeeld door R. Kies de vorm waarvan je de twee grootheden hebt.",
            waarom=[
                None,
                None,
                "Let op dat een kilowattuur een eenheid van energie is en geen vermogen. Reken het "
                "vermogen in kilowatt en de tijd in uren, dan valt de omzetting weg.",
                "Let op dat je hier R maal I kwadraat neemt, want je kent de spanning niet. En "
                "vermogen in watt is al joule per seconde, dus het antwoord staat er meteen.",
            ],
        ),
        dict(
            aanpak="Zeg bij elke vraag eerst of het om een serie- of een parallelschakeling gaat, en "
                   "welke formule daaruit volgt. Dan schrijft het antwoord zich bijna zelf.",
            waarom=[
                "Noem beide gevolgen: de totale weerstand stijgt dus de stroom daalt, en diezelfde "
                "bronspanning moet nu over meer lampjes verdeeld worden. Daarom branden ze alle "
                "zwakker, niet enkel het nieuwe.",
                "Noem beide redenen, want er zijn er twee. Elk toestel krijgt de volle 230 volt, en "
                "een toestel dat uitvalt onderbreekt de rest niet.",
                "Noem de twee formules samen. Het verlies gaat met de stroom in het kwadraat, en een "
                "dikkere kabel heeft een grotere doorsnede en dus een kleinere weerstand.",
                "Noem waar elk toestel staat. Een ampèremeter staat in serie en mag de stroom niet "
                "verkleinen; een voltmeter staat parallel en mag geen stroom wegtrekken van het "
                "onderdeel dat ze meet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-magneten-en-het-magnetisch-veld-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee regels dekken deze hele reeks: gelijke polen stoten af, en enkel ijzer, "
                   "nikkel en kobalt worden aangetrokken. Alle andere metalen niet.",
            waarom=[
                None,
                "Let op dat een spoel met stroom zich net als een staafmagneet gedraagt, met een "
                "noord- en een zuidkant. Dezelfde regel over polen geldt dus ook voor twee spoelen.",
                "Let op koper: het is een uitstekende geleider van elektriciteit maar wordt niet "
                "aangetrokken. Goed geleiden en magnetisch zijn hebben niets met elkaar te maken.",
                "Let op aluminium: ook een metaal, en ook niet magnetisch. De drie die wel werken "
                "zijn ijzer, nikkel en kobalt, en dat rijtje is het waard om vanbuiten te kennen.",
            ],
        ),
        dict(
            aanpak="Zet de voorvoegsels om naar machten van tien, en hou de twee eenheden uit "
                   "elkaar: de tesla is de officiële eenheid, de gauss een oudere die tienduizend "
                   "keer kleiner is.",
            waarom=[
                None,
                "Let op dat gauss de kleinere eenheid is, dus wordt het getal groter: 1,5 tesla is "
                "15 000 gauss. Vermenigvuldig met tien tot de vierde, niet delen.",
                "Let op de weissgebieden: dat zijn hele gebiedjes waarin de magneetjes al gelijk "
                "staan, niet de magneetjes zelf. Magnetiseren betekent die gebiedjes gelijk richten.",
                "Let op het verschil tussen de twee: de rechterhandregel geeft de zin van het veld, "
                "de flux is een hoeveelheid veldlijnen door een oppervlak.",
                "Let op de curietemperatuur: boven die temperatuur schudt de warmte de "
                "weissgebieden door elkaar, dus verliest ijzer zijn magnetisme. Voor ijzer ligt ze "
                "rond 770 graden celsius.",
            ],
        ),
        dict(
            aanpak="Reken met mu nul gedeeld door twee pi als twee maal tien tot de min zeven, dan "
                   "blijft er enkel I gedeeld door r over. Zet de afstand altijd in meter.",
            waarom=[
                None,
                None,
                "Let op de twee centimeter: dat is 0,020 meter. Vorm de formule eerst om naar I en "
                "vul dan pas in.",
                "Let op wat de vraag betekent: je zoekt de afstand waarop het veld van de draad even "
                "sterk is als dat van de aarde. Het aardveld is dus de gegeven B, en je vormt om "
                "naar r.",
                "Let op dat de afstand hier gewoon in de noemer staat, dus vier keer verder geeft "
                "vier keer zwakker. Niet zestien keer: dat zou gelden bij een kwadraat.",
                "Let op dat de twee veranderingen elkaar hier opheffen. Stroom en afstand beide maal "
                "twee laat de verhouding I op r gelijk, dus blijft B dezelfde.",
                "Reken met de verhouding, zoals gevraagd: maal drie door de stroom en gedeeld door "
                "zes door de afstand geeft samen de helft. Dat is sneller en veiliger dan opnieuw "
                "invullen.",
            ],
        ),
        dict(
            aanpak="In een spoel telt enkel het aantal windingen per meter, niet het aantal "
                   "windingen alleen. Reken dus eerst N gedeeld door de lengte uit, en vul dat in.",
            waarom=[
                "Let op dat je eerst N gedeeld door de lengte neemt: 500 windingen op 0,25 meter is "
                "2000 per meter. Vul je 500 in, dan zit je er een factor vier naast.",
                None,
                None,
                "Let op dat hier naar windingen per meter gevraagd wordt en niet naar een aantal "
                "windingen. Je antwoord is dus een getal per meter, en de lengte van de spoel speelt "
                "geen rol.",
                "Noem dat enkel de windingdichtheid verschilt. Even veel windingen op de halve "
                "lengte geeft dubbel zo veel per meter, dus een twee keer zo sterk veld.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke bewering af of ze over een magneet, een rechte draad of een "
                   "spoel gaat. De drie gedragen zich anders, en juist dat wordt hier getoetst.",
            waarom=[
                "Niet waar: je krijgt twee kleinere magneten, elk met een noord- en een zuidpool. "
                "Een losse pool bestaat niet, en daarin verschilt magnetisme van elektrische lading.",
                None,
                "Waar, en dat verrast vaak. De noordpool van een kompasnaald wijst naar het "
                "geografische noorden, dus moet daar een magnetische zuidpool liggen, want "
                "ongelijke polen trekken aan.",
                "Niet waar: de veldlijnen van een rechte draad zijn cirkels rond de draad. Zet je "
                "duim in de zin van de stroom, dan geven je vingers de zin van die cirkels.",
                None,
                "Niet waar: bij een rechte draad daalt het veld met de afstand zelf, dus met één op "
                "r. Het kwadraat hoort bij een puntlading of een puntmassa.",
                None,
                "Niet waar: de tesla is een heel grote eenheid. Een koelkastmagneet zit rond enkele "
                "millitesla, een MRI-toestel rond anderhalf tot drie tesla.",
            ],
        ),
        dict(
            aanpak="Deze vragen vragen een reden. Zeg telkens welk beeld je gebruikt: de "
                   "weissgebieden, het aardveld of de manier waarop het veld zich in de ruimte "
                   "spreidt.",
            waarom=[
                "Noem de weissgebieden. In ijzer staan er magneetjes die je gelijk kan richten, in "
                "koper zijn er geen, dus valt er niets te richten.",
                "Noem beide delen van de vraag. De naald draait zich in het aardveld, en een magneet "
                "dichtbij maakt een veel sterker veld ter plaatse, dus wint die het van de aarde.",
                "Noem er drie, zoals gevraagd: meer stroom, meer windingen per meter, en een kern "
                "van zacht ijzer. Zacht ijzer, want dat laat zijn magnetisme weer los als de stroom "
                "wegvalt.",
                "Noem hoe het veld zich spreidt. Rond een punt spreidt het over een bol, en de "
                "oppervlakte van een bol gaat met r in het kwadraat; rond een lange draad spreidt "
                "het enkel over een cilinder, en de omtrek gaat met r. Eén richting minder geeft één "
                "macht minder.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-magnetische-kracht-op-een-stroom-en-op-een-lading-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="F is B maal I maal de lengte, en de sinus van de hoek erbij. Staat er geen hoek, "
                   "dan is de sinus één en valt hij weg.",
            waarom=[
                None,
                None,
                None,
                "Let op de 25 centimeter: dat is 0,25 meter. Een lengte in centimeter laten staan "
                "geeft een antwoord dat honderd keer te klein is.",
                "Let op de sinus van dertig graden: die is precies een half, dus halveert de kracht. "
                "Dat is een waarde die het waard is vanbuiten te kennen.",
                "Let op de sinus van vijfenveertig graden: ongeveer 0,71, dus iets meer dan twee "
                "derde van de volle kracht. Reken eerst de kracht zonder hoek en vermenigvuldig dan.",
            ],
        ),
        dict(
            aanpak="De lorentzkracht is q maal v maal B, met de sinus van de hoek tussen de snelheid "
                   "en het veld. Werk met machten van tien en tel de exponenten op.",
            waarom=[
                None,
                "Let op dat je voor een elektron de elementaire lading neemt, zonder het minteken. "
                "Het teken bepaalt enkel de kant waar de kracht naartoe wijst, niet de grootte.",
                "Let op dat de massa hier geen rol speelt: in de formule voor de kracht staat enkel "
                "de lading. Een proton en een elektron met dezelfde snelheid voelen dezelfde kracht, "
                "maar het elektron buigt veel sterker af.",
                None,
                "Noem de sinus van nul. Beweegt de lading langs de veldlijnen, dan is er geen "
                "component dwars op het veld, dus geen kracht. Dat is het enige geval waarin een "
                "bewegende lading in een magnetisch veld niets voelt.",
            ],
        ),
        dict(
            aanpak="De magnetische kracht is hier de middelpuntzoekende kracht, en daaruit volgt r "
                   "is m v gedeeld door q B. Let erop dat in de omlooptijd geen snelheid staat.",
            waarom=[
                None,
                "Let op dat een elektron een veel kleinere bocht maakt dan een proton, ook al is het "
                "sneller: zijn massa is bijna tweeduizend keer kleiner, en de straal gaat met de "
                "massa.",
                "Let op dat je hier de omlooptijd neemt en niet de omtrek gedeeld door de snelheid. "
                "Beide geven hetzelfde, maar de formule met T is korter en je hebt de snelheid niet "
                "nodig.",
                "Let op dat bij dezelfde lading en snelheid de straal gewoon met de massa gaat. De "
                "verhouding van de stralen is dus de verhouding van de massa's, en dat is precies "
                "waarop een massaspectrometer werkt.",
                "Noem beide stukken van de snelheid. Het deel langs het veld gaat onveranderd door, "
                "het deel dwars erop maakt een cirkel, en samen geeft dat een schroeflijn.",
            ],
        ),
        dict(
            aanpak="Kijk waar de grootheid in de formule staat: boven de breuk geeft recht "
                   "proportioneel, onder de breuk omgekeerd. Veranderen er twee, dan combineer je de "
                   "twee effecten.",
            waarom=[
                "Let op de sinus: van negentig naar dertig graden gaat de sinus van één naar een "
                "half, dus halveert de kracht. De hoek zelf delen door drie zou een heel ander "
                "antwoord geven.",
                "Let op het laatste geval: ligt de draad evenwijdig met het veld, dan is de hoek nul "
                "en de sinus ook, dus is er geen kracht.",
                None,
                "Let op dat snelheid en veld beide verdubbelen: de een staat boven en de ander onder "
                "de breuk, dus heffen ze elkaar op en blijft de straal gelijk.",
            ],
        ),
        dict(
            aanpak="Alle beweringen hier draaien om één eigenschap: de magnetische kracht staat "
                   "loodrecht op de snelheid. Uit die ene eigenschap volgen de meeste antwoorden.",
            waarom=[
                None,
                "Niet waar: in de formule staat de snelheid, dus zonder beweging is er geen "
                "magnetische kracht. Een stilstaande lading voelt wel een elektrische kracht als er "
                "een elektrisch veld is.",
                "Niet waar: de kracht staat loodrecht op de snelheid, dus levert ze geen arbeid en "
                "verandert de kinetische energie niet. Enkel de richting draait.",
                None,
                "Waar, en dat verrast vaak. Twee draden met stroom in dezelfde zin trekken elkaar "
                "aan; staat de stroom in tegengestelde zin, dan stoten ze af. Juist het omgekeerde "
                "van wat je bij twee gelijke ladingen verwacht.",
                "Niet waar: de weerstand staat niet in deze formule. Ze bepaalt wel hoe groot de "
                "stroom bij een gegeven spanning wordt, maar voor de kracht gebruik je enkel de "
                "stroom zelf.",
                None,
            ],
        ),
        dict(
            aanpak="Zeg bij elke toepassing welke formule erachter zit. De massaspectrometer leeft "
                   "van de straal, het cyclotron van de omlooptijd, de motor van het koppel.",
            waarom=[
                "Let op het verschil in richting: een massaspectrometer meet en scheidt, een "
                "elektromotor zet energie om in beweging. Beide gebruiken wel dezelfde kracht.",
                "Let op de hallsensor: die meet een veld door de spanning die dwars over een "
                "stroomvoerend plaatje ontstaat. Hij zit in elke fietscomputer en in elk toestel dat "
                "weet of de klep dicht is.",
                "Noem de arbeid. Een kracht loodrecht op de verplaatsing levert geen arbeid, dus "
                "blijft de kinetische energie en daarmee de grootte van de snelheid gelijk.",
                "Noem het koppel en de collector. Op de twee zijden van de lus werken krachten in "
                "tegengestelde zin, dus draait de as; zonder omkeren van de stroom zou ze na een "
                "halve ronde stilvallen.",
                "Noem dat de omlooptijd niet van de snelheid afhangt. Een sneller deeltje maakt een "
                "ruimere bocht en legt dus een langere weg af in dezelfde tijd, waardoor het ritme "
                "van de duwtjes mag blijven zoals het is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektromagnetische-inductie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist alles: verandert de flux door de spoel. Verandert ze niet, dan "
                   "is er geen inductiespanning, hoe sterk het veld ook is.",
            waarom=[
                "Let op de eerste: een magneet stilhouden geeft niets, ook al zit hij middenin de "
                "spoel. Enkel de verandering telt, niet de aanwezigheid van het veld.",
                "Let op de laatste: de twee spoelen raken elkaar niet aan, maar de stroom in de ene "
                "verandert het veld door de andere. Dat is precies hoe een transformator werkt.",
            ],
        ),
        dict(
            aanpak="De flux is B maal de oppervlakte maal de cosinus van de hoek met de normaal. "
                   "Let goed op: de hoek wordt gemeten met de normaal op het vlak, niet met het vlak "
                   "zelf.",
            waarom=[
                None,
                "Let op de cosinus van zestig graden: die is een half. Bij flux werk je met de "
                "cosinus, bij de kracht op een draad met de sinus, en die twee verwisselen is de "
                "fout die het vaakst gemaakt wordt.",
                None,
                None,
                "Noem de hoek met de normaal. Ligt de winding plat in het veld, dan staat de normaal "
                "dwars op de veldlijnen, dus is de hoek negentig graden en de cosinus nul: geen "
                "enkele veldlijn gaat erdoor.",
            ],
        ),
        dict(
            aanpak="De inductiespanning is het aantal windingen maal de fluxverandering per "
                   "seconde. Reken dus eerst de verandering van de flux uit, en deel dan pas door de "
                   "tijd.",
            waarom=[
                None,
                "Let op dat het aantal windingen gewoon als factor vooraan staat. Vijftig windingen "
                "geven vijftig keer meer spanning bij dezelfde fluxverandering.",
                None,
                None,
                "Let op de twee stappen: eerst de flux uit B maal de oppervlakte, en dan pas de wet "
                "van Faraday. Met het veld rechtstreeks in de formule van Faraday invullen kan niet.",
                "Let op dat beide veranderingen hetzelfde effect hebben: tweemaal zoveel windingen "
                "en dezelfde verandering in de halve tijd geven allebei een dubbele spanning.",
                "Let op het laatste geval: blijft de flux een tijdlang gelijk, dan is de verandering "
                "nul en dus ook de spanning, hoe groot die flux ook is.",
            ],
        ),
        dict(
            aanpak="Een transformator verdeelt de spanning in verhouding tot de windingen. Is hij "
                   "ideaal, dan blijft het vermogen gelijk, dus gaat de stroom juist de andere kant "
                   "op.",
            waarom=[
                None,
                None,
                None,
                "Let op dat je hier via het vermogen werkt en niet via de windingen. Minder spanning "
                "primair bestaat niet: de spanning gaat naar beneden en de stroom dus naar boven aan "
                "de secundaire kant, en primair loopt er juist minder.",
                "Noem beide formules, zoals gevraagd. Hetzelfde vermogen bij hogere spanning geeft "
                "een kleinere stroom, en het verlies gaat met die stroom in het kwadraat.",
            ],
        ),
        dict(
            aanpak="Hou de drie namen uit elkaar: de wet van Faraday zegt hoe groot de spanning is, "
                   "de wet van Lenz welke kant de stroom op loopt, en de weber is de eenheid van de "
                   "flux.",
            waarom=[
                "Let op de wet van Lenz: die gaat over de zin van de inductiestroom, en daarom staat "
                "er een minteken in de formule van Faraday.",
                None,
                None,
                None,
                None,
                "Niet waar: op gelijkspanning verandert de flux niet, dus komt er aan de secundaire "
                "kant niets uit. Een transformator heeft wisselspanning nodig.",
                "Waar, en dat is de reden achter het minteken: zou de stroom de verandering "
                "versterken, dan kwam er energie uit het niets.",
                "Niet waar: in de formule staat enkel de verandering van de flux, niet de flux zelf. "
                "Een grote flux die niet verandert, geeft geen spanning.",
                None,
            ],
        ),
        dict(
            aanpak="Elk van deze drie vragen leeft van de wet van Lenz: de inductiestroom werkt de "
                   "verandering tegen. Zeg dat uitdrukkelijk in je antwoord.",
            waarom=[
                "Noem de wervelstromen en de wet van Lenz samen. De vallende magneet wekt in het "
                "koper kringstromen op, en die maken een veld dat de val tegenwerkt; het koper zelf "
                "is niet magnetisch.",
                "Noem het behoud van energie. Een stroom die de verandering versterkt, zou zichzelf "
                "blijven aandrijven, en dan kwam er energie uit het niets.",
                "Noem waarom het glas koel blijft. De wervelstromen ontstaan enkel in metaal dat "
                "stroom geleidt, dus in de bodem van de pan; het glas geleidt niet en wordt enkel "
                "warm door de pan erop.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-statica-krachten-moment-en-evenwicht-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet bij elke vraag eerst de juiste formule neer en reken in SI-eenheden: meter, "
                   "kilogram, newton. Let op welke waarde van g gevraagd wordt.",
            waarom=[
                None,
                "Let op de twee stappen: eerst de normaalkracht, die hier gelijk is aan het gewicht, "
                "en dan pas de wrijving. De massa rechtstreeks met de wrijvingscoëfficiënt "
                "vermenigvuldigen geeft een getal zonder betekenis.",
                "Let op de centimeters: vijftien centimeter is 0,15 meter. De veerconstante staat in "
                "newton per meter, dus moet de uitrekking ook in meter.",
                None,
                "Let op de sinus bij een helling: de component langs het vlak is het gewicht maal de "
                "sinus, de component dwars erop maal de cosinus. Bij dertig graden is de sinus "
                "precies een half.",
            ],
        ),
        dict(
            aanpak="Liggen twee krachten op één lijn, dan tel je op of trek je af. Staan ze "
                   "loodrecht, dan gebruik je Pythagoras; in alle andere gevallen ontbind je in "
                   "componenten.",
            waarom=[
                "Let op het derde geval: dertig en veertig loodrecht geven vijftig, en dat is "
                "minder dan de som maar meer dan het verschil. De drie uitkomsten samen laten mooi "
                "zien hoe de hoek het antwoord bepaalt.",
                "Let op dat dit twee bekende pythagorasdrietallen zijn: negen, twaalf, vijftien en "
                "vijf, twaalf, dertien. Herken je die, dan reken je ze zonder rekenmachine.",
                "Noem dat een kracht een vector is. Ze heeft een grootte en een richting, dus stel "
                "je ze samen met de parallellogramregel of met Pythagoras en niet met een gewone "
                "som.",
            ],
        ),
        dict(
            aanpak="Het moment is de kracht maal de arm, met de sinus van de hoek tussen de kracht "
                   "en de stang. De arm is de afstand tot het draaipunt, in meter.",
            waarom=[
                None,
                None,
                None,
                "Let op de sinus van dertig graden: een half, dus het halve moment. Vergelijk dit "
                "met de volgende oefening, waar dezelfde kracht loodrecht werkt.",
                "Let op dat het moment hier het dubbele is van de vorige oefening, met precies "
                "dezelfde kracht en arm. Loodrecht duwen levert altijd het grootste moment.",
                "Noem de werklijn. Werkt de kracht langs de stang, dan gaat haar werklijn door het "
                "draaipunt en is de arm nul, dus het moment ook. Duw je een deur naar de scharnieren "
                "toe, dan draait ze niet.",
            ],
        ),
        dict(
            aanpak="In rotatie-evenwicht zijn de momenten aan beide zijden even groot: kracht links "
                   "maal arm links is kracht rechts maal arm rechts. Vorm die ene gelijkheid om naar "
                   "wat gevraagd wordt.",
            waarom=[
                None,
                None,
                "Let op dat je hier met massa's mag rekenen in plaats van met gewichten: de g valt "
                "aan beide kanten weg. Het zwaardere kind zit altijd dichter bij het draaipunt.",
                "Let op de keuze van het draaipunt: neem je de rechtersteun, dan valt die onbekende "
                "kracht weg omdat haar arm nul is. Daarna vind je de tweede steun met de som van de "
                "krachten.",
            ],
        ),
        dict(
            aanpak="Evenwicht heeft twee voorwaarden: de som van de krachten nul en de som van de "
                   "momenten nul. Vraag je bij elke bewering af over welke van de twee ze gaat.",
            waarom=[
                "Niet waar: ook een voorwerp dat met een constante snelheid beweegt is in evenwicht. "
                "Evenwicht betekent geen versnelling, niet geen beweging.",
                None,
                None,
                "Niet waar: er werkt ook de normaalkracht van de tafel, en die is precies even groot "
                "en tegengesteld. Zonder die tweede kracht zou het voorwerp vallen.",
                None,
                "Niet waar, het is net omgekeerd: zolang het zwaartepunt bóven het steunvlak blijft, "
                "kantelt het voorwerp niet. Komt het erbuiten, dan valt het om.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een reden. Noem telkens of het om de arm, het "
                   "zwaartepunt of het evenwicht van momenten gaat.",
            waarom=[
                "Noem de arm. Aan de kruk is de afstand tot de scharnieren veel groter, dus volstaat "
                "een kleinere kracht voor hetzelfde moment.",
                "Noem beide: een laag zwaartepunt en een breed steunvlak. Juist de combinatie van de "
                "twee maakt dat je ver moet kantelen voor het zwaartepunt buiten het steunvlak komt.",
                "Noem het evenwicht van momenten rond de mast. Het blok achteraan levert een moment "
                "in de andere zin dan de last vooraan, en daarom blijft de kraan staan.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-wetten-van-newton-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af waar de uitspraak over gaat. Over een lichaam zonder resultante is "
                   "de eerste, over een verband tussen kracht en versnelling de tweede, over twee "
                   "lichamen die op elkaar duwen de derde.",
            waarom=[
                None,
                "Let op de tweede: een raket is de derde wet, want er zijn twee lichamen in het "
                "spel, de raket en het gas. De laatste is de tweede wet, want dezelfde kracht geeft "
                "een lichtere kar een grotere versnelling.",
            ],
        ),
        dict(
            aanpak="Reken altijd met de resulterende kracht, dus met alles samen wat op het voorwerp "
                   "werkt. Vorm F is m maal a om naar wat gevraagd wordt.",
            waarom=[
                None,
                None,
                "Let op dat een gewicht een kracht is, dus in newton. Vijftien kilogram is de massa, "
                "en 147 newton het gewicht op aarde.",
                "Let op dat je eerst de resultante moet nemen: negentig newton trekken min vijftien "
                "newton wrijving is vijfenzeventig newton. Met de volle negentig rekenen geeft een te "
                "grote versnelling.",
                "Let op de twee stappen: eerst de versnelling uit de snelheidsverandering per "
                "seconde, dan de kracht. De snelheid rechtstreeks in F is m maal a invullen kan niet.",
                "Let op het teken: de versnelling is negatief omdat de snelheid daalt, maar de "
                "grootte van de remkracht is gewoon 4800 newton. Zeg erbij dat ze tegen de "
                "rijrichting in werkt.",
            ],
        ),
        dict(
            aanpak="In a is F gedeeld door m staat de kracht boven en de massa onder. Dus meer "
                   "kracht geeft meer versnelling, meer massa minder.",
            waarom=[
                None,
                "Let op het eerste geval: kracht maal vier en massa maal twee geeft samen maal twee. "
                "Reken de twee effecten na elkaar en je kan ze niet verwisselen.",
            ],
        ),
        dict(
            aanpak="Massa en gewicht zijn twee verschillende dingen: massa is hoeveel stof er is en "
                   "staat in kilogram, gewicht is een kracht en staat in newton.",
            waarom=[
                None,
                "Let op de traagheid: dat is precies wat massa betekent, namelijk hoe moeilijk het "
                "is om iets van snelheid te doen veranderen. Op de maan is je massa dezelfde en je "
                "gewicht ongeveer zes keer kleiner.",
            ],
        ),
        dict(
            aanpak="Alle beweringen hier draaien om twee dingen: zonder resultante verandert de "
                   "snelheid niet, en actie en reactie werken op verschillende lichamen.",
            waarom=[
                "Niet waar: zonder resultante blijft de snelheid gelijk, en die kan ook een andere "
                "waarde dan nul hebben. Stilstaan en met een constante snelheid bewegen zijn voor "
                "Newton hetzelfde geval.",
                None,
                "Niet waar: ze werken op twee verschillende lichamen, dus kunnen ze elkaar niet "
                "opheffen. Opheffen kan enkel bij twee krachten op hetzelfde lichaam.",
                None,
                "Niet waar: de massa staat in de noemer. Juist daarom versnelt een zwaarder voorwerp "
                "minder bij dezelfde kracht.",
                None,
            ],
        ),
        dict(
            aanpak="Zeg bij elke uitleg welke wet je gebruikt, en bij de derde wet ook op welke twee "
                   "lichamen de krachten werken. Dat is wat deze vragen echt toetsen.",
            waarom=[
                "Noem de eerste wet. Jij houdt je snelheid, de bus vertraagt, en daarom schuif je "
                "naar voren ten opzichte van de bus. Er duwt je dus niets naar voren.",
                "Noem dat de twee krachten op verschillende lichamen werken. Op de raket zelf blijft "
                "één kracht over, namelijk die van het gas, en die versnelt hem.",
                "Noem dat de vloer harder duwt dan je gewicht. Ze moet je gewicht dragen en je "
                "bovendien versnellen, en die extra kracht voel je.",
                "Noem dat de massa wegvalt. Uit m g is m a volgt a is g, en dat is dezelfde "
                "versnelling voor elk voorwerp, licht of zwaar. In lucht verstoort de wrijving dat "
                "beeld.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-rechtlijnige-beweging-erb-en-evrb-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: verandert de snelheid. Blijft ze gelijk, dan is het een ERB; "
                   "verandert ze gelijkmatig, dan is het een EVRB.",
            waarom=[
                "Let op dat ook een vrije val en een gelijkmatige vertraging EVRB zijn. Het woord "
                "versneld in de naam sluit vertragen niet uit.",
                None,
                "Let op het verschil tussen de grafieken: bij een EVRB stijgt of daalt de v,t-"
                "grafiek schuin, bij een ERB loopt ze horizontaal. Een rechte in een x,t-grafiek "
                "hoort juist bij een ERB.",
            ],
        ),
        dict(
            aanpak="Bij een ERB is de afstand gewoon de snelheid maal de tijd. Zet km per uur eerst "
                   "om naar meter per seconde door te delen door 3,6.",
            waarom=[
                None,
                None,
                "Let op de richting van de omzetting: van meter per seconde naar kilometer per uur "
                "vermenigvuldig je met 3,6, omgekeerd deel je erdoor. Twijfel je, denk dan aan "
                "wandelen: ongeveer 1 meter per seconde is ongeveer 4 kilometer per uur.",
                "Let op het verschil tussen de afgelegde weg en de verplaatsing. De weg is 2,4 "
                "kilometer, maar de verplaatsing is nul, want de wandelaar staat weer op zijn "
                "vertrekpunt.",
            ],
        ),
        dict(
            aanpak="Kies de formule naar wat je mist. Heb je de tijd, neem dan de vormen met t; heb "
                   "je de tijd niet maar wel de afstand, neem dan de formule met v kwadraat.",
            waarom=[
                None,
                "Let op het kwadraat van de tijd: zes seconden geeft zesendertig, en daarna nog de "
                "helft van de versnelling. Niet de snelheid maal de tijd, want die snelheid "
                "verandert voortdurend.",
                None,
                "Let op dat je hier de formule zonder tijd neemt, want de tijd is niet gegeven. De "
                "remweg is het kwadraat van de snelheid gedeeld door twee keer de vertraging.",
                "Let op dat je met het kwadraat van beide snelheden rekent: 64 min 4 en niet 8 min "
                "2. Dat is de meest gemaakte fout bij deze formule.",
            ],
        ),
        dict(
            aanpak="Een vrije val is een EVRB met a gelijk aan g. Een bal die je omhoog gooit, "
                   "vertraagt met dezelfde g, dus kan je dezelfde formules gebruiken.",
            waarom=[
                None,
                None,
                "Let op dat je hier de formule zonder tijd nodig hebt: de hoogte is het kwadraat van "
                "de snelheid gedeeld door twee keer g.",
                "Let op dat dit dezelfde formule is als de vorige, maar omgekeerd gebruikt: bovenaan "
                "is de snelheid nul, dus wordt de beginsnelheid helemaal hoogte.",
                "Noem dat de tijd in het kwadraat staat. Dubbel zo lang vallen is dus vier keer zo "
                "diep, en dat is ook de reden dat een val van tien meter zo veel gevaarlijker is dan "
                "een val van twee en een halve meter.",
            ],
        ),
        dict(
            aanpak="Een grafiek lees je met twee vragen: wat is de helling, en wat is de oppervlakte "
                   "eronder. Die twee geven telkens een andere grootheid.",
            waarom=[
                "Let op dat de helling van een x,t-grafiek de snelheid geeft en de helling van een "
                "v,t-grafiek de versnelling. De oppervlakte onder een v,t-grafiek geeft dan weer de "
                "verplaatsing.",
                None,
            ],
        ),
        dict(
            aanpak="Let bij elke bewering op het verschil tussen de grootte en het teken van een "
                   "grootheid. Een teken zegt iets over de zin, niet over sneller of trager.",
            waarom=[
                "Niet waar: rijd je achteruit en word je sneller, dan is de versnelling ook "
                "negatief. Het teken zegt enkel in welke zin de verandering gaat.",
                None,
                "Niet waar: bij een vrije val is de versnelling g voor elk voorwerp, want de massa "
                "valt weg uit m g is m a. Enkel luchtweerstand maakt verschil.",
                None,
            ],
        ),
        dict(
            aanpak="Deze twee vragen vragen een reden en geen getal. Zeg telkens welke zin je "
                   "positief rekent, of welke formule de massa doet wegvallen.",
            waarom=[
                "Noem dat het van de gekozen zin afhangt. Reken je vooruit positief, dan zijn hier "
                "zowel de snelheid als de versnelling negatief, en toch gaat de auto sneller.",
                "Noem dat de massa wegvalt. Uit m g is m a volgt a is g voor allebei, dus komen ze "
                "samen aan; in lucht verstoort de wrijving dat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-horizontale-worp-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Hou de twee richtingen streng apart. Horizontaal gebeurt er niets met de "
                   "snelheid, verticaal is het een gewone vrije val, en enkel de tijd hebben ze "
                   "samen.",
            waarom=[
                "Let op dat de valtijd uit de verticale beweging komt. De horizontale snelheid heeft "
                "er niets mee te maken, en dat is de kern van dit hele hoofdstuk.",
                None,
            ],
        ),
        dict(
            aanpak="Werk altijd in dezelfde orde: eerst de valtijd uit de hoogte, dan de dracht uit "
                   "die tijd en de horizontale snelheid. Nooit omgekeerd.",
            waarom=[
                None,
                None,
                None,
                None,
                "Let op dat je hier Pythagoras nodig hebt: de snelheid bij het neerkomen is de "
                "samenstelling van de horizontale en de verticale snelheid. Die twee gewoon optellen "
                "geeft een te groot antwoord.",
                "Let op dat je hier met 9,81 moet rekenen en niet met 10, want dat staat er "
                "uitdrukkelijk bij. Reken de valtijd eerst apart uit en hou er genoeg cijfers in "
                "voor je vermenigvuldigt.",
            ],
        ),
        dict(
            aanpak="Ook omgekeerd blijft de orde dezelfde: haal eerst de valtijd uit de hoogte of "
                   "uit de dracht, en reken daarna de onbekende.",
            waarom=[
                None,
                None,
                "Let op dat de hoogte hier gevraagd wordt uit de tijd alleen. De horizontale "
                "snelheid speelt geen rol, want ze beïnvloedt de valtijd niet.",
            ],
        ),
        dict(
            aanpak="Elke bewering gaat over dezelfde onafhankelijkheid van de twee richtingen. "
                   "Vraag je af of de uitspraak de twee door elkaar haalt.",
            waarom=[
                "Niet waar: de valtijd komt enkel uit de hoogte. Een bal die je heel hard weggooit, "
                "valt even lang als een bal die je gewoon laat vallen.",
                None,
                None,
                "Niet waar: de zwaartekracht werkt verticaal, dus verandert ze enkel de verticale "
                "snelheid. Zonder luchtweerstand blijft de horizontale snelheid de hele worp "
                "dezelfde.",
            ],
        ),
        dict(
            aanpak="Vergelijkingsvragen los je op met de formules in plaats van met je gevoel. Kijk "
                   "welke grootheid in welke formule staat, en of ze onder een wortel zit.",
            waarom=[
                "Let op dat beide paren samen landen. De valtijd hangt enkel van de hoogte af, dus "
                "harder gooien verandert waar ze landen, niet wanneer.",
                "Let op dat de hoogte onder een wortel staat: dubbel zo hoog geeft wortel twee keer "
                "zo lang vallen. Samen met de dubbele snelheid is dat twee keer wortel twee, dus "
                "ongeveer 2,8 keer.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg met een formule erbij. Zeg telkens welke "
                   "grootheid wél en welke níet in die formule staat.",
            waarom=[
                "Noem dat de beginsnelheid niet in de formule voor de valtijd staat. Verticaal "
                "begint de worp met snelheid nul, dus hangt de tijd enkel van de hoogte en van g af.",
                "Noem de wortel. Dubbel zo hoog geeft wortel twee keer zo ver, dus ongeveer 1,4 "
                "keer; recht evenredig is enkel de beginsnelheid.",
                "Noem dat het pakket de snelheid van het vliegtuig meeneemt. Het beschrijft een "
                "parabool en landt verderop, dus moet de piloot vroeger lossen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-gravitatiekracht-en-de-cirkelbeweging-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk waar de grootheid staat: de massa's staan boven de breuk en werken recht "
                   "evenredig, de afstand staat in het kwadraat onder de breuk.",
            waarom=[
                "Let op de derde: drie keer verder geeft negen keer kleiner, dus zestig gedeeld door "
                "negen is ongeveer 6,7 newton. Niet drie keer kleiner.",
                "Let op dat de eerste twee hetzelfde antwoord geven, langs twee verschillende wegen: "
                "beide massa's verdubbelen geeft maal vier, en de afstand halveren ook.",
            ],
        ),
        dict(
            aanpak="Bij een cirkelbeweging heb je altijd dezelfde keten: snelheid uit de omtrek en "
                   "de omlooptijd, dan de middelpuntzoekende versnelling, dan de kracht.",
            waarom=[
                "Let op dat pi hier wegvalt: twee pi maal een half gedeeld door pi geeft precies "
                "één. Vul een getal voor pi pas in als het echt nodig is.",
                None,
                None,
                "Let op het verschil tussen de twee grootheden: de omlooptijd is de tijd voor één "
                "ronde, de hoeksnelheid is twee pi gedeeld door die tijd. Twee ronden per seconde "
                "geeft dus een halve seconde en vier pi radiaal per seconde.",
                "Let op dat je hier de vorm met de hoeksnelheid gebruikt, want de snelheid in meter "
                "per seconde is niet gegeven. Omega staat in het kwadraat.",
            ],
        ),
        dict(
            aanpak="Vul in de gravitatiewet alles in SI-eenheden in en reken met machten van tien. "
                   "Voor g aan een oppervlak neem je de straal van de planeet, voor een baan de "
                   "baanstraal.",
            waarom=[
                "Let op dat de uitkomst heel klein is: twee massa's van duizend kilogram trekken "
                "elkaar met honderdduizendsten van een newton aan. Gravitatie is pas merkbaar bij "
                "hemellichamen.",
                "Let op dat je hier de straal van de planeet gebruikt en niet de afstand van de "
                "maan. De uitkomst van bijna 9,8 verraadt dat deze planeet onze aarde is.",
                "Let op dat de baansnelheid uit de gelijkstelling van de gravitatiekracht met de "
                "middelpuntzoekende kracht volgt. De massa van de maan valt daarbij weg, dus telt "
                "enkel de massa van de planeet.",
                "Let op dat je de omlooptijd uit de omtrek gedeeld door de snelheid haalt. "
                "Vijfentwintig honderdduizend seconden omzetten naar dagen maakt het antwoord pas "
                "leesbaar, en die 29 dagen kloppen mooi met onze eigen maan.",
            ],
        ),
        dict(
            aanpak="Hou bij elke bewering in het oog dat versnelling over de verandering van de "
                   "vector gaat, niet enkel over de grootte van de snelheid.",
            waarom=[
                None,
                "Niet waar: de richting van de snelheid verandert voortdurend, dus is er wel een "
                "versnelling. Ze is naar het middelpunt gericht en verandert enkel de richting.",
                None,
                "Niet waar: de zwaartekracht is daar bijna even groot als op aarde, en ze is precies "
                "wat de satelliet in zijn baan houdt. Gewichtloos voelen is iets anders dan geen "
                "zwaartekracht ondervinden.",
                None,
            ],
        ),
        dict(
            aanpak="De middelpuntzoekende kracht is geen nieuwe kracht: het is de rol die een "
                   "bestaande kracht speelt. Zoek dus telkens welke echte kracht die rol opneemt.",
            waarom=[
                "Let op dat de wrijving van de wielen in een bocht naar het midden van de bocht "
                "wijst. Daarom heeft die kracht een bovengrens, en daarom kan een auto slippen.",
                None,
            ],
        ),
        dict(
            aanpak="Elk van deze drie vragen leeft van het verschil tussen een kracht en een gevoel, "
                   "of tussen grootte en richting. Zeg dat verschil uitdrukkelijk.",
            waarom=[
                "Noem dat versnelling over de vector gaat. De grootte blijft gelijk, de richting "
                "draait, en juist die draai is de versnelling naar het middelpunt.",
                "Noem dat er geen tegenkracht van een vloer is. Wat je normaal als gewicht voelt, is "
                "de vloer die tegen je duwt; valt het hele station mee, dan is er niets dat duwt.",
                "Noem dat de bocht een bepaalde kracht vraagt en de wrijving die moet leveren. Bij "
                "regen is de beschikbare wrijving kleiner, dus moet de snelheid naar beneden of de "
                "bocht ruimer.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-arbeid-energie-en-vermogen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Arbeid is kracht maal weg, maar enkel het stuk van de kracht langs de "
                   "verplaatsing telt. Vraag je dus altijd af welke hoek de kracht met de weg maakt.",
            waarom=[
                None,
                None,
                "Let op dat er geen arbeid is zonder verplaatsing. Je spieren werken wel, maar het "
                "boek verplaatst niet, dus is de arbeid nul.",
                "Let op de cosinus van zestig graden: die is een half, dus de helft van de arbeid. "
                "Bij arbeid werk je met de cosinus, bij een moment met de sinus.",
                "Let op het minteken. Wrijving werkt tegen de verplaatsing in, dus is haar arbeid "
                "negatief; ze haalt energie uit de beweging.",
            ],
        ),
        dict(
            aanpak="Elke energievorm heeft zijn eigen formule. Let erop welke grootheid in het "
                   "kwadraat staat: de snelheid bij kinetische energie, de uitrekking bij een veer.",
            waarom=[
                None,
                None,
                "Let op dat de uitrekking in het kwadraat staat: 0,10 meter geeft 0,010. Die stap "
                "overslaan is de klassieke fout bij een veer.",
                None,
                "Noem het kwadraat. Twee keer zo snel is vier keer zo veel energie, en daarom groeit "
                "een remweg zo snel met de snelheid.",
            ],
        ),
        dict(
            aanpak="Bij behoud van energie stel je de ene vorm gelijk aan de andere. De massa valt "
                   "vaak weg, en dat is een goede controle op je werk.",
            waarom=[
                None,
                "Let op dat de massa wegvalt uit de gelijkheid: de snelheid beneden hangt enkel van "
                "de hoogte af. Een zware en een lichte slee komen even snel beneden.",
                "Let op dat dit dezelfde formule is als de vorige, maar omgekeerd: hier zet "
                "kinetische energie om in hoogte.",
                "Noem waar elke vorm maximaal is. In de uiterste standen is alles potentieel, in het "
                "laagste punt alles kinetisch, en de som blijft gelijk zolang er geen wrijving is.",
            ],
        ),
        dict(
            aanpak="De totale arbeid is gelijk aan de verandering van de kinetische energie. Reken "
                   "dus eerst het verschil in energie, en haal daar de gevraagde grootheid uit.",
            waarom=[
                None,
                "Let op het minteken: de kinetische energie daalt tot nul, dus is de totale arbeid "
                "negatief. De remmen halen energie uit de auto.",
                "Let op dat je de arbeid hier door de weg deelt om de kracht te vinden. Het teken "
                "laat je weg als je enkel naar de grootte van de remkracht vraagt.",
            ],
        ),
        dict(
            aanpak="Vermogen is arbeid per seconde. Let op de eenheden van tijd: minuten en uren "
                   "moet je omzetten, behalve als je in kilowattuur rekent.",
            waarom=[
                None,
                "Let op de twee stappen: eerst de arbeid uit kracht maal weg, dan het vermogen door "
                "de tijd. De kracht rechtstreeks door de tijd delen heeft geen betekenis.",
                None,
                "Let op dat een kilowattuur een energie is: duizend watt gedurende 3600 seconden. "
                "Daarom staat je elektriciteitsrekening in kilowattuur en niet in kilowatt.",
                "Let op de tien minuten: dat is 600 seconden. In een formule met joule en watt hoort "
                "de tijd in seconden.",
                "Let op dat je hier juist niet omzet naar seconden: in kilowattuur reken je met "
                "kilowatt en uren, dus 0,060 maal 5,0.",
            ],
        ),
        dict(
            aanpak="Let bij elke bewering op het verschil tussen arbeid en vermogen, en tussen een "
                   "conservatieve en een niet-conservatieve kracht.",
            waarom=[
                None,
                "Niet waar: in een echte machine gaat er altijd energie naar wrijving en warmte, dus "
                "blijft het rendement onder honderd procent.",
                None,
                "Niet waar: juist bij wrijving hangt de arbeid wel van de weg af, want een langere "
                "weg geeft meer wrijvingsarbeid. Daarom is wrijving niet conservatief.",
                None,
                "Niet waar: even hoog tillen is dezelfde arbeid, want kracht en weg zijn dezelfde. "
                "Sneller tillen betekent een groter vermogen, niet meer arbeid.",
                None,
                "Niet waar: een kilowattuur is een energie en geen vermogen. De kilowatt alleen is "
                "het vermogen.",
            ],
        ),
        dict(
            aanpak="Zoek bij elk geval één van de twee redenen waarom de arbeid nul kan zijn: de "
                   "kracht staat loodrecht op de weg, of er is geen verplaatsing.",
            waarom=[
                "Let op dat de drie gevallen twee verschillende redenen hebben. Bij het blad en bij "
                "de normaalkracht staat de kracht loodrecht op de beweging; bij de muur is er "
                "gewoon geen verplaatsing.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een reden met een formule erbij. Noem telkens welke hoek "
                   "of welke grootheid de uitkomst bepaalt.",
            waarom=[
                "Noem dat de hoek negentig graden is. Je draagkracht wijst naar boven en de weg is "
                "horizontaal, dus is de arbeid op de tas nul; dat je spieren moe worden, is een "
                "ander verhaal.",
                "Noem ook een voorbeeld, zoals gevraagd. Een conservatieve kracht levert een arbeid "
                "die enkel van begin- en eindpunt afhangt, en de zwaartekracht is er een.",
                "Noem dat de kracht onderweg verandert. Bij een veer groeit de kracht met de "
                "uitrekking, dus is er geen vaste kracht om mee te vermenigvuldigen en neem je de "
                "oppervlakte onder de grafiek.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-gaswetten-en-de-algemene-gaswet-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De naam van het proces zegt wat gelijk blijft: iso-therm de temperatuur, "
                   "iso-baar de druk, iso-choor het volume. Zoek dus eerst wat vastgehouden wordt.",
            waarom=[
                None,
                "Let op de ballon in de zon: die kan uitzetten, dus blijft de druk gelijk en is het "
                "proces isobaar. Een gesloten metalen vat kan niet uitzetten, dus is dat isochoor.",
                "Let op het verschil tussen de drie formules: bij isotherm staat het product, bij de "
                "twee andere een quotiënt. Welke twee grootheden in dat quotiënt staan, verraadt "
                "welke de derde constant is.",
            ],
        ),
        dict(
            aanpak="Zet de temperatuur altijd eerst om naar kelvin, voor je iets anders doet. Bij "
                   "kelvin tel je 273 op, bij celsius trek je 273 af.",
            waarom=[
                "Let op min 73 graden: dat is 200 kelvin. Een negatieve celsiuswaarde geeft nog "
                "altijd een positieve kelvinwaarde, zolang je boven min 273 blijft.",
                None,
            ],
        ),
        dict(
            aanpak="Kies de wet die bij het proces hoort en vul de temperatuur in kelvin in. Reken "
                   "met verhoudingen, dan hoef je de eenheden van druk en volume niet om te zetten.",
            waarom=[
                None,
                "Let op dat je de temperaturen in kelvin gebruikt. In celsius zou de verhouding van "
                "27 op 177 staan en dat geeft een heel ander getal.",
                None,
                "Let op dat je hier kan rekenen zonder formule: de druk verdubbelt, dus halveert het "
                "volume. Een omgekeerde evenredigheid zie je vaak sneller dan je ze berekent.",
                "Let op de omzetting naar kelvin: 27 graden is 300 kelvin en 127 graden is 400 "
                "kelvin. Dan staat er netjes een verhouding van vier op drie.",
            ],
        ),
        dict(
            aanpak="De algemene gaswet is de drie wetten in één: p maal V gedeeld door T blijft "
                   "gelijk. Werk je met mol, dan neem je de ideale gaswet, met alles in SI-"
                   "eenheden.",
            waarom=[
                None,
                None,
                "Let op dat je hier in SI-eenheden moet werken: kubieke meter en pascal. Honderd "
                "kilopascal is tien tot de vijfde pascal, en de uitkomst van ongeveer één mol "
                "controleert zichzelf.",
                "Let op dat het antwoord in kubieke meter uitkomt, dus zet het nog om naar liter: "
                "0,050 kubieke meter is vijftig liter.",
                "Let op dat normomstandigheden nul graden celsius en 101,3 kilopascal zijn. Die 22,4 "
                "liter is het waard om vanbuiten te kennen; bij kamertemperatuur is het ongeveer 24 "
                "liter.",
            ],
        ),
        dict(
            aanpak="Kijk of de twee grootheden omgekeerd of recht evenredig zijn. Omgekeerd geeft "
                   "een hyperbool, recht evenredig een rechte door de oorsprong.",
            waarom=[
                "Let op dat de rechte door de oorsprong gaat omdat je in kelvin werkt. In celsius "
                "zou ze de as bij min 273 snijden, en juist dat heeft men ooit gebruikt om het "
                "absolute nulpunt te vinden.",
            ],
        ),
        dict(
            aanpak="Hou één grootheid vast en volg de twee andere. Zijn ze omgekeerd evenredig, dan "
                   "doet de ene het omgekeerde van de andere.",
            waarom=[
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de eenheden, het deeltjesmodel, en waar een "
                   "echt gas van het ideale afwijkt. Vraag je bij elke af welke van de drie.",
            waarom=[
                "Niet waar: de gaswetten zijn verhoudingen, dus moet de temperatuur in kelvin. In "
                "celsius kloppen de verhoudingen niet, want die schaal heeft geen echt nulpunt.",
                None,
                None,
                None,
                "Niet waar: bij het absolute nulpunt is de beweging van de deeltjes minimaal. Juist "
                "daarom ligt het nulpunt van de kelvinschaal daar.",
                None,
                "Niet waar, het is net omgekeerd: bij hoge druk en lage temperatuur zitten de "
                "moleculen dicht bij elkaar, en dan tellen hun eigen volume en hun onderlinge "
                "aantrekking mee. Bij lage druk en hoge temperatuur gedraagt een gas zich bijna "
                "ideaal.",
                None,
                "Niet waar: bij een isobaar proces blijft de druk constant, zoals de baar in de naam "
                "zegt. Het volume blijft gelijk bij een isochoor proces.",
                "Niet waar: één mol van elk gas neemt bij dezelfde druk en temperatuur hetzelfde "
                "volume in, namelijk 22,4 liter. In de gaswet staat het aantal mol en niet de massa.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg met het deeltjesmodel of met de schaal van de "
                   "temperatuur. Noem telkens wat de deeltjes doen.",
            waarom=[
                "Noem beide gevolgen: de moleculen botsen vaker én harder. Samen geven die "
                "botsingen de druk, en daarom stijgt ze bij hetzelfde volume.",
                "Noem dat het volume vast staat. Stijgt de temperatuur, dan stijgt de druk mee, en "
                "boven een zekere druk begeeft de bus het.",
                "Noem dat het om verhoudingen gaat. Verhoudingen gelden enkel vanaf een echt "
                "nulpunt, en de nul van de celsiusschaal is willekeurig gekozen bij het smeltpunt "
                "van water.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-warmteleer-temperatuur-warmte-en-faseovergangen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de zes overgangen als drie paren: smelten en stollen, verdampen en "
                   "condenseren, sublimeren en rijpen. Van elk paar ken je dan de twee richtingen.",
            waarom=[
                "Let op sublimeren: dat is van vast rechtstreeks naar gas, zoals droogijs of sneeuw "
                "die verdwijnt zonder te smelten.",
                "Let op rijpen: gas rechtstreeks naar vast, zoals de witte laag op een koude ruit. "
                "Dat is de omgekeerde weg van sublimeren.",
            ],
        ),
        dict(
            aanpak="Één regel volstaat: naar een losser geheel toe kost warmte, naar een vaster "
                   "geheel geeft warmte af. Vast is het vastste, gas het losste.",
            waarom=[
                None,
                "Let op dat condenseren en rijpen warmte afgeven. Juist daarom voelt een "
                "vochtige, warme lucht zo warm aan: de damp die op je huid condenseert, geeft "
                "haar warmte af.",
            ],
        ),
        dict(
            aanpak="Q is c maal m maal het temperatuurverschil. Vorm de formule eerst om naar de "
                   "gevraagde grootheid, en reken in joule en kilogram.",
            waarom=[
                None,
                None,
                "Let op dat ijzer een veel kleinere soortelijke warmtecapaciteit heeft dan water. "
                "Daarom warmt een pan veel sneller op dan het water erin.",
                "Let op de kilojoule: 36 kJ is 36 000 joule. Een eenheid met een voorvoegsel laten "
                "staan geeft hier een antwoord dat duizend keer te klein is.",
                "Let op dat de soortelijke warmtecapaciteit in joule per kilogram en per kelvin "
                "staat. Je antwoord moet dus die eenheid krijgen, niet gewoon joule.",
            ],
        ),
        dict(
            aanpak="Bij een faseovergang is Q de latente warmte maal de massa, zonder "
                   "temperatuurverschil. De temperatuur verandert daar immers niet.",
            waarom=[
                None,
                "Let op hoe groot verdampen is tegenover smelten: verdampen vraagt bijna zeven keer "
                "meer warmte per kilogram. Daarom duurt een pot water droogkoken zo veel langer dan "
                "aan de kook brengen.",
                None,
                "Let op dat stollen even veel warmte afgeeft als smelten opneemt. De latente warmte "
                "is dezelfde, enkel de richting verschilt.",
            ],
        ),
        dict(
            aanpak="Splits het probleem in stukken: elk stuk opwarmen apart, elke faseovergang "
                   "apart, en tel de warmtes op het einde op. Reken nooit een faseovergang en een "
                   "opwarming in één formule.",
            waarom=[
                "Let op hoe klein het opwarmen is tegenover het verdampen: 84 kilojoule tegen 2256. "
                "Het grootste deel van de energie gaat naar de faseovergang.",
                "Let op de orde van de twee stappen: eerst smelten op nul graden, dan het "
                "gesmolten water opwarmen. Draai je ze om, dan reken je met de verkeerde stof.",
            ],
        ),
        dict(
            aanpak="Op een verwarmingscurve betekent een stijgend stuk opwarmen en een vlak stuk een "
                   "faseovergang. Twee vlakke stukken betekenen dus twee overgangen.",
            waarom=[
                "Let op dat een vlak stuk niet betekent dat er niets gebeurt: er gaat juist veel "
                "warmte in, maar die wordt gebruikt om de deeltjes los te maken en niet om ze "
                "sneller te doen bewegen.",
            ],
        ),
        dict(
            aanpak="Hou warmte en temperatuur streng uit elkaar: warmte is energie die stroomt, "
                   "temperatuur is hoe snel de deeltjes gemiddeld bewegen.",
            waarom=[
                "Niet waar: temperatuur is een maat voor de beweging van de deeltjes, warmte is "
                "energie die van warm naar koud stroomt. Een badkuip lauw water bevat meer energie "
                "dan een kop kokend water.",
                None,
                None,
                "Niet waar, net omgekeerd: bij een lagere druk kookt water bij een lagere "
                "temperatuur. Hoog in de bergen kookt het rond negentig graden, en daarom gaart eten "
                "er trager.",
                None,
                "Niet waar: hoeveel energie een voorwerp bevat, hangt ook van zijn massa en zijn "
                "soortelijke warmtecapaciteit af. Een vonk van duizend kelvin bevat minder energie "
                "dan een bad van driehonderd kelvin.",
                None,
                "Niet waar: een mengsel smelt over een traject in plaats van bij één temperatuur. "
                "Een scherp smeltpunt is juist een aanwijzing dat een stof zuiver is.",
                None,
                "Niet waar: sublimeren gaat van vast naar gas. De omgekeerde weg, van gas naar vast, "
                "heet rijpen.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een uitleg met het deeltjesmodel of met de drie manieren "
                   "van warmtetransport. Noem telkens waar de energie naartoe gaat.",
            waarom=[
                "Noem waar de warmte naartoe gaat. Ze wordt gebruikt om de deeltjes uit hun rooster "
                "los te maken, dus gaat ze niet naar hun snelheid en stijgt de temperatuur niet.",
                "Noem dat verdampen warmte vraagt en dat die uit je huid komt. Daarom koelt zweten "
                "beter af in droge lucht, waar het water sneller verdampt.",
                "Noem beide, zoals gevraagd. Het vacuüm sluit geleiding en stroming uit, de "
                "spiegelende wand kaatst de straling terug; dat zijn precies de drie manieren waarop "
                "warmte zich verplaatst.",
                "Noem dat zout het smeltpunt verlaagt. Bij strenge vorst ligt de temperatuur onder "
                "dat verlaagde smeltpunt, en dan bevriest de pekel toch.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-harmonische-trillingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De frequentie is één gedeeld door de periode, en omgekeerd. Zet de tijd altijd "
                   "in seconden, dan komt de frequentie in hertz.",
            waarom=[
                None,
                None,
            ],
        ),
        dict(
            aanpak="De pulsatie is twee pi gedeeld door de periode, of twee pi maal de frequentie. "
                   "Ze is dus de frequentie uitgedrukt in radiaal per seconde.",
            waarom=[
                "Let op dat de pulsatie altijd ongeveer zes keer groter is dan de frequentie, want "
                "twee pi is ongeveer 6,28. Dat is een handige controle op je antwoord.",
            ],
        ),
        dict(
            aanpak="Vergelijk de gegeven vergelijking met de algemene vorm y is A maal de sinus van "
                   "omega t plus de beginfase. Dan lees je elke grootheid rechtstreeks af.",
            waarom=[
                None,
                None,
                "Let op dat de beginfase nul is omdat er niets achter de t staat. Dat betekent dat "
                "de trilling in het evenwicht begint; stond er een cosinus, dan begon ze in een "
                "uiterste stand.",
                None,
                "Let op dat de uitwijking na een halve periode weer nul is, niet min de amplitude. "
                "De sinus van pi is nul; min de amplitude bereik je na drie kwart periode.",
            ],
        ),
        dict(
            aanpak="De eigenfrequentie van een veer hangt af van de stijfheid en de massa, die van "
                   "een slinger van de lengte en van g. De amplitude speelt bij geen van beide een "
                   "rol.",
            waarom=[
                "Let op de laatste: een grotere amplitude verandert de frequentie niet. Dat is net "
                "wat een harmonische trilling bijzonder maakt.",
                "Let op de slinger: de massa van de bol doet niets, want ze valt weg uit de formule. "
                "Op de maan is g kleiner, dus trilt dezelfde slinger langzamer.",
                "Let op dat massa en stijfheid onder een wortel staan: vier keer zo zwaar geeft twee "
                "keer zo traag, en twee keer zo zwaar geeft een factor wortel twee.",
            ],
        ),
        dict(
            aanpak="Hou in je hoofd dat uitwijking en versnelling samen maximaal zijn in de uiterste "
                   "stand, en de snelheid in het evenwicht. De drie zitten nooit samen op hun "
                   "maximum.",
            waarom=[
                "Let op dat snelheid en versnelling hier elkaars tegengestelde volgen: waar de "
                "snelheid maximaal is, is de versnelling nul, en omgekeerd.",
                None,
            ],
        ),
        dict(
            aanpak="Het faseverschil zegt hoe de twee trillingen tegenover elkaar lopen: nul is "
                   "samen, pi is precies tegengesteld, en alles ertussen heeft geen eigen naam.",
            waarom=[
                "Let op dat een faseverschil van een halve pi geen naam heeft: de ene is dan "
                "maximaal terwijl de andere door het evenwicht gaat. Enkel nul en pi heten in fase "
                "en in tegenfase.",
            ],
        ),
        dict(
            aanpak="Elke grootheid heeft haar eigen eenheid. Let erop dat de beginfase en de "
                   "pulsatie in radiaal gerekend worden en niet in meter of in seconden.",
            waarom=[
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een amplitude is, waarvan de periode "
                   "afhangt, en wat demping en resonantie doen. Vraag je bij elke af welk van de "
                   "drie.",
            waarom=[
                "Niet waar: de amplitude is de grootste uitwijking, dus een afstand, en die kan niet "
                "negatief zijn. De uitwijking zelf kan dat wel.",
                None,
                "Niet waar: bij demping neemt vooral de amplitude af. De frequentie verandert maar "
                "heel licht.",
                None,
                "Niet waar: de periode hangt niet van de amplitude af. Juist daarom kan een slinger "
                "een uurwerk aandrijven.",
                None,
                "Niet waar: de massa van de bol valt weg uit de formule van een slinger. Enkel de "
                "lengte en g bepalen haar periode.",
                None,
                None,
                "Niet waar: de beginfase staat in radiaal. Ze zegt waar in de trilling je begint, "
                "niet hoe ver iets uitwijkt.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen gaan over resonantie en demping. Noem telkens de "
                   "eigenfrequentie of waar de energie naartoe gaat.",
            waarom=[
                "Noem ook een voorbeeld, zoals gevraagd. Resonantie is het samenvallen van de "
                "aandrijvende frequentie met de eigenfrequentie, en de schommel is het "
                "duidelijkste voorbeeld.",
                "Noem beide: de aardbeving kan het gebouw op zijn eigenfrequentie aandrijven, en "
                "dempers halen energie uit de trilling. Daarom staat of valt zo'n ontwerp met de "
                "eigenfrequentie van het gebouw.",
                "Noem dat de periode niet van de amplitude afhangt. Bij een kleine uitslag hangt ze "
                "enkel van de lengte en van g af, en dat maakt een slinger geschikt als uurwerk.",
                "Noem dat de energie niet verdwijnt maar warmte wordt. Wrijving en luchtweerstand "
                "voeren ze af naar de omgeving, en het behoud van energie blijft dus gelden.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-golven-en-hun-eigenschappen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De snelheid is de golflengte maal de frequentie. Vorm die ene formule om naar "
                   "wat gevraagd wordt, en let op de voorvoegsels bij licht.",
            waarom=[
                None,
                None,
                "Let op de nanometers: 600 nanometer is 6,0 maal tien tot de min zeven meter. Dat is "
                "de stap die hier het vaakst misloopt.",
                "Let op dat je hier de periode krijgt en niet de frequentie. De snelheid is dan de "
                "golflengte gedeeld door de periode, wat op hetzelfde neerkomt.",
            ],
        ),
        dict(
            aanpak="Het golfgetal is voor de ruimte wat de pulsatie voor de tijd is: twee pi gedeeld "
                   "door de golflengte, respectievelijk door de periode.",
            waarom=[
                None,
                "Let op dat je de drie grootheden rechtstreeks afleest: de factor vooraan is de "
                "amplitude, het getal bij t is de pulsatie en het getal bij x het golfgetal. Reken "
                "er niets aan.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de deeltjes dwars op de golf of in de looprichting bewegen. "
                   "Dwars is transversaal, in de looprichting longitudinaal.",
            waarom=[
                "Let op dat geluid longitudinaal is: de lucht wordt samengeperst en weer uitgerekt in "
                "de looprichting. Licht is transversaal, en daarom kan je het polariseren en geluid "
                "niet.",
            ],
        ),
        dict(
            aanpak="Leer de vier woorden met hun kern: terugkaatsen, van richting veranderen in een "
                   "andere stof, afbuigen rond een hindernis, en twee golven die samenkomen.",
            waarom=[
                "Let op het verschil tussen diffractie en refractie: diffractie is afbuigen rond een "
                "hoek of door een opening, refractie is breken bij de overgang naar een andere stof.",
                "Let op de staande golf: dat is interferentie van een golf met haar eigen "
                "weerkaatsing, dus geen apart verschijnsel.",
            ],
        ),
        dict(
            aanpak="Bij breking blijft de frequentie gelijk, want de bron blijft dezelfde. De "
                   "snelheid verandert, en dus moet de golflengte mee veranderen.",
            waarom=[
                "Let op dat juist de frequentie gelijk blijft: de golf wordt niet trager omdat de "
                "bron anders trilt, maar omdat de stof anders is. Daarom verandert de golflengte.",
                None,
                "Let op de regel: naar een stof met een grotere brekingsindex buigt de straal naar "
                "de normaal toe, naar een kleinere ervan weg. Bij de overgang glas naar lucht kan "
                "dat zelfs totale weerkaatsing geven.",
                "Let op dat de brekingsindex de verhouding van de snelheid in vacuüm tot die in de "
                "stof is. De snelheid in stof 1 heb je hier niet nodig.",
                "Noem dat de sinus kleiner wordt. Water heeft een grotere brekingsindex dan lucht, "
                "dus is de brekingshoek kleiner dan de invalshoek.",
            ],
        ),
        dict(
            aanpak="Bij interferentie beslist het faseverschil: top op top versterkt, top op dal "
                   "dooft uit. Bij een staande golf ligt tussen twee knopen altijd een halve "
                   "golflengte.",
            waarom=[
                None,
                "Let op dat een snaar in haar grondtoon een halve golflengte lang is. De golflengte "
                "is dus het dubbele van de snaarlengte, niet de snaarlengte zelf.",
                "Let op dat de twee vaste uiteinden zelf de knopen zijn. In de grondtoon zijn er dus "
                "twee knopen en één buik ertussen.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een golf wel en niet vervoert, wat bij "
                   "breking verandert, en wat een knoop is. Vraag je bij elke af welk van de drie.",
            waarom=[
                None,
                "Niet waar: de snelheid van een golf hangt van de stof af, niet van de amplitude. "
                "Hard roepen maakt je stem luider, niet sneller.",
                None,
                "Niet waar: elk deeltje begint later te trillen dan het vorige, want de golf heeft "
                "tijd nodig om er te komen. Juist dat verschil maakt het golfbeeld.",
                None,
                "Niet waar: de frequentie blijft gelijk bij breking. Enkel de snelheid en de "
                "golflengte veranderen.",
                None,
                "Niet waar: geluid heeft een stof nodig om zich voort te planten, dus loopt het niet "
                "door het vacuüm. Licht wel, want dat heeft geen middenstof nodig.",
                None,
                "Niet waar: tussen twee knopen ligt een halve golflengte. Een hele golflengte beslaat "
                "drie knopen.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een uitleg. Noem telkens de golflengte, het beginsel van "
                   "Huygens of de interferentie die erachter zit.",
            waarom=[
                "Let op dat je twee tijden van elkaar moet aftrekken: de bron trilde vijf seconden, "
                "maar de golf had er drie nodig om ter plaatse te komen.",
                "Noem dat lage tonen een grote golflengte hebben. Buiging rond hoeken lukt beter bij "
                "een grote golflengte, en daarom blijft juist het gebrom over.",
                "Noem ook wat je ermee verklaart, zoals gevraagd. Elk punt van een golffront is zelf "
                "een bron, en daarmee verklaar je weerkaatsing, breking en buiging in één keer.",
                "Noem beide delen van de vraag. Een staande golf ontstaat uit interferentie met de "
                "eigen weerkaatsing, en een knoop is een punt waar de twee golven elkaar altijd "
                "opheffen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-licht-geluid-en-het-elektromagnetisch-spectrum-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer het spectrum als één rij van lage naar hoge frequentie. Hoe hoger de "
                   "frequentie, hoe korter de golflengte en hoe meer energie per foton.",
            waarom=[
                "Let op dat de golflengte juist de andere kant op loopt: radiogolven hebben de "
                "laagste frequentie en de grootste golflengte, gammastraling de hoogste frequentie "
                "en de kleinste golflengte.",
            ],
        ),
        dict(
            aanpak="Ioniserend betekent dat één foton genoeg energie heeft om een elektron uit een "
                   "atoom te slaan. Dat begint pas bij harde uv-straling en geldt dus enkel voor het "
                   "bovenste stuk van het spectrum.",
            waarom=[
                None,
                "Let op dat de grens bij uv ligt: alles daaronder, dus licht, infrarood, microgolven "
                "en radiogolven, is niet ioniserend. Microgolven verwarmen wel, maar dat is iets "
                "anders dan ioniseren.",
            ],
        ),
        dict(
            aanpak="Twee formules volstaan: de snelheid is golflengte maal frequentie, en de energie "
                   "van een foton is h maal de frequentie. Werk met machten van tien.",
            waarom=[
                None,
                None,
                "Let op de megahertz: 100 MHz is tien tot de achtste hertz. Dat geeft netjes drie "
                "meter, en dat is waarom een FM-antenne ongeveer die lengte heeft.",
                "Noem dat de energie met de frequentie gaat. Röntgenstraling heeft een veel hogere "
                "frequentie dan infrarood, dus veel meer energie per foton.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk beeld twee dingen: kan je het op een scherm opvangen, en staat "
                   "het rechtop. Reëel en omgekeerd horen samen, virtueel en rechtop ook.",
            waarom=[
                "Let op het verschil tussen de twee gevallen bij de bolle lens. Buiten het dubbele "
                "van de brandpuntsafstand krijg je een reëel en kleiner beeld, binnen de "
                "brandpuntsafstand een virtueel en groter beeld.",
                None,
                "Let op dat een vergrootglas net daarom een virtueel beeld geeft: het voorwerp zit "
                "binnen de brandpuntsafstand, dus kan je dat beeld niet op een scherm opvangen.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over de snelheid van elektromagnetische golven, over het "
                   "verschil tussen reëel en virtueel, en over wat de proef van Young aantoont.",
            waarom=[
                None,
                "Niet waar: een virtueel beeld bestaat enkel voor je oog, want de stralen komen daar "
                "niet echt samen. Enkel een reëel beeld kan je op een scherm opvangen.",
                None,
                None,
                "Niet waar: de proef van Young geeft interferentiestreepjes, en die horen bij een "
                "golf. Dat licht zich ook als deeltjes gedraagt, blijkt uit het foto-elektrisch "
                "effect.",
            ],
        ),
        dict(
            aanpak="Bij geluid reken je met 340 meter per seconde in lucht. Let bij een echo op dat "
                   "het geluid de afstand twee keer aflegt.",
            waarom=[
                None,
                "Let op het heen en terug: het geluid legde 680 meter af, dus staat de wand op de "
                "helft daarvan. Die deling vergeten is de klassieke fout bij een echo.",
                None,
                None,
                "Let op dat de harmonischen gewoon veelvouden van de grondtoon zijn. De vierde is "
                "dus vier keer de eerste, en dat is wat een toon zijn klankkleur geeft.",
            ],
        ),
        dict(
            aanpak="De decibelschaal is logaritmisch: elke tien decibel is een factor tien in "
                   "intensiteit. Reken dus met stappen van tien en niet met gewone verhoudingen.",
            waarom=[
                "Let op dat nul decibel niet geen geluid betekent, maar het zwakste geluid dat een "
                "mens nog hoort. Het is dus een gekozen nulpunt.",
                "Let op dat dertig decibel erbij een factor duizend is, niet een factor drie. Drie "
                "stappen van tien geven tien tot de derde.",
                None,
                "Let op dat de intensiteit met het kwadraat van de afstand gaat. Drie keer dichter "
                "geeft dus negen keer zo intens, en dat verklaart waarom vooraan op een concert zo "
                "schadelijk is.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een uitleg. Noem telkens de haarcellen, de golflengte of "
                   "de harmonischen die erachter zitten.",
            waarom=[
                "Noem dat de trilhaartjes niet terug groeien. Daarom is gehoorschade blijvend, en "
                "daarom helpt enkel voorkomen.",
                "Noem uitdrukkelijk dat de bron niets verandert, want dat is de kern van de vraag. "
                "De golven komen enkel dichter op elkaar of verder uiteen bij de waarnemer.",
                "Noem de harmonischen. De grondtoon is dezelfde, maar de sterkte van de boventonen "
                "verschilt, en die verdeling heet de klankkleur.",
                "Noem de golflengte. Radiogolven hebben een veel grotere golflengte, dus buigen ze "
                "beter af rond gebouwen; microgolven worden tegengehouden.",
            ],
        ),
        dict(
            aanpak="Let bij deze drie op het verschil tussen de bron en de waarnemer, en op de "
                   "grenzen van wat een mens hoort.",
            waarom=[
                "Let op dat geluid sneller loopt in een vastere stof: in staal rond vijfduizend "
                "meter per seconde, in water rond vijftienhonderd, in lucht 340.",
                "Niet waar: de bron zendt onveranderd dezelfde frequentie uit. Enkel de waarnemer "
                "meet een andere, en dat is precies het dopplereffect.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kwantumfysica-het-foto-elektrisch-effect-en-dualiteit-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: zit de frequentie boven de drempelfrequentie. Zo niet, dan "
                   "komt er niets los, hoe fel het licht ook is.",
            waarom=[
                "Let op het derde geval: fel licht van een te lage frequentie geeft nog altijd "
                "niets. Meer fotonen van te weinig energie blijven fotonen van te weinig energie.",
                "Let op dat zwak licht van een hoge frequentie wel werkt. Er komen dan weinig "
                "elektronen los, maar ze komen onmiddellijk los.",
            ],
        ),
        dict(
            aanpak="De energie van een foton is h maal de frequentie. De uittree-arbeid is diezelfde "
                   "formule met de drempelfrequentie, en wat overblijft is kinetische energie.",
            waarom=[
                None,
                None,
                "Let op dat de uittree-arbeid gewoon h maal de drempelfrequentie is. Dat is de "
                "energie die het elektron nodig heeft om net los te komen.",
                "Let op dat je hier twee energieën van elkaar aftrekt: de energie van het foton min "
                "de uittree-arbeid. Dat is de vergelijking van Einstein voor dit effect.",
                "Noem dat de energie met de frequentie gaat. Blauw heeft een hogere frequentie en "
                "dus een kleinere golflengte, en daarom meer energie per foton.",
            ],
        ),
        dict(
            aanpak="Hou de twee rollen streng uit elkaar: de frequentie bepaalt de energie per "
                   "foton, de intensiteit het aantal fotonen.",
            waarom=[
                "Let op dat de intensiteit enkel het aantal elektronen beïnvloedt en nooit hun "
                "energie. Juist dat kon het oude golfmodel niet verklaren.",
            ],
        ),
        dict(
            aanpak="Verschijnselen waarbij golven samenkomen of afbuigen vragen het golfmodel; "
                   "verschijnselen met een drempel of met één pakketje energie vragen het "
                   "deeltjesmodel.",
            waarom=[
                None,
                "Let op dat licht beide kanten heeft en dat daar niets fout aan is. Welk model je "
                "nodig hebt, hangt af van de proef die je doet.",
            ],
        ),
        dict(
            aanpak="De golflengte van de materie is h gedeeld door massa maal snelheid. Omdat h zo "
                   "klein is, speelt ze enkel bij heel lichte deeltjes een rol.",
            waarom=[
                None,
                "Let op hoe klein dit getal is: tien tot de min vierendertig meter, tegen tien tot "
                "de min tien voor een elektron. Dat verschil van vierentwintig machten is de hele "
                "reden dat we het golfkarakter van een bal niet zien.",
                "Noem de vergelijking met een atoom. De golflengte is zo veel kleiner dan elke "
                "structuur die bestaat, dat er niets is waaraan ze zich zou kunnen verraden.",
            ],
        ),
        dict(
            aanpak="Leer de drie begrippen met wat ze beschrijven: een gebied met kans, een "
                   "ondergrens in frequentie, en de vergelijking achter de golffunctie.",
            waarom=[
                "Let op dat een orbitaal geen baan is maar een gebied met een grote kans. Dat is "
                "precies het verschil met het oude beeld van een elektron dat rondjes draait.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: één foton per elektron, wat het "
                   "onzekerheidsbeginsel wel en niet is, en hoe de grafiek van de kinetische energie "
                   "loopt.",
            waarom=[
                "Niet waar: één elektron neemt de energie van één foton op. Energie van meerdere "
                "fotonen sparen kan niet, en daarom helpt fel licht van een te lage frequentie "
                "niet.",
                None,
                "Niet waar: het is geen gebrek aan goede toestellen maar een eigenschap van de "
                "natuur zelf. Betere meettoestellen veranderen er niets aan.",
                None,
                "Niet waar: een elektron heeft geen baan zoals een planeet. Je kan enkel een gebied "
                "met een grote kans tekenen, en dat is een orbitaal.",
                None,
                "Niet waar: een kleinere golflengte betekent een hogere frequentie en dus meer "
                "energie. Gammastraling heeft de kleinste golflengte en de meeste energie.",
                "Waar, en dat is hoe men h gemeten heeft. Zet je de kinetische energie uit tegen de "
                "frequentie, dan is de helling de constante van Planck en het snijpunt de uittree-"
                "arbeid.",
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg. Noem telkens of je het golfmodel of het "
                   "deeltjesmodel nodig hebt, en waarom het andere tekortkomt.",
            waarom=[
                "Noem wat het golfmodel zou voorspellen en wat je werkelijk ziet. Volgens dat model "
                "zou wachten helpen, en in werkelijkheid helpt wachten nooit.",
                "Noem dat de massa in de noemer staat. Daardoor is de golflengte van een bal "
                "onmeetbaar klein, terwijl die van een elektron van de orde van een atoom is.",
                "Noem beide kanten, want dat is de kern van de vraag. Elk elektron komt als één stip "
                "aan, dus als deeltje, en samen vormen ze toch het strepenpatroon van een golf.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-atoomkern-radioactief-verval-en-halveringstijd-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het getal in de naam is het massagetal A, dus het aantal protonen plus neutronen. "
                   "Zoek het aantal protonen Z op en trek dat af.",
            waarom=[
                "Let op dat je Z uit de naam van het element haalt en niet uit het getal erachter. "
                "Natrium heeft altijd elf protonen, lood tweeëntachtig, koolstof zes.",
            ],
        ),
        dict(
            aanpak="Leer de vier soorten aan wat er wegvliegt: een heliumkern, een elektron, een "
                   "positron, of enkel energie. Daaruit volgt meteen wat A en Z doen.",
            waarom=[
                None,
                "Let op bèta-plus: daar wordt een proton een neutron en vertrekt er een positron, "
                "dus daalt Z met één. Bij bèta-min is het net omgekeerd.",
            ],
        ),
        dict(
            aanpak="Bij alfa daalt A met vier en Z met twee, bij bèta-min blijft A gelijk en stijgt "
                   "Z met één, bij gamma verandert geen van de twee.",
            waarom=[
                None,
                "Let op het gammaverval: daar blijven A en Z precies gelijk, want er vertrekt enkel "
                "energie. De kern is daarna dezelfde, maar wel minder aangeslagen.",
                "Let op dat je hier ook de naam moet geven. Twee protonen minder dan radium brengt "
                "je bij radon, en die stap is net waarom radon in kelders opduikt.",
            ],
        ),
        dict(
            aanpak="Reken in halveringen in plaats van met formules: na elke halveringstijd blijft "
                   "er de helft over. Tel dus hoeveel keer de helft je nodig hebt.",
            waarom=[
                None,
                "Let op dat een zestiende vier halveringen is, want een half tot de vierde is een "
                "zestiende. Vier maal vier jaar geeft zestien jaar.",
                None,
                "Let op dat een kwart twee halveringstijden is, dus twee keer 5730 jaar. Die methode "
                "werkt tot ongeveer vijftigduizend jaar; daarna is er te weinig koolstof-14 over om "
                "te meten.",
            ],
        ),
        dict(
            aanpak="De activiteit is de vervalconstante maal het aantal kernen, en die constante is "
                   "0,693 gedeeld door de halveringstijd. Let op de eenheid van tijd die gevraagd "
                   "wordt.",
            waarom=[
                "Let op dat de activiteit even snel daalt als het aantal kernen: negen uur is drie "
                "halveringen, dus gedeeld door acht.",
                "Let op dat de vervalconstante de eenheid van je halveringstijd overneemt. Staat de "
                "halveringstijd in dagen, dan staat lambda per dag.",
                None,
                "Noem dat de kortste halveringstijd de grootste vervalconstante geeft. Bij hetzelfde "
                "aantal kernen is die bron dus het actiefst, en ook het snelst uitgewerkt.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een halveringstijd wel en niet betekent, "
                   "dat verval niet te beïnvloeden is, en het verband tussen activiteit en aantal "
                   "kernen.",
            waarom=[
                "Niet waar: na twee halveringstijden is er nog een kwart over. Volledig vervallen "
                "gebeurt in theorie nooit, want er blijft telkens de helft over.",
                "Niet waar: verval is een eigenschap van de kern zelf. Temperatuur, druk en "
                "scheikundige verbindingen veranderen de halveringstijd niet, en juist daarom is ze "
                "zo betrouwbaar als klok.",
                None,
                "Niet waar: bij gammaverval blijven A en Z gelijk, dus blijft het hetzelfde element. "
                "Enkel alfa en bèta veranderen het element.",
                None,
                None,
                "Niet waar, het is net omgekeerd: een kortere halveringstijd geeft een grotere "
                "vervalconstante. Lambda is 0,693 gedeeld door de halveringstijd.",
                None,
            ],
        ),
        dict(
            aanpak="Deze drie vragen vragen een uitleg. Noem telkens de twee krachten in de kern, of "
                   "de formule die het verband legt.",
            waarom=[
                "Noem beide krachten. De afstoting tussen protonen werkt over de hele kern, de "
                "kernkracht enkel tussen naburen, en extra neutronen voegen kernkracht toe zonder "
                "afstoting.",
                "Noem dat de aanvulling stopt bij de dood. Zolang een organisme leeft, blijft het "
                "gehalte gelijk; daarna daalt het met een vaste halveringstijd, en dat geeft de "
                "ouderdom.",
                "Noem de formule. De activiteit is lambda maal het aantal kernen, en lambda "
                "verandert niet, dus zijn de twee recht evenredig.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kernenergie-straling-en-haar-effecten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de drie soorten met hun tegenstelling: alfa ioniseert het sterkst maar "
                   "dringt het minst door, gamma net omgekeerd. Bèta zit in het midden.",
            waarom=[
                None,
                "Let op dat gamma niet afbuigt in een magnetisch veld: het is straling zonder "
                "lading. Alfa en bèta hebben wel een lading en buigen dus af, in tegengestelde zin.",
            ],
        ),
        dict(
            aanpak="E is m maal c kwadraat, met de massa in kilogram. Omdat c kwadraat negen maal "
                   "tien tot de zestiende is, levert elke gram een enorme energie.",
            waarom=[
                "Let op de omzetting: twee gram is 0,002 kilogram. En dat kleine beetje massa geeft "
                "al tien tot de veertiende joule, ongeveer wat een grote stad op een paar uur "
                "verbruikt.",
                None,
                None,
                "Noem de twee stappen. De bindingsenergie volgt uit het massadefect maal c kwadraat, "
                "en pas daarna deel je door het massagetal om de energie per kerndeeltje te "
                "krijgen.",
            ],
        ),
        dict(
            aanpak="Hou de drie dosissen uit elkaar: de geabsorbeerde dosis in gray, de equivalente "
                   "dosis met de weegfactor van de stralingssoort, en de effectieve dosis met de "
                   "weegfactor van het weefsel.",
            waarom=[
                None,
                "Let op het verschil tussen de twee weegfactoren: de ene hoort bij de soort "
                "straling, de andere bij het bestraalde weefsel. Beide staan in sievert.",
                None,
                "Let op dat de geabsorbeerde dosis dezelfde is en toch de schade twintig keer groter. "
                "Juist dat verschil is waarom men met sievert en niet met gray naar risico kijkt.",
            ],
        ),
        dict(
            aanpak="Splijting gaat van zwaar naar middelzwaar, fusie van licht naar middelzwaar. "
                   "Beide bewegen naar ijzer toe, en dat is waarom er energie vrijkomt.",
            waarom=[
                None,
                None,
                "Noem de top van de curve. Ijzer-56 heeft de grootste bindingsenergie per "
                "kerndeeltje, dus is er geen weg meer omhoog, niet van links en niet van rechts.",
                "Let op het verschil tussen de moderator en de regelstaven: de moderator vertraagt "
                "de neutronen zodat ze beter splijten, de regelstaven slorpen ze op om de reactie te "
                "temperen.",
                None,
                "Let op dat een rendement van een derde betekent dat twee derde als warmte "
                "verdwijnt. Dat is waarom een centrale aan een rivier of aan de zee staat.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een centrale wel en niet uitstoot, hoe "
                   "gevaarlijk een soort straling is binnen of buiten het lichaam, en wat de "
                   "eenheden betekenen.",
            waarom=[
                "Niet waar: bij het opwekken zelf komt er geen koolstofdioxide vrij. Bij het bouwen "
                "van de centrale en het winnen van het uranium wel, dus volledig nul is het niet.",
                "Niet waar: doorstraald voedsel wordt niet radioactief. De straling doodt enkel de "
                "micro-organismen en gaat er dan door, zoals licht door glas.",
                "Niet waar: België heeft nog geen definitieve bergingsplaats voor hoogactief afval "
                "van categorie C. Dat is precies waarom dat afval nu bovengronds bewaard wordt.",
                "Niet waar: bij een kernproces verdwijnt er een beetje massa, en die wordt energie. "
                "Dat massadefect is net waar de energie uit komt.",
                None,
                None,
                None,
                "Niet waar, het is net omgekeerd: van buiten houdt je huid alfastraling al tegen. "
                "Binnen in het lichaam is ze juist het gevaarlijkst, want daar geeft ze al haar "
                "energie aan weefsel af.",
                None,
                None,
                "Niet waar: gammastraling heeft geen lading, dus buigt ze niet af, niet in een "
                "elektrisch en niet in een magnetisch veld.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een uitleg. Noem telkens de drie beschermingsmaatregelen, "
                   "het orgaan dat het stofje opneemt, of het verschil tussen buiten en binnen het "
                   "lichaam.",
            waarom=[
                "Noem er drie, zoals gevraagd, en zeg bij elk waarom het werkt: afstand, tijd en "
                "afscherming. Dat rijtje is het waard om vanbuiten te kennen.",
                "Noem dat de schildklier jodium opneemt. Vul je ze met gewoon jodium, dan is er geen "
                "plaats meer voor de radioactieve soort.",
                "Noem dat alfastraling haar energie in een klein gebied afgeeft. Dezelfde energie "
                "geconcentreerd op enkele cellen doet veel meer schade dan verspreid over een groot "
                "volume.",
                "Noem van elk waar de bron zit. Bij bestraling blijft de bron buiten je en stopt het "
                "als je weggaat; bij besmetting zit de stof op of in je lichaam en gaat ze mee.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meetinstrumenten-en-meetonzekerheid-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke grootheid het toestel met de passende eenheid. Een multimeter "
                   "doet er meerdere, maar dan moet je wel de juiste stand kiezen.",
            waarom=[
                None,
                "Let op waar je de meter zet: een voltmeter parallel over het onderdeel, een "
                "ampèremeter in serie in de kring. Een ampèremeter parallel aansluiten is de "
                "klassieke manier om er een te verbranden.",
            ],
        ),
        dict(
            aanpak="Zet alles om via de macht van tien van het voorvoegsel. Voor km per uur naar "
                   "meter per seconde deel je door 3,6, omgekeerd vermenigvuldig je.",
            waarom=[
                None,
                "Let op de microfarad: 470 microfarad is 470 maal tien tot de min zes farad. De "
                "farad is zo groot dat je in de praktijk altijd met micro of nano werkt.",
            ],
        ),
        dict(
            aanpak="Leer de voorvoegsels als een rij van machten van drie: kilo, mega, giga naar "
                   "boven, en milli, micro, nano naar beneden. Centi en deci vallen daarbuiten.",
            waarom=[
                None,
                "Let op dat centi tien tot de min twee is en dus niet in de rij van drie past. "
                "Hetzelfde geldt voor deci, tien tot de min één.",
            ],
        ),
        dict(
            aanpak="Beduidende cijfers zeggen hoe fijn er gemeten is. Nullen vooraan tellen niet "
                   "mee, nullen achteraan na een komma wel.",
            waarom=[
                "Let op 0,0340: de nul vooraan telt niet mee, de nul achteraan wel, dus drie "
                "beduidende cijfers. Bij 1200 zonder komma zijn er maar twee.",
                "Let op dat de slechtste meting het antwoord bepaalt. Bij optellen gaat het om het "
                "aantal cijfers na de komma, bij vermenigvuldigen om het aantal beduidende cijfers.",
                "Noem dat je niet fijner mag noteren dan je meet. Een lat tot op de millimeter geeft "
                "hoogstens één cijfer na de komma in centimeter.",
                None,
                "Noem het aantal beduidende cijfers. Die extra nul is geen opsmuk maar een "
                "mededeling: er is tot op drie cijfers gemeten.",
            ],
        ),
        dict(
            aanpak="Kies een bereik dat net boven je verwachte waarde ligt en een nauwkeurigheid die "
                   "bij de grootte van je meting past. Te grof en te fijn zijn beide fout.",
            waarom=[
                "Let op de twee soorten fout: de eerste meting gaat buiten het bereik van de meter, "
                "de tweede is binnen het bereik maar veel te grof. Drie gram op een weegschaal van "
                "één gram geeft maar één cijfer.",
                "Let op dat de nauwkeurigheid altijd tegenover de grootte van je meting staat. Een "
                "tiende seconde op een halve seconde is twintig procent, een centimeter op zes meter "
                "bijna niets.",
            ],
        ),
        dict(
            aanpak="Een grafiek verraadt het verband: een rechte door de oorsprong is recht "
                   "evenredig, een rechte met een snijpunt is lineair, een dalende kromme is "
                   "omgekeerd evenredig.",
            waarom=[
                None,
                "Let op het verschil tussen recht evenredig en lineair: bij recht evenredig gaat de "
                "rechte door de oorsprong, bij lineair hoeft dat niet. Dat kleine getal q maakt het "
                "verschil.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over het kiezen van een instrument, over eenheden, en over "
                   "veilig werken. Vraag je bij elke af welk van de drie.",
            waarom=[
                "Niet waar: een te nauwkeurig toestel is vaak trager, duurder en gevoeliger. Je kiest "
                "een nauwkeurigheid die bij je meting past.",
                "Niet waar: zonder eenheid betekent een getal niets. Dat is in de fysica geen "
                "vormfout maar een echte fout.",
                None,
                None,
                "Niet waar: water geleidt, en een natte hand verlaagt de weerstand van je lichaam "
                "sterk. Ook bij een lage spanning blijf je met droge handen werken.",
            ],
        ),
        dict(
            aanpak="Let bij deze drie op het aflezen zelf en op wat er na de proef gebeurt. Opruimen "
                   "hoort bij het werk, niet erna.",
            waarom=[
                "Niet waar: van opzij lees je een analoge meter fout af, want de naald hangt boven de "
                "schaal. Dat is de parallaxfout, en je vermijdt ze door recht van boven te kijken.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Zoek bij elk geval welke van de drie klassieke fouten het is: een voorvoegsel "
                   "kwijt, te veel cijfers, of geen eenheid.",
            waarom=[
                "Noem het voorvoegsel. Vijfhonderd milliampère is een halve ampère, dus zit er een "
                "factor duizend verschil tussen de twee notaties.",
                "Noem dat de slechtste meting het aantal cijfers bepaalt. Twee komma vijf heeft één "
                "cijfer na de komma, dus het antwoord ook.",
                "Noem dat de eenheid ontbreekt. Tweehonderddertig kan volt, ohm of milliampère zijn, "
                "en dat zijn drie heel verschillende metingen.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een reden. Noem telkens wat er kan mislopen en hoe je "
                   "dat voorkomt.",
            waarom=[
                "Noem dat je zo rustig kan opdrijven. Bij een verkeerde schakeling merk je het bij "
                "een lage spanning nog voor er iets doorbrandt.",
                "Noem je reactietijd en vergelijk ze met de meting. Een tiende seconde op een halve "
                "seconde is twintig procent, en dat is veel te veel.",
                "Noem dat je de waarde niet overneemt. Eerst bereik, aansluiting en stand nagaan, "
                "dan opnieuw meten; een onmogelijke waarde opschrijven is nooit het antwoord.",
                "Noem ook hoe je ze vermijdt, zoals gevraagd. De naald hangt boven de schaal, dus "
                "kijk je recht van boven en niet schuin.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De zes stappen staan in een vaste orde: eerst denken, dan meten, dan verwerken, "
                   "dan besluiten. De hypothese komt altijd vóór de metingen.",
            waarom=[
                "Let op dat de hypothese op de derde plaats staat, dus voor het meten. Een "
                "verwachting die je achteraf opschrijft, is geen hypothese meer.",
            ],
        ),
        dict(
            aanpak="Een bruikbare onderzoeksvraag noemt twee grootheden en een verband ertussen. "
                   "Staat er geen meetbare grootheid in, dan is ze te breed.",
            waarom=[
                None,
                "Let op dat een bruikbare vraag altijd de vorm heeft hoe hangt A af van B. Daarin "
                "zitten je twee variabelen al.",
            ],
        ),
        dict(
            aanpak="Drie soorten variabelen: die jij instelt, die je meet, en die je gelijk houdt. "
                   "Zonder die derde soort is je proef niets waard.",
            waarom=[
                None,
                None,
                "Let op de afspraak voor de assen: wat jij instelt komt op de horizontale as, wat je "
                "meet op de verticale. Dus de valtijd in functie van de hoogte en niet omgekeerd.",
            ],
        ),
        dict(
            aanpak="In een verslag staat alles wat iemand anders nodig heeft om je proef over te "
                   "doen. Alles wat daar niets aan bijdraagt, mag weg.",
            waarom=[
                None,
                "Let op dat ook een weggelaten meting in het verslag hoort, mét de reden. Een "
                "meting stil laten verdwijnen is niet eerlijk; ze vermelden en verantwoorden wel.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een geldig resultaat is, hoever een "
                   "conclusie mag gaan, en hoe je een proef opzet.",
            waarom=[
                None,
                "Niet waar: een conclusie blijft binnen wat je gemeten hebt. Meet je tot twee meter "
                "hoog, dan zeg je niets over tien meter.",
                "Niet waar: verander er één per keer, anders weet je niet welke voor het verschil "
                "zorgde. Juist dat is wat een proef van een losse observatie onderscheidt.",
                None,
                "Niet waar: STEM betekent net dat je de disciplines samenbrengt. Eén vak grondig "
                "inzetten is geen STEM-opdracht.",
            ],
        ),
        dict(
            aanpak="Let bij deze drie op de orde van de stappen en op wat een criterium "
                   "bruikbaar maakt. Een criterium moet je kunnen nameten.",
            waarom=[
                "Niet waar: de hypothese komt vóór de metingen. Anders heb je geen verwachting maar "
                "een beschrijving van wat je al weet.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Een criterium is een eis die je kan nameten, met een getal en een eenheid. Een "
                   "mening kan je niet nameten, en hoort dus niet in je lijst.",
            waarom=[
                None,
                "Let op dat de tweede een mening is: sportief uitzien kan niemand nameten. Met een "
                "getal en een eenheid wordt een eis een criterium.",
                "Schrijf er twee, zoals gevraagd, en geef elk een getal en een eenheid. Eén over het "
                "resultaat en één over de middelen is een goede combinatie.",
            ],
        ),
        dict(
            aanpak="Deze vier vragen vragen een uitleg. Noem telkens de toevallige fout, de "
                   "weerlegbaarheid, of wat elk vak aan de oplossing bijdraagt.",
            waarom=[
                "Noem de toevallige afwijking. Door te herhalen en het gemiddelde te nemen vallen die "
                "afwijkingen grotendeels weg; een systematische fout verdwijnt er wel niet mee.",
                "Noem dat een onweerlegbare verwachting niets te onderzoeken geeft. Juist doordat de "
                "meting je hypothese kan tegenspreken, leer je er iets uit.",
                "Noem de vier letters en geef bij elk zijn bijdrage, zoals gevraagd. Wetenschappen, "
                "technologie, techniek en wiskunde.",
                "Noem dat de keuzes ieders energie en kosten raken. Een technische vraag is zo ook "
                "een maatschappelijke keuze, en dat is net wat STEM bedoelt.",
            ],
        ),
    ],
)

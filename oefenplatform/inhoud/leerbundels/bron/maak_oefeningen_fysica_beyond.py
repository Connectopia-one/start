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
             opdracht="De gravitatiekracht was 60 N. Schrijf de nieuwe kracht.",
             oefeningen=[
                 ("rij", [("de afstand verdubbelt", "15 N"), ("één massa verdubbelt", "120 N"),
                          ("de afstand wordt drie keer groter", "6,67 N")],
                  "Welke kracht nu?", WW),
                 ("rij", [("beide massa's verdubbelen", "240 N"),
                          ("de afstand halveert", "240 N"),
                          ("één massa halveert", "30 N")],
                  "Welke kracht nu?", WW),
             ]),
        dict(kop="Rekenen aan een cirkelbeweging",
             opdracht="Reken uit met v = 2πr/T en a = v²/r.",
             oefeningen=[
                 ("kort", "Een punt draait op r = 0,5 m met een periode van π seconden. Welke snelheid?",
                  "1 m/s, want 2π · 0,5 gedeeld door π.", WW),
                 ("kort", "v = 4 m/s op een cirkel van r = 2 m. Hoe groot is de centripetale versnelling?",
                  "8 m/s², want 16 gedeeld door 2.", WW),
                 ("kort", "m = 3 kg, v = 4 m/s, r = 2 m. Hoe groot is de centripetale kracht?",
                  "24 N, want 3 · 8.", W),
                 ("kort", "Een rad draait 2 keer per seconde rond. Hoe groot is de periode?",
                  "0,5 s, want 1 gedeeld door 2.", W),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een eenparige cirkelbeweging blijft de snelheid constant in grootte.", True),
                 ("waar", "Bij een eenparige cirkelbeweging is er geen versnelling.", False),
                 ("waar", "De centripetale kracht wijst naar het middelpunt van de cirkel.", True),
                 ("waar", "Een satelliet in een baan om de aarde ondervindt geen zwaartekracht.", False),
                 ("waar", "Hoe verder een planeet van de zon, hoe langer haar omlooptijd.", True),
             ]),
        dict(kop="Wie levert de kracht?",
             opdracht="Antwoord in één of twee woorden.",
             oefeningen=[
                 ("rij", [("de maan rond de aarde", "de gravitatiekracht"),
                          ("een auto in een bocht", "de wrijving van de wielen")],
                  "Wat levert de centripetale kracht?", WL),
                 ("rij", [("een bal aan een touw rondzwaaien", "de spankracht van het touw"),
                          ("een elektron rond een kern", "de coulombkracht")],
                  "Wat levert de centripetale kracht?", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een eenparige cirkelbeweging heeft een constante snelheid in grootte en tóch een versnelling. Leg dat uit.",
                  "Versnelling is de verandering van de snelheidsvector, niet alleen van haar "
                  "grootte. De richting draait voortdurend, en die verandering is de centripetale "
                  "versnelling, naar het middelpunt gericht.", 6),
                 ("open", "Waarom voelt een astronaut in het ruimtestation zich gewichtloos, terwijl de zwaartekracht er bijna even groot is als op aarde?",
                  "Het station en de astronaut vallen samen rond de aarde: de zwaartekracht dient "
                  "volledig als centripetale kracht. Er is dus geen vloer die tegen hem duwt, en net "
                  "die tegenkracht voel je normaal als gewicht.", 7),
                 ("open", "Waarom slipt een auto in een bocht makkelijker bij regen?",
                  "De bocht vraagt een centripetale kracht, en die moet van de wrijving tussen de "
                  "wielen en de weg komen. Bij regen is die wrijving kleiner, dus volstaat ze niet "
                  "meer bij dezelfde snelheid.", 6),
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
             opdracht="Reken uit met W = F · s, met de kracht in de zin van de beweging.",
             oefeningen=[
                 ("rij", [("F = 25 N, s = 4 m", "W = 100 J"), ("W = 60 J, s = 3 m", "F = 20 N"),
                          ("F = 12 N, W = 72 J", "s = 6 m")],
                  "Wat ontbreekt?", WW),
                 ("kort", "Je duwt een kast 5 m vooruit met 80 N. Welke arbeid verricht je?",
                  "400 J, want 80 · 5.", W),
                 ("kort", "Je houdt een boek van 20 N een minuut stil in je hand. Welke arbeid verricht je?",
                  "0 J, want er is geen verplaatsing.", WW),
             ]),
        dict(kop="Energievormen",
             opdracht="Reken uit. Neem g gelijk aan 10 m/s².",
             oefeningen=[
                 ("kort", "m = 2 kg op 5 m hoogte. Hoe groot is de zwaarte-energie?",
                  "100 J, want 2 · 10 · 5.", W),
                 ("kort", "m = 4 kg met v = 3 m/s. Hoe groot is de kinetische energie?",
                  "18 J, want ½ · 4 · 9.", W),
                 ("kort", "Hoe verandert de kinetische energie als de snelheid verdubbelt?",
                  "Ze wordt vier keer zo groot, want v staat in het kwadraat.", WL),
             ]),
        dict(kop="Behoud van energie",
             opdracht="Reken uit. Neem g gelijk aan 10 m/s² en verwaarloos de wrijving.",
             oefeningen=[
                 ("kort", "Een bal van 1 kg valt van 20 m. Welke snelheid heeft hij bij de grond?",
                  "20 m/s, want ½·v² is g·h, dus v is de wortel van 400.", WW),
                 ("open", "Een slinger zwaait heen en weer. Beschrijf hoe de energie onderweg verandert.",
                  "In de uiterste standen staat hij stil en is alles zwaarte-energie. Onderweg naar "
                  "het midden zet die om in kinetische energie, en in het laagste punt is de "
                  "snelheid maximaal en de zwaarte-energie minimaal. De som blijft gelijk zolang er "
                  "geen wrijving is.", 7),
             ]),
        dict(kop="Vermogen en rendement",
             opdracht="Reken uit met P = W/t.",
             oefeningen=[
                 ("kort", "900 J arbeid in 3 s. Welk vermogen?",
                  "300 W, want 900 gedeeld door 3.", W),
                 ("kort", "Een motor van 500 W werkt 20 s. Welke arbeid?",
                  "10 000 J, want 500 · 20.", W),
                 ("kort", "Een motor krijgt 1000 J en levert 250 J nuttige arbeid. Welk rendement?",
                  "25 %, want 250 gedeeld door 1000.", W),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een kracht loodrecht op de beweging verricht geen arbeid.", True),
                 ("waar", "Het rendement van een echte machine kan 100 % zijn.", False),
                 ("waar", "De zwaartekracht is een conservatieve kracht.", True),
                 ("waar", "De arbeid van de wrijvingskracht hangt niet van de gevolgde weg af.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je draagt een boodschappentas horizontaal over 20 m. Verricht je arbeid op de tas? Leg uit.",
                  "Op de tas niet: je kracht wijst naar boven en de verplaatsing is horizontaal, dus "
                  "staan ze loodrecht op elkaar. Je spieren verbruiken wel energie, maar dat is iets "
                  "anders dan arbeid op de tas.", 6),
                 ("open", "Leg uit wat men bedoelt met een conservatieve kracht, met een voorbeeld.",
                  "Een kracht waarvan de arbeid alleen van het begin- en eindpunt afhangt en niet "
                  "van de weg ertussen. De zwaartekracht is er een: of je recht omhoog klimt of via "
                  "een lange helling, de arbeid tegen de zwaartekracht is dezelfde.", 6),
                 ("open", "Waarom is het rendement van een gloeilamp zo laag?",
                  "Het grootste deel van de elektrische energie wordt warmte in plaats van licht. "
                  "Alleen dat licht is het nuttige deel, en dus blijft het rendement klein.", 5),
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
                 ("rij", [("de temperatuur blijft gelijk", "isotherm"),
                          ("de druk blijft gelijk", "isobaar"),
                          ("het volume blijft gelijk", "isochoor")],
                  "Welk proces?", WW),
                 ("rij", [("een gesloten metalen vat verwarmen", "isochoor"),
                          ("een ballon in de zon leggen", "isobaar"),
                          ("een spuit langzaam indrukken bij kamertemperatuur", "isotherm")],
                  "Welk proces?", WW),
             ]),
        dict(kop="Temperatuur omrekenen",
             opdracht="Reken om. 0 °C is 273 K.",
             oefeningen=[
                 ("rij", [("27 °C", "300 K"), ("−73 °C", "200 K"), ("127 °C", "400 K")],
                  "Hoeveel kelvin?", WW),
                 ("rij", [("500 K", "227 °C"), ("273 K", "0 °C"), ("350 K", "77 °C")],
                  "Hoeveel graden celsius?", WW),
             ]),
        dict(kop="Rekenen met de gaswetten",
             opdracht="Reken uit. Gebruik altijd kelvin.",
             oefeningen=[
                 ("kort", "Isotherm: 3 L bij 100 kPa wordt samengeperst tot 1 L. Welke druk?",
                  "300 kPa, want p · V blijft gelijk.", WW),
                 ("kort", "Isobaar: 2 L bij 300 K wordt opgewarmd tot 450 K. Welk volume?",
                  "3 L, want V/T blijft gelijk.", WW),
                 ("kort", "Isochoor: 200 kPa bij 250 K wordt opgewarmd tot 500 K. Welke druk?",
                  "400 kPa, want p/T blijft gelijk.", WW),
                 ("kort", "Van 2 L bij 100 kPa en 300 K naar 400 K bij 200 kPa. Welk volume?",
                  "ongeveer 1,33 L, want pV/T blijft gelijk.", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In de gaswetten mag je de temperatuur in graden celsius invullen.", False),
                 ("waar", "Bij constante temperatuur zijn druk en volume omgekeerd evenredig.", True),
                 ("waar", "Bij een ideaal gas verwaarloost men het eigen volume van de moleculen.", True),
                 ("waar", "De druk van een gas komt van de botsingen van de moleculen op de wand.", True),
                 ("waar", "Bij 0 K beweegt een gasmolecule nog even snel als bij kamertemperatuur.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg met het deeltjesmodel uit waarom de druk stijgt als je een gas verwarmt bij constant volume.",
                  "Bij een hogere temperatuur bewegen de moleculen sneller. Ze botsen dus vaker en "
                  "harder op de wand, en die botsingen samen zijn net de druk.", 6),
                 ("open", "Waarom staat er op een spuitbus dat je ze niet in het vuur mag gooien?",
                  "Het volume staat vast, dus stijgt de druk mee met de temperatuur. Boven een "
                  "zekere druk houdt de bus het niet en ontploft ze.", 5),
                 ("open", "Waarom gebruik je in de gaswetten kelvin en niet celsius?",
                  "De wetten zijn verhoudingen, en die gelden enkel vanaf een echt nulpunt. De "
                  "celsiusschaal heeft haar nul bij het smeltpunt van water, dus zou een "
                  "verdubbeling van de temperatuur daar niets betekenen.", 6),
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
        dict(kop="Rekenen met Q = c · m · ΔT",
             opdracht="Neem c van water gelijk aan 4186 J/(kg·K).",
             oefeningen=[
                 ("kort", "Hoeveel warmte heb je nodig om 3 kg water 20 K op te warmen?",
                  "ongeveer 251 kJ, want 4186 · 3 · 20.", WW),
                 ("kort", "0,5 kg water krijgt 41 860 J. Hoeveel stijgt de temperatuur?",
                  "20 K, want 41 860 gedeeld door (4186 · 0,5).", WW),
                 ("kort", "Hoeveel warmte heb je nodig om 1 kg ijzer 10 K op te warmen? Neem c gelijk aan 450 J/(kg·K).",
                  "4500 J, want 450 · 1 · 10.", WW),
             ]),
        dict(kop="Rekenen met Q = l · m",
             opdracht="Neem l van smelten gelijk aan 334 kJ/kg en l van verdampen gelijk aan 2256 kJ/kg, voor water.",
             oefeningen=[
                 ("kort", "Hoeveel warmte vraagt het smelten van 2 kg ijs van 0 °C?",
                  "668 kJ, want 334 · 2.", W),
                 ("kort", "Hoeveel warmte vraagt het verdampen van 0,5 kg water van 100 °C?",
                  "1128 kJ, want 2256 · 0,5.", W),
                 ("open", "Leg uit waarom de temperatuur tijdens het smelten niet stijgt.",
                  "Alle toegevoerde warmte gaat naar het losmaken van de deeltjes uit het rooster, "
                  "niet naar het sneller doen bewegen ervan. Pas als alles vloeibaar is, stijgt de "
                  "temperatuur weer.", 6),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Warmte en temperatuur zijn hetzelfde.", False),
                 ("waar", "Warmte stroomt spontaan van warm naar koud.", True),
                 ("waar", "Water heeft een hoge specifieke warmtecapaciteit in vergelijking met metalen.", True),
                 ("waar", "Bij een lagere luchtdruk kookt water bij een hogere temperatuur.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom koelt zweten je af?",
                  "Het verdampen van water vraagt veel warmte, en die haalt het zweet uit je huid. "
                  "Je huid verliest dus energie en koelt af.", 5),
                 ("open", "Een thermosfles heeft een vacuüm tussen twee spiegelende wanden. Leg uit wat elk van die twee tegenhoudt.",
                  "Het vacuüm heeft geen deeltjes, dus kan er geen warmte geleid of gestroomd "
                  "worden. De spiegelende wand kaatst de warmtestraling terug, en dat is de derde "
                  "weg die anders overblijft.", 6),
                 ("open", "Waarom strooit men zout op een besneeuwde weg, en waarom helpt dat niet bij strenge vorst?",
                  "Zout verlaagt het smeltpunt van het ijs, dus smelt het ook onder nul graden. Bij "
                  "strenge vorst zakt de temperatuur onder het verlaagde smeltpunt, en dan bevriest "
                  "de pekel toch.", 6),
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
             opdracht="Reken om. f is 1 gedeeld door T.",
             oefeningen=[
                 ("rij", [("T = 0,5 s", "f = 2 Hz"), ("f = 50 Hz", "T = 0,02 s"),
                          ("T = 0,2 s", "f = 5 Hz")],
                  "Wat ontbreekt?", WW),
                 ("rij", [("f = 4 Hz", "T = 0,25 s"), ("T = 2 s", "f = 0,5 Hz"),
                          ("f = 10 Hz", "T = 0,1 s")],
                  "Wat ontbreekt?", WW),
             ]),
        dict(kop="Uit de trillingsvergelijking lezen",
             opdracht="y = 0,04 · sin(10·t). Antwoord met eenheid.",
             oefeningen=[
                 ("kort", "Hoe groot is de amplitude?", "0,04 m, dus 4 cm.", W),
                 ("kort", "Hoe groot is de pulsatie?", "10 rad/s.", W),
                 ("kort", "Hoe groot is de beginfase?", "0 rad, dus ze vertrekt uit het evenwicht.", WW),
                 ("kort", "Hoe groot is de periode? Neem π gelijk aan 3,14.",
                  "ongeveer 0,63 s, want 2π gedeeld door 10.", WW),
             ]),
        dict(kop="De eigenfrequentie",
             opdracht="Schrijf hoger, lager of gelijk.",
             oefeningen=[
                 ("rij", [("een stijvere veer bij dezelfde massa", "hoger"),
                          ("een grotere massa aan dezelfde veer", "lager"),
                          ("een grotere amplitude bij dezelfde veer", "gelijk")],
                  "Eigenfrequentie?", WW),
                 ("rij", [("een langere slinger", "lager"), ("een zwaardere bol aan dezelfde slinger", "gelijk"),
                          ("dezelfde slinger op de maan", "lager")],
                  "Eigenfrequentie?", WW),
             ]),
        dict(kop="Waar staat wat maximaal?",
             opdracht="Schrijf in het evenwicht of in de uiterste stand.",
             oefeningen=[
                 ("rij", [("de snelheid is maximaal", "in het evenwicht"),
                          ("de versnelling is maximaal", "in de uiterste stand"),
                          ("de uitwijking is nul", "in het evenwicht")],
                  "Waar?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De amplitude van een trilling kan negatief zijn.", False),
                 ("waar", "Twee trillingen met een faseverschil van π radiaal zijn in tegenfase.", True),
                 ("waar", "Bij een gedempte trilling neemt vooral de frequentie snel af.", False),
                 ("waar", "Bij resonantie kan een kleine kracht een grote amplitude geven.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat resonantie is en geef één voorbeeld.",
                  "Resonantie treedt op als de frequentie van een aandrijvende kracht de "
                  "eigenfrequentie van het lichaam benadert; dan loopt de amplitude sterk op. Een "
                  "schommel die je telkens op het juiste ogenblik duwt, gaat zo steeds hoger.", 6),
                 ("open", "Waarom zet men dempers in een gebouw dat tegen aardbevingen moet kunnen?",
                  "Een aardbeving kan het gebouw op zijn eigenfrequentie aandrijven, en dan wordt de "
                  "amplitude gevaarlijk groot. Dempers halen energie uit de trilling, zodat die "
                  "amplitude beperkt blijft.", 6),
                 ("open", "Waarom was een slingeruurwerk nauwkeurig, ook als de slinger wat minder ver uitzwaaide?",
                  "Bij een kleine uitslag hangt de periode van een slinger alleen van zijn lengte en "
                  "van g af, niet van de amplitude. Een kleinere uitslag verandert het ritme dus "
                  "bijna niet.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-golven-en-hun-eigenschappen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Golven en hun eigenschappen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rekenen met v = λ · f",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("λ = 4 m, f = 25 Hz", "v = 100 m/s"), ("v = 340 m/s, f = 170 Hz", "λ = 2 m"),
                          ("v = 12 m/s, λ = 3 m", "f = 4 Hz")],
                  "Wat ontbreekt?", WW),
                 ("kort", "Geluid loopt 340 m/s. Welke golflengte hoort bij 1700 Hz?",
                  "0,2 m, want 340 gedeeld door 1700.", WW),
                 ("kort", "Licht loopt 3 · 10⁸ m/s. Welke frequentie hoort bij een golflengte van 600 nm?",
                  "5 · 10¹⁴ Hz, want 3 · 10⁸ gedeeld door 6 · 10⁻⁷.", WL),
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
                 ("rij", [("de frequentie", "blijft gelijk"), ("de golflengte", "verandert"),
                          ("de snelheid", "verandert")],
                  "Bij breking?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een golf vervoert energie zonder materie te verplaatsen.", True),
                 ("waar", "Een golf met een grotere amplitude loopt sneller.", False),
                 ("waar", "Een knoop van een staande golf trilt helemaal niet.", True),
                 ("waar", "Alle deeltjes van een lopende golf beginnen samen te trillen.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een bron trilt al 5 s. Een deeltje ligt 12 m verder en de golf loopt 4 m/s. Hoelang trilt dat deeltje al? Reken voor.",
                  "2 s. De golf had 12 gedeeld door 4, dus 3 s nodig om er te komen, en dus trilt "
                  "het deeltje 5 min 3 seconden.", 5),
                 ("open", "Leg uit waarom je het gebrom van een feest verder hoort dan de hoge tonen.",
                  "Lage tonen hebben een grote golflengte en buigen daardoor veel beter af rond "
                  "huizen en hoeken. Hoge tonen met een kleine golflengte worden tegengehouden.", 6),
                 ("open", "Wat zegt het principe van Huygens, en wat verklaar je ermee?",
                  "Elk punt van een golffront werkt zelf als een nieuwe bron van golfjes. Daarmee "
                  "verklaar je weerkaatsing, breking en buiging in één keer.", 6),
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
        dict(kop="Rekenen aan geluid",
             opdracht="Neem de geluidssnelheid in lucht gelijk aan 340 m/s.",
             oefeningen=[
                 ("kort", "Je hoort de donder 9 s na de bliksem. Hoe ver is het onweer?",
                  "ongeveer 3 km, want 340 · 9.", WW),
                 ("kort", "Een echo komt na 2 s terug van een wand. Hoe ver staat die wand?",
                  "340 m, want het geluid legde 680 m af, heen en terug.", WW),
                 ("kort", "Een snaar heeft een grondfrequentie van 150 Hz. Welke frequentie heeft de vierde harmonische?",
                  "600 Hz, want 4 · 150.", WW),
             ]),
        dict(kop="Lenzen en spiegels",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("het beeld in een vlakke spiegel", "virtueel en even groot"),
                          ("een voorwerp verder dan 2f bij een bolle lens", "reëel, omgekeerd en kleiner")],
                  "Welk beeld?", WL),
                 ("waar", "Een virtueel beeld kan je op een scherm opvangen.", False),
                 ("waar", "Bij een ruw oppervlak kaatsen de stralen alle kanten op.", True),
             ]),
        dict(kop="Decibel en gehoor",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de gehoordrempel van een mens", "0 dB"),
                          ("de gevaargrens voor het gehoor", "80 dB"),
                          ("het hoorbare gebied", "20 tot 20 000 Hz")],
                  "Welke waarde?", WL),
                 ("open", "Je gaat drie keer zo dicht bij een luidspreker staan. Wat gebeurt er met de intensiteit? Leg uit.",
                  "Ze wordt negen keer zo groot. De intensiteit daalt met het kwadraat van de "
                  "afstand, dus geeft drie keer dichter een factor drie in het kwadraat.", 6),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit hoe blijvende gehoorschade in het binnenoor ontstaat.",
                  "De trilhaartjes op de haarcellen breken af door te hard of te lang geluid. Ze "
                  "groeien niet terug, dus is de schade blijvend.", 5),
                 ("open", "Wat is het dopplereffect, en verandert de bron daarbij iets aan zijn toon?",
                  "De waargenomen frequentie verschilt van de uitgezonden frequentie als bron en "
                  "waarnemer naar of van elkaar bewegen. De bron zelf zendt onveranderd dezelfde "
                  "frequentie uit; alleen de golven komen dichter op elkaar of verder uiteen.", 7),
                 ("open", "Waarom hoor je een verschil tussen een viool en een fluit die dezelfde toon spelen?",
                  "De grondfrequentie is dezelfde, maar de harmonischen erboven hebben een andere "
                  "sterkteverdeling. Dat verschil in de vorm van het patroon is de klankkleur of het "
                  "timbre.", 6),
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
             opdracht="De drempelfrequentie van het metaal is 5 · 10¹⁴ Hz. Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("licht van 7 · 10¹⁴ Hz", "ja"), ("licht van 3 · 10¹⁴ Hz", "nee"),
                          ("heel fel licht van 3 · 10¹⁴ Hz", "nee")],
                  "Komen er elektronen los?", WW),
                 ("rij", [("zwak licht van 6 · 10¹⁴ Hz", "ja"), ("licht van 5 · 10¹⁴ Hz", "ja"),
                          ("heel fel infrarood", "nee")],
                  "Komen er elektronen los?", WW),
             ]),
        dict(kop="Rekenen met E = h · f",
             opdracht="Neem h gelijk aan 6,63 · 10⁻³⁴ J·s.",
             oefeningen=[
                 ("kort", "Welke energie heeft een foton van 4 · 10¹⁴ Hz?",
                  "ongeveer 2,7 · 10⁻¹⁹ J.", WL),
                 ("kort", "Welke energie heeft een foton van 1 · 10¹⁵ Hz?",
                  "ongeveer 6,6 · 10⁻¹⁹ J.", WL),
                 ("kort", "Welk foton is energierijker: rood of blauw licht?",
                  "blauw, want het heeft een hogere frequentie en een kleinere golflengte.", WL),
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
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Eén elektron kan de energie van meerdere fotonen samen opnemen.", False),
                 ("waar", "Het experiment van Davisson en Germer liet het golfkarakter van elektronen zien.", True),
                 ("waar", "Het onzekerheidsbeginsel komt door de beperkingen van onze meettoestellen.", False),
                 ("waar", "De golffunctie geeft de kans om een deeltje op een plaats te vinden.", True),
                 ("waar", "Van een elektron in een atoom kan je een baan tekenen zoals van een planeet.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom het klassieke golfmodel het foto-elektrisch effect niet kan verklaren.",
                  "Volgens dat model zou fel rood licht na wat wachten genoeg energie aanbrengen om "
                  "elektronen los te maken. In werkelijkheid komt er met rood licht nooit één "
                  "elektron los, hoe fel het ook schijnt, want elk elektron krijgt precies één foton "
                  "en dat moet op zich genoeg energie hebben.", 7),
                 ("open", "Waarom merken we het golfkarakter van een voetbal niet?",
                  "Zijn massa is zo groot dat de bijhorende golflengte onvoorstelbaar klein wordt. "
                  "Bij een elektron is die golflengte van de orde van een atoom, en daar zie je het "
                  "effect dus wel.", 6),
                 ("open", "Je vuurt elektronen één per één door twee spleten. Wat zie je na lang wachten, en waarom is dat merkwaardig?",
                  "Er staat toch een patroon van strepen op het scherm. Merkwaardig is dat elk "
                  "elektron als één stip aankomt, dus als deeltje, en dat ze samen toch het patroon "
                  "van een golf vormen.", 7),
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
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["nuclide", "A", "Z", "aantal neutronen"],
                  [["natrium-23", "23", "11", None], ["lood-207", "207", "82", None],
                   ["koolstof-14", "14", "6", None], ["uranium-235", "235", "92", None]],
                  "natrium-23: 12 · lood-207: 125 · koolstof-14: 8 · uranium-235: 143", W),
             ]),
        dict(kop="Welk verval?",
             opdracht="Schrijf alfa, bèta-min, bèta-plus of gamma.",
             oefeningen=[
                 ("rij", [("er vertrekt een heliumkern", "alfa"),
                          ("een neutron wordt een proton", "bèta-min"),
                          ("A en Z blijven gelijk", "gamma")],
                  "Welk verval?", WW),
                 ("rij", [("er vertrekt een positron", "bèta-plus"),
                          ("A daalt met vier en Z met twee", "alfa"),
                          ("Z stijgt met één en A blijft gelijk", "bèta-min")],
                  "Welk verval?", WW),
             ]),
        dict(kop="Na het verval",
             opdracht="Schrijf het nieuwe massagetal en atoomnummer.",
             oefeningen=[
                 ("rij", [("A 238, Z 92, alfaverval", "A 234, Z 90"),
                          ("A 14, Z 6, bèta-min-verval", "A 14, Z 7")],
                  "Wat krijg je?", WL),
                 ("rij", [("A 210, Z 84, alfaverval", "A 206, Z 82"),
                          ("A 60, Z 27, gammaverval", "A 60, Z 27")],
                  "Wat krijg je?", WL),
             ]),
        dict(kop="Halveringstijd",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Halveringstijd 6 dagen. Welk deel is er na 18 dagen nog over?",
                  "een achtste, want dat zijn drie halveringen.", WW),
                 ("kort", "Halveringstijd 4 jaar. Na hoeveel jaar is er nog een zestiende over?",
                  "16 jaar, want dat zijn vier halveringen.", WW),
                 ("kort", "Een bron van 1600 Bq heeft een halveringstijd van 3 uur. Welke activiteit na 9 uur?",
                  "200 Bq, want 1600 gedeeld door 8.", WW),
                 ("kort", "Halveringstijd 10 dagen. Hoe groot is de desintegratieconstante per dag?",
                  "ongeveer 0,069 per dag, want 0,693 gedeeld door 10.", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Na twee halveringstijden is een bron volledig vervallen.", False),
                 ("waar", "Je kan het verval van een radionuclide versnellen door te verwarmen.", False),
                 ("waar", "De activiteit van een bron staat in becquerel.", True),
                 ("waar", "Bij gammaverval verandert de kern in een ander element.", False),
                 ("waar", "Twee isotopen van hetzelfde element hebben hetzelfde atoomnummer.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom zijn zware kernen pas stabiel met meer neutronen dan protonen?",
                  "De protonen stoten elkaar over de hele kern af met de coulombkracht. Extra "
                  "neutronen voegen wel kernkracht toe maar geen extra afstoting, en houden de kern "
                  "zo samen.", 6),
                 ("open", "Leg uit waarop de koolstof-14-methode berust.",
                  "Een levend organisme vult zijn voorraad koolstof-14 aan uit de lucht. Na de dood "
                  "stopt dat, en daalt het gehalte met een vaste halveringstijd; uit wat er nog over "
                  "is, volgt de ouderdom.", 6),
                 ("open", "Een bron heeft een korte halveringstijd. Is haar activiteit bij dezelfde hoeveelheid groter of kleiner? Leg uit.",
                  "Groter. De activiteit is de desintegratieconstante maal het aantal kernen, en een "
                  "korte halveringstijd geeft een grote constante: er vervallen per seconde meer "
                  "kernen.", 6),
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
        dict(kop="Dosis",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de energie van de straling per kilogram weefsel", "de geabsorbeerde dosis"),
                          ("de eenheid daarvan", "gray")],
                  "Hoe heet dat?", WL),
                 ("rij", [("de geabsorbeerde dosis maal de stralingsweegfactor", "de equivalente dosis"),
                          ("houdt ook rekening met het bestraalde weefsel", "de effectieve dosis")],
                  "Hoe heet dat?", WL),
             ]),
        dict(kop="Rekenen met E = m · c²",
             opdracht="Neem c gelijk aan 3 · 10⁸ m/s.",
             oefeningen=[
                 ("kort", "Hoeveel energie zit er in 2 g massa?",
                  "ongeveer 1,8 · 10¹⁴ J, want 0,002 · 9 · 10¹⁶.", WL),
                 ("kort", "Hoeveel energie zit er in 0,5 kg massa?",
                  "4,5 · 10¹⁶ J.", WL),
             ]),
        dict(kop="Splijting of fusie",
             opdracht="Schrijf splijting of fusie.",
             oefeningen=[
                 ("rij", [("een zware kern valt uiteen", "splijting"),
                          ("twee lichte kernen worden één", "fusie"),
                          ("de energie van de zon", "fusie")],
                  "Splijting of fusie?", WW),
                 ("rij", [("een gewone kerncentrale op uranium", "splijting"),
                          ("waterstof wordt helium", "fusie"),
                          ("wordt met regelstaven in de hand gehouden", "splijting")],
                  "Splijting of fusie?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een kerncentrale op splijting stoot bij het opwekken van stroom CO₂ uit.", False),
                 ("waar", "Doorstraald voedsel wordt zelf radioactief.", False),
                 ("waar", "Voor hoogactief afval van categorie C ligt in België al een definitieve bergingsplaats vast.", False),
                 ("waar", "Bij een kernproces blijft de totale massa van de deeltjes precies gelijk.", False),
                 ("waar", "Natuurlijke straling komt onder meer van radon uit de bodem.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem de drie manieren om je tegen ioniserende straling te beschermen, en leg elk in één zin uit.",
                  "Afstand: de intensiteit daalt met het kwadraat van de afstand. Tijd: hoe korter "
                  "je in de buurt blijft, hoe kleiner de dosis. Afscherming: lood of beton tussen "
                  "jou en de bron zwakt de straling af.", 7),
                 ("open", "Waarom deelt men bij een kernongeval jodiumpillen uit?",
                  "De schildklier neemt jodium op. Door ze met gewoon jodium te vullen, kan ze geen "
                  "radioactief jodium meer opnemen, en blijft de dosis daar laag.", 6),
                 ("open", "Waarom gebruikt men bij een PET-scan een stof met een korte halveringstijd?",
                  "Dan is de straling in het lichaam snel weer weg, dus blijft de dosis voor de "
                  "patiënt beperkt terwijl het beeld toch gemaakt kan worden.", 6),
                 ("open", "Leg uit wat het verschil is tussen bestraling en besmetting.",
                  "Bij bestraling blijft de bron buiten je lichaam en stopt het zodra je weggaat. "
                  "Bij besmetting zit de radioactieve stof op of in je lichaam, en blijft ze dus "
                  "stralen tot ze verwijderd of vervallen is.", 7),
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
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [("3,5 mA in ampère", "0,0035 A"), ("2,2 kΩ in ohm", "2200 Ω"),
                          ("90 km/h in m/s", "25 m/s")],
                  "Hoeveel?", WW),
                 ("rij", [("0,25 MΩ in ohm", "250 000 Ω"), ("15 m/s in km/h", "54 km/h"),
                          ("470 µF in farad", "0,000470 F")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Schrijf de macht van tien.",
             oefeningen=[
                 ("rij", [("milli", "10⁻³"), ("micro", "10⁻⁶"), ("nano", "10⁻⁹")],
                  "Welke factor?", WW),
                 ("rij", [("kilo", "10³"), ("mega", "10⁶"), ("centi", "10⁻²")],
                  "Welke factor?", WW),
             ]),
        dict(kop="Beduidende cijfers",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("0,0340 m", "drie"), ("1200 g", "twee"), ("5,07 s", "drie")],
                  "Hoeveel beduidende cijfers?", WW),
                 ("kort", "Je telt 3,4 m en 2,15 m op. Hoe schrijf je het antwoord?",
                  "5,6 m, met één cijfer na de komma, want de slechtste meting bepaalt dat.", WL),
                 ("kort", "Hoe schrijf je 0,0000067 in wetenschappelijke notatie?",
                  "6,7 · 10⁻⁶.", WW),
             ]),
        dict(kop="Grafieken en verbanden",
             opdracht="Schrijf recht evenredig, omgekeerd evenredig of kwadratisch.",
             oefeningen=[
                 ("rij", [("een rechte door de oorsprong", "recht evenredig"),
                          ("een kromme die daalt en de assen nadert", "omgekeerd evenredig"),
                          ("een parabool door de oorsprong", "kwadratisch")],
                  "Welk verband?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een nauwkeuriger meetinstrument is altijd de beste keuze.", False),
                 ("waar", "Een antwoord zonder eenheid is in de fysica even goed.", False),
                 ("waar", "Een meetinstrument uitschakelen als je niet meet, hoort bij duurzaam werken.", True),
                 ("waar", "In de wetenschappelijke notatie staat er één cijfer voor de komma.", True),
                 ("waar", "Je mag elektrische toestellen met natte handen bedienen als de spanning laag is.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom zet je een spanningsbron op de laagste stand voor je hem aansluit?",
                  "Dan kan je de spanning rustig opdrijven en zien wat er gebeurt, zonder dat er "
                  "meteen iets doorbrandt bij een verkeerde schakeling.", 5),
                 ("open", "Waarom meet je een snelle beweging liever met een sensor dan met een handchronometer?",
                  "Je eigen reactietijd geeft bij de hand een fout van wel een tiende seconde. Bij "
                  "een meting van een halve seconde is dat een vijfde van het resultaat, en dus "
                  "onbruikbaar.", 6),
                 ("open", "Een toestel wijst een waarde aan die niet kan kloppen. Wat doe je?",
                  "Je neemt ze niet over. Eerst nagaan of je goed aangesloten en goed ingesteld "
                  "hebt, of je binnen het meetbereik zit, en dan opnieuw meten.", 6),
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
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een meting die je hypothese tegenspreekt, is een geldig resultaat.", True),
                 ("waar", "Een conclusie mag verder gaan dan wat je gemeten hebt.", False),
                 ("waar", "In een proef verander je het best meerdere grootheden tegelijk, dat gaat sneller.", False),
                 ("waar", "Een onderzoek moet herhaalbaar zijn: iemand anders moet met jouw plan hetzelfde vinden.", True),
                 ("waar", "Bij een STEM-opdracht volstaat het om één discipline grondig in te zetten.", False),
             ]),
        dict(kop="Ontwerpen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de eisen waaraan je oplossing moet voldoen", "de criteria"),
                          ("de kleinere stukken van een groot probleem", "de deelproblemen"),
                          ("waarin je alle deeloplossingen samenbrengt", "de totaaloplossing")],
                  "Hoe heet dat?", WL),
                 ("open", "Je ontwerpt een zonneoven die water tot 60 °C moet brengen. Schrijf twee criteria op.",
                  "Bijvoorbeeld: het water moet binnen twee uur 60 °C halen, en de oven moet met "
                  "materiaal uit de winkel te bouwen zijn voor minder dan twintig euro. Een "
                  "criterium is altijd meetbaar.", 6),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom herhaal je een meting meerdere keren?",
                  "Elke meting heeft een toevallige afwijking. Door te herhalen en het gemiddelde te nemen "
                  "vallen die afwijkingen grotendeels weg, en blijft het werkelijke verband over.", 5),
                 ("open", "Waarvoor staan de letters van STEM, en waarom bekijk je een probleem vanuit al die hoeken?",
                  "Wetenschappen, technologie, techniek en wiskunde. Elk vak brengt een stuk van de "
                  "oplossing aan: de wetenschap het waarom, de techniek het bouwen, de technologie "
                  "de middelen en de wiskunde het rekenwerk.", 7),
                 ("open", "Waarom is een onderzoek naar zonnepanelen ook een maatschappelijke zaak?",
                  "De keuzes die eruit volgen raken ieders energie en kosten, en bepalen mee hoe een "
                  "land zijn stroom maakt. Zulke uitdagingen zijn net een reden om nieuwe technieken "
                  "en materialen te ontwikkelen.", 6),
             ]),
    ],
)

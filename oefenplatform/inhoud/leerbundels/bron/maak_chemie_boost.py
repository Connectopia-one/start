# -*- coding: utf-8 -*-
"""De leerbundels voor chemie op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche chemie van de 2de graad doorstroomfinaliteit, geldig
vanaf 1 januari 2027. Die fiche geldt enkel voor de studierichting
natuurwetenschappen: die legt haar wetenschappen af in drie aparte examens,
biologie, chemie en fysica, in plaats van één examen natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De twaalf thema's volgen de weging van het examen: twee over de opbouw van
materie (10 %), één over de chemische reacties (5 %), drie over de atoom- en
molecuulbouw (20 %), vier over de organische en anorganische stoffen (40 %),
één over de berekeningen (15 %) en één over het onderzoek en STEM (10 %).

Twee afspraken van de fiche zelf staan in de bundels overgenomen, omdat bronnen
erover verschillen: een verschil in elektronegativiteit onder 0,4 geldt als
apolair, en de relatieve atoommassa wordt op 0,1 afgerond.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/chemie.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-chemie-boost-doorstroom".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Chemie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────── 1. Mengsels, zuivere stoffen en scheidingstechnieken
BUNDELS["mengsels-zuivere-stoffen-en-scheidingstechnieken-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Mengsels, zuivere stoffen en scheidingstechnieken",
    onder="Zuivere stoffen en mengsels, de soorten mengsels, de stofeigenschappen en de negen scheidingstechnieken.",
    secties=[
        dict(kop="Zuivere stof of mengsel", blokken=[
            ("p", "Een <strong>zuivere stof bestaat uit één soort deeltje</strong>, dus uit één soort "
                  "<strong>molecule</strong> of formule-eenheid. Een <strong>mengsel</strong> bevat "
                  "<strong>minstens twee bestanddelen</strong> die je er in principe weer uit kan halen."),
            ("p", "Een <strong>molecule</strong> is een <strong>deeltje dat uit meerdere atomen "
                  "bestaat</strong>, zoals H₂O of O₂."),
            ("p", "Bij een <strong>homogeen mengsel</strong> zie je de bestanddelen niet meer "
                  "afzonderlijk, ook niet met een microscoop. Bij een <strong>heterogeen "
                  "mengsel</strong> zie je ze nog wel, zoals zand in water of olie op azijn."),
            ("p", "Een <strong>oplossing</strong> van keukenzout in water is homogeen, en "
                  "<strong>brons, een legering van koper en tin</strong>, ook: een "
                  "<strong>legering is homogeen</strong>, want je ziet de metalen niet meer apart. "
                  "Zand in water en een slaatje met olie en azijn zijn heterogeen."),
        ]),
        dict(kop="De soorten mengsels", blokken=[
            ("p", tabel(["Soort mengsel", "Wat zit waarin", "Voorbeeld"], [
                ["aerosol", "vloeistof of vaste stof in een gas", "rook (vast), nevel (vloeibaar)"],
                ["oplossing", "opgeloste stof in een oplosmiddel", "keukenzout in water"],
                ["schuim", "gas in een vloeistof of vaste stof", "slagroom, badschuim"],
                ["suspensie", "vaste deeltjes zwevend in een vloeistof", "vruchtensap met pulp"],
                ["emulsie", "vloeistof in een vloeistof", "mayonaise, melk"],
                ["legering", "metaal in een metaal", "brons, messing"],
            ])),
            ("p", "<strong>Rook bestaat uit vaste deeltjes die in een gas zweven</strong>: dat is een "
                  "<strong>aerosol</strong>. <strong>Nevel</strong> is de vloeibare soort: "
                  "<strong>vloeibare druppeltjes die zweven in een gas</strong>, zoals mist in de lucht."),
            ("p", "<strong>Mayonaise bestaat uit olie en water die fijn verdeeld door elkaar "
                  "zitten</strong>: dat is een <strong>emulsie</strong>, een mengsel van twee "
                  "vloeistoffen die normaal niet mengen. <strong>Melk is geen heldere oplossing</strong> "
                  "maar ook een emulsie: er zweven vetbolletjes in het water, en daarom is ze wit en troebel."),
            ("p", "In een <strong>schuim</strong> zit een gas verdeeld in een vloeistof of in een vaste "
                  "stof. <strong>Slagroom is lucht in room.</strong>"),
            ("p", "Bij een <strong>suspensie</strong> zweven vaste deeltjes in een vloeistof zonder op te "
                  "lossen; ze <strong>zakken na een tijd naar de bodem</strong>. Een glas vruchtensap met "
                  "pulp is er een voorbeeld van."),
        ]),
        dict(kop="Aggregatietoestand en stofeigenschappen", blokken=[
            ("p", "De drie <strong>aggregatietoestanden</strong> zijn <strong>vast, vloeibaar en "
                  "gas</strong>. De aggregatietoestand zegt hoe de deeltjes ten opzichte van elkaar "
                  "liggen en bewegen: bij vast liggen ze vast, bij gas bewegen ze vrij door de ruimte."),
            ("p", "Een <strong>stofeigenschap hangt niet af van hoeveel je ervan hebt</strong>. Het "
                  "<strong>kookpunt</strong>, het <strong>smeltpunt</strong>, de "
                  "<strong>massadichtheid</strong>, de <strong>deeltjesgrootte</strong>, de "
                  "<strong>geleidbaarheid</strong>, de <strong>oplosbaarheid</strong> en het "
                  "<strong>aanhechtings- of adsorptievermogen</strong> zijn stofeigenschappen. De "
                  "<strong>massa en het volume van het staal zijn dat niet</strong>: die veranderen met "
                  "de hoeveelheid en zeggen dus niets over welke stof het is."),
            ("p", "De <strong>massadichtheid</strong> is de <strong>massa per volume</strong>, "
                  "bijvoorbeeld in kg/m³ of in g/L. Daarom zinkt een stof met een grotere massadichtheid "
                  "in water."),
            ("p", "De <strong>oplosbaarheid</strong> zegt <strong>hoeveel van een stof in een bepaald "
                  "volume oplosmiddel oplost</strong>, bij een bepaalde temperatuur."),
            ("p", "Het <strong>smeltpunt</strong> is de <strong>temperatuur waarbij een zuivere vaste "
                  "stof vloeibaar wordt</strong>. Voor elke zuivere stof is dat een vast getal, dus kan "
                  "je er twee witte poeders mee onderscheiden terwijl de kleur niet helpt."),
            ("p", "Het <strong>adsorptievermogen</strong> is de eigenschap die <strong>actieve kool "
                  "gebruikt om kleurstoffen uit water te halen</strong>: de deeltjes hechten zich vast "
                  "aan het enorme oppervlak van de kool."),
        ]),
        dict(kop="Kookpunt en kooktraject", blokken=[
            ("p", "Een <strong>zuivere stof heeft een vast kookpunt en een vast smeltpunt</strong>. Een "
                  "<strong>mengsel heeft een kooktraject</strong> en een <strong>smelttraject</strong>, "
                  "dus een <strong>temperatuurgebied</strong> in plaats van één punt."),
            ("p", "Dat komt doordat de <strong>samenstelling verandert terwijl het kookt</strong>: het "
                  "bestanddeel met het laagste kookpunt gaat er eerst uit, en daardoor stijgt de "
                  "temperatuur verder."),
        ]),
        dict(kop="De negen scheidingstechnieken", blokken=[
            ("p", tabel(["Techniek", "Werkt op een verschil in", "Voorbeeld"], [
                ["zeven", "deeltjesgrootte", "grind uit zand"],
                ["filtreren", "deeltjesgrootte", "zand uit water"],
                ["decanteren", "massadichtheid, niet mengen", "olie en water"],
                ["indampen of kristalliseren", "kookpunt", "zout uit pekel"],
                ["centrifugeren", "massadichtheid", "bloedcellen uit plasma"],
                ["destilleren", "kookpunt", "zuiver water uit zeewater"],
                ["extraheren", "oplosbaarheid", "cafeïne uit koffiebonen"],
                ["chromatografie", "aanhechtingsvermogen", "kleurstoffen in een stift"],
                ["adsorptie", "adsorptievermogen", "kleur- en geurstoffen aan actieve kool"],
            ])),
            ("p", "<strong>Zand uit water</strong> haal je met <strong>filtreren</strong>: de zandkorrels "
                  "zijn groter dan de poriën van het filter. Je kan het ook <strong>decanteren</strong>, "
                  "want het zand zakt naar de bodem en dan giet je het water eraf. <strong>Zeven en "
                  "filtreren werken allebei op een verschil in deeltjesgrootte</strong>, niet op een "
                  "verschil in kookpunt."),
            ("p", "Bij het filtreren heet de <strong>vloeistof die door het filter gaat het "
                  "filtraat</strong>, en wat <strong>op het filter achterblijft het residu</strong>. Het "
                  "is dus niet omgekeerd."),
            ("p", "<strong>Een oplossing van zout in water kan je niet filtreren</strong> om het zout "
                  "eruit te halen: opgeloste ionen zijn veel kleiner dan de poriën. Je moet het water "
                  "laten verdampen, met <strong>indampen</strong> of <strong>kristalliseren</strong>."),
            ("p", "<strong>Zuiver water uit zeewater</strong> haal je met <strong>destilleren</strong>, dus met een "
                  "<strong>destillatie</strong>: water en zout hebben een heel verschillend kookpunt. Bij destilleren "
                  "<strong>koelt de damp in een liebigkoeler weer af tot vloeistof</strong> en vang je "
                  "die op als <strong>destillaat</strong>."),
            ("p", "<strong>Olie en water in twee lagen</strong> scheid je met <strong>decanteren</strong>, "
                  "in een <strong>scheitrechter</strong>, die twee <strong>vloeistoflagen</strong> van "
                  "elkaar laat lopen: die heeft onderaan een kraantje, dus kan je de "
                  "onderste laag eruit laten lopen en op tijd stoppen. Dat werkt omdat de twee "
                  "<strong>een verschillende massadichtheid hebben en niet mengen</strong>; olie heeft de "
                  "kleinste massadichtheid en gaat bovenaan liggen."),
            ("p", "<strong>Centrifugeren</strong> gebruikt een <strong>draaiende beweging om zware "
                  "deeltjes sneller te laten zakken</strong>: de deeltjes met de grootste massadichtheid "
                  "gaan naar buiten."),
            ("p", "<strong>De kleurstoffen in een stift</strong> scheid je met "
                  "<strong>chromatografie</strong>: een oplosmiddel loopt over papier mee, en elke "
                  "kleurstof hecht anders aan het papier en komt dus op een andere hoogte terecht."),
            ("p", "<strong>Cafeïne uit koffiebonen</strong> haal je met <strong>extraheren</strong>: je "
                  "kiest een oplosmiddel waarin enkel de gewenste stof goed oplost."),
            ("p", "Twee vloeistoffen die <strong>wel mengen maar een verschillend kookpunt hebben</strong>, "
                  "scheid je met <strong>destilleren</strong>; decanteren werkt daar niet."),
            ("weetje", "Een waterzuiveringsstation gebruikt na het filteren ook adsorptie aan actieve "
                       "kool. De kleur- en geurstoffen lossen niet op en gaan door geen enkel filter, "
                       "maar ze blijven wel aan de kool hangen."),
        ]),
    ],
    onthoud=[
        "Een zuivere stof heeft één soort deeltje; een mengsel heeft minstens twee bestanddelen.",
        "Homogeen betekent dat je de bestanddelen niet meer apart ziet; een legering en een oplossing zijn homogeen.",
        "Aerosol is in een gas, emulsie is vloeistof in vloeistof, schuim is gas in vloeistof, suspensie zakt naar de bodem.",
        "Een stofeigenschap hangt niet af van de hoeveelheid; massa en volume van het staal dus niet.",
        "Een zuivere stof heeft een kookpunt, een mengsel een kooktraject.",
        "Zeven en filtreren werken op deeltjesgrootte, destilleren op kookpunt, extraheren op oplosbaarheid.",
        "Filtraat gaat door het filter, residu blijft erop liggen.",
        "Opgelost zout haal je niet uit water met een filter maar met indampen of kristalliseren.",
        "Decanteren doe je met een scheitrechter, bij vloeistoffen die niet mengen.",
    ],
)

# ───────────────────── 2. Enkelvoudige en samengestelde stoffen
BUNDELS["enkelvoudige-en-samengestelde-stoffen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Enkelvoudige en samengestelde stoffen",
    onder="De namen en symbolen van de elementen, een formule lezen, en de eigenschappen van metalen, niet-metalen en edelgassen.",
    secties=[
        dict(kop="Namen en symbolen van de elementen", blokken=[
            ("p", "Het <strong>eerste letterteken van een elementsymbool is een hoofdletter</strong>, en "
                  "een eventuele tweede letter is klein: Mg, Cl, Na."),
            ("p", tabel(["Symbool", "Naam", "Symbool", "Naam"], [
                ["H", "waterstof", "Na", "natrium"],
                ["He", "helium", "Mg", "magnesium"],
                ["Li", "lithium", "Al", "aluminium"],
                ["Be", "beryllium", "Si", "silicium"],
                ["B", "boor", "P", "fosfor"],
                ["C", "koolstof", "S", "zwavel"],
                ["N", "stikstof", "Cl", "chloor"],
                ["O", "zuurstof", "Ar", "argon"],
                ["F", "fluor", "K", "kalium"],
                ["Ne", "neon", "Ca", "calcium"],
            ])),
            ("p", tabel(["Symbool", "Naam", "Symbool", "Naam"], [
                ["Cr", "chroom", "Ag", "zilver"],
                ["Mn", "mangaan", "Cd", "cadmium"],
                ["Fe", "ijzer", "Sn", "tin"],
                ["Co", "kobalt", "Sb", "antimoon"],
                ["Ni", "nikkel", "I", "jood"],
                ["Cu", "koper", "Xe", "xenon"],
                ["Zn", "zink", "Ba", "barium"],
                ["Ge", "germanium", "Pt", "platina"],
                ["As", "arseen", "Au", "goud"],
                ["Br", "broom", "Hg", "kwik"],
                ["Kr", "krypton", "Pb", "lood"],
                ["Rn", "radon", "U", "uranium"],
                ["Pu", "plutonium", "", ""],
            ])),
            ("p", "Let op de symbolen die van een Latijnse naam komen: <strong>Fe is ijzer</strong> "
                  "(ferrum), <strong>Na is natrium</strong>, <strong>K is kalium</strong>, "
                  "<strong>Ag is zilver</strong> (argentum) en Au is goud (aurum). Verwar ze niet met "
                  "fosfor (P), fluor (F), stikstof (N), calcium (Ca) of chloor (Cl)."),
            ("p", "Twee valkuilen: <strong>koolstof is C en niet Co</strong>, want Co is kobalt. En "
                  "<strong>magnesium is Mg en niet Mn</strong>, want Mn is mangaan."),
            ("p", "<strong>Cu (koper)</strong> en <strong>Zn (zink)</strong> zijn metalen; "
                  "<strong>S (zwavel)</strong> is een niet-metaal en <strong>Ne (neon)</strong> een "
                  "edelgas."),
        ]),
        dict(kop="Een formule lezen", blokken=[
            ("p", "De <strong>coëfficiënt</strong> staat <strong>vooraan</strong> en zegt "
                  "<strong>hoeveel deeltjes van die stof er zijn</strong>. In 3 H₂SO₄ is "
                  "<strong>3 de coëfficiënt</strong>."),
            ("p", "De <strong>index</strong> staat <strong>rechts onderaan bij een symbool</strong> en "
                  "zegt <strong>hoeveel atomen van dat element in één deeltje zitten</strong>. De "
                  "<strong>4 achter de O in H₂SO₄</strong> betekent dus dat er "
                  "<strong>vier zuurstofatomen in de molecule</strong> zitten."),
            ("p", "In <strong>één molecule H₂SO₄</strong> zitten <strong>zeven atomen</strong>: twee "
                  "waterstof, één zwavel en vier zuurstof."),
            ("p", "In <strong>2 Ca(NO₃)₂</strong> komen <strong>drie verschillende atoomsoorten</strong> "
                  "voor: calcium, stikstof en zuurstof. De coëfficiënt en de indexen veranderen het "
                  "aantal soorten niet."),
            ("p", "Een <strong>coëfficiënt geldt voor het hele deeltje</strong>. <strong>2 H₂O zijn twee "
                  "watermoleculen</strong>, dus vier waterstof- en twee zuurstofatomen; het betekent niet "
                  "dat er twee zuurstofatomen in één molecule zitten. In <strong>3 H₂O</strong> zitten "
                  "dus <strong>zes waterstofatomen</strong> in totaal."),
        ]),
        dict(kop="Enkelvoudig of samengesteld", blokken=[
            ("p", "Een <strong>enkelvoudige stof bevat maar één element</strong>: O₂ bestaat enkel uit "
                  "zuurstof, Fe enkel uit ijzer. Een <strong>samengestelde stof bestaat uit meerdere "
                  "verschillende elementen</strong>, zoals H₂O of NaCl."),
            ("p", "<strong>O₃ is een enkelvoudige stof</strong>, ook al staan er drie atomen in: "
                  "<strong>alle atomen horen bij hetzelfde element</strong>. Enkelvoudig of samengesteld "
                  "hangt dus af van het aantal verschillende elementen, niet van het aantal atomen."),
            ("p", "Bij een <strong>synthese ontstaat uit meerdere stoffen één nieuwe stof</strong>. Bij "
                  "een <strong>analyse valt een stof uiteen in haar bestanddelen</strong>. Het zijn dus "
                  "geen twee namen voor hetzelfde."),
            ("p", "De schrijfwijze <strong>NaCl voor keukenzout heet een formule-eenheid</strong>: bij "
                  "een ionverbinding bestaan er geen losse moleculen, dus geeft de formule enkel de "
                  "kleinste verhouding. Bij een molecule spreekt men van een "
                  "<strong>brutoformule</strong>."),
        ]),
        dict(kop="Metalen, niet-metalen en edelgassen", blokken=[
            ("p", "<strong>Metalen</strong>: ze <strong>geleiden elektriciteit en warmte goed</strong>, "
                  "ze zijn <strong>vervormbaar</strong> en ze hebben <strong>glans</strong>. "
                  "<strong>Op kwik na zijn ze bij kamertemperatuur vast</strong>; kwik is vloeibaar."),
            ("p", "<strong>Vervormbaarheid</strong> is de eigenschap van een metaal om <strong>zich te "
                  "laten pletten en buigen zonder te breken</strong>. Dat kan doordat de elektronen vrij "
                  "bewegen, zodat de atomen langs elkaar schuiven zonder dat de binding breekt."),
            ("p", "<strong>Niet-metalen geleiden elektriciteit over het algemeen slecht</strong>, want "
                  "hun elektronen zitten vast in bindingen. Grafiet is de bekende uitzondering."),
            ("p", "<strong>Edelgassen zijn inert</strong>: ze gaan bijna geen reacties aan, want hun "
                  "buitenste schil is volledig gevuld. <strong>He en Ar</strong> zijn edelgassen; "
                  "<strong>N₂ en Cl₂ zijn niet-metalen</strong>."),
            ("p", "De fiche vraagt twee kleuren: <strong>chloorgas is geelgroen</strong>, met een scherpe "
                  "geur, en <strong>zuiver koper is roodbruin</strong> en glanzend, terwijl de meeste "
                  "andere metalen zilvergrijs zijn."),
        ]),
        dict(kop="Triviale namen en toepassingen", blokken=[
            ("p", tabel(["Triviale naam", "Formule", "Toepassing"], [
                ["zuurstofgas", "O₂", "ademlucht, zuurstofmasker, verbranding"],
                ["ozon", "O₃", "beschermt hoog in de atmosfeer tegen uv-straling"],
                ["waterstofgas", "H₂", "brandstof: bij verbranding ontstaat enkel water"],
                ["stikstofgas", "N₂", "bijna vier vijfde van de lucht"],
                ["chloorgas", "Cl₂", "desinfecteren van water"],
                ["grafiet", "C", "potloodstift, elektrode (geleidt)"],
                ["diamant", "C", "boor- en zaagwerktuigen (hardste natuurlijke stof)"],
                ["helium", "He", "ballonnen: licht en niet brandbaar"],
                ["neon", "Ne", "lichtreclame: oranjerood licht"],
            ])),
            ("p", "<strong>Zuurstofgas bestaat uit moleculen van twee zuurstofatomen</strong> (O₂). "
                  "<strong>Ozon</strong> heeft er <strong>drie per molecule</strong> (O₃). "
                  "<strong>Ozon en zuurstofgas zijn niet dezelfde stof</strong>, ook al bestaan ze uit "
                  "hetzelfde element: ozon ruikt scherp en is giftig om in te ademen."),
            ("p", "<strong>De triviale naam van N₂ is stikstofgas</strong>; de IUPAC-naam is distikstof. "
                  "<strong>Waterstofgas</strong> bestaat uit moleculen van twee waterstofatomen, dus "
                  "<strong>H₂</strong>, met als IUPAC-naam diwaterstof."),
            ("p", "<strong>Waterstofgas als brandstof</strong>: bij de verbranding met zuurstof "
                  "<strong>ontstaat enkel water</strong>, dus geen koolstofdioxide. Het gas is wel heel "
                  "brandbaar en vraagt dus voorzichtigheid."),
            ("p", "<strong>Helium in een weerballon</strong> wordt gebruikt omdat het "
                  "<strong>licht is en niet reageert</strong>: als edelgas is het inert en dus niet "
                  "brandbaar. <strong>Neon</strong> gebruikt men vooral voor "
                  "<strong>lichtreclame</strong>, want het geeft in een buis onder spanning een "
                  "oranjerood licht."),
            ("p", "<strong>Grafiet en diamant bestaan allebei uit koolstof</strong>, maar de "
                  "<strong>atomen liggen anders geschikt</strong>. In <strong>diamant</strong> zit elk "
                  "koolstofatoom aan vier andere vast in een stevig ruimtelijk rooster: daarom is het de "
                  "hardste natuurlijke stof en gebruikt men het in <strong>boor- en "
                  "zaagwerktuigen</strong>. In <strong>grafiet</strong> liggen de atomen in "
                  "<strong>lagen die over elkaar schuiven</strong>, en net daarom laat een "
                  "<strong>potloodstift</strong> een streep na op papier."),
            ("p", "<strong>Grafiet geleidt elektriciteit en diamant niet</strong>: in grafiet hoort elk "
                  "koolstofatoom maar aan drie andere vast, dus <strong>kunnen de overblijvende "
                  "elektronen zich vrij bewegen</strong>. In diamant zit elk elektron vast in een binding."),
        ]),
    ],
    onthoud=[
        "Een elementsymbool begint met een hoofdletter; Fe is ijzer, Na natrium, K kalium, Ag zilver.",
        "Koolstof is C (Co is kobalt) en magnesium is Mg (Mn is mangaan).",
        "De coëfficiënt staat vooraan en geldt voor het hele deeltje; de index staat rechts onderaan bij één symbool.",
        "Enkelvoudig betekent één element, ook bij O₃; samengesteld betekent meerdere elementen.",
        "Synthese bouwt op, analyse valt uiteen.",
        "Metalen: glans, geleiding, vervormbaar, vast behalve kwik. Niet-metalen geleiden slecht, behalve grafiet.",
        "Edelgassen zijn inert; chloorgas is geelgroen en koper roodbruin.",
        "Helium voor ballonnen, neon voor lichtreclame, waterstof als brandstof met water als product.",
        "Diamant: ruimtelijk rooster, hard, isolator. Grafiet: lagen, zacht, geleidt.",
    ],
)

# ───────────────────── 3. Chemische reacties en energie
BUNDELS["chemische-reacties-en-energie-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische reacties en energie",
    onder="De wet van behoud van massa, een vergelijking kloppend maken, en exo- en endo-energetische reacties met hun energiediagram.",
    secties=[
        dict(kop="De wet van behoud van massa", blokken=[
            ("p", "De <strong>wet van behoud van massa</strong> zegt dat de <strong>totale massa tijdens "
                  "een reactie gelijk blijft</strong>. Bij een reactie <strong>worden atomen anders "
                  "geschikt, maar niet gemaakt of vernietigd</strong>: er verdwijnen geen atomen en er "
                  "ontstaan geen nieuwe elementen. Het <strong>aantal atomen van elk element blijft "
                  "gelijk</strong>, en er <strong>ontstaan nieuwe stoffen</strong>."),
            ("p", "In een <strong>reactievergelijking</strong> staan de stoffen van een reactie met hun "
                  "coëfficiënten. De stoffen <strong>links van de pijl</strong> zijn de <strong>reagentia</strong>, de "
                  "stoffen <strong>rechts van de pijl</strong> de <strong>reactieproducten</strong>. Men "
                  "schrijft een <strong>pijl en geen gelijkheidsteken</strong> omdat de pijl "
                  "<strong>de richting van de omzetting aangeeft</strong>; het aantal atomen is wel links "
                  "en rechts gelijk."),
            ("p", "Rekenen met de wet: <strong>tien gram ijzer met vier gram zwavel geeft veertien gram "
                  "ijzersulfide</strong>, en <strong>vijftien gram koper met vier gram zuurstofgas geeft "
                  "negentien gram koperoxide</strong>. Je telt dus gewoon de beginmassa's op."),
            ("p", "Een <strong>kaars die opbrandt</strong> laat de kandelaar lichter achter, en dat is "
                  "<strong>geen uitzondering</strong>: de <strong>gassen zijn weggegaan in de "
                  "lucht</strong>, namelijk koolstofdioxide en waterdamp. <strong>In een gesloten vat "
                  "blijft de massa tijdens een verbranding gelijk</strong>, want de gassen kunnen er niet "
                  "uit. Als er een gas ontstaat, <strong>verdwijnt er dus geen massa</strong>."),
            ("p", "Dat er echt een reactie gebeurd is en niet enkel een vermenging, merk je doordat "
                  "<strong>er een neerslag ontstaat</strong> of <strong>er een gas vrijkomt</strong>: dat "
                  "zijn nieuwe stoffen. Zand dat een vloeistof troebel maakt, blijft gewoon zand."),
        ]),
        dict(kop="Een vergelijking kloppend maken", blokken=[
            ("p", "Je mag <strong>enkel de coëfficiënten aanpassen</strong>, nooit een "
                  "<strong>index</strong>: een index aanpassen maakt er een andere stof van, want H₂O₂ is "
                  "waterstofperoxide en niet meer water. Je mag ook geen stof bijschrijven die er niet in "
                  "staat. En de <strong>coëfficiënt 1 schrijf je niet op</strong>: staat er niets voor "
                  "een formule, dan is ze toch 1."),
            ("p", tabel(["Vergelijking", "Coëfficiënten"], [
                ["H₂ + O₂ → H₂O", "2, 1 en 2"],
                ["Fe + O₂ → Fe₂O₃", "4, 3 en 2"],
                ["CH₄ + O₂ → CO₂ + H₂O", "1, 2, 1 en 2"],
                ["C₂H₆ + O₂ → CO₂ + H₂O", "2, 7, 4 en 6"],
            ])),
            ("p", "<strong>2 H₂ + O₂ → 2 H₂O</strong>: links vier waterstof- en twee zuurstofatomen, "
                  "rechts precies hetzelfde. Hoort er rechts <strong>2 H₂O</strong>, dan is de "
                  "<strong>coëfficiënt voor O₂ gelijk aan 1</strong>."),
            ("p", "<strong>4 Fe + 3 O₂ → 2 Fe₂O₃</strong>: rechts staan vier ijzeratomen en zes "
                  "zuurstofatomen, dus links 4 Fe en 3 O₂."),
            ("p", "<strong>CH₄ + 2 O₂ → CO₂ + 2 H₂O</strong>: één CH₄ geeft één CO₂ en twee H₂O, dus "
                  "rechts vier zuurstofatomen en links twee O₂."),
        ]),
        dict(kop="Exo- en endo-energetische reacties", blokken=[
            ("p", "Bij een <strong>exo-energetische reactie komt energie vrij</strong>. Exo betekent naar "
                  "buiten: de reactieproducten hebben minder inwendige energie dan de reagentia, en het "
                  "verschil gaat naar de omgeving."),
            ("p", "Bij een <strong>endo-energetische reactie wordt energie opgenomen</strong> uit de "
                  "omgeving. De stoffen hebben energie nodig en halen die uit hun omgeving."),
            ("p", "<strong>Exo</strong>: het <strong>verbranden van aardgas</strong>, een "
                  "<strong>handwarmer die warm wordt</strong>, en <strong>elke verbranding</strong>. "
                  "<strong>Endo</strong>: een <strong>koudepakje dat koud wordt</strong>, het "
                  "<strong>ontleden van water met elektriciteit</strong>, en de "
                  "<strong>fotosynthese</strong>, waarvoor de plant lichtenergie nodig heeft."),
            ("p", "Stijgt de temperatuur van een oplossing <strong>van 20 naar 34 graden</strong> tijdens "
                  "een reactie, dan komt er energie vrij: de reactie is <strong>exo-energetisch</strong>. "
                  "Voelt de beker <strong>koud</strong> aan, dan haalt de reactie warmte uit de beker en "
                  "uit je hand: dan is ze <strong>endo-energetisch</strong>, niet exo."),
        ]),
        dict(kop="Het energiediagram", blokken=[
            ("p", "Op de <strong>verticale as</strong> van een energiediagram staat de "
                  "<strong>inwendige energie</strong> van de stoffen, horizontaal het verloop van de "
                  "reactie."),
            ("p", "Bij een <strong>exo-energetische reactie liggen de reactieproducten lager dan de "
                  "reagentia</strong>. Bij een <strong>endo-energetische reactie liggen ze hoger</strong>. "
                  "<strong>Aan het energiediagram kan je dus zien of een reactie energie opneemt of "
                  "afstaat.</strong>"),
            ("p", "De <strong>reactie-energie</strong> is het <strong>verschil in energie tussen de "
                  "reagentia en de reactieproducten</strong>, dus de hoeveelheid die opgenomen of "
                  "afgestaan wordt. Je leest ze af als het hoogteverschil in het diagram."),
        ]),
        dict(kop="Energievormen en omzettingen", blokken=[
            ("p", "<strong>Chemische energie</strong> zit <strong>opgeslagen in de bindingen van een "
                  "stof</strong>. De andere vormen die je hier nodig hebt, zijn <strong>thermische "
                  "energie</strong> (warmte), <strong>lichtenergie</strong> en <strong>elektrische "
                  "energie</strong>."),
            ("p", tabel(["Wat gebeurt er", "Omzetting"], [
                ["een kaars brandt", "chemisch naar thermisch en licht"],
                ["water ontleden met een batterij", "elektrisch naar chemisch"],
                ["een batterij doet een lampje branden", "chemisch naar elektrisch"],
                ["een plant doet fotosynthese", "licht naar chemisch"],
            ])),
            ("p", "Bij het <strong>branden van een kaars</strong> komen <strong>thermische energie en "
                  "lichtenergie</strong> vrij; elektriciteit komt er niet aan te pas. Een "
                  "<strong>gloeiende houtskool</strong> geeft naast licht vooral <strong>warmte</strong> "
                  "af."),
            ("p", "<strong>Water ontleden met een batterij</strong> in waterstofgas en zuurstofgas is "
                  "<strong>elektrische energie die chemische energie wordt</strong>: de batterij levert de "
                  "energie om de bindingen te verbreken. In een <strong>batterij die een lampje doet "
                  "branden</strong> gaat het net de andere kant op."),
            ("p", "Bij de <strong>fotosynthese</strong> zet een plant <strong>lichtenergie om in "
                  "chemische energie</strong>: ze vangt met haar bladgroen het licht op en gebruikt die "
                  "energie om glucose te vormen."),
            ("weetje", "Een energiediagram zegt niets over de snelheid van een reactie. Het "
                       "hoogteverschil zegt enkel hoeveel energie er in totaal vrijkomt of nodig is. "
                       "Ijzer dat roest is ook exo-energetisch, maar het duurt jaren."),
        ]),
    ],
    onthoud=[
        "Wet van behoud van massa: atomen worden anders geschikt, niet gemaakt of vernietigd.",
        "Reagentia staan links van de pijl, reactieproducten rechts.",
        "Bij het kloppend maken pas je enkel coëfficiënten aan, nooit een index.",
        "Een kaars lijkt massa te verliezen omdat de gassen wegwaaien; in een gesloten vat blijft de massa gelijk.",
        "Exo geeft energie af en de producten liggen lager; endo neemt energie op en ze liggen hoger.",
        "Op de verticale as van een energiediagram staat de inwendige energie.",
        "De reactie-energie is het hoogteverschil tussen reagentia en producten.",
        "Verbranden is exo; een koudepakje, water ontleden en fotosynthese zijn endo.",
        "Chemische energie zit in de bindingen; een batterij maakt er elektrische energie van.",
    ],
)

# ───────────────────── 4. De bouw van atomen en ionen
BUNDELS["de-bouw-van-atomen-en-ionen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De bouw van atomen en ionen",
    onder="De elementaire deeltjes, het atoomnummer en het massagetal, ionen, de relatieve en absolute massa en de elektronenconfiguratie volgens Bohr.",
    secties=[
        dict(kop="De elementaire deeltjes", blokken=[
            ("p", tabel(["Deeltje", "Waar", "Eenheidslading", "Massa"], [
                ["proton", "in de kern", "+1", "ongeveer 1 u"],
                ["neutron", "in de kern", "0", "ongeveer 1 u"],
                ["elektron", "rond de kern", "−1", "verwaarloosbaar"],
            ])),
            ("p", "In de <strong>atoomkern zitten de protonen en de neutronen</strong>, samen de "
                  "<strong>nucleonen</strong>. De <strong>elektronen bewegen eromheen</strong>."),
            ("p", "Een <strong>proton is positief</strong>, een <strong>elektron negatief</strong> en een "
                  "<strong>neutron heeft geen lading</strong>. Het <strong>neutron zit in de kern</strong>, "
                  "draait dus niet rond de kern, en het weegt ongeveer hetzelfde als een proton, dus veel "
                  "meer dan een elektron."),
            ("p", "De <strong>massa van een elektron is niet gelijk aan die van een proton</strong>: een "
                  "elektron is bijna tweeduizend keer lichter. Daarom zit <strong>vrijwel de hele massa "
                  "van een atoom in de kern</strong>. En <strong>het grootste deel van een atoom is lege "
                  "ruimte</strong>, want de kern is heel klein tegenover het hele atoom."),
        ]),
        dict(kop="Atoomnummer, massagetal en ionen", blokken=[
            ("p", "Het <strong>atoomnummer Z is het aantal protonen in de kern</strong>. Het "
                  "<strong>bepaalt om welk element het gaat</strong>: verander je het aantal protonen, dan "
                  "heb je een ander element."),
            ("p", "Het <strong>massagetal A is het aantal protonen en neutronen samen</strong>, dus het "
                  "aantal nucleonen. De elektronen tellen niet mee, want hun massa is verwaarloosbaar."),
            ("p", "<strong>Aantal neutronen = massagetal − atoomnummer.</strong> Bij atoomnummer 17 en "
                  "massagetal 35 zijn dat <strong>achttien neutronen</strong>; bij atoomnummer 26 en "
                  "massagetal 56 zijn het <strong>dertig neutronen</strong>."),
            ("p", "In een <strong>neutraal atoom is het aantal elektronen gelijk aan het aantal "
                  "protonen</strong>, dus gelijk aan het <strong>atoomnummer</strong>. Het aantal "
                  "neutronen staat daar los van, en het massagetal geeft niet het aantal elektronen."),
            ("p", "Een <strong>ion is een atoom dat elektronen heeft opgenomen of afgegeven</strong>. "
                  "<strong>Alleen elektronen bewegen</strong>: een positief ion ontstaat niet doordat een "
                  "atoom protonen afgeeft, maar doordat het <strong>elektronen afgeeft</strong>, zodat er "
                  "meer protonen overblijven."),
            ("p", tabel(["Deeltje", "Protonen", "Elektronen", "Besluit"], [
                ["elf protonen, tien elektronen", "11", "10", "een positief ion (Na¹⁺)"],
                ["Cl¹⁻ (Z = 17)", "17", "18", "één elektron meer dan protonen"],
                ["Mg²⁺ (Z = 12)", "12", "10", "twee elektronen minder"],
                ["O²⁻ (Z = 8)", "8", "10", "het aantal protonen blijft 8"],
            ])),
        ]),
        dict(kop="Relatieve en absolute massa", blokken=[
            ("p", "De <strong>relatieve atoommassa</strong> is de <strong>massa van het atoom vergeleken "
                  "met de eenheid u</strong>. Ze is een verhouding en <strong>heeft dus geen "
                  "eenheid</strong>; ze wordt niet in gram uitgedrukt. Je leest ze af in het periodiek "
                  "systeem, <strong>afgerond op 0,1</strong>."),
            ("p", "De <strong>atoommassa-eenheid u is 1,66.10⁻²⁷ kg</strong>. Dat getal staat in de "
                  "bijlage die je op het examen mag gebruiken; het is ongeveer de massa van één nucleon."),
            ("p", "De <strong>absolute massa</strong> bereken je door de relatieve massa <strong>met u te "
                  "vermenigvuldigen</strong>, niet erdoor te delen. Voor koolstof met Ar = 12,0: "
                  "<strong>12,0 × 1,66.10⁻²⁷ kg = 1,99.10⁻²⁶ kg</strong>. Voor helium met Ar = 4,0: "
                  "<strong>4,0 × 1,66.10⁻²⁷ kg = 6,64.10⁻²⁷ kg</strong>."),
        ]),
        dict(kop="De elektronenconfiguratie volgens Bohr", blokken=[
            ("p", "De <strong>elektronenconfiguratie volgens Bohr</strong> beschrijft <strong>hoe de "
                  "elektronen over de schillen verdeeld zijn</strong>. In het <strong>schillenmodel</strong> van Bohr liggen de "
                  "elektronen in <strong>schillen met elk een eigen energieniveau</strong>."),
            ("p", "De <strong>eerste schil bevat maximaal twee elektronen</strong>, de "
                  "<strong>tweede acht</strong> en bij de eerste achttien elementen ook de "
                  "<strong>derde tot acht</strong>. Je <strong>vult de schillen van binnen naar "
                  "buiten</strong>. De elektronen zitten niet mee in de kern."),
            ("p", tabel(["Element", "Z", "Configuratie"], [
                ["zuurstof", "8", "2, 6"],
                ["natrium", "11", "2, 8, 1"],
                ["chloor", "17", "2, 8, 7"],
                ["neon", "10", "2, 8"],
                ["argon", "18", "2, 8, 8"],
            ])),
            ("p", "De <strong>edelgasconfiguratie</strong> is een <strong>volledig gevulde buitenste "
                  "schil</strong>. Die toestand is bijzonder stabiel, dus nemen atomen elektronen op of "
                  "geven ze af om ze te bereiken. <strong>Helium en argon</strong> hebben een volle "
                  "buitenste schil; natrium heeft er één te veel en chloor één te weinig."),
            ("p", "<strong>Een natriumatoom geeft liever één elektron af dan er zeven op te "
                  "nemen</strong>, want <strong>met één minder heeft het al een volle buitenste "
                  "schil</strong>: van 2, 8, 1 blijft 2, 8 over, de configuratie van neon."),
            ("p", "In het <strong>elektron-stipmodel</strong> tekent men <strong>stippen rond het symbool "
                  "voor de buitenste elektronen</strong>. Zo zie je meteen hoeveel valentie-elektronen een "
                  "atoom heeft. Het <strong>aantal elektronen in de buitenste schil bepaalt mee de "
                  "eigenschappen</strong> van een element: net die elektronen doen mee aan de bindingen."),
        ]),
    ],
    onthoud=[
        "Protonen en neutronen zitten in de kern en heten nucleonen; elektronen bewegen eromheen.",
        "Proton +1, elektron −1, neutron 0; een elektron is bijna tweeduizend keer lichter dan een proton.",
        "Atoomnummer Z is het aantal protonen; massagetal A is protonen plus neutronen.",
        "Aantal neutronen is A min Z; in een neutraal atoom is het aantal elektronen gelijk aan Z.",
        "Een ion ontstaat door elektronen op te nemen of af te geven; protonen bewegen nooit.",
        "De relatieve atoommassa heeft geen eenheid; de absolute massa is Ar maal u, met u = 1,66.10⁻²⁷ kg.",
        "Schillen vullen van binnen naar buiten: eerste twee, tweede acht, derde acht.",
        "Natrium is 2, 8, 1 en chloor 2, 8, 7; een volle buitenste schil is de edelgasconfiguratie.",
        "In het stipmodel staan de valentie-elektronen als stippen rond het symbool.",
    ],
)

# ───────────────────── 5. Het periodiek systeem der elementen
BUNDELS["het-periodiek-systeem-der-elementen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het periodiek systeem der elementen",
    onder="Groepen en perioden, de valentie-elektronen, de namen van de hoofdgroepen, het vormen van ionen en de elektronegativiteit.",
    secties=[
        dict(kop="Groepen en perioden", blokken=[
            ("p", "Een <strong>verticale kolom</strong> in het periodiek systeem heet een "
                  "<strong>groep</strong>, een <strong>horizontale rij</strong> een "
                  "<strong>periode</strong>."),
            ("p", "Elementen uit <strong>dezelfde hoofdgroep hebben hetzelfde aantal "
                  "valentie-elektronen</strong>, en daarom <strong>gelijkaardige chemische "
                  "eigenschappen</strong>. Bij een hoofdgroep is het <strong>groepsnummer in Romeinse "
                  "cijfers gelijk aan het aantal elektronen in de buitenste schil</strong>: groep VIA "
                  "heeft er zes, groep IIA twee."),
            ("p", "Het <strong>periodenummer is gelijk aan het aantal bezette schillen</strong>. Een "
                  "element uit <strong>periode 4 heeft dus vier bezette schillen</strong>."),
            ("p", "Het <strong>atoomnummer stijgt van links naar rechts in een periode</strong>, want de "
                  "elementen staan op volgorde van hun aantal protonen. Het <strong>aantal elementen per "
                  "periode is niet overal hetzelfde</strong>: de eerste heeft er twee, de tweede en de "
                  "derde acht, en daarna worden de perioden langer."),
            ("p", "<strong>Zwavel staat in groep VIA en periode 3</strong>: drie bezette schillen en zes "
                  "valentie-elektronen, dus de configuratie 2, 8, 6. En omgekeerd: een element met de "
                  "configuratie <strong>2, 8, 3 staat in groep IIIA, periode 3</strong>, en dat is "
                  "aluminium."),
        ]),
        dict(kop="De namen van de hoofdgroepen", blokken=[
            ("p", tabel(["Groep", "Naam", "Valentie-elektronen", "Voorbeelden"], [
                ["IA", "alkalimetalen (zonder waterstof)", "1", "Li, Na, K"],
                ["IIA", "aardalkalimetalen", "2", "Mg, Ca, Ba"],
                ["VIIA", "halogenen", "7", "F, Cl, Br, I"],
                ["VIIIA", "edelgassen", "volle schil", "He, Ne, Ar"],
            ])),
            ("p", "De <strong>alkalimetalen</strong> hebben <strong>één valentie-elektron</strong> en "
                  "reageren daarom heftig met water. <strong>Waterstof staat bovenaan in de kolom van "
                  "groep IA</strong>, helemaal linksboven, maar het is geen alkalimetaal en het staat "
                  "zeker niet bij de edelgassen."),
            ("p", "De <strong>aardalkalimetalen zijn groep IIA</strong>: <strong>magnesium en "
                  "calcium</strong> horen erbij, natrium (IA) en chloor (VIIA) niet."),
            ("p", "<strong>Halogeen betekent zoutvormer</strong>: <strong>fluor, chloor, broom en "
                  "jood</strong> vormen met een metaal een zout, zoals natriumchloride."),
            ("p", "De <strong>edelgassen staan in de laatste groep</strong> en hun <strong>buitenste "
                  "schil is volledig gevuld</strong>. Daarom <strong>vormen ze geen ionen</strong> en zijn "
                  "ze <strong>geen metalen</strong>."),
        ]),
        dict(kop="Ionen vormen uit de plaats in het systeem", blokken=[
            ("p", tabel(["Groep", "Elektronen op of af", "Lading van het ion"], [
                ["IA", "één elektron af", "1+"],
                ["IIA", "twee elektronen af", "2+"],
                ["IIIA", "drie elektronen af", "3+"],
                ["VA", "drie elektronen op", "3−"],
                ["VIA", "twee elektronen op", "2−"],
                ["VIIA", "één elektron op", "1−"],
            ])),
            ("p", "Een atoom uit <strong>groep IA geeft één elektron af</strong>, want dan houdt het de "
                  "configuratie van het edelgas ervoor. Een atoom uit <strong>groep IIA geeft er twee "
                  "af</strong> en krijgt lading <strong>2+</strong>; <strong>aluminium uit groep IIIA "
                  "geeft er drie af</strong> en wordt <strong>Al³⁺</strong>."),
            ("p", "Een atoom uit <strong>groep VIIA neemt één elektron op</strong> en krijgt lading "
                  "<strong>1−</strong>. <strong>Zuurstof neemt twee elektronen op</strong>, want het staat "
                  "in groep VIA met zes valentie-elektronen: <strong>dan heeft het een volle buitenste "
                  "schil</strong>. De elementen van <strong>groep VIA vormen dus O²⁻ en S²⁻</strong>; een "
                  "atoom uit <strong>groep VA neemt drie elektronen op</strong>."),
            ("p", "Een <strong>ion met tien elektronen en lading 1+</strong> heeft één elektron afgegeven, "
                  "dus had het atoom er elf: dat is <strong>natrium, groep IA</strong>. Het ion "
                  "<strong>Na¹⁺ heeft dezelfde elektronenconfiguratie als neon</strong>."),
        ]),
        dict(kop="Elektronegativiteit en metaalkarakter", blokken=[
            ("p", "De <strong>elektronegativiteit</strong> zegt <strong>hoe sterk een element elektronen "
                  "naar zich toe trekt</strong> in een binding."),
            ("p", "Ze <strong>stijgt van links naar rechts in een periode</strong>, want naar rechts komen "
                  "er protonen bij terwijl het aantal schillen gelijk blijft. Ze <strong>daalt als je in "
                  "een groep naar onder gaat</strong>, want de buitenste schil komt verder van de kern. "
                  "De <strong>hoogste waarden staan dus rechtsboven</strong>, en "
                  "<strong>fluor</strong> en <strong>zuurstof</strong> staan daar."),
            ("p", "Een <strong>lage elektronegativiteit hoort bij een metaal</strong>: een metaal houdt "
                  "zijn valentie-elektronen maar los vast en geeft ze liever af."),
            ("p", "De <strong>metalen staan links en in het midden</strong>, de <strong>niet-metalen "
                  "rechtsboven</strong>. Een atoom <strong>links</strong> in het systeem "
                  "<strong>geeft makkelijk elektronen af</strong>, heeft een "
                  "<strong>metaalkarakter</strong> en <strong>vormt een positief ion</strong>. Een "
                  "<strong>niet-metaal neemt eerder elektronen op</strong>, want het heeft veel "
                  "valentie-elektronen en een hoge elektronegativiteit."),
        ]),
    ],
    onthoud=[
        "Een groep is een kolom, een periode een rij; het periodenummer geeft het aantal bezette schillen.",
        "Bij een hoofdgroep geeft het groepsnummer het aantal valentie-elektronen.",
        "IA alkalimetalen, IIA aardalkalimetalen, VIIA halogenen, VIIIA edelgassen.",
        "Waterstof staat bij groep IA maar is geen alkalimetaal.",
        "Groep IA geeft 1 elektron af, IIA 2, IIIA 3; VIIA neemt 1 op, VIA 2, VA 3.",
        "Na¹⁺ heeft de configuratie van neon; edelgassen vormen zelf geen ionen.",
        "Elektronegativiteit stijgt naar rechts en daalt naar onder; fluor heeft de hoogste.",
        "Een lage elektronegativiteit hoort bij een metaal, dat elektronen afgeeft.",
        "Metalen staan links en in het midden, niet-metalen rechtsboven.",
    ],
)

# ───────────────────── 6. Chemische bindingen en roosters
BUNDELS["chemische-bindingen-en-roosters-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische bindingen en roosters",
    onder="De drie bindingstypes, de Lewisstructuur met haar elektronenparen, de vier roostertypes en de eigenschappen die eruit volgen.",
    secties=[
        dict(kop="Het bindingstype bepalen", blokken=[
            ("p", "Het <strong>bindingstype kan je voorspellen uit het metaal- en niet-metaalkarakter van "
                  "de elementen</strong>."),
            ("p", tabel(["Combinatie", "Bindingstype", "Wat gebeurt er"], [
                ["metaal + niet-metaal", "ionbinding", "elektronen gaan over, er ontstaan ionen"],
                ["niet-metaal + niet-metaal", "atoombinding (covalent)", "de atomen delen elektronenparen"],
                ["metaal + metaal", "metaalbinding", "de valentie-elektronen bewegen vrij"],
            ])),
            ("p", "Bij een <strong>ionbinding worden elektronen overgedragen</strong> en "
                  "<strong>ontstaan er geladen deeltjes</strong>: het metaal geeft af, het niet-metaal "
                  "neemt op, en de ionen trekken elkaar aan. Er wordt dus niets gedeeld, en de binding komt "
                  "niet tussen metalen onderling voor. <strong>NaCl en MgO</strong> bevatten een "
                  "ionbinding; <strong>CO₂ en Cl₂</strong> niet."),
            ("p", "Bij een <strong>atoombinding delen twee atomen een of meer elektronenparen</strong>. Zo "
                  "komen ze beide aan een volle buitenste schil zonder elektronen af te geven. Een ander "
                  "woord ervoor is <strong>covalente binding</strong>."),
            ("p", "Een <strong>metaalbinding</strong> ontstaat <strong>tussen metaalatomen</strong>: de "
                  "<strong>valentie-elektronen bewegen vrij tussen de ionen</strong> en vormen een wolk die "
                  "de positieve ionen bij elkaar houdt. Metaal met niet-metaal geeft dus geen "
                  "metaalbinding."),
        ]),
        dict(kop="De Lewisstructuur", blokken=[
            ("p", "In een Lewisstructuur <strong>tekent men enkel de valentie-elektronen</strong>, niet de "
                  "elektronen uit de binnenste schillen, want enkel die doen mee aan de bindingen."),
            ("p", "Een <strong>bindend elektronenpaar</strong> is een <strong>paar dat door twee atomen "
                  "gedeeld wordt</strong>; het vormt de binding zelf en wordt vaak als een streepje "
                  "getekend. Een <strong>vrij elektronenpaar</strong> is een <strong>paar dat niet aan een "
                  "binding deelneemt</strong> en bij één atoom alleen blijft."),
            ("p", tabel(["Stof", "Binding", "Gedeelde paren"], [
                ["H₂", "enkelvoudig", "1"],
                ["O₂", "dubbel", "2"],
                ["N₂", "drievoudig", "3"],
            ])),
            ("p", "Een <strong>dubbele binding bestaat uit twee gedeelde elektronenparen</strong>, dus "
                  "vier elektronen, niet twee. In <strong>O₂ zitten twee bindende elektronenparen</strong>: "
                  "zuurstof heeft zes valentie-elektronen en heeft er twee nodig. Tussen de twee "
                  "stikstofatomen in <strong>N₂ zit een drievoudige binding</strong>, en die is heel sterk."),
            ("p", "Een <strong>koolstofatoom vormt gewoonlijk vier atoombindingen</strong>, want het heeft "
                  "vier valentie-elektronen en heeft er vier nodig. Een <strong>waterstofatoom vormt er "
                  "één</strong>."),
            ("p", "Het <strong>zuurstofatoom in een watermolecule heeft twee vrije "
                  "elektronenparen</strong>: van de zes valentie-elektronen gaan er twee in de bindingen "
                  "met waterstof, en de vier andere vormen twee vrije paren."),
            ("p", "Bij een ionverbinding geeft men de <strong>formule-eenheid</strong>, de "
                  "<strong>kleinste verhouding van de ionen</strong>, want er bestaan geen losse "
                  "moleculen. Magnesium met chloor geeft <strong>MgCl₂</strong>: magnesium geeft twee "
                  "elektronen af en chloor neemt er één op, dus zijn er twee chloride-ionen nodig."),
        ]),
        dict(kop="De vier roostertypes", blokken=[
            ("p", tabel(["Roostertype", "Voorbeeld", "Smeltpunt", "Geleidt"], [
                ["ionrooster", "NaCl, MgO", "hoog", "opgelost of gesmolten"],
                ["atoomrooster", "diamant", "heel hoog", "nee (grafiet wel)"],
                ["molecuulrooster", "vast CO₂", "laag", "nee"],
                ["metaalrooster", "ijzer, koper", "meestal hoog", "ja, ook als vaste stof"],
            ])),
            ("p", "<strong>Natriumchloride en magnesiumoxide hebben een ionrooster</strong>: positieve en "
                  "negatieve ionen liggen afwisselend in een regelmatig patroon. <strong>Diamant heeft een "
                  "atoomrooster</strong>, waarin alle koolstofatomen met atoombindingen aan elkaar zitten. "
                  "<strong>Ijzer heeft een metaalrooster</strong> en <strong>vast koolstofdioxide een "
                  "molecuulrooster</strong>, waarin de moleculen CO₂ blijven bestaan."),
            ("p", "Een <strong>ionrooster heeft een hoog smeltpunt</strong> omdat de <strong>aantrekking "
                  "tussen de ionen sterk is</strong>. Een <strong>atoomrooster heeft een heel hoog "
                  "smeltpunt</strong>, want je moet de atoombindingen van het hele rooster verbreken."),
            ("p", "Een <strong>molecuulrooster heeft vaak een laag smeltpunt</strong> omdat de "
                  "<strong>krachten tussen de moleculen zwak zijn</strong>, al zitten de moleculen zelf "
                  "stevig aan elkaar. Daarom gaat droogijs snel over in gas."),
        ]),
        dict(kop="Geleiden, breken en glanzen", blokken=[
            ("p", "Een <strong>metaal geleidt elektriciteit omdat de elektronen vrij kunnen "
                  "bewegen</strong>. Die vrije elektronen geven het metaal ook zijn "
                  "<strong>glans</strong>, want ze kaatsen het licht terug. <strong>Een molecuulrooster "
                  "geleidt niet</strong>, want daar zitten de elektronen vast in de bindingen."),
            ("p", "Een <strong>zout geleidt als het opgelost is in water of gesmolten</strong> is, want "
                  "dan kunnen de ionen bewegen. Een <strong>vast zout is een isolator</strong>: de ionen "
                  "zitten vast in het rooster."),
            ("p", "Een <strong>zoutkristal is breekbaar</strong>: schuift een laag ionen een plaatsje op, "
                  "dan <strong>komen gelijke ladingen naast elkaar</strong>, en die afstoting splijt het "
                  "kristal. Een <strong>metaal is wel vervormbaar</strong>, want de "
                  "<strong>elektronenwolk houdt de ionen samen bij verschuiving</strong>."),
            ("p", "<strong>Grafiet is zacht en diamant hard</strong>, al bestaan beide uit koolstof: in "
                  "<strong>grafiet liggen de atomen in lagen die over elkaar schuiven</strong>. Binnen een "
                  "laag zijn de bindingen sterk, maar tussen de lagen zijn de krachten zwak."),
        ]),
        dict(kop="Het oxidatiegetal", blokken=[
            ("p", "Het <strong>oxidatiegetal</strong> zegt welke lading een atoom zou hebben als je alle "
                  "bindingen als ionbindingen zou rekenen. Je noteert het met een Romeins cijfer en een "
                  "teken."),
            ("p", "In een <strong>enkelvoudige stof is het oxidatiegetal van het element nul</strong>, want "
                  "er is geen ander element dat de elektronen naar zich toe trekt. Dat geldt dus ook voor "
                  "O₂ en voor Fe."),
            ("p", "<strong>Zuurstof is in de meeste verbindingen −II</strong>; in peroxiden is het −I, dus "
                  "kijk altijd naar de formule. <strong>Waterstof in HCl is +I</strong>, want chloor is "
                  "het meest elektronegatieve van de twee en krijgt de elektronen toegewezen."),
            ("weetje", "De tabel met oxidatiegetallen in bijlage 2 mag je op het examen gebruiken. "
                       "Veel metalen hebben er meerdere: ijzer is +II of +III, koper +I of +II. Daarom "
                       "staat er in een naam zoals ijzer(III)chloride een Romeins cijfer."),
        ]),
    ],
    onthoud=[
        "Metaal met niet-metaal geeft een ionbinding, twee niet-metalen een atoombinding, twee metalen een metaalbinding.",
        "Bij een ionbinding gaan elektronen over; bij een atoombinding worden paren gedeeld.",
        "In een metaalbinding bewegen de valentie-elektronen vrij tussen de positieve ionen.",
        "Een bindend paar wordt gedeeld, een vrij paar niet; dubbel is twee paren, drievoudig drie.",
        "Koolstof vormt vier bindingen, waterstof één; zuurstof in water heeft twee vrije paren.",
        "Vier roosters: ion, atoom, molecuul en metaal, met elk hun eigen smeltpunt en geleiding.",
        "Een zout geleidt opgelost of gesmolten, nooit als vaste stof.",
        "Een zoutkristal breekt omdat gelijke ladingen naast elkaar komen; een metaal vervormt wel.",
        "In een enkelvoudige stof is het oxidatiegetal nul; zuurstof is meestal −II.",
    ],
)

# ───────────────────── 7. Anorganische stofklassen en naamgeving
BUNDELS["anorganische-stofklassen-en-naamgeving-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Anorganische stofklassen en naamgeving",
    onder="De vier anorganische stofklassen, binair en ternair, de zuurresten, de IUPAC-naamgeving met de triviale namen, en de reactiepatronen.",
    secties=[
        dict(kop="De vier stofklassen", blokken=[
            ("p", tabel(["Stofklasse", "Waaraan je ze herkent", "Voorbeeld"], [
                ["oxide", "een element met zuurstof alleen", "CaO, CO₂"],
                ["hydroxide", "de functionele groep OH bij een metaalion", "NaOH, Al(OH)₃"],
                ["zuur", "de formule begint met waterstof", "HCl, H₂SO₄"],
                ["zout", "een metaalion of ammonium met een zuurrest", "NaCl, CaCO₃"],
            ])),
            ("p", "Een <strong>oxide is een verbinding van een element met zuurstof</strong>. "
                  "<strong>CaO en CO₂ zijn oxiden</strong>; NaOH is een hydroxide en HCl een zuur."),
            ("p", "De <strong>functionele groep van een hydroxide is OH</strong>. In water geeft die groep "
                  "het <strong>hydroxide-ion OH⁻</strong> en maakt ze de oplossing basisch. "
                  "<strong>Al(OH)₃</strong> is een hydroxide, met de groep drie keer, want aluminium vormt "
                  "een ion met lading 3+."),
            ("p", "Bij een <strong>anorganisch zuur staan de waterstofatomen vooraan</strong> in de "
                  "formule, zoals in <strong>HCl en H₂SO₄</strong>. Die waterstof komt in water als H⁺ "
                  "vrij. <strong>H₂O hoort niet bij de zuren</strong>, al begint de formule met "
                  "waterstof: water is een oxide van waterstof en is neutraal."),
            ("p", "Een <strong>zout bestaat uit een positief en een negatief ion</strong>: meestal een "
                  "metaalion of het ammoniumion, en een zuurrest."),
            ("p", "Het <strong>ammoniumion NH₄¹⁺</strong> is een positief geladen groepje dat de plaats "
                  "van een metaalion inneemt. Ammoniumsulfaat wordt veel gebruikt als meststof."),
        ]),
        dict(kop="Binair en ternair", blokken=[
            ("p", "<strong>Binair betekent twee elementen, ternair drie.</strong> <strong>HCl is een "
                  "binair zuur</strong>, want het bevat waterstof en chloor. <strong>H₂SO₄ is "
                  "ternair</strong>: waterstof, zwavel en zuurstof. Ook HBr en H₂S zijn binair."),
            ("p", "Bij de zouten geldt hetzelfde. <strong>CaCO₃ is een ternair zout</strong>, want het "
                  "bevat calcium, koolstof en zuurstof; NaCl is binair. <strong>Niet elk zout bevat "
                  "zuurstof</strong>: alleen de ternaire zouten hebben zuurstof in de zuurrest."),
        ]),
        dict(kop="De zuurresten", blokken=[
            ("p", tabel(["Ion", "Naam", "Hoort bij"], [
                ["NO₃¹⁻", "nitraation", "salpeterzuur"],
                ["SO₄²⁻", "sulfaation", "zwavelzuur"],
                ["PO₄³⁻", "fosfaation", "fosforzuur"],
                ["CO₃²⁻", "carbonaation", "koolzuur"],
                ["ClO₃¹⁻", "chloraation", "chloorzuur"],
                ["BrO₃¹⁻", "bromaation", "broomzuur"],
                ["IO₃¹⁻", "jodaation", "joodzuur"],
                ["S²⁻", "sulfide-ion", "waterstofsulfide"],
                ["Cl¹⁻, Br¹⁻, I¹⁻, F¹⁻", "chloride-, bromide-, jodide-, fluoride-ion", "de binaire zuren"],
            ])),
            ("p", "Een <strong>zuurrest zonder zuurstof krijgt de uitgang -ide</strong>: het "
                  "<strong>chloride-ion Cl¹⁻</strong>, het <strong>sulfide-ion S²⁻</strong>, het "
                  "<strong>jodide-ion I¹⁻</strong>. Die horen bij een binair zuur. <strong>Carbonaat en "
                  "fosfaat bevatten wel zuurstof.</strong>"),
            ("p", "<strong>Nitraten zijn allemaal goed oplosbaar in water</strong>, dus gebruikt men ze "
                  "graag als men een bepaald ion in oplossing nodig heeft. <strong>Kalksteen is "
                  "calciumcarbonaat.</strong>"),
        ]),
        dict(kop="De naamgeving", blokken=[
            ("p", "Bij een <strong>atoomverbinding gebruikt men Griekse telwoorden</strong>: ze zeggen "
                  "hoeveel atomen er van elk element zijn. <strong>CO₂ is koolstofdioxide</strong> en "
                  "<strong>N₂O is distikstofoxide</strong>."),
            ("p", "Bij een <strong>ionverbinding gebruikt men geen Griekse telwoorden</strong> maar de "
                  "<strong>stocknotatie</strong>, met een Romeins cijfer tussen haakjes. Dat cijfer "
                  "<strong>geeft het oxidatiegetal van het metaal</strong>: ijzer kan +II of +III zijn, "
                  "dus zegt <strong>ijzer(III)chloride</strong> hoeveel chloride-ionen erbij horen. Heeft "
                  "een metaal maar één mogelijkheid, dan laat men het cijfer weg: "
                  "<strong>CaO is calciumoxide</strong>."),
            ("p", tabel(["Triviale naam", "Formule", "Stofklasse"], [
                ["water", "H₂O", "oxide"],
                ["zoutzuur", "HCl in water", "binair zuur"],
                ["ammoniak", "NH₃", "base in water"],
                ["salpeterzuur", "HNO₃", "ternair zuur"],
                ["zwavelzuur", "H₂SO₄", "ternair zuur"],
                ["fosforzuur", "H₃PO₄", "ternair zuur"],
                ["koolzuur", "H₂CO₃", "ternair zuur"],
                ["koolzuurgas", "CO₂", "oxide"],
                ["lachgas", "N₂O", "oxide"],
                ["ongebluste kalk", "CaO", "oxide"],
                ["gebluste kalk", "Ca(OH)₂", "hydroxide"],
                ["bijtende soda of loogoplossing", "NaOH", "hydroxide"],
                ["soda", "Na₂CO₃", "ternair zout"],
                ["bakpoeder", "NaHCO₃", "ternair zout"],
                ["keukenzout", "NaCl", "binair zout"],
            ])),
            ("p", "<strong>Zoutzuur</strong> is een oplossing van waterstofchloride in water: het zit in "
                  "ontkalkers en in je maag. <strong>Ammoniak NH₃</strong> is een gas met een scherpe "
                  "geur dat in water een basische oplossing geeft, en het zit in kuisproducten."),
            ("p", "<strong>Ongebluste kalk is CaO</strong> en <strong>gebluste kalk Ca(OH)₂</strong>: je "
                  "maakt gebluste kalk door water bij ongebluste kalk te doen, en het zit in mortel en in "
                  "kalkmelk voor de landbouw."),
            ("p", "<strong>Soda is Na₂CO₃</strong>, gebruikt om te kuisen en om glas te maken. "
                  "<strong>Bijtende soda is NaOH</strong>, en dat is iets anders. "
                  "<strong>NaHCO₃ is bakpoeder</strong>, natriumwaterstofcarbonaat, en dus niet bijtende "
                  "soda. Meng je <strong>bakpoeder met azijn</strong>, dan komt <strong>koolzuurgas "
                  "CO₂</strong> vrij: het zuur maakt koolzuur, en dat valt meteen uiteen in water en "
                  "koolstofdioxide."),
            ("p", "<strong>Methaan is geen anorganische stof</strong> maar een alkaan, dus organisch. Het "
                  "is het hoofdbestanddeel van aardgas."),
        ]),
        dict(kop="De drie reactiepatronen", blokken=[
            ("p", tabel(["Patroon", "Wat ontstaat er"], [
                ["metaal of niet-metaal + dizuurstof", "een metaaloxide of een niet-metaaloxide"],
                ["metaaloxide + water", "een hydroxide (basevormend)"],
                ["niet-metaaloxide + water", "een zuur (zuurvormend)"],
                ["zuur + hydroxide", "een zout en water"],
            ])),
            ("p", "Een <strong>metaaloxide is basevormend</strong>: met water geeft het een "
                  "<strong>hydroxide</strong>, zoals CaO dat Ca(OH)₂ wordt. Een "
                  "<strong>niet-metaaloxide is zuurvormend</strong>: met water geeft het een "
                  "<strong>zuur</strong>, zoals CO₂ dat koolzuur wordt. SO₂ in de lucht draagt zo bij aan "
                  "zure regen."),
            ("p", "Reageert een <strong>zuur met een hydroxide</strong>, dan ontstaan "
                  "<strong>een zout en water</strong>: het metaalion en de zuurrest vormen het zout, en de "
                  "H⁺ en de OH⁻ vormen water."),
        ]),
    ],
    onthoud=[
        "Oxide is een element met zuurstof, hydroxide heeft OH, een zuur begint met waterstof, een zout heeft een metaalion en een zuurrest.",
        "Binair is twee elementen, ternair drie; NaCl is binair, CaCO₃ ternair.",
        "Zuurresten met zuurstof: nitraat, sulfaat, fosfaat, carbonaat. Zonder zuurstof krijgen ze -ide.",
        "Atoomverbinding: Griekse telwoorden (koolstofdioxide). Ionverbinding: stocknotatie met een Romeins cijfer.",
        "Ongebluste kalk CaO, gebluste kalk Ca(OH)₂, bijtende soda NaOH, soda Na₂CO₃, bakpoeder NaHCO₃.",
        "Zoutzuur is HCl in water, salpeterzuur HNO₃, zwavelzuur H₂SO₄, lachgas N₂O.",
        "Een metaaloxide is basevormend, een niet-metaaloxide zuurvormend.",
        "Zuur plus hydroxide geeft een zout en water.",
        "Water hoort bij de oxiden, niet bij de zuren; methaan is organisch.",
    ],
)

# ───────────────────── 8. Organische stoffen en de alkanen
BUNDELS["organische-stoffen-en-de-alkanen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Organische stoffen en de alkanen",
    onder="De tien laagste n-alkanen met hun formule, de vijf organische stofklassen, en de triviale namen en toepassingen.",
    secties=[
        dict(kop="De alkanen", blokken=[
            ("p", "<strong>Organische stoffen zijn verbindingen waarin koolstof de hoofdrol speelt</strong>: "
                  "de koolstofketen is het geraamte. Koolstofdioxide en de carbonaten zijn de klassieke "
                  "uitzonderingen, die rekent men bij de anorganische stoffen."),
            ("p", "Een <strong>alkaan bestaat enkel uit koolstof en waterstof, met enkelvoudige "
                  "bindingen</strong>. Ze zijn verzadigd, en daarom horen ze bij de koolwaterstoffen. "
                  "Komt er zuurstof bij, dan gaat het om een andere stofklasse."),
            ("p", "De <strong>algemene formule van de n-alkanen is CnH2n+2</strong>: elke extra koolstof "
                  "brengt twee waterstofatomen mee, en aan de twee uiteinden komt er telkens één bij. Alle "
                  "<strong>alkanen hebben de uitgang -aan</strong>."),
            ("p", tabel(["Naam", "Formule", "Naam", "Formule"], [
                ["methaan", "CH₄", "hexaan", "C₆H₁₄"],
                ["ethaan", "C₂H₆", "heptaan", "C₇H₁₆"],
                ["propaan", "C₃H₈", "octaan", "C₈H₁₈"],
                ["butaan", "C₄H₁₀", "nonaan", "C₉H₂₀"],
                ["pentaan", "C₅H₁₂", "decaan", "C₁₀H₂₂"],
            ])),
            ("p", "<strong>Methaan is CH₄</strong>, want koolstof vormt vier bindingen. "
                  "<strong>Ethaan is C₂H₆ en niet C₂H₄</strong>: C₂H₄ is etheen, met een dubbele binding. "
                  "<strong>Hexaan heeft zes koolstofatomen</strong>, <strong>C₅H₁₂ is pentaan</strong>, "
                  "<strong>C₇H₁₆ is heptaan</strong> en het <strong>alkaan met negen koolstofatomen heeft "
                  "twintig waterstofatomen</strong>."),
            ("p", "Bij de <strong>volledige verbranding van een alkaan ontstaan koolstofdioxide en "
                  "water</strong>. Bij te weinig zuurstof ontstaat ook het giftige koolstofmonoxide."),
            ("p", "Een <strong>alkaan lost niet goed op in water</strong>: alkanen zijn apolair en water "
                  "is polair, dus blijft benzine op water liggen. En <strong>hoe langer de koolstofketen, "
                  "hoe hoger het kookpunt</strong>, want de londonkrachten tussen de moleculen worden "
                  "groter. Daarom is methaan een gas en octaan een vloeistof."),
            ("p", "<strong>Methaan is het hoofdbestanddeel van aardgas.</strong> <strong>Propaan en butaan "
                  "zitten in gasflessen</strong> en in een aansteker: ze zijn bij lichte druk al vloeibaar, "
                  "dus krijg je er veel van in een kleine fles. <strong>Propaan</strong> blijft ook bij "
                  "koud weer verdampen, dus werkt een propaanfles buiten in de winter beter. Decaan en "
                  "hexaan zijn bij kamertemperatuur vloeistoffen."),
        ]),
        dict(kop="Alkenen en alkynen", blokken=[
            ("p", "Het <strong>specifieke structuuronderdeel van een alkeen is een dubbele binding tussen "
                  "twee koolstofatomen</strong>. Daardoor zijn er twee waterstofatomen minder dan bij het "
                  "alkaan, en wordt de <strong>algemene formule CnH2n</strong>. De uitgang is "
                  "<strong>-een</strong>."),
            ("p", "Het <strong>specifieke structuuronderdeel van een alkyn is een drievoudige binding "
                  "tussen twee koolstofatomen</strong>. De <strong>uitgang is -yn</strong>."),
            ("p", "<strong>Etheen is C₂H₄ en ethaan C₂H₆</strong>: de dubbele binding scheelt twee "
                  "waterstofatomen, dus zijn het niet dezelfde formules. <strong>Etheen</strong> gebruikt "
                  "men in de voedingssector <strong>om vruchten sneller te laten rijpen</strong>: het is "
                  "een plantenhormoon dat rijping op gang brengt, en daarom rijpt fruit sneller naast een "
                  "rijpe banaan."),
        ]),
        dict(kop="Alcoholen en carbonzuren", blokken=[
            ("p", "De <strong>functionele groep van een alcohol is OH</strong>, en de uitgang van de naam "
                  "is <strong>-ol</strong>. Die OH-groep hangt hier <strong>aan een koolstofatoom en niet "
                  "aan een metaalion</strong>, en daarom is <strong>een alcohol geen base</strong>."),
            ("p", "De <strong>functionele groep van een carbonzuur is COOH</strong>. Die groep "
                  "<strong>kan haar waterstof als H⁺ afgeven</strong>, en net daarom reageert een "
                  "carbonzuur zuur: azijn heeft een pH onder zeven."),
            ("p", tabel(["Triviale naam", "IUPAC-naam", "Formule", "Stofklasse"], [
                ["drankalcohol", "ethanol", "C₂H₅OH", "alcohol"],
                ["(giftige alcohol)", "methanol", "CH₃OH", "alcohol"],
                ["mierenzuur", "methaanzuur", "HCOOH", "carbonzuur"],
                ["azijnzuur", "ethaanzuur", "CH₃COOH", "carbonzuur"],
                ["brandspiritus", "ethanol met bittere stof", "—", "alcohol"],
            ])),
            ("p", "<strong>Azijnzuur is ethaanzuur</strong>: twee koolstofatomen met een COOH-groep. "
                  "Keukenazijn is een oplossing van ongeveer vijf procent ervan. "
                  "<strong>Methaanzuur HCOOH</strong> is het eenvoudigste carbonzuur, met één "
                  "koolstofatoom; het geeft een brandnetelprik en een mierenbeet hun scherpe karakter."),
            ("p", "<strong>Drankalcohol is ethanol</strong>, dat bij de gisting van suikers ontstaat en "
                  "ook in handgel zit. <strong>Methanol lijkt erop maar is zwaar giftig</strong>: het "
                  "<strong>lichaam zet het om in giftige stoffen</strong> die het oog en het zenuwstelsel "
                  "aantasten, en enkele milliliter kan al blind maken."),
            ("p", "<strong>Brandspiritus</strong> is ethanol waaraan men een bittere stof toevoegt zodat "
                  "niemand het opdrinkt. Men gebruikt het <strong>als brandstof en als oplosmiddel</strong>, "
                  "en het brandt met een bijna onzichtbare vlam."),
            ("weetje", "De vijf organische stofklassen die je kent, zijn alkanen, alkenen, alkynen, "
                       "alcoholen en carbonzuren. Aan de uitgang van de naam zie je meteen welke het is: "
                       "-aan, -een, -yn, -ol of -zuur."),
        ]),
    ],
    onthoud=[
        "Een alkaan heeft enkel koolstof en waterstof met enkelvoudige bindingen; de formule is CnH2n+2.",
        "Methaan CH₄, ethaan C₂H₆, propaan C₃H₈, butaan C₄H₁₀, pentaan C₅H₁₂, hexaan C₆H₁₄, heptaan C₇H₁₆, octaan C₈H₁₈, nonaan C₉H₂₀, decaan C₁₀H₂₂.",
        "Een alkeen heeft een dubbele binding (CnH2n), een alkyn een drievoudige; uitgang -een en -yn.",
        "Een alcohol heeft een OH-groep aan koolstof en is geen base; een carbonzuur heeft COOH en geeft H⁺ af.",
        "Verbranding van een alkaan geeft CO₂ en water; bij te weinig zuurstof ook koolstofmonoxide.",
        "Alkanen zijn apolair en lossen niet op in water; langere keten betekent hoger kookpunt.",
        "Methaan zit in aardgas, propaan en butaan in gasflessen, etheen laat vruchten rijpen.",
        "Drankalcohol is ethanol, azijnzuur is ethaanzuur, methaanzuur zit in een mierenbeet.",
        "Methanol lijkt op ethanol maar is zwaar giftig; brandspiritus is ethanol met een bittere stof.",
    ],
)

# ───────────────────── 9. Stoffen in water: polariteit, oplossen en pH
BUNDELS["stoffen-in-water-polariteit-oplossen-en-ph-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen in water: polariteit, oplossen en pH",
    onder="Polaire en apolaire stoffen, de vier intermoleculaire krachten, elektrolyten met dissociatie en ionisatie, en de pH met haar indicatoren.",
    secties=[
        dict(kop="Polair of apolair", blokken=[
            ("p", "Een binding is <strong>polair als het verschil in elektronegativiteit minstens 0,4 "
                  "is</strong>. Onder die waarde geldt ze als <strong>apolair</strong>. Dat is een "
                  "vaste afspraak, dus een <strong>verschil van 0,2 is apolair</strong>."),
            ("p", "Bij een groot verschil trekt het ene atoom de elektronen duidelijk naar zich toe, en "
                  "krijgt de binding een <strong>plus- en een minkant</strong>."),
            ("p", "Een <strong>watermolecule is polair</strong> omdat ze <strong>gebogen is en zuurstof "
                  "harder trekt</strong>: door de hoek vallen de twee effecten niet weg, dus blijft er een "
                  "minkant en een pluskant over."),
            ("p", "Een <strong>molecule met polaire bindingen kan als geheel toch apolair zijn</strong>, "
                  "als ze symmetrisch is. <strong>CCl₄ is apolair</strong>, want de polaire bindingen "
                  "vallen tegen elkaar weg, en <strong>CO₂ is apolair</strong> omdat de molecule recht en "
                  "symmetrisch is. <strong>Alkanen zoals hexaan</strong> zijn de klassieke apolaire "
                  "stoffen, samen met de enkelvoudige stoffen."),
        ]),
        dict(kop="De vier intermoleculaire krachten", blokken=[
            ("p", tabel(["Kracht", "Werkt tussen", "Sterkte"], [
                ["waterstofbrug", "H aan O, N of F en een naburige molecule", "de sterkste van de vier"],
                ["ion-dipoolkracht", "een ion en een polaire molecule", "sterk"],
                ["dipoolkracht", "twee polaire moleculen", "matig"],
                ["londonkracht", "alle moleculen", "zwak"],
            ])),
            ("p", "Een <strong>waterstofbrug ontstaat als waterstof aan zuurstof, stikstof of fluor "
                  "hangt</strong>, en is de <strong>sterkste intermoleculaire kracht</strong>. Daarom "
                  "<strong>kookt water pas bij honderd graden</strong>, veel hoger dan je bij zo'n kleine "
                  "molecule zou verwachten: om te koken moet je die bruggen verbreken. Een waterstofbrug "
                  "is wel <strong>veel zwakker dan een atoombinding</strong>, want die zit bínnen een "
                  "molecule."),
            ("p", "<strong>Londonkrachten werken tussen alle moleculen, ook tussen polaire</strong>: ze "
                  "ontstaan uit tijdelijke, toevallige verschuivingen van de elektronen. Bij een "
                  "<strong>apolaire stof zijn ze de enige kracht</strong>; bij polaire stoffen komen de "
                  "dipoolkrachten erbovenop."),
            ("p", "Bij een <strong>dipoolkracht</strong> richt de pluskant van de ene molecule zich naar "
                  "de minkant van de andere."),
            ("p", "De <strong>ion-dipoolkracht houdt een opgelost ion vast aan de watermoleculen "
                  "eromheen</strong>: de minkant van het water richt zich naar een positief ion en de "
                  "pluskant naar een negatief ion. Dat omhullen heet <strong>hydratatie</strong>, en "
                  "daardoor valt het rooster van het zout uiteen."),
        ]),
        dict(kop="Oplosbaarheid", blokken=[
            ("p", "De vuistregel is <strong>gelijk lost op in gelijk</strong>: polaire stoffen lossen op "
                  "in polaire oplosmiddelen en apolaire in apolaire."),
            ("p", "<strong>Olie lost niet op in water omdat olie apolair en water polair is.</strong> De "
                  "watermoleculen houden elkaar sterk vast met waterstofbruggen en laten de apolaire "
                  "oliemoleculen er niet tussen."),
            ("p", "<strong>Keukenzout</strong> bestaat uit ionen en <strong>suiker</strong> heeft veel "
                  "OH-groepen, dus lossen ze <strong>allebei goed op in water</strong>. "
                  "<strong>Olijfolie en paraffine</strong> zijn apolair en lossen niet op."),
            ("p", "Een <strong>apolair oplosmiddel is geschikt om vet te verwijderen</strong>, want vet is "
                  "zelf apolair. Daarom werkt vlekkenwater op een vetvlek en water niet."),
        ]),
        dict(kop="Elektrolyten: dissociëren en ioniseren", blokken=[
            ("p", "Een <strong>elektrolyt geeft in water vrij bewegende ionen</strong> en "
                  "<strong>geleidt daardoor elektriciteit in oplossing</strong>. Zouten, zuren en "
                  "hydroxiden zijn alle drie elektrolyten. Een <strong>niet-elektrolyt vormt geen ionen en "
                  "geleidt dus niet</strong>: <strong>suiker en ethanol</strong> lossen wel op, maar "
                  "blijven neutrale moleculen."),
            ("p", "De <strong>dissociatievergelijking</strong> en de <strong>ionisatievergelijking</strong> "
                  "schrijven op wat er met een stof in water gebeurt. Bij <strong>dissociëren komen de "
                  "ionen uit het rooster los in het water</strong>. Die "
                  "ionen bestonden al, het water trekt ze alleen los van elkaar. Bij "
                  "<strong>ioniseren ontstaan de ionen pas in het water</strong>: een polaire molecule "
                  "zoals HCl heeft er nog geen. Dat is dus het verschil."),
            ("p", tabel(["Stof", "Wat gebeurt er", "Vergelijking"], [
                ["NaCl", "dissocieert", "NaCl → Na¹⁺ + Cl¹⁻"],
                ["CaCl₂", "dissocieert", "CaCl₂ → Ca²⁺ + 2 Cl¹⁻"],
                ["NaOH", "dissocieert", "NaOH → Na¹⁺ + OH¹⁻"],
                ["HCl", "ioniseert", "HCl → H¹⁺ + Cl¹⁻"],
            ])),
            ("p", "Bij <strong>CaCl₂</strong> zijn er <strong>twee chloride-ionen</strong> nodig, want "
                  "calcium geeft een ion met lading 2+ en elk chloride-ion heeft lading 1−. Bij "
                  "<strong>HCl</strong> breekt de polaire binding en laat het waterstofatoom zijn elektron "
                  "bij chloor achter."),
            ("p", "<strong>NaCl en HCl geleiden opgelost in water</strong>; <strong>suiker</strong> lost "
                  "op zonder ionen te vormen en <strong>hexaan</strong> lost niet op. Een <strong>vast "
                  "zout is een isolator</strong>: de ionen zitten vast in het rooster. Opgelost of "
                  "gesmolten geleidt hetzelfde zout wel, en dan is het een <strong>geleider</strong>."),
        ]),
        dict(kop="De pH en de indicatoren", blokken=[
            ("p", "<strong>Zuiver water heeft een pH van 7</strong> en is neutraal: de concentratie H⁺ en "
                  "OH⁻ zijn er gelijk. <strong>Onder zeven is een oplossing zuur</strong>, "
                  "<strong>boven zeven basisch</strong>. Een oplossing met <strong>pH 3 is dus "
                  "zuur</strong>."),
            ("p", "<strong>Hoe lager de pH, hoe meer H⁺ in de oplossing.</strong> Een hoge pH betekent "
                  "dus weinig H⁺ en veel OH⁻. Het <strong>waterstofion H⁺, ook een proton genoemd, maakt een oplossing zuur</strong>, en een "
                  "<strong>hydroxide geeft in water OH⁻-ionen</strong> die ze basisch maken."),
            ("p", tabel(["Indicator", "Zuur midden", "Neutraal", "Basisch midden"], [
                ["fenolftaleïne", "kleurloos", "kleurloos", "paars"],
                ["lakmoes", "rood", "—", "blauw"],
            ])),
            ("p", "<strong>Lakmoes wordt rood in een zuur en blauw in een base.</strong> "
                  "<strong>Fenolftaleïne blijft kleurloos in een zuur en in een neutraal midden, en wordt "
                  "paars zodra de oplossing basisch is.</strong> Die kleuren staan in de bijlage die je op "
                  "het examen mag gebruiken."),
            ("p", "Is een oplossing <strong>kleurloos met fenolftaleïne en rood met lakmoes</strong>, dan "
                  "is ze <strong>zuur</strong>: rood lakmoes wijst op een zuur, en fenolftaleïne is in een "
                  "zuur én in een neutraal midden kleurloos, dus beslist lakmoes hier."),
            ("p", "Met een <strong>pH-meter</strong> meet je de pH nauwkeurig: een indicator geeft een "
                  "gebied aan, een pH-meter een getal met decimalen."),
        ]),
    ],
    onthoud=[
        "Een binding is polair vanaf een verschil in elektronegativiteit van 0,4; eronder apolair.",
        "Water is polair omdat de molecule gebogen is; CO₂ en CCl₄ zijn symmetrisch en dus apolair.",
        "Waterstofbrug is het sterkst, dan ion-dipool, dan dipool, dan londonkracht.",
        "Gelijk lost op in gelijk; olie is apolair en lost niet op in water.",
        "Hydratatie is het omhullen van een ion door watermoleculen, met ion-dipoolkrachten.",
        "Een elektrolyt geeft ionen en geleidt; suiker en ethanol zijn niet-elektrolyten.",
        "Een zout dissocieert (de ionen bestonden al), een polaire molecule zoals HCl ioniseert.",
        "pH 7 is neutraal, eronder zuur, erboven basisch; hoe lager de pH, hoe meer H⁺.",
        "Lakmoes: rood in zuur, blauw in base. Fenolftaleïne: kleurloos in zuur en neutraal, paars in base.",
    ],
)

# ───────────────────── 10. Neerslag-, gas-, neutralisatie- en redoxreacties
BUNDELS["neerslag-gas-neutralisatie-en-redoxreacties-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Neerslag-, gas-, neutralisatie- en redoxreacties",
    onder="De drie ionenuitwisselingsreacties met de oplosbaarheidstabel, de essentiële reactievergelijking, en de redoxreacties met hun oxidatiegetallen.",
    secties=[
        dict(kop="De oplosbaarheidstabel", blokken=[
            ("p", tabel(["Verbindingen", "Goed oplosbaar", "Slecht oplosbaar"], [
                ["met Na¹⁺ of K¹⁺", "alle", "—"],
                ["ammonium, nitraten", "alle", "—"],
                ["chloriden, bromiden, jodiden", "alle behalve", "Ag¹⁺ (en Hg, Pb)"],
                ["sulfaten", "alle behalve", "Ba²⁺ (en Pb, Ca matig)"],
                ["sulfiden", "Na, K, NH₄, Mg, Ba, Ca", "alle andere"],
                ["fosfaten en carbonaten", "Na, K, NH₄", "alle andere"],
                ["hydroxiden", "groep IA, beperkter groep IIA", "alle andere groepen"],
            ])),
            ("p", "<strong>Alle verbindingen met natrium zijn goed oplosbaar</strong>, en met kalium ook: "
                  "de tabel zegt daar zonder meer alle. <strong>Alle nitraten zijn goed oplosbaar</strong>, "
                  "ook zonder uitzondering. Daarom gebruikt men die stoffen graag om een reactie mee op te "
                  "zetten."),
            ("p", "<strong>Bariumsulfaat is niet goed oplosbaar in water.</strong> Sulfaten zijn goed "
                  "oplosbaar behalve die van barium, en juist daarom kan men bariumsulfaat veilig als "
                  "contrastmiddel laten drinken."),
            ("p", "<strong>Carbonaten van natrium, kalium en ammonium zijn goed oplosbaar, de andere "
                  "niet.</strong> Daarom slaat calciumcarbonaat neer als kalksteen of ketelsteen."),
        ]),
        dict(kop="De neerslagreactie", blokken=[
            ("p", "Bij een <strong>neerslagreactie ontstaat een slecht oplosbare vaste stof</strong>: twee "
                  "ionen uit de twee oplossingen vormen samen een stof die slecht oplost, en die zakt naar "
                  "de bodem."),
            ("p", "Giet je <strong>zilvernitraat bij een oplossing van keukenzout</strong>, dan "
                  "<strong>ontstaat een witte neerslag</strong> van zilverchloride, want "
                  "<strong>het zilverion en het chloride-ion reageren</strong>. Er komt geen gas vrij en "
                  "de oplossing wordt niet basisch."),
            ("p", "<strong>Ba²⁺ met SO₄²⁻</strong> en <strong>Ag¹⁺ met Cl¹⁻</strong> geven een neerslag. "
                  "<strong>Na¹⁺ met NO₃¹⁻</strong> en <strong>K¹⁺ met Cl¹⁻</strong> niet, want die lossen "
                  "allemaal goed op."),
            ("p", "De <strong>essentiële reactievergelijking</strong> bevat <strong>enkel de ionen die "
                  "echt reageren</strong>: <strong>Ag¹⁺ + Cl¹⁻ → AgCl</strong>. Natrium en nitraat blijven "
                  "gewoon opgelost. Die ionen die niets doen, heten <strong>tribune-ionen</strong>, en in "
                  "de <strong>stoffenreactievergelijking</strong> staan ze er wel bij: "
                  "AgNO₃ + NaCl → AgCl + NaNO₃."),
        ]),
        dict(kop="De gasontwikkelingsreactie", blokken=[
            ("p", tabel(["Combinatie", "Gas dat vrijkomt"], [
                ["carbonaat of waterstofcarbonaat + zuur", "koolstofdioxide CO₂"],
                ["sulfide + zuur", "waterstofsulfide H₂S"],
                ["ammoniumzout + sterke base", "ammoniak NH₃"],
            ])),
            ("p", "Giet je <strong>azijn op bakpoeder</strong>, dan schuimt er "
                  "<strong>koolstofdioxide</strong> op: het zuur maakt uit het waterstofcarbonaat "
                  "koolzuur, en dat valt onmiddellijk uiteen in water en koolstofdioxide. Hetzelfde "
                  "gebeurt met <strong>zoutzuur op kalksteen</strong>."),
            ("p", "Een <strong>zuur bij een sulfide</strong> geeft <strong>waterstofsulfide</strong>, dat "
                  "naar rotte eieren ruikt en giftig is; daarom doet men zo'n proef onder een trekkast. "
                  "Een <strong>sterke base bij een ammoniumzout</strong> geeft "
                  "<strong>ammoniak</strong>: de base haalt een H⁺ van het ammoniumion weg."),
        ]),
        dict(kop="De neutralisatiereactie", blokken=[
            ("p", "Bij een <strong>neutralisatiereactie ontstaan een zout en water</strong>: de H⁺ van het "
                  "zuur en de OH⁻ van de base vormen water, en het metaalion en de zuurrest blijven als "
                  "zout over. <strong>Er ontstaat dus geen gas.</strong>"),
            ("p", "De <strong>essentiële reactievergelijking is H¹⁺ + OH¹⁻ → H₂O</strong>. Enkel die twee "
                  "ionen reageren echt."),
            ("p", "<strong>Zoutzuur met natriumhydroxide geeft natriumchloride</strong> en water. "
                  "<strong>Zwavelzuur met kaliumhydroxide geeft kaliumsulfaat</strong> en water, met twee "
                  "kaliumionen per sulfaation."),
        ]),
        dict(kop="Oxidatie, reductie, oxidator en reductor", blokken=[
            ("p", "Bij een <strong>oxidatie geeft een deeltje elektronen af</strong> en "
                  "<strong>stijgt zijn oxidatiegetal</strong>. Bij een <strong>reductie neemt het "
                  "elektronen op en daalt het oxidatiegetal</strong>. <strong>Oxidatie en reductie "
                  "gebeuren altijd samen</strong>, want de elektronen die de ene stof afgeeft, moet de "
                  "andere opnemen. <strong>Protonen blijven altijd in de kern.</strong>"),
            ("p", "Een <strong>oxidator neemt elektronen op</strong> en wordt daarbij zelf gereduceerd. "
                  "Een <strong>reductor geeft elektronen af</strong>, <strong>wordt zelf "
                  "geoxideerd</strong> en zijn oxidatiegetal stijgt."),
            ("p", "In <strong>2 Mg + O₂ → 2 MgO</strong> wordt <strong>magnesium geoxideerd van 0 naar "
                  "+II</strong>: het geeft per atoom twee elektronen af en is dus de reductor. Het "
                  "<strong>zuurstofgas is de oxidator</strong> en gaat van 0 naar −II."),
            ("p", "In een <strong>enkelvoudige stof is het oxidatiegetal van elk atoom nul</strong>, dus "
                  "ook in O₂ en in Fe."),
            ("p", "<strong>Het verbranden van propaan en het roesten van ijzer zijn "
                  "redoxreacties</strong>, want er gaan elektronen over. Een <strong>neutralisatie en een "
                  "neerslagreactie zijn dat niet</strong>: daar wisselen de ionen enkel van partner en "
                  "blijven hun ladingen gelijk. Een <strong>neerslagreactie is dus geen "
                  "elektronenoverdracht</strong> maar ionenuitwisseling."),
        ]),
        dict(kop="De reactiepatronen van de redoxreacties", blokken=[
            ("p", tabel(["Patroon", "Voorbeeld", "Product"], [
                ["metaal + dizuurstof", "ijzer dat roest", "Fe₂O₃, een metaaloxide"],
                ["niet-metaal + dizuurstof", "zwavel die brandt", "SO₂, een niet-metaaloxide"],
                ["metaal + niet-metaal", "ijzer met zwavel", "FeS, een zout"],
                ["alkaan, alkeen, alkyn of alcohol + O₂", "verbranding", "CO₂ en water"],
            ])),
            ("p", "<strong>Een metaal met dizuurstof geeft een metaaloxide.</strong> Roest is zo een "
                  "metaaloxide: ijzer gaat naar oxidatiegetal +III, dus <strong>Fe₂O₃</strong>, en roest "
                  "bladdert af en beschermt het metaal eronder dus niet. <strong>Zwavel met "
                  "zuurstof</strong> geeft <strong>SO₂</strong>, zwaveldioxide, een niet-metaaloxide dat "
                  "met water in de lucht zure regen geeft."),
            ("p", "Bij de <strong>volledige verbranding van ethanol ontstaan koolstofdioxide en "
                  "water</strong>: ook een alcohol bevat enkel koolstof, waterstof en zuurstof."),
            ("p", "Bij een <strong>slechte verbranding ontstaat koolstofmonoxide omdat er te weinig "
                  "zuurstof is</strong>: elk koolstofatoom krijgt dan maar één zuurstofatoom mee. "
                  "Koolstofmonoxide is kleurloos, geurloos en dodelijk."),
            ("p", "Kloppend maken: <strong>2 C₂H₆ + 7 O₂ → 4 CO₂ + 6 H₂O</strong>. En om "
                  "<strong>één molecule CH₄</strong> volledig te verbranden heb je <strong>twee "
                  "moleculen O₂</strong> nodig."),
        ]),
    ],
    onthoud=[
        "Alles met natrium, kalium, ammonium of nitraat lost goed op; bariumsulfaat en zilverchloride niet.",
        "Carbonaten en fosfaten lossen enkel op met natrium, kalium of ammonium.",
        "Een neerslagreactie geeft een vaste stof; de essentiële vergelijking laat de tribune-ionen weg.",
        "Carbonaat met zuur geeft CO₂, sulfide met zuur H₂S, ammoniumzout met base NH₃.",
        "Een neutralisatie geeft een zout en water: H⁺ + OH⁻ → H₂O.",
        "Oxidatie is elektronen afgeven en het oxidatiegetal stijgt; reductie is het omgekeerde.",
        "Een oxidator neemt elektronen op, een reductor geeft ze af en wordt zelf geoxideerd.",
        "Verbranden en roesten zijn redox; een neutralisatie en een neerslagreactie zijn ionenuitwisseling.",
        "Metaal met O₂ geeft een metaaloxide, niet-metaal met O₂ een zuurvormend oxide.",
    ],
)

# ───────────────────── 11. Rekenen met mol, massa en concentratie
BUNDELS["rekenen-met-mol-massa-en-concentratie-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rekenen met mol, massa en concentratie",
    onder="De mol en het getal van Avogadro, de molaire massa, de twee concentraties, verdunnen met c₁V₁ = c₂V₂ en de stoichiometrische berekeningen.",
    secties=[
        dict(kop="De mol en het getal van Avogadro", blokken=[
            ("p", "In <strong>één mol van een stof zitten 6,02.10²³ deeltjes</strong>. Dat getal heet het "
                  "<strong>getal van Avogadro</strong> en staat in de bijlage die je op het examen mag "
                  "gebruiken. Het is een afspraak, zoals een dozijn er twaalf zijn, maar veel groter."),
            ("p", "<strong>Eén mol van een stof bevat altijd evenveel deeltjes, welke stof het ook "
                  "is</strong>, en <strong>twee mol bevat twee keer zoveel deeltjes als één mol</strong>: "
                  "het aantal deeltjes is recht evenredig met de stofhoeveelheid. De "
                  "<strong>massa</strong> van die mol verschilt wel per stof: <strong>één mol water en "
                  "één mol koolstofdioxide hebben niet dezelfde massa</strong>, want water is 18,0 g/mol "
                  "en koolstofdioxide 44,0 g/mol."),
            ("p", "De fiche spreekt af: <strong>vraagt men naar de stofhoeveelheid, dan bedoelt men het "
                  "aantal mol</strong>, niet de massa in gram. Anders staat er uitdrukkelijk massa of "
                  "aantal deeltjes."),
            ("p", tabel(["Omzetting", "Formule"], [
                ["massa naar mol", "n = m / M"],
                ["aantal deeltjes naar mol", "n = N / N<sub>A</sub>"],
                ["mol naar massa", "m = n · M"],
                ["mol naar aantal deeltjes", "N = n · N<sub>A</sub>"],
            ])),
            ("p", "<strong>n = m / M</strong>: je deelt de massa door de massa van één mol, en wat "
                  "overblijft is het aantal mol. Je hebt daarvoor enkel de <strong>massa van het "
                  "staal</strong> en de <strong>molaire massa van de stof</strong> nodig; het volume en "
                  "de temperatuur komen er niet bij."),
            ("p", "<strong>1,204.10²⁴ moleculen is 2,00 mol</strong> (gedeeld door 6,02.10²³), en "
                  "<strong>3,01.10²³ deeltjes is 0,500 mol</strong>, precies de helft. Omgekeerd zitten er "
                  "in <strong>0,250 mol 1,51.10²³ moleculen</strong>."),
        ]),
        dict(kop="De molaire massa", blokken=[
            ("p", "De <strong>molaire massa</strong> zegt hoeveel gram één mol weegt, dus is haar eenheid "
                  "<strong>g/mol</strong>. Je <strong>leest ze af uit de relatieve atoommassa's in het "
                  "periodiek systeem</strong> door die van alle atomen in de formule op te tellen; "
                  "je rondt af op 0,1."),
            ("p", tabel(["Stof", "Berekening", "Molaire massa"], [
                ["H₂O", "2 × 1,0 + 16,0", "18,0 g/mol"],
                ["CO₂", "12,0 + 2 × 16,0", "44,0 g/mol"],
                ["NaOH", "23,0 + 16,0 + 1,0", "40,0 g/mol"],
                ["NaCl", "23,0 + 35,5", "58,5 g/mol"],
            ])),
            ("p", "Rekenvoorbeelden: <strong>36,0 g water is 2,00 mol</strong>, "
                  "<strong>88,0 g CO₂ is 2,00 mol</strong>, <strong>0,500 mol natriumchloride weegt "
                  "29,3 g</strong> en <strong>0,200 mol water weegt 3,60 g</strong>."),
            ("p", "Een <strong>schatting vooraf</strong> laat je zien of je antwoord in de goede orde "
                  "ligt: <strong>drie keer ruim veertig is ongeveer honderdtwintig</strong>, en 3 mol CO₂ "
                  "weegt inderdaad 132 g."),
        ]),
        dict(kop="De twee concentraties", blokken=[
            ("p", "De <strong>molaire concentratie is de stofhoeveelheid per volume</strong>: "
                  "<strong>c = n / V</strong>, met als <strong>eenheid mol per liter</strong>, ook "
                  "molariteit of M genoemd. De <strong>massaconcentratie is de massa per volume</strong>, "
                  "met als <strong>eenheid g/L</strong>."),
            ("p", "Rekenvoorbeelden: <strong>0,500 mol tot 2,00 L geeft 0,250 mol/L</strong>; "
                  "<strong>0,100 mol tot 250 mL geeft 0,400 mol/L</strong> (zet eerst om naar 0,250 L); "
                  "<strong>0,300 mol tot 1,50 L geeft 0,200 mol/L</strong>. En omgekeerd: in "
                  "<strong>500 mL van 0,400 mol/L zit 0,200 mol</strong>."),
            ("p", "Van <strong>massaconcentratie naar molaire concentratie</strong> deel je door de "
                  "molaire massa: <strong>40,0 g NaOH per liter is 1,00 mol/L</strong>, want M is "
                  "40,0 g/mol."),
        ]),
        dict(kop="Verdunnen", blokken=[
            ("p", "Bij het verdunnen gebruik je <strong>c₁V₁ = c₂V₂</strong>. Dat werkt omdat je "
                  "<strong>enkel water toevoegt, zodat het aantal mol opgeloste stof gelijk "
                  "blijft</strong>: het volume stijgt en de concentratie daalt in dezelfde verhouding. De "
                  "<strong>concentratie stijgt dus niet als je water toevoegt</strong>, ze daalt."),
            ("p", "<strong>50,0 mL van 1,00 mol/L tot 250 mL</strong> geeft <strong>0,200 mol/L</strong>: "
                  "het volume wordt vijf keer groter. <strong>25,0 mL van 0,800 mol/L tot 100 mL</strong> "
                  "geeft <strong>0,200 mol/L</strong>, want vier keer groter."),
            ("p", "Omgekeerd: voor <strong>100 mL van 2,00 mol/L uit een voorraad van 10,0 mol/L</strong> "
                  "neem je <strong>20,0 mL</strong> uit die voorraad en vul je aan tot 100 mL."),
        ]),
        dict(kop="Stoichiometrische berekeningen", blokken=[
            ("p", "De <strong>coëfficiënten in een reactievergelijking geven de verhouding in aantal "
                  "deeltjes, dus in mol</strong>, en niet in gram. Daarom reken je bij een berekening "
                  "<strong>eerst de massa om in mol</strong>, dan <strong>gebruik je de verhouding uit de "
                  "coëfficiënten</strong>, en pas daarna reken je terug naar gram. Massa's gewoon bij "
                  "elkaar optellen of volumes vergelijken werkt niet."),
            ("p", "In <strong>2 H₂ + O₂ → 2 H₂O</strong> hoort op twee H₂ één O₂, dus bij "
                  "<strong>4,00 mol H₂ hoort 2,00 mol O₂</strong>. In "
                  "<strong>CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂</strong> is de verhouding tussen CaCO₃ en "
                  "CO₂ één op één, dus geeft <strong>1,00 mol kalksteen 1,00 mol CO₂</strong>."),
            ("p", "Een <strong>aflopende reactie gaat door tot een van de reagentia helemaal opgebruikt "
                  "is</strong>. Die stof heet het <strong>beperkende reagens</strong>: ze bepaalt hoeveel "
                  "product er maximaal kan ontstaan, en de andere stof blijft in overmaat over. De "
                  "verhouding waarin de stoffen reageren, heet de "
                  "<strong>stoichiometrische verhouding</strong>."),
            ("p", "Je <strong>antwoord noteer je met het juiste aantal beduidende cijfers</strong>: een "
                  "meting is nooit exact, dus mag je antwoord niet nauwkeuriger lijken dan je gegevens."),
        ]),
    ],
    onthoud=[
        "Eén mol is 6,02.10²³ deeltjes; stofhoeveelheid betekent altijd het aantal mol.",
        "n = m / M, en n = het aantal deeltjes gedeeld door het getal van Avogadro; omgekeerd m = n · M.",
        "De molaire massa in g/mol tel je op uit de relatieve atoommassa's: water 18,0, CO₂ 44,0, NaOH 40,0, NaCl 58,5.",
        "Molaire concentratie c = n / V in mol/L; massaconcentratie is massa per volume in g/L.",
        "Van g/L naar mol/L deel je door de molaire massa.",
        "Verdunnen: c₁V₁ = c₂V₂, want het aantal mol blijft gelijk en het volume stijgt.",
        "Coëfficiënten gelden in mol, niet in gram: reken eerst naar mol, dan de verhouding, dan terug.",
        "Het beperkende reagens is als eerste opgebruikt en bepaalt hoeveel product er kan ontstaan.",
        "Noteer je antwoord in het juiste aantal beduidende cijfers en in wetenschappelijke notatie.",
    ],
)

# ───────────────────── 12. Veilig werken, meten en onderzoek
BUNDELS["veilig-werken-meten-en-onderzoek-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en onderzoek",
    onder="De veiligheidspictogrammen en de P- en H-zinnen, het glaswerk en de meetinstrumenten, de eenheden en beduidende cijfers, en de onderzoeksmethode.",
    secties=[
        dict(kop="De veiligheidspictogrammen", blokken=[
            ("p", tabel(["Pictogram", "Wat het betekent"], [
                ["bijtend of corrosief", "veroorzaakt brandwonden en tast materialen aan"],
                ["ontvlambaar", "vat vlam bij een vonk of vlam"],
                ["oxiderend", "kan brand en ontploffing veroorzaken of verergeren"],
                ["explosief", "kan ontploffen"],
                ["gassen onder druk", "de fles zelf is gevaarlijk bij warmte of stoten"],
                ["giftig", "werkt onmiddellijk schadelijk of dodelijk"],
                ["irriterend, schadelijk", "prikt op de huid, de ogen of de luchtwegen"],
                ["langetermijngevaar voor de gezondheid", "kanker, erfelijke schade, orgaanschade"],
                ["gevaarlijk voor het aquatische milieu", "schadelijk voor het water en wat erin leeft"],
            ])),
            ("p", "Het pictogram met de <strong>twee druppels die een hand en een plaat "
                  "aantasten</strong>, betekent <strong>bijtend of corrosief</strong>: de stof veroorzaakt "
                  "brandwonden. Zwavelzuur en bijtende soda horen daarbij."),
            ("p", "Het pictogram voor <strong>oxiderend</strong> staat op een fles die <strong>brand kan "
                  "veroorzaken of verergeren</strong>: de stof geeft zuurstof af en voedt zo een brand. "
                  "Zo'n fles houd je weg van brandbare stoffen."),
            ("p", "De pictogrammen die <strong>vooral voor schade aan je gezondheid</strong> waarschuwen, "
                  "zijn <strong>giftig</strong> (dat werkt meteen) en het "
                  "<strong>langetermijngevaar</strong>, dat wijst op kanker, erfelijke schade of "
                  "orgaanschade. Gassen onder druk gaat over de fles zelf, en het laatste pictogram over "
                  "het milieu."),
            ("p", "De <strong>H-zinnen benoemen het gevaar</strong> van de stof; H staat voor hazard. De "
                  "<strong>P-zinnen</strong> zeggen welke <strong>voorzorgen</strong> je neemt."),
        ]),
        dict(kop="Veilig en duurzaam werken", blokken=[
            ("p", "<strong>In een labo eet en drink je niet</strong>, want er kunnen sporen van stoffen op "
                  "je handen of op het glaswerk zitten. Een <strong>stof die je niet kan benoemen, ruik of "
                  "smaak je nooit</strong>: sommige dampen zijn al bij één keer inademen schadelijk."),
            ("p", "Morst je een product, dan <strong>kuis je dat onmiddellijk op volgens de "
                  "voorschriften</strong>: het kan iemand verwonden of met een andere stof reageren."),
            ("p", "Bij veilig en duurzaam werken horen: <strong>zuinig omgaan met chemische "
                  "stoffen</strong>, een <strong>meetinstrument uitzetten als je niet meet</strong>, "
                  "<strong>het meetbereik en de nauwkeurigheid respecteren</strong>, "
                  "<strong>onderhoudsvoorschriften en handleidingen juist interpreteren</strong> en "
                  "<strong>glaswerk voorzichtig behandelen en glasscherven veilig opruimen</strong>. "
                  "<strong>Elektrische toestellen met natte handen bedienen</strong> en "
                  "<strong>glasscherven met de hand bij elkaar vegen</strong> horen daar net niet bij."),
            ("p", "Je <strong>houdt je altijd aan het meetbereik</strong> van een instrument: buiten dat "
                  "bereik is de meting niet geldig en kan het toestel beschadigen, dus belast je een "
                  "balans van 200 g niet met een kilo."),
            ("p", "Een <strong>bunsenbrander laat je niet onbewaakt branden</strong>: een open vlam kan "
                  "altijd iets doen ontvlammen. En <strong>chemisch afval giet je niet in de "
                  "gootsteen</strong>, want het kan het water vervuilen of in de leiding reageren."),
        ]),
        dict(kop="Glaswerk en meetinstrumenten", blokken=[
            ("p", tabel(["Materiaal", "Waarvoor"], [
                ["volpipet", "één bepaald volume heel nauwkeurig afmeten"],
                ["maatkolf", "een oplossing tot een nauwkeurig volume aanvullen"],
                ["maatcilinder", "een volume afmeten, redelijk nauwkeurig"],
                ["maatbeker", "een ruwe aanduiding van het volume"],
                ["erlenmeyer", "zwenken zonder te morsen, bij een titratie"],
                ["scheitrechter", "twee vloeistoflagen scheiden, met een kraantje"],
                ["mortier en stamper", "een vaste stof fijnmaken"],
                ["liebigkoeler", "damp weer laten condenseren bij destilleren"],
                ["balans", "de massa van een staal bepalen"],
                ["pH-meter", "de pH nauwkeurig meten"],
            ])),
            ("p", "Om <strong>precies 25,0 mL</strong> af te meten gebruik je een "
                  "<strong>volpipet</strong>: die is voor één volume gemaakt en dus heel nauwkeurig, "
                  "terwijl een maatbeker maar een ruwe aanduiding geeft. Een <strong>maatkolf</strong> "
                  "heeft één streepje op de nek, dus vul je een oplossing daarmee aan tot een "
                  "<strong>nauwkeurig volume</strong>."),
            ("p", "Je <strong>kiest een instrument waarvan het meetbereik net boven je volume "
                  "ligt</strong>: voor ongeveer 40 mL dus een <strong>maatcilinder van 50 mL</strong> en "
                  "niet een van 500 mL, want een te grote cilinder leest veel grover af."),
            ("p", "Je <strong>leest het volume in een maatcilinder af op ooghoogte, onderaan de holle "
                  "vloeistofspiegel</strong>. Die holle spiegel heet de meniscus, en op ooghoogte maak je "
                  "geen kijkfout."),
            ("p", "Een <strong>erlenmeyer</strong> is het kegelvormige glas met een nauwe hals: door die "
                  "hals blijft de vloeistof binnen als je ze ronddraait. Een "
                  "<strong>scheitrechter</strong> is het trechtervormige glas met een kraantje. Met een "
                  "<strong>mortier en stamper</strong> maak je een vaste stof fijn, zodat ze sneller "
                  "oplost."),
        ]),
        dict(kop="Grootheden, eenheden en nauwkeurigheid", blokken=[
            ("p", "Een <strong>grootheid noteer je altijd samen met haar eenheid</strong>, want zonder "
                  "eenheid betekent een getal niets."),
            ("p", tabel(["Grootheid", "SI-eenheid", "Ook gebruikt"], [
                ["volume V", "kubieke meter m³", "liter L"],
                ["massa m", "kilogram kg", "gram g"],
                ["temperatuur θ", "—", "graden Celsius °C"],
                ["absolute temperatuur T", "kelvin K", "—"],
                ["massadichtheid ρ", "kg/m³", "g/L"],
                ["stofhoeveelheid n", "mol", "—"],
                ["molaire massa M", "—", "g/mol"],
                ["molaire concentratie c", "—", "mol/L of M"],
                ["massaconcentratie c", "—", "g/L"],
            ])),
            ("p", tabel(["Voorvoegsel", "Symbool", "Waarde"], [
                ["mega", "M", "10⁶"], ["kilo", "k", "10³"], ["hecto", "h", "10²"],
                ["deca", "da", "10¹"], ["deci", "d", "10⁻¹"], ["centi", "c", "10⁻²"],
                ["milli", "m", "10⁻³"], ["micro", "μ", "10⁻⁶"], ["nano", "n", "10⁻⁹"],
            ])),
            ("p", "<strong>Milli en nano staan voor een waarde kleiner dan één</strong> (een duizendste "
                  "en een miljardste); <strong>kilo is duizend</strong> en mega een miljoen keer de "
                  "eenheid. <strong>Een centimeter is een honderdste van een meter.</strong>"),
            ("p", "Omrekenen: <strong>2,5 mg is 0,0025 g</strong> en <strong>0,75 L is 750 mL</strong>."),
            ("p", "Een <strong>meting met een instrument is niet exact</strong>: elk instrument heeft een "
                  "beperkte nauwkeurigheid. Daarom noteer je het juiste aantal "
                  "<strong>beduidende cijfers</strong>. In <strong>0,00340 zijn er drie</strong>: de "
                  "nullen vooraan tellen niet mee, de nul achteraan wel."),
            ("p", "In de <strong>wetenschappelijke notatie</strong> staat er één cijfer verschillend van "
                  "nul voor de komma: <strong>0,00450 wordt 4,50.10⁻³</strong>."),
            ("p", "Verbanden tussen grootheden: <strong>recht evenredig</strong>, "
                  "<strong>omgekeerd evenredig</strong>, <strong>lineair</strong> of "
                  "<strong>kwadratisch</strong>. Verdubbelt het volume van een oplossing en wordt de "
                  "concentratie gehalveerd, dan is dat <strong>omgekeerd evenredig</strong>: het product "
                  "van de twee blijft constant, en dat product is hier het aantal mol."),
        ]),
        dict(kop="De onderzoeksmethode", blokken=[
            ("p", "De stappen: <strong>de probleemstelling definiëren en afbakenen</strong>, "
                  "<strong>een onderzoeksvraag opstellen en een hypothese formuleren</strong>, "
                  "<strong>een onderzoeksplan opstellen</strong>, <strong>data waarnemen en "
                  "verzamelen</strong>, <strong>de data analyseren</strong>, "
                  "<strong>conclusies trekken</strong> en ten slotte "
                  "<strong>over je methode en resultaten reflecteren en communiceren</strong>."),
            ("p", "Een <strong>hypothese</strong> is een <strong>beredeneerde verwachting die je met een "
                  "proef wil toetsen</strong>: geen gok, maar iets dat je op wat je al weet baseert. Een "
                  "<strong>weerlegde hypothese betekent niet dat je onderzoek mislukt is</strong>: blijkt "
                  "ze niet te kloppen, dan heb je iets geleerd."),
            ("p", "Wat <strong>niet</strong> bij onderzoek hoort: <strong>de meetwaarden aanpassen aan de "
                  "hypothese</strong> of <strong>de conclusie vooraf vastleggen</strong>."),
            ("p", tabel(["Criterium", "Dit wil zeggen"], [
                ["open", "het is een open vraag"],
                ["enkelvoudig", "ze gaat over één onderwerp of probleem"],
                ["objectief", "ze laat geen overtuiging of mening doorschemeren"],
                ["haalbaar", "het onderzoek is uitvoerbaar met genoeg tijd en middelen"],
                ["onderzoekbaar", "het is geen opzoekvraag en niet direct oplosbaar"],
                ["relevant", "het antwoord draagt bij aan de bestaande kennis"],
            ])),
            ("p", "<strong>Enkelvoudig</strong> betekent dat de vraag <strong>over één onderwerp "
                  "gaat</strong>: onderzoek je twee dingen tegelijk, dan weet je achteraf niet waaraan het "
                  "resultaat ligt. <strong>Objectief</strong> betekent dat ze "
                  "<strong>geen overtuiging of mening laat doorschemeren</strong>; een vraag als waarom is "
                  "dit middel het beste, legt het antwoord al vast."),
            ("p", "De vraag <strong>wanneer werd zuurstof ontdekt, is een opzoekvraag en geen "
                  "onderzoeksvraag</strong>: het antwoord ligt al in een boek, terwijl je een "
                  "onderzoeksvraag met een proef of met eigen metingen moet kunnen beantwoorden."),
            ("p", "Op de <strong>horizontale as van een grafiek</strong> zet je de grootheid die je "
                  "<strong>zelf instelt</strong>, de onafhankelijke variabele. De grootheid die je meet, "
                  "komt op de verticale as. Bij elke as horen de naam, de eenheid en een schaal."),
            ("p", "<strong>STEM</strong> staat voor <strong>wetenschappen, technologie, "
                  "ingenieurswetenschappen en wiskunde</strong>; de <strong>M staat dus voor "
                  "wiskunde</strong>. Je zet die vier samen in om een maatschappelijk probleem op te "
                  "lossen: je <strong>definieert het probleem</strong>, geeft "
                  "<strong>criteria</strong> waaraan de oplossing moet voldoen, splitst het in "
                  "<strong>deelproblemen</strong>, bedenkt oplossingen en "
                  "<strong>evalueert en stuurt bij</strong>."),
            ("weetje", "De criteria voor een onderzoeksvraag krijg je op het examen mee. De fiche zegt "
                       "ook dat één doel over handelingen gesimuleerd wordt: je legt de handeling uit in "
                       "plaats van ze uit te voeren."),
        ]),
    ],
    onthoud=[
        "H-zinnen benoemen het gevaar, P-zinnen de voorzorgen.",
        "Bijtend geeft brandwonden, oxiderend voedt een brand, giftig werkt meteen, het langetermijnpictogram wijst op kanker en orgaanschade.",
        "In een labo eet en drink je niet en een onbekende stof ruik je nooit.",
        "Volpipet en maatkolf zijn nauwkeurig, een maatbeker geeft een ruwe aanduiding.",
        "Lees een volume af op ooghoogte, onderaan de meniscus, met een instrument dat net groot genoeg is.",
        "SI: kubieke meter voor volume, kilogram voor massa, kelvin voor absolute temperatuur.",
        "Kilo is 10³ en mega 10⁶; milli 10⁻³, micro 10⁻⁶ en nano 10⁻⁹.",
        "In 0,00340 zijn er drie beduidende cijfers; 0,00450 wordt 4,50.10⁻³.",
        "Een onderzoeksvraag is open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant.",
    ],
)

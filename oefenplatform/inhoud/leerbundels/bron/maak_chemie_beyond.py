# -*- coding: utf-8 -*-
"""De leerbundels voor chemie op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche chemie van de 3de graad doorstroomfinaliteit, geldig
vanaf 1 januari 2027. Die fiche hoort bij de richtingen die hun wetenschappen
in drie aparte examens afleggen: biologie, chemie en fysica. Ze gaat dus veel
dieper dan het onderdeel chemie van de fiche natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De drieëntwintig thema's volgen de weging van de fiche zelf: zes thema's voor de
toepassingen, zes voor de opbouw van de stof, vier voor het rekenen, twee voor
de organische reacties en twee voor het onderzoek; kunststoffen, nanomaterialen
en duurzame chemie krijgen elk een eigen thema omdat ze elk veel afzonderlijke
begrippen bevatten.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde woorden
als de vraag. `python3 dekking.py ../../beyond/chemie.json` doet daar het
voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Chemie"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────── 1. Anorganische stoffen: stofklassen en naamgeving
BUNDELS["anorganische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Anorganische stoffen: stofklassen en naamgeving",
    onder="Hoe je een anorganische stof in een klasse zet, en hoe ze aan haar naam komt.",
    secties=[
        dict(kop="Enkelvoudig of samengesteld, binair of ternair", blokken=[
            ("p", "Een <strong>enkelvoudige stof</strong> bestaat uit "
                  "<strong>één soort atoom, dus één element</strong>. "
                  "<strong>Zuurstofgas</strong> is O₂ en <strong>ozon</strong> is O₃: beide zijn "
                  "enkelvoudig, maar ze zijn <strong>niet dezelfde stof</strong> en gedragen zich "
                  "heel anders. Water en keukenzout zijn <strong>samengesteld</strong>."),
            ("p", "Een <strong>binaire verbinding</strong> bestaat uit "
                  "<strong>twee verschillende elementen</strong>, niet uit twee atomen: Fe₂O₃ heeft "
                  "vijf atomen en is toch binair. Een <strong>ternaire verbinding</strong> heeft "
                  "<strong>drie verschillende elementen</strong>, zoals "
                  "<strong>calciumcarbonaat CaCO₃</strong> met calcium, koolstof en zuurstof."),
            ("p", "De <strong>brutoformule</strong> of <strong>molecuulformule</strong> zegt "
                  "<strong>enkel hoeveel atomen van elk element</strong> er in een molecule zitten, "
                  "zoals C₂H₆O. Hoe die atomen aan elkaar zitten, zegt pas een "
                  "<strong>structuurformule</strong>. Bij een ionverbinding spreken we van een "
                  "<strong>formule-eenheid</strong>: die geeft "
                  "<strong>de kleinste verhouding van de ionen</strong> en niet één molecule, want "
                  "<strong>NaCl bestaat niet als losse molecule</strong>."),
        ]),
        dict(kop="De vier grote stofklassen", blokken=[
            ("p", "Een <strong>oxide</strong> is een <strong>verbinding van zuurstof met één "
                  "ander element</strong>, zoals <strong>calciumoxide CaO</strong> en "
                  "<strong>zwaveldioxide SO₂</strong>. Omdat er precies twee elementen in zitten, "
                  "zijn <strong>alle oxiden binaire verbindingen</strong>. In NaOH zit wel "
                  "zuurstof, maar samen met waterstof <strong>als hydroxidegroep</strong>, dus dat "
                  "is geen oxide."),
            ("p", "Een <strong>hydroxide</strong> heeft als functionele groep de "
                  "<strong>OH-groep</strong>, dus één of meer <strong>OH⁻-ionen</strong>: NaOH, "
                  "Ca(OH)₂, Al(OH)₃. <strong>Calciumhydroxide</strong> heeft "
                  "<strong>twee hydroxide-ionen</strong>, want Ca²⁺ heeft er twee nodig om neutraal "
                  "uit te komen, en is dus <strong>tweewaardig</strong>. Een waterige oplossing van "
                  "een hydroxide heet een <strong>loogoplossing</strong>."),
            ("p", "Een <strong>zuur</strong> <strong>begint in de formule met waterstof dat als "
                  "H⁺ kan weggaan</strong>: <strong>waterstofsulfaat H₂SO₄</strong> en "
                  "<strong>waterstofnitraat HNO₃</strong>. De <strong>waardigheid van een "
                  "zuur</strong> is <strong>het aantal waterstofatomen dat het als ion kan "
                  "afstaan</strong>: <strong>fosforzuur H₃PO₄ is driewaardig</strong>."),
            ("p", "Een <strong>zout</strong> is een <strong>verbinding van een metaalion met een "
                  "zuurrest</strong>, zoals NaCl, CaCO₃ en KNO₃. Een zout ontstaat uit een zuur en "
                  "een base: <strong>de zuurrest komt uit het zuur</strong> en het metaalion uit de "
                  "base. Uit HNO₃ en NaOH ontstaat zo NaNO₃. Staat er natrium op de plaats van de "
                  "waterstof, zoals in Na₂SO₄, dan is het dus een zout en geen zuur."),
        ]),
        dict(kop="Vier bijzondere gevallen", blokken=[
            ("p", "Bij een <strong>peroxide</strong> zitten "
                  "<strong>twee zuurstofatomen aan elkaar gebonden</strong>: in H₂O₂ en in Na₂O₂ "
                  "zit een <strong>O–O-brug</strong>, en zuurstof heeft daar oxidatiegetal "
                  "<strong>−I</strong> in plaats van −II. <strong>Zuurstofwater</strong> is "
                  "<strong>waterstofperoxide H₂O₂</strong>; het valt langzaam uiteen in water en "
                  "zuurstofgas, en daarom staat het in een donkere fles."),
            ("p", "In een <strong>hydraat</strong> zit <strong>kristalwater in het "
                  "rooster</strong>. <strong>CuSO₄·5H₂O</strong> heet "
                  "<strong>kopersulfaatpentahydraat</strong>: het Griekse telwoord "
                  "<strong>penta-</strong> zegt hoeveel moleculen water er per formule-eenheid vast "
                  "ingebouwd zitten."),
            ("p", "In een <strong>waterstofzout</strong> is <strong>maar een deel van de "
                  "waterstofionen van het zuur vervangen</strong>, dus blijft er één in de zuurrest "
                  "zitten: <strong>natriumwaterstofcarbonaat NaHCO₃</strong>."),
            ("p", "In een <strong>ammoniumzout</strong> neemt het <strong>ammoniumion NH₄⁺</strong> "
                  "<strong>de plaats van het metaalion</strong> in. Daarom is NH₄Cl een zout, ook al "
                  "zit er geen metaal in, en <strong>bevat een ammoniumzout dus niet altijd een "
                  "metaal</strong>: in NH₄NO₃ zit geen enkel metaalatoom."),
        ]),
        dict(kop="Namen geven volgens de regels", blokken=[
            ("p", "Het <strong>Romeinse cijfer in de stocknotatie</strong>, zoals in "
                  "<strong>ijzer(III)chloride</strong>, <strong>geeft het oxidatiegetal van het "
                  "metaal</strong>. IJzer kan +II of +III zijn; het cijfer zegt welk van de twee, en "
                  "daaruit volgt de formule FeCl₃."),
            ("p", "<strong>Griekse telwoorden zoals di- en tri-</strong> gebruik je "
                  "<strong>bij atoomverbindingen</strong>: CO₂ is <strong>koolstofdioxide</strong>. "
                  "Bij een ionverbinding volgt het aantal al uit de ladingen, dus zijn telwoorden "
                  "daar niet nodig."),
            ("p", "De uitgang zegt hoeveel zuurstof er in de zuurrest zit. De "
                  "<strong>uitgang -iet duidt op minder zuurstofatomen dan de uitgang "
                  "-aat</strong>: <strong>sulfaat is SO₄²⁻, sulfiet is SO₃²⁻</strong>, en zo hoort "
                  "<strong>zwavelzuur bij H₂SO₄</strong> en <strong>zwaveligzuur bij "
                  "H₂SO₃</strong>. Nitraat hoort bij HNO₃ en nitriet bij HNO₂. Het voorvoegsel "
                  "<strong>hypo-</strong> betekent <strong>nog één zuurstofatoom minder dan bij de "
                  "uitgang -iet</strong>. De volle rij loopt van "
                  "<strong>perchloorzuur HClO₄</strong> over <strong>chloorzuur HClO₃</strong> en "
                  "<strong>chlorigzuur HClO₂</strong> naar "
                  "<strong>hypochlorigzuur HClO</strong>."),
            ("p", "Eén stof heeft dus vaak twee namen. <strong>HNO₃</strong> heet "
                  "<strong>salpeterzuur</strong> en <strong>waterstofnitraat</strong>. Een "
                  "<strong>waterige oplossing van waterstofchloride</strong> heet "
                  "<strong>zoutzuur</strong>; de IUPAC-naam waterstofchloride hoort bij het gas "
                  "zelf."),
        ]),
        dict(kop="Symbolen en namen uit het dagelijks leven", blokken=[
            ("p", "Enkele symbolen om te kennen: <strong>K</strong> is "
                  "<strong>kalium</strong>, van het Latijnse kalium; <strong>Pb</strong> is "
                  "<strong>lood</strong>, van plumbum, waar ook loodgieter van komt; Ca is calcium "
                  "en C is koolstof. <strong>Fe</strong> en <strong>Cu</strong> zijn "
                  "<strong>metalen uit het d-blok</strong>, dus overgangsmetalen; silicium staat in "
                  "het p-blok en argon is een edelgas."),
            ("p", "Een <strong>triviale naam</strong> of gebruiksnaam "
                  "<strong>zegt niets over de formule</strong>. "
                  "<strong>Bijtende soda</strong> is <strong>natriumhydroxide</strong> en "
                  "<strong>gebluste kalk</strong> is <strong>calciumhydroxide</strong>. "
                  "<strong>Ongebluste kalk is CaO, gebluste kalk is Ca(OH)₂</strong>: giet je water "
                  "bij CaO, dan ontstaat Ca(OH)₂ en komt er veel warmte vrij, en dat blussen zit in "
                  "de naam."),
            ("p", "Drie natriumstoffen worden vaak verward. <strong>Soda</strong> is "
                  "<strong>Na₂CO₃</strong> of natriumcarbonaat, <strong>bakpoeder</strong> is "
                  "<strong>natriumwaterstofcarbonaat NaHCO₃</strong>, dat bij verwarmen "
                  "koolstofdioxide afgeeft en zo het deeg laat rijzen, en "
                  "<strong>ontstopper</strong> is <strong>een sterke oplossing van "
                  "natriumhydroxide</strong>, die vet en haar aantast."),
            ("p", "Nog drie gassen: <strong>N₂O</strong> heet <strong>lachgas</strong> of "
                  "distikstofmonoxide, <strong>CO₂</strong> heet in drank "
                  "<strong>koolzuurgas</strong> omdat het in water deels koolzuur H₂CO₃ vormt, en "
                  "<strong>blauwzuur</strong> is <strong>HCN of waterstofcyanide</strong>, heel "
                  "giftig en met een geur van bittere amandelen. "
                  "<strong>Blauwzuur is dus niet de gebruiksnaam van waterstofchloride</strong>."),
        ]),
    ],
    onthoud=[
        "Enkelvoudig is één element, binair twee elementen, ternair drie.",
        "Oxide: zuurstof met één ander element. Hydroxide: OH-groep.",
        "Zuur: H dat als H⁺ weggaat. Zout: metaalion plus zuurrest.",
        "Peroxide heeft een O–O-brug, hydraat heeft kristalwater.",
        "-aat heeft meer zuurstof dan -iet; hypo- nog één minder.",
        "Stocknotatie: het Romeinse cijfer is het oxidatiegetal.",
        "Soda Na₂CO₃, bakpoeder NaHCO₃, bijtende soda NaOH.",
    ],
)

# ───────────────────── 2. Organische stoffen: stofklassen en naamgeving
BUNDELS["organische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische stoffen: stofklassen en naamgeving",
    onder="De functionele groepen, de IUPAC-namen en de voorstellingen van een molecule.",
    secties=[
        dict(kop="Koolwaterstoffen: verzadigd en onverzadigd", blokken=[
            ("p", "Een keten is <strong>verzadigd</strong> als er "
                  "<strong>enkel enkelvoudige bindingen tussen de koolstofatomen</strong> zitten: "
                  "er kan geen waterstof meer bij. Een <strong>alkaan</strong> is verzadigd, en de "
                  "<strong>brutoformule van een alkaan met n koolstofatomen is "
                  "CnH2n+2</strong>: butaan heeft vier koolstofatomen en dus tien waterstofatomen, "
                  "C₄H₁₀."),
            ("p", "Een <strong>alkeen heeft minstens één dubbele binding</strong>, een C=C, en de "
                  "formule CnH2n. Een <strong>alkyn heeft een drievoudige binding</strong>, met de "
                  "uitgang <strong>-yn</strong>, zoals <strong>ethyn of acetyleen</strong> in de "
                  "snijbrander. Een <strong>alkeen heeft dus geen drievoudige binding</strong>."),
            ("p", "Een <strong>aromatische</strong> molecule, ook een "
                  "<strong>aromaat</strong>, heeft <strong>een benzeenring</strong> erin. "
                  "<strong>Benzeen is C₆H₆</strong>: <strong>de ring heeft zes "
                  "koolstofatomen</strong>, elk met één waterstofatoom, en "
                  "<strong>de elektronen zijn over de hele ring verdeeld</strong>. Daardoor "
                  "reageert benzeen anders dan een gewoon alkeen. "
                  "<strong>Cyclisch is niet hetzelfde als aromatisch</strong>: cyclohexaan is een "
                  "ring zonder dubbele bindingen en dus niet aromatisch."),
            ("p", "Een keten kan <strong>vertakt</strong> of onvertakt zijn. "
                  "<strong>2-methylbutaan</strong> is <strong>vertakt</strong> én "
                  "<strong>verzadigd</strong>: de methylgroep aan het tweede koolstofatoom maakt de "
                  "vertakking, en er zit geen dubbele binding in. Dat we een onvertakte keten "
                  "<strong>lineair</strong> noemen, is eigenlijk een afspraak: "
                  "<strong>een onvertakte keten is in werkelijkheid een zigzag, geen rechte "
                  "lijn</strong>, want de bindingshoek rond koolstof is ongeveer 109°."),
        ]),
        dict(kop="De functionele groepen, klasse per klasse", blokken=[
            ("p", "Bij de <strong>alcoholen</strong> hoort <strong>een OH-groep aan een "
                  "koolstofatoom</strong>, de <strong>hydroxylgroep</strong>: ethaan wordt "
                  "<strong>ethanol</strong>. Het aantal OH-groepen is de waardigheid: een "
                  "<strong>tweewaardige alcohol heeft twee OH-groepen</strong>, zoals "
                  "<strong>ethaandiol</strong>, waar de uitgang <strong>-diol</strong> zegt dat "
                  "<strong>er twee OH-groepen in de molecule zitten</strong>, en "
                  "<strong>propaantriol</strong> heeft er drie."),
            ("p", "De <strong>aldehyden</strong> en de <strong>ketonen</strong> hebben beide een "
                  "<strong>C=O-groep</strong>: bij een aldehyde staat die "
                  "<strong>aan het uiteinde</strong>, bij een keton <strong>ertussen</strong>. Een "
                  "aldehyde eindigt op <strong>-al</strong>, een keton op <strong>-on</strong>, een "
                  "alcohol op <strong>-ol</strong>. <strong>Propanon</strong> is het eenvoudigste "
                  "keton."),
            ("p", "Een <strong>carbonzuur</strong> heeft de "
                  "<strong>carboxylgroep COOH</strong>, zoals azijnzuur; het is dat waterstofatoom "
                  "dat als H⁺ kan weggaan. Een <strong>tweewaardig carbonzuur heeft twee "
                  "COOH-groepen</strong>, zoals <strong>ethaandizuur of oxaalzuur</strong>."),
            ("p", "Een <strong>ether</strong> heeft <strong>een zuurstofatoom tussen twee "
                  "koolstofketens, zonder dubbele binding</strong>: CH₃-O-CH₃. Er is dus geen "
                  "OH-groep, en daarom vormt een ether geen waterstofbruggen met zichzelf."),
            ("p", "Een <strong>ester</strong> krijgt een naam uit twee delen, met "
                  "<strong>de alcoholkant vooraan en de zuurkant achteraan</strong> met de uitgang "
                  "<strong>-oaat</strong>: <strong>ethylethanoaat</strong> en "
                  "<strong>methylpropanoaat</strong> zijn esters, en in "
                  "<strong>methylethanoaat</strong> staat de methylgroep van de alcohol vooraan."),
            ("p", "Een <strong>amine</strong> herken je <strong>aan een stikstofatoom met waterstof "
                  "eraan</strong>: CH₃-NH₂ is methaanamine. Zit er naast de stikstof ook een C=O, "
                  "dan is het een <strong>amide</strong>: dat is wat je krijgt als je "
                  "<strong>de OH van een carbonzuur vervangt door NH₂</strong>. In een eiwit heet "
                  "die verbinding een <strong>peptidebinding</strong>."),
            ("p", "Bij een <strong>halogeenalkaan</strong> is <strong>minstens één waterstofatoom "
                  "vervangen door F, Cl, Br of I</strong>: <strong>chloormethaan</strong> en "
                  "<strong>broomethaan</strong>."),
        ]),
        dict(kop="Primair, secundair en tertiair", blokken=[
            ("p", "Een <strong>alcohol is secundair</strong> als "
                  "<strong>het koolstofatoom met de OH-groep aan twee andere koolstofatomen "
                  "zit</strong>. Je kijkt dus naar <strong>de buren van dat ene "
                  "koolstofatoom</strong>, niet naar het nummer in de naam: propaan-2-ol is "
                  "secundair."),
            ("p", "Bij een <strong>amine</strong> tel je iets anders: "
                  "<strong>het aantal koolstofketens aan het stikstofatoom</strong>. Eén bij "
                  "primair, twee bij secundair, drie bij tertiair. Een "
                  "<strong>primair amine heeft dus niet drie ketens</strong> aan de stikstof."),
        ]),
        dict(kop="Namen en nummers", blokken=[
            ("p", "Het <strong>stamwoord</strong> zegt hoeveel koolstofatomen "
                  "<strong>de hoofdketen</strong> heeft: <strong>meth-</strong> 1, "
                  "<strong>eth-</strong> 2, <strong>prop-</strong> 3, <strong>but-</strong> 4, "
                  "<strong>pent-</strong> 5, <strong>hex-</strong> 6. In "
                  "<strong>pentaan</strong> zitten er dus <strong>vijf</strong>."),
            ("p", "Een cijfer in de naam <strong>zegt bij welk koolstofatoom de functionele groep "
                  "of de dubbele binding zit</strong>. In <strong>but-1-een</strong> zit de dubbele "
                  "binding vooraan, in <strong>but-2-een</strong> in het midden: dat zijn twee "
                  "verschillende stoffen. <strong>Bij het nummeren van de hoofdketen begin je aan "
                  "de kant die de functionele groep het laagste nummer geeft</strong>, dus is het "
                  "propaan-1-ol en niet propaan-3-ol."),
            ("p", "Twee voorbeelden om zelf na te rekenen. "
                  "<strong>CH₃-CH₂-CHO</strong> heet <strong>propanal</strong>: de CHO-groep aan het "
                  "uiteinde maakt er een aldehyde van, met drie koolstofatomen. "
                  "<strong>CH₃-CH₂-COOH</strong> heet <strong>propaanzuur</strong>: je telt het "
                  "koolstofatoom van de COOH-groep mee."),
        ]),
        dict(kop="Voorstellingen en gebruiksnamen", blokken=[
            ("p", "Een <strong>skeletnotatie</strong> laat "
                  "<strong>de koolstofatomen en hun waterstofatomen</strong> weg: elke hoek en elk "
                  "uiteinde van de lijn is een koolstofatoom, en de waterstof wordt niet getekend. "
                  "Functionele groepen schrijf je wel uit. In een "
                  "<strong>beknopte structuurformule</strong> staan "
                  "<strong>de waterstofatomen samengenomen per koolstofatoom</strong>, zoals "
                  "CH₃-CH₂-OH; <strong>uitgebreid</strong> teken je elke C-H-binding apart. Het "
                  "<strong>bolstaafmodel</strong> zegt het meest over de "
                  "<strong>ruimtelijke bouw</strong>, want daarin zie je ook de hoeken tussen de "
                  "bindingen."),
            ("p", "Enkele namen uit het dagelijks leven. <strong>Ethanol</strong> "
                  "(CH₃-CH₂-OH) is de <strong>drankalcohol</strong>; brandspiritus is ethanol die "
                  "ondrinkbaar gemaakt is. <strong>Azijnzuur</strong> heet volgens IUPAC "
                  "<strong>ethaanzuur</strong>, mierenzuur is methaanzuur en boterzuur is "
                  "butaanzuur. <strong>Glycerol</strong> is <strong>propaantriol</strong>, met "
                  "<strong>drie</strong> OH-groepen, en <strong>glycol</strong> is "
                  "<strong>ethaandiol</strong>: beide dus <strong>alcoholen</strong>. "
                  "<strong>Aceton</strong> is <strong>propanon</strong>, dus een "
                  "<strong>keton</strong>, en <strong>formol is een oplossing van methanal in "
                  "water</strong>, dat gebruikt werd om preparaten te bewaren."),
            ("p", "<strong>Aardgas bestaat hoofdzakelijk uit methaan</strong>, CH₄, het kortste "
                  "alkaan. <strong>Chloroform</strong> heet volgens IUPAC "
                  "<strong>trichloormethaan</strong>: drie van de vier waterstofatomen van methaan "
                  "zijn vervangen door chloor, CHCl₃."),
        ]),
    ],
    onthoud=[
        "Alkaan CnH2n+2, alkeen een dubbele binding, alkyn een drievoudige.",
        "OH is alcohol, C=O aan het eind aldehyde, ertussen keton, COOH zuur.",
        "Ether: zuurstof tussen twee ketens. Ester: alcoholkant vooraan.",
        "Amine: stikstof met waterstof. Amide: stikstof plus C=O.",
        "Nummer zo dat de functionele groep het laagste nummer krijgt.",
        "Alcohol: tel de buren van de koolstof. Amine: tel de ketens aan N.",
        "Benzeen C₆H₆ is aromatisch; cyclohexaan is enkel cyclisch.",
    ],
)

# ───────────────────── 3. Isomerie en chiraliteit
BUNDELS["isomerie-en-chiraliteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Isomerie en chiraliteit",
    onder="Dezelfde brutoformule, een andere stof: van ketenisomerie tot spiegelbeelden.",
    secties=[
        dict(kop="Wat isomeren gemeen hebben", blokken=[
            ("p", "Twee <strong>isomeren</strong> hebben altijd "
                  "<strong>dezelfde brutoformule</strong>: "
                  "<strong>alle</strong> elementen zijn dezelfde én er zijn "
                  "<strong>evenveel atomen van elk</strong>. Alleen zitten die atomen anders aan "
                  "elkaar, en daardoor zijn het verschillende stoffen. Ethaan en propaan "
                  "verschillen in het aantal koolstofatomen en zijn dus geen isomeren."),
            ("p", "Verschillende stoffen betekent ook verschillende eigenschappen. "
                  "<strong>Twee isomeren hebben dus niet hetzelfde smelt- en kookpunt</strong>: "
                  "butaan kookt bij −0,5 °C en 2-methylpropaan bij −12 °C. Ze hebben ook "
                  "<strong>niet altijd dezelfde geur en smaak</strong>, want onze reukcellen voelen "
                  "de vorm van een molecule."),
            ("p", "<strong>Een vertakte keten is vluchtiger dan een onvertakte</strong> met "
                  "dezelfde formule, omdat <strong>de moleculen elkaar over een kleiner oppervlak "
                  "raken</strong>: minder contact geeft zwakkere "
                  "<strong>londonkrachten</strong> en dus een lager kookpunt."),
        ]),
        dict(kop="Drie soorten structuurisomerie", blokken=[
            ("p", "Bij <strong>ketenisomerie</strong> zit het verschil "
                  "<strong>in de vorm van de keten</strong>: onvertakt tegenover vertakt. "
                  "<strong>Butaan en 2-methylpropaan</strong> hebben beide C₄H₁₀ en zijn "
                  "ketenisomeren; de stofklasse blijft dezelfde."),
            ("p", "Bij <strong>plaatsisomerie</strong> zit "
                  "<strong>de functionele groep op een andere plaats in dezelfde keten</strong>. "
                  "<strong>Propaan-1-ol en propaan-2-ol</strong> zijn plaatsisomeren, en "
                  "<strong>but-1-een en but-2-een</strong> verschillen in "
                  "<strong>de plaats van de dubbele binding</strong>. "
                  "<strong>Plaatsisomeren horen tot dezelfde stofklasse</strong>, want de "
                  "functionele groep verhuist alleen."),
            ("p", "Bij <strong>functie-isomerie</strong> verandert "
                  "<strong>de stofklasse zelf</strong>. <strong>Ethanol en dimethylether</strong> "
                  "zijn beide C₂H₆O: de ene is een alcohol, de andere een ether. Ook een "
                  "<strong>aldehyde en een keton</strong> met dezelfde brutoformule zijn "
                  "functie-isomeren, zoals propanal en propanon (C₃H₆O), en "
                  "<strong>een carbonzuur en een ester</strong>: ethaanzuur en methylmethanoaat "
                  "zijn beide C₂H₄O₂, maar het zuur staat een H⁺ af en de ester niet. Een stof met "
                  "de formule <strong>C₃H₈O</strong> kan dus <strong>een alcohol of een "
                  "ether</strong> zijn."),
            ("p", "Tellen helpt. Van <strong>C₃H₈</strong> bestaat er "
                  "<strong>één</strong> structuurisomeer, want propaan kan niet vertakken; van "
                  "<strong>C₄H₁₀</strong> bestaan er <strong>twee</strong> (butaan en "
                  "2-methylpropaan) en van <strong>C₅H₁₂</strong> <strong>drie</strong> (pentaan, "
                  "2-methylbutaan en 2,2-dimethylpropaan). <strong>Methaan heeft geen "
                  "isomeren</strong>, want <strong>er is maar één manier om één koolstof en vier "
                  "waterstof te verbinden</strong>. Een alcohol op de keten van butaan heeft "
                  "<strong>twee</strong> plaatsisomeren, butaan-1-ol en butaan-2-ol, want je mag de "
                  "keten ook van de andere kant nummeren."),
        ]),
        dict(kop="Stereo-isomerie: Z en E", blokken=[
            ("p", "Bij <strong>stereo-isomerie</strong> "
                  "<strong>zitten de atomen in dezelfde volgorde aan elkaar</strong> en zit "
                  "<strong>het verschil in de ruimtelijke plaatsing</strong>. "
                  "<strong>Z/E-isomeren zijn dus geen structuurisomeren.</strong>"),
            ("p", "Voor <strong>Z/E-isomerie</strong> bij een dubbele binding moet "
                  "<strong>elk koolstofatoom van de dubbele binding twee verschillende groepen "
                  "dragen</strong>. Bij <strong>but-2-een</strong> zit "
                  "<strong>aan elk koolstofatoom van de dubbele binding een methylgroep en een "
                  "waterstofatoom</strong>, dus heeft die stof een Z- en een E-vorm; but-1-een "
                  "niet. <strong>Z</strong> betekent dat "
                  "<strong>de twee voorrangsgroepen aan dezelfde kant staan</strong>, van het "
                  "Duitse zusammen; <strong>E</strong> komt van entgegen, tegenover."),
            ("p", "<strong>Rond een enkelvoudige binding bestaat geen Z/E-isomerie</strong>, want "
                  "<strong>die binding kan vrij draaien</strong>: een sigma-binding laat draaien "
                  "toe, en de <strong>pi-binding</strong> van een dubbele binding zet dat draaien "
                  "vast. Een Z- en een E-isomeer hebben toch "
                  "<strong>een verschillend kookpunt</strong>, want "
                  "<strong>hun vorm maakt hun polariteit en hun onderlinge krachten "
                  "anders</strong>: bij de Z-vorm versterken de dipooltjes elkaar, bij de E-vorm "
                  "heffen ze elkaar vaker op."),
        ]),
        dict(kop="Chiraliteit en optische isomerie", blokken=[
            ("p", "Een koolstofatoom met <strong>vier verschillende groepen</strong> eraan heet "
                  "<strong>asymmetrisch</strong> of <strong>chiraal</strong>. Zo'n koolstofatoom "
                  "maakt de molecule chiraal: ze valt niet samen met haar spiegelbeeld, net zoals "
                  "je linker- en rechterhand. <strong>Een molecule met één asymmetrisch "
                  "koolstofatoom is dus altijd chiraal.</strong> "
                  "<strong>2-chloorbutaan</strong> heeft er <strong>één</strong>: het tweede "
                  "koolstofatoom draagt een waterstofatoom, een chlooratoom, een methylgroep en een "
                  "ethylgroep. <strong>Propaan-2-ol is niet chiraal</strong>, want "
                  "<strong>het middelste koolstofatoom draagt twee gelijke methylgroepen</strong>."),
            ("p", "Twee isomeren die elkaars spiegelbeeld zijn, heten "
                  "<strong>spiegelbeeldisomeren</strong>, <strong>enantiomeren</strong> of "
                  "<strong>optische isomeren</strong>. Het aantal "
                  "<strong>stereo-isomeren</strong> is <strong>2ⁿ</strong>, met n het aantal "
                  "asymmetrische koolstofatomen: bij twee zijn er <strong>vier</strong>, bij drie "
                  "<strong>acht</strong>."),
            ("p", "Je onderscheidt ze met <strong>gepolariseerd licht</strong>, dat in één vlak "
                  "trilt: een optisch actieve stof draait dat vlak over een meetbare hoek. "
                  "<strong>Twee spiegelbeeldisomeren draaien het vlak niet naar dezelfde "
                  "kant</strong>: ze draaien het over dezelfde hoek, maar naar de andere kant. "
                  "Daarom heet het ook <strong>optische isomerie</strong>."),
            ("p", "Een <strong>racemisch mengsel</strong> is "
                  "<strong>een mengsel met evenveel van beide spiegelbeeldisomeren</strong>, en "
                  "het <strong>draait het vlak van gepolariseerd licht niet</strong>, want de twee "
                  "helften heffen elkaar precies op. <strong>Enkele eigenschappen zijn voor beide "
                  "gelijk</strong>, zoals <strong>het smeltpunt</strong> en "
                  "<strong>de molaire massa</strong>. In het lichaam niet: receptoren en enzymen "
                  "zijn zelf chiraal en passen maar op één van de twee. Het nadeel van een "
                  "<strong>medicijn als racemisch mengsel</strong> is dus dat "
                  "<strong>de helft niet werkt of zelfs anders werkt in het lichaam</strong>, en "
                  "daarom wordt een medicijn soms gescheiden."),
        ]),
    ],
    onthoud=[
        "Isomeren: dezelfde brutoformule, een andere stof.",
        "Keten: vertakt of niet. Plaats: groep verhuist. Functie: andere klasse.",
        "C₃H₈ één isomeer, C₄H₁₀ twee, C₅H₁₂ drie.",
        "Z/E vraagt twee verschillende groepen aan elke kant van de C=C.",
        "Een enkelvoudige binding draait vrij, een dubbele niet.",
        "Vier verschillende groepen aan één koolstof: asymmetrisch, dus chiraal.",
        "Aantal stereo-isomeren is 2ⁿ; een racemisch mengsel draait niet.",
    ],
)

# ───────────────────── 4. Atoombouw, orbitalen en het periodiek systeem
BUNDELS["atoombouw-orbitalen-en-het-periodiek-systeem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Atoombouw, orbitalen en het periodiek systeem",
    onder="Van kwantumgetal tot configuratie, en hoe het systeem dat allemaal samenvat.",
    secties=[
        dict(kop="Orbitalen en kwantumgetallen", blokken=[
            ("p", "Een <strong>orbitaal</strong> is "
                  "<strong>het gebied waar een elektron zich met grote kans bevindt</strong>. In "
                  "het <strong>model van Schrödinger</strong> ligt de plaats van een elektron niet "
                  "vast: een orbitaal is dus een <strong>kansgebied, geen baan</strong>. Twee "
                  "modellen gaan verder dan de schillen van Bohr: het "
                  "<strong>model van Bohr-Sommerfeld, met subniveaus</strong>, en het "
                  "<strong>model van Schrödinger, met orbitalen</strong> en de golfmechanica."),
            ("p", "In één orbitaal passen <strong>twee elektronen, met tegengestelde "
                  "spin</strong>. Dat volgt uit het <strong>uitsluitingsprincipe van "
                  "Pauli</strong>: <strong>twee elektronen in hetzelfde atoom kunnen nooit alle "
                  "vier hun kwantumgetallen gelijk hebben</strong>, en vaak is de spin het enige "
                  "verschil."),
            ("p", "<strong>Vier</strong> kwantumgetallen beschrijven één elektron volledig. Het "
                  "<strong>hoofdkwantumgetal n</strong> geeft "
                  "<strong>het hoofdniveau of de schil waarin het elektron zit</strong>; hoe groter "
                  "n, hoe verder van de kern en hoe hoger de energie. Het "
                  "<strong>nevenkwantumgetal</strong> <strong>bepaalt of een elektron in een s-, "
                  "p-, d- of f-orbitaal zit</strong>, dus het subniveau, en elk subniveau heeft zijn "
                  "eigen vorm: <strong>s is bolvormig, p heeft twee lobben</strong>. Het "
                  "<strong>magnetisch kwantumgetal</strong> zegt "
                  "<strong>in welk orbitaal van dat subniveau</strong> het elektron zit, en dus "
                  "<strong>niet hoeveel elektronen er in een subniveau passen</strong>. Het "
                  "<strong>spinkwantumgetal</strong> kan <strong>+½ en −½</strong> zijn, in de "
                  "hokjesvoorstelling een pijl omhoog en een pijl omlaag."),
            ("p", "Hoeveel elektronen passen er in een subniveau? Een "
                  "<strong>p-subniveau</strong> heeft drie orbitalen en dus "
                  "<strong>zes</strong> plaatsen, s heeft er 2, een volledig "
                  "<strong>d-subniveau</strong> heeft vijf orbitalen en dus "
                  "<strong>tien</strong> plaatsen, en f heeft er 14."),
        ]),
        dict(kop="De vulregels en de configuratie", blokken=[
            ("p", "De <strong>regel van Hund</strong> zegt dat "
                  "<strong>orbitalen van dezelfde energie eerst elk met één elektron "
                  "vullen</strong>. Pas als elk orbitaal van dat subniveau één elektron heeft, komt "
                  "het tweede erbij, en die eerste elektronen hebben dezelfde spin."),
            ("p", "De <strong>diagonaalregel</strong> dient "
                  "<strong>om de volgorde te vinden waarin de subniveaus gevuld worden</strong>. "
                  "Daarom komt <strong>4s</strong> vóór <strong>3d</strong>: de diagonaal loopt niet "
                  "gewoon van laag naar hoog hoofdniveau, en de configuratie van calcium eindigt op "
                  "4s²."),
            ("p", "Een voorbeeld: een <strong>zuurstofatoom met acht elektronen</strong> heeft de "
                  "configuratie <strong>1s² 2s² 2p⁴</strong>, dus zes valentie-elektronen en twee "
                  "te kort voor een octet. In de <strong>verkorte notatie</strong> "
                  "<strong>vervang je het begin van de configuratie door het symbool van het "
                  "vorige edelgas</strong>: kalium wordt <strong>[Ar] 4s¹</strong>. De "
                  "<strong>valentie-elektronen</strong> zijn die van het hoogste hoofdniveau, dus "
                  "een atoom met <strong>[Ne] 3s² 3p³</strong> heeft er "
                  "<strong>vijf</strong>: dat is fosfor."),
            ("p", "De <strong>hokjesvoorstelling</strong> toont "
                  "<strong>hoe de elektronen over de orbitalen verdeeld zijn, met hun "
                  "spin</strong>; de exponentennotatie doet dat niet. Zo zie je of de regel van "
                  "Hund gevolgd is."),
            ("p", "Twee uitzonderingen horen bij het d-blok. De configuratie van "
                  "<strong>chroom</strong> eindigt op <strong>3d⁵ 4s¹</strong> en niet op 3d⁴ 4s², "
                  "want <strong>een halfgevuld d-subniveau is stabieler dan een gewone "
                  "vulling</strong>. Bij chroom en koper schuift er daarom één elektron van 4s naar "
                  "3d."),
            ("p", "Ook een ion heeft een configuratie. <strong>Na⁺</strong> "
                  "<strong>heeft tien elektronen</strong> en "
                  "<strong>heeft de configuratie van neon</strong>: natrium staat één elektron af "
                  "en wat overblijft is 1s² 2s² 2p⁶."),
        ]),
        dict(kop="Groepen, perioden en blokken", blokken=[
            ("p", "Alle elementen van dezelfde <strong>groep</strong> hebben "
                  "<strong>het aantal elektronen in het buitenste hoofdniveau</strong> gemeen, en "
                  "daarom reageren ze op dezelfde manier. Het "
                  "<strong>groepsnummer van een hoofdgroepelement heeft dus wél alles te maken met "
                  "het aantal valentie-elektronen</strong>: groep 1 heeft er één, groep 2 twee, "
                  "groep 16 zes en groep 17 zeven."),
            ("p", "Een <strong>periode is een rij in het systeem</strong> en "
                  "<strong>het nummer geeft het hoogste hoofdniveau</strong>. Een groep is de "
                  "kolom. Drie groepsnamen om te kennen: "
                  "<strong>groep 17 heet de halogenen</strong> (fluor, chloor, broom en jood, met "
                  "zeven valentie-elektronen), <strong>groep 1 met lithium, natrium en kalium heet "
                  "de alkalimetalen</strong>, die heftig met water reageren en een hydroxide vormen, "
                  "en <strong>groep 16 met zuurstof, zwavel en selenium heet de "
                  "zuurstofgroep</strong>, die graag twee elektronen opneemt tot een ion met lading "
                  "2−."),
            ("p", "Het blok draagt de naam van het subniveau dat als laatste gevuld wordt. De "
                  "<strong>overgangselementen</strong> of nevengroepelementen staan "
                  "<strong>in het d-blok</strong>, waarvan "
                  "<strong>een volledige rij tien elementen</strong> heeft. De "
                  "<strong>zeldzame aarden staan in het f-blok</strong>, de twee rijen die onder het "
                  "systeem apart staan; ze zitten in magneten en in de elektronica van een gsm. Zit "
                  "het buitenste elektron in een p-orbitaal, dan staat het element in het "
                  "<strong>p-blok</strong>, dus groep 13 tot 18. Een atoom met "
                  "<strong>[Ar] 4s² 3d¹⁰ 4p⁵</strong> staat "
                  "<strong>in groep 17, bij de halogenen</strong>: 2 plus 5 valentie-elektronen, "
                  "dus broom."),
            ("p", "De <strong>edelgassen</strong> zijn zo weinig reactief omdat "
                  "<strong>hun buitenste hoofdniveau helemaal volgevuld is</strong>: acht "
                  "valentie-elektronen, en dat is de edelgasconfiguratie waar de "
                  "<strong>octetregel</strong> naar verwijst. "
                  "<strong>Helium volgt die regel niet met acht</strong> maar met twee, want zijn "
                  "enige hoofdniveau is dan al vol. Uit het groepsnummer volgt ook het verwachte "
                  "oxidatiegetal: bij <strong>groep 2</strong> is dat "
                  "<strong>+II</strong>, dus Mg²⁺."),
        ]),
        dict(kop="Trends in het systeem", blokken=[
            ("p", "<strong>De atoomradius van de hoofdgroepelementen neemt toe naar beneden in een "
                  "groep</strong>, want elk nieuw hoofdniveau ligt verder van de kern: kalium is "
                  "groter dan natrium. Ga je <strong>in een periode naar rechts</strong>, dan "
                  "<strong>wordt hij kleiner, want de kern trekt sterker aan</strong>: er komt elke "
                  "keer een proton bij terwijl de elektronen in hetzelfde hoofdniveau blijven."),
            ("p", "Een <strong>positief ion</strong> "
                  "<strong>is kleiner dan het atoom waaruit het ontstond</strong> en "
                  "<strong>heeft minder elektronen dan protonen</strong>: bij het afstaan van een "
                  "elektron verdwijnt vaak een heel hoofdniveau. Een "
                  "<strong>negatief ion is groter</strong>, want "
                  "<strong>de extra elektronen stoten elkaar af en de kernlading blijft "
                  "gelijk</strong>: Cl⁻ is duidelijk groter dan het chlooratoom."),
            ("p", "<strong>Fluor</strong> heeft "
                  "<strong>de hoogste elektronegatieve waarde</strong> en trekt dus het hardst aan "
                  "de elektronen van een binding; naar links en naar beneden wordt die waarde "
                  "kleiner. Het sterkste <strong>metaalkarakter</strong> vind je "
                  "<strong>linksonder in het periodiek systeem</strong>, want een metaal staat zijn "
                  "elektronen makkelijk af en dat gaat het best als ze ver van de kern zitten en er "
                  "maar één of twee zijn."),
        ]),
    ],
    onthoud=[
        "Een orbitaal is een kansgebied; er passen twee elektronen met tegengestelde spin.",
        "Vier kwantumgetallen: hoofdniveau, subniveau, magnetisch niveau, spin.",
        "s 2, p 6, d 10, f 14 elektronen.",
        "Hund: eerst elk orbitaal één elektron. Diagonaalregel: 4s voor 3d.",
        "Groep is de kolom en geeft de valentie-elektronen; periode is de rij.",
        "Naar rechts kleiner, naar beneden groter; fluor is het meest elektronegatief.",
        "Positief ion kleiner dan zijn atoom, negatief ion groter.",
    ],
)

# ───────────────────── 5. Atoombinding en lewisstructuren
BUNDELS["atoombinding-en-lewisstructuren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Atoombinding en lewisstructuren",
    onder="Sigma en pi, vrije elektronenparen, formele lading en de drie soorten binding.",
    secties=[
        dict(kop="Sigma- en pi-bindingen", blokken=[
            ("p", "Een <strong>sigma-binding</strong> ontstaat doordat "
                  "<strong>twee orbitalen recht tegenover elkaar overlappen, langs de "
                  "bindingsas</strong>. Die overlapping ligt op de lijn tussen de twee kernen en "
                  "heet daarom <strong>coaxiaal</strong>; ze is "
                  "<strong>radiaal symmetrisch</strong> rond die as, wat betekent dat "
                  "<strong>de binding er van alle kanten rond de as hetzelfde uitziet</strong>."),
            ("p", "Daardoor <strong>kan een molecule vrij draaien rond een enkelvoudige "
                  "binding</strong>: <strong>de sigma-binding blijft bij draaien even goed "
                  "overlappen</strong>. Bij een pi-binding zou de overlapping juist verdwijnen."),
            ("p", "Een <strong>pi-binding</strong> ontstaat uit "
                  "<strong>de overlapping van twee p-orbitalen die naast elkaar staan</strong>, "
                  "boven en onder het vlak van de molecule. Ze "
                  "<strong>verhindert het draaien rond de binding</strong> en ze "
                  "<strong>is reactiever dan een sigma-binding</strong>. Een "
                  "<strong>pi-binding is ook zwakker</strong> dan een sigma-binding tussen dezelfde "
                  "atomen, want de zijdelingse overlapping is kleiner. Daarom breekt bij een "
                  "reactie meestal eerst de pi-binding."),
            ("p", "Tussen twee atomen ligt <strong>altijd precies één</strong> sigma-binding: "
                  "<strong>er kunnen geen meerdere sigma-bindingen naast elkaar liggen</strong>, "
                  "want de coaxiale plaats is maar één keer vrij. Een "
                  "<strong>dubbele binding</strong> heeft dus <strong>één</strong> pi-binding en "
                  "een <strong>drievoudige binding bestaat niet uit drie sigma-bindingen</strong> "
                  "maar uit <strong>één sigma en twee pi</strong>."),
            ("p", "Tellen op drie moleculen: <strong>methaan CH₄</strong> heeft "
                  "<strong>vier</strong> sigma-bindingen en geen pi, want het is verzadigd; "
                  "<strong>etheen CH₂=CH₂</strong> heeft "
                  "<strong>vijf sigma en één pi</strong>; <strong>ethyn HC≡CH</strong> heeft "
                  "<strong>drie sigma en twee pi</strong>."),
            ("p", "Komt er een pi-binding bij, dan <strong>wordt de bindingslengte korter, want de "
                  "atomen worden dichter naar elkaar getrokken</strong>: een C-C is ongeveer "
                  "154 pm, een C=C 134 pm en een C≡C 120 pm. Dat verklaart ook waarom "
                  "<strong>de drievoudige binding van stikstofgas zo moeilijk te breken is</strong>: "
                  "<strong>er moeten één sigma- en twee pi-bindingen samen verbroken worden</strong>, "
                  "en daarom kost kunstmest maken uit N₂ zoveel energie."),
            ("p", "Bij een <strong>alkeen</strong> is <strong>de dubbele binding reactiever dan een "
                  "enkelvoudige</strong> en <strong>kunnen de twee koolstofatomen niet vrij "
                  "draaien</strong>. Een alkeen is reactiever dan een alkaan omdat "
                  "<strong>de elektronen van de pi-binding open liggen voor een aanval</strong>. Bij "
                  "een <strong>additiereactie</strong> gaat dan ook "
                  "<strong>de pi-binding</strong> open en blijft de sigma-binding tussen de "
                  "koolstofatomen bestaan, zodat de molecule niet uiteenvalt. In een "
                  "<strong>benzeenring liggen de pi-elektronen over de hele ring "
                  "verspreid</strong>, en daardoor is benzeen stabieler dan drie losse dubbele "
                  "bindingen zouden doen vermoeden."),
        ]),
        dict(kop="Lewisstructuren en de octetregel", blokken=[
            ("p", "Een <strong>streepje tussen twee atomen</strong> in een "
                  "<strong>lewisstructuur</strong> stelt "
                  "<strong>een bindend elektronenpaar</strong> voor, dus twee elektronen die samen "
                  "de binding vormen. Een <strong>vrij paar</strong> tekent men als twee puntjes "
                  "naast het atoom. In <strong>één elektronenpaar</strong> zitten altijd "
                  "<strong>twee</strong> elektronen, bindend of vrij."),
            ("p", "De <strong>octetregel</strong> zegt dat "
                  "<strong>elk atoom streeft naar acht elektronen in zijn buitenste "
                  "niveau</strong>, en <strong>de vrije elektronenparen tellen daarvoor mee</strong>: "
                  "bij water heeft zuurstof twee bindende en twee vrije paren, samen acht. "
                  "<strong>Waterstof</strong> is de uitzondering: dat atoom is "
                  "<strong>tevreden met twee elektronen</strong>, de configuratie van helium. Een "
                  "<strong>koolstofatoom in een neutrale organische molecule heeft altijd "
                  "vier</strong> bindingen, enkelvoudig of niet."),
            ("p", "Vrije paren tellen is een vaardigheid op zich. Het zuurstofatoom in "
                  "<strong>water</strong> heeft <strong>twee</strong> vrije paren, het "
                  "stikstofatoom in <strong>ammoniak</strong> <strong>één</strong>, en elk "
                  "chlooratoom in <strong>Cl₂</strong> <strong>drie</strong>. Het koolstofatoom in "
                  "<strong>koolstofdioxide</strong> heeft "
                  "<strong>vier bindende elektronenparen, verdeeld over twee dubbele "
                  "bindingen</strong>: O=C=O, en zo komt koolstof aan zijn octet."),
            ("p", "Heeft een <strong>polyatomisch ion</strong> een lading van 2−, dan "
                  "<strong>zitten er twee elektronen meer in dan de neutrale atomen samen "
                  "hebben</strong>. Bij het sulfaation SO₄²⁻ reken je die twee dus mee bij het "
                  "verdelen over de bindingen en de vrije paren."),
        ]),
        dict(kop="Donor-acceptorbinding en formele lading", blokken=[
            ("p", "Bij een <strong>normale atoombinding</strong> "
                  "<strong>levert elk atoom één elektron voor het bindende paar</strong>. Bij een "
                  "<strong>donor-acceptorbinding</strong> "
                  "<strong>levert één atoom het hele elektronenpaar</strong>: het stikstofatoom van "
                  "ammoniak geeft zijn vrij paar aan een H⁺, en zo ontstaat het "
                  "<strong>ammoniumion NH₄⁺</strong>. Ook "
                  "<strong>in het hydroxoniumion H₃O⁺ zit een donor-acceptorbinding</strong>: het "
                  "zuurstofatoom van water geeft een vrij paar aan een H⁺, en daarna zijn de drie "
                  "bindingen niet meer van elkaar te onderscheiden."),
            ("p", "De <strong>formele lading</strong> van een atoom in een lewisstructuur bereken "
                  "je als <strong>de valentie-elektronen min de vrije elektronen min het aantal "
                  "bindingen</strong>. Voor het stikstofatoom in NH₄⁺ geeft 5 − 0 − 4 dus "
                  "<strong>+1</strong>, en dat verklaart de lading van het hele ion. Het "
                  "ammoniumion <strong>heeft vier bindende elektronenparen</strong> en geen vrij "
                  "paar meer."),
            ("p", "<strong>De formele lading is niet hetzelfde als het oxidatiegetal.</strong> Bij "
                  "de formele lading verdeel je de bindende elektronen eerlijk over de twee atomen; "
                  "bij het oxidatiegetal geef je ze helemaal aan het meest elektronegatieve atoom."),
        ]),
        dict(kop="Ionbinding en metaalbinding", blokken=[
            ("p", "Bij een <strong>ionbinding</strong> "
                  "<strong>worden elektronen volledig overgedragen</strong> en "
                  "<strong>trekken de deeltjes elkaar aan door hun lading</strong>: natrium geeft "
                  "zijn elektron aan chloor, en de <strong>coulombkracht</strong> tussen Na⁺ en Cl⁻ "
                  "houdt het rooster samen."),
            ("p", "De <strong>metaalbinding</strong> is de binding "
                  "<strong>tussen positieve metaalionen en vrij bewegende elektronen</strong>. Een "
                  "<strong>metaal geleidt stroom</strong> omdat "
                  "<strong>de valentie-elektronen vrij door het hele rooster bewegen</strong>. Die "
                  "elektronenzee verklaart ook waarom je een metaal kunt pletten zonder dat het "
                  "breekt."),
        ]),
    ],
    onthoud=[
        "Sigma is coaxiaal en draait vrij; pi overlapt zijdelings en zet vast.",
        "Dubbel is één sigma plus één pi, drievoudig één sigma plus twee pi.",
        "Meer bindingen betekent korter en sterker.",
        "Octet: bindende én vrije paren tellen mee; waterstof is tevreden met twee.",
        "Donor-acceptor: één atoom levert het hele paar (NH₄⁺, H₃O⁺).",
        "Formele lading = valentie-elektronen − vrije elektronen − bindingen.",
        "Ionbinding draagt elektronen over, metaalbinding heeft een elektronenzee.",
    ],
)

# ───────────────────── 6. Ruimtelijke structuur, polariteit en intermoleculaire krachten
BUNDELS["ruimtelijke-structuur-polariteit-en-intermoleculaire-krachten-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Ruimtelijke structuur, polariteit en intermoleculaire krachten",
    onder="Van sterisch getal naar vorm, van vorm naar polariteit, en van polariteit naar oplossen.",
    secties=[
        dict(kop="Het sterisch getal bepaalt de vorm", blokken=[
            ("p", "Het <strong>sterisch getal</strong> van een atoom is "
                  "<strong>het aantal bindingspartners plus het aantal vrije "
                  "elektronenparen</strong>. Bij water zijn dat twee partners en twee vrije paren, "
                  "dus sterisch getal vier. Een "
                  "<strong>dubbele binding telt als één bindingspartner</strong>, want "
                  "<strong>de twee bindingen wijzen samen naar hetzelfde buuratoom</strong>: het "
                  "sterisch getal telt richtingen rond het centrale atoom, niet bindingen."),
            ("p", "<strong>Het sterisch getal bepaalt zowel de ruimtelijke structuur als het "
                  "hybridisatietype.</strong> <strong>Sterisch getal 2</strong> geeft een "
                  "<strong>lineaire</strong> vorm van <strong>180°</strong> en "
                  "<strong>sp-hybridisatie</strong>, waarbij "
                  "<strong>een s-orbitaal en een p-orbitaal</strong> mengen. "
                  "<strong>Sterisch getal 3</strong> geeft een vlakke driehoek en "
                  "<strong>sp²</strong>, met een theoretische hoek van "
                  "<strong>120°</strong>. <strong>Sterisch getal 4</strong> geeft een "
                  "<strong>tetraëder</strong> en <strong>sp³</strong>, met een theoretische "
                  "bindingshoek van <strong>109,5°</strong>; bij sp³ "
                  "<strong>liggen de vier orbitalen niet in hetzelfde vlak</strong> maar wijzen ze "
                  "naar de hoeken van een tetraëder, terwijl sp²-orbitalen wel in één vlak liggen. "
                  "Een koolstofatoom met een <strong>dubbele binding</strong> heeft dus "
                  "<strong>sp²</strong>."),
            ("p", "De vrije paren beslissen daarna over de werkelijke vorm. "
                  "<strong>Een vrij elektronenpaar duwt harder op de bindingen dan een bindend "
                  "paar</strong>, want het hangt dichter bij het centrale atoom. De "
                  "<strong>werkelijke bindingshoek</strong> "
                  "<strong>is dus kleiner dan de theoretische als er vrije paren zijn</strong> en "
                  "<strong>gelijk aan de theoretische zonder vrije paren</strong>: methaan haalt "
                  "netjes 109,5°, <strong>ammoniak 107°</strong> en <strong>water 104,5°</strong>. "
                  "Daarom is de bindingshoek in ammoniak kleiner dan in methaan: "
                  "<strong>ammoniak heeft een vrij elektronenpaar dat de bindingen "
                  "samenduwt</strong>."),
            ("p", "Zo komen de vormen eruit. <strong>Water</strong> is "
                  "<strong>geknikt</strong>: twee bindingen en twee vrije paren, en die vorm maakt "
                  "water polair. Een centraal atoom met <strong>sterisch getal 4 en één vrij "
                  "elektronenpaar</strong> heeft <strong>drie</strong> bindingspartners en dus de "
                  "vorm van een piramide, zoals ammoniak. Een molecule met "
                  "<strong>sterisch getal 3 en één vrij paar is niet lineair</strong> maar vlak en "
                  "geknikt, zoals zwaveldioxide met een hoek van ongeveer 119°. Bij "
                  "<strong>koolstofdioxide</strong> is "
                  "<strong>het sterisch getal van koolstof twee</strong> en is "
                  "<strong>de molecule lineair</strong>. Het "
                  "<strong>ammoniumion NH₄⁺</strong> is "
                  "<strong>een tetraëder</strong>, want het vrije paar van stikstof is in de vierde "
                  "binding gaan zitten. Het zuurstofatoom in <strong>methanol CH₃-OH</strong> heeft "
                  "sterisch getal <strong>vier</strong>: twee partners en twee vrije paren, dus een "
                  "geknikte C-O-H-hoek."),
        ]),
        dict(kop="Polaire en apolaire moleculen", blokken=[
            ("p", "Een binding is <strong>polair</strong> "
                  "<strong>als de twee atomen een verschillende elektronegatieve waarde "
                  "hebben</strong>: het meest elektronegatieve atoom trekt het bindende paar naar "
                  "zich toe, en zo ontstaat er een kant met een klein negatief overschot."),
            ("p", "De vorm beslist daarna over de hele molecule. "
                  "<strong>Koolstofdioxide is apolair terwijl de bindingen polair zijn</strong>, "
                  "want <strong>de molecule is lineair, dus de twee dipolen heffen elkaar "
                  "op</strong>. Bij water lukt dat niet, want daar staan de bindingen in een hoek. "
                  "Het schoolvoorbeeld van een <strong>apolaire stof</strong> is "
                  "<strong>tetrachloormethaan CCl₄</strong>: de vier polaire C-Cl-bindingen staan "
                  "in een tetraëder en heffen elkaar precies op. Het schoolvoorbeeld van een "
                  "<strong>polair oplosmiddel</strong> is <strong>water</strong>; wasbenzine en "
                  "white spirit zijn de apolaire voorbeelden."),
        ]),
        dict(kop="De krachten tussen de moleculen", blokken=[
            ("p", "<strong>Intramoleculair</strong> is "
                  "<strong>binnen een molecule</strong>, dus de atoombinding zelf; "
                  "<strong>intermoleculair</strong> is "
                  "<strong>tussen moleculen</strong>, dus de krachten die moleculen bij elkaar "
                  "houden."),
            ("p", "De zwakste intermoleculaire kracht is de "
                  "<strong>londonkracht</strong> of <strong>dispersiekracht</strong>, en die werkt "
                  "<strong>tussen alle moleculen</strong>. Ze ontstaat doordat de elektronenwolk "
                  "kort verschuift, en bij grote moleculen is ze samen toch sterk genoeg voor een "
                  "hoog kookpunt. Daarom <strong>kookt pentaan bij een hogere temperatuur dan "
                  "butaan</strong>: <strong>de langere keten geeft meer contact en dus sterkere "
                  "londonkrachten</strong>. En daarom <strong>kookt een vertakt alkaan juist bij "
                  "een lagere temperatuur dan het onvertakte</strong> met dezelfde formule: een "
                  "bolle vertakte molecule raakt haar buren over een kleiner oppervlak."),
            ("p", "Een <strong>waterstofbrug</strong> ontstaat "
                  "<strong>als waterstof aan stikstof, zuurstof of fluor gebonden is</strong>. Die "
                  "drie atomen zijn klein en sterk elektronegatief, waardoor de waterstof bijna "
                  "bloot blijft en een vrij paar van de buur aantrekt. Een "
                  "<strong>waterstofbrug is sterker dan een gewone dipoolkracht</strong>: daarom "
                  "kookt water bij 100 °C, terwijl waterstofsulfide met bijna dezelfde massa al bij "
                  "−60 °C een gas is. Het is ook de "
                  "<strong>waterstofbrug</strong> die <strong>twee watermoleculen bij elkaar "
                  "houdt</strong>."),
            ("p", "Een <strong>ion</strong> wordt in water vastgehouden door de "
                  "<strong>ion-dipoolkracht</strong>: de negatieve kant van de watermoleculen gaat "
                  "rond een positief ion staan, en omgekeerd. De kracht tussen "
                  "<strong>twee tegengesteld geladen ionen</strong> heet de "
                  "<strong>coulombkracht</strong>; die is veel sterker dan de krachten tussen "
                  "moleculen, en daarom smelt een zout pas bij hoge temperatuur."),
        ]),
        dict(kop="Oplossen en de vier roosters", blokken=[
            ("p", "Gelijk lost op in gelijk. <strong>Keukenzout lost op in water</strong> omdat "
                  "<strong>de watermoleculen de ionen met ion-dipoolkrachten uit het rooster "
                  "trekken</strong>; rond elk ion komt een laagje watermoleculen te staan. In "
                  "<strong>wasbenzine</strong> lossen <strong>olie</strong> en "
                  "<strong>vet</strong> goed op, want dat zijn apolaire stoffen in een apolair "
                  "oplosmiddel; zout en suiker blijven liggen. "
                  "<strong>Ethanol is goed mengbaar met water en hexaan niet</strong>, want "
                  "<strong>ethanol heeft een OH-groep die waterstofbruggen met water vormt</strong> "
                  "en hexaan is helemaal apolair."),
            ("p", "Het <strong>atoomrooster</strong>, zoals <strong>diamant</strong>, heeft "
                  "<strong>het hoogste smeltpunt</strong>, want je moet echte atoombindingen "
                  "breken; bij een molecuulrooster volstaat het de zwakke krachten ertussen te "
                  "verbreken. Een <strong>ionrooster</strong> "
                  "<strong>geleidt stroom als het gesmolten is</strong> en "
                  "<strong>is hard maar breekbaar</strong>: in de vaste stof zitten de ionen vast, "
                  "en pas gesmolten of opgelost kunnen ze bewegen. Een "
                  "<strong>metaalrooster geleidt stroom ook in vaste toestand</strong>, want de "
                  "valentie-elektronen bewegen vrij door het hele rooster. Een "
                  "<strong>molecuulrooster geleidt juist niet</strong>: de moleculen zijn neutraal "
                  "en de elektronen zitten in hun bindingen vast, dus suiker en ijs geleiden niet."),
        ]),
    ],
    onthoud=[
        "Sterisch getal = bindingspartners + vrije paren; een dubbele telt als één.",
        "2 lineair sp 180°, 3 vlak sp² 120°, 4 tetraëder sp³ 109,5°.",
        "Elk vrij paar duwt de hoek kleiner: 109,5° — 107° — 104,5°.",
        "Polaire bindingen in een symmetrische vorm heffen elkaar op (CO₂, CCl₄).",
        "London werkt altijd; waterstofbrug bij H aan N, O of F.",
        "Gelijk lost op in gelijk.",
        "Atoomrooster smelt het hoogst; metaal geleidt vast, zout pas gesmolten.",
    ],
)

# ───────────────────── 7. Chemisch rekenen: mol, molaire massa en concentratie
BUNDELS["chemisch-rekenen-mol-molaire-massa-en-concentratie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch rekenen: mol, molaire massa en concentratie",
    onder="Van gram naar mol naar deeltjes, en van mol naar een concentratie in de beker.",
    secties=[
        dict(kop="De mol en het getal van Avogadro", blokken=[
            ("p", "In één mol van een stof zitten "
                  "<strong>6,022 × 10²³</strong> deeltjes. Dat is het "
                  "<strong>getal van Avogadro</strong>, en het geldt voor atomen, moleculen en "
                  "ionen evengoed. In <strong>2 mol</strong> zitten er dus "
                  "<strong>ongeveer 1,2 × 10²⁴</strong> moleculen: let op het verspringen van de "
                  "exponent bij het verdubbelen."),
            ("p", "De <strong>stofhoeveelheid</strong> heeft als "
                  "<strong>symbool n</strong> en als <strong>eenheid de mol</strong>. "
                  "<strong>Eén mol zuurstofgas en één mol waterstofgas bevatten evenveel "
                  "moleculen</strong>, want het aantal staat vast; hun massa verschilt wel, 32 gram "
                  "tegenover 2 gram."),
        ]),
        dict(kop="Molaire massa: van gram naar mol en terug", blokken=[
            ("p", "De <strong>molaire massa M</strong> is de massa van één mol, met als "
                  "<strong>eenheid gram per mol</strong>; de getalwaarde is dezelfde als die van de "
                  "molecuulmassa in atomaire eenheden. De formule die de stofhoeveelheid uit de "
                  "massa geeft, is <strong>n is gelijk aan m gedeeld door M</strong>, en omgekeerd "
                  "is <strong>m is n maal M</strong>."),
            ("p", "Je rekent de molaire massa uit door de atoommassa's op te tellen, elk zo vaak "
                  "als het element in de formule staat. Met H 1, C 12, O 16 en S 32 g/mol: "
                  "<strong>water H₂O is 18 g/mol</strong> (twee keer 1 plus 16), "
                  "<strong>zwavelzuur H₂SO₄ is 98 g/mol</strong> (2 plus 32 plus vier keer 16) en "
                  "koolstofdioxide is 44 g/mol. In één mol zwavelzuur zitten dan ook "
                  "<strong>vier mol</strong> zuurstofatomen, want per molecule zitten er vier."),
            ("p", "Vijf rekenvoorbeelden. <strong>36 gram water</strong> bij 18 g/mol is "
                  "<strong>2 mol</strong>. <strong>100 gram calciumcarbonaat</strong> bij 100 g/mol "
                  "is <strong>1 mol</strong>, met daarin één mol calciumionen en één mol "
                  "carbonaationen. <strong>0,5 mol koolstofdioxide</strong> bij 44 g/mol weegt "
                  "<strong>22 gram</strong>. <strong>2 mol natriumchloride</strong> bij 58,5 g/mol "
                  "weegt <strong>117 gram</strong>. En <strong>3 mol waterstofgas</strong> bij "
                  "2 g/mol weegt <strong>6 gram</strong>, want waterstofgas is H₂ en niet H."),
            ("p", "<strong>Twee stoffen met dezelfde massa bevatten dus niet altijd hetzelfde "
                  "aantal mol</strong>: achttien gram water is één mol, achttien gram glucose maar "
                  "een tiende van een mol. Van <strong>één mol ijzer</strong> geldt wel dat het "
                  "<strong>6,022 × 10²³ atomen bevat</strong> en dat het "
                  "<strong>56 gram weegt als de molaire massa 56 g/mol is</strong>: het aantal "
                  "deeltjes staat vast, de massa hangt af van het element."),
            ("p", "De <strong>massadichtheid</strong> is iets anders: daarvoor heb je "
                  "<strong>de massa van de stof</strong> en "
                  "<strong>het volume van de stof</strong> nodig. Haar eenheid is "
                  "<strong>gram per kubieke centimeter</strong>, voor water ongeveer 1 g/cm³ en "
                  "voor ijzer bijna 8."),
            ("p", "Eén mol gas neemt bij <strong>normomstandigheden</strong> "
                  "<strong>22,4 liter</strong> in, het <strong>molair volume</strong> bij 0 °C en "
                  "normale druk. Dat is voor elk gas ongeveer gelijk, maar het geldt "
                  "<strong>niet bij elke temperatuur</strong>: warm je het gas op, dan zet het uit "
                  "en neemt het meer plaats in."),
        ]),
        dict(kop="Concentratie uitdrukken", blokken=[
            ("p", "De <strong>molaire concentratie</strong> heeft als symbool "
                  "<strong>c</strong> en als eenheid mol per liter, die men ook als M schrijft "
                  "(0,1 M zoutzuur). De formule is <strong>c is n gedeeld door V</strong>, met het "
                  "<strong>volume altijd in liter</strong>: "
                  "<strong>250 milliliter is 0,25 liter</strong>. Zo is een oplossing met "
                  "<strong>0,5 mol in 2 liter</strong> <strong>0,25 mol/L</strong> sterk, zit er in "
                  "<strong>500 mL van 0,2 mol/L</strong> <strong>0,1 mol</strong> opgeloste stof, en "
                  "weeg je voor <strong>250 mL van 0,4 mol/L</strong> "
                  "<strong>0,1 mol</strong> stof af."),
            ("p", "<strong>Een oplossing van 1 mol/L bevat niet altijd één mol</strong>: ze bevat "
                  "één mol per liter, dus in 100 mL heb je maar 0,1 mol in handen."),
            ("p", "Naast de molaire concentratie bestaan er uitdrukkingen in massa en volume. De "
                  "<strong>massaconcentratie</strong> en het "
                  "<strong>massaprocent</strong> gebruiken "
                  "<strong>een massa in de teller</strong>. Een "
                  "<strong>massaprocent van 5 %</strong> betekent "
                  "<strong>5 gram opgeloste stof per 100 gram oplossing</strong>, dus de massa van "
                  "het oplosmiddel én van de opgeloste stof samen: in "
                  "<strong>200 gram oplossing van 10 massaprocent</strong> zit "
                  "<strong>20 gram</strong> zout en 180 gram water. Een "
                  "<strong>wijn van 12 volumeprocent</strong> bevat "
                  "<strong>12 mL alcohol per 100 mL wijn</strong>."),
            ("p", "Voor heel kleine hoeveelheden gebruikt men kleinere eenheden. "
                  "<strong>Procent</strong> is op honderd, "
                  "<strong>promille betekent één deel op duizend</strong>, "
                  "<strong>1 ppm</strong> is <strong>één deel op een miljoen</strong> en, omdat een "
                  "liter water duizend gram weegt, ook "
                  "<strong>1 milligram per liter water</strong>. <strong>Ppb</strong> "
                  "<strong>staat voor één deel op een miljard</strong> en "
                  "<strong>wordt gebruikt voor heel kleine hoeveelheden</strong>, zoals een spoor "
                  "van een zwaar metaal in drinkwater."),
            ("p", "Twee praktische punten. Je <strong>vult bij het maken van een oplossing aan tot "
                  "de maatstreep</strong> en meet niet eerst het water af, want "
                  "<strong>de opgeloste stof neemt zelf ook plaats in het eindvolume</strong>: de "
                  "concentratie hoort bij het volume van de oplossing. En "
                  "<strong>het massaprocent verandert wél als je er water bij giet</strong>, want "
                  "de massa van de oplossing wordt groter terwijl die van de opgeloste stof gelijk "
                  "blijft."),
        ]),
        dict(kop="Verdunnen en een formule uit percentages", blokken=[
            ("p", "<strong>Bij het verdunnen van een oplossing blijft het aantal mol opgeloste stof "
                  "gelijk</strong>: je giet er enkel water bij. Daarom geldt de "
                  "<strong>verdunningsregel</strong>: "
                  "<strong>c₁ maal V₁ is gelijk aan c₂ maal V₂</strong>. Verdun je "
                  "<strong>10 mL van 2 mol/L tot 100 mL</strong>, dan wordt het volume tien keer "
                  "groter en de concentratie tien keer kleiner: "
                  "<strong>0,2 mol/L</strong>."),
            ("p", "Uit massapercentages vind je een formule door elk percentage door de atoommassa "
                  "te delen. Bij <strong>40 % koolstof, 6,7 % waterstof en 53,3 % zuurstof</strong> "
                  "geeft 40/12, 6,7/1 en 53,3/16 ongeveer 3,3 : 6,7 : 3,3, dus 1 : 2 : 1 en de "
                  "formule <strong>CH₂O</strong>. Omgekeerd zit er in water "
                  "<strong>ongeveer 11 %</strong> waterstof in massa: twee gram op achttien. Het "
                  "aantal atomen en de massa zijn dus twee verschillende dingen."),
        ]),
    ],
    onthoud=[
        "Eén mol is 6,022 × 10²³ deeltjes, het getal van Avogadro.",
        "n = m / M en m = n · M; M in gram per mol.",
        "Eén mol gas is 22,4 liter, maar enkel bij normomstandigheden.",
        "c = n / V, met V altijd in liter.",
        "Massaprocent rekent per 100 gram oplossing, niet per 100 gram water.",
        "ppm is één op een miljoen, ppb één op een miljard.",
        "Verdunnen: c₁V₁ = c₂V₂, want het aantal mol blijft gelijk.",
    ],
)

# ───────────────────── 8. Stoichiometrie, overmaat en de algemene gaswet
BUNDELS["stoichiometrie-overmaat-en-de-algemene-gaswet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stoichiometrie, overmaat en de algemene gaswet",
    onder="Uitbalanceren, rekenen met de verhouding, en wat een gas met druk en warmte doet.",
    secties=[
        dict(kop="Uitbalanceren", blokken=[
            ("p", "Een reactievergelijking moet uitgebalanceerd zijn, want "
                  "<strong>er mogen geen atomen bijkomen of verdwijnen tijdens een "
                  "reactie</strong>. Bindingen worden verbroken en gemaakt, maar de atomen blijven "
                  "bestaan: dat is de <strong>wet van het behoud van massa</strong>. In een "
                  "uitgebalanceerde vergelijking "
                  "<strong>staat links en rechts evenveel atomen van elk element</strong>; het "
                  "aantal moleculen hoeft niet gelijk te zijn."),
            ("p", "<strong>Je mag de formule van een stof nooit aanpassen om uit te "
                  "balanceren.</strong> Je zet alleen <strong>coëfficiënten</strong> voor de "
                  "formules."),
            ("p", "Drie vergelijkingen om te kennen. Het verbranden van methaan is "
                  "<strong>CH₄ + 2 O₂ → CO₂ + 2 H₂O</strong>: de coëfficiënt voor "
                  "<strong>H₂O</strong> is <strong>2</strong>, want methaan heeft vier "
                  "waterstofatomen en elke watermolecule gebruikt er twee. Bij propaan, "
                  "C₃H₈ + … O₂ → 3 CO₂ + 4 H₂O, is de coëfficiënt voor O₂ "
                  "<strong>5</strong>: rechts staan zes plus vier, dus tien zuurstofatomen. De "
                  "vorming van aluminiumoxide is "
                  "<strong>4 Al + 3 O₂ → 2 Al₂O₃</strong>."),
            ("p", "Bij een verbranding <strong>balanceer je de zuurstof meestal het laatst</strong>, "
                  "want <strong>zuurstof komt in meerdere producten voor en past zich het "
                  "makkelijkst aan</strong>: staan koolstof en waterstof goed, dan ligt het aantal "
                  "zuurstofatomen rechts vast."),
        ]),
        dict(kop="Rekenen met de verhouding", blokken=[
            ("p", "<strong>De coëfficiënten van een reactievergelijking geven de verhouding in "
                  "mol</strong>, niet in gram. Daarom is "
                  "<strong>de eerste stap bij een stoichiometrische berekening met massa's: de "
                  "gegeven massa omrekenen naar een stofhoeveelheid in mol</strong>. Bij een "
                  "berekening van massa naar massa doe je dus "
                  "<strong>eerst omrekenen van gram naar mol</strong> en "
                  "<strong>daarna de verhouding uit de vergelijking gebruiken</strong>, en pas "
                  "daarna terug naar gram. Gram, mol, verhouding, mol, gram: dat is de hele weg."),
            ("p", "Oefen de verhouding op "
                  "<strong>N₂ + 3 H₂ → 2 NH₃</strong>, dus 1 op 3 op 2. Uit "
                  "<strong>1 mol stikstofgas</strong> ontstaat "
                  "<strong>2 mol</strong> ammoniak, en voor "
                  "<strong>2 mol ammoniak</strong> is <strong>3 mol</strong> waterstofgas nodig."),
            ("p", "En op <strong>2 H₂ + O₂ → 2 H₂O</strong>, dus 2 op 1 op 2. Voor "
                  "<strong>4 mol waterstofgas</strong> is "
                  "<strong>2 mol</strong> zuurstofgas nodig, en uit "
                  "<strong>3 mol waterstofgas</strong> komt <strong>3 mol</strong> water, want "
                  "waterstofgas en water staan één op één."),
            ("p", "Bij <strong>2 Mg + O₂ → 2 MgO</strong> geldt: "
                  "<strong>per 2 mol magnesium is er 1 mol zuurstofgas nodig</strong> en "
                  "<strong>er ontstaat evenveel mol magnesiumoxide als er magnesium "
                  "reageert</strong>. Uit <strong>2 mol magnesium</strong> komt bij M(MgO) "
                  "40 g/mol dus <strong>80 gram</strong> magnesiumoxide. Bij de ontleding "
                  "<strong>CaCO₃ → CaO + CO₂</strong> geeft <strong>100 gram kalksteen</strong> "
                  "(M 100 g/mol) <strong>1 mol</strong> koolstofdioxide. En voor het volledig "
                  "verbranden van <strong>1 mol propaan C₃H₈</strong> is "
                  "<strong>5 mol</strong> zuurstofgas nodig."),
        ]),
        dict(kop="Limiterend reagens en overmaat", blokken=[
            ("p", "Het <strong>limiterend reagens</strong> of "
                  "<strong>beperkend reagens</strong> is "
                  "<strong>de stof die als eerste opgebruikt is en de reactie stopzet</strong>. Ze "
                  "bepaalt hoeveel product er maximaal kan ontstaan. "
                  "<strong>Bij een aflopende reactie blijft er dus niet van elke beginstof iets "
                  "over</strong>: de reactie gaat door tot minstens één beginstof op is."),
            ("p", "Je vindt het limiterend reagens door "
                  "<strong>van elke stof het aantal mol door haar coëfficiënt te delen</strong>; de "
                  "kleinste uitkomst hoort bij het beperkend reagens. "
                  "<strong>Het is dus niet altijd de stof waarvan je het minste mol hebt</strong>, "
                  "want de coëfficiënten tellen mee. Met "
                  "<strong>1 mol N₂ en 6 mol H₂</strong> voor N₂ + 3 H₂ → 2 NH₃ geeft 1/1 = 1 en "
                  "6/3 = 2, dus is <strong>het stikstofgas</strong> beperkend."),
            ("p", "Laat je <strong>2 mol H₂ met 2 mol O₂</strong> reageren volgens "
                  "2 H₂ + O₂ → 2 H₂O, dan is <strong>het zuurstofgas in overmaat</strong> en "
                  "ontstaat er <strong>2 mol</strong> water; één mol zuurstofgas blijft over. "
                  "Algemeen geldt: <strong>van de stof in overmaat blijft er na de reactie "
                  "over</strong> en <strong>de stof in overmaat bepaalt niet hoeveel product er "
                  "ontstaat</strong>. In de industrie werkt men daarom soms "
                  "<strong>met een overmaat van de goedkoopste stof</strong>, "
                  "<strong>zodat de dure stof zo volledig mogelijk wegreageert</strong>; het "
                  "overschot wordt vaak hergebruikt."),
        ]),
        dict(kop="De algemene gaswet", blokken=[
            ("p", "De <strong>algemene gaswet</strong> is "
                  "<strong>p maal V is gelijk aan n maal R maal T</strong>, met R de algemene "
                  "gasconstante. De temperatuur moet "
                  "<strong>in kelvin</strong> staan, want nul kelvin is het absolute nulpunt: "
                  "<strong>27 °C is 300 K</strong> en 25 °C is 298 K. "
                  "<strong>De wet geldt ook voor een mengsel van gassen, met n het totale aantal "
                  "mol</strong>, zoals bij lucht."),
            ("p", "Bij de <strong>normomstandigheden</strong> is "
                  "<strong>de temperatuur 0 °C of 273 K</strong> en neemt "
                  "<strong>één mol gas er 22,4 liter</strong> in; bij 25 °C is het molair volume "
                  "ongeveer 24,5 liter, dus spreek altijd af welke omstandigheden je bedoelt. "
                  "<strong>2 mol gas</strong> neemt er <strong>44,8 L</strong> in, "
                  "<strong>11,2 liter</strong> hoort bij <strong>0,5 mol</strong>, en de "
                  "<strong>1 mol CO₂</strong> uit de ontleding van kalksteen is "
                  "<strong>22,4 liter</strong> gas; in een warme oven is dat volume groter."),
            ("p", "<strong>Twee verschillende gassen nemen bij dezelfde druk en temperatuur "
                  "evenveel plaats in per mol</strong>: dat is de kern van de "
                  "<strong>wet van Avogadro</strong>, want de grootte van de moleculen speelt bij "
                  "een gas bijna geen rol."),
            ("p", "De wet zegt ook wat er bij verandering gebeurt. "
                  "<strong>Verdubbel je de temperatuur bij gelijke druk, dan verdubbelt het "
                  "volume, als je de temperatuur in kelvin rekent</strong>, want V en T staan aan "
                  "weerszijden van het gelijkheidsteken. "
                  "<strong>Bij hogere druk neemt een gas juist minder plaats in</strong>, want p en "
                  "V staan aan dezelfde kant."),
        ]),
    ],
    onthoud=[
        "Uitbalanceren: evenveel atomen links en rechts, enkel coëfficiënten aanpassen.",
        "De coëfficiënten geven een verhouding in mol, nooit in gram.",
        "Gram → mol → verhouding → mol → gram.",
        "Limiterend reagens: deel het aantal mol door de coëfficiënt, kleinste wint.",
        "De stof in overmaat blijft over en bepaalt de opbrengst niet.",
        "pV = nRT, met T altijd in kelvin.",
        "Eén mol gas is 22,4 liter bij 0 °C; warmer betekent meer volume.",
    ],
)

# ───────────────────── 9. Reactiesnelheid, botsingsmodel en energiediagram
BUNDELS["reactiesnelheid-botsingsmodel-en-energiediagram-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Reactiesnelheid, botsingsmodel en energiediagram",
    onder="Waarom botsingen wel of niet lukken, en wat een berg in een diagram betekent.",
    secties=[
        dict(kop="Snelheid meten", blokken=[
            ("p", "De snelheid van een reactie druk je uit "
                  "<strong>als de verandering van een concentratie per tijdseenheid</strong>, dus "
                  "in <strong>mol/(L·s)</strong>: de mol per liter staat in de teller en de seconde "
                  "in de noemer. Je kan ook het aantal effectieve botsingen per tijdseenheid nemen."),
            ("p", "In een <strong>concentratie-tijdgrafiek</strong> zet je "
                  "<strong>de tijd op de horizontale as</strong> en "
                  "<strong>de concentratie op de verticale as</strong>. Uit "
                  "<strong>de steilheid</strong> lees je "
                  "<strong>de snelheid van de reactie op dat ogenblik</strong>: een steile kromme "
                  "betekent een hoge snelheid, een vlakke kromme een trage reactie. "
                  "<strong>Een reactie verloopt in het begin meestal het snelst</strong>, want dan "
                  "is de concentratie van de reagentia het hoogst; naar het einde toe vlakt de "
                  "kromme af."),
        ]),
        dict(kop="Het botsingsmodel", blokken=[
            ("p", "<strong>Een reactie kan niet verlopen als de deeltjes elkaar nooit "
                  "raken.</strong> Dat is de kern van het <strong>botsingsmodel</strong>, en "
                  "daarom roer je, verwarm je of maal je een stof fijn. Een "
                  "<strong>effectieve botsing</strong> is "
                  "<strong>een botsing met genoeg energie en de juiste stand om te "
                  "reageren</strong>; beide voorwaarden moeten kloppen. Een botsing die er niet aan "
                  "voldoet, heet <strong>elastisch</strong> of niet-effectief: de deeltjes ketsen "
                  "af en er gebeurt niets. Verreweg de meeste botsingen zijn van dat soort."),
            ("p", "De <strong>activeringsenergie</strong> of "
                  "<strong>activeringsdrempel</strong> is "
                  "<strong>de energie die een botsing minstens moet hebben om te kunnen "
                  "reageren</strong>. De <strong>Boltzmannverdeling</strong> "
                  "<strong>toont hoe de energie over de deeltjes verdeeld is</strong>, want niet "
                  "alle deeltjes hebben dezelfde energie, en "
                  "<strong>bij een hogere temperatuur schuift ze naar rechts</strong>: er komen dus "
                  "meer deeltjes boven de activeringsenergie uit."),
            ("p", "Wat maakt een reactie sneller? "
                  "<strong>Een hogere concentratie van de reagentia</strong> en "
                  "<strong>een fijnere verdeling van een vaste stof</strong>; verdunnen of afkoelen "
                  "doet het omgekeerde. Een <strong>poeder reageert sneller dan één groot "
                  "stuk</strong> omdat het <strong>een veel groter contactoppervlak</strong> heeft: "
                  "dat is de <strong>verdelingsgraad</strong>, en daarom is meelstof in een silo zo "
                  "gevaarlijk. Bij een hogere temperatuur "
                  "<strong>botsen de deeltjes niet alleen vaker, maar ook harder</strong>, en dat "
                  "tweede weegt het zwaarst. Daarom <strong>staat voedsel langer goed in de "
                  "koelkast</strong>: <strong>bij een lagere temperatuur verlopen de reacties van "
                  "bederf trager</strong>, al stoppen ze niet, vandaar een houdbaarheidsdatum. Ook "
                  "<strong>licht versnelt sommige reacties</strong>, want "
                  "<strong>het levert de energie om een binding te verbreken</strong>: daarom staat "
                  "zuurstofwater in een donkere fles."),
            ("p", "Een <strong>katalysator</strong> "
                  "<strong>verlaagt de activeringsenergie, zodat meer botsingen effectief "
                  "zijn</strong>, en <strong>wordt tijdens de reactie niet verbruikt</strong>: hij "
                  "doet mee en komt er onveranderd weer uit, en daarom schrijft men hem boven de "
                  "pijl. <strong>Een katalysator wordt dus niet opgebruikt</strong>, en een kleine "
                  "hoeveelheid kan heel veel reactie op gang brengen. Een katalysator die in een "
                  "levend organisme werkt, heet een <strong>enzym</strong> of "
                  "<strong>biokatalysator</strong>. Een enzym werkt maar op één soort stof omdat "
                  "<strong>de vorm van zijn actieve plaats op één soort molecule past</strong>: dat "
                  "is de <strong>specificiteit</strong>, en door hitte of een scheve pH verandert "
                  "die vorm."),
        ]),
        dict(kop="Het energiediagram", blokken=[
            ("p", "De <strong>activeringsenergie</strong> in een energiediagram is "
                  "<strong>de energie die nodig is om de reactie op gang te brengen</strong>: de "
                  "hoogte van de berg die de deeltjes over moeten. De top heet het "
                  "<strong>geactiveerd complex</strong>, "
                  "<strong>de onstabiele toestand op de top van het energiediagram</strong>, waar "
                  "de oude bindingen half verbroken en de nieuwe half gevormd zijn; het bestaat maar "
                  "heel kort."),
            ("p", "De <strong>reactie-energie</strong> bepaal je "
                  "<strong>als het verschil in energie tussen producten en reagentia</strong>. "
                  "Liggen <strong>de producten lager dan de reagentia</strong>, dan is "
                  "<strong>de reactie exo-energetisch en zet ze energie vrij</strong>; zo'n reactie "
                  "heet <strong>exotherm</strong> of exo-energetisch. Bij een "
                  "<strong>endo-energetische reactie</strong> "
                  "<strong>liggen de producten hoger in energie dan de reagentia</strong> en "
                  "<strong>koelt de omgeving tijdens de reactie af</strong>: een koudepakje in de "
                  "sportzaal werkt op dat principe."),
            ("p", "<strong>Een exo-energetische reactie verloopt niet altijd snel.</strong> De "
                  "reactie-energie en de activeringsenergie zijn twee verschillende dingen: benzine "
                  "geeft veel energie en heeft toch een vlam nodig. Zet je een katalysator in het "
                  "diagram, dan <strong>komt de top van de berg lager te liggen</strong> maar "
                  "<strong>blijven het begin- en eindpunt op dezelfde hoogte</strong>: een "
                  "katalysator verandert de weg, niet de bestemming."),
        ]),
        dict(kop="De snelheidsvergelijking", blokken=[
            ("p", "Voor een <strong>eenstapsreactie A + B → C</strong> is de "
                  "snelheidsvergelijking <strong>v is k maal [A] maal [B]</strong>: bij één stap "
                  "zijn de exponenten gelijk aan de coëfficiënten. "
                  "<strong>Bij een meerstapsreactie volgt de orde van een reagens uit "
                  "meetresultaten</strong>: je meet wat er met de snelheid gebeurt als je één "
                  "concentratie verandert."),
            ("p", "De <strong>orde</strong> lees je zo af. Verdubbel je een concentratie en "
                  "<strong>verdubbelt de snelheid</strong>, dan is de reactie van "
                  "<strong>eerste orde</strong> in die stof. Wordt de snelheid "
                  "<strong>vier keer groter</strong>, dan is het <strong>tweede orde</strong>, want "
                  "twee tot de macht twee is vier. <strong>Blijft de snelheid gelijk, dan is de "
                  "reactie van nulde orde</strong> in die stof, want alles tot de macht nul is één; "
                  "zo'n stof komt niet voor in de snelheidsbepalende stap. De "
                  "<strong>totale orde</strong> is de som van de exponenten: bij "
                  "<strong>v is k maal [A]² maal [B]</strong> is dat "
                  "<strong>drie</strong>."),
            ("p", "De letter <strong>k</strong> staat voor de "
                  "<strong>snelheidsconstante</strong>. Ze "
                  "<strong>wordt groter bij een hogere temperatuur</strong> en "
                  "<strong>haar eenheid hangt af van de orde van de reactie</strong>: bij "
                  "<strong>eerste orde</strong> is dat <strong>per seconde</strong>, want links "
                  "staat mol/(L·s) en [A] levert al mol/L. "
                  "<strong>Een katalysator laat k niet onveranderd</strong>: door de lagere "
                  "activeringsenergie wordt k juist groter, en ook de orde kan veranderen, want de "
                  "weg is een andere."),
        ]),
    ],
    onthoud=[
        "Snelheid is concentratieverandering per tijd, in mol/(L·s).",
        "Effectief = genoeg energie én de juiste stand; anders elastisch.",
        "Concentratie, verdelingsgraad, temperatuur, licht en katalysator versnellen.",
        "Een katalysator verlaagt de drempel en wordt niet verbruikt.",
        "Activeringsenergie is de berg, reactie-energie het hoogteverschil.",
        "Exo-energetisch zegt niets over de snelheid.",
        "v = k·[A]^x·[B]^y; de orde meet je, behalve bij één stap.",
    ],
)

# ───────────────────── 10. Chemisch evenwicht en de wet van Le Chatelier
BUNDELS["chemisch-evenwicht-en-de-wet-van-le-chatelier-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch evenwicht en de wet van Le Chatelier",
    onder="Twee reacties die even snel lopen, en wat er gebeurt als je eraan komt.",
    secties=[
        dict(kop="Wat een evenwicht is", blokken=[
            ("p", "Een <strong>chemisch evenwicht</strong> is "
                  "<strong>dynamisch</strong>: <strong>de heen- en de terugreactie blijven "
                  "doorgaan, even snel</strong>. Van buitenaf lijkt er niets te gebeuren, want "
                  "<strong>de concentraties blijven constant</strong> en "
                  "<strong>er zijn nog van alle stoffen aanwezig</strong>. Bij een aflopende "
                  "reactie is minstens één beginstof op. Je schrijft een evenwicht met een "
                  "<strong>dubbele pijl ⇌</strong>, twee pijlen in tegengestelde richting; een "
                  "enkele pijl staat voor een aflopende reactie. De reactie die "
                  "<strong>van rechts naar links</strong> verloopt, heet de "
                  "<strong>terugreactie</strong>."),
            ("p", "Op het ogenblik dat het evenwicht bereikt wordt, "
                  "<strong>is de snelheid van de heenreactie gelijk aan die van de "
                  "terugreactie</strong> en <strong>veranderen de concentraties vanaf dan niet "
                  "meer</strong>. In het begin is de heenreactie het snelst; terwijl er product "
                  "bijkomt, wordt de terugreactie sneller, tot de twee gelijk zijn."),
            ("p", "<strong>De concentraties van reagentia en producten zijn daarbij niet gelijk aan "
                  "elkaar</strong>: ze zijn constant. Vaak ligt het evenwicht sterk aan één kant. "
                  "In het labo zie je dat een reactie een evenwicht is doordat "
                  "<strong>er van elke beginstof iets overblijft, hoelang je ook wacht</strong>, of "
                  "doordat het mengsel de andere kant op gaat als je een product toevoegt. "
                  "<strong>Een mengsel waarin niets gebeurt, is daarom nog geen chemisch "
                  "evenwicht</strong>: misschien is er geen reactie mogelijk of is de drempel te "
                  "hoog. Een evenwicht kan je ook "
                  "<strong>van twee kanten bereiken: vanuit de reagentia of vanuit de "
                  "producten</strong>, en je komt bij dezelfde verhouding uit. Blijft in een "
                  "evenwicht van een gekleurde met een kleurloze stof de kleur gelijk, dan "
                  "<strong>verandert de verhouding tussen de twee stoffen niet meer</strong>."),
        ]),
        dict(kop="De evenwichtsconstante", blokken=[
            ("p", "Voor het evenwicht <strong>A + 2 B ⇌ C</strong> is "
                  "<strong>K gelijk aan [C] gedeeld door [A] maal [B]²</strong>: de producten komen "
                  "in de teller, de reagentia in de noemer, en "
                  "<strong>de coëfficiënten staan als exponent</strong>. Bij "
                  "N₂ + 3 H₂ ⇌ 2 NH₃ wordt dat [NH₃]² gedeeld door [N₂] maal [H₂]³."),
            ("p", "De <strong>evenwichtsconstante</strong> "
                  "<strong>verandert enkel met de temperatuur</strong> en "
                  "<strong>heeft de producten in de teller</strong>. Is ze "
                  "<strong>heel groot</strong>, dan "
                  "<strong>ligt het evenwicht sterk aan de kant van de producten</strong>; is ze "
                  "<strong>gelijk aan 1</strong>, dan "
                  "<strong>zijn teller en noemer ongeveer even groot</strong> en ligt het evenwicht "
                  "in het midden. Een K van duizend ligt rechts, een K van een duizendste links. "
                  "<strong>Een hoge K zegt niets over de snelheid</strong>, want "
                  "<strong>K gaat over de verhouding in het evenwicht, niet over de weg "
                  "ernaartoe</strong>."),
            ("p", "Het <strong>reactiequotiënt Q</strong> heeft dezelfde vorm als K, maar met de "
                  "concentraties van dat ogenblik. Is <strong>Q kleiner dan K</strong>, dan "
                  "<strong>verloopt de reactie verder naar rechts, naar meer product</strong>, tot "
                  "Q gelijk is aan K."),
            ("p", "De <strong>omzettingsgraad</strong> is "
                  "<strong>het deel van een beginstof dat werkelijk gereageerd heeft</strong>: "
                  "heeft 0,2 mol van 1 mol gereageerd, dan is dat 20 procent. Bij een evenwicht "
                  "blijft die altijd onder de honderd procent. Het "
                  "<strong>rendement</strong> is "
                  "<strong>de werkelijke opbrengst gedeeld door de theoretische "
                  "opbrengst</strong>: 8 gram van de 10 mogelijke is 80 procent."),
        ]),
        dict(kop="De wet van Le Chatelier-Van 't Hoff", blokken=[
            ("p", "De <strong>wet van Le Chatelier-Van 't Hoff</strong> zegt dat "
                  "<strong>een verstoord evenwicht verschuift zo dat het de verstoring "
                  "tegenwerkt</strong>. Voeg je iets toe, dan wordt het deels weggewerkt; neem je "
                  "iets weg, dan wordt het deels bijgemaakt. Bij een verstoring "
                  "<strong>zijn de snelheden van heen- en terugreactie even tijdelijk "
                  "verschillend</strong> en <strong>zijn de twee na een tijd weer gelijk</strong>."),
            ("p", "<strong>Extra reagens</strong> toevoegen stuurt het evenwicht "
                  "<strong>naar rechts, naar meer producten</strong>. Een "
                  "<strong>product wegnemen</strong> stuurt het ook "
                  "<strong>naar rechts</strong>. Daarom "
                  "<strong>haalt men in de industrie het product voortdurend uit het "
                  "mengsel</strong>: <strong>zo blijft het evenwicht naar rechts werken en reageert "
                  "er meer weg</strong>, want Q blijft kleiner dan K."),
            ("p", "Druk werkt enkel bij gassen. Maak je "
                  "<strong>het volume van een gasevenwicht kleiner</strong>, dan gaat het "
                  "<strong>naar de kant met het minste aantal mol gas</strong>, want minder volume "
                  "betekent meer druk. <strong>Verlaag je de druk</strong>, dan gaat het "
                  "<strong>naar meer gas</strong>. In <strong>N₂ + 3 H₂ ⇌ 2 NH₃</strong> "
                  "<strong>neemt de hoeveelheid ammoniak bij hogere druk toe, want rechts staan "
                  "minder mol gas</strong>: links vier, rechts twee, en daarom werkt de industrie "
                  "bij hoge druk. <strong>Een evenwicht met links en rechts evenveel mol gas "
                  "verschuift niet door een drukverandering.</strong>"),
            ("p", "De temperatuur is bijzonder: zij is "
                  "<strong>de enige verstoring die de waarde van de evenwichtsconstante "
                  "verandert</strong>. Bij een temperatuurverandering "
                  "<strong>krijgt de evenwichtsconstante een andere waarde</strong> én "
                  "<strong>verschuift het evenwicht naar één kant</strong>. Verwarm je een "
                  "<strong>exo-energetisch evenwicht</strong>, dan gaat het "
                  "<strong>naar links, want de endo-energetische richting werkt de warmte "
                  "weg</strong>. Wordt een gekleurd evenwicht lichter bij verwarmen, dan is "
                  "<strong>de reactie naar de kleurloze kant endo-energetisch</strong>."),
            ("p", "Een <strong>katalysator verschuift het evenwicht niet</strong> naar de "
                  "producten: hij versnelt heen- en terugreactie evenveel, dus "
                  "<strong>wordt het evenwicht sneller bereikt, op dezelfde plaats</strong>. "
                  "<strong>Bij het toevoegen van een reagens verandert de evenwichtsconstante "
                  "evenmin</strong>: het evenwicht verschuift juist om K weer te laten uitkomen. "
                  "Samengevat: <strong>de ligging van een evenwicht kan je met druk, concentratie "
                  "en temperatuur beïnvloeden</strong>, en de verstoringen die een gasevenwicht "
                  "doen verschuiven zijn onder meer "
                  "<strong>het volume van het vat verkleinen</strong> en "
                  "<strong>de temperatuur verhogen</strong>."),
        ]),
    ],
    onthoud=[
        "Dynamisch evenwicht: heen en terug lopen even snel, de concentraties staan stil.",
        "K: producten boven, reagentia onder, coëfficiënten als exponent.",
        "Grote K betekent veel product, maar zegt niets over de snelheid.",
        "Q kleiner dan K: de reactie loopt verder naar rechts.",
        "Le Chatelier: het evenwicht werkt elke verstoring tegen.",
        "Meer druk stuurt naar de kant met het minste mol gas.",
        "Alleen de temperatuur verandert K; een katalysator verschuift niets.",
    ],
)

# ───────────────────── 11. Zuren en basen en het doorgeven van protonen
BUNDELS["zuren-en-basen-en-het-doorgeven-van-protonen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Zuren en basen en het doorgeven van protonen",
    onder="Het model van Brønsted-Lowry: geconjugeerde paren, amfolyten, sterk en zwak.",
    secties=[
        dict(kop="Zuur en base volgens Brønsted-Lowry", blokken=[
            ("p", "Een <strong>zuur volgens Brønsted-Lowry</strong> is "
                  "<strong>een stof die een proton kan afstaan</strong>; een proton is hier een "
                  "H⁺-ion. Een <strong>base</strong> is het omgekeerde: ze neemt dat proton op. "
                  "<strong>Een base moet dus niet altijd een hydroxidegroep bevatten</strong>: "
                  "ammoniak heeft geen OH en is toch een base."),
            ("p", "Bij een <strong>protolysereactie</strong> "
                  "<strong>gaat een proton van het zuur naar de base</strong>. Daarom heeft een "
                  "protolyse altijd een zuur én een base nodig, en "
                  "<strong>kan een stof alleen zuur zijn als er een base aanwezig is die het proton "
                  "opneemt</strong>: zuiver zwavelzuur zonder water ioniseert niet."),
            ("p", "Neemt water een proton op, dan ontstaat het "
                  "<strong>hydroxoniumion H₃O⁺</strong>. Daarom schrijft men de ionisatie van een "
                  "zuur in water met het hydroxoniumion en niet met een los H⁺. Het "
                  "<strong>hydroxoniumion kan zelf geen base zijn</strong>: het heeft al een proton "
                  "te veel en staat het liever af, en het is dus het sterkste zuur dat in water kan "
                  "bestaan."),
        ]),
        dict(kop="Geconjugeerde paren", blokken=[
            ("p", "Twee deeltjes die <strong>precies één proton van elkaar verschillen</strong>, "
                  "vormen een <strong>geconjugeerd paar</strong> of "
                  "<strong>zuurbasekoppel</strong>. Het deeltje met het extra proton is het zuur, "
                  "het andere de base, en elke protolyse heeft twee zulke paren. "
                  "<strong>Een zuur en zijn geconjugeerde base verschillen dus precies één "
                  "proton</strong>, zoals azijnzuur CH₃COOH en het acetaation CH₃COO⁻."),
            ("p", "Oefen het op drie voorbeelden. De geconjugeerde base van "
                  "<strong>waterstofchloride HCl</strong> is "
                  "<strong>het chloride-ion</strong>. Het geconjugeerde zuur van "
                  "<strong>ammoniak NH₃</strong> is <strong>het ammoniumion</strong>, dat het "
                  "proton weer kan afstaan. En <strong>H₂CO₃ en HCO₃⁻</strong> en "
                  "<strong>NH₄⁺ en NH₃</strong> zijn paren, terwijl H₂O en H₃O⁺ een paar vormen met "
                  "water als base."),
            ("p", "Het <strong>hydroxide-ion</strong> "
                  "<strong>neemt een proton op en wordt water</strong> en "
                  "<strong>is de geconjugeerde base van water</strong>."),
            ("p", "Sommige stoffen kunnen beide rollen spelen. Een "
                  "<strong>amfolyt</strong> of <strong>amfoteer</strong> deeltje kan een proton "
                  "afstaan én opnemen: <strong>water</strong> en "
                  "<strong>het waterstofcarbonaation</strong> zijn de twee voorbeelden, want HCO₃⁻ "
                  "kan naar CO₃²⁻ of naar H₂CO₃. Tegenover HCl is water een base, tegenover "
                  "ammoniak een zuur: reageert <strong>water met ammoniak</strong>, dan "
                  "<strong>is het water het zuur en staat het een proton af</strong>, want NH₃ plus "
                  "H₂O geeft NH₄⁺ plus OH⁻. <strong>In de reactie van azijnzuur met water is het "
                  "water juist de base</strong>. Welke reactie een amfolyt in water aangaat, weet je "
                  "door <strong>zijn zuurconstante met zijn baseconstante te vergelijken</strong>: "
                  "is Kz groter dan Kb, dan gedraagt het zich vooral als zuur; bij HCO₃⁻ is het "
                  "omgekeerd, en daarom is bakpoeder in water lichtbasisch."),
            ("p", "Een zuur kan meer dan één proton kwijt. "
                  "<strong>Zwavelzuur is tweewaardig</strong> omdat het "
                  "<strong>twee protonen kan afstaan, in twee stappen</strong>: eerst H₂SO₄ naar "
                  "HSO₄⁻, dan naar SO₄²⁻, waarbij de eerste stap veel sterker is. "
                  "<strong>Fosforzuur H₃PO₄</strong> kan er <strong>drie</strong> afstaan. Een "
                  "<strong>meerwaardige base</strong> "
                  "<strong>kan meer dan één proton opnemen</strong>, zoals het carbonaation CO₃²⁻."),
        ]),
        dict(kop="Sterk en zwak", blokken=[
            ("p", "Een <strong>sterk zuur in water</strong> "
                  "<strong>staat zijn proton zo goed als volledig af</strong>: "
                  "<strong>zoutzuur</strong> en <strong>salpeterzuur</strong> zijn sterke zuren, "
                  "terwijl azijnzuur en koolzuur zwakke zuren zijn die grotendeels als molecule in "
                  "de oplossing blijven. De <strong>ionisatiegraad</strong> is "
                  "<strong>het deel van de moleculen dat zijn proton heeft afgestaan</strong>; bij "
                  "verdunnen wordt die graad groter."),
            ("p", "<strong>Sterk en geconcentreerd betekenen niet hetzelfde</strong>: sterk gaat "
                  "over hoe goed een zuur ioniseert, geconcentreerd over hoeveel mol er per liter "
                  "in zit. Verdund zoutzuur blijft een sterk zuur. En "
                  "<strong>een zwak zuur kan wél een lage pH geven</strong> als het geconcentreerd "
                  "genoeg is: azijn is daarvan een voorbeeld. Twee zuren van "
                  "<strong>dezelfde concentratie, één sterk en één zwak</strong>, verschillen in "
                  "<strong>de pH van de twee oplossingen</strong>."),
            ("p", "De <strong>zuurconstante</strong> van een zuur HA in water is "
                  "<strong>Kz is [H₃O⁺] maal [A⁻] gedeeld door [HA]</strong>, gewoon de "
                  "evenwichtsconstante van de protolyse; het water staat er niet in, want het is in "
                  "overmaat. De <strong>baseconstante Kb</strong> heeft dezelfde vorm met het "
                  "hydroxide-ion in de teller. Een <strong>kleine pKz-waarde</strong> hoort bij een "
                  "<strong>sterk</strong> zuur, want pKz is de negatieve logaritme van Kz: van twee "
                  "zuren met <strong>pKz 3 en pKz 5</strong> is "
                  "<strong>het zuur met pKz 3 het sterkste</strong>, en twee eenheden verschil is "
                  "een factor honderd."),
            ("p", "<strong>Voor een geconjugeerd paar geldt: hoe sterker het zuur, hoe zwakker "
                  "zijn base</strong>, want het product van Kz en Kb is altijd de "
                  "ionisatieconstante van water. "
                  "<strong>De geconjugeerde base van een sterk zuur is dus een heel zwakke "
                  "base</strong>: het chloride-ion neemt bijna nooit een proton terug op."),
        ]),
        dict(kop="Zouten in water, en hoe je de pH ziet", blokken=[
            ("p", "Daaruit volgt hoe een zout in water reageert. "
                  "<strong>Een oplossing van keukenzout in water is neutraal</strong>, want Na⁺ en "
                  "Cl⁻ komen van een sterke base en een sterk zuur; ook "
                  "<strong>kaliumnitraat in water</strong> is neutraal. Een oplossing van "
                  "<strong>natriumacetaat is basisch</strong> omdat "
                  "<strong>het acetaation de geconjugeerde base van een zwak zuur is</strong> en "
                  "dus sterk genoeg om een proton van water af te pakken. Een oplossing van "
                  "<strong>ammoniumchloride is zuur</strong> omdat "
                  "<strong>het ammoniumion een proton afstaat aan het water</strong>. Soda is "
                  "basisch."),
            ("p", "Een <strong>pH-meter</strong> meet de pH nauwkeurig als een getal; je ijkt ze "
                  "eerst met bufferoplossingen van bekende pH. Een "
                  "<strong>zuurbase-indicator</strong> geeft maar een gebied: "
                  "<strong>het is zelf een zwak zuur waarvan de twee vormen anders gekleurd "
                  "zijn</strong>. Het <strong>omslaggebied</strong> "
                  "<strong>ligt rond de pKz van de indicator</strong> en "
                  "<strong>beslaat ongeveer twee pH-eenheden</strong>: "
                  "<strong>fenolftaleïen</strong> is "
                  "<strong>kleurloos in zuur en roze in basisch midden</strong> met een omslag rond "
                  "pH 9, en methyloranje slaat om rond pH 4. Daarom kies je je indicator bij de "
                  "titratie die je doet."),
        ]),
    ],
    onthoud=[
        "Zuur geeft een proton, base neemt het op; zonder base geen protolyse.",
        "Een geconjugeerd paar verschilt precies één proton.",
        "Een amfolyt kan beide: water en HCO₃⁻.",
        "Sterk is niet hetzelfde als geconcentreerd.",
        "Kleine pKz betekent sterk zuur; Kz · Kb is de constante van water.",
        "Sterk zuur plus sterke base geeft een neutraal zout.",
        "Fenolftaleïen: kleurloos in zuur, roze in basisch, omslag rond pH 9.",
    ],
)

# ───────────────────── 12. pH, pOH en rekenen met zuren en basen
BUNDELS["ph-poh-en-rekenen-met-zuren-en-basen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="pH, pOH en rekenen met zuren en basen",
    onder="De logaritmische schaal, en hoe je er een echte concentratie uit haalt.",
    secties=[
        dict(kop="De pH-schaal", blokken=[
            ("p", "De <strong>pH</strong> van een oplossing is "
                  "<strong>de negatieve logaritme van de concentratie hydroxoniumionen</strong>: is "
                  "[H₃O⁺] gelijk aan 10⁻³ mol/L, dan is de pH 3. Men gebruikt zo'n "
                  "<strong>logaritmische schaal</strong> omdat "
                  "<strong>de concentraties over heel veel machten van tien verspreid "
                  "liggen</strong>: van 1 mol/L tot 10⁻¹⁴ mol/L is veertien machten verschil."),
            ("p", "<strong>De schaal is logaritmisch opgebouwd</strong> en "
                  "<strong>één eenheid verschil is een factor tien</strong>. Zo bevat "
                  "<strong>een oplossing met pH 3 honderd keer meer hydroxoniumionen dan een met "
                  "pH 5</strong>, zit er in <strong>pH 2</strong> "
                  "<strong>100</strong> keer meer dan in pH 4, en is een oplossing met "
                  "<strong>pH 1</strong> <strong>duizend keer</strong> zuurder dan een met pH 4. Bij "
                  "heel geconcentreerde oplossingen kan de pH zelfs onder nul of boven veertien "
                  "liggen: de schaal is geen grens, maar een rekenwijze. Let op het minteken: "
                  "<strong>hoe hoger de pH, hoe minder hydroxoniumionen</strong> er in de oplossing "
                  "zitten."),
            ("p", "Het <strong>product van de concentratie hydroxonium en hydroxide</strong> in "
                  "water heet de <strong>ionisatieconstante van water</strong> of "
                  "<strong>Kw</strong>, en is bij 25 °C <strong>10⁻¹⁴</strong>, namelijk 10⁻⁷ maal "
                  "10⁻⁷. Daaruit volgt dat <strong>pH plus pOH</strong> bij 25 °C "
                  "<strong>veertien</strong> is, en dat <strong>zuiver water pH 7</strong> heeft: "
                  "dat is het neutrale punt. <strong>De pH hangt wél af van de "
                  "temperatuur</strong>, want Kw verandert ermee, en dus ook het neutrale punt."),
            ("p", "Reken heen en terug. Bij <strong>pH 4</strong> hoort "
                  "<strong>pOH tien</strong>; bij <strong>pOH 2</strong> hoort "
                  "<strong>pH twaalf</strong>, zoals ontstopper; bij "
                  "<strong>pH 11</strong> hoort <strong>pOH 3</strong>. Bij "
                  "<strong>[H₃O⁺] gelijk aan 10⁻² mol/L</strong> hoort "
                  "<strong>pH 2</strong>, ongeveer zo zuur als citroensap, en bij "
                  "<strong>pH 5</strong> hoort <strong>10⁻⁵ mol/L</strong>, want [H₃O⁺] is tien tot "
                  "de macht min de pH. Bij <strong>pH 9</strong> is de concentratie hydroxide-ionen "
                  "<strong>10⁻⁵ mol/L</strong>, want pOH is dan vijf."),
            ("p", "Een <strong>basische oplossing</strong> heeft "
                  "<strong>een pH groter dan 7</strong> en "
                  "<strong>een pOH kleiner dan 7</strong>, en "
                  "<strong>er zit meer hydroxide dan hydroxonium</strong> in; hydroxoniumionen "
                  "blijven er altijd in, want het evenwicht van water staat nooit helemaal stil. "
                  "Zuur zijn onder meer <strong>een oplossing met pH 2</strong> en "
                  "<strong>een oplossing met pOH 12</strong>, want die hoort bij pH 2. Meet je "
                  "<strong>pH 6,5 in regenwater</strong>, dan "
                  "<strong>is het lichtzuur, want de pH ligt onder zeven</strong>: er lost "
                  "koolstofdioxide uit de lucht in op, en dat vormt koolzuur."),
        ]),
        dict(kop="Rekenen met een sterk zuur of een sterke base", blokken=[
            ("p", "Bij een <strong>sterk zuur mag je de concentratie van het zuur als [H₃O⁺] "
                  "nemen</strong>, want <strong>elk molecule staat zijn proton af, dus is de "
                  "omzetting volledig</strong>. Zo heeft "
                  "<strong>0,1 mol/L zoutzuur pH 1</strong>, "
                  "<strong>0,01 mol/L zoutzuur pH 2</strong> en "
                  "<strong>0,0001 mol/L zoutzuur pH 4</strong>; let goed op het aantal nullen voor "
                  "de komma. Bij een <strong>tweewaardig sterk zuur is de concentratie "
                  "hydroxoniumionen dubbel die van het zuur</strong>: zwavelzuur van 0,05 mol/L "
                  "geeft ongeveer 0,1 mol/L, dus pH 1. Reken dus altijd de waardigheid mee."),
            ("p", "Bij een <strong>sterke base</strong> reken je eerst de pOH uit. "
                  "<strong>0,001 mol/L natriumhydroxide</strong> geeft [OH⁻] gelijk aan 10⁻³, dus "
                  "pOH 3 en <strong>pH 11</strong>; "
                  "<strong>0,01 mol/L natriumhydroxide</strong> geeft "
                  "<strong>pH 12</strong>. Van een rij oplossingen heeft "
                  "<strong>0,1 mol/L natriumhydroxide</strong> dan ook de hoogste pH: pOH 1 en dus "
                  "pH 13."),
            ("p", "Verdunnen en inkoken schuiven de pH. "
                  "<strong>Verdun je een sterk zuur tien keer, dan stijgt de pH met één "
                  "eenheid</strong>. <strong>Door heel sterk te verdunnen komt de pH niet boven "
                  "zeven</strong>: ze kruipt naar zeven toe en blijft eronder, want water zelf kan "
                  "de oplossing niet basisch maken. Damp je een oplossing "
                  "<strong>in tot de helft van het volume</strong>, dan "
                  "<strong>daalt de pH, want de concentratie wordt groter</strong>, met ongeveer "
                  "0,3. En <strong>de pH van een sterk zuur komt bij gewone concentraties niet "
                  "onder nul</strong>, want <strong>daarvoor zou de concentratie boven 1 mol per "
                  "liter moeten liggen</strong>."),
            ("p", "Meng je <strong>gelijke volumes van een sterk zuur en een sterke base van "
                  "dezelfde concentratie</strong>, dan krijg je "
                  "<strong>een neutrale oplossing met pH 7</strong>: alle hydroxonium- en "
                  "hydroxide-ionen reageren precies weg tot water, en er blijft een neutraal zout "
                  "over."),
        ]),
        dict(kop="En bij een zwak zuur", blokken=[
            ("p", "<strong>De pH van een zwak zuur bereken je niet rechtstreeks uit zijn "
                  "concentratie.</strong> Je hebt daarvoor "
                  "<strong>de concentratie van het zuur</strong> én "
                  "<strong>de zuurconstante van het zuur</strong> nodig, want maar een deel van de "
                  "moleculen staat zijn proton af."),
            ("p", "Van twee oplossingen van 0,1 mol/L heeft "
                  "<strong>het zoutzuur de laagste pH, want het is een sterk zuur</strong>: "
                  "azijnzuur geeft maar een paar procent van zijn protonen af, al zit er in beide "
                  "bekers evenveel mol zuur. Daarom geldt ook: "
                  "<strong>een zwak zuur en een sterk zuur van dezelfde concentratie "
                  "neutraliseren evenveel base</strong>, want het aantal mol zuur bepaalt hoeveel "
                  "base je nodig hebt, niet de sterkte."),
            ("p", "Verdun je een zwak zuur, dan "
                  "<strong>wordt de ionisatiegraad groter</strong> en "
                  "<strong>wordt de pH hoger</strong>: het evenwicht schuift naar de kant van de "
                  "ionen, maar er zijn in totaal toch minder ionen per liter."),
        ]),
    ],
    onthoud=[
        "pH = −log[H₃O⁺]; één eenheid is een factor tien.",
        "Kw is 10⁻¹⁴, dus pH + pOH = 14 bij 25 °C; zuiver water heeft pH 7.",
        "Hoge pH betekent weinig hydroxonium, veel hydroxide.",
        "Sterk zuur: de concentratie van het zuur is [H₃O⁺]; reken de waardigheid mee.",
        "Bij een base eerst de pOH, dan 14 min pOH.",
        "Tien keer verdunnen schuift de pH één eenheid, maar nooit over zeven.",
        "Voor een zwak zuur heb je ook Kz nodig.",
    ],
)

# ───────────────────── 13. Buffers en zuurbasetitraties
BUNDELS["buffers-en-zuurbasetitraties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Buffers en zuurbasetitraties",
    onder="Een mengsel dat de pH vasthoudt, en een proef die een concentratie verraadt.",
    secties=[
        dict(kop="Wat een buffer doet", blokken=[
            ("p", "Een <strong>buffer</strong> of <strong>buffermengsel</strong> is een mengsel "
                  "<strong>dat de pH bijna gelijk houdt als je zuur of base toevoegt</strong>. Het "
                  "bestaat uit <strong>een zwak zuur samen met zijn geconjugeerde base</strong>, "
                  "beide in vergelijkbare hoeveelheden; <strong>azijnzuur met "
                  "natriumacetaat</strong> is het schoolvoorbeeld, en "
                  "<strong>ammoniak met ammoniumchloride</strong> is de basische tegenhanger."),
            ("p", "<strong>Een buffer werkt naar twee kanten</strong>, niet enkel tegen "
                  "toegevoegd zuur. Giet je er een beetje <strong>sterk zuur</strong> bij, dan "
                  "<strong>neemt de geconjugeerde base de hydroxoniumionen weg</strong> en wordt ze "
                  "zelf het zwakke zuur. Voeg je een beetje <strong>sterke base</strong> toe, dan "
                  "<strong>neemt het zwakke zuur van het paar de hydroxide-ionen weg</strong> en "
                  "ontstaat er water."),
            ("p", "<strong>Een buffer houdt de pH niet precies gelijk, hoeveel je er ook bij "
                  "giet.</strong> Hij vangt het op zolang er genoeg van beide deeltjes is; is er te "
                  "veel bijgekomen, dan is de buffer uitgeput en schiet de pH weg. De "
                  "<strong>capaciteit</strong> van een buffer "
                  "<strong>is groter als de concentraties hoger zijn</strong> en "
                  "<strong>is op als een van de twee deeltjes verbruikt is</strong>: een buffer van "
                  "1 mol/L vangt veel meer op dan een van 0,01 mol/L, ook al hebben ze dezelfde pH. "
                  "<strong>Verdunnen verandert de pH van een buffer bijna niet</strong>, want de "
                  "verhouding tussen zuur en base blijft gelijk; de capaciteit wordt wel kleiner."),
        ]),
        dict(kop="Welke buffer voor welke pH", blokken=[
            ("p", "Een buffer werkt het best "
                  "<strong>als het zuur en zijn geconjugeerde base in dezelfde concentratie "
                  "aanwezig zijn</strong>: dan kan hij naar beide kanten evenveel opvangen, en dan "
                  "is zijn <strong>pH gelijk aan de pKz</strong> van het zuur, want de twee "
                  "concentraties vallen tegen elkaar weg."),
            ("p", "Het bereik van een buffer is ongeveer "
                  "<strong>één</strong> pH-eenheid rond die pKz, plus of min. Een buffer met een "
                  "zuur van <strong>pKz 5</strong> werkt dus "
                  "<strong>ongeveer tussen pH 4 en pH 6</strong>, en een "
                  "<strong>buffer met pKz 7 is geschikt om een oplossing rond pH 7 te "
                  "houden</strong>. Daarbuiten is de verhouding tussen zuur en base te scheef "
                  "geworden. Zo kies je het zuur op basis van de pH die je nodig hebt: voor een "
                  "buffer rond pH 9 meng je <strong>ammoniak met ammoniumchloride</strong>, want "
                  "het ammoniumion heeft een pKz van ongeveer 9,2, terwijl azijnzuur je rond pH 5 "
                  "zou brengen."),
            ("p", "Een <strong>basische buffer</strong> "
                  "<strong>bestaat uit een zwakke base met haar geconjugeerde zuur</strong> en "
                  "<strong>zijn pH ligt boven zeven</strong>. Een "
                  "<strong>mengsel van zoutzuur en natriumchloride buffert niet</strong>, want "
                  "<strong>het chloride-ion is een te zwakke base om protonen op te nemen</strong>: "
                  "bij een sterk zuur is de geconjugeerde base daarvoor te zwak. Hetzelfde geldt "
                  "voor een sterke base met haar zout."),
            ("p", "Je kan een buffer ook per ongeluk maken. Meng je een "
                  "<strong>zwak zuur met een sterke base, maar niet genoeg base om alles weg te "
                  "werken</strong>, dan krijg je "
                  "<strong>een buffer van het zwakke zuur met zijn geconjugeerde base</strong>: de "
                  "base zet een deel van het zuur om, en zo zitten beide deeltjes in dezelfde "
                  "beker."),
            ("p", "In het lichaam is dat levensbelangrijk. "
                  "<strong>De pH van bloed blijft zo constant omdat koolzuur en het "
                  "waterstofcarbonaation er een buffer vormen</strong>. Dat "
                  "<strong>geconjugeerde paar</strong> houdt de pH rond 7,4, en een afwijking van "
                  "een paar tienden is al levensgevaarlijk. Door sneller te ademen verlies je "
                  "koolstofdioxide, en dat verschuift dat evenwicht."),
        ]),
        dict(kop="Een titratie uitvoeren", blokken=[
            ("p", "Bij een titratie laat je het <strong>titrans</strong> of "
                  "<strong>titreervloeistof</strong> uit de buret lopen; haar concentratie moet "
                  "nauwkeurig gekend zijn. De onbekende oplossing staat in de "
                  "<strong>erlenmeyer</strong>, waarvan de schuine wanden je laten zwenken zonder "
                  "te spatten. Om precies 20 mL van de onbekende oplossing af te meten gebruik je "
                  "een <strong>pipet</strong>, die je met een pipetvuller vult en nooit met de mond."),
            ("p", "Je <strong>spoelt de buret met titrans</strong> voor je begint, want water zou "
                  "het verdunnen. <strong>De erlenmeyer mag wel nat zijn van water</strong>, want "
                  "<strong>water verandert het aantal mol in de erlenmeyer niet</strong>: daar gaat "
                  "het om mol, niet om concentratie. <strong>Je mag de buret niet tot boven de "
                  "nulstreep vullen en dan het verschil berekenen</strong>, want boven de nulstreep "
                  "is er geen schaal. Bij het aflezen "
                  "<strong>lees je af bij de onderkant van de meniscus</strong> en "
                  "<strong>houd je je oog op dezelfde hoogte als de vloeistof</strong>; scheef "
                  "aflezen geeft een parallaxfout. Een <strong>proeftitratie</strong> doe je "
                  "<strong>om ongeveer te weten waar de sprong ligt, zodat je daarna traag kan "
                  "druppelen</strong>."),
            ("p", "<strong>Fouten die een te groot volume titrans geven</strong> zijn onder meer: "
                  "<strong>de buret is met water gespoeld en niet met titrans</strong>, en "
                  "<strong>je druppelt door na de kleuromslag</strong>. Beide geven een te hoge "
                  "berekende concentratie."),
        ]),
        dict(kop="De curve lezen en de concentratie berekenen", blokken=[
            ("p", "Het <strong>equivalentiepunt</strong> is "
                  "<strong>het punt waarop er precies genoeg base is voor al het zuur</strong>, dus "
                  "waar het aantal mol gelijk is, met de waardigheid meegerekend. Je ziet het op de "
                  "curve <strong>aan de steile sprong in de pH, midden in het verloop</strong>. "
                  "<strong>De pH is daar niet altijd zeven</strong>: bij een "
                  "<strong>sterk zuur met een sterke base</strong> ligt het "
                  "<strong>bij pH 7, want er blijft een neutraal zout over</strong>, maar "
                  "<strong>bij de titratie van een zwak zuur met een sterke base ligt het "
                  "equivalentiepunt boven pH 7</strong>, want er blijft de geconjugeerde base van "
                  "een zwak zuur over."),
            ("p", "Een <strong>indicator</strong> kies je zo dat "
                  "<strong>haar omslaggebied binnen de pH-sprong van de curve valt</strong>; bij "
                  "een zwak zuur met een sterke base past fenolftaleïen dus goed. "
                  "<strong>Het equivalentiepunt en het punt van de kleuromslag zijn niet precies "
                  "hetzelfde</strong>: dat laatste heet het <strong>eindpunt</strong> en ligt er "
                  "meestal een druppel naast. Je kan het equivalentiepunt ook "
                  "<strong>met een pH-meter of met een geleidbaarheidsmeting</strong> bepalen, dus "
                  "zonder indicator."),
            ("p", "Twee eigenschappen van de curve. <strong>Bij de titratie van een zwak zuur loopt "
                  "er een stuk van de curve vlak, want daar werkt een buffer</strong>: halverwege "
                  "zitten het zuur en zijn geconjugeerde base samen in de beker, en daar is de pH "
                  "gelijk aan de pKz. En titreer je een verdunder zuur, dan "
                  "<strong>wordt de sprong kleiner en minder steil</strong>, want begin en einde "
                  "liggen dichter bij pH 7."),
            ("p", "Rekenen doe je in mol. Titreer je "
                  "<strong>20 mL zuur met 0,1 mol/L base en verbruik je 20 mL</strong>, dan is het "
                  "eenwaardige zuur <strong>0,1 mol/L</strong>: 0,1 maal 0,020 is 0,002 mol base, "
                  "dus ook 0,002 mol zuur. Titreer je "
                  "<strong>20 mL van een tweewaardig zuur en verbruik je 40 mL</strong> van "
                  "0,1 mol/L base, dan is het zuur ook <strong>0,1 mol/L</strong>: 0,004 mol base "
                  "neutraliseert 0,002 mol tweewaardig zuur."),
        ]),
    ],
    onthoud=[
        "Een buffer is een zwak zuur met zijn geconjugeerde base.",
        "Gelijke concentraties: pH = pKz; bereik is pKz plus of min één.",
        "Capaciteit hangt af van de concentraties, niet van de pH.",
        "Bloed wordt gebufferd door koolzuur en waterstofcarbonaat, rond pH 7,4.",
        "Buret spoelen met titrans, erlenmeyer mag nat zijn van water.",
        "Equivalentiepunt is de steile sprong; bij een zwak zuur ligt die boven pH 7.",
        "Kies de indicator met haar omslaggebied binnen de sprong.",
    ],
)

# ───────────────────── 14. Oxidatiegetallen en redoxreacties
BUNDELS["oxidatiegetallen-en-redoxreacties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Oxidatiegetallen en redoxreacties",
    onder="Elektronen die van hand wisselen, en hoe je dat in een vergelijking zet.",
    secties=[
        dict(kop="Oxidatiegetallen bepalen", blokken=[
            ("p", "In een <strong>enkelvoudige stof</strong> is het oxidatiegetal "
                  "<strong>nul</strong>: in O₂, Fe en Cl₂ is er geen verschil tussen de atomen. "
                  "<strong>Zuurstof</strong> heeft in de meeste verbindingen "
                  "<strong>min twee</strong>; alleen in een peroxide is het min een door de "
                  "O-O-brug, en in OF₂ zelfs positief. "
                  "<strong>Waterstof</strong> heeft in een verbinding met een niet-metaal "
                  "<strong>+I</strong>, maar in een metaalhydride zoals NaH min een, want daar is "
                  "waterstof het meest elektronegatieve atoom. "
                  "<strong>Zuurstof heeft dus niet overal −II</strong>: niet "
                  "<strong>in waterstofperoxide H₂O₂</strong> en niet "
                  "<strong>in zuurstofgas O₂</strong>."),
            ("p", "<strong>De som van de oxidatiegetallen in een neutrale verbinding is "
                  "nul</strong>, en bij een ion is die som gelijk aan de lading. Dat is je controle. "
                  "Reken mee: zwavel in <strong>H₂SO₄</strong> is "
                  "<strong>+VI</strong>, mangaan in <strong>MnO₄⁻</strong> is "
                  "<strong>+VII</strong>, chroom in <strong>Cr₂O₇²⁻</strong> is "
                  "<strong>+VI</strong> (de twee chroomatomen dragen samen +12), stikstof in "
                  "<strong>NO₃⁻</strong> is <strong>+V</strong>, koolstof in "
                  "<strong>CH₄</strong> is <strong>−IV</strong> en in "
                  "<strong>koolstofdioxide</strong> <strong>+IV</strong> — zo sterk geoxideerd als "
                  "het kan, en daarom brandt CO₂ niet meer."),
            ("p", "<strong>Koolstof heeft niet in elke organische verbinding hetzelfde "
                  "oxidatiegetal</strong>: in methanol is het −II, in methanal nul en in methaanzuur "
                  "+II. Zo zie je dat de reeks alcohol, aldehyde en zuur telkens een oxidatie is."),
        ]),
        dict(kop="Oxidatie, reductie, oxidator en reductor", blokken=[
            ("p", "Bij een <strong>oxidatie</strong> "
                  "<strong>staat een deeltje elektronen af en stijgt zijn "
                  "oxidatiegetal</strong>; oxidatie heeft dus niet noodzakelijk met zuurstof te "
                  "maken. Bij een <strong>reductie</strong> neemt een deeltje "
                  "<strong>elektronen op</strong> en daalt het oxidatiegetal."),
            ("p", "Een <strong>oxidator</strong> <strong>neemt elektronen op</strong> en "
                  "<strong>wordt zelf gereduceerd</strong>; een <strong>reductor</strong> of "
                  "<strong>reducens</strong> is het deeltje dat "
                  "<strong>elektronen afstaat</strong> en zelf geoxideerd wordt."),
            ("p", "In een <strong>redoxreactie</strong> "
                  "<strong>is er altijd een oxidatie en een reductie samen</strong> en is "
                  "<strong>het aantal afgestane elektronen gelijk aan het aantal "
                  "opgenomen</strong>, want elektronen kunnen niet los blijven rondzweven."),
            ("p", "Oefen het herkennen. <strong>Bij de verbranding van methaan wordt koolstof "
                  "geoxideerd</strong>, van −IV naar +IV, dus acht eenheden stijging. Gaat ijzer "
                  "<strong>van Fe²⁺ naar Fe³⁺</strong>, dan "
                  "<strong>is het geoxideerd en heeft het een elektron afgestaan</strong>. Eén "
                  "<strong>aluminiumatoom</strong> dat Al³⁺ wordt, staat "
                  "<strong>drie</strong> elektronen af. En "
                  "<strong>een stof die zuurstof opneemt, wordt niet gereduceerd maar "
                  "geoxideerd</strong>, want zuurstof trekt de elektronen naar zich toe."),
        ]),
        dict(kop="Een redoxvergelijking opstellen", blokken=[
            ("p", "De eerste stap is "
                  "<strong>de oxidatiegetallen bepalen en zien welk atoom verandert</strong>. Pas "
                  "dan kan je de <strong>halfreacties</strong> schrijven. Zo'n halfreactie "
                  "<strong>bevat de elektronen die afgestaan of opgenomen worden</strong> en "
                  "<strong>beschrijft enkel de oxidatie of enkel de reductie</strong>."),
            ("p", "Je <strong>vermenigvuldigt de twee halfreacties met een factor</strong> omdat "
                  "<strong>het aantal afgestane en opgenomen elektronen gelijk moet zijn</strong>: "
                  "staat de ene er twee af en neemt de andere er drie op, dan vermenigvuldig je met "
                  "drie en met twee. Bij het optellen vallen de elektronen weg, en "
                  "<strong>in de eindvergelijking mogen er dus geen losse elektronen meer "
                  "staan</strong>."),
            ("p", "Om de vergelijking in evenwicht te brengen gebruik je in zuur midden "
                  "<strong>water en H₃O⁺</strong>, in basisch midden water en hydroxide-ionen: daar "
                  "<strong>gebruik je hydroxide-ionen om de lading te regelen</strong> en "
                  "<strong>water om de waterstofatomen te regelen</strong>. "
                  "<strong>De lading links en rechts van een ionenreactievergelijking moet gelijk "
                  "zijn</strong> — niet nul, maar gelijk — en dat is naast het aantal atomen je "
                  "tweede controle."),
            ("p", "Het verschil tussen een <strong>ionenreactievergelijking</strong> en een "
                  "<strong>stoffenreactievergelijking</strong> is dat je "
                  "<strong>in de eerste de ionen weglaat die niet meedoen</strong>. Zo'n ion dat "
                  "<strong>aan beide kanten onveranderd staat</strong>, heet een "
                  "<strong>toeschouwerion</strong>."),
        ]),
        dict(kop="Voorspellen met de normpotentialen", blokken=[
            ("p", "Om te voorspellen of een redoxreactie spontaan doorgaat, gebruik je de tabel van "
                  "de <strong>normpotentialen</strong>; op het examen krijg je die in de bijlage. "
                  "Een <strong>hoge normpotentiaal</strong> betekent dat "
                  "<strong>de geoxideerde vorm een sterke oxidator is</strong>: hoog in de tabel "
                  "staat de sterkste oxidator, onderaan de sterkste reductoren zoals de "
                  "alkalimetalen."),
            ("p", "<strong>Een reactie tussen twee redoxkoppels gaat spontaan door als de sterkste "
                  "oxidator met de sterkste reductor reageert</strong>: de oxidator moet een hogere "
                  "normpotentiaal hebben dan het koppel van de reductor. Zo'n "
                  "<strong>spontane reactie</strong> levert energie; een gedwongen reactie heeft "
                  "een spanningsbron nodig."),
            ("p", "Drie voorspellingen. Leg je <strong>een stukje zink in een oplossing van "
                  "kopersulfaat</strong>, dan "
                  "<strong>lost het zink op en slaat er koper op het stukje neer</strong>, want "
                  "zink is de sterkere reductor. Met "
                  "<strong>Cu²⁺/Cu op +0,34 V en Zn²⁺/Zn op −0,76 V</strong> "
                  "<strong>wordt zink geoxideerd en het koperion gereduceerd</strong>. En laat je "
                  "<strong>ijzer reageren met zoutzuur</strong>, dan ontstaan er "
                  "<strong>ijzer(II)ionen en waterstofgas</strong>."),
            ("p", "<strong>Koper wordt niet aangetast door zoutzuur</strong>, want "
                  "<strong>het hydroxoniumion is een te zwakke oxidator voor koper</strong>: koper "
                  "staat in de tabel boven waterstof. <strong>Salpeterzuur tast koper wel aan, want "
                  "het nitraation is een sterkere oxidator dan het hydroxoniumion</strong>, en "
                  "daarbij ontstaat NO of NO₂; de sterkte van het zuur speelt daar dus geen rol. "
                  "Algemeen: <strong>een metaal boven waterstof lost niet op in een gewoon "
                  "zuur</strong>, een metaal eronder wel, en dan komt er waterstofgas vrij."),
        ]),
    ],
    onthoud=[
        "Enkelvoudige stof nul, zuurstof meestal −II, waterstof +I.",
        "De som is nul in een verbinding en gelijk aan de lading in een ion.",
        "Oxidatie stijgt en staat elektronen af; reductie daalt en neemt ze op.",
        "De oxidator wordt gereduceerd, de reductor geoxideerd.",
        "Halfreacties gelijkstellen op elektronen, dan optellen.",
        "Lading én atomen moeten links en rechts kloppen.",
        "Hoog in de tabel staat de sterkste oxidator.",
    ],
)

# ───────────────────── 15. Galvanische cellen en elektrolyse
BUNDELS["galvanische-cellen-en-elektrolyse-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Galvanische cellen en elektrolyse",
    onder="Een redoxreactie die stroom levert, en een stroom die een reactie afdwingt.",
    secties=[
        dict(kop="De galvanische cel", blokken=[
            ("p", "Een <strong>galvanische cel zet chemische energie om in elektrische "
                  "energie</strong>: de reactie gaat spontaan door en levert daarbij spanning. Een "
                  "<strong>batterij is een toepassing van een galvanische cel</strong>, en is de "
                  "reactie uitgewerkt, dan is ze leeg."),
            ("p", "Aan de <strong>anode</strong> gebeurt "
                  "<strong>de oxidatie, waarbij elektronen vrijkomen</strong>; aan de "
                  "<strong>kathode</strong> gebeurt de <strong>reductie</strong>. In een "
                  "galvanische cel is de anode <strong>de negatieve pool</strong>, want daar is een "
                  "overschot aan negatieve lading. <strong>De oxidatie gebeurt in een galvanische "
                  "cel dus niet aan de positieve pool.</strong> De "
                  "<strong>elektronen lopen van de anode naar de kathode, door de draad</strong>; "
                  "de stroomrichting die men in de natuurkunde afspreekt, is net omgekeerd."),
            ("p", "Twee bruggen verbinden de halfcellen. De "
                  "<strong>elektronenbrug</strong> is <strong>de draad</strong> met eventueel een "
                  "toestel ertussen en <strong>brengt de elektronen van de ene elektrode naar de "
                  "andere</strong>. De <strong>zoutbrug</strong> dient "
                  "<strong>om de ladingen in de twee halfcellen in evenwicht te houden</strong>; "
                  "<strong>de elektronen lopen dus niet door de zoutbrug</strong>, enkel ionen "
                  "doen dat. De <strong>negatieve ionen bewegen daarin naar de halfcel van de "
                  "anode</strong>, waar positieve metaalionen bijkomen. Elke halfcel moet haar "
                  "eigen oplossing hebben, want <strong>anders reageren de twee koppels "
                  "rechtstreeks, zonder stroom door de draad</strong>."),
            ("p", "De voorstelling <strong>Zn/Zn²⁺//Cu²⁺/Cu</strong> betekent: "
                  "<strong>links de anode met haar oplossing, rechts de kathode met de hare</strong>, "
                  "met de dubbele streep als zoutbrug. Links staat altijd de oxidatie."),
            ("p", "De elektroden veranderen tijdens het gebruik. "
                  "<strong>Aan de anode gebeurt de oxidatie</strong> en "
                  "<strong>wordt de anode tijdens het gebruik dunner</strong>, want het metaal lost "
                  "op als ion. De <strong>massa van de kathode wordt juist groter, want er slaat "
                  "metaal op neer</strong>."),
            ("p", "De <strong>bronspanning</strong> bij normomstandigheden bereken je als "
                  "<strong>de normpotentiaal van de kathode min die van de anode</strong>, zodat er "
                  "bij een spontane cel een positief getal uitkomt; het koppel met de hoogste "
                  "waarde wordt de kathode. Ze <strong>wordt uitgedrukt in volt</strong> en "
                  "<strong>is groter als de twee normpotentialen verder uit elkaar liggen</strong>; "
                  "de afstand tussen de elektroden speelt geen rol. Met "
                  "<strong>Cu²⁺/Cu op +0,34 V en Zn²⁺/Zn op −0,76 V</strong> is de bronspanning "
                  "<strong>1,10 V</strong>, met <strong>zink</strong> als anode, want het heeft de "
                  "laagste normpotentiaal en is dus de sterkste reductor."),
        ]),
        dict(kop="De elektrolyse", blokken=[
            ("p", "Een <strong>elektrolyse</strong> heeft "
                  "<strong>een spanningsbron die de reactie afdwingt</strong> nodig, want ze "
                  "verloopt niet spontaan. Dat is een "
                  "<strong>gedwongen reactie</strong>: <strong>een reactie die enkel doorgaat met "
                  "energie van buitenaf</strong>. Bij een elektrolyse "
                  "<strong>wordt elektrische energie omgezet in chemische energie</strong> en "
                  "<strong>zou de reactie zonder spanningsbron niet doorgaan</strong>. "
                  "<strong>Een elektrolyse levert dus geen elektrische energie op</strong>, ze "
                  "verbruikt die juist."),
            ("p", "<strong>Bij een elektrolyse en in een galvanische cel gebeurt de oxidatie "
                  "telkens aan de anode</strong>; alleen het teken van de polen verschilt. Bij een "
                  "elektrolyse is <strong>de kathode de negatieve pool</strong>, want de "
                  "spanningsbron duwt daar elektronen naartoe, en "
                  "<strong>de anode de positieve pool</strong>, waar ze elektronen wegtrekt. De "
                  "<strong>positieve ionen bewegen dus naar de kathode</strong> en niet naar de "
                  "anode."),
            ("p", "Wat een galvanische cel en een elektrolyse gemeen hebben: "
                  "<strong>er is een oxidatie en een reductie</strong> en "
                  "<strong>er moeten ionen kunnen bewegen in de vloeistof</strong>. Wat ze "
                  "onderscheidt: <strong>de reactie is spontaan of gedwongen</strong> en "
                  "<strong>het teken van de polen is omgekeerd</strong>. Daarom kan je "
                  "<strong>gesmolten keukenzout elektrolyseren en vast keukenzout niet</strong>: "
                  "<strong>in de smelt kunnen de ionen bewegen, in het vaste rooster niet</strong>."),
            ("p", "Drie toepassingen. Bij de elektrolyse van een oplossing van een koperzout "
                  "<strong>slaat koper als metaal op de kathode neer</strong>. Bij de "
                  "<strong>elektrolyse van water</strong> ontstaat het "
                  "<strong>waterstofgas aan de kathode, want daar gebeurt de reductie</strong>, en "
                  "het volume waterstofgas is dubbel dat van het zuurstofgas. En "
                  "<strong>aluminium</strong> maakt men met elektrolyse omdat "
                  "<strong>het aluminiumion een te zwakke oxidator is om spontaan te "
                  "reageren</strong>; daarom kost het veel elektriciteit."),
            ("p", "<strong>Galvaniseren</strong> is "
                  "<strong>het aanbrengen van een metaallaagje met behulp van elektrolyse</strong>, "
                  "zoals verzilveren en verkoperen. Het <strong>voorwerp</strong> hangt daarbij aan "
                  "de <strong>negatieve pool</strong>, de kathode, want daar gebeurt de reductie. "
                  "Bij het verzilveren <strong>lost de zilveren anode langzaam op in de "
                  "oplossing</strong>, zodat de concentratie zilverionen gelijk blijft."),
            ("p", "Laad je een <strong>oplaadbare batterij</strong> op, dan "
                  "<strong>wordt de reactie door een elektrolyse teruggeduwd</strong>. Opladen is "
                  "dus een gedwongen reactie: het kost energie, terwijl ontladen ze levert."),
        ]),
    ],
    onthoud=[
        "Oxidatie altijd aan de anode, reductie altijd aan de kathode.",
        "Galvanische cel: anode negatief. Elektrolyse: anode positief.",
        "Elektronen door de draad, ionen door de zoutbrug.",
        "Bronspanning = normpotentiaal kathode min die van de anode.",
        "De anode lost op, de kathode wordt zwaarder.",
        "Elektrolyse is gedwongen en verbruikt energie; een cel levert ze.",
        "Galvaniseren: het voorwerp hangt aan de kathode.",
    ],
)

# ───────────────────── 16. Toepassingen van redox: batterijen, galvaniseren en corrosie
BUNDELS["toepassingen-van-redox-batterijen-galvaniseren-en-corrosie-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Toepassingen van redox: batterijen, galvaniseren en corrosie",
    onder="Wat er in een batterij gebeurt, hoe je een laagje metaal aanbrengt, en hoe roest werkt.",
    secties=[
        dict(kop="Batterijen en brandstofcellen", blokken=[
            ("p", "Een batterij levert spanning omdat "
                  "<strong>er binnenin een spontane redoxreactie verloopt</strong>; het verschil in "
                  "normpotentiaal tussen de twee koppels is "
                  "<strong>de bronspanning in volt</strong>, en hoeveel lading er in zit staat er "
                  "apart bij in milliampère-uur. De <strong>anode van een batterij</strong> is "
                  "<strong>de negatieve</strong> pool, waar de oxidatie gebeurt. Een batterij "
                  "<strong>levert gelijkspanning</strong>, want de oxidatie gebeurt altijd aan "
                  "dezelfde pool; het stopcontact levert wisselspanning. Ze "
                  "<strong>raakt leeg</strong> omdat "
                  "<strong>de stoffen die de reactie voeden, opgebruikt zijn</strong>."),
            ("p", "<strong>Een batterij mag je niet kortsluiten</strong>, want "
                  "<strong>de reactie loopt dan heel snel en de batterij wordt gevaarlijk "
                  "warm</strong>: zonder weerstand in de kring beperkt niets de stroom, en bij een "
                  "lithiumbatterij kan dat brand geven. <strong>Oude batterijen horen bij het klein "
                  "gevaarlijk afval</strong> omdat "
                  "<strong>ze zware metalen bevatten die in het milieu terechtkomen</strong>; bij "
                  "de inzameling worden die metalen teruggewonnen."),
            ("p", "Een <strong>oplaadbare</strong> batterij of <strong>accu</strong> kan je opnieuw "
                  "opladen: <strong>de reactie wordt door een elektrolyse teruggeduwd</strong> en "
                  "de stoffen van het begin worden opnieuw gevormd. Op lange termijn is ze "
                  "goedkoper omdat je <strong>de reactie honderden keren kan terugduwen met een "
                  "lader</strong>, al gaat elke cyclus een beetje slechter. "
                  "<strong>Een gewone alkalinebatterij kan je niet veilig opladen</strong>: haar "
                  "reactie is niet goed omkeerbaar, er ontstaat gas, en dan kan de cel openbarsten "
                  "of lekken."),
            ("p", "In een <strong>brandstofcel wordt de brandstof voortdurend aangevoerd</strong>, "
                  "en daarom raakt ze niet leeg. Ze "
                  "<strong>zet chemische energie direct om in elektrische energie</strong> en "
                  "<strong>blijft werken zolang er brandstof aangevoerd wordt</strong>: het is een "
                  "galvanische cel met een open toevoer, die je dus bijvult in plaats van oplaadt. "
                  "Aan een waterstofbrandstofcel voedt men "
                  "<strong>waterstof en zuurstof</strong> aan: het waterstofgas wordt aan de anode "
                  "geoxideerd en het zuurstofgas aan de kathode gereduceerd, en het "
                  "<strong>reactieproduct is water</strong>, dus geen broeikasgas."),
        ]),
        dict(kop="Galvaniseren in de praktijk", blokken=[
            ("p", "Bij <strong>galvaniseren</strong> "
                  "<strong>hangt het voorwerp aan de kathode</strong> en "
                  "<strong>wordt er een laagje metaal op het voorwerp neergeslagen</strong>, want "
                  "daar gebeurt de reductie. Het aanbrengen van een dun laagje zilver heet "
                  "<strong>verzilveren</strong>: het voorwerp hangt in een oplossing van een "
                  "zilverzout en de zilveren anode lost langzaam op. Bij het "
                  "<strong>verkoperen</strong> <strong>levert de anode koperionen, doordat ze zelf "
                  "oplost</strong>, zodat de concentratie in het bad gelijk blijft."),
            ("p", "Men verguldt of verzilvert juwelen in plaats van ze volledig uit dat metaal te "
                  "maken omdat <strong>een dun laagje volstaat voor het uitzicht en veel minder "
                  "kost</strong>; de kern mag van een goedkoper metaal zijn. "
                  "<strong>De dikte van het laagje ligt daarbij niet vast</strong>: hoe langer en "
                  "hoe sterker de stroom, hoe meer metaal er neerslaat, want dat volgt rechtstreeks "
                  "uit het aantal elektronen dat erdoor gaat."),
        ]),
        dict(kop="Corrosie en roest", blokken=[
            ("p", "<strong>Corrosie</strong> is "
                  "<strong>het aantasten van een metaal door een redoxreactie met zijn "
                  "omgeving</strong>: het metaal wordt geoxideerd, meestal door zuurstof uit de "
                  "lucht. Om te roesten heeft ijzer "
                  "<strong>zuurstof en water</strong> nodig; in droge lucht of onder water zonder "
                  "zuurstof roest het bijna niet. Bij het roesten "
                  "<strong>wordt het ijzer geoxideerd tot ionen</strong> en "
                  "<strong>wordt het zuurstofgas gereduceerd</strong>: ijzer speelt dus de rol van "
                  "<strong>reductor</strong> en water is enkel het midden waarin de ionen kunnen "
                  "bewegen."),
            ("p", "<strong>Een auto roest sneller aan de kust of in de winter</strong> omdat "
                  "<strong>zout het water geleidend maakt en de redoxreactie versnelt</strong>: de "
                  "ionen laten de lading door het laagje water stromen, zodat de oxidatie op de ene "
                  "plaats en de reductie op de andere kan gebeuren."),
            ("p", "<strong>Roest beschermt het metaal eronder niet</strong>: hij is poreus en laat "
                  "water en lucht door. Bij <strong>aluminium</strong> is dat anders — "
                  "<strong>er vormt zich een dicht laagje oxide dat de rest afschermt</strong> — en "
                  "daarom corrodeert aluminium in de praktijk zo weinig, al is het juist een sterke "
                  "reductor. Algemeen geldt: "
                  "<strong>een metaal dat laag in de tabel van de normpotentialen staat, "
                  "corrodeert juist makkelijker</strong>, want laag betekent een sterke reductor; "
                  "goud en platina staan hoog en corroderen bijna niet."),
        ]),
        dict(kop="Beschermen tegen corrosie", blokken=[
            ("p", "De eenvoudigste bescherming is een barrière. "
                  "<strong>Een laag verf beschermt ijzer doordat ze het van lucht en water "
                  "afsluit</strong>, maar komt er een kras in, dan begint het roesten daar. "
                  "<strong>Vet of olie op een gereedschap</strong> werkt net zo: "
                  "<strong>het laagje houdt water en zuurstof van het metaal weg</strong>, en "
                  "beschermt niet meer zodra het weg is."),
            ("p", "Een <strong>laagje zink</strong> beschermt ijzer ook nog "
                  "<strong>als er een kras in zit</strong>, want "
                  "<strong>zink is de sterkere reductor en wordt in plaats van het ijzer "
                  "aangetast</strong>. Dat aanbrengen van zink op staal heet "
                  "<strong>verzinken</strong> of galvaniseren, door onderdompelen in gesmolten zink "
                  "of met elektrolyse; dakgoten en schroeven zijn vaak zo behandeld. Bij een "
                  "<strong>conservenblik roest het juist op een kras in het tinlaagje</strong>, "
                  "want <strong>tin is een zwakkere reductor, dus wordt het ijzer "
                  "aangetast</strong>."),
            ("p", "<strong>Kathodische bescherming</strong> is "
                  "<strong>de bescherming waarbij je het metaal aan de negatieve pool legt</strong>: "
                  "als kathode kan het geen elektronen meer afstaan. "
                  "<strong>Dat kan ook zonder spanningsbron, met een onedeler metaal</strong>, en "
                  "dan heet dat een <strong>verteringselektrode</strong>. Zo'n elektrode "
                  "<strong>is van een metaal dat een sterkere reductor is</strong> en "
                  "<strong>wordt opgebruikt en moet af en toe vervangen worden</strong>; daarom "
                  "hoort ze op het onderhoudsschema. Men hangt "
                  "<strong>magnesiumblokken aan een stalen scheepsromp</strong> omdat "
                  "<strong>het magnesium opgegeten wordt in plaats van het staal</strong>, en een "
                  "<strong>boiler met een anode van magnesium</strong> gaat langer mee omdat "
                  "<strong>de anode aangetast wordt in plaats van de stalen wand</strong>. Het "
                  "<strong>magnesium</strong> en zink zijn daarvoor de gebruikelijke metalen; welk "
                  "van de twee hangt af van het water of de grond errond."),
            ("p", "Twee manieren die werken, samengevat: "
                  "<strong>een laagje zink erop brengen</strong> en "
                  "<strong>een verteringselektrode van magnesium aansluiten</strong>. Aan de "
                  "positieve pool zou het ijzer juist de anode worden en dus sneller oxideren."),
        ]),
    ],
    onthoud=[
        "Een batterij is een spontane redoxreactie; leeg betekent de stoffen zijn op.",
        "Een accu laad je op met een elektrolyse; een alkalinebatterij niet.",
        "Een brandstofcel wordt bijgevuld en geeft enkel water.",
        "Galvaniseren: het voorwerp aan de kathode, de anode lost op.",
        "Roesten vraagt zuurstof én water; zout versnelt het.",
        "Zink beschermt ook door een kras heen, tin niet.",
        "Een verteringselektrode van magnesium wordt opgegeten in plaats van het staal.",
    ],
)

# ───────────────────── 17. Organische reacties: substitutie en het radicalaire mechanisme
BUNDELS["organische-reacties-substitutie-en-het-radicalaire-mechanisme-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Organische reacties: substitutie en het radicalaire mechanisme",
    onder="Vier reactietypes, drie soorten aanvallers, en de kettingreactie met radicalen.",
    secties=[
        dict(kop="Splitsen, aanvallen en de vier types", blokken=[
            ("p", "Een binding kan op twee manieren breken. Bij een "
                  "<strong>homolytische splitsing</strong> "
                  "<strong>houdt elk atoom één elektron van het bindende paar</strong>, en zo "
                  "ontstaan er twee <strong>radicalen</strong>: "
                  "<strong>een deeltje met een ongepaard elektron</strong>, dat daardoor heel "
                  "reactief is. Bij een <strong>heterolytische splitsing</strong> neemt één atoom "
                  "het hele paar mee, en dan ontstaat er een positief en een negatief deeltje. "
                  "<strong>Bij een heterolytische splitsing ontstaan er dus geen radicalen.</strong>"),
            ("p", "Een aanvallend deeltje dat <strong>een vrij elektronenpaar aanbiedt</strong>, "
                  "heet een <strong>nucleofiel</strong>: het zoekt een plaats met een "
                  "elektronentekort. Een <strong>elektrofiel</strong> zoekt juist "
                  "<strong>een plaats met veel elektronen, zoals een dubbele binding</strong>; het "
                  "betekent letterlijk elektronenvriend en valt dus de pi-elektronen van een alkeen "
                  "of een benzeenring aan."),
            ("p", "De vier organische reactietypes zijn "
                  "<strong>substitutie</strong>, <strong>additie</strong>, eliminatie en "
                  "condensatie; neutralisatie en neerslagvorming horen bij de anorganische chemie. "
                  "<strong>Bij een substitutiereactie wordt een atoom of groep vervangen door een "
                  "andere</strong>, en daarbij "
                  "<strong>verandert het aantal koolstofatomen van de hoofdketen niet</strong>. Bij "
                  "een additie komt er iets bij zonder dat er iets weggaat. Bij een "
                  "<strong>eliminatiereactie</strong> "
                  "<strong>gaat er een kleine molecule uit de stof en ontstaat er een dubbele "
                  "binding</strong>: water of een waterstofhalogenide gaat eruit. Bij een "
                  "<strong>condensatie</strong> koppelen "
                  "<strong>twee moleculen en komt er water vrij</strong>; het vormen van een ester "
                  "uit een alcohol en een carbonzuur is <strong>een condensatie, want er komt water "
                  "vrij</strong>, en de omgekeerde reactie met water heet hydrolyse."),
            ("p", "<strong>Een substitutie kan radicalair, elektrofiel of nucleofiel "
                  "verlopen.</strong> Welk van de drie het is, hangt af van de stof: een alkaan "
                  "radicalair, benzeen elektrofiel en een halogeenalkaan nucleofiel."),
        ]),
        dict(kop="De radicalaire substitutie van een alkaan", blokken=[
            ("p", "<strong>Een alkaan reageert niet met een elektrofiel</strong>, want "
                  "<strong>het heeft geen plaats met veel elektronen om aan te vallen</strong>: "
                  "alle bindingen zijn sigma-bindingen en bijna apolair. Daarom heeft een alkaan "
                  "een radicaal nodig om toch te reageren, en is "
                  "<strong>uv-licht</strong> of warmte nodig om de reactie te starten."),
            ("p", "Zo'n reactie "
                  "<strong>verloopt in drie soorten stappen</strong>. In de "
                  "<strong>initiatiestap</strong> "
                  "<strong>splitst het dihalogeen homolytisch in twee radicalen</strong>: Cl₂ wordt "
                  "onder uv-licht twee chloorradicalen. In de "
                  "<strong>propagatiestappen</strong> "
                  "<strong>reageert een radicaal en ontstaat er telkens een nieuw radicaal</strong>, "
                  "zodat de reactie als een ketting doorloopt; één lichtdeeltje kan zo duizenden "
                  "moleculen laten reageren. In de laatste stap, de "
                  "<strong>terminatie</strong>, "
                  "<strong>ontstaan er geen twee nieuwe radicalen</strong> maar koppelen twee "
                  "radicalen tot een molecule zonder ongepaard elektron, en stopt die ketting. "
                  "Daarom vindt men bij de chlorering van methaan ook wat ethaan in het mengsel "
                  "terug."),
            ("p", "Bij de radicalaire substitutie van methaan met chloorgas ontstaan er "
                  "<strong>chloormethaan en waterstofchloride</strong>: één waterstofatoom wordt "
                  "door chloor vervangen, en dat waterstofatoom gaat met het tweede chlooratoom mee "
                  "als HCl. Zo'n reactie "
                  "<strong>geeft een mengsel van verschillende producten</strong>, want er kan een "
                  "tweede en een derde waterstofatoom vervangen worden. Ook bij de "
                  "<strong>chlorering van een cycloalkaan onder uv-licht</strong> valt "
                  "<strong>een radicaal</strong> aan, want een cycloalkaan is net als een alkaan "
                  "verzadigd en apolair."),
        ]),
        dict(kop="De elektrofiele substitutie van benzeen", blokken=[
            ("p", "Benzeen ondergaat een substitutie en geen additie met broom omdat "
                  "<strong>de ring bij een additie haar stabiele elektronenwolk zou "
                  "verliezen</strong>: de verspreide pi-elektronen maken benzeen bijzonder stabiel, "
                  "en een substitutie houdt de ring intact. Het aanvallende deeltje is een "
                  "<strong>elektrofiel</strong>, want de ring is rijk aan elektronen."),
            ("p", "Met broom en een katalysator ontstaan er "
                  "<strong>broombenzeen en waterstofbromide</strong>. Die "
                  "<strong>katalysator is nodig omdat ze het broom pas echt elektrofiel "
                  "maakt</strong>: met een stof als ijzerbromide wordt het broommolecule "
                  "gepolariseerd, en dan is het sterk genoeg om de stabiele ring aan te vallen. Het "
                  "verschil met de chlorering van methaan is dus dat "
                  "<strong>bij methaan een radicaal aanvalt en bij benzeen een elektrofiel</strong>: "
                  "methaan heeft uv-licht nodig, benzeen een katalysator, en in beide gevallen "
                  "wordt een waterstofatoom vervangen."),
        ]),
        dict(kop="De nucleofiele substitutie van een halogeenalkaan", blokken=[
            ("p", "Bij een halogeenalkaan is "
                  "<strong>het koolstofatoom naast het halogeen lichtpositief</strong> en "
                  "<strong>valt het nucleofiel juist dat koolstofatoom aan</strong>: het halogeen is "
                  "sterk elektronegatief en trekt de elektronen naar zich toe. "
                  "<strong>Een alkaan reageert dus niet makkelijker met een nucleofiel dan een "
                  "halogeenalkaan</strong>, want in een alkaan is er geen plaats met zo'n tekort. "
                  "De naam zegt waarom het nucleofiel heet: "
                  "<strong>het aanvallende deeltje brengt zelf een elektronenpaar mee</strong>."),
            ("p", "<strong>Bij een nucleofiele substitutie verlaat het halogeen de molecule als "
                  "ion</strong>, want de binding splitst heterolytisch. Bij broomethaan gaat dat "
                  "weg als <strong>bromide-ion</strong>, dat het hele bindende elektronenpaar "
                  "meeneemt."),
            ("p", "Welke producten krijg je? Met <strong>water</strong> ontstaat er "
                  "<strong>een alcohol</strong>, met een <strong>alcohol</strong> ontstaat er "
                  "<strong>een ether</strong>, en met <strong>ammoniak</strong> ontstaat er "
                  "<strong>een amine</strong>, doordat het vrije paar van de stikstof het "
                  "koolstofatoom aanvalt. Als nucleofiel kunnen onder meer "
                  "<strong>water</strong> en <strong>een amine</strong> optreden, want beide hebben "
                  "een vrij elektronenpaar, op zuurstof of op stikstof."),
            ("p", "Twee reacties tussen alcoholen en zuren om niet te verwarren. Uit een alcohol en "
                  "een carbonzuur ontstaat een <strong>ester</strong>: de "
                  "<strong>verestering</strong>, waarbij "
                  "<strong>er water vrijkomt</strong> en die "
                  "<strong>omkeerbaar is met water als reagens</strong>. "
                  "<strong>Uit een alcohol met een carbonzuur ontstaat dus geen ether</strong>; een "
                  "ether krijg je uit <strong>twee alcoholen</strong>, waarbij "
                  "<strong>een ether en water</strong> ontstaan, of uit een alcohol met een "
                  "halogeenalkaan. Valt een ester met water terug uiteen, dan heet dat "
                  "<strong>hydrolyse</strong>; met een base heet het "
                  "<strong>verzeping</strong>, en dan ontstaat het zout van het carbonzuur: zo "
                  "wordt zeep gemaakt."),
        ]),
    ],
    onthoud=[
        "Homolytisch geeft radicalen, heterolytisch geeft ionen.",
        "Nucleofiel brengt een elektronenpaar mee, elektrofiel zoekt er een.",
        "Substitutie vervangt, additie voegt toe, eliminatie haalt weg, condensatie koppelt.",
        "Alkaan radicalair met uv-licht, benzeen elektrofiel met katalysator.",
        "Initiatie, propagatie, terminatie; het mengsel bevat meerdere producten.",
        "Halogeenalkaan plus water geeft een alcohol, plus ammoniak een amine.",
        "Alcohol plus carbonzuur geeft een ester; hydrolyse draait het terug.",
    ],
)

# ───────────────────── 18. Organische reacties: additie, eliminatie en condensatie
BUNDELS["organische-reacties-additie-eliminatie-en-condensatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Organische reacties: additie, eliminatie en condensatie",
    onder="Een dubbele binding die opengaat, en een die juist ontstaat.",
    secties=[
        dict(kop="Additie aan een alkeen en een alkyn", blokken=[
            ("p", "Bij een <strong>additiereactie aan een alkeen</strong> "
                  "<strong>gaat de pi-binding open en komen er twee groepen bij</strong>. De "
                  "sigma-binding tussen de twee koolstofatomen blijft bestaan en de keten wordt "
                  "verzadigd. <strong>Een additie is geen substitutie</strong>, want "
                  "<strong>er gaat geen enkel atoom weg uit de molecule</strong>. Bij een "
                  "<strong>alkyn</strong> gaat er ook <strong>een pi-binding</strong> open, en "
                  "omdat er twee zijn, <strong>kan de additie twee keer gebeuren</strong>. Ook een "
                  "<strong>cycloalkeen kan een additie ondergaan</strong>: de ring blijft bestaan en "
                  "de dubbele binding erin gaat open; het is de ring van benzeen die niet addeert."),
            ("p", "Wat kan adderen? Onder meer "
                  "<strong>waterstofchloride</strong> en <strong>diwaterstof</strong>: aan een "
                  "dubbele binding adderen diwaterstof, een dihalogeen, een waterstofhalogenide en "
                  "water. Een zout addeert niet."),
            ("p", "De producten, één voor één. De additie van "
                  "<strong>diwaterstof aan etheen</strong> geeft "
                  "<strong>ethaan</strong>; die <strong>hydrogenering</strong> heeft een "
                  "katalysator van nikkel of platina nodig, en zo maakt men van vloeibare olie een "
                  "vaster vet. De additie van <strong>broom aan een alkeen</strong> geeft "
                  "<strong>een dibroomalkaan</strong>: elk koolstofatoom van de dubbele binding "
                  "krijgt één broomatoom. De additie van "
                  "<strong>water aan etheen, met een zuur als katalysator</strong>, geeft "
                  "<strong>ethanol</strong>, en zo maakt men industrieel alcohol. "
                  "<strong>De additie van water verloopt dus niet zonder katalysator</strong>: "
                  "zonder zuur zou water veel te zwak zijn."),
            ("p", "Daarop berust een test. Men gebruikt <strong>broomwater</strong> om te weten of "
                  "een stof onverzadigd is, want "
                  "<strong>het broom reageert weg en de bruine kleur verdwijnt</strong>; bij een "
                  "alkaan gebeurt er in het donker niets."),
            ("p", "De <strong>verzadigingsgraad</strong> "
                  "<strong>zegt hoeveel keer diwaterstof er kan adderen</strong>, en "
                  "<strong>een alkyn heeft een verzadigingsgraad van twee</strong>: "
                  "<strong>een alkyn kan dus twee keer diwaterstof opnemen</strong>, eerst tot een "
                  "dubbele en dan tot een enkelvoudige binding. Een alkaan is al verzadigd en heeft "
                  "dus verzadigingsgraad nul."),
            ("p", "De <strong>regel van Markownikov</strong> zegt dat "
                  "<strong>het waterstofatoom naar het koolstofatoom met het meeste waterstof "
                  "gaat</strong>; het halogeen of de OH-groep komt dus op het meest vertakte "
                  "koolstofatoom. Laat je <strong>HCl adderen aan propeen</strong>, dan overheerst "
                  "dus <strong>2-chloorpropaan</strong>."),
        ]),
        dict(kop="Elektrofiel of nucleofiel adderen", blokken=[
            ("p", "Bij de additie van <strong>HBr aan een alkeen</strong> valt "
                  "<strong>een elektrofiel</strong> aan: de pi-elektronen van de dubbele binding "
                  "trekken het lichtpositieve waterstofatoom aan, en daarom heet het een "
                  "<strong>elektrofiele additie</strong>."),
            ("p", "Bij een aldehyde of een keton is het omgekeerd, want "
                  "<strong>het koolstofatoom van de C=O-groep is lichtpositief en trekt een "
                  "nucleofiel aan</strong>: zuurstof trekt de elektronen van de dubbele binding "
                  "naar zich toe, terwijl bij een alkeen beide atomen gelijk zijn. "
                  "<strong>Bij een nucleofiele additie aan een aldehyde ontstaat er een primaire "
                  "alcohol</strong>, want de C=O-groep aan het uiteinde wordt een CH-OH-groep. De "
                  "additie van <strong>diwaterstof aan een aldehyde</strong> geeft dus "
                  "<strong>een primaire alcohol</strong>, en die aan "
                  "<strong>propanon</strong> geeft <strong>propaan-2-ol</strong>, een secundaire "
                  "alcohol, want de C=O-groep zit in het midden."),
        ]),
        dict(kop="Eliminatie: water of waterstof eruit", blokken=[
            ("p", "<strong>Een eliminatie maakt een verzadigde keten onverzadigd</strong>: er gaan "
                  "twee groepen weg van twee buuratomen en daar komt een dubbele binding. "
                  "<strong>Een eliminatie is dan ook het omgekeerde van een additie.</strong>"),
            ("p", "Bij de <strong>dehydratatie</strong> of "
                  "<strong>waterafsplitsing</strong> van een alcohol "
                  "<strong>gaat er water uit en ontstaat er een dubbele binding</strong>: de "
                  "OH-groep en een waterstofatoom van het buuratoom gaan samen weg. "
                  "<strong>Het is een eliminatiereactie</strong> en "
                  "<strong>er ontstaat een alkeen uit een alcohol</strong>. In het labo heb je "
                  "daarvoor <strong>geconcentreerd zwavelzuur en warmte</strong> nodig. De "
                  "dehydratatie van <strong>butaan-2-ol</strong> levert twee verschillende alkenen "
                  "op, want <strong>het water kan aan twee kanten van de OH-groep weggaan</strong>: "
                  "je krijgt but-1-een en but-2-een naast elkaar."),
            ("p", "Bij de <strong>dehydrogenatie</strong> gaat er diwaterstof uit. Een "
                  "<strong>primaire alcohol</strong> wordt dan "
                  "<strong>een aldehyde</strong> en een "
                  "<strong>secundaire alcohol</strong> wordt "
                  "<strong>een keton</strong>; propaan-2-ol geeft propanon en "
                  "<strong>butaan-2-ol</strong> geeft <strong>butanon</strong>. "
                  "<strong>Een tertiaire alcohol kan geen dehydrogenatie ondergaan</strong> omdat "
                  "<strong>het koolstofatoom met de OH-groep geen waterstofatoom meer heeft</strong>: "
                  "bij zo'n alcohol "
                  "<strong>draagt dat koolstofatoom drie koolstofketens</strong>, maar "
                  "<strong>ze kan wel een dehydratatie ondergaan</strong>, want daarvoor moet er "
                  "enkel een waterstofatoom op een buuratoom zitten. Bij een "
                  "<strong>secundaire alcohol</strong> zitten er "
                  "<strong>twee</strong> koolstofketens aan dat koolstofatoom; bij een primaire één."),
            ("p", "Ook bij een halogeenalkaan kan je elimineren: uit broomethaan ontstaat "
                  "<strong>etheen</strong>, want het broomatoom en een waterstofatoom van het "
                  "buuratoom gaan samen weg als HBr. "
                  "<strong>Dat verloopt niet zonder base</strong>: de base haalt juist dat "
                  "waterstofatoom weg, en zonder base verloopt eerder een nucleofiele substitutie. "
                  "<strong>Een eliminatie bij een alcohol en een eliminatie bij een halogeenalkaan "
                  "geven beide een alkeen.</strong>"),
        ]),
        dict(kop="Oxideren en condenseren", blokken=[
            ("p", "De oxidatieladder van een primaire alcohol loopt van alcohol over aldehyde naar "
                  "carbonzuur. Oxideer je <strong>propaan-1-ol</strong> voorzichtig, dan ontstaat "
                  "er eerst <strong>propanal</strong>. "
                  "<strong>Bij de oxidatie van een primaire alcohol kan je wel stoppen bij het "
                  "aldehyde</strong>, met een voorzichtige oxidator en door het aldehyde af te "
                  "destilleren. Oxideer je <strong>volledig</strong>, dan krijg je "
                  "<strong>een carbonzuur</strong>; daarom wordt wijn die te lang openstaat azijn."),
            ("p", "Bij een <strong>condensatie tussen een carbonzuur en een alcohol</strong> "
                  "ontstaan er <strong>een ester</strong> en <strong>water</strong>: de OH van het "
                  "zuur en de H van de alcohol gaan samen weg, en wat overblijft koppelt tot de "
                  "ester."),
        ]),
    ],
    onthoud=[
        "Additie opent de pi-binding; er gaat niets weg.",
        "Broomwater ontkleurt bij een onverzadigde stof.",
        "Verzadigingsgraad: alkeen één, alkyn twee, alkaan nul.",
        "Markownikov: de waterstof gaat naar de koolstof met het meeste waterstof.",
        "Alkeen addeert elektrofiel, een C=O-groep nucleofiel.",
        "Dehydratatie geeft een alkeen, dehydrogenatie een aldehyde of keton.",
        "Primair geeft aldehyde dan zuur, secundair geeft keton, tertiair geen van beide.",
    ],
)

# ───────────────────── 19. Kunststoffen: polymeren en hun eigenschappen
BUNDELS["kunststoffen-polymeren-en-hun-eigenschappen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunststoffen: polymeren en hun eigenschappen",
    onder="Van monomeer naar keten, en waarom de ene plooit en de andere niet.",
    secties=[
        dict(kop="Monomeer en polymeer", blokken=[
            ("p", "Een <strong>polymeer</strong> is "
                  "<strong>een heel lange molecule van veel gelijke bouwstenen</strong>. Die "
                  "bouwsteen heet het <strong>monomeer</strong>: mono betekent één, poly veel, en "
                  "twee bouwstenen samen vormen een <strong>dimeer</strong>. In één polymeerketen "
                  "zitten er <strong>duizenden</strong> monomeren. Daarom is de molaire massa van "
                  "een kunststof enorm en verschilt ze van keten tot keten, en daarom "
                  "<strong>heeft een kunststof geen scherp smeltpunt zoals een zout</strong> maar "
                  "een <strong>smelttraject</strong>."),
            ("p", "<strong>De eigenschappen van een kunststof volgen uit de bouw van haar "
                  "ketens</strong>: de lengte van de ketens, hun zijgroepen en het aantal "
                  "crosslinks bepalen of het materiaal hard, buigzaam of elastisch is."),
        ]),
        dict(kop="Twee manieren om te polymeriseren", blokken=[
            ("p", "Bij een <strong>polymerisatie</strong> of "
                  "<strong>polyadditie</strong> "
                  "<strong>gaan de dubbele bindingen open en komt er geen bijproduct vrij</strong>. "
                  "<strong>Bij een polyadditie zit de volledige massa van de monomeren in het "
                  "polymeer</strong>, dus is de atoomeconomie heel hoog. Een "
                  "<strong>monomeer voor een polyadditie moet een dubbele binding hebben</strong>, "
                  "want die levert de twee nieuwe bindingen naar de buren; een verzadigd alkaan kan "
                  "dus niet polymeriseren."),
            ("p", "Bij een <strong>polycondensatie</strong> verdwijnt er bij elke koppeling een "
                  "kleine molecule, meestal <strong>water</strong>. Daarom zit niet alle massa van "
                  "de monomeren in het polymeer. <strong>PET</strong> en "
                  "<strong>PA of nylon</strong> worden zo gemaakt; PE en PS komen van een "
                  "polyadditie. <strong>Nylon heeft twee verschillende monomeren nodig</strong> "
                  "omdat <strong>een amidebinding ontstaat tussen een zuurgroep en een "
                  "aminegroep</strong>: het ene monomeer brengt de COOH-groepen aan, het andere de "
                  "NH₂-groepen. <strong>PET</strong> "
                  "<strong>wordt gemaakt uit een tweewaardige alcohol en een tweewaardig "
                  "zuur</strong> en <strong>wordt met een polycondensatie gemaakt</strong>; de "
                  "esterbindingen geven het zijn naam, polyethyleentereftalaat, en daarom kan je het "
                  "ook weer afbreken met water."),
            ("p", "Om het monomeer uit de structuur van een polyadditiepolymeer terug te vinden, "
                  "<strong>neem je het stukje dat zich herhaalt en zet je de dubbele binding "
                  "terug</strong>. Dat herhalende stukje heet de "
                  "<strong>repeterende eenheid</strong>: bij PVC is dat CH₂-CHCl, en dus is het "
                  "monomeer chlooretheen."),
            ("p", "De monomeren om te kennen: <strong>PE</strong> komt van "
                  "<strong>etheen</strong>, met <strong>een polyadditie</strong>; "
                  "<strong>PVC</strong> van <strong>chlooretheen</strong>, ook wel vinylchloride, "
                  "vandaar de naam; <strong>PP</strong> van <strong>propeen</strong>, waarvan de "
                  "methylgroep als zijgroep in de keten hangt en PP steviger maakt dan PE; "
                  "<strong>PS</strong> van <strong>fenyletheen</strong> of styreen, een "
                  "etheenmolecule met een benzeenring eraan; en "
                  "<strong>PTFE</strong> van <strong>tetrafluoretheen</strong>, waarin alle vier de "
                  "waterstofatomen van etheen vervangen zijn door fluor. "
                  "<strong>PVC en PE hebben dus niet hetzelfde monomeer</strong>: dat ene "
                  "chlooratoom maakt de eigenschappen helemaal anders."),
        ]),
        dict(kop="Thermoplast, thermoharder en elastomeer", blokken=[
            ("p", "De bruggen tussen de ketens heten <strong>crosslinks</strong> of "
                  "<strong>dwarsverbindingen</strong>. Veel crosslinks geven een thermoharder, "
                  "enkele een elastomeer en geen een thermoplast."),
            ("p", "Een <strong>thermoplast</strong> "
                  "<strong>wordt zacht bij verwarmen en is opnieuw te vormen</strong>: "
                  "<strong>de ketens liggen los naast elkaar</strong> en "
                  "<strong>worden enkel door intermoleculaire krachten samengehouden</strong>, dus "
                  "verbreekt verwarmen die zwakke krachten en niet de bindingen in de ketens zelf. "
                  "PE, PP, PET, PVC en PS horen daarbij."),
            ("p", "Een <strong>thermoharder</strong> "
                  "<strong>ontleedt of verbrandt zonder eerst te smelten</strong>, want de ketens "
                  "zitten met veel crosslinks vast aan elkaar en kunnen niet verschuiven. "
                  "<strong>Je kan hem dus niet opnieuw in een andere vorm persen.</strong> Voor een "
                  "<strong>tandwiel</strong> is een thermoharder beter omdat hij "
                  "<strong>niet vervormt als het mechanisme warm wordt</strong>."),
            ("p", "Een <strong>elastomeer</strong> "
                  "<strong>vervormt onder een kracht en veert daarna terug</strong>, want enkele "
                  "crosslinks houden de ketens samen en laten ze toch uitrekken. Wil je een "
                  "voorwerp dat terugveert na het indrukken, dan kies je dus "
                  "<strong>een elastomeer</strong>. "
                  "<strong>Gevulkaniseerd rubber heeft wel crosslinks</strong>, namelijk bruggen "
                  "van zwavel, en die maken van kleverig natuurrubber een elastomeer dat terugveert."),
            ("p", "<strong>Een thermoplast is beter te recycleren dan een thermoharder</strong>, "
                  "want hij kan opnieuw gesmolten en gevormd worden; een thermoharder kan alleen "
                  "nog vermalen worden als vulstof. Bij recycleren geldt verder: "
                  "<strong>gesorteerde, zuivere kunststof levert een beter product op</strong> en "
                  "<strong>een thermoplast kan opnieuw gesmolten worden</strong>. Gemengde kunststof "
                  "geeft een materiaal van mindere kwaliteit, en dat heet downcycling."),
        ]),
        dict(kop="Welke kunststof waarvoor", blokken=[
            ("p", "<strong>PE</strong> zit in een <strong>plastic zak</strong>: zacht, buigzaam en "
                  "goedkoop, met een hardere variant voor flessen en emmers. "
                  "<strong>PET</strong> is de kunststof voor <strong>drankflessen</strong>, want "
                  "het is sterk, doorzichtig en laat weinig gas door; daarom staat de recyclagecode "
                  "1 erop. <strong>PVC</strong> dient onder meer voor "
                  "<strong>buizen voor afvoer</strong> en "
                  "<strong>profielen voor een raam</strong>, want het is stevig en weerbestendig."),
            ("p", "<strong>PS-schuim</strong> dient als verpakking omdat "
                  "<strong>het heel licht is en tegen stoten beschermt</strong>: het bestaat bijna "
                  "volledig uit lucht. <strong>PUR</strong> of "
                  "<strong>polyurethaan</strong> is het <strong>isolatieschuim</strong> in een "
                  "huis, want de kleine gasbelletjes geleiden de warmte slecht. "
                  "<strong>PTFE</strong> of teflon zit in de "
                  "<strong>antikleeflaag van een pan</strong>: de fluoratomen maken het oppervlak "
                  "heel apolair, dus blijft er niets aan plakken. En "
                  "<strong>PA</strong> of <strong>nylon</strong> dient voor "
                  "<strong>kleding en touw</strong>, want de amidebindingen maken de vezel sterk — "
                  "dezelfde soort binding als in een eiwit."),
            ("p", "<strong>Microplastics zijn een probleem</strong> omdat "
                  "<strong>ze niet afbreken en in het water en in de voedselketen terechtkomen</strong>: "
                  "de ketens zijn zo stabiel dat bacteriën er niet aan kunnen, en daarom blijven de "
                  "deeltjes honderden jaren rondzwerven."),
        ]),
    ],
    onthoud=[
        "Monomeer is de bouwsteen, polymeer de lange keten van duizenden ervan.",
        "Polyadditie: dubbele binding open, geen bijproduct. Polycondensatie: water eruit.",
        "PE etheen, PVC chlooretheen, PP propeen, PS fenyletheen, PTFE tetrafluoretheen.",
        "PET en nylon komen van een polycondensatie.",
        "Geen crosslinks: thermoplast. Enkele: elastomeer. Veel: thermoharder.",
        "Een thermoplast is herbruikbaar, een thermoharder niet.",
        "Een kunststof heeft een smelttraject, geen scherp smeltpunt.",
    ],
)

# ───────────────────── 20. Nanomaterialen
BUNDELS["nanomaterialen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Nanomaterialen",
    onder="Waarom dezelfde stof op nanomaat heel andere eigenschappen krijgt.",
    secties=[
        dict(kop="Hoe klein is nano", blokken=[
            ("p", "Een <strong>nanometer</strong> is "
                  "<strong>een miljardste van een meter</strong>, dus 10⁻⁹ m. Een nanomateriaal "
                  "ligt tussen <strong>1 en 100</strong> nanometer: onder één nanometer kom je bij "
                  "losse atomen en moleculen, erboven bij gewoon materiaal. Een atoom is ongeveer "
                  "een tiende van een nanometer en een "
                  "<strong>menselijke haar is duizenden keren groter</strong> dan een nanodeeltje, "
                  "ongeveer 80 000 nanometer dik. <strong>Nanodeeltjes zijn met een gewone "
                  "lichtmicroscoop niet te zien</strong>, want ze zijn kleiner dan de golflengte "
                  "van licht; daarvoor heb je een "
                  "<strong>elektronenmicroscoop</strong> nodig."),
            ("p", "Men deelt nanomaterialen in naar het aantal richtingen waarin ze klein zijn. Een "
                  "<strong>0D-nanomateriaal</strong> is "
                  "<strong>een deeltje dat in alle drie de richtingen nanoklein is</strong>, zoals "
                  "een <strong>buckyball</strong> of een <strong>quantumdot</strong>. Bij "
                  "<strong>1D</strong> is één richting lang, zoals bij een nanobuis of een "
                  "nanodraad; bij <strong>2D</strong> zijn twee richtingen groot, en "
                  "<strong>grafeen is een 2D-nanomateriaal</strong>. Een "
                  "<strong>3D-nanomateriaal</strong> is "
                  "<strong>een gewoon groot materiaal met een structuur op nanomaat erin</strong>, "
                  "zoals een materiaal vol nanoporen of nanokorrels."),
            ("p", "Er zijn twee manieren om ze te maken. "
                  "<strong>Top-down</strong> begint bij groot materiaal en haalt er stukken af: "
                  "<strong>een vaste stof fijnmalen tot nanodeeltjes</strong> en "
                  "<strong>een laag wegetsen tot er een nanopatroon overblijft</strong>. "
                  "<strong>Bottom-up</strong> betekent "
                  "<strong>het materiaal opbouwen vanuit losse atomen of moleculen</strong>, "
                  "bijvoorbeeld atomen laten neerslaan tot een dun laagje of moleculen zichzelf "
                  "laten ordenen."),
        ]),
        dict(kop="De drie koolstofvormen", blokken=[
            ("p", "<strong>Grafeen</strong> en <strong>de buckyball</strong> zijn nanomaterialen; "
                  "diamant in een ring en houtskool zijn gewone vormen van koolstof. "
                  "<strong>Grafeen</strong> is <strong>één laag koolstofatomen in een "
                  "honingraatpatroon</strong>. Het is <strong>sterk</strong> omdat "
                  "<strong>de koolstofatomen met sterke bindingen in een vlak net zitten</strong>: "
                  "per gewicht veel sterker dan staal, en toch doorzichtig en buigbaar. Juist die "
                  "combinatie — <strong>doorzichtig en geleidend</strong> — maakt grafeen geschikt "
                  "voor een buigbaar scherm."),
            ("p", "De bekendste <strong>buckyball</strong> bestaat uit "
                  "<strong>60</strong> koolstofatomen, C₆₀, met de vorm van een voetbal uit vijf- "
                  "en zeshoeken. Een <strong>koolstofnanobuis</strong> is "
                  "<strong>een opgerolde laag koolstofatomen, dus 1D</strong>. Ze "
                  "<strong>geleidt elektrische stroom goed</strong> omdat "
                  "<strong>de elektronen van de pi-bindingen langs de hele buis kunnen "
                  "bewegen</strong>, en ze is geschikt om een materiaal te versterken door "
                  "<strong>haar grote sterkte bij een heel klein gewicht</strong>: nanobuizen in "
                  "een kunststof geven een licht en stevig materiaal voor sportgerief en luchtvaart."),
        ]),
        dict(kop="Waarom nanomaat andere eigenschappen geeft", blokken=[
            ("p", "De verhouding <strong>oppervlak tot volume</strong> "
                  "<strong>wordt groter als het deeltje kleiner wordt</strong> en "
                  "<strong>verklaart waarom nanodeeltjes zo reactief zijn</strong>. "
                  "<strong>Hoe kleiner een deeltje, hoe groter zijn oppervlak ten opzichte van zijn "
                  "volume</strong>: dat is de kern van de nanochemie."),
            ("p", "Daaruit volgt veel. Een <strong>nanodeeltje goud smelt bij een lagere "
                  "temperatuur dan een goudklomp</strong> omdat "
                  "<strong>een groot deel van de atomen aan het oppervlak zit en daar minder "
                  "vastzit</strong>. Een <strong>nanodeeltje van een metaal is reactiever dan een "
                  "blok</strong> omdat <strong>er veel meer oppervlak per gram is waar de reactie "
                  "kan gebeuren</strong> — hetzelfde idee als een poeder dat sneller brandt dan een "
                  "blok. En <strong>nanodeeltjes kunnen als katalysator werken met heel weinig "
                  "materiaal</strong>, want een katalysator werkt aan zijn oppervlak; het "
                  "<strong>voordeel van een nanokatalysator</strong> is dan ook dat "
                  "<strong>er veel minder materiaal nodig is voor hetzelfde effect</strong>. De "
                  "reactie-energie verandert daarbij niet."),
            ("p", "<strong>Een nanomateriaal heeft dus niet dezelfde eigenschappen als dezelfde "
                  "stof in het groot.</strong> Wat kan veranderen zijn de "
                  "<strong>optische eigenschappen, zoals de kleur</strong>, en de "
                  "<strong>mechanische eigenschappen, zoals de sterkte</strong>; het aantal "
                  "protonen en de molaire massa veranderen natuurlijk niet, want de stof blijft "
                  "chemisch dezelfde. Ook magnetisch kan het verschillen: "
                  "<strong>een nanomateriaal kan magnetisch zijn terwijl dezelfde stof in het groot "
                  "dat niet is</strong>, en dat gebruikt men in medische beeldvorming."),
            ("p", "<strong>Goud op nanomaat is niet goudkleurig</strong> omdat "
                  "<strong>de elektronen in zo'n klein deeltje anders op licht reageren</strong>; de "
                  "kleur hangt af van de grootte van het deeltje. Daarop berust de "
                  "<strong>kleur van een quantumdot in een scherm</strong>, een toepassing van de "
                  "optische eigenschappen."),
        ]),
        dict(kop="Toepassingen, voordelen en nadelen", blokken=[
            ("p", "In <strong>zonnecrème</strong> gebruikt men nanodeeltjes omdat "
                  "<strong>ze uv-licht tegenhouden en toch doorzichtig blijven op de huid</strong>. "
                  "Dat zijn <strong>zinkoxide</strong> en <strong>titaandioxide</strong>, die in "
                  "grove vorm een witte laag geven."),
            ("p", "Van <strong>zilvernanodeeltjes</strong> gebruikt men "
                  "<strong>hun antibacteriële werking</strong> in verband en sokken: door het grote "
                  "oppervlak komen er genoeg zilverionen vrij om bacteriën te doden. In een "
                  "<strong>covidtest</strong> zorgen nanodeeltjes van "
                  "<strong>goud</strong> voor de gekleurde streep; ze hangen aan antilichamen die "
                  "het virus herkennen. Op een etiket van een cosmetisch product schrijft men "
                  "<strong>nano</strong> <strong>zodat de koper weet dat er deeltjes op nanomaat in "
                  "zitten</strong>: de wet vraagt die vermelding omdat nanomaat andere "
                  "eigenschappen geeft. <strong>Nanotechnologie is dus geen zaak van de verre "
                  "toekomst</strong>: ze zit al in zonnecrème, verband, tandpasta, schermen en "
                  "autokatalysatoren."),
            ("p", "De nadelen: "
                  "<strong>hun effect op gezondheid en milieu is nog niet overal "
                  "onderzocht</strong> en <strong>ze zijn moeilijk te meten en te volgen in een "
                  "product</strong>. <strong>Nanodeeltjes in het lichaam zijn een risico</strong> "
                  "omdat <strong>ze zo klein zijn dat ze tot in de cellen kunnen komen</strong>. "
                  "<strong>Nanoplastics</strong> zijn in dat opzicht "
                  "<strong>kleiner dan microplastics</strong> en "
                  "<strong>kunnen door een celmembraan geraken</strong>: nano is duizend keer "
                  "kleiner dan micro."),
        ]),
    ],
    onthoud=[
        "Nano is 10⁻⁹ m; een nanomateriaal ligt tussen 1 en 100 nm.",
        "0D deeltje, 1D buis, 2D laag, 3D nanostructuur in een blok.",
        "Top-down maalt of etst, bottom-up bouwt op vanuit atomen.",
        "Grafeen is 2D, de buckyball C₆₀ is 0D, de nanobuis is opgerold grafeen.",
        "Kleiner deeltje, grotere verhouding oppervlak tot volume, dus reactiever.",
        "Zonnecrème zinkoxide en titaandioxide, verband zilver, covidtest goud.",
        "Risico: ze komen tot in de cellen en zijn moeilijk te volgen.",
    ],
)

# ───────────────────── 21. Duurzame chemie en de circulaire economie
BUNDELS["duurzame-chemie-en-de-circulaire-economie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Duurzame chemie en de circulaire economie",
    onder="Van wieg tot graf of van wieg tot wieg, en de woorden die daarbij horen.",
    secties=[
        dict(kop="Lineair, keten en circulair", blokken=[
            ("p", "Een <strong>lineaire economie</strong> loopt van "
                  "<strong>grondstof, product, gebruik en daarna afval dat verdwijnt</strong>. Die "
                  "keten heet <strong>van wieg tot graf</strong>, en in één woord is ze "
                  "<strong>lineair</strong>."),
            ("p", "Bij <strong>cradle to cradle</strong>, van wieg tot wieg, is "
                  "<strong>het afval van het ene product de grondstof van het volgende</strong>. Er "
                  "is dus geen eindpunt, en dat vraagt dat je al bij het ontwerp nadenkt over wat "
                  "er later met het materiaal gebeurt. In één woord is zo'n kringloop "
                  "<strong>circulair</strong>, en "
                  "<strong>in een circulaire economie bestaat het woord afval eigenlijk niet "
                  "meer</strong>: wat uit het ene proces komt, gaat als grondstof in het volgende. "
                  "In de praktijk haalt geen enkele keten dat volledig."),
            ("p", "Daartussen zit de <strong>keteneconomie</strong>: "
                  "<strong>een tussenvorm die veel hergebruikt maar toch nog afval "
                  "overhoudt</strong>. Er wordt al veel gerecycleerd, maar helemaal rond is de "
                  "cirkel nog niet."),
            ("p", "<strong>Downcycling</strong> is "
                  "<strong>recycleren tot een product van mindere kwaliteit</strong>: een petfles "
                  "die tot vulling voor een jas wordt, kan daarna niet meer terug naar een fles. "
                  "<strong>Downcycling en recyclage betekenen dus niet hetzelfde</strong>: bij "
                  "downcycling zakt de kwaliteit, terwijl recyclage op gelijk niveau het materiaal "
                  "bruikbaar houdt voor hetzelfde doel."),
            ("p", "Keuzes bij het ontwerp bepalen of een product in een kringloop past: "
                  "<strong>de onderdelen kunnen weer van elkaar los</strong> en "
                  "<strong>er zitten zo weinig verschillende materialen in</strong>. Wat je niet "
                  "kan scheiden, kan je niet zuiver recycleren."),
        ]),
        dict(kop="De ladder van Lansink", blokken=[
            ("p", "De <strong>ladder van Lansink</strong> zet de manieren van afvalbeheer op een "
                  "rij van best naar slechtst. Bovenaan staat "
                  "<strong>preventie: zorgen dat het afval niet ontstaat</strong>, daaronder "
                  "<strong>hergebruik</strong>, dan <strong>recyclage</strong>, dan "
                  "<strong>verbranden</strong> met energierecuperatie, en onderaan "
                  "<strong>storten</strong>. <strong>Storten staat dus niet boven "
                  "verbranden</strong> maar eronder; lozen in de rivier staat er zelfs niet op."),
            ("p", "Hoger dan verbranden staan onder meer "
                  "<strong>preventie</strong> en <strong>hergebruik</strong>. "
                  "<strong>Hergebruik staat hoger dan recyclage</strong>, want bij hergebruik "
                  "blijft het voorwerp zelf heel, terwijl recyclage het eerst afbreekt tot "
                  "grondstof, en dat kost meer energie. <strong>Preventie is de beste trede</strong> "
                  "omdat <strong>afval dat nooit ontstaat, ook nooit verwerkt moet worden</strong>: "
                  "elke andere trede kost nog energie, transport en materiaal."),
        ]),
        dict(kop="Doelen, de vijf P's en greenwashing", blokken=[
            ("p", "De <strong>duurzame ontwikkelingsdoelen</strong>: "
                  "<strong>er zijn er zeventien</strong> en "
                  "<strong>ze zijn afgesproken binnen de Verenigde Naties</strong>, in 2015 en met "
                  "2030 als streefjaar. <strong>Ze gelden voor alle landen</strong>, niet enkel de "
                  "rijkste, en <strong>ze gaan over meer dan het klimaat</strong>: ook over "
                  "armoede, gezondheid, onderwijs en gelijkheid."),
            ("p", "De <strong>vijf P's</strong> van duurzame ontwikkeling zijn "
                  "<strong>people, planet, prosperity, peace en partnership</strong>. Het oudere "
                  "model sprak van people, planet en profit; de vijf P's voegen vrede en "
                  "samenwerking toe en spreken van welvaart."),
            ("p", "<strong>Greenwashing</strong> is "
                  "<strong>een product groener voorstellen dan het in werkelijkheid is</strong>. "
                  "<strong>Een vaag woord als natuurlijk is nog geen bewijs</strong> en "
                  "<strong>een groene verpakking zegt niets over de inhoud</strong>. Een "
                  "onafhankelijk gecontroleerd keurmerk en openbare cijfers zijn juist wat je nodig "
                  "hebt om een bewering na te gaan; <strong>een keurmerk met controle is dus geen "
                  "greenwashing</strong>, en een bedrijf dat cijfers publiceert evenmin."),
        ]),
        dict(kop="Biogebaseerd, afbreekbaar en composteerbaar", blokken=[
            ("p", "<strong>Biogebaseerd</strong> betekent dat "
                  "<strong>de grondstof uit biomassa komt in plaats van uit aardolie</strong>. Het "
                  "zegt dus enkel waar de grondstof van komt: biogebaseerd plastic kan even goed "
                  "honderden jaren blijven liggen."),
            ("p", "<strong>Biodegradeerbaar</strong> betekent dat "
                  "<strong>micro-organismen de stof kunnen afbreken tot kleine moleculen</strong>. "
                  "Hoe snel en onder welke omstandigheden staat er niet bij: in koud zeewater kan "
                  "hetzelfde materiaal jaren blijven liggen. "
                  "<strong>Een biogebaseerde kunststof is daarom niet automatisch "
                  "biodegradeerbaar</strong>: bio-pet uit plantaardige grondstof breekt niet af."),
            ("p", "<strong>Composteerbaar</strong> "
                  "<strong>is strenger dan biodegradeerbaar</strong> en "
                  "<strong>er hoort een tijd en een temperatuur bij</strong>. Industrieel "
                  "composteerbaar vraagt een installatie op een hoge temperatuur, dus gebeurt het "
                  "niet in je eigen compostbak."),
            ("p", "<strong>Microplastics</strong> zijn "
                  "<strong>kleiner dan vijf millimeter</strong>, dus met het oog nog zichtbaar; "
                  "nanoplastics zijn nog duizend keer kleiner. "
                  "<strong>Primaire microplastics zijn al klein gemaakt</strong>, zoals korrels in "
                  "scrubs of grondstofpellets, en "
                  "<strong>secundaire ontstaan door afbraak van groter plastic</strong>, zoals een "
                  "fles die in de zon en de golven uiteenvalt."),
        ]),
        dict(kop="Waterstof, water en de cijfers van een reactie", blokken=[
            ("p", "De kleuren van <strong>waterstof</strong> zeggen hoe het gemaakt is; "
                  "<strong>waterstof zelf is bij elke kleur precies dezelfde stof</strong>, want H₂ "
                  "is H₂. <strong>Groene waterstof</strong> komt van "
                  "<strong>elektrolyse van water met stroom uit wind of zon</strong>; "
                  "<strong>grijze</strong> van stoomreforming van aardgas waarbij de CO₂ de lucht in "
                  "gaat; <strong>blauwe</strong> ook van aardgas, maar daar "
                  "<strong>wordt de CO₂ afgevangen en opgeslagen</strong>."),
            ("p", "De kleuren van water gaan over de vervuiling. "
                  "<strong>Wit water is drinkbaar</strong>, zoals het uit de kraan komt. "
                  "<strong>Grijs water</strong> is "
                  "<strong>licht vervuild water van bad, wastafel en wasmachine</strong>, "
                  "<strong>niet drinkbaar</strong> maar vaak nog goed om door te spoelen. "
                  "<strong>Zwart water komt uit het toilet</strong>, met fecaliën en urine, en moet "
                  "altijd eerst naar de waterzuivering."),
            ("p", "De <strong>atoomeconomie</strong> van een reactie meet "
                  "<strong>welk deel van de massa van de reagentia in het product zit</strong>. Ze "
                  "kijkt naar de reactievergelijking zelf, dus naar hoeveel massa noodgedwongen in "
                  "bijproducten belandt. Een <strong>additiereactie waarbij alles in het product "
                  "belandt</strong> heeft in principe de hoogste atoomeconomie, "
                  "<strong>100 %</strong>, want bij een eliminatie, een substitutie of een "
                  "condensatie gaat er altijd massa naar een bijproduct. "
                  "<strong>Een hoog rendement en een hoge atoomeconomie betekenen niet "
                  "hetzelfde</strong>: het rendement meet hoeveel je er echt uithaalt, de "
                  "atoomeconomie wat de vergelijking in het beste geval toelaat."),
            ("p", "In de <strong>groene chemie</strong> staat het hoogst: "
                  "<strong>afval voorkomen in plaats van het achteraf opruimen</strong>, dezelfde "
                  "gedachte als de bovenste trede van de ladder van Lansink; verdunnen lost niets "
                  "op, want de stof blijft in het milieu. "
                  "<strong>Katalyse helpt de groene chemie omdat de katalysator niet opgebruikt "
                  "raakt</strong> en dus niet als afval eindigt. En "
                  "<strong>een solvent is dikwijls het grootste milieuprobleem van een "
                  "synthese</strong> omdat <strong>er meestal veel meer solvent in gaat dan "
                  "reagens</strong>; daarom zoekt men naar reacties in water of zonder solvent."),
        ]),
    ],
    onthoud=[
        "Lineair is van wieg tot graf, circulair van wieg tot wieg.",
        "Ladder van Lansink: preventie, hergebruik, recyclage, verbranden, storten.",
        "Downcycling is recyclage waarbij de kwaliteit zakt.",
        "Zeventien duurzame ontwikkelingsdoelen; vijf P's met peace en partnership.",
        "Biogebaseerd gaat over de grondstof, biodegradeerbaar over de afbraak.",
        "Groene waterstof uit elektrolyse, grijze uit aardgas, blauwe met CO₂-afvang.",
        "Atoomeconomie is wat de vergelijking toelaat, rendement wat je echt haalt.",
    ],
)

# ───────────────────── 22. Veilig werken, meetinstrumenten en beduidende cijfers
BUNDELS["veilig-werken-meetinstrumenten-en-beduidende-cijfers-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Veilig werken, meetinstrumenten en beduidende cijfers",
    onder="Wat je leest voor je begint, waarmee je meet, en hoeveel cijfers je mag opschrijven.",
    secties=[
        dict(kop="Het etiket lezen", blokken=[
            ("p", "Op een etiket staan twee soorten zinnen. Een "
                  "<strong>H-zin</strong> gaat "
                  "<strong>over het gevaar dat de stof zelf oplevert</strong>; de "
                  "<strong>H</strong> komt van <strong>hazard</strong>, dus "
                  "<strong>gevaar</strong>. Een <strong>P-zin</strong> gaat "
                  "<strong>over de voorzorg en wat je bij een ongeval doet</strong>; de P komt van "
                  "precaution, en zo'n zin zegt bijvoorbeeld dat je een veiligheidsbril draagt of de "
                  "huid grondig spoelt."),
            ("p", "De <strong>gevarenpictogrammen zijn ruitvormig</strong>, met een rode rand en "
                  "een wit vlak; <strong>ronde groene tekens</strong> zijn gebodstekens. Vier om te "
                  "kennen. <strong>Een hand en een oppervlak waar een druppel een gat in bijt</strong> "
                  "betekent dat <strong>de stof bijtend is voor huid en materiaal</strong>, dus "
                  "corrosief: bril en handschoenen. Een "
                  "<strong>doodshoofd met twee gekruiste beenderen</strong> betekent dat "
                  "<strong>de stof giftig is, ook in een kleine hoeveelheid</strong>. Het "
                  "<strong>uitroepteken</strong> staat voor schadelijk of irriterend, dus "
                  "<strong>niet altijd dodelijk giftig</strong>. En een "
                  "<strong>boom met een dode vis</strong> betekent dat "
                  "<strong>de stof schadelijk is voor het leven in het water</strong>, dus nooit in "
                  "de gootsteen maar in een aparte afvalfles."),
            ("p", "Een <strong>veiligheidsfiche</strong> "
                  "<strong>vermeldt de H- en P-zinnen van de stof</strong> en "
                  "<strong>zegt wat je bij een ongeval moet doen</strong>. Ze "
                  "<strong>vervangt het etiket op de fles niet</strong>: dat blijft nodig, en de "
                  "fiche staat erbij voor wie meer wil weten over opslag, blussen en eerste hulp."),
        ]),
        dict(kop="Glaswerk en meten", blokken=[
            ("p", "Om precies <strong>250,0 mL oplossing</strong> te maken gebruik je "
                  "<strong>een maatkolf van 250 mL</strong>: die heeft één streepje en is daarvoor "
                  "gekalibreerd. Nauwkeurig genoeg voor een volume dat in een berekening komt, zijn "
                  "<strong>de maatkolf</strong> en <strong>de volumetrische pipet</strong>; een "
                  "bekerglas en een erlenmeyer dienen om in te werken, niet om in te meten, en een "
                  "maatcilinder zit ertussen. Voor een volume tot op honderdsten bij een titratie "
                  "gebruik je <strong>een buret</strong>: daar "
                  "<strong>lees je het volume af dat eruit gelopen is</strong>, en daarom loopt de "
                  "schaal van boven naar onder."),
            ("p", "Je leest een volume af bij <strong>de meniscus</strong>, en wel bij de onderkant "
                  "van die holle kromming, op ooghoogte; van boven of onder kijken geeft een "
                  "afleesfout. Je <strong>spoelt een pipet eerst met de oplossing die je gaat "
                  "pipetteren</strong>, want achtergebleven water zou verdunnen; bij een maatkolf "
                  "is het net omgekeerd, die mag wel nat zijn van water."),
            ("p", "Het <strong>meetbereik</strong> van een instrument is "
                  "<strong>de kleinste en de grootste waarde die het kan meten</strong>; buiten dat "
                  "bereik is de waarde onbetrouwbaar. De "
                  "<strong>resolutie</strong> of <strong>schaalverdeling</strong> is "
                  "<strong>de kleinste stap die het nog kan onderscheiden</strong>. Daarom "
                  "<strong>meet je 5 mL niet af in een maatcilinder van 500 mL</strong>: "
                  "<strong>de streepjes staan daar veel te ver van elkaar</strong>, en één streepje "
                  "ernaast is al 5 mL."),
            ("p", "Nog twee veiligheidsregels. "
                  "<strong>Een zuur verdun je door het zuur bij het water te gieten, niet "
                  "omgekeerd</strong>, want het verdunnen geeft veel warmte en water bij "
                  "geconcentreerd zuur kan spatten of koken. En gemorst zuur ruim je op door het "
                  "<strong>eerst te neutraliseren met een zwakke base</strong> en het "
                  "<strong>daarna op te nemen en af te voeren bij het juiste afval</strong>; een "
                  "sterke base maakt er een tweede probleem van, terwijl "
                  "natriumwaterstofcarbonaat zwak genoeg is."),
        ]),
        dict(kop="Eenheden en voorvoegsels", blokken=[
            ("p", "De SI-eenheid van massa is de <strong>kilogram</strong>, de enige basiseenheid "
                  "met een voorvoegsel erin. Basiseenheden zijn onder meer de "
                  "<strong>seconde</strong> en de <strong>kelvin</strong>; de "
                  "<strong>liter is een afgeleide eenheid</strong> en de "
                  "<strong>celsiusgraad is geen basiseenheid</strong>. De zeven zijn meter, "
                  "kilogram, seconde, ampère, kelvin, mol en candela."),
            ("p", "De voorvoegsels gaan telkens drie machten van tien verder. "
                  "<strong>Mega</strong> is <strong>een miljoen</strong> (10⁶), kilo is 10³ en giga "
                  "10⁹; <strong>milli</strong> is 10⁻³, <strong>micro</strong> is "
                  "<strong>10⁻⁶</strong> en nano 10⁻⁹. Daarom gaan er "
                  "<strong>1000</strong> micrometer in één millimeter."),
            ("p", "Deel je <strong>massa in gram door volume in milliliter</strong>, dan krijg je "
                  "<strong>g/mL</strong>, de massadichtheid; in SI-eenheden zou dat kg/m³ zijn."),
        ]),
        dict(kop="Beduidende cijfers en wetenschappelijke notatie", blokken=[
            ("p", "<strong>0,00450</strong> heeft <strong>drie</strong> beduidende cijfers: de "
                  "nullen vooraan dienen enkel om de komma te plaatsen, en "
                  "<strong>nullen vooraan tellen dus niet mee</strong>, terwijl de nul achteraan wel "
                  "meetelt omdat ze zegt dat er echt tot daar gemeten is. Ook "
                  "<strong>2,40</strong> en <strong>0,00106</strong> hebben er drie; 0,0012 heeft "
                  "er twee, en bij 12 000 weet je het niet — schrijf het als 1,20·10⁴ als je er "
                  "drie bedoelt."),
            ("p", "Bij <strong>vermenigvuldigen en delen</strong> volg je de factor met het minste "
                  "aantal beduidende cijfers: <strong>2,5 maal 3,142</strong> geeft dus "
                  "<strong>twee</strong> beduidende cijfers, 7,9 en niet 7,855. Bij "
                  "<strong>optellen en aftrekken</strong> kijk je naar "
                  "<strong>het aantal decimalen</strong>: "
                  "<strong>12,11 g plus 0,2 g is 12,3 g</strong>. "
                  "<strong>Bij optellen volg je dus niet het aantal beduidende cijfers.</strong> En "
                  "<strong>een rekenmachine geeft vaak meer cijfers dan je mag opschrijven</strong>, "
                  "want het toestel weet niet hoe nauwkeurig je gemeten hebt."),
            ("p", "In de <strong>wetenschappelijke notatie</strong> "
                  "<strong>staat er precies één cijfer voor de komma</strong>, van 1 tot 9, en "
                  "<strong>ze maakt het aantal beduidende cijfers duidelijk</strong>: "
                  "<strong>1,0·10³</strong> heeft er <strong>2</strong>. "
                  "<strong>De exponent is niet altijd positief</strong> en de notatie is juist bij "
                  "kleine getallen het handigst: <strong>0,000 072</strong> schrijf je als "
                  "<strong>7,2·10⁻⁵</strong>, want de komma schuift vijf plaatsen."),
            ("p", "Twee grootheden zijn <strong>recht evenredig</strong> als "
                  "<strong>de andere ook verdubbelt wanneer de ene verdubbelt</strong>: hun "
                  "quotiënt blijft constant, en in een grafiek geeft dat "
                  "<strong>een rechte door de oorsprong</strong> — door de oorsprong is de "
                  "voorwaarde, want een rechte die hoger begint is wel lineair maar niet evenredig. "
                  "Ze zijn <strong>omgekeerd evenredig</strong> als "
                  "<strong>de andere halveert wanneer de ene verdubbelt</strong>: dan blijft "
                  "<strong>het product constant</strong>, zoals bij druk en volume van een gas, en "
                  "geeft de grafiek een hyperbool."),
        ]),
    ],
    onthoud=[
        "H-zin is het gevaar (hazard), P-zin de voorzorg (precaution).",
        "Pictogrammen zijn ruitvormig met een rode rand.",
        "Maatkolf en volumetrische pipet zijn nauwkeurig, bekerglas niet.",
        "Meetbereik is van klein tot groot, resolutie is de kleinste stap.",
        "Zuur bij water, nooit water bij zuur.",
        "Vermenigvuldigen volgt beduidende cijfers, optellen volgt decimalen.",
        "Recht evenredig: quotiënt constant. Omgekeerd: product constant.",
    ],
)

# ───────────────────── 23. Wetenschappelijk onderzoek, ontwerpen en STEM
BUNDELS["wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="De stappen van een onderzoek, de stappen van een ontwerp, en het verschil ertussen.",
    secties=[
        dict(kop="Van vraag naar hypothese", blokken=[
            ("p", "Een goede <strong>onderzoeksvraag</strong> is "
                  "<strong>een vraag die je met een meting kan beantwoorden</strong>: nauwkeurig "
                  "afgebakend en meetbaar. Hoe los het zout op is geen onderzoeksvraag, hoeveel "
                  "gram per 100 mL water wel."),
            ("p", "Een <strong>hypothese</strong> is "
                  "<strong>een onderbouwd vermoeden dat je kan testen</strong>: ze zegt wat je "
                  "verwacht en waarom. <strong>Een hypothese die verworpen wordt, maakt het "
                  "onderzoek niet waardeloos</strong>: ook dat is een antwoord op de vraag."),
            ("p", "De <strong>stappen van een onderzoek</strong> zijn onder meer "
                  "<strong>een onderzoeksvraag opstellen</strong> en "
                  "<strong>de resultaten rapporteren</strong>. Wat er niet bij hoort, is het besluit "
                  "vooraf vastleggen of de metingen aanpassen aan de hypothese: "
                  "<strong>het besluit volgt uit de metingen, niet omgekeerd</strong>."),
        ]),
        dict(kop="De proefopzet", blokken=[
            ("p", "Wat je zelf instelt, is de "
                  "<strong>onafhankelijke</strong> variabele; wat je meet, is de "
                  "<strong>afhankelijke</strong> variabele; al de rest houd je "
                  "<strong>constant</strong>. Onderzoek je hoe de temperatuur de reactiesnelheid "
                  "beïnvloedt, dan is <strong>de temperatuur de onafhankelijke variabele, want die "
                  "stel jij zelf in</strong>, en houd je bijvoorbeeld "
                  "<strong>de concentratie van de oplossing</strong> en "
                  "<strong>de hoeveelheid vaste stof per proef</strong> gelijk."),
            ("p", "Een <strong>controleproef</strong> of <strong>blanco</strong> dient "
                  "<strong>om te zien wat er zonder de behandeling gebeurt</strong>. Zonder dat "
                  "vergelijkingspunt weet je niet of het verschil van jouw ingreep komt; daarom "
                  "hoort er bij een katalysatorproef een buis zonder katalysator."),
            ("p", "Je <strong>herhaalt een meting meerdere keren</strong> "
                  "<strong>om toevallige afwijkingen te kunnen uitvlakken</strong>. Een "
                  "<strong>systematische fout wijkt altijd naar dezelfde kant af</strong> en "
                  "verdwijnt niet met een gemiddelde: een balans die 0,2 g te veel aangeeft, doet "
                  "dat elke keer, en dan helpt kalibreren. Dat is ook het verschil tussen "
                  "<strong>nauwkeurig en precies</strong>: "
                  "<strong>nauwkeurig ligt dicht bij de echte waarde, precies dicht bij "
                  "elkaar</strong>. Vijf metingen die mooi samen liggen maar alle vijf te hoog, zijn "
                  "precies maar niet nauwkeurig."),
            ("p", "Je <strong>noteert ook wat er misliep</strong>, "
                  "<strong>omdat dat de afwijking in je resultaat kan verklaren</strong>. Een "
                  "<strong>uitschieter</strong> of outlier is "
                  "<strong>een meting die sterk afwijkt van de andere</strong>: "
                  "<strong>je mag een meting die niet in je verwachting past niet gewoon "
                  "weglaten</strong>, je noteert ze en zoekt uit waar ze van komt."),
        ]),
        dict(kop="Rapporteren", blokken=[
            ("p", "In een <strong>besluit</strong> hoort "
                  "<strong>een antwoord op de onderzoeksvraag, met de meting erbij</strong>: het "
                  "zegt of de hypothese klopt en waaruit je dat besluit. De werkwijze hoort in het "
                  "verslag."),
            ("p", "<strong>Een grafiek hoort een titel en op beide assen een eenheid te "
                  "krijgen</strong>, want zonder eenheid betekent een getal niets; de as met wat je "
                  "instelde komt liggend, de as met wat je meette staand."),
            ("p", "<strong>Reproduceerbaarheid</strong> betekent dat "
                  "<strong>iemand anders hetzelfde resultaat moet kunnen krijgen</strong> en dat "
                  "<strong>daarvoor je werkwijze nauwkeurig beschreven moet zijn</strong>. Eén keer "
                  "lukken bij jou is niet genoeg, en geheimhouden kan niet. "
                  "<strong>Peer review betekent dat vakgenoten het werk nakijken voor het "
                  "verschijnt</strong>; dat maakt een artikel niet onfeilbaar, maar wel "
                  "betrouwbaarder."),
        ]),
        dict(kop="Ontwerpen", blokken=[
            ("p", "Een <strong>ontwerpvraag</strong> is "
                  "<strong>een vraag naar iets wat je moet maken of oplossen</strong>. Daarin zit "
                  "het hele <strong>verschil tussen onderzoeken en ontwerpen</strong>: "
                  "<strong>onderzoeken zoekt kennis, ontwerpen zoekt een oplossing</strong>. Ook een "
                  "ontwerper meet, maar hij meet om na te gaan of zijn oplossing de criteria haalt."),
            ("p", "Een <strong>criterium</strong> is "
                  "<strong>een eis waaraan de oplossing moet voldoen</strong>; een "
                  "<strong>randvoorwaarde</strong> is "
                  "<strong>een beperking waarbinnen je moet blijven werken</strong>, zoals het "
                  "budget, de tijd en de beschikbare materialen. Het filter moet minstens 90 % van "
                  "het zand tegenhouden: dat is een criterium. Je hebt maar één lesuur: dat is een "
                  "randvoorwaarde. Criteria zijn "
                  "<strong>best meetbaar opgeschreven</strong> en je "
                  "<strong>legt ze vast voor je begint te bouwen</strong>; "
                  "<strong>ze achteraf versoepelen zodat je ontwerp wel slaagt, is geen "
                  "ontwerpen</strong>."),
            ("p", "Je <strong>splitst een ontwerpopdracht in deelproblemen</strong> "
                  "<strong>omdat je elk stuk apart kan oplossen en testen</strong>: bij een "
                  "waterzuivering zijn het bezinken, het filtreren en het ontsmetten elk een eigen "
                  "probleem."),
            ("p", "Een <strong>prototype</strong> is "
                  "<strong>een eerste bouwsel waarmee je het idee uittest</strong>; het mag ruw "
                  "zijn en van karton en tape, want de bedoeling is leren wat werkt. Voldoet het "
                  "niet aan de criteria, dan ga je <strong>nagaan waar het faalt en het "
                  "bijsturen</strong>: ontwerpen gaat in rondes van bouwen, testen, bijsturen en "
                  "opnieuw testen, dus <strong>hoort er niet één poging bij</strong>. "
                  "<strong>Een ontwerp is pas af als het aan elk opgeschreven criterium "
                  "voldoet.</strong> Bij een ontwerpproces horen dus "
                  "<strong>de criteria en randvoorwaarden vastleggen</strong> en "
                  "<strong>het prototype testen en bijsturen</strong>; een hypothese en variabelen "
                  "horen bij onderzoek."),
        ]),
        dict(kop="STEM en de samenleving", blokken=[
            ("p", "<strong>STEM</strong> staat voor "
                  "<strong>science, technology, engineering en mathematics</strong>. Die vier horen "
                  "samen: een technisch probleem vraagt wetenschap, techniek, ontwerp en rekenwerk "
                  "tegelijk."),
            ("p", "<strong>Een wetenschappelijke vondst is niet meteen klaar voor gebruik</strong>: "
                  "tussen het labo en een product zitten jaren van opschalen, testen en goedkeuren, "
                  "en veel vondsten halen die weg nooit. "
                  "<strong>Opschalen van labo naar fabriek is niet vanzelfsprekend</strong> omdat "
                  "<strong>warmte en menging zich anders gedragen in het groot</strong>: in een "
                  "reactor van duizend liter raak je de warmte veel moeilijker kwijt, al blijft de "
                  "reactievergelijking natuurlijk dezelfde. En "
                  "<strong>de kostprijs van een proces kan bepalen of een reactie in de industrie "
                  "gebruikt wordt</strong>: een reactie die chemisch mooi werkt maar te duur is, "
                  "haalt de fabriek niet."),
            ("p", "Bij het beoordelen van een nieuwe chemische toepassing horen vragen als "
                  "<strong>wat gebeurt er met de stof na gebruik</strong> en "
                  "<strong>wie draagt het risico en wie het voordeel</strong>. Die vragen lossen de "
                  "cijfers alleen niet op. Een <strong>risicoafweging</strong> hoort erbij "
                  "<strong>omdat het voordeel moet opwegen tegen wat het kan kosten</strong>: geen "
                  "enkele toepassing is volledig zonder risico, en de vraag is of het voordeel groot "
                  "genoeg is en wie het risico draagt."),
        ]),
    ],
    onthoud=[
        "Een onderzoeksvraag is meetbaar, een hypothese is een onderbouwd vermoeden.",
        "Onafhankelijk stel je in, afhankelijk meet je, de rest houd je constant.",
        "Een controleproef laat zien wat er zonder de ingreep gebeurt.",
        "Herhalen vlakt toevallige fouten uit; een systematische fout niet.",
        "Nauwkeurig is dicht bij de echte waarde, precies is dicht bij elkaar.",
        "Criteria zijn eisen, randvoorwaarden zijn beperkingen.",
        "Onderzoeken wil weten, ontwerpen wil oplossen; een prototype mag mislukken.",
    ],
)

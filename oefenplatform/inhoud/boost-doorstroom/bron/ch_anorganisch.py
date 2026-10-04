# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Anorganische stofklassen en naamgeving.

Hoort bij "organische en anorganische stoffen" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_organisch], [ch_water] en
[ch_reactietypes]. Samen 40 % van het examen, het zwaarste onderdeel.

Deel 1 gaat over de vier anorganische stofklassen die de fiche opsomt, over het
onderscheid tussen binair en ternair, en over de namen van de zuurresten.
Deel 2 gaat over de IUPAC-naamgeving en de triviale namen, over het verschil
tussen een zuurvormend en een basevormend oxide, en over de reactiepatronen van
de fiche.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn oxiden? Kruis alles aan wat juist is.",
        opties=[
            "CaO",
            "CO₂",
            "NaOH",
            "HCl",
        ],
        antwoord=[0, 1],
        uitleg="Een oxide is een verbinding van een element met zuurstof alleen. NaOH is een hydroxide en HCl een zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke stofklasse hoort NaOH?",
        opties=[
            "een hydroxide",
            "een oxide",
            "een zuur",
            "een zout",
        ],
        antwoord=0,
        uitleg="De groep OH is de functionele groep van de hydroxiden. In water geeft die groep een basische oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een anorganisch zuur in zijn formule?",
        opties=[
            "de formule begint met waterstof",
            "de formule eindigt op OH",
            "de formule bevat geen zuurstof",
            "de formule begint met een metaal",
        ],
        antwoord=0,
        uitleg="Bij een zuur staan de waterstofatomen vooraan, zoals in HCl of H₂SO₄. Die waterstof komt in water als H⁺ vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn zuren? Kruis alles aan wat juist is.",
        opties=[
            "HCl",
            "H₂SO₄",
            "NaOH",
            "NaCl",
        ],
        antwoord=[0, 1],
        uitleg="Bij een zuur staat de waterstof vooraan. NaOH is een hydroxide en NaCl is een zout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat HCl een binair zuur is?",
        opties=[
            "het bevat twee verschillende elementen",
            "het bevat twee waterstofatomen",
            "het kan twee reacties aangaan",
            "het lost op in twee stappen",
        ],
        antwoord=0,
        uitleg="Binair betekent dat er twee elementen in zitten, hier waterstof en chloor. Een ternair zuur bevat er drie, met zuurstof erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zuren is ternair?",
        opties=[
            "H₂SO₄",
            "HCl",
            "HBr",
            "H₂S",
        ],
        antwoord=0,
        uitleg="H₂SO₄ bevat waterstof, zwavel en zuurstof, dus drie elementen. De andere drie bevatten er twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke stofklasse hoort CaCO₃?",
        opties=[
            "een ternair zout",
            "een binair zout",
            "een hydroxide",
            "een oxide",
        ],
        antwoord=0,
        uitleg="Een zout bestaat uit een metaalion en een zuurrest. Hier zitten calcium, koolstof en zuurstof in, dus is het ternair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het ion SO₄²⁻?",
        opties=[
            "het sulfaation",
            "het sulfide-ion",
            "het sulfietion",
            "het zwavelion",
        ],
        antwoord=0,
        uitleg="Het sulfaation is de zuurrest van zwavelzuur. Het sulfide-ion is S²⁻, dus zonder zuurstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het ion NO₃¹⁻?",
        opties=[
            "het nitraation",
            "het nitride-ion",
            "het stikstofion",
            "het nitrietion",
        ],
        antwoord=0,
        uitleg="Het nitraation is de zuurrest van salpeterzuur. Nitraten zijn allemaal goed oplosbaar in water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ionen zijn zuurresten zonder zuurstof? Kruis alles aan wat juist is.",
        opties=[
            "Cl¹⁻",
            "S²⁻",
            "CO₃²⁻",
            "PO₄³⁻",
        ],
        antwoord=[0, 1],
        uitleg="Het chloride-ion en het sulfide-ion horen bij een binair zuur en bevatten geen zuurstof. Carbonaat en fosfaat wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk ion zit in een ammoniumzout?",
        opties=[
            "NH₄¹⁺",
            "NH₃",
            "NO₃¹⁻",
            "N³⁻",
        ],
        antwoord=0,
        uitleg="Het ammoniumion is een positief geladen groepje dat de plaats van een metaalion inneemt. Ammoniumsulfaat wordt veel gebruikt als meststof.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oxide is een verbinding van een element met zuurstof.",
        antwoord=True,
        uitleg="Dat is net de omschrijving van de stofklasse, zoals bij CO₂ of Fe₂O₃.",
    ),
    dict(
        type="waarofniet",
        vraag="De functionele groep van een hydroxide is OH.",
        antwoord=True,
        uitleg="Die groep geeft in water het hydroxide-ion OH⁻ en maakt de oplossing basisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk zout bevat zuurstof.",
        antwoord=False,
        uitleg="Een binair zout zoals NaCl bevat geen zuurstof. Alleen ternaire zouten hebben zuurstof in de zuurrest.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zout bestaat uit een positief en een negatief ion.",
        antwoord=True,
        uitleg="Meestal is het positieve ion een metaalion of het ammoniumion, en het negatieve ion een zuurrest.",
    ),
    dict(
        type="waarofniet",
        vraag="H₂O hoort bij de stofklasse van de zuren, want de formule begint met waterstof.",
        antwoord=False,
        uitleg="Water is een oxide van waterstof. Het geeft in water geen overmaat aan H⁺ en is dus neutraal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het ion CO₃²⁻?",
        antwoord=["carbonaation", "het carbonaation", "carbonaat"],
        uitleg="Het carbonaation is de zuurrest van koolzuur. Kalksteen is calciumcarbonaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het ion PO₄³⁻?",
        antwoord=["fosfaation", "het fosfaation", "fosfaat"],
        uitleg="Het fosfaation is de zuurrest van fosforzuur. Op natrium, kalium en ammonium na zijn fosfaten slecht oplosbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Tot welke stofklasse hoort Al(OH)₃?",
        antwoord=["hydroxide", "een hydroxide", "hydroxiden"],
        uitleg="De groep OH staat er drie keer in, want aluminium vormt een ion met lading 3+.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het ion I¹⁻?",
        antwoord=["jodide-ion", "jodide", "het jodide-ion"],
        uitleg="Een zuurrest zonder zuurstof krijgt de uitgang -ide. Jodide is dus de rest van waterstofjodide.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam zoutzuur?",
        opties=[
            "HCl",
            "H₂SO₄",
            "HNO₃",
            "NaCl",
        ],
        antwoord=0,
        uitleg="Zoutzuur is een oplossing van waterstofchloride in water. Het zit in ontkalkers en in je maag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam ammoniak?",
        opties=[
            "NH₃",
            "NH₄Cl",
            "HNO₃",
            "N₂",
        ],
        antwoord=0,
        uitleg="Ammoniak is een gas met een scherpe geur. Opgelost in water geeft het een basische oplossing en het zit in kuisproducten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen hebben een triviale naam die naar kalk verwijst? Kruis alles aan wat juist is.",
        opties=[
            "CaO, ongebluste kalk",
            "Ca(OH)₂, gebluste kalk",
            "NaOH, bijtende soda",
            "NaHCO₃, bakpoeder",
        ],
        antwoord=[0, 1],
        uitleg="Ongebluste kalk is het oxide, gebluste kalk het hydroxide. Je maakt gebluste kalk door water bij ongebluste kalk te doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam keukenzout?",
        opties=[
            "NaCl",
            "NaOH",
            "Na₂CO₃",
            "NaHCO₃",
        ],
        antwoord=0,
        uitleg="Natriumchloride is het zout op tafel. Na₂CO₃ is soda en NaHCO₃ is bakpoeder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam soda?",
        opties=[
            "Na₂CO₃",
            "NaOH",
            "NaCl",
            "NaNO₃",
        ],
        antwoord=0,
        uitleg="Natriumcarbonaat heet soda en wordt gebruikt om te kuisen en om glas te maken. Bijtende soda is NaOH.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men CO₂ volgens de IUPAC-regels, met Griekse telwoorden?",
        opties=[
            "koolstofdioxide",
            "koolstofoxide",
            "dikoolstofoxide",
            "carbonaat",
        ],
        antwoord=0,
        uitleg="Bij een atoomverbinding zeggen de Griekse telwoorden hoeveel atomen er van elk element zijn. Twee zuurstof wordt dus dioxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men N₂O volgens de IUPAC-regels?",
        opties=[
            "distikstofoxide",
            "stikstofdioxide",
            "stikstofoxide",
            "dioxidestikstof",
        ],
        antwoord=0,
        uitleg="Twee stikstofatomen en één zuurstofatoom: distikstofoxide. De triviale naam is lachgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de stocknotatie in een naam zoals ijzer(III)chloride?",
        opties=[
            "ze geeft het oxidatiegetal van het metaal",
            "ze geeft het aantal chlooratomen",
            "ze geeft de plaats in het periodiek systeem",
            "ze geeft de massa van één formule-eenheid",
        ],
        antwoord=0,
        uitleg="Ijzer kan +II of +III zijn. Het Romeinse cijfer tussen haakjes zegt welk van de twee, dus weet je hoeveel chloride-ionen erbij horen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er als een metaaloxide met water reageert?",
        opties=[
            "een hydroxide",
            "een zuur",
            "een zout",
            "een oxide",
        ],
        antwoord=0,
        uitleg="Een metaaloxide is basevormend. Met water geeft het een hydroxide, zoals CaO dat Ca(OH)₂ wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er als een niet-metaaloxide met water reageert?",
        opties=[
            "een zuur",
            "een hydroxide",
            "een zout",
            "een metaal",
        ],
        antwoord=0,
        uitleg="Een niet-metaaloxide is zuurvormend. CO₂ met water geeft koolzuur, en SO₂ in de lucht draagt zo bij aan zure regen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen ontstaan als een zuur met een hydroxide reageert? Kruis alles aan wat juist is.",
        opties=[
            "een zout",
            "water",
            "een oxide",
            "een metaal",
        ],
        antwoord=[0, 1],
        uitleg="Dat is het patroon van de neutralisatie: het metaalion en de zuurrest vormen het zout, en de H⁺ en de OH⁻ vormen water.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaaloxide is basevormend.",
        antwoord=True,
        uitleg="Met water geeft het een hydroxide, en een hydroxide maakt de oplossing basisch.",
    ),
    dict(
        type="waarofniet",
        vraag="De triviale naam van NaHCO₃ is bijtende soda.",
        antwoord=False,
        uitleg="NaHCO₃ is bakpoeder, natriumwaterstofcarbonaat. Bijtende soda is NaOH.",
    ),
    dict(
        type="waarofniet",
        vraag="Zwavelzuur heeft de formule H₂SO₄.",
        antwoord=True,
        uitleg="Het zit onder andere in een autobatterij. Het is een sterk zuur en bijtend.",
    ),
    dict(
        type="waarofniet",
        vraag="Methaan is een anorganische stof.",
        antwoord=False,
        uitleg="Methaan is een alkaan en dus organisch. Het is het hoofdbestanddeel van aardgas.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een ionverbinding gebruikt men in de IUPAC-naam geen Griekse telwoorden.",
        antwoord=True,
        uitleg="Daar gebruikt men de stocknotatie met een Romeins cijfer, of men laat het weg als het metaal maar één mogelijkheid heeft.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof heeft de triviale naam gebluste kalk?",
        antwoord=["Ca(OH)2", "calciumhydroxide", "Ca(OH)₂"],
        uitleg="Je maakt het door water bij ongebluste kalk te doen. Het zit in mortel en in kalkmelk voor de landbouw.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof heeft de triviale naam salpeterzuur?",
        antwoord=["HNO3", "HNO₃"],
        uitleg="Salpeterzuur is een ternair zuur. De zuurrest is het nitraation en het zuur wordt veel gebruikt voor meststoffen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk gas met de triviale naam koolzuurgas komt vrij als je bakpoeder met azijn mengt?",
        antwoord=["CO2", "koolstofdioxide", "CO₂"],
        uitleg="Het zuur maakt uit het waterstofcarbonaat koolzuur, en dat valt meteen uiteen in water en koolstofdioxide.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men CaO volgens de IUPAC-regels?",
        antwoord=["calciumoxide", "calcium oxide"],
        uitleg="Calcium heeft maar één mogelijk oxidatiegetal, dus is een Romeins cijfer niet nodig. De triviale naam is ongebluste kalk.",
    ),
]

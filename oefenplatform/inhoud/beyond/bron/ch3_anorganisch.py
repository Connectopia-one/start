# -*- coding: utf-8 -*-
"""Anorganische stoffen: stofklassen en naamgeving — 🌍 Beyond, chemie.

Deel 1 gaat over de indeling: enkelvoudig of samengesteld, de vier stofklassen
oxide, hydroxide, zuur en zout, en de verdere indeling in binair, ternair,
hydraat, waterstofzout, ammoniumzout en peroxide. Deel 2 gaat over de namen:
de IUPAC-naam met stocknotatie of met Griekse telwoorden, de triviale namen die
in een keuken of een werkhuis gebruikt worden, en de symbolen van de elementen.

De namen van de zuren staan in de fiche als één lange lijst. Daarom vragen de
vragen niet de hele lijst op, maar het systeem erachter: -aat tegenover -iet,
per- tegenover hypo-, en het verband tussen de IUPAC-naam waterstofnitraat en
de gebruiksnaam salpeterzuur.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn enkelvoudige stoffen? Kruis alles aan wat juist is.",
        opties=[
            "ozon",
            "zuurstofgas",
            "water",
            "keukenzout",
        ],
        antwoord=[0, 1],
        uitleg="Ozon is O₃ en zuurstofgas is O₂: in beide zit maar één soort atoom, dus "
        "één element. Water en keukenzout zijn samengesteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze stoffen zijn oxiden? Kruis alles aan wat juist is.",
        opties=[
            "calciumoxide, met de formule CaO",
            "zwaveldioxide, met de formule SO₂",
            "natriumhydroxide, met de formule NaOH",
            "waterstofchloride, met de formule HCl",
        ],
        antwoord=[0, 1],
        uitleg="Een oxide is een verbinding van zuurstof met één ander element. In NaOH "
        "zit zuurstof wel, maar samen met waterstof als hydroxidegroep.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de stofklasse van een verbinding van een metaalion met een zuurrest?",
        antwoord=["zout", "een zout", "zouten"],
        uitleg="NaCl, CaCO₃ en KNO₃ zijn zouten. Het metaalion komt van een base, de "
        "zuurrest van een zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de waardigheid van fosforzuur, H₃PO₄?",
        opties=[
            "driewaardig",
            "eenwaardig",
            "tweewaardig",
            "vierwaardig",
        ],
        antwoord=0,
        uitleg="De waardigheid van een zuur is het aantal waterstofatomen dat het als "
        "ion kan afstaan. H₃PO₄ heeft er drie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een binaire verbinding bestaat uit precies twee atomen.",
        antwoord=False,
        uitleg="Ze bestaat uit twee elementen, niet uit twee atomen. Fe₂O₃ heeft vijf "
        "atomen en is toch binair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verbinding is ternair?",
        opties=[
            "calciumcarbonaat, CaCO₃",
            "natriumchloride, NaCl",
            "waterstofsulfide, H₂S",
            "aluminiumoxide, Al₂O₃",
        ],
        antwoord=0,
        uitleg="Ternair betekent drie verschillende elementen. In CaCO₃ zitten calcium, "
        "koolstof en zuurstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een hydraat?",
        opties=[
            "er zit kristalwater in het rooster",
            "er zit waterstofgas in opgelost",
            "het reageert heftig met water",
            "het lost niet op in water",
        ],
        antwoord=0,
        uitleg="CuSO₄·5H₂O is kopersulfaatpentahydraat: vijf moleculen water per "
        "formule-eenheid, vast ingebouwd in het kristal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof is een waterstofzout?",
        opties=[
            "natriumwaterstofcarbonaat, NaHCO₃",
            "natriumcarbonaat, Na₂CO₃",
            "waterstofcarbonaat, H₂CO₃",
            "calciumcarbonaat, CaCO₃",
        ],
        antwoord=0,
        uitleg="In een waterstofzout is maar een deel van de waterstofionen van het "
        "zuur vervangen; er blijft er dus één in de zuurrest zitten.",
    ),
    dict(
        type="invultekst",
        vraag="Welk ion neemt in een ammoniumzout de plaats van het metaalion in?",
        antwoord=["ammoniumion", "NH4+", "ammonium"],
        uitleg="Het ammoniumion NH₄⁺ gedraagt zich als een metaalion: NH₄Cl is een zout, "
        "ook al zit er geen metaal in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een peroxide?",
        opties=[
            "aan twee zuurstofatomen die aan elkaar gebonden zijn",
            "aan een zuurstofatoom met een negatieve lading",
            "aan een hydroxidegroep naast een metaalion",
            "aan een zuurrest met drie zuurstofatomen",
        ],
        antwoord=0,
        uitleg="In H₂O₂ en in Na₂O₂ zit een O–O-brug. Zuurstof heeft daar oxidatiegetal "
        "−I in plaats van −II.",
    ),
    dict(
        type="waarofniet",
        vraag="De formule-eenheid van een ionverbinding geeft de kleinste verhouding van de ionen, niet één molecule.",
        antwoord=True,
        uitleg="NaCl bestaat niet als losse molecule: in het rooster staan de ionen in "
        "verhouding 1 op 1. Daarom spreken we van een formule-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke groep is de functionele groep van de hydroxiden?",
        opties=[
            "de OH-groep",
            "de O-groep",
            "het H-ion vooraan",
            "de zuurrest achteraan",
        ],
        antwoord=0,
        uitleg="Een hydroxide heeft één of meer OH⁻-ionen: NaOH, Ca(OH)₂, Al(OH)₃.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel hydroxide-ionen staan er in de formule van calciumhydroxide?",
        opties=[
            "twee",
            "een",
            "drie",
            "vier",
        ],
        antwoord=0,
        uitleg="Ca²⁺ heeft twee OH⁻ nodig om neutraal uit te komen: Ca(OH)₂, dus "
        "tweewaardig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen horen bij de stofklasse van de zuren? Kruis alles aan wat juist is.",
        opties=[
            "waterstofsulfaat, H₂SO₄",
            "waterstofnitraat, HNO₃",
            "natriumsulfaat, Na₂SO₄",
            "magnesiumoxide, MgO",
        ],
        antwoord=[0, 1],
        uitleg="Een zuur begint in de formule met waterstof dat als H⁺ kan weggaan. "
        "In Na₂SO₄ staat natrium op die plaats, dus is het een zout.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de formule die enkel zegt hoeveel atomen van elk element er in een molecule zitten?",
        antwoord=["brutoformule", "de brutoformule", "molecuulformule"],
        uitleg="C₂H₆O is een brutoformule. Ze zegt niet hoe de atomen aan elkaar zitten; "
        "daarvoor heb je een structuurformule nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zout is ontstaan uit een zuur en een base. Wat komt uit het zuur?",
        opties=[
            "de zuurrest",
            "het metaalion",
            "de hydroxidegroep",
            "het kristalwater",
        ],
        antwoord=0,
        uitleg="Uit HNO₃ en NaOH ontstaat NaNO₃: het nitraation komt van het zuur, het "
        "natriumion van de base.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle oxiden zijn binaire verbindingen.",
        antwoord=True,
        uitleg="Een oxide is zuurstof met één ander element, dus twee elementen. "
        "Een hydroxide heeft er drie en is dus geen oxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij zuurstofwater?",
        opties=[
            "H₂O₂",
            "H₂O",
            "HO₂",
            "H₂O₃",
        ],
        antwoord=0,
        uitleg="Zuurstofwater is waterstofperoxide, H₂O₂. Het valt langzaam uiteen in "
        "water en zuurstofgas, en daarom staat het in een donkere fles.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ammoniumzout bevat altijd een metaal.",
        antwoord=False,
        uitleg="Juist niet: in NH₄NO₃ zit geen enkel metaalatoom. Het ammoniumion neemt "
        "die plaats in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel verschillende elementen zitten er in een binaire verbinding?",
        antwoord=["twee", "2"],
        uitleg="Binair betekent twee elementen, hoeveel atomen er ook van elk in de "
        "formule staan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het Romeinse cijfer in de stocknotatie, zoals in ijzer(III)chloride?",
        opties=[
            "het geeft het oxidatiegetal van het metaal",
            "het geeft het aantal chlooratomen",
            "het geeft de plaats in het periodiek systeem",
            "het geeft de waardigheid van het zuur",
        ],
        antwoord=0,
        uitleg="IJzer kan +II of +III zijn. Het cijfer zegt welk van de twee, en daaruit "
        "volgt de formule: FeCl₃.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke soort stoffen gebruik je Griekse telwoorden zoals di- en tri- in de naam?",
        opties=[
            "bij atoomverbindingen",
            "bij ionverbindingen",
            "bij metaallegeringen",
            "bij hydraten van zouten",
        ],
        antwoord=0,
        uitleg="CO₂ is koolstofdioxide. Bij een ionverbinding volgt het aantal al uit de "
        "ladingen, dus daar zijn telwoorden niet nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de triviale naam van een waterige oplossing van waterstofchloride?",
        antwoord=["zoutzuur", "salzuur"],
        uitleg="HCl in water heet zoutzuur. De IUPAC-naam waterstofchloride hoort bij "
        "het gas zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen horen bij HNO₃? Kruis alles aan wat juist is.",
        opties=[
            "salpeterzuur",
            "waterstofnitraat",
            "salpeterigzuur",
            "waterstofnitriet",
        ],
        antwoord=[0, 1],
        uitleg="De uitgang -aat hoort bij het zuur met het meeste zuurstof: nitraat bij "
        "HNO₃, nitriet bij HNO₂.",
    ),
    dict(
        type="waarofniet",
        vraag="De uitgang -iet duidt op minder zuurstofatomen dan de uitgang -aat.",
        antwoord=True,
        uitleg="Sulfaat is SO₄²⁻, sulfiet is SO₃²⁻. Zo hoort zwaveligzuur bij H₂SO₃ en "
        "zwavelzuur bij H₂SO₄.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het voorvoegsel hypo- in hypochlorigzuur?",
        opties=[
            "nog één zuurstofatoom minder dan bij de uitgang -iet",
            "nog één zuurstofatoom meer dan bij de uitgang -aat",
            "nog één waterstofatoom meer dan gewoonlijk",
            "nog één chlooratoom minder dan gewoonlijk",
        ],
        antwoord=0,
        uitleg="De rij loopt van perchloorzuur HClO₄ over chloorzuur HClO₃ en "
        "chlorigzuur HClO₂ naar hypochlorigzuur HClO.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen dragen in het dagelijks leven een naam die niets over hun formule zegt? Kruis alles aan wat juist is.",
        opties=[
            "bijtende soda voor natriumhydroxide",
            "gebluste kalk voor calciumhydroxide",
            "waterstofsulfaat voor H₂SO₄",
            "calciumoxide voor CaO",
        ],
        antwoord=[0, 1],
        uitleg="Bijtende soda en gebluste kalk zijn gebruiksnamen. De twee andere zijn "
        "systematische namen, die de formule juist wel verraden.",
    ),
    dict(
        type="invultekst",
        vraag="Welk zout wordt in de keuken bakpoeder genoemd?",
        antwoord=["natriumwaterstofcarbonaat", "NaHCO3", "natriumbicarbonaat"],
        uitleg="NaHCO₃ geeft bij verwarmen koolstofdioxide af, en dat laat het deeg "
        "rijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen ongebluste en gebluste kalk?",
        opties=[
            "ongebluste kalk is CaO, gebluste kalk is Ca(OH)₂",
            "ongebluste kalk is Ca(OH)₂, gebluste kalk is CaO",
            "ongebluste kalk is CaCO₃, gebluste kalk is CaO",
            "ongebluste kalk is CaCl₂, gebluste kalk is CaCO₃",
        ],
        antwoord=0,
        uitleg="Giet je water bij CaO, dan ontstaat Ca(OH)₂ en komt er veel warmte vrij. "
        "Dat blussen zit in de naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke triviale naam hoort bij N₂O?",
        opties=[
            "lachgas",
            "koolzuurgas",
            "stikstofgas",
            "chloorgas",
        ],
        antwoord=0,
        uitleg="N₂O of distikstofmonoxide heet lachgas. Koolzuurgas is CO₂, een heel "
        "andere stof.",
    ),
    dict(
        type="waarofniet",
        vraag="Blauwzuur is de gebruiksnaam van waterstofchloride.",
        antwoord=False,
        uitleg="Blauwzuur is HCN of waterstofcyanide, heel giftig en met een geur van "
        "bittere amandelen. Waterstofchloride in water heet zoutzuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool hoort bij het element kalium?",
        opties=[
            "K",
            "Ka",
            "C",
            "Ca",
        ],
        antwoord=0,
        uitleg="Kalium is K, van het Latijnse kalium. Ca is calcium en C is koolstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke symbolen horen bij een metaal uit het d-blok? Kruis alles aan wat juist is.",
        opties=[
            "Fe",
            "Cu",
            "Si",
            "Ar",
        ],
        antwoord=[0, 1],
        uitleg="IJzer en koper zijn overgangsmetalen. Silicium staat in het p-blok en "
        "argon is een edelgas.",
    ),
    dict(
        type="invultekst",
        vraag="Welk element heeft het symbool Pb?",
        antwoord=["lood", "Pb"],
        uitleg="Pb komt van plumbum, het Latijnse woord voor lood. Daar komt ook "
        "loodgieter van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij soda?",
        opties=[
            "Na₂CO₃",
            "NaHCO₃",
            "NaOH",
            "NaCl",
        ],
        antwoord=0,
        uitleg="Soda is natriumcarbonaat. NaHCO₃ is bakpoeder en NaOH is bijtende soda: "
        "drie stoffen die in het dagelijks leven vaak verward worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Ozon en zuurstofgas zijn twee namen voor dezelfde stof.",
        antwoord=False,
        uitleg="Zuurstofgas is O₂, ozon is O₃. Beide bestaan uit zuurstofatomen, maar ze "
        "gedragen zich heel anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je CuSO₄·5H₂O volgens de IUPAC-regels?",
        opties=[
            "kopersulfaatpentahydraat",
            "kopersulfaatpentaoxide",
            "koperpentasulfaathydraat",
            "koperwaterstofsulfaat",
        ],
        antwoord=0,
        uitleg="Het Griekse telwoord penta- zegt hoeveel moleculen kristalwater er per "
        "formule-eenheid in het rooster zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heet in het dagelijks leven ontstopper?",
        opties=[
            "een sterke oplossing van natriumhydroxide",
            "een sterke oplossing van natriumchloride",
            "een verdunde oplossing van azijnzuur",
            "een verdunde oplossing van waterstofperoxide",
        ],
        antwoord=0,
        uitleg="Bijtende soda tast vet en haar aan. Daarom staat er een bijtend "
        "pictogram op de fles en horen er handschoenen bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een loogoplossing is een waterige oplossing van een hydroxide.",
        antwoord=True,
        uitleg="Loog is de gebruiksnaam voor een basische oplossing, meestal van NaOH of "
        "KOH.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het gas met de formule CO₂ in het dagelijks leven?",
        antwoord=["koolzuurgas", "koolstofdioxide"],
        uitleg="In drank heet CO₂ koolzuurgas, omdat het in water deels koolzuur H₂CO₃ "
        "vormt.",
    ),
]

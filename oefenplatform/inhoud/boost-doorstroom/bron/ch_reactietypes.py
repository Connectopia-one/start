# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Neerslag-, gas-, neutralisatie- en redoxreacties.

Hoort bij "organische en anorganische stoffen" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_anorganisch], [ch_organisch] en [ch_water].

Deel 1 gaat over de drie ionenuitwisselingsreacties van de fiche en over het
onderscheid tussen de stoffenreactievergelijking en de essentiële
reactievergelijking. De oplosbaarheden volgen de tabel die een kind op het
examen mag gebruiken. Deel 2 gaat over de redoxreacties: de oxidatiegetallen,
de elektronenoverdracht en de reactiepatronen die de fiche opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij een neerslagreactie?",
        opties=[
            "een slecht oplosbare vaste stof",
            "een gas dat uit de oplossing ontsnapt",
            "een neutrale oplossing met water",
            "een nieuw metaal op de bodem",
        ],
        antwoord=0,
        uitleg="Twee ionen uit de twee oplossingen vormen samen een stof die slecht oplost. Die zakt als vaste stof naar de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je giet zilvernitraat bij een oplossing van keukenzout. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er ontstaat een witte neerslag",
            "het zilverion en het chloride-ion reageren",
            "er komt een gas met een scherpe geur vrij",
            "de oplossing wordt daardoor basisch",
        ],
        antwoord=[0, 1],
        uitleg="Alle chloriden lossen goed op behalve die van zilver, dus vormen net die twee ionen een neerslag. Natrium en nitraat blijven gewoon opgelost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinaties geven een neerslag? Kruis alles aan wat juist is.",
        opties=[
            "Ba²⁺ en SO₄²⁻",
            "Ag¹⁺ en Cl¹⁻",
            "Na¹⁺ en NO₃¹⁻",
            "K¹⁺ en Cl¹⁻",
        ],
        antwoord=[0, 1],
        uitleg="Bariumsulfaat en zilverchloride staan in de tabel als slecht oplosbaar. Alle verbindingen met natrium of kalium lossen juist goed op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de essentiële reactievergelijking van de vorming van zilverchloride?",
        opties=[
            "Ag¹⁺ + Cl¹⁻ → AgCl",
            "AgNO₃ + NaCl → AgCl + NaNO₃",
            "Ag + Cl → AgCl",
            "Ag¹⁺ + NO₃¹⁻ → AgNO₃",
        ],
        antwoord=0,
        uitleg="In de essentiële vergelijking laat men de ionen weg die niets doen. Natrium en nitraat blijven gewoon opgelost, dus horen ze er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de ionen die in een oplossing niets doen tijdens de reactie?",
        opties=[
            "tribune-ionen",
            "zuurresten",
            "elektrolyten",
            "oxidatoren",
        ],
        antwoord=0,
        uitleg="Ze blijven opgelost en veranderen niet. Daarom staan ze niet in de essentiële reactievergelijking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je giet azijn op bakpoeder en er schuimt een gas op. Welk gas is dat?",
        opties=[
            "koolstofdioxide",
            "zuurstofgas",
            "waterstofgas",
            "ammoniak",
        ],
        antwoord=0,
        uitleg="Het zuur maakt uit het waterstofcarbonaat koolzuur, en dat valt onmiddellijk uiteen in water en koolstofdioxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gas komt vrij als je een zuur bij een sulfide giet?",
        opties=[
            "waterstofsulfide",
            "koolstofdioxide",
            "ammoniak",
            "chloorgas",
        ],
        antwoord=0,
        uitleg="Waterstofsulfide ruikt naar rotte eieren en is giftig. Daarom doet men zo'n proef onder een trekkast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gas komt vrij als je een sterke base bij een ammoniumzout giet?",
        opties=[
            "ammoniak",
            "koolstofdioxide",
            "waterstofgas",
            "stikstofgas",
        ],
        antwoord=0,
        uitleg="De base haalt een H⁺ van het ammoniumion weg, en wat overblijft is ammoniak. Je ruikt het meteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij een neutralisatiereactie?",
        opties=[
            "een zout en water",
            "een gas en een neerslag",
            "een metaal en een zuur",
            "twee nieuwe zuren",
        ],
        antwoord=0,
        uitleg="De H⁺ van het zuur en de OH⁻ van de base vormen water. Het metaalion en de zuurrest blijven als zout over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de essentiële reactievergelijking van een neutralisatie?",
        opties=[
            "H¹⁺ + OH¹⁻ → H₂O",
            "HCl + NaOH → NaCl + H₂O",
            "Na¹⁺ + Cl¹⁻ → NaCl",
            "H₂ + O₂ → H₂O",
        ],
        antwoord=0,
        uitleg="Enkel die twee ionen reageren echt. Het natriumion en het chloride-ion blijven opgelost en doen niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk zout ontstaat er als zoutzuur reageert met natriumhydroxide?",
        opties=[
            "natriumchloride",
            "natriumnitraat",
            "natriumsulfaat",
            "natriumcarbonaat",
        ],
        antwoord=0,
        uitleg="Het natriumion van de base en het chloride-ion van het zuur vormen samen het zout.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle nitraten zijn goed oplosbaar in water.",
        antwoord=True,
        uitleg="De tabel zegt dat voor nitraten zonder uitzondering. Daarom gebruikt men ze graag als men een ion in oplossing nodig heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Bariumsulfaat is goed oplosbaar in water.",
        antwoord=False,
        uitleg="Sulfaten zijn goed oplosbaar behalve die van barium. Juist daarom kan men bariumsulfaat veilig als contrastmiddel laten drinken.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle verbindingen met natrium zijn goed oplosbaar in water.",
        antwoord=True,
        uitleg="De tabel zegt bij natrium en bij kalium zonder meer alle. Dat maakt ze handig om een reactie mee op te zetten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een neutralisatie ontstaat er altijd een gas.",
        antwoord=False,
        uitleg="Bij een neutralisatie ontstaan een zout en water. Een gas hoort bij de gasontwikkelingsreactie.",
    ),
    dict(
        type="waarofniet",
        vraag="Carbonaten van natrium, kalium en ammonium zijn goed oplosbaar, de andere niet.",
        antwoord=True,
        uitleg="Dat staat zo in de tabel. Daarom slaat calciumcarbonaat neer als kalksteen of ketelsteen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het reactietype waarbij twee oplossingen samen een slecht oplosbare stof vormen?",
        antwoord=["neerslagreactie", "een neerslagreactie", "neerslag"],
        uitleg="De vaste stof die ontstaat, noemt men de neerslag.",
    ),
    dict(
        type="invultekst",
        vraag="Welk gas ontstaat er als je zoutzuur bij kalksteen giet?",
        antwoord=["CO2", "koolstofdioxide", "CO₂"],
        uitleg="Het zuur maakt uit het carbonaat koolzuur, en dat valt meteen uiteen in water en koolstofdioxide.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de vergelijking waarin enkel de ionen staan die echt reageren?",
        antwoord=["essentiële reactievergelijking", "essentiële vergelijking", "essentieel"],
        uitleg="De tribune-ionen laat men weg, want die veranderen niet.",
    ),
    dict(
        type="invultekst",
        vraag="Welk zout ontstaat er als zwavelzuur reageert met kaliumhydroxide?",
        antwoord=["kaliumsulfaat", "K2SO4"],
        uitleg="Het kaliumion van de base en het sulfaation van het zuur vormen het zout. Er is twee keer kalium nodig per sulfaation.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een oxidatie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het deeltje geeft elektronen af",
            "het oxidatiegetal van het deeltje stijgt",
            "het deeltje neemt elektronen op",
            "het deeltje verliest protonen uit zijn kern",
        ],
        antwoord=[0, 1],
        uitleg="Elk afgegeven elektron verhoogt het oxidatiegetal met één. Protonen blijven altijd in de kern zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het oxidatiegetal van een deeltje dat gereduceerd wordt?",
        opties=[
            "het daalt",
            "het stijgt",
            "het blijft gelijk",
            "het wordt altijd nul",
        ],
        antwoord=0,
        uitleg="Bij reductie neemt het deeltje elektronen op, en elk elektron verlaagt het oxidatiegetal met één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een oxidator in een redoxreactie?",
        opties=[
            "hij neemt elektronen op",
            "hij geeft elektronen af",
            "hij neemt protonen op",
            "hij verandert niet",
        ],
        antwoord=0,
        uitleg="De oxidator laat de andere stof oxideren en wordt daarbij zelf gereduceerd. De reductor doet net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een reductor zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "hij geeft elektronen af",
            "hij wordt zelf geoxideerd",
            "zijn oxidatiegetal daalt",
            "hij neemt elektronen op",
        ],
        antwoord=[0, 1],
        uitleg="Een reductor laat de andere stof reduceren door er elektronen aan te geven. Daarbij stijgt zijn eigen oxidatiegetal.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de reactie 2 Mg + O₂ → 2 MgO: wat gebeurt er met magnesium?",
        opties=[
            "het wordt geoxideerd van 0 naar +II",
            "het wordt gereduceerd van 0 naar −II",
            "het oxidatiegetal blijft nul",
            "het neemt twee elektronen op",
        ],
        antwoord=0,
        uitleg="Magnesium geeft per atoom twee elektronen af aan zuurstof. Het is hier dus de reductor.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de reactie 2 Mg + O₂ → 2 MgO: welke stof is de oxidator?",
        opties=[
            "het zuurstofgas",
            "het magnesium",
            "het magnesiumoxide",
            "er is geen oxidator",
        ],
        antwoord=0,
        uitleg="Zuurstof neemt de elektronen op en gaat van 0 naar −II. Wie elektronen opneemt, is de oxidator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coëfficiënten maken de verbranding ... C₂H₆ + ... O₂ → ... CO₂ + ... H₂O kloppend?",
        opties=[
            "2, 7, 4 en 6",
            "1, 3, 2 en 3",
            "2, 5, 4 en 6",
            "1, 7, 2 en 3",
        ],
        antwoord=0,
        uitleg="Twee moleculen ethaan geven vier CO₂ en zes H₂O. Rechts staan dan veertien zuurstofatomen, dus links zeven O₂.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de volledige verbranding van ethanol?",
        opties=[
            "koolstofdioxide en water",
            "koolstofmonoxide en waterstof",
            "azijnzuur en water",
            "koolstof en zuurstof",
        ],
        antwoord=0,
        uitleg="Ook een alcohol bevat enkel koolstof, waterstof en zuurstof. Bij genoeg zuurstof wordt alles CO₂ en H₂O.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstaat er bij een slechte verbranding koolstofmonoxide?",
        opties=[
            "er is te weinig zuurstof",
            "er is te veel zuurstof",
            "de brandstof is te zuiver",
            "de vlam is te warm",
        ],
        antwoord=0,
        uitleg="Bij te weinig zuurstof krijgt elk koolstofatoom maar één zuurstofatoom mee. Koolstofmonoxide is kleurloos, geurloos en dodelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er als een metaal met dizuurstof reageert?",
        opties=[
            "een metaaloxide",
            "een zuur",
            "een zout",
            "een hydroxide",
        ],
        antwoord=0,
        uitleg="Dat is een van de reactiepatronen van de fiche. Roest is zo een metaaloxide van ijzer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reacties zijn redoxreacties? Kruis alles aan wat juist is.",
        opties=[
            "het verbranden van propaan",
            "het roesten van ijzer",
            "zoutzuur dat natriumhydroxide neutraliseert",
            "zilvernitraat dat met keukenzout een neerslag geeft",
        ],
        antwoord=[0, 1],
        uitleg="Bij een redoxreactie gaan er elektronen over en veranderen de oxidatiegetallen. Bij een neutralisatie en bij een neerslagreactie wisselen de ionen enkel van partner.",
    ),
    dict(
        type="waarofniet",
        vraag="Oxidatie en reductie gebeuren altijd samen.",
        antwoord=True,
        uitleg="De elektronen die de ene stof afgeeft, moet de andere opnemen. Zonder ontvanger is er geen oxidatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verbranding is een redoxreactie.",
        antwoord=True,
        uitleg="De brandstof geeft elektronen af aan de zuurstof, dus veranderen de oxidatiegetallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een oxidatie daalt het oxidatiegetal van het deeltje.",
        antwoord=False,
        uitleg="Bij een oxidatie stijgt het, want het deeltje geeft elektronen af. Bij een reductie daalt het.",
    ),
    dict(
        type="waarofniet",
        vraag="In een enkelvoudige stof is het oxidatiegetal van elk atoom nul.",
        antwoord=True,
        uitleg="Er is geen partner die de elektronen naar zich toe trekt, dus blijft het getal op nul. Dat geldt ook voor O₂ en voor Fe.",
    ),
    dict(
        type="waarofniet",
        vraag="Een neerslagreactie is een vorm van elektronenoverdracht.",
        antwoord=False,
        uitleg="Bij een neerslagreactie wisselen de ionen enkel van partner en blijven hun ladingen gelijk. Dat is ionenuitwisseling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stof die in een redoxreactie elektronen afgeeft?",
        antwoord=["reductor", "de reductor"],
        uitleg="Door elektronen af te geven laat ze de andere stof reduceren, en wordt ze zelf geoxideerd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel moleculen O₂ heb je nodig om één molecule CH₄ volledig te verbranden?",
        antwoord=["2", "twee"],
        uitleg="Er ontstaan één CO₂ en twee H₂O, samen vier zuurstofatomen. Dat zijn twee moleculen O₂.",
    ),
    dict(
        type="invultekst",
        vraag="Welk metaaloxide ontstaat er als ijzer in vochtige lucht roest?",
        antwoord=["Fe2O3", "ijzer(III)oxide", "Fe₂O₃"],
        uitleg="Ijzer gaat daarbij naar oxidatiegetal +III. Roest is bruin en bladdert af, dus beschermt het het metaal eronder niet.",
    ),
    dict(
        type="invultekst",
        vraag="Wat ontstaat er als een niet-metaal met een ander niet-metaal reageert, bijvoorbeeld zwavel met zuurstof?",
        antwoord=["SO2", "zwaveldioxide", "een oxide"],
        uitleg="Zwaveldioxide is een niet-metaaloxide en dus zuurvormend. Met water in de lucht geeft het zure regen.",
    ),
]

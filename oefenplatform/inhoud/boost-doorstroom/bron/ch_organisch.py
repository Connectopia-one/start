# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Organische stoffen en de alkanen.

Hoort bij "organische en anorganische stoffen" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_anorganisch], [ch_water] en
[ch_reactietypes].

Deel 1 gaat over de alkanen: de omzettingen tussen naam en formule voor de
laagste tien n-alkanen, en de algemene formule. Deel 2 gaat over de vier andere
organische stofklassen van de fiche, hun functionele groep of specifieke
structuuronderdeel, en de triviale namen en toepassingen die de fiche opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat een alkaan?",
        opties=[
            "enkel uit koolstof en waterstof, met enkelvoudige bindingen",
            "uit koolstof, waterstof en zuurstof",
            "uit koolstof met een dubbele binding",
            "uit koolstof en een metaal",
        ],
        antwoord=0,
        uitleg="Alkanen zijn verzadigd: elke koolstof-koolstofbinding is een enkelvoudige binding, en de rest wordt opgevuld met waterstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij methaan?",
        opties=[
            "CH₄",
            "C₂H₆",
            "CH₃",
            "CH₂",
        ],
        antwoord=0,
        uitleg="Koolstof vormt vier bindingen, dus hangen er vier waterstofatomen aan dat ene koolstofatoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij propaan?",
        opties=[
            "C₃H₈",
            "C₃H₆",
            "C₂H₆",
            "C₃H₄",
        ],
        antwoord=0,
        uitleg="Met drie koolstofatomen geeft de regel 2n plus 2 acht waterstofatomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de algemene formule van de n-alkanen?",
        opties=[
            "CnH2n+2",
            "CnH2n",
            "CnH2n-2",
            "CnHn",
        ],
        antwoord=0,
        uitleg="Elke extra koolstof brengt twee waterstofatomen mee, en aan de twee uiteinden komt er telkens één bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel koolstofatomen heeft hexaan?",
        opties=[
            "zes",
            "vijf",
            "zeven",
            "acht",
        ],
        antwoord=0,
        uitleg="Het voorvoegsel hex- staat voor zes. De formule is dus C₆H₁₄.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk alkaan heeft de formule C₅H₁₂?",
        opties=[
            "pentaan",
            "butaan",
            "hexaan",
            "propaan",
        ],
        antwoord=0,
        uitleg="Vijf koolstofatomen is pent-, en 2 keer 5 plus 2 is twaalf waterstofatomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen horen bij een alkaan? Kruis alles aan wat juist is.",
        opties=[
            "butaan",
            "octaan",
            "etheen",
            "ethanol",
        ],
        antwoord=[0, 1],
        uitleg="De uitgang -aan hoort bij de alkanen. Etheen is een alkeen en ethanol is een alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij decaan?",
        opties=[
            "C₁₀H₂₂",
            "C₁₀H₂₀",
            "C₉H₂₀",
            "C₁₀H₁₈",
        ],
        antwoord=0,
        uitleg="Tien koolstofatomen geven 2 keer 10 plus 2, dus tweeëntwintig waterstofatomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de volledige verbranding van een alkaan?",
        opties=[
            "koolstofdioxide en water",
            "koolstofmonoxide en waterstof",
            "koolstof en zuurstof",
            "enkel waterdamp",
        ],
        antwoord=0,
        uitleg="De koolstof wordt CO₂ en de waterstof wordt H₂O. Bij te weinig zuurstof ontstaat ook het giftige koolstofmonoxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof is het hoofdbestanddeel van aardgas?",
        opties=[
            "methaan",
            "propaan",
            "butaan",
            "etheen",
        ],
        antwoord=0,
        uitleg="Aardgas bestaat vooral uit methaan. Propaan en butaan zitten in gasflessen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke alkanen gebruikt men als brandstof in een gasfles? Kruis alles aan wat juist is.",
        opties=[
            "propaan",
            "butaan",
            "decaan",
            "hexaan",
        ],
        antwoord=[0, 1],
        uitleg="Propaan en butaan zijn bij lichte druk al vloeibaar, dus krijg je er veel van in een kleine fles. Decaan en hexaan zijn bij kamertemperatuur vloeistoffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Alkanen bevatten enkel koolstof en waterstof.",
        antwoord=True,
        uitleg="Daarom horen ze bij de koolwaterstoffen. Komt er zuurstof bij, dan gaat het om een andere stofklasse.",
    ),
    dict(
        type="waarofniet",
        vraag="Ethaan heeft de formule C₂H₄.",
        antwoord=False,
        uitleg="Ethaan is C₂H₆. C₂H₄ is etheen, met een dubbele binding.",
    ),
    dict(
        type="waarofniet",
        vraag="De alkanen hebben allemaal de uitgang -aan in hun naam.",
        antwoord=True,
        uitleg="De uitgang zegt tot welke stofklasse een stof hoort: -aan, -een of -yn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alkaan lost goed op in water.",
        antwoord=False,
        uitleg="Alkanen zijn apolair en water is polair, dus mengen ze niet. Benzine blijft op water liggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe langer de koolstofketen van een alkaan, hoe hoger het kookpunt.",
        antwoord=True,
        uitleg="Bij een langere molecule zijn de londonkrachten tussen de moleculen groter. Methaan is daardoor een gas en octaan een vloeistof.",
    ),
    dict(
        type="invultekst",
        vraag="Welke formule hoort bij butaan?",
        antwoord=["C4H10", "C₄H₁₀"],
        uitleg="Vier koolstofatomen, en 2 keer 4 plus 2 is tien waterstofatomen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk alkaan heeft de formule C₇H₁₆?",
        antwoord=["heptaan", "het heptaan"],
        uitleg="Hept- staat voor zeven, en 2 keer 7 plus 2 is zestien.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel waterstofatomen heeft het alkaan met negen koolstofatomen?",
        antwoord=["20", "twintig"],
        uitleg="2 keer 9 plus 2 is twintig. Dat alkaan heet nonaan.",
    ),
    dict(
        type="invultekst",
        vraag="Welk alkaan zit in de gasfles van een barbecue, naast butaan?",
        antwoord=["propaan", "het propaan"],
        uitleg="Propaan blijft ook bij koud weer nog verdampen, dus werkt een propaanfles buiten in de winter beter.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het specifieke structuuronderdeel van een alkeen?",
        opties=[
            "een dubbele binding tussen twee koolstofatomen",
            "een drievoudige binding tussen twee koolstofatomen",
            "een OH-groep aan het uiteinde",
            "een COOH-groep aan het uiteinde",
        ],
        antwoord=0,
        uitleg="Door die dubbele binding zijn er twee waterstofatomen minder dan bij het alkaan. De algemene formule wordt CnH2n.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het specifieke structuuronderdeel van een alkyn?",
        opties=[
            "een drievoudige binding tussen twee koolstofatomen",
            "een dubbele binding tussen twee koolstofatomen",
            "een OH-groep aan het uiteinde",
            "een ring van zes koolstofatomen",
        ],
        antwoord=0,
        uitleg="Bij een alkyn delen twee koolstofatomen drie elektronenparen. De uitgang van de naam is dan -yn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functionele groep van een alcohol?",
        opties=[
            "OH",
            "COOH",
            "CO",
            "NH₂",
        ],
        antwoord=0,
        uitleg="De OH-groep hangt hier aan een koolstofatoom, niet aan een metaal. Daarom is een alcohol geen base.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functionele groep van een carbonzuur?",
        opties=[
            "COOH",
            "OH",
            "CH₃",
            "NO₃",
        ],
        antwoord=0,
        uitleg="De COOH-groep kan haar waterstof als H⁺ afgeven. Daarom reageert een carbonzuur zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam azijnzuur?",
        opties=[
            "ethaanzuur",
            "methaanzuur",
            "ethanol",
            "methanol",
        ],
        antwoord=0,
        uitleg="Ethaanzuur heeft twee koolstofatomen en een COOH-groep. Keukenazijn is een oplossing van ongeveer vijf procent ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn carbonzuren? Kruis alles aan wat juist is.",
        opties=[
            "methaanzuur",
            "ethaanzuur",
            "methanol",
            "etheen",
        ],
        antwoord=[0, 1],
        uitleg="Een carbonzuur heeft een COOH-groep. Methanol is een alcohol en etheen een alkeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn alcoholen? Kruis alles aan wat juist is.",
        opties=[
            "methanol",
            "ethanol",
            "methaanzuur",
            "etheen",
        ],
        antwoord=[0, 1],
        uitleg="De uitgang -ol hoort bij de alcoholen. Methaanzuur is een carbonzuur en etheen een alkeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruikt men etheen in de voedingssector?",
        opties=[
            "om vruchten sneller te laten rijpen",
            "om vlees langer te bewaren",
            "om water te ontkalken",
            "om brood te laten rijzen",
        ],
        antwoord=0,
        uitleg="Etheen is een plantenhormoon dat rijping op gang brengt. Daarom rijpt fruit sneller naast een rijpe banaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruikt men brandspiritus?",
        opties=[
            "als brandstof en als oplosmiddel",
            "als meststof voor planten",
            "als bleekmiddel voor textiel",
            "als koelvloeistof in een frigo",
        ],
        antwoord=0,
        uitleg="Brandspiritus is ethanol waaraan men een bittere stof toevoegt zodat niemand het opdrinkt. Het brandt met een bijna onzichtbare vlam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof geeft een brandnetelprik en een mierenbeet hun scherpe karakter en heet methaanzuur?",
        opties=[
            "HCOOH",
            "CH₃COOH",
            "CH₃OH",
            "CH₄",
        ],
        antwoord=0,
        uitleg="Methaanzuur is het eenvoudigste carbonzuur: één koolstofatoom met een COOH-groep. De oude naam is mierenzuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is methanol gevaarlijk, al lijkt het op drankalcohol?",
        opties=[
            "het lichaam zet het om in giftige stoffen",
            "het is radioactief",
            "het ontploft bij contact met water",
            "het lost niet op in water",
        ],
        antwoord=0,
        uitleg="In het lichaam wordt methanol omgezet in stoffen die het oog en het zenuwstelsel aantasten. Enkele milliliter kan al blind maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alkeen heeft de algemene formule CnH2n.",
        antwoord=True,
        uitleg="Door de dubbele binding zitten er twee waterstofatomen minder in dan bij het alkaan met dezelfde keten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alcohol is een base, want de formule bevat een OH-groep.",
        antwoord=False,
        uitleg="Bij een base hangt de OH-groep aan een metaalion en komt ze als OH⁻ vrij. In een alcohol zit ze vast aan koolstof.",
    ),
    dict(
        type="waarofniet",
        vraag="Een carbonzuur kan zijn waterstof als H⁺ afgeven.",
        antwoord=True,
        uitleg="Net die eigenschap maakt het een zuur. Daarom heeft azijn een pH onder zeven.",
    ),
    dict(
        type="waarofniet",
        vraag="Etheen heeft dezelfde formule als ethaan.",
        antwoord=False,
        uitleg="Etheen is C₂H₄ en ethaan is C₂H₆. De dubbele binding scheelt twee waterstofatomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Organische stoffen zijn verbindingen waarin koolstof de hoofdrol speelt.",
        antwoord=True,
        uitleg="De koolstofketen is het geraamte. Koolstofdioxide en de carbonaten zijn de klassieke uitzonderingen: die rekent men bij de anorganische stoffen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof heeft de triviale naam drankalcohol en de formule C₂H₅OH?",
        antwoord=["ethanol", "het ethanol"],
        uitleg="Ethanol is de alcohol die bij gisting ontstaat en die ook in handgel zit.",
    ),
    dict(
        type="invultekst",
        vraag="Tot welke organische stofklasse hoort een stof met een COOH-groep?",
        antwoord=["carbonzuur", "een carbonzuur", "carbonzuren"],
        uitleg="De COOH-groep kan een H⁺ afgeven, dus reageert de stof als een zuur.",
    ),
    dict(
        type="invultekst",
        vraag="Welke uitgang heeft de naam van een alkyn?",
        antwoord=["-yn", "yn"],
        uitleg="De uitgang -yn staat voor een drievoudige binding tussen twee koolstofatomen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke organische stof in keukenazijn heeft de IUPAC-naam ethaanzuur?",
        antwoord=["azijnzuur", "ethaanzuur", "CH3COOH"],
        uitleg="Azijnzuur is de triviale naam. Twee koolstofatomen met een COOH-groep, dus ethaanzuur.",
    ),
]

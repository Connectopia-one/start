# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Stoffen in water: polariteit, oplossen en pH.

Hoort bij "organische en anorganische stoffen" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_anorganisch], [ch_organisch] en
[ch_reactietypes].

Deel 1 gaat over polaire en apolaire stoffen, de vier intermoleculaire krachten
van de fiche en de oplosbaarheid die daaruit volgt. Deel 2 gaat over
elektrolyten, over het verschil tussen dissociëren en ioniseren, en over de
pH-schaal met de twee indicatoren die op het examen in de bijlage staan.

De fiche spreekt af dat een binding met een verschil in elektronegativiteit
onder 0,4 als apolair geldt, en vanaf 0,4 als polair.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een binding tussen twee atomen polair?",
        opties=[
            "als het verschil in elektronegativiteit minstens 0,4 is",
            "als beide atomen een metaal zijn",
            "als de atomen evenveel elektronen hebben",
            "als de stof vast is bij kamertemperatuur",
        ],
        antwoord=0,
        uitleg="Bij een groot verschil trekt het ene atoom de elektronen duidelijk naar zich toe. De binding krijgt dan een plus- en een minkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een watermolecule polair?",
        opties=[
            "de molecule is gebogen en zuurstof trekt harder",
            "de molecule is recht en volledig symmetrisch",
            "de molecule bevat een metaal",
            "de molecule heeft geen vrije elektronenparen",
        ],
        antwoord=0,
        uitleg="Zuurstof trekt de elektronen naar zich toe, en door de hoek vallen de twee effecten niet weg. Er blijft dus een minkant en een pluskant over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn apolair? Kruis alles aan wat juist is.",
        opties=[
            "CCl₄",
            "hexaan",
            "water",
            "natriumchloride",
        ],
        antwoord=[0, 1],
        uitleg="CCl₄ is symmetrisch, dus vallen de polaire bindingen tegen elkaar weg. Alkanen zoals hexaan zijn de klassieke apolaire stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de vuistregel voor de oplosbaarheid van stoffen?",
        opties=[
            "gelijk lost op in gelijk",
            "zwaar lost op in licht",
            "vast lost op in vast",
            "zuur lost op in zuur",
        ],
        antwoord=0,
        uitleg="Polaire stoffen lossen op in polaire oplosmiddelen en apolaire in apolaire. Daarom mengt olie niet met water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lost olie niet op in water?",
        opties=[
            "olie is apolair en water polair",
            "olie is te zwaar voor water",
            "olie is een zout en water niet",
            "olie bevat geen koolstof",
        ],
        antwoord=0,
        uitleg="De watermoleculen houden elkaar sterk vast met waterstofbruggen en laten de apolaire oliemoleculen er niet tussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke intermoleculaire kracht is de sterkste van de vier?",
        opties=[
            "de waterstofbrug",
            "de londonkracht",
            "de dipoolkracht",
            "geen van de vier",
        ],
        antwoord=0,
        uitleg="Een waterstofbrug ontstaat als waterstof aan zuurstof, stikstof of fluor hangt. Daardoor kookt water pas bij honderd graden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht werkt tussen de moleculen van een apolaire stof?",
        opties=[
            "de londonkracht",
            "de waterstofbrug",
            "de ion-dipoolkracht",
            "de ionbinding",
        ],
        antwoord=0,
        uitleg="Londonkrachten ontstaan uit tijdelijke, toevallige verschuivingen van de elektronen. Ze zijn zwak maar werken tussen alle moleculen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht houdt een opgelost ion vast aan de watermoleculen eromheen?",
        opties=[
            "de ion-dipoolkracht",
            "de londonkracht",
            "de metaalbinding",
            "de atoombinding",
        ],
        antwoord=0,
        uitleg="De minkant van het water richt zich naar een positief ion en de pluskant naar een negatief ion. Dat omhullen heet hydratatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het omhullen van een opgelost ion door watermoleculen?",
        opties=[
            "hydratatie",
            "destillatie",
            "adsorptie",
            "neutralisatie",
        ],
        antwoord=0,
        uitleg="Het water omringt elk ion apart en houdt het zo in oplossing. Daardoor valt het rooster van het zout uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kookt water bij een veel hogere temperatuur dan je bij zo'n kleine molecule zou verwachten?",
        opties=[
            "de watermoleculen houden elkaar vast met waterstofbruggen",
            "water bevat een metaal dat de warmte vasthoudt",
            "water is apolair en apolaire stoffen koken hoog",
            "watermoleculen zijn zwaarder dan luchtmoleculen",
        ],
        antwoord=0,
        uitleg="Om te koken moet je die bruggen verbreken, en dat vraagt veel energie. Daarom blijft water vloeibaar tot honderd graden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen lossen goed op in water? Kruis alles aan wat juist is.",
        opties=[
            "keukenzout",
            "suiker",
            "olijfolie",
            "paraffine",
        ],
        antwoord=[0, 1],
        uitleg="Keukenzout bestaat uit ionen en suiker heeft veel OH-groepen, dus allebei goed bruikbaar voor het polaire water. Olie en paraffine zijn apolair.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecule met polaire bindingen kan als geheel toch apolair zijn.",
        antwoord=True,
        uitleg="Als de molecule symmetrisch is, vallen de effecten tegen elkaar weg. CCl₄ en CO₂ zijn zo.",
    ),
    dict(
        type="waarofniet",
        vraag="Een waterstofbrug is sterker dan een atoombinding.",
        antwoord=False,
        uitleg="Een waterstofbrug is de sterkste van de krachten tússen moleculen, maar nog altijd veel zwakker dan een binding bínnen een molecule.",
    ),
    dict(
        type="waarofniet",
        vraag="Een apolair oplosmiddel is geschikt om vet te verwijderen.",
        antwoord=True,
        uitleg="Vet is apolair, dus lost het goed op in een apolair oplosmiddel. Daarom werkt vlekkenwater op een vetvlek en water niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een binding met een verschil in elektronegativiteit van 0,2 is polair.",
        antwoord=False,
        uitleg="De afspraak van de fiche legt de grens op 0,4. Onder die waarde geldt de binding als apolair.",
    ),
    dict(
        type="waarofniet",
        vraag="Londonkrachten werken tussen alle moleculen, ook tussen polaire.",
        antwoord=True,
        uitleg="Elke molecule heeft elektronen die toevallig even opzij schuiven. Bij polaire stoffen komen de dipoolkrachten er bovenop.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een stof die een plus- en een minkant heeft?",
        antwoord=["polair", "een polaire stof", "polaire stof"],
        uitleg="Zo'n stof lost goed op in water, want water is zelf polair.",
    ),
    dict(
        type="invultekst",
        vraag="Welke intermoleculaire kracht ontstaat als waterstof aan zuurstof, stikstof of fluor hangt?",
        antwoord=["waterstofbrug", "een waterstofbrug", "waterstofbruggen"],
        uitleg="Die kracht is de sterkste tussen moleculen en verklaart het hoge kookpunt van water.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kracht werkt tussen twee polaire moleculen onderling?",
        antwoord=["dipoolkracht", "de dipoolkracht", "dipoolkrachten"],
        uitleg="De pluskant van de ene molecule richt zich naar de minkant van de andere.",
    ),
    dict(
        type="invultekst",
        vraag="Is CO₂ als molecule polair of apolair?",
        antwoord=["apolair", "apolaire"],
        uitleg="De molecule is recht en symmetrisch, dus vallen de twee polaire bindingen tegen elkaar weg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een elektrolyt zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het geeft in water vrij bewegende ionen",
            "het geleidt elektriciteit in oplossing",
            "het lost niet op in water",
            "het is altijd een zuur",
        ],
        antwoord=[0, 1],
        uitleg="De ionen kunnen de lading doorgeven, dus geleidt de oplossing. Zouten, zuren en hydroxiden zijn alle drie elektrolyten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als een zout in water dissocieert?",
        opties=[
            "de ionen uit het rooster komen los in het water",
            "de moleculen vallen uiteen in atomen",
            "het zout verandert in een zuur",
            "er ontstaan nieuwe moleculen",
        ],
        antwoord=0,
        uitleg="De ionen bestonden al in het rooster; het water trekt ze alleen los van elkaar. Daarom spreekt men van dissociëren en niet van ioniseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen ioniseren en dissociëren?",
        opties=[
            "bij ioniseren ontstaan de ionen pas in het water",
            "bij ioniseren verdampt het oplosmiddel",
            "bij dissociëren ontstaan nieuwe moleculen",
            "er is geen verschil tussen die twee",
        ],
        antwoord=0,
        uitleg="Een zout bevat al ionen en dissocieert. Een polaire molecule zoals HCl heeft er nog geen en vormt ze pas in water, dus ioniseert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de dissociatievergelijking van NaCl in water?",
        opties=[
            "NaCl → Na¹⁺ + Cl¹⁻",
            "NaCl → Na + Cl",
            "NaCl → NaOH + HCl",
            "NaCl + H₂O → NaOH + Cl₂",
        ],
        antwoord=0,
        uitleg="Het rooster valt uiteen in de ionen die er al in zaten: één natriumion en één chloride-ion per formule-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de ionisatievergelijking van HCl in water?",
        opties=[
            "HCl → H¹⁺ + Cl¹⁻",
            "HCl → H + Cl",
            "HCl → H₂ + Cl₂",
            "HCl + H₂O → HClO + H₂",
        ],
        antwoord=0,
        uitleg="De polaire binding breekt en het waterstofatoom laat zijn elektron bij chloor. Zo ontstaan een H⁺ en een Cl⁻.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de dissociatievergelijking van CaCl₂ in water?",
        opties=[
            "CaCl₂ → Ca²⁺ + 2 Cl¹⁻",
            "CaCl₂ → Ca¹⁺ + Cl₂¹⁻",
            "CaCl₂ → Ca²⁺ + Cl²⁻",
            "CaCl₂ → CaCl¹⁺ + Cl¹⁻",
        ],
        antwoord=0,
        uitleg="Calcium geeft een ion met lading 2+ en elk chloride-ion heeft lading 1−, dus zijn er twee chloride-ionen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen geleiden elektriciteit als ze in water opgelost zijn? Kruis alles aan wat juist is.",
        opties=[
            "NaCl",
            "HCl",
            "suiker",
            "hexaan",
        ],
        antwoord=[0, 1],
        uitleg="Keukenzout dissocieert en waterstofchloride ioniseert, dus krijg je beweegbare ionen. Suiker lost op zonder ionen te vormen, en hexaan lost niet op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een oplossing met een pH van 3?",
        opties=[
            "ze is zuur",
            "ze is basisch",
            "ze is neutraal",
            "ze geleidt nooit",
        ],
        antwoord=0,
        uitleg="Onder zeven is de oplossing zuur, boven zeven basisch. Hoe lager het getal, hoe meer H⁺ er in zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kleur krijgt lakmoes in een zuur midden?",
        opties=[
            "rood",
            "blauw",
            "paars",
            "kleurloos",
        ],
        antwoord=0,
        uitleg="Lakmoes wordt rood in een zuur en blauw in een base. Die twee kleuren staan in de bijlage die je op het examen mag gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kleur krijgt fenolftaleïne in een basisch midden?",
        opties=[
            "paars",
            "rood",
            "blauw",
            "kleurloos",
        ],
        antwoord=0,
        uitleg="Fenolftaleïne blijft kleurloos in een zuur en in een neutraal midden, en wordt paars zodra de oplossing basisch is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oplossing is kleurloos met fenolftaleïne en rood met lakmoes. Wat weet je dan?",
        opties=[
            "de oplossing is zuur",
            "de oplossing is basisch",
            "de oplossing is zeker neutraal",
            "je kan er niets uit besluiten",
        ],
        antwoord=0,
        uitleg="Rood lakmoes wijst op een zuur. Fenolftaleïne is in een zuur én in een neutraal midden kleurloos, dus beslist lakmoes hier.",
    ),
    dict(
        type="waarofniet",
        vraag="Zuiver water heeft een pH van 7.",
        antwoord=True,
        uitleg="De concentratie H⁺ en OH⁻ zijn er gelijk, dus is de oplossing neutraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe hoger de pH, hoe meer H⁺ in de oplossing.",
        antwoord=False,
        uitleg="Het is net omgekeerd: een hoge pH betekent weinig H⁺ en veel OH⁻, dus een basische oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hydroxide geeft in water OH⁻-ionen.",
        antwoord=True,
        uitleg="Die ionen maken de oplossing basisch. NaOH geeft er één per formule-eenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Suiker opgelost in water is een elektrolyt.",
        antwoord=False,
        uitleg="Suiker lost wel goed op, maar als neutrale moleculen. Zonder ionen is er geen geleiding.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vast zout is een isolator.",
        antwoord=True,
        uitleg="De ionen zitten vast in het rooster, dus kan er geen lading door. Opgelost of gesmolten geleidt hetzelfde zout wel.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk toestel meet je de pH van een oplossing nauwkeurig?",
        antwoord=["pH-meter", "een pH-meter", "pH meter"],
        uitleg="Een indicator geeft een gebied aan, een pH-meter een getal met decimalen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kleur krijgt lakmoes in een basisch midden?",
        antwoord=["blauw", "blauwe"],
        uitleg="Rood in een zuur, blauw in een base. Zo zie je in één oogopslag welke kant je oplossing op is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die in water geen ionen vormt en dus niet geleidt?",
        antwoord=["niet-elektrolyt", "een niet-elektrolyt", "niet elektrolyt"],
        uitleg="Suiker en ethanol lossen wel op, maar blijven neutrale moleculen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk ion maakt een oplossing zuur?",
        antwoord=["H+", "waterstofion", "proton"],
        uitleg="Een zuur geeft bij ionisatie H⁺ vrij. Hoe meer daarvan, hoe lager de pH.",
    ),
]

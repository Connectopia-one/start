# -*- coding: utf-8 -*-
"""pH, pOH en rekenen met zuren en basen — 🌍 Beyond, chemie.

Deel 1 gaat over de schaal zelf: de pH als negatieve logaritme van de
concentratie hydroxoniumionen, de pOH, hun som van 14, de ionisatieconstante van
water, en wat een verschil van één of twee eenheden werkelijk betekent. Deel 2
gaat over het rekenwerk: de pH van een sterk zuur of een sterke base, het effect
van verdunnen of indampen, en het verschil met een zwak zuur, waar de
zuurconstante nodig is.

De getallen zijn zo gekozen dat ze zonder rekentoestel uitkomen: machten van
tien, en concentraties die een hele pH-waarde geven. Alle waarden gelden bij
25 °C.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de pH van een oplossing?",
        opties=[
            "de negatieve logaritme van de concentratie hydroxoniumionen",
            "de negatieve logaritme van de concentratie hydroxide-ionen",
            "de concentratie hydroxoniumionen in mol per liter",
            "het aantal mol zuur dat je in de oplossing gedaan hebt",
        ],
        antwoord=0,
        uitleg="Is [H₃O⁺] gelijk aan 10⁻³ mol/L, dan is de pH 3. De schaal maakt van heel "
        "kleine getallen een handig getal tussen 0 en 14.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is pH plus pOH bij 25 °C?",
        opties=[
            "veertien",
            "zeven",
            "tien",
            "een",
        ],
        antwoord=0,
        uitleg="Dat volgt uit de ionisatieconstante van water, 10⁻¹⁴. Ken je de pH, dan "
        "ken je dus ook de pOH.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft zuiver water bij 25 °C?",
        antwoord=["7", "pH 7", "zeven"],
        uitleg="In zuiver water is [H₃O⁺] gelijk aan [OH⁻], namelijk 10⁻⁷ mol/L. Daarom "
        "is pH 7 het neutrale punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oplossing heeft pH 4. Wat is haar pOH?",
        opties=[
            "tien",
            "vier",
            "zeven",
            "veertien",
        ],
        antwoord=0,
        uitleg="Veertien min vier is tien. De concentratie hydroxide-ionen is dus "
        "10⁻¹⁰ mol/L.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing met pH 3 bevat honderd keer meer hydroxoniumionen dan een oplossing met pH 5.",
        antwoord=True,
        uitleg="Elke pH-eenheid is een factor tien. Twee eenheden verschil is dus een "
        "factor honderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een basische oplossing zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "haar pH is groter dan 7",
            "haar pOH is kleiner dan 7",
            "haar pH is kleiner dan 7",
            "ze bevat geen hydroxoniumionen meer",
        ],
        antwoord=[0, 1],
        uitleg="Er blijven altijd hydroxoniumionen in, want het evenwicht van water staat "
        "nooit helemaal stil. Ze zijn alleen in de minderheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de waarde van de ionisatieconstante van water bij 25 °C?",
        opties=[
            "10⁻¹⁴",
            "10⁻⁷",
            "10⁻¹",
            "10¹⁴",
        ],
        antwoord=0,
        uitleg="Kw is [H₃O⁺] maal [OH⁻]. In zuiver water is dat 10⁻⁷ maal 10⁻⁷.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft een oplossing met [H₃O⁺] gelijk aan 10⁻² mol/L?",
        antwoord=["2", "pH 2", "twee"],
        uitleg="De pH is de exponent zonder minteken. Dat is een flink zure oplossing, "
        "ongeveer zo zuur als citroensap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oplossing heeft pOH 2. Welke pH hoort daarbij?",
        opties=[
            "twaalf",
            "twee",
            "zeven",
            "veertien",
        ],
        antwoord=0,
        uitleg="Veertien min twee is twaalf. Dat is een sterk basische oplossing, zoals "
        "ontstopper.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de pH-schaal zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is logaritmisch opgebouwd",
            "één eenheid verschil is een factor tien",
            "ze loopt altijd van 0 tot 14 en nooit erbuiten",
            "één eenheid verschil is een factor twee",
        ],
        antwoord=[0, 1],
        uitleg="Bij heel geconcentreerde oplossingen kan de pH zelfs onder nul of boven "
        "veertien liggen. De schaal is dus geen grens, maar een rekenwijze.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe hoger de pH, hoe meer hydroxoniumionen er in de oplossing zitten.",
        antwoord=False,
        uitleg="Net omgekeerd: door het minteken in de logaritme hoort een hoge pH bij "
        "een lage concentratie hydroxoniumionen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de concentratie hydroxide-ionen in een oplossing met pH 9?",
        opties=[
            "10⁻⁵ mol/L",
            "10⁻⁹ mol/L",
            "10⁻⁷ mol/L",
            "10⁵ mol/L",
        ],
        antwoord=0,
        uitleg="pOH is veertien min negen, dus vijf. Daar hoort een concentratie van "
        "10⁻⁵ mol/L bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men een logaritmische schaal voor de zuurtegraad?",
        opties=[
            "de concentraties liggen over heel veel machten van tien verspreid",
            "de concentraties zijn anders niet te meten met een pH-meter",
            "de schaal moet van nul tot veertien lopen voor elke oplossing",
            "de pH is anders niet met een indicator te bepalen",
        ],
        antwoord=0,
        uitleg="Van 1 mol/L tot 10⁻¹⁴ mol/L is een verschil van veertien machten. Met "
        "gewone getallen zou dat onhandelbaar zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pOH heeft een oplossing met pH 11?",
        antwoord=["3", "pOH 3", "drie"],
        uitleg="Veertien min elf is drie. Hun som is bij 25 °C altijd veertien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oplossingen zijn zuur? Kruis alles aan wat juist is.",
        opties=[
            "een oplossing met pH 2",
            "een oplossing met pOH 12",
            "een oplossing met pH 9",
            "een oplossing met pOH 3",
        ],
        antwoord=[0, 1],
        uitleg="pOH 12 hoort bij pH 2, dus zuur. pOH 3 hoort bij pH 11, en dat is "
        "basisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee oplossingen, één met pH 1 en één met pH 4. Hoeveel keer zuurder is de eerste?",
        opties=[
            "duizend keer",
            "honderd keer",
            "vier keer",
            "tien keer",
        ],
        antwoord=0,
        uitleg="Drie eenheden verschil is tien maal tien maal tien. Dat is een factor "
        "duizend in de concentratie hydroxoniumionen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een basische oplossing is er meer hydroxide dan hydroxonium.",
        antwoord=True,
        uitleg="Hun product blijft 10⁻¹⁴. Zit er veel van het ene in, dan zit er dus "
        "weinig van het andere in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een pH van 6,5 in regenwater. Wat besluit je?",
        opties=[
            "het is lichtzuur, want de pH ligt onder zeven",
            "het is lichtbasisch, want de pH ligt boven zes",
            "het is neutraal, want de pH ligt dicht bij zeven",
            "het is sterk zuur, want de pH ligt onder zeven",
        ],
        antwoord=0,
        uitleg="Regenwater is lichtzuur doordat er koolstofdioxide uit de lucht in oplost. "
        "Dat vormt koolzuur.",
    ),
    dict(
        type="waarofniet",
        vraag="De pH van een oplossing hangt niet af van de temperatuur.",
        antwoord=False,
        uitleg="De ionisatieconstante van water verandert met de temperatuur, en dus ook "
        "het neutrale punt. Bij 25 °C is dat zeven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het product van de concentratie hydroxonium en hydroxide in water?",
        antwoord=["Kw", "ionisatieconstante", "waterconstante"],
        uitleg="Bij 25 °C is die 10⁻¹⁴. Daaruit volgt dat pH en pOH samen veertien geven.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de pH van 0,01 mol/L zoutzuur?",
        opties=[
            "2",
            "1",
            "12",
            "0,01",
        ],
        antwoord=0,
        uitleg="Zoutzuur is een sterk zuur, dus [H₃O⁺] is 0,01 of 10⁻² mol/L. Daar hoort "
        "pH 2 bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de pH van 0,001 mol/L natriumhydroxide?",
        opties=[
            "11",
            "3",
            "10",
            "13",
        ],
        antwoord=0,
        uitleg="Een sterke base geeft [OH⁻] gelijk aan 10⁻³, dus pOH 3 en pH 11.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft 0,1 mol/L zoutzuur?",
        antwoord=["1", "pH 1", "een"],
        uitleg="0,1 is 10⁻¹, dus pH 1. Zoutzuur ioniseert volledig, en daarom mag je de "
        "concentratie van het zuur rechtstreeks gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdunt een sterk zuur tien keer. Wat gebeurt er met de pH?",
        opties=[
            "ze stijgt met één eenheid",
            "ze daalt met één eenheid",
            "ze stijgt met tien eenheden",
            "ze blijft ongeveer dezelfde",
        ],
        antwoord=0,
        uitleg="Tien keer minder hydroxoniumionen is één logaritme-eenheid. Verdunnen "
        "maakt een zuur dus minder zuur, maar nooit basisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Door een sterk zuur heel sterk te verdunnen kan de pH boven zeven komen.",
        antwoord=False,
        uitleg="De pH kruipt naar zeven toe en blijft eronder. Water zelf kan de oplossing "
        "niet basisch maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je dampt een oplossing van een sterk zuur in tot de helft van het volume. Wat gebeurt er met de pH?",
        opties=[
            "ze daalt, want de concentratie wordt groter",
            "ze stijgt, want er verdwijnt zuur met het water",
            "ze blijft gelijk, want er is evenveel zuur in de beker",
            "ze wordt precies de helft van wat ze was",
        ],
        antwoord=0,
        uitleg="Het aantal mol zuur blijft gelijk, het volume halveert, dus verdubbelt de "
        "concentratie. De pH daalt met ongeveer 0,3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig voor de pH van een zwak zuur? Kruis alles aan wat juist is.",
        opties=[
            "de concentratie van het zuur",
            "de zuurconstante van het zuur",
            "het volume van de oplossing",
            "de molaire massa van het zuur",
        ],
        antwoord=[0, 1],
        uitleg="Bij een zwak zuur ioniseert maar een deel. Hoeveel precies, dat zegt de "
        "zuurconstante.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft 0,0001 mol/L zoutzuur?",
        antwoord=["4", "pH 4", "vier"],
        uitleg="0,0001 is 10⁻⁴, dus pH 4. Let goed op het aantal nullen voor de komma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee oplossingen van 0,1 mol/L: één zoutzuur, één azijnzuur. Welke heeft de laagste pH?",
        opties=[
            "het zoutzuur, want het is een sterk zuur",
            "het azijnzuur, want het heeft meer koolstofatomen",
            "ze hebben precies dezelfde pH",
            "het azijnzuur, want het is een zwak zuur",
        ],
        antwoord=0,
        uitleg="Zoutzuur geeft al zijn protonen af, azijnzuur maar een paar procent. Toch "
        "zit er in beide bekers evenveel mol zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je bij een sterk zuur de concentratie van het zuur als [H₃O⁺] nemen?",
        opties=[
            "elk molecule staat zijn proton af, dus is de omzetting volledig",
            "een sterk zuur heeft altijd een concentratie van 1 mol per liter",
            "de zuurconstante van een sterk zuur is gelijk aan één",
            "de pH van een sterk zuur ligt altijd onder de één",
        ],
        antwoord=0,
        uitleg="Bij een zwak zuur mag dat niet: daar blijft het grootste deel als "
        "molecule in de oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een tweewaardig sterk zuur is de concentratie hydroxoniumionen dubbel die van het zuur.",
        antwoord=True,
        uitleg="Zwavelzuur van 0,05 mol/L geeft ongeveer 0,1 mol/L hydroxoniumionen, dus "
        "pH 1. Reken dus altijd eerst de waardigheid mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oplossing heeft pH 5. Wat is de concentratie hydroxoniumionen?",
        opties=[
            "10⁻⁵ mol/L",
            "10⁻⁹ mol/L",
            "5 mol/L",
            "10⁵ mol/L",
        ],
        antwoord=0,
        uitleg="Je draait de logaritme om: [H₃O⁺] is tien tot de macht min de pH.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het verdunnen van een zwak zuur zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de ionisatiegraad wordt groter",
            "de pH wordt hoger",
            "de ionisatiegraad wordt kleiner",
            "de zuurconstante wordt kleiner",
        ],
        antwoord=[0, 1],
        uitleg="Het evenwicht schuift bij verdunnen naar de kant van de ionen, dus "
        "ioniseert een groter deel. Toch zijn er in totaal minder ionen per liter.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft 0,01 mol/L natriumhydroxide?",
        antwoord=["12", "pH 12", "twaalf"],
        uitleg="pOH is 2, dus pH is 14 min 2. Reken bij een base altijd eerst de pOH uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mengt gelijke volumes van een sterk zuur en een sterke base van dezelfde concentratie. Wat verwacht je?",
        opties=[
            "een neutrale oplossing met pH 7",
            "een zure oplossing met pH onder 7",
            "een basische oplossing met pH boven 7",
            "een oplossing waarvan de pH niet te voorspellen is",
        ],
        antwoord=0,
        uitleg="Alle hydroxonium- en hydroxide-ionen reageren precies weg tot water. Er "
        "blijft een neutraal zout over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom daalt de pH van een sterk zuur niet onder nul bij gewone concentraties?",
        opties=[
            "daarvoor zou de concentratie boven 1 mol per liter moeten liggen",
            "de pH-schaal staat negatieve waarden niet toe",
            "water neutraliseert het overschot aan zuur altijd",
            "een sterk zuur ioniseert nooit volledig in water",
        ],
        antwoord=0,
        uitleg="pH 0 hoort bij 1 mol/L. Bij een nog hogere concentratie kan de pH "
        "inderdaad negatief worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oplossing heeft de hoogste pH?",
        opties=[
            "0,1 mol/L natriumhydroxide",
            "0,001 mol/L natriumhydroxide",
            "0,1 mol/L azijnzuur",
            "zuiver water bij 25 °C",
        ],
        antwoord=0,
        uitleg="0,1 mol/L geeft pOH 1 en dus pH 13. De verdunde base komt maar aan pH 11.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwak zuur en een sterk zuur van dezelfde concentratie neutraliseren evenveel base.",
        antwoord=True,
        uitleg="Het aantal mol zuur bepaalt hoeveel base je nodig hebt, niet de sterkte. "
        "Daarom verbruiken ze bij een titratie hetzelfde volume.",
    ),
    dict(
        type="waarofniet",
        vraag="De pH van een zwak zuur bereken je rechtstreeks uit zijn concentratie.",
        antwoord=False,
        uitleg="Daar heb je ook de zuurconstante voor nodig, want maar een deel van de "
        "moleculen staat zijn proton af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel keer meer hydroxoniumionen zitten er in een oplossing van pH 2 dan in een van pH 4?",
        antwoord=["100", "honderd", "100 keer"],
        uitleg="Twee eenheden verschil op een logaritmische schaal is tien maal tien.",
    ),
]

"""Samenhang en causaliteit — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond over samenhang en causaliteit (met de prent van de ijsjes) binnen wi_causaliteit, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import steekproeven as S
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(S.VRAGEN, [0, 1, 2, 14, 16, 17, 18, 24, 25, 26, 27]) + [
    casus(
        "Een gemeente plaatst in vijf straten extra straatlampen. Een jaar later zijn er in die straten minder inbraken. "
        "De burgemeester zegt: « Licht houdt inbrekers weg. » In hetzelfde jaar daalde het aantal inbraken in de hele gemeente.",
        [
            mk("Wat moet je nog nagaan voor je de burgemeester gelijk geeft?",
               ["Of de inbraken in straten zonder nieuwe lampen ook daalden.", "Of de nieuwe lampen ook 's nachts genoeg licht geven op de hele stoep.", "Of de inwoners de nieuwe lampen mooi vinden.", "Hoeveel de nieuwe lampen gekost hebben."], 0,
               "Je hebt een vergelijkingsgroep nodig."),
            keuze("De straten zonder nieuwe lampen spelen hier de rol van [[*controlegroep|steekproef|verborgen variabele]].", "Zo zie je of de daling door de lampen komt."),
            open_("Welke andere verklaring voor de daling is mogelijk?",
                  "Er kan een andere oorzaak zijn die in de hele gemeente speelde, zoals meer politiecontroles of een buurtwerking. Dan zou de daling ook zonder de lampen gekomen zijn.",
                  "Een daling die overal optreedt, wijst op een factor die overal speelt."),
        ],
    ),
    tabel("Welk verband is het meest waarschijnlijk?", [
        ("Wie meer oefent met de gitaar, speelt beter.", "causaliteit"),
        ("Steden met meer ziekenhuizen hebben meer zieken.", "derde variabele"),
        ("Wie zich slecht voelt, sport minder.", "omgekeerde causaliteit"),
        ("Het aantal piraten daalde terwijl de aarde opwarmde.", "toeval"),
    ], "Bij de ziekenhuizen speelt de grootte van de stad mee.", kolommen=["causaliteit", "omgekeerde causaliteit", "derde variabele", "toeval"]),
    mk("Leerlingen met meer boeken thuis halen betere punten voor taal. Welke verborgen variabele ligt voor de hand?",
       ["hoeveel er thuis gelezen en voorgelezen wordt", "de kleur en de grootte van de boekenkast in de woonkamer", "het aantal boeken op de schoolbibliotheek", "de afstand van huis tot de school"], 0,
       "Thuis lezen beïnvloedt zowel het aantal boeken als de taalpunten."),
    mk("Hoe toon je het best aan dat een nieuwe leermethode betere punten geeft?",
       ["Twee groepen lukraak maken: de ene krijgt de methode, de andere niet.", "Na een maand aan alle leerlingen vragen of ze de nieuwe methode goed vinden.", "Kijken of de beste leerlingen de methode al gebruiken.", "De methode een jaar gebruiken en de punten bekijken."], 0,
       "Een gecontroleerde proef met een controlegroep."),
    keuze("Een onderzoek dat alleen [[*waarneemt|een proef doet]], kan nooit met zekerheid een oorzaak aantonen.", "Er kan altijd een verborgen variabele meespelen."),
    sorteer("Is de samenhang positief of negatief?", ["positief", "negatief"], [
        ["hoe meer je oefent, hoe minder fouten je maakt", "negatief"], ["hoe ouder een kind, hoe groter", "positief"],
        ["hoe warmer het is, hoe minder soep er verkocht wordt", "negatief"], ["hoe meer uren je werkt, hoe meer je verdient", "positief"],
    ], "Negatief: als de ene stijgt, daalt de andere."),
    mk("Een reclame zegt: « Wie onze vitaminepillen neemt, is minder vaak ziek. » Wat ontbreekt er om dat te geloven?",
       ["een vergelijking met een groep die de pillen niet neemt", "een grote foto van een gezonde, lachende persoon op de verpakking", "een duurdere verpakking met meer pillen erin", "een lijst met de prijzen van andere merken"], 0,
       "Wie pillen neemt, leeft misschien ook in andere opzichten gezonder."),
    tabel("Klopt dit over samenhang?", [
        ("Samenhang is geen bewijs van causaliteit.", J),
        ("Bij een verborgen variabele beïnvloeden de twee variabelen elkaar niet rechtstreeks.", J),
        ("Van samenhang spreek je alleen als beide variabelen stijgen.", F),
        ("Een controlegroep helpt om een oorzakelijk verband aan te tonen.", J),
    ], "Ook als de ene stijgt en de andere daalt, is er samenhang."),
    mk("Een studie ziet dat wie meer koffie drinkt, minder slaapt. Welke omgekeerde verklaring is mogelijk?",
       ["Wie minder slaapt, drinkt meer koffie om wakker te blijven.", "Koffie zorgt er bij iedereen en altijd voor dat je minder slaapt.", "Er is geen enkel verband tussen koffie en slaap.", "Wie meer koffie drinkt, slaapt juist veel langer."], 0,
       "Oorzaak en gevolg kunnen omgewisseld zijn."),
    open_("In landen met meer smartphones leven mensen gemiddeld langer. Leg uit waarom smartphones daar waarschijnlijk niet de oorzaak van zijn.",
          "In rijkere landen hebben meer mensen een smartphone, en in rijkere landen is ook de gezondheidszorg beter. De welvaart is een verborgen variabele die beide verklaart.",
          "Zoek de factor die beide variabelen tegelijk beïnvloedt."),
    koppel("Koppel elk begrip aan zijn betekenis.", [
        ["causaliteit", "de ene variabele veroorzaakt de andere"], ["omgekeerde causaliteit", "het gevolg blijkt de oorzaak te zijn"],
        ["verborgen variabele", "een derde factor beïnvloedt beide"], ["toevallige samenhang", "twee reeksen lopen samen zonder verklaring"],
    ], ["de steekproef is te klein"], "Vier gevallen bij een statistisch verband."),
    inv("In een klas van \\(20\\) leerlingen gaan \\(8\\) leerlingen naar de muziekschool. Van die \\(8\\) halen er \\(6\\) meer dan \\(70\\) % voor wiskunde, van de anderen \\(6\\). Hoeveel procent van de leerlingen zonder muziekschool haalt meer dan \\(70\\) %?", ["50", "50 %", "50%"],
        "Twaalf leerlingen gaan niet, en daarvan halen er zes het: de helft."),
    keuze("Uit het vorige voorbeeld mag je [[*niet|wel]] besluiten dat de muziekschool betere wiskundepunten veroorzaakt.", "Twintig leerlingen zijn weinig en er kan een verborgen variabele meespelen."),
    mk("Een verzekeraar merkt dat jonge chauffeurs met een sportwagen vaker ongevallen hebben. Wat is de voorzichtigste uitspraak?",
       ["Er is samenhang, maar de manier van rijden kan beide verklaren.", "Sportwagens veroorzaken zelf de ongevallen, los van wie er rijdt.", "Ongevallen zorgen ervoor dat mensen een sportwagen kopen.", "Er is geen enkele samenhang tussen de twee, het is allemaal toeval."], 0,
       "Wie graag snel rijdt, kiest vaker een sportwagen."),
    tabel("Is dit een gecontroleerde proef of een waarnemingsonderzoek?", [
        ("je vraagt aan mensen hoeveel ze sporten en hoe gezond ze zijn", "waarneming"),
        ("je geeft lukraak de helft van de planten meststof en meet de groei", "proef"),
        ("je vergelijkt de punten van leerlingen die zelf kozen om bijles te volgen", "waarneming"),
    ], "In een proef bepaal jij wie wat krijgt.", kolommen=["proef", "waarneming"]),
]

"""Begrippen uit de moraalfilosofie — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_moraal: het moreel dilemma, waarden en normen,
goed en kwaad en vrijheid en verantwoordelijkheid. Met zes zelfgetekende
kaartjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, LICHTGROEN

KA = Prent("zes-kaartjes-moraal", "Zes kaartjes op het prikbord", "zes kaartjes met een woord of een regel, letters A tot F")
KA.rect(30, 60, 940, 560, "#e8dcc0", "#8a8470", 10, 3)
KAART = [("A", 70, 100, ["eerlijkheid"], "#fff6c8"), ("B", 380, 100, ["Je laat anderen", "uitspreken."], "#fff6c8"),
         ("C", 690, 100, ["vrijheid"], "#fff6c8"), ("D", 70, 360, ["Je spiekt niet", "op een examen."], "#fff6c8"),
         ("E", 380, 360, ["respect"], "#fff6c8"), ("F", 690, 360, ["Je kiest zelf", "welke kleren je draagt."], "#fff6c8")]
for t, x, y, regels, vul in KAART:
    KA.rect(x, y, 240, 200, vul, DONKER, 6, 2)
    KA.cirkel(x + 120, y + 12, 8, "#b03a2e", DONKER, 1)
    for i, r in enumerate(regels):
        KA.tekst(x + 120, y + 100 + i * 30 - (len(regels) - 1) * 15, r, 22)
    KA.letter(x + 210, y + 170, t)
U = "zes-kaartjes-moraal.svg"
Z = {t: [Prent.zone(x, y, 240, 200)] for t, x, y, r, v in KAART}

VOORVAL = ("Lees het voorval.\n\n"
           "Lotte ziet dat haar beste vriendin Jade tijdens een toets spiekt. Na de toets vraagt de leerkracht aan Lotte of ze iets gezien heeft. "
           "Als Lotte de waarheid zegt, krijgt Jade een nul. Als ze zwijgt, liegt ze tegen de leerkracht.")

VRAGEN = [
    klik("Bekijk de kaartjes op het prikbord. Klik op de norm die volgt uit de waarde respect.", U, Z["B"], "Respect wordt zichtbaar in hoe je met anderen omgaat."),
    klik("Klik op de norm die volgt uit de waarde eerlijkheid.", U, Z["D"], "Uit eerlijkheid volgt ook: niet bedriegen bij een examen."),
    klik("Klik op de waarde die achter de norm op kaartje F zit.", U, Z["C"], "Zelf kiezen: vrijheid."),
    klik("Klik op de waarde die achter de norm op kaartje D zit.", U, Z["A"], "De norm maakt de waarde concreet."),
    casus(VOORVAL, [
        keuze("Dit is een moreel dilemma, want [[*elke keuze schendt iets waardevols|er is een duidelijk juiste keuze|niemand iets verliest]].", "Een vlotte oplossing is er niet."),
        mk("Welke twee waarden botsen voor Lotte?",
           ["eerlijkheid en trouw", "vrijheid en gezondheid van de leerlingen", "respect en het recht op privacy van de leerkracht", "veiligheid en de vrije meningsuiting op school"],
           0, "Eerlijk zijn tegenover trouw blijven aan een vriendin."),
        keuze("Lotte moet haar keuze [[*verantwoorden met argumenten|geheimhouden|laten afhangen van toeval]].", "Daar dient de AUB-methode voor."),
        tabel("Klopt dit over Lottes keuze?",
              [("Er is een keuze zonder enige pijn.", F), ("Beide waarden zijn echt.", J), ("Het dilemma lost zich vanzelf op als ze wacht.", F)],
              "Daarom knelt het."),
    ]),
    sorteer("Waarde of norm?", ["waarde", "norm"],
            [("solidariteit", "waarde"), ("Je mag niet stelen.", "norm"), ("respect", "waarde"), ("Je laat iemand uitspreken.", "norm"), ("vrijheid", "waarde"), ("Je liegt niet.", "norm")],
            "De waarde is het doel, de norm de regel ernaartoe."),
    koppel("Koppel het begrip aan de uitleg.",
           [("waarde", "iets wat je belangrijk vindt"), ("norm", "een concrete regel die uit een waarde volgt"), ("moreel dilemma", "een keuze waarbij elke optie iets waardevols schendt"), ("moreel relativisme", "goed hangt af van de cultuur")],
           ["een regel die nooit verandert"], "Vier begrippen uit de moraalfilosofie."),
    mk("In het ene land geef je elkaar een hand, in het andere buig je. Wat toont dat?",
       ["dezelfde waarde, andere normen", "een andere waarde, maar precies dezelfde norm", "dat beide landen respect onbelangrijk vinden", "dat normen nooit uit een waarde voortkomen"],
       0, "Beide vinden respect belangrijk, maar de regels verschillen."),
    tabel("Klopt dit over normen?",
          [("Normen volgen uit waarden.", J), ("Normen zijn overal en altijd dezelfde.", F), ("Uit één waarde kunnen meerdere normen volgen.", J), ("Een norm is minder concreet dan een waarde.", F)],
          "Normen verschillen per cultuur en per tijd."),
    mk("Iemand zegt: 'Slavernij was in die cultuur normaal, dus het was daar goed.' Welk probleem van het moreel relativisme toont die zin?",
       ["je kan dan niets meer afkeuren", "het vraagt te veel van gewone mensen in het dagelijkse leven", "het zegt dat er maar één cultuur echt goed is", "het laat geen enkele verschillende norm toe"],
       0, "Geen grond meer om onrecht elders af te wijzen."),
    keuze("Iemand steelt omdat hij met een mes bedreigd wordt. Zijn verantwoordelijkheid is [[*kleiner|groter|even groot]], want zijn vrijheid was beperkt.", "Zonder keuze geen schuld."),
    keuze("Een kind van vier breekt met opzet een vaas. Zijn verantwoordelijkheid is [[*beperkt|volledig|onbestaand]], want het overziet de gevolgen nog niet goed.", "Verantwoordelijkheid groeit met het vermogen gevolgen te overzien."),
    tabel("Klopt dit over vrijheid en verantwoordelijkheid?",
          [("Verantwoordelijkheid veronderstelt vrijheid.", J), ("Vrijheid betekent dat alles mag.", F), ("Vrijheid kan beperkt zijn.", J), ("Wie niet kon kiezen, kan je minder verwijten.", J)],
          "Vrijheid in de ethiek is kunnen kiezen en je keuze verantwoorden."),
    sleep("Een [[waarde]] zegt wat belangrijk is. Een [[norm]] zegt wat je dus moet doen. Wie vrij kiest, draagt [[verantwoordelijkheid]].",
          ["dilemma", "relativisme"], "Waarden en normen, vrijheid en verantwoordelijkheid."),
    keuze("Een wet verbiedt roken op een terras. Hier botsen vrijheid en [[*gezondheid|eerlijkheid|trouw]].", "De vrijheid van de een tegen de gezondheid van de ander."),
    mk("Een leerling kent de schoolregel, maar weet niet waarom ze er is. Waarom is dat een probleem in een dilemma?",
       ["hij kan de regel niet wegen", "omdat schoolregels alleen voor de jongste kinderen gelden", "omdat waarden altijd strenger zijn dan normen", "omdat je normen anders nergens kan opschrijven"],
       0, "Wie enkel de regel kent, kan ze niet wegen in een dilemma."),
    inv("Hoe noem je het standpunt dat goed en kwaad afhangen van de cultuur? Twee woorden.", ["moreel relativisme", "relativisme", "het moreel relativisme"], "Het moreel relativisme."),
    tabel("Is dit een moreel dilemma?",
          [("Een arts heeft één bed en twee zieke patiënten.", J), ("Je kiest tussen een rode of een blauwe trui.", F), ("Je kan een vriend verklikken of zwijgen.", J), ("Je moet kiezen tussen één leven redden of vijf.", J)],
          "Bij een dilemma botsen twee waarden, niet twee smaken."),
    keuze("Als alles door brein en omstandigheden bepaald is, wankelt de [[*schuldvraag|kleurenleer|tijdlijn]].", "Het probleem van de vrije wil."),
    mk("Waarom kan onderzoek de vraag naar goed en kwaad niet beslechten?",
       ["het toont wat mensen vinden", "omdat onderzoekers zelf helemaal geen waarden of normen hebben", "omdat er nog nooit iemand een onderzoek over goed en kwaad deed", "omdat goed en kwaad enkel in oude filosofieboeken bestaan"],
       0, "Het blijft een filosofische vraag."),
    keuze("Begrippen als waarden en normen blijven abstract tot je ze toepast op [[*een echte casus|een rekensom|een tijdlijn]].", "Dan merk je hoe waarden botsen."),
    inv("Welk begrip hoort als paar bij vrijheid? Eén woord.", ["verantwoordelijkheid", "verantwoordelijk"], "Het ene zonder het andere heeft geen zin."),
    keuze("Uit de waarde eerlijkheid volgen [[*meerdere normen|precies één norm|geen normen]]: niet stelen, niet liegen, niet bedriegen bij een examen.", "Eén waarde, meerdere regels."),
    tabel("Hoort dit begrip bij de moraalfilosofie van dit thema?",
          [("moreel dilemma", J), ("waarden en normen", J), ("vrijheid en verantwoordelijkheid", J), ("monisme en dualisme", F)],
          "Monisme en dualisme horen bij lichaam en geest."),
    mk("Hoe verantwoord je volgens dit thema je keuze in een dilemma?",
       ["met argument, uitleg en voorbeeld", "door te doen wat de meerderheid van de klas het beste vindt", "door de keuze te laten afhangen van het toeval met een munt", "door gewoon niets te kiezen en af te wachten"],
       0, "De AUB-methode."),
    keuze("Zodra je iets goed noemt, moet je zeggen [[*waaraan je dat afmeet|hoe oud je bent|wie het eerst zei]].", "Goed en kwaad vragen om een maatstaf."),
    open_("Bedenk zelf een moreel dilemma uit het dagelijkse leven. Noem de twee waarden die botsen.",
          "Bijvoorbeeld: je vriend vertelt je een geheim, maar je merkt dat hij zichzelf in gevaar brengt. Trouw (het geheim bewaren) botst met zorg of bescherming (iemand inlichten die kan helpen). Elke keuze kost iets."),
]

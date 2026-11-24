"""Wetenschappelijk onderzoek, ontwerpen en STEM — pittig (🧬 Beyond doorstroom, biologie)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Grafiek met een uitschieter --------------------------------------------
GR = Prent("grafiek-waterpest", "Zuurstofbelletjes van waterpest bij verschillende lampafstanden", "puntgrafiek: hoe dichter de lamp, hoe meer belletjes; één punt ligt duidelijk lager dan de rest")
X, Y = assen(GR, 0, 60, 0, 40, "afstand lamp (cm)", "belletjes per minuut", 10, 10, boven=110)
PUNTEN = [(10, 34), (20, 26), (30, 8), (40, 13), (50, 9), (60, 6)]
GR.pad("M" + " L".join(f"{X(x):.0f} {Y(y):.0f}" for x, y in [(10, 34), (20, 26), (30, 19), (40, 13), (50, 9), (60, 6)]), "none", GRIJS, 2)
for x, y in PUNTEN:
    GR.cirkel(X(x), Y(y), 9, BLAUW if (x, y) != (30, 8) else ORANJE, DONKER, 1.5)
ZGR = {"uit": [Prent.rond(X(30), Y(8), 26)], "eerste": [Prent.rond(X(10), Y(34), 26)]}

# Ontwerpcyclus -------------------------------------------------------------
OC = Prent("ontwerpcyclus", "De cyclus van het ontwerpen", "vijf vakjes: probleem en eisen, ideeën bedenken, prototype bouwen, testen, bijsturen; pijlen ertussen; letters A tot E")
STAP = [("A", "probleem en eisen"), ("B", "ideeën bedenken"), ("C", "prototype bouwen"), ("D", "testen"), ("E", "bijsturen")]
MX, MY, R = 500, 330, 200
POS = []
for i, (k, t) in enumerate(STAP):
    h = math.radians(-90 + i * 72)
    x, y = MX + R * math.cos(h), MY + R * math.sin(h)
    POS.append((x, y))
for i in range(5):
    x1, y1 = POS[i]
    x2, y2 = POS[(i + 1) % 5] if i < 4 else POS[2]
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    OC.pijl(x1 + dx / d * 85, y1 + dy / d * 45, x2 - dx / d * 85, y2 - dy / d * 45, DONKER, 2)
for i, (k, t) in enumerate(STAP):
    x, y = POS[i]
    OC.rect(x - 80, y - 30, 160, 60, "#fbf6ea", DONKER, 12, 2)
    OC.tekst(x, y + 6, t, 16, vet=True)
    OC.letter(x - 100, y - 38, k)
ZOC = {k: [Prent.zone(POS[i][0] - 80, POS[i][1] - 30, 160, 60), Prent.rond(POS[i][0] - 100, POS[i][1] - 38, 22)] for i, (k, t) in enumerate(STAP)}

VRAGEN = [
    klik(
        "Klik op de meting die een uitschieter is.",
        GR.bestand, ZGR["uit"],
        "Bij 30 cm verwacht je ongeveer 19 belletjes, niet 8.",
    ),
    met_prent(GR.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("De afstand van de lamp is de onafhankelijke variabele.", J),
            ("Het aantal belletjes is de afhankelijke variabele.", J),
            ("De meting bij 30 cm herhaal je best.", J),
            ("De meting bij 30 cm laat je stilletjes weg uit je verslag.", F),
        ],
        "Een uitschieter vermeld je en probeer je te verklaren.",
    )),
    met_prent(GR.bestand, mk(
        "Welk besluit past bij deze grafiek?",
        [
            "Dichter bij de lamp, meer belletjes",
            "Hoe verder de lamp, hoe meer belletjes per minuut",
            "De lamp heeft geen enkele invloed op de belletjes",
            "De plant maakt bij 30 cm geen zuurstof meer aan",
        ],
        0,
        "Meer licht geeft meer fotosynthese en dus meer zuurstof.",
    )),
    klik(
        "Een prototype haalt de eisen niet. Klik op de stap die je dan zet.",
        OC.bestand, ZOC["E"],
        "Je stuurt bij en bouwt en test opnieuw: ontwerpen verloopt in rondes.",
    ),
    met_prent(OC.bestand, tabel(
        "Kijk naar de ontwerpcyclus. Klopt dit?",
        [
            ("Na E bouw je een aangepast prototype.", J),
            ("A legt vast wat de oplossing moet kunnen.", J),
            ("De kosten en het milieu horen al bij A.", J),
            ("Na de eerste test is het ontwerp altijd klaar.", F),
        ],
        "Meestal zijn er meerdere rondes van bouwen, testen en bijsturen.",
    )),
    casus(
        "Jonas wil weten of de temperatuur invloed heeft op de werking van het enzym amylase. Hij zet vijf proefbuizen klaar met zetmeel en amylase, elk bij een andere temperatuur.",
        [
            tabel(
                "Welke rol speelt dit in de proef van Jonas?",
                [
                    ("de temperatuur", "Onafhankelijk"),
                    ("de tijd tot het zetmeel weg is", "Afhankelijk"),
                    ("de hoeveelheid amylase", "Constant"),
                    ("de hoeveelheid zetmeel", "Constant"),
                ],
                "Alleen de temperatuur mag verschillen.",
                kolommen=["Onafhankelijk", "Afhankelijk", "Constant"],
            ),
            keuze(
                "Een buis met zetmeel maar zonder amylase dient als [[*controleproef|hypothese|prototype]].",
                "Zo zie je of het zetmeel ook zonder enzym verdwijnt.",
            ),
            mk(
                "Jonas meet elke temperatuur maar één keer. Wat is daar het probleem mee?",
                [
                    "Een toevallige afwijking valt dan niet op",
                    "Het enzym werkt dan bij geen enkele temperatuur",
                    "Een enzym mag maar één keer gebruikt worden",
                    "Hij heeft dan te veel metingen om te tekenen",
                ],
                0,
                "Door te herhalen middelen toevallige afwijkingen uit.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van een wetenschappelijk onderzoek in volgorde.",
        ["Probleem afbakenen", "Onderzoeksvraag stellen", "Hypothese opschrijven", "Proef uitvoeren en meten", "Resultaten verwerken", "Besluit en reflectie"],
        "De hypothese schrijf je vooraf, niet na de proef.",
    ),
    tabel(
        "Waarneming of besluit?",
        [
            ("De bladeren van plant A zijn geel.", "Waarneming"),
            ("Plant A kreeg te weinig licht.", "Besluit"),
            ("Er ontstaan 12 belletjes per minuut.", "Waarneming"),
            ("Meer licht versnelt de fotosynthese.", "Besluit"),
        ],
        "Een waarneming is wat je ziet, een besluit wat je eruit afleidt.",
        kolommen=["Waarneming", "Besluit"],
    ),
    tabel(
        "Is dit een goede onderzoeksvraag?",
        [
            ("Kiemen tuinkerszaden sneller bij 25 °C dan bij 15 °C?", J),
            ("Is biologie leuk?", F),
            ("Hoeveel zuurstofbelletjes maakt waterpest bij 10 en bij 30 cm van een lamp?", J),
            ("Waarom bestaan planten?", F),
        ],
        "Een goede vraag is afgebakend en met een meting te beantwoorden.",
    ),
    mk(
        "Sara geeft vijf bonenplanten op de vensterbank water met suiker en vijf bonenplanten in de kelder gewoon water. Waarom kan ze niets besluiten over suiker?",
        [
            "Ook het licht verschilt",
            "Vijf planten per groep zijn veel te veel",
            "Suiker mag je nooit op planten testen",
            "Bonen groeien helemaal niet op een vensterbank",
        ],
        0,
        "Je weet dan niet of het verschil van de suiker of van het licht komt.",
    ),
    inv(
        "Vijf metingen geven 12, 14, 13, 15 en 11 belletjes. Wat is het gemiddelde?",
        ["13"],
        "(12 + 14 + 13 + 15 + 11) / 5 = 65 / 5 = 13.",
    ),
    tabel(
        "Klopt dit over het gemiddelde en de spreiding?",
        [
            ("Twee reeksen met hetzelfde gemiddelde kunnen een andere spreiding hebben.", J),
            ("Een reeks met een grote spreiding is minder betrouwbaar.", J),
            ("Een uitschieter kan het gemiddelde sterk verschuiven.", J),
            ("Het gemiddelde zegt alles over hoe betrouwbaar de metingen zijn.", F),
        ],
        "Kijk ook naar hoe ver de metingen uit elkaar liggen.",
    ),
    tabel(
        "Toevallige of systematische fout?",
        [
            ("de stopwatch telkens te laat indrukken", "Systematisch"),
            ("een balans die niet op nul gezet is", "Systematisch"),
            ("één keer verkeerd aflezen", "Toevallig"),
            ("een kleine schommeling in de temperatuur", "Toevallig"),
        ],
        "Een systematische fout zit in elke meting en verdwijnt niet door te herhalen.",
        kolommen=["Toevallig", "Systematisch"],
    ),
    tabel(
        "Welk soort grafiek past het best?",
        [
            ("de lengte van een plant, elke dag gemeten", "Lijngrafiek"),
            ("het aantal kiemende zaden bij vier soorten meststof", "Staafdiagram"),
            ("de temperatuur in een serre over een week", "Lijngrafiek"),
            ("het aantal vogels per soort in een tuin", "Staafdiagram"),
        ],
        "Een lijn toont een verloop, staven vergelijken losse groepen.",
        kolommen=["Lijngrafiek", "Staafdiagram"],
    ),
    mk(
        "Er worden meer ijsjes verkocht op dagen dat er meer mensen verdrinken. Welke verklaring is het meest waarschijnlijk?",
        [
            "Warm weer verhoogt allebei",
            "IJsjes eten doet mensen verdrinken",
            "Verdrinkingen doen mensen ijs kopen",
            "Er is geen enkel verband tussen beide",
        ],
        0,
        "Er is een verband, maar geen oorzaak: een gemeenschappelijke oorzaak.",
    ),
    tabel(
        "Klopt dit over een grafiek?",
        [
            ("De onafhankelijke variabele staat op de horizontale as.", J),
            ("Bij elke as hoort een grootheid en een eenheid.", J),
            ("Een as mag bij een andere waarde dan nul beginnen, als je dat duidelijk toont.", J),
            ("De schaalverdeling mag onregelmatig zijn.", F),
        ],
        "Een regelmatige schaal maakt de vorm van het verband eerlijk zichtbaar.",
    ),
    koppel(
        "Koppel elke letter van STEM aan zijn betekenis.",
        [
            ("S", "wetenschappen"),
            ("T", "technologie"),
            ("E", "techniek, ontwerpen"),
            ("M", "wiskunde"),
        ],
        ["economie"],
        "STEM verbindt die vier domeinen.",
    ),
    tabel(
        "Onderzoeken of ontwerpen?",
        [
            ("nagaan of zout de kieming remt", "Onderzoeken"),
            ("een bewateringssysteem voor de serre bouwen", "Ontwerpen"),
            ("een prototype testen en bijsturen", "Ontwerpen"),
            ("een hypothese toetsen", "Onderzoeken"),
        ],
        "Onderzoek zoekt een antwoord, ontwerpen zoekt een oplossing.",
        kolommen=["Onderzoeken", "Ontwerpen"],
    ),
    sleep(
        "Een proef is pas betrouwbaar als iemand anders ze kan [[reproduceren]] met hetzelfde resultaat. Daarom beschrijf je je [[werkwijze]] nauwkeurig en laat je je besluit door anderen [[nalezen]].",
        ["vergeten", "hypothese", "weggooien"],
        "Wetenschappelijk werk wordt nagelezen voor het verschijnt.",
    ),
    tabel(
        "Wat hoort in een besluit?",
        [
            ("een antwoord op de onderzoeksvraag", J),
            ("de gegevens waarop dat antwoord steunt", J),
            ("of de hypothese bevestigd of weerlegd is", J),
            ("enkel de metingen die in je verwachting passen", F),
        ],
        "Ook een weerlegde hypothese is een resultaat.",
    ),
    mk(
        "Tom laat drie tuinkerszaden kiemen, Lies vijftig. Wiens resultaat is het betrouwbaarst, en waarom?",
        [
            "Van Lies, door de grotere steekproef",
            "Van Tom, want drie zaden kiemen altijd samen",
            "Van Tom, want hij moet minder tellen",
            "Ze zijn even betrouwbaar, kiemen is altijd gelijk",
        ],
        0,
        "Bij drie zaden kan één slecht zaadje het hele resultaat bepalen.",
    ),
    tabel(
        "Klopt dit over een school die het waterverbruik van haar serre wil verlagen?",
        [
            ("Eerst meten hoeveel water er nu verbruikt wordt.", J),
            ("De oplossing moet ook betaalbaar zijn.", J),
            ("Ook het milieu telt mee bij de keuze.", J),
            ("Testen is overbodig als het idee goed klinkt.", F),
        ],
        "Zonder meting weet je niet of de oplossing werkt.",
    ),
    keuze(
        "Waarnemingen noteer je [[*tijdens|een week na|vóór]] de proef.",
        "Wie achteraf noteert, vult onbewust aan wat hij verwachtte.",
    ),
    tabel(
        "Klopt dit over reflecteren na een proef?",
        [
            ("Je gaat na wat het resultaat onzeker maakt.", J),
            ("Je vermeldt wat er misliep, zoals een gebroken buis.", J),
            ("Je stelt voor hoe het beter kan.", J),
            ("Je past je metingen aan tot ze kloppen met de hypothese.", F),
        ],
        "Eerlijk rapporteren is de basis van wetenschap.",
    ),
    keuze(
        "Het verwachte antwoord dat je vóór de proef opschrijft, heet de [[*hypothese|controleproef|uitschieter]].",
        "Een hypothese is een toetsbare verwachting.",
    ),
    tabel(
        "Hoort dit in een onderzoeksplan?",
        [
            ("welk materiaal je nodig hebt", J),
            ("hoe je meet en hoe vaak", J),
            ("het besluit, al op voorhand ingevuld", F),
            ("welke variabelen je constant houdt", J),
        ],
        "Het besluit volgt pas uit de metingen.",
    ),
    keuze(
        "Een eerste werkend model dat je bouwt en test, heet een [[*prototype|hypothese|steekproef]].",
        "Het hoeft nog niet mooi te zijn, wel te werken.",
    ),
    open_(
        "Leg uit waarom je in een proef maar één factor tegelijk laat verschillen.",
        "Als je maar één factor verandert en de rest constant houdt, kan elk verschil in het resultaat alleen van die factor komen. Verander je twee factoren tegelijk, bv. licht en meststof, dan weet je niet welke van de twee het verschil veroorzaakt. Een controleproef helpt om dat nog duidelijker te zien.",
    ),
]

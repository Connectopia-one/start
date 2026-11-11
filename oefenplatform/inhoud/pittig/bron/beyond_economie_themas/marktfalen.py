"""Marktmacht, marktfalen, externe effecten en publieke goederen — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone, pix_zone, s_tekst, s_vak, GROEN, LICHT

G = venster("marktfalen-extern-effect", 0, 90, 0, 100, 10, 10)
PUNTEN = {"M": (40, 50), "O": (30, 60)}

# Prent 2: kruistabel rivaliserend / uitsluitbaar (eigen tekening, vakken leeg).
K_X0, K_Y0, K_B, K_H = 380, 200, 270, 170


def _kruistabel():
    d = [s_tekst(K_X0 + K_B, 125, "Rivaliserend?", 23, kleur=GROEN, vet=True),
         s_tekst(170, K_Y0 + K_H + 8, "Uitsluitbaar?", 23, kleur=GROEN, vet=True)]
    for j, k in enumerate(["ja", "nee"]):
        x = K_X0 + j * K_B
        d.append(s_vak(x, K_Y0 - 50, K_B, 50, vul=LICHT, rand=GROEN))
        d.append(s_tekst(x + K_B / 2, K_Y0 - 18, k, 22, vet=True))
    for i, k in enumerate(["ja", "nee"]):
        y = K_Y0 + i * K_H
        d.append(s_vak(K_X0 - 100, y, 100, K_H, vul=LICHT, rand=GROEN))
        d.append(s_tekst(K_X0 - 50, y + K_H / 2 + 8, k, 22, vet=True))
        for j in range(2):
            d.append(s_vak(K_X0 + j * K_B, y, K_B, K_H, vul="#fffdf7", rand=GROEN))
    return d


def vak(i, j):
    return pix_zone(K_X0 + j * K_B + 4, K_Y0 + i * K_H + 4, K_B - 8, K_H - 8)


GRAFIEKEN = [
    dict(naam=G, titel="Een vervuilende fabriek: privékost en maatschappelijke kost",
         krommen=[(lambda q: 90 - q, "groen", "V", (0, 82)), (lambda q: 10 + q, "blauw", "privékost", (0, 80)),
                  (lambda q: 30 + q, "oranje", "maatschappelijke kost", (0, 64))],
         labelplek={"V": (80, 10), "privékost": (78, 80), "maatschappelijke kost": (33, 88)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="hoeveelheid", ylabel="prijs, kosten", ijk_x=10, ijk_y=10),
    dict(naam="marktfalen-soorten-goederen", titel="Soorten goederen", eigen=_kruistabel),
]

PRENTEN = [
    dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over een negatief extern effect"),
    dict(bestand="marktfalen-soorten-goederen.svg", zelf=True, wat="Lege kruistabel rivaliserend / uitsluitbaar", vragen="klikvragen over private en publieke goederen"),
]
P = f"{G}.svg"
PK = "marktfalen-soorten-goederen.svg"

VRAGEN = [
    klik(
        "Klik op het punt waar de vrije markt uitkomt.",
        P, [punt_zone(G, *PUNTEN["M"])],
        "De producent kijkt enkel naar zijn eigen kosten. De markt komt uit waar de vraag de privékost snijdt: punt M.",
    ),
    klik(
        "Klik op het maatschappelijk optimum.",
        P, [punt_zone(G, *PUNTEN["O"])],
        "In het optimum is ook de schade aan derden meegeteld: de vraag snijdt de maatschappelijke kost in punt O.",
    ),
    klik(
        "Klik in het gebied dat het welvaartsverlies door de vervuiling voorstelt.",
        P, [vak_zone(G, 35, 39, 56, 64)],
        "Het welvaartsverlies is de driehoek voorbij het maatschappelijk optimum, tussen vraag en maatschappelijke kost, van Q = 30 tot Q = 40.",
    ),
    met_prent(P, inv(
        "Hoeveel euro schade aan derden veroorzaakt elk stuk? Lees af. Schrijf enkel het getal.",
        "20",
        "De maatschappelijke kost ligt overal 20 boven de privékost: 30 + Q tegenover 10 + Q.",
    )),
    met_prent(P, mk(
        "De overheid wil met een Pigouviaanse heffing het maatschappelijk optimum bereiken. Hoe groot moet de heffing per stuk zijn?",
        ["20 euro", "10 euro", "50 euro", "60 euro"],
        0,
        "Een Pigouviaanse heffing is gelijk aan de schade aan derden per stuk: 20 euro.",
    )),
    met_prent(P, inv(
        "Bereken het welvaartsverlies op de vrije markt. Schrijf enkel het getal.",
        "100",
        "½ · (40 − 30) · 20 = 100.",
    )),
    met_prent(P, tabel(
        "Is het op de vrije markt hoger of lager dan in het maatschappelijk optimum?",
        [
            ("De prijs", "Lager"),
            ("De verhandelde hoeveelheid", "Hoger"),
            ("De totale welvaart", "Lager"),
        ],
        "Op de vrije markt is de prijs 50 en de hoeveelheid 40. Het optimum ligt bij prijs 60 en hoeveelheid 30.",
        kolommen=["Hoger", "Lager"],
    )),
    klik(
        "Klik op het vak waar een zuiver publiek goed, zoals straatverlichting, hoort.",
        PK, [vak(1, 1)],
        "Straatverlichting is niet-rivaliserend en niet-uitsluitbaar: rechtsonder.",
    ),
    klik(
        "Klik op het vak waar een privaat goed, zoals een broodje, hoort.",
        PK, [vak(0, 0)],
        "Een broodje is rivaliserend (wat jij opeet, kan ik niet meer eten) en uitsluitbaar (wie niet betaalt, krijgt het niet): linksboven.",
    ),
    tabel(
        "Gaat het om een negatief of een positief extern effect?",
        [
            ("Een fabriek die de lucht vervuilt", "Negatief"),
            ("De bijen van een imker bestuiven ook de fruitbomen van de buren", "Positief"),
            ("Een vaccin beschermt ook wie zich niet liet vaccineren", "Positief"),
            ("Lawaai van een fabriek houdt de buren uit hun slaap", "Negatief"),
        ],
        "Schade aan derden die niet in de prijs zit: negatief. Voordeel voor derden dat niet in de prijs zit: positief.",
        kolommen=["Negatief", "Positief"],
    ),
    tabel(
        "Produceert de vrije markt hier te veel of te weinig?",
        [
            ("Een goed met een negatief extern effect", "Te veel"),
            ("Een goed met een positief extern effect", "Te weinig"),
            ("Een zuiver publiek goed", "Te weinig"),
            ("Een goed van een monopolist", "Te weinig"),
        ],
        "Bij een negatief effect is de prijs te laag, dus te veel. Positieve effecten, publieke goederen en marktmacht geven te weinig.",
        kolommen=["Te veel", "Te weinig"],
    ),
    sorteer(
        "Is deze overheidsmaatregel vooral bedoeld voor negatieve of voor positieve externe effecten?",
        ["Negatief extern effect", "Positief extern effect"],
        [
            ["Een Pigouviaanse heffing", "Negatief extern effect"],
            ["Emissierechten", "Negatief extern effect"],
            ["Een uitstootnorm voor nieuwe auto's", "Negatief extern effect"],
            ["Een subsidie", "Positief extern effect"],
            ["Iets gratis aanbieden", "Positief extern effect"],
        ],
        "Wie schade veroorzaakt, laat je betalen of beperk je. Wat voordeel geeft, moedig je aan.",
    ),
    mk(
        "Hoe zorgt emissiehandel ervoor dat de uitstoot daalt waar dat het goedkoopst kan?",
        ["Wie goedkoop minder kan uitstoten, verkoopt zijn rechten aan wie dat duur vindt",
         "De overheid bepaalt per bedrijf hoeveel het moet besparen, ongeacht de kosten",
         "Elk bedrijf krijgt evenveel rechten en mag ze niet doorverkopen aan een ander",
         "Bedrijven betalen een vaste boete per ton uitstoot, ongeacht hoeveel ze uitstoten"],
        0,
        "Het aantal rechten is beperkt. Wie goedkoop kan besparen, doet dat en verkoopt zijn rechten.",
    ),
    mk(
        "Een verkoper van een tweedehandsauto kent de gebreken, de koper niet. Wat kan daardoor gebeuren?",
        ["Kopers willen niet veel betalen, waardoor goede auto's van de markt verdwijnen",
         "Kopers betalen te veel, waardoor er te veel tweedehandsauto's verkocht worden",
         "De prijs van nieuwe auto's daalt, omdat niemand nog tweedehands wil kopen",
         "Er ontstaat een monopolie, omdat er maar één verkoper overblijft"],
        0,
        "Bij asymmetrische informatie durven kopers niet veel te betalen. Wie een goede auto heeft, verkoopt dan niet meer.",
    ),
    sorteer(
        "Tegen welk probleem helpt deze maatregel vooral?",
        ["Asymmetrische informatie", "Negatief extern effect"],
        [
            ["Een verplichte autokeuring", "Asymmetrische informatie"],
            ["Een etiket met de ingrediënten", "Asymmetrische informatie"],
            ["Een wettelijke garantie", "Asymmetrische informatie"],
            ["Een heffing op uitstoot", "Negatief extern effect"],
        ],
        "Etiketten, keuringen en garanties geven de koper meer informatie.",
    ),
    mk(
        "Waarom biedt de vrije markt een zuiver publiek goed zoals een dijk niet of te weinig aan?",
        ["Niemand kan verplicht worden te betalen, dus mensen liften mee",
         "Een dijk is rivaliserend: als de ene buurman beschermd is, de andere niet",
         "Er is te weinig vraag naar bescherming tegen overstromingen",
         "Bedrijven mogen wettelijk geen dijken bouwen"],
        0,
        "Wie niet betaalt, kan je niet uitsluiten van de bescherming. Daarom zorgt de overheid ervoor, met belastingen.",
    ),
    keuze(
        "Onderwijs is een [[*quasipubliek|zuiver publiek]] goed: het is [[*deels|helemaal niet]] rivaliserend en uitsluitbaar.",
        "Onderwijs zit tussen een privaat en een zuiver publiek goed in.",
    ),
    sleep(
        "Iemand die een publiek goed [[gebruikt]] zonder te [[betalen]], heet een [[meelifter]].",
        ["investeerder", "verkopen", "monopolist"],
        "In het Engels: een free rider.",
    ),
    mk(
        "Waarom geeft de overheid een patent aan een uitvinder, ook al vermindert dat de concurrentie?",
        ["Om uitvinders tijdelijk te belonen voor hun uitvinding",
         "Om de prijs van de uitvinding zo laag mogelijk te houden",
         "Om zoveel mogelijk bedrijven de uitvinding te laten namaken",
         "Om een negatief extern effect van de uitvinding te belasten"],
        0,
        "Een patent geeft tijdelijke marktmacht als beloning. Dat geeft net minder concurrentie op die markt.",
    ),
    tabel(
        "Waar of niet waar over het mededingingsbeleid?",
        [
            ("Een groot marktaandeel is op zich verboden in de EU.", F),
            ("Misbruik van een dominante positie is verboden.", J),
            ("De Belgische Mededingingsautoriteit kan boetes opleggen voor prijsafspraken.", J),
            ("Het antitrustbeleid van de EU wordt uitgevoerd door het Europees Parlement.", F),
        ],
        "Niet het marktaandeel, wel het misbruik is verboden. De Europese Commissie voert het antitrustbeleid uit.",
    ),
    koppel(
        "Koppel elke instelling aan haar taak.",
        [
            ["Belgische Mededingingsautoriteit", "Spoort kartels en machtsmisbruik op en legt boetes op"],
            ["Dienst voor Mededinging (FOD Economie)", "Bewaakt eerlijke concurrentie in België"],
            ["Europese Commissie", "Voert het antitrustbeleid van de EU uit"],
        ],
        ["Bepaalt de rentevoet in de eurozone"],
        "De rentevoet in de eurozone bepaalt de Europese Centrale Bank, niet een mededingingsinstelling.",
    ),
    tabel(
        "Is dit een oorzaak van marktfalen?",
        [
            ("Marktmacht", "Wel"),
            ("Asymmetrische informatie", "Wel"),
            ("Publieke goederen", "Wel"),
            ("Volkomen concurrentie zonder externe effecten", "Niet"),
        ],
        "Volkomen concurrentie zonder externe effecten leidt net tot de grootste welvaart.",
        kolommen=["Wel", "Niet"],
    ),
    mk(
        "Wat bedoelen we met een collectieve behoefte?",
        ["Een behoefte die je best samen invult, zoals veiligheid", "Een behoefte die enkel rijke mensen hebben",
         "Een behoefte die een bedrijf voor zijn werknemers invult", "Een behoefte die verdwijnt als het inkomen stijgt"],
        0,
        "Veiligheid vul je best samen in. Daarom zorgt de overheid ervoor, betaald met belastingen.",
    ),
    mk(
        "Een Pigouviaanse heffing wordt ingevoerd op een vervuilend product. Wat gebeurt er?",
        ["De prijs stijgt en de hoeveelheid daalt, tot het maatschappelijk optimum",
         "De prijs daalt en de hoeveelheid stijgt, want de producent krijgt geld van de overheid",
         "De prijs en de hoeveelheid blijven gelijk, maar de overheid krijgt extra ontvangsten",
         "De productie stopt volledig, want elke vervuiling is verboden"],
        0,
        "De heffing laat de producent de schade aan derden mee betalen. Zo verkleint het welvaartsverlies.",
    ),
    open_(
        "Een chemisch bedrijf loost afvalwater in een rivier, waardoor vissers verderop minder vangen. Leg uit waarom de vrije markt hier te veel produceert en wat de overheid kan doen.",
        "De schade aan de vissers zit niet in de kosten en dus niet in de prijs van het bedrijf. De maatschappelijke kost is hoger dan de privékost, de prijs is te laag en er wordt te veel geproduceerd. De overheid kan een Pigouviaanse heffing gelijk aan de schade per stuk opleggen, een norm voor het afvalwater invoeren of met rechten werken.",
    ),
    mk(
        "Wanneer spreken we van marktfalen?",
        ["Als de vrije markt niet tot de grootste welvaart leidt", "Als een bedrijf failliet gaat en zijn werknemers ontslaat",
         "Als de prijzen op een markt plots sterk dalen", "Als de overheid een maximumprijs oplegt"],
        0,
        "Marktfalen: de markt alleen brengt niet de grootste welvaart.",
    ),
    mk(
        "Bij een negatief extern effect: hoe verhouden de maatschappelijke kost en de privékost zich?",
        ["De maatschappelijke kost is hoger dan de privékost", "De privékost is hoger dan de maatschappelijke kost",
         "Ze zijn altijd even groot", "De maatschappelijke kost is nul"],
        0,
        "De maatschappelijke kost is de privékost plus de schade aan derden.",
    ),
    tabel(
        "Is dit een privaat goed of een zuiver publiek goed?",
        [
            ("Landsverdediging", "Zuiver publiek goed"),
            ("Een pizza", "Privaat goed"),
            ("Een dijk die een stad beschermt", "Zuiver publiek goed"),
            ("Een nieuwe fiets", "Privaat goed"),
        ],
        "Landsverdediging en een dijk beschermen iedereen tegelijk, en wie niet betaalt, kan je niet uitsluiten.",
        kolommen=["Privaat goed", "Zuiver publiek goed"],
    ),
    inv(
        "Elk stuk van een product veroorzaakt 4 euro schade aan derden. Hoeveel euro per stuk moet een Pigouviaanse heffing bedragen? Schrijf enkel het getal.",
        "4",
        "De heffing is gelijk aan de schade aan derden per stuk.",
    ),
    mk(
        "Wat bedoelen we met niet-rivaliserend?",
        ["Als ik het gebruik, kan jij het nog evengoed gebruiken", "Wie niet betaalt, kan je niet tegenhouden van het gebruik",
         "Er is maar één aanbieder van het goed op de hele markt", "Het goed kost niets om te maken voor de producent"],
        0,
        "Niet-uitsluitbaar is iets anders: dan kan je wie niet betaalt niet tegenhouden.",
    ),
]

"""De onderzoekscyclus van oriënteren tot rapporteren — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
grafiek uit een verzonnen leerlingenonderzoek, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Resultaat van een verzonnen enquête -----------------------------------------------------
GR = Prent("enquete-vervoer", "Hoe komen de 200 leerlingen van een school naar school? (enquête, oktober)", "een staafdiagram met vier staven: fiets 45 %, bus 30 %, auto 15 %, te voet 10 %; de verticale as is percentage leerlingen, de horizontale as is vervoermiddel")
L0, R0, T0, B0 = 160, 900, 110, 520


def X(i):
    return L0 + (R0 - L0) * i / 4


def Y(w):
    return B0 - (B0 - T0) * w / 50


GR.lijn(L0, B0, R0, B0, DONKER, 3)
GR.lijn(L0, B0, L0, T0 - 20, DONKER, 3)
for w in range(0, 51, 10):
    GR.lijn(L0, Y(w), R0, Y(w), "#ecebe6", 1)
    GR.tekst(L0 - 12, Y(w) + 6, str(w), 16, "end")
GR.tekst(L0 - 10, T0 - 35, "% leerlingen", 18, "start")
GR.tekst((L0 + R0) / 2, 600, "vervoermiddel", 18)
DATA = [("fiets", 45), ("bus", 30), ("auto", 15), ("te voet", 10)]
for i, (naam, w) in enumerate(DATA):
    x = X(i + 0.5)
    GR.rect(x - 55, Y(w), 110, Y(0) - Y(w), "#c4d5b5", DONKER, 0, 2)
    GR.tekst(x, Y(w) - 10, f"{w} %", 18)
    GR.tekst(x, B0 + 30, naam, 20)


def staaf(i):
    x = X(i + 0.5)
    return [Prent.zone(x - 65, Y(50), 130, Y(0) - Y(50))]


VRAGEN = [
    klik("Klik op de staaf van het vervoermiddel dat de meeste leerlingen gebruiken.", GR.bestand, staaf(0),
         "De fiets: 45 procent."),
    met_prent(GR.bestand, inv("Hoeveel van de 200 leerlingen komen met de bus? Schrijf het getal.", ["60"],
              "30 procent van 200 is 60.")),
    met_prent(GR.bestand, tabel("Welke conclusie blijft binnen deze gegevens?", [
        ("Bijna de helft van de leerlingen van deze school komt met de fiets.", J),
        ("In heel Vlaanderen fietsen de meeste jongeren naar school.", F),
        ("Leerlingen die met de auto komen, zijn luier.", F),
        ("Minder dan een op de vijf leerlingen komt met de auto.", J),
    ], "Een conclusie blijft binnen de gegevens: één school, en niets over karakter.")),
    met_prent(GR.bestand, keuze("Dit is [[*kwantitatief|kwalitatief]] onderzoek, want het telt hoeveel leerlingen iets doen.",
              "Kwantitatief zoekt aantallen.")),
    met_prent(GR.bestand, mk("Waarom koos de onderzoeker hier een grafiek in plaats van een tabel?",
              ["het verschil is meteen zichtbaar",
               "een grafiek bevat meer getallen dan een tabel",
               "een tabel mag niet in een verslag staan",
               "een grafiek heeft nooit een titel nodig"], 0,
              "Een grafiek toont snel een verloop of een verschil.")),
    met_prent(GR.bestand, keuze("Bij deze grafiek staan een titel en een naam bij [[*elke as|geen enkele as|enkel de staven]], zoals het hoort.",
              "Zonder titel en asnamen weet een lezer niet wat hij ziet.")),
    volgorde("Zet de fasen van de onderzoekscyclus in de juiste volgorde.", [
        "oriënteren",
        "voorbereiden",
        "uitvoeren",
        "rapporteren",
    ], "Pas als de vraag staat, mag je aan de methode beginnen."),
    tabel("Welk criterium haalt deze onderzoeksvraag NIET?", [
        ("Fietsen veel leerlingen naar school?", "open"),
        ("Waarom is het slechte busaanbod zo nadelig voor leerlingen?", "objectief"),
        ("Hoe komen leerlingen naar school en wat eten ze 's middags?", "enkelvoudig"),
        ("Hoeveel inwoners telt Hasselt?", "onderzoekbaar"),
    ], "Ja of nee, een verborgen mening, twee vragen in één, of een opzoekvraag.",
       kolommen=["open", "objectief", "enkelvoudig", "onderzoekbaar"]),
    sorteer("Desk- of fieldresearch?", ["Deskresearch", "Fieldresearch"], [
        ["cijfers van het statistiekbureau opzoeken", "Deskresearch"],
        ["leerlingen interviewen aan de schoolpoort", "Fieldresearch"],
        ["een wetenschappelijk artikel lezen", "Deskresearch"],
        ["een enquête afnemen in de klas", "Fieldresearch"],
    ], "Bestaande gegevens of zelf gegevens ophalen."),
    tabel("Kwalitatief of kwantitatief?", [
        ("Hoeveel jongeren in Limburg nemen dagelijks de bus?", "kwantitatief"),
        ("Hoe beleven leerlingen hun eerste week in het middelbaar?", "kwalitatief"),
        ("Welk percentage ouders werkt deeltijds?", "kwantitatief"),
    ], "Aantallen of diepte.", kolommen=["kwalitatief", "kwantitatief"]),
    tabel("In welke fase zit de onderzoeker?", [
        ("Hij formuleert een hypothese.", "oriënteren"),
        ("Hij kiest zijn bronnen en maakt een planning.", "voorbereiden"),
        ("Hij selecteert de bruikbare antwoorden en analyseert ze.", "uitvoeren"),
        ("Hij schrijft wat hij besluit en wat beter kon.", "rapporteren"),
    ], "Vier fasen, elk met hun eigen werk.", kolommen=["oriënteren", "voorbereiden", "uitvoeren", "rapporteren"]),
    casus(
        "Lotte onderzoekt: 'Hoe beïnvloedt het aantal uren schermtijd de slaap van leerlingen van het vierde jaar?' "
        "Ze neemt een enquête af bij twaalf leerlingen van haar eigen klas. Haar conclusie: 'Schermtijd maakt alle "
        "jongeren in Vlaanderen slaperig.'",
        [
            mk("Wat is het grootste probleem met haar conclusie?",
               ["ze gaat verder dan de gegevens",
                "de vraag is niet open genoeg",
                "ze had beter een grafiek gemaakt",
                "het onderwerp is niet relevant"], 0,
               "Twaalf leerlingen zeggen iets over die twaalf, niet over heel Vlaanderen."),
            keuze("Haar onderzoeksvraag is [[*open|gesloten]], want je kan er niet met ja of nee op antwoorden.",
                  "Ze begint met hoe."),
            tabel("Wat kan Lotte in haar reflectie zeggen?", [
                ("De groep was te klein en enkel uit haar eigen klas.", J),
                ("Haar resultaat bewijst iets voor alle jongeren.", F),
                ("Een grotere en meer verspreide steekproef zou sterker zijn.", J),
            ], "Wie zelf zegt waar zijn onderzoek zwak staat, maakt het sterker."),
        ],
    ),
    keuze("Een hypothese is [[*een verwachting die je nog gaat toetsen|hetzelfde als een onderzoeksvraag|het besluit van je onderzoek]].",
          "Een onderzoeksvraag is een vraag, een hypothese een verwachting."),
    tabel("Waarop let je bij de betrouwbaarheid van een bron?", [
        ("wie de bron maakte", J),
        ("met welk belang ze gemaakt werd", J),
        ("hoe mooi de opmaak is", F),
        ("hoe recent ze is", J),
    ], "Auteur, belang, datum en methode."),
    koppel("Koppel elk criterium van een onderzoeksvraag aan zijn betekenis.", [
        ["enkelvoudig", "over één onderwerp"],
        ["objectief", "verraadt geen mening"],
        ["haalbaar", "uitvoerbaar met je tijd en middelen"],
        ["relevant", "draagt bij aan de bestaande kennis"],
    ], ["kan met ja of nee beantwoord worden"], "Vier van de zes criteria."),
    keuze("Een onverwacht resultaat is [[*geen mislukking: je noteert wat het beïnvloed heeft|een reden om het onderzoek te verzwijgen|altijd een rekenfout]].",
          "Ook dat hoort in de rapportering."),
    inv("Hoeveel criteria van een goede onderzoeksvraag zijn er? Schrijf het getal.", ["6", "zes"],
        "Open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant."),
    sleep("Bij [[deskresearch]] gebruik je gegevens die al bestaan. Bij [[fieldresearch]] haal je zelf gegevens op.",
          ["kwalitatief", "rapporteren"], "Bureau of veld."),
    keuze("In de fase rapporteren horen het resultaat, het besluit en [[*een terugblik op het verloop|een nieuwe hypothese|de keuze van de methode]].",
          "Drie dingen bij rapporteren."),
    mk("Je krijgt drie conclusies bij één onderzoek. Wat doe je?",
       ["de meest volledige kiezen en uitleggen",
        "de kortste kiezen, want die is duidelijk",
        "de conclusie kiezen die het meest verrast",
        "alle drie samen overnemen in je verslag"], 0,
       "Kies de meest volledige en verantwoord je keuze."),
    klik("Klik op de staaf die precies een derde zo groot is als die van de fiets.", GR.bestand, staaf(2),
         "45 gedeeld door 3 is 15: de auto."),
    met_prent(GR.bestand, inv("Hoeveel procentpunt meer leerlingen fietsen dan er met de bus komen? Schrijf het getal.", ["15"],
              "45 min 30 is 15.")),
    keuze("Een enquête bij duizend mensen is [[*kwantitatief|kwalitatief]] fieldresearch.",
          "Veel mensen, aantallen."),
    mk("Welke vraag haalt het criterium haalbaar het minst?",
       ["Hoe denken alle jongeren ter wereld over school?",
        "Hoe beleven leerlingen van onze school de speeltijd?",
        "Hoeveel leerlingen van onze klas eten 's middags warm?",
        "Hoe komen leerlingen van onze school naar school?"], 0,
       "Alle jongeren ter wereld bevragen kan een leerling niet."),
    keuze("De zes criteria van een goede onderzoeksvraag krijg je [[*ook op het examen|nooit op het examen]], dus je moet ze vooral kunnen toepassen.",
          "Toepassen, niet opsommen."),
    tabel("Hoort dit in de fase voorbereiden?", [
        ("je methode kiezen", J),
        ("de gegevens analyseren", F),
        ("een planning maken", J),
    ], "Analyseren hoort bij uitvoeren."),
    keuze("Een goede conclusie geeft [[*een antwoord op de onderzoeksvraag|een nieuwe vraag|een mening van de onderzoeker]], uit de gegevens zelf.",
          "Ze blijft binnen de gegevens."),
    open_("Bedenk een goede onderzoeksvraag over sociale media en slaap bij jongeren. Toon met drie criteria waarom ze goed is en kies een passende methode.",
          "Bijvoorbeeld: 'Hoe hangt het gebruik van sociale media na 22 uur samen met de slaapduur van leerlingen van de derde graad in onze school?' Open: begint met hoe. Enkelvoudig: één onderwerp. Objectief: geen mening in de vraag. Methode: kwantitatief fieldresearch met een enquête bij een grote groep leerlingen."),
]

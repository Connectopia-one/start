"""Wat bepaalt onze gezondheid — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_determinanten: het model van Lalonde met vier
gezondheidsdeterminanten en het gedragswiel met competenties, drijfveren en
context. Met een zelfgetekende prent met vier voorbeelden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, GEEL, BLAUW, ORANJE

LA = Prent("vier-voorbeelden-gezondheid", "Wat speelt mee voor de gezondheid van Ann?", "vier kaders rond een cirkel, elk met een voorbeeld, letters A tot D")
LA.cirkel(500, 335, 80, GEEL, DONKER, 3)
LA.tekst(500, 330, "de gezondheid", 18, vet=True); LA.tekst(500, 354, "van Ann", 18, vet=True)
KADER = {"A": (60, 80, ["Haar ouders hadden allebei", "een hoge bloeddruk."]),
         "B": (580, 80, ["Ann woont naast een", "drukke autosnelweg."]),
         "C": (60, 450, ["Ann rookt elke dag", "een pakje sigaretten."]),
         "D": (580, 450, ["De dichtstbijzijnde huisarts", "is dertig kilometer ver."])}
Z = {}
for t, (x, y, regels) in KADER.items():
    LA.rect(x, y, 360, 120, "#ffffff", DONKER, 14, 2)
    LA.tekst(x + 195, y + 55, regels[0], 20); LA.tekst(x + 195, y + 85, regels[1], 20)
    LA.letter(x + 28, y + 30, t)
    LA.lijn(x + 180 + (0 if x < 500 else 0), y + (120 if y < 300 else 0), 500 + (-60 if x < 500 else 60), 335 + (-50 if y < 300 else 50), DONKER, 2)
    Z[t] = [Prent.zone(x, y, 360, 120)]
U = "vier-voorbeelden-gezondheid.svg"

SITUATIE = ("Lees de situatie.\n\n"
            "Yusuf (45) wil gezonder eten, want zijn dokter waarschuwde hem voor zijn cholesterol. Hij wil het echt. "
            "Maar hij kookt nooit en weet niet hoe je groenten klaarmaakt. In zijn wijk is er enkel een nachtwinkel en een frituur.")

VRAGEN = [
    klik("Bekijk de prent. Klik op het voorbeeld van een biologische factor.", U, Z["A"], "Erfelijkheid zit in je lichaam: een biologische factor."),
    klik("Klik op het voorbeeld van de omgeving.", U, Z["B"], "Lawaai en vuile lucht van een snelweg komen van buiten je lichaam."),
    klik("Klik op het voorbeeld van de voorzieningen van de gezondheidszorg.", U, Z["D"], "Hoe ver de zorg is, hoort bij de voorzieningen."),
    klik("Klik op het voorbeeld waar Ann zelf het meest aan kan veranderen.", U, Z["C"], "Roken is leefstijl, en daar heb je zelf de meeste greep op."),
    casus(SITUATIE, [
        keuze("Dat Yusuf niet weet hoe hij groenten klaarmaakt, gaat over zijn [[*competenties|drijfveren|context]].", "Kennis en vaardigheden zijn competenties."),
        keuze("Enkel een nachtwinkel en een frituur in de wijk is een probleem in de [[*context|competenties|drijfveren]].", "Het aanbod in de buurt hoort bij de context."),
        keuze("Dat hij het echt wil na de waarschuwing van de dokter, is een sterke [[*drijfveer|competentie|context]].", "Motivatie is een drijfveer."),
        mk("Wat helpt Yusuf het meest om zijn gedrag echt te veranderen?",
           ["een kookles én een groentepakket aan huis", "nog een strengere waarschuwing van zijn dokter", "een folder over het belang van gezond eten", "een nieuwe frituur met een groter menu"],
           0, "Hij wil al; wat hij nog mist zijn de competentie en de context. Pak je ze samen aan, dan houdt het."),
    ]),
    tabel("Welke determinant van Lalonde?",
          [("je geslacht", "biologie"), ("fijn stof in de lucht", "omgeving"), ("elke dag fietsen naar je werk", "leefstijl"), ("de wachttijd bij een specialist", "voorzieningen"), ("een erfelijke ziekte in de familie", "biologie")],
          "Biologische factoren, omgeving, leefstijl en de voorzieningen van de gezondheidszorg.", ["biologie", "omgeving", "leefstijl", "voorzieningen"]),
    sorteer("Competentie, drijfveer of context?", ["competentie", "drijfveer", "context"],
            [("weten hoeveel water je per dag nodig hebt", "competentie"), ("zin hebben om te gaan zwemmen", "drijfveer"), ("de prijs van een zwembadbeurt", "context"), ("kunnen fietsen", "competentie"), ("de gewoonte om elke avond chips te eten", "drijfveer"), ("vrienden die allemaal roken", "context")],
            "Kunnen en kennen, willen en voelen, alles om je heen."),
    mk("Een gemeente legt een veilig fietspad aan. Op welke determinant van Lalonde werkt ze?",
       ["de omgeving", "de biologische factoren", "de erfelijkheid van de inwoners", "de voorzieningen van de gezondheidszorg"],
       0, "De overheid werkt vooral aan de omgeving en de voorzieningen."),
    tabel("Kan je dit zelf veranderen?",
          [("je leeftijd", F), ("hoeveel je beweegt", J), ("je erfelijkheid", F), ("of je rookt", J)],
          "Biologische factoren liggen vast; je leefstijl kan je zelf sturen."),
    keuze("Er komt een nieuw wijkgezondheidscentrum. Dat verandert de [[*voorzieningen van de gezondheidszorg|biologische factoren|leefstijl]].", "Artsen en zorg in de buurt horen bij de voorzieningen."),
    inv("Welke determinant van het gedragswiel gaat over je motivatie, je gewoonten en je gevoelens? Eén woord.", ["drijfveren", "drijfveer", "de drijfveren"], "De drijfveren."),
    tabel("Wat ontbreekt er?",
          [("Sara wil stoppen met roken en weet hoe, maar al haar vrienden roken.", "context"), ("Tom heeft een zwembad om de hoek en wil zwemmen, maar kan het niet.", "competenties"), ("Ines kan koken en heeft een volle koelkast, maar bestelt liever pizza.", "drijfveren")],
          "Zoek wat er niet is: kunnen, willen of de omgeving.", ["competenties", "drijfveren", "context"]),
    koppel("Koppel het model aan wat het laat zien.",
           [("het model van Lalonde", "wat de gezondheid van mensen bepaalt"), ("het gedragswiel", "waarom iemand iets wel of niet doet"), ("de geluksdriehoek", "waaraan je kan werken om je beter te voelen")],
           ["hoe snel een kind groeit"],
           "Elk model kijkt naar iets anders."),
    keuze("Volgens Lalonde is gezondheid [[*niet enkel een eigen keuze|enkel een kwestie van leefstijl|enkel erfelijk bepaald]].", "Vier determinanten spelen mee."),
    tabel("Klopt dit over het gedragswiel?",
          [("Wie iets wil, zal het ook altijd doen.", F), ("Een gewoonte hoort bij de drijfveren.", J), ("Regels op school horen bij de context.", J), ("Kennis hoort bij de context.", F)],
          "Kennis is een competentie."),
    sorteer("Een school wil dat leerlingen meer water drinken. Op welke gedragsdeterminant werkt elke maatregel?", ["competenties", "drijfveren", "context"],
            [("gratis waterfonteinen in de gangen", "context"), ("een les over wat water doet in je lichaam", "competenties"), ("een wedstrijd tussen de klassen", "drijfveren"), ("frisdrank uit de automaat halen", "context"), ("een filmpje waarin leerlingen vertellen hoe fit ze zich voelen", "drijfveren")],
            "Wie alle drie aanpakt, heeft de meeste kans dat het gedrag blijft."),
    inv("Hoe heet de onderzoeker van het model met vier gezondheidsdeterminanten? Eén woord.", ["Lalonde"], "Lalonde."),
    mk("Een vrouw heeft door erfelijkheid meer kans op diabetes. Wat kan ze wel doen?",
       ["via haar leefstijl het risico verkleinen", "haar erfelijkheid laten aanpassen bij de huisarts", "niets, want erfelijkheid bepaalt alles", "verhuizen, want de omgeving bepaalt haar erfelijkheid"],
       0, "Erfelijkheid ligt vast, maar de andere determinanten kan je wel beïnvloeden."),
    keuze("Roken, slapen en bewegen zijn voorbeelden van [[*gezondheidsgedrag|biologische factoren|voorzieningen]].", "Het is gedrag met gevolgen voor je gezondheid."),
    mk("Welke uitspraak past bij het model van Lalonde?",
       ["gezondheid komt van vier kanten", "gezondheid hangt enkel af van hoeveel je sport", "gezondheid is iets wat alleen artsen bepalen", "gezondheid ligt helemaal vast bij je geboorte"],
       0, "Biologie, omgeving, leefstijl en voorzieningen."),
    tabel("Hoort dit bij de omgeving van Lalonde?",
          [("je woning", J), ("je bloedgroep", F), ("lawaai in je buurt", J), ("je werkplek", J), ("je eetgewoonten", F)],
          "Je bloedgroep is biologisch, je eetgewoonten zijn leefstijl."),
    keuze("Je bloedgroep is een [[*biologische factor|leefstijlkeuze|omgevingsfactor]].", "Hij zit in je lichaam en kan je niet veranderen."),
    mk("Wie kan het meest doen aan de voorzieningen van de gezondheidszorg?",
       ["de overheid en de zorgsector", "elke burger door meer te sporten", "je ouders via je erfelijkheid", "de supermarkt met zijn aanbiedingen"],
       0, "Ziekenhuizen, huisartsen en de prijs van zorg regel je niet alleen."),
    keuze("Haakt er één determinant van het gedragswiel, dan [[*houdt nieuw gedrag vaak niet|lukt het toch altijd|maakt dat niets uit]].", "Kunnen, willen en de omgeving moeten samen kloppen."),
    sleep("Het gedragswiel heeft drie determinanten: wat je kan en kent zijn je [[competenties]], wat je wil en voelt zijn je [[drijfveren]], en alles om je heen is de [[context]].",
          ["leefstijl", "erfelijkheid"],
          "Leefstijl en erfelijkheid horen bij Lalonde."),
    tabel("Leefstijl of biologische factor?",
          [("je leeftijd", "biologische factor"), ("hoeveel alcohol je drinkt", "leefstijl"), ("je geslacht", "biologische factor"), ("hoe laat je gaat slapen", "leefstijl")],
          "Leefstijl is wat je doet.", ["leefstijl", "biologische factor"]),
    open_("Kies een gezonde gewoonte die je zelf wil aanleren. Geef bij het gedragswiel telkens één ding: wat je moet kunnen, wat je moet willen en wat er in je omgeving moet zijn.",
          "Ik wil elke dag fietsen naar school. Kunnen: een band kunnen plakken. Willen: ik wil fitter worden voor mijn voetbal. Omgeving: een veilige fietsroute en een fietsenstalling op school."),
]

"""Ontwikkeling: groeien, rijpen en leren — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_ontwikkeling: groeien, rijpen en leren, de
negen levensloopfasen, nature, nurture en zelfbepaling, en de vijf
ontwikkelingsdomeinen. Met een zelfgetekende levenslijn."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ROOD, LICHTGROEN

LL = Prent("levenslijn", "Een levenslijn van 0 tot 90 jaar", "een lijn met leeftijden en letters A tot G")
def X(j):
    return 120 + j / 90 * 780
LL.rect(60, 300, 880, 40, "#eef3e6", DONKER, 20, 2)
LL.rect(60, 300, X(0) - 60, 40, "#f6e3c4", DONKER, 20, 2)
for j in (0, 10, 20, 30, 40, 50, 60, 70, 80, 90):
    LL.lijn(X(j), 340, X(j), 360, DONKER, 2); LL.tekst(X(j), 385, str(j), 18)
LL.tekst(500, 430, "leeftijd in jaren", 20)
PT = {"A": -3, "B": 2, "C": 5, "D": 9, "E": 15, "F": 45, "G": 78}
for t, j in PT.items():
    x = X(j) if j >= 0 else 88
    LL.cirkel(x, 320, 9, ROOD, DONKER, 2)
    LL.lijn(x, 310, x, 250 if t in "ACEG" else 200, DONKER, 1)
    LL.letter(x, 230 if t in "ACEG" else 180, t)
U = "levenslijn.svg"
Z = {t: [Prent.rond(X(j) if j >= 0 else 88, 230 if t in "ACEG" else 180, 34)] for t, j in PT.items()}

TWEELING = ("Lees het verhaal.\n\n"
            "Ella en Noor zijn een eeneiige tweeling. Ze hebben precies dezelfde genen. Ella groeit op bij haar ouders aan zee, "
            "Noor wordt opgevoed door haar tante in de stad. Op hun twintigste spreekt Ella vlot Frans, wat Noor niet kan. "
            "Noor speelt goed piano, omdat ze zelf koos om elke dag te oefenen. Allebei zijn ze even groot en hebben ze dezelfde bloedgroep.")

VRAGEN = [
    klik("Bekijk de levenslijn. Klik op de letter bij de fase waarin alle organen gevormd worden.", U, Z["A"], "De prenatale fase, nog vóór de geboorte."),
    klik("Klik op de letter bij de peutertijd, de fase van de koppigheid.", U, Z["B"], "Ongeveer één tot drie jaar."),
    klik("Klik op de letter bij de fase waarin je zoekt wie je zelf bent.", U, Z["E"], "De adolescentie."),
    klik("Klik op de letter bij de late volwassenheid.", U, Z["G"], "Vaak na het pensioen."),
    casus(TWEELING, [
        sorteer("Nature, nurture of zelfbepaling?", ["nature", "nurture", "zelfbepaling"],
                [("dezelfde bloedgroep", "nature"), ("Ella spreekt vlot Frans", "nurture"), ("Noor koos zelf om elke dag piano te oefenen", "zelfbepaling"), ("even groot", "nature")],
                "Genen, omgeving en wat je zelf kiest."),
        mk("Wat toont het verschil tussen Ella en Noor het duidelijkst?",
           ["het gewicht van de omgeving", "dat genen in hun leven helemaal niets betekenen", "dat een tweeling altijd volledig hetzelfde wordt", "dat de stad slimmere kinderen maakt dan de zee"],
           0, "Dezelfde genen en toch een ander resultaat."),
        keuze("Dat Noor zelf koos om te oefenen, betekent [[*niet|wel]] dat ze haar hele ontwikkeling vrij kiest.", "Je kiest binnen wat nature en nurture mogelijk maken."),
        tabel("Klopt dit over het verhaal?",
              [("Nature en nurture werken samen.", J), ("De genen bepalen alles.", F), ("Zelfbepaling is een derde factor.", J)],
              "Het is nooit het een of het ander."),
    ]),
    sorteer("Groeien, rijpen of leren?", ["groeien", "rijpen", "leren"],
            [("drie kilo bijkomen", "groeien"), ("de eerste tandjes krijgen", "rijpen"), ("leren zwemmen in het zwembad", "leren"), ("een grotere schoenmaat krijgen", "groeien"), ("eerst zitten, dan staan, dan stappen", "rijpen"), ("een gedicht van buiten leren", "leren")],
            "Groeien is meetbaar, rijpen gaat vanzelf, leren vraagt ervaring."),
    volgorde("Zet deze levensloopfasen in de juiste volgorde.",
             ["de babytijd", "de peutertijd", "de kleutertijd", "de lagereschoolkindfase", "de adolescentie", "de vroege volwassenheid"],
             "De fasen volgen elkaar in een vaste orde."),
    koppel("Koppel het ontwikkelingsdomein aan het voorbeeld.",
           [("fysiek", "een kind wordt tien centimeter groter"), ("cognitief", "een kind begrijpt dat een getal ook achteruit kan"), ("moreel", "een kind vindt stelen fout, ook als niemand het ziet"), ("socio-emotioneel", "een kind troost een vriendje dat huilt")],
           ["een kind krijgt een nieuwe fiets"], "Er is ook een vijfde domein: de persoonlijkheid."),
    mk("Een kind kan pas leren schrijven als de fijne motoriek gerijpt is. Wat toont dat?",
       ["rijpen en leren hebben elkaar nodig", "leren is veel belangrijker dan rijpen bij elk kind", "rijpen gaat altijd sneller als je meer oefent", "schrijven hoort enkel bij het groeien van de hand"],
       0, "Rijping alleen leert nog geen letters, en oefenen lukt niet zonder rijping."),
    tabel("Klopt dit over de levensloopfasen?",
          [("Er zijn negen fasen.", J), ("De grenzen liggen op een vaste verjaardag.", F), ("De volwassenheid is in drie verdeeld.", J), ("Ontwikkeling stopt bij de volwassenheid.", F)],
          "Daarom spreek je van de hele levensloop."),
    keuze("Een stap vooruit in het ene domein opent het andere. Dat heet de [[*wisselwerking|rijping|groeispurt]] tussen de domeinen.", "Wie kan stappen, kan meer ontdekken."),
    keuze("Een kind met een spraakachterstand krijgt logopedie en haalt de achterstand in. Hier werkt vooral [[*nurture|nature|rijping]].", "Hulp uit de omgeving."),
    tabel("Hoort dit bij nature?",
          [("de kleur van je ogen", J), ("de taal die thuis gesproken wordt", F), ("een erfelijke aandoening", J), ("de buurt waar je woont", F)],
          "Nature is wat je meekrijgt van je ouders."),
    mk("Lien kwam op tien jaar in de puberteit, haar vriendin op dertien. Wat toont dat over de levensloopfasen?",
       ["de grenzen verschuiven per persoon", "omdat leeftijden in de wetenschap niet meetellen", "omdat elke fase precies tien jaar duurt", "omdat de fasen in een willekeurige volgorde komen"],
       0, "De orde ligt vast, het moment niet."),
    sleep("Ontwikkeling bestaat uit [[groeien]], [[rijpen]] en [[leren]].",
          ["erven", "zitten"], "Die drie altijd samen."),
    keuze("De prenatale fase is de [[*kortste|langste]] fase, en toch gebeurt er dan het meest.", "Negen maanden."),
    inv("Hoe heet de fase tussen de kindertijd en de volwassenheid? Eén woord.", ["adolescentie", "de adolescentie"], "De fase van de identiteit."),
    sorteer("Welk ontwikkelingsdomein?", ["fysiek", "cognitief", "persoonlijkheid"],
            [("Een kind leert tellen tot twintig.", "cognitief"), ("Een tiener krijgt een groeispurt.", "fysiek"), ("Een jongere ontdekt wat hij echt belangrijk vindt in het leven.", "persoonlijkheid"), ("Een kleuter leert dat een bal rond blijft als hij hem niet ziet.", "cognitief")],
            "Vijf domeinen in wisselwerking."),
    mk("In welk domein gaat het in de late volwassenheid het duidelijkst achteruit?",
       ["het fysieke", "het cognitieve, want alles wat je weet verdwijnt", "het morele, want ouderen weten geen goed en kwaad meer", "het socio-emotionele, want ouderen hebben geen gevoelens meer"],
       0, "Kracht, zicht en gehoor nemen af; woordenschat blijft vaak."),
    keuze("Een jongen erft muzikaal talent maar oefent nooit. Zijn [[*nature|nurture]] is er dus wel, maar zonder oefening komt er niets van terecht.", "Talent alleen volstaat niet."),
    tabel("Is dit een van de vijf ontwikkelingsdomeinen?",
          [("fysiek", J), ("financieel", F), ("moreel", J), ("socio-emotioneel", J), ("cognitief", J)],
          "Fysiek, cognitief, moreel, socio-emotioneel en persoonlijkheid."),
    inv("Je kiest zelf om elke dag te trainen voor een loopwedstrijd. Welke ontwikkelingsfactor is dat? Eén woord.", ["zelfbepaling"], "Wat je zelf kiest, naast nature en nurture."),
    keuze("Het hoofd van een baby is in verhouding veel [[*groter|kleiner]] dan dat van een volwassene.", "De verhoudingen veranderen tijdens de groei."),
    tabel("Hoort dit bij de kindertijd?",
          [("de peutertijd", J), ("de kleutertijd", J), ("de lagereschoolkindfase", J), ("de adolescentie", F)],
          "Na de kindertijd komt de adolescentie."),
    mk("Waarom is het nuttig om de ontwikkelingsdomeinen apart te bekijken?",
       ["je kan gerichter helpen", "zo kan je elk kind een cijfer geven voor zijn ontwikkeling", "zo weet je meteen welke genen een kind heeft gekregen", "zo hoef je de wisselwerking niet meer te bekijken"],
       0, "Wie weet waar iets vastloopt, kan gerichter helpen."),
    keuze("Een kleuter en een adolescent vergelijken in hoe ze denken, is twee fasen vergelijken binnen het [[*cognitieve|fysieke|morele]] domein.", "Vergelijken binnen één domein."),
    open_("Leg met een eigen voorbeeld uit hoe twee ontwikkelingsdomeinen elkaar beïnvloeden.",
          "Bijvoorbeeld: een baby leert kruipen (fysiek). Daardoor kan hij zelf de kamer verkennen en ontdekt hij dat een bal achter de zetel nog bestaat (cognitief). Een stap in het ene domein opent het andere."),
]

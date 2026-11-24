"""Transport en logistiek — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_logistiek, met een zelfgetekende vereenvoudigde
vrachtbrief om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER

CM = Prent("vrachtbrief-cmr", "", "vereenvoudigde internationale vrachtbrief met zes vakken A tot F")
CM.rect(60, 20, 880, 600, "#ffffff", DONKER, 10, 3)
CM.rect(60, 20, 880, 60, LICHTGROEN, DONKER, 10, 3)
CM.tekst(500, 60, "Internationale vrachtbrief CMR nr. 2026-0417", 24, vet=True)
VAK = [
    ("A", 60, 80, 440, 150, ["Fietsen Trappers bv", "Industrieweg 12, Alken (België)"]),
    ("B", 500, 80, 440, 150, ["Vélo Plus", "Rue du Port 8, Lille (Frankrijk)"]),
    ("C", 60, 230, 880, 120, ["Transport Maes nv, Genk", "vrachtwagen 1-ABC-123"]),
    ("D", 60, 350, 440, 140, ["40 elektrische fietsen", "in 40 dozen"]),
    ("E", 500, 350, 440, 140, ["1 120 kg"]),
    ("F", 60, 490, 880, 130, ["ingeladen in Alken op 12/11/2026", "te leveren in Lille op 13/11/2026"]),
]
for t, x, y, b, h, regels in VAK:
    CM.rect(x, y, b, h, "none", DONKER, 0, 2)
    CM.letter(x + 36, y + 36, t)
    for i, r in enumerate(regels):
        CM.tekst(x + 74, y + 44 + i * 34, r, 21, "start")
U = "vrachtbrief-cmr.svg"
Z = {t: Prent.rond(x + 36, y + 36, 30) for t, x, y, b, h, _ in VAK}

VRAGEN = [
    klik("Klik op de letter bij de bestemmeling.", U, [Z["B"]],
         "Vélo Plus in Lille krijgt de fietsen: de bestemmeling."),
    klik("Klik op de letter bij de afzender.", U, [Z["A"]],
         "Fietsen Trappers in Alken verstuurt de fietsen."),
    klik("Klik op de letter bij de vervoerder.", U, [Z["C"]],
         "Transport Maes rijdt de vracht naar Lille."),
    klik("Klik op de letter bij het gewicht van de zending.", U, [Z["E"]],
         "Op een CMR staat ook het gewicht."),
    klik("Klik op de letter bij de aard van de goederen.", U, [Z["D"]],
         "Wat er vervoerd wordt: 40 elektrische fietsen."),
    casus("Bekijk de vrachtbrief van Fietsen Trappers.", [
        tabel("Klopt dit volgens de vrachtbrief?",
              [("Het gaat om internationaal wegvervoer.", J), ("De vrachtbrief zegt hoeveel de fietsen kosten.", F), ("Voor Fietsen Trappers is dit uitvoer.", J), ("De vrachtbrief moet door drie partijen getekend worden.", J)],
              "Een CMR regelt het vervoer, geen prijzen. Afzender, vervoerder en bestemmeling tekenen."),
        inv("Hoeveel kilogram weegt één doos met een fiets gemiddeld? Schrijf enkel het getal.", ["28"],
            "1 120 kg / 40 dozen = 28 kg."),
        keuze("Voor Frankrijk zijn deze fietsen [[*invoer|uitvoer|doorvoer]].",
              "Ze komen uit het buitenland het land binnen."),
    ]),
    tabel("Welke transportmodus past het best?",
          [("een dringend klein pakje naar Japan", "luchtvracht"), ("duizenden containers van China naar Antwerpen", "maritiem vervoer"), ("aardgas van de haven naar een fabriek", "pijpleiding"), ("vers fruit van Spanje naar een supermarkt in Hasselt", "wegvervoer")],
          "Je kiest op snelheid, kosten, capaciteit en de aard van het product.",
          kolommen=["wegvervoer", "maritiem vervoer", "luchtvracht", "pijpleiding"]),
    sorteer("Voordeel van welke transportmodus?", ["wegvervoer", "spoorvervoer", "luchtvracht", "maritiem vervoer"],
            [("tot aan de deur van de klant", "wegvervoer"), ("minder uitstoot per ton dan de vrachtwagen, over land", "spoorvervoer"), ("het snelst over grote afstand", "luchtvracht"), ("de grootste capaciteit", "maritiem vervoer")],
            "Elke modus heeft zijn sterke punt."),
    koppel("Welk nadeel hoort bij welke transportmodus?",
           [("wegvervoer", "files en meer uitstoot per ton"), ("luchtvracht", "duur per kilo"), ("maritiem vervoer", "het traagst"), ("pijpleiding", "enkel vloeistof of gas")],
           ["geen nadelen"], "Geen enkele modus is in alles de beste."),
    mk("Waarom gaat een container vaak per schip, dan per trein en ten slotte per vrachtwagen?",
       ["Elke modus doet het stuk dat hij het best kan.", "Een vrachtwagen mag niet over de grens rijden.", "Een trein kan geen containers dragen.", "Zo wordt het transport sneller dan met het vliegtuig."], 0,
       "Een schip en een trein stoppen bij een terminal; de laatste kilometers gaan over de weg."),
    keuze("Binnenscheepvaart vervoert goederen over [[*rivieren en kanalen|de oceaan|de lucht]] in het binnenland.",
          "Maritiem vervoer gaat over zee."),
    tabel("Invoer, uitvoer of doorvoer, gezien vanuit België?",
          [("Belgische chocolade gaat naar Canada.", "uitvoer"), ("Bananen uit Ecuador komen in Antwerpen toe voor Belgische winkels.", "invoer"), ("Nederlandse kaas rijdt via België naar Frankrijk zonder hier verkocht te worden.", "doorvoer")],
          "Doorvoer passeert enkel.",
          kolommen=["invoer", "uitvoer", "doorvoer"]),
    volgorde("Zet de taken in de loods bij een bestelling van een klant in de juiste volgorde.",
             ["de goederen ontvangen van de leverancier", "de goederen opslaan in de rekken", "de goederen van de order picken", "de zending verzenden met een pakbon"],
             "De goederenstroom van binnenkomen tot vertrekken."),
    tabel("Hoort dit bij de taken van expeditie en logistiek?",
          [("transport plannen", J), ("voorraad beheren", J), ("een retour afhandelen", J), ("de lonen uitbetalen", F)],
          "Lonen zijn werk voor HR en de boekhouding."),
    mk("Een webwinkel houdt van elk artikel tien keer te veel in voorraad. Wat is het probleem?",
       ["Voorraad kost plaats en geld en veroudert.", "Klanten kunnen dan helemaal niets meer bestellen.", "De vrachtwagens raken dan nooit meer helemaal vol.", "Er is dan bij een zending geen pakbon meer nodig."], 0,
       "Te veel voorraad is even slecht als te weinig."),
    keuze("Een te [[*kleine|grote]] voorraad kan een verkoop doen mislopen: wat je niet in huis hebt, kan je niet leveren.",
          "Voorraadbeheer is op tijd bijbestellen."),
    tabel("Pakbon of CMR?",
          [("een lijst van wat er in de zending zit", "pakbon"), ("de vervoersovereenkomst bij internationaal wegvervoer", "CMR"), ("getekend door afzender, vervoerder en bestemmeling", "CMR"), ("zodat de ontvanger nakijkt of alles er is", "pakbon")],
          "De pakbon zegt wat erin zit; de CMR regelt wie waarvoor aansprakelijk is.",
          kolommen=["pakbon", "CMR"]),
    inv("Een vrachtwagen mag 24 000 kg laden. Hoeveel pallets van 600 kg kan hij hoogstens meenemen? Schrijf enkel het getal.", ["40"],
        "24 000 / 600 = 40 pallets. Gewichten berekenen is een eenvoudige logistieke taak."),
    sleep("Het uit de rekken halen van de artikels van een order heet [[picken]]. Goederen die de klant terugstuurt, zijn een [[retour]].",
          ["doorvoer", "offerte"], "Twee taken in de loods."),
    mk("Waarom gaat er vooral lichte, dringende of kostbare vracht met het vliegtuig mee?",
       ["Luchtvracht is snel maar duur.", "Vliegtuigen mogen geen zware lading dragen.", "Luchtvracht stoot het minst uit van alle modi.", "Een vliegtuig levert tot aan de deur."], 0,
       "Je betaalt per kilo veel, maar het is in een dag ter plaatse."),
    tabel("Klopt dit over de transportmodi?",
          [("Spoorvervoer stoot per ton minder uit dan wegvervoer.", J), ("Maritiem vervoer is de snelste modus.", F), ("Elke modus kan tot aan de deur leveren.", F), ("Een pijpleiding werkt dag en nacht zonder chauffeur.", J)],
          "Een zeeschip is het traagst; enkel het wegvervoer geraakt tot aan de deur."),
    open_("Een onderneming in Genk moet elke week 500 ton zand naar Antwerpen sturen. Het is niet dringend. Welke transportmodus raad je aan, en waarom?",
          "Binnenscheepvaart via het Albertkanaal, of anders het spoor. Het gaat om een groot volume dat niet dringend is: per ton is dat goedkoop en het stoot minder uit dan honderden vrachtwagens.",
          "Je vergelijkt op snelheid, kosten, capaciteit en milieu."),
    keuze("Een CMR wordt ondertekend door de afzender, de [[*vervoerder|boekhouder|notaris]] en de bestemmeling.",
          "Drie partijen."),
    klik("Klik op de letter bij de plaats en de datum van inlading en levering.", U, [Z["F"]],
         "Ook die horen op een CMR."),
    tabel("Welke transportmodus is dit?",
          [("een goederentrein met containers", "spoorvervoer"), ("een duwbak op het Albertkanaal", "binnenscheepvaart"), ("een containerschip van Shanghai naar Antwerpen", "maritiem vervoer"), ("een vrachtwagen met koeling", "wegvervoer")],
          "Zes transportmodi: weg, spoor, binnenvaart, zee, lucht en pijpleiding.",
          kolommen=["wegvervoer", "spoorvervoer", "binnenscheepvaart", "maritiem vervoer"]),
    keuze("Picken betekent de artikels van een order [[*uit de rekken halen en samenbrengen|in de rekken leggen|naar de klant rijden]].",
          "Daarna wordt de zending verzonden."),
    mk("Waarom is een goede logistiek belangrijk voor de verkoop?",
       ["De verkoop kan zijn beloftes nakomen.", "De logistiek bepaalt de prijs van reclame.", "De logistiek werft de verkopers aan.", "De logistiek schrijft de offertes."], 0,
       "De klant krijgt zijn levering op tijd en de voorraad kost niet te veel."),
    tabel("Waarop vergelijk je transportmodi?",
          [("de snelheid", J), ("de kosten", J), ("het milieueffect", J), ("de kleur van het vervoermiddel", F)],
          "Ook op bereikbaarheid, capaciteit en de aard van het product."),
]

"""De organisatiestructuur van een onderneming — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_organisatiestructuur, met een zelfgetekend organogram."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, GROEN, LICHTGROEN, GRIJS, DONKER, BLAUW

OG = Prent("organogram-bakkerij", "Organogram van bakkerij Gouden Korst", "lijnstaforganisatie met zaakvoerder, adviseur, vier afdelingen, ploegbaas en arbeiders, letters A tot G")
def doos(x, y, b, t, vul="#ffffff"):
    OG.rect(x, y, b, 52, vul, DONKER, 10, 2); OG.tekst(x + b / 2, y + 33, t, 18)
doos(400, 66, 200, "zaakvoerder", LICHTGROEN)
doos(720, 150, 220, "juridisch adviseur", "#eef3f8")
OG.lijn(500, 118, 500, 232, DONKER, 3)
OG.lijn(500, 176, 720, 176, BLAUW, 3, True)
OG.lijn(130, 232, 870, 232, DONKER, 3)
for c, t in ((130, "aankoop"), (375, "productie"), (625, "verkoop"), (870, "boekhouding")):
    OG.lijn(c, 232, c, 262, DONKER, 3); doos(c - 90, 262, 180, t)
OG.lijn(375, 314, 375, 362, DONKER, 3); doos(285, 362, 180, "ploegbaas")
OG.lijn(625, 314, 625, 362, DONKER, 3); doos(535, 362, 180, "winkelverkoper")
OG.lijn(375, 414, 375, 452, DONKER, 3); OG.lijn(270, 452, 480, 452, DONKER, 3)
for c in (270, 480):
    OG.lijn(c, 452, c, 482, DONKER, 3); doos(c - 75, 482, 150, "bakker")
LET = {"A": (630, 92), "B": (965, 176), "C": (258, 288), "D": (258, 388), "E": (172, 508), "F": (508, 288), "G": (753, 288)}
for t, (x, y) in LET.items():
    OG.letter(x, y, t)
U = "organogram-bakkerij.svg"
Z = {t: Prent.rond(x, y, 32) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Klik op de letter bij de staf in dit organogram.", U, [Z["B"]],
         "De juridisch adviseur hangt met een stippellijn naast de lijn: hij adviseert, hij beslist niet."),
    klik("Klik op de letter bij wie de ploegbaas rechtstreeks verantwoording geeft.", U, [Z["C"]],
         "Volg de lijn van de ploegbaas naar boven tot het eerste vakje: de chef productie."),
    klik("Klik op de letter bij wie in deze bakkerij de eindbeslissing neemt.", U, [Z["A"]],
         "Bovenaan het organogram staat de leiding: de zaakvoerder."),
    klik("Klik op de letter bij iemand op het laagste niveau van de bakkerij.", U, [Z["E"]],
         "De bakkers hangen onder de ploegbaas: zij geven aan niemand leiding."),
    klik("Klik op de letter bij de chef van wie de winkelverkoper zijn opdrachten krijgt.", U, [Z["F"]],
         "De winkelverkoper hangt onder de afdeling verkoop."),
    casus("Bekijk het organogram van bakkerij Gouden Korst.", [
        mk("Welke organisatiestructuur toont dit organogram?",
           ["een lijnstaforganisatie", "een functionele organisatie", "een zuivere lijnorganisatie", "een organisatie zonder hiërarchie"], 0,
           "Iedereen heeft één chef, en naast de lijn staat een adviserende staf."),
        inv("Hoeveel niveaus tel je van de zaakvoerder tot de bakkers? Schrijf enkel het getal.", ["4", "vier"],
            "Zaakvoerder, afdelingen, ploegbaas, bakkers."),
        tabel("Klopt dit volgens het organogram?",
              [("Elke bakker heeft precies één chef.", J), ("De juridisch adviseur geeft bevelen aan de ploegbaas.", F), ("De chef aankoop geeft leiding aan de winkelverkoper.", F), ("Het organogram toont hoeveel brood er verkocht wordt.", F)],
              "Een organogram toont de structuur, geen cijfers. De staf adviseert enkel."),
    ]),
    sorteer("Welke structuur past bij deze beschrijving?", ["lijn", "lijnstaf", "functioneel", "horizontaal"],
            [("Iedereen heeft precies één chef en de bevelen lopen van boven naar onder.", "lijn"), ("Naast de lijn staan adviseurs zonder bevelen.", "lijnstaf"), ("Elke chef leidt zijn eigen vakgebied, een medewerker kan meerdere chefs hebben.", "functioneel"), ("Er zijn maar twee niveaus en medewerkers beslissen veel zelf.", "horizontaal")],
            "Vier organisatiestructuren, elk met hun eigen kenmerk."),
    tabel("Is dit een voordeel of een nadeel?",
          [("functionele organisatie: elke chef kent zijn vak door en door", "voordeel"), ("functionele organisatie: twee chefs geven tegenstrijdige orders", "nadeel"), ("horizontale organisatie: er wordt snel beslist", "voordeel"), ("veel niveaus: informatie raakt onderweg kwijt", "nadeel")],
          "Elke structuur heeft sterke en zwakke kanten.",
          kolommen=["voordeel", "nadeel"]),
    keuze("In een lijnstaforganisatie [[*beslist de lijn|beslist de staf]] en [[*adviseert de staf|adviseert de lijn]].",
          "De lijn hoeft het advies niet te volgen."),
    keuze("Een organisatie met weinig niveaus tussen de top en de werkvloer heet een [[*horizontale|verticale|functionele]] of platte organisatie.",
          "Medewerkers krijgen er meer verantwoordelijkheid."),
    mk("Een medewerker in een fabriek krijgt van de chef kwaliteit en van de chef planning een andere opdracht. Welke structuur heeft die fabriek wellicht?",
       ["een functionele organisatie", "een zuivere lijnorganisatie", "een horizontale organisatie", "een eenmanszaak zonder chefs"], 0,
       "In een functionele organisatie kan een medewerker meerdere chefs hebben, met het risico op tegenstrijdige orders."),
    tabel("Welke structuur past het best?",
          [("een kleine bakkerij met een zaakvoerder en drie bakkers", "lijn"), ("een grote fabriek met veel specialisten", "functioneel"), ("een startend softwarebedrijf waar iedereen mee beslist", "horizontaal"), ("een ziekenhuis met een juridische dienst die advies geeft aan de directie", "lijnstaf")],
          "Je kiest op de grootte van de zaak, de aard van het werk en het aantal specialisten.",
          kolommen=["lijn", "lijnstaf", "functioneel", "horizontaal"]),
    keuze("Een volle verticale lijn in een organogram is een [[*gezagslijn|adviesrelatie]]; een stippellijn naar een vakje ernaast is een [[*adviesrelatie|gezagslijn]].",
          "Zo staat de staf in het organogram."),
    mk("Wat kan je niet uit een organogram afleiden?",
       ["de omzet van elke afdeling", "wie aan wie leiding geeft in de zaak", "welke afdelingen er zijn", "hoeveel niveaus er zijn"], 0,
       "Cijfers staan in de jaarrekening, niet in het organogram."),
    keuze("Een groot nadeel van veel niveaus is dat beslissen [[*lang duurt|sneller gaat|niet meer nodig is]].",
          "Elke vraag moet de hele lijn omhoog en weer naar beneden."),
    koppel("Welke pijler van MVO hoort bij welk voorbeeld?",
           [("de bakkerij geeft haar personeel opleiding en veilig werk", "people"), ("de bakkerij gebruikt groene stroom en minder plastic", "planet"), ("de bakkerij houdt genoeg winst over om te investeren", "profit")],
           ["product"], "Mens, milieu en winst: people, planet, profit."),
    sorteer("People, planet of profit?", ["people", "planet", "profit"],
            [("gelijke kansen bij aanwerving", "people"), ("minder uitstoot van de vrachtwagens", "planet"), ("een gezonde winst", "profit"), ("een leefbaar loon", "people"), ("afval sorteren en recycleren", "planet"), ("investeren in een nieuwe oven die meer opbrengt", "profit")],
            "Bij MVO weegt een onderneming de drie pijlers samen af."),
    tabel("Klopt dit over maatschappelijk verantwoord ondernemen?",
          [("Een onderneming die MVO toepast, mag geen winst maken.", F), ("MVO weegt mens, milieu en winst samen af.", J), ("Een beslissing die enkel goed is voor de winst, is volgens MVO een goede beslissing.", F)],
          "Profit is een pijler, maar niet de enige."),
    mk("Een kledingbedrijf laat goedkoop produceren in fabrieken met onveilige werkomstandigheden. Welke pijler van MVO schiet het tekort?",
       ["people", "planet", "profit", "geen enkele pijler"], 0,
       "People gaat over de mensen: werknemers, klanten en de buurt."),
    open_("Beoordeel dit voorbeeld met de drie pijlers van MVO: een supermarkt geeft overschotten aan de voedselbank in plaats van ze weg te gooien.",
          "People: mensen in armoede krijgen eten. Planet: er wordt minder voedsel weggegooid. Profit: de supermarkt verliest weinig, want het eten was toch onverkoopbaar, en ze krijgt een goed imago.",
          "Je kijkt naar de drie pijlers naast elkaar."),
    keuze("In een zuivere lijnorganisatie heeft iedereen precies [[*één|twee|geen]] chef.",
          "De bevelen lopen in een rechte lijn van boven naar onder."),
    volgorde("Zet deze vakjes van boven naar onder zoals ze in een organogram van een fabriek staan.",
             ["de directie", "de chef productie", "de ploegbaas", "de arbeider aan de machine"],
             "Bovenaan staat de leiding, onderaan de werkvloer."),
    sleep("Een [[organogram]] is een schema van de structuur. De adviesgroep naast de lijn heet de [[staf]].",
          ["jaarrekening", "directie"], "Een organogram toont de afdelingen en de hiërarchie."),
    inv("Hoe noem je de structuur waarin het werk per taak is ingedeeld, elk met een eigen chef die er veel van kent? Schrijf één woord.", ["functionele", "functioneel", "functionele organisatie"],
        "De functionele organisatie."),
    tabel("Is dit een nadeel van een organisatie met veel niveaus?",
          [("medewerkers voelen zich ver van de top", J), ("beslissingen duren lang", J), ("er is geen leiding meer", F)],
          "Met veel niveaus is er net veel leiding."),
    keuze("Een organisatiestructuur toont [[*hoe het werk verdeeld is|hoeveel winst er gemaakt wordt|welke producten er verkocht worden]].",
          "Wie wat doet en wie aan wie leiding geeft."),
    mk("Waarom heeft een kleine kapperszaak met twee kappers meestal geen staf?",
       ["Er is te weinig werk voor eigen adviseurs.", "Een staf is bij wet verboden in kleine zaken.", "Kappers mogen geen advies van anderen volgen.", "Een staf geeft bevelen die de zaak vertragen."], 0,
       "Een kleine zaak heeft geen staf nodig, een grote met specialisten wel."),
    tabel("Lijnorganisatie of lijnstaforganisatie?",
          [("enkel een gezagslijn van boven naar onder", "lijn"), ("een preventieadviseur adviseert de directie", "lijnstaf"), ("een IT-specialist geeft advies zonder bevelen", "lijnstaf"), ("de zaakvoerder leidt drie werknemers zonder adviseurs", "lijn")],
          "Bij de lijnstaforganisatie komt een adviserende staf naast de lijn.",
          kolommen=["lijn", "lijnstaf"]),
]

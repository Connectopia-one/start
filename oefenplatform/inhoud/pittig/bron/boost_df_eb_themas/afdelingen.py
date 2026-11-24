"""De afdelingen en hun samenwerking — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_afdelingen, met een zelfgetekend schema van de
informatiestroom tussen de afdelingen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, BLAUW

ST = Prent("stroom-afdelingen", "Wat loopt er tussen de afdelingen?", "klant, verkoop, logistiek, boekhouding en aankoop met zes genummerde pijlen A tot F")
def doos(x, y, t, vul="#ffffff"):
    ST.rect(x - 95, y - 30, 190, 60, vul, DONKER, 12, 2); ST.tekst(x, y + 7, t, 20, vet=True)
POS = {"klant": (150, 320), "verkoop": (440, 170), "logistiek": (440, 470), "boekhouding": (800, 170), "aankoop": (800, 470)}
for t, (x, y) in POS.items():
    doos(x, y, t, LICHTGROEN if t == "klant" else "#ffffff")
PIJLEN = {
    "A": ((215, 285), (345, 195), (262, 222)),   # klant -> verkoop
    "B": ((420, 202), (420, 438), (382, 320)),   # verkoop -> logistiek
    "C": ((537, 160), (703, 160), (620, 128)),   # verkoop -> boekhouding
    "D": ((537, 470), (703, 470), (620, 438)),   # logistiek -> aankoop
    "E": ((345, 450), (215, 355), (262, 420)),   # logistiek -> klant
    "F": ((760, 202), (225, 300), (560, 262)),   # boekhouding -> klant
}
for t, ((x1, y1), (x2, y2), (lx, ly)) in PIJLEN.items():
    ST.pijl(x1, y1, x2, y2, BLAUW, 3); ST.letter(lx, ly, t)
U = "stroom-afdelingen.svg"
Z = {t: Prent.rond(lx, ly, 32) for t, (_, _, (lx, ly)) in PIJLEN.items()}

VRAGEN = [
    klik("Klik op de pijl waarlangs de bestelling gaat zodat de goederen gepickt en verzonden kunnen worden.", U, [Z["B"]],
         "De verkoop geeft de bestelling door aan de logistiek."),
    klik("Klik op de pijl waarlangs de gegevens gaan om een factuur te maken: wie wat kocht, aan welke prijs en met welke korting.", U, [Z["C"]],
         "De verkoop geeft die gegevens door aan de boekhouding."),
    klik("Klik op de pijl waarlangs het bericht gaat dat de voorraad bijna op is.", U, [Z["D"]],
         "Voorraadbeheer hoort bij de logistiek; zij verwittigt de aankoop."),
    klik("Klik op de pijl waarlangs de klant de factuur krijgt.", U, [Z["F"]],
         "De boekhouding maakt de factuur en stuurt ze naar de klant."),
    tabel("Klopt dit volgens het schema?",
          [("Eén verkoop raakt de verkoop, de logistiek en de boekhouding.", J), ("De aankoop krijgt de bestelling rechtstreeks van de klant.", F), ("Als pijl B wegvalt, loopt de levering mis.", J), ("Pijl E is de levering van de goederen.", J)],
          "Weet de logistiek niet wat verkocht is, dan volgen verkeerde of te late leveringen."),
    koppel("Welke afdeling doet deze taak?",
           [("leveranciers zoeken en prijzen vergelijken", "aankoop"), ("offertes maken en klanten opvolgen", "verkoop"), ("de btw-aangifte opmaken", "boekhouding"), ("goederen ontvangen, opslaan en verzenden", "logistiek"), ("personeel aanwerven en opleiden", "HR")],
           ["IT"], "Elke afdeling heeft haar eigen taken."),
    sorteer("Welke afdeling hoort bij deze taak?", ["marketing", "IT", "R&D"],
            [("een reclamecampagne bedenken", "marketing"), ("het netwerk beveiligen", "IT"), ("een nieuw product ontwikkelen", "R&D"), ("onderzoeken wat de klant wil", "marketing"), ("de boekhoudsoftware laten draaien", "IT"), ("een betere werkwijze uittesten", "R&D")],
            "Marketing bewerkt de markt, IT verzorgt de systemen, R&D zoekt nieuwe producten."),
    keuze("HR staat voor [[*human resources|hogere rekeningen|handel en reclame]]: de mensen van de onderneming.",
          "De personeelsafdeling."),
    keuze("R&D staat voor [[*research and development|retail and distribution|risk and damage]]: onderzoek en ontwikkeling.",
          "Nieuwe producten en betere werkwijzen."),
    mk("Een webwinkel verkoopt 200 sneakers in een actie, maar de logistiek wist niets van die actie. Wat gebeurt er waarschijnlijk?",
       ["De leveringen lopen mis en klanten worden boos.", "De boekhouding maakt helemaal geen facturen meer op.", "De R&D-afdeling ontwerpt meteen een nieuwe sneaker.", "De klanten krijgen hun sneakers net veel sneller."], 0,
       "Slechte communicatie geeft fouten, vertraging en klachten."),
    tabel("Hoort dit bij de taken van de boekhouding?",
          [("facturen boeken", J), ("de jaarrekening voorbereiden", J), ("het transport plannen", F), ("de betalingen opvolgen", J)],
          "Het transport plannen is werk voor de logistiek."),
    mk("Waarom werkt de IT-afdeling voor alle andere afdelingen?",
       ["Alle afdelingen gebruiken computersystemen.", "IT maakt de facturen voor elke klant op.", "IT werft het personeel van elke afdeling aan.", "IT bepaalt de prijs van elk product."], 0,
       "Van het kassasysteem tot de boekhoudsoftware loopt alles over hun netwerk."),
    casus("Lees de situatie.\n\nFietsenwinkel Trappers heeft drie werknemers. Lies doet de verkoop en de marketing, Omar de herstellingen, de aankoop en het magazijn. De zaakvoerder houdt zelf de boekhouding en het personeel bij. Een computerfirma komt af en toe het kassasysteem nakijken.", [
        tabel("Wie doet bij Trappers deze taak?",
              [("de reclame op sociale media", "Lies"), ("nieuwe fietsen bestellen bij de leverancier", "Omar"), ("de loonadministratie", "zaakvoerder"), ("de voorraad in het magazijn", "Omar")],
              "In een kleine zaak liggen de taken van meerdere afdelingen bij één persoon.",
              kolommen=["Lies", "Omar", "zaakvoerder"]),
        keuze("De taken van de afdeling [[*IT|marketing|aankoop]] laat Trappers door een firma van buiten doen.",
              "De computerfirma verzorgt het kassasysteem."),
        mk("Wat toont dit voorbeeld?",
           ["De taken bestaan altijd, ook zonder aparte afdeling.", "Een kleine zaak heeft helemaal geen boekhouding nodig.", "Elke onderneming heeft alle acht afdelingen apart.", "Een fietsenwinkel heeft helemaal geen logistiek nodig."], 0,
           "Of er een aparte afdeling voor is, hangt af van de grootte van de zaak."),
    ]),
    keuze("Een fout van de [[*aankoop|marketing|HR]] kan de verkoop stilleggen: zonder goederen in huis valt er niets te leveren.",
          "Alles hangt samen."),
    tabel("Wat heeft deze afdeling nodig van een andere?",
          [("R&D", "wat de klant wil, van de marketing"), ("HR", "welke functies vrijkomen, van de afdelingen"), ("de boekhouding", "de verkoopgegevens, van de verkoop"), ("de aankoop", "welke voorraad laag is, van de logistiek")],
          "Elke afdeling heeft gegevens van de andere nodig.",
          kolommen=["wat de klant wil, van de marketing", "welke functies vrijkomen, van de afdelingen", "de verkoopgegevens, van de verkoop", "welke voorraad laag is, van de logistiek"]),
    volgorde("Zet de documentenstroom bij één bestelling in een logische volgorde.",
             ["De verkoop neemt de bestelling van de klant op.", "De logistiek pickt en verzendt de goederen.", "De boekhouding maakt de factuur.", "De boekhouding volgt de betaling van de klant op."],
             "Van bestelling tot betaling."),
    inv("Hoe noem je de reeks documenten die van de ene afdeling naar de andere gaat? Schrijf één woord.", ["documentenstroom", "de documentenstroom", "documentstroom"],
        "De documentenstroom."),
    sleep("De verkoop geeft de [[bestelbon]] door aan de logistiek. Bij de levering gaat er een [[leverbon]] mee.",
          ["loonfiche", "btw-aangifte"], "Loonfiches en de btw-aangifte lopen langs HR en de boekhouding."),
    tabel("Klopt dit over de samenwerking tussen afdelingen?",
          [("Elke afdeling kan volledig op haar eigen werken.", F), ("De boekhouding staat los van de rest.", F), ("Een goede samenwerking helpt de klant sneller.", J), ("Een onderneming bespreekt haar cijfers met alle chefs om samen bij te sturen.", J)],
          "Elke aankoop, verkoop en loonbetaling komt bij de boekhouding terecht."),
    mk("Een winkelketen start een grote kortingsactie. Welke afdeling moet de details van de marketing het eerst kennen om klanten goed te helpen?",
       ["de verkoop", "de IT", "de logistiek", "de boekhouding"], 0,
       "Wat de klant wil en wat er in de actie zit, bepaalt het verkoopgesprek."),
    keuze("Het doorgeven van informatie tussen afdelingen heet [[*communicatie|concurrentie|consumptie]].",
          "Of overleg."),
    tabel("Is deze afdeling betrokken bij één gewone verkoop aan een klant?",
          [("de verkoop", J), ("de logistiek", J), ("de boekhouding", J), ("R&D", F)],
          "R&D werkt aan nieuwe producten, niet aan een losse verkoop."),
    open_("Een klant krijgt een factuur voor 10 dozen, maar ontving er maar 8. Welke afdelingen hebben slecht samengewerkt en wat ging er wellicht mis?",
          "De logistiek leverde 8 dozen, maar de verkoop gaf 10 dozen door aan de boekhouding, of de logistiek meldde niet dat er maar 8 vertrokken. De boekhouding factureerde dus op foute gegevens. Verkoop, logistiek en boekhouding moeten dezelfde gegevens delen.",
          "Slechte communicatie geeft fouten en klachten."),
    klik("Klik op de pijl die toont dat de klant iets bestelt.", U, [Z["A"]],
         "Alles begint bij de bestelling van de klant aan de verkoop."),
    keuze("Een vacature voor een magazijnier schrijft de afdeling [[*HR|R&D|marketing]] uit, op vraag van de logistiek.",
          "HR moet weten welke functies vrijkomen."),
    tabel("Welke afdeling is dit?",
          [("Ze zorgt voor computers, netwerk en de beveiliging van gegevens.", "IT"), ("Ze zoekt nieuwe producten en betere werkwijzen.", "R&D"), ("Ze bepaalt product, prijs, plaats en promotie.", "marketing"), ("Ze regelt de loonadministratie.", "HR")],
          "Acht afdelingen, elk met een eigen opdracht.",
          kolommen=["IT", "R&D", "marketing", "HR"]),
    mk("Wat is het gevolg van slechte communicatie tussen de verkoop en de boekhouding?",
       ["Klanten krijgen een foute factuur.", "De machines in de fabriek vallen stil.", "Het netwerk van de onderneming crasht.", "De marketing bedenkt geen reclame meer."], 0,
       "De boekhouding factureert met de gegevens die de verkoop doorgeeft."),
    keuze("Een zaak met drie werknemers heeft [[*meestal geen|altijd een]] eigen R&D-afdeling.",
          "De taken bestaan wel, maar niet als aparte afdeling."),
]

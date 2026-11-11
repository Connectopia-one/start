"""Inflatie, deflatie en prijsstabiliteit — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("inflatie-cpi-verloop", 2018, 2027, 95, 130, 1, 5)
CPI = [(2019, 100), (2020, 101), (2021, 103), (2022, 112), (2023, 118), (2024, 121), (2025, 120), (2026, 123)]


def lijn(pts):
    def f(x):
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if x0 <= x <= x1:
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        return None
    return f


GRAFIEKEN = [
    dict(naam=G, titel="Consumptieprijsindex (CPI) van een land, elk jaar in januari",
         krommen=[(lijn(CPI), "groen", "", (2019, 2026))],
         punten=[(x, y, str(y)) for x, y in CPI],
         xlabel="jaar", ylabel="CPI", ijk_x=1, ijk_y=5),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen en rekenvragen over inflatie en deflatie")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "Klik op het punt van het jaar waarin de CPI daalde ten opzichte van het jaar ervoor.",
        P, [punt_zone(G, 2025, 120)],
        "Van 121 naar 120: het prijspeil daalde, dat is deflatie.",
    ),
    klik(
        "Klik op het punt van het jaar waarin de inflatie ten opzichte van het jaar ervoor het hoogst was.",
        P, [punt_zone(G, 2022, 112)],
        "Van 103 naar 112: 9 / 103 · 100 ≈ 8,7 %. Geen enkele andere stijging is procentueel zo groot.",
    ),
    met_prent(P, inv(
        "Bereken de inflatie van 2023 naar 2024 in procent. Rond af op één decimaal en schrijf het getal met een komma.",
        "2,5",
        "(121 − 118) / 118 · 100 = 2,54 %, afgerond 2,5 %.",
    )),
    met_prent(P, inv(
        "Met hoeveel procent stegen de prijzen van 2019 tot 2026 in totaal? Schrijf enkel het getal.",
        "23",
        "(123 − 100) / 100 · 100 = 23 %.",
    )),
    met_prent(P, mk(
        "De ECB streeft naar een inflatie van 2 % op middellange termijn. Wat deed ze waarschijnlijk in 2022?",
        ["De beleidsrente verhogen", "De beleidsrente verlagen", "De btw in dit land verlagen", "Geld bijdrukken om de prijzen te doen dalen"],
        0,
        "De inflatie lag ver boven 2 %. Bij te hoge inflatie verhoogt de ECB de beleidsrente.",
    )),
    tabel(
        "Welk begrip past bij de beschrijving?",
        [
            ("Een algemene en aanhoudende stijging van het prijspeil", "Inflatie"),
            ("Een algemene daling van het prijspeil", "Deflatie"),
            ("Inflatie samen met een stilstaande economie en werkloosheid", "Stagflatie"),
            ("De verpakking wordt kleiner, de prijs blijft gelijk", "Krimpflatie"),
            ("De service daalt, de prijs blijft gelijk", "Beknibbelflatie"),
        ],
        "Krimpflatie en beknibbelflatie zie je niet aan een hoger prijskaartje.",
        kolommen=["Inflatie", "Deflatie", "Stagflatie", "Krimpflatie", "Beknibbelflatie"],
    ),
    inv(
        "Een zak chips gaat van 250 gram naar 200 gram, voor dezelfde prijs. Met hoeveel procent is hij per gram duurder geworden? Schrijf enkel het getal.",
        "25",
        "250 / 200 = 1,25: per gram 25 % duurder.",
    ),
    tabel(
        "Welke soort inflatie is dit?",
        [
            ("De prijs van ingevoerde olie verdubbelt", "Importinflatie"),
            ("Bouwvakkers krijgen een flinke loonsverhoging, die aannemers doorrekenen", "Kosteninflatie"),
            ("De overheid geeft in een hoogconjunctuur veel meer uit, de vraag is groter dan de productie", "Bestedingsinflatie"),
            ("Een land drukt massaal geld bij", "Monetaire inflatie"),
        ],
        "Duurdere invoer: import. Duurdere lonen of grondstoffen: kosten. Te veel vraag: bestedingen. Te veel geld: monetair.",
        kolommen=["Bestedingsinflatie", "Kosteninflatie", "Importinflatie", "Monetaire inflatie"],
    ),
    mk(
        "Weinig concurrentie en automatische koppelingen zorgen in een land jaar na jaar voor inflatie. Welke soort inflatie is dat?",
        ["Structurele inflatie", "Conjuncturele inflatie", "Importinflatie", "Beknibbelflatie"],
        0,
        "Structurele inflatie komt uit blijvende kenmerken van een economie.",
    ),
    casus(
        "In een land is de geldhoeveelheid M = 400, de omloopsnelheid V = 5 en het aantal transacties T = 1 000.",
        [
            inv("Bereken het prijspeil P met de ruilvergelijking van Fisher. Schrijf enkel het getal.", "2",
                "M · V = P · T: 400 · 5 = P · 1 000, dus P = 2."),
            mk("De geldhoeveelheid verdubbelt; V en T blijven gelijk. Wat gebeurt er met P?",
               ["P verdubbelt naar 4", "P blijft 2", "P halveert naar 1", "P stijgt met 400"], 0,
               "800 · 5 = P · 1 000, dus P = 4."),
            mk("Wat stelt V voor?", ["De omloopsnelheid van het geld", "De waarde van de munt", "Het volume van de productie", "De rente"], 0,
               "V is hoe vaak een euro gemiddeld van eigenaar verandert."),
        ],
    ),
    tabel(
        "Welke index past bij de beschrijving?",
        [
            ("Om de inflatie tussen EU-landen te vergelijken", "HICP"),
            ("De CPI zonder tabak, alcohol, benzine en diesel", "Gezondheidsindex"),
            ("Een drempel waarna uitkeringen en ambtenarenlonen aangepast worden", "Spilindex"),
            ("De prijzen van alles wat in een land geproduceerd wordt", "Bbp-deflator"),
        ],
        "De afgevlakte gezondheidsindex is het gemiddelde van de laatste vier maanden; overschrijdt hij de spilindex, dan volgt een aanpassing.",
        kolommen=["HICP", "Gezondheidsindex", "Spilindex", "Bbp-deflator"],
    ),
    mk(
        "Waarom gebruikt België voor de loonindexering de gezondheidsindex en niet de gewone CPI?",
        ["Om te vermijden dat duurdere tabak, alcohol en brandstof de lonen opdrijven",
         "Omdat de gezondheidsindex enkel de prijzen van ziekenhuizen en apothekers meet",
         "Omdat de gewone CPI enkel in andere EU-landen gemeten wordt, niet in België",
         "Omdat de gezondheidsindex altijd hoger ligt dan de CPI, zodat werknemers meer krijgen"],
        0,
        "De gezondheidsindex is de CPI zonder tabak, alcohol, benzine en diesel.",
    ),
    inv(
        "De afgevlakte gezondheidsindex is het gemiddelde van de laatste vier maanden. De gezondheidsindex was 128, 129, 131 en 132. Bereken de afgevlakte gezondheidsindex. Schrijf enkel het getal.",
        "130",
        "(128 + 129 + 131 + 132) / 4 = 520 / 4 = 130.",
    ),
    tabel(
        "Wie verliest bij een onverwacht hoge inflatie?",
        [
            ("Een spaarder met een lage rente", "Verliest koopkracht"),
            ("Iemand met een vast inkomen dat niet geïndexeerd wordt", "Verliest koopkracht"),
            ("Een werknemer wiens loon automatisch geïndexeerd wordt", "Beschermd door indexering"),
        ],
        "Inflatie maakt geld minder waard: spaarders met een lage rente en vaste inkomens verliezen. De indexering beschermt de koopkracht.",
        kolommen=["Verliest koopkracht", "Beschermd door indexering"],
    ),
    mk(
        "De inflatie is 4 % en je loon stijgt niet. Wat gebeurt er met je koopkracht?",
        ["Ze daalt met ongeveer 4 %", "Ze stijgt met ongeveer 4 %", "Ze blijft gelijk", "Ze daalt met ongeveer 40 %"],
        0,
        "Met hetzelfde loon koop je ongeveer 4 % minder.",
    ),
    mk(
        "Waarom kan deflatie de economie verder afremmen?",
        ["Consumenten stellen aankopen uit, omdat ze verwachten dat het later goedkoper wordt",
         "Bedrijven verkopen dan veel meer, waardoor ze minder mensen nodig hebben in hun winkels",
         "Schulden met een vaste rente worden lichter, waardoor gezinnen veel minder gaan lenen",
         "De ECB moet dan volgens de regels de rente verhogen tot boven de 2 %"],
        0,
        "Uitgestelde aankopen doen de vraag verder dalen. Bovendien worden schulden met vaste rente zwaarder.",
    ),
    tabel(
        "Waar of niet waar over deflatie?",
        [
            ("Bij deflatie wordt een schuld met vaste rente zwaarder om te dragen.", J),
            ("Een sterke daling van de vraag in een crisis kan deflatie veroorzaken.", J),
            ("Deflatie is een algemene stijging van het prijspeil.", F),
            ("Sterk stijgende grondstofprijzen veroorzaken deflatie.", F),
        ],
        "Sterk dalende grondstofprijzen kunnen deflatie veroorzaken, stijgende niet.",
    ),
    sorteer(
        "Is dit een rechtstreeks of een onrechtstreeks prijsbeleid van de overheid?",
        ["Rechtstreeks", "Onrechtstreeks"],
        [
            ["Een maximumprijs voor energie vastleggen", "Rechtstreeks"],
            ["De btw op energie verlagen", "Onrechtstreeks"],
            ["Meer concurrentie op een markt toelaten", "Onrechtstreeks"],
        ],
        "Rechtstreeks: de prijs zelf vastleggen. Onrechtstreeks: de omstandigheden veranderen.",
    ),
    mk(
        "Een politicus vraagt de ECB om de btw op energie in België te verlagen. Wat klopt?",
        ["Dat kan de ECB niet: de btw verlagen doet de nationale overheid", "De ECB kan dat, maar enkel als de inflatie boven 2 % ligt in België",
         "De ECB kan enkel de btw verhogen, niet verlagen, om de inflatie te remmen", "De ECB moet dat doen zodra de spilindex in België overschreden is"],
        0,
        "De ECB stuurt met de rente. Belastingen zijn een zaak van de overheid.",
    ),
    keuze(
        "Bij stagflatie [[*remt|versnelt]] een renteverhoging de inflatie af, maar ze remt ook de [[*groei|werkloosheid]].",
        "Daarom is stagflatie lastig: de rente kan niet tegelijk tegen inflatie en voor groei werken.",
    ),
    koppel(
        "Koppel elk teken van de ruilvergelijking M · V = P · T aan zijn betekenis.",
        [
            ["M", "De geldhoeveelheid"],
            ["P", "Het prijspeil"],
            ["T", "Het aantal transacties"],
        ],
        ["De marginale consumptiequote"],
        "V is de omloopsnelheid van het geld.",
    ),
    open_(
        "De prijzen in België stijgen al een tijd sneller dan in de buurlanden. Leg uit wat dat betekent voor de Belgische export.",
        "Belgische producten worden duurder tegenover buitenlandse. Buitenlandse klanten kopen dan minder bij Belgische bedrijven: de export daalt en de concurrentiekracht van België verzwakt.",
    ),
    inv(
        "De CPI daalt van 140 naar 133. Bereken de inflatie in procent. Zet een minteken als ze negatief is.",
        "-5",
        "(133 − 140) / 140 · 100 = −5 %: deflatie.",
    ),
    mk(
        "Een merk koekjes verkoopt voortaan 18 koekjes per pak in plaats van 20, voor dezelfde prijs. Waarom merk je dat niet aan het etiket?",
        ["Het is krimpflatie: de verpakking wordt kleiner, de prijs blijft gelijk", "Het is deflatie: de prijs per pak en per koekje daalt voor de klant",
         "Het is beknibbelflatie: de kwaliteit van elk koekje daalt, de prijs blijft gelijk", "Het is monetaire inflatie: er is veel meer geld in omloop dan vroeger"],
        0,
        "Per koekje betaal je wel meer: 20 / 18 ≈ 1,11, dus ongeveer 11 % duurder.",
    ),
    mk(
        "Wat is de inflatiedoelstelling van de ECB?",
        ["2 % op middellange termijn", "0 % elk jaar", "5 % per kwartaal", "Zo hoog mogelijk, om de groei te steunen"],
        0,
        "De ECB streeft naar 2 % op middellange termijn.",
    ),
    inv(
        "Volgens Fisher geldt M · V = P · T. Bereken T als M = 600, V = 4 en P = 3. Schrijf enkel het getal.",
        "800",
        "600 · 4 = 3 · T, dus 2 400 = 3T en T = 800.",
    ),
    sleep(
        "Inflatie is een [[algemene]] en [[aanhoudende]] stijging van het prijspeil.",
        ["tijdelijke", "beperkte"],
        "Een enkel product dat duurder wordt, is nog geen inflatie.",
    ),
    mk(
        "Welke soort inflatie volgt de hoog- en laagconjunctuur?",
        ["Conjuncturele inflatie", "Structurele inflatie", "Importinflatie", "Krimpflatie"],
        0,
        "Conjuncturele inflatie beweegt mee met de conjunctuur; structurele inflatie komt uit blijvende kenmerken.",
    ),
]

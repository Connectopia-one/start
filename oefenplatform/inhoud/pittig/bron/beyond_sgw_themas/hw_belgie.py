"""Humane wetenschappen: de Belgische staat en zijn bestuursniveaus — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm en twee eigen schema's: de
bestuursniveaus, en welke gemeenschap in welk gewest bevoegd is. Strikt
binnen beyond/bron/sg_hw_belgie.py."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# De bestuursniveaus ------------------------------------------------------------------
BN = Prent("bestuursniveaus", "Vier bestuursniveaus in België",
           "vier brede balken onder elkaar, van boven naar beneden smaller wordend gebied: federale overheid, gemeenschappen en gewesten, provincies, gemeenten; elk met een letter A tot D")
NIV = [("A", "federale overheid", "parlement: Kamer en Senaat · regering"),
       ("B", "gemeenschappen en gewesten", "bv. Vlaams Parlement · Vlaamse Regering"),
       ("C", "provincies", "provincieraad · deputatie en gouverneur"),
       ("D", "gemeenten", "gemeenteraad · college van burgemeester en schepenen")]
Y0 = {}
for i, (k, naam, organen) in enumerate(NIV):
    y = 80 + i * 130
    x = 120 + i * 40
    b = 760 - i * 80
    Y0[k] = (x, y, b)
    BN.rect(x, y, b, 105, ["#e2eadb", "#eef3e8", "#f4f2ea", "#ffffff"][i], DONKER, 14, 2)
    BN.letter(x + 35, y + 52, k)
    BN.tekst(x + b / 2 + 20, y + 45, naam, 24, vet=True)
    BN.tekst(x + b / 2 + 20, y + 80, organen, 17)


def niveau(k):
    x, y, b = Y0[k]
    return [Prent.zone(x, y, b, 105)]


# Gewesten en gemeenschappen --------------------------------------------------------------
GG = Prent("gewesten-gemeenschappen", "Welke gemeenschap is bevoegd in welk gewest?",
           "drie kolommen voor de gewesten (Vlaams Gewest, Brussels Hoofdstedelijk Gewest, Waals Gewest) en eronder gekleurde blokken voor de gemeenschappen die er bevoegd zijn")
KOL = {"V": (90, "Vlaams Gewest"), "B": (380, "Brussels Hoofdstedelijk Gewest"), "W": (670, "Waals Gewest")}
for k, (x, naam) in KOL.items():
    GG.rect(x, 90, 250, 70, GRIJS, DONKER, 12, 2)
    GG.tekst(x + 125, 134, naam if k != "B" else "Brussels Hoofdst. Gewest", 19, vet=True)
    GG.rect(x, 170, 250, 400, "#ffffff", DONKER, 12, 2)
GG.rect(105, 190, 220, 360, LICHTGROEN, DONKER, 10, 2)
GG.tekst(215, 375, "Vlaamse", 20, vet=True)
GG.tekst(215, 400, "Gemeenschap", 20, vet=True)
GG.rect(395, 190, 105, 360, LICHTGROEN, DONKER, 10, 2)
GG.tekst(447, 365, "Vlaamse", 16, vet=True)
GG.tekst(447, 388, "Gem.", 16, vet=True)
GG.rect(510, 190, 105, 360, "#f1d9b5", DONKER, 10, 2)
GG.tekst(562, 365, "Franse", 16, vet=True)
GG.tekst(562, 388, "Gem.", 16, vet=True)
GG.rect(685, 190, 220, 270, "#f1d9b5", DONKER, 10, 2)
GG.tekst(795, 320, "Franse", 20, vet=True)
GG.tekst(795, 345, "Gemeenschap", 20, vet=True)
GG.rect(685, 470, 220, 80, "#cfe0ee", DONKER, 10, 2)
GG.tekst(795, 505, "Duitstalige", 18, vet=True)
GG.tekst(795, 528, "Gemeenschap", 18, vet=True)
GG.tekst(500, 615, "Gemeenschappen: onderwijs, cultuur, welzijn · Gewesten: economie, milieu, ruimtelijke ordening", 16)


def gewest(k):
    x = KOL[k][0]
    return [Prent.zone(x, 90, 250, 480)]


VRAGEN = [
    klik("Klik op het bestuursniveau dat bevoegd is voor defensie en justitie.", BN.bestand, niveau("A"),
         "Defensie, justitie, buitenlandse zaken en de sociale zekerheid blijven federaal."),
    klik("Klik op het bestuursniveau waar een college van burgemeester en schepenen de beslissingen uitvoert.", BN.bestand, niveau("D"),
         "Het college van burgemeester en schepenen is het uitvoerend orgaan van de gemeente."),
    klik("Een leerkracht wil weten wie de eindtermen van het secundair onderwijs in Vlaanderen vastlegt. Klik op het juiste niveau.", BN.bestand, niveau("B"),
         "Onderwijs is een gemeenschapsbevoegdheid."),
    met_prent(BN.bestand, keuze("Op niveau C voert de [[*deputatie|gemeenteraad|Kamer]] het beleid uit dat de provincieraad goedkeurt.",
              "De deputatie, met de gouverneur, is het uitvoerend orgaan van de provincie.")),
    klik("Klik op het gewest waar zowel de Vlaamse als de Franse Gemeenschap bevoegd is voor onderwijs.", GG.bestand, gewest("B"),
         "In Brussel zijn er Nederlandstalige en Franstalige scholen. Voor de eerste is de Vlaamse, voor de tweede de Franse Gemeenschap bevoegd."),
    klik("Klik op het gewest waarin het Duitse taalgebied ligt.", GG.bestand, gewest("W"),
         "Het Duitse taalgebied heeft een eigen gemeenschap, maar hoort voor de gewestbevoegdheden bij het Waals Gewest."),
    met_prent(GG.bestand, mk("Waarom heeft België gewesten én gemeenschappen?",
              ["Vlamingen wilden vooral culturele, Walen vooral economische zelfstandigheid",
               "elke provincie wilde een eigen parlement en een eigen regering om zelf te beslissen",
               "de Europese Unie verplichtte België tot die verdeling",
               "de grondwet van 1830 voorzag die verdeling al"], 0,
              "Gemeenschappen kwamen er voor taal en cultuur, gewesten voor economie en grondgebied.")),
    tabel("Wie is bevoegd?", [
        ("de bouw van een nieuwe ringweg rond Antwerpen", "gewest"),
        ("het aantal lesuren Nederlands in het secundair onderwijs", "gemeenschap"),
        ("de aankoop van nieuwe gevechtsvliegtuigen", "federaal"),
        ("een vergunning voor een windmolenpark in Wallonië", "gewest"),
        ("de subsidies voor een Nederlandstalig theater in Brussel", "gemeenschap"),
    ], "Grondgebonden zaken bij de gewesten, persoonsgebonden bij de gemeenschappen, en wat het hele land aangaat federaal.",
       kolommen=["federaal", "gemeenschap", "gewest"]),
    volgorde("Zet van de grootste naar de kleinste bestuurseenheid.", [
        "de federale staat",
        "een gewest",
        "een provincie",
        "een gemeente",
    ], "België, een gewest, een provincie en een gemeente: elk ligt binnen het vorige."),
    keuze("België werd een federale staat [[*stap voor stap, via staatshervormingen|in één keer, bij de onafhankelijkheid|door een beslissing van de NAVO]].",
          "Sinds 1970 waren er zes staatshervormingen."),
    sorteer("Hoort dit bij een unitaire of een federale staat?", ["Unitair", "Federaal"], [
        ["Eén regering beslist over onderwijs in het hele land.", "Unitair"],
        ["Deelstaten maken eigen decreten.", "Federaal"],
        ["Er is enkel een nationaal parlement.", "Unitair"],
        ["De bevoegdheden zijn verdeeld over meerdere regeringen.", "Federaal"],
    ], "Eén centrum of een verdeling van de macht over meerdere niveaus."),
    koppel("Koppel elk controleorgaan aan wat het doet.", [
        ["Grondwettelijk Hof", "toetst wetten en decreten aan de grondwet"],
        ["Raad van State", "vernietigt onwettige beslissingen van een overheid"],
        ["Hof van Cassatie", "kijkt na of rechters de wet juist toepasten"],
    ], ["telt de stemmen na de verkiezingen"], "Drie controleorganen met elk een eigen taak."),
    tabel("Welk controleorgaan kan hier tussenkomen?", [
        ("Een decreet van de Franse Gemeenschap regelt iets dat federaal is.", "Grondwettelijk Hof"),
        ("Een provincie weigert een vergunning zonder de regels te volgen.", "Raad van State"),
        ("Een hof van beroep paste een wetsartikel verkeerd toe in een vonnis.", "Hof van Cassatie"),
    ], "Bevoegdheidsconflicten en wetten bij het Grondwettelijk Hof, bestuurshandelingen bij de Raad van State, vonnissen bij het Hof van Cassatie.",
       kolommen=["Grondwettelijk Hof", "Raad van State", "Hof van Cassatie"]),
    casus(
        "Na de verkiezingen hebben vier partijen samen 88 van de 150 zetels in de Kamer. "
        "Ze schrijven een regeerakkoord en vormen een regering. Drie andere partijen, met samen 45 zetels, "
        "zitten niet in de regering. Een van hen vraagt in de Kamer elke week uitleg aan de minister van Justitie over de overvolle gevangenissen.",
        [
            keuze("De vier partijen in de regering vormen samen een [[*coalitie|oppositie|deputatie]].",
                  "Partijen die samen een meerderheid vormen en regeren, vormen een coalitie."),
            keuze("De partijen die niet in de regering zitten, vormen de [[*oppositie|coalitie|deputatie]].",
                  "De oppositie controleert de regering kritisch."),
            mk("Welke functie van het parlement zie je bij de wekelijkse vragen?",
               ["de controle op de regering",
                "het goedkeuren van de begroting",
                "het maken van een decreet",
                "het benoemen van de rechters"], 0,
               "Vragen stellen aan ministers is een middel van controle."),
            inv("Hoeveel zetels heeft de coalitie meer dan de minimale meerderheid van 76?", ["12"],
                "88 min 76 is 12."),
        ],
    ),
    sleep("De Vlaamse Gemeenschap en het Vlaams Gewest werken met één [[parlement]] en één [[regering]].",
          ["provincieraad", "gemeenteraad"], "Vlaanderen voegde de instellingen van gemeenschap en gewest samen."),
    keuze("Een regel van het federale parlement heet een [[*wet|decreet|ordonnantie]], een regel van het Vlaams Parlement een [[*decreet|wet|ordonnantie]].",
          "Wet, decreet of ordonnantie (Brussel)."),
    mk("Welk voorbeeld past bij een confederale staat?",
       ["deelstaten beslissen bijna alles en spreken af wat ze samen doen",
        "één hoofdstad beslist over alles wat er in het land en in elke stad gebeurt",
        "elke gemeente heeft een eigen leger en een eigen munt",
        "de koning maakt alle wetten zonder een parlement"], 0,
       "In een confederatie ligt de meeste macht bij de deelstaten."),
    tabel("Klopt dit over de Belgische staatsstructuur?", [
        ("Het Duitse taalgebied heeft een eigen gemeenschap.", J),
        ("Er zijn drie gewesten en drie gemeenschappen.", J),
        ("Provincies maken decreten over onderwijs.", F),
        ("België was bij zijn ontstaan al een federale staat.", F),
    ], "De provincies zijn geen deelstaten, en België begon als unitaire staat."),
    inv("Vanaf welk jaar staat in de grondwet dat België een federale staat is?", ["1993"],
        "De staatshervorming van 1993 maakte België officieel federaal."),
    keuze("Het [[*Grondwettelijk Hof|Hof van Cassatie|vredegerecht]] heette vroeger het Arbitragehof, omdat het conflicten over bevoegdheden tussen de overheden beslechtte.",
          "Arbitrage betekent bemiddelen in een conflict."),
    mk("Welke regering is bevoegd voor het afvalbeleid in Gent?",
       ["de Vlaamse Regering",
        "de federale regering",
        "de Franse Gemeenschap",
        "de Europese Raad"], 0,
       "Afval en milieu zijn gewestbevoegdheden. Gent ligt in het Vlaams Gewest."),
    sorteer("Persoonsgebonden of grondgebonden bevoegdheid?", ["Persoonsgebonden (gemeenschap)", "Grondgebonden (gewest)"], [
        ["cultuur", "Persoonsgebonden (gemeenschap)"],
        ["ruimtelijke ordening", "Grondgebonden (gewest)"],
        ["onderwijs", "Persoonsgebonden (gemeenschap)"],
        ["landbouw", "Grondgebonden (gewest)"],
        ["openbare werken", "Grondgebonden (gewest)"],
    ], "Wat met mensen te maken heeft, of met het grondgebied."),
    keuze("In een parlementaire democratie heeft de regering het [[*vertrouwen|bevel|vonnis]] van de meerderheid in het parlement nodig.",
          "Verliest ze dat vertrouwen, dan moet ze opstappen."),
    mk("Waarom duurt een federale regeringsvorming in België vaak lang?",
       ["er moeten meerdere partijen uit beide taalgroepen akkoord gaan",
        "de grondwet verbiedt regeren voor de zomervakantie",
        "de gemeenten moeten eerst allemaal goedkeuring geven",
        "de koning moet elke minister apart laten verkiezen door het volk van zijn taalgroep"], 0,
       "Een meerderheid vraagt een coalitie, en de federale regering telt evenveel Nederlandstalige als Franstalige ministers."),
    inv("Hoeveel staatshervormingen waren er sinds 1970?", ["6", "zes"],
        "Zes staatshervormingen maakten van de unitaire staat stap voor stap een federale staat."),
    tabel("Bij welk orgaan hoort dit?", [
        ("keurt de decreten van Vlaanderen goed", "Vlaams Parlement"),
        ("voert de decreten van Vlaanderen uit", "Vlaamse Regering"),
        ("beslist in een gemeente over het reglement voor de markt", "gemeenteraad"),
    ], "Het parlement en de raad maken regels, de regering voert ze uit.",
       kolommen=["Vlaams Parlement", "Vlaamse Regering", "gemeenteraad"]),
    open_("Leg met een voorbeeld uit waarom België zowel gemeenschappen als gewesten heeft.",
          "Gemeenschappen zijn gebaseerd op taal en regelen persoonsgebonden zaken, zoals onderwijs en cultuur. Gewesten zijn gebaseerd op grondgebied en regelen grondgebonden zaken, zoals milieu of ruimtelijke ordening. In Brussel zie je waarom dat nodig is: het is één gewest, maar zowel de Vlaamse als de Franse Gemeenschap zijn er bevoegd voor de eigen scholen."),
]

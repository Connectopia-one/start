"""Humane wetenschappen: ideologieën, partijen en verkiezingen — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm, een eigen grafiek van de
zetelverdeling in de Kamer na 9 juni 2024 (bron: officiële uitslag, FOD
Binnenlandse Zaken) en een links-rechtsas met drie lege vakken. Strikt binnen
beyond/bron/sg_hw_partijen.py. Partijen worden neutraal beschreven, met de
ideologie waartoe ze gewoonlijk gerekend worden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

# Zetels in de Kamer na 9 juni 2024 ----------------------------------------------------------
ZETELS = [("N-VA", 24), ("Vlaams Belang", 20), ("MR", 20), ("PS", 16), ("PVDA-PTB", 15), ("Les Engagés", 14),
          ("Vooruit", 13), ("cd&v", 11), ("Open Vld", 7), ("Groen", 6), ("Ecolo", 3), ("DéFI", 1)]
NL = {"N-VA", "Vlaams Belang", "Vooruit", "cd&v", "Open Vld", "Groen"}
ZK = Prent("zetels-kamer-2024", "Zetels in de Kamer na de verkiezingen van 9 juni 2024 (150 zetels)",
           "een staafgrafiek met twaalf staven, één per partij, met het aantal zetels erboven; Nederlandstalige partijen in groen, Franstalige in oranje, PVDA-PTB in grijs")
X0, BR, ONDER = 70, 70, 560
STAAF = {}
for i, (naam, z) in enumerate(ZETELS):
    x = X0 + i * 75
    h = z * 18
    kleur = LICHTGROEN if naam in NL else (GRIJS if naam == "PVDA-PTB" else "#f1d9b5")
    ZK.rect(x, ONDER - h, 55, h, kleur, DONKER, 4, 2)
    ZK.tekst(x + 27, ONDER - h - 10, str(z), 18, vet=True)
    ZK.svg(f'<text x="{x + 30}" y="{ONDER + 18}" font-size="15" text-anchor="end" fill="#24331b" transform="rotate(-35 {x + 30} {ONDER + 18})">{naam.replace("&", "&amp;")}</text>')
    STAAF[naam] = (x, ONDER - h, h)
ZK.lijn(60, ONDER, 960, ONDER, DONKER, 2)
ZK.rect(650, 70, 24, 18, LICHTGROEN, DONKER, 3, 1)
ZK.tekst(682, 85, "Nederlandstalig", 16, "start")
ZK.rect(800, 70, 24, 18, "#f1d9b5", DONKER, 3, 1)
ZK.tekst(832, 85, "Franstalig", 16, "start")
ZK.rect(650, 98, 24, 18, GRIJS, DONKER, 3, 1)
ZK.tekst(682, 113, "nationale partij", 16, "start")


def staaf(naam):
    x, y, h = STAAF[naam]
    return [Prent.zone(x - 8, y - 35, 71, h + 70)]


# Links-rechtsas --------------------------------------------------------------------
LR = Prent("links-rechts-as", "De sociaal-economische links-rechtsas (vereenvoudigd)",
           "een lange pijl van links naar rechts met drie lege vakken A (links), B (midden) en C (rechts); links staat 'meer herverdeling, sterke overheid', rechts 'meer vrije markt, minder belastingen'")
LR.pijl(80, 300, 920, 300, DONKER, 4)
LR.pijl(920, 300, 80, 300, DONKER, 4)
LR.tekst(90, 250, "links", 24, "start", vet=True)
LR.tekst(910, 250, "rechts", 24, "end", vet=True)
LR.tekst(90, 380, "meer herverdeling,", 18, "start")
LR.tekst(90, 404, "sterke overheid", 18, "start")
LR.tekst(910, 380, "meer vrije markt,", 18, "end")
LR.tekst(910, 404, "minder belastingen", 18, "end")
AS = {"A": 270, "B": 500, "C": 730}
for k, x in AS.items():
    LR.rect(x - 70, 250, 140, 100, "#ffffff", DONKER, 12, 2)
    LR.letter(x, 300, k)
LR.tekst(500, 520, "Een partij kan per thema anders staan. De as is een vereenvoudiging.", 17)


def plek(k):
    return [Prent.zone(AS[k] - 70, 250, 140, 100)]


VRAGEN = [
    klik("Klik op de grootste partij in de Kamer na de verkiezingen van 9 juni 2024.", ZK.bestand, staaf("N-VA"),
         "N-VA haalde 24 zetels. Dat is veel minder dan de 76 die nodig zijn voor een meerderheid."),
    klik("Klik op de grootste Franstalige partij.", ZK.bestand, staaf("MR"),
         "MR haalde 20 zetels, evenveel als Vlaams Belang, en is de grootste aan Franstalige kant."),
    klik("Klik op de enige partij in de grafiek die zowel in Vlaanderen als in Wallonië en Brussel opkomt onder één naam.", ZK.bestand, staaf("PVDA-PTB"),
         "PVDA-PTB is een nationale partij. De andere partijen zijn Nederlandstalig of Franstalig."),
    met_prent(ZK.bestand, inv("Hoeveel zetels halen N-VA, MR, Les Engagés, Vooruit en cd&v samen?", ["82"],
              "24 + 20 + 14 + 13 + 11 = 82. Dat is meer dan 76, dus samen een meerderheid.")),
    met_prent(ZK.bestand, mk("Wat leer je uit deze grafiek over de regeringsvorming?",
              ["geen enkele partij kan alleen een meerderheid vormen",
               "de grootste partij krijgt meteen alle ministers in de regering",
               "enkel Nederlandstalige partijen mogen de regering vormen",
               "de kleinste partij beslist wie eerste minister wordt"], 0,
              "De grootste partij heeft maar 24 van de 150 zetels. Er is dus een coalitie van meerdere partijen nodig.")),
    met_prent(ZK.bestand, keuze("Dat er zoveel partijen in de Kamer zitten, komt mee door het kiesstelsel van [[*evenredige vertegenwoordiging|het meerderheidsstelsel|de cijnskiezing]].",
              "Bij evenredige vertegenwoordiging krijgen ook kleinere partijen zetels.")),
    klik("Klik op het vak waar een partij staat die vooral meer herverdeling en een sterke overheid wil.", LR.bestand, plek("A"),
         "Links op de sociaal-economische as staan partijen die meer herverdeling willen."),
    klik("Een partij wil vooral lagere belastingen en minder overheid in de economie. Klik waar ze op de as staat.", LR.bestand, plek("C"),
         "Rechts op de sociaal-economische as staan partijen die meer vrije markt willen."),
    met_prent(LR.bestand, keuze("cd&v wordt op deze as gewoonlijk geplaatst in vak [[*B|A|C]], PVDA in vak [[*A|B|C]].",
              "cd&v staat gewoonlijk in het centrum, PVDA het verst links. Dat is een ruwe indeling.")),
    koppel("Koppel de Vlaamse partij aan de ideologie waartoe ze gewoonlijk gerekend wordt.", [
        ["Open Vld", "liberalisme"],
        ["Vooruit", "sociaaldemocratie"],
        ["Groen", "ecologisme"],
        ["cd&v", "christendemocratie"],
        ["N-VA", "Vlaams-nationalisme"],
    ], ["monarchisme"], "Elke partij met haar ideologische familie."),
    tabel("Welke breuklijn zie je in dit conflict?", [
        ("Werkgevers en vakbonden zijn het oneens over de loonsverhoging.", "sociaal-economisch"),
        ("Er is ruzie over subsidies voor katholieke en officiële scholen.", "levensbeschouwelijk"),
        ("Nederlandstaligen en Franstaligen zijn het oneens over de taal van de rand rond Brussel.", "communautair"),
    ], "Arbeid tegenover kapitaal, kerk tegenover staat, en taal en identiteit.",
       kolommen=["sociaal-economisch", "levensbeschouwelijk", "communautair"]),
    keuze("Een samenhangend geheel van ideeën over hoe de samenleving moet zijn, is een [[*ideologie|breuklijn|coalitie]].",
          "Liberalisme, socialisme en ecologisme zijn ideologieën."),
    sorteer("Bij welk criterium van het verkiezingsproces hoort dit?", ["Actoren", "Informatie", "Mechanismen"], [
        ["een vakbond die haar leden oproept", "Actoren"],
        ["een peiling in de krant", "Informatie"],
        ["de regels over campagnegeld", "Mechanismen"],
        ["een debat op televisie", "Informatie"],
        ["de kiezers", "Actoren"],
        ["de stemprocedure", "Mechanismen"],
    ], "Wie speelt mee, wat hoort of leest de kiezer, en welke regels gelden."),
    casus(
        "In het land Arvel zijn er 100 zetels. Partij Zon gaat van 30 naar 22 zetels, partij Maan van 18 naar 27, "
        "partij Ster blijft op 25 en partij Wolk gaat van 27 naar 26. Zon en Wolk regeerden samen, maar hebben nu geen meerderheid meer.",
        [
            inv("Hoeveel zetels hebben Zon en Wolk nu samen?", ["48"],
                "22 + 26 = 48. Dat is minder dan 51, dus geen meerderheid meer."),
            keuze("De grootste winnaar is partij [[*Maan|Ster|Wolk]], de grootste verliezer partij [[*Zon|Wolk|Ster]].",
                  "Maan wint 9 zetels, Zon verliest er 8."),
            mk("Welke combinatie van twee partijen heeft nu een meerderheid?",
               ["Maan en Wolk", "Zon en Ster", "Zon en Wolk opnieuw", "Zon en Maan"], 0,
               "27 + 26 = 53. Zon en Ster hebben 47, Zon en Wolk 48 en Zon en Maan 49."),
            keuze("Dat de machtsverhoudingen zo veranderen, noem je een politieke [[*verschuiving|breuklijn|ideologie]].",
                  "Winst en verlies van zetels verschuift de macht in het parlement."),
        ],
    ),
    tabel("Klopt dit over peilingen?", [
        ("Een peiling is een schatting bij een steekproef van kiezers.", J),
        ("Een peiling heeft dezelfde waarde als de officiële uitslag.", F),
        ("Een peiling kan het gedrag van kiezers beïnvloeden.", J),
        ("Een peiling is een regel uit de kieswetgeving.", F),
    ], "Een peiling is informatie, geen uitslag en geen regel."),
    mk("Een partij komt op voor een sterke sociale zekerheid, hogere minimumlonen en meer rechten voor werknemers. Welke ideologie past daar het best bij?",
       ["de sociaaldemocratie",
        "het liberalisme",
        "het Vlaams-nationalisme",
        "het ecologisme"], 0,
       "Gelijkheid en solidariteit via de overheid en de rechten van werknemers zijn kernideeën van het socialisme en de sociaaldemocratie."),
    mk("Een partij wil dat Vlaanderen zoveel mogelijk zelf beslist over belastingen, onderwijs en werk. Welke ideologie past daar het best bij?",
       ["het Vlaams-nationalisme",
        "het internationale socialisme",
        "het ecologisme",
        "de sociaaldemocratie"], 0,
       "Meer zelfbestuur voor het eigen volk is een kernidee van het nationalisme."),
    keuze("Een partij die economisch eerder rechts is, kan bij ethische thema's [[*progressief|altijd conservatief|nooit een standpunt]] zijn.",
          "Daarom is één links-rechtsas een vereenvoudiging."),
    volgorde("Zet de stappen na de verkiezingen in een logische volgorde.", [
        "de stemmen worden geteld en omgezet in zetels",
        "partijen verkennen welke coalitie mogelijk is",
        "de coalitiepartijen schrijven een regeerakkoord",
        "de nieuwe regering legt de eed af",
    ], "Eerst de uitslag, dan onderhandelen, dan het akkoord en dan de regering."),
    inv("Hoeveel zetels heb je minstens nodig voor een meerderheid in een parlement van 124 zetels, zoals het Vlaams Parlement?", ["63"],
        "De helft van 124 is 62. Een meerderheid is minstens 63."),
    sleep("Over het arbeidsloon en de winst botsen [[arbeid]] en [[kapitaal]]. Over de rol van de kerk in het onderwijs botsen kerk en [[staat]].",
          ["taal", "natie"], "De sociaal-economische en de levensbeschouwelijke breuklijn."),
    tabel("Is dit een identificatie, een actor of een verkiezingsresultaat?", [
        ("Het gaat om de verkiezing van het Europees Parlement.", "identificatie"),
        ("Partij X verliest vijf zetels en gaat in de oppositie.", "resultaat"),
        ("Een milieuorganisatie vergelijkt de klimaatplannen van de partijen.", "actor"),
    ], "Over welk niveau het gaat, wie meespeelt, en wat de uitslag is.",
       kolommen=["identificatie", "actor", "resultaat"]),
    keuze("Linkse en rechtse partijen in dezelfde regering kunnen botsen over belastingen. Dat leidt vaak tot [[*een compromis of uitstel|een nieuwe grondwet|de afschaffing van de verkiezingen]].",
          "Beleidsconflicten tussen links en rechts kunnen beslissingen vertragen."),
    mk("Waarom is een partij die het meeste stemmen haalt, niet altijd de partij met de meeste macht?",
       ["macht hangt af van de coalitie die er gevormd kan worden",
        "de grondwet verbiedt dat de grootste partij een minister levert",
        "stemmen worden in België niet omgezet in zetels",
        "de kleinste partij krijgt altijd de eerste minister"], 0,
       "Wie samen een meerderheid vindt, regeert. De grootste partij kan zelfs in de oppositie belanden."),
    tabel("Klopt dit over ideologieën?", [
        ("Het liberalisme legt de nadruk op de vrijheid van het individu en de vrije markt.", J),
        ("Het ecologisme stelt de zorg voor het milieu en de toekomstige generaties centraal.", J),
        ("De christendemocratie wil dat de kerk de wetten maakt.", F),
        ("Het socialisme wil dat de overheid zich zo weinig mogelijk met de economie bemoeit.", F),
    ], "De christendemocratie steunt op christelijke waarden, maar de wetten maakt het parlement. Minder overheid in de economie is een liberaal idee."),
    keuze("Een groep partijen die samen een meerderheid vormt en de regering levert, noem je de [[*coalitie|oppositie|breuklijn]]. De partijen die niet in de regering zitten, vormen de [[*oppositie|coalitie|kieskring]].",
          "De coalitie regeert, de oppositie controleert en stelt alternatieven voor."),
    open_("Leg uit hoe structurele breuklijnen de regeringsvorming in België moeilijker maken. Gebruik een voorbeeld.",
          "Partijen zijn ontstaan rond breuklijnen zoals arbeid tegenover kapitaal, kerk tegenover staat en Nederlandstaligen tegenover Franstaligen. Een coalitie moet partijen verzoenen die op die breuklijnen tegenover elkaar staan. Een linkse partij wil bijvoorbeeld meer belastingen op vermogen, een rechtse minder belastingen. Bovendien moeten er partijen uit beide taalgroepen in de federale regering zitten, die ook over de staatsstructuur anders denken. Daarom zijn de onderhandelingen vaak lang en eindigen ze in compromissen."),
]

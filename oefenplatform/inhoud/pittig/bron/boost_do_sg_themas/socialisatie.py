"""Socialisatie, enculturatie en acculturatie — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_socialisatie: het begrip, het belang voor
individu en samenleving, de drie niveaus en de vormen acculturatie,
anticiperende socialisatie en enculturatie. Met een zelfgetekend
kringenschema."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, ROOD, BLAUW, LICHTGROEN, ORANJE

KR = Prent("drie-kringen-socialisatie", "Drie kringen rond een kind", "drie kringen rond elkaar met een tekening, letters A tot C")
KR.ellips(500, 340, 440, 280, "#f3efe2", DONKER, 3)
KR.ellips(500, 340, 300, 190, "#e4ecd8", DONKER, 3)
KR.ellips(500, 340, 150, 95, "#ffffff", DONKER, 3)
# kind in het midden
KR.cirkel(500, 320, 16, GRIJS, DONKER, 2); KR.rect(488, 336, 24, 34, GRIJS, DONKER, 6, 2)
# huisje in de binnenste kring
KR.pad("M 400 330 L 430 300 L 460 330 Z", ROOD, DONKER, 2); KR.rect(407, 330, 46, 36, "#ffffff", DONKER, 0, 2)
# schoolgebouw in de middelste kring
KR.rect(255, 300, 80, 60, "#ffffff", DONKER, 0, 2); KR.pad("M 250 300 L 295 270 L 340 300 Z", BLAUW, DONKER, 2)
for i in range(3):
    KR.rect(262 + i * 25, 315, 16, 16, "#cfe3f0", DONKER, 0, 1)
# gsm en tv in de buitenste kring
KR.rect(118, 300, 40, 70, DONKER, DONKER, 6, 2); KR.rect(123, 307, 30, 50, "#9ec7e6", "none", 0, 0)
KR.rect(820, 300, 90, 60, DONKER, DONKER, 4, 2); KR.rect(827, 306, 76, 46, "#9ec7e6", "none", 0, 0); KR.lijn(865, 360, 865, 375, DONKER, 3); KR.lijn(845, 377, 885, 377, DONKER, 3)
KR.letter(540, 290, "A"); KR.letter(670, 200, "B"); KR.letter(800, 130, "C")
U = "drie-kringen-socialisatie.svg"
Z = {"A": [Prent.zone(360, 250, 280, 180)], "B": [Prent.zone(205, 200, 140, 280), Prent.zone(655, 200, 140, 280), Prent.zone(350, 155, 300, 85), Prent.zone(350, 440, 300, 85)], "C": [Prent.zone(65, 180, 135, 320), Prent.zone(805, 180, 130, 320), Prent.zone(250, 65, 500, 80), Prent.zone(250, 535, 500, 80)]}

AMIR = ("Lees het verhaal.\n\n"
        "Amir (14) kwam twee jaar geleden met zijn ouders uit Syrië naar Mechelen. Thuis spreken ze Arabisch en vieren ze het Suikerfeest, zoals Amir het van kleins af leerde. "
        "Op school leerde hij Nederlands en nu viert hij ook Sinterklaas mee met zijn klas. Amir wil later verpleegkundige worden: hij kijkt filmpjes over het beroep en vraagt zijn tante, die verpleegkundige is, hoe het er in een ziekenhuis aan toegaat. "
        "Zijn jongere zusje leert haar ouders ondertussen hoe ze de app van de school moeten gebruiken.")

VRAGEN = [
    klik("Bekijk de drie kringen. Klik op de kring van de primaire socialisatie.", U, Z["A"], "Het gezin: de eerste en diepste socialisatie."),
    klik("Klik op de kring van de secundaire socialisatie.", U, Z["B"], "School, vrienden en werk."),
    klik("Klik op de kring van de tertiaire socialisatie.", U, Z["C"], "Media en andere kanalen, zonder rechtstreeks contact."),
    casus(AMIR, [
        sorteer("Welke vorm van socialisatie zie je?", ["enculturatie", "acculturatie", "anticiperende socialisatie"],
                [("Het Suikerfeest vieren zoals hij het van kleins af leerde.", "enculturatie"), ("Sinterklaas meevieren met zijn klas.", "acculturatie"), ("Zich verdiepen in het beroep van verpleegkundige.", "anticiperende socialisatie")],
                "Je eigen cultuur, een andere cultuur, en een rol die nog komt."),
        keuze("Dat Amirs zusje haar ouders de schoolapp leert gebruiken, toont dat socialisatie [[*tweerichtingsverkeer|eenrichtingsverkeer]] is.", "Ook jongeren geven iets door."),
        keuze("De filmpjes over het beroep horen bij de [[*tertiaire|primaire|secundaire]] socialisatie.", "Media, op afstand."),
        mk("Wat toont het verhaal van Amir over socialisatie?",
           ["ze loopt een leven lang door", "ze stopt helemaal als je naar een ander land verhuist", "ze gebeurt alleen in het gezin en nergens anders", "ze is aangeboren en verandert dus nooit meer"],
           0, "Ook op latere leeftijd leer je nieuwe normen."),
    ]),
    koppel("Koppel het niveau aan het voorbeeld.",
           [("primaire socialisatie", "een kind leert thuis dankjewel zeggen"), ("secundaire socialisatie", "een leerling leert op school zijn vinger opsteken"), ("tertiaire socialisatie", "een tiener leert via YouTube hoe je je kleedt voor een sollicitatie")],
           ["een baby krijgt blauwe ogen"], "Gezin, school en media."),
    tabel("Klopt dit over socialisatie?",
          [("Socialisatie stopt na de kindertijd.", F), ("De primaire socialisatie is de diepste.", J), ("De drie niveaus kunnen tegelijk werken.", J), ("Tertiaire socialisatie vraagt rechtstreeks contact.", F)],
          "Socialisatie loopt het hele leven door."),
    mk("Stel dat ouders, school en media niets meer zouden doorgeven aan kinderen. Wat zou er met de samenleving gebeuren?",
       ["de gedeelde afspraken verdwijnen", "omdat iedereen anders dezelfde genen krijgt", "omdat er anders te veel scholen zouden zijn", "omdat een samenleving geen waarden nodig heeft"],
       0, "Elke generatie moet de afspraken opnieuw leren."),
    sorteer("Prosociaal of antisociaal gedrag bij deze jongeren?", ["prosociaal", "antisociaal"],
            [("een oudere dame helpen met haar boodschappen", "prosociaal"), ("graffiti spuiten op het schoolgebouw", "antisociaal"), ("je boterham delen met wie de zijne vergat", "prosociaal")],
            "Een gevolg van geslaagde of mislukte socialisatie."),
    keuze("Opvoeding is bewust en gericht. Socialisatie is [[*breder|smaller]]: ze gebeurt ook ongemerkt.", "Via voorbeeld, sfeer en media."),
    keuze("De school heet secundaire socialisatie omdat ze [[*na het gezin komt|tweederangs is|minder belangrijk is]].", "Secundair betekent hier tweede in de tijd."),
    mk("Een tiener hoort thuis iets anders dan in zijn vriendengroep. Waarom kan dat spanning geven?",
       ["de niveaus spreken elkaar tegen", "omdat hij dan helemaal niet gesocialiseerd wordt", "omdat vrienden geen invloed hebben op normen", "omdat de primaire socialisatie dan stopt"],
       0, "Hij moet zelf kiezen en wegen."),
    tabel("Wordt dit doorgegeven bij socialisatie?",
          [("waarden", J), ("normen", J), ("andere cultuuruitingen", J), ("je bloedgroep", F)],
          "Erfelijke aanleg krijg je mee bij de geboorte."),
    keuze("Een kind doet zijn oudere broer na die naar het middelbaar gaat. Dat is [[*anticiperende socialisatie|enculturatie|acculturatie]].", "Hij oefent een rol die hij nog niet heeft."),
    keuze("Enculturatie en acculturatie betekenen [[*niet hetzelfde|hetzelfde]].", "Je eigen cultuur binnenkrijgen tegenover een andere overnemen."),
    mk("Oma leerde haar normen vooral thuis en in de kerk, haar kleinzoon vooral thuis en via zijn gsm. Wat toont dat?",
       ["de rol van instituties is verschoven", "omdat grootouders nooit gesocialiseerd werden", "omdat tieners vandaag geen gezin meer hebben", "omdat de school vroeger niet bestond"],
       0, "Media wegen zwaarder, de kerk lichter."),
    sleep("Socialisatie is het [[doorgeven]] en overnemen van [[waarden]], normen en andere cultuuruitingen. Ze loopt een heel [[leven]] lang.",
          ["erven", "jaar"], "Cultuur leren en doorgeven."),
    inv("Een kind leert van kleins af de feesten en gewoontes van zijn eigen groep, zonder het te merken. Hoe heet die vorm van socialisatie? Eén woord.", ["enculturatie"], "Je eigen cultuur binnenkrijgen."),
    tabel("Is dit een vorm van socialisatie?",
          [("acculturatie", J), ("anticiperende socialisatie", J), ("enculturatie", J), ("collectivisatie", F)],
          "Drie vormen."),
    keuze("Binnen dezelfde cultuur legt het ene gezin de nadruk op zelfstandigheid, het andere op [[*samenhorigheid|lengte|bloedgroep]]. Socialisatie verschilt per gezin.", "Elk gezin heeft eigen waarden."),
    keuze("Een kind neemt [[*niet zomaar alles|altijd alles]] over wat het via socialisatie meekrijgt: het kiest en weegt.", "Zeker in de adolescentie."),
    tabel("Hoort dit bij anticiperende socialisatie?",
          [("ze gaat over een toekomstige rol", J), ("ze gebeurt voor de rol begint", J), ("ze maakt de overgang makkelijker", J), ("ze gaat over je eigen cultuur als baby", F)],
          "Je bereidt je voor op wat komt."),
    keuze("Een gezin uit Marokko viert in België ook Sinterklaas mee. Dat is [[*acculturatie|enculturatie|tertiaire socialisatie]].", "Gewoontes van de nieuwe omgeving komen erbij."),
    tabel("Klopt dit over enculturatie en acculturatie?",
          [("Ze gaat via meer dan één groep.", J), ("Ze zorgt dat een cultuur blijft bestaan.", J), ("Ze helpt je aanpassen aan je omgeving.", J), ("Ze gebeurt alleen bewust.", F)],
          "Ze gebeurt ook ongemerkt."),
    keuze("Iemand begint een nieuwe job en leert hoe het er op het werk aan toegaat. Dat is [[*secundaire|primaire|tertiaire]] socialisatie.", "School, vrienden en werk."),
    mk("Een kind leert thuis en op school wat wel en niet kan. Wat levert dat het kind zelf op?",
       ["aanpassing aan de omgeving", "een betere gezondheid en een langer leven", "een hogere intelligentie dan zijn ouders", "een vaste plaats in de dominante cultuur"],
       0, "Je leert wat kan en wat niet."),
    keuze("Cultuur is [[*wat|hoe]] doorgegeven wordt; socialisatie is hoe dat gebeurt.", "Daarom horen ze samen."),
    open_("Leg met een eigen voorbeeld uit hoe de primaire en de secundaire socialisatie elkaar kunnen aanvullen of tegenspreken.",
          "Bijvoorbeeld: thuis leer ik dat je volwassenen met 'u' aanspreekt (primair). Op school spreken veel leerlingen de leerkracht met 'jij' aan (secundair). Dat spreekt elkaar tegen, en ik moet zelf kiezen wat ik in welke situatie doe."),
]

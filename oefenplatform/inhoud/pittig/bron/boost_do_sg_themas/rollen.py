"""Sociale positie, sociale rol en rollenconflicten — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_rollen: positie, rol en status, toegewezen of
verworven en tijdelijk of levenslang, rollenset en rolverwachtingen, interne
en externe rollenconflicten. Met een zelfgetekende weekagenda."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, ROOD, BLAUW, LICHTGROEN

AG = Prent("weekagenda-sara", "De weekagenda van Sara: leerkracht, trainer en mama", "een agenda met vier dagen, letters A tot D")
DAG = [("A", "maandag", ["8u-12u: lesgeven", "in het 3de jaar"]),
       ("B", "dinsdag", ["14u: de directie wil", "strengere punten,", "mijn leerlingen vragen", "net meer kansen"]),
       ("C", "woensdag", ["15u: training geven", "bij de voetbalclub", "15u: met zoon naar", "de tandarts"]),
       ("D", "donderdag", ["19u: avondcursus", "Spaans volgen"])]
for i, (t, naam, regels) in enumerate(DAG):
    x = 30 + i * 240
    AG.rect(x, 70, 220, 470, "#ffffff", DONKER, 8, 3)
    AG.rect(x, 70, 220, 50, "#dfe9d2", DONKER, 8, 3)
    AG.tekst(x + 110, 104, naam, 22, vet=True)
    for k in range(7):
        AG.lijn(x + 10, 170 + k * 50, x + 210, 170 + k * 50, "#e4e1d6", 1)
    for k, r in enumerate(regels):
        AG.tekst(x + 18, 160 + k * 34, r, 18, "start")
    AG.letter(x + 110, 580, t)
U = "weekagenda-sara.svg"
Z = {t: [Prent.zone(30 + i * 240, 70, 220, 540)] for i, (t, n, r) in enumerate(DAG)}

ADAM = ("Lees de voorstelling.\n\n"
        "Adam is 19. Hij is de oudste zoon van een Belgisch-Marokkaans gezin, studeert verpleegkunde en werkt in het weekend als jobstudent in een supermarkt. "
        "Sinds dit jaar is hij voor twee jaar verkozen als voorzitter van de studentenraad. Vrijdagavond heeft de studentenraad een belangrijke vergadering, "
        "maar zijn baas vraagt dat hij die avond inspringt in de winkel.")

VRAGEN = [
    klik("Bekijk de agenda van Sara. Klik op de dag met een extern rollenconflict.", U, Z["C"], "Twee verschillende posities, trainer en moeder, botsen."),
    klik("Klik op de dag met een intern rollenconflict.", U, Z["B"], "Binnen één positie, leerkracht, botsen verwachtingen van directie en leerlingen."),
    klik("Klik op de dag waarop Sara een vierde positie inneemt, naast leerkracht, trainer en mama.", U, Z["D"], "Cursist: een verworven positie die ze zelf koos."),
    casus(ADAM, [
        sorteer("Toegewezen of verworven positie?", ["toegewezen", "verworven"],
                [("oudste zoon", "toegewezen"), ("student verpleegkunde", "verworven"), ("jobstudent", "verworven"), ("Belgisch-Marokkaanse afkomst", "toegewezen")],
                "Wat je niet koos tegenover wat je zelf behaalde."),
        keuze("Voorzitter van de studentenraad voor twee jaar is een positie die verworven en [[*tijdelijk|levenslang]] is.", "Hij kreeg ze door verkiezing, voor een beperkte tijd."),
        keuze("Vrijdagavond botsen voorzitter en jobstudent. Dat is een [[*extern|intern]] rollenconflict.", "Twee verschillende posities."),
        mk("Wat kan Adam doen met dat rollenconflict?",
           ["prioriteiten stellen en afspraken maken", "zijn positie als oudste zoon opgeven", "ruzie maken met zijn baas zodat het opgelost is", "niets doen, want een rollenconflict lost zich altijd vanzelf op"],
           0, "Kiezen wat voorgaat, afspraken maken of een rol tijdelijk afbouwen."),
    ]),
    koppel("Koppel het begrip over sociale rollen aan de uitleg.",
           [("sociale positie", "de plaats die je inneemt"), ("sociale rol", "het gedrag dat van je verwacht wordt"), ("sociale status", "het aanzien bij een positie"), ("rollenset", "alle rollen bij één positie")],
           ["de cultuur van de meerderheid"], "Positie, rol en status horen samen."),
    sorteer("Intern of extern rollenconflict?", ["intern", "extern"],
            [("Een verpleegkundige wil tijd nemen voor een patiënt, maar moet ook snel werken.", "intern"), ("Een student werkt in het weekend en kan daardoor niet studeren.", "extern"), ("Een trainer moet zijn eigen zoon op de bank zetten.", "extern"), ("Een scheidsrechter moet streng zijn maar wil ook de sfeer goed houden.", "intern")],
            "Binnen één positie of tussen twee posities."),
    tabel("Klopt dit over sociale rollen?",
          [("Positie en rol betekenen hetzelfde.", F), ("Iedereen heeft maar één sociale positie.", F), ("Een rolverwachting kan per groep verschillen.", J), ("Een rollenconflict betekent ruzie met een ander.", F)],
          "Het gaat over botsende verwachtingen."),
    tabel("Is deze positie levenslang?",
          [("zoon zijn", J), ("leerling zijn", F), ("dochter zijn", J), ("voorzitter van een club zijn", F)],
          "Familiebanden verdwijnen niet."),
    mk("Waarom verandert de rol van een vader in de loop van de tijd?",
       ["de verwachtingen verschuiven", "omdat de positie vader verdwijnt", "omdat vaders vroeger geen positie hadden", "omdat rollen aangeboren zijn"],
       0, "Wat men in 1960 van een vader verwachtte, verschilt van nu."),
    keuze("Een leerkracht wordt geacht eerlijk te verbeteren. Dat is een [[*rolverwachting|toegewezen positie|status]].", "Wat men van iemand in die positie verwacht."),
    tabel("Hoort dit bij de rollenset van een leerkracht?",
          [("tegenover de leerlingen", J), ("tegenover de ouders", J), ("tegenover de directie", J), ("tegenover de bakker in zijn straat", F)],
          "Alle rollen bij die ene positie."),
    mk("Waarom komen rollenconflicten vandaag vaker voor dan vroeger?",
       ["mensen hebben meer posities tegelijk", "omdat mensen vroeger geen rollen hadden", "omdat er vroeger geen verwachtingen waren", "omdat rollenconflicten pas sinds kort bestaan"],
       0, "Werken, studeren, zorgen en vrijwilligerswerk lopen vaker door elkaar."),
    keuze("Wat toegewezen is, ligt vast. Wat [[*verworven|toegewezen|levenslang]] is, hangt af van je eigen inzet.", "Daarom is die indeling nuttig."),
    sleep("Bij elke [[positie]] hoort een [[rol]] en een [[status]].",
          ["cultuur", "groep"], "Drie begrippen die samenhoren."),
    keuze("De verwachtingen van de groep vormen samen de [[*rol|positie|afkomst]].", "Een rolverwachting komt van anderen."),
    inv("Een arts heeft rollen tegenover patiënten, verpleegkundigen, familie en het ziekenhuis. Hoe noem je dat geheel? Eén woord.", ["rollenset", "de rollenset"], "Alle rollen bij één positie."),
    tabel("Is deze positie toegewezen?",
          [("zestien jaar zijn", J), ("jongste van het gezin zijn", J), ("verpleegkundige zijn", F), ("kapitein van de ploeg zijn", F)],
          "Toegewezen posities kies je niet."),
    keuze("Een moeder moet werken en tegelijk haar ziek kind verzorgen. Dat is een [[*extern|intern]] rollenconflict.", "Werknemer en moeder botsen."),
    mk("Waarom benoem je in een voorbeeld welke posities botsen?",
       ["zo wordt een vage spanning duidelijk", "zo verdwijnt het rollenconflict meteen", "zo weet je wie er gelijk heeft", "zo kan je de status van iemand berekenen"],
       0, "Door de posities te benoemen, wordt de spanning een helder probleem."),
    keuze("Je kan een rol [[*op je eigen manier|helemaal niet]] invullen, maar de verwachtingen blijven er.", "Rolverwachtingen komen van de groep."),
    tabel("Is dit een positie?",
          [("buur", J), ("collega", J), ("eerlijk verbeteren", F), ("leerling", J)],
          "Eerlijk verbeteren is een rolverwachting."),
    keuze("Iemand wordt na jaren studeren advocaat. Dat is een [[*verworven|toegewezen]] positie.", "Het resultaat van eigen inspanning."),
    tabel("Kan je dit doen bij een rollenconflict?",
          [("prioriteiten stellen", J), ("afspraken maken", J), ("een rol tijdelijk afbouwen", J), ("doen alsof het niet bestaat en hopen dat het verdwijnt", F)],
          "Het conflict verdwijnt zelden vanzelf."),
    keuze("Bij de positie leerling hoort de rol: op tijd komen, taken maken en [[*luisteren|lesgeven|punten geven]].", "Het verwachte gedrag."),
    mk("Een positie en de rolverwachtingen: hoe hangen ze samen?",
       ["bij elke positie horen verwachtingen", "een positie staat volledig los van verwachtingen", "verwachtingen bestaan enkel bij levenslange posities", "alleen toegewezen posities hebben verwachtingen"],
       0, "Samen vormen ze de rol."),
    keuze("Sara is leerkracht, trainer en moeder tegelijk. Ze heeft [[*meerdere posities|één positie|geen positie]].", "Samen vormen die posities haar plaats in de samenleving."),
    open_("Beschrijf een rollenconflict uit je eigen leven of omgeving. Zeg of het intern of extern is en welke posities of verwachtingen botsen.",
          "Bijvoorbeeld: ik ben leerling en speler in een voetbalploeg. Op zaterdag heb ik een belangrijke match, maar maandag een examen waarvoor ik moet studeren. Dat is een extern rollenconflict: de positie leerling botst met de positie speler."),
]

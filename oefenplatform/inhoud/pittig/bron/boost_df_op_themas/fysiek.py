"""De fysieke en motorische ontwikkeling — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_fysiek: groeicurves, de groeiprincipes, de groeispurt, de
zintuigen van de baby, de babyreflexen, grove en fijne motoriek en de
sensomotorische ontwikkeling. Met een zelfgetekende groeicurve."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, ROOD, assen

GC = Prent("groeicurve-noah", "Groeicurve van Noah", "een groeicurve met drie percentiellijnen en de metingen van één kind, letters A tot C")
X, Y = assen(GC, 0, 18, 40, 200, "leeftijd (jaar)", "lengte (cm)", 2, 20)
LIJNEN = {"P97": [(0, 54), (1, 80), (2, 93), (4, 111), (6, 125), (8, 138), (10, 149), (12, 162), (14, 177), (16, 186), (18, 189)],
          "P50": [(0, 50), (1, 75), (2, 87), (4, 103), (6, 116), (8, 128), (10, 138), (12, 149), (14, 163), (16, 173), (18, 177)],
          "P3": [(0, 46), (1, 70), (2, 81), (4, 95), (6, 107), (8, 118), (10, 127), (12, 136), (14, 149), (16, 160), (18, 165)]}
for naam, pts in LIJNEN.items():
    GC.pad("M " + " L ".join(f"{X(a):.0f} {Y(b):.0f}" for a, b in pts), "none", GRIJS if naam != "P50" else "#9a9480", 3)
    GC.tekst(X(18) + 8, Y(pts[-1][1]) + 5, naam, 15, "start")
NOAH = [(0, 50), (1, 75), (2, 87), (4, 103), (6, 116), (8, 128), (9, 129), (10, 131), (11, 134), (12, 139), (13, 149), (14, 161), (15, 168), (16, 172)]
GC.pad("M " + " L ".join(f"{X(a):.0f} {Y(b):.0f}" for a, b in NOAH), "none", BLAUW, 4)
for a, b in NOAH:
    GC.cirkel(X(a), Y(b), 5, BLAUW, BLAUW, 1)
LET = {"A": (4, 103, -40, -30), "B": (10, 131, 30, 35), "C": (13.5, 155, -45, -10)}
Z = {}
for t, (a, b, dx, dy) in LET.items():
    GC.letter(X(a) + dx, Y(b) + dy, t)
    Z[t] = [Prent.rond(X(a) + dx, Y(b) + dy, 30), Prent.rond(X(a), Y(b), 30)]
U = "groeicurve-noah.svg"

SITUATIE = ("Lees de situatie.\n\n"
            "Elias is twaalf. Op een half jaar tijd werd hij acht centimeter langer. Hij stoot vaak tegen dingen en laat dingen vallen, "
            "en zijn klasgenoten lachen met zijn lange benen. Zijn beste vriend is nog even klein als vorig jaar.")

VRAGEN = [
    klik("Bekijk de groeicurve. Klik op de letter waar Noah duidelijk afwijkt van de lijn die hij altijd volgde.", U, Z["B"], "Tot acht jaar volgt hij P50; daarna zakt hij weg richting P3."),
    klik("Klik op de letter bij een groeispurt.", U, Z["C"], "In korte tijd wordt Noah veel langer: de lijn gaat steil omhoog."),
    klik("Klik op de letter waar Noah gewoon zijn verwachte lijn volgt.", U, Z["A"], "Op vier jaar zit hij mooi op P50."),
    volgorde("Zet deze mijlpalen van de grove motoriek in de volgorde waarin ze meestal komen.",
             ["het hoofd optillen", "rollen", "zitten", "kruipen", "stappen"],
             "Van kop naar staart: eerst het hoofd, dan de romp, dan de benen."),
    sorteer("Grove of fijne motoriek?", ["grove motoriek", "fijne motoriek"],
            [("kruipen", "grove motoriek"), ("een erwtje oppakken", "fijne motoriek"), ("een bal trappen", "grove motoriek"), ("een tekening inkleuren", "fijne motoriek"), ("een knoop dichtdoen", "fijne motoriek"), ("de trap op lopen", "grove motoriek")],
            "Grote bewegingen van armen, benen en romp tegenover precieze bewegingen van handen en vingers."),
    tabel("Welk groeiprincipe zie je?",
          [("Een baby houdt eerst zijn hoofd rechtop en kan pas later staan.", "van kop naar staart"), ("Een baby beweegt eerst zijn schouders goed en pas later zijn vingers.", "van midden naar buiten"), ("Een kind grijpt eerst met de hele hand en later met twee vingers.", "van grof naar fijn")],
          "Drie groeiprincipes, drie richtingen.", ["van kop naar staart", "van midden naar buiten", "van grof naar fijn"]),
    koppel("Koppel de babyreflex aan wat er gebeurt.",
           [("zuigreflex", "de baby zuigt als je zijn mond aanraakt"), ("grijpreflex", "het handje sluit zich rond je vinger"), ("zoekreflex", "de baby draait zijn hoofd naar een aanraking op zijn wang"), ("schrikreflex", "de baby gooit zijn armen open bij een plots geluid")],
           ["de baby leest een prentenboek"],
           "Een leesreflex bestaat niet."),
    casus(SITUATIE, [
        keuze("Elias zit in een [[*groeispurt|groeicurve|pincetgreep]].", "Veel groei in korte tijd."),
        mk("Waarom is Elias onhandiger geworden?",
           ["zijn lichaam groeit sneller dan zijn motoriek volgt", "hij heeft te weinig geslapen voor de toetsen", "zijn ogen zijn achteruitgegaan door het lezen van boeken", "hij is van nature altijd al onhandig geweest"],
           0, "De motoriek moet zich aanpassen aan langere armen en benen."),
        keuze("Zijn vriend die nog klein is, krijgt wellicht een [[*latere|vroegere]] groeispurt.", "Niet iedereen groeit op dezelfde leeftijd."),
        tabel("Klopt dit over Elias?",
              [("Hij valt op in de groep.", J), ("Alle kinderen van twaalf groeien even snel.", F), ("Hij kan zich anders voelen dan zijn klasgenoten.", J)],
              "Een vroege groeispurt maakt dat je uit de toon valt."),
    ]),
    sorteer("Werkt dit zintuig bij een pasgeboren baby al goed?", ["al goed", "nog niet klaar"],
            [("het gehoor", "al goed"), ("de reuk", "al goed"), ("het scherpe zicht", "nog niet klaar"), ("de smaak", "al goed"), ("het dieptezicht", "nog niet klaar")],
            "Het zicht heeft nog maanden nodig."),
    mk("Een baby van drie dagen herkent zijn mama nog niet aan haar gezicht. Waaraan dan wel?",
       ["aan haar geur en haar stem", "aan de kleur van haar kleren", "aan haar handschrift op een kaartje", "aan haar haarkleur van ver"],
       0, "Reuk en gehoor zijn vroeg klaar."),
    keuze("De meeste babyreflexen verdwijnen in [[*het eerste levensjaar|het tiende levensjaar|de adolescentie]].", "De bewuste beweging neemt het over."),
    mk("Welke activiteit is sensomotorisch: zintuig en beweging samen?",
       ["touwtjespringen op het ritme van een liedje", "stil in je bed liggen en rustig in slaap vallen", "een verhaal horen zonder te bewegen", "een prent bekijken zonder iets te doen"],
       0, "Je hoort het ritme en je benen springen mee."),
    tabel("Lees je dit af op een groeicurve?",
          [("de lengte", J), ("de leeftijd", J), ("de schoolresultaten", F), ("het gewicht", J), ("de schoenmaat", F)],
          "Lengte of gewicht tegenover de leeftijd."),
    inv("Hoe noem je de lijnen op een groeicurve die tonen hoe leeftijdsgenoten groeien? Eén woord.", ["percentiellijnen", "percentiellijn", "de percentiellijnen"], "De percentiellijnen, zoals P3, P50 en P97."),
    keuze("Op een groeicurve vergelijk je een kind met [[*leeftijdsgenoten|volwassenen|zijn eigen ouders]].", "De percentiellijnen tonen de groei van kinderen van dezelfde leeftijd."),
    tabel("Klopt dit over de fysieke ontwikkeling?",
          [("Grote bewegingen komen voor precieze bewegingen.", J), ("Een baby kan eerst stappen en daarna pas zitten.", F), ("Een pasgeboren baby ziet al scherp op grote afstand.", F), ("Babyreflexen zijn er al vanaf de geboorte.", J)],
          "Van grof naar fijn, van kop naar staart."),
    mk("Een kleuter houdt zijn potlood nog in een vuist. Welk groeiprincipe zie je?",
       ["van grof naar fijn", "van kop naar staart", "van fijn naar grof", "van buiten naar midden"],
       0, "Eerst de hele hand, pas later de precieze vingergreep."),
    sleep("Een groeicurve zet de [[lengte]] of het gewicht uit tegenover de [[leeftijd]]. Een periode van heel snelle groei heet een [[groeispurt]].",
          ["pincetgreep", "reflex"],
          "De percentiellijnen tonen hoe leeftijdsgenoten groeien."),
    keuze("Je legt een vinger in het handje van een pasgeboren baby en het handje sluit zich. Dat is de [[*grijpreflex|pincetgreep|zuigreflex]].", "Een reflex, geen aangeleerde greep."),
    inv("Hoe noem je de precieze bewegingen van handen en vingers? Twee woorden.", ["fijne motoriek", "de fijne motoriek", "fijnmotoriek"], "De fijne motoriek."),
    mk("Waarom komt zitten vóór stappen?",
       ["de controle gaat van boven naar onder", "zitten is minder leuk dan stappen", "stappen leert een kind pas op school", "ouders leren zitten altijd als eerste aan"],
       0, "Van kop naar staart: eerst hoofd en romp, dan de benen."),
    sorteer("Babyreflex of aangeleerde beweging?", ["babyreflex", "aangeleerd"],
            [("zuigen als je mond aangeraakt wordt", "babyreflex"), ("leren fietsen", "aangeleerd"), ("het handje sluit rond een vinger", "babyreflex"), ("een lepel naar je mond brengen", "aangeleerd"), ("de armen opengooien bij een plots geluid", "babyreflex")],
            "Reflexen zijn er vanaf het begin, zonder oefenen."),
    mk("Waarom hang je een mobiel best niet te hoog boven het bedje van een pasgeborene?",
       ["een pasgeborene ziet enkel op korte afstand", "een mobiel maakt altijd te veel lawaai", "baby's horen in de eerste weken na de geboorte nog niets", "kleuren zijn schadelijk voor jonge ogen"],
       0, "Het zicht is bij de geboorte nog onscherp."),
    keuze("Een groeispurt gebeurt vooral in de [[*puberteit|babytijd|late volwassenheid]].", "Dan wordt een kind in korte tijd veel langer en zwaarder."),
    tabel("Hoort dit bij de fijne motoriek?",
          [("de pincetgreep", J), ("kruipen", F), ("leren tekenen", J), ("rollen", F)],
          "Kruipen en rollen zijn grove motoriek."),
    keuze("Een bal zien aankomen en je handen meebewegen om hem te vangen, is [[*sensomotorisch|moreel|cognitief]] handelen.", "Zintuig en beweging werken samen."),
    open_("Een mama vraagt waarom haar zoon van dertien de laatste tijd zo onhandig is. Leg het haar in twee zinnen uit.",
          "Hij zit wellicht in een groeispurt: zijn armen en benen worden snel langer. Zijn motoriek moet zich daar nog aan aanpassen, en dat komt vanzelf goed."),
]

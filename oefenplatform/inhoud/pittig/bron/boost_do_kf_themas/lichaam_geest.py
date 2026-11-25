"""Lichaam en geest — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_lichaam_geest: monisme en dualisme, en de
visies van Plato, Aristoteles en Descartes in tijd en ruimte. Met een
zelfgetekende tijdlijn en twee mensbeelden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ROOD

TL = Prent("tijdlijn-en-mensbeelden", "Een tijdlijn en twee mensbeelden", "een tijdlijn met letters A tot D en twee tekeningen E en F")
TL.lijn(80, 150, 920, 150, DONKER, 4)
def X(j):
    return 80 + (j + 600) / 2600 * 840
for j, lab in ((-500, "500 v.C."), (0, "0"), (500, "500"), (1000, "1000"), (1500, "1500"), (2000, "2000")):
    TL.lijn(X(j), 140, X(j), 160, DONKER, 2); TL.tekst(X(j), 190, lab, 18)
PT = {"A": -380, "B": 500, "C": 1640, "D": 1900}
for t, j in PT.items():
    TL.cirkel(X(j), 150, 9, ROOD, DONKER, 2); TL.letter(X(j), 100, t)
# E: geest in het hoofd, één geheel
def figuur(cx, cy):
    TL.cirkel(cx, cy, 40, GRIJS, DONKER, 3); TL.pad(f"M {cx-70} {cy+170} Q {cx-70} {cy+50} {cx} {cy+45} Q {cx+70} {cy+50} {cx+70} {cy+170} Z", GRIJS, DONKER, 3)
figuur(300, 330)
TL.pad("M 280 335 q -5 -20 12 -22 q 8 -12 20 0 q 15 2 10 20 Z", "#ffffff", BLAUW, 2)
TL.letter(300, 560, "E")
# F: geest los boven het lichaam
figuur(700, 380)
TL.pad("M 650 290 q -15 -40 25 -45 q 15 -30 50 -10 q 40 -5 35 35 q 20 25 -15 30 Z", "#ffffff", BLAUW, 3)
TL.lijn(700, 312, 700, 335, BLAUW, 2, True)
TL.letter(700, 590, "F")
U = "tijdlijn-en-mensbeelden.svg"
Z = {t: [Prent.rond(X(j), 125, 40)] for t, j in PT.items()}
Z["E"] = [Prent.zone(210, 280, 180, 300)]
Z["F"] = [Prent.zone(610, 230, 180, 380)]

GESPREK = ("Lees het gesprek.\n\n"
           "Noor: « Na zijn ongeval was mijn oom een ander mens. Hij werd sneller boos en vergat veel. Dat komt door zijn hersenen. »\n\n"
           "Sem: « Maar een gedachte heeft geen gewicht en geen kleur. Je kan ze niet vastnemen. Er moet dus meer zijn dan alleen het lichaam. »")

VRAGEN = [
    klik("Bekijk de tijdlijn. Klik op de letter bij de tijd waarin Plato en Aristoteles leefden.", U, Z["A"], "Athene, vierde eeuw voor Christus."),
    klik("Klik op de letter bij de tijd waarin Descartes leefde.", U, Z["C"], "Frankrijk, zeventiende eeuw."),
    klik("Klik op de tekening die het best past bij het dualisme.", U, Z["F"], "Lichaam en geest zijn twee aparte dingen."),
    klik("Klik op de tekening die het best past bij het monisme.", U, Z["E"], "De mens is één geheel."),
    casus(GESPREK, [
        sorteer("Welke mensvisie steunt het argument?", ["monisme", "dualisme"],
                [("het argument van Noor", "monisme"), ("het argument van Sem", "dualisme")],
                "Een gekwetst brein verandert iemand; een gedachte voelt niet stoffelijk."),
        mk("Welke vraag kan Noor aan Sem stellen om zijn standpunt te toetsen?",
           ["hoe raakt jouw geest dan het lichaam?", "hoeveel weegt een gemiddeld menselijk brein precies?", "wanneer had je oom zijn ongeval met de wagen?", "welke kleur heeft de gedachte waar jij aan denkt?"],
           0, "Dat is het probleem van hoe twee aparte dingen elkaar raken."),
        keuze("Sem sluit het best aan bij [[*Descartes|Aristoteles]]: het denkende is iets anders dan het uitgebreide.", "Descartes onderscheidt de geest die denkt van het lichaam dat ruimte inneemt."),
        tabel("Klopt dit over het gesprek?",
              [("Een hersenscan kan beslissen wie gelijk heeft.", F), ("Het debat is nog niet beslecht.", J), ("Beiden geven een argument, geen loutere mening.", J)],
              "Een hersenscan toont activiteit, geen bewustzijn."),
    ]),
    koppel("Koppel de filosoof aan zijn visie.",
           [("Plato", "de ziel is gevangen in het lichaam"), ("Aristoteles", "de ziel is de vorm van het lichaam"), ("Descartes", "ik denk, dus ik ben")],
           ["de mens is enkel een machine van vlees"], "Twee dualisten en een filosoof die dichter bij het monisme staat."),
    tabel("Dualist of niet?",
          [("Plato", "dualist"), ("Aristoteles", "niet dualist"), ("Descartes", "dualist")],
          "Aristoteles ziet de mens als één geheel van vorm en stof.", ["dualist", "niet dualist"]),
    sorteer("Monisme of dualisme?", ["monisme", "dualisme"],
            [("Zonder brein geen gedachten.", "monisme"), ("Na de dood leeft de ziel verder.", "dualisme"), ("Verliefdheid is enkel een werking van de hersenen.", "monisme"), ("Het lichaam is tijdelijk, de ziel niet.", "dualisme")],
            "Monos is één, duo is twee."),
    mk("Waarom is pijn in je vinger een probleem voor het dualisme?",
       ["iets lichamelijks stoort dan de geest", "pijn bestaat volgens het dualisme helemaal niet", "een vinger is geen echt deel van het lichaam", "pijn kan je volgens het dualisme altijd meten"],
       0, "Hoe raken twee aparte dingen elkaar?"),
    volgorde("Zet deze filosofen in de volgorde waarin ze leefden.",
             ["Plato", "Aristoteles", "Descartes"],
             "Aristoteles was leerling van Plato; Descartes kwam bijna tweeduizend jaar later."),
    keuze("Descartes trok eerst alles in twijfel om [[*een zeker beginpunt|zoveel mogelijk vragen|een nieuwe godsdienst]] te vinden.", "Eén zekerheid bleef over: hij twijfelde, dus hij dacht."),
    keuze("'Zonder lichaam kan er geen ziel bestaan.' Dat sluit aan bij [[*Aristoteles|Plato|Descartes]].", "Vorm zonder stof bestaat bij hem niet."),
    tabel("Klopt dit over Plato, Aristoteles en Descartes?",
          [("Aristoteles was een leerling van Plato.", J), ("Descartes leefde in het oude Athene.", F), ("Plato noemt de ziel onsterfelijk.", J), ("De drie filosofen leefden in dezelfde eeuw.", F)],
          "Plato en Aristoteles: Athene; Descartes: Frankrijk."),
    mk("Waarom raakt het thema lichaam en geest ook aan de ethiek?",
       ["schuld hangt aan een vrije wil", "omdat dokters soms over hersenen beslissen in een ziekenhuis", "omdat de ethiek alleen over het lichaam van de mens gaat", "omdat Plato ook regels voor de stad Athene schreef"],
       0, "Als je brein alles beslist, blijft er van vrije wil weinig over."),
    sleep("Bij het [[monisme]] is de mens één geheel. Bij het [[dualisme]] bestaat hij uit een [[lichaam]] en een geest.",
          ["ziel alleen", "vorm"], "Monos betekent één, duo twee."),
    tabel("Is dit een filosofische vraag bij het thema lichaam en geest?",
          [("Ben ik mijn brein?", J), ("Hoeveel weegt een brein?", F), ("Waar zitten gedachten?", J), ("Heb ik een ziel?", J)],
          "Het gewicht van een brein is een weetvraag."),
    keuze("Plato en Descartes zijn allebei dualist, maar [[*elk om een andere reden|om precies dezelfde reden]].", "Plato spreekt van een onsterfelijke ziel, Descartes van denken tegenover uitgebreidheid."),
    inv("Hoe noem je het probleem van hoe geest en lichaam elkaar kunnen raken? Eén woord.", ["interactieprobleem", "het interactieprobleem"], "Het interactieprobleem."),
    mk("Waarom plaats je Descartes in zijn eigen tijd?",
       ["hij dacht na de opkomst van de wetenschap", "omdat hij in dezelfde stad als Plato woonde", "omdat hij de leraar van Aristoteles was", "omdat hij in de vierde eeuw voor Christus schreef"],
       0, "Hun antwoord hangt aan hun tijd."),
    keuze("Iemand zegt: 'Wie na een hersenletsel een ander karakter heeft, toont hoe sterk geest en lichaam samenhangen.' Dat argument steunt het [[*monisme|dualisme]].", "De geest hangt af van het brein."),
    keuze("Descartes leefde [[*bijna tweeduizend jaar|ongeveer honderd jaar|ongeveer vijfhonderd jaar]] na Plato en Aristoteles.", "Vierde eeuw voor Christus tegenover de zeventiende eeuw."),
    tabel("Past deze uitspraak bij Descartes?",
          [("Ik twijfel eerst aan alles.", J), ("Geest en stof zijn apart.", J), ("De ziel is de vorm van het lichaam.", F), ("Ik denk, dus ik ben.", J)],
          "De ziel als vorm van het lichaam is Aristoteles."),
    mk("Waarom is de vraag naar lichaam en geest filosofisch en niet enkel wetenschappelijk?",
       ["geen meting beslecht ze", "omdat wetenschappers het brein nog nooit bestudeerd hebben", "omdat je ze kan opzoeken in een oud Grieks boek", "omdat ze enkel over de tijd van Plato gaat"],
       0, "Een scan toont activiteit, geen ervaring."),
    inv("Welke Griekse filosoof zag het lichaam als een gevangenis van de ziel? Eén naam.", ["Plato", "plato"], "Voor Plato is de ziel onsterfelijk."),
    keuze("Het woord monisme komt van het Griekse monos, dat [[*één|twee|ziel]] betekent.", "Eén geheel."),
    sorteer("Plato, Aristoteles of Descartes?", ["Plato", "Aristoteles", "Descartes"],
            [("Frankrijk, zeventiende eeuw", "Descartes"), ("vorm en stof horen samen", "Aristoteles"), ("de ziel is onsterfelijk", "Plato"), ("het denkende tegenover het uitgebreide", "Descartes")],
            "Elk in zijn tijd en ruimte."),
    open_("Geef een argument volgens de AUB-methode voor of tegen het dualisme.",
          "A: Mijn argument is dat het dualisme moeilijk vol te houden is. U: want als lichaam en geest twee aparte dingen zijn, kan je niet uitleggen hoe ze elkaar raken. Dat is slecht voor de theorie, omdat ze dan het gewone leven niet verklaart. B: Stel je voor dat je beslist om je hand op te steken. Hoe beweegt een gedachte zonder gewicht dan je arm?"),
]

"""Van brutoloon naar nettoloon — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen loonbrief."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een vereenvoudigde loonbrief met vijf regels zonder namen --------------------------
LB = Prent("loonbrief", "Loonbrief van een bediende, maand oktober", "een loonbrief met vijf regels A tot E onder elkaar, elk met een bedrag: A 2 600,00; B min 339,82; C 2 260,18; D min 430,00; E 1 830,18")
LB.rect(160, 70, 680, 520, "#ffffff", DONKER, 10, 2)
LB.tekst(200, 120, "Werknemer: bediende, voltijds", 18, "start")
LB.tekst(800, 120, "bedrag (euro)", 18, "end", vet=True)
RIJ = [("A", "2 600,00"), ("B", "− 339,82"), ("C", "2 260,18"), ("D", "− 430,00"), ("E", "1 830,18")]
YL = {}
for i, (k, bedrag) in enumerate(RIJ):
    y = 190 + i * 80
    YL[k] = y
    if k in "CE":
        LB.rect(180, y - 32, 640, 60, "#f2efe6", GRIJS, 6, 1)
    LB.letter(230, y, k)
    LB.lijn(270, y + 10, 600, y + 10, "#d9d4c4", 1, True)
    LB.tekst(800, y + 8, bedrag, 22, "end", vet=k in "CE")
ZL = {k: [Prent.zone(180, y - 35, 640, 70)] for k, y in YL.items()}

VRAGEN = [
    klik("Klik op het belastbaar loon.", LB.bestand, ZL["C"],
         "Het belastbaar loon is wat overblijft na de sociale zekerheidsbijdrage: 2 600,00 min 339,82."),
    klik("Klik op het voorschot op de personenbelasting.", LB.bestand, ZL["D"],
         "De bedrijfsvoorheffing wordt berekend op het belastbaar loon en is een voorschot op je personenbelasting."),
    klik("Klik op het bedrag dat naar de RSZ gaat.", LB.bestand, ZL["B"],
         "De sociale zekerheidsbijdrage wordt als eerste van het brutoloon afgetrokken."),
    klik("Klik op het bedrag dat op de rekening van de werknemer komt.", LB.bestand, ZL["E"],
         "Het nettoloon is het eindpunt van de berekening."),
    met_prent(LB.bestand, inv("Controleer de loonbrief: hoeveel is C min D, in euro?", ["1830,18", "1 830,18", "1830.18"],
              "2 260,18 min 430,00 is 1 830,18: precies het nettoloon E.")),
    met_prent(LB.bestand, tabel("Kijk naar de loonbrief. Klopt dit?", [
        ("A is het brutoloon.", J),
        ("De bedrijfsvoorheffing wordt op A berekend.", F),
        ("Met kinderen ten laste zou D lager zijn.", J),
        ("Met kinderen ten laste zou B lager zijn.", F),
    ], "De gezinssituatie verandert de bedrijfsvoorheffing, niet de sociale bijdrage.")),
    volgorde("Zet de stappen van brutoloon naar nettoloon in de juiste volgorde.", [
        "brutoloon",
        "sociale zekerheidsbijdrage aftrekken",
        "belastbaar loon",
        "bedrijfsvoorheffing aftrekken",
        "nettoloon",
    ], "Eerst de sociale bijdrage, dan de bedrijfsvoorheffing."),
    casus(
        "Jef is arbeider en Nina bediende. Ze verdienen allebei 2 000 euro bruto per maand. "
        "Hun werkgever rekent voor de sociale zekerheidsbijdrage met hetzelfde percentage.",
        [
            mk("Op welk bedrag wordt de sociale bijdrage van Jef berekend?",
               ["Op 2 160 euro",
                "Op 2 000 euro",
                "Op 1 840 euro",
                "Op 1 080 euro"], 0,
               "Bij een arbeider rekent men op 108 procent van het brutoloon: 2 000 maal 1,08."),
            keuze("Wie betaalt de hoogste sociale bijdrage? [[*Jef|Nina|Ze betalen evenveel]]",
                  "Hetzelfde percentage op een hoger bedrag."),
            tabel("Klopt dit voor Jef en Nina?", [
                ("De regel van 108 procent geldt enkel voor arbeiders.", J),
                ("Bij Nina wordt de sociale bijdrage op haar brutoloon berekend.", J),
                ("Jef betaalt minder bedrijfsvoorheffing omdat hij arbeider is.", F),
            ], "De 108-procentregel is een oude regel uit de tijd dat arbeiders per dag betaald werden."),
        ],
    ),
    casus(
        "Sam (17) heeft een studentenjob in een supermarkt met een studentencontract. Hij "
        "verdient 200 euro bruto voor een weekend. Zijn oudere zus heeft een gewoon contract "
        "in dezelfde winkel.",
        [
            tabel("Wat gaat er af van Sams loon binnen zijn studentencontract?", [
                ("een solidariteitsbijdrage", J),
                ("de gewone sociale zekerheidsbijdrage", F),
                ("bedrijfsvoorheffing", F),
            ], "Een student betaalt enkel een lagere solidariteitsbijdrage."),
            mk("Waarom ligt Sams nettoloon dicht bij zijn brutoloon?",
               ["Er gaat weinig af",
                "Zijn werkgever betaalt zijn belastingen",
                "Studenten hebben recht op overloon",
                "Zijn loon wordt op 108 procent berekend"], 0,
               "Enkel een kleine solidariteitsbijdrage, geen bedrijfsvoorheffing."),
            keuze("Hoeveel uren Sam dit jaar nog mag werken, kijkt hij na op [[*student@work|de loonbrief van zijn zus|de website van de RVA]].",
                  "Daar volgt een student zijn gewerkte uren op."),
        ],
    ),
    koppel("Koppel elk bedrag aan zijn betekenis.", [
        ["brutoloon", "het loon voor er iets afgaat"],
        ["belastbaar loon", "het loon na de sociale bijdrage"],
        ["nettoloon", "wat je op je rekening krijgt"],
        ["loonkost", "het brutoloon plus de bijdrage van de werkgever"],
    ], ["het loon na de personenbelasting van vorig jaar"], "Van loonkost voor de werkgever tot nettoloon voor de werknemer."),
    inv("Iemand verdient 2 400 euro bruto. Na de sociale bijdrage blijft er 2 086 euro over. De bedrijfsvoorheffing is 380 euro. Wat is het nettoloon, in euro?",
        ["1706", "1 706", "1706 euro"], "2 086 min 380."),
    inv("Een werkgever betaalt bovenop een brutoloon van 3 000 euro nog 750 euro eigen bijdrage aan de RSZ. Wat is de loonkost, in euro?",
        ["3750", "3 750", "3750 euro"], "Brutoloon plus de werkgeversbijdrage."),
    tabel("Hangt dit af van de gezinssituatie van de werknemer?", [
        ("de bedrijfsvoorheffing", J),
        ("de sociale zekerheidsbijdrage", F),
        ("het nettoloon", J),
    ], "Kinderen ten laste verlagen de bedrijfsvoorheffing en verhogen dus het nettoloon."),
    mk("Na de belastingaangifte blijkt dat Nora te veel bedrijfsvoorheffing betaalde. Wat gebeurt er?",
       ["Ze krijgt het verschil terug",
        "Ze moet het verschil nog eens bijbetalen",
        "Haar werkgever houdt het verschil",
        "Het verschil gaat naar de RSZ"], 0,
       "De bedrijfsvoorheffing is een voorschot; bij de aangifte wordt afgerekend."),
    sorteer("Gaat dit naar de sociale zekerheid of naar de belastingen?", ["Sociale zekerheid", "Belastingen"], [
        ["de sociale zekerheidsbijdrage", "Sociale zekerheid"],
        ["de bedrijfsvoorheffing", "Belastingen"],
        ["de bijdrage van de werkgever aan de RSZ", "Sociale zekerheid"],
        ["de personenbelasting", "Belastingen"],
    ], "Twee inhoudingen met een ander doel."),
    keuze("De bedrijfsvoorheffing heet zo omdat ze [[*vooraf|achteraf|eenmalig]] geheven wordt.",
          "Zo moet je na je aangifte niet alles in één keer bijbetalen."),
    tabel("Klopt dit over de berekening van het loon?", [
        ("Het belastbaar loon is hetzelfde als het nettoloon.", F),
        ("De bedrijfsvoorheffing wordt na de sociale bijdrage afgetrokken.", J),
        ("Een werknemer kost zijn werkgever meer dan zijn brutoloon.", J),
        ("Een student met een studentencontract betaalt bedrijfsvoorheffing.", F),
    ], "Het belastbaar loon staat tussen bruto en netto."),
    mk("Twee collega's verdienen evenveel bruto, maar de ene heeft twee kinderen ten laste. Wat verwacht je?",
       ["Die met kinderen houdt netto meer over",
        "Die zonder kinderen houdt netto meer over",
        "Ze houden netto precies evenveel over",
        "Die met kinderen betaalt een hogere sociale bijdrage"], 0,
       "Kinderen ten laste verlagen de bedrijfsvoorheffing."),
    sleep("Van het [[brutoloon]] gaat eerst de sociale bijdrage af. Wat overblijft is het [[belastbaar]] loon. Na de [[bedrijfsvoorheffing]] blijft het nettoloon over.",
          ["nettoloon", "overloon"], "Twee inhoudingen, in een vaste volgorde."),
    inv("Een arbeider verdient 2 500 euro bruto. Op welk bedrag wordt zijn sociale bijdrage berekend, in euro?",
        ["2700", "2 700", "2700 euro"], "108 procent van 2 500 is 2 700 euro."),
    met_prent(LB.bestand, keuze("Bedrag B gaat naar de [[*RSZ|FOD Financiën|werkgever]] en D is een voorschot op de [[*personenbelasting|sociale zekerheid|btw]].",
              "Eerst de sociale bijdrage, dan de bedrijfsvoorheffing.")),
    met_prent(LB.bestand, inv("Hoeveel euro wordt er in totaal ingehouden op deze loonbrief?", ["769,82", "769.82"],
              "339,82 + 430,00 = 769,82 euro, of A min E.")),
    tabel("Welke instantie hoort bij dit bedrag?", [
        ("de sociale zekerheidsbijdrage", "RSZ"),
        ("de bedrijfsvoorheffing", "belastingen"),
        ("de bijdrage van de werkgever bovenop het brutoloon", "RSZ"),
    ], "De RSZ int de sociale bijdragen; de voorheffing gaat naar de belastingen.", kolommen=["RSZ", "belastingen"]),
    mk("Waarom kost een werknemer zijn werkgever meer dan het brutoloon?",
       ["De werkgever betaalt een eigen RSZ-bijdrage",
        "De werkgever betaalt ook de bedrijfsvoorheffing van zijn eigen zak",
        "Het nettoloon is altijd hoger dan het brutoloon",
        "De werkgever moet het vakantiegeld elke maand betalen"], 0,
       "De werkgeversbijdrage komt bovenop het brutoloon."),
    keuze("Op een loonbrief van een student met een studentencontract staat een [[*solidariteitsbijdrage|gewone sociale bijdrage|bedrijfsvoorheffing]].",
          "Binnen het studentencontract geldt die lagere bijdrage."),
    open_("Leg uit waarom er op een loonbrief zowel een bedrag voor de RSZ als een bedrag voor de bedrijfsvoorheffing staat.",
          "Het zijn twee verschillende inhoudingen. De sociale zekerheidsbijdrage gaat naar de RSZ en betaalt mee pensioenen, ziekteverzekering en werkloosheid. De bedrijfsvoorheffing is een voorschot op de personenbelasting en gaat naar de belastingen."),
]

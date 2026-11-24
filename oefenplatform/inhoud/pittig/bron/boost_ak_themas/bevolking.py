"""Hoe een bevolking verandert — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_bevolking, met drie zelfgetekende
leeftijdshistogrammen om op te klikken. ALG geldt voor doorstroom en dubbele
finaliteit; DO_ALLEEN gaat over het vruchtbaarheidscijfer, het migratiesaldo
en de demografische transitie (enkel doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, DONKER

HIST = Prent("drie-histogrammen", "Drie leeftijdshistogrammen", "drie leeftijdshistogrammen naast elkaar, mannen links en vrouwen rechts, met de letters A, B en C")
VORMEN = {
    "A": [95, 85, 75, 64, 54, 44, 34, 25, 16, 9],   # jong: brede basis
    "B": [40, 44, 50, 56, 58, 60, 58, 54, 46, 34],  # vergrijsd
    "C": [60, 62, 60, 30, 58, 57, 55, 50, 40, 25],  # inkeping
}
for i, (t, w) in enumerate(VORMEN.items()):
    mx = 170 + i * 330
    for j, b in enumerate(w):
        y = 540 - (j + 1) * 42
        HIST.rect(mx - b, y, b, 36, BLAUW, DONKER, 0, 1)
        HIST.rect(mx, y, b, 36, ORANJE, DONKER, 0, 1)
    HIST.lijn(mx, 110, mx, 545, DONKER, 2)
    HIST.letter(mx, 85, t)
for j in range(0, 10, 2):
    HIST.tekst(30, 540 - j * 42 - 12, f"{j*10}", 13, "start")
HIST.tekst(30, 590, "leeftijd per groep van 10 jaar; blauw = mannen, oranje = vrouwen", 16, "start")
U = "drie-histogrammen.svg"
Z = {t: Prent.zone(170 + i * 330 - 110, 60, 220, 490) for i, t in enumerate(VORMEN)}

ALG = [
    klik("Klik op het histogram van een bevolking met veel kinderen en weinig ouderen.", U, [Z["A"]],
         "Een brede basis die snel smal toeloopt: een jonge, snel groeiende bevolking."),
    klik("Klik op het histogram van een vergrijzende bevolking.", U, [Z["B"]],
         "Smal onderaan en breed bij de ouderen: weinig geboorten, mensen leven lang."),
    klik("Klik op het histogram met een inkeping, bijvoorbeeld door een oorlog of een crisis.", U, [Z["C"]],
         "Eén groep is veel smaller: die mensen werden toen niet geboren of stierven."),
    casus("Land X heeft een geboortecijfer van 11 ‰ en een sterftecijfer van 13 ‰. Het telt 10 miljoen inwoners.", [
        inv("Hoe groot is de natuurlijke aangroei in ‰? Schrijf het getal met teken.", ["-2", "−2", "-2 ‰", "−2 ‰"],
            "11 − 13 = −2 ‰: er sterven meer mensen dan er geboren worden."),
        inv("Met hoeveel mensen daalt de bevolking door die aangroei in één jaar?", ["20000", "20 000"],
            "2 per 1000 van 10 miljoen = 20 000 mensen."),
        tabel("Klopt dit over land X?",
              [("De bevolking kan toch groeien door immigratie.", J), ("Het histogram is waarschijnlijk smal onderaan.", J), ("Het land heeft veel jonge kinderen.", F)],
              "Een negatieve aangroei past bij weinig geboorten en vergrijzing."),
    ]),
    sorteer("Doet dit het geboortecijfer eerder dalen of stijgen?", ["eerder dalen", "eerder stijgen"],
            [("meisjes die lang naar school gaan", "eerder dalen"), ("goede toegang tot voorbehoedsmiddelen", "eerder dalen"), ("kinderen als hulp op de boerderij", "eerder stijgen"), ("een goed pensioen voor ouderen", "eerder dalen"), ("hoge kindersterfte", "eerder stijgen")],
            "Waar kinderen nodig zijn als hulp of oudedagsvoorziening, worden er meer geboren."),
    tabel("Klopt dit over kengetallen?",
          [("Het geboortecijfer telt geboorten per 1000 inwoners per jaar.", J), ("Een land met veel ouderen kan een hoog sterftecijfer hebben, ook met goede zorg.", J), ("Kengetallen in ‰ maken landen eerlijk vergelijkbaar.", J), ("Een negatieve natuurlijke aangroei is onmogelijk.", F)],
          "Verhoudingsgetallen per duizend maken vergelijken eerlijk."),
    koppel("Welke term hoort bij welke omschrijving?",
           [("immigratie", "mensen komen in een land wonen"), ("emigratie", "mensen vertrekken uit hun land"), ("braindrain", "hoogopgeleiden vertrekken"), ("braingain", "hoogopgeleiden komen aan")],
           ["vergrijzing"], "Im- is binnenkomen, e- is vertrekken."),
    sorteer("Is dit een pushfactor of een pullfactor?", ["pushfactor", "pullfactor"],
            [("oorlog in het eigen land", "pushfactor"), ("werk in het land van aankomst", "pullfactor"), ("aanhoudende droogte", "pushfactor"), ("familie die er al woont", "pullfactor"), ("vervolging om je geloof", "pushfactor"), ("goede scholen", "pullfactor")],
            "Push duwt weg, pull trekt aan."),
    tabel("Klopt dit over migratie?",
          [("De meeste migranten blijven in hun eigen wereldregio.", J), ("Wie vlucht voor droogte, steekt meestal meteen een oceaan over.", F), ("Wie migreert, is vaak jongvolwassen.", J)],
          "Vluchten gebeurt meestal naar een buurland."),
    mk("Een land voerde jarenlang een beleid van één kind per gezin. Wat zie je nu in zijn histogram?",
       ["smalle balken bij de jongere groepen", "een brede basis die heel snel smal toeloopt", "overal even brede balken", "een inkeping bij de oudste groep van het land"], 0,
       "Minder geboorten maakt de onderste balken smal."),
    casus("In een land daalt het geboortecijfer al twintig jaar en leven mensen steeds langer.", [
        mk("Wat verwacht je over twintig jaar?",
           ["een groter aandeel ouderen", "een grotere groep kleine kinderen", "een veel hoger geboortecijfer", "een jongere beroepsbevolking"], 0,
           "Minder jongeren en langer leven: de bevolking vergrijst."),
        tabel("Welke gevolgen heeft die vergrijzing?",
              [("meer uitgaven aan pensioenen", J), ("meer vraag naar zorg voor ouderen", J), ("minder nood aan rusthuizen", F), ("minder mensen op de arbeidsmarkt", J)],
              "Vergrijzing kost geld voor pensioenen en zorg en maakt de beroepsbevolking kleiner."),
    ]),
    tabel("Klopt dit over braindrain?",
          [("Het land van vertrek verliest artsen en ingenieurs.", J), ("Het is vooral een voordeel voor het land van vertrek.", F), ("Het land van aankomst kent dan braingain.", J)],
          "Het land dat hoogopgeleiden verliest, verliest de kennis die het nodig heeft."),
    sleep("Een leeftijdshistogram met een brede [[basis]] wijst op een jonge bevolking. Is de top breed, dan is de bevolking [[vergrijsd]]. Een [[inkeping]] schuift met de jaren mee naar boven.",
          ["top", "verjongd"], "Je leest de vorm van onder naar boven."),
    keuze("Een inkeping in een histogram schuift na enkele jaren [[*mee naar boven|vanzelf weer dicht|naar onderen]].",
          "Wie toen niet geboren werd, komt later ook niet terug."),
    mk("Waarom zet men een histogram in groepen van vijf of tien jaar?",
       ["zo blijft de vorm overzichtelijk", "omdat de gegevens per jaar geheim zijn", "omdat mannen en vrouwen anders tellen", "zo past het histogram op één blad papier"], 0,
       "Honderd balken per jaar maken de vorm onleesbaar."),
    inv("Een land heeft een geboortecijfer van 25 ‰ en een natuurlijke aangroei van 18 ‰. Hoe groot is het sterftecijfer in ‰?", ["7", "7 ‰"],
        "25 − 18 = 7 ‰."),
    tabel("Welke kengetallen heb je samen nodig om de totale bevolkingsgroei te kennen?",
          [("het geboortecijfer", J), ("het sterftecijfer", J), ("hoeveel mensen er inwijken en uitwijken", J), ("de bevolkingsdichtheid", F)],
          "Geboorten, sterften en migratie bepalen samen de groei."),
    inv("Een land van 8 miljoen inwoners heeft een geboortecijfer van 15 ‰. Hoeveel kinderen worden er in een jaar geboren?", ["120000", "120 000"],
        "15 per 1000 van 8 miljoen = 120 000."),
    tabel("Lees de drie histogrammen. Klopt dit?",
          [("A hoort het best bij een land met veel geboorten.", J), ("B hoort het best bij een land met een lange levensverwachting.", J), ("C toont een land zonder enige verstoring.", F)],
          "De vorm vertelt het verhaal van geboorten, sterften en gebeurtenissen."),
]

DO_ALLEEN = [
    casus("Land Y heeft een geboortecijfer van 36 ‰, een sterftecijfer van 10 ‰ en een vruchtbaarheidscijfer van 4,8.", [
        mk("In welke fase van de demografische transitie zit land Y waarschijnlijk?",
           ["de tweede fase", "de eerste fase", "de derde fase", "de vierde fase"], 0,
           "De sterfte is al gedaald, de geboorten blijven hoog: de snelste groei."),
        inv("Hoeveel kinderen krijgen vrouwen in land Y gemiddeld?", ["4,8", "4.8"],
            "Het vruchtbaarheidscijfer is het gemiddeld aantal kinderen per vrouw."),
    ]),
    volgorde("Rangschik de fasen van de demografische transitie.",
             ["geboorte- en sterftecijfer allebei hoog", "sterftecijfer daalt, geboortecijfer blijft hoog", "geboortecijfer daalt ook", "geboorte- en sterftecijfer allebei laag"],
             "Eerst daalt de sterfte, pas daarna de geboorten."),
    tabel("Klopt dit over het migratiesaldo?",
          [("Het is de immigratie min de emigratie.", J), ("Voor de hele wereld samen is het nul.", J), ("Een positief saldo kan een negatieve natuurlijke aangroei compenseren.", J), ("Het is altijd positief in een rijk land.", F)],
          "Wie ergens vertrekt, komt elders aan."),
    inv("Een land telt in een jaar 45 000 immigranten en 30 000 emigranten. Hoe groot is het migratiesaldo?", ["15000", "15 000", "+15000", "+15 000"],
        "45 000 − 30 000 = 15 000."),
    mk("Een land heeft een geboortecijfer van 12 ‰ en een sterftecijfer van 11 ‰. In welke fase van de transitie zit het waarschijnlijk?",
       ["de vierde fase", "de eerste fase", "de tweede fase", "de derde fase, net begonnen"], 0,
       "Allebei laag en dicht bij elkaar: de bevolking groeit nog maar traag."),
    tabel("Klopt dit over het vruchtbaarheidscijfer?",
          [("Een cijfer van 1,4 betekent gemiddeld 1,4 kinderen per vrouw.", J), ("Bij ongeveer 2,1 blijft een bevolking op lange termijn gelijk.", J), ("Het is hetzelfde als het geboortecijfer.", F)],
          "Het geboortecijfer telt per 1000 inwoners; het vruchtbaarheidscijfer per vrouw."),
    keuze("Een land in de vierde fase heeft een histogram met een [[*smalle basis|brede basis|inkeping bovenaan]].",
          "Weinig geboorten geven smalle balken onderaan."),
]

DF_ALLEEN = [
    casus("In dorp Z worden er dit jaar 30 kinderen geboren en sterven er 45 mensen. Het dorp telt 5000 inwoners.", [
        inv("Hoe groot is het geboortecijfer in ‰?", ["6", "6 ‰"],
            "30 per 5000 = 6 per 1000."),
        inv("Hoe groot is het sterftecijfer in ‰?", ["9", "9 ‰"],
            "45 per 5000 = 9 per 1000; de natuurlijke aangroei is dus −3 ‰."),
    ]),
    tabel("Welke factoren verklaren waarom bevolkingen anders veranderen?",
          [("de welvaart en het welzijn", J), ("het beleid van de overheid", J), ("een oorlog", J), ("de lengte van de nationale vlag", F)],
          "Ook klimaat en armoede spelen mee."),
    mk("Een dorp verliest elk jaar veel jongeren die in de stad gaan werken. Wat verwacht je in het dorp?",
       ["meer ouderen en minder geboorten", "meer kleine kinderen dan vroeger", "een hoger geboortecijfer", "een snellere natuurlijke aangroei"], 0,
       "Wie vertrekt, is jong; wie blijft, wordt ouder."),
    tabel("Vergelijk de balken van de drie histogrammen. Klopt dit?",
          [("Bij A is de groep van 0 tot 10 jaar de grootste.", J), ("Bij B zijn er meer mensen van 50 tot 60 dan kinderen van 0 tot 10.", J), ("Bij C is de groep van 30 tot 40 jaar de grootste.", F)],
          "Vergelijk de breedte van de balken."),
    keuze("Wie migreert is vaak [[*jongvolwassen|bejaard|een klein kind]].",
          "Daarom verandert migratie de vorm van een histogram."),
    mk("Hoe kan een land met meer sterften dan geboorten toch groeien?",
       ["door meer mensen die er komen wonen", "door de bevolkingsdichtheid te verhogen", "door een hoger sterftecijfer", "door meer mensen te laten vertrekken"], 0,
       "Immigratie kan het tekort aan geboorten aanvullen."),
    sorteer("Waar zie je dit in een histogram?", ["onderaan", "bovenaan"],
            [("veel geboorten", "onderaan"), ("veel ouderen", "bovenaan"), ("een babyboom van vorig jaar", "onderaan"), ("een lange levensverwachting", "bovenaan")],
            "Jongeren onderaan, ouderen bovenaan."),
]

VRAGEN = ALG + DO_ALLEEN
VRAGEN_DF = ALG + DF_ALLEEN

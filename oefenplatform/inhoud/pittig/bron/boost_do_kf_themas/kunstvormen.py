"""De kunstvormen — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_kunstvormen: de vijf kunstvormen
(architectuur en design, audiovisuele kunsten, beeldende kunsten, literatuur,
podiumkunsten), hun onderverdeling, grensgevallen en samengestelde werken.
Met zelfgetekende pictogrammen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, ROOD, LICHTGROEN, ORANJE

PG = Prent("vijf-pictogrammen", "Het programma van het cultuurcentrum", "vijf vakjes met een pictogram, letters A tot E")
VK = [("A", 60), ("B", 245), ("C", 430), ("D", 615), ("E", 800)]
for t, x in VK:
    PG.rect(x, 160, 150, 300, "#ffffff", DONKER, 12, 3)
    PG.letter(x + 75, 500, t)
# A: filmcamera
PG.rect(85, 290, 90, 60, DONKER, DONKER, 6, 2); PG.cirkel(105, 270, 20, GRIJS, DONKER, 3); PG.cirkel(150, 270, 20, GRIJS, DONKER, 3)
PG.pad("M 175 305 L 200 290 L 200 350 L 175 335 Z", DONKER, DONKER, 2)
# B: danseres
PG.cirkel(320, 230, 16, ROOD, DONKER, 2); PG.lijn(320, 246, 320, 320, ROOD, 8)
PG.lijn(320, 265, 280, 240, ROOD, 6); PG.lijn(320, 265, 362, 235, ROOD, 6)
PG.lijn(320, 320, 300, 390, ROOD, 7); PG.lijn(320, 320, 365, 340, ROOD, 7)
PG.pad("M 295 320 Q 320 300 345 320 L 352 345 L 288 345 Z", ROOD, DONKER, 2)
# C: huis met plat dak en grote ramen (architectuur)
PG.rect(455, 260, 100, 130, "#ffffff", DONKER, 0, 3); PG.rect(445, 250, 120, 14, DONKER, DONKER, 0, 2)
PG.rect(470, 280, 70, 40, "#9ec7e6", DONKER, 0, 2); PG.rect(490, 340, 30, 50, "#8a6a4a", DONKER, 0, 2)
# D: open boek
PG.pad("M 635 300 Q 665 285 690 300 L 690 380 Q 665 365 635 380 Z", "#ffffff", DONKER, 3)
PG.pad("M 690 300 Q 715 285 745 300 L 745 380 Q 715 365 690 380 Z", "#ffffff", DONKER, 3)
for yy in (315, 330, 345):
    PG.lijn(645, yy, 680, yy - 4, GRIJS, 2); PG.lijn(700, yy - 4, 735, yy, GRIJS, 2)
# E: ezel met doek
PG.lijn(845, 400, 875, 230, DONKER, 4); PG.lijn(905, 400, 875, 230, DONKER, 4); PG.lijn(875, 330, 875, 410, DONKER, 4)
PG.rect(835, 250, 80, 80, "#ffffff", DONKER, 0, 3); PG.cirkel(860, 280, 12, GEEL, GEEL, 0); PG.pad("M 840 325 L 870 295 L 910 325 Z", LICHTGROEN, LICHTGROEN, 0)
U = "vijf-pictogrammen.svg"
Z = {t: [Prent.zone(x, 160, 150, 360)] for t, x in VK}

FESTIVAL = ("Lees de tekst.\n\n"
            "Het zomerfestival in de stadstuin heeft dit jaar vijf onderdelen. Op vrijdag draait er een kortfilm over de haven, "
            "gemaakt door leerlingen. Op zaterdag brengt een dansgroep een voorstelling tussen bronzen beelden van een beeldhouwer. "
            "Op zondag lezen dichters hun werk voor, terwijl een cellist speelt. De affiche en de houten zitbanken zijn ontworpen "
            "door een jonge ontwerper.")

VRAGEN = [
    klik("Bekijk het programma. Klik op het vakje van de audiovisuele kunsten.", U, Z["A"], "Een filmcamera: film, fotografie, videokunst."),
    klik("Klik op het vakje van de podiumkunsten.", U, Z["B"], "Dans gebeurt in de tijd, voor een publiek."),
    klik("Klik op het vakje van de kunstvorm die met taal werkt.", U, Z["D"], "Het boek staat voor literatuur."),
    klik("Klik op het vakje van de kunstvorm die je kan binnengaan.", U, Z["C"], "Architectuur: een gebouw is kunst die je binnengaat."),
    klik("Klik op het vakje van de schilderkunst.", U, Z["E"], "Een ezel met een doek: beeldende kunsten."),
    casus(FESTIVAL, [
        sorteer("Welke kunstvorm?", ["audiovisuele kunsten", "podiumkunsten", "beeldende kunsten", "literatuur", "architectuur en design"],
                [("de kortfilm over de haven", "audiovisuele kunsten"), ("de dansvoorstelling", "podiumkunsten"), ("de bronzen beelden", "beeldende kunsten"), ("de gedichten", "literatuur"), ("de zitbanken", "architectuur en design")],
                "Elk onderdeel hoort bij een andere kunstvorm."),
        mk("Hoe benoem je het onderdeel op zaterdag het best?",
           ["podiumkunst en beeldende kunst samen", "enkel beeldende kunst, want de beelden blijven staan", "enkel podiumkunst, want de beelden tellen niet", "audiovisuele kunst, want je ziet beweging"],
           0, "Bij één werk mag je meerdere kunstvormen benoemen."),
        keuze("Het onderdeel op zondag brengt [[*literatuur en muziek|film en dans|design en architectuur]] samen.", "Gedichten en een cellist."),
        keuze("De affiche van het festival hoort het dichtst bij [[*design|literatuur|podiumkunst]].", "Grafische vormgeving: vormgegeven én gebruikt."),
    ]),
    tabel("Hoort het bij de beeldende kunsten?",
          [("een ets", J), ("een fotoreeks", F), ("een marmeren buste", J), ("een houtsnede", J), ("een toneelstuk", F)],
          "Fotografie is audiovisueel, theater een podiumkunst."),
    koppel("Koppel het werk aan de kunstvorm.",
           [("een documentaire", "audiovisuele kunsten"), ("een fresco", "beeldende kunsten"), ("een kortverhaal", "literatuur"), ("een concert", "podiumkunsten")],
           ["natuurkunde"],
           "Vijf kunstvormen, elk met eigen middelen."),
    mk("Waarom is een podiumkunst anders dan een schilderij?",
       ["een voorstelling duurt en is daarna voorbij", "een voorstelling is altijd duurder dan een schilderij", "een schilderij heeft nooit een publiek nodig", "een schilderij is altijd ouder dan een voorstelling"],
       0, "Podiumkunsten gebeuren in de tijd."),
    keuze("Een toneeltekst wordt pas podiumkunst als [[*iemand ze uitvoert|iemand ze koopt|ze gedrukt wordt]].", "De podiumkunst heeft een uitvoerder nodig."),
    tabel("Klopt dit over de kunstvormen?",
          [("Er zijn vijf kunstvormen.", J), ("Fotografie hoort bij de beeldende kunsten.", F), ("Eén werk kan bij meerdere kunstvormen horen.", J), ("Er is een rangorde: architectuur is de hoogste.", F)],
          "Er is geen rangorde tussen de kunstvormen."),
    mk("Een film noemt men een samengestelde kunstvorm. Waarom?",
       ["beeld, muziek, tekst en vormgeving komen samen", "hij wordt door één persoon helemaal alleen gemaakt", "hij duurt altijd langer dan twee uur", "hij wordt altijd in een bioscoop getoond"],
       0, "Dat maakt de analyse rijker."),
    sleep("De vijf kunstvormen zijn: architectuur en [[design]], de [[audiovisuele]] kunsten, de beeldende kunsten, de [[literatuur]] en de [[podiumkunsten]].",
          ["wetenschap", "sport"], "Vijf vormen, elk met eigen middelen."),
    keuze("Een stoel van een ontwerper hoort bij [[*architectuur en design|de beeldende kunsten|de podiumkunsten]].", "Of hij ook kunst is, beredeneer je met de criteria."),
    mk("Een installatie met beelden, geluid en voorwerpen in één zaal. Wat doe je?",
       ["je benoemt meerdere kunstvormen", "je kiest willekeurig één kunstvorm", "je zegt dat het geen kunst kan zijn", "je benoemt enkel de duurste kunstvorm"],
       0, "Grensgevallen mogen; benoem dan meerdere vormen."),
    inv("Bij welke kunstvorm hoort animatie? Eén woord.", ["audiovisuele", "audiovisueel", "audiovisuele kunsten"], "De audiovisuele kunsten."),
    keuze("Een striptekening hoort bij [[*de beeldende kunsten|de podiumkunsten|de architectuur]], en met de tekst erbij raakt ze aan de literatuur.", "Een strip is getekend."),
    sorteer("Laat het werk iets tastbaars na?", ["blijft staan", "is voorbij na de uitvoering"],
            [("een gebouw", "blijft staan"), ("een dansvoorstelling", "is voorbij na de uitvoering"), ("een beeld in brons", "blijft staan"), ("een concert", "is voorbij na de uitvoering"), ("een ontworpen lamp", "blijft staan")],
            "Beeldende kunst, architectuur en design laten iets na."),
    volgorde("Zet de eerste stappen van een kunstanalyse in de juiste volgorde.",
             ["de kunstvorm bepalen", "de periode en de stroming bepalen", "de inhoud en de context onderzoeken"],
             "De kunstvorm is de eerste ordening."),
    mk("Waarom krijgen beeldende kunst en architectuur elk eigen richtvragen?",
       ["ze werken met eigen middelen", "ze zijn allebei ouder dan film", "ze worden door dezelfde mensen gemaakt", "ze zijn allebei heel duur om te maken"],
       0, "Elke kunstvorm heeft eigen bouwstenen, materialen en technieken."),
    keuze("Een luisterspel op de radio brengt [[*literatuur en muziek|beeldende kunst en dans|architectuur en film]] samen.", "Tekst en geluid, geen beeld."),
    tabel("Hoort het bij de podiumkunsten?",
          [("een opera", J), ("een ballet", J), ("een olieverfdoek", F), ("een stand-upcomedyshow", J)],
          "Een olieverfdoek is beeldende kunst."),
    open_("Kies een werk dat bij twee kunstvormen hoort. Leg uit welke twee en waarom.",
          "Een opera: het is podiumkunst, want zangers voeren ze uit voor een publiek, en literatuur, want er is een tekst, het libretto."),
    inv("Bij welke kunstvorm hoort een stadhuis uit de zestiende eeuw? Eén woord.", ["architectuur", "de architectuur"], "Een gebouw met vormgeving en een functie."),
    keuze("Videokunst en film zijn [[*aparte onderdelen binnen dezelfde kunstvorm|precies hetzelfde|twee verschillende kunstvormen]].", "Allebei audiovisuele kunsten."),
    tabel("Is dit audiovisuele kunst?",
          [("een kortfilm", J), ("een fotoreeks", J), ("een ets", F), ("een videoinstallatie", J)],
          "Een ets is grafiek, dus beeldende kunst."),
    keuze("Een fresco op een kerkmuur is [[*schilderkunst|architectuur|literatuur]]; de kerk eromheen is architectuur.", "Het is geschilderd."),
]

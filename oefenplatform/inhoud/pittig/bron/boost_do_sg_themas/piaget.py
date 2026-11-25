"""De cognitieve ontwikkeling volgens Piaget — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_piaget: de vier stadia met hun kenmerken en
het stadium bepalen uit een voorbeeld. Met een zelfgetekende proeftafel."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ROOD, LICHTGROEN, ORANJE

PT = Prent("proeftafel-piaget", "Een proeftafel met glazen en stokjes", "twee glazen met water (D en E) en drie rijen stokjes (A tot C)")
# twee glazen, evenveel water
PT.rect(170, 110, 70, 230, "#ffffff", DONKER, 4, 3); PT.rect(173, 200, 64, 137, "#9ec7e6", "none", 0, 0)
PT.rect(330, 230, 180, 110, "#ffffff", DONKER, 4, 3); PT.rect(333, 287, 174, 50, "#9ec7e6", "none", 0, 0)
PT.lijn(120, 342, 560, 342, "#8a8470", 3)
PT.letter(205, 385, "D"); PT.letter(420, 385, "E")
# drie rijen stokjes
RIJEN = {
    "A": [(110, ROOD), (60, BLAUW), (150, ROOD), (90, BLAUW), (40, ROOD), (130, BLAUW)],
    "B": [(40, ROOD), (60, BLAUW), (90, ROOD), (110, BLAUW), (130, ROOD), (150, BLAUW)],
    "C": [(110, ROOD), (150, ROOD), (40, ROOD), (60, BLAUW), (130, BLAUW), (90, BLAUW)],
}
for i, (t, stokjes) in enumerate(RIJEN.items()):
    y0 = 200 + i * 175
    for k, (h, kl) in enumerate(stokjes):
        h = int(h * 0.8)
        x = 630 + k * 42 + (25 if t == "C" and k >= 3 else 0)
        PT.rect(x, y0 - h, 22, h, kl, DONKER, 3, 2)
    PT.lijn(615, y0, 920, y0, "#8a8470", 2)
    PT.letter(945, y0 - 40, t)
U = "proeftafel-piaget.svg"
Z = {"D": [Prent.zone(150, 100, 110, 310)], "E": [Prent.zone(320, 220, 200, 190)]}
for i, t in enumerate("ABC"):
    y0 = 200 + i * 175
    Z[t] = [Prent.zone(610, y0 - 130, 360, 140)]

KLEI = ("Lees het verslag van een proef.\n\n"
        "Een onderzoeker toont Mo (vijf jaar) en Sara (negen jaar) twee even grote bollen klei. Hij rolt één bol uit tot een lange worst. "
        "Mo zegt: « Nu is er meer klei, want hij is langer. » Sara zegt: « Het is evenveel. Als je de worst terug oprolt, heb je weer dezelfde bol. »")

VRAGEN = [
    klik("Bekijk de proeftafel. In beide glazen zit evenveel water. Klik op het glas waarvan een kleuter zegt dat er meer in zit.", U, Z["D"], "Hij kijkt enkel naar de hoogte: centratie."),
    klik("Klik op de rij stokjes die gesorteerd is van klein naar groot.", U, Z["B"], "Seriatie."),
    klik("Klik op de rij stokjes die in groepen volgens kleur verdeeld is.", U, Z["C"], "Classificatie."),
    casus(KLEI, [
        sorteer("In welk stadium van Piaget zit dit kind?", ["pre-operationeel", "concreet-operationeel"],
                [("Mo", "pre-operationeel"), ("Sara", "concreet-operationeel")],
                "Mo heeft de conservatienotie nog niet, Sara wel."),
        keuze("Mo kijkt enkel naar de lengte van de worst. Dat heet [[*centratie|animisme|seriatie]].", "Op één kenmerk letten en de rest vergeten."),
        keuze("Sara draait de bewerking in gedachten terug. Dat is [[*reversibel denken|magisch denken|egocentrisme]].", "Wie de worst terug oprolt, heeft weer de bol."),
        mk("Welke notie heeft Sara wel en Mo nog niet?",
           ["de conservatienotie", "de objectpermanentie, want Mo ziet de klei niet meer", "het abstract denken over iets dat je niet ziet", "het hypothetisch denken in als-dan"],
           0, "De hoeveelheid blijft, ook als de vorm verandert."),
    ]),
    volgorde("Zet de stadia van Piaget in de juiste volgorde.",
             ["sensomotorisch", "pre-operationeel", "concreet-operationeel", "formeel-operationeel"],
             "Van de geboorte tot de adolescentie."),
    sorteer("Welk stadium volgens Piaget?", ["sensomotorisch", "pre-operationeel", "concreet-operationeel", "formeel-operationeel"],
            [("Een baby zoekt een bal die onder een doek verdween.", "sensomotorisch"), ("Een kleuter gebruikt een doos als auto.", "pre-operationeel"), ("Een kind legt blokken van klein naar groot.", "concreet-operationeel"), ("Een jongere denkt na over wat rechtvaardigheid is.", "formeel-operationeel")],
            "Telkens het kenmerk dat het stadium verraadt."),
    sorteer("Welke denkfout van de kleuter?", ["animisme", "magisch denken", "egocentrisme"],
            [("'De maan loopt achter mij aan omdat ze mij leuk vindt.'", "animisme"), ("'Oma werd ziek omdat ik boos op haar was.'", "magisch denken"), ("Hij houdt een tekening naar zich toe en vraagt of jij ze mooi vindt.", "egocentrisme"), ("'Mijn knuffel is verdrietig als ik hem alleen laat.'", "animisme")],
            "Drie denkfouten van het pre-operationeel stadium."),
    koppel("Koppel het begrip aan het voorbeeld.",
           [("objectpermanentie", "een baby tilt een doek op om een speeltje te zoeken"), ("symbolisch denken", "een kleuter gebruikt een stok als zwaard"), ("transitief redeneren", "An > Bo en Bo > Cis, dus An > Cis"), ("experimenteel denken", "één factor veranderen en de rest gelijk houden")],
           ["een kind wordt tien centimeter groter"], "Elk begrip hoort bij een ander stadium."),
    mk("Waarom noemt Piaget het stadium van de kleuter pre-operationeel?",
       ["logische bewerkingen komen nog niet", "omdat kleuters nog niet kunnen praten", "omdat kleuters nog geen zintuigen gebruiken", "omdat het kind dan nog niet naar school gaat"],
       0, "Operaties zijn logische bewerkingen in het hoofd."),
    tabel("Klopt dit over Piaget?",
          [("Egocentrisme betekent bij Piaget dat een kleuter egoïstisch is.", F), ("Een kind van negen denkt nog moeilijk over iets dat het nooit zag.", J), ("Iedereen gebruikt het formeel-operationeel denken in elk vak.", F), ("Persoonspermanentie kan scheidingsangst meebrengen.", J)],
          "Egocentrisme is enkel je eigen standpunt kunnen innemen."),
    keuze("Een kind van elf begrijpt breuken met stukken pizza, maar niet zonder. Het zit in het [[*concreet-operationeel|formeel-operationeel|pre-operationeel]] stadium.", "Zijn logica heeft nog iets concreets nodig."),
    keuze("'Stel dat er geen zwaartekracht was, wat zou er dan gebeuren?' Wie zo denkt, denkt [[*hypothetisch|magisch|egocentrisch]].", "Denken in als-dan."),
    inv("Hoe heet het weten dat iets blijft bestaan als je het niet ziet? Eén woord.", ["objectpermanentie"], "Rond acht maanden zoekt een baby naar een verstopte bal."),
    mk("Waarom kan een adolescent over de toekomst piekeren en een kleuter veel minder?",
       ["hij denkt over wat nog niet is", "omdat een kleuter nog geen geheugen heeft", "omdat een adolescent in het sensomotorisch stadium zit", "omdat een kleuter de toekomst al kent"],
       0, "Hypothetisch denken opent de toekomst, en dus ook de zorgen."),
    tabel("Hoort dit bij het concreet-operationeel stadium?",
          [("seriatie", J), ("classificatie", J), ("animisme", F), ("conservatie", J), ("objectpermanentie leren", F)],
          "Animisme is van de kleuter, objectpermanentie van de baby."),
    keuze("Een kind kan uitleggen hoe zijn zus aan de andere kant van de tafel het blokkenhuis ziet. Het kan nu [[*een ander perspectief nemen|enkel aan zichzelf denken|nog niet logisch denken]].", "Het egocentrisme is voorbij."),
    keuze("Een baby schudt een rammelaar om het geluid te horen. Dat is [[*intentioneel handelen|een reflex|symbolisch denken]].", "Iets doen met een doel."),
    sleep("Een kleuter met [[centratie]] kijkt enkel naar de hoogte. Een schoolkind dat [[decentreert]], ziet de hoogte én de [[breedte]].",
          ["seriatie", "kleur"], "Decentreren is het tegendeel van centratie."),
    mk("Een leerkracht legt de breuken uit met een taart in stukken. Waarom past dat bij een kind van acht?",
       ["het denkt logisch over iets concreets", "het denkt al volledig abstract zonder voorbeelden", "het is nog in het sensomotorisch stadium", "het kan nog geen hoeveelheden vergelijken"],
       0, "Wie het stadium kent, kan de uitleg erop afstemmen."),
    tabel("Bij welk stadium hoort deze leeftijd ongeveer?",
          [("0 tot 2 jaar", "sensomotorisch"), ("2 tot 7 jaar", "pre-operationeel"), ("7 tot 12 jaar", "concreet-operationeel"), ("vanaf 12 jaar", "formeel-operationeel")],
          "De orde ligt vast, het tempo niet helemaal.", ["sensomotorisch", "pre-operationeel", "concreet-operationeel", "formeel-operationeel"]),
    keuze("Een kleuter is echt bang van een monster onder zijn bed. Voor hem zijn fantasie en werkelijkheid [[*niet altijd gescheiden|altijd goed gescheiden]].", "Dat hoort bij het pre-operationeel stadium."),
    keuze("Een adolescent zet een proef op: hij verandert enkel de hoeveelheid licht en houdt water en grond gelijk. Dat is [[*experimenteel denken|magisch denken|centratie]].", "Eén factor veranderen, de rest gelijk."),
    tabel("Hoort dit bij het sensomotorisch stadium?",
          [("objectpermanentie", J), ("persoonspermanentie", J), ("imiteren wat je gezien hebt", J), ("abstract denken", F)],
          "Abstract denken komt pas in het laatste stadium."),
    keuze("'Wie weet dat 3 + 4 = 7, weet ook dat 7 − 4 = 3.' Dat is [[*reversibel|egocentrisch|symbolisch]] denken.", "Een bewerking in gedachten terugdraaien."),
    inv("Hoe heet het eerste stadium van Piaget? Eén woord.", ["sensomotorisch", "sensomotorische", "het sensomotorisch stadium"], "Denken met zintuigen en bewegingen."),
    mk("Een kind van zes ziet een broertje een glas water omgieten in een breed glas en roept: 'Nu heeft hij minder!' Wat ziet het kind nog niet?",
       ["de begin- en de eindtoestand samen", "dat water nat is en op de grond kan vallen", "dat zijn broertje een ander standpunt heeft", "dat het glas uit glas gemaakt is"],
       0, "Aandacht voor begin- en eindtoestand komt in het concreet-operationeel stadium."),
    open_("Beschrijf de proef met de twee glazen water van Piaget en leg uit wat een kleuter en een kind van negen antwoorden.",
          "Je giet evenveel water in een smal, hoog glas en in een breed, laag glas. Een kleuter zegt dat er meer in het hoge glas zit: hij let enkel op de hoogte (centratie) en heeft de conservatienotie nog niet. Een kind van negen zegt dat het evenveel is: het let op hoogte en breedte en kan het overgieten in gedachten terugdraaien."),
]

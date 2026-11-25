"""Het denken volgens Piaget — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_piaget: de vier stadia met hun kenmerken, de denkfouten van
peuters en kleuters, de conservatienotie en de taalontwikkeling tot drie
jaar. Met een zelfgetekende trap van vier treden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

TR = Prent("trap-vier-treden", "Vier treden van het denken", "een trap van vier treden die van links naar rechts oploopt, letters A tot D")
Z = {}
for i, t in enumerate("ABCD"):
    x, h = 90 + i * 210, 110 + i * 110
    TR.rect(x, 560 - h, 210, h, LICHTGROEN, DONKER, 6, 3)
    TR.letter(x + 105, 560 - h + 40, t)
    Z[t] = [Prent.zone(x, 560 - h, 210, h)]
TR.pijl(90, 600, 930, 600, DONKER, 3)
TR.tekst(510, 630, "ouder worden", 18)
U = "trap-vier-treden.svg"

SITUATIE = ("Lees de situatie.\n\n"
            "Juf Sofie giet water uit een breed, laag glas in een hoog, smal glas. Kato (4) roept: 'Nu is er meer!' "
            "Haar broer Jules (8) lacht: 'Nee, het is evenveel. Je kan het gewoon terug gieten.' Hun zusje van acht maanden kijkt vanuit haar stoeltje toe.")

VRAGEN = [
    klik("Bekijk de trap: elke trede is een stadium van Piaget. Een baby zoekt een bal die onder een deken verdween. Klik op zijn trede.", U, Z["A"], "Objectpermanentie hoort bij het sensomotorische stadium."),
    klik("Een kleuter zegt dat de maan met hem meewandelt. Klik op zijn trede.", U, Z["B"], "Magisch denken en egocentrisme horen bij het pre-operationele stadium."),
    klik("Een kind van negen rekent met blokjes en weet dat water in een smaller glas evenveel blijft. Klik op zijn trede.", U, Z["C"], "Logisch denken over concrete dingen: concreet-operationeel."),
    klik("Een tiener bedenkt wat er zou gebeuren als er geen zwaartekracht was. Klik op zijn trede.", U, Z["D"], "Hypothetisch denken hoort bij het formeel-operationele stadium."),
    sorteer("Welke denkfout van een kleuter?", ["animisme", "magisch denken", "egocentrisme", "centratie"],
            [("'De stoel is stout, want ik stootte mijn knie.'", "animisme"), ("'Als ik heel hard wens dat het sneeuwt, gaat het sneeuwen.'", "magisch denken"), ("Een kleuter houdt een tekening omhoog aan de telefoon om ze aan oma te tonen.", "egocentrisme"), ("Een kleuter denkt dat het hoge, smalle glas meer drank bevat.", "centratie"), ("'De zon gaat slapen omdat ze moe is.'", "animisme")],
            "Gevoelens aan dingen geven, wensen die iets doen gebeuren, enkel de eigen kijk, en op één kenmerk letten."),
    casus(SITUATIE, [
        keuze("Kato let enkel op de hoogte van het glas. Dat is [[*centratie|animisme|seriatie]].", "Ze ziet niet dat het glas ook smaller is."),
        keuze("Jules begrijpt de [[*conservatienotie|objectpermanentie|persoonspermanentie]].", "De hoeveelheid blijft gelijk, ook al verandert de vorm."),
        keuze("'Je kan het gewoon terug gieten' toont [[*reversibel denken|magisch denken|hypothetisch denken]].", "Hij draait de handeling in gedachten terug."),
        tabel("In welk stadium zit elk kind?",
              [("Kato", "pre-operationeel"), ("Jules", "concreet-operationeel"), ("hun zusje van acht maanden", "sensomotorisch")],
              "Kleuter, lagereschoolkind en baby.", ["sensomotorisch", "pre-operationeel", "concreet-operationeel"]),
    ]),
    koppel("Koppel het begrip aan het voorbeeld.",
           [("decentreren", "op meer dan één kenmerk tegelijk letten"), ("classificatie", "dieren verdelen in vogels en vissen"), ("symbolisch denken", "een kartonnen doos wordt een raceauto"), ("intentioneel handelen", "aan een dekentje trekken om het speeltje erop dichterbij te halen")],
           ["een wens laten uitkomen"],
           "Een wens die iets laat gebeuren, is magisch denken: een denkfout, geen vaardigheid."),
    volgorde("Zet de stadia van Piaget in de juiste volgorde.",
             ["sensomotorisch", "pre-operationeel", "concreet-operationeel", "formeel-operationeel"],
             "Baby, kleuter, lagereschoolkind, adolescent."),
    volgorde("Zet de stappen in de taalontwikkeling van nul tot drie jaar in de juiste volgorde.",
             ["huilen en brabbelen", "een eerste woordje", "tweewoordzinnen", "korte zinnen"],
             "Rond één jaar het eerste woordje, rond twee jaar tweewoordzinnen."),
    mk("Een baby van drie maanden kijkt niet meer naar een speeltje dat onder een doek verdwijnt. Wat heeft hij nog niet?",
       ["objectpermanentie", "de conservatienotie", "reversibel denken", "hypothetisch denken"],
       0, "Uit het oog is voor hem nog uit het hart."),
    tabel("Kan een kind van zeven dit meestal al?",
          [("rekenen met blokjes", J), ("een abstracte formule met letters oplossen", F), ("dingen in groepen indelen", J), ("redeneren over iets wat nooit gebeurd is", F)],
          "Logisch, maar nog over wat het kan zien of vastnemen."),
    inv("Hoe noem je de denkfout waarbij een kind denkt dat zijn wens iets kan doen gebeuren? Twee woorden.", ["magisch denken", "het magisch denken"], "Magisch denken."),
    keuze("Een kind van zeven heeft nog blokjes nodig om te rekenen. Het denkt [[*concreet|abstract|hypothetisch]].", "Het moet het kunnen zien of vastnemen."),
    mk("Wat is het verschil tussen egocentrisme en egoïsme bij een kleuter?",
       ["een egocentrische kleuter kan zich nog niet in een ander inleven", "een egocentrische kleuter wil bewust en met opzet alles voor zichzelf alleen houden", "egocentrisme en egoïsme betekenen precies hetzelfde", "egoïsme komt enkel voor bij baby's"],
       0, "Egocentrisme is geen slechte wil: de kleuter kent gewoon enkel zijn eigen kijk."),
    tabel("Klopt dit over het formeel-operationele stadium?",
          [("Een adolescent kan denken in 'wat als'.", J), ("Abstract denken lukt pas in dit stadium.", J), ("Objectpermanentie ontstaat in dit stadium.", F), ("Een adolescent kan zelf een proefje bedenken om iets te testen.", J), ("Een adolescent heeft altijd blokjes nodig om te rekenen.", F)],
          "Objectpermanentie hoort bij de baby."),
    keuze("Een kind laat een stok een paard zijn. Dat komt uit het [[*symbolisch denken|reversibel denken|hypothetisch denken]].", "Het ene ding staat voor het andere."),
    sleep("Een baby zit in het [[sensomotorische]] stadium, een kleuter in het [[pre-operationele]], een lagereschoolkind in het [[concreet-operationele]] en een adolescent in het [[formeel-operationele]].",
          ["post-conventionele"],
          "Post-conventioneel is een stadium van Kohlberg."),
    keuze("Rond twee jaar spreekt een kind meestal in [[*tweewoordzinnen|lange verhalen|volledige brieven]].", "'Mama weg', 'nog koek'."),
    mk("Een kleuter bedekt zijn ogen en denkt dat niemand hem nu ziet. Welke denkfout is dat?",
       ["egocentrisme", "animisme", "seriatie", "classificatie"],
       0, "Wat hij niet ziet, ziet volgens hem ook niemand anders."),
    tabel("Hoort dit bij het pre-operationele stadium?",
          [("veel fantasie", J), ("systematisch denken", F), ("doen-alsof-spel", J), ("hypothetisch denken", F)],
          "Systematisch denken komt in het concreet-operationele stadium."),
    keuze("Een kind dat begrijpt dat 3 + 4 = 7 ook betekent dat 7 − 4 = 3, denkt [[*reversibel|magisch|egocentrisch]].", "Het kan de handeling in gedachten terugdraaien."),
    inv("Hoe noem je het besef dat een vertrouwd persoon blijft bestaan als die de kamer uitgaat? Eén woord.", ["persoonspermanentie", "de persoonspermanentie"], "Persoonspermanentie."),
    mk("Waarom snapt een kleuter de conservatienotie nog niet?",
       ["hij let maar op één kenmerk tegelijk", "hij kan nog niet tot tien tellen", "hij heeft nog nooit water in een glas gezien", "hij denkt al te abstract voor zijn leeftijd"],
       0, "Door centratie ziet hij enkel dat het glas hoger is."),
    keuze("Een kind van tien legt zijn knikkers op een rij van klein naar groot. Dat is [[*seriatie|classificatie|animisme]].", "Ordenen op grootte."),
    mk("Welke zin past bij een kind in het sensomotorische stadium?",
       ["het leert de wereld kennen door te voelen, proeven en bewegen", "het lost moeilijke raadsels op met logische en abstracte redeneringen", "het denkt na over rechtvaardigheid in de wereld", "het kan al vlot lezen en schrijven in korte zinnen"],
       0, "Zintuigen en bewegingen zijn zijn manier om te leren."),
    keuze("Piaget beschrijft de [[*cognitieve|morele|fysieke]] ontwikkeling.", "De ontwikkeling van het denken."),
    open_("Bedenk voor kleuters een spelletje dat past bij het pre-operationele stadium. Leg uit waarom het past.",
          "Winkeltje spelen met lege dozen en papieren geld. Kleuters denken symbolisch en hebben veel fantasie, dus een doos wordt gemakkelijk een pak melk."),
]

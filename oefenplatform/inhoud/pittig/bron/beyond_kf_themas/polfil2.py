"""Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid — pittig
(🌍 Beyond doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_polfil2.py: rechtvaardigheid bij Aristoteles, het sociaal
contract (Hobbes, Locke, Rousseau), Rawls, individuele en culturele
politieke gelijkheid, Mill, Berlin, Arendt en de kritiek van Tronto."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD

# Prent: twee soorten vrijheid -----------------------------------------------------------
VR = Prent("twee-vrijheden", "Twee manieren om vrij te zijn",
           "A een weg met een slagboom die opengaat: niemand houdt je nog tegen; B een trap met boeken en gereedschap op de treden, waarmee iemand zelf naar boven klimt naar een doel")
PANEEL = {}
for letter, x in (("A", 40), ("B", 520)):
    VR.rect(x, 70, 440, 460, "#fbfaf5", DONKER, 10, 3)
    VR.letter(x + 220, 585, letter)
    PANEEL[letter] = (x, 70, 440, 460)
# A: weg met open slagboom
VR.pad("M 60 520 L 200 260 L 320 260 L 460 520 Z", "#d9d4c4", DONKER, 2)
VR.lijn(260, 500, 260, 290, "#ffffff", 4, stippel=True)
VR.rect(330, 300, 18, 120, DONKER, DONKER, 0, 1)
VR.pad("M 339 305 L 420 150", "none", ROOD, 12)
VR.pad("M 339 305 L 420 150", "none", "#ffffff", 4)
VR.cirkel(200, 440, 16, "#f1d9b5", DONKER, 2)
VR.lijn(200, 456, 200, 500, BLAUW, 8)
VR.pijl(225, 470, 260, 380, DONKER, 3)
# B: trap met middelen
for i in range(5):
    VR.rect(560 + i * 70, 470 - i * 70, 70 + (4 - i) * 0, 60 + i * 70, "#e9e2cf", DONKER, 0, 2)
VR.rect(575, 445, 40, 22, BLAUW, DONKER, 2, 1)
VR.rect(645, 375, 40, 22, ORANJE, DONKER, 2, 1)
VR.rect(715, 305, 40, 22, LICHTGROEN, DONKER, 2, 1)
VR.cirkel(870, 160, 26, GEEL, DONKER, 2)
VR.cirkel(670, 330, 15, "#f1d9b5", DONKER, 2)
VR.lijn(670, 345, 670, 380, BLAUW, 8)


def vz(l):
    return [Prent.zone(*PANEEL[l])]


VRAGEN = [
    klik("Klik op het beeld dat negatieve vrijheid voorstelt.", VR.bestand, vz("A"),
         "Negatieve vrijheid is vrij zijn van inmenging: de slagboom gaat open, niemand houdt je nog tegen."),
    klik("Klik op het beeld dat positieve vrijheid voorstelt.", VR.bestand, vz("B"),
         "Positieve vrijheid is vrij zijn tot iets: je eigen leven sturen, soms met middelen zoals onderwijs."),
    met_prent(VR.bestand, keuze("Gratis onderwijs voor iedereen past het best bij beeld [[*B|A]]. Een verbod op betogen afschaffen past het best bij beeld [[*A|B]].",
              "Middelen krijgen versterkt de positieve vrijheid. Een belemmering wegnemen versterkt de negatieve vrijheid.")),
    met_prent(VR.bestand, mk("Welk gevaar ziet Berlin bij een te sterke nadruk op het idee achter beeld B?",
              ["dwang in naam van je 'ware' vrijheid", "mensen krijgen dan te weinig onderwijs en kansen",
               "de staat verdwijnt dan helemaal en er komen geen wetten", "niemand mag dan nog stemmen of zich verkiesbaar stellen"], 0,
              "Wie beweert beter te weten wat je echt wilt, kan zo dwang goedpraten.")),
    sorteer("Verdelende of herstellende rechtvaardigheid bij Aristoteles?", ["verdelend", "herstellend"], [
        ["eer en goederen verdelen naar verdienste", "verdelend"],
        ["een gebroken fiets vergoeden", "herstellend"],
        ["wie meer bijdraagt, krijgt meer", "verdelend"],
        ["een schade rechtzetten, wie de dader ook is", "herstellend"],
        ["gelijken gelijk, ongelijken ongelijk behandelen", "verdelend"],
    ], "Verdelende rechtvaardigheid gaat in verhouding. Herstellende rechtvaardigheid zet een onrecht recht."),
    koppel("Koppel de denker aan zijn idee van het sociaal contract.", [
        ["Hobbes", "vrijheid afstaan voor veiligheid"],
        ["Locke", "de staat beschermt leven, vrijheid en eigendom"],
        ["Rousseau", "het volk bestuurt zichzelf via de algemene wil"],
    ], ["de soeverein beslist over vriend en vijand"], "Het vriend-vijandonderscheid hoort bij Schmitt, niet bij de contractdenkers."),
    casus(
        "Stel: je moet de regels kiezen voor een nieuwe samenleving. Je weet niet of je er rijk of arm, gezond of ziek, "
        "man of vrouw, gelovig of niet gelovig zult zijn. Pas als de regels vastliggen, hoor je welke plaats je krijgt.",
        [
            inv("Hoe heet dit gedachte-experiment van Rawls? De sluier van ...", ["onwetendheid"],
                "Wie zijn eigen plaats niet kent, kiest eerlijke regels voor iedereen."),
            tabel("Welke regel zou je volgens Rawls kiezen?", [
                ("Iedereen krijgt dezelfde basisvrijheden.", J),
                ("Ongelijkheid mag als ze ook de minst bevoordeelden helpt.", J),
                ("Wie het sterkst is, beslist alles alleen.", F),
            ], "Dat zijn het vrijheidsbeginsel en het verschilbeginsel.",
               kolommen=None),
            mk("Waarom kies je zo voor goede zorg voor wie het slechtst af is?",
               ["je kunt zelf bij de zwaksten horen", "je bent van nature heel vrijgevig en altijd goed",
                "een sterke vorst verplicht je ertoe", "je krijgt er achteraf een beloning voor van de staat"], 0,
               "Uit voorzichtigheid kies je regels die ook goed zijn als je het slechtst terechtkomt."),
        ],
    ),
    tabel("Individuele of culturele politieke gelijkheid?", [
        ("één persoon, één stem, welke afkomst ook", "individueel"),
        ("onderwijs in de eigen taal voor een minderheid", "cultureel"),
        ("dezelfde rechten voor elke burger", "individueel"),
        ("erkenning van de identiteit van een groep", "cultureel"),
    ], "Het liberalisme kijkt naar het individu, het communitarisme ook naar de groep en haar cultuur.",
       kolommen=["individueel", "cultureel"]),
    keuze("Volgens het schadebeginsel van [[*Mill|Rawls|Hobbes]] mag de staat je vrijheid enkel beperken om [[*schade aan anderen|schade aan jezelf|een slechte smaak]] te voorkomen.",
          "Over wat enkel jezelf aangaat, beslis je zelf. Mill schreef On Liberty in 1859."),
    tabel("Mag de staat dit verbieden volgens het schadebeginsel van Mill?", [
        ("dronken autorijden", J),
        ("alleen thuis heel ongezond eten", F),
        ("een gevaarlijke sport beoefenen die enkel jezelf kan verwonden", F),
        ("fabrieksafval in een rivier lozen", J),
    ], "Mill trekt de grens bij schade aan anderen. Wat enkel jezelf aangaat, beslis je zelf."),
    tabel("Klopt dit over Mill?", [
        ("Vrije meningsuiting helpt volgens Mill om de waarheid te vinden.", J),
        ("Volgens Mill mag de staat je verbieden iets te doen wat enkel jezelf schaadt.", F),
        ("Ook een foute mening kan helpen de waarheid scherper te zien.", J),
    ], "Mill verdedigt de vrijheid van denken en spreken."),
    mk("Jongeren starten samen een actie, spreken op een gemeenteraad en zetten een nieuw jeugdhuis op. Welke denker ziet net dit als politieke vrijheid?",
       ["Arendt", "Hobbes", "Schmitt", "Hume"], 0,
       "Voor Hannah Arendt toont vrijheid zich als mensen samen handelen en spreken in de publieke ruimte."),
    tabel("Klopt dit over Hannah Arendt?", [
        ("Vrijheid is voor haar iets wat je samen met anderen doet.", J),
        ("Vrijheid betekent voor haar dat je je terugtrekt uit de politiek.", F),
        ("Iets nieuws beginnen in de publieke ruimte is voor haar een vorm van vrijheid.", J),
    ], "Handelen, spreken en samen iets nieuws beginnen staan centraal bij Arendt."),
    casus(
        "In een land werken vooral vrouwen, migranten en laagbetaalde werknemers in de zorg voor ouderen en kinderen. Hun loon is laag en hun werk krijgt weinig erkenning. "
        "Rijke gezinnen huren hulp in en denken zelf nauwelijks na over wie voor hun ouders zorgt.",
        [
            mk("Welke denker geeft kritiek op deze manier van zorg organiseren?",
               ["Tronto", "Hobbes", "Mill", "Schmitt"], 0,
               "Joan Tronto vindt dat zorg een publieke, politieke zaak is die eerlijk verdeeld moet worden."),
            inv("Hoe noemt Tronto het gedrag van de rijke gezinnen? Bevoorrechte ...", ["onverantwoordelijkheid"],
                "Wie macht of geld heeft, schuift zorgtaken door en ontloopt zo de verantwoordelijkheid."),
            keuze("Tronto zegt dat zorgwerk [[*ondergewaardeerd|overbetaald|overbodig]] is, en dat zorg geen privézaak is maar een [[*politieke|economische|religieuze]] zaak.",
                  "Wie zorgt en wie zorg krijgt, hangt samen met macht en verdeling."),
        ],
    ),
    sleep("Rawls noemt het beginsel dat ongelijkheid enkel toelaat als ze de minst bevoordeelden helpt, het [[verschilbeginsel]]. Samen met gelijke [[basisvrijheden]] vormt het zijn grondbeginselen.",
          ["schadebeginsel", "algemene wil"], "Rawls' rechtvaardigheid gaat over de basisstructuur van de samenleving."),
    mk("Een school geeft een leerling met dyslexie extra tijd bij een examen. Welk idee past hier het best?",
       ["gelijke kansen, zoals bij Rawls", "herstel van schade, zoals bij een rechtbank",
        "iedereen exact hetzelfde behandelen", "de sterkste leerling krijgt het meeste tijd"], 0,
       "Gelijk behandelen is hier niet eerlijk. Wat extra steun maakt de kansen gelijker."),
    keuze("Rechtvaardigheid in algemene zin is voor Aristoteles [[*de wetten volgen en bijdragen aan het goede leven van allen|iedereen exact hetzelfde geven|het eigen voordeel zoeken]]. In specifieke zin gaat het om [[*verdelen en herstellen|stemmen en betogen|kopen en verkopen]].",
          "Aristoteles onderscheidt rechtvaardigheid in algemene en in specifieke zin."),
    tabel("Positieve of negatieve vrijheid?", [
        ("niemand verbiedt je om te reizen", "negatief"),
        ("je krijgt een beurs zodat je kunt studeren", "positief"),
        ("de censuur op kranten wordt afgeschaft", "negatief"),
        ("je leert lezen zodat je zelf kunt kiezen wat je leest", "positief"),
    ], "Negatief: geen inmenging. Positief: in staat zijn om je leven zelf te sturen.",
       kolommen=["positief", "negatief"]),
    mk("Een land zegt: 'Iedereen is vrij om naar de universiteit te gaan', maar het inschrijvingsgeld is heel hoog. Welke kritiek past hier?",
       ["vrij op papier, maar zonder middelen", "de staat bemoeit zich met elk detail van je leven",
        "niemand mag er nog een eigen mening uiten", "iedereen krijgt er hetzelfde werk en dezelfde opleiding"], 0,
       "Niemand houdt je tegen om te studeren, maar zonder geld of steun lukt het misschien niet."),
    volgorde("In welke volgorde leefden deze denkers over rechtvaardigheid en vrijheid?", [
        "Aristoteles", "Hobbes", "Locke", "Rousseau", "Mill", "Rawls",
    ], "Van de Griekse oudheid via de 17de, 18de en 19de eeuw naar 1971."),
    mk("Waarom is gelijk niet hetzelfde als identiek bij Aristoteles' verdelende rechtvaardigheid?",
       ["wie meer bijdraagt, krijgt in verhouding meer", "iedereen krijgt altijd exact hetzelfde bedrag",
        "de sterkste in de stad beslist wat eerlijk is", "enkel wie schade aanricht, krijgt iets"], 0,
       "Gelijken worden gelijk en ongelijken ongelijk behandeld, naar verdienste."),
    keuze("Bij Rawls gaat social justice over de [[*instellingen|privéwoningen|smaak]] van een samenleving, zoals belastingen, onderwijs en gezondheidszorg. Die moeten rechten, kansen en middelen [[*eerlijk|willekeurig|enkel naar geboorte]] verdelen.",
          "Het gaat om de basisstructuur van de samenleving."),
    tabel("Klopt dit over het sociaal contract?", [
        ("Volgens de contracttheorie ontstaat de staat uit een afspraak tussen mensen.", J),
        ("Hobbes, Locke en Rousseau zien de natuurtoestand alle drie precies hetzelfde.", F),
        ("Bij Locke moet de staat de natuurlijke rechten beschermen.", J),
    ], "De drie denkers delen het idee van een contract, maar zien de natuurtoestand anders."),
    koppel("Koppel het begrip aan de denker.", [
        ["sluier van onwetendheid", "Rawls"],
        ["schadebeginsel", "Mill"],
        ["positieve en negatieve vrijheid", "Berlin"],
        ["bevoorrechte onverantwoordelijkheid", "Tronto"],
    ], ["Spinoza"], "Spinoza hoort bij noodzakelijkheid in de zijnsleer."),
    mk("Waarom vinden communitaristen culturele gelijkheid belangrijk?",
       ["cultuur vormt mee wie je bent", "culturen moeten opgaan in één cultuur",
        "enkel de meerderheid telt in de politiek", "cultuur speelt geen rol in de politiek"], 0,
       "Daarom pleiten ze voor erkenning van culturele groepen, zoals Charles Taylor met zijn politiek van erkenning."),
    open_("Leg uit wat het verschil is tussen positieve en negatieve vrijheid, en geef bij elk een mogelijk gevolg.",
          "Negatieve vrijheid is vrij zijn van inmenging: niemand houdt je tegen. Een gevolg kan zijn dat wie geen middelen heeft, op papier vrij is maar er weinig mee kan. Positieve vrijheid is vrij zijn tot iets: je eigen leven sturen, bijvoorbeeld dankzij onderwijs. Berlin waarschuwt dat een staat in naam van je 'ware' vrijheid ook dwang kan goedpraten."),
]

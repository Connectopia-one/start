"""Humane wetenschappen: het recht in de samenleving — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm en een eigen, vereenvoudigde
gerechtelijke piramide. Strikt binnen beyond/bron/sg_hw_recht.py."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

GP = Prent("gerechtelijke-piramide", "De gerechtelijke piramide (vereenvoudigd)",
           "een piramide in vier lagen: onderaan vredegerecht en politierechtbank; daarboven rechtbank van eerste aanleg, arbeidsrechtbank en ondernemingsrechtbank; daarboven hof van beroep, arbeidshof en hof van assisen; bovenaan het Hof van Cassatie")
GP.pad("M 500 70 L 950 610 L 50 610 Z", "#f6f8f2", DONKER, 3)
for y in (190, 330, 470):
    dx = (y - 70) * 450 / 540
    GP.lijn(500 - dx, y, 500 + dx, y, DONKER, 2)
VAKKEN = {}


def vak(sleutel, x, y, b, h, regels, klein=None):
    GP.rect(x, y, b, h, LICHTGROEN, DONKER, 10, 2)
    y0 = y + (h - (16 if klein else 0)) / 2 - (len(regels) - 1) * 11 + 6
    for i, r in enumerate(regels):
        GP.tekst(x + b / 2, y0 + i * 22, r, 18, vet=True)
    if klein:
        GP.tekst(x + b / 2, y + h - 12, klein, 13)
    VAKKEN[sleutel] = (x, y, b, h)


vak("cassatie", 420, 120, 160, 60, ["Hof van", "Cassatie"])
vak("beroep", 280, 220, 140, 90, ["hof van", "beroep"])
vak("arbeidshof", 430, 220, 140, 90, ["arbeidshof"])
vak("assisen", 580, 220, 140, 90, ["hof van", "assisen"])
vak("eerste", 170, 350, 260, 105, ["rechtbank van", "eerste aanleg"], "burgerlijk · correctioneel · familie · jeugd")
vak("arbeid", 440, 350, 160, 105, ["arbeids-", "rechtbank"])
vak("onderneming", 610, 350, 210, 105, ["ondernemings-", "rechtbank"])
vak("vrede", 200, 495, 270, 90, ["vredegerecht"])
vak("politie", 530, 495, 270, 90, ["politierechtbank"])


def hof(sleutel):
    x, y, b, h = VAKKEN[sleutel]
    return [Prent.zone(x, y, b, h)]


VRAGEN = [
    klik("Klik op de rechtbank die een boete voor te snel rijden behandelt.", GP.bestand, hof("politie"),
         "De politierechtbank behandelt verkeersovertredingen en de schade bij verkeersongevallen."),
    klik("Klik op de plek waar een ruzie tussen buren over geluidshinder behandeld wordt.", GP.bestand, hof("vrede"),
         "De vrederechter behandelt kleinere burgerlijke geschillen, burenhinder en huur."),
    klik("Klik op het hof waar een volksjury mee beslist over een moord.", GP.bestand, hof("assisen"),
         "Bij het hof van assisen beslist een jury van burgers mee over de schuld."),
    klik("Een bedrijf kan zijn schulden niet meer betalen. Klik op de bevoegde rechtbank.", GP.bestand, hof("onderneming"),
         "De ondernemingsrechtbank behandelt faillissementen en geschillen tussen ondernemingen."),
    klik("Klik op het hof dat enkel nakijkt of de wet juist werd toegepast, zonder de feiten opnieuw te beoordelen.", GP.bestand, hof("cassatie"),
         "Het Hof van Cassatie is het hoogste hof en beoordeelt de feiten niet opnieuw."),
    klik("Iemand is het niet eens met een vonnis van de correctionele rechtbank. Klik waar hij in beroep gaat.", GP.bestand, hof("beroep"),
         "Tegen een vonnis van de rechtbank van eerste aanleg ga je in beroep bij het hof van beroep."),
    klik("Een werknemer vindt dat hij onterecht ontslagen werd. Klik op de rechtbank waar hij in eerste aanleg naartoe gaat.", GP.bestand, hof("arbeid"),
         "De arbeidsrechtbank behandelt conflicten tussen werknemers en werkgevers."),
    met_prent(GP.bestand, keuze("Een echtscheiding komt voor de [[*familierechtbank|politierechtbank|ondernemingsrechtbank]]. Die is een afdeling van de [[*rechtbank van eerste aanleg|vredegerecht|hof van assisen]].",
              "De familierechtbank behandelt zaken over gezin en familie.")),
    met_prent(GP.bestand, keuze("Welke soort zaak een rechtbank behandelt, is haar [[*materiële|territoriale]] bevoegdheid. Of de rechtbank van Gent of van Hasselt bevoegd is, is de [[*territoriale|materiële]] bevoegdheid.",
              "Materieel gaat over de soort zaak, territoriaal over de plaats.")),
    tabel("Is dit burgerlijk recht of strafrecht?", [
        ("Een eigenaar betaalt de huurwaarborg niet terug.", "burgerlijk recht"),
        ("Iemand breekt in en steelt een laptop.", "strafrecht"),
        ("Twee buren zijn het oneens over een haag op de grens.", "burgerlijk recht"),
        ("Iemand rijdt dronken en wordt vervolgd.", "strafrecht"),
    ], "Burgerlijk recht gaat over conflicten tussen burgers, strafrecht over misdrijven.",
       kolommen=["burgerlijk recht", "strafrecht"]),
    tabel("Welke functie van justitie staat hier voorop?", [
        ("Een rechter beslist wie gelijk heeft in een ruzie over een contract.", "conflictbeslechting"),
        ("Een zware straf moet anderen afschrikken.", "preventie"),
        ("De politie zorgt dat een betoging rustig verloopt.", "ordehandhaving"),
        ("Een gevaarlijke dader wordt opgesloten om anderen te beschermen.", "veiligheid"),
    ], "Conflicten oplossen, voorkomen, de orde bewaren en de samenleving beschermen.",
       kolommen=["conflictbeslechting", "preventie", "ordehandhaving", "veiligheid"]),
    koppel("Koppel het principe van rechtspraak aan wat het betekent.", [
        ["hoor en wederhoor", "elke partij kan haar verhaal doen en reageren"],
        ["vermoeden van onschuld", "je bent onschuldig tot je schuld bewezen is"],
        ["openbaarheid", "zittingen zijn in principe toegankelijk voor iedereen"],
        ["onafhankelijkheid", "de rechter krijgt geen bevelen van de regering"],
    ], ["de rechter maakt zelf de wetten"], "De vier principes van een eerlijke rechtspraak."),
    casus(
        "Sem (17) slaat bij een ruzie een andere jongen, Jens, zwaar in elkaar. Jens moet een week naar het ziekenhuis. "
        "Een krant schrijft al de dag nadien dat Sem 'de dader' is, met zijn foto erbij. Het parket opent een dossier.",
        [
            keuze("Omdat Sem minderjarig is, komt hij in principe voor de [[*jeugdrechtbank|politierechtbank|arbeidsrechtbank]].",
                  "Minderjarigen komen in principe voor de jeugdrechtbank, die vooral kiest voor maatregelen die opvoeden en herstellen."),
            mk("Bij zware feiten kan de jeugdrechter Sem doorsturen naar een gewone rechtbank. Hoe heet dat?",
               ["uithandengeving", "voorwaardelijke invrijheidstelling", "cassatie", "openbaarheid"], 0,
               "Uithandengeving kan vanaf 16 jaar bij zware feiten."),
            keuze("Het krantenartikel zet vooral het [[*vermoeden van onschuld|principe van openbaarheid|recht op een advocaat]] onder druk.",
                  "Dat noem je trial by media: de media stellen iemand al schuldig voor."),
            tabel("Klopt dit over de zaak?", [
                ("Jens kan naast de strafzaak een schadevergoeding vragen.", J),
                ("Het parket beslist zelf over de straf van Sem.", F),
                ("Eén feit kan zowel een strafzaak als een burgerlijke zaak opleveren.", J),
            ], "Het parket vervolgt, maar de rechter beslist. De schadevergoeding is burgerlijk."),
        ],
    ),
    tabel("Klopt dit?", [
        ("Een werkstraf en een enkelband zijn alternatieve straffen.", J),
        ("Na de verjaringstermijn kan een misdrijf niet meer vervolgd worden.", J),
        ("Het vredegerecht behandelt de zwaarste misdaden.", F),
        ("Het openbaar ministerie verdedigt de verdachte.", F),
    ], "Het vredegerecht behandelt kleinere burgerlijke zaken. De advocaat verdedigt, het openbaar ministerie vervolgt."),
    sorteer("Wie doet wat in een strafzaak?", ["Openbaar ministerie", "Advocaat", "Rechter"], [
        ["vervolgt de verdachte in naam van de samenleving", "Openbaar ministerie"],
        ["verdedigt de belangen van de cliënt", "Advocaat"],
        ["spreekt het vonnis uit", "Rechter"],
        ["vraagt een straf", "Openbaar ministerie"],
        ["zoekt argumenten voor vrijspraak", "Advocaat"],
        ["beslist onafhankelijk volgens de wet", "Rechter"],
    ], "Het parket vervolgt, de advocaat verdedigt en de rechter beslist."),
    mk("Een rechter moet oordelen over een zaak van zijn schoonbroer. Wat moet hij doen?",
       ["zich laten vervangen door een andere rechter",
        "de zaak zelf behandelen maar extra streng zijn",
        "de zaak met gesloten deuren behandelen",
        "de minister van Justitie om raad vragen over het vonnis"], 0,
       "Een rechter mag geen persoonlijk belang hebben in een zaak. Daarom laat hij zich vervangen."),
    keuze("Een veroordeelde wil met een enkelband vroeger naar huis. Daarover beslist de [[*strafuitvoeringsrechtbank|vrederechter|ondernemingsrechtbank]].",
          "De strafuitvoeringsrechtbank beslist hoe een langere straf uitgevoerd wordt."),
    volgorde("Zet de stappen van een strafzaak in een logische volgorde.", [
        "de politie stelt een misdrijf vast",
        "het parket onderzoekt het dossier en vervolgt",
        "de rechter hoort beide partijen",
        "de rechter spreekt een vonnis uit",
        "wie het niet eens is, kan in beroep gaan",
    ], "Vaststellen, vervolgen, hoor en wederhoor, vonnis en eventueel beroep."),
    sleep("Een zitting gebeurt soms met [[gesloten]] deuren, bijvoorbeeld om [[minderjarigen]] te beschermen. Normaal geldt het principe van [[openbaarheid]].",
          ["verjaring", "cassatie"], "Openbaarheid zorgt voor controle op de rechters, met uitzonderingen."),
    mk("Waarom is een onafhankelijke rechtspraak belangrijk voor een burger die de overheid aanklaagt?",
       ["de rechter staat los van de regering en oordeelt eerlijk",
        "de rechter moet de regering altijd gelijk geven",
        "de burger mag dan zelf zijn rechter uitkiezen",
        "de zaak gaat dan meteen en zonder beroep naar het Hof van Cassatie"], 0,
       "Omdat rechters los staan van de regering, kan zelfs de overheid voor de rechter verliezen."),
    tabel("Is dit een argument in het debat over de volksjury bij het hof van assisen?", [
        ("Burgers krijgen zo een stem in de rechtspraak.", J),
        ("Leken kunnen sterker beïnvloed worden door emoties of de media.", J),
        ("De volksjury beslist over verkeersboetes.", F),
    ], "Er is een maatschappelijk debat over het afschaffen van de volksjury. Verkeersboetes horen bij de politierechtbank."),
    inv("Hoeveel lagen telt de gerechtelijke piramide op deze prent?", ["4", "vier"],
        "Onderaan vredegerecht en politierechtbank, dan de rechtbanken van eerste aanleg, dan de hoven, en bovenaan het Hof van Cassatie."),
    met_prent(GP.bestand, mk("Een vijftienjarige pleegt een diefstal. In welk vak van de piramide zit de rechtbank die de zaak in principe behandelt?",
              ["rechtbank van eerste aanleg", "politierechtbank", "hof van assisen", "het vredegerecht van de woonplaats"], 0,
              "De jeugdrechtbank is een afdeling van de rechtbank van eerste aanleg.")),
    met_prent(GP.bestand, keuze("Een wanbedrijf zoals diefstal komt voor de [[*correctionele rechtbank|vrederechter|arbeidsrechtbank]]. Wie in beroep gaat tegen een vonnis van de arbeidsrechtbank, gaat naar het [[*arbeidshof|hof van assisen|Hof van Cassatie]].",
              "De correctionele rechtbank is een afdeling van de rechtbank van eerste aanleg. Boven de arbeidsrechtbank staat het arbeidshof.")),
    mk("Een verdachte wordt veroordeeld zonder dat hij of zijn advocaat iets mocht zeggen. Welk principe wordt geschonden?",
       ["hoor en wederhoor", "verjaring", "openbaarheid van de zitting", "preventie"], 0,
       "Elke partij moet de argumenten van de andere kunnen horen en beantwoorden."),
    keuze("Een grotere burgerlijke zaak komt in eerste aanleg voor de [[*burgerlijke rechtbank|politierechtbank|strafuitvoeringsrechtbank]]. Kleinere geschillen gaan naar de [[*vrederechter|correctionele rechtbank|jeugdrechtbank]].",
          "De burgerlijke rechtbank is een afdeling van de rechtbank van eerste aanleg."),
    open_("Leg met een voorbeeld uit waarom één feit zowel een strafzaak als een burgerlijke zaak kan opleveren.",
          "Wie iemand in elkaar slaat, pleegt een misdrijf. Het openbaar ministerie kan de dader vervolgen en de rechter kan een straf opleggen: dat is strafrecht. Het slachtoffer heeft ook schade, zoals ziekenhuiskosten. Daarvoor kan het een schadevergoeding vragen van de dader: dat is burgerlijk recht. Het eerste beschermt de samenleving, het tweede herstelt de schade van het slachtoffer."),
]

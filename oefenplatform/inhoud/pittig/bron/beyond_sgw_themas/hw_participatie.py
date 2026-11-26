"""Humane wetenschappen: participatie, kiesstelsel en kiesrecht — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm, een eigen tijdlijn van het
kiesrecht in België en een eigen vergelijking van twee kiesstelsels met
verzonnen cijfers. Strikt binnen beyond/bron/sg_hw_participatie.py."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, ORANJE, GEEL

# Tijdlijn kiesrecht ----------------------------------------------------------------
TL = Prent("tijdlijn-kiesrecht", "Het kiesrecht in België, stap voor stap",
           "een horizontale tijdlijn met vijf vakken: 1831, 1893, 1919, 1948 en 1981, met de letters A tot E eronder")
TL.pijl(60, 330, 950, 330, DONKER, 4)
JAREN = {"A": (130, "1831"), "B": (310, "1893"), "C": (490, "1919"), "D": (670, "1948"), "E": (850, "1981")}
for k, (x, jaar) in JAREN.items():
    TL.lijn(x, 280, x, 330, DONKER, 2)
    TL.rect(x - 75, 200, 150, 80, LICHTGROEN, DONKER, 14, 2)
    TL.tekst(x, 252, jaar, 30, vet=True)
    TL.cirkel(x, 330, 9, DONKER, DONKER, 1)
    TL.letter(x, 400, k)
TL.tekst(500, 520, "Welke stap hoort bij welk jaar?", 18)


def jaar(k):
    x = JAREN[k][0]
    return [Prent.zone(x - 75, 200, 150, 230)]


# Twee kiesstelsels -----------------------------------------------------------------
KS = Prent("twee-kiesstelsels", "Dezelfde stemmen, twee kiesstelsels (verzonnen land, 100 zetels)",
           "bovenaan de stemmen: partij X 40 procent, Y 35 procent, Z 25 procent; daaronder twee panelen met de zetels: in paneel A krijgen X, Y en Z 40, 35 en 25 zetels, in paneel B krijgen ze 60, 40 en 0 zetels")
KS.tekst(500, 90, "Stemmen:  partij X 40 %   ·   partij Y 35 %   ·   partij Z 25 %", 20, vet=True)
PANELEN = {"A": (60, [40, 35, 25]), "B": (530, [60, 40, 0])}
KLEUR = [LICHTGROEN, "#f1d9b5", GRIJS]
for k, (x0, zetels) in PANELEN.items():
    KS.rect(x0, 130, 410, 470, "#ffffff", DONKER, 16, 2)
    KS.letter(x0 + 40, 170, k)
    KS.tekst(x0 + 230, 178, "zetels", 20, vet=True)
    for i, z in enumerate(zetels):
        bx = x0 + 60 + i * 115
        h = z * 5
        if h:
            KS.rect(bx, 540 - h, 70, h, KLEUR[i], DONKER, 4, 2)
        KS.tekst(bx + 35, 530 - h, str(z), 20, vet=True)
        KS.tekst(bx + 35, 572, "XYZ"[i], 20, vet=True)
    KS.lijn(x0 + 40, 540, x0 + 390, 540, DONKER, 2)


def paneel(k):
    return [Prent.zone(PANELEN[k][0], 130, 410, 470)]


VRAGEN = [
    klik("Klik op het jaar waarin vrouwen voor het eerst mochten stemmen voor het parlement.", TL.bestand, jaar("D"),
         "Vrouwen stemden al vanaf 1921 voor de gemeenteraad, maar pas vanaf 1948 voor het parlement."),
    klik("Klik op het jaar van het cijnskiesrecht.", TL.bestand, jaar("A"),
         "In 1831 mocht enkel wie genoeg belasting betaalde stemmen."),
    klik("Klik op het jaar waarin de stemleeftijd van 21 naar 18 jaar ging.", TL.bestand, jaar("E"),
         "Sinds 1981 mag je stemmen vanaf 18 jaar."),
    met_prent(TL.bestand, keuze("Het algemeen meervoudig stemrecht hoort bij [[*B|C|A]], het algemeen enkelvoudig stemrecht voor mannen bij [[*C|B|D]].",
              "1893 gaf alle mannen een stem, met extra stemmen voor sommigen. In 1919 kreeg elke man één stem.")),
    met_prent(TL.bestand, keuze("De opkomstplicht ontstond tegelijk met stap [[*B|A|E]].",
              "Sinds 1893 moet je naar het stembureau gaan.")),
    klik("Klik op het paneel dat evenredige vertegenwoordiging toont.", KS.bestand, paneel("A"),
         "In paneel A komen de zetels overeen met het deel van de stemmen: 40, 35 en 25."),
    klik("Klik op het paneel waar een partij met een kwart van de stemmen geen enkele zetel krijgt.", KS.bestand, paneel("B"),
         "In paneel B krijgt partij Z 0 zetels, ook al haalde ze 25 procent. Dat kan bij een meerderheidsstelsel."),
    met_prent(KS.bestand, keuze("In paneel B heeft partij [[*X|Y|Z]] alleen een meerderheid. In paneel A is er een [[*coalitie|meerderheidspartij|cijns]] nodig.",
              "60 van de 100 zetels is een meerderheid. In paneel A heeft geen partij er meer dan 50.")),
    met_prent(KS.bestand, mk("Welke uitspraak past bij paneel B?",
              ["grote partijen worden bevoordeeld",
               "elke stem weegt even zwaar door in de zetels",
               "kleine partijen krijgen er extra zetels bij",
               "de zetels volgen precies het deel van de stemmen"], 0,
              "Bij een meerderheidsstelsel gaan de stemmen voor verliezers in een district verloren. Dat helpt grote partijen.")),
    volgorde("Zet de stappen in de evolutie van het kiesrecht in de juiste volgorde.", [
        "enkel wie genoeg belasting betaalt, mag stemmen",
        "alle mannen stemmen, sommigen hebben extra stemmen",
        "elke man heeft één stem",
        "vrouwen stemmen ook voor het parlement",
        "de stemleeftijd zakt naar 18 jaar",
    ], "1831, 1893, 1919, 1948 en 1981."),
    tabel("Klopt dit over het kiesrecht in België?", [
        ("Bij het cijnskiesrecht mocht een klein deel van de mannen stemmen.", J),
        ("Sinds 1919 heeft elke man drie stemmen.", F),
        ("Bij de opkomstplicht mag je blanco stemmen.", J),
        ("Vrouwen stemden al voor 1948 voor het parlement.", F),
    ], "In 1919 kreeg elke man één stem. Vrouwen stemden voor het parlement pas vanaf 1948."),
    inv("In een land met evenredige vertegenwoordiging en 150 zetels haalt een partij 20 procent van de stemmen. Hoeveel zetels krijgt ze ongeveer?", ["30"],
        "20 procent van 150 is 30."),
    sorteer("Is dit conventionele of niet-conventionele participatie?", ["Conventioneel", "Niet-conventioneel"], [
        ["stemmen bij de verkiezingen", "Conventioneel"],
        ["een boycot van een merk", "Niet-conventioneel"],
        ["lid worden van een partij", "Conventioneel"],
        ["een petitie tekenen", "Niet-conventioneel"],
        ["een betoging", "Niet-conventioneel"],
        ["kandidaat zijn op een lijst", "Conventioneel"],
    ], "Conventioneel gaat via de gewone politieke kanalen, niet-conventioneel erbuiten."),
    koppel("Koppel het voorbeeld aan de vorm van participatie.", [
        ["Een vakbond overlegt met de minister over de pensioenen.", "belangengroep"],
        ["Duizenden jongeren betogen voor het klimaat.", "sociale beweging"],
        ["Buurtbewoners brengen zelf een plan voor een speelplein op de gemeenteraad.", "burgerinitiatief"],
        ["De gemeente laat de inwoners stemmen over één vraag.", "volksraadpleging"],
    ], ["cijnskiesrecht"], "Elke vorm met een typisch voorbeeld."),
    tabel("Welke factor van participatie speelt hier vooral?", [
        ("Een hoogopgeleide vrouw stapt sneller naar een politicus met een voorstel.", "scholingsgraad"),
        ("Een jongere deelt een politiek filmpje op sociale media in plaats van lid te worden van een partij.", "leeftijd"),
        ("Een vader met drie jonge kinderen heeft geen tijd voor politieke vergaderingen.", "gezinssituatie"),
    ], "Opleiding, leeftijd en gezinssituatie beïnvloeden hoe mensen participeren.",
       kolommen=["scholingsgraad", "leeftijd", "gezinssituatie"]),
    casus(
        "In de gemeente Ravel wil het bestuur een parking aanleggen op een grasveld. Een groep bewoners verzamelt 800 handtekeningen. "
        "Een milieuorganisatie organiseert een betoging. Het bestuur besluit de inwoners via een volksraadpleging naar hun mening te vragen.",
        [
            mk("Wat doen de bewoners met de handtekeningen?",
               ["ze nemen een burgerinitiatief", "ze voeren een verkiezing uit", "ze vormen een partij", "ze stemmen een wet"], 0,
               "Burgers nemen zelf het initiatief en brengen het bij de politiek."),
            keuze("De betoging is een vorm van [[*niet-conventionele|conventionele]] participatie.",
                  "Een betoging gaat buiten de gewone kanalen om, ook al is ze toegelaten."),
            tabel("Klopt dit over de volksraadpleging?", [
                ("De inwoners stemmen over één vraag.", J),
                ("Het resultaat verplicht het gemeentebestuur altijd.", F),
                ("Het is een vorm van rechtstreekse inspraak van burgers.", J),
            ], "In België is een volksraadpleging niet bindend."),
            keuze("De milieuorganisatie is geen partij, maar een [[*belangengroep|kieskring|regering]] die druk uitoefent.",
                  "Ze komt niet op bij verkiezingen, maar probeert beslissingen te beïnvloeden."),
        ],
    ),
    mk("Waarom spreek je in België beter van opkomstplicht dan van stemplicht?",
       ["je moet enkel naar het stembureau gaan, wat je daar stemt is vrij",
        "je moet verplicht op de grootste partij of haar lijsttrekker stemmen",
        "je moet een ingevuld formulier van je gemeente kunnen voorleggen",
        "je moet een cijns betalen voor je in het stembureau binnen mag"], 0,
       "Blanco of ongeldig stemmen mag. Enkel aanwezig zijn is verplicht."),
    tabel("Is dit een argument vóór of tegen het afschaffen van de opkomstplicht?", [
        ("Stemmen is een recht, geen plicht.", "vóór afschaffen"),
        ("Zonder plicht gaan vooral bepaalde groepen stemmen en worden zwakkere groepen minder gehoord.", "tegen afschaffen"),
        ("Een stem uit vrije wil is meer waard.", "vóór afschaffen"),
    ], "Voorstanders benadrukken vrijheid, tegenstanders de gelijke vertegenwoordiging.",
       kolommen=["vóór afschaffen", "tegen afschaffen"]),
    keuze("Een kiesstelsel met evenredige vertegenwoordiging geeft gewoonlijk [[*meer|minder]] partijen in het parlement en [[*vaker|zelden]] een coalitie.",
          "Ook kleinere partijen krijgen zetels. Daardoor heeft zelden één partij alleen een meerderheid."),
    sleep("In 1831 gold het [[cijnskiesrecht]]. Arbeiders betaalden te weinig [[belasting]] om te mogen stemmen. Na stakingen kwam in 1893 het algemeen [[meervoudig]] stemrecht.",
          ["enkelvoudig", "vrouwen"], "Cijns betekent belasting. Daarom eisten arbeiders algemeen stemrecht."),
    mk("Waarom is de mate van politieke participatie in een dictatuur meestal kleiner dan in een democratie?",
       ["vrije verkiezingen en acties zijn er vaak verboden",
        "mensen in een dictatuur hebben minder interesse in politiek",
        "in een dictatuur bestaat er geen enkele vorm van belasting",
        "de dictatuur heeft altijd een strenge opkomstplicht"], 0,
       "De staatsvorm bepaalt mee hoeveel burgers kunnen participeren."),
    inv("Een partij haalt in een meerderheidsstelsel in 3 van de 10 districten de meeste stemmen. Hoeveel zetels krijgt ze, als elk district één zetel heeft?", ["3"],
        "Per district krijgt enkel de winnaar een zetel. Drie gewonnen districten zijn drie zetels."),
    keuze("Wie in een representatieve democratie stemt, geeft een [[*mandaat|cijns|referendum]] aan een vertegenwoordiger.",
          "De vertegenwoordiger beslist dan in naam van de kiezers."),
    tabel("Klopt dit over belangengroepen en sociale bewegingen?", [
        ("Een werkgeversorganisatie is een belangengroep.", J),
        ("Een sociale beweging is strakker georganiseerd dan een belangengroep.", F),
        ("Een belangengroep komt op met eigen kandidatenlijsten bij de verkiezingen.", F),
        ("De vrouwenbeweging is een voorbeeld van een sociale beweging.", J),
    ], "Een sociale beweging is losser georganiseerd. Kandidatenlijsten zijn iets van partijen."),
    keuze("Dat iemand in de stad meer acties en verenigingen vindt dan op het platteland, heeft te maken met de factor [[*urbanisatie|scholingsgraad|leeftijd]].",
          "Waar je woont, in een stad of op het platteland, beïnvloedt hoe je participeert."),
    mk("Waarom woog de stem van veel arbeiders na 1893 nog steeds minder door?",
       ["rijkere en hoger opgeleide mannen kregen extra stemmen",
        "arbeiders mochten pas vanaf 30 jaar naar het stembureau",
        "arbeiders moesten van de wet blanco stemmen in elk stembureau",
        "enkel arbeiders kregen een opkomstplicht en de rest niet"], 0,
       "Het meervoudig stemrecht gaf extra stemmen voor eigendom, een diploma of een gezin. Pas in 1919 had elke man één stem."),
    open_("Vergelijk evenredige vertegenwoordiging met een meerderheidsstelsel. Geef bij elk een voordeel en een nadeel.",
          "Bij evenredige vertegenwoordiging krijgt een partij ongeveer evenveel procent zetels als procent stemmen. Voordeel: meer stromingen krijgen een stem in het parlement. Nadeel: er zijn bijna altijd coalities nodig, waardoor regeringsvorming moeilijker is. Bij een meerderheidsstelsel krijgt per district enkel de winnaar een zetel. Voordeel: vaker een regering van één partij, dus duidelijke verantwoordelijkheid. Nadeel: stemmen voor verliezers gaan verloren en kleine partijen worden benadeeld."),
]

"""Mediatisering en de functies van de massamedia — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
krantenpagina, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een verzonnen krantenpagina ------------------------------------------------------------
KR = Prent("krantenpagina", "Een pagina uit een verzonnen regionale krant", "een krantenpagina met vier blokken: linksboven een groot artikel 'Schepen gebruikte gemeentegeld voor eigen verbouwing' (A), rechtsboven een kader 'Onze mening: het is tijd voor openheid' (B), linksonder 'Bewoners van de Lindewijk: wij worden niet gehoord' met citaten van bewoners (C), rechtsonder een advertentie 'Nieuwe fiets? Nu 20 % korting bij Fietsen Peeters' (D)")
KR.rect(70, 50, 860, 560, "#ffffff", GRIJS, 4, 2)
KR.tekst(500, 95, "De Kempische Bode", 30, "middle", DONKER, True)
KR.lijn(90, 112, 910, 112, DONKER, 2)
KR.rect(90, 130, 480, 230, "#ffffff", GRIJS, 0, 1)
KR.tekst(105, 165, "Schepen gebruikte gemeentegeld", 22, "start", DONKER, True)
KR.tekst(105, 192, "voor eigen verbouwing", 22, "start", DONKER, True)
KR.tekst(105, 225, "Onze redactie vond facturen die tonen dat ...", 16, "start", "#5c6356")
for i in range(4):
    KR.lijn(105, 255 + i * 25, 550, 255 + i * 25, "#d8d6cc", 6)
KR.letter(540, 165, "A")
KR.rect(590, 130, 320, 230, "#f4f4f2", GRIJS, 0, 1)
KR.tekst(605, 165, "Onze mening", 20, "start", DONKER, True)
KR.tekst(605, 192, "Het is tijd voor openheid", 18, "start")
for i in range(5):
    KR.lijn(605, 225 + i * 25, 890, 225 + i * 25, "#d8d6cc", 6)
KR.letter(880, 165, "B")
KR.rect(90, 380, 480, 210, "#ffffff", GRIJS, 0, 1)
KR.tekst(105, 415, "Bewoners van de Lindewijk:", 20, "start", DONKER, True)
KR.tekst(105, 442, "“Wij worden niet gehoord”", 20, "start", DONKER, True)
KR.tekst(105, 475, "“Al twee jaar geen speelplein,” zegt een moeder.", 16, "start", "#5c6356")
for i in range(3):
    KR.lijn(105, 505 + i * 25, 550, 505 + i * 25, "#d8d6cc", 6)
KR.letter(540, 415, "C")
KR.rect(590, 380, 320, 210, "#e8efe1", DONKER, 8, 2)
KR.tekst(750, 430, "Nieuwe fiets?", 26, "middle", DONKER, True)
KR.tekst(750, 475, "Nu 20 % korting", 22, "middle")
KR.tekst(750, 510, "bij Fietsen Peeters", 18, "middle", "#5c6356")
KR.letter(880, 560, "D")
BLOK = {"A": [Prent.zone(90, 130, 480, 230)], "B": [Prent.zone(590, 130, 320, 230)],
        "C": [Prent.zone(90, 380, 480, 210)], "D": [Prent.zone(590, 380, 320, 210)]}

VRAGEN = [
    klik("Klik op het blok waar de krant de macht controleert.", KR.bestand, BLOK["A"],
         "De onthulling over de schepen is de waakhondfunctie, samen met de onderzoeksfunctie."),
    klik("Klik op het blok met de commentaarfunctie.", KR.bestand, BLOK["B"],
         "'Onze mening' geeft een eigen beoordeling bij het nieuws."),
    klik("Klik op het blok met de spreekbuisfunctie.", KR.bestand, BLOK["C"],
         "De bewoners komen zelf aan het woord."),
    klik("Klik op het blok dat vooral de commerciële functie vervult.", KR.bestand, BLOK["D"],
         "Reclame wil je aanzetten tot kopen."),
    met_prent(KR.bestand, tabel("Kijk naar de krantenpagina. Klopt dit?", [
        ("In blok A zie je de onderzoeksfunctie.", J),
        ("Blok B brengt vooral nieuwe feiten boven.", F),
        ("Blok D wil je mening over een politieke partij veranderen.", F),
        ("Blok C geeft een stem aan wie anders niet gehoord wordt.", J),
    ], "B geeft commentaar, D wil verkopen.")),
    met_prent(KR.bestand, inv("Welke bijnaam krijgen de media omdat ze doen wat in blok A gebeurt? Vul aan: de ... macht.", ["vierde"],
              "Naast de wetgevende, uitvoerende en rechterlijke macht.")),
    tabel("Welke functie voor het individu staat voorop?", [
        ("Een nieuwsuitzending over het weer en het verkeer.", "informatief"),
        ("Een online cursus gitaar spelen.", "educatief"),
        ("Een spelprogramma op zaterdagavond.", "ontspannend"),
        ("Een filmpje dat je wil doen stemmen voor een partij.", "persuasief"),
    ], "Op de hoogte brengen, iets bijleren, ontspannen, of overtuigen.",
       kolommen=["informatief", "educatief", "ontspannend", "persuasief"]),
    tabel("Infotainment of edutainment?", [
        ("een praatprogramma met nieuws en grappen", "infotainment"),
        ("een leerzame quiz voor kinderen over dieren", "edutainment"),
        ("een documentaire met humor over het menselijk lichaam", "edutainment"),
    ], "Informatie of onderwijs, telkens gemengd met ontspanning.", kolommen=["infotainment", "edutainment"]),
    keuze("Een risico van infotainment is dat de informatie [[*ondergeschikt wordt aan het vermaak|altijd te moeilijk is|helemaal verdwijnt]].",
          "Wat goed bekeken wordt, krijgt meer tijd dan wat belangrijk is."),
    sorteer("Functie voor het individu of voor de samenleving?", ["Individu", "Samenleving"], [
        ["de ontspannende functie", "Individu"],
        ["de politieke functie", "Samenleving"],
        ["de cultuuroverdrachtfunctie", "Samenleving"],
        ["de commerciële functie", "Individu"],
        ["de vrijetijdsfunctie", "Samenleving"],
    ], "Twee lijsten, elk vanuit een andere kant."),
    koppel("Koppel elk onderdeel van de politieke functie aan zijn uitleg.", [
        ["waakhondfunctie", "de macht in het oog houden"],
        ["spreekbuisfunctie", "groepen aan het woord laten"],
        ["onderzoeksfunctie", "zelf nieuwe feiten opzoeken"],
        ["commentaarfunctie", "het nieuws van een standpunt voorzien"],
    ], ["mensen leren een gitaar stemmen"], "Vier van de vijf onderdelen."),
    inv("Hoeveel onderdelen heeft de politieke functie? Schrijf het getal.", ["5", "vijf"],
        "Informerend, spreekbuis, onderzoek, commentaar en waakhond."),
    casus(
        "Een burgemeester zet elke dag korte video's op haar eigen sociale media. Ze geeft geen interviews meer aan kranten. "
        "Veel jongeren volgen haar en praten op school over haar filmpjes.",
        [
            keuze("Dit is een voorbeeld van [[*mediatisering|cultuuroverdracht|edutainment]] van de politiek.",
                  "Steeds meer van het politieke leven loopt langs de media."),
            mk("Wat is het risico als zij journalisten omzeilt?",
               ["de waakhondfunctie valt weg",
                "de video's worden minder bekeken door jongeren",
                "de burgemeester verliest haar wettelijke macht",
                "de krant krijgt meer commerciële reclame"], 0,
               "Zonder journalist tussen zender en burger is er minder controle."),
            keuze("Dat jongeren erover praten, toont de [[*sociale|commerciële|educatieve]] functie.",
                  "Media verbinden mensen en geven gespreksstof."),
        ],
    ),
    keuze("Dezelfde uitzending kan voor het individu ontspanning zijn en voor de samenleving [[*cultuuroverdracht|een waakhond|persuasie]].",
          "De twee lijsten kijken van een andere kant."),
    tabel("Klopt dit over de functies van media?", [
        ("De persuasieve en de commerciële functie zijn hetzelfde.", F),
        ("Mediatisering speelt in verschillende velden, niet alleen in de politiek.", J),
        ("De media hebben als vierde macht een wettelijke bevoegdheid.", F),
        ("Eén programma kan meerdere functies tegelijk vervullen.", J),
    ], "Persuasief wil je mening veranderen, commercieel wil je iets verkopen."),
    sleep("Infotainment mengt informatie en [[ontspanning]]. Edutainment mengt [[onderwijs]] en ontspanning.",
          ["reclame", "politiek"], "Twee mengvormen voor het individu."),
    mk("Waarom heten de media de vierde macht?",
       ["ze houden de andere drie in het oog",
        "ze maken samen met het parlement de wetten",
        "ze spreken recht bij ruzies tussen burgers",
        "ze voeren de beslissingen van de regering uit"], 0,
       "Ze controleren de wetgevende, uitvoerende en rechterlijke macht."),
    keuze("Een documentaire over de Eerste Wereldoorlog vervult vooral de [[*educatieve|commerciële|persuasieve]] functie.",
          "Er wordt kennis aangereikt."),
    inv("Hoe heet het dat steeds meer van het leven langs de media loopt?", ["mediatisering"],
        "Media brengen niet alleen verslag uit, ze bepalen mee."),
    keuze("De vrijetijdsfunctie staat bij de functies voor [[*de samenleving|het individu]].",
          "Bij het individu heet de verwante functie de ontspannende functie."),
    tabel("Welke functie voor de samenleving?", [
        ("Een kinderprogramma leert kinderen de liedjes en feesten van hun land.", "cultuuroverdracht"),
        ("Een uitzending over de verkiezingen legt de standpunten van de partijen uit.", "politiek"),
        ("Iedereen praat op het werk over de finale van gisteren.", "sociaal"),
    ], "Gewoonten doorgeven, politiek, of mensen verbinden.",
       kolommen=["politiek", "cultuuroverdracht", "sociaal"]),
    keuze("Persuasief komt van het Latijnse woord voor [[*overtuigen|verkopen|ontspannen]].",
          "De persuasieve functie wil je van een standpunt overtuigen."),
    mk("Een schoolreportage over een nieuwe gsm staat vol merknamen en links naar winkels. Wat is het probleem?",
       ["info en reclame mengen zich",
        "het is enkel educatief en dus saai",
        "er is geen enkele functie te vinden",
        "het hoort bij de waakhondfunctie"], 0,
       "De informatieve en de commerciële functie mengen zich."),
    keuze("De onderzoeksfunctie brengt [[*nieuwe feiten|een mening|reclame]] boven.",
          "De commentaarfunctie geeft een mening."),
    inv("Hoe heet de mengvorm van onderwijs en ontspanning?", ["edutainment"],
        "Education en entertainment."),
    keuze("Politici gebruiken sociale media om [[*kiezers rechtstreeks te bereiken|wetten goed te keuren|rechtszaken te beslissen]].",
          "Media werken in beide richtingen: burgers informeren zich, politici bereiken kiezers."),
    tabel("Welk onderdeel van de politieke functie?", [
        ("Een journalist zoekt maandenlang naar verborgen documenten.", "onderzoek"),
        ("Een editoriaal zegt dat de regering moet aftreden.", "commentaar"),
        ("Een nieuwsbericht meldt welke wet gisteren gestemd werd.", "informerend"),
    ], "Onderzoek, mening, of gewoon informeren.", kolommen=["informerend", "onderzoek", "commentaar"]),
    open_("Leg uit waarom de waakhondfunctie belangrijk is in een democratie, met een eigen voorbeeld.",
          "De media houden de macht in het oog en brengen misbruik aan het licht, zodat burgers weten wat er gebeurt en politici verantwoording moeten afleggen. Bijvoorbeeld: een krant onthult dat een minister een opdracht gaf aan het bedrijf van een vriend, en daarna volgt een onderzoek."),
]

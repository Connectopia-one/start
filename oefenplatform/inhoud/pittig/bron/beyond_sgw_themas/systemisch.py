"""Ontwikkeling: de humanistische en de systemische benadering — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en eigen schema's
(de piramide van Maslow, de systemen van Bronfenbrenner), zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Piramide van Maslow, zonder namen ------------------------------------------------------
MP = Prent("maslow-piramide", "De behoeften volgens Maslow", "een piramide met vijf lagen zonder namen, van onder naar boven A, B, C, D en E")
LAGEN = "ABCDE"
TOP, VOET, HL = 70, 570, 100
for i, k in enumerate(LAGEN):
    yb = VOET - i * HL
    yt = yb - HL
    def xh(y):
        return 400 * (y - TOP) / (VOET - TOP)
    MP.pad(f"M{500 - xh(yb)} {yb} L{500 + xh(yb)} {yb} L{500 + xh(yt)} {yt} L{500 - xh(yt)} {yt} Z",
           ["#e8efe1", "#dfe9d6", "#d6e2cb", "#cddcc0", "#c4d5b5"][i], DONKER, 2)
    MP.letter(500, yb - HL / 2 + 8, k)


def laag(k):
    i = LAGEN.index(k)
    yb = VOET - i * HL
    return [Prent.zone(500 - 60 - (4 - i) * 50, yb - HL + 10, 120 + (4 - i) * 100, HL - 20)]


# Systemen van Bronfenbrenner ------------------------------------------------------------
BR = Prent("bronfenbrenner-systemen", "De systemen rond een kind volgens Bronfenbrenner", "vier ringen rond een kind in het midden: de binnenste ring A, de tweede ring B als de verbindingen tussen delen van A, de derde ring C, de buitenste ring D; onderaan een pijl van links naar rechts E")
BR.ellips(470, 300, 420, 250, "#eef2e9", DONKER, 2)
BR.ellips(470, 300, 320, 190, "#e2eadb", DONKER, 2)
BR.ellips(470, 300, 220, 130, "#d6e2cb", DONKER, 2)
BR.ellips(470, 300, 120, 70, "#c4d5b5", DONKER, 2)
BR.cirkel(470, 300, 22, "#ffffff", DONKER, 2)
BR.tekst(470, 307, "kind", 16)
BR.letter(470, 252, "A")
BR.letter(470, 196, "B")
BR.letter(470, 136, "C")
BR.letter(470, 78, "D")
BR.pijl(120, 600, 860, 600, DONKER, 4)
BR.letter(900, 600, "E")
PLEK = {"A": (470, 252), "B": (470, 196), "C": (470, 136), "D": (470, 78), "E": (900, 600)}


RX = {"A": (120, 22), "B": (220, 120), "C": (320, 220), "D": (420, 320)}


def ring(k):
    x, y = PLEK[k]
    zones = [Prent.rond(x, y, 34)]
    if k in RX:
        buiten, binnen = RX[k]
        b = buiten - binnen - 10
        zones += [Prent.zone(470 - buiten + 5, 260, b, 80), Prent.zone(470 + binnen + 5, 260, b, 80)]
    return zones


VRAGEN = [
    klik("Klik op de laag die eerst vervuld moet zijn.", MP.bestand, laag("A"),
         "Onderaan staan de lichamelijke behoeften, zoals eten en slapen."),
    klik("Klik op de laag die gaat over worden wie je kan worden.", MP.bestand, laag("E"),
         "Bovenaan staat de zelfontplooiing."),
    klik("Klik op de laag van de behoefte aan veiligheid en zekerheid.", MP.bestand, laag("B"),
         "Veiligheid komt meteen na de lichamelijke behoeften."),
    met_prent(MP.bestand, tabel("Welke laag is het?", [
        ("behoefte aan contact met vrienden", "C"),
        ("behoefte aan waardering en erkenning", "D"),
        ("behoefte aan eten en slapen", "A"),
    ], "Van onder naar boven: lichamelijk, veiligheid, contact, waardering, zelfontplooiing.",
       kolommen=["A", "C", "D"])),
    klik("Klik op het systeem met de wetten en de waarden van een land.", BR.bestand, ring("D"),
         "Het macrosysteem is de grote laag errond."),
    klik("Klik op het systeem met de verbindingen tussen gezin en school.", BR.bestand, ring("B"),
         "Het mesosysteem verbindt twee microsystemen."),
    klik("Klik op het systeem dat over de tijd en veranderingen gaat.", BR.bestand, ring("E"),
         "Het chronosysteem: chronos is tijd."),
    met_prent(BR.bestand, tabel("Welk systeem is het?", [
        ("de klas van het kind", "A"),
        ("de werkplek van mama", "C"),
        ("een nieuwe wet op kinderbijslag", "D"),
    ], "Micro (A), meso (B), exo (C), macro (D), chrono (E).", kolommen=["A", "C", "D"])),
    casus(
        "Amina zit in het derde leerjaar. Haar mama verloor haar werk, waardoor het gezin moest verhuizen naar "
        "een kleiner appartement. Amina komt nu vaak moe en zonder ontbijt naar school. De juf belt met mama en "
        "regelt een schoolontbijt. Daarna geeft ze Amina bij rekenen eerst een uitgewerkt voorbeeld, dan een half "
        "voorbeeld en dan niets meer.",
        [
            keuze("Het telefoontje tussen de juf en mama hoort bij het [[*mesosysteem|microsysteem|exosysteem]].",
                  "Een verbinding tussen twee microsystemen."),
            mk("Waarom regelt de juf eerst het ontbijt?",
               ["volgens Maslow komt eten eerst",
                "volgens Vygotsky leert een kind beter na het eten",
                "volgens Rogers bepaalt de juf wat het kind eet",
                "volgens Bronfenbrenner is eten het chronosysteem"], 0,
               "Pas als de lagere behoeften vervuld zijn, komt een kind aan leren toe."),
            inv("Hoe heet de hulp bij rekenen die stap voor stap afgebouwd wordt?", ["scaffolding"],
                "Zoals een steiger die weggaat als het gebouw staat."),
            keuze("Dat mama haar werk verloor en dat Amina daardoor anders leeft, werkt via het [[*exosysteem|macrosysteem|chronosysteem]].",
                  "Het werk van mama werkt indirect in op Amina."),
        ],
    ),
    koppel("Koppel elke humanistische of systemische theorie aan haar naam.", [
        ["motivatietheorie", "Abraham Maslow"],
        ["client centered therapy", "Carl Rogers"],
        ["bio-ecologisch model", "Urie Bronfenbrenner"],
        ["sociaal-culturele theorie", "Lev Vygotsky"],
    ], ["Ivan Pavlov"], "Twee humanistische en twee systemische theorieën."),
    tabel("In welke zone van Vygotsky valt deze opdracht voor een kind dat vlot tot twintig telt?", [
        ("tot tien tellen", "comfortzone"),
        ("tot dertig tellen met een getallenlijn erbij", "zone van de naaste ontwikkeling"),
        ("vergelijkingen met twee onbekenden oplossen", "angstzone"),
    ], "Wat al lukt, wat met hulp lukt, of wat veel te moeilijk is.",
       kolommen=["comfortzone", "zone van de naaste ontwikkeling", "angstzone"]),
    keuze("Een kind telt eerst hardop met de juf en later stil in zijn hoofd. Vygotsky noemt dat het [[*interiorisatieproces|scaffolding|mesosysteem]].",
          "Wat samen gebeurt, wordt eigen denken."),
    tabel("Klopt dit over Maslow, Bronfenbrenner en Vygotsky?", [
        ("Zelfontplooiing betekent beter willen zijn dan de anderen.", F),
        ("De systemen van Bronfenbrenner werken door elkaar.", J),
        ("Vygotsky ziet ontwikkeling eerder als cultureel bepaald.", J),
        ("Scaffolding betekent dat de hulp altijd blijft.", F),
    ], "Zelfontplooiing is worden wie je zelf kan worden; scaffolding wordt afgebouwd."),
    sorteer("Humanistisch of systemisch?", ["Humanistisch", "Systemisch"], [
        ["piramide van behoeften", "Humanistisch"],
        ["zone van de naaste ontwikkeling", "Systemisch"],
        ["de persoon zelf in het midden van de begeleiding", "Humanistisch"],
        ["microsysteem en macrosysteem", "Systemisch"],
    ], "Humanistisch vertrekt bij wat de mens zelf wil, systemisch bij wat rond hem staat."),
    mk("Een begeleider zegt: 'Ik ga niet zeggen wat je moet doen, ik volg jou.' Welke houding past daar NIET bij?",
       ["de oplossing zelf opleggen",
        "de ander aanvaarden zoals hij is",
        "echt en open zijn over jezelf",
        "je inleven in de ander"], 0,
       "Bij Rogers staat de persoon zelf in het midden, niet de methode van de begeleider."),
    keuze("De humanistische benadering geeft op de tweede basisvraag veel plaats aan [[*zelfbepaling|nature|toeval]].",
          "Een mens kiest zelf richting."),
    keuze("Op de eerste basisvraag antwoordt de humanistische benadering eerder [[*continu|discontinu]].",
          "Maslow en Rogers werken niet met vaste fasen."),
    volgorde("Zet de behoeften van Maslow in de juiste volgorde, van onder naar boven.", [
        "eten en slapen",
        "veiligheid en zekerheid",
        "contact met anderen",
        "waardering en erkenning",
        "zelfontplooiing",
    ], "Lagere behoeften moeten eerst genoeg vervuld zijn."),
    inv("Hoeveel systemen onderscheidt Bronfenbrenner? Schrijf het getal.", ["5", "vijf"],
        "Micro, meso, exo, macro en chrono."),
    mk("Wat is een bezwaar tegen de theorie van Maslow?",
       ["de volgorde klopt niet voor iedereen",
        "ze geeft geen plaats aan behoeften",
        "ze werkt alleen voor dieren in een kooi",
        "ze gaat enkel over de cultuur van een land"], 0,
       "Mensen zetten soms een hogere behoefte voor een lagere."),
    sleep("Bij Bronfenbrenner zit het kind zelf in het [[microsysteem]], maar niet in het [[exosysteem]], dat enkel onrechtstreeks op hem inwerkt.",
          ["chronosysteem", "comfortzone"], "Het kind zit zelf in het microsysteem, niet in het exosysteem."),
    mk("Waarin verschillen Maslow en Rogers het sterkst van Skinner?",
       ["wie kiest: de mens of de omgeving",
        "het aantal fasen in de ontwikkeling",
        "de rol van het geheugen bij leren",
        "de leeftijd waarop ontwikkeling stopt"], 0,
       "Het behaviorisme legt de nadruk op de omgeving, de humanistische benadering op zelfbepaling."),
    inv("Hoe heet bij Vygotsky de zone waarin een opdracht al zelfstandig lukt?", ["comfortzone", "de comfortzone"],
        "Daar valt niets meer bij te leren."),
    keuze("Een kind dat opgroeit met smartphones terwijl zijn ouders dat niet deden, ervaart de invloed van het [[*chronosysteem|macrosysteem|mesosysteem]].",
          "Het chronosysteem gaat over veranderingen in de tijd."),
    mk("Welke theorie zit achter een school die eerst zorgt voor een vast ritme en een veilige klas, en pas daarna voor extra uitdaging?",
       ["de motivatietheorie", "de client centered therapy", "het bio-ecologisch model", "de sociaal-culturele theorie"], 0,
       "Eerst de lagere behoeften, dan de hogere: Maslow."),
    keuze("In de angstzone van Vygotsky [[*valt het leren stil|gaat het leren het snelst|lukt alles al alleen]].",
          "De afstand is te groot: het is te moeilijk."),
    open_("Een leerkracht wil een leerling helpen die een nieuwe opdracht niet alleen kan. Leg met de begrippen van Vygotsky uit hoe ze dat best aanpakt.",
          "De opdracht moet in de zone van de naaste ontwikkeling liggen: niet in de comfortzone, waar niets te leren valt, en niet in de angstzone, waar het te moeilijk is. Ze geeft eerst veel hulp en bouwt die stap voor stap af (scaffolding), tot de leerling het zelfstandig kan."),
]

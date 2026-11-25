"""Spelvormen en speelgoed — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_spel: de zes spelvormen, speelgoed kiezen per leeftijd en
per ontwikkelingsgebied, veiligheid, en een activiteit voorbereiden,
begeleiden en afronden. Met een zelfgetekende speelgoedplank."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, ROOD, GEEL, LICHTGROEN, PAARS

SG = Prent("speelgoedplank", "Zes stukken speelgoed", "zes stukken speelgoed in vakjes met hun naam, letters A tot F")
VAK = [("A", "rammelaar"), ("B", "verkleedkoffer"), ("C", "kralen om te rijgen"), ("D", "bal"), ("E", "prentenboek"), ("F", "zakje knikkers")]
Z = {}
for i, (t, naam) in enumerate(VAK):
    x, y = 60 + (i % 3) * 300, 70 + (i // 3) * 280
    SG.rect(x, y, 280, 260, "#ffffff", GRIJS, 16, 2)
    SG.letter(x + 30, y + 30, t)
    SG.tekst(x + 140, y + 240, naam, 20)
    cx, cy = x + 140, y + 120
    if t == "A":
        SG.lijn(cx, cy + 20, cx, cy + 90, DONKER, 10); SG.cirkel(cx, cy - 10, 45, GEEL, DONKER, 3)
        for dx, dy in ((-15, -20), (15, -5), (-5, 10)):
            SG.cirkel(cx + dx, cy - 10 + dy, 7, ROOD, DONKER, 1)
    elif t == "B":
        SG.rect(cx - 90, cy - 40, 180, 110, ORANJE, DONKER, 10, 3); SG.rect(cx - 30, cy - 65, 60, 25, "none", DONKER, 8, 4)
        SG.pad(f"M {cx-60} {cy-40} L {cx-80} {cy-90} L {cx-40} {cy-80}", PAARS, DONKER, 2)
    elif t == "C":
        SG.pad(f"M {cx-100} {cy+40} Q {cx} {cy-80} {cx+100} {cy+40}", "none", DONKER, 2)
        for k in range(7):
            SG.cirkel(cx - 90 + k * 30, cy + 30 - (60 - abs(k - 3) * 20), 12, [ROOD, BLAUW, GEEL, LICHTGROEN][k % 4], DONKER, 2)
    elif t == "D":
        SG.cirkel(cx, cy, 70, ROOD, DONKER, 3); SG.pad(f"M {cx-70} {cy} Q {cx} {cy-40} {cx+70} {cy}", "none", "#ffffff", 4)
    elif t == "E":
        SG.rect(cx - 90, cy - 70, 90, 130, BLAUW, DONKER, 4, 3); SG.rect(cx, cy - 70, 90, 130, LICHTGROEN, DONKER, 4, 3)
        SG.cirkel(cx + 45, cy - 20, 20, GEEL, DONKER, 2)
    else:
        SG.pad(f"M {cx-50} {cy-60} L {cx+50} {cy-60} L {cx+65} {cy+50} L {cx-65} {cy+50} Z", GRIJS, DONKER, 2)
        for dx, dy in ((-30, 75), (0, 82), (30, 72), (55, 85)):
            SG.cirkel(cx + dx, cy + dy, 9, [BLAUW, ROOD, GEEL, LICHTGROEN][(dx // 30) % 4], DONKER, 2)
    Z[t] = [Prent.zone(x, y, 280, 260)]
U = "speelgoedplank.svg"

KRALEN = ("Lees de situatie.\n\n"
          "Je maakt een activiteit voor zes kleuters: ze rijgen kralen aan een draad. Er liggen ook heel kleine kraaltjes, en het broertje van één jaar van een kleuter is mee. "
          "Halverwege raakt Ella (4) gefrustreerd: de gaatjes van de kralen zijn te klein voor haar.")

VRAGEN = [
    klik("Bekijk de speelgoedplank. Klik op het speelgoed dat vooral de fijne motoriek oefent.", U, Z["C"], "Kleine, precieze bewegingen van vingers en handen."),
    klik("Klik op het speelgoed dat vooral de taalontwikkeling helpt.", U, Z["E"], "Samen kijken en benoemen levert woorden en zinnen op."),
    klik("Klik op het speelgoed dat het best past bij een baby van vier maanden.", U, Z["A"], "Een baby ontdekt met ogen, oren, mond en handen."),
    klik("Klik op het speelgoed dat gevaarlijk is voor een baby.", U, Z["F"], "Kleine losse stukjes kunnen ingeslikt worden."),
    sorteer("Welke spelvorm?", ["spelen met dingen", "spelen door bewegen", "creatief spelen", "fantasiespel", "tekenen", "spelen met taal"],
            [("blokken sorteren op kleur", "spelen met dingen"), ("een hindernissenparcours lopen", "spelen door bewegen"), ("een kasteel boetseren", "creatief spelen"), ("dokter spelen met een knuffel", "fantasiespel"), ("een tekening maken van je familie", "tekenen"), ("zelf rijmpjes verzinnen", "spelen met taal")],
            "Zes spelvormen."),
    volgorde("Zet de stappen van een activiteit in de juiste volgorde.",
             ["het materiaal klaarzetten en de ruimte nakijken", "de afspraken uitleggen", "de kinderen opvolgen tijdens het spel", "samen opruimen en kort nabespreken"],
             "Voorbereiden, begeleiden en afronden."),
    casus(KRALEN, [
        mk("Waarop let je meteen voor het broertje van één jaar?",
           ["dat de kleine kraaltjes buiten zijn bereik liggen", "dat hij ook zelf een lange, kleurrijke draad krijgt om mee te doen", "dat hij de mooiste kralen mag kiezen", "dat hij stil blijft zitten aan tafel"],
           0, "Een kind van één stopt alles in zijn mond."),
        keuze("Kralen rijgen oefent vooral de [[*fijne|grove]] motoriek.", "Precieze bewegingen met de vingers."),
        mk("Wat doe je bij Ella?",
           ["je geeft haar grotere kralen, zodat het toch lukt", "je laat haar stoppen en aan de kant zitten", "je neemt het over en maakt de hele ketting voor haar af", "je zegt dat ze beter moet opletten"],
           0, "Je past de activiteit aan, zodat het kind toch slaagt."),
        keuze("Na de activiteit [[*ruimen de kinderen samen met jou op|ruim jij alleen op terwijl zij spelen|blijft alles liggen tot morgen]].", "Opruimen leert zorg dragen."),
    ]),
    tabel("Past dit speelgoed bij deze leeftijd?",
          [("een rammelaar voor een baby", J), ("een verkleedkoffer voor een kleuter", J), ("knikkers voor een baby", F), ("een grote bal voor een peuter", J)],
          "Leeftijd en veiligheid gaan samen."),
    koppel("Koppel het speelgoed aan wat het vooral oefent.",
           [("een bal", "de grove motoriek"), ("kralen rijgen", "de fijne motoriek"), ("een prentenboek", "de taalontwikkeling"), ("een verkleedkoffer", "het fantasiespel")],
           ["de prijs"],
           "Je kiest speelgoed op wat het kind ermee leert."),
    keuze("Een begeleider mag meespelen, zolang [[*het spel van het kind blijft|zij alle regels bepaalt|het kind stil zit]].", "Het kind blijft de baas over zijn spel."),
    tabel("Is dit een veiligheidsrisico bij speelgoed?",
          [("kleine losse stukjes bij een baby", J), ("scherpe randen", J), ("een felle kleur", F), ("een wankel klimrek", J), ("een zacht knuffeldier zonder losse delen", F)],
          "Kijk naar kleine stukjes, randen en stevigheid."),
    keuze("Een peuter die blokken in en uit een doos doet, is vooral [[*met dingen|met taal|een fantasiespel]] aan het spelen.", "Hij onderzoekt wat hij met voorwerpen kan."),
    inv("Hoe noem je de spelvorm waarbij een kind knutselt, boetseert of zelf iets bouwt? Twee woorden.", ["creatief spelen", "creatief spel"], "Creatief spelen."),
    mk("Wat leert een kleuter als hij met vriendjes winkeltje speelt?",
       ["zich inleven, taal gebruiken en samen afspreken", "enkel rekenen met echt geld", "stil op zijn stoel zitten en enkel luisteren naar de juf", "alleen spelen zonder anderen"],
       0, "In een rol kruipen vraagt inleving, taal en overleg."),
    tabel("Hoort dit bij het voorbereiden van een activiteit?",
          [("het materiaal klaarzetten", J), ("de ruimte veilig maken", J), ("samen opruimen", F), ("de afspraken uitleggen", J)],
          "Opruimen hoort bij het afronden."),
    keuze("Opruimen na het spel is [[*een deel van de activiteit|een straf|overbodig]].", "Het hoort bij het afronden."),
    sleep("Bij het kiezen van speelgoed let je op de [[leeftijd]], de [[veiligheid]] en wat het kind ermee [[leert]].",
          ["prijs", "merk"],
          "De prijs komt niet eerst."),
    keuze("Een kind tekent zijn familie, lang voor het kan schrijven. Tekenen is een manier om [[*vorm te geven aan ideeën en gevoelens|de fijne motoriek te vermijden|stil te zijn]].", "Tekenen is ook een spelvorm."),
    keuze("Rijmpjes, moppen en zelfverzonnen woorden horen bij [[*spelen met taal|spelen door bewegen|spelen met dingen]].", "Spelen met woorden."),
    keuze("Tijdens een activiteit [[*volg je de kinderen op en help je waar nodig|zit je op je gsm|laat je de kinderen helemaal alleen]].", "Je kijkt, helpt en past aan."),
    mk("Waarom is een verkleedkoffer geschikt voor een kleuter?",
       ["hij denkt symbolisch en speelt graag doen-alsof", "hij kan al vlot lezen", "hij moet leren stilzitten", "verkleden traint vooral het rekenen met grote getallen"],
       0, "Doen-alsof hoort helemaal bij de kleuter."),
    tabel("Klopt dit over spel en speelgoed?",
          [("Fantasiespel vraagt overleg met andere kinderen.", J), ("Een baby ontdekt speelgoed met ogen, oren, mond en handen.", J), ("Een peuter speelt vooral spelletjes met ingewikkelde regels.", F), ("Spel komt vanzelf op gang, ook zonder tijd en ruimte.", F)],
          "Een peuter onderzoekt vooral voorwerpen."),
    keuze("Klimmen, rennen en fietsen zijn [[*spelen door bewegen|spelen met taal|creatief spelen]].", "Het lichaam is het speelgoed."),
    mk("Je mag één speelgoed kopen voor een baby van zes maanden. Wat kies je?",
       ["een zachte rammelaar zonder losse stukjes", "een doos met heel kleine bouwsteentjes", "een spel met kaartjes en ingewikkelde regels", "een boek met lange verhalen zonder prenten"],
       0, "Veilig en passend bij de leeftijd."),
    keuze("Na de activiteit bespreek je kort [[*hoe het ging|wie het slechtst deed|helemaal niets]] met de kinderen.", "Nabespreken hoort bij het afronden."),
    keuze("Spelen met dingen betekent dat een kind onderzoekt wat het met [[*voorwerpen|woorden|zijn stem]] kan doen.", "Stapelen, sorteren, in elkaar steken."),
    open_("Kies speelgoed voor een kind van één jaar en voor een kind van vijf. Leg telkens uit waarom.",
          "Eén jaar: grote stapelbekers zonder kleine stukjes, want het kind onderzoekt voorwerpen en stopt alles in zijn mond. Vijf jaar: een verkleedkoffer, want een kleuter speelt graag doen-alsof."),
]

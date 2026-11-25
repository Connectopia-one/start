"""Activiteiten voor volwassenen — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_activiteiten_volwassenen: belevingsgerichte, ADL-,
functiebehoudende en recreatieve activiteiten, en kwaliteitsbewust handelen:
veilig, hygiënisch, ergonomisch, economisch en duurzaam. Met twee
zelfgetekende prenten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, ROOD, GEEL, LICHTGROEN

# ── Prent 1: de dagzaal van bovenaf ───────────────────────────────────
DZ = Prent("dagzaal-bovenaf", "De dagzaal van het woonzorgcentrum, van bovenaf", "een grondplan van een zaal met vijf dingen, letters A tot E")
DZ.rect(60, 60, 880, 540, "#f7f4ea", DONKER, 4, 5)
DZ.rect(440, 590, 120, 20, "#ffffff", DONKER, 0, 2); DZ.tekst(500, 630, "deur", 16)
# A: losse mat in het looppad
DZ.rect(420, 470, 160, 80, ROOD, DONKER, 4, 2)
for k in range(9):
    DZ.lijn(425 + k * 19, 550, 425 + k * 19, 562, DONKER, 2)
# B: tafel met stoelen
DZ.rect(140, 140, 220, 140, ORANJE, DONKER, 8, 3)
for sx, sy in ((150, 110), (290, 110), (150, 285), (290, 285)):
    DZ.rect(sx, sy, 50, 30, GRIJS, DONKER, 4, 2)
# C: snoer over de vloer van lamp naar stopcontact
DZ.cirkel(800, 140, 30, GEEL, DONKER, 3)
DZ.pad("M 800 170 C 780 300 640 280 620 380 S 560 430 520 420 S 380 400 330 470 L 64 470", "none", DONKER, 4)
DZ.rect(60, 460, 14, 22, "#ffffff", DONKER, 2, 2)
# D: zetel
DZ.rect(700, 330, 190, 90, LICHTGROEN, DONKER, 16, 3); DZ.rect(700, 330, 190, 25, LICHTGROEN, DONKER, 10, 3)
# E: natte plek
DZ.pad("M 640 500 C 620 470 690 455 720 480 C 760 470 780 520 740 535 C 700 555 650 540 640 500 Z", "#9ec7e6", BLAUW, 2)
LET = {"A": (390, 510), "B": (250, 210), "C": (650, 330), "D": (795, 385), "E": (690, 503)}
for t, (x, y) in LET.items():
    DZ.letter(x, y, t)
ZD = {"A": [Prent.zone(370, 460, 220, 110)], "B": [Prent.zone(130, 100, 240, 220)], "C": [Prent.zone(580, 150, 260, 220), Prent.rond(650, 330, 30), Prent.zone(70, 400, 520, 80)],
      "D": [Prent.zone(690, 320, 210, 110)], "E": [Prent.zone(610, 450, 180, 110)]}
U1 = "dagzaal-bovenaf.svg"

# ── Prent 2: twee manieren van tillen ──────────────────────────────────
TL = Prent("twee-keer-tillen", "Twee begeleiders tillen een doos", "twee figuren die een doos optillen, letters A en B")
HUID = "#f3dcc2"
# A: benen gestrekt, rug krom voorover, doos ver van het lichaam
TL.cirkel(170, 240, 30, HUID, DONKER, 3)
TL.pad("M 195 255 Q 260 250 300 330", "none", DONKER, 8)
TL.lijn(300, 330, 290, 540, DONKER, 8); TL.lijn(300, 330, 330, 540, DONKER, 8)
TL.lijn(200, 265, 150, 450, DONKER, 6)
TL.rect(60, 450, 130, 90, ORANJE, DONKER, 4, 3)
# B: knieën gebogen, rug recht, doos dicht tegen het lichaam
TL.cirkel(700, 230, 30, HUID, DONKER, 3)
TL.lijn(700, 260, 700, 400, DONKER, 8)
TL.lijn(700, 400, 640, 460, DONKER, 8); TL.lijn(640, 460, 680, 540, DONKER, 8)
TL.lijn(700, 400, 770, 460, DONKER, 8); TL.lijn(770, 460, 740, 540, DONKER, 8)
TL.lijn(700, 290, 740, 380, DONKER, 6)
TL.rect(715, 360, 120, 90, ORANJE, DONKER, 4, 3)
TL.lijn(40, 545, 960, 545, DONKER, 3)
TL.letter(110, 120, "A"); TL.letter(620, 120, "B")
ZT = {"A": [Prent.zone(40, 90, 400, 460)], "B": [Prent.zone(560, 90, 400, 460)]}
U2 = "twee-keer-tillen.svg"

CLAES = ("Lees de situatie.\n\n"
         "Mevrouw Claes (86) woont in een woonzorgcentrum. Ze kan nog zelf haar boterham smeren, maar dat duurt lang. "
         "Vroeger kookte ze graag voor haar grote familie. Ze is wat vergeetachtig en zit vaak alleen op haar kamer.")

VRAGEN = [
    klik("Bekijk de dagzaal. Een bewoner met een rollator komt binnen. Klik op alle valrisico's.", U1, ZD["A"] + ZD["C"] + ZD["E"],
         "Een losse mat, een snoer over de vloer en een natte plek zijn de grootste valrisico's."),
    klik("Bekijk de twee begeleiders. Klik op wie ergonomisch tilt.", U2, ZT["B"],
         "Door de knieën, rug recht, de last dicht tegen het lichaam."),
    sorteer("Welk soort activiteit?", ["belevingsgericht", "ADL", "functiebehoudend", "recreatief"],
            [("samen ruiken aan kruiden uit de tuin", "belevingsgericht"), ("zelf je tanden poetsen", "ADL"), ("samen de tafel dekken voor het middagmaal", "functiebehoudend"), ("een quiznamiddag met muziek", "recreatief"), ("een handmassage met geurende crème", "belevingsgericht"), ("zich zelf aankleden", "ADL")],
            "Beleving, dagelijkse handelingen, kunnen wakker houden, of plezier."),
    sorteer("Welke manier van kwaliteitsbewust handelen?", ["veilig", "hygiënisch", "ergonomisch", "economisch", "duurzaam"],
            [("de tafel op de juiste hoogte zetten voor je rug", "ergonomisch"), ("je handen wassen voor je de soep maakt", "hygiënisch"), ("een snoer wegnemen uit het looppad", "veilig"), ("niet meer verf uitdelen dan nodig", "economisch"), ("lege potjes hergebruiken om te knutselen", "duurzaam"), ("het afval sorteren na de activiteit", "duurzaam")],
            "Snelheid staat niet in het rijtje."),
    casus(CLAES, [
        mk("Wat doe je bij het ontbijt?",
           ["je laat haar zelf smeren en geeft haar de tijd", "je smeert alles snel voor haar, dat gaat sneller", "je geeft haar enkel nog soep, zodat ze niets hoeft te doen", "je laat haar ontbijt overslaan als ze te traag is"],
           0, "Overnemen gaat sneller, maar kost haar een stukje kunnen."),
        keuze("Zelf haar boterham smeren is een [[*ADL-activiteit|recreatieve activiteit|belevingsgerichte activiteit]].", "Een gewone dagelijkse handeling."),
        mk("Welke activiteit houdt haar kunnen het best wakker?",
           ["samen met haar groenten snijden voor de soep", "haar elke dag een uur tv laten kijken", "alles voor haar doen, zodat ze de hele dag lekker kan rusten", "haar vragen om stil te blijven zitten"],
           0, "Een functiebehoudende activiteit die aansluit bij wat ze vroeger graag deed."),
        keuze("Samen naar haar lievelingsmuziek van vroeger luisteren is een [[*belevingsgerichte|hygiënische|ergonomische]] activiteit.", "Het gaat om wat het oproept."),
        open_("Bedenk een recreatieve activiteit waarbij mevrouw Claes ook andere bewoners ontmoet.",
              "Een kooknamiddag waarbij een paar bewoners samen pannenkoeken bakken en daarna samen opeten. Mevrouw Claes kan haar oude recept delen."),
    ]),
    tabel("Is dit kwaliteitsbewust handelen?",
          [("zo snel mogelijk werken, wat er ook gebeurt", F), ("veilig en hygiënisch werken", J), ("zuinig zijn met water en energie", J), ("met een kromme rug zware dozen tillen", F)],
          "Veilig, hygiënisch, ergonomisch, economisch en duurzaam."),
    keuze("Een functiebehoudende activiteit [[*houdt wakker wat iemand nog kan|leert iets helemaal nieuws aan|is er enkel voor het plezier]].", "Wat je niet meer gebruikt, verlies je."),
    inv("Waarvoor staat de A in ADL? Eén woord.", ["activiteiten", "activiteit"], "Activiteiten van het dagelijks leven."),
    mk("Je ziet een natte plek op de vloer van de dagzaal. Wat doe je?",
       ["je droogt ze meteen op en meldt het daarna", "je laat ze liggen tot de poetsdienst morgen komt", "je legt er een losse mat over", "je vraagt een bewoner om het te doen"],
       0, "Eerst het gevaar wegnemen, daarna melden."),
    tabel("Hoort dit bij ergonomisch tillen?",
          [("door je knieën zakken", J), ("je rug recht houden", J), ("de last ver van je lichaam houden", F), ("draaien met je rug terwijl je tilt", F)],
          "De last hoort dicht tegen je lichaam."),
    keuze("Zuinig omgaan met materiaal, water en tijd heet [[*economisch|ergonomisch|recreatief]] handelen.", "Je gebruikt niet meer dan nodig."),
    tabel("Is dit een recreatieve activiteit?",
          [("een uitstap naar zee", J), ("zich wassen", F), ("een spelnamiddag", J), ("zich aankleden", F), ("een optreden van een koor", J)],
          "Wassen en aankleden zijn ADL."),
    keuze("Een bewoner van wie alles overgenomen wordt, verliest [[*sneller zijn zelfstandigheid|meer gewicht|nooit iets]].", "Zelf doen houdt zelfstandig."),
    sleep("ADL staat voor activiteiten van het [[dagelijks]] leven, zoals je [[wassen]], je aankleden en zelf [[eten]].",
          ["weekend", "sporten"],
          "Gewone dagelijkse handelingen."),
    mk("Je maakt soep met bewoners. Wat doe je eerst?",
       ["iedereen wast zijn handen", "je snijdt alle groenten alleen", "je zet de muziek luid", "je gooit de schillen bij het restafval"],
       0, "Zeker bij voedsel en bij kwetsbare mensen."),
    keuze("Losse matten, snoeren en natte vloeren zijn de grootste [[*valrisico's|ADL-activiteiten|kwaliteitsnormen]].", "Daarom houd je het looppad vrij."),
    tabel("Klopt dit over activiteiten voor volwassenen?",
          [("Een belevingsgerichte activiteit spreekt de zintuigen aan.", J), ("Recreatie heeft ontspanning als doel.", J), ("Hygiënisch werken is enkel nodig bij kinderen.", F), ("Snelheid is het belangrijkste kenmerk van kwaliteit.", F)],
          "Snelheid is geen kwaliteit."),
    keuze("Een activiteit lukt niet bij een bewoner. Je [[*maakt de stap kleiner of helpt een deel|stopt er meteen mee|laat hem alleen proberen tot het lukt]].", "Zo lukt er toch iets."),
    inv("Hoe noem je een activiteit die een vaardigheid wakker houdt? Eén woord.", ["functiebehoudend", "functiebehoudende activiteit", "functiebehoudende"], "Een functiebehoudende activiteit."),
    mk("Waarom is hygiënisch werken extra belangrijk bij ouderen?",
       ["ze zijn kwetsbaarder voor besmetting", "ouderen houden eigenlijk helemaal niet van de geur van zeep", "hygiëne is enkel nodig bij voedsel", "het gaat sneller dan veilig werken"],
       0, "Besmetting is bij ouderen een echt risico."),
    keuze("Je ziet een onveilige situatie. Je [[*neemt het gevaar meteen weg en meldt het|wacht tot iemand anders het ziet|schrijft het op voor volgende week]].", "Eerst wegnemen, dan melden."),
    tabel("Is dit duurzaam handelen bij een activiteit?",
          [("materiaal hergebruiken", J), ("het afval sorteren", J), ("de kraan laten lopen tijdens het schilderen", F), ("alles na één keer weggooien", F)],
          "Duurzaam is aan later denken."),
    mk("Een bewoner met dementie wordt rustig van de geur van lavendel. Welk soort activiteit bied je aan?",
       ["een belevingsgerichte activiteit", "een ADL-activiteit zoals zich zelf wassen", "een functiebehoudende rekenquiz", "een ergonomische tiloefening"],
       0, "De beleving zelf is het doel."),
    keuze("Na de activiteit [[*maak je het materiaal schoon en berg je het op|laat je alles staan voor de volgende|gooi je alles weg]].", "Zo blijft het bruikbaar."),
    keuze("Een bewoner die zich nog zelf kan aankleden, laat je dat [[*zelf doen|nooit meer doen|enkel op zondag doen]].", "Zelf doen houdt zijn kunnen vast."),
    keuze("Genoeg licht en een vrije doorgang in de zaal horen bij [[*veilig|economisch|recreatief]] werken.", "Niets om over te struikelen."),
]

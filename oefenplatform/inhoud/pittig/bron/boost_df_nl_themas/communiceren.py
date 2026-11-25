"""Lichaamstaal, beleefdheid en een tekst die werkt — pittig (Boost dubbele finaliteit, Nederlands).

Strikt binnen nldf_communiceren: non-verbale communicatie, beleefdheid en
register, een gesprek beginnen, gaande houden en beëindigen, en de criteria
voor spreken en schrijven. Met twee zelfgetekende prenten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, LICHTGROEN, GEEL

# ── Prent 1: een spreker voor twee luisteraars ─────────────────────────
SP = Prent("spreker-en-luisteraars", "Een presentatie voor de klas", "een spreker met een vol blad tekst en een tekstballon, en twee luisteraars")


def mens(p, x, kleur, mond="recht", armen="open"):
    p.cirkel(x, 190, 50, "#f3dcc2", DONKER, 3)
    p.cirkel(x - 18, 180, 5, DONKER, DONKER, 1); p.cirkel(x + 18, 180, 5, DONKER, DONKER, 1)
    if mond == "lach":
        p.pad(f"M {x-20} 207 Q {x} 228 {x+20} 207", "none", DONKER, 3)
    elif mond == "frons":
        p.pad(f"M {x-20} 218 Q {x} 202 {x+20} 218", "none", DONKER, 3)
        p.lijn(x - 28, 164, x - 10, 170, DONKER, 3); p.lijn(x + 28, 164, x + 10, 170, DONKER, 3)
    else:
        p.lijn(x - 16, 212, x + 16, 212, DONKER, 3)
    p.rect(x - 45, 245, 90, 170, kleur, DONKER, 14, 3)
    p.lijn(x - 25, 415, x - 25, 520, DONKER, 6); p.lijn(x + 25, 415, x + 25, 520, DONKER, 6)
    if armen == "gekruist":
        p.lijn(x - 45, 300, x + 40, 330, DONKER, 8); p.lijn(x + 45, 300, x - 40, 330, DONKER, 8)


mens(SP, 260, BLAUW)
# arm met open hand (gebaar) en arm met blad
SP.lijn(215, 270, 140, 330, DONKER, 7); SP.cirkel(132, 338, 16, "#f3dcc2", DONKER, 3)
SP.lijn(305, 270, 350, 330, DONKER, 7)
SP.rect(330, 300, 90, 120, "#ffffff", DONKER, 3, 2)
for i in range(9):
    SP.lijn(340, 315 + i * 11, 410, 315 + i * 11, GRIJS, 3)
# tekstballon
SP.rect(320, 60, 230, 70, "#ffffff", DONKER, 18, 2)
SP.pad("M 345 130 L 320 160 L 370 130", "#ffffff", DONKER, 2)
SP.tekst(435, 103, "euh ... dus ... euh ...", 20)
mens(SP, 690, LICHTGROEN, "lach")
mens(SP, 870, ORANJE, "frons", "gekruist")
LET = {"A": (90, 380), "B": (375, 450), "C": (580, 95), "D": (690, 560), "E": (870, 560)}
for t, (x, y) in LET.items():
    SP.letter(x, y, t)
U1 = "spreker-en-luisteraars.svg"
Z1 = {"A": Prent.zone(100, 310, 70, 60), "B": Prent.zone(325, 295, 100, 130), "C": Prent.zone(315, 55, 240, 110),
      "D": Prent.zone(630, 130, 120, 400), "E": Prent.zone(810, 130, 120, 400)}
for t, (x, y) in LET.items():
    Z1[t] = [Z1[t], Prent.rond(x, y, 28)]

# ── Prent 2: een sollicitatiemail ──────────────────────────────────────
ML = Prent("sollicitatiemail", "Een mail voor een vakantiejob", "een mailvenster met vijf delen, letters A tot E")
ML.rect(60, 60, 880, 540, "#ffffff", DONKER, 10, 3)
ML.rect(60, 60, 880, 50, GRIJS, DONKER, 10, 3)
ML.tekst(90, 93, "Aan: winkel De Kaasstolp", 18, "start")
ML.tekst(90, 140, "Onderwerp: sollicitatie vakantiejob juli", 18, "start")
ML.lijn(60, 160, 940, 160, GRIJS, 2)
DELEN = [("A", "Hey meneer Peeters!!"),
         ("B", "Ik wil graag solliciteren voor de vakantiejob in uw winkel."),
         ("C", "Ik ben vlot, eerlijk en ik werk graag met mensen."),
         ("D", "Laat ff weten of da ok is ;-)"),
         ("E", "Met vriendelijke groeten, Sam Janssens")]
Z2 = {}
for i, (t, zin) in enumerate(DELEN):
    y = 210 + i * 80
    ML.letter(110, y - 7, t)
    ML.tekst(150, y, zin, 21, "start")
    Z2[t] = [Prent.zone(85, y - 40, 820, 64)]

SITUATIE = ("Lees de situatie.\n\n"
            "Sam heeft een gesprek met de verantwoordelijke van een jeugdkamp, want hij wil er vrijwilliger worden. "
            "Hij komt binnen met zijn handen in de zakken, zegt 'Yo' en kijkt intussen naar zijn gsm. "
            "Tijdens het gesprek onderbreekt hij de verantwoordelijke twee keer. "
            "Op het einde staat hij op en loopt weg zonder iets te zeggen.")

VRAGEN = [
    klik("Bekijk de presentatie. Klik op wat de spreker beter vervangt door een spreekplan met kernwoorden.", U1, Z1["B"],
         "Wie een volledige tekst afleest, kijkt naar zijn blad en niet naar zijn publiek."),
    klik("Klik op wat de vlotheid van de spreker in het gedrang brengt.", U1, Z1["C"],
         "Veel stopwoordjes maken een presentatie minder vlot."),
    klik("Klik op de luisteraar die met zijn lichaamstaal toont dat de boodschap niet goed aankomt.", U1, Z1["E"],
         "Fronsen en gekruiste armen zijn signalen; de spreker kan dan iets trager gaan of een voorbeeld geven."),
    klik("Klik op het gebaar van de spreker, een vorm van non-verbale communicatie.", U1, Z1["A"],
         "Een open hand ondersteunt wat je zegt, zonder woorden."),
    klik("Bekijk de mail. Klik op alle delen die niet passen in een formele mail.", "sollicitatiemail.svg", Z2["A"] + Z2["D"],
         "Een aanhef met 'Hey' en twee uitroeptekens, afkortingen, tussentaal en een knipoog horen niet in een sollicitatie."),
    klik("Klik op het deel dat het tekstdoel van de mail het duidelijkst zegt.", "sollicitatiemail.svg", Z2["B"],
         "Sam wil solliciteren: dat moet de lezer meteen weten."),
    casus(SITUATIE, [
        keuze("Handen in de zakken en naar je gsm kijken is [[*non-verbale|verbale]] communicatie.", "Je zegt er niets mee, en toch komt het over."),
        keuze("'Yo' als begroeting is hier het verkeerde [[*register|kanaal|tekstdoel]].", "Bij een volwassene die je niet kent, groet je formeler."),
        keuze("Sam onderbreekt de verantwoordelijke. Dat botst met de [[*beleefdheidsconventies|spellingregels|tekststructuur]].", "Iemand laten uitspreken hoort bij een beleefd gesprek."),
        mk("Wat ontbreekt er op het einde van het gesprek?",
           ["bedanken en groeten", "nog een laatste blik op zijn gsm voor hij vertrekt", "een grap om de sfeer wat losser te maken", "een tweede keer 'Yo' zeggen bij het buitengaan"],
           0, "Een gesprek correct voeren betekent het ook netjes beëindigen."),
        open_("Schrijf in één of twee zinnen hoe Sam het gesprek beter kan beginnen.",
              "Goedemiddag, ik ben Sam Janssens. Dank u dat ik even mag langskomen; ik wil graag vrijwilliger worden op uw kamp."),
    ]),
    sorteer("Verbaal of non-verbaal?", ["verbaal", "non-verbaal"],
            [("de woorden die je kiest", "verbaal"), ("je intonatie", "non-verbaal"), ("een emoji in een bericht", "non-verbaal"), ("de zinnen in je mail", "verbaal"), ("de afstand tot je gesprekspartner", "non-verbaal"), ("je kleding op een sollicitatie", "non-verbaal")],
            "Non-verbaal is alles wat je overbrengt zonder woorden."),
    koppel("Koppel het begrip aan de uitleg.",
           [("articulatie", "hoe duidelijk je de klanken vormt"), ("intonatie", "hoe je stem stijgt en daalt"), ("volume", "hoe luid je spreekt"), ("tempo", "hoe snel je spreekt")],
           ["hoe goed je spelt"],
           "Spelling hoort bij schrijven, niet bij je stem."),
    tabel("Geldt dit criterium voor spreken, voor schrijven of voor allebei?",
          [("spelling en leestekens", "schrijven"), ("uitspraak en intonatie", "spreken"), ("woordenschat", "allebei"), ("lay-out", "schrijven"), ("taakvoltooiing", "allebei")],
          "Bij elke opdracht telt of je doel bereikt is.", ["spreken", "schrijven", "allebei"]),
    mk("Je presenteert voor de klas en ziet veel luisteraars fronsen. Wat doe je best?",
       ["iets trager gaan en een voorbeeld geven", "gewoon sneller praten, zodat je sneller klaar bent", "luider spreken en niet meer naar de klas kijken", "je blad nemen en alles letterlijk voorlezen"],
       0, "Je reageert op de lichaamstaal van je publiek."),
    tabel("Spreek je deze persoon aan met u of met jij?",
          [("de directeur van een bedrijf waar je solliciteert", "u"), ("je beste vriend", "jij"), ("een onbekende oudere dame op de bus", "u"), ("je neef van twintig", "jij")],
          "Het gaat om afstand, niet enkel om leeftijd.", ["u", "jij"]),
    mk("Wat is het tekstdoel van een sollicitatiebrief?",
       ["iemand overtuigen om jou te kiezen", "iemand stap voor stap iets uitleggen", "iemand ontspannen met een grappig verhaal", "iemand informeren over het nieuws van de dag"],
       0, "Je wil de lezer overtuigen dat jij de juiste persoon bent."),
    tabel("Hoort dit in een goed spreekplan?",
          [("kernwoorden in de juiste volgorde", J), ("de volledige tekst, woord voor woord", F), ("een inleiding, een midden en een slot", J), ("zo veel mogelijk moeilijke woorden", F)],
          "Met kernwoorden hou je je lijn vast en blijf je vrij spreken."),
    keuze("Je laat niet elke zin met hetzelfde woord beginnen. Dat heet [[*variatie in zinsbouw|taakvoltooiing|articulatie]].", "Variatie houdt je lezer of luisteraar bij de les."),
    mk("Je mail is foutloos, maar de ontvanger weet na het lezen nog altijd niet wat je vraagt. Welk criterium haal je niet?",
       ["taakvoltooiing", "spelling en leestekens", "lay-out en alinea's", "woordenschat"],
       0, "Een tekst zonder fouten die zijn doel mist, voldoet niet."),
    sorteer("Hoort dit bij het begin, het midden of het einde van een gesprek?", ["beginnen", "gaande houden", "beëindigen"],
            [("jezelf voorstellen en groeten", "beginnen"), ("een vraag stellen over wat de ander zei", "gaande houden"), ("bedanken voor het gesprek", "beëindigen"), ("knikken terwijl de ander spreekt", "gaande houden"), ("zeggen waarom je komt", "beginnen"), ("afspreken wat er nu volgt", "beëindigen")],
            "Drie aparte vaardigheden."),
    tabel("Klopt dit over non-verbale communicatie?",
          [("Wie met gekruiste armen luistert, kan afwijzend overkomen.", J), ("Intonatie hoort bij wat je schrijft.", F), ("Non-verbale signalen kunnen je woorden tegenspreken.", J), ("De afstand tot je gesprekspartner zegt niets.", F)],
          "Intonatie hoor je enkel als iemand spreekt."),
    inv("Hoe noem je de uitdrukking op je gezicht terwijl je spreekt? Eén woord.", ["mimiek", "de mimiek"], "Mimiek."),
    mk("'Ja hoor, super leuk', zegt je vriend met een zucht en rollende ogen. Wat geloof je?",
       ["de lichaamstaal: hij vindt het niet leuk", "de woorden: hij vindt het echt super leuk", "geen van beide, want zuchten betekent niets", "allebei evenveel, want ze zeggen hetzelfde"],
       0, "Als woorden en lichaamstaal botsen, zegt de lichaamstaal vaak meer."),
    keuze("Wie tijdens een presentatie te stil spreekt, moet letten op zijn [[*volume|articulatie|spelling]].", "Volume gaat over hoe luid je spreekt."),
    sleep("Een mail aan een onbekende volwassene begint met een nette [[aanhef]], spreekt de ontvanger aan met [[u]] en sluit af met een [[slotgroet]] zoals 'Met vriendelijke groeten'.",
          ["jij", "emoji"],
          "Zo kies je een formeel register."),
    tabel("Past dit in een chatbericht aan een goede vriend?",
          [("een smiley", J), ("'Geachte heer'", F), ("een korte zin zonder aanhef", J), ("'Hoogachtend'", F)],
          "Een chat met een vriend is informeel."),
    mk("Welke zin past het best in een mail aan een leerkracht die je niet goed kent?",
       ["Zou u mij de opdracht nog eens kunnen bezorgen?", "Hey, stuur jij die opdracht ff opnieuw?", "Ik heb die opdracht niet, dus stuur maar door!", "Yo, waar staat die opdracht nu weer ergens online?"],
       0, "Met u en een beleefde vraag kies je het juiste register."),
    keuze("Een emoji in een bericht doet wat je [[*gezicht|spelling|alinea]] doet als je spreekt.", "Hij geeft de toon aan bij de woorden."),
    open_("Je geeft morgen een korte presentatie over je hobby. Geef drie tips voor je non-verbale communicatie.",
          "Kijk je publiek aan in plaats van je blad. Sta rechtop en gebruik je handen om iets aan te wijzen. Spreek luid genoeg en niet te snel."),
]

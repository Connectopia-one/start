"""De fysieke ontwikkeling — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_fysiek: lengte, gewicht en
lichaamsverhoudingen, de sensorische, de motorische en de sensomotorische
ontwikkeling. Met vier silhouetten en een zelfgetekende groeicurve."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ROOD, assen

SI = Prent("vier-silhouetten", "Vier silhouetten, even groot getekend", "vier figuren met een andere verhouding tussen hoofd en lichaam, letters A tot D")
def silhouet(cx, deel):
    hoog = 440; top = 90
    r = hoog / deel / 2
    SI.cirkel(cx, top + r, r, GRIJS, DONKER, 3)
    romp = top + 2 * r
    been = (hoog - 2 * r) * 0.5
    SI.rect(cx - r * 0.9 - 8, romp, 2 * r * 0.9 + 16, hoog - 2 * r - been, GRIJS, DONKER, 8, 3)
    SI.rect(cx - r * 0.9 - 6, romp + hoog - 2 * r - been, r * 0.9, been, GRIJS, DONKER, 6, 2)
    SI.rect(cx + 6, romp + hoog - 2 * r - been, r * 0.9, been, GRIJS, DONKER, 6, 2)
    SI.lijn(cx - 90, top + hoog, cx + 90, top + hoog, "#8a8470", 2)
VIER = [("A", 140, 8), ("B", 380, 4), ("C", 620, 5.5), ("D", 860, 7)]
for t, cx, deel in VIER:
    silhouet(cx, deel); SI.letter(cx, 580, t)
U1 = "vier-silhouetten.svg"
Z1 = {t: [Prent.zone(cx - 110, 80, 220, 530)] for t, cx, d in VIER}

GC = Prent("groeicurve-lengte", "De lengte van Tom van 0 tot 18 jaar", "een grafiek van lengte tegen leeftijd met letters A tot D op de lijn")
Xg, Yg = assen(GC, 0, 18, 40, 200, "leeftijd (jaar)", "lengte (cm)", 2, 20)
PUNTEN = [(0, 50), (1, 75), (2, 87), (4, 102), (6, 115), (8, 127), (10, 138), (11, 143), (12, 149), (13, 157), (14, 166), (15, 172), (16, 176), (17, 178), (18, 179)]
GC.pad("M " + " L ".join(f"{Xg(a):.1f} {Yg(l):.1f}" for a, l in PUNTEN), "none", BLAUW, 5)
LET = {"A": (0.6, 66), "B": (7, 121), "C": (12.5, 153), "D": (17.5, 178.5)}
for t, (a, l) in LET.items():
    GC.letter(Xg(a) + 26, Yg(l) - 24, t)
U2 = "groeicurve-lengte.svg"
Z2 = {t: [Prent.rond(Xg(a) + 13, Yg(l) - 12, 44)] for t, (a, l) in LET.items()}

LOTTE = ("Lees het verslag van een kinderverzorgster.\n\n"
         "Lotte is acht maanden. Ze zit stevig zonder steun en begint te kruipen. Als ze een blokje ziet, strekt ze haar hand uit en pakt het met haar hele hand. "
         "Elk nieuw voorwerp gaat meteen naar haar mond. Een fijne pincetgreep met duim en wijsvinger lukt nog niet.")

VRAGEN = [
    klik("De vier figuren zijn even groot getekend. Klik op de figuur met de lichaamsverhoudingen van een pasgeborene.", U1, Z1["B"], "Bij een pasgeborene is het hoofd ongeveer een vierde van de lengte."),
    klik("Klik op de figuur met de lichaamsverhoudingen van een volwassene.", U1, Z1["A"], "Het hoofd is dan nog maar een klein deel van de lengte."),
    klik("Bekijk de groeicurve van Tom. Klik op de letter bij de groeispurt.", U2, Z2["C"], "De snelle groei van de puberteit."),
    klik("Klik op de letter waar Tom traag en gelijkmatig groeit.", U2, Z2["B"], "Tussen de kleutertijd en de puberteit."),
    klik("Klik op de letter waar Tom bijna niet meer groeit.", U2, Z2["D"], "Na de puberteit vlakt de lijn af."),
    klik("Klik op de letter waar Tom het allersnelst groeit.", U2, Z2["A"], "In de babytijd groeit een kind het snelst van al."),
    casus(LOTTE, [
        sorteer("Welke ontwikkeling zie je hier vooral?", ["grove motoriek", "fijne motoriek", "sensomotorisch"],
                [("zitten zonder steun", "grove motoriek"), ("beginnen kruipen", "grove motoriek"), ("een blokje zien en ernaar grijpen", "sensomotorisch"), ("de pincetgreep met duim en wijsvinger", "fijne motoriek")],
                "Het oog stuurt de hand: dat is sensomotorisch."),
        mk("Waarom steekt Lotte alles in haar mond?",
           ["ze onderzoekt het met haar mond", "ze heeft altijd honger op die leeftijd", "ze wil de volwassenen boos maken", "ze kan nog niet zien wat ze vastheeft"],
           0, "De mond is in die fase het gevoeligste zintuig."),
        keuze("Dat de pincetgreep nog niet lukt, past bij de regel dat de grove motoriek zich [[*vóór|na]] de fijne motoriek ontwikkelt.", "Van groot naar klein."),
        keuze("Lotte zat eerst en begint nu te kruipen. Die orde ligt vast door de [[*rijping|groeispurt|sensorische ontwikkeling]].", "De orde ligt vast, het tempo niet."),
    ]),
    volgorde("In welke orde leert een baby zich meestal bewegen?",
             ["rollen", "zitten", "kruipen", "stappen"],
             "Sommige kinderen slaan het kruipen over."),
    sorteer("Fijne of grove motoriek?", ["fijne motoriek", "grove motoriek"],
            [("een veter knopen", "fijne motoriek"), ("huppelen", "grove motoriek"), ("een potlood vasthouden", "fijne motoriek"), ("klimmen in een rek", "grove motoriek"), ("een knoop dichtdoen", "fijne motoriek"), ("een bal trappen", "grove motoriek")],
            "Kleine spieren van de hand tegenover grote spieren."),
    tabel("Klopt dit over de fysieke ontwikkeling?",
          [("Een baby hoort al geluiden voor de geboorte.", J), ("Het zicht is bij een pasgeborene het scherpste zintuig.", F), ("De meeste babyreflexen verdwijnen in het eerste jaar.", J), ("Jongens en meisjes beginnen hun groeispurt op hetzelfde moment.", F)],
          "Meisjes beginnen gemiddeld twee jaar vroeger."),
    koppel("Koppel het begrip over de fysieke ontwikkeling aan de uitleg.",
           [("reflex", "een beweging zonder nadenken"), ("gecontroleerde beweging", "een beweging die het kind zelf bestuurt"), ("sensorisch", "over de zintuigen"), ("sensomotorisch", "zintuigen en beweging samen")],
           ["over de grootte van de organen"], "Reflexen maken plaats voor gecontroleerde bewegingen."),
    mk("Een adolescent stoot na een groeispurt overal tegen. Waarom?",
       ["de besturing moet zich aanpassen", "zijn zintuigen werken plots slechter dan vroeger", "zijn fijne motoriek is helemaal verdwenen", "hij heeft geen reflexen meer na de puberteit"],
       0, "Armen en benen zijn plots langer."),
    keuze("Een baby heft eerst zijn hoofd, daarna zijn romp, en pas later staat hij. De motoriek gaat van [[*hoofd naar voeten|voeten naar hoofd|links naar rechts]].", "En van het midden naar buiten."),
    tabel("Hoort dit bij de fysieke ontwikkeling in de adolescentie?",
          [("de groeispurt", J), ("de geslachtsrijping", J), ("de zuigreflex", F), ("de stemverandering", J)],
          "De zuigreflex hoort bij de pasgeborene."),
    keuze("Een kind dat veel sport, heeft een betere uithouding. Ook de fysieke ontwikkeling hangt dus af van [[*nurture|alleen nature|alleen rijping]].", "Oefening is omgeving."),
    mk("Waarom meet de arts bij elk consult opnieuw de lengte?",
       ["om de lijn over de tijd te volgen", "omdat één meting precies alles zegt over een kind", "om te weten hoe groot het kind later wordt", "omdat de lengte elke week sterk verandert"],
       0, "Een plotse knik in de lijn vraagt aandacht."),
    sleep("Kleuters oefenen met [[knippen]] en rijgen om de [[fijne]] motoriek klaar te maken voor het [[schrijven]].",
          ["grove", "lopen"], "De hand wordt klaargemaakt."),
    keuze("Schrijven hoort bij de fysieke én de [[*cognitieve|morele|sensorische]] ontwikkeling: de hand vormt de letter, het denken kiest het woord.", "Wisselwerking tussen domeinen."),
    inv("Je streelt de wang van een pasgeborene en hij draait zijn hoofd en begint te zuigen. Is dat een reflex of een gecontroleerde beweging? Eén woord.", ["reflex", "een reflex"], "Het gebeurt vanzelf, zonder dat het kind het wil."),
    tabel("Klopt dit over de late volwassenheid?",
          [("Zicht en gehoor nemen af.", J), ("Kracht en evenwicht nemen af.", J), ("Bewegen is dan onmogelijk.", F)],
          "Oefening helpt."),
    keuze("Bij een pasgeborene werken horen en voelen al veel beter dan [[*zien|ruiken|proeven]].", "Een baby ziet eerst maar twintig tot dertig centimeter scherp."),
    keuze("Een kleuter is minder mollig dan een peuter: zijn [[*lichaamsverhoudingen|reflexen|zintuigen]] veranderen.", "De benen worden langer."),
    keuze("Elk kind doorloopt de motorische mijlpalen in dezelfde [[*orde|leeftijd]], maar niet op dezelfde leeftijd.", "Het ene kind stapt op tien maanden, het andere op zestien."),
    mk("Een zwangere vrouw krijgt de raad goed te eten en niet te roken. Waarom weegt de prenatale fase fysiek zo zwaar?",
       ["dan worden alle organen gevormd", "dan groeit een kind het snelst in lengte van zijn hele leven", "dan leert een kind al zijn reflexen bewust te gebruiken", "dan ontwikkelt de fijne motoriek zich het snelst"],
       0, "Uit één cel ontstaat een heel lichaam."),
    tabel("Staat dit op een groeicurve?",
          [("de lengte", J), ("de leeftijd", J), ("de percentiellijnen", J), ("de schoenmaat", F)],
          "Lengte of gewicht tegen leeftijd."),
    keuze("Veel mensen hebben vanaf hun veertigste een [[*leesbril|hoorapparaat|wandelstok]] nodig, omdat het zicht minder scherp wordt.", "De zintuigen worden minder scherp."),
    open_("Leg uit waarom kruipen belangrijk is voor de motorische ontwikkeling.",
          "Kruipen oefent de grote spieren van de schouders en de romp, en de samenwerking tussen links en rechts. Het kind gebruikt ook ogen en handen samen om ergens naartoe te gaan. Zo wordt het lichaam klaargemaakt voor stappen en later voor fijnere bewegingen."),
]

"""Mens en dier — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_mens_dier: de traditionele tweedeling en de
visies van Aristoteles, Descartes, Darwin en Singer in tijd en ruimte. Met vier
zelfgetekende zinnebeelden."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ORANJE, LICHTGROEN, GROEN

MD = Prent("vier-zinnebeelden-mens-dier", "Vier zinnebeelden over mens en dier", "vier vakjes met een tekening, letters A tot D")
VK = [("A", 60, 80), ("B", 290, 80), ("C", 520, 80), ("D", 750, 80)]
for t, x, y in VK:
    MD.rect(x, y, 200, 430, "#ffffff", DONKER, 12, 3)
    MD.letter(x + 100, y + 470, t)
# A: tandwielen
def tandwiel(cx, cy, r):
    pts = []
    for i in range(24):
        a = i * math.pi / 12
        rr = r + (10 if i % 2 == 0 else 0)
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    MD.svg(f'<polygon points="{" ".join(pts)}" fill="#d9d4c4" stroke="{DONKER}" stroke-width="3"/>')
    MD.cirkel(cx, cy, r / 3, "#ffffff", DONKER, 2)
tandwiel(150, 220, 50); tandwiel(185, 345, 38)
# B: boom met takken die zich splitsen
MD.lijn(390, 480, 390, 380, ORANJE, 8)
for (x1, y1, x2, y2) in ((390, 380, 330, 290), (390, 380, 450, 290), (330, 290, 310, 200), (330, 290, 360, 200), (450, 290, 420, 200), (450, 290, 470, 200), (310, 200, 305, 140), (470, 200, 462, 140)):
    MD.lijn(x1, y1, x2, y2, ORANJE, 5)
for (x, y) in ((305, 135), (360, 195), (420, 195), (480, 135), (310, 195)):
    MD.cirkel(x, y, 11, LICHTGROEN, DONKER, 2)
# C: weegschaal in evenwicht met een mens en een dier
MD.lijn(620, 140, 620, 420, DONKER, 5); MD.lijn(545, 180, 695, 180, DONKER, 5)
for cx in (555, 685):
    MD.lijn(cx, 180, cx - 25, 250, DONKER, 2); MD.lijn(cx, 180, cx + 25, 250, DONKER, 2)
    MD.pad(f"M {cx-32} 250 Q {cx} 275 {cx+32} 250 Z", GEEL, DONKER, 2)
MD.cirkel(555, 222, 8, GRIJS, DONKER, 2); MD.rect(549, 230, 12, 20, GRIJS, DONKER, 3, 2)
MD.ellips(685, 238, 18, 10, GRIJS, DONKER, 2); MD.cirkel(705, 228, 7, GRIJS, DONKER, 2)
MD.rect(590, 415, 60, 12, GRIJS, DONKER, 3)
# D: ladder met een mens bovenaan en een dier lager
MD.lijn(810, 140, 810, 480, DONKER, 4); MD.lijn(890, 140, 890, 480, DONKER, 4)
for i in range(6):
    MD.lijn(810, 170 + i * 60, 890, 170 + i * 60, DONKER, 3)
MD.cirkel(850, 120, 12, GRIJS, DONKER, 2); MD.rect(840, 132, 20, 30, GRIJS, DONKER, 4, 2)
MD.ellips(850, 400, 22, 12, GRIJS, DONKER, 2); MD.cirkel(875, 390, 8, GRIJS, DONKER, 2)
U = "vier-zinnebeelden-mens-dier.svg"
Z = {t: [Prent.zone(x, y, 200, 480)] for t, x, y in VK}

KRAAI = ("Lees het bericht.\n\n"
         "In een proef kreeg een kraai een rechte draad en een buisje met eten. De kraai boog de draad tot een haakje en viste het eten eruit. "
         "Een onderzoeker zegt: « Werktuigen maken dachten we vroeger enkel bij mensen te zien. »")

VRAGEN = [
    klik("Bekijk de vier zinnebeelden. Klik op het zinnebeeld dat het best past bij Descartes' kijk op dieren.", U, Z["A"], "Dieren als ingewikkelde automaten."),
    klik("Klik op het zinnebeeld dat het best past bij Darwin.", U, Z["B"], "Mens en dier als takken aan dezelfde boom."),
    klik("Klik op het zinnebeeld dat het best past bij Peter Singer.", U, Z["C"], "Lijden weegt even zwaar, welke soort ook."),
    klik("Klik op het zinnebeeld dat het best past bij de traditionele tweedeling.", U, Z["D"], "De mens staat boven het dier."),
    casus(KRAAI, [
        keuze("Deze proef zet de traditionele tweedeling onder druk, want [[*dieren kunnen meer dan gedacht|kraaien zijn eigenlijk mensen|werktuigen bestaan niet]].", "Wat men voor menselijk hield, komt ook bij dieren voor."),
        mk("Welke filosoof zou zeggen dat de kraai enkel als een machine werkt?",
           ["Descartes", "Darwin, de Engelse bioloog uit de negentiende eeuw", "Singer, de Australische filosoof van vandaag", "Aristoteles, de leerling van Plato in Athene"],
           0, "Zonder denkende geest is een dier voor hem een automaat."),
        keuze("Darwin zou zeggen dat het verschil tussen de kraai en de mens een verschil in [[*graad|soort|plaats]] is.", "Mensen kunnen meer van hetzelfde, niet iets volkomen anders."),
        tabel("Klopt dit na de proef?",
              [("De biologie beslist nu wat het verschil betekent.", F), ("De proef geeft gegevens die de filosofie overweegt.", J), ("De vraag naar mens en dier blijft open.", J)],
              "Onderzoek levert gegevens, geen beslissing over wat ze betekenen."),
    ]),
    koppel("Koppel de filosoof aan zijn tijd en plaats.",
           [("Aristoteles", "Athene, vierde eeuw voor Christus"), ("Descartes", "Frankrijk, zeventiende eeuw"), ("Darwin", "Engeland, negentiende eeuw"), ("Singer", "Australië, vandaag")],
           ["Rome, eerste eeuw"], "Hun tijd verklaart mee hun antwoord."),
    volgorde("Zet deze denkers over mens en dier in de volgorde waarin ze leefden.",
             ["Aristoteles", "Descartes", "Darwin", "Singer"],
             "Oudheid, zeventiende eeuw, negentiende eeuw, vandaag."),
    sorteer("Verkleint deze filosoof de kloof tussen mens en dier, of maakt hij ze groot?", ["verkleint de kloof", "maakt de kloof groot"],
            [("Darwin", "verkleint de kloof"), ("Singer", "verkleint de kloof"), ("Descartes", "maakt de kloof groot")],
            "Darwin door verwantschap, Singer door het lijden."),
    mk("Hoe noemde Aristoteles de mens, en wat zegt dat over het verschil met dieren?",
       ["een redelijk dier: zelfde natuur, maar met rede", "een machine: zonder geest net als alle dieren", "een god: helemaal anders dan alle dieren", "een tak: enkel verschillend in graad, niet in rede"],
       0, "Een dier, maar met rede: dat maakt bij hem het verschil."),
    tabel("Hoorde dit volgens de traditie enkel bij de mens?",
          [("de rede", J), ("de taal", J), ("honger", F), ("moreel besef", J), ("slaap", F)],
          "Honger en slaap heeft elk dier."),
    keuze("Singer noemt het voortrekken van je eigen soort [[*speciësisme|evolutie|dualisme]].", "Net als racisme of seksisme een onderscheid dat hij niet gerechtvaardigd acht."),
    mk("Een stad twijfelt of ze een circus met wilde dieren nog toelaat. Waarom helpt de vraag naar mens en dier daarbij?",
       ["ze beslist mee wat we met dieren mogen", "omdat dieren zelf ook ethische regels opstellen", "omdat de ethiek enkel over dieren en niet over mensen gaat", "omdat Darwin een boek over goed en kwaad schreef"],
       0, "Dierproeven, veeteelt, jacht en dierenrechten."),
    sorteer("Pleit dit voor of tegen een scherp onderscheid tussen mens en dier?", ["voor", "tegen"],
            [("Enkel mensen bouwen kunst, wetenschap en geschiedenis.", "voor"), ("Dieren communiceren met elkaar.", "tegen"), ("Dieren voelen pijn.", "tegen"), ("Dieren leren iets en geven het door.", "tegen")],
            "Waarnemingen bij dieren maken de kloof kleiner."),
    keuze("Wie het dier lager plaatst, vindt het makkelijker om [[*dierproeven en veeteelt te rechtvaardigen|dieren rechten te geven|de jacht te verbieden]].", "De tweedeling heeft gevolgen voor ons handelen."),
    inv("Welke theorie van Darwin maakt mens en dier verwant? Eén woord.", ["evolutietheorie", "evolutie", "de evolutietheorie"], "De evolutietheorie."),
    tabel("Klopt dit over Peter Singer?",
          [("Voor hem telt het lijden, niet de soort.", J), ("Hij leefde in de negentiende eeuw.", F), ("Hij werd in Australië geboren.", J), ("Hij vond dieren machines.", F)],
          "Singer is een hedendaagse filosoof."),
    keuze("'Een dier voelt niets, want het heeft geen geest.' Dat sluit aan bij [[*Descartes|Singer|Darwin]].", "Darwin en Singer zouden hem fel tegenspreken."),
    keuze("Aristoteles en Descartes komen ook terug bij het thema [[*lichaam en geest|de kunststromingen|de AUB-methode]].", "Hun antwoord daar bepaalt mee wat ze over dieren zeggen."),
    mk("Waarom is de vraag wat mens en dier onderscheidt filosofisch en niet enkel biologisch?",
       ["ze vraagt wat de verschillen betekenen", "omdat biologen nooit naar dieren kijken", "omdat ze in een boek van Darwin staat", "omdat je het antwoord kan opmeten"],
       0, "De biologie beschrijft, de filosofie vraagt naar betekenis."),
    sleep("Volgens de [[traditionele]] tweedeling staat de mens boven het dier. [[Darwin]] maakt het verschil een verschil in graad. [[Singer]] laat het lijden tellen.",
          ["Plato", "moderne"], "Twee visies die de traditie in vraag stellen."),
    inv("Welk vermogen is voor Singer de echte grens die telt? Eén woord.", ["lijden", "het lijden", "pijn"], "Wie kan lijden, heeft belangen."),
    keuze("Volgens de traditionele tweedeling gold een dier eerder als [[*bezit|rechthebbende|filosoof]].", "Omdat het lager stond dan de mens."),
    tabel("Past dit bij Darwin?",
          [("Hij is Engels.", J), ("Hij werkte in de negentiende eeuw.", J), ("Hij maakte het verschil gradueel.", J), ("Hij schreef over speciësisme.", F)],
          "Over speciësisme schreef Singer, een eeuw later."),
    sorteer("Aristoteles, Descartes, Darwin of Singer?", ["Aristoteles", "Descartes", "Darwin", "Singer"],
            [("een redelijk dier", "Aristoteles"), ("dieren als automaten", "Descartes"), ("een tak aan dezelfde boom", "Darwin"), ("lijden telt, niet de soort", "Singer")],
            "Vier visies op mens en dier."),
    keuze("Iemand zegt: 'Mensen kunnen meer van hetzelfde, niet iets totaal anders.' Hij ziet het verschil als [[*gradueel|absoluut|onbestaand]].", "Een verschil in graad."),
    tabel("Is dit een filosofische vraag bij het thema mens en dier?",
          [("Wat onderscheidt een mens van een dier?", J), ("Hoeveel kilo weegt een olifant?", F), ("Mag je een dier opeten?", J), ("Hoe oud wordt een kraai?", F)],
          "Weetvragen kan je opzoeken."),
    open_("Geef een argument volgens de AUB-methode bij de vraag: 'Mogen we dieren gebruiken voor proeven?'",
          "A: Mijn argument is dat dierproeven zo veel mogelijk vermeden moeten worden. U: want dieren kunnen lijden, en dat lijden weegt mee, zoals Singer zegt. Dat is belangrijk omdat de soort niet bepaalt of pijn telt. B: Stel je voor dat een medicijn ook zonder proef op een levend dier getest kan worden: dan kies je beter die weg."),
]

"""Kunst van de prehistorie tot de middeleeuwen — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_periodes: prehistorie, Egypte en het nabije
Oosten, de klassieke oudheid (Grieks en Romeins) en de middeleeuwen (romaans
en gotisch). Met vier zelfgetekende bouwwerken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
import math

from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, ROOD

BW = Prent("vier-bouwwerken", "Vier bouwwerken", "vier gebouwen naast elkaar, letters A tot D")
GROND = 520
BW.lijn(30, GROND, 970, GROND, DONKER, 3)
# A: piramide
BW.pad(f"M 50 {GROND} L 150 300 L 250 {GROND} Z", "#e8d9a8", DONKER, 3)
for k in range(1, 6):
    y = GROND - k * 37
    dx = (GROND - y) * 100 / 220
    BW.lijn(50 + dx, y, 250 - dx, y, "#b8a878", 2)
# B: Griekse tempel
BW.pad(f"M 280 270 L 380 220 L 480 270 Z", "#f2efe6", DONKER, 3)
BW.rect(280, 270, 200, 22, "#f2efe6", DONKER, 0, 3)
for k in range(5):
    BW.rect(292 + k * 38, 292, 18, 210, "#f2efe6", DONKER, 0, 2)
BW.rect(275, 502, 210, 18, "#f2efe6", DONKER, 0, 3)
# C: romaanse kerk: dikke muren, kleine rondboogvensters
BW.rect(520, 300, 190, 220, "#cfc6b0", DONKER, 0, 4)
BW.pad("M 520 300 L 615 240 L 710 300 Z", "#cfc6b0", DONKER, 4)
for x in (550, 650):
    BW.pad(f"M {x} 400 L {x} 370 A 12 12 0 0 1 {x + 24} 370 L {x + 24} 400 Z", "#3a3a3a", DONKER, 2)
BW.pad("M 590 520 L 590 460 A 25 25 0 0 1 640 460 L 640 520 Z", "#8a6a4a", DONKER, 3)
# D: gotische kathedraal: spitsbogen, groot glasraam, torens
BW.rect(750, 260, 200, 260, "#ddd6c4", DONKER, 0, 3)
BW.pad("M 750 260 L 770 150 L 790 260 Z", "#ddd6c4", DONKER, 3); BW.pad("M 910 260 L 930 150 L 950 260 Z", "#ddd6c4", DONKER, 3)
BW.cirkel(850, 320, 36, BLAUW, DONKER, 3)
for a in range(0, 360, 45):
    BW.lijn(850, 320, 850 + 36 * math.cos(math.radians(a)), 320 + 36 * math.sin(math.radians(a)), DONKER, 1)
BW.pad("M 775 470 L 775 400 Q 775 370 795 360 Q 815 370 815 400 L 815 470 Z", ROOD, DONKER, 2)
BW.pad("M 885 470 L 885 400 Q 885 370 905 360 Q 925 370 925 400 L 925 470 Z", GEEL, DONKER, 2)
BW.pad("M 825 520 L 825 450 Q 825 410 850 395 Q 875 410 875 450 L 875 520 Z", "#8a6a4a", DONKER, 3)
LET = {"A": (150, 560), "B": (380, 560), "C": (615, 560), "D": (850, 560)}
for t, (x, y) in LET.items():
    BW.letter(x, y, t)
U = "vier-bouwwerken.svg"
Z = {"A": [Prent.zone(40, 280, 220, 300)], "B": [Prent.zone(270, 210, 220, 370)], "C": [Prent.zone(510, 230, 210, 350)], "D": [Prent.zone(740, 140, 220, 440)]}

VRAGEN = [
    klik("Bekijk de vier bouwwerken. Klik op de romaanse kerk.", U, Z["C"], "Dikke muren, kleine vensters met rondbogen."),
    klik("Klik op het gotische bouwwerk.", U, Z["D"], "Spitsbogen, hoge torens en een groot glasraam."),
    klik("Klik op het bouwwerk dat diende als koningsgraf.", U, Z["A"], "De piramide: Egypte, gericht op het hiernamaals."),
    klik("Klik op het bouwwerk uit de klassieke oudheid.", U, Z["B"], "Een tempel met zuilen: Grieks."),
    volgorde("Zet de periodes in de juiste volgorde, van oud naar jong.",
             ["prehistorie", "Egypte en het nabije Oosten", "klassieke oudheid", "romaanse kunst", "gotiek"],
             "De periodes volgen de tijd."),
    sorteer("Romaans of gotisch?", ["romaans", "gotisch"],
            [("rondboog", "romaans"), ("spitsboog", "gotisch"), ("dikke muren", "romaans"), ("luchtbogen", "gotisch"), ("kleine vensters", "romaans"), ("grote glasramen", "gotisch")],
            "De spitsboog leidt de last naar de pijlers, zodat de muur open mag."),
    sorteer("Grieks of Romeins?", ["Grieks", "Romeins"],
            [("een ideaal atletenbeeld in marmer", "Grieks"), ("een portret van een oude man met rimpels", "Romeins"), ("een aquaduct", "Romeins"), ("vaasschilderkunst", "Grieks"), ("een koepel", "Romeins")],
            "Grieken idealiseerden, Romeinen portretteerden zoals iemand was."),
    mk("Waarom kon de gotiek veel grotere vensters maken dan de romaanse kunst?",
       ["de last ging via ribben en luchtbogen naar de pijlers", "glas was in de gotiek veel goedkoper dan gewone steen", "de gotische kerken waren veel lager en kleiner gebouwd", "men bouwde gotische kerken toen helemaal in hout"],
       0, "Dan hoeft de muur het gewicht niet te dragen."),
    tabel("Klopt dit over de prehistorie?",
          [("De bekendste schilderingen staan op grotwanden.", J), ("Mensen zijn er het vaakst afgebeeld.", F), ("Er zijn kleine beeldjes in steen en been bewaard.", J), ("Teksten leggen uit waarvoor grotkunst diende.", F)],
          "Dieren komen het vaakst voor; schrift bestond nog niet."),
    mk("Een Egyptische wandschildering toont een man met hoofd en benen van opzij en schouders van voren. Waarom?",
       ["elk deel staat van zijn meest kenbare kant", "de schilder kon nog geen perspectief tekenen", "de man draaide zich om tijdens het schilderen", "het is een fout die later is verbeterd"],
       0, "Een vast schema, volgens strakke regels."),
    keuze("De Egyptische beeldtaal bleef eeuwenlang gelijk, omdat [[*de regels bij godsdienst en macht hoorden|niemand iets nieuws kon bedenken|de kunstenaars geen verf hadden]].", "Vernieuwing was niet de bedoeling."),
    keuze("De Assyrische paleisreliëfs tonen vooral [[*de macht van de koning|het dagelijkse leven van boeren|het hiernamaals]].", "Jacht en veldslagen die de koning wint."),
    inv("Hoe noemt men de kleine prehistorische vrouwenfiguurtjes? Eén woord.", ["venusbeeldjes", "venusbeeldje", "venussen"], "Venusbeeldjes."),
    keuze("De romaanse bouwkunst dankt haar naam aan de [[*rondboog die van de Romeinen kwam|eerste bouwer Romanus|stad Rome waar ze ontstond]].", "De rondboog werd van de Romeinen overgenomen."),
    mk("Een heilige op een middeleeuws glasraam is veel groter dan de mensen rond hem. Waarom?",
       ["het verhaal en de rangorde wogen zwaarder", "de kunstenaars hadden toen nog geen goede verf", "men mocht toen geen mensen meer schilderen", "de kerken waren te donker om goed te zien"],
       0, "Belangrijke figuren werden groter getekend."),
    koppel("Koppel het werk aan de periode.",
           [("een stier op een grotwand", "prehistorie"), ("een sarcofaag met hiërogliefen", "Egypte"), ("een tempel met zuilen", "klassieke oudheid"), ("een kathedraal met spitsbogen", "gotiek")],
           ["popart"],
           "De periodes volgen de tijd."),
    tabel("Hoort het bij de Romeinse bouwkunst?",
          [("de rondboog", J), ("de koepel", J), ("het kruisribgewelf", F), ("de triomfboog", J)],
          "Het kruisribgewelf hoort bij de gotiek."),
    keuze("De hoogte en het gekleurde licht van een gotische kerk drukken [[*het streven naar de hemel|de macht van de koning|het hiernamaals van de farao]] uit.", "Hoogte en licht richten de gelovige naar boven."),
    mk("Je vindt een klein beeldje van been, duizenden jaren oud, zonder schrift erbij. Welke periode is het meest waarschijnlijk?",
       ["de prehistorie", "de gotiek", "de Romeinse tijd", "de Egyptische oudheid"],
       0, "Been, een kleine vorm en geen schrift wijzen op de prehistorie."),
    inv("Welk volk kopieerde veel Griekse beelden, zodat we ze nu nog kennen? Eén woord.", ["Romeinen", "romeinen", "de Romeinen"], "Veel Griekse werken kennen we door Romeinse kopieën."),
    keuze("Middeleeuwse kunst stond grotendeels in dienst van [[*de kerk|de handel|de wetenschap]].", "Kerken, glasramen en handschriften voor de eredienst."),
    sleep("De Griekse beeldhouwkunst zocht een [[ideale]] verhouding. De Romeinen maakten [[levensechte]] portretten. In de gotiek kwam de [[spitsboog]].",
          ["rondboog", "vlakke"], "Ideaal tegenover levensecht."),
    tabel("Klopt dit over de oude kunst?",
          [("De gotiek komt na de romaanse kunst.", J), ("Prehistorische kunst is jonger dan de Egyptische.", F), ("Egyptische kunst diende vaak voor het graf.", J), ("De kunst van het nabije Oosten staat los van Egypte.", F)],
          "Egypte en het nabije Oosten vormen samen één onderdeel."),
    mk("Een Egyptisch beeldje van een dienaar werd in een graf gelegd. Wat zegt dat over de Egyptische kunst?",
       ["ze diende een doel: de dode helpen", "ze werd gemaakt om in een museum te hangen", "ze werd vooral voor de handel met andere volken gemaakt", "ze was enkel bedoeld om er mooi uit te zien"],
       0, "Schoonheid alleen was niet de bedoeling."),
    keuze("Een kerk met luchtbogen en steunberen brengt je thuis bij [[*de gotiek|de romaanse kunst|de klassieke oudheid]].", "Luchtbogen zijn typisch gotisch."),
    sorteer("Welke periode?", ["prehistorie", "Egypte en nabije Oosten", "klassieke oudheid", "middeleeuwen"],
            [("rotskunst in Lascaux", "prehistorie"), ("een zegel in steen uit Mesopotamië", "Egypte en nabije Oosten"), ("een marmeren godin met ideale verhoudingen", "klassieke oudheid"), ("een glasraam met heiligen", "middeleeuwen")],
            "Materiaal, onderwerp en stijl verraden de periode."),
    open_("Je staat voor een oude kerk. Hoe beslis je of ze romaans of gotisch is? Noem twee kenmerken die je bekijkt.",
          "Ik kijk naar de bogen: rondbogen wijzen op romaans, spitsbogen op gotisch. En ik kijk naar de muren en vensters: dikke muren met kleine vensters zijn romaans, hoge muren met grote glasramen en luchtbogen zijn gotisch."),
    keuze("De bekendste prehistorische schilderingen beelden vooral [[*dieren|mensen|gebouwen]] af.", "Stieren, paarden, herten en bizons."),
    inv("Welke boogvorm hoort bij de gotiek? Eén woord.", ["spitsboog", "de spitsboog", "spitsbogen"], "De spitsboog draagt hoger."),
    keuze("Over de bedoeling van grotkunst kan men enkel redeneren, omdat [[*er toen nog geen schrift bestond|de grotten nu gesloten zijn|de schilderingen verdwenen zijn]].", "Geen teksten om te lezen."),
]

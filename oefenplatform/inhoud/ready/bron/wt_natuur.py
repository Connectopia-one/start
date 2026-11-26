# -*- coding: utf-8 -*-
"""Ready wetenschap en techniek: Natuur en milieu (seizoenen, dag en nacht, het weer
meten, de waterkringloop, afval sorteren, zorg voor de natuur)."""
from vr import mk, inv, wn

TITEL = "Natuur en milieu"
UITLEG_1 = "Seizoenen, dag en nacht, en het weer."
UITLEG_2 = "Afval sorteren en zorgen voor de natuur."

DEEL_1 = [
    mk("Welk seizoen komt na de winter?", ["de lente", "de zomer", "de herfst", "de winter"], 0, "Winter, lente, zomer, herfst."),
    inv("Een jaar heeft ___ seizoenen.", "4", "Lente, zomer, herfst en winter.", 4),
    mk("In welk seizoen vallen de bladeren van de bomen?", ["de lente", "de zomer", "de herfst", "de winter"], 2, "In de herfst kleuren de bladeren en vallen ze af."),
    wn("In de zomer zijn de dagen langer dan in de winter.", True, "In de zomer is het 's avonds lang licht."),
    mk("Waarom wordt het nacht?", ["De aarde draait rond zichzelf.", "De zon gaat slapen.", "De maan duwt de zon weg.", "De wolken worden zwart."], 0, "De kant van de aarde die van de zon wegdraait, krijgt nacht."),
    wn("De zon draait rond de aarde.", False, "Het is omgekeerd: de aarde draait rond de zon. Dat duurt een jaar."),
    mk("Waarmee meet je hoe warm het buiten is?", ["een thermometer", "een liniaal", "een weegschaal", "een klok"], 0, "Een thermometer meet de temperatuur."),
    mk("Waarmee meet je hoeveel regen er gevallen is?", ["een regenmeter", "een thermometer", "een kompas", "een windzak"], 0, "In een regenmeter lees je af hoeveel water erin gevallen is."),
    wn("Een windvaan toont uit welke richting de wind waait.", True, "De pijl van de windvaan draait mee met de wind."),
    mk("Waar komt regen vandaan?", ["uit de wolken", "uit de zee rechtstreeks", "uit de bomen", "uit de grond"], 0, "Waterdruppeltjes in de wolken worden groter en vallen naar beneden."),
    inv("Water uit de zee verdampt, wordt een wolk en valt als regen terug. Dat noem je de water___. (k...)", ["kringloop"], "Het water gaat altijd rond: verdampen, wolk, regen, rivier, zee."),
    wn("Sneeuw is bevroren water.", True, "Als het heel koud is in de wolk, vallen er sneeuwvlokjes in plaats van regen."),
    mk("Wat zie je vaak na een regenbui als de zon schijnt?", ["een regenboog", "sneeuw", "hagel", "mist"], 0, "Zonlicht door regendruppels geeft een regenboog."),
    wn("Bij onweer schuil je best onder een hoge boom.", False, "Bliksem slaat vaak in hoge dingen. Ga liever binnen schuilen."),
    mk("In welk seizoen bloeien veel bloemen en komen jonge dieren?", ["de lente", "de herfst", "de winter", "geen enkel seizoen"], 0, "In de lente wordt het warmer en groeit alles weer."),
    inv("De maan draait rond de ___.", ["aarde"], "De maan draait in ongeveer een maand rond de aarde."),
    wn("In België is het in juli meestal warmer dan in januari.", True, "Juli is zomer, januari is winter."),
    mk("Hoe heet het weerbericht dat zegt wat voor weer het morgen wordt?", ["de weersverwachting", "het nieuws over sport", "het verkeersbericht", "de reclame"], 0, "De weerman of weervrouw vertelt de weersverwachting."),
    wn("Mist is een wolk dicht bij de grond.", True, "In mist zweven heel veel kleine waterdruppeltjes laag bij de grond."),
    wn("De zon is een planeet.", False, "De zon is een ster. De aarde is een planeet."),
]

DEEL_2 = [
    mk("Waar gooi je een lege plastic fles in Vlaanderen?", ["in de blauwe zak (pmd)", "bij het gft", "in de glasbak", "in de vuilniszak voor restafval"], 0, "Plastic flessen, metalen blikjes en drankkartons gaan bij het pmd."),
    mk("Waar gaat een bananenschil naartoe?", ["bij het gft", "in de glasbak bij de flessen", "bij het oud papier", "bij het pmd"], 0, "Groente-, fruit- en tuinafval kan je composteren."),
    wn("Oud papier en karton kan je recycleren.", True, "Van oud papier maakt men nieuw papier."),
    inv("Een glazen bokaal gaat in de ___bak.", ["glas", "glasbak"], "Glas breng je naar de glasbak."),
    mk("Wat betekent recycleren?", ["Van oud materiaal iets nieuws maken.", "Alles weggooien in de natuur.", "Iets heel snel kapotmaken.", "Iets heel lang bewaren in de kast op zolder."], 0, "Van oude flessen maakt men bijvoorbeeld nieuwe flessen of fleecetruien."),
    wn("Zwerfvuil in de natuur is gevaarlijk voor dieren.", True, "Dieren kunnen erin vast raken of het opeten."),
    mk("Hoe kan je water besparen?", ["De kraan dichtdraaien tijdens het poetsen.", "Elke avond een uur lang in bad liggen.", "De kraan laten lopen.", "De tuin elke middag sproeien met de tuinslang."], 0, "Zo stroomt er geen water nutteloos weg."),
    wn("Met de fiets naar school gaan is beter voor het milieu dan met de auto.", True, "Een fiets maakt geen uitlaatgassen."),
    mk("Wat kan je doen in plaats van iets weg te gooien?", ["het herstellen of doorgeven", "het verbranden in de tuin", "het in de beek gooien", "het ergens diep in het bos achterlaten"], 0, "Herstellen, hergebruiken of doorgeven zorgt voor minder afval."),
    wn("Een boterhamdoos gebruiken is beter dan elke dag aluminiumfolie.", True, "Een doos gebruik je elke dag opnieuw. Folie wordt afval."),
    mk("Waarom zijn bijen belangrijk?", ["Ze helpen bloemen om vruchten te maken.", "Ze maken een gezellig zoemend lawaai.", "Ze eten al het afval op.", "Ze maken het water in de vijver schoon."], 0, "Zonder bijen zouden er veel minder appels, peren en aardbeien zijn."),
    inv("Een plek waar dieren en planten beschermd worden, heet een natuur___. (g...)", ["gebied", "natuurgebied", "reservaat", "natuurreservaat"], "In een natuurgebied laat je alles zoals het is."),
    wn("In een natuurgebied mag je bloemen plukken zoveel je wil.", False, "In een natuurgebied laat je planten en dieren met rust."),
    mk("Wat is een insectenhotel?", ["een schuilplaats voor insecten", "een duur hotel voor mensen op reis", "een zwembad voor vissen", "een kooi voor vogels"], 0, "Bijen en lieveheersbeestjes vinden er een veilig plekje."),
    wn("Lege batterijen gooi je bij het gft.", False, "Batterijen breng je naar een inzamelpunt. Ze bevatten stoffen die slecht zijn voor de natuur."),
    mk("Wat doe je met een goede jas die te klein is?", ["Je geeft hem door.", "Je gooit hem in de natuur.", "Je verbrandt hem.", "Je stopt hem in de glasbak."], 0, "Kleren die je niet meer past, kan je doorgeven of naar de kringwinkel brengen."),
    inv("Een winkel waar je tweedehands spullen koopt, heet een ___winkel. (k...)", ["kring", "kringwinkel"], "In de kringwinkel krijgen spullen een tweede leven."),
    wn("Het licht laten branden als niemand in de kamer is, verspilt energie.", True, "Doe het licht uit als je weggaat."),
    mk("Welke bak is voor groenten- en fruitresten?", ["de gft-bak", "de glasbak", "de pmd-zak", "de papierbak"], 0, "Gft staat voor groente-, fruit- en tuinafval."),
    wn("Een drankkarton hoort bij het restafval.", False, "Drankkartons gaan in de blauwe pmd-zak."),
]


# Prentvragen (vraag 21 tot 24), Kim 26/11.
from vr import mk, inv, wn
import prent as P
PRENT_1 = [
    mk("Welk seizoen zie je op de prent?", ["de herfst", "de lente", "de zomer", "de winter"], 0, "De blaadjes worden oranje en vallen af: het is herfst.", prent=P.p_seizoenboom("natuur-herfst", "herfst")),
    inv("Welk seizoen zie je op de prent? De ...", ["winter", "de winter"], "Kale takken en sneeuw: het is winter.", prent=P.p_seizoenboom("natuur-winter", "winter")),
    wn("Op de prent is het herfst.", False, "De boom krijgt bloesems: het is lente.", prent=P.p_seizoenboom("natuur-lente", "lente")),
    mk("Welk weer toont het weerbericht?", ["regen", "zon", "sneeuw", "mist"], 0, "Uit de wolk vallen druppels: het regent.", prent=P.p_weer("natuur-regen", "regen")),
]
PRENT_2 = [
    mk("In de blauwe PMD-zak gooi je ...", ["een leeg blikje", "een bananenschil", "een krant", "een kapotte tas"], 0, "PMD is plastic flessen, metalen blikjes en drankkartons.", prent=P.p_afvalbak("natuur-pmd", "pmd")),
    inv("Wat gooi je bij het groente-, fruit- en tuinafval? Schrijf de letter.", ["C"], "C is een bananenschil: dat is fruitafval (gft).", prent=P.p_eten("natuur-afval-kiezen", ["blikje", "chips", "banaan", "lolly"])),
    wn("In de groene gft-bak gooi je lege flessen.", False, "In de gft-bak gaat enkel groente-, fruit- en tuinafval.", prent=P.p_afvalbak("natuur-gft", "gft")),
    inv("Van groente-, fruit- en tuinafval maakt men c... (goede aarde voor de tuin)", ["compost"], "Gft wordt compost: voeding voor planten.", prent=P.p_afvalbak("natuur-gft-2", "gft")),
]

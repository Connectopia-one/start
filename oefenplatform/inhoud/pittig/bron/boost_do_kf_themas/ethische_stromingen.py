"""De ethische stromingen en hun filosofen — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_ethische_stromingen: gevolgenethiek en
plichtethiek, en Kant, Bentham, Mill en Singer in tijd en ruimte. Met een
zelfgetekende tijdlijn en twee zinnebeelden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ROOD, LICHTGROEN

ET = Prent("tijdlijn-ethiek", "Een tijdlijn en twee zinnebeelden", "een tijdlijn van 1600 tot 2050 met letters A tot D en twee tekeningen E en F")
ET.lijn(80, 150, 920, 150, DONKER, 4)
def X(j):
    return 80 + (j - 1600) / 450 * 840
for j in (1600, 1700, 1800, 1900, 2000):
    ET.lijn(X(j), 140, X(j), 160, DONKER, 2); ET.tekst(X(j), 190, str(j), 18)
PT = {"A": 1640, "B": 1760, "C": 1855, "D": 1995}
for t, j in PT.items():
    ET.cirkel(X(j), 150, 9, ROOD, DONKER, 2); ET.letter(X(j), 100, t)
# E: een bord met een uitroepteken: een regel die altijd geldt
ET.lijn(300, 446, 300, 580, DONKER, 6)
ET.pad("M 300 260 L 400 440 L 200 440 Z", "#ffffff", ROOD, 10)
ET.tekst(300, 425, "!", 110, kleur=DONKER, vet=True)
ET.letter(420, 560, "E")
# F: een weegschaal die lachende en droeve gezichtjes afweegt
ET.lijn(700, 270, 700, 560, DONKER, 5); ET.lijn(600, 300, 800, 330, DONKER, 5); ET.rect(660, 555, 80, 12, GRIJS, DONKER, 3)
for cx, cy in ((600, 300), (800, 330)):
    ET.lijn(cx, cy, cx - 35, cy + 70, DONKER, 2); ET.lijn(cx, cy, cx + 35, cy + 70, DONKER, 2)
    ET.pad(f"M {cx-42} {cy+70} Q {cx} {cy+95} {cx+42} {cy+70} Z", GEEL, DONKER, 2)
def gezicht(x, y, blij):
    ET.cirkel(x, y, 13, "#ffffff", DONKER, 2); ET.cirkel(x - 5, y - 3, 2, DONKER, DONKER, 1); ET.cirkel(x + 5, y - 3, 2, DONKER, DONKER, 1)
    ET.pad(f"M {x-6} {y+4} Q {x} {y+(11 if blij else -3)} {x+6} {y+4}", "none", DONKER, 2)
gezicht(585, 356, False); gezicht(613, 356, False)
for dx in (-25, 0, 25):
    gezicht(800 + dx, 386, True)
gezicht(800, 360, True)
ET.letter(820, 560, "F")
U = "tijdlijn-ethiek.svg"
Z = {t: [Prent.rond(X(j), 125, 40)] for t, j in PT.items()}
Z["E"] = [Prent.zone(190, 250, 240, 340)]
Z["F"] = [Prent.zone(550, 260, 300, 330)]

HUIS = ("Lees het voorval.\n\n"
        "Tijdens een oorlog verbergt Anna een vluchteling op haar zolder. Soldaten bellen aan en vragen of er iemand verstopt zit. "
        "Anna weet: als ze de waarheid zegt, wordt de vluchteling opgepakt.")

VRAGEN = [
    klik("Bekijk de tijdlijn. Klik op de letter bij de tijd waarin Kant leefde.", U, Z["B"], "Koningsbergen, achttiende eeuw."),
    klik("Klik op de letter bij de tijd waarin John Stuart Mill werkte.", U, Z["C"], "Engeland, negentiende eeuw."),
    klik("Klik op de letter bij de tijd waarin Peter Singer schrijft.", U, Z["D"], "Een hedendaagse filosoof."),
    klik("Klik op het zinnebeeld dat het best past bij de plichtethiek.", U, Z["E"], "Een regel die onvoorwaardelijk geldt."),
    klik("Klik op het zinnebeeld dat het best past bij de gevolgenethiek.", U, Z["F"], "Je weegt af welke keuze het meeste welzijn geeft."),
    casus(HUIS, [
        sorteer("Welke stroming hoort bij deze redenering?", ["gevolgenethiek", "plichtethiek"],
                [("Anna liegt, want zo wordt een leven gered.", "gevolgenethiek"), ("Anna mag niet liegen, want liegen is in zichzelf fout.", "plichtethiek")],
                "Bij een leugen om bestwil lopen de stromingen uiteen."),
        mk("Welk bezwaar tegen de plichtethiek toont dit voorval?",
           ["ze kan hardvochtig zijn", "ze kan de gevolgen van een daad nooit goed voorspellen", "ze laat een minderheid altijd inschieten bij een meerderheid", "ze kan elk middel goedpraten zolang het resultaat goed is"],
           0, "Wie nooit mag liegen, moet de vluchteling verraden."),
        keuze("De filosoof die zegt dat Anna nooit mag liegen, is [[*Kant|Bentham|Mill]].", "Een morele wet geldt bij hem onvoorwaardelijk."),
        keuze("Een gevolgenethicus moet hier wel inschatten wat er zal gebeuren. Een bezwaar tegen zijn stroming is dat gevolgen [[*niet altijd te voorspellen zijn|altijd vastliggen|niet belangrijk zijn]].", "Anna weet niet zeker wat de soldaten doen."),
    ]),
    koppel("Koppel de filosoof aan zijn stroming of idee.",
           [("Kant", "een regel die voor iedereen moet kunnen gelden"), ("Bentham", "het grootste geluk voor het grootste aantal"), ("Mill", "geluk heeft ook kwaliteit"), ("Singer", "wie het meeste leed voorkomt, handelt goed")],
           ["de ziel is de vorm van het lichaam"], "Drie gevolgenethici en één plichtethicus."),
    sorteer("Gevolgenethiek of plichtethiek?", ["gevolgenethiek", "plichtethiek"],
            [("Een regering kiest de maatregel die de meeste mensen helpt.", "gevolgenethiek"), ("Hij houdt zijn belofte, ook al kost het hem veel.", "plichtethiek"), ("Een arts zegt de harde waarheid, ook als het pijn doet.", "plichtethiek"), ("Je geeft geld zolang het meer leed voorkomt dan het jou kost.", "gevolgenethiek")],
            "Kijk of de uitkomst of de regel beslist."),
    tabel("Klopt dit over de ethische stromingen?",
          [("Kant en Bentham horen tot dezelfde stroming.", F), ("Bentham en Mill zijn allebei Engels.", J), ("Volgens Kant mag je een mens nooit louter als middel gebruiken.", J), ("Volgens de gevolgenethiek telt enkel de bedoeling.", F)],
          "Bij de gevolgenethiek telt de uitkomst."),
    mk("Welke vraag stelt Kant om te toetsen of een daad mag?",
       ["kan iedereen zo handelen?", "welke keuze geeft het meeste geluk aan de meeste mensen?", "welk gevolg heeft mijn daad voor mijzelf op lange termijn?", "wat zou de meerderheid van mijn vrienden er zelf van vinden?"],
       0, "Kan je willen dat jouw regel een wet voor iedereen wordt?"),
    volgorde("Zet deze filosofen in de volgorde waarin ze leefden of werkten.",
             ["Kant", "Mill", "Singer"],
             "Achttiende eeuw, negentiende eeuw, vandaag."),
    keuze("Het woord utilitarisme komt van het Latijnse utilis, dat [[*nuttig|plicht|geluk]] betekent.", "Een andere naam voor de gevolgenethiek."),
    tabel("Is dit een bezwaar tegen de gevolgenethiek?",
          [("Gevolgen zijn niet altijd te voorspellen.", J), ("Een minderheid kan erbij inschieten.", J), ("Ze kan elk middel goedpraten.", J), ("Ze laat nooit een uitzondering toe.", F)],
          "Geen uitzondering toelaten is net een bezwaar tegen de plichtethiek."),
    mk("Waarom halen mensen in de praktijk vaak beide stromingen erbij?",
       ["elk antwoord heeft zijn grens", "omdat de twee stromingen eigenlijk precies hetzelfde zeggen", "omdat Kant en Bentham samen één boek schreven", "omdat je zo nooit meer een keuze hoeft te maken"],
       0, "Enkel regels wordt hard, enkel gevolgen praat alles goed."),
    keuze("'Je mag nooit martelen, ook niet om tien mensen te redden.' Dat sluit aan bij [[*Kant|Bentham|Singer]].", "De regel geldt onvoorwaardelijk."),
    sleep("De [[plichtethiek]] kijkt naar de regel zelf. De [[gevolgenethiek]] kijkt naar het resultaat. Men noemt die laatste ook het [[utilitarisme]].",
          ["monisme", "dualisme"], "Twee stromingen."),
    tabel("Past dit bij Mill?",
          [("Hij bouwt voort op Bentham.", J), ("Voor hem weegt niet elk genot even zwaar.", J), ("Hij is een plichtethicus.", F), ("Hij werkte in Duitsland.", F)],
          "Mill is een Engelse gevolgenethicus."),
    inv("Welke filosoof uit dit thema komt ook terug bij mens en dier? Eén naam.", ["Singer", "Peter Singer", "singer"], "Bij hem telt ook dierenleed mee."),
    keuze("In een discussie praten twee mensen langs elkaar: de een let op de regel, de ander op het gevolg. Het onderscheid tussen de stromingen helpt je te zien [[*waarop iemand zich baseert|wie gelijk heeft|wie het luidst praat]].", "Daarom is het bruikbaar."),
    mk("Een bedrijf zegt: 'We liegen niet in onze reclame, ook al zou een leugen meer verkopen.' Welke stroming?",
       ["plichtethiek", "gevolgenethiek, want het bedrijf wil zoveel mogelijk verkopen", "utilitarisme, want het grootste geluk telt voor iedereen", "geen van beide, want reclame heeft niets met ethiek te maken"],
       0, "De regel gaat voor het resultaat."),
    tabel("Klopt dit over de vier filosofen?",
          [("Singer leeft vandaag nog.", J), ("Kant werkte in Koningsbergen.", J), ("De vier leefden in dezelfde eeuw.", F)],
          "Achttiende eeuw tot vandaag."),
    keuze("Jeremy Bentham leefde [[*in Engeland rond 1800|in Duitsland in de zeventiende eeuw|in Australië vandaag]].", "Mill kende zijn werk van jongs af."),
    tabel("Hoort deze filosoof bij de gevolgenethiek?",
          [("Bentham", J), ("Mill", J), ("Singer", J), ("Kant", F)],
          "Kant is juist de tegenpool."),
    keuze("Volgens Kant is een mens altijd ook een [[*doel in zichzelf|middel voor anderen|deel van de natuur]].", "Je mag een mens nooit louter als middel gebruiken."),
    mk("Een leerling schrijft het antwoord van een vriend over, zodat die vriend geen straf krijgt. Waarom keurt een plichtethicus dat af?",
       ["bedriegen is in zichzelf fout", "omdat de vriend er later toch nog straf voor kan krijgen", "omdat het voor de meeste mensen in de klas slecht afloopt", "omdat de leerkracht het toch vroeg of laat zal ontdekken"],
       0, "De daad zelf telt, niet de uitkomst."),
    inv("Welke andere naam heeft de plichtethiek? Eén woord.", ["deontologie", "deontologische ethiek", "de deontologie"], "Van het Griekse woord voor plicht."),
    open_("Bedenk zelf een situatie waarin de gevolgenethiek en de plichtethiek een ander antwoord geven. Leg uit.",
          "Bijvoorbeeld: je vriend vraagt of je zijn tekening mooi vindt, maar je vindt ze lelijk. Een plichtethicus zegt dat je eerlijk moet zijn, want liegen is fout. Een gevolgenethicus kijkt naar wat je vriend het meest helpt en kan een leugentje om bestwil goedkeuren."),
]

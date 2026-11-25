"""Welzijn en welbevinden — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_welbevinden: welzijn, de vier soorten welbevinden, de
geluksdriehoek, de drie dimensies van gezondheid, hefbomen en drempels, en de
drie soorten zorg. Met een zelfgetekende geluksdriehoek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, GEEL

GD = Prent("geluksdriehoek", "Drie hoeken van een driehoek", "een driehoek met in elke hoek een voorbeeld, letters A tot C")
GD.pad("M 500 175 L 190 520 L 810 520 Z", LICHTGROEN, DONKER, 4)
HOEK = {"A": (500, 135, ["Je vrienden staan klaar", "als het even tegenzit."]),
        "B": (190, 545, ["Je slaapt goed en voelt", "je fit en rustig."]),
        "C": (810, 545, ["Je durft te zeggen wat", "je denkt, zonder masker."])}
Z = {}
for t, (x, y, regels) in HOEK.items():
    bx, by = x - 150, y - 45
    GD.rect(bx, by, 300, 90, "#ffffff", DONKER, 12, 2)
    GD.tekst(x + 10, by + 38, regels[0], 19); GD.tekst(x + 10, by + 64, regels[1], 19)
    GD.letter(bx + 2, by + 2, t)
    Z[t] = [Prent.zone(bx - 20, by - 20, 320, 110)]
U = "geluksdriehoek.svg"

SITUATIE = ("Lees de situatie.\n\n"
            "Mira (16) woont met haar mama in een klein appartement aan een drukke straat. Geld is er niet veel, maar ze heeft een hechte vriendengroep. "
            "Sinds ze leiding geeft bij de jeugdbeweging, voelt ze dat ze ertoe doet. Door het verkeer slaapt ze wel slecht.")

VRAGEN = [
    klik("Bekijk de driehoek. Klik op het voorbeeld bij de bouwsteen goed omringd zijn.", U, Z["A"], "Goed omringd zijn gaat over mensen om je heen en steun."),
    klik("Klik op het voorbeeld bij de bouwsteen jezelf kunnen zijn.", U, Z["C"], "Je hoeft je niet te verstoppen voor de mensen om je heen."),
    klik("Klik op het voorbeeld bij de bouwsteen je goed voelen.", U, Z["B"], "Je goed voelen gaat over hoe je je lichamelijk en in je hoofd voelt."),
    sorteer("Materiële of immateriële tevredenheid?", ["materieel", "immaterieel"],
            [("een vast inkomen", "materieel"), ("een warme vriendschap", "immaterieel"), ("een fiets om naar school te gaan", "materieel"), ("erkenning op je werk", "immaterieel"), ("een hobby die je zin geeft", "immaterieel"), ("een verwarmde woning", "materieel")],
            "Materieel is wat je hebt, immaterieel is wat je voelt en beleeft."),
    sorteer("Welk soort welbevinden?", ["fysiek", "psychisch", "sociaal", "existentieel"],
            [("Na een goede nachtrust heb je nergens pijn.", "fysiek"), ("Je voelt je rustig en zeker van jezelf.", "psychisch"), ("Je hoort erbij in je volleybalploeg.", "sociaal"), ("Je vrijwilligerswerk geeft je leven betekenis.", "existentieel"), ("Je hoofdpijn is eindelijk weg.", "fysiek"), ("Je hebt vrienden bij wie je terechtkunt.", "sociaal")],
            "Lichaam, gevoel, relaties en zin."),
    casus(SITUATIE, [
        keuze("Het kleine appartement en het weinige geld gaan over [[*materiële|immateriële]] tevredenheid.", "Het gaat over wat Mira en haar mama hebben."),
        keuze("Dat ze bij de jeugdbeweging voelt dat ze ertoe doet, hoort bij [[*existentieel|fysiek|financieel]] welbevinden.", "Het gaat over zin en betekenis."),
        keuze("Het slechte slapen raakt vooral haar [[*fysiek|existentieel|sociaal]] welbevinden.", "Uitgerust zijn gaat over je lichaam."),
        keuze("Haar hechte vriendengroep is een sterkte voor de bouwsteen [[*goed omringd zijn|jezelf kunnen zijn|je goed voelen]].", "Mensen om je heen om op terug te vallen."),
        mk("Welke hefboom zou Mira's slaap het meest helpen?",
           ["een slaapkamer aan de rustige achterkant", "meer zakgeld om meer te kunnen kopen", "nog meer uren leiding geven bij de jeugdbeweging", "een tweede vriendengroep op een andere school"],
           0, "Een hefboom maakt het gezonde makkelijker; hier is het lawaai de drempel."),
    ]),
    tabel("Hefboom of drempel voor een gezonde levensstijl?",
          [("een gratis waterfontein op school", "hefboom"), ("een frietkraam naast de schoolpoort", "drempel"), ("een veilige fietsstraat", "hefboom"), ("een sportclub die heel veel lidgeld vraagt", "drempel"), ("gratis fruit in de klas", "hefboom")],
          "Een hefboom maakt de gezonde keuze makkelijker, een drempel moeilijker.", ["hefboom", "drempel"]),
    sorteer("Zelfzorg, mantelzorg of professionele zorg?", ["zelfzorg", "mantelzorg", "professionele zorg"],
            [("Je smeert zonnecrème voor je gaat fietsen.", "zelfzorg"), ("Een buurvrouw doet elke week boodschappen voor een oudere man.", "mantelzorg"), ("Een thuisverpleegkundige verzorgt een wonde.", "professionele zorg"), ("Een zoon helpt zijn vader met wassen na een beroerte.", "mantelzorg"), ("Je gaat op tijd slapen voor een toets.", "zelfzorg"), ("Een kinesitherapeut oefent met een patiënt.", "professionele zorg")],
            "Een mantelzorger is een naaste, een professional heeft er een opleiding voor."),
    tabel("Welke dimensie van gezondheid raakt dit vooral?",
          [("een gebroken arm", "fysiek"), ("al weken somber zijn", "psychisch"), ("geen vrienden hebben op een nieuwe school", "sociaal"), ("een zware griep", "fysiek")],
          "Gezondheid heeft drie dimensies.", ["fysiek", "psychisch", "sociaal"]),
    mk("Waarom is 'niet ziek zijn' geen volledige omschrijving van gezondheid?",
       ["je kan je psychisch of sociaal slecht voelen zonder ziek te zijn", "omdat ziek zijn enkel telt als een arts het officieel vaststelt", "omdat gezondheid vooral gaat over hoeveel geld je hebt voor de dokter", "omdat iedereen eigenlijk altijd een beetje ziek is, ook als hij zich goed voelt"],
       0, "Gezondheid is volledig fysiek, psychisch en sociaal welbevinden."),
    tabel("Klopt dit over zorg?",
          [("Een mantelzorger kan ook een buur zijn.", J), ("Zelfzorg is enkel iets voor zieke mensen.", F), ("Professionele zorg komt van iemand met een opleiding in de zorg.", J), ("Mantelzorg is meestal betaald werk.", F)],
          "Zelfzorg doet iedereen, elke dag."),
    inv("Hoe noem je iets in je omgeving dat een gezonde keuze makkelijker maakt? Eén woord.", ["hefboom", "een hefboom"], "Een hefboom."),
    koppel("Koppel het soort welbevinden aan waar het over gaat.",
           [("fysiek", "je lichaam"), ("psychisch", "je gevoelens en gedachten"), ("sociaal", "je relaties"), ("existentieel", "zin en waarden")],
           ["je bankrekening"],
           "Geld is materiële tevredenheid, geen soort welbevinden."),
    mk("Een school wil het welbevinden verhogen. Welke actie past bij 'jezelf kunnen zijn'?",
       ["een klas waar je jezelf mag tonen zonder uitgelachen te worden", "een nieuwe drankautomaat met frisdrank en snoep in de grote refter", "strengere straffen voor wie te laat komt in de les", "een duurdere schooluitstap naar het buitenland"],
       0, "Jezelf kunnen zijn betekent dat je je niet moet verstoppen."),
    keuze("Een oudere dame woont alleen en krijgt nooit bezoek. Vooral haar [[*sociaal|fysiek|existentieel]] welbevinden staat onder druk.", "Het gaat over haar relaties en haar plaats bij anderen."),
    sleep("Welzijn bestaat uit [[materiële]] en [[immateriële]] tevredenheid. Welbevinden heeft [[vier]] soorten. De geluksdriehoek heeft [[drie]] bouwstenen.",
          ["financiële", "vijf"],
          "Fysiek, psychisch, sociaal en existentieel; omringd zijn, je goed voelen en jezelf zijn."),
    mk("Een papa zorgt elke dag voor zijn zieke dochter en raakt zelf uitgeput. Wat is dan belangrijk?",
       ["dat hij ook voor zichzelf zorgt", "dat hij nog meer uren zorg opneemt", "dat hij zijn eigen gezondheid opzijzet", "dat hij geen hulp vraagt aan anderen"],
       0, "Ook een mantelzorger heeft zelfzorg nodig, anders houdt hij het niet vol."),
    keuze("Een hoog loon maar geen enkele vriend: dan ontbreekt vooral [[*immateriële|materiële]] tevredenheid.", "Vriendschap heb je niet, die beleef je."),
    mk("Welke uitspraak past bij existentieel welbevinden?",
       ["Ik weet waarvoor ik 's ochtends opsta.", "Ik heb deze week geen enkele keer hoofdpijn gehad.", "Ik heb een grote groep vrienden op school.", "Ik verdien genoeg om mijn huur te betalen."],
       0, "Existentieel welbevinden gaat over zin en waarden."),
    tabel("Hoort dit bij de geluksdriehoek?",
          [("goed omringd zijn", J), ("veel geld verdienen", F), ("jezelf kunnen zijn", J), ("populair zijn op sociale media", F), ("je goed voelen", J)],
          "Geld en populariteit staan er niet in."),
    keuze("Gezonde voeding in de schoolkantine kost meer dan friet. Die prijs is een [[*drempel|hefboom]].", "Ze maakt de gezonde keuze moeilijker."),
    mk("Wie neemt hier mantelzorg op?",
       ["een kleinzoon die elke zondag voor zijn oma kookt", "een kinesist die per behandeling door de patiënt betaald wordt", "een apotheker die medicijnen meegeeft", "een poetshulp van een dienstenbedrijf"],
       0, "Een mantelzorger zorgt uit betrokkenheid, niet als beroep."),
    keuze("Psychisch welbevinden gaat over je [[*gevoelens en gedachten|spieren en botten|bezittingen]].", "Het lichaam hoort bij fysiek welbevinden."),
    mk("Een jongere met astma sport in een ploeg, heeft fijne vrienden en voelt zich goed. Wat klopt?",
       ["hij kan zich op veel vlakken gezond voelen", "hij is door zijn astma altijd ongezond", "astma hoort enkel bij het psychisch welbevinden", "hij moet stoppen met sporten om gezond te zijn"],
       0, "Gezondheid heeft drie dimensies; een aandoening op één ervan maakt je niet volledig ongezond."),
    inv("Hoe noem je zorg door iemand met een opleiding en een beroep in de zorg? Twee woorden.", ["professionele zorg", "de professionele zorg"], "Professionele zorg."),
    open_("Geef voor jezelf een hefboom en een drempel om meer te bewegen. Leg telkens uit waarom.",
          "Hefboom: mijn school ligt op een veilige fietsroute, dus fietsen gaat makkelijk. Drempel: de sportclub kost veel lidgeld, dus ik ga minder vaak sporten."),
]

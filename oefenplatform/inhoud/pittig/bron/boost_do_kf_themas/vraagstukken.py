"""Ethische vraagstukken analyseren — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_vraagstukken: botsende waarden benoemen,
argumenten bij de stromingen plaatsen, drogredenen herkennen en een argument
opbouwen met de AUB-methode, bij de vijf vraagstukken. Geen standpunt, enkel
analyse. Met een zelfgetekend discussieblad."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW

DB = Prent("discussieblad-dierproeven", "Een discussieblad over dierproeven", "vier tekstwolkjes met een argument, letters A tot D")
WOLK = [("A", 60, 80, ["Het leed van de dieren", "weegt zwaarder dan", "wat de proef oplevert."]),
        ("B", 520, 80, ["Een dier mag nooit", "louter een middel zijn,", "wat het ook opbrengt."]),
        ("C", 60, 350, ["Iedereen in mijn", "klas is ertegen,", "dus het is fout."]),
        ("D", 520, 350, ["Wie onderzoek doet,", "moet vrij kunnen kiezen", "hoe hij werkt."])]
for t, x, y, regels in WOLK:
    DB.rect(x, y, 420, 210, "#ffffff", DONKER, 30, 3)
    for i, r in enumerate(regels):
        DB.tekst(x + 200, y + 70 + i * 34, r, 23)
    DB.letter(x + 390, y + 180, t)
U = "discussieblad-dierproeven.svg"
Z = {t: [Prent.zone(x, y, 420, 210)] for t, x, y, r in WOLK}

CASUS = ("Lees het voorstel.\n\n"
         "Een gemeente wil een avondklok voor jongeren onder zestien jaar: na tien uur 's avonds mogen ze niet meer alleen op straat. "
         "Het stadsbestuur zegt dat het zo minder ongelukken en minder alcoholgebruik verwacht. "
         "Een jongerenvereniging zegt dat jongeren zelf moeten leren kiezen.")

VRAGEN = [
    klik("Bekijk het discussieblad. Klik op het argument dat bij de gevolgenethiek hoort.", U, Z["A"], "Leed wordt afgewogen tegen winst."),
    klik("Klik op het argument dat bij de plichtethiek hoort.", U, Z["B"], "De daad zelf is fout, los van de opbrengst."),
    klik("Klik op de drogreden.", U, Z["C"], "Dat veel mensen iets vinden, zegt niet dat het goed is."),
    klik("Klik op het argument dat de waarde vrijheid inroept tegen een verbod.", U, Z["D"], "Hier botst vrijheid met dierenwelzijn."),
    casus(CASUS, [
        keuze("Dit voorstel is een voorbeeld van het vraagstuk [[*risicogedrag bij jongeren|genderdiversiteit|anticonceptie]].", "Alcohol en ongelukken."),
        sorteer("Welke waarde roept deze partij in?", ["bescherming", "vrijheid"],
                [("het stadsbestuur", "bescherming"), ("de jongerenvereniging", "vrijheid")],
                "Bij risicogedrag botst de vrijheid van de jongere met zijn bescherming."),
        keuze("Het argument van het stadsbestuur rekent met de schade die je voorkomt. Het hoort dus bij de [[*gevolgenethiek|plichtethiek]].", "De verwachte uitkomst beslist."),
        mk("De jongerenvereniging noemt het voorstel paternalisme. Wat bedoelt ze?",
           ["beslissen voor iemands eigen bestwil", "een regel die enkel voor volwassenen geldt", "een voorstel dat van de ouders van de jongeren komt", "een maatregel die enkel in grote steden werkt"],
           0, "Het bezwaar: je neemt iemand zijn eigen keuze af."),
        tabel("Helpt deze vraag bij de analyse van het voorstel?",
              [("Wie draagt de schade?", J), ("Kunnen jongeren van vijftien de gevolgen overzien?", J), ("Welke waarden botsen hier?", J), ("Hoeveel kost een lantaarnpaal?", F)],
              "Drie vragen die de analyse richting geven."),
    ]),
    volgorde("Zet de stappen bij het analyseren van een ethisch vraagstuk in een logische volgorde.",
             ["de botsende waarden benoemen", "de argumenten van beide kanten zoeken", "je eigen argument opbouwen met de AUB-methode"],
             "Zolang je niet weet welke waarden botsen, weet je niet waarover het gaat."),
    koppel("Koppel het vraagstuk aan de waarden die er vaak botsen.",
           [("abortus", "zelfbeschikking tegenover bescherming van leven"), ("circusdieren", "dierenwelzijn tegenover vrij ondernemen"), ("een leeftijdsgrens voor anticonceptie", "bescherming tegenover zelfbeschikking"), ("risicogedrag", "vrijheid tegenover bescherming")],
           ["schoonheid tegenover nut"], "Bij elk vraagstuk botsen twee echte waarden."),
    tabel("Hoort dit begrip bij genderdiversiteit?",
          [("genderidentiteit", J), ("gendergelijkheid", J), ("genderongelijkheid", J), ("paternalisme", F)],
          "Paternalisme komt bij risicogedrag ter sprake."),
    keuze("Genderidentiteit gaat over [[*hoe iemand zichzelf ervaart|wat anderen over iemand denken|wat in de wet staat]].", "Niet over het oordeel van anderen."),
    keuze("De loonkloof tussen mannen en vrouwen is een voorbeeld van [[*genderongelijkheid|gendergelijkheid|genderidentiteit]].", "Ongelijke kansen door geslacht."),
    sorteer("Argument of drogreden?", ["argument", "drogreden"],
            [("Dat doet toch iedereen.", "drogreden"), ("Een verbod voorkomt meer schade dan het kost.", "argument"), ("De meeste mensen vinden het normaal.", "drogreden"), ("Een mens mag nooit louter een middel zijn.", "argument")],
            "Een argument verwijst naar een waarde of een stroming."),
    mk("Waarom zijn deze vraagstukken filosofisch en niet enkel juridisch?",
       ["ze vragen of de wet juist is", "omdat er voor deze vraagstukken nog helemaal geen wetten bestaan", "omdat rechters nooit over zulke onderwerpen moeten oordelen", "omdat filosofen de wetten in België schrijven"],
       0, "De wet zegt wat geldt, de ethiek vraagt wat zou moeten."),
    tabel("Klopt dit over het examen bij een ethisch vraagstuk?",
          [("Het beoordeelt de kwaliteit van je argument.", J), ("Je krijgt meer punten voor het juiste standpunt.", F), ("Een voorbeeld maakt je argument sterker.", J)],
          "Welk standpunt je verdedigt, is aan jou."),
    keuze("Een argument is sterker dan een mening omdat het [[*een reden geeft|luider klinkt|korter is]].", "Pas dan kan de ander erop ingaan."),
    mk("Waarom moet je ook de tegenargumenten kennen?",
       ["anders kan je ze niet weerleggen", "omdat je dan zeker van standpunt verandert", "omdat het examen enkel naar tegenargumenten vraagt", "omdat je eigen argument dan overbodig wordt"],
       0, "Een argument dat de bezwaren negeert, staat zwak."),
    inv("Hoe noem je een argument dat overtuigend klinkt maar niet geldig is? Eén woord.", ["drogreden", "een drogreden"], "Een drogreden."),
    sorteer("Hoort dit argument bij de gevolgenethiek of de plichtethiek?", ["gevolgenethiek", "plichtethiek"],
            [("Een leeftijdsgrens voorkomt meer schade dan ze kost.", "gevolgenethiek"), ("Je mag nooit ingrijpen in iemands lichaam zonder toestemming.", "plichtethiek"), ("Een verbod op circusdieren spaart veel leed.", "gevolgenethiek")],
            "Kijk of de uitkomst of de daad zelf beslist."),
    keuze("Een voorstel om anticonceptie te verplichten raakt aan de [[*lichamelijke zelfbeschikking|gendergelijkheid|dierenrechten]].", "Ingrijpen in iemands lichaam zonder toestemming."),
    tabel("Is dit een van de vijf ethische vraagstukken?",
          [("dierenrechten", J), ("abortus", J), ("anticonceptie", J), ("ruimtevaart", F), ("risicogedrag bij jongeren", J)],
          "Het vijfde is genderdiversiteit."),
    keuze("Verantwoordelijkheid weegt mee bij jongeren, want ze [[*groeit met het overzicht over de gevolgen|is bij iedereen even groot|verdwijnt na je zestiende]].", "Wie de gevolgen nog niet overziet, is minder verantwoordelijk."),
    sleep("Bij een vraagstuk benoem je eerst de botsende [[waarden]]. Daarna bouw je een [[argument]] op en maak je het concreet met een [[voorbeeld]].",
          ["drogreden", "mening"], "Zo blijft het een onderbouwde analyse."),
    mk("Welke vraag stel je het best als eerste bij een nieuw ethisch vraagstuk?",
       ["welke waarden botsen hier?", "wat vindt de meerderheid van de mensen in mijn omgeving?", "welk standpunt levert op het examen de meeste punten op?", "welke wet bestaat er vandaag al over dit onderwerp?"],
       0, "Eerst de botsende waarden benoemen."),
    tabel("Is dit een voorbeeld van risicogedrag bij jongeren?",
          [("alcoholgebruik", J), ("druggebruik", J), ("experimenteren met seks", J), ("huiswerk maken", F)],
          "Drie voorbeelden uit het vraagstuk."),
    keuze("Bij dierenrechten zijn een verbod op dierproeven en een verbod op [[*circusdieren|ruimtevaart|anticonceptie]] voorbeelden.", "Allebei over het welzijn van dieren."),
    keuze("Bij abortus is het debat [[*niet|wel]] met één argument beslecht, want beide kanten voeren zwaarwegende waarden aan.", "Daarom is het een vraagstuk."),
    open_("Analyseer het vraagstuk 'een verbod op circusdieren'. Noem de botsende waarden en geef een argument volgens de AUB-methode, voor of tegen.",
          "Er botsen dierenwelzijn en de vrijheid van wie met dieren werkt. Argument (voor een verbod): A: Mijn argument is dat een verbod nodig is. U: want wilde dieren lijden onder kleine kooien en veel reizen, en dat leed weegt zwaarder dan het plezier van het publiek. B: Stel je een olifant voor die maandenlang in een vrachtwagen van stad naar stad gaat."),
]

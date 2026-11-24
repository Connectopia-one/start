"""Presenteren en gegevens in een databank — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Pittige vragen over presenteren uit Samenleving en economie Beyond, aangevuld met
eigen vragen strikt binnen te_presenteren en een zelfgetekende tabel uit een
databank om record, veld en primaire sleutel aan te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS
from ..beyond_se_themas import powerpoint as _p

DB = Prent("databank-klanten", "Tabel Klanten", "tabel uit een databank met veldnamen bovenaan en vijf records, met letters A tot F")
KOL = [("Klantnr", 120), ("Naam", 190), ("Gemeente", 160), ("Postcode", 120), ("Geboortedatum", 170)]
X0, Y0, RH = 90, 110, 52
x = X0
for naam, b in KOL:
    DB.rect(x, Y0, b, RH, "#e8efe0", DONKER, 0, 1)
    DB.tekst(x + 10, Y0 + 33, naam, 17, "start", vet=True)
    x += b
RIJEN = [("1001", "Lien Aerts", "Hasselt", "3500", "12/03/1990"), ("1002", "Tom Claes", "Genk", "3600", "05/11/1985"),
         ("1003", "Sara Peeters", "Hasselt", "3500", "21/07/1979"), ("1004", "Tom Claes", "Bree", "3960", "30/01/1992"),
         ("1005", "Mo Jacobs", "Alken", "3570", "")]
for i, rij in enumerate(RIJEN):
    x = X0; y = Y0 + RH * (i + 1)
    for (naam, b), w in zip(KOL, rij):
        DB.rect(x, y, b, RH, "#fff5d6" if i == 2 else "#ffffff", DONKER, 0, 1)
        DB.tekst(x + 10, y + 33, w, 17, "start")
        x += b
RECHTS = X0 + sum(b for _, b in KOL)
LET = {"A": (X0 + 60, 75), "B": (RECHTS + 40, Y0 + RH * 3 + 26), "C": (X0 + 120 + 190 + 80, 75), "D": (X0 + 120 + 190 + 160 + 120 + 85, 75), "E": (X0 + 120 + 190 + 160 + 120 + 85, Y0 + RH * 6 + 40), "F": (X0 + 120 + 165, Y0 + RH * 6 + 40)}
for t, (lx, ly) in LET.items():
    DB.letter(lx, ly, t)
DB.pijl(LET["E"][0], LET["E"][1] - 22, LET["E"][0], Y0 + RH * 6 - 10, DONKER, 2)
DB.pijl(LET["F"][0], LET["F"][1] - 22, LET["F"][0], Y0 + RH * 4 + 44, DONKER, 2)
U = "databank-klanten.svg"
Z = {t: Prent.rond(lx, ly, 30) for t, (lx, ly) in LET.items()}

VRAGEN = [_p.VRAGEN[i] for i in (0, 5, 9, 10, 17, 27)] + [
    klik("Klik op de letter bij het veld dat elk record uniek maakt.", U, [Z["A"]],
         "Het klantnummer is de primaire sleutel: twee klanten kunnen dezelfde naam hebben, geen hetzelfde nummer."),
    klik("Klik op de letter bij één record.", U, [Z["B"]],
         "Een record is één rij: alles over één klant."),
    klik("Klik op de letter bij het veld waarop je filtert om enkel de klanten uit Hasselt te zien.", U, [Z["C"]],
         "Het veld Gemeente: de filter houdt enkel de records met Hasselt over."),
    klik("Klik op de letter bij het veld dat als gegevenstype datum moet krijgen.", U, [Z["D"]],
         "Met een datum kan je rekenen en sorteren, met tekst niet."),
    klik("Het veld Geboortedatum wordt verplicht. Klik op de letter bij het record dat dan niet bewaard kan worden.", U, [Z["E"]],
         "Bij Mo Jacobs is de geboortedatum leeg; een verplicht veld mag niet leeg zijn."),
    klik("Klik op de letter die aantoont waarom de naam geen goede primaire sleutel is.", U, [Z["F"]],
         "Er zijn twee klanten met de naam Tom Claes; hun klantnummer is wel verschillend."),
    casus("Bekijk de tabel Klanten.", [
        inv("Hoeveel records telt de tabel? Schrijf enkel het getal.", ["5"],
            "Vijf rijen, vijf klanten."),
        inv("Hoeveel velden telt de tabel? Schrijf enkel het getal.", ["5"],
            "Klantnr, Naam, Gemeente, Postcode en Geboortedatum."),
        inv("Een filter op Gemeente is Hasselt. Hoeveel records blijven zichtbaar? Schrijf enkel het getal.", ["2"],
            "Lien Aerts en Sara Peeters."),
    ]),
    tabel("Welk gegevenstype past bij het veld?",
          [("geboortedatum", "datum"), ("klantnaam", "tekst"), ("aantal bestelde stuks", "getal"), ("nieuwsbrief gewenst", "ja of nee")],
          "Het gegevenstype zegt wat er in een veld mag.",
          kolommen=["tekst", "getal", "datum", "ja of nee"]),
    tabel("Tabel, formulier, rapport of query?",
          [("een invulscherm om een nieuwe klant toe te voegen", "formulier"), ("een nette lijst met totalen om af te drukken", "rapport"), ("alle klanten opvragen die meer dan 500 euro kochten", "query"), ("de plaats waar de gegevens zelf zitten", "tabel")],
          "De gegevens zitten in tabellen; de rest kijkt ernaar.",
          kolommen=["tabel", "formulier", "rapport", "query"]),
    tabel("Is dit een veldeigenschap?",
          [("de veldlengte", J), ("een standaardwaarde", J), ("het veld is verplicht", J), ("het aantal records in de tabel", F)],
          "Eigenschappen horen bij een veld, niet bij de tabel."),
    mk("Een klant verhuist. Waarom is dat in een databank sneller aangepast dan in drie losse rekenbladen?",
       ["Het adres staat één keer en verandert overal mee.", "Een databank zoekt zelf op het internet het nieuwe adres op.", "In een rekenblad kan je een adres achteraf niet meer wijzigen.", "Een databank wist de oude klant en maakt een nieuwe aan."], 0,
       "De gegevens staan één keer, op één plaats."),
    keuze("Een selectiequery [[*haalt gegevens op zonder ze te wijzigen|wist de records die niet passen|verandert het gegevenstype]].",
          "Wat niet past, blijft gewoon in de tabel staan."),
    tabel("Klopt dit over presenteren?",
          [("Een overgang zit tussen twee dia's.", J), ("Een animatie werkt binnen één dia.", J), ("Het publiek ziet de notities bij een dia.", F), ("Een sjabloon geeft elke dia dezelfde kleuren en lettertypes.", J)],
          "De notities zijn je spiekblad; enkel jij ziet ze."),
    volgorde("Zet de stappen om een presentatie te maken in de juiste volgorde.",
             ["een storyboard schetsen", "een sjabloon kiezen", "de dia's invullen", "een proef geven met de diavoorstelling"],
             "Eerst plannen, dan opmaken, dan oefenen."),
    sorteer("Past dit bij het KISS-principe?", ["ja", "nee"],
            [("één idee per dia", "ja"), ("je hele tekst op de dia zetten", "nee"), ("grote letters met veel contrast", "ja"), ("op elke dia een andere animatie", "nee")],
            "Keep it short and simple: weinig tekst, grote letters, weinig beweging."),
    koppel("Welk hulpmiddel past bij welk doel?",
           [("ideeën rond één onderwerp ordenen", "mindmap"), ("cijfers en tekeningen in één beeld", "infographic"), ("vooraf per dia plannen wat erop komt", "storyboard"), ("de dia's op papier meegeven", "hand-out")], ["overgang"],
           "Elk hulpmiddel heeft zijn eigen nut."),
    mk("Waarom zet je de omzet van vier jaar beter in een grafiek op de dia dan in een tabel met getallen?",
       ["Het publiek ziet het verloop in één oogopslag.", "Een grafiek bevat altijd meer gegevens dan een tabel.", "Een tabel kan je niet invoegen in een presentatie.", "Een grafiek beweegt vanzelf zonder animatie."], 0,
       "Volgens het KISS-principe toon je een beeld, geen rij getallen."),
    sleep("Eén rij in een tabel van een databank is een [[record]]. Eén soort gegeven, zoals postcode, is een [[veld]].",
          ["query", "dia"], "Twee databankbegrippen."),
    tabel("Klopt dit over de primaire sleutel?",
          [("Twee records mogen dezelfde primaire sleutel hebben.", F), ("Een klantnummer is een goede primaire sleutel.", J), ("De databank weigert een record met een sleutel die al bestaat.", J)],
          "De primaire sleutel is in elk record anders."),
    keuze("Een filter toont [[*minder records|meer velden|een nieuwe tabel]]: enkel wat aan je voorwaarde voldoet.",
          "De andere records blijven bestaan, je ziet ze even niet."),
    tabel("Welke afdruk of weergave gebruik je?",
          [("De dia's vullen het hele scherm tijdens je uitleg.", "diavoorstelling"), ("Het publiek krijgt zes dia's per blad mee.", "hand-out"), ("Jij leest je steekwoorden terwijl je spreekt.", "notities"), ("De klas krijgt achteraf alle dia's op papier.", "hand-out")],
          "Elk heeft een ander publiek.",
          kolommen=["diavoorstelling", "hand-out", "notities"]),
    mk("Wat maakt een dia leesbaar tot achteraan in de zaal?",
       ["weinig tekst in grote letters met veel contrast", "een foto als achtergrond achter alle tekst", "zoveel mogelijk tekst zodat niemand nog iets mist", "kleine letters zodat alles op één dia past"], 0,
       "Een drukke achtergrond maakt de tekst juist moeilijker leesbaar."),
]

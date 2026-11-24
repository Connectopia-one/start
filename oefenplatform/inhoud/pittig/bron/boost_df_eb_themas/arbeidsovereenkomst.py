"""Aanwerving en de arbeidsovereenkomst — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_arbeidsovereenkomst, met een zelfgetekende
arbeidsovereenkomst om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER

AO = Prent("arbeidsovereenkomst-winkel", "", "vereenvoudigde arbeidsovereenkomst met zeven regels en letters A tot G")
AO.rect(70, 24, 860, 596, "#ffffff", DONKER, 14, 3)
AO.rect(70, 24, 860, 66, LICHTGROEN, DONKER, 14, 3)
AO.tekst(500, 67, "Arbeidsovereenkomst voor bedienden", 26, vet=True)
REGELS = [
    ("A", "Tussen de bv Groen & Fris, Alken, en mevrouw Sara Peeters, Hasselt."),
    ("B", "Mevrouw Peeters werkt als verkoopster in de winkel."),
    ("C", "De overeenkomst begint op 1 maart 2027."),
    ("D", "De overeenkomst eindigt op 31 augustus 2027."),
    ("E", "Ze werkt 19 uur per week, van woensdag tot vrijdag."),
    ("F", "Het brutoloon is 15,20 euro per uur, betaald op de laatste dag van de maand."),
    ("G", "Ze volgt de opdrachten van de winkelverantwoordelijke."),
]
Y0, DY = 145, 68
for i, (t, r) in enumerate(REGELS):
    y = Y0 + i * DY
    AO.letter(118, y - 7, t)
    AO.tekst(156, y, r, 20, "start")
U = "arbeidsovereenkomst-winkel.svg"
Z = {t: Prent.rond(118, Y0 + i * DY - 7, 30) for i, (t, _) in enumerate(REGELS)}

VRAGEN = [
    klik("Klik op de letter bij de regel die toont dat dit een overeenkomst van bepaalde duur is.", U, [Z["D"]],
         "Er staat een einddatum in: op 31 augustus 2027 stopt ze, zonder dat iemand moet opzeggen."),
    klik("Klik op de letter bij de regel die toont dat dit een deeltijdse overeenkomst is.", U, [Z["E"]],
         "19 uur per week is minder dan een volle werkweek."),
    klik("Klik op de letter bij de regel die het gezag van de werkgever toont.", U, [Z["G"]],
         "De werknemer volgt de opdrachten van de werkgever: dat onderscheidt haar van een zelfstandige."),
    klik("Klik op de letter bij de identiteit van de partijen.", U, [Z["A"]],
         "De werkgever en de werknemer worden met naam en adres vermeld."),
    klik("Klik op de letter bij de functie van de werknemer.", U, [Z["B"]],
         "Ze werkt als verkoopster."),
    casus("Bekijk de arbeidsovereenkomst van Sara Peeters.", [
        tabel("Klopt dit volgens de overeenkomst?",
              [("De overeenkomst moet schriftelijk zijn.", J), ("Sara is een arbeider.", F), ("Het loon wordt per uur uitgedrukt.", J), ("Sara moet zelf opzeggen om op 31 augustus te stoppen.", F)],
              "Een overeenkomst van bepaalde duur moet op papier staan en stopt vanzelf op de einddatum. Sara is bediende: het staat in de titel."),
        inv("Hoeveel verdient Sara bruto per week? Schrijf enkel het getal in euro.", ["288,8", "288,80", "288.8", "288.80"],
            "19 uur × 15,20 euro = 288,80 euro."),
        mk("Wanneer moet de werkgever de DIMONA-aangifte voor Sara doen?",
           ["ten laatste op 1 maart 2027", "na de eerste maand dat ze werkt", "op 31 augustus 2027", "pas als ze haar eerste loon krijgt"], 0,
           "Uiterlijk op het moment dat de werknemer begint, niet erna."),
    ]),
    tabel("Welke soort arbeidsovereenkomst is dit volgens de duur?",
          [("Een contract zonder einddatum.", "onbepaalde duur"), ("Een contract van 1 juli tot 31 augustus.", "bepaalde duur"), ("Een contract tot de nieuwe keuken in het restaurant af is.", "duidelijk omschreven werk"), ("Een contract zolang een zieke collega afwezig is.", "vervanging")],
          "Niet altijd bepaalt een datum het einde: soms de opdracht of de terugkeer van een collega.",
          kolommen=["onbepaalde duur", "bepaalde duur", "duidelijk omschreven werk", "vervanging"]),
    sorteer("Arbeider of bediende?", ["arbeider", "bediende"],
            [("een metser op een werf", "arbeider"), ("een boekhouder op kantoor", "bediende"), ("een magazijnier die dozen sjouwt", "arbeider"), ("een receptionist in een hotel", "bediende"), ("een schilder die gevels verft", "arbeider"), ("een verkoopster die offertes opmaakt", "bediende")],
            "Een arbeider doet vooral handenarbeid, een bediende vooral hoofdarbeid."),
    keuze("Een overeenkomst van [[*bepaalde|onbepaalde]] duur moet schriftelijk zijn. Staat ze niet op papier, dan geldt ze als een overeenkomst van [[*onbepaalde|bepaalde]] duur.",
          "Zo is de werknemer beschermd."),
    tabel("Moet dit verplicht in een schriftelijke arbeidsovereenkomst?",
          [("de begindatum", J), ("het loon en de arbeidsduur", J), ("de hobby's van de werknemer", F), ("de functie", J)],
          "Ook de identiteit van beide partijen hoort erin."),
    volgorde("Zet de stappen bij de aanwerving van een eerste werknemer in een logische volgorde.",
             ["Een arbeidsongevallenverzekering afsluiten.", "De arbeidsovereenkomst laten ondertekenen.", "De DIMONA-aangifte doen bij de RSZ.", "De werknemer begint te werken."],
             "Verzekering, contract en DIMONA zijn in orde vóór de eerste werkdag."),
    mk("Een snackbar laat een student een weekend werken zonder DIMONA-aangifte. Wat is dat?",
       ["zwartwerk", "studentenarbeid", "klein verlet", "uitzendarbeid"], 0,
       "Zonder DIMONA-aangifte is het zwartwerk, met zware boetes voor de werkgever."),
    tabel("Is dit een plicht van de werkgever of van de werknemer?",
          [("het loon op tijd betalen", "werkgever"), ("het werk zorgvuldig uitvoeren", "werknemer"), ("zorgen voor een veilige werkplek", "werkgever"), ("niets doorvertellen over klanten", "werknemer")],
          "Elk heeft eigen plichten; wat voor de ene een plicht is, is voor de andere een recht.",
          kolommen=["werkgever", "werknemer"]),
    keuze("De plicht om niets door te vertellen over de zaak of de klanten heet de [[*discretieplicht|loyaliteitsplicht|meldingsplicht]].",
          "Wat je op het werk hoort, blijft binnen."),
    mk("Wat onderscheidt een werknemer van een zelfstandige?",
       ["Hij werkt onder het gezag van een werkgever.", "Hij krijgt elke maand een factuur van zijn klant.", "Hij bepaalt zelf welke taken hij doet.", "Hij betaalt zelf zijn sociale bijdragen."], 0,
       "De werkgever bepaalt wat, waar en wanneer er gewerkt wordt."),
    tabel("Voltijds of deeltijds?",
          [("38 uur per week in een sector met een werkweek van 38 uur", "voltijds"), ("vier vijfde van een volle werkweek", "deeltijds"), ("halftijds werken", "deeltijds"), ("de volle werkweek van de sector", "voltijds")],
          "De omvang van de prestaties is een tweede manier om in te delen.",
          kolommen=["voltijds", "deeltijds"]),
    koppel("Welke afkorting of welk begrip hoort bij welke omschrijving?",
           [("RSZ", "Rijksdienst voor Sociale Zekerheid"), ("DIMONA", "melden wie in en uit dienst gaat"), ("gezag", "de werkgever geeft opdrachten")],
           ["het gewaarborgd loon"], "Drie begrippen bij de aanwerving."),
    tabel("Is dit een recht van de werknemer?",
          [("jaarlijkse vakantie", J), ("loon voor zijn werk", J), ("een bedrijfswagen", F), ("een veilige werkplek", J)],
          "Een bedrijfswagen is een extra die in het contract kan staan, geen recht."),
    keuze("Een overeenkomst voor studentenarbeid moet [[*schriftelijk|mondeling]] zijn en er zijn [[*vóór|na]] de student begint.",
          "Ze heeft eigen regels over het aantal uren en lagere sociale bijdragen."),
    mk("Een werknemer blijft drie dagen weg zonder iets te laten weten. Wat is waar?",
       ["Hij komt zijn plichten niet na.", "Dat mag, zolang hij er geen loon voor vraagt.", "Dat is klein verlet en dus gewoon betaald.", "Zijn contract stopt dan vanzelf op dag drie."], 0,
       "Afwezig zijn moet gerechtvaardigd zijn: ziekte, verlof of een wettelijke reden."),
    sleep("Bij een overeenkomst van [[onbepaalde duur]] is er geen einddatum. Bij een overeenkomst voor een [[duidelijk omschreven werk]] stopt het contract als het werk af is.",
          ["bepaalde duur", "studentenarbeid"], "De duur bepaalt de soort overeenkomst."),
    open_("Waarom is een schriftelijke arbeidsovereenkomst ook voor een vast contract veiliger, al mag dat mondeling?",
          "Op papier staan de afspraken over loon, uren, functie en begindatum zwart op wit. Bij een discussie kan elke partij bewijzen wat er afgesproken was, en de werknemer weet precies waar hij recht op heeft.",
          "Schriftelijk is veel veiliger voor beide partijen."),
    inv("Bij welke dienst doet de werkgever de DIMONA-aangifte? Schrijf de afkorting.", ["rsz", "de rsz"],
        "Bij de Rijksdienst voor Sociale Zekerheid."),
    klik("Klik op de letter bij de regel die zegt hoeveel en wanneer Sara betaald wordt.", U, [Z["F"]],
         "Het bedrag, de eenheid per uur en het ogenblik van uitbetaling."),
    tabel("Waarop deel je de arbeidsovereenkomsten in?",
          [("onbepaalde of bepaalde duur", "duur"), ("voltijds of deeltijds", "omvang van de prestaties"), ("arbeider of bediende", "soort werk")],
          "De leeftijd of het loon bepalen de soort overeenkomst niet.",
          kolommen=["duur", "omvang van de prestaties", "soort werk"]),
    keuze("Bij een overeenkomst van bepaalde duur stopt het werk op de einddatum, [[*zonder|na]] een opzegging.",
          "De datum bepaalt het einde."),
    mk("Wat moet in orde zijn vóór een nieuwe werknemer begint?",
       ["de DIMONA-aangifte en de verzekering", "zijn eerste loonbrief van de maand", "zijn belastingaangifte van het jaar", "zijn opzegtermijn en zijn ontslagbrief"], 0,
       "Ook de arbeidsovereenkomst hoort erbij."),
    keuze("Ontbreekt in een schriftelijk contract de einddatum, dan is de [[*werknemer|werkgever]] beschermd: het contract geldt vaak als van onbepaalde duur.",
          "Ontbrekende vermeldingen spelen in het voordeel van de werknemer."),
]

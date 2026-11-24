"""Het oor en het evenwicht — pittig (🚀 Boost doorstroom, biologie).

Eigen vragen strikt binnen bi_oor, met een zelfgetekende doorsnede van het oor om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Doorsnede van het oor, zonder namen -----------------------------------------
OOR = Prent("oor-doorsnede", "Doorsnede van het oor", "schematische doorsnede van uitwendig oor, middenoor en inwendig oor, zonder namen")
OOR.rect(0, 60, 1000, 580, "#f6efe3", "#f6efe3", 0, 0)                                   # schedelbeen
OOR.pad("M 150 170 C 40 180 40 460 150 470 C 200 470 190 400 170 380 C 140 350 150 300 185 300 L 185 345 C 170 345 165 360 175 370 C 205 400 215 470 160 490 C 20 500 10 150 150 150 Z", "#f2c9a8", DONKER, 3)  # oorschelp
OOR.rect(180, 300, 245, 45, "#ffffff", DONKER, 8)                                       # gehoorgang
OOR.ellips(428, 322, 9, 56, ORANJE, DONKER, 2)                                           # trommelvel
OOR.rect(440, 240, 135, 165, "#e6eef6", DONKER, 14)                                      # middenoor
OOR.pad("M 440 322 L 470 300 L 480 312 Z", GRIJS, DONKER, 2)                             # hamer
OOR.rect(478, 292, 34, 18, GRIJS, DONKER, 6)                                             # aambeeld
OOR.pad("M 512 300 L 560 290 L 560 330 L 512 312 Z", GRIJS, DONKER, 2)                   # stijgbeugel
OOR.pad("M 510 405 C 520 470 580 520 650 575", "none", BLAUW, 14)                        # buis van Eustachius
for (cx, cy, rx, ry) in [(650, 175, 45, 55), (720, 160, 55, 40), (690, 215, 40, 30)]:
    OOR.ellips(cx, cy, rx, ry, "none", PAARS, 10)                                        # kanaaltjes
OOR.rect(600, 240, 70, 60, "#e8dcf0", DONKER, 14)                                        # zakjes
for r, w in [(70, 14), (50, 12), (30, 10), (12, 8)]:
    OOR.cirkel(700, 370, r, "none", GROEN, w)                                            # slakkenhuis
OOR.pad("M 765 360 C 820 350 860 330 930 320", "none", GEEL, 10)                         # gehoorzenuw
for x, y, t in [(110, 130, "A"), (300, 285, "B"), (420, 240, "C"), (510, 270, "D"), (640, 600, "E"), (700, 470, "F"), (790, 120, "G"), (930, 290, "H")]:
    OOR.letter(x, y, t)

Z_SCHELP = Prent.zone(30, 140, 180, 370)
Z_GANG = Prent.zone(185, 295, 235, 55)
Z_TROMMEL = Prent.zone(412, 262, 30, 120)
Z_BEEN = Prent.zone(445, 280, 125, 60)
Z_EUST = Prent.zone(505, 405, 160, 180)
Z_SLAK = Prent.zone(625, 295, 150, 150)
Z_KANAAL = Prent.zone(595, 110, 190, 140)
Z_ZENUW = Prent.zone(770, 300, 180, 60)
U = "oor-doorsnede.svg"

VRAGEN = [
    klik("Klik op het dunne vlies dat als eerste gaat trillen als het geluid het einde van de gehoorgang bereikt.", U, [Z_TROMMEL],
         "Het trommelvel scheidt de gehoorgang van het middenoor en trilt mee met het geluid."),
    klik("Klik op het deel dat de druk in het middenoor gelijk houdt met de buitenlucht.", U, [Z_EUST],
         "De buis van Eustachius verbindt het middenoor met de keel; daarom helpt slikken in een vliegtuig."),
    klik("Klik op het deel met het orgaan van Corti, waar geluid in zenuwimpulsen wordt omgezet.", U, [Z_SLAK],
         "Het slakkenhuis is met vloeistof gevuld; de haarcellen van het orgaan van Corti zetten de trilling om."),
    klik("Klik op het deel dat merkt dat je hoofd begint te draaien.", U, [Z_KANAAL],
         "De drie halfcirkelvormige kanaaltjes vangen draaibewegingen op: de rotatiezin."),
    klik("Klik op de drie kleine beentjes die de trilling versterken.", U, [Z_BEEN],
         "Hamer, aambeeld en stijgbeugel werken als hefbomen tussen trommelvel en slakkenhuis."),
    klik("Klik op het deel dat de impulsen naar de hersenen brengt.", U, [Z_ZENUW],
         "De gehoorzenuw vertrekt bij de haarcellen in het slakkenhuis."),
    met_prent(U, tabel("Kijk naar de doorsnede. Bij welk deel van het oor hoort elke letter?",
          [("A", "uitwendig oor"), ("D", "middenoor"), ("F", "inwendig oor"), ("B", "uitwendig oor"), ("G", "inwendig oor")],
          "Oorschelp en gehoorgang vormen het uitwendige oor, de beentjes zitten in het middenoor, slakkenhuis en kanaaltjes in het inwendige oor.",
          ["uitwendig oor", "middenoor", "inwendig oor"])),
    met_prent(U, mk("Een prop oorsmeer zit vast bij letter B. Welke soort slechthorendheid ontstaat er?",
       ["geleidingsslechthorendheid", "slechthorendheid door kapotte haarcellen", "tinnitus door de gehoorzenuw", "een stoornis van de rotatiezin"], 0,
       "Het geluid raakt niet goed tot bij het trommelvel: de geleiding is gestoord.")),
    volgorde("Zet de weg van het geluid in de juiste volgorde.",
             ["oorschelp", "gehoorgang", "trommelvel", "gehoorbeentjes", "slakkenhuis", "gehoorzenuw"],
             "Van opvangen over trillen en versterken tot omzetten en doorgeven."),
    casus("Sem gaat elk weekend naar een concert, altijd vooraan bij de boxen, zonder oordopjes. Na een concert hoort hij soms urenlang een piep.", [
        mk("Hoe heet die piep die er van buiten niet is?",
           ["tinnitus of oorsuizen", "geleidingsslechthorendheid", "wagenziekte", "ouderdomsslechthorendheid"], 0,
           "Beschadigde haarcellen of de gehoorzenuw geven dan zelf signalen."),
        tabel("Klopt dit over de gehoorschade van Sem?",
              [("Haarcellen die door hard geluid kapot zijn, groeien niet meer terug.", J), ("Een hoortoestel kan zijn kapotte haarcellen herstellen.", F), ("Oordopjes beschermen de haarcellen tegen te veel geluid.", J)],
              "Gehoorschade is blijvend; een hoortoestel versterkt enkel het geluid voor de cellen die nog werken."),
        mk("Waarom beschermt het oor zich niet goed genoeg tegen een concert van uren?",
           ["De spiertjes in het middenoor houden de beentjes niet urenlang strak.", "Het trommelvel gaat bij hard geluid altijd vanzelf helemaal dicht.", "De buis van Eustachius laat het geluid naar de keel ontsnappen.", "De kanaaltjes van het evenwichtsorgaan vangen het geluid op."], 0,
           "Die bescherming werkt even, maar niet bij aanhoudend hard geluid."),
    ]),
    sorteer("Positiezin of rotatiezin?", ["Positiezin", "Rotatiezin"],
            [("je weet met gesloten ogen of je hoofd voorover hangt", "Positiezin"), ("je merkt dat je op een draaimolen ronddraait", "Rotatiezin"), ("je voelt dat je in een lift naar beneden kantelt", "Positiezin"), ("je hoofd snel naar links draaien", "Rotatiezin"), ("rechtop staan tegenover de zwaartekracht", "Positiezin")],
            "De positiezin meet de stand van het hoofd tegenover de zwaartekracht, de rotatiezin meet draaien."),
    mk("Je draait een hele tijd rond op een bureaustoel en stopt plots. Waarom blijf je even duizelig?",
       ["De vloeistof in de kanaaltjes draait nog even door.", "Je trommelvel trilt nog een hele tijd na van de snelle beweging.", "De gehoorbeentjes zijn even van hun plaats geschoven.", "Je ogen zien nog een stilstaand beeld terwijl je draait."], 0,
       "Door haar traagheid stopt de vloeistof later dan je hoofd."),
    keuze("Bij een draai blijft de vloeistof in de kanaaltjes door haar [[*traagheid|dikte|temperatuur]] even achter en buigt ze de haarcellen.",
          "Traagheid: een vloeistof wil haar toestand behouden."),
    tabel("Welke informatie gebruiken je hersenen om je evenwicht te bewaren?",
          [("de signalen van het evenwichtsorgaan", J), ("wat je ogen zien", J), ("signalen uit je spieren en gewrichten", J), ("de geluiden die het slakkenhuis opvangt", F)],
          "Oor, ogen en spieren: drie bronnen die de kleine hersenen samenleggen."),
    mk("Waarom word je soms wagenziek als je in een rijdende auto een boek leest?",
       ["Je oor meldt beweging terwijl je ogen een stilstaand blad zien.", "Het lezen van kleine letters maakt je trommelvel heel moe.", "De buis van Eustachius gaat helemaal dicht door de hoge snelheid.", "Je slakkenhuis vangt het geluid van de motor op."], 0,
       "De hersenen krijgen twee tegenstrijdige berichten."),
    koppel("Welke taak hoort bij elk deel?",
           [("oorschelp", "het geluid opvangen en naar binnen leiden"), ("trommelvel", "meetrillen met het geluid"), ("gehoorbeentjes", "de trilling versterken"), ("slakkenhuis", "de trilling omzetten in impulsen")],
           ["de druk gelijkhouden", "draaibewegingen meten"], "Elk deel doet een stap in het horen."),
    tabel("Klopt dit over het horen?",
          [("Horen gebeurt pas echt in de hersenen.", J), ("In het slakkenhuis reist het geluid door lucht.", F), ("De gehoorbeentjes liggen in het middenoor.", J), ("Het evenwichtsorgaan ligt naast het slakkenhuis.", J)],
          "Het slakkenhuis is met vloeistof gevuld; de hersenschors maakt er geluid van."),
    mk("Een ontsteking in het inwendige oor maakt iemand duizelig én slechthorend. Hoe komt dat?",
       ["Gehoor en evenwicht liggen vlak naast elkaar.", "De ontsteking zit in de oorschelp, die gehoor en evenwicht regelt.", "Het trommelvel regelt naast het horen ook het evenwicht.", "De gehoorbeentjes sturen de kanaaltjes aan."], 0,
       "Slakkenhuis en evenwichtsorgaan zitten in hetzelfde benige doolhof."),
    inv("Hoe heet het spiraalvormige deel van het inwendige oor waarin het gehoor zit? Antwoord met één woord.",
        ["slakkenhuis", "het slakkenhuis", "cochlea"], "Het slakkenhuis, met daarin het orgaan van Corti."),
    sleep("De [[hamer]], het aambeeld en de [[stijgbeugel]] brengen de trilling van het [[trommelvel]] naar het slakkenhuis.",
          ["oorschelp", "gehoorzenuw"], "De gehoorbeentjes vormen een ketting in het middenoor."),
    tabel("Wat hebben de haarcellen in het slakkenhuis en die in het evenwichtsorgaan gemeen?",
          [("Ze worden geprikkeld door een bewegende vloeistof.", J), ("Ze sturen hun signaal naar de hersenen.", J), ("Ze vangen allebei geluid op.", F)],
          "Allebei worden ze gebogen door vloeistof; de ene meldt geluid, de andere beweging."),
    met_prent(U, mk("Kijk naar de doorsnede. Bij welke letter zit het deel dat in een vliegtuig 'plopt' als je slikt?",
       ["E", "C", "F", "A"], 0,
       "Bij het slikken gaat de buis van Eustachius even open en wordt de druk in het middenoor gelijk.")),
    tabel("Klopt dit over de buis van Eustachius?",
          [("Ze verbindt het middenoor met de keel.", J), ("Ze brengt het geluid naar het slakkenhuis.", F), ("Zonder die buis zou het trommelvel bij drukverschil pijnlijk bol gaan staan.", J)],
          "De buis houdt de druk aan beide kanten van het trommelvel gelijk."),
    mk("Een gaatje in het trommelvel na een ontsteking zorgt vooral voor welk probleem?",
       ["Het geluid wordt slechter doorgegeven naar het middenoor.", "De kanaaltjes melden voortdurend een draai.", "De haarcellen in het slakkenhuis sterven allemaal af.", "De gehoorzenuw stuurt geen signalen meer naar de hersenen."], 0,
       "Een kapot trommelvel trilt minder goed mee: dat is geleidingsslechthorendheid."),
    sorteer("Uitwendig oor, middenoor of inwendig oor?", ["Uitwendig oor", "Middenoor", "Inwendig oor"],
            [("de oorschelp", "Uitwendig oor"), ("de stijgbeugel", "Middenoor"), ("het slakkenhuis", "Inwendig oor"), ("de gehoorgang", "Uitwendig oor"), ("het aambeeld", "Middenoor"), ("het evenwichtsorgaan", "Inwendig oor")],
            "Drie delen van het oor, elk met hun eigen onderdelen."),
    mk("Een danser draait snel rond en valt toch niet om. Hoe lukt dat?",
       ["Door oefening wegen de hersenen de signalen van het oor anders.", "Dansers hebben geen vloeistof in hun kanaaltjes.", "Haar gehoorbeentjes houden de kanaaltjes stil tijdens het draaien.", "Ze houdt tijdens het draaien de hele tijd haar ogen dicht."], 0,
       "Dansers kiezen ook een vast punt om naar te kijken en trainen hun hersenen."),
    keuze("De kleine hersenen leggen de signalen van het [[*evenwichtsorgaan|slakkenhuis|trommelvel]], de ogen en de spieren samen.",
          "Zo bewaar je je evenwicht."),
    open_("Leg uit hoe je merkt dat je hoofd begint te draaien. Gebruik de woorden kanaaltjes, vloeistof, traagheid en haarcellen.",
          "In de drie kanaaltjes zit vloeistof. Als je hoofd begint te draaien, blijft de vloeistof door haar traagheid even achter. Ze buigt daardoor de haarcellen, die een signaal naar de hersenen sturen."),
]

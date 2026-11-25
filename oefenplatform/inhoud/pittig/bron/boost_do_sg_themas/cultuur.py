"""Cultuur en cultuuruitingen — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_cultuur: het begrip cultuur, de zeven
cultuuruitingen en culturen vergelijken (westers en niet-westers, dominante
cultuur en subculturen, jongerenculturen). Met zes zelfgetekende
pictogrammen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, ROOD, BLAUW, LICHTGROEN, ORANJE

PI = Prent("zes-pictogrammen-cultuur", "Zes pictogrammen", "zes vakjes met een tekening, letters A tot F")
VAK = [("A", 60, 70), ("B", 370, 70), ("C", 680, 70), ("D", 60, 345), ("E", 370, 345), ("F", 680, 345)]
for t, x, y in VAK:
    PI.rect(x, y, 260, 230, "#ffffff", DONKER, 14, 3)
    PI.letter(x + 230, y + 200, t)
# A: vlag
PI.lijn(130, 110, 130, 270, DONKER, 5); PI.rect(130, 110, 120, 80, BLAUW, DONKER, 0, 2); PI.cirkel(190, 150, 22, "#ffffff", "none", 0)
# B: twee ringen
PI.cirkel(470, 180, 42, "none", "#c9a24a", 10); PI.cirkel(530, 180, 42, "none", "#c9a24a", 10)
# C: palet met verf
PI.pad("M 740 200 q -10 -90 90 -90 q 90 0 80 80 q -5 40 -45 25 q -30 -10 -35 25 q -5 40 -45 25 q -40 -15 -45 -65 Z", "#e8d3a8", DONKER, 3)
for (cx, cy, k) in ((790, 150, ROOD), (835, 135, BLAUW), (875, 160, GEEL), (775, 195, LICHTGROEN)):
    PI.cirkel(cx, cy, 12, k, DONKER, 1)
# D: twee tekstballonnen in twee talen
PI.rect(90, 380, 120, 60, "#ffffff", DONKER, 14, 2); PI.tekst(150, 418, "Hallo!", 22)
PI.rect(170, 460, 120, 60, "#ffffff", DONKER, 14, 2); PI.tekst(230, 498, "Salam!", 22)
# E: open boek
PI.pad("M 500 400 Q 450 385 405 400 L 405 510 Q 450 495 500 510 Z", "#ffffff", DONKER, 3)
PI.pad("M 500 400 Q 550 385 595 400 L 595 510 Q 550 495 500 510 Z", "#ffffff", DONKER, 3)
for i in range(4):
    PI.lijn(420, 425 + i * 20, 485, 425 + i * 18, GRIJS, 2); PI.lijn(515, 425 + i * 18, 580, 425 + i * 20, GRIJS, 2)
# F: klok
PI.cirkel(810, 455, 70, "#ffffff", DONKER, 4)
for i in range(12):
    import math
    a = i * math.pi / 6
    PI.lijn(810 + 58 * math.sin(a), 455 - 58 * math.cos(a), 810 + 66 * math.sin(a), 455 - 66 * math.cos(a), DONKER, 2)
PI.lijn(810, 455, 810, 405, DONKER, 4); PI.lijn(810, 455, 845, 455, DONKER, 5)
U = "zes-pictogrammen-cultuur.svg"
Z = {t: [Prent.zone(x, y, 260, 230)] for t, x, y in VAK}

STAGE = ("Lees het verslag.\n\n"
         "Femke (17) doet een stage van drie maanden in Japan. De eerste dagen voelt ze zich verloren: mensen buigen in plaats van een hand te geven, "
         "en in de bus is het muisstil. Ze vindt dat eerst « raar en afstandelijk ». Na een maand begrijpt ze dat stilte daar beleefdheid toont. "
         "Ze buigt nu ook en mist soms de luidruchtige gesprekken thuis.")

VRAGEN = [
    klik("Bekijk de pictogrammen. Klik op het pictogram dat het best past bij een ritueel.", U, Z["B"], "Een trouwfeest: een handeling met een vaste vorm en een betekenis."),
    klik("Klik op het pictogram dat het best past bij een symbool.", U, Z["A"], "Een vlag staat voor iets anders: een land of een idee."),
    klik("Klik op het pictogram dat het best past bij taal als cultuuruiting.", U, Z["D"], "Wie de taal leert, leert ook de gewoontes erachter."),
    klik("Klik op het pictogram dat het best past bij de gewoonte 'op tijd komen'.", U, Z["F"], "Wat hier te laat heet, kan elders gewoon zijn."),
    casus(STAGE, [
        keuze("De verwarring van Femke in de eerste dagen heet een [[*cultuurschok|subcultuur|enculturatie]].", "Wat vanzelf sprak, klopt plots niet meer."),
        keuze("'Raar en afstandelijk' vinden, vanuit je eigen gewoontes, is [[*etnocentrisme|een ritueel|een symbool]].", "De eigen gewoontes als de normale nemen."),
        sorteer("Welke cultuuruiting zie je?", ["gebruik of gewoonte", "waarden en normen"],
                [("buigen in plaats van een hand geven", "gebruik of gewoonte"), ("stilte in de bus toont respect", "waarden en normen")],
                "Een gewoonte, en de waarde die erachter zit."),
        mk("Wat toont het verhaal over cultuur?",
           ["ze wordt aangeleerd", "ze is aangeboren en verandert nooit", "ze is in elk land precies dezelfde", "ze bestaat enkel uit kunst en muziek"],
           0, "Femke leert de gewoontes stap voor stap."),
    ]),
    tabel("Is dit een van de zeven cultuuruitingen?",
          [("rituelen", J), ("symbolen", J), ("lichaamslengte", F), ("taal", J), ("kennis", J)],
          "Zeven uitingen: gebruiken en gewoontes, kennis, kunst, rituelen, symbolen, taal, waarden en normen."),
    sorteer("Welke cultuuruiting?", ["ritueel", "symbool", "kennis", "kunst"],
            [("een begrafenis met een vaste volgorde", "ritueel"), ("het logo van een voetbalclub", "symbool"), ("weten hoe je rijst kweekt", "kennis"), ("een volksdans", "kunst")],
            "Ook praktische kennis telt mee."),
    koppel("Koppel het begrip over cultuur aan de uitleg.",
           [("dominante cultuur", "de cultuur van de meerderheid"), ("subcultuur", "een groep met eigen gewoontes binnen een grotere cultuur"), ("jongerencultuur", "een cultuur van jongeren met eigen muziek en kledij"), ("etnocentrisme", "een andere cultuur beoordelen vanuit de jouwe")],
           ["een cultuur die aangeboren is"], "Culturen vergelijken."),
    tabel("Klopt dit over cultuur?",
          [("Cultuur is aangeboren.", F), ("Een gebaar betekent in elke cultuur hetzelfde.", F), ("Cultuur verandert in de loop van de tijd.", J), ("Je kan tegelijk bij de dominante cultuur en een subcultuur horen.", J)],
          "Cultuur wordt aangeleerd en doorgegeven."),
    mk("Een krant zet Japan en Marokko samen onder 'niet-westerse culturen'. Wat is het probleem?",
       ["ze verschillen onderling sterk", "het Westen heeft eigenlijk helemaal geen eigen cultuur", "alle niet-westerse landen zijn in alles precies gelijk", "er bestaan geen verschillen tussen culturen"],
       0, "Japan en Marokko zijn allebei niet-westers en lijken weinig op elkaar."),
    keuze("Een groep skaters met eigen kledij, taal en vaste plekken is een [[*subcultuur|dominante cultuur|natie]].", "Eigen symbolen binnen een grotere samenleving."),
    keuze("Een subcultuur staat [[*niet altijd|altijd]] tegenover de dominante cultuur.", "Alleen een tegencultuur zet zich uitdrukkelijk af."),
    mk("Een kledingmerk was 'cool' bij jongeren, tot ook hun ouders het gingen dragen. Wat toont dat?",
       ["een jongerencultuur draait om onderscheid", "dat jongeren helemaal geen waarden en normen hebben", "dat jongerenculturen geen enkel symbool kennen", "dat volwassenen nooit iets overnemen van jongeren"],
       0, "Zodra iedereen iets overneemt, verliest het zijn waarde als teken."),
    tabel("Wordt dit vaak aan westerse culturen toegeschreven?",
          [("nadruk op het individu", J), ("nadruk op zelfstandigheid", J), ("nadruk op prestatie", J), ("nadruk op de grote familie boven alles", F)],
          "Wel met voorzichtigheid: binnen elke groep verschilt veel."),
    keuze("Uit de waarde respect volgt de [[*norm|symbool|ritueel]] dat je iemand laat uitspreken.", "Een waarde is een ideaal, een norm de regel."),
    sleep("Cultuur is alles wat een groep [[deelt]] en [[doorgeeft]]. Ze wordt [[aangeleerd]], niet geërfd.",
          ["aangeboren", "verbergt"], "Daarom kan ze ook veranderen."),
    keuze("Twee landen vieren nieuwjaar op een andere dag. Je ziet [[*hetzelfde ritueel met een andere invulling|twee totaal verschillende rituelen|geen ritueel]].", "De functie is gelijk, de vorm verschilt."),
    mk("Waarmee vergelijk je twee culturen het best?",
       ["met de cultuuruitingen", "met de gemiddelde lengte van de inwoners", "met het aantal toeristen dat er elk jaar komt", "met de kleuren die op hun vlag staan"],
       0, "Zo vergelijk je punt per punt."),
    keuze("Eten, muziek en woorden reizen mee als culturen in contact komen. Culturen [[*beïnvloeden elkaar|blijven onaangeroerd|verdwijnen meteen]].", "Een groot deel van wat 'eigen' lijkt, kwam ooit van elders."),
    inv("Hoeveel cultuuruitingen onderscheid je? Schrijf het getal.", ["7", "zeven"], "Samen beschrijven ze wat een cultuur is."),
    tabel("Hoort dit bij een subcultuur?",
          [("eigen symbolen", J), ("bestaan binnen een grotere cultuur", J), ("je kan er zelf bij gaan horen", J), ("ze heeft geen enkele band met de dominante cultuur", F)],
          "Een subcultuur deelt veel met de dominante cultuur."),
    keuze("Een jongere draagt kledij die zijn ouders lelijk vinden. Die kledij werkt als een [[*symbool|ritueel|norm]] dat toont bij welke groep hij hoort.", "Kledij staat voor iets anders."),
    keuze("Wat één persoon alleen doet, is [[*nog geen|al een]] cultuur: het delen maakt het cultuur.", "Cultuur is een gedeeld geheel."),
    keuze("Cultuur wordt doorgegeven via [[*socialisatie|erfelijkheid|rijping]].", "Socialisatie geeft waarden, normen en andere cultuuruitingen door."),
    tabel("Is dit een kunstuiting?",
          [("muziek", J), ("schilderkunst", J), ("dans", J), ("een verkeersregel", F)],
          "Kunst is één van de zeven uitingen."),
    keuze("Een duim omhoog betekent [[*niet overal|overal]] goedkeuring.", "Je leest een gebaar altijd in zijn cultuur."),
    open_("Vergelijk twee culturen of groepen die je kent op twee cultuuruitingen.",
          "Bijvoorbeeld een voetbalclub en een theatergroep. Symbolen: de club heeft een sjaal en een logo, de theatergroep een eigen poster. Rituelen: de club zingt het clublied voor de match, de theatergroep wenst elkaar 'toi toi toi' voor de voorstelling."),
]

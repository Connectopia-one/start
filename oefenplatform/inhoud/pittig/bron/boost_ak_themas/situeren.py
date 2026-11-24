"""Waar ligt het, en hoe weet je dat? — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_situeren, met een zelfgetekend gradennet om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, ROOD, GROEN, DONKER

# Gradennet (equirectangulair): x = 140 + (lengte + 180) * 2, y = 320 − breedte * 2.6
NET = Prent("gradennet", "Gradennet met punten", "rechthoekig gradennet van 180° WL tot 180° OL en van 90° ZB tot 90° NB, met de bijzondere lijnen en zes punten met een letter")
def X(l): return 140 + (l + 180) * 2
def Y(b): return 340 - b * 2.6
NET.rect(X(-180), Y(90), 720, 468, "#f3f8fc", DONKER, 0, 2)
for l in range(-150, 180, 30):
    NET.lijn(X(l), Y(90), X(l), Y(-90), "#c9d6e2", 1)
    NET.tekst(X(l), Y(-90) + 22, f"{abs(l)}°", 14)
for b in range(-60, 90, 30):
    NET.lijn(X(-180), Y(b), X(180), Y(b), "#c9d6e2", 1)
    NET.tekst(X(-180) - 8, Y(b) + 5, f"{abs(b)}°", 14, "end")
NET.lijn(X(-180), Y(0), X(180), Y(0), ROOD, 3)
NET.lijn(X(0), Y(90), X(0), Y(-90), ROOD, 3)
for b in (23.5, -23.5):
    NET.lijn(X(-180), Y(b), X(180), Y(b), ORANJE, 2, True)
for b in (66.5, -66.5):
    NET.lijn(X(-180), Y(b), X(180), Y(b), BLAUW, 2, True)
NET.tekst(X(180) + 8, Y(0) + 5, "0°", 14, "start")
NET.tekst(X(0), Y(90) - 8, "0°", 14)
PUNTEN = {"A": (40, -100), "B": (-30, 60), "C": (60, 30), "D": (-15, -45), "E": (10, 120), "F": (70, -150)}
for t, (b, l) in PUNTEN.items():
    NET.cirkel(X(l), Y(b), 6, DONKER, DONKER, 1)
    NET.letter(X(l) + 22, Y(b) - 20, t)
U = "gradennet.svg"
Z = {t: Prent.zone(X(l) - 30, Y(b) - 45, 75, 65) for t, (b, l) in PUNTEN.items()}

VRAGEN = [
    klik("Klik op de plaats met coördinaten 40° NB en 100° WL.", U, [Z["A"]],
         "Noorderbreedte ligt boven de evenaar, westerlengte links van de nulmeridiaan."),
    klik("Klik op de plaats op 30° ZB en 60° OL.", U, [Z["B"]],
         "Zuiderbreedte onder de evenaar, oosterlengte rechts van de nulmeridiaan."),
    klik("Klik op de plaats die tussen de evenaar en de Kreeftskeerkring ligt, ten oosten van de nulmeridiaan.", U, [Z["E"]],
         "E ligt op 10° NB en 120° OL: in de tropen van het noordelijk halfrond."),
    klik("Klik op de plaats die ten noorden van de noordpoolcirkel ligt.", U, [Z["F"]],
         "F ligt op 70° NB, boven de poolcirkel van 66,5°."),
    tabel("Lees de coördinaten van de punten op het gradennet. Klopt dit?",
          [("C ligt op 60° NB en 30° OL.", J), ("D ligt op het zuidelijk halfrond.", J), ("D ligt ten oosten van de nulmeridiaan.", F), ("A en F liggen allebei op het westelijk halfrond.", J)],
          "D ligt op 15° ZB en 45° WL: zuid en west."),
    casus("Mila stuurt drie berichten vanuit haar wereldreis: 'Ik zit op 52° NB en 4° OL.' Daarna: 'Nu sta ik aan de voet van de Andes, in het westen van Zuid-Amerika.' Tot slot: 'Mijn hotel ligt naast de grootste moskee van de stad.'", [
        tabel("Hoe situeert Mila in elk bericht?",
              [("het eerste bericht", "absoluut"), ("het tweede bericht", "relatief, fysisch"), ("het derde bericht", "relatief, sociaaleconomisch")],
              "Coördinaten zijn absoluut; een gebergte is fysisch; een gebouw of religie is sociaaleconomisch.",
              ["absoluut", "relatief, fysisch", "relatief, sociaaleconomisch"]),
        mk("Op welk halfrond lag Mila bij haar eerste bericht?",
           ["noordelijk en oostelijk", "noordelijk en westelijk", "zuidelijk en oostelijk", "zuidelijk en westelijk"], 0,
           "NB is noordelijk, OL is oostelijk."),
    ]),
    sorteer("Is het element fysischgeografisch of sociaaleconomisch?", ["fysischgeografisch", "sociaaleconomisch"],
            [("een gebergte", "fysischgeografisch"), ("een wereldstad", "sociaaleconomisch"), ("een klimaatzone", "fysischgeografisch"), ("de taal die er gesproken wordt", "sociaaleconomisch"), ("een rivier", "fysischgeografisch"), ("een wereldblok als de Europese Unie", "sociaaleconomisch")],
            "Natuurlijke elementen zijn fysisch; wat de mens maakt of afspreekt, is sociaaleconomisch."),
    volgorde("Rangschik de lijnen van noord naar zuid.",
             ["noordpoolcirkel", "Kreeftskeerkring", "evenaar", "Steenbokskeerkring", "zuidpoolcirkel"],
             "66,5° NB, 23,5° NB, 0°, 23,5° ZB en 66,5° ZB."),
    koppel("Welke breedte hoort bij welke lijn?",
           [("evenaar", "0°"), ("keerkringen", "23,5°"), ("poolcirkels", "66,5°"), ("polen", "90°")],
           ["45°"], "Die vier waarden zijn de vaste ankerpunten van het gradennet."),
    mk("Hoe lang is een breedtecirkel op 60° NB vergeleken met de evenaar?",
       ["korter", "even lang", "langer", "dat hangt af van de lengte"], 0,
       "Breedtecirkels worden korter naar de polen toe; de evenaar is de langste."),
    tabel("Klopt dit over de datumlijn?",
          [("Ze volgt ongeveer de meridiaan van 180°.", J), ("Ze loopt grotendeels door de Stille Oceaan.", J), ("Ze is een rechte lijn zonder bochten.", F)],
          "De lijn maakt bochten om eilandengroepen niet in twee data te splitsen."),
    sleep("Meridianen lopen van [[pool]] tot pool en geven de geografische [[lengte]]. Breedtecirkels lopen evenwijdig met de [[evenaar]] en geven de geografische breedte.",
          ["breedte", "datumlijn"], "Lengte en breedte samen geven de absolute ligging."),
    casus("Een klas moet bepalen in welke vegetatiezone een stad op 64° NB in Rusland ligt.", [
        mk("Welke bron helpt het meest?",
           ["een vegetatiekaart in de atlas", "een gedetailleerd stratenplan van de stad", "een wereldkaart met alle wereldblokken", "de mentale kaart van een klasgenoot"], 0,
           "Een vegetatiekaart toont de zones rechtstreeks."),
        mk("Welke vegetatiezone verwacht je daar?",
           ["naaldwoud", "tropisch regenwoud", "savanne", "woestijn"], 0,
           "Net onder de poolcirkel ligt in Rusland de taiga of het naaldwoud."),
        tabel("Klopt dit over haar redenering?",
              [("De breedte zegt veel over de klimaatzone.", J), ("De lengte alleen volstaat om de klimaatzone te bepalen.", F), ("Een klimatogram van een station in die stad helpt ook.", J)],
              "Klimaat hangt vooral samen met breedte, hoogte en ligging tegenover de zee."),
    ]),
    tabel("Een kaart met Groenland even groot als Afrika. Klopt dit?",
          [("De kaart vertekent oppervlakten naar de polen toe.", J), ("Groenland is in werkelijkheid veel kleiner dan Afrika.", J), ("Deze kaart toont vormen, oppervlakten en afstanden allemaal juist.", F)],
          "Een bol op een plat vlak brengen geeft altijd vertekening."),
    sorteer("Over welke afstand gaat het?", ["werkelijke afstand", "ervaren afstand", "mentale afstand"],
            [("de 120 km die de gps aangeeft", "werkelijke afstand"), ("een rit die lang lijkt door files", "ervaren afstand"), ("denken dat Marokko verder ligt dan Griekenland", "mentale afstand"), ("de kilometerteller na de rit", "werkelijke afstand"), ("een treinreis die voorbijvliegt met een goed boek", "ervaren afstand")],
            "Werkelijk is meetbaar; ervaren gaat over de reis; mentaal is wat je denkt."),
    tabel("Klopt dit over mentale kaarten?",
          [("Een mentale kaart zit in je hoofd.", J), ("Ze is voor iedereen dezelfde.", F), ("Plaatsen die je vaak bezoekt, krijgen er meer details in.", J), ("Het kaartbeeld dat je vaak ziet, kleurt je mentale kaart.", J)],
          "Een mentale kaart is persoonlijk en onvolledig."),
    mk("Voor een jongere is een plein vooral een plek om af te spreken; voor een oudere de plaats van de vroegere markt. Wat toont dat?",
       ["dat je context de betekenis van een plaats kleurt", "dat het plein in werkelijkheid twee aparte plaatsen is", "dat een van beiden het plein verkeerd situeert", "dat de echte betekenis van elke plaats in de atlas staat"], 0,
       "Plaatsen krijgen betekenis door ervaring, leeftijd en cultuur."),
    casus("Je onderzoekt welke straten in je gemeente bij hevige regen onder water kunnen lopen. Je vindt een digitale kaart op het internet.", [
        volgorde("Rangschik je stappen.",
                 ["Kijk na wie de kaart gemaakt heeft.", "Lees de titel, de legende en het jaartal.", "Zoek de overstromingsgevoelige gebieden op.", "Leg ze naast een stratenplan van je gemeente."],
                 "Eerst de betrouwbaarheid en de legende, dan pas het eigenlijke werk."),
        tabel("Klopt dit over je bron?",
              [("Een thematische kaart over overstromingen past bij je vraag.", J), ("De maker kiest wat er wel en niet op de kaart staat.", J), ("Een toeristische kaart toont dezelfde informatie.", F)],
              "Elke kaart kiest een thema en laat de rest weg."),
    ]),
    inv("Een plaats ligt op 23,5° ZB. Op welke bijzondere lijn ligt ze? Schrijf de naam.", ["Steenbokskeerkring", "steenbokskeerkring", "de Steenbokskeerkring"],
        "De keerkring op het zuidelijk halfrond is de Steenbokskeerkring."),
    keuze("Een kaart met het zuiden bovenaan is [[*een keuze van de maker|een fout tegen de regels|onmogelijk te lezen]].",
          "Het noorden bovenaan is een gewoonte, geen natuurwet."),
    klik("Klik op de plaats die in de keerkringszone van het zuidelijk halfrond ligt, ten westen van de nulmeridiaan.", U, [Z["D"]],
         "D ligt op 15° ZB, tussen de evenaar en de Steenbokskeerkring, en op 45° WL."),
    tabel("Twee plaatsen liggen op dezelfde meridiaan. Klopt dit?",
          [("Ze hebben op hetzelfde moment dezelfde zonnetijd.", J), ("Ze hebben dezelfde geografische lengte.", J), ("Ze hebben dezelfde geografische breedte.", F)],
          "Een meridiaan verbindt plaatsen met dezelfde lengte, van pool tot pool."),
    mk("Waarom vraagt men om absoluut te situeren op 1° nauwkeurig?",
       ["omdat je dat met een gewone atlas nog goed kan aflezen", "omdat kleinere eenheden dan een graad niet bestaan", "omdat de coördinaten elk jaar een beetje verschuiven", "omdat elke stad precies één graad groot is"], 0,
       "Met een atlas lees je graden goed af; minuten zijn al moeilijk."),
    koppel("Welke kaart kies je voor welke vraag?",
           [("Waar liggen de bergen en dalen?", "reliëfkaart"), ("Welke gebieden lopen onder bij hoogwater?", "kaart van overstromingsgevoelige gebieden"), ("Waar ligt het dichtstbijzijnde museum?", "toeristische kaart"), ("In welke klimaatzone ligt een plaats?", "klimaatkaart")],
           ["mentale kaart"], "Kies de thematische kaart die bij je vraag past."),
    tabel("Waarmee wordt hier gesitueerd?",
          [("'De stad ligt aan de monding van de Schelde.'", "fysisch element"), ("'Het dorp ligt in de Kempense laagvlakte.'", "reliëfeenheid"), ("'De haven is de grootste van de Europese Unie.'", "wereldblok")],
          "Een rivier is een fysisch element, een laagvlakte een reliëfeenheid, de EU een wereldblok.",
          ["fysisch element", "reliëfeenheid", "wereldblok"]),
    inv("Hoeveel graden liggen de Kreeftskeerkring en de Steenbokskeerkring van elkaar af? Schrijf het getal.", ["47", "47°"],
        "23,5° NB tot 23,5° ZB is samen 47°."),
]

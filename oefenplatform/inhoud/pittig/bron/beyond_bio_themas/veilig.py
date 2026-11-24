"""Veilig en duurzaam werken in het labo — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Gevarenpictogrammen (vereenvoudigd) -------------------------------------
GP = Prent("gevarenpictogrammen", "Vier gevarenpictogrammen (vereenvoudigd getekend)", "vier ruiten met rode rand: een vlam, een doodshoofd, een vloeistof op een hand, een uitroepteken; letters P tot S")
for i in range(4):
    cx, cy = 140 + i * 240, 300
    GP.svg(f'<polygon points="{cx},{cy-110} {cx+110},{cy} {cx},{cy+110} {cx-110},{cy}" fill="#fff" stroke="#d0202a" stroke-width="12" stroke-linejoin="round"/>')
# P vlam
GP.pad("M140 360 C 95 350 95 300 120 270 C 120 300 135 300 135 290 C 130 260 150 240 160 220 C 165 260 190 280 180 320 C 178 345 165 360 140 360 Z", DONKER, DONKER, 1)
GP.rect(100, 362, 80, 8, DONKER, DONKER, 0, 0)
# Q doodshoofd
GP.ellips(380, 280, 34, 32, DONKER, DONKER, 1)
GP.rect(362, 300, 36, 22, DONKER, DONKER, 4, 0)
GP.cirkel(367, 278, 9, "#fff", "none", 0)
GP.cirkel(393, 278, 9, "#fff", "none", 0)
GP.lijn(335, 335, 425, 365, DONKER, 8)
GP.lijn(335, 365, 425, 335, DONKER, 8)
# R bijtend: buisje dat druppelt op hand en plaat
GP.rect(585, 230, 30, 14, DONKER, DONKER, 2, 0)
GP.lijn(600, 244, 610, 262, DONKER, 3)
GP.lijn(655, 244, 650, 262, DONKER, 3)
GP.rect(640, 230, 30, 14, DONKER, DONKER, 2, 0)
GP.pad("M575 300 L 625 300 L 625 318 L 575 318 Z", DONKER, DONKER, 1)
GP.pad("M640 300 L 690 300 L 680 318 L 650 318 Z", DONKER, DONKER, 1)
GP.rect(560, 340, 140, 12, DONKER, DONKER, 0, 0)
# S uitroepteken
GP.rect(851, 230, 18, 90, DONKER, DONKER, 6, 0)
GP.cirkel(860, 350, 12, DONKER, DONKER, 0)
for i, k in enumerate("PQRS"):
    GP.letter(140 + i * 240, 470, k)
ZGP = {k: [Prent.zone(30 + i * 240, 190, 220, 220), Prent.rond(140 + i * 240, 470, 22)] for i, k in enumerate("PQRS")}

# Microscoop ---------------------------------------------------------------
MS = Prent("microscoop-delen", "Een lichtmicroscoop (schematisch)", "zijaanzicht van een microscoop met letters A tot F")
MS.rect(330, 520, 300, 40, "#cfd8dc", DONKER, 10, 2)
MS.pad("M560 520 L 590 520 L 600 260 C 600 200 560 170 520 170 L 500 200 C 540 205 565 230 565 270 Z", "#cfd8dc", DONKER, 2)
MS.svg(f'<polygon points="480,215 520,175 540,190 500,232" fill="#cfd8dc" stroke="{DONKER}" stroke-width="2"/>')
MS.rect(380, 400, 200, 18, "#90a4ae", DONKER, 3, 2)
MS.rect(470, 418, 20, 70, "#ffe9a8", DONKER, 4, 1.5)
MS.svg(f'<polygon points="420,190 470,170 495,220 445,240" fill="#90a4ae" stroke="{DONKER}" stroke-width="2"/>')
MS.svg(f'<polygon points="430,100 470,85 488,175 448,190" fill="#cfd8dc" stroke="{DONKER}" stroke-width="2"/>')
MS.rect(420, 80, 46, 30, "#90a4ae", DONKER, 4, 2)
MS.rect(440, 245, 22, 70, "#b0bec5", DONKER, 3, 2)
MS.rect(470, 245, 18, 50, "#b0bec5", DONKER, 3, 2)
MS.cirkel(600, 360, 34, "#78909c", DONKER, 2)
MS.cirkel(600, 440, 20, "#b0bec5", DONKER, 2)
LMS = {"A": (330, 90), "B": (340, 290), "C": (300, 410), "D": (720, 360), "E": (720, 440), "F": (720, 540)}
MS.lijn(352, 92, 418, 95, DONKER, 1)
MS.lijn(362, 290, 438, 280, DONKER, 1)
MS.lijn(322, 410, 378, 409, DONKER, 1)
MS.lijn(698, 360, 636, 360, DONKER, 1)
MS.lijn(698, 440, 622, 440, DONKER, 1)
MS.lijn(698, 540, 632, 540, DONKER, 1)
for k, (x, y) in LMS.items():
    MS.letter(x, y, k)
ZMS = {"A": [Prent.zone(415, 75, 60, 40), Prent.rond(*LMS["A"], 22)],
       "B": [Prent.zone(435, 240, 60, 80), Prent.rond(*LMS["B"], 22)],
       "C": [Prent.zone(375, 395, 210, 28), Prent.rond(*LMS["C"], 22)],
       "D": [Prent.rond(600, 360, 38), Prent.rond(*LMS["D"], 22)],
       "E": [Prent.rond(600, 440, 24), Prent.rond(*LMS["E"], 22)],
       "F": [Prent.zone(330, 515, 300, 50), Prent.rond(*LMS["F"], 22)],
       "arm": [Prent.zone(500, 170, 100, 350)]}

VRAGEN = [
    klik(
        "Klik op het pictogram dat waarschuwt voor een ontvlambaar product.",
        GP.bestand, ZGP["P"],
        "Een vlam: weg van vuur en warmtebronnen houden.",
    ),
    met_prent(GP.bestand, tabel(
        "Welk pictogram hoort hierbij?",
        [
            ("acuut giftig", "Q"),
            ("bijtend, tast huid en metaal aan", "R"),
            ("kan bij gebruik een bunsenbrander vuur vatten", "P"),
            ("schadelijk of irriterend", "S"),
        ],
        "Het uitroepteken waarschuwt voor een minder ernstig gevaar.",
        kolommen=["P", "Q", "R", "S"],
    )),
    met_prent(GP.bestand, mk(
        "Een fles draagt pictogram R. Wat doe je als je er een spat van in je oog krijgt?",
        [
            "Minutenlang spoelen met de oogdouche",
            "In je oog wrijven tot het niet meer prikt",
            "Wachten tot het vanzelf weer beter gaat",
            "Er een ander product bij gieten om het te neutraliseren",
        ],
        0,
        "Spoelen verdunt en verwijdert het product. Daarna verwittig je de leerkracht.",
    )),
    klik(
        "Klik op de schroef waarmee je bij de grootste vergroting scherpstelt.",
        MS.bestand, ZMS["E"],
        "De fijne stelschroef. Met de grove duw je het objectief door het dekglaasje.",
    ),
    klik(
        "Klik op de twee delen waaraan je de microscoop draagt.",
        MS.bestand, ZMS["arm"] + ZMS["F"],
        "Aan de arm en de voet, nooit aan de buis of de tafel.",
    ),
    met_prent(MS.bestand, tabel(
        "Kijk naar de microscoop. Klopt dit?",
        [
            ("A is het oculair, waar je doorkijkt.", J),
            ("B zijn de objectieven.", J),
            ("Je start altijd met het kortste objectief bij B.", J),
            ("Op C ligt de lamp.", F),
        ],
        "Op C, de tafel, ligt het preparaat. Het kleinste objectief geeft de kleinste vergroting.",
    )),
    tabel(
        "Goed of fout in het labo?",
        [
            ("een warme kolf met een tang vastnemen", J),
            ("met de mond pipetteren", F),
            ("lang haar vastmaken bij de bunsenbrander", J),
            ("een flesje recht onder je neus houden om te ruiken", F),
            ("je handen wassen na het werk met een bacteriekweek", J),
        ],
        "Als je al ruikt, waaier je met je hand wat damp naar je toe.",
    ),
    sorteer(
        "Waar hoort dit afval thuis?",
        ["Afvalvat chemisch afval", "Container biologisch afval", "Glascontainer voor scherven"],
        [
            ("de rest van een afgemeten zuur", "Afvalvat chemisch afval"),
            ("een gebruikte petrischaal met bacteriën", "Container biologisch afval"),
            ("een gebroken bekerglas", "Glascontainer voor scherven"),
            ("dierlijk weefsel na een dissectie", "Container biologisch afval"),
        ],
        "Chemisch afval gaat nooit in de gootsteen: de waterzuivering haalt niet alles weg.",
    ),
    volgorde(
        "Zet de stappen om een preparaat te bekijken in de juiste volgorde.",
        ["Kleinste objectief kiezen", "Preparaat op de tafel leggen", "Scherpstellen met de grove stelschroef", "Groter objectief draaien", "Bijstellen met de fijne stelschroef"],
        "Zo vind je eerst het beeld en vermijd je schade aan lens en preparaat.",
    ),
    casus(
        "Lina moet 2,5 g zout afwegen en 50 ml water afmeten. Ze heeft een balans die tot op 0,1 g weegt en een maatbeker van 500 ml met streepjes per 50 ml.",
        [
            keuze(
                "Voor ze het zout afweegt, zet ze de balans met het schaaltje erop op [[*nul|het maximum|2,5 g]].",
                "Zo weegt ze het schaaltje niet mee.",
            ),
            mk(
                "Waarom kiest ze best een maatcilinder van 100 ml in plaats van de maatbeker?",
                [
                    "Kleiner instrument, nauwkeuriger",
                    "Een maatbeker kan geen koud water bevatten",
                    "Een maatcilinder warmt het water een beetje op",
                    "Een maatbeker meet alleen in gram, niet in ml",
                ],
                0,
                "Kies een instrument dat past bij de grootte van de meting.",
            ),
            tabel(
                "Klopt dit over de balans van Lina?",
                [
                    ("Ze kan 2,5 g onderscheiden van 2,6 g.", J),
                    ("Haar nauwkeurigheid is 0,1 g.", J),
                    ("Ze kan 2,55 g van 2,56 g onderscheiden.", F),
                ],
                "De nauwkeurigheid is de kleinste waarde die je nog onderscheidt.",
            ),
        ],
    ),
    tabel(
        "Waarom draag je dit beschermingsmiddel?",
        [
            ("veiligheidsbril bij verhitten", "Ogen"),
            ("handschoenen bij menselijk weefsel", "Besmetting"),
            ("labojas bij het werken met zuren", "Kledij en huid"),
            ("handschoenen bij een bacteriekweek", "Besmetting"),
        ],
        "Handschoenen voorkomen besmetting in twee richtingen.",
        kolommen=["Ogen", "Besmetting", "Kledij en huid"],
    ),
    tabel(
        "Klopt dit over een pictogram?",
        [
            ("Een product zonder pictogram is altijd volkomen veilig.", F),
            ("Een etiket vertelt ook hoe je het product bewaart.", J),
            ("Je leest het etiket voor je met een product begint.", J),
            ("Een vlam op een ruit betekent: ontvlambaar.", J),
        ],
        "Een ontbrekend pictogram betekent alleen dat die gevaren niet gelden.",
    ),
    mk(
        "Een leerling zet een warme kolf meteen op de koude stenen tafel. Wat kan er gebeuren?",
        [
            "Het glas kan barsten",
            "De tafel neemt de vloeistof uit de kolf op",
            "De vloeistof wordt er meteen giftig door",
            "De kolf wordt magnetisch en trekt aan de tafel",
        ],
        0,
        "Zet warm glas op een hittebestendige onderlaag.",
    ),
    tabel(
        "Duurzaam of niet duurzaam?",
        [
            ("afmeten wat je nodig hebt en niet meer", "Duurzaam"),
            ("een microscooplamp laten branden zonder te kijken", "Niet duurzaam"),
            ("glaswerk na het schoonmaken hergebruiken", "Duurzaam"),
            ("een meettoestel aan laten staan na de proef", "Niet duurzaam"),
        ],
        "Minder product gebruiken geeft ook minder afval en minder risico.",
        kolommen=["Duurzaam", "Niet duurzaam"],
    ),
    koppel(
        "Koppel elke handeling aan de reden waarom je ze doet.",
        [
            ("werkblad ontsmetten voor de proef", "je proef niet laten besmetten"),
            ("werkblad ontsmetten na de proef", "niemand anders laten besmetten"),
            ("meteen noteren wat je meet", "achteraf kunnen nagaan wat er gebeurde"),
            ("glaswerk meteen schoonmaken", "opgedroogde resten vermijden"),
        ],
        ["het product sneller laten koken"],
        "Netjes en veilig werken gaan samen.",
    ),
    keuze(
        "Materiaal volledig kiemvrij maken met stoom onder druk heet [[*steriliseren|ontsmetten|filtreren]].",
        "Ontsmetten doodt veel kiemen, steriliseren alle.",
    ),
    tabel(
        "Klopt dit over werken met een bunsenbrander?",
        [
            ("Geen brandbare stoffen in de buurt.", J),
            ("Losse kledij vastmaken.", J),
            ("De vlam nooit onbewaakt laten branden.", J),
            ("Je buigt over de vlam om beter te zien.", F),
        ],
        "Houd hoofd en haar uit de buurt van de vlam.",
    ),
    mk(
        "Waarom verhit je een vloeistof in een proefbuis nooit met de opening naar iemand toe?",
        [
            "De vloeistof kan opspatten",
            "De proefbuis smelt dan veel sneller dan normaal",
            "Het licht van de vlam verblindt de buur",
            "De vloeistof koelt dan veel te snel af",
        ],
        0,
        "Daarom ook altijd een veiligheidsbril.",
    ),
    tabel(
        "Wat doe je als er glaswerk breekt?",
        [
            ("de scherven met borstel en blik opruimen", J),
            ("de scherven in de glascontainer doen", J),
            ("de scherven met je blote handen oprapen", F),
            ("de leerkracht verwittigen", J),
        ],
        "Zo vermijd je snijwonden.",
    ),
    tabel(
        "Klopt dit over het meetbereik?",
        [
            ("Het zegt tussen welke waarden het instrument betrouwbaar meet.", J),
            ("Buiten het bereik klopt de meting niet meer.", J),
            ("Een thermometer tot 50 °C gebruik je om kokend water te meten.", F),
        ],
        "Kokend water is 100 °C: dat ligt buiten het bereik.",
    ),
    keuze(
        "Water geleidt stroom. Daarom bedien je een elektrisch toestel nooit met [[*natte handen|een labojas|een veiligheidsbril]].",
        "Dat geldt ook voor toestellen naast een kraan.",
    ),
    tabel(
        "Klopt dit over het werken met levende organismen?",
        [
            ("Ze krijgen zo weinig mogelijk ongemak.", J),
            ("Dat is een ethische en een wetenschappelijke keuze.", J),
            ("Een gestreste plant of dier kan je resultaten verstoren.", J),
            ("Levende dieren mag je zonder reden bij een proef betrekken.", F),
        ],
        "Respect voor het leven hoort bij goed onderzoek.",
    ),
    inv(
        "Een thermometer heeft streepjes per 0,5 °C. Wat is de nauwkeurigheid in °C?",
        ["0,5", "0.5"],
        "De kleinste waarde die je nog kunt onderscheiden.",
    ),
    tabel(
        "Klopt dit over het werken met een bacteriekweek?",
        [
            ("De petrischaal blijft gesloten.", J),
            ("Je wast nadien grondig je handen.", J),
            ("De schaal gaat na de proef bij het biologisch afval.", J),
            ("Je ruikt even aan de kweek om te zien of ze groeit.", F),
        ],
        "Kiemen kunnen zo in je lichaam komen.",
    ),
    mk(
        "Tijdens een lange proef heeft Noor honger. Waarom eet ze haar koek niet aan de labotafel?",
        [
            "Producten of kiemen komen zo in haar mond",
            "Het eten verstoort de meting van de balans",
            "De labotafel is veel te hoog om aan te eten",
            "Eten maakt de bunsenbrander naast haar onstabiel",
        ],
        0,
        "Via je handen of een glas komt er zo iets binnen.",
    ),
    tabel(
        "Klopt dit over de nooddouche en de oogdouche?",
        [
            ("Je kijkt voor de proef na waar ze hangen.", J),
            ("Bij een ongeval tellen seconden.", J),
            ("Je zoekt ze pas als er iets gebeurd is.", F),
        ],
        "Dan is er geen tijd meer om te zoeken.",
    ),
    keuze(
        "Voor je met een product begint te werken, lees je altijd eerst het [[*etiket|logboek|verslag]].",
        "Daarop staan de pictogrammen en de veiligheidsvoorschriften.",
    ),
    open_(
        "Leg uit waarom je chemisch afval niet in de gootsteen giet, ook al spoel je met veel water na.",
        "Wat in de gootsteen gaat, komt via de riolering in de waterzuivering en daarna in het oppervlaktewater. De waterzuivering haalt niet alle stoffen eruit. Verdunnen maakt de stof niet onschadelijk, ze komt alleen over een groter gebied terecht. Daarom gaat chemisch afval in het daarvoor voorziene afvalvat.",
    ),
]

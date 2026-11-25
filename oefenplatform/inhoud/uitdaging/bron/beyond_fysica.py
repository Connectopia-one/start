# -*- coding: utf-8 -*-
"""Uitdaging Fysica 🌍 Beyond doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen, van elektrostatica en inductie tot mechanica, trillingen,
golven en kernfysica. Casussen, tabellen, keuzelijsten, koppelen, sorteren,
volgorde, veel rekenvragen, klikvragen op twee zelf getekende prenten (een
trilling en een vervalcurve) en een open onderzoeksvraag. Geen nieuwe
leerstof: alles staat in de hoofdstukken van Fysica Beyond doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_fysica.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Fysica"
BESTAND = "beyond-fysica-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/fysica-beyond-uitdaging"
TRILLING = "trilling-u-t.svg"
VERVAL = "vervalcurve-activiteit.svg"
# klikvakken: zie maak_prenten_beyond_fysica.py
NULDOORGANGEN = [[24.0, 44.7, 6.4, 10.7], [40.2, 44.7, 6.4, 10.7], [56.4, 44.7, 6.4, 10.7], [72.6, 44.7, 6.4, 10.7]]
MINIMA = [[32.1, 71.3, 6.4, 10.7], [64.5, 71.3, 6.4, 10.7]]
KWART = [40.0, 64.1, 6.8, 11.3]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Trilling (prent)
    klik("Bekijk de grafiek van de trilling. Klik op een punt waar de massa haar grootste snelheid heeft.",
         TRILLING, NULDOORGANGEN,
         "De snelheid is het grootst bij de doorgang door de evenwichtsstand, waar de uitwijking nul is. Daar loopt de grafiek het steilst."),
    klik("Klik op een punt waar de uitwijking maximaal negatief is.",
         TRILLING, MINIMA,
         "Op 0,6 s en op 1,4 s bereikt de massa \\(-4\\) cm: het laagste punt. Daar is de snelheid even nul."),
    met_prent(TRILLING, tabel(
        "Lees af en reken uit.",
        [
            ("de amplitude", "\\(4\\) cm"),
            ("de periode", "\\(0{,}8\\) s"),
            ("de frequentie", "\\(1{,}25\\) Hz"),
        ],
        "De amplitude is de grootste uitwijking. Eén volledige trilling duurt van 0 tot 0,8 s. \\(f = 1 / T = 1 / 0{,}8 = 1{,}25\\) Hz.",
        kolommen=["\\(4\\) cm", "\\(0{,}8\\) s", "\\(1{,}25\\) Hz"])),
    met_prent(TRILLING, mk(
        "Welke vergelijking hoort bij deze trilling, met u in cm en t in s?",
        ["\\(u = 4\\sin(2{,}5\\pi t)\\)", "\\(u = 4\\sin(0{,}8\\pi t)\\)", "\\(u = 8\\sin(2{,}5\\pi t)\\)", "\\(u = 4\\cos(2{,}5\\pi t)\\)"],
        0,
        "\\(\\omega = 2\\pi / T = 2\\pi / 0{,}8 = 2{,}5\\pi\\) rad/s. De trilling start in de evenwichtsstand en gaat omhoog: een sinus met amplitude 4.")),

    # Vervalcurve (prent)
    klik("Bekijk de vervalcurve. Klik op het punt waar de activiteit gedaald is tot een kwart van de beginwaarde.",
         VERVAL, [KWART],
         "De beginactiviteit is 800 Bq. Een kwart is 200 Bq, en die waarde bereikt de bron na 12 uur."),
    met_prent(VERVAL, inv(
        "Hoeveel uur bedraagt de halveringstijd van deze stof? Geef enkel het getal.",
        "6",
        "Na 6 uur is de activiteit gedaald van 800 naar 400 Bq: de helft.")),
    met_prent(VERVAL, inv(
        "Hoe groot is de activiteit na 18 uur, in becquerel? Geef enkel het getal.",
        "100",
        "18 uur is drie halveringstijden: \\(800 \\cdot \\left(\\tfrac{1}{2}\\right)^{3} = 100\\) Bq.")),
    met_prent(VERVAL, tabel(
        "Klopt dit over radioactief verval?",
        [
            ("Na twee halveringstijden is er niets meer van de stof over.", F),
            ("Je kan niet voorspellen wanneer één bepaalde kern vervalt.", J),
            ("De halveringstijd hangt af van de temperatuur van de bron.", F),
            ("Elke halveringstijd daalt de activiteit met dezelfde factor.", J),
        ],
        "Na twee halveringstijden blijft er een kwart over. Verval is een toevalsproces per kern, maar voor veel kernen samen volgt het een vaste exponentiële wet. Temperatuur heeft er geen invloed op.")),

    # Elektrostatica
    inv("Twee puntladingen van elk \\(2{,}0\\ \\mu\\text{C}\\) liggen \\(0{,}30\\) m van elkaar. Hoe groot is de kracht tussen hen, in newton? Neem \\(k = 8{,}99 \\cdot 10^{9}\\ \\text{N\\,m}^{2}/\\text{C}^{2}\\) en rond af op twee decimalen.",
        ["0,40", "0,4", "0.40", "0.4"],
        "\\(F = k\\dfrac{q_1 q_2}{r^{2}} = 8{,}99 \\cdot 10^{9} \\cdot \\dfrac{(2{,}0 \\cdot 10^{-6})^{2}}{0{,}30^{2}} \\approx 0{,}40\\) N."),
    keuze(
        "Als je de afstand tussen twee ladingen verdubbelt, wordt de kracht [[*vier keer kleiner|twee keer kleiner|twee keer groter]]. Elektrische veldlijnen vertrekken bij een [[*positieve|negatieve]] lading.",
        "De wet van Coulomb is omgekeerd evenredig met het kwadraat van de afstand. Veldlijnen wijzen in de zin van de kracht op een positieve proeflading: van plus naar min."),
    mk("Een elektron doorloopt een spanning van \\(100\\) V. Hoeveel kinetische energie wint het?",
       ["\\(100\\) eV", "\\(1\\) eV", "\\(100\\) J", "\\(1{,}6\\) J"],
       0,
       "\\(W = q \\cdot U\\). Voor een elektron is dat \\(e \\cdot 100\\) V, dus 100 elektronvolt, of \\(1{,}6 \\cdot 10^{-17}\\) J."),

    # Schakelingen
    casus(
        "Een weerstand van \\(6\\,\\Omega\\) staat in serie met twee parallelle weerstanden van \\(6\\,\\Omega\\) en \\(3\\,\\Omega\\). Het geheel hangt aan een bron van \\(24\\) V.",
        [
            tabel(
                "Reken uit.",
                [
                    ("de vervangingsweerstand van het parallelle deel, in Ω", "\\(2\\)"),
                    ("de vervangingsweerstand van de hele kring, in Ω", "\\(8\\)"),
                    ("de stroom uit de bron, in A", "\\(3\\)"),
                    ("de spanning over het parallelle deel, in V", "\\(6\\)"),
                ],
                "\\(1/R = 1/6 + 1/3 = 1/2\\), dus \\(2\\,\\Omega\\). In serie: \\(6 + 2 = 8\\,\\Omega\\). \\(I = 24/8 = 3\\) A. Over het parallelle deel: \\(U = 3 \\cdot 2 = 6\\) V.",
                kolommen=["\\(2\\)", "\\(3\\)", "\\(6\\)", "\\(8\\)"]),
            inv("Hoeveel ampère loopt er door de weerstand van \\(3\\,\\Omega\\)? Geef enkel het getal.",
                "2",
                "Over het parallelle deel staat 6 V. \\(I = 6 / 3 = 2\\) A. Door de weerstand van \\(6\\,\\Omega\\) loopt de overige 1 A."),
        ],
    ),

    # Magnetisme en inductie
    inv("Een rechte geleider van \\(0{,}20\\) m voert een stroom van \\(4{,}0\\) A loodrecht door een magnetisch veld van \\(0{,}50\\) T. Hoe groot is de kracht erop, in newton? Geef enkel het getal.",
        ["0,4", "0,40", "0.4", "0.40"],
        "\\(F = B \\cdot I \\cdot L = 0{,}50 \\cdot 4{,}0 \\cdot 0{,}20 = 0{,}40\\) N."),
    inv("De flux door een spoel met \\(100\\) windingen verandert in \\(0{,}020\\) s gelijkmatig met \\(0{,}060\\) Wb. Hoe groot is de inductiespanning, in volt? Geef enkel het getal.",
        "300",
        "Volgens Faraday is \\(U = N \\dfrac{\\Delta\\Phi}{\\Delta t} = 100 \\cdot \\dfrac{0{,}060}{0{,}020} = 300\\) V."),
    inv("Een transformator heeft \\(1200\\) windingen primair en \\(60\\) windingen secundair. Hij hangt aan \\(230\\) V. Hoeveel volt geeft hij secundair? Geef enkel het getal.",
        ["11,5", "11.5"],
        "\\(U_s / U_p = N_s / N_p\\), dus \\(U_s = 230 \\cdot 60 / 1200 = 11{,}5\\) V."),
    keuze(
        "Volgens de wet van [[*Lenz|Coulomb|Ohm]] werkt de inductiestroom de oorzaak van haar ontstaan [[*tegen|in de hand]]. Een generator met een draaiende winding levert [[*wisselspanning|gelijkspanning]].",
        "Een magneet die je in een spoel duwt, krijgt een tegenwerkende kracht. Een draaiende winding ziet de flux periodiek veranderen: dat geeft een wisselspanning."),

    # Mechanica
    inv("Een auto van \\(1200\\) kg remt gelijkmatig van \\(20\\) m/s tot stilstand in \\(4{,}0\\) s. Hoe groot is de remkracht, in newton? Geef enkel het getal.",
        ["6000", "6 000", "6.000"],
        "\\(a = \\Delta v / \\Delta t = -20 / 4{,}0 = -5{,}0\\) m/s². \\(F = m \\cdot a = 1200 \\cdot 5{,}0 = 6000\\) N, tegen de beweging in."),
    casus(
        "Een bal rolt met \\(12\\) m/s horizontaal van een rots van \\(45\\) m hoog. Neem \\(g = 10\\) m/s² en verwaarloos de luchtweerstand.",
        [
            inv("Hoeveel seconden duurt de val? Geef enkel het getal.",
                "3",
                "Verticaal is het een vrije val: \\(45 = \\tfrac{1}{2} \\cdot 10 \\cdot t^{2}\\), dus \\(t^{2} = 9\\) en \\(t = 3\\) s."),
            inv("Hoeveel meter van de voet van de rots komt de bal neer? Geef enkel het getal.",
                "36",
                "Horizontaal blijft de snelheid constant: \\(x = 12 \\cdot 3 = 36\\) m."),
            mk("Hoe groot is de verticale snelheid bij de landing?",
               ["\\(30\\) m/s", "\\(12\\) m/s", "\\(45\\) m/s", "\\(15\\) m/s"],
               0,
               "\\(v_y = g \\cdot t = 10 \\cdot 3 = 30\\) m/s. De horizontale snelheid blijft 12 m/s."),
        ],
    ),
    inv("Een auto van \\(1000\\) kg rijdt met \\(20\\) m/s door een bocht met een straal van \\(50\\) m. Hoe groot is de middelpuntzoekende kracht, in newton? Geef enkel het getal.",
        ["8000", "8 000", "8.000"],
        "\\(F_c = m \\dfrac{v^{2}}{r} = 1000 \\cdot \\dfrac{400}{50} = 8000\\) N."),
    tabel(
        "Welke wet van Newton verklaart dit het best?",
        [
            ("Een passagier schiet naar voren als de bus plots remt.", "Eerste wet"),
            ("Een zwaardere kar heeft meer kracht nodig voor dezelfde versnelling.", "Tweede wet"),
            ("Een roeier duwt water naar achter en de boot gaat vooruit.", "Derde wet"),
        ],
        "Traagheid is de eerste wet. \\(F = m \\cdot a\\) is de tweede. Actie en reactie zijn de derde wet.",
        kolommen=["Eerste wet", "Tweede wet", "Derde wet"]),
    inv("Een steen valt vanuit rust \\(5{,}0\\) m naar beneden. Met welke snelheid raakt hij de grond, in m/s? Neem \\(g = 9{,}81\\) m/s², verwaarloos de luchtweerstand en rond af op één decimaal.",
        ["9,9", "9.9"],
        "Behoud van energie: \\(mgh = \\tfrac{1}{2}mv^{2}\\), dus \\(v = \\sqrt{2gh} = \\sqrt{2 \\cdot 9{,}81 \\cdot 5{,}0} \\approx 9{,}9\\) m/s."),
    mk("Wat gebeurt er met de gravitatiekracht tussen twee hemellichamen als de afstand drie keer zo groot wordt?",
       ["Ze wordt negen keer kleiner.", "Ze wordt maar drie keer kleiner.", "Ze wordt negen keer groter.", "Ze blijft gewoon even groot."],
       0,
       "De gravitatiekracht is omgekeerd evenredig met het kwadraat van de afstand: \\(3^{2} = 9\\)."),

    mk("Een proton beweegt met een constante snelheid loodrecht op een homogeen magnetisch veld. Welke baan beschrijft het?",
       ["een cirkel", "een rechte lijn", "een parabool", "een spiraal naar buiten"],
       0,
       "De lorentzkracht staat altijd loodrecht op de snelheid. Ze verandert enkel de richting, niet de grootte van de snelheid: het proton beschrijft een cirkel."),
    inv("Je trekt een slee \\(10\\) m vooruit met een kracht van \\(50\\) N onder een hoek van \\(60^{\\circ}\\) met de grond. Hoeveel arbeid verricht je, in joule? Geef enkel het getal.",
        "250",
        "Enkel de component in de zin van de verplaatsing verricht arbeid: \\(W = F \\cdot s \\cdot \\cos\\alpha = 50 \\cdot 10 \\cdot 0{,}5 = 250\\) J."),
    tabel(
        "Klopt dit over een lichaam in evenwicht?",
        [
            ("De resulterende kracht op het lichaam is nul.", J),
            ("De som van de momenten om elk punt is nul.", J),
            ("Een lichaam in evenwicht staat altijd stil.", F),
        ],
        "Voor evenwicht moeten zowel de krachten als de momenten elkaar opheffen. Een lichaam dat eenparig rechtlijnig beweegt, is ook in evenwicht."),

    # Gassen en warmte
    inv("\\(2{,}0\\) mol gas zit bij \\(300\\) K in een vat van \\(0{,}050\\) m³. Hoe groot is de druk, in kPa? Neem \\(R = 8{,}31\\) J/(mol·K) en rond af op één decimaal.",
        ["99,7", "99.7"],
        "\\(p = \\dfrac{nRT}{V} = \\dfrac{2{,}0 \\cdot 8{,}31 \\cdot 300}{0{,}050} = 99\\,720\\) Pa, of 99,7 kPa."),
    inv("Je mengt \\(1{,}0\\) kg water van \\(80\\) °C met \\(3{,}0\\) kg water van \\(20\\) °C. Wat is de eindtemperatuur, in °C, als er geen warmte verloren gaat? Geef enkel het getal.",
        "35",
        "Warmtebalans: \\(1{,}0 \\cdot (80 - T) = 3{,}0 \\cdot (T - 20)\\), dus \\(80 - T = 3T - 60\\) en \\(T = 35\\) °C."),

    # Golven, licht en kwantum
    inv("Een geluidsgolf van \\(680\\) Hz loopt met \\(340\\) m/s door de lucht. Hoe groot is de golflengte, in meter? Geef enkel het getal.",
        ["0,5", "0,50", "0.5", "0.50"],
        "\\(\\lambda = v / f = 340 / 680 = 0{,}50\\) m."),
    volgorde(
        "Zet deze soorten elektromagnetische straling van kleine naar grote frequentie.",
        ["radiogolven", "microgolven", "infrarood", "zichtbaar licht", "ultraviolet", "röntgenstraling", "gammastraling"],
        "Hoe groter de frequentie, hoe kleiner de golflengte en hoe groter de energie per foton."),
    tabel(
        "Klopt dit over het foto-elektrisch effect?",
        [
            ("Onder de grensfrequentie komen er geen elektronen vrij, ook niet bij fel licht.", J),
            ("Feller licht met dezelfde frequentie maakt meer elektronen vrij.", J),
            ("Feller licht geeft de vrijgekomen elektronen meer kinetische energie.", F),
            ("Licht gedraagt zich hier als een stroom van deeltjes, fotonen.", J),
        ],
        "De energie van één foton is \\(E = hf\\) en hangt enkel van de frequentie af. Meer intensiteit betekent meer fotonen, dus meer elektronen, maar niet sneller. Dat toont het deeltjeskarakter van licht."),
    keuze(
        "Bij [[*interferentie|breking|polarisatie]] versterken of verzwakken twee golven elkaar. Op een gespannen snaar ontstaat zo een [[*staande golf|lopende golf]] met knopen en buiken.",
        "Golven tellen op waar ze elkaar ontmoeten. Een golf die heen en weer weerkaatst, kan een staande golf vormen."),

    # Kernfysica
    tabel(
        "Wat gebeurt er met de kern bij dit verval?",
        [
            ("alfaverval", "Massagetal min 4, atoomnummer min 2"),
            ("bèta-minverval", "Atoomnummer plus 1, massagetal gelijk"),
            ("gammaverval", "Beide getallen blijven gelijk"),
        ],
        "Een alfadeeltje is een heliumkern: 2 protonen en 2 neutronen. Bij bèta-min wordt een neutron een proton en komt er een elektron vrij. Gammastraling voert enkel energie af.",
        kolommen=["Massagetal min 4, atoomnummer min 2", "Atoomnummer plus 1, massagetal gelijk", "Beide getallen blijven gelijk"]),
    inv("Uranium-238 vervalt met een alfaverval. Welk massagetal heeft de kern die ontstaat? Geef enkel het getal.",
        "234",
        "Bij alfaverval verliest de kern 4 nucleonen: \\(238 - 4 = 234\\). Het wordt thorium-234."),
    sorteer(
        "Hoort dit bij kernsplijting of bij kernfusie?",
        ["Kernsplijting", "Kernfusie"],
        [
            ["een zware kern valt uiteen in twee lichtere kernen", "Kernsplijting"],
            ["de energiebron van de zon", "Kernfusie"],
            ["een kettingreactie met neutronen", "Kernsplijting"],
            ["lichte kernen smelten samen tot een zwaardere", "Kernfusie"],
            ["de werking van een kerncentrale vandaag", "Kernsplijting"],
        ],
        "Bij splijting breekt een zware kern zoals uranium, bij fusie versmelten lichte kernen zoals waterstof. In beide gevallen komt energie vrij door het massadefect."),
    sleep(
        "Je beschermt je tegen straling door de [[afstand]] tot de bron groot te maken, de [[tijd]] in de buurt kort te houden en voor [[afscherming]] te zorgen, zoals een loden wand.",
        ["temperatuur", "frequentie"],
        "Afstand, tijd en afscherming zijn de drie basisregels van stralingsbescherming."),

    # Meten en onderzoek
    tabel(
        "Klopt dit over meten?",
        [
            ("Een meetresultaat geef je met een onzekerheid en een eenheid.", J),
            ("Door een meting te herhalen, verklein je toevallige fouten.", J),
            ("Een systematische fout verdwijnt als je het gemiddelde neemt.", F),
            ("Een digitaal toestel meet altijd exact.", F),
        ],
        "Toevallige fouten middelen uit, een systematische fout (een verkeerd geijkt toestel) niet. Ook een digitaal toestel heeft een beperkte nauwkeurigheid."),
    open_("Je wil onderzoeken of de periode van een slinger afhangt van de massa die eraan hangt. Beschrijf je proefopzet: wat verander je, wat meet je, wat houd je constant en hoe maak je je meting nauwkeurig?",
          "Ik verander de massa (bijvoorbeeld 50, 100, 150 en 200 g). Ik meet de periode. Ik houd de lengte van de slinger en de beginuitwijking (klein, minder dan tien graden) constant. Om nauwkeurig te meten, meet ik de tijd van tien slingeringen en deel ik door tien, en herhaal ik elke meting drie keer. Daarna zet ik de periode uit tegen de massa in een grafiek.",
          "Een goed antwoord verandert één grootheid, houdt de andere constant, meet meerdere perioden tegelijk om de reactietijd te verkleinen en herhaalt de metingen."),
]

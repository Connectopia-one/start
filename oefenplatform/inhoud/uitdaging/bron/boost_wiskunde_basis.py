# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde basis 🚀 Boost doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een rechte met vijf punten en een rechthoekige driehoek om
op te klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in
de hoofdstukken van Wiskunde basis Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_wiskunde_basis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Wiskunde basis"
BESTAND = "boost-wiskunde-basis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-basis-boost-uitdaging"
RECHTE = "rechte-vijf-punten.svg"
DRIEHOEK = "rechthoekige-driehoek.svg"

# klikvakken uit maak_prenten_boost_wiskunde_basis.py
PT = {1: [27.1, 71.2, 7.9, 7.5], 2: [40.8, 45.2, 7.9, 7.5], 3: [54.5, 19.2, 7.9, 7.5],
      4: [20.3, 84.2, 7.9, 7.5], 5: [61.3, 32.2, 7.9, 7.5]}
ZIJDE = {"AB": [15.0, 78.0, 60.0, 9.0], "BC": [71.0, 16.7, 8.0, 66.7],
         "AC": [[17.0, 63.0, 16.0, 18.3], [37.0, 40.8, 16.0, 18.3], [57.0, 18.7, 16.0, 18.3]]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Rechte (prent)
    klik("Bekijk de grafiek van \\(f\\). Klik op het punt dat de nulwaarde van \\(f\\) toont.",
         RECHTE, [PT[2]],
         "De nulwaarde is de \\(x\\)-waarde waar de grafiek de \\(x\\)-as snijdt: in punt 2, bij \\(x = 2\\)."),
    klik("Klik op het snijpunt van de grafiek met de \\(y\\)-as.",
         RECHTE, [PT[1]],
         "Op de \\(y\\)-as is \\(x = 0\\). De grafiek snijdt de \\(y\\)-as in \\((0, -4)\\), punt 1."),
    klik("Eén genummerd punt ligt niet op de grafiek van \\(f\\). Klik erop.",
         RECHTE, [PT[5]],
         "Punt 5 is \\((5, 2)\\). Maar \\(f(5) = 2 \\cdot 5 - 4 = 6\\), dus het punt ligt niet op de rechte."),
    met_prent(RECHTE, inv(
        "Bereken de richtingscoëfficiënt van \\(f\\) met de punten 2 en 3. Een getal.",
        ["2"],
        "Punt 2 is \\((2, 0)\\) en punt 3 is \\((4, 4)\\). \\(a = \\frac{4 - 0}{4 - 2} = 2\\).")),
    met_prent(RECHTE, keuze(
        "Het voorschrift van \\(f\\) is [[*\\(f(x) = 2x - 4\\)|\\(f(x) = -4x + 2\\)|\\(f(x) = 2x + 4\\)]]. De functie is positief voor [[*\\(x > 2\\)|\\(x < 2\\)]].",
        "De richtingscoëfficiënt is 2 en het snijpunt met de \\(y\\)-as is \\(-4\\). De stijgende rechte ligt boven de \\(x\\)-as rechts van de nulwaarde.")),

    # Driehoek (prent)
    klik("Bekijk de rechthoekige driehoek \\(ABC\\). Klik op de schuine zijde.",
         DRIEHOEK, ZIJDE["AC"],
         "De schuine zijde ligt tegenover de rechte hoek bij \\(B\\): dat is \\([AC]\\), de langste zijde."),
    klik("Klik op de overstaande rechthoekszijde van hoek \\(\\alpha\\).",
         DRIEHOEK, [ZIJDE["BC"]],
         "De overstaande zijde ligt tegenover \\(\\alpha\\): dat is \\([BC]\\), met lengte 6 cm."),
    met_prent(DRIEHOEK, inv(
        "Hoe lang is de schuine zijde \\([AC]\\) in cm? Een getal.",
        ["10"],
        "Pythagoras: \\(|AC|^{2} = 8^{2} + 6^{2} = 64 + 36 = 100\\), dus \\(|AC| = 10\\) cm.")),
    met_prent(DRIEHOEK, tabel(
        "Klopt dit voor hoek \\(\\alpha\\) in de driehoek?",
        [
            ("\\(\\sin \\alpha = 0{,}6\\)", J),
            ("\\(\\cos \\alpha = 0{,}8\\)", J),
            ("\\(\\tan \\alpha = \\frac{4}{3}\\)", F),
        ],
        "\\(\\sin \\alpha = \\frac{6}{10}\\), \\(\\cos \\alpha = \\frac{8}{10}\\) en \\(\\tan \\alpha = \\frac{6}{8} = \\frac{3}{4}\\).")),

    # Getallen
    tabel(
        "Tot welke kleinste getallenverzameling hoort dit getal?",
        [
            ("\\(-5\\)", "\\(\\mathbb{Z}\\)"),
            ("\\(\\frac{3}{4}\\)", "\\(\\mathbb{Q}\\)"),
            ("\\(\\sqrt{2}\\)", "\\(\\mathbb{R}\\)"),
            ("\\(12\\)", "\\(\\mathbb{N}\\)"),
        ],
        "Natuurlijke getallen zitten in \\(\\mathbb{N}\\), negatieve gehele in \\(\\mathbb{Z}\\), breuken in \\(\\mathbb{Q}\\) en \\(\\sqrt{2}\\) is irrationaal, dus enkel reëel.",
        kolommen=["\\(\\mathbb{N}\\)", "\\(\\mathbb{Z}\\)", "\\(\\mathbb{Q}\\)", "\\(\\mathbb{R}\\)"]),
    inv("Bereken \\(\\frac{2^{5} \\cdot 2^{3}}{2^{6}}\\). Een getal.",
        ["4"],
        "\\(2^{5 + 3 - 6} = 2^{2} = 4\\)."),
    mk("Welke schrijfwijze is gelijk aan \\(\\sqrt{50}\\)?",
       ["\\(5\\sqrt{2}\\)", "\\(25\\sqrt{2}\\)", "\\(2\\sqrt{5}\\)", "\\(10\\sqrt{5}\\)"],
       0,
       "\\(\\sqrt{50} = \\sqrt{25 \\cdot 2} = 5\\sqrt{2}\\)."),

    # Intervallen en ongelijkheden
    koppel(
        "Koppel de ongelijkheid aan het interval.",
        [
            ["\\(2 < x < 5\\)", "\\(\\left]2, 5\\right[\\)"],
            ["\\(2 \\leq x \\leq 5\\)", "\\(\\left[2, 5\\right]\\)"],
            ["\\(x \\geq 2\\)", "\\(\\left[2, +\\infty\\right[\\)"],
        ],
        ["\\(\\left]-\\infty, 2\\right]\\)"],
        "Een grens die erbij hoort, krijgt een gesloten haakje. Aan de kant van oneindig staat het haakje altijd open."),
    inv("Los op: \\(-2x + 6 > 0\\). Vul in: \\(x < \\) …",
        ["3"],
        "\\(-2x > -6\\). Delen door \\(-2\\) keert het teken om: \\(x < 3\\)."),

    # Logica
    tabel(
        "Neem \\(p\\) waar en \\(q\\) vals. Wat is de waarheidswaarde?",
        [
            ("\\(p \\wedge q\\)", F),
            ("\\(p \\vee q\\)", J),
            ("\\(p \\Rightarrow q\\)", F),
            ("\\(\\neg q\\)", J),
        ],
        "Een conjunctie is enkel waar als beide waar zijn. Een disjunctie is waar als minstens één waar is. Een implicatie is enkel vals als \\(p\\) waar en \\(q\\) vals is."),
    keuze(
        "Een waarheidstabel met drie uitspraken heeft [[*8|6|4]] rijen. Een uitspraak die altijd waar is, heet een [[*tautologie|contradictie]].",
        "Met \\(n\\) uitspraken heeft de tabel \\(2^{n}\\) rijen: \\(2^{3} = 8\\)."),
    mk("Iemand beweert: voor elk getal \\(a\\) geldt \\(a^{2} > a\\). Welk getal is een tegenvoorbeeld?",
       ["\\(\\frac{1}{2}\\)", "\\(\\frac{7}{2}\\)", "\\(-\\frac{5}{2}\\)", "\\(\\sqrt{10}\\)"],
       0,
       "\\(\\left(\\frac{1}{2}\\right)^{2} = \\frac{1}{4}\\) en dat is kleiner dan \\(\\frac{1}{2}\\). Eén tegenvoorbeeld volstaat om de bewering te weerleggen."),

    # Ruimte en vectoren
    keuze(
        "Twee rechten in de ruimte die elkaar niet snijden en niet evenwijdig zijn, heten [[*kruisend|snijdend]]. Een vector heeft een richting, een zin en een [[*grootte|kleur]].",
        "In de ruimte kunnen rechten ook kruisen: ze liggen niet in hetzelfde vlak."),
    inv("Twee krachten van 5 N en 3 N werken in dezelfde richting en zin. Hoe groot is de som in N?",
        ["8"],
        "Dezelfde richting en zin: de groottes tellen op, \\(5 + 3 = 8\\) N."),

    # Schaal en gelijkvormigheid
    inv("Twee gelijkvormige kubussen hebben gelijkvormigheidsfactor \\(k = 2\\). Met welke factor vermenigvuldigt het volume?",
        ["8"],
        "Het volume vermenigvuldigt met \\(k^{3} = 2^{3} = 8\\)."),
    inv("Een stok van 1 m geeft een schaduw van 2 m. Een boom geeft op hetzelfde moment een schaduw van 14 m. Hoe hoog is de boom in m?",
        ["7"],
        "De driehoeken zijn gelijkvormig: \\(\\frac{1}{2} = \\frac{h}{14}\\), dus \\(h = 7\\) m."),

    # Formules
    koppel(
        "Koppel de formule aan de omgevormde vorm.",
        [
            ["\\(\\rho = \\frac{m}{V}\\), druk \\(m\\) uit", "\\(m = \\rho \\cdot V\\)"],
            ["\\(U = I \\cdot R\\), druk \\(I\\) uit", "\\(I = \\frac{U}{R}\\)"],
            ["\\(P = \\frac{E}{t}\\), druk \\(t\\) uit", "\\(t = \\frac{E}{P}\\)"],
        ],
        ["\\(t = P \\cdot E\\)"],
        "Je doet aan beide kanten dezelfde bewerking tot de gevraagde letter alleen staat."),

    # Vergelijkingen en stelsels
    inv("Los op: \\(3(x - 2) = 2x + 5\\). Een getal.",
        ["11"],
        "\\(3x - 6 = 2x + 5\\), dus \\(x = 11\\)."),
    mk("Wat is de oplossing van het stelsel \\(\\begin{cases} x + y = 12 \\\\ x - y = 4 \\end{cases}\\)?",
       ["\\(x = 8\\) en \\(y = 4\\)", "\\(x = 4\\) en \\(y = 8\\)", "\\(x = 6\\) en \\(y = 6\\)", "\\(x = 16\\) en \\(y = 4\\)"],
       0,
       "Optellen geeft \\(2x = 16\\), dus \\(x = 8\\) en \\(y = 4\\). Controle: \\(8 - 4 = 4\\)."),
    keuze(
        "Twee rechten met dezelfde richtingscoëfficiënt en een ander snijpunt met de \\(y\\)-as zijn [[*evenwijdig|samenvallend]]. Het stelsel is dan [[*strijdig|onbepaald]].",
        "Evenwijdige rechten hebben geen snijpunt: er is geen oplossing."),

    # Tweede graad
    tabel(
        "Klopt dit merkwaardig product?",
        [
            ("\\((x + 3)^{2} = x^{2} + 6x + 9\\)", J),
            ("\\((x - 5)^{2} = x^{2} - 25\\)", F),
            ("\\((x + 2)(x - 2) = x^{2} - 4\\)", J),
        ],
        "\\((x - 5)^{2} = x^{2} - 10x + 25\\). Het verschil van twee kwadraten komt uit \\((a + b)(a - b)\\)."),
    inv("Bereken de discriminant van \\(x^{2} - 6x + 5\\). Een getal.",
        ["16"],
        "\\(D = b^{2} - 4ac = 36 - 20 = 16\\)."),
    mk("Wat zijn de oplossingen van \\(x^{2} - 6x + 5 = 0\\)?",
       ["\\(x = 1\\) of \\(x = 5\\)", "\\(x = -1\\) of \\(x = -5\\)", "\\(x = 2\\) of \\(x = 3\\)", "\\(x = 6\\) of \\(x = 5\\)"],
       0,
       "\\(x = \\frac{6 \\pm 4}{2}\\), dus 5 of 1. Ontbinden kan ook: \\((x - 1)(x - 5) = 0\\)."),

    # Functies en parabool
    keuze(
        "De top van \\(f(x) = (x - 3)^{2} + 2\\) ligt in [[*\\((3, 2)\\)|\\((-3, 2)\\)|\\((2, 3)\\)]]. De parabool heeft een [[*minimum|maximum]].",
        "Bij \\(f(x) = (x - p)^{2} + q\\) ligt de top in \\((p, q)\\). De parabool opent naar boven, dus de top is een minimum."),
    inv("Gegeven \\(f(x) = x^{2} - 2x\\). Bereken \\(f(-3)\\). Een getal.",
        ["15"],
        "\\(f(-3) = 9 + 6 = 15\\)."),
    sorteer(
        "Opent deze parabool naar boven of naar beneden?",
        ["Naar boven", "Naar beneden"],
        [
            ["\\(f(x) = 2x^{2} - 1\\)", "Naar boven"],
            ["\\(f(x) = -x^{2} + 4\\)", "Naar beneden"],
            ["\\(f(x) = (x + 1)^{2}\\)", "Naar boven"],
            ["\\(f(x) = -3(x - 2)^{2} + 5\\)", "Naar beneden"],
        ],
        "Het teken van de coëfficiënt van \\(x^{2}\\) bepaalt het: positief opent naar boven, negatief naar beneden."),

    # Tellen
    inv("Je kiest uit 4 voorgerechten, 3 hoofdgerechten en 2 desserts. Hoeveel verschillende menu's zijn er?",
        ["24"],
        "Met een boomdiagram: \\(4 \\cdot 3 \\cdot 2 = 24\\)."),
    inv("In een klas doen 14 kinderen aan voetbal, 10 aan zwemmen en 5 aan beide. Hoeveel kinderen doen minstens één van de twee sporten?",
        ["19"],
        "Met een venndiagram: \\(14 + 10 - 5 = 19\\). Wie beide doet, tel je anders dubbel."),

    # Statistiek
    tabel(
        "De gegevens zijn 3, 5, 5, 7, 10. Klopt dit?",
        [
            ("Het gemiddelde is 6.", J),
            ("De mediaan is 5.", J),
            ("De modus is 7.", F),
            ("Het bereik is 7.", J),
        ],
        "Gemiddelde \\(= \\frac{30}{5} = 6\\). De middelste waarde is 5. De modus is 5, want die komt het vaakst voor. Bereik \\(= 10 - 3 = 7\\)."),
    keuze(
        "Een correlatiecoëfficiënt \\(r\\) dicht bij \\(-1\\) wijst op een sterk [[*dalend|stijgend]] lineair verband. Een sterke correlatie bewijst [[*niet|altijd]] dat het ene het andere veroorzaakt.",
        "Een negatieve \\(r\\) betekent: als de ene grootheid stijgt, daalt de andere. Correlatie is geen oorzakelijk verband."),


    # Extra examenvormen
    volgorde(
        "Zet deze getallen van klein naar groot.",
        ["\\(-\\sqrt{5}\\)", "\\(-\\frac{3}{2}\\)", "\\(0{,}7\\)", "\\(\\frac{3}{4}\\)", "\\(\\sqrt{3}\\)"],
        "\\(-\\sqrt{5} \\approx -2{,}24\\), \\(-\\frac{3}{2} = -1{,}5\\), \\(\\frac{3}{4} = 0{,}75\\) en \\(\\sqrt{3} \\approx 1{,}73\\)."),
    sleep(
        "Bij een boxplot ligt de helft van de gegevens tussen het eerste en het derde [[kwartiel]]. De lijn in het doosje toont de [[mediaan]].",
        ["modus", "gemiddelde"],
        "Het doosje loopt van \\(Q_{1}\\) tot \\(Q_{3}\\) en bevat de middelste helft. De streep in het doosje is \\(Q_{2}\\), de mediaan."),
    casus(
        "Een bioscoop verkoopt kaartjes voor kinderen en volwassenen. Op een middag zijn er 50 bezoekers. Een kinderkaartje kost 6 euro, een volwassenenkaartje 10 euro. Samen brengen ze 380 euro op.",
        [
            inv("Hoeveel kinderen kwamen er naar de film?",
                ["30"],
                "Stel \\(k + v = 50\\) en \\(6k + 10v = 380\\). Uit de eerste: \\(v = 50 - k\\). Invullen: \\(6k + 500 - 10k = 380\\), dus \\(k = 30\\)."),
            inv("Hoeveel volwassenen kwamen er naar de film?",
                ["20"],
                "\\(v = 50 - 30 = 20\\). Controle: \\(6 \\cdot 30 + 10 \\cdot 20 = 380\\)."),
        ]),

    # Schrijfopdracht
    open_("Een fietsenverhuur rekent 5 euro vaste kost plus 3 euro per uur. Stel een voorschrift op voor de prijs \\(p\\) in functie van het aantal uren \\(u\\), bereken de prijs voor 4 uur en leg uit wat de richtingscoëfficiënt hier betekent.",
          "Het voorschrift is \\(p(u) = 3u + 5\\). Voor 4 uur betaal je \\(p(4) = 3 \\cdot 4 + 5 = 17\\) euro. De richtingscoëfficiënt is 3: elk extra uur kost 3 euro meer. Het getal 5 is het snijpunt met de verticale as: wat je betaalt bij 0 uur, de vaste kost.",
          "Een goed antwoord geeft het voorschrift, de juiste berekening (17 euro) en de betekenis van 3 als prijs per extra uur."),
]

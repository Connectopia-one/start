# -*- coding: utf-8 -*-
"""Uitdaging wiskunde 🌱 Start: alle domeinen door elkaar, met een tussenstap.

Geen nieuwe leerstof: elke vraag staat op wat in de gewone hoofdstukken al aan
bod komt, maar vraagt twee stappen, een omgekeerde redenering of een besluit.
"""
NIVEAU = "start"
VAK = "Wiskunde"
BESTAND = "start-wiskunde-uitdaging.json"

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": r"Een fiets kost \(240\) euro. In de solden gaat er eerst \(25\,\%\) af, en van die nieuwe prijs gaat er nog eens \(10\,\%\) af. Wat betaal je?",
        "opties": [r"\(156\) euro", r"\(162\) euro", r"\(168\) euro", r"\(180\) euro"],
        "antwoord": 1,
        "reken": "240 * 0.75 * 0.9",
        "uitleg": r"Eerst \(25\,\%\) van \(240\) eraf: dat is \(60\) euro, dus \(180\) euro. Daarna \(10\,\%\) van \(180\) eraf: dat is \(18\) euro. Je betaalt \(162\) euro.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Eerst \(25\,\%\) korting en daarna nog eens \(10\,\%\) korting is hetzelfde als in één keer \(35\,\%\) korting.",
        "antwoord": False,
        "uitleg": r"Niet waar. De tweede korting rekent op de nieuwe, lagere prijs. Bij \(240\) euro betaal je zo \(162\) euro, en met \(35\,\%\) ineens \(156\) euro.",
    },
    {
        "type": "invultekst",
        "vraag": r"Vier kinderen halen samen een gemiddelde van \(14\) punten. Drie van hen hebben \(12\), \(15\) en \(16\). Hoeveel punten heeft het vierde kind?",
        "antwoord": "13",
        "reken": "14 * 4 - (12 + 15 + 16)",
        "uitleg": r"Gemiddeld \(14\) bij vier kinderen betekent \(14 \times 4 = 56\) punten samen. De drie andere hebben er samen \(43\), dus blijft er \(13\) over.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Twee rechthoeken hebben allebei een omtrek van \(24\) cm. Wat weet je dan over hun oppervlakte?",
        "opties": [
            "Die is altijd even groot, want de omtrek is bij allebei gelijk",
            r"Die kan verschillen; een vierkant van \(6\) bij \(6\) geeft de grootste",
            r"Die is altijd \(36\,\text{cm}^{2}\), ook bij een lange smalle rechthoek",
            "Hoe langer en smaller de rechthoek, hoe groter de oppervlakte",
        ],
        "antwoord": 1,
        "uitleg": r"\(8\) bij \(4\) heeft dezelfde omtrek als \(6\) bij \(6\), maar \(32\,\text{cm}^{2}\) tegenover \(36\,\text{cm}^{2}\). Bij een vaste omtrek geeft het vierkant de grootste oppervlakte.",
    },
    {
        "type": "invultekst",
        "vraag": r"Bus A vertrekt om de \(12\) minuten, bus B om de \(18\) minuten. Om \(8\) uur vertrekken ze samen. Na hoeveel minuten vertrekken ze weer samen?",
        "antwoord": "36",
        "reken": "36",
        "uitleg": r"Je zoekt het kleinste getal waar \(12\) en \(18\) allebei in passen. \(12\), \(24\), \(36\) en \(18\), \(36\): dat is \(36\) minuten, dus om 8.36 u.",
    },
    {
        "type": "waarofniet",
        "vraag": "Als je de zijde van een vierkant verdubbelt, wordt de oppervlakte ook dubbel zo groot.",
        "antwoord": False,
        "uitleg": r"Niet waar, ze wordt vier keer zo groot. Een vierkant van \(3\) cm heeft \(9\,\text{cm}^{2}\), een van \(6\) cm heeft \(36\,\text{cm}^{2}\).",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In een zak zitten \(3\) rode en \(5\) blauwe knikkers. Je neemt er één uit, hij is rood, en je legt hem niet terug. Hoe groot is de kans dat de volgende ook rood is?",
        "opties": [r"\(2\) op \(7\)", r"\(2\) op \(8\)", r"\(3\) op \(7\)", r"\(3\) op \(8\)"],
        "antwoord": 0,
        "uitleg": r"Er zijn nog \(7\) knikkers over en daarvan zijn er nog \(2\) rood. De kans is dus \(2\) op \(7\).",
    },
    {
        "type": "invultekst",
        "vraag": r"Een lege doos weegt \(250\) gram. Met \(6\) gelijke blikjes erin weegt ze \(2{,}5\) kilogram. Hoeveel gram weegt één blikje?",
        "antwoord": "375",
        "reken": "(2500 - 250) / 6",
        "uitleg": r"\(2{,}5\) kg is \(2\,500\) gram. Trek de doos eraf: \(2\,250\) gram voor \(6\) blikjes. \(2\,250 : 6 = 375\) gram.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Een trein rijdt \(90\) kilometer per uur. Hoeveel minuten doet hij over \(30\) kilometer?",
        "opties": [r"\(15\) minuten", r"\(20\) minuten", r"\(30\) minuten", r"\(45\) minuten"],
        "antwoord": 1,
        "reken": "30 / 90 * 60",
        "uitleg": r"\(30\) km is een derde van \(90\) km, en een derde van \(60\) minuten is \(20\) minuten.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Een getal dat deelbaar is door \(6\), is altijd ook deelbaar door \(3\).",
        "antwoord": True,
        "uitleg": r"Waar. In elke \(6\) zitten twee keer \(3\), dus wie door \(6\) kan, kan ook door \(3\). Denk aan \(18\), \(24\) of \(42\).",
    },
    {
        "type": "waarofniet",
        "vraag": r"Een getal dat deelbaar is door \(2\) én door \(4\), is altijd ook deelbaar door \(8\).",
        "antwoord": False,
        "uitleg": r"Niet waar. \(12\) en \(20\) kunnen allebei door \(2\) en door \(4\), maar niet door \(8\).",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welk van deze vier getallen is het grootst?",
        "opties": [r"\(\tfrac{11}{20}\)", r"\(0{,}58\)", r"\(\tfrac{3}{5}\)", r"\(57\,\%\)"],
        "antwoord": 2,
        "uitleg": r"Zet alles om naar kommagetallen: \(\tfrac{11}{20} = 0{,}55\), dan \(0{,}58\), dan \(0{,}57\) en \(\tfrac{3}{5} = 0{,}60\). Drie vijfde is dus het grootst.",
    },
    {
        "type": "invultekst",
        "vraag": r"Hoeveel is \(\tfrac{2}{3}\) van \(\tfrac{3}{4}\) van \(240\)?",
        "antwoord": "120",
        "reken": "240 * 3 / 4 * 2 / 3",
        "uitleg": r"Eerst \(\tfrac{3}{4}\) van \(240 = 180\). Daarvan \(\tfrac{2}{3}\) nemen: \(180 : 3 = 60\) en \(2 \times 60 = 120\). Samen is dat gewoon de helft van \(240\).",
    },
    {
        "type": "meerkeuze",
        "vraag": r"De punten in een groepje waren \(5\), \(5\), \(6\), \(8\) en \(16\). Welk getal zegt het meest over een gewone leerling van dat groepje?",
        "opties": [
            r"Het gemiddelde \(8\), want dan tellen alle punten even hard mee",
            r"Het middelste getal \(6\), want die ene \(16\) trekt het gemiddelde omhoog",
            r"Het grootste getal \(16\), want dat laat zien wat er haalbaar is",
            r"Het kleinste getal \(5\), want dat kwam als enige twee keer voor",
        ],
        "antwoord": 1,
        "uitleg": r"Het gemiddelde is hier \(8\), maar vier van de vijf leerlingen halen minder. Eén uitschieter trekt een gemiddelde scheef; het middelste getal niet.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het gemiddelde van een rij getallen hoeft zelf niet in die rij voor te komen.",
        "antwoord": True,
        "uitleg": r"Waar. Het gemiddelde van \(4\) en \(7\) is \(5{,}5\), en dat getal staat er niet bij.",
    },
    {
        "type": "invultekst",
        "vraag": r"Een balk is \(2\) cm bij \(4\) cm bij \(8\) cm. Een kubus met precies dezelfde inhoud heeft een ribbe van hoeveel cm?",
        "antwoord": "4",
        "reken": "round((2 * 4 * 8) ** (1 / 3))",
        "uitleg": r"De inhoud is \(2 \times 4 \times 8 = 64\,\text{cm}^{3}\). Zoek nu het getal dat drie keer met zichzelf vermenigvuldigd \(64\) geeft: \(4 \times 4 \times 4 = 64\).",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Een kraan laat \(3\) liter per minuut lopen. Hoeveel minuten duurt het om een bad van \(120\) liter voor drie vierde te vullen?",
        "opties": [r"\(25\) minuten", r"\(30\) minuten", r"\(40\) minuten", r"\(45\) minuten"],
        "antwoord": 1,
        "reken": "120 * 3 / 4 / 3",
        "uitleg": r"Drie vierde van \(120\) liter is \(90\) liter. En \(90 : 3 = 30\) minuten.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Kijk naar de rij \(1\), \(4\), \(9\), \(16\), \(25\), ... Welk getal staat op de tiende plaats?",
        "opties": [r"\(64\)", r"\(81\)", r"\(100\)", r"\(121\)"],
        "antwoord": 2,
        "reken": "10 * 10",
        "uitleg": r"Elk getal is een plaats maal zichzelf: 1x1, 2x2, 3x3 ... Op de tiende plaats staat dus \(10 \times 10 = 100\).",
    },
    {
        "type": "waarofniet",
        "vraag": r"Als \(4\) kranen een bad vullen in \(20\) minuten, doen \(8\) even sterke kranen er \(10\) minuten over.",
        "antwoord": True,
        "uitleg": "Waar. Dubbel zoveel kranen laten per minuut dubbel zoveel water lopen, dus het duurt half zo lang.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In een driehoek is één hoek \(90\) graden. Van de twee andere is de ene dubbel zo groot als de andere. Hoeveel graden is de kleinste hoek?",
        "opties": [r"\(20\) graden", r"\(30\) graden", r"\(45\) graden", r"\(60\) graden"],
        "antwoord": 1,
        "uitleg": r"De drie hoeken zijn samen \(180\) graden, dus de twee andere zijn samen \(90\). Eén stuk plus twee stukken is \(90\), dus één stuk is \(30\) graden.",
    },
]

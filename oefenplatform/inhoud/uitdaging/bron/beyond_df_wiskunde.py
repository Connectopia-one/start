# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde 🌍 Beyond dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een temperatuurgrafiek en twee groeimodellen om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte uitleg in eigen woorden. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Wiskunde Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_wiskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Wiskunde"
BESTAND = "beyond-df-wiskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-beyond-df-uitdaging"
TEMP = "temperatuur-dag.svg"
GROEI = "groeimodellen.svg"

# klikvakken uit maak_prenten_beyond_df_wiskunde.py
MIN = [14.8, 58.8, 6.0, 10.0]
MAX = [55.2, 19.8, 6.0, 10.0]
LIJN_A = [78.0, 42.9, 18.0, 11.7]
LIJN_B = [81.0, 22.4, 15.0, 15.0]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Temperatuur (prent)
    klik("Bekijk de grafiek. Klik op het punt waar de temperatuur het hoogst is.",
         TEMP, [MAX],
         "Om 14 uur bereikt de temperatuur haar maximum: 18 °C."),
    klik("Klik op het punt waar de temperatuur het laagst is.",
         TEMP, [MIN],
         "Om 2 uur 's nachts is het het koudst: 6 °C."),
    met_prent(TEMP, tabel(
        "Lees af op de grafiek.",
        [
            ("Temperatuur om 6 uur (°C)", "9"),
            ("Maximum (°C)", "18"),
            ("Minimum (°C)", "6"),
            ("Verschil tussen maximum en minimum (°C)", "12"),
        ],
        "Om 6 uur is het 9 °C. Het maximum is 18 °C en het minimum 6 °C, een verschil van 12 °C.",
        kolommen=["6", "9", "12", "18"])),
    met_prent(TEMP, inv(
        "Bereken de gemiddelde verandering van de temperatuur tussen 6 uur en 14 uur, in °C per uur.",
        ["1,125", "1.125"],
        "Differentiequotiënt: (18 − 9) / (14 − 6) = 9 / 8 = 1,125 °C per uur.")),
    met_prent(TEMP, keuze(
        "Tussen 2 uur en 14 uur is de functie [[*stijgend|dalend|constant]]. Het differentiequotiënt op [14, 22] is [[*negatief|positief|nul]].",
        "Van het minimum naar het maximum stijgt de grafiek. Van 14 uur tot 22 uur daalt de temperatuur, dus de gemiddelde verandering is negatief.")),

    # Groeimodellen (prent)
    klik("Bekijk de twee modellen. Klik op de letter van het exponentiële model.",
         GROEI, [LIJN_B],
         "Model B buigt steeds steiler omhoog: elke maand komt er een vast percentage bij. Model A is een rechte: elke maand evenveel erbij."),
    klik("Klik op de letter van het model waarbij er elke maand evenveel volgers bijkomen.",
         GROEI, [LIJN_A],
         "Een lineair model is een rechte: elke maand komen er 20 volgers bij."),
    met_prent(GROEI, tabel(
        "Model A is \\(N = 100 + 20t\\) en model B is \\(N = 100 \\cdot 1{,}2^{t}\\). Bereken.",
        [
            ("Model A na 5 maanden", "200"),
            ("Model B na 1 maand", "120"),
            ("Model B na 2 maanden", "144"),
        ],
        "A: 100 + 20 · 5 = 200. B: 100 · 1,2 = 120 en 100 · 1,2² = 144.",
        kolommen=["120", "144", "200"])),
    met_prent(GROEI, mk(
        "Met hoeveel procent per maand groeit model B?",
        ["20 %", "1,2 %", "120 %", "2 %"],
        0,
        "Groeifactor 1,2 betekent 1 + 0,20: een groei van 20 % per maand.")),

    # Problemen oplossen
    volgorde(
        "Zet de stappen van het oplossen van een probleem in de juiste volgorde.",
        ["Het probleem begrijpen", "Een plan maken", "Het plan uitvoeren", "Terugblikken en controleren"],
        "Je begrijpt eerst wat er gevraagd wordt, kiest een aanpak, rekent en controleert dan of je antwoord zinvol is."),
    inv("Een gsm-abonnement kost 15 euro per maand plus 0,10 euro per MB boven de bundel. Iemand betaalt 21 euro. Hoeveel MB ging hij boven de bundel?",
        ["60"],
        "21 − 15 = 6 euro extra. 6 / 0,10 = 60 MB."),

    # Machten en wortels
    tabel(
        "Bereken zonder rekenmachine.",
        [
            ("\\(27^{\\frac{1}{3}}\\)", "3"),
            ("\\(16^{\\frac{3}{4}}\\)", "8"),
            ("\\(4^{-\\frac{1}{2}}\\)", "0,5"),
            ("\\(\\sqrt[4]{81}\\)", "3"),
        ],
        "\\(27^{\\frac{1}{3}} = \\sqrt[3]{27} = 3\\), \\(16^{\\frac{3}{4}} = (\\sqrt[4]{16})^{3} = 2^{3} = 8\\), \\(4^{-\\frac{1}{2}} = \\dfrac{1}{\\sqrt{4}} = 0{,}5\\) en \\(3^{4} = 81\\).",
        kolommen=["0,5", "3", "8"]),
    keuze(
        "\\(a^{3} \\cdot a^{4}\\) is gelijk aan [[*\\(a^{7}\\)|\\(a^{12}\\)|\\(2a^{7}\\)]]. \\((a^{2})^{3}\\) is gelijk aan [[*\\(a^{6}\\)|\\(a^{5}\\)|\\(a^{8}\\)]].",
        "Bij een product van machten met hetzelfde grondtal tel je de exponenten op. Bij een macht van een macht vermenigvuldig je ze."),
    mk("Welke uitdrukking is gelijk aan \\(\\sqrt[3]{x^{2}}\\)?",
       ["\\(x^{\\frac{2}{3}}\\)", "\\(x^{\\frac{3}{2}}\\)", "\\(x^{6}\\)", "\\(x^{-\\frac{2}{3}}\\)"],
       0,
       "\\(\\sqrt[n]{x^{m}} = x^{\\frac{m}{n}}\\), dus \\(\\sqrt[3]{x^{2}} = x^{\\frac{2}{3}}\\)."),

    # Logaritmen
    tabel(
        "Bereken.",
        [
            ("\\(\\log_{2} 64\\)", "6"),
            ("\\(\\log 0{,}01\\)", "-2"),
            ("\\(\\log_{3} 1\\)", "0"),
            ("\\(\\log_{5} 125\\)", "3"),
        ],
        "\\(2^{6} = 64\\), \\(10^{-2} = 0{,}01\\), \\(3^{0} = 1\\) en \\(5^{3} = 125\\).",
        kolommen=["-2", "0", "3", "6"]),
    inv("Los op: \\(2^{x} = 32\\). Geef x.",
        ["5"],
        "\\(32 = 2^{5}\\), dus \\(x = 5\\). Of: \\(x = \\log_{2} 32 = 5\\)."),
    keuze(
        "\\(\\log 1000 = 3\\) omdat [[*\\(10^{3} = 1000\\)|\\(3^{10} = 1000\\)|\\(1000 / 3 = 10\\)]]. \\(\\log\\) van een negatief getal [[*bestaat niet|is negatief|is nul]].",
        "De logaritme is de exponent die je aan het grondtal moet geven. Een macht van 10 is altijd positief, dus van een negatief getal bestaat geen logaritme."),

    # Functies en groei
    sorteer(
        "Is de groei lineair of exponentieel?",
        ["Lineair", "Exponentieel"],
        [
            ["Elk jaar komt er 500 euro bij op de rekening.", "Lineair"],
            ["Een bevolking groeit 2 % per jaar.", "Exponentieel"],
            ["Een kaars wordt elk uur 1 cm korter.", "Lineair"],
            ["Een auto verliest elk jaar 15 % van zijn waarde.", "Exponentieel"],
        ],
        "Elke periode hetzelfde bedrag erbij of eraf: lineair. Elke periode hetzelfde percentage: exponentieel."),
    inv("Een auto kost nieuw 20 000 euro en verliest elk jaar 15 % van zijn waarde. Wat is hij na 2 jaar waard? Enkel het getal in euro.",
        ["14450", "14 450", "14.450"],
        "\\(20\\,000 \\cdot 0{,}85^{2} = 20\\,000 \\cdot 0{,}7225 = 14\\,450\\) euro."),
    keuze(
        "Bij \\(f(x) = 5 \\cdot 3^{x}\\) is de beginwaarde [[*5|3|15]] en de groeifactor [[*3|5|15]].",
        "Een exponentiële functie \\(b \\cdot a^{x}\\) heeft beginwaarde b (bij \\(x = 0\\)) en groeifactor a."),
    mk("Een bacteriekolonie verdubbelt elk uur. Er zijn nu 300 bacteriën. Hoeveel zijn er over 4 uur?",
       ["4800", "1200", "2400", "600"],
       0,
       "\\(300 \\cdot 2^{4} = 300 \\cdot 16 = 4800\\)."),

    # Kansen
    tabel(
        "Je gooit één eerlijke dobbelsteen. Bereken de kans volgens Laplace.",
        [
            ("Een even getal", "1/2"),
            ("Meer dan 4", "1/3"),
            ("Een 7", "0"),
            ("Een getal kleiner dan 7", "1"),
        ],
        "Even: 2, 4, 6 → 3/6. Meer dan 4: 5, 6 → 2/6. Een 7 kan niet. Alle uitkomsten zijn kleiner dan 7.",
        kolommen=["0", "1/3", "1/2", "1"]),
    tabel(
        "Een basketbalspeler scoort een vrije worp met kans 0,7. Hij gooit twee keer. Bereken.",
        [
            ("Twee keer raak", "0,49"),
            ("Precies één keer raak", "0,42"),
            ("Minstens één keer raak", "0,91"),
        ],
        "Raak-raak: 0,7 · 0,7 = 0,49. Precies één: 0,7 · 0,3 + 0,3 · 0,7 = 0,42. Minstens één: 1 − 0,3 · 0,3 = 0,91.",
        kolommen=["0,42", "0,49", "0,91"]),
    keuze(
        "Bij een kansboom [[*vermenigvuldig|tel]] je de kansen langs één tak. Kansen van verschillende takken die bij dezelfde gebeurtenis horen, [[*tel je op|vermenigvuldig je]].",
        "Productregel langs een pad, somregel voor verschillende paden."),
    inv("In een zak zitten 3 rode en 5 blauwe knikkers. Je trekt er één. Wat is de kans op rood? Schrijf als breuk.",
        ["3/8"],
        "3 gunstige uitkomsten op 8 mogelijke: 3/8."),

    # Steekproeven en samenhang
    sorteer(
        "Is deze steekproef representatief voor alle Vlaamse jongeren?",
        ["Representatief", "Niet representatief"],
        [
            ["1000 willekeurig gekozen jongeren uit heel Vlaanderen", "Representatief"],
            ["Enkel de leerlingen van één sportschool", "Niet representatief"],
            ["Wie zelf reageert op een oproep op sociale media", "Niet representatief"],
            ["Een loting uit alle Vlaamse scholen", "Representatief"],
        ],
        "Een representatieve steekproef lijkt op de hele populatie. Toevallig kiezen uit de hele groep helpt; één groep of vrijwillige deelname geeft vertekening."),
    mk("Mensen die meer ijs eten, hebben vaker zonnebrand. Wat is de beste verklaring?",
       ["Warm, zonnig weer zorgt voor allebei.", "IJs eten maakt je huid gevoeliger voor de zon.", "Zonnebrand geeft je zin in ijs, dus eet je meer.", "Het is toeval, want er is geen enkele samenhang."],
       0,
       "Samenhang is geen oorzakelijk verband. Het weer verklaart zowel het ijs eten als de zonnebrand."),
    keuze(
        "De populatie is [[*de hele groep die je wil onderzoeken|het deel dat je bevraagt]]. De steekproef is [[*het deel dat je bevraagt|de hele groep die je wil onderzoeken]].",
        "Je trekt besluiten over de populatie op basis van een steekproef."),

    # Normale verdeling
    tabel(
        "Pakken koffie wegen normaal verdeeld met \\(\\mu = 500\\) g en \\(\\sigma = 10\\) g. Hoeveel procent ligt ongeveer",
        [
            ("tussen 490 g en 510 g", "68 %"),
            ("tussen 480 g en 520 g", "95 %"),
            ("boven 510 g", "16 %"),
            ("onder 480 g", "2,5 %"),
        ],
        "Binnen één σ ligt 68 %, binnen twee σ 95 %. Boven \\(\\mu + \\sigma\\): (100 − 68) / 2 = 16 %. Onder \\(\\mu - 2\\sigma\\): (100 − 95) / 2 = 2,5 %.",
        kolommen=["2,5 %", "16 %", "68 %", "95 %"]),
    keuze(
        "De Gausskromme is [[*symmetrisch rond het gemiddelde|scheef naar rechts]]. Hoe groter σ, hoe [[*breder en lager|smaller en hoger]] de klok.",
        "Een normale verdeling is klokvormig en symmetrisch. Meer spreiding maakt de klok breder; de totale oppervlakte blijft 1."),
    mk("Bij welke gegevens verwacht je een normale verdeling?",
       ["De lengte van alle 18-jarigen in België", "Het aantal ogen bij één worp met een dobbelsteen", "De huisnummers in een lange straat", "De uitkomst van kop of munt"],
       0,
       "Natuurlijke metingen zoals lengte zijn vaak klokvormig verdeeld. Een dobbelsteen geeft een uniforme verdeling."),

    # Gemengd
    koppel(
        "Koppel het voorschrift aan het soort functie.",
        [
            ["\\(f(x) = 3x + 2\\)", "lineaire functie"],
            ["\\(f(x) = 2 \\cdot 1{,}5^{x}\\)", "exponentiële functie"],
            ["\\(f(x) = \\log x\\)", "logaritmische functie"],
        ],
        ["kwadratische functie"],
        "Een rechte heeft een eerstegraads voorschrift, bij een exponentiële functie staat x in de exponent en log x is logaritmisch."),
    volgorde(
        "Rangschik deze getallen van klein naar groot.",
        ["\\(\\log 0{,}1\\)", "\\(2^{0}\\)", "\\(\\sqrt{9}\\)", "\\(\\log_{2} 16\\)", "\\(8^{\\frac{2}{3}} \\cdot 2\\)"],
        "\\(\\log 0{,}1 = -1\\), \\(2^{0} = 1\\), \\(\\sqrt{9} = 3\\), \\(\\log_{2} 16 = 4\\) en \\(8^{\\frac{2}{3}} \\cdot 2 = 4 \\cdot 2 = 8\\)."),
    sleep(
        "Bij exponentiële groei met 5 % per jaar is de groeifactor [[1,05]]. Bij een daling van 5 % per jaar is de groeifactor [[0,95]].",
        ["0,05", "1,5"],
        "Groei: 1 + 0,05. Daling: 1 − 0,05."),
    inv("Een bedrag van 1000 euro groeit 4 % per jaar. Na hoeveel volle jaren is het voor het eerst meer dan 1200 euro?",
        ["5"],
        "\\(1000 \\cdot 1{,}04^{4} \\approx 1169{,}86\\) en \\(1000 \\cdot 1{,}04^{5} \\approx 1216{,}65\\). Dus na 5 jaar."),
    tabel(
        "Klopt deze rekenregel voor machten en logaritmen?",
        [
            ("\\(\\log(a \\cdot b) = \\log a + \\log b\\)", J),
            ("\\(\\log(a + b) = \\log a + \\log b\\)", F),
            ("\\(a^{0} = 1\\) voor elke \\(a \\neq 0\\)", J),
            ("\\(a^{-1} = -a\\)", F),
        ],
        "De logaritme van een product is de som van de logaritmen, niet bij een som. \\(a^{-1} = \\dfrac{1}{a}\\)."),

    inv("Bereken: \\(\\log 50 + \\log 2\\).",
        ["2"],
        "\\(\\log 50 + \\log 2 = \\log 100 = 2\\)."),
    tabel(
        "Je trekt één kaart uit een spel van 52 kaarten. Bereken de kans.",
        [
            ("Een harten", "1/4"),
            ("Een aas", "1/13"),
            ("Een rode kaart", "1/2"),
        ],
        "13 harten op 52 = 1/4, 4 azen op 52 = 1/13, 26 rode kaarten op 52 = 1/2.",
        kolommen=["1/13", "1/4", "1/2"]),
    keuze(
        "Een lineaire functie \\(f(x) = 4x - 3\\) heeft richtingscoëfficiënt [[*4|−3|1]] en snijdt de y-as in [[*−3|4|0]].",
        "In \\(f(x) = mx + q\\) is m de richtingscoëfficiënt en q het snijpunt met de y-as."),

    # Uitleg
    open_("Leg in 3 à 5 zinnen uit wat het verschil is tussen lineaire en exponentiële groei, en geef van elk een voorbeeld.",
          "Bij lineaire groei komt er elke periode evenveel bij, bijvoorbeeld elke maand 20 euro sparen. De grafiek is een rechte. Bij exponentiële groei komt er elke periode hetzelfde percentage bij, bijvoorbeeld een bevolking die 2 % per jaar groeit. De grafiek wordt steeds steiler, omdat het percentage telkens op een groter bedrag berekend wordt.",
          "Een goed antwoord zegt dat lineair telkens hetzelfde bedrag en exponentieel telkens hetzelfde percentage of dezelfde factor is, met een passend voorbeeld van elk."),
]

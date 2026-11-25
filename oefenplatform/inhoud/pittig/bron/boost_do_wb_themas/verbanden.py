"""Verbanden tussen twee grootheden — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_verbanden: spreidingsdiagram, puntenwolk, trendlijn en
voorspellen, correlatie en de correlatiecoëfficiënt r, en het verschil met
causaliteit (derde factor). Met twee zelfgetekende prenten: vier
puntenwolken en een spreidingsdiagram met trendlijn."""
import random
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone, venster, punt_zone

VW = "vier-puntenwolken"
PANELEN = [("A", (60, 70)), ("B", (530, 70)), ("C", (60, 360)), ("D", (530, 360))]
PB, PH = 410, 260


def _wolk(letter):
    rnd = random.Random({"A": 1, "B": 2, "C": 3, "D": 4}[letter])
    pts = []
    for _ in range(26):
        x = rnd.uniform(0.05, 0.95)
        if letter == "A":
            y = 0.1 + 0.8 * x + rnd.gauss(0, 0.04)
        elif letter == "B":
            y = 0.9 - 0.75 * x + rnd.gauss(0, 0.09)
        elif letter == "C":
            y = rnd.uniform(0.1, 0.9)
        else:
            y = 0.3 + 0.4 * x + rnd.gauss(0, 0.17)
        pts.append((x, min(0.95, max(0.05, y))))
    return pts


def _vier():
    d = []
    for letter, (x0, y0) in PANELEN:
        d.append(s_vak(x0, y0, PB, PH, vul="#ffffff", rand="#b9b29c", dikte=2, rond=10))
        ax, ay, bw, bh = x0 + 50, y0 + PH - 30, PB - 80, PH - 70
        d.append(s_lijn(ax, ay, ax + bw, ay, kleur="#24331b", dikte=2))
        d.append(s_lijn(ax, ay, ax, ay - bh, kleur="#24331b", dikte=2))
        for x, y in _wolk(letter):
            d.append(f'<circle cx="{ax + x * bw:.1f}" cy="{ay - y * bh:.1f}" r="6" fill="#3b6fa0"/>')
        d.append(f'<circle cx="{x0+30}" cy="{y0+30}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
        d.append(s_tekst(x0 + 30, y0 + 37, letter, 20, vet=True))
    return d


def _pz(*letters):
    pos = dict(PANELEN)
    return [pix_zone(pos[l][0], pos[l][1], PB, PH) for l in letters]


G = venster("studie-en-punten", 0, 9, 0, 20, 1, 2)
METING = [(1, 8), (2, 9.5), (3, 10), (3, 11), (4, 11.5), (5, 13), (6, 6), (7, 15.5)]
GRAFIEKEN = [dict(naam=VW, titel="Vier puntenwolken", eigen=_vier),
             dict(naam=G, titel="", xlabel="uren studeren", ylabel="punten op 20", ijk_y=2,
                  krommen=[(lambda x: 1.1 * x + 7, "oranje", "", (0, 9))],
                  punten=[(x, y, "") for x, y in METING])]
UW, UG = f"{VW}.svg", f"{G}.svg"
SG = "Het spreidingsdiagram toont per leerling hoeveel uur die studeerde en welk punt die haalde, met een oranje trendlijn. "

VRAGEN = [
    klik("Klik op de puntenwolk met de sterkste correlatie.", UW, _pz("A"), r"De punten liggen bijna op een rechte: \(r\) dicht bij \(1\)."),
    klik(r"Klik op de puntenwolk die het best past bij \(r \approx -0{,}8\).", UW, _pz("B"), "De punten dalen, met wat spreiding."),
    klik("Klik op de puntenwolk zonder verband.", UW, _pz("C"), r"Geen richting: \(r \approx 0\)."),
    klik("Klik op de puntenwolk met een stijgend, maar zwak verband.", UW, _pz("D"), "De punten stijgen licht, maar liggen ver uit elkaar."),
    klik(SG + "Klik op de uitschieter.", UG, [punt_zone(G, 6, 6)], "Zes uur gestudeerd, maar maar 6 op 20: ver van het patroon."),
    met_prent(UG, inv("Hoeveel punten voorspelt de trendlijn bij 5 uur studeren?", ["12,5", "12.5"], r"\(1{,}1 \cdot 5 + 7 = 12{,}5\). Lees af op de oranje lijn.")),
    met_prent(UG, keuze("Bij 0 uur studeren voorspelt de trendlijn [[*7|0|20]] punten.", "Daar snijdt de trendlijn de verticale as.")),
    met_prent(UG, mk("Bij 20 uur studeren voorspelt de trendlijn 29 op 20. Wat leer je daaruit?",
                     ["voorspellen buiten de metingen is riskant", "wie 20 uur studeert, krijgt extra bonuspunten", "de trendlijn is verkeerd getekend", "twintig uur studeren is onmogelijk"], 0,
                     "Het verband geldt enkel ongeveer binnen de gemeten waarden, hier van 1 tot 7 uur.")),
    met_prent(UG, keuze("Laat je de uitschieter weg, dan wordt het verband [[*sterker|zwakker]].", "De overige punten liggen dicht bij een stijgende rechte.")),
    met_prent(UG, inv("Hoeveel meetparen staan er in het spreidingsdiagram?", ["8", "acht"], "Elke stip is één leerling met twee waarden.")),
    tabel("Welk verband verwacht je?",
          [("de leeftijd van een auto en zijn verkoopprijs", "dalend"), ("je lengte en je armspanwijdte", "stijgend"),
           ("je schoenmaat en je punt op wiskunde", "geen verband"), ("de buitentemperatuur en de stookkosten", "dalend"),
           ("uren typen oefenen en je typsnelheid", "stijgend")],
          "Hoe ouder de auto of hoe warmer het is, hoe lager de prijs of de kosten.",
          kolommen=["stijgend", "dalend", "geen verband"]),
    sorteer("Oorzaak, of zit er een derde factor achter?", ["oorzaak", "derde factor"],
            [("Bij grotere branden zijn er meer brandweerlieden en meer schade.", "derde factor"), ("Meer uren zon, meer verkochte zonnecrème.", "oorzaak"),
             ("Kinderen met grotere voeten lezen beter.", "derde factor"), ("Meer regen, meer verkochte paraplu's.", "oorzaak")],
            "De brandweer veroorzaakt de schade niet: de grootte van de brand stuurt beide. Bij voeten en lezen is het de leeftijd."),
    mk(r"Welk verband is het sterkst?",
       [r"het verband met \(r = -0{,}95\)", r"het verband met \(r = 0{,}6\)", "ze zijn allebei even sterk", "dat kan je niet zeggen zonder een grafiek"], 0,
       r"De sterkte hangt af van hoe dicht \(r\) bij \(1\) of \(-1\) ligt. Het teken geeft enkel de richting."),
    casus("Een onderzoek vindt: leerlingen die 's morgens ontbijten, halen hogere punten. De correlatiecoëfficiënt is \\(r = 0{,}6\\).", [
        keuze("Het verband is [[*matig stijgend|sterk dalend|onbestaand]].", r"Positief, maar niet dicht bij 1."),
        mk("Mag je besluiten dat ontbijten de punten doet stijgen?",
           ["nee, samenhang is geen oorzaak", "ja, want r is positief", "ja, want het onderzoek zegt het", "nee, want r is kleiner dan 0"], 0,
           "Een correlatie toont enkel dat twee grootheden samen bewegen."),
        mk("Welke derde factor kan beide verklaren?",
           ["een vast dagritme in het gezin", "de kleur van de boekentas", "het weer op de dag van de toets", "het merk van de ontbijtgranen"], 0,
           "Een vast ritme kan zorgen voor ontbijt én voor regelmatig studeren en slapen."),
        mk("Hoe onderzoek je of ontbijten zelf de punten verhoogt?",
           ["twee gelijke groepen vergelijken", "meer leerlingen dezelfde vraag stellen", "r opnieuw berekenen met een rekentoestel", "de leerlingen met lage punten weglaten"], 0,
           "In een experiment verschillen de groepen enkel in wat je onderzoekt."),
    ]),
    inv(r"Een trendlijn heeft als vergelijking \(y = 2x + 3\). Welke \(y\) voorspel je bij \(x = 8\)?", ["19", "negentien"], r"\(2 \cdot 8 + 3 = 19\)."),
    tabel("Klopt dit over spreidingsdiagrammen en correlatie?",
          [(r"Bij \(r = 1\) liggen alle punten precies op een stijgende rechte.", J), (r"Een puntenwolk in de vorm van een boog kan \(r \approx 0\) geven, ook al is er een verband.", J),
           ("Een trendlijn moet door de oorsprong gaan.", F), ("Hoe meer meetpunten, hoe betrouwbaarder de trendlijn meestal is.", J)],
          r"\(r\) meet enkel hoe goed de punten bij een rechte passen.",
          kolommen=["Juist", "Fout"]),
    sleep(r"Bij een [[negatief]] verband dalen de punten. Een waarde van \(r\) dicht bij [[\(-1\)]] wijst op een sterk dalend verband.",
          ["positief", r"\(0\)"], "Het teken geeft de richting, de grootte de sterkte."),
    volgorde("Zet van het zwakste naar het sterkste verband.",
             [r"\(r = 0{,}1\)", r"\(r = -0{,}4\)", r"\(r = 0{,}7\)", r"\(r = -0{,}95\)"],
             "Kijk naar de afstand tot nul, niet naar het teken."),
    mk(r"Waarom betekent \(r = 0\) niet altijd dat er geen enkel verband is?",
       ["het verband kan krom zijn", "r rekent altijd een beetje fout", "dan zijn er te weinig punten gemeten", "r kan nooit precies nul zijn"], 0,
       r"\(r\) meet enkel een lineair verband. Een boog of een golf kan sterk samenhangen en toch \(r \approx 0\) geven."),
    open_("Het aantal verkochte verwarmingsketels en het aantal griepgevallen stijgen samen. Leg uit waarom dat geen oorzakelijk verband is, en wat er wel achter zit.",
          "Een verwarmingsketel geeft niemand griep. Er is een derde factor: in de winter is het koud. Dan kopen mensen meer ketels én verspreidt griep zich makkelijker. De twee stijgen samen zonder dat de ene de andere veroorzaakt."),
    mk("Je onderzoekt of meer uren studeren tot betere punten leidt. Wat zet je op de horizontale as?",
       ["de uren studeren", "de punten op de toets", "de naam van de leerling", "de datum van de toets"], 0,
       "Op de horizontale as komt de grootheid waarvan je denkt dat ze de andere beïnvloedt."),
    keuze("Een spreidingsdiagram toont [[*twee grootheden per persoon of voorwerp|één grootheid die verandert in de tijd]].", "Voor een verloop in de tijd gebruik je een lijndiagram."),
    inv(r"Een trendlijn gaat door \((2, 10)\) en \((6, 18)\). Welke \(y\) voorspel je bij \(x = 4\)?", ["14", "veertien"],
        r"Per stap van \(x\) stijgt \(y\) met \(2\). Bij \(x = 4\): \(10 + 2 \cdot 2 = 14\)."),
    mk(r"Een onderzoeker meet bij vijf leerlingen en vindt \(r = 0{,}9\). Wat is het probleem?",
       ["vijf metingen zijn te weinig", r"\(r = 0{,}9\) bestaat niet", "het verband is dan dalend", "leerlingen mag je nooit zomaar meten"], 0,
       "Bij zo weinig punten kan toeval een sterk verband doen lijken."),
    met_prent(UG, tabel("De metingen gaan van 1 tot 7 uur. Is een voorspelling bij dit aantal uren binnen of buiten de gemeten waarden?",
                        [("4 uur", "binnen"), ("6,5 uur", "binnen"), ("12 uur", "buiten"), ("0 uur", "buiten")],
                        "Buiten de metingen weet je niet of het verband nog geldt.",
                        kolommen=["binnen", "buiten"])),
    koppel("Verbind de beschrijving van de puntenwolk met de passende r.",
           [("punten bijna op een dalende rechte", r"\(r = -0{,}97\)"), ("punten verspreid, licht stijgend", r"\(r = 0{,}4\)"), ("punten zonder richting", r"\(r = 0{,}02\)")],
           [r"\(r = 1{,}5\)"], r"\(r\) ligt altijd tussen \(-1\) en \(1\)."),
    keuze(r"Een correlatiecoëfficiënt \(r = 1{,}3\) is [[*onmogelijk|een heel sterk verband]].", r"\(-1 \leq r \leq 1\)."),
]

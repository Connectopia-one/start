"""Misleiding met cijfers, en verbanden in een puntenwolk — pittig (🚀 Boost doorstroom)."""
import random
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_lijn, s_tekst, s_vak, pix_zone, DONKER, GROEN

WOLK = "misleiding-drie-wolken-do"
STAAF = "misleiding-staven-do"
VAKKEN = {"A": 60, "B": 370, "C": 680}  # linkerrand van elk vak, breedte 270


def _wolken():
    rnd = random.Random(7)
    d = []
    for letter, x0 in VAKKEN.items():
        d.append(s_vak(x0, 90, 270, 420, vul="#fffdf7", rond=12))
        d.append(s_lijn(x0 + 30, 480, x0 + 250, 480, kleur=DONKER, dikte=2))
        d.append(s_lijn(x0 + 30, 480, x0 + 30, 110, kleur=DONKER, dikte=2))
        d.append(s_tekst(x0 + 135, 560, f"wolk {letter}", 26, vet=True))
        for i in range(22):
            t = rnd.random()
            if letter == "A":      # sterk negatief
                u = 1 - t + rnd.uniform(-0.08, 0.08)
            elif letter == "B":    # geen verband
                u = rnd.random()
            else:                  # zwak positief
                u = 0.15 + 0.7 * t + rnd.uniform(-0.25, 0.25)
            u = min(max(u, 0.02), 0.98)
            d.append(f'<circle cx="{x0 + 40 + 200 * t:.1f}" cy="{470 - 340 * u:.1f}" r="7" fill="{GROEN}"/>')
    return d


def _vakzone(letter):
    return pix_zone(VAKKEN[letter], 90, 270, 500)


JAREN = [("2023", 50.2), ("2024", 50.9), ("2025", 51.6)]


def _staven():
    d = []
    lo, hi = 50, 52
    def Y(v):
        return 520 - (v - lo) / (hi - lo) * 400
    d.append(s_lijn(200, 520, 200, 100, kleur=DONKER, dikte=3))
    d.append(s_lijn(200, 520, 860, 520, kleur=DONKER, dikte=3))
    for k in range(5):
        v = lo + k * 0.5
        d.append(s_lijn(192, Y(v), 208, Y(v), kleur=DONKER, dikte=2))
        d.append(s_tekst(180, Y(v) + 7, f"{v:.1f}".replace(".", ","), 20, anker="end"))
    for i, (jaar, v) in enumerate(JAREN):
        x = 280 + i * 200
        d.append(f'<rect x="{x}" y="{Y(v):.1f}" width="120" height="{520 - Y(v):.1f}" fill="#7a4b8c"/>')
        d.append(s_tekst(x + 60, 556, jaar, 22, vet=True))
        d.append(s_tekst(x + 60, Y(v) - 12, f"{v}".replace(".", ","), 20))
    d.append(s_tekst(100, 90, "prijs (euro)", 20, anker="start"))
    return d


GRAFIEKEN = [
    dict(naam=WOLK, titel="Drie puntenwolken", eigen=_wolken),
    dict(naam=STAAF, titel="Gemiddelde prijs van een winkelkar", eigen=_staven),
]
PRENTEN = [
    dict(bestand=f"{WOLK}.svg", zelf=True, wat="drie puntenwolken: sterk negatief, geen verband, zwak positief", vragen="klikvragen over correlatie"),
    dict(bestand=f"{STAAF}.svg", zelf=True, wat="staafdiagram met een verticale as die bij 50 begint", vragen="vragen over misleidende grafieken"),
]

VRAGEN = [
    klik(
        "Klik op de puntenwolk met een correlatiecoëfficiënt dicht bij −1.",
        f"{WOLK}.svg",
        [_vakzone("A")],
        "In wolk A liggen de punten bijna op een dalende rechte: een sterk negatief verband.",
    ),
    klik(
        "Klik op de puntenwolk waar r het dichtst bij 0 ligt.",
        f"{WOLK}.svg",
        [_vakzone("B")],
        "In wolk B is er geen richting te zien: geen rechtlijnig verband.",
    ),
    klik(
        "Klik op de puntenwolk met een zwak positief verband.",
        f"{WOLK}.svg",
        [_vakzone("C")],
        "Wolk C stijgt van links naar rechts, maar de punten liggen breed verspreid.",
    ),
    met_prent(f"{WOLK}.svg", tabel(
        "Kijk naar de drie wolken. Welke waarde van r past het best?",
        [("wolk A", "−0,95"), ("wolk B", "0,05"), ("wolk C", "0,6")],
        "Een teken toont de richting, de grootte toont hoe dicht de punten bij een rechte liggen.",
        kolommen=["−0,95", "0,05", "0,6"],
    )),
    met_prent(f"{STAAF}.svg", mk(
        "Kijk naar het staafdiagram. De staaf van 2025 lijkt acht keer zo hoog als die van 2023. Met hoeveel procent steeg de prijs echt?",
        [r"ongeveer \(3\,\%\)", r"ongeveer \(300\,\%\)", r"ongeveer \(30\,\%\)", r"ongeveer \(1{,}4\,\%\)"],
        0,
        r"\(\tfrac{51{,}6 - 50{,}2}{50{,}2} \approx 0{,}028\): bijna \(3\,\%\). De as begint bij \(50\) en niet bij \(0\), daardoor lijkt het verschil enorm.",
    )),
    met_prent(f"{STAAF}.svg", tabel(
        "Kijk naar het staafdiagram. Juist of fout?",
        [("De verticale as begint niet bij nul.", J),
         ("De prijs is van 2023 tot 2025 meer dan verdubbeld.", F),
         ("De getallen boven de staven kloppen, maar de tekening overdrijft.", J),
         ("Met een as vanaf 0 zouden de staven bijna even hoog lijken.", J)],
        "Een grafiek kan juiste cijfers tonen en toch een verkeerde indruk geven.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Een partij haalde vorige keer 8 % en nu 10 %. Juist of fout?",
        [("Ze won 2 procentpunt.", J), ("Ze won 2 procent.", F), ("Ze groeide met 25 %.", J), ("Ze haalt nu een kwart meer stemmen dan vorige keer, als evenveel mensen stemden.", J)],
        r"Het verschil in procentpunt is \(10 - 8 = 2\). De relatieve groei is \(\tfrac{2}{8} = 25\,\%\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Een jas kost 80 euro. Eerst gaat de prijs 25 % omhoog, daarna krijg je 25 % korting. Wat betaal je?",
        ["75 euro", "80 euro", "85 euro", "60 euro"],
        0,
        r"\(80 \cdot 1{,}25 = 100\), dan \(100 \cdot 0{,}75 = 75\). De korting is berekend op een groter bedrag.",
    ),
    inv(
        "Een prijs daalt met 50 %. Met hoeveel procent moet ze daarna stijgen om terug op de oude prijs te komen?",
        ["100", "100%", "100 %"],
        "Van 100 naar 50 is de helft eraf. Van 50 terug naar 100 is er 50 bij, en dat is 100 % van 50.",
    ),
    sorteer(
        "Bewijst dit een oorzakelijk verband?",
        ["Wellicht een derde factor", "Een echte oorzaak is aannemelijk"],
        [("Wie meer schoenen koopt, heeft vaker een hoger loon.", "Wellicht een derde factor"),
         ("In de zomer worden er meer zonnebrillen en meer ijsjes verkocht.", "Wellicht een derde factor"),
         ("Wie meer oefent op de piano, speelt foutlozer.", "Een echte oorzaak is aannemelijk"),
         ("Kinderen met grotere voeten lezen beter.", "Wellicht een derde factor"),
         ("Hoe harder je trapt, hoe sneller je fiets gaat.", "Een echte oorzaak is aannemelijk")],
        "Grotere voeten en beter lezen horen allebei bij oudere kinderen. Een correlatie alleen bewijst nooit een oorzaak.",
    ),
    casus(
        "Een bedrijf meldt: 'Onze klanten zijn zeer tevreden: 90 % gaf ons 5 sterren!' Die cijfers komen uit een enquête op de eigen site waar 20 klanten op reageerden.",
        [
            mk("Hoeveel klanten gaven 5 sterren?", ["18", "90", "2", "20"], 0, r"\(90\,\%\) van \(20\) is \(18\)."),
            mk("Wat is het grootste probleem met dit cijfer?",
               ["de groep is klein en wie reageert, is vaak extra tevreden of boos", "90 % is altijd te hoog om waar te kunnen zijn bij een echte enquête", "sterren mag je nooit omzetten naar een percentage van de klanten", "er is geen probleem, want de cijfers zelf kloppen allemaal wel"], 0,
               "Een percentage zegt weinig zonder het aantal en zonder te weten wie er antwoordde."),
            mk("Welke informatie mis je het meest?", ["hoeveel klanten het bedrijf in totaal heeft", "welke kleur de sterren op de website hadden", "hoe de zaakvoerder van het bedrijf heet", "in welk jaar het bedrijf werd opgericht"], 0,
               "Twintig van de tienduizend klanten is iets heel anders dan twintig van de vijfentwintig."),
        ],
    ),
    keuze(
        "Een sterke correlatie tussen twee variabelen betekent dat ze [[*samen veranderen|elkaar zeker veroorzaken|altijd gelijk zijn]]. Om een oorzaak te bewijzen, heb je [[*een experiment of een andere verklaring|een grotere correlatie|een trendlijn]] nodig.",
        "Correlatie is geen oorzakelijk verband. Een derde factor kan beide beïnvloeden.",
    ),
    tabel(
        "Juist of fout over de correlatiecoëfficiënt r?",
        [(r"\(r = -0{,}8\) wijst op een sterker verband dan \(r = 0{,}5\).", J),
         (r"\(r = 1{,}3\) is mogelijk bij heel veel punten.", F),
         (r"\(r = 0\) betekent dat er zeker geen enkel verband is.", F),
         (r"Bij \(r = -1\) liggen alle punten op een dalende rechte.", J)],
        r"De sterkte hangt af van \(|r|\). Bij \(r = 0\) is er geen rechtlijnig verband, maar een gebogen verband kan wel.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Een trendlijn door de lengte van kinderen van 2 tot 10 jaar geeft: lengte = 6 · leeftijd + 80 (in cm). Wat zegt de lijn voor een volwassene van 40 jaar?",
        ["320 cm, wat onzin is: je voorspelt ver buiten de metingen", "320 cm, dus een volwassene van 40 jaar is ongeveer zo groot", "180 cm, want een trendlijn buigt vanzelf af na de metingen", "80 cm, want daar snijdt de trendlijn de verticale as"],
        0,
        "Buiten het gemeten gebied kan een verband er helemaal anders uitzien. Kinderen groeien niet hun hele leven door.",
    ),
    koppel(
        "Verbind de misleidende grafiek met de truc.",
        [("de verticale as begint bij 95 in plaats van 0", "kleine verschillen lijken groot"),
         ("blokken in 3D in plaats van platte staven", "het oog vergelijkt volumes"),
         ("op de as staan 0, 10, 20, 50, 100 op gelijke afstand", "de ijk is fout"),
         ("een jaar zonder stijging is weggelaten", "gegevens zijn weggelaten")],
        ["de bron staat erbij"],
        "Een bron vermelden is net eerlijk: dan kan de lezer de cijfers nagaan.",
    ),
    inv(
        r"Een gemeente heeft 4000 inwoners. Het aantal fietsdiefstallen steeg van 4 naar 6. Met hoeveel procent steeg het aantal diefstallen?",
        ["50", "50%", "50 %"],
        r"\(\tfrac{6 - 4}{4} = 50\,\%\). Klinkt veel, maar het gaat om twee fietsen meer.",
    ),
    mk(
        "Een krant schrijft: 'Het risico op een zeldzame ziekte verdubbelt bij wie dagelijks frisdrank drinkt.' Het risico was 1 op 100 000. Wat is het nu?",
        ["2 op 100 000", "1 op 50", "50 op 100 000", "1 op 2"],
        0,
        "Een verdubbeling van een heel klein risico blijft een heel klein risico. Vraag altijd naar het absolute aantal.",
    ),
    volgorde(
        "Je wilt een puntenwolk eerlijk beschrijven. Zet de stappen in een zinnige volgorde.",
        ["de twee variabelen op de assen zetten", "de punten uitzetten", "kijken naar richting en spreiding", "eventueel een trendlijn tekenen", "voorzichtig besluiten, zonder oorzaak te beweren"],
        "Eerst de gegevens zien, dan samenvatten, en pas dan besluiten.",
    ),
    sleep(
        "Bij een [[negatieve]] correlatie loopt de wolk van linksboven naar rechtsonder. Eén [[uitschieter]] ver van de wolk kan de trendlijn flink verplaatsen.",
        ["positieve", "mediaan"],
        "Kijk altijd naar de punten zelf en niet enkel naar het getal r.",
    ),
    tabel(
        "In een gemeente verdienen 99 mensen 2500 euro per maand en één persoon 1 000 000 euro. Juist of fout?",
        [("Het gemiddelde loon is meer dan 12 000 euro.", J), ("De mediaan is 2500 euro.", J), ("Het gemiddelde geeft een goed beeld van een gewoon loon.", F), ("De modus is 2500 euro.", J)],
        r"\(\tfrac{99 \cdot 2500 + 1\,000\,000}{100} = 12\,475\) euro. Eén uitschieter trekt het gemiddelde ver weg.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "Een cirkeldiagram over vrije tijd toont: sport 40 %, muziek 35 %, gamen 38 %. Hoeveel procent is dat samen?",
        ["113", "113%", "113 %"],
        r"\(40 + 35 + 38 = 113\,\%\). Dat kan niet in een cirkeldiagram: wie meerdere hobby's mocht kiezen, telt dubbel.",
    ),
    mk(
        "Het aantal leerlingen met een smartphone steeg van 60 % naar 90 %. Welke zin klopt?",
        ["er kwam 30 procentpunt bij, een stijging van 50 %", "er kwam 30 % bij, dus een stijging van 30 procentpunt", "er kwam 50 procentpunt bij, want 30 is de helft van 60", "het aantal leerlingen met een smartphone verdubbelde"],
        0,
        r"\(90 - 60 = 30\) procentpunt. Relatief: \(\tfrac{30}{60} = 50\,\%\).",
    ),
    tabel(
        "Een trendlijn is y = 2x + 10 voor x tussen 0 en 20. Is de voorspelling zinvol?",
        [("bij x = 5", J), ("bij x = 12", J), ("bij x = 200", F), ("bij x = −50", F)],
        "Binnen het gemeten gebied mag je voorspellen. Ver erbuiten weet je niet of het verband nog geldt.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "Een partij gaat van 30 % naar 24 % van de stemmen. Met hoeveel procentpunt daalde ze?",
        ["6"],
        r"\(30 - 24 = 6\) procentpunt. In procent is dat een daling van \(\tfrac{6}{30} = 20\,\%\).",
    ),
    mk(
        "Een reclame zegt: 'Nu 33 % meer inhoud!' De fles ging van 75 cl naar 100 cl. Klopt dat?",
        ["ja, want 25 is ongeveer een derde van 75", "nee, het is 25 % meer, want er kwam 25 cl bij", "nee, het is 75 % meer, want de oude fles was 75 cl", "nee, de inhoud verdubbelde, want 100 is veel meer"],
        0,
        r"\(\tfrac{25}{75} = 0{,}33\ldots\): een derde meer. De reclame klopt dus.",
    ),
    tabel(
        "Een spreidingsdiagram toont studietijd en punten van 30 leerlingen met r = 0,8. Juist of fout?",
        [("In deze groep halen leerlingen die meer studeren meestal betere punten.", J),
         ("Elke leerling die meer studeert, haalt zeker betere punten.", F),
         ("Er is een sterk positief verband.", J),
         ("Studeren is bewezen de enige oorzaak van goede punten.", F)],
        "Een correlatie beschrijft de groep, niet elke leerling, en bewijst geen oorzaak.",
        kolommen=["Juist", "Fout"],
    ),
    met_prent(f"{WOLK}.svg", mk(
        "Kijk naar de drie wolken. Bij welke wolk geeft een trendlijn de betrouwbaarste voorspelling?",
        ["wolk A", "wolk B", "wolk C", "bij alle drie even goed"],
        0,
        "Hoe dichter de punten bij de rechte liggen, hoe beter de trendlijn ze samenvat. Dat de lijn daalt, maakt niet uit.",
    )),
    sorteer(
        "Is de grafiek eerlijk of misleidend?",
        ["Eerlijk", "Misleidend"],
        [("een staafdiagram met as vanaf nul en bron vermeld", "Eerlijk"),
         ("een lijndiagram waarin de stappen op de tijdas ongelijk zijn", "Misleidend"),
         ("een cirkeldiagram waarvan de delen samen 100 % geven", "Eerlijk"),
         ("een staafdiagram waarin één staaf breder getekend is dan de andere", "Misleidend")],
        "Een eerlijke grafiek laat de lezer de verhoudingen juist zien.",
    ),
]

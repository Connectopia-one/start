"""Misleiding met cijfers en grafieken — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_lijn, s_vak, DONKER, GROEN

STAAF = "misleiding-staafdiagram"
# verticale as van 90 tot 97 tevredenheid in procent
Y0, Y1, V0, V1 = 520, 120, 90, 97


def _y(v):
    return Y0 - (v - V0) / (V1 - V0) * (Y0 - Y1)


def _staaf():
    d = [s_lijn(160, Y0, 860, Y0, kleur=DONKER, dikte=3), s_lijn(160, Y0, 160, Y1 - 20, kleur=DONKER, dikte=3)]
    for v in range(90, 98):
        d.append(s_lijn(150, _y(v), 160, _y(v), kleur=DONKER, dikte=2))
        d.append(s_tekst(138, _y(v) + 7, f"{v} %", 20, anker="end"))
    for x, v, naam, kleur in [(270, 92, "Winkel A", "#b9b29c"), (560, 96, "Winkel B", GROEN)]:
        d.append(s_vak(x, _y(v), 180, Y0 - _y(v), vul=kleur, rand=DONKER))
        d.append(s_tekst(x + 90, Y0 + 36, naam, 22, vet=True))
        d.append(s_tekst(x + 90, _y(v) - 12, f"{v} %", 22, vet=True))
    d.append(s_tekst(500, 600, "Tevreden klanten", 20, kleur="#6b6b5a"))
    return d


GRAFIEKEN = [dict(naam=STAAF, titel="Reclame van winkel B: 'Veel meer tevreden klanten!'", eigen=_staaf)]
PRENTEN = [dict(bestand=f"{STAAF}.svg", zelf=True, wat="misleidend staafdiagram", vragen="klikvraag over een as die niet bij nul begint")]

VRAGEN = [
    klik(
        "Klik op de plaats in de grafiek die het verschil tussen de twee winkels groter doet lijken dan het is.",
        f"{STAAF}.svg",
        [pix_zone(60, _y(90) - 30, 120, 60)],
        "De verticale as begint bij 90 % in plaats van bij 0. Daardoor lijkt de staaf van B drie keer zo hoog, terwijl het verschil maar 4 procentpunt is.",
    ),
    met_prent(f"{STAAF}.svg", mk(
        "Hoeveel keer zo hoog lijkt de staaf van winkel B in deze grafiek, en hoeveel keer zo groot is het percentage echt?",
        [
            r"ze lijkt \(3\) keer zo hoog, het percentage is ongeveer \(1{,}04\) keer zo groot",
            r"ze lijkt \(2\) keer zo hoog, het percentage is \(2\) keer zo groot",
            r"ze lijkt \(4\) keer zo hoog, het percentage is \(4\) keer zo groot",
            r"ze lijkt \(1{,}04\) keer zo hoog, net zoals het percentage, want de staven tonen gewoon de cijfers",
        ],
        0,
        r"Boven \(90\%\) is A \(2\) eenheden hoog en B \(6\): drie keer zo hoog. Echt: \(\tfrac{96}{92} \approx 1{,}04\).",
    )),
    met_prent(f"{STAAF}.svg", tabel(
        "Juist of fout over deze reclame?",
        [
            ("Winkel B heeft 4 procentpunt meer tevreden klanten.", J),
            ("Winkel B heeft 4 % meer tevreden klanten dan A.", F),
            ("Je weet niet hoeveel klanten werden bevraagd.", J),
            ("Met een as vanaf 0 zouden de staven bijna even hoog zijn.", J),
        ],
        r"Het verschil is \(4\) procentpunt. In procent is dat \(\tfrac{4}{92} \approx 4{,}3\%\) meer. Er staat geen bron en geen aantal bij.",
    )),
    mk(
        r"Een werkloosheidscijfer daalt van \(8\%\) naar \(6\%\). Wat klopt?",
        [
            r"het daalt met \(2\) procentpunt, en dat is een daling van \(25\%\)",
            r"het daalt met \(2\%\), en dat is een daling van \(2\) procentpunt",
            r"het daalt met \(25\) procentpunt",
            r"het daalt met \(2\) procentpunt, en dat is een daling van \(33\%\)",
        ],
        0,
        r"\(8 - 6 = 2\) procentpunt. Ten opzichte van de beginwaarde: \(\tfrac{2}{8} = 25\%\). \(33\%\) krijg je als je deelt door \(6\), de eindwaarde.",
    ),
    inv(
        r"Een trui kost \(80\) euro. Ze krijgt eerst \(25\%\) korting en aan de kassa nog eens \(20\%\) op de verlaagde prijs. Hoeveel betaal je, in euro?",
        ["48", "48 euro"],
        r"\(80 \cdot 0{,}75 = 60\), en \(60 \cdot 0{,}80 = 48\) euro. Dat is \(40\%\) korting, niet \(45\%\).",
    ),
    mk(
        r"Een aandeel stijgt eerst met \(50\%\) en daalt daarna met \(50\%\). Waar staat het ten opzichte van het begin?",
        [r"op hetzelfde", r"\(25\%\) lager", r"\(25\%\) hoger", r"\(50\%\) lager"],
        1,
        r"\(100 \cdot 1{,}5 = 150\), en \(150 \cdot 0{,}5 = 75\). De daling werkt op een grotere waarde dan de stijging.",
    ),
    casus(
        r"In een klein bedrijf verdienen \(6\) werknemers elk \(2200\) euro per maand. De zaakvoerder verdient \(15\,000\) euro.",
        [
            inv(
                "Wat is het gemiddelde loon, afgerond op een euro?",
                ["4029", "4029 euro", "4 029"],
                r"\(\tfrac{6 \cdot 2200 + 15\,000}{7} = \tfrac{28\,200}{7} \approx 4029\) euro.",
            ),
            mk(
                "Het bedrijf zet in een vacature: 'Bij ons verdien je gemiddeld 4000 euro.' Wat is het probleem?",
                [
                    "het cijfer is fout berekend, want je moet het loon van de zaakvoerder weglaten uit de som",
                    "een gemiddelde mag je nooit gebruiken bij lonen",
                    "het cijfer klopt, maar zes van de zeven verdienen veel minder: de mediaan is 2200 euro",
                    "het gemiddelde ligt eigenlijk onder 2200 euro",
                ],
                2,
                "Een juist cijfer kan toch misleiden. Eén hoog loon trekt het gemiddelde omhoog; de mediaan toont wat een gewone werknemer verdient.",
            ),
        ],
    ),
    koppel(
        "Koppel elke grafiek aan de manier waarop ze misleidt.",
        [
            ["de verticale as begint bij 95 in plaats van 0", "kleine verschillen lijken groot"],
            ["een omzet die verdubbelt, getoond als een zak geld die twee keer zo breed én hoog is", "de groei lijkt vier keer zo groot"],
            ["een lijndiagram toont enkel de drie beste maanden", "data weglaten"],
            ["een cirkeldiagram in 3D, schuin van voor", "de sectoren vooraan lijken groter"],
        ],
        ["de grafiek heeft een bron en een titel"],
        "Een bron en een titel maken een grafiek net betrouwbaarder.",
    ),
    tabel(
        "Juist of fout over procenten?",
        [
            ("Een stijging van 200 % betekent dat iets verdrievoudigd is.", J),
            ("Een daling van 100 % betekent dat er niets meer over is.", J),
            ("Een daling van 150 % is mogelijk bij een aantal personen.", F),
            ("Een prijs die 10 % stijgt en dan 10 % daalt, staat terug op de beginprijs.", F),
        ],
        "200 % erbij: 100 + 200 = 300 %. Een aantal kan niet meer dan 100 % dalen. 100 · 1,1 · 0,9 = 99: iets lager dan het begin.",
    ),
    mk(
        r"Een krant schrijft: 'Het risico op een zeldzame ziekte verdubbelt door dit product.' Het risico was \(1\) op \(100\,000\). Wat is het nu?",
        [r"\(2\) op \(100\,000\)", r"\(1\) op \(50\)", r"\(50\%\)", r"\(2\) op \(1000\)"],
        0,
        r"Verdubbelen van \(1\) op \(100\,000\) geeft \(2\) op \(100\,000\): nog altijd heel klein. Een verdubbeling zegt niets zonder het beginrisico.",
    ),
    sorteer(
        "Is deze steekproef representatief voor alle jongeren in Vlaanderen?",
        ["representatief", "niet representatief"],
        [
            ["een bevraging bij de ingang van een fitnesszaal over sportgewoontes", "niet representatief"],
            ["een online stemming op de site van een gamebedrijf over schermtijd", "niet representatief"],
            ["een toevallige keuze van 1000 jongeren uit alle scholen, verspreid over Vlaanderen", "representatief"],
            ["een bevraging bij de vrienden van één klas", "niet representatief"],
        ],
        "Een steekproef moet lijken op de hele groep. Wie zichzelf aanbiedt of op één plek wordt gevraagd, verschilt vaak van de rest.",
    ),
    keuze(
        r"Een prijs stijgt van \(50\) naar \(60\) euro. Dat is een stijging van [[*\(20\%\)|\(10\%\)|\(16{,}7\%\)]]. Daalt hij daarna terug naar \(50\) euro, dan is dat een daling van ongeveer [[*\(16{,}7\%\)|\(20\%\)|\(10\%\)]].",
        r"\(\tfrac{10}{50} = 20\%\), maar \(\tfrac{10}{60} \approx 16{,}7\%\): je deelt telkens door de beginwaarde van die stap.",
    ),
    mk(
        r"Een reclame zegt: '\(9\) op de \(10\) gebruikers is tevreden!' Er werden \(10\) gebruikers bevraagd, gekozen door het bedrijf. Wat is de beste reactie?",
        [
            "de steekproef is te klein en niet toevallig gekozen, dus het cijfer zegt weinig",
            r"het cijfer is fout, want bij een tevredenheid van \(9\) op \(10\) moet je eerst het gemiddelde nemen",
            r"het cijfer is betrouwbaar, want \(90\%\) is heel hoog",
            "je moet het percentage omrekenen naar procentpunt",
        ],
        0,
        "Bij tien zelf gekozen mensen kan het bedrijf makkelijk tevreden klanten uitkiezen. Vraag altijd: hoeveel mensen en wie koos ze?",
    ),
    volgorde(
        "Je ziet een grafiek op sociale media. Zet de vragen die je stelt in een logische volgorde.",
        [
            "Wat is de titel, en wat staat er op de assen?",
            "Begint de verticale as bij nul en is de schaal gelijkmatig?",
            "Worden alle gegevens getoond, of maar een deel?",
            "Waar komen de cijfers vandaan, en wie heeft er belang bij?",
        ],
        "Eerst begrijpen wat de grafiek toont, dan hoe ze getekend is, dan wat er ontbreekt en tot slot wie ze maakt.",
    ),
    inv(
        r"Een gemeente had vorig jaar \(40\) diefstallen en dit jaar \(50\). Met hoeveel procent steeg het aantal?",
        ["25", "25%", "25 %"],
        r"\(\tfrac{50 - 40}{40} = 0{,}25 = 25\%\).",
    ),
    mk(
        r"Dezelfde gemeente telt \(20\,000\) inwoners. Een krant kopt: 'Diefstallen stijgen met 25%!' Welke extra informatie geeft een eerlijker beeld?",
        [
            r"dat het om \(10\) diefstallen meer gaat, op \(20\,000\) inwoners",
            "dat er ook meer inwoners zijn bijgekomen in de stad",
            "dat procenten altijd overdrijven",
            "dat de krant ook over andere misdrijven schrijft",
        ],
        0,
        "Een percentage op een klein aantal kan groot klinken. De absolute aantallen en de grootte van de groep tonen hoe groot het echt is.",
    ),
    sleep(
        "Het verschil tussen 4 % en 6 % is 2 [[procentpunt]]. Ten opzichte van 4 % is dat een stijging van 50 [[procent]].",
        ["procentuele", "promille"],
        "Procentpunt is het gewone verschil tussen twee percentages. Procent vergelijkt dat verschil met de beginwaarde.",
    ),
    tabel(
        "Is deze vergelijking eerlijk?",
        [
            ("twee lijndiagrammen naast elkaar met een andere schaal op de verticale as", F),
            ("het aantal ongevallen in een grote en een kleine stad, zonder rekening te houden met het aantal inwoners", F),
            ("de gemiddelde temperatuur in juli van twee jaren, gemeten op dezelfde plaats", J),
            ("de prijs van een brood in 1990 en nu, zonder rekening te houden met de inflatie", F),
        ],
        "Eerlijk vergelijken vraagt dezelfde schaal, dezelfde groepsgrootte en dezelfde omstandigheden.",
    ),
    mk(
        r"Een winkel adverteert: 'Tot \(60\%\) korting!' Wat weet je zeker?",
        [
            r"alle artikelen hebben \(60\%\) korting",
            r"de meeste artikelen in de winkel krijgen minstens \(60\%\) korting op de oude prijs",
            r"geen enkel artikel heeft meer dan \(60\%\) korting",
            r"minstens de helft van de artikelen heeft korting",
        ],
        2,
        r"'Tot' geeft enkel de grootste korting. Misschien heeft maar één artikel \(60\%\) en de rest \(10\%\).",
    ),
    open_(
        r"Een frisdrankmerk zegt: 'Onze nieuwe fles heeft \(30\%\) minder suiker!' De oude fles had \(10\) suikerklontjes per liter. Leg uit welke vragen je stelt voor je besluit dat de drank gezond is.",
        r"\(30\%\) minder dan \(10\) klontjes is nog altijd \(7\) klontjes per liter: dat blijft veel. Je vraagt ook met wat het vergeleken wordt, hoe groot de fles is en wie het cijfer naar buiten brengt.",
    ),
    mk(
        r"De omzet van een bedrijf groeide van \(2\) naar \(3\) miljoen euro. In een folder staat een vierkant dat \(1{,}5\) keer zo breed én zo hoog is als het eerste. Hoeveel keer zo groot lijkt de omzet?",
        [r"\(1{,}5\) keer", r"\(2{,}25\) keer", r"\(3\) keer", r"\(3{,}375\) keer"],
        1,
        r"De oppervlakte groeit met \(1{,}5^{2} = 2{,}25\), terwijl de omzet maar \(1{,}5\) keer zo groot werd.",
    ),
    inv(
        r"Een prijs stijgt met \(20\%\). Met hoeveel procent moet hij daarna dalen om terug op de beginprijs te komen? Rond af op een tiende.",
        ["16,7", "16,7%", "16,7 %", "16.7"],
        r"Van \(100\) naar \(120\), en terug naar \(100\) is \(20\) van de \(120\): \(\tfrac{20}{120} \approx 16{,}7\%\).",
    ),
    mk(
        r"Twee studies over hetzelfde medicijn: studie A met \(30\) patiënten toont een groot effect, studie B met \(3000\) patiënten toont bijna geen effect. Welke studie weegt het zwaarst?",
        [
            "studie A, want een groot effect is belangrijker dan een klein",
            "studie B, want een grote steekproef geeft een betrouwbaarder beeld",
            "allebei even zwaar, want het zijn allebei wetenschappelijke studies over hetzelfde medicijn",
            "geen van beide, want medicijnen kan je niet onderzoeken",
        ],
        1,
        "Bij weinig patiënten speelt het toeval een grote rol. Hoe groter de steekproef, hoe kleiner die invloed.",
    ),
    inv(
        r"Na een prijsstijging van \(15\%\) kost een product \(46\) euro. Wat kostte het vóór de stijging, in euro?",
        ["40", "40 euro"],
        r"\(46\) euro is \(115\%\) van de oude prijs: \(46 : 1{,}15 = 40\). Wie \(15\%\) van \(46\) aftrekt, vindt \(39{,}10\) euro: dat is fout.",
    ),
    keuze(
        r"Een stijging van \(100\%\) is een [[*verdubbeling|verdrievoudiging|halvering]]. Een daling van \(50\%\) is een [[*halvering|verdubbeling|verdwijning]].",
        r"\(100\%\) erbij geeft \(200\%\) van het begin. \(50\%\) eraf laat de helft over.",
    ),
    mk(
        r"In een straat kosten negen huizen ongeveer \(300\,000\) euro en één villa \(3\) miljoen euro. Een makelaar wil de straat duur laten lijken. Welk cijfer kiest hij?",
        [r"de mediaan: \(300\,000\) euro", r"het gemiddelde: \(570\,000\) euro", r"de modus: \(300\,000\) euro", r"de variatiebreedte: \(2{,}7\) miljoen euro"],
        1,
        r"\(\tfrac{9 \cdot 300\,000 + 3\,000\,000}{10} = 570\,000\) euro. De ene villa trekt het gemiddelde omhoog; de mediaan blijft \(300\,000\) euro.",
    ),
    mk(
        r"Op de tijdas van een lijndiagram staan \(2018\), \(2019\), \(2022\) en \(2025\) op gelijke afstanden. Waarom is dat misleidend?",
        [
            "de stappen tussen de jaren zijn ongelijk, dus de helling van de lijn klopt niet",
            "een tijdas hoort altijd van rechts naar links te lopen",
            "jaartallen horen op de verticale as te staan",
            "een lijndiagram mag je nooit gebruiken voor jaren",
        ],
        0,
        "Van 2019 naar 2022 zijn drie jaar, maar het lijkt één stap. Een groei over drie jaar lijkt dan een groei in één jaar.",
    ),
    inv(
        r"Een school telt \(600\) leerlingen. Van de \(24\) leerlingen die stemden, stemden er \(18\) ja. Een affiche zegt: 'Driekwart van de school is voor!' Hoeveel procent van alle leerlingen stemde echt ja?",
        ["3", "3%", "3 %"],
        r"\(\tfrac{18}{600} = 0{,}03 = 3\%\). Driekwart klopt enkel voor wie stemde.",
    ),
    mk(
        r"Een nieuwe app meldt: 'Ons aantal gebruikers steeg met \(300\%\)!' Vorige maand waren er \(5\) gebruikers. Hoeveel zijn er nu?",
        [r"\(15\)", r"\(20\)", r"\(300\)", r"\(305\)"],
        1,
        r"\(300\%\) erbij betekent \(5 + 3 \cdot 5 = 20\) gebruikers. Een groot percentage op een klein aantal blijft klein.",
    ),
]

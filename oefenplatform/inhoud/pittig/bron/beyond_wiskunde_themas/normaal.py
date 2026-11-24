"""Statistiek: normale verdeling en hypothesetoets — pittig (🌍 Beyond doorstroom)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone

GRAF = venster("normaal-twee-klokken-bey", 20, 110, 0, 0.09, 10, 0.01)


def _n(mu, s):
    return lambda x: math.exp(-((x - mu) / s) ** 2 / 2) / (s * math.sqrt(2 * math.pi))


GRAFIEKEN = [
    dict(naam=GRAF, titel="Twee normale verdelingen A en B",
         krommen=[(_n(60, 10), "groen", "A", (20, 110)), (_n(80, 5), "blauw", "B", (20, 110))],
         labelplek={"A": (44, 0.037), "B": (89, 0.07)}, xlabel="x", ylabel=""),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="twee klokkrommen N(60, 10²) en N(80, 5²)", vragen="klikvragen over gemiddelde, spreiding en de 95-procentregel")]

VRAGEN = [
    klik(
        "Klik op de top van de verdeling met de kleinste standaardafwijking.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 80, _n(80, 5)(80))],
        "De smalste en hoogste klok heeft de kleinste spreiding: B.",
    ),
    klik(
        r"Verdeling A heeft \(\sigma = 10\). Klik op de plaats op de x-as waarboven ongeveer 2,5 % van de metingen van A ligt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 80, 0)],
        r"Binnen \(\mu \pm 2\sigma\) ligt ongeveer 95 %, dus boven \(\mu + 2\sigma\) ongeveer 2,5 %.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de twee klokken. Juist of fout?",
        [("A heeft het kleinste gemiddelde.", J), ("De oppervlakte onder B is groter dan die onder A, omdat B hoger is.", F), ("Bij A ligt ongeveer de helft van de metingen onder 60.", J), ("De twee verdelingen hebben dezelfde spreiding.", F)],
        "Onder elke klok is de oppervlakte 1: een smallere klok is daardoor hoger.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        r"\(X \sim N(70,\ 5^{2})\). Ongeveer hoeveel procent?",
        [(r"\(P(65 < X < 75)\)", "68 %"), (r"\(P(60 < X < 80)\)", "95 %"), (r"\(P(X > 80)\)", "2,5 %"), (r"\(P(X < 70)\)", "50 %")],
        r"68 % binnen \(\mu \pm \sigma\), 95 % binnen \(\mu \pm 2\sigma\); de klok is symmetrisch rond 70.",
        kolommen=["68 %", "95 %", "2,5 %", "50 %"],
    ),
    casus(
        "Lies haalt 72 op een toets met gemiddelde 60 en standaardafwijking 8. Tom haalt 85 op een andere toets met gemiddelde 75 en standaardafwijking 5.",
        [
            inv("Welke z-score heeft Lies? Geef een decimaal getal.", ["1,5", "1.5"], r"\(\tfrac{72 - 60}{8}\)."),
            inv("Welke z-score heeft Tom?", ["2", "twee"], r"\(\tfrac{85 - 75}{5}\)."),
            mk("Wie deed het relatief het best?", ["Tom, want zijn z-score is hoger", "Lies, want haar punt is hoger boven het gemiddelde", "Tom, want 85 is meer dan 72", "even goed, want beiden zitten boven het gemiddelde"], 0,
               "De z-score vergelijkt over verdelingen heen."),
        ],
    ),
    inv(
        r"\(X \sim N(50,\ 4^{2})\). Welke meting heeft z-score \(-1{,}5\)?",
        ["44", "vierenveertig"],
        r"\(x = \mu + z\sigma = 50 - 6\).",
    ),
    mk(
        "Van 1000 leerlingen is de lengte normaal verdeeld. Ongeveer hoeveel leerlingen zijn groter dan het gemiddelde plus één standaardafwijking?",
        ["160", "340", "320", "25"],
        0,
        "Buiten μ ± σ ligt ongeveer 32 %, de helft daarvan rechts.",
    ),
    mk(
        "IQ is normaal verdeeld met gemiddelde 100 en standaardafwijking 15. Hoe groot is ongeveer de kans op een IQ boven 130?",
        ["2,5 %", "5 %", "16 %", "0,15 %"],
        0,
        r"130 ligt \(2\sigma\) boven \(\mu\).",
    ),
    tabel(
        "Over de normale verdeling: juist of fout?",
        [(r"Bij \(N(\mu, \sigma^{2})\) is \(P(X \leq \mu) = 0{,}5\).", J), (r"Bij een normale verdeling is \(P(X = \mu)\) de grootste kans.", F), (r"\(P(X < a) = P(X \leq a)\) bij een continue verdeling.", J), (r"Een grotere \(\sigma\) maakt de klok hoger.", F)],
        r"Een afzonderlijke waarde heeft kans 0; een grotere \(\sigma\) maakt de klok breder en lager.",
        kolommen=["Juist", "Fout"],
    ),
    koppel(
        "Verbind het begrip met zijn betekenis.",
        [("type I-fout", r"\(H_{0}\) verwerpen terwijl ze waar is"), ("type II-fout", r"\(H_{0}\) niet verwerpen terwijl ze fout is"), ("p-waarde", r"kans op zo'n resultaat of extremer als \(H_{0}\) waar is"), ("significantieniveau", "vooraf gekozen grens voor de p-waarde")],
        [r"de kans dat \(H_{0}\) waar is"],
        "De p-waarde is niet de kans dat de nulhypothese klopt.",
    ),
    sorteer(
        r"Verwerp je \(H_{0}\)?",
        [r"Verwerpen", r"Niet verwerpen"],
        [(r"\(p = 0{,}02\) en \(\alpha = 0{,}05\)", r"Verwerpen"), (r"\(p = 0{,}08\) en \(\alpha = 0{,}05\)", r"Niet verwerpen"), (r"\(p = 0{,}004\) en \(\alpha = 0{,}01\)", r"Verwerpen"),
         (r"\(p = 0{,}03\) en \(\alpha = 0{,}01\)", r"Niet verwerpen"), (r"\(p = 0{,}049\) en \(\alpha = 0{,}05\)", r"Verwerpen"), (r"\(p = 0{,}5\) en \(\alpha = 0{,}1\)", r"Niet verwerpen")],
        r"Verwerp \(H_{0}\) als \(p < \alpha\).",
    ),
    volgorde(
        "Zet de stappen van een hypothesetoets in volgorde.",
        [r"formuleer \(H_{0}\) en de alternatieve hypothese", r"kies het significantieniveau \(\alpha\)", "verzamel de gegevens met een aselecte steekproef", "bereken de p-waarde", r"vergelijk met \(\alpha\) en besluit"],
        "Kies α vooraf, niet nadat je de p-waarde kent.",
    ),
    casus(
        "Een fabrikant beweert dat een munt eerlijk is. Jij vermoedt dat ze vaker kop geeft. Je gooit 100 keer.",
        [
            mk(r"Wat is \(H_{0}\)?", [r"\(p = 0{,}5\)", r"\(p > 0{,}5\)", r"\(p < 0{,}5\)", r"\(p \neq 0{,}5\)"], 0, "De nulhypothese is de bewering van de fabrikant."),
            mk("Welke toets past?", ["eenzijdig, want je verwacht een richting", "tweezijdig, want een munt heeft twee kanten", "eenzijdig, want je gooit maar één munt", "geen toets, want 100 worpen is te weinig"], 0, "Je vermoedt alleen 'vaker kop'."),
            mk(r"De p-waarde is 0,08 bij \(\alpha = 0{,}05\). Wat besluit je?", ["er is onvoldoende bewijs dat de munt vaker kop geeft", "de munt is eerlijk, dat is nu met zekerheid bewezen", "de munt geeft vaker kop, want 0,08 is een kleine kans", "je verhoogt α achteraf tot 0,1 en verwerpt dan toch"], 0,
               r"Niet verwerpen betekent niet dat \(H_{0}\) bewezen is."),
        ],
    ),
    keuze(
        r"Kies je \(\alpha\) kleiner, dan wordt de kans op een type I-fout [[*kleiner|groter]] en de kans op een type II-fout [[*groter|kleiner]].",
        "Strenger zijn tegen onterecht verwerpen maakt het moeilijker om een echt effect te vinden.",
    ),
    sorteer(
        "Is de steekproef aselect of niet?",
        ["Aselect", "Niet aselect"],
        [("met een loting 50 nummers uit de leerlingenlijst trekken", "Aselect"), ("de eerste 50 leerlingen aan de schoolpoort bevragen", "Niet aselect"), ("een online peiling waar wie wil op stemt", "Niet aselect"),
         ("met een computer 200 adressen willekeurig uit het bevolkingsregister kiezen", "Aselect"), ("enkel je vrienden bevragen", "Niet aselect"), ("elk lid evenveel kans geven via een genummerde trekking", "Aselect")],
        "Aselect betekent: iedereen evenveel kans om gekozen te worden.",
    ),
    tabel(
        "Steekproeffout of niet-steekproeffout?",
        [("Door toeval zitten er net iets meer meisjes in de steekproef.", "steekproeffout"), ("De vraag is suggestief gesteld.", "niet-steekproeffout"), ("Veel mensen antwoorden niet op de enquête.", "niet-steekproeffout"), ("Twee aselecte steekproeven geven een iets ander gemiddelde.", "steekproeffout")],
        "Een steekproeffout komt door het toeval van de trekking; de rest komt door de opzet.",
        kolommen=["steekproeffout", "niet-steekproeffout"],
    ),
    mk(
        "Een onderzoek vindt r = −0,9 tussen uren gamen en toetsresultaat. Wat mag je besluiten?",
        ["er is een sterk dalend lineair verband", "gamen veroorzaakt slechte resultaten", "er is geen verband, want r is negatief", "er is een zwak maar stijgend verband"],
        0,
        "Een sterke correlatie zegt niets over oorzaak en gevolg.",
    ),
    inv(
        r"\(X \sim N(\mu,\ 3^{2})\) en een meting van 81 heeft z-score 2. Hoeveel is \(\mu\)?",
        ["75", "vijfenzeventig"],
        r"\(81 = \mu + 2 \cdot 3\).",
    ),
    tabel(
        "Over hypothesetoetsen en steekproeven: juist of fout?",
        [(r"Een p-waarde van 0,03 betekent dat \(H_{0}\) met 3 % kans waar is.", F), ("Een grotere steekproef verkleint de steekproeffout.", J), (r"Je kan \(H_{0}\) nooit met zekerheid bewijzen met een toets.", J), ("Bij een tweezijdige toets kijk je naar afwijkingen in beide richtingen.", J)],
        r"De p-waarde rekent met de veronderstelling dat \(H_{0}\) waar is; ze geeft niet de kans erop.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"De z-score is [[\(\tfrac{x - \mu}{\sigma}\)]]. Een meting met \(z = 0\) ligt precies op [[het gemiddelde]].",
        [r"\(\tfrac{x - \sigma}{\mu}\)", "de standaardafwijking"],
        "De z-score telt hoeveel standaardafwijkingen je van het gemiddelde ligt.",
    ),
    mk(
        "Een histogram heeft rechts een lange staart. Is de normale verdeling een goed model?",
        ["nee, want een normale verdeling is symmetrisch", "ja, als je een grote σ kiest die de staart opvangt", "ja, als je μ naar rechts schuift tot in de staart", "ja, want elke meting is normaal verdeeld"],
        0,
        "Een normale verdeling is symmetrisch: een scheve verdeling past er niet bij.",
    ),
    mk(
        r"Bij \(X \sim N(20,\ 2^{2})\) bereken je \(P(X > 23)\) met de rekenapp. Welke z-score hoort bij 23?",
        ["1,5", "3", "0,67", "11,5"],
        0,
        r"\(\tfrac{23 - 20}{2}\).",
    ),
    inv(
        r"\(X \sim N(40,\ 3^{2})\). Ongeveer hoeveel procent van de metingen ligt tussen 40 en 46? Geef een decimaal getal.",
        ["47,5", "47.5"],
        "46 ligt 2σ boven 40: de helft van 95 %, want de klok is symmetrisch.",
    ),
    inv(
        r"Bij \(N(100,\ \sigma^{2})\) ligt ongeveer 95 % van de metingen tussen 80 en 120. Hoeveel is \(\sigma\)?",
        ["10", "tien"],
        r"\(\mu \pm 2\sigma = 100 \pm 20\).",
    ),
    koppel(
        "Verbind de correlatiecoëfficiënt met de puntenwolk.",
        [(r"\(r = 0{,}95\)", "punten dicht bij een stijgende rechte"), (r"\(r = -0{,}3\)", "een zwak dalend patroon"), (r"\(r = 0{,}02\)", "geen lineair patroon"), (r"\(r = 0{,}5\)", "een matig stijgend patroon")],
        ["punten dicht bij een dalende rechte"],
        "Het teken geeft de richting, de grootte de sterkte.",
    ),
    mk(
        "Waarom deel je bij de z-score door σ?",
        ["om verdelingen met een andere spreiding te vergelijken", "om de oppervlakte onder de klok gelijk aan 1 te maken", "omdat een z-score anders altijd negatief zou zijn", "om het gemiddelde van de meting af te trekken"],
        0,
        "Zo meet je de afstand tot het gemiddelde in standaardafwijkingen.",
    ),
]

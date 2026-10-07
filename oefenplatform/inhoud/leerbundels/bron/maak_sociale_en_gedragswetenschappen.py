# -*- coding: utf-8 -*-
"""De leerbundels voor sociale en gedragswetenschappen op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche sociale en gedragswetenschappen 2DO, geldig vanaf
1 januari 2027. Die fiche geldt voor één richting: humane wetenschappen. Ze
weegt gedragswetenschappen 60 % en sociale wetenschappen 40 %, en de zestien
thema's volgen dat.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py
../../boost-doorstroom/sociale-en-gedragswetenschappen.json` doet daar het
voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, want een titel alleen is binnen een vak geen sleutel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Sociale en gedragswetenschappen"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. Ontwikkeling: groeien, rijpen en leren
zet("ontwikkeling-groeien-rijpen-en-leren",
    titel="Ontwikkeling: groeien, rijpen en leren",
    onder="Waaruit ontwikkeling bestaat, welke levensloopfasen een mens doorloopt, en wat nature, nurture en zelfbepaling eraan bijdragen.",
    secties=[
        dict(kop="Drie dingen tegelijk: groeien, rijpen en leren", blokken=[
            ("p", "Ontwikkeling is geen enkel woord voor één ding. Ze bestaat uit <strong>groeien, rijpen en "
                  "leren</strong>, en die drie lopen je hele leven door elkaar."),
            ("p", "<strong>Groeien</strong> is de zuiver lichamelijke toename: je wordt langer, zwaarder, groter. "
                  "Een baby die in een jaar <strong>twintig centimeter langer</strong> wordt, groeit. "
                  "<strong>Vijf centimeter langer worden</strong>, <strong>drie kilo bijkomen</strong> en "
                  "<strong>een grotere schoenmaat krijgen</strong> zijn alle drie groeien: er komt letterlijk "
                  "lichaam bij."),
            ("p", "<strong>Rijpen</strong> is wat vanzelf komt, zonder dat je het oefent. Het zit in je "
                  "lichaam ingebakken en wacht alleen op zijn moment. Een baby die zijn "
                  "<strong>eerste tandjes</strong> krijgt, rijpt: niemand heeft hem dat geleerd. Hetzelfde "
                  "geldt voor de puberteit of voor het ogenblik waarop de spieren sterk genoeg zijn om te "
                  "stappen."),
            ("p", "<strong>Leren</strong> is wat er door ervaring en oefening bij komt. Een kind dat "
                  "<strong>leert fietsen na veel vallen en opstaan</strong>, leert: zonder die uren op de "
                  "fiets gebeurt er niets."),
            ("kader", "Rijpen en leren hebben elkaar <strong>nodig</strong>. Je kan een kind niet leren "
                      "fietsen voor zijn evenwicht gerijpt is, en het rijpste evenwicht brengt niemand "
                      "vanzelf op een fiets. Het één opent de deur, het ander zet de stap."),
        ]),
        dict(kop="De negen levensloopfasen", blokken=[
            ("p", "De fiche onderscheidt <strong>negen levensloopfasen</strong>. Ze beginnen al vóór de "
                  "geboorte en lopen door tot het einde van het leven."),
            ("kader", tabel(["fase", "ongeveer"],
                            [["de <strong>prenatale fase</strong>", "vóór de geboorte, negen maanden"],
                             ["de <strong>babytijd</strong>", "0 tot 1 jaar"],
                             ["de <strong>peutertijd</strong>", "1 tot 3 jaar"],
                             ["de <strong>kleutertijd</strong>", "3 tot 6 jaar"],
                             ["de <strong>lagereschoolkindfase</strong>", "6 tot 12 jaar"],
                             ["de <strong>adolescentie</strong>", "12 tot ongeveer 20 jaar"],
                             ["de <strong>vroege volwassenheid</strong>", "20 tot 40 jaar"],
                             ["de <strong>middenvolwassenheid</strong>", "40 tot 65 jaar"],
                             ["de <strong>late volwassenheid</strong>", "vanaf ongeveer 65 jaar"]])),
            ("p", "De <strong>prenatale fase</strong> komt dus vóór de geboorte, en ze is meteen de fase die "
                  "in de levensloop <strong>het kortst duurt</strong>: negen maanden tegenover de tientallen "
                  "jaren van de volwassenheid."),
            ("p", "De <strong>kindertijd</strong> bundelt de <strong>peutertijd</strong>, de "
                  "<strong>kleutertijd</strong> en de <strong>lagereschoolkindfase</strong>. De "
                  "<strong>adolescentie</strong> is de fase tussen de kindertijd en de volwassenheid. Een "
                  "vrouw van <strong>72 die met pensioen is</strong>, zit in de <strong>late "
                  "volwassenheid</strong>."),
            ("p", "Men spreekt bewust van <strong>levensloopfasen en niet van leeftijdsgroepen</strong>, "
                  "<strong>omdat de grenzen verschuiven</strong>. De ene puber is op zijn elfde al volop "
                  "adolescent, de andere pas op zijn veertiende. Een leeftijd is een getal; een fase is een "
                  "stuk van een leven."),
            ("weetje", "Een <strong>peuter die bij alles nee zegt</strong>, zit midden in de "
                       "<strong>peutertijd</strong>. Dat nee is geen stoutheid maar ontwikkeling: het kind "
                       "ontdekt dat het een eigen wil heeft die los staat van die van zijn ouders."),
        ]),
        dict(kop="Ontwikkeling is een proces", blokken=[
            ("p", "Ontwikkeling <strong>stopt niet bij de volwassenheid</strong>. Ook een mens van veertig of "
                  "van tachtig verandert nog: in denken, in relaties, in wat hij belangrijk vindt. Dat is "
                  "precies waarom de fiche fasen tot in de late volwassenheid opsomt."),
            ("p", "Ontwikkeling is bovendien een <strong>proces</strong>, en daarvoor gelden drie dingen. Het "
                  "<strong>gebeurt stap na stap</strong>, <strong>elke stap bouwt op de vorige</strong>, en een "
                  "<strong>fase overslaan lukt moeilijk</strong>. Een kind kruipt voor het stapt, en stapt voor "
                  "het loopt."),
            ("p", "Ook de verhoudingen van het lichaam veranderen mee. De <strong>lichaamsverhoudingen van een "
                  "baby zijn niet dezelfde als die van een volwassene</strong>: het hoofd van een baby is in "
                  "verhouding veel groter, de benen veel korter. Groeien is dus niet gewoon alles evenveel "
                  "vergroten."),
            ("weetje", "Een <strong>adolescent die verschillende vriendengroepen uitprobeert</strong>, doet dat "
                       "<strong>omdat hij zoekt wie hij zelf is</strong>. Die zoektocht naar een eigen identiteit "
                       "is het werk van die fase."),
        ]),
        dict(kop="Nature, nurture en zelfbepaling", blokken=[
            ("p", "Waar komt die ontwikkeling vandaan? De fiche noemt drie factoren."),
            ("p", "<strong>Nature</strong> is <strong>de erfelijkheid</strong>: alles wat in je genen meekomt. "
                  "<strong>Je bloedgroep</strong>, <strong>je lichaamslengte als mogelijkheid</strong> en "
                  "<strong>een erfelijke aandoening</strong> horen bij nature. Let op dat woord "
                  "<em>mogelijkheid</em>: je genen bepalen hoe lang je zou kunnen worden, niet hoe lang je "
                  "wordt."),
            ("p", "<strong>Nurture</strong> is alles wat de omgeving aanbrengt: <strong>de school waar je "
                  "zit</strong>, <strong>de buurt waar je woont</strong>, <strong>de taal die thuis gesproken "
                  "wordt</strong>, de vrienden, het eten, de kansen."),
            ("p", "<strong>Zelfbepaling</strong> is de derde factor: de mens kiest ook zelf. Maar "
                  "<strong>zelfbepaling betekent niet dat je je ontwikkeling volledig zelf kiest</strong>. Je "
                  "kiest binnen wat nature en nurture je meegeven, en dat is iets anders dan vrij spel."),
            ("kader", "<strong>Nature en nurture werken samen.</strong> Een jongen die "
                      "<strong>muzikaal talent erft maar nooit oefent</strong>, mist <strong>de "
                      "oefening</strong>: de aanleg alleen levert niets op. Een <strong>tweeling die in twee "
                      "verschillende gezinnen opgroeit en sterk verschilt</strong>, toont <strong>het gewicht "
                      "van nurture</strong>: dezelfde genen, een ander resultaat. En een kind met een "
                      "spraakachterstand dat <strong>logopedie</strong> krijgt en de achterstand inhaalt, is "
                      "<strong>nurture</strong> aan het werk. In het Engels heet die wisselwerking kortweg "
                      "<strong>nature en nurture</strong>."),
        ]),
        dict(kop="De vijf ontwikkelingsdomeinen", blokken=[
            ("p", "Om overzicht te houden, verdeelt men de ontwikkeling in <strong>domeinen</strong>. De fiche "
                  "noemt er vijf: <strong>de fysieke</strong>, de cognitieve, <strong>de morele</strong>, de "
                  "socio-emotionele en <strong>de persoonlijkheidsontwikkeling</strong>. Die laatste is in de "
                  "fiche dus <strong>een eigen ontwikkelingsdomein</strong> en geen onderdeel van een ander."),
            ("kader", tabel(["domein", "waarover het gaat"],
                            [["de <strong>fysieke</strong> ontwikkeling", "het lichaam, de motoriek, de zintuigen"],
                             ["de <strong>cognitieve</strong> ontwikkeling", "<strong>het denken</strong>, het geheugen, de taal"],
                             ["de <strong>morele</strong> ontwikkeling", "<strong>goed en kwaad</strong>, waarden, geweten"],
                             ["de <strong>socio-emotionele</strong> ontwikkeling", "<strong>gevoelens en omgaan met anderen</strong>"],
                             ["de <strong>persoonlijkheids</strong>ontwikkeling", "wie iemand als persoon wordt"]])),
            ("p", "Die domeinen <strong>gaan niet los van elkaar vooruit</strong>. Een <strong>kleuter die leert "
                  "stappen en daardoor ook de keuken gaat verkennen</strong>, laat de "
                  "<strong>wisselwerking</strong> zien: een fysieke stap zet een cognitieve stap in gang."),
            ("p", "Waarom dan toch onderscheiden? <strong>Om gerichter te kijken.</strong> Wie weet welk domein "
                  "hij volgt, ziet meer dan wie alleen naar het kind in het algemeen kijkt. In de "
                  "<strong>late volwassenheid</strong> gaat <strong>het fysieke</strong> domein het duidelijkst "
                  "achteruit, terwijl het cognitieve op veel punten nog wint."),
            ("p", "De fiche vraagt ook om <strong>twee levensloopfasen binnen één domein met elkaar te "
                  "vergelijken</strong>: hoe denkt een kleuter tegenover een adolescent, hoe beweegt een baby "
                  "tegenover een oudere. Dat is een vergelijking in de breedte van één domein, niet een "
                  "opsomming van alles."),
        ]),
    ])

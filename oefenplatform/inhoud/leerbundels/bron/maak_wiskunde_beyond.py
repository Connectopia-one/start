# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde gevorderd op 🌍 Beyond-niveau.

Gebaseerd op de drie vakfiches wiskunde 3de graad doorstroomfinaliteit
(G1, G2 en G3), geldig vanaf 1 januari 2027. Alle drie gelden ze voor
economie-wiskunde, Latijn-wiskunde-wetenschappen en wetenschappen-wiskunde:
het zijn drie examens van hetzelfde vak, dus één vak op het platform.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/wiskunde-gevorderd.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond". Dat is nodig en niet alleen netjes:
Boost doorstroom heeft een vak met precies dezelfde naam, en daar staan
thema's met verwante titels in. De pdf's komen dus naast elkaar in
`leerbundels/wiskunde-gevorderd/` terecht.

Wiskunde staat hier in echte notatie, tussen \( en \). Enya Vermeyen,
leerkracht wiskunde, keek op 10 oktober 2026 naar het eerste hoofdstuk toen
alles nog in woorden stond en had gelijk: een leerling van de derde graad moet
\(a^{2/3}\) kunnen lezen. Zie oefenplatform/lib/wiskunde.ts.

De omzetting gebeurt thema per thema, samen met de vragen van dat thema, zodat
een kind in de bundel dezelfde schrijfwijze terugvindt als in de oefening.
Omgezet: thema 1 tot 12. De andere thema's staan nog in woorden.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Wiskunde gevorderd"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Machtswortels, machten en logaritmen
BUNDELS["machtswortels-machten-en-logaritmen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Machtswortels, machten en logaritmen",
    onder="Rekenen met rationale exponenten, en de logaritme als de exponent die je zoekt.",
    secties=[
        dict(kop="Machten met een gehele exponent", blokken=[
            ("p", r"Je kent de machten met een natuurlijke exponent al. Daar komen twee afspraken bij. "
                  r"<strong>\(a^{0}=1\) voor elke \(a\neq 0\).</strong> Dat is geen willekeurige afspraak: "
                  r"\(\dfrac{a^{n}}{a^{n}}\) is enerzijds \(1\), en anderzijds \(a^{n-n}=a^{0}\). En "
                  r"<strong>\(a^{-n}=\dfrac{1}{a^{n}}\)</strong>. Een negatieve exponent betekent dus "
                  r"<strong>omkeren, niet van teken veranderen</strong>: \(2^{-3}=\tfrac{1}{8}\) en niet \(-8\)."),
            ("p", tabel(["Rekenregel", "Wat je met de exponenten doet", "Voorbeeld"], [
                [r"\(a^{m}\cdot a^{n}\)", "je telt ze op", r"\(a^{m}\cdot a^{n}=a^{m+n}\)"],
                [r"\(\dfrac{a^{m}}{a^{n}}\)", "je trekt ze af", r"\(\dfrac{a^{-2}b^{3}}{a^{3}b^{-1}}=a^{-5}b^{4}=\dfrac{b^{4}}{a^{5}}\)"],
                [r"\(\left(a^{m}\right)^{n}\)", "je vermenigvuldigt ze", r"\(\left(a^{2}\right)^{3}=a^{6}\)"],
                [r"\((ab)^{n}\)", "elke factor krijgt die macht", r"\((ab)^{n}=a^{n}b^{n}\)"],
            ])),
            ("p", r"Met die regels los je een vergelijking met gelijke grondtallen op zonder logaritme. "
                  r"Uit \(2^{x}\cdot 2^{x+3}=2^{11}\) volgt \(2^{2x+3}=2^{11}\), dus \(2x+3=11\) en \(x=4\)."),
            ("kader", r"Een macht verdeelt zich over een <strong>product</strong> en over een "
                      r"<strong>quotiënt</strong>, maar <strong>nooit over een som</strong>: "
                      r"\((a+b)^{n}\neq a^{n}+b^{n}\). Dat geldt ook voor wortels en straks voor "
                      r"logaritmen. Het is de fout die het vaakst gemaakt wordt."),
        ]),
        dict(kop="Machtswortels", blokken=[
            ("p", r"De <strong>n-de machtswortel uit \(a\)</strong>, geschreven \(\sqrt[n]{a}\), is het getal "
                  r"waarvan de n-de macht \(a\) is. Zo is \(\sqrt[5]{32}=2\), want \(2^{5}=32\), en "
                  r"\(\sqrt[3]{-8}=-2\), want \((-2)^{3}=-8\)."),
            ("p", r"<strong>\(\sqrt[n]{a}\) met \(a<0\) bestaat in \(\mathbb{R}\) alleen als \(n\) oneven "
                  r"is.</strong> Een even macht van een reëel getal is immers nooit negatief, dus "
                  r"\(\sqrt{-16}\) en \(\sqrt[4]{-16}\) bestaan niet in \(\mathbb{R}\). Daaruit volgt ook "
                  r"het domein van een wortelfunctie: \(\sqrt[4]{x-3}\) bestaat voor \(x-3\geq 0\), dus "
                  r"voor \(x\geq 3\). Bij \(x=3\) is de wortel \(0\), en dat mag."),
            ("kader", r"<strong>\(\sqrt{a^{2}}=|a|\), niet \(a\).</strong> Een vierkantswortel is nooit "
                      r"negatief. Neem \(a=-3\): \(\sqrt{(-3)^{2}}=\sqrt{9}=3\) en niet \(-3\). Bij een "
                      r"oneven wortelexponent is er geen absolute waarde nodig: \(\sqrt[3]{a^{3}}=a\)."),
        ]),
        dict(kop="Machten met een rationale exponent", blokken=[
            ("p", r"Een macht met een <strong>rationale exponent</strong> is niets anders dan een wortel: "
                  r"<strong>\(a^{1/n}=\sqrt[n]{a}\)</strong> en algemeen "
                  r"<strong>\(a^{m/n}=\sqrt[n]{a^{m}}=\left(\sqrt[n]{a}\right)^{m}\)</strong>. De noemer van "
                  r"de exponent wordt de wortelexponent, de teller blijft de macht. Reken altijd eerst de "
                  r"wortel uit en kwadrateer daarna: dat houdt de getallen klein."),
            ("p", tabel(["Uitdrukking", "Hoe je ze leest", "Uitkomst"], [
                [r"\(8^{2/3}\)", r"\(\sqrt[3]{8}=2\), dan kwadrateren", r"\(4\)"],
                [r"\(16^{3/4}\)", r"\(\sqrt[4]{16}=2\), dan tot de derde", r"\(8\)"],
                [r"\(64^{1/6}\)", r"\(\sqrt[6]{64}\)", r"\(2\)"],
                [r"\(4^{3/2}\)", r"\(\sqrt{4}=2\), dan tot de derde", r"\(8\), en dus niet \(6\)"],
                [r"\(\left(\tfrac{8}{27}\right)^{-2/3}\)", r"eerst omkeren, dan de derdemachtswortel, dan kwadrateren", r"\(\tfrac{9}{4}\)"],
            ])),
            ("p", r"Omdat \(\left(a^{m}\right)^{n}=a^{mn}\) ook geldt voor breuken, mag je wortels gewoon "
                  r"samenvoegen: \(\sqrt{a}\cdot\sqrt[3]{a}=a^{1/2}\cdot a^{1/3}=a^{5/6}\), en "
                  r"\(\sqrt{2}\cdot\sqrt[3]{2}\cdot\sqrt[6]{2}=2^{1/2+1/3+1/6}=2^{1}=2\). Een vergelijking "
                  r"als \(x^{3/4}=8\) los je op door beide leden tot de macht \(\tfrac{4}{3}\) te verheffen: "
                  r"\(x=8^{4/3}=16\)."),
            ("p", r"Rationale exponenten maken getallen ook vergelijkbaar. Welk getal is het grootst, "
                  r"\(2^{1/2}\), \(3^{1/3}\), \(5^{1/5}\) of \(6^{1/6}\)? Verhef alles tot de macht \(6\): "
                  r"\(2^{3}=8\), \(3^{2}=9\), \(5^{6/5}\approx 6{,}9\) en \(6^{1}=6\). Dus \(3^{1/3}\) is het grootst."),
            ("weetje", r"<strong>\(a^{m/n}\) is afgesproken voor \(a\geq 0\).</strong> Bij een negatief "
                       r"grondtal zou dezelfde exponent, anders geschreven, twee uitkomsten geven: "
                       r"\(\sqrt[3]{-8}=-2\) maar \(\sqrt[6]{(-8)^{2}}=\sqrt[6]{64}=2\), terwijl "
                       r"\(\tfrac{1}{3}=\tfrac{2}{6}\). Daarom blijft die schrijfwijze bij niet-negatieve "
                       r"grondtallen, ook al bestaat \(\sqrt[3]{-8}\) gewoon."),
        ]),
        dict(kop="Wortels vereenvoudigen", blokken=[
            ("p", r"Een wortel schrijf je <strong>zo eenvoudig mogelijk</strong> door er de volkomen machten "
                  r"uit te halen: \(\sqrt{50}=\sqrt{25\cdot 2}=5\sqrt{2}\), \(\sqrt{72}=6\sqrt{2}\) en "
                  r"\(\sqrt[3]{54}=\sqrt[3]{27\cdot 2}=3\sqrt[3]{2}\). Bij letters deel je elke exponent "
                  r"door de wortelexponent: \(\sqrt[4]{16a^{8}b^{12}}=2a^{2}b^{3}\) voor \(a,b>0\)."),
            ("p", r"Zijn de wortels na het vereenvoudigen gelijk, dan kan je ze optellen: "
                  r"\(\sqrt{50}+\sqrt{18}-\sqrt{8}=5\sqrt{2}+3\sqrt{2}-2\sqrt{2}=6\sqrt{2}\)."),
            ("kader", r"<strong>\(\sqrt{a+b}\neq\sqrt{a}+\sqrt{b}\).</strong> Probeer het met \(9\) en "
                      r"\(16\): \(\sqrt{25}=5\), maar \(3+4=7\)."),
            ("p", r"Een breuk met een wortel in de noemer maak je netter door de <strong>noemer rationaal "
                  r"te maken</strong>. Staat er één wortel, dan vermenigvuldig je teller en noemer met "
                  r"diezelfde wortel: \(\dfrac{1}{\sqrt{3}}=\dfrac{\sqrt{3}}{3}\). Staat er een verschil, "
                  r"dan neem je het <strong>toegevoegde tweeterm</strong>: "
                  r"\(\dfrac{6}{\sqrt{5}-\sqrt{2}}=\dfrac{6\left(\sqrt{5}+\sqrt{2}\right)}{5-2}"
                  r"=2\left(\sqrt{5}+\sqrt{2}\right)\)."),
        ]),
        dict(kop="De logaritme is een exponent", blokken=[
            ("p", r"<strong>\(\log_{a}x\) is de exponent waartoe je \(a\) verheft om \(x\) te krijgen.</strong> "
                  r"Meer is het niet. Zo is \(\log_{2}8=3\) want \(2^{3}=8\), \(\log_{3}81=4\) want "
                  r"\(3^{4}=81\), en \(\log_{2}16=4\) — niet \(8\). Ook negatieve uitkomsten horen erbij: "
                  r"\(\log_{5}\tfrac{1}{25}=-2\) want \(5^{-2}=\tfrac{1}{25}\), en \(\log_{1/2}8=-3\) want "
                  r"\(\left(\tfrac{1}{2}\right)^{-3}=8\)."),
            ("p", r"Staat er geen grondtal bij, dan bedoelt men <strong>grondtal \(10\)</strong>: "
                  r"\(\log 100=2\) en \(\log 0{,}001=-3\). Schrijft men <strong>\(\ln\)</strong>, dan is het "
                  r"grondtal <strong>\(e\approx 2{,}718\)</strong>, dus \(\ln e=1\). Het grondtal moet "
                  r"<strong>positief en verschillend van \(1\)</strong> zijn."),
            ("p", r"Het <strong>domein</strong> van een logaritme is \(\left]0,+\infty\right[\): "
                  r"\(a^{x}\) is altijd strikt positief, dus geen enkele exponent geeft \(0\) of een negatief "
                  r"getal. Daarom bestaat \(\log_{2}0\) niet, en vraagt \(f(x)=\ln\left(x^{2}-4\right)\) dat "
                  r"\(x^{2}-4>0\), dus \(x<-2\) of \(x>2\): "
                  r"\(\text{dom}\,f=\left]-\infty,-2\right[\;\cup\;\left]2,+\infty\right[\). De negatieve tak "
                  r"hoort er wél bij, want \((-3)^{2}-4=5>0\)."),
            ("p", tabel(["Rekenregel", "Waarom", "Voorbeeld"], [
                [r"\(\log_{a}(xy)=\log_{a}x+\log_{a}y\)", "machten tellen hun exponenten op", r"\(\log 2+\log 5=\log 10=1\)"],
                [r"\(\log_{a}\dfrac{x}{y}=\log_{a}x-\log_{a}y\)", "machten trekken hun exponenten af", r"\(\log_{2}\tfrac{8}{4}=3-2=1\)"],
                [r"\(\log_{a}x^{n}=n\log_{a}x\)", "een macht van een macht vermenigvuldigt", r"\(\log_{a}\sqrt[3]{x}=\tfrac{1}{3}\log_{a}x\)"],
                [r"\(\log_{a}1=0\)", r"\(a^{0}=1\) bij elk grondtal", r"elke grafiek \(y=\log_{a}x\) gaat door \((1,0)\)"],
            ])),
            ("p", r"Die drie regels samen ontleden elke uitdrukking: "
                  r"\(\log_{a}\dfrac{x^{3}\sqrt{y}}{z}=3\log_{a}x+\tfrac{1}{2}\log_{a}y-\log_{a}z\), want "
                  r"\(\sqrt{y}=y^{1/2}\)."),
            ("kader", r"<strong>\(\log(a+b)\neq\log a+\log b\).</strong> Die regel geldt voor een "
                      r"<strong>product</strong>. En <strong>\(\left(\ln x\right)^{2}\neq 2\ln x\)</strong>: "
                      r"\(2\ln x\) is \(\ln x^{2}\). Bij \(x=e\) is het kwadraat \(1\) en \(2\ln e=2\)."),
        ]),
        dict(kop="Waar je de logaritme voor gebruikt", blokken=[
            ("p", r"Een logaritme haalt de onbekende <strong>uit de exponent</strong>. Soms zie je het "
                  r"antwoord meteen: \(2^{x}=32\) geeft \(x=5\). Lukt dat niet, neem dan van beide leden de "
                  r"logaritme: uit \(3^{x}=20\) volgt \(x\ln 3=\ln 20\), dus "
                  r"\(x=\dfrac{\ln 20}{\ln 3}\approx 2{,}73\). Dat is tegelijk de regel voor het "
                  r"<strong>veranderen van grondtal</strong>: \(\log_{a}x=\dfrac{\ln x}{\ln a}\). Let op de "
                  r"volgorde — het getal waarvan je de logaritme zoekt staat boven, het oude grondtal onder. "
                  r"Daaruit volgt ook \(\log_{a}b\cdot\log_{b}a=1\) en "
                  r"\(\log_{2}5\cdot\log_{5}8=\log_{2}8=3\)."),
            ("p", r"Een logaritme en een macht met hetzelfde grondtal <strong>heffen elkaar op</strong>: "
                  r"\(10^{\log 7}=7\) en \(\ln\left(e^{x}\right)=x\) voor elke \(x\in\mathbb{R}\). Omgekeerd "
                  r"geldt \(e^{\ln x}=x\) enkel voor \(x>0\), want anders bestaat \(\ln x\) niet. Zo is "
                  r"\(e^{2\ln 3}=e^{\ln 9}=9\)."),
            ("p", r"Staat de onbekende twee keer in dezelfde macht, <strong>stel dan een hulponbekende</strong>. "
                  r"Bij \(2^{x+1}=5\cdot 2^{x}-12\) stel je \(t=2^{x}\): links staat \(2t\), dus \(2t=5t-12\), "
                  r"\(t=4\) en \(x=2\)."),
            ("kader", r"Zet je twee logaritmen samen, <strong>controleer dan het domein van je oplossing</strong>. "
                      r"\(\log_{2}x+\log_{2}(x-2)=3\) wordt \(x^{2}-2x-8=0\), met \(x=4\) of \(x=-2\). Maar "
                      r"\(\log_{2}(-2)\) bestaat niet, dus enkel \(x=4\) is een oplossing. Samenvoegen "
                      r"verbreedt het domein, en dan sluipen er valse oplossingen binnen."),
            ("p", r"Twee toepassingen die je buiten de wiskundeles terugvindt. <strong>Groei</strong>: een "
                  r"belegging aan \(4\%\) per jaar staat na \(n\) jaar op \(1{,}04^{n}\) keer het startbedrag, "
                  r"en \(1{,}04^{n}\geq 2\) geeft \(n\geq\dfrac{\ln 2}{\ln 1{,}04}\approx 17{,}7\): na "
                  r"\(18\) volle jaren is ze verdubbeld. <strong>Een logaritmische schaal</strong>: het "
                  r"geluidsniveau \(L=10\log\dfrac{I}{I_{0}}\) stijgt met \(10\log 100=20\) decibel wanneer "
                  r"de intensiteit honderd keer zo groot wordt."),
        ]),
    ],
    onthoud=[
        r"\(a^{0}=1\) voor elke \(a\neq 0\), en \(a^{-n}=\dfrac{1}{a^{n}}\): omkeren, niet van teken veranderen.",
        r"\(a^{m}\cdot a^{n}=a^{m+n}\), \(\dfrac{a^{m}}{a^{n}}=a^{m-n}\) en \(\left(a^{m}\right)^{n}=a^{mn}\).",
        r"Een macht of wortel verdeelt zich over een product en een quotiënt, nooit over een som.",
        r"\(a^{m/n}=\sqrt[n]{a^{m}}\), afgesproken voor \(a\geq 0\); en \(\sqrt{a^{2}}=|a|\).",
        r"\(\sqrt[n]{a}\) met \(a<0\) bestaat in \(\mathbb{R}\) alleen als \(n\) oneven is.",
        r"\(\sqrt{50}=5\sqrt{2}\); maak een noemer rationaal met het toegevoegde tweeterm.",
        r"\(\log_{a}x\) is de exponent waartoe je \(a\) verheft om \(x\) te krijgen; \(\text{dom}=\left]0,+\infty\right[\).",
        r"Zonder grondtal is het \(10\); \(\ln\) heeft grondtal \(e\approx 2{,}718\).",
        r"\(\log_{a}(xy)=\log_{a}x+\log_{a}y\), \(\log_{a}x^{n}=n\log_{a}x\), \(\log_{a}1=0\).",
        r"Veranderen van grondtal: \(\log_{a}x=\dfrac{\ln x}{\ln a}\).",
        r"Logaritmen samenvoegen? Controleer achteraf of je oplossing in het domein ligt.",
    ],
)

# ───────────────────────── 2. Veeltermen, deelbaarheid en Horner
BUNDELS["veeltermen-deelbaarheid-en-horner-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veeltermen, deelbaarheid en Horner",
    onder="De euclidische deling, de reststelling, het schema van Horner en het ontbinden in factoren.",
    secties=[
        dict(kop="De euclidische deling van veeltermen", blokken=[
            ("p", r"Delen van veeltermen werkt zoals delen van getallen. Je deelt \(A\) door \(B\) en krijgt "
                  r"een <strong>quotiënt</strong> \(Q\) en een <strong>rest</strong> \(R\), en er geldt "
                  r"altijd <strong>\(A=B\cdot Q+R\)</strong>. Dat is meteen de controle op elke deling; "
                  r"klopt ze niet, dan zit er een rekenfout in je schema."),
            ("p", r"Over de rest weet je één ding zeker: <strong>\(\deg R<\deg B\)</strong>. Zolang de rest "
                  r"nog even hoog in graad staat als de deler, kan je verder delen. Deel je door een "
                  r"<strong>tweedegraadsveelterm</strong>, dan is de rest dus hoogstens van de vorm "
                  r"\(ax+b\). <strong>Gaat een deling op, dan is \(R=0\)</strong>; een rest is een veelterm "
                  r"en nooit een graad."),
            ("p", r"De graad van het quotiënt vind je door af te trekken: \(\deg Q=\deg A-\deg B\). Een "
                  r"veelterm van graad \(5\) gedeeld door een veelterm van graad \(2\) geeft dus een "
                  r"quotiënt van graad \(3\)."),
            ("p", r"Een voorbeeld met een deler van graad \(2\), waar Horner niet helpt: "
                  r"\(\left(x^{3}+1\right):\left(x^{2}+1\right)\). Je zoekt eerst waarmee je \(x^{2}\) tot "
                  r"\(x^{3}\) maakt, dat is \(x\); \(x\left(x^{2}+1\right)=x^{3}+x\), en wat overblijft is "
                  r"\(x^{3}+1-\left(x^{3}+x\right)=-x+1\). Die rest heeft graad \(1\), lager dan de deler, "
                  r"dus je stopt: quotiënt \(x\), rest \(-x+1\)."),
        ]),
        dict(kop="De reststelling", blokken=[
            ("p", r"<strong>De rest bij de deling van \(P(x)\) door \(x-a\) is \(P(a)\).</strong> Je hoeft "
                  r"dus niet te delen om de rest te kennen: <strong>invullen volstaat</strong>. Is "
                  r"\(P(a)=7\), dan is de rest \(7\)."),
            ("p", r"Voorbeeld: \(\left(x^{3}-2x^{2}+3x-4\right):(x-1)\). Vul \(1\) in: "
                  r"\(P(1)=1-2+3-4=-2\). Dat is de rest."),
            ("p", r"<strong>De reststelling werkt ook bij een deler \(x+a\)</strong>: je schrijft "
                  r"\(x+a=x-(-a)\) en vult \(-a\) in. Zo is de rest bij "
                  r"\(\left(2x^{3}-x+5\right):(x+2)\) gelijk aan \(P(-2)=-16+2+5=-9\)."),
            ("kader", r"Het gevolg dat je het vaakst gebruikt: <strong>is \(P(a)=0\), dan is \(x-a\) een "
                      r"deler van \(P\)</strong>. De rest is dan immers \(0\) en de deling gaat op. Neem "
                      r"\(P(x)=x^{3}-8\): \(P(2)=0\), dus \(x-2\) is een deler."),
            ("p", r"Omgekeerd gebruik je die stelling om een onbekende coëfficiënt te vinden. Voor welke "
                  r"\(m\) is \(x^{3}+mx^{2}-4x+6\) deelbaar door \(x-2\)? Deelbaar wil zeggen \(P(2)=0\), "
                  r"dus \(8+4m-8+6=0\) en \(m=-\tfrac{3}{2}\)."),
        ]),
        dict(kop="Het rekenschema van Horner", blokken=[
            ("p", r"Het <strong>rekenschema van Horner</strong> is een snelle schrijfwijze om <strong>te "
                  r"delen door een tweeterm \(x-a\)</strong>. Voor een deler van hogere graad, zoals "
                  r"\(x^{2}+1\), werkt het <strong>niet</strong>; daar val je terug op de gewone "
                  r"euclidische deling hierboven."),
            ("p", r"<strong>Bovenaan zet je alle coëfficiënten</strong>, van de hoogste graad tot en met de "
                  r"constante term. Voor een <strong>derdegraadsveelterm</strong> zijn dat er dus vier. Een "
                  r"ontbrekende graad schrijf je als \(0\); die mag je niet overslaan. Bij "
                  r"\(P(x)=x^{5}-2x^{3}+x\) staan bovenaan zes getallen: \(1,\,0,\,-2,\,0,\,1,\,0\)."),
            ("p", r"<strong>Links zet je \(a\)</strong>, en niet het getal uit de deler. Deel je door "
                  r"\(x+3\), dan is dat \(x-(-3)\), dus zet je \(-3\) links. Dat tekenfoutje is de "
                  r"klassieker van dit hoofdstuk."),
            ("p", r"Onderaan verschijnen de <strong>coëfficiënten van het quotiënt</strong>, en het "
                  r"<strong>laatste getal is de rest</strong>, en dus ook \(P(a)\). Zo geeft "
                  r"\(\left(x^{3}-6x^{2}+11x-6\right):(x-1)\) als quotiënt \(x^{2}-5x+6\) en rest \(0\); "
                  r"de volledige ontbinding is \((x-1)(x-2)(x-3)\)."),
        ]),
        dict(kop="Nulwaarden", blokken=[
            ("p", r"Een <strong>nulwaarde</strong> van een veeltermfunctie is een \(x\) waarvoor "
                  r"\(P(x)=0\). Op de grafiek zijn dat de snijpunten met de \(x\)-as. \(P(0)\) is iets "
                  r"anders: dat is het snijpunt met de \(y\)-as."),
            ("p", r"<strong>Een veelterm van graad \(n\) heeft hoogstens \(n\) reële nulwaarden</strong>, "
                  r"want elke nulwaarde levert een factor van graad \(1\) op. <strong>Elke veelterm van "
                  r"oneven graad heeft er minstens één</strong>: haar grafiek loopt van \(-\infty\) naar "
                  r"\(+\infty\) en moet de \(x\)-as dus kruisen."),
            ("p", r"Zoek je een <strong>gehele nulwaarde</strong> van een veelterm met gehele coëfficiënten, "
                  r"probeer dan de <strong>delers van de constante term</strong>: een gehele nulwaarde moet "
                  r"die term delen. Bij \(2x^{3}-3x^{2}-8x+12\) zijn dat de delers van \(12\), en \(x=2\) "
                  r"lukt meteen."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", r"<strong>Je ontbindt een veelterm in factoren om haar nulwaarden en haar delers te "
                  r"zien.</strong> Een product is \(0\) zodra één factor \(0\) is, dus elke factor van graad "
                  r"\(1\) levert meteen een nulwaarde op. <strong>Ontbinden is dus een manier om nulwaarden "
                  r"te vinden.</strong>"),
            ("p", tabel(["Merkwaardig product", "Ontbinding of uitwerking", "Let op"], [
                [r"\(a^{2}-b^{2}\)", r"\((a-b)(a+b)\)", "het verschil van twee kwadraten"],
                [r"\((a+b)^{2}\)", r"\(a^{2}+2ab+b^{2}\)", "de dubbele term vergeten is de vaakst gemaakte fout"],
                [r"\((a-b)^{2}\)", r"\(a^{2}-2ab+b^{2}\)", "alleen de middelste term wisselt van teken"],
                [r"\(a^{3}-b^{3}\)", r"\((a-b)\left(a^{2}+ab+b^{2}\right)\)", r"zo is \(x^{3}-8=(x-2)\left(x^{2}+2x+4\right)\)"],
            ])),
            ("p", r"De vier manieren die je nodig hebt, naast elkaar. <strong>De gemeenschappelijke factor "
                  r"afzonderen</strong>: \(3x^{3}-6x^{2}=3x^{2}(x-2)\). <strong>Termen samennemen</strong>: "
                  r"\(ax+ay+bx+by=a(x+y)+b(x+y)=(a+b)(x+y)\). <strong>Een merkwaardig product "
                  r"herkennen</strong>: \(x^{2}-9=(x-3)(x+3)\) en \(4x^{2}-12x+9=(2x-3)^{2}\). En "
                  r"<strong>een nulwaarde zoeken en met Horner delen</strong>: \(2x^{3}-3x^{2}-8x+12\) "
                  r"heeft \(P(2)=0\), Horner geeft \(2x^{2}+x-6\), en dus "
                  r"\(2x^{3}-3x^{2}-8x+12=(x-2)(x+2)(2x-3)\)."),
            ("p", r"Bij een tweedegraadsveelterm zoek je twee getallen met de juiste som en het juiste "
                  r"product: \(x^{2}-5x+6=(x-2)(x-3)\). De <strong>discriminant</strong> "
                  r"\(D=b^{2}-4ac\) zegt hoeveel reële nulwaarden er zijn: hier \(25-24=1>0\), dus twee. "
                  r"<strong>Bij \(D<0\) zijn er geen reële nulwaarden</strong>, en daarom valt "
                  r"\(x^{2}+4\) in \(\mathbb{R}\) niet uiteen in twee factoren van graad één; in "
                  r"\(\mathbb{C}\) lukt dat wel. <strong>Bij \(D=0\) is er één nulwaarde die dubbel "
                  r"telt</strong>: \(x^{2}+2x+1=(x+1)^{2}\) raakt de \(x\)-as in \(x=-1\)."),
            ("p", r"Twee verbanden die je zonder rekenen laten antwoorden: voor \(ax^{2}+bx+c\) is de "
                  r"<strong>som van de nulwaarden \(-\tfrac{b}{a}\)</strong> en het <strong>product "
                  r"\(\tfrac{c}{a}\)</strong>. Bij \(x^{2}-7x+12\) is de som dus \(7\) en het product "
                  r"\(12\); de nulwaarden zijn \(3\) en \(4\)."),
            ("weetje", r"\(x^{4}-16\) ontbind je zo ver mogelijk in \(\mathbb{R}\) tot "
                       r"\((x-2)(x+2)\left(x^{2}+4\right)\). Eerst het verschil van kwadraten, dan nog eens "
                       r"op \(x^{2}-4\). De laatste factor blijft staan, want die heeft geen reële "
                       r"nulwaarden."),
        ]),
    ],
    onthoud=[
        r"\(A=B\cdot Q+R\), en \(\deg R<\deg B\); gaat de deling op, dan is \(R=0\).",
        r"\(\deg Q=\deg A-\deg B\).",
        r"Reststelling: de rest bij \(P(x):(x-a)\) is \(P(a)\).",
        r"Is \(P(a)=0\), dan is \(x-a\) een deler van \(P\).",
        r"Horner werkt alleen bij \(x-a\); bij \(x+3\) zet je \(-3\) links.",
        r"Bovenaan in Horner staan alle coëfficiënten; een ontbrekende graad schrijf je als \(0\).",
        r"Een veelterm van graad \(n\) heeft hoogstens \(n\) reële nulwaarden; bij oneven graad minstens één.",
        r"Zoek een gehele nulwaarde bij de delers van de constante term.",
        r"\(a^{2}-b^{2}=(a-b)(a+b)\) en \(a^{3}-b^{3}=(a-b)\left(a^{2}+ab+b^{2}\right)\).",
        r"\(D>0\): twee nulwaarden. \(D=0\): één dubbele. \(D<0\): geen in \(\mathbb{R}\).",
        r"Som van de nulwaarden \(-\tfrac{b}{a}\), product \(\tfrac{c}{a}\).",
    ],
)

# ───────────────────────── 3. Vergelijkingen en ongelijkheden oplossen
BUNDELS["vergelijkingen-en-ongelijkheden-oplossen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vergelijkingen en ongelijkheden oplossen",
    onder="Algebraïsch en grafisch, met bestaansvoorwaarden, kwadrateringsvoorwaarden en tekenschema's.",
    secties=[
        dict(kop="Grafisch oplossen", blokken=[
            ("p", r"<strong>De oplossingen van \(f(x)=0\) zijn de snijpunten met de \(x\)-as.</strong> Dat "
                  r"zijn net de nulwaarden. Los je <strong>\(f(x)=g(x)\)</strong> grafisch op, dan lees je "
                  r"<strong>de \(x\)-waarden van de snijpunten</strong> af: op een snijpunt zijn beide "
                  r"functiewaarden gelijk, en de oplossing is de \(x\), niet de \(y\)."),
            ("p", r"Dat geldt ook met een grafische rekenapp: je noteert de \(x\)-waarden van de snijpunten. "
                  r"De oplossingenverzameling bestaat uit \(x\)-waarden; de \(y\)-waarde hoort bij het punt, "
                  r"niet bij de oplossing."),
            ("kader", r"<strong>Een vergelijking grafisch oplossen geeft niet altijd een exact "
                      r"antwoord.</strong> Meestal lees je een benadering af. Wil je exact werken, dan moet "
                      r"je algebraïsch oplossen."),
        ]),
        dict(kop="Bestaansvoorwaarden en kwadrateringsvoorwaarden", blokken=[
            ("p", r"Voor je begint te rekenen, schrijf je op wat \(x\) mág zijn. Bij \(\sqrt{x-3}\) is de "
                  r"bestaansvoorwaarde <strong>\(x\geq 3\)</strong>: wat onder een even wortel staat mag "
                  r"niet negatief zijn, en \(0\) mag wel. Bij \(\log(x-2)\) is ze "
                  r"<strong>\(x>2\)</strong>: het argument van een logaritme moet strikt positief zijn, "
                  r"dus \(0\) mag hier niet."),
            ("p", r"<strong>Kwadrateren is geen gelijkwaardige bewerking.</strong> \(-2\) en \(2\) hebben "
                  r"hetzelfde kwadraat, dus je kan er oplossingen bij krijgen die niet aan de "
                  r"oorspronkelijke vergelijking voldoen. Daarom moet je na het kwadrateren van een "
                  r"irrationale vergelijking <strong>elke gevonden oplossing in de oorspronkelijke "
                  r"vergelijking controleren</strong>."),
            ("p", r"Voorbeeld: \(\sqrt{x+1}=x-1\). Kwadrateren geeft \(x+1=x^{2}-2x+1\), dus "
                  r"\(x^{2}-3x=0\) en \(x=0\) of \(x=3\). <strong>De enige oplossing is \(x=3\).</strong> "
                  r"Vul \(x=0\) in en links staat \(\sqrt{1}=1\), terwijl rechts \(-1\) staat: een valse "
                  r"oplossing die bij het kwadrateren ontstond."),
        ]),
        dict(kop="Vergelijkingen van elk soort", blokken=[
            ("p", tabel(["Vergelijking", "Hoe je ze aanpakt", "Oplossing"], [
                [r"\(5x-20=0\)", "overbrengen en delen", r"\(x=4\)"],
                [r"\(x^{2}=9\)", "de wortel nemen, allebei de tekens", r"\(x=3\) en \(x=-3\)"],
                [r"\(|x-1|=3\)", "splitsen in twee gevallen", r"\(x=4\) en \(x=-2\)"],
                [r"\(2^{x}=8\)", r"\(8\) schrijven als \(2^{3}\)", r"\(x=3\)"],
                [r"\(3^{2x}=3^{x+4}\)", "de exponenten gelijkstellen", r"\(x=4\)"],
                [r"\(\log_{2}(x+3)=\log_{2}(2x-1)\)", "de argumenten gelijkstellen, dan het domein nakijken", r"\(x=4\)"],
                [r"\(\sin x=0\)", "de functie is periodiek", "oneindig veel oplossingen"],
            ])),
            ("p", r"De <strong>discriminant \(D=b^{2}-4ac\)</strong> vertelt hoeveel reële oplossingen een "
                  r"tweedegraadsvergelijking heeft: \(D>0\) geeft er twee, \(D=0\) één, \(D<0\) geen "
                  r"enkele. Bij \(x^{2}+2x+1\) is \(D=4-4=0\), dus precies één oplossing, \(x=-1\). Het "
                  r"teken van \(a\) bepaalt alleen de opening van de parabool."),
            ("p", r"Omgekeerd bepaalt die discriminant een onbekende coëfficiënt. Voor welke \(m\) heeft "
                  r"\(x^{2}-4x+m=0\) precies één oplossing? Uit \(D=16-4m=0\) volgt \(m=4\), en de "
                  r"vergelijking wordt \((x-2)^{2}=0\)."),
            ("p", r"<strong>Is \(\log x=\log y\) en bestaan ze allebei, dan is \(x=y\)</strong>: de "
                  r"logaritmische functie is strikt stijgend, dus elke waarde hoort bij precies één "
                  r"argument."),
            ("weetje", r"<strong>Niet elke vergelijking \(f(x)=0\) heeft een reële oplossing.</strong> Neem "
                       r"\(f(x)=x^{2}+1\): die functie wordt nooit \(0\), want haar grafiek blijft volledig "
                       r"boven de \(x\)-as."),
            ("kader", r"<strong>Deel nooit beide leden door een uitdrukking met \(x\) in.</strong> Die "
                      r"uitdrukking kan \(0\) zijn, en dan gooi je net die oplossing weg. Breng alles naar "
                      r"één lid en ontbind in factoren."),
        ]),
        dict(kop="Ongelijkheden lezen van de grafiek", blokken=[
            ("p", r"<strong>\(f(x)>0\) betekent dat de grafiek boven de \(x\)-as ligt.</strong> Het teken "
                  r"van de functiewaarde is de hoogte ten opzichte van de \(x\)-as; stijgen is iets anders, "
                  r"dat gaat over de richting. En <strong>\(f(x)<g(x)\) betekent dat de grafiek van \(f\) "
                  r"onder die van \(g\) ligt</strong>, met de snijpunten als grenzen. Bij \(f(x)\geq g(x)\) "
                  r"horen de snijpunten erbij, want daar zijn de twee functiewaarden gelijk."),
            ("p", r"<strong>Ongelijkheden los je grafisch op.</strong> Alleen de tweedegraadsongelijkheid "
                  r"moet je ook algebraïsch aankunnen; een ongelijkheid van de vijfde graad hoef je niet "
                  r"met de hand te ontbinden."),
        ]),
        dict(kop="Tekenschema en oplossingenverzameling", blokken=[
            ("p", r"<strong>De eerste stap bij een tweedegraadsongelijkheid is alles naar één lid brengen "
                  r"zodat er \(0\) overblijft.</strong> Pas dan kan je nulwaarden zoeken en een tekenschema "
                  r"maken. In het tekenschema van \(x^{2}-9\) zet je twee nulwaarden, \(-3\) en \(3\); die "
                  r"verdelen de getallenas in drie stukken."),
            ("p", r"Daarna gebruik je de vorm van de parabool. Bij <strong>\(a>0\) met twee nulwaarden is "
                  r"de functie negatief tussen de nulwaarden in</strong>; bij <strong>\(a<0\) met twee "
                  r"nulwaarden is ze net dáár positief</strong>."),
            ("p", tabel(["Ongelijkheid", "Oplossing", "Waarom"], [
                [r"\(2x-6>0\)", r"\(x>3\)", "je deelt door een positief getal, het teken blijft"],
                [r"\(3x+9<0\)", r"\(x<-3\)", "overbrengen en door drie delen"],
                [r"\(x^{2}-4\leq 0\)", r"\(\left[-2,2\right]\)", "tussen de nulwaarden duikt de dalparabool onder de as"],
                [r"\(x^{2}-5x+6>0\)", r"\(x<2\) of \(x>3\)", "buiten de nulwaarden ligt de dalparabool boven de as"],
                [r"\((x-1)(x+2)<0\)", r"\(-2<x<1\)", "een product is negatief bij een verschillend teken"],
                [r"\(x^{2}\geq 9\)", r"\(x\leq -3\) of \(x\geq 3\)", r"buiten de nulwaarden \(-3\) en \(3\)"],
                [r"\(\dfrac{x-1}{x+2}\geq 0\)", r"\(x<-2\) of \(x\geq 1\)", r"teller en noemer hetzelfde teken; in \(-2\) bestaat de breuk niet"],
            ])),
            ("p", r"Let op die laatste: bij een <strong>breuk</strong> maak je een tekenschema van teller en "
                  r"noemer apart. De nulwaarde van de teller mag erbij staan wanneer het teken \(\geq\) is, "
                  r"maar de nulwaarde van de noemer <strong>nooit</strong>, want daar bestaat de breuk niet."),
            ("p", r"<strong>\(x^{2}+1>0\) geldt voor elke \(x\in\mathbb{R}\)</strong>: een kwadraat is nooit "
                  r"negatief, dus de som met \(1\) is altijd minstens \(1\). Omgekeerd heeft \(x^{2}<0\) "
                  r"geen enkele reële oplossing."),
            ("p", r"Het resultaat noteer je als <strong>interval</strong>. Grenzen inbegrepen geeft "
                  r"\(\left[-2,2\right]\), grenzen uitgesloten \(\left]-2,2\right[\). Een ongelijkheid heeft "
                  r"meestal een heel interval als oplossing, dus oneindig veel getallen, en niet hoogstens "
                  r"twee losse oplossingen."),
            ("kader", r"Twee valkuilen die bij elkaar horen. <strong>Deel je beide leden door een negatief "
                      r"getal, dan draait het ongelijkheidsteken om</strong>: \(2<4\), maar \(-2>-4\). En "
                      r"<strong>vermenigvuldig een ongelijkheid nooit zomaar met \(x\)</strong>, want het "
                      r"teken van \(x\) is niet gekend: is \(x<0\), dan moet het teken omdraaien, en is "
                      r"\(x=0\), dan klopt er niets meer."),
        ]),
    ],
    onthoud=[
        r"Bij \(f(x)=g(x)\) is de oplossing de \(x\) van het snijpunt, niet de \(y\).",
        r"Onder een even wortel mag niets negatiefs staan; het argument van een logaritme moet \(>0\) zijn.",
        r"Na het kwadrateren controleer je elke oplossing in de oorspronkelijke vergelijking.",
        r"\(D>0\): twee oplossingen. \(D=0\): één. \(D<0\): geen.",
        r"Deel nooit beide leden door een uitdrukking met \(x\) in.",
        r"\(f(x)>0\) betekent dat de grafiek boven de \(x\)-as ligt.",
        r"Breng bij een tweedegraadsongelijkheid eerst alles naar één lid zodat er \(0\) overblijft.",
        r"Bij \(a>0\) is de functie negatief tussen de twee nulwaarden in.",
        r"Deel je door een negatief getal, dan draait het ongelijkheidsteken om.",
        r"Bij een breuk hoort de nulwaarde van de noemer nooit bij de oplossing.",
    ],
)

# ───────────────────────── 4. Een functie aflezen van haar grafiek
BUNDELS["een-functie-aflezen-van-haar-grafiek-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een functie aflezen van haar grafiek",
    onder="Domein, bereik, symmetrie, verloop en asymptoten, en wat een inverse functie is.",
    secties=[
        dict(kop="Domein, bereik en voorstellingswijzen", blokken=[
            ("p", r"<strong>\(\text{dom}\,f\) zijn alle \(x\) waarvoor \(f(x)\) bestaat.</strong> Het "
                  r"domein ligt op de \(x\)-as. <strong>\(\text{ber}\,f\) is de verzameling van alle "
                  r"waarden \(f(x)\) die ze aanneemt</strong>, en dat lees je af op de \(y\)-as. Bij "
                  r"\(f(x)=\dfrac{1}{x-5}\) hoort \(5\) niet bij het domein, want dan wordt de noemer "
                  r"\(0\)."),
            ("p", r"Het <strong>praktisch domein</strong> is het stuk van het domein dat zinvol is in de "
                  r"context. Bij een model voor de hoogte van een plant is een negatieve tijd "
                  r"betekenisloos, ook al hoort ze bij het wiskundige domein."),
            ("p", r"Een functie kan je op <strong>vier manieren voorstellen</strong>: met een "
                  r"<strong>verwoording</strong>, met een <strong>tabel</strong>, met een "
                  r"<strong>grafiek</strong> en met een <strong>voorschrift</strong>. Je moet van elke "
                  r"voorstellingswijze naar elke andere kunnen overstappen."),
            ("kader", r"<strong>Een verticale rechte mag de grafiek van een functie hoogstens één keer "
                      r"snijden.</strong> Bij twee snijpunten zouden er voor dezelfde \(x\) twee waarden "
                      r"\(f(x)\) zijn, en dan is het geen functie meer."),
        ]),
        dict(kop="Nulwaarden, tekenverloop en symmetrie", blokken=[
            ("p", r"Een <strong>nulwaarde is een getal</strong>, een <strong>nulpunt is een punt</strong>. "
                  r"De nulwaarde is de \(x\) waarvoor \(f(x)=0\); het nulpunt is \((x,0)\). Snijdt een "
                  r"grafiek de \(x\)-as in drie punten, dan heeft de functie drie nulwaarden."),
            ("p", r"In een <strong>tekenverloop</strong> lees je af waar \(f(x)>0\) en waar \(f(x)<0\), dus "
                  r"boven of onder de \(x\)-as. Stijgen en dalen is iets anders: dat is het verloop, en dat "
                  r"lees je af uit \(f'\)."),
            ("p", tabel(["Soort symmetrie", "Wat geldt", "Hoe de grafiek ligt", "Voorbeeld"], [
                ["even functie", r"\(f(-x)=f(x)\)", r"symmetrisch om de \(y\)-as", r"\(f(x)=x^{2}\)"],
                ["oneven functie", r"\(f(-x)=-f(x)\)", "symmetrisch om de oorsprong", r"\(f(x)=x^{3}\)"],
            ])),
            ("kader", r"Verwissel die twee niet. <strong>Een grafiek die symmetrisch is om de oorsprong "
                      r"hoort bij een oneven functie</strong>, niet bij een even functie. Bij een oneven "
                      r"functie legt een halve draai om de oorsprong de grafiek op zichzelf."),
        ]),
        dict(kop="Het verloop lezen", blokken=[
            ("p", r"<strong>Een toenemende stijging betekent dat de grafiek stijgt en daarbij almaar "
                  r"steiler wordt.</strong> Bij een afnemende stijging gaat ze wel nog omhoog, maar met een "
                  r"kleinere helling. Blijft de helling gelijk, dan spreek je van lineaire groei."),
            ("p", r"<strong>Een buigpunt is het punt waar hol in bol overgaat.</strong> Het gaat dus over "
                  r"de kromming, niet over de richting. Waar stijgen in dalen overgaat, ligt een maximum."),
            ("p", r"<strong>In een maximum bereikt de functie niet altijd haar grootste waarde op het hele "
                  r"domein.</strong> Dat geldt alleen voor een <strong>absoluut maximum</strong>. Een "
                  r"<strong>plaatselijk maximum</strong> is enkel de hoogste waarde in zijn eigen omgeving; "
                  r"verderop kan de grafiek nog hoger gaan."),
            ("p", r"Bij een golvende grafiek horen nog twee woorden. De <strong>amplitude</strong> is de "
                  r"afstand van de evenwichtslijn tot de top: schommelt een sinusgrafiek tussen \(-3\) en "
                  r"\(3\) rond de \(x\)-as, dan is de amplitude \(\tfrac{3-(-3)}{2}=3\). De "
                  r"<strong>periode</strong> is de kleinste \(p>0\) waarvoor \(f(x+p)=f(x)\) voor elke "
                  r"\(x\): herhaalt een grafiek zich om de vier eenheden, dan is de periode \(4\)."),
        ]),
        dict(kop="Gedrag op oneindig en asymptoten", blokken=[
            ("p", r"<strong>Het gedrag van \(f\) op oneindig is wat er met \(f(x)\) gebeurt als "
                  r"\(x\to+\infty\) of \(x\to-\infty\).</strong> Oneindig is geen getal, dus de functie "
                  r"heeft daar geen waarde; je kijkt naar waar de waarden naartoe kruipen."),
            ("p", r"<strong>Een horizontale asymptoot betekent dat de grafiek op oneindig een vaste hoogte "
                  r"nadert.</strong> Bij een rationale functie wegen voor grote \(|x|\) alleen de hoogste "
                  r"graden mee: \(f(x)=\dfrac{2x+1}{x-3}\) heeft dus \(y=2\) als horizontale asymptoot. Een "
                  r"<strong>verticale asymptoot</strong> ligt waar de noemer \(0\) wordt en de teller niet, "
                  r"hier dus bij \(x=3\)."),
            ("p", r"<strong>Niet elke functie heeft een asymptoot</strong>: een parabool of een rechte "
                  r"heeft er geen enkele. Asymptoten horen vooral bij rationale, exponentiële en "
                  r"logaritmische functies."),
        ]),
        dict(kop="De inverse functie", blokken=[
            ("p", r"De <strong>inverse functie \(f^{-1}\)</strong> maakt ongedaan wat \(f\) doet. Je vindt "
                  r"haar voorschrift door <strong>\(x\) en \(y\) te verwisselen en dan naar \(y\) op te "
                  r"lossen</strong>. Voor \(f(x)=\dfrac{2x-1}{3}\) geeft \(x=\dfrac{2y-1}{3}\) dat "
                  r"\(3x+1=2y\), dus \(f^{-1}(x)=\dfrac{3x+1}{2}\). Let op: <strong>\(f^{-1}\) is niet "
                  r"\(\dfrac{1}{f}\)</strong>, ook al lijkt de notatie erop."),
            ("p", r"<strong>De grafieken van \(f\) en \(f^{-1}\) zijn elkaars spiegelbeeld om de eerste "
                  r"bissectrice</strong>, de rechte \(y=x\). Die deelt het eerste en het derde kwadrant "
                  r"doormidden; \(y=-x\) is de tweede bissectrice. Spiegelen werkt alleen netjes in een "
                  r"orthonormaal assenstelsel. Daarbij wisselen de coördinaten van plaats: \((0,2)\) wordt "
                  r"\((2,0)\). Daarom geldt ook <strong>\(\text{dom}\,f^{-1}=\text{ber}\,f\)</strong>."),
            ("p", r"<strong>Een functie is niet inverteerbaar als een horizontale rechte haar grafiek meer "
                  r"dan één keer snijdt</strong>; bij een inverteerbare functie mag dat hoogstens één keer. "
                  r"Anders hoort dezelfde waarde bij meerdere \(x\)-waarden en weet \(f^{-1}\) niet welke "
                  r"ze moet teruggeven. Daarom is \(f(x)=x^{2}\) niet inverteerbaar op heel "
                  r"\(\mathbb{R}\): \(2\) en \(-2\) hebben hetzelfde kwadraat. Beperk je het domein tot "
                  r"\(\left[0,+\infty\right[\), dan is ze strikt stijgend en is \(f^{-1}(x)=\sqrt{x}\). "
                  r"<strong>Ook niet elke rechte is inverteerbaar</strong>: \(y=c\) wordt na spiegeling een "
                  r"verticale rechte, en dat is geen functie."),
            ("p", tabel(["Functie", "Haar inverse", "Waarom"], [
                [r"\(f(x)=a^{x}\)", r"\(f^{-1}(x)=\log_{a}x\)", "de logaritme geeft net de exponent terug"],
                [r"\(f(x)=x^{2}\) op \(\left[0,+\infty\right[\)", r"\(f^{-1}(x)=\sqrt{x}\)", "kwadrateren en worteltrekken heffen elkaar daar op"],
                [r"\(f(x)=x+3\)", r"\(f^{-1}(x)=x-3\)", "wat de functie erbij doet, haalt de inverse er weer af"],
                [r"\(f(x)=2x\)", r"\(f^{-1}(x)=\tfrac{x}{2}\)", r"de functie verdubbelt, dus \(f^{-1}(10)=5\)"],
            ])),
            ("p", r"<strong>\(\arcsin\) is de inverse van \(\sin\) op een beperkt domein</strong>, meestal "
                  r"\(\left[-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]\). Men beperkt het domein omdat de sinus "
                  r"anders dezelfde waarde oneindig vaak aanneemt: zonder beperking zou \(\arcsin\) bij één "
                  r"getal oneindig veel hoeken moeten teruggeven. \(\arcsin\), \(\arccos\) en \(\arctan\) "
                  r"heten samen de <strong>cyclometrische functies</strong>."),
            ("weetje", r"Twee gevolgen die je meteen mag gebruiken. <strong>De inverse van een strikt "
                       r"stijgende functie is zelf ook strikt stijgend</strong>, want spiegelen draait de "
                       r"volgorde van de punten niet om. En ligt een grafiek symmetrisch om \(y=x\), dan is "
                       r"<strong>de functie haar eigen inverse</strong>: \(f(x)=\tfrac{1}{x}\) is zo een "
                       r"functie."),
        ]),
    ],
    onthoud=[
        r"\(\text{dom}\,f\) zijn alle \(x\) waarvoor \(f(x)\) bestaat, \(\text{ber}\,f\) alle waarden die ze aanneemt.",
        r"Een verticale rechte mag de grafiek van een functie hoogstens één keer snijden.",
        r"Een nulwaarde is een getal, een nulpunt is het punt \((x,0)\).",
        r"Even: \(f(-x)=f(x)\), symmetrisch om de \(y\)-as. Oneven: \(f(-x)=-f(x)\), om de oorsprong.",
        r"Een buigpunt is het punt waar hol in bol overgaat.",
        r"Een plaatselijk maximum is enkel de hoogste waarde in zijn eigen omgeving.",
        r"Bij een rationale functie geven de hoogste graden de horizontale asymptoot.",
        r"\(f^{-1}\) vind je door \(x\) en \(y\) te verwisselen en naar \(y\) op te lossen; \(f^{-1}\neq\tfrac{1}{f}\).",
        r"\(f\) en \(f^{-1}\) zijn elkaars spiegelbeeld om \(y=x\), en \(\text{dom}\,f^{-1}=\text{ber}\,f\).",
    ],
)

# ───────────────────────── 5. Tweedegraadsfuncties en transformaties
BUNDELS["tweedegraadsfuncties-en-transformaties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tweedegraadsfuncties en transformaties",
    onder="De parabool met haar top, nulwaarden en symmetrieas, en de vier transformaties van een grafiek.",
    secties=[
        dict(kop="De parabool", blokken=[
            ("p", r"<strong>De grafiek van een tweedegraadsfunctie \(f(x)=ax^{2}+bx+c\) heet een "
                  r"parabool.</strong> Die van \(f(x)=\tfrac{1}{x}\) heet een hyperbool, die van een "
                  r"eerstegraadsfunctie een rechte."),
            ("p", r"<strong>Alleen het teken van \(a\) bepaalt de opening.</strong> Is \(a>0\), dan is het "
                  r"een <strong>dalparabool</strong> met een minimum. Is \(a<0\), dan krijg je een "
                  r"<strong>bergparabool</strong>, en die heeft geen minimum maar een maximum. "
                  r"<strong>Hoe groter \(|a|\), hoe smaller de parabool</strong>: een grote \(|a|\) rekt de "
                  r"grafiek verticaal uit."),
            ("p", r"<strong>De symmetrieas gaat altijd door de top.</strong> Ze is de verticale rechte door "
                  r"de top, dus haar vergelijking is van de vorm \(x=\) een getal: bij een top \((2,7)\) is "
                  r"dat \(x=2\)."),
            ("p", r"Om één parabool vast te leggen heb je minstens <strong>drie punten</strong> nodig, want "
                  r"er zijn drie onbekende coëfficiënten \(a\), \(b\) en \(c\)."),
        ]),
        dict(kop="Top, nulwaarden en discriminant", blokken=[
            ("p", r"De \(x\) van de top is <strong>\(x=\dfrac{-b}{2a}\)</strong>. De discriminant is "
                  r"<strong>\(D=b^{2}-4ac\)</strong>, en haar teken beslist over het aantal reële "
                  r"nulwaarden: \(D>0\) geeft er twee, \(D=0\) geeft er één (de parabool raakt de \(x\)-as "
                  r"dan precies in haar top), en bij \(D<0\) zijn er nul, want de parabool ligt dan "
                  r"volledig boven of volledig onder de as."),
            ("p", r"<strong>Heeft een parabool twee nulwaarden, dan ligt de \(x\) van de top precies in het "
                  r"midden ertussen.</strong> Het gemiddelde van de nulwaarden geeft dus de top."),
            ("p", tabel([r"Vraag over \(f(x)=x^{2}-6x+5\)", "Antwoord", "Hoe"], [
                [r"de \(x\) van de top", r"\(3\)", r"\(\dfrac{-b}{2a}=\dfrac{6}{2}\)"],
                [r"de \(y\) van de top", r"\(-4\)", r"\(f(3)=9-18+5\)"],
                ["de nulwaarden", r"\(1\) en \(5\)", r"\((x-1)(x-5)\): som \(6\), product \(5\)"],
                [r"het snijpunt met de \(y\)-as", r"\(y=5\)", r"\(f(0)=c\)"],
            ])),
            ("p", r"Nog een voorbeeld: de top van \(f(x)=-x^{2}+4x\) is \((2,4)\), want "
                  r"\(\dfrac{-4}{-2}=2\) en \(f(2)=-4+8=4\)."),
            ("p", r"Een dalparabool met top \((3,-4)\) heeft als bereik \(\left[-4,+\infty\right[\): de top "
                  r"is het laagste punt. En een parabool kan de \(y\)-as niet twee keer snijden, want voor "
                  r"\(x=0\) is er maar één functiewaarde, namelijk \(c\)."),
            ("p", r"Omgekeerd legt de discriminant een onbekende coëfficiënt vast. Voor welke \(m\) raakt "
                  r"\(y=x^{2}-6x+m\) de \(x\)-as? Raken wil zeggen \(D=0\), dus \(36-4m=0\) en \(m=9\); "
                  r"het voorschrift wordt \((x-3)^{2}\)."),
            ("weetje", r"Bij de hoogte van een <strong>opgegooide bal</strong>, die een bergparabool volgt, "
                       r"is de top het hoogste punt van de baan. De landing is de tweede nulwaarde en de "
                       r"beginhoogte lees je af op de \(y\)-as."),
        ]),
        dict(kop="De topvorm", blokken=[
            ("p", r"Staat een voorschrift in de vorm <strong>\(f(x)=a(x-p)^{2}+q\)</strong>, dan lees je de "
                  r"top meteen af: \((p,q)\). Dat heet de <strong>topvorm</strong>. Let op het minteken in "
                  r"de haakjes: \((x-3)^{2}\) geeft een top in \(x=3\), niet in \(x=-3\)."),
            ("p", r"Zo heeft \((x-4)^{2}+1\) haar top in \(x=4\), en is bij \((x-2)^{2}+7\) de kleinste "
                  r"functiewaarde \(7\), want een kwadraat is minstens \(0\). Bij \(2(x-1)^{2}+3\) is de "
                  r"\(y\) van de top \(3\): de factor \(2\) verandert de breedte, niet de ligging van de "
                  r"top."),
            ("p", r"Omgekeerd kan je uit de topvorm een voorschrift opbouwen. Een parabool met top "
                  r"\((4,2)\) die door \((5,5)\) gaat, heeft als voorschrift \(y=3(x-4)^{2}+2\): vul het "
                  r"extra punt in, dan is \(a\cdot 1+2=5\)."),
        ]),
        dict(kop="De vier transformaties", blokken=[
            ("p", tabel(["Schrijfwijze", "Wat de grafiek doet", "Geheugensteun"], [
                [r"\(f(x)+3\)", r"\(3\) omhoog", "buiten de haakjes werkt verticaal"],
                [r"\(f(x)-5\)", r"\(5\) omlaag", "de hele grafiek zakt, ook de top"],
                [r"\(f(x-2)\)", r"\(2\) naar rechts", "binnen de haakjes werkt omgekeerd"],
                [r"\(f(x+3)\)", r"\(3\) naar links", "ook hier omgekeerd dan het voelt"],
                [r"\(-f(x)\)", r"spiegeling om de \(x\)-as", "elke functiewaarde wisselt van teken"],
                [r"\(f(-x)\)", r"spiegeling om de \(y\)-as", r"je vult \(-x\) in in plaats van \(x\)"],
                [r"\(3f(x)\)", r"verticale uitrekking met factor \(3\)", "de grafiek wordt driemaal zo hoog"],
            ])),
            ("p", r"<strong>\(2x^{2}\) is dus smaller dan \(x^{2}\)</strong>, niet breder: elke "
                  r"functiewaarde verdubbelt, dus de parabool loopt sneller omhoog."),
            ("p", r"Twee voorbeelden met meerdere stappen. Van \(x^{2}\) naar \((x+1)^{2}-3\) ga je met "
                  r"<strong>\(1\) naar links en \(3\) omlaag</strong>; de top komt op \((-1,-3)\). Van "
                  r"\(x^{2}\) naar \(2(x-1)^{2}+3\) ga je met <strong>\(1\) naar rechts, verticaal "
                  r"uitrekken met \(2\), en \(3\) omhoog</strong>."),
            ("p", r"<strong>Spiegel je een dalparabool om de \(x\)-as, dan krijg je een bergparabool met een "
                  r"maximum</strong>: het teken van \(a\) draait om."),
        ]),
        dict(kop="Wat een transformatie wel en niet verandert", blokken=[
            ("p", r"<strong>Een verticale uitrekking laat de nulwaarden onveranderd</strong>, want "
                  r"\(3\cdot 0=0\). Elke verschuiving verplaatst de nulwaarden wel."),
            ("p", r"<strong>Een verticale verschuiving verandert het bereik</strong>, want alle "
                  r"functiewaarden schuiven mee op, maar ze <strong>laat de symmetrieas op haar "
                  r"plaats</strong>: de \(x\) van de top blijft dezelfde. Ze kan wel het tekenverloop "
                  r"veranderen, want de nulwaarden verschuiven: een dalparabool die net onder de as lag, "
                  r"kan er na \(2\) omhoog helemaal boven komen, en dan zijn de nulwaarden weg."),
            ("p", r"<strong>Een horizontale verschuiving verandert het domein van een tweedegraadsfunctie "
                  r"niet</strong>: dat is en blijft \(\mathbb{R}\). Bij een wortelfunctie zou het wel "
                  r"veranderen."),
            ("weetje", r"<strong>De linkertak van een gewone dalparabool daalt, met een afnemende "
                       r"daling</strong>: ze gaat omlaag, maar steeds minder steil, tot ze in de top even "
                       r"vlak loopt."),
        ]),
    ],
    onthoud=[
        r"De grafiek van \(f(x)=ax^{2}+bx+c\) heet een parabool.",
        r"\(a>0\): dalparabool. \(a<0\): bergparabool. Hoe groter \(|a|\), hoe smaller.",
        r"De \(x\) van de top is \(\dfrac{-b}{2a}\); de symmetrieas gaat door de top.",
        r"\(D=b^{2}-4ac\), en \(D=0\) betekent dat de parabool de \(x\)-as raakt.",
        r"In de topvorm \(a(x-p)^{2}+q\) is de top \((p,q)\).",
        r"Buiten de haakjes werkt verticaal, binnen de haakjes werkt omgekeerd.",
        r"\(-f(x)\) spiegelt om de \(x\)-as, \(f(-x)\) om de \(y\)-as.",
        r"Een verticale uitrekking laat de nulwaarden onveranderd.",
        r"Een verticale verschuiving verandert het bereik, maar laat de symmetrieas staan.",
    ],
)

# ───────────────────────── 6. Exponentiële en logaritmische functies
BUNDELS["exponentiele-en-logaritmische-functies-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Exponentiële en logaritmische functies",
    onder="De twee grafieken en hun asymptoten, en groeimodellen met groeifactor, verdubbelings- en halveringstijd.",
    secties=[
        dict(kop="De exponentiële functie", blokken=[
            ("p", r"Neem \(f(x)=a^{x}\) met \(a>0\). Dan is <strong>\(\text{dom}\,f=\mathbb{R}\)</strong>: je mag "
                  r"elke exponent nemen, ook negatieve en gebroken. Het bereik is wel beperkt, want "
                  r"<strong>\(\text{ber}\,f=\left]0,+\infty\right[\)</strong>: een macht van een positief grondtal "
                  r"wordt nooit \(0\) of negatief. <strong>Zonder transformatie kan zo'n functie dus geen negatieve "
                  r"waarden aannemen.</strong>"),
            ("p", r"Elke grafiek van \(a^{x}\) gaat door <strong>\((0,1)\)</strong>, want \(a^{0}=1\) bij elk "
                  r"grondtal, en door <strong>\((1,a)\)</strong>, want \(a^{1}=a\). Dat tweede punt is handig: "
                  r"<strong>in \(x=1\) lees je het grondtal rechtstreeks af</strong>. Gaat de grafiek door "
                  r"\((1,5)\), dan is \(a=5\). Zo is ook \(f(2)=3^{2}=9\) voor \(f(x)=3^{x}\)."),
            ("p", r"<strong>Is \(a>1\), dan stijgt de functie</strong>; dat geldt dus ook voor grondtal \(e\), "
                  r"want \(e\approx 2{,}718\). <strong>Is \(0<a<1\), dan daalt ze</strong>: "
                  r"\(\left(\tfrac{1}{2}\right)^{3}=\tfrac{1}{8}\), dus hoe groter de exponent, hoe kleiner de "
                  r"uitkomst. <strong>\(a=1\) is niet toegelaten, omdat de grafiek dan de horizontale rechte "
                  r"\(y=1\) wordt</strong>: \(1^{x}=1\) voor elke \(x\), en een constante functie groeit niet."),
            ("p", r"<strong>\(f(x)=2^{x}\) heeft de rechte \(y=0\) als horizontale asymptoot</strong>, want voor "
                  r"\(x\to-\infty\) kruipen de waarden naar \(0\). <strong>De grafiek snijdt haar asymptoot "
                  r"nooit</strong>; ze nadert die alleen oneindig dicht. Schuif je de grafiek op, dan schuift de "
                  r"asymptoot mee: <strong>\(2^{x}+5\) heeft de rechte \(y=5\)</strong>, en <strong>\(2^{x}-4\) is "
                  r"\(4\) omlaag geschoven</strong>, met asymptoot \(y=-4\). De \(-4\) staat buiten de macht, dus "
                  r"hij werkt op de functiewaarde. <strong>Spiegel je \(2^{x}\) om de \(x\)-as, dan wordt het "
                  r"bereik \(\left]-\infty,0\right[\)</strong>, want alle functiewaarden wisselen van teken."),
        ]),
        dict(kop="De logaritmische functie", blokken=[
            ("p", r"Voor \(f(x)=\log_{a}x\) is <strong>\(\text{dom}\,f=\left]0,+\infty\right[\)</strong>: alleen "
                  r"strikt positieve argumenten hebben een logaritme, dus het domein bestaat uit alle getallen "
                  r"strikt groter dan \(0\). Daarom heeft ze <strong>een verticale asymptoot</strong>: voor "
                  r"\(x\to 0^{+}\) duikt de logaritme naar \(-\infty\), dus de \(y\)-as is die asymptoot."),
            ("p", r"<strong>Haar grafiek gaat altijd door \((1,0)\)</strong>, want \(\log_{a}1=0\) bij elk "
                  r"grondtal. Dat is net het spiegelbeeld van het punt \((0,1)\) van de exponentiële functie."),
            ("p", r"<strong>\(a^{x}\) en \(\log_{a}x\) met hetzelfde grondtal spiegelen om de rechte "
                  r"\(y=x\).</strong> Het zijn elkaars inverse functies, en inverse functies spiegelen altijd om "
                  r"de eerste bissectrice."),
        ]),
        dict(kop="Groeifactor en procenten", blokken=[
            ("p", r"Een <strong>groeifactor</strong> is het getal waarmee je per tijdseenheid vermenigvuldigt. "
                  r"<strong>Hij is nooit negatief.</strong> Bij een toename van \(p\%\) is hij "
                  r"<strong>\(1+\tfrac{p}{100}\)</strong>; bij een afname blijft er \(p\%\) over."),
            ("p", tabel(["Situatie", "Groeifactor", "Hoe je eraan komt"], [
                [r"\(3\%\) groei per jaar", r"\(1{,}03\)", r"\(1+\dfrac{3}{100}\)"],
                [r"\(20\%\) daling per jaar", r"\(0{,}8\)", r"er blijft \(80\%\) over"],
                [r"\(5\%\) samengestelde intrest", r"\(1{,}05\)", r"elk jaar dezelfde factor"],
                [r"van \(100\) naar \(150\)", r"\(1{,}5\)", r"\(\dfrac{150}{100}\)"],
                [r"groeifactor \(1{,}12\)", r"\(12\%\) erbij", r"\(1{,}12-1=0{,}12\)"],
            ])),
            ("p", r"<strong>Een groeifactor kleiner dan \(1\) betekent dat de hoeveelheid afneemt.</strong> Bij "
                  r"precies \(1\) blijft alles gelijk."),
            ("p", r"Groeifactoren combineer je door te <strong>vermenigvuldigen</strong>, nooit door op te tellen. "
                  r"<strong>Ken je de factor \(g\) per maand, dan is de factor per jaar \(g^{12}\)</strong>, en "
                  r"<strong>is de jaarfactor \(2\), dan is de factor per twee jaar \(2^{2}=4\)</strong>. Daaruit "
                  r"volgt ook een bekende valstrik: <strong>een stijging met \(10\%\) gevolgd door een daling met "
                  r"\(10\%\) brengt je niet terug bij de beginwaarde</strong>, want \(1{,}1\cdot 0{,}9=0{,}99\), "
                  r"dus je verliest \(1\%\)."),
        ]),
        dict(kop="Groeimodellen", blokken=[
            ("p", r"In het model <strong>\(N(x)=b\cdot a^{x}\)</strong> is <strong>\(b\) de beginwaarde</strong>: "
                  r"bij \(N(x)=200\cdot 1{,}05^{x}\) is \(N(0)=200\cdot 1=200\), want voor \(x=0\) is de macht "
                  r"\(1\)."),
            ("p", tabel(["Soort groei", "Vorm", "Waaraan je ze herkent"], [
                [r"lineaire groei", r"\(f(x)=ax+b\)", r"elke tijdseenheid komt hetzelfde getal erbij"],
                [r"exponentiële groei", r"\(f(x)=b\cdot a^{x}\)", r"elke tijdseenheid dezelfde factor"],
            ])),
            ("p", r"Staat in een tabel bij elke stap van \(1\) in \(x\) <strong>dezelfde "
                  r"vermenigvuldigingsfactor</strong>, dan past een <strong>exponentieel model</strong>. De rij "
                  r"<strong>\(3,\ 6,\ 12,\ 24\)</strong> is exponentieel, telkens maal \(2\); \(3,\ 6,\ 9,\ 12\) "
                  r"heeft een vaste toename en is dus lineair. <strong>Kies een lineair model als de verandering "
                  r"per tijdseenheid even groot blijft</strong>: een vast bedrag sparen per maand is lineair, "
                  r"intrest op intrest is exponentieel. <strong>Bij exponentiële groei komt er niet elke "
                  r"tijdseenheid evenveel bij</strong>, maar elke tijdseenheid hetzelfde percentage, en dus in "
                  r"absolute aantallen steeds meer. Een populatie van \(500\) die met \(8\%\) per jaar groeit, "
                  r"staat na tien jaar op \(500\cdot 1{,}08^{10}\approx 1079\), niet op \(500+10\cdot 40=900\)."),
            ("p", r"De <strong>verdubbelingstijd</strong> is <strong>de tijd die nodig is om twee keer zo groot te "
                  r"worden</strong>, en bij exponentiële groei is die altijd even lang, waar je ook begint te "
                  r"meten. De <strong>halveringstijd hoort bij een groeifactor kleiner dan \(1\)</strong>; "
                  r"radioactief verval is het bekendste voorbeeld. Heeft een stof een halveringstijd van \(5\) "
                  r"jaar, dan blijft er <strong>na \(10\) jaar \(\left(\tfrac{1}{2}\right)^{2}=\tfrac{1}{4}\)</strong> "
                  r"over."),
            ("p", r"<strong>Om te berekenen na hoeveel jaar een bedrag met groeifactor \(1{,}05\) verdubbeld is, "
                  r"heb je een logaritme nodig</strong>, want de onbekende staat in de exponent. Je lost "
                  r"\(1{,}05^{t}=2\) op:"),
            ("p", r"\[t=\frac{\ln 2}{\ln 1{,}05}\approx 14{,}2\ \text{jaar}\]"),
            ("p", r"De vuistregel \(\tfrac{100}{5}=20\) zit er met vijf jaar flink naast."),
            ("kader", r"Twee grenzen aan zo'n model. <strong>Een zuiver exponentieel model voorspelt een groei die "
                      r"nooit stopt</strong>, terwijl echte groei vastloopt op voedsel, ruimte of geld. En "
                      r"<strong>een groeimodel heeft vaak een praktisch domein</strong>, omdat een negatieve tijd "
                      r"meestal geen betekenis heeft: de functie bestaat wiskundig voor elke \(x\), maar in de "
                      r"context tel je pas vanaf het begin van de meting."),
        ]),
    ],
    onthoud=[
        r"\(\text{dom}\,a^{x}=\mathbb{R}\) en \(\text{ber}\,a^{x}=\left]0,+\infty\right[\).",
        r"Is \(a>1\), dan stijgt \(a^{x}\); is \(0<a<1\), dan daalt ze. \(a=1\) is niet toegelaten.",
        r"\(2^{x}\) heeft de rechte \(y=0\) als horizontale asymptoot en snijdt die nooit.",
        r"\(a^{x}\) gaat door \((0,1)\) en \((1,a)\); \(\log_{a}x\) gaat door \((1,0)\).",
        r"\(\text{dom}\log_{a}x=\left]0,+\infty\right[\), met de \(y\)-as als verticale asymptoot.",
        r"\(a^{x}\) en \(\log_{a}x\) spiegelen om de rechte \(y=x\).",
        r"Bij een toename van \(p\%\) is de groeifactor \(1+\tfrac{p}{100}\), en nooit negatief.",
        r"Groeifactoren combineer je door te vermenigvuldigen: per jaar is dat \(g^{12}\) uit een maandfactor.",
        r"In \(N(x)=b\cdot a^{x}\) is \(b\) de beginwaarde.",
        r"De verdubbelingstijd volgt uit \(a^{t}=2\), dus \(t=\tfrac{\ln 2}{\ln a}\).",
    ],
)

# ───────────────────────── 7. Goniometrische functies en goniometrie
BUNDELS["goniometrische-functies-en-goniometrie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Goniometrische functies en goniometrie",
    onder="Driehoeken oplossen met de sinus- en cosinusregel, de goniometrische cirkel, en de algemene sinusfunctie.",
    secties=[
        dict(kop="Driehoeken oplossen", blokken=[
            ("p", r"De som van de hoeken in een driehoek is \(180^\circ\). Ken je twee hoeken, dan "
                  r"volgt de derde daar meteen uit: \(\widehat{C} = 180^\circ - \widehat{A} - \widehat{B}\)."),
            ("p", tabel(["Wat je kent", "Welke regel", "Waarom"], [
                ["een zijde samen met de hoek ertegenover", "de sinusregel", "die koppelt telkens een zijde aan haar overstaande hoek"],
                ["twee zijden en de hoek ertussen", "de cosinusregel", "er is geen zijde met haar overstaande hoek bekend"],
                ["de drie zijden", "de cosinusregel", "de sinusregel heeft altijd één gekende hoek nodig"],
            ])),
            ("kader", r"Sinusregel: \(\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}\). "
                      r"Cosinusregel: \(a^{2} = b^{2} + c^{2} - 2bc\cos A\)."),
            ("p", r"In de cosinusregel is de hoek altijd die tegenover de zijde die je zoekt. Ken je "
                  r"de drie zijden, dan vorm je ze om naar "
                  r"\(\cos A = \dfrac{b^{2} + c^{2} - a^{2}}{2bc}\) en lees je de hoek af met de "
                  r"inverse cosinus."),
            ("kader", r"De cosinusregel is een veralgemening van de stelling van Pythagoras. Bij "
                      r"\(\widehat{A} = 90^\circ\) is \(\cos A = 0\), dus valt de laatste term weg "
                      r"en blijft \(a^{2} = b^{2} + c^{2}\) over."),
        ]),
        dict(kop="Graden en radialen", blokken=[
            ("p", r"Een radiaal is de hoek waarbij de boog even lang is als de straal. Omdat een "
                  r"halve cirkel \(\pi\) radialen meet, is \(\pi\) radialen hetzelfde als "
                  r"\(180^\circ\), en daaruit volgt elke andere omzetting. Zo is \(2\pi\) radialen "
                  r"gelijk aan \(360^\circ\), een volledige omwenteling, is \(90^\circ\) gelijk aan "
                  r"\(\dfrac{\pi}{2}\) en is \(\dfrac{\pi}{3}\) gelijk aan \(60^\circ\)."),
            ("p", r"Eén radiaal zelf is ongeveer \(57^\circ\), want \(\dfrac{180}{\pi} \approx 57{,}3\). "
                  r"Van graden naar radialen vermenigvuldig je met \(\dfrac{\pi}{180}\); de andere "
                  r"kant op met \(\dfrac{180}{\pi}\). Zet altijd eerst je rekenapp in de juiste "
                  r"stand, anders klopt geen enkele uitkomst."),
        ]),
        dict(kop="De goniometrische cirkel", blokken=[
            ("fig", svg.goniocirkel(),
             "Dezelfde hoek, twee aflezingen: de ene op de liggende as, de andere op de staande."),
            ("p", r"De goniometrische cirkel heeft straal \(1\). Door de straal op \(1\) te zetten "
                  r"zijn de coördinaten van het beeldpunt meteen \((\cos\alpha,\ \sin\alpha)\). De "
                  r"cosinus is dus de \(x\)-coördinaat en de sinus de \(y\)-coördinaat; die twee "
                  r"verwisselen is de klassieke fout."),
        ]),
        dict(kop="De waarden die je uit het hoofd kent", blokken=[
            ("p", r"Uit de cirkel lees je de bekende waarden af. \(\cos 0^\circ = 1\), want het "
                  r"beeldpunt ligt helemaal rechts. \(\sin 90^\circ = 1\), want dan ligt het "
                  r"bovenaan. En \(\sin 30^\circ = \tfrac{1}{2}\), net als \(\cos 60^\circ\)."),
            ("p", r"Omdat de sinus een coördinaat is op een cirkel met straal \(1\), geldt altijd "
                  r"\(-1 \leq \sin\alpha \leq 1\): groter dan \(1\) kan ze nooit worden. De tangens "
                  r"kent die grens niet, want \(\tan\alpha = \dfrac{\sin\alpha}{\cos\alpha}\) loopt "
                  r"naar oneindig zodra de cosinus naar nul gaat."),
        ]),
        dict(kop="De grondformule", blokken=[
            ("kader", r"\(\sin^{2}x + \cos^{2}x = 1\)"),
            ("p", r"Ze volgt rechtstreeks uit Pythagoras op de cirkel met straal \(1\): de twee "
                  r"coördinaten van het beeldpunt zijn de rechthoekszijden, de straal is de "
                  r"schuine zijde. Je gebruikt de grondformule vooral om de ene goniometrische "
                  r"functie in de andere om te zetten: ken je \(\sin x\), dan is "
                  r"\(\cos x = \pm\sqrt{1 - \sin^{2}x}\), en het teken bepaal je met het kwadrant."),
        ]),
        dict(kop="Hoeken die bij elkaar horen", blokken=[
            ("p", tabel(["Verband tussen twee hoeken", "Hun som of vorm", "Wat geldt"], [
                ["tegengesteld", r"\(\alpha\) en \(-\alpha\)", "dezelfde cosinus, tegengestelde sinus"],
                ["supplementair", r"samen \(180^\circ\)", "dezelfde sinus, tegengestelde cosinus"],
                ["complementair", r"samen \(90^\circ\)", "de sinus van de ene is de cosinus van de andere"],
            ])),
            ("p", r"Bij tegengestelde hoeken spiegelt het beeldpunt om de horizontale as, dus "
                  r"\(\cos(-\alpha) = \cos\alpha\) en \(\sin(-\alpha) = -\sin\alpha\). Bij "
                  r"supplementaire hoeken spiegelt het om de verticale as: "
                  r"\(\sin(180^\circ - \alpha) = \sin\alpha\) en "
                  r"\(\cos(180^\circ - \alpha) = -\cos\alpha\)."),
            ("p", r"Bij complementaire hoeken zie je het meteen in een rechthoekige driehoek: de "
                  r"overstaande zijde van de ene is de aanliggende van de andere, dus "
                  r"\(\sin(90^\circ - \alpha) = \cos\alpha\). Uit de eerste rij volgt ook dat de "
                  r"sinus een oneven functie is en de cosinus een even."),
        ]),
        dict(kop="De algemene sinusfunctie", blokken=[
            ("kader", r"\(y = a\sin(bx - c) + d\)"),
            ("p", tabel(["Letter", "Wat ze doet", "Voorbeeld"], [
                ["a", "de amplitude, de hoogte van de golf", r"\(y = 3\sin x\) heeft amplitude \(3\)"],
                ["b", r"perst de grafiek samen, de periode wordt \(\dfrac{2\pi}{b}\)", r"\(y = \sin 2x\) heeft periode \(\pi\)"],
                ["c", "zorgt voor een horizontale verschuiving, de faseverschuiving", "het schuift de hele golf opzij"],
                ["d", "schuift verticaal en bepaalt de evenwichtslijn", r"\(y = \sin x + 4\) schommelt rond \(y = 4\)"],
            ])),
            ("p", r"De periode van \(y = \sin x\) is \(2\pi\): na één volledige omwenteling begint "
                  r"het beeld opnieuw. De grafiek van \(y = \sin 3x\) heeft een periode die drie "
                  r"keer korter is. De frequentie van een periodieke functie is het aantal "
                  r"volledige schommelingen per eenheid, dus \(f = \dfrac{1}{T}\)."),
        ]),
        dict(kop="Amplitude, bereik en nulwaarden", blokken=[
            ("p", r"De amplitude kan niet negatief zijn, want ze is een afstand. Een negatieve "
                  r"factor voor de sinus spiegelt de grafiek wel om de evenwichtslijn."),
            ("p", r"Het bereik volgt uit \(a\) en \(d\): \(y = 2\sin x + 1\) loopt over "
                  r"\([-1,\ 3]\), en de grootste waarde van \(y = 5\sin x\) is \(5\). Op "
                  r"\([0,\ 2\pi]\), de grenzen inbegrepen, heeft \(y = \sin x\) drie nulwaarden: in "
                  r"\(0\), in \(\pi\) en in \(2\pi\)."),
            ("weetje", r"Een sinusfunctie is een geschikt model voor het getij aan de kust. Het "
                       r"water stijgt en daalt met een vaste periode rond een gemiddeld peil, en "
                       r"dat is precies wat zo'n functie beschrijft."),
        ]),
        dict(kop="Goniometrische formules", blokken=[
            ("kader", r"\(\sin 2x = 2\sin x\cos x\) en \(\cos 2x = \cos^{2}x - \sin^{2}x\)"),
            ("p", r"De verdubbelingsformules volgen uit de somformules met twee gelijke hoeken. "
                  r"Gewoon maal twee werkt niet: \(\cos 2x\) is dus géén \(2\cos x\). Een "
                  r"goniometrisch getal is geen factor die je zomaar buiten haalt."),
            ("p", r"De formules van Simpson zetten een som van sinussen om in een product. Ze heten "
                  r"daarom ook de som-naar-productformules, en ze zijn handig om een vergelijking "
                  r"te ontbinden in factoren: een product is nul zodra één factor nul is."),
            ("kader", r"Een goniometrische identiteit bewijs je door één lid te herleiden tot het "
                      r"andere met bekende formules. Enkele hoeken invullen toont alleen dat ze "
                      r"daar klopt, niet dat ze altijd klopt. Een grafiek is een aanwijzing, geen "
                      r"bewijs."),
        ]),
    ],
    onthoud=[
        r"De som van de hoeken in een driehoek is \(180^\circ\).",
        "Ken je een zijde met haar overstaande hoek, dan gebruik je de sinusregel; anders de cosinusregel.",
        r"\(a^{2} = b^{2} + c^{2} - 2bc\cos A\).",
        r"\(\pi\) radialen is \(180^\circ\); van graden naar radialen: maal \(\dfrac{\pi}{180}\).",
        r"Op de cirkel is \(\cos\alpha\) de \(x\)-coördinaat en \(\sin\alpha\) de \(y\)-coördinaat.",
        r"\(\sin^{2}x + \cos^{2}x = 1\).",
        "Supplementaire hoeken hebben dezelfde sinus, tegengestelde hoeken dezelfde cosinus.",
        r"In \(y = a\sin(bx - c) + d\) is \(a\) de amplitude en is de periode \(\dfrac{2\pi}{b}\).",
        r"\(\sin 2x = 2\sin x\cos x\).",
    ],
)

# ───────────────────────── 8. Limieten, continuïteit en asymptoten
BUNDELS["limieten-continuiteit-en-asymptoten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Limieten, continuïteit en asymptoten",
    onder="Wat een limiet is, hoe je onbepaaldheden wegwerkt, en hoe je alle soorten asymptoten vindt.",
    secties=[
        dict(kop="Wat een limiet zegt", blokken=[
            ("p", r"\(\lim\limits_{x \to a} f(x) = b\) betekent: de functiewaarden naderen \(b\) als "
                  r"\(x\) dicht genoeg bij \(a\) komt. Een limiet zegt dus iets over de buurt van "
                  r"\(a\), niet over \(a\) zelf. Een functie hoeft in \(a\) zelfs niet gedefinieerd "
                  r"te zijn om daar een limiet te hebben."),
            ("p", r"In de \(\varepsilon\)-\(\delta\)-definitie is \(\varepsilon\) eerst gegeven: de "
                  r"gewenste nauwkeurigheid op de \(y\)-as. Iemand daagt je uit met een "
                  r"\(\varepsilon\), en jij moet er een \(\delta\) bij vinden zodat alle \(x\) "
                  r"binnen \(\delta\) van \(a\) een beeld binnen \(\varepsilon\) van \(b\) hebben. "
                  r"Die volgorde omdraaien maakt de definitie betekenisloos."),
            ("p", r"De limiet in een punt bestaat als de linkerlimiet en de rechterlimiet gelijk "
                  r"zijn. Daarom bestaat \(\lim\limits_{x \to 0} \dfrac{1}{x}\) niet: van links "
                  r"kruipt ze naar \(-\infty\), van rechts naar \(+\infty\). Bij "
                  r"\(\dfrac{1}{x^{2}}\) is de limiet in \(0\) wél \(+\infty\), want een kwadraat "
                  r"is langs beide kanten positief."),
            ("p", r"Is de functie continu, dan mag je gewoon invullen: "
                  r"\(\lim\limits_{x \to 3} (x + 5) = 8\)."),
        ]),
        dict(kop="Wat er in één punt kan misgaan", blokken=[
            ("fig", svg.drieonderbrekingen(),
             "Links springt de grafiek, in het midden ontbreekt één punt, rechts loopt ze weg langs een rechte."),
            ("p", r"Een perforatie is een punt dat op de grafiek ontbreekt terwijl de limiet er wel "
                  r"bestaat; je tekent er een open bolletje. Bij een sprong verschillen de linker- "
                  r"en de rechterlimiet. En bij een pool gaat de functiewaarde naar \(\pm\infty\)."),
        ]),
        dict(kop="Onbepaaldheden wegwerken", blokken=[
            ("p", r"Een onbepaaldheid is een vorm waaruit je de uitkomst nog niet kan afleiden. "
                  r"\(\dfrac{0}{0}\) kan alles opleveren: een getal, oneindig of niets. Je moet "
                  r"eerst herschrijven."),
            ("p", tabel(["Wat je krijgt", "Wat je doet", "Voorbeeld"], [
                [r"\(\dfrac{0}{0}\)", "ontbinden en de gemeenschappelijke factor schrappen",
                 r"\(\lim\limits_{x \to 2} \dfrac{x^{2}-4}{x-2} = 4\)"],
                [r"teller \(\neq 0\), noemer \(= 0\)", r"er ligt een pool, dus \(\pm\infty\)",
                 "met een tekenonderzoek links en rechts bepaal je het teken"],
                [r"\(\infty - \infty\) met twee wortels", "vermenigvuldigen met de toegevoegde tweeterm",
                 r"\((a-b)(a+b) = a^{2} - b^{2}\) laat de wortels verdwijnen"],
                [r"\(\dfrac{\infty}{\infty}\)", "de hoogstegraadstermen tegen elkaar afwegen",
                 r"\(\lim\limits_{x \to +\infty} \dfrac{3x^{2}+1}{x^{2}-5} = 3\)"],
            ])),
            ("p", r"\(\lim\limits_{x \to +\infty} \dfrac{2x+1}{x^{2}} = 0\): de noemer groeit "
                  r"sneller dan de teller. In het algemeen bepaalt enkel de term met de hoogste "
                  r"graad het gedrag van een veeltermfunctie op oneindig. Bij een irrationale "
                  r"functie is de eerste stap de hoogstegraadsterm buiten de wortel afzonderen, "
                  r"bijvoorbeeld \(\sqrt{x^{2}+x} = |x|\sqrt{1 + \tfrac{1}{x}}\)."),
        ]),
        dict(kop="De regel van de l'Hôpital", blokken=[
            ("kader", r"Mag rechtstreeks op \(\dfrac{0}{0}\) en op \(\dfrac{\infty}{\infty}\): "
                      r"\(\lim \dfrac{f(x)}{g(x)} = \lim \dfrac{f'(x)}{g'(x)}\)."),
            ("p", r"De andere onbepaaldheden, zoals \(0 \cdot \infty\) of \(\infty - \infty\), moet "
                  r"je eerst omvormen tot een van die twee breuken. Op \(\dfrac{2}{0}\) mag je "
                  r"l'Hôpital niet toepassen: dat is geen onbepaaldheid maar een pool."),
            ("p", r"De gewone rekenregels helpen zolang de limieten bestaan en eindig zijn: de "
                  r"limiet van een som is de som van de limieten. Bij oneindig moet je opletten "
                  r"voor onbepaaldheden."),
        ]),
        dict(kop="Continuïteit", blokken=[
            ("kader", r"\(f\) is continu in \(a\) als \(f(a)\) bestaat en "
                      r"\(\lim\limits_{x \to a} f(x) = f(a)\)."),
            ("p", r"Drie dingen moeten dus kloppen: de limiet bestaat, de functiewaarde bestaat, en "
                  r"ze zijn gelijk. Op een grafiek betekent continuïteit dat je ze kan tekenen "
                  r"zonder je pen op te heffen. Een knik mag wel."),
            ("p", r"Elke veeltermfunctie is continu op heel haar domein: er zit geen noemer en geen "
                  r"wortel in, dus nergens een pool of een sprong. \(f(x) = \dfrac{1}{x}\) is niet "
                  r"continu in \(0\), want die functie bestaat daar niet. Verschillen de linker- en "
                  r"de rechterlimiet, dan zie je een sprong; bij een gat zijn de twee limieten net "
                  r"wel gelijk, maar ontbreekt de functiewaarde."),
            ("p", r"Continuïteit is belangrijk omdat je de limiet dan mag berekenen door gewoon in "
                  r"te vullen. En een functie die in een punt afleidbaar is, is daar zeker ook "
                  r"continu; omgekeerd geldt het niet, want \(f(x) = |x|\) is continu in \(0\) maar "
                  r"heeft er een knik en dus geen afgeleide."),
        ]),
        dict(kop="De drie soorten asymptoten", blokken=[
            ("p", tabel(["Soort asymptoot", "Hoe je ze vindt", "Wanneer ze er is"], [
                ["verticaal", "de noemer nulstellen", "bij een pool van de functie"],
                ["horizontaal", r"\(\lim\limits_{x \to \pm\infty} f(x)\) berekenen", "als die limiet een getal is"],
                ["schuin", "de euclidische deling, of de formules van Cauchy", "als de graad van de teller precies één hoger is"],
            ])),
            ("p", r"\(f(x) = \dfrac{1}{x-3}\) heeft één verticale asymptoot, met vergelijking "
                  r"\(x = 3\). Een verticale asymptoot hoort bij een pool: daar gaat de "
                  r"functiewaarde naar \(\pm\infty\)."),
            ("p", r"\(f(x) = \dfrac{3x+1}{x-2}\) heeft \(y = 3\) als horizontale asymptoot: teller "
                  r"en noemer hebben dezelfde graad, dus je deelt de hoogste coëfficiënten. Een "
                  r"grafiek mag haar horizontale asymptoot snijden, zelfs meermaals; alleen op "
                  r"oneindig moet ze er onbeperkt dicht bij komen. Een verticale asymptoot snijden "
                  r"kan niet."),
        ]),
        dict(kop="De schuine asymptoot", blokken=[
            ("p", r"Bij een schuine asymptoot werk je met de euclidische deling: het quotiënt is de "
                  r"vergelijking van de asymptoot, want de rest gedeeld door de noemer kruipt naar "
                  r"nul. Zo is \(\dfrac{x^{2}+1}{x} = x + \dfrac{1}{x}\), met \(y = x\) als schuine "
                  r"asymptoot."),
            ("kader", r"Formules van Cauchy: \(m = \lim\limits_{x \to \infty} \dfrac{f(x)}{x}\) en "
                      r"\(q = \lim\limits_{x \to \infty} \left(f(x) - m\,x\right)\)."),
            ("p", r"Een functie kan aan dezelfde kant niet tegelijk een horizontale en een schuine "
                  r"asymptoot hebben: allebei beschrijven ze het gedrag op oneindig, en dat kan "
                  r"maar één ding tegelijk zijn. Aan de andere kant kan het wel anders lopen. Een "
                  r"gewone parabool heeft nul asymptoten: ze groeit wel naar oneindig, maar nadert "
                  r"daarbij geen enkele rechte."),
            ("kader", r"Teken asymptoten als stippellijnen, want ze horen niet bij de grafiek. Een "
                      r"asymptoot is een hulplijn die het gedrag beschrijft."),
        ]),
    ],
    onthoud=[
        r"Een limiet zegt iets over de buurt van \(a\), niet over \(a\) zelf.",
        "De limiet in een punt bestaat als de linkerlimiet en de rechterlimiet gelijk zijn.",
        r"Bij \(\dfrac{0}{0}\) ontbind je en schrap je de gemeenschappelijke factor.",
        "Op oneindig bepaalt enkel de term met de hoogste graad het gedrag van een veeltermfunctie.",
        r"L'Hôpital mag rechtstreeks op \(\dfrac{0}{0}\) en \(\dfrac{\infty}{\infty}\).",
        r"\(f\) is continu in \(a\) als \(\lim\limits_{x \to a} f(x) = f(a)\).",
        "Een functie die in een punt afleidbaar is, is daar ook continu; omgekeerd niet.",
        "Verticale asymptoot: noemer nulstellen. Schuine: het quotiënt van de deling.",
    ],
)

# ───────────────────────── 9. Afgeleiden en het verloop van een functie
BUNDELS["afgeleiden-en-het-verloop-van-een-functie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Afgeleiden en het verloop van een functie",
    onder="Van differentiequotiënt naar raaklijn, de rekenregels, en het volledige functieonderzoek.",
    secties=[
        dict(kop="Van gemiddelde naar ogenblikkelijke verandering", blokken=[
            ("fig", svg.koordeenraaklijn(),
             "Twee punten geven een rechte; schuiven ze naar elkaar toe, dan blijft er één rechte over."),
            ("p", r"Een differentiequotiënt \(\dfrac{f(b) - f(a)}{b - a}\) berekent de gemiddelde "
                  r"verandering over een interval. Voor \(f(x) = x^{2}\) tussen \(1\) en \(3\) is "
                  r"dat \(\dfrac{9 - 1}{3 - 1} = 4\)."),
            ("kader", r"\(f'(a) = \lim\limits_{h \to 0} \dfrac{f(a+h) - f(a)}{h}\)"),
            ("p", r"Je laat het tweede punt naar het eerste kruipen; de koorde wordt dan de "
                  r"raaklijn. Meetkundig is \(f'(a)\) dus de richtingscoëfficiënt van de raaklijn "
                  r"in dat punt. Een voorbeeld van begin tot eind: de raaklijn aan \(f(x) = x^{2}\) "
                  r"in \(x = 3\) is \(y = 6x - 9\). De helling is \(f'(3) = 6\), het raakpunt is "
                  r"\((3,\ 9)\), en invullen geeft \(q = -9\)."),
        ]),
        dict(kop="De rekenregels", blokken=[
            ("p", tabel(["Functie", "Haar afgeleide", "Let op"], [
                [r"\(x^{n}\)", r"\(n\,x^{n-1}\)", "de exponent komt vooraan en gaat zelf met één omlaag"],
                [r"\(c\)", r"\(0\)", "de grafiek is een horizontale rechte"],
                [r"\(5x + 2\)", r"\(5\)", "de afgeleide van een rechte is haar richtingscoëfficiënt"],
                [r"\(\sin x\)", r"\(\cos x\)", r"en \(\left(\cos x\right)' = -\sin x\)"],
                [r"\(e^{x}\)", r"\(e^{x}\)", r"de machtsregel geldt hier niet, \(x\) staat in de exponent"],
                [r"\(\ln x\)", r"\(\dfrac{1}{x}\)", "altijd positief, dus de functie stijgt overal"],
            ])),
            ("p", r"Zo is \(f'(3) = 6\) voor \(f(x) = x^{2}\), en \(f'(2) = 12\) voor "
                  r"\(f(x) = x^{3}\). Sinus wordt cosinus, en cosinus wordt min sinus: pas na vier "
                  r"keer afleiden sta je weer bij het begin."),
        ]),
        dict(kop="Product, quotiënt en ketting", blokken=[
            ("kader", r"\(\left(u\,v\right)' = u'v + u\,v'\), "
                      r"\(\left(\dfrac{u}{v}\right)' = \dfrac{u'v - u\,v'}{v^{2}}\) en "
                      r"\(\left(f(g(x))\right)' = f'(g(x)) \cdot g'(x)\)"),
            ("p", r"De afgeleide van een product is dus niet het product van de afgeleiden: "
                  r"probeer het met \(x \cdot x\), de afgeleide is \(2x\) en niet \(1\). Bij de "
                  r"quotiëntregel staat de noemer in het kwadraat onderaan, en let op het "
                  r"minteken: dat hoort bij de quotiëntregel, niet bij de productregel."),
            ("p", r"De kettingregel leid je af van buiten naar binnen, en onderweg vermenigvuldig "
                  r"je. De binnenste afgeleide vergeten is de klassieke fout: "
                  r"\(\left(\sin 3x\right)' = 3\cos 3x\), niet \(\cos 3x\)."),
        ]),
        dict(kop="De hellinggrafiek", blokken=[
            ("p", r"Op de verticale as van een hellinggrafiek staat \(f'(x)\). Een hellinggrafiek "
                  r"is dus gewoon de grafiek van de afgeleide functie."),
            ("p", r"Waar \(f\) een vloeiend maximum heeft, snijdt \(f'\) de \(x\)-as: in de top "
                  r"loopt de raaklijn horizontaal, dus is de afgeleide daar nul en wisselt ze van "
                  r"teken."),
        ]),
        dict(kop="Stijgen, dalen en extrema", blokken=[
            ("p", r"Is \(f'(x) > 0\) op een interval, dan stijgt de functie daar. Het teken van de "
                  r"afgeleide gaat over de richting, niet over de hoogte: een stijgende functie kan "
                  r"best negatieve waarden hebben."),
            ("p", r"Is \(f'(a) = 0\) en wisselt \(f'\) daar van plus naar min, dan heeft \(f\) in "
                  r"\(a\) een maximum; van min naar plus geeft een minimum. Niet elk punt waar de "
                  r"afgeleide nul is, is een extremum: bij \(f(x) = x^{3}\) is \(f'(0) = 0\), maar "
                  r"de functie blijft stijgen. En een functie kan een maximum bereiken in een punt "
                  r"waar ze niet afleidbaar is, zoals in de scherpe punt van \(f(x) = -|x|\)."),
            ("p", r"\(f(x) = x^{3} - 3x\) heeft twee extrema: \(f'(x) = 3x^{2} - 3\) is nul in "
                  r"\(-1\) en in \(1\). Het minimum ligt bij \(x = 1\). Twee nulwaarden van de "
                  r"afgeleide verdelen de getallenas in drie stukken in het tekenschema."),
        ]),
        dict(kop="Hol, bol en buigpunten", blokken=[
            ("p", r"Is \(f''(x) > 0\) op een interval, dan is de grafiek daar hol, met de holle "
                  r"kant naar boven: de helling neemt toe. Buigpunten vind je waar \(f''(x) = 0\) "
                  r"én \(f''\) van teken wisselt."),
            ("p", r"\(f'\) hoeft in een buigpunt niet nul te zijn: een buigpunt kan midden op een "
                  r"stijgend stuk liggen, want alleen de kromming verandert er. Is \(f'(a) = 0\) en "
                  r"\(f''(a) > 0\), dan ligt er een minimum; dat is de tweede-afgeleidetest."),
            ("p", r"Stijgt een functie steeds trager, dan is \(f' > 0\) en \(f'' < 0\). Stijgen "
                  r"geeft een positieve eerste afgeleide; trager stijgen betekent dat die afgeleide "
                  r"zelf daalt. In de samenvattende tabel van een functieonderzoek zet je het teken "
                  r"van \(f'\) en \(f''\), met stijgen, dalen, hol, bol, extrema en buigpunten. "
                  r"Daarmee schets je de grafiek zonder nog één punt te berekenen."),
        ]),
        dict(kop="Rolle en Lagrange", blokken=[
            ("p", r"De stelling van Rolle eist dat \(f(a) = f(b)\) in de twee uiteinden. Pas dan "
                  r"kan je besluiten dat er ergens tussenin een punt ligt met een horizontale "
                  r"raaklijn."),
            ("kader", r"Middelwaardestelling van Lagrange: er is een \(c\) tussen \(a\) en \(b\) "
                      r"met \(f'(c) = \dfrac{f(b) - f(a)}{b - a}\)."),
            ("p", r"Ergens is de raaklijn dus evenwijdig met de koorde tussen de uiteinden: er is "
                  r"een punt waar de ogenblikkelijke verandering gelijk is aan de gemiddelde. Rolle "
                  r"is het bijzondere geval waarin die koorde horizontaal loopt."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", r"De eerste stap bij een extremumprobleem met context is zelf een veranderlijke "
                  r"kiezen en het functievoorschrift opstellen. Zonder voorschrift valt er niets af "
                  r"te leiden. Daarna bereken je de extrema, en je gaat na of je oplossing in het "
                  r"praktisch domein ligt: een negatieve lengte is wiskundig misschien een "
                  r"oplossing, in de opgave niet."),
            ("p", r"Geeft \(s(t)\) de afgelegde weg in functie van de tijd, dan is \(s'(t)\) de "
                  r"snelheid op dat ogenblik; de afgeleide daarvan is de versnelling, en de "
                  r"gemiddelde snelheid is het differentiequotiënt over het hele interval. Kent een "
                  r"bedrijf zijn totale kost in functie van het aantal stuks, dan is de marginale "
                  r"kost de afgeleide van die totale kost: ze zegt wat één extra stuk ongeveer kost."),
            ("weetje", r"Is \(f'(x) > 0\) op heel het domein, dan is \(f\) overal strikt stijgend "
                       r"en dus inverteerbaar. Strikt stijgend betekent immers dat elke "
                       r"functiewaarde maar één keer voorkomt."),
        ]),
    ],
    onthoud=[
        "Een differentiequotiënt berekent de gemiddelde verandering over een interval.",
        r"\(f'(a)\) is de richtingscoëfficiënt van de raaklijn in dat punt.",
        r"\(\left(x^{n}\right)' = n\,x^{n-1}\).",
        r"\(\left(u\,v\right)' = u'v + u\,v'\): niet het product van de afgeleiden.",
        r"Kettingregel: \(\left(f(g(x))\right)' = f'(g(x)) \cdot g'(x)\).",
        r"Waar \(f\) een vloeiend maximum heeft, snijdt \(f'\) de \(x\)-as.",
        "Is de afgeleide nul zonder tekenwissel, dan is er geen extremum.",
        r"Buigpunten: \(f''(x) = 0\) én een tekenwissel.",
        r"Rolle eist \(f(a) = f(b)\); Lagrange geeft een raaklijn evenwijdig met de koorde.",
    ],
)

# ───────────────────────── 10. Rijen en hun limiet
BUNDELS["rijen-en-hun-limiet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rijen en hun limiet",
    onder="Rekenkundige en meetkundige rijen, hun sommen, en wat convergeren betekent.",
    secties=[
        dict(kop="Twee soorten rijen", blokken=[
            ("p", r"Een rij is een lijstje getallen met een vaste volgorde. Je noteert de "
                  r"\(n\)-de term als \(u_{n}\), dus \(u_{1}\) is de eerste term, \(u_{2}\) de "
                  r"tweede. Er zijn twee soorten die telkens terugkomen."),
            ("p", tabel(["Soort rij", "Wat je telkens doet", "Het vaste getal", "In symbolen"], [
                ["rekenkundige rij", "telkens hetzelfde getal optellen",
                 r"het verschil \(d\)", r"\(u_{n+1} = u_{n} + d\)"],
                ["meetkundige rij", "telkens met hetzelfde getal vermenigvuldigen",
                 r"de reden \(q\)", r"\(u_{n+1} = u_{n} \cdot q\)"],
            ])),
        ]),
        dict(kop="De twee rijen in beeld", blokken=[
            ("fig", svg.tweerijen(),
             "Links de rij 3, 7, 11, 15, 19, 23. Rechts de rij 2, 6, 18, 54, 162."),
            ("p", r"<strong>De punten \((n,\ u_{n})\) van een rekenkundige rij liggen op een "
                  r"rechte</strong>, met \(d\) als richtingscoëfficiënt. Daarom hoort een "
                  r"rekenkundige rij bij <strong>lineaire groei</strong> en een meetkundige rij "
                  r"bij <strong>exponentiële groei</strong>: een vaste factor per stap is net wat "
                  r"\(f(x) = a \cdot b^{x}\) doet."),
        ]),
        dict(kop="Het verschil en de reden vinden", blokken=[
            ("p", r"Het verschil haal je uit een aftrekking, de reden uit een deling: "
                  r"\(d = u_{n+1} - u_{n}\) en \(q = \dfrac{u_{n+1}}{u_{n}}\)."),
            ("p", tabel(["Rij", "Soort", "Vast getal"], [
                [r"\(3,\ 7,\ 11,\ 15,\ \dots\)", "rekenkundig", r"\(d = 4\)"],
                [r"\(2,\ 6,\ 18,\ 54,\ \dots\)", "meetkundig", r"\(q = 3\)"],
                [r"\(1,\ \tfrac{1}{3},\ \tfrac{1}{9},\ \dots\)", "meetkundig",
                 r"\(q = \tfrac{1}{3}\)"],
            ])),
            ("p", r"De rij \(2,\ 6,\ 18,\ 54,\ \dots\) is dus <strong>geen rekenkundige "
                  r"rij</strong>: het verschil groeit telkens (\(4\), dan \(12\), dan \(36\)) "
                  r"terwijl de factor \(3\) blijft."),
        ]),
        dict(kop="Recursief of expliciet", blokken=[
            ("p", r"<strong>Een recursief voorschrift berekent \(u_{n+1}\) uit \(u_{n}\)</strong>, "
                  r"en daarom heb je er altijd een beginterm bij nodig. Een <strong>expliciet "
                  r"voorschrift</strong> geeft \(u_{n}\) rechtstreeks, zonder dat je eerst alle "
                  r"vorige termen moet berekenen."),
            ("kader", r"recursief: \(u_{1} = 3\) en \(u_{n+1} = u_{n} + 4\)<br>"
                      r"expliciet: \(u_{n} = 4n - 1\)<br>"
                      r"Twee schrijfwijzen van dezelfde rij. Vul \(n = 1\) in en je vindt "
                      r"\(u_{1} = 3\)."),
        ]),
        dict(kop="De n-de term van een rekenkundige rij", blokken=[
            ("p", r"<strong>Het expliciete voorschrift van een rekenkundige rij is "
                  r"\(u_{n} = u_{1} + (n-1)\,d\).</strong> Om bij de \(n\)-de term te komen tel "
                  r"je het verschil precies \(n-1\) keer op bij de eerste term. Zo is de tiende "
                  r"term van \(3,\ 7,\ 11,\ \dots\) gelijk aan "
                  r"\(u_{10} = 3 + 9 \cdot 4 = 39\): negen stappen en niet tien, want \(u_{1}\) "
                  r"staat er al."),
        ]),
        dict(kop="De n-de term van een meetkundige rij", blokken=[
            ("p", r"Bij een meetkundige rij vermenigvuldig je in plaats van op te tellen: "
                  r"\(u_{n} = u_{1} \cdot q^{\,n-1}\). De vijfde term van \(2,\ 6,\ 18,\ \dots\) "
                  r"is dus \(u_{5} = 2 \cdot 3^{4} = 2 \cdot 81 = 162\)."),
        ]),
        dict(kop="De som van een rekenkundige rij", blokken=[
            ("p", r"<strong>De som van de eerste \(n\) termen van een rekenkundige rij is "
                  r"\(S_{n} = n \cdot \dfrac{u_{1} + u_{n}}{2}\)</strong>, dus \(n\) maal het "
                  r"gemiddelde van de eerste en de laatste term. Je legt de rij twee keer naast "
                  r"elkaar, een keer vooruit en een keer achteruit; elk paar geeft dan dezelfde "
                  r"som \(u_{1} + u_{n}\). Zo is "
                  r"\(1 + 2 + 3 + \dots + 10 = 10 \cdot \dfrac{1 + 10}{2} = 55\)."),
        ]),
        dict(kop="De som van een meetkundige rij", blokken=[
            ("p", r"<strong>Voor een meetkundige rij met \(q \neq 1\) geldt "
                  r"\(S_{n} = u_{1} \cdot \dfrac{1 - q^{\,n}}{1 - q}\).</strong> Je hebt er dus "
                  r"<strong>de eerste term, de reden en het aantal termen</strong> voor nodig, "
                  r"want \(q\) staat er tot de macht \(n\) in. Die formule werkt niet als de "
                  r"reden één is: dan wordt de noemer nul en reken je gewoon "
                  r"\(S_{n} = n \cdot u_{1}\)."),
        ]),
        dict(kop="Hoe een rij verloopt", blokken=[
            ("p", r"<strong>Een rekenkundige rij daalt als \(d < 0\).</strong> Alleen het teken "
                  r"van het verschil beslist: een rij die begint bij \(u_{1} = -100\) met "
                  r"\(d = 3\) stijgt gewoon."),
            ("p", r"Een <strong>meetkundige rij met \(q > 1\) en \(u_{1} > 0\) stijgt, met een "
                  r"toenemende stijging</strong>: elke stap wordt groter dan de vorige, want je "
                  r"vermenigvuldigt telkens een groter getal met dezelfde \(q\). "
                  r"<strong>Bij \(q = 1\) blijft elke term gelijk</strong> en is de rij constant, "
                  r"dus zo'n rij stijgt zeker niet steeds sneller. <strong>Bij \(q < 0\) wisselen "
                  r"de termen van teken</strong>: ze zijn om beurten positief en negatief. Zo'n "
                  r"rij heet <strong>alternerend</strong>, en je herkent haar aan een factor "
                  r"\((-1)^{n}\) in het voorschrift."),
            ("weetje", r"Zet je geld op een rekening met <strong>samengestelde intrest</strong>, "
                       r"dan vormen de jaarlijkse saldo's een <strong>meetkundige rij</strong>: "
                       r"elk jaar dezelfde groeifactor \(q\). Bij enkelvoudige intrest tel je elk "
                       r"jaar hetzelfde bedrag op, en dan is de rij rekenkundig."),
        ]),
        dict(kop="Convergeren en divergeren", blokken=[
            ("p", r"<strong>Een rij convergeert als haar termen een vast eindig getal "
                  r"naderen</strong>: \(\lim\limits_{n \to +\infty} u_{n} = L\). Gaat ze naar "
                  r"oneindig of blijft ze springen, dan <strong>divergeert</strong> ze. "
                  r"<strong>Een divergente rij kan dus naar \(+\infty\) gaan</strong>: divergent "
                  r"betekent alleen dat er geen eindige limiet is."),
            ("kader", r"<strong>Bij een rij spreek je alleen over de limiet op oneindig, omdat "
                      r"\(n\) enkel in de natuurlijke getallen \(\mathbb{N}\) ligt.</strong> Er "
                      r"zijn geen tussenwaarden om naartoe te kruipen: tussen \(u_{3}\) en "
                      r"\(u_{4}\) ligt niets."),
        ]),
        dict(kop="Limieten van bekende rijen", blokken=[
            ("p", tabel(["Rij", "Limiet", "Waarom"], [
                [r"\(\dfrac{1}{n}\)", r"\(0\)", "hoe groter n, hoe kleiner de breuk"],
                [r"\(\dfrac{2n + 1}{n}\)", r"\(2\)",
                 r"splits op in \(2 + \dfrac{1}{n}\)"],
                [r"\(2^{\,n}\)", r"\(+\infty\)", "bij een reden groter dan één groeien de termen onbeperkt"],
                [r"\((-1)^{n}\)", "bestaat niet", r"de rij blijft springen tussen \(-1\) en \(1\)"],
                [r"\(q^{\,n}\) met \(-1 < q < 1\)", r"\(0\)",
                 "telkens met een kleiner getal vermenigvuldigen"],
            ])),
            ("p", r"<strong>Een rekenkundige rij met \(d = 2\) convergeert niet</strong>: ze "
                  r"blijft met twee per stap toenemen. Alleen een rekenkundige rij met "
                  r"\(d = 0\) convergeert. Voor <strong>twee convergente rijen is de limiet van "
                  r"de som de som van de limieten</strong>, net als bij functies."),
        ]),
        dict(kop="De somrij", blokken=[
            ("p", r"<strong>De somrij van een rij is de rij \(S_{1},\ S_{2},\ S_{3},\ \dots\) "
                  r"van de som van de eerste \(n\) termen.</strong> Haar \(n\)-de term is dus "
                  r"\(S_{n} = u_{1} + u_{2} + \dots + u_{n}\). <strong>De somrij van een "
                  r"meetkundige rij met \(q = \tfrac{1}{2}\) convergeert.</strong>"),
            ("fig", svg.meetkundigesom(),
             r"De stukken 1, ½, ¼, ⅛ … achter elkaar gelegd. Elk volgend stuk is half "
             r"zo lang als het vorige."),
        ]),
        dict(kop="De oneindige meetkundige som", blokken=[
            ("p", r"<strong>De som van een oneindige meetkundige rij is "
                  r"\(S = \dfrac{u_{1}}{1 - q}\).</strong> In de gewone somformule kruipt "
                  r"\(q^{\,n}\) immers naar nul, en dan blijft dit over. Zo is "
                  r"\(1 + \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{8} + \dots = "
                  r"\dfrac{1}{1 - 0{,}5} = 2\)."),
            ("p", r"<strong>Niet elke oneindige meetkundige rij heeft een eindige som.</strong> "
                  r"De voorwaarde is dat <strong>de absolute waarde van de reden kleiner is dan "
                  r"één</strong>, dus \(|q| < 1\); bij \(q = 2\) groeit de som onbeperkt."),
        ]),
        dict(kop="Een bal die uitstuitert", blokken=[
            ("p", r"Een voorbeeld uit de praktijk: een <strong>bal die telkens tot \(70\%\) van "
                  r"de vorige hoogte stuitert</strong>. Omdat \(q = 0{,}7\) onder één ligt, kan "
                  r"je <strong>de totale afgelegde hoogte berekenen</strong>: oneindig veel "
                  r"sprongen geven samen een eindige hoogte."),
            ("weetje", r"<strong>\(0{,}999\dots\), met oneindig veel negens, is gelijk aan "
                       r"\(1\).</strong> Het is de som van een meetkundige rij met "
                       r"\(u_{1} = \tfrac{9}{10}\) en \(q = \tfrac{1}{10}\), en "
                       r"\(\dfrac{0{,}9}{1 - 0{,}1} = 1\)."),
        ]),
    ],
    onthoud=[
        r"Rekenkundig: \(u_{n+1} = u_{n} + d\). Meetkundig: \(u_{n+1} = u_{n} \cdot q\).",
        r"Een recursief voorschrift berekent elke term uit de vorige en heeft een beginterm nodig.",
        r"\(u_{n} = u_{1} + (n-1)\,d\) en \(u_{n} = u_{1} \cdot q^{\,n-1}\).",
        r"\(S_{n} = n \cdot \dfrac{u_{1} + u_{n}}{2}\) en \(S_{n} = u_{1} \cdot \dfrac{1 - q^{\,n}}{1 - q}\).",
        r"Een rekenkundige rij hoort bij lineaire groei, een meetkundige rij bij exponentiële groei.",
        r"Bij \(q < 0\) wisselen de termen van teken: de rij is alternerend.",
        r"Een rij convergeert als haar termen een vast eindig getal naderen.",
        r"De oneindige meetkundige som is \(S = \dfrac{u_{1}}{1 - q}\), en bestaat alleen als \(|q| < 1\).",
    ],
)

# ───────────────────────── 11. Primitieven en de onbepaalde integraal
BUNDELS["primitieven-en-de-onbepaalde-integraal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Primitieven en de onbepaalde integraal",
    onder="Afleiden in omgekeerde richting, de basisprimitieven en de vier integratiemethoden.",
    secties=[
        dict(kop="Wat een primitieve is", blokken=[
            ("p", r"<strong>Een primitieve functie \(F\) van \(f\) is een functie met "
                  r"\(F'(x) = f(x)\).</strong> <strong>Primitiveren is dus de omgekeerde bewerking "
                  r"van afleiden</strong>, en dat is meteen de beste controle op je werk: "
                  r"<strong>leid je antwoord af en je moet de integrand terugkrijgen</strong>. Leid "
                  r"je een primitieve van \(f\) af, dan krijg je <strong>\(f\)</strong>."),
            ("p", r"Je noteert dat zo: \(\int f(x)\,dx = F(x) + C\). De functie die je integreert "
                  r"heet de <strong>integrand</strong>, en die staat tussen \(\int\) en \(dx\)."),
        ]),
        dict(kop=r"Waarom er altijd \(+\,C\) bij staat", blokken=[
            ("p", r"<strong>Bij een onbepaalde integraal schrijf je altijd \(+\,C\), omdat elke "
                  r"constante bij het afleiden verdwijnt.</strong> Een functie met één primitieve "
                  r"heeft er dus <strong>oneindig veel</strong>. <strong>Twee primitieven van "
                  r"dezelfde functie hebben altijd dezelfde afgeleide</strong>; ze verschillen "
                  r"alleen een constante."),
            ("fig", svg.primitievenfamilie(),
             r"Drie primitieven van \(f(x) = x\), namelijk \(F(x) = \tfrac{x^{2}}{2} + C\)."),
            ("p", r"Daarom heet de integraal zonder grenzen de <strong>onbepaalde</strong> "
                  r"integraal: <strong>de uitkomst blijft op een constante na onbepaald</strong>. "
                  r"Die \(C\) heet de <strong>integratieconstante</strong>, en ze hoort bij elke "
                  r"onbepaalde integraal: \(\int 5\,dx = 5x + C\)."),
        ]),
        dict(kop="Onbepaald of bepaald", blokken=[
            ("p", r"<strong>Het verschil met een bepaalde integraal: die heeft grenzen en levert "
                  r"een getal op.</strong> \(\int f(x)\,dx\) is een familie van functies, "
                  r"\(\int_{a}^{b} f(x)\,dx\) is een getal. <strong>Bij een bepaalde integraal "
                  r"schrijf je geen \(+\,C\), want die valt bij het aftrekken van de twee grenzen "
                  r"weg</strong>: \(\left(F(b) + C\right) - \left(F(a) + C\right) = F(b) - F(a)\)."),
            ("weetje", r"<strong>Elke continue functie heeft een primitieve.</strong> Dat volgt uit "
                       r"de hoofdstelling van de integraalrekening. Of je die primitieve ook in een "
                       r"formule kan schrijven, is een andere vraag."),
        ]),
        dict(kop="De basisprimitieven", blokken=[
            ("p", tabel(["Integraal", "Uitkomst", "Let op"], [
                [r"\(\int x^{n}\,dx\)", r"\(\dfrac{x^{\,n+1}}{n+1} + C\)",
                 "de exponent gaat omhoog, en je deelt door die nieuwe exponent"],
                [r"\(\int \dfrac{1}{x}\,dx\)", r"\(\ln|x| + C\)",
                 r"de regel hierboven werkt niet voor \(n = -1\)"],
                [r"\(\int k\,dx\)", r"\(k\,x + C\)",
                 r"de grafiek van de primitieve is een rechte met helling \(k\)"],
                [r"\(\int \cos x\,dx\)", r"\(\sin x + C\)", "afleiden gaat de andere kant op"],
                [r"\(\int \sin x\,dx\)", r"\(-\cos x + C\)", "het minteken hoort erbij"],
                [r"\(\int e^{x}\,dx\)", r"\(e^{x} + C\)",
                 "die functie is haar eigen afgeleide én haar eigen primitieve"],
            ])),
            ("p", r"De machtregel <strong>werkt niet voor \(n = -1\)</strong>, want dan zou je door "
                  r"nul delen; die ene integraal geeft net de logaritme. De <strong>absolute "
                  r"waarde</strong> in \(\ln|x|\) zorgt dat de formule ook werkt voor \(x < 0\)."),
        ]),
        dict(kop="De lineariteit", blokken=[
            ("p", r"<strong>De lineariteit van de integraal</strong> zegt dat je <strong>termsgewijs "
                  r"mag integreren en constanten buiten mag halen</strong>:"),
            ("kader", r"\(\int \left(f(x) + g(x)\right)dx = \int f(x)\,dx + \int g(x)\,dx\)<br>"
                      r"\(\int k\,f(x)\,dx = k \int f(x)\,dx\)"),
            ("p", r"<strong>Een constante factor mag dus voor het integraalteken</strong>; een "
                  r"factor met een \(x\) erin niet. Voor een product of een quotiënt werkt het "
                  r"evenmin, en daar bestaan net de andere methodes voor."),
            ("p", r"Twee bepaalde integralen om mee te oefenen: \(\int_{0}^{2} x\,dx = 2\) (de "
                  r"primitieve is \(\tfrac{x^{2}}{2}\), en het is ook de oppervlakte van een "
                  r"driehoek met basis \(2\) en hoogte \(2\)), en "
                  r"\(\int_{0}^{1} x^{2}\,dx = \tfrac{1}{3}\)."),
        ]),
        dict(kop="De vier integratiemethoden", blokken=[
            ("p", tabel(["Methode", "Wanneer", "Hoe"], [
                ["onmiddellijke integratie", "de integrand staat meteen in de tabel",
                 r"soms moet je eerst herschrijven, \(\sqrt{x} = x^{1/2}\)"],
                ["integratie door splitsing", "de integrand is een som",
                 "elke term apart integreren, dankzij de lineariteit"],
                ["integratie door substitutie",
                 "een binnenste functie staat er met haar afgeleide naast",
                 "de kettingregel in omgekeerde richting"],
                ["partiële integratie", "een product van twee heel verschillende functies",
                 r"\(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\)"],
            ])),
            ("p", r"<strong>Splits je \(\int (2x + 3)\,dx\), dan valt ze uiteen in twee aparte "
                  r"integralen</strong>, en de factor \(2\) mag je buiten de eerste halen."),
        ]),
        dict(kop="Substitutie van dichtbij", blokken=[
            ("p", r"<strong>Bij een substitutie kies je als nieuwe veranderlijke \(u\) een binnenste "
                  r"functie waarvan de afgeleide ook in de integrand staat.</strong> Zonder die "
                  r"afgeleide erbij kan je \(dx\) niet omzetten naar \(du\) en loopt de substitutie "
                  r"vast."),
            ("p", r"Een vast patroon dat je overal terugziet: "
                  r"<strong>\(\int \dfrac{f'(x)}{f(x)}\,dx = \ln|f(x)| + C\)</strong>. Je herkent "
                  r"het aan de afgeleide van de noemer die in de teller staat. <strong>Een integraal "
                  r"met een wortel erin kan je wel degelijk met substitutie oplossen</strong>; dat "
                  r"is er zelfs een van de vaste methodes voor."),
            ("kader", r"<strong>Bij een bepaalde integraal mag je na een substitutie de oude grenzen "
                      r"niet laten staan.</strong> Ze horen bij \(x\), niet bij \(u\): zet ze mee "
                      r"om, of ga na de integratie eerst terug naar \(x\)."),
        ]),
        dict(kop="Partiële integratie", blokken=[
            ("p", r"<strong>Partiële integratie volgt uit de productregel voor afgeleiden</strong>: "
                  r"je integreert \(\left(u\,v\right)' = u'v + u\,v'\) langs beide kanten en brengt "
                  r"één term naar de andere kant. Zo krijg je "
                  r"\(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\)."),
            ("p", r"Het typische geval is <strong>\(\int x\,e^{x}\,dx\)</strong>: een product van "
                  r"twee heel verschillende soorten functies. <strong>Het minteken in de formule "
                  r"vergeten</strong> is de meest gemaakte fout bij deze methode."),
        ]),
        dict(kop="Handigheden", blokken=[
            ("p", r"<strong>Bij een breuk waarvan de teller een hogere graad heeft dan de noemer, "
                  r"voer je eerst een euclidische deling uit.</strong> Na de deling houd je een "
                  r"veelterm over plus een eenvoudige rest, en die twee stukken integreer je apart."),
            ("p", r"<strong>Soms heb je goniometrische formules nodig</strong>, en dan vooral "
                  r"<strong>de grondformule en de formule voor de dubbele hoek</strong>. Daarmee "
                  r"herschrijf je bijvoorbeeld \(\sin^{2}x = \dfrac{1 - \cos 2x}{2}\) tot iets wat "
                  r"je wel kan integreren. Zo is \(\int_{0}^{\pi} \sin x\,dx = 2\) en "
                  r"\(\int_{1}^{3} 2x\,dx = 8\)."),
            ("p", r"<strong>Volstaat één methode niet, dan combineer je methodes</strong>, "
                  r"bijvoorbeeld eerst splitsen en dan substitueren. Bij een moeilijkere integraal "
                  r"heb je er vaak meerdere na elkaar nodig."),
            ("p", r"<strong>Controleer het resultaat van een onbepaalde integraal door je antwoord "
                  r"af te leiden en met de integrand te vergelijken.</strong> Dat is een echte "
                  r"controle, want afleiden is eenduidig; opnieuw rekenen herhaalt vaak dezelfde "
                  r"fout."),
        ]),
    ],
    onthoud=[
        r"Een primitieve \(F\) van \(f\) is een functie met \(F'(x) = f(x)\).",
        r"Bij een onbepaalde integraal schrijf je altijd \(+\,C\), bij een bepaalde integraal niet.",
        r"\(\int x^{n}\,dx = \dfrac{x^{\,n+1}}{n+1} + C\), behalve voor \(n = -1\).",
        r"\(\int \dfrac{1}{x}\,dx = \ln|x| + C\) en \(\int \sin x\,dx = -\cos x + C\).",
        r"Een constante factor mag voor het integraalteken, een factor met een \(x\) erin niet.",
        r"Bij substitutie kies je een binnenste functie waarvan de afgeleide ook in de integrand staat.",
        r"\(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\); vergeet het minteken niet.",
        r"Controleer een onbepaalde integraal door je antwoord af te leiden.",
    ],
)

# ───────────────────────── 12. De bepaalde integraal en haar toepassingen
BUNDELS["de-bepaalde-integraal-en-haar-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De bepaalde integraal en haar toepassingen",
    onder="Van Riemannsommen naar de hoofdstelling, en wat je met een integraal allemaal berekent.",
    secties=[
        dict(kop="Riemannsommen", blokken=[
            ("p", r"<strong>Een Riemannsom is de som van de oppervlakten van rechthoekjes onder "
                  r"een grafiek</strong>, dus \(\sum f(x_{i})\,\Delta x\). Je verdeelt \([a,\ b]\) "
                  r"in smalle stukjes en benadert elk stukje door een rechthoekje. <strong>De "
                  r"\(dx\) in een integraal komt overeen met de breedte van die "
                  r"rechthoekjes</strong>; \(f(x)\) is de hoogte."),
            ("fig", svg.riemannsom(),
             "Zes rechthoekjes onder dezelfde kromme, een keer te laag en een keer te hoog."),
        ]),
        dict(kop="Onder, boven en ertussen", blokken=[
            ("p", r"<strong>De ondersom is het kleinst en de bovensom het grootst</strong>: de "
                  r"ondersom gebruikt in elk stukje de laagste functiewaarde, de bovensom de "
                  r"hoogste, en de echte oppervlakte ligt ertussen. <strong>Een ondersom is dus "
                  r"nooit groter dan de werkelijke oppervlakte.</strong> <strong>Hoe meer "
                  r"deelintervallen je gebruikt, hoe beter de benadering</strong>, want de "
                  r"rechthoekjes volgen de kromme dan nauwer."),
            ("p", r"<strong>De limiet van Riemannsommen levert een exacte oppervlakte op omdat "
                  r"onder- en bovensom naar hetzelfde getal kruipen.</strong> De werkelijke "
                  r"oppervlakte ligt er altijd tussen, dus als de twee samenvallen is er maar één "
                  r"getal mogelijk. Dat getal is \(\int_{a}^{b} f(x)\,dx\)."),
        ]),
        dict(kop="De georiënteerde oppervlakte", blokken=[
            ("p", r"<strong>De georiënteerde oppervlakte is een oppervlakte die onder de x-as "
                  r"negatief meetelt.</strong> Dat is wat de bepaalde integraal rechtstreeks "
                  r"berekent. Ligt \(f\) op heel \([a,\ b]\) onder de x-as, dan is "
                  r"<strong>\(\int_{a}^{b} f(x)\,dx < 0\)</strong>."),
            ("fig", svg.georienteerd(),
             r"\(\int_{0}^{2\pi} \sin x\,dx\): het bovenste stuk telt positief, het onderste negatief."),
            ("p", r"<strong>Een bepaalde integraal is dus niet altijd positief</strong>, en ze kan "
                  r"zelfs nul worden als de stukken elkaar opheffen. <strong>Een werkelijke "
                  r"oppervlakte kan nooit negatief zijn</strong>; alleen de georiënteerde."),
            ("p", r"<strong>Snijdt de grafiek de x-as midden in het interval, dan splits je in de "
                  r"nulwaarde en tel je de stukken positief op.</strong> Anders heffen een positief "
                  r"en een negatief stuk elkaar op en krijg je een te kleine of zelfs een "
                  r"nul-uitkomst."),
        ]),
        dict(kop="Twee eigenschappen van de grenzen", blokken=[
            ("kader", r"\(\int_{a}^{a} f(x)\,dx = 0\): onder- en bovengrens vallen samen.<br>"
                      r"\(\int_{b}^{a} f(x)\,dx = -\int_{a}^{b} f(x)\,dx\): de grenzen verwisselen "
                      r"wisselt het teken."),
            ("p", r"<strong>De bovengrens \(b\) is de rechterkant van het interval waarover je "
                  r"integreert</strong>; de grenzen staan op de x-as, niet op de y-as. Dat "
                  r"verwarren leidt tot heel vreemde uitkomsten."),
        ]),
        dict(kop="De hoofdstelling", blokken=[
            ("p", r"<strong>Het gevolg van de hoofdstelling van de integraalrekening zegt: "
                  r"\(\int_{a}^{b} f(x)\,dx = F(b) - F(a)\).</strong> Daarmee hoef je geen "
                  r"rechthoekjes meer te tellen; een primitieve \(F\) zoeken volstaat. <strong>Dat "
                  r"invullen en aftrekken noteer je kort als \(\left[F(x)\right]_{a}^{b}\)</strong>, "
                  r"zodat je eerst de primitieve opschrijft en pas daarna invult."),
            ("p", r"<strong>De hoofdstelling geldt voor continue functies</strong>, niet voor elke "
                  r"functie: bij een sprong moet je het interval eerst opsplitsen."),
            ("p", r"<strong>De middelwaardestelling van de integraalrekening</strong> zegt dat er "
                  r"een \(c\) bestaat met "
                  r"<strong>\(f(c) = \dfrac{1}{b-a}\displaystyle\int_{a}^{b} f(x)\,dx\)</strong>, "
                  r"dus een punt waar de functiewaarde gelijk is aan de gemiddelde waarde. Er "
                  r"bestaat dan een rechthoek met dezelfde breedte en dezelfde oppervlakte als het "
                  r"gebied onder de kromme."),
        ]),
        dict(kop="Vier om na te rekenen", blokken=[
            ("p", tabel(["Integraal", "Uitkomst", "Hoe"], [
                [r"\(\int_{0}^{3} 2\,dx\)", r"\(6\)", r"een rechthoek van \(3\) breed en \(2\) hoog"],
                [r"\(\int_{0}^{2} 3x^{2}\,dx\)", r"\(8\)", r"de primitieve is \(x^{3}\)"],
                [r"\(\int_{1}^{2} \dfrac{1}{x^{2}}\,dx\)", r"\(\tfrac{1}{2}\)",
                 r"de primitieve is \(-\dfrac{1}{x}\)"],
                [r"\(\int_{0}^{1} \left(x - x^{2}\right)dx\)", r"\(\tfrac{1}{6}\)",
                 r"\(\tfrac{1}{2} - \tfrac{1}{3}\)"],
            ])),
        ]),
        dict(kop="Oppervlakte tussen twee krommen", blokken=[
            ("p", r"<strong>De oppervlakte tussen twee krommen is "
                  r"\(\int_{a}^{b} \left(\text{boven} - \text{onder}\right)dx\).</strong> Het "
                  r"hoogteverschil is de hoogte van elk reepje. Als <strong>grenzen neem je "
                  r"meestal de x-waarden van hun snijpunten</strong>; die vind je door "
                  r"\(f(x) = g(x)\) op te lossen."),
            ("fig", svg.tussenkrommen(),
             r"Het gebied tussen \(y = x\) en \(y = x^{2}\), met oppervlakte \(\tfrac{1}{6}\)."),
            ("p", r"<strong>Kruisen twee krommen elkaar midden in het interval, dan splits je in "
                  r"het snijpunt</strong>, want daar wisselen boven en onder van rol. <strong>Maak "
                  r"eerst een schets om te zien welke kromme boven ligt en waar ze elkaar "
                  r"snijden</strong>; zonder schets zet je de twee functies gemakkelijk in de "
                  r"verkeerde volgorde."),
            ("p", r"Nog twee: de oppervlakte onder \(y = 2\) tussen \(x = 0\) en \(x = 5\) is "
                  r"<strong>\(10\)</strong>. Lopen twee grafieken evenwijdig met de ene overal "
                  r"\(3\) hoger, dan is de oppervlakte over een interval van lengte \(4\) gelijk "
                  r"aan <strong>\(12\)</strong>."),
        ]),
        dict(kop="Omwentelingslichaam en booglengte", blokken=[
            ("p", r"<strong>Bij een omwentelingslichaam om de x-as is "
                  r"\(V = \pi \displaystyle\int_{a}^{b} f(x)^{2}\,dx\).</strong> <strong>Je "
                  r"kwadrateert de functie dus onder het integraalteken</strong>, tot de tweede "
                  r"macht: elke dunne schijf "
                  r"is een cirkel met straal \(f(x)\), en de oppervlakte van een cirkel is "
                  r"\(\pi r^{2}\). <strong>De inhoud hangt af van de as waarrond je de kromme laat "
                  r"draaien</strong>: rond de x-as of rond de y-as geeft een heel ander lichaam."),
            ("p", r"<strong>De booglengte is "
                  r"\(L = \displaystyle\int_{a}^{b} \sqrt{1 + f'(x)^{2}}\,dx\)</strong>: onder de "
                  r"wortel staat <strong>één plus de afgeleide in het kwadraat</strong>. Ze volgt "
                  r"uit Pythagoras op een heel klein stukje kromme, met een horizontale \(dx\) en "
                  r"een verticale \(dy\)."),
        ]),
        dict(kop="Integralen met een betekenis", blokken=[
            ("p", tabel(["Wat je integreert", "Wat je krijgt", "Let op"], [
                ["de snelheid over de tijd", "de verplaatsing",
                 "niet de afgelegde weg, want achteruit telt negatief"],
                ["de versnelling over de tijd", "de verandering van de snelheid",
                 "één stap terug in dezelfde ketting"],
                ["het debiet van een kraan over de tijd", "de totale hoeveelheid water",
                 "liter per seconde maal seconden geeft liter"],
                ["de marginale kost over een aantal stuks", "de toename van de totale kost",
                 "de marginale kost is de afgeleide van de totale"],
            ])),
            ("p", r"Integreer je de snelheid van een wagen over een tijdsinterval, dan krijg je "
                  r"de verplaatsing. <strong>En de eenheid rekent mee</strong>: een snelheid in "
                  r"\(\text{m/s}\) maal seconden geeft \(\text{m}\), want "
                  r"\(\text{m/s} \cdot \text{s} = \text{m}\). Die controle vangt veel fouten."),
            ("kader", r"<strong>Op het examen gebruik je ICT bij een integraal als de opgave dat met het icoon "
                      r"aangeeft, en ook dan toon je je werkwijze.</strong> Functioneel gebruik "
                      r"betekent dat ICT het rekenwerk ondersteunt, terwijl je redenering en je "
                      r"tussenstappen op papier staan."),
        ]),
    ],
    onthoud=[
        r"Een Riemannsom is \(\sum f(x_{i})\,\Delta x\): rechthoekjes onder een grafiek.",
        r"De ondersom is het kleinst en de bovensom het grootst; de echte oppervlakte ligt ertussen.",
        r"De bepaalde integraal geeft de georiënteerde oppervlakte: onder de x-as telt ze negatief mee.",
        r"\(\int_{b}^{a} f(x)\,dx = -\int_{a}^{b} f(x)\,dx\) en \(\int_{a}^{a} f(x)\,dx = 0\).",
        r"\(\int_{a}^{b} f(x)\,dx = \left[F(x)\right]_{a}^{b} = F(b) - F(a)\).",
        r"Oppervlakte tussen twee krommen: \(\int_{a}^{b}\left(\text{boven} - \text{onder}\right)dx\).",
        r"Omwentelingslichaam: \(V = \pi \int_{a}^{b} f(x)^{2}dx\). Booglengte: \(L = \int_{a}^{b} \sqrt{1 + f'(x)^{2}}\,dx\).",
        r"De integraal van de snelheid over de tijd is de verplaatsing, niet de afgelegde weg.",
    ],
)

# ───────────────────────── 13. Complexe getallen
BUNDELS["complexe-getallen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Complexe getallen",
    onder="De imaginaire eenheid, het vlak van Gauss, de goniometrische vorm en de formule van de Moivre.",
    secties=[
        dict(kop="De imaginaire eenheid", blokken=[
            ("p", "<strong>De imaginaire eenheid i is het getal waarvan het kwadraat min één is.</strong> "
                  "<strong>De complexe getallen werden ingevoerd omdat niet elke vergelijking een oplossing "
                  "had in de reële getallen</strong>: een getal met kwadraat min één bestond niet, en door "
                  "het toe te voegen kreeg elke veeltermvergelijking oplossingen."),
            ("p", "De machten van i <strong>herhalen zich om de vier</strong>: i, dan min één, dan "
                  "<strong>min i</strong>, dan <strong>één</strong>. <strong>i tot de derde is dus niet i "
                  "maar min i</strong>, en <strong>i tot de vierde is één</strong>. Pas i tot de vijfde is "
                  "weer i."),
            ("p", "Een complex getal schrijf je in <strong>cartesische vorm</strong> als een reëel deel "
                  "plus een imaginair deel maal i. Bij <strong>drie min vijf i</strong> is het "
                  "<strong>reëel deel drie</strong>; bij <strong>zeven min twee i</strong> is het "
                  "<strong>imaginair deel min twee</strong>, dus zonder de i erbij. <strong>Elk reëel getal "
                  "is ook een complex getal</strong>, met imaginair deel nul. <strong>Een zuiver imaginair "
                  "getal heeft reëel deel nul.</strong>"),
            ("kader", "<strong>Je kan twee complexe getallen niet van klein naar groot ordenen.</strong> "
                      "Hun moduli kan je wel vergelijken, maar de getallen zelf niet."),
        ]),
        dict(kop="Rekenen in cartesische vorm", blokken=[
            ("p", "<strong>Optellen doe je deel per deel</strong>: twee plus drie i, plus één min i, geeft "
                  "<strong>drie plus twee i</strong>, net als bij vectoren. Bij vermenigvuldigen werk je "
                  "uit en gebruik je dat i in het kwadraat min één is: <strong>één plus i, in het kwadraat, "
                  "is twee i</strong>."),
            ("p", "Het <strong>toegevoegde complexe getal</strong> krijg je door enkel het imaginair deel "
                  "van teken te laten wisselen: dat van <strong>twee plus drie i is twee min drie i</strong>. "
                  "<strong>Een complex getal maal zijn toegevoegde is altijd een reëel getal</strong>, "
                  "namelijk het kwadraat van de modulus. Daarom <strong>deel je door een complex getal door "
                  "teller en noemer met de toegevoegde van de noemer te vermenigvuldigen</strong>: de noemer "
                  "wordt dan reëel. Apart delen werkt niet, net zoals bij een breuk met een wortel."),
        ]),
        dict(kop="Het vlak van Gauss", blokken=[
            ("p", "Elk complex getal is een <strong>punt in het vlak van Gauss</strong>: horizontaal het "
                  "reëel deel, en <strong>op de verticale as het imaginair deel</strong>. De reële getallen "
                  "liggen dus op de horizontale as, de zuiver imaginaire op de verticale."),
            ("p", "De <strong>modulus</strong> is de afstand tot de oorsprong. Die van <strong>drie plus "
                  "vier i is vijf</strong> (de wortel uit negen plus zestien), die van <strong>vijf i is "
                  "vijf</strong>, en die van <strong>min drie is drie</strong>: een modulus is nooit "
                  "negatief, en voor een reëel getal is ze de absolute waarde. Het "
                  "<strong>argument</strong> is <strong>de hoek met de positieve reële as</strong>. Samen "
                  "leggen modulus en argument het getal volledig vast. Het argument van <strong>i is "
                  "negentig graden</strong>, dat van een <strong>negatief reëel getal honderdtachtig "
                  "graden</strong>."),
            ("p", "Daarmee krijgen de bewerkingen een meetkundige betekenis. <strong>Optellen is dezelfde "
                  "constructie als het optellen van twee vectoren</strong>: je legt de pijlen achter "
                  "elkaar. <strong>Het toegevoegde nemen spiegelt het punt om de horizontale as.</strong> "
                  "En <strong>vermenigvuldigen met i draait het punt een kwart slag rond de "
                  "oorsprong</strong>, want de modulus van i is één en haar argument negentig graden."),
        ]),
        dict(kop="De goniometrische vorm", blokken=[
            ("p", "<strong>De goniometrische vorm is de modulus maal de cosinus van het argument plus i "
                  "maal de sinus ervan.</strong> Zo zie je de twee gegevens meteen staan: hoe ver en onder "
                  "welke hoek. <strong>Van cartesisch naar goniometrisch bereken je de modulus en het "
                  "argument uit het reëel en imaginair deel</strong>: de modulus is de wortel uit de som "
                  "van de kwadraten, en het argument vind je met de tangens, met het juiste kwadrant erbij."),
            ("p", tabel(["Bewerking", "Met de moduli", "Met de argumenten"], [
                ["vermenigvuldigen", "vermenigvuldigen", "optellen"],
                ["delen", "delen", "aftrekken"],
                ["tot de macht n verheffen", "tot de macht n verheffen", "met n vermenigvuldigen"],
            ])),
            ("p", "Vermenigvuldigen is dus <strong>uitrekken en draaien tegelijk</strong>, delen is krimpen "
                  "en terugdraaien. <strong>De modulus van een product is het product van de moduli, niet "
                  "hun som</strong>; het zijn de argumenten die worden opgeteld. De regel voor machten "
                  "heet de <strong>formule van de Moivre</strong>: <strong>je verheft de modulus tot de "
                  "macht n en vermenigvuldigt het argument met n</strong>. Ze volgt rechtstreeks uit de "
                  "regel voor vermenigvuldigen, n keer toegepast. <strong>Daarom is de goniometrische vorm "
                  "zo handig bij machtsverheffen</strong>: probeer één plus i tot de tiende maar eens in "
                  "cartesische vorm."),
        ]),
        dict(kop="Vergelijkingen in de complexe getallen", blokken=[
            ("p", "<strong>Een tweedegraadsvergelijking met een negatieve discriminant heeft wel degelijk "
                  "oplossingen in de complexe getallen</strong>, namelijk twee. In de reële getallen zijn "
                  "er inderdaad geen. Zo heeft <strong>x kwadraat plus één is nul</strong> als oplossingen "
                  "<strong>i</strong> en min i, en <strong>x kwadraat min twee x plus vijf is nul</strong> "
                  "de oplossingen <strong>één plus twee i en één min twee i</strong>: de discriminant is "
                  "min zestien, de wortel daaruit is vier i."),
            ("p", "<strong>De twee complexe oplossingen van een tweedegraadsvergelijking met reële "
                  "coëfficiënten zijn elkaars toegevoegde</strong>: ze verschillen alleen in het teken voor "
                  "de wortel uit de discriminant."),
            ("p", "<strong>De vergelijking z tot de derde is acht heeft drie oplossingen</strong> in de "
                  "complexe getallen; algemeen heeft <strong>z tot de macht n is a er precies n</strong>, "
                  "en <strong>een complex getal dat niet nul is heeft precies n n-de machtswortels</strong>. "
                  "<strong>Die n oplossingen liggen op één cirkel, gelijkmatig over de omtrek "
                  "verdeeld</strong>: ze hebben dezelfde modulus en hun argumenten verschillen telkens "
                  "evenveel, dus ze vormen de hoekpunten van een regelmatige veelhoek."),
            ("weetje", "<strong>Een veelterm van graad n heeft in de complexe getallen precies n "
                       "nulwaarden</strong>, als je ze met hun multipliciteit telt. Dat is de hoofdstelling "
                       "van de algebra. In de reële getallen kunnen het er minder zijn."),
        ]),
    ],
    onthoud=[
        "De imaginaire eenheid i is het getal waarvan het kwadraat min één is.",
        "De machten van i herhalen zich om de vier: i, min één, min i, één.",
        "Bij zeven min twee i is het imaginair deel min twee, zonder de i erbij.",
        "Het toegevoegde van twee plus drie i is twee min drie i.",
        "Delen doe je door teller en noemer met de toegevoegde van de noemer te vermenigvuldigen.",
        "De modulus is de afstand tot de oorsprong, het argument de hoek met de positieve reële as.",
        "Bij vermenigvuldigen vermenigvuldig je de moduli en tel je de argumenten op.",
        "Formule van de Moivre: verhef de modulus tot de macht n en vermenigvuldig het argument met n.",
        "z tot de macht n is a heeft precies n oplossingen, gelijkmatig verdeeld op één cirkel.",
    ],
)

# ───────────────────────── 14. Telproblemen en het binomium
BUNDELS["telproblemen-en-het-binomium-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Telproblemen en het binomium",
    onder="Faculteit, permutaties, variaties en combinaties, de driehoek van Pascal en het binomium van Newton.",
    secties=[
        dict(kop="Faculteit en permutaties", blokken=[
            ("p", "<strong>n faculteit is het product van alle natuurlijke getallen van één tot en met "
                  "n.</strong> <strong>Vijf faculteit is dus honderdtwintig</strong>. <strong>Nul "
                  "faculteit is één</strong>: dat is een afspraak die alle formules kloppend houdt, want "
                  "er is precies één manier om niets te rangschikken."),
            ("p", "Een <strong>permutatie</strong> is een rangschikking van álle elementen. <strong>Vijf "
                  "verschillende boeken naast elkaar zetten kan op honderdtwintig manieren</strong>, dus "
                  "op vijf faculteit manieren."),
            ("p", "Een <strong>herhalingspermutatie is een rangschikking van alle elementen waarvan er "
                  "enkele gelijk zijn</strong>. Je deelt dan door de faculteiten van de groepjes gelijke "
                  "elementen: met de letters van <strong>MAMA</strong> maak je <strong>zes</strong> "
                  "verschillende woorden, want vier faculteit gedeeld door twee faculteit maal twee "
                  "faculteit."),
        ]),
        dict(kop="Variaties en combinaties", blokken=[
            ("p", tabel(["Soort", "Telt de volgorde mee?", "Voorbeeld"], [
                ["variatie", "ja", "goud, zilver en brons op een podium"],
                ["combinatie", "nee", "drie leden van een jury kiezen uit twaalf"],
                ["herhalingsvariatie", "ja, en herhaling is toegelaten", "een code van vier cijfers"],
            ])),
            ("p", "<strong>Bij een variatie telt de volgorde mee en bij een combinatie niet.</strong> "
                  "Daarom zijn er <strong>altijd minder combinaties dan variaties</strong> bij dezelfde n "
                  "en p: bij een combinatie vallen alle volgordes van dezelfde keuze samen. <strong>Bij "
                  "een herhalingsvariatie mag een element wel meer dan één keer voorkomen</strong>; bij "
                  "een gewone variatie niet. Zo bestaan er <strong>tienduizend codes van vier "
                  "cijfers</strong> als elk cijfer van nul tot negen mag en herhaling toegelaten is."),
            ("p", "Drie uitkomsten om bij de hand te hebben. <strong>Twee personen kiezen uit vijf zonder "
                  "volgorde kan op tien manieren</strong>. <strong>Zes mensen die elkaar allemaal één keer "
                  "een hand geven, geven vijftien handdrukken</strong>. En <strong>één persoon kiezen uit "
                  "tien kan op tien manieren</strong>. <strong>Een jury van drie uit twaalf kandidaten is "
                  "een combinatie</strong>, want de volgorde van de drie telt niet mee; zou je een "
                  "voorzitter, een secretaris en een penningmeester kiezen, dan was het een variatie."),
            ("p", "<strong>Het aantal manieren om p uit n te kiezen is even groot als het aantal manieren "
                  "om n min p uit n te kiezen</strong>: wie je kiest, bepaalt meteen wie je niet kiest."),
        ]),
        dict(kop="De drie telregels", blokken=[
            ("p", "<strong>De somregel gebruik je als je moet kiezen tussen twee mogelijkheden die elkaar "
                  "uitsluiten.</strong> <strong>De productregel gebruik je bij keuzes die na elkaar "
                  "komen</strong>: eerst een hoofdgerecht en daarna een dessert. <strong>Of-of betekent "
                  "optellen, en-en betekent vermenigvuldigen</strong>, en dat onderscheid is de kern van "
                  "elk telprobleem."),
            ("p", "<strong>De complementregel zegt: tel het aantal gevallen dat niet voldoet en trek dat "
                  "van het totaal af.</strong> Bij een opgave met de woorden minstens of hoogstens is dat "
                  "vaak veel korter werk."),
            ("weetje", "<strong>Het sommatieteken dient om een lange som kort te schrijven met een lopende "
                       "index.</strong> Onder het teken staat waar de index begint, erboven waar hij "
                       "eindigt."),
        ]),
        dict(kop="De driehoek van Pascal", blokken=[
            ("p", "<strong>In de driehoek van Pascal staan de binomiaalcoëfficiënten, rij per rij.</strong> "
                  "<strong>Je berekent een getal als de som van de twee getallen schuin erboven</strong>, "
                  "en dat is net wat <strong>de formule van Stifel-Pascal</strong> in symbolen zegt: "
                  "<strong>één binomiaalcoëfficiënt als de som van twee andere uit de vorige rij</strong>. "
                  "Daarmee bouw je de hele driehoek op zonder één faculteit te berekenen."),
            ("p", "<strong>Aan het begin en op het einde van elke rij staat een één</strong>: er is maar "
                  "één manier om niets te kiezen en maar één manier om alles te kiezen. <strong>Nul "
                  "elementen kiezen uit n kan dus op één manier.</strong> <strong>Elke rij is "
                  "symmetrisch, omdat p elementen kiezen hetzelfde is als n min p elementen "
                  "weglaten.</strong> <strong>De som van alle getallen in een rij is een macht van "
                  "twee</strong>: rij n telt op tot twee tot de macht n, en dat is ook het aantal "
                  "deelverzamelingen van een verzameling met n elementen. Zo is de <strong>som van de rij "
                  "één, drie, drie, één gelijk aan acht</strong>."),
            ("p", "Twee aantallen die je rechtstreeks uit de driehoek haalt: <strong>twee elementen kiezen "
                  "uit vier kan op zes manieren</strong>, het middelste getal van de rij één, vier, zes, "
                  "vier, één."),
            ("kader", "<strong>De driehoek van Pascal heeft wel degelijk met kansrekening te maken.</strong> "
                      "De binomiale verdeling gebruikt net die coëfficiënten: ze tellen op hoeveel manieren "
                      "k successen in n pogingen kunnen vallen."),
        ]),
        dict(kop="Het binomium van Newton", blokken=[
            ("p", "<strong>Het binomium van Newton geeft de uitwerking van een tweeterm tot een "
                  "willekeurige macht.</strong> Elke term bestaat uit een binomiaalcoëfficiënt maal een "
                  "macht van a maal een macht van b. <strong>Het heet zo omdat het over een macht van een "
                  "tweeterm gaat</strong>, en een binomium is een som van twee termen."),
            ("p", "<strong>a plus b, tot de derde macht, is a tot de derde, plus drie a kwadraat b, plus "
                  "drie a b kwadraat, plus b tot de derde.</strong> De coëfficiënten één, drie, drie, één "
                  "zijn de vierde rij van de driehoek. <strong>De coëfficiënt bij a kwadraat b is dus "
                  "drie</strong>: je kiest uit de drie factoren er één waaruit je b neemt. <strong>a plus "
                  "b, tot de vijfde macht, heeft zes termen</strong>, altijd één meer dan de exponent. En "
                  "in <strong>één plus x, tot de vierde macht, heeft x kwadraat coëfficiënt zes</strong>."),
            ("p", "<strong>Bij a min b tot de macht n wisselen de tekens van term tot term</strong>, want "
                  "je past dezelfde formule toe met min b in plaats van b. En de bekendste valstrik: "
                  "<strong>a plus b in het kwadraat is niet a kwadraat plus b kwadraat</strong>, want de "
                  "middelste term twee ab ontbreekt; de tweede rij van Pascal is één, twee, één."),
            ("p", "<strong>Eén bepaalde term vind je zonder alles uit te werken met de algemene term uit "
                  "het binomium van Newton</strong>: je vult de juiste index in en krijgt meteen de "
                  "coëfficiënt en de twee machten."),
            ("kader", "<strong>Een identiteit met binomiaalcoëfficiënten bewijs je door beide leden met "
                      "faculteiten uit te schrijven en te vereenvoudigen.</strong> Een paar getallen "
                      "invullen toont alleen dat het dáár klopt. Een telkundige redenering mag ook, als ze "
                      "voor alle n geldt."),
        ]),
    ],
    onthoud=[
        "n faculteit is het product van alle natuurlijke getallen van één tot en met n; nul faculteit is één.",
        "Een permutatie is een rangschikking van alle elementen: vijf boeken kan op honderdtwintig manieren.",
        "Bij een variatie telt de volgorde mee, bij een combinatie niet.",
        "Bij een herhalingsvariatie mag een element meer dan één keer voorkomen.",
        "Of-of betekent optellen, en-en betekent vermenigvuldigen.",
        "Complementregel: tel de gevallen die niet voldoen en trek dat van het totaal af.",
        "In de driehoek van Pascal is elk getal de som van de twee getallen schuin erboven.",
        "De som van rij n van de driehoek van Pascal is twee tot de macht n.",
        "a plus b in het kwadraat is niet a kwadraat plus b kwadraat: de middelste term twee ab ontbreekt.",
    ],
)

# ───────────────────────── 15. Kansrekenen en kansverdelingen
BUNDELS["kansrekenen-en-kansverdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansrekenen en kansverdelingen",
    onder="Laplace, kansbomen en kruistabellen, voorwaardelijke kans, en de binomiale verdeling.",
    secties=[
        dict(kop="Wat een kans is", blokken=[
            ("p", "<strong>De wet van Laplace zegt: de kans is het aantal gunstige gedeeld door het aantal "
                  "mogelijke uitkomsten.</strong> Ze geldt alleen als alle uitkomsten even waarschijnlijk "
                  "zijn, dus bij een eerlijke dobbelsteen of munt."),
            ("p", tabel(["Vraag", "Kans", "Hoe"], [
                ["een even getal met een dobbelsteen", "een half", "drie gunstige van de zes"],
                ["een zes met een dobbelsteen", "een zesde", "één gunstige van de zes"],
                ["een getal kleiner dan drie", "een derde", "één en twee, dus twee van de zes"],
                ["harten uit een spel van tweeënvijftig kaarten", "een vierde", "dertien harten op tweeënvijftig"],
            ])),
            ("p", "<strong>Een kans kan nooit groter zijn dan één</strong>: ze ligt altijd tussen nul en "
                  "één. Krijg je meer dan één, dan zit er een fout in je redenering. <strong>De som van de "
                  "kansen op alle mogelijke uitkomsten samen is één</strong>, want er gebeurt altijd iets. "
                  "<strong>Een kans gelijk aan nul betekent dat de gebeurtenis bij dit experiment niet kan "
                  "voorkomen</strong>, zoals een zeven gooien met een gewone dobbelsteen."),
            ("p", "De <strong>uitkomstenverzameling is de verzameling van alle mogelijke uitkomsten</strong>: "
                  "bij één worp met een dobbelsteen de getallen één tot en met zes. Het verschil met een "
                  "gebeurtenis: <strong>een gebeurtenis kan uit meerdere uitkomsten bestaan</strong>, zoals "
                  "een even getal gooien."),
            ("weetje", "<strong>Bij heel veel herhalingen komt de relatieve frequentie dicht bij de kans te "
                       "liggen.</strong> Dat is net wat een kans in de praktijk betekent. Bij tien worpen "
                       "kan het nog ver uit elkaar liggen."),
        ]),
        dict(kop="Kansbomen, kruistabellen en voorwaardelijke kans", blokken=[
            ("p", "<strong>In een kansboom vermenigvuldig je de kansen op de takken van één pad.</strong> "
                  "<strong>Verschillende paden die allemaal voldoen, tel je daarna op.</strong> Na elkaar "
                  "betekent dus vermenigvuldigen, of-of betekent optellen, op voorwaarde dat de gevallen "
                  "elkaar uitsluiten. Zo is de <strong>kans op twee keer kop bij twee worpen met een munt "
                  "een vierde</strong>: een half maal een half."),
            ("p", "<strong>In een kruistabel zet je de aantallen voor elke combinatie van twee "
                  "kenmerken.</strong> De randtotalen geven je de gewone kansen, de cellen de kansen op "
                  "beide kenmerken samen."),
            ("p", "<strong>Een voorwaardelijke kans is de kans op A als je al weet dat B gebeurd is.</strong> "
                  "Je kijkt dan alleen nog naar de gevallen waarin B optreedt, dus naar één rij of één "
                  "kolom van de kruistabel."),
            ("p", "<strong>Twee gebeurtenissen zijn onafhankelijk als de ene de kans op de andere niet "
                  "verandert</strong>; dan is de kans op allebei samen gewoon het product. <strong>Twee "
                  "keer een kaart trekken zonder terugleggen is niet onafhankelijk</strong>, want de eerste "
                  "kaart verandert wat er nog in het spel zit. Mét terugleggen wel."),
            ("p", "<strong>De complementregel voor kansen zegt: de kans dat iets niet gebeurt is één min "
                  "de kans dat het wel gebeurt.</strong> Is de kans op een gebeurtenis nul komma drie, dan "
                  "is de kans dat ze niet gebeurt <strong>nul komma zeven</strong>. Daarom bereken je "
                  "<strong>de kans op minstens één succes als één min de kans op nul successen</strong>."),
        ]),
        dict(kop="Kansvariabelen", blokken=[
            ("p", "<strong>Een kansvariabele is een grootheid die aan elke uitkomst een getal "
                  "toekent.</strong> Bij tien worpen met een munt kan dat het aantal keer kop zijn."),
            ("p", "<strong>Een discrete kansvariabele neemt losse waarden aan, een continue elke waarde in "
                  "een interval.</strong> Het aantal defecte stukken is discreet; <strong>de tijd die een "
                  "trein te laat is, is continu</strong>, want tijd kan elke waarde in een interval "
                  "aannemen. <strong>De som van alle kansen in een kansverdeling is één.</strong>"),
            ("p", "<strong>De verwachtingswaarde is het gemiddelde dat je op lange termijn zou "
                  "meten.</strong> Bij één enkel experiment zegt ze niets met zekerheid. <strong>Ze hoeft "
                  "zelf geen mogelijke uitkomst te zijn</strong>: het gemiddelde aantal kinderen per gezin "
                  "is één komma zeven, en zoveel kinderen heeft geen enkel gezin."),
        ]),
        dict(kop="De binomiale verdeling", blokken=[
            ("p", "<strong>Een Bernoulli-experiment heeft precies twee mogelijke uitkomsten</strong>, "
                  "succes of mislukking, en bestaat uit <strong>één</strong> poging. Herhaal je het, dan "
                  "krijg je een binomiale verdeling."),
            ("p", "<strong>Een kansvariabele is binomiaal verdeeld bij een vast aantal onafhankelijke "
                  "pogingen met telkens dezelfde slaagkans.</strong> Drie voorwaarden dus; valt er één weg, "
                  "dan is de verdeling niet binomiaal. <strong>De slaagkans mag dus niet van poging tot "
                  "poging verschillen</strong>, en daarom voldoet een trekking zonder terugleggen uit een "
                  "kleine groep vaak niet. <strong>Het aantal zessen in vijftig worpen met een dobbelsteen "
                  "is wel binomiaal verdeeld.</strong>"),
            ("p", "<strong>In de formule voor de kans op precies k successen uit n pogingen staat een "
                  "binomiaalcoëfficiënt maal p tot de k maal één min p tot de n min k.</strong> Die "
                  "coëfficiënt telt op hoeveel verschillende volgordes die k successen kunnen hebben."),
            ("p", tabel(["Grootheid", "Formule", "Voorbeeld"], [
                ["verwachtingswaarde", "het aantal pogingen maal de kans per poging", "tien worpen met een munt: vijf keer kop"],
                ["verwachtingswaarde", "zelfde formule", "twintig stukken met kans nul komma één: twee foute stukken"],
                ["standaardafwijking", "de wortel uit n maal p maal één min p", "onder de wortel staat de variantie"],
            ])),
            ("p", "<strong>Een grotere standaardafwijking betekent dat de uitkomsten verder uit elkaar "
                  "liggen</strong>; ze meet hoe sterk de waarden rond de verwachtingswaarde schommelen. "
                  "Hebben <strong>twee binomiale verdelingen dezelfde verwachtingswaarde maar een "
                  "verschillende standaardafwijking</strong>, dan <strong>liggen de uitkomsten bij de ene "
                  "meer verspreid dan bij de andere</strong>: gemiddeld hetzelfde resultaat, maar bij de "
                  "ene schommelt het sterker."),
            ("kader", "<strong>Aan de rekenapp laat je de kansen, de verwachtingswaarde en de "
                      "standaardafwijking berekenen.</strong> Beoordelen of het model past en wat het "
                      "antwoord betekent, blijft jouw werk."),
        ]),
    ],
    onthoud=[
        "Laplace: de kans is het aantal gunstige gedeeld door het aantal mogelijke uitkomsten.",
        "Een kans ligt altijd tussen nul en één.",
        "In een kansboom vermenigvuldig je de kansen langs één pad en tel je verschillende paden op.",
        "Een voorwaardelijke kans is de kans op A als je al weet dat B gebeurd is.",
        "De kans op minstens één succes is één min de kans op nul successen.",
        "Een discrete kansvariabele neemt losse waarden aan, een continue elke waarde in een interval.",
        "De verwachtingswaarde is het gemiddelde op lange termijn en hoeft zelf geen mogelijke uitkomst te zijn.",
        "Binomiaal verdeeld: een vast aantal onafhankelijke pogingen met telkens dezelfde slaagkans.",
        "De binomiale verwachtingswaarde is het aantal pogingen maal de kans per poging.",
    ],
)

# ───────────────────────── 16. Statistiek: normale verdeling en hypothesetoets
BUNDELS["statistiek-normale-verdeling-en-hypothesetoets-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Statistiek: normale verdeling en hypothesetoets",
    onder="De Gausskromme en de z-score, steekproeven en vertekening, samenhang en causaliteit, en toetsen met een p-waarde.",
    secties=[
        dict(kop="De normale verdeling", blokken=[
            ("p", "<strong>De grafiek van een normale verdeling is klokvormig en symmetrisch rond het "
                  "gemiddelde</strong>; die kromme heet de <strong>Gausskromme</strong>. <strong>Het "
                  "gemiddelde bepaalt waar de top ligt</strong> en <strong>de standaardafwijking bepaalt "
                  "hoe breed de kromme is</strong>: klein geeft een smalle, hoge klok, groot een brede, "
                  "platte. Hebben <strong>twee Gausskrommen hetzelfde gemiddelde en is de ene "
                  "smaller</strong>, dan <strong>liggen bij die smalle de metingen dichter bij het "
                  "gemiddelde</strong>."),
            ("p", "<strong>De totale oppervlakte onder een Gausskromme is één</strong>, want alle kans "
                  "samen is één. <strong>Een kans komt dus overeen met de oppervlakte onder de "
                  "kromme</strong>; de hoogte alleen zegt niets. Daaruit volgt ook dat <strong>bij een "
                  "continue verdeling de kans op precies één welbepaalde waarde nul is</strong>: een "
                  "enkele waarde heeft geen breedte. En <strong>vijftig procent van de metingen ligt links "
                  "van het gemiddelde</strong>."),
            ("p", "<strong>De Gausskromme raakt de horizontale as niet.</strong> Ze nadert die wel, maar "
                  "bereikt haar nooit, dus elke waarde blijft in principe mogelijk. <strong>Of de normale "
                  "verdeling een geschikt model is, beoordeel je door te kijken of het histogram ongeveer "
                  "klokvormig is</strong>; je kan er ook de dichtheidsfunctie met de geschatte parameters "
                  "over tekenen. Is een histogram duidelijk scheef, dan past het model niet."),
        ]),
        dict(kop="De z-score", blokken=[
            ("p", "<strong>De z-score bereken je als het verschil met het gemiddelde, gedeeld door de "
                  "standaardafwijking.</strong> Ze meet dus <strong>hoeveel standaardafwijkingen je van "
                  "het gemiddelde af zit</strong>, en daardoor kan je metingen uit verschillende groepen "
                  "vergelijken. <strong>Een meting die precies gelijk is aan het gemiddelde heeft z-score "
                  "nul</strong>, en bij een <strong>gemiddelde van zeventig met standaardafwijking vijf "
                  "heeft een meting van tachtig z-score twee</strong>."),
            ("p", "<strong>Een z-score kan negatief zijn</strong>: dan ligt de meting onder het "
                  "gemiddelde. <strong>Een z-score van min anderhalf betekent dat de meting anderhalve "
                  "standaardafwijking onder het gemiddelde ligt</strong>; de z-score telt in "
                  "standaardafwijkingen, niet in de eenheid van de meting zelf."),
            ("p", "<strong>De standaardnormale verdeling heeft gemiddelde nul en standaardafwijking "
                  "één.</strong> Ze is de normale verdeling na omzetting naar z-scores, zodat één eenheid "
                  "op de as precies één standaardafwijking is."),
            ("p", tabel(["Binnen hoeveel standaardafwijkingen", "Ongeveer welk deel van de metingen"], [
                ["één", "achtenzestig procent"],
                ["twee", "vijfennegentig procent"],
                ["drie", "negenennegentig komma zeven procent"],
            ])),
            ("kader", "Let op de eerste rij: <strong>binnen één standaardafwijking ligt ongeveer "
                      "achtenzestig procent, niet vijfennegentig.</strong> Vijfennegentig procent hoort bij "
                      "twee standaardafwijkingen."),
        ]),
        dict(kop="Steekproeven", blokken=[
            ("p", "<strong>Het gemiddelde van een populatie is de echte waarde, dat van een steekproef een "
                  "schatting ervan.</strong> Daarom krijgen ze een ander symbool: je kent het "
                  "populatiegemiddelde meestal niet."),
            ("p", "<strong>Een steekproef is representatief als ze op de belangrijke kenmerken op de "
                  "populatie lijkt.</strong> Grootte alleen helpt niet: een heel grote maar scheve "
                  "steekproef blijft scheef. <strong>Randomisatie betekent iedereen uit de populatie "
                  "evenveel kans geven om gekozen te worden</strong>, en dat is de beste bescherming tegen "
                  "vertekening."),
            ("p", "<strong>Een steekproeffout komt door het toeval van de trekking, een niet-steekproeffout "
                  "door de opzet.</strong> Toeval kan je inschatten en kleiner maken: <strong>een grotere "
                  "aselecte steekproef geeft doorgaans een betrouwbaarder resultaat</strong>. Een fout in "
                  "de opzet blijft ook bij duizend deelnemers bestaan."),
            ("p", "Laat een krant haar lezers online stemmen over een stelling, dan heb je "
                  "<strong>vrijwillige respons</strong>: wie zich sterk betrokken voelt, stemt vaker. De "
                  "groep die antwoordt is dan niet toevallig samengesteld, en meer stemmen lost dat niet op."),
        ]),
        dict(kop="Samenhang is geen oorzaak", blokken=[
            ("p", "<strong>In een spreidingsdiagram lees je af of er een verband is tussen twee numerieke "
                  "grootheden.</strong> Elk punt is één waarneming met twee kenmerken. Een "
                  "<strong>trendlijn is een rechte of kromme die het patroon in de puntenwolk "
                  "samenvat</strong>; ze gaat meestal niet door de punten zelf."),
            ("p", "<strong>De correlatiecoëfficiënt ligt tussen min één en plus één.</strong> Het teken "
                  "geeft de richting, de grootte de sterkte van het lineaire verband. <strong>Dicht bij "
                  "nul betekent dus net dat er nauwelijks lineair verband is</strong>; sterk is ze dicht "
                  "bij min één of plus één."),
            ("kader", "<strong>Sterke samenhang betekent niet dat de ene de oorzaak van de andere is.</strong> "
                      "Het kan ook komen van een <strong>derde verborgen variabele</strong>, van omgekeerde "
                      "oorzaak en gevolg, of gewoon van toeval. In de zomer worden er meer ijsjes verkocht "
                      "en gebeuren er meer verdrinkingen: de verborgen variabele is <strong>het warme "
                      "weer</strong>, dat allebei de aantallen verhoogt."),
        ]),
        dict(kop="De hypothesetoets", blokken=[
            ("p", "<strong>De nulhypothese is niet wat je wil aantonen, maar wat je probeert te "
                  "verwerpen.</strong> Wat je wil aantonen, staat in de alternatieve hypothese."),
            ("p", "<strong>De p-waarde is de kans op zo'n resultaat of extremer, als de nulhypothese waar "
                  "is.</strong> Ze zegt niets over de kans dat de hypothese klopt, alleen hoe verrassend je "
                  "resultaat zou zijn mocht ze kloppen. Je vergelijkt ze met het "
                  "<strong>significantieniveau</strong> alfa, <strong>de kans die je vooraf aanvaardt om "
                  "de nulhypothese onterecht te verwerpen</strong>. Alfa gelijk aan nul komma nul vijf is "
                  "<strong>vijf procent</strong>; soms kiest men één procent als een vals alarm duur "
                  "uitvalt. <strong>Ligt de p-waarde onder alfa, dan verwerp je</strong>: bij een p-waarde "
                  "van nul komma nul twee en alfa nul komma nul vijf is het antwoord <strong>ja</strong>."),
            ("p", tabel(["Soort fout", "Wat er gebeurt", "Hoe je het noemt"], [
                ["type I", "de nulhypothese verwerpen terwijl ze waar is", "een vals alarm; de kans erop is alfa"],
                ["type II", "de nulhypothese onterecht niet verwerpen", "er was wel een effect, maar je vond het niet"],
            ])),
            ("p", "Een type II-fout gebeurt vaker bij een kleine steekproef. <strong>Een eenzijdige toets "
                  "gebruik je als je vooraf een richting verwacht</strong>, bijvoorbeeld een stijging; "
                  "vermoed je alleen dat er íéts verandert, dan toets je tweezijdig."),
            ("kader", "<strong>Verwerp je de nulhypothese niet, dan besluit je dat er onvoldoende bewijs "
                      "tegen gevonden is.</strong> Geen bewijs vinden is niet hetzelfde als bewijzen dat er "
                      "niets is: misschien was je steekproef gewoon te klein."),
        ]),
    ],
    onthoud=[
        "De Gausskromme is klokvormig en symmetrisch rond het gemiddelde.",
        "Het gemiddelde bepaalt waar de top ligt, de standaardafwijking hoe breed de kromme is.",
        "Een kans is de oppervlakte onder de kromme; de totale oppervlakte is één.",
        "De z-score is het verschil met het gemiddelde, gedeeld door de standaardafwijking.",
        "Binnen één standaardafwijking ligt ongeveer achtenzestig procent, binnen twee ongeveer vijfennegentig procent.",
        "Een steekproef is representatief als ze op de belangrijke kenmerken op de populatie lijkt.",
        "Sterke samenhang betekent niet dat de ene de oorzaak van de andere is.",
        "De p-waarde is de kans op zo'n resultaat of extremer, als de nulhypothese waar is.",
        "Ligt de p-waarde onder alfa, dan verwerp je de nulhypothese.",
    ],
)

# ───────────────────────── 17. Matrices en hun bewerkingen
BUNDELS["matrices-en-hun-bewerkingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Matrices en hun bewerkingen",
    onder="Dimensie, optellen en vermenigvuldigen, bijzondere matrices, en de determinant, de inverse en de rang.",
    secties=[
        dict(kop="Dimensie en bewerkingen", blokken=[
            ("p", "<strong>Een matrix van dimensie drie bij vier heeft drie rijen en vier kolommen.</strong> "
                  "Eerst de rijen, dan de kolommen: die volgorde omdraaien is de meest gemaakte fout van "
                  "het hoofdstuk. Een matrix van <strong>twee bij vijf heeft tien elementen</strong>, en "
                  "een <strong>kolommatrix met vier elementen heeft vier rijen</strong>."),
            ("p", "<strong>Twee matrices kan je optellen als ze precies dezelfde dimensie hebben</strong>, "
                  "want je telt element per element op. <strong>Bij een vermenigvuldiging met een reëel "
                  "getal vermenigvuldig je elk element met dat getal</strong>; dat heet de scalaire "
                  "vermenigvuldiging en is iets heel anders dan het product van twee matrices."),
            ("p", "<strong>Het product A maal B kan je berekenen als het aantal kolommen van A gelijk is "
                  "aan het aantal rijen van B.</strong> Elk element van het product is een rij van A tegen "
                  "een kolom van B, en die twee moeten even lang zijn. Zo heeft het <strong>product van "
                  "een matrix twee bij drie met een matrix drie bij vier de dimensie twee bij vier</strong>: "
                  "de binnenste getallen vallen weg, de buitenste blijven over."),
            ("kader", "<strong>Het vermenigvuldigen van matrices is niet commutatief.</strong> A maal B is "
                      "in het algemeen iets anders dan B maal A, en soms bestaat maar één van de twee. Dat "
                      "is het grote verschil met gewone getallen."),
        ]),
        dict(kop="Bijzondere matrices", blokken=[
            ("p", tabel(["Soort matrix", "Wat ze is", "Weetje"], [
                ["vierkante matrix", "evenveel rijen als kolommen", "alleen zij kan een determinant of een inverse hebben"],
                ["nulmatrix", "elk element is nul", "niet te verwarren met een matrix met determinant nul"],
                ["eenheidsmatrix", "enen op de hoofddiagonaal, elders nullen", "van orde drie staan er dus drie enen"],
                ["diagonaalmatrix", "vierkant, en alles buiten de hoofddiagonaal is nul", "de eenheidsmatrix is er een bijzonder geval van"],
                ["symmetrische matrix", "gelijk aan haar getransponeerde", "ze is dan noodzakelijk vierkant"],
            ])),
            ("p", "<strong>De eenheidsmatrix is het neutraal element voor de vermenigvuldiging van "
                  "vierkante matrices</strong>: vermenigvuldigen ermee verandert niets. Een matrix met "
                  "<strong>determinant nul</strong> heet een niet-inverteerbare of singuliere matrix, en "
                  "dat is iets anders dan een nulmatrix."),
            ("p", "<strong>Transponeren maakt van de rijen kolommen en van de kolommen rijen.</strong> Een "
                  "matrix van twee bij vijf wordt zo een matrix van vijf bij twee, met dus "
                  "<strong>vijf</strong> rijen. <strong>De getransponeerde van een product A maal B is de "
                  "getransponeerde van B maal de getransponeerde van A</strong>: de volgorde draait om, "
                  "anders zouden de dimensies niet meer passen."),
            ("p", "<strong>De matrices van een vaste dimensie vormen met de optelling de structuur van een "
                  "commutatieve groep</strong>: de nulmatrix is het neutraal element en de tegengestelde matrix het "
                  "symmetrisch element."),
            ("weetje", "<strong>Bij matrices bestaan er nuldelers.</strong> Twee matrices die geen van "
                       "beide nul zijn, kunnen samen toch de nulmatrix geven. Bij reële getallen kan dat "
                       "niet."),
        ]),
        dict(kop="De determinant", blokken=[
            ("p", "<strong>De determinant van een matrix van orde twee is het product van de "
                  "hoofddiagonaal min het product van de andere diagonaal</strong>: linksboven maal "
                  "rechtsonder, min rechtsboven maal linksonder. Voor de matrix met op de eerste rij één "
                  "en twee en op de tweede rij drie en vier is dat <strong>min twee</strong>. De "
                  "<strong>determinant van de eenheidsmatrix is één</strong>, en een matrix met "
                  "<strong>twee volledig gelijke rijen heeft determinant nul</strong>."),
            ("p", "<strong>Alleen vierkante matrices hebben een determinant.</strong> Bij een rechthoekige "
                  "matrix is ze niet gedefinieerd; de rang kan je er wel van bepalen."),
            ("p", "<strong>De minor van een element is de determinant die overblijft als je zijn rij en "
                  "kolom schrapt.</strong> Een <strong>cofactor is die minor met een teken dat van de "
                  "plaats afhangt</strong>, afwisselend als een schaakbord, te beginnen met plus "
                  "linksboven. <strong>Een determinant van orde drie bereken je met de hand door te "
                  "ontwikkelen naar een rij of een kolom, met minoren en cofactoren</strong>; kies er een "
                  "met veel nullen, dan valt het meeste rekenwerk weg."),
            ("p", "<strong>De determinant is nuttig omdat je er in één berekening mee ziet of een matrix "
                  "inverteerbaar is</strong>, en daarmee ook of een stelsel met die coëfficiëntenmatrix "
                  "precies één oplossing heeft."),
        ]),
        dict(kop="Inverse en rang", blokken=[
            ("p", "<strong>Een vierkante matrix is inverteerbaar als haar determinant verschillend is van "
                  "nul.</strong> Determinant nul betekent dat rijen van elkaar afhangen, en dan kan je de "
                  "bewerking niet ongedaan maken: <strong>zo'n matrix heeft geen inverse</strong>. "
                  "<strong>Een rechthoekige matrix heeft er evenmin een.</strong> <strong>Vermenigvuldig "
                  "je een matrix met haar inverse, dan krijg je de eenheidsmatrix</strong>, in beide "
                  "volgordes."),
            ("p", "<strong>De rang van een matrix is het aantal rijen dat niet nul is in haar rijcanonieke "
                  "vorm.</strong> De rang zegt dus hoeveel rijen echt nieuwe informatie geven. De "
                  "<strong>rang van de eenheidsmatrix van orde drie is drie</strong> en de <strong>rang "
                  "van de nulmatrix is nul</strong>. <strong>Een matrix heeft maar één rijcanonieke "
                  "vorm</strong>, welke rijoperaties je ook kiest, en daarom is de rang eenduidig bepaald."),
            ("p", "<strong>Een vierkante matrix van orde n is inverteerbaar als haar rang gelijk is aan "
                  "n.</strong> Volle rang, determinant verschillend van nul en inverteerbaar zijn drie "
                  "manieren om hetzelfde te zeggen."),
            ("p", "<strong>De drie elementaire rijoperaties</strong> zijn: <strong>rijen verwisselen, een "
                  "rij met een getal vermenigvuldigen, of een veelvoud van een rij bij een andere "
                  "tellen</strong>. Ze veranderen de rang niet en houden een stelsel gelijkwaardig. "
                  "Vermenigvuldigen met nul mag niet."),
            ("p", "Een praktijkvoorbeeld van het product: zet een winkel <strong>de bestelde aantallen in "
                  "één matrix en de eenheidsprijzen in een andere</strong>, dan geeft hun product <strong>de "
                  "totale prijs per bestelling</strong>, want elk element is een rij aantallen tegen een "
                  "kolom prijzen."),
            ("kader", "<strong>Bij de inverse van een matrix van orde drie laat je het rekenwerk aan de "
                      "rekenapp over, maar je controleert het resultaat met de eenheidsmatrix.</strong> Het "
                      "product met de oorspronkelijke matrix moet de eenheidsmatrix geven. Die controle "
                      "kost één bewerking en vangt elke tikfout."),
        ]),
    ],
    onthoud=[
        "Een matrix van dimensie drie bij vier heeft drie rijen en vier kolommen.",
        "Twee matrices optellen kan alleen als ze precies dezelfde dimensie hebben.",
        "A maal B bestaat als het aantal kolommen van A gelijk is aan het aantal rijen van B.",
        "Het vermenigvuldigen van matrices is niet commutatief.",
        "De eenheidsmatrix is het neutraal element voor de vermenigvuldiging van vierkante matrices.",
        "De getransponeerde van A maal B is de getransponeerde van B maal de getransponeerde van A.",
        "Determinant van orde twee: het product van de hoofddiagonaal min het product van de andere diagonaal.",
        "Een vierkante matrix is inverteerbaar als haar determinant verschillend is van nul.",
        "De rang is het aantal rijen dat niet nul is in de rijcanonieke vorm.",
    ],
)

# ───────────────────────── 18. Stelsels oplossen en matrixmodellen
BUNDELS["stelsels-oplossen-en-matrixmodellen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stelsels oplossen en matrixmodellen",
    onder="Gauss-Jordan, de rang en de vrijheidsgraden, en matrices die een toestand laten evolueren.",
    secties=[
        dict(kop="Een stelsel als matrix", blokken=[
            ("p", "<strong>In de uitgebreide coëfficiëntenmatrix staan de coëfficiënten én de constanten "
                  "uit het rechterlid.</strong> Die constanten komen in een extra kolom, meestal met een "
                  "streep ervoor."),
            ("p", "<strong>Twee stelsels heten gelijkwaardig als ze dezelfde oplossingenverzameling "
                  "hebben.</strong> Elke <strong>elementaire rijoperatie maakt een gelijkwaardig "
                  "stelsel</strong> en <strong>verandert de oplossingenverzameling dus niet</strong>; "
                  "daarom mag je ze blijven toepassen tot de oplossing eruit af te lezen is. "
                  "<strong>Rijen optellen en verwisselen mag omdat die bewerkingen een gelijkwaardig "
                  "stelsel opleveren</strong> — de determinant verandert er wél door, maar die telt hier "
                  "niet. <strong>Een rij met nul vermenigvuldigen mag niet</strong>: dan gooi je een hele "
                  "vergelijking weg. Vermenigvuldigen mag alleen met een getal dat niet nul is."),
            ("p", "<strong>De methode van Gauss-Jordan vormt de matrix met rijoperaties om naar de "
                  "rijcanonieke vorm.</strong> In die vorm lees je de oplossing meteen af, of zie je dat "
                  "er geen of oneindig veel zijn."),
        ]),
        dict(kop="Bepaald, onbepaald of strijdig", blokken=[
            ("p", tabel(["Soort stelsel", "Wat geldt voor de rangen", "Hoeveel oplossingen"], [
                ["bepaald", "beide rangen gelijk aan het aantal onbekenden", "één"],
                ["onbepaald", "beide rangen gelijk, maar kleiner dan het aantal onbekenden", "oneindig veel"],
                ["strijdig", "de rang van de coëfficiëntenmatrix is de kleinste", "nul"],
            ])),
            ("p", "<strong>Een bepaald stelsel heeft precies één oplossing</strong>, en daarvoor moeten "
                  "<strong>beide rangen gelijk zijn aan het aantal onbekenden</strong>: bij vier "
                  "onbekenden dus rang <strong>vier</strong>. Evenveel vergelijkingen als onbekenden "
                  "volstaat niet, want twee keer dezelfde vergelijking telt maar één keer mee. Je kan zo'n "
                  "stelsel ook <strong>met de inverse matrix oplossen, als de coëfficiëntenmatrix vierkant "
                  "en inverteerbaar is</strong>."),
            ("p", "<strong>Een onbepaald stelsel heeft oneindig veel oplossingen</strong>, die je schrijft "
                  "met parameters. <strong>Een vrijheidsgraad is een onbekende die je vrij mag kiezen, "
                  "waarna de rest vastligt</strong>, en het aantal vrijheidsgraden is het aantal "
                  "onbekenden min de rang: bij <strong>drie onbekenden en rang twee is dat "
                  "één</strong>. Je <strong>noteert de oplossingenverzameling als een verzameling van "
                  "koppels of drietallen met een parameter erin</strong>, zodat je ziet hoe de oplossingen "
                  "van elkaar afhangen."),
            ("p", "<strong>Een strijdig stelsel heeft nul oplossingen</strong>: de "
                  "oplossingenverzameling is leeg. Je <strong>herkent het in de rijcanonieke vorm aan een "
                  "rij met overal nullen links en een getal dat niet nul is rechts</strong>. Die rij zegt "
                  "letterlijk dat nul gelijk is aan dat getal; een rij met overal nullen, ook rechts, is "
                  "net onschuldig. Meetkundig: <strong>twee evenwijdige rechten die niet samenvallen geven "
                  "een strijdig stelsel</strong>."),
            ("kader", "<strong>Een stelsel met meer onbekenden dan vergelijkingen heeft niet altijd "
                      "oplossingen.</strong> Het kan nog strijdig zijn. Heeft het er wel, dan zijn het "
                      "meteen oneindig veel."),
        ]),
        dict(kop="Matrixmodellen", blokken=[
            ("p", "<strong>Een overgangsmatrix beschrijft hoe een toestand overgaat in de volgende "
                  "toestand.</strong> Je vermenigvuldigt de huidige toestand ermee en krijgt de volgende. "
                  "<strong>Een overgangsmatrix is altijd vierkant</strong>, want ze zet een toestand om in "
                  "een toestand van dezelfde soort. <strong>Een nul erin betekent dat die overgang niet "
                  "voorkomt.</strong>"),
            ("p", "<strong>De toestand na twee overgangen bereken je met het kwadraat van de "
                  "overgangsmatrix</strong>, en na vijf stappen verhef je haar tot de "
                  "<strong>vijfde</strong> macht: één macht per stap. Voor tien jaar klantenverloop neem "
                  "je dus <strong>de beginverdeling maal de overgangsmatrix tot de tiende macht</strong>."),
            ("p", tabel(["Soort matrix", "Wat ze beschrijft", "Kenmerk"], [
                ["Markov-matrix", "overgangskansen tussen toestanden", "elke kolom telt op tot één"],
                ["Lesliematrix", "hoe een populatie per leeftijdsgroep evolueert", "met overlevingskansen en nakomelingen"],
                ["migratiematrix", "hoeveel inwoners van de ene streek naar de andere verhuizen", "de toestanden zijn de streken"],
                ["verbindingsmatrix", "welke knopen van een graaf verbonden zijn", "een één bij een verbinding, anders een nul"],
            ])),
            ("p", "<strong>Een graaf is een tekening met punten en verbindingen ertussen</strong>; die "
                  "punten heten knopen. Elke graaf kan je als matrix schrijven en elke zo'n matrix als "
                  "graaf tekenen: <strong>een graaf met vier knopen geeft een verbindingsmatrix van orde "
                  "vier</strong>. Een <strong>directe wegen matrix laat zien welke knopen rechtstreeks "
                  "verbonden zijn</strong>; omwegen vind je pas in haar machten terug, want <strong>het "
                  "kwadraat van een verbindingsmatrix telt de wegen van lengte twee</strong>."),
            ("p", "<strong>Een evenwichtstoestand is een toestand die na de overgang gelijk blijft.</strong> "
                  "Je <strong>ziet dat een model stabiliseert doordat de opeenvolgende toestanden bijna niet "
                  "meer van elkaar verschillen</strong>. <strong>Niet elk matrixmodel komt in evenwicht</strong>: "
                  "sommige blijven schommelen of groeien onbeperkt, dus dat moet je nagaan."),
            ("kader", "<strong>Een matrixmodel voorspelt niet met zekerheid wat er zal gebeuren.</strong> "
                      "Het rekent uit wat er gebeurt als de overgangen gelijk blijven. Verandert er iets in "
                      "de werkelijkheid, dan klopt het model niet meer. <strong>De rekenapp gebruik je "
                      "omdat je vaak hoge machten nodig hebt</strong>: het model opstellen en de uitkomst "
                      "duiden blijft jouw werk."),
        ]),
        dict(kop="Een stelsel uit een context", blokken=[
            ("p", "Ken je het <strong>totaalbedrag van drie bestellingen met telkens dezelfde drie "
                  "artikelen</strong>, dan kan je <strong>de prijs per artikel berekenen als het stelsel "
                  "bepaald is</strong>. Drie vergelijkingen met drie onbekenden, maar enkel als de drie "
                  "bestellingen echt nieuwe informatie geven; anders is het stelsel onbepaald of strijdig."),
        ]),
    ],
    onthoud=[
        "In de uitgebreide coëfficiëntenmatrix staan de coëfficiënten én de constanten uit het rechterlid.",
        "Elementaire rijoperaties veranderen de oplossingenverzameling niet; een rij met nul vermenigvuldigen mag niet.",
        "Gauss-Jordan vormt de matrix met rijoperaties om naar de rijcanonieke vorm.",
        "Een bepaald stelsel heeft precies één oplossing: beide rangen zijn gelijk aan het aantal onbekenden.",
        "Het aantal vrijheidsgraden is het aantal onbekenden min de rang.",
        "Strijdig: een rij met overal nullen links en een getal dat niet nul is rechts.",
        "De toestand na twee overgangen bereken je met het kwadraat van de overgangsmatrix.",
        "Een evenwichtstoestand is een toestand die na de overgang gelijk blijft.",
        "Uit drie bestellingen bereken je de prijs per artikel alleen als het stelsel bepaald is.",
    ],
)

# ───────────────────────── 19. Algebraïsche structuren en groepen
BUNDELS["algebraische-structuren-en-groepen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Algebraïsche structuren en groepen",
    onder="De vier eigenschappen van een groep, de Cayley-tabel, en de uniciteit van het neutraal en het invers element.",
    secties=[
        dict(kop="Wat een groep is", blokken=[
            ("p", "<strong>Een verzameling met een bewerking is een groep als ze aan vier eigenschappen "
                  "voldoet</strong>: de bewerking is <strong>intern</strong> en <strong>associatief</strong>, "
                  "er is een <strong>neutraal element</strong>, en elk element heeft een <strong>invers "
                  "element</strong>."),
            ("p", tabel(["Eigenschap", "Wat ze zegt", "Voorbeeld"], [
                ["intern", "het resultaat ligt altijd weer in de verzameling", "de optelling in de gehele getallen wel, de deling niet"],
                ["associatief", "de haakjes mogen verschuiven zonder gevolg", "a met (b met c) geeft hetzelfde als (a met b) met c"],
                ["neutraal element", "het laat elk ander element ongewijzigd", "nul bij de optelling, één bij de vermenigvuldiging"],
                ["invers element", "samen met a geeft het het neutraal element", "het tegengestelde, of het omgekeerde"],
            ])),
            ("p", "<strong>Een groep heet commutatief als de volgorde van de twee elementen niets "
                  "uitmaakt.</strong> Dat is een vijfde eigenschap die erbij komt, dus <strong>niet elke "
                  "groep is commutatief</strong>: de vermenigvuldiging van matrices bijvoorbeeld niet. "
                  "<strong>Een eindige groep is een groep met een eindig aantal elementen</strong>, maar "
                  "<strong>een groep hoeft niet eindig te zijn</strong>: de gehele getallen met de "
                  "optelling vormen een oneindige groep."),
            ("p", "<strong>Om aan te tonen dat iets een groep is, ga je de vier eigenschappen één voor één "
                  "na.</strong> Eén tegenvoorbeeld bij één eigenschap volstaat om te besluiten dat het "
                  "geen groep is."),
        ]),
        dict(kop="Voorbeelden en tegenvoorbeelden", blokken=[
            ("p", "<strong>De gehele getallen vormen met de optelling een groep</strong>: de optelling is "
                  "intern en associatief, <strong>nul is het neutraal element</strong> en elk geheel getal "
                  "heeft zijn tegengestelde. Het <strong>invers element van zeven is min zeven</strong>."),
            ("p", "<strong>De natuurlijke getallen vormen met de optelling geen groep</strong>: er zijn "
                  "geen negatieve getallen, dus drie heeft geen tegengestelde binnen de verzameling. "
                  "<strong>De gehele getallen vormen met de vermenigvuldiging evenmin een groep</strong>: "
                  "het invers van drie zou een derde zijn, en dat is geen geheel getal. Alleen één en min "
                  "één hebben er een."),
            ("p", "<strong>De reële getallen zonder nul vormen met de vermenigvuldiging wél een "
                  "groep</strong>, met <strong>één</strong> als neutraal element. Nul moet eruit, want "
                  "<strong>nul heeft geen invers element voor de vermenigvuldiging</strong>: er bestaat "
                  "geen getal dat maal nul één geeft."),
            ("p", "<strong>De matrices van orde twee vormen onder de optelling een groep, en ze is "
                  "bovendien commutatief</strong>: de nulmatrix is het neutraal element en elke matrix "
                  "heeft haar tegengestelde. Bij de vermenigvuldiging lukt het niet."),
            ("weetje", "Een voorbeeld uit de meetkunde: de <strong>vier draaiingen die een vierkant op "
                       "zichzelf afbeelden</strong>, met na elkaar uitvoeren als bewerking, vormen een "
                       "<strong>eindige commutatieve groep</strong>. De draaiing over nul graden is het "
                       "neutraal element en elke draaiing heeft haar tegendraaiing."),
        ]),
        dict(kop="De Cayley-tabel", blokken=[
            ("p", "<strong>In een Cayley-tabel staat het resultaat van de bewerking voor elk paar "
                  "elementen</strong>: rij voor het eerste element, kolom voor het tweede, en in het vakje "
                  "het resultaat. Een groep met <strong>vijf elementen</strong> geeft dus een tabel met "
                  "<strong>vijfentwintig</strong> vakjes, en een groep met zes elementen heeft "
                  "<strong>zes</strong> rijen. <strong>Van een oneindige groep kan je de volledige tabel "
                  "niet opstellen</strong>, want ze zou oneindig veel rijen hebben."),
            ("p", "Uit de tabel lees je de eigenschappen af. <strong>Is de tabel symmetrisch om de "
                  "hoofddiagonaal, dan is de groep commutatief.</strong> <strong>Het neutraal element "
                  "herken je doordat zijn rij en zijn kolom gewoon de kopregel herhalen.</strong> <strong>Het "
                  "invers element van a vind je door in de rij van a te zoeken waar het neutraal element "
                  "staat</strong>; de kolom waarin dat vakje staat, wijst het aan. En <strong>is elk "
                  "element zijn eigen invers, dan staat op de hoofddiagonaal overal het neutraal "
                  "element</strong>."),
            ("p", "<strong>In de Cayley-tabel van een groep komt elk element precies één keer voor in elke "
                  "rij.</strong> Zou een element twee keer voorkomen, dan had je twee oplossingen voor "
                  "dezelfde vergelijking, en dat kan niet in een groep."),
        ]),
        dict(kop="Uniciteit en rekenen in een groep", blokken=[
            ("p", "<strong>Een groep heeft juist één neutraal element</strong> en <strong>elk element heeft "
                  "juist één invers element</strong>. Dat heet de <strong>uniciteit</strong>: allebei zijn ze "
                  "<strong>uniek</strong>, en dat is te bewijzen. Let op wat je precies bewijst: <strong>dat er één bestaat, is een van de vier "
                  "eigenschappen; dat het er maar één is, moet je aantonen.</strong> <strong>Het bewijs "
                  "begint door te veronderstellen dat er twee neutrale elementen zijn</strong>; daarna "
                  "bewerk je ze met elkaar en toont elk van de twee aan dat het resultaat de andere is."),
            ("p", "Twee rekenregels voor inversen. <strong>Het invers van het invers van a is "
                  "a</strong>: twee keer omkeren brengt je terug bij het begin. En bij een product "
                  "<strong>keert de volgorde om</strong>: het invers van a bewerkt met b is eerst het "
                  "invers van b en dan dat van a, <strong>niet andersom</strong>. <strong>Dat komt omdat "
                  "je het binnenste paar eerst moet kunnen wegwerken</strong>: zet je ze omgekeerd naast "
                  "elkaar, dan valt eerst b weg en pas daarna a. Bij een commutatieve groep maakt dat "
                  "verschil natuurlijk niets uit."),
            ("p", "<strong>In een groep mag je links en rechts van het gelijkheidsteken hetzelfde element "
                  "wegwerken</strong> door beide leden met zijn invers te bewerken. Dat is het hele idee "
                  "achter het oplossen van vergelijkingen in een groep, en <strong>de kant volgt a</strong>: "
                  "bij <strong>a bewerkt met x is b</strong> bewerk je <strong>links</strong> met het "
                  "invers van a, bij <strong>x bewerkt met a is b</strong> bewerk je <strong>rechts</strong>. "
                  "In een groep die niet commutatief is, is die kant belangrijk."),
        ]),
    ],
    onthoud=[
        "Een groep: intern, associatief, een neutraal element, en voor elk element een invers element.",
        "Niet elke groep is commutatief: de vermenigvuldiging van matrices bijvoorbeeld niet.",
        "Eén tegenvoorbeeld bij één eigenschap volstaat om te besluiten dat het geen groep is.",
        "De gehele getallen vormen met de optelling een groep, met nul als neutraal element.",
        "De reële getallen zonder nul vormen met de vermenigvuldiging een groep; nul heeft geen invers element.",
        "Is de Cayley-tabel symmetrisch om de hoofddiagonaal, dan is de groep commutatief.",
        "In de Cayley-tabel van een groep komt elk element precies één keer voor in elke rij.",
        "Een groep heeft juist één neutraal element en elk element heeft juist één invers element.",
        "Het invers van a bewerkt met b is eerst het invers van b en dan dat van a.",
    ],
)

# ───────────────────────── 20. Punten, vectoren en afstanden in de ruimte
BUNDELS["punten-vectoren-en-afstanden-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Punten, vectoren en afstanden in de ruimte",
    onder="Vectoren met hun coördinaten en hun norm, het scalair product, en afstanden, hoeken en zwaartepunten.",
    secties=[
        dict(kop="Vrije vector en puntvector", blokken=[
            ("p", "<strong>Een vrije vector is een richting, een zin en een lengte, zonder vast "
                  "beginpunt.</strong> Je mag hem overal in de ruimte neerleggen; het blijft dezelfde "
                  "vector. <strong>Twee pijlen met dezelfde coördinaten maar met een ander beginpunt zijn "
                  "dus dezelfde vrije vector.</strong> Een <strong>puntvector</strong> is <strong>de "
                  "vector van de oorsprong naar een punt</strong>, en zijn coördinaten zijn precies die "
                  "van het punt."),
            ("p", "<strong>Een vector in de ruimte heeft drie coördinaten</strong>, één per as; in het "
                  "vlak zijn het er twee. Je werkt in een <strong>orthonormaal assenstelsel</strong>: "
                  "<strong>de assen staan loodrecht op elkaar en de eenheden zijn even lang</strong>. "
                  "Alleen dan kloppen de formules voor de norm, de afstand en de hoek."),
            ("p", "<strong>De coördinaten van de vector van A naar B zijn die van B min die van A</strong>: "
                  "eindpunt min beginpunt. Draai je het om, dan krijg je de tegengestelde vector. Een "
                  "<strong>richtingsvector van een rechte is een vector die evenwijdig is met die "
                  "rechte</strong>, en <strong>elke rechte heeft er oneindig veel</strong>, want elk "
                  "veelvoud is er ook een."),
        ]),
        dict(kop="Rekenen met vectoren", blokken=[
            ("p", "<strong>Optellen doe je coördinaat per coördinaat</strong>: de eerste bij de eerste, en "
                  "zo verder. <strong>Grafisch leg je de staart van de tweede aan de kop van de "
                  "eerste</strong>, en de somvector loopt van de eerste staart naar de laatste kop; met de "
                  "parallellogramregel krijg je hetzelfde. <strong>De optelling van vectoren is "
                  "commutatief</strong>, <strong>de nulvector is het neutraal element</strong> en "
                  "<strong>het symmetrisch element is de tegengestelde vector</strong>, met alle "
                  "coördinaten van teken veranderd."),
            ("p", "<strong>Bij een vermenigvuldiging met een getal vermenigvuldig je elke coördinaat "
                  "afzonderlijk</strong>: de vector twee, min één, drie maal twee heeft als eerste "
                  "coördinaat <strong>vier</strong>. <strong>Met een negatief getal keert de zin om</strong>; "
                  "de richting blijft dezelfde en de lengte verandert met de grootte van dat getal."),
            ("p", "<strong>De norm van een vector is zijn lengte</strong>, berekend als de wortel uit de "
                  "som van de kwadraten van de coördinaten. <strong>Een norm kan nooit negatief zijn</strong>; "
                  "alleen de nulvector heeft norm nul. De norm van de vector <strong>drie, nul, vier is "
                  "vijf</strong>."),
            ("p", "<strong>Een vector ontbinden in zijn componenten betekent hem schrijven als een som van "
                  "vectoren langs de assen.</strong> Elke coördinaat is de lengte van één component, en "
                  "dat kan grafisch en door te rekenen."),
            ("weetje", "Werken er <strong>twee krachten tegelijk op een voorwerp</strong>, dan vind je de "
                       "<strong>resulterende kracht door de twee krachtvectoren op te tellen</strong>. Een "
                       "kracht heeft immers een grootte én een richting. Enkel de getallen optellen klopt "
                       "alleen als ze dezelfde kant op wijzen."),
        ]),
        dict(kop="Het scalair product", blokken=[
            ("p", "<strong>Het scalair product van twee vectoren levert een getal op</strong>, geen "
                  "vector; daar komt de naam vandaan. <strong>In coördinaten tel je de producten van de "
                  "overeenkomstige coördinaten op</strong>: voor één, twee, drie en twee, nul, één geeft "
                  "dat <strong>vijf</strong>. <strong>Het scalair product is commutatief.</strong>"),
            ("p", "<strong>Het scalair product van twee loodrechte vectoren is nul</strong>, en dat werkt "
                  "ook omgekeerd: dat is het <strong>criterium voor loodrechte stand</strong>. <strong>Om "
                  "na te gaan of twee rechten loodrecht staan, bereken je dus het scalair product van hun "
                  "richtingsvectoren</strong>, tenminste in een orthonormaal assenstelsel. <strong>Het "
                  "werkt omdat de cosinus van negentig graden nul is</strong>: het scalair product is het "
                  "product van de normen maal die cosinus."),
            ("p", "<strong>De hoek tussen twee vectoren bereken je uit het scalair product gedeeld door "
                  "het product van de normen</strong>; die breuk is de cosinus van de hoek. <strong>Is het "
                  "scalair product negatief, dan is de hoek stomp</strong>, niet scherp: bij een scherpe "
                  "hoek is het positief, bij een rechte hoek nul."),
            ("p", "<strong>Het scalair product van een vector met zichzelf is het kwadraat van zijn "
                  "norm</strong>, niet de norm zelf. En <strong>twee vectoren zijn evenwijdig als de ene "
                  "een veelvoud van de andere is</strong>: alle coördinaten verschillen dan met dezelfde "
                  "factor. Een <strong>normaalvector van een vlak</strong> is <strong>een vector die "
                  "loodrecht op dat vlak staat</strong>; zijn coördinaten lees je af uit de cartesische "
                  "vergelijking."),
        ]),
        dict(kop="Afstanden, middens en zwaartepunten", blokken=[
            ("p", "<strong>De afstand tussen twee punten is de norm van de vector tussen die twee "
                  "punten</strong>: eerst de vector, dan zijn lengte. De punten <strong>één, twee, drie en "
                  "één, twee, acht liggen vijf uit elkaar</strong>, en het punt <strong>twee, drie, zes "
                  "ligt zeven van de oorsprong</strong>."),
            ("p", tabel(["Wat je zoekt", "Hoe je het berekent", "Voorbeeld"], [
                ["het midden van een lijnstuk", "het gemiddelde van de coördinaten van de twee uiteinden", "tussen twee, vier, zes en vier, acht, tien is de eerste coördinaat drie"],
                ["het zwaartepunt van een driehoek", "de som van de drie hoekpunten gedeeld door drie", "bij eerste coördinaten nul, drie en zes wordt dat drie"],
                ["het zwaartepunt van een viervlak", "de som van de vier hoekpunten gedeeld door vier", "hetzelfde recept, met vier punten"],
            ])),
            ("weetje", "Vliegt een drone <strong>eerst drie meter naar het oosten en dan vier meter naar "
                       "het noorden</strong>, dan vind je zijn verplaatsing <strong>als de som van de twee "
                       "verplaatsingsvectoren</strong>: vijf meter, niet zeven. De afgelegde weg is wel "
                       "zeven meter."),
        ]),
    ],
    onthoud=[
        "Een vrije vector is een richting, een zin en een lengte, zonder vast beginpunt.",
        "De coördinaten van de vector van A naar B zijn die van B min die van A.",
        "Vectoren optellen doe je coördinaat per coördinaat.",
        "De norm is de wortel uit de som van de kwadraten van de coördinaten.",
        "Het scalair product levert een getal op: de som van de producten van de overeenkomstige coördinaten.",
        "Het scalair product van twee loodrechte vectoren is nul.",
        "Is het scalair product negatief, dan is de hoek stomp.",
        "De afstand tussen twee punten is de norm van de vector tussen die twee punten.",
        "Het zwaartepunt van een driehoek is de som van de drie hoekpunten gedeeld door drie.",
    ],
)

# ───────────────────────── 21. Rechten en vlakken in de ruimte
BUNDELS["rechten-en-vlakken-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rechten en vlakken in de ruimte",
    onder="Vectoriële, parametrische en cartesische vergelijkingen, onderlinge ligging, afstanden en hoeken.",
    secties=[
        dict(kop="De vergelijking van een rechte", blokken=[
            ("p", "<strong>Om de vergelijking van een rechte op te stellen heb je een punt en een "
                  "richtingsvector nodig</strong>: het punt zegt waar ze ligt, de richtingsvector welke "
                  "kant ze op loopt. Twee punten volstaan ook, want daar haal je de richtingsvector uit."),
            ("p", "In de <strong>parametrische vergelijkingen</strong> geeft <strong>elke waarde van de "
                  "parameter een ander punt van de rechte</strong>; laat je de parameter alle reële "
                  "waarden doorlopen, dan krijg je de hele rechte. In de ruimte zijn dat <strong>drie</strong> "
                  "vergelijkingen, één per coördinaat, allemaal met dezelfde parameter."),
            ("p", "<strong>Een rechte in de ruimte heeft twee cartesische vergelijkingen, geen één</strong>: "
                  "ze is de doorsnede van twee vlakken. <strong>In het vlak heeft een rechte er wel precies "
                  "één</strong>. <strong>Van parametrisch naar cartesisch werk je de parameter weg</strong>: "
                  "je drukt hem uit in één vergelijking en vult die in de twee andere in."),
            ("p", "<strong>Of een punt op een rechte ligt, controleer je door zijn coördinaten in de "
                  "vergelijkingen in te vullen.</strong> Bij de parametrische vorm moet er voor alle drie "
                  "dezelfde parameterwaarde uitkomen."),
        ]),
        dict(kop="De vergelijking van een vlak", blokken=[
            ("p", "<strong>Een vlak ligt vast door één punt en twee richtingsvectoren die niet evenwijdig "
                  "zijn</strong>, of door <strong>drie punten die niet op eenzelfde rechte liggen</strong>. "
                  "<strong>Drie punten op één rechte bepalen geen vlak</strong>, want daar gaan oneindig "
                  "veel vlakken door. Daarom staat een tafel met drie poten nooit te wiebelen. In de "
                  "<strong>parametrische vergelijkingen van een vlak staan twee parameters</strong>, één "
                  "per richtingsvector."),
            ("p", "<strong>De cartesische vergelijking van een vlak heeft de vorm: a maal x plus b maal y "
                  "plus c maal z plus d is nul.</strong> Eén vergelijking van de eerste graad in drie "
                  "onbekenden. <strong>De coëfficiënten van x, y en z vormen samen een "
                  "normaalvector</strong> van dat vlak: voor <strong>twee x min drie y plus z min vijf is "
                  "nul</strong> is de eerste coördinaat daarvan <strong>twee</strong>. Ken je <strong>een "
                  "punt en een normaalvector, dan kan je die cartesische vergelijking opstellen</strong>. "
                  "Het vlak door de x-as en de y-as heeft als vergelijking <strong>z is gelijk aan "
                  "nul</strong>."),
            ("p", "<strong>Met een drie bij drie determinant stel je de cartesische vergelijking op door "
                  "die determinant gelijk te stellen aan nul.</strong> In de determinant staan de "
                  "verbindingsvector naar een onbekend punt en de twee richtingsvectoren. Nul betekent "
                  "<strong>dat de drie vectoren in eenzelfde vlak liggen</strong>; was de determinant niet "
                  "nul, dan zouden ze de hele ruimte opspannen."),
            ("p", "Omgekeerd, <strong>van cartesisch naar parametrisch zoek je een punt en twee "
                  "richtingsvectoren van het vlak</strong>. Twee van de drie onbekenden mag je vrij kiezen, "
                  "en die twee vrijheidsgraden worden je twee parameters."),
        ]),
        dict(kop="Onderlinge ligging", blokken=[
            ("p", tabel(["Wat je vergelijkt", "Mogelijke liggingen"], [
                ["twee rechten", "samenvallend, evenwijdig, snijdend of kruisend"],
                ["een rechte en een vlak", "in het vlak, evenwijdig ernaast, of snijdend"],
                ["twee vlakken", "samenvallend, evenwijdig, of snijdend volgens een rechte"],
            ])),
            ("p", "<strong>Kruisende rechten zijn rechten die niet evenwijdig zijn en toch geen snijpunt "
                  "hebben.</strong> Ze liggen niet in eenzelfde vlak; denk aan twee wegen boven elkaar met "
                  "een brug ertussen. Dat bestaat alleen in de ruimte, en daarom zijn <strong>twee rechten "
                  "die elkaar niet snijden niet noodzakelijk evenwijdig</strong>. <strong>Twee evenwijdige "
                  "rechten liggen wél altijd in eenzelfde vlak</strong>, en door twee kruisende rechten "
                  "gaat net geen enkel vlak."),
            ("p", "<strong>Twee vlakken zijn evenwijdig als hun normaalvectoren veelvouden van elkaar "
                  "zijn.</strong> Ze <strong>vallen samen als je de ene vergelijking uit de andere kan "
                  "vermenigvuldigen</strong>; anders liggen ze er netjes naast. <strong>Twee vlakken die "
                  "niet evenwijdig zijn, snijden elkaar volgens een rechte</strong>, nooit in één punt."),
            ("p", "<strong>Een rechte is evenwijdig met een vlak als haar richtingsvector loodrecht op de "
                  "normaalvector staat</strong>, dus als hun scalair product nul is. Ligt er dan ook nog "
                  "een punt van de rechte in het vlak, dan ligt ze er helemaal in; in de praktijk "
                  "<strong>volstaat het dat twee van haar punten in het vlak liggen</strong>. "
                  "<strong>Loodrecht op het vlak staat ze als haar richtingsvector evenwijdig is met de "
                  "normaalvector.</strong>"),
        ]),
        dict(kop="Afstanden en hoeken", blokken=[
            ("p", "<strong>De afstand van een punt tot een vlak meet je langs de loodlijn uit dat punt op "
                  "het vlak</strong>, want de afstand is altijd de kortste. <strong>De afstand tussen twee "
                  "evenwijdige vlakken bereken je als de afstand van een punt van het ene tot het "
                  "andere</strong>; welk punt je kiest maakt niet uit. <strong>Tussen twee samenvallende "
                  "vlakken is de afstand nul</strong>, en ook <strong>tussen twee snijdende rechten is ze "
                  "nul</strong>, want ze hebben een punt gemeen."),
            ("p", "<strong>De hoek tussen twee vlakken is de hoek tussen hun normaalvectoren</strong>, "
                  "waarvan je de scherpe neemt. <strong>Tussen twee evenwijdige vlakken is die hoek "
                  "nul</strong> graden. <strong>De hoek tussen twee rechten vind je uit het scalair "
                  "product van hun richtingsvectoren</strong>, ook bij kruisende rechten, want de hoek "
                  "hangt enkel van de richtingen af."),
            ("weetje", "Bij een <strong>hellend dakvlak en de verticale gevel eronder</strong> is de hoek "
                       "tussen de twee vlakken <strong>de hoek tussen hun normaalvectoren, als scherpe hoek "
                       "genomen</strong>. De hellingshoek van het dak met de grond is een andere hoek."),
        ]),
    ],
    onthoud=[
        "Voor de vergelijking van een rechte heb je een punt en een richtingsvector nodig.",
        "Een rechte in de ruimte heeft twee cartesische vergelijkingen, in het vlak precies één.",
        "Een vlak ligt vast door drie punten die niet op eenzelfde rechte liggen.",
        "Cartesische vergelijking van een vlak: a maal x plus b maal y plus c maal z plus d is nul.",
        "De coëfficiënten van x, y en z vormen samen een normaalvector van dat vlak.",
        "Kruisende rechten zijn niet evenwijdig en hebben toch geen snijpunt.",
        "Twee vlakken zijn evenwijdig als hun normaalvectoren veelvouden van elkaar zijn.",
        "De afstand van een punt tot een vlak meet je langs de loodlijn uit dat punt op het vlak.",
        "De hoek tussen twee vlakken is de scherpe hoek tussen hun normaalvectoren.",
    ],
)

# ───────────────────────── 22. Programmeren: algoritmen en structuren
BUNDELS["programmeren-algoritmen-en-structuren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Programmeren: algoritmen en structuren",
    onder="De bouwstenen van een programma, de vier datastructuren, de algoritmische technieken, en correctheid en eindigheid.",
    secties=[
        dict(kop="Van probleem naar programma", blokken=[
            ("p", "<strong>Een algoritme is een stappenplan dat na eindig veel stappen tot een oplossing "
                  "komt.</strong> Het bestaat los van de taal; pas daarna schrijf je het in "
                  "<strong>Python</strong>, in een online omgeving, zodat je niets op je eigen computer "
                  "hoeft te installeren."),
            ("p", "Je werkt in <strong>vier stappen</strong>: <strong>het probleem analyseren, een "
                  "algoritme ontwerpen, het programmeren, en testen en debuggen</strong>. Meteen beginnen "
                  "typen zonder het probleem te analyseren kost je achteraf meer tijd dan het wint. "
                  "<strong>Debuggen is fouten opsporen en herstellen</strong>, en je <strong>test ook met "
                  "randgevallen, omdat fouten zich daar verstoppen</strong>: een lege lijst, één element, "
                  "een nul, een negatief getal."),
            ("p", "<strong>Geef variabelen een zinvolle naam, zodat je code leesbaar blijft</strong> voor "
                  "jezelf en voor anderen. De computer kan het niets schelen, maar een lezer wel, en dat "
                  "telt mee in de beoordeling. <strong>Commentaar wordt niet mee uitgevoerd</strong>; ze "
                  "staat er alleen voor wie de code leest."),
        ]),
        dict(kop="De bouwstenen", blokken=[
            ("p", tabel(["Bouwsteen", "Wat ze doet", "In Python"], [
                ["variabele", "een naam waarachter een waarde zit die kan veranderen", "je overschrijft de waarde gewoon"],
                ["constante", "een waarde die tijdens het programma niet verandert", "het aantal seconden in een uur, met een naam erbij"],
                ["conditie", "een stuk code alleen laten lopen als iets waar is", "de constructie met als en anders"],
                ["iteratie", "een herhaling van hetzelfde stuk code", "een lus, over een lijst of zolang iets geldt"],
                ["functie", "een stuk code een naam geven en hergebruiken", "één keer schrijven, zo vaak oproepen als je wil"],
            ])),
        ]),
        dict(kop="De vier datastructuren", blokken=[
            ("p", "<strong>Een string is een rij tekens</strong>: letters, cijfers en leestekens na "
                  "elkaar, tussen aanhalingstekens."),
            ("p", tabel(["Datastructuur", "Waarvoor", "Kenmerk"], [
                ["list", "een geordende rij die je nog wil aanpassen", "geordend én aanpasbaar"],
                ["tuple", "een geordende rij die vastligt", "je kan hem achteraf niet meer wijzigen"],
                ["set", "enkel de verschillende waarden overhouden", "elk element komt er maar één keer in voor"],
                ["dictionary, in het Nederlands een woordenboek", "paren van een sleutel en een waarde", "je zoekt iets op met de sleutel"],
            ])),
            ("p", "<strong>Een list en een tuple zijn allebei geordend; alleen de tuple ligt vast.</strong> "
                  "<strong>Een set kan hetzelfde element niet twee keer bevatten</strong>: steek je de "
                  "getallen één, twee, twee en drie erin, dan blijven er <strong>drie</strong> elementen "
                  "over. Dubbels eruit halen is precies waar een set voor dient."),
        ]),
        dict(kop="Algoritmische technieken", blokken=[
            ("p", "<strong>Recursie is een functie die zichzelf oproept</strong>, waarbij het probleem "
                  "telkens een beetje kleiner wordt tot het vanzelf oplosbaar is. <strong>Elke recursieve "
                  "functie heeft een geval nodig waarin ze zichzelf niet meer oproept</strong>, een "
                  "stopgeval. <strong>Zonder dat blijft ze zichzelf oproepen tot het programma "
                  "vastloopt</strong>, en geeft Python een foutmelding omdat de oproepen te diep gaan."),
            ("p", "<strong>Verdeel-en-heers</strong> is de techniek waarbij je <strong>een probleem "
                  "opsplitst in kleinere deelproblemen en de deeloplossingen daarna samenvoegt</strong>. "
                  "Sorteren doe je zo: splits de lijst in twee, sorteer elke helft en voeg ze samen. Moet "
                  "je in een <strong>gesorteerde lijst van duizend getallen</strong> nagaan of een getal "
                  "erin staat, dan is de slimste aanpak <strong>telkens de helft wegnemen</strong>: tien "
                  "stappen volstaan dan."),
            ("p", "<strong>Bij dynamisch programmeren bewaar je tussenresultaten zodat je ze niet twee "
                  "keer hoeft te berekenen.</strong> Bij de rij van Fibonacci scheelt dat het verschil "
                  "tussen een seconde en een eeuwigheid. Het <strong>kost meer geheugen maar wint "
                  "tijd</strong>."),
        ]),
        dict(kop="Correctheid, eindigheid en vergelijken", blokken=[
            ("p", "<strong>Een algoritme is correct als het voor elke toegelaten invoer het juiste antwoord "
                  "geeft</strong>, niet alleen voor de gevallen die je toevallig uitprobeerde. <strong>Het "
                  "is eindig als het na een eindig aantal stappen stopt.</strong> <strong>Je "
                  "beargumenteert de eindigheid omdat een programma dat blijft lopen niets oplost</strong>, "
                  "ook al klopt elke stap: bij een lus toon je dat de voorwaarde ooit vals wordt, bij "
                  "recursie dat je het stopgeval altijd bereikt."),
            ("p", "<strong>Twee oplossingen voor hetzelfde probleem vergelijk je op snelheid, "
                  "geheugengebruik en gedrag bij veel gegevens.</strong> <strong>Twee algoritmen die "
                  "hetzelfde antwoord geven, zijn daarom nog niet even snel</strong>: het ene kan duizend "
                  "keer trager zijn. Een oplossing die bij tien getallen vlot werkt, kan bij een miljoen "
                  "getallen onbruikbaar worden."),
        ]),
        dict(kop="Bestanden en bibliotheken", blokken=[
            ("p", "Naast een gewoon tekstbestand lees je ook <strong>CSV</strong>-bestanden in en schrijf "
                  "je ze weg: bestanden waarin de waarden door komma's of puntkomma's gescheiden staan, "
                  "zoals een tabel."),
            ("p", "<strong>Je mag matplotlib, numpy en random gebruiken</strong>, en geen andere, tenzij "
                  "de opdracht er uitdrukkelijk een vermeldt en toelicht. <strong>Matplotlib dient om "
                  "grafieken te tekenen</strong> van je gegevens, <strong>numpy om vlot met grote rijen "
                  "getallen te rekenen</strong> (veel sneller dan met een lus over een gewone list), en "
                  "<strong>random om toevalsgetallen te laten genereren</strong>, handig voor een simulatie."),
            ("p", "<strong>Een numerieke methode is een manier om een antwoord te benaderen met "
                  "rekenstappen.</strong> Je krijgt geen exacte formule maar een benadering, die je zo "
                  "nauwkeurig maakt als je wil. Zo <strong>benader je een bepaalde integraal door de "
                  "oppervlakte van heel veel smalle stroken op te tellen</strong>: precies de Riemannsom, "
                  "maar dan door de computer uitgevoerd."),
        ]),
    ],
    onthoud=[
        "Een algoritme is een stappenplan dat na eindig veel stappen tot een oplossing komt.",
        "Vier stappen: analyseren, een algoritme ontwerpen, programmeren, en testen en debuggen.",
        "De bouwstenen zijn variabele, constante, conditie, iteratie en functie.",
        "Een list is aanpasbaar, een tuple ligt vast, een set bevat elk element maar één keer.",
        "Elke recursieve functie heeft een stopgeval nodig waarin ze zichzelf niet meer oproept.",
        "Verdeel-en-heers splitst een probleem in kleinere deelproblemen en voegt de deeloplossingen samen.",
        "Bij dynamisch programmeren bewaar je tussenresultaten: het kost meer geheugen maar wint tijd.",
        "Correct is het juiste antwoord voor elke toegelaten invoer; eindig is stoppen na eindig veel stappen.",
        "Je mag matplotlib, numpy en random gebruiken; andere alleen als de opdracht er uitdrukkelijk een vermeldt.",
    ],
)

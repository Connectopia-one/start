# -*- coding: utf-8 -*-
r"""Machtswortels, machten met rationale exponent en logaritmen.

Het eerste onderdeel van de analysefiche G1. Het is rekengereedschap: zonder
de rekenregels hieronder kan je de exponentiële en logaritmische functies van
de latere thema's niet aan.

Deel 1 is machten en n-de machtswortels, deel 2 is de logaritme.

De vragen staan in echte wiskundige notatie, tussen \( en \). Enya Vermeyen,
leerkracht wiskunde, keek op 10 oktober 2026 naar dit hoofdstuk toen het nog
in woorden geschreven stond en had gelijk: een leerling van de derde graad
moet \(a^{1/3}\) kunnen lezen, niet "a tot de macht één derde". Zie
oefenplatform/lib/wiskunde.ts voor hoe je een formule schrijft.

Het antwoord van een invulvraag blijft wel gewone tekst: dat typt een kind in
een invulvakje, dus 9/4 en niet \(\tfrac{9}{4}\).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(\sqrt[3]{54}\).",
        opties=[
            r"\(3\sqrt[3]{2}\)",
            r"\(2\sqrt[3]{3}\)",
            r"\(3\sqrt[3]{6}\)",
            r"\(6\sqrt[3]{3}\)",
        ],
        antwoord=0,
        uitleg=r"Splits \(54=27\cdot 2\). Omdat \(\sqrt[3]{27}=3\), komt die 3 buiten het wortelteken: \(\sqrt[3]{54}=3\sqrt[3]{2}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\left(\dfrac{8}{27}\right)^{-2/3}\)? Schrijf je antwoord als een breuk.",
        antwoord=["9/4"],
        uitleg=r"De negatieve exponent keert de breuk om: \(\left(\tfrac{27}{8}\right)^{2/3}\). De derdemachtswortel geeft \(\tfrac{3}{2}\) en kwadrateren geeft \(\tfrac{9}{4}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(\sqrt[4]{16a^{8}b^{12}}\), met \(a>0\) en \(b>0\).",
        opties=[
            r"\(2a^{2}b^{3}\)",
            r"\(4a^{2}b^{3}\)",
            r"\(2a^{4}b^{8}\)",
            r"\(4a^{4}b^{6}\)",
        ],
        antwoord=0,
        uitleg=r"Elke exponent wordt door 4 gedeeld: \(\sqrt[4]{16}=2\), \(\sqrt[4]{a^{8}}=a^{2}\) en \(\sqrt[4]{b^{12}}=b^{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor elk reëel getal \(a\) geldt \(\sqrt{a^{2}}=a\).",
        antwoord=False,
        uitleg=r"Een vierkantswortel is nooit negatief, dus \(\sqrt{a^{2}}=|a|\). Neem \(a=-3\): \(\sqrt{9}=3\) en niet \(-3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(x^{3/4}=8\). Schrijf het getal.",
        antwoord=["16"],
        uitleg=r"Verhef beide leden tot de macht \(\tfrac{4}{3}\): \(x=8^{4/3}=\left(\sqrt[3]{8}\right)^{4}=2^{4}=16\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Maak de noemer rationaal in \(\dfrac{6}{\sqrt{5}-\sqrt{2}}\).",
        opties=[
            r"\(2\left(\sqrt{5}+\sqrt{2}\right)\)",
            r"\(2\left(\sqrt{5}-\sqrt{2}\right)\)",
            r"\(\dfrac{6\left(\sqrt{5}+\sqrt{2}\right)}{7}\)",
            r"\(\sqrt{5}+\sqrt{2}\)",
        ],
        antwoord=0,
        uitleg=r"Vermenigvuldig teller en noemer met \(\sqrt{5}+\sqrt{2}\). De noemer wordt \(5-2=3\), en \(\tfrac{6}{3}=2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt[3]{-8}=-2\).",
        antwoord=True,
        uitleg=r"\((-2)^{3}=-8\). Bij een oneven wortelexponent mag het grondtal negatief zijn; bij een even wortelexponent niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\sqrt{50}+\sqrt{18}-\sqrt{8}\).",
        opties=[
            r"\(6\sqrt{2}\)",
            r"\(4\sqrt{2}\)",
            r"\(10\sqrt{2}\)",
            r"\(\sqrt{60}\)",
        ],
        antwoord=0,
        uitleg=r"\(\sqrt{50}=5\sqrt{2}\), \(\sqrt{18}=3\sqrt{2}\) en \(\sqrt{8}=2\sqrt{2}\). Samen: \(5+3-2=6\), dus \(6\sqrt{2}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(16^{3/4}\)? Schrijf het getal.",
        antwoord=["8"],
        uitleg=r"\(16^{3/4}=\left(\sqrt[4]{16}\right)^{3}=2^{3}=8\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Schrijf \(\sqrt{a}\cdot\sqrt[3]{a}\) als één macht van \(a\), met \(a>0\).",
        opties=[
            r"\(a^{5/6}\)",
            r"\(a^{1/6}\)",
            r"\(a^{2/3}\)",
            r"\(a^{6/5}\)",
        ],
        antwoord=0,
        uitleg=r"\(a^{1/2}\cdot a^{1/3}=a^{1/2+1/3}=a^{5/6}\). Bij vermenigvuldigen tel je de exponenten op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor alle \(a>0\) en \(b>0\) geldt \(\sqrt{a+b}=\sqrt{a}+\sqrt{b}\).",
        antwoord=False,
        uitleg=r"Neem \(a=9\) en \(b=16\): \(\sqrt{25}=5\), maar \(3+4=7\). Een wortel verdeelt zich over een product en een quotiënt, nooit over een som.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\sqrt[5]{\dfrac{1}{32}}\)? Schrijf je antwoord als een breuk.",
        antwoord=["1/2"],
        uitleg=r"\(\left(\tfrac{1}{2}\right)^{5}=\tfrac{1}{32}\), dus de vijfdemachtswortel is \(\tfrac{1}{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2^{x}\cdot 2^{x+3}=2^{11}\).",
        opties=[r"\(x=4\)", r"\(x=5\)", r"\(x=8\)", r"\(x=11\)"],
        antwoord=0,
        uitleg=r"Links staat \(2^{2x+3}\). Gelijke grondtallen geven \(2x+3=11\), dus \(x=4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke \(x\) bestaat \(\sqrt[4]{x-3}\) in \(\mathbb{R}\)?",
        opties=[r"\(x\geq 3\)", r"\(x>3\)", r"\(x\leq 3\)", r"\(x\in\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"Een even wortelexponent vraagt een grondtal dat niet negatief is: \(x-3\geq 0\), dus \(x\geq 3\). Bij \(x=3\) is de wortel 0 en dat mag.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor \(a>0\) geldt \(\left(a^{m}\right)^{n}=a^{mn}\) ook wanneer \(m\) en \(n\) breuken zijn.",
        antwoord=True,
        uitleg=r"Net daarom spreken we rationale exponenten af: \(\left(a^{1/2}\right)^{1/3}=a^{1/6}=\sqrt[6]{a}\). Het grondtal moet wel positief blijven.",
    ),
    dict(
        type="invultekst",
        vraag=r"Er geldt \(\sqrt{72}=k\sqrt{2}\). Hoeveel is \(k\)? Schrijf het getal.",
        antwoord=["6"],
        uitleg=r"\(72=36\cdot 2\) en \(\sqrt{36}=6\), dus \(\sqrt{72}=6\sqrt{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(\dfrac{a^{-2}b^{3}}{a^{3}b^{-1}}\).",
        opties=[
            r"\(\dfrac{b^{4}}{a^{5}}\)",
            r"\(\dfrac{b^{2}}{a^{6}}\)",
            r"\(\dfrac{a^{5}}{b^{4}}\)",
            r"\(\dfrac{b^{3}}{a^{6}}\)",
        ],
        antwoord=0,
        uitleg=r"Trek de exponenten af: \(a^{-2-3}=a^{-5}\) en \(b^{3-(-1)}=b^{4}\). Dus \(a^{-5}b^{4}=\tfrac{b^{4}}{a^{5}}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\sqrt{2}\cdot\sqrt[3]{2}\cdot\sqrt[6]{2}\).",
        opties=[r"\(2\)", r"\(2^{5/6}\)", r"\(2^{3/2}\)", r"\(\sqrt[11]{2}\)"],
        antwoord=0,
        uitleg=r"\(\tfrac{1}{2}+\tfrac{1}{3}+\tfrac{1}{6}=1\), dus het product is \(2^{1}=2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welk van deze getallen is het grootst?",
        opties=[r"\(3^{1/3}\)", r"\(2^{1/2}\)", r"\(6^{1/6}\)", r"\(5^{1/5}\)"],
        antwoord=0,
        uitleg=r"Verhef alles tot de macht 6: \(3^{2}=9\), \(2^{3}=8\), \(6^{1}=6\) en \(5^{6/5}\approx 6{,}9\). Negen is het grootst, dus \(3^{1/3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom spreekt men \(a^{m/n}\) alleen af voor \(a\geq 0\)?",
        opties=[
            r"omdat \((-8)^{1/3}\) en \((-8)^{2/6}\) anders zouden verschillen",
            r"omdat \(a^{m/n}\) dan altijd negatief zou worden",
            r"omdat \(\sqrt[n]{0}\) niet bestaat voor oneven \(n\)",
            r"omdat \(\tfrac{m}{n}\) dan geen breuk meer is",
        ],
        antwoord=0,
        uitleg=r"\(\tfrac{1}{3}\) en \(\tfrac{2}{6}\) zijn hetzelfde getal, maar \(\sqrt[3]{-8}=-2\) terwijl \(\sqrt[6]{(-8)^{2}}=\sqrt[6]{64}=2\). Eén exponent met twee uitkomsten kan niet, dus blijft de afspraak bij \(a\geq 0\).",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\log_{3}81\)? Schrijf het getal.",
        antwoord=["4"],
        uitleg=r"Een logaritme is een exponent: \(3^{4}=81\), dus \(\log_{3}81=4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Schrijf \(\log_{a}\dfrac{x^{3}\sqrt{y}}{z}\) als een som en een verschil van logaritmen.",
        opties=[
            r"\(3\log_{a}x+\tfrac{1}{2}\log_{a}y-\log_{a}z\)",
            r"\(3\log_{a}x+2\log_{a}y-\log_{a}z\)",
            r"\(3\log_{a}x-\tfrac{1}{2}\log_{a}y+\log_{a}z\)",
            r"\(\tfrac{1}{3}\log_{a}x+\tfrac{1}{2}\log_{a}y-\log_{a}z\)",
        ],
        antwoord=0,
        uitleg=r"Een product wordt een som, een quotiënt een verschil, en een exponent komt vooraan. \(\sqrt{y}=y^{1/2}\) levert dus \(\tfrac{1}{2}\log_{a}y\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(\log_{2}(x-1)=5\). Schrijf het getal.",
        antwoord=["33"],
        uitleg=r"\(x-1=2^{5}=32\), dus \(x=33\). Controleer altijd of het argument positief blijft: \(33-1=32>0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(3^{x}=20\).",
        opties=[
            r"\(x=\dfrac{\ln 20}{\ln 3}\)",
            r"\(x=\ln 20-\ln 3\)",
            r"\(x=\dfrac{\ln 3}{\ln 20}\)",
            r"\(x=\ln\dfrac{20}{3}\)",
        ],
        antwoord=0,
        uitleg=r"Neem van beide leden de natuurlijke logaritme: \(x\ln 3=\ln 20\), dus \(x=\tfrac{\ln 20}{\ln 3}\approx 2{,}73\). Dat is de regel voor het veranderen van grondtal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\log(a+b)=\log a+\log b\).",
        antwoord=False,
        uitleg=r"Die regel geldt voor een product: \(\log(ab)=\log a+\log b\). Neem \(a=b=1\): links \(\log 2\approx 0{,}30\), rechts \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor \(a,b>0\) en \(a,b\neq 1\) geldt \(\log_{a}b\cdot\log_{b}a=1\).",
        antwoord=True,
        uitleg=r"Met het veranderen van grondtal is \(\log_{b}a=\tfrac{1}{\log_{a}b}\). Hun product is dus 1. Probeer het met \(\log_{2}8\cdot\log_{8}2=3\cdot\tfrac{1}{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\log_{5}\dfrac{1}{25}\)? Schrijf het getal.",
        antwoord=["-2", "min 2"],
        uitleg=r"\(5^{-2}=\tfrac{1}{25}\), dus de logaritme is \(-2\). Een argument tussen 0 en 1 geeft bij grondtal groter dan 1 altijd een negatieve logaritme.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het domein van \(f(x)=\ln\left(x^{2}-4\right)\)?",
        opties=[
            r"\(\left]-\infty,-2\right[\;\cup\;\left]2,+\infty\right[\)",
            r"\(\left]-2,2\right[\)",
            r"\(\left]2,+\infty\right[\)",
            r"\(\mathbb{R}\setminus\{-2,2\}\)",
        ],
        antwoord=0,
        uitleg=r"Het argument moet strikt positief zijn: \(x^{2}-4>0\), dus \(x<-2\) of \(x>2\). De negatieve tak hoort er wel bij, want \((-3)^{2}-4=5>0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor elke \(x\in\mathbb{R}\) geldt \(\ln\left(e^{x}\right)=x\).",
        antwoord=True,
        uitleg=r"De logaritme en de macht met hetzelfde grondtal heffen elkaar op. Let op het verschil met \(e^{\ln x}=x\): dat geldt enkel voor \(x>0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(\log_{2}x+\log_{2}(x-2)=3\).",
        opties=[
            r"\(x=4\)",
            r"\(x=4\) of \(x=-2\)",
            r"\(x=-2\)",
            r"\(x=8\)",
        ],
        antwoord=0,
        uitleg=r"Samen: \(\log_{2}\left(x(x-2)\right)=3\), dus \(x^{2}-2x-8=0\) en \(x=4\) of \(x=-2\). Maar \(\log_{2}(-2)\) bestaat niet, dus enkel \(x=4\) blijft over.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\log_{2}5\cdot\log_{5}8\)? Schrijf het getal.",
        antwoord=["3"],
        uitleg=r"\(\log_{2}5\cdot\log_{5}8=\log_{2}8=3\). Het tussengrondtal 5 valt weg; dat is dezelfde regel als het veranderen van grondtal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(y=\log_{a}x\) gaat bij elk toegelaten grondtal door het punt \((1,0)\).",
        antwoord=True,
        uitleg=r"\(a^{0}=1\) voor elk grondtal, dus \(\log_{a}1=0\). Daarom snijden alle logaritmische grafieken de \(x\)-as in \(x=1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(e^{2\ln 3}\).",
        opties=[r"\(9\)", r"\(6\)", r"\(2e^{3}\)", r"\(\ln 9\)"],
        antwoord=0,
        uitleg=r"\(2\ln 3=\ln 3^{2}=\ln 9\), en \(e^{\ln 9}=9\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een belegging groeit met 4 % per jaar: na \(n\) jaar staat ze op \(1{,}04^{n}\) keer het startbedrag. Na hoeveel volle jaren is ze voor het eerst verdubbeld? Schrijf het getal.",
        antwoord=["18"],
        uitleg=r"Los op \(1{,}04^{n}\geq 2\), dus \(n\geq\tfrac{\ln 2}{\ln 1{,}04}\approx 17{,}7\). Na 17 jaar staat ze op \(1{,}95\) keer, na 18 jaar op \(2{,}03\) keer.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\left(\ln x\right)^{2}=2\ln x\).",
        antwoord=False,
        uitleg=r"\(2\ln x\) is \(\ln x^{2}\). Het kwadraat van de logaritme is iets anders: bij \(x=e\) is links \(1\) en rechts \(2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\log_{2}x\) bestaat ook voor \(x=0\).",
        antwoord=False,
        uitleg=r"Geen enkele exponent maakt van 2 het getal 0: \(2^{x}\) is altijd strikt positief. Daarom is \(\left]0,+\infty\right[\) het domein van elke logaritme.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een geluid wordt 100 keer zo intens. Met hoeveel stijgt het geluidsniveau \(L=10\log\dfrac{I}{I_{0}}\)?",
        opties=[r"\(20\) dB", r"\(100\) dB", r"\(2\) dB", r"\(10\) dB"],
        antwoord=0,
        uitleg=r"\(10\log\dfrac{100I}{I_{0}}=10\log 100+10\log\dfrac{I}{I_{0}}=20+L\). Honderd keer zo intens is dus 20 decibel meer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\log_{1/2}8\)?",
        opties=[r"\(-3\)", r"\(3\)", r"\(\tfrac{1}{3}\)", r"\(-\tfrac{1}{3}\)"],
        antwoord=0,
        uitleg=r"\(\left(\tfrac{1}{2}\right)^{-3}=2^{3}=8\), dus de logaritme is \(-3\). Bij een grondtal tussen 0 en 1 daalt de logaritme.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(2^{x+1}=5\cdot 2^{x}-12\). Schrijf het getal.",
        antwoord=["2"],
        uitleg=r"Stel \(t=2^{x}\). Links staat \(2t\), dus \(2t=5t-12\) en \(t=4\). Uit \(2^{x}=4\) volgt \(x=2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waaraan is \(\log_{a}\sqrt[3]{x}\) gelijk?",
        opties=[
            r"\(\tfrac{1}{3}\log_{a}x\)",
            r"\(3\log_{a}x\)",
            r"\(\sqrt[3]{\log_{a}x}\)",
            r"\(\log_{a}x-3\)",
        ],
        antwoord=0,
        uitleg=r"\(\sqrt[3]{x}=x^{1/3}\), en een exponent komt voor de logaritme te staan: \(\tfrac{1}{3}\log_{a}x\).",
    ),
]

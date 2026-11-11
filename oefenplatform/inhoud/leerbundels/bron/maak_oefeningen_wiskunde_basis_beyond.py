# -*- coding: utf-8 -*-
r"""De afdrukbare oefenbundels bij wiskunde basis 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen, andere situaties. Wie hier iets bijschrijft, legt het
eerst naast `../../beyond/wiskunde-basis.json` en naast
`maak_wiskunde_basis_beyond.py`. Wiskunde staat tussen \( en \).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Wiskunde basis"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "110px"
WW = "170px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."
HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf je tussenstappen op. Een antwoord zonder berekening is niet na te kijken.",
    "Gebruik je rekentoestel enkel waar de opgave dat zegt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS["oefenbundel-" + slug + "-beyond-doorstroom"] = b


# ============================================================ 1
zet("machtswortels-machten-en-logaritmen",
    titel="Machtswortels, machten en logaritmen",
    reeksen=[
        dict(kop="Machtswortels", opdracht=r"Bereken zonder rekentoestel. Bestaat het niet in \(\mathbb{R}\), schrijf dan 'bestaat niet'.",
             oefeningen=[
                 ("rij", [(r"\(\sqrt[3]{27}\)", r"\(3\)"), (r"\(\sqrt[5]{32}\)", r"\(2\)"), (r"\(\sqrt[3]{-8}\)", r"\(-2\)"),
                          (r"\(\sqrt[6]{-64}\)", "bestaat niet"), (r"\(\sqrt[4]{625}\)", r"\(5\)")], "Vul in.", W),
             ]),
        dict(kop="Van wortel naar macht en terug", opdracht="Schrijf om (alle letters zijn positief).",
             oefeningen=[
                 ("rij", [(r"\(\sqrt[4]{x^{3}}\)", r"\(x^{\frac{3}{4}}\)"), (r"\(\dfrac{1}{\sqrt{a}}\)", r"\(a^{-\frac{1}{2}}\)"),
                          (r"\(5^{\frac{3}{2}}\) als wortel", r"\(\sqrt{5^{3}}\)"), (r"\(\dfrac{1}{\sqrt[3]{y^{2}}}\)", r"\(y^{-\frac{2}{3}}\)")], "Vul in.", W),
                 ("rij", [(r"\(27^{\frac{2}{3}}\)", r"\(9\)"), (r"\(25^{-\frac{1}{2}}\)", r"\(\frac{1}{5}\)"), (r"\(16^{\frac{3}{4}}\)", r"\(8\)"),
                          (r"\(4^{-\frac{3}{2}}\)", r"\(\frac{1}{8}\)")], "Bereken zonder rekentoestel.", W),
             ]),
        dict(kop="Rekenregels", opdracht="Schrijf als één macht (alle letters zijn positief).",
             oefeningen=[
                 ("rij", [(r"\(x^{\frac{2}{3}}\cdot x^{\frac{1}{6}}\)", r"\(x^{\frac{5}{6}}\)"), (r"\(\dfrac{a^{\frac{7}{4}}}{a^{\frac{3}{4}}}\)", r"\(a\)"),
                          (r"\(\left(b^{\frac{2}{5}}\right)^{5}\)", r"\(b^{2}\)"), (r"\(\sqrt[3]{x}\cdot\sqrt[4]{x}\)", r"\(x^{\frac{7}{12}}=\sqrt[12]{x^{7}}\)")], "Vul in.", WW),
                 ("waar", r"\(\sqrt{36+64}=\sqrt{36}+\sqrt{64}\)", False),
                 ("waar", r"\(\sqrt[3]{4}\cdot\sqrt[3]{16}=4\)", True),
             ]),
        dict(kop="Logaritmen berekenen", opdracht="Bereken zonder rekentoestel.",
             oefeningen=[
                 ("rij", [(r"\(\log_{3}81\)", r"\(4\)"), (r"\(\log 0{,}01\)", r"\(-2\)"), (r"\(\log_{2}\dfrac{1}{8}\)", r"\(-3\)"),
                          (r"\(\log_{9}3\)", r"\(\frac{1}{2}\)"), (r"\(\ln e^{-2}\)", r"\(-2\)"), (r"\(\log_{7}1\)", r"\(0\)")], "Vul in.", W),
                 ("rij", [(r"\(\log_{4}8+\log_{4}2\)", r"\(\log_{4}16=2\)"), (r"\(\log_{3}54-\log_{3}2\)", r"\(\log_{3}27=3\)"),
                          (r"\(\log 4+\log 25\)", r"\(\log 100=2\)")], "Gebruik de rekenregels.", WW),
             ]),
        dict(kop="Met het rekentoestel", opdracht="Rond af op twee cijfers na de komma.",
             oefeningen=[
                 ("kort", r"\(\sqrt[4]{50}\)", r"\(2{,}66\)", W),
                 ("kort", r"\(\log_{5}40\) (schrijf ook de formule)", r"\(\dfrac{\log 40}{\log 5}\approx 2{,}29\)", WL),
                 ("kort", r"Los op: \(3^{x}=20\)", r"\(x=\log_{3}20\approx 2{,}73\)", WL),
                 ("kort", r"Een kubus heeft een inhoud van \(512\ \text{cm}^{3}\). Hoe lang is een ribbe?", r"\(\sqrt[3]{512}=8\) cm", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(\log_{8}2=4\)", False),
                 ("waar", r"\(\log_{a}x^{3}=3\log_{a}x\) voor \(x>0\)", True),
                 ("waar", r"\(\dfrac{\log 9}{\log 3}=\log 3\)", False),
                 ("waar", r"\(\log_{5}(-25)\) bestaat niet in \(\mathbb{R}\)", True),
             ]),
    ])


# ============================================================ 2
zet("grafisch-onderzoek-van-een-functie",
    titel="Grafisch onderzoek van een functie",
    reeksen=[
        dict(kop="Domein en snijpunten", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"domein van \(f(x)=\dfrac{3}{x+5}\)", r"\(\mathbb{R}\setminus\{-5\}\)"),
                          (r"snijpunt met de \(y\)-as van \(f(x)=-2x+8\)", r"\((0,8)\)"),
                          (r"nulwaarde van \(f(x)=-2x+8\)", r"\(4\)"),
                          (r"nulpunt van \(f(x)=-2x+8\)", r"\((4,0)\)"),
                          (r"verticale asymptoot van \(f(x)=\dfrac{1}{x-7}\)", r"\(x=7\)")], "Vul in.", WW),
             ]),
        dict(kop="Een grafiek lezen", opdracht=r"Een functie \(f\) daalt van \(x=-\infty\) tot \(x=-2\), waar \(f(-2)=-3\). Daarna stijgt ze. Ze snijdt de \(x\)-as in \(-5\) en in \(1\).",
             oefeningen=[
                 ("kort", r"Heeft \(f\) een maximum of een minimum? Waar en hoeveel?", r"minimum \(-3\) in \(x=-2\)", WL),
                 ("kort", "Wat is het bereik?", r"\([-3,+\infty[\)", WW),
                 ("tabel", [r"\(x\)", "", r"\(-5\)", "", r"\(1\)", ""], [[r"\(f(x)\)", None, None, None, None, None]],
                  r"\(+\), \(0\), \(-\), \(0\), \(+\)", "40px"),
                 ("kort", r"Voor welke \(x\) is \(f(x)<0\)?", r"\(]-5,1[\)", WW),
             ]),
        dict(kop="Welk verloop?", opdracht="Schrijf: toenemende stijging, afnemende stijging, constante stijging, toenemende daling of afnemende daling.",
             oefeningen=[
                 ("rij", [(r"\(f(0)=3\), \(f(1)=4\), \(f(2)=7\), \(f(3)=12\)", "toenemende stijging"),
                          (r"\(f(0)=50\), \(f(1)=30\), \(f(2)=20\), \(f(3)=15\)", "afnemende daling"),
                          (r"\(f(0)=1\), \(f(1)=5\), \(f(2)=9\), \(f(3)=13\)", "constante stijging"),
                          (r"\(f(0)=0\), \(f(1)=8\), \(f(2)=12\), \(f(3)=14\)", "afnemende stijging")], "Vul in.", WW),
             ]),
        dict(kop="Even of oneven?", opdracht="Schrijf even, oneven of geen van beide.",
             oefeningen=[
                 ("rij", [(r"\(f(x)=x^{4}\)", "even"), (r"\(f(x)=x^{3}-x\)", "oneven"), (r"\(f(x)=x^{2}+x\)", "geen van beide")], "Vul in.", WW),
             ]),
        dict(kop="Een situatie", opdracht=r"Een pijl wordt omhoog geschoten: \(h(t)=40t-5t^{2}\), met \(h\) in meter en \(t\) in seconden, tot de pijl de grond raakt.",
             oefeningen=[
                 ("kort", "Wat is het praktisch domein?", r"\(h(t)=0\) bij \(t=0\) en \(t=8\): \([0,8]\)", WL),
                 ("kort", r"Hoe hoog is de pijl na \(3\) seconden?", r"\(120-45=75\) m", WW),
                 ("kort", "Wat is de grootste hoogte, en wat is het praktisch bereik?", r"\(h(4)=80\) m; \([0,80]\)", WL),
             ]),
        dict(kop="Betekenis in de situatie", opdracht="Wat betekent het kenmerk?",
             oefeningen=[
                 ("open", r"Een fietsverhuur rekent \(P(u)=3u+5\) euro voor \(u\) uur. Wat betekent het snijpunt met de \(y\)-as? Hoeveel uur huur je voor \(26\) euro?",
                  r"De vaste kost van \(5\) euro. \(3u+5=26\), dus \(u=7\) uur.", 2),
                 ("open", r"De temperatuur van thee die afkoelt, komt steeds dichter bij \(20\) °C. Welk kenmerk is dat?",
                  r"Een horizontale asymptoot \(T=20\).", 1),
                 ("open", r"Een reuzenrad brengt je elke \(8\) minuten terug op dezelfde hoogte. Welk kenmerk is dat?", r"De periode: \(8\) minuten.", 1),
             ]),
    ])


# ============================================================ 3
zet("tweedegraadsfuncties",
    titel="Tweedegraadsfuncties",
    reeksen=[
        dict(kop="Top en symmetrieas", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["functie", "dal of berg", "top", "symmetrieas"],
                  [[r"\(2(x+3)^{2}-1\)", None, None, None], [r"\(-(x-4)^{2}+6\)", None, None, None],
                   [r"\(x^{2}+8x+10\)", None, None, None], [r"\(-x^{2}+2x+3\)", None, None, None]],
                  r"dal, \((-3,-1)\), \(x=-3\) · berg, \((4,6)\), \(x=4\) · dal, \((-4,-6)\), \(x=-4\) · berg, \((1,4)\), \(x=1\)", "90px"),
             ]),
        dict(kop="Nulwaarden en bereik", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"nulwaarden van \(f(x)=-3(x+2)(x-6)\)", r"\(-2\) en \(6\)"),
                          (r"\(x\)-coördinaat van de top van die functie", r"\(2\)"),
                          (r"snijpunt met de \(y\)-as van \(2x^{2}-5x-3\)", r"\((0,-3)\)"),
                          (r"bereik van \(f(x)=(x+1)^{2}-4\)", r"\([-4,+\infty[\)"),
                          (r"aantal nulwaarden van \(f(x)=-(x-2)^{2}-1\)", r"geen")], "Vul in.", WW),
                 ("kort", r"Schrijf \((x+3)^{2}-4\) in de vorm \(ax^{2}+bx+c\).", r"\(x^{2}+6x+5\)", WW),
             ]),
        dict(kop="Transformaties", opdracht=r"Schrijf het voorschrift dat je krijgt uit \(f(x)=x^{2}\).",
             oefeningen=[
                 ("rij", [("4 naar links", r"\((x+4)^{2}\)"), ("2 naar beneden", r"\(x^{2}-2\)"),
                          (r"spiegelen rond de \(x\)-as, dan 1 naar rechts", r"\(-(x-1)^{2}\)"),
                          ("verticaal uitrekken met factor 3, dan 5 naar boven", r"\(3x^{2}+5\)")], "Vul in.", WW),
                 ("open", r"Beschrijf de transformaties van \(x^{2}\) naar \(g(x)=-\tfrac{1}{2}(x-3)^{2}+2\).",
                  r"Verschuiving \(3\) naar rechts, verticale samendrukking met factor \(\tfrac{1}{2}\), spiegeling rond de \(x\)-as, verschuiving \(2\) naar boven.", 2),
             ]),
        dict(kop="Een voorschrift opstellen", opdracht="Schrijf je werkwijze op.",
             oefeningen=[
                 ("kort", r"Top \((2,-3)\), door \((0,5)\).", r"\(a(0-2)^{2}-3=5\), \(a=2\): \(f(x)=2(x-2)^{2}-3\)", WL),
                 ("kort", r"Nulwaarden \(-1\) en \(5\), door \((2,18)\).", r"\(a(3)(-3)=18\), \(a=-2\): \(f(x)=-2(x+1)(x-5)\)", WL),
             ]),
        dict(kop="Toepassingen", opdracht="Schrijf je berekening op.",
             oefeningen=[
                 ("kort", r"Een kogel volgt \(h(x)=-0{,}1x^{2}+2x+1{,}5\). Op welke afstand is hij het hoogst, en hoe hoog?", r"\(x=10\) m; \(h(10)=11{,}5\) m", WL),
                 ("kort", r"Met \(60\) m hek zet je een rechthoek af: \(A(x)=x(30-x)\). Grootste oppervlakte?", r"\(x=15\): \(225\ \text{m}^{2}\), een vierkant", WL),
                 ("kort", r"Omzet \(O(p)=-2p^{2}+120p\). Bij welke prijs is de omzet het grootst, en hoeveel is ze dan?", r"\(p=30\) euro; \(O(30)=1800\) euro", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De parabool \(5x^{2}\) is breder dan \(x^{2}\).", False),
                 ("waar", r"\(x^{2}-10x+25\) raakt de \(x\)-as in één punt.", True),
                 ("waar", r"De top van \((x+6)^{2}\) ligt \(6\) eenheden rechts van die van \(x^{2}\).", False),
             ]),
    ])


# ============================================================ 4
zet("tweedegraadsvergelijkingen-algebraisch-oplossen",
    titel="Tweedegraadsvergelijkingen algebraïsch oplossen",
    reeksen=[
        dict(kop="Onvolledige vergelijkingen", opdracht="Los op zonder discriminant. Schrijf de oplossingsverzameling.",
             oefeningen=[
                 ("rij", [(r"\(x^{2}=81\)", r"\(V=\{-9,9\}\)"), (r"\(5x^{2}-20=0\)", r"\(V=\{-2,2\}\)"),
                          (r"\(x^{2}+16=0\)", r"\(V=\varnothing\)"), (r"\(x^{2}+7x=0\)", r"\(V=\{-7,0\}\)"),
                          (r"\(2x^{2}=8x\)", r"\(V=\{0,4\}\)")], "Vul in.", WW),
             ]),
        dict(kop="De discriminant", opdracht=r"Bereken \(D\) en zeg hoeveel oplossingen er zijn.",
             oefeningen=[
                 ("tabel", ["vergelijking", r"\(D\)", "aantal oplossingen"],
                  [[r"\(x^{2}-4x+3=0\)", None, None], [r"\(x^{2}+10x+25=0\)", None, None], [r"\(3x^{2}+x+2=0\)", None, None]],
                  r"\(4\), twee · \(0\), één · \(-23\), geen", "80px"),
                 ("kort", r"Voor welke \(c\) heeft \(x^{2}-6x+c=0\) precies één oplossing?", r"\(36-4c=0\), \(c=9\)", WW),
             ]),
        dict(kop="Oplossen", opdracht="Los op met de discriminant of door te ontbinden.",
             oefeningen=[
                 ("rij", [(r"\(x^{2}-x-12=0\)", r"\(V=\{-3,4\}\)"), (r"\(2x^{2}-5x+2=0\)", r"\(V=\left\{\tfrac{1}{2},2\right\}\)"),
                          (r"\(x^{2}+8x+15=0\)", r"\(V=\{-5,-3\}\)"), (r"\((x+2)^{2}=25\)", r"\(V=\{-7,3\}\)"),
                          (r"\(x^{2}-2x-5=0\) (op twee cijfers na de komma)", r"\(3{,}45\) en \(-1{,}45\)")], "Vul in.", WW),
                 ("rij", [(r"\(x^{2}-49\)", r"\((x-7)(x+7)\)"), (r"\(x^{2}-9x+20\)", r"\((x-4)(x-5)\)"), (r"\(x^{2}+x-6\)", r"\((x+3)(x-2)\)")],
                  "Ontbind in factoren.", WW),
             ]),
        dict(kop="Snijpunten", opdracht="Bereken de snijpunten van de grafieken.",
             oefeningen=[
                 ("kort", r"\(f(x)=x^{2}\) en \(g(x)=2x+3\)", r"\(x^{2}-2x-3=0\): \((-1,1)\) en \((3,9)\)", WL),
                 ("kort", r"\(f(x)=x^{2}+4\) en \(g(x)=4x\)", r"\((x-2)^{2}=0\): ze raken in \((2,8)\)", WL),
             ]),
        dict(kop="Vraagstukken", opdracht="Stel een vergelijking op en los op. Controleer of je antwoord zin heeft.",
             oefeningen=[
                 ("open", r"Een rechthoek is \(4\) m langer dan breed en heeft een oppervlakte van \(60\ \text{m}^{2}\). Hoe breed is hij?",
                  r"\(x(x+4)=60\), \(x^{2}+4x-60=0\), \(x=6\) of \(x=-10\). De breedte is \(6\) m.", 3),
                 ("open", r"Een duiker springt van een rots: \(h(t)=-5t^{2}+5t+10\). Na hoeveel seconden raakt hij het water?",
                  r"\(-5t^{2}+5t+10=0\), \(t^{2}-t-2=0\), \(t=2\) of \(t=-1\). Na \(2\) s.", 3),
                 ("open", r"Winst \(W(q)=-q^{2}+60q-500\). Bij welke aantallen is de winst nul?",
                  r"\(q^{2}-60q+500=0\), \(D=1600\), \(q=10\) of \(q=50\).", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Bij \(x^{2}=6x\) mag je door \(x\) delen.", False),
                 ("waar", r"\((x-3)(x+1)=5\) heeft als oplossingen \(3\) en \(-1\).", False),
                 ("waar", r"Als \(D<0\), dan snijdt de parabool de \(x\)-as niet.", True),
             ]),
    ])


# ============================================================ 5
zet("exponentiele-functies-en-groeimodellen",
    titel="Exponentiële functies en groeimodellen",
    reeksen=[
        dict(kop="Kenmerken", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["functie", "stijgend of dalend", "asymptoot", "bereik", r"snijpunt \(y\)-as"],
                  [[r"\(4^{x}\)", None, None, None, None], [r"\(\left(\tfrac{1}{3}\right)^{x}\)", None, None, None, None],
                   [r"\(2\cdot 3^{x}-5\)", None, None, None, None], [r"\(-2^{x}+1\)", None, None, None, None]],
                  r"stijgend, \(y=0\), \(]0,+\infty[\), \((0,1)\) · dalend, \(y=0\), \(]0,+\infty[\), \((0,1)\) · stijgend, \(y=-5\), \(]-5,+\infty[\), \((0,-3)\) · dalend, \(y=1\), \(]-\infty,1[\), \((0,0)\)", "80px"),
             ]),
        dict(kop="Voorschriften", opdracht="Vul in.",
             oefeningen=[
                 ("kort", r"De grafiek van \(a^{x}\) gaat door \((2,25)\). Hoeveel is \(a\)?", r"\(a=5\)", W),
                 ("kort", r"Tabel: \(f(0)=2\), \(f(1)=8\), \(f(2)=32\), \(f(3)=128\). Voorschrift?", r"\(f(x)=2\cdot 4^{x}\)", WW),
                 ("kort", r"\(5^{x}\) verticaal uitrekken met factor \(2\) en \(3\) naar boven. Voorschrift?", r"\(2\cdot 5^{x}+3\)", WW),
                 ("kort", r"Bij welke \(c\) heeft \(3^{x}+c\) de nulwaarde \(2\)?", r"\(9+c=0\), \(c=-9\)", WW),
             ]),
        dict(kop="Groeifactoren", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"\(+6\%\) per jaar", r"\(1{,}06\)"), (r"\(-20\%\) per jaar", r"\(0{,}8\)"), (r"groeifactor \(1{,}125\)", r"\(+12{,}5\%\)"),
                          (r"groeifactor \(0{,}97\)", r"\(-3\%\)")], "Vul in.", W),
                 ("kort", r"\(44\%\) groei per twee jaar. Groeifactor per jaar?", r"\(\sqrt{1{,}44}=1{,}2\)", WW),
                 ("kort", r"\(1{,}01\) per maand. Groeifactor per jaar (drie cijfers na de komma)?", r"\(1{,}01^{12}\approx 1{,}127\)", WW),
             ]),
        dict(kop="Welke groei?", opdracht="Schrijf lineair, exponentieel (met groeifactor) of geen van beide.",
             oefeningen=[
                 ("rij", [(r"\(40, 34, 28, 22\)", "lineair"), (r"\(40, 20, 10, 5\)", r"exponentieel, \(g=0{,}5\)"),
                          (r"\(2, 3, 5, 9\)", "geen van beide"), (r"\(200, 220, 242, 266{,}2\)", r"exponentieel, \(g=1{,}1\)")], "Vul in.", WW),
             ]),
        dict(kop="Toepassingen", opdracht="Schrijf je berekening op.",
             oefeningen=[
                 ("kort", r"Je zet \(5000\) euro vast aan \(2{,}5\%\) samengestelde intrest. Voorschrift en bedrag na \(10\) jaar?", r"\(B(t)=5000\cdot 1{,}025^{t}\); \(\approx 6400{,}42\) euro", WL),
                 ("kort", r"Een smartphone van \(900\) euro verliest elk jaar \(30\%\) waarde. Waarde na \(3\) jaar?", r"\(900\cdot 0{,}7^{3}=308{,}70\) euro", WL),
                 ("kort", r"Halveringstijd \(5\) jaar, start \(240\) g. Hoeveel na \(20\) jaar?", r"\(240\to 120\to 60\to 30\to 15\) g", WL),
                 ("kort", r"Verdubbelingstijd bij \(8\%\) groei per jaar (één cijfer na de komma)?", r"\(\log_{1{,}08}2\approx 9{,}0\) jaar", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De grafiek van \(5^{x}\) snijdt de \(x\)-as.", False),
                 ("waar", r"\(3\cdot 2^{x}\) en \(6^{x}\) zijn dezelfde functie.", False),
                 ("waar", r"Bij enkelvoudige intrest groeit het kapitaal lineair.", True),
                 ("waar", r"Hoe groter de beginwaarde, hoe langer de verdubbelingstijd.", False),
             ]),
    ])


# ============================================================ 6
zet("de-sinusfunctie-en-de-goniometrische-cirkel",
    titel="De sinusfunctie en de goniometrische cirkel",
    reeksen=[
        dict(kop="Graden en radialen", opdracht="Zet om.",
             oefeningen=[
                 ("rij", [(r"\(90°\)", r"\(\frac{\pi}{2}\)"), (r"\(120°\)", r"\(\frac{2\pi}{3}\)"), (r"\(\frac{\pi}{4}\)", r"\(45°\)"),
                          (r"\(\frac{5\pi}{6}\)", r"\(150°\)"), (r"\(2\) rad (op een graad)", r"\(115°\)")], "Vul in.", W),
             ]),
        dict(kop="De goniometrische cirkel", opdracht="Vul in zonder rekentoestel.",
             oefeningen=[
                 ("rij", [(r"\(\sin\frac{3\pi}{2}\)", r"\(-1\)"), (r"\(\sin 0\)", r"\(0\)"), (r"\(\sin\frac{5\pi}{6}\)", r"\(\frac{1}{2}\)"),
                          (r"kwadrant van \(\frac{7\pi}{4}\)", "vierde"), (r"teken van \(\sin\frac{4\pi}{3}\)", r"\(-\)")], "Vul in.", W),
                 ("kort", r"Geef een tweede hoek in \([0,2\pi]\) met dezelfde sinus als \(\frac{\pi}{3}\).", r"\(\frac{2\pi}{3}\)", W),
                 ("kort", r"Bereken met je rekentoestel \(\sin 1\) (radialen, twee cijfers na de komma).", r"\(0{,}84\)", W),
             ]),
        dict(kop="Kenmerken van sinusfuncties", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["functie", "amplitude", "evenwichtslijn", "periode", "bereik"],
                  [[r"\(2\sin x-1\)", None, None, None, None], [r"\(\sin 3x\)", None, None, None, None],
                   [r"\(4\sin\frac{1}{2}x+6\)", None, None, None, None], [r"\(-3\sin x\)", None, None, None, None]],
                  r"\(2\), \(y=-1\), \(2\pi\), \([-3,1]\) · \(1\), \(y=0\), \(\frac{2\pi}{3}\), \([-1,1]\) · \(4\), \(y=6\), \(4\pi\), \([2,10]\) · \(3\), \(y=0\), \(2\pi\), \([-3,3]\)", "70px"),
                 ("kort", r"Wat is de faseverschuiving van \(\sin\left(x+\frac{\pi}{4}\right)\)?", r"\(\frac{\pi}{4}\) naar links", WW),
                 ("kort", r"Maximum van \(3\sin 2(x-1)+4\)?", r"\(7\)", W),
             ]),
        dict(kop="Periodieke situaties", opdracht="Schrijf je berekening op.",
             oefeningen=[
                 ("kort", r"Een sinusfunctie heeft maximum \(14\) en minimum \(6\). Evenwichtslijn en amplitude?", r"\(y=10\), amplitude \(4\)", WL),
                 ("kort", r"Het getij: hoogst \(4{,}5\) m, laagst \(0{,}5\) m, periode \(12{,}5\) uur. Amplitude, evenwichtslijn en \(b\)?", r"\(2\), \(2{,}5\), \(b=\frac{2\pi}{12{,}5}\approx 0{,}50\)", WL),
                 ("kort", r"Een reuzenrad: diameter \(30\) m, as op \(18\) m. Hoogste en laagste punt van een bakje?", r"\(33\) m en \(3\) m", WL),
                 ("kort", r"Een slinger zwaait \(5\) keer heen en terug in \(10\) s. Periode en frequentie?", r"\(2\) s; \(0{,}5\) per seconde", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De sinus van een hoek in het tweede kwadrant is positief.", True),
                 ("waar", r"\(\sin(x+2\pi)=\sin x\)", True),
                 ("waar", r"Een verticale verschuiving verandert de periode.", False),
                 ("waar", r"\(\sin 2x\) heeft periode \(4\pi\).", False),
             ]),
    ])


# ============================================================ 7
zet("vergelijkingen-grafisch-oplossen",
    titel="Vergelijkingen grafisch oplossen",
    reeksen=[
        dict(kop="Aflezen", opdracht=r"Schrijf de oplossingenverzameling \(V\).",
             oefeningen=[
                 ("rij", [(r"De grafieken van \(f\) en \(g\) snijden in \((-3,1)\) en \((4,8)\). \(f(x)=g(x)\)?", r"\(V=\{-3,4\}\)"),
                          (r"\(f\) snijdt de \(x\)-as in \(-1\), \(2\) en \(5\). \(f(x)=0\)?", r"\(V=\{-1,2,5\}\)"),
                          (r"De grafieken van \(f\) en \(g\) snijden elkaar niet. \(f(x)=g(x)\)?", r"\(V=\varnothing\)")], "Vul in.", WW),
             ]),
        dict(kop="Welke grafieken?", opdracht="Welke twee grafieken teken je om de vergelijking op te lossen?",
             oefeningen=[
                 ("rij", [(r"\(x^{3}+x=4\)", r"\(y=x^{3}+x\) en \(y=4\)"), (r"\(2^{x}=x+3\)", r"\(y=2^{x}\) en \(y=x+3\)"),
                          (r"\(\sin x=0{,}8\)", r"\(y=\sin x\) en \(y=0{,}8\)")], "Vul in.", WL),
             ]),
        dict(kop="Hoeveel oplossingen?", opdracht="Schrijf het aantal en leg kort uit.",
             oefeningen=[
                 ("rij", [(r"\(3^{x}=-1\)", r"geen: \(3^{x}>0\)"), (r"\(\sin x=-1{,}5\)", r"geen: \(\sin x\geq -1\)"),
                          (r"\(\sin x=-\frac{1}{2}\) op \([0,2\pi]\)", "twee"), (r"\(4\cdot 2^{x}=32\)", r"één: \(x=3\)"),
                          (r"\(\sin x=0{,}9\) op \(\mathbb{R}\)", "oneindig veel")], "Vul in.", WW),
             ]),
        dict(kop="Vraagstukken", opdracht="Stel de vergelijking op, los op (met een rekenapp mag) en formuleer het antwoord in een zin.",
             oefeningen=[
                 ("open", r"Je zet \(2000\) euro vast aan \(3\%\) per jaar. Na hoeveel jaar staat er voor het eerst meer dan \(2500\) euro?",
                  r"\(2000\cdot 1{,}03^{t}=2500\), \(t\approx 7{,}55\). Na \(8\) jaar staat er voor het eerst meer dan \(2500\) euro.", 3),
                 ("open", r"Een bacteriekolonie: \(N(t)=50\cdot 2^{t}\) na \(t\) uur. Wanneer zijn er \(800\) bacteriën?",
                  r"\(50\cdot 2^{t}=800\), \(2^{t}=16\), \(t=4\) uur.", 2),
                 ("open", r"Fitness A: \(25\) euro per maand plus \(2\) euro per bezoek. Fitness B: \(5\) euro per bezoek. Vanaf hoeveel bezoeken per maand is A goedkoper?",
                  r"\(25+2x=5x\), \(x\approx 8{,}33\). Vanaf \(9\) bezoeken is A goedkoper.", 3),
                 ("open", r"Een doos uit karton van \(16\) bij \(16\) cm: \(I(x)=x(16-2x)^{2}\). Een app geeft voor \(I(x)=288\): \(x=2\), \(x\approx 3{,}53\) en \(x\approx 10{,}47\). Welke oplossingen passen?",
                  r"Enkel \(2\) en \(3{,}53\): \(x\) moet kleiner zijn dan \(8\).", 2),
             ]),
        dict(kop="Periodiek", opdracht=r"De hoogte van een bakje: \(h(t)=12\sin\left(\frac{\pi}{5}t\right)+14\) m, \(t\) in minuten.",
             oefeningen=[
                 ("kort", "Hoe lang duurt één toer?", r"\(\frac{2\pi}{\pi/5}=10\) min", WW),
                 ("kort", "Hoogste en laagste punt?", r"\(26\) m en \(2\) m", WW),
                 ("kort", r"Hoe vaak per toer is het bakje op \(14\) m?", "twee keer", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Een derdegraadsvergelijking heeft altijd drie oplossingen.", False),
                 ("waar", r"Een grafiek die de rechte \(y=2\) raakt, levert een oplossing van \(f(x)=2\).", True),
                 ("waar", r"Elke oplossing van de vergelijking is ook een antwoord op het vraagstuk.", False),
             ]),
    ])


# ============================================================ 8
zet("afgeleiden-helling-en-raaklijn",
    titel="Afgeleiden: helling en raaklijn",
    reeksen=[
        dict(kop="Gemiddelde verandering", opdracht="Bereken het differentiequotiënt.",
             oefeningen=[
                 ("rij", [(r"\(f(x)=x^{2}\) over \([2,5]\)", r"\(\frac{25-4}{3}=7\)"), (r"\(f(x)=3x-1\) over \([0,10]\)", r"\(3\)"),
                          (r"\(f(x)=x^{3}\) over \([-1,2]\)", r"\(\frac{8+1}{3}=3\)"), (r"\(f(x)=3^{x}\) over \([0,2]\)", r"\(\frac{9-1}{2}=4\)")], "Vul in.", WW),
                 ("kort", r"Een trein is na \(1\) uur op \(120\) km, na \(4\) uur op \(480\) km. Gemiddelde snelheid?", r"\(120\) km/h", WW),
             ]),
        dict(kop="De afgeleide uit een tabel", opdracht=r"Differentiequotiënten over \([3,3+h]\): \(h=0{,}1\): \(6{,}1\); \(h=0{,}01\): \(6{,}01\); \(h=0{,}001\): \(6{,}001\).",
             oefeningen=[
                 ("kort", r"Hoeveel is \(f'(3)\)?", r"\(6\)", W),
                 ("kort", r"Stijgt of daalt \(f\) in de buurt van \(x=3\)?", "stijgt", W),
             ]),
        dict(kop="Raaklijnen", opdracht="Schrijf de vergelijking van de raaklijn.",
             oefeningen=[
                 ("rij", [(r"\(f(1)=2\), \(f'(1)=4\)", r"\(y=4x-2\)"), (r"\(f(3)=-1\), \(f'(3)=-2\)", r"\(y=-2x+5\)"),
                          (r"\(f(0)=7\), \(f'(0)=0\)", r"\(y=7\)")], "Vul in.", WW),
                 ("kort", r"De raaklijn in \(x=2\) gaat door \((2,1)\) en \((4,-5)\). Hoeveel is \(f'(2)\)?", r"\(-3\)", W),
             ]),
        dict(kop="Betekenis", opdracht="Wat betekent het? Schrijf een zin met de eenheid.",
             oefeningen=[
                 ("open", r"\(s(t)\) is de afgelegde weg van een loper in meter na \(t\) seconden. \(s'(20)=4\).", r"Na \(20\) seconden loopt de loper \(4\) m/s.", 1),
                 ("open", r"\(K(q)\) is de kost in euro voor \(q\) stoelen. \(K'(100)=35\).", r"De marginale kost bij \(100\) stoelen is \(35\) euro: een stoel extra kost ongeveer \(35\) euro.", 2),
                 ("open", r"\(v(t)=0\) op \(t=5\).", r"Op \(t=5\) staat het voorwerp even stil.", 1),
             ]),
        dict(kop="De hellinggrafiek", opdracht=r"Lees het tekenverloop van \(f'\) en beantwoord de vragen.",
             oefeningen=[
                 ("tekst", r'<table class="invul"><tr><th>\(x\)</th><th></th><th>\(-3\)</th><th></th><th>\(1\)</th><th></th></tr>'
                           r'<tr><th>\(f^{\prime}(x)\)</th><td>\(-\)</td><td>\(0\)</td><td>\(+\)</td><td>\(0\)</td><td>\(-\)</td></tr></table>'),
                 ("kort", r"Waar stijgt \(f\)?", r"\([-3,1]\)", WW),
                 ("kort", r"Waar heeft \(f\) een minimum, waar een maximum?", r"minimum in \(-3\), maximum in \(1\)", WL),
                 ("kort", r"\(f\) is een bergparabool met top in \(x=-2\). Hoe ziet de hellinggrafiek eruit?", r"een dalende rechte die de \(x\)-as snijdt in \(-2\)", WL),
                 ("kort", r"Op een interval is \(f'\) positief en dalend. Hoe verloopt \(f\)?", "afnemende stijging", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"In de top van een parabool is de raaklijn horizontaal.", True),
                 ("waar", r"Als \(f'(2)=0\), dan heeft \(f\) zeker een extremum in \(2\).", False),
                 ("waar", r"\(f(x)=x^{2}\) en \(g(x)=x^{2}+5\) hebben dezelfde hellinggrafiek.", True),
                 ("waar", r"Waar \(f\) een nulwaarde heeft, is \(f'=0\).", False),
             ]),
    ])


# ============================================================ 9
zet("rekenkundige-en-meetkundige-rijen",
    titel="Rekenkundige en meetkundige rijen",
    reeksen=[
        dict(kop="Welke rij?", opdracht=r"Schrijf rekenkundig (met \(v\)), meetkundig (met \(q\)) of geen van beide.",
             oefeningen=[
                 ("rij", [(r"\(7, 11, 15, 19\)", r"rekenkundig, \(v=4\)"), (r"\(5, 15, 45, 135\)", r"meetkundig, \(q=3\)"),
                          (r"\(64, 16, 4, 1\)", r"meetkundig, \(q=\frac{1}{4}\)"), (r"\(1, 4, 9, 16\)", "geen van beide"),
                          (r"\(20, 17{,}5, 15, 12{,}5\)", r"rekenkundig, \(v=-2{,}5\)")], "Vul in.", WW),
             ]),
        dict(kop="Rekenkundige rijen", opdracht=r"De rij \(4, 10, 16, 22,\dots\)",
             oefeningen=[
                 ("kort", "Recursief voorschrift?", r"\(u_{1}=4\), \(u_{n+1}=u_{n}+6\)", WL),
                 ("kort", "Expliciet voorschrift?", r"\(u_{n}=4+(n-1)\cdot 6\)", WL),
                 ("kort", r"\(u_{30}\)?", r"\(4+29\cdot 6=178\)", WW),
                 ("kort", r"Som van de eerste \(30\) termen?", r"\(30\cdot\frac{4+178}{2}=2730\)", WW),
                 ("kort", r"Een rekenkundige rij heeft \(u_{1}=3\) en \(u_{9}=43\). Verschil?", r"\(3+8v=43\), \(v=5\)", WW),
                 ("kort", r"\(2+4+6+\dots+200\)?", r"\(100\cdot\frac{2+200}{2}=10\,100\)", WW),
             ]),
        dict(kop="Meetkundige rijen", opdracht=r"De rij \(2, 6, 18, 54,\dots\)",
             oefeningen=[
                 ("kort", "Reden en expliciet voorschrift?", r"\(q=3\); \(u_{n}=2\cdot 3^{n-1}\)", WL),
                 ("kort", r"\(u_{7}\)?", r"\(2\cdot 3^{6}=1458\)", WW),
                 ("kort", r"Som van de eerste \(7\) termen?", r"\(2\cdot\frac{1-3^{7}}{1-3}=2186\)", WW),
                 ("kort", r"Een meetkundige rij heeft \(u_{1}=5\) en \(u_{3}=80\) (positieve termen). Reden?", r"\(5q^{2}=80\), \(q=4\)", WW),
             ]),
        dict(kop="Toepassingen", opdracht="Rekenkundig of meetkundig? Bereken.",
             oefeningen=[
                 ("open", r"Een amfitheater heeft \(20\) stoelen op de eerste rij en telkens \(3\) meer. Hoeveel stoelen op rij \(15\), en hoeveel op de eerste \(15\) rijen?",
                  r"Rekenkundig: \(u_{15}=20+14\cdot 3=62\); \(s_{15}=15\cdot\frac{20+62}{2}=615\).", 2),
                 ("open", r"Je zet \(2500\) euro aan \(3\%\) samengestelde intrest. Hoeveel na \(4\) jaar (op een cent)?",
                  r"Meetkundig met \(q=1{,}03\): \(2500\cdot 1{,}03^{4}\approx 2813{,}77\) euro.", 2),
                 ("open", r"Een bal valt van \(5\) m en botst telkens terug tot \(60\%\). Hoe hoog na de vierde bots?",
                  r"\(5\cdot 0{,}6^{4}=0{,}648\) m.", 2),
                 ("open", r"Een kettingbericht: elke ontvanger stuurt het naar \(4\) nieuwe mensen. Ronde \(1\) bereikt \(4\) mensen. Hoeveel in ronde \(5\), en samen?",
                  r"\(4^{5}=1024\); samen \(4+16+64+256+1024=1364\).", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(u_{n}=10-3n\) is een stijgende rij.", False),
                 ("waar", r"In een rekenkundige rij is elke term het gemiddelde van zijn buren.", True),
                 ("waar", r"Een meetkundige rij met \(u_{1}=8\) en \(q=0{,}5\) is dalend.", True),
             ]),
    ])


# ============================================================ 10
zet("kansrekenen-met-kansbomen-en-kruistabellen",
    titel="Kansrekenen met kansbomen en kruistabellen",
    reeksen=[
        dict(kop="Laplace en complement", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [(r"\(P(\text{meer dan }4)\) met een dobbelsteen", r"\(\frac{2}{6}=\frac{1}{3}\)"),
                          (r"\(P(\text{harten})\) uit \(52\) kaarten", r"\(\frac{13}{52}=\frac{1}{4}\)"),
                          (r"\(P(\text{geel})\): \(4\) gele, \(6\) rode, \(10\) blauwe knikkers", r"\(\frac{4}{20}=0{,}2\)"),
                          (r"\(P(\text{geen regen})\) als \(P(\text{regen})=0{,}35\)", r"\(0{,}65\)")], "Vul in.", W),
             ]),
        dict(kop="Frequenties", opdracht="Bereken.",
             oefeningen=[
                 ("kort", r"Een punaise valt \(130\) keer op haar kop bij \(250\) worpen. Relatieve frequentie?", r"\(0{,}52\)", W),
                 ("kort", r"Kans op een prijs is \(0{,}15\). Hoeveel prijzen verwacht je bij \(400\) loten?", r"\(60\)", W),
             ]),
        dict(kop="Een kruistabel", opdracht=r"Een enquête bij \(400\) jongeren.",
             oefeningen=[
                 ("tekst", r'<table class="invul"><tr><th></th><th>bijbaan</th><th>geen bijbaan</th><th>totaal</th></tr>'
                           r'<tr><th>5de jaar</th><td>90</td><td>110</td><td>200</td></tr>'
                           r'<tr><th>6de jaar</th><td>130</td><td>70</td><td>200</td></tr>'
                           r'<tr><th>totaal</th><td>220</td><td>180</td><td>400</td></tr></table>'),
                 ("kort", r"\(P(\text{bijbaan})\)?", r"\(\frac{220}{400}=0{,}55\)", WW),
                 ("kort", r"\(P(\text{bijbaan}\mid\text{6de jaar})\)?", r"\(\frac{130}{200}=0{,}65\)", WW),
                 ("kort", r"\(P(\text{6de jaar}\mid\text{bijbaan})\)?", r"\(\frac{130}{220}\approx 0{,}59\)", WW),
             ]),
        dict(kop="Kansbomen", opdracht="Teken een kansboom op een kladblad en bereken.",
             oefeningen=[
                 ("kort", r"Een zak met \(4\) rode en \(6\) witte ballen. Twee rode, zonder terugleggen?", r"\(\frac{4}{10}\cdot\frac{3}{9}=\frac{2}{15}\)", WL),
                 ("kort", r"Dezelfde zak, twee rode, met terugleggen?", r"\(0{,}4\cdot 0{,}4=0{,}16\)", WL),
                 ("kort", r"Precies één rode, zonder terugleggen?", r"\(\frac{4}{10}\cdot\frac{6}{9}+\frac{6}{10}\cdot\frac{4}{9}=\frac{8}{15}\)", WL),
                 ("kort", r"Minstens één zes bij vier worpen (twee cijfers na de komma)?", r"\(1-\left(\frac{5}{6}\right)^{4}\approx 0{,}52\)", WL),
                 ("kort", r"Een penaltynemer scoort met kans \(0{,}8\). Twee penalty's: minstens één goal?", r"\(1-0{,}2^{2}=0{,}96\)", WL),
             ]),
        dict(kop="Een test", opdracht=r"\(5\%\) van de kippen is ziek. Een test is positief bij \(90\%\) van de zieke en bij \(20\%\) van de gezonde kippen.",
             oefeningen=[
                 ("kort", "Kans op ziek én positief?", r"\(0{,}05\cdot 0{,}9=0{,}045\)", WL),
                 ("kort", "Kans op een positieve test?", r"\(0{,}045+0{,}95\cdot 0{,}2=0{,}235\)", WL),
                 ("kort", "Kans dat een positief geteste kip echt ziek is?", r"\(\frac{0{,}045}{0{,}235}\approx 0{,}19\)", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Na drie keer munt is de kans op kop bij de volgende worp groter dan \(\frac{1}{2}\).", False),
                 ("waar", r"\(P(A\mid B)\) is altijd gelijk aan \(P(B\mid A)\).", False),
                 ("waar", r"De paden van een volledige kansboom tellen samen op tot \(1\).", True),
             ]),
    ])


# ============================================================ 11
zet("steekproeven-samenhang-en-causaliteit",
    titel="Steekproeven, samenhang en causaliteit",
    reeksen=[
        dict(kop="Populatie en variabele", opdracht=r"Een gemeente wil weten hoeveel kilometer haar inwoners per week fietsen. Ze bevraagt \(600\) inwoners.",
             oefeningen=[
                 ("kort", "Wat is de populatie?", "alle inwoners van de gemeente", WL),
                 ("kort", "Wat is de variabele?", "het aantal gefietste kilometer per week", WL),
                 ("open", "Beschrijf hoe je een enkelvoudig aselecte steekproef trekt.", r"Alle inwoners uit het bevolkingsregister nummeren en met een toevalsgenerator \(600\) verschillende nummers trekken.", 2),
             ]),
        dict(kop="Welke steekproef?", opdracht="Schrijf: EAS, vrijwillige respons of opportunistisch. Is ze representatief?",
             oefeningen=[
                 ("rij", [("Je bevraagt de mensen op het fietspad aan het station", "opportunistisch, niet representatief"),
                          ("Een radiozender vraagt luisteraars om te sms'en", "vrijwillige respons, niet representatief"),
                          ("Een computer kiest willekeurig 600 namen uit het register", "EAS, representatief")], "Vul in.", WL),
             ]),
        dict(kop="Welke fout?", opdracht="Steekproeffout of niet-steekproeffout? Helpt een grotere steekproef?",
             oefeningen=[
                 ("rij", [("De vraag luidt: 'Vindt u ook dat de dure parkeerplaatsen weg moeten?'", "niet-steekproeffout, helpt niet"),
                          ("Twee aselecte steekproeven geven 42 km en 45 km", "steekproeffout, helpt wel"),
                          ("Veel mensen geven minder alcoholgebruik op dan echt", "niet-steekproeffout, helpt niet")], "Vul in.", WL),
             ]),
        dict(kop="Samenhang of causaliteit?", opdracht="Geef de beste verklaring: derde variabele (welke?), omwisseling van oorzaak en gevolg, toeval of causaliteit.",
             oefeningen=[
                 ("open", "Hoe meer zonnebrandcrème er verkocht wordt, hoe meer mensen zonnebrand oplopen.", "Derde variabele: zonnig weer.", 1),
                 ("open", "Steden met meer politieagenten hebben meer misdaad.", "Omwisseling of derde variabele: steden met veel misdaad zetten meer agenten in; ook de grootte van de stad speelt.", 2),
                 ("open", "Hoe meer water je in een plantje giet (tot een grens), hoe sneller het groeit.", "Causaliteit (aan te tonen met een experiment).", 1),
                 ("open", "Het aantal piraten daalt en de aarde warmt op.", "Toeval.", 1),
                 ("open", "Hoe zou je onderzoeken of een nieuwe leermethode echt betere punten geeft?", "Met een experiment: het toeval beslist welke leerlingen de nieuwe methode krijgen, de anderen krijgen de oude; daarna vergelijk je.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een grotere steekproef lost een sturende vraag op.", False),
                 ("waar", "Randomisatie betekent dat het toeval kiest wie meedoet.", True),
                 ("waar", "Een sterke samenhang bewijst dat de ene variabele de andere veroorzaakt.", False),
             ]),
    ])


# ============================================================ 12
zet("de-normale-verdeling",
    titel="De normale verdeling",
    reeksen=[
        dict(kop="De kromme", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"De top van \(N(42,3)\) ligt boven", r"\(42\)"),
                          (r"Welke is hoger: \(N(20,5)\) of \(N(20,1)\)?", r"\(N(20,1)\)"),
                          (r"Oppervlakte onder elke Gausskromme", r"\(1\)"),
                          (r"Een app geeft \(\bar{x}=64{,}2\) en \(s=3{,}1\) bij een klokvormig histogram. Model?", r"\(N(64{,}2;\ 3{,}1)\)")], "Vul in.", WW),
             ]),
        dict(kop="Vuistregels", opdracht=r"IQ-scores zijn \(N(100,15)\). Gebruik de vuistregels \(68\%\) en \(95\%\).",
             oefeningen=[
                 ("rij", [(r"\(P(85<X<115)\)", r"\(0{,}68\)"), (r"\(P(70<X<130)\)", r"\(0{,}95\)"), (r"\(P(X<100)\)", r"\(0{,}5\)"),
                          (r"\(P(X>115)\)", r"\(0{,}16\)"), (r"\(P(X<70)\)", r"\(0{,}025\)"), (r"\(P(100<X<130)\)", r"\(0{,}475\)")], "Vul in.", W),
             ]),
        dict(kop="Een productieproces", opdracht=r"Zakken chips wegen \(N(150,3)\) gram. Een app geeft \(P(X<144)\approx 0{,}0228\).",
             oefeningen=[
                 ("kort", r"Wat betekent dat in een zin?", r"Ongeveer \(2{,}3\%\) van de zakken weegt minder dan \(144\) g.", WL),
                 ("kort", r"Hoeveel zakken van \(5000\) verwacht je onder \(144\) g?", r"ongeveer \(114\)", WW),
                 ("kort", r"\(P(X>144)\)?", r"\(0{,}9772\)", WW),
                 ("kort", r"\(P(144<X<156)\)?", r"\(1-2\cdot 0{,}0228=0{,}9544\)", WW),
                 ("kort", r"Wat geef je in de app in om \(P(X<147)\) te berekenen?", r"grens \(147\), gemiddelde \(150\), standaardafwijking \(3\)", WL),
             ]),
        dict(kop="Interpreteren", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", r"Toetsresultaten zijn \(N(70,8)\). Sam haalt \(54\). Wat zeg je over zijn plaats?", r"\(54=\mu-2\sigma\): hij zit bij de zwakste \(2{,}5\%\).", 2),
                 ("open", r"Een app geeft bij \(N(150,3)\) en kans \(0{,}05\) links de waarde \(145{,}1\). Wat betekent dat?", r"\(5\%\) van de zakken weegt minder dan ongeveer \(145{,}1\) g.", 2),
                 ("open", "Waarom is de normale verdeling geen goed model voor de huizenprijzen in België?", "Die verdeling is niet symmetrisch: ze heeft een lange staart naar rechts (enkele zeer dure huizen).", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Bij een grotere standaardafwijking wordt de kromme smaller.", False),
                 ("waar", r"\(P(X>a)=1-P(X<a)\)", True),
                 ("waar", r"De hoogte van de kromme in \(a\) is de kans dat \(X=a\).", False),
             ]),
    ])


# ============================================================ 13
zet("bedrijfswetenschappen-ongelijkheden-oplossen",
    titel="Bedrijfswetenschappen: ongelijkheden oplossen",
    reeksen=[
        dict(kop="Intervallen", opdracht="Schrijf als interval.",
             oefeningen=[
                 ("rij", [(r"\(-2<x\leq 3\)", r"\(]-2,3]\)"), (r"\(x\geq 5\)", r"\([5,+\infty[\)"), (r"\(x<0\)", r"\(]-\infty,0[\)"),
                          (r"\(0\leq x<4\)", r"\([0,4[\)"), (r"\(x<-1\) of \(x>2\)", r"\(]-\infty,-1[\cup]2,+\infty[\)")], "Vul in.", WW),
             ]),
        dict(kop="Grafisch", opdracht=r"Een functie \(f\) heeft nulwaarden \(-4\) en \(2\) en is positief tussen die nulwaarden.",
             oefeningen=[
                 ("rij", [(r"\(f(x)>0\)", r"\(]-4,2[\)"), (r"\(f(x)\geq 0\)", r"\([-4,2]\)"), (r"\(f(x)<0\)", r"\(]-\infty,-4[\cup]2,+\infty[\)")], "Vul in.", WW),
                 ("kort", r"Een stijgende \(f\) en een dalende \(g\) snijden in \(x=1\). Los op: \(f(x)\leq g(x)\).", r"\(]-\infty,1]\)", WW),
                 ("kort", r"Nulwaarden \(-1\), \(2\), \(5\), tekenverloop \(+,-,+,-\). Los op: \(f(x)<0\).", r"\(]-1,2[\cup]5,+\infty[\)", WL),
             ]),
        dict(kop="Zonder rekenen", opdracht="Geef de oplossingsverzameling.",
             oefeningen=[
                 ("rij", [(r"\(3^{x}>0\)", r"\(\mathbb{R}\)"), (r"\(3^{x}<0\)", r"\(\varnothing\)"), (r"\(\sin x<-1\)", r"\(\varnothing\)"),
                          (r"\(x^{2}\geq 0\)", r"\(\mathbb{R}\)"), (r"\(x^{2}<0\)", r"\(\varnothing\)"), (r"\(x^{2}\leq 0\)", r"\(\{0\}\)")], "Vul in.", W),
             ]),
        dict(kop="Eerstegraads", opdracht="Los op en schrijf als interval.",
             oefeningen=[
                 ("rij", [(r"\(2x-8>0\)", r"\(]4,+\infty[\)"), (r"\(-4x+12\geq 0\)", r"\(]-\infty,3]\)"),
                          (r"\(5-x<2\)", r"\(]3,+\infty[\)"), (r"\(-2x>6\)", r"\(]-\infty,-3[\)")], "Vul in.", WW),
             ]),
        dict(kop="Tweedegraads", opdracht="Zoek de nulwaarden, maak een tekenverloop en los op.",
             oefeningen=[
                 ("rij", [(r"\(x^{2}-7x+10<0\)", r"\(]2,5[\)"), (r"\(x^{2}-16\geq 0\)", r"\(]-\infty,-4]\cup[4,+\infty[\)"),
                          (r"\(-x^{2}+4x+5>0\)", r"\(]-1,5[\)"), (r"\(x^{2}+1>0\)", r"\(\mathbb{R}\)"),
                          (r"\(x^{2}-4x+4>0\)", r"\(\mathbb{R}\setminus\{2\}\)"), (r"\(x^{2}-4x+4\leq 0\)", r"\(\{2\}\)"),
                          (r"\(3x^{2}\leq 12x\)", r"\([0,4]\)"), (r"\(-3x^{2}+27\leq 0\)", r"\(]-\infty,-3]\cup[3,+\infty[\)")], "Vul in.", WL),
             ]),
        dict(kop="Toepassingen", opdracht="Stel een ongelijkheid op en los ze op.",
             oefeningen=[
                 ("kort", r"Winst \(W(q)=-q^{2}+40q-300\) (in euro, \(q\) stuks). Voor welke \(q\) is er winst?", r"\(10<q<30\)", WW),
                 ("kort", r"Bij welke \(q\) is die winst het grootst?", r"\(q=20\)", W),
                 ("kort", r"Een bal: \(h(t)=-5t^{2}+30t\). Wanneer is hij hoger dan \(40\) m?", r"\(2<t<4\)", WW),
                 ("kort", r"Een rechthoek met omtrek \(20\) heeft zijden \(x\) en \(10-x\). Voor welke \(x\) is de oppervlakte minstens \(21\)?", r"\(3\leq x\leq 7\)", WW),
                 ("kort", r"\(2\cdot 1{,}1^{x}\) en \(5\) snijden bij \(x\approx 9{,}61\). Los op: \(2\cdot 1{,}1^{x}<5\).", r"\(]-\infty;\ 9{,}61[\)", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Bij \(x^{2}-3x\leq 0\) mag je beide leden door \(x\) delen.", False),
                 ("waar", r"Een bergparabool is positief tussen haar nulwaarden.", True),
                 ("waar", r"De oplossing van een tweedegraadsongelijkheid is altijd een begrensd interval.", False),
                 ("waar", r"Bij \(f(x)>0\) horen de nulwaarden bij de oplossing.", False),
             ]),
    ])


# ============================================================ 14
zet("bedrijfswetenschappen-exponentiele-en-goniometrische-vergelijkingen",
    titel="Bedrijfswetenschappen: exponentiële en goniometrische vergelijkingen",
    reeksen=[
        dict(kop="Zelfde grondtal", opdracht="Los op zonder rekentoestel.",
             oefeningen=[
                 ("rij", [(r"\(2^{x}=32\)", r"\(5\)"), (r"\(3^{x}=81\)", r"\(4\)"), (r"\(5^{x}=\frac{1}{25}\)", r"\(-2\)"),
                          (r"\(10^{x}=0{,}01\)", r"\(-2\)"), (r"\(4^{x}=2\)", r"\(\frac{1}{2}\)"), (r"\(3\cdot 2^{x}-24=0\)", r"\(3\)")], "Vul in.", W),
             ]),
        dict(kop="Met een logaritme", opdracht="Los op. Geef de exacte oplossing en rond af op twee decimalen.",
             oefeningen=[
                 ("rij", [(r"\(2^{x}=10\)", r"\(\log_{2}10\approx 3{,}32\)"), (r"\(e^{x}=3\)", r"\(\ln 3\approx 1{,}10\)"),
                          (r"\(1{,}5^{x}=4\)", r"\(\log_{1{,}5}4\approx 3{,}42\)"), (r"\(5\cdot 1{,}2^{x}=20\)", r"\(\log_{1{,}2}4\approx 7{,}60\)")], "Vul in.", WL),
                 ("kort", r"Los op: \(6\cdot 1{,}4^{x}+2=0\).", r"\(V=\varnothing\): \(1{,}4^{x}\) kan niet negatief zijn.", WL),
                 ("open", r"Iemand schrijft \(4\cdot 3^{x}=36\Rightarrow 12^{x}=36\). Wat loopt er mis en wat is de oplossing?", r"\(4\cdot 3^{x}\) is niet \(12^{x}\). Deel eerst door \(4\): \(3^{x}=9\), dus \(x=2\).", 2),
             ]),
        dict(kop="Groei en verval", opdracht="Stel een vergelijking op en los op.",
             oefeningen=[
                 ("kort", r"Een kapitaal van \(1000\) euro groeit met \(4\%\) per jaar. Na hoeveel jaar is het \(1500\) euro?", r"\(1{,}04^{t}=1{,}5\): \(t\approx 10{,}3\) jaar", WL),
                 ("kort", r"Verdubbelingstijd bij \(5\%\) groei per jaar?", r"\(1{,}05^{t}=2\): \(t\approx 14{,}2\) jaar", WL),
                 ("kort", r"\(M(t)=64\cdot 0{,}5^{t/3}\). Wanneer is er nog \(8\) gram?", r"\(0{,}5^{t/3}=\frac{1}{8}\): \(t=9\)", WL),
                 ("kort", r"Een auto van \(30\,000\) euro verliest \(15\%\) per jaar. Na hoeveel volle jaren is hij minder dan \(15\,000\) euro waard?", r"\(0{,}85^{t}<0{,}5\): na \(5\) jaar", WL),
             ]),
        dict(kop="Sinusvergelijkingen", opdracht=r"Los op in \([0,2\pi]\).",
             oefeningen=[
                 ("rij", [(r"\(\sin x=\frac{\sqrt{3}}{2}\)", r"\(\frac{\pi}{3}\) en \(\frac{2\pi}{3}\)"),
                          (r"\(\sin x=1\)", r"\(\frac{\pi}{2}\)"),
                          (r"\(2\sin x+1=0\)", r"\(\frac{7\pi}{6}\) en \(\frac{11\pi}{6}\)"),
                          (r"\(\sin x=0\)", r"\(0\), \(\pi\) en \(2\pi\)"),
                          (r"\(2\sin x=3\)", r"geen oplossing"),
                          (r"\(\sin x=-\frac{\sqrt{2}}{2}\)", r"\(\frac{5\pi}{4}\) en \(\frac{7\pi}{4}\)")], "Vul in.", WL),
                 ("kort", r"\(\sin x=0{,}6\) met je rekentoestel in radialen, afgerond op twee decimalen.", r"\(0{,}64\) en \(\pi-0{,}64\approx 2{,}50\)", WL),
             ]),
        dict(kop="Algemene oplossing", opdracht=r"Geef alle oplossingen in \(\mathbb{R}\) (met \(k\in\mathbb{Z}\)).",
             oefeningen=[
                 ("kort", r"\(\sin x=\frac{1}{2}\)", r"\(x=\frac{\pi}{6}+k2\pi\) of \(x=\frac{5\pi}{6}+k2\pi\)", WL),
                 ("kort", r"\(\sin 2x=0\)", r"\(x=k\frac{\pi}{2}\)", WL),
                 ("kort", r"\(\sin\left(x-\frac{\pi}{3}\right)=0\)", r"\(x=\frac{\pi}{3}+k\pi\)", WL),
             ]),
        dict(kop="Toepassingen", opdracht="Los op.",
             oefeningen=[
                 ("kort", r"Waterhoogte \(h(t)=3\sin\left(\frac{\pi}{6}t\right)+4\) (meter, \(t\) in uur). Wanneer is het water voor het eerst \(5{,}5\) m hoog?", r"\(\sin\left(\frac{\pi}{6}t\right)=\frac{1}{2}\): na \(1\) uur", WL),
                 ("kort", r"Wanneer is het daar voor het eerst hoogwater (\(7\) m)?", r"na \(3\) uur", WW),
                 ("kort", r"Reuzenrad \(h(t)=8\sin\left(\frac{\pi}{4}(t-2)\right)+10\). Wanneer is een bakje voor het eerst op \(10\) m?", r"bij \(t=2\) min", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(\sin x=\frac{1}{3}\) heeft op \(\mathbb{R}\) precies twee oplossingen.", False),
                 ("waar", r"\(5^{x}=-25\) heeft geen oplossing.", True),
                 ("waar", r"\(\log_{3}7\) is positief.", True),
                 ("waar", r"Bij \(\sin x=0{,}3\) ligt een oplossing in het derde kwadrant.", False),
             ]),
    ])


# ============================================================ 15
zet("bedrijfswetenschappen-afgeleiden-berekenen-met-rekenregels",
    titel="Bedrijfswetenschappen: afgeleiden berekenen met rekenregels",
    reeksen=[
        dict(kop="Basisafgeleiden", opdracht=r"Geef \(f^{\prime}(x)\).",
             oefeningen=[
                 ("rij", [(r"\(x^{7}\)", r"\(7x^{6}\)"), (r"\(4x^{3}-5x^{2}+x-8\)", r"\(12x^{2}-10x+1\)"), (r"\(9\)", r"\(0\)"),
                          (r"\(\dfrac{3}{x}\)", r"\(-\dfrac{3}{x^{2}}\)"), (r"\(\dfrac{2}{x^{3}}\)", r"\(-\dfrac{6}{x^{4}}\)"), (r"\(6\sqrt{x}\)", r"\(\dfrac{3}{\sqrt{x}}\)"),
                          (r"\(5e^{x}\)", r"\(5e^{x}\)"), (r"\(3^{x}\)", r"\(3^{x}\ln 3\)"), (r"\(2\ln x\)", r"\(\dfrac{2}{x}\)"), (r"\(\log_{2}x\)", r"\(\dfrac{1}{x\ln 2}\)")], "Vul in.", WW),
             ]),
        dict(kop="Product en quotiënt", opdracht=r"Geef \(f^{\prime}(x)\) en vereenvoudig.",
             oefeningen=[
                 ("rij", [(r"\((x+3)(x^{2}-1)\)", r"\(3x^{2}+6x-1\)"), (r"\(x^{2}e^{x}\)", r"\((x^{2}+2x)e^{x}\)"), (r"\(x\ln x\)", r"\(\ln x+1\)"),
                          (r"\(\dfrac{x}{x-2}\)", r"\(\dfrac{-2}{(x-2)^{2}}\)"), (r"\(\dfrac{3x+1}{x}\)", r"\(-\dfrac{1}{x^{2}}\)"), (r"\(\dfrac{x}{e^{x}}\)", r"\(\dfrac{1-x}{e^{x}}\)")], "Vul in.", WL),
                 ("open", r"Iemand rekent \(\big(x^{2}\cdot x^{3}\big)^{\prime}=2x\cdot 3x^{2}=6x^{3}\). Wat loopt er mis? Wat is de juiste afgeleide?", r"De afgeleide van een product is niet het product van de afgeleiden. Juist: \(x^{5}\) geeft \(5x^{4}\).", 2),
             ]),
        dict(kop="Kettingregel", opdracht=r"Geef \(f^{\prime}(x)\).",
             oefeningen=[
                 ("rij", [(r"\((2x+5)^{3}\)", r"\(6(2x+5)^{2}\)"), (r"\((x^{2}-4)^{5}\)", r"\(10x(x^{2}-4)^{4}\)"), (r"\(e^{4x}\)", r"\(4e^{4x}\)"),
                          (r"\(e^{-x}\)", r"\(-e^{-x}\)"), (r"\(\ln(x^{2}+1)\)", r"\(\dfrac{2x}{x^{2}+1}\)"), (r"\(\ln(5x)\)", r"\(\dfrac{1}{x}\)"),
                          (r"\(\sqrt{4x+1}\)", r"\(\dfrac{2}{\sqrt{4x+1}}\)")], "Vul in.", WW),
             ]),
        dict(kop="Waarde van de afgeleide", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [(r"\(f(x)=x^{3}-2x\), \(f^{\prime}(1)\)", r"\(1\)"), (r"\(f(x)=e^{3x}\), \(f^{\prime}(0)\)", r"\(3\)"),
                          (r"\(f(x)=\ln(2x)\), \(f^{\prime}(4)\)", r"\(\frac{1}{4}\)"), (r"\(f(x)=\dfrac{x-1}{x}\), \(f^{\prime}(2)\)", r"\(\frac{1}{4}\)")], "Vul in.", W),
             ]),
        dict(kop="Raaklijn", opdracht="Stel een vergelijking op van de raaklijn.",
             oefeningen=[
                 ("kort", r"aan \(y=x^{2}\) in \((2,4)\)", r"\(y=4x-4\)", WW),
                 ("kort", r"aan \(y=x^{3}\) in \((1,1)\)", r"\(y=3x-2\)", WW),
                 ("kort", r"aan \(y=e^{x}\) in \((0,1)\)", r"\(y=x+1\)", WW),
             ]),
        dict(kop="In een bedrijf", opdracht="Los op en antwoord in een zin.",
             oefeningen=[
                 ("kort", r"\(K(q)=0{,}2q^{2}+15q+500\). Geef de marginale kost \(K^{\prime}(q)\).", r"\(0{,}4q+15\)", WW),
                 ("kort", r"Wat is de marginale kost bij \(q=50\)?", r"\(35\) euro", W),
                 ("open", r"Wat betekent dat getal?", r"Eén stuk extra maken kost bij \(50\) stuks ongeveer \(35\) euro.", 1),
                 ("kort", r"\(B(t)=2000\cdot e^{0{,}03t}\). Geef \(B^{\prime}(t)\).", r"\(60\cdot e^{0{,}03t}\)", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\((5\cdot f(x))^{\prime}=5\cdot f^{\prime}(x)\)", True),
                 ("waar", r"De afgeleide van \(3^{x}\) is \(x\cdot 3^{x-1}\).", False),
                 ("waar", r"Bij de quotiëntregel mag je \(f^{\prime}g\) en \(fg^{\prime}\) van plaats wisselen.", False),
                 ("waar", r"Is \(f^{\prime}(a)<0\), dan daalt \(f\) in \(a\).", True),
             ]),
    ])


# ============================================================ 16
zet("bedrijfswetenschappen-verloop-van-een-functie-en-optimaliseren",
    titel="Bedrijfswetenschappen: verloop van een functie en optimaliseren",
    reeksen=[
        dict(kop="Extrema zoeken", opdracht=r"Bereken \(f^{\prime}\), zoek de nulwaarden en bepaal de extrema.",
             oefeningen=[
                 ("kort", r"\(f(x)=x^{3}-12x\)", r"max \(16\) in \(x=-2\), min \(-16\) in \(x=2\)", WL),
                 ("kort", r"\(f(x)=2x^{3}+3x^{2}-12x\)", r"max \(20\) in \(x=-2\), min \(-7\) in \(x=1\)", WL),
                 ("kort", r"\(f(x)=x^{4}-8x^{2}\)", r"min \(-16\) in \(x=\pm 2\), max \(0\) in \(x=0\)", WL),
                 ("kort", r"\(f(x)=x^{2}-6x+4\): bereik?", r"\([-5,+\infty[\)", WW),
             ]),
        dict(kop="Hol, bol en buigpunten", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"\(f(x)=x^{3}-3x^{2}+1\): buigpunt bij \(x=\)", r"\(1\)"),
                          (r"Waar is die grafiek hol?", r"\(x>1\)"),
                          (r"\(f(x)=x^{3}+6x^{2}\): buigpunt bij \(x=\)", r"\(-2\)"),
                          (r"\(f^{\prime}<0\) en \(f^{\prime\prime}>0\): hoe heet dat?", "afnemende daling")], "Vul in.", WL),
             ]),
        dict(kop="Samenvattende tabel", opdracht=r"Vul de tabel in voor \(f(x)=x^{3}-3x^{2}\), met \(f^{\prime}(x)=3x^{2}-6x\) en \(f^{\prime\prime}(x)=6x-6\).",
             oefeningen=[
                 ("tabel", [r"\(x\)", r"\(0\)", r"\(1\)", r"\(2\)"],
                  [[r"teken \(f^{\prime}\)", None, None, None], [r"teken \(f^{\prime\prime}\)", None, None, None], [r"\(f(x)\)", None, None, None]],
                  r"\(f^{\prime}\): \(0\), \(-\), \(0\). \(f^{\prime\prime}\): \(-\), \(0\), \(+\). \(f\): max \(0\), buigpunt \(-2\), min \(-4\).", WW),
             ]),
        dict(kop="Extremumproblemen", opdracht="Volg het stappenplan en antwoord in een zin.",
             oefeningen=[
                 ("open", r"Met \(60\) m hekwerk maak je een rechthoekige weide. Welke afmetingen geven de grootste oppervlakte?", r"\(A(x)=x(30-x)\), \(A^{\prime}=30-2x=0\): \(x=15\). Een vierkant van \(15\) m op \(15\) m (\(225\) m²).", 3),
                 ("open", r"Winst \(W(q)=-3q^{2}+240q-2000\). Bij welk aantal stuks is de winst het grootst, en hoeveel is ze?", r"\(W^{\prime}=-6q+240=0\): \(q=40\). De grootste winst is \(2800\) euro.", 3),
                 ("open", r"Gemiddelde kost \(G(q)=q+\dfrac{900}{q}\) (\(q>0\)). Bij welk aantal is ze het laagst?", r"\(G^{\prime}=1-\frac{900}{q^{2}}=0\): \(q=30\). De laagste gemiddelde kost is \(60\) euro per stuk.", 3),
                 ("open", r"Opbrengst \(O(p)=p(120-3p)\). Welke prijs geeft de grootste opbrengst?", r"\(O^{\prime}=120-6p=0\): \(p=20\) euro, opbrengst \(1200\) euro.", 2),
                 ("open", r"Uit karton van \(18\) cm op \(18\) cm maak je een open doos door hoekjes \(x\) weg te knippen. Geef \(V(x)\), het praktisch domein en de beste \(x\).", r"\(V(x)=x(18-2x)^{2}\), domein \(]0,9[\). \(V^{\prime}=(18-2x)(18-6x)=0\): \(x=3\) cm (\(x=9\) valt weg).", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Als \(f^{\prime}(a)=0\) en \(f^{\prime\prime}(a)>0\), dan heeft \(f\) een minimum in \(a\).", True),
                 ("waar", r"Elke \(x\) met \(f^{\prime}(x)=0\) is een extremum.", False),
                 ("waar", r"Een buigpunt van \(f\) is een top van de grafiek van \(f^{\prime}\).", True),
                 ("waar", r"Het grootste resultaat kan nooit in een grenspunt van het domein liggen.", False),
             ]),
    ])


# ============================================================ 17
zet("bedrijfswetenschappen-integralen-en-oppervlakte",
    titel="Bedrijfswetenschappen: integralen en oppervlakte",
    reeksen=[
        dict(kop="Onder- en bovensom", opdracht=r"Benader de oppervlakte onder \(f(x)=2x\) op \([0,3]\) met \(3\) rechthoekjes van breedte \(1\).",
             oefeningen=[
                 ("rij", [("Ondersom", r"\(0+2+4=6\)"), ("Bovensom", r"\(2+4+6=12\)"), ("Echte oppervlakte (driehoek)", r"\(9\)")], "Vul in.", WW),
                 ("kort", "Hoe krijg je een betere benadering?", "meer en smallere rechthoekjes nemen", WL),
             ]),
        dict(kop="Primitieven", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [(r"\(\int x^{3}\,dx\)", r"\(\frac{x^{4}}{4}+c\)"), (r"\(\int 5\,dx\)", r"\(5x+c\)"), (r"\(\int(9x^{2}-6x+2)\,dx\)", r"\(3x^{3}-3x^{2}+2x+c\)"),
                          (r"\(\int 8x^{3}\,dx\)", r"\(2x^{4}+c\)"), (r"\(\int(x+1)\,dx\)", r"\(\frac{x^{2}}{2}+x+c\)")], "Vul in.", WL),
                 ("kort", r"Geef twee verschillende primitieven van \(f(x)=4x\).", r"bv. \(2x^{2}\) en \(2x^{2}+7\)", WL),
             ]),
        dict(kop="Bepaalde integralen", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [(r"\(\int_{0}^{2}x^{3}\,dx\)", r"\(4\)"), (r"\(\int_{1}^{3}(2x+1)\,dx\)", r"\(10\)"), (r"\(\int_{0}^{1}(6x^{2}-2x)\,dx\)", r"\(1\)"),
                          (r"\(\int_{2}^{4}x\,dx\)", r"\(6\)"), (r"\(\int_{0}^{3}(x^{2}-9)\,dx\)", r"\(-18\)"), (r"\(\int_{-2}^{2}x^{3}\,dx\)", r"\(0\)"), (r"\(\int_{5}^{5}x^{2}\,dx\)", r"\(0\)")], "Vul in.", W),
             ]),
        dict(kop="Werkelijke oppervlakte", opdracht="Bereken de oppervlakte.",
             oefeningen=[
                 ("kort", r"tussen \(y=x^{3}\) en de \(x\)-as op \([-2,2]\)", r"\(4+4=8\)", WW),
                 ("kort", r"tussen \(y=x^{2}-4\) en de \(x\)-as op \([0,3]\)", r"\(\frac{16}{3}+\frac{7}{3}=\frac{23}{3}\)", WW),
                 ("kort", r"ingesloten door \(y=x^{2}\) en \(y=4x\)", r"grenzen \(0\) en \(4\): \(\frac{32}{3}\)", WW),
                 ("kort", r"ingesloten door \(y=x^{2}\) en \(y=x\)", r"\(\frac{1}{6}\)", WW),
             ]),
        dict(kop="Toepassingen", opdracht="Bereken en antwoord in een zin.",
             oefeningen=[
                 ("open", r"Een auto rijdt met \(v(t)=4t\) m/s. Hoeveel meter legt hij af in de eerste \(5\) seconden?", r"\(\int_{0}^{5}4t\,dt=50\) m", 1),
                 ("open", r"De marginale kost is \(K^{\prime}(q)=4q+20\) euro per stuk. Hoeveel kost het om van \(10\) naar \(20\) stuks te gaan?", r"\(\int_{10}^{20}(4q+20)\,dq=[2q^{2}+20q]_{10}^{20}=1200-400=800\) euro", 2),
                 ("open", r"Een kraan geeft \(d(t)=10-2t\) liter per minuut (\(0\leq t\leq 5\)). Hoeveel liter stroomt er in totaal uit?", r"\(\int_{0}^{5}(10-2t)\,dt=25\) liter", 1),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"\(\int(f(x)\cdot g(x))\,dx=\int f(x)\,dx\cdot\int g(x)\,dx\)", False),
                 ("waar", r"Een bepaalde integraal kan negatief zijn.", True),
                 ("waar", r"Bij de oppervlakte tussen twee krommen trek je de onderste van de bovenste af.", True),
                 ("waar", r"\(\int_{0}^{4}f(x)\,dx=\int_{0}^{2}f(x)\,dx+\int_{2}^{4}f(x)\,dx\)", True),
             ]),
    ])


# ============================================================ 18
zet("bedrijfswetenschappen-matrices-grafen-en-stelsels",
    titel="Bedrijfswetenschappen: matrices, grafen en stelsels",
    reeksen=[
        dict(kop="Dimensie en elementen", opdracht=r"\(A=\begin{bmatrix}3&-1&0&2\\5&4&7&1\\0&6&-2&8\end{bmatrix}\)",
             oefeningen=[
                 ("rij", [(r"Dimensie van \(A\)", r"\(3\times 4\)"), (r"\(a_{24}\)", r"\(1\)"), (r"\(a_{32}\)", r"\(6\)"), (r"Dimensie van \(A^{T}\)", r"\(4\times 3\)")], "Vul in.", W),
             ]),
        dict(kop="Rekenen", opdracht=r"\(A=\begin{bmatrix}2&1\\0&3\end{bmatrix}\), \(B=\begin{bmatrix}1&-2\\4&0\end{bmatrix}\). Bereken.",
             oefeningen=[
                 ("rij", [(r"\(A+B\)", r"\(\begin{bmatrix}3&-1\\4&3\end{bmatrix}\)"), (r"\(2A\)", r"\(\begin{bmatrix}4&2\\0&6\end{bmatrix}\)"),
                          (r"\(A\cdot B\)", r"\(\begin{bmatrix}6&-4\\12&0\end{bmatrix}\)"), (r"\(B\cdot A\)", r"\(\begin{bmatrix}2&-5\\8&4\end{bmatrix}\)"),
                          (r"\(A^{2}\)", r"\(\begin{bmatrix}4&5\\0&9\end{bmatrix}\)")], "Vul in.", WW),
                 ("kort", r"Wat leer je uit \(A\cdot B\) en \(B\cdot A\)?", r"Het product van matrices is niet commutatief.", WL),
                 ("kort", r"\(C\) is \(3\times 2\), \(D\) is \(2\times 5\). Dimensie van \(C\cdot D\)? Bestaat \(D\cdot C\)?", r"\(3\times 5\); \(D\cdot C\) bestaat niet.", WL),
             ]),
        dict(kop="Een winkel", opdracht=r"Een winkel verkoopt \(20\) koffies, \(15\) thee en \(8\) taartjes, aan \(3\), \(2{,}5\) en \(4\) euro.",
             oefeningen=[
                 ("kort", "Schrijf de omzet als product van twee matrices.", r"\(\begin{bmatrix}20&15&8\end{bmatrix}\cdot\begin{bmatrix}3\\2{,}5\\4\end{bmatrix}\)", WL),
                 ("kort", "Hoeveel is de omzet?", r"\(129{,}50\) euro", WW),
             ]),
        dict(kop="Overgangsmatrix", opdracht=r"Klanten kiezen elke maand tussen winkel X en Y. \(T=\begin{bmatrix}0{,}9&0{,}2\\0{,}1&0{,}8\end{bmatrix}\) (kolom = van, rij = naar), \(X_{0}=\begin{bmatrix}600\\400\end{bmatrix}\).",
             oefeningen=[
                 ("kort", r"Waarom is \(T\) een overgangsmatrix?", "De kolommen tellen op tot 1.", WL),
                 ("kort", "Toestand na één maand?", r"\(\begin{bmatrix}620\\380\end{bmatrix}\)", WW),
                 ("kort", r"Hoe bereken je de toestand na \(6\) maanden?", r"\(T^{6}\cdot X_{0}\)", WW),
                 ("kort", r"Is \(\begin{bmatrix}667\\333\end{bmatrix}\) (afgerond) een evenwicht? Controleer \(T\cdot X\).", r"Ja: \(0{,}9\cdot 667+0{,}2\cdot 333\approx 667\).", WL),
             ]),
        dict(kop="Grafen", opdracht=r"Een graaf heeft pijlen \(A\to B\), \(A\to C\), \(B\to C\) en \(C\to A\).",
             oefeningen=[
                 ("kort", "Geef de verbindingsmatrix (volgorde A, B, C).", r"\(\begin{bmatrix}0&1&1\\0&0&1\\1&0&0\end{bmatrix}\)", WW),
                 ("kort", r"Wat tel je met \(M^{2}\)?", r"de wegen van lengte \(2\)", WW),
             ]),
        dict(kop="Gauss-Jordan", opdracht="Los op met de uitgebreide coëfficiëntenmatrix.",
             oefeningen=[
                 ("kort", r"\(\begin{cases}x+y=10\\x-y=4\end{cases}\)", r"\(V=\{(7,3)\}\)", WW),
                 ("kort", r"\(\begin{cases}2x+y=8\\x+3y=9\end{cases}\)", r"\(V=\{(3,2)\}\)", WW),
                 ("kort", r"Eindmatrix \(\left[\begin{array}{cc|c}1&2&3\\0&0&5\end{array}\right]\): soort stelsel?", r"strijdig, \(V=\varnothing\)", WW),
                 ("kort", r"Eindmatrix \(\left[\begin{array}{ccc|c}1&0&-1&2\\0&1&3&4\\0&0&0&0\end{array}\right]\): oplossingen met \(z=r\)?", r"\(V=\{(2+r,\ 4-3r,\ r)\mid r\in\mathbb{R}\}\)", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"Een nulrij \(\left[\begin{array}{cc|c}0&0&0\end{array}\right]\) maakt een stelsel strijdig.", False),
                 ("waar", r"\((AB)^{T}=A^{T}B^{T}\)", False),
                 ("waar", "Twee rijen van plaats wisselen is een elementaire rijoperatie.", True),
                 ("waar", "In een evenwichtstoestand verhuist niemand meer.", False),
             ]),
    ])


# ============================================================ 19
zet("bedrijfswetenschappen-hypothesetoetsen-en-correlatie",
    titel="Bedrijfswetenschappen: hypothesetoetsen en correlatie",
    reeksen=[
        dict(kop="Hypothesen", opdracht=r"Geef \(H_{0}\) en \(H_{1}\), en zeg of de toets eenzijdig of tweezijdig is.",
             oefeningen=[
                 ("kort", r"Een fabrikant zegt dat zijn batterijen gemiddeld \(20\) uur meegaan. Jij denkt dat het minder is.", r"\(H_{0}:\mu=20\), \(H_{1}:\mu<20\); eenzijdig", WL),
                 ("kort", r"Een bakker wil weten of zijn broden van \(800\) g te zwaar of te licht zijn.", r"\(H_{0}:\mu=800\), \(H_{1}:\mu\neq 800\); tweezijdig", WL),
                 ("kort", r"Een school denkt dat meer dan \(30\%\) van de leerlingen met de fiets komt.", r"\(H_{0}:p=0{,}30\), \(H_{1}:p>0{,}30\); eenzijdig", WL),
                 ("kort", r"In een steekproef komen \(84\) van \(240\) leerlingen met de fiets. Steekproefproportie?", r"\(0{,}35\)", W),
             ]),
        dict(kop="Besluiten", opdracht=r"Verwerp je \(H_{0}\)?",
             oefeningen=[
                 ("rij", [(r"\(\alpha=0{,}05\), \(p=0{,}01\)", "verwerpen"), (r"\(\alpha=0{,}05\), \(p=0{,}12\)", "niet verwerpen"),
                          (r"\(\alpha=0{,}01\), \(p=0{,}02\)", "niet verwerpen"), (r"\(\alpha=0{,}10\), \(p=0{,}07\)", "verwerpen")], "Vul in.", WW),
                 ("open", r"Een toets geeft \(p=0{,}03\). Iemand zegt: \"Er is \(3\%\) kans dat \(H_{0}\) waar is.\" Verbeter.", r"De p-waarde is de kans op zo'n (of een extremer) resultaat als \(H_{0}\) waar is, niet de kans dat \(H_{0}\) waar is.", 2),
                 ("open", r"Bij \(\alpha=0{,}05\) is \(p=0{,}40\). Mag je besluiten dat \(H_{0}\) waar is?", r"Nee. Je verwerpt \(H_{0}\) niet, maar je hebt ze ook niet bewezen: het resultaat is gewoon goed te verklaren als \(H_{0}\) waar is.", 2),
             ]),
        dict(kop="Correlatie", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [(r"Sterkste lineair verband: \(0{,}6\), \(-0{,}9\) of \(0{,}85\)?", r"\(-0{,}9\)"),
                          (r"Puntenwolk zonder patroon: \(r\approx\)", r"\(0\)"),
                          (r"\(r=0{,}3\) is ...", "zwak en positief"),
                          (r"Punten dicht bij een stijgende rechte: \(r\approx\)", r"dicht bij \(1\)")], "Vul in.", WL),
                 ("kort", "Je onderzoekt of de temperatuur de ijsverkoop beïnvloedt. Wat is de onafhankelijke variabele?", "de temperatuur", WW),
             ]),
        dict(kop="Trendlijn", opdracht=r"Een rekenblad geeft \(y=1{,}8x+12\), met \(x\) het aantal uren studie en \(y\) de punten op \(40\). Gemeten: \(x\) van \(2\) tot \(12\) uur, \(r=0{,}82\).",
             oefeningen=[
                 ("kort", r"Wat betekent \(1{,}8\)?", r"per extra uur studie ongeveer \(1{,}8\) punten meer", WL),
                 ("kort", r"Voorspelling bij \(10\) uur?", r"\(30\) punten", W),
                 ("kort", r"Waarom geeft \(x=20\) geen betrouwbare voorspelling?", r"\(20\) ligt ver buiten de gemeten gegevens (en geeft zelfs \(48\) op \(40\)).", WL),
                 ("open", r"Bewijst \(r=0{,}82\) dat studeren de punten veroorzaakt?", "Nee, samenhang is geen oorzaak. Er kan een andere verklaring of verborgen variabele zijn (bv. interesse in het vak).", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", r"De nulhypothese bevat altijd een gelijkheidsteken.", True),
                 ("waar", r"Het significantieniveau kies je nadat je de p-waarde kent.", False),
                 ("waar", r"Bij een parabool met de top in het midden is \(r\) dicht bij \(1\).", False),
                 ("waar", r"Omgekeerd evenredige grootheden volgen \(y=\frac{a}{x}\).", True),
             ]),
    ])

r"""Kansvariabelen en de binomiale verdeling — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen en een eigen staafdiagram,
zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Kansverdeling van X ~ B(4; 0,5) ------------------------------------------------------
BV = Prent("binomiaal-4", "Kansverdeling van het aantal keer kop bij vier muntworpen", "een staafdiagram met vijf staven voor k = 0 tot 4, met hoogten 0,0625; 0,25; 0,375; 0,25; 0,0625; verticale as P(X = k)")
L0, R0, T0, B0 = 160, 880, 90, 520


def Y(w):
    return B0 - (B0 - T0) * w / 0.4


BV.lijn(L0, B0, R0, B0, DONKER, 3)
BV.lijn(L0, B0, L0, T0 - 10, DONKER, 3)
for w in [0, 0.1, 0.2, 0.3, 0.4]:
    BV.lijn(L0, Y(w), R0, Y(w), "#ecebe6", 1)
    BV.tekst(L0 - 12, Y(w) + 6, f"{w:.1f}".replace(".", ","), 16, "end")
BV.tekst(L0, T0 - 25, "P(X = k)", 18, "start")
BV.tekst((L0 + R0) / 2, 600, "k = aantal keer kop", 18)
KANS = [0.0625, 0.25, 0.375, 0.25, 0.0625]
XS = [L0 + 72 + i * 144 for i in range(5)]
for k, (x, w) in enumerate(zip(XS, KANS)):
    BV.rect(x - 40, Y(w), 80, B0 - Y(w), "#c4d5b5", DONKER, 0, 2)
    BV.tekst(x, B0 + 30, str(k), 20)


def staaf(k):
    return [Prent.zone(XS[k] - 55, T0, 110, B0 - T0 + 10)]


VRAGEN = [
    klik("Klik op de staaf van P(X = 3).", BV.bestand, staaf(3),
         "De vierde staaf, bij k = 3."),
    klik("Klik op de staaf met de grootste kans.", BV.bestand, staaf(2),
         r"Bij \(p = 0{,}5\) ligt de top in het midden: k = 2."),
    met_prent(BV.bestand, inv("Hoe groot is P(X = 2)? Schrijf als decimaal getal.", ["0,375", "0.375"],
              r"\(C(4, 2) \cdot 0{,}5^4 = 6 / 16 = 0{,}375\).")),
    met_prent(BV.bestand, inv("Hoe groot is P(X ≥ 1)? Schrijf als decimaal getal.", ["0,9375", "0.9375"],
              r"\(1 - P(X = 0) = 1 - 0{,}0625 = 0{,}9375\).")),
    met_prent(BV.bestand, keuze("Deze kansverdeling is [[*symmetrisch|scheef naar rechts|scheef naar links]], omdat p gelijk is aan 0,5.",
              "Kop is even waarschijnlijk als munt.")),
    met_prent(BV.bestand, inv("Wat is de som van de hoogten van alle staven?", ["1", "één"],
              "De som van alle kansen in een kansverdeling is 1.")),
    tabel("Discreet of continu?", [
        ("het aantal goals in een match", "discreet"),
        ("de reactietijd van een sprinter", "continu"),
        ("het aantal sms'jes per dag", "discreet"),
        ("het gewicht van een appel", "continu"),
    ], "Tellen geeft losse waarden, meten geeft elke waarde in een interval.",
       kolommen=["discreet", "continu"]),
    tabel("Is X binomiaal verdeeld?", [
        ("X = aantal zessen bij 12 worpen met een dobbelsteen", J),
        ("X = aantal rode knikkers bij 3 trekkingen zonder terugleggen uit een kleine zak", F),
        ("X = aantal juiste antwoorden als je 15 vragen met 4 opties gokt", J),
        ("X = de lengte van een willekeurige leerling", F),
    ], "Vaste n, onafhankelijke experimenten, telkens dezelfde kans p op succes."),
    keuze(r"Een quiz heeft 12 vragen met 5 opties. Je gokt alles. Dan is X ~ B(12; [[*0,2|0,25|5]]).",
          "Eén juiste optie uit vijf."),
    casus(
        "Een basketbalspeler scoort 70 procent van zijn vrijworpen. Hij neemt 5 vrijworpen, onafhankelijk van elkaar. "
        "X is het aantal gescoorde vrijworpen.",
        [
            keuze("X ~ B([[*5|70|0,7]]; 0,7).", "n is het aantal experimenten."),
            inv("Hoe groot is P(X = 5)? Rond af op vier decimalen.", ["0,1681", "0.1681"],
                r"\(0{,}7^5 = 0{,}16807\)."),
            inv("Hoe groot is P(X = 0)? Rond af op vijf decimalen.", ["0,00243", "0.00243"],
                r"\(0{,}3^5 = 0{,}00243\)."),
            mk("Waar liggen de hoogste staven van deze kansverdeling?",
               ["rechts van het midden",
                "precies in het midden",
                "links van het midden",
                "alle staven zijn even hoog"], 0,
               "Succes is waarschijnlijker dan mislukking."),
        ],
    ),
    inv(r"Bij X ~ B(3; 0,5): hoe groot is P(X = 1)? Schrijf als breuk of decimaal.", ["0,375", "0.375", "3/8"],
        r"\(C(3, 1) \cdot 0{,}5^3 = 3/8\)."),
    tabel("Klopt deze kansverdeling?", [
        ("P(X=0)=0,3; P(X=1)=0,3; P(X=2)=0,4", J),
        ("P(X=0)=0,5; P(X=1)=0,4; P(X=2)=0,2", F),
        ("P(X=0)=0,6; P(X=1)=-0,1; P(X=2)=0,5", F),
    ], "De kansen moeten samen 1 zijn en elk tussen 0 en 1 liggen."),
    keuze(r"In de formule \(P(X = k) = C(n, k)\, p^k (1-p)^{n-k}\) telt \(C(n, k)\) [[*op hoeveel plaatsen de successen kunnen staan|de kans op één succes|het aantal mislukkingen]].",
          "De combinatie telt de volgordes."),
    sleep("Een experiment met juist twee uitkomsten heet een [[Bernoulli]]-experiment. Een ander woord voor kansvariabele is [[stochast]].",
          ["binomium", "parameter"], "Twee termen uit de bijlage."),
    mk(r"Een machine maakt 4 procent defecte stukken. Je neemt 25 stukken. Welke verdeling hoort bij het aantal defecte?",
       ["B(25; 0,04)", "B(4; 0,25)", "B(25; 4)", "B(0,04; 25)"], 0,
       "n = 25, p = 0,04."),
    keuze("De kans op één exacte waarde bij een continue kansvariabele is [[*0|0,5|1]].",
          "Je rekent met kansen op een interval."),
    inv("Een tabel geeft P(X=1)=0,15; P(X=2)=0,45; P(X=3)=? Wat moet P(X=3) zijn als dit alle waarden zijn?", ["0,4", "0.4", "0,40"],
        "1 - 0,15 - 0,45 = 0,4."),
    inv("Bij diezelfde tabel: hoe groot is P(X ≤ 2)?", ["0,6", "0.6", "0,60"],
        "0,15 + 0,45 = 0,6."),
    sorteer("Hoort dit bij de voorwaarden van een binomiale verdeling?", ["Voorwaarde", "Geen voorwaarde"], [
        ["een vast aantal experimenten n", "Voorwaarde"],
        ["onafhankelijke experimenten", "Voorwaarde"],
        ["telkens dezelfde kans p", "Voorwaarde"],
        ["p moet 0,5 zijn", "Geen voorwaarde"],
    ], "Elke p tussen 0 en 1 mag."),
    keuze("Bij X ~ B(n; p) loopt k van 0 tot en met [[*n|n + 1|p]].",
          "Meer successen dan experimenten kan niet."),
    inv(r"Je gooit 4 keer met een dobbelsteen. Hoe groot is de kans op geen enkele zes? Rond af op vier decimalen.", ["0,4823", "0.4823"],
        r"\((5/6)^4 \approx 0{,}4823\)."),
    keuze("De kans op minstens één zes bij 4 worpen is dan ongeveer [[*0,5177|0,4823|0,1667]].",
          "1 - 0,4823."),
    klik("Klik op de staaf die even hoog is als die van k = 1.", BV.bestand, staaf(3),
         "Bij p = 0,5 is de verdeling symmetrisch: P(X = 1) = P(X = 3)."),
    inv(r"Bij X ~ B(6; 0,5): hoe groot is P(X = 6)? Schrijf als breuk.", ["1/64"],
        r"\(0{,}5^6 = 1/64\)."),
    keuze(r"Bij X ~ B(8; 0,1) liggen de hoogste staven [[*links, bij kleine k|rechts, bij grote k|precies in het midden]].",
          "Met een kleine kans op succes zijn weinig successen het meest waarschijnlijk."),
    mk("Welke vraag kan je beantwoorden met de complementregel?",
       ["kans op minstens één succes",
        "kans op juist twee successen",
        "kans dat het eerste succes valt",
        "het aantal mogelijke volgordes"], 0,
       r"\(P(X \geq 1) = 1 - P(X = 0)\)."),
    open_("Leg uit waarom het aantal meisjes bij 3 trekkingen zonder terugleggen uit een groep van 5 meisjes en 5 jongens niet binomiaal verdeeld is.",
          "Bij een binomiale verdeling moeten de experimenten onafhankelijk zijn met telkens dezelfde kans p. Zonder terugleggen verandert de kans na elke trekking: eerst 5/10, daarna 4/9 of 5/9. Dus is p niet constant."),
]

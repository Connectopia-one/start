"""Lineaire en exponentiële groeimodellen — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond over groeimodellen binnen wi_groei, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import exponentieel as E
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(E.VRAGEN, [7, 8, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 27], {"halveringstijd": "halveringstijd"}) + [
    casus(
        "Sam zet \\(2000\\) euro op een spaarrekening met \\(3\\) procent samengestelde intrest per jaar. "
        "Zijn zus Lien krijgt elk jaar een vast bedrag van \\(60\\) euro bij op haar \\(2000\\) euro.",
        [
            keuze("Het model van Sam is [[*exponentieel|lineair]], dat van Lien [[*lineair|exponentieel]].", "Sam krijgt een vaste factor, Lien een vast bedrag."),
            inv("Hoeveel euro heeft Lien na \\(10\\) jaar?", ["2600", "2 600"], "\\(2000 + 10 \\cdot 60\\)."),
            inv("Hoeveel euro heeft Sam na \\(10\\) jaar? Rond af op een euro.", ["2688", "2 688"], "\\(2000 \\cdot 1{,}03^{10} \\approx 2687{,}83\\)."),
            mk("Wie heeft na het eerste jaar het meest?",
               ["Ze hebben allebei \\(2060\\) euro.", "Sam, want samengestelde intrest wint altijd.", "Lien, want een vast bedrag is altijd meer.", "Dat kan je niet berekenen zonder logaritme."], 0,
               "Drie procent van \\(2000\\) is precies \\(60\\). Pas daarna loopt Sam uit."),
        ],
    ),
    tabel("Wat is de groeifactor per tijdseenheid?", [
        ("\\(8\\) procent erbij per jaar", "\\(1{,}08\\)"), ("\\(8\\) procent eraf per jaar", "\\(0{,}92\\)"),
        ("de helft eraf per dag", "\\(0{,}5\\)"), ("verdubbelen per uur", "\\(2\\)"),
    ], "Groeifactor is \\(1\\) plus of min het percentage als decimaal getal.", kolommen=["\\(0{,}5\\)", "\\(0{,}92\\)", "\\(1{,}08\\)", "\\(2\\)"]),
    mk("Een prijs stijgt eerst \\(10\\) procent en daalt daarna \\(10\\) procent. Waar eindigt de prijs?",
       ["\\(1\\) procent lager dan in het begin", "precies op de beginprijs", "\\(1\\) procent hoger dan in het begin", "\\(20\\) procent lager dan in het begin"], 0,
       "\\(1{,}1 \\cdot 0{,}9 = 0{,}99\\)."),
    inv("Een groeifactor van \\(1{,}44\\) per \\(2\\) jaar. Wat is de groeifactor per jaar?", ["1,2", "1.2"], "\\(\\sqrt{1{,}44} = 1{,}2\\)."),
    inv("Een populatie verdubbelt elke \\(4\\) jaar. Hoeveel keer zo groot is ze na \\(20\\) jaar?", ["32", "tweeëndertig"], "Vijf keer verdubbelen: \\(2^{5}\\)."),
    keuze("Een groeipercentage van \\(0\\) procent hoort bij een groeifactor van [[*\\(1\\)|\\(0\\)|\\(100\\)]].", "Er verandert dan niets."),
    sorteer("Lineair of exponentieel model?", ["lineair", "exponentieel"], [
        ["een taxi met een vaste instapprijs en een prijs per kilometer", "lineair"], ["een virus dat zich elke dag met een kwart uitbreidt", "exponentieel"],
        ["een gsm-abonnement van \\(12\\) euro per maand", "lineair"], ["een auto die elk jaar \\(15\\) procent van zijn waarde verliest", "exponentieel"],
        ["enkelvoudige intrest op een spaarboekje", "lineair"],
    ], "Vast bedrag erbij: lineair. Vaste factor: exponentieel."),
    inv("Een prijs daalt van \\(250\\) naar \\(200\\) euro. Met hoeveel procent is dat?", ["20", "20 %", "20%"], "\\(50 : 250 = 0{,}2\\)."),
    mk("Een bedrag is na \\(10\\) jaar \\(1{,}5\\) keer zo groot. Hoe vind je de groeifactor per jaar?",
       ["de tiendemachtswortel uit \\(1{,}5\\)", "\\(1{,}5\\) gewoon delen door het aantal jaren", "\\(1{,}5\\) verheffen tot de tiende macht", "\\(1{,}5\\) min tien"], 0,
       "\\(a^{10} = 1{,}5\\), dus \\(a = \\sqrt[10]{1{,}5}\\)."),
    tabel("Klopt dit over groei?", [
        ("Twee keer \\(10\\) procent erbij is samen \\(21\\) procent erbij.", J),
        ("Bij exponentiële afname bereik je ooit precies nul.", F),
        ("Verdubbelingstijd hangt niet af van de beginwaarde.", J),
        ("Een groeifactor per jaar zet je om naar een factor per maand door te delen door twaalf.", F),
    ], "Per maand neem je de twaalfdemachtswortel."),
    open_("Een bevolking groeit met \\(2\\) procent per jaar. Leg uit waarom er elk jaar meer mensen bijkomen dan het jaar ervoor.",
          "Twee procent is telkens twee procent van een groter aantal. Omdat de bevolking zelf groeit, worden die twee procent elk jaar meer mensen.",
          "Bij exponentiële groei groeit de toename mee."),
    mk("Een tabel toont \\(200\\), \\(150\\), \\(112{,}5\\), \\(84{,}375\\). Welk model past?",
       ["exponentieel, factor \\(0{,}75\\)", "lineair, telkens \\(50\\) eraf", "exponentieel, factor \\(1{,}25\\)", "lineair, telkens \\(25\\) procent eraf"], 0,
       "Het verschil wordt kleiner, het quotiënt blijft \\(0{,}75\\)."),
]

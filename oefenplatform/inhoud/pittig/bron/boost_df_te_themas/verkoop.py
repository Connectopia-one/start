"""Verkopen en de verkoopfactuur — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_verkoop, met een zelfgetekende verkoopfactuur met
twee btw-tarieven om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, GRIJS
from ..boost_ec_themas import boekhouden as _bh

VF = Prent("verkoopfactuur-twee-tarieven", "", "verkoopfactuur van bakkerij Gouden Korst aan restaurant De Smaak met twee btw-tarieven en letters A tot G")
VF.rect(60, 20, 880, 600, "#ffffff", DONKER, 12, 3)
VF.tekst(100, 66, "Bakkerij Gouden Korst bv", 24, "start", vet=True)
VF.tekst(100, 96, "Markt 3, Alken", 18, "start")
VF.tekst(100, 124, "btw BE 0123.456.789", 18, "start")
VF.tekst(900, 66, "FACTUUR", 28, "end", vet=True)
VF.tekst(900, 100, "nr. 2026/0815 · 12 november 2026", 18, "end")
VF.tekst(900, 134, "aan: Restaurant De Smaak bv, Genk", 18, "end")
VF.tekst(900, 174, "btw BE 0987.654.321", 18, "end")
VF.lijn(90, 190, 910, 190, GRIJS, 2)
RIJ = [
    ("C", "brood en gebak, btw 6 %", "600,00"),
    ("D", "servetten en bekers, btw 21 %", "400,00"),
    ("E", "btw 6 % op 600,00", "36,00"),
    ("F", "btw 21 % op 400,00", "84,00"),
    ("G", "te betalen", "1 120,00"),
]
Y0, DY = 245, 62
for i, (t, r, b) in enumerate(RIJ):
    y = Y0 + i * DY + (24 if t == "G" else 0)
    VF.letter(120, y - 7, t)
    VF.tekst(160, y, r, 21, "start", vet=(t == "G"))
    VF.tekst(890, y, b + " euro", 21, "end", vet=(t == "G"))
VF.lijn(560, Y0 + 4 * DY - 18, 910, Y0 + 4 * DY - 18, DONKER, 2)
VF.tekst(500, 600, "Te betalen binnen 30 dagen.", 18)
VF.letter(588, 93, "A"); VF.letter(330, 118, "B"); VF.letter(692, 168, "H")
U = "verkoopfactuur-twee-tarieven.svg"
Z = {t: Prent.rond(120, Y0 + i * DY + (24 if t == "G" else 0) - 7, 30) for i, (t, _, _) in enumerate(RIJ)}
Z["A"] = Prent.rond(588, 93, 28); Z["B"] = Prent.rond(330, 118, 28); Z["H"] = Prent.rond(692, 168, 28)

VRAGEN = [_bh.VRAGEN[15]] + [
    klik("Klik op de letter bij de wettelijke vermelding die het de bakkerij makkelijk maakt om te zien dat er geen factuur ontbreekt.", U, [Z["A"]],
         "Het factuurnummer: wie doorlopend nummert, ziet meteen of er een factuur ontbreekt."),
    klik("Klik op de letter bij het btw-nummer van de verkoper.", U, [Z["B"]],
         "De verkoper is de bakkerij. H is het btw-nummer van de klant."),
    klik("Klik op de letter bij de verschuldigde btw aan het verlaagde tarief.", U, [Z["E"]],
         "6 % op het brood en het gebak: 36 euro."),
    klik("Klik op de letter bij het bedrag dat de bakkerij als vordering op de klant boekt.", U, [Z["G"]],
         "De vordering op de klant is het totaal, btw inbegrepen."),
    casus("Bekijk de verkoopfactuur van Bakkerij Gouden Korst.", [
        inv("Hoeveel btw stort de bakkerij voor deze factuur door aan de staat, in euro? Schrijf enkel het getal.", ["120", "120,00"],
            "36 + 84 = 120 euro verschuldigde btw."),
        inv("Hoe groot is de omzet uit deze factuur, zonder btw, in euro? Schrijf enkel het getal.", ["1000", "1 000", "1.000"],
            "600 + 400 = 1 000 euro. De btw hoort niet bij de omzet."),
        tabel("Klopt dit volgens de verkoopfactuur?",
              [("Voor Restaurant De Smaak is dit een aankoopfactuur.", J), ("De btw wordt per tarief apart berekend.", J), ("De factuur moet door de klant ondertekend zijn om geldig te zijn.", F), ("De klant betaalt later: tot dan heeft de bakkerij een vordering.", J)],
              "Een factuur hoeft niet getekend te zijn. Dezelfde factuur is voor de klant een aankoopfactuur."),
        keuze("Op de leverbon die bij de levering meeging, stonden [[*enkel de aantallen|ook alle prijzen en de btw]].",
              "De bedragen staan op de factuur."),
    ]),
    volgorde("Zet de stappen van een verkoop in de juiste volgorde.",
             ["De klant stuurt een prijsaanvraag.", "De verkoper maakt een offerte.", "De verkoper levert met een leverbon.", "De verkoper stuurt de factuur.", "De verkoper volgt de betaling op."],
             "Van prijsaanvraag tot betaling."),
    casus("Reken de verkoopfactuur uit.\n\nEen drukkerij verkoopt folders aan een sportclub.\nbrutoprijs: 2 400 euro\nhandelskorting: 5 %\ndoorgerekend vervoer: 60 euro\nbtw: 21 %", [
        inv("Hoe groot is de handelskorting, in euro? Schrijf enkel het getal.", ["120"],
            "5 % van 2 400 = 120 euro."),
        inv("Hoe groot is de maatstaf van heffing, in euro? Schrijf enkel het getal.", ["2340", "2 340", "2.340"],
            "2 400 − 120 + 60 = 2 340 euro: eerst de korting eraf, dan het vervoer erbij."),
        inv("Hoeveel btw komt erbij, in euro? Schrijf het getal met een komma.", ["491,4", "491,40", "491.4", "491.40"],
            "2 340 × 0,21 = 491,40 euro."),
        inv("Hoe groot is het factuurtotaal, in euro? Schrijf het getal met een komma.", ["2831,4", "2831,40", "2 831,40", "2.831,40", "2831.4", "2831.40"],
            "2 340 + 491,40 = 2 831,40 euro."),
    ]),
    sorteer("Verhoogt of verlaagt dit het bedrag waarop de btw berekend wordt?", ["verhoogt", "verlaagt", "verandert niets"],
            [("doorgerekend vervoer", "verhoogt"), ("een handelskorting", "verlaagt"), ("een financiële korting", "verlaagt"), ("verpakking die niet terugkomt", "verhoogt"), ("terugstuurbare verpakking", "verandert niets")],
            "Terugstuurbare verpakking is een waarborg en valt buiten de maatstaf."),
    tabel("Maakt de verkoper dit document zelf?",
          [("de offerte", J), ("de leverbon", J), ("de prijsaanvraag", F), ("de uitgaande creditnota", J)],
          "De prijsaanvraag komt van de klant."),
    keuze("Een uitgaande creditnota [[*verlaagt|verhoogt]] de omzet van de verkoper en bevat [[*ook|nooit]] btw.",
          "De btw op het teruggedraaide bedrag gaat mee terug."),
    mk("Waarom houdt een verkoper een kopie van elke verkoopfactuur bij?",
       ["Als bewijs, want de wet vraagt het.", "Zo betaalt de klant sneller zijn factuur.", "Zo stijgt de btw niet bij elke nieuwe factuur.", "Zo hoeft hij geen boekhouding meer te voeren."], 0,
       "Facturen moeten een aantal jaren bewaard blijven."),
    tabel("Wat gebeurt er bij een verkoop op krediet?",
          [("de voorraad", "daalt"), ("de vordering op de klant", "stijgt"), ("de omzet", "stijgt"), ("de bank, op het moment van de factuur", "verandert niet")],
          "De klant betaalt pas later; dan pas stijgt de bank.",
          kolommen=["stijgt", "daalt", "verandert niet"]),
    keuze("De verkoper mag de btw die hij int [[*niet houden|houden]]: hij stort ze door via zijn btw-aangifte.",
          "Hij int ze voor de staat."),
    mk("Een klant stuurt 3 van de 20 bestelde stoelen terug. Wat maakt de verkoper?",
       ["een creditnota", "een nieuwe offerte", "een tweede leverbon", "een nieuwe prijsaanvraag"], 0,
       "De verkoop wordt deels teruggedraaid."),
    inv("Een klant krijgt 2 % financiële korting op 1 500 euro omdat hij binnen acht dagen betaalt. Hoe groot is die korting, in euro? Schrijf enkel het getal.", ["30"],
        "2 % van 1 500 = 30 euro."),
    tabel("Is dit een wettelijke vermelding op een verkoopfactuur?",
          [("het factuurnummer", J), ("de datum", J), ("het btw-nummer van de verkoper", J), ("de handtekening van de klant", F)],
          "Een factuur hoeft niet getekend te zijn."),
    sleep("Wat klanten nog moeten betalen, staat bij de [[handelsdebiteuren]]. De btw op de verkopen is de [[verschuldigde]] btw.",
          ["leveranciers", "aftrekbare"], "Rekening 400 en de btw die je moet doorstorten."),
    keuze("Een klant die niet betaalt: de vordering blijft [[*openstaan|vanzelf verdwijnen]] bij de handelsdebiteuren.",
          "Tot ze betaald of afgeboekt wordt."),
    open_("Waarom berekent een verkoper de btw pas na de handelskorting en niet erop?",
          "De btw komt op het bedrag dat de klant echt betaalt. Na de korting is dat bedrag kleiner, dus ook de btw. Anders zou de klant btw betalen op geld dat hij nooit uitgeeft.",
          "Eerst de kortingen eraf, dan de kosten erbij, dan pas de btw."),
    klik("Klik op de letter bij het btw-nummer van de klant.", U, [Z["H"]],
         "Restaurant De Smaak is de klant; ook zijn btw-nummer staat op de factuur."),
    tabel("Is dit voor de verkoper een opbrengst, een vordering of een schuld?",
          [("de verkoop van het brood", "opbrengst"), ("wat de klant nog moet betalen", "vordering"), ("de btw die hij aanrekende", "schuld")],
          "De opbrengst staat in klasse 7, de vordering en de btw-schuld in klasse 4.",
          kolommen=["opbrengst", "vordering", "schuld"]),
    keuze("Bij een verkoop op krediet gebeurt de levering [[*eerst|pas na de betaling]], de betaling volgt later.",
          "Tot dan heeft de verkoper een vordering."),
    inv("Hoeveel betaalt een klant voor 250 euro goederen met 21 % btw? Schrijf het getal met een komma.", ["302,5", "302,50", "302.5", "302.50"],
        "250 × 0,21 = 52,50 euro btw; 250 + 52,50 = 302,50 euro."),
]

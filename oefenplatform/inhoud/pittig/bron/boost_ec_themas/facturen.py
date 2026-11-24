"""Facturen, kortingen en btw — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen bw_facturen, met een zelfgetekende factuur om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GROEN

FA = Prent("factuur-tegelhandel", "Factuur van Tegelhandel Verbeke", "factuur met brutoprijs, kortingen, vervoer, maatstaf, btw, verpakking en totaal, elke lijn met een letter")
FA.rect(120, 60, 760, 560, "#ffffff", DONKER, 6, 2)
FA.tekst(150, 100, "Tegelhandel Verbeke · Factuur nr. 2026/418", 20, "start", vet=True)
FA.tekst(150, 128, "Klant: bv Bouwwerken Peeters · vervaldag: 30 dagen na factuurdatum", 16, "start")
LIJN = [("A", "200 m² vloertegels à 12,00 euro (brutoprijs)", "2 400,00"),
        ("B", "handelskorting 10 %", "− 240,00"),
        ("C", "financiële korting 2 % bij betaling binnen 8 dagen", "− 43,20"),
        ("D", "doorgerekend vervoer", "80,00"),
        ("E", "subtotaal", "2 196,80"),
        ("F", "btw 21 %", "461,33"),
        ("G", "terugstuurbare paletten (zonder btw)", "50,00"),
        ("H", "TE BETALEN", "2 708,13")]
Z = {}
for i, (l, tekst, bedrag) in enumerate(LIJN):
    y = 180 + i * 54
    vet = l in ("E", "H")
    FA.letter(160, y - 6, l)
    FA.tekst(195, y, tekst, 18, "start", vet=vet)
    FA.tekst(850, y, bedrag, 18, "end", vet=vet)
    Z[l] = Prent.zone(135, y - 32, 730, 50)
    if l in ("D", "G"):
        FA.lijn(190, y + 20, 860, y + 20, "#c9c3b1", 1)
U = "factuur-tegelhandel.svg"

VRAGEN = [
    klik("Klik op de lijn met het bedrag waarop de btw berekend wordt.", U, [Z["E"]],
         "De maatstaf van heffing: 2 400 − 240 − 43,20 + 80 = 2 196,80 euro."),
    klik("Klik op de korting die de klant krijgt omdat hij snel betaalt.", U, [Z["C"]],
         "De financiële korting, berekend op de prijs na de handelskorting."),
    klik("Klik op het bedrag dat de klant terugkrijgt als hij iets terugstuurt.", U, [Z["G"]],
         "Terugstuurbare verpakking: zonder btw, na de btw bij het totaal."),
    klik("Klik op de lijn die de maatstaf van heffing verhoogt.", U, [Z["D"]],
         "Doorgerekende vervoerkosten horen bij de levering."),
    tabel("Klopt dit volgens de factuur?",
          [("De financiële korting is 2 % van 2 160 euro.", J), ("Op de paletten wordt btw gerekend.", F), ("De btw is 21 % van 2 196,80 euro.", J), ("De handelskorting staat in procent.", J)],
          "Eerst de handelskorting, dan de financiële korting op wat overblijft."),
    casus("Een andere factuur.\n\nBrutoprijs goederen: 5 000 euro\nHandelskorting: 20 %\nFinanciële korting: 1 %\nDoorgerekend vervoer: 150 euro\nBtw: 21 %", [
        inv("Hoe groot is de prijs na de handelskorting? Schrijf enkel het getal.", ["4000", "4 000", "4.000"],
            "20 % van 5 000 = 1 000; 5 000 − 1 000 = 4 000."),
        inv("Hoe groot is de financiële korting? Schrijf enkel het getal.", ["40"],
            "1 % van 4 000 = 40."),
        inv("Hoe groot is de maatstaf van heffing? Schrijf enkel het getal.", ["4110", "4 110", "4.110"],
            "4 000 − 40 + 150 = 4 110."),
        inv("Hoeveel btw komt erbij? Schrijf het getal met een komma.", ["863,10", "863,1", "863.10", "863.1"],
            "4 110 × 0,21 = 863,10 euro."),
    ]),
    sorteer("Verhoogt of verlaagt dit de maatstaf van heffing?", ["verhoogt", "verlaagt", "verandert niets"],
            [("handelskorting", "verlaagt"), ("doorgerekend vervoer", "verhoogt"), ("financiële korting", "verlaagt"), ("terugstuurbare verpakking", "verandert niets"), ("doorgerekende verzekering", "verhoogt")],
            "Verpakking die je terugstuurt, staat buiten de btw."),
    tabel("Handelskorting of financiële korting?",
          [("5 % omdat de klant 1 000 stuks koopt", "handelskorting"), ("2 % bij betaling binnen 10 dagen", "financiële korting"), ("10 % voor een vaste klant", "handelskorting"), ("1 % bij contante betaling", "financiële korting")],
          "De handelskorting hangt af van de aankoop, de financiële van de betaling.",
          kolommen=["handelskorting", "financiële korting"]),
    keuze("Je berekent de financiële korting op de prijs [[*na de handelskorting|voor de handelskorting|met btw]].",
          "Eerst de handelskorting eraf."),
    inv("De brutoprijs is 800 euro, de handelskorting 15 %. Hoeveel blijft er over? Schrijf enkel het getal.", ["680"],
        "15 % van 800 = 120; 800 − 120 = 680."),
    inv("De maatstaf is 1 250 euro. Hoeveel btw komt erbij aan 21 %? Schrijf het getal met een komma.", ["262,50", "262,5", "262.50", "262.5"],
        "1 250 × 0,21 = 262,50 euro."),
    inv("Een factuur: 400 euro goederen, 21 % btw en 30 euro terugstuurbare verpakking. Hoe groot is het totaal? Schrijf enkel het getal.", ["514"],
        "Btw 84; 400 + 84 + 30 = 514 euro."),
    keuze("Een verstuurde factuur bevat een fout. Je [[*maakt een creditnota|past de factuur gewoon aan|gooit de factuur weg]].",
          "Een factuur mag je niet aanpassen."),
    tabel("Is dit een reden voor een creditnota?",
          [("de klant stuurt beschadigde goederen terug", J), ("er werd een te hoge prijs gefactureerd", J), ("de klant betaalt te laat", F), ("een korting werd vergeten", J)],
          "Een creditnota verbetert een factuur."),
    keuze("Een creditnota die een verkoop met btw terugdraait, [[*bevat ook btw|bevat nooit btw]].",
          "Anders zou de staat te veel btw krijgen."),
    sorteer("Handelsgoederen, diensten en diverse goederen of investering voor een bakker?", ["handelsgoederen", "diensten en diverse goederen", "investering"],
            [("frisdrank om door te verkopen", "handelsgoederen"), ("de verzekeringspremie", "diensten en diverse goederen"), ("een nieuwe oven", "investering"), ("de telefoonrekening", "diensten en diverse goederen")],
            "Wat je doorverkoopt, wat je verbruikt en wat jaren meegaat."),
    mk("Tegelhandel Verbeke geeft 2 % korting bij betaling binnen 8 dagen. Wat wil de handelaar daarmee bereiken?",
       ["om sneller betaald te worden", "omdat de klant veel stuks koopt", "omdat de goederen beschadigd zijn", "omdat de klant een vaste klant is"], 0,
       "Snel geld in kas is voor de leverancier iets waard."),
    keuze("Het gewone btw-tarief in België is [[*21|6|12]] %.",
          "Er bestaan ook verlaagde tarieven."),
    keuze("Een factuur met een vervaldag van 30 dagen betekent dat je [[*30 dagen hebt om te betalen|na 30 dagen een korting krijgt|30 dagen moet wachten om te betalen]].",
          "De vervaldag is de uiterste betaaldatum."),
    sleep("Op de factuur gaat eerst de [[handelskorting]] van de brutoprijs af, daarna de [[financiële korting]]. Na het [[vervoer]] erbij te tellen, heb je de maatstaf van heffing.",
          ["btw", "verpakking"], "De volgorde op een factuur."),
    klik("Klik op de lijn met de prijs vóór elke korting.", U, [Z["A"]],
         "De brutoprijs: 200 × 12 = 2 400 euro."),
    inv("Hoe heet het bedrag waarop je de btw berekent? Schrijf vier woorden.", ["maatstaf van heffing", "de maatstaf van heffing"],
        "Op de factuur van Verbeke is dat het subtotaal van 2 196,80 euro."),
    keuze("Een doorgerekende verzekering op de factuur [[*verhoogt|verlaagt|verandert niets aan]] de maatstaf van heffing.",
          "Doorgerekende kosten horen bij de levering."),
    inv("De brutoprijs is 3 000 euro met 10 % handelskorting en daarna 2 % financiële korting. Hoe groot is de maatstaf van heffing? Schrijf enkel het getal.", ["2646", "2 646", "2.646"],
        "3 000 − 300 = 2 700; 2 % van 2 700 = 54; 2 700 − 54 = 2 646."),
    tabel("Komt er btw op dit bedrag?",
          [("de goederen na de kortingen", J), ("het doorgerekende vervoer", J), ("de terugstuurbare kratten", F)],
          "Enkel de terugstuurbare verpakking blijft buiten de btw."),
    keuze("De financiële korting gaat van de maatstaf af, [[*ook als de klant er niet van gebruikmaakt|alleen als de klant echt snel betaalt]].",
          "Zo staat het in de regels voor de maatstaf van heffing."),
    open_("Leg uit waarom een terugstuurbare verpakking zonder btw op de factuur staat.",
          "De verpakking wordt niet echt verkocht: het is een soort waarborg die de klant terugkrijgt als hij ze terugstuurt.",
          "Geen verkoop, dus geen btw."),
]

"""Het loon: van bruto naar netto — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_loon, met een zelfgetekende loonbrief om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, GRIJS

LB = Prent("loonbrief-oktober", "", "loonbrief van oktober met vijf bedragen en letters A tot E")
LB.rect(90, 24, 820, 596, "#ffffff", DONKER, 14, 3)
LB.rect(90, 24, 820, 66, LICHTGROEN, DONKER, 14, 3)
LB.tekst(500, 67, "Loonbrief oktober 2026 — Jonas Claes, magazijnier", 24, vet=True)
LB.tekst(140, 130, "werkgever: bv Groen & Fris, Alken", 18, "start")
LB.tekst(860, 130, "gewerkte dagen: 20", 18, "end")
LB.lijn(120, 150, 880, 150, GRIJS, 2)
REGELS = [
    ("A", "brutoloon (152 uur × 15,00 euro)", "2 280,00"),
    ("B", "werknemersbijdrage RSZ (13,07 %)", "− 298,00"),
    ("C", "belastbaar loon", "1 982,00"),
    ("D", "bedrijfsvoorheffing", "− 380,00"),
    ("E", "nettoloon", "1 602,00"),
]
Y0, DY = 210, 82
for i, (t, r, b) in enumerate(REGELS):
    y = Y0 + i * DY
    LB.letter(140, y - 7, t)
    LB.tekst(180, y, r, 22, "start")
    LB.tekst(860, y, b + " euro", 22, "end", vet=True)
    if t in ("B", "D"):
        LB.lijn(560, y + 26, 880, y + 26, GRIJS, 2)
U = "loonbrief-oktober.svg"
Z = {t: Prent.rond(140, Y0 + i * DY - 7, 30) for i, (t, _, _) in enumerate(REGELS)}

VRAGEN = [
    klik("Klik op de letter bij het bedrag dat op de rekening van Jonas komt.", U, [Z["E"]],
         "Het nettoloon: wat overblijft na alle afhoudingen."),
    klik("Klik op de letter bij het voorschot op de personenbelasting.", U, [Z["D"]],
         "De bedrijfsvoorheffing houdt de werkgever af en stort hij door aan de fiscus."),
    klik("Klik op de letter bij de afhouding voor de sociale zekerheid.", U, [Z["B"]],
         "De werknemersbijdrage RSZ gaat naar pensioen, ziekteverzekering, werkloosheid en gezinsbijslag."),
    klik("Klik op de letter bij het bedrag waarop de bedrijfsvoorheffing berekend wordt.", U, [Z["C"]],
         "Het belastbaar loon: het brutoloon na aftrek van de RSZ-bijdrage."),
    klik("Klik op de letter bij het bedrag dat in de arbeidsovereenkomst van Jonas staat.", U, [Z["A"]],
         "Het brutoloon is het loon vóór de afhoudingen."),
    casus("Bekijk de loonbrief van Jonas.", [
        tabel("Klopt dit volgens de loonbrief?",
              [("Het nettoloon is lager dan het brutoloon.", J), ("De bedrijfsvoorheffing wordt van het brutoloon berekend.", F), ("Jonas kan zijn gewerkte dagen nakijken.", J), ("De patronale bijdrage staat bij de afhoudingen van Jonas.", F)],
              "De voorheffing wordt berekend op het belastbaar loon. De patronale bijdrage betaalt de werkgever bovenop het brutoloon."),
        inv("Hoeveel werd er in totaal van het brutoloon afgehouden, in euro? Schrijf enkel het getal.", ["678", "678,00", "678.00"],
            "298 + 380 = 678 euro, of 2 280 − 1 602."),
        mk("Jonas werkte in oktober eigenlijk 160 uur. Wat doet hij best?",
           ["het zijn werkgever laten nakijken", "niets, want de loonbrief is altijd juist", "zelf zijn nettoloon op de brief aanpassen", "een nieuwe DIMONA-aangifte laten doen"], 0,
           "Een vergeten uur vind je enkel door je loonbrief na te kijken."),
    ]),
    volgorde("Zet de stappen van een eenvoudige loonberekening in de juiste volgorde.",
             ["Het brutoloon bepalen.", "De werknemersbijdrage RSZ aftrekken.", "Het belastbaar loon bekomen.", "De bedrijfsvoorheffing aftrekken.", "Het nettoloon bekomen."],
             "Eerst de RSZ eraf, dan de voorheffing."),
    casus("Reken het loon uit.\n\nLaura is deeltijds bediende. Haar brutoloon is 1 500 euro. De werknemersbijdrage RSZ is 13,07 %. De bedrijfsvoorheffing is 150 euro.", [
        inv("Hoe groot is haar RSZ-bijdrage, in euro? Rond af op twee cijfers na de komma.", ["196,05", "196.05", "196,05 euro"],
            "1 500 × 0,1307 = 196,05 euro."),
        inv("Hoe groot is haar belastbaar loon, in euro? Schrijf het getal.", ["1303,95", "1 303,95", "1303.95", "1.303,95"],
            "1 500 − 196,05 = 1 303,95 euro."),
        inv("Hoe groot is haar nettoloon, in euro? Schrijf het getal.", ["1153,95", "1 153,95", "1153.95", "1.153,95"],
            "1 303,95 − 150 = 1 153,95 euro."),
    ]),
    tabel("Bruto of netto?",
          [("het bedrag in je contract", "bruto"), ("het bedrag op je rekening", "netto"), ("het loon vóór de afhoudingen", "bruto"), ("wat je echt krijgt", "netto")],
          "Van bruto gaan de RSZ en de voorheffing af.",
          kolommen=["bruto", "netto"]),
    sorteer("Waar gaat dit bedrag naartoe?", ["sociale zekerheid", "fiscus", "werknemer"],
            [("de werknemersbijdrage RSZ", "sociale zekerheid"), ("de bedrijfsvoorheffing", "fiscus"), ("het nettoloon", "werknemer"), ("de patronale bijdrage", "sociale zekerheid")],
            "De RSZ int de sociale bijdragen; de voorheffing gaat naar de fiscus."),
    keuze("De patronale bijdrage betaalt de [[*werkgever|werknemer]] bovenop het brutoloon. Daarom is de loonkost [[*hoger|lager]] dan het brutoloon.",
          "Een werknemer kost meer dan zijn brutoloon."),
    mk("Ali en Bert hebben hetzelfde brutoloon, maar Ali heeft drie kinderen ten laste. Wat is waar?",
       ["Ali heeft wellicht een hoger nettoloon.", "Ze hebben altijd exact hetzelfde nettoloon.", "Ali betaalt een hogere RSZ-bijdrage.", "Bert krijgt geen bedrijfsvoorheffing."], 0,
       "De bedrijfsvoorheffing hangt ook af van de gezinssituatie en de kinderen ten laste."),
    tabel("Speelt dit mee voor de hoogte van de bedrijfsvoorheffing?",
          [("de hoogte van het loon", J), ("de gezinssituatie", J), ("het aantal kinderen ten laste", J), ("de kleur van je bedrijfswagen", F)],
          "Daarom zijn er officiële tabellen voor elke situatie."),
    keuze("De bedrijfsvoorheffing is een [[*voorschot|eindafrekening]] op de personenbelasting. Was ze te hoog, dan krijg je bij je aangifte geld [[*terug|bij te betalen]].",
          "De eindafrekening komt met het aanslagbiljet."),
    tabel("Wat staat er op het jaaroverzicht 281.10 van een werknemer?",
          [("het totale brutoloon van het jaar", J), ("de ingehouden bedrijfsvoorheffing", J), ("de omzet van de onderneming", F), ("de identiteit van de werknemer", J)],
          "Het gaat over één werknemer, niet over de zaak."),
    mk("Waarvoor gebruik je het jaaroverzicht 281.10?",
       ["voor je belastingaangifte", "voor de DIMONA-aangifte", "voor je sollicitatiebrief", "voor je schriftelijke opzegging"], 0,
       "De bedragen vul je in bij je personenbelasting."),
    koppel("Welke extra hoort bij welke omschrijving?",
           [("vakantiegeld", "een bedrag bovenop het loon, meestal in mei of juni"), ("eindejaarspremie", "een dertiende maand in december"), ("patronale bijdrage", "RSZ die de werkgever zelf betaalt")],
           ["bedrijfsvoorheffing"], "Drie bedragen die naast het gewone loon staan."),
    keuze("Wie bedrijfsvoorheffing betaalde, moet [[*toch|geen]] belastingaangifte doen.",
          "Daar wordt de voorheffing mee verrekend."),
    inv("Een werknemer werkt 120 uur aan 14 euro bruto per uur. Hoe groot is zijn brutoloon, in euro? Schrijf enkel het getal.", ["1680", "1 680", "1.680"],
        "120 × 14 = 1 680 euro."),
    tabel("Klopt dit over de RSZ?",
          [("De werkgever houdt de RSZ-bijdrage af van het loon.", J), ("De bedrijfsvoorheffing is een deel van de RSZ-bijdrage.", F), ("De RSZ-bijdrage dient voor pensioen en ziekteverzekering.", J)],
          "RSZ en voorheffing zijn twee verschillende afhoudingen."),
    sleep("Het brutoloon min de RSZ-bijdrage is het [[belastbaar loon]]. Daarvan gaat de [[bedrijfsvoorheffing]] af en wat overblijft is het nettoloon.",
          ["patronale bijdrage", "vakantiegeld"], "Twee stappen van bruto naar netto."),
    open_("Waarom kijkt een werknemer best elke maand zijn loonbrief na?",
          "Zo kan hij controleren of zijn gewerkte dagen, overuren, premies en afhoudingen juist zijn. Een vergeten overuur of een verkeerd aantal dagen vind je enkel door de loonbrief na te kijken.",
          "Fouten op de loonbrief kosten je geld."),
    mk("Wat kost een werknemer zijn werkgever?",
       ["meer dan zijn brutoloon", "precies zijn nettoloon", "precies zijn brutoloon", "minder dan zijn nettoloon"], 0,
       "Bovenop het brutoloon betaalt de werkgever nog de patronale bijdrage."),
    keuze("Twee werknemers met hetzelfde brutoloon kunnen een [[*ander|identiek]] nettoloon hebben.",
          "De bedrijfsvoorheffing hangt ook af van de gezinssituatie."),
    inv("Een brutoloon is 2 000 euro, de RSZ-bijdrage is 261,40 euro en de bedrijfsvoorheffing 310 euro. Hoe groot is het nettoloon, in euro? Schrijf het getal.", ["1428,6", "1428,60", "1 428,60", "1 428,6", "1428.6", "1428.60"],
        "2 000 − 261,40 = 1 738,60 belastbaar; 1 738,60 − 310 = 1 428,60 euro."),
    tabel("Wie bezorgt dit aan de werknemer?",
          [("de maandelijkse loonbrief", "werkgever"), ("het jaaroverzicht 281.10", "werkgever"), ("het aanslagbiljet na de aangifte", "fiscus")],
          "De werkgever, of zijn sociaal secretariaat, bezorgt de loonbrieven en het jaaroverzicht.",
          kolommen=["werkgever", "fiscus"]),
]

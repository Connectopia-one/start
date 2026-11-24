"""Aankopen, verkopen en bankverrichtingen boeken — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Pittige verrichtingen uit Economie Boost doorstroom (aankoop, verkoop, betaling,
creditnota), aangevuld met eigen vragen strikt binnen te_registreren en een
zelfgetekend bankrekeninguittreksel om de bewegingen aan te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS
from ..boost_ec_themas import boekhouden as _bh

BU = Prent("bankuittreksel-mei", "", "bankrekeninguittreksel van een winkel met oud saldo, vier bewegingen en nieuw saldo, met letters A tot F")
BU.rect(80, 40, 840, 560, "#ffffff", DONKER, 10)
BU.tekst(110, 82, "Bank Limburg · Rekeninguittreksel nr. 5", 22, "start", vet=True)
BU.tekst(110, 112, "Rekening van Fietsen Trappers bv · BE00 0000 0000 0000", 16, "start", kleur=GRIJS)
BU.rect(110, 135, 780, 40, "#eef1e8", "none", 0, 0)
for x, t in ((120, "datum"), (230, "omschrijving"), (870, "bedrag")):
    BU.tekst(x, 162, t, 17, "end" if t == "bedrag" else "start", vet=True)
RIJ = [("", "Oud saldo", "3 200,00"), ("02/05", "Ontvangst klant Fietshoek, factuur 27/041", "+ 1 452,00"),
       ("06/05", "Betaling leverancier Velo Parts, factuur 7781", "- 2 420,00"), ("15/05", "Storting uit de kas", "+ 500,00"),
       ("31/05", "Bankkosten mei", "- 6,50"), ("", "Nieuw saldo", "2 725,50")]
for i, (d, o, b) in enumerate(RIJ):
    y = 215 + i * 56
    vet = o.endswith("saldo")
    if vet:
        BU.lijn(110, y - 30, 890, y - 30, GRIJS, 1)
    BU.tekst(120, y, d, 17, "start")
    BU.tekst(230, y, o, 17, "start", vet=vet)
    BU.tekst(870, y, b, 17, "end", vet=vet)
LET = {"A": (60, 215), "B": (60, 271), "C": (60, 327), "D": (60, 383), "E": (60, 439), "F": (60, 495)}
for t, (x, y) in LET.items():
    BU.letter(x, y - 6, t)
U = "bankuittreksel-mei.svg"
Z = {t: Prent.rond(x, y - 6, 28) for t, (x, y) in LET.items()}

VRAGEN = [_bh.VRAGEN[i] for i in (0, 3, 4, 7, 10, 11, 12)] + [
    klik("Klik op de letter bij de beweging waarbij de handelsdebiteuren dalen.", U, [Z["B"]],
         "Een klant betaalt: de bank stijgt en de vordering op de klant daalt."),
    klik("Klik op de letter bij de beweging die je boekt met 440 Leveranciers in debet.", U, [Z["C"]],
         "Je betaalt een leverancier: de schuld daalt en komt in debet, de bank in credit."),
    klik("Klik op de letter bij de beweging waarbij de rekening 570 Kassen in credit komt.", U, [Z["D"]],
         "Geld gaat uit de kas naar de bank: de kas daalt, de bank stijgt."),
    klik("Klik op de letter bij de beweging die een financiële kost is.", U, [Z["E"]],
         "Bankkosten horen bij het financieel resultaat."),
    casus("Bekijk het bankrekeninguittreksel van mei.", [
        inv("Hoeveel euro kwam er in mei in totaal binnen op de bankrekening? Schrijf enkel het getal.", ["1952"],
            "1452 + 500 = 1952 euro."),
        tabel("Klopt dit volgens het uittreksel?",
              [("Het nieuwe saldo is het oude saldo plus de ontvangsten min de uitgaven.", J), ("De ontvangst van 1452 euro is een nieuwe verkoop die je als omzet boekt.", F), ("De betaling aan Velo Parts verlaagt de bank.", J), ("Het uittreksel is een bewijsstuk dat je bewaart.", J)],
              "De omzet was al geboekt bij de factuur; bij de betaling verhuist enkel het geld."),
        keuze("Voor de bank schrijft Bank Limburg de ontvangst van de klant in haar eigen boeken in [[*credit|debet]]; voor Fietsen Trappers is het een ontvangst.",
              "De bank schrijft vanuit haar eigen boekhouding."),
    ]),
    tabel("Debet of credit bij de boeking van een aankoopfactuur?",
          [("604 Aankopen handelsgoederen", "debet"), ("411 Terug te vorderen btw", "debet"), ("440 Leveranciers", "credit")],
          "Kost en btw in debet, de schuld aan de leverancier in credit.",
          kolommen=["debet", "credit"]),
    casus("Een winkel koopt fietsen: 4 000 euro, 10 % handelskorting, 80 euro doorgerekende vervoerkosten, en 21 % btw op het geheel.", [
        inv("Welk bedrag boek je op de rekening aankopen handelsgoederen? Schrijf enkel het getal.", ["3600"],
            "4000 min 10 % korting is 3600; de handelskorting krijgt geen eigen rekening."),
        inv("Hoeveel euro btw rekent de leverancier aan? Schrijf enkel het getal.", ["772,8", "772.8", "772,80", "772.80"],
            "(3600 + 80) maal 21 % is 772,80 euro."),
        inv("Welk bedrag boek je in credit bij de leverancier? Schrijf enkel het getal.", ["4452,8", "4452.8", "4452,80", "4452.80"],
            "3600 + 80 + 772,80 = 4452,80 euro."),
    ]),
    keuze("De doorgerekende vervoerkosten boek je [[*op een eigen kostenrekening voor aankoopkosten|bij de terug te vorderen btw|bij de handelsdebiteuren]].",
          "Ze verhogen de kostprijs van de aankoop."),
    mk("Een inkomende creditnota van 200 euro plus 42 euro btw. Wat staat er in debet?",
       ["242 euro bij de leveranciers", "200 euro bij de aankopen handelsgoederen", "42 euro bij de terug te vorderen btw", "242 euro bij de rekening van de bank"], 0,
       "Omgekeerd aan de factuur: de schuld daalt en komt in debet."),
    keuze("De boekhouding toont een kassaldo van 450 euro. Bij het tellen zit er 430 euro in de kas. Dan [[*zoek je het verschil|pas je het saldo zonder meer aan|is er niets aan de hand]].",
          "Het getelde geld moet kloppen met de boekhouding."),
    open_("Een collega boekt de betaling van een klant als een nieuwe verkoop. Leg uit wat er fout is en wat het gevolg is.",
          "De verkoop werd al geboekt toen de factuur vertrok. Bij de betaling stijgt enkel de bank en dalen de handelsdebiteuren. Boekt hij ze opnieuw als verkoop, dan telt de omzet dubbel en lijkt de winst groter dan ze is.",
          "Bij een betaling verhuist enkel het geld."),
]

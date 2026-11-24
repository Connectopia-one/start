"""Producten, merken, prijsstrategie en distributie — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen bw_product, met een zelfgetekende productlevenscyclus om op te klikken."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, BLAUW, GRIJS

PL = Prent("productlevenscyclus", "Verkoop van een product in de tijd", "verkoopcurve van een product met vijf zones A tot E langs de tijdas")
OX, OY = 120, 540
PL.lijn(OX, OY, OX + 800, OY, DONKER, 3); PL.lijn(OX, OY, OX, 70, DONKER, 3)
PL.tekst(OX + 800, OY + 40, "tijd", 18, "end"); PL.tekst(OX - 10, 60, "verkoop", 18, "start")
def v(t):  # t van 0 tot 10
    if t < 2: return 0
    return 380 * math.exp(-((t - 6.2) / 2.3) ** 2) * (1 if t > 2.6 else (t - 2) / 0.6)
pts = [(OX + t * 78, OY - v(t)) for t in [i / 10 for i in range(0, 101)]]
PL.pad("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts), "none", BLAUW, 4)
GRENS = [0, 2, 3.6, 5.2, 7.2, 10]
for g in GRENS[1:-1]:
    PL.lijn(OX + g * 78, OY, OX + g * 78, 90, "#b9b3a2", 2, True)
Z = {}
for i, l in enumerate("ABCDE"):
    a, b = GRENS[i], GRENS[i + 1]
    xm = OX + (a + b) / 2 * 78
    PL.letter(xm, OY + 34, l)
    Z[l] = Prent.zone(OX + a * 78, 90, (b - a) * 78, OY - 90 + 60)
U = "productlevenscyclus.svg"

VRAGEN = [
    klik("Klik op de fase waarin de verkoop het snelst stijgt.", U, [Z["C"]],
         "De groeifase: de curve loopt het steilst omhoog."),
    klik("Klik op de fase waarin er nog niets verkocht wordt, omdat het product nog bedacht en getest wordt.", U, [Z["A"]],
         "De ontwikkelingsfase: kosten zonder verkoop."),
    klik("Klik op de fase waarin de verkoop hoog blijft maar nauwelijks nog stijgt.", U, [Z["D"]],
         "De volwassenheidsfase: de markt is verzadigd."),
    klik("Klik op de fase waarin het bedrijf moet kiezen: het product vernieuwen of laten verdwijnen.", U, [Z["E"]],
         "De neergangsfase: de verkoop daalt."),
    klik("Klik op de fase waarin een afroomstrategie het best past.", U, [Z["B"]],
         "In de introductiefase is er nog geen alternatief: early adopters betalen een hoge prijs."),
    sorteer("Convenience, shopping, speciality of unsought goed?", ["convenience", "shopping", "speciality", "unsought"],
            [("een pak melk", "convenience"), ("een winterjas", "shopping"), ("een sportwagen van één bepaald merk", "speciality"), ("een uitvaartverzekering", "unsought"), ("een krant", "convenience"), ("een nieuwe zetel", "shopping")],
            "Hoeveel moeite doet de koper?"),
    tabel("Breed of diep assortiment?",
          [("een winkel met brood, groenten, vlees, drank en schoonmaakmiddelen", "breed"), ("een winkel met 40 soorten thee", "diep"), ("een warenhuis met kleding, speelgoed en elektro", "breed")],
          "Breedte is het aantal productgroepen, diepte het aantal varianten binnen één groep.",
          kolommen=["breed", "diep"]),
    tabel("Lijnextensie, merkextensie of multibrands?",
          [("een frisdrankmerk brengt een versie zonder suiker uit", "lijnextensie"), ("een sportschoenenmerk verkoopt ook horloges", "merkextensie"), ("een wasmiddelenfabrikant verkoopt twee eigen merken in hetzelfde rek", "multibrands")],
          "Zelfde groep, nieuwe groep, of twee eigen merken naast elkaar.",
          kolommen=["lijnextensie", "merkextensie", "multibrands"]),
    koppel("Welke prijsstrategie hoort bij welke omschrijving?",
           [("cost-plus pricing", "kostprijs plus een vaste marge"), ("consumer-based pricing", "wat de klant ervoor wil betalen"), ("competitor-based pricing", "net onder of boven de concurrent"), ("premium pricing", "een hoge prijs als teken van kwaliteit")],
           ["gratis weggeven"], "Vier manieren om een prijs te bepalen."),
    inv("Een fabrikant maakt een fiets voor 300 euro en rekent 40 % marge (cost-plus). Wat is de verkoopprijs? Schrijf enkel het getal.", ["420"],
        "40 % van 300 = 120; 300 + 120 = 420 euro."),
    tabel("Afroom- of penetratiestrategie?",
          [("een nieuwe spelconsole start aan 600 euro en zakt na een jaar", "afroom"), ("een nieuwe streamingdienst kost de eerste drie maanden 1 euro", "penetratie"), ("een nieuwe smartphone zonder concurrent start heel duur", "afroom")],
          "Afromen: hoog beginnen. Penetreren: laag beginnen om snel klanten te winnen.",
          kolommen=["afroom", "penetratie"]),
    tabel("Intensieve, selectieve of exclusieve distributie?",
          [("chewinggum in elke supermarkt, tankstation en krantenwinkel", "intensief"), ("een merk van wandelschoenen in een beperkt aantal sportwinkels", "selectief"), ("een luxehorloge enkel bij één juwelier per stad", "exclusief")],
          "Overal, in enkele gekozen punten, of in één punt per gebied.",
          kolommen=["intensief", "selectief", "exclusief"]),
    sorteer("Push- of pullstrategie?", ["push", "pull"],
            [("een producent geeft winkeliers extra korting om het product in te slaan", "push"), ("een tv-reclame waarna klanten in de winkel naar het product vragen", "pull"), ("een sterke merknaam waar klanten naar zoeken", "pull"), ("bonussen voor verkopers die het product aanraden", "push")],
            "Push duwt via de winkel; pull trekt via de klant."),
    keuze("Een A-merk is meestal [[*duurder|goedkoper]] dan een winkelmerk.",
          "Het A-merk heeft eigen reclame en een bekende naam."),
    mk("Waarom zet een supermarkt een budgetmerk naast een A-merk?",
       ["Om elke klant te bedienen.", "Omdat A-merken verboden zijn.", "Omdat budgetmerken altijd beter zijn.", "Om de breedte van het assortiment te verkleinen."], 0,
       "Prijsbewuste klanten en merkentrouwe klanten vinden allebei iets."),
    keuze("Studenten betalen minder voor een bioscoopticket dan andere bezoekers. Dat is [[*prijsdiscriminatie|premium pricing|cost-plus pricing]].",
          "Een andere prijs per groep klanten voor hetzelfde product."),
    keuze("Een duurzaam goed, zoals een koelkast, gebruik je [[*meermaals en lang|één keer]].",
          "Niet-duurzame goederen zijn snel op."),
    tabel("Klopt dit over de productlevenscyclus?",
          [("Na de introductiefase komt de groeifase.", J), ("In de volwassenheidsfase groeit de verkoop het snelst.", F), ("In de neergangsfase daalt de verkoop.", J)],
          "De groei is het snelst in de groeifase."),
    keuze("Een fabrikant die zijn machines koopt bij een ander bedrijf, koopt [[*industriële goederen|convenience goederen|unsought goederen]].",
          "Goederen om zelf mee te werken."),
    sleep("Bij [[e-commerce]] verkoopt een bedrijf via het internet. Bij [[intensieve]] distributie ligt een product in zoveel mogelijk verkooppunten.",
          ["exclusieve", "multibrands"], "Plaats in de marketingmix."),
    keuze("Een premiumprijs werkt alleen als het product [[*echt meer kwaliteit of prestige biedt|het goedkoopste van de markt is|nog niet bestaat]].",
          "Anders kopen klanten bij de concurrent."),
    volgorde("Zet de fases van de productlevenscyclus in de juiste volgorde.",
             ["ontwikkeling", "introductie", "groei", "volwassenheid", "neergang"],
             "Van idee tot verdwijnen."),
    tabel("Welke soort winkelmerk is dit?",
          [("het goedkoopste huismerk in een witte verpakking", "budget"), ("het gewone huismerk van de keten", "standaard"), ("een huismerk met biologische producten", "bio")],
          "Een keten zet vaak drie eigen lijnen naast elkaar.",
          kolommen=["standaard", "budget", "bio"]),
    keuze("Een brandblusser koop je pas als je er echt aan denkt. Het is een [[*unsought|convenience|shopping]] goed.",
          "Je zoekt het niet, en toch heb je het soms nodig."),
    inv("Een winkel koopt een jas aan voor 50 euro en rekent 60 % marge. Wat is de verkoopprijs zonder btw? Schrijf enkel het getal.", ["80"],
        "60 % van 50 = 30; 50 + 30 = 80 euro."),
    keuze("Een merk zet zijn prijs net onder die van de grootste concurrent. Dat is [[*competitor-based pricing|cost-plus pricing|premium pricing]].",
          "De prijs vertrekt van de concurrentie."),
    keuze("Bij consumer-based pricing vertrekt de prijs van [[*de waarde die de klant eraan geeft|de kostprijs van het product|de prijs van de concurrent]].",
          "Wat is de klant bereid te betalen?"),
    keuze("Een merk van dure designerkledij kiest meestal voor [[*exclusieve|intensieve]] distributie.",
          "Weinig verkooppunten passen bij het exclusieve imago."),
    tabel("Duurzaam of niet-duurzaam goed?",
          [("een fiets", "duurzaam"), ("tandpasta", "niet-duurzaam"), ("een laptop", "duurzaam"), ("een brood", "niet-duurzaam")],
          "Duurzame goederen gebruik je lang en meermaals.",
          kolommen=["duurzaam", "niet-duurzaam"]),
    open_("Een chocolademerk wil een nieuwe reep lanceren. Kies een prijsstrategie en leg uit waarom.",
          "Penetratie: een lage prijs bij de start, zodat veel mensen de reep proberen en het merk snel marktaandeel wint tegenover de vele concurrenten.",
          "Afromen past bij iets zonder alternatief; penetratie bij een markt met veel concurrentie."),
]

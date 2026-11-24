"""Grafieken maken en lezen — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_grafieken, met een zelfgetekende kolomgrafiek om de
grafiekelementen aan te klikken, aangevuld met enkele pittige vragen uit Statistiek
en Samenleving en economie Beyond."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE
from ..beyond_st_themas import grafieken as _g
from ..beyond_se_themas import excel as _x

KG = Prent("kolomgrafiek-omzet", "Omzet Fietsen Trappers per kwartaal", "kolomgrafiek met twee reeksen 2026 en 2027 per kwartaal, met letters A tot F bij de grafiekelementen")
OX, OY, H = 150, 540, 400   # oorsprong; 0 tot 100 duizend euro
def Y(v): return OY - v / 100 * H
for v in range(0, 101, 20):
    KG.lijn(OX, Y(v), 860, Y(v), "#e2ded2", 1)
    KG.tekst(OX - 10, Y(v) + 6, str(v), 16, "end")
KG.lijn(OX, OY, 860, OY, DONKER, 2); KG.lijn(OX, OY, OX, 110, DONKER, 2)
DATA = [("kw 1", 40, 48), ("kw 2", 75, 82), ("kw 3", 90, 70), ("kw 4", 35, 52)]
for i, (k, a, b) in enumerate(DATA):
    x = OX + 40 + i * 172
    KG.rect(x, Y(a), 55, OY - Y(a), BLAUW, "none", 0, 0)
    KG.rect(x + 60, Y(b), 55, OY - Y(b), ORANJE, "none", 0, 0)
    KG.tekst(x + 57, OY + 26, k, 17)
KG.tekst(OX + 40 + 2 * 172 + 87, Y(70) - 8, "70", 16, vet=True)
KG.tekst(80, 96, "omzet (duizend euro)", 17, "start", kleur=DONKER)
KG.rect(700, 70, 22, 16, BLAUW, "none", 0, 0); KG.tekst(730, 84, "2026", 16, "start")
KG.rect(790, 70, 22, 16, ORANJE, "none", 0, 0); KG.tekst(820, 84, "2027", 16, "start")
LET = {"A": (500, 34 + 26), "B": (44, 90), "C": (900, 78), "D": (650, Y(70) - 40), "E": (900, Y(60)), "F": (500, OY + 66)}
for t, (x, y) in LET.items():
    KG.letter(x, y, t)
U = "kolomgrafiek-omzet.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}

VRAGEN = [_g.VRAGEN[i] for i in (0, 8)] + [_x.VRAGEN[i] for i in (11, 23)] + [
    klik("Klik op de letter bij de legende.", U, [Z["C"]],
         "De legende zegt welke kleur bij welke reeks hoort: blauw is 2026, oranje 2027."),
    klik("Klik op de letter bij de astitel.", U, [Z["B"]],
         "De astitel zegt wat de as meet: de omzet in duizend euro."),
    klik("Klik op de letter bij een gegevenslabel.", U, [Z["D"]],
         "Het getal 70 boven de kolom is een gegevenslabel: de precieze waarde."),
    klik("Klik op de letter bij de rasterlijnen.", U, [Z["E"]],
         "De lichte horizontale lijnen helpen om de hoogte af te lezen."),
    klik("Klik op de letter bij de categorieën op de horizontale as.", U, [Z["F"]],
         "Op de horizontale as van een kolomgrafiek staan de categorieën: hier de kwartalen."),
    casus("Bekijk de kolomgrafiek van Fietsen Trappers.", [
        tabel("Klopt dit volgens de grafiek?",
              [("De grafiek toont twee gegevensreeksen.", J), ("In kwartaal 3 was de omzet in 2027 lager dan in 2026.", J), ("In elk kwartaal steeg de omzet van 2026 naar 2027.", F), ("De verticale as begint bij nul.", J)],
              "In kwartaal 3 daalde de omzet van 90 naar 70 duizend euro."),
        inv("Hoeveel duizend euro omzet maakte de winkel in 2027 in totaal? Schrijf enkel het getal.", ["252"],
            "48 + 82 + 70 + 52 = 252 duizend euro."),
        keuze("Wil je enkel het verloop van de omzet in 2027 over de kwartalen tonen, dan kies je best een [[*lijngrafiek|cirkeldiagram|staafgrafiek met liggende balken]].",
              "Een lijn toont een verloop in de tijd."),
    ]),
    tabel("Welke grafiek kies je?",
          [("de omzet per maand over een heel jaar", "lijngrafiek"), ("het aandeel van lonen, huur en aankopen in de kosten", "cirkeldiagram"), ("de omzet van vier filialen naast elkaar", "kolomgrafiek"), ("het verloop van het aantal klanten per week", "lijngrafiek")],
          "Verloop in de tijd wordt een lijn, delen van een geheel een cirkel, vergelijken kolommen.",
          kolommen=["kolomgrafiek", "lijngrafiek", "cirkeldiagram"]),
    tabel("Maakt dit een grafiek misleidend?",
          [("een verticale as die bij 90 begint", J), ("een as met ongelijke stappen", J), ("een stuk uit de reeks weglaten", J), ("een duidelijke titel", F)],
          "Een eerlijke grafiek begint bij nul en toont de hele reeks."),
    keuze("Een staafgrafiek heeft [[*liggende|staande]] balken, een kolomgrafiek [[*staande|liggende]].",
          "Liggende balken zijn handig bij lange namen."),
    mk("Een cirkeldiagram van de kosten telt samen 112 %. Wat is er aan de hand?",
       ["Er zit een fout in de cijfers.", "De zaak maakte veel winst.", "De cirkel is te klein getekend.", "Er zijn te weinig schijfjes."], 0,
       "De hele cirkel is honderd procent."),
    keuze("Je wijzigt een getal in het rekenblad. De grafiek [[*verandert mee|blijft zoals ze was]], want ze kijkt naar het bereik.",
          "Dat is net het nut ervan."),
    sorteer("Hoort dit in de grafiek of in de tabel ernaast?", ["grafiek", "tabel"],
            [("een beeld van het verloop", "grafiek"), ("de exacte waarden tot op de euro", "tabel"), ("een snelle vergelijking in één oogopslag", "grafiek"), ("de cijfers om mee verder te rekenen", "tabel")],
            "Een grafiek toont een beeld, een tabel de exacte waarden."),
    tabel("Welke informatie heeft een lezer nodig om je grafiek te begrijpen?",
          [("wat er gemeten is", J), ("in welke eenheid", J), ("over welke periode", J), ("wie de grafiek maakte", F)],
          "Titel, astitel en eenheid maken een grafiek leesbaar."),
    keuze("Bij cijfers van iemand anders zet je onder de grafiek [[*de bron|je eigen naam|een legende]].",
          "Waar de cijfers vandaan komen en van welk jaar."),
    mk("Waarom houd je een cirkeldiagram bij een handvol schijfjes?",
       ["Met te veel schijfjes leest niemand het nog.", "Een cirkel kan maar vier kleuren tonen.", "Meer schijfjes maken de som groter dan 100 %.", "Het rekenblad laat er niet meer toe."], 0,
       "Te veel kleine stukjes zijn niet te vergelijken."),
    sleep("Eén rij met waarden in een grafiek is een [[gegevensreeks]]. Het getal bij een kolom is een [[gegevenslabel]].",
          ["legende", "astitel"], "Twee grafiekbegrippen."),
    keuze("Een piek in een lijngrafiek van de verkoop is een periode met [[*veel|weinig]] verkoop; zoek er een verklaring bij, zoals een actie of een feestdag.",
          "Een grafiek vertel je met uitleg."),
    open_("De omzet van een winkel in kwartaal 3 daalde. Waarom is een grafiek met twee reeksen naast elkaar handig om dat aan de zaakvoerder te tonen?",
          "Met de kolommen van twee jaren per kwartaal naast elkaar ziet hij in één oogopslag in welk kwartaal de omzet daalde en hoe groot het verschil is. Een rij getallen moet hij eerst zelf vergelijken.",
          "Een beeld laat een verschil sneller zien dan een rij getallen."),
keuze("Om een grafiek te maken selecteer je eerst [[*het bereik met de gegevens|een lege cel|enkel de titel]].",
          "Het rekenblad tekent wat je geselecteerd hebt."),
    tabel("Wat pas je aan via de grafiekopties?",
          [("de kleur van een reeks", J), ("de titel boven de grafiek", J), ("de getallen in de cellen zelf", F), ("de plaats van de legende", J)],
          "De getallen pas je aan in de cellen, niet in de grafiek."),
    mk("Een lijngrafiek toont de verkoop van januari tot december. Wat staat er op de horizontale as?",
       ["de maanden", "het aantal stuks", "de legende", "de titel"], 0,
       "Bij een verloop in de tijd staat de tijd op de horizontale as."),
    koppel("Welk grafiekelement hoort bij welke vraag van de lezer?",
           [("Waarover gaat de grafiek?", "titel"), ("Welke kleur is welk jaar?", "legende"), ("Wat meet de as?", "astitel"), ("Hoeveel precies?", "gegevenslabel")], ["rasterlijn"],
           "Elk element beantwoordt een vraag van de lezer."),
    keuze("Je verplaatst een grafiek naar een eigen werkblad. De koppeling met de gegevens [[*blijft|verdwijnt]].",
          "De grafiek verwijst nog altijd naar hetzelfde bereik."),
    mk("Twee reeksen hebben heel verschillende getallen: omzet in duizenden en aantal klanten in tientallen. Wat is een goede oplossing?",
       ["twee aparte grafieken maken", "de omzet weglaten", "beide reeksen in één cirkeldiagram", "de as bij 1000 laten beginnen"], 0,
       "Anders zie je de kleine reeks bijna niet."),
]
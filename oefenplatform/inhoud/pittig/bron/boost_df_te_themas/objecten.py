"""Illustraties, schema's en tabellen — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_word_objecten, met een zelfgetekende bladzijde vol
objecten om op te klikken, aangevuld met de tabelvragen uit Samenleving en
economie Beyond (beyond_se_themas/word.py)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, GRIJS, BLAUW, ROOD, GEEL
from ..beyond_se_themas import word as _w

BL = Prent("bladzijde-objecten", "", "bladzijde van een folder met foto, tekstvak, schema, tabel, pictogram en een onderlijnd woord, letters A tot F")
BL.rect(150, 14, 700, 612, "#ffffff", DONKER, 4, 2)
BL.tekst(500, 60, "Fietsen Trappers: wie doet wat?", 26, vet=True)
# A: foto met tekst errond (vierkant)
BL.rect(190, 90, 200, 140, "#dfe9f2", GRIJS, 0, 2)
BL.pad("M 200 220 L 260 150 L 300 190 L 330 160 L 380 220 Z", "#9fb9cf", "none", 0)
BL.cirkel(350, 120, 14, GEEL, "none", 0)
for i in range(6):
    BL.lijn(410, 100 + i * 24, 810, 100 + i * 24, GRIJS, 6)
BL.letter(190, 90, "A")
# B: tekstvak
BL.rect(560, 250, 250, 80, "#fff8d6", DONKER, 6, 2)
BL.tekst(685, 282, "Nieuw: herstelling", 18); BL.tekst(685, 308, "binnen 24 uur!", 18)
BL.letter(820, 250, "B")
# C: schema (organogram)
BL.rect(270, 250, 120, 36, LICHTGROEN, DONKER, 6, 2); BL.tekst(330, 274, "zaakvoerder", 15)
BL.lijn(330, 286, 330, 304, DONKER, 2); BL.lijn(240, 304, 420, 304, DONKER, 2)
for c, t in ((240, "verkoop"), (420, "atelier")):
    BL.lijn(c, 304, c, 318, DONKER, 2); BL.rect(c - 55, 318, 110, 32, LICHTGROEN, DONKER, 6, 2); BL.tekst(c, 340, t, 15)
BL.letter(190, 268, "C")
# D: tabel met koprij
X0, Y0, CB, RH = 190, 390, 205, 36
for r in range(4):
    for k in range(3):
        BL.rect(X0 + k * CB, Y0 + r * RH, CB, RH, LICHTGROEN if r == 0 else "#ffffff", DONKER, 0, 1)
for k, t in enumerate(("dienst", "prijs", "duur")):
    BL.tekst(X0 + k * CB + CB / 2, Y0 + 24, t, 16, vet=True)
for r, rij in enumerate((("band plakken", "12 euro", "15 min"), ("remmen", "25 euro", "30 min"), ("grote beurt", "79 euro", "2 uur")), 1):
    for k, t in enumerate(rij):
        BL.tekst(X0 + k * CB + CB / 2, Y0 + r * RH + 24, t, 16)
BL.letter(170, 408, "D")
# E: pictogram telefoon
BL.cirkel(230, 580, 22, "#ffffff", DONKER, 2)
BL.pad("M 220 570 Q 224 566 228 572 L 226 578 Q 230 586 236 590 L 242 588 Q 248 592 244 596 Q 236 600 226 592 Q 216 582 220 570 Z", DONKER, "none", 0)
BL.tekst(270, 587, "011 12 34 56", 18, "start")
BL.letter(190, 556, "E")
# F: woord met rode kronkellijn
BL.tekst(560, 587, "Wij herstellen alle merken", 18, "start")
BL.tekst(560, 612, "en modelen.", 18, "start")
d = "M 590 616 " + " ".join(f"Q {593 + i * 6} {620 if i % 2 == 0 else 612} {596 + i * 6} 616" for i in range(12))
BL.pad(d, "none", ROOD, 2)
BL.letter(820, 600, "F")
U = "bladzijde-objecten.svg"
Z = {"A": Prent.rond(190, 90, 30), "B": Prent.rond(820, 250, 30), "C": Prent.rond(190, 268, 30), "D": Prent.rond(170, 408, 30), "E": Prent.rond(190, 556, 30), "F": Prent.rond(820, 600, 30)}

VRAGEN = [_w.VRAGEN[i] for i in (9, 14, 17, 25)] + [
    klik("Klik op de letter bij het kader met tekst dat je vrij over de bladzijde kan schuiven.", U, [Z["B"]],
         "Een tekstvak staat los van de gewone tekst."),
    klik("Klik op de letter bij het schema dat je met SmartArt kan maken.", U, [Z["C"]],
         "Een organogram: wie onder wie werkt. SmartArt tekent het schema zelf."),
    klik("Klik op de letter bij een melding van de spellingcontrole.", U, [Z["F"]],
         "De rode kronkellijn onder 'modelen': het moet 'modellen' zijn. Ze wordt niet afgedrukt."),
    klik("Klik op de letter bij een pictogram.", U, [Z["E"]],
         "Een eenvoudige tekening van een telefoon maakt sneller duidelijk dan een woord."),
    klik("Klik op de letter bij de afbeelding waar de tekst vierkant omheen loopt.", U, [Z["A"]],
         "Tekstterugloop vierkant: de regels stoppen netjes naast de foto."),
    casus("Bekijk de bladzijde van Fietsen Trappers.", [
        tabel("Klopt dit volgens de bladzijde?",
              [("In tabel D is de eerste rij een koprij.", J), ("De tabel telt drie kolommen.", J), ("De rode lijn onder het woord wordt mee afgedrukt.", F), ("Een lezer met een voorleesprogramma heeft iets aan alternatieve tekst bij foto A.", J)],
              "De kronkellijn staat enkel op je scherm. Alternatieve tekst beschrijft het beeld voor wie het niet ziet."),
        inv("Hoeveel cellen telt tabel D in totaal? Schrijf enkel het getal.", ["12", "twaalf"],
            "4 rijen × 3 kolommen = 12 cellen."),
        keuze("Wil je boven de tabel één titel over alle drie de kolommen, dan [[*voeg je drie cellen samen|splits je één cel|wis je de koprij]].",
              "Samenvoegen maakt van meerdere cellen één cel."),
    ]),
    tabel("Welke tekstterugloop past?",
          [("een watermerk dat achter de tekst ligt", "achter de tekst"), ("een foto met de tekst er netjes naast", "vierkant"), ("een foto op een eigen regel, met tekst erboven en eronder", "boven en onder")],
          "De tekstterugloop bepaalt hoe de tekst rond een afbeelding loopt.",
          kolommen=["vierkant", "boven en onder", "achter de tekst"]),
    mk("Je trekt een foto aan de zijkant breder. Wat gebeurt er?",
       ["De foto vervormt.", "De foto wordt scherper.", "De foto wordt bijgesneden.", "Er gebeurt niets met de foto."], 0,
       "Trek aan een hoekpunt, dan blijft de verhouding juist."),
    keuze("Het wegsnijden van de randen van een foto heet [[*bijsnijden|samenvoegen|vervormen]]; de foto zelf blijft heel.",
          "Je toont er minder van."),
    tabel("Spellingcontrole, grammaticacontrole of autocorrectie?",
          [("toont een verkeerd gespeld woord", "spellingcontrole"), ("toont een fout in de zinsbouw", "grammaticacontrole"), ("zet de eerste letter na een punt meteen als hoofdletter", "autocorrectie"), ("zet een typfout meteen recht zonder te vragen", "autocorrectie")],
          "De autocorrectie wijzigt meteen; je kan dat ongedaan maken met ctrl + z.",
          kolommen=["spellingcontrole", "grammaticacontrole", "autocorrectie"]),
    mk("Je typt 'hij word morgen achttien'. Waarom ziet de spellingcontrole dat niet?",
       ["'Word' is een bestaand woord.", "De spellingcontrole staat altijd uit.", "Werkwoorden worden niet gecontroleerd.", "Er staat geen punt na de zin."], 0,
       "Ze vergelijkt elk woord met een woordenlijst; daarom mag je ze niet blind vertrouwen."),
    keuze("Staat de taal van je document op Engels, dan [[*onderlijnt de controle bijna elk Nederlands woord|werkt de controle beter|verdwijnt de autocorrectie]].",
          "Zet de taal van de tekst juist."),
    tabel("Kan je dit aanpassen aan een ingevoegde vorm?",
          [("de vulkleur", J), ("de rand", J), ("een schaduw", J), ("de spellingcontrole", F)],
          "Een vorm geef je een eigen vulkleur, rand, schaduw en tekst."),
    keuze("Een foto die je wil gebruiken, haal je best uit een [[*vrije beeldbank|willekeurige zoekmachine|sociaal netwerk van een ander]].",
          "Niet elke foto op het internet mag je gebruiken."),
    sleep("Een vakje in een tabel heet een [[cel]]. Een horizontale reeks cellen is een [[rij]].",
          ["kolom", "record"], "Rijen lopen van links naar rechts, kolommen van boven naar onder."),
    tabel("Klopt dit over tabellen?",
          [("Een tabel moet altijd zichtbare randen hebben.", F), ("Met tab in de laatste cel maak je een nieuwe rij.", J), ("Een koprij kan je bovenaan elke bladzijde laten herhalen.", J)],
          "Je kan de randen wegnemen; de tabel houdt de uitlijning."),
    mk("Waarom zet een onderneming de prijzen in een factuur in een tabel?",
       ["De bedragen staan mooi onder elkaar.", "Een tabel berekent vanzelf de btw.", "Een tabel kan je achteraf niet wijzigen.", "Zonder tabel is een factuur ongeldig."], 0,
       "Zo vindt de klant snel wat hij zoekt en ziet het er verzorgd uit."),
    keuze("Wat je invult bij alternatieve tekst, is [[*een beschrijving van het beeld|de bestandsnaam van de foto|de prijs van de foto]].",
          "Een voorleesprogramma leest die voor."),
    open_("Waarom is het riskant om de autocorrectie blind te laten werken in een offerte met merknamen en afkortingen?",
          "De autocorrectie wijzigt meteen wat ze voor een fout houdt, ook een merknaam of een afkorting die juist was. Zo kan er een verkeerde naam in de offerte belanden. Lees het document daarom altijd na en maak een ongewenste wijziging ongedaan.",
          "Autocorrectie vraagt geen toestemming."),
    klik("Klik op de letter bij het object waarvan je de koprij kan laten herhalen als het over twee bladzijden loopt.", U, [Z["D"]],
         "Een tabel met een koprij: de rij met de titels."),
    keuze("De optie [[*achter de tekst|vierkant|boven en onder]] laat de tekst gewoon over de afbeelding lopen.",
          "Handig voor een watermerk."),
    tabel("Kan je dit als illustratie invoegen?",
          [("een foto", J), ("een pictogram", J), ("een vorm", J), ("een lijst met sneltoetsen", F)],
          "Een lijst met sneltoetsen is gewoon tekst."),
    inv("Welke opdracht maakt van drie cellen in de bovenste rij één brede cel? Schrijf één woord.", ["samenvoegen", "mergen", "cellen samenvoegen"],
        "Samenvoegen."),
    keuze("Een pictogram is [[*een eenvoudige tekening|altijd een foto|een soort tabel]] van een ding of een idee.",
          "Een oogje of een winkelkarretje leest sneller dan een woord."),
]

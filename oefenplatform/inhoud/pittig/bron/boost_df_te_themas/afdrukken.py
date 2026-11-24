"""Afdrukken, kopiëren en scannen — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_afdrukken, met een zelfgetekend multifunctioneel
toestel om de onderdelen aan te klikken, plus twee vragen uit Samenleving en
economie Beyond over afdrukken en pdf."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS
from ..beyond_se_themas import word as _w

MF = Prent("multifunctioneel-toestel", "Een multifunctioneel toestel", "printer, scanner en copier in één toestel met letters A tot F bij de onderdelen")
# kast
MF.rect(250, 200, 500, 330, "#eceae4", DONKER, 14)
# doorvoer bovenaan (schuin bakje met bladen)
MF.pad("M 300 200 L 330 120 L 640 120 L 610 200 Z", "#ffffff")
MF.lijn(335, 140, 620, 140, GRIJS, 2); MF.lijn(330, 155, 615, 155, GRIJS, 2)
# deksel en glasplaat (doorkijk)
MF.rect(270, 205, 460, 50, "#d9d6cc", DONKER, 6)
MF.rect(290, 262, 330, 26, "#cfe6f2", DONKER, 4)
# bedieningsscherm
MF.rect(640, 260, 90, 60, "#2b3a4a", DONKER, 6); MF.tekst(685, 296, "12:05", 16, kleur="#ffffff")
# uitvoerbak
MF.rect(300, 330, 330, 40, "#ffffff", DONKER, 4)
MF.rect(330, 336, 270, 8, "#f4f2ec", GRIJS, 1)
# klep met tonercassette
MF.rect(270, 390, 460, 50, "#e2dfd6", DONKER, 6)
MF.rect(560, 400, 140, 30, "#3a3a3a", DONKER, 6)
# papierlade
MF.rect(270, 455, 460, 60, "#f4f2ec", DONKER, 6)
MF.rect(460, 478, 80, 14, GRIJS, DONKER, 7)
LET = {"A": (475, 95), "B": (205, 275), "C": (790, 290), "D": (205, 350), "E": (790, 415), "F": (790, 485)}
for t, (x, y) in LET.items():
    MF.letter(x, y, t)
MF.lijn(225, 275, 290, 275, DONKER, 1); MF.lijn(225, 350, 300, 350, DONKER, 1)
MF.lijn(770, 290, 730, 290, DONKER, 1); MF.lijn(770, 415, 700, 415, DONKER, 1); MF.lijn(770, 485, 730, 485, DONKER, 1)
U = "multifunctioneel-toestel.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}

VRAGEN = [_w.VRAGEN[i] for i in (13, 24)] + [
    klik("Klik op de letter bij het deel dat een hele stapel bladen één per één meeneemt.", U, [Z["A"]],
         "De doorvoer bovenaan neemt de bladen één voor één mee om te kopiëren of te scannen."),
    klik("Klik op de letter bij het deel waar je één blad met de bedrukte zijde naar beneden legt.", U, [Z["B"]],
         "Op de glasplaat leg je een blad of een boek, tegen de hoek."),
    klik("Klik op de letter bij het deel waar je het aantal exemplaren intikt.", U, [Z["C"]],
         "Op het bedieningsscherm kies je de kopieerinstellingen."),
    klik("Klik op de letter waar de afgedrukte bladen uitkomen.", U, [Z["D"]],
         "De uitvoerbak vangt de afdrukken op."),
    klik("Het scherm meldt: toner bijna op. Klik op de letter bij het deel dat je vervangt.", U, [Z["E"]],
         "Achter de klep zit de tonercassette."),
    klik("Je kiest A3 maar er zit enkel A4 in het toestel. Klik op de letter waar je A3 moet bijleggen.", U, [Z["F"]],
         "Het papier zit in de papierlade, vaak één lade per formaat."),
    tabel("Welke melding of oplossing hoort bij het probleem?",
          [("Er komt een half blad gekreukt uit en het toestel stopt.", "papierstoring"), ("Je laptop vindt de printer niet in de lijst.", "geen verbinding"), ("De afdruk is bleek en vol strepen.", "toner of inkt bijna op"), ("Een blad zit vast in de doorvoer.", "papierstoring")],
          "Lees de melding en begin bij het eenvoudigste.",
          kolommen=["papierstoring", "geen verbinding", "toner of inkt bijna op"]),
    volgorde("Een blad zit vast. Zet de stappen in de juiste volgorde.",
             ["de melding op het scherm lezen", "de klep openen die het scherm aanwijst", "het blad voorzichtig in de richting van de doorvoer uittrekken", "de klep sluiten en de opdracht hervatten"],
             "Trek nooit tegen de richting in, dan scheurt het blad."),
    inv("Een verslag telt 36 bladzijden. Je drukt het dubbelzijdig af in 5 exemplaren. Hoeveel bladen papier heb je nodig? Schrijf enkel het getal.", ["90"],
        "36 bladzijden dubbelzijdig is 18 bladen, maal 5 is 90."),
    inv("Je kopieert 2 A4-bladzijden verkleind op één A4 (twee op één). Hoeveel bladen heb je nodig voor 24 bladzijden? Schrijf enkel het getal.", ["12"],
        "Twee bladzijden per blad: 24 gedeeld door 2 is 12."),
    mk("Je moet 400 folders in zwart-wit afdrukken. Welk toestel is per blad het goedkoopst?",
       ["een laserprinter", "een inkjetprinter", "een leespen", "een vlakbedscanner"], 0,
       "Toner is per blad goedkoper bij veel afdrukken."),
    tabel("Is dit een kopieerinstelling?",
          [("het aantal exemplaren", J), ("zwart-wit of kleur", J), ("vergroten of verkleinen", J), ("het lettertype van de tekst", F)],
          "Een copier maakt een beeld van het blad; de tekst zelf kan hij niet aanpassen."),
    keuze("Je startte per ongeluk een opdracht van 200 bladzijden. Je annuleert ze snel in [[*de afdrukwachtrij|de papierlade|het afdrukbereik]].",
          "In de wachtrij staan alle opdrachten die nog moeten afgedrukt worden."),
    tabel("Kies je dit in de printereigenschappen?",
          [("de papierlade", J), ("dubbelzijdig", J), ("de afdrukkwaliteit", J), ("de inhoud van bladzijde 3", F)],
          "De inhoud wijzig je in het document zelf."),
    keuze("Je wil enkel bladzijde 4 tot en met 7 afdrukken. Je stelt [[*het afdrukbereik|het aantal exemplaren|de lade]] in op 4-7.",
          "Zo druk je niet het hele document opnieuw af."),
    mk("Een factuur moet er bij de klant precies hetzelfde uitzien als bij jou. Wat stuur je?",
       ["een pdf", "het tekstbestand zelf", "een foto van je scherm", "de afdrukwachtrij"], 0,
       "In een pdf zit de opmaak vast, met de lettertypes erin."),
    sorteer("Komt er een blad uit het toestel?", ["ja", "nee"],
            [("afdrukken naar pdf", "nee"), ("een kopie in kleur", "ja"), ("een scan naar je e-mail", "nee"), ("een proefafdruk van een folder", "ja")],
            "Afdrukken naar pdf en scannen geven een bestand, geen blad."),
    tabel("Welke scanner past best?",
          [("één regel uit een boek overnemen", "leespen"), ("een volledige factuur van A4 inscannen", "vlakbedscanner"), ("een breed affiche in stukken over het blad slepen", "handscanner"), ("een pagina uit een dik boek op glas leggen", "vlakbedscanner")],
          "Een leespen voor een regel, een handscanner sleep je zelf, een vlakbedscanner heeft glas.",
          kolommen=["leespen", "handscanner", "vlakbedscanner"]),
    casus("Lotte scant een stapel aankoopfacturen in voor de boekhouding.", [
        keuze("Ze wil later op het bedrag kunnen zoeken. Daarvoor zet ze [[*tekenherkenning|een hogere resolutie|de kleur]] aan.",
              "Zonder OCR is de scan een afbeelding waarin je niet kan zoeken."),
        tabel("Klopt dit over het scannen?",
              [("Na OCR kijkt Lotte de herkende bedragen na.", J), ("Een scan zonder OCR is een foto van de tekst.", J), ("Een hoge resolutie maakt het bestand kleiner.", F)],
              "Meer puntjes geven meer detail maar een zwaarder bestand."),
        mk("De facturen worden snel na elkaar ingelezen. Welk deel van het toestel gebruikt ze?",
           ["de doorvoer bovenaan", "de papierlade onderaan", "de uitvoerbak in het midden", "het bedieningsscherm"], 0,
           "De doorvoer neemt de hele stapel één per één."),
    ]),
    tabel("Hoort dit bij scannen of bij afdrukken?",
          [("de resolutie kiezen", "scannen"), ("het aantal exemplaren", "afdrukken"), ("tekenherkenning", "scannen"), ("dubbelzijdig", "afdrukken")],
          "Scannen maakt een bestand, afdrukken een blad.",
          kolommen=["scannen", "afdrukken"]),
    keuze("Een inkjetprinter drukt met [[*vloeibare inkt|toner|poeder]], een laserprinter met [[*toner|vloeibare inkt]].",
          "Toner is een fijn poeder."),
    mk("Waarom druk je bij 300 uitnodigingen eerst één proefblad af?",
       ["om een fout te zien voor alles verloren is", "omdat de printer eerst moet opwarmen", "om de toner te sparen voor later", "omdat de wachtrij er anders niet aan begint"], 0,
       "Een fout in één blad kost minder dan in driehonderd."),
    sleep("Een toestel dat afdrukt, kopieert en scant heet een [[multifunctioneel toestel]]. Tekst herkennen in een scan heet [[tekenherkenning]].",
          ["laserprinter", "afdrukbereik"], "Twee begrippen uit dit hoofdstuk."),
    tabel("Klopt dit over de wachtrij en de lade?",
          [("Zonder papier blijft een opdracht in de wachtrij wachten.", J), ("Een opdracht in de wachtrij kan je nog annuleren.", J), ("Elk formaat papier mag in dezelfde lade gemengd worden.", F)],
          "Vaak is er één lade per formaat."),
    mk("Een printer doet niets na je opdracht. Wat kijk je eerst na?",
       ["of hij aan staat en er papier in zit", "of de netwerkkabel van de server goed zit", "of je een nieuwe printer moet bestellen", "of de toner van vorig jaar nog goed is"], 0,
       "Eerst het eenvoudigste, daarna pas het netwerk."),
    open_("Je collega wil een contract van tien bladzijden naar een klant sturen. Hij drukt het af, scant het in en mailt de scan. Geef hem een betere werkwijze en zeg waarom.",
          "Afdrukken naar pdf of opslaan als pdf: er komt geen papier aan te pas, de opmaak blijft juist en de klant kan in de tekst zoeken. Een scan is een afbeelding, zwaarder en minder scherp.",
          "Een pdf is lichter, scherper en doorzoekbaar."),
]

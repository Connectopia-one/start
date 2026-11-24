"""Presenteren met PowerPoint — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen schermafdruk
van het bewerkingsvenster, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Het bewerkingsvenster -----------------------------------------------------------------
PP = Prent("powerpoint-venster", "Het bewerkingsvenster van een presentatie (verkleind)", "links een smalle kolom met drie kleine dia's onder elkaar (A); rechts een grote dia met bovenaan een vette regel (B), daaronder links een kader met drie opsommingsregels (C), rechts een foto-kader met een dikke pijl ernaar (D), rechtsonder op de dia een klein rond knopje met een driehoekje (E); onder de grote dia een smalle strook met twee regels gewone tekst (F)")
# miniaturen
PP.rect(60, 60, 170, 520, "#f4f4f2", GRIJS, 6, 1)
for i in range(3):
    y = 80 + i * 130
    PP.rect(80, y, 130, 90, "#ffffff", DONKER if i == 1 else GRIJS, 3, 3 if i == 1 else 1)
    PP.lijn(92, y + 20, 170, y + 20, DONKER, 3)
    PP.lijn(92, y + 45, 150, y + 45, GRIJS, 2)
    PP.lijn(92, y + 60, 160, y + 60, GRIJS, 2)
    PP.tekst(70, y + 15, str(i + 1), 14, "start")
PP.letter(145, 500, "A")
# grote dia
PP.rect(260, 60, 680, 400, "#ffffff", GRIJS, 4, 2)
PP.tekst(600, 120, "Afval sorteren op school", 32, "middle", DONKER, True)
PP.letter(860, 110, "B")
for i, t in enumerate(["Restafval", "Papier en karton", "PMD"]):
    PP.cirkel(300, 190 + i * 50, 5, DONKER, DONKER, 1)
    PP.tekst(315, 197 + i * 50, t, 22, "start")
PP.rect(285, 160, 260, 160, "none", GRIJS, 0, 1)
PP.letter(520, 350, "C")
PP.rect(690, 160, 200, 150, "#e8efe1", GRIJS, 4, 1)
PP.pad("M720 285 L760 225 L790 260 L820 215 L870 285 Z", "#c9d8bc", "#9db58a", 1)
PP.pijl(600, 360, 680, 290, DONKER, 6)
PP.letter(600, 400, "D")
PP.cirkel(900, 420, 22, "#ecebe6", DONKER, 2)
PP.pad("M893 408 L912 420 L893 432 Z", DONKER, DONKER, 1)
PP.letter(840, 425, "E")
# notities
PP.rect(260, 480, 680, 100, "#fbfbf9", GRIJS, 4, 1)
PP.tekst(280, 515, "Eerst vragen wie thuis sorteert.", 18, "start", "#5c6356")
PP.tekst(280, 545, "Daarna de drie bakken tonen.", 18, "start", "#5c6356")
PP.letter(900, 530, "F")

ZONE = {"A": [Prent.zone(60, 60, 170, 520)], "B": [Prent.zone(300, 85, 600, 55)],
        "C": [Prent.zone(285, 160, 260, 160)], "D": [Prent.zone(590, 280, 100, 90)],
        "E": [Prent.rond(900, 420, 34)], "F": [Prent.zone(260, 480, 680, 100)]}

VRAGEN = [
    klik("Klik op het deel waar de spreker typt wat hij wil zeggen, zonder dat het publiek het ziet.", PP.bestand, ZONE["F"],
         "Dat is het notitievenster. In de presentatorweergave zie jij die notities, het publiek niet."),
    klik("Klik op het deel waar je dia's versleept om hun volgorde te veranderen.", PP.bestand, ZONE["A"],
         "In de kolom met miniaturen sleep je een dia naar een andere plaats."),
    klik("Klik op de knop die je zelf op de dia zette en die bij een klik naar de volgende dia gaat.", PP.bestand, ZONE["E"],
         "Dat is een actieknop: het driehoekje betekent verder gaan."),
    klik("Klik op de vorm die iets op de dia aanduidt.", PP.bestand, ZONE["D"],
         "Met een vorm, zoals een pijl, duid je het belangrijkste aan."),
    met_prent(PP.bestand, koppel("Koppel elke letter aan wat je daar ziet.", [
        ["A", "de miniaturen van de dia's"],
        ["C", "een tekstvak met een opsomming"],
        ["E", "een actieknop"],
        ["F", "de notities van de spreker"],
    ], ["een hand-out", "een diaovergang"], "Een hand-out en een overgang zie je niet als vak in het venster.")),
    met_prent(PP.bestand, keuze("Je wil dat de drie regels in C één voor één verschijnen. Daarvoor gebruik je een [[*animatie|diaovergang|hyperlink]].",
              "Een animatie werkt op iets dat op de dia staat; een overgang werkt tussen twee dia's.")),
    met_prent(PP.bestand, mk("Welke dia is in de linkerkolom geselecteerd?",
              ["dia 2", "dia 1", "dia 3", "geen enkele dia"], 0,
              "De tweede miniatuur heeft een dikke rand: die dia staat groot rechts.")),
    met_prent(PP.bestand, tabel("Kijk naar het venster. Klopt dit?", [
        ("Het publiek ziet de tekst in F tijdens de voorstelling.", F),
        ("De pijl in D is een vorm.", J),
        ("Op een notitiepagina komt de dia met de tekst uit F eronder.", J),
        ("De volgorde van de dia's verander je in vak B.", F),
    ], "F is voor de spreker. B is de titel van de dia.")),
    casus(
        "Lina presenteert morgen over afval sorteren. Ze wil haar eigen geheugensteuntjes zien, "
        "het publiek moet een blad met alle dia's krijgen om op mee te schrijven, en de presentatie "
        "moet op de laptop van de school meteen als voorstelling starten.",
        [
            mk("Wat gebruikt Lina om haar geheugensteuntjes te zien terwijl het publiek alleen de dia ziet?",
               ["de presentatorweergave",
                "de diasorteerder",
                "een overzicht als afdruk",
                "een diaovergang met geluid"], 0,
               "In de presentatorweergave zie je je notities op je eigen scherm."),
            keuze("Voor het publiek drukt ze [[*hand-outs|notitiepagina's|een overzicht]] af.",
                  "Een hand-out zet meerdere dia's op één blad, met plaats om mee te schrijven."),
            inv("In welke bestandsindeling bewaart ze, zodat de presentatie meteen als voorstelling start? Schrijf de afkorting.",
                ["ppsm", "PPSM", ".ppsm"], "De s staat voor show."),
        ],
    ),
    tabel("Diaovergang of animatie?", [
        ("een foto vliegt op de dia binnen", "animatie"),
        ("de hele dia vervaagt naar de volgende", "diaovergang"),
        ("een opsommingsregel verschijnt pas na een klik", "animatie"),
        ("de volgende dia schuift van rechts binnen", "diaovergang"),
    ], "Een overgang zit tussen twee dia's, een animatie op een onderdeel van de dia.",
       kolommen=["diaovergang", "animatie"]),
    tabel("Welke afdruk past?", [
        ("een blad per dia met je eigen notities eronder", "notitiepagina"),
        ("zes dia's op één blad voor de klas", "hand-out"),
        ("enkel de tekst van alle dia's, zonder beelden", "overzicht"),
    ], "Notitiepagina voor de spreker, hand-out voor het publiek, overzicht voor de tekst.",
       kolommen=["hand-out", "notitiepagina", "overzicht"]),
    sorteer("Werkt dit op de hele presentatie of op één dia of onderdeel?", ["Hele presentatie", "Eén dia of onderdeel"], [
        ["een thema kiezen", "Hele presentatie"],
        ["een animatie op een foto", "Eén dia of onderdeel"],
        ["de indeling van dia 4 aanpassen", "Eén dia of onderdeel"],
        ["als ppsm bewaren", "Hele presentatie"],
    ], "Een thema en een bestandsindeling gelden voor alles."),
    volgorde("Je maakt een dia die bijna hetzelfde is als dia 5. Zet de stappen in de juiste volgorde.", [
        "dia 5 selecteren in de miniaturen",
        "dia 5 dupliceren",
        "in de kopie de tekst aanpassen",
        "de kopie naar de juiste plaats slepen",
    ], "Dupliceren maakt een exacte kopie die je daarna aanpast."),
    mk("Je presentatie heeft twaalf dia's. Je verwijdert dia 7. Welk nummer krijgt de dia die eerst dia 9 was?",
       ["8", "9", "7", "10"], 0,
       "Alle dia's na de verwijderde schuiven één plaats op."),
    keuze("Een hyperlink op een dia kan naar een website of naar [[*een andere dia|een hand-out|de notities]] verwijzen.",
          "Zo kan je ook binnen je eigen presentatie springen."),
    tabel("Klopt dit over bestandsindelingen?", [
        ("Een pptx opent om verder te bewerken.", J),
        ("Een ppsm opent meteen als diavoorstelling.", J),
        ("Een ppsm kan je nooit meer bewerken.", F),
    ], "Je kan een ppsm in PowerPoint zelf nog openen en aanpassen."),
    inv("Hoe heet de weergave waarin alle dia's als miniaturen naast elkaar staan om ze te ordenen?",
        ["diasorteerder", "de diasorteerder", "diasorteerweergave"], "In de diasorteerder sleep je dia's naar een andere plaats."),
    mk("Een publiek achteraan in de zaal kan je dia's niet lezen. Wat pas je best aan?",
       ["minder tekst per dia, in grotere letters",
        "een donkerder thema met kleinere letters erop",
        "meer animaties zodat de tekst opvalt",
        "de hand-outs pas na afloop uitdelen"], 0,
       "Weinig tekst per dia, groot genoeg om te lezen."),
    met_prent(PP.bestand, mk("Welk vak op de grote dia is de titel?",
              ["B", "C", "D", "F"], 0,
              "B staat bovenaan in het titelvak, in grote vette letters.")),
    keuze("Je wil dat dia 4 een titel en twee vakken naast elkaar krijgt. Je verandert de [[*indeling|thema|overgang]] van die dia.",
          "De indeling is het vaste patroon van vakken op één dia."),
    klik("Klik op het tekstvak met de opsomming.", PP.bestand, ZONE["C"],
         "Het kader met de drie regels en bolletjes is een tekstvak."),
    met_prent(PP.bestand, inv("Lina wil met de knop in E niet naar de volgende maar naar de laatste dia springen. Wat past ze aan? Vul aan: de ... van de actieknop.",
              ["actie", "de actie", "koppeling", "hyperlink"], "Bij een actieknop kies je zelf wat er gebeurt bij een klik.")),
    tabel("Voor wie is deze afdruk bedoeld?", [
        ("hand-out", "publiek"),
        ("notitiepagina", "spreker"),
        ("overzicht met alleen tekst", "spreker"),
    ], "De hand-out is voor het publiek; notities en overzicht helpen jou voorbereiden.",
       kolommen=["publiek", "spreker"]),
    volgorde("Zet de stappen om een presentatie voor te bereiden in een logische volgorde.", [
        "een thema voor de hele presentatie kiezen",
        "de dia's met titels en tekst maken",
        "animaties en overgangen toevoegen",
        "de voorstelling vanaf het begin oefenen",
    ], "Eerst de opmaak en de inhoud, dan de effecten, dan oefenen."),
    sorteer("Zie je dit tijdens de voorstelling op het grote scherm?", ["Ja", "Nee"], [
        ["een animatie op een tekstvak", "Ja"],
        ["de notities van de spreker", "Nee"],
        ["de miniaturenkolom", "Nee"],
        ["een actieknop", "Ja"],
    ], "Notities en miniaturen zijn enkel voor de maker of spreker."),
    sleep("Op elke dia hetzelfde lettertype en dezelfde achtergrond krijg je met een [[thema]]. Het vaste patroon van vakken op één dia heet de [[indeling]].",
          ["animatie", "hand-out"], "Een thema geldt voor de hele presentatie, een indeling per dia."),
    koppel("Koppel elk probleem aan de oplossing.", [
        ["je wil tijdens het presenteren naar de laatste dia springen", "een actieknop of hyperlink"],
        ["je publiek wil meeschrijven", "hand-outs afdrukken"],
        ["je wil een dia met dezelfde opmaak", "de dia dupliceren"],
        ["je wil starten vanaf de dia waar je staat", "voorstelling vanaf huidige dia"],
    ], ["een overzicht afdrukken"], "Elk hulpmiddel lost iets anders op."),
    open_("Leg aan een klasgenoot uit wat het verschil is tussen een diaovergang en een animatie, met een voorbeeld van elk.",
          "Een diaovergang is het effect tussen twee dia's, bijvoorbeeld de dia die vervaagt naar de volgende. Een animatie werkt op iets op de dia zelf, bijvoorbeeld een opsommingsregel die pas na een klik verschijnt."),
]

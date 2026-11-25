# -*- coding: utf-8 -*-
"""Uitdaging Toegepaste economie 🚀 Boost dubbele finaliteit (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen, van de balans, het MAR en het redeneerschema
tot facturen, btw, eindejaarsverrichtingen, tekstverwerking, rekenblad,
grafieken, bestanden en databanken. Een rekenblad en zes verzonnen
verrichtingen om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, een casus en een open vraag. Geen nieuwe leerstof: alles
staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_te.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Toegepaste economie"
BESTAND = "boost-df-te-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/te-boost-df-uitdaging"
BLAD = "rekenblad-bestelling.svg"
VER = "zes-verrichtingen.svg"
# klikvakken: zie maak_prenten_boost_df_te.py
NAAMVAK = [4.0, 13.5, 12.0, 7.7]
FORMULEBALK = [22.0, 13.5, 74.0, 7.7]
F2 = [75.0, 35.8, 15.0, 8.4]
D5 = [55.0, 61.0, 15.0, 8.4]
D6 = [55.0, 69.4, 15.0, 8.4]
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Rekenblad
    klik("Bekijk het rekenblad. Klik op de cel waarin het btw-tarief staat.",
         BLAD, [F2],
         "Het btw-tarief staat in cel F2: 21%."),
    klik("Klik op de cel waarin de formule =SOM(D2:D4) staat.",
         BLAD, [D5],
         "De som van de totalen van de drie artikels staat in D5: 20 + 20 + 10 = 50."),
    klik("Klik op de plaats waar je ziet welke cel geselecteerd is.",
         BLAD, [NAAMVAK],
         "Het naamvak links van de formulebalk toont het adres van de geselecteerde cel: D2."),
    klik("Klik op de plaats waar je de formule van de geselecteerde cel leest.",
         BLAD, [FORMULEBALK],
         "In de formulebalk staat de formule: =B2*C2. In de cel zelf zie je alleen de uitkomst."),
    klik("Klik op de cel waarin een absolute verwijzing nodig is in de formule, omdat ze naar het btw-tarief verwijst.",
         BLAD, [D6],
         "In D6 bereken je de btw: =D5*$F$2. Het btw-tarief staat in één vaste cel, daarom zet je die vast."),
    met_prent(BLAD, keuze(
        "Als je de formule van D2 met de vulgreep naar D3 sleept, verwijst ze naar [[*B3 en C3|B2 en C2|B4 en C4]]. Dat komt doordat B2 en C2 [[*relatieve|absolute]] verwijzingen zijn.",
        "Een relatieve verwijzing schuift mee bij het kopiëren. Een absolute verwijzing met dollartekens blijft staan.")),
    met_prent(BLAD, inv(
        "Bereken het totaal inclusief btw in euro als de prijs van de mappen 10,00 wordt in plaats van 5,00. Een getal.",
        ["72,60", "72,6"],
        "D4 wordt 2 × 10 = 20. Totaal excl. btw = 20 + 20 + 20 = 60. Btw = 60 × 0,21 = 12,60. Totaal = 72,60.")),

    # Verrichtingen
    klik("Bekijk de zes verrichtingen. Klik op de verrichting waarbij 604 Aankopen handelsgoederen in debet komt.",
         VER, [Z[1]],
         "Bij een aankoop van handelsgoederen stijgt de kost 604 in debet. De schuld bij 440 Leveranciers stijgt in credit."),
    klik("Klik op de verrichting waarbij 400 Handelsdebiteuren in debet komt.",
         VER, [Z[3]],
         "Bij een verkoop op krediet krijg je een vordering op de klant: 400 Handelsdebiteuren stijgt in debet."),
    klik("Klik op de eindejaarsverrichting.",
         VER, [Z[5]],
         "De afschrijving van een vast actief boek je op het einde van het boekjaar."),
    klik("Klik op de verrichting waarbij de omzet niet verandert, maar 550 Kredietinstellingen in debet komt.",
         VER, [Z[2]],
         "Als een klant betaalt, stijgt de bank in debet en daalt de vordering 400 in credit. De verkoop was al geboekt."),
    met_prent(VER, keuze(
        "Bij verrichting 6 komt [[*570 Kassen|550 Kredietinstellingen]] in debet. Verrichting 4 boek je [[*omgekeerd aan|op dezelfde manier als]] de factuur.",
        "Het geld gaat naar de kas: 570 stijgt in debet, 550 daalt in credit. Een creditnota boek je omgekeerd aan de factuur.")),

    # Balans en resultaat
    sorteer(
        "Hoort deze post bij het actief of bij het passief van de balans?",
        ["actief", "passief"],
        [
            ["een machine", "actief"],
            ["het eigen vermogen", "passief"],
            ["het tegoed op de bank", "actief"],
            ["een schuld bij een leverancier", "passief"],
            ["een vordering op een klant", "actief"],
        ],
        "Het actief toont wat de onderneming bezit en tegoed heeft. Het passief toont waar het geld vandaan komt: eigen vermogen en schulden."),
    tabel(
        "Klopt dit over de balans en de resultatenrekening?",
        [
            ("De aankoop van een machine is een kost in de resultatenrekening.", F),
            ("De winst van het boekjaar staat bij het eigen vermogen.", J),
            ("Een opbrengst stijgt in credit.", J),
            ("Het bedrag in debet mag verschillen van het bedrag in credit.", F),
        ],
        "Een machine is een vast actief; ze wordt over meerdere jaren afgeschreven. Bij elke boeking zijn debet en credit even groot."),
    inv("Een machine van 20 000 euro wordt vijf jaar lang aan 4 000 euro per jaar afgeschreven. Wat is de boekwaarde na twee jaar, in euro? Een getal.",
        ["12000", "12 000", "12.000"],
        "Na twee jaar is er 2 × 4 000 = 8 000 afgeschreven. Boekwaarde = 20 000 − 8 000 = 12 000."),
    keuze(
        "Grond wordt [[*niet|wel]] afgeschreven. Een rekening met een debetsaldo heeft meer in [[*debet|credit]] dan in credit.",
        "Grond verliest geen waarde door gebruik. Een debetsaldo betekent dat de debetkant groter is."),

    # MAR en redeneerschema
    koppel(
        "Koppel het rekeningnummer aan de naam.",
        [
            ["604", "Aankopen handelsgoederen"],
            ["700", "Verkopen handelsgoederen"],
            ["440", "Leveranciers"],
            ["550", "Kredietinstellingen"],
        ],
        ["Personeelskosten"],
        "Klasse 6 zijn kosten, klasse 7 opbrengsten, klasse 4 vorderingen en schulden op korte termijn, klasse 5 geldmiddelen."),
    tabel(
        "Een aankoopfactuur: handelsgoederen 1 000 euro plus 210 euro btw, op krediet. Klopt deze boeking?",
        [
            ("604 Aankopen handelsgoederen in debet: 1 000", J),
            ("De aftrekbare btw in debet: 210", J),
            ("440 Leveranciers in credit: 1 210", J),
            ("700 Verkopen handelsgoederen in credit: 1 000", F),
        ],
        "Bij een aankoop staan de kost en de aftrekbare btw in debet, de schuld bij de leverancier in credit. Rekening 700 hoort bij een verkoop."),

    # Aankopen, verkopen en btw
    inv("Een factuur van 800 euro krijgt 10 procent handelskorting. Daarna komt er 21 procent btw bij. Hoeveel btw is dat, in euro? Een getal.",
        ["151,20", "151,2"],
        "800 − 80 = 720. De btw wordt berekend op het bedrag na korting: 720 × 0,21 = 151,20."),
    volgorde(
        "Zet de documenten van een aankoop in de gewone volgorde.",
        ["offerte", "bestelbon", "leverbon", "aankoopfactuur"],
        "Je vraagt een prijs (offerte), bestelt, ontvangt de goederen met een leverbon en krijgt daarna de factuur."),
    inv("Een bakker betaalt 6 euro btw op bloem en rekent 18 euro btw aan op brood. Hoeveel euro btw stort hij door aan de staat? Een getal.",
        ["12"],
        "Verschuldigde btw min aftrekbare btw: 18 − 6 = 12 euro."),
    tabel(
        "Klopt dit over btw?",
        [
            ("Btw is een belasting op de winst van een onderneming.", F),
            ("Het standaardtarief in België is 21 procent.", J),
            ("De handelskorting wordt na de btw afgetrokken.", F),
        ],
        "Btw is een belasting op het verbruik, geïnd door de onderneming voor de staat. De korting gaat eraf vóór de btw berekend wordt."),
    keuze(
        "Een uitgaande creditnota stuurt de [[*verkoper|klant]]. Op een creditnota staat [[*ook|geen]] btw.",
        "De verkoper corrigeert met een creditnota een factuur. De btw wordt mee verminderd."),

    mk("Een klant betaalt zijn factuur van 605 euro via de bank. Wat gebeurt er met de omzet?",
       ["Niets, de verkoop was al geboekt bij de factuur",
        "De omzet stijgt opnieuw met 605 euro bij de betaling",
        "De omzet daalt met 605 euro, want de vordering verdwijnt",
        "De omzet stijgt met de btw, want die is nu betaald"],
       0,
       "De opbrengst boek je bij de factuur. Bij de betaling stijgt de bank en daalt de vordering op de klant."),
    keuze(
        "De jaarrekening bestaat onder meer uit de balans en de [[*resultatenrekening|proefbalans]]. Als de kosten groter zijn dan de opbrengsten, maakt de onderneming [[*verlies|winst]].",
        "De jaarrekening toont de toestand (balans) en het resultaat van het boekjaar. Kosten groter dan opbrengsten geeft verlies."),
    tabel(
        "Klopt dit over afdrukken en scannen?",
        [
            ("Dubbelzijdig afdrukken halveert het aantal bladen.", J),
            ("Afdrukken naar pdf gebruikt inkt.", F),
            ("In de afdrukwachtrij zie je welke opdrachten nog wachten.", J),
        ],
        "Afdrukken naar pdf maakt een bestand, er komt geen papier of inkt aan te pas."),

    # Tekstverwerking en documenten
    koppel(
        "Koppel de sneltoets aan wat hij doet.",
        [
            ["ctrl + c", "kopiëren"],
            ["ctrl + v", "plakken"],
            ["ctrl + x", "knippen"],
            ["ctrl + a", "alles selecteren"],
        ],
        ["afdrukken op beide zijden"],
        "Sneltoetsen laten je sneller werken zonder de muis."),
    tabel(
        "Klopt dit over tekstverwerking?",
        [
            ("Een kop- en voettekst herhaalt zich op elke bladzijde van de sectie.", J),
            ("Een sjabloon en een stijl zijn hetzelfde.", F),
            ("Een tab is iets anders dan een reeks spaties.", J),
        ],
        "Een stijl geeft opmaak aan tekst. Een sjabloon is een volledig basisdocument."),
    mk("Welk schema toont de structuur van een onderneming, met wie onder wie werkt?",
       ["Een organogram", "Een cirkeldiagram", "Een storyboard", "Een kolomgrafiek"],
       0,
       "Een organogram toont de afdelingen en de lijnen van wie verantwoordelijk is voor wie."),

    # Rekenblad en functies
    koppel(
        "Koppel de functie aan wat ze doet.",
        [
            ["SOM", "telt de getallen op"],
            ["GEMIDDELDE", "berekent het gemiddelde"],
            ["MIN", "geeft het kleinste getal"],
            ["ALS", "kiest een uitkomst volgens een voorwaarde"],
        ],
        ["sorteert de kolom"],
        "Functies schrijf je met de argumenten tussen haakjes, bijvoorbeeld =SOM(B2:B10)."),
    keuze(
        "Een cel vol hekjes betekent dat de kolom te [[*smal|breed]] is. Een formule begint altijd met een [[*isgelijkteken|dollarteken]].",
        "Hekjes verschijnen als het getal niet in de cel past. Elke formule start met =."),

    # Grafieken
    mk("Je wil tonen hoe de omzet van een winkel elke maand evolueerde. Welke grafiek kies je?",
       ["Een lijngrafiek", "Een cirkeldiagram", "Een organogram", "Een tabel met randen"],
       0,
       "Een lijngrafiek toont een evolutie in de tijd. Een cirkeldiagram toont de verdeling van een geheel."),
    tabel(
        "Klopt dit over grafieken?",
        [
            ("Een grafiek zonder titel laat de lezer gissen.", J),
            ("Een cirkeldiagram past bij twintig categorieën.", F),
            ("Een grafiek volgt de cijfers in het blad.", J),
        ],
        "Met te veel categorieën wordt een cirkeldiagram onleesbaar. Verander je de cijfers in het blad, dan past de grafiek zich aan."),

    # Afdrukken, bestanden, databank
    sorteer(
        "Bij welk soort bestand hoort deze extensie?",
        ["tekstdocument", "rekenblad", "pdf"],
        [
            [".docx", "tekstdocument"],
            [".xlsx", "rekenblad"],
            [".pdf", "pdf"],
        ],
        "De extensie zegt welk soort bestand het is."),
    keuze(
        "Een scan zonder [[*tekenherkenning|kleur]] is een afbeelding waarin je niet kan zoeken. Een kopie van je bestanden op een andere plaats heet een [[*back-up|sjabloon]].",
        "Met tekenherkenning (OCR) wordt de tekst doorzoekbaar. Een back-up beschermt tegen verlies."),
    tabel(
        "Klopt dit over een databank?",
        [
            ("Twee records mogen dezelfde primaire sleutel hebben.", F),
            ("Een veld bevat één soort gegeven, zoals de postcode.", J),
            ("Met een query zoek je gegevens op die aan voorwaarden voldoen.", J),
        ],
        "De primaire sleutel maakt elk record uniek. Een query vraagt gegevens op."),
    sleep(
        "Bij een presentatie volg je het [[KISS]]-principe: houd het kort en eenvoudig. Voor je dia's maakt, teken je een [[storyboard]].",
        ["organogram", "MAR"],
        "KISS betekent: keep it short and simple. Een storyboard plant de volgorde van je dia's."),

    casus(
        "Handelszaak Pluim verkoopt op 3 maart op krediet 50 dozen pennen aan 8 euro per doos aan klant Schoolshop. Er is 10 procent handelskorting en 21 procent btw.",
        [
            inv("Wat is het bedrag van de factuur inclusief btw, in euro? Een getal.",
                ["435,60", "435,6"],
                "50 × 8 = 400. Korting 40, dus 360. Btw = 360 × 0,21 = 75,60. Totaal = 435,60."),
            tabel(
                "Hoe boekt Pluim deze verkoopfactuur?",
                [
                    ("400 Handelsdebiteuren", "debet"),
                    ("700 Verkopen handelsgoederen", "credit"),
                    ("de te betalen btw", "credit"),
                ],
                "De klant moet het totaal betalen: 400 in debet. De verkoop (360) en de te betalen btw (75,60) staan in credit.",
                kolommen=["debet", "credit"]),
        ]),

    open_("Pluim wil de verkopen van elke maand opvolgen in een rekenblad. Beschrijf hoe je dat blad opbouwt: welke kolommen, welke formules en welke grafiek je kiest. Leg kort uit waarom.",
          "Kolom A: de maand, kolom B: de omzet zonder btw, kolom C: de btw met =B2*$F$1 (het btw-tarief in F1), kolom D: het totaal met =B2+C2. Onderaan zet ik =SOM(B2:B13) en =GEMIDDELDE(B2:B13). Ik kies een lijngrafiek van kolom B, met een titel en asbenamingen, want zo zie je de evolutie over het jaar.",
          "Een goed antwoord noemt duidelijke kolommen, gebruikt passende formules (SOM, GEMIDDELDE, een absolute verwijzing naar het btw-tarief) en kiest een lijngrafiek voor een evolutie."),
]

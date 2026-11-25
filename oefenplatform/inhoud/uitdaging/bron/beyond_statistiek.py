# -*- coding: utf-8 -*-
"""Uitdaging Statistiek 🌍 Beyond doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Twee boxplots en een binomiale verdeling om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen en
een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Statistiek Beyond doorstroom. Alle cijfers zijn verzonnen.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_statistiek.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Statistiek"
BESTAND = "beyond-statistiek-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/statistiek-beyond-uitdaging"
BOX = "boxplots-klassen.svg"
BIN = "binomiaal-worpen.svg"

# klikvakken uit maak_prenten_beyond_statistiek.py
MED_A = [56.3, 25.9, 3.2, 19.6]
BOX_A = [45.8, 25.9, 24.2, 19.6]
BOX_B = [53.6, 54.5, 12.5, 19.6]
MAX_A = [87.3, 30.0, 3.6, 11.4]
STAAF2 = [42.1, 25.5, 10.9, 59.5]
STAAF5 = [83.2, 75.0, 10.9, 10.0]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Boxplots (prent)
    klik("Bekijk de boxplots. Klik op de mediaan van klas A.",
         BOX, [MED_A],
         "De mediaan is de dikke streep in de doos. Bij klas A ligt die op 11 punten."),
    klik("Klik op de doos van de klas waarvan de middelste helft van de punten het dichtst bij elkaar ligt.",
         BOX, [BOX_B],
         "De doos toont de middelste 50 %. Bij klas B loopt ze van 10 tot 13: een interkwartielafstand van 3. Bij klas A is dat 14 − 8 = 6."),
    klik("Klik op de hoogste score die in klas A behaald werd.",
         BOX, [MAX_A],
         "Het einde van de rechtse snorhaar is het maximum: 19 op 20."),
    met_prent(BOX, tabel(
        "Lees af op de boxplots.",
        [
            ("Interkwartielafstand van klas A", "6"),
            ("Variatiebreedte van klas A", "15"),
            ("Variatiebreedte van klas B", "11"),
        ],
        "IKA = Q3 − Q1 = 14 − 8 = 6. Variatiebreedte = max − min: 19 − 4 = 15 voor A en 17 − 6 = 11 voor B.",
        kolommen=["6", "11", "15"])),
    met_prent(BOX, tabel(
        "Klopt dit volgens de boxplots?",
        [
            ("Minstens de helft van klas B haalde 12 of meer.", J),
            ("In klas A haalde ongeveer een kwart 14 of meer.", J),
            ("Het gemiddelde van klas A is zeker 11.", F),
            ("Klas A heeft een kleinere spreiding dan klas B.", F),
        ],
        "De mediaan en de kwartielen verdelen de groep in vier stukken. Een boxplot toont het gemiddelde niet, en klas A heeft de grotere spreiding.")),

    # Binomiale verdeling (prent)
    klik("X is het aantal treffers bij 5 worpen met kans 0,4 per worp. Klik op de staaf van de meest waarschijnlijke waarde.",
         BIN, [STAAF2],
         "De hoogste staaf hoort bij x = 2, met kans 0,3456."),
    klik("Klik op de staaf die hoort bij P(X = 5): vijf keer raak.",
         BIN, [STAAF5],
         "P(X = 5) = 0,4⁵ ≈ 0,01. Die staaf is bijna onzichtbaar klein."),
    met_prent(BIN, inv(
        "Bereken P(X = 2) voor X ~ B(5; 0,4). Rond af op vier decimalen.",
        ["0,3456", "0.3456"],
        "P(X = 2) = C(5,2) · 0,4² · 0,6³ = 10 · 0,16 · 0,216 = 0,3456.")),
    met_prent(BIN, tabel(
        "Bereken voor X ~ B(5; 0,4).",
        [
            ("Verwachtingswaarde E(X)", "2"),
            ("Variantie Var(X)", "1,2"),
            ("Aantal mogelijke waarden van X", "6"),
        ],
        "E(X) = n · p = 5 · 0,4 = 2. Var(X) = n · p · (1 − p) = 5 · 0,4 · 0,6 = 1,2. X kan 0, 1, 2, 3, 4 of 5 zijn.",
        kolommen=["1,2", "2", "6"])),
    met_prent(BIN, inv(
        "Wat is de kans op minstens één treffer, P(X ≥ 1)? Rond af op vier decimalen.",
        ["0,9222", "0.9222"],
        "Gebruik het complement: P(X ≥ 1) = 1 − P(X = 0) = 1 − 0,6⁵ = 1 − 0,07776 ≈ 0,9222.")),

    # Telregels en combinaties
    inv("Een fietsslot heeft een code van 4 cijfers (0 tot 9). Hoeveel codes zijn er als geen enkel cijfer twee keer mag voorkomen?",
        ["5040"],
        "Productregel zonder herhaling: 10 · 9 · 8 · 7 = 5040."),
    tabel(
        "Herhaling of niet, volgorde of niet: hoeveel mogelijkheden?",
        [
            ("3 leerlingen uit 8 kiezen voor een werkgroep", "56"),
            ("Een voorzitter, secretaris en penningmeester kiezen uit 8", "336"),
            ("Een code van 3 tekens uit 8 letters, herhaling mag", "512"),
        ],
        "Zonder volgorde: C(8,3) = 56. Met volgorde, zonder herhaling: 8 · 7 · 6 = 336. Met herhaling: 8³ = 512.",
        kolommen=["56", "336", "512"]),
    keuze(
        "Bij een combinatie speelt de volgorde [[*geen rol|wel een rol]]. Daarom is C(n, k) [[*kleiner dan of gelijk aan|groter dan]] het aantal variaties van k uit n.",
        "Bij een combinatie tel je elke groep één keer, in welke volgorde ook. Daardoor zijn er nooit meer combinaties dan variaties."),
    mk("Een klas van 20 leerlingen telt 12 meisjes. Je kiest willekeurig één leerling. Wat is de kans dat het géén meisje is?",
       ["0,4", "0,6", "0,8", "0,12"],
       0,
       "Complementregel: 1 − 12/20 = 1 − 0,6 = 0,4."),
    inv("Hoeveel is 7! / 5! ?",
        ["42"],
        "7! / 5! = 7 · 6 = 42. De factoren 5 · 4 · 3 · 2 · 1 vallen weg."),

    # Normale verdeling
    inv("De lengte van volwassen mannen is normaal verdeeld met μ = 178 cm en σ = 8 cm. Wat is de z-score van 190 cm?",
        ["1,5", "1.5"],
        "z = (190 − 178) / 8 = 12 / 8 = 1,5."),
    tabel(
        "Gebruik de 68-95-99,7-regel bij μ = 178 cm en σ = 8 cm. Hoeveel procent ligt ongeveer in dit interval?",
        [
            ("Tussen 170 en 186 cm", "68 %"),
            ("Tussen 162 en 194 cm", "95 %"),
            ("Tussen 154 en 202 cm", "99,7 %"),
        ],
        "Eén, twee en drie standaardafwijkingen rond het gemiddelde bevatten ongeveer 68 %, 95 % en 99,7 %.",
        kolommen=["68 %", "95 %", "99,7 %"]),
    mk("Ongeveer hoeveel procent van de mannen is langer dan 186 cm (μ = 178, σ = 8)?",
       ["16 %", "34 %", "32 %", "2,5 %"],
       0,
       "Tussen 170 en 186 ligt 68 %. Buiten dat interval ligt 32 %, de helft daarvan rechts: 16 %."),

    # Steekproeven
    keuze(
        "Als je de steekproefgrootte vier keer zo groot maakt, wordt de standaardfout van het steekproefgemiddelde [[*twee keer zo klein|vier keer zo klein|twee keer zo groot]].",
        "De standaardfout is σ/√n. Vier keer n geeft √4 = 2 keer kleiner."),
    inv("Een populatie heeft σ = 12. Je neemt steekproeven van n = 36. Hoe groot is de standaardfout van het gemiddelde?",
        ["2"],
        "σ / √n = 12 / 6 = 2."),
    sorteer(
        "Is dit een aselecte steekproef of niet?",
        ["Aselect", "Niet aselect"],
        [
            ["Elke tiende naam uit de leerlingenlijst, met een toevallig startpunt", "Aselect"],
            ["Alleen de vrienden van de onderzoeker bevragen", "Niet aselect"],
            ["Namen trekken uit een bak met alle namen", "Aselect"],
            ["Een online poll waar wie wil op klikt", "Niet aselect"],
        ],
        "Bij een aselecte steekproef heeft elk lid van de populatie een gekende kans om gekozen te worden. Vrijwillige deelname of bekenden kiezen geeft vertekening."),

    # Hypothesetoetsen
    keuze(
        "Een fabrikant beweert dat een batterij gemiddeld 20 uur werkt. Een consumentenorganisatie denkt dat het minder is. Dan is H0: μ [[*= 20|< 20|> 20]] en H1: μ [[*< 20|> 20|≠ 20]].",
        "H0 is de bewering die je wil toetsen (gelijkheid). H1 drukt het vermoeden uit: minder, dus een linkszijdige toets."),
    tabel(
        "Wat besluit je bij een significantieniveau α = 0,05?",
        [
            ("p-waarde = 0,03", "H0 verwerpen"),
            ("p-waarde = 0,12", "H0 niet verwerpen"),
            ("p-waarde = 0,001", "H0 verwerpen"),
            ("p-waarde = 0,40", "H0 niet verwerpen"),
        ],
        "Is de p-waarde kleiner dan α, dan is het resultaat significant en verwerp je H0. Anders heb je onvoldoende bewijs.",
        kolommen=["H0 verwerpen", "H0 niet verwerpen"]),
    koppel(
        "Koppel de fout aan de beschrijving.",
        [
            ["fout van de eerste soort", "H0 verwerpen terwijl ze waar is"],
            ["fout van de tweede soort", "H0 niet verwerpen terwijl ze vals is"],
        ],
        ["H1 aannemen terwijl ze waar is", "de steekproef te klein kiezen"],
        "De kans op een fout van de eerste soort is α. Een fout van de tweede soort betekent dat je een echt effect mist."),
    mk("Wat betekent een p-waarde van 0,02?",
       ["Als H0 klopt, is zo'n resultaat of extremer maar 2 % waarschijnlijk.", "De kans dat H0 waar is, bedraagt precies 2 % in dit hele onderzoek.", "De kans dat H1 waar is, bedraagt precies 98 % in dit hele onderzoek.", "Er is 2 % kans dat de steekproef op een verkeerde manier getrokken werd."],
       0,
       "De p-waarde is de kans op dit resultaat of iets extremer, als H0 waar zou zijn. Ze zegt niet hoe waarschijnlijk H0 zelf is."),

    # Betrouwbaarheidsinterval
    mk("In een steekproef van 400 jongeren sport 60 %. Wat is ongeveer het 95 %-betrouwbaarheidsinterval voor het echte percentage?",
       ["Van 55,2 % tot 64,8 %", "Van 59,0 % tot 61,0 %", "Van 50,0 % tot 70,0 %", "Van 57,55 % tot 62,45 %"],
       0,
       "Foutenmarge = 1,96 · √(0,6 · 0,4 / 400) = 1,96 · 0,0245 ≈ 0,048. Het interval loopt van 55,2 % tot 64,8 %."),
    keuze(
        "Een 99 %-betrouwbaarheidsinterval is [[*breder|smaller]] dan een 95 %-interval met dezelfde gegevens. Een grotere steekproef maakt de foutenmarge [[*kleiner|groter]].",
        "Meer zekerheid vraagt een breder interval. Meer gegevens maken de schatting nauwkeuriger."),

    # Correlatie
    tabel(
        "Welke beschrijving past bij de correlatiecoëfficiënt r?",
        [
            ("r = 0,92", "Sterk positief verband"),
            ("r = −0,85", "Sterk negatief verband"),
            ("r = 0,05", "Nauwelijks lineair verband"),
        ],
        "Hoe dichter r bij 1 of −1 ligt, hoe sterker het lineaire verband. Het teken geeft de richting.",
        kolommen=["Sterk positief verband", "Sterk negatief verband", "Nauwelijks lineair verband"]),
    mk("In zomers worden meer ijsjes verkocht en zijn er meer verdrinkingen. De correlatie is sterk. Wat besluit je?",
       ["Er is een verband, maar ijsjes veroorzaken geen verdrinkingen.", "IJsjes eten vergroot echt de kans dat je verdrinkt in zee.", "Verdrinkingen zorgen ervoor dat er meer ijs verkocht wordt.", "De correlatie moet een rekenfout zijn, want er is geen oorzaak."],
       0,
       "Correlatie is geen causaliteit. Een derde factor, het warme weer, verklaart allebei."),

    # Beschrijvende statistiek
    tabel(
        "Bereken voor de dataset 2, 4, 4, 5, 10.",
        [
            ("Gemiddelde", "5"),
            ("Mediaan", "4"),
            ("Variatiebreedte", "8"),
        ],
        "Gemiddelde = 25 / 5 = 5. De middelste waarde is 4. Variatiebreedte = 10 − 2 = 8.",
        kolommen=["4", "5", "8"]),
    keuze(
        "In de dataset 2, 4, 4, 5, 10 is de modus [[*4|5|10]]. Als je 10 vervangt door 100, verandert [[*het gemiddelde|de mediaan|de modus]] het sterkst.",
        "De modus is de waarde die het vaakst voorkomt. Het gemiddelde is gevoelig voor uitschieters; de mediaan en de modus niet."),
    sorteer(
        "Welke grafiek kies je best?",
        ["Staafdiagram", "Histogram", "Spreidingsdiagram"],
        [
            ["Lievelingssport van de leerlingen", "Staafdiagram"],
            ["Lengtes van 200 leerlingen in klassen van 5 cm", "Histogram"],
            ["Verband tussen studietijd en punten", "Spreidingsdiagram"],
            ["Aantal broers en zussen per leerling", "Staafdiagram"],
        ],
        "Een staafdiagram voor categorieën of weinig discrete waarden, een histogram voor gegroepeerde continue gegevens, een spreidingsdiagram voor een verband tussen twee variabelen."),
    inv("In een frequentietabel komt de waarde 7 twaalf keer voor op 48 waarnemingen. Wat is de relatieve frequentie in procent? Enkel het getal.",
        ["25"],
        "12 / 48 = 0,25 = 25 %."),
    mk("Welke formule in een rekenblad geeft de mediaan van de cellen A1 tot A20?",
       ["=MEDIAAN(A1:A20)", "=GEMIDDELDE(A1:A20)", "=MODUS(A1:A20)", "=KWARTIEL(A1:A20;3)"],
       0,
       "MEDIAAN geeft de middelste waarde. GEMIDDELDE, MODUS en KWARTIEL geven andere maten."),

    # Onderzoek
    volgorde(
        "In welke volgorde verloopt een statistisch onderzoek bij jongeren?",
        ["Onderzoeksvraag formuleren", "Steekproef trekken", "Gegevens verzamelen", "Gegevens verwerken en voorstellen", "Besluit trekken en kritisch bekijken"],
        "Eerst weet je wat je wil weten, dan kies je wie je bevraagt, verzamel en verwerk je de gegevens, en pas daarna besluit je."),
    keuze(
        "Leeftijd in jaren is een [[*kwantitatieve|kwalitatieve]] variabele. Haarkleur is een [[*kwalitatieve|kwantitatieve]] variabele.",
        "Kwantitatieve variabelen zijn getallen waarmee je kan rekenen. Kwalitatieve variabelen zijn categorieën."),
    mk("Van een normaal verdeelde toets is μ = 60 en σ = 10. Wie zit bij de beste 2,5 %?",
       ["Iedereen met meer dan 80 punten", "Iedereen met meer dan 70 punten", "Iedereen met meer dan 90 punten", "Iedereen met meer dan 62,5 punten"],
       0,
       "95 % ligt tussen μ − 2σ en μ + 2σ, dus tussen 40 en 80. Boven 80 ligt de helft van de overige 5 %: 2,5 %."),

    inv("Een dobbelsteen wordt 3 keer gegooid. Hoeveel uitkomsten (geordende rijtjes) zijn er in totaal?",
        ["216"],
        "Productregel met herhaling: 6 · 6 · 6 = 216."),
    tabel(
        "Klopt dit over de binomiale verdeling?",
        [
            ("De pogingen moeten onafhankelijk van elkaar zijn.", J),
            ("De kans op succes blijft bij elke poging gelijk.", J),
            ("Er mogen bij elke poging drie uitkomsten zijn.", F),
            ("Het aantal pogingen ligt niet vast.", F),
        ],
        "Een binomiaal experiment heeft een vast aantal onafhankelijke pogingen met telkens twee uitkomsten (succes of niet) en een vaste succeskans."),

    # Schrijfopdracht
    open_("Een school beweert dat haar leerlingen gemiddeld 7 uur per nacht slapen. Jij vermoedt dat het minder is. Beschrijf in 4 à 6 zinnen hoe je dat met een hypothesetoets onderzoekt: hypothesen, steekproef, significantieniveau en besluit.",
          "H0: μ = 7 uur en H1: μ < 7 uur, een linkszijdige toets. Ik trek een aselecte steekproef van bijvoorbeeld 50 leerlingen en vraag hoeveel ze slapen. Ik kies α = 0,05. Met de rekenapp bereken ik de p-waarde bij het steekproefgemiddelde. Is p kleiner dan 0,05, dan verwerp ik H0 en besluit ik dat de leerlingen minder dan 7 uur slapen. Anders heb ik onvoldoende bewijs.",
          "Een goed antwoord noemt H0 en een linkszijdige H1, een aselecte steekproef, een gekozen α, en vergelijkt de p-waarde met α om H0 al dan niet te verwerpen."),
]

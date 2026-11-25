# -*- coding: utf-8 -*-
"""Uitdaging Economie 🚀 Boost doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen. Een marktgrafiek en zes balansposten om op te klikken, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Economie Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_economie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Economie"
BESTAND = "boost-economie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/economie-boost-uitdaging"
MARKT = "markt-aardbeien.svg"
BAL = "balansposten.svg"

# klikvakken uit maak_prenten_boost_economie.py
PT = {1: [47.5, 48.4, 7.0, 11.3], 2: [28.0, 35.2, 7.0, 11.3], 3: [67.0, 35.2, 7.0, 11.3],
      4: [67.0, 61.6, 7.0, 11.3], 5: [28.0, 61.6, 7.0, 11.3]}
POST = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
        4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Markt (prent)
    klik("Bekijk de markt voor verse aardbeien. Klik op het marktevenwicht.",
         MARKT, [PT[1]],
         "In het snijpunt van vraag en aanbod is de gevraagde hoeveelheid gelijk aan de aangeboden hoeveelheid: 50 kg aan 5 euro per kg."),
    klik("De prijs staat op 7 euro per kg. Klik op het punt dat toont hoeveel de kopers dan willen kopen.",
         MARKT, [PT[2]],
         "Bij 7 euro lees je de gevraagde hoeveelheid af op de vraagcurve: 25 kg. De verkopers bieden er dan 75 kg aan."),
    klik("De overheid legt een maximumprijs op van 3 euro per kg. Klik op het punt dat toont hoeveel de verkopers dan nog aanbieden.",
         MARKT, [PT[5]],
         "Bij 3 euro lees je de aangeboden hoeveelheid af op de aanbodcurve: 25 kg. De kopers vragen 75 kg: er ontstaat een tekort."),
    met_prent(MARKT, inv(
        "Hoe groot is het overschot in kg als de prijs op 7 euro per kg staat? Enkel het getal.",
        ["50"],
        "Aanbod 75 kg − vraag 25 kg = 50 kg overschot. Boven de evenwichtsprijs ontstaat er altijd een overschot.")),
    met_prent(MARKT, keuze(
        "Het inkomen van de gezinnen stijgt en aardbeien zijn een normaal goed. De vraagcurve verschuift naar [[*rechts|links]] en de evenwichtsprijs [[*stijgt|daalt]].",
        "Bij een hoger inkomen vragen gezinnen bij elke prijs meer. Het nieuwe snijpunt ligt hoger en verder naar rechts.")),

    # Balans (prent)
    klik("Bekijk de zes balansposten van bv Fietsenhof. Klik op de post die bij het eigen vermogen hoort.",
         BAL, [POST[3]],
         "Het kapitaal is het geld dat de eigenaars in de zaak gestoken hebben. Het staat bij het eigen vermogen aan de passiefzijde."),
    klik("Welke post van bv Fietsenhof moet pas over meerdere jaren helemaal terugbetaald zijn? Klik erop.",
         BAL, [POST[4]],
         "Een lening op tien jaar is een schuld op meer dan één jaar. Leveranciers zijn schulden op ten hoogste één jaar."),
    met_prent(BAL, tabel(
        "Staat deze post van bv Fietsenhof aan de actiefzijde of aan de passiefzijde?",
        [
            ("Gebouwen", "Actief"),
            ("Voorraad handelsgoederen", "Actief"),
            ("Leveranciers", "Passief"),
            ("Tegoed op de bankrekening", "Actief"),
        ],
        "Het actief toont de bezittingen, het passief toont hoe die gefinancierd zijn: eigen vermogen en schulden.",
        kolommen=["Actief", "Passief"])),
    met_prent(BAL, mk(
        "Welke post van bv Fietsenhof is een vast actief?",
        ["Gebouwen", "Voorraad handelsgoederen", "Tegoed op de bankrekening", "Leveranciers"],
        0,
        "Een gebouw blijft jaren in de zaak: het is een vast actief. Voorraad en geld op de bank zijn vlottende activa.")),

    # Kringloop en bbp
    sorteer(
        "Is dit een lek of een injectie in de binnenlandse kringloop?",
        ["Lek", "Injectie"],
        [
            ["sparen", "Lek"],
            ["uitvoer", "Injectie"],
            ["invoer", "Lek"],
            ["investeringen", "Injectie"],
        ],
        "Een lek haalt geld uit de binnenlandse kringloop (sparen, belastingen, invoer). Een injectie brengt geld erin (investeringen, overheidsuitgaven, uitvoer)."),
    inv("Een bedrijfskolom: de boer verkoopt graan voor 300 euro, de maalderij verkoopt meel voor 500 euro en de bakker verkoopt brood voor 900 euro. Hoeveel bedraagt de totale toegevoegde waarde in euro?",
        ["900"],
        "300 + (500 − 300) + (900 − 500) = 900 euro. De totale toegevoegde waarde is gelijk aan de waarde van het eindproduct."),
    inv("Het nominale bbp stijgt met 6 % en de prijzen stijgen met 2 %. Hoeveel procent bedraagt de reële groei ongeveer? Enkel het getal.",
        ["4"],
        "Reële groei ≈ nominale groei − prijsstijging = 6 − 2 = 4 %."),
    keuze(
        "Het bbp stijgt met 2 % en de bevolking met 3 %. Het bbp per capita [[*daalt|stijgt]]. Welvaart en welzijn zijn [[*niet hetzelfde|precies hetzelfde]].",
        "Als de bevolking sneller groeit dan het bbp, krijgt elke inwoner gemiddeld minder. Welzijn omvat ook gezondheid, milieu en geluk."),

    # Behoeften en goederen
    tabel(
        "Welk soort goed is dit?",
        [
            ("Een straatlantaarn", "Collectief goed"),
            ("Een broodrooster in de keuken", "Gebruiksgoed"),
            ("Een boterham", "Verbruiksgoed"),
        ],
        "Een collectief goed gebruikt iedereen samen. Een gebruiksgoed gaat lang mee, een verbruiksgoed verdwijnt bij gebruik.",
        kolommen=["Collectief goed", "Gebruiksgoed", "Verbruiksgoed"]),

    # Nut en budget
    inv("Het grensnut van vier opeenvolgende pannenkoeken is 9, 6, 2 en −1. Hoeveel bedraagt het totale nut van drie pannenkoeken?",
        ["17"],
        "9 + 6 + 2 = 17. Het totale nut is de som van de grensnutten."),
    mk("Een consument heeft 60 euro. Een boek kost 12 euro en een film 6 euro. Welke combinatie ligt precies op de budgetlijn?",
       ["3 boeken en 4 films", "4 boeken en 3 films", "2 boeken en 5 films", "5 boeken en 2 films"],
       0,
       "3 · 12 + 4 · 6 = 36 + 24 = 60 euro. Bij 4 boeken en 3 films kom je op 66 euro, dat is te veel."),
    keuze(
        "Als enkel het budget stijgt, verschuift de budgetlijn [[*evenwijdig naar buiten|evenwijdig naar binnen|en kantelt ze]]. De optimale goederencombinatie ligt waar de budgetlijn een indifferentiecurve [[*raakt|snijdt]].",
        "Een groter budget laat de prijsverhouding gelijk: de helling blijft. In het raakpunt bereik je de hoogste haalbare indifferentiecurve."),

    # Productie en kosten
    tabel(
        "TP bij 1 tot 4 werknemers is 20, 50, 70 en 80. Klopt dit?",
        [
            ("MP van de tweede werknemer is 30.", J),
            ("De gemiddelde productie bij vier werknemers is 20.", J),
            ("MP daalt vanaf de derde werknemer.", J),
            ("TP bereikt zijn maximum bij de tweede werknemer.", F),
        ],
        "MP = 20, 30, 20, 10. De gemiddelde productie bij vier is 80 / 4 = 20. TP stijgt zolang MP positief is."),
    sorteer(
        "Is dit een vaste of een variabele kost voor een bakkerij?",
        ["Vaste kost", "Variabele kost"],
        [
            ["de huur van het pand", "Vaste kost"],
            ["bloem en gist", "Variabele kost"],
            ["de verzekering van de oven", "Vaste kost"],
            ["de verpakking per brood", "Variabele kost"],
        ],
        "Vaste kosten blijven gelijk, wat je ook produceert. Variabele kosten stijgen met elke extra eenheid."),
    inv("Een bedrijf verkoopt 300 stuks aan 15 euro. De constante kosten zijn 1 200 euro en de variabele kost is 9 euro per stuk. Hoeveel winst maakt het in euro?",
        ["600"],
        "TO = 300 · 15 = 4 500. TK = 1 200 + 300 · 9 = 3 900. Winst = 4 500 − 3 900 = 600 euro."),
    keuze(
        "Een bedrijf bij volkomen concurrentie produceert de optimale hoeveelheid waar [[*MK gelijk is aan MO|GK zo laag mogelijk is|TO zo hoog mogelijk is]]. Bij volkomen concurrentie is MO gelijk aan de [[*prijs|totale kost]].",
        "Zolang een extra stuk meer oplevert dan het kost, loont het om meer te maken. Een prijsnemer krijgt voor elk stuk dezelfde prijs."),

    inv("Een bedrijf verkoopt aan 20 euro per stuk. De constante kosten zijn 3 000 euro en de variabele kost is 8 euro per stuk. Bij hoeveel stuks ligt het break-evenpunt?",
        ["250"],
        "Per stuk blijft er 20 − 8 = 12 euro over om de constante kosten te dekken. 3 000 / 12 = 250 stuks."),
    mk("Wat is het verschil tussen een kapitaalgoed en een intermediair goed bij een schrijnwerker?",
       ["De zaagmachine blijft, het hout gaat op in de kast.", "Het hout blijft jaren in de zaak, de zaagmachine verdwijnt.", "Beide gaan helemaal op in het eindproduct, de kast.", "Een kapitaalgoed koop je nooit, je huurt het altijd."],
       0,
       "Een kapitaalgoed zoals een machine gebruik je vele keren. Een intermediair goed zoals hout gaat op in het product."),
    # Markt en overheid
    mk("Waarom heeft een maximumprijs boven de evenwichtsprijs geen effect?",
       ["De marktprijs ligt al lager, dus die grens verandert niets.", "Verkopers mogen dan geen enkel stuk meer verkopen op de markt.", "Kopers moeten dan altijd die hoge maximumprijs gaan betalen.", "Er ontstaat dan automatisch een groot tekort op de markt."],
       0,
       "Een maximumprijs werkt enkel als hij onder de evenwichtsprijs ligt. Erboven verandert er niets."),

    # Arbeidsmarkt
    keuze(
        "Een minimumloon boven het evenwichtsloon leidt volgens het model tot [[*werkloosheid|een tekort aan werknemers]]. Een beroep waarvoor werkgevers moeilijk mensen vinden, heet een [[*knelpuntberoep|interprofessioneel akkoord]].",
        "Bij een loon boven het evenwicht willen meer mensen werken dan werkgevers vragen: er is een overschot aan arbeidsaanbod."),

    # Internationale handel
    tabel(
        "België legt een importheffing op ingevoerde fietsen. Klopt dit?",
        [
            ("De prijs van ingevoerde producten stijgt.", J),
            ("Binnenlandse producenten krijgen minder concurrentie.", J),
            ("Consumenten betalen minder dan voordien.", F),
            ("De overheid krijgt extra inkomsten.", J),
        ],
        "Een importheffing maakt buitenlandse producten duurder. Binnenlandse producenten en de overheid winnen, consumenten verliezen."),
    koppel(
        "Koppel de handelsbelemmering aan de uitleg.",
        [
            ["importheffing", "een belasting op ingevoerde goederen"],
            ["invoerquotum", "een maximum op de ingevoerde hoeveelheid"],
            ["uitvoersubsidie", "steun aan bedrijven die naar het buitenland verkopen"],
        ],
        ["een akkoord dat alle heffingen afschaft"],
        "Een handelsakkoord dat heffingen afschaft, is net het omgekeerde van een belemmering."),

    tabel(
        "Gaat de handelsbalans van dit land naar een overschot of een tekort?",
        [
            ("Uitvoer 500 miljard, invoer 450 miljard", "Overschot"),
            ("Uitvoer 300 miljard, invoer 340 miljard", "Tekort"),
            ("Uitvoer 120 miljard, invoer 100 miljard", "Overschot"),
        ],
        "Voert een land meer uit dan het invoert, dan heeft de handelsbalans een overschot. Omgekeerd is er een tekort.",
        kolommen=["Overschot", "Tekort"]),
    # Ondernemingsvormen
    tabel(
        "Eenmanszaak of bv?",
        [
            ("Je staat ook met je privévermogen in voor de schulden.", "Eenmanszaak"),
            ("De onderneming is een rechtspersoon.", "Bv"),
            ("Je betaalt personenbelasting op de winst.", "Eenmanszaak"),
            ("Er is een notariële akte nodig bij de oprichting.", "Bv"),
        ],
        "Een eenmanszaak heeft geen eigen rechtspersoonlijkheid: de eigenaar is onbeperkt aansprakelijk. Een bv is een rechtspersoon die vennootschapsbelasting betaalt.",
        kolommen=["Eenmanszaak", "Bv"]),

    # Resultatenrekening
    inv("Bedrijfsopbrengsten 400 000 euro, bedrijfskosten 340 000 euro, financieel resultaat −20 000 euro. Hoeveel is het resultaat voor belastingen in euro?",
        ["40000", "40 000"],
        "Bedrijfsresultaat = 400 000 − 340 000 = 60 000. Resultaat voor belastingen = 60 000 − 20 000 = 40 000 euro."),

    inv("De maatstaf van heffing is 800 euro. Hoeveel btw komt daarbij aan 21 procent? Enkel het getal.",
        ["168"],
        "21 % van 800 = 0,21 · 800 = 168 euro."),
    # Boekhouden
    keuze(
        "Een kost boek je in klasse [[*6|7|2]]. Bij elke boeking is het totaal in het debet [[*gelijk aan|groter dan]] het totaal in het credit.",
        "Klasse 6 zijn de kosten, klasse 7 de opbrengsten. Dubbel boekhouden betekent dat debet en credit altijd in evenwicht zijn."),
    volgorde(
        "Zet de stappen van het boeken van een verrichting in de juiste volgorde.",
        ["Het stuk lezen, bijvoorbeeld een factuur", "Het redeneerschema invullen", "De boeking in het journaal schrijven", "De bedragen overbrengen naar het grootboek"],
        "Je begrijpt eerst de verrichting, redeneert welke rekeningen stijgen of dalen, boekt in het journaal op datum en brengt dan over naar het grootboek."),

    # Facturen
    inv("Goederen kosten 2 000 euro. De handelskorting is 10 %, de financiële korting 2 %. Hoeveel bedraagt de maatstaf van heffing in euro?",
        ["1764", "1 764"],
        "2 000 − 200 = 1 800. Financiële korting: 2 % van 1 800 = 36. Maatstaf van heffing = 1 800 − 36 = 1 764 euro."),
    mk("Waarom geeft een leverancier een handelskorting?",
       ["Om een trouwe of grote klant te belonen.", "Om sneller betaald te worden door de klant.", "Om de btw op de factuur niet te moeten betalen.", "Om de vervoerkosten van de levering door te rekenen."],
       0,
       "Een handelskorting is een korting op de prijs, bv. voor een grote bestelling. Een financiële korting beloont snel betalen."),

    # Strategie en marketing
    sorteer(
        "Hoort dit bij de interne of de externe analyse in een SWOT?",
        ["Intern (sterkte of zwakte)", "Extern (kans of bedreiging)"],
        [
            ["goed opgeleid personeel", "Intern (sterkte of zwakte)"],
            ["een nieuwe concurrent in de straat", "Extern (kans of bedreiging)"],
            ["een verouderde website", "Intern (sterkte of zwakte)"],
            ["een groeiende vraag naar bio", "Extern (kans of bedreiging)"],
        ],
        "Sterktes en zwaktes liggen binnen het bedrijf. Kansen en bedreigingen komen uit de omgeving."),
    koppel(
        "Koppel de P van de marketingmix aan het voorbeeld.",
        [
            ["product", "een nieuwe smaak en een mooie verpakking"],
            ["prijs", "een lage introductieprijs"],
            ["plaats", "verkoop via de eigen webwinkel"],
            ["promotie", "een reclamefilmpje op sociale media"],
        ],
        [],
        "De vier P's zijn product, prijs, plaats (distributie) en promotie."),
    mk("Wie is een externe stakeholder van een bakkerij?",
       ["De leverancier van bloem", "De bakkers die er werken", "De eigenaar van de zaak", "De verkopers achter de toonbank"],
       0,
       "Externe stakeholders staan buiten de organisatie: klanten, leveranciers, buren, overheid. Personeel en eigenaars zijn interne stakeholders."),
    keuze(
        "Een nieuw product begint met een hoge prijs voor wie het meteen wil hebben. Dat is een [[*afroomstrategie|penetratiestrategie]]. Wie het product in zoveel mogelijk winkels legt, kiest voor [[*intensieve distributie|exclusieve distributie]].",
        "Afromen haalt eerst de klanten binnen die veel willen betalen. Intensieve distributie zet in op zoveel mogelijk verkooppunten."),

    # Schrijfopdracht
    open_("De prijs van aardbeien daalt sterk na een zeer goede oogst. Leg in 4 à 6 zinnen uit met vraag en aanbod wat er op de markt gebeurt en waarom de markt zichzelf regelt.",
          "Door de goede oogst stijgt het aanbod: de aanbodcurve verschuift naar rechts. Bij de oude prijs is er dan een overschot, want er zijn meer aardbeien dan kopers willen. Verkopers verlagen hun prijs om toch te verkopen. Bij een lagere prijs kopen mensen meer aardbeien. Zo ontstaat er een nieuw evenwicht met een lagere prijs en een grotere hoeveelheid. Het marktmechanisme heft het overschot vanzelf op.",
          "Een goed antwoord noemt de verschuiving van het aanbod, het overschot bij de oude prijs, de prijsdaling en het nieuwe evenwicht."),
]

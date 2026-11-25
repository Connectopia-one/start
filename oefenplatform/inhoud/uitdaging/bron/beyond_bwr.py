# -*- coding: utf-8 -*-
"""Uitdaging Bedrijfswetenschappen en recht 🌍 Beyond doorstroom (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een break-evengrafiek en een BCG-matrix om op
te klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in
de hoofdstukken van Bedrijfswetenschappen en recht Beyond doorstroom. Alle
bedrijven, producten en cijfers zijn verzonnen.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_bwr.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Bedrijfswetenschappen en recht"
BESTAND = "beyond-bwr-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/bwr-beyond-uitdaging"
BE = "breakeven-fietsen.svg"
BCG = "bcg-snoep.svg"

# klikvakken uit maak_prenten_beyond_bwr.py
BEP = [55.8, 38.8, 6.8, 10.6]
ZONE1 = [32.9, 55.2, 6.4, 10.0]
ZONE2 = [75.2, 25.6, 6.4, 10.0]
ZUUR = [60.6, 65.0, 26.7, 9.7]
PROT = [23.9, 29.7, 26.7, 9.7]
CHOC = [23.9, 65.0, 26.7, 9.7]
VEGAN = [60.6, 29.7, 26.7, 9.7]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Break-even (prent)
    klik("Bekijk de grafiek. Klik op het break-evenpunt.",
         BE, [BEP],
         "Het break-evenpunt ligt waar de totale opbrengst (TO) gelijk is aan de totale kosten (TK): bij 600 herstellingen en 15 000 euro."),
    klik("Klik op het cijfer in de zone waar de fietsenmaker winst maakt.",
         BE, [ZONE2],
         "Rechts van het break-evenpunt ligt de opbrengstlijn boven de kostenlijn: daar is er winst."),
    met_prent(BE, tabel(
        "Lees af en reken na. De vaste kosten zijn 6000 euro, de variabele kost is 15 euro per herstelling en de prijs 25 euro.",
        [
            ("Dekkingsbijdrage per herstelling (euro)", "10"),
            ("Break-evenafzet (herstellingen)", "600"),
            ("Break-evenomzet (euro)", "15000"),
        ],
        "Dekkingsbijdrage = 25 − 15 = 10 euro. Break-evenafzet = 6000 / 10 = 600. Omzet = 600 · 25 = 15 000 euro.",
        kolommen=["10", "600", "15000"])),
    met_prent(BE, inv(
        "Hoeveel winst maakt de fietsenmaker bij 900 herstellingen? Enkel het getal in euro.",
        ["3000", "3 000", "3.000"],
        "Winst = 900 · 10 − 6000 = 9000 − 6000 = 3000 euro."),
    ),
    met_prent(BE, mk(
        "Wat is de veiligheidsmarge als hij 800 herstellingen verwacht?",
        ["200 herstellingen of 25 %", "600 herstellingen of 75 %", "800 herstellingen of 100 %", "200 herstellingen of 33 %"],
        0,
        "Veiligheidsmarge = verwachte afzet − break-evenafzet = 800 − 600 = 200. Dat is 200 / 800 = 25 % van de verwachte afzet.")),

    # BCG-matrix (prent)
    klik("Bekijk de BCG-matrix. Klik op de melkkoe.",
         BCG, [CHOC],
         "Een melkkoe heeft een hoog marktaandeel in een markt die weinig groeit. Ze brengt veel geld op en vraagt weinig investeringen."),
    klik("Klik op het vraagteken.",
         BCG, [VEGAN],
         "Een vraagteken heeft een laag marktaandeel in een snelgroeiende markt. Het bedrijf moet kiezen: fors investeren of stoppen."),
    met_prent(BCG, tabel(
        "Welke strategie past volgens de BCG-matrix?",
        [
            ("Proteïnerepen", "Investeren om de positie te houden"),
            ("Chocoladerepen", "Geld afromen voor andere producten"),
            ("Zuurstokken", "Afbouwen of afstoten"),
        ],
        "Een ster (proteïnerepen) verdient investeringen, een melkkoe (chocoladerepen) levert geld, een hond (zuurstokken) bouw je af.",
        kolommen=["Investeren om de positie te houden", "Geld afromen voor andere producten", "Afbouwen of afstoten"])),

    # Ondernemingsvormen en belastingen
    tabel(
        "Welke ondernemingsvorm past?",
        [
            ("Eén persoon, geen rechtspersoonlijkheid, privévermogen niet beschermd", "Eenmanszaak"),
            ("Rechtspersoon, geen minimumkapitaal, aandeelhouders beperkt aansprakelijk", "BV"),
            ("Geschikt voor grote bedrijven met aandelen op de beurs", "NV"),
        ],
        "In een eenmanszaak zijn ondernemer en zaak één. De BV is de gewone vennootschap voor kmo's, de NV voor grote bedrijven en beursnoteringen.",
        kolommen=["Eenmanszaak", "BV", "NV"]),
    keuze(
        "De personenbelasting is [[*progressief|vast|degressief]]: hoe hoger het inkomen, hoe [[*hoger|lager]] het tarief voor de hogere schijven.",
        "Het belastbaar inkomen wordt in schijven verdeeld met stijgende tarieven."),
    mk("Waarom doet een vennootschap voorafbetalingen voor de vennootschapsbelasting?",
       ["Om een belastingvermeerdering te vermijden.", "Om haar winst kunstmatig kleiner te maken.", "Omdat ze anders geen btw mag aanrekenen.", "Omdat ze anders haar boekhouding niet mag afsluiten."],
       0,
       "Wie te weinig vooraf betaalt, krijgt een belastingvermeerdering. Wie vooraf betaalt, kan zelfs een voordeel krijgen."),
    inv("Een vennootschap heeft een belastbare winst van 400 000 euro en valt onder het gewone tarief van 25 %. Hoeveel vennootschapsbelasting is dat? Enkel het getal.",
        ["100000", "100 000", "100.000"],
        "25 % van 400 000 = 100 000 euro."),

    # Boekhouden
    tabel(
        "Op welke rekening boek je dit bij een aankoop van handelsgoederen op krediet?",
        [
            ("De waarde van de goederen exclusief btw", "604 Aankopen handelsgoederen"),
            ("De btw op de aankoop", "411 Terug te vorderen btw"),
            ("Het totaalbedrag dat je nog moet betalen", "440 Leveranciers"),
        ],
        "De kost staat in klasse 6, de aftrekbare btw op 411 en de schuld aan de leverancier op 440.",
        kolommen=["604 Aankopen handelsgoederen", "411 Terug te vorderen btw", "440 Leveranciers"]),
    keuze(
        "Bij een verkoopfactuur boek je de klant op 400 in het [[*debet|credit]]. De te betalen btw komt op 451 in het [[*credit|debet]].",
        "De klant is een vordering (actief): die vermeerdert in het debet. De btw die je aan de staat verschuldigd bent, is een schuld: vermeerdering in het credit."),
    inv("Een factuur vermeldt 2000 euro handelsgoederen, 2 % korting en 21 % btw. Hoeveel bedraagt het te betalen bedrag? Enkel het getal in euro.",
        ["2371,6", "2371,60", "2371.6", "2371.60"],
        "Na korting: 2000 · 0,98 = 1960 euro. Btw: 1960 · 0,21 = 411,60. Totaal: 2371,60 euro."),
    sorteer(
        "Is dit een balansrekening of een resultatenrekening?",
        ["Balans", "Resultatenrekening"],
        [
            ["550 Bank", "Balans"],
            ["700 Omzet", "Resultatenrekening"],
            ["440 Leveranciers", "Balans"],
            ["620 Bezoldigingen", "Resultatenrekening"],
            ["221 Gebouwen", "Balans"],
            ["650 Rentelasten", "Resultatenrekening"],
        ],
        "Klassen 1 tot 5 staan op de balans, klassen 6 en 7 (kosten en opbrengsten) op de resultatenrekening."),
    mk("Waarom boekt een bedrijf aan het einde van het jaar afschrijvingen?",
       ["Om de waardedaling van vaste activa over de jaren te spreiden.", "Om de schulden aan de leveranciers definitief te schrappen.", "Om de omzet van het volgende boekjaar nu al mee te tellen.", "Om het geld op de bankrekening opnieuw sneller te laten groeien."],
       0,
       "Een machine gaat meerdere jaren mee. Met afschrijvingen verdeel je de aankoopprijs als kost over die jaren."),

    # Financiële analyse
    tabel(
        "Een bedrijf heeft: vlottende activa 300 000, schulden op korte termijn 200 000, eigen vermogen 400 000, totaal vermogen 1 000 000, nettowinst 40 000. Bereken.",
        [
            ("Current ratio", "1,5"),
            ("Solvabiliteit (in %)", "40"),
            ("Rendabiliteit van het eigen vermogen (in %)", "10"),
        ],
        "Current ratio = 300 000 / 200 000 = 1,5. Solvabiliteit = 400 000 / 1 000 000 = 40 %. REV = 40 000 / 400 000 = 10 %.",
        kolommen=["1,5", "10", "40"]),
    keuze(
        "Een current ratio onder 1 wijst op [[*liquiditeitsproblemen|een hoge winst|een sterke solvabiliteit]]: het bedrijf kan zijn [[*kortetermijnschulden|aandeelhouders]] moeilijk betalen.",
        "Als de vlottende activa kleiner zijn dan de schulden op korte termijn, dreigen betalingsproblemen."),
    sorteer(
        "Is dit eigen of vreemd vermogen?",
        ["Eigen vermogen", "Vreemd vermogen"],
        [
            ["Kapitaal ingebracht door de aandeelhouders", "Eigen vermogen"],
            ["Een banklening op vijf jaar", "Vreemd vermogen"],
            ["Overgedragen winst", "Eigen vermogen"],
            ["Schulden aan leveranciers", "Vreemd vermogen"],
        ],
        "Eigen vermogen komt van de eigenaars (kapitaal, reserves, overgedragen winst). Vreemd vermogen zijn schulden aan derden."),
    inv("Een investering kost 50 000 euro en levert elk jaar 12 500 euro netto kasstroom op. Wat is de terugverdientijd in jaren?",
        ["4"],
        "50 000 / 12 500 = 4 jaar."),
    mk("Welke financieringsvorm is meestal het best voor een nieuwe bedrijfshal?",
       ["Een lening op lange termijn", "Een kaskrediet op korte termijn", "Leverancierskrediet van 30 dagen", "Een voorschot van een klant"],
       0,
       "Vaste activa financier je met lang vermogen (gouden balansregel). Kortlopend krediet past bij vlottende activa."),

    # Strategie en marketing
    sorteer(
        "Hoort dit bij de interne of de externe analyse van SWOT?",
        ["Intern (sterktes en zwaktes)", "Extern (kansen en bedreigingen)"],
        [
            ["Ervaren en gemotiveerd personeel", "Intern (sterktes en zwaktes)"],
            ["Een nieuwe concurrent opent in de buurt", "Extern (kansen en bedreigingen)"],
            ["Verouderde machines", "Intern (sterktes en zwaktes)"],
            ["Stijgende vraag naar duurzame producten", "Extern (kansen en bedreigingen)"],
        ],
        "Sterktes en zwaktes gaan over het bedrijf zelf. Kansen en bedreigingen komen van buiten."),
    tabel(
        "Bij welke P van de marketingmix hoort dit?",
        [
            ("Een kortingsactie van 20 %", "Prijs"),
            ("Een reclamecampagne op sociale media", "Promotie"),
            ("Verkopen via een webshop en in supermarkten", "Plaats"),
            ("Een nieuwe smaak en verpakking", "Product"),
        ],
        "De marketingmix bestaat uit product, prijs, plaats (distributie) en promotie.",
        kolommen=["Product", "Prijs", "Plaats", "Promotie"]),
    koppel(
        "Koppel het bouwblok van het Business Model Canvas aan het voorbeeld.",
        [
            ["klantsegmenten", "sportieve jongeren tussen 16 en 25"],
            ["waardepropositie", "gezonde snack met veel eiwitten"],
            ["kanalen", "webshop en fitnesscentra"],
            ["inkomstenstromen", "verkoop per doos en abonnementen"],
        ],
        ["een hogere vennootschapsbelasting"],
        "Het canvas beschrijft voor wie je waarde maakt, welke, hoe je de klant bereikt en hoe je geld verdient."),
    mk("Welke stakeholder is een interne belanghebbende?",
       ["De werknemers", "De overheid", "De banken", "De buurtbewoners"],
       0,
       "Interne stakeholders werken in of bezitten het bedrijf: werknemers, management en eigenaars."),

    # Arbeidsrecht en HRM
    tabel(
        "Klopt dit over de arbeidsovereenkomst?",
        [
            ("Een arbeidsovereenkomst bevat arbeid, loon en gezag.", J),
            ("Tijdens ziekte wordt de overeenkomst geschorst.", J),
            ("Een werkgever mag zonder opzeg ontslaan bij elke kleine fout.", F),
            ("Een overeenkomst van bepaalde duur eindigt vanzelf op de einddatum.", J),
        ],
        "De drie kenmerken zijn arbeid, loon en een gezagsverhouding. Ontslag zonder opzeg kan enkel bij een dringende reden: een zware fout."),
    volgorde(
        "Zet de stappen van het aanwervingsproces in de juiste volgorde.",
        ["Functieomschrijving opstellen", "Vacature bekendmaken", "Kandidaten selecteren", "Arbeidsovereenkomst ondertekenen", "Nieuwe medewerker onthalen"],
        "Eerst weet je wie je zoekt, dan maak je de vacature bekend, selecteer je, teken je het contract en verwelkom je de nieuwe collega."),

    # Logistiek, kostprijs en databanken
    keuze(
        "Bij just-in-time leveren leveranciers [[*precies wanneer het nodig is|zo vroeg mogelijk]], zodat de voorraad [[*klein|groot]] blijft.",
        "Just-in-time beperkt opslagkosten, maar maakt het bedrijf afhankelijk van stipte leveringen."),
    tabel(
        "Is dit een vaste of een variabele kost voor een fietsenmaker?",
        [
            ("Huur van het atelier", "Vaste kost"),
            ("Binnenbanden voor elke herstelling", "Variabele kost"),
            ("Verzekering van het atelier", "Vaste kost"),
            ("Smeerolie per herstelling", "Variabele kost"),
        ],
        "Vaste kosten blijven gelijk, wat de productie ook is. Variabele kosten stijgen mee met het aantal herstellingen.",
        kolommen=["Vaste kost", "Variabele kost"]),
    inv("Een product kost 8 euro aan grondstoffen, 5 euro aan loon en 3 euro aan toegerekende vaste kosten per stuk. Het bedrijf wil 25 % winstopslag op de kostprijs. Wat is de verkoopprijs exclusief btw? Enkel het getal.",
        ["20", "20,00"],
        "Kostprijs = 8 + 5 + 3 = 16 euro. Met 25 % opslag: 16 · 1,25 = 20 euro."),
    keuze(
        "In een relationele databank identificeert de [[*primaire sleutel|vreemde sleutel]] elk record uniek. De [[*vreemde sleutel|primaire sleutel]] verwijst naar een record in een andere tabel.",
        "Een primaire sleutel (bv. klantnummer) is uniek per rij. Een vreemde sleutel legt de relatie met een andere tabel."),
    mk("Een tabel Bestellingen bevat het veld klantnummer, dat verwijst naar de tabel Klanten. Welke relatie is dat meestal?",
       ["Eén klant heeft meerdere bestellingen.", "Elke bestelling heeft meerdere klanten.", "Eén klant heeft precies één bestelling.", "Er is geen relatie tussen beide tabellen."],
       0,
       "Een klant kan vaak bestellen, maar elke bestelling hoort bij één klant: een een-op-veelrelatie."),

    # Recht en algemeen
    keuze(
        "Een vennootschap is een [[*rechtspersoon|natuurlijk persoon]]: ze kan zelf contracten sluiten en [[*eigen schulden|geen bezittingen]] hebben.",
        "Een rechtspersoon heeft een eigen vermogen los van dat van de aandeelhouders."),
    mk("Een klant betaalt een factuur van 1210 euro (incl. 21 % btw) via overschrijving. Welke boeking hoort daarbij?",
       ["550 Bank debet en 400 Klanten credit, elk 1210 euro.", "400 Klanten debet en 550 Bank credit, elk 1210 euro.", "550 Bank debet 1000 euro en 451 Btw credit 210 euro.", "700 Omzet debet en 550 Bank credit, elk voor 1210 euro."],
       0,
       "Het geld komt binnen op de bank (debet) en de vordering op de klant verdwijnt (credit). De btw werd al bij de verkoopfactuur geboekt."),

    tabel(
        "Is dit een kenmerk van de arbeidsovereenkomst voor bepaalde of onbepaalde duur?",
        [
            ("Er staat een vaste einddatum in het contract.", "Bepaalde duur"),
            ("Het contract loopt tot iemand opzegt.", "Onbepaalde duur"),
            ("Hij eindigt vanzelf als het afgesproken werk af is.", "Bepaalde duur"),
        ],
        "Een contract van bepaalde duur of voor een duidelijk omschreven werk eindigt vanzelf. Een contract van onbepaalde duur loopt door tot opzeg.",
        kolommen=["Bepaalde duur", "Onbepaalde duur"]),
    mk("Wat is het hoofddoel van supply chain management?",
       ["De hele keten van leverancier tot klant op elkaar afstemmen.", "Zo veel mogelijk voorraad aanleggen voor elk product in elk magazijn.", "Alle leveranciers vervangen door één enkele buitenlandse leverancier.", "De verkoopprijzen verhogen zodra de vraag van de klanten stijgt."],
       0,
       "Supply chain management stemt aankoop, productie, opslag en levering op elkaar af, zodat de klant op tijd krijgt wat hij wil tegen zo laag mogelijke kosten."),
    keuze(
        "In de saldibalans moet het totaal van de debetsaldi [[*gelijk zijn aan|groter zijn dan]] het totaal van de creditsaldi. Dat controleert of je [[*dubbel|enkel]] boekhoudt zonder fouten.",
        "Elke boeking heeft evenveel debet als credit. Daarom moeten de totalen in de saldibalans altijd gelijk zijn."),
    inv("Een bedrijf koopt een machine van 30 000 euro die 5 jaar meegaat, zonder restwaarde. Hoeveel bedraagt de jaarlijkse lineaire afschrijving? Enkel het getal.",
        ["6000", "6 000", "6.000"],
        "30 000 / 5 = 6000 euro per jaar."),

    # Schrijfopdracht
    open_("Een vriendin wil een koffiebar starten. Leg in 4 à 6 zinnen uit welke ondernemingsvorm je haar aanraadt en waarom, en noem twee onderdelen die zeker in haar ondernemingsplan moeten staan.",
          "Ik raad een BV aan, omdat ze dan beperkt aansprakelijk is: als het misloopt, blijft haar privévermogen beschermd. Een BV heeft geen minimumkapitaal, maar wel een financieel plan. Een eenmanszaak is eenvoudiger, maar dan staat haar huis op het spel. In het ondernemingsplan moet zeker een marktanalyse staan met klanten en concurrenten, en een financieel plan met de investeringen, kosten en verwachte omzet.",
          "Een goed antwoord kiest een ondernemingsvorm met een argument (aansprakelijkheid, belastingen, eenvoud) en noemt twee onderdelen van het ondernemingsplan, zoals marktanalyse, marketingplan of financieel plan."),
]

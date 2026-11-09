"""Relationele databanken — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import db_veld_zone, db_record_zone, db_naam_zone, db_relatie_zone

PRENTEN = [
    dict(bestand="databank.svg", zelf=True,
         wat="Twee tabellen van een webwinkel (Klanten en Bestellingen) met een één-op-veel-relatie.",
         vragen="klikvragen en vragen over sleutels, relaties en query's"),
]

VRAGEN = [
    klik(
        "Klik op de primaire sleutel van de tabel Bestellingen.",
        "databank.svg",
        [db_veld_zone("Bestellingen", 0)],
        "Bestelnr is uniek voor elke bestelling: dat is de primaire sleutel (het sleuteltje).",
    ),
    klik(
        "Klik op het veld in de tabel Bestellingen dat de koppeling maakt met de tabel Klanten.",
        "databank.svg",
        [db_veld_zone("Bestellingen", 1)],
        "Klantnr in Bestellingen verwijst naar de primaire sleutel Klantnr in Klanten.",
    ),
    klik(
        "Klik op de relatie tussen de twee tabellen.",
        "databank.svg",
        [db_relatie_zone()],
        "De lijn verbindt Klantnr in Klanten met Klantnr in Bestellingen.",
    ),
    klik(
        "Klik op de primaire tabel van de relatie.",
        "databank.svg",
        [db_naam_zone("Klanten")],
        "Klanten staat aan de kant van de 1: dat is de primaire tabel. Bestellingen is de gerelateerde tabel.",
    ),
    klik(
        "Klik op het record van de bestelling van klant Claes.",
        "databank.svg",
        [db_record_zone("Bestellingen", 1)],
        "Claes heeft klantnummer 3. Bestelling 102 hoort bij klantnummer 3.",
    ),
    met_prent("databank.svg", mk(
        "Welke soort relatie bestaat er tussen Klanten en Bestellingen?",
        ["Eén-op-veel", "Eén-op-één", "Veel-op-veel", "Er is geen relatie"],
        0,
        "Eén klant kan veel bestellingen hebben, maar elke bestelling hoort bij één klant.",
    )),
    met_prent("databank.svg", mk(
        "Een totaalquery telt het aantal bestellingen per klant. Welk resultaat krijgt klant 1?",
        ["3", "1", "5", "224,90"],
        0,
        "Bestellingen 101, 103 en 105 horen bij klant 1.",
    )),
    met_prent("databank.svg", mk(
        "Een totaalquery berekent de som van het bedrag per klant. Wat is het resultaat voor klant 1?",
        ["224,90", "120,00", "500,40", "3"],
        0,
        "120,00 + 89,90 + 15,00 = 224,90.",
    )),
    met_prent("databank.svg", mk(
        "Een selectiequery toont de klanten uit Hasselt. Hoeveel records krijg je?",
        ["2", "1", "4", "3"],
        0,
        "Peeters en Maes wonen in Hasselt.",
    )),
    met_prent("databank.svg", tabel(
        "Referentiële integriteit staat aan. Wat laat de databank toe?",
        [
            ("Een nieuwe bestelling toevoegen voor klant 4", J),
            ("Een nieuwe bestelling toevoegen voor klant 9, die niet in Klanten staat", F),
            ("Klant 2 verwijderen terwijl bestelling 104 nog naar hem verwijst", F),
            ("Klant 4 verwijderen, die geen bestellingen heeft", J),
        ],
        "Met referentiële integriteit kan een bestelling niet verwijzen naar een klant die niet bestaat.",
    )),
    met_prent("databank.svg", mk(
        "Waarom staat de naam van de klant niet in de tabel Bestellingen?",
        [
            "Om redundantie te vermijden: de naam staat één keer in Klanten",
            "Omdat namen niet in een databank mogen",
            "Omdat Bestellingen geen tekstvelden mag hebben",
            "Omdat de naam de primaire sleutel is",
        ],
        0,
        "Anders staat Peeters drie keer in Bestellingen, met kans op tikfouten en tegenstrijdige gegevens.",
    )),
    tabel(
        "Welk gegevenstype past het best bij het veld?",
        [
            ("Geboortedatum", "Datum/tijd"),
            ("Prijs in euro", "Valuta"),
            ("Telefoonnummer", "Korte tekst"),
            ("Factuur betaald of niet", "Ja/nee"),
        ],
        "Een telefoonnummer is tekst: je rekent er niet mee en een voorloopnul moet blijven staan.",
        kolommen=["Datum/tijd", "Valuta", "Korte tekst", "Ja/nee"],
    ),
    tabel(
        "Welke veldeigenschap gebruik je?",
        [
            ("Een postcode moet altijd ingevuld worden", "Vereist"),
            ("Een nieuw record krijgt automatisch het land België", "Standaardwaarde"),
            ("Een prijs mag niet negatief zijn", "Validatieregel"),
            ("Een postcode moet uit vier cijfers bestaan, in een vast patroon", "Invoermasker"),
        ],
        "Veldeigenschappen bewaken de gegevensintegriteit.",
        kolommen=["Vereist", "Standaardwaarde", "Validatieregel", "Invoermasker"],
    ),
    tabel(
        "Welke query heb je nodig?",
        [
            ("Alle prijzen met 5 % verhogen", "Bijwerkquery"),
            ("De bestellingen van 2024 naar een archieftabel kopiëren", "Toevoegquery"),
            ("Alle bestellingen van een opgeheven winkel wissen", "Verwijderquery"),
            ("Van een selectie een nieuwe tabel maken", "Tabelmaakquery"),
        ],
        "Elke query heeft haar eigen taak.",
        kolommen=["Bijwerkquery", "Toevoegquery", "Verwijderquery", "Tabelmaakquery"],
    ),
    sorteer(
        "Verandert de query gegevens of niet?",
        ["Verandert gegevens", "Toont enkel"],
        [
            ["Bijwerkquery", "Verandert gegevens"],
            ["Selectiequery", "Toont enkel"],
            ["Verwijderquery", "Verandert gegevens"],
            ["Totaalquery", "Toont enkel"],
        ],
        "Actiequery's wijzigen de tabellen, selectie- en totaalquery's tonen een resultaat.",
    ),
    koppel(
        "Koppel het onderdeel van de databank aan zijn functie.",
        [
            ["Tabel", "Bewaart de gegevens"],
            ["Query", "Zoekt, berekent of wijzigt gegevens"],
            ["Formulier", "Maakt het invoeren van gegevens makkelijk"],
            ["Rapport", "Toont gegevens netjes om af te drukken"],
        ],
        ["Berekent de btw-aangifte automatisch"],
        "Elk onderdeel heeft zijn eigen taak.",
    ),
    tabel(
        "Waar of niet waar over databanken?",
        [
            ("Een query kan gegevens uit twee gerelateerde tabellen samen tonen.", J),
            ("Een totaalquery kan het gemiddelde bedrag per klant berekenen.", J),
            ("Een veld is een kolom, een record is een rij.", J),
            ("Een primaire sleutel moet altijd een tekstveld zijn.", F),
        ],
        "Een primaire sleutel mag ook een getal of een autonummering zijn.",
    ),
    keuze(
        "Een totaalquery kan per groep de [[*som|validatieregel|primaire sleutel]] van een veld berekenen, of het [[*aantal|invoermasker|bijschrift]] records tellen.",
        "Een totaalquery groepeert records en vat ze samen.",
    ),
    mk(
        "Een bedrijf bewaart werknemers en hun toegangsbadges. Elke werknemer heeft precies één badge en elke badge hoort bij precies één werknemer. Welke relatie is dat?",
        ["Eén-op-één", "Eén-op-veel", "Veel-op-één", "Geen relatie"],
        0,
        "Bij elk record in de ene tabel hoort hoogstens één record in de andere: één-op-één.",
    ),
    mk(
        "In de tabel heet een veld Klantnr, maar in het formulier wil je 'Klantnummer' zien. Welke veldeigenschap stel je in, en wat doet ze?",
        [
            "Ze bepaalt welke naam je in formulieren boven het veld ziet",
            "Ze bepaalt hoeveel tekens het veld mag bevatten",
            "Ze vult automatisch een waarde in",
            "Ze controleert of de invoer juist is",
        ],
        0,
        "Bijvoorbeeld Klantnr in de tabel, maar 'Klantnummer' in het formulier.",
    ),
    inv(
        "Hoe noemt men het dubbel opslaan van dezelfde gegevens op verschillende plaatsen in een databank?",
        "redundantie",
        "Redundantie vergroot de kans op tegenstrijdige gegevens.",
    ),
    sleep(
        "Gegevens zijn [[juist]], [[volledig]] en consistent: dat heet gegevensintegriteit.",
        ["redundant", "verborgen"],
        "Veldeigenschappen en referentiële integriteit helpen om dat te bewaken.",
    ),
    mk(
        "In de tabel Klanten is het veld Klantnr de primaire sleutel. Wat gebeurt er als je een nieuwe klant invoert met klantnummer 2?",
        [
            "De databank weigert het record, want 2 bestaat al",
            "Janssens wordt automatisch overschreven",
            "Het record wordt als 2b opgeslagen",
            "Beide klanten krijgen klantnummer 2",
        ],
        0,
        "Een primaire sleutel moet uniek zijn.",
    ),
    mk(
        "Welke veldeigenschap bepaalt hoeveel tekens er maximaal in een tekstveld mogen?",
        ["Veldlengte", "Standaardwaarde", "Bijschrift", "Vereist"],
        0,
        "Bijvoorbeeld een veldlengte van 4 voor een postcode.",
    ),
    met_prent("databank.svg", mk(
        "Je zet een filter op Gemeente = Genk in de tabel Klanten. Wat gebeurt er met de andere klanten?",
        [
            "Ze worden tijdelijk verborgen en blijven in de tabel",
            "Ze worden definitief uit de tabel gewist",
            "Ze worden naar een nieuwe tabel gekopieerd",
            "Hun gemeente wordt veranderd in Genk",
        ],
        0,
        "Een filter toont enkel de records die voldoen. Zet je het filter uit, dan zie je alles terug.",
    )),
    met_prent("databank.svg", mk(
        "Welke klant heeft samen voor het grootste bedrag besteld?",
        ["Janssens", "Peeters", "Claes", "Maes"],
        0,
        "Peeters bestelde drie keer, samen 224,90 euro. Janssens bestelde één keer, maar voor meer.",
    )),
    open_(
        "Een webwinkel bewaart alles in één grote tabel: bij elke bestelling staan opnieuw de naam, het adres en het telefoonnummer van de klant. Leg uit waarom dat een probleem is en hoe je het oplost.",
        "Dezelfde klantgegevens staan vele keren in de tabel (redundantie). Als een klant verhuist, moet je elk record aanpassen en vergeet je er gemakkelijk een, zodat de gegevens tegenstrijdig worden. Oplossing: een aparte tabel Klanten met een primaire sleutel Klantnr, en in Bestellingen enkel het Klantnr, met een één-op-veel-relatie.",
        "Splitsen in tabellen vermijdt dubbele gegevens.",
    ),
    casus(
        "Bekijk de tabellen van de webwinkel. De winkel wil een rapport met alle bestellingen boven 50 euro, gesorteerd van groot naar klein.",
        [
            met_prent("databank.svg", mk(
                "Welke query maak je?",
                ["Een selectiequery met een voorwaarde op Bedrag", "Een verwijderquery op Bedrag", "Een tabelmaakquery op Klantnr", "Een bijwerkquery op Datum"],
                0,
                "Je wil enkel tonen en sorteren, niets wijzigen.",
            )),
            met_prent("databank.svg", mk(
                "Hoeveel records toont de query?",
                ["3", "2", "4", "5"],
                0,
                "Drie bestellingen hebben een bedrag boven 50 euro.",
            )),
            met_prent("databank.svg", mk(
                "Welke bestelling staat onderaan in het rapport?",
                ["103", "102", "105", "101"],
                0,
                "Van de bestellingen boven 50 euro heeft 103 het kleinste bedrag: 89,90 euro.",
            )),
        ],
    ),
]

"""Eindejaarsverrichtingen en de saldibalans — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone

PRENTEN = [
    dict(bestand="overlopende-rekeningen.svg", zelf=True,
         wat="Schema met de vier overlopende rekeningen: kost of opbrengst, en volgend jaar of dit jaar.",
         vragen="klikvragen en een tabel over de overlopende rekeningen"),
]

VRAGEN = [
    klik(
        "Een onderneming betaalt op 1 oktober de verzekering voor een heel jaar vooraf. Klik op de overlopende rekening die ze op 31 december gebruikt.",
        "overlopende-rekeningen.svg",
        [raster_zone(0, 0, 2, 2)],
        "De premie is al betaald, maar negen maanden horen bij het volgende jaar: over te dragen kosten.",
    ),
    klik(
        "De interest op een belegging over de laatste maanden van dit jaar wordt pas in maart volgend jaar gestort. Klik op de overlopende rekening die je op 31 december gebruikt.",
        "overlopende-rekeningen.svg",
        [raster_zone(1, 1, 2, 2)],
        "De opbrengst hoort bij dit jaar, maar het geld komt pas later: verkregen opbrengsten.",
    ),
    met_prent("overlopende-rekeningen.svg", tabel(
        "Welke overlopende rekening gebruik je op 31 december?",
        [
            ("Een huurder betaalt in december al de huur van januari", "Over te dragen opbrengsten"),
            ("De factuur van het water van het vierde kwartaal komt pas in februari", "Toe te rekenen kosten"),
            ("Een abonnement op vakliteratuur voor volgend jaar is al betaald", "Over te dragen kosten"),
            ("Commissielonen van november worden pas in januari ontvangen", "Verkregen opbrengsten"),
        ],
        "Eerst: kost of opbrengst? Dan: hoort het bij dit jaar of bij volgend jaar?",
        kolommen=["Over te dragen kosten", "Toe te rekenen kosten", "Over te dragen opbrengsten", "Verkregen opbrengsten"],
    )),
    mk(
        "Een verhuurder ontvangt op 1 november 3 000 euro huur voor zes maanden. Welk bedrag zet hij op 31 december op over te dragen opbrengsten?",
        ["2 000 euro", "1 000 euro", "3 000 euro", "500 euro"],
        0,
        "Per maand 500 euro. November en december horen bij dit jaar, januari tot april (4 maanden = 2 000 euro) bij volgend jaar.",
    ),
    mk(
        "Een lening loopt van 1 juli tot 30 juni. De jaarlijkse interest van 1 200 euro wordt op 30 juni betaald. Welk bedrag zet je op 31 december op toe te rekenen kosten?",
        ["600 euro", "1 200 euro", "300 euro", "900 euro"],
        0,
        "Van juli tot december is zes maanden interest al verlopen, maar nog niet betaald: 1 200 · 6/12 = 600 euro.",
    ),
    mk(
        "Een machine kost 60 000 euro, gaat 5 jaar mee zonder restwaarde en wordt op 1 april gekocht. Hoeveel is de afschrijving in het eerste boekjaar, pro rata?",
        ["9 000 euro", "12 000 euro", "3 000 euro", "15 000 euro"],
        0,
        "Per jaar 60 000 / 5 = 12 000 euro. Van april tot december is 9 maanden: 12 000 · 9/12 = 9 000 euro.",
    ),
    mk(
        "Een bestelwagen van 36 000 euro wordt lineair afgeschreven over 6 jaar. Wat is de boekwaarde na 4 volle jaren?",
        ["12 000 euro", "24 000 euro", "6 000 euro", "30 000 euro"],
        0,
        "Per jaar 6 000 euro. Na 4 jaar is 24 000 euro afgeschreven: 36 000 − 24 000 = 12 000 euro.",
    ),
    sorteer(
        "Je boekt de jaarlijkse afschrijving op een machine. Debet of credit?",
        ["Debet", "Credit"],
        [
            ["630 Afschrijvingen (kost)", "Debet"],
            ["Geboekte afschrijvingen op machines", "Credit"],
        ],
        "De afschrijving is een kost (debet). De waarde van de machine daalt via de rekening geboekte afschrijvingen (credit). Er gaat geen geld van de bank.",
    ),
    tabel(
        "Een handelaar heeft een beginvoorraad van 15 000 euro en telt op 31 december 11 000 euro. Welke uitspraken kloppen?",
        [
            ("De voorraad nam af met 4 000 euro.", J),
            ("De voorraadwijziging verhoogt de kosten van het jaar.", J),
            ("Je boekt 609 credit en de voorraad debet.", F),
            ("Er werd meer verkocht dan aangekocht.", J),
        ],
        "Een afname betekent dat er ook goederen uit de beginvoorraad verkocht zijn. 609 staat dan debet, de voorraad credit.",
    ),
    mk(
        "Aankopen handelsgoederen 70 000 euro, beginvoorraad 15 000 euro, eindvoorraad 11 000 euro. Hoeveel kostten de verkochte goederen?",
        ["74 000 euro", "66 000 euro", "70 000 euro", "96 000 euro"],
        0,
        "70 000 + 15 000 − 11 000 = 74 000 euro.",
    ),
    mk(
        "De kostprijs van de verkochte goederen is 52 000 euro. De aankopen waren 50 000 euro en de eindvoorraad 9 000 euro. Hoe groot was de beginvoorraad?",
        ["11 000 euro", "7 000 euro", "2 000 euro", "9 000 euro"],
        0,
        "Aankopen + beginvoorraad − eindvoorraad = 52 000. 50 000 + x − 9 000 = 52 000, dus x = 11 000 euro.",
    ),
    mk(
        "Een onderneming verwacht over drie jaar een groot onderhoud van 30 000 euro aan haar dak. Wat boekt ze dit jaar als ze elk jaar een even groot deel opzijzet?",
        [
            "Een voorziening van 10 000 euro: kost debet, voorziening credit",
            "Een afschrijving van 30 000 euro op het dak",
            "Niets, want de herstelling is nog niet gebeurd",
            "Een schuld van 30 000 euro aan de dakwerker",
        ],
        0,
        "Een voorziening spreidt een waarschijnlijke grote kost over de jaren waarin hij ontstaat. Het bedrag is nog niet zeker, dus het is geen schuld.",
    ),
    tabel(
        "Is het een voorziening, een schuld of een afschrijving?",
        [
            ("Een geschat bedrag voor een lopend geschil met een klant", "Voorziening"),
            ("De factuur van de dakwerker die al ontvangen is", "Schuld"),
            ("De waardevermindering van een computer door gebruik", "Afschrijving"),
        ],
        "Een voorziening is waarschijnlijk maar onzeker. Een schuld staat vast. Een afschrijving verdeelt de kost van een vast actief.",
        kolommen=["Voorziening", "Schuld", "Afschrijving"],
    ),
    mk(
        "Een kleine vennootschap heeft een winst voor belasting van 140 000 euro. Gegeven: 20 % op de eerste 100 000 euro, 25 % op de rest. Ze deed 22 000 euro voorafbetalingen. Hoeveel belasting moet ze nog betalen?",
        ["8 000 euro", "30 000 euro", "13 000 euro", "35 000 euro"],
        0,
        "Geraamde belasting 20 000 + 10 000 = 30 000 euro. Min 22 000 euro voorafbetalingen: 8 000 euro.",
    ),
    keuze(
        "De geraamde belasting boek je als een [[*kost|opbrengst|vordering]] in groep [[*67|70|17]], en het nog te betalen deel als een [[*schuld|voorziening|reserve]].",
        "Belastingen op het resultaat zijn een kost van het boekjaar. Wat nog niet betaald is, is een schuld aan de fiscus.",
    ),
    mk(
        "Winst na belasting 110 000 euro. De algemene vergadering beslist: 20 000 euro naar de reserves en 60 000 euro dividend. Wat gebeurt er met de rest?",
        [
            "30 000 euro wordt overgedragen naar volgend jaar",
            "30 000 euro wordt als kost geboekt",
            "30 000 euro gaat naar de fiscus",
            "Er blijft niets over, want het dividend is altijd de rest",
        ],
        0,
        "110 000 − 20 000 − 60 000 = 30 000 euro overgedragen winst.",
    ),
    tabel(
        "Waar of niet waar over de bestemming van het resultaat?",
        [
            ("Een dividend is een kost van de vennootschap.", F),
            ("Zolang het dividend niet uitbetaald is, is het een schuld aan de aandeelhouders.", J),
            ("Reserves verhogen het eigen vermogen.", J),
        ],
        "Een dividend is een verdeling van de winst, geen kost. Reserves blijven in de vennootschap en horen bij het eigen vermogen.",
    ),
    volgorde(
        "Zet de stappen op het einde van het boekjaar in de juiste volgorde.",
        [
            "De voorlopige saldibalans opmaken",
            "De inventaris opmaken en de eindejaarsboekingen doen",
            "De definitieve saldibalans opmaken",
            "De jaarrekening opstellen",
        ],
        "Eerst controleer je de boekingen van het jaar, dan pas je ze aan met de inventaris, en uit de definitieve saldibalans volgt de jaarrekening.",
    ),
    sorteer(
        "Gaat de rekening van de definitieve saldibalans naar de balans of naar de resultatenrekening?",
        ["Balans", "Resultatenrekening"],
        [
            ["Voorraad handelsgoederen", "Balans"],
            ["Afschrijvingen", "Resultatenrekening"],
            ["Over te dragen kosten", "Balans"],
            ["Verkopen handelsgoederen", "Resultatenrekening"],
            ["Voorzieningen voor risico's en kosten", "Balans"],
            ["Voorraadwijziging", "Resultatenrekening"],
        ],
        "Bezittingen, schulden en overlopende rekeningen staan op de balans. Kosten en opbrengsten op de resultatenrekening.",
    ),
    mk(
        "In de saldibalans is het totaal van de debetsaldi 4 000 euro groter dan het totaal van de creditsaldi. Wat besluit je?",
        [
            "Er zit een fout in de boekingen",
            "De onderneming maakte 4 000 euro winst",
            "De onderneming maakte 4 000 euro verlies",
            "Dat is normaal na de eindejaarsboekingen",
        ],
        0,
        "Bij dubbel boekhouden staat elk bedrag zowel debet als credit. De totalen moeten altijd gelijk zijn.",
    ),
    tabel(
        "Waar of niet waar over de proefbalans en de saldibalans?",
        [
            ("De proefbalans toont per rekening het totaal debet en het totaal credit.", J),
            ("De saldibalans toont per rekening enkel het saldo.", J),
            ("Een gelijke saldibalans bewijst dat elke boeking op de juiste rekening staat.", F),
        ],
        "Een boeking op de verkeerde rekening, aan de juiste kant, laat de totalen gelijk. De saldibalans vindt dus niet elke fout.",
    ),
    inv(
        "Een computer van 2 400 euro wordt lineair afgeschreven over 3 jaar, zonder restwaarde. Hoeveel euro is de jaarlijkse afschrijving? Schrijf enkel het getal.",
        "800",
        "2 400 / 3 = 800 euro per jaar.",
    ),
    mk(
        "Een lening van 50 000 euro wordt afgelost in vijf jaarlijkse schijven van 10 000 euro. Na twee aflossingen: wat boek je op 31 december?",
        [
            "10 000 euro van 17 naar 42",
            "30 000 euro van 17 naar 42",
            "10 000 euro van 42 naar 17",
            "Niets, want er is al afgelost",
        ],
        0,
        "Er blijft 30 000 euro over. De schijf van volgend jaar, 10 000 euro, gaat naar de schulden die binnen het jaar vervallen.",
    ),
    sleep(
        "Overlopende rekeningen passen het principe van de [[periodetoerekening]] toe: elke kost en opbrengst komt in het boekjaar waarin hij [[ontstaat]], los van het moment van [[betalen]].",
        ["voorzichtigheid", "factureren"],
        "Niet de betaling, maar de periode waarop een kost of opbrengst slaat, bepaalt het boekjaar.",
    ),
    koppel(
        "Welke eindejaarsverrichting hoort bij elke situatie?",
        [
            ["Een vrachtwagen verliest elk jaar waarde", "Afschrijving"],
            ["De voorraad op 31 december is kleiner dan op 1 januari", "Voorraadwijziging"],
            ["Een klant eist schadevergoeding, de uitspraak volgt later", "Voorziening"],
            ["De huur van januari is in december al betaald", "Overlopende rekening"],
        ],
        ["Btw-vereffening"],
        "Elke verrichting zorgt dat de jaarrekening een getrouw beeld geeft van het boekjaar.",
    ),
    mk(
        "Waarom boek je een afschrijving, als er toch geen geld van de rekening gaat?",
        [
            "Om de kost van de machine te spreiden over de jaren dat je ze gebruikt",
            "Om geld opzij te zetten op een spaarrekening voor een nieuwe machine",
            "Omdat de fiscus dat geld elk jaar int bij de onderneming, samen met de belastingen",
            "Om de btw op de machine terug te vorderen",
        ],
        0,
        "De machine werd één keer betaald, maar helpt jaren mee de omzet te maken. Elk jaar draagt zijn deel van de kost.",
    ),
    open_(
        "Leg uit waarom een stijging van de voorraad handelsgoederen de winst van het jaar verhoogt tegenover een jaar zonder voorraadwijziging.",
        "Een deel van wat dit jaar is aangekocht, is nog niet verkocht en ligt nog in het magazijn. Die goederen zijn geen kost van dit jaar. De voorraadwijziging trekt ze af van de kosten, waardoor de winst hoger uitvalt.",
        "Enkel wat verkocht is, hoort als kost bij de omzet van het jaar.",
    ),
    casus(
        "Handelszaak Vos bv sluit haar boekjaar af op 31 december. Gegevens: beginvoorraad 20 000 euro, eindvoorraad 26 000 euro; een machine van 48 000 euro, gekocht op 1 juli, 8 jaar zonder restwaarde; op 1 september werd 2 400 euro verzekering voor 12 maanden betaald.",
        [
            mk(
                "Welke voorraadwijziging boekt Vos?",
                [
                    "Een toename van 6 000 euro: voorraad debet, 609 credit",
                    "Een afname van 6 000 euro: 609 debet, voorraad credit",
                    "Een toename van 26 000 euro: voorraad debet, 609 credit",
                    "Een afname van 20 000 euro: 609 debet, voorraad credit",
                ],
                0,
                "26 000 − 20 000 = 6 000 euro meer voorraad: dat verlaagt de kosten.",
            ),
            mk(
                "Hoeveel is de afschrijving op de machine dit jaar?",
                ["3 000 euro", "6 000 euro", "1 500 euro", "4 000 euro"],
                0,
                "Per jaar 48 000 / 8 = 6 000 euro. Van juli tot december: 6/12, dus 3 000 euro.",
            ),
            mk(
                "Welk bedrag van de verzekering zet Vos op over te dragen kosten?",
                ["1 600 euro", "800 euro", "2 400 euro", "1 200 euro"],
                0,
                "Per maand 200 euro. September tot december (4 maanden) horen bij dit jaar, januari tot augustus (8 maanden = 1 600 euro) bij volgend jaar.",
            ),
        ],
    ),
]

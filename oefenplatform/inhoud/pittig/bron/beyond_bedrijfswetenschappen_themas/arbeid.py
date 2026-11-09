"""De arbeidsovereenkomst: begin, schorsing en einde — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import opzeg_zone

PRENTEN = [
    dict(bestand="opzegtermijnen.svg", zelf=True,
         wat="Tabel met de wettelijke opzegtermijnen volgens anciënniteit, bij opzegging door de werkgever en door de werknemer.",
         vragen="klikvragen en rekenvragen met de opzegtermijnen"),
]

VRAGEN = [
    klik(
        "Lies werkt 20 maanden bij haar werkgever. De werkgever zegt de overeenkomst op. Klik op de opzegtermijn die geldt.",
        "opzegtermijnen.svg",
        [opzeg_zone(8, 1)],
        "20 maanden valt in de rij 18 tot 21 maanden. De werkgever zegt op: 10 weken.",
    ),
    klik(
        "Omar werkt 3 jaar en 4 maanden bij dezelfde werkgever en vindt zelf een nieuwe job. Klik op de opzegtermijn die hij moet geven.",
        "opzegtermijnen.svg",
        [opzeg_zone(11, 2)],
        "3 jaar en 4 maanden valt in de rij 3 tot 4 jaar. De werknemer zegt op: 6 weken.",
    ),
    klik(
        "Een werknemer heeft een anciënniteit van 7 maanden. Klik op de rij die je moet aflezen.",
        "opzegtermijnen.svg",
        [opzeg_zone(4, 0)],
        "7 maanden ligt tussen 6 en 9 maanden.",
    ),
    met_prent("opzegtermijnen.svg", tabel(
        "Lees de opzegtermijn af.",
        [
            ("Anciënniteit 2 maanden, de werkgever zegt op", "1 week"),
            ("Anciënniteit 4 jaar en 2 maanden, de werkgever zegt op", "15 weken"),
            ("Anciënniteit 4 jaar en 2 maanden, de werknemer zegt op", "7 weken"),
            ("Anciënniteit 13 maanden, de werknemer zegt op", "4 weken"),
        ],
        "Zoek eerst de juiste rij (anciënniteit), dan de juiste kolom (wie zegt op).",
        kolommen=["1 week", "4 weken", "7 weken", "15 weken"],
    )),
    met_prent("opzegtermijnen.svg", mk(
        "Sam werkt 5 jaar en 3 maanden bij zijn werkgever. Hoeveel weken langer is de opzegtermijn als de werkgever opzegt dan als Sam zelf opzegt?",
        ["9 weken", "18 weken", "7 weken", "27 weken"],
        0,
        "Rij 5 tot 6 jaar: werkgever 18 weken, werknemer 9 weken. Het verschil is 9 weken.",
    )),
    met_prent("opzegtermijnen.svg", mk(
        "Een werkgever ontslaat een werknemer met 11 maanden anciënniteit, maar wil niet dat hij de opzegtermijn nog komt werken. Hij betaalt een verbrekingsvergoeding. Voor hoeveel weken loon?",
        ["7 weken", "3 weken", "11 weken", "Geen, want de werknemer werkt niet"],
        0,
        "De verbrekingsvergoeding is gelijk aan het loon van de opzegtermijn die niet gepresteerd wordt: rij 9 tot 12 maanden, werkgever, 7 weken.",
    )),
    tabel(
        "Is het een geldigheidsvereiste van een arbeidsovereenkomst?",
        [
            ("Beide partijen stemmen vrij in.", J),
            ("De partijen zijn bekwaam om een overeenkomst te sluiten.", J),
            ("Het werk is geoorloofd.", J),
            ("De werknemer heeft een diploma.", F),
            ("De overeenkomst wordt in een krant bekendgemaakt.", F),
        ],
        "Toestemming, bekwaamheid, een geoorloofd voorwerp en een geoorloofde oorzaak.",
    ),
    tabel(
        "Volgens welk criterium deel je de arbeidsovereenkomst zo in?",
        [
            ("Arbeider of bediende", "Aard"),
            ("Voltijds of deeltijds", "Omvang"),
            ("Onbepaalde tijd, bepaalde tijd of duidelijk omschreven werk", "Duur"),
        ],
        "Aard: hand- of hoofdarbeid. Omvang: hoeveel uren. Duur: hoe lang.",
        kolommen=["Aard", "Omvang", "Duur"],
    ),
    sorteer(
        "Ligt de oorzaak van de schorsing bij de werknemer of bij de werkgever?",
        ["Werknemer", "Werkgever"],
        [
            ["Ziekte", "Werknemer"],
            ["Geboorteverlof", "Werknemer"],
            ["Tijdskrediet", "Werknemer"],
            ["Economische werkloosheid", "Werkgever"],
            ["Werkloosheid wegens slecht weer", "Werkgever"],
            ["Technische stoornis", "Werkgever"],
        ],
        "Bij de werkgever ligt de oorzaak in het bedrijf: geen werk, slecht weer of een defect.",
    ),
    tabel(
        "Welke schorsing is het?",
        [
            ("Een kraan valt stil en de bouwvakkers kunnen die dag niet werken", "Technische stoornis"),
            ("Een overstroming maakt het bedrijf een week onbruikbaar", "Overmacht"),
            ("Een werkneemster zorgt een maand voor haar zwaar zieke moeder", "Zorgverlof"),
            ("Er zijn al weken te weinig bestellingen", "Economische werkloosheid"),
        ],
        "Telkens valt het werk tijdelijk stil, maar de overeenkomst blijft bestaan.",
        kolommen=["Technische stoornis", "Overmacht", "Zorgverlof", "Economische werkloosheid"],
    ),
    tabel(
        "Schorsing of einde van de arbeidsovereenkomst?",
        [
            ("Bevallingsverlof", "Schorsing"),
            ("Ontslag om dringende reden", "Einde"),
            ("Jaarlijkse vakantie", "Schorsing"),
            ("De afgesproken einddatum van een contract van bepaalde duur is bereikt", "Einde"),
            ("Voorlopige hechtenis", "Schorsing"),
            ("Overlijden van de werknemer", "Einde"),
        ],
        "Bij een schorsing blijft de overeenkomst bestaan. Bij een einde houdt ze op.",
        kolommen=["Schorsing", "Einde"],
    ),
    keuze(
        "Bij een staking leggen [[*de werknemers|de werkgevers|de vakbonden van de werkgevers]] het werk neer. Bij een lock-out sluit [[*de werkgever|de werknemer|de rechter]] de werknemers uit.",
        "Beide zijn een schorsing: er wordt niet gewerkt en er is geen loon.",
    ),
    mk(
        "Een arbeider is drie weken ziek. Wat klopt?",
        [
            "De werkgever betaalt eerst het loon, daarna neemt het ziekenfonds het over",
            "Het ziekenfonds betaalt meteen vanaf de eerste dag, de werkgever betaalt nooit iets",
            "De arbeidsovereenkomst eindigt automatisch na twee weken afwezigheid",
            "De werknemer krijgt geen geld omdat hij niet werkt",
        ],
        0,
        "Eerst is er gewaarborgd loon van de werkgever, daarna een uitkering van het ziekenfonds.",
    ),
    mk(
        "Het huis van een werknemer loopt onder water en hij moet dringend naar huis. Welke schorsing kan hij inroepen?",
        [
            "Verlof om dwingende redenen",
            "Klein verlet",
            "Economische werkloosheid",
            "Gewaarborgd dagloon",
        ],
        0,
        "Een onvoorziene, dringende gebeurtenis thuis vraagt zijn aanwezigheid. Dat verlof is in principe onbetaald.",
    ),
    tabel(
        "Waar of niet waar over de vorm van het contract?",
        [
            ("Een deeltijdse arbeidsovereenkomst moet schriftelijk zijn.", J),
            ("Een studentenovereenkomst mag mondeling blijven.", F),
            ("Een flexi-job is mogelijk voor wie elders al minstens 4/5 werkt.", J),
            ("Een student mag een onbeperkt aantal uren werken met verminderde sociale bijdragen.", F),
        ],
        "Deeltijds en student: schriftelijk. Studenten hebben een maximum aantal uren met verminderde bijdragen.",
    ),
    sleep(
        "Een arbeidsovereenkomst bestaat als iemand [[arbeid]] verricht tegen [[loon]] en onder het [[gezag]] van een werkgever.",
        ["winst", "aandelen"],
        "Die drie elementen samen maken er een arbeidsovereenkomst van.",
    ),
    mk(
        "Een werknemer steelt geld uit de kassa. De werkgever stuurt hem dezelfde dag weg. Wat is er met de opzegtermijn?",
        [
            "Er is geen opzegtermijn: dit is ontslag om dringende reden",
            "De werkgever moet de gewone opzegtermijn uit de tabel respecteren",
            "De werknemer krijgt een dubbele opzegtermijn als straf voor de werkgever",
            "De overeenkomst wordt geschorst tot de rechter beslist",
        ],
        0,
        "Een zware fout maakt elke verdere samenwerking onmogelijk. De overeenkomst eindigt meteen.",
    ),
    tabel(
        "Hoe eindigt de arbeidsovereenkomst hier?",
        [
            ("Werkgever en werknemer spreken samen een einddatum af", "Onderling akkoord"),
            ("Een tijdelijk contract loopt tot 30 juni en het is 30 juni", "Einde van de termijn"),
            ("Het huis waarvoor een metselaar werd aangenomen, is af", "Einde van het werk"),
            ("De werkgever geeft ontslag met een opzegtermijn van 8 weken", "Opzegging"),
        ],
        "Er zijn verschillende manieren waarop een arbeidsovereenkomst eindigt.",
        kolommen=["Onderling akkoord", "Einde van de termijn", "Einde van het werk", "Opzegging"],
    ),
    koppel(
        "Koppel de soort arbeidsovereenkomst aan het voorbeeld.",
        [
            ["Bepaalde tijd", "Een contract van 1 maart tot 31 augustus"],
            ["Duidelijk omschreven werk", "Een contract tot de nieuwe keuken geplaatst is"],
            ["Vervangingsovereenkomst", "Een contract zolang een collega in bevallingsverlof is"],
            ["Onbepaalde tijd", "Een contract zonder einddatum"],
        ],
        ["Een contract van één dag per jaar"],
        "Het verschil zit in hoe het einde vastligt: een datum, een taak, een terugkeer of niets.",
    ),
    mk(
        "Een werknemer wordt verkozen als gemeenteraadslid en neemt af en toe een dag vrij om vergaderingen voor te bereiden. Welke schorsing?",
        ["Politiek mandaat", "Klein verlet", "Tijdskrediet", "Zorgverlof"],
        0,
        "De uitoefening van een politiek ambt is een aparte schorsingsgrond.",
    ),
    mk(
        "Wat is het verschil tussen zorgverlof en tijdskrediet?",
        [
            "Zorgverlof dient om een familielid te verzorgen, tijdskrediet kan ook om andere redenen",
            "Zorgverlof is altijd betaald door de werkgever, tijdskrediet nooit",
            "Tijdskrediet beëindigt de overeenkomst, zorgverlof schorst ze",
            "Er is geen verschil: het zijn twee namen voor hetzelfde",
        ],
        0,
        "Beide zijn schorsingen. Zorgverlof heeft een bepaalde reden, tijdskrediet is ruimer.",
    ),
    inv(
        "Hoe noemt men de duur dat een werknemer al ononderbroken bij dezelfde werkgever werkt?",
        "anciënniteit",
        "De anciënniteit bepaalt de lengte van de opzegtermijn.",
    ),
    mk(
        "Een werkgever ontslaat een werknemer met 2 jaar en 6 maanden anciënniteit. Wat is de verbrekingsvergoeding als het weekloon 900 euro is en de werknemer meteen moet stoppen?",
        ["10 800 euro", "5 400 euro", "11 700 euro", "2 250 euro"],
        0,
        "Rij 2 tot 3 jaar, werkgever: 12 weken. 12 × 900 = 10 800 euro.",
    ),
    tabel(
        "Waar of niet waar over de opzegtermijn?",
        [
            ("Hoe langer iemand ergens werkt, hoe langer de opzegtermijn.", J),
            ("De opzegtermijn hangt af van het loon van de werknemer.", F),
            ("Tijdens de opzegtermijn blijft de werknemer gewoon werken en loon krijgen.", J),
            ("Bij een contract van bepaalde duur moet je op de einddatum nog een opzegtermijn geven.", F),
        ],
        "De duur hangt af van de anciënniteit en van wie opzegt. Een contract van bepaalde duur eindigt vanzelf.",
    ),
    mk(
        "Een gepensioneerde kok wil 's avonds bijspringen in een restaurant. Welke formule past het best?",
        ["Een flexi-job", "Een studentenovereenkomst", "Een vervangingsovereenkomst", "Tijdskrediet"],
        0,
        "Gepensioneerden mogen een flexi-job doen in de sectoren waar dat toegelaten is.",
    ),
    mk(
        "Bij welke gebeurtenis heeft een werknemer recht op klein verlet?",
        ["Het huwelijk van zijn dochter", "Een tandartsbezoek", "Een dag zonder bestellingen", "Een staking"],
        0,
        "Klein verlet is afwezigheid met behoud van loon bij bepaalde familiegebeurtenissen.",
    ),
    open_(
        "Leg uit waarom de opzegtermijn langer is als de werkgever opzegt dan als de werknemer opzegt.",
        "De werknemer verliest zijn inkomen en heeft tijd nodig om een nieuwe job te zoeken. De werkgever kan meestal sneller iemand anders vinden. Daarom beschermt de wet de werknemer met een langere termijn.",
        "Het sociaal recht beschermt de zwakkere partij.",
    ),
    casus(
        "Nina werkt sinds 1 februari 2024 voltijds als bediende bij een drukkerij, met een contract van onbepaalde tijd. Op 1 november 2026 krijgt ze een brief: de drukkerij zegt de overeenkomst op. Gebruik de tabel met opzegtermijnen.",
        [
            met_prent("opzegtermijnen.svg", mk(
                "Hoeveel is Nina's anciënniteit op 1 november 2026?",
                ["2 jaar en 9 maanden", "2 jaar en 3 maanden", "3 jaar en 1 maand", "1 jaar en 9 maanden"],
                0,
                "Van 1 februari 2024 tot 1 november 2026: 2 jaar en 9 maanden.",
            )),
            met_prent("opzegtermijnen.svg", mk(
                "Welke opzegtermijn moet de drukkerij geven?",
                ["12 weken", "6 weken", "13 weken", "11 weken"],
                0,
                "Rij 2 tot 3 jaar, kolom werkgever: 12 weken.",
            )),
            tabel(
                "Nina wordt tijdens haar opzegtermijn twee weken ziek. Wat klopt?",
                [
                    ("Nina bezorgt haar werkgever een doktersattest.", J),
                    ("Nina moet eerst al haar vakantiedagen opnemen.", F),
                    ("Nina mag zelf een nieuwe opzegtermijn kiezen omdat ze ziek is.", F),
                ],
                "Met een attest kan de werkgever de afwezigheid nagaan. Vakantie en ziekte zijn twee verschillende dingen.",
            ),
        ],
    ),
]

"""Economisch onderzoek: onderzoeksvraag, methode en besluit — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, GROEN, LICHT

# De onderzoekscyclus: vijf genummerde fasen zonder namen (eigen tekening).
FX, FY, FB, FH, STAP = 40, 250, 150, 130, 190


def _cyclus():
    d = [s_tekst(500, 90, "De vijf fasen van de onderzoekscyclus", 26, vet=True),
         '<defs><marker id="pijl" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto">'
         f'<path d="M0,0 L14,7 L0,14 z" fill="{GROEN}"/></marker></defs>']
    for i in range(5):
        x = FX + i * STAP
        d.append(s_vak(x, FY, FB, FH, vul=LICHT, rand=GROEN, dikte=3, rond=20))
        d.append(s_tekst(x + FB / 2, FY + FH / 2 + 8, f"fase {i + 1}", 26, kleur=GROEN, vet=True))
        if i < 4:
            d.append(f'<line x1="{x + FB + 4}" y1="{FY + FH / 2}" x2="{x + STAP - 8}" y2="{FY + FH / 2}" '
                     f'stroke="{GROEN}" stroke-width="4" marker-end="url(#pijl)"/>')
    return d


def fase(i):
    return pix_zone(FX + i * STAP + 4, FY + 4, FB - 8, FH - 8)


GRAFIEKEN = [dict(naam="onderzoek-cyclus", titel="", eigen=_cyclus)]
PRENTEN = [dict(bestand="onderzoek-cyclus.svg", zelf=True, wat="Vijf genummerde fasen van de onderzoekscyclus", vragen="klikvragen over de fasen")]
P = "onderzoek-cyclus.svg"

VRAGEN = [
    klik(
        "In welke fase kies je je methode en maak je een planning? Klik erop.",
        P, [fase(1)],
        "Fase 2, voorbereiden: na het oriënteren kies je hoe je de vraag zal onderzoeken.",
    ),
    klik(
        "In welke fase kijk je terug op wat goed ging en wat beter kan? Klik erop.",
        P, [fase(4)],
        "Fase 5, reflecteren: de laatste fase van de cyclus.",
    ),
    klik(
        "In welke fase verzamel en verwerk je de gegevens? Klik erop.",
        P, [fase(2)],
        "Fase 3, uitvoeren: na het oriënteren en het voorbereiden.",
    ),
    met_prent(P, mk(
        "Wat doe je in fase 1?",
        ["Je verkent het onderwerp en formuleert je onderzoeksvraag", "Je verwerkt je resultaten in een verslag of een presentatie",
         "Je verzamelt cijfers bij Statbel en de Nationale Bank", "Je trekt een besluit en schrijft de beperkingen erbij"],
        0,
        "Fase 1 is oriënteren.",
    )),
    tabel(
        "Aan welke eis voor een goede onderzoeksvraag voldoet deze vraag niet?",
        [
            ("Is de jeugdwerkloosheid gestegen?", "Open"),
            ("Waarom is de btw op energie veel te hoog?", "Objectief"),
            ("Hoe evolueerde de inflatie en waarom stegen de lonen?", "Enkelvoudig"),
            ("Wat zou de werkloosheid zijn als de euro nooit had bestaan?", "Onderzoekbaar"),
        ],
        "Ja of nee: niet open. 'Veel te hoog': een mening. Twee vragen: niet enkelvoudig. Geen gegevens mogelijk: niet onderzoekbaar.",
        kolommen=["Open", "Objectief", "Enkelvoudig", "Onderzoekbaar"],
    ),
    mk(
        "Welke onderzoeksvraag is het best?",
        ["Hoe evolueerde het aantal faillissementen in Limburg sinds 2020?",
         "Zijn er in Limburg meer faillissementen dan vroeger?",
         "Waarom gaan er in Limburg veel te veel bedrijven failliet?",
         "Hoe evolueerden de faillissementen en waarom stegen de huurprijzen?"],
        0,
        "Open, objectief, enkelvoudig, onderzoekbaar en haalbaar.",
    ),
    mk(
        "Een leerling wil alle bedrijven van Europa bevragen voor zijn taak van drie weken. Aan welke eis voldoet zijn plan niet?",
        ["Haalbaar", "Open", "Objectief", "Enkelvoudig"],
        0,
        "Met de tijd en middelen van een leerling is dat niet te doen.",
    ),
    tabel(
        "Kwantitatief of kwalitatief onderzoek?",
        [
            ("500 jongeren bevragen over hoeveel zakgeld ze krijgen", "Kwantitatief"),
            ("Met vijf jongeren diepgaand praten over waarom ze een bijbaan kozen", "Kwalitatief"),
            ("Cijfers over de werkloosheid per provincie vergelijken", "Kwantitatief"),
        ],
        "Kwantitatief: met cijfers, vaak bij veel mensen. Kwalitatief: het waarom, diepgaand bij weinig mensen.",
        kolommen=["Kwantitatief", "Kwalitatief"],
    ),
    tabel(
        "Welke methode is dit?",
        [
            ("Cijfers opzoeken bij Statbel en de Nationale Bank", "Deskresearch"),
            ("Elke deelnemer krijgt dezelfde vragen op papier", "Enquête"),
            ("Een diepgaand gesprek met een ondernemer", "Interview"),
            ("Een week lang klanten tellen aan de zelfscankassa", "Observatie"),
            ("De prijs aanpassen in de helft van de filialen en vergelijken", "Experiment"),
        ],
        "Deskresearch gebruikt bestaande gegevens; de andere vier zijn fieldresearch.",
        kolommen=["Deskresearch", "Enquête", "Interview", "Observatie", "Experiment"],
    ),
    sorteer(
        "Deskresearch of fieldresearch?",
        ["Deskresearch", "Fieldresearch"],
        [
            ["Literatuuronderzoek in de bibliotheek", "Deskresearch"],
            ["Een enquête bij klanten", "Fieldresearch"],
            ["Bestaande cijfers van de Nationale Bank gebruiken", "Deskresearch"],
            ["Een experiment in een winkel", "Fieldresearch"],
        ],
        "Deskresearch: bestaande gegevens opzoeken. Fieldresearch: zelf nieuwe gegevens verzamelen.",
    ),
    mk(
        "Je wilt weten hoe duizenden Belgische jongeren hun zakgeld besteden. Welke methode is het minst geschikt?",
        ["Een interview", "Een enquête", "Deskresearch", "Een combinatie van enquête en deskresearch"],
        0,
        "Een interview is diepgaand en geschikt voor weinig mensen, niet om duizenden te bevragen.",
    ),
    mk(
        "Wat is er mis met de enquêtevraag 'Vind jij ook dat de prijzen te hoog zijn?'",
        ["Het is een gesuggereerde vraag: ze stuurt het antwoord", "Ze is te open: je kan er onmogelijk kort op antwoorden",
         "Ze hoort bij deskresearch, niet bij een enquête op papier", "Er is niets mis mee, want ze is kort en duidelijk"],
        0,
        "Zo'n vraag maakt een enquête minder objectief.",
    ),
    casus(
        "Lena onderzoekt of Limburgse jongeren meer sparen dan vroeger. Ze bevraagt de 24 leerlingen van haar eigen klas.",
        [
            mk("Wat is de populatie in haar onderzoek?", ["Alle Limburgse jongeren", "De 24 leerlingen van haar klas",
                                                         "Alle Belgen", "De leerkrachten van haar school"], 0,
               "De populatie is de hele groep waarover je iets wil weten."),
            mk("Wat is de steekproef?", ["De 24 leerlingen van haar klas", "Alle Limburgse jongeren van haar leeftijd", "Alle middelbare scholen in Limburg", "Haar onderzoeksvraag over sparen"], 0,
               "De steekproef is het deel van de populatie dat je bevraagt."),
            mk("Is haar steekproef representatief?",
               ["Nee: één klas is geen goede afspiegeling van alle Limburgse jongeren", "Ja: 24 leerlingen is genoeg voor elk onderzoek over jongeren",
                "Ja: alle leerlingen in haar klas zijn Limburgse jongeren", "Nee: ze had ook alle leerkrachten van de school moeten bevragen"], 0,
               "Een representatieve steekproef is een goede afspiegeling van de populatie."),
        ],
    ),
    mk(
        "Een onderzoeker kijkt of de hoogte van de huurprijs invloed heeft op het aantal studenten dat op kot gaat. Wat is de afhankelijke variabele?",
        ["Het aantal studenten dat op kot gaat", "De hoogte van de huurprijs", "De stad waar de studenten studeren en wonen", "De onderzoeker zelf"],
        0,
        "Het aantal studenten hangt (misschien) af van de huurprijs. De huurprijs is de onafhankelijke variabele.",
    ),
    mk(
        "In de zomer stijgen de verkoop van ijsjes en het aantal verkochte zonnebrandflessen samen. Wat besluit je?",
        ["Het ene veroorzaakt het andere niet: samen stijgen bewijst geen oorzaak", "Wie een ijsje koopt, koopt daarna ook meer zonnebrand voor op het strand",
         "Wie zonnebrand koopt, krijgt daardoor ook meer zin in een ijsje bij het zwembad", "De twee variabelen zijn eigenlijk één en dezelfde variabele, met twee namen"],
        0,
        "Als twee variabelen samen stijgen, bewijst dat niet dat de ene de oorzaak is van de andere.",
    ),
    tabel(
        "Waar of niet waar over het besluit en de bronnen?",
        [
            ("In het besluit staat een antwoord op de onderzoeksvraag.", J),
            ("In het besluit vermeld je ook de beperkingen van het onderzoek.", J),
            ("Bronnen vermelden is enkel nodig als je letterlijk citeert.", F),
            ("Een besluit zonder beperkingen is altijd het sterkste besluit.", F),
        ],
        "Bronnen vermeld je altijd, zodat de lezer je gegevens kan nakijken en ziet wat van anderen komt.",
    ),
    mk(
        "Wat staat er in het besluit van een onderzoek?",
        ["Een antwoord op de onderzoeksvraag en de beperkingen van het onderzoek", "Enkel de onderzoeksvraag, nog eens herhaald in andere woorden",
         "De ruwe gegevens van alle deelnemers aan de enquête, in een grote tabel", "Een nieuwe onderzoeksvraag voor een volgend onderzoek over hetzelfde"],
        0,
        "Het besluit beantwoordt de vraag en zegt eerlijk waar het onderzoek tekortschiet.",
    ),
    keuze(
        "Een variabele is een kenmerk dat [[*verschillende waarden|maar één waarde]] kan aannemen. Je kan kwantitatief en kwalitatief onderzoek [[*combineren|nooit combineren]] in één onderzoek.",
        "Cijfers en het waarom vullen elkaar aan.",
    ),
    sleep(
        "Een onderzoeksvraag is [[relevant]] als ze nuttige kennis oplevert voor een bepaalde doelgroep, en [[haalbaar]] als je ze kan beantwoorden met de tijd en middelen die je hebt.",
        ["gesloten", "subjectief"],
        "Samen met open, objectief, enkelvoudig en onderzoekbaar: zes eisen.",
    ),
    open_(
        "Formuleer een goede onderzoeksvraag over de prijs van busabonnementen voor jongeren, en leg uit waarom ze voldoet aan de eisen open, objectief en enkelvoudig.",
        "Bijvoorbeeld: Hoe evolueerde de prijs van een busabonnement voor jongeren in Vlaanderen sinds 2020? Ze is open (niet met ja of nee te beantwoorden), objectief (er zit geen mening in) en enkelvoudig (één vraag).",
    ),
    sorteer(
        "Is dit een eis voor een goede onderzoeksvraag?",
        ["Wel een eis", "Geen eis"],
        [
            ["Onderzoekbaar", "Wel een eis"],
            ["Enkelvoudig", "Wel een eis"],
            ["Met ja of nee te beantwoorden", "Geen eis"],
            ["Met je eigen mening erin", "Geen eis"],
        ],
        "Een goede vraag is open, objectief, enkelvoudig, onderzoekbaar, haalbaar en relevant.",
    ),
    tabel(
        "Welke methode past het best bij deze onderzoeksvraag?",
        [
            ("Hoeveel klanten kiezen voor de zelfscankassa?", "Observatie"),
            ("Waarom kiezen jongeren voor een bijbaan in de horeca?", "Interview"),
            ("Verkoopt een winkel meer als de prijs met 10 % daalt?", "Experiment"),
        ],
        "Kijken naar gedrag: observatie. Het waarom: interview. Eén ding veranderen en vergelijken: experiment.",
        kolommen=["Observatie", "Interview", "Experiment"],
    ),
    mk(
        "Je wil weten hoe tevreden de klanten van een supermarktketen in heel Vlaanderen zijn. Welke steekproef is het meest representatief?",
        ["Klanten van filialen in alle Vlaamse provincies, op verschillende dagen en uren",
         "Alle klanten van één filiaal op zaterdagochtend, omdat het dan het drukst is in de winkel",
         "Je eigen familie en vrienden, omdat die zeker eerlijk antwoorden op al je vragen",
         "Enkel de klanten die het voorbije jaar zelf een klacht indienden bij de klantendienst"],
        0,
        "Een representatieve steekproef is een goede afspiegeling van de hele populatie.",
    ),
    mk(
        "Een onderzoeker bevraagt 10 mensen in Hasselt en besluit dat alle Belgen meer sparen. Wat is het probleem?",
        ["De steekproef is te klein en niet representatief voor heel België", "Hij had een experiment moeten doen in plaats van mensen te bevragen",
         "Sparen kan je met geen enkele methode onderzoeken", "Hij had eerst deskresearch moeten doen in de bibliotheek van Hasselt"],
        0,
        "Uit 10 mensen kan je geen besluit trekken over heel België.",
    ),
    koppel(
        "Koppel elke eis aan haar betekenis.",
        [
            ["Open", "Niet te beantwoorden met ja of nee"],
            ["Objectief", "Geen mening in de vraag"],
            ["Haalbaar", "Te beantwoorden met de tijd en middelen die je hebt"],
            ["Relevant", "Levert nuttige kennis op voor een doelgroep"],
        ],
        ["Zo kort mogelijk, met minder dan tien woorden"],
        "Een goede onderzoeksvraag moet niet per se kort zijn.",
    ),
    mk(
        "Wat is het verschil tussen een enquête en een interview?",
        ["Bij een enquête krijgt elke deelnemer dezelfde vragen; een interview is een diepgaand gesprek",
         "Een enquête is deskresearch met bestaande cijfers, een interview is fieldresearch",
         "Een interview is net geschikt om duizenden mensen tegelijk te bevragen, een enquête niet",
         "Er is geen verschil: het zijn twee woorden voor exact dezelfde onderzoeksmethode"],
        0,
        "Beide zijn fieldresearch. Een interview is goed voor het waarom, bij weinig mensen.",
    ),
    tabel(
        "Waar of niet waar over onderzoeksmethodes?",
        [
            ("Een observatie werkt zonder vragen te stellen.", J),
            ("Deskresearch gebruikt bestaande gegevens.", J),
            ("Bij een experiment verander je zoveel mogelijk dingen tegelijk.", F),
            ("Kwalitatief onderzoek gebeurt meestal bij heel veel mensen.", F),
        ],
        "Bij een experiment verander je één ding en vergelijk je. Kwalitatief onderzoek gaat diep bij weinig mensen.",
    ),
    mk(
        "Je verwerkt je resultaten in een verslag en een presentatie voor de klas. In welke fase van de onderzoekscyclus zit je?",
        ["Rapporteren", "Oriënteren", "Voorbereiden", "Reflecteren"],
        0,
        "Na het uitvoeren rapporteer je; daarna kijk je nog terug in het reflecteren.",
    ),
]

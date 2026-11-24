"""Een Engelse tekst analyseren — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "(1) Many British schools have banned mobile phones during the school day. "
    "(2) Supporters say the ban helps pupils concentrate and reduces bullying. "
    "(3) However, a study of 1,200 pupils found that their marks did not improve after the ban. "
    "(4) The researchers did notice that pupils talked to each other more during breaks. "
    "(5) Some parents, on the other hand, complain that they can no longer reach their children. "
    "(6) The authors therefore conclude that a ban is not a magic solution, although it may make breaks more social."
)

TEKST2 = (
    "Read the text.\n\n"
    "Dear Mr Patel,\n"
    "I am writing to complain about the bicycle I bought in your shop on 3 March. "
    "After only two weeks, the brakes stopped working. I returned to the shop, where one of your staff told me that "
    "the repair would cost £60. As the bike is still under guarantee, I believe it should be repaired free of charge. "
    "Unless I hear from you within ten days, I will contact a consumer organisation. "
    "I would be grateful if you could reply by email.\n"
    "Yours sincerely,\nEmma Clarke"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Wat is de hoofdgedachte van de tekst?",
                [
                    "Een gsm-verbod is geen wondermiddel",
                    "Een gsm-verbod zorgt op school voor betere punten",
                    "Ouders zijn het helemaal niet eens met het verbod",
                    "Pesten verdwijnt volledig door een gsm-verbod",
                ],
                0,
                "Zin 6 vat de tekst samen, met het signaalwoord therefore.",
            ),
            mk(
                "Welk verband legt however in zin 3?",
                ["Een tegenstelling", "Een gevolg ervan", "Een voorbeeld ervan", "Een opsomming"],
                0,
                "Zin 2 zegt wat voorstanders verwachten, zin 3 zegt dat het niet zo uitdraait.",
            ),
            tabel(
                "Staat dit in de tekst (over het lezen)?",
                [
                    ("De punten van de leerlingen stegen na het verbod.", F),
                    ("Leerlingen praatten meer met elkaar tijdens de pauze.", J),
                    ("Sommige ouders kunnen hun kind niet meer bereiken.", J),
                    ("Alle Britse scholen hebben een gsm-verbod.", F),
                ],
                "Many schools is niet all schools.",
            ),
            inv(
                "Hoeveel leerlingen deden mee aan het onderzoek? Schrijf het getal.",
                ["1200", "1.200", "1 200", "1,200"],
                "A study of 1,200 pupils: in het Engels staat er een komma tussen de duizendtallen.",
            ),
            keuze(
                "Volgens de laatste zin [[*kan|moet]] een verbod de pauzes socialer maken.",
                "May drukt een mogelijkheid uit, geen zekerheid.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Wat wil Emma met deze brief bereiken?",
                [
                    "Dat haar fiets gratis hersteld wordt",
                    "Dat ze haar geld helemaal terugkrijgt",
                    "Dat de winkel een nieuwe fiets opstuurt",
                    "Dat de verkoper zich verontschuldigt",
                ],
                0,
                "It should be repaired free of charge.",
            ),
            inv(
                "Binnen hoeveel dagen wil Emma een antwoord krijgen? Schrijf het getal.",
                ["10", "tien"],
                "Unless I hear from you within ten days.",
            ),
            mk(
                "Wat doet Emma als ze geen antwoord krijgt?",
                [
                    "Ze stapt naar een consumentenorganisatie",
                    "Ze betaalt dan toch maar de £60 voor de herstelling",
                    "Ze brengt de fiets naar een andere winkel",
                    "Ze schrijft een slechte review over de winkel",
                ],
                0,
                "Unless betekent tenzij: zonder antwoord volgt die stap.",
            ),
            keuze(
                "Het woord it in de zin over de garantie verwijst naar [[*de fiets|de herstelling]].",
                "As the bike is still under guarantee, I believe it should be repaired.",
            ),
            mk(
                "Welk soort tekst is dit?",
                ["Een formele klachtenbrief", "Een informele mail aan een vriend", "Een advertentie", "Een krantenartikel"],
                0,
                "Dear Mr …, I am writing to complain en Yours sincerely zijn vaste formules.",
            ),
        ],
    ),
    mk(
        "Lees: « Despite the heavy rain, the match went ahead. » Wat gebeurde er met de wedstrijd?",
        ["Ze ging door", "Ze werd uitgesteld", "Ze werd stilgelegd", "Ze werd afgelast"],
        0,
        "Despite betekent ondanks; to go ahead is doorgaan.",
    ),
    mk(
        "Lees: « Tickets are non-refundable unless the event is cancelled. » Wanneer krijg je je geld terug?",
        ["Als het evenement niet doorgaat", "Als je zelf niet kan komen opdagen", "Altijd binnen een termijn van veertien dagen", "In geen enkel geval"],
        0,
        "Unless geeft de enige uitzondering.",
    ),
    mk(
        "Lees: « Tom and his sister both play the piano, but only the latter takes lessons. » Wie volgt les?",
        ["De zus van Tom", "Tom", "Allebei", "Geen van beiden"],
        0,
        "The latter is het laatste van de twee genoemde.",
    ),
    mk(
        "Lees: « The new law, which came into force last year, has hardly changed anything. » Wat zegt de zin over de wet?",
        ["Ze heeft bijna niets veranderd", "Ze heeft heel veel hard veranderd", "Ze is nog altijd niet van kracht", "Ze was erg moeilijk om te maken"],
        0,
        "Hardly betekent nauwelijks, niet hard.",
    ),
    keuze(
        "Lees: « You needn't bring food; lunch is provided. » Eten meebrengen is [[*niet nodig|verboden]].",
        "Needn't betekent hoeft niet; mustn't zou verboden zijn.",
    ),
    keuze(
        "Lees: « He must have missed the bus. » De spreker is [[*vrij zeker|helemaal niet zeker]] dat hij de bus miste.",
        "Must have plus voltooid deelwoord is een sterke conclusie over het verleden.",
    ),
    tabel(
        "Welk verband legt dit signaalwoord?",
        [
            ("nevertheless", "Tegenstelling"),
            ("consequently", "Gevolg"),
            ("for instance", "Voorbeeld"),
            ("moreover", "Opsomming"),
        ],
        "Moreover voegt een extra argument toe, net als in addition.",
        kolommen=["Tegenstelling", "Gevolg", "Voorbeeld", "Opsomming"],
    ),
    sorteer(
        "Hoe sterk is deze uitspraak?",
        ["Zeker", "Mogelijk"],
        [
            ("The price will rise.", "Zeker"),
            ("The price might rise.", "Mogelijk"),
            ("The price could rise.", "Mogelijk"),
            ("The price is rising.", "Zeker"),
        ],
        "Might en could laten ruimte; will en een gewone tijd niet.",
    ),
    koppel(
        "Koppel elk Engels woord aan zijn betekenis (over het lezen).",
        [
            ("owing to", "wegens"),
            ("whereas", "terwijl, daarentegen"),
            ("unless", "tenzij"),
            ("although", "hoewel"),
        ],
        ["daarom"],
        "Deze woordjes sturen hoe je de rest van de zin leest.",
    ),
    mk(
        "Lees: « Not every student who failed the test had skipped classes. » Wat volgt hieruit?",
        ["Niet alle gebuisden spijbelden", "Alle gebuisde leerlingen hadden lessen gemist", "Geen enkele leerling was gebuisd voor de toets", "Wie lessen miste, slaagde toch voor de toets"],
        0,
        "Not every betekent niet allemaal: er zijn uitzonderingen.",
    ),
    mk(
        "Lees: « The flight was delayed. This meant we missed our connection. » Waar verwijst this naar?",
        ["Naar de vertraging", "Naar de aansluitende vlucht", "Naar de drukke luchthaven", "Naar de andere passagiers"],
        0,
        "This vat de vorige zin samen.",
    ),
    mk(
        "Lees: « The cheaper of the two offers is not necessarily the better one. » Wat zegt de schrijver?",
        ["Goedkoper is niet altijd beter", "Het goedkoopste aanbod is altijd het slechtste", "Beide aanbiedingen zijn precies even duur", "Het duurste aanbod is zonder twijfel beter"],
        0,
        "Not necessarily betekent niet noodzakelijk.",
    ),
    inv(
        "Lees: « Applications must reach us no later than 15 May. » Wat is de laatste dag om in te dienen? Schrijf de dag en de maand in cijfers, bv. 1/1.",
        ["15/5", "15 mei", "15/05", "15-5", "15 May"],
        "No later than betekent ten laatste.",
    ),
    tabel(
        "Klopt dit over lezen in het Engels?",
        [
            ("De titel en de tussentitels helpen je het onderwerp te vinden.", J),
            ("Een voorbeeld in de tekst is meestal een hoofdpunt.", F),
            ("Een woord als therefore kondigt vaak een conclusie aan.", J),
            ("Je antwoord mag ingaan tegen wat in de tekst staat als je het beter weet.", F),
        ],
        "Je antwoord komt altijd uit de tekst.",
    ),
    mk(
        "Lees: « She was unable to attend. » Hoe leid je de betekenis van unable af?",
        ["Uit un- plus able: niet in staat", "Uit un, het Franse woord voor één", "Uit het woord table zonder de letter t", "Uit unity, dat eenheid betekent"],
        0,
        "Un- maakt een woord ontkennend.",
    ),
    mk(
        "Lees: « Hardly anyone turned up for the meeting. » Hoeveel mensen kwamen er?",
        ["Bijna niemand", "Heel veel mensen", "Iedereen die uitgenodigd was", "Precies de helft van de leden"],
        0,
        "Hardly anyone betekent bijna niemand.",
    ),
    keuze(
        "Lees: « Visitors are required to sign in at reception. » Inschrijven aan het onthaal is [[*verplicht|vrijblijvend]].",
        "To be required to betekent verplicht zijn om.",
    ),
    volgorde(
        "Zet de stappen van een goede leesaanpak in de juiste volgorde.",
        ["titel en beeld bekijken", "de vraag lezen", "de tekst globaal lezen", "het antwoord gericht opzoeken", "het antwoord nakijken in de tekst"],
        "Eerst oriënteren, dan gericht zoeken.",
    ),
    sleep(
        "In « the former and the latter » verwijst [[former]] naar het eerste en [[latter]] naar het tweede. Het woord [[however]] kondigt een tegenstelling aan.",
        ["therefore", "unless"],
        "Verwijswoorden en signaalwoorden dragen de samenhang.",
    ),
    open_(
        "Lees: « Although tourism brings money to the island, it also puts pressure on its water supply. » Leg in het Nederlands uit wat de schrijver zegt.",
        "Toerisme brengt geld op voor het eiland, maar het zorgt ook voor druk op de watervoorraad. Although geeft eerst het voordeel toe en zet daar het nadeel tegenover.",
    ),
]

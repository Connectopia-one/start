"""Geloof, kunst en macht in de middeleeuwen — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="bogen.svg", zelf=True,
         wat="Twee bogen naast elkaar zonder naam: A met een punt bovenaan, B rond.",
         vragen="klikvraag: welke boog leidt het gewicht steiler naar beneden"),
    dict(bestand="wereldkaart-middeleeuwen.svg", zelf=True,
         wat="Schema van een middeleeuwse wereldkaart: een cirkel met een T van water, A in het midden, B in de bovenste helft, C en D onderaan.",
         vragen="invulvraag op A en tabelvraag over de kaart"),
    dict(bestand="tijdlijn-1000-1500.svg", zelf=True,
         wat="Tijdlijn van 1000 tot 1500 (dezelfde als bij Standen, domein en stad).",
         vragen="klikvragen op 1215 en 1291"),
    dict(bestand="lam-gods.webp", zelf=False,
         wat="Het Lam Gods van Jan en Hubert van Eyck (1432), Sint-Baafskathedraal Gent, het middenpaneel of het geopende retabel.",
         waar="Wikimedia Commons, zoek op 'Ghent Altarpiece' (publiek domein; de foto's van KIK-IRPA closertovaneyck zijn vrij te gebruiken).",
         vragen="tabelvraag over de Vlaamse primitieven"),
]

TL = "tijdlijn-1000-1500.svg"
KAART = "/examenvormen/geschiedenis-boost/wereldkaart-middeleeuwen.svg"

VRAGEN = [
    # --- bekering en Kerk
    mk(
        "Hoe verspreidden missionarissen het christendom over West-Europa?",
        [
            "Ze bekeerden eerst de vorst, en daarna volgde zijn volk",
            "Ze bekeerden eerst de boeren, die daarna hun heer overtuigden",
            "Ze lieten elk dorp zelf stemmen over het nieuwe geloof",
            "Ze bouwden eerst scholen, en pas eeuwen later kerken",
        ],
        0,
        "Bekeerde je de koning, dan volgde zijn hofhouding en daarna zijn onderdanen.",
    ),
    tabel(
        "Oude gewoonten en het christendom gingen vaak samen. Klopt elke uitspraak?",
        [
            ("Een midwinterfeest kreeg een christelijke betekenis.", J),
            ("Een oude bron kon een heiligenbron worden.", J),
            ("Alle oude gebruiken verdwenen meteen na de bekering.", F),
            ("De oude goden bleven officieel naast de christelijke God vereerd.", F),
        ],
        "Sommige feesten en gebruiken kregen een christelijke betekenis. Zo versmolten Germaanse, Romeinse en christelijke gewoonten.",
    ),
    sleep(
        "De katholieke Kerk was opgebouwd als een piramide: bovenaan de [[paus]], daaronder de [[bisschoppen]], en daaronder de [[pastoors]] in de parochies.",
        ["koning", "graven", "ridders"],
        "Paus, bisschoppen, pastoors. Die vaste ordening gaf de Kerk macht over de grenzen van vorstendommen heen.",
    ),
    sorteer(
        "Deden de middeleeuwse kloosters dit of niet?",
        ["Deden ze", "Deden ze niet"],
        [
            ["oude teksten kopiëren en bewaren", "Deden ze"],
            ["woeste grond ontginnen tot landbouwgrond", "Deden ze"],
            ["zorgen voor zieken en reizigers", "Deden ze"],
            ["munten slaan", "Deden ze niet"],
            ["boeken drukken met losse letters", "Deden ze niet"],
        ],
        "Kopiëren, ontginnen en zorgen deden de monniken naast het gebed. Munten slaan was een recht van de vorst, en drukken met losse letters bestond nog niet.",
    ),
    mk(
        "In welk maatschappelijk domein situeer je de organisatie van de katholieke Kerk in de eerste plaats?",
        ["Het culturele domein", "Het maritieme domein", "Het ecologische domein", "Het demografische domein"],
        0,
        "De Kerk hoort vooral bij het culturele domein, al was ze ook economisch en politiek van gewicht.",
    ),
    inv(
        "Hoe noemt men een geloofsopvatting die afwijkt van de leer van de Kerk? Antwoord met één woord.",
        ["ketterij", "een ketterij", "de ketterij"],
        "Dat is ketterij. Omdat geloof en samenleving samenvielen, zag men afwijken als een aanval op de orde zelf.",
    ),
    tabel(
        "Klopt elke uitspraak over de joden in de middeleeuwse steden?",
        [
            ("Ze mochten vaak geen grond bezitten.", J),
            ("Ze mochten vaak geen ambacht uitoefenen.", J),
            ("Ze hadden dezelfde rechten als christenen.", F),
            ("Ze moesten soms een kenteken dragen.", J),
        ],
        "Joden hadden niet dezelfde rechten. Ze moesten soms apart wonen of een kenteken dragen, en bij rampen kregen ze de schuld.",
    ),
    mk(
        "Waarom lees je een middeleeuwse bron over joden extra kritisch?",
        [
            "Ze is bijna altijd door een christen geschreven, met zijn beeld van de ander",
            "Middeleeuwse bronnen zijn altijd vervalsingen van veel later",
            "Joden schreven alleen in een taal die niemand nog kan lezen",
            "De Kerk liet alle bronnen over joden achteraf herschrijven",
        ],
        0,
        "De auteur is bijna altijd christelijk. De stem van de groep zelf ontbreekt meestal.",
    ),
    # --- kunst
    mk(
        "Waarom noemde men een kerk wel eens de bijbel van de armen?",
        [
            "Glasramen, beelden en schilderingen vertelden de Bijbel aan wie niet kon lezen",
            "Arme mensen kregen er gratis een Bijbel mee naar huis",
            "Alleen arme mensen mochten in de kerk komen, rijken baden thuis",
            "De kerk werd betaald met de giften van de armste boeren",
        ],
        0,
        "Voor wie niet kon lezen, was christelijke kunst een verhaal in beeld.",
    ),
    klik(
        "Bekijk de twee bogen. Klik op de boog die het gewicht steiler naar beneden leidt.",
        "bogen.svg", [[0, 0, 50, 100]],
        "Boog A heeft een punt bovenaan: een spitsboog. Die leidt het gewicht steiler naar beneden dan een rondboog, die meer naar buiten duwt.",
    ),
    sorteer(
        "Is dit een kenmerk van romaanse of van gotische bouwkunst?",
        ["Romaans", "Gotisch"],
        [
            ["dikke muren", "Romaans"],
            ["kleine vensters", "Romaans"],
            ["een zware, donkere indruk", "Romaans"],
            ["luchtbogen", "Gotisch"],
            ["kruisribgewelven", "Gotisch"],
            ["grote glasramen", "Gotisch"],
        ],
        "Romaanse kerken zijn zwaar en donker met kleine vensters. Gotische kerken zijn hoger en lichter.",
    ),
    mk(
        "Waarom konden er in een gotische kerk zulke grote glasramen komen?",
        [
            "Het geraamte droeg het gewicht, dus de muur hoefde dat niet meer",
            "Glas was in die tijd goedkoper geworden dan steen",
            "De gotische kerken hadden geen dak, alleen een gewelf",
            "De muren werden dikker gemaakt, zodat ze meer glas konden dragen",
        ],
        0,
        "Het verschil zit in de bouwtechniek. Draagt het geraamte het gewicht, dan kunnen er grote ramen in de muur.",
    ),
    met_prent(
        "lam-gods.webp",
        tabel(
            "Bekijk dit werk van de gebroeders Van Eyck. Klopt elke uitspraak over de Vlaamse primitieven?",
            [
                ("Ze schilderden als een van de eersten zo gedetailleerd met olieverf.", J),
                ("Primitief betekent hier dat hun werk onbeholpen was.", F),
                ("Het werk toont hoe ver hun techniek al stond.", J),
                ("Het werk is in de 19de eeuw gemaakt als kopie van een fresco.", F),
            ],
            "Primitief betekent hier eerste, niet onbeholpen. Dit is het Lam Gods in Gent, uit de 15de eeuw.",
        ),
    ),
    # --- wereldbeeld en kennis
    dict(
        **inv(
            "Bekijk het schema van een middeleeuwse wereldkaart. Welke stad stond op zo'n kaart in het midden, bij letter A?",
            ["Jeruzalem"],
            "In het midden stond Jeruzalem. De kaart ordent de wereld naar het geloof.",
        ),
        afbeelding_url=KAART,
    ),
    dict(
        **tabel(
            "Bekijk opnieuw het schema van de middeleeuwse wereldkaart. Klopt elke uitspraak?",
            [
                ("Het deel bij B ligt in het oosten.", J),
                ("Met zo'n kaart kan je afstanden nauwkeurig meten.", F),
                ("Zo'n kaart vertelt eerder dan dat ze meet.", J),
                ("Een zeevaarder vond er zijn weg mee naar een andere haven.", F),
            ],
            "Op zo'n kaart staat het oosten bovenaan. Ze ordent de wereld naar het geloof, niet naar afstand.",
        ),
        afbeelding_url=KAART,
    ),
    mk(
        "Wat past bij het middeleeuwse wereldbeeld?",
        [
            "Alles was door God geordend en elk wezen had zijn vaste plaats",
            "De zon stond in het midden en de aarde draaide eromheen",
            "Elke mens kon zelf kiezen welke plaats hij in de wereld innam",
            "De wereld was toevallig ontstaan en had geen vaste orde",
        ],
        0,
        "De aarde stond in het midden en alles was door God geordend, van steen tot engel. Ook de standenleer past daarin.",
    ),
    tabel(
        "Wat kwam via de Arabische wetenschappen naar christelijk Europa? Klopt elke uitspraak?",
        [
            ("Griekse teksten, via Arabische vertalingen.", J),
            ("De cijfers waarmee wij nog altijd rekenen.", J),
            ("De boekdrukkunst met losse letters.", F),
            ("Vooruitgang in geneeskunde en sterrenkunde.", J),
        ],
        "Griekse teksten, onze cijfers en veel kennis van geneeskunde, sterrenkunde en wiskunde kwamen langs die weg. De boekdrukkunst met losse letters komt van Gutenberg.",
    ),
    mk(
        "Vanaf de 12de eeuw ontstaan in Europa de eerste universiteiten, zoals die van Bologna. In welke taal studeerde men daar?",
        ["Latijn", "Arabisch", "Frans", "Grieks"],
        0,
        "Aan de middeleeuwse universiteiten studeerde men in het Latijn, ook in Leuven.",
    ),
    # --- Frankrijk en Engeland
    keuze(
        "Aan het einde van de middeleeuwen regeert de Franse koning steeds meer [[*alleen|samen met een parlement]], de Engelse steeds meer [[*samen met een parlement|alleen]]. De Franse koning breidde zijn gezag uit vanuit [[*Parijs|Londen|Aken]].",
        "Twee wegen: in Frankrijk een groot, centraal bestuurd rijk, in Engeland een koning die zijn macht moet delen.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Engelse adel de Magna Carta afdwingt.",
        TL, [[40.8, 25, 3.5, 55]],
        "De Magna Carta dateert van 1215.",
    ),
    mk(
        "Wat betekende de Magna Carta voor de macht van de Engelse koning?",
        [
            "Ook de koning moest zich aan afspraken houden",
            "Engeland werd meteen een democratie met verkiezingen",
            "De koning kreeg voortaan alle macht zonder adel of parlement",
            "De graven kregen het recht om de koning af te zetten",
        ],
        0,
        "Het is nog geen democratie, maar wel een macht die niet meer onbeperkt is.",
    ),
    # --- de Guldensporenslag
    tabel(
        "Klopt elke uitspraak over de Guldensporenslag bij Kortrijk?",
        [
            ("Aan Vlaamse kant vochten veel stedelingen.", J),
            ("Tegenover hen stond het ridderleger van de Franse koning.", J),
            ("Na de slag werd Vlaanderen een onafhankelijk koninkrijk.", F),
            ("De ambachten kregen daarna meer invloed in de steden.", J),
        ],
        "Stedelingen, met de ambachten voorop, versloegen het Franse ridderleger. De inlijving werd voorlopig afgewend, maar Vlaanderen moest later zware betalingen doen.",
    ),
    inv(
        "Welke dag is vandaag de feestdag van de Vlaamse Gemeenschap, als herinnering aan de Guldensporenslag? Schrijf dag en maand.",
        ["11 juli", "elf juli", "11/7"],
        "11 juli. Dat een middeleeuwse gebeurtenis vandaag nog betekenis krijgt, hoort bij beeldvorming.",
    ),
    mk(
        "Waarom was de Guldensporenslag geen taalstrijd?",
        [
            "Het ging om macht, geld en zeggenschap; de taalkant kwam er pas veel later bij",
            "Iedereen in Vlaanderen sprak toen Frans, ook de stedelingen",
            "De Franse ridders spraken Nederlands, dus was er geen verschil",
            "Taal mocht in de middeleeuwen van de Kerk geen reden voor oorlog zijn",
        ],
        0,
        "De taalkant is er pas in de 19de eeuw bij gekomen. Het ging om macht, geld en zeggenschap in de steden.",
    ),
    # --- islam en kruistochten
    sorteer(
        "Welk soort motief voor de kruistochten is dit?",
        ["Godsdienstig", "Economisch", "Sociaal"],
        [
            ["de heilige plaatsen in bezit krijgen", "Godsdienstig"],
            ["handel met het oosten", "Economisch"],
            ["buit", "Economisch"],
            ["jongere adellijke zonen die een eigen gebied zoeken", "Sociaal"],
        ],
        "Godsdienstig: de heilige plaatsen. Economisch: handel en buit. Sociaal: jongere zonen zonder erfenis.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Akko valt, het laatste steunpunt van de kruisvaarders.",
        TL, [[54.1, 25, 3.5, 55]],
        "Akko viel in 1291.",
    ),
    tabel(
        "Klopt elke uitspraak over de gevolgen van de kruistochten voor West-Europa?",
        [
            ("Er kwam meer handel met het oosten via Italiaanse steden.", J),
            ("Nieuwe producten en kennis kwamen mee.", J),
            ("De verhouding met moslims en joden verhardde.", J),
            ("De standensamenleving verdween.", F),
        ],
        "De kruisvaardersstaten hielden het niet vol, maar de gevolgen bleven: meer handel, nieuwe producten en kennis, en meer vijandschap. De standen bleven bestaan.",
    ),
    mk(
        "Wat zijn de zijderoutes?",
        [
            "Een net van handelswegen over land en zee tussen het Westen en China",
            "Eén lange weg waarlangs enkel zijde naar Europa werd gebracht",
            "De route die de kruisvaarders volgden naar het Heilige Land",
            "Een rivier in China waarop zijde werd vervoerd",
        ],
        0,
        "Het is geen enkele weg maar een net van routes, en er ging veel meer over dan zijde alleen.",
    ),
    casus(
        "In Toledo en Palermo werkten in de middeleeuwen christelijke, joodse en islamitische geleerden samen om Arabische boeken te vertalen. In dezelfde tijd vochten elders kruisvaarders tegen moslimlegers.",
        [
            mk(
                "Wat zegt dit over het contact tussen de islam en het Westen?",
                [
                    "Het bestond zowel uit oorlog als uit handel en kennis delen",
                    "Het bestond enkel uit oorlog, vertalen was een uitzondering",
                    "Er was geen enkel contact, alleen vertalers kenden de islam",
                    "Het was enkel vriendschappelijk, de oorlogen zijn een mythe",
                ],
                0,
                "Er werd samen vertaald terwijl er elders gevochten werd. Het contact had beide kanten.",
            ),
            open_(
                "Waarom mag je de kruistochten niet enkel vanuit westerse bronnen bekijken? Leg uit in twee zinnen.",
                "Wie schrijft, kiest wat hij vertelt. De Arabische kronieken geven een ander beeld van dezelfde gebeurtenissen, dus heb je beide kanten nodig.",
                "Een goed antwoord zegt dat elke bron een standpunt heeft en dat de andere kant een ander beeld geeft.",
            ),
        ],
    ),
]

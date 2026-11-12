"""Vorsten, opstand en de Verlichting — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1400-1800.svg", zelf=True,
         wat="Tijdlijn van 1400 tot 1800 (dezelfde als bij De 'Nieuwe' Wereld).",
         vragen="klikvragen op 1566, 1688 en op de jaren van de oorlog met Spanje"),
    dict(bestand="nederlanden.svg", zelf=True,
         wat="Schema van de Nederlanden in twee delen, A boven en B onder, met de zee links en een havenstad aan een rivier.",
         vragen="klikvraag: welk deel werd onafhankelijk"),
    dict(bestand="lodewijk-xiv-rigaud.webp", zelf=False,
         wat="Het staatsieportret van Lodewijk XIV door Hyacinthe Rigaud (1701).",
         waar="Wikimedia Commons, zoek op 'Louis XIV of France Rigaud' (publiek domein).",
         vragen="tabelvraag over Versailles en het absolutisme"),
    dict(bestand="beeldenstorm-hogenberg.webp", zelf=False,
         wat="Prent van Frans Hogenberg van de Beeldenstorm van 1566 in een kerk.",
         waar="Wikimedia Commons, zoek op 'Beeldenstorm Hogenberg' (publiek domein).",
         vragen="tabelvraag over de Beeldenstorm"),
]

TL = "tijdlijn-1400-1800.svg"

VRAGEN = [
    # --- absolutisme
    tabel(
        "Klopt elke uitspraak over het vorstelijk absolutisme?",
        [
            ("Alle macht ligt bij de koning.", J),
            ("De koning stelt zijn ministers zelf aan en zet ze zelf af.", J),
            ("De standenvergadering wordt niet meer bijeengeroepen.", J),
            ("De koning wordt om de zoveel jaar verkozen.", F),
        ],
        "De koning is aan niemand verantwoording schuldig. Verkozen worden hoort bij een republiek.",
    ),
    inv(
        "Hoe heet de opvatting dat de macht van de koning rechtstreeks van God komt? Antwoord met twee Franse woorden.",
        ["droit divin", "het droit divin"],
        "Het droit divin. Wie zich dan tegen de koning verzet, verzet zich tegen God zelf.",
    ),
    met_prent(
        "lodewijk-xiv-rigaud.webp",
        tabel(
            "Bekijk het portret van de Zonnekoning. Waarvoor gebruikte hij zijn hof in Versailles? Klopt elke uitspraak?",
            [
                ("om de adel aan het hof te binden en zo onschadelijk te maken", J),
                ("om zijn macht in kunst en ceremonie zichtbaar te maken", J),
                ("om het bestuur onder zijn eigen oog te houden", J),
                ("om er geregeld de Staten-Generaal samen te roepen", F),
            ],
            "Versailles bond de adel, toonde macht en hield het bestuur dichtbij. De Staten-Generaal riep hij niet meer samen.",
        ),
    ),
    mk(
        "Wat ondermijnde op lange termijn de absolute macht in Frankrijk?",
        [
            "Oorlogen en geldgebrek",
            "Een verkozen parlement dat elke wet tegenhield",
            "De paus, die de koning had afgezet",
            "Een opstand van de adel in Versailles zelf",
        ],
        0,
        "Oorlogen en hofhouding kostten enorm veel, en de belasting drukte op wie ze het minst kon dragen.",
    ),
    mk(
        "Na 1689 is Engeland een constitutionele parlementaire monarchie. Wat betekent dat?",
        [
            "Een koning gebonden aan een grondwet, met een parlement dat mee beslist",
            "Een koning die door het parlement om de vijf jaar opnieuw verkozen of weggestuurd wordt",
            "Een land zonder koning, waar enkel een verkozen parlement over alles beslist",
            "Een koning die zijn macht van God krijgt en zelf de wetten maakt",
        ],
        0,
        "De koning blijft, maar hij regeert binnen regels die hij niet zelf kan veranderen.",
    ),
    # --- Engeland
    sorteer(
        "Was dit een oorzaak van de Glorious Revolution of niet?",
        ["Oorzaak", "Geen oorzaak"],
        [
            ["de koning wilde zonder het parlement regeren", "Oorzaak"],
            ["de koning was katholiek in een overwegend protestants land", "Oorzaak"],
            ["het parlement vreesde voor zijn eigen bestaan", "Oorzaak"],
            ["een boerenopstand tegen de tiende penning", "Geen oorzaak"],
        ],
        "Het ging om de macht van het parlement en om het geloof van de koning. De tiende penning was een belasting in de Nederlanden.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar van de Glorious Revolution.",
        TL, [[66.8, 25, 2.2, 55]],
        "In 1688 vluchtte Jacobus II en werd Willem III uit de Nederlanden gehaald, zonder grote veldslag in Engeland.",
    ),
    mk(
        "Wat legde de Bill of Rights vast?",
        [
            "De koning mag geen wetten opheffen of belastingen heffen zonder het parlement",
            "De koning mag het parlement ontbinden en zonder parlement regeren wanneer hij dat zelf wil",
            "Alle volwassen Engelsen krijgen voortaan stemrecht, zowel de mannen als de vrouwen",
            "De koning moet voortaan katholiek zijn",
        ],
        0,
        "Daarmee is de macht van de vorst voor het eerst in een tekst begrensd.",
    ),
    keuze(
        "In de 17de eeuw wint in Frankrijk [[*de vorst|het parlement]] het van [[*het parlement|de vorst]], in Engeland net omgekeerd.",
        "Dezelfde eeuw, twee tegengestelde antwoorden: absolutisme in Frankrijk, een begrensde vorst in Engeland.",
    ),
    # --- de Opstand
    tabel(
        "Klopt elke uitspraak over het beleid van Karel V en Filips II in de Nederlanden?",
        [
            ("Ze wilden het bestuur centraliseren.", J),
            ("Ze stelden nieuwe bisdommen in.", J),
            ("Ze traden hard op tegen het protestantisme.", J),
            ("Ze gaven de steden meer privileges.", F),
        ],
        "Meer privileges gaven ze niet; ze knabbelden er net aan.",
    ),
    mk(
        "Waarom voelde centralisatie voor een stad als diefstal van haar rechten?",
        [
            "Het bestuur kwam van één punt, terwijl de stad eigen privileges had",
            "De vorst nam elk jaar al het geld uit de stadskas mee naar zijn hof in Spanje",
            "De stad moest voortaan zelf haar soldaten betalen",
            "De stad mocht geen markt meer houden",
        ],
        0,
        "Centralisatie is doelmatig voor de vorst, maar een stad met een eigen keure verloor zo haar zelfstandigheid.",
    ),
    sorteer(
        "Is dit een oorzaak of een gevolg van de Opstand in de Nederlanden?",
        ["Oorzaak", "Gevolg"],
        [
            ["de aantasting van de oude privileges", "Oorzaak"],
            ["de vervolging van protestanten", "Oorzaak"],
            ["zware belastingen zoals de tiende penning", "Oorzaak"],
            ["de sluiting van de Schelde", "Gevolg"],
            ["kooplui en geleerden trekken naar het noorden", "Gevolg"],
        ],
        "Privileges, geloof en belastingen dreven tot opstand. De sluiting van de Schelde en het vertrek van kooplui volgden erop.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar van de Beeldenstorm.",
        TL, [[40.1, 25, 2.2, 55]],
        "De Beeldenstorm is van 1566. Hij begon in Steenvoorde en trok in enkele weken over de Nederlanden.",
    ),
    met_prent(
        "beeldenstorm-hogenberg.webp",
        tabel(
            "Bekijk deze prent van Frans Hogenberg. Klopt elke uitspraak?",
            [
                ("De prent toont hoe beelden in een kerk vernield worden.", J),
                ("Voor Filips II was dit het bewijs dat hard optreden nodig was.", J),
                ("Daarna stuurde hij de hertog van Alva met zijn Raad van Beroerten.", J),
                ("De beeldenstormers wilden de kerk mooier versieren.", F),
            ],
            "De Beeldenstorm was voor Filips II het teken om in te grijpen.",
        ),
    ),
    mk(
        "Een Spaanse bron noemt Alva de redder van orde en geloof, een Nederlandse bron de bloedhertog. Wat besluit je?",
        [
            "Ze kunnen allebei eerlijk zijn en toch iets anders belangrijk vinden",
            "Een van beide bronnen liegt zeker, dus moet je er één weggooien en de andere geloven",
            "De oudste bron heeft altijd gelijk",
            "Bronnen die elkaar zo sterk tegenspreken, zijn allebei waardeloos voor een historicus",
        ],
        0,
        "Elke auteur schrijft vanuit zijn eigen kant van het conflict. Tegenspraak betekent niet dat er zeker één liegt.",
    ),
    mk(
        "Hoe redeneert het Plakkaat van Verlatinghe?",
        [
            "Een vorst die zijn onderdanen als een tiran behandelt, verspeelt zijn recht",
            "Een vorst krijgt zijn macht rechtstreeks van God en mag dus door niemand afgezworen worden",
            "Een vorst moet om de vier jaar door de verzamelde gewesten opnieuw herkozen worden om te blijven",
            "Een vorst die protestant wordt, verliest automatisch zijn kroon",
        ],
        0,
        "In 1581 zwoeren de gewesten Filips II af. Dat idee komt bij de Verlichting terug.",
    ),
    klik(
        "De oorlog met Spanje duurde tachtig jaar, met een bestand van twaalf jaar ertussen. Klik op de tijdlijn op die hele periode.",
        TL, [[41.7, 25, 17.5, 55]],
        "De oorlog duurde van 1568 tot 1648.",
    ),
    klik(
        "Bekijk het schema van de Nederlanden. Klik op het deel waarvan de Vrede van Münster de onafhankelijkheid erkende.",
        "nederlanden.svg", [[19.0, 0, 76.0, 48.0]],
        "Het noorden werd onafhankelijk en een republiek. Het zuiden bleef katholiek en onder Spaans bestuur.",
    ),
    # --- Verlichting
    mk(
        "Waar verwijst het licht in de naam Verlichting naar?",
        [
            "Naar het verstand tegenover de duisternis van vooroordeel en willekeur",
            "Naar de eerste straatverlichting met olielampen in de straten van Parijs en Londen",
            "Naar het licht van God dat volgens de Kerk de koning zijn macht geeft",
            "Naar de grote glasramen van de gotische kathedralen",
        ],
        0,
        "De Verlichting neemt het verstand als leidraad voor kennis en samenleving. Ze ontstond vooral in de 18de eeuw.",
    ),
    koppel(
        "Welk idee hoort bij elke filosoof?",
        [
            ["John Locke", "natuurlijke rechten op leven, vrijheid en bezit"],
            ["Voltaire", "godsdienstige verdraagzaamheid en vrije meningsuiting"],
            ["Montesquieu", "de scheiding der machten"],
            ["Rousseau", "de macht gaat uit van het volk"],
        ],
        ["de predestinatie"],
        "Locke, Voltaire, Montesquieu en Rousseau. De predestinatie hoort bij het calvinisme.",
    ),
    inv(
        "Welke filosoof vatte de Verlichting samen in 'durf zelf te denken', sapere aude?",
        ["Kant", "Immanuel Kant"],
        "Immanuel Kant.",
    ),
    mk(
        "Waarom splits je de macht in een wetgevende, een uitvoerende en een rechterlijke macht?",
        [
            "Zodat de ene macht de andere kan tegenhouden",
            "Zodat de regering de rechtbanken kan leiden",
            "Zodat de koning sneller kan beslissen",
            "Zodat elke stand één macht krijgt",
        ],
        0,
        "De scheiding der machten betekent net niet dat de regering de rechtbanken leidt, maar het omgekeerde.",
    ),
    koppel(
        "Welk begrip uit de Verlichting past bij elke beschrijving?",
        [
            ["dezelfde wet geldt voor iedereen, ongeacht stand of geboorte", "Rechtsgelijkheid"],
            ["je kan vooraf weten wat verboden is en welke straf erop staat", "Rechtszekerheid"],
            ["de tekst met de grondregels van een staat, boven de gewone wetten", "Grondwet"],
        ],
        ["Absolutisme"],
        "Rechtsgelijkheid botst met de standensamenleving, rechtszekerheid met willekeur. De grondwet staat boven de gewone wetten.",
    ),
    sorteer(
        "Bij welk begrip hoort deze uitspraak?",
        ["Empirisme", "Rationalisme", "Vooruitgangsoptimisme"],
        [
            ["eerst kijken en meten, dan besluiten", "Empirisme"],
            ["met de rede tot een besluit komen", "Rationalisme"],
            ["kennis en rede kunnen de samenleving beter maken", "Vooruitgangsoptimisme"],
        ],
        "Empirisme vertrekt van de waarneming, rationalisme van het redeneren, vooruitgangsoptimisme van het geloof in een betere samenleving.",
    ),
    mk(
        "Op welk punt komen empirisme en rationalisme overeen?",
        [
            "Allebei verwerpen ze het argument van het gezag alleen",
            "Allebei vertrekken ze van de waarneming",
            "Allebei steunen ze op de Bijbel als enige bron",
            "Allebei vinden ze dat de koning het laatste woord heeft",
        ],
        0,
        "Dat iets waar is omdat een hooggeplaatst iemand het zegt, geldt voor geen van beide.",
    ),
    tabel(
        "Wat herken je van de Verlichting in de Belgische grondwet? Klopt elke uitspraak?",
        [
            ("de scheiding der machten", J),
            ("de gelijkheid van alle Belgen voor de wet", J),
            ("de vrijheid van godsdienst en van meningsuiting", J),
            ("erfelijke voorrechten voor de adel", F),
        ],
        "Erfelijke voorrechten zijn net afgeschaft. De grondwet van 1831 gold als een van de meest verlichte van Europa.",
    ),
    sleep(
        "In België wordt beslist op het niveau van de [[gemeente]], van de gemeenschappen en de gewesten, op het [[federale]] en op het [[Europese]] niveau.",
        ["keizerlijke", "pauselijke"],
        "Vijf niveaus, van dichtbij tot ver weg.",
    ),
    casus(
        "Lina is zestien. Ze wil dat er een veilig fietspad komt naar haar school.",
        [
            tabel(
                "Hoe kan Lina zelf verantwoordelijkheid opnemen binnen de rechtsstaat? Klopt elke uitspraak?",
                [
                    ("Ze ondertekent een petitie of start er zelf een.", J),
                    ("Ze gaat naar een inspraakavond in het stadhuis.", J),
                    ("Ze sluit zich aan bij de jeugdraad.", J),
                    ("Ze zet de burgemeester zelf af.", F),
                ],
                "Petitie, inspraak en een jeugdraad zijn wegen binnen de rechtsstaat. Stemmen en je informeren horen er ook bij.",
            ),
            mk(
                "Lina zegt: 'Als een bestuur mijn rechten schendt, mag ik me verzetten.' Hoe heet dat recht?",
                ["Het weerstandsrecht", "Het kiesrecht", "Het stemrecht", "Het erfrecht"],
                0,
                "Het weerstandsrecht is het recht om je te verzetten tegen een bestuur dat je rechten schendt.",
            ),
            open_(
                "Waarom is de Verlichting een keerpunt in het politieke domein? Leg uit in twee zinnen.",
                "De bron van het gezag verschuift van God naar het volk. Wie zegt dat de macht van het volk komt, zegt ook dat het volk ze kan terugnemen.",
                "Een goed antwoord noemt de verschuiving van God naar het volk.",
            ),
        ],
    ),
]

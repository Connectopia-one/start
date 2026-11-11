"""Humanisme, Reformatie, renaissance en barok — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1400-1800.svg", zelf=True,
         wat="Tijdlijn van 1400 tot 1800 (dezelfde als bij De 'Nieuwe' Wereld).",
         vragen="klikvragen op 1517 en op de jaren van het Concilie van Trente"),
    dict(bestand="perspectief.svg", zelf=True,
         wat="Tekening van een plein met tegels en twee rijen bomen die naar één verdwijnpunt lopen.",
         vragen="klikvraag op het verdwijnpunt"),
    dict(bestand="vesalius-fabrica.jpg", zelf=False,
         wat="Een houtsnede uit De humani corporis fabrica van Vesalius (1543), bijvoorbeeld een spierfiguur of een geraamte.",
         waar="Wikimedia Commons, zoek op 'Vesalius Fabrica' (publiek domein).",
         vragen="tabelvraag over de nieuwe wetenschappelijke methode"),
    dict(bestand="kruisoprichting.jpg", zelf=False,
         wat="De Kruisoprichting van Rubens (rond 1610), Onze-Lieve-Vrouwekathedraal Antwerpen.",
         waar="Wikimedia Commons, zoek op 'Rubens Elevation of the Cross' (publiek domein).",
         vragen="tabelvraag over de kenmerken van de barok"),
]

TL = "tijdlijn-1400-1800.svg"

VRAGEN = [
    # --- humanisme
    mk(
        "Waarom ontstond het humanisme in steden zoals Florence, Venetië en Rome?",
        [
            "Ze hadden geld, handelscontacten en Romeinse resten om op voort te bouwen",
            "De paus verplichtte alle geleerden om in die steden te gaan wonen",
            "Er waren daar geen kloosters, dus kon men vrij nadenken",
            "Ze lagen het verst van de Arabische wereld en haar invloed",
        ],
        0,
        "Rijke Italiaanse steden hadden het geld en de contacten, en de oudheid lag er letterlijk voor het oprapen.",
    ),
    tabel(
        "Klopt elke uitspraak over de humanisten?",
        [
            ("Ze hadden belangstelling voor de mens en zijn mogelijkheden.", J),
            ("Ze grepen terug naar de Griekse en Romeinse oudheid.", J),
            ("Ze onderzochten de oorspronkelijke teksten kritisch.", J),
            ("Ze wilden het geloof afschaffen.", F),
        ],
        "De meeste humanisten bleven gelovig. Ze wilden het geloof zuiveren, niet afschaffen.",
    ),
    inv(
        "Hoe heet het boek waarin Erasmus de misbruiken in Kerk en samenleving bespotte?",
        ["Lof der Zotheid", "de Lof der Zotheid", "Lof der zotheid"],
        "In Lof der Zotheid pleitte Erasmus ook voor onderwijs en verdraagzaamheid.",
    ),
    mk(
        "Welke rol speelde de boekdrukkunst voor het humanisme?",
        [
            "Ideeën raakten veel sneller en wijder verspreid",
            "Boeken mochten voortaan enkel nog in het Latijn",
            "Monniken konden sneller overschrijven met een pen",
            "Ze maakte de universiteiten overbodig",
        ],
        0,
        "Wat een monnik vroeger in maanden overschreef, rolde nu bij honderden van de pers.",
    ),
    mk(
        "Wat verandert er aan de wetenschappelijke methode?",
        [
            "Men gaat zelf waarnemen en proeven doen",
            "Men gelooft voortaan enkel nog wat de Kerk zegt",
            "Men leest de oude gezaghebbende teksten nog vaker en zorgvuldiger",
            "Men laat wetenschap over aan de vorsten",
        ],
        0,
        "Men vertrouwt eigen waarneming en proeven meer dan oude gezaghebbende teksten.",
    ),
    met_prent(
        "vesalius-fabrica.jpg",
        tabel(
            "Bekijk deze prent uit het boek van Vesalius. Klopt elke uitspraak?",
            [
                ("Vesalius ontleedde zelf lichamen.", J),
                ("Hij toonde dat de oude Griekse teksten niet in alles gelijk hadden.", J),
                ("De tekeningen zijn gemaakt naar eigen waarneming.", J),
                ("Hij nam de tekeningen over uit een middeleeuws handboek.", F),
            ],
            "Het echte nieuwe is dat je mag vaststellen dat Galenus zich vergiste, op basis van wat je zelf ziet.",
        ),
        volgt=True,
    ),
    tabel(
        "Hoe beïnvloedde de Arabische wereld de westerse geneeskunde? Klopt elke uitspraak?",
        [
            ("Arabische handboeken, zoals die van Ibn Sina, werden aan de universiteiten gebruikt.", J),
            ("Griekse geneeskundige teksten kwamen via Arabische vertalingen terug.", J),
            ("De microscoop werd uitgevonden in Bagdad.", F),
            ("Kennis over geneesmiddelen en ziekenzorg kwam mee.", J),
        ],
        "De microscoop kwam uit de Nederlanden, in de 17de eeuw.",
    ),
    # --- Reformatie
    sorteer(
        "Was dit een oorzaak van de Reformatie of niet?",
        ["Oorzaak", "Geen oorzaak"],
        [
            ["de aflaathandel", "Oorzaak"],
            ["het rijke, wereldse leven van hoge geestelijken", "Oorzaak"],
            ["de kritische lezing van de Bijbel door humanisten", "Oorzaak"],
            ["een verbod op kerkbezoek", "Geen oorzaak"],
        ],
        "Misbruiken in de Kerk en de kritische Bijbellezing waren oorzaken. Kerkbezoek werd nergens verboden.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Luther zijn stellingen tegen de aflaathandel ophangt.",
        TL, [[29.4, 25, 2.2, 55]],
        "Luther hing zijn stellingen op in 1517, in Wittenberg.",
    ),
    mk(
        "Luther kwam in verzet tegen de aflaten. Wat was zo'n aflaat?",
        [
            "Een kwijtschelding van straf voor zonden, die men ook kon kopen",
            "Een verbod om de mis bij te wonen, opgelegd door de bisschop",
            "Een belasting die de vorst hief op elke kerk in zijn gebied",
            "Een boek waarin de priester de zonden van zijn parochie noteerde",
        ],
        0,
        "Het geld diende onder meer voor de bouw van de Sint-Pietersbasiliek in Rome.",
    ),
    keuze(
        "Luther leerde dat een mens gered wordt door [[*het geloof alleen|goede werken|het kopen van aflaten]] en dat [[*de Bijbel|de paus|het concilie]] de enige bron is. Daarmee kwam de bemiddelende rol van [[*de priesters|de vorsten|de kooplui]] op de helling.",
        "Sola fide en sola scriptura: geloof alleen en de Bijbel alleen. Dan heb je de Kerk niet meer nodig als tussenpersoon.",
    ),
    mk(
        "Wat wilde Luther toen hij zijn stellingen ophing?",
        [
            "Een discussie, geen scheuring",
            "Meteen een nieuwe Kerk stichten met hemzelf als paus",
            "De Duitse keizer afzetten",
            "Alle kloosters laten sluiten en de monniken verjagen",
        ],
        0,
        "Hij wilde een discussie over de aflaathandel. De scheuring kwam later.",
    ),
    sorteer(
        "Hoort dit bij het calvinisme of bij de katholieke Kerk na het Concilie van Trente?",
        ["Calvinisme", "Katholieke Kerk"],
        [
            ["predestinatie", "Calvinisme"],
            ["een sobere eredienst zonder beelden", "Calvinisme"],
            ["een kerk bestuurd door gekozen ouderlingen", "Calvinisme"],
            ["seminaries die priesters opleiden", "Katholieke Kerk"],
            ["een index van verboden boeken", "Katholieke Kerk"],
        ],
        "Calvinisten geloven dat God vooraf bepaalt wie gered wordt, en kiezen voor soberheid en ouderlingen. De katholieke Kerk vernieuwde met seminaries en bewaakte wat men las.",
    ),
    mk(
        "Hoe ontstond het anglicanisme?",
        [
            "Uit een politieke breuk: de koning wilde scheiden en de paus weigerde",
            "Uit een lange discussie over de predestinatie onder Engelse geleerden",
            "Uit een opstand van Engelse boeren tegen hun bisschoppen",
            "Uit een verdrag tussen de paus en de Engelse koning",
        ],
        0,
        "Hendrik VIII maakte zichzelf hoofd van de Engelse Kerk toen de paus zijn scheiding weigerde.",
    ),
    mk(
        "Waarom kozen sommige vorsten in Noord-Europa graag voor het protestantisme?",
        [
            "Wie zich van Rome losmaakte, kon de kerkelijke goederen in beslag nemen",
            "Protestantse vorsten hoefden geen leger meer te onderhouden",
            "De paus betaalde vorsten die protestant werden",
            "Protestanten mochten als enigen handel drijven met Azië",
        ],
        0,
        "Losmaken van Rome bracht ook gronden en goederen op. Het protestantisme sloeg aan in de Duitse vorstendommen, Scandinavië, Engeland en Schotland.",
    ),
    mk(
        "Men zei: 'Erasmus legde het ei, en Luther broedde het uit.' Wat bedoelde men daarmee?",
        [
            "Het humanisme was een voorwaarde voor de Reformatie",
            "Erasmus en Luther schreven samen één boek",
            "Luther was een leerling van Erasmus aan de universiteit",
            "Erasmus was tegen het humanisme, Luther ervoor",
        ],
        0,
        "Humanisten lazen de Bijbel in de oorspronkelijke taal en zagen dat de vertaling niet overal klopte. Daarop kon Luther verder bouwen.",
    ),
    mk(
        "In welk maatschappelijk domein situeer je de Reformatie in de eerste plaats?",
        ["Het culturele domein", "Het economische domein", "Het demografische domein", "Het ecologische domein"],
        0,
        "Het gaat in de eerste plaats over geloof, dus cultureel, al zette de Reformatie vorstendommen tegen elkaar op.",
    ),
    # --- Contrareformatie
    klik(
        "Het Concilie van Trente vergaderde met tussenpozen een kleine twintig jaar. Klik op de tijdlijn op die periode.",
        TL, [[36.6, 25, 3.9, 55]],
        "Het concilie vergaderde van 1545 tot 1563.",
    ),
    tabel(
        "Klopt elke uitspraak over de Contrareformatie?",
        [
            ("Ze bestond enkel uit de vervolging van protestanten.", F),
            ("Nieuwe orden zoals de jezuïeten richtten scholen op.", J),
            ("De mis werd afgeschaft.", F),
            ("Wat het concilie besliste, bleef eeuwenlang gelden.", J),
        ],
        "Er waren ook hervormingen van binnenuit. De mis werd net bevestigd en plechtiger gemaakt.",
    ),
    sleep(
        "De godsdienstige breuk had politieke gevolgen: godsdienstoorlogen in [[Frankrijk]], de Dertigjarige Oorlog in [[Duitsland]] en de Opstand in de [[Nederlanden]].",
        ["Spanje", "Italië"],
        "Overal in Europa zette de breuk vorsten en onderdanen tegen elkaar op.",
    ),
    # --- renaissance
    mk(
        "Renaissance betekent letterlijk wedergeboorte. Wat werd er volgens de kunstenaars en geleerden herboren?",
        [
            "De klassieke oudheid van de Grieken en Romeinen",
            "Het geloof van de eerste christenen",
            "De macht van het Romeinse keizerrijk",
            "De middeleeuwse kloosterkunst",
        ],
        0,
        "Kunstenaars en geleerden namen de Grieken en Romeinen opnieuw als voorbeeld.",
    ),
    klik(
        "Een renaissanceschilder wekt diepte op een plat vlak. Klik in deze tekening op het punt waar alle lijnen naartoe lopen.",
        "perspectief.svg", [[60.0, 35.0, 8.0, 13.0]],
        "Dat is het verdwijnpunt. Dingen worden kleiner naarmate ze verder staan.",
    ),
    tabel(
        "Waarom hoort de David van Michelangelo bij de renaissance? Klopt elke uitspraak?",
        [
            ("Het naakte lichaam is naar de natuur bestudeerd.", J),
            ("Het beeld heeft rustige, klassieke verhoudingen.", J),
            ("Het beeld is in brons gegoten.", F),
            ("David draagt een aureool als teken van heiligheid.", F),
        ],
        "Het is marmer, zonder aureool: de mens zelf is het onderwerp.",
    ),
    sorteer(
        "Hoort deze kunstenaar bij de Italiaanse renaissance of bij de barok?",
        ["Renaissance", "Barok"],
        [
            ["Leonardo da Vinci", "Renaissance"],
            ["Rafaël", "Renaissance"],
            ["Rubens", "Barok"],
            ["Bernini", "Barok"],
        ],
        "De renaissance bloeit rond 1500, de barok vanaf ongeveer 1600.",
    ),
    mk(
        "Wat is het grootste verschil tussen renaissancekunst en middeleeuwse kunst?",
        [
            "De renaissance toont de wereld zoals het oog ze ziet",
            "De renaissance gebruikt voor het eerst kleur",
            "De middeleeuwen schilderden enkel op doek",
            "De renaissance schilderde geen godsdienstige onderwerpen meer",
        ],
        0,
        "Op een middeleeuws paneel is de belangrijkste figuur het grootst, hoe ver hij ook staat.",
    ),
    mk(
        "Hoe verschilden de Vlaamse primitieven van de Italiaanse schilders?",
        [
            "Ze gingen vooral voor het detail, met olieverf",
            "Ze schilderden enkel portretten, nooit godsdienstige taferelen",
            "Ze kenden geen olieverf en werkten met kalk op muren",
            "Ze gingen vooral voor de klassieke verhoudingen van de oudheid",
        ],
        0,
        "Twee wegen naar de natuur toe: de Vlamingen het detail, de Italianen de klassieke verhoudingen.",
    ),
    # --- barok
    met_prent(
        "kruisoprichting.jpg",
        tabel(
            "Bekijk dit schilderij uit een Antwerpse kerk, van rond 1610. Klopt elke uitspraak?",
            [
                ("Je ziet veel beweging en drama.", J),
                ("Er zijn sterke contrasten tussen licht en donker.", J),
                ("Rust en evenwicht overheersen.", F),
                ("Zo'n werk past bij de kunst van de Contrareformatie.", J),
            ],
            "Beweging, drama en licht-donker zijn typisch voor de barok, de kunst waarmee de katholieke Kerk de kijker wilde raken.",
        ),
        volgt=True,
    ),
    mk(
        "Waarom lieten vorsten in de 17de eeuw hun paleizen vol barokkunst zetten?",
        [
            "Om hun macht en aanzien te tonen",
            "Om te tonen hoe sober ze leefden",
            "Om de protestanten in hun rijk gerust te stellen",
            "Om geld te besparen op hun paleizen",
        ],
        0,
        "Paleizen, tuinen en grote portretten moesten indruk maken. Soberheid was het laatste wat Versailles uitstraalde.",
    ),
    casus(
        "Rond 1600 laat een rijke koopman een groot altaarstuk maken voor een kerk in Antwerpen. Hijzelf staat er geknield op, in een hoekje.",
        [
            tabel(
                "Je gebruikt het altaarstuk als historische bron. Welke vragen helpen je verder? Klopt elke uitspraak?",
                [
                    ("Wie betaalde het werk, en waarom?", J),
                    ("Voor welke plaats en welk publiek werd het gemaakt?", J),
                    ("Wat staat er bewust wel en niet op?", J),
                    ("Hoeveel kostte de verf?", F),
                ],
                "Opdrachtgever, plaats, publiek en keuzes vertellen veel. De prijs van de verf brengt je niet ver.",
            ),
            open_(
                "Waarom noemt men de vroegmoderne tijd een breuk met de middeleeuwen? Noem ook iets wat gewoon doorloopt.",
                "Mens- en wereldbeeld, geloof, wetenschap en kunst veranderen alle vier tegelijk. Toch lopen de standen, de landbouw en de macht van de vorsten gewoon door.",
                "Een goed antwoord noemt meerdere dingen die tegelijk veranderen, en minstens één continuïteit.",
            ),
        ],
    ),
]

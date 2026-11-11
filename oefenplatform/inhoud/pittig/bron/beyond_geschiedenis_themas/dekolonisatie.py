"""Dekolonisatie en de wereld van vandaag — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvragen op 1960 en 1997"),
]

VRAGEN = [
    mk(
        "Een journalist schrijft dat een land zich in de jaren zestig dekoloniseerde. Wat bedoelt hij?",
        [
            "Koloniën worden zelfstandige staten en maken zich los van hun kolonisator",
            "Een kolonisator ruilt een kolonie met een andere Europese mogendheid tegen geld of grond",
            "Europese landen kopen hun koloniën terug van de inwoners",
            "Een kolonie krijgt een nieuwe gouverneur uit het moederland",
        ],
        0,
        "Dekolonisatie is het losmaken van de kolonisator: de kolonie wordt een zelfstandige staat.",
    ),
    tabel(
        "Is het een oorzaak van de dekolonisatie na 1945?",
        [
            ("De Europese mogendheden kwamen verzwakt uit de Tweede Wereldoorlog.", J),
            ("In de koloniën groeiden nationalistische bewegingen met opgeleide leiders.", J),
            ("Het Handvest van de VN schreef het zelfbeschikkingsrecht van volkeren in.", J),
            ("De Verenigde Staten en de Sovjet-Unie wilden zelf de Europese koloniën overnemen.", F),
        ],
        "Drie oorzaken: een verzwakt Europa, nationalisme in de koloniën en het zelfbeschikkingsrecht van volkeren.",
    ),
    mk(
        "Hoe stonden de Verenigde Staten en de Sovjet-Unie tegenover de Europese koloniale rijken?",
        [
            "Beide stonden er kritisch tegenover, elk om eigen redenen",
            "Beide steunden de koloniale rijken om Europa sterk te houden",
            "Enkel de Sovjet-Unie was kritisch; de VS steunden de koloniën",
            "Enkel de VS waren kritisch; de Sovjet-Unie wilde zelf koloniën",
        ],
        0,
        "Zowel Washington als Moskou zag de oude koloniale rijken liever verdwijnen, elk om eigen redenen.",
    ),
    keuze(
        "[[*India|Algerije|Congo]] werd in [[*1947|1960|1955]] onafhankelijk van het Verenigd Koninkrijk en gaf het voorbeeld. 1960 heet het Afrikajaar omdat [[*zeventien|drie|dertig]] Afrikaanse koloniën in dat ene jaar onafhankelijk werden.",
        "India in 1947 was het voorbeeld. In 1960 volgden er zeventien in Afrika.",
    ),
    sorteer(
        "Onderhandelde overdracht of gewapende strijd? Sorteer volgens de bundel.",
        ["Gewapende onafhankelijkheidsstrijd", "Niet gewapend"],
        [
            ["Algerije, met een oorlog van acht jaar", "Gewapende onafhankelijkheidsstrijd"],
            ["Een overdracht na onderhandelingen aan een rondetafel", "Niet gewapend"],
            ["Strijders die met wapens tegen het koloniale leger vechten", "Gewapende onafhankelijkheidsstrijd"],
            ["Een akkoord over een datum van onafhankelijkheid", "Niet gewapend"],
        ],
        "Dekolonisatie kon via onderhandelingen of via een gewapende strijd. In Algerije duurde de oorlog acht jaar.",
    ),
    mk(
        "Na de onafhankelijkheid braken in veel Afrikaanse staten grensconflicten uit. Wat had daar het meest mee te maken?",
        [
            "Ze waren door de kolonisatoren getrokken, dwars door volkeren heen",
            "Ze werden na de onafhankelijkheid elk jaar opnieuw vastgelegd door een stemming",
            "Ze volgden precies de grenzen van de vroegere volkeren",
            "Ze waren door de Verenigde Naties bij loting toegewezen",
        ],
        0,
        "Op de Conferentie van Berlijn en daarna trokken Europeanen grenzen op de kaart, zonder rekening te houden met wie er woonde.",
    ),
    inv(
        "Hoe noemt men economische overheersing van een land dat politiek wel onafhankelijk is?",
        "neokolonialisme",
        "Neokolonialisme: de vlag is veranderd, maar de economische afhankelijkheid bleef.",
    ),
    mk(
        "Waarom is de bijeenkomst in Bandung belangrijk voor de dekolonisatie?",
        [
            "Aziatische en Afrikaanse landen kwamen in 1955 samen tegen kolonialisme",
            "De Europese koloniale mogendheden verdeelden de rest van Afrika",
            "De NAVO en het Warschaupact sloten er een vredesakkoord na de Koreaoorlog",
            "België en Congo legden er de datum van de onafhankelijkheid vast",
        ],
        0,
        "Uit Bandung groeide de beweging van de niet-gebonden landen, die bij geen van beide blokken wilden horen.",
    ),
    tabel(
        "Juist of fout? Het verband tussen dekolonisatie en de Koude Oorlog.",
        [
            ("De supermachten probeerden de nieuwe staten naar hun kamp te trekken.", J),
            ("Ze steunden soms dictators, zolang die aan de juiste kant stonden.", J),
            ("In Korea, Vietnam en Angola voerden ze een strijd via anderen.", J),
            ("De nieuwe staten moesten verplicht lid worden van de NAVO of het Warschaupact.", F),
        ],
        "De nieuwe staten waren een inzet in de strijd tussen de blokken, maar konden ook niet-gebonden blijven.",
    ),
    tabel(
        "Is het een gevolg van de dekolonisatie op lange termijn?",
        [
            ("Blijvende economische afhankelijkheid van enkele grondstoffen", J),
            ("Een veel grotere groep landen binnen de Verenigde Naties", J),
            ("Migratie naar de voormalige moederlanden in Europa", J),
            ("Het einde van alle handel tussen Europa en Afrika", F),
        ],
        "Drie gevolgen op lange termijn. De handel stopte niet; vaak bleef de afhankelijkheid juist bestaan.",
    ),
    mk(
        "Wat betekent dekolonisering van het denken?",
        [
            "Opnieuw bekijken hoe wij over het koloniale verleden spreken en leren",
            "Alles wat met de koloniale tijd te maken heeft uit de boeken schrappen",
            "De koloniale tijd voortaan enkel nog positief voorstellen",
            "Koloniale geschiedenis enkel in de voormalige koloniën onderwijzen",
        ],
        0,
        "Het gaat om een nieuwe blik, niet om schrappen of goedpraten.",
    ),
    tabel(
        "Hoort de vraag bij het actuele debat over dekolonisering?",
        [
            ("Moeten voorwerpen uit koloniale musea terug naar het land van herkomst?", J),
            ("Wat doen we met standbeelden van koloniale figuren in onze straten?", J),
            ("Welke plaats krijgt het koloniale verleden in het onderwijs?", J),
            ("Moet België opnieuw koloniën verwerven?", F),
        ],
        "Teruggave, standbeelden en onderwijs: dat zijn de drie vragen van het debat.",
    ),
    mk(
        "Waarom werd het AfricaMuseum in Tervuren grondig hertekend?",
        [
            "Het bewaart een grote koloniale verzameling, en het geweld moest een plaats krijgen",
            "Het gebouw werd door een brand verwoest en moest volledig opnieuw",
            "Het museum verhuisde in 2018 naar Kinshasa en kreeg daar een nieuw ontwerp",
            "Het museum toonde voortaan alleen nog Belgische kunst uit de 19de eeuw",
        ],
        0,
        "Bij de heropening in 2018 kreeg het koloniale geweld er een plaats.",
    ),
    volgorde(
        "Zet de gebeurtenissen rond de Congolese onafhankelijkheid in de juiste volgorde.",
        ["Het plan-Van Bilsen", "De rellen in Leopoldstad", "De rondetafelconferentie in Brussel", "De onafhankelijkheid", "De moord op Lumumba"],
        "Eerst het plan voor dertig jaar, dan de rellen, de rondetafel, de onafhankelijkheid en enkele maanden later de moord.",
    ),
    mk(
        "Het plan van professor Van Bilsen uit 1955 stelde voor:",
        [
            "Een geleidelijke onafhankelijkheid over dertig jaar",
            "Een onmiddellijke onafhankelijkheid nog datzelfde jaar",
            "Congo voor altijd bij België te houden als provincie",
            "Congo te verdelen tussen België en Frankrijk",
        ],
        0,
        "Dertig jaar: toen werd dat door iedereen weggehoond. Na de rellen van 1959 ging het plots veel sneller.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Congo onafhankelijk werd.",
        "tijdlijn-1750-2030.svg",
        [[67.4, 25, 6.2, 55]],
        "Op 30 juni 1960, het Afrikajaar.",
    ),
    mk(
        "Waarom was Congo bij de onafhankelijkheid slecht voorbereid om zichzelf te besturen?",
        [
            "Er was geen ruime groep Congolese universitair geschoolden",
            "Er waren geen grondstoffen om de staat mee te betalen",
            "De Verenigde Naties verboden een eigen Congolese regering",
            "Er werden geen verkiezingen georganiseerd voor 1960",
        ],
        0,
        "Het Belgische bestuur had nauwelijks in hoger onderwijs voor Congolezen geïnvesteerd.",
    ),
    koppel(
        "Wie of wat past bij elke omschrijving?",
        [
            ["De eerste eerste minister van Congo", "Patrice Lumumba"],
            ["De eerste president van Congo", "Kasa-Vubu"],
            ["De provincie met de meeste kopererts, die zich afscheidde", "Katanga"],
        ],
        ["Laurent-Désiré Kabila", "Mobutu"],
        "Kabila en Mobutu kwamen pas later aan de macht.",
    ),
    tabel(
        "Juist of fout? De Congocrisis.",
        [
            ("De rijkste mijnprovincie scheidde zich af met Belgische steun.", J),
            ("De Verenigde Naties stuurden een vredesmacht naar Congo.", J),
            ("Lumumba zocht steun bij Moskou, waarna het Westen hem als gevaar zag.", J),
            ("Lumumba werd in 1965 door Mobutu afgezet en verbannen naar België.", F),
        ],
        "Lumumba werd in januari 1961 na zijn afzetting naar Katanga gebracht en daar vermoord.",
    ),
    mk(
        "Waartoe besloot een Belgische onderzoekscommissie in 2001 over de moord op Lumumba?",
        [
            "Tot een morele verantwoordelijkheid van Belgische regeringsleden",
            "Dat België er op geen enkele manier en op geen enkel moment bij betrokken was",
            "Dat Belgische ministers voor de rechter moesten verschijnen",
            "Dat de Verenigde Naties de enige schuldige waren",
        ],
        0,
        "Een morele verantwoordelijkheid, geen veroordeling door een rechter.",
    ),
    sorteer(
        "Is het een kenmerk van het bewind van Mobutu?",
        ["Kenmerk", "Geen kenmerk"],
        [
            ["Een autoritair eenpartijbewind", "Kenmerk"],
            ["Veel corruptie", "Kenmerk"],
            ["Een persoonscultus", "Kenmerk"],
            ["Steun van het Westen omdat hij zich tegen het communisme keerde", "Kenmerk"],
            ["Een sterk parlement dat de leider controleert", "Geen kenmerk"],
        ],
        "Mobutu duldde geen controle op zijn macht.",
    ),
    keuze(
        "In 1971 gaf Mobutu het land de naam [[*Zaïre|Katanga|Kivu]]. In [[*1997|1989|2019]] verdreef Laurent-Désiré Kabila hem en kreeg het land zijn naam Congo terug.",
        "Zaïre van 1971 tot 1997.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Mobutu verdreven werd.",
        "tijdlijn-1750-2030.svg",
        [[78.9, 25, 6.2, 55]],
        "1997, net voor het streepje van 2000.",
    ),
    mk(
        "Wat was er bijzonder aan de machtsoverdracht van 2019 in Congo?",
        [
            "Voor het eerst ging de macht na verkiezingen naar een andere president",
            "Voor het eerst nam een generaal de macht met een staatsgreep in Kinshasa",
            "België benoemde opnieuw een gouverneur voor Congo",
            "Het oosten van het land scheidde zich af en werd een aparte staat",
        ],
        0,
        "Een vreedzame machtswissel na verkiezingen was in Congo een primeur.",
    ),
    mk(
        "Wat heeft jouw gsm te maken met de strijd in het oosten van Congo?",
        [
            "Hij bevat kobalt en coltan, grondstoffen die onder meer uit Congo komen",
            "Congo is de grootste olieproducent van de wereld",
            "Rubber uit Congo is nog altijd de belangrijkste grondstof voor banden",
            "Er zijn geen grondstoffen meer, dus is er strijd om de laatste resten",
        ],
        0,
        "Kobalt en coltan: het koloniale verleden zit letterlijk in je telefoon. In Kivu woeden al decennia gewapende conflicten.",
    ),
    tabel(
        "Speelt het mee in de verhouding tussen België en Congo vandaag?",
        [
            ("De teruggave van voorwerpen die in de koloniale tijd zijn meegenomen", J),
            ("De vraag of België officiële excuses moet aanbieden", J),
            ("De band met de grote Congolese gemeenschap in België", J),
            ("De Belgische koning die Congo nog altijd bestuurt", F),
        ],
        "Koning Filip drukte in 2020 zijn diepste spijt uit over de wonden van het koloniale verleden.",
    ),
    casus(
        "Lees de twee uitspraken. Een Belgisch schoolboek uit 1950: België bracht in Congo beschaving, wegen en ziekenhuizen. Een Congolese historicus vandaag: De kolonie werd uitgebaat voor de rijkdom van België, met dwang en geweld.",
        [
            mk(
                "Wat is de beste manier om met deze twee bronnen om te gaan?",
                [
                    "Bekijken wie ze maakte, wanneer en waarom, en vergelijken met andere bronnen",
                    "De oudste bron geloven, want die staat het dichtst bij de feiten",
                    "De nieuwste bron geloven, want nieuwe boeken hebben altijd gelijk",
                    "Beide bronnen weggooien, want ze spreken elkaar tegen en zijn dus allebei vals",
                ],
                0,
                "Elke bron heeft een standplaats. Een tegenspraak is een aanwijzing om verder te zoeken.",
            ),
            keuze(
                "Het schoolboek uit 1950 toont vooral het [[*Belgische|Congolese|Amerikaanse]] perspectief. Wie beide bronnen naast elkaar legt, past de redeneerwijze [[*meerdere perspectieven hanteren|evolutie en revolutie|continuïteit]] toe.",
                "Twee standpunten over hetzelfde verleden: dat is meerdere perspectieven hanteren.",
            ),
            tabel(
                "Is het een voorbeeld van dekolonisering van het denken?",
                [
                    ("Een schoolboek dat ook Congolese stemmen aan het woord laat", J),
                    ("Een les waarin ook de koloniale misdaden aan bod komen", J),
                    ("Het schoolboek van 1950 ongewijzigd opnieuw drukken", F),
                ],
                "Wie andere stemmen toevoegt of de misdaden toont, kijkt opnieuw naar het verleden. Ongewijzigd herdrukken doet dat niet.",
            ),
        ],
    ),
    open_(
        "Geef twee manieren waarop het koloniale verleden de wereld van vandaag nog vormt.",
        "Bijvoorbeeld: de grenzen van Afrikaanse staten zijn door kolonisatoren getrokken en zorgen nog voor conflicten; talen als Frans en Engels worden er nog gesproken; migratie naar de vroegere moederlanden, zoals de Congolese gemeenschap in België; de handel in grondstoffen zoals kobalt en coltan voor onze telefoons.",
    ),
]

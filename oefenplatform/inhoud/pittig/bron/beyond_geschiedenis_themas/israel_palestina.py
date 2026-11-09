"""De Israëlisch-Palestijnse kwestie — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="balfourverklaring.webp", zelf=False,
         wat="De brief van de Britse minister Balfour aan Lord Rothschild van 2 november 1917 (de Balfourverklaring), de scan van het origineel.",
         waar="Wikimedia Commons, zoek op 'Balfour declaration unmarked'. Publiek domein.",
         vragen="bronvraag over de oorsprong van het conflict en wat Groot-Brittannië belooft"),
    dict(bestand="verdelingsplan-1947.webp", zelf=False,
         wat="Kaart van het verdelingsplan van de VN van 1947 (Joodse staat, Arabische staat, Jeruzalem internationaal). Graag een versie zonder veel tekst erop.",
         waar="Wikimedia Commons, zoek op 'UN Partition Plan for Palestine 1947 map'. Stuur me de link als je twijfelt, dan pas ik ze aan zoals bij de kaart van Afrika.",
         vragen="vragen over het plan van 1947: wat kan je met de kaart staven"),
    dict(bestand="oslo-handdruk-1993.webp", zelf=False,
         wat="De foto van de handdruk tussen Rabin en Arafat met Clinton in het midden, Witte Huis, 13 september 1993.",
         waar="Wikimedia Commons, zoek op 'Bill Clinton, Yitzhak Rabin, Yasser Arafat at the White House 1993'. Foto van de Amerikaanse overheid, publiek domein.",
         vragen="bronvraag over de vreedzame fase en de rol van de Verenigde Staten"),
    dict(bestand="tijdlijn-israel-palestina.svg", zelf=True,
         wat="Tijdlijn van 1917 tot vandaag met de gewelddadige en vreedzame fases.",
         vragen="klikvragen op oorlogen, intifada's en akkoorden"),
]

VRAGEN = [
    # ------------------------------------------------ oorsprong
    tabel(
        "Juist of fout? De oorsprong van de Israëlisch-Palestijnse kwestie.",
        [
            ("Palestina hoorde voor de Eerste Wereldoorlog bij het Ottomaanse Rijk.", J),
            ("Na die oorlog kreeg Groot-Brittannië er van de Volkenbond een mandaat over.", J),
            ("Rond 1900 woonden er in Palestina nauwelijks mensen.", F),
            ("Joodse immigranten kochten er grond en stichtten er landbouwkolonies.", J),
        ],
        "Het gebied was wel bewoond, vooral door Arabieren. Door de groeiende Joodse immigratie nam de spanning toe.",
    ),
    met_prent("balfourverklaring.webp", mk(
        "Wat beloofde de Britse regering in deze brief van minister Balfour?",
        [
            "Steun voor een nationaal tehuis voor het Joodse volk in Palestina",
            "Een onafhankelijke Arabische staat in heel het Midden-Oosten",
            "Het einde van alle Britse invloed in het Midden-Oosten na de oorlog",
            "Een verdeling van Palestina tussen Frankrijk en Groot-Brittannië",
        ],
        0,
        "Dat is de Balfourverklaring. Er staat ook in dat de rechten van de niet-Joodse gemeenschappen niet geschaad mogen worden.",
    ), volgt=True),
    keuze(
        "Het [[*zionisme|panarabisme|kolonialisme]] ontstond eind 19de eeuw onder Joden in Europa, mee als reactie op het [[*antisemitisme|liberalisme|imperialisme]]. Theodor [[*Herzl|Balfour|Rothschild]] riep op tot een eigen Joodse staat.",
        "Herzl schreef in 1896 Der Judenstaat. Pogroms in Oost-Europa en de Dreyfusaffaire in Frankrijk toonden dat Joden nergens veilig waren.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar van de Balfourverklaring.",
        "tijdlijn-israel-palestina.svg",
        [[8.6, 25, 2.9, 55]],
        "In november 1917, midden in de Eerste Wereldoorlog, toen de Britten Palestina op de Ottomanen aan het veroveren waren.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de staat Israël werd uitgeroepen.",
        "tijdlijn-israel-palestina.svg",
        [[31.2, 25, 2.9, 55]],
        "Op 14 mei 1948, op de dag dat het Britse mandaat afliep.",
    ),
    sorteer(
        "Waarom groeide de spanning in het Britse mandaatgebied tussen de twee wereldoorlogen en kort erna?",
        ["Joodse kant", "Arabische kant"],
        [
            ["Vluchten voor jodenvervolging in Europa en een eigen veilig land zoeken", "Joodse kant"],
            ["Na de Holocaust overtuigd dat een eigen staat noodzakelijk is", "Joodse kant"],
            ["Vrezen dat de Joodse immigratie hen in eigen land tot minderheid maakt", "Arabische kant"],
            ["Zich bedrogen voelen door Britse beloftes van onafhankelijkheid", "Arabische kant"],
        ],
        "Beide groepen hadden hun redenen en beide voelden zich door de Britten in de steek gelaten. Daarom gaven die het probleem in 1947 door aan de VN.",
    ),
    met_prent("verdelingsplan-1947.webp", tabel(
        "Bekijk de kaart van het VN-plan van 1947. Welke uitspraken kan je met de kaart staven?",
        [
            ("Het gebied wordt verdeeld in een Joodse en een Arabische staat.", J),
            ("Jeruzalem krijgt een aparte, internationale status.", J),
            ("De twee staten vormen elk één aaneengesloten gebied.", F),
            ("Het plan werd door beide partijen aanvaard.", F),
        ],
        "De staten bestaan uit losse stukken die elkaar raken. Dat het plan door de Arabische landen verworpen werd, staat niet op de kaart: dat weet je uit je kennis, niet uit deze bron.",
    ), volgt=True),
    mk(
        "Wat bedoelen Palestijnen met de Nakba, de catastrofe?",
        [
            "De vlucht en verdrijving van Palestijnen bij de stichting van Israël",
            "De nederlaag van het Ottomaanse Rijk in de Eerste Wereldoorlog",
            "De bouw van de muur rond de Westelijke Jordaanoever, vanaf het begin van de 21ste eeuw",
            "Het mislukken van de vredesonderhandelingen van Camp David in 2000",
        ],
        0,
        "Ongeveer 700 000 mensen raakten hun huis kwijt. Voor Israëli's is diezelfde oorlog de onafhankelijkheidsoorlog: dezelfde gebeurtenis, twee herinneringen.",
    ),
    # ------------------------------------------------ gewelddadige fases
    volgorde(
        "Zet de oorlogen en opstanden in de juiste volgorde.",
        [
            "De eerste Arabisch-Israëlische oorlog",
            "De Zesdaagse Oorlog",
            "De Jom Kipoeroorlog",
            "De eerste intifada",
            "De tweede intifada",
        ],
        "Na de eerste oorlog volgden nog twee oorlogen tussen Israël en zijn buurlanden. Daarna kwamen de Palestijnen in de bezette gebieden zelf in opstand, twee keer.",
    ),
    tabel(
        "Juist of fout? De Zesdaagse Oorlog van 1967.",
        [
            ("Israël veroverde de Westelijke Jordaanoever en de Gazastrook.", J),
            ("Ook Oost-Jeruzalem kwam onder Israëlisch gezag.", J),
            ("Israël verloor de oorlog en moest gebied afstaan.", F),
            ("Na de oorlog kwamen veel meer Palestijnen onder Israëlisch bestuur te leven.", J),
        ],
        "Israël won in zes dagen en nam ook de Sinaï van Egypte en de Golanhoogte van Syrië in. De bezette gebieden staan sindsdien centraal in het conflict.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de eerste intifada begon.",
        "tijdlijn-israel-palestina.svg",
        [[59.6, 25, 2.9, 55]],
        "Eind 1987, in de Gazastrook, en daarna ook op de Westelijke Jordaanoever.",
    ),
    mk(
        "Wat bedoelt men met een intifada?",
        [
            "Een Palestijnse volksopstand tegen de Israëlische bezetting",
            "Een vredesakkoord tussen Israël en een Arabisch buurland",
            "Een Israëlische nederzetting in bezet gebied",
            "Een VN-resolutie die een wapenstilstand oplegt",
        ],
        0,
        "Het woord betekent afschudden. De eerste intifada begon met stakingen en jongeren die stenen gooiden, de tweede was veel bloediger, met zelfmoordaanslagen en zware militaire acties.",
    ),
    keuze(
        "In 1964 werd de [[*PLO|Hamas|Likoed]] opgericht, die lang geleid werd door [[*Yasser Arafat|Anwar Sadat|Menachem Begin]]. Tijdens de eerste intifada ontstond ook de islamistische beweging [[*Hamas|PLO|Fatah-Jeugd]].",
        "De PLO was de seculiere koepel van Palestijnse groepen. Hamas is islamistisch en weigerde de vredesakkoorden te erkennen.",
    ),
    # ------------------------------------------------ vreedzame fases
    koppel(
        "Welk akkoord of initiatief hoort bij welke beschrijving?",
        [
            ["Camp David (1978)", "Egypte erkent Israël en krijgt de Sinaï terug"],
            ["Oslo (1993)", "Israël en de PLO erkennen elkaar en er komt een Palestijns zelfbestuur"],
            ["Vredesverdrag met Jordanië (1994)", "Een tweede Arabisch buurland sluit vrede met Israël"],
            ["Arabisch vredesinitiatief (2002)", "Saoedi-Arabië stelt namens de Arabische Liga een vredesplan voor"],
        ],
        ["Een Palestijnse staat met Jeruzalem als hoofdstad wordt een feit"],
        "Een Palestijnse staat met Jeruzalem als hoofdstad is er nooit gekomen.",
    ),
    met_prent("oslo-handdruk-1993.webp", tabel(
        "Juist of fout? Wat zegt deze foto uit 1993?",
        [
            ("De Amerikaanse president staat letterlijk tussen de twee leiders in, als bemiddelaar.", J),
            ("De handdruk is een symbool voor de erkenning van elkaar als gesprekspartner.", J),
            ("De foto bewijst dat het conflict daarna voorbij was.", F),
            ("De foto is bewust zo in scène gezet voor de pers.", J),
        ],
        "Een foto toont een moment, geen afloop. Twee jaar later werd Rabin vermoord door een Israëlische extremist die tegen het akkoord was.",
    ), volgt=True),
    sorteer(
        "Hoort de gebeurtenis bij een gewelddadige of een vreedzame fase?",
        ["Gewelddadig", "Vreedzaam"],
        [
            ["De Jom Kipoeroorlog", "Gewelddadig"],
            ["De oorlog in Libanon in 1982", "Gewelddadig"],
            ["De akkoorden van Camp David", "Vreedzaam"],
            ["De onderhandelingen van Oslo", "Vreedzaam"],
            ["De tweede intifada", "Gewelddadig"],
        ],
        "Het conflict wisselde voortdurend tussen oorlog en onderhandelen. Vaak werden vredespogingen door nieuw geweld onderbroken.",
    ),
    mk(
        "Waarom bracht het vredesproces van Oslo geen blijvende vrede?",
        [
            "Er bleef geweld van extremisten en de moeilijkste punten werden uitgesteld",
            "De Verenigde Staten trokken zich volledig uit het Midden-Oosten terug",
            "De PLO werd kort na de akkoorden door de Verenigde Naties ontbonden en verboden",
            "Egypte en Jordanië verklaarden Israël opnieuw de oorlog",
        ],
        0,
        "De moeilijkste kwesties werden naar later geschoven. Aanslagen en de moord op Rabin ondermijnden het vertrouwen.",
    ),
    # ------------------------------------------------ actuele situatie
    tabel(
        "Juist of fout? De situatie van de laatste jaren.",
        [
            ("Op de Westelijke Jordaanoever wonen honderdduizenden Israëlische kolonisten in nederzettingen.", J),
            ("Sinds 2007 heeft Hamas de macht in de Gazastrook.", J),
            ("Op 7 oktober 2023 viel Hamas Israël aan, waarbij ongeveer 1200 mensen omkwamen en honderden gijzelaars werden meegenomen.", J),
            ("De oorlog die volgde in Gaza bleef beperkt tot enkele honderden doden.", F),
        ],
        "De oorlog in Gaza kostte tienduizenden Palestijnse levens en veroorzaakte een zware humanitaire crisis.",
    ),
    mk(
        "Wat bedoelt men met de tweestatenoplossing?",
        [
            "Een Israëlische en een Palestijnse staat naast elkaar",
            "Eén staat waarin Israëli's en Palestijnen samen stemmen",
            "Israël en Egypte verdelen de Gazastrook onder elkaar",
            "Twee Palestijnse staten, één in Gaza en één in Jordanië",
        ],
        0,
        "Al sinds het VN-plan van 1947 duikt dit idee op, maar het is er nooit van gekomen.",
    ),
    sleep(
        "Tijdens de tweede intifada begon Israël in [[2002]] met de bouw van een [[afscheidingsbarrière]] rond de Westelijke Jordaanoever, die voor een groot deel op [[bezet]] gebied staat.",
        ["1967", "nederzetting", "Egyptisch"],
        "Het Internationaal Gerechtshof oordeelde in 2004 dat de muur, waar hij op bezet gebied staat, in strijd is met het internationaal recht.",
    ),
    # ------------------------------------------------ houding van de Verenigde Staten
    sorteer(
        "Toont deze daad van de Verenigde Staten steun aan Israël of bemiddeling tussen de partijen?",
        ["Steun", "Bemiddeling"],
        [
            ["Elk jaar miljarden dollars aan militaire hulp", "Steun"],
            ["Een veto tegen een resolutie die Israël veroordeelt", "Steun"],
            ["De top van Camp David met de leiders van Egypte en Israël", "Bemiddeling"],
            ["De ondertekening van de Oslo-akkoorden in het Witte Huis", "Bemiddeling"],
        ],
        "De VS zijn tegelijk de belangrijkste bondgenoot van Israël en de vaste bemiddelaar. Dat maakt hun rol omstreden.",
    ),

    mk(
        "De Verenigde Staten steunen Israël, maar bemiddelden ook bij Camp David en Oslo. Hoe rijm je dat?",
        [
            "Rust in de regio dient ook hun eigen belangen",
            "Ze steunden in het geheim vooral de Palestijnse kant",
            "Ze werden door de VN verplicht om te bemiddelen",
            "Ze bemiddelden enkel om Europa uit de regio te houden",
        ],
        0,
        "Stabiliteit, olie en de strijd om invloed maken vrede ook voor Washington belangrijk. Critici vinden de VS daardoor geen neutrale bemiddelaar.",
    ),
    mk(
        "In de Veiligheidsraad gebruiken de Verenigde Staten vaak hun veto bij resoluties die Israël veroordelen. Wat is daarvan het gevolg?",
        [
            "De Veiligheidsraad kan dan geen bindende beslissing nemen",
            "Israël wordt dan automatisch lid van de NAVO",
            "De Algemene Vergadering wordt dan ontbonden",
            "De resolutie geldt dan enkel voor de Palestijnse gebieden",
        ],
        0,
        "Eén veto van een vast lid volstaat om een resolutie tegen te houden. Zo blijft de Veiligheidsraad bij dit conflict vaak machteloos.",
    ),
    # ------------------------------------------------ bronnen en perspectieven
    casus(
        "Een Israëlische krant noemt de afscheidingsbarrière een veiligheidshek dat aanslagen tegenhoudt. Een Palestijnse krant noemt hetzelfde bouwwerk een muur die land inpikt.",
        [
            mk(
                "Welke redeneerwijze heb je nodig om deze twee bronnen goed te gebruiken?",
                ["Meerdere perspectieven hanteren", "Continuïteit benoemen", "Chronologisch ordenen", "Synchroniciteit benoemen"],
                0,
                "Elke kant kijkt naar hetzelfde bouwwerk vanuit de eigen ervaring. Pas samen geven ze een vollediger beeld.",
            ),
            tabel(
                "Juist of fout?",
                [
                    ("Een van beide kranten moet liegen.", F),
                    ("De naam die je aan een gebeurtenis geeft, toont al een standpunt.", J),
                    ("Beide kranten zijn bruikbaar om te onderzoeken hoe elke kant de muur beleeft.", J),
                ],
                "Ze spreken elkaar niet tegen over de feiten, maar wel over de betekenis. Dat is standplaatsgebondenheid.",
            ),
        ],
    ),
    tabel(
        "Waarom is het conflict zo moeilijk op te lossen? Welke punten zijn echte twistpunten bij elke onderhandeling?",
        [
            ("De grenzen van een Palestijnse staat", J),
            ("Het statuut van Jeruzalem, heilig voor joden, christenen en moslims", J),
            ("De terugkeer van de vluchtelingen van 1948 en hun nakomelingen", J),
            ("De officiële taal van de Verenigde Naties", F),
        ],
        "Grenzen, Jeruzalem, vluchtelingen, nederzettingen en veiligheid zijn telkens de struikelblokken.",
    ),
    mk(
        "Een krant schrijft: het conflict gaat al tweeduizend jaar terug. Waarom is dat historisch misleidend?",
        [
            "Het is vooral een moderne strijd om land",
            "Tweeduizend jaar geleden woonden er nog geen mensen in die streek",
            "Het conflict begon pas echt met de aanval van Hamas in 2023",
            "Joden en moslims hebben in het verleden nooit vreedzaam samengeleefd",
        ],
        0,
        "Religie speelt mee, maar het is in de eerste plaats een strijd tussen twee nationale bewegingen van de 19de en 20ste eeuw om hetzelfde land.",
    ),
    open_(
        "Geef een historische verklaring voor de houding van de Verenigde Staten tegenover het conflict tussen Israël en Palestina. Gebruik minstens twee argumenten.",
        "Bijvoorbeeld: tijdens de Koude Oorlog was Israël een belangrijke bondgenoot tegen Arabische staten die door de Sovjet-Unie gesteund werden. In de Verenigde Staten zelf hebben de Joodse gemeenschap en een pro-Israëlische lobby veel invloed, en veel Amerikanen zien Israël als een democratie met gedeelde waarden. Daarom krijgt Israël militaire steun en gebruiken de VS hun veto in de Veiligheidsraad. Tegelijk willen de VS rust in de regio en bemiddelden ze bij Camp David en Oslo.",
    ),
    mk(
        "Na de oorlog van 1967 vroeg VN-resolutie 242 land voor vrede. Wat betekent dat?",
        [
            "Israël geeft bezet gebied terug, de buurlanden erkennen Israël",
            "Israël koopt het bezette gebied van de buurlanden af tegen een vaste prijs",
            "De VN nemen de bezette gebieden voor altijd zelf in bestuur",
            "Elk land behoudt wat het in de oorlog veroverd heeft, zonder verdere eisen",
        ],
        0,
        "Grond in ruil voor erkenning en veilige grenzen. Dat principe zit in bijna elk later vredesplan.",
    ),
    mk(
        "Welk gevolg had de Jom Kipoeroorlog van 1973 voor Europa?",
        [
            "Arabische olielanden beperkten de olie-uitvoer: er kwam een oliecrisis",
            "Europese landen stuurden samen een groot leger naar het Midden-Oosten",
            "Europa erkende Israël pas na deze oorlog als een volwaardige staat",
            "De Europese Gemeenschap viel uiteen door ruzie over de oorlog",
        ],
        0,
        "De olie werd een politiek wapen tegen landen die Israël steunden. In België kwamen er onder meer autoloze zondagen.",
    ),


]

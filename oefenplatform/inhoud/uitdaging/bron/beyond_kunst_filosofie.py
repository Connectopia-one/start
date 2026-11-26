# -*- coding: utf-8 -*-
"""Uitdaging Kunstbeschouwing en filosofie 🌍 Beyond (26 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die kunstbeschouwing
en filosofie door elkaar halen. Casussen, tabellen, keuzelijsten, koppelen,
sorteren, volgorde, sleepzinnen en een open vraag. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Kunstbeschouwing en filosofie Beyond.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

NIVEAU = "beyond-doorstroom"
VAK = "Kunstbeschouwing en filosofie"
BESTAND = "beyond-kunst-filosofie-uitdaging.json"
AANTAL = 40

VRAGEN = [
    # Kunstvormen en middelen
    tabel(
        "Een museum plant een tentoonstelling. Bij welke kunstvorm hoort elk onderdeel?",
        [
            ("Een zaal vol zwart-witfoto's van havenarbeiders", "Audiovisuele kunsten"),
            ("Een kamer waarin bezoekers tussen hangende spiegels en geluid lopen", "Installatiekunst"),
            ("Een kaartje met de zin: stel je een blauwe zaal voor", "Conceptuele kunst"),
            ("Een bronzen beeld van een danser", "Beeldende kunsten"),
        ],
        "Fotografie hoort bij de audiovisuele kunsten. Bij installatiekunst is de ruimte het werk, bij conceptuele kunst het idee.",
        kolommen=["Audiovisuele kunsten", "Beeldende kunsten", "Installatiekunst", "Conceptuele kunst"]),
    sorteer(
        "Een recensent schrijft over een voorstelling. Bij welke kunstvorm hoort de bouwsteen die hij beschrijft?",
        ["Dans", "Muziek", "Media"],
        [
            ["De dansers bewegen eerst slap, dan hoekig en krachtig.", "Dans"],
            ["Twee dansers bewegen exact gelijk, de derde net niet.", "Dans"],
            ["De cello neemt de melodie over van de viool.", "Muziek"],
            ["Het orkest zwelt aan tot een oorverdovend slot.", "Muziek"],
            ["De film springt zonder overgang van de straat naar de keuken.", "Media"],
            ["We zien het gebouw van onderen, zodat het dreigend lijkt.", "Media"],
        ],
        "Kracht en relatie zijn bouwstenen van dans, klankkleur en dynamiek van muziek, montage en kader van media."),
    keuze(
        "Een beeldhouwer giet een beeld in brons. Brons is het [[*materiaal|techniek|bouwsteen]], gieten in een mal is de [[*techniek|materiaal|context]]. Wie het beeld bestelde, hoort bij de [[*context|vormgeving|bouwstenen]].",
        "Materiaal is waarmee je werkt, techniek is hoe. De opdrachtgever is geen middel van vormgeving, maar hoort bij de context."),
    mk("Een filmmaker wil dat een personage klein en verloren lijkt. Welk kader past daar het best bij?",
       ["een close-up vanuit een laag kikkerperspectief", "een long shot vanuit vogelperspectief",
        "een medium shot op ooghoogte", "een close-up op ooghoogte"], 1,
       "In een long shot zie je de figuur klein in een grote ruimte. Vanuit vogelperspectief kijk je op iemand neer, wat hem nog kleiner doet lijken."),

    # Inhoud, functie, context
    casus(
        "Een schilder maakt in 1937 een enorm doek over het bombardement op een Spaans stadje tijdens de burgeroorlog. Hij gebruikt enkel zwart, wit en grijs, en schildert gebroken lichamen en een schreeuwend paard. Het werk hangt eerst in het Spaanse paviljoen op de wereldtentoonstelling in Parijs.",
        [
            mk("Welke functie staat hier voorop?",
               ["decoratief en versierend", "maatschappijkritisch", "economisch, om te verkopen", "ontspannend en vrolijk"], 1,
               "Het werk klaagt de gruwel van de oorlog aan."),
            tabel("Over welk deel van de context gaat het?",
                  [("geschilderd in 1937", "Tijd"),
                   ("voor het Spaanse paviljoen in Parijs", "Ruimte"),
                   ("tijdens de Spaanse Burgeroorlog", "Politiek")],
                  "Het jaartal is de tijd, de plaats waarvoor het gemaakt werd de ruimte, de oorlog de politieke context.",
                  kolommen=["Tijd", "Ruimte", "Politiek"]),
            mk("Hoe verklaart de functie hier de vormgeving?",
               ["vrolijke kleuren zouden de pijn voor de kijker draaglijker maken",
                "sombere kleuren en gebroken vormen versterken de aanklacht",
                "het grote formaat moest het werk op de kunstmarkt duurder maken",
                "het grijs was goedkoper dan andere verf in oorlogstijd"], 1,
               "De context verklaart de functie en de functie verklaart de vormgeving: wie gruwel wil aanklagen, kiest voor sombere kleuren en gebroken vormen."),
        ]),
    tabel(
        "Welke functie staat voorop bij deze werken?",
        [
            ("Een tapijt dat een kasteelzaal mooier maakt", "Decoratief"),
            ("Een reeks beeldjes die meteen online verkocht wordt", "Economisch"),
            ("Een standbeeld dat de macht van een vorst toont", "Politiek"),
            ("Een werk dat doet nadenken over de dood", "Filosofisch"),
        ],
        "Versieren is decoratief, geld opbrengen economisch, macht tonen politiek, doen nadenken over grote vragen filosofisch.",
        kolommen=["Decoratief", "Economisch", "Politiek", "Filosofisch"]),

    # Kunstgeschiedenis
    volgorde(
        "Zet deze werken of gebouwen in de juiste volgorde, van oud naar recent.",
        ["de grotschilderingen van Lascaux", "de piramiden van Gizeh", "het Parthenon", "het Pantheon",
         "de kathedraal van Chartres", "het Lam Gods"],
        "Prehistorie, Egypte, Griekenland, Rome, gotiek en dan de Vlaamse primitieven in de 15de eeuw."),
    volgorde(
        "Zet deze stromingen in de juiste volgorde, van oud naar recent.",
        ["neoclassicisme", "romantiek", "impressionisme", "kubisme", "surrealisme", "popart"],
        "Het neoclassicisme en de romantiek horen rond 1800, het impressionisme in de tweede helft van de 19de eeuw, het kubisme rond 1907, het surrealisme na de Eerste Wereldoorlog en de popart na 1950."),
    koppel(
        "Koppel de kunstenaar aan het kenmerk dat in zijn werk opvalt.",
        [
            ["Leonardo da Vinci", "sfumato"],
            ["Caravaggio", "hard contrast tussen licht en donker"],
            ["Van Eyck", "olieverf in dunne lagen"],
            ["Polykleitos", "contrapposto"],
            ["Pollock", "drip painting"],
        ],
        ["readymade", "aspectief"],
        "Een readymade hoort bij Duchamp, aspectief bij de Egyptische kunst."),
    keuze(
        "Een beeld staat met het gewicht op één been en de heupen schuin: dat is [[*contrapposto|aspectief|sfumato]]. Een Romeins borstbeeld daarentegen toont rimpels en eigen trekken, omdat de Romeinen vooral [[*realistische|geïdealiseerde|abstracte]] portretten maakten.",
        "Contrapposto is typisch voor klassieke Griekse beelden. Romeinse portretten waren realistisch."),
    casus(
        "Je bezoekt een kerk. Ze is hoog en licht, met grote glasramen en een roosvenster. Aan de buitenkant zie je bogen die tegen de muren steunen. Binnen hangt een veelluik uit de 15de eeuw met heel fijn geschilderde stoffen en juwelen.",
        [
            keuze("De kerk is [[*gotisch|romaans|barok]]. De bogen buiten heten [[*luchtbogen|rondbogen|hoefijzerbogen]].",
                  "Hoogte, licht en luchtbogen zijn typisch voor de gotiek."),
            mk("Waarom konden de muren zoveel glas bevatten?",
               ["de muren waren veel dikker dan in een romaanse kerk",
                "de bogen buiten vingen de druk van het gewelf op",
                "het dak was van licht hout in plaats van zware steen",
                "er stonden zuilen in het midden van de ramen"], 1,
               "Luchtbogen en steunberen dragen een deel van het gewicht. Zo hoeft de muur niet alles te dragen."),
            mk("Het veelluik hoort bij de Vlaamse primitieven. Wat betekent primitief hier?",
               ["ongeschoold, eenvoudig en nog zonder echte techniek",
                "de eersten van een nieuwe schilderkunst",
                "geschilderd met natuurlijke pigmenten",
                "gemaakt zonder een rijke opdrachtgever"], 1,
               "Primitief verwijst naar de eersten, niet naar een gebrek aan kunde."),
        ]),
    tabel(
        "Renaissance of barok?",
        [
            ("Figuren in een rustige, symmetrische opstelling", "Renaissance"),
            ("Een diagonale compositie vol beweging", "Barok"),
            ("Diepte met één verdwijnpunt", "Renaissance"),
            ("Gemaakt om gelovigen te ontroeren na de reformatie", "Barok"),
        ],
        "Rust en perspectief horen bij de renaissance. Beweging, emotie en de contrareformatie bij de barok.",
        kolommen=["Renaissance", "Barok"]),
    sleep(
        "De [[romantiek]] reageerde op de rede van het neoclassicisme met gevoel en natuur. Het [[realisme]] toonde daarna het gewone leven zonder mooimakerij. Het [[dadaïsme]] protesteerde tegen de oorlog en tegen de kunst zelf.",
        ["surrealisme", "fauvisme"],
        "Elke stroming kan je lezen als een reactie op wat eraan voorafging."),
    tabel(
        "Welke niet-westerse invloed herken je?",
        [
            ("Vlakke kleurvlakken, sterke contouren, een afgesneden beeld", "Japanse houtsneden"),
            ("Hoekige, maskerachtige gezichten in een kubistisch werk", "Afrikaanse beelden"),
            ("Geometrische sterpatronen zonder mensfiguren", "Islamitische kunst"),
        ],
        "Japanse prenten beïnvloedden Van Gogh en Monet, Afrikaanse beelden Picasso, islamitische patronen o.a. Matisse.",
        kolommen=["Japanse houtsneden", "Afrikaanse beelden", "Islamitische kunst"]),
    mk("Een klasgenoot zegt: een Afrikaans masker in een Europees museum toont gewoon primitieve kunst. Wat is de sterkste kritiek daarop?",
       ["het masker is veel te oud om vandaag nog iets te betekenen voor wie het bekijkt",
        "musea mogen volgens de wet geen religieuze maskers tonen",
        "het had een eigen betekenis en kwam vaak via kolonisatie hier",
        "maskers horen bij de podiumkunsten en dus niet in een museum"], 2,
       "Westerse kunstenaars en musea kenden de betekenis vaak niet, en veel voorwerpen kwamen via de koloniale overheersing naar Europa."),

    # Analyse
    volgorde(
        "Zet de stappen van een kunstanalyse in de goede volgorde.",
        ["beschrijven wat je ziet", "de vormgeving bekijken", "de context zoeken", "functie en betekenis bepalen", "je eigen oordeel geven"],
        "Eerst kijken en beschrijven, pas op het einde oordelen, en dat oordeel steunen op wat je zag."),
    tabel(
        "Vanuit welk perspectief kijkt deze bezoeker naar het werk?",
        [
            ("Dit was het eerste schilderij met zo'n perspectief.", "Historisch"),
            ("De compositie is mooi in evenwicht.", "Vormelijk"),
            ("Het werk doet me aan mijn opa denken.", "Persoonlijk"),
            ("Het werk zet ons aan het denken over armoede.", "Maatschappelijk"),
        ],
        "Wat nieuw was voor zijn tijd is historisch, hoe het gemaakt is vormelijk, wat het bij jou oproept persoonlijk, wat het over de samenleving zegt maatschappelijk.",
        kolommen=["Vormelijk", "Historisch", "Maatschappelijk", "Persoonlijk"]),
    open_("Je ziet een ongekend schilderij: een fabriekshal, uitgeputte arbeiders, bruine en grijze tinten, geschilderd rond 1850. Analyseer het kort: stroming, functie en één kenmerk van de vormgeving.",
          "Het past bij het realisme: het gewone, zware leven zonder mooimakerij. De functie is maatschappijkritisch. De sombere bruine en grijze tinten versterken de uitputting.",
          "Steun elke bewering op iets wat je in het werk ziet."),

    # Filosofie
    koppel(
        "Koppel de filosoof aan zijn beeld of uitspraak.",
        [
            ["Heraclitus", "je stapt nooit twee keer in dezelfde rivier"],
            ["Plato", "gevangenen in een grot zien enkel schaduwen"],
            ["Aristoteles", "een eikel is in mogelijkheid een eik"],
            ["Camus", "we moeten ons Sisyphus gelukkig voorstellen"],
            ["Sartre", "het bestaan gaat vooraf aan de essentie"],
        ],
        ["God of de natuur", "these, antithese, synthese"],
        "God of de natuur is van Spinoza, these-antithese-synthese van Hegel."),
    mk("Hume ziet de zon elke ochtend opkomen. Wat zegt hij over de verwachting dat ze morgen weer opkomt?",
       ["ze is met het verstand logisch en zeker bewezen",
        "ze steunt op gewoonte, niet op een waargenomen oorzaak",
        "ze is aangeboren kennis die iedereen al bij de geboorte heeft",
        "ze is onmogelijk omdat alles stroomt"], 1,
       "Volgens Hume zien we enkel dat dingen na elkaar komen. Dat het ene het andere veroorzaakt, is een gewoonte van onze geest."),
    keuze(
        "Kant zegt dat we de dingen enkel kennen zoals ze aan ons [[*verschijnen|zijn|werken]]. Het ding op zich blijft voor ons [[*onkenbaar|zichtbaar|veranderlijk]].",
        "Kant onderscheidt het fenomeen van het ding op zich."),
    tabel(
        "Welke ethische benadering spreekt hier?",
        [
            ("Kies wat het meeste geluk oplevert voor de meeste mensen.", "Gevolgenethiek"),
            ("Liegen mag nooit, ook niet om iemand te sparen.", "Plichtethiek"),
            ("Wat zou een moedig en eerlijk mens doen?", "Deugdethiek"),
            ("Vertrek van wie kwetsbaar is en van jou afhangt.", "Zorgethiek"),
        ],
        "Gevolgen, plicht, deugd en zorg zijn de vier benaderingen.",
        kolommen=["Gevolgenethiek", "Plichtethiek", "Deugdethiek", "Zorgethiek"]),
    sorteer(
        "Rationalisme of empirisme?",
        ["Rationalisme", "Empirisme"],
        [
            ["Descartes", "Rationalisme"],
            ["ik denk, dus ik ben", "Rationalisme"],
            ["Locke", "Empirisme"],
            ["de geest is bij de geboorte een onbeschreven blad", "Empirisme"],
            ["Hume", "Empirisme"],
        ],
        "Rationalisten zoeken zekere kennis in het verstand, empiristen in de ervaring."),
    mk("Iemand zegt: mijn horoscoop klopt altijd, wat er ook gebeurt. Waarom is dat volgens Popper geen wetenschap?",
       ["omdat geen enkele waarneming het kan weerleggen",
        "omdat het nooit in een echt labo getest werd",
        "omdat te weinig mensen erin geloven",
        "omdat de sterren veel te ver weg staan om ze te meten"], 0,
       "Een wetenschappelijke uitspraak moet falsifieerbaar zijn: je moet kunnen zeggen welke waarneming haar zou weerleggen."),
    tabel(
        "Welke drogreden zit hierin?",
        [
            ("Je mag niet over gezond eten praten, je eet zelf chips.", "Jij-bak"),
            ("Het is natuurlijk, dus het is goed.", "Beroep op de natuur"),
            ("Iedereen doet het, dus het mag.", "Beroep op de massa"),
        ],
        "Een jij-bak valt de persoon aan in plaats van het argument. Natuurlijk of populair is nog niet goed of waar.",
        kolommen=["Jij-bak", "Beroep op de natuur", "Beroep op de massa"]),
    mk("Een robot schrijft een gedicht dat lezers ontroert. Welke vraag hoort het meest bij het thema mens, dier en machine?",
       ["is creativiteit exclusief menselijk?",
        "wie is de opdrachtgever van het gedicht?",
        "welk rijmschema gebruikte de robot?",
        "hoeveel kost zo'n robot?"], 0,
       "Bij mens, dier en machine vraag je wat exclusief menselijk is: denken, voelen, scheppen?"),

    # Politieke filosofie
    casus(
        "Een gemeente wil een nieuw zwembad. Er is geld voor één project. Drie inwoners reageren. Inwoner A: de gemeente moet vooral mijn eigendom beschermen en zich niet met vrije tijd bemoeien. Inwoner B: het zwembad mag enkel als ook de armste gezinnen er toegang toe krijgen. Inwoner C: het zwembad is de plek waar onze dorpsgemeenschap samenkomt en tradities doorgeeft.",
        [
            tabel("Bij welke visie past elke inwoner het best?",
                  [("Inwoner A", "Liberalisme"),
                   ("Inwoner B", "Egalitair liberalisme"),
                   ("Inwoner C", "Communitarisme")],
                  "A legt de nadruk op eigen rechten en een beperkte staat, B op het verschilprincipe van Rawls, C op de gemeenschap.",
                  kolommen=["Liberalisme", "Egalitair liberalisme", "Communitarisme", "Socialisme"]),
            mk("Inwoner B redeneert achter een sluier van onwetendheid. Wat betekent dat?",
               ["hij weet niet hoeveel het nieuwe zwembad uiteindelijk zal kosten",
                "hij kiest zonder te weten waar hij zelf zou staan",
                "hij verbergt zijn mening voor de anderen",
                "hij laat de keuze volledig over aan wie het meeste geld betaalt"], 1,
               "Wie niet weet of hij rijk of arm wordt, kiest regels die ook de zwaksten beschermen."),
        ]),
    tabel(
        "Wie zegt het?",
        [
            ("Zonder staat is het leven een oorlog van allen tegen allen.", "Hobbes"),
            ("Het volk mag een regering die de rechten schendt afzetten.", "Locke"),
            ("Samen worden we vrij door de algemene wil te volgen.", "Rousseau"),
            ("Soeverein is wie beslist over de uitzonderingstoestand.", "Schmitt"),
        ],
        "Hobbes: Leviathan. Locke: natuurlijke rechten. Rousseau: algemene wil. Schmitt: uitzonderingstoestand.",
        kolommen=["Hobbes", "Locke", "Rousseau", "Schmitt"]),
    keuze(
        "Volgens Mill mag de staat een volwassene niet verbieden om te [[*roken in zijn eigen tuin|rijden zonder rijbewijs|lawaai te maken 's nachts]], want dat schaadt enkel hemzelf. Dat heet het [[*schadebeginsel|verschilprincipe|sociaal contract]].",
        "De staat mag vrijheid enkel beperken om schade aan anderen te voorkomen."),
    tabel(
        "Negatieve of positieve vrijheid volgens Berlin?",
        [
            ("Niemand verbiedt je om te studeren.", "Negatieve vrijheid"),
            ("Je hebt genoeg geld en steun om echt te kunnen studeren.", "Positieve vrijheid"),
            ("De overheid censureert geen kranten.", "Negatieve vrijheid"),
        ],
        "Vrij van inmenging is negatief, vrij om je leven echt zelf te sturen is positief.",
        kolommen=["Negatieve vrijheid", "Positieve vrijheid"]),
    mk("Een topmanager laat de zorg voor zijn kinderen en zijn huis volledig over aan slecht betaalde krachten en denkt er nooit over na. Hoe noemt Tronto dat?",
       ["de algemene wil van de gemeenschap",
        "bevoorrechte onverantwoordelijkheid",
        "kwade trouw zoals Sartre ze beschrijft",
        "herstellende rechtvaardigheid"], 1,
       "Wie macht heeft, kan zorg doorschuiven naar anderen en er niet over nadenken. Daarom wil Tronto zorg politiek maken."),
    mk("Waar toont vrijheid zich volgens Arendt het sterkst?",
       ["in het bezit van zoveel mogelijk eigendom en geld",
        "in samen spreken en handelen in het publieke leven",
        "in je volledig terugtrekken uit de politiek en het openbare leven",
        "in het gehoorzamen aan een sterke leider"], 1,
       "Voor Arendt is vrijheid iets wat je samen met anderen doet, in het openbaar. Totalitarisme vernietigt net die ruimte."),

    # Kunst en filosofie samen
    mk("Een schilder uit de romantiek toont een kleine figuur voor een woeste, mistige zee. Welk idee uit de filosofie sluit daar het dichtst bij aan?",
       ["de mens die zich klein voelt tegenover een overweldigende natuur",
        "de staat als Leviathan die vrede brengt",
        "kennis die enkel uit het verstand komt",
        "ongelijkheid die de zwaksten moet helpen vooruit"], 0,
       "De romantiek zette gevoel en de overweldigende natuur voorop, tegenover de koele rede van het neoclassicisme."),
    mk("Een kunstenaar zet een gewoon fietswiel op een krukje en noemt het kunst. Welke filosofische vraag roept dat het sterkst op?",
       ["wie beslist wat kunst is?",
        "is de mens van nature goed?",
        "bestaat er een ding op zich?",
        "mag de staat vrijheid beperken?"], 0,
       "Readymades doen nadenken over wat kunst is en wie dat beslist: de kunstenaar, het museum of het publiek."),
    tabel(
        "Klopt dit?",
        [
            ("Plato zoekt het echte buiten de dingen, Aristoteles in de dingen zelf.", J),
            ("Parmenides vond verandering echt en het zijn schijn.", F),
            ("Bij Sartre heeft de mens vooraf een vaste natuur.", F),
            ("Spinoza zag geest en lichaam als twee kanten van één substantie.", J),
        ],
        "Parmenides vond net het zijn echt en verandering schijn. Sartre zegt dat de mens zichzelf maakt."),
]

"""De Tweede Wereldoorlog en de Holocaust — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="kazerne-dossin.webp", zelf=False,
         wat="Foto van de Dossinkazerne in Mechelen (vandaag Kazerne Dossin).",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over de deportatie uit België"),
]

VRAGEN = [
    # --- verloop
    tabel(
        "Eerste of Tweede Wereldoorlog?",
        [
            ("Een oorlog van beweging met tanks en vliegtuigen", "Tweede"),
            ("Maanden in loopgraven zonder veel te vorderen", "Eerste"),
            ("Het front blijft vier jaar aan de IJzer steken", "Eerste"),
            ("De Belgische veldtocht duurt achttien dagen", "Tweede"),
            ("Atoombommen op twee steden", "Tweede"),
        ],
        "De eerste oorlog was een loopgravenoorlog, de tweede een blitzkrieg en een oorlog van beweging.",
        kolommen=["Eerste", "Tweede"],
    ),
    volgorde(
        "Zet de gebeurtenissen in chronologische volgorde.",
        ["De inval in Polen", "De inval in België", "De inval in de Sovjet-Unie", "Pearl Harbor", "D-day", "De atoombommen op Japan"],
        "September 1939, 10 mei 1940, juni 1941, december 1941, 6 juni 1944 en augustus 1945.",
    ),
    mk(
        "In juni 1941 viel Duitsland de Sovjet-Unie binnen. Waarom is dat opvallend?",
        [
            "Het verbrak daarmee zijn eigen pact",
            "De Sovjet-Unie was een bondgenoot van de Verenigde Staten",
            "Het was de eerste keer dat Duitsland een land aanviel",
            "De Sovjet-Unie had Duitsland al in 1939 aangevallen",
        ],
        0,
        "In augustus 1939 hadden ze beloofd elkaar niet aan te vallen.",
    ),
    tabel(
        "Welke gebeurtenissen keerden het tij in het voordeel van de Geallieerden?",
        [
            ("De slag om Stalingrad", J),
            ("De Amerikanen kwamen na Pearl Harbor in de oorlog.", J),
            ("De landing in Normandië", J),
            ("De Belgische veldtocht van achttien dagen", F),
        ],
        "Stalingrad was het keerpunt aan het oostfront. Met de VS erbij en D-day kwam de bevrijding van het westen.",
    ),
    tabel(
        "Een leerling vergelijkt mei 1940 met augustus 1914. Wat zegt hij terecht?",
        [
            ("Beide keren had België zich neutraal verklaard.", J),
            ("Beide keren hielp de neutraliteit niet.", J),
            ("Beide keren hield het leger vier jaar stand aan de IJzer.", F),
            ("Beide keren bleef de regering in Brussel.", F),
        ],
        "In 1940 duurde de veldtocht achttien dagen. De regering week uit naar Londen, de koning bleef.",
    ),
    mk(
        "Waaruit groeide na de oorlog de koningskwestie?",
        [
            "Koning en regering kozen een andere weg",
            "De koning vluchtte naar Amerika en weigerde terug te komen",
            "De regering wilde zelf een nieuwe koning uit Duitsland",
            "De koning tekende het Verdrag van Versailles",
        ],
        0,
        "De koning bleef in het bezette land, de regering week uit naar Londen. Die breuk werd na de oorlog de koningskwestie.",
    ),
    tabel(
        "Hoe werd de burgerbevolking een doelwit?",
        [
            ("Steden werden gebombardeerd.", J),
            ("Antwerpen kreeg honderden V-bommen te verwerken.", J),
            ("Mensen werden vervolgd en gedeporteerd.", J),
            ("Enkel soldaten aan het front liepen gevaar.", F),
        ],
        "Bombardementen, honger en vervolging troffen gewone mensen.",
    ),
    keuze(
        "Het grootste deel van België werd bevrijd in [[*september 1944|mei 1945|juni 1944]]. In december volgde nog het [[*Ardennenoffensief|IJzerfront|Blitzkrieg-offensief]].",
        "Na D-day in juni kwam de bevrijding in september, maar in de Ardennen sloeg het Duitse leger nog terug.",
    ),
    # --- bezet België
    sorteer(
        "Collaboratie, verzet of geen van beide?",
        ["Collaboratie", "Verzet", "Geen van beide"],
        [
            ["een spoorlijn opblazen voor een Duitse trein", "Verzet"],
            ["een sluikblad drukken", "Verzet"],
            ["vrijwillig voor de bezetter werken als verklikker", "Collaboratie"],
            ["proberen rond te komen met de bonnen en zwijgen", "Geen van beide"],
        ],
        "De meeste mensen deden geen van beide: zij probeerden de oorlog door te komen.",
    ),
    casus(
        "Jan is in 1943 twintig jaar. Hij krijgt een brief: hij moet in een fabriek in Duitsland gaan werken. Hij weigert en duikt onder bij een boer in de Ardennen. Daar komt hij in contact met een verzetsgroep.",
        [
            inv(
                "Hoe noem je de maatregel waardoor Jan in Duitsland moest gaan werken?",
                ["de verplichte tewerkstelling", "verplichte tewerkstelling", "verplichte arbeid", "dwangarbeid"],
                "Belgen werden gedwongen in Duitsland te werken.",
            ),
            mk(
                "Waarom kwamen onderduikers zoals Jan vaak bij het verzet terecht?",
                [
                    "Ze leefden al buiten de wet en hadden hulp nodig",
                    "De bezetter stuurde hen zelf naar het verzet",
                    "Het verzet betaalde een hoog loon aan iedereen",
                    "Het verzet was een officiële afdeling van het leger",
                ],
                0,
                "Wie ondergedoken was, had valse papieren, eten en een schuilplaats nodig. Dat bracht hen in contact met het verzet.",
            ),
        ],
    ),
    mk(
        "Waarom gebeurde het verzet in het geheim?",
        [
            "Er was geen vrije pers of rechter meer",
            "Het verzet was verboden door de Belgische grondwet",
            "De Geallieerden wilden niet dat iemand het wist",
            "Het verzet bestond enkel uit buitenlanders",
        ],
        0,
        "Onder de bezetting kon je niet stemmen, niet vrij schrijven en niet naar de rechter stappen.",
    ),
    # --- Holocaust
    volgorde(
        "Zet de stappen van de vervolging van de Joden in de juiste volgorde.",
        ["Uitsluiting bij wet met de Neurenberger wetten", "Verplichte kentekens en registratie", "Opsluiting in getto's", "De conferentie in Wannsee", "Deportatie naar vernietigingskampen"],
        "De vervolging begon met uitsluiting bij wet, nog voor de oorlog, en eindigde in de georganiseerde vernietiging.",
    ),
    tabel(
        "Concentratiekamp of vernietigingskamp?",
        [
            ("Ingericht om mensen te doden", "Vernietigingskamp"),
            ("Gevangenen moeten er dwangarbeid doen", "Concentratiekamp"),
            ("Lag in bezet Polen, zoals Auschwitz-Birkenau", "Vernietigingskamp"),
        ],
        "Een vernietigingskamp was voor het doden ingericht. Die kampen lagen in bezet Polen.",
        kolommen=["Concentratiekamp", "Vernietigingskamp"],
    ),
    mk(
        "Waarom zegt men dat de Holocaust niet het werk van enkele individuen was?",
        [
            "Er waren treinen en ambtenaren voor nodig",
            "Hitler voerde alle deportaties zelf uit",
            "Alleen de geheime politie wist ervan",
            "Hij werd georganiseerd door de Volkenbond",
        ],
        0,
        "Een staat plande de vernietiging. Daarvoor waren verordeningen, lijsten, treinen en veel uitvoerders nodig.",
    ),
    casus(
        "Bekijk de foto van de Dossinkazerne in Mechelen. Vandaag is het een herinneringsplaats en museum: Kazerne Dossin.",
        [
            met_prent("kazerne-dossin.webp", mk(
                "Welke rol speelde dit gebouw tijdens de oorlog?",
                [
                    "Een verzamelkamp voor deportatie",
                    "Het hoofdkwartier van het Belgische verzet",
                    "De plaats van het proces van Neurenberg",
                    "Een ziekenhuis voor Geallieerde soldaten",
                ],
                0,
                "Uit de Dossinkazerne werden de Joden uit België gedeporteerd.",
            ), volgt=True),
            tabel(
                "Welke uitspraken over de deportatie uit België kloppen?",
                [
                    ("Meer dan vijfentwintigduizend mensen werden gedeporteerd.", J),
                    ("Slechts een kleine minderheid overleefde de oorlog.", J),
                    ("Er werden uit België geen Joden gedeporteerd.", F),
                ],
                "Ook uit België vertrokken de treinen naar de vernietigingskampen.",
            ),
        ],
    ),
    tabel(
        "Welke middelen gebruikten helpers om Joodse kinderen in bezet België te redden?",
        [
            ("Ze werden ondergebracht bij gezinnen.", J),
            ("Ze werden verborgen in kloosters en instellingen.", J),
            ("Ze kregen vervalste papieren.", J),
            ("De bezetter liet hen vrij naar Amerika reizen.", F),
        ],
        "Israël eert de mensen die met gevaar voor hun leven hielpen als rechtvaardigen onder de volkeren.",
    ),
    mk(
        "Hoe noemt Israël mensen die tijdens de oorlog met gevaar voor eigen leven Joden hielpen?",
        [
            "Rechtvaardigen onder de volkeren",
            "Helden van het IJzerfront",
            "Activisten van de bezetter",
            "Bewakers van de getto's",
        ],
        0,
        "Ook in België waren er zulke mensen. Niet iedereen keek weg.",
    ),
    tabel(
        "Welke groepen werden naast de Joden door het naziregime vervolgd?",
        [
            ("Roma en Sinti", J),
            ("Mensen met een handicap", J),
            ("Homoseksuelen", J),
            ("Politieke tegenstanders en Jehova's getuigen", J),
            ("Alle leden van de nazipartij", F),
        ],
        "De vervolging trof veel groepen. De Holocaust gaat over de systematische vernietiging van de Joden van Europa.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Een afgesloten wijk waar Joden gedwongen moesten wonen", "Getto"],
            ["Het opzettelijk uitroeien van een volk of groep", "Genocide"],
            ["Samenwerken met de bezetter", "Collaboratie"],
            ["Een snelle aanval met tanks en vliegtuigen", "Blitzkrieg"],
        ],
        ["Appeasement", "Repressie"],
        "Repressie is de bestraffing van de collaboratie na de oorlog. Appeasement hoort bij de jaren voor 1939.",
    ),
    # --- na de oorlog
    mk(
        "Wat was nieuw aan de processen van Neurenberg?",
        [
            "Leiders werden berecht voor misdaden tegen de menselijkheid",
            "Het was de eerste keer dat een oorlog eindigde met een verdrag",
            "De Volkenbond sprak er zijn eerste vonnis uit",
            "Duitsland mocht er de voorwaarden van de vrede bepalen",
        ],
        0,
        "Dat begrip werd pas na de Tweede Wereldoorlog in het recht opgenomen.",
    ),
    sorteer(
        "Hoort het bij de Eerste of bij de Tweede Wereldoorlog?",
        ["Na de Eerste", "Na de Tweede"],
        [
            ["de Volkenbond", "Na de Eerste"],
            ["het Verdrag van Versailles", "Na de Eerste"],
            ["de Verenigde Naties", "Na de Tweede"],
            ["de Universele Verklaring van de Rechten van de Mens", "Na de Tweede"],
            ["de processen van Neurenberg", "Na de Tweede"],
        ],
        "De Volkenbond en Versailles horen bij de vorige oorlog. In 1945 kwamen de VN, in 1948 de Universele Verklaring.",
    ),
    casus(
        "Een vrouw vertelt in 2005 hoe ze als meisje van veertien in 1944 in Auschwitz aankwam: de kou, het lawaai, de scheiding van haar moeder op het perron.",
        [
            mk(
                "Hoe ga je als historicus met deze getuigenis om?",
                [
                    "Als waardevolle bron, naast documenten en cijfers",
                    "Als onbruikbaar, want het is zestig jaar later verteld",
                    "Als volledig bewijs voor alle aantallen en data",
                    "Als propaganda van de bezetter",
                ],
                0,
                "Over de beleving is een getuigenis onvervangbaar. Voor aantallen en data zijn de administratieve bronnen scherper.",
            ),
            tabel(
                "Waarvoor is deze getuigenis een sterke bron, en waarvoor minder?",
                [
                    ("hoe de aankomst aanvoelde", "Sterk"),
                    ("hoeveel mensen in 1944 in het kamp aankwamen", "Zwakker"),
                    ("wat een kind van veertien beleefde", "Sterk"),
                ],
                "Een getuige vertelt wat zij meemaakte. Voor de omvang en de organisatie heb je documenten nodig.",
                kolommen=["Sterk", "Zwakker"],
            ),
        ],
    ),
    sleep(
        "In de Holocaust kwamen ongeveer [[zes miljoen]] Joden om het leven. De organisatie van de vernietiging werd besproken in [[Wannsee]], in januari 1942. Het bekendste vernietigingskamp is [[Auschwitz]].",
        ["zestigduizend", "Neurenberg", "Mechelen"],
        "In Neurenberg werden na de oorlog de leiders berecht. Mechelen was het verzamelkamp in België.",
    ),
    open_(
        "Leg uit waarom de Holocaust niet plots begon in de oorlog, maar stap voor stap groeide.",
        "Het begon met uitsluiting bij wet, nog voor de oorlog, met de Neurenberger wetten van 1935: Joden verloren hun rechten. Daarna kwamen verplichte kentekens en registratie, en in de oorlog getto's. In Wannsee werd in 1942 de vernietiging georganiseerd, en volgden deportaties naar vernietigingskampen. Elke stap maakte de volgende mogelijk.",
    ),
    open_(
        "Leg uit welke lessen de wereld na 1945 trok uit de Tweede Wereldoorlog. Geef drie voorbeelden.",
        "De leiders van het naziregime werden in Neurenberg berecht voor misdaden tegen de menselijkheid, een begrip dat toen in het recht kwam. Het woord genocide werd in het internationaal recht vastgelegd. In 1945 werden de Verenigde Naties opgericht en in 1948 kwam de Universele Verklaring van de Rechten van de Mens.",
    ),
    mk(
        "Je ziet een foto uit 1944: juichende mensen rond een tank in een Belgische straat. Wat is de sterkste conclusie?",
        [
            "De bevrijding werd met vreugde onthaald",
            "Iedereen in België had in het verzet gezeten",
            "De oorlog in Europa was die dag voorbij",
            "De tank was een Duitse tank die binnenviel",
        ],
        0,
        "De foto toont de vreugde van de bevrijding in september 1944. De oorlog duurde in Europa nog tot mei 1945.",
    ),
    tabel(
        "Welke uitspraken over de repressie kloppen?",
        [
            ("Ze volgde na de oorlog.", J),
            ("Ze ging over het bestraffen van collaboratie.", J),
            ("Ze was de naam van het verzet tijdens de oorlog.", F),
        ],
        "Collaboratie tijdens de oorlog, repressie erna.",
    ),
]

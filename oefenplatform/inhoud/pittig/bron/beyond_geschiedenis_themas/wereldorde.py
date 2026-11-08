"""Een nieuwe wereldorde: VN, Koude Oorlog en Europa — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="ijzeren-gordijn.webp", zelf=False,
         wat="Kaart van Europa tijdens de Koude Oorlog met het IJzeren Gordijn, de NAVO-landen en de landen van het Warschaupact in twee kleuren. Liefst met een legende.",
         waar="Wikimedia Commons, zoek 'Iron Curtain map NATO Warsaw Pact'.",
         vragen="kaartvraag over de twee blokken"),
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvragen op 1961 en 1989"),
]

VRAGEN = [
    tabel(
        "Juist of fout? Lees elke uitspraak over de Verenigde Naties.",
        [
            ("Ze werden opgericht in 1945, enkele maanden na het einde van de oorlog in Europa.", J),
            ("Het hoofddoel is de vrede en de veiligheid in de wereld bewaren.", J),
            ("De Europese Commissie is een orgaan van de VN.", F),
            ("Het Internationaal Gerechtshof zetelt in Den Haag.", J),
        ],
        "De VN hebben de Algemene Vergadering, de Veiligheidsraad en het Internationaal Gerechtshof. De Europese Commissie hoort bij de EU.",
    ),
    mk(
        "Welke landen hebben een vaste zetel met vetorecht in de Veiligheidsraad? (meerdere antwoorden)",
        ["De Verenigde Staten", "China", "Rusland", "Duitsland", "Frankrijk"],
        [0, 1, 2, 4],
        "Vijf vaste leden: de Verenigde Staten, Rusland, China, Frankrijk en het Verenigd Koninkrijk. Duitsland is er geen vast lid van.",
    ),
    mk(
        "Veertien landen van de Veiligheidsraad stemmen voor een vredesmissie, één vast lid stemt tegen. Wat gebeurt er?",
        [
            "De beslissing gaat niet door, want één vast lid kan met zijn veto alles tegenhouden",
            "De beslissing gaat door, want een ruime meerderheid van de landen is voor",
            "De Algemene Vergadering beslist dan in de plaats van de Veiligheidsraad",
            "Het Internationaal Gerechtshof moet de knoop doorhakken tussen beide",
        ],
        0,
        "Het vetorecht is de grote zwakte van de VN: één vast lid kan een beslissing blokkeren, ook als alle anderen voor zijn.",
    ),
    sorteer(
        "Sterkte of zwakte van de Verenigde Naties?",
        ["Sterkte", "Zwakte"],
        [
            ["Alle landen kunnen er met elkaar spreken", "Sterkte"],
            ["Humanitaire hulp bij rampen en hongersnood", "Sterkte"],
            ["Wereldwijde normen vastleggen, zoals de mensenrechten", "Sterkte"],
            ["Het vetorecht van vijf landen", "Zwakte"],
            ["Geen eigen staand leger", "Zwakte"],
        ],
        "De VN zijn sterk als ontmoetingsplaats en voor normen en hulp. Vetorecht en het ontbreken van een eigen leger maken haar zwak.",
    ),
    keuze(
        "De duurzame ontwikkelingsdoelen zijn [[*zeventien|vijf|veertien]] doelen die de wereld tegen [[*2030|2000|2100]] wil halen. De organisatie die zich met de gezondheid in de wereld bezighoudt, is de [[*WHO|NAVO|EGKS]].",
        "Zeventien doelen tegen 2030. De WHO is de wereldgezondheidsorganisatie van de VN.",
    ),
    mk(
        "Waarom noemt men de Koude Oorlog koud?",
        [
            "De twee supermachten vochten nooit rechtstreeks tegen elkaar",
            "De oorlog werd vooral in de winter en in koude streken gevoerd",
            "Er vielen in die hele periode nergens ter wereld doden",
            "Beide kampen spraken af om geen wapens meer te maken",
        ],
        0,
        "De Verenigde Staten en de Sovjet-Unie stonden ideologisch lijnrecht tegenover elkaar, maar vochten nooit rechtstreeks. Elders vielen wel doden, in oorlogen via anderen.",
    ),
    sorteer(
        "Hoort het kenmerk bij het westerse of bij het oostelijke blok?",
        ["Westers blok", "Oostelijk blok"],
        [
            ["Kapitalisme en democratie", "Westers blok"],
            ["Communisme en partijstaat", "Oostelijk blok"],
            ["De NAVO", "Westers blok"],
            ["Het Warschaupact", "Oostelijk blok"],
            ["De Bondsrepubliek Duitsland", "Westers blok"],
            ["De DDR", "Oostelijk blok"],
        ],
        "Twee blokken met elk een ideologie, een bondgenootschap en een eigen Duitse staat.",
    ),
    met_prent("ijzeren-gordijn.webp", tabel(
        "Bekijk de kaart van Europa tijdens de Koude Oorlog. Welke uitspraken kan je staven?",
        [
            ("Het IJzeren Gordijn liep dwars door Europa.", J),
            ("Duitsland was verdeeld over beide blokken.", J),
            ("België hoorde bij de NAVO.", J),
            ("Hongarije hoorde bij de NAVO.", F),
        ],
        "Churchill noemde de scheidslijn in 1946 het IJzeren Gordijn. België zat in de NAVO, Hongarije in het Warschaupact.",
    ), volgt=True),
    volgorde(
        "Zet de gebeurtenissen van de Koude Oorlog in de juiste volgorde.",
        ["Churchill spreekt over het IJzeren Gordijn", "De blokkade van Berlijn", "De Hongaarse opstand", "De bouw van de Berlijnse Muur", "De Cubacrisis", "De Praagse Lente"],
        "1946, 1948-1949, 1956, 1961, 1962 en 1968.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Berlijnse Muur gebouwd werd.",
        "tijdlijn-1750-2030.svg",
        [[67.7, 25, 6.2, 55]],
        "1961, net na het streepje van 1960.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Berlijnse Muur viel.",
        "tijdlijn-1750-2030.svg",
        [[76.4, 25, 6.2, 55]],
        "November 1989, vlak voor het streepje van 1990. Twee jaar later hield de Sovjet-Unie op te bestaan.",
    ),
    koppel(
        "Waarover ging elke gebeurtenis?",
        [
            ["De blokkade van Berlijn", "Westerse geallieerden bevoorraden de stad maandenlang door de lucht"],
            ["De Cubacrisis", "Sovjetraketten op een eiland vlak bij de Verenigde Staten"],
            ["De Praagse Lente", "Een poging tot hervorming in Tsjecho-Slowakije, met tanks beëindigd"],
            ["De SALT-besprekingen", "Het aantal kernwapens beperken"],
        ],
        ["Een schild in de ruimte tegen aanvallende raketten"],
        "Het schild in de ruimte is het SDI-plan van Reagan uit 1983, en hoort bij geen van deze vier.",
    ),
    mk(
        "Wat zei de Brezjnevdoctrine?",
        [
            "Moskou mocht in elk socialistisch land ingrijpen",
            "Elk land mocht zelf zijn bondgenootschap kiezen",
            "De Sovjet-Unie gaf al haar kernwapens op",
            "Duitsland moest opnieuw één land worden",
        ],
        0,
        "Ze rechtvaardigde achteraf het ingrijpen in Tsjecho-Slowakije in 1968.",
    ),
    tabel(
        "Met welke middelen voerden beide kampen de Koude Oorlog, naast wapens?",
        [
            ("Propaganda en spionage", J),
            ("Economische hulp aan bondgenoten", J),
            ("Een wedloop in de ruimtevaart", J),
            ("Rechtstreekse veldslagen tussen Amerikaanse en Sovjetlegers", F),
        ],
        "De strijd liep via propaganda, spionage, hulp en ruimtevaart. Rechtstreeks vochten de supermachten nooit tegen elkaar.",
    ),
    keuze(
        "De Sovjetleider Gorbatsjov lanceerde vanaf 1985 [[*glasnost|perestrojka|détente]], dat betekent openheid, en perestrojka, dat betekent [[*hervorming|ontspanning|bewapening]].",
        "Openheid en hervorming moesten de Sovjet-Unie redden, maar versnelden haar einde.",
    ),
    tabel(
        "Unipolair, bipolair of multipolair?",
        [
            ("Twee machtscentra, zoals tijdens de Koude Oorlog", "Bipolair"),
            ("Eén supermacht die overblijft na 1991", "Unipolair"),
            ("Meerdere machtscentra naast elkaar", "Multipolair"),
        ],
        "Na de Koude Oorlog bleef één supermacht over. Welk woord vandaag past, is een discussie.",
        kolommen=["Unipolair", "Bipolair", "Multipolair"],
    ),
    mk(
        "Hoe zijn de verhoudingen tussen de Verenigde Staten en Rusland sinds het einde van de Koude Oorlog geëvolueerd?",
        [
            "Na een periode van toenadering liepen de spanningen weer op",
            "Ze zijn sinds 1991 voortdurend vriendschappelijk gebleven",
            "Ze zijn sinds 1991 voortdurend in oorlog met elkaar",
            "Rusland trad in 1991 toe tot de NAVO en de EU",
        ],
        0,
        "Er was toenadering, maar de spanningen kwamen terug. Ze bleven dus niet voortdurend vriendschappelijk.",
    ),
    mk(
        "Wat is het verband tussen de Europese eenmaking en de Tweede Wereldoorlog?",
        [
            "De eenmaking moest een nieuwe oorlog tussen buurlanden onmogelijk maken",
            "De eenmaking was een beloning voor de landen die de oorlog gewonnen hadden",
            "De eenmaking werd door de Sovjet-Unie opgelegd aan West-Europa",
            "Er is geen verband: de eenmaking begon pas na de val van de Muur",
        ],
        0,
        "Door kolen en staal, de grondstoffen van de oorlog, samen te beheren, werd een oorlog tussen Frankrijk en Duitsland onmogelijk.",
    ),
    tabel(
        "Welk verdrag bracht wat?",
        [
            ("De Europese Economische Gemeenschap en de gemeenschappelijke markt", "Rome"),
            ("De Europese Unie zelf en de weg naar een gezamenlijke munt", "Maastricht"),
            ("Een vaste voorzitter van de Europese Raad en bindende grondrechten", "Lissabon"),
        ],
        "Rome in 1957, Maastricht in 1992 en Lissabon in 2007, in werking in 2009.",
        kolommen=["Rome", "Maastricht", "Lissabon"],
    ),
    volgorde(
        "Zet de stappen van de Europese eenmaking in de juiste volgorde.",
        ["De Europese Gemeenschap voor Kolen en Staal", "Het Verdrag van Rome", "Het Verdrag van Maastricht", "De euro als biljetten", "Het Verdrag van Lissabon treedt in werking"],
        "Eerst de EGKS, dan Rome (1957), Maastricht (1992), de euro als biljetten (2002) en Lissabon in werking (2009).",
    ),
    koppel(
        "Welke Europese instelling past bij elke omschrijving?",
        [
            ["Heeft het recht om wetgeving voor te stellen", "De Europese Commissie"],
            ["Wordt rechtstreeks door de burgers verkozen", "Het Europees Parlement"],
            ["Hier zetelen de staatshoofden en regeringsleiders", "De Europese Raad"],
            ["Hier zetelen de vakministers van de lidstaten", "De Raad van de Europese Unie"],
        ],
        ["De Raad van Europa"],
        "De Raad van Europa is een aparte organisatie die niet eens bij de EU hoort. Let ook op het verschil tussen de Europese Raad en de Raad van de EU.",
    ),
    mk(
        "Een krant schrijft: \"De Raad van Europa besliste gisteren over het Europese landbouwbeleid.\" Wat is er mis?",
        [
            "De Raad van Europa hoort niet bij de EU; de krant verwart hem met een EU-instelling",
            "Er is niets mis: de Raad van Europa is het belangrijkste orgaan van de EU",
            "De Raad van Europa bestaat sinds het Verdrag van Lissabon niet meer",
            "Landbouw is een bevoegdheid van de Verenigde Naties en niet van Europa",
        ],
        0,
        "De Raad van Europa is een aparte organisatie. Over EU-beleid beslissen de Commissie, het Parlement en de Raad van de EU.",
    ),
    tabel(
        "Is het een actuele uitdaging voor de EU?",
        [
            ("Migratie en de bewaking van de buitengrenzen", J),
            ("De klimaatomslag en de energiebevoorrading", J),
            ("Euroscepsis, met de brexit als verste voorbeeld", J),
            ("De wederopbouw van de kolen- en staalindustrie van 1950", F),
        ],
        "Migratie, klimaat en energie, en euroscepsis zijn uitdagingen van vandaag. De EGKS hoort bij het begin van de eenmaking.",
    ),
    tabel(
        "Welke doelstellingen had de Europese Gemeenschap voor Kolen en Staal?",
        [
            ("Een nieuwe oorlog tussen Frankrijk en Duitsland onmogelijk maken", J),
            ("De economieën met elkaar verweven door handel", J),
            ("Samen sterker staan tegenover de grote mogendheden", J),
            ("Eén gemeenschappelijk Europees leger oprichten", F),
        ],
        "Vrede, verweven economieën en samen sterker staan. Een Europees leger hoorde daar niet bij.",
    ),
    mk(
        "De VN hebben geen eigen staand leger. Hoe komt een vredesmacht met blauwhelmen dan tot stand?",
        [
            "Lidstaten leveren per missie soldaten",
            "De VN huren soldaten in van private firma's",
            "De NAVO stuurt automatisch haar troepen",
            "De Veiligheidsraad heeft een eigen vast korps",
        ],
        0,
        "Blauwhelmen worden per missie door lidstaten geleverd. Daarom duurt het soms lang voor een missie kan starten.",
    ),
    mk(
        "Het Verenigd Koninkrijk stemde in 2016 voor de brexit. Wanneer werd die van kracht?",
        ["Eind januari 2020", "Meteen in 2016", "In 2009", "Ze is nooit van kracht geworden"],
        0,
        "Na de volksraadpleging van 2016 duurde het tot eind januari 2020 voor het land de Unie echt verliet.",
    ),
    casus(
        "Lees de twee uitspraken. Een Amerikaanse president in 1947: Wij helpen Europa met geld en goederen om zich te herstellen. Een Sovjetkrant in 1947: Met dat geld koopt Amerika zich bondgenoten in Europa.",
        [
            mk(
                "Waarom verschillen de twee bronnen zo sterk?",
                [
                    "Elke maker kijkt vanuit het eigen kamp en de eigen belangen",
                    "Een van de twee bronnen is gewoon vervalst",
                    "Ze gaan over twee totaal verschillende gebeurtenissen",
                    "De Sovjetkrant had geen toegang tot het nieuws",
                ],
                0,
                "Dat is standplaatsgebondenheid. Een tegenspraak tussen bronnen is geen probleem maar een aanwijzing.",
            ),
            keuze(
                "Het Marshallplan wilde Europa heropbouwen: dat is een [[*bedoeld|onbedoeld|toevallig]] gevolg. Dat het West-Europa ook stevig in het westerse kamp vastzette, noemt de bundel een [[*onbedoeld|bedoeld|verborgen]] gevolg.",
                "Heropbouw was het doel. Dat Europa er ook door in een kamp terechtkwam, is het voorbeeld van een onbedoeld gevolg.",
            ),
            mk(
                "Welke redeneerwijze pas je toe als je beide bronnen naast elkaar legt?",
                ["Meerdere perspectieven hanteren", "Stereotypering analyseren", "Evolutie en revolutie benoemen", "Continuïteit benoemen"],
                0,
                "Je bekijkt dezelfde gebeurtenis vanuit twee kampen. Zo krijg je een vollediger beeld.",
            ),
        ],
    ),
    open_(
        "Vergelijk de Volkenbond met de Verenigde Naties. Geef een gelijkenis en een verschil.",
        "Gelijkenis: beide werden na een wereldoorlog opgericht om conflicten tussen landen vreedzaam op te lossen, en geen van beide heeft een eigen staand leger. Verschil: de Verenigde Staten traden nooit toe tot de Volkenbond, maar wel tot de VN. Bij de Volkenbond vroegen beslissingen de instemming van iedereen; bij de VN kunnen vijf vaste leden met hun vetorecht een beslissing tegenhouden.",
    ),
]

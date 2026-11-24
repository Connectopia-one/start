"""De Europese eenmaking — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = []

VRAGEN = [
    # --- waarom
    tabel(
        "Waarom gingen Europese landen na 1945 samenwerken?",
        [
            ("Om een nieuwe oorlog tussen Frankrijk en Duitsland te voorkomen", J),
            ("Om de verwoeste economie te heropbouwen", J),
            ("Om gewicht te hebben tussen de twee blokken", J),
            ("Om samen één leger op te richten in plaats van de NAVO", F),
        ],
        "De eenmaking was geen militair bondgenootschap. Dat bestond apart: de NAVO.",
    ),
    mk(
        "Waarom stelde Schuman net voor om kolen en staal samen te beheren?",
        [
            "Het waren de grondstoffen van de oorlogsindustrie",
            "Het waren de enige grondstoffen die Europa toen nog had",
            "Kolen en staal waren in 1950 volledig waardeloos geworden",
            "De Verenigde Staten verplichtten Europa om dat te doen",
        ],
        0,
        "Wie kolen en staal samen beheert, kan moeilijk nog een oorlog tegen elkaar voorbereiden.",
    ),
    sorteer(
        "Hoorde het land bij de zes stichters van 1951?",
        ["Stichter in 1951", "Pas later lid"],
        [
            ["België", "Stichter in 1951"],
            ["Italië", "Stichter in 1951"],
            ["Luxemburg", "Stichter in 1951"],
            ["Groot-Brittannië", "Pas later lid"],
            ["Ierland", "Pas later lid"],
            ["Denemarken", "Pas later lid"],
        ],
        "België, Nederland, Luxemburg, Frankrijk, Duitsland en Italië. Groot-Brittannië, Ierland en Denemarken kwamen er in 1973 bij.",
    ),
    # --- verdragen
    volgorde(
        "Zet de stappen van de Europese eenmaking in de juiste volgorde.",
        ["De Schuman-verklaring", "De EGKS", "Het Verdrag van Rome", "Schengen", "Het Verdrag van Maastricht", "De euro als biljet en munt"],
        "1950, 1951, 1957, 1985, 1992 en 2002.",
    ),
    koppel(
        "Welk verdrag of welke stap hoort bij elke omschrijving?",
        [
            ["Een gemeenschappelijke markt, de EEG", "Verdrag van Rome"],
            ["De controles aan de binnengrenzen verdwijnen", "Schengen"],
            ["De Europese Unie wordt opgericht", "Verdrag van Maastricht"],
            ["Kolen en staal samen beheren", "EGKS"],
        ],
        ["Brexit", "Warschaupact"],
        "Van kolen en staal over een gemeenschappelijke markt naar de Unie.",
    ),
    tabel(
        "Een leerling zegt: \"De Europese samenwerking begon met de euro en met politiek.\" Wat is juist?",
        [
            ("Ze begon met kolen en staal.", J),
            ("Ze begon met economische samenwerking.", J),
            ("De euro kwam als biljet pas in 2002.", J),
            ("De euro bestond al in 1951.", F),
        ],
        "Eerst economie, stap voor stap, en pas veel later een munt.",
    ),
    casus(
        "Een Duits bedrijf verkoopt in 1970 machines aan België, een Amerikaans bedrijf ook. Op de Duitse machines betaalt de Belgische koper geen invoerrechten, op de Amerikaanse wel, en in heel de Gemeenschap even veel.",
        [
            inv(
                "Hoe noem je zo'n samenwerking tussen landen?",
                ["een douane-unie", "douane-unie", "douane unie"],
                "Geen invoerrechten op elkaars goederen, en één tarief tegenover de buitenwereld.",
            ),
            mk(
                "Welk verdrag legde die gemeenschappelijke markt vast?",
                [
                    "Het Verdrag van Rome",
                    "Het Verdrag van Versailles",
                    "Het Verdrag van Maastricht",
                    "Het verdrag van Schengen",
                ],
                0,
                "In 1957 in Rome kwam de gemeenschappelijke markt, de EEG.",
            ),
        ],
    ),
    tabel(
        "Welke uitspraken over Schengen en de euro kloppen?",
        [
            ("Noorwegen en Zwitserland doen mee aan Schengen zonder EU-lid te zijn.", J),
            ("Niet elk EU-land doet mee aan Schengen.", J),
            ("Denemarken, Polen en Zweden hebben hun eigen munt.", J),
            ("Elk land van de Unie betaalt met de euro.", F),
        ],
        "Schengen, de euro en de Unie zijn drie verschillende kringen die niet volledig samenvallen.",
    ),
    mk(
        "Waarom kreeg het gemeenschappelijk landbouwbeleid lang zoveel aandacht?",
        [
            "Het nam het grootste deel van de begroting",
            "Het was het enige beleid dat in Rome geregeld werd",
            "Het was verboden om voedsel uit het buitenland te halen",
            "Het werd volledig door de NAVO betaald",
        ],
        0,
        "Europa steunde de landbouw en regelde de prijzen. Dat kostte veel geld.",
    ),
    # --- instellingen
    tabel(
        "Welke instelling doet wat?",
        [
            ("Wordt sinds 1979 rechtstreeks verkozen", "Parlement"),
            ("Stelt wetgeving voor en voert beleid uit", "Commissie"),
            ("Ministers van de lidstaten, beslissen mee", "Raad"),
            ("Spreekt recht over de verdragen", "Hof van Justitie"),
        ],
        "Parlement en Raad beslissen samen. De Commissie stelt voor, het Hof spreekt recht.",
        kolommen=["Parlement", "Commissie", "Raad", "Hof van Justitie"],
    ),
    mk(
        "Hoe komen de leden van de Europese Commissie aan hun plaats?",
        [
            "Regeringen dragen hen voor, het Parlement keurt goed",
            "De burgers verkiezen hen rechtstreeks om de vijf jaar",
            "De Europese Centrale Bank benoemt hen",
            "Het Hof van Justitie loot hen uit",
        ],
        0,
        "De Commissie wordt niet rechtstreeks verkozen. Dat voedt soms de kritiek dat Europa ver van de burger staat.",
    ),
    mk(
        "Welke instelling bepaalt de rentevoet van de euro?",
        [
            "De Europese Centrale Bank",
            "Het Europees Parlement",
            "De Raad van Europa",
            "Het Hof van Justitie",
        ],
        0,
        "De Europese Centrale Bank waakt over de euro.",
    ),
    casus(
        "Een gemeente wil zelf beslissen over de openingsuren van haar bibliotheek. Een Europese regel daarover komt er niet.",
        [
            inv(
                "Welk beginsel van de Unie zie je hier aan het werk?",
                ["subsidiariteit", "de subsidiariteit", "het subsidiariteitsbeginsel", "subsidiariteitsbeginsel"],
                "Wat lager geregeld kan worden, blijft daar.",
            ),
            tabel(
                "Welke zaken regelt de Unie eerder wel?",
                [
                    ("Vrij verkeer van goederen tussen de lidstaten", J),
                    ("De rentevoet van de euro", J),
                    ("De openingsuren van een gemeentelijke bibliotheek", F),
                ],
                "Grensoverschrijdende zaken horen eerder bij de Unie.",
            ),
        ],
    ),
    tabel(
        "Europese Unie of Raad van Europa?",
        [
            ("Waakt over de mensenrechten, met een hof in Straatsburg", "Raad van Europa"),
            ("Heeft veel meer leden", "Raad van Europa"),
            ("Heeft een Commissie in Brussel", "Europese Unie"),
            ("Heeft de euro", "Europese Unie"),
        ],
        "Twee verschillende organisaties. De Raad van Europa staat los van de Unie.",
        kolommen=["Europese Unie", "Raad van Europa"],
    ),
    sleep(
        "België is [[stichtend]] lid. De Commissie en de Raad zitten in [[Brussel]]. Het Parlement vergadert in Brussel en in [[Straatsburg]].",
        ["Genève", "New York", "later"],
        "België speelt een grote rol, met veel instellingen in Brussel.",
    ),
    # --- uitbreiding en crisis
    mk(
        "Waarom konden in 2004 tien landen, vooral uit Midden-Europa, lid worden?",
        [
            "Het ijzeren gordijn was gevallen",
            "Ze hadden in 1951 de EGKS mee opgericht",
            "De Sovjet-Unie had hen in de EU gestuurd",
            "Ze hadden Schengen opgericht",
        ],
        0,
        "Na het einde van de Koude Oorlog konden landen uit het vroegere Oostblok aansluiten.",
    ),
    tabel(
        "Welke uitspraken over de brexit kloppen?",
        [
            ("Er was een volksstemming in 2016.", J),
            ("Het Verenigd Koninkrijk trad begin 2020 uit.", J),
            ("Het is de eerste en tot nu enige lidstaat die vertrok.", J),
            ("Het Verenigd Koninkrijk was nooit lid.", F),
        ],
        "Het trad in 1973 toe en stapte er in 2020 uit.",
    ),
    mk(
        "Wat deed de Unie tijdens de eurocrisis na 2008?",
        [
            "Ze leende geld met harde voorwaarden",
            "Ze schafte de euro af en voerde de oude munten weer in",
            "Ze liet de landen in nood volledig aan hun lot over",
            "Ze verbood alle banken in de eurozone",
        ],
        0,
        "Leningen voor landen in nood, met strengere begrotingsregels.",
    ),
    casus(
        "Een opiniestuk in een krant: \"Brussel beslist alles. De burger heeft niets meer te zeggen, en ons land geeft zijn macht uit handen.\"",
        [
            mk(
                "Wat is dit stuk?",
                [
                    "Een standpunt in het debat over de Unie",
                    "Een objectieve beschrijving van de feiten",
                    "Een officiële tekst van de Europese Commissie",
                    "Een verslag van het Hof van Justitie",
                ],
                0,
                "Geen vaststelling en ook geen onzin: een standpunt dat je naast het andere legt.",
            ),
            tabel(
                "Welk gegeven kan een voorstander van de Unie ertegenover plaatsen?",
                [
                    ("Het Europees Parlement wordt rechtstreeks verkozen.", J),
                    ("Subsidiariteit laat zaken lager regelen.", J),
                    ("Mensen kunnen vrij over de grenzen werken.", J),
                    ("De Commissie wordt rechtstreeks verkozen.", F),
                ],
                "De Commissie wordt niet rechtstreeks verkozen. Dat is net een argument van critici.",
            ),
        ],
    ),
    tabel(
        "Voordeel of kritiek?",
        [
            ("Bedrijven en mensen kunnen vrij over de grenzen werken.", "Voordeel"),
            ("Diploma's worden in andere lidstaten erkend.", "Voordeel"),
            ("Beslissingen staan te ver van de burger.", "Kritiek"),
            ("Lidstaten geven te veel bevoegdheid uit handen.", "Kritiek"),
        ],
        "Twee kanten van hetzelfde debat.",
        kolommen=["Voordeel", "Kritiek"],
    ),
    mk(
        "Wat is het grootste verschil tussen de Europese Unie en de Verenigde Naties?",
        [
            "De Unie maakt wetten die in de lidstaten gelden",
            "De Verenigde Naties hebben de euro als munt",
            "De Unie heeft meer lidstaten dan de VN",
            "De VN hebben een rechtstreeks verkozen parlement",
        ],
        0,
        "De VN werken met verdragen en resoluties. De Unie is op dat punt supranationaal.",
    ),
    tabel(
        "Is de Europese Unie een staat?",
        [
            ("Ze heeft één regering voor alle lidstaten.", F),
            ("Ze heeft één eigen leger.", F),
            ("Lidstaten oefenen bevoegdheden samen uit.", J),
            ("Ze maakt wetten die in de lidstaten gelden.", J),
        ],
        "Een verbond van staten, geen staat met één regering en één leger.",
    ),
    keuze(
        "Het Europees Parlement wordt sinds [[*1979|1951|2002]] rechtstreeks verkozen. Groot-Brittannië trad toe in [[*1973|1951|2004]].",
        "Het Parlement is de enige instelling die de burgers rechtstreeks kiezen.",
    ),
    open_(
        "Leg uit hoe de twee wereldoorlogen en de Koude Oorlog de Europese eenmaking beïnvloedden.",
        "Na twee oorlogen in dertig jaar tussen dezelfde buren wilde men een nieuwe oorlog onmogelijk maken: daarom begon men met het samen beheren van kolen en staal, de grondstoffen van de oorlogsindustrie. In de Koude Oorlog zocht West-Europa gewicht tussen de twee blokken. Na de val van het ijzeren gordijn konden landen uit het vroegere Oostblok lid worden, met tien nieuwe landen in 2004.",
    ),
    open_(
        "Toon aan dat de Europese eenmaking stap voor stap groeide. Gebruik minstens vier stappen.",
        "In 1951 kwam de EGKS met zes landen voor kolen en staal. In 1957 bracht het Verdrag van Rome een gemeenschappelijke markt. In 1985 schafte Schengen de grenscontroles af. In 1992 richtte het Verdrag van Maastricht de Europese Unie op, en in 2002 kwamen de eurobiljetten. Ondertussen groeide het aantal leden, met onder meer 1973 en 2004.",
    ),
    mk(
        "Waarom vertrouwden de zes landen in 1951 een gemeenschappelijk beheer meer dan een vredesverdrag?",
        [
            "Samen beheren maakt oorlog praktisch onmogelijk",
            "Een vredesverdrag was in 1951 verboden",
            "De Volkenbond weigerde nog verdragen te tekenen",
            "Kolen en staal waren toen in handen van de VS",
        ],
        0,
        "Na Versailles wist men dat papieren beloftes niet volstonden. Gedeelde belangen maken oorlog zinloos.",
    ),
    tabel(
        "Welke uitspraken over België en Europa kloppen?",
        [
            ("België hoorde bij de zes stichters.", J),
            ("België betaalt met de euro.", J),
            ("België doet mee aan Schengen.", J),
            ("België trad pas in 2004 toe.", F),
        ],
        "België is stichtend lid en zit in alle kringen.",
    ),
]

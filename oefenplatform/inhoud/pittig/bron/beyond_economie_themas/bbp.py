"""Het bbp, economische groei en welvaartsindicatoren — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

GRAFIEKEN = []
PRENTEN = []

VRAGEN = [
    casus(
        "Een bedrijfskolom: een boswachter verkoopt hout voor 1 000 euro aan een zagerij. De zagerij verkoopt planken voor 2 500 euro aan een meubelmaker. De meubelmaker verkoopt tafels voor 6 000 euro aan gezinnen.",
        [
            inv("Hoeveel draagt deze kolom bij aan het bbp? Schrijf enkel het getal in euro.", "6000",
                "Het bbp telt enkel de finale goederen: de tafels van 6 000 euro. Of: 1 000 + 1 500 + 3 500 toegevoegde waarde."),
            inv("Hoe groot is de bruto toegevoegde waarde van de zagerij? Schrijf enkel het getal.", "1500",
                "Omzet min aankopen bij andere bedrijven: 2 500 − 1 000 = 1 500 euro."),
            mk("Een leerling telt alle omzetten op: 9 500 euro. Wat is er fout?",
               ["Hij telt het hout meerdere keren mee", "Hij vergeet de btw op de tafels",
                "Hij vergeet de lonen van de meubelmaker", "Er is niets fout: dat is het bbp"],
               0, "Het hout zit in de planken en de planken in de tafels: zo tel je het dubbel en driedubbel."),
        ],
    ),
    inv(
        "Een bakker verkoopt brood voor 80 000 euro, koopt voor 30 000 euro grondstoffen en heeft 6 000 euro afschrijvingen op zijn oven. Hoe groot is zijn netto toegevoegde waarde? Schrijf enkel het getal.",
        "44000",
        "Bruto: 80 000 − 30 000 = 50 000. Netto: 50 000 − 6 000 = 44 000 euro.",
    ),
    mk(
        "De bruto toegevoegde waarde van een bedrijf is 120 000 euro en de netto toegevoegde waarde 105 000 euro. Wat is het verschil?",
        ["15 000 euro afschrijvingen", "15 000 euro btw", "15 000 euro lonen", "15 000 euro aankopen bij andere bedrijven"],
        0,
        "Het verschil tussen bruto en netto zijn de afschrijvingen.",
    ),
    tabel(
        "Welke benadering van het bbp gebruik je?",
        [
            ("Je telt de lonen, interesten, huren en winsten op", "Inkomensbenadering"),
            ("Je telt C + I + G + (X − M) op", "Bestedingsbenadering"),
            ("Je telt de toegevoegde waarde van alle bedrijven op", "Productiebenadering"),
        ],
        "Drie wegen, één uitkomst: elke besteding is iemands inkomen en iemands toegevoegde waarde.",
        kolommen=["Bestedingsbenadering", "Inkomensbenadering", "Productiebenadering"],
    ),
    mk(
        "Waarom komen de drie berekeningswijzen van het bbp op hetzelfde uit?",
        ["Elke besteding is voor iemand een inkomen en bij iemand toegevoegde waarde",
         "De Nationale Bank past de cijfers achteraf aan tot ze gelijk zijn",
         "Ze tellen alle drie de omzetten van alle bedrijven op",
         "Ze komen niet op hetzelfde uit; men neemt het gemiddelde"],
        0,
        "Het is dezelfde koek, van drie kanten bekeken.",
    ),
    inv(
        "Het bbp tegen factorprijzen is 620, de indirecte belastingen zijn 90 en de subsidies 15. Hoe groot is het bbp tegen marktprijzen? Schrijf enkel het getal.",
        "695",
        "620 + 90 − 15 = 695.",
    ),
    mk(
        "Het bbp tegen marktprijzen is 540 en het bbp tegen factorprijzen 500. De subsidies zijn 10. Hoe groot zijn de indirecte belastingen?",
        ["50", "40", "30", "550"],
        0,
        "Marktprijzen = factorprijzen + indirecte belastingen − subsidies: 540 = 500 + IB − 10, dus IB = 50.",
    ),
    sorteer(
        "Telt het mee in het Belgische bbp, in het Belgische bnp, of in allebei?",
        ["Enkel bbp", "Enkel bnp", "Allebei"],
        [
            ["Een Nederlander werkt in Antwerpen", "Enkel bbp"],
            ["Een Belg werkt in Maastricht en woont in België", "Enkel bnp"],
            ["Een Belg werkt in Gent bij een Belgisch bedrijf", "Allebei"],
            ["Een Duits bedrijf maakt winst in zijn fabriek in Genk", "Enkel bbp"],
        ],
        "Het bbp kijkt naar het grondgebied, het bnp naar de inwoners.",
    ),
    mk(
        "Het nominaal bbp stijgt met 7 % en de prijzen stijgen met 4 %. Hoeveel groeide het reëel bbp ongeveer?",
        ["3 %", "11 %", "7 %", "1,75 %"],
        0,
        "Reële groei ≈ nominale groei − prijsstijging: 7 − 4 = 3 %.",
    ),
    mk(
        "Het nominaal bbp stijgt met 2 % en de prijzen stijgen met 5 %. Wat besluit je?",
        ["Het reëel bbp daalde met ongeveer 3 %", "De economie groeide met 7 %",
         "Het reëel bbp steeg met ongeveer 3 %", "Je kan niets besluiten zonder het aantal inwoners"],
        0,
        "2 − 5 = −3 %: er werd minder geproduceerd, ook al stijgt het nominaal bbp.",
    ),
    keuze(
        "Wil je weten of een economie echt meer produceerde, dan vergelijk je het [[*reëel|nominaal]] bbp, want daar is de [[*prijsstijging|bevolkingsgroei|btw]] uitgehaald.",
        "Het nominaal bbp kan ook stijgen omdat alles duurder werd.",
    ),
    inv(
        "Een land heeft een bbp van 450 miljard euro en 9 miljoen inwoners. Hoe groot is het bbp per capita? Schrijf enkel het getal in euro.",
        "50000",
        "450 000 000 000 / 9 000 000 = 50 000 euro.",
    ),
    mk(
        "Land A heeft een bbp van 800 miljard euro en 20 miljoen inwoners. Land B heeft 300 miljard euro en 5 miljoen inwoners. Welk land heeft het hoogste bbp per capita?",
        ["Land B, met 60 000 euro per inwoner", "Land A, met 40 000 euro per inwoner",
         "Land A, want het totale bbp is groter", "Ze zijn gelijk, want het verschil is enkel de grootte"],
        0,
        "A: 800 / 20 = 40 000 euro. B: 300 / 5 = 60 000 euro.",
    ),
    tabel(
        "Waar of niet waar over het bbp per capita?",
        [
            ("Een hoger bbp per capita betekent altijd dat de meeste inwoners er beter aan toe zijn.", F),
            ("Vrijwilligerswerk telt mee in het bbp.", F),
            ("De heropbouw na een overstroming doet het bbp stijgen.", J),
            ("Het bbp per capita houdt geen rekening met milieuschade.", J),
        ],
        "Het bbp per capita zegt niets over de verdeling, telt geen onbetaald werk en ziet herstel na een ramp als productie.",
    ),
    mk(
        "Na een zware storm worden honderden daken hersteld en stijgt het bbp. Waarom is dat een tekortkoming van het bbp als welvaartsmaat?",
        ["Herstel telt als productie, terwijl de welvaart niet hoger is dan voor de storm",
         "Dakwerken tellen niet mee omdat ze in het zwart gebeuren",
         "De overheid betaalt de herstellingen, dus tellen ze dubbel",
         "Een storm doet het bbp altijd dalen, dus de cijfers zijn fout"],
        0,
        "Je bent na het herstel terug waar je was, maar het bbp toont groei.",
    ),
    koppel(
        "Welke welvaartsindicator past bij de beschrijving?",
        [
            ["Levensverwachting, onderwijs en inkomen per inwoner", "HDI"],
            ["Geluk en welzijn, bekend gemaakt door Bhutan", "BNG"],
            ["Het bbp aangepast voor vrije tijd, onbetaald werk en schade", "MEW"],
            ["Je kiest zelf hoe zwaar elk onderdeel doorweegt", "Better Life Index"],
        ],
        ["Bbp per capita"],
        "Elke indicator probeert meer te meten dan materiële welvaart.",
    ),
    mk(
        "Twee landen hebben ongeveer hetzelfde bbp per capita, maar land X heeft een veel hogere HDI. Wat is de meest logische verklaring?",
        ["In land X zijn de levensverwachting en het onderwijs beter",
         "Land X heeft meer inwoners, dus automatisch ook een hogere HDI-score",
         "Land X heeft een hoger nominaal bbp door inflatie",
         "In land X telt het vrijwilligerswerk mee in het bbp"],
        0,
        "De HDI kijkt ook naar levensverwachting en onderwijs, niet enkel naar inkomen.",
    ),
    mk(
        "Welke indicator gebruik je best om te zien hoe ver een land staat met de duurzame ontwikkelingsdoelen?",
        ["De SDG Index", "Het nominaal bbp", "Het bbp per capita", "Het bnp tegen factorprijzen"],
        0,
        "Het SDG Dashboard en de SDG Index meten de vooruitgang op de 17 doelen.",
    ),
    sorteer(
        "Telt het mee in het bbp of niet?",
        ["Telt mee", "Telt niet mee"],
        [
            ["Een gezin koopt een nieuwe fiets", "Telt mee"],
            ["Een ouder blijft thuis om voor de kinderen te zorgen", "Telt niet mee"],
            ["Een bedrijf koopt een nieuwe machine", "Telt mee"],
            ["Een bakker koopt bloem om brood te bakken", "Telt niet mee"],
            ["Een buurman helpt gratis bij een verhuis", "Telt niet mee"],
        ],
        "Het bbp telt finale goederen en betaalde productie. Bloem is een tussenproduct, onbetaald werk telt niet.",
    ),
    mk(
        "Waarom heet innovatie zowel een motor van groei als een disruptieve factor?",
        ["Ze laat toe meer te maken met dezelfde middelen, maar kan bestaande bedrijven en jobs overbodig maken",
         "Ze doet het bbp eerst stijgen en daarna altijd even sterk dalen",
         "Ze verhoogt de prijzen, waardoor het nominaal bbp stijgt maar het reëel bbp daalt",
         "Ze wordt enkel door de overheid betaald en verstoort zo de markt"],
        0,
        "Nieuwe technieken verhogen de productie, maar een vernieuwing kan een hele sector omverwerpen.",
    ),
    tabel(
        "Bij welke bestedingscategorie van het bbp hoort de aankoop?",
        [
            ("Een gezin koopt een smartphone", "C"),
            ("Een bedrijf bouwt een nieuwe loods", "I"),
            ("De overheid betaalt de bouw van een school", "G"),
            ("Een Franse klant koopt Belgische chocolade", "X"),
        ],
        "C consumptie, I investeringen, G overheidsbestedingen, X export.",
        kolommen=["C", "I", "G", "X"],
    ),
    inv(
        "C = 300, I = 90, G = 120, X = 250 en M = 230. Hoe groot is het bbp? Schrijf enkel het getal.",
        "530",
        "300 + 90 + 120 + (250 − 230) = 530.",
    ),
    sleep(
        "'Binnenlands' wil zeggen: alles wat binnen de [[grenzen]] geproduceerd wordt, [[wie]] het ook maakt. Het bnp kijkt naar de [[inwoners]].",
        ["bedrijven", "export", "prijzen"],
        "Grondgebied tegenover nationaliteit van de inwoners.",
    ),
    mk(
        "Welke instelling publiceert in België de officiële cijfers over het bbp?",
        ["De Nationale Bank van België", "De Europese Centrale Bank", "Het Internationaal Monetair Fonds", "De Wereldbank"],
        0,
        "De Nationale Bank van België maakt de nationale rekeningen bekend.",
    ),
    volgorde(
        "Je wil weten of de inwoners van een land er echt op vooruitgingen. Zet de stappen in een logische volgorde.",
        ["Het reëel bbp van beide jaren opzoeken", "Delen door het aantal inwoners", "Kijken naar de verdeling en naar indicatoren zoals de HDI"],
        "Eerst de prijsstijging eruit, dan per inwoner, en ten slotte verder kijken dan het bbp.",
    ),
    mk(
        "Een Belgisch bedrijf keert 40 miljoen euro dividend uit aan Amerikaanse aandeelhouders. Belgen ontvangen 25 miljoen euro lonen uit Nederland. Wat is het effect op het Belgische bnp tegenover het bbp, als er verder niets is?",
        ["Het bnp is 15 miljoen euro kleiner dan het bbp", "Het bnp is 15 miljoen euro groter dan het bbp, door het dividend",
         "Het bnp is 65 miljoen euro groter dan het bbp", "Bnp en bbp zijn even groot"],
        0,
        "Het bnp telt de inkomens van inwoners: + 25 uit het buitenland, − 40 naar het buitenland, samen −15.",
    ),
    tabel(
        "Stijgt het reëel bbp, daalt het, of blijft het ongeveer gelijk?",
        [
            ("Nominaal bbp +6 %, prijzen +2 %", "Stijgt"),
            ("Nominaal bbp +3 %, prijzen +3 %", "Blijft ongeveer gelijk"),
            ("Nominaal bbp +1 %, prijzen +4 %", "Daalt"),
        ],
        "Reële groei is ongeveer nominale groei min de prijsstijging.",
        kolommen=["Stijgt", "Blijft ongeveer gelijk", "Daalt"],
    ),
    open_(
        "Leg uit waarom een land met een hoog bbp per capita toch veel arme inwoners kan hebben.",
        "Het bbp per capita is een gemiddelde. Het zegt niets over hoe het inkomen verdeeld is: als een kleine groep heel veel verdient, kan het gemiddelde hoog zijn terwijl veel mensen weinig hebben.",
    ),
]

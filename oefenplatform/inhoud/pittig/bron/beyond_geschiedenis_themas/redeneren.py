"""Redeneren met historische bronnen — pittig (🌍 Beyond).

De bronnen in de casussen zijn oefenbronnen: verzonnen voorbeelden, en dat staat er ook bij.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="betoging-van-bovenaf.svg", zelf=True,
         wat="Eigen tekening: een plein van bovenaf met verspreide betogers en één drukke hoek.",
         vragen="klikvraag over bijsnijden"),
]

VRAGEN = [
    mk(
        "Welke historische vraag is het best onderzoekbaar?",
        [
            "Hoe reageerden Antwerpse dokwerkers in 1900-1914 op machines?",
            "Was het leven van de mensen vroeger in het algemeen zwaarder dan nu?",
            "Hoe leefden de mensen in de hele wereld in het verleden?",
            "Waarom vind ik de middeleeuwen de boeiendste periode?",
        ],
        0,
        "Een tijd, een plaats, een groep en een domein, en er bestaan bronnen over. De andere vragen zijn niet afgebakend of gaan over de eigen smaak.",
    ),
    mk(
        "Een leerling stelt de onderzoeksvraag: \"Was de Eerste Wereldoorlog verschrikkelijk?\" Wat is het grootste probleem?",
        [
            "Je kan ze met ja of nee afdoen, en ze is niet afgebakend",
            "Er bestaan geen bruikbare bronnen meer over de Eerste Wereldoorlog",
            "Een onderzoeksvraag mag nooit over een oorlog gaan",
            "De vraag is te kort om onderzoekbaar te zijn",
        ],
        0,
        "Een ja-neevraag levert geen onderzoek op, en zonder afbakening in tijd en ruimte weet je niet waar je moet zoeken.",
    ),
    tabel(
        "Kan je een historische vraag afbakenen binnen dit domein?",
        [
            ("Het politieke domein", J),
            ("Het economische domein", J),
            ("Het culturele domein", J),
            ("Wat de onderzoeker zelf het leukst vindt", F),
        ],
        "Politiek, sociaal, economisch en cultureel. Eigen smaak is geen domein.",
    ),
    volgorde(
        "Zet de stappen van de bronnenanalyse in de juiste volgorde.",
        ["De context van elke bron verzamelen", "De inhoud van elke bron lezen of bekijken", "Elke bron interpreteren en beoordelen", "De informatie samenbrengen met je historische kennis"],
        "Vier stappen. Zelf een bron maken hoort bij geen enkele stap.",
    ),
    sorteer(
        "Is de bron primair of secundair voor het onderzoek dat erbij staat?",
        ["Primair", "Secundair"],
        [
            ["Een brief van een soldaat uit 1916, voor een onderzoek naar het leven aan het front", "Primair"],
            ["Een handboek uit 2015, voor een onderzoek naar de Russische revolutie", "Secundair"],
            ["Een schoolboek uit 1950, voor een onderzoek naar wat kinderen in 1950 leerden", "Primair"],
            ["Een documentaire uit 2020, voor een onderzoek naar de Franse Revolutie", "Secundair"],
        ],
        "Primair betekent: uit de onderzochte periode zelf. Dat zegt iets over de afstand in tijd, niet over de kwaliteit. En het hangt mee af van je vraag.",
    ),
    tabel(
        "Welke soort bron naar vorm?",
        [
            ("Het dagboek van een verpleegster", "Geschreven"),
            ("Een helm uit een loopgraaf", "Materieel"),
            ("Filmbeelden van een militaire parade", "Audiovisueel"),
            ("Een interview met een grootmoeder over de bevrijding", "Mondeling"),
        ],
        "Brieven en dagboeken zijn geschreven, voorwerpen materieel, foto's en film audiovisueel, en wat iemand vertelt mondeling.",
        kolommen=["Geschreven", "Materieel", "Audiovisueel", "Mondeling"],
    ),
    koppel(
        "Welk begrip uit het contextualiseren past bij elke omschrijving?",
        [
            ["Degene die de bron liet maken, met een bedoeling", "Opdrachtgever"],
            ["Voor wie de bron gemaakt werd", "Doelpubliek"],
            ["Waarom de bron gemaakt werd", "Bedoeling"],
            ["Hoeveel er aan de bron veranderd is voor ze bij jou terechtkwam", "Mate van bewerking"],
        ],
        ["Representativiteit"],
        "Wie, voor wie, waarom en hoeveel bewerkt: zo leer je een bron kennen.",
    ),
    tabel(
        "Hoort het bij het contextualiseren van de maker van een bron?",
        [
            ("Zijn naam, beroep en afkomst", J),
            ("Zijn maatschappelijke positie", J),
            ("Of hij ooggetuige of tijdgenoot was", J),
            ("Het lettertype waarin zijn tekst vandaag gedrukt is", F),
        ],
        "Wie de maker was en waar hij stond, kleurt wat hij schreef.",
    ),
    mk(
        "In je bronnenmap zit een brief zonder datum en zonder naam. Wat is de juiste aanpak?",
        [
            "Noteren dat die contextgegevens ontbreken, en daar rekening mee houden",
            "Een waarschijnlijke datum en maker invullen, zodat de analyse volledig is",
            "De brief meteen weggooien, want zonder maker is hij waardeloos",
            "Aannemen dat de brief uit dezelfde tijd komt als je andere bronnen",
        ],
        0,
        "Een gat benoemen is iets anders dan het met een gok opvullen.",
    ),
    mk(
        "Een officier en een gewone soldaat beschrijven dezelfde slag heel anders. Wat is de beste verklaring?",
        [
            "Elk kijkt vanuit de eigen positie, tijd en belangen",
            "Een van beiden liegt bewust over wat er gebeurde",
            "Officieren mochten in die tijd niet over de oorlog schrijven",
            "Soldaten waren nooit echt bij de gevechten aanwezig",
        ],
        0,
        "Dat heet standplaatsgebondenheid. Een verschil wil niet zeggen dat iemand liegt.",
    ),
    tabel(
        "Waarom geeft een ooggetuige niet altijd een objectief verslag?",
        [
            ("Hij ziet maar een stuk van wat er gebeurt.", J),
            ("Hij kan er zelf belang bij hebben.", J),
            ("Zijn geheugen kan na een tijd verschuiven.", J),
            ("Ooggetuigen mochten vroeger nooit iets opschrijven.", F),
        ],
        "Ooggetuigen zijn waardevol, maar niet vanzelf objectief.",
    ),
    klik(
        "Dit is een tekening van een plein tijdens een betoging, van bovenaf. Een fotograaf houdt enkel het drukste stuk over. Klik op dat stuk.",
        "betoging-van-bovenaf.svg",
        [[60.0, 18.0, 26.0, 42.0]],
        "Wie enkel dat stuk toont, laat de betoging veel groter lijken dan ze was. Er is niets vervalst, en toch klopt het beeld niet meer.",
    ),
    koppel(
        "Bij welk criterium hoort elke richtvraag?",
        [
            ["Geeft de bron een antwoord op mijn historische vraag?", "Bruikbaarheid"],
            ["Had de maker er belang bij om het zo voor te stellen?", "Betrouwbaarheid"],
            ["Zijn er bronnen die op een ander standpunt wijzen?", "Representativiteit"],
            ["Is de bron vertaald, ingekort of bijgesneden?", "Presentatie"],
        ],
        ["Standplaatsgebondenheid"],
        "Vier criteria om een bron te beoordelen, elk met eigen richtvragen.",
    ),
    inv(
        "Je legt drie verslagen van verschillende, onafhankelijke makers naast elkaar, en ze vertellen hetzelfde. Hoe heet die werkwijze? (twee woorden)",
        "bronnen kruisen",
        "Bronnen kruisen versterkt de betrouwbaarheid.",
    ),
    tabel(
        "Verzwakt het de betrouwbaarheid, of heeft het daar op zich geen invloed op?",
        [
            ("De maker schreef het pas jaren later op.", "Verzwakt"),
            ("De bron spreekt andere bronnen tegen.", "Verzwakt"),
            ("De bron is geschreven in een vreemde taal.", "Geen invloed"),
        ],
        "Afstand in tijd en tegenspraak doen twijfelen. Een vreemde taal maakt een bron niet minder betrouwbaar.",
        kolommen=["Verzwakt", "Geen invloed"],
    ),
    mk(
        "Een krant verscheen de ochtend na een grote brand. Is ze daardoor betrouwbaar?",
        [
            "Niet automatisch: een krant van de dag zelf kan vol geruchten zitten",
            "Ja, want hoe dichter bij de gebeurtenis, hoe betrouwbaarder een bron altijd is",
            "Nee, kranten zijn nooit betrouwbare bronnen voor een historicus",
            "Ja, want een krant wordt altijd door meerdere journalisten nagelezen",
        ],
        0,
        "Snel is niet hetzelfde als juist. Ook een bron van kort na de feiten moet je beoordelen.",
    ),
    casus(
        "Oefenbron (verzonnen voorbeeld). Een brief van een Gentse spinster aan haar zus, 1890: \"Wij werken van zes uur 's morgens tot acht uur 's avonds. De opzichter is streng voor de kinderen. Toch ben ik blij dat ik werk heb.\" Je onderzoekt hoe Gentse textielarbeiders in 1890 over hun werk dachten.",
        [
            mk(
                "Wat is het probleem als dit je enige bron is?",
                [
                    "Eén brief zegt weinig over een hele groep",
                    "De brief is te kort om als bron te gebruiken",
                    "Een brief aan een familielid is nooit een primaire bron voor een historicus",
                    "Over 1890 mag je enkel officiële bronnen gebruiken",
                ],
                0,
                "De brief blijft waardevol. Hij toont alleen niet dat iedereen er zo over dacht.",
            ),
            tabel(
                "Mag je dit besluiten op basis van deze brief?",
                [
                    ("Deze vrouw vond haar werk zwaar, maar was blij met werk.", "Mag"),
                    ("Alle arbeiders in Gent dachten er zo over.", "Mag niet"),
                    ("De brief is waardeloos, omdat hij maar over één persoon gaat.", "Mag niet"),
                ],
                "Je besluit over wat de bron echt toont, niet meer en niet minder.",
                kolommen=["Mag", "Mag niet"],
            ),
            mk(
                "Je zoekt meer brieven van arbeiders uit 1890, maar vindt er veel minder dan van fabrikanten. Waarom?",
                [
                    "Arme en ongeletterde groepen lieten minder geschreven bronnen na",
                    "Arbeiders mochten in 1890 bij wet geen brieven naar hun familie schrijven",
                    "Fabrikanten kochten alle brieven van arbeiders op",
                    "Brieven van arbeiders werden na 1945 allemaal vernietigd",
                ],
                0,
                "Wie arm is en niet kan schrijven, laat minder papier na. Daar hou je rekening mee.",
            ),
            mk(
                "Hoe bruikbaar is de brief voor je vraag?",
                [
                    "Rechtstreeks, maar slechts een gedeeltelijk antwoord",
                    "Ze geeft geen enkel antwoord, want ze gaat over een familie en niet over werk",
                    "Ze geeft een volledig antwoord op de vraag",
                    "Ze is onbruikbaar, want de zus kan de brief achteraf veranderd hebben",
                ],
                0,
                "De brief spreekt over het werk zelf, maar maar voor één persoon.",
            ),
        ],
    ),
    casus(
        "Oefenbron (verzonnen voorbeeld). Een groot schilderij uit 1820, besteld door het koninklijk hof, toont de koning op een wit paard in het midden van een veldslag, terwijl de vijand vlucht.",
        [
            mk(
                "Wie is de opdrachtgever van deze bron?",
                ["Het koninklijk hof", "De schilder", "De soldaten op het schilderij", "Wie het schilderij vandaag bekijkt"],
                0,
                "Het hof liet het werk maken en had er dus een bedoeling mee.",
            ),
            mk(
                "Wat besluit je over het beoogde effect van dit schilderij?",
                [
                    "Het zegt vooral iets over hoe de koning gezien wilde worden",
                    "Het toont precies hoe de veldslag verlopen is",
                    "Het bewijst dat de koning persoonlijk de slag gewonnen heeft",
                    "Het wil de kijker afschrikken voor elke vorm van oorlog",
                ],
                0,
                "Het beoogde effect is wat de maker bij zijn publiek wilde teweegbrengen: bewondering voor de koning.",
            ),
        ],
    ),
    casus(
        "Oefenbronnen (verzonnen voorbeelden). De krant van de werkgevers schrijft: \"Slechts enkele onruststokers legden gisteren het werk neer.\" De krant van de vakbond schrijft: \"Duizenden arbeiders staakten gisteren eensgezind.\"",
        [
            mk(
                "Wat doe je met deze tegenspraak?",
                [
                    "Je onderzoekt de standplaats en de bedoeling van elke maker",
                    "Je kiest de bron die je het sympathiekst vindt",
                    "Je laat beide bronnen vallen, want ze spreken elkaar tegen",
                    "Je neemt het gemiddelde van beide aantallen",
                ],
                0,
                "Een tegenspraak is geen probleem maar een aanwijzing.",
            ),
            mk(
                "Wat brengt je het dichtst bij een goed antwoord op de vraag hoeveel mensen staakten?",
                [
                    "Nog bronnen uit andere hoeken zoeken, zoals een politieverslag of een stadsarchief",
                    "Enkel de krant van de werkgevers gebruiken, want die is ouder",
                    "Enkel de krant van de vakbond gebruiken, want die stond dichter bij de arbeiders",
                    "Een eigen schatting maken zonder verdere bronnen",
                ],
                0,
                "Hoe meer verschillende hoeken, hoe vollediger het beeld.",
            ),
            keuze(
                "Een historisch verhaal dat nergens wringt, heeft meestal bronnen [[*weggelaten|gekruist|vertaald]].",
                "Echte bronnen spreken elkaar vaak tegen. Wie geen enkele tegenspraak tegenkomt, heeft maar één hoek bekeken.",
            ),
        ],
    ),
    mk(
        "Een tekst uit 1830 staat vertaald en ingekort in je handboek. Waar let je op?",
        [
            "Dat de betekenis door vertalen en inkorten kan verschoven zijn",
            "Nergens op, want een handboek past een bron nooit op enige manier aan",
            "Dat de tekst daardoor een secundaire bron van 1830 wordt",
            "Dat een vertaalde tekst nooit als bron mag dienen",
        ],
        0,
        "Bewerken kan de betekenis verschuiven. Daarom kijk je hoe een bron aan jou getoond wordt.",
    ),
    mk(
        "Een leerling beoordeelt meteen de betrouwbaarheid van een tekst, zonder te weten wie hem schreef. Wat loopt er mis?",
        [
            "Zonder de maker te kennen, beoordeel je de inhoud slecht",
            "Niets: wie de maker is, speelt geen rol bij het beoordelen",
            "Hij had eerst een eigen bron moeten maken",
            "Hij had de tekst eerst moeten vertalen naar een andere taal",
        ],
        0,
        "Wie de maker en zijn bedoeling kent, leest de inhoud met andere ogen.",
    ),
    mk(
        "Je situeert een bron in de tijd, in de ruimte en in de maatschappelijke domeinen. Van welk hulpmiddel zijn dat de drie vensters?",
        ["Het historisch referentiekader", "Het stappenplan van de bronnenanalyse", "De bronnenkritiek", "De periodisering"],
        0,
        "Hetzelfde kader dat je voor gebeurtenissen gebruikt, gebruik je ook voor bronnen.",
    ),
    mk(
        "Een leerling zegt: \"Deze affiche is propaganda, dus ik gebruik ze niet.\" Wat is de beste reactie?",
        [
            "Ze is zwak over wat er gebeurde, maar sterk over wat men wilde laten geloven",
            "De leerling heeft gelijk: propaganda hoort in geen enkel historisch onderzoek thuis",
            "Propaganda is altijd de betrouwbaarste bron, want de overheid maakte ze",
            "Je mag propaganda enkel gebruiken als ze in je eigen taal geschreven is",
        ],
        0,
        "Het hangt af van je vraag. Over de beeldvorming die een regime wilde, is propaganda net heel bruikbaar.",
    ),
    open_(
        "Je krijgt een foto zonder vermelding van maker of datum en een dagboekfragment van een soldaat. Beschrijf in de juiste volgorde wat je met deze bronnen doet.",
        "Eerst verzamel ik de context: tijd, ruimte, domein, soort bron, maker, opdrachtgever, doelpubliek en bedoeling. Bij de foto noteer ik dat maker en datum ontbreken. Dan lees of bekijk ik de inhoud. Daarna interpreteer en beoordeel ik elke bron op bruikbaarheid, betrouwbaarheid, representativiteit en presentatie. Tot slot breng ik de informatie samen met mijn historische kennis.",
    ),
]

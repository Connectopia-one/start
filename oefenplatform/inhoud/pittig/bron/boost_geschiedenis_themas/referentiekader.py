"""Het historisch referentiekader — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-0-2000.svg", zelf=True,
         wat="Tijdlijn van het jaar 0 tot 2000, een groot streepje om de honderd jaar, jaartallen om de vijfhonderd jaar.",
         vragen="klikvragen op 476, het begin van de vroegmoderne tijd en 1789"),
    dict(bestand="schaalniveaus.svg", zelf=True,
         wat="Schema met vijf gebieden in elkaar: de wereld, Europa, het koninkrijk Frankrijk, het graafschap Vlaanderen, Kortrijk.",
         vragen="klikvraag op het regionale schaalniveau van de Guldensporenslag"),
    dict(bestand="kaart-rijk-karel-v.webp", zelf=False,
         wat="Historische kaart van het rijk van Karel V rond 1550, met de Nederlanden, Spanje, delen van Italië, het Heilige Roomse Rijk en de kolonies in Amerika in één kleur.",
         waar="Wikimedia Commons, zoek op 'Empire of Charles V map' (kies een kaart die vrij te gebruiken is), of een kaart uit een atlas die we mogen tonen.",
         vragen="tabelvraag: een gegeven in de ruimte situeren met een historische kaart"),
    dict(bestand="portret-suleyman.webp", zelf=False,
         wat="Geschilderd portret van sultan Süleyman I (16de eeuw), bijvoorbeeld het portret uit de werkplaats van Titiaan in het Kunsthistorisches Museum in Wenen.",
         waar="Wikimedia Commons, zoek op 'Suleiman the Magnificent portrait Titian' (publiek domein).",
         vragen="meerkeuzevraag: in welke maatschappelijke domeinen hoort het portret"),
]

# De zes nagemaakte prenten van de periodes van Geschiedenis Spark (zelfde bestand).
PERIODES = "/examenvormen/beeld/prenten-periodes.webp"

TL = "tijdlijn-0-2000.svg"

VRAGEN = [
    # --- de drie assen
    tabel(
        "Een leerling situeert de Guldensporenslag van 1302. Welke van deze stappen horen bij het historisch referentiekader?",
        [
            ("Ze plaatst de slag in de middeleeuwen.", J),
            ("Ze zegt dat het om een gebeurtenis bij Kortrijk in het graafschap Vlaanderen gaat.", J),
            ("Ze legt uit dat het om macht én om de verhouding tussen bevolkingsgroepen ging.", J),
            ("Ze rekent uit hoeveel de wapens van de ridders kostten.", F),
        ],
        "Tijd, ruimte en maatschappelijke domeinen zijn de drie assen. Wat iets kostte, is geen as van het kader.",
    ),
    mk(
        "Waarom geeft een datum zonder plaats en zonder domein een scheef beeld?",
        [
            "Een datum is in de geschiedenis altijd onbetrouwbaar en dus nutteloos",
            "Datums horen bij het economische domein en niet bij de tijd",
            "Je weet niet waar het gebeurde en waarmee je het vergelijkt",
            "Zonder plaats is het geen gebeurtenis maar een hele periode",
        ],
        2,
        "Het kader heeft drie assen. Wie er één weglaat, kan de gebeurtenis niet goed plaatsen en niet vergelijken met andere.",
    ),
    # --- structuurbegrippen van de tijd
    koppel(
        "Welk structuurbegrip van de tijd past bij elke zin?",
        [
            ["Terwijl het wereldbeeld in de 16de eeuw verandert, werkt de landbouw nog zoals in 1300.", "Continuïteit"],
            ["De industriële omwenteling duurde meer dan een eeuw, maar veranderde alles.", "Revolutie"],
            ["In de 13de eeuw schrijft men in het Arabische rijk op papier, in Europa op perkament.", "Ongelijktijdigheid"],
            ["Ik zet de val van Rome, de kroning van Karel de Grote en Verdun in de juiste volgorde.", "Chronologie"],
        ],
        ["Periodisering"],
        "Wat blijft duren is continuïteit. Revolutie slaat op de omvang, niet op de snelheid. Dezelfde ontwikkeling die elders al verder staat, is ongelijktijdigheid. In volgorde zetten is chronologie; periodisering geeft stukken tijd een naam.",
    ),
    mk(
        "De industriële revolutie duurde meer dan honderd jaar. Waarom heet ze toch een revolutie?",
        [
            "Ze begon met een gewapende opstand van de fabrieksarbeiders in Manchester en Londen",
            "Het woord gaat over hoe groot de verandering was, niet hoe snel",
            "Elke verandering in het economische domein heet altijd een revolutie",
            "Historici noemen alles wat langer dan een eeuw duurt een revolutie",
        ],
        1,
        "Revolutie gaat over de omvang van de verandering. Ze hoeft niet snel te gaan en niet over politiek te gaan.",
    ),
    tabel(
        "Klopt elke uitspraak over de structuurbegrippen van de tijd?",
        [
            ("Chronologie en periodisering betekenen hetzelfde.", F),
            ("Een evolutie kan ook in het culturele domein voorkomen.", J),
            ("Met duur bedoelt een historicus hoe lang een toestand voortduurt.", J),
            ("Maritiem is een structuurbegrip van de tijd.", F),
            ("Gelijktijdige gebeurtenissen moeten iets met elkaar te maken hebben.", F),
        ],
        "Chronologie ordent, periodisering groepeert. Evolutie en revolutie komen in elk domein voor. Duur is hoe lang iets duurt. Maritiem is een begrip van de ruimte. Gelijktijdige gebeurtenissen kunnen los van elkaar staan.",
    ),
    inv(
        "Hoeveel jaar ligt er tussen 200 v.C. en 300 n.C.? Er bestaat geen jaar 0. Antwoord met een getal.",
        "499",
        "Van 200 v.C. tot 1 v.C. is 199 jaar, van 1 v.C. naar 1 n.C. is 1 jaar, en van 1 n.C. tot 300 n.C. nog 299 jaar: samen 499.",
    ),
    inv(
        "Welk structuurbegrip van de tijd gebruik je voor wat blijft duren, ook al verandert er elders veel? Antwoord met één woord.",
        ["continuïteit", "continuiteit"],
        "Continuïteit is wat blijft, verandering is wat anders wordt. In elke periode zitten ze allebei.",
    ),
    mk(
        "Wat is het verschil tussen gelijktijdigheid en ongelijktijdigheid?",
        [
            "Gelijktijdigheid gaat over de ruimte, ongelijktijdigheid over de maatschappelijke domeinen",
            "Ongelijktijdig: dezelfde ontwikkeling staat op de ene plaats verder dan elders",
            "Ongelijktijdige gebeurtenissen hebben nooit iets met elkaar te maken, gelijktijdige altijd",
            "Er is geen verschil, beide woorden betekenen dat iets lang duurt",
        ],
        1,
        "Gelijktijdig wil zeggen in dezelfde tijd. Ongelijktijdigheid is dezelfde ontwikkeling die op verschillende plaatsen niet even ver staat, zoals papier in het Arabische rijk en perkament in Europa.",
    ),
    # --- periodes en scharnierpunten
    klik(
        "Klik op de tijdlijn op het scharnierpunt tussen de klassieke oudheid en de middeleeuwen.",
        TL, [[23.6, 25, 4.4, 55]],
        "De middeleeuwen beginnen met de val van het West-Romeinse Rijk in 476, net voor het streepje van 500.",
    ),
    klik(
        "Klik op de tijdlijn op de plaats waar de vroegmoderne tijd begint.",
        TL, [[65.8, 25, 5.2, 55]],
        "De vroegmoderne tijd begint met 1453 (val van Constantinopel) of 1492 (Columbus op de Caraïben): net voor het streepje van 1500.",
    ),
    klik(
        "Klik op de tijdlijn op het scharnierpunt waarmee de moderne tijd begint.",
        TL, [[80.0, 25, 3.5, 55]],
        "De moderne tijd begint in 1789, met de Franse Revolutie, net voor het streepje van 1800.",
    ),
    volgorde(
        "Zet de zeven periodes van de westerse periodisering in de juiste volgorde.",
        ["Prehistorie", "Oude nabije oosten", "Klassieke oudheid", "Middeleeuwen", "Vroegmoderne tijd", "Moderne tijd", "Hedendaagse tijd"],
        "Van de tijd vóór het schrift tot vandaag. Voor dit vak ken je de middeleeuwen en de vroegmoderne tijd grondig.",
    ),
    keuze(
        "De Tweede Wereldoorlog situeer je in de [[*moderne tijd|hedendaagse tijd|vroegmoderne tijd]], want de hedendaagse tijd begint pas in [[*1945|1918|1789]].",
        "De moderne tijd loopt van 1789 tot 1945. Pas na de Tweede Wereldoorlog begint de hedendaagse tijd.",
    ),
    dict(
        **tabel(
            "Bekijk de zes nagemaakte prenten: een ziggurat, het Colosseum, een burcht, een zeilschip van de ontdekkingsreizen, een stoomlocomotief en de vlaggen van de Europese Unie. Klopt elke uitspraak?",
            [
                ("Prent 3 en prent 4 horen in twee verschillende periodes.", J),
                ("Prent 5 hoort in dezelfde periode als de Franse Revolutie.", J),
                ("Prent 1 hoort bij de klassieke oudheid.", F),
                ("Prent 6 hoort nog bij de moderne tijd.", F),
            ],
            "De burcht is middeleeuws, het zeilschip hoort bij de vroegmoderne tijd: 1492 ligt ertussen. De stoomlocomotief is van de 19de eeuw, de moderne tijd die in 1789 begint. De ziggurat hoort bij het oude nabije oosten. De Europese Unie ontstond na 1945, in de hedendaagse tijd.",
        ),
        afbeelding_url=PERIODES,
    ),
    mk(
        "Met welke twee principes baken je een periode af?",
        [
            "met de regeringsjaren van een belangrijke koning en de grenzen van zijn rijk",
            "met de eerste en de laatste geschreven bron uit die tijd",
            "met wat de mensen van toen zelf over hun tijd zeiden",
            "met gekozen kenmerken en een symbolische begin- en einddatum",
        ],
        3,
        "Je kiest kenmerken en gebeurtenissen die je belangrijk vindt, en een symbolische begin- en einddatum. Allebei zijn keuzes, dus een periodegrens is altijd voor discussie vatbaar.",
    ),
    mk(
        "Waarom laat men met 1492 een nieuwe periode beginnen?",
        [
            "Daarna veranderen de contacten tussen de continenten blijvend",
            "In dat jaar werd de boekdrukkunst met losse letters uitgevonden in Mainz",
            "In dat jaar viel het West-Romeinse Rijk definitief",
            "Toen begon in Europa de eerste industriële fabriek",
        ],
        0,
        "Met de aankomst van Columbus op de Caraïben veranderen de contacten tussen de continenten voorgoed. Daarom geldt 1492 als scharnierpunt.",
    ),
    tabel(
        "Welke uitspraken over de beperkingen van een periodisering kloppen?",
        [
            ("Ze steunt op een selectie, dus wat niet gekozen is, valt weg.", J),
            ("Ze suggereert een scherpe breuk waar de werkelijkheid geleidelijk is.", J),
            ("Ze past niet even goed op niet-westerse samenlevingen.", J),
            ("Ze maakt het dateren van gebeurtenissen onmogelijk.", F),
        ],
        "De eerste drie zijn echte beperkingen. Dateren blijft wel gewoon mogelijk.",
    ),
    casus(
        "Twee leerlingen discussiëren. Amir: \"De westerse indeling in zeven periodes is de enige juiste, want bijna elk handboek gebruikt ze.\" Lies: \"In China deelt men de geschiedenis in dynastieën in, de islamitische tijdrekening telt vanaf de hidjra en Nederland gebruikt tien tijdvakken. Dus de westerse indeling is fout.\"",
        [
            mk(
                "Wie heeft gelijk?",
                [
                    "Amir, want wat in de meeste handboeken staat, is juist",
                    "Lies, want tien tijdvakken zijn preciezer dan zeven periodes",
                    "Geen van beiden: elke indeling steunt op een keuze van kenmerken",
                    "Allebei, want er bestaat maar één juiste indeling per land",
                ],
                2,
                "Een indeling is een keuze en geen natuurwet. Dat er andere indelingen bestaan, maakt de westerse niet fout, en dat ze veel gebruikt wordt, maakt ze niet de enige juiste.",
            ),
            mk(
                "Wat is een gevolg van zulke verschillende indelingen?",
                [
                    "Een jaartal kan in de ene indeling een grens zijn, in de andere niet",
                    "Een gebeurtenis in China kan je niet dateren met de westerse jaartallen",
                    "Je mag bronnen uit andere landen niet gebruiken",
                    "Het jaar 1492 bestaat niet in de islamitische tijdrekening",
                ],
                0,
                "Elke indeling legt haar grenzen op een andere plaats. Dateren blijft mogelijk; alleen de grenzen en namen verschillen.",
            ),
            open_(
                "Leg in twee zinnen uit waarom je periodiseringen met elkaar vergelijkt.",
                "Niet om te bewijzen welke de beste is, maar om te zien dat elke indeling steunt op een keuze van kenmerken. Zo begrijp je dat een periodegrens een afspraak is en geen natuurwet.",
            ),
        ],
    ),
    # --- ruimte
    klik(
        "De Guldensporenslag was een veldslag bij Kortrijk, maar ook een zaak van een groter gebied. Klik in het schema op het gebied dat bij het regionale schaalniveau van de slag hoort.",
        "schaalniveaus.svg",
        [[22.0, 34.7, 56.0, 12.1], [22.0, 59.7, 56.0, 8.9], [22.0, 46.8, 15.0, 12.9], [63.0, 46.8, 15.0, 12.9]],
        "Kortrijk is het lokale niveau, het graafschap Vlaanderen het regionale. De strijd om Frankrijk en Europa is continentaal; mondiaal, de hele wereld, past hier niet.",
    ),
    sorteer(
        "De ruimtebegrippen vallen in twee rijtjes uiteen. Sleep elk begrip naar het juiste rijtje.",
        ["Hoe groot is het gebied?", "Wat voor gebied is het?"],
        [
            ["lokaal", "Hoe groot is het gebied?"],
            ["nationaal", "Hoe groot is het gebied?"],
            ["continentaal", "Hoe groot is het gebied?"],
            ["mondiaal", "Hoe groot is het gebied?"],
            ["maritiem", "Wat voor gebied is het?"],
            ["ruraal", "Wat voor gebied is het?"],
            ["stedelijk", "Wat voor gebied is het?"],
            ["westers", "Wat voor gebied is het?"],
        ],
        "Lokaal tot mondiaal zegt hoe groot een gebied is. Maritiem, ruraal, stedelijk en westers zeggen wat voor gebied het is.",
    ),
    met_prent(
        "kaart-rijk-karel-v.webp",
        tabel(
            "Bekijk de historische kaart van het rijk van Karel V rond 1550. Klopt elke uitspraak?",
            [
                ("Met deze kaart situeer je het rijk in de ruimte.", J),
                ("De grenzen op de kaart zijn de grenzen van vandaag.", F),
                ("Het rijk had stukken in verschillende delen van Europa en daarbuiten.", J),
                ("Uit de kaart lees je af hoeveel belasting de inwoners betaalden.", F),
            ],
            "Een historische kaart toont het gebied met de grenzen van toen. Leg je ze naast een kaart van vandaag, dan situeer je het rijk in de ruimte. Over belastingen zegt een kaart niets.",
        ),
    ),
    mk(
        "Wat bedoelt men met westers?",
        [
            "Samenlevingen met een gedeelde geschiedenis; de grens is een discussie",
            "Alle landen die op de kaart ten westen van de nulmeridiaan van Greenwich liggen",
            "Alle landen die aan de Atlantische Oceaan grenzen",
            "Een begrip van de tijd dat de moderne periode aanduidt",
        ],
        0,
        "Westers is meer dan een windstreek op de kaart: het slaat op samenlevingen met een gedeelde geschiedenis. Waar die groep ophoudt, is zelf een discussie.",
    ),
    # --- domeinen
    sorteer(
        "In welk maatschappelijk domein hoort elk voorbeeld?",
        ["Politiek", "Sociaal", "Economisch", "Cultureel"],
        [
            ["het absolutisme van Lodewijk XIV", "Politiek"],
            ["migratie", "Sociaal"],
            ["slavernij", "Sociaal"],
            ["e-commerce", "Economisch"],
            ["de geldeconomie", "Economisch"],
            ["de drukkunst", "Cultureel"],
            ["de Reformatie", "Cultureel"],
        ],
        "Macht en bestuur zijn politiek, de verhouding tussen groepen sociaal, produceren en handelen economisch, geloof, kunst en wetenschap cultureel. E-commerce is economisch, hoe modern het ook klinkt.",
    ),
    met_prent(
        "portret-suleyman.webp",
        mk(
            "Bekijk het geschilderde portret van sultan Süleyman I. In welke maatschappelijke domeinen hoort het? (meerdere antwoorden)",
            ["Het politieke domein", "Het culturele domein", "Het economische domein", "Het sociale domein"],
            [0, 1],
            "Het toont de macht van de sultan (politiek) en is een kunstwerk (cultureel). Met het economische of het sociale domein heeft het weinig te maken.",
        ),
    ),
    keuze(
        "Het [[*geografische|politieke|sociale]] domein is geen maatschappelijk domein. Een handelsvloot die specerijen aanvoert, breng je onder bij het [[*economische|maritieme|militaire]] domein.",
        "Er zijn vier maatschappelijke domeinen: politiek, sociaal, economisch en cultureel. Het geografische, maritieme en militaire domein bestaan niet; handel is economisch.",
    ),
    sleep(
        "Het kader heeft drie assen: de [[tijd]], de [[ruimte]] en de [[maatschappelijke domeinen]]. Je gebruikt het om te [[situeren]] en daarna te vergelijken.",
        ["bronnen", "jaartallen", "bewijzen"],
        "Tijd, ruimte en domeinen zijn de assen. Het kader situeert en maakt vergelijken mogelijk; het bewijst niets.",
    ),
    mk(
        "Waarom moet een historische vraag afgebakend zijn in tijd, ruimte en domein?",
        [
            "Omdat een vraag anders te kort is voor een examen",
            "Omdat je ze anders niet met bronnen kan beantwoorden",
            "Omdat elke vraag over de middeleeuwen moet gaan",
            "Omdat je anders het jaartal van de gebeurtenis niet kan uitrekenen",
        ],
        1,
        "Een vraag die niet afgebakend is, is te breed om met bronnen te beantwoorden. Daarom begin je met het kader.",
    ),
    open_(
        "Leg uit waarom de Guldensporenslag in twee maatschappelijke domeinen tegelijk thuishoort.",
        "Ze hoort in het politieke domein, want het ging om de macht over Vlaanderen. En ze hoort in het sociale domein, want het ging ook om de verhouding tussen bevolkingsgroepen in de steden.",
    ),
]

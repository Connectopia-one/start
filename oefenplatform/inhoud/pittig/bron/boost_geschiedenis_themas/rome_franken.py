"""Van Rome naar de Franken — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-400-1000.svg", zelf=True,
         wat="Tijdlijn van 400 tot 1000, een groot streepje om de honderd jaar, een klein om de tien jaar.",
         vragen="klikvragen op 751, 800 en 843"),
    dict(bestand="invallen.svg", zelf=True,
         wat="Schema: het rijk van de Karolingers in het midden, drie pijlen A (noorden), B (zuiden) en C (oosten).",
         vragen="koppelvraag: welk volk viel binnen langs welke kant"),
    dict(bestand="kroning-karel-de-grote.jpg", zelf=False,
         wat="Middeleeuwse miniatuur van de keizerskroning van Karel de Grote door de paus, bijvoorbeeld die uit de Grandes Chroniques de France (14de eeuw).",
         waar="Wikimedia Commons, zoek op 'Coronation of Charlemagne Grandes Chroniques de France' (publiek domein).",
         vragen="tabelvraag over de domeinen en over de prent als bron"),
]

TL = "tijdlijn-400-1000.svg"

VRAGEN = [
    # --- het einde van het West-Romeinse Rijk
    tabel(
        "Klopt elke uitspraak over het einde van het West-Romeinse Rijk?",
        [
            ("Historici zien de val liever als een proces dan als één gebeurtenis.", J),
            ("In hetzelfde jaar viel ook het Oost-Romeinse Rijk.", F),
            ("Een leger dat steeds meer uit ingehuurde Germanen bestond, was een interne oorzaak.", J),
            ("Na de val nam een sterke staat met ambtenaren en een beroepsleger het over.", F),
        ],
        "Het gezag viel over meer dan een eeuw stukje bij beetje weg. Het Oost-Romeinse Rijk bleef nog bijna duizend jaar bestaan. Na de val kwamen er kleinere, zwak bestuurde koninkrijken.",
    ),
    mk(
        "Waarom noemt men 476 een symbolische datering?",
        [
            "Het is een afgesproken grens voor iets wat een eeuw duurde",
            "In dat jaar viel de laatste stad van het rijk na een lang beleg",
            "In dat jaar werd het christendom de godsdienst van het rijk",
            "Het jaartal staat op het oudste bewaarde document van de Kerk",
        ],
        0,
        "In 476 werd de laatste keizer afgezet, maar het rijk viel over meer dan een eeuw uiteen. Het jaartal is een afgesproken scharnierpunt tussen de klassieke oudheid en de middeleeuwen.",
    ),
    # --- de Germaanse migraties
    sorteer(
        "Is dit een interne of een externe oorzaak van de Germaanse migraties?",
        ["Interne oorzaak", "Externe oorzaak"],
        [
            ["bevolkingsgroei", "Interne oorzaak"],
            ["gebrek aan landbouwgrond", "Interne oorzaak"],
            ["de druk van de Hunnen", "Externe oorzaak"],
            ["de rijkdom van het Romeinse rijk", "Externe oorzaak"],
            ["het klimaat van het Romeinse rijk", "Externe oorzaak"],
            ["de verzwakte grensverdediging van Rome", "Externe oorzaak"],
        ],
        "Intern zijn redenen binnen de Germaanse samenlevingen zelf. Wat van buiten de Germaanse wereld komt, zoals de Hunnen of de aantrekkingskracht van Rome, is extern.",
    ),
    mk(
        "Waarom is migratie in deze periode zowel een sociaal als een politiek verschijnsel?",
        [
            "Het verandert wie naast wie woont en wie de macht heeft",
            "Alleen koningen en hun legers trokken toen naar een ander gebied",
            "Het ging altijd gepaard met een oorlog tussen twee keizers",
            "Het verandert enkel de taal die de mensen thuis spreken",
        ],
        0,
        "Wie er naast wie woont, is sociaal. Wie de macht heeft, is politiek. De migraties veranderden allebei.",
    ),
    tabel(
        "Na de migraties ontstaat een gemengde samenleving. Wat bedoelt men daarmee?",
        [
            ("Germaans recht bestond naast Romeins recht.", J),
            ("Iedereen sprak voortaan dezelfde taal.", F),
            ("Oude feesten kregen een christelijke betekenis.", J),
            ("Van elke groep woonden er evenveel mensen.", F),
        ],
        "Gemengd gaat over gewoonten die naast elkaar bestaan en zich vermengen: Germaans, Romeins en christelijk. Het gaat niet over één taal of over aantallen.",
    ),
    sorteer(
        "Werkt dit stuk Romeinse erfenis door in de vroege middeleeuwen of niet?",
        ["Werkt door", "Werkt niet door"],
        [
            ["het Latijn als taal van kerk en bestuur", "Werkt door"],
            ["het wegennet", "Werkt door"],
            ["de indeling in bisdommen", "Werkt door"],
            ["een keizer die door het volk gekozen wordt", "Werkt niet door"],
            ["de Romeinse theaters en badhuizen", "Werkt niet door"],
            ["een beroepsleger betaald met belastingen", "Werkt niet door"],
        ],
        "Taal, wegen en bisdommen blijven. De Romeinse staat met belastingen en beroepsleger verdwijnt, en de theaters gaan niet opnieuw open.",
    ),
    # --- de Merovingers
    inv(
        "Hoe heet de eerste dynastie die over het Frankische rijk regeert? Antwoord met één woord.",
        ["Merovingers", "de Merovingers"],
        "De Merovingers zijn de eerste Frankische dynastie. De Karolingers komen later.",
    ),
    mk(
        "Waarom was de doop van Clovis ook een politieke daad?",
        [
            "Hij won zo de steun van de bisschoppen en de Gallo-Romeinen",
            "De paus maakte hem daarbij meteen tot keizer van het Westen",
            "Zonder doop mocht een Frank volgens de wet geen grond bezitten",
            "Hij kreeg daardoor het Oost-Romeinse Rijk erbij",
        ],
        0,
        "Clovis koos voor het katholieke geloof van de Gallo-Romeinse bevolking en de bisschoppen, en won zo hun steun.",
    ),
    mk(
        "Wat was het gevolg van het Frankische erfrecht voor de koninklijke macht?",
        [
            "Het rijk viel telkens uiteen, met broederoorlogen erbovenop",
            "De koning moest zijn opvolger laten kiezen door de bisschoppen",
            "De macht ging bij elke dood naar de hofmeier van het hof",
            "Het rijk groeide bij elke opvolging, want elke zoon veroverde iets",
        ],
        0,
        "Het rijk werd onder de zonen verdeeld. Daardoor viel het telkens uiteen en volgden er broederoorlogen.",
    ),
    koppel(
        "Welk begrip past bij elke beschrijving?",
        [
            ["de hoogste ambtenaar aan het hof, die in naam van de koning bestuurde", "Hofmeier"],
            ["de laatste koningen van de eerste dynastie, met de titel maar zonder echte macht", "Vadsige koningen"],
            ["een reeks heersers uit dezelfde familie", "Dynastie"],
        ],
        ["Missi dominici"],
        "De hofmeier had de echte macht, de vadsige koningen alleen de titel. Een dynastie is een reeks heersers uit één familie. De missi dominici waren de rondreizende controleurs van Karel de Grote.",
    ),
    # --- de Karolingers
    klik(
        "Klik op de tijdlijn op het jaar waarin Pepijn de Korte zich koning laat maken.",
        TL, [[54.6, 25, 2.9, 55]],
        "Pepijn de Korte wordt in 751 koning en laat zich door de paus zalven.",
    ),
    mk(
        "Wat wilde Pepijn de Korte bereiken met zijn zalving door de paus?",
        [
            "Om zijn machtsovername godsdienstig te laten bevestigen",
            "Omdat de Frankische wet een gezalfde keizer verplichtte",
            "Om de paus te dwingen hem Constantinopel te geven",
            "Omdat de Merovingers het al lang zo deden bij elke kroning",
        ],
        0,
        "De zalving gaf zijn machtsovername een godsdienstige bevestiging. De paus kreeg er een beschermer voor terug.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Karel de Grote in Rome tot keizer gekroond wordt.",
        TL, [[61.7, 25, 2.9, 55]],
        "Karel de Grote wordt in het jaar 800 in Rome tot keizer gekroond.",
    ),
    met_prent(
        "kroning-karel-de-grote.jpg",
        tabel(
            "Bekijk de middeleeuwse miniatuur van de keizerskroning van Karel de Grote. Klopt elke uitspraak?",
            [
                ("Je situeert de kroning in het politieke én in het culturele domein.", J),
                ("De prent toont hoe de paus en de Frankische koning op elkaar steunen.", J),
                ("De miniatuur werd gemaakt door een ooggetuige van de kroning.", F),
                ("Na deze kroning had Karel rechtstreeks gezag over heel Europa.", F),
            ],
            "Een kroning gaat over macht (politiek) en is een godsdienstige plechtigheid (cultureel). Deze miniatuur is eeuwen later gemaakt. Buiten zijn eigen rijk gaf de keizerstitel vooral aanzien.",
        ),
        volgt=True,
    ),
    tabel(
        "Welke middelen gebruikte Karel de Grote om zijn rijk te besturen? Klopt elke uitspraak?",
        [
            ("met graven die elk een gouw bestuurden", J),
            ("met rondreizende controleurs", J),
            ("met wetten en richtlijnen die hij liet opschrijven", J),
            ("met een vast parlement dat de wetten stemde", F),
            ("met ambtenaren betaald uit een Romeins belastingstelsel", F),
        ],
        "Graven, rondreizende controleurs en opgeschreven wetten. Een parlement bestond niet, en het Romeinse belastingstelsel was verdwenen.",
    ),
    mk(
        "Waarom bleven de graven niet altijd trouwe uitvoerders van de koninklijke wil?",
        [
            "Hoe verder van Aken, hoe meer ze hun gouw als eigen bezit zagen",
            "Ze werden elk jaar opnieuw verkozen door de boeren van hun gouw",
            "De paus kon hen op elk moment ontslaan, dus ze volgden hem",
            "Ze moesten elke wet eerst laten goedkeuren door de bisschoppen",
        ],
        0,
        "Ver van het hof was er weinig toezicht. Veel graven gingen hun gouw als hun eigen bezit beschouwen.",
    ),
    mk(
        "Wat hoort bij de Karolingische renaissance?",
        [
            "Kopieerwerkplaatsen en een nieuw, leesbaar schrift",
            "De bouw van de eerste gotische kathedralen in Aken",
            "De uitvinding van de boekdrukkunst aan het hof",
            "De heropening van de Romeinse theaters en badhuizen",
        ],
        0,
        "Aan het hof en in de kloosters werden oude teksten gekopieerd in een nieuw schrift. Gotiek en boekdrukkunst komen pas eeuwen later.",
    ),
    mk(
        "Waarom bereikte de Karolingische renaissance de gewone boeren nauwelijks?",
        [
            "Ze konden niet lezen en kwamen nooit in Aken",
            "Karel de Grote verbood boeren om naar school te gaan",
            "De kloosters lagen allemaal buiten het rijk",
            "Alle teksten waren in het Grieks geschreven",
        ],
        0,
        "Het bleef een zaak van het hof, de kloosters en een kleine groep geletterden.",
    ),
    keuze(
        "Onder de Karolingers werd de koninklijke macht eerst [[*sterker|zwakker]], daarna [[*verbrokkelde|groeide]] ze opnieuw, want het [[*erfrecht|leenstelsel|keizerschap]] bleef gelden.",
        "Karel de Grote versterkte de macht, maar het rijk werd nog altijd onder de zonen verdeeld. Daardoor verbrokkelde het opnieuw.",
    ),
    # --- Verdun en de invallen
    volgorde(
        "Zet deze gebeurtenissen in de juiste volgorde, van vroeg naar laat.",
        [
            "De laatste West-Romeinse keizer wordt afgezet",
            "Clovis laat zich dopen",
            "Pepijn de Korte wordt koning",
            "Karel de Grote wordt keizer",
            "Het rijk wordt in drie delen verdeeld",
            "Noormannen, Saracenen en Hongaren vallen het rijk binnen",
        ],
        "Eerst valt het West-Romeinse Rijk, dan laat Clovis zich dopen. Daarna komen de Karolingers: Pepijn, dan Karel, dan de verdeling onder zijn kleinzonen. De invallen volgen in de 9de en 10de eeuw.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin het rijk van Karel de Grote bij een verdrag in drie delen gesplitst wordt.",
        TL, [[68.0, 25, 2.9, 55]],
        "Die verdeling dateert van 843.",
    ),
    sleep(
        "Bij het Verdrag van Verdun werd het rijk onder drie [[kleinzonen]] van Karel de Grote verdeeld. Daaruit groeiden later [[Frankrijk]] en [[Duitsland]].",
        ["zonen", "Spanje", "Engeland"],
        "Drie kleinzonen kregen elk een deel. Uit die verdeling groeiden later Frankrijk en Duitsland.",
    ),
    mk(
        "Is Verdun een voorbeeld van territoriale eenheid of van verdeeldheid?",
        [
            "Een beoordelingsvraag: in naam één keizerrijk, in feite drie delen",
            "Eenheid, want alle drie de delen hadden dezelfde koning",
            "Verdeeldheid, want het verdrag schafte het keizerrijk meteen helemaal af",
            "Eenheid, want de drie broers bestuurden samen vanuit Aken",
        ],
        0,
        "Het rijk bleef in naam één keizerrijk, maar in feite ontstonden er drie zelfstandige delen. Je antwoord hangt af van hoe je het beoordeelt.",
    ),
    dict(
        **koppel(
            "Bekijk het schema. Welk volk viel in de 9de en 10de eeuw het rijk binnen langs de kant van elke letter?",
            [["A", "Noormannen"], ["B", "Saracenen"], ["C", "Hongaren"]],
            ["Mongolen"],
            "Noormannen uit het noorden, Saracenen uit het zuiden, Hongaren of Magyaren uit het oosten. De Mongolen kwamen pas in de 13de eeuw en bereikten West-Europa niet.",
        ),
        afbeelding_url="/examenvormen/geschiedenis-boost/invallen.svg",
    ),
    mk(
        "Wat was het gevolg van de invallen voor de macht in het rijk?",
        [
            "De bevolking zocht bescherming bij de lokale heer",
            "De koning kreeg meer macht omdat iedereen hem nodig had",
            "Het rijk werd opnieuw één geheel onder één keizer",
            "De Noormannen namen het bestuur in Aken over",
        ],
        0,
        "De lokale heer kon meteen helpen, de verre koning niet. Zo verzwakte het centrale gezag verder.",
    ),
    mk(
        "Wat is het leenstelsel?",
        [
            "Een heer geeft grond in leen voor trouw en krijgsdienst",
            "Een bank die de koning geld leent voor zijn oorlogen",
            "Een stelsel van ambtenaren die de koning betaalt",
            "Een wet die bepaalt dat het rijk onder de zonen verdeeld wordt",
        ],
        0,
        "Macht wordt een keten van persoonlijke afspraken: grond in ruil voor trouw en krijgsdienst.",
    ),
    mk(
        "In welke maatschappelijke domeinen situeer je de zalving van een koning door de paus? (meerdere antwoorden)",
        ["Het politieke domein", "Het culturele domein", "Het economische domein", "Het sociale domein"],
        [0, 1],
        "Het gaat over wie mag heersen (politiek) en het is een godsdienstige plechtigheid (cultureel). Politiek en godsdienst leunden bij de Franken op elkaar.",
    ),
    # --- Karel de Grote als historische vraag
    casus(
        "Drie leerlingen antwoorden op de vraag of Karel de Grote de vader van Europa is. Noor: \"Ja, want onder hem stonden Frankrijk, Duitsland en Italië onder één gezag.\" Bram: \"Nee, hij was een veroveraar die de Saksen met geweld bekeerde.\" Lena: \"Ja, want zonder zijn kopieerwerkplaatsen kenden we veel oude teksten niet.\"",
        [
            mk(
                "Waarom is dit een historische vraag en geen feitenvraag?",
                [
                    "Het antwoord hangt af van wat je onder Europa verstaat",
                    "Er bestaan geen bronnen over Karel de Grote",
                    "Het antwoord staat in een jaartal dat historici kennen",
                    "Alleen de paus kon die titel toekennen",
                ],
                0,
                "Er is geen jaartal dat het beslist. Het antwoord hangt af van hoe je Europa opvat en welke bronnen je kiest.",
            ),
            tabel(
                "Klopt elke uitspraak over de drie leerlingen?",
                [
                    ("Alle drie gebruiken een argument dat op bronnen kan steunen.", J),
                    ("Omdat hun antwoorden verschillen, heeft minstens één van hen een fout gemaakt.", F),
                    ("Bram kijkt vooral naar de veldtochten van Karel.", J),
                    ("Lena kijkt vooral naar het politieke domein.", F),
                ],
                "Alle drie steunen op bronnen. Dat de antwoorden verschillen, is geen fout. Bram kijkt naar de veroveringen; Lena kijkt naar cultuur, niet naar politiek.",
            ),
            open_(
                "Geef in drie zinnen je eigen beargumenteerd antwoord op de vraag.",
                "Karel de Grote bracht Frankrijk, Duitsland en Italië onder één gezag en liet in Aken oude teksten bewaren. Maar hij veroverde ook met geweld, en zijn rijk viel na zijn dood uiteen. Daarom noem ik hem eerder een belangrijke voorloper dan de vader van Europa.",
                "Een goed antwoord weegt argumenten uit bronnen tegen elkaar af. Elk standpunt kan, zolang je het onderbouwt.",
            ),
        ],
    ),
]

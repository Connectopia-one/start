"""Literaire begrippen en genres — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lees het fragment.\n\n"
        "\"Er was eens een vos die een kraai zag zitten met een stuk kaas in haar bek. 'Wat zing je mooi,' riep de vos, 'laat me nog eens horen!' "
        "De kraai opende trots haar bek en de kaas viel recht in de muil van de vos. Wie vleiers gelooft, betaalt de rekening.\"",
        [
            mk(
                "Welk genre is dit?",
                ["Een fabel", "Een sage", "Een epos", "Een parabel"],
                0,
                "Sprekende dieren die menselijke gebreken tonen, met een les op het einde.",
            ),
            keuze(
                "De laatste zin is de [[*moraal|pointe|proloog]] van het verhaal.",
                "Een fabel eindigt met een les voor de lezer.",
            ),
            tabel(
                "Klopt dit over het fragment?",
                [
                    ("Het hoort bij de epiek.", J),
                    ("Het is fictie.", J),
                    ("Het is lyriek.", F),
                ],
                "Er wordt een verhaal verteld, dus epiek. Het is verzonnen, dus fictie.",
            ),
        ],
    ),
    sorteer(
        "Epiek, lyriek of dramatiek?",
        ["Epiek", "Lyriek", "Dramatiek"],
        [
            ["een roman", "Epiek"],
            ["een kortverhaal", "Epiek"],
            ["een gedicht over heimwee", "Lyriek"],
            ["een lied", "Lyriek"],
            ["een toneelstuk", "Dramatiek"],
        ],
        "Epiek vertelt, lyriek zingt, dramatiek speelt.",
    ),
    tabel(
        "Fictie of non-fictie?",
        [
            ("een biografie van een wielrenner", "Non-fictie"),
            ("een dystopische roman", "Fictie"),
            ("een essay over vriendschap", "Non-fictie"),
            ("een historische roman over Napoleon", "Fictie"),
        ],
        "Een historische roman blijft fictie in een historisch decor.",
        kolommen=["Fictie", "Non-fictie"],
    ),
    koppel(
        "Welk genre hoort bij elke omschrijving?",
        [
            ["Een verhaal waarin alles voor iets anders staat", "Allegorie"],
            ["Een verhaal in verhaal", "Raamvertelling"],
            ["Een levenswijsheid in één of twee zinnen", "Aforisme"],
            ["Een lang verhalend gedicht over een held", "Epos"],
        ],
        ["Column", "Recensie"],
        "Vier subgenres uit de termenlijst.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Het overkwam de neef van een collega van mijn moeder. Hij kocht op een markt een tweedehandsjas. In de binnenzak vond hij een briefje: 'Help, ik zit opgesloten in een kledingfabriek.' Echt waar.\"",
        [
            mk(
                "Welk genre is dit vooral?",
                ["Een stadssage", "Een fabel", "Een cultuursprookje", "Een epos"],
                0,
                "Het overkwam altijd een vriend van een vriend. Dat maakt het geloofwaardig en moeilijk na te gaan.",
            ),
            keuze(
                "Een ander woord voor zo'n verhaal is een [[*broodjeaapverhaal|briefroman|aforisme]].",
                "Een stadssage wordt verteld alsof het echt gebeurd is.",
            ),
        ],
    ),
    tabel(
        "Welke soort humor zit in elke zin?",
        [
            ("Bij stromende regen: \"Heerlijk weertje vandaag.\"", "Ironie"),
            ("\"Goed gedaan, weer gebuisd. Je bent echt een genie.\"", "Sarcasme"),
            ("Een toespraak van een minister nagedaan in de stijl van een sportcommentator", "Parodie"),
        ],
        "Sarcasme is ironie met een scherpe, kwetsende kant. Een parodie imiteert een stijl.",
        kolommen=["Ironie", "Sarcasme", "Parodie"],
    ),
    mk(
        "Een cabaretier hekelt in een sketch hoe politici beloften breken. Welke vorm van humor is dat vooral?",
        ["Satire", "Taalhumor", "Situatiehumor", "Een woordspeling"],
        0,
        "Een satire mikt op de inhoud: ze klaagt een misstand aan.",
    ),
    tabel(
        "Welk romangenre is elk boek?",
        [
            ("een roman die bestaat uit mails tussen twee zussen", "Briefroman"),
            ("een roman over een meisje dat volwassen wordt", "Bildungsroman"),
            ("een roman over een samenleving waar alles bewaakt wordt", "Dystopie"),
            ("een roman met echte politici achter verzonnen namen", "Sleutelroman"),
        ],
        "Elk genre heeft een herkenbaar kenmerk.",
        kolommen=["Briefroman", "Bildungsroman", "Dystopie", "Sleutelroman"],
    ),
    mk(
        "Een roman speelt in een vervallen kasteel, met geheime gangen, kaarslicht en een gevoel van onheil. Welk genre?",
        ["Gothic novel", "Streekroman", "Schelmenroman", "Tendensroman"],
        0,
        "Kastelen, geheimen en dreiging: het gothic register.",
    ),
    tabel(
        "Klopt dit over romangenres?",
        [
            ("Eén roman kan tot meerdere genres behoren.", J),
            ("Een historische roman moet in elk detail kloppen.", F),
            ("Literaire non-fictie bestaat.", J),
            ("Een novelle is langer dan een roman.", F),
        ],
        "Genres sluiten elkaar niet uit. Een novelle zit tussen kortverhaal en roman.",
    ),
    casus(
        "Een schrijfster vertelt in een roman over een meisje dat opgroeit in een Limburgs mijndorp. Ze verwerkt veel uit haar eigen jeugd, maar verandert namen en verzint scènes. Het dorp, het dialect en de gebruiken van de streek dragen het verhaal.",
        [
            tabel(
                "Welke genres passen bij deze roman?",
                [
                    ("autobiografische roman", J),
                    ("streekliteratuur", J),
                    ("Bildungsroman", J),
                    ("briefroman", F),
                ],
                "Eigen leven, één streek en het opgroeien van een personage. Brieven komen er niet in voor.",
            ),
            mk(
                "Mag je alles uit het boek als waar gebeurd beschouwen?",
                [
                    "Nee, het blijft een roman",
                    "Ja, want ze schrijft over haar eigen leven",
                    "Ja, want het dorp bestaat echt",
                    "Nee, want streekliteratuur is altijd verzonnen",
                ],
                0,
                "Autobiografisch betekent over het eigen leven, maar als roman geschreven en dus niet noodzakelijk waar.",
            ),
        ],
    ),
    mk(
        "Waarin verschilt een cultuursprookje van een volkssprookje?",
        [
            "Een cultuursprookje heeft een bekende auteur",
            "Een volkssprookje heeft altijd een moraal",
            "Een cultuursprookje heeft geen sprekende dieren",
            "Een volkssprookje speelt altijd in een stad",
        ],
        0,
        "Een volkssprookje groeide mondeling; een cultuursprookje is door een schrijver bedacht.",
    ),
    sleep(
        "[[Proza]] loopt door in zinnen en alinea's. [[Poëzie]] werkt met verzen en strofen. Een tekst met verschillende betekenislagen is [[gelaagd]].",
        ["canon", "dramatiek"],
        "Drie algemene literaire begrippen.",
    ),
    tabel(
        "Klopt dit over de canon?",
        [
            ("Het is een reeks werken die als belangrijk beschouwd wordt.", J),
            ("Wie hem samenstelt, bepaalt mee wat belangrijk heet.", J),
            ("Hij ligt voor altijd vast.", F),
        ],
        "Een canon is een keuze, en dus betwistbaar.",
    ),
    mk(
        "Een kort verhaal over een zaaier wiens zaad op verschillende grond valt, om iets over geloof uit te leggen. Wat is dat?",
        ["Een parabel", "Een legende", "Een fabel", "Een aforisme"],
        0,
        "Een parabel zet een alledaags beeld in om een diepere les over te brengen.",
    ),
    tabel(
        "Komt dit genre uit de mondelinge traditie?",
        [
            ("de mythe", J),
            ("de legende", J),
            ("de column", F),
            ("de sage", J),
        ],
        "Een column is een modern krantengenre met een herkenbare auteur.",
    ),
    mk(
        "Waarom gebruik je best de juiste literaire term als je over een boek praat?",
        [
            "Eén woord zegt wat anders een alinea kost",
            "Leraren geven punten per gebruikte vakterm",
            "Zonder vakterm mag je geen mening geven",
            "De term bepaalt of het boek goed is",
        ],
        0,
        "Wie \"sleutelroman\" zegt, hoeft het verschijnsel niet uit te leggen.",
    ),
    keuze(
        "Middeleeuwse verhalen over Karel de Grote horen bij de [[*Karelepiek|Arthurroman|gothic novel]].",
        "De Arthurroman draait rond koning Arthur.",
    ),
    mk(
        "Een detectiveroman waarin de lezer tot het einde moet raden wie de moord pleegde, heet ook een ...",
        ["Whodunit", "Tendensroman", "Sleutelroman", "Allegorie"],
        0,
        "Van \"who has done it\": de spanning zit in het zoeken naar de dader.",
    ),
    tabel(
        "Een graphic novel. Klopt dit?",
        [
            ("Het is een verhaal in beeld en tekst.", J),
            ("Het heet ook een striproman.", J),
            ("Het kan niet literair zijn.", F),
        ],
        "Een graphic novel heeft de lengte en thematiek van een roman.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Lieve Marthe,\nHier in Kaapstad regent het al drie dagen. Ik mis je, en ik mis de geur van onze bakkerij. Schrijf me snel terug.\nJe Anna\"\n\n"
        "\"Lieve Anna,\nDe bakkerij is verkocht. Ik wist niet hoe ik het je moest zeggen.\nMarthe\"",
        [
            mk(
                "Als de hele roman zo is opgebouwd, welk genre is het?",
                ["Een briefroman", "Een sleutelroman", "Een raamvertelling", "Een schelmenroman"],
                0,
                "Alles wat je weet, komt uit wat de personages elkaar schrijven.",
            ),
            tabel(
                "Klopt dit over deze vorm?",
                [
                    ("Er is geen alwetende verteller die alles uitlegt.", J),
                    ("Je kent enkel wat de personages zelf schrijven.", J),
                    ("Het is dramatiek, want er zijn twee personages.", F),
                ],
                "Een briefroman blijft epiek: er wordt een verhaal verteld, alleen via brieven.",
            ),
        ],
    ),
    mk(
        "Een roman volgt een sluwe jongen die van baas tot baas trekt en iedereen bedriegt. Welk genre?",
        ["Een schelmenroman", "Een psychologische roman", "Een sleutelroman", "Een tendensroman"],
        0,
        "De schelm overleeft met list en bedrog, avontuur na avontuur.",
    ),
    keuze(
        "Een roman die de lezer wil overtuigen dat kinderarbeid moet stoppen, is een [[*tendensroman|whodunit|gothic novel]].",
        "De tendens is de strekking: de roman wil je iets doen vinden.",
    ),
    tabel(
        "Klopt dit over Young Adult-literatuur?",
        [
            ("Ze is geschreven voor jongvolwassenen.", J),
            ("De leeftijd van de schrijver bepaalt het genre.", F),
            ("Een Young Adult-roman kan ook een dystopie zijn.", J),
        ],
        "De doelgroep bepaalt het genre.",
    ),
    open_(
        "Leg het verschil uit tussen een utopie en een dystopie, met een eigen voorbeeld van een verhaal.",
        "Een utopie toont een ideale samenleving, een dystopie een samenleving die is misgelopen. Voorbeeld van een dystopie: een verhaal over een land waar een app elke beweging van de burgers bijhoudt en wie slecht scoort, geen werk meer krijgt.",
    ),
]

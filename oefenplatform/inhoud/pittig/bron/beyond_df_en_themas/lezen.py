"""Een Engelse tekst lezen — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the text.\n\n« Every year more young people in Britain start a part-time job while they are still at school. "
        "Most of them work in shops or cafés at the weekend. They earn their own money, and they learn to deal with customers. "
        "However, teachers are worried. Pupils who work more than ten hours a week often get lower marks, because they are too tired to study. "
        "So the advice is simple: a small job is fine, but school comes first. »",
        [
            mk("Wat is het onderwerp van de tekst?",
               ["bijbaantjes van scholieren", "Britse winkels en hun klanten", "de punten op een Brits rapport", "het weekend van Britse leraren"], 0,
               "De hele tekst gaat over jongeren met een bijbaantje."),
            mk("Wat is de hoofdgedachte?",
               ["Een klein bijbaantje is oké, maar school gaat voor.", "Scholieren moeten in het weekend in een winkel werken.",
                "Leraren willen dat scholieren meer geld verdienen.", "Wie werkt, haalt altijd betere punten op school."], 0,
               "Het slot vat de boodschap samen: school comes first."),
            keuze("Het signaalwoord « However » kondigt een [[*tegenstelling|gevolg|opsomming]] aan.", "Na de voordelen komt de zorg van de leraren."),
            keuze("« because they are too tired » geeft een [[*reden|voorbeeld]].", "Because geeft de oorzaak van de lagere punten."),
            inv("Vanaf hoeveel uur per week halen scholieren volgens de tekst vaak lagere punten? Geef het getal.", ["10", "tien"],
                "More than ten hours a week."),
        ],
    ),
    casus(
        "Read the message on the website of a sports centre.\n\n« From Monday 4 March the swimming pool will be closed for repairs. "
        "The gym and the tennis courts stay open as usual. Members can use the pool in Riverside free of charge during this period. "
        "Show your card at the desk. We expect to open again on 1 April. Sorry for the trouble! »",
        [
            mk("Wat is gesloten vanaf 4 maart?",
               ["het zwembad", "de fitnesszaal en het zwembad", "de tennisvelden achter de zaal", "het hele sportcentrum"], 0,
               "Enkel the swimming pool sluit; de rest blijft open."),
            keuze("« free of charge » betekent [[*gratis|tegen betaling]].", "Leden mogen gratis naar Riverside."),
            mk("Wat moeten leden in Riverside doen?",
               ["hun kaart tonen aan de balie", "vooraf een plaats reserveren", "een extra bijdrage betalen", "hun eigen handdoek meebrengen"], 0,
               "Show your card at the desk."),
            keuze("Het zwembad gaat normaal weer open op [[*1 april|4 maart|1 maart]].", "We expect to open again on 1 April."),
            keuze("Het woord « repairs » kan je raden: het zwembad wordt [[*hersteld|verkocht|gebouwd]].", "Repair lijkt op repareren."),
        ],
    ),
    mk("Lees: « Jack bought a second-hand guitar. It was cheap, but it sounds great. » Naar wat verwijst it?",
       ["de gitaar", "het geld dat Jack betaalde", "de winkel waar Jack was", "het liedje dat Jack speelt"], 0,
       "It zoekt een ding in de zin ervoor: the guitar."),
    mk("Lees: « Emma and her cousin went to the zoo. Their favourite animals were the penguins. » Naar wie verwijst their?",
       ["Emma en haar neef", "alleen Emma", "de pinguïns in de zoo", "de mensen van de zoo"], 0,
       "Their is meervoud en verwijst naar de twee personen."),
    mk("Lees: « The road was blocked, so we took a different route. » Wat betekent blocked?",
       ["versperd", "pas aangelegd", "heel erg druk", "goed verlicht"], 0,
       "Het gevolg (een andere weg nemen) verraadt de betekenis."),
    mk("Lees: « Tickets cost £12 for adults. Children under five go in free. » Hoeveel betaalt een kind van drie?",
       ["niets", "12 pond", "de helft van 12 pond", "5 pond"], 0, "Under five go in free."),
    mk("Lees: « I wanted to go to the beach. Instead, I stayed home and cleaned my room. » Wat deed de schrijver?",
       ["thuisblijven en opruimen", "naar het strand gaan", "eerst opruimen en dan naar het strand", "naar het strand met een vriend"], 0,
       "Instead: in plaats daarvan."),
    mk("Lees: « Plastic bags are bad for the sea. For example, turtles often eat them. » Wat doet de tweede zin?",
       ["een voorbeeld geven", "een tegenstelling geven", "het besluit van de tekst geven", "een nieuw onderwerp beginnen"], 0,
       "For example kondigt een voorbeeld aan."),
    tabel("Lees: « Our café is open every day from 8 a.m. to 6 p.m., except on Wednesday. We sell coffee, tea and homemade cakes. » Klopt dit?", [
        ("Het café is op woensdag gesloten.", J), ("Je kan er om 7 uur 's avonds nog binnen.", F),
        ("Ze verkopen zelfgemaakte taart.", J), ("Het café is ook op zondag open.", J),
    ], "Except on Wednesday; 6 p.m. is 18 uur."),
    tabel("Lees: « Leo is fifteen. He lives in Leeds with his mum and his two sisters. His dad lives in Spain. » Klopt dit?", [
        ("Leo heeft twee zussen.", J), ("Leo woont bij zijn papa.", F), ("Leo's papa woont in Spanje.", J),
    ], "His dad lives in Spain; Leo woont bij zijn mama."),
    tabel("Lees de zin en duid aan wat de hoofdzaak en wat een bijzaak is: « The festival raised £5,000 for the hospital. It was a sunny day and many people wore hats. »", [
        ("Het festival bracht geld op voor het ziekenhuis.", "hoofdzaak"),
        ("Het was een zonnige dag.", "bijzaak"),
        ("Veel mensen droegen een hoed.", "bijzaak"),
    ], "Het geld voor het ziekenhuis is de boodschap; het weer is een detail.", kolommen=["hoofdzaak", "bijzaak"]),
    koppel("Koppel elk signaalwoord aan wat het aankondigt.", [
        ["but", "een tegenstelling"], ["so", "een gevolg"], ["because", "een reden"], ["finally", "de laatste stap"],
    ], ["een vraag"], "Signaalwoorden tonen hoe zinnen samenhangen."),
    volgorde("Lees: « After lunch we visited the castle. In the morning we took the train to York. In the evening we had dinner by the river. » Zet de activiteiten in de juiste volgorde.", [
        "de trein naar York nemen", "het kasteel bezoeken", "eten aan de rivier",
    ], "In the morning, after lunch, in the evening."),
    inv("Lees: « The bus leaves at 7.45 a.m. and the trip takes twenty minutes. » Hoe laat komt de bus aan? Schrijf als 8.05.", ["8.05", "8:05", "8u05"],
        "7.45 + 20 minuten = 8.05."),
    inv("Lees: « My grandmother is eighty, but she still goes swimming twice a week. » Hoeveel keer per week gaat ze zwemmen? Geef het getal.", ["2", "twee"],
        "Twice a week: twee keer."),
    inv("Lees: « The word 'unfriendly' means not friendly. » Welk Engels woord betekent dan niet bekend? Begin met un-.", ["unknown"],
        "Un- maakt een woord ontkennend."),
    keuze("Lees: « Sam was nervous before the test. His hands were shaking. » Nervous betekent [[*zenuwachtig|blij|moe]].",
          "Trillende handen verraden de betekenis."),
    keuze("Lees: « Although the hotel was expensive, we enjoyed our stay. » Although betekent [[*hoewel|omdat|daarna]].",
          "Een tegenstelling: duur, en toch genoten."),
    keuze("Lees: « Eventually the train arrived, two hours late. » Eventually betekent [[*uiteindelijk|eventueel]].",
          "Een valse vriend: eventually is uiteindelijk."),
    mk("Lees: « Mia is a nurse. Every night she cares for patients in the city hospital. » Welke informatie is hier een hoofdpunt?",
       ["Mia werkt als verpleegster", "het ziekenhuis ligt in de stad", "Mia werkt zowel 's nachts als overdag", "Mia heeft zelf ook ooit in het ziekenhuis gelegen"], 0,
       "Het beroep is de kern; waar het ziekenhuis ligt is een detail."),
    mk("Lees: « Recycling at home is easy. First, rinse your bottles. Then put them in the blue bin. » Wat doe je eerst?",
       ["de flessen uitspoelen", "de flessen in de blauwe bak leggen", "de blauwe bak buiten zetten", "de flessen naar de winkel brengen"], 0,
       "First, rinse your bottles."),
    open_("Lees: « Last year Tom forgot his passport, so he missed his flight to Rome. This year he packed it a week before. » Leg in het Nederlands uit waarom Tom dit jaar zo vroeg pakte.",
          "Omdat hij vorig jaar zijn paspoort vergat en daardoor zijn vlucht miste.",
          "So geeft het gevolg; de tweede zin toont wat hij eruit leerde."),
]

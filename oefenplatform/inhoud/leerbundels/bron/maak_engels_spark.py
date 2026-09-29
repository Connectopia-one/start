# -*- coding: utf-8 -*-
"""De leerbundels voor Engels op ✨ Spark-niveau.

Gebaseerd op de vakfiche Engels 1ste graad A-stroom (geldig in 2027) die Kim
aanleverde.

Let op: dit vak oefent **alleen het schriftelijke Engels**. Het examen van de
Examencommissie bestaat ook uit luisteren, spreken en twee gesprekken, en dat
kan een oefenplatform met tekstvragen niet nabootsen. Dat staat ook met zoveel
woorden in de eerste bundel, zodat niemand denkt dat dit het hele examen dekt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. De bundel wordt dus
twee keer geüpload, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/engels.json` doet daar
het voorwerk voor; daarna gaat elke vraag nog één voor één naast de tekst.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Engels"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

SCHRIFTELIJK = (
    "<strong>Dit oefenplatform oefent alleen het schriftelijke Engels.</strong> Het examen "
    "van de Examencommissie telt zeven onderdelen: lezen (30 %), luisteren (30 %), schrijven "
    "(8 %), schriftelijke interactie (8 %), spreken (8 %) en twee mondelinge gesprekken "
    "(elk 8 %). Luisteren, spreken en de gesprekken oefen je hier niet: daar heb je geluid "
    "en een gesprekspartner voor nodig. Wat je hier wél oefent — lezen, schrijven, "
    "schriftelijke interactie, woordenschat en grammatica — is samen goed voor 46 % van je "
    "punten, en je hebt het ook nodig om te kunnen luisteren en spreken."
)

BUNDELS = {}

# ---------------------------------------------------------------------------

BUNDELS["een-engelse-tekst-lezen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Een Engelse tekst lezen",
    onder="Het onderwerp, de hoofdgedachte en de hoofdpunten vinden, ook als je niet elk woord kent.",
    secties=[
        dict(kop="Waarvoor dient dit vak hier?", blokken=[
            ("kader", SCHRIFTELIJK),
            ("p", "Lezen is met 30 % het zwaarste onderdeel dat je hier kan inoefenen, "
                  "evenveel als luisteren. En wie vlot leest, herkent dezelfde woorden ook "
                  "terug als hij ze hoort. Het niveau van de eerste graad is A2 van het "
                  "Europees referentiekader, maar reken erop dat je ook iets uitdagenders "
                  "krijgt."),
        ]),
        dict(kop="Drie lagen in elke tekst", blokken=[
            ("p", "Het <strong>onderwerp</strong> is waarover een tekst gaat. Je zegt het in "
                  "één of enkele <strong>woorden</strong>, bijvoorbeeld 'de nieuwe "
                  "fietsenstalling'. Je schrijft het dus niet op in een volledige zin."),
            ("p", "De <strong>hoofdgedachte</strong> is de belangrijkste boodschap, in "
                  "één <strong>zin</strong>: 'De school heeft een nieuwe fietsenstalling voor "
                  "leerlingen.' De <strong>hoofdpunten</strong> zijn de inhoudelijke elementen "
                  "die die hoofdgedachte <strong>ondersteunen</strong>: leerlingen mogen er "
                  "gratis parkeren, en de stalling is open van 8 tot 5."),
            ("fig", svg.kernpiramide(),
             "Onderwerp in enkele woorden, hoofdgedachte in één zin, daaronder de punten die haar dragen."),
            ("kader", "<strong>Doe het eens op een echte tekst.</strong> <em>Our school has a "
                      "new bike shed. Students can park their bikes there for free. The shed "
                      "is open from 8 a.m. until 5 p.m.</em><br>"
                      "Het <strong>onderwerp</strong> is 'de nieuwe fietsenstalling'. De "
                      "<strong>hoofdgedachte</strong> is 'de school heeft een nieuwe "
                      "fietsenstalling voor leerlingen'. De twee <strong>hoofdpunten</strong> "
                      "zijn de zinnen die dat staande houden: gratis parkeren, en de "
                      "openingsuren."),
            ("p", "Pas op met wat er <strong>niet</strong> staat. In die tekst staat niets "
                  "over gezondheid of over fietsen dat goed is voor het milieu. Hoe logisch het "
                  "ook klinkt: als het er niet staat, is het geen hoofdpunt."),
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a bike shed", "een fietsenstalling"],
                ["for free", "gratis"],
                ["a film review", "een filmbespreking, een recensie"],
                ["an actor, actors", "een acteur, acteurs"],
                ["a costume", "een kostuum"],
                ["to pick up", "oprapen"],
                ["a bag", "een zak"],
                ["inhabitants", "inwoners"],
                ["famous for", "beroemd om"],
                ["nobody", "niemand"],
            ]), "Woorden uit de leesteksten van dit hoofdstuk."),
        ]),
        dict(kop="Informatie selecteren", blokken=[
            ("p", "Soms hoef je de tekst niet helemaal te begrijpen: je moet er één ding "
                  "<strong>uit halen</strong>. Hoeveel kost de schoolreis? Hoe laat vertrekt de "
                  "bus? Waar is het feest? Dan lees je <strong>gericht</strong>: je weet wat je "
                  "zoekt en je zoekt het op, in plaats van elk woord te vertalen."),
            ("kader", "<em>The school trip to London costs 180 euros. Please pay before "
                      "15 March. The bus leaves at 6 a.m.</em><br>"
                      "Kost: 180 euro. Betalen: <em>before</em> (vóór) 15 maart. Vertrek: "
                      "6 <strong>a.m.</strong>, dus 's ochtends. <em>A.m.</em> is vóór de "
                      "middag, <em>p.m.</em> erna. Wie dat verwart, staat twaalf uur naast de "
                      "afspraak."),
            ("p", "Let ook op de <strong>dagen</strong>: <em>Saturday</em> is zaterdag, "
                  "<em>Sunday</em> is zondag. <em>On Sundays</em> met een -s betekent élke "
                  "zondag."),
        ]),
        dict(kop="Strategieën: wat doe je vóór en tijdens het lezen?", blokken=[
            ("p", "De vakfiche somt strategieën op die je mag en moet gebruiken. Ze staan er "
                  "niet voor de sier: ze schelen punten."),
            ("fig", tabel(["strategie", "wat je doet"], [
                ["jezelf vragen stellen", "Wat weet ik al over dit onderwerp? Waarover zou de tekst kunnen gaan?"],
                ["het communicatiemodel", "Van wie is de tekst? Waarom is hij gemaakt? Voor wie is hij bedoeld?"],
                ["visuele hulpmiddelen", "de titel en de tussentitels, woorden in het vet, een foto, een tekening of een grafiek"],
                ["structuuraanduiders", "verwijswoorden (they, there) en signaalwoorden (first, next, finally)"],
                ["betekenis afleiden", "uit de context, uit je voorkennis, uit de vorm van het woord, uit het Nederlands of het Frans"],
                ["beslissen wat je opzoekt", "Is dit woord echt nodig om de tekst te begrijpen? Alleen dan het woordenboek."],
            ]), "De strategieën uit de vakfiche, in de volgorde waarin je ze gebruikt."),
            ("p", "Dat laatste is belangrijk. Je <strong>mag</strong> tijdens het digitale "
                  "examen een online woordenboek gebruiken, maar je hebt geen tijd om elk woord "
                  "op te zoeken. Je moet dus niet elk Engels woord kennen: je moet kunnen "
                  "beslissen wélk woord ertoe doet."),
            ("kader", "<em>The train leaves at eight, but it is often delayed.</em> Je kent "
                      "<em>delayed</em> niet. De zin gaat over een trein en draait met "
                      "<em>but</em>, dus het is iets vervelends: <strong>vertraagd</strong>. "
                      "Zo leid je een betekenis af uit de context, zonder op te zoeken."),
            ("weetje", "Ook de vorm van een woord helpt. <em>Unhappy</em> is <em>happy</em> met "
                       "<em>un-</em> ervoor, dus niet blij. Zo werken ook <em>impossible</em> en "
                       "<em>dislike</em>."),
        ]),
        dict(kop="Verwijswoorden: wie is 'he'?", blokken=[
            ("p", "Een tekst hangt aan elkaar met <strong>verwijswoorden</strong>. <em>Tom was "
                  "late again. He had missed the bus.</em> — <em>he</em> is Tom. Zulke woorden "
                  "sparen herhaling uit, maar je moet wel weten waarnaar ze wijzen, anders "
                  "begrijp je de tekst verkeerd."),
            ("p", "Ook <strong>signaalwoorden</strong> sturen je: <em>so</em> kondigt een "
                  "gevolg aan (<em>The weather was terrible, so we stayed at home</em>), "
                  "<em>because</em> een oorzaak, <em>but</em> een tegenstelling."),
        ]),
        dict(kop="Wat voor tekst heb je voor je?", blokken=[
            ("p", "Zodra je ziet wat voor soort tekst het is, weet je wat je mag verwachten. "
                  "<em>Please do not feed the animals. Keep your dog on a lead.</em> — dat zegt "
                  "wat je moet doen, dus het is een <strong>prescriptieve</strong> tekst. "
                  "<em>Once upon a time, a poor boy lived near a dark forest.</em> — dat "
                  "vertelt, dus <strong>narratief</strong>. <em>I think school should start "
                  "later.</em> — dat is een mening, dus <strong>opiniërend</strong>. De vijf "
                  "soorten staan uitgewerkt in de bundel bij het volgende hoofdstuk."),
        ]),
        dict(kop="Tien korte teksten, uitgewerkt", blokken=[
            ("p", "Lezen leer je door te lezen. Hieronder staan tien tekstjes zoals je ze op "
                  "het examen krijgt. Lees telkens eerst het Engels, en kijk dan wat de "
                  "uitleg eronder ermee doet."),
            ("kader", "<strong>1. Een filmreview.</strong> <em>I saw the new Spider-Man film "
                      "last Saturday. The story is not very original, but the actors are great "
                      "and the costumes look amazing. I loved it, and I still think about the "
                      "last scene.</em><br>"
                      "De schrijver vindt de film prachtig: <em>great</em>, <em>amazing</em>, "
                      "<em>I loved it</em>. De acteurs spelen goed. Maar let op <em>but</em>: "
                      "het verhaal (<em>the story</em>) vindt hij niet origineel. Een mening is "
                      "zelden helemaal positief, en <em>still</em> betekent hier nog altijd."),
            ("kader", "<strong>2. De speelplaats.</strong> <em>Every Friday our class cleans "
                      "the schoolyard. Last week we filled three bags with paper and "
                      "plastic.</em><br>"
                      "Elke vrijdag ruimt de klas de speelplaats op. Vorige week vulden ze drie "
                      "zakken met papier en plastic. Hoeveel zakken waren het? Drie. Dat is "
                      "gericht lezen: je haalt er één ding uit."),
            ("kader", "<strong>3. Een bericht dat zich verontschuldigt.</strong> <em>Sorry, I "
                      "can\'t come to your party. I have to visit my grandmother.</em><br>"
                      "De schrijver van dit bericht verontschuldigt zich: hij kan niet naar het "
                      "feest komen, want hij moet op bezoek bij zijn grootmoeder."),
            ("kader", "<strong>4. Een recept.</strong> <em>Put the pasta in boiling water. Cook "
                      "for eight minutes, then add the sauce.</em><br>"
                      "Een recipe is een recept, en dit is een prescriptieve tekst: hij zegt "
                      "wat je moet doen. Hoeveel minuten koken? Acht minutes. <em>Boiling "
                      "water</em> is kokend water, <em>sauce</em> is saus."),
            ("kader", "<strong>5. Openingsuren.</strong> <em>The museum is closed on Mondays. "
                      "The garden is open every day.</em><br>"
                      "Het museum is op maandag gesloten (dicht), de tuin is elke dag open. "
                      "<em>On Mondays</em> met een -s betekent élke maandag."),
            ("kader", "<strong>6. Een reisverslag.</strong> <em>We arrived in Scotland on "
                      "Monday. It rained every day, but the mountains were beautiful.</em><br>"
                      "Ze kwamen maandag aan in Schotland. Het regende elke dag, en ondanks die "
                      "regen vonden ze de bergen prachtig. Weer dat <em>but</em>: het draait de "
                      "zin om."),
            ("kader", "<strong>7. Een stukje uit een krant.</strong> <em>Teenagers who look at "
                      "screens late at night sleep less well.</em><br>"
                      "Wie denkt dat dit over school gaat, leest te snel. Het gaat over "
                      "tieners, schermen en slaap. Wie tot laat in de nacht naar een scherm "
                      "kijkt, slaapt minder goed en is de dag erna moe (<em>tired</em>)."),
            ("kader", "<strong>8. Een affiche.</strong> <em>School party! Friday, 7 p.m. on the "
                      "playground. Tickets: 5 euros.</em><br>"
                      "Een schoolfeest, op vrijdag om zeven uur \'s avonds, op de speelplaats. "
                      "Het bedrag staat op de laatste regel: vijf euro."),
            ("kader", "<strong>9. De weg vragen.</strong> <em>Excuse me, could you tell me the "
                      "way to the station?</em><br>"
                      "De spreker vraagt de weg naar het station. <em>Could you</em> is de "
                      "beleefde vorm. Het antwoord noemt vaak een herkenningspunt: <em>go "
                      "straight on and cross the bridge</em> (de brug)."),
            ("kader", "<strong>10. Een bordje aan de deur.</strong> <em>The shop is closed on "
                      "Sundays.</em><br>"
                      "De winkel is op zondag dicht. Meer staat er niet, dus meer mag je er ook "
                      "niet uit afleiden."),
            ("p", "Twee laatste tips. Bekijk altijd eerst de titel en het beeld: dat gaat "
                  "sneller dan lezen en het zegt je waarover de tekst gaat. En als de vraag "
                  "een antwoord (<em>answer</em>) in het Engels vraagt, kijk dan of je woorden "
                  "uit de tekst zelf kan hergebruiken; dat doet je leerkracht "
                  "(<em>teacher</em>) ook."),
        ]),
    ],
    onthoud=[
        "Onderwerp = enkele woorden. Hoofdgedachte = één zin. Hoofdpunten = wat haar draagt.",
        "Wat er niet staat, is geen hoofdpunt, hoe logisch het ook lijkt.",
        "a.m. is vóór de middag, p.m. erna.",
        "Kijk eerst naar titel, tussentitels en beeld; lees dan pas.",
        "Leid onbekende woorden af uit de context; zoek alleen op wat je echt nodig hebt.",
        "Verwijswoorden (he, it, they, there) wijzen terug naar iets uit de vorige zin.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["tekstsoorten-en-signaalwoorden-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Tekstsoorten, signaalwoorden en verwijswoorden",
    onder="Vijf soorten teksten herkennen, en de woordjes die de gedachtegang vasthouden.",
    secties=[
        dict(kop="Vijf soorten teksten", blokken=[
            ("p", "De vakfiche noemt vijf soorten lees- en luisterteksten. Op het examen krijg "
                  "je ze door elkaar, en de soort bepaalt wat je eruit moet halen."),
            ("fig", tabel(["soort", "wat het doet", "voorbeelden"], [
                ["informatief", "geeft informatie over een onderwerp",
                 "een krantenartikel, een stukje uit een leerboek, een interview, een gesprek over een afspraak"],
                ["opiniërend", "iemand geeft zijn mening",
                 "een gesprek over een boek, een reactie op sociale media"],
                ["prescriptief", "legt uit wat of hoe je iets moet doen",
                 "een recept (a recipe), een instructiefilmpje, een schoolreglement (a school rule)"],
                ["narratief", "geeft gebeurtenissen verhalend weer",
                 "een videoblog, een reisverslag, een podcast"],
                ["literair", "heeft esthetische waarde, speelt in op emoties",
                 "een lied, een gedicht, een cartoon, een strip, een kortverhaal"],
            ]), "De vijf soorten, met de voorbeelden die de vakfiche zelf geeft."),
            ("kader", "<strong>Waaraan zie je het?</strong> Een <em>bevelende vorm</em> "
                      "(<em>Mix the eggs. Next, add the flour.</em>) verraadt een prescriptieve "
                      "tekst. <em>I think</em> of <em>Our town needs</em> verraadt een mening. "
                      "<em>Once upon a time</em> verraadt een verhaal."),
            ("p", "Let op: een tekst die uitlegt <strong>hoe je een fiets herstelt</strong>, is "
                  "prescriptief, geen opiniërende tekst. En een <strong>schoolreglement</strong> "
                  "is dat ook, geen informatieve tekst zoals een krantenartikel."),
        ]),
        dict(kop="Het communicatiemodel", blokken=[
            ("p", "Bij elke tekst kan je dezelfde drie vragen stellen: <strong>van wie</strong> "
                  "is de tekst, <strong>waarom</strong> heeft de schrijver hem gemaakt, en "
                  "<strong>voor wie</strong> is hij bedoeld? Dat heet het "
                  "<strong>communicatiemodel</strong>."),
            ("kader", "<em>Keep in a dry place. Use before the date on the box.</em> Van wie? "
                      "De fabrikant. Waarom? Om te zeggen hoe je het bewaart. Voor wie? Voor wie "
                      "het product koopt.<br>"
                      "<em>How to survive your first week at a new school</em> — het woordje "
                      "<em>your</em> zegt het al: voor nieuwe leerlingen."),
            ("p", "Hoeveel woorden of bladzijden een tekst telt, zegt niets over zijn boodschap. "
                  "Dat is geen deel van het communicatiemodel."),
        ]),
        dict(kop="Signaalwoorden: de gedachtegang", blokken=[
            ("p", "<strong>Signaalwoorden</strong> tonen hoe de delen van een tekst zich tot "
                  "elkaar verhouden. De vakfiche noemt er vier functies bij de voegwoorden."),
            ("fig", tabel(["wat het aangeeft", "voorbeelden"], [
                ["chronologisch verloop", "first, then, next, after that, finally"],
                ["opsomming", "and, also, first of all, secondly, in addition"],
                ["oorzaak en gevolg", "because (oorzaak), so (gevolg)"],
                ["tegenstelling", "but, however"],
            ]), "De vier functies uit de vakfiche, met hun frequentste woorden."),
            ("kader", "<em>First we bought the tickets. Then we took the train. Finally we "
                      "walked to the hotel.</em> — drie stappen in de tijd.<br>"
                      "<em>The shop was closed. However, the bakery next door was open.</em> — "
                      "<em>however</em> is de deftige broer van <em>but</em> en staat meestal "
                      "vooraan, met een komma erachter.<br>"
                      "<em>In addition</em> telt iets bij; dat is een opsomming, geen "
                      "tegenstelling."),
            ("p", "<strong>Nevenschikkend of onderschikkend?</strong> <em>And</em>, "
                  "<em>but</em> en <em>so</em> zijn <strong>nevenschikkend</strong>: ze "
                  "verbinden twee delen die even belangrijk zijn. <em>When</em> en "
                  "<em>because</em> zijn <strong>onderschikkend</strong>: die maken van het "
                  "tweede deel een bijzin. <em>When I came home, my sister was cooking</em> — de "
                  "bijzin zegt wanneer het gebeurde."),
        ]),
        dict(kop="Verwijswoorden: structuuraanduiders", blokken=[
            ("p", "Verwijswoorden zijn de tweede soort structuuraanduiders. Ze grijpen terug "
                  "naar iets dat er al stond, zodat je niet steeds hetzelfde woord moet "
                  "herhalen."),
            ("kader", "<em>My cousins live in Wales. They have a farm there.</em> — "
                      "<em>they</em> = de neven en nichten, <em>there</em> = Wales.<br>"
                      "<em>Sarah gave her brother a book. He read it in one day.</em> — "
                      "<em>he</em> = de broer, <em>it</em> = het boek."),
            ("p", "De regel is simpel: neem het dichtstbijzijnde woord ervóór dat past. Een "
                  "boek is <em>it</em>, een jongen is <em>he</em>, meerdere mensen zijn "
                  "<em>they</em>, een plaats is <em>there</em>."),
        ]),
        dict(kop="Woorden afleiden uit hun vorm", blokken=[
            ("p", "Je kan de betekenis van een onbekend woord vaak afleiden uit de manier "
                  "waarop het gevormd is. Een <strong>voorvoegsel</strong> draait de betekenis "
                  "soms helemaal om."),
            ("fig", tabel(["voorvoegsel", "voorbeeld", "betekenis"], [
                ["un-", "unhappy, unfair", "niet blij, oneerlijk"],
                ["im- / in-", "impossible, incorrect", "onmogelijk, onjuist"],
                ["dis-", "dislike, disagree", "niet graag hebben, het oneens zijn"],
                ["-ful", "hopeful, useful", "hoopvol, nuttig — dit maakt net positief"],
            ]), "Un-, im- en dis- ontkennen; -ful doet het omgekeerde."),
            ("p", "Ook je <strong>moedertaal</strong> of het Frans helpt: <em>television</em>, "
                  "<em>restaurant</em>, <em>information</em>. De vakfiche noemt dat "
                  "uitdrukkelijk als strategie."),
        ]),
        dict(kop="Reageren op een literaire tekst", blokken=[
            ("p", "Bij een gedicht, een lied of een kortverhaal vraagt het examen je "
                  "<strong>eigen beleving en interpretatie</strong>, schriftelijk en in het "
                  "Engels. Je krijgt daarvoor een schrijfkader, sleutelwoorden of een "
                  "voorbeeld."),
            ("p", "Wat mag je schrijven? Waarom een tekst je aanspreekt, of je je herkent in "
                  "een <strong>personage</strong> (<em>the main character</em>), of je zoiets "
                  "zelf al hebt meegemaakt, welk gevoel de tekst oproept, waarom de stijl of de "
                  "vorm je bevalt. En: een <strong>geloofwaardig einde</strong> verzinnen bij "
                  "een verhaal dat halverwege stopt. Het aantal verzen tellen is géén reactie."),
            ("weetje", "Een <em>review</em> is een bespreking of recensie. De vakfiche gebruikt "
                       "<em>a film review</em> als voorbeeld van een tekst met een mening erin."),
        ]),
        dict(kop="Oefenen op echte tekstjes", blokken=[
            ("kader", "<strong>Een mening in de schoolkrant.</strong> <em>Our town has only one "
                      "small swimming pool, and it is often closed. A young swimmer from our "
                      "school has to train in another town. We need a new pool.</em><br>"
                      "Dit is een <strong>opiniërende</strong> tekst: iemand vindt iets en "
                      "geeft er argumenten bij. Het zwembad is klein en vaak gesloten, en een "
                      "zwemster van de school moet elders trainen. De lezer moet overtuigd "
                      "worden."),
            ("kader", "<strong>Een recept.</strong> <em>Add two spoons of sugar. Mix well.</em> "
                      "Suiker toevoegen en goed mengen: dat zegt wat je moet doen bij een "
                      "gerecht, dus <strong>prescriptief</strong>. Zo\'n tekst begint bijna "
                      "altijd met een werkwoord."),
            ("kader", "<strong>Een verhaal.</strong> <em>The door opened slowly. There was a "
                      "noise upstairs, and I was nearly asleep.</em><br>"
                      "De deur ging traag open, er was lawaai boven, de verteller was bijna in "
                      "slaap. Dit vertelt, dus het is <strong>narratief</strong>. Wie dat saai "
                      "(<em>boring</em>) vindt, mag dat zeggen, maar verveling is geen "
                      "tekstsoort."),
            ("kader", "<strong>Op een verpakking.</strong> <em>Keep in a dry place.</em> Ook "
                      "een instruction op een doosje is prescriptief."),
            ("p", "Een tekst heeft vaak een <strong>titel</strong> boven en soms een "
                  "<strong>tekening</strong> met een onderschrift eronder. Die twee mag je "
                  "gerust eerst bekijken; ze zeggen waarover de tekst gaat. Wat je "
                  "<strong>niet</strong> mag doen, is een hele alinea overslaan omdat er een "
                  "moeilijk woord in staat."),
            ("p", "Nog wat woorden die in de vragen terugkomen: <em>weather</em> is het weer, "
                  "<em>it was raining</em> betekent dat het regende, <em>we stayed at "
                  "home</em> dat we thuisbleven, en <em>we wanted to go out</em> dat we wilden "
                  "buitengaan. In <em>The weather was terrible, so we stayed at home</em> "
                  "kondigt <em>so</em> het gevolg aan."),
            ("p", "Let bij tekstsoorten ook op wie er aan het woord is. In een verhaal volg je "
                  "meestal het <strong>hoofdpersonage</strong>; in een opiniestuk is dat de "
                  "schrijver zelf. En in het Nederlands noemen we dat een narratieve tekst, "
                  "net zoals in het Engels."),
            ("weetje", "<em>However</em> en <em>but</em> zeggen het tegengestelde van wat "
                       "ervoor stond; ze zetten twee dingen tegenover elkaar. <em>In "
                       "addition</em> doet net het omgekeerde: het telt er iets bij. En "
                       "<em>first of all</em> gebruik je om een opsomming aan te kondigen. Let "
                       "op de kleine letters: signaalwoorden schrijf je gewoon, alleen vooraan "
                       "een zin met een hoofdletter."),
        ]),
    ],
    onthoud=[
        "Vijf soorten: informatief, opiniërend, prescriptief, narratief, literair.",
        "Communicatiemodel: van wie, waarom, voor wie?",
        "first – then – finally = volgorde; because = oorzaak; so = gevolg; but en however = tegenstelling.",
        "and, but, so zijn nevenschikkend; when en because onderschikkend.",
        "Verwijswoorden wijzen naar het dichtstbijzijnde passende woord ervóór.",
        "un-, im- en dis- ontkennen een woord.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["schrijven-berichten-en-mails-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Schrijven: berichten, uitnodigingen en mails",
    onder="Wat je schrijft, hoe je het opbouwt, en tegen wie je het zegt.",
    secties=[
        dict(kop="Wat vraagt het examen?", blokken=[
            ("p", "Schrijven weegt 8 % en <strong>schriftelijke interactie</strong> nog eens "
                  "8 %. Dat laatste is schrijven waarbij je <strong>reageert</strong> op iemand "
                  "anders: je krijgt een mail met een vraag erin en je antwoordt. Bij elke "
                  "opdracht krijg je een <strong>schrijfkader</strong> dat je op weg helpt."),
            ("p", "De vakfiche somt op wat je moet kunnen: alledaagse sociale contacten leggen "
                  "(begroeten, aanspreken, afscheid nemen, iets voorstellen, bedanken, "
                  "feliciteren, uitnodigen, je verontschuldigen en reageren op "
                  "verontschuldigingen), informatie geven en vragen, je mening geven, iets "
                  "vertellen en iemand iets uitleggen."),
        ]),
        dict(kop="Register: tegen wie schrijf je?", blokken=[
            ("fig", svg.registerschaal(zinnen=("Hi Tom, coming tonight?",
                                               "Are you coming tonight?",
                                               "Would you like to join us?")),
             "Dezelfde vraag, drie keer anders, afhankelijk van wie ze leest."),
            ("fig", tabel(["", "informeel", "neutraal of formeel"], [
                ["begin", "Hi Tom, / Hello Emma,", "Dear Mr Jones, / Dear Sir or Madam,"],
                ["einde", "See you soon! / Bye, Lisa", "Kind regards, / Yours faithfully,"],
                ["vragen", "Can you send it?", "Could you please send me the form?"],
                ["aanspreken", "mate", "Sir, Madam"],
            ]), "Dear Sir or Madam gebruik je als je de naam van de lezer niet kent."),
            ("p", "<em>Sir</em> en <em>mate</em> kan je dus niet in dezelfde situatie "
                  "gebruiken. En vergeet niet genoeg <strong>please</strong> en <strong>thank "
                  "you</strong> te zeggen: dat hoort bij de beleefdheidsconventies. Vermijd "
                  "scheldwoorden, ook verpakte."),
            ("p", "Bevelen klinken onvriendelijk. <em>Send me the form now</em> wordt "
                  "<em>Could you please send me the form?</em> En <em>You have to come to my "
                  "party</em> wordt <em>Would you like to come to my party?</em>"),
        ]),
        dict(kop="Vaste zinnen voor sociale contacten", blokken=[
            ("fig", tabel(["wat je doet", "wat je schrijft"], [
                ["uitnodigen", "Would you like to come to my party?"],
                ["iets voorstellen", "Shall we go to the cinema? / Why don't we meet at six?"],
                ["bedanken", "Thank you so much for the present!"],
                ["feliciteren", "Congratulations!"],
                ["je verontschuldigen", "I'm sorry I'm late. / Sorry, I can't come."],
                ["reageren op een excuus", "That's all right. / No problem."],
                ["om hulp vragen", "Could you help me, please?"],
                ["je mening geven", "In my opinion, … / I think … / I don't agree with …"],
            ]), "Congratulations staat altijd in het meervoud en heeft geen d."),
            ("p", "Bij een <strong>uitnodiging</strong> horen altijd drie dingen: "
                  "<strong>wanneer</strong>, <strong>waar</strong> en <strong>waarvoor</strong>. "
                  "Zonder die drie kan je lezer niets met je bericht. Bij een "
                  "<strong>reservatie</strong> zijn dat de data van je verblijf, het aantal "
                  "personen en je naam."),
        ]),
        dict(kop="De opbouw van je tekst", blokken=[
            ("fig", svg.tekstopbouw([
                ("inleiding", "waarom je schrijft: I am writing about the headphones I bought last week.", 1.3),
                ("midden", "de inhoud, één gedachte per alinea", 1.6),
                ("slot", "afronden en groeten: I hope to see you soon. Bye, Lisa", 1.3),
            ]), "Inleiding, midden, slot — de structuur die de vakfiche vraagt."),
            ("p", "Gebruik ook in je eigen tekst <strong>signaalwoorden</strong>: "
                  "<em>first</em>, <em>after that</em>, <em>in the end</em>. Ze maken je tekst "
                  "overzichtelijk. En zet je alinea's zo dat er <strong>één gedachte per "
                  "alinea</strong> staat; niet alles in één blok, en ook niet elke zin op een "
                  "nieuwe regel."),
            ("p", "De <strong>lay-out</strong> telt mee. Een mail met een aanhef, alinea's en "
                  "een groet leest nu eenmaal beter dan een lap tekst."),
        ]),
        dict(kop="Waarop word je beoordeeld?", blokken=[
            ("fig", tabel(["vereiste", "wat men verwacht"], [
                ["taakvoltooiing", "het doel is bereikt, je boodschap komt over, en je respecteert de opgegeven lengte (write about 80 words)"],
                ["woordenschat", "je gebruikt frequente woorden en vaste uitdrukkingen correct"],
                ["grammatica en zinsbouw", "eenvoudige correcte zinnen; fouten verstoren de communicatie niet"],
                ["tekststructuur en samenhang", "inleiding, midden, slot, met herkenbare tekstverbanden"],
                ["register en beleefdheid", "een gepast register en gepaste beleefdheidsconventies"],
                ["tekstopbouw en lay-out", "de opbouw is duidelijk herkenbaar, de lay-out is gepast"],
                ["spelling en leestekens", "je spelt redelijk correct, met hulp van de spellingcontrole"],
            ]), "De vereisten uit de vakfiche voor een geschreven tekst."),
            ("p", "Schrijf je 25 woorden waar er 60 gevraagd zijn, dan zakt je "
                  "<strong>taakvoltooiing</strong>, ook al is elk woord juist. Schrijf je zes "
                  "zinnen zonder punt of hoofdletter, dan zakt je <strong>spelling en "
                  "leestekengebruik</strong>. Lichaamstaal geldt alleen voor spreken, niet voor "
                  "een geschreven tekst."),
            ("weetje", "Kleine grammaticafouten die de boodschap niet in de weg staan, zijn op "
                       "dit niveau <strong>aanvaardbaar</strong>. Perfect hoeft niet; "
                       "begrijpelijk wel."),
        ]),
        dict(kop="Spelling die je vaak nodig hebt", blokken=[
            ("fig", tabel(["fout", "juist", "waarom"], [
                ["i went to londen", "I went to London", "I krijgt altijd een hoofdletter, net als landen en steden"],
                ["my freind", "my friend", "friend met -ie-; er zit 'end' in"],
                ["congratulation", "congratulations", "altijd meervoud"],
                ["becouse", "because", "Big Elephants Can Always Understand Small Elephants"],
            ]), "Weekend is wél juist gespeld, ook al ziet het er Nederlands uit."),
            ("p", "Je mag tijdens het examen een <strong>spellingcontrole</strong> en een online "
                  "<strong>woordenboek</strong> gebruiken. Oefen daar thuis mee, zodat je er op "
                  "het examen geen tijd mee verliest. Lees je tekst achteraf nog eens na: is de "
                  "communicatie helder, gepast en vlot?"),
            ("p", "Weet je niet hoe je iets moet zeggen? Laat je niet ontmoedigen. Probeer je "
                  "doel te bereiken met de woorden en structuren die je wél al kent. Dat staat "
                  "zo in de vakfiche."),
        ]),
        dict(kop="Zes schrijfopdrachten, uitgewerkt", blokken=[
            ("p", "Zo ziet een schrijfopdracht eruit op het examen. Lees telkens wat er "
                  "gevraagd wordt en let op het register: schrijf je aan een vriendin of aan "
                  "de directeur van de school?"),
            ("kader", "<strong>1. Een mailtje aan de directeur.</strong> Dit is formeel. Je "
                      "begint met <em>Dear Mr Jones,</em> en je sluit datzelfde mailtje af met "
                      "<em>Kind regards,</em> en je naam. Aan een leraar schrijf je op dezelfde "
                      "manier."),
            ("kader", "<strong>2. Een uitnodiging voor je verjaardag.</strong> <em>Hi Emma, "
                      "would you like to come to my birthday party on Saturday at four, at my "
                      "house?</em> Wanneer, waar en waarvoor: alle drie erin. Aan een vriendin "
                      "mag dit informele register."),
            ("kader", "<strong>3. Bedanken voor een cadeau.</strong> Je stuurt een kaartje: "
                      "<em>Thank you so much for the present. I really love it!</em> Wie iets "
                      "te vieren heeft, krijgt <em>Congratulations!</em> — gefeliciteerd."),
            ("kader", "<strong>4. Een berichtje in de groepschat.</strong> Aan een "
                      "buitenlandse leerling die net in je klas zit: <em>Hi! I am Sam. Do you "
                      "want to sit with us at lunch?</em> Kort en vriendelijk; niemand "
                      "verwacht hier een brief."),
            ("kader", "<strong>5. Je mening over schooluniformen.</strong> <em>In my opinion, "
                      "school uniforms are boring, but they are also practical.</em> Begin met "
                      "je standpunt, geef dan je redenen. Dat is het middenstuk van je tekst."),
            ("kader", "<strong>6. Een hotelkamer reserveren.</strong> <em>Dear Sir or Madam, I "
                      "would like to book a room for two people from 3 to 7 July. Could you "
                      "confirm the price?</em> Bij een reservering zet je de data van je "
                      "verblijf, het aantal personen en je naam erbij."),
            ("p", "Nog één situatie die vaak terugkomt: je koopt een toestel in een "
                  "<strong>winkel</strong> en het is kapot. Dan schrijf je een klacht. Zeg "
                  "eerst wat je kocht en wanneer, dan wat er scheelt, en dan wat je wil: "
                  "<em>I bought these headphones last week, but the left one does not work. "
                  "Could I have a new pair?</em>"),
            ("p", "Een paar praktische dingen. Zet je naam <strong>vooraan</strong> in de "
                  "aanhef en achteraan bij de groet. Laat gerust weg wat er niet toe doet: een "
                  "tekstje van zestig woorden heeft geen plaats voor je hele vorige vakantie. "
                  "Deel je tekst in alinea\'s, want dat leest overzichtelijker. En schrijf je "
                  "zinnen in de past simple als je vertelt wat er gebeurd is."),
            ("p", "Van welke vorm mag je zeker zijn dat hij het beleefdst is? "
                  "<em>Would you like…?</em> en <em>Could you please…?</em> winnen het altijd "
                  "van een bevel. Wie je tekst nakijkt, geeft zijn beoordeling op de zeven "
                  "punten uit de tabel hierboven, en elk onderdeel telt mee. Kijk je tekst dus "
                  "nog eens na voor je hem afgeeft."),
        ]),
    ],
    onthoud=[
        "Dear Mr Jones + Kind regards is neutraal; Hi Tom + Bye is informeel.",
        "Would you like…? en Could you please…? zijn de beleefde vormen.",
        "Een uitnodiging zegt wanneer, waar en waarvoor.",
        "Inleiding, midden, slot — en één gedachte per alinea.",
        "Respecteer de opgegeven lengte: dat is taakvoltooiing.",
        "Vergeet please en thank you niet.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["engelstalige-landen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Engelstalige landen en literaire teksten",
    onder="Gewoontes en verschillen in landen waar Engels gesproken wordt, en reageren op een verhaal.",
    secties=[
        dict(kop="Waarom staat dit in de vakfiche?", blokken=[
            ("p", "De vakfiche vraagt letterlijk dat je <strong>aspecten van maatschappijen en "
                  "culturen</strong> identificeert waarin Engels gesproken wordt. Op het examen "
                  "krijg je teksten over het dagelijkse leven, de leefomstandigheden, "
                  "gewoontes, sociale verhoudingen, waarden en normen, lichaamstaal en sociale "
                  "conventies in die landen."),
            ("p", "Engels is de taal van onder meer het <strong>Verenigd Koninkrijk</strong> "
                  "(met London als hoofdstad), "
                  "<strong>Ierland</strong>, de <strong>Verenigde Staten</strong>, "
                  "<strong>Canada</strong>, <strong>Australië</strong> en "
                  "<strong>Nieuw-Zeeland</strong>. Een tekst over 'een Engelstalig land' gaat "
                  "dus lang niet altijd over Groot-Brittannië. Canada heeft Engels én Frans als "
                  "officiële talen; Nieuw-Zeeland heeft er ook Maori naast."),
        ]),
        dict(kop="Verschillen die in teksten opduiken", blokken=[
            ("fig", tabel(["waar het over gaat", "wat je moet weten"], [
                ["verkeer", "in het Verenigd Koninkrijk en Ierland rijdt men links, in de Verenigde Staten rechts"],
                ["geld", "in Ierland betaal je met euro, in het Verenigd Koninkrijk met pond (pounds)"],
                ["temperatuur", "de Verenigde Staten meten in graden Fahrenheit, niet in Celsius (70°F ≈ 21°C)"],
                ["afstand", "in miles: één mile is ongeveer 1,6 kilometer"],
                ["verdiepingen", "Brits: the ground floor is de begane grond, the first floor de eerste verdieping. Amerikaans: the first floor ís de begane grond"],
                ["datums", "Brits 14/06/2027 = 14 juni; Amerikaans 06/14/2027 = diezelfde dag"],
                ["voetbal", "in de Verenigde Staten is football een ander spel; wat wij voetbal noemen heet daar soccer"],
                ["school", "Britse leerlingen (pupils) dragen vaak een school uniform"],
                ["fooi", "in Amerikaanse restaurants is een tip (fooi) gebruikelijk"],
                ["in de rij", "queue politely: netjes aanschuiven is er een gewoonte"],
            ]), "Allemaal dingen die in een examentekst terloops vermeld worden."),
        ]),
        dict(kop="Feesten", blokken=[
            ("fig", tabel(["feest", "wanneer en waar"], [
                ["Halloween", "31 oktober, in veel Engelstalige landen"],
                ["Thanksgiving", "vierde donderdag van november in de Verenigde Staten, met turkey (kalkoen) op tafel; Canada viert het op de tweede maandag van oktober"],
                ["Bonfire Night", "5 november, in het Verenigd Koninkrijk"],
                ["Saint Patrick's Day", "17 maart, de Ierse feestdag"],
                ["Christmas", "25 december — maar in Australië valt dat midden in de zomer, want dat land ligt op het zuidelijk halfrond"],
            ]), "Sinterklaas hoort hier niet bij: dat is een gewoonte van bij ons en van Nederland."),
            ("weetje", "In het Engels schrijf je feesten, dagen, maanden, landen, "
                       "nationaliteiten én talen met een <strong>hoofdletter</strong>: "
                       "<em>Christmas, Monday, July, Belgium, Belgian, English</em>. In het "
                       "Nederlands doen we dat niet."),
        ]),
        dict(kop="Brits of Amerikaans?", blokken=[
            ("fig", tabel(["Brits", "Amerikaans", "Nederlands"], [
                ["lift", "elevator", "lift"],
                ["biscuit", "cookie", "koekje"],
                ["autumn", "fall", "herfst"],
                ["colour, theatre, travelling", "color, theater, traveling", "kleur, theater, reizend"],
                ["holiday", "vacation", "vakantie"],
                ["a flat", "an apartment", "een appartement"],
                ["chips", "french fries", "frieten"],
            ]), "Allebei zijn juist. Wissel alleen niet binnen één tekst."),
            ("p", "Wie in een Amerikaanse tekst <em>color</em>, <em>theater</em> en "
                  "<em>traveling</em> ziet staan, leest dus geen schrijffouten maar Amerikaanse "
                  "spelling."),
        ]),
        dict(kop="Reageren op een literaire tekst", blokken=[
            ("p", "Het tweede stuk van dit hoofdstuk: je <strong>verwoordt schriftelijk in het "
                  "Engels je eigen beleving en interpretatie</strong> bij een literaire tekst. "
                  "Je krijgt daarvoor een schrijfkader, sleutelwoorden of een voorbeeld, dus je "
                  "moet nooit uit het niets beginnen."),
            ("fig", tabel(["wat je kan zeggen", "voorbeeldzin"], [
                ["welk gevoel de tekst oproept", "I feel sad when I read this poem."],
                ["of je zelf al zoiets meemaakte", "This poem reminds me of a rainy holiday."],
                ["waarom de stijl of de vorm je bevalt", "I like the way the poet repeats the rain."],
                ["of je je herkent in een personage", "I know this feeling, because I moved too."],
                ["wat je verraste", "The end surprised me, because I expected the brother to come back."],
            ]), "Het aantal woorden of verzen tellen is geen reactie."),
            ("p", "Er is <strong>geen juiste mening</strong> over een gedicht. Maar "
                  "<em>I liked it</em> alleen volstaat niet: je moet er telkens "
                  "<strong>waarom</strong> bij zetten. Dat waarom ís je interpretatie."),
            ("p", "Een <strong>geloofwaardig einde</strong> verzinnen is ook een opdracht uit de "
                  "fiche. Geloofwaardig betekent: het past bij wat er al gebeurd is. Stopt een "
                  "verhaal met <em>She opened the letter and started to cry</em>, dan past "
                  "'het nieuws in de brief raakte haar diep'. Een draak die uit het niets komt, "
                  "breekt het verhaal."),
            ("p", "Literaire teksten zijn <em>a song</em> (een lied), <em>a poem</em> (een "
                  "gedicht), <em>a comic</em> (een strip), een cartoon en <em>a short story</em> "
                  "(een kortverhaal). Een schoolrapport hoort daar niet bij."),
            ("weetje", "Een strip zonder woorden lees je aan de gezichten en de "
                       "<strong>lichaamstaal</strong> van de personages. Ook dat rekent de "
                       "vakfiche mee."),
            ("p", "Schrijvers geven soms menselijke trekken aan dingen: <em>The old house was "
                  "watching them with its broken windows.</em> Een huis kan niet kijken; die "
                  "beeldspraak maakt de sfeer onheilspellend. Zoiets mag je gerust benoemen in "
                  "je reactie."),
        ]),
        dict(kop="Vier stukjes uit teksten over cultuur", blokken=[
            ("kader", "<strong>Uit een reisgids.</strong> <em>Remember: in the United Kingdom "
                      "and in Ireland people drive on the left.</em><br>"
                      "Hieruit leer je dat men er langs de linkerkant rijdt. Dat is geen "
                      "mening, dat is informatie: een reisgids legt uit wat je moet weten."),
            ("kader", "<strong>Over Thanksgiving.</strong> <em>On Thanksgiving, the whole "
                      "family usually comes together for a big meal.</em><br>"
                      "Het wordt met het hele gezin gevierd, gewoonlijk rond een groot maal. "
                      "Zulke eetgewoontes horen bij de cultuur van een land, en Amerikanen "
                      "vieren het op de vierde donderdag van november."),
            ("kader", "<strong>Over Australië.</strong> <em>In Australia, Christmas is in the "
                      "middle of the summer.</em><br>"
                      "Kerstmis valt er midden in de zomer, want het land ligt op het zuidelijk "
                      "halfrond. Wie dat niet weet, begrijpt de tekeningen van een kerstman op "
                      "het strand niet."),
            ("kader", "<strong>Een gedicht.</strong> <em>The street is empty tonight. Nobody "
                      "waits at the door. The rain keeps falling.</em><br>"
                      "De straat is leeg, niemand wacht, de regen blijft vallen. Waarover gaat "
                      "dit? Over <strong>eenzaamheid</strong>. Dat is het onderwerp, en dat mag "
                      "je zeggen zonder het te kunnen bewijzen: een gedicht vraagt jouw "
                      "interpretatie, geen volledige uitleg."),
            ("p", "En een verhaal: <em>The girl always leaves before the others.</em> Een "
                  "meisje dat altijd vertrekt voor de anderen, of dat naar het platteland "
                  "verhuist — vertel dan wat je zelf al eens overkwam. Dat is precies wat de "
                  "vakfiche met <em>eigen beleving</em> bedoelt, en het is een goede manier om "
                  "aan jezelf uit te leggen waarom een tekst je aanspreekt."),
            ("p", "Twee woorden die vaak in zo\'n tekst staan: <em>people</em> zijn mensen, en "
                  "<em>British</em> is het bijvoeglijk naamwoord bij het Verenigd Koninkrijk, "
                  "waarvan Londen de hoofdstad is. Een gebouw met vier verdiepingen boven de "
                  "begane grond telt men in het Brits anders dan in het Amerikaans; zie de "
                  "tabel hierboven."),
        ]),
    ],
    onthoud=[
        "Engels wordt ook gesproken in Ierland, de VS, Canada, Australië en Nieuw-Zeeland.",
        "VK en Ierland rijden links; de VS meet in Fahrenheit en miles.",
        "Brits first floor = eerste verdieping; Amerikaans first floor = begane grond.",
        "Feesten, dagen, maanden, landen, nationaliteiten en talen: hoofdletter.",
        "Bij een literaire tekst zeg je wat je voelt én waarom.",
        "Een geloofwaardig einde past bij wat er al gebeurd is.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woorden-mensen-en-gezondheid-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: mensen, familie, gevoelens en gezondheid",
    onder="Vier woordvelden uit de vakfiche, met de valse vrienden erbij.",
    secties=[
        dict(kop="Waarom woordenschat?", blokken=[
            ("p", "De vakfiche zegt het zelf: woordenschat leren is <strong>nooit een doel op "
                  "zich</strong>. Je hebt ze nodig om teksten te begrijpen en om zelf te "
                  "schrijven over het dagelijkse leven, de samenleving en het schoolleven. Hoe "
                  "rijker je woordenschat, hoe vlotter het gaat — en hoe minder je moet "
                  "opzoeken tijdens het examen."),
        ]),
        dict(kop="Familie", blokken=[
            ("fig", svg.stamboom(), "Wie is wie in een Engelse stamboom."),
            ("fig", tabel(["Engels", "Nederlands"], [
                ["grandfather, grandmother", "grootvader, grootmoeder (informeel: grandpa, gran)"],
                ["parents", "ouders"],
                ["aunt, uncle", "tante, oom"],
                ["cousin", "neef of nicht (kind van je tante of oom)"],
                ["nephew, niece", "neefje, nichtje (kind van je broer of zus)"],
                ["daughter, son", "dochter, zoon"],
                ["twins", "een tweeling"],
                ["stepmother, stepfather", "stiefmoeder, stiefvader"],
                ["grandchild", "kleinkind"],
                ["an only child", "een enig kind"],
            ]), "A cousin kan zowel een neef als een nicht zijn; het Engels maakt daar geen verschil in."),
            ("p", "Let op wat er géén familie is: <em>a neighbour</em> is een buur en "
                  "<em>a classmate</em> een klasgenoot. En <em>an only child</em> betekent "
                  "<strong>enig kind</strong>, niet 'iemand die alleen woont'."),
            ("p", "<em>To get married</em> is trouwen: <em>My parents got married twenty years "
                  "ago.</em>"),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["happy / unhappy, sad", "blij / niet blij, verdrietig"],
                ["angry", "boos"],
                ["proud", "trots"],
                ["worried", "bezorgd"],
                ["nervous", "zenuwachtig"],
                ["disappointed", "teleurgesteld"],
                ["surprised, relieved, jealous", "verrast, opgelucht, jaloers"],
                ["afraid of", "bang van (altijd met of!)"],
                ["to look forward to", "uitkijken naar"],
            ]), "Tall (groot van gestalte) is geen gevoel maar een uiterlijk kenmerk."),
            ("p", "<strong>Bored of boring?</strong> <em>I am bored</em> = ik verveel me. "
                  "<em>The film is boring</em> = de film is saai. Wie <em>I am boring</em> zegt, "
                  "noemt zichzelf saai."),
            ("p", "<strong>Valse vriend.</strong> <em>Sympathetic</em> betekent "
                  "<strong>meelevend</strong> of begripvol, niet 'sympathiek'. Wil je zeggen dat "
                  "iemand sympathiek is, gebruik dan <em>nice</em> of <em>likeable</em>."),
            ("p", "Woorden die zeggen hoe iemand <strong>is</strong> (het karakter): "
                  "<em>friendly</em>, <em>shy</em>, <em>patient</em>. Woorden over het "
                  "<strong>uiterlijk</strong>: <em>blond</em>, <em>tall</em>."),
        ]),
        dict(kop="Gezondheid en lichaamsdelen", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a sore throat", "keelpijn"],
                ["a headache, toothache, stomach ache, backache", "hoofdpijn, tandpijn, buikpijn, rugpijn"],
                ["a fever, to have a temperature", "koorts hebben"],
                ["to feel sick", "zich misselijk of ziek voelen"],
                ["a doctor, a nurse, a dentist", "een dokter, een verpleegkundige, een tandarts"],
                ["a hospital, an ambulance", "een ziekenhuis, een ziekenwagen"],
                ["a chemist's (Brits), a pharmacy", "een apotheek"],
                ["medicine", "medicijn"],
                ["twice a day", "twee keer per dag (once = één keer)"],
            ]), "Met -ache maak je pijnwoorden. Should + werkwoord geeft een raad: You should see a doctor."),
            ("fig", tabel(["hoofd", "romp en ledematen"], [
                ["chin (kin), cheek (wang), forehead (voorhoofd)", "shoulder (schouder), elbow (elleboog), knee (knie)"],
                ["ear (oor), eye (oog), mouth (mond)", "hand, finger (vinger), thumb (duim)"],
                ["tooth – teeth (tand – tanden)", "foot – feet (voet – voeten), ankle (enkel)"],
            ]), "Tooth wordt teeth en foot wordt feet: onregelmatige meervouden."),
            ("p", "<em>To break</em> is breken; de verleden tijd is <em>broke</em>. <em>She "
                  "broke her leg while skiing.</em>"),
            ("p", "<strong>Hair</strong> is in het Engels ontelbaar en staat dus in het "
                  "<strong>enkelvoud</strong>: <em>her hair is long</em>. Alleen losse haren tel "
                  "je: <em>there were two hairs on my plate</em>."),
        ]),
        dict(kop="Persoonlijke gegevens", blokken=[
            ("fig", tabel(["op het formulier", "wat je invult"], [
                ["first name", "je voornaam"],
                ["surname / last name", "je achternaam of familienaam"],
                ["date of birth", "je geboortedatum"],
                ["place of birth", "je geboorteplaats"],
                ["address", "je adres"],
                ["nationality", "Belgian (met een hoofdletter!)"],
            ]), "Belgium is het land, Belgian de nationaliteit. Je lievelingskleur is geen persoonlijk gegeven."),
            ("p", "Iemand beschrijven doe je met zijn <strong>uiterlijk</strong>: <em>He has "
                  "short brown hair. He is quite tall. He wears glasses.</em> Waar hij woont, "
                  "zegt niets over hoe hij eruitziet. De vakfiche gebruikt net dat voorbeeld: je "
                  "beschrijft hoe je beste vriend eruitziet."),
            ("p", "<em>In her early twenties</em> betekent: een jaar of twintig tot drieëntwintig. "
                  "<em>Early</em> is het begin van dat tiental, <em>mid</em> het midden, "
                  "<em>late</em> het einde."),
            ("weetje", "<em>A mark</em> is een punt of cijfer op school. <em>I was really "
                       "disappointed with my mark</em> zegt iets over je gevoel; <em>there were "
                       "twenty questions</em> geeft alleen een feit."),
        ]),
        dict(kop="Deze woorden in hele zinnen", blokken=[
            ("kader", "<em>My grandmother was born in Bristol. She lives with us now.</em><br>"
                      "Geboren in Bristol, en ze woont nu bij het gezin in. <em>To be born</em> "
                      "is geboren worden; de verleden tijd is <em>was born</em>."),
            ("kader", "<em>We are a family of five: my parents, my two sisters and me.</em><br>"
                      "Een gezin van vijf, met twee zussen. Kinderen tel je in het Engels met "
                      "<em>children</em>, het onregelmatige meervoud van <em>child</em>."),
            ("kader", "<em>Take this medicine twice a day, before you eat.</em><br>"
                      "Het geneesmiddel twee keer per dag innemen, en wel vóór het eten. "
                      "<em>Before</em> is vóór, <em>after</em> is na."),
            ("p", "Op een formulier vul je je <strong>personal details</strong> in. Dat zijn je "
                  "voornaam, je familienaam, je geboortedatum en je adres, niet je "
                  "lievelingskleur en niet de talen die je spreekt. Wie ergens "
                  "<strong>woont</strong>, schrijft dat als <em>she lives in Hasselt</em>, met "
                  "een -s."),
            ("p", "Bij het uiterlijk hoort ook het haar: <em>dark hair</em> is donker haar. En "
                  "<em>a little</em> gebruik je bij iets wat je niet kan tellen: <em>a little "
                  "water</em>, <em>a little time</em>."),
            ("p", "Gevoelens komen los van de feiten. <em>I got a bad result on the test</em> "
                  "geeft een slechte uitslag van een toets; <em>I was disappointed</em> zegt "
                  "wat je daarbij voelde. Wie iets zoekt, is <em>looking for</em> iets; wie "
                  "iets gaat halen in de winkel, <em>goes to get</em> it. En wie zinnen leest "
                  "of schrijft (<em>write</em>) in het Engels, zet <em>I</em> altijd met een "
                  "hoofdletter — dat is gewoon zo, en het is het enige woord met dat recht."),
        ]),
    ],
    onthoud=[
        "aunt/uncle, cousin (neef én nicht), nephew/niece, twins, an only child.",
        "I am bored = ik verveel me; the film is boring = de film is saai.",
        "Sympathetic = meelevend, niet sympathiek.",
        "afraid OF, nooit afraid from.",
        "tooth–teeth, foot–feet; hair staat in het enkelvoud.",
        "Belgium is het land, Belgian de nationaliteit — met hoofdletter.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woorden-eten-wonen-kleding-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: eten, wonen, kleding en dagelijkse dingen",
    onder="De woorden van het gewone leven, met het verschil tussen Brits en Amerikaans.",
    secties=[
        dict(kop="Eten en drinken", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["breakfast, lunch, dinner", "ontbijt, middagmaal, avondmaal"],
                ["bread, jam, cheese", "brood, confituur, kaas"],
                ["tea, orange juice, milk", "thee, sinaasappelsap, melk"],
                ["a carrot, an onion, a pea", "een wortel, een ui, een erwt"],
                ["a pear, a grape", "een peer, een druif"],
                ["chicken, soup, apple pie", "kip, soep, appeltaart"],
                ["sugar, flour, a spoon", "suiker, bloem, een lepel"],
                ["to add", "toevoegen"],
            ]), "A grape is een druif, geen grapefruit: een valse vriend."),
            ("p", "<strong>Chips</strong> is de beroemdste verwarring. Een Brit bestelt "
                  "<em>fish and chips</em> en krijgt frieten; een Amerikaan zegt <em>french "
                  "fries</em> voor frieten en <em>chips</em> voor wat wij chips noemen."),
            ("p", "<strong>Ontelbaar.</strong> <em>Bread</em>, <em>water</em> en <em>rice</em> "
                  "kan je niet zomaar in het meervoud zetten. Je telt ze met een maat erbij: "
                  "<em>two slices of bread</em>, <em>three glasses of water</em>, <em>two bowls "
                  "of rice</em>."),
            ("fig", tabel(["in het restaurant", "betekenis"], [
                ["the menu", "de kaart"],
                ["a waiter", "een ober"],
                ["the bill (Brits) / the check (Amerikaans)", "de rekening"],
                ["Would you like some more soup?", "Wil je nog wat soep? — het beleefde aanbod"],
            ]), "A timetable is geen restaurantwoord: dat is een uurrooster of dienstregeling."),
        ]),
        dict(kop="Wonen", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a flat (Brits) / an apartment", "een appartement"],
                ["a bedroom, a kitchen, a bathroom", "een slaapkamer, een keuken, een badkamer"],
                ["a living room / a sitting room", "een woonkamer"],
                ["a hall", "een gang of hal"],
                ["a cellar, an attic", "een kelder, een zolder"],
                ["a garden, a garage", "een tuin, een garage"],
                ["a wardrobe, an armchair, a bookcase", "een kleerkast, een zetel, een boekenkast"],
                ["a curtain", "een gordijn (geen meubel)"],
            ]), "Living room en sitting room betekenen ongeveer hetzelfde; sitting room klinkt Britser."),
            ("p", "<em>To turn off</em> is uitzetten, <em>to turn on</em> aanzetten. Je hoort "
                  "ook <em>to switch off</em> en <em>to switch on</em>. <em>Turn off the light "
                  "when you leave.</em>"),
        ]),
        dict(kop="Kleding en accessoires", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a jumper (Brits) / a sweater", "een trui"],
                ["a shirt, a skirt, a coat", "een hemd, een rok, een jas"],
                ["trousers, jeans", "een broek, een jeansbroek"],
                ["trainers (Brits) / sneakers", "sportschoenen"],
                ["a belt, a scarf, a watch", "een riem, een sjaal, een horloge"],
                ["glasses", "een bril"],
                ["to wear", "dragen, aanhebben"],
            ]), "Trousers, jeans en glasses staan altijd in het meervoud: my trousers are new."),
            ("p", "<em>Made of</em> zegt uit welk materiaal iets bestaat: <em>The shirt is made "
                  "of cotton</em> (katoen). Verder: <em>wool</em> (wol), <em>leather</em> "
                  "(leder), <em>wood</em> (hout), <em>glass</em> (glas), <em>metal</em>, "
                  "<em>plastic</em>, <em>paper</em>."),
        ]),
        dict(kop="Kleuren en vormen", blokken=[
            ("fig", tabel(["kleuren", "vormen"], [
                ["red, blue, yellow, green", "round (rond)"],
                ["black, white, brown, grey (Brits) / gray", "square (vierkant)"],
                ["orange, purple (paars), pink (roze)", "rectangular (rechthoekig), triangular (driehoekig)"],
            ]), "Rood en wit samen geeft pink. Heavy (zwaar) is een gewicht, geen vorm."),
        ]),
        dict(kop="Dagelijkse bezigheden en voorwerpen", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["to get up", "opstaan"],
                ["to wake up", "wakker worden"],
                ["to have a shower", "een douche nemen"],
                ["to brush your teeth", "je tanden poetsen"],
                ["to get dressed", "je aankleden"],
                ["to go to bed", "gaan slapen"],
                ["to do the washing-up", "de afwas doen"],
                ["to do the washing", "de was doen, met de wasmachine"],
                ["to go shopping", "gaan winkelen"],
            ]), "Zulke gewone handelingen heten samen je daily routine."),
            ("p", "De dingen die je elke dag bij je hebt: <em>keys</em> (sleutels), "
                  "<em>a wallet</em> (een portefeuille), <em>a phone</em>. Een "
                  "<em>wardrobe</em> steek je niet in je zak."),
        ]),
        dict(kop="Winkels en diensten", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a baker's / a bakery", "een bakkerij"],
                ["a butcher's", "een slagerij"],
                ["a chemist's", "een apotheek"],
                ["a newsagent's", "een krantenwinkel"],
                ["a bank, a post office", "een bank, een postkantoor"],
                ["a library", "een bibliotheek"],
                ["a bookshop", "een boekhandel"],
                ["a supermarket", "een supermarkt"],
            ]), "Winkels krijgen in het Brits vaak een 's, van 'de winkel van de bakker'."),
            ("p", "<strong>Twee valse vrienden op een rij.</strong> <em>A library</em> is een "
                  "<strong>bibliotheek</strong>, geen boekhandel. En <em>a magazine</em> is een "
                  "<strong>tijdschrift</strong>, geen magazijn; dat laatste is <em>a "
                  "warehouse</em> of <em>a store</em>."),
            ("p", "Openingsuren lees je met a.m. en p.m.: <em>open from 9 a.m. to 8 p.m.</em> "
                  "betekent van negen uur 's ochtends tot acht uur 's avonds."),
        ]),
        dict(kop="Deze woorden in hele zinnen", blokken=[
            ("kader", "<em>Would you like some more soup?</em><br>"
                      "Dat vraagt een gastheer aan tafel. Het is een beleefd aanbod, geen "
                      "bevel. Je antwoordt met <em>Yes, please</em> of <em>No, thank you</em>."),
            ("kader", "<em>On Saturday morning we go to the market at seven.</em><br>"
                      "Zaterdagvoormiddag om zeven uur naar de markt. <em>Morning</em> is de "
                      "voormiddag, en waar je naartoe gaat, zeg je met <em>to</em>."),
            ("kader", "<em>First you mix the eggs and the flour. Then you add a little "
                      "milk.</em><br>"
                      "Zo staat het in een recept: je mengt eerst, dan voeg je toe. "
                      "<em>To mix</em> is mengen."),
            ("p", "Een <strong>maaltijd</strong> heeft vaak een voorgerecht, een hoofdgerecht "
                  "en een nagerecht. Bij het hoofdgerecht horen groenten "
                  "(<em>vegetables</em>) zoals wortelen, uien en erwten; dranken "
                  "(<em>drinks</em>) zijn water, melk en sinaasappelsap. Wie iets koopt in de "
                  "winkel, <em>buys</em> het; wie iets gaat halen, <em>gets</em> het."),
            ("p", "<em>Bread</em>, <em>water</em> en <em>rice</em> staan altijd in het "
                  "<strong>enkelvoud</strong>, ook als er veel van is. Je telt ze met een maat "
                  "erbij, en je ziet meteen waarvan er hoeveel is: <em>two slices of "
                  "bread</em>."),
            ("p", "Bij kleding hoort <em>to wear</em>: <em>she is wearing a red coat</em>, ze "
                  "heeft een rode jas aan. Iets uitdoen is <em>to take off</em>. En als het "
                  "buiten licht regent, doe je een jas aan en sluit je de deur "
                  "(<em>close</em>) achter je; <em>could you close the door, please?</em> is "
                  "hoe een persoon dat beleefd vraagt."),
            ("weetje", "Veel Engelse woorden voor eten ontlenen we gewoon: <em>pizza</em>, "
                       "<em>pasta</em>, <em>sandwich</em>. Die lijken op elkaar in elke taal, "
                       "dus ze zijn gratis meegenomen."),
        ]),
    ],
    onthoud=[
        "Brits chips = frieten; Amerikaans chips = chips uit een zakje.",
        "Bread, water en rice zijn ontelbaar: two slices of bread.",
        "Trousers, jeans en glasses staan altijd in het meervoud.",
        "A library is een bibliotheek, a magazine een tijdschrift.",
        "the bill (Brits) tegenover the check (Amerikaans).",
        "to do the washing-up = de afwas; to do the washing = de was.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woorden-school-en-vrije-tijd-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: school, beroepen, sport en vrije tijd",
    onder="Ook de instructietaal: de woorden waarin de opdracht zelf geschreven staat.",
    secties=[
        dict(kop="Instructietaal: lees eerst de opdracht", blokken=[
            ("p", "Op een digitaal examen staat de <strong>opdracht zelf in het Engels</strong>. "
                  "Wie die woorden niet kent, verliest punten op een vraag die hij eigenlijk "
                  "kan. Daarom staan ze hier vooraan."),
            ("fig", tabel(["opdracht", "wat je moet doen"], [
                ["Tick the correct answer.", "kruis het juiste antwoord aan"],
                ["Choose the correct answer.", "kies het juiste antwoord"],
                ["Underline the verbs.", "onderstreep de werkwoorden"],
                ["Circle the right word.", "omcirkel het juiste woord"],
                ["Cross out the wrong word.", "streep het foute woord door"],
                ["Match the words with the pictures.", "koppel de woorden aan de prenten"],
                ["Complete the sentences.", "vul de zinnen aan"],
                ["Fill in the gaps.", "vul de leegtes in"],
                ["Put the sentences in the right order.", "zet de zinnen in de juiste volgorde"],
                ["True or false?", "waar of niet waar?"],
                ["Answer in full sentences.", "antwoord met volledige zinnen"],
                ["Write about 80 words.", "schrijf ongeveer 80 woorden"],
            ]), "About betekent ongeveer; de opgegeven lengte telt mee voor je taakvoltooiing."),
            ("p", "<em>Decide if the sentence is correct</em> vraagt ook om waar of niet waar. "
                  "En <em>answer in full sentences</em> betekent: niet <em>yes</em>, maar "
                  "<em>Yes, I do</em>."),
        ]),
        dict(kop="School", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a pupil, a student", "een leerling, een student"],
                ["a teacher", "een leerkracht"],
                ["a headteacher (Brits) / a principal", "een directeur"],
                ["a subject", "een vak"],
                ["Maths (Brits) / Math", "wiskunde, voluit mathematics"],
                ["Geography, History, PE", "aardrijkskunde, geschiedenis, lichamelijke opvoeding"],
                ["a mark (Brits) / a grade", "een punt of cijfer"],
                ["homework", "huiswerk — altijd enkelvoud"],
                ["a timetable", "een uurrooster"],
                ["a playground", "een speelplaats"],
            ]), "PE staat voor physical education."),
            ("p", "<em>Homework</em> is ontelbaar, net als <em>information</em> en "
                  "<em>advice</em>: je zegt <em>my homework is difficult</em>, nooit "
                  "'homeworks'."),
            ("p", "In Brits Engels is <em>a pupil</em> eerder een leerling op school en "
                  "<em>a student</em> iemand aan de universiteit. Amerikanen zeggen bijna altijd "
                  "<em>student</em>."),
            ("p", "Getallen in schoolzinnen lees je gewoon mee: <em>Our class has twenty-four "
                  "pupils</em> zijn er 24. In het Engels staat het tiental vooraan, met een "
                  "streepje: <em>twenty-four</em>."),
        ]),
        dict(kop="Beroepen", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a nurse", "een verpleegkundige"],
                ["an engineer", "een ingenieur"],
                ["a plumber", "een loodgieter"],
                ["a lawyer", "een advocaat"],
                ["a baker", "een bakker"],
                ["a shop assistant", "een winkelbediende"],
                ["a firefighter", "een brandweerman of -vrouw"],
                ["an actor, an actress", "een acteur, een actrice"],
                ["a dancer", "een danser of danseres"],
            ]), "An office is een kantoor; 'from nine to five' is de gewone kantoordag."),
            ("p", "<em>To look for</em> betekent zoeken: <em>We are looking for a shop "
                  "assistant.</em>"),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("p", "Twee vaste regeltjes die vaak fout gaan. Bij een <strong>sport</strong> "
                  "gebruik je <em>play</em> <strong>zonder</strong> lidwoord: <em>I play "
                  "tennis</em>. Bij een <strong>instrument</strong> staat er <em>the</em> bij: "
                  "<em>I play the piano</em>, <em>He plays the guitar in a band</em>."),
            ("fig", tabel(["Engels", "Nederlands"], [
                ["to go swimming, cycling, running, skating", "gaan zwemmen, fietsen, lopen, schaatsen"],
                ["a match", "een wedstrijd"],
                ["to win, to lose", "winnen, verliezen"],
                ["a draw", "een gelijkspel"],
                ["reading, drawing, gardening", "lezen, tekenen, tuinieren"],
                ["a hobby", "een hobby"],
                ["chess", "schaken"],
            ]), "Na 'go' komt bij een sport de -ing-vorm: go swimming, twice a week."),
            ("weetje", "<em>Favourite</em> schrijf je in Brits Engels met <strong>-our-</strong>, "
                       "in Amerikaans Engels als <em>favorite</em>."),
        ]),
        dict(kop="Communicatie en multimedia", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["a mobile (Brits) / a cell phone", "een gsm"],
                ["to send a message", "een bericht sturen"],
                ["to switch off your phone", "je telefoon uitzetten"],
                ["social media, to post, to share, to like", "sociale media, posten, delen, liken"],
                ["to follow", "volgen"],
                ["to download", "binnenhalen van het internet"],
                ["to upload", "naar het internet sturen"],
                ["to chat", "babbelen — ook gewoon met je mond"],
            ]), "Down is omlaag, up is omhoog: download en upload zijn elkaars tegengestelde."),
        ]),
        dict(kop="Deze woorden in hele zinnen", blokken=[
            ("kader", "<em>A firefighter puts out fires. A baker sells bread. A nurse helps "
                      "people in a hospital.</em><br>"
                      "Een brandweerman blust branden, een bakker verkoopt brood, een "
                      "verpleegkundige helpt mensen in het ziekenhuis, waar ook de dokters "
                      "(<em>doctors</em>) werken."),
            ("kader", "<em>We are looking for a shop assistant. Send your letter before "
                      "1 October.</em><br>"
                      "Zo staat een vacature in de krant: ze zoeken een winkelbediende."),
            ("kader", "<em>He plays the guitar in a band. They play every Friday.</em><br>"
                      "Hij speelt gitaar in een groep. Bij een instrument staat er "
                      "<em>the</em>, bij een sport niet: <em>she is playing tennis</em>."),
            ("p", "Over school: <em>lessons</em> zijn de lessen, <em>the holidays</em> de "
                  "vakantie. <em>After the holidays the timetable changed</em> betekent dat het "
                  "uurrooster na de vakantie veranderde. En PE is de afgekorte vorm van "
                  "<em>physical education</em>; zulke afkortingen komen vaak terug."),
            ("p", "Over multimedia: <em>I downloaded the film yesterday</em> betekent dat je de "
                  "film gisteren hebt binnengehaald. Wat je omhoog stuurt, upload je. Wie op "
                  "een scherm typt, kijkt vaak te lang naar dat scherm, ook overdag."),
            ("p", "Tot slot de instructietaal zelf. <em>Complete the sentence</em> betekent dat "
                  "je de zin aanvult; <em>tick</em> en <em>circle</em> vragen je iets aan te "
                  "duiden; <em>decide</em> betekent dat je beslist of iets juist is. Lees dus "
                  "eerst wat de tekst van je verwacht, en vergeet (<em>forget</em>) daarna niet "
                  "wat er gevraagd werd. Wie de opdracht half leest, geeft waarschijnlijk een "
                  "juist antwoord op een andere vraag."),
            ("weetje", "<em>To speak</em> wordt in de verleden tijd <em>spoke</em>: <em>He "
                       "spoke to the teacher yesterday</em>, hij sprak gisteren met de "
                       "leerkracht. En <em>the match ended in a draw</em>: de wedstrijd "
                       "eindigde op een gelijkspel, waar het hele (<em>whole</em>) stadion op "
                       "zat te wachten. Dat gebeurt vaak (<em>often</em>) in de zomer "
                       "(<em>summer</em>)."),
        ]),
    ],
    onthoud=[
        "tick = aankruisen, underline = onderstrepen, match = koppelen, gaps = leegtes.",
        "Answer in full sentences: niet 'yes' maar 'Yes, I do'.",
        "homework, information en advice krijgen nooit een meervouds-s.",
        "I play tennis (geen the) maar I play the piano (wel the).",
        "a draw = een gelijkspel.",
        "download = binnenhalen, upload = versturen.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woorden-tijd-weer-en-reizen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: getallen, tijd, weer, reizen en landen",
    onder="Alles wat je nodig hebt om een dienstregeling, een weerbericht of een reisverslag te lezen.",
    secties=[
        dict(kop="Hoe laat is het?", blokken=[
            ("fig", svg.naast_elkaar([svg.klok(8, 15), svg.klok(5, 50), svg.klok(7, 30)]),
             "a quarter past eight — ten to six — half past seven."),
            ("p", "<strong>Past</strong> is erover, <strong>to</strong> is ervoor. "
                  "<em>A quarter past eight</em> is 8.15 uur, <em>a quarter to eight</em> is "
                  "7.45 uur, <em>ten to six</em> is 5.50 uur."),
            ("kader", "<strong>De grootste valstrik van allemaal.</strong> <em>Half past "
                      "seven</em> is <strong>half acht</strong>, niet half zeven. Het Engels "
                      "telt vanaf het uur dat <em>geweest</em> is, het Nederlands naar het uur "
                      "dat <em>komt</em>. Wie dat verwart, staat een uur te vroeg of te laat."),
            ("p", "<em>Noon</em> of <em>midday</em> is de middag, 12 uur. <em>Midnight</em> is "
                  "middernacht. <em>A.m.</em> staat voor <em>ante meridiem</em> (vóór de "
                  "middag), <em>p.m.</em> voor <em>post meridiem</em> (erna). <em>The film "
                  "starts at 7 p.m.</em> is dus 's avonds."),
        ]),
        dict(kop="Dagen, maanden en seizoenen", blokken=[
            ("fig", tabel(["dagen", "maanden", "seizoenen"], [
                ["Monday, Tuesday, Wednesday", "January, February, March", "spring (lente)"],
                ["Thursday, Friday", "April, May, June", "summer (zomer)"],
                ["Saturday, Sunday", "July, August, September", "autumn (Brits) / fall (Amerikaans)"],
                ["", "October, November, December", "winter"],
            ]), "In Wednesday spreek je de d niet uit: 'wensdee'."),
            ("p", "Dagen en maanden krijgen in het Engels een <strong>hoofdletter</strong>. In "
                  "het Nederlands schrijven we die klein; dat verschil kost punten bij het "
                  "schrijven."),
        ]),
        dict(kop="Getallen, maten en hoeveelheden", blokken=[
            ("fig", tabel(["soort", "voorbeelden"], [
                ["hoofdtelwoorden", "one, two, ten, fifteen, twenty-four, a hundred, a thousand, a million"],
                ["rangtelwoorden", "first, second, third, fourth, fifth, twelfth, twentieth"],
                ["hoeveelheden", "a dozen (twaalf), a few, a little, much, many, a lot of"],
                ["maten", "kilos, miles (1 mile ≈ 1,6 km), degrees (graden)"],
            ]), "Bij een datum gebruik je een rangtelwoord: the third of May, the fifth of June."),
            ("p", "<strong>A few of a little?</strong> <em>A few</em> gebruik je bij dingen die "
                  "je kan tellen (<em>a few eggs</em>), <em>a little</em> bij ontelbare "
                  "(<em>a little milk</em>, <em>a little time</em>). Zo ook: <em>many "
                  "books</em>, maar <em>much water</em> en <em>a lot of water</em>."),
            ("p", "<em>To weigh</em> is wegen. <em>The box weighs three kilos.</em> In het "
                  "Verenigd Koninkrijk en de Verenigde Staten meet men afstanden in "
                  "<em>miles</em>."),
        ]),
        dict(kop="Het weer", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["sunny, cloudy", "zonnig, bewolkt"],
                ["rainy, a shower", "regenachtig, een bui"],
                ["windy, foggy, snowy", "winderig, mistig, met sneeuw"],
                ["freezing", "ijskoud"],
                ["it is raining", "het regent (nu)"],
                ["an umbrella", "een paraplu"],
                ["the temperature drops / rises", "de temperatuur daalt / stijgt"],
                ["a degree", "een graad"],
            ]), "Crowded (druk met mensen) zegt niets over het weer."),
            ("p", "Weer dat op dit moment bezig is, zet je in de present continuous: <em>it is "
                  "raining</em>. Weer dat vaak gebeurt, in de present simple: <em>it often rains "
                  "here</em>."),
        ]),
        dict(kop="Reizen en vervoer", blokken=[
            ("fig", tabel(["Engels", "Nederlands"], [
                ["by bike, by car, by bus, by train, by plane", "met de fiets, auto, bus, trein, het vliegtuig"],
                ["on foot", "te voet — de enige met on"],
                ["a flight, delayed, cancelled", "een vlucht, vertraagd, geannuleerd"],
                ["a boarding pass, luggage, a gate", "een instapkaart, bagage, een gate"],
                ["a platform, to depart, to arrive", "een perron, vertrekken, aankomen"],
                ["a single ticket / a one-way ticket", "een enkele reis"],
                ["a return ticket", "een ticket heen en terug"],
                ["a suitcase, a passport, a ticket", "een koffer, een paspoort, een ticket"],
                ["to stay, a hotel, the beach", "verblijven, een hotel, het strand"],
            ]), "Een gate hoort bij de luchthaven, een platform bij het station."),
            ("p", "De weg vragen: <em>Excuse me, how do I get to the museum?</em> Het antwoord "
                  "bevat meestal <em>go straight on</em> (rechtdoor), <em>turn left</em> (links "
                  "afslaan), <em>turn right</em> (rechts afslaan), of een herkenningspunt zoals "
                  "<em>the church</em> (de kerk)."),
        ]),
        dict(kop="Landen en nationaliteiten", blokken=[
            ("fig", tabel(["land", "nationaliteit"], [
                ["Belgium", "Belgian"],
                ["Spain", "Spanish"],
                ["France", "French"],
                ["Scotland", "Scottish"],
                ["Ireland", "Irish"],
                ["the United Kingdom (hoofdstad: London)", "British"],
            ]), "Landen én nationaliteiten schrijf je in het Engels met een hoofdletter."),
            ("p", "<em>Holiday</em> (Brits) en <em>vacation</em> (Amerikaans) betekenen allebei "
                  "vakantie. Een Brit gaat <em>on holiday</em>, een Amerikaan <em>on "
                  "vacation</em>. In het Brits kan <em>a holiday</em> ook één feestdag zijn."),
        ]),
        dict(kop="Deze woorden in hele zinnen", blokken=[
            ("kader", "<em>The train leaves at 8.15 and arrives at 9.40. It is two hours "
                      "delayed.</em><br>"
                      "De trein vertrekt om kwart over acht en komt om twintig voor tien aan. "
                      "Twee uur vertraging, dus. <em>To leave</em> is vertrekken, <em>to "
                      "arrive</em> aankomen."),
            ("kader", "<em>The shop opens on Wednesday at nine and the film starts "
                      "tomorrow at 8 p.m.</em><br>"
                      "De winkel opent woensdag om negen uur, de film begint morgen om acht "
                      "uur \'s avonds."),
            ("kader", "<em>The box weighs three kilos. The station is about two miles from "
                      "here.</em><br>"
                      "De doos weegt drie kilogram en is dus niet zo zwaar; het station ligt "
                      "ongeveer twee mijl verderop, wat iets meer dan drie kilometer is."),
            ("p", "Getallen: <em>a hundred</em> is honderd, <em>a thousand</em> duizend. Een "
                  "<em>dozen</em> is twaalf, geen cijfer maar een aantal. Bij een datum of een "
                  "afspraak (<em>a meeting</em>) gebruik je een rangtelwoord: <em>the meeting "
                  "is on the third of May</em>."),
            ("p", "Op reis: <em>we stayed in a small hotel near the beach</em> betekent dat we "
                  "in een klein hotel bij het strand verbleven en er dus ook sliepen. Wie "
                  "reist, moet een geldig document bij zich hebben, en dat is een ander "
                  "document dan je ticket: een <em>passport</em>."),
            ("p", "Bij vervoermiddelen hoort het <strong>voorzetsel</strong> <em>by</em>: "
                  "<em>by bike</em>, <em>by bus</em>, <em>by train</em>. Alleen te voet is het "
                  "<em>on foot</em>. Ga je naar school, dan zeg je <em>I go to school by "
                  "bike</em>, zonder lidwoord voor <em>school</em>."),
            ("p", "En het weer: <em>showers</em> zijn buien, <em>it is raining outside</em> "
                  "betekent dat het nu buiten regent. Wie het weer van morgen beschrijft, "
                  "gebruikt <em>tomorrow</em> en <em>will</em>: <em>Tomorrow it will be "
                  "sunny.</em> Zo vraagt een persoon ook naar het weer: <em>What will the "
                  "weather be like?</em>"),
        ]),
    ],
    onthoud=[
        "half past seven = half acht. Past is erover, to is ervoor.",
        "noon = 12 uur 's middags, midnight = 12 uur 's nachts.",
        "Dagen en maanden: hoofdletter.",
        "a few bij telbare dingen, a little bij ontelbare.",
        "by bike, by car, by train — maar on foot.",
        "a return ticket = heen en terug; a single ticket = enkele reis.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["grammatica-naamwoorden-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Grammatica: naamwoorden, lidwoorden en voornaamwoorden",
    onder="Meervouden, a of an, this of these, my of mine, en de trappen van vergelijking.",
    secties=[
        dict(kop="Het meervoud van een naamwoord", blokken=[
            ("fig", tabel(["regel", "voorbeeld"], [
                ["gewoon -s", "book – books, table – tables"],
                ["-es na s, x, ch, sh", "box – boxes, watch – watches, dish – dishes, bus – buses"],
                ["-y na een medeklinker wordt -ies", "baby – babies, city – cities"],
                ["-y na een klinker blijft -y", "boy – boys, day – days"],
                ["-f of -fe wordt vaak -ves", "knife – knives, leaf – leaves, wife – wives"],
                ["onregelmatig", "man – men, woman – women, child – children, tooth – teeth, foot – feet, mouse – mice"],
            ]), "De onregelmatige meervouden moet je uit het hoofd kennen; er zit geen regel achter."),
            ("p", "Sommige woorden hebben <strong>geen</strong> meervoud: <em>information</em>, "
                  "<em>advice</em>, <em>homework</em>. Je zegt <em>much information</em> of "
                  "<em>a piece of advice</em>."),
        ]),
        dict(kop="Lidwoorden: a, an en the", blokken=[
            ("p", "<em>The</em> is het <strong>bepaalde</strong> lidwoord (definite article): je "
                  "weet over welk ding het gaat. <em>A</em> en <em>an</em> zijn "
                  "<strong>onbepaald</strong> (indefinite): het maakt niet uit welke."),
            ("kader", "<strong>A of an?</strong> Het gaat om de <strong>klank</strong>, niet om "
                      "de letter. <em>An elephant</em>, <em>an apple</em>, <em>an hour</em> (de h "
                      "zwijgt) — maar <em>a university</em>, want dat begint met een joe-klank."),
            ("p", "Bij een <strong>beroep</strong> staat er in het Engels altijd een lidwoord: "
                  "<em>She is a teacher</em>, <em>He is an engineer</em>. In het Nederlands laten "
                  "we dat weg."),
        ]),
        dict(kop="Determiners: dit, dat, mijn, welk", blokken=[
            ("fig", tabel(["soort", "vormen", "voorbeeld"], [
                ["aanwijzend (demonstrative)", "this, these (dichtbij) — that, those (veraf)",
                 "This book here is mine. Those books are theirs."],
                ["bezittelijk (possessive adjective)", "my, your, his, her, its, our, their",
                 "my book, her bag"],
                ["vragend (interrogative adjective)", "which, what, whose",
                 "Which film do you prefer? Whose bag is this?"],
            ]), "This en that zijn enkelvoud, these en those meervoud."),
            ("p", "<strong>Which of what?</strong> <em>Which</em> gebruik je als er een "
                  "beperkte keuze is (<em>Which colour, red or blue?</em>), <em>what</em> als de "
                  "keuze open is (<em>What is your favourite subject?</em>). En <em>whose</em> "
                  "vraagt naar de eigenaar — niet te verwarren met <em>who's</em>, dat <em>who "
                  "is</em> betekent."),
            ("kader", "<strong>Its of it's?</strong> <em>It's</em> met apostrof betekent <em>it "
                      "is</em>. <em>Its</em> zonder apostrof is het bezittelijke: <em>The dog "
                      "wagged its tail.</em> Een klassieke valstrik."),
        ]),
        dict(kop="Voornaamwoorden: ik, mij, de mijne", blokken=[
            ("fig", tabel(["onderwerp (subject)", "voorwerp (object)", "bezittelijk voornaamwoord"], [
                ["I", "me", "mine"],
                ["you", "you", "yours"],
                ["he / she / it", "him / her / it", "his / hers / its"],
                ["we", "us", "ours"],
                ["they", "them", "theirs"],
            ]), "Mine, yours, hers en theirs staan alleen, zonder naamwoord erachter."),
            ("p", "<strong>De plaats van het persoonlijk voornaamwoord.</strong> De vorm vóór "
                  "het werkwoord is het onderwerp (<em>Sarah and I went to the cinema</em>), de "
                  "vorm erna is het voorwerp (<em>Tom helped me</em>). En die staat "
                  "<strong>achter</strong> het werkwoord: <em>I saw him</em>, nooit 'I him "
                  "saw'."),
            ("p", "Vragende voornaamwoorden: <em>what</em> (wat), <em>who</em> (wie), "
                  "<em>where</em> (waar), <em>when</em> (wanneer), <em>whose</em> (van wie)."),
        ]),
        dict(kop="Bijvoeglijke naamwoorden en de trappen van vergelijking", blokken=[
            ("fig", tabel(["soort", "vergrotende trap", "overtreffende trap"], [
                ["kort (big, small, easy)", "bigger, smaller, easier", "the biggest, the smallest, the easiest"],
                ["lang (expensive, interesting)", "more expensive", "the most expensive"],
                ["onregelmatig", "good – better / bad – worse / far – further", "the best / the worst / the furthest"],
            ]), "Bij één korte klinker verdubbelt de medeklinker: big wordt bigger, hot wordt hotter."),
            ("p", "Bij een vergelijking hoort <strong>than</strong>: <em>This exercise is easier "
                  "than the first one.</em> Bij een gelijkheid <strong>as … as</strong>: "
                  "<em>She is as tall as her brother.</em> En nooit allebei tegelijk: "
                  "<em>more better</em> bestaat niet, het is gewoon <em>better</em>."),
            ("p", "Een bijvoeglijk naamwoord staat in het Engels <strong>vóór</strong> het "
                  "naamwoord en verandert <strong>nooit</strong> van vorm: <em>a red car</em>, "
                  "<em>red cars</em>. Geen -s dus, ook niet in het meervoud."),
        ]),
        dict(kop="Telwoorden en voorzetsels", blokken=[
            ("p", "<strong>Hoofdtelwoorden</strong> (cardinal numbers) tellen: <em>one, two, "
                  "fifteen</em>. <strong>Rangtelwoorden</strong> (ordinal numbers) zeggen de "
                  "plaats in een rij: <em>first, second, third, twelfth, twentieth</em>. "
                  "<em>He came second in the race.</em> Let op de lastige: <em>five → "
                  "fifth</em>, <em>nine → ninth</em>, <em>twelve → twelfth</em>."),
            ("fig", tabel(["voorzetsel", "waarvoor", "voorbeeld"], [
                ["at", "een uur", "at nine o'clock"],
                ["on", "een dag of datum", "on Monday, on the third of May"],
                ["in", "een maand, seizoen of jaar", "in May, in winter, in 2027"],
                ["in", "een land of stad", "in Belgium, in London"],
                ["by", "een vervoermiddel", "by bike, by bus, by train"],
                ["on", "te voet", "on foot"],
                ["plaats", "on (op), in (in), under (onder), next to (naast), between (tussen), behind (achter), in front of (voor)", "The cat is on the table."],
            ]), "At voor een punt in de tijd, on voor een dag, in voor een langere periode."),
        ]),
        dict(kop="De Engelse namen, en nog wat voorbeelden", blokken=[
            ("p", "De vergrotende trap heet in het Engels de <strong>comparative</strong>, de "
                  "overtreffende trap de <strong>superlative</strong>. Je zal die namen op een "
                  "examen tegenkomen, dus onthoud ze samen met de vormen."),
            ("kader", "<em>Sarah helped me with the exercise. I thanked her.</em><br>"
                      "Sarah hielp mij: <em>me</em> is het voorwerp, want het staat achter het "
                      "werkwoord. <em>Her</em> is dat ook. In <em>I saw him</em> is <em>him</em> "
                      "het lijdend voorwerp."),
            ("kader", "<em>My cousins live in Wales. They have a farm there.</em><br>"
                      "<em>They</em> wijst naar de neven en nichten: meerdere personen, dus een "
                      "meervoud. Wil je weten waarnaar een verwijswoord wijst, zoek dan het "
                      "dichtstbijzijnde woord ervóór dat past — soms is dat een hele groep."),
            ("p", "Nog wat zinnen om de vormen in te zien: <em>The lesson starts at nine.</em> "
                  "<em>She lives near the school.</em> <em>We walked to the station.</em> "
                  "<em>The meeting is on the third of May.</em> In elk van die zinnen staat een "
                  "bijvoeglijk naamwoord of een lidwoord op zijn vaste plaats, en je hoeft er "
                  "geen extra woord bij te zetten."),
        ]),
    ],
    onthoud=[
        "box – boxes, baby – babies, knife – knives, child – children, foot – feet.",
        "a of an hangt af van de klank: an hour, a university.",
        "this/these dichtbij, that/those veraf.",
        "my book, maar this book is mine.",
        "it's = it is; its = van hem/haar/het.",
        "korte woorden -er/-est, lange more/most, en nooit 'more better'.",
        "at een uur, on een dag, in een maand.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["grammatica-werkwoorden-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Grammatica: werkwoorden, tijden en zinsbouw",
    onder="De zes tijden uit de vakfiche, de soorten zinnen, en wat bij wat hoort.",
    secties=[
        dict(kop="De tijden die je moet kennen", blokken=[
            ("fig", tabel(["tijd", "vorm", "wanneer"], [
                ["infinitive", "to swim, to be, to have", "de basisvorm, zoals in het woordenboek"],
                ["imperative", "Close the door. Don't forget!", "een bevel of een instructie"],
                ["present simple", "I work, she works", "een gewoonte: she goes to school every day"],
                ["present continuous", "I am working, it is raining", "wat nu bezig is: Look, it is raining!"],
                ["past simple", "I worked, we went", "gebeurd en afgelopen: last summer we went to Spain"],
                ["future simple", "I will help, he will be", "de toekomst, met will"],
            ]), "De zes vormen die de vakfiche opsomt."),
            ("p", "<strong>Present simple of continuous?</strong> <em>I read every evening</em> "
                  "is een gewoonte. <em>I am reading now</em> is op dit moment bezig. "
                  "Werkwoorden van weten, vinden en voelen (<em>to know</em>, <em>to like</em>) "
                  "gebruik je normaal <strong>niet</strong> in de continuous: je zegt <em>I know "
                  "the answer</em>, niet 'I am knowing'."),
            ("p", "De continuous maak je met <em>to be</em> + <em>-ing</em>: <em>she is "
                  "writing</em>, <em>they are watching</em>. De -e van <em>write</em> valt weg "
                  "voor -ing."),
        ]),
        dict(kop="De -s bij he, she en it", blokken=[
            ("fig", svg.persoonsvormen([
                ("I|you|we|they", "work", "#2f5d50"),
                ("he|she|it", "works", "#c06a2a"),
            ]), "De overeenkomst tussen onderwerp en persoonsvorm, in de present simple."),
            ("p", "Die -s heet de <strong>overeenkomst</strong> (agreement) tussen onderwerp en "
                  "persoonsvorm. In een vraag of een ontkenning verhuist ze naar het "
                  "hulpwerkwoord: <em>Does she live in Ghent?</em> en <em>He doesn't like "
                  "tea</em> — dus niet 'does she lives' of 'doesn't likes'."),
            ("p", "De persoonsvorm volgt het <strong>onderwerp</strong>, niet het woord dat er "
                  "toevallig vlak voor staat: <em>The books on the table <strong>are</strong> "
                  "mine.</em> En twee personen samen zijn meervoud: <em>My sister and I are "
                  "going.</em>"),
        ]),
        dict(kop="Verleden tijd: regelmatig en onregelmatig", blokken=[
            ("p", "Regelmatige werkwoorden krijgen <strong>-ed</strong>: <em>played, worked, "
                  "watched</em>. Staat er al een -e, dan komt er alleen een -d bij: "
                  "<em>liked</em>."),
            ("fig", tabel(["infinitief", "past simple", "voltooid deelwoord"], [
                ["to go", "went", "gone"],
                ["to see", "saw", "seen"],
                ["to take", "took", "taken"],
                ["to buy", "bought", "bought"],
                ["to bring", "brought", "brought"],
                ["to think", "thought", "thought"],
                ["to be", "was / were", "been"],
            ]), "Na have komt het voltooid deelwoord: I have gone. 'I have went' bestaat niet."),
            ("p", "<em>To be</em> is het onregelmatigste van allemaal: <em>I was, you were, he "
                  "was, we were, they were</em>."),
            ("p", "De vakfiche noemt de <strong>signaalwoorden</strong> bij de past simple: "
                  "<em>ago</em>, <em>yesterday</em>, <em>last week</em>. Ook <em>last summer</em> "
                  "en <em>last year</em> horen daarbij. Zie je die staan, dan weet je welke tijd "
                  "je nodig hebt."),
            ("p", "De toekomst maak je met <strong>will</strong> + het werkwoord zonder to: "
                  "<em>I will call you tonight</em>, <em>She will be fifteen in June</em>. "
                  "<em>Will</em> verandert nooit: ook <em>he will</em>, nooit 'he wills'."),
        ]),
        dict(kop="Soorten zinnen", blokken=[
            ("fig", tabel(["soort", "Engels", "voorbeeld"], [
                ["mededelend", "declarative sentence", "My sister lives in Antwerp."],
                ["vragend", "interrogative sentence", "Do you like coffee?"],
                ["bevelend", "imperative sentence", "Close the door, please."],
                ["uitroepend", "exclamative sentence", "What a beautiful day!"],
                ["ontkennend", "negative sentence", "I don't like fish. We never go there."],
                ["bevestigend", "affirmative sentence", "They are happy."],
            ]), "Een bevelende zin heeft geen onderwerp: het werkwoord staat vooraan."),
            ("p", "Een vraag in de present simple maak je met <strong>do</strong> of "
                  "<strong>does</strong>: <em>Do you like coffee?</em>, <em>Does she live in "
                  "Ghent?</em> Ontkennen doe je met <em>don't</em> en <em>doesn't</em>, of met "
                  "<em>not</em> en <em>never</em>."),
            ("p", "<em>Don't forget your keys!</em> is tegelijk <strong>bevelend</strong> en "
                  "<strong>ontkennend</strong>, met een uitroepteken erbij — en zonder "
                  "onderwerp, zoals elke imperative."),
        ]),
        dict(kop="Enkelvoudige en samengestelde zinnen", blokken=[
            ("p", "Een <strong>enkelvoudige</strong> zin heeft één persoonsvorm: <em>The dog "
                  "barked.</em> Een <strong>samengestelde</strong> zin heeft er twee of meer, "
                  "verbonden door een voegwoord: <em>I like reading, but my brother prefers "
                  "football.</em>"),
            ("fig", svg.zinsdelen([
                ("The children", "onderwerp (subject)", "#2f5d50"),
                ("played", "persoonsvorm (finite verb)", "#c06a2a"),
                ("outside", "rest van de zin", "#6b7a63"),
            ]), "Het onderwerp is wie of wat het werkwoord doet; de persoonsvorm verandert met de tijd."),
            ("p", "De frequente voegwoorden uit de vakfiche: <em>and</em>, <em>but</em>, "
                  "<em>so</em>, <em>when</em> en <em>because</em>. <em>I was tired, so I went to "
                  "bed early</em> — <em>so</em> geeft het gevolg, <em>because</em> de reden. "
                  "<em>Very</em> is géén voegwoord: dat versterkt alleen een bijvoeglijk "
                  "naamwoord."),
        ]),
        dict(kop="Spelling en klank", blokken=[
            ("p", "De vakfiche vraagt dat je de <strong>spelling van frequente woorden</strong> "
                  "beheerst en dat je de relatie tussen <strong>klank- en schriftbeeld</strong> "
                  "kent. Enkele woorden waar het vaak misgaat: <em>because</em> (niet becouse), "
                  "<em>friend</em>, <em>their</em> tegenover <em>there</em>, <em>its</em> "
                  "tegenover <em>it's</em>."),
            ("weetje", "Een ezelsbruggetje voor <em>because</em>: <strong>B</strong>ig "
                       "<strong>E</strong>lephants <strong>C</strong>an <strong>A</strong>lways "
                       "<strong>U</strong>nderstand <strong>S</strong>mall "
                       "<strong>E</strong>lephants."),
            ("p", "De <strong>uitspraak</strong> zelf — klanken, woordklemtoon, articulatie en "
                  "intonatie — hoort bij luisteren en spreken. Die oefen je hier niet: daar heb "
                  "je geluid en een gesprekspartner voor nodig."),
        ]),
        dict(kop="Nog wat zinnen om op te oefenen", blokken=[
            ("p", "<em>Doesn\'t</em> en <em>don\'t</em> zijn <strong>samengetrokken</strong> "
                  "vormen van <em>does not</em> en <em>do not</em>. Op een examen mag je "
                  "allebei schrijven, als je maar consequent blijft binnen één tekst."),
            ("kader", "<em>It is raining. → Het regent nu.</em> Iets dat aan het regenen is, "
                      "zet je in de present continuous.<br>"
                      "<em>I will write a letter tomorrow.</em> Een brief die je morgen gaat "
                      "schrijven staat in de <strong>toekomende</strong> tijd, met "
                      "<em>will</em>.<br>"
                      "<em>Last year we went to London for our holiday.</em> Vorig jaar, dus de "
                      "past simple; die vakantie is voorbij."),
            ("p", "De <strong>derde</strong> persoon enkelvoud is de enige die een -s krijgt: "
                  "<em>he writes</em>, <em>she finished her homework</em>. Schrijf je een zin "
                  "zelf, kijk dan altijd na of die -s er staat waar hij hoort; een correcte "
                  "persoonsvorm is het eerste wat opvalt."),
            ("p", "Welke <strong>zinssoort</strong> heb je voor je? <em>Close the door.</em> is "
                  "bevelend. <em>What a beautiful day!</em> is uitroepend. <em>Do you like "
                  "coffee?</em> is vragend. <em>My sister lives in Antwerp.</em> is mededelend. "
                  "En voegwoorden verbinden twee zinnen tot één samengestelde zin; welk "
                  "voegwoord je kiest, zegt hoe de delen samenhangen. Kijk dus goed of je "
                  "antwoord echt juist (<em>right</em>) is voor die ene zin."),
        ]),
    ],
    onthoud=[
        "he, she, it krijgen een -s: she goes. In een vraag verhuist die naar does.",
        "present simple = gewoonte, present continuous = nu bezig.",
        "Signaalwoorden voor de past simple: ago, yesterday, last week.",
        "go–went–gone, see–saw–seen, buy–bought–bought.",
        "will verandert nooit, en erna komt het werkwoord zonder to.",
        "Eén persoonsvorm = enkelvoudige zin; twee of meer = samengesteld.",
    ],
)

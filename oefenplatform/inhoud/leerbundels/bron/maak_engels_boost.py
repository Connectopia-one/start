# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor Engels op 🚀 Boost doorstroom-niveau.

Gebaseerd op de twee vakfiches Engels van de 2de graad doorstroomfinaliteit,
geldig vanaf 1 januari 2027. Engels 1 gaat over lezen (50 %) en luisteren
(50 %), Engels 2 over schrijven (29 %), schriftelijke interactie (29 %),
mondelinge interactie (30 %), spreken (8 %) en literatuurbeleving (4 %).
Allebei gelden ze voor economische wetenschappen, humane wetenschappen,
natuurwetenschappen en Latijn. Het ERK-niveau is B1.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/engels.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie. De oefenbundels dragen daarbovenop het voorvoegsel "oefenbundel-".

In elke bundel staat achteraan hetzelfde kader: luisteren is de helft van het
examen Engels 1, en mondelinge interactie en spreken zijn samen 38 % van
Engels 2. Dat zijn precies de stukken die je niet achter een scherm leert.
De opdracht in dat kader is telkens een andere, en hoort bij het thema van
de bundel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Engels"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def luister(opdracht):
    """Het vaste slotkader over oefenen buiten het scherm."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je lezen, woordenschat en grammatica. Maar <strong>luisteren</strong> is "
              "de helft van het examen Engels 1, en <strong>mondelinge interactie</strong> (30 %) en "
              "<strong>spreken</strong> (8 %) zijn samen <strong>38 %</strong> van Engels 2. Die drie leer je "
              "niet achter een scherm. Je leert ze door te luisteren naar mensen die echt Engels spreken, en "
              "door zelf je mond open te doen, ook als het hakkelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en let daarna op wat je "
                  "miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


# ───────────────────────── 1. Een Engelse tekst analyseren
BUNDELS["een-engelse-tekst-analyseren-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Een Engelse tekst analyseren",
    onder="Onderwerp en hoofdgedachte vinden, gericht zoeken, tussen de regels lezen en het oordeel van de schrijver horen.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie woorden die op elkaar lijken en die je uit elkaar moet houden. Het "
                  "<strong>onderwerp</strong> van een tekst zeg je in <strong>enkele woorden</strong>: waar gaat "
                  "hij over? De <strong>hoofdgedachte</strong> zeg je in <strong>een hele zin</strong>: wat zegt "
                  "de tekst daarover? En de <strong>hoofdpunten</strong> zijn de elementen die de hoofdgedachte "
                  "<strong>ondersteunen</strong>."),
            ("p", tabel(["", "Hoe lang", "Voorbeeld"], [
                ["onderwerp", "enkele woorden", "de nestplaatsen van gierzwaluwen"],
                ["hoofdgedachte", "een hele zin", "Gierzwaluwen verliezen hun nestplaatsen, en steden doen daar iets aan."],
                ["hoofdpunten", "de zinnen eronder", "They nest under roof tiles and in wall cavities."],
            ])),
            ("kader", "Krijg je een vraag over de <strong>hoofdgedachte</strong>, antwoord dan nooit met een "
                      "<strong>los woord</strong>. Een los woord is het onderwerp. De hoofdgedachte is een zin."),
            ("p", "Snap je de hoofdgedachte van een tekst niet, lees dan eerst de "
                  "<strong>titel en de eerste en laatste zin</strong> opnieuw. Daar staat ze in negen van de "
                  "tien teksten, in andere woorden."),
        ]),
        dict(kop="Wat er staat, en wat je eruit afleidt", blokken=[
            ("p", "Niet elk antwoord staat letterlijk in de tekst. Een deel van de vragen vraagt je om iets "
                  "<strong>af te leiden</strong>: je legt twee zinnen naast elkaar en trekt zelf de conclusie. "
                  "Alles wat je afleidt moet <strong>volgen uit</strong> de tekst, maar het hoeft er niet "
                  "letterlijk in te staan."),
            ("p", tabel(["Wat er staat", "Wat je eruit afleidt"], [
                ["Because many old buildings are being renovated, those nesting places are disappearing fast.",
                 "Steden vragen neststenen in nieuwe muren omdat de oude nestplaatsen bij renovatie verdwijnen."],
                ["Unlike her sister, Maya has never been abroad.", "De zus is wel al in het buitenland geweest."],
                ["The tickets sold out within an hour.", "De tickets waren heel snel uitverkocht."],
                ["The museum is closed on Mondays and on public holidays.",
                 "Op maandag 1 mei is het museum zeker gesloten: het is allebei."],
                ["Students who have not returned the form by Friday will not be able to join the trip.",
                 "Heb je het formulier niet terugbezorgd, dan mag je niet mee op de reis."],
            ])),
            ("weetje", "<em>Unlike</em> is het handigste woordje van de hele leestoets. Het vergelijkt twee "
                       "dingen en zegt meteen dat ze verschillen. Over het ene ding staat er iets, over het "
                       "andere weet je dan automatisch het tegendeel."),
        ]),
        dict(kop="Zoeken, en een woord dat je niet kent", blokken=[
            ("p", "Krijg je een <strong>lange tekst en één gerichte vraag</strong>, bijvoorbeeld op welke dag de "
                  "bus vertrekt, dan lees je die tekst niet van voor naar achter. Je <strong>zoekt in de tekst "
                  "naar een dag of een datum</strong> en je leest alleen die zin volledig. Hetzelfde geldt voor "
                  "een prijs, een naam of een uur: je weet welke vorm je zoekt, dus je scant erop."),
            ("p", "Je mag op het examen een <strong>online woordenboek</strong> gebruiken. Dat klinkt "
                  "geruststellender dan het is: je hebt <strong>niet de tijd om elk woord op te zoeken</strong>. "
                  "Je hebt dus een <strong>basiswoordenschat</strong> nodig, en je spaart het woordenboek voor de "
                  "twee of drie woorden waar de vraag echt op staat of valt."),
            ("p", "Ontgaat je één woord terwijl je de zin verder wel begrijpt, dan zoek je niets op: je "
                  "<strong>leidt de betekenis af uit de rest van de zin</strong>. Wie in <em>they nest under roof "
                  "tiles</em> het woord <em>tiles</em> niet kent, weet door <em>roof</em> en <em>nest</em> al "
                  "genoeg om verder te lezen."),
            ("kader", "Een tekst <strong>analyseren</strong> is niet hetzelfde als een tekst <strong>letterlijk "
                      "vertalen</strong>. Je moet de boodschap eruit halen, niet elke zin omzetten. Wie vertaalt, "
                      "is na twee alinea's door zijn tijd."),
        ]),
        dict(kop="Het oordeel in een tekst horen", blokken=[
            ("p", "Bij een <strong>opiniërende</strong> tekst, zoals een <strong>hotelbeoordeling</strong> of een "
                  "filmrecensie, is de vraag zelden of de schrijver tevreden was, maar <strong>hoe</strong> "
                  "tevreden, en <strong>waarover</strong>. Een oordeel is vaak <strong>gemengd</strong>: goede "
                  "kamers en vriendelijk personeel, maar een slecht ontbijt."),
            ("p", "Het oordeel zit in een handvol woorden. In een hotelbeoordeling dragen "
                  "<em>disappointing</em>, <em>cold coffee</em> en <em>very little choice</em> het negatieve "
                  "deel. De rest van de zinnen is vriendelijk, maar die drie woorden bepalen de toon."),
            ("p", tabel(["Zin", "Wat er gezegd wordt"], [
                ["the staff could not have been friendlier", "het personeel was heel vriendelijk"],
                ["two hours I will never get back", "de film was verloren tijd"],
                ["a masterpiece", "een lovend oordeel over diezelfde film"],
            ])),
            ("p", "Lees je twee teksten over dezelfde film waarvan de ene hem <em>a masterpiece</em> noemt en de "
                  "andere <em>two hours I will never get back</em>, dan is het antwoord niet dat er één gelijk "
                  "heeft: de twee schrijvers geven een <strong>tegengesteld oordeel</strong>."),
            ("weetje", "<em>Could not have been friendlier</em> is een lofbetuiging in de vorm van een "
                       "ontkenning. Letterlijk: vriendelijker had niet gekund. Het Engels doet dat vaker, en wie "
                       "alleen op <em>not</em> let, leest het oordeel precies omgekeerd."),
        ]),
        dict(kop="Alinea's, verbanden en soorten teksten", blokken=[
            ("p", "Een tekst is in <strong>alinea's</strong> verdeeld, en die <strong>alinea-indeling</strong> is "
                  "geen opmaak maar inhoud. Daarom is ze <strong>nuttig</strong> zodra je een tekst "
                  "<strong>analyseert</strong>: elke alinea heeft meestal <strong>één eigen punt</strong>. Weet "
                  "je per alinea wat er staat, dan zie je ook welke <strong>functie</strong> alinea 3 heeft ten "
                  "opzichte van de <strong>vorige</strong>. Een alinea kan een <strong>oorzaak geven</strong>, "
                  "een <strong>tegenstelling maken</strong> of een <strong>voorbeeld geven</strong>."),
            ("p", "Binnen een zin doen kleine woordjes hetzelfde werk. In <em>By the evening my legs hurt, but I "
                  "would do it again tomorrow</em> legt <strong>but</strong> een <strong>tekstverband</strong>, en wel een <strong>tegenstelling</strong>: "
                  "de benen deden pijn, en toch zou de schrijver het overdoen. De hoofdgedachte van zo'n "
                  "reisverslag is dan ook dat de schrijver de lange wandeling de moeite vond, ondanks de "
                  "vermoeidheid."),
            ("p", "Welke <strong>tekstsoort</strong> je voor je hebt, bepaalt waar je moet kijken. Een "
                  "<strong>hotelbeoordeling</strong> op een online platform is <strong>opiniërend</strong>. Een "
                  "<strong>recept</strong> en een <strong>bijsluiter</strong> zijn allebei "
                  "<strong>prescriptief</strong>: ze zeggen wat je moet doen. Een <strong>lied</strong>, een "
                  "<strong>gedicht</strong> en een <strong>kortverhaal</strong> zijn <strong>literair</strong>. "
                  "Een tekst die je probeert te overtuigen of te beïnvloeden, heet "
                  "<strong>persuasief</strong>."),
            ("kader", "Een <strong>krantenartikel</strong> en een <strong>interview</strong> zijn géén "
                      "opiniërende teksten: ze geven informatie. Dat er in een interview meningen van anderen "
                      "staan, verandert daar niets aan."),
            ("p", "In een <strong>prescriptieve</strong> tekst let je op de volgorde. Staat er <em>Before you "
                  "start, read all the steps</em>, dan is dat de eerste stap: <strong>alle stappen "
                  "doorlezen</strong>. En <em>Do not add the butter until the mixture is smooth</em> betekent "
                  "dat je de boter pas toevoegt <strong>als het mengsel glad is</strong>, niet ervoor. Zo'n tekst "
                  "staat vol <strong>aanwijzingen</strong> in de gebiedende wijs, de "
                  "<strong>imperatieven</strong>: <em>Preheat the oven</em>, <em>Mix the flour</em>, "
                  "<em>Bake for 25 minutes</em>."),
            ("p", "Al die namen van tekstsoorten zijn <strong>vakwoorden</strong>: persuasief, opiniërend, "
                  "prescriptief, narratief, informatief en literair. Je moet ze niet alleen herkennen maar ook "
                  "zelf kunnen opschrijven, want een vraag kan er uitdrukkelijk naar vragen. En wat je uit een "
                  "zin <strong>besluit</strong>, zeg je in je eigen woorden: dat is de kern van analyseren."),
            ("p", "In een <strong>persuasieve</strong> campagnetekst zoek je de <strong>oproep</strong> en de "
                  "<strong>onderbouwing</strong>. <em>Slow down</em> wil dat je trager rijdt in de bebouwde kom; "
                  "de zin <em>A child hit at 50 km/h is five times more likely to die than a child hit at 30 "
                  "km/h</em> dient om die oproep <strong>te onderbouwen met een cijfer</strong>: het "
                  "<strong>risico</strong> is vijf keer groter. En <em>Every second you save "
                  "could cost a life</em> betekent dat elke seconde die je wint een leven kan kosten."),
        ]),
        luister("kijk een aflevering van een Engelstalige reeks met Engelse ondertitels in plaats van "
                "Nederlandse, en schrijf achteraf in drie zinnen op waar ze over ging."),
    ],
    onthoud=[
        "Het onderwerp zeg je in enkele woorden, de hoofdgedachte in een hele zin. Antwoord op een vraag naar de hoofdgedachte dus nooit met een los woord.",
        "De hoofdpunten zijn de elementen die de hoofdgedachte ondersteunen.",
        "Vind je de hoofdgedachte niet, lees dan de titel en de eerste en laatste zin opnieuw.",
        "Wat je afleidt, moet volgen uit de tekst maar hoeft er niet letterlijk in te staan.",
        "Unlike her sister betekent dat het voor de zus juist wél geldt.",
        "Eén gerichte vraag bij een lange tekst: zoek naar de vorm die je nodig hebt, een dag, een datum, een prijs.",
        "Je mag een online woordenboek gebruiken, maar je hebt niet de tijd om elk woord op te zoeken.",
        "Ken je één woord niet en begrijp je de zin verder wel, dan leid je de betekenis af uit de rest van de zin.",
        "Een tekst analyseren is niet hetzelfde als een tekst letterlijk vertalen.",
        "Een oordeel is vaak gemengd. Zoek de woorden die het dragen: disappointing, cold coffee, very little choice.",
        "Could not have been friendlier betekent heel vriendelijk, geen kritiek.",
        "Elke alinea heeft meestal één eigen punt: een oorzaak geven, een tegenstelling maken, een voorbeeld geven.",
        "But legt een tegenstelling binnen de zin.",
        "Een hotelbeoordeling is opiniërend, een recept en een bijsluiter prescriptief, een lied, een gedicht en een kortverhaal literair, en een krantenartikel en een interview informatief.",
        "Een tekst die wil overtuigen of beïnvloeden, heet persuasief.",
    ],
)


# ───────────────────────── 2. Tekstsoorten, tekstverbanden en verwijswoorden
BUNDELS["tekstsoorten-tekstverbanden-en-verwijswoorden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Tekstsoorten, tekstverbanden en verwijswoorden",
    onder="Zes soorten teksten herkennen, de signaalwoorden lezen die de gedachtegang sturen, en weten waar een voornaamwoord naar verwijst.",
    secties=[
        dict(kop="Zes soorten teksten", blokken=[
            ("p", "Het is <strong>nuttig</strong> om bij het begin te weten met welke <strong>tekstsoort</strong> "
                  "je te maken hebt, want dan weet je ook <strong>waar je de belangrijkste informatie mag "
                  "verwachten</strong>. De naam van elke soort is een <strong>vakwoord</strong> dat je zelf moet "
                  "kunnen opschrijven. In een handleiding staat "
                  "ze in de stappen, in een opiniestuk in de eerste en de laatste alinea, in een flyer in de "
                  "kleine lettertjes onderaan."),
            ("p", tabel(["Tekstsoort", "Wil vooral", "Voorbeelden"], [
                ["informatief", "informatie geven",
                 "a newspaper article, an interview, a news item on television, a leaflet with opening hours"],
                ["persuasief (een persuasieve tekst)", "overtuigen of beïnvloeden",
                 "een campagne tegen zwerfvuil, een flyer voor een sportevenement, reclame"],
                ["opiniërend (een opiniërende tekst)", "een mening geven",
                 "een hotelbeoordeling, een filmrecensie, een reactie op een forum"],
                ["prescriptief", "zeggen wat of hoe je iets moet doen",
                 "the rules of a board game, a school regulations booklet, an instruction video on YouTube, een recept, een bijsluiter"],
                ["narratief (een narratieve tekst)", "feiten en gebeurtenissen verhalend weergeeft",
                 "een reisverslag, een getuigenis van iemand die een ongeval meemaakte"],
                ["literair", "raken, met een eigen stijl",
                 "een lied, een gedicht, een kortverhaal, een cartoon, een strip"],
            ])),
            ("p", "Zes zinnetjes en zes soorten:"),
            ("p", tabel(["Zin", "Soort"], [
                ["The library will be closed from 3 to 10 August for building work.", "informatief"],
                ["Don't let your rubbish end up in the sea. Bring your plastic to the recycling point today.", "persuasief"],
                ["In my view, the new bus timetable makes life harder for everyone who works early shifts.", "opiniërend"],
                ["Turn the device off, wait ten seconds and press the red button twice.", "prescriptief"],
                ["That morning I missed my train, lost my umbrella and arrived soaking wet.", "narratief"],
                ["The city slept, and the river carried the moon away on its back.", "literair"],
            ])),
            ("kader", "Eén tekst kan kenmerken van <strong>meer dan één tekstsoort</strong> hebben. <em>Best film "
                      "I have seen all year. Go and watch it.</em> doet twee dingen: <strong>een mening "
                      "geven</strong> en <strong>de lezer overtuigen</strong>. Je kijkt dan naar het hoofddoel."),
        ]),
        dict(kop="Waaraan je een soort herkent", blokken=[
            ("p", "Zie je een <strong>titel, een ondertitel, tussenkopjes en een foto met bijschrift</strong>, "
                  "dan heb je waarschijnlijk een <strong>krantenartikel</strong> voor je. Een "
                  "<strong>literaire</strong> tekst herken je aan <strong>beeldspraak, ritme of een bijzondere "
                  "stijl</strong>: een rivier die de maan op haar rug meedraagt, komt in geen enkel "
                  "nieuwsbericht voor."),
            ("p", "Een <strong>persuasieve</strong> tekst geeft <strong>niet altijd eerlijk alle "
                  "informatie</strong>. Dat is geen fout van die tekst, het hoort bij zijn doel. Krijg je een "
                  "<strong>flyer voor een sportevenement</strong>, let dan vooral op <strong>wat de flyer van je "
                  "wil en welke gegevens hij geeft</strong>: datum, plaats, prijs, en wat er niet bij staat."),
            ("p", "Twee valstrikken. Een <strong>bijsluiter</strong> bij een geneesmiddel is géén informatieve "
                  "tekst maar een <strong>prescriptieve</strong>: hij zegt wat je moet doen en laten. En een "
                  "<strong>cartoon</strong> en een <strong>strip</strong> horen wél bij de "
                  "<strong>literaire</strong> teksten, samen met een lied, een gedicht en een kortverhaal. "
                  "Literatuur zit niet alleen in romans."),
        ]),
        dict(kop="Tekstverbanden en hun signaalwoorden", blokken=[
            ("p", "Zinnen staan niet los van elkaar. Kleine woordjes, de <strong>signaalwoorden</strong>, zeggen "
                  "welk <strong>verband</strong> er tussen twee zinnen ligt. Ze staan er niet om een tekst mooier "
                  "te laten klinken: wie ze leest, leest de gedachtegang."),
            ("p", tabel(["Verband", "Signaalwoorden", "Voorbeeld"], [
                ["een oorzaak", "because, as, since",
                 "The match was cancelled <strong>because</strong> the pitch was under water."],
                ["een gevolg", "so, therefore, as a result",
                 "The pitch was under water, <strong>so</strong> the match was cancelled."],
                ["een tegenstelling", "however, although, on the other hand, despite, yet, in fact",
                 "Tickets are expensive. <strong>However</strong>, the concert is worth every penny."],
                ["een voorbeeld", "for instance, for example",
                 "Many animals are losing their homes. <strong>For instance</strong>, hedgehogs can no longer cross our gardens."],
                ["er komt nog iets bij", "in addition, moreover, besides",
                 "The film was long. <strong>In addition</strong>, the sound was terrible."],
                ["vergelijken en het verschil aanduiden", "unlike, compared with",
                 "<strong>Unlike</strong> Spain, Ireland has cool summers."],
            ])),
            ("p", "<strong>Although</strong> en <strong>but</strong> leggen allebei een tegenstelling, maar ze "
                  "staan <strong>niet op dezelfde plaats in de zin</strong>. <em>Although</em> opent een bijzin "
                  "en kan vooraan: <em>Although it rained, we went out.</em> <em>But</em> staat tussen twee "
                  "hoofdzinnen: <em>It rained, but we went out.</em> Samen in één zin zet je ze niet."),
            ("p", "<strong>Despite</strong> doet hetzelfde werk, maar er volgt geen zin op, wel een naamwoord of "
                  "een -ing-vorm: <em>Despite the rain, the festival went ahead.</em> Dat is dus ook een "
                  "tegenstelling."),
            ("kader", "<strong>Therefore</strong> en <strong>however</strong> kan je niet zomaar verwisselen. "
                      "Er is wel degelijk een <strong>betekenisverschil</strong>: therefore kondigt een "
                      "<strong>gevolg</strong> aan, however een <strong>tegenstelling</strong>. Eén woord "
                      "verwisselen draait de hele redenering om."),
            ("p", "Weerlegt alinea 2 wat alinea 1 beweert, dan zie je dat meestal aan de <strong>eerste woorden "
                  "van die alinea</strong>: <em>however</em>, <em>in fact</em> of <em>yet</em>."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", "Een <strong>voornaamwoord</strong> verwijst naar iets dat eerder genoemd is. Weet je niet "
                  "waarnaar, dan <strong>mis je de samenhang tussen de zinnen</strong>, ook al begrijp je elk "
                  "woord apart."),
            ("p", tabel(["Zin", "Waar het verwijswoord naar verwijst"], [
                ["My brother works in Dublin. <strong>He</strong> comes home twice a year.", "de broer"],
                ["The council closed two swimming pools last year. <strong>This</strong> made a lot of people angry.",
                 "naar het sluiten van de twee zwembaden"],
                ["Sara gave Nora her keys.", "volgens de gewone lezing: die van Sara"],
            ])),
            ("p", "Terugverwijzen kan met meer dan alleen <em>he</em> en <em>she</em>. Ook "
                  "<strong>they</strong>, <strong>these</strong> en een groepje als <strong>such a "
                  "problem</strong> pakken iets op dat eerder in de tekst stond. En <strong>it</strong> kan "
                  "verwijzen naar een voorwerp, maar net zo goed naar een <strong>hele zin</strong>: "
                  "<em>The train was late again. It happens every week.</em>"),
            ("weetje", "<em>Sara gave Nora her keys</em> is strikt genomen dubbelzinnig, maar de gewone lezing is "
                       "op de vraag wiens sleutels het zijn, dat het Sara's sleutels zijn: het voornaamwoord "
                       "pakt meestal het onderwerp van de zin op. "
                       "Wil je het zeker maken, dan herhaal je de naam."),
        ]),
        luister("luister naar een Engelstalige podcast van tien minuten over iets wat je toch al interesseert, "
                "en let op de signaalwoorden: hoor je however, so of for instance?"),
    ],
    onthoud=[
        "Zes tekstsoorten: informatief, persuasief, opiniërend, prescriptief, narratief en literair.",
        "Eén tekst kan kenmerken van meer dan één tekstsoort hebben. Kijk naar het hoofddoel.",
        "Weet je de tekstsoort, dan weet je waar de belangrijkste informatie staat.",
        "Een krantenartikel, een interview en een nieuwsitem op tv zijn informatief.",
        "De spelregels van een gezelschapsspel, een schoolreglement, een instructievideo, een recept en een bijsluiter zijn prescriptief.",
        "Een cartoon en een strip horen bij de literaire teksten.",
        "Een getuigenis van iemand die een ongeval meemaakte, is narratief.",
        "Een persuasieve tekst geeft niet altijd eerlijk alle informatie.",
        "Because geeft een oorzaak, so een gevolg, however een tegenstelling.",
        "Tegenstelling: however, although, on the other hand, despite, yet, in fact. Gevolg: therefore, as a result, so.",
        "For instance geeft een voorbeeld, in addition voegt iets toe, unlike vergelijkt en wijst op het verschil.",
        "Although en but leggen allebei een tegenstelling, maar staan niet op dezelfde plaats in de zin.",
        "Therefore en however kan je niet verwisselen: het ene is een gevolg, het andere een tegenstelling.",
        "Een voornaamwoord verwijst terug. Weet je niet waarnaar, dan mis je de samenhang tussen de zinnen.",
        "It kan verwijzen naar een voorwerp, maar ook naar een hele zin.",
    ],
)


# ───────────────────────── 3. De Engelstalige wereld: gewoontes en conventies
BUNDELS["de-engelstalige-wereld-gewoontes-en-conventies-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De Engelstalige wereld: gewoontes en conventies",
    onder="Waar Engels gesproken wordt, waarin Brits en Amerikaans Engels verschillen, en hoe je beleefd blijft in een brief of een gesprek.",
    secties=[
        dict(kop="Waar Engels gesproken wordt", blokken=[
            ("p", "Het <strong>Verenigd Koninkrijk</strong> bestaat uit vier landsdelen: "
                  "<strong>England, Scotland, Wales en Northern Ireland</strong>. De Republiek Ierland hoort er "
                  "niet bij, dat is een apart land. En <strong>England</strong> en <strong>Great "
                  "Britain</strong> betekenen niet hetzelfde: Great Britain is het eiland waarop England, "
                  "Scotland en Wales liggen."),
            ("p", "Engels is de officiële of voornaamste voertaal in veel meer landen: "
                  "<strong>Australia</strong>, <strong>New Zealand</strong>, <strong>Canada</strong> (naast het "
                  "Frans), de Verenigde Staten en Ierland. Ook in <strong>India</strong> en in <strong>Zuid-"
                  "Afrika</strong> is Engels een officiële taal. In Brazilië niet: daar spreekt men Portugees."),
            ("weetje", "Meer mensen spreken Engels als tweede taal dan als moedertaal. Daarom kom je op het "
                       "examen ook teksten tegen die niet uit Londen of New York komen."),
        ]),
        dict(kop="Brits en Amerikaans Engels", blokken=[
            ("p", "Dezelfde taal, twee woordenlijsten. Je moet de varianten <strong>herkennen</strong>, en in je "
                  "eigen tekst <strong>consequent</strong> blijven."),
            ("p", tabel(["Brits", "Amerikaans", "Nederlands"], [
                ["lift", "elevator", "lift"],
                ["flat", "apartment", "appartement"],
                ["holiday", "vacation", "vakantie"],
                ["lorry", "truck", "vrachtwagen"],
                ["petrol", "gas", "benzine"],
                ["autumn", "fall", "herfst"],
                ["chips", "fries", "frieten"],
                ["crisps", "chips", "chips uit een zakje"],
            ])),
            ("p", "Ook de <strong>spelling</strong> loopt uiteen. Een Brit schrijft <strong>colour</strong>, "
                  "<strong>favourite</strong> en <strong>centre</strong>; een Amerikaan schrijft "
                  "<strong>color</strong>, <strong>favorite</strong> en <strong>center</strong>. Zo ook "
                  "<em>travelled</em> tegenover <em>traveled</em> en <em>organise</em> tegenover "
                  "<em>organize</em>."),
            ("kader", "Op een examen mag je Brits en Amerikaans Engels <strong>niet</strong> door elkaar "
                      "gebruiken, ook al is elk woord op zich juist gespeld. Kies één variant en hou die vol in "
                      "je hele tekst. Door elkaar gebruiken leest als slordigheid."),
            ("p", "De taalvariant hoort ook bij het <strong>begrijpen</strong> van een tekst, en niet alleen bij "
                  "het schrijven: <strong>hetzelfde woord kan in de VS iets anders betekenen dan in het "
                  "VK</strong>. Zegt een Brit <em>chips</em>, dan bedoelt hij <strong>frieten</strong>. En "
                  "<strong>football</strong> betekent in de Verenigde Staten <em>niet</em> hetzelfde als bij "
                  "ons: daar is het American football, en ons voetbal heet <em>soccer</em>."),
        ]),
        dict(kop="Verdiepingen, datums, maten en temperaturen", blokken=[
            ("p", "In het Verenigd Koninkrijk is <strong>the ground floor</strong> het "
                  "<strong>gelijkvloers</strong>, en de first floor is de eerste verdieping. In de Verenigde "
                  "Staten is de first floor wél het gelijkvloers. In een lift scheelt dat een verdieping."),
            ("p", "Een Britse brief die <strong>5/3/2027</strong> vermeldt, bedoelt <strong>5 maart "
                  "2027</strong>: eerst de dag, dan de maand. In de Verenigde Staten is diezelfde notatie 3 mei. "
                  "Wil je geen misverstand, schrijf dan de maand voluit."),
            ("p", "Deze <strong>maateenheden</strong> kom je in het Verenigd Koninkrijk en de Verenigde Staten nog vaak tegen:"),
            ("p", tabel(["Eenheid", "Waarvoor", "Ongeveer"], [
                ["miles", "afstand", "1 mile is 1,6 km"],
                ["pounds", "gewicht en geld", "1 pound is 0,45 kg"],
                ["pints", "inhoud", "1 pint is ruim een halve liter"],
                ["Fahrenheit", "temperatuur in de VS", "100 °F is ongeveer 38 °C"],
            ])),
            ("p", "In de <strong>Verenigde Staten</strong> wordt de <strong>temperatuur</strong> meestal in "
                  "<strong>Fahrenheit</strong> gegeven. Staat er in een tekst <em>it was 90 degrees</em>, dan is "
                  "dat geen onmogelijke hittegolf maar een warme zomerdag."),
        ]),
        dict(kop="Beleefd blijven op papier", blokken=[
            ("p", "Ken je de <strong>ontvanger</strong> niet, bijvoorbeeld bij een mail aan een "
                  "medewerker van een school of een bedrijf, dan begin je met <strong>Dear Sir or Madam,</strong> Na <strong>Dear</strong> hoort "
                  "altijd een naam of een aanspreking: <em>Dear</em> alleen bestaat niet."),
            ("p", tabel(["Situatie", "Aanhef", "Afsluiter"], [
                ["je kent de naam niet", "Dear Sir or Madam,", "Yours faithfully,"],
                ["je kent de naam wel", "Dear Mr Smith, / Dear Ms Taylor,", "Yours sincerely,"],
                ["een vriend of leeftijdsgenoot", "Hi Sam, / Hello Lise,", "Best wishes, / See you soon, / Take care,"],
            ])),
            ("p", "Voor een vrouw van wie je <strong>niet weet of ze getrouwd is</strong>, gebruik je "
                  "<strong>Ms</strong>. Mrs is voor een getrouwde vrouw, Miss voor een ongetrouwde, en die twee "
                  "raden aan te vermijden als je het niet zeker weet."),
            ("kader", "<strong>Yours sincerely</strong> gebruik je als je de <strong>naam van je lezer "
                      "kent</strong>, <strong>Yours faithfully</strong> als je die <strong>niet kent</strong>. "
                      "Ze horen vast bij hun aanhef: Dear Sir or Madam gaat met Yours faithfully, Dear Mr Smith "
                      "met Yours sincerely."),
            ("p", tabel(["Wat je wil", "Hoe je het zegt"], [
                ["beleefd om informatie vragen", "Could you tell me when the course starts?"],
                ["je mening geven", "In my opinion, … / As far as I'm concerned, … / I would say that …"],
                ["je verontschuldigen", "I'm really sorry about the delay."],
                ["reageren op een verontschuldiging", "That's all right, don't worry."],
            ])),
            ("p", "Het Engels gebruikt <strong>please</strong> en <strong>thank you</strong> veel "
                  "<strong>vaker</strong> dan wij <em>alsjeblieft</em> en <em>dankjewel</em>. Even vaak is dus "
                  "niet genoeg: te weinig klinkt in het Engels snel bot, ook als je het niet zo bedoelt."),
            ("p", "Een gepast <strong>register</strong> gebruiken betekent dat je <strong>je toon afstemt op wie "
                  "je aanspreekt</strong>. Aan een directeur schrijf je anders dan aan een vriend. "
                  "<strong>Scheldwoorden</strong> horen in geen enkele examenopdracht thuis, ook niet als ze bij "
                  "de situatie zouden passen."),
        ]),
        dict(kop="Gewoontes, feesten en lichaamstaal", blokken=[
            ("p", "In de <strong>Verenigde Staten</strong> spreken mensen elkaar vaak snel met de "
                  "<strong>voornaam</strong> aan. Twijfel je, dan <strong>begin je formeel en volg je wat de "
                  "ander doet</strong>: Mr of Ms, en schakel over zodra hij of zij dat doet."),
            ("p", "Deze feesten worden <strong>gevierd</strong> in de Engelstalige wereld:"),
            ("p", tabel(["Feest", "Wanneer", "Waar vooral"], [
                ["Thanksgiving", "vierde donderdag van november", "Verenigde Staten"],
                ["Independence Day", "4 juli", "Verenigde Staten"],
                ["Halloween", "31 oktober", "Verenigde Staten, en intussen breder"],
                ["St Patrick's Day", "17 maart", "Ierland, en overal waar Ieren wonen"],
            ])),
            ("p", "In een <strong>restaurant in de Verenigde Staten</strong> is het gebruikelijk om "
                  "<strong>fooi</strong> te geven; het bedienend personeel rekent erop. In het Verenigd "
                  "Koninkrijk is het minder vanzelfsprekend."),
            ("p", "Lees je in een Britse tekst <em>Join the queue, please</em>, dan moet je "
                  "<strong>achteraan in de rij gaan staan</strong>. <em>To queue</em> is aanschuiven, en het is "
                  "in het Verenigd Koninkrijk een van de gevoeligste sociale regels die er zijn."),
            ("p", "<strong>Lichaamstaal</strong> hoort bij dit vak omdat ze bij de <strong>gewoontes</strong> "
                  "hoort die je in een tekst moet kunnen herkennen: een hand geven, afstand houden, iemand "
                  "aankijken."),
            ("kader", "Krijg je een tekst over <strong>eetgewoonten in het Verenigd Koninkrijk</strong>, of lees "
                      "je dat mensen ergens elkaar bij een eerste ontmoeting een hand geven, dan mag je daaruit "
                      "besluiten <strong>wat die tekst beschrijft, en niet meer dan dat</strong>. Je "
                      "<strong>onthoudt het als een gewoonte die de tekst beschrijft</strong>. Een tekst kan je "
                      "iets over een land vertellen, maar een volk heeft geen karakter."),
        ]),
        luister("zet de taalinstelling van één app of van je telefoon een week op Engels, en let op de woorden "
                "die je dan tegenkomt: staat er colour of color?"),
    ],
    onthoud=[
        "Het Verenigd Koninkrijk bestaat uit England, Scotland, Wales en Northern Ireland. England is niet hetzelfde als Great Britain.",
        "Engels is ook de voornaamste taal in Australia, New Zealand en Canada, en een officiële taal in India en Zuid-Afrika.",
        "Brits lift, flat, holiday, lorry, petrol, autumn, chips. Amerikaans elevator, apartment, vacation, truck, gas, fall, fries.",
        "Brits colour en centre, Amerikaans color en center. Meng de twee varianten nooit in één tekst.",
        "Football betekent in de VS American football; ons voetbal heet daar soccer.",
        "The ground floor is in het VK het gelijkvloers. 5/3/2027 is in een Britse brief 5 maart 2027.",
        "Miles, pounds en pints kom je nog vaak tegen, en in de VS wordt de temperatuur in Fahrenheit gegeven.",
        "Dear Sir or Madam gaat met Yours faithfully, Dear Mr Smith met Yours sincerely.",
        "Ms gebruik je voor een vrouw van wie je niet weet of ze getrouwd is.",
        "Please en thank you gebruik je in het Engels vaker dan bij ons.",
        "Een gepast register betekent dat je je toon afstemt op wie je aanspreekt. Scheldwoorden nooit.",
        "Twijfel je over voornaam of achternaam, begin dan formeel en volg wat de ander doet.",
        "Thanksgiving en Independence Day (4 juli) horen bij de VS, St Patrick's Day (17 maart) bij Ierland.",
        "Join the queue betekent achteraan aansluiten.",
        "Uit een tekst over gewoontes besluit je wat die tekst beschrijft, en niet meer dan dat.",
    ],
)


# ───────────────────────── 4. Schrijven, schriftelijke interactie en literatuurbeleving
BUNDELS["schrijven-schriftelijke-interactie-en-literatuurbeleving-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Schrijven, schriftelijke interactie en literatuurbeleving",
    onder="De zes schrijfopdrachten, waarop je tekst beoordeeld wordt, wat je doet als je vastzit, en hoe je over een verhaal of gedicht schrijft.",
    secties=[
        dict(kop="Wat je moet kunnen schrijven", blokken=[
            ("p", "Schrijven en schriftelijke interactie wegen samen <strong>58 %</strong> van het examen Engels "
                  "2. De opdrachten komen telkens op hetzelfde neer: je krijgt een situatie, en je moet er een "
                  "tekst bij schrijven die <strong>iets doet</strong>. Deze zes komen het vaakst terug."),
            ("p", tabel(["Opdracht", "Voorbeeld", "Voorbeeldzin"], [
                ["iets vertellen", "een verslag over een uitstap, of wat je op een concert meemaakte",
                 "The concert was amazing. We got there early and stood right at the front."],
                ["iets uitleggen", "aan een vriend uitleggen hoe je een gerecht klaarmaakt",
                 "First you boil the pasta, then you add the sauce."],
                ["iemand proberen te overtuigen", "een vriend meekrijgen naar een activiteit",
                 "You really should join us, it will be so much fun."],
                ["informatie vragen", "je inschrijven voor een taalstage",
                 "I would like to know how I can register for the course."],
                ["je mening of standpunt geven", "reageren op een probleem op school",
                 "I think the school should open the library at lunchtime."],
                ["informatie geven", "iemand de praktische gegevens doorsturen",
                 "The bus leaves at half past seven from the station."],
            ])),
            ("kader", "<strong>Je mening geven</strong> en <strong>informatie geven</strong> zijn twee "
                      "<strong>verschillende</strong> schrijfopdrachten. Wie een mening moet geven en alleen "
                      "feiten opsomt, heeft de opdracht niet uitgevoerd, hoe correct het Engels ook is."),
            ("p", "Een <strong>formele mail</strong> open je met een zin die meteen zegt waarom je schrijft: "
                  "<em>I am writing to ask about …</em> Dat is een gepaste openingszin. Een "
                  "<strong>informeel bericht</strong> aan een leeftijdsgenoot begint gewoon met <em>Hi Sam, how "
                  "are things?</em>"),
        ]),
        dict(kop="Alledaagse sociale contacten", blokken=[
            ("p", "Een deel van de opdrachten gaat niet over informatie maar over <strong>contact</strong>: "
                  "iemand uitnodigen, bedanken, belangstelling tonen, je verontschuldigen, en ook een "
                  "uitnodiging <strong>afslaan</strong>. Dat laatste hoort er wel degelijk bij, en het is in een "
                  "vreemde taal een van de moeilijkste dingen die er zijn."),
            ("p", tabel(["Wat je doet", "Wat je schrijft"], [
                ["uitnodigen", "Would you like to come along on Saturday? / Would you like to <strong>join</strong> us on Saturday?"],
                ["belangstelling tonen", "How are you doing? / How was your trip? / Are you feeling better now?"],
                ["contact houden", "How have you been? / It was lovely to see you again."],
                ["bedanken", "Thanks so much for having me. / Thank you so much, I had a wonderful time."],
                ["je verontschuldigen, met een reden", "Sorry I missed your call, I was on the train."],
                ["beleefd weigeren", "I'd love to, but I'm afraid I can't."],
            ])),
            ("weetje", "<em>To join</em> is het werkwoord waarmee je iemand uitnodigt om mee te doen: "
                       "<em>Would you like to join us on Saturday?</em> Het betekent zowel meedoen als lid "
                       "worden."),
            ("p", "<strong>Schriftelijke interactie</strong> is iets anders dan gewoon een tekst schrijven. Je "
                  "schrijft een <strong>reactie op een bericht</strong>, en dus <strong>moet je reageren op wat "
                  "er in dat bericht staat</strong>. De vragen van je correspondent <strong>onbeantwoord "
                  "laten</strong> mag niet, ook niet als je tekst verder volledig is. Dat is precies wat "
                  "interactie betekent."),
        ]),
        dict(kop="Waarop je tekst beoordeeld wordt", blokken=[
            ("p", "Er zijn <strong>zeven dingen</strong> waarop je schrijfopdracht beoordeeld wordt. Ze staan "
                  "niet in volgorde van belang, maar <strong>taakvoltooiing</strong> haalt de meeste punten "
                  "onderuit als ze mislukt."),
            ("p", tabel(["Wat", "Wat er gevraagd wordt"], [
                ["taakvoltooiing", "je boodschap komt over en je opdracht is volledig uitgevoerd"],
                ["tekststructuur en samenhang", "een inleiding, een midden en een slot, met verbindende woorden"],
                ["woordenschat", "genoeg woorden, en de juiste voor de situatie"],
                ["grammatica", "correcte zinnen, al mogen er nog fouten in staan"],
                ["spelling", "fouten tellen mee als ze het begrip in de weg staan"],
                ["register", "je toon past bij wie je aanspreekt"],
                ["tekstopbouw en lay-out", "een titel en duidelijke alinea's"],
            ])),
            ("p", "Een tekst met een <strong>herkenbare structuur</strong> heeft drie delen: <strong>een "
                  "inleiding</strong>, <strong>een midden</strong> en <strong>een slot</strong>. De samenhang "
                  "maak je zichtbaar met woorden als <strong>first</strong>, <strong>however</strong> en "
                  "<strong>finally</strong>."),
            ("p", "Er <strong>mogen</strong> nog <strong>grammaticafouten</strong> in je tekst staan: op "
                  "B1-niveau wordt geen foutloos Engels verwacht, wel Engels dat overkomt. Hetzelfde geldt voor "
                  "<strong>spelfouten</strong>: die tellen <strong>alleen mee als ze het begrip van je tekst in "
                  "de weg staan</strong>."),
            ("p", "<em>Je vormt af en toe samengestelde zinnen</em> betekent dat je <strong>niet enkel korte "
                  "hoofdzinnen</strong> schrijft. Af en toe een bijzin met <em>because</em>, <em>although</em> "
                  "of <em>which</em> laat zien dat je verbanden kan leggen."),
            ("kader", "Krijg je een opdracht van <strong>120 tot 150 woorden</strong> en schrijf je er "
                      "<strong>70</strong>, dan <strong>verlies je punten op taakvoltooiing</strong>. Te kort "
                      "betekent bijna altijd: niet alles behandeld. En de <strong>fout die je het meest "
                      "kost</strong> bij taakvoltooiing is <strong>één van de drie gevraagde punten niet "
                      "behandelen</strong>."),
            ("p", "Wat je precies vertelt, mag je <strong>zelf verzinnen</strong>, zolang je de opdracht "
                  "uitvoert. Niemand controleert of je echt op dat concert was."),
        ]),
        dict(kop="Voorbereiden, en wat je doet als je vastzit", blokken=[
            ("p", "Voor je begint te schrijven, stel je jezelf de vragen van het "
                  "<strong>communicatiemodel</strong>: <strong>waarom schrijf ik?</strong>, <strong>voor wie is "
                  "mijn boodschap?</strong>, <strong>welk kanaal gebruik ik?</strong> en wat wil ik precies "
                  "vertellen. Dat kost een halve minuut en bepaalt je hele toon."),
            ("p", "Daarna maak je een <strong>schrijfplan met kernwoorden</strong>: <strong>een lijstje van wat "
                  "je in welke volgorde wil zeggen</strong>. Vijf woorden op je kladblad volstaan, en ze houden "
                  "je tekst op koers."),
            ("p", "Zit je <strong>vast</strong> bij het schrijven, dan stop je <strong>niet</strong> met die zin "
                  "om aan een andere opdracht te beginnen. Je probeert je doel te bereiken met de woorden en "
                  "structuren die je <strong>wél</strong> al kent. Ken je het woord <em>crutches</em> niet, dan "
                  "<strong>omschrijf je het</strong>: <em>the sticks you walk with after you break a leg</em>. "
                  "Dat is geen noodoplossing, dat is een strategie."),
            ("p", "Je mag een <strong>online woordenboek en spellingcontrole</strong> gebruiken. Die zijn "
                  "bedoeld <strong>om te controleren en een enkel woord op te zoeken</strong>, niet om je tekst "
                  "te schrijven. Hou je nog <strong>vijf minuten</strong> over, dan is <strong>je tekst nalezen op "
                  "werkwoordsvormen en leestekens</strong> het beste wat je kan doen: daar zitten de punten die je zonder extra "
                  "kennis nog kan rapen."),
        ]),
        dict(kop="Literatuurbeleving", blokken=[
            ("p", "<strong>Literatuurbeleving</strong> weegt bij Engels 2 <strong>4 %</strong>. Dat is minder "
                  "dan schrijven (29 %), maar het is wel het enige onderdeel waar geen fout antwoord bestaat, "
                  "zolang je je mening <strong>onderbouwt met de tekst</strong>."),
            ("p", "Lees je een gedicht of een verhaal en moet je je <strong>eigen beleving verwoorden</strong>, "
                  "dan schrijf je <strong>waarom bepaalde beelden je raken en wat ze bij je oproepen</strong>. "
                  "Je mag ook schrijven <strong>waarom je je met een personage identificeert</strong>, "
                  "<strong>of je zelf al iets gelijkaardigs meemaakte</strong> en <strong>waarom de stijl of de "
                  "vorm je aanspreekt</strong>."),
            ("p", tabel(["Dit is een leeservaring", "Dit is een samenvatting"], [
                ["The ending made me feel uncomfortable.", "The main character leaves the village."],
                ["I recognised myself in the younger sister.", "The story is set in Ireland in 1950."],
                ["The short sentences made me read faster.", "The book has twelve chapters."],
            ])),
            ("kader", "Verkoopcijfers, prijzen en wat anderen van het boek vinden, zeggen niets over "
                      "<strong>jouw</strong> beleving. Schrijf over wat de tekst met <strong>jou</strong> deed, "
                      "en toon in de tekst zelf waar dat vandaan komt."),
        ]),
        luister("vertel aan iemand thuis in het Engels wat je dit weekend gedaan hebt, in vijf zinnen. "
                "Hakkel gerust, en omschrijf de woorden die je niet vindt."),
    ],
    onthoud=[
        "Zes schrijfopdrachten: iets vertellen, iets uitleggen, overtuigen, informatie vragen, je mening geven en informatie geven.",
        "Je mening geven en informatie geven zijn twee verschillende opdrachten.",
        "I am writing to ask about … opent een formele mail; Hi Sam, how are things? een informeel bericht.",
        "Would you like to join us on Saturday? nodigt uit. Een uitnodiging afslaan hoort er ook bij.",
        "Bij schriftelijke interactie moet je reageren op wat er in het bericht staat, en alle vragen beantwoorden.",
        "Zeven beoordelingspunten, met taakvoltooiing voorop: je boodschap komt over en je opdracht is volledig uitgevoerd.",
        "Een tekst met structuur heeft een inleiding, een midden en een slot, met first, however en finally.",
        "Grammaticafouten mogen nog. Spelfouten tellen mee als ze het begrip in de weg staan.",
        "Samengestelde zinnen vormen betekent: niet enkel korte hoofdzinnen schrijven.",
        "Te weinig woorden schrijven kost punten op taakvoltooiing. Eén van de drie gevraagde punten niet behandelen kost het meest.",
        "Wat je vertelt, mag je zelf verzinnen, zolang je de opdracht uitvoert.",
        "Vooraf: waarom schrijf ik, voor wie, welk kanaal. Daarna een schrijfplan met kernwoorden.",
        "Zit je vast, stop dan niet, maar omschrijf: the sticks you walk with after you break a leg.",
        "Woordenboek en spellingcontrole zijn om te controleren en een enkel woord op te zoeken.",
        "Bij literatuurbeleving bestaat geen fout antwoord, zolang je je mening met de tekst onderbouwt. Ze weegt 4 %, schrijven 29 %.",
    ],
)


# ───────────────────────── 5. Woordvelden: mensen, gezondheid en het dagelijkse leven
BUNDELS["woordvelden-mensen-gezondheid-en-het-dagelijkse-leven-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: mensen, gezondheid en het dagelijkse leven",
    onder="Familie, persoonlijke gegevens, gevoelens, het lichaam, eten, kleren, wonen en de dagelijkse bezigheden.",
    secties=[
        dict(kop="Familie", blokken=[
            ("p", "Het Nederlands heeft één woord <em>neef</em> en één woord <em>nicht</em>, het Engels heeft er "
                  "twee. Daar gaat het bijna altijd mis."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>nephew</strong>", "de zoon van je broer of je zus"],
                ["<strong>niece</strong>", "de dochter van je broer of je zus"],
                ["<strong>cousin</strong>", "het kind van je oom of je tante"],
                ["<strong>uncle</strong> / <strong>aunt</strong>", "de broer van je vader of je moeder / de zus"],
                ["<strong>grandson</strong> / granddaughter", "de kleinzoon / de kleindochter"],
                ["mother-in-law, brother-in-law", "familie die je door je huwelijk krijgt: schoonmoeder, schoonbroer"],
                ["stepmother, stepfather", "een stiefouder, die je krijgt door het huwelijk van een ouder"],
                ["great-aunt", "de tante van je vader of moeder"],
            ])),
            ("kader", "<strong>Nephew</strong> gebruik je <strong>niet</strong> voor de zoon van je oom of je "
                      "tante: dat is je <strong>cousin</strong>. En cousin dekt in het Engels zowel een neef als "
                      "een nicht."),
        ]),
        dict(kop="Persoonlijke gegevens", blokken=[
            ("p", "Op een Engels formulier staan altijd dezelfde velden. In het Engels staat de "
                  "<strong>voornaam eerst</strong>."),
            ("p", tabel(["Veld", "Wat je invult"], [
                ["first name", "je voornaam"],
                ["<strong>surname</strong> (of last name)", "je achternaam of familienaam"],
                ["<strong>date of birth</strong>", "je geboortedatum"],
                ["place of birth", "je geboorteplaats"],
                ["<strong>marital status</strong>", "je burgerlijke staat: single, married, divorced"],
                ["occupation", "je beroep"],
                ["nationality", "je nationaliteit"],
            ])),
            ("p", "<strong>Nationaliteiten</strong> en talen schrijf je in het Engels <strong>met een "
                  "hoofdletter</strong>: <em>he is Belgian</em>, <em>I speak English</em>. Het Nederlands doet "
                  "dat niet, en die gewoonte sleept iedereen mee."),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("p", tabel(["Blij", "Verdrietig of somber", "Bang of zenuwachtig", "Boos"], [
                ["cheerful, joyful, merry, lively, <strong>delighted</strong>",
                 "sad, <strong>gloomy</strong>, miserable, <strong>disappointed</strong> (teleurgesteld)",
                 "<strong>nervous</strong>, <strong>anxious</strong>, <strong>scared</strong>, worried",
                 "angry, annoyed, furious"],
            ])),
            ("p", "<strong>Cheerful</strong> is opgewekt; het tegenovergestelde is <strong>gloomy</strong>. "
                  "<strong>Delighted</strong> betekent heel blij, en hoort dus niet bij de angst. En let op de "
                  "spelling van <strong>disappointed</strong>: twee keer een p, één keer een s."),
            ("p", "De zin <em>I feel sick</em> zegt dat je je <strong>misselijk of ziek</strong> voelt. Wil je "
                  "zeggen dat je iemand beu bent, dan heb je <em>I'm sick <strong>of</strong> him</em> nodig: "
                  "het voorzetsel maakt het verschil."),
        ]),
        dict(kop="Gezondheid en lichaamsdelen", blokken=[
            ("p", tabel(["Arm", "Been", "Hoofd en romp"], [
                ["<strong>elbow</strong> (elleboog), <strong>wrist</strong> (pols), <strong>shoulder</strong> (schouder), hand, finger",
                 "<strong>knee</strong> (knie), <strong>ankle</strong> (enkel), <strong>hip</strong> (heup), foot, toe",
                 "<strong>neck</strong> (hals, nek), throat (keel), chest, back, stomach"],
            ])),
            ("p", "Het Engelse woord <strong>arm</strong> betekent alleen het lichaamsdeel. Voor arm in de zin "
                  "van weinig geld hebben, zeg je <strong>poor</strong>."),
            ("p", tabel(["Klacht", "Engels"], [
                ["keelpijn", "I have a <strong>sore throat</strong>"],
                ["hoofdpijn", "I have a headache"],
                ["buikpijn", "I have a stomach ache"],
                ["tandpijn", "I have a toothache"],
                ["je niet lekker voelen", "I'm feeling a bit <strong>under the weather</strong>"],
            ])),
            ("p", "<strong>Under the weather</strong> is een vaste uitdrukking voor lichtjes ziek zijn. Ze heeft "
                  "niets met het weer buiten te maken."),
            ("p", "Bij de dokter is <em>What seems to be the problem?</em> de gewone openingsvraag: ze wil weten "
                  "<strong>waar je last van hebt</strong>. Medicijnen haal je in het Verenigd Koninkrijk bij de "
                  "<strong>chemist's</strong>, de <strong>apotheek</strong>; in de Verenigde Staten heet dat een "
                  "pharmacy of een drugstore."),
        ]),
        dict(kop="Eten en drinken", blokken=[
            ("p", "Op een Engelse menukaart is <strong>a starter</strong> het <strong>voorgerecht</strong>, "
                  "daarna komt the main course en tot slot dessert. In de Verenigde Staten heet het voorgerecht "
                  "an appetizer."),
            ("p", "Een klassiek Brits ontbijt bestaat onder meer uit <strong>porridge</strong> (havermout), "
                  "<strong>toast</strong> en <strong>bacon</strong>, met eggs, sausages en beans erbij. "
                  "<em>Sushi</em> hoort daar niet bij."),
            ("p", "Bestek heet samen <em>cutlery</em>: a knife, a fork en een <strong>spoon</strong>, en met die "
                  "laatste eet je soep."),
            ("weetje", "<strong>Bread</strong> is ontelbaar en krijgt dus geen meervouds-s. Je telt het met een "
                       "maatwoord: <em>a slice of bread</em>, <em>two loaves of bread</em>."),
        ]),
        dict(kop="Kleding en accessoires", blokken=[
            ("p", tabel(["Aan je voeten", "Aan je lijf", "Erbij"], [
                ["<strong>trainers</strong> (sportschoenen), <strong>boots</strong> (laarzen), <strong>socks</strong> (kousen)",
                 "<strong>jumper</strong> / <strong>sweater</strong> / <strong>pullover</strong> (trui), shirt, jacket, <strong>trousers</strong>",
                 "<strong>scarf</strong> (sjaal), <strong>gloves</strong> (handschoenen), belt, hat"],
            ])),
            ("p", "<strong>Trousers</strong> staat altijd in het <strong>meervoud</strong>: <em>these trousers "
                  "are new</em>. Zo werkt het ook bij jeans, shorts, glasses en scissors. Bedoel je er één, dan "
                  "zeg je <em>a pair of trousers</em>."),
            ("p", "<strong>Jumper</strong> is de Britse variant voor een trui, <strong>sweater</strong> de "
                  "Amerikaanse; pullover kan in allebei."),
        ]),
        dict(kop="De woning", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>cooker</strong> (Amerikaans: stove)", "het fornuis, in the <strong>kitchen</strong>"],
                ["<strong>wardrobe</strong>", "de kleerkast"],
                ["washing machine", "de wasmachine"],
                ["loft, attic", "de zolder"],
                ["desk", "het bureau"],
                ["<strong>curtain</strong>, <strong>cushion</strong>, <strong>carpet</strong>", "gordijn, sierkussen, tapijt"],
                ["<strong>ground floor</strong>", "het gelijkvloers"],
                ["first floor", "in het VK de eerste verdieping, in de VS het gelijkvloers"],
            ])),
            ("kader", "De <strong>first floor</strong> van een Brits gebouw is <strong>niet</strong> ons "
                      "gelijkvloers. Dat heet <strong>ground floor</strong>, en in een lift staat daar een G bij."),
        ]),
        dict(kop="Dagelijkse bezigheden, kleuren, vormen en materialen", blokken=[
            ("p", "In het Engels kies je bij elke klus het juiste werkwoord. Je <strong>doet</strong> de afwas, "
                  "je <strong>maakt</strong> je bed op."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>do</strong> the washing-up / <strong>do</strong> the dishes", "afwassen"],
                ["<strong>make</strong> the bed", "je bed opmaken"],
                ["<strong>hang out</strong> the washing", "de was buiten hangen"],
                ["<strong>do</strong> your homework", "je huiswerk maken (nooit make)"],
                ["sit an exam", "een examen afleggen"],
                ["<strong>washing-up liquid</strong>", "afwasmiddel (waspoeder is washing powder)"],
            ])),
            ("p", "<strong>Make</strong> gebruik je als er iets nieuws ontstaat: make a cake, make a mistake, "
                  "make a plan. <strong>Do</strong> gebruik je bij werk en klusjes."),
            ("p", tabel(["Kleuren", "Vormen", "Materialen"], [
                ["<strong>purple</strong> (paars), red, blue, green, grey",
                 "round, <strong>oval</strong>, square, <strong>narrow</strong> (smal), wide",
                 "<strong>wooden</strong> (houten), <strong>leather</strong> (leer), <strong>cotton</strong> (katoen), <strong>plastic</strong>, metal"],
            ])),
            ("p", "Een kleur zet je <strong>vóór</strong> het zelfstandig naamwoord: <em>a blue jacket</em>. En "
                  "een bijvoeglijk naamwoord krijgt nooit een meervouds-s: <em>two blue jackets</em>. "
                  "<strong>Striped</strong> betekent gestreept, en dat is geen materiaal maar een uiterlijk."),
        ]),
        luister("kijk een kookfilmpje in het Engels en probeer het gerecht daarna na te vertellen met de "
                "woorden die je gehoord hebt."),
    ],
    onthoud=[
        "Nephew en niece zijn de kinderen van je broer of zus, cousin is het kind van je oom of tante.",
        "Met -in-law bedoel je de schoonfamilie; een stiefouder is een stepmother of stepfather.",
        "Surname is je achternaam, date of birth je geboortedatum, marital status je burgerlijke staat.",
        "Nationaliteiten en talen krijgen in het Engels een hoofdletter.",
        "Cheerful tegenover gloomy. Nervous, anxious en scared horen bij angst, delighted bij blijdschap.",
        "Disappointed: twee keer p, één keer s.",
        "Elbow, wrist en shoulder horen bij de arm; knee, ankle en hip bij het been; neck is de hals.",
        "Arm betekent enkel het lichaamsdeel; weinig geld hebben is poor.",
        "I have a sore throat is keelpijn. Under the weather betekent je niet lekker voelen.",
        "Een chemist's is in het VK de apotheek.",
        "A starter is het voorgerecht. Bread is ontelbaar: two loaves of bread.",
        "Trousers, jeans en glasses staan altijd in het meervoud.",
        "Trainers, boots en socks draag je aan je voeten; een jumper of sweater is een trui.",
        "Een cooker staat in the kitchen, een wardrobe is een kleerkast, en de ground floor is het gelijkvloers.",
        "Do the washing-up en do your homework, maar make the bed. Washing-up liquid is afwasmiddel.",
        "Purple is paars; wooden, leather, cotton en plastic zijn materialen, narrow is een vorm.",
    ],
)


# ───────────────────────── 6. Woordvelden: school, werk, reizen en de samenleving
BUNDELS["woordvelden-school-werk-reizen-en-de-samenleving-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: school, werk, reizen en de samenleving",
    onder="Het schoolleven, de opdrachtwoorden van een examen, beroepen en werk, en alles wat je onderweg, in een winkel of op je scherm tegenkomt.",
    secties=[
        dict(kop="Onderwijs en vorming", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>primary school</strong>", "de lagere school, ongeveer vier tot elf jaar"],
                ["<strong>secondary school</strong>", "het middelbaar"],
                ["nursery", "de opvang voor de allerkleinsten"],
                ["<strong>college</strong>", "in het VK een school na je zestiende, in de VS de universiteit"],
                ["<strong>headteacher</strong> (VS: principal)", "de directeur"],
                ["pupil, student", "de leerling"],
                ["<strong>timetable</strong>", "het lessenrooster"],
                ["<strong>subject</strong>", "een vak"],
                ["<strong>term</strong>", "een trimester"],
                ["classroom", "het klaslokaal"],
            ])),
            ("p", "Rond het examen: je <strong>sit an exam</strong>, en daarna <strong>pass</strong> je (je bent "
                  "<strong>geslaagd</strong>) of <strong>fail</strong> je (je bent gebuisd). Moet je het "
                  "overdoen, dan <strong>resit</strong> je het. Ben je er niet, dan ben je <em>absent</em>."),
            ("kader", "Het Engelse <strong>college</strong> betekent <strong>niet</strong> hetzelfde als ons "
                      "woord college. Een les bij ons heet in het Engels <em>a lesson</em> of <em>a "
                      "class</em>."),
        ]),
        dict(kop="Instructietaal: de woorden van de opdracht", blokken=[
            ("p", "De opdracht zelf staat in het Engels. Lees ze twee keer: het verschil tussen aanduiden en "
                  "zelf schrijven zit in één werkwoord."),
            ("p", tabel(["Opdracht", "Wat je moet doen"], [
                ["<strong>Tick</strong> the correct box.", "het juiste vakje aankruisen"],
                ["<strong>Underline</strong> the answer.", "het juiste woord onderlijnen"],
                ["<strong>Circle</strong> the odd one out.", "het juiste woord omcirkelen"],
                ["<strong>Match</strong> the words with the pictures.", "elk woord verbinden met de juiste afbeelding"],
                ["<strong>Fill in the gaps.</strong>", "de gaten in de tekst invullen (ook: complete the sentences)"],
                ["<strong>Summarise</strong> the text.", "samenvatten, dus zelf schrijven"],
                ["<strong>Explain</strong> why …", "uitleggen, dus zelf schrijven"],
                ["<strong>Describe</strong> the picture.", "beschrijven, dus zelf schrijven"],
            ])),
            ("p", "<strong>Match</strong> betekent bij elkaar zoeken, <strong>niet</strong> vertalen. En de "
                  "laatste drie vragen dat je <strong>zelf iets schrijft</strong>, terwijl de eerste vijf alleen "
                  "een streep, een kring of een woord vragen."),
        ]),
        dict(kop="Beroepen en de professionele wereld", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>plumber</strong>", "loodgieter"],
                ["carpenter", "schrijnwerker"],
                ["butcher", "slager"],
                ["engineer", "ingenieur"],
                ["<strong>nurse</strong>", "verpleegkundige"],
                ["<strong>surgeon</strong>", "chirurg"],
                ["<strong>midwife</strong>", "vroedvrouw"],
                ["<strong>solicitor</strong>", "advocaat"],
                ["<strong>estate agent</strong> (VS: realtor)", "makelaar"],
                ["<strong>chef</strong>", "een kok in een restaurant, niet de baas van een bedrijf"],
            ])),
            ("p", "Wie de leiding heeft over een bedrijf, is <em>the boss</em>, <em>the manager</em> of <em>the "
                  "chief executive</em>. Een <strong>chef</strong> staat in de keuken."),
            ("p", "Werk zoeken en werken:"),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>apply for</strong> a job", "solliciteren voor een baan (let op: apply <em>for</em>)"],
                ["your <strong>CV</strong> en a covering letter", "je cv en je sollicitatiebrief"],
                ["a <strong>job interview</strong>", "een sollicitatiegesprek"],
                ["a <strong>salary</strong>, a wage", "een loon"],
                ["full-time / <strong>part-time</strong>", "voltijds / deeltijds, dus minder uren"],
                ["shift work", "ploegenwerk"],
                ["to <strong>resign</strong>", "zelf ontslag nemen"],
                ["to be fired, to be made redundant", "ontslagen worden"],
                ["to retire", "met pensioen gaan"],
            ])),
            ("weetje", "<strong>Work</strong> is in het Engels meestal <strong>ontelbaar</strong>: <em>I have a "
                       "lot of work</em>, nooit <em>two works</em>. Een afzonderlijke baan is <strong>a "
                       "job</strong>, en die is wel telbaar."),
        ]),
        dict(kop="Onderweg", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>return ticket</strong> / a <strong>single ticket</strong>", "heen en terug / enkele reis (VS: round trip / one way)"],
                ["a <strong>coach</strong>", "een touringcar"],
                ["a <strong>ferry</strong>", "een veerboot"],
                ["a <strong>tram</strong>", "een tram"],
                ["the Underground, the Tube", "de metro van Londen"],
                ["a <strong>subway</strong>", "in de VS de metro, in het VK een voetgangerstunnel"],
                ["a <strong>platform</strong>", "het perron"],
                ["a <strong>delay</strong>, to be delayed", "vertraging hebben (afgeschaft is cancelled)"],
                ["<strong>luggage</strong>, a suitcase", "bagage, een koffer"],
                ["a <strong>boarding pass</strong>, to check in", "de instapkaart, inchecken"],
                ["a <strong>youth hostel</strong>, a <strong>campsite</strong>, a <strong>bed and breakfast</strong>", "jeugdherberg, camping, logies met ontbijt"],
            ])),
            ("p", "Op het bord in het station lees je <em>The 10.20 to Leeds is delayed by 15 minutes</em>: die "
                  "trein heeft <strong>een kwartier vertraging</strong>. En <strong>luggage</strong> krijgt geen "
                  "meervouds-s: <em>my luggage is heavy</em>, net als information en furniture."),
        ]),
        dict(kop="Winkels en diensten", blokken=[
            ("p", "Britse winkels dragen een <strong>apostrof met s</strong>, omdat er oorspronkelijk "
                  "<em>shop</em> achter stond."),
            ("p", tabel(["Winkel", "Wat je er koopt"], [
                ["the <strong>newsagent's</strong>", "kranten, tijdschriften en snoep"],
                ["the butcher's", "vlees"],
                ["the greengrocer's", "groenten en fruit"],
                ["the stationer's", "papier en schrijfgerief"],
                ["the chemist's", "geneesmiddelen"],
            ])),
            ("p", tabel(["Engels", "Nederlands"], [
                ["the <strong>till</strong>, the checkout", "de kassa"],
                ["a <strong>receipt</strong>", "het kassaticket"],
                ["a <strong>refund</strong>", "je geld terug"],
                ["a <strong>discount</strong>", "een korting"],
                ["a delivery", "een levering"],
            ])),
            ("p", "Is iets stuk dat je gekocht hebt, dan vraag je <strong>a refund</strong>. Daarvoor heb je je "
                  "<strong>receipt</strong> nodig."),
        ]),
        dict(kop="Weer, tijd, plaats en scherm", blokken=[
            ("p", tabel(["Weer", "Betekenis"], [
                ["<strong>drizzle</strong>", "motregen, heel fijne lichte regen"],
                ["a downpour", "een stortbui"],
                ["<strong>hail</strong> / <strong>thunder</strong>", "hagel / donder"],
                ["<strong>mild</strong>, <strong>freezing</strong>, <strong>foggy</strong>", "zacht, ijskoud, mistig"],
                ["the (weather) <strong>forecast</strong>", "de weersvoorspelling"],
            ])),
            ("p", "De tijd is de grootste valstrik van allemaal. Het Engels telt vanaf het uur dat "
                  "<strong>voorbij</strong> is, het Nederlands noemt het uur dat <strong>komt</strong>."),
            ("p", tabel(["Engels", "Uur", "Nederlands"], [
                ["<strong>half past seven</strong>", "7.30", "half acht"],
                ["<strong>quarter past nine</strong>", "9.15", "kwart na negen"],
                ["<strong>quarter to nine</strong>", "8.45", "kwart voor negen"],
                ["<strong>a fortnight</strong>", "2 weken", "veertien dagen"],
            ])),
            ("p", "Plaatsbepalingen: <strong>just around the corner</strong> (vlakbij), opposite the station, "
                  "next to the bank, at the end of the road. Ver weg is <em>miles away</em>."),
            ("p", "Op je scherm: <strong>to log in</strong> (inloggen), <strong>to upload</strong> (opladen naar "
                  "het internet), <strong>to scroll</strong>, to post, to text, an account, a password, a link. "
                  "<em>To iron</em> hoort daar niet bij: dat is strijken."),
            ("p", "En bij sport kies je het werkwoord op de soort: <strong>play</strong> bij balsporten "
                  "(play <strong>football</strong>, play tennis), <strong>go</strong> bij sporten op -ing (go "
                  "swimming, go cycling) en <strong>do</strong> bij de rest (do yoga, do judo)."),
        ]),
        luister("luister naar het weerbericht van een Britse of Ierse zender en schrijf op wat ze voor morgen "
                "voorspellen. Hoor je drizzle, showers of mild?"),
    ],
    onthoud=[
        "Primary school, secondary school, college en headteacher. Een les is a lesson of a class.",
        "To sit an exam, to pass, to fail, to resit.",
        "Tick aankruisen, underline onderlijnen, circle omcirkelen, match verbinden, fill in the gaps invullen.",
        "Summarise, explain en describe vragen dat je zelf schrijft.",
        "Plumber, nurse, surgeon, midwife, solicitor, estate agent. Een chef is een kok.",
        "Apply for a job, a CV, a job interview, a salary. Part-time is minder uren dan full-time.",
        "To resign is zelf opstappen, to be made redundant is ontslagen worden.",
        "Work is ontelbaar, a job is telbaar.",
        "Return ticket is heen en terug, single is enkel. Een subway is in het VK een voetgangerstunnel.",
        "Platform is het perron, delayed is vertraagd, cancelled is afgeschaft. Luggage krijgt geen meervouds-s.",
        "Newsagent's, butcher's, greengrocer's: Britse winkels dragen een apostrof met s.",
        "Till is de kassa, receipt het kassaticket, refund je geld terug, discount een korting.",
        "Drizzle is motregen, mild zacht, freezing ijskoud, foggy mistig, forecast de voorspelling.",
        "Half past seven is 7.30 en quarter to nine is 8.45. A fortnight is twee weken.",
        "Play football, go swimming, do yoga.",
    ],
)


# ───────────────────────── 7. Nouns, articles, quantifiers en numerals
BUNDELS["nouns-articles-quantifiers-en-numerals-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Nouns, articles, quantifiers en numerals",
    onder="Het meervoud, telbaar en ontelbaar, de bezitsvorm, de lidwoorden a, an en the, de hoeveelheidswoorden en de telwoorden.",
    secties=[
        dict(kop="Het meervoud", blokken=[
            ("p", "De hoofdregel is een <strong>s</strong>. Daarnaast zijn er vier spellingregels en een handvol "
                  "onregelmatige vormen die je gewoon kent of niet."),
            ("p", tabel(["Regel", "Voorbeeld"], [
                ["een y na een <strong>medeklinker</strong> wordt <strong>ies</strong>", "<strong>city → cities</strong>, baby → babies, country → countries"],
                ["een y na een <strong>klinker</strong> blijft staan", "<strong>boy → boys</strong>, day → days, key → keys"],
                ["woorden op f of fe krijgen vaak <strong>ves</strong>", "<strong>knife → knives</strong>, life → lives, wolf → wolves (maar roof → roofs)"],
                ["na een sisklank komt <strong>es</strong>", "bus → buses, watch → watches, box → boxes"],
                ["een paar woorden op o krijgen <strong>es</strong>", "<strong>tomato → tomatoes</strong>, potato → potatoes, hero → heroes (maar photo → photos)"],
                ["woorden op <strong>-is</strong> krijgen <strong>-es</strong>", "<strong>analysis → analyses</strong>, crisis → crises, basis → bases"],
            ])),
            ("p", tabel(["Onregelmatig", "Meervoud"], [
                ["child", "<strong>children</strong> (nooit childrens)"],
                ["man / <strong>woman</strong>", "men / <strong>women</strong>"],
                ["foot / tooth / mouse", "<strong>feet</strong> / <strong>teeth</strong> / <strong>mice</strong>"],
                ["person", "<strong>people</strong> (peoples zijn volkeren)"],
                ["<strong>sheep</strong>, <strong>fish</strong>, <strong>series</strong>", "blijven hetzelfde: one sheep, two sheep"],
            ])),
            ("p", "Bij een <strong>samengesteld naamwoord</strong> krijgt alleen het <strong>laatste</strong> "
                  "deel de meervouds-s: <em>two <strong>toothbrushes</strong></em>, niet two teethbrush. En "
                  "<strong>trousers</strong> staat altijd in het meervoud, dus ook het werkwoord: <em>these "
                  "trousers are too long</em>."),
        ]),
        dict(kop="Telbaar en ontelbaar", blokken=[
            ("p", "Een <strong>ontelbaar</strong> woord kan je <strong>niet in het meervoud</strong> zetten. Je "
                  "telt het met een maatwoord."),
            ("p", tabel(["Ontelbaar", "Hoe je het telt"], [
                ["<strong>information</strong>", "two pieces of information"],
                ["<strong>advice</strong>", "a piece of advice"],
                ["<strong>furniture</strong>", "two pieces of furniture"],
                ["<strong>money</strong>", "a lot of money"],
                ["<strong>hair</strong> (het haar op je hoofd)", "<strong>my hair is very long</strong> (losse haren zijn wel hairs)"],
                ["luggage, bread, work", "a piece of luggage, a loaf of bread, a lot of work"],
            ])),
            ("kader", "Het woord <strong>news</strong> eindigt op een s maar is <strong>enkelvoud</strong>: "
                      "<em>the news is good</em>. Zo werkt het ook bij mathematics en physics. <em>A chair</em> "
                      "is wél gewoon telbaar."),
        ]),
        dict(kop="De bezitsvorm", blokken=[
            ("p", tabel(["Situatie", "Vorm", "Voorbeeld"], [
                ["één persoon", "'s", "<strong>my sister's bike</strong>"],
                ["meer dan één, met meervouds-s", "s'", "<strong>the boys' room</strong>"],
                ["onregelmatig meervoud zonder s", "'s", "<strong>the children's room</strong>"],
                ["een ding", "of", "<strong>the roof of the house</strong>"],
                ["tijd", "'s", "today's paper, a week's holiday"],
            ])),
            ("p", "Bij <strong>mensen en dieren</strong> gebruik je de apostrofvorm, bij <strong>dingen</strong> "
                  "liever <strong>of</strong>. <em>The bike of my sister</em> klinkt in het Engels vreemd."),
        ]),
        dict(kop="De lidwoorden", blokken=[
            ("p", "Je kiest <strong>a</strong> of <strong>an</strong> op de <strong>klank</strong>, niet op de "
                  "letter."),
            ("p", tabel(["an, want klinkerklank", "a, want medeklinkerklank"], [
                ["an <strong>apple</strong>, an <strong>umbrella</strong>, an <strong>hour</strong> (de h zwijgt), an <strong>honest man</strong>, an <strong>engineer</strong>",
                 "a <strong>university</strong> (klinkt als you), a hotel, a European country, a year"],
            ])),
            ("p", "Bij een <strong>beroep</strong> laat het Engels het lidwoord <strong>niet</strong> weg: "
                  "<em>he is <strong>a</strong> teacher</em>, <em>she is <strong>an</strong> engineer</em>. Het "
                  "Nederlands doet dat wel, en daar glijdt iedereen over uit."),
            ("p", "<strong>The</strong> gebruik je als je een <strong>bepaald exemplaar</strong> bedoelt: "
                  "<em>The book you lent me was great.</em> Spreek je <strong>algemeen</strong> over boeken, "
                  "muziek of een vak, dan zet je er <strong>niets</strong> voor: <em>I like music</em>, <em>I "
                  "study history</em>, <em>I speak English</em>, <em>I like maths</em>. Met the erbij bedoel je "
                  "een bepaald deel: <em>the history of Wales</em>."),
        ]),
        dict(kop="Hoeveelheidswoorden", blokken=[
            ("p", tabel(["Bij telbaar meervoud", "Bij ontelbaar", "Bij allebei"], [
                ["<strong>many</strong>, <strong>a few</strong>, <strong>several</strong>, few",
                 "<strong>much</strong>, <strong>a little</strong>, little",
                 "<strong>a lot of</strong>, some, any, plenty of"],
            ])),
            ("p", "<em>How <strong>much</strong> water do you need?</em> tegenover <em>How <strong>many</strong> "
                  "books?</em> In een gewone bevestigende zin klinkt <em>a lot of</em> natuurlijker dan much: "
                  "<em>I don't have <strong>much</strong> time left</em>, maar <em>I have a lot of time</em>."),
            ("p", "<strong>A few</strong> hoort bij telbare woorden, <strong>a little</strong> bij ontelbare. En "
                  "het lidwoordje ervoor verandert de toon: <em>she has <strong>a few</strong> friends</em> "
                  "betekent dat ze er enkele heeft, <em>she has <strong>few</strong> friends</em> dat ze er "
                  "bijna geen heeft. <strong>A few klinkt positief, few klinkt als weinig.</strong>"),
            ("p", "In <strong>vragen en ontkenningen</strong> gebruik je <strong>any</strong>, in bevestigende "
                  "zinnen <strong>some</strong>: <em>Is there <strong>any</strong> milk left?</em> Bied je iets "
                  "aan, dan mag some wel: <em>Would you like some tea?</em>"),
            ("kader", "<strong>Very</strong> hoort voor een bijvoeglijk naamwoord of een bijwoord (<em>very "
                      "tired</em>), <strong>a lot</strong> bij een werkwoord (<em>she talks a lot</em>). Ze "
                      "betekenen dus niet hetzelfde en staan niet op dezelfde plaats."),
            ("p", "Na <strong>a lot of</strong> kijk je naar het naamwoord erachter om te weten of je is of are "
                  "neemt: <em>There <strong>are</strong> a lot of people here</em>, want people is meervoud."),
        ]),
        dict(kop="Telwoorden", blokken=[
            ("p", tabel(["Getal", "Rangtelwoord"], [
                ["1, 2, 3", "first, second, <strong>third</strong> (onregelmatig)"],
                ["4, 5, 6", "fourth, <strong>fifth</strong>, sixth"],
                ["9, 12", "<strong>ninth</strong> (de e valt weg), <strong>twelfth</strong> (de ve wordt f)"],
                ["21, 40", "<strong>twenty-first</strong>, <strong>fortieth</strong>"],
            ])),
            ("p", "Het getal <strong>1500</strong> lees je als <strong>one thousand five hundred</strong>; gaat "
                  "het over een jaartal, dan zeg je <em>fifteen hundred</em>. Bij hundred en thousand komt er "
                  "<strong>geen meervouds-s</strong> als er een getal voor staat."),
            ("p", "<strong>1,250</strong> lees je als <strong>one thousand two hundred and fifty</strong>. "
                  "Britten zetten <em>and</em> voor de laatste twee cijfers."),
            ("kader", "De <strong>komma</strong> is in het Engels het <strong>duizendtalteken</strong> en de "
                      "<strong>punt</strong> het <strong>decimaalteken</strong>: 3,5 schrijf je als "
                      "<strong>3.5</strong> en je leest het als <em>three point five</em>."),
        ]),
        luister("luister naar een Engelstalig nieuwsbericht en schrijf de getallen op die je hoort. "
                "Klopt jouw notatie met de punt en de komma?"),
    ],
    onthoud=[
        "City wordt cities, boy wordt boys, knife wordt knives, tomato wordt tomatoes, analysis wordt analyses.",
        "Children, women, feet, teeth, mice en people zijn onregelmatig. Sheep, fish en series blijven hetzelfde.",
        "Bij een samengesteld naamwoord krijgt alleen het laatste deel de s: two toothbrushes.",
        "Information, advice, furniture, money, hair en work zijn ontelbaar. News eindigt op s maar is enkelvoud.",
        "My sister's bike, the boys' room, the children's room, the roof of the house.",
        "A of an kies je op de klank: an hour, an honest man, maar a university.",
        "Bij een beroep hoort een lidwoord: he is a teacher.",
        "Geen the bij een taal of een schoolvak in het algemeen: I study history.",
        "Many, a few en several bij telbaar; much en a little bij ontelbaar; a lot of bij allebei.",
        "A few klinkt positief, few klinkt als weinig.",
        "Any in vragen en ontkenningen, some in bevestigende zinnen.",
        "Very staat bij een bijvoeglijk naamwoord, a lot bij een werkwoord.",
        "First, second, third, fifth, ninth, twelfth, twenty-first, fortieth.",
        "One thousand five hundred; hundred en thousand krijgen geen meervouds-s na een getal.",
        "In het Engels is de komma het duizendtalteken en de punt het decimaalteken: 3.5.",
    ],
)


# ───────────────────────── 8. Pronouns: de zeven soorten
BUNDELS["pronouns-de-zeven-soorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Pronouns: de zeven soorten",
    onder="Persoonlijk, bezittelijk, wederkerend, aanwijzend, vragend, betrekkelijk en onbepaald, en hoe je duidelijk blijft in je verwijzing.",
    secties=[
        dict(kop="Persoonlijke voornaamwoorden", blokken=[
            ("p", tabel(["Onderwerpsvorm", "Voorwerpsvorm", "Bezittelijk (voor een naamwoord)", "Zelfstandig bezittelijk"], [
                ["I", "<strong>me</strong>", "my", "<strong>mine</strong>"],
                ["you", "you", "your", "<strong>yours</strong>"],
                ["he / she / it", "<strong>him</strong> / her / <strong>it</strong>", "his / her / <strong>its</strong>", "his / <strong>hers</strong>"],
                ["we", "us", "our", "ours"],
                ["<strong>they</strong>", "<strong>them</strong>", "<strong>their</strong>", "<strong>theirs</strong>"],
            ])),
            ("p", "Wie de handeling <strong>doet</strong>, staat in de onderwerpsvorm: <em><strong>She and "
                  "I</strong> went to the cinema.</em> Laat de andere persoon even weg en je hoort het meteen: "
                  "<em>I went</em>, niet <em>me went</em>. Staat het voornaamwoord <strong>na het "
                  "werkwoord</strong> of <strong>na een voorzetsel</strong>, dan neem je de voorwerpsvorm: "
                  "<em>my parents called <strong>me</strong></em>, <em>this is for <strong>her</strong></em>, "
                  "<em>between you and <strong>me</strong></em>."),
            ("p", "<strong>It</strong> verwijst naar <strong>een ding of een dier</strong>. Bij een huisdier met "
                  "een naam wordt het vaak he of she."),
            ("kader", "<strong>Its</strong> en <strong>it's</strong> zijn twee verschillende woorden. "
                      "<em>Its</em> is bezittelijk: <em>the dog wagged <strong>its</strong> tail</em>, <em>the "
                      "cat has hurt <strong>its</strong> paw</em>, <em>the house and <strong>its</strong> garden "
                      "are for sale</em>. <em>It's</em> is de korte vorm van it is of it has. En "
                      "<strong>yours</strong> schrijf je nooit met een apostrof."),
        ]),
        dict(kop="Wederkerende voornaamwoorden", blokken=[
            ("p", "Slaat de handeling terug op het onderwerp, dan neem je de vorm op <strong>-self</strong> of "
                  "<strong>-selves</strong>: <em>I hurt <strong>myself</strong></em>."),
            ("p", tabel(["Enkelvoud", "Meervoud"], [
                ["myself, yourself, <strong>himself</strong>, herself, itself",
                 "<strong>ourselves</strong>, yourselves, <strong>themselves</strong>"],
            ])),
            ("p", "<em>Theirselves</em> en <em>hisself</em> bestaan niet. <strong>By myself</strong> betekent "
                  "dat je iets <strong>alleen</strong> doet, zonder hulp; <em>I did it myself</em> legt de "
                  "nadruk op wie het deed."),
            ("p", "Let op: <strong>wash</strong> en <strong>dress</strong> zijn in het Engels <strong>niet "
                  "wederkerend</strong>. Wij zeggen zich wassen, het Engels zegt gewoon <em>she washed and got "
                  "dressed</em>."),
        ]),
        dict(kop="Aanwijzende voornaamwoorden", blokken=[
            ("p", tabel(["", "Dichtbij", "Verder weg"], [
                ["enkelvoud", "<strong>this</strong>", "<strong>that</strong>"],
                ["meervoud", "<strong>these</strong>", "<strong>those</strong>"],
            ])),
            ("p", "<em><strong>Those</strong> shoes over there are mine.</em> Over there zegt dat ze ver zijn, "
                  "en shoes is meervoud."),
        ]),
        dict(kop="Vragende voornaamwoorden", blokken=[
            ("p", tabel(["Vraagwoord", "Vraagt naar"], [
                ["<strong>who</strong>", "een persoon als onderwerp: Who broke the window?"],
                ["<strong>whom</strong>", "een persoon als voorwerp, formeel: To whom did you speak?"],
                ["<strong>whose</strong>", "de eigenaar: <strong>Whose bag is this?</strong>"],
                ["<strong>which</strong>", "een keuze uit een beperkte groep: Which colour, red or blue?"],
                ["<strong>what</strong>", "een open keuze: What colour do you want?"],
                ["where / when / why", "een plaats / een tijd / een reden"],
            ])),
            ("kader", "<strong>Who's</strong> is de korte vorm van <em>who is</em>: <em>Who's coming "
                      "tonight?</em> <strong>Whose</strong> is bezittelijk. Ze klinken hetzelfde en betekenen "
                      "iets heel anders."),
        ]),
        dict(kop="Betrekkelijke voornaamwoorden", blokken=[
            ("p", tabel(["Woord", "Waarbij"], [
                ["<strong>who</strong>", "een persoon: the woman <strong>who</strong> lives next door"],
                ["<strong>which</strong>", "een ding: the shop <strong>which</strong> sells old records"],
                ["<strong>that</strong>", "personen én dingen: the book <strong>that</strong> I read"],
                ["<strong>whose</strong>", "bezit, ook bij een ding: the house <strong>whose</strong> roof is red"],
                ["<strong>where</strong> / <strong>when</strong> / why", "een plaats / een tijd / een reden"],
            ])),
            ("p", "<em>This is the town <strong>where</strong> I was born.</em> <em>I remember the day "
                  "<strong>when</strong> we met.</em> Bij een tijdstip hoort when, bij een plaats where."),
            ("p", "Volgt er meteen een <strong>nieuw onderwerp</strong>, dan mag het betrekkelijk voornaamwoord "
                  "<strong>weg</strong>: <em>the book I read</em>. Is het zelf het onderwerp van de bijzin, dan "
                  "moet het blijven staan."),
            ("kader", "<strong>What</strong> kan geen betrekkelijk voornaamwoord zijn. <em>The film what I "
                      "saw</em> hoor je wel in spreektaal, maar het is fout: het moet <em>the film that I "
                      "saw</em> of <em>the film I saw</em> zijn."),
        ]),
        dict(kop="Onbepaalde voornaamwoorden", blokken=[
            ("p", "<strong>Someone</strong>, <strong>anything</strong>, <strong>nobody</strong>, everybody, "
                  "everything, none en each. Ze zijn grammaticaal <strong>enkelvoud</strong>: "
                  "<em>Somebody <strong>has</strong> left their umbrella.</em> <em>Everybody "
                  "<strong>is</strong> here.</em> <em>Each of the students <strong>has</strong> a laptop</em>, "
                  "ook al volgt er een meervoud na <em>of</em>."),
            ("p", "In vragen en ontkenningen gebruik je <strong>anything</strong>, in bevestigende zinnen "
                  "something: <em>Do you need anything?</em>, <em>I didn't see <strong>anything</strong>.</em> "
                  "Bied je iets aan, dan mag something: <em>Would you like something to drink?</em>"),
            ("kader", "<strong>Twee ontkenningen in één zin mag niet</strong> in het Engels. Het is <em>I didn't "
                      "see anything</em> of <em>I saw nothing</em>, nooit <em>I didn't see nothing</em>."),
            ("p", "<strong>None of them came</strong> betekent dat <strong>niemand van hen gekomen is</strong>. "
                  "None is de ontkenning van all. En <em>there is <strong>nobody</strong> in the room</em> zegt "
                  "dat de kamer leeg is; <em>there isn't anybody</em> betekent hetzelfde, maar dan met de "
                  "ontkenning in het werkwoord."),
        ]),
        dict(kop="Duidelijk blijven", blokken=[
            ("p", "Het Engels heeft <strong>één woord voor jij en u</strong>: <strong>you</strong>, enkelvoud én "
                  "meervoud, beleefd én gewoon. Beleefdheid toon je met andere woorden, bijvoorbeeld met "
                  "<em>could you</em>."),
            ("p", "Juist omdat er zo weinig vormen zijn, wordt een verwijzing snel onduidelijk. <em>Tom told Ben "
                  "that he had passed.</em> Je <strong>weet niet wie geslaagd is</strong>: he kan naar Tom of "
                  "naar Ben verwijzen. En <em>The teachers helped the pupils, and they thanked them</em> is even "
                  "troebel, want allebei de groepen zijn meervoud."),
            ("kader", "Zodra twee mogelijke antwoorden even goed passen, <strong>herhaal je het "
                      "naamwoord</strong>: <em>The teachers helped the pupils, and <strong>the pupils</strong> "
                      "thanked them.</em> Dat leest minder elegant en is veel duidelijker."),
        ]),
        luister("luister naar een gesprek in een Engelstalige serie en let één scène lang alleen op de "
                "voornaamwoorden: weet je telkens naar wie ze verwijzen?"),
    ],
    onthoud=[
        "Onderwerpsvorm I, he, she, they. Voorwerpsvorm me, him, her, them, ook na een voorzetsel: between you and me.",
        "Its is bezittelijk, it's is it is. Yours schrijf je nooit met een apostrof.",
        "Mine, yours, his, hers, ours en theirs staan alleen; my, your, their horen voor een naamwoord.",
        "Wederkerend: myself, himself, ourselves, themselves. Theirselves bestaat niet.",
        "By myself betekent alleen, zonder hulp. Wash en dress zijn in het Engels niet wederkerend.",
        "This en these zijn dichtbij, that en those verder weg.",
        "Who vraagt naar een persoon, whose naar de eigenaar, which bij een beperkte keuze, what bij een open keuze.",
        "Who's is who is, whose is bezittelijk.",
        "Who bij personen, which bij dingen, that bij allebei, whose ook bij een ding.",
        "Volgt er een nieuw onderwerp, dan mag that weg: the book I read. What kan nooit betrekkelijk zijn.",
        "Someone, anything, nobody, everybody en each zijn enkelvoud.",
        "Twee ontkenningen in één zin mag niet: I didn't see anything.",
        "None of them came betekent dat niemand kwam.",
        "You is enkelvoud en meervoud, beleefd en gewoon.",
        "Wordt een verwijzing dubbelzinnig, herhaal dan het naamwoord.",
    ],
)


# ───────────────────────── 9. Adjectives, adverbs, comparatives en voorzetsels
BUNDELS["adjectives-adverbs-comparatives-en-voorzetsels-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Adjectives, adverbs, comparatives en voorzetsels",
    onder="Het verschil tussen een bijvoeglijk naamwoord en een bijwoord, waar ze in de zin staan, hoe je vergelijkt, en welk voorzetsel waarbij hoort.",
    secties=[
        dict(kop="Bijvoeglijke naamwoorden", blokken=[
            ("p", "Een bijvoeglijk naamwoord staat in het Engels <strong>vóór het naamwoord</strong>: <em>a red "
                  "car</em>, nooit <em>a car red</em>. Achter het naamwoord komt het alleen na een "
                  "koppelwerkwoord: <em>the car is red</em>."),
            ("p", "Het <strong>blijft altijd hetzelfde</strong>, ook bij een meervoud: <em>two <strong>red</strong> "
                  "cars</em>, niet <em>two reds cars</em>. Het Nederlands verandert wel: een rode auto, twee rode "
                  "auto's."),
            ("p", "Stapel je er meer dan één op, dan is de volgorde: eerst je <strong>mening</strong>, dan de "
                  "<strong>grootte</strong>, dan de leeftijd en de vorm, en pas daarna de <strong>kleur</strong>. "
                  "Dus <em>a <strong>lovely big red</strong> balloon</em>. In de praktijk stapel je er hoogstens "
                  "twee of drie."),
        ]),
        dict(kop="Bijwoorden", blokken=[
            ("p", "Een bijwoord zegt iets over de <strong>handeling</strong>. Meestal maak je het met "
                  "<strong>-ly</strong>."),
            ("p", tabel(["Bijvoeglijk naamwoord", "Bijwoord", "Regel"], [
                ["quick, careful", "<strong>quickly</strong>, <strong>carefully</strong>", "gewoon -ly erbij"],
                ["easy, <strong>happy</strong>, angry", "<strong>easily</strong>, <strong>happily</strong>, angrily", "y na een medeklinker wordt i"],
                ["<strong>terrible</strong>, simple", "<strong>terribly</strong>, simply", "bij -le valt de e weg"],
                ["<strong>good</strong>", "<strong>well</strong>", "helemaal onregelmatig"],
                ["<strong>fast</strong>, hard, late, early", "fast, hard, late, early", "blijven hetzelfde (fastly bestaat niet)"],
            ])),
            ("p", "<em>She sings <strong>well</strong></em> zegt hoe ze zingt. <em>She is a <strong>good</strong> "
                  "singer</em> zegt iets over haar. Bij de werkwoorden <em>drive</em>, <em>speak</em> en "
                  "<em>work</em> heb je dus een bijwoord nodig: <em>drive <strong>carefully</strong>, the roads "
                  "are icy</em>."),
            ("kader", "Drie woorden waarvan de -ly de betekenis <strong>omdraait</strong>. "
                      "<strong>Hard</strong> is hard, <strong>hardly</strong> is nauwelijks. <strong>Late</strong> "
                      "is laat, <strong>lately</strong> is de laatste tijd. <em>This is a lot of hard work</em>, "
                      "<em>she has worked hard</em> en <em>he has hardly worked</em> zeggen dus drie verschillende "
                      "dingen. Wie hard werkt, is moe; wie hardly werkt, doet bijna niets."),
            ("p", "Omgekeerd eindigen <strong>friendly</strong>, lovely, lonely en silly op -ly en zijn het toch "
                  "<strong>bijvoeglijke</strong> naamwoorden. Wil je er een bijwoord van maken, dan zeg je "
                  "<em>in a friendly way</em>."),
        ]),
        dict(kop="Waar een bijwoord staat", blokken=[
            ("p", "Bijwoorden van <strong>frequentie</strong> (always, usually, <strong>often</strong>, "
                  "sometimes, never) staan <strong>voor het hoofdwerkwoord</strong>: <em>She "
                  "<strong>often</strong> goes to the gym.</em> Maar bij <strong>to be</strong> staan ze "
                  "<strong>erachter</strong>: <em>he is <strong>always</strong> late</em>."),
            ("p", "Na een <strong>koppelwerkwoord</strong> zoals <em>look</em>, <em>smell</em>, "
                  "<strong>taste</strong>, <em>sound</em> en <em>feel</em> komt een <strong>bijvoeglijk "
                  "naamwoord</strong>, want het zegt iets over het onderwerp: <em>it smells good</em>, <em>the "
                  "soup tastes <strong>delicious</strong></em>. Vergelijk: <em>she looks happy</em> tegenover "
                  "<em>she looked at me happily</em>."),
            ("p", "Versterkers: <strong>very</strong>, <strong>quite</strong> en <strong>extremely</strong> gaan "
                  "voor een bijvoeglijk naamwoord (<em>very tired</em>). Voor een <strong>vergrotende "
                  "trap</strong> gebruik je geen very maar <strong>much</strong>, <strong>far</strong> of "
                  "<strong>a lot</strong>: <em>much better</em>, niet <em>very better</em>."),
        ]),
        dict(kop="Vergelijken", blokken=[
            ("p", tabel(["Soort woord", "Vergrotende trap", "Overtreffende trap"], [
                ["kort (één lettergreep)", "small → <strong>smaller</strong>", "smallest"],
                ["korte klinker + medeklinker", "<strong>big → bigger</strong>, hot → hotter", "biggest, hottest"],
                ["twee lettergrepen op -y", "<strong>easy → easier</strong>", "easiest"],
                ["twee of meer lettergrepen", "<strong>more</strong> expensive, <strong>more</strong> interesting, <strong>more</strong> beautiful", "the most expensive"],
                ["onregelmatig", "good → <strong>better</strong>, bad → <strong>worse</strong>, little → less", "best, <strong>worst</strong>, least"],
            ])),
            ("p", "Na een vergrotende trap komt <strong>than</strong>: <em>this book is more interesting "
                  "<strong>than</strong> the other one</em>. Verwar het niet met <em>then</em>, dat daarna "
                  "betekent."),
            ("p", "Zijn twee dingen <strong>gelijk</strong>, dan zeg je <strong>as … as</strong>: <em>She is "
                  "<strong>as tall as</strong> her brother.</em> Zijn ze niet gelijk, dan <strong>not as … "
                  "as</strong>: <em>this test is <strong>not as hard as</strong> the last one</em> betekent dat "
                  "<strong>deze toets makkelijker is</strong>."),
            ("p", "Voor een overtreffende trap zet je bijna altijd <strong>the</strong>: <em>she is "
                  "<strong>the</strong> tallest in the class</em>. Bij de vergrotende trap niet."),
            ("kader", "Eén vaste vorm om te kennen: <strong>the … , the …</strong> — <em><strong>The more</strong> "
                      "you practise, <strong>the easier</strong> it gets.</em> Twee keer <em>the</em>, en easy "
                      "krijgt -ier en geen more."),
        ]),
        dict(kop="Voorzetsels van tijd", blokken=[
            ("p", tabel(["Voorzetsel", "Waarbij", "Voorbeeld"], [
                ["<strong>at</strong>", "een uur, en night", "<strong>at seven o'clock</strong>, <strong>at night</strong>"],
                ["<strong>on</strong>", "een dag of een volledige datum", "on Monday, <strong>on 14 March</strong>, on Friday morning"],
                ["<strong>in</strong>", "een maand, een seizoen, een jaar, een dagdeel", "in <strong>July</strong>, in <strong>2027</strong>, in <strong>the morning</strong>"],
            ])),
            ("p", "Bij <strong>night</strong> hoort <strong>at</strong>, terwijl het bij the morning, the "
                  "afternoon en the evening <em>in</em> is. En staat er een dag bij, dan wint de dag: <em>on "
                  "Monday morning</em>."),
        ]),
        dict(kop="Voorzetsels van plaats, en vaste combinaties", blokken=[
            ("p", "<strong>On</strong> voor een oppervlak (<em>the keys are <strong>on</strong> the table</em>), "
                  "<strong>in</strong> voor iets wat omsloten is (<em>in the box</em>), <strong>at</strong> voor "
                  "een punt of een plaats waar je bent (<em>at the bus stop</em>, <em>at school</em>)."),
            ("p", "Sommige werkwoorden en bijvoeglijke naamwoorden hebben hun voorzetsel <strong>vast</strong>, "
                  "en dat volgt lang niet altijd het Nederlands. Leer het woord en het voorzetsel als "
                  "<strong>één geheel</strong>."),
            ("p", tabel(["Vaste combinatie", "Nederlands"], [
                ["<strong>wait for</strong> the bus", "op de bus wachten"],
                ["<strong>listen to</strong> music", "naar muziek luisteren"],
                ["<strong>belong to</strong> someone", "van iemand zijn"],
                ["<strong>explain</strong> something <strong>to</strong> someone", "iets aan iemand uitleggen"],
                ["<strong>discuss</strong> the problem", "over het probleem praten (zonder voorzetsel!)"],
                ["<strong>good at</strong> maths, bad at", "goed in wiskunde"],
                ["interested <strong>in</strong>, afraid <strong>of</strong>", "geïnteresseerd in, bang van"],
                ["<strong>married to</strong> someone", "getrouwd met iemand (nooit married with)"],
                ["<strong>arrive at</strong> the station / <strong>arrive in</strong> London", "aankomen in een gebouw / in een stad of land"],
            ])),
        ]),
        luister("luister naar een Engelstalig liedje dat je goed kent en zoek de bijwoorden en de "
                "voorzetsels erin. Staan ze waar je ze zou verwachten?"),
    ],
    onthoud=[
        "Een bijvoeglijk naamwoord staat voor het naamwoord en krijgt nooit een meervouds-s.",
        "Volgorde: mening, grootte, leeftijd en vorm, dan kleur: a lovely big red balloon.",
        "Bijwoord met -ly: quickly, easily, happily, terribly. Good wordt well; fast, hard en late blijven hetzelfde.",
        "Hard is hard, hardly is nauwelijks. Late is laat, lately is de laatste tijd.",
        "Friendly en lovely eindigen op -ly maar zijn bijvoeglijke naamwoorden: in a friendly way.",
        "Frequentiebijwoorden staan voor het hoofdwerkwoord, maar achter to be.",
        "Na look, smell, taste en sound komt een bijvoeglijk naamwoord: the soup tastes delicious.",
        "Very bij een bijvoeglijk naamwoord, much of far bij een vergrotende trap: much better.",
        "Big wordt bigger, easy wordt easier, expensive wordt more expensive.",
        "Good, better, best. Bad, worse, worst.",
        "Na een vergrotende trap komt than. Gelijk is as … as, en not as … as betekent minder.",
        "Bij de overtreffende trap hoort the. The more you practise, the easier it gets.",
        "At bij een uur en at night, on bij een dag of datum, in bij een maand, een jaar of een dagdeel.",
        "On een oppervlak, in iets omslotens, at een punt of plaats.",
        "Wait for, listen to, belong to, good at, interested in, afraid of, married to, arrive at of in. Discuss neemt niets.",
    ],
)


# ───────────────────────── 10. De tegenwoordige tijden
BUNDELS["de-tegenwoordige-tijden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De tegenwoordige tijden",
    onder="There is en there are, de present simple, de present continuous, en de present perfect die het Nederlands niet kent.",
    secties=[
        dict(kop="There is en there are", blokken=[
            ("p", "Je kijkt naar het woord dat <strong>erachter</strong> komt. <em>There <strong>are</strong> "
                  "three books on the table.</em> <em>There <strong>is</strong> some milk in the fridge</em>, "
                  "want <strong>milk is ontelbaar</strong> en neemt de enkelvoudsvorm. Bij een opsomming kijk je "
                  "naar het eerste woord: <em>there is a knife and two forks</em>."),
            ("p", "In een ontkenning: <em>There <strong>aren't any</strong> eggs left.</em> Eggs is meervoud, en "
                  "in een ontkenning hoort <strong>any</strong>, niet some."),
        ]),
        dict(kop="De present simple", blokken=[
            ("p", "Voor <strong>gewoontes en feiten</strong>: <em>I get up at seven every day</em>, <em>The sun "
                  "rises in the east</em>, <em>I <strong>work</strong> in a shop every Saturday</em>. Ook <em>how often do you <strong>go swimming</strong>?</em> vraagt naar een gewoonte "
                  "en staat dus in de present simple, niet in de continuous. Staat er "
                  "<em>every Saturday</em>, <em>always</em> of <em>how often</em> bij, dan is het bijna altijd "
                  "present simple."),
            ("p", tabel(["Derde persoon enkelvoud", "Regel"], [
                ["<strong>watches</strong>, misses, fixes, goes, does", "na een sisklank komt es"],
                ["<strong>flies</strong>, studies, tries", "y na een medeklinker wordt ies"],
                ["plays, says", "y na een klinker blijft staan"],
                ["<strong>studies French</strong>, <strong>does his homework</strong>, he <strong>goes</strong> to school", "de s van de derde persoon vergeten is de meest gemaakte fout in het Engels"],
            ])),
            ("kader", "In een <strong>vraag</strong> of een <strong>ontkenning</strong> neemt "
                      "<strong>does</strong> de s over, en blijft het hoofdwerkwoord in de basisvorm: "
                      "<em><strong>Does she live</strong> here?</em>, <em>she <strong>doesn't live</strong> "
                      "here</em>. Nooit <em>does she lives</em> of <em>she doesn't lives</em>."),
        ]),
        dict(kop="De present continuous", blokken=[
            ("p", "De vorm is <strong>am, is of are</strong> plus het werkwoord op <strong>-ing</strong>: "
                  "<em>She <strong>is writing</strong> a letter.</em> I neemt am, he, she en it nemen is, en "
                  "you, we en <strong>they</strong> nemen <strong>are</strong>."),
            ("p", tabel(["Spelling van -ing", "Voorbeeld"], [
                ["stomme e valt weg", "write → <strong>writing</strong>, make → making"],
                ["ie wordt y", "lie → <strong>lying</strong>, die → dying"],
                ["korte klinker + medeklinker verdubbelt", "<strong>sit → sitting</strong>, run → running, begin → <strong>beginning</strong>"],
            ])),
            ("p", "Je gebruikt hem voor wat <strong>nu bezig is</strong>: <em>Look! It is raining.</em> "
                  "Vergelijk met <em>It rains a lot in Belgium</em>, een gewoonte. Hij kan ook iets zeggen dat "
                  "<strong>al afgesproken</strong> is voor later: <em>we are meeting at six</em>, <em>I am "
                  "seeing the dentist tomorrow</em>."),
            ("p", "In een vraag wisselen het onderwerp en de vorm van to be van plaats: <em><strong>What are "
                  "you doing</strong> right now?</em>"),
            ("kader", "Werkwoorden die een <strong>toestand</strong> beschrijven in plaats van een handeling, "
                      "gaan <strong>niet</strong> in de -ing-vorm: <strong>know</strong>, believe, want, like, "
                      "<strong>understand</strong>, <strong>belong</strong>. Je zegt <em>I know</em>, nooit <em>I "
                      "am knowing</em>. <em>Listen</em> kan wel: <em>I am listening to music</em>."),
        ]),
        dict(kop="De present perfect", blokken=[
            ("p", "De vorm is <strong>have of has</strong> plus het <strong>voltooid deelwoord</strong>, de "
                  "derde vorm van het werkwoord: <em>I have seen</em>, <em>she <strong>has</strong> "
                  "finished</em>. Na have komt <strong>eaten</strong>, niet ate: <em>Have you ever "
                  "<strong>eaten</strong> sushi?</em>"),
            ("p", "Hij legt altijd een <strong>verband met nu</strong>. Dat verband komt in drie vormen:"),
            ("p", tabel(["Gebruik", "Voorbeeld"], [
                ["begon vroeger en is nog bezig", "<strong>I have lived in Antwerp since 2020.</strong>"],
                ["het gevolg is er nog", "<strong>I have lost my keys</strong> (en ik vind ze nu niet)"],
                ["ergens ooit, zonder tijdstip", "Have you ever eaten sushi?"],
            ])),
            ("kader", "<em>Ik woon sinds 2020 in Antwerpen</em> wordt in het Engels <strong>geen present "
                      "simple</strong> maar een present perfect: <strong>I have lived in Antwerp since "
                      "2020</strong>. Het Nederlands gebruikt daar de tegenwoordige tijd. Dat is de klassiekste "
                      "fout van allemaal."),
            ("p", "<strong>Since</strong> noemt het <strong>moment waarop iets begon</strong>: since 2020, since "
                  "Monday, since last Monday. <strong>For</strong> noemt de <strong>duur</strong>: for "
                  "<strong>two hours</strong>, for <strong>a week</strong>, for <strong>ages</strong>, for "
                  "three years."),
            ("p", tabel(["Woord", "Waar het staat", "Voorbeeld"], [
                ["<strong>just</strong>", "tussen have en het deelwoord", "I have <strong>just</strong> arrived"],
                ["<strong>already</strong>", "tussen have en het deelwoord, bevestigend", "I have <strong>already</strong> seen that film"],
                ["<strong>yet</strong>", "achteraan, in een vraag of een ontkenning", "Have you finished <strong>yet</strong>? / I haven't finished yet"],
            ])),
        ]),
        dict(kop="Present perfect of past simple?", blokken=[
            ("p", "Noemt de zin een <strong>afgesloten moment</strong>, dan gebruik je de "
                  "<strong>past simple</strong>, ook al is het gevolg er nog."),
            ("p", tabel(["Past simple", "Present perfect"], [
                ["<strong>I saw her yesterday.</strong>", "I have seen her twice this week."],
                ["<strong>We moved house in 2019.</strong>", "We have lived here for years."],
                ["<strong>She called me two hours ago.</strong>", "<strong>I have known him for years.</strong>"],
                ["<strong>I went to London last year.</strong>", "I have been to London three times."],
                ["<strong>When did you arrive?</strong>", "How long have you been here?"],
            ])),
            ("kader", "<em>I have been to London <strong>last year</strong></em> is fout: last year is een "
                      "afgelopen tijd. En <strong>when</strong> als vraagwoord vraagt naar een precies moment, "
                      "dus <em>when <strong>did</strong> you arrive?</em>, nooit <em>when have you "
                      "arrived?</em>"),
        ]),
        dict(kop="De present perfect continuous", blokken=[
            ("p", "De vorm is <strong>have of has been</strong> plus de <strong>-ing</strong>-vorm: <em>I "
                  "<strong>have been</strong> waiting</em>, <em>they have <strong>been</strong> working all "
                  "morning</em>."),
            ("p", "Hij benadrukt <strong>hoelang het al duurt</strong> of de <strong>bezigheid</strong> zelf, "
                  "terwijl de simple vorm het <strong>resultaat</strong> telt."),
            ("p", tabel(["Continuous: de bezigheid", "Simple: het resultaat"], [
                ["<strong>I have been waiting for an hour.</strong>", "I have waited long enough."],
                ["<strong>I have been gardening</strong> (vandaar mijn vuile handen).", "I have gardened three times this week."],
                ["<strong>It has been raining</strong> (de straat is nog nat).", "It has rained twice today."],
                ["<strong>How long have you been learning English?</strong>", "How much have you learnt?"],
            ])),
            ("p", "Ook hier gelden de werkwoorden van toestand: <em>I have been knowing her for years</em> is "
                  "fout, het moet <em>I have <strong>known</strong> her for years</em> zijn."),
        ]),
        luister("luister naar een Engelstalig interview en tel hoe vaak je have of has hoort. "
                "Gaat het telkens over iets dat nu nog meetelt?"),
    ],
    onthoud=[
        "There is bij enkelvoud en bij ontelbaar, there are bij meervoud. Bij een opsomming telt het eerste woord.",
        "Present simple voor gewoontes en feiten. Derde persoon: watches, flies, goes, does.",
        "In een vraag of ontkenning neemt does de s over: does she live here, she doesn't live here.",
        "Present continuous: am, is of are plus -ing. Writing, lying, sitting, beginning.",
        "De present continuous kan ook een vaste afspraak voor later zijn: we are meeting at six.",
        "Know, believe, want, like, understand en belong gaan niet in de -ing-vorm.",
        "Present perfect: have of has plus het voltooid deelwoord. Na have komt eaten, niet ate.",
        "Ik woon sinds 2020 in Antwerpen wordt I have lived in Antwerp since 2020.",
        "Since noemt het beginmoment, for de duur: since Monday, for two hours.",
        "Just en already staan tussen have en het deelwoord, yet achteraan in een vraag of ontkenning.",
        "Yesterday, in 2019, ago en last year vragen de past simple.",
        "When did you arrive, nooit when have you arrived.",
        "Present perfect continuous: have of has been plus -ing. Hij benadrukt de duur of de bezigheid.",
        "I have been gardening toont de sporen; I have gardened three times telt het resultaat.",
        "I have been knowing bestaat niet: het is I have known her for years.",
    ],
)


# ───────────────────────── 11. De verleden en de toekomende tijden
BUNDELS["de-verleden-en-de-toekomende-tijden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De verleden en de toekomende tijden",
    onder="De past simple met haar onregelmatige werkwoorden, de past continuous, de past perfect, en het verschil tussen will en going to.",
    secties=[
        dict(kop="De past simple", blokken=[
            ("p", "Bij een <strong>regelmatig</strong> werkwoord zet je er <strong>-ed</strong> achter: work → "
                  "worked, play → played."),
            ("p", tabel(["Spelling", "Voorbeeld"], [
                ["er stond al een e", "like → <strong>liked</strong>"],
                ["y na een medeklinker wordt i", "<strong>study → studied</strong>, try → tried, carry → carried"],
                ["korte klinker + medeklinker verdubbelt", "<strong>stop → stopped</strong>, travel → <strong>travelled</strong> (Brits)"],
            ])),
            ("p", "Bij een <strong>onregelmatig</strong> werkwoord leer je <strong>drie vormen</strong>: de "
                  "basisvorm, de verleden tijd en het voltooid deelwoord. Die derde heb je nodig na have en had."),
            ("p", tabel(["Basisvorm", "Verleden tijd", "Voltooid deelwoord"], [
                ["go", "<strong>went</strong>", "<strong>gone</strong>"],
                ["see", "<strong>saw</strong>", "<strong>seen</strong>"],
                ["take", "<strong>took</strong>", "<strong>taken</strong>"],
                ["write", "<strong>wrote</strong>", "<strong>written</strong>"],
                ["<strong>buy</strong>", "<strong>bought</strong>", "bought"],
                ["bring / think", "brought / thought", "brought / thought"],
                ["drink", "<strong>drank</strong>", "<strong>drunk</strong>"],
                ["read", "read (klinkt als red)", "read"],
            ])),
            ("kader", "In een <strong>vraag</strong> of een <strong>ontkenning</strong> gebruik je "
                      "<strong>did</strong>, en blijft het werkwoord in de <strong>basisvorm</strong>: <em>Did "
                      "you <strong>go</strong> to the party?</em>, <em>She <strong>didn't come</strong> "
                      "yesterday.</em> De verleden tijd zit al in did. Behalve bij <strong>to be</strong>: daar "
                      "heb je geen did nodig, <em><strong>were</strong> you there?</em> I, he, she en it nemen "
                      "<strong>was</strong>; you, we en <strong>they</strong> nemen <strong>were</strong>."),
            ("p", "<strong>Used to</strong> zegt dat iets <strong>vroeger gewoonte</strong> was en nu niet meer: "
                  "<em>I used to play the piano.</em> De ontkenning is <em>I didn't <strong>use</strong> to</em>, "
                  "zonder d."),
        ]),
        dict(kop="De past continuous", blokken=[
            ("p", "De vorm is <strong>was of were</strong> plus <strong>-ing</strong>. Hij beschrijft iets dat "
                  "<strong>aan de gang</strong> was."),
            ("p", tabel(["Zin", "Wat er gebeurt"], [
                ["<strong>I was reading when the phone rang.</strong>", "de lange handeling in de past continuous, de korte die erdoorheen komt in de past simple"],
                ["<strong>While we were waiting, it started to rain.</strong>", "na <strong>while</strong> staat de langst durende handeling, na <strong>when</strong> de korte"],
                ["<strong>She was cooking while he was setting the table.</strong>", "twee keer continuous: allebei tegelijk bezig"],
                ["<strong>The sun was shining and the birds were singing.</strong>", "het decor van een verhaal"],
            ])),
            ("p", "In een vraag wisselen <em>were</em> en het onderwerp van plaats: <em><strong>What were you "
                  "doing</strong> at eight o'clock?</em> En ook hier geldt de regel van de toestandswerkwoorden: "
                  "<em>I was knowing the answer</em> is fout, het moet <em>I <strong>knew</strong> the "
                  "answer</em> zijn."),
            ("weetje", "Woorden als <strong>yesterday</strong>, <em>last week</em> en <em>ago</em> verraden "
                       "meteen dat je de past simple nodig hebt. Since, already en yet horen bij de present "
                       "perfect."),
        ]),
        dict(kop="De past perfect", blokken=[
            ("p", "De vorm is <strong>had</strong> plus het <strong>voltooid deelwoord</strong>, voor elke "
                  "persoon hetzelfde. Hij zegt wat er <strong>nog vroeger</strong> gebeurde dan de rest van het "
                  "verhaal: <em>The train <strong>had already left</strong> when we arrived.</em>"),
            ("p", "Twee momenten in het verleden: het <strong>oudste</strong> krijgt de past perfect. <em>By the "
                  "time she called, I <strong>had</strong> already gone to bed.</em> En <em>When I got home, my "
                  "brother had cooked dinner</em> betekent dat <strong>hij eerst kookte en ik daarna "
                  "thuiskwam</strong>."),
            ("p", tabel(["Terecht past perfect", "Waarom"], [
                ["She had never seen the sea before that trip.", "voor dat latere moment"],
                ["They had finished the test before the bell rang.", "voor de bel"],
                ["I had left my key at home, so I could not get in.", "de oorzaak lag eerder"],
                ["<strong>Yesterday I walked to school.</strong>", "geen tweede moment om mee te vergelijken: gewoon past simple"],
            ])),
            ("kader", "Na <strong>after</strong> en <strong>before</strong> is de past perfect vaak "
                      "<strong>overbodig</strong>, want die woorden zeggen zelf al wat eerst kwam. <em>After she "
                      "finished, she went home</em> leest even helder als <em>after she had finished</em>."),
        ]),
        dict(kop="De toekomst: will en going to", blokken=[
            ("p", tabel(["Vorm", "Wanneer", "Voorbeeld"], [
                ["<strong>will</strong> + basisvorm", "een beslissing op het moment zelf, een belofte, een aanbod, een gok",
                 "<em>That bag looks heavy. <strong>I'll help you.</strong></em> / <em>I promise I <strong>won't</strong> tell anyone.</em>"],
                ["<strong>going to</strong>", "een plan dat je al had, of een voorspelling met bewijs",
                 "<em>I'm going to study medicine.</em> / <em>Look at those clouds, <strong>it is going to rain</strong>.</em>"],
                ["present continuous", "een afspraak die vastligt", "<em>We are meeting at six.</em>"],
                ["present simple", "een dienstregeling", "<em>The train leaves at six tomorrow.</em>"],
                ["<strong>will be</strong> + -ing", "iets dat op een bepaald moment bezig zal zijn", "<em>This time tomorrow I will be flying to Dublin.</em>"],
            ])),
            ("p", "Na <strong>will</strong> komt de <strong>kale basisvorm</strong>, zonder to, en will krijgt "
                  "zelf nooit een s: <em>she will come</em>. De korte vorm van will not is "
                  "<strong>won't</strong>. In een vraag wisselen will en het onderwerp van plaats: <em>Where "
                  "<strong>will you be</strong> next week?</em>"),
            ("p", "Twee modale werkwoorden na elkaar kan niet. Voor de toekomst van can gebruik je "
                  "<strong>will be able to</strong>: <em>She <strong>won't be able to</strong> come "
                  "tomorrow.</em>"),
            ("kader", "Na <strong>if</strong> en <strong>when</strong> zet je <strong>geen will</strong>: <em>I "
                      "will call you when I <strong>arrive</strong></em>, <em><strong>If it rains</strong>, we "
                      "<strong>will</strong> stay at home.</em> De will hoort in de hoofdzin, niet in de bijzin."),
            ("p", "<strong>Shall</strong> komt in het moderne Engels vooral voor in vragen: <em>Shall I open the "
                  "window?</em>, <em>Shall we go?</em> Die bieden iets aan of stellen iets voor. Voor de gewone "
                  "toekomst gebruikt men will."),
        ]),
        luister("kijk naar de trailer van een Engelstalige film en let op de tijden: hoor je will, going to of "
                "een verleden tijd? Vertel daarna in drie zinnen waar de film over gaat."),
    ],
    onthoud=[
        "Regelmatig: worked, liked, studied, stopped, travelled.",
        "Onregelmatig: go went gone, see saw seen, take took taken, write wrote written, buy bought bought, drink drank drunk.",
        "In een vraag of ontkenning gebruik je did plus de basisvorm: didn't come, did you go.",
        "To be heeft geen did nodig: were you there? Was bij I, he, she en it; were bij you, we en they.",
        "Used to zegt dat iets vroeger gewoonte was. Ontkenning: I didn't use to.",
        "Past continuous: was of were plus -ing. De lange handeling continuous, de korte simple.",
        "Na while de lange handeling, na when de korte. Twee keer continuous is tegelijk bezig.",
        "Yesterday, last week en ago vragen de past simple.",
        "Past perfect: had plus het deelwoord, voor wat nog vroeger gebeurde.",
        "Na after en before is de past perfect vaak overbodig.",
        "Will voor een beslissing op het moment zelf, een belofte of een aanbod. Going to voor een plan of een voorspelling met bewijs.",
        "Na will komt de kale basisvorm en will krijgt nooit een s. Won't is will not.",
        "Twee modale werkwoorden na elkaar kan niet: will be able to.",
        "Na if en when geen will: if it rains, we will stay at home.",
        "Shall komt vooral voor in vragen: shall I open the window?",
    ],
)


# ───────────────────────── 12. Modal auxiliaries, imperative en infinitive
BUNDELS["modal-auxiliaries-imperative-en-infinitive-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Modal auxiliaries, imperative en infinitive",
    onder="Can, may, must en should, de gebiedende wijs, de infinitief met en zonder to, de nadrukkelijke do en de onpersoonlijke zinnen.",
    secties=[
        dict(kop="De modale hulpwerkwoorden", blokken=[
            ("p", "Modale hulpwerkwoorden hebben een <strong>grote invloed op de interpretatie</strong> van een "
                  "zin. Eén woord verandert een vraag in een bevel, of een verbod in een vrije keuze."),
            ("p", "Twee vormregels gelden voor allemaal. Ze krijgen <strong>nooit een s</strong> in de derde "
                  "persoon (<em>she can</em>, niet she cans), en er komt <strong>geen to</strong> achter "
                  "(<em>she can swim</em>, niet she can to swim). <strong>Ought to</strong> is de enige "
                  "uitzondering, dat heeft zijn to al vast."),
            ("p", tabel(["Werkwoord", "Wat het doet", "Voorbeeld"], [
                ["<strong>can</strong>", "kunnen, en in spreektaal ook toestemming vragen", "<em>she can swim</em>, <em>can I go now?</em>"],
                ["<strong>could</strong>", "beleefder dan can", "<em><strong>Could you help me, please?</strong></em>"],
                ["<strong>may</strong>", "toestemming, formeel, en mogelijkheid", "<em><strong>May I leave early today?</strong></em>, <em>she may be at home</em>"],
                ["<strong>might</strong>", "mogelijkheid, iets onzekerder", "<em>it <strong>might</strong> rain tomorrow</em>"],
                ["<strong>must</strong>", "verplichting, of een sterke conclusie", "<em>you must wear a helmet</em>, <em>he <strong>must</strong> be exhausted</em>"],
                ["<strong>have to</strong>", "verplichting die van een regel komt", "<em>you have to wear a helmet here</em>"],
                ["<strong>should</strong> / <strong>ought to</strong>", "advies", "<em><strong>You should see a doctor.</strong></em>"],
                ["<strong>would rather</strong>", "liever", "<em><strong>I would rather stay home.</strong></em>"],
            ])),
            ("kader", "<strong>Mustn't</strong> en <strong>don't have to</strong> zijn bijna elkaars tegendeel. "
                      "<em>You <strong>mustn't</strong> park here</em> betekent dat <strong>hier parkeren "
                      "verboden is</strong>. <em>You <strong>don't have to</strong> come</em> betekent dat je "
                      "<strong>niet hoeft te komen</strong>, maar mag."),
            ("p", "<strong>Must</strong> heeft <strong>geen eigen verleden tijd</strong>. <em>I must go</em> "
                  "wordt in het verleden <strong>I had to go</strong>."),
        ]),
        dict(kop="Mogelijkheid en conclusie", blokken=[
            ("p", "Dezelfde woorden zeggen soms iets over hoe <strong>zeker</strong> je bent. <em>She "
                  "<strong>may</strong> be at home</em>, <em>she <strong>might</strong> call later</em> en "
                  "<em>it <strong>could</strong> be true</em> drukken een <strong>mogelijkheid</strong> uit."),
            ("p", "<em>She <strong>must</strong> be at home</em> is geen verplichting maar een sterke "
                  "<strong>conclusie</strong>: het zal wel zo zijn. <em>He's been running for an hour, he "
                  "<strong>must</strong> be exhausted.</em> De ontkenning daarvan is <strong>can't</strong>: "
                  "<em>That <strong>can't</strong> be true</em> betekent dat het <strong>onmogelijk waar kan "
                  "zijn</strong>. <em>Mustn't</em> zou daar fout zijn, want dat is een verbod."),
            ("p", "Wil je zeggen wat je <strong>achteraf bekeken beter had gedaan</strong>, dan gebruik je "
                  "<strong>should have</strong> plus het deelwoord: <em><strong>You should have done your "
                  "homework.</strong></em>"),
        ]),
        dict(kop="De gebiedende wijs", blokken=[
            ("p", "De <strong>imperatief</strong> is de <strong>kale basisvorm</strong>, zonder onderwerp en "
                  "zonder to: <em>close the door</em>. Ontkennend wordt het <strong>don't</strong> plus de "
                  "basisvorm: <em>don't open the window</em>, ook als je iemand met u aanspreekt."),
            ("p", "Stel je iets voor aan jezelf en je vrienden, dan gebruik je <strong>let's</strong>, de korte "
                  "vorm van let us: <em><strong>Let's</strong> go to the cinema tonight.</em>"),
            ("kader", "De imperatief is <strong>niet altijd onbeleefd</strong>. Hij staat gewoon in instructies "
                      "en recepten: <em>mix the eggs</em>, <em>turn left</em>. Met <strong>please</strong> erbij "
                      "klinkt hij vriendelijk: <em>please sit down</em>, nooit <em>please to sit down</em>."),
        ]),
        dict(kop="De infinitief", blokken=[
            ("p", "De <strong>infinitief</strong> is de <strong>basisvorm</strong>, vaak met <strong>to</strong> "
                  "ervoor: to go, to be, to write. Zonder to heet hij de <strong>kale infinitief</strong>."),
            ("p", tabel(["Na wat", "Welke vorm", "Voorbeeld"], [
                ["<strong>want</strong>, <strong>decide</strong>, <strong>hope</strong>, need, would like", "infinitief <strong>met to</strong>", "<em>I want to go</em>, <em>I need to go</em>"],
                ["<strong>let</strong>, <strong>make</strong>, en de modale werkwoorden", "<strong>kale</strong> infinitief", "<em><strong>She made me laugh.</strong></em>, <em>let him go</em>"],
                ["<strong>enjoy</strong>, finish, avoid, mind", "de <strong>-ing</strong>-vorm", "<em>I enjoy <strong>reading</strong> books</em>"],
                ["een <strong>voorzetsel</strong>", "de <strong>-ing</strong>-vorm", "<em>he left without saying goodbye</em>, <em>she is good at drawing</em>"],
            ])),
            ("kader", "<em>I look forward <strong>to hearing</strong> from you</em> is juist, en <em>I look "
                      "forward to hear from you</em> is fout. De <strong>to</strong> in <em>look forward "
                      "to</em> is een <strong>voorzetsel</strong> en geen infinitief, dus komt er een -ing-vorm "
                      "achter. Het is een van de gewoonste afsluiters van een formele mail, dus die wil je "
                      "juist hebben."),
            ("p", "<strong>Need</strong> is een gewoon werkwoord en neemt to, maar als hulpwerkwoord in een "
                  "ontkenning kan het kaal: <em>you <strong>needn't</strong> worry</em>."),
        ]),
        dict(kop="De nadrukkelijke do", blokken=[
            ("p", "In een <strong>bevestigende</strong> zin kunnen <strong>do</strong>, <strong>does</strong> en "
                  "<strong>did</strong> <strong>nadruk</strong> leggen. De zin kan ook zonder, en precies daarom "
                  "hoor je de klemtoon."),
            ("p", tabel(["Zin", "Wat je ermee zegt"], [
                ["<strong>I do like your new coat.</strong>", "ik vind je nieuwe jas echt mooi"],
                ["<strong>Do sit down.</strong>", "ga toch zitten"],
                ["<strong>She does look tired.</strong>", "ze ziet er wel degelijk moe uit"],
                ["<strong>I did tell you, honestly.</strong>", "ik heb het je wél gezegd"],
                ["Do you want tea?", "gewone vraag, geen nadruk"],
                ["<strong>I do believe you, really.</strong>", "ik geloof je echt"],
            ])),
        ]),
        dict(kop="Wederkerende en onpersoonlijke werkwoorden", blokken=[
            ("p", "Een paar Engelse werkwoorden zijn <strong>wederkerend</strong> terwijl wij ze gewoon "
                  "gebruiken: <strong>enjoy yourself</strong> (<em>Enjoy yourself at the party!</em>), "
                  "<strong>help yourself</strong> en <strong>behave yourself</strong>. Omgekeerd is "
                  "<strong>wash</strong> in het Engels juist <strong>niet</strong> wederkerend: wij zeggen zich "
                  "wassen, het Engels zegt <em>she washed</em>."),
            ("p", "Een Engelse zin heeft <strong>altijd een onderwerp</strong> nodig, behalve de imperatief. Is "
                  "er niets te noemen, dan zet je <strong>it</strong> of <strong>there</strong>. Dat heet een "
                  "<strong>onpersoonlijk</strong> onderwerp: het verwijst nergens naar."),
            ("p", tabel(["Zin", "Waarom onpersoonlijk"], [
                ["<strong>It is raining.</strong>", "de it verwijst nergens naar"],
                ["<strong>It was snowing all night.</strong>", "idem"],
                ["<strong>It seems that he is right.</strong>", "idem"],
                ["<strong>It takes an hour to get there.</strong>", "idem, en take krijgt hier wel een s"],
                ["<strong>There is no milk left.</strong>", "there vult de plaats van het onderwerp"],
                ["He is right about that.", "hier verwijst he wél naar een echte persoon"],
            ])),
            ("p", "Zo ook in <em>it is cold</em> en <em>it is five o'clock</em>."),
        ]),
        luister("vraag iemand in het Engels om iets te doen, op drie manieren: met can, met could en met would "
                "you mind. Luister naar het verschil in toon."),
    ],
    onthoud=[
        "Een modaal hulpwerkwoord krijgt nooit een s en er volgt geen to: she can swim. Ought to is de uitzondering.",
        "Could klinkt beleefder dan can; may is formeler dan can bij toestemming.",
        "Mustn't is een verbod, don't have to betekent dat het niet hoeft.",
        "Must heeft geen verleden tijd: I had to go.",
        "Should en ought to geven advies; should have plus deelwoord zegt wat je beter had gedaan.",
        "May, might en could drukken een mogelijkheid uit; must be is een conclusie en can't be het tegendeel.",
        "Would rather betekent liever, met de kale basisvorm erachter.",
        "Twee modale werkwoorden na elkaar kan niet: won't be able to.",
        "De imperatief is de kale basisvorm zonder onderwerp; ontkennend met don't. Let's is let us.",
        "De imperatief is niet onbeleefd: please sit down, nooit please to sit down.",
        "Want, decide en hope nemen to; let, make en de modale werkwoorden nemen de kale infinitief.",
        "Na enjoy, finish, avoid en mind komt -ing, en na elk voorzetsel ook.",
        "I look forward to hearing from you, want die to is een voorzetsel.",
        "Do, does en did kunnen in een bevestigende zin nadruk leggen: I do like your new coat.",
        "Enjoy yourself, help yourself en behave yourself zijn wederkerend; wash is dat niet.",
        "Een Engelse zin heeft altijd een onderwerp: it is raining, it takes an hour, there is no milk left.",
    ],
)


# ───────────────────────── 13. Zinsdelen, soorten zinnen en bijzinnen
BUNDELS["zinsdelen-soorten-zinnen-en-bijzinnen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zinsdelen, soorten zinnen en bijzinnen",
    onder="De bouwstenen van een Engelse zin, de vaste woordvolgorde, de vijf soorten zinnen, de voegwoorden en de conditionals zero en first.",
    secties=[
        dict(kop="De zinsdelen", blokken=[
            ("p", tabel(["Zinsdeel", "Hoe je het vindt", "Voorbeeld"], [
                ["<strong>onderwerp</strong> (subject)", "wie of wat doet de persoonsvorm?", "<em><strong>My little sister</strong> reads three books a week.</em>"],
                ["<strong>persoonsvorm</strong> (finite verb)", "welk werkwoord verandert mee met het onderwerp?", "<em>The children <strong>were</strong> playing outside.</em>"],
                ["<strong>lijdend voorwerp</strong> (direct object)", "wat ondergaat de handeling?", "<em>She wrote <strong>a long letter</strong>.</em>"],
                ["<strong>meewerkend voorwerp</strong> (indirect object)", "voor wie of aan wie?", "<em>He gave <strong>his friend</strong> a present.</em>"],
            ])),
            ("p", "Staat het meewerkend voorwerp <strong>achter</strong> het lijdend voorwerp, dan komt er "
                  "<strong>to</strong> of <strong>for</strong> voor: <em>he gave a present <strong>to</strong> "
                  "his friend</em>, <em>she sent a card to him</em>. Zonder voorzetsel staat het meewerkend "
                  "voorwerp eerst: <em>she sent him a card</em>."),
            ("weetje", "In <em>The children <strong>were</strong> playing outside</em> is <em>were</em> de "
                       "persoonsvorm en <em>playing</em> niet: playing verandert niet mee als je het onderwerp "
                       "verandert."),
        ]),
        dict(kop="De woordvolgorde", blokken=[
            ("p", "De gewone volgorde in een mededelende zin is <strong>onderwerp, persoonsvorm, rest</strong>, "
                  "en het Engels houdt die veel strenger vast dan het Nederlands."),
            ("p", "Zet je een bepaling vooraan, dan wisselen het onderwerp en de persoonsvorm "
                  "<strong>niet</strong> van plaats: <em><strong>Yesterday I went home.</strong></em> Het "
                  "Nederlands doet dat wel, en dat is de fout die je het vaakst hoort."),
            ("p", "Zet <strong>nooit iets tussen het werkwoord en zijn lijdend voorwerp</strong>: <em>I like "
                  "<strong>this film very much</strong></em>, niet <em>I like very much this film</em>."),
            ("kader", "De bepalingen achteraan staan in de volgorde <strong>hoe, waar, wanneer</strong>: "
                      "<em>She sang <strong>beautifully at the concert last night</strong>.</em> Het Nederlands "
                      "doet het net omgekeerd, en daarom klinkt een letterlijke vertaling altijd vreemd."),
        ]),
        dict(kop="De vijf soorten zinnen", blokken=[
            ("p", tabel(["Soort", "Hoe hij eruitziet", "Voorbeeld"], [
                ["mededelend", "onderwerp, persoonsvorm, rest", "<em>She plays tennis.</em>"],
                ["<strong>ontkennend</strong>", "met don't, doesn't of didn't, of met een hulpwerkwoord", "<em><strong>She doesn't want to go.</strong></em>"],
                ["<strong>vragend</strong>", "hulpwerkwoord vooraan", "<em><strong>Does she play tennis?</strong></em>"],
                ["bevelend", "kale basisvorm, geen onderwerp", "<em>Close the door.</em>"],
                ["<strong>uitroepend</strong>", "<strong>What a</strong> + naamwoord, of <strong>How</strong> + bijvoeglijk naamwoord", "<em><strong>What a beautiful garden!</strong></em>, <em>How lovely!</em>"],
            ])),
            ("p", "Bij een uitroep <strong>draait de volgorde niet om</strong>: <em>How fast she runs!</em>, "
                  "<em>What a mess!</em> Zodra er een vraagteken staat en de volgorde wél omdraait, heb je een "
                  "gewone vraag: <em>How do you do it?</em>"),
            ("p", "Staat er al een <strong>hulpwerkwoord</strong> in de zin, dan heb je voor een vraag "
                  "<strong>geen do</strong> nodig: <em>Is she coming?</em>, <em>Have you finished?</em>, "
                  "<em>Can he swim?</em> Het hulpwerkwoord schuift gewoon naar voren."),
            ("p", "Een <strong>aanhangvraag</strong> keert om: is de zin bevestigend, dan is de aanhangvraag "
                  "ontkennend. <em>You're coming tonight, <strong>aren't you</strong>?</em> en <em>You aren't "
                  "coming, are you?</em>"),
        ]),
        dict(kop="Congruentie", blokken=[
            ("p", "<strong>Congruentie</strong> betekent dat het werkwoord zich aanpast aan het onderwerp. Twee "
                  "onderwerpen samen zijn meervoud: <em>My brother and I <strong>are</strong> going out.</em>"),
            ("p", tabel(["Zin", "Waarom"], [
                ["<strong>The news is good.</strong>", "news eindigt op s maar is enkelvoud"],
                ["<strong>Everybody was there.</strong>", "onbepaalde voornaamwoorden zijn enkelvoud"],
                ["<strong>The police are looking for him.</strong>", "police staat in het Engels altijd in het meervoud"],
                ["<strong>One of my friends is coming tonight.</strong>", "het onderwerp is <em>one</em>, niet friends: kijk naar het woord vóór <em>of</em>"],
                ["My family is big.", "gewoner dan are, al mag are als je de leden apart bedoelt"],
            ])),
            ("kader", "Het Engels laat het onderwerp <strong>nooit</strong> weg, behalve bij de imperatief. "
                      "<em>Is raining today</em> bestaat niet: het moet <em><strong>It</strong> is raining "
                      "today</em> zijn."),
        ]),
        dict(kop="Nevenschikking en onderschikking", blokken=[
            ("p", "<strong>Nevenschikking</strong> knoopt <strong>twee zinnen van gelijke waarde</strong> aan "
                  "elkaar: allebei de delen kunnen alleen staan. <em>I called her <strong>and</strong> she "
                  "answered.</em> De nevenschikkende voegwoorden zijn <strong>and</strong>, "
                  "<strong>but</strong>, <strong>or</strong>, <strong>so</strong>, for en yet."),
            ("p", "<strong>Onderschikking</strong> hangt een <strong>bijzin</strong> onder een hoofdzin. Een "
                  "bijzin kan <strong>niet alleen staan</strong>: <em>because it was raining</em> is geen zin. "
                  "De onderschikkende voegwoorden zijn <strong>because</strong>, <strong>although</strong>, "
                  "<strong>unless</strong>, <strong>while</strong>, if, when, since en until."),
            ("p", tabel(["Voegwoord", "Wat het doet", "Voorbeeld"], [
                ["<strong>because</strong>", "de reden", "<em>I stayed at home <strong>because</strong> it was raining.</em>"],
                ["<strong>so</strong>", "het gevolg", "<em>It was raining, <strong>so</strong> I stayed at home.</em>"],
                ["<strong>but</strong> / <strong>yet</strong>", "een tegenstelling", "<em>She was tired, <strong>but</strong> she kept working.</em>"],
                ["<strong>although</strong>", "een tegenstelling, vooraan in een bijzin", "<em><strong>Although</strong> she was tired, she kept working.</em>"],
                ["<strong>unless</strong>", "if not", "<em><strong>Unless you hurry</strong>, you will miss the bus.</em>"],
            ])),
            ("kader", "<strong>Although</strong> en <strong>but</strong> zet je <strong>niet samen</strong> in "
                      "één zin. Eén tegenstelling volstaat. En <strong>unless</strong> bevat al een ontkenning, "
                      "dus daar komt er geen tweede bij."),
            ("p", "Komt de bijzin <strong>vooraan</strong>, dan staat de komma <strong>achter de "
                  "bijzin</strong>: <em>When I arrived, she was asleep.</em> Komt hij achteraan, dan valt de "
                  "komma meestal weg: <em>she was asleep when I arrived</em>."),
        ]),
        dict(kop="Betrekkelijke bijzinnen en de komma", blokken=[
            ("p", "Een <strong>betrekkelijke bijzin</strong> hangt aan een naamwoord vast en zegt er iets meer "
                  "over: <em>The man <strong>who lives next door</strong> is a nurse.</em> <em>This is the "
                  "house <strong>where</strong> we lived for ten years.</em>"),
            ("p", "Geeft de bijzin <strong>alleen extra informatie</strong>, dan zet je hem <strong>tussen "
                  "komma's</strong>: <em>My sister, <strong>who lives in Ghent</strong>, is a vet.</em> Beperkt "
                  "hij wie je bedoelt, dan geen komma's: <em>my sister who lives in Ghent</em> betekent dat je "
                  "<strong>meer dan één zus</strong> hebt."),
            ("kader", "Eén leesteken verandert de hele boodschap. <em>The students <strong>who worked "
                      "hard</strong> passed</em> zegt dat <strong>alleen de groep die hard werkte</strong> "
                      "slaagde. <em>The students, who worked hard, passed</em> zegt dat ze allemaal hard werkten "
                      "én allemaal slaagden."),
        ]),
        dict(kop="De conditionals zero en first", blokken=[
            ("p", tabel(["Soort", "Vorm", "Waarvoor", "Voorbeeld"], [
                ["<strong>zero</strong>", "if + present simple, <strong>present simple</strong>", "wat altijd waar is",
                 "<em>If you mix blue and yellow, you <strong>get</strong> green.</em>"],
                ["<strong>first</strong>", "if + present simple, <strong>will</strong>", "één echte mogelijkheid in de toekomst",
                 "<em>If you study hard, you <strong>will</strong> pass.</em>"],
            ])),
            ("p", "Meer voorbeelden van de <strong>zero</strong>: <em>If it rains, the streets get wet.</em> "
                  "<em>If you press this button, the light goes on.</em> Telkens gaat het over <strong>elke "
                  "keer</strong>, niet over één bepaalde keer."),
            ("p", "En van de <strong>first</strong>: <em>If it rains, we will stay at home.</em> <em>If I miss "
                  "the train, I will take the bus.</em> Die kijken naar één moment dat nog moet komen."),
            ("kader", "Na <strong>if</strong> zet je <strong>geen will</strong>: <em>if it will rain</em> is "
                      "fout. De will hoort in de <strong>hoofdzin</strong>. De hoofdzin mag ook vooraan staan, "
                      "en dan valt de komma weg: <em>we will stay at home if it rains</em>."),
            ("p", "Tot slot: wissel af tussen de soorten zinnen. Alleen maar korte hoofdzinnen leest hakkelend, "
                  "alleen maar lange samengestelde zinnen leest zwaar. Een <strong>verhaal wordt levendiger</strong> "
                  "van de afwisseling."),
        ]),
        luister("luister naar een Engelstalige stand-upcomedian of presentator en let op de zinslengte. "
                "Hoor je afwisseling tussen korte en lange zinnen?"),
    ],
    onthoud=[
        "Onderwerp, persoonsvorm, lijdend voorwerp en meewerkend voorwerp. Het meewerkend voorwerp achteraan krijgt to of for.",
        "De volgorde is onderwerp, persoonsvorm, rest, ook na een bepaling vooraan: yesterday I went home.",
        "Zet nooit iets tussen het werkwoord en zijn lijdend voorwerp: I like this film very much.",
        "Bepalingen achteraan: hoe, waar, wanneer.",
        "Vijf soorten zinnen: mededelend, ontkennend, vragend, bevelend en uitroepend.",
        "Uitroepend met What a + naamwoord of How + bijvoeglijk naamwoord, zonder omkering.",
        "Zonder hulpwerkwoord haal je do, does of did erbij; met hulpwerkwoord schuift dat naar voren.",
        "Aanhangvraag: bevestigend wordt ontkennend, en omgekeerd.",
        "The news is, everybody was, the police are, one of my friends is.",
        "Het Engels laat het onderwerp nooit weg, behalve bij de imperatief.",
        "Nevenschikkend: and, but, or, so. Onderschikkend: because, although, unless, while, if, when.",
        "Although en but niet samen in één zin. Unless betekent if not.",
        "Bijzin vooraan: komma erachter. Bijzin achteraan: meestal geen komma.",
        "Komma's rond een betrekkelijke bijzin betekenen extra informatie; zonder komma's beperkt hij wie je bedoelt.",
        "Conditional zero: if + present simple, present simple, voor wat altijd waar is.",
        "Conditional first: if + present simple, will, voor één mogelijkheid in de toekomst. Na if nooit will.",
    ],
)

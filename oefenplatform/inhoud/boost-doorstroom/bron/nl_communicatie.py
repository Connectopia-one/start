# -*- coding: utf-8 -*-
"""De vragen voor "Zender, ruis en de zeven tekstsoorten" (🚀 Boost doorstroom, Nederlands).

Uit allebei de vakfiches, want het communicatiemodel staat er in allebei:
zender, boodschap, ontvanger, kanaal, context, doel, effect en ruis, en de
zeven soorten lees- en luisterteksten.

Deel 1 is het communicatiemodel zelf, met het verschil tussen doel en effect en
tussen interne en externe ruis. Deel 2 zijn de zeven tekstsoorten, en vooral de
drie die op elkaar lijken: persuasief, opiniërend en argumentatief.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je bus is te laat. Je belt je leerkracht op om te zeggen dat je tien minuten later zal zijn. Wat is in dit voorbeeld het kanaal?",
        opties=[
            "het telefoongesprek",
            "de leerkracht die je opbelt",
            "de bus die vertraging heeft",
            "dat je tien minuten later zal zijn",
        ],
        antwoord=0,
        uitleg="Het kanaal is de weg die de boodschap aflegt. De leerkracht is de ontvanger, de vertraging is de context en de late aankomst is de boodschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen thuis in het communicatiemodel?",
        opties=["ruis", "kanaal", "effect", "rijmschema"],
        antwoord=[0, 1, 2],
        uitleg="Het model telt acht elementen: zender, boodschap, ontvanger, kanaal, context, doel, effect en ruis. Een rijmschema hoort bij poëzie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord alles wat een boodschap onderweg stoort?",
        antwoord="ruis",
        uitleg="Ruis is elke storing die maakt dat de boodschap niet of verkeerd aankomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke situatie is er sprake van interne ruis?",
        opties=[
            "Je bent moe en je hoort maar de helft van wat er gezegd wordt",
            "Er rijdt een luide brommer voorbij terwijl iemand aan het praten is",
            "De verbinding valt weg tijdens een videogesprek met je oma",
            "Het bericht komt aan met allerlei vreemde tekens erin",
        ],
        antwoord=0,
        uitleg="Interne ruis zit in de zender of de ontvanger zelf: moe zijn, verstrooid zijn, het onderwerp niet kennen. De drie andere storingen komen van buitenaf.",
    ),
    dict(
        type="waarofniet",
        vraag="Het doel van een boodschap en het effect ervan zijn altijd hetzelfde.",
        antwoord=False,
        uitleg="Het doel is wat de zender wil bereiken, het effect is wat er werkelijk gebeurt. Een campagne die jou vooral doet lachen, mist haar doel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met de context van een boodschap?",
        opties=[
            "de situatie waarin de boodschap verstuurd en gelezen wordt",
            "de woorden die de zender precies gekozen heeft",
            "het gevoel dat de ontvanger achteraf overhoudt",
            "de drager waarlangs de boodschap verstuurd wordt",
        ],
        antwoord=0,
        uitleg="Context is de omringende situatie: de plaats, het moment, de relatie tussen zender en ontvanger. Het laatste antwoord beschrijft het kanaal.",
    ),
    dict(
        type="invultekst",
        vraag="Het middel waarlangs een boodschap verstuurd wordt, mail, telefoon of blog, heet het ___.",
        antwoord=["kanaal", "het kanaal"],
        uitleg="Het kanaal is de drager. Dezelfde boodschap via een ander kanaal komt vaak heel anders over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze storingen zijn externe ruis?",
        opties=[
            "lawaai op straat tijdens een gesprek",
            "een slechte verbinding bij een videogesprek",
            "een vlek over de tekst van een brief",
            "je gedachten die alsmaar afdwalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Externe ruis komt van buiten de zender en de ontvanger. Afdwalende gedachten zitten in de ontvanger zelf en zijn dus interne ruis.",
    ),
    dict(
        type="waarofniet",
        vraag="De zender van een reclamefilmpje is het bedrijf dat het product wil verkopen.",
        antwoord=True,
        uitleg="De zender is wie de boodschap de wereld in stuurt. Bij reclame is dat de adverteerder, ook al zie je op het scherm alleen acteurs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stuurt eerst een spraakbericht en daarna dezelfde tekst als mail. Welk element van het communicatiemodel verandert daardoor?",
        opties=[
            "het kanaal",
            "de zender",
            "de boodschap",
            "de ontvanger",
        ],
        antwoord=0,
        uitleg="Dezelfde zender stuurt dezelfde boodschap naar dezelfde ontvanger, maar langs een andere weg. Die weg is het kanaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Dat een bericht nergens een auteur vermeldt, is een reden om aan de betrouwbaarheid te twijfelen.",
        antwoord=True,
        uitleg="Als je de zender niet kent, kan je niet nagaan of die deskundig is of wat die met het bericht wil bereiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een publireportage over een sportdrank ziet eruit als een gewoon artikel. Wat is het echte doel van de zender?",
        opties=[
            "je het drankje laten kopen",
            "je objectief informeren over sport",
            "je aan het lachen brengen met een grap",
            "je een verhaal vertellen over een atleet",
        ],
        antwoord=0,
        uitleg="Een publireportage is betaalde reclame in de vorm van een artikel. De vorm is informatief, het doel is verkopen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat een boodschap werkelijk teweegbrengt bij de ontvanger, heet het ___.",
        antwoord=["effect", "het effect"],
        uitleg="Het effect kan samenvallen met het doel, maar ook helemaal niet. Dat verschil is precies waarom die twee apart in het model staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bekijkt een filmpje dat uitlegt hoe je brood bakt. Wat is het doel van de zender?",
        opties=[
            "je stap voor stap iets leren doen",
            "je overtuigen om brood te kopen",
            "zijn mening over bakkers geven",
            "een verhaal over een bakkerij vertellen",
        ],
        antwoord=0,
        uitleg="Wie instructies geeft, wil dat je daarna zelf iets kan. Dat is een ander doel dan overtuigen, oordelen of vertellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je jezelf als je het communicatiemodel op een tekst toepast?",
        opties=[
            "Wie is de zender van deze tekst?",
            "Voor wie is de tekst bedoeld?",
            "Via welk kanaal is de tekst verspreid?",
            "Hoeveel strofen telt de tekst?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het aantal strofen hoort bij een gedicht analyseren, niet bij het communicatiemodel.",
    ),
    dict(
        type="waarofniet",
        vraag="Ruis zit altijd buiten de zender en de ontvanger.",
        antwoord=False,
        uitleg="Ruis kan ook intern zijn: hoofdpijn, verstrooidheid, of te weinig voorkennis over het onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand typt op een forum een heel bericht in hoofdletters. Hoe komt dat meestal over?",
        opties=[
            "als schreeuwerig en storend",
            "als heel beleefd en formeel",
            "als grappig en luchtig bedoeld",
            "als onzeker en voorzichtig",
        ],
        antwoord=0,
        uitleg="Hoofdletters zijn op het scherm een vorm van non-verbale communicatie. Ze worden gelezen als roepen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bericht zelf, los van wie het stuurt en wie het krijgt?",
        antwoord=["de boodschap", "boodschap"],
        uitleg="De boodschap is de inhoud. Zender en ontvanger staan eromheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een filmpje wil je doen stoppen met roken, maar jij vindt het vooral grappig. Wat besluit je daaruit?",
        opties=[
            "het effect wijkt af van het doel",
            "de zender is niet de maker van het filmpje",
            "het kanaal is verkeerd gekozen",
            "de boodschap bevat te weinig context",
        ],
        antwoord=0,
        uitleg="De zender wou je gedrag veranderen. Wat er werkelijk gebeurde, lachen, is het effect. Doel en effect lopen hier uit elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat 'context' apart in het communicatiemodel?",
        opties=[
            "omdat dezelfde zin in een andere situatie iets anders betekent",
            "omdat elke tekst een inleiding, midden en slot heeft",
            "omdat een boodschap altijd langs één kanaal reist",
            "omdat de zender de ontvanger meestal persoonlijk kent",
        ],
        antwoord=0,
        uitleg="'Doe de deur dicht' klinkt anders van een vriend dan van een directeur, en anders in de klas dan thuis. Die situatie is de context.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze teksten zijn prescriptief?",
        opties=[
            "een bijsluiter bij een geneesmiddel",
            "de veiligheidsvoorschriften in een bedrijf",
            "het schoolreglement",
            "een reisverslag van drie weken Peru",
        ],
        antwoord=[0, 1, 2],
        uitleg="Prescriptieve teksten schrijven voor hoe je iets doet of moet doen. Een reisverslag vertelt een verhaal en is narratief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een opiniërende en een argumentatieve tekst?",
        opties=[
            "een opiniërende tekst geeft vooral een oordeel, een argumentatieve bouwt het op",
            "een opiniërende tekst verschijnt altijd in een krant of tijdschrift",
            "een argumentatieve tekst is altijd langer dan een opiniërende tekst",
            "een argumentatieve tekst mag geen enkele mening van de schrijver bevatten",
        ],
        antwoord=0,
        uitleg="Allebei komt er een standpunt in voor. In een argumentatieve tekst, zoals een betoog of een pleidooi, is de opbouw met argumenten en tegenargumenten de kern.",
    ),
    dict(
        type="invultekst",
        vraag="Een reclamefilmpje wil je overtuigen of beïnvloeden. Hoe noemen we zo'n tekstsoort?",
        antwoord=["persuasief", "persuasieve"],
        uitleg="Persuasief komt van het Latijnse persuadere, overtuigen. Reclame, propaganda en campagnes horen erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recensie van een boek is een opiniërende tekst.",
        antwoord=True,
        uitleg="In een recensie geeft iemand zijn oordeel over een werk. Ook een hotelbeoordeling en een productreview horen daarbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een true crime podcast vertelt hoe een zaak zich afspeelde. Welke tekstsoort is dat?",
        opties=["narratief", "prescriptief", "persuasief", "argumentatief"],
        antwoord=0,
        uitleg="Narratieve teksten vertellen een verhaal, of dat nu een podcast, een vlog of een verhalend gedicht is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke tekstsoort hoort een pleidooi?",
        opties=["argumentatief", "narratief", "prescriptief", "informatief"],
        antwoord=0,
        uitleg="Een pleidooi, een betoog en een debat bouwen een standpunt op met argumenten. Dat is argumentatief.",
    ),
    dict(
        type="invultekst",
        vraag="Welk woord gebruiken we voor teksten die een verhaal vertellen?",
        antwoord=["narratief", "narratieve"],
        uitleg="Narratief komt van narrare, vertellen. Een reisverslag, een vlog en een true crime podcast zijn narratief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een publireportage reken je bij de informatieve teksten.",
        antwoord=False,
        uitleg="Een publireportage ziet eruit als informatie, maar wil je iets verkopen. Naar doel is hij dus persuasief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze teksten zijn literair?",
        opties=[
            "een gedicht over de zee",
            "een kortverhaal in een tijdschrift",
            "een stand-upcomedyvoorstelling",
            "de handleiding bij een wasmachine",
        ],
        antwoord=[0, 1, 2],
        uitleg="Literaire teksten hebben een esthetische waarde en spelen in op emoties. Een handleiding is prescriptief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een folder van een politieke partij vlak voor de verkiezingen. Welke tekstsoort?",
        opties=["persuasief", "informatief", "narratief", "prescriptief"],
        antwoord=0,
        uitleg="De folder wil je stem winnen. Hij geeft ook informatie, maar het doel is je beïnvloeden.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén tekst kan maar tot één tekstsoort behoren.",
        antwoord=False,
        uitleg="Teksten mengen vaak. Een reclamespot kan een verhaal vertellen en tegelijk willen verkopen. Je kijkt dan naar het hoofddoel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een reclametekst die eruitziet als een gewoon artikel?",
        antwoord="publireportage",
        uitleg="Een publireportage is betaalde reclame die de vorm van journalistiek aanneemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noem je een satirische nieuwssite geen informatieve tekst?",
        opties=[
            "omdat het doel is je te laten lachen, niet je te informeren",
            "omdat de artikels er veel te kort zijn om informatie te geven",
            "omdat er geen enkel waar gegeven in zo'n artikel staat",
            "omdat er nooit een auteur onder zo'n artikel vermeld wordt",
        ],
        antwoord=0,
        uitleg="Je kijkt naar het doel van de zender. Satire gebruikt de vorm van nieuws om te lachen met de werkelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn voorbeelden van narratieve teksten?",
        opties=[
            "een videoblog over een verhuis",
            "een reisverslag uit Noorwegen",
            "een verhalend gedicht",
            "een bijsluiter bij een zalf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alle drie vertellen ze iets wat gebeurd is. Een bijsluiter geeft instructies en is prescriptief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een strip kan een literaire tekst zijn.",
        antwoord=True,
        uitleg="Literatuur zit niet alleen in romans. Een strip, een lied of een graphic novel kan evengoed literair zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een instructiefilmpje waarin iemand toont hoe je een fietsband plakt. Welke tekstsoort?",
        opties=["prescriptief", "narratief", "opiniërend", "argumentatief"],
        antwoord=0,
        uitleg="Het filmpje schrijft voor wat je in welke volgorde doet. Dat is prescriptief, ook al is het beeld en geen tekst.",
    ),
    dict(
        type="invultekst",
        vraag="Welke tekstsoort geeft je instructies over hoe je iets doet?",
        antwoord=["prescriptief", "prescriptieve"],
        uitleg="Prescriptief betekent voorschrijvend: een recept, een handleiding, een reglement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een tekst eerder persuasief dan argumentatief?",
        opties=[
            "hij wil je vooral beïnvloeden, desnoods zonder sterke argumenten",
            "hij is bedoeld voor een heel groot publiek in plaats van een klein",
            "hij verschijnt op een scherm in plaats van op papier",
            "hij is geschreven door iemand met verstand van zaken",
        ],
        antwoord=0,
        uitleg="Persuasieve teksten zetten ook beelden, muziek en gevoel in. Argumentatieve teksten leunen op de redenering zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hotelbeoordeling op een reissite hoort bij welke tekstsoort?",
        opties=["opiniërend", "informatief", "prescriptief", "narratief"],
        antwoord=0,
        uitleg="De schrijver geeft zijn oordeel over het hotel. Dat is een mening, dus opiniërend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een interview met een wetenschapper in de krant hoort bij welke tekstsoort?",
        opties=["informatief", "persuasief", "prescriptief", "literair"],
        antwoord=0,
        uitleg="Een interview, een krantenartikel en een stukje uit een leerboek geven je informatie over een onderwerp.",
    ),
]

# -*- coding: utf-8 -*-
"""🌍 Beyond — Chemisch evenwicht.

Chemie, de kop "Chemisch evenwicht" uit de vakfiche natuurwetenschappen 3DO.
Deel 1 gaat over het verschil tussen een aflopende reactie, een chemisch
evenwicht en geen reactie, over het dynamische karakter van een evenwicht en
over het limiterend reagens en de overmaat. Deel 2 gaat helemaal over de wet
van Le Chatelier en Van 't Hoff en de vier verstoringen die de fiche noemt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is er typisch voor een aflopende reactie?",
        opties=[
            "minstens één reagens raakt volledig op",
            "de reagentia blijven allemaal gedeeltelijk over",
            "er ontstaat helemaal geen reactieproduct",
            "de heen- en terugreactie gaan even snel",
        ],
        antwoord=0,
        uitleg="Bij een aflopende reactie gaat de reactie door tot een reagens weg is. Blijven alle stoffen naast elkaar bestaan, dan heb je een evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken horen bij een chemisch evenwicht? Kruis alles aan wat juist is.",
        opties=[
            "de reagentia en de producten zijn allebei nog aanwezig",
            "de concentraties veranderen niet meer",
            "de heenreactie en de terugreactie gaan even snel",
            "er gebeurt op deeltjesniveau niets meer",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn precies wat een evenwicht is. Op deeltjesniveau gaat het wel door, in beide richtingen even snel, en daarom heet het dynamisch.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een evenwicht waarbij de heen- en terugreactie blijven doorgaan?",
        antwoord=["dynamisch evenwicht", "dynamisch chemisch evenwicht"],
        uitleg="Van buiten lijkt er niets te veranderen, want de concentraties blijven gelijk. Binnenin wordt er voortdurend product gevormd en weer afgebroken.",
    ),
    dict(
        type="waarofniet",
        vraag="In een chemisch evenwicht zijn de concentraties van reagentia en producten altijd aan elkaar gelijk.",
        antwoord=False,
        uitleg="Ze veranderen niet meer, maar ze mogen ver van elkaar liggen. Een evenwicht kan heel ver naar de productkant of naar de reagenskant liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet op een grafiek dat twee concentratielijnen eerst veranderen en daarna vlak naast elkaar doorlopen. Waarover gaat het?",
        opties=[
            "over een chemisch evenwicht",
            "over een aflopende reactie",
            "over een mengsel waarin niets reageert",
            "over een reactie met een katalysator",
        ],
        antwoord=0,
        uitleg="Er is iets gebeurd, want de lijnen veranderden eerst, en op het einde blijven beide stoffen over. Dat is precies het beeld van een evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mengt twee stoffen en de concentraties veranderen helemaal niet. Wat besluit je?",
        opties=[
            "er is geen reactie",
            "er is een aflopende reactie",
            "er is een chemisch evenwicht ontstaan",
            "de terugreactie gaat sneller dan de heenreactie",
        ],
        antwoord=0,
        uitleg="Bij een evenwicht veranderen de concentraties eerst wel en daarna niet meer. Veranderen ze van het begin af aan niet, dan gebeurt er niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een aflopende reactie blijft er van het reagens in overmaat nog over.",
        antwoord=True,
        uitleg="Het limiterend reagens raakt op en stopt de reactie. Wat van de andere stof nog niet gereageerd heeft, blijft gewoon in het mengsel staan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het reagens dat als eerste opgebruikt is en zo de reactie stopt?",
        antwoord=["limiterend reagens", "beperkend reagens"],
        uitleg="Dat reagens bepaalt hoeveel product je maximaal kan maken. Van de andere stof blijft er dan iets over, en die noem je in overmaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je in het labo nagaan of je met een evenwicht te doen hebt? Kruis alles aan wat juist is.",
        opties=[
            "nakijken of er op het einde nog van beide reagentia is",
            "iets toevoegen en kijken of er nog iets verandert",
            "nakijken of de reactie warmte of koude afgeeft",
            "nakijken hoe lang de reactie in totaal geduurd heeft",
        ],
        antwoord=[0, 1],
        uitleg="Blijven de reagentia naast de producten bestaan, dan is het een evenwicht. En een evenwicht reageert nog op een verstoring, een afgelopen reactie niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een snelheid-tijdgrafiek van een evenwicht staan de heen- en de terugreactie. Wat doen die twee lijnen?",
        opties=[
            "ze komen naar elkaar toe en lopen daarna samen verder",
            "ze zakken allebei tot op de horizontale as en blijven daar",
            "ze lopen van het begin tot het einde netjes parallel",
            "ze kruisen elkaar en lopen daarna weer van elkaar weg",
        ],
        antwoord=0,
        uitleg="De heenreactie zakt en de terugreactie stijgt tot ze gelijk zijn. Vanaf dat moment lopen ze als één vlakke lijn verder, want het evenwicht is dynamisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een evenwicht kan je ook van rechts naar links bereiken, dus vertrekkend van de producten.",
        antwoord=True,
        uitleg="Je komt dan bij dezelfde eindconcentraties uit als wanneer je van de reagentia vertrekt. Dat is een mooi bewijs dat het evenwicht in twee richtingen werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de snelheid van de heenreactie in de loop naar het evenwicht toe?",
        opties=[
            "ze daalt, want de reagentia raken op",
            "ze stijgt, want er komt meer product bij",
            "ze blijft van het begin tot het einde gelijk",
            "ze wordt nul zodra er product ontstaat",
        ],
        antwoord=0,
        uitleg="De heenreactie begint snel en wordt trager omdat er minder reagens is. De terugreactie begint bij nul en versnelt, tot de twee gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de twee snelheden in een evenwicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de heenreactie vertraagt onderweg naar het evenwicht",
            "de terugreactie versnelt onderweg naar het evenwicht",
            "in het evenwicht zijn beide snelheden gelijk",
            "in het evenwicht zijn beide snelheden nul",
        ],
        antwoord=[0, 1, 2],
        uitleg="De twee snelheden groeien naar elkaar toe en blijven daarna gelijk. Nul zijn ze niet, want het evenwicht is dynamisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Zodra een evenwicht bereikt is, worden er geen nieuwe productmoleculen meer gevormd.",
        antwoord=False,
        uitleg="Er worden er nog altijd gevormd, maar er verdwijnen er precies even veel. Daardoor blijft de concentratie onveranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mengt 2 mol van stof A met 5 mol van stof B, terwijl de reactie één op één verloopt. Welke stof is in overmaat?",
        opties=["stof B", "stof A", "geen van de twee", "beide stoffen"],
        antwoord=0,
        uitleg="A is na 2 mol op en is dus het limiterend reagens. Van B blijven er 3 mol staan, dus B is in overmaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het reagens waarvan er na de reactie nog overblijft?",
        antwoord=["overmaat", "reagens in overmaat"],
        uitleg="Dat is de stof waarvan je meer had dan nodig. Het andere reagens, het limiterende, bepaalt hoeveel product er maximaal kan ontstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het bij een proef soms handig om één reagens in overmaat te gebruiken?",
        opties=[
            "om zeker te zijn dat het andere reagens volledig reageert",
            "om de reactie-energie van de reactie kleiner te maken",
            "om de activeringsenergie van de reactie te doen zakken",
            "om van de reactie in het vat een evenwicht te maken",
        ],
        antwoord=0,
        uitleg="Met een overmaat kan het limiterend reagens niets anders dan opgebruikt worden. Zo haal je er zoveel product uit als mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het evenwicht van ijzerthiocyanaat is de oplossing bloedrood. Wat zegt die kleur?",
        opties=[
            "dat er een duidelijke hoeveelheid gekleurd product aanwezig is",
            "dat de reagentia allemaal volledig opgebruikt zijn",
            "dat de reactie van het begin af aan niet verlopen is",
            "dat de twee snelheden allebei tot nul gezakt zijn",
        ],
        antwoord=0,
        uitleg="Een kleur komt van een stof die licht opneemt, dus is die stof er. Wordt de kleur sterker of bleker, dan weet je in welke richting het evenwicht schuift.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kleurverandering is een handige manier om een verschuiving van een evenwicht te volgen.",
        antwoord=True,
        uitleg="Je ziet rechtstreeks of er meer of minder van de gekleurde stof is. Daarom gebruiken scheikundigen graag evenwichten met een gekleurde stof erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk beeld hoort bij een aflopende reactie op een concentratie-tijdgrafiek?",
        opties=[
            "de lijn van een reagens zakt tot op de horizontale as",
            "alle lijnen lopen op het einde vlak maar boven de as",
            "alle lijnen blijven van begin tot einde horizontaal",
            "de lijn van het product zakt naar de horizontale as",
        ],
        antwoord=0,
        uitleg="Nul betekent dat die stof helemaal weg is, dus was ze het limiterend reagens. Bij een evenwicht blijft elke lijn boven de as.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Hoe heet de wet die voorspelt in welke richting een evenwicht verschuift?",
        antwoord=["Le Chatelier", "LeChatelier"],
        uitleg="Ze heet voluit de wet van Le Chatelier en Van 't Hoff. Ze zegt dat een evenwicht een verstoring zoveel mogelijk tegenwerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Le Chatelier en Van 't Hoff?",
        opties=[
            "een evenwicht schuift zo op dat het de verstoring tegenwerkt",
            "een evenwicht schuift altijd naar de kant van de producten",
            "een evenwicht wordt door een verstoring een aflopende reactie",
            "een evenwicht verandert door een verstoring helemaal niet",
        ],
        antwoord=0,
        uitleg="Verhoog je iets, dan gaat het evenwicht dat juist verbruiken. Haal je iets weg, dan gaat het evenwicht dat bijmaken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voegt extra reagens toe aan een evenwicht. Welke kant kiest het evenwicht?",
        opties=[
            "de kant van de producten",
            "de kant van de reagentia",
            "geen van de twee kanten",
            "eerst links en daarna rechts",
        ],
        antwoord=0,
        uitleg="Het evenwicht werkt de verhoging tegen door dat extra reagens op te gebruiken. Dus verschuift het naar rechts en komt er meer product.",
    ),
    dict(
        type="waarofniet",
        vraag="Haal je product uit een evenwichtsmengsel weg, dan maakt het evenwicht nieuw product aan.",
        antwoord=True,
        uitleg="Het evenwicht werkt de daling tegen, dus schuift het naar rechts. Zo haal je uit een evenwicht toch veel product, door het steeds af te voeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verstoringen kunnen een evenwicht doen verschuiven? Kruis alles aan wat juist is.",
        opties=[
            "de concentratie van één stof veranderen",
            "het volume van het vat veranderen bij een gasevenwicht",
            "de temperatuur veranderen",
            "een katalysator toevoegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie veranderen de ligging van het evenwicht. Een katalysator versnelt heen- en terugreactie even sterk, dus komt het evenwicht enkel sneller tot stand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een katalysator met een chemisch evenwicht?",
        opties=[
            "het evenwicht wordt sneller bereikt, maar ligt niet anders",
            "het evenwicht verschuift naar de kant van de producten",
            "het evenwicht verschuift naar de kant van de reagentia",
            "het evenwicht wordt een aflopende reactie",
        ],
        antwoord=0,
        uitleg="Hij verlaagt de activeringsenergie van de heen- en de terugreactie even veel. Daarom veranderen de eindconcentraties niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een exo-energetisch evenwicht verschuift opwarmen het evenwicht naar links.",
        antwoord=True,
        uitleg="De heenreactie geeft warmte, dus werkt het evenwicht extra warmte tegen door de warmte-opnemende kant te kiezen. Dat is hier de terugreactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je koelt een evenwicht af waarvan de heenreactie exo-energetisch is. Wat gebeurt er?",
        opties=[
            "het evenwicht schuift naar rechts, want zo komt er warmte vrij",
            "het evenwicht schuift naar links, want zo wordt er warmte opgenomen",
            "het evenwicht blijft precies waar het was",
            "de katalysator in het mengsel wordt opgebruikt",
        ],
        antwoord=0,
        uitleg="Afkoelen is warmte wegnemen, dus werkt het evenwicht dat tegen door warmte te maken. Dat is bij een exo-energetische heenreactie de rechterkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gasevenwicht heeft links 3 mol gas en rechts 2 mol gas. Je perst het mengsel in een kleiner vat. Wat gebeurt er?",
        opties=[
            "het evenwicht schuift naar rechts, naar de kant met minder gasdeeltjes",
            "het evenwicht schuift naar links, naar de kant met meer gasdeeltjes",
            "het evenwicht blijft onveranderd, want er komt niets bij",
            "het evenwicht wordt een aflopende reactie naar rechts",
        ],
        antwoord=0,
        uitleg="Een kleiner volume betekent een hogere druk. Het evenwicht werkt dat tegen door naar de kant met het kleinste aantal gasdeeltjes te schuiven.",
    ),
    dict(
        type="invultekst",
        vraag="Waarnaar schuift een gasevenwicht als je de druk verhoogt: naar de kant met het kleinste of met het grootste aantal gasdeeltjes?",
        antwoord=["kleinste", "het kleinste"],
        uitleg="Minder gasdeeltjes nemen minder plaats, dus zakt de druk weer wat. Zo werkt het evenwicht de verhoging tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een volumeverandering verschuift elk gasevenwicht, ook als links en rechts hetzelfde aantal gasdeeltjes staan.",
        antwoord=False,
        uitleg="Staan er aan beide kanten even veel gasdeeltjes, dan helpt verschuiven niet tegen de druk. Dan blijft het evenwicht waar het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwijdert een reagens uit een evenwichtsmengsel. Wat zie je gebeuren?",
        opties=[
            "het evenwicht schuift naar links en er verdwijnt product",
            "het evenwicht schuift naar rechts en er komt product bij",
            "het evenwicht blijft precies hetzelfde liggen",
            "de terugreactie komt volledig tot stilstand",
        ],
        antwoord=0,
        uitleg="Het evenwicht werkt het verlies tegen door dat reagens bij te maken. Dat kan alleen door product terug af te breken, dus schuift het naar links.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voegt reagens toe aan een evenwicht. Wat gebeurt er met de snelheid van de heenreactie meteen na die toevoeging?",
        opties=[
            "die stijgt eerst en zakt daarna naar de nieuwe evenwichtswaarde",
            "die zakt eerst en stijgt daarna weer",
            "die blijft de hele tijd precies gelijk",
            "die wordt eerst nul en start daarna opnieuw",
        ],
        antwoord=0,
        uitleg="Meer reagens betekent meer botsingen, dus een snellere heenreactie. Terwijl het product aangroeit, versnelt de terugreactie tot de twee weer gelijk zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een verstoring komen de twee snelheden opnieuw op dezelfde waarde als voor de verstoring uit.",
        antwoord=False,
        uitleg="Ze worden wel weer aan elkaar gelijk, maar bij andere concentraties en dus op een andere hoogte. Dat is een nieuw evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een evenwicht met een bruin gas en een kleurloos gas wordt het mengsel bleker als je het afkoelt. Wat besluit je?",
        opties=[
            "de reactie naar het kleurloze gas geeft warmte af",
            "de reactie naar het bruine gas geeft warmte af",
            "de reactie is bij lage temperatuur een aflopende reactie",
            "er zit in het mengsel een katalysator die bruin wordt",
        ],
        antwoord=0,
        uitleg="Afkoelen doet het evenwicht de warmtegevende kant kiezen, en dat is hier de kleurloze kant. Daarom gaat de bruine kleur achteruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen zet je om uit een grafiek af te leiden welke factor een evenwicht verstoord heeft? Kruis alles aan wat juist is.",
        opties=[
            "kijken welke lijn als eerste plots verspringt",
            "kijken in welke richting de lijnen daarna evolueren",
            "kijken of alle lijnen op hetzelfde moment van richting veranderen",
            "kijken hoeveel gram product er in totaal ontstaan is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een plotse sprong in één lijn wijst op een toevoeging van die stof. Veranderen alle lijnen samen zonder sprong, dan gaat het eerder over temperatuur of volume.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verschuiving van een evenwicht naar rechts betekent dat de concentratie van alle producten stijgt.",
        antwoord=True,
        uitleg="Naar rechts schuiven betekent dat de heenreactie het overwicht krijgt. Dus groeien alle producten aan en zakken alle reagentia.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ingrepen gebruikt een fabriek om uit een evenwicht meer product te halen? Kruis alles aan wat juist is.",
        opties=[
            "het product onderweg uit het vat afvoeren",
            "extra reagens blijven toevoegen",
            "de temperatuur in de gunstige richting zetten",
            "het volume van het vat zo groot mogelijk maken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie schuiven het evenwicht echt naar rechts. Het volume helpt enkel als links en rechts een ander aantal gasdeeltjes staat, en dan niet zomaar in die richting.",
    ),
    dict(
        type="invultekst",
        vraag="Een evenwicht schuift naar de kant van de reagentia. Spreek je dan van een verschuiving naar links of naar rechts?",
        antwoord=["links", "naar links"],
        uitleg="De reagentia staan links in de reactievergelijking. Naar links schuiven betekent dus dat de terugreactie het overwicht heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voegt extra reagens toe aan een evenwicht waarvan het product gekleurd is. Wat zie je aan de kleur?",
        opties=[
            "de kleur wordt sterker",
            "de kleur wordt bleker",
            "de kleur verdwijnt volledig",
            "de kleur slaat om naar een andere kleur",
        ],
        antwoord=0,
        uitleg="Het evenwicht schuift naar rechts, dus komt er meer van het gekleurde product bij. Hoe meer van die stof, hoe donkerder de oplossing.",
    ),
]

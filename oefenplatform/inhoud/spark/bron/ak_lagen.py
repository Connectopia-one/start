# -*- coding: utf-8 -*-
"""De vragen voor "De lagen van een landschap" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "landschappen beschrijven en
patronen herkennen" (12,5 % van het examen).

Deel 1 gaat over de fysischgeografische of natuurlijke lagen: het reliëf met
zijn elementen en vormen, het klimaat, de natuurlijke vegetatie, de bodem, de
ondergrond en het water.
Deel 2 gaat over de sociaalgeografische of menselijke lagen, het landgebruik:
landbouw, industrie, lijninfrastructuur, woongebied, bebouwing, ontginning, en
recreatie en toerisme.

De ruimtelijke patronen (de reliëfeenheden van België, de klimaatzones, de
vegetatiezones en de bevolkingsspreiding) staan niet hier maar in
[[ak_verschillen]], want daar hoort ook het illustreren ervan.

De lijstjes in dit thema komen woord voor woord uit de fiche: de vier textuur-
soorten van de bodem (klei, leem, zand, grind), de vier soorten natuurlijke
vegetatie (naaldbomen, loofbomen, grassen, mossen), de vijf klimaatwoorden
(warm, gematigd, koud, droog, nat) en de zeven vormen van landgebruik. Wie hier
iets bijschrijft, houdt zich aan die lijsten, want het examen doet dat ook.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Twee streken zien er totaal anders uit. Waaraan ligt dat volgens de aardrijkskunde?",
        opties=[
            "Aan de lagen waaruit het landschap is opgebouwd",
            "Aan de mensen die er toevallig wonen",
            "Aan het weer op de dag dat je er toevallig bent",
            "Aan de naam die de streek gekregen heeft",
        ],
        antwoord=0,
        uitleg="Een landschap bestaat uit lagen die over elkaar liggen: reliëf, klimaat, vegetatie, bodem, ondergrond, water, en daarbovenop wat de mens ermee doet. Verschillen in die lagen maken het verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze lagen zijn natuurlijk, dus fysischgeografisch? Er zijn er meerdere juist.",
        opties=[
            "Het reliëf",
            "Het klimaat",
            "De ondergrond",
            "De industrie",
            "Het woongebied",
        ],
        antwoord=[0, 1, 2],
        uitleg="Reliëf, klimaat, natuurlijke vegetatie, bodem, ondergrond en water zijn de natuurlijke lagen. Industrie en woongebied heeft de mens gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met het reliëf van een gebied?",
        opties=[
            "De hoogteverschillen in het gebied",
            "De planten die er van nature groeien",
            "De hoeveelheid regen die er jaarlijks valt",
            "De manier waarop de mensen er wonen",
        ],
        antwoord=0,
        uitleg="Reliëf gaat over de vorm van het oppervlak: waar het hoog en laag ligt, hoe steil het stijgt, hoe groot de hoogteverschillen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de reliëfelementen? Er zijn er meerdere juist.",
        opties=[
            "De helling",
            "De horizonlijn",
            "Het hoogteverschil",
            "De temperatuur",
            "De regenval",
        ],
        antwoord=[0, 1, 2],
        uitleg="De reliëfelementen zijn de helling, de horizonlijn, het hoogteverschil en de hoogteligging. Temperatuur en regenval horen bij het klimaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vlakte en een plateau liggen allebei even hoog boven de zeespiegel.",
        antwoord=False,
        uitleg="Allebei zijn ze vlak, maar een plateau ligt hoog en een vlakte laag. Dat is juist het verschil tussen de twee.",
    ),
    dict(
        type="invultekst",
        vraag="Een hooggelegen gebied dat bovenaan vlak is, heet een ___.",
        antwoord="plateau",
        uitleg="Op de reliëfkaart van België dragen verschillende eenheden dat woord, zoals het Plateau van de Ardennen en het Plateau van Herve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klimaatwoorden gebruikt de vakfiche om een landschap te beschrijven? Er zijn er meerdere juist.",
        opties=[
            "Warm",
            "Gematigd",
            "Koud",
            "Winderig",
            "Bewolkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche werkt met warm, gematigd, koud, droog en nat. Winderig en bewolkt zijn beschrijvingen van het weer van vandaag, niet van het klimaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen weer en klimaat?",
        opties=[
            "Weer is van nu, klimaat is het gemiddelde over jaren",
            "Weer meet je met toestellen, klimaat schat je zelf in",
            "Weer geldt voor een land, klimaat voor een werelddeel",
            "Weer gaat over regen, klimaat gaat over temperatuur",
        ],
        antwoord=0,
        uitleg="Het weer is de toestand van de lucht op dit moment. Het klimaat is hoe het weer er gemiddeld uitziet over vele jaren, meestal dertig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten natuurlijke vegetatie noemt de fiche? Er zijn er meerdere juist.",
        opties=[
            "Naaldbomen",
            "Loofbomen",
            "Grassen en mossen",
            "Fruitbomen in een boomgaard",
            "Maïs op een akker",
        ],
        antwoord=[0, 1, 2],
        uitleg="Natuurlijke vegetatie groeit vanzelf: naaldbomen, loofbomen, grassen en mossen. Een boomgaard en een maïsakker zijn door de mens aangeplant en horen bij de landbouw.",
    ),
    dict(
        type="waarofniet",
        vraag="Loofbomen verliezen hun blad in de winter, naaldbomen meestal niet.",
        antwoord=True,
        uitleg="Daarom blijft een naaldbos ook in januari donkergroen, terwijl een loofbos dan kaal staat. Op een luchtfoto in de winter zie je dat verschil meteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar groeien er van nature vooral mossen en heel lage planten?",
        opties=[
            "In koude streken, waar de zomer kort is",
            "In warme streken, waar het veel regent",
            "In gematigde streken met een zachte winter",
            "In droge streken met veel zand en weinig regen",
        ],
        antwoord=0,
        uitleg="Op de toendra is het te koud en te kort zomer voor bomen. Er blijven mossen, korstmossen en lage struikjes over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de textuur van een bodem?",
        opties=[
            "Uit hoe grove of fijne korrels hij bestaat",
            "Hoeveel planten er op groeien per vierkante meter",
            "Hoe diep je kan graven voor je op steen stoot",
            "Welke kleur hij krijgt als hij nat geworden is",
        ],
        antwoord=0,
        uitleg="De textuur zegt of een bodem uit klei, leem, zand of grind bestaat. Klei heeft de fijnste korrels, grind de grofste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bodemsoort houdt het water het langst vast?",
        opties=[
            "Klei",
            "Zand",
            "Grind",
            "Alle drie evenveel",
        ],
        antwoord=0,
        uitleg="Klei bestaat uit heel fijne korrels die dicht op elkaar liggen, dus het water raakt er moeilijk door. Door zand en grind zakt het snel weg.",
    ),
    dict(
        type="invultekst",
        vraag="De bodemsoort met de fijnste korrels, die het water moeilijk doorlaat, is ___.",
        antwoord="klei",
        uitleg="In de polders aan de kust ligt kleigrond. Die is zwaar te bewerken, maar vruchtbaar, en er blijft gemakkelijk water op staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Onder de bodem ligt de ondergrond, en die bestaat uit zand, leem, klei of vast gesteente.",
        antwoord=True,
        uitleg="De bodem is de bovenste laag waarin planten wortelen. Daaronder zit de ondergrond, en dat is iets anders: zand, leem, klei of vast gesteente zoals kalksteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van vast gesteente in de ondergrond?",
        opties=[
            "Kalksteen",
            "Zand",
            "Leem",
            "Klei",
        ],
        antwoord=0,
        uitleg="Zand, leem en klei zijn losse gesteenten: je kan ze met een schop weghalen. Kalksteen is vast gesteente, daar heb je gereedschap voor nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is water een aparte laag in het landschap?",
        opties=[
            "Omdat het de andere lagen mee vormt en verandert",
            "Omdat het overal ter wereld even diep in de grond zit",
            "Omdat het altijd de grens tussen twee landen vormt",
            "Omdat het als enige laag door de mens gemaakt werd",
        ],
        antwoord=0,
        uitleg="Rivieren slijpen dalen uit, grondwater bepaalt of een bodem nat of droog is, en de zee vormt de kust. Water werkt op alle andere lagen in.",
    ),
    dict(
        type="waarofniet",
        vraag="Een natte bodem en een droge bodem laten dezelfde planten groeien.",
        antwoord=False,
        uitleg="De vochtigheid van de bodem bepaalt mee wat er groeit. Op een natte bodem staan riet en wilgen, op een droge zandbodem eerder heide en dennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de Kempen ligt een zandbodem. Wat volgt daaruit?",
        opties=[
            "Het regenwater zakt er snel weg",
            "Er blijft lang water op het land staan",
            "Er kan geen enkele boom groeien",
            "De grond is er nooit te bewerken",
        ],
        antwoord=0,
        uitleg="Zand laat water snel door. Daarom droogt zo'n bodem vlug uit en waren de Kempen lang heidegebied, tot er dennen aangeplant werden.",
    ),
    dict(
        type="invultekst",
        vraag="De bovenste losse laag waarin planten hun wortels zetten, heet de ___.",
        antwoord="bodem",
        uitleg="De bodem is dun, vaak maar enkele tientallen centimeters. Alles wat daaronder ligt, is de ondergrond.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je kijkt van een heuvel over een streek uit en ziet akkers, een dorp, een spoorlijn en een fabriek. Wat zie je?",
        opties=[
            "Hoe de mensen de grond gebruiken",
            "Hoe hoog de streek boven de zeespiegel ligt",
            "Welke bodemsoort er in de grond zit",
            "Hoeveel regen er jaarlijks valt",
        ],
        antwoord=0,
        uitleg="Akkers, huizen, wegen en fabrieken zijn landgebruik: de sociaalgeografische of menselijke lagen van het landschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze lagen heeft de mens gemaakt? Er zijn er meerdere juist.",
        opties=[
            "De bebouwing",
            "De transportwegen",
            "De ontginning",
            "De ondergrond",
            "Het reliëf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bebouwing, infrastructuur en ontginning zijn menselijke lagen. De ondergrond en het reliëf lagen er al lang voor er iemand woonde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is akkerbouw?",
        opties=[
            "Gewassen telen op het veld",
            "Dieren houden voor vlees of melk",
            "Groenten kweken onder glas",
            "Bomen planten om hout te oogsten",
        ],
        antwoord=0,
        uitleg="Akkerbouw is het telen van gewassen op akkers: graan, aardappelen, suikerbieten, maïs. Dieren houden is veeteelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boer houdt melkkoeien én teelt maïs op zijn akkers. Hoe noem je zijn bedrijf?",
        opties=[
            "Gemengde landbouw",
            "Gespecialiseerde tuinbouw",
            "Intensieve serreteelt",
            "Biologische fruitteelt",
        ],
        antwoord=0,
        uitleg="Wie akkerbouw en veeteelt combineert, doet aan gemengde landbouw. Vaak dient de maïs dan als voer voor de eigen dieren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de tuinbouw? Er zijn er meerdere juist.",
        opties=[
            "Serreteelt",
            "Fruitteelt",
            "Groenten kweken op kleine percelen",
            "Graan telen op grote velden",
            "Runderen houden in de weide",
        ],
        antwoord=[0, 1, 2],
        uitleg="Tuinbouw werkt intensief op kleine oppervlakte: groenten, fruit en teelt onder glas. Graanvelden horen bij de akkerbouw, runderen bij de veeteelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een serre maakt de teler minder afhankelijk van het weer buiten.",
        antwoord=True,
        uitleg="Onder glas stuurt de teler zelf de warmte, het licht en het water. Daardoor kan hij oogsten in een seizoen waarin het buiten niet zou lukken.",
    ),
    dict(
        type="invultekst",
        vraag="Landbouw waarbij dieren gehouden worden voor vlees, melk of eieren, heet ___.",
        antwoord="veeteelt",
        uitleg="In België zie je veel veeteelt in streken met vochtige weiden, want gras groeit daar goed en akkerbouw lukt er minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de lijninfrastructuur? Er zijn er meerdere juist.",
        opties=[
            "Een autosnelweg",
            "Een spoorlijn",
            "Een hoogspanningsleiding",
            "Een voetbalstadion",
            "Een woonwijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Lijninfrastructuur bestaat uit transportwegen en nutsvoorzieningen: wegen, spoorwegen, kanalen, leidingen en kabels. Een stadion en een wijk zijn geen lijnen in het landschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn nutsvoorzieningen?",
        opties=[
            "Leidingen en kabels voor water, gas en stroom",
            "Wegen waarover het vrachtvervoer rijdt",
            "Gebouwen waarin de gemeente haar diensten heeft",
            "Gebieden die voor de natuur beschermd worden",
        ],
        antwoord=0,
        uitleg="Nutsvoorzieningen brengen water, gas, elektriciteit en data tot bij de mensen. Ze liggen vaak onder de grond, maar ze horen wel bij het landgebruik.",
    ),
    dict(
        type="waarofniet",
        vraag="Een woongebied en de bebouwing erin zijn precies hetzelfde.",
        antwoord=False,
        uitleg="Het woongebied is de zone waar gewoond wordt. De bebouwing gaat over de gebouwen zelf: welk type het is en hoe ze verspreid staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met de verspreiding van de bebouwing?",
        opties=[
            "Of de huizen dicht bijeen of verspreid staan",
            "Hoeveel verdiepingen de huizen tellen",
            "Uit welke materialen de huizen gebouwd zijn",
            "Hoe oud de huizen in de straat gemiddeld zijn",
        ],
        antwoord=0,
        uitleg="De verspreiding zegt of de bebouwing geconcentreerd is in een kern, gespreid over het platteland, of in een lint langs de weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Langs een gewestweg staan huizen in één rij aan beide kanten, kilometers ver. Hoe heet dat?",
        opties=[
            "Lintbebouwing",
            "Kernbebouwing",
            "Verspreide bebouwing",
            "Hoogbouw",
        ],
        antwoord=0,
        uitleg="Lintbebouwing is typisch voor Vlaanderen. Het kost veel wegen, riolering en leidingen voor weinig woningen, en het snijdt het open landschap in stukken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is ontginning?",
        opties=[
            "Grondstoffen uit de bodem of ondergrond halen",
            "Een stuk grond bouwrijp maken voor woningen",
            "Een bos aanplanten op een oude akker",
            "Een rivier rechttrekken voor de scheepvaart",
        ],
        antwoord=0,
        uitleg="Bij ontginning worden grondstoffen weggehaald: zand, grind, klei, kalksteen, steenkool. Dat laat groeves en putten in het landschap achter.",
    ),
    dict(
        type="invultekst",
        vraag="Een put waaruit steen of zand gehaald wordt, noem je een ___.",
        antwoord="groeve",
        uitleg="In Wallonië liggen grote kalksteengroeves. Als er niet meer ontgonnen wordt, loopt zo'n groeve vaak vol water en wordt ze een vijver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij recreatie en toerisme? Er zijn er meerdere juist.",
        opties=[
            "Een camping",
            "Een skipiste",
            "Een provinciaal domein met wandelpaden",
            "Een containerterminal in de haven",
            "Een rioolwaterzuivering",
        ],
        antwoord=[0, 1, 2],
        uitleg="Recreatie en toerisme is grondgebruik voor vrije tijd: campings, domeinen, pretparken, pistes, jachthavens. Een terminal en een zuivering dienen daar niet voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Toerisme verandert het landschap niet, want toeristen blijven maar even.",
        antwoord=False,
        uitleg="Toerisme laat wel degelijk sporen na: hotels, appartementen aan de kust, skiliften, parkings en wegen. Die blijven staan als de toeristen weg zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabriek wordt gebouwd langs een kanaal en vlak bij een autosnelweg. Waarom juist daar?",
        opties=[
            "Omdat grondstoffen en producten er vlot aankomen en weggaan",
            "Omdat de bodem er altijd het stevigst is",
            "Omdat het er veel stiller is dan elders in die hele streek",
            "Omdat er daar nooit een vergunning voor nodig is",
        ],
        antwoord=0,
        uitleg="Industrie zoekt goede verbindingen. Water en weg samen maken aanvoer en afvoer goedkoop, en daarom liggen industriegebieden zelden midden in de velden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen er in een havengebied zo weinig woningen?",
        opties=[
            "Omdat het er lawaaierig is en de grond voor bedrijven dient",
            "Omdat de grond er veel te nat is om huizen op te bouwen",
            "Omdat er geen wegen naartoe lopen",
            "Omdat het er te ver van een rivier ligt",
        ],
        antwoord=0,
        uitleg="Een haven draait dag en nacht, met schepen, treinen en vrachtwagens. De ruimte is er voorbehouden voor bedrijven, en wonen gebeurt verderop.",
    ),
    dict(
        type="waarofniet",
        vraag="De menselijke lagen van een landschap kunnen op enkele jaren tijd sterk veranderen.",
        antwoord=True,
        uitleg="Een weiland kan binnen twee jaar een verkaveling zijn. De natuurlijke lagen, zoals het reliëf en de ondergrond, veranderen doorgaans veel trager.",
    ),
    dict(
        type="invultekst",
        vraag="Het geheel van wat de mens met de grond doet, noemen we het land___.",
        antwoord="landgebruik",
        uitleg="Landgebruik vat alle menselijke lagen samen: landbouw, industrie, infrastructuur, wonen, bebouwing, ontginning en recreatie.",
    ),
]

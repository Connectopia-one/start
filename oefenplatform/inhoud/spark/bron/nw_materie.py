# -*- coding: utf-8 -*-
"""De vragen voor "Materie, stoffen en mengsels" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel chemie en fysica, "Materie": het verschil tussen een
chemisch en een fysisch verschijnsel aan de hand van het deeltjesmodel,
aggregatietoestanden en faseovergangen, thermisch uitzetten en krimpen, het
deeltje als chemische verbinding uit een of meer atoomsoorten (C, O, H, Fe), en
het verschil tussen mengsels en zuivere stoffen.

Deel 1 gaat over de namen en de kenmerken. Deel 2 laat je uitleggen waarom, met
het deeltjesmodel in de hand: waarom een rails uitzet, waarom een gas samen te
persen is, waarom roesten iets anders is dan smelten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn de drie aggregatietoestanden van een stof?",
        opties=[
            "Vast, vloeibaar en gasvormig",
            "Hard, zacht en vloeibaar",
            "Warm, koud en lauw",
        ],
        antwoord=0,
        uitleg="Dezelfde stof kan in drie toestanden voorkomen. Water is daar het bekendste voorbeeld van: ijs, water en waterdamp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe liggen de deeltjes in een vaste stof volgens het deeltjesmodel?",
        opties=[
            "Dicht bij elkaar, op een vaste plaats, ze trillen alleen",
            "Ver uit elkaar en snel door elkaar",
            "Dicht bij elkaar, maar ze schuiven vrij langs elkaar",
        ],
        antwoord=0,
        uitleg="In een vaste stof zitten de deeltjes op een vaste plek en trillen ze alleen. In een vloeistof schuiven ze langs elkaar, in een gas vliegen ze ver uit elkaar rond.",
    ),
    dict(
        type="invultekst",
        vraag="Een vaste stof die vloeibaar wordt: die faseovergang heet ___.",
        antwoord="smelten",
        uitleg="Smelten is van vast naar vloeibaar, stollen is het omgekeerde. IJs smelt bij 0 °C en water stolt bij diezelfde temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet de overgang van gasvormig naar vloeibaar?",
        opties=["Condenseren", "Verdampen", "Sublimeren"],
        antwoord=0,
        uitleg="Condenseren is gas dat vloeistof wordt, zoals damp op een koude spiegel. Verdampen is net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke faseovergangen gebeuren er als je een stof opwarmt?",
        opties=["Smelten", "Verdampen", "Sublimeren", "Stollen"],
        antwoord=[0, 1, 2],
        uitleg="Opwarmen geeft de deeltjes meer bewegingsenergie: smelten, verdampen en sublimeren (vast rechtstreeks naar gas). Stollen, condenseren en rijpen gebeuren net bij afkoelen.",
    ),
    dict(
        type="invultekst",
        vraag="Een gas dat rechtstreeks een vaste stof wordt, zoals rijp op een tak: dat heet ___.",
        antwoord="rijpen",
        uitleg="Rijpen of desublimeren is de overgang van gas naar vast, zonder vloeibare tussenstap. Sublimeren is het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een fysisch verschijnsel?",
        opties=[
            "Er ontstaat geen nieuwe stof, alleen de vorm of de toestand verandert",
            "Er ontstaat altijd een nieuwe stof",
            "Er komt altijd gas bij vrij",
        ],
        antwoord=0,
        uitleg="Bij een fysisch verschijnsel blijven de deeltjes dezelfde: smelten, breken, oplossen. Bij een chemisch verschijnsel veranderen de deeltjes zelf en ontstaan er nieuwe stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn chemische verschijnselen?",
        opties=["IJzer dat roest", "Hout dat verbrandt", "IJs dat smelt", "Suiker die oplost"],
        antwoord=[0, 1],
        uitleg="Bij roesten en verbranden ontstaan er nieuwe stoffen. Smelten en oplossen zijn fysisch: de stof is er nog, alleen in een andere toestand of verdeeld in water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verschijnsel wijst erop dat er een chemische reactie gebeurt?",
        opties=[
            "Er ontstaat een gas of een neerslag",
            "De stof wordt warmer",
            "De stof wordt in stukken gebroken",
        ],
        antwoord=0,
        uitleg="Kleurverandering, geurverandering, smaakverandering, neerslagvorming en gasontwikkeling zijn aanwijzingen voor een chemische omzetting.",
    ),
    dict(
        type="waarofniet",
        vraag="Water dat kookt, is een chemisch verschijnsel.",
        antwoord=False,
        uitleg="Koken is verdampen, dus fysisch: uit watermoleculen komen weer watermoleculen, alleen in gasvorm. Er ontstaat geen nieuwe stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een zuivere stof?",
        opties=[
            "Een stof die maar uit één soort deeltje bestaat",
            "Een stof zonder kleur",
            "Een stof die je kan drinken",
        ],
        antwoord=0,
        uitleg="In een zuivere stof zit maar één soort deeltjes, zoals in zuiver water of in koper. In een mengsel zitten er verschillende soorten door elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn mengsels?",
        opties=["Zeewater", "Lucht", "Zuiver water", "Koper"],
        antwoord=[0, 1],
        uitleg="Zeewater is water met opgeloste zouten, lucht is een mengsel van gassen. Zuiver water en koper zijn zuivere stoffen.",
    ),
    dict(
        type="invultekst",
        vraag="Het chemisch symbool van zuurstof is ___.",
        antwoord="O",
        uitleg="Koolstof is C, zuurstof O, waterstof H en ijzer Fe. Zuurstofgas in de lucht schrijf je als O₂: twee zuurstofatomen aan elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat een chemische verbinding?",
        opties=[
            "Uit atomen van een of meer atoomsoorten die aan elkaar gebonden zijn",
            "Uit losse deeltjes die niets met elkaar te maken hebben",
            "Uit één enkel atoom",
        ],
        antwoord=0,
        uitleg="Een verbinding of molecule is een groepje atomen dat met bindingen samenhangt. Water (H₂O) bestaat uit twee waterstofatomen en één zuurstofatoom.",
    ),
    dict(
        type="waarofniet",
        vraag="Het symbool Fe staat voor ijzer.",
        antwoord=True,
        uitleg="Fe komt van het Latijnse ferrum. In de eerste graad moet je zeker C, O, H en Fe kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan je een gas samenpersen en een vaste stof niet?",
        opties=[
            "Omdat er tussen de deeltjes van een gas veel lege ruimte zit",
            "Omdat gasdeeltjes kleiner zijn",
            "Omdat een gas lichter is",
        ],
        antwoord=0,
        uitleg="In een gas liggen de deeltjes ver uit elkaar, dus je kan ze dichter bij elkaar duwen. In een vaste stof raken ze elkaar al bijna: daar is geen ruimte meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stofeigenschap?",
        opties=[
            "Een kenmerk dat typisch is voor een stof, zoals haar smelttemperatuur",
            "De vorm van het voorwerp",
            "Het gewicht van het voorwerp",
        ],
        antwoord=0,
        uitleg="Smelt- en kooktemperatuur, kleur, geleidbaarheid en massadichtheid zijn stofeigenschappen: ze hangen niet af van hoe groot je stuk is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het smelten van ijs veranderen de watermoleculen zelf.",
        antwoord=False,
        uitleg="De moleculen blijven precies dezelfde; ze gaan alleen sneller bewegen en laten hun vaste plaats los. Daarom is smelten een fysisch verschijnsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een vloeistof geen vaste vorm, maar wel een vast volume?",
        opties=[
            "De deeltjes schuiven langs elkaar, maar blijven tegen elkaar aan",
            "De deeltjes liggen ver uit elkaar",
            "De deeltjes staan helemaal stil",
        ],
        antwoord=0,
        uitleg="Ze raken elkaar nog, dus de hoeveelheid ruimte blijft gelijk, maar ze zitten niet vast, dus de vloeistof neemt de vorm van het vat aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Melk waar je suiker in roert tot je die niet meer ziet: wat is dat?",
        opties=["Een mengsel", "Een zuivere stof", "Een chemisch verschijnsel"],
        antwoord=0,
        uitleg="Oplossen is fysisch: de suikerdeeltjes zitten verspreid tussen de deeltjes van de melk, maar ze zijn nog altijd suiker. Je kan ze er weer uit krijgen door te verdampen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom zet een metalen staaf uit als je hem opwarmt?",
        opties=[
            "De deeltjes trillen heviger en nemen daardoor meer plaats in",
            "Er komen deeltjes bij",
            "De deeltjes worden zelf groter",
        ],
        antwoord=0,
        uitleg="Thermisch uitzetten verklaar je met het deeltjesmodel: meer warmte betekent meer beweging, dus meer ruimte tussen de deeltjes. Het aantal deeltjes en hun grootte blijven gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laten ze bij spoorstaven en bruggen een kleine opening?",
        opties=[
            "Zodat het metaal bij warm weer kan uitzetten zonder kromtrekken",
            "Zodat het regenwater weg kan",
            "Zodat het metaal lichter is",
        ],
        antwoord=0,
        uitleg="Zonder ruimte duwt het uitzettende metaal tegen zichzelf en vervormt het. Bij koud weer krimpt het weer en wordt de opening groter.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij afkoelen komen de deeltjes van een stof dichter bij elkaar.",
        antwoord=True,
        uitleg="Minder warmte betekent minder beweging, dus krimpt de stof. Water is de bekende uitzondering: bij het bevriezen zet het net uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de deeltjes bij het verdampen van water?",
        opties=[
            "Ze bewegen zo snel dat ze zich losmaken van de vloeistof",
            "Ze veranderen in zuurstof en waterstof",
            "Ze vallen uiteen in atomen",
        ],
        antwoord=0,
        uitleg="Verdampen is fysisch. De snelste moleculen ontsnappen uit de vloeistof; het blijven watermoleculen, alleen ver uit elkaar in de lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beslaat de binnenkant van een raam in de winter?",
        opties=[
            "Waterdamp uit de kamerlucht condenseert tegen het koude glas",
            "Er sijpelt water door het glas",
            "Het glas verdampt",
        ],
        antwoord=0,
        uitleg="Koud glas koelt de lucht ernaast af. Koude lucht kan minder waterdamp bevatten, dus die damp wordt weer vloeibaar: condenseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een chemisch verschijnsel kloppen?",
        opties=[
            "Er ontstaan nieuwe stoffen",
            "De deeltjes zelf veranderen",
            "Het is meestal niet zomaar om te keren",
            "De aggregatietoestand verandert altijd",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij een chemische omzetting worden bindingen verbroken en nieuwe gevormd. Geroosterd brood krijg je niet meer wit. Een toestandsverandering hoort er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stukje ijzerwol wordt na een week in vochtige lucht bruin en zwaarder. Wat is er gebeurd?",
        opties=[
            "Een chemische reactie: het ijzer verbond zich met zuurstof tot roest",
            "Een fysisch verschijnsel: het ijzer werd nat",
            "Het ijzer is gesmolten",
        ],
        antwoord=0,
        uitleg="Kleurverandering én meer massa wijzen op een nieuwe stof: er zijn zuurstofatomen bij gekomen. Roest is dus geen ijzer meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een tekening met deeltjes: allemaal identieke bolletjes van twee aan elkaar. Wat stelt dat voor?",
        opties=[
            "Een zuivere stof die uit moleculen bestaat",
            "Een mengsel van twee stoffen",
            "Een mengsel van atomen en moleculen",
        ],
        antwoord=0,
        uitleg="Eén soort deeltje betekent een zuivere stof. Bestaat dat deeltje uit twee gebonden atomen, dan is het een verbinding, zoals O₂.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke deeltjesvoorstellingen horen bij een mengsel?",
        opties=[
            "Bolletjes van twee verschillende soorten door elkaar",
            "Losse atomen samen met moleculen",
            "Allemaal dezelfde moleculen",
            "Allemaal dezelfde atomen",
        ],
        antwoord=[0, 1],
        uitleg="Zodra er meer dan één soort deeltje in zit, is het een mengsel. Allemaal hetzelfde deeltje betekent een zuivere stof, ook als dat deeltje zelf uit meerdere atomen bestaat.",
    ),
    dict(
        type="invultekst",
        vraag="Een vaste stof die rechtstreeks een gas wordt, zoals droogijs: die overgang heet ___.",
        antwoord="sublimeren",
        uitleg="Droogijs is vast koolstofdioxide. Het gaat zonder vloeibare tussenstap over in gas, en daarom heet het droog ijs.",
    ),
    dict(
        type="waarofniet",
        vraag="Zuiver water en zeewater bevriezen bij dezelfde temperatuur.",
        antwoord=False,
        uitleg="Het opgeloste zout verlaagt de stoltemperatuur van water. Daarom strooien ze zout op de weg en bevriest de zee pas bij lagere temperaturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwarmt een afgesloten fles met lucht. Wat gebeurt er met de deeltjes?",
        opties=[
            "Ze bewegen sneller en botsen harder tegen de wand, dus de druk stijgt",
            "Er komen deeltjes bij",
            "Ze gaan stilstaan",
        ],
        antwoord=0,
        uitleg="Het volume kan niet groter worden, dus vertaalt de extra bewegingsenergie zich in meer druk. Daarom mag je een spuitbus nooit in het vuur gooien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschijnselen zijn fysisch?",
        opties=[
            "Een glas dat breekt",
            "Zout dat oplost in water",
            "Boter die smelt",
            "Een appel die bruin wordt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij de eerste drie blijft de stof zichzelf. Een appel die bruin wordt, reageert met zuurstof uit de lucht: dat is chemisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Water is H₂O. Wat betekent dat?",
        opties=[
            "Eén molecule bestaat uit twee waterstofatomen en één zuurstofatoom",
            "Water is een mengsel van waterstof en zuurstof",
            "Water bevat twee soorten moleculen",
        ],
        antwoord=0,
        uitleg="De formule geeft de bouw van één deeltje. Water is een zuivere stof, geen mengsel: alle deeltjes zijn identiek.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens het smelten van ijs stijgt de temperatuur van het mengsel ijs en water.",
        antwoord=False,
        uitleg="Zolang er nog ijs drijft, blijft de temperatuur 0 °C. Alle toegevoerde warmte gaat naar het losmaken van de deeltjes, niet naar opwarmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ruikt je hele keuken naar soep terwijl de pot in de hoek staat?",
        opties=[
            "Gasdeeltjes bewegen snel en verspreiden zich door de hele ruimte",
            "De geur loopt over de vloer",
            "De soep straalt licht uit",
        ],
        antwoord=0,
        uitleg="Gasdeeltjes vliegen alle kanten op en mengen zich vanzelf met de lucht. Hoe warmer, hoe sneller ze bewegen en hoe sneller je de geur ruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn opgebouwd uit meer dan één atoomsoort?",
        opties=["Water (H₂O)", "Koolstofdioxide (CO₂)", "Zuurstofgas (O₂)", "Glucose (C₆H₁₂O₆)"],
        antwoord=[0, 1, 3],
        uitleg="Water, koolstofdioxide en glucose bevatten verschillende atoomsoorten. Zuurstofgas bestaat uit twee atomen van dezelfde soort.",
    ),
    dict(
        type="invultekst",
        vraag="De overgang van vloeibaar naar vast heet ___.",
        antwoord="stollen",
        uitleg="Stollen is het omgekeerde van smelten. Voor eenzelfde zuivere stof gebeuren ze bij dezelfde temperatuur, bijvoorbeeld 0 °C voor water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kaars brandt. Welke twee verschijnselen zie je tegelijk?",
        opties=[
            "Smelten van de was is fysisch, het branden is chemisch",
            "Allebei fysisch",
            "Allebei chemisch",
        ],
        antwoord=0,
        uitleg="De was smelt en verdampt eerst (fysisch) en die damp verbrandt daarna met zuurstof tot koolstofdioxide en water (chemisch).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verklaar je met het deeltjesmodel dat een gas geen vaste vorm én geen vast volume heeft?",
        opties=[
            "De deeltjes bewegen vrij en ver uit elkaar, dus ze vullen elke ruimte op",
            "De deeltjes trekken elkaar sterk aan",
            "De deeltjes liggen op een vaste plaats",
        ],
        antwoord=0,
        uitleg="In een gas is de aantrekking tussen de deeltjes te zwak om ze bij elkaar te houden. Ze verspreiden zich tot ze tegen de wand van het vat botsen.",
    ),
]

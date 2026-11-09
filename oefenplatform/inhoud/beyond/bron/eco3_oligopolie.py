# -*- coding: utf-8 -*-
"""Monopolistische concurrentie, oligopolie en speltheorie.

Fiche: verschil tussen monopolistische concurrentie, monopolie, oligopolie en
volkomen concurrentie; prijsvorming en prijsafzetcurve bij monopolistische
concurrentie; winstmaximalisatie op korte en lange termijn; prijsvorming bij
oligopolie, geknikte prijsafzetcurve, prijsstarheid; kartelvorming;
speltheorie: best-response strategie, dominante strategie, Nash-evenwicht,
gevangenendilemma; speltheorie als verklaring voor kartelvorming.

De spelvoorbeelden staan in woorden, zodat ze ook op een smal scherm leesbaar
zijn.
"""

SPEL = (
    "Twee bedrijven A en B kiezen een hoge of een lage prijs. Beide hoog: elk 10 winst. "
    "A hoog en B laag: A 2, B 15. A laag en B hoog: A 15, B 2. Beide laag: elk 5. "
)

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt monopolistische concurrentie?",
        opties=[
            "veel aanbieders van gelijkaardige maar verschillende producten",
            "één aanbieder zonder concurrenten en met hoge drempels",
            "enkele grote aanbieders die sterk op elkaar letten",
            "veel aanbieders van precies hetzelfde product, zonder merken",
        ],
        antwoord=0,
        uitleg="Denk aan kappers, restaurants of kledingwinkels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een oligopolie?",
        opties=[
            "enkele grote aanbieders die van elkaar afhankelijk zijn",
            "veel kleine aanbieders van gelijkaardige producten",
            "één aanbieder die de hele markt bedient",
            "veel aanbieders zonder enige productdifferentiatie",
        ],
        antwoord=0,
        uitleg="Denk aan telecomoperatoren of vliegtuigbouwers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad heeft honderden restaurants, elk met een eigen keuken en sfeer. Welke marktvorm?",
        opties=["monopolistische concurrentie", "oligopolie", "monopolie", "volkomen concurrentie"],
        antwoord=0,
        uitleg="Veel aanbieders, gedifferentieerd product, vrije toetreding.",
    ),
    dict(
        type="meerkeuze",
        vraag="In België bieden drie grote operatoren de meeste mobiele abonnementen aan. Welke marktvorm?",
        opties=["oligopolie", "monopolistische concurrentie", "monopolie", "volkomen concurrentie"],
        antwoord=0,
        uitleg="Weinig aanbieders, hoge toetredingsdrempels.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij monopolistische concurrentie heeft elke aanbieder een dalende prijsafzetcurve.",
        antwoord=True,
        uitleg="Door zijn eigen merk of stijl heeft hij wat marktmacht, maar door de vele concurrenten is de curve vrij elastisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maximaliseert een monopolistische concurrent zijn winst op korte termijn?",
        opties=["hij produceert waar MO = MK", "hij produceert waar P = GK", "hij vraagt de laagste prijs van de markt", "hij produceert zoveel mogelijk"],
        antwoord=0,
        uitleg="Net als een monopolist, maar met een vlakkere prijsafzetcurve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op lange termijn als monopolistische concurrenten winst maken?",
        opties=[
            "nieuwe aanbieders treden toe, tot de winst verdwenen is",
            "de winst blijft altijd even groot, want het product is uniek",
            "de overheid neemt de winst af met een extra belasting",
            "de bestaande bedrijven smelten samen tot één monopolie",
        ],
        antwoord=0,
        uitleg="Door de vrije toetreding verdeelt de vraag zich over meer aanbieders. Op lange termijn is P = GK.",
    ),
    dict(
        type="waarofniet",
        vraag="Op lange termijn maakt een monopolistische concurrent een grote economische winst.",
        antwoord=False,
        uitleg="Toetreders duwen de winst naar nul: de prijsafzetcurve raakt dan de GK-curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is prijsstarheid bij oligopolie?",
        opties=[
            "de prijs blijft lang gelijk, ook bij andere kosten",
            "de prijs verandert elke dag met de vraag mee",
            "de overheid legt de prijs voor de hele sector vast",
            "de prijs volgt elke maand automatisch de inflatie",
        ],
        antwoord=0,
        uitleg="Wie zijn prijs verhoogt, verliest klanten; wie verlaagt, start een prijzenoorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft de prijsafzetcurve bij oligopolie een knik?",
        opties=[
            "concurrenten volgen wel een daling, geen stijging",
            "de overheid legt de oligopolist een maximumprijs op",
            "de kosten stijgen plots vanaf een bepaalde hoeveelheid",
            "de consumenten kopen enkel bij een mooie ronde prijs",
        ],
        antwoord=0,
        uitleg="Boven de knik is de curve elastisch, eronder inelastisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Boven de knik van de geknikte prijsafzetcurve is de vraag elastisch.",
        antwoord=True,
        uitleg="Wie alleen zijn prijs verhoogt, verliest veel klanten aan de concurrenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband is er tussen de geknikte prijsafzetcurve en prijsstarheid?",
        opties=[
            "de MO-curve maakt een sprong, dus een kleine kostenwijziging verandert de prijs niet",
            "de knik zorgt ervoor dat de kosten van de oligopolist altijd gelijk blijven",
            "de knik verplicht de oligopolist om zijn prijs elk jaar een beetje te verhogen",
            "de knik doet de vraag helemaal verdwijnen bij elke kleine prijsverandering",
        ],
        antwoord=0,
        uitleg="Zolang MK door de sprong in MO loopt, blijft MO = MK bij dezelfde hoeveelheid en prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kartel?",
        opties=[
            "een afspraak tussen aanbieders over prijzen of markten",
            "een vereniging van consumenten die samen goedkoper inkopen",
            "een bedrijf dat door de overheid is opgericht en beheerd",
            "een groep landen die dezelfde munt gebruiken",
        ],
        antwoord=0,
        uitleg="Zo gedragen ze zich samen als een monopolist. In de EU is dat verboden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben monopolie, oligopolie en monopolistische concurrentie gemeen? Duid alle juiste antwoorden aan.",
        opties=[
            "de aanbieders hebben wat invloed op de prijs",
            "de prijsafzetcurve van een aanbieder daalt",
            "er zijn overal heel veel aanbieders",
            "de producten zijn overal precies hetzelfde",
        ],
        antwoord=[0, 1],
        uitleg="Dat onderscheidt ze van volkomen concurrentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij monopolistische concurrentie zijn de toetredingsdrempels hoog.",
        antwoord=False,
        uitleg="Toetreden is er vrij gemakkelijk. Dat is net een verschil met oligopolie en monopolie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom doen bedrijven bij monopolistische concurrentie veel aan reclame?",
        opties=[
            "om hun product te onderscheiden van dat van de concurrent",
            "omdat de overheid dat verplicht",
            "omdat ze precies hetzelfde product verkopen als de rest",
            "om de toetreding van nieuwe bedrijven te vergemakkelijken",
        ],
        antwoord=0,
        uitleg="Productdifferentiatie geeft een beetje marktmacht.",
    ),
    dict(
        type="waarofniet",
        vraag="Oligopolisten houden bij hun beslissingen rekening met de reactie van hun concurrenten.",
        antwoord=True,
        uitleg="Die onderlinge afhankelijkheid is typisch voor oligopolie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke marktvorm heeft de meest elastische prijsafzetcurve voor één aanbieder?",
        opties=["volkomen concurrentie", "monopolistische concurrentie", "oligopolie", "monopolie"],
        antwoord=0,
        uitleg="Daar is ze perfect elastisch (horizontaal).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken passen bij oligopolie? Duid alle juiste antwoorden aan.",
        opties=["weinig aanbieders", "hoge toetredingsdrempels", "atomische markt", "geen enkele marktmacht"],
        antwoord=[0, 1],
        uitleg="Een atomische markt zonder marktmacht hoort bij volkomen concurrentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Kartelafspraken zijn in de Europese Unie toegelaten als ze geheim blijven.",
        antwoord=False,
        uitleg="Ze zijn verboden en worden zwaar beboet, of ze nu geheim zijn of niet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een best-response strategie?",
        opties=[
            "de beste keuze voor een speler, gegeven wat de andere speler doet",
            "de keuze die voor beide spelers samen het beste is",
            "de keuze die de overheid aanraadt",
            "de keuze die de tegenstander het meest schade toebrengt",
        ],
        antwoord=0,
        uitleg="Je kijkt telkens per keuze van de tegenspeler wat voor jou het beste is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een dominante strategie?",
        opties=[
            "een strategie die het beste is, wat de andere speler ook doet",
            "de strategie van de grootste speler op de markt",
            "een strategie die enkel werkt als de andere meedoet",
            "een strategie die altijd de hoogste totale winst oplevert",
        ],
        antwoord=0,
        uitleg="Je hoeft dan niet te weten wat de ander kiest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een Nash-evenwicht?",
        opties=[
            "geen speler wint iets door in zijn eentje te veranderen",
            "een situatie waarin beide spelers de hoogst mogelijke winst halen",
            "een situatie waarin de overheid de prijzen vastlegt",
            "een situatie waarin vraag en aanbod gelijk zijn",
        ],
        antwoord=0,
        uitleg="Elke speler speelt een best-response op de keuze van de ander.",
    ),
    dict(
        type="meerkeuze",
        vraag=SPEL + "Wat is de best-response van A als B een hoge prijs kiest?",
        opties=["een lage prijs", "een hoge prijs", "maakt niet uit", "stoppen met verkopen"],
        antwoord=0,
        uitleg="Laag geeft A 15, hoog geeft 10.",
    ),
    dict(
        type="meerkeuze",
        vraag=SPEL + "Wat is de best-response van A als B een lage prijs kiest?",
        opties=["een lage prijs", "een hoge prijs", "maakt niet uit", "stoppen met verkopen"],
        antwoord=0,
        uitleg="Laag geeft A 5, hoog geeft 2.",
    ),
    dict(
        type="waarofniet",
        vraag=SPEL + "Een lage prijs is voor A een dominante strategie.",
        antwoord=True,
        uitleg="Wat B ook doet, laag levert A meer op.",
    ),
    dict(
        type="meerkeuze",
        vraag=SPEL + "Wat is het Nash-evenwicht?",
        opties=["beide laag", "beide hoog", "A hoog en B laag", "A laag en B hoog"],
        antwoord=0,
        uitleg="Bij beide laag wint geen van beiden iets door alleen te veranderen.",
    ),
    dict(
        type="waarofniet",
        vraag=SPEL + "In het Nash-evenwicht halen beide bedrijven samen de hoogste winst.",
        antwoord=False,
        uitleg="Samen halen ze 10, terwijl beide hoog 20 zou opleveren. Dat is het gevangenendilemma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gevangenendilemma?",
        opties=[
            "eigenbelang leidt tot een slechtere uitkomst voor beide",
            "een spel waarin één van de spelers altijd wint",
            "een spel waarin samenwerken door de wet verboden is",
            "een spel waarin er geen enkel Nash-evenwicht bestaat",
        ],
        antwoord=0,
        uitleg="Het eigenbelang leidt niet tot de beste uitkomst voor de groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verklaart speltheorie dat bedrijven een kartel willen vormen?",
        opties=[
            "samen een hoge prijs afspreken levert elk meer op dan het Nash-evenwicht",
            "een kartel verlaagt de prijzen voor de consumenten",
            "de overheid beloont kartels met subsidies",
            "zonder kartel kan geen enkel bedrijf winst maken",
        ],
        antwoord=0,
        uitleg="Ze proberen uit het gevangenendilemma te ontsnappen door af te spreken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn kartels volgens de speltheorie vaak niet stabiel?",
        opties=[
            "elk lid wint erbij door stiekem een lagere prijs te vragen",
            "de leden hebben altijd precies dezelfde kosten",
            "de consumenten weigeren bij een kartel te kopen",
            "een kartel mag volgens de wet maar één jaar bestaan",
        ],
        antwoord=0,
        uitleg="Valsspelen is de best-response als de anderen zich aan de afspraak houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spel kan een Nash-evenwicht hebben zonder dat een speler een dominante strategie heeft.",
        antwoord=True,
        uitleg="Het volstaat dat elke speler een best-response speelt op de keuze van de ander.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee tankstations staan naast elkaar. Als één de prijs verlaagt, volgt de ander meteen. Als één de prijs verhoogt, volgt de ander niet. Wat verklaart dit?",
        opties=["de geknikte prijsafzetcurve", "een kartelafspraak", "volkomen concurrentie", "een monopolie"],
        antwoord=0,
        uitleg="Daardoor blijven de prijzen lang gelijk: prijsstarheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Onder de knik van de geknikte prijsafzetcurve is de vraag inelastisch.",
        antwoord=True,
        uitleg="Bij een prijsverlaging volgen de concurrenten, dus de verkoop stijgt maar weinig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het gevangenendilemma bij twee bedrijven kloppen? Duid alle juiste antwoorden aan.",
        opties=[
            "elk bedrijf heeft een dominante strategie om niet samen te werken",
            "beide zouden beter af zijn als ze konden samenwerken",
            "het Nash-evenwicht is de beste uitkomst voor beide samen",
            "er is nooit een Nash-evenwicht",
        ],
        antwoord=[0, 1],
        uitleg="Het Nash-evenwicht is net slechter voor beide samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee bedrijven kiezen veel of weinig reclame. Weinig voor beide: elk 8. Veel voor beide: elk 4. Eén veel, de ander weinig: 10 voor wie veel maakt, 2 voor de andere. Wat is het Nash-evenwicht?",
        opties=["beide veel reclame", "beide weinig reclame", "één veel, de ander weinig", "er is geen evenwicht"],
        antwoord=0,
        uitleg="Veel reclame is voor elk dominant (10 > 8 en 4 > 2). Ook hier een gevangenendilemma.",
    ),
    dict(
        type="waarofniet",
        vraag="Speltheorie is enkel nuttig bij volkomen concurrentie.",
        antwoord=False,
        uitleg="Bij volkomen concurrentie hoef je niet op elkaar te letten. Speltheorie past juist bij oligopolie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij monopolistische concurrentie op lange termijn raakt de prijsafzetcurve de GK-curve. Wat betekent dat?",
        opties=[
            "de prijs is gelijk aan de gemiddelde kosten, dus de winst is nul",
            "de prijs ligt ver boven de gemiddelde kosten van het bedrijf",
            "het bedrijf maakt een groot verlies en moet sluiten",
            "de marginale kosten zijn nul bij elke hoeveelheid",
        ],
        antwoord=0,
        uitleg="Er is geen reden meer om toe te treden of uit te treden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke marktvorm sluit het best aan bij deze beschrijving: twee grote vliegtuigbouwers verdelen de wereldmarkt?",
        opties=["oligopolie", "monopolie", "monopolistische concurrentie", "volkomen concurrentie"],
        antwoord=0,
        uitleg="Een oligopolie met twee spelers heet ook een duopolie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een Nash-evenwicht heeft elke speler spijt van zijn keuze, gegeven wat de ander deed.",
        antwoord=False,
        uitleg="Net niet: gegeven de keuze van de ander, kon hij niets beters doen.",
    ),
]

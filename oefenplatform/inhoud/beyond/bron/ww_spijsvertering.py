# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Het spijsverteringsstelsel.

Biologie, blok "Stofwisselingsfysiologie en secretie". Deel 1 gaat over de
bouw van het spijsverteringsstelsel en de verteringssappen en enzymen, deel 2
over absorptie en transport, voedingsstoffen, darmflora en aandoeningen.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "Welke laag van de wand van het spijsverteringskanaal ligt aan de binnenkant, tegen de voedselbrij?",
        ["de slijmvlieslaag of mucosa", "de spierlaag", "de buitenste bindweefsellaag", "het middenrif"],
        0,
        "Van binnen naar buiten liggen de slijmvlieslaag, een bindweefsellaag, de spierlaag en tot slot een bindweefsel- of steunweefsellaag.",
    ),
    M(
        "Wat is de taak van de spierlaag in de wand van het spijsverteringskanaal?",
        [
            "ze kneedt het voedsel en duwt het verder door peristaltiek",
            "ze maakt verteringsenzymen aan die het voedsel afbreken",
            "ze neemt de voedingsstoffen op en geeft ze door aan het bloed",
            "ze beschermt het kanaal tegen bacteriën met antistoffen",
        ],
        0,
        "Kringspieren en lengtespieren trekken beurtelings samen. Die golfbeweging, de peristaltiek, duwt de voedselbrij door het kanaal.",
    ),
    I(
        "Hoe heet de golfvormige samentrekking van de spieren in de wand van de slokdarm en de darmen, die het voedsel voortstuwt?",
        "peristaltiek",
        "Bij peristaltiek trekken de kringspieren achter de voedselbrok samen en ontspannen ze ervoor. Zo schuift het voedsel verder, zelfs als je ondersteboven hangt.",
    ),
    M(
        "Wat belet dat voedsel bij het slikken in de luchtpijp terechtkomt?",
        ["het strottenklepje", "de maagportier", "de sluitspier van de anus", "het middenrif"],
        0,
        "Bij het slikken sluit het strottenklepje de ingang van het strottenhoofd af. Het voedsel gaat zo de slokdarm in.",
    ),
    W(
        "De maagportier is de kringspier tussen de slokdarm en de maag.",
        False,
        "De maagportier ligt aan de uitgang van de maag, tussen de maag en de twaalfvingerige darm. Ze laat de maaginhoud met kleine porties door.",
    ),
    M(
        "Welke delen behoren tot de dunne darm? Kruis alles aan wat juist is.",
        ["de twaalfvingerige darm", "de nuchtere darm of jejunum", "de blinde darm of caecum", "de karteldarm of colon"],
        [0, 1],
        "De dunne darm bestaat uit de twaalfvingerige darm, de nuchtere darm en de kronkeldarm of ileum. De blinde darm en het colon horen bij de dikke darm.",
    ),
    M(
        "Welke delen behoren tot de dikke darm? Kruis alles aan wat juist is.",
        ["de blinde darm met het wormvormig aanhangsel", "de karteldarm of colon", "de endeldarm of rectum", "de nuchtere darm"],
        [0, 1, 2],
        "De dikke darm begint bij de blinde darm, loopt via het opstijgend, dwarslopend, afdalend en S-vormig deel van het colon en eindigt bij de endeldarm.",
    ),
    M(
        "Wat is vertering?",
        [
            "het afbreken van grote voedingsmoleculen tot kleine die opgenomen kunnen worden",
            "het opnemen van de voedingsstoffen uit de dunne darm in het bloed en in de lymfevaten",
            "het verwijderen van de onverteerbare voedselresten langs de anus",
            "het opslaan van voedingsstoffen in de lever voor later gebruik",
        ],
        0,
        "Grote moleculen zoals zetmeel, eiwitten en vetten passen niet door de darmwand. Vertering knipt ze in kleine bouwstenen die wel opgenomen kunnen worden.",
    ),
    M(
        "Welke cellen in de maagwand maken het zoutzuur van het maagsap?",
        ["de pariëtale cellen", "de slijmcellen", "de darmepitheelcellen", "de rode bloedcellen"],
        0,
        "Pariëtale cellen in de maagklieren maken HCl. Slijmcellen maken een laag slijm die de maagwand tegen dat zuur beschermt.",
    ),
    M(
        "Wat doet het maagzuur? Kruis alles aan wat juist is.",
        [
            "het doodt veel bacteriën die met het voedsel binnenkomen",
            "het zet pepsinogeen om in het actieve pepsine",
            "het zorgt voor de lage pH waarbij pepsine goed werkt",
            "het emulgeert de vetten tot kleine druppeltjes",
        ],
        [0, 1, 2],
        "Maagzuur ontsmet, activeert pepsinogeen tot pepsine en zorgt voor de lage pH die pepsine nodig heeft. Vetten emulgeren doen de galzouten.",
    ),
    W(
        "Pepsine wordt eerst aangemaakt als het inactieve pepsinogeen, zodat het de cellen die het maken niet zelf verteert.",
        True,
        "Pas in de maagholte zet maagzuur pepsinogeen om in pepsine. Zo blijft de cel die het maakt gespaard.",
    ),
    M(
        "Waar wordt gal aangemaakt?",
        ["in de lever", "in de galblaas", "in de alvleesklier", "in de maag"],
        0,
        "De lever maakt gal. De galblaas slaat de gal op en dikt ze in, en geeft ze af aan de twaalfvingerige darm na een maaltijd.",
    ),
    M(
        "Wat doen galzouten met vetten in de dunne darm?",
        [
            "ze verdelen grote vetdruppels in kleine druppeltjes, zodat lipase beter kan werken",
            "ze knippen de vetten chemisch in glycerol en losse vetzuren",
            "ze zetten de vetten om in glucose voor de energievoorziening",
            "ze brengen de vetten zonder verdere vertering in de bloedbaan",
        ],
        0,
        "Galzouten emulgeren: ze maken van grote vetdruppels veel kleine. Dat vergroot het oppervlak waarop lipase de vetten afbreekt.",
    ),
    W(
        "Gal bevat zelf enzymen die vetten afbreken tot glycerol en vetzuren.",
        False,
        "Gal bevat geen verteringsenzymen. De galzouten emulgeren alleen. De chemische afbraak gebeurt door lipase uit het alvleeskliersap.",
    ),
    M(
        "Waarom geeft de alvleesklier natriumwaterstofcarbonaat (NaHCO₃) af aan de twaalfvingerige darm?",
        [
            "om het zure maagsap te neutraliseren, zodat de darmenzymen kunnen werken",
            "om de eiwitten in de darm af te breken tot losse aminozuren en kleine peptiden",
            "om de vetten in de darm te emulgeren tot kleine druppeltjes",
            "om de bacteriën in de dunne darm te doden voor ze zich vermenigvuldigen",
        ],
        0,
        "De voedselbrij uit de maag is zeer zuur. NaHCO₃ neutraliseert dat, zodat enzymen zoals trypsine en lipase bij een licht basische pH werken.",
    ),
    M(
        "Welke enzymen zitten in het alvleeskliersap? Kruis alles aan wat juist is.",
        ["amylase", "trypsine", "lactase", "pepsine"],
        [0, 1],
        "Het alvleeskliersap bevat amylase voor zetmeel, trypsine voor eiwitten en lipase voor vetten. Pepsine komt uit de maag, en lactase zit in de wand van de dunne darm.",
    ),
    M(
        "Wat is het eindproduct van de volledige vertering van zetmeel?",
        ["glucose", "aminozuren", "glycerol en vetzuren", "maltose"],
        0,
        "Amylase knipt zetmeel tot maltose, en maltase knipt maltose verder tot glucose. Glucose wordt opgenomen.",
    ),
    I(
        "Welk enzym in de dunne darm splitst melksuiker in glucose en galactose?",
        "lactase",
        "Lactase breekt lactose af. Wie te weinig lactase heeft, verteert melksuiker slecht en heeft last van lactose-intolerantie.",
    ),
    M(
        "Wat is het verschil tussen endopeptidasen en exopeptidasen?",
        [
            "endopeptidasen knippen midden in een eiwitketen, exopeptidasen knippen aminozuren van de uiteinden",
            "endopeptidasen werken in de maag, exopeptidasen enkel in de mond",
            "endopeptidasen breken vetten af, exopeptidasen breken suikers af",
            "endopeptidasen bouwen eiwitten op, exopeptidasen breken ze af",
        ],
        0,
        "Endopeptidasen zoals pepsine en trypsine knippen eiwitten in kortere stukken. Exopeptidasen halen daarna aminozuren één voor één van de uiteinden.",
    ),
    W(
        "Sacharase splitst sacharose, de gewone suiker, in glucose en fructose.",
        True,
        "Sacharose is een disacharide uit glucose en fructose. Sacharase knipt de binding tussen beide.",
    ),
]

DEEL2 = [
    M(
        "Waarom heeft de binnenwand van de dunne darm plooien, darmvlokken en microvilli?",
        [
            "ze vergroten het oppervlak voor de opname van voedingsstoffen",
            "ze vertragen de doorgang van het voedsel zodat het langer gist",
            "ze maken gal aan voor de vertering van vetten",
            "ze beschermen de darm tegen het zure maagsap",
        ],
        0,
        "Darmplooien, villi en microvilli vergroten samen het opnameoppervlak enorm. Daardoor kunnen voedingsstoffen snel opgenomen worden.",
    ),
    I(
        "Hoe noemt men de vele microvilli samen aan de binnenkant van een darmepitheelcel?",
        "borstelzoom",
        "Onder de microscoop lijken de microvilli op de haren van een borstel. Daarom heet die rand de borstelzoom.",
    ),
    M(
        "Wat is osmose?",
        [
            "water dat door een halfdoorlatend membraan naar de geconcentreerdste kant gaat",
            "opgeloste deeltjes die met ATP tegen hun concentratieverschil in door het membraan gaan",
            "grote deeltjes die de cel opneemt door ze in een blaasje te sluiten",
            "zouten die een eiwitpomp in het membraan naar buiten de cel duwt",
        ],
        0,
        "Bij osmose beweegt water door een halfdoorlatend membraan van een hypotone naar een hypertone oplossing, zonder dat de cel energie moet leveren.",
    ),
    M(
        "Welke transportvormen zijn passief en kosten de cel dus geen ATP? Kruis alles aan wat juist is.",
        ["diffusie", "gefaciliteerde diffusie", "osmose", "transport met een pomp"],
        [0, 1, 2],
        "Diffusie, gefaciliteerde diffusie en osmose volgen het concentratieverschil. Een pomp werkt ertegenin en kost ATP: dat is actief transport.",
    ),
    M(
        "Wat is gefaciliteerde diffusie?",
        [
            "passief transport via een transporteiwit, met het concentratieverschil mee",
            "actief transport tegen het concentratieverschil in, met energie uit ATP",
            "het opnemen van vloeistof door de cel via een kleine instulping van het membraan",
            "de verplaatsing van water door een membraan zonder dat er een eiwit aan te pas komt",
        ],
        0,
        "Bij gefaciliteerde diffusie helpt een transmembraaneiwit, zoals een glucosetransporter, de stof door het membraan. De beweging volgt het concentratieverschil, dus er is geen ATP nodig.",
    ),
    W(
        "Bij actief transport verplaatst een stof zich met het concentratieverschil mee, zodat de cel er geen energie voor nodig heeft.",
        False,
        "Bij actief transport gaat een stof net tegen het concentratieverschil in, van laag naar hoog. Pompen in het membraan doen dat met energie uit ATP.",
    ),
    M(
        "Een rode bloedcel komt in zuiver water terecht. Wat gebeurt er?",
        [
            "er stroomt water de cel in, zodat ze opzwelt en kan barsten",
            "er stroomt water de cel uit, zodat ze verschrompelt",
            "er gebeurt niets, want water gaat niet door het celmembraan",
            "de cel neemt zouten op uit het water en wordt groter",
        ],
        0,
        "Zuiver water is hypotoon tegenover de cel. Water stroomt door osmose naar binnen en de cel kan openbarsten.",
    ),
    I(
        "Hoe noemt men een oplossing met dezelfde osmotische waarde als de inhoud van de cel, zodat er netto geen water in of uit de cel stroomt?",
        "isotoon",
        "In een isotone oplossing blijft de cel even groot. Fysiologisch zout is daarom isotoon gemaakt met het bloed.",
    ),
    M(
        "Hoe worden glycerol en vetzuren na opname in de darmepitheelcel verder vervoerd?",
        [
            "ze worden weer vetten, verpakt in lipoproteïnen, en gaan naar het lymfevat",
            "ze gaan rechtstreeks via de leverpoortader naar de lever, net als glucose en aminozuren",
            "ze blijven in de darmepitheelcel opgeslagen tot ze daar verbrand worden",
            "ze verlaten het lichaam met de ontlasting zonder dat ze opgenomen worden",
        ],
        0,
        "In de darmepitheelcel worden vetten opnieuw opgebouwd en met eiwitten verpakt tot lipoproteïnedeeltjes. Die gaan naar het lymfevat in de darmvlok en komen pas later in het bloed.",
    ),
    M(
        "Via welk bloedvat gaan opgenomen glucose en aminozuren van de darm naar de lever?",
        ["via de leverpoortader", "via de aorta", "via de longader", "via de onderste holle ader rechtstreeks"],
        0,
        "Het bloed uit de darmen gaat eerst via de leverpoortader naar de lever. Die verwerkt de opgenomen stoffen voor ze in de grote bloedsomloop komen.",
    ),
    W(
        "Het meeste water uit het voedsel en de verteringssappen wordt in de dikke darm opgenomen, en niet in de dunne darm.",
        False,
        "Het grootste deel van het water wordt al in de dunne darm opgenomen. De dikke darm neemt nog een deel op en dikt de ontlasting zo in.",
    ),
    M(
        "Wat zijn essentiële voedingsstoffen?",
        [
            "stoffen die het lichaam nodig heeft maar niet zelf kan maken",
            "stoffen die het lichaam altijd zelf kan maken uit glucose",
            "stoffen die enkel een rol spelen bij de vertering in de darm",
            "stoffen die het lichaam nooit opneemt en meteen uitscheidt",
        ],
        0,
        "Essentiële aminozuren, essentiële vetzuren, vitaminen en mineralen moet je met de voeding binnenkrijgen, want je lichaam maakt ze niet.",
    ),
    M(
        "Welke vitaminen zijn vetoplosbaar? Kruis alles aan wat juist is.",
        ["vitamine A", "vitamine D", "vitamine B12", "vitamine C"],
        [0, 1],
        "De vetoplosbare vitaminen zijn A, D, E en K. Vitamine C en de B-vitaminen zijn wateroplosbaar.",
    ),
    M(
        "Welk vetzuur is een voorbeeld van een essentieel vetzuur?",
        ["een omega-3-vetzuur", "een verzadigd vetzuur uit boter", "glycerol", "cholesterol"],
        0,
        "Omega-3- en omega-6-vetzuren kan het lichaam niet zelf maken. Ze moeten uit de voeding komen, bijvoorbeeld uit vette vis of noten.",
    ),
    M(
        "Wat doen voedingsvezels in de darm?",
        [
            "ze geven volume aan de darminhoud en houden de stoelgang vlot",
            "ze worden volledig verteerd tot glucose in de dunne darm",
            "ze maken samen met de lever de gal aan voor de vertering van vetten",
            "ze breken in de maag de eiwitten af tot losse aminozuren",
        ],
        0,
        "Vezels worden door onze enzymen niet verteerd. Ze houden water vast, geven volume en dienen als voedsel voor de darmflora.",
    ),
    M(
        "Wat doet de darmflora voor ons? Kruis alles aan wat juist is.",
        [
            "ze maakt vitamine K aan",
            "ze helpt het immuunsysteem en houdt ziekteverwekkers weg",
            "ze breekt een deel van de voedingsvezels af",
            "ze maakt gal aan voor de vertering van vetten",
        ],
        [0, 1, 2],
        "De goede bacteriën in de darm maken onder meer vitamine K, verdringen schadelijke bacteriën en breken vezels af. Gal komt uit de lever.",
    ),
    W(
        "Escherichia coli komt normaal voor in de dikke darm en maakt er onder meer vitamine K aan.",
        True,
        "E. coli is een gewone bewoner van de dikke darm. Buiten de darm, of als een ziekmakende variant, kan ze wel problemen geven.",
    ),
    M(
        "Wat is coeliakie?",
        [
            "een auto-immuunziekte waarbij gluten de darmvlokken beschadigen",
            "een bacteriële infectie van de maag door Helicobacter pylori",
            "een ontsteking door Salmonella na het eten van besmette eieren",
            "een tekort aan lactase waardoor melksuiker slecht verteerd wordt",
        ],
        0,
        "Bij coeliakie reageert het afweersysteem op gluten en beschadigt het de darmvlokken. De behandeling is een strikt glutenvrij dieet.",
    ),
    M(
        "Welke bacterie is een belangrijke oorzaak van maagzweren?",
        ["Helicobacter pylori", "Lactobacillus", "Escherichia coli uit de darmflora", "Salmonella"],
        0,
        "Helicobacter pylori kan overleven in de zure maag en de slijmlaag aantasten. Een maagzweer wordt dan behandeld met antibiotica en maagzuurremmers.",
    ),
    W(
        "De ziekte van Crohn is een chronische ontsteking die overal in het spijsverteringskanaal kan voorkomen.",
        True,
        "Crohn is een chronische darmontsteking die met periodes opflakkert. Ze komt het vaakst voor in het laatste stuk van de dunne darm en in de dikke darm.",
    ),
]

# -*- coding: utf-8 -*-
"""Enzymen, transport door membranen en osmose — 🌍 Beyond, biologie.

Deel 1 gaat over enzymen: het sleutel-slotprincipe, de activeringsenergie,
denaturatie en de grafieken van temperatuur, zuurtegraad, enzymconcentratie en
substraatconcentratie. Deel 2 gaat over passief en actief transport, over
osmose bij dierlijke en plantaardige cellen, en over endocytose en exocytose.

De fiche vraagt uitdrukkelijk om de grafieken hierover te kunnen lezen, dus
vragen de vragen ook naar de vorm van een curve en niet enkel naar de begrippen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een enzym?",
        opties=[
            "een eiwit dat een reactie versnelt",
            "een suiker die energie levert",
            "een vetzuur in een membraan",
            "een stuk DNA met een code",
        ],
        antwoord=0,
        uitleg="Een enzym is een biokatalysator: een eiwit dat een reactie in de cel "
        "versnelt zonder er zelf bij op te gaan.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke lettergreep eindigt de naam van bijna elk enzym?",
        antwoord=["ase", "-ase"],
        uitleg="Lactase, amylase, helicase, polymerase: de uitgang -ase verraadt een "
        "enzym, en het eerste deel verwijst naar het substraat of de reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het actief centrum van een enzym?",
        opties=[
            "de holte waarin het substraat past",
            "de kern van het enzym met zijn DNA",
            "het membraan rond het enzym",
            "de suikerketen op het enzym",
        ],
        antwoord=0,
        uitleg="Het actief centrum is het slot en het substraat de sleutel. Alleen een "
        "molecule met de juiste vorm past erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de tijdelijke verbinding van een enzym met zijn substraat?",
        opties=[
            "het enzym-substraatcomplex",
            "het co-enzym",
            "de inhibitor",
            "de cofactor",
        ],
        antwoord=0,
        uitleg="In het enzym-substraatcomplex zitten de twee even aan elkaar. Daarna "
        "laat het enzym de producten los en is het weer vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enzym verlaagt de activeringsenergie van een reactie.",
        antwoord=True,
        uitleg="Door het substraat in de juiste stand te houden, kost het minder energie "
        "om de reactie te starten. Daardoor verloopt ze bij lichaamstemperatuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enzym wordt bij de reactie zelf opgebruikt.",
        antwoord=False,
        uitleg="Een enzym komt er onveranderd uit en kan meteen een volgend substraat "
        "aanpakken. Daarom volstaat er heel weinig van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een enzym substraatspecifiek is?",
        opties=[
            "het past maar op één soort molecule",
            "het werkt bij elke temperatuur",
            "het zit altijd in een membraan",
            "het heeft geen cofactor nodig",
        ],
        antwoord=0,
        uitleg="Lactase splitst lactose en niets anders. De vorm van het actief centrum "
        "laat maar één substraat toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een enzym bij denaturatie?",
        opties=[
            "zijn ruimtelijke vorm gaat verloren",
            "zijn DNA wordt verdubbeld",
            "het wordt in een vesikel verpakt",
            "het wordt tot glucose afgebroken",
        ],
        antwoord=0,
        uitleg="Bij hoge temperatuur of een verkeerde zuurtegraad vouwt het eiwit open. "
        "Het actief centrum past dan niet meer en het enzym werkt niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een enzym werkt het best bij 37 °C. Wat gebeurt er bij 70 °C? Kruis alles aan wat juist is.",
        opties=[
            "het enzym denatureert",
            "de reactiesnelheid valt sterk terug",
            "de reactiesnelheid blijft stijgen",
            "het enzym wordt substraatspecifieker",
        ],
        antwoord=[0, 1],
        uitleg="Boven het temperatuursoptimum verliest het eiwit zijn vorm. De curve "
        "stijgt dus eerst, bereikt een top en valt daarna steil terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de temperatuur waarbij een enzym het snelst werkt?",
        antwoord=["temperatuursoptimum", "optimum", "temperatuuroptimum"],
        uitleg="Het temperatuursoptimum is de top van de curve. Bij de mens ligt dat "
        "voor de meeste enzymen rond 37 °C.",
    ),
    dict(
        type="meerkeuze",
        vraag="Pepsine in de maag werkt het best bij pH 2. Wat zegt dat?",
        opties=[
            "elk enzym heeft zijn eigen pH-optimum",
            "elk enzym werkt het best bij pH 7",
            "de zuurtegraad doet niets met een enzym",
            "pepsine is geen enzym",
        ],
        antwoord=0,
        uitleg="Pepsine hoort in het zure maagsap, trypsine in de basische dunne darm. "
        "Buiten hun pH-optimum denatureren ze.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer enzym je toevoegt bij voldoende substraat, hoe sneller de reactie verloopt.",
        antwoord=True,
        uitleg="Zolang er substraat genoeg is, geeft elke extra enzymmolecule extra "
        "omzetting. De grafiek is dan een stijgende rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom buigt de curve van de reactiesnelheid af als je steeds meer substraat toevoegt?",
        opties=[
            "alle enzymen zijn dan bezig",
            "het substraat denatureert dan",
            "de enzymen worden dan afgebroken",
            "de temperatuur stijgt dan te veel",
        ],
        antwoord=0,
        uitleg="Bij verzadiging is elk actief centrum bezet. De maximale reactiesnelheid "
        "is bereikt en meer substraat verandert er niets meer aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de toestand waarin elk actief centrum van de aanwezige enzymen bezet is?",
        antwoord=["verzadiging", "verzadigd"],
        uitleg="Bij verzadiging ligt de reactiesnelheid op haar maximum. De curve loopt "
        "dan horizontaal verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een inhibitor?",
        opties=[
            "de werking van een enzym remmen",
            "de werking van een enzym versnellen",
            "een enzym van een cofactor voorzien",
            "het substraat van een enzym aanmaken",
        ],
        antwoord=0,
        uitleg="Een inhibitor bezet het actief centrum of verandert de vorm van het "
        "enzym. Veel geneesmiddelen en gifstoffen werken zo.",
    ),
    dict(
        type="waarofniet",
        vraag="Een co-enzym is zelf een eiwit.",
        antwoord=False,
        uitleg="Een co-enzym is een kleine organische molecule, vaak uit een vitamine. "
        "Het helpt het enzym, maar is geen eiwit; een cofactor is vaak zelfs een ion.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke processen zijn enzymen onmisbaar? Kruis alles aan wat juist is.",
        opties=[
            "de spijsvertering",
            "de DNA-replicatie",
            "de diffusie van zuurstof",
            "het neerslaan van kalk in water",
        ],
        antwoord=[0, 1],
        uitleg="Elke stap van de spijsvertering en van de replicatie heeft haar eigen "
        "enzym. Diffusie verloopt van zichzelf en kalkaanslag is geen celproces.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker kookt een stukje lever en legt het dan in waterstofperoxide. Er gebeurt niets. Waarom?",
        opties=[
            "het catalase is gedenatureerd",
            "er zat geen catalase in de lever",
            "waterstofperoxide is geen substraat",
            "koken maakt het enzym specifieker",
        ],
        antwoord=0,
        uitleg="Rauwe lever doet waterstofperoxide schuimen door catalase. Na koken is "
        "het eiwit open gevouwen en werkt het niet meer.",
    ),
    dict(
        type="invultekst",
        vraag="Welk enzym splitst de melksuiker lactose?",
        antwoord=["lactase"],
        uitleg="Lactase splitst lactose in glucose en galactose. Wie het niet genoeg "
        "aanmaakt, verdraagt melk slecht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enzym bepaalt in welke richting een reactie uiteindelijk zal verlopen.",
        antwoord=False,
        uitleg="Een enzym versnelt alleen. Welke kant de reactie uitgaat, hangt af van "
        "de concentraties en de energie, niet van het enzym.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor passief transport? Kruis alles aan wat juist is.",
        opties=[
            "het kost de cel geen energie",
            "het volgt de concentratiegradiënt",
            "het gaat tegen de gradiënt in",
            "het gebeurt enkel bij plantencellen",
        ],
        antwoord=[0, 1],
        uitleg="Passief transport volgt de concentratiegradiënt, dus van veel naar "
        "weinig. Dat verloopt van zichzelf en kost geen ATP.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is diffusie?",
        opties=[
            "deeltjes spreiden zich van veel naar weinig",
            "deeltjes hopen zich op aan één kant",
            "water gaat door een membraan naar het zout",
            "een pomp duwt ionen naar buiten",
        ],
        antwoord=0,
        uitleg="Door hun eigen beweging verdelen deeltjes zich tot de concentratie "
        "overal gelijk is. Dan is er een evenwicht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het verschil in concentratie tussen twee kanten van een membraan?",
        antwoord=["concentratiegradiënt", "gradiënt", "concentratiegradient"],
        uitleg="De concentratiegradiënt is de drijvende kracht van diffusie en osmose. "
        "Is hij weg, dan stopt het netto transport.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een kanaaleiwit in een membraan?",
        opties=[
            "een gaatje vormen waardoor ionen gaan",
            "ionen tegen de gradiënt in pompen",
            "glucose afbreken tot pyruvaat",
            "het membraan stevig maken",
        ],
        antwoord=0,
        uitleg="Een kanaaleiwit vormt een doorgang met de juiste maat en lading. Het "
        "transport blijft passief: het volgt de gradiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat een aquaporine door?",
        opties=["water", "glucose", "natriumionen", "eiwitten"],
        antwoord=0,
        uitleg="Aquaporines zijn waterkanalen. Ze laten veel meer water per seconde door "
        "dan het blote membraan zou toelaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Geleide diffusie door een carriereiwit kost de cel ATP.",
        antwoord=False,
        uitleg="Een carriereiwit verandert wel van vorm, maar het transport volgt nog "
        "altijd de gradiënt. Het blijft dus passief en gratis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is osmose?",
        opties=[
            "water gaat door een membraan naar de hogere concentratie",
            "zout gaat door een membraan naar het water",
            "een pomp duwt water naar buiten",
            "een cel neemt een deeltje op in een blaasje",
        ],
        antwoord=0,
        uitleg="Bij osmose gaat het water door een halfdoorlaatbaar membraan naar de "
        "kant met de meeste opgeloste stof, want die stof zelf kan er niet door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt een dierlijke cel in zuiver water. Wat gebeurt er? Kruis alles aan wat juist is.",
        opties=[
            "er stroomt water de cel in",
            "de cel kan barsten",
            "de cel verschrompelt",
            "er stroomt water de cel uit",
        ],
        antwoord=[0, 1],
        uitleg="Zuiver water is hypotoon. Het water stroomt naar binnen en zonder "
        "celwand om de druk op te vangen, treedt cellyse op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een omgeving met dezelfde osmotische waarde als de cel?",
        antwoord=["isotoon", "isotone omgeving"],
        uitleg="In een isotone omgeving gaat er even veel water in als uit. Een "
        "fysiologische oplossing is daarom isotoon met ons bloed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt een plantencel in een sterke zoutoplossing. Wat gebeurt er?",
        opties=[
            "het cytoplasma trekt van de celwand weg",
            "de cel barst open",
            "de vacuole wordt groter",
            "de celwand lost op",
        ],
        antwoord=0,
        uitleg="Het water verlaat de vacuole en het cytoplasma krimpt los van de "
        "celwand. Dat is plasmolyse; in water komt het weer bij, deplasmolyse.",
    ),
    dict(
        type="waarofniet",
        vraag="Turgor is de druk waarmee een volle vacuole tegen de celwand duwt.",
        antwoord=True,
        uitleg="Die druk houdt een blad of een steel stevig. Verliest de plant water, "
        "dan daalt de turgor en gaat ze slap hangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom barst een plantencel niet in zuiver water, en een rode bloedcel wel?",
        opties=[
            "de plantencel heeft een celwand",
            "de plantencel laat geen water door",
            "de plantencel heeft geen vacuole",
            "de plantencel is isotoon met water",
        ],
        antwoord=0,
        uitleg="De celwand kan de druk van binnenuit opvangen. Een rode bloedcel heeft "
        "er geen en lyseert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de natrium-kaliumpomp?",
        opties=[
            "ze pompt tegen de gradiënt in met ATP",
            "ze laat ionen passief doorstromen",
            "ze pompt enkel water",
            "ze zit enkel in plantencellen",
        ],
        antwoord=0,
        uitleg="De pomp zet drie natriumionen naar buiten en twee kaliumionen naar "
        "binnen, tegen hun gradiënt in. Dat kost ATP en maakt actief transport.",
    ),
    dict(
        type="invultekst",
        vraag="Welke molecule levert de energie voor actief transport?",
        antwoord=["ATP", "atp"],
        uitleg="Bij de hydrolyse van ATP naar ADP en fosfaat komt energie vrij. Die "
        "gebruikt het transporteiwit om van vorm te veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een protonpomp?",
        opties=[
            "waterstofionen door een membraan pompen",
            "water in de cel pompen",
            "glucose afbreken",
            "eiwitten uit de cel brengen",
        ],
        antwoord=0,
        uitleg="Een protonpomp bouwt een protonengradiënt op. Die gradiënt wordt in het "
        "mitochondrion en de chloroplast gebruikt om ATP te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij endocytose brengt de cel iets naar buiten.",
        antwoord=False,
        uitleg="Endocytose is opnemen: het membraan plooit naar binnen en snijdt een "
        "blaasje af. Naar buiten brengen is exocytose.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het opnemen van een vast deeltje, bijvoorbeeld een bacterie, door een witte bloedcel?",
        opties=["fagocytose", "exocytose", "osmose", "plasmolyse"],
        antwoord=0,
        uitleg="Bij fagocytose omsluit de cel het deeltje. Het blaasje smelt daarna "
        "samen met een lysosoom, dat de inhoud afbreekt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij exocytose smelt een secretieblaasje samen met het celmembraan.",
        antwoord=True,
        uitleg="Het blaasje versmelt met het membraan en giet zijn inhoud naar buiten. "
        "Zo komt insuline of een enzym in het bloed of in de darm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een anabole reactie?",
        opties=[
            "ze bouwt grote moleculen op en kost energie",
            "ze breekt moleculen af en levert energie",
            "ze verloopt zonder enzym",
            "ze gebeurt enkel buiten de cel",
        ],
        antwoord=0,
        uitleg="Anabool is opbouwen, zoals eiwitsynthese en fotosynthese: endoenergetisch. "
        "Katabool is afbreken, zoals de celademhaling: exoenergetisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke processen zijn katabool? Kruis alles aan wat juist is.",
        opties=[
            "de celademhaling",
            "de spijsvertering",
            "de fotosynthese",
            "de eiwitsynthese",
        ],
        antwoord=[0, 1],
        uitleg="Celademhaling en spijsvertering breken moleculen af en leveren energie. "
        "Fotosynthese en eiwitsynthese bouwen op en kosten energie.",
    ),
]

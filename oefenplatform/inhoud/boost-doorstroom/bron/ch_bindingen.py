# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Chemische bindingen en roosters.

Hoort bij "atoom- en molecuulbouw" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_atoom] en [ch_pse].

Deel 1 gaat over het bepalen van het bindingstype uit het metaal- en
niet-metaalkarakter, over hoe elk bindingstype ontstaat, en over de
Lewisstructuur met haar bindende en vrije elektronenparen. Deel 2 gaat over de
vier roostertypes en over het verband met het smelt- en kookpunt, de
geleidbaarheid, de breekbaarheid en de glans, met diamant en grafiet als
uitgewerkt voorbeeld.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk bindingstype ontstaat tussen een metaal en een niet-metaal?",
        opties=[
            "een ionbinding",
            "een atoombinding",
            "een metaalbinding",
            "een waterstofbrug",
        ],
        antwoord=0,
        uitleg="Het metaal geeft elektronen af en het niet-metaal neemt ze op. De ionen die zo ontstaan trekken elkaar aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bindingstype ontstaat tussen twee niet-metalen?",
        opties=[
            "een atoombinding",
            "een ionbinding",
            "een metaalbinding",
            "een ion-dipoolkracht",
        ],
        antwoord=0,
        uitleg="Beide atomen willen elektronen opnemen, dus delen ze er een paar. Dat heet een atoombinding of covalente binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat een metaalbinding?",
        opties=[
            "de valentie-elektronen bewegen vrij tussen de ionen",
            "twee atomen delen elk één elektronenpaar",
            "een metaal geeft elektronen aan een niet-metaal",
            "de kernen van twee atomen smelten samen",
        ],
        antwoord=0,
        uitleg="De metaalatomen laten hun valentie-elektronen los. Die vormen een wolk die de positieve ionen bij elkaar houdt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen bevatten een ionbinding? Kruis alles aan wat juist is.",
        opties=[
            "NaCl",
            "MgO",
            "CO₂",
            "Cl₂",
        ],
        antwoord=[0, 1],
        uitleg="Natriumchloride en magnesiumoxide bestaan elk uit een metaal en een niet-metaal. CO₂ en Cl₂ bevatten enkel niet-metalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noemt men in een Lewisstructuur een bindend elektronenpaar?",
        opties=[
            "een paar dat door twee atomen gedeeld wordt",
            "een paar dat bij één atoom alleen blijft",
            "een paar dat vrij door het rooster beweegt",
            "een paar protonen in de kern",
        ],
        antwoord=0,
        uitleg="Een bindend paar vormt de binding zelf en wordt vaak als een streepje tussen de symbolen getekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noemt men een vrij elektronenpaar?",
        opties=[
            "een paar dat niet aan een binding deelneemt",
            "een paar dat twee atomen samenhoudt",
            "een paar dat tussen de metaalionen beweegt",
            "een paar dat in de kern van het atoom zit",
        ],
        antwoord=0,
        uitleg="Een vrij paar hoort bij één atoom en doet niet mee aan de binding. In water heeft het zuurstofatoom er twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bindende elektronenparen zitten er tussen de twee atomen in O₂?",
        opties=[
            "twee",
            "één",
            "drie",
            "vier",
        ],
        antwoord=0,
        uitleg="Zuurstof heeft zes valentie-elektronen en heeft er twee nodig. De twee atomen delen dus twee paren, een dubbele binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke binding zit er tussen de twee stikstofatomen in N₂?",
        opties=[
            "een drievoudige binding",
            "een enkelvoudige binding",
            "een dubbele binding",
            "een ionbinding",
        ],
        antwoord=0,
        uitleg="Stikstof heeft vijf valentie-elektronen en heeft er drie nodig. De atomen delen dus drie paren, en die binding is heel sterk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel atoombindingen vormt een koolstofatoom gewoonlijk?",
        opties=[
            "vier",
            "twee",
            "zes",
            "één",
        ],
        antwoord=0,
        uitleg="Koolstof heeft vier valentie-elektronen en heeft er vier nodig. Dat verklaart waarom de koolstofchemie zo rijk is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel vrije elektronenparen heeft het zuurstofatoom in een watermolecule?",
        opties=[
            "twee",
            "één",
            "drie",
            "geen",
        ],
        antwoord=0,
        uitleg="Zuurstof heeft zes valentie-elektronen. Twee gaan in de bindingen met waterstof, de vier andere vormen twee vrije paren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ionbinding zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er worden elektronen overgedragen",
            "er ontstaan geladen deeltjes",
            "er wordt een elektronenpaar gedeeld",
            "de binding komt enkel tussen metalen voor",
        ],
        antwoord=[0, 1],
        uitleg="Bij een ionbinding gaan elektronen over van het ene atoom naar het andere, en daardoor krijgen beide een lading. Delen hoort bij de atoombinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een atoombinding delen twee atomen een of meer elektronenparen.",
        antwoord=True,
        uitleg="Zo komen ze beide aan een volle buitenste schil zonder elektronen af te geven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaalbinding ontstaat tussen een metaal en een niet-metaal.",
        antwoord=False,
        uitleg="Een metaalbinding zit tussen metaalatomen onderling. Metaal met niet-metaal geeft een ionbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bindingstype kan je voorspellen uit het metaal- en niet-metaalkarakter van de elementen.",
        antwoord=True,
        uitleg="Metaal met niet-metaal geeft een ionbinding, niet-metaal met niet-metaal een atoombinding, en metaal met metaal een metaalbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="In een Lewisstructuur tekent men ook de elektronen uit de binnenste schillen.",
        antwoord=False,
        uitleg="Je tekent enkel de valentie-elektronen, want enkel die doen mee aan de bindingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dubbele binding bestaat uit twee gedeelde elektronen.",
        antwoord=False,
        uitleg="Het zijn twee gedeelde páren, dus vier elektronen. Enkelvoudig is één paar en drievoudig drie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een atoombinding met een ander, gelijkwaardig woord?",
        antwoord=["covalente binding", "covalent", "een covalente binding"],
        uitleg="Covalent betekent dat de atomen samen over de elektronen beschikken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel atoombindingen vormt een waterstofatoom?",
        antwoord=["1", "een", "één"],
        uitleg="Waterstof heeft één valentie-elektron en heeft er één nodig, dus vormt het precies één binding.",
    ),
    dict(
        type="invultekst",
        vraag="Welke formule hoort bij de verbinding van magnesium en chloor?",
        antwoord=["MgCl2", "MgCl₂"],
        uitleg="Magnesium geeft twee elektronen af en chloor neemt er één op. Er zijn dus twee chloride-ionen nodig per magnesiumion.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de schrijfwijze die per ionverbinding de kleinste verhouding van de ionen geeft?",
        antwoord=["formule-eenheid", "een formule-eenheid", "formule eenheid"],
        uitleg="In een ionrooster bestaan geen losse moleculen, dus geeft de formule enkel de verhouding.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen hebben een ionrooster? Kruis alles aan wat juist is.",
        opties=[
            "natriumchloride",
            "magnesiumoxide",
            "diamant",
            "ijzer",
        ],
        antwoord=[0, 1],
        uitleg="Bij een metaal met een niet-metaal liggen positieve en negatieve ionen afwisselend in een rooster. Diamant heeft een atoomrooster en ijzer een metaalrooster.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk roostertype hoort bij diamant?",
        opties=[
            "een atoomrooster",
            "een ionrooster",
            "een molecuulrooster",
            "een metaalrooster",
        ],
        antwoord=0,
        uitleg="Alle koolstofatomen zitten met atoombindingen aan elkaar in één doorlopend rooster. Daarom is diamant zo hard.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een stof met een ionrooster een hoog smeltpunt?",
        opties=[
            "de aantrekking tussen de ionen is sterk",
            "de ionen zijn zwaarder dan moleculen",
            "een ionrooster geleidt elektriciteit",
            "de ionen hebben geen lading",
        ],
        antwoord=0,
        uitleg="Om te smelten moet je de aantrekking tussen de tegengesteld geladen ionen overwinnen, en die is krachtig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hebben stoffen met een molecuulrooster vaak een laag smeltpunt?",
        opties=[
            "de krachten tussen de moleculen zijn zwak",
            "de bindingen in de moleculen zijn zwak",
            "de moleculen hebben geen massa",
            "er zijn geen bindingen in de stof",
        ],
        antwoord=0,
        uitleg="De moleculen zelf zitten stevig aan elkaar, maar de krachten tussen de moleculen zijn zwak. Net die moet je overwinnen om te smelten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt een metaal elektriciteit?",
        opties=[
            "de elektronen kunnen vrij bewegen",
            "de ionen kunnen vrij bewegen",
            "er zitten geen elektronen in",
            "de atomen trillen snel",
        ],
        antwoord=0,
        uitleg="In een metaalrooster is er een wolk van vrije elektronen. Zet je een spanning aan, dan bewegen die allemaal dezelfde kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer geleidt een zout elektriciteit? Kruis alles aan wat juist is.",
        opties=[
            "als het opgelost is in water",
            "als het gesmolten is",
            "als het als vaste stof in de pot zit",
            "als het in de koelkast staat",
        ],
        antwoord=[0, 1],
        uitleg="Er moeten vrij bewegende ladingen zijn. In het vaste rooster zitten de ionen vast; opgelost of gesmolten kunnen ze bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een zoutkristal breekbaar?",
        opties=[
            "bij verschuiving komen gelijke ladingen naast elkaar",
            "het rooster bevat te weinig ionen",
            "de ionen hebben geen lading",
            "er zitten luchtbellen in het kristal",
        ],
        antwoord=0,
        uitleg="Schuift een laag ionen een plaatsje op, dan liggen plus bij plus en min bij min. Die afstoting splijt het kristal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een metaal vervormbaar en een zoutkristal niet?",
        opties=[
            "de elektronenwolk houdt de ionen samen bij verschuiving",
            "een metaal heeft geen rooster",
            "een metaal bestaat uit moleculen",
            "een metaal heeft een laag smeltpunt",
        ],
        antwoord=0,
        uitleg="In een metaal is de elektronenwolk niet aan een plaats gebonden. Schuiven de ionen op, dan houdt die wolk ze gewoon verder samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is grafiet zacht en diamant hard, al bestaan beide uit koolstof?",
        opties=[
            "in grafiet liggen de atomen in lagen die over elkaar schuiven",
            "in grafiet zitten de atomen verder van elkaar in de kern",
            "diamant bevat meer koolstofatomen per molecule",
            "grafiet heeft een ionrooster en diamant niet",
        ],
        antwoord=0,
        uitleg="Binnen een laag zijn de bindingen sterk, maar tussen de lagen zijn de krachten zwak. Daarom laten die lagen los.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen horen bij een metaalrooster? Kruis alles aan wat juist is.",
        opties=[
            "glans",
            "goede elektrische geleiding",
            "breekbaarheid bij een kleine stoot",
            "een laag smeltpunt bij elk metaal",
        ],
        antwoord=[0, 1],
        uitleg="Glans en geleiding komen allebei van de vrije elektronen. Metalen zijn juist vervormbaar, en de meeste hebben een hoog smeltpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het oxidatiegetal van zuurstof in de meeste verbindingen?",
        opties=[
            "−II",
            "+II",
            "−I",
            "0",
        ],
        antwoord=0,
        uitleg="Zuurstof neemt gewoonlijk twee elektronen op. In peroxiden is het wel −I, dus kijk altijd naar de formule.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vaste stof met een atoomrooster heeft een heel hoog smeltpunt.",
        antwoord=True,
        uitleg="Om te smelten moet je de atoombindingen van het hele rooster verbreken, en dat vraagt heel veel energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zout geleidt elektriciteit als vaste stof.",
        antwoord=False,
        uitleg="De ionen zitten dan vast in het rooster en kunnen niet bewegen. Pas opgelost of gesmolten geleidt het.",
    ),
    dict(
        type="waarofniet",
        vraag="De glans van een metaal komt van de vrije elektronen.",
        antwoord=True,
        uitleg="Die elektronen kaatsen het licht terug. Daarom glanst een vers gepolijst metaaloppervlak.",
    ),
    dict(
        type="waarofniet",
        vraag="In een enkelvoudige stof is het oxidatiegetal van het element nul.",
        antwoord=True,
        uitleg="Er is geen ander element dat elektronen naar zich toe trekt, dus blijft het getal op nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecuulrooster geleidt elektriciteit even goed als een metaalrooster.",
        antwoord=False,
        uitleg="In een molecuulrooster zitten de elektronen vast in de bindingen en zijn er geen vrije ladingen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk roostertype hoort bij ijzer?",
        antwoord=["metaalrooster", "een metaalrooster", "metaal"],
        uitleg="De ijzerionen liggen in een rooster met een wolk van vrije elektronen ertussen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk roostertype hoort bij vast koolstofdioxide?",
        antwoord=["molecuulrooster", "een molecuulrooster", "molecuul"],
        uitleg="De moleculen CO₂ blijven bestaan en liggen regelmatig naast elkaar. De krachten ertussen zijn zwak, dus gaat droogijs snel over in gas.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het oxidatiegetal van waterstof in HCl?",
        antwoord=["+I", "+1", "I"],
        uitleg="Chloor is het meest elektronegatieve van de twee, dus krijgt het de elektronen toegewezen. Waterstof houdt dan +I over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht die de positieve ionen in een metaal samenhoudt, en die van de vrije elektronen komt?",
        antwoord=["metaalbinding", "de metaalbinding"],
        uitleg="De elektronenwolk werkt als een soort lijm tussen de positieve metaalionen.",
    ),
]

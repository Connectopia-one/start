# -*- coding: utf-8 -*-
"""Organische reacties: substitutie en het radicalaire mechanisme — chemie.

🌍 Beyond. Deel 1 gaat over de begrippen waarmee je een organische reactie
indeelt: de aard van het aanvallende deeltje (elektrofiel, nucleofiel of
radicaal), de aard van de splitsing (homolytisch of heterolytisch) en de vier
reactietypes, en over de radicalaire substitutie bij een alkaan met haar drie
stappen initiatie, propagatie en terminatie. Deel 2 gaat over de andere
substituties: de elektrofiele substitutie bij benzeen en de nucleofiele
substitutie bij een halogeenalkaan en bij een alcohol, met het product dat
daarbij ontstaat.

Een reactiemechanisme tekenen kan op het scherm niet. De vragen vragen dus naar
de naam van een stap, naar het soort deeltje dat aanvalt, en naar de naam en de
stofklasse van het product.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een homolytische splitsing?",
        opties=[
            "elk atoom houdt één elektron van het bindende paar",
            "één atoom houdt het hele bindende paar",
            "er komt een proton vrij uit de binding",
            "er ontstaan twee ionen met tegengestelde lading",
        ],
        antwoord=0,
        uitleg="Zo ontstaan er twee radicalen. Bij een heterolytische splitsing krijg je "
        "een positief en een negatief deeltje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een radicaal?",
        opties=[
            "een deeltje met een ongepaard elektron",
            "een deeltje met een positieve lading",
            "een deeltje met een vrij elektronenpaar",
            "een deeltje met twee dubbele bindingen",
        ],
        antwoord=0,
        uitleg="Dat ene elektron maakt het heel reactief. Licht of warmte kan een binding "
        "homolytisch splitsen en zo radicalen maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een aanvallend deeltje dat een vrij elektronenpaar aanbiedt?",
        antwoord=["nucleofiel", "een nucleofiel", "nucleofiele"],
        uitleg="Het zoekt een plaats met een elektronentekort. Een elektrofiel doet net "
        "het omgekeerde: het zoekt elektronen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zoekt een elektrofiel in een molecule?",
        opties=[
            "een plaats met veel elektronen, zoals een dubbele binding",
            "een plaats met een elektronentekort, zoals een positief atoom",
            "een plaats met een ongepaard elektron, zoals een radicaal",
            "een plaats met een waterstofatoom dat kan weggaan",
        ],
        antwoord=0,
        uitleg="Elektrofiel betekent letterlijk elektronenvriend. Daarom valt het de "
        "pi-elektronen van een alkeen of een benzeenring aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een substitutiereactie wordt een atoom of groep vervangen door een andere.",
        antwoord=True,
        uitleg="Bij een additie komt er iets bij zonder dat er iets weggaat, en bij een "
        "eliminatie gaat er iets weg zonder dat er iets bij komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk reactietype hoort bij het vormen van een ester uit een alcohol en een carbonzuur?",
        opties=[
            "een condensatie, want er komt water vrij",
            "een additie, want er komt een molecule bij",
            "een eliminatie, want er gaat een groep weg",
            "een radicalaire substitutie met twee radicalen",
        ],
        antwoord=0,
        uitleg="Twee moleculen koppelen en een kleine molecule, hier water, gaat eruit. "
        "Dat is wat een condensatie kenmerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reactietypes bestaan er bij organische stoffen? Kruis alles aan wat juist is.",
        opties=[
            "substitutie",
            "additie",
            "neutralisatie",
            "precipitatie",
        ],
        antwoord=[0, 1],
        uitleg="De vier organische types zijn substitutie, additie, eliminatie en "
        "condensatie. Neutralisatie en neerslagvorming horen bij de anorganische chemie.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is er nodig om de radicalaire substitutie van een alkaan te starten?",
        antwoord=["uv-licht", "licht", "warmte"],
        uitleg="Dat licht splitst de binding in het dihalogeen homolytisch. Daarom heet "
        "die eerste stap de initiatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de initiatiestap van een radicalaire substitutie?",
        opties=[
            "het dihalogeen splitst homolytisch in twee radicalen",
            "een radicaal haalt een waterstofatoom van het alkaan",
            "twee radicalen koppelen tot een stabiele molecule",
            "het alkaan splitst in een positief en een negatief deeltje",
        ],
        antwoord=0,
        uitleg="Cl₂ wordt onder uv-licht twee chloorradicalen. Pas daarna kan de "
        "kettingreactie van de propagatie beginnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de propagatiestappen?",
        opties=[
            "een radicaal reageert en er ontstaat telkens een nieuw radicaal",
            "er ontstaan twee radicalen uit één molecule halogeen",
            "twee radicalen verdwijnen door samen te koppelen",
            "de reactie stopt doordat alle radicalen verbruikt zijn",
        ],
        antwoord=0,
        uitleg="Daardoor loopt de reactie als een ketting door. Eén lichtdeeltje kan zo "
        "duizenden moleculen laten reageren.",
    ),
    dict(
        type="waarofniet",
        vraag="In de terminatiestap ontstaan er twee nieuwe radicalen.",
        antwoord=False,
        uitleg="Daar koppelen twee radicalen juist tot een molecule zonder ongepaard "
        "elektron, en stopt die ketting. Daarom vindt men bij de chlorering van methaan "
        "ook wat ethaan in het mengsel terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de radicalaire substitutie van methaan met chloorgas?",
        opties=[
            "chloormethaan en waterstofchloride",
            "dichloormethaan en waterstofgas",
            "methanol en waterstofchloride",
            "etheen en waterstofchloride",
        ],
        antwoord=0,
        uitleg="Eén waterstofatoom wordt door chloor vervangen, en dat waterstofatoom "
        "gaat met het tweede chlooratoom mee als HCl.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een radicalaire substitutie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze verloopt in drie soorten stappen",
            "ze geeft een mengsel van verschillende producten",
            "ze verloopt met een nucleofiel als aanvaller",
            "ze geeft altijd één zuiver product",
        ],
        antwoord=[0, 1],
        uitleg="Er kan een tweede en een derde waterstofatoom vervangen worden. Daarom is "
        "de opbrengst van één bepaald product altijd beperkt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de laatste stap van een radicalaire kettingreactie?",
        antwoord=["terminatie", "de terminatie", "terminatiestap"],
        uitleg="Twee radicalen koppelen en de ketting stopt. De drie stappen zijn dus "
        "initiatie, propagatie en terminatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom reageert een alkaan niet met een elektrofiel?",
        opties=[
            "een alkaan heeft geen plaats met veel elektronen om aan te vallen",
            "een alkaan heeft te veel waterstofatomen in de weg staan",
            "een alkaan is te zwaar om door een elektrofiel geraakt te worden",
            "een alkaan heeft al een volledig gevulde dubbele binding",
        ],
        antwoord=0,
        uitleg="Alle bindingen zijn sigma-bindingen en bijna apolair. Daarom heeft een "
        "alkaan een radicaal nodig om toch te reageren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een eliminatiereactie?",
        opties=[
            "er gaat een kleine molecule uit de stof en er ontstaat een dubbele binding",
            "er komt een kleine molecule bij over een dubbele binding",
            "er wordt een atoom vervangen door een ander atoom",
            "er koppelen twee moleculen met verlies van water",
        ],
        antwoord=0,
        uitleg="Water of een waterstofhalogenide gaat eruit. De keten wordt daardoor "
        "onverzadigd.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een heterolytische splitsing ontstaan er twee radicalen.",
        antwoord=False,
        uitleg="Daar neemt één atoom het hele elektronenpaar mee, dus ontstaan er ionen. "
        "Twee radicalen komen van een homolytische splitsing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk soort deeltje valt aan bij de chlorering van een cycloalkaan onder uv-licht?",
        opties=[
            "een radicaal",
            "een elektrofiel",
            "een nucleofiel",
            "een proton",
        ],
        antwoord=0,
        uitleg="Een cycloalkaan is net als een alkaan verzadigd en apolair. Dus verloopt "
        "ook daar de substitutie radicalair.",
    ),
    dict(
        type="waarofniet",
        vraag="Een substitutie kan radicalair, elektrofiel of nucleofiel verlopen.",
        antwoord=True,
        uitleg="Welk van de drie het is, hangt af van de stof: een alkaan radicalair, "
        "benzeen elektrofiel en een halogeenalkaan nucleofiel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reactie waarbij twee moleculen koppelen en er water vrijkomt?",
        antwoord=["condensatie", "een condensatie", "condensatiereactie"],
        uitleg="De verestering is daarvan het bekendste voorbeeld. De omgekeerde reactie "
        "met water heet hydrolyse.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom ondergaat benzeen een substitutie en geen additie met broom?",
        opties=[
            "bij een additie zou de ring zijn stabiele elektronenwolk verliezen",
            "bij een additie zou de ring te veel waterstofatomen krijgen",
            "benzeen heeft geen dubbele bindingen om een additie te doen",
            "benzeen is te zwaar om een additie te kunnen ondergaan",
        ],
        antwoord=0,
        uitleg="De verspreide pi-elektronen maken benzeen bijzonder stabiel. Een "
        "substitutie houdt die ring intact.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de reactie van benzeen met broom in aanwezigheid van een katalysator?",
        opties=[
            "broombenzeen en waterstofbromide",
            "dibroombenzeen en waterstofgas",
            "broomcyclohexaan en waterstofbromide",
            "benzeenbromide en broomwaterstof",
        ],
        antwoord=0,
        uitleg="Eén waterstofatoom van de ring wordt vervangen door broom. Het andere "
        "broomatoom gaat met dat waterstofatoom mee als HBr.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort deeltje valt benzeen aan bij een substitutie?",
        antwoord=["elektrofiel", "een elektrofiel", "elektrofiele"],
        uitleg="De ring is rijk aan elektronen, dus trekt ze een deeltje met een "
        "elektronentekort aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de nucleofiele substitutie van een halogeenalkaan met water?",
        opties=[
            "een alcohol",
            "een ether",
            "een ester",
            "een amine",
        ],
        antwoord=0,
        uitleg="Het water valt met zijn vrij elektronenpaar aan en neemt de plaats van "
        "het halogeen in. Het halogeen gaat als ion weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een nucleofiele substitutie verlaat het halogeen de molecule als ion.",
        antwoord=True,
        uitleg="De binding splitst heterolytisch: het halogeen neemt het elektronenpaar "
        "mee. Daarom vind je het in de oplossing terug als chloride- of bromide-ion.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de reactie van een halogeenalkaan met een alcohol?",
        opties=[
            "een ether",
            "een ester",
            "een carbonzuur",
            "een aldehyde",
        ],
        antwoord=0,
        uitleg="De alcohol valt aan met het vrij paar van haar zuurstofatoom. Zo ontstaat "
        "een zuurstofbrug tussen twee koolstofketens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen kunnen als nucleofiel een halogeenalkaan aanvallen? Kruis alles aan wat juist is.",
        opties=[
            "water",
            "een amine",
            "een alkaan",
            "een radicaal",
        ],
        antwoord=[0, 1],
        uitleg="Allebei hebben ze een vrij elektronenpaar, op zuurstof of op stikstof. Een "
        "alkaan heeft er geen en een radicaal valt op een andere manier aan.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stofklasse ontstaat er uit een alcohol en een carbonzuur?",
        antwoord=["ester", "een ester", "esters"],
        uitleg="Die reactie heet de verestering en is een condensatie, want er komt water "
        "vrij. Veel esters ruiken naar fruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de reactie van twee alcoholen met elkaar?",
        opties=[
            "een ether en water",
            "een ester en water",
            "een aldehyde en waterstofgas",
            "een carbonzuur en water",
        ],
        antwoord=0,
        uitleg="De ene alcohol valt de andere aan en er gaat water uit. Het resultaat is "
        "een zuurstofbrug tussen de twee ketens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een nucleofiele substitutie bij een halogeenalkaan zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het koolstofatoom naast het halogeen is lichtpositief",
            "het nucleofiel valt juist dat koolstofatoom aan",
            "het halogeen valt zelf het nucleofiel aan",
            "de binding splitst homolytisch in twee radicalen",
        ],
        antwoord=[0, 1],
        uitleg="Het halogeen is sterk elektronegatief en trekt de elektronen naar zich "
        "toe. Daardoor ontstaat er net een plaats met een elektronentekort.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alkaan reageert makkelijker met een nucleofiel dan een halogeenalkaan.",
        antwoord=False,
        uitleg="Omgekeerd: de polaire C-X-binding van een halogeenalkaan maakt het "
        "koolstofatoom lichtpositief. In een alkaan is er geen enkele plaats met zo'n "
        "tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft de elektrofiele substitutie van benzeen een katalysator nodig?",
        opties=[
            "de katalysator maakt het broom pas echt elektrofiel",
            "de katalysator verlaagt de temperatuur van de reactie",
            "de katalysator breekt de ring van benzeen eerst open",
            "de katalysator levert het waterstofatoom dat weggaat",
        ],
        antwoord=0,
        uitleg="Met een stof als ijzerbromide wordt het broommolecule gepolariseerd. Dan "
        "is het sterk genoeg om de stabiele ring aan te vallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk product ontstaat er bij de reactie van broomethaan met ammoniak?",
        opties=[
            "een amine",
            "een amide",
            "een alcohol",
            "een ether",
        ],
        antwoord=0,
        uitleg="Het vrije paar van de stikstof valt het koolstofatoom aan. Het broom gaat "
        "weg als bromide-ion.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de verestering zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er komt water vrij bij de reactie",
            "ze is omkeerbaar met water als reagens",
            "er komt waterstofgas vrij bij de reactie",
            "ze verloopt met een radicaal als aanvaller",
        ],
        antwoord=[0, 1],
        uitleg="Met water en een zuur als katalysator breekt de ester weer in alcohol en "
        "carbonzuur. Dat heet hydrolyse.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reactie waarbij een ester met water terug uiteenvalt?",
        antwoord=["hydrolyse", "een hydrolyse", "verzeping"],
        uitleg="Met een base heet dat verzeping, en dan ontstaat het zout van het "
        "carbonzuur. Dat is hoe zeep gemaakt wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de substitutie bij een halogeenalkaan nucleofiel?",
        opties=[
            "het aanvallende deeltje brengt zelf een elektronenpaar mee",
            "het aanvallende deeltje heeft een ongepaard elektron",
            "het aanvallende deeltje zoekt naar elektronen in de molecule",
            "het aanvallende deeltje is altijd een halogeen",
        ],
        antwoord=0,
        uitleg="De naam van een substitutie komt van het soort aanvaller: radicalair, "
        "elektrofiel of nucleofiel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschillen zijn er tussen de chlorering van methaan en die van benzeen?",
        opties=[
            "bij methaan valt een radicaal aan, bij benzeen een elektrofiel",
            "bij methaan valt een nucleofiel aan, bij benzeen een radicaal",
            "bij methaan is er een katalysator nodig en bij benzeen niet",
            "bij methaan blijft de ring intact en bij benzeen niet",
        ],
        antwoord=0,
        uitleg="Methaan heeft uv-licht nodig, benzeen een katalysator. In beide gevallen "
        "wordt er een waterstofatoom vervangen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een nucleofiele substitutie van een alcohol met een carbonzuur ontstaat er een ether.",
        antwoord=False,
        uitleg="Dan ontstaat er een ester. Een ether krijg je uit twee alcoholen of uit "
        "een alcohol met een halogeenalkaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een substitutie verandert het aantal koolstofatomen van de hoofdketen niet.",
        antwoord=True,
        uitleg="Er wordt alleen een atoom of groep vervangen. Bij een condensatie komen "
        "twee ketens juist aan elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Welk ion verlaat de molecule bij de nucleofiele substitutie van broomethaan?",
        antwoord=["bromide-ion", "bromide", "Br-"],
        uitleg="Het neemt het hele bindende elektronenpaar mee. Daarom is die splitsing "
        "heterolytisch.",
    ),
]

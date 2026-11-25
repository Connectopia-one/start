# -*- coding: utf-8 -*-
"""Uitdaging Geschiedenis 🚀 Boost dubbele finaliteit (25 november 2026), in
de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen, van Rome en de Franken tot de revoluties en
het Ottomaanse Rijk. Een tijdlijn en een verzonnen bron om op te klikken,
tabellen, keuzelijsten, koppelen, sorteren, volgorde en een open vraag. Geen
nieuwe leerstof: alles staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_geschiedenis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Geschiedenis"
BESTAND = "boost-df-geschiedenis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/geschiedenis-boost-df-uitdaging"
TIJDLIJN = "tijdlijn-periodes.svg"
BRIEF = "brief-pest-1349.svg"
# klikvakken: zie maak_prenten_boost_df_geschiedenis.py
OUDHEID = [5.0, 40.5, 22.5, 26.2]
MIDDELEEUWEN = [27.5, 40.5, 48.1, 26.2]
NIEUWE_TIJD = [75.7, 40.5, 14.1, 26.2]


def regel(i, n=6):
    """Klikvak van zin i (vanaf 1) in de brief."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Tijdlijn (prent)
    klik("Bekijk de tijdlijn. Klik op de periode waarin de Guldensporenslag plaatsvond.",
         TIJDLIJN, [MIDDELEEUWEN],
         "De Guldensporenslag was in 1302. Dat valt in de middeleeuwen, die lopen van 476 tot ongeveer 1492."),
    klik("Klik op de periode waarin de driehoekshandel tussen Europa, Afrika en Amerika op gang kwam.",
         TIJDLIJN, [NIEUWE_TIJD],
         "Na de ontdekkingsreizen vanaf 1492 ontstonden kolonies in Amerika. De driehoekshandel hoort bij de Nieuwe Tijd."),
    klik("Klik op de periode waarin de Romeinen over onze gewesten heersten.",
         TIJDLIJN, [OUDHEID],
         "Het Romeinse Rijk hoort bij de oudheid. Het West-Romeinse Rijk viel symbolisch in 476."),
    met_prent(TIJDLIJN, tabel(
        "Welke gebeurtenis gebruikt men als grens bij dit jaartal?",
        [
            ("476", "Val van het West-Romeinse Rijk"),
            ("1492", "Columbus bereikt Amerika"),
            ("1789", "Franse Revolutie"),
        ],
        "Historici kiezen een symbolische gebeurtenis als grens tussen twee periodes: de val van Rome, de reis van Columbus en de Franse Revolutie.",
        kolommen=["Val van het West-Romeinse Rijk", "Columbus bereikt Amerika", "Franse Revolutie"])),
    met_prent(TIJDLIJN, mk(
        "Waarom zijn de grenzen op deze tijdlijn eerder afspraken dan harde breuken?",
        ["De samenleving verandert niet overal tegelijk.", "Historici weten niet in welk jaar de gebeurtenissen plaatsvonden.", "Elke grens werd door één vorst gekozen en daarna overal ingevoerd.", "Na elke grens begon de tijdrekening opnieuw bij het jaar nul."],
        0,
        "Een periodegrens is een symbolische datum. Veranderingen in economie, cultuur en politiek lopen niet gelijk en verschillen van plaats tot plaats.")),

    # Bron: brief over de pest (prent)
    klik("Lees de verzonnen brief. Klik op de zin waarin de schrijver zegt dat hij iets met eigen ogen gezien heeft.",
         BRIEF, [regel(3)],
         "In zin 3 is de schrijver ooggetuige: hij heeft de kar zelf zien rijden. In zin 4 geeft hij door wat anderen zeggen."),
    klik("Klik op de zin waarin de schrijver uit een gerucht iets besluit over een hele groep mensen.",
         BRIEF, [regel(5)],
         "Uit een gerucht over enkele kooplui besluit de schrijver iets over alle vreemdelingen. Dat is een veralgemening."),
    met_prent(BRIEF, tabel(
        "Klopt dit over de brief?",
        [
            ("Zin 1 geeft de plaats en de datum van de bron.", J),
            ("De brief is een bron uit de Nieuwe Tijd.", F),
            ("Zin 4 bewijst dat de kooplui de pest meebrachten.", F),
            ("Zin 6 toont hoe veel mensen toen de ramp verklaarden.", J),
        ],
        "1349 valt in de middeleeuwen. Zin 4 geeft een gerucht weer, geen bewijs. Zin 6 toont een opvatting uit die tijd: de pest als straf van God.")),
    met_prent(BRIEF, mk(
        "Wat voor bron zou deze brief zijn, als hij echt was?",
        ["een primaire bron, want hij komt uit de tijd zelf", "een secundaire bron, want hij is met de hand geschreven", "een secundaire bron, want de schrijver is een koopman", "geen bron, want er staan meningen in die niet kloppen"],
        0,
        "Een primaire bron komt uit de tijd die je onderzoekt. Ook een bron met meningen of fouten is bruikbaar: ze toont hoe mensen toen dachten.")),
    met_prent(BRIEF, keuze(
        "Zin 6 hoort vooral bij het [[*culturele|economische|politieke]] domein. De pest liet de bevolking sterk [[*dalen|stijgen]].",
        "Geloof en verklaringen van de wereld horen bij het culturele domein. De zwarte dood doodde een groot deel van de bevolking van Europa.")),

    # Rome en de Franken
    volgorde(
        "Zet deze gebeurtenissen in de juiste volgorde.",
        ["de val van het West-Romeinse Rijk", "de doop van Clovis", "de keizerskroning van Karel de Grote", "het verdrag van Verdun", "de Guldensporenslag", "de zwarte dood in Europa"],
        "476, rond 500, 800, 843, 1302 en vanaf 1347."),
    mk("Waarom viel het Frankische Rijk telkens weer uiteen in kleinere delen?",
       ["Bij de dood van een koning kreeg elke zoon een deel.", "De paus verdeelde na elke kroning het land onder de bisschoppen.", "De Romeinen veroverden telkens een deel van het rijk terug.", "De graven kozen bij elke nieuwe koning een eigen hoofdstad."],
       0,
       "Het Frankische erfrecht verdeelde het rijk onder de zonen. Zo viel het na Karel de Grote uiteen, onder meer bij het verdrag van Verdun."),

    # Middeleeuwse samenleving
    tabel(
        "Bij welke stand hoort deze taak in de middeleeuwse driedeling?",
        [
            ("bidden voor het zielenheil van iedereen", "Geestelijkheid"),
            ("het land verdedigen met de wapens", "Adel"),
            ("het land bewerken en voedsel voortbrengen", "Derde stand"),
        ],
        "De middeleeuwse samenleving zag drie standen: wie bidt, wie vecht en wie werkt.",
        kolommen=["Geestelijkheid", "Adel", "Derde stand"]),
    koppel(
        "Koppel elk begrip aan zijn betekenis.",
        [
            ["horige", "onvrije boer die gebonden is aan het domein van zijn heer"],
            ["ambacht", "vereniging van ambachtslui met hetzelfde beroep"],
            ["keure", "document met de rechten van een stad"],
            ["leenman", "edelman die land krijgt in ruil voor trouw en hulp"],
        ],
        ["vrije boer die zijn eigen land in eigendom heeft"],
        "Op het domein werkten horigen voor de heer. In de steden verenigden ambachtslui zich in ambachten, en een keure legde de stadsrechten vast. Een leenman kreeg een leen van een leenheer."),
    sorteer(
        "Is dit kenmerk romaans of gotisch?",
        ["Romaans", "Gotisch"],
        [
            ["ronde bogen", "Romaans"],
            ["spitsbogen", "Gotisch"],
            ["dikke muren met kleine vensters", "Romaans"],
            ["grote glasramen met veel licht", "Gotisch"],
            ["luchtbogen en steunberen aan de buitenkant", "Gotisch"],
        ],
        "Romaanse kerken hebben dikke muren die het dak dragen, en dus weinig vensters. Gotische bouwers leidden het gewicht af via spitsbogen, steunberen en luchtbogen, zodat er grote ramen konden komen."),
    keuze(
        "In 1302 versloeg een Vlaams leger met veel [[*stedelingen|ridders]] het leger van de Franse koning. Vlaamsgezinden vieren die slag later op [[*11 juli|21 juli]].",
        "Bij de Guldensporenslag vochten veel ambachtslui uit de steden. De Vlaamse Gemeenschap viert haar feestdag op 11 juli. Op 21 juli is de nationale feestdag van België."),

    inv("In welk jaar werd de Bastille in Parijs bestormd? Geef enkel het jaartal.",
        "1789",
        "Op 14 juli 1789 bestormde een menigte de Bastille. Die dag geldt als het begin van de Franse Revolutie."),
    tabel(
        "In welk maatschappelijk domein hoort dit vooral thuis?",
        [
            ("de handel in specerijen met Azië", "Economisch"),
            ("de kroning van een koning", "Politiek"),
            ("de verering van heiligen", "Cultureel"),
            ("de verhouding tussen heer en horige", "Sociaal"),
        ],
        "Economisch gaat over geld, handel en productie. Politiek over macht en bestuur. Cultureel over geloof, kunst en kennis. Sociaal over hoe groepen mensen samenleven.",
        kolommen=["Economisch", "Politiek", "Cultureel", "Sociaal"]),
    mk("Waarom zochten Portugezen en Spanjaarden in de 15de eeuw een zeeroute naar Azië?",
       ["Om de specerijen zonder dure tussenhandelaars te kopen.", "Om nieuwe kloosters te stichten in de Romeinse provincies.", "Omdat het Frankische Rijk de landroutes had afgesloten.", "Omdat de pest in Azië al lang verdwenen was en daar niet."],
       0,
       "Specerijen kwamen over land via Arabische, Ottomaanse en Venetiaanse tussenhandelaars en werden onderweg steeds duurder. Een eigen zeeroute moest dat omzeilen."),
    sorteer(
        "Hoort dit bij de Reformatie of bij de Contrareformatie?",
        ["Reformatie", "Contrareformatie"],
        [
            ["de Bijbel als enige bron van het geloof", "Reformatie"],
            ["het concilie van Trente", "Contrareformatie"],
            ["Luther en zijn kritiek op de aflaten", "Reformatie"],
            ["prachtige barokkerken die de gelovigen moeten raken", "Contrareformatie"],
        ],
        "De Reformatie van Luther brak met Rome. De katholieke Kerk antwoordde met de Contrareformatie: Trente legde de leer vast en de barokkunst moest de gelovigen opnieuw aanspreken."),
    keuze(
        "Na de dood van Karel de Grote werd zijn rijk in 843 bij het verdrag van [[*Verdun|Trente|Wenen]] verdeeld. Daaruit groeiden later de koninkrijken [[*Frankrijk en Duitsland|Spanje en Portugal]].",
        "Het verdrag van Verdun verdeelde het rijk onder de kleinzonen van Karel de Grote. Het westelijke deel werd later Frankrijk, het oostelijke Duitsland."),
    tabel(
        "Klopt dit over de middeleeuwse stad?",
        [
            ("Een stad kreeg haar rechten vaak van de vorst in een keure.", J),
            ("Ambachtslui met hetzelfde beroep verenigden zich in een ambacht.", J),
            ("In de stad waren alle inwoners horigen van een heer.", F),
            ("De stadsbevolking groeide mee met de handel.", J),
        ],
        "Stadslucht maakt vrij, zei men: wie in de stad woonde, was geen horige meer. Steden groeiden door handel en nijverheid en kregen eigen rechten."),

    # Nieuwe Wereld en driehoekshandel
    tabel(
        "Wat werd er vervoerd op elk traject van de driehoekshandel?",
        [
            ("van Europa naar West-Afrika", "Wapens, textiel en drank"),
            ("van West-Afrika naar Amerika", "Tot slaaf gemaakte mensen"),
            ("van Amerika naar Europa", "Suiker, katoen en tabak"),
        ],
        "Europese handelaars ruilden goederen in Afrika voor mensen, die als slaven naar de plantages in Amerika gingen. De producten van die plantages gingen naar Europa.",
        kolommen=["Wapens, textiel en drank", "Tot slaaf gemaakte mensen", "Suiker, katoen en tabak"]),
    tabel(
        "Was dit een gevolg van de Europese kolonisatie van Amerika?",
        [
            ("Een groot deel van de inheemse bevolking stierf aan ziekten uit Europa.", J),
            ("Grote gebieden werden met één gewas beplant voor de uitvoer.", J),
            ("De inheemse volken kregen meer politieke macht in Europa.", F),
            ("Er kwamen nieuwe gewassen zoals de aardappel naar Europa.", J),
        ],
        "De kolonisatie bracht ziekten, monocultuur en uitbuiting. De uitwisseling van gewassen veranderde ook de Europese landbouw. Politieke macht kregen de inheemse volken er niet bij."),

    # Humanisme, Reformatie, kunst
    koppel(
        "Koppel elke persoon aan wat bij hem past.",
        [
            ["Luther", "redding door het geloof alleen"],
            ["Erasmus", "humanist die de klassieke teksten bestudeerde"],
            ["Michelangelo", "beeldhouwer van de renaissance"],
            ["Rubens", "schilder van de barok"],
        ],
        ["absolute vorst die zei: de staat ben ik", "filosoof van de scheiding der machten"],
        "Luther begon de Reformatie, Erasmus was een humanist, Michelangelo maakte onder meer de David en Rubens is de grote barokschilder uit Antwerpen."),
    tabel(
        "Is dit kenmerk renaissance of barok?",
        [
            ("rust, evenwicht en klassieke verhoudingen", "Renaissance"),
            ("veel beweging, drama en sterke lichtcontrasten", "Barok"),
            ("kunst die de pracht van Kerk en vorst moet tonen", "Barok"),
            ("de mens zelf in het middelpunt, naar het voorbeeld van de oudheid", "Renaissance"),
        ],
        "De renaissance zocht harmonie en het menselijke, naar het voorbeeld van Grieken en Romeinen. De barok wil indruk maken: beweging, emotie, licht en donker.",
        kolommen=["Renaissance", "Barok"]),
    mk("Wat wilde de Kerk met het concilie van Trente?",
       ["De katholieke leer opnieuw vastleggen na de Reformatie.", "De protestantse leer van Luther overal officieel goedkeuren.", "De paus vervangen door een raad van verkozen vorsten uit Europa.", "Het Latijn als taal van de mis voorgoed laten verdwijnen."],
       0,
       "Met het concilie van Trente zette de katholieke Kerk haar leer op een rij en voerde ze hervormingen door. Dat heet de Contrareformatie."),

    # Vorsten, opstand en Verlichting
    keuze(
        "Lodewijk XIV regeerde als [[*absoluut|parlementair]] vorst: alle macht lag bij hem. Locke vond dat elke mens [[*natuurrechten|geen rechten]] heeft, zoals leven, vrijheid en bezit. Montesquieu pleitte voor de [[*scheiding der machten|macht van één vorst]].",
        "Het absolutisme legt alle macht bij één vorst. Verlichtingsdenkers als Locke en Montesquieu wilden die macht beperken met rechten en een verdeling van de macht."),
    volgorde(
        "Zet de gebeurtenissen in de Nederlanden in de juiste volgorde.",
        ["Karel V regeert over de Nederlanden", "de Beeldenstorm", "de Opstand tegen Filips II", "de scheiding tussen Noord en Zuid"],
        "Karel V werd opgevolgd door zijn zoon Filips II. Na de Beeldenstorm van 1566 brak de Opstand uit. Op het einde van de 16de eeuw scheidden de Noordelijke en de Zuidelijke Nederlanden."),
    tabel(
        "Klopt dit over de revoluties op het einde van de 18de eeuw?",
        [
            ("De Amerikaanse Onafhankelijkheidsverklaring dateert van 1776.", J),
            ("De Franse Revolutie begon met de bestorming van de Bastille.", J),
            ("Na de Franse Revolutie kreeg de adel er nieuwe voorrechten bij.", F),
            ("Beide revoluties steunden op ideeën van de Verlichting.", J),
        ],
        "De Amerikanen verklaarden zich in 1776 onafhankelijk. Op 14 juli 1789 werd de Bastille bestormd. De Franse Revolutie schafte de voorrechten van adel en geestelijkheid af."),

    # Industriële omwenteling
    keuze(
        "De industriële revolutie begon in [[*Groot-Brittannië|Frankrijk|de Nederlanden]]. Watt maakte de [[*stoommachine|spinmachine|drukpers]] zuiniger en bruikbaar voor allerlei fabrieken.",
        "Groot-Brittannië had steenkool, kapitaal, arbeidskrachten en een grote markt. De verbeterde stoommachine dreef fabrieken, treinen en schepen aan."),
    mk("Hoe verschilt een fabriek van een vroegere manufactuur?",
       ["In een fabriek doen machines het zware werk.", "In een manufactuur werkt men enkel thuis.", "Een fabriek maakt enkel voedsel voor de stad.", "Een manufactuur hoort bij de oudheid en niet later."],
       0,
       "In een manufactuur werkten veel arbeiders samen met de hand. In een fabriek draaien machines, aangedreven door bijvoorbeeld stoom."),
    tabel(
        "Is dit een aanbodfactor voor de industriële revolutie?",
        [
            ("veel steenkool en ijzererts in de grond", J),
            ("kapitaal van rijke handelaars", J),
            ("arbeidskrachten die van het platteland naar de stad trokken", J),
            ("een daling van de bevolking", F),
        ],
        "Aanbodfactoren maken de productie mogelijk: grondstoffen, kapitaal en arbeid. De bevolking groeide net, waardoor er meer arbeiders en meer kopers waren."),

    # Ottomaanse Rijk
    casus(
        "In 1453 veroverden de Ottomanen Constantinopel. Onder Suleyman I groeide het rijk verder en in 1529 belegerde het Ottomaanse leger Wenen.",
        [
            mk("Welke naam kreeg Constantinopel later?",
               ["Istanboel", "Ankara", "Jeruzalem", "Alexandrië"],
               0,
               "De Ottomanen maakten van Constantinopel hun hoofdstad. Die stad heet vandaag Istanboel."),
            tabel(
                "Klopt dit over het Ottomaanse Rijk?",
                [
                    ("De sultan regeerde als absoluut heerser, net als Lodewijk XIV in Frankrijk.", J),
                    ("Het beleg van Wenen in 1529 was een Ottomaanse overwinning.", F),
                    ("Het rijk lag op het kruispunt van handelsroutes tussen Europa en Azië.", J),
                ],
                "Ook de sultan had alle macht en hoefde aan niemand verantwoording af te leggen. Wenen hield in 1529 stand. Het rijk controleerde belangrijke handelswegen."),
        ],
    ),

    # Redeneren met bronnen
    tabel(
        "Is dit een goede, onderzoekbare historische vraag?",
        [
            ("Waarom kwamen de Vlaamse steden in 1302 in opstand tegen de Franse koning?", J),
            ("Was Karel de Grote een sympathieke man?", F),
            ("Hoe veranderde de zwarte dood de bevolking van Brugge tussen 1340 en 1360?", J),
            ("Wat zou er gebeurd zijn als Columbus nooit vertrokken was?", F),
        ],
        "Een onderzoekbare vraag kan je met bronnen beantwoorden en is afgebakend in tijd en ruimte. Persoonlijke smaak en wat-als-vragen kan je niet met bronnen onderzoeken."),
    mk("Waarom vergelijk je best verschillende bronnen over dezelfde gebeurtenis?",
       ["Elke bron is gemaakt door iemand met een eigen blik en doel.", "Hoe meer bronnen je leest, hoe minder werk je nadien hebt.", "Oudere bronnen zijn altijd juister dan nieuwere bronnen erover.", "Een historicus mag maar één bron gebruiken per vraag die hij stelt."],
       0,
       "Wie een bron maakt, kiest wat hij vertelt en verzwijgt. Door bronnen naast elkaar te leggen, zie je verschillen en kom je dichter bij wat er gebeurde."),
    sleep(
        "Een historicus [[situeert]] een gebeurtenis in tijd en ruimte. Als twee dingen in hetzelfde jaar gebeuren op plaatsen die niets van elkaar weten, spreekt hij van [[gelijktijdigheid]]. Hoe lang een toestand duurt, noemt hij de [[duur]].",
        ["veralgemening", "chronologie"],
        "Dat zijn begrippen van het historisch referentiekader: situeren, gelijktijdigheid en duur."),

    # Beeldvorming
    mk("Waarom kan het beeld van een gebeurtenis zoals de Guldensporenslag in de loop van de tijd veranderen?",
       ["Er komen nieuwe bronnen en nieuwe vragen, en elke tijd kijkt anders.", "De gebeurtenis zelf verandert telkens als er een boek over verschijnt.", "Historici mogen na honderd jaar zelf beslissen wat er gebeurd is.", "Oude bronnen worden na een tijd onleesbaar en dus onbruikbaar."],
       0,
       "Het verleden zelf verandert niet, het beeld ervan wel. In de 19de eeuw maakten Vlaamsgezinden van 1302 een symbool van Vlaamse trots, terwijl het toen vooral om de steden en de graaf ging."),

    # Open vraag
    open_("Vergelijk het absolutisme van Lodewijk XIV met de ideeën van de Verlichting. Noem een verschil en leg uit waarom de Verlichting voor vorsten gevaarlijk kon zijn.",
          "Bij Lodewijk XIV lag alle macht bij de koning, die aan niemand verantwoording aflegde. Verlichtingsdenkers zoals Montesquieu wilden de macht verdelen over wetgevende, uitvoerende en rechterlijke macht, en Locke vond dat elke mens natuurrechten heeft. Dat was gevaarlijk voor vorsten, omdat het volk zo kon eisen dat de macht van de koning beperkt werd, zoals later in de Amerikaanse en Franse Revolutie gebeurde.",
          "Een goed antwoord noemt een concreet verschil, bijvoorbeeld alle macht bij één persoon tegenover de scheiding der machten, en legt het verband met de revoluties."),
]

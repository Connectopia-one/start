# -*- coding: utf-8 -*-
"""Uitdaging Geschiedenis 🚀 Boost doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een schema van het leenstelsel en een
verzonnen pamflet uit 1789 om op te klikken, tabellen, keuzelijsten,
koppelen, sorteren, volgorde en een open vraag. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Geschiedenis Boost doorstroom. Bewust andere
vragen dan in de uitdaging van Boost dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_geschiedenis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Geschiedenis"
BESTAND = "boost-geschiedenis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/geschiedenis-boost-uitdaging"
PIRAMIDE = "piramide-leenstelsel.svg"
PAMFLET = "pamflet-1789.svg"
# klikvakken: zie maak_prenten_boost_geschiedenis.py
LAAG = {1: [32.0, 18.3, 36.0, 17.5], 2: [22.0, 35.8, 56.0, 17.5], 3: [12.0, 53.3, 76.0, 17.5], 4: [2.0, 70.8, 96.0, 17.5]}


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1) in het pamflet."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Het leenstelsel (prent)
    klik("Bekijk het schema. Klik op de laag van de ridders.",
         PIRAMIDE, [LAAG[3]],
         "Ridders kregen een klein leen en vochten te paard voor hun leenheer. Onder hen stonden enkel nog de boeren."),
    klik("Klik op de laag van de hertogen en de graven.",
         PIRAMIDE, [LAAG[2]],
         "Hertogen en graven kregen een groot leen van de koning en gaven zelf kleinere lenen door aan ridders."),
    met_prent(PIRAMIDE, keuze(
        "Bovenaan staat de [[*koning|paus|graaf]]. Wie een leen kreeg, werd [[*leenman|horige|stedeling]] en beloofde in ruil [[*trouw en hulp|een vaste huur in geld]].",
        "De koning gaf lenen aan zijn leenmannen. Een leenman beloofde trouw en militaire hulp aan zijn leenheer.")),
    met_prent(PIRAMIDE, tabel(
        "Klopt dit over het leenstelsel?",
        [
            ("Laag 4 telde de meeste mensen.", J),
            ("Een leenman kon zelf ook leenheer zijn van iemand anders.", J),
            ("De boeren in laag 4 gaven lenen aan de ridders.", F),
            ("De graven bleven altijd trouw aan de wil van de koning.", F),
        ],
        "Het overgrote deel van de bevolking was boer. Een graaf was leenman van de koning en leenheer van zijn ridders. Graven werden vaak zo machtig dat ze hun eigen gang gingen.")),

    # Pamflet uit 1789 (prent)
    klik("Lees het verzonnen pamflet. Klik op de zin die een idee van de Verlichting verwoordt over de rechten van elke mens.",
         PAMFLET, [zin(4)],
         "Dat elke mens vrij en gelijk in rechten geboren wordt, is een idee van de Verlichting, onder meer van Locke over natuurrechten."),
    klik("Klik op de zin waarin de schrijver tegenstanders zwartmaakt in plaats van te argumenteren.",
         PAMFLET, [zin(6)],
         "Wie iemand een vijand van het vaderland noemt omdat hij een andere mening heeft, geeft geen argument. Dat is een kenmerk van propaganda."),
    met_prent(PAMFLET, tabel(
        "Klopt dit over het pamflet?",
        [
            ("Zin 2 klaagt over de voorrechten van adel en geestelijkheid.", J),
            ("Zin 5 verdedigt het absolutisme van de koning.", F),
            ("De schrijver hoort vermoedelijk bij de derde stand.", J),
            ("Het pamflet geeft een evenwichtig beeld van alle standen.", F),
        ],
        "Zin 2 en 3 klagen de ongelijkheid aan, zin 5 wil de macht van de koning net beperken. De schrijver kiest duidelijk de kant van de derde stand: de bron is eenzijdig.")),
    met_prent(PAMFLET, mk(
        "Voor wie werd dit pamflet vooral gemaakt?",
        ["voor de gewone burgers, om hen tegen de voorrechten op te zetten", "voor de koning, om hem raad te geven over nieuwe belastingen", "voor historici van later, om de revolutie precies te beschrijven", "voor de adel, om haar te bedanken voor haar steun aan het volk"],
        0,
        "Zin 1 spreekt alle burgers aan. Het pamflet wil overtuigen en mensen in beweging brengen. Wie het publiek is, bepaalt mee wat er verteld en verzwegen wordt.")),
    met_prent(PAMFLET, keuze(
        "Zin 2 gaat vooral over het [[*economische|culturele]] domein, zin 5 over het [[*politieke|sociale]] domein.",
        "Belastingen horen bij het economische domein. Wie de wetten maakt, is een politieke kwestie.")),

    # Rome en de Franken
    tabel(
        "Waarom gebruikten deze Frankische koningen de Kerk?",
        [
            ("Clovis liet zich dopen.", J),
            ("Pepijn de Korte liet zich door de paus zalven.", J),
            ("Karel de Grote liet zich in Rome tot keizer kronen.", J),
            ("De Frankische koningen hielden de Kerk buiten de politiek.", F),
        ],
        "Clovis, Pepijn en Karel gebruikten de Kerk om hun macht te onderbouwen, en de Kerk gebruikte hen om zich te beschermen. Politiek en godsdienst liepen bij de Franken door elkaar."),
    mk("Hoe verspreidde het christendom zich meestal over West-Europa?",
       ["Missionarissen bekeerden eerst de vorst, daarna volgde zijn volk.", "De Romeinse keizers dwongen elke boer persoonlijk tot de doop.", "Het christendom kwam pas na de kruistochten naar West-Europa.", "Elke stad koos zelf haar godsdienst bij een stemming op de markt."],
       0,
       "Bekeerde de vorst zich, dan volgden zijn volgelingen en uiteindelijk het volk. Zo ging het bij Clovis."),

    # Middeleeuwse samenleving en geloof
    sorteer(
        "Hoort dit bij het platteland of bij de middeleeuwse stad?",
        ["Platteland", "Stad"],
        [
            ["horigen op een domein", "Platteland"],
            ["een ambacht van bakkers", "Stad"],
            ["een keure met rechten en vrijheden", "Stad"],
            ["het drieslagstelsel op de akkers", "Platteland"],
            ["een lakenhalle voor de handel", "Stad"],
        ],
        "Op het platteland werkten horigen op het domein van hun heer, met het drieslagstelsel. In de stad verenigden ambachtslui zich, regelde een keure de rechten en bloeide de handel."),
    keuze(
        "Een geloofsopvatting die afweek van de leer van de Kerk, noemde men [[*ketterij|humanisme|absolutisme]]. In de middeleeuwen ontstonden ook de eerste [[*universiteiten|fabrieken|kolonies]].",
        "Ketters weken af van de officiële leer. Het hoger onderwijs bestond al: universiteiten ontstonden vanaf de 12de en 13de eeuw."),
    mk("Waarom mag je de kruistochten niet enkel via westerse bronnen bestuderen?",
       ["Ook de Arabische kant liet bronnen na, met een andere blik.", "Westerse bronnen over de kruistochten zijn allemaal verloren gegaan.", "De kruistochten vonden enkel plaats in West-Europa zelf, niet elders.", "Arabische bronnen zijn altijd betrouwbaarder dan westerse bronnen."],
       0,
       "Elke bron toont het standpunt van wie ze maakte. Door ook Arabische bronnen te lezen, krijg je een vollediger beeld."),

    inv("In welk jaar liet Pepijn de Korte zich tot koning van de Franken kronen? Geef enkel het jaartal.",
        "751",
        "In 751 werd Pepijn de Korte, zoon van Karel Martel, koning. Met hem begon de dynastie van de Karolingers."),
    tabel(
        "In welke eeuw valt dit jaartal?",
        [
            ("476", "5de eeuw"),
            ("1302", "14de eeuw"),
            ("1566", "16de eeuw"),
            ("1789", "18de eeuw"),
        ],
        "De eeuw is altijd één meer dan de honderdtallen: de jaren 1301 tot 1400 vormen de 14de eeuw, de jaren 1701 tot 1800 de 18de eeuw.",
        kolommen=["5de eeuw", "14de eeuw", "16de eeuw", "18de eeuw"]),
    keuze(
        "In 1453 veroverden de [[*Ottomanen|Franken|Spanjaarden]] Constantinopel. De sultan die men in het Westen 'de Prachtlievende' noemde, was [[*Suleyman I|Karel V|Lodewijk XIV]].",
        "Met de verovering van Constantinopel werd het Ottomaanse Rijk een grootmacht. Onder Suleyman I bereikte het zijn grootste bloei."),
    sorteer(
        "Is dit een oorzaak of een gevolg van de Franse Revolutie?",
        ["Oorzaak", "Gevolg"],
        [
            ["de ongelijkheid tussen de drie standen", "Oorzaak"],
            ["de ideeën van de Verlichting", "Oorzaak"],
            ["de afschaffing van de voorrechten van adel en geestelijkheid", "Gevolg"],
            ["het einde van het absolutisme in Frankrijk", "Gevolg"],
            ["een lege staatskas en duur brood", "Oorzaak"],
        ],
        "Ongelijkheid, nieuwe ideeën en een financiële crisis zetten de revolutie in gang. Ze maakte een einde aan de voorrechten en aan de absolute macht van de koning."),
    mk("Wat veranderde er door de boekdrukkunst?",
       ["Boeken werden goedkoper en ideeën verspreidden zich sneller.", "Alleen kloosters mochten nog boeken maken en lezen.", "Boeken werden duurder, want elke letter was met de hand gesneden.", "Het Latijn verdween meteen helemaal als taal van de geleerden."],
       0,
       "Met de drukpers kon je snel veel exemplaren maken. Zo verspreidden de ideeën van humanisten en hervormers zich over heel Europa."),
    mk("Waarom groeide de bevolking in de 18de eeuw sterk?",
       ["Een betere landbouw leverde meer voedsel op.", "De pest doodde in die eeuw vooral de ouderen.", "Er kwamen veel kolonisten uit Amerika naar Europa.", "Elke stad gaf gratis brood aan alle inwoners."],
       0,
       "Nieuwe methodes zoals het vruchtwisselstelsel en nieuwe gewassen zoals de aardappel zorgden voor meer voedsel. Daardoor stierven minder mensen aan honger."),
    inv("Hoe noemt men de beweging die Luther in gang zette en die tot nieuwe, protestantse kerken leidde?",
        ["Reformatie", "de Reformatie", "reformatie", "de reformatie"],
        "Luther wilde de Kerk hervormen. Zijn beweging heet de Reformatie; de katholieke reactie erop heet de Contrareformatie."),

    # Nieuwe Wereld
    koppel(
        "Koppel elk begrip aan zijn uitleg.",
        [
            ["mercantilisme", "meer uitvoeren dan invoeren om edelmetaal binnen te halen"],
            ["monocultuur", "een heel gebied beplant met één gewas voor de uitvoer"],
            ["vruchtwisselstelsel", "elk jaar een ander gewas op hetzelfde veld, zonder braakland"],
            ["astrolabium", "instrument om op zee de breedtegraad te bepalen"],
        ],
        ["een kerkvergadering die de leer vastlegt"],
        "Mercantilisme is een economisch beleid van de vorsten. Monocultuur hoort bij de plantages in de kolonies. Het vruchtwisselstelsel vernieuwde de landbouw. Het astrolabium hielp de zeevaarders."),
    tabel(
        "Klopt dit over de verovering van Amerika?",
        [
            ("Het Aztekenrijk lag in het huidige Mexico.", J),
            ("De Spanjaarden versloegen de Azteken en de Inca's met kleine legers en bondgenoten.", J),
            ("Ziekten uit Europa doodden een groot deel van de inheemse bevolking.", J),
            ("China werd in dezelfde periode door Spanje veroverd.", F),
        ],
        "Met paarden, vuurwapens, bondgenoten en vooral ziekten vielen de grote rijken van Amerika. China en het Ottomaanse Rijk bleven buiten het bereik van de Europeanen."),
    mk("Wat is het verschil tussen kolonialisme en imperialisme?",
       ["Imperialisme is breder: macht over andere gebieden.", "Kolonialisme gaat enkel over handel, imperialisme enkel over godsdienst.", "Er is geen verschil: de twee woorden betekenen precies hetzelfde.", "Imperialisme bestond alleen in de oudheid en niet meer daarna."],
       0,
       "Kolonialisme is het stichten en uitbuiten van kolonies. Imperialisme is breder: het streven van een staat naar macht en invloed over andere gebieden, ook zonder ze rechtstreeks te besturen."),

    # Humanisme en kunst
    tabel(
        "Klopt dit over de nieuwe manier van denken in de 15de en 16de eeuw?",
        [
            ("Humanisten bestudeerden opnieuw de teksten van de Grieken en Romeinen.", J),
            ("Vesalius ontleedde zelf lichamen en verbeterde zo oude teksten.", J),
            ("Dankzij de drukpers raakten ideeën veel sneller verspreid.", J),
            ("Wetenschappers bleven alles uit oude boeken overnemen zonder zelf te kijken.", F),
        ],
        "Men ging zelf waarnemen en proeven doen in plaats van oude teksten blind te volgen. De drukpers maakte boeken goedkoper en ideeën sneller bekend."),
    mk("Waarin verschilden de Vlaamse primitieven, zoals Van Eyck, van de Italiaanse renaissanceschilders?",
       ["Zij schilderden met olieverf elk detail haarfijn uit.", "Zij schilderden enkel landschappen zonder mensen erin.", "Zij gebruikten nooit kleur en werkten in zwart en wit.", "Zij maakten alleen beelden in marmer en geen schilderijen."],
       0,
       "Van Eyck schilderde elke haar en elke weerspiegeling met olieverf. Een Italiaan zocht eerst de bouw van het geheel en de juiste verhoudingen."),
    volgorde(
        "Zet deze stappen van de Reformatie en de reactie erop in de juiste volgorde.",
        ["Luther uit kritiek op de aflaathandel", "de Reformatie verspreidt zich met de drukpers", "het concilie van Trente legt de katholieke leer vast", "de barokkunst moet de gelovigen opnieuw raken"],
        "Luthers kritiek verspreidde zich snel dankzij gedrukte teksten. De Kerk antwoordde met het concilie van Trente en de Contrareformatie, waarin ook de barokkunst een rol speelde."),

    # Vorsten en revoluties
    tabel(
        "Waar of niet waar?",
        [
            ("De Glorious Revolution van 1688 verliep zonder grote veldslag.", J),
            ("Na de Glorious Revolution kreeg het Engelse parlement meer macht.", J),
            ("Lodewijk XIV deelde zijn macht met een verkozen parlement.", F),
            ("Een grondwet legt de grondregels en de macht van een staat vast.", J),
        ],
        "In Engeland werd de macht van de koning beperkt door het parlement. Lodewijk XIV regeerde absoluut. Een grondwet legt vast wie welke macht heeft."),
    tabel(
        "Welk bestuursniveau beslist hierover in België vooral?",
        [
            ("de vuilnisophaling in je straat", "Gemeente"),
            ("het onderwijs in Vlaanderen", "Gemeenschap"),
            ("het leger en de rechtbanken", "Federaal"),
        ],
        "In België verdelen verschillende niveaus de macht: de gemeente regelt lokale zaken, de gemeenschappen onder meer onderwijs, en het federale niveau onder meer defensie en justitie. Ook dat is een vorm van verdeelde macht.",
        kolommen=["Gemeente", "Gemeenschap", "Federaal"]),
    volgorde(
        "Zet deze gebeurtenissen in de juiste volgorde.",
        ["de Beeldenstorm", "de Glorious Revolution", "de Amerikaanse Onafhankelijkheidsverklaring", "de bestorming van de Bastille"],
        "1566, 1688, 1776 en 1789."),

    # Industriële omwenteling
    tabel(
        "Klopt dit over de industriële revolutie op het vasteland?",
        [
            ("De eerste fabrieken op het vasteland kwamen er onder meer rond Luik en Gent.", J),
            ("Cockerill bouwde in Seraing een bedrijf dat zijn eigen machines maakte.", J),
            ("De industriële revolutie begon op het vasteland en sloeg dan over naar Groot-Brittannië.", F),
        ],
        "De industriële revolutie begon in Groot-Brittannië. Daarna volgde het vasteland, met onze gewesten bij de eersten: steenkool, ijzer en textiel."),
    sleep(
        "Rond 1800 veranderde er veel tegelijk: de [[industriële]] revolutie veranderde de economie, de Franse Revolutie de [[politiek]] en de bevolking groeide door betere [[landbouw]].",
        ["godsdienst", "kruistochten"],
        "De revoluties van die tijd raakten elk een ander maatschappelijk domein, maar ze beïnvloedden elkaar."),

    # Ottomaanse Rijk en vergelijken
    tabel(
        "Droeg dit bij tot het latere verval van het Ottomaanse Rijk?",
        [
            ("de nieuwe zeeroutes die de landhandel via het rijk minder belangrijk maakten", J),
            ("de nederlaag bij het beleg van Wenen", J),
            ("de verovering van Constantinopel in 1453", F),
        ],
        "De verovering van Constantinopel was net een hoogtepunt. Later verloor het rijk handel door de zeeroutes rond Afrika en raakte het in Europa terrein kwijt."),
    mk("Je vergelijkt het Ottomaanse Rijk en Frankrijk onder Lodewijk XIV. Welke gelijkenis vind je?",
       ["In beide lag alle macht bij één heerser.", "In beide was de godsdienst het christendom.", "Beide hadden een verkozen parlement.", "Beide waren republieken zonder vorst."],
       0,
       "De sultan en Lodewijk XIV regeerden allebei absoluut. De Ottomanen waren moslims, Frankrijk katholiek, en geen van beide had een verkozen parlement."),

    # Redeneren met bronnen
    koppel(
        "Welke historische redeneerwijze gebruik je?",
        [
            ["Waarom brak de Franse Revolutie uit?", "oorzaak en gevolg"],
            ["Wat bleef hetzelfde en wat veranderde na de Reformatie?", "continuïteit en verandering"],
            ["Hoe verschilt een Ottomaanse stad van een Vlaamse stad rond 1550?", "vergelijken"],
        ],
        ["veralgemenen"],
        "Historici zoeken oorzaken en gevolgen, kijken naar wat blijft en wat verandert, en vergelijken samenlevingen."),
    tabel(
        "Klopt dit over historische bronnen?",
        [
            ("Een tijdgenoot is altijd ook een ooggetuige.", F),
            ("Een schilderij kan een historische bron zijn.", J),
            ("Een geschiedenisboek van vorig jaar over 1789 is een secundaire bron.", J),
            ("Een bron met een duidelijke mening is waardeloos voor een historicus.", F),
        ],
        "Wie in dezelfde tijd leefde, was er niet altijd zelf bij. Elk spoor uit het verleden kan een bron zijn. Ook een gekleurde bron is nuttig: ze toont hoe iemand dacht."),
    volgorde(
        "Zet de stappen om een historische vraag te beantwoorden in de juiste volgorde.",
        ["een onderzoekbare vraag stellen", "bronnen zoeken en selecteren", "de bronnen kritisch bekijken", "een antwoord formuleren en staven met de bronnen"],
        "Je begint met een goede vraag, zoekt bruikbare bronnen, weegt hun betrouwbaarheid en formuleert dan een onderbouwd antwoord."),

    # Beeldvorming
    mk("Wat is het gevolg als je enkel de bronnen van één kant van een conflict leest?",
       ["Je neemt hun blik over zonder het te merken.", "Je kent dan meteen de volledige waarheid erover.", "Je kan dan geen enkele vraag meer stellen.", "Je bron wordt dan automatisch een secundaire."],
       0,
       "Elke partij vertelt het verhaal vanuit haar eigen standpunt. Wie maar één kant leest, neemt die blik over."),
    tabel(
        "Gaat dit over beeldvorming van het verleden?",
        [
            ("Een standbeeld uit de 19de eeuw maakt van een middeleeuwse graaf een volksheld.", J),
            ("Een film over de kruistochten toont enkel dappere ridders en wrede vijanden.", J),
            ("Een historicus telt de belastingrollen van een stad uit 1350.", F),
        ],
        "Beeldvorming gaat over hoe later naar het verleden gekeken wordt, met keuzes en blinde vlekken. Het tellen van belastingrollen is onderzoek naar het verleden zelf."),

    # Open vraag
    open_("Leg met een voorbeeld uit hoe de economische en de sociale domeinen in de driehoekshandel met elkaar verbonden waren.",
          "Economisch: Europese handelaars verdienden veel aan suiker, katoen en tabak van de plantages. Sociaal: daarvoor werden miljoenen Afrikanen tot slaaf gemaakt en weggerukt uit hun samenleving, en in Amerika ontstond een samenleving met een kleine groep rijke planters en een grote groep slaven zonder rechten. De winst in het ene domein steunde dus rechtstreeks op het onrecht in het andere.",
          "Een goed antwoord noemt een concreet economisch element (winst, handel, producten) en een concreet sociaal gevolg (slavernij, ongelijkheid) en legt uit hoe het ene het andere veroorzaakte."),
]

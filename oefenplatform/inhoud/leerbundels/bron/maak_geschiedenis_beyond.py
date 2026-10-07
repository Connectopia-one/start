# -*- coding: utf-8 -*-
"""De leerbundels voor geschiedenis op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche geschiedenis 3de graad doorstroomfinaliteit
(domeinoverschrijdend), geldig vanaf 1 januari 2027. Die ene fiche geldt voor
economie-wiskunde, humane wetenschappen, moderne talen, wetenschappen-wiskunde,
Latijn-moderne talen en Latijn-wiskunde-wetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/geschiedenis.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond", de naam van de categorie. Dat is
nodig en niet alleen netjes: Boost doorstroom heeft een thema dat precies
"Het historisch referentiekader" heet, net als dit. Zonder de categorie in de
bestandsnaam weet noch dekking.py noch het uploadscherm welke van de twee
bedoeld is.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Geschiedenis"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Het historisch referentiekader
BUNDELS["het-historisch-referentiekader-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het historisch referentiekader",
    onder="Tijd, ruimte en de maatschappelijke domeinen, en wat een periodisering eigenlijk is.",
    secties=[
        dict(kop="De drie assen", blokken=[
            ("p", "Het <strong>historisch referentiekader</strong> is het rooster waarop je elke "
                  "gebeurtenis, elke bron en elke samenleving legt. Het heeft drie assen: de "
                  "<strong>tijd</strong>, de <strong>ruimte</strong> en de <strong>maatschappelijke "
                  "domeinen</strong>. Het is een <strong>hulpmiddel, geen natuurwet</strong>: het ordent, "
                  "het bewijst niets."),
            ("p", "Het courante westerse referentiekader telt <strong>zeven periodes</strong>: de "
                  "<strong>prehistorie</strong>, het <strong>oude nabije oosten</strong>, de "
                  "<strong>klassieke oudheid</strong>, de <strong>middeleeuwen</strong>, de "
                  "<strong>vroegmoderne tijd</strong>, de <strong>moderne tijd</strong> en de "
                  "<strong>hedendaagse tijd</strong>. Tussen de periodes liggen "
                  "<strong>scharnierpunten</strong>."),
            ("p", tabel(["Periode", "Ongeveer", "Scharnierpunt aan het begin"], [
                ["Vroegmoderne tijd", "16de tot 18de eeuw", "1492, de overtocht van Columbus"],
                ["Moderne tijd", "1789 tot 1945", "de Franse Revolutie"],
                ["Hedendaagse tijd", "1945 tot nu", "het einde van de Tweede Wereldoorlog"],
            ])),
            ("p", "De <strong>Reformatie</strong> hoort dus in de <strong>vroegmoderne tijd</strong>, en de "
                  "<strong>moderne tijd begint volgens dat kader bij de Franse Revolutie</strong>. Ook het "
                  "<strong>Congres van Wenen</strong> wordt soms als scharnierpunt genoemd. Dat men met het "
                  "<strong>einde van de Tweede Wereldoorlog</strong> een nieuwe periode laat beginnen, komt "
                  "doordat de <strong>machtsverhoudingen in de wereld toen ingrijpend verschoven</strong>."),
        ]),
        dict(kop="Structuurbegrippen van de tijd", blokken=[
            ("p", "<strong>Structuurbegrippen van de tijd</strong> zijn de woorden waarmee je over tijd "
                  "praat: <strong>chronologie</strong>, <strong>periodisering</strong>, "
                  "<strong>tijdrekening</strong>, <strong>continuïteit en verandering</strong>, "
                  "<strong>evolutie en revolutie</strong>, <strong>gelijktijdigheid en "
                  "ongelijktijdigheid</strong>, <strong>breuk</strong> en <strong>duur</strong>. "
                  "<strong>Tijdrekening</strong> is het afspreken vanaf welk punt je de jaren telt."),
            ("p", "<strong>Continuïteit</strong> is wat over een lange periode in grote lijnen hetzelfde "
                  "blijft. Schrijft een historicus dat <strong>de boerenstiel in een streek eeuwenlang "
                  "nauwelijks veranderde</strong>, dan is dat continuïteit. <strong>Verandering</strong> is "
                  "het omgekeerde; een scherpe, duidelijke onderbreking met wat ervoor kwam heet een "
                  "<strong>breuk</strong>. De <strong>val van de Berlijnse Muur in 1989</strong> is voor "
                  "naoorlogs Europa <strong>verandering</strong>, want de deling van Europa eindigde ermee."),
            ("p", "<strong>Gelijktijdigheid</strong> betekent dat twee gebeurtenissen in dezelfde periode "
                  "plaatsvonden, <strong>ook al hadden ze niets met elkaar te maken</strong>. "
                  "<strong>Ongelijktijdigheid</strong> is dat <strong>dezelfde ontwikkeling elders vroeger "
                  "of later op gang komt</strong>."),
            ("kader", "Let op het onderscheid: <strong>chronologie</strong> ordent gebeurtenissen in "
                      "volgorde, <strong>periodisering</strong> groepeert ze in stukken met een naam. "
                      "Chronologie hoort bij de tijd en gebruik je dus <strong>niet</strong> om iets in de "
                      "<strong>ruimte</strong> te situeren."),
        ]),
        dict(kop="Structuurbegrippen van de ruimte", blokken=[
            ("p", "In de ruimte situeer je met begrippen als <strong>lokaal, regionaal, nationaal, "
                  "continentaal en mondiaal</strong>, met <strong>stedelijk</strong> tegenover "
                  "<strong>ruraal</strong> (het platteland), en met <strong>maritiem</strong> tegenover "
                  "<strong>continentaal</strong>. Het tegenovergestelde van <strong>stedelijk</strong> is "
                  "dus <strong>ruraal</strong>."),
            ("p", "Het begrip <strong>westers</strong> is lastiger dan het lijkt: het wijst <strong>niet "
                  "alleen op een plaats op de kaart maar ook op een manier van samenleven</strong>, met "
                  "bepaalde instellingen, een bepaald mensbeeld en een bepaalde economie. Australië ligt in "
                  "het oosten van de kaart en heet toch westers."),
        ]),
        dict(kop="De vier maatschappelijke domeinen", blokken=[
            ("p", "Het referentiekader onderscheidt <strong>vier maatschappelijke domeinen</strong>: het "
                  "<strong>politieke</strong>, het <strong>sociale</strong>, het <strong>economische</strong> "
                  "en het <strong>culturele</strong>. Het <strong>culturele</strong> domein (cultureel) gaat over "
                  "<strong>geloof, kunst, taal en mens- en wereldbeelden</strong>."),
            ("p", tabel(["Voorbeeld", "Domein in de eerste plaats"], [
                ["De invoering van het algemeen enkelvoudig stemrecht", "het politieke domein"],
                ["Het ontstaan van vakbonden", "het sociale domein"],
                ["Het Congres van Wenen", "het politieke domein"],
                ["De vijfjarenplannen in de Sovjet-Unie", "het economische domein"],
            ])),
            ("p", "Een gebeurtenis hoort <strong>niet altijd bij precies één domein</strong>. Een "
                  "<strong>propaganda-affiche van Stalin</strong> hoort tegelijk in het "
                  "<strong>politieke</strong> domein (het bewind verheerlijken), het "
                  "<strong>culturele</strong> domein (beeldtaal en wereldbeeld) en het "
                  "<strong>economische</strong> domein (de productiecijfers die ze aanprijst)."),
        ]),
        dict(kop="Wat een periodisering is, en wat ze verbergt", blokken=[
            ("p", "Een <strong>scharnierpunt</strong> is <strong>een gebeurtenis die de overgang vormt "
                  "tussen twee periodes</strong>. Een periode bakent men af <strong>met een selectie van "
                  "kenmerken en gebeurtenissen</strong>, met een <strong>symbolische begin- en "
                  "einddatum</strong>, en <strong>achteraf, als constructie</strong>. Dat 1492 een "
                  "<strong>symbolische begindatum</strong> is, betekent dat <strong>de datum staat voor een "
                  "verandering die veel langer duurde</strong>."),
            ("p", "Een periodisering is dus <strong>een constructie achteraf</strong>: <strong>wie in 1492 "
                  "leefde, wist niet dat de middeleeuwen bijna voorbij waren</strong>. En ze is "
                  "<strong>altijd een keuze van wie ze maakt</strong>, want <strong>iemand beslist welke "
                  "gebeurtenis belangrijk genoeg is om een grens te zijn</strong>."),
            ("p", "Die keuze heeft gevolgen. Ze kan leiden tot een <strong>etnocentrische blik</strong> "
                  "(<strong>de eigen groep als maatstaf voor de rest nemen</strong>), tot een "
                  "<strong>ruimtelijk beperkte blik</strong>, en tot een <strong>gebrek aan meerdere "
                  "perspectieven</strong>. Het <strong>Congres van Wenen als scharnierpunt kiezen getuigt "
                  "van een eurocentrische blik</strong>, en een handboek dat <strong>de 19de eeuw enkel aan "
                  "de hand van Europese staten</strong> behandelt, heeft vooral een <strong>ruimtelijk "
                  "beperkte blik</strong>."),
            ("p", "Noemt een tekst de middeleeuwen <strong>de donkere eeuwen</strong>, dan is het probleem "
                  "dat <strong>er een morele maatstaf in verstopt zit</strong>: de naam oordeelt al voor je "
                  "iets onderzocht hebt."),
        ]),
        dict(kop="Andere periodiseringen", blokken=[
            ("p", "<strong>China deelt zijn verleden in volgens dynastieën.</strong> Daarin herken je "
                  "hetzelfde principe: <strong>afbakening op basis van een selectie van kenmerken</strong>, "
                  "alleen zijn het andere kenmerken dan de onze. Een andere periodisering is daarom "
                  "<strong>niet verkeerd</strong> zodra ze niet met de westerse zeven periodes samenvalt."),
            ("p", "Daarom vraagt de leerstof dat je periodiseringen kan vergelijken: <strong>elke indeling "
                  "toont wat iemand belangrijk vindt</strong>. En daarom is een gebeurtenis die <strong>in "
                  "Europa een scharnierpunt is, dat niet overal ter wereld</strong>. Scharnierpunten liggen "
                  "trouwens <strong>niet altijd op het politieke domein</strong>: de boekdrukkunst en de "
                  "industrialisering zijn er evengoed."),
            ("kader", "Samengevat: het referentiekader <strong>ordent in tijd, ruimte en maatschappelijke "
                      "domeinen</strong>, het <strong>gebruikt scharnierpunten tussen de periodes</strong>, "
                      "en het is <strong>een hulpmiddel, geen natuurwet</strong>."),
        ]),
    ],
    onthoud=[
        "Het referentiekader heeft drie assen: tijd, ruimte en maatschappelijke domeinen.",
        "Het westerse kader telt zeven periodes; de moderne tijd begint bij de Franse Revolutie.",
        "Chronologie ordent in volgorde, periodisering groepeert in stukken met een naam.",
        "Continuïteit blijft in grote lijnen hetzelfde; een breuk is een scherpe onderbreking.",
        "Het tegenovergestelde van stedelijk is ruraal; westers is ook een manier van samenleven.",
        "Vier domeinen: politiek, sociaal, economisch en cultureel. Een gebeurtenis kan bij meerdere horen.",
        "Een periodisering is een constructie achteraf en altijd een keuze van wie ze maakt.",
        "Het Congres van Wenen als scharnierpunt kiezen getuigt van een eurocentrische blik.",
        "China deelt zijn verleden in volgens dynastieën; een andere periodisering is niet verkeerd.",
    ],
)

# ───────────────────────── 2. Restauratie, revolutie en het ontstaan van België
BUNDELS["restauratie-revolutie-en-het-ontstaan-van-belgie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Restauratie, revolutie en het ontstaan van België",
    onder="Van het Congres van Wenen over de Belgische revolutie tot de eenmaking van Duitsland.",
    secties=[
        dict(kop="Het Congres van Wenen", blokken=[
            ("p", "Napoleon is verslagen en de vorsten van Europa komen samen. Ze vergaderen in 1814 en "
                  "1815 in <strong>Wenen</strong>, onder leiding van de Oostenrijkse kanselier "
                  "<strong>Metternich</strong>. Het congres eindigde in <strong>1815</strong>, hetzelfde "
                  "jaar als de slag bij Waterloo, en je situeert het in de eerste plaats in het "
                  "<strong>politieke domein</strong>."),
            ("p", "De <strong>doelstellingen</strong> waren: <strong>de vorstenhuizen van voor 1789 "
                  "herstellen</strong>, <strong>een evenwicht tussen de grote mogendheden scheppen</strong> "
                  "en <strong>Frankrijk door bufferstaten laten omringen</strong>. <strong>Restauratie</strong> "
                  "betekent precies dat: <strong>men wilde de toestand van voor de Franse Revolutie "
                  "herstellen</strong>."),
            ("p", "Het <strong>beginsel van de legitimiteit</strong> houdt in dat <strong>de oude "
                  "dynastieën het rechtmatige gezag hebben</strong>. Als buffer ten noorden van Frankrijk "
                  "richtte het congres het <strong>Verenigd Koninkrijk der Nederlanden</strong> op. "
                  "<strong>Pruisen</strong> kreeg het <strong>Rijnland</strong> erbij. De Duitse staten "
                  "werden <strong>niet</strong> in één keizerrijk samengebracht, maar in een los verband, "
                  "de <strong>Duitse Bond</strong>."),
            ("p", "Bij het tekenen van de grenzen <strong>hielden de vorsten geen rekening met de taal en "
                  "de wensen van de bevolking</strong>. Dat verklaart veel van wat erna kwam."),
            ("p", "Op langere termijn had het congres drie grote <strong>gevolgen</strong>: "
                  "<strong>liberale en nationale bewegingen werden onderdrukt</strong>, <strong>de grote "
                  "mogendheden vochten decennialang geen grote oorlog meer uit</strong>, en er "
                  "<strong>volgden revolutiegolven in 1830 en in 1848</strong>. Op die revoluties "
                  "<strong>reageerden de mogendheden door ze te onderdrukken of in te dammen</strong>."),
        ]),
        dict(kop="Liberalisme en nationalisme", blokken=[
            ("p", "De <strong>liberalen</strong> van de eerste helft van de 19de eeuw vroegen <strong>een "
                  "grondwet die de macht van de vorst beperkt</strong>, <strong>vrijheid van drukpers, "
                  "vereniging en godsdienst</strong>, en <strong>zo weinig mogelijk staatsbemoeienis met de "
                  "economie</strong>. Ze kwamen vooral uit de <strong>burgerij</strong>. Het stemrecht "
                  "waarbij <strong>alleen wie genoeg belasting betaalt mag stemmen</strong>, heet "
                  "<strong>cijnskiesrecht</strong> of censuskiesrecht."),
            ("p", "In het 19de-eeuwse <strong>nationalisme</strong> is een <strong>natie</strong> "
                  "<strong>een groep met een gedeelde taal, cultuur en geschiedenis</strong>. Dat "
                  "nationalisme werkt in twee richtingen, en die twee moet je uit elkaar kunnen houden."),
            ("kader", tabel(["vorm", "wat ze wil", "voorbeelden"],
                            [["<strong>verbindend nationalisme</strong>",
                              "<strong>losse staten van hetzelfde volk samenbrengen</strong>",
                              "de eenmaking van Italië en van Duitsland"],
                             ["<strong>ontbindend nationalisme</strong>",
                              "zich losmaken uit een groter geheel",
                              "de <strong>Belgische afscheiding van Nederland</strong>, de <strong>Griekse opstand tegen het Ottomaanse Rijk</strong>, de <strong>Poolse opstand tegen Rusland</strong>"]])),
            ("p", "<strong>Liberalisme en nationalisme gingen in de 19de eeuw vaak hand in hand</strong> "
                  "tegen de orde van Wenen in: allebei keerden ze zich tegen vorsten die zonder grondwet en "
                  "zonder het volk regeerden."),
        ]),
        dict(kop="Willem I en het ongenoegen in het Zuiden", blokken=[
            ("p", "De koning van het Verenigd Koninkrijk der Nederlanden was <strong>Willem I</strong>. In "
                  "het Zuiden groeiden <strong>grieven</strong>: <strong>het Nederlands werd opgelegd als "
                  "bestuurstaal</strong>, <strong>de koning bemoeide zich met de opleiding van "
                  "priesters</strong>, en <strong>het Zuiden had te weinig zetels voor zijn "
                  "inwonertal</strong>."),
            ("p", "Ook de economie botste: <strong>het Zuiden wilde bescherming van zijn jonge industrie, "
                  "het Noorden wilde vrijhandel</strong> voor zijn handelshuizen. Katholieken en liberalen, "
                  "normaal elkaars tegenstanders, sloten in 1828 een verbond: de <strong>unie der "
                  "oppositie</strong>."),
        ]),
        dict(kop="De Belgische revolutie en de grondwet", blokken=[
            ("p", "De Belgische opstand begon in Brussel op <strong>25 augustus 1830</strong>, "
                  "<strong>na een opvoering van de opera De Stomme van Portici</strong>. Daarna volgden de "
                  "<strong>septemberdagen</strong> en zette de revolutie haar stappen: <strong>een "
                  "Voorlopig Bewind nam het bestuur over</strong>, <strong>de onafhankelijkheid werd "
                  "uitgeroepen op 4 oktober</strong> en <strong>een Nationaal Congres schreef een "
                  "grondwet</strong>."),
            ("p", "Die grondwet werd afgekondigd in <strong>1831</strong>. De staatsvorm die België toen "
                  "koos, is een <strong>constitutionele parlementaire monarchie</strong>: een koning, maar "
                  "met een grondwet boven hem en een parlement naast hem. De grondwet schreef uitdrukkelijk "
                  "de <strong>vrijheid van drukpers</strong>, de <strong>vrijheid van vereniging</strong> "
                  "en de <strong>vrijheid van onderwijs</strong> in."),
            ("p", "Modern was dat voor zijn tijd, democratisch nog niet: <strong>bij de eerste "
                  "verkiezingen mochten slechts enkele procenten van de bevolking stemmen</strong>, want "
                  "het cijnskiesrecht gold. Het samen besturen van katholieken en liberalen na 1830 heet "
                  "<strong>unionisme</strong>."),
        ]),
        dict(kop="Taal en de Vlaamse beweging", blokken=[
            ("p", "<strong>Het Nederlands was in het jonge België níét de taal van het bestuur en de "
                  "rechtbanken.</strong> Het Frans was dat, in heel het land, ook in Vlaanderen. Daar kwam "
                  "verzet tegen."),
            ("p", "De <strong>Vlaamse beweging begon als een culturele beweging rond taal en "
                  "letteren</strong>, niet als een politieke partij. Het boek <strong>De Leeuw van "
                  "Vlaanderen</strong> van Hendrik Conscience uit 1838 gaf haar een verhaal om zich aan op "
                  "te trekken. De <strong>eerste Belgische taalwetten die het Nederlands erkenden, kwamen "
                  "er pas vanaf de jaren 1870</strong>, veertig jaar na de onafhankelijkheid."),
        ]),
        dict(kop="De eenmaking van Duitsland", blokken=[
            ("p", "De <strong>Duitse Bond</strong> was na 1815 <strong>een los verband van zelfstandige "
                  "Duitse staten</strong>, negenendertig in getal. De eenmaking werd geleid door de "
                  "Pruisische minister-president <strong>Bismarck</strong>."),
            ("p", "Hij bracht ze tot stand <strong>met een reeks oorlogen tegen buurlanden</strong> "
                  "(Denemarken, Oostenrijk, Frankrijk), <strong>met een douane-unie die de staten "
                  "economisch bond</strong>, en <strong>met handige diplomatie tussen de "
                  "mogendheden</strong>. Het Duitse Keizerrijk werd in 1871 uitgeroepen <strong>in de "
                  "Spiegelzaal van Versailles</strong>, in het hart van het verslagen Frankrijk."),
            ("p", "De eenmaking <strong>veranderde de territoriale verhoudingen in Europa grondig</strong>: "
                  "in het midden van het continent stond plots een grote, industriële en militaire macht. "
                  "Het evenwicht van Wenen was voorbij."),
            ("weetje", "De vernedering in de Spiegelzaal werd in 1919 omgekeerd: daar moest Duitsland het "
                       "Verdrag van Versailles tekenen. Dezelfde zaal, de rollen omgedraaid."),
        ]),
    ],
    onthoud=[
        "Het Congres van Wenen (1814-1815) wilde de vorstenhuizen van voor 1789 herstellen.",
        "Als buffer ten noorden van Frankrijk kwam het Verenigd Koninkrijk der Nederlanden.",
        "Cijnskiesrecht: alleen wie genoeg belasting betaalt, mag stemmen.",
        "Verbindend nationalisme brengt staten samen, ontbindend nationalisme maakt zich los.",
        "Onder Willem I werd het Nederlands opgelegd en had het Zuiden te weinig zetels.",
        "De Belgische opstand begon op 25 augustus 1830; de onafhankelijkheid volgde op 4 oktober.",
        "De grondwet van 1831 maakte België een constitutionele parlementaire monarchie.",
        "De Vlaamse beweging begon cultureel; de eerste taalwetten kwamen pas vanaf de jaren 1870.",
        "Bismarck leidde de Duitse eenmaking; het Keizerrijk werd in 1871 uitgeroepen in Versailles.",
    ],
)

# ───────────────────────── 3. Industrialisatie en de sociale kwestie
BUNDELS["industrialisatie-en-de-sociale-kwestie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Industrialisatie en de sociale kwestie",
    onder="Twee industriële revoluties, een nieuwe klassenmaatschappij en de antwoorden daarop.",
    secties=[
        dict(kop="Twee industriële revoluties", blokken=[
            ("p", "De <strong>eerste industriële revolutie</strong> werd aangedreven door "
                  "de energiebron <strong>steenkool</strong> en kwam als eerste op gang in <strong>Engeland</strong>. De "
                  "Schotse uitvinder <strong>Watt</strong> verbeterde de <strong>stoommachine</strong> zo "
                  "grondig dat ze bruikbaar werd in fabrieken. Omdat kolen zwaar en duur te vervoeren waren, "
                  "<strong>stond de fabriek juist dicht bij de steenkool</strong> en niet ver ervandaan."),
            ("p", "De <strong>tweede industriële revolutie</strong> herken je aan <strong>elektriciteit als "
                  "nieuwe krachtbron</strong>, aan <strong>aardolie en de verbrandingsmotor</strong>, en aan "
                  "<strong>staal en de scheikundige nijverheid</strong>. Ze werd vooral door "
                  "<strong>Duitsland en de Verenigde Staten</strong> getrokken. De bedrijfsorganisatie "
                  "veranderde mee: <strong>de lopende band verdeelde het werk in kleine stappen</strong>."),
            ("p", "Men <strong>vergelijkt het energiegebruik van beide revoluties</strong> omdat <strong>de "
                  "overstap van kolen naar elektriciteit en olie alles veranderde</strong>: waar een fabriek "
                  "kon staan, hoe ver je kon vervoeren, en wie de nieuwe grootmachten werden."),
            ("p", "<strong>Transport en communicatie</strong> sprongen vooruit met de <strong>spoorweg met "
                  "stoomlocomotieven</strong>, het <strong>stoomschip op de grote vaarroutes</strong> en de "
                  "<strong>telegraaf en later de telefoon</strong>. De <strong>steenkoolmijnbouw</strong> "
                  "hoort trouwens bij de <strong>primaire sector</strong>: ze haalt een grondstof uit de "
                  "bodem. Tijdens de industrialisatie <strong>daalde</strong> het aandeel van de landbouw in "
                  "de tewerkstelling, het groeide niet."),
        ]),
        dict(kop="Economisch liberalisme en kapitalisme", blokken=[
            ("p", "Het <strong>economisch liberalisme</strong> houdt in dat <strong>de overheid de "
                  "economie zoveel mogelijk vrij laat</strong>. De Schotse denker <strong>Smith</strong> "
                  "gaf de vrije markt in 1776 haar grondslag."),
            ("p", "Het <strong>kapitalisme vergroot de sociale ongelijkheid</strong>, <strong>doordat de "
                  "winst naar wie de fabriek bezit gaat en niet naar wie er werkt</strong>. Die spanning "
                  "noemt men de <strong>sociale kwestie</strong>."),
        ]),
        dict(kop="België als vroege industriestaat", blokken=[
            ("p", "België was een van de eerste landen op het vasteland dat industrialiseerde. De "
                  "<strong>aanbodfactoren</strong> die daarbij hielpen: <strong>steenkool in de bodem van "
                  "Henegouwen en Luik</strong>, <strong>kapitaal van banken die durfden investeren</strong>, "
                  "en <strong>vaklui met ervaring in textiel en metaal</strong>. Een "
                  "<strong>vraagfactor</strong> is iets anders: dat is bijvoorbeeld <strong>een groeiende "
                  "bevolking die meer goederen koopt</strong>."),
            ("p", "De eerste spoorlijn van het Europese vasteland reed in <strong>1835</strong> tussen "
                  "<strong>Brussel en Mechelen</strong>. De Engelse ondernemer <strong>Cockerill</strong> "
                  "bouwde in <strong>Seraing</strong> een groot metaalbedrijf en geldt als de vader van de "
                  "Belgische zware industrie."),
            ("p", "De sterkst geïndustrialiseerde streken waren de <strong>steenkoolbekkens van Henegouwen "
                  "en Luik</strong>, de <strong>textielstreek rond Gent</strong> en de "
                  "<strong>wolnijverheid rond Verviers</strong>. De industrialisatie van de 19de eeuw "
                  "<strong>lag in België vooral in Wallonië, en Vlaanderen bleef langer landelijk</strong>."),
        ]),
        dict(kop="De klassenmaatschappij", blokken=[
            ("p", "In een <strong>klassenmaatschappij</strong> bepalen <strong>je bezit en je plaats in de "
                  "productie</strong> waar je staat, niet je geboorte. Het proces waarbij <strong>boeren en "
                  "ambachtslui hun eigen werktuigen verliezen en loonarbeider worden</strong>, heet "
                  "<strong>proletarisering</strong>."),
            ("p", "De <strong>leef- en werkomstandigheden</strong> van arbeiders in de 19de eeuw: "
                  "<strong>werkdagen van twaalf uur en meer</strong>, <strong>woningen zonder stromend water "
                  "in overvolle beluiken</strong>, en <strong>geen enkele vergoeding bij ziekte of "
                  "ongeval</strong>. <strong>De Belgische grondwet van 1831 verbood kinderarbeid niet</strong>; "
                  "dat kwam er pas veel later. Fabrikanten zetten graag kinderen aan het werk omdat "
                  "<strong>kinderen goedkoop waren en niet klaagden</strong>."),
        ]),
        dict(kop="Antwoorden op de sociale kwestie", blokken=[
            ("p", "Arbeiders organiseerden zich. In een <strong>coöperatie kopen of produceren de leden "
                  "samen en delen ze de winst</strong>. Een <strong>vakbond</strong> doet iets anders: "
                  "<strong>een vakbond onderhandelt en staakt, een coöperatie produceert</strong>. De "
                  "vereniging waarbij <strong>arbeiders samen sparen om bij ziekte een uitkering te "
                  "krijgen</strong>, is een <strong>mutualiteit</strong>, ook ziekenfonds of ziekenkas genoemd."),
            ("p", "Ook in het denken kwamen antwoorden. Kernideeën van het <strong>marxisme</strong>: "
                  "<strong>de geschiedenis is een strijd tussen klassen</strong>, <strong>de arbeiders "
                  "moeten de productiemiddelen in handen nemen</strong>, en <strong>er is een revolutie "
                  "nodig, geen geduldige hervorming</strong>. De <strong>sociaaldemocratie</strong> "
                  "verschilt daarvan doordat <strong>zij langs verkiezingen en wetten vooruit wil</strong>."),
            ("p", "De <strong>christendemocratie</strong> kreeg haar sociale programma van de pauselijke "
                  "brief <strong>Rerum Novarum</strong> uit 1891. Zij <strong>aanvaardde het privébezit, "
                  "maar vroeg een rechtvaardig loon en bescherming voor de arbeider</strong>."),
        ]),
        dict(kop="Stemrecht, migratie en de stad", blokken=[
            ("p", "In België gold van 1831 tot 1893 <strong>cijnskiesrecht voor wie genoeg belasting "
                  "betaalde</strong>. Het <strong>algemeen meervoudig stemrecht kwam er in 1893 na een "
                  "algemene staking</strong>: één man kon toen ten hoogste <strong>3</strong> stemmen "
                  "uitbrengen. Het <strong>algemeen enkelvoudig stemrecht voor mannen</strong> kwam er in "
                  "<strong>1919</strong>."),
            ("p", "<strong>Plattelandsvlucht</strong> is dat <strong>mensen van het platteland naar de stad "
                  "trekken</strong>. In België bleef dat deels uit, dankzij <strong>goedkope "
                  "werkmanskaarten op de trein</strong>: arbeiders konden op het platteland blijven wonen en "
                  "elke dag naar de fabriek sporen."),
            ("p", "Veel Europeanen trokken in de 19de eeuw naar <strong>Amerika</strong> wegens "
                  "<strong>armoede en honger in eigen streek</strong>, <strong>de belofte van goedkope grond "
                  "en werk</strong>, en <strong>vervolging om geloof of politieke overtuiging</strong>. "
                  "<strong>Seizoensarbeid</strong> is iets anders dan verhuizen: men ging <strong>tijdelijk, "
                  "voor een seizoen</strong>, elders werken en kwam daarna terug."),
        ]),
    ],
    onthoud=[
        "De eerste industriële revolutie draaide op steenkool en begon in Engeland.",
        "De tweede industriële revolutie bracht elektriciteit, aardolie en de verbrandingsmotor.",
        "Economisch liberalisme: de overheid laat de economie zoveel mogelijk vrij.",
        "De eerste spoorlijn van het vasteland reed in 1835 tussen Brussel en Mechelen.",
        "De Belgische industrie van de 19de eeuw lag vooral in Wallonië.",
        "Proletarisering: boeren en ambachtslui verliezen hun werktuigen en worden loonarbeider.",
        "Een vakbond onderhandelt en staakt, een coöperatie produceert.",
        "Marxisme wil revolutie, sociaaldemocratie wil vooruit langs verkiezingen en wetten.",
        "Algemeen meervoudig stemrecht kwam er in 1893, algemeen enkelvoudig stemrecht voor mannen in 1919.",
    ],
)

# ───────────────────────── 4. Modern imperialisme, Congo en China
BUNDELS["modern-imperialisme-congo-en-china-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Modern imperialisme, Congo en China",
    onder="De wedloop om Afrika, de Congo-Vrijstaat en een keizerrijk dat niet gekoloniseerd werd.",
    secties=[
        dict(kop="Wat het modern imperialisme mogelijk maakte", blokken=[
            ("p", "Rond 1880 begint Europa in enkele decennia bijna heel Afrika te bezetten. Die periode "
                  "heet het <strong>modern imperialisme</strong>. Men spreekt van een <strong>wedloop om "
                  "Afrika</strong> omdat <strong>de mogendheden gebieden bezetten uit schrik voor "
                  "elkaar</strong>."),
            ("p", "De <strong>technische voorsprong</strong> maakte het mogelijk: "
                  "<strong>repeteergeweren en mitrailleurs</strong>, <strong>stoomschepen die rivieren op "
                  "konden varen</strong>, en <strong>kinine of chinine als bescherming tegen malaria</strong>. Juist "
                  "dat geneesmiddel, <strong>kinine</strong>, opende het Afrikaanse binnenland."),
            ("p", "De <strong>motieven</strong> liepen door elkaar. Economisch: <strong>goedkope "
                  "grondstoffen voor de eigen fabrieken</strong>, en afzetmarkten. Politiek: prestige en "
                  "strategische punten. Cultureel: <strong>Europese mogendheden rechtvaardigden hun koloniën "
                  "met het idee dat zij beschaving brachten</strong>. Het <strong>modern imperialisme "
                  "speelde zich dus niet enkel in het economische domein af</strong>."),
            ("p", "Het <strong>sociaal darwinisme paste het idee van de strijd om het bestaan toe op "
                  "volkeren en gebruikte dat om overheersing goed te praten</strong>. "
                  "<strong>Missionarissen verspreidden het geloof en richtten scholen op</strong>, en waren "
                  "zo tegelijk hulpverleners en een arm van het koloniale bestel."),
        ]),
        dict(kop="De verdeling van de wereld", blokken=[
            ("p", "Op de <strong>Conferentie van Berlijn</strong> van 1884 en 1885 spraken de Europese "
                  "mogendheden de regels voor Afrika af. De belangrijkste: <strong>je moest het gebied "
                  "werkelijk bezetten en besturen</strong> om er aanspraak op te maken. <strong>Tegen 1914 "
                  "was vrijwel heel Afrika onder Europese mogendheden verdeeld</strong>; alleen "
                  "<strong>Ethiopië</strong> en <strong>Liberia</strong> bleven zelfstandig."),
            ("p", "Dat <strong>koloniale grenzen met een lat getrokken lijken</strong>, betekent dat "
                  "<strong>ze Europese afspraken volgden en geen bestaande samenlevingen</strong>. De "
                  "<strong>gevolgen</strong> voor de bezette gebieden: <strong>grenzen die dwars door "
                  "volkeren liepen</strong>, <strong>een economie die op uitvoer naar Europa werd "
                  "afgestemd</strong>, en <strong>gezagsstructuren die door de kolonisator werden "
                  "vervangen</strong>."),
            ("p", "Ook in Azië: <strong>Groot-Brittannië in Indië</strong>, <strong>Frankrijk in "
                  "Indochina</strong> en <strong>Nederland in de Indische archipel</strong>. "
                  "<strong>Japan moderniseerde vanaf de Meiji-restauratie van 1868 snel en werd zelf een "
                  "koloniale macht</strong>. <strong>Rusland breidde over land uit tot aan de Stille "
                  "Oceaan</strong>. En <strong>de Verenigde Staten hielden zich er niet buiten</strong>: "
                  "denk aan de Filipijnen en Cuba na 1898."),
            ("p", "Een <strong>invloedssfeer</strong> is <strong>een gebied waar een mogendheid de dienst "
                  "uitmaakt zonder het te besturen</strong>. Dat is de lichtere vorm van overheersing, en "
                  "ze komt vooral in China voor."),
        ]),
        dict(kop="De Congo-Vrijstaat", blokken=[
            ("p", "De <strong>Congo-Vrijstaat</strong> was tussen 1885 en 1908 <strong>het persoonlijke "
                  "bezit van Leopold II</strong>, niet van België. De ontdekkingsreiziger "
                  "<strong>Stanley</strong> verkende het gebied voor hem en sloot er verdragen met lokale "
                  "leiders. De Vrijstaat verdiende vooral geld met <strong>rubber en ivoor</strong>."),
            ("p", "Het <strong>rubberregime</strong> werkte zo: <strong>dorpen moesten een vastgelegde "
                  "hoeveelheid rubber leveren</strong>, <strong>wie te weinig leverde werd zwaar "
                  "gestraft</strong>, en <strong>vrouwen en kinderen werden gegijzeld als drukmiddel</strong>. "
                  "<strong>De bevolking van Congo nam tijdens de Vrijstaat sterk af door geweld, honger en "
                  "ziekte.</strong>"),
            ("p", "Rond 1900 voerden <strong>Edmund Dene Morel met zijn hervormingsbeweging</strong>, "
                  "<strong>Roger Casement met zijn verslag voor de Britse regering</strong> en "
                  "<strong>schrijvers zoals Mark Twain en Arthur Conan Doyle</strong> campagne tegen dat "
                  "bewind. Onder die internationale druk nam de Belgische staat de kolonie in "
                  "<strong>1908</strong> over."),
        ]),
        dict(kop="Belgisch Congo", blokken=[
            ("p", "Belgisch Congo werd bestuurd door <strong>drie machten samen</strong>: <strong>de staat "
                  "met haar ambtenaren en leger</strong>, <strong>de kerk met haar missies en "
                  "scholen</strong>, en <strong>de grote bedrijven met hun mijnen en plantages</strong>. Men "
                  "noemt dat de koloniale drie-eenheid."),
            ("p", "<strong>Paternalisme</strong> in het koloniale bestuur betekent dat <strong>men de "
                  "bevolking behandelt als kinderen die men opvoedt</strong>. Zo bleef <strong>het onderwijs "
                  "vooral in handen van de missies en grotendeels bij lager onderwijs steken</strong>. De "
                  "kolonie leverde <strong>koper uit Katanga</strong>, <strong>diamant</strong> en "
                  "<strong>uranium</strong>."),
            ("p", "De <strong>beeldvorming over Leopold II en Congo</strong> ging in België <strong>van "
                  "koning-bouwer naar een veel kritischer blik</strong>. Let op wat dat wel en niet "
                  "betekent: <strong>dat de blik op een koloniaal verleden verandert, betekent niet dat de "
                  "feiten veranderen</strong>. Wat verandert, zijn de vragen die men stelt en de bronnen die "
                  "men laat spreken."),
        ]),
        dict(kop="China in de 19de eeuw", blokken=[
            ("p", "China werd in de 19de eeuw geregeerd door de <strong>Qing-dynastie</strong>. Het kampte "
                  "met <strong>een sterk groeiende bevolking op te weinig grond</strong>, "
                  "<strong>wijdverspreide corruptie in het bestuur</strong> en <strong>grote opstanden zoals "
                  "die van de Taiping</strong>."),
            ("p", "De <strong>Opiumoorlogen</strong> met Groot-Brittannië gingen <strong>over de Britse "
                  "handel in opium die China wilde stoppen</strong>. Bij het <strong>Verdrag van "
                  "Nanking</strong> van 1842 moest China <strong>Hongkong</strong> afstaan. Zulke verdragen "
                  "heten <strong>ongelijke verdragen</strong> omdat <strong>ze enkel aan China "
                  "verplichtingen oplegden</strong>."),
            ("p", "<strong>China werd niet volledig gekoloniseerd zoals Congo.</strong> Het bleef formeel "
                  "een keizerrijk, maar werd in invloedssferen verdeeld. Het gevolg van de westerse "
                  "contacten: <strong>het gezag van de keizer verzwakte en in 1912 viel het rijk</strong>."),
            ("kader", "Vergelijk de twee: in <strong>Congo</strong> volledige bezetting en rechtstreeks "
                      "bestuur, in <strong>China</strong> invloedssferen en ongelijke verdragen. Twee "
                      "vormen van hetzelfde imperialisme, met heel andere gevolgen tot vandaag."),
        ]),
    ],
    onthoud=[
        "Rond 1880 begint de wedloop om Afrika: het modern imperialisme.",
        "Repeteergeweren, stoomschepen en kinine maakten de bezetting mogelijk.",
        "Sociaal darwinisme gebruikte de strijd om het bestaan om overheersing goed te praten.",
        "Conferentie van Berlijn (1884-1885): je moest een gebied werkelijk bezetten en besturen.",
        "Tegen 1914 bleven in Afrika alleen Ethiopië en Liberia zelfstandig.",
        "Een invloedssfeer is een gebied waar een mogendheid de dienst uitmaakt zonder het te besturen.",
        "De Congo-Vrijstaat was van 1885 tot 1908 persoonlijk bezit van Leopold II.",
        "Belgisch Congo werd bestuurd door staat, kerk en grote bedrijven samen.",
        "China werd niet volledig gekoloniseerd maar kreeg ongelijke verdragen en invloedssferen.",
    ],
)

# ───────────────────────── 5. De Eerste Wereldoorlog en de Russische revoluties
BUNDELS["de-eerste-wereldoorlog-en-de-russische-revoluties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De Eerste Wereldoorlog en de Russische revoluties",
    onder="Van Sarajevo tot Versailles, en van de tsaar tot de bolsjewieken.",
    secties=[
        dict(kop="Aanleiding en oorzaken", blokken=[
            ("p", "In juni 1914 wordt in Sarajevo de Oostenrijkse troonopvolger "
                  "<strong>Frans Ferdinand</strong> doodgeschoten. Dat is de "
                  "<strong>aanleiding</strong>, niet de oorzaak: <strong>de aanleiding is de vonk, de "
                  "oorzaken zijn de opgestapelde spanningen</strong>."),
            ("p", "De <strong>diepere oorzaken</strong>: <strong>nationalisme en wedijver tussen de grote "
                  "mogendheden</strong>, <strong>militarisme met een wedloop in bewapening</strong>, en "
                  "<strong>een web van bondgenootschappen dat landen meesleepte</strong>. De "
                  "<strong>Triple Entente</strong> bestond uit <strong>Frankrijk, Rusland en "
                  "Groot-Brittannië</strong>, tegenover de Centralen."),
            ("p", "Het Duitse aanvalsplan, <strong>het plan Von Schlieffen</strong>, wilde Frankrijk snel "
                  "uitschakelen <strong>door door het neutrale België te trekken</strong>. "
                  "<strong>België koos in 1914 dus niet zelf de kant van Frankrijk</strong>: het werd "
                  "binnengevallen en verdedigde zijn neutraliteit. <strong>Bij het uitbreken dachten veel "
                  "mensen dat de oorlog voor de kerstdagen voorbij zou zijn.</strong>"),
        ]),
        dict(kop="Een totale oorlog", blokken=[
            ("p", "De <strong>bewegingsoorlog van 1914 ging over in een loopgravenoorlog</strong> doordat "
                  "<strong>de opmars vastliep en beide legers zich ingroeven</strong>. Nieuwe wapens maakten "
                  "er een slachting zonder weerga van: <strong>de mitrailleur</strong>, <strong>gifgas</strong> "
                  "en <strong>de tank</strong>."),
            ("p", "Men noemt het een <strong>totale oorlog</strong> omdat <strong>de hele samenleving voor "
                  "de oorlog werd ingezet</strong>: fabrieken, voedsel, vrouwen, kolonies, nieuws. "
                  "<strong>Propaganda moest de steun van de bevolking vasthouden.</strong> En er veranderde "
                  "iets blijvends aan de plaats van vrouwen: <strong>ze namen in de fabrieken het werk van "
                  "de mannen over</strong>."),
            ("p", "In België hield het leger stand aan de rivier de <strong>IJzer</strong>, het IJzerfront. <strong>Het Belgische "
                  "leger hield tijdens de oorlog een klein stuk van het land bezet</strong>, en die "
                  "vuurdoop was vooral waard dat <strong>het laatste stuk vrij België in handen "
                  "bleef</strong>. Van de oorlog in Vlaanderen zie je vandaag kerkhoven, monumenten en "
                  "musea; <strong>de loopgraven zelf kan je niet meer in hun oorspronkelijke staat "
                  "zien</strong>, wat er te bezoeken valt, is heraangelegd."),
            ("p", "In 1917 traden de <strong>Verenigde Staten</strong> toe <strong>door de onbeperkte "
                  "Duitse duikbotenoorlog</strong>. <strong>Rusland vocht niet tot het einde mee</strong>: "
                  "na de revolutie sloot het een aparte vrede. De wapenstilstand viel op "
                  "<strong>11/11</strong> van 1918."),
            ("p", "De gevolgen situeer je in verschillende domeinen tegelijk: <strong>het politieke domein, "
                  "met nieuwe staten en regimes</strong>, <strong>het economische domein, met schulden en "
                  "verwoesting</strong>, en <strong>het sociale domein, met miljoenen doden en "
                  "gewonden</strong>."),
        ]),
        dict(kop="Versailles en de Volkenbond", blokken=[
            ("p", "De Amerikaanse president <strong>Woodrow Wilson</strong> stelde in 1918 een plan van "
                  "veertien punten voor, het <strong>Veertienpuntenplan</strong>. Daarin stonden <strong>open diplomatie in plaats van geheime "
                  "verdragen</strong>, <strong>het zelfbeschikkingsrecht van de volkeren</strong> en "
                  "<strong>de oprichting van een volkerenbond</strong>."),
            ("p", "Het <strong>Verdrag van Versailles</strong> legde Duitsland op dat <strong>het de schuld "
                  "voor de oorlog moest erkennen</strong>, dat <strong>het herstelbetalingen moest "
                  "doen</strong> en dat <strong>het nog maar een klein leger mocht houden</strong>. "
                  "<strong>Elzas-Lotharingen</strong> ging terug naar Frankrijk. "
                  "<strong>In Duitsland werd het verdrag als een opgelegd dictaat ervaren.</strong> Een "
                  "<strong>onbedoeld gevolg</strong> daarvan was <strong>de voedingsbodem voor extreme "
                  "partijen in Duitsland</strong>; <strong>de wrok over het verdrag hielp Hitler aan "
                  "steun</strong>, en dat is het verband met de Tweede Wereldoorlog."),
            ("p", "De <strong>Volkenbond</strong> werd in 1920 opgericht <strong>om conflicten tussen "
                  "landen vreedzaam te beslechten</strong>. Haar <strong>zwaktes</strong>: <strong>de "
                  "Verenigde Staten traden nooit toe</strong>, <strong>de bond had geen eigen leger</strong>, "
                  "en <strong>beslissingen vroegen de instemming van iedereen</strong>. Ze kon landen die "
                  "zich niet aan de afspraken hielden dus <strong>niet met een eigen leger tot de orde "
                  "roepen</strong>."),
        ]),
        dict(kop="Rusland in 1917", blokken=[
            ("p", "Aan de vooravond van 1917 was Rusland onder tsaar <strong>Nicolaas II</strong> "
                  "<strong>een autocratie met een grote, arme boerenbevolking</strong>. De Eerste "
                  "Wereldoorlog speelde een sleutelrol: <strong>nederlagen en honger ondermijnden het gezag "
                  "van de tsaar</strong>."),
            ("p", "Bij de <strong>Februarirevolutie van 1917</strong> <strong>deed de tsaar troonsafstand "
                  "en kwam er een voorlopige regering</strong>. Die verloor snel haar steun omdat <strong>ze "
                  "de oorlog voortzette</strong>, <strong>ze de verdeling van de grond uitstelde</strong> en "
                  "<strong>de voedseltekorten bleven aanhouden</strong>."),
            ("p", "<strong>Lenin</strong> vatte zijn belofte samen in drie woorden: <strong>vrede, brood en "
                  "land</strong>. De <strong>Oktoberrevolutie van 1917 bracht de bolsjewieken onder Lenin "
                  "aan de macht</strong>. De <strong>dictatuur van het proletariaat</strong> betekent dat "
                  "<strong>de arbeidersklasse alle macht grijpt in de overgangsfase</strong>."),
            ("p", "<strong>Na de Oktoberrevolutie bleef het in Rusland niet rustig en kwam er geen meteen "
                  "vrede</strong>: er volgde een burgeroorlog van jaren. Het <strong>oorlogscommunisme</strong> "
                  "van die jaren herken je hieraan: <strong>de industrie kwam in handen van de "
                  "staat</strong>, <strong>graan werd bij de boeren opgeëist</strong> en <strong>voedsel "
                  "werd op rantsoen gezet</strong>."),
        ]),
    ],
    onthoud=[
        "De moord op Frans Ferdinand is de aanleiding; de oorzaken zijn de opgestapelde spanningen.",
        "Het plan Von Schlieffen trok door het neutrale België om Frankrijk snel uit te schakelen.",
        "Een totale oorlog zet de hele samenleving in; aan de IJzer hield het Belgische leger stand.",
        "De Verenigde Staten traden in 1917 toe door de onbeperkte Duitse duikbotenoorlog.",
        "Versailles legde Duitsland schuld, herstelbetalingen en een klein leger op.",
        "De Volkenbond (1920) had geen eigen leger en de Verenigde Staten traden nooit toe.",
        "Bij de Februarirevolutie van 1917 deed de tsaar troonsafstand.",
        "De Oktoberrevolutie van 1917 bracht de bolsjewieken onder Lenin aan de macht.",
        "Oorlogscommunisme: industrie in handen van de staat, graan opgeëist, voedsel op rantsoen.",
    ],
)

# ───────────────────────── 6. Interbellum: totalitarisme en crisis
BUNDELS["interbellum-totalitarisme-en-crisis-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Interbellum: totalitarisme en crisis",
    onder="De crash van 1929, de New Deal, en drie regimes die alles wilden beheersen.",
    secties=[
        dict(kop="De crisis van de jaren dertig", blokken=[
            ("p", "In oktober 1929 stort de beurs van New York in: de <strong>beurscrash van Wall "
                  "Street</strong>. De oorzaken: <strong>aandelen kopen met geleend geld</strong>, "
                  "<strong>overproductie in industrie en landbouw</strong>, en <strong>een zeer ongelijke "
                  "verdeling van de welvaart</strong>."),
            ("p", "<strong>De crisis bleef niet beperkt tot de Verenigde Staten.</strong> In Europa leidde "
                  "ze tot <strong>massale werkloosheid en politieke radicalisering</strong>. Het verband met "
                  "de extreme partijen is rechtstreeks: <strong>werkloosheid en armoede maakten mensen "
                  "vatbaar voor wie orde beloofde</strong>. Leg je dat verband uit, dan pas je de "
                  "redeneerwijze <strong>oorzaak en gevolg benoemen</strong> toe."),
            ("p", "De Amerikaanse president <strong>Roosevelt</strong> lanceerde vanaf 1933 de <strong>New "
                  "Deal</strong>: <strong>grote openbare werken om mensen aan het werk te zetten</strong>, "
                  "<strong>toezicht op de banken en de beurs</strong>, en <strong>de eerste federale sociale "
                  "zekerheid</strong>. <strong>Daarmee brak de Amerikaanse overheid met het idee dat ze zich "
                  "beter niet met de economie bemoeide.</strong>"),
            ("p", "<strong>De crisis trof de Sovjet-Unie veel minder hard dan het Westen</strong>, omdat "
                  "haar economie buiten de wereldmarkt om werd gepland. Dat gaf het stelsel in die jaren "
                  "een aantrekkingskracht die achteraf moeilijk voor te stellen is."),
        ]),
        dict(kop="De Sovjet-Unie onder Stalin", blokken=[
            ("p", "Na de dood van Lenin in 1924 nam <strong>Stalin</strong> de macht over. De "
                  "<strong>vijfjarenplannen</strong> vanaf 1928 hadden als doel <strong>de zware industrie "
                  "in hoog tempo uit te bouwen</strong>; je situeert ze in de eerste plaats in het "
                  "<strong>economische domein</strong>."),
            ("p", "<strong>Collectivisatie</strong> is het <strong>samenvoegen van kleine boerderijen tot "
                  "grote staats- en gemeenschapsbedrijven</strong>. De gevolgen: <strong>verzet van boeren "
                  "dat met geweld gebroken werd</strong>, <strong>deportatie van wie als koelak werd "
                  "aangeduid</strong>, en <strong>een zware hongersnood, onder meer in Oekraïne</strong>."),
            ("p", "De <strong>goelags</strong> waren <strong>strafkampen waar gevangenen dwangarbeid "
                  "verrichtten</strong>. <strong>Tijdens de Grote Zuivering liet Stalin ook partijgenoten en "
                  "legerofficieren veroordelen en terechtstellen.</strong> Een "
                  "<strong>personencultus</strong> is dat <strong>de leider als onfeilbaar en haast "
                  "bovenmenselijk wordt voorgesteld</strong>. De kunst heette <strong>socialistisch "
                  "realisme</strong> omdat <strong>ze de arbeider en de opbouw van het land moest "
                  "verheerlijken</strong>."),
            ("kader", "Een <strong>totalitaire staat</strong> herken je aan <strong>één partij en één "
                      "leider</strong>, <strong>controle over pers, onderwijs en kunst</strong>, en "
                      "<strong>een geheime politie die tegenstanders uitschakelt</strong>. "
                      "<strong>Propaganda en terreur sluiten elkaar niet uit</strong>: elk regime gebruikt "
                      "ze naast elkaar, de ene hand lokt en de andere dreigt."),
        ]),
        dict(kop="Het Italiaanse fascisme", blokken=[
            ("p", "<strong>Mussolini</strong> kwam in 1922 aan de macht: <strong>na de Mars op Rome "
                  "benoemde de koning hem tot regeringsleider</strong>. Hij noemde zich de "
                  "<strong>Duce</strong>."),
            ("p", "Hij bouwde Italië tot een totalitaire staat om: <strong>hij verbood de andere "
                  "partijen</strong>, <strong>hij bracht de pers onder controle</strong> en <strong>hij "
                  "richtte een politieke politie op</strong>. <strong>Het fascisme stelde de staat en de "
                  "natie boven het individu.</strong>"),
        ]),
        dict(kop="Het nationaalsocialisme in Duitsland", blokken=[
            ("p", "<strong>Hitler werd rijkskanselier in januari 1933.</strong> In 1933 en 1934 greep hij "
                  "alle macht: <strong>de Machtigingswet gaf hem het recht zonder parlement te "
                  "regeren</strong>, <strong>de andere partijen en de vakbonden werden verboden</strong>, en "
                  "<strong>na de dood van Hindenburg voegde hij het presidentschap bij zijn ambt</strong>. "
                  "In februari 1933 brandde de <strong>Rijksdag</strong> af (de <strong>Rijksdagbrand</strong>), waarna hij de grondrechten liet "
                  "opschorten."),
            ("p", "De werkloosheid ging naar beneden <strong>met openbare werken en vooral met "
                  "herbewapening</strong>. Om de bevolking in de pas te doen lopen gebruikte het <strong>naziregime</strong> "
                  "<strong>propaganda in pers, film en radio</strong>, <strong>jeugdbewegingen waar kinderen "
                  "verplicht in terechtkwamen</strong>, en <strong>een geheime politie en "
                  "concentratiekampen</strong>."),
            ("p", "De <strong>Neurenbergse wetten van 1935</strong> bepaalden dat <strong>Joden hun "
                  "burgerrechten verloren en niet meer mochten huwen met niet-Joden</strong>. <strong>In de "
                  "nacht van 9 op 10 november 1938 werden in heel Duitsland synagogen in brand gestoken en "
                  "Joodse winkels vernield.</strong>"),
            ("p", "Wat het <strong>stalinisme</strong>, het Italiaanse fascisme en het nationaalsocialisme <strong>gemeen hebben</strong>: <strong>één partij, één leider en "
                  "geen ruimte voor tegenspraak</strong>. Waarin het <strong>nationaalsocialisme "
                  "verschilde</strong> van het Italiaanse fascisme: <strong>de rassenleer en het "
                  "antisemitisme stonden centraal</strong>. En <strong>de democratieën in West-Europa bleven "
                  "in de jaren dertig niet onaangeroerd</strong>: ook daar groeiden crisis, werkloosheid en "
                  "extreme partijen."),
        ]),
        dict(kop="Naar de oorlog", blokken=[
            ("p", "Tussen 1935 en 1939 tastte Hitler de afspraken van Versailles af: <strong>hij voerde "
                  "opnieuw de dienstplicht in en herbewapende</strong>, <strong>hij liet troepen het "
                  "Rijnland binnentrekken</strong>, en <strong>hij lijfde Oostenrijk in bij Duitsland</strong>."),
            ("p", "Op de <strong>Conferentie van München</strong> van september 1938 werd beslist dat "
                  "<strong>Duitsland het Sudetenland van Tsjecho-Slowakije mocht inlijven</strong>. De "
                  "politiek waarbij Frankrijk en Groot-Brittannië toegevingen deden om een oorlog te "
                  "vermijden, heet <strong>appeasement</strong>."),
            ("p", "In augustus 1939 sprak Duitsland met de Sovjet-Unie <strong>een niet-aanvalspact met "
                  "een geheime verdeling van Polen</strong> af. <strong>Hitler wachtte daarna geen jaar "
                  "meer</strong>: amper een week later viel hij Polen binnen."),
        ]),
    ],
    onthoud=[
        "Oorzaken van de crash van 1929: aandelen op krediet, overproductie en ongelijke welvaart.",
        "Met de New Deal vanaf 1933 ging de Amerikaanse overheid zich met de economie bemoeien.",
        "Stalins vijfjarenplannen vanaf 1928 moesten de zware industrie in hoog tempo uitbouwen.",
        "Collectivisatie leidde tot een zware hongersnood, onder meer in Oekraïne.",
        "Een totalitaire staat heeft één partij, één leider en een geheime politie.",
        "Mussolini kwam in 1922 aan de macht na de Mars op Rome.",
        "Hitler werd rijkskanselier in januari 1933; de Machtigingswet liet hem zonder parlement regeren.",
        "Door de Neurenbergse wetten van 1935 verloren Joden hun burgerrechten.",
        "Appeasement: in München (1938) mocht Duitsland het Sudetenland inlijven.",
    ],
)

# ───────────────────────── 7. De Tweede Wereldoorlog en de Holocaust
BUNDELS["de-tweede-wereldoorlog-en-de-holocaust-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De Tweede Wereldoorlog en de Holocaust",
    onder="Het verloop van de oorlog, bezet België, en de vernietiging van de Europese Joden.",
    secties=[
        dict(kop="Oorzaken en verloop", blokken=[
            ("p", "De Tweede Wereldoorlog begon in Europa met <strong>de Duitse inval in Polen</strong>. "
                  "De <strong>oorzaken</strong> die men aanhaalt: <strong>de wrok over het Verdrag van "
                  "Versailles</strong>, <strong>de economische crisis van de jaren dertig</strong>, en "
                  "<strong>de expansiedrang van de totalitaire regimes</strong>."),
            ("p", "De Duitse aanvalstactiek met snelle tankcolonnes en vliegtuigen heet "
                  "<strong>Blitzkrieg</strong>. De kern van de <strong>asmogendheden</strong> was "
                  "<strong>Duitsland, Italië en Japan</strong>. <strong>Tussen 1939 en 1942 boekten de "
                  "asmogendheden vooral overwinningen.</strong>"),
            ("p", "Op <strong>22 juni 1941 viel Duitsland de Sovjet-Unie binnen</strong>. In december 1941 "
                  "kwamen de Verenigde Staten erin terecht <strong>door de Japanse aanval op Pearl "
                  "Harbor</strong>. De <strong>keerpunten van 1942</strong> zijn <strong>Stalingrad aan het "
                  "oostfront</strong>, <strong>El Alamein in Noord-Afrika</strong> en <strong>Midway in de "
                  "Stille Oceaan</strong>."),
            ("p", "De geallieerden landden in Normandië op <strong>6/6</strong> van 1944. De oorlog "
                  "<strong>eindigde in Europa met de Duitse capitulatie in mei 1945</strong> en "
                  "<strong>in Azië na de atoombommen op Hiroshima en Nagasaki</strong>."),
        ]),
        dict(kop="De twee wereldoorlogen vergeleken", blokken=[
            ("p", "Wat ze <strong>gemeen hebben</strong>: <strong>het zijn allebei totale oorlogen waarin "
                  "de hele samenleving betrokken is</strong>. Waarin de tweede <strong>verschilt</strong>: "
                  "<strong>de oorlog werd op veel meer plaatsen in de wereld uitgevochten</strong>, "
                  "<strong>bezetting en uitroeiingspolitiek hoorden tot de oorlogvoering</strong>, en "
                  "<strong>de legers bewogen zich snel in plaats van zich in te graven</strong>."),
            ("p", "<strong>Gifgas aan het front</strong> hoort bij de <strong>Eerste</strong> "
                  "Wereldoorlog, niet bij de tweede: aan het front werd het toen niet meer ingezet. "
                  "<strong>In de Tweede Wereldoorlog vielen meer burgerslachtoffers dan militaire "
                  "slachtoffers</strong>, en <strong>de geallieerden en de asmogendheden vochten niet alleen "
                  "in Europa</strong> maar ook in Azië, Afrika en op de oceanen."),
            ("p", "De <strong>gevolgen voor de wereldorde</strong>: <strong>de Verenigde Staten en de "
                  "Sovjet-Unie werden supermachten</strong>, <strong>de Verenigde Naties werden "
                  "opgericht</strong>, en <strong>de dekolonisatie kwam op gang</strong>. De nazileiders "
                  "werden berecht in <strong>Neurenberg</strong>. <strong>Duitsland bleef na de oorlog niet "
                  "één land met één regering</strong>: het werd in bezettingszones verdeeld en in 1949 in "
                  "twee staten gesplitst. In 1948 nam de jonge VN de <strong>Universele Verklaring van de "
                  "Rechten van de Mens</strong> aan."),
        ]),
        dict(kop="Bezet België", blokken=[
            ("p", "Duitsland viel België binnen <strong>op 10 mei 1940</strong>. De Belgische veldtocht "
                  "duurde <strong>18</strong> dagen. Er ontstond een breuk tussen koning Leopold III en de "
                  "regering: <strong>de koning bleef in bezet land, de regering week uit naar "
                  "Londen</strong>."),
            ("p", "<strong>Collaboratie</strong> nam verschillende vormen aan: <strong>politieke "
                  "collaboratie door bewegingen als het VNV en Rex</strong>, <strong>militaire collaboratie "
                  "door vrijwilligers aan het oostfront</strong>, en <strong>economische collaboratie door "
                  "bedrijven die voor de bezetter werkten</strong>."),
            ("p", "<strong>Verzetslieden</strong> gingen <strong>sluikbladen drukken en "
                  "verspreiden</strong>, <strong>ontsnappingslijnen voor piloten opzetten</strong> en "
                  "<strong>onderduikadressen zoeken voor Joodse kinderen</strong>. <strong>In 1943 slaagden "
                  "drie verzetslieden erin een deportatietrein bij Boortmeerbeek tot stilstand te "
                  "brengen.</strong>"),
            ("p", "<strong>Antwerpen</strong> werd in september 1944 bevrijd met een haven die vrijwel "
                  "onbeschadigd bleef, wat de bevoorrading van de geallieerden redde. Het "
                  "<strong>Ardennenoffensief</strong> was <strong>een laatste Duits tegenoffensief in de "
                  "winter van 1944</strong>. <strong>Na de bevrijding werden mensen die met de bezetter "
                  "hadden samengewerkt vervolgd in wat men de repressie noemt.</strong>"),
            ("p", "Let op bij herinneringsplaatsen: <strong>de bewaarde loopgraven aan het IJzerfront "
                  "herinneren aan de Eerste</strong> Wereldoorlog, niet aan de tweede. En "
                  "<strong>collaboratie en verzet waren geen twee scherp gescheiden kampen waartussen niets "
                  "lag</strong>: de meeste mensen probeerden vooral te overleven, en sommigen deden in de "
                  "loop van vier jaar allebei iets."),
        ]),
        dict(kop="De Holocaust", blokken=[
            ("p", "De vervolging van de Joden in nazi-Duitsland verliep in stappen: <strong>eerst "
                  "uitsluiting uit het openbare leven</strong>, <strong>daarna gedwongen samenleven in "
                  "getto's</strong>, en <strong>ten slotte de systematische vernietiging in kampen</strong>. "
                  "Op de <strong>Wannseeconferentie van januari 1942</strong> werd <strong>de praktische "
                  "organisatie van de vernietiging van de Joden</strong> besproken."),
            ("p", "Bij benadering kwamen <strong>6</strong> miljoen Joden om. Uit België vertrokken de "
                  "treinen vanuit de <strong>Dossinkazerne</strong> in Mechelen naar Auschwitz. Het regime "
                  "vervolgde en vermoordde ook <strong>Roma en Sinti</strong>, <strong>mensen met een "
                  "beperking</strong> en <strong>politieke tegenstanders</strong>."),
            ("p", "<strong>Genocide</strong> is het opzettelijk geheel of gedeeltelijk vernietigen van een "
                  "nationale, etnische, raciale of religieuze groep. Dat is op de Holocaust van toepassing, "
                  "<strong>want een hele bevolkingsgroep moest doelbewust verdwijnen</strong>. "
                  "<strong>Het begrip genocide bestond nog niet voor de Tweede Wereldoorlog</strong>: het "
                  "werd in 1944 gemunt en kwam in 1948 in het internationale recht."),
            ("p", "<strong>Getuigenissen van overlevenden</strong> blijven belangrijk omdat <strong>ze de "
                  "ervaring weergeven die cijfers niet kunnen tonen</strong>. En zeg je dat de Holocaust "
                  "<strong>niet enkel het werk was van enkele leiders maar ook van gewone ambtenaren en "
                  "spoorwegpersoneel</strong>, dan gebruik je de redeneerwijze <strong>menselijke actoren "
                  "benoemen</strong>."),
        ]),
    ],
    onthoud=[
        "De oorlog begon in Europa met de Duitse inval in Polen.",
        "De keerpunten van 1942 zijn Stalingrad, El Alamein en Midway.",
        "In de Tweede Wereldoorlog vielen meer burgerslachtoffers dan militaire slachtoffers.",
        "Na de oorlog werden de Verenigde Staten en de Sovjet-Unie supermachten.",
        "Duitsland viel België binnen op 10 mei 1940; de veldtocht duurde 18 dagen.",
        "Collaboratie was politiek, militair of economisch; na de bevrijding volgde de repressie.",
        "Op de Wannseeconferentie van januari 1942 werd de organisatie van de vernietiging van de Joden besproken.",
        "Bij benadering kwamen 6 miljoen Joden om.",
        "Uit België vertrokken de treinen vanuit de Dossinkazerne in Mechelen naar Auschwitz.",
    ],
)

# ───────────────────────── 8. Een nieuwe wereldorde: VN, Koude Oorlog en Europa
BUNDELS["een-nieuwe-wereldorde-vn-koude-oorlog-en-europa-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een nieuwe wereldorde: VN, Koude Oorlog en Europa",
    onder="De Verenigde Naties, veertig jaar blokvorming, en een Europa dat ondertussen gebouwd werd.",
    secties=[
        dict(kop="De Verenigde Naties", blokken=[
            ("p", "De Verenigde Naties werden opgericht in <strong>1945</strong>, enkele maanden na het "
                  "einde van de oorlog in Europa. Het <strong>hoofddoel</strong> is <strong>de vrede en de "
                  "veiligheid in de wereld bewaren</strong>; daarnaast staan samenwerking en mensenrechten "
                  "in het Handvest."),
            ("p", "Tot de <strong>organen</strong> horen <strong>de Algemene Vergadering</strong>, "
                  "<strong>de Veiligheidsraad</strong> en <strong>het Internationaal Gerechtshof in Den "
                  "Haag</strong>. (De Europese Commissie hoort bij de EU, niet bij de VN.) In de "
                  "Veiligheidsraad hebben <strong>5</strong> landen een vast lidmaatschap met vetorecht: de "
                  "Verenigde Staten, Rusland, China, Frankrijk en het Verenigd Koninkrijk. <strong>Eén vast "
                  "lid kan met zijn veto een beslissing tegenhouden, ook als alle andere landen voor "
                  "zijn.</strong>"),
            ("p", "De <strong>duurzame ontwikkelingsdoelen</strong> zijn <strong>zeventien doelen die de "
                  "wereld tegen 2030 wil halen</strong>. De <strong>sterktes</strong> van de VN: <strong>een "
                  "plek waar alle landen elkaar kunnen spreken</strong>, <strong>humanitaire hulp bij rampen "
                  "en hongersnood</strong>, en <strong>het vastleggen van wereldwijde normen zoals de "
                  "mensenrechten</strong>. Haar grote zwakte is het vetorecht, en <strong>ze beschikt niet "
                  "over een eigen staand leger</strong>: blauwhelmen worden per missie door lidstaten "
                  "geleverd. De <strong>WHO</strong> is de organisatie die zich met de gezondheid in de "
                  "wereld bezighoudt."),
        ]),
        dict(kop="Het ontstaan van de Koude Oorlog", blokken=[
            ("p", "De Koude Oorlog ontstond doordat <strong>de twee overwinnaars van 1945 ideologisch "
                  "lijnrecht tegenover elkaar stonden</strong>: kapitalisme en democratie tegenover "
                  "communisme en partijstaat. Men noemt het een <strong>koude</strong> oorlog omdat <strong>de "
                  "twee supermachten nooit rechtstreeks tegen elkaar vochten</strong>."),
            ("p", "Churchill sprak in 1946 over het <strong>IJzeren Gordijn</strong>, de scheidslijn dwars door Europa. Tijdens de "
                  "<strong>blokkade van Berlijn</strong> in 1948 en 1949 <strong>bevoorraadden de westerse "
                  "geallieerden de stad maandenlang door de lucht</strong>. <strong>Duitsland bleef na 1949 "
                  "geen één staat</strong>: het werd in twee gesplitst, de Bondsrepubliek en de DDR, elk met "
                  "een eigen bondgenoot."),
            ("p", "De twee bondgenootschappen waren <strong>de NAVO en het Warschaupact</strong>. In "
                  "<strong>Hongarije in 1956</strong> werd <strong>een opstand tegen het communistische "
                  "bewind met tanks neergeslagen</strong>. De <strong>Berlijnse Muur</strong> werd gebouwd "
                  "in <strong>1961</strong>. De <strong>Cubacrisis van 1962</strong> ging <strong>over "
                  "Sovjetraketten op Cuba, vlak bij de Verenigde Staten</strong>."),
            ("p", "<strong>Beide kampen voerden een wapenwedloop met kernwapens.</strong> Naast wapens "
                  "zette men ook <strong>propaganda en spionage</strong>, <strong>economische hulp aan "
                  "bondgenoten</strong> en <strong>een wedloop in de ruimtevaart</strong> in."),
        ]),
        dict(kop="Van ontspanning tot het einde", blokken=[
            ("p", "De <strong>Praagse Lente van 1968</strong> was <strong>een poging tot hervorming in "
                  "Tsjecho-Slowakije, met tanks beëindigd</strong>; de Brezjnevdoctrine zei dat Moskou in "
                  "elk socialistisch land mocht ingrijpen. De <strong>SALT-besprekingen</strong> van de "
                  "jaren zeventig gingen <strong>over het beperken van het aantal kernwapens</strong>. Het "
                  "<strong>SDI-plan van president Reagan in 1983</strong> was <strong>een schild in de "
                  "ruimte tegen aanvallende raketten</strong>."),
            ("p", "De <strong>Sovjetleider</strong> <strong>Gorbatsjov</strong> lanceerde vanaf 1985 glasnost (openheid) en perestrojka "
                  "(hervorming). <strong>De Berlijnse Muur viel in november 1989, en twee jaar later hield "
                  "de Sovjet-Unie op te bestaan.</strong>"),
            ("p", "Het <strong>gevolg voor de internationale verhoudingen</strong>: <strong>er bleef één "
                  "supermacht over en de wereld werd voorlopig unipolair</strong>. <strong>Bij bipolair "
                  "zijn er twee machtscentra, bij multipolair meerdere</strong>; over welke van de drie "
                  "vandaag van toepassing is, wordt gediscussieerd. <strong>De verhoudingen tussen de "
                  "Verenigde Staten en Rusland zijn sindsdien niet voortdurend vriendschappelijk "
                  "gebleven</strong>: na een periode van toenadering liepen de spanningen weer op."),
        ]),
        dict(kop="De Europese eenmaking", blokken=[
            ("p", "De eenmaking begon met de <strong>Europese Gemeenschap voor Kolen en Staal</strong>: de "
                  "grondstoffen van de oorlog kwamen onder gezamenlijk beheer. De "
                  "<strong>doelstellingen</strong>: <strong>een nieuwe oorlog tussen Frankrijk en Duitsland "
                  "onmogelijk maken</strong>, <strong>de economieën met elkaar verweven door handel</strong>, "
                  "en <strong>samen sterker staan tegenover de grote mogendheden</strong>. Dat is meteen het "
                  "<strong>verband met de Tweede Wereldoorlog</strong>: <strong>de eenmaking moest een "
                  "nieuwe oorlog tussen buurlanden onmogelijk maken</strong>."),
            ("p", tabel(["Verdrag", "Jaar", "Wat het bracht"], [
                ["Verdrag van Rome", "1957", "de Europese Economische Gemeenschap en de gemeenschappelijke markt"],
                ["Verdrag van Maastricht", "1992", "de Europese Unie zelf en de weg naar een gezamenlijke munt"],
                ["Verdrag van Lissabon", "2007, in werking 2009", "een vaste voorzitter, meer macht voor het Parlement, bindende grondrechten"],
            ])),
            ("p", "<strong>Het Verdrag van Lissabon</strong> zorgde dus dat <strong>de Europese Raad een "
                  "vaste voorzitter kreeg</strong>, dat <strong>het Europees Parlement meer te zeggen "
                  "kreeg</strong> en dat <strong>het Handvest van de grondrechten bindend werd</strong>. De "
                  "euro kwam er al eerder, in 1999 giraal en in 2002 als biljetten."),
            ("p", "De instellingen uit elkaar houden: <strong>de Europese Commissie heeft het recht om "
                  "wetgeving voor te stellen</strong>, <strong>het Europees Parlement wordt rechtstreeks "
                  "door de burgers verkozen</strong>, en in <strong>de Europese Raad zetelen de "
                  "staatshoofden en regeringsleiders van de lidstaten</strong>. <strong>De Raad van de "
                  "Europese Unie en de Europese Raad zijn níét hetzelfde orgaan</strong>: in de eerste "
                  "zetelen de vakministers. En er bestaat daarnaast nog een Raad van Europa, die niet eens "
                  "bij de EU hoort."),
            ("p", "<strong>Uitdagingen</strong> vandaag: <strong>migratie en de bewaking van de "
                  "buitengrenzen</strong>, <strong>de klimaatomslag en de energiebevoorrading</strong>, en "
                  "<strong>euroscepsis, waarvan de brexit het verste voorbeeld is</strong>. <strong>Het "
                  "Verenigd Koninkrijk verliet de Unie na een volksraadpleging</strong>: gestemd in 2016, "
                  "van kracht eind januari 2020."),
        ]),
    ],
    onthoud=[
        "De VN werden in 1945 opgericht om de vrede en de veiligheid in de wereld te bewaren.",
        "In de Veiligheidsraad hebben 5 vaste leden een vetorecht.",
        "De Koude Oorlog heet koud omdat de supermachten nooit rechtstreeks tegen elkaar vochten.",
        "De Berlijnse Muur werd gebouwd in 1961; de Cubacrisis volgde in 1962.",
        "De Berlijnse Muur viel in november 1989, twee jaar later hield de Sovjet-Unie op te bestaan.",
        "Na de Koude Oorlog werd de wereld voorlopig unipolair.",
        "De Europese eenmaking moest een nieuwe oorlog tussen buurlanden onmogelijk maken.",
        "Verdragen: Rome 1957, Maastricht 1992, Lissabon 2007, in werking 2009.",
        "De Raad van de Europese Unie en de Europese Raad zijn niet hetzelfde orgaan.",
    ],
)

# ───────────────────────── 9. Dekolonisatie en de wereld van vandaag
BUNDELS["dekolonisatie-en-de-wereld-van-vandaag-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Dekolonisatie en de wereld van vandaag",
    onder="Hoe de koloniale rijken uiteenvielen, wat er in Congo gebeurde, en wat ervan overblijft.",
    secties=[
        dict(kop="Oorzaken en vormen", blokken=[
            ("p", "<strong>Dekolonisatie</strong> betekent dat <strong>koloniën zelfstandige staten worden "
                  "en zich losmaken van hun kolonisator</strong>. De <strong>oorzaken</strong> na 1945: "
                  "<strong>de Europese mogendheden kwamen verzwakt uit de Tweede Wereldoorlog</strong>, "
                  "<strong>in de koloniën groeiden nationalistische bewegingen met opgeleide leiders</strong>, "
                  "en <strong>het Handvest van de VN schreef het zelfbeschikkingsrecht van volkeren "
                  "in</strong>."),
            ("p", "<strong>Zowel de Verenigde Staten als de Sovjet-Unie stonden kritisch tegenover de "
                  "Europese koloniale rijken</strong>, elk om eigen redenen. <strong>India</strong> werd in "
                  "1947 onafhankelijk van het Verenigd Koninkrijk en gaf het voorbeeld."),
            ("p", "Dekolonisatie kon <strong>twee vormen</strong> aannemen: <strong>een onderhandelde "
                  "overdracht, of een gewapende onafhankelijkheidsstrijd</strong>. <strong>Niet alle "
                  "Afrikaanse koloniën werden zonder geweld onafhankelijk</strong>: in Algerije duurde de "
                  "oorlog acht jaar. <strong>1960 heet het Afrikajaar</strong> omdat <strong>zeventien "
                  "Afrikaanse koloniën in dat ene jaar onafhankelijk werden</strong>, Congo daaronder."),
        ]),
        dict(kop="Gevolgen en de Koude Oorlog", blokken=[
            ("p", "De grenzen van de nieuwe Afrikaanse staten zorgden vaak voor conflicten omdat <strong>ze "
                  "door de kolonisatoren getrokken waren, dwars door volkeren heen</strong>. <strong>Na de "
                  "onafhankelijkheid waren de meeste nieuwe staten niet meteen economisch "
                  "zelfstandig</strong>; daarvoor gebruikt men het woord <strong>neokolonialisme</strong>: "
                  "<strong>economische overheersing van een land dat politiek wel onafhankelijk is</strong>."),
            ("p", "Op de <strong>conferentie van Bandung in 1955</strong> <strong>kwamen Aziatische en "
                  "Afrikaanse landen samen tegen kolonialisme en blokvorming</strong>. Daaruit groeide de "
                  "beweging van de <strong>niet-gebonden</strong> landen."),
            ("p", "Het <strong>verband met de Koude Oorlog</strong>: <strong>de twee supermachten "
                  "probeerden de nieuwe staten naar hun kamp te trekken</strong>. <strong>Ze steunden daarbij "
                  "soms dictators, zolang die aan de juiste kant stonden.</strong> In <strong>Korea</strong>, "
                  "<strong>Vietnam</strong> en <strong>Angola</strong> voerden ze een strijd via anderen."),
            ("p", "De <strong>gevolgen op lange termijn</strong>: <strong>nieuwe staten met grenzen die "
                  "niet met volkeren samenvielen</strong>, <strong>een blijvende economische afhankelijkheid "
                  "van enkele grondstoffen</strong>, en <strong>een veel grotere groep landen binnen de "
                  "Verenigde Naties</strong>. <strong>De dekolonisatie zorgde ook voor migratie naar de "
                  "voormalige moederlanden in Europa.</strong>"),
        ]),
        dict(kop="Dekolonisering vandaag", blokken=[
            ("p", "<strong>Dekolonisering van het denken</strong> betekent <strong>opnieuw bekijken hoe wij "
                  "over het koloniale verleden spreken en leren</strong>. Tot het actuele debat horen de "
                  "vragen <strong>of voorwerpen uit koloniale musea moeten teruggaan naar het land van "
                  "herkomst</strong>, <strong>wat we doen met standbeelden van koloniale figuren in onze "
                  "straten</strong>, en <strong>welke plaats het koloniale verleden in het onderwijs "
                  "krijgt</strong>."),
            ("p", "Het <strong>AfricaMuseum in Tervuren</strong> bewaart in België de grote koloniale "
                  "verzameling en werd daarom grondig hertekend; bij de heropening in 2018 kreeg het "
                  "koloniale geweld er een plaats."),
        ]),
        dict(kop="Van Belgisch Congo naar onafhankelijkheid", blokken=[
            ("p", "In januari 1959 braken in <strong>Leopoldstad zware rellen</strong> uit, <strong>met "
                  "tientallen doden en veel vernieling</strong>. Dat dwong België tot een snelle "
                  "koerswijziging. Het <strong>plan van professor Van Bilsen</strong> uit 1955 had nog "
                  "<strong>een geleidelijke onafhankelijkheid over een termijn van dertig jaar</strong> "
                  "voorgesteld; dat was toen door iedereen weggehoond."),
            ("p", "Congo werd onafhankelijk op <strong>30 juni 1960</strong>, vijf maanden na de "
                  "rondetafelconferentie in Brussel. <strong>Congo beschikte toen niet over een ruime groep "
                  "Congolese universitair geschoolden</strong> om het land te besturen: het Belgische "
                  "bestuur had nauwelijks in hoger onderwijs voor Congolezen geïnvesteerd."),
            ("p", "<strong>Patrice Lumumba</strong> werd de eerste eerste minister, Kasa-Vubu president. "
                  "<strong>Katanga, de provincie met de grootste rijkdom aan kopererts</strong>, scheidde "
                  "zich af, met Belgische steun. <strong>De Verenigde Naties stuurden in 1960 een "
                  "vredesmacht naar Congo.</strong> In januari 1961 <strong>werd Lumumba na zijn afzetting "
                  "naar Katanga gebracht en daar vermoord</strong>; een Belgische onderzoekscommissie besloot "
                  "in 2001 tot een morele verantwoordelijkheid van Belgische regeringsleden."),
            ("p", "De <strong>Koude Oorlog</strong> speelde in de Congocrisis mee: <strong>Lumumba zocht steun bij Moskou, "
                  "waarna het Westen hem als gevaar zag</strong>."),
        ]),
        dict(kop="Congo van 1960 tot vandaag", blokken=[
            ("p", "Generaal <strong>Mobutu</strong> greep in 1965 de macht en bleef meer dan dertig jaar aan. In "
                  "1971 gaf hij het land de naam <strong>Zaïre</strong>. Zijn bewind was <strong>een "
                  "autoritair eenpartijbewind met veel corruptie en een persoonscultus</strong>. "
                  "<strong>Westerse landen bleven hem steunen omdat hij zich uitdrukkelijk tegen het "
                  "communisme keerde.</strong>"),
            ("p", "<strong>Laurent-Désiré Kabila</strong> verdreef hem in 1997 en gaf het land zijn naam "
                  "Congo terug. <strong>Het oosten van Congo is sindsdien niet vrij van gewapende "
                  "conflicten gebleven</strong>: in Kivu woeden er al decennia. Wat <strong>bijzonder was "
                  "aan de machtsoverdracht van 2019</strong>: <strong>voor het eerst ging de macht na "
                  "verkiezingen van de ene president naar de andere</strong>."),
            ("p", "De <strong>strijd om grondstoffen</strong> blijft belangrijk omdat <strong>kobalt en "
                  "coltan uit Congo in gsm's, laptops en elektrische auto's zitten</strong>. In de "
                  "<strong>verhouding tussen België en Congo</strong> spelen vandaag <strong>de teruggave "
                  "van voorwerpen die in de koloniale tijd zijn meegenomen</strong>, <strong>de vraag of "
                  "België officiële excuses moet aanbieden voor de kolonisatie</strong>, en <strong>de band "
                  "met de grote Congolese gemeenschap die in België woont</strong>. <strong>Koning Filip "
                  "drukte in 2020 zijn diepste spijt uit over de wonden van het koloniale verleden.</strong>"),
            ("kader", "Het <strong>verband met de wereld van vandaag</strong>: <strong>grenzen, talen, "
                      "migratie en handelsstromen van nu zijn er grotendeels door gevormd</strong>. Het "
                      "koloniale verleden ligt niet achter ons; het zit in de kaart, in de taal en in je "
                      "telefoon."),
        ]),
    ],
    onthoud=[
        "Dekolonisatie: koloniën worden zelfstandige staten en maken zich los van hun kolonisator.",
        "1960 heet het Afrikajaar: zeventien Afrikaanse koloniën werden toen onafhankelijk.",
        "Neokolonialisme is economische overheersing van een land dat politiek wel onafhankelijk is.",
        "In Bandung kwamen in 1955 Aziatische en Afrikaanse landen samen tegen kolonialisme en blokvorming.",
        "Dekolonisering van het denken: opnieuw bekijken hoe wij over het koloniale verleden spreken.",
        "Congo werd onafhankelijk op 30 juni 1960; Lumumba werd de eerste eerste minister.",
        "Lumumba werd in januari 1961 in Katanga vermoord.",
        "Mobutu greep in 1965 de macht en noemde het land in 1971 Zaïre.",
        "In 2019 ging de macht voor het eerst na verkiezingen van de ene president naar de andere.",
    ],
)

# ───────────────────────── 10. België na 1945
BUNDELS["belgie-na-1945-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="België na 1945",
    onder="Sociale zekerheid, drie breuklijnen, en de weg van een unitaire naar een federale staat.",
    secties=[
        dict(kop="Het sociaal pact en de sociale zekerheid", blokken=[
            ("p", "In het <strong>sociaal pact van 1944</strong> spraken werkgevers en vakbonden <strong>de "
                  "grondslagen van een verplichte sociale zekerheid voor alle werknemers</strong> af. Het "
                  "legde ook het overleg tussen beide vast, en dat model bestaat nog."),
            ("p", "Tot de takken van de <strong>sociale zekerheid</strong> horen <strong>de ziekteverzekering en de "
                  "terugbetaling van geneeskundige zorg</strong>, <strong>de werkloosheidsuitkering voor wie "
                  "zijn werk verliest</strong>, en <strong>het wettelijk pensioen en de kinderbijslag voor "
                  "gezinnen</strong>. <strong>Ze wordt vooral betaald met bijdragen op het loon van "
                  "werkenden en werkgevers</strong>, aangevuld uit de algemene belastingen."),
            ("p", "Dat België een <strong>verzorgingsstaat</strong> werd, betekent dat <strong>de overheid "
                  "bestaanszekerheid garandeert bij ziekte, werkloosheid en ouderdom</strong>. Nieuw aan het "
                  "idee van een <strong>actieve welvaartsstaat</strong> is dat <strong>de nadruk verschuift "
                  "van uitkeren naar mensen opnieuw aan het werk helpen</strong>, met opleiding, begeleiding "
                  "en kinderopvang."),
        ]),
        dict(kop="De drie breuklijnen", blokken=[
            ("p", "Door de Belgische samenleving lopen <strong>drie breuklijnen</strong>: de "
                  "<strong>levensbeschouwelijke breuklijn tussen gelovig en vrijzinnig</strong>, de "
                  "<strong>sociaaleconomische breuklijn tussen arbeid en kapitaal</strong>, en de "
                  "<strong>communautaire breuklijn tussen Vlamingen en Franstaligen</strong>."),
            ("p", tabel(["Debat of conflict", "Breuklijn"], [
                ["De schoolstrijd", "de levensbeschouwelijke breuklijn"],
                ["Hoeveel de hoogste inkomens moeten bijdragen", "de sociaaleconomische breuklijn"],
                ["Meer bevoegdheden voor Vlaanderen", "de communautaire breuklijn"],
                ["Hogere uitkeringen en een kortere werkweek", "de sociaaleconomische breuklijn, aan de kant van de arbeid"],
            ])),
            ("p", "In de <strong>schoolstrijd</strong> kwam de <strong>levensbeschouwelijke "
                  "breuklijn</strong> het sterkst naar boven. <strong>Het schoolpact van 1958 regelde de "
                  "financiering van zowel het vrije als het officiële onderwijs</strong> en garandeerde de "
                  "vrije schoolkeuze."),
        ]),
        dict(kop="De koningskwestie en Leuven Vlaams", blokken=[
            ("p", "De <strong>koningskwestie</strong> ging <strong>over de vraag of Leopold III na de "
                  "oorlog opnieuw koning mocht worden</strong>. De volksraadpleging viel in "
                  "<strong>1950</strong>: bijna achtenvijftig procent stemde voor, maar <strong>Vlaanderen "
                  "stemde heel anders dan Wallonië</strong>, ruim zeventig procent tegenover amper vier op "
                  "de tien. Het liep af doordat <strong>Leopold III troonsafstand deed ten voordele van zijn "
                  "zoon Boudewijn</strong>, na stakingen en drie doden bij een betoging in Grâce-Berleur."),
            ("p", "<strong>Leuven Vlaams</strong> in 1968 ging <strong>over de Franstalige afdeling van de "
                  "universiteit in Vlaams gebied</strong>. De <strong>gevolgen</strong>: <strong>de regering "
                  "van dat ogenblik viel over de kwestie</strong>, <strong>de grote nationale partijen "
                  "splitsten in een Vlaamse en een Franstalige</strong>, en <strong>de communautaire "
                  "breuklijn werd de belangrijkste van de drie</strong>. De Franstalige universiteit bouwde "
                  "een nieuwe stad: Louvain-la-Neuve."),
        ]),
        dict(kop="Verzuiling en ontzuiling", blokken=[
            ("p", "<strong>Verzuiling</strong> betekent dat <strong>de samenleving verdeeld is in groepen "
                  "met elk hun eigen scholen, ziekenfondsen en verenigingen</strong>. België kende de "
                  "<strong>katholieke zuil</strong>, de <strong>socialistische zuil</strong> en de "
                  "<strong>liberale zuil</strong>, elk met een partij, een vakbond, een ziekenfonds en een "
                  "hele reeks verenigingen."),
            ("p", "<strong>De verzuiling werd vanaf de jaren zestig net zwakker, niet sterker.</strong> De "
                  "<strong>oorzaken van de ontzuiling</strong>: <strong>de secularisering, waardoor de kerk "
                  "greep op het leven verloor</strong>, <strong>de individualisering, waardoor mensen vrijer "
                  "gingen kiezen</strong>, en <strong>het onderwijs en de televisie, die buiten de eigen zuil "
                  "keken</strong>. <strong>Zuilorganisaties zoals ziekenfondsen en vakbonden zijn daarmee "
                  "niet verdwenen</strong>: ze tellen nog miljoenen leden. Wat verdween, is de "
                  "vanzelfsprekendheid."),
        ]),
        dict(kop="Van unitaire naar federale staat", blokken=[
            ("p", "Een <strong>federale staat</strong> is <strong>een staat waarin de bevoegdheden "
                  "verdeeld zijn over verschillende zelfstandige niveaus</strong>. De eerste Belgische "
                  "staatshervorming viel in <strong>1970</strong>, en bracht <strong>de cultuurgemeenschappen "
                  "en de grondwettelijke vastlegging van de taalgebieden</strong>. <strong>Sinds de "
                  "staatshervorming van 1993 staat in artikel 1 van de grondwet dat België een federale "
                  "staat is.</strong> De <strong>zesde staatshervorming van 2011 tot 2014</strong> bracht "
                  "<strong>de overheveling van onder meer de kinderbijslag en delen van het "
                  "arbeidsmarktbeleid</strong>, en de splitsing van Brussel-Halle-Vilvoorde."),
            ("p", "België telt <strong>drie gewesten en drie gemeenschappen</strong>. De bevoegdheden van "
                  "een <strong>gemeenschap</strong> gaan <strong>over personen: onderwijs, cultuur, welzijn "
                  "en het gebruik van de talen</strong>. Tot de bevoegdheden van de <strong>gewesten</strong> "
                  "horen <strong>de ruimtelijke ordening en het vergunningenbeleid</strong>, <strong>het "
                  "leefmilieu en het beleid rond water en afval</strong>, en <strong>de economie, het "
                  "werkgelegenheidsbeleid en de mobiliteit</strong>. Een bevoegdheid die federaal gebleven is, is onder meer "
                  "<strong>de landsverdediging en het leger</strong>, naast justitie en het grootste deel "
                  "van de sociale zekerheid."),
            ("p", "<strong>In Vlaanderen werden het gewest en de gemeenschap samengevoegd tot één parlement "
                  "en één regering</strong>; de Franstaligen deden dat niet. Een wet van het Vlaams "
                  "Parlement heet een <strong>decreet</strong>. <strong>De federale overheid kan een "
                  "beslissing van het Vlaams Parlement niet zomaar overrulen</strong>: een decreet heeft "
                  "dezelfde kracht als een federale wet."),
            ("p", "Over het leven van een inwoner van Vlaanderen beslissen verschillende bestuursniveaus: <strong>de gemeente en de "
                  "provincie waar hij woont</strong>, <strong>het Vlaams Gewest en de Vlaamse "
                  "Gemeenschap</strong>, en <strong>de federale overheid en de Europese Unie</strong>. Tot "
                  "de <strong>principes van een democratische rechtsstaat</strong> horen <strong>de "
                  "scheiding van de wetgevende, de uitvoerende en de rechterlijke macht</strong>, "
                  "<strong>vrije en geheime verkiezingen waaraan iedereen mag deelnemen</strong>, en "
                  "<strong>grondrechten die ook de overheid zelf moet naleven</strong>."),
        ]),
        dict(kop="Partijen en actuele debatten", blokken=[
            ("p", "Standpunten in een bron plaats je op een breuklijn. <strong>Een partijprogramma kan "
                  "standpunten op meer dan één breuklijn tegelijk bevatten</strong>, dus kijk per standpunt "
                  "en niet naar de partij als geheel. <strong>Sinds de splitsing van de nationale partijen "
                  "kan een kiezer in Vlaanderen niet op een Franstalige partij stemmen</strong>, behalve in "
                  "de kieskring Brussel."),
            ("p", "<strong>Actuele debatten</strong> die rechtstreeks aan de drie breuklijnen raken: "
                  "<strong>de vraag of er nog een nieuwe staatshervorming moet komen</strong>, <strong>de "
                  "vraag hoe pensioenen en uitkeringen betaalbaar blijven</strong>, en <strong>de vraag "
                  "welke plaats levensbeschouwing in de school krijgt</strong>."),
            ("kader", "Het <strong>verband tussen de breuklijnen en de staatshervormingen</strong>: "
                      "<strong>de staatshervormingen zijn vooral antwoorden op de communautaire "
                      "breuklijn</strong>. Telkens de spanning te hoog opliep, kwam er een nieuwe ronde."),
        ]),
    ],
    onthoud=[
        "Het sociaal pact van 1944 legde de grondslagen van een verplichte sociale zekerheid.",
        "Drie breuklijnen: levensbeschouwelijk, sociaaleconomisch en communautair.",
        "Het schoolpact van 1958 regelde de financiering van het vrije en het officiële onderwijs.",
        "Na de koningskwestie deed Leopold III troonsafstand ten voordele van zijn zoon Boudewijn.",
        "Na Leuven Vlaams (1968) splitsten de nationale partijen in een Vlaamse en een Franstalige.",
        "De verzuiling werd vanaf de jaren zestig zwakker, maar zuilorganisaties zijn niet verdwenen.",
        "Eerste staatshervorming in 1970; sinds 1993 is België volgens artikel 1 een federale staat.",
        "Gemeenschappen gaan over personen, gewesten onder meer over ruimtelijke ordening en economie.",
        "De staatshervormingen zijn vooral antwoorden op de communautaire breuklijn.",
    ],
)

# ───────────────────────── 11. Denken, kunst en emancipatie
BUNDELS["denken-kunst-en-emancipatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Denken, kunst en emancipatie",
    onder="Vrouwen, holebi's en burgerrechten, een eigen jongerencultuur, en de popart.",
    secties=[
        dict(kop="Wat emancipatie is", blokken=[
            ("p", "<strong>Emancipatie</strong> is dat <strong>een groep gelijke rechten verwerft en zich "
                  "losmaakt uit een ondergeschikte positie</strong>. Let op het verschil met dekolonisatie: "
                  "dat gaat over een land dat zich van een ander losmaakt, emancipatie over mensen binnen "
                  "een samenleving. <strong>Emancipatiebewegingen lopen vaak over meerdere generaties voor "
                  "ze hun doel bereiken.</strong>"),
        ]),
        dict(kop="De emancipatie van de vrouw", blokken=[
            ("p", "Vrouwen kregen in België stemrecht voor de nationale verkiezingen in "
                  "<strong>1948</strong>, dertig jaar na de mannen; voor de gemeenteraad mochten sommigen al "
                  "sinds 1921 stemmen. In 1966 staakten de vrouwen van de wapenfabriek <strong>FN in "
                  "Herstal</strong> twaalf weken lang <strong>voor gelijk loon voor gelijk werk</strong>."),
            ("p", "Tot de <strong>emancipatie van de vrouw in België</strong> horen <strong>het stemrecht "
                  "voor vrouwen bij alle verkiezingen</strong>, <strong>de afschaffing van de man als "
                  "wettelijk hoofd van het gezin</strong> (in 1976), en <strong>de sterke stijging van het "
                  "aantal vrouwen in het hoger onderwijs</strong>."),
            ("p", "<strong>De loonkloof tussen mannen en vrouwen is vandaag niet volledig verdwenen.</strong> "
                  "Het <strong>glazen plafond</strong> is <strong>een onzichtbare grens die vrouwen "
                  "tegenhoudt om de hoogste functies te bereiken</strong>; daarom kwamen er quota voor de "
                  "raden van bestuur."),
        ]),
        dict(kop="De seksuele revolutie en lgbtqia+", blokken=[
            ("p", "De <strong>anticonceptiepil</strong> speelde een grote rol in de seksuele revolutie van "
                  "de jaren zestig: voor het eerst konden vrouwen zelf bepalen of en wanneer ze kinderen "
                  "kregen. <strong>De seksuele revolutie maakte het onderwerp seksualiteit bespreekbaar en "
                  "haalde er taboes van af.</strong> Abortus werd in België in <strong>1990</strong> uit het "
                  "strafrecht gehaald; koning Boudewijn weigerde te tekenen en werd daarom één dag in de "
                  "onmogelijkheid tot regeren gesteld."),
            ("p", "De afkorting <strong>lgbtqia+</strong> verwijst <strong>naar mensen met uiteenlopende "
                  "seksuele oriëntaties en genderidentiteiten</strong>; de plus staat er bewust bij. In 1969 "
                  "<strong>verzetten bezoekers van de Stonewall Inn in New York zich tegen een "
                  "politieoptreden, wat het begin werd van de holebibeweging</strong>. <strong>België was in "
                  "2003 na Nederland het tweede land ter wereld dat het huwelijk openstelde voor koppels van "
                  "hetzelfde geslacht</strong>; adoptie volgde in 2006."),
        ]),
        dict(kop="De strijd tegen de rassensegregatie", blokken=[
            ("p", "De <strong>Jim Crow-wetten</strong> in de Verenigde Staten waren <strong>wetten die "
                  "zwarte en witte Amerikanen in het openbare leven van elkaar scheidden</strong>: aparte "
                  "scholen, aparte wachtzalen, aparte plaatsen op de bus."),
            ("p", "<strong>Rosa Parks</strong> werd in 1955 in Montgomery gearresteerd omdat <strong>ze "
                  "weigerde haar zitplaats op de bus aan een witte reiziger af te staan</strong>. Daarna "
                  "volgde een busboycot van meer dan een jaar, geleid door <strong>Martin Luther "
                  "King</strong>, die staat <strong>voor geweldloos verzet en voor gelijke rechten voor alle "
                  "Amerikanen</strong>. Zijn beroemdste zin begint met <strong>I have a dream</strong>, bij "
                  "de mars op Washington in 1963. Hij werd in 1968 vermoord."),
            ("p", "De <strong>resultaten</strong> van de burgerrechtenbeweging: <strong>de Civil Rights "
                  "Act, die discriminatie in het openbare leven verbood</strong>, <strong>de Voting Rights "
                  "Act, die het stemrecht van zwarte kiezers beschermde</strong>, en <strong>het einde van "
                  "de wettelijke scheiding in scholen en openbare plaatsen</strong>. <strong>Niet alle "
                  "leiders kozen voor geweldloos verzet</strong>: Malcolm X en de Black Panthers sloten "
                  "gewapende zelfverdediging niet uit."),
            ("p", "<strong>Black Lives Matter</strong> staat <strong>tegen politiegeweld en racisme "
                  "tegenover zwarte mensen</strong>. De beweging ontstond in 2013 en groeide in 2020 "
                  "wereldwijd uit, ook in Belgische steden."),
        ]),
        dict(kop="Jongerencultuur en protest", blokken=[
            ("p", "Vanaf de jaren vijftig ontstond een aparte jongerencultuur omdat <strong>jongeren langer "
                  "studeerden, zelf verdienden en zo een eigen groep met eigen smaak vormden</strong>. De "
                  "<strong>rock-'n-roll</strong> werd het geluid daarvan."),
            ("p", "<strong>De jongerencultuur van de jaren zestig ging niet alleen over muziek en "
                  "kleding</strong>: ze had wel degelijk een politieke kant. In mei 1968 protesteerden "
                  "studenten in Parijs en elders <strong>tegen het gezag van de oude orde, op de "
                  "universiteit en in de maatschappij</strong>. In België viel Leuven Vlaams in hetzelfde "
                  "jaar."),
            ("p", "<strong>Actuele protestbewegingen</strong>: <strong>de klimaatmarsen van "
                  "jongeren</strong>, <strong>de beweging Black Lives Matter</strong> en <strong>de "
                  "MeToo-beweging tegen grensoverschrijdend gedrag</strong>. <strong>Sociale media spelen "
                  "daarbij een grote rol in het mobiliseren van mensen.</strong> Het verschil met een "
                  "partij: <strong>een beweging voert actie rond een thema, een partij komt op bij "
                  "verkiezingen</strong>."),
        ]),
        dict(kop="De popart, en hoe je ze van andere stromingen onderscheidt", blokken=[
            ("p", "De kunststroming <strong>popart</strong> ontstond in de jaren vijftig en zestig en <strong>haalde haar "
                  "beelden uit reclame, strips en supermarkt</strong>. Pop staat voor popular. Haar "
                  "<strong>kenmerken</strong>: <strong>beelden uit de reclame en de massaproductie</strong>, "
                  "<strong>felle, vlakke kleuren en veel herhaling</strong>, en <strong>de grens tussen hoge "
                  "en lage cultuur vervaagt</strong>. <strong>De popart kijkt met een zekere ironie naar de "
                  "consumptiemaatschappij.</strong>"),
            ("p", "<strong>Warhol</strong> maakte de reeks met de soepblikken van Campbell en gebruikte de techniek van "
                  "<strong>de zeefdruk</strong> om hetzelfde beeld in reeksen te herhalen. Een werk van "
                  "<strong>Roy Lichtenstein</strong> herken je <strong>aan de vergrote stripbeelden met de "
                  "zichtbare drukstippen</strong>. De kunstenaar <strong>Claes Oldenburg</strong> maakte reusachtige "
                  "beelden van alledaagse voorwerpen zoals een wasknijper of een lepel."),
            ("p", "De <strong>band met de tijd</strong>: <strong>de naoorlogse welvaart bracht reclame, "
                  "merken en massaproductie in elk huis</strong>. Zonder supermarkt, televisiereclame en "
                  "filmsterren bestaat de popart niet."),
            ("p", tabel(["Stroming", "Waaraan je ze herkent"], [
                ["Cobra", "ontstond in 1948 in Kopenhagen, Brussel en Amsterdam; spontane, bijna kinderlijke beelden"],
                ["Minimal art", "enkel eenvoudige geometrische vormen, in serie"],
                ["Optical art", "vormen en kleuren die het oog laten denken dat er beweging in het vlak zit"],
                ["Land art", "het werk wordt rechtstreeks in een landschap in de natuur gemaakt"],
                ["Conceptuele kunst", "het idee achter het werk telt meer dan het voorwerp dat je ziet"],
                ["Postmodernisme", "stijlen uit verschillende tijden worden door elkaar gebruikt en geciteerd"],
            ])),
            ("p", "<strong>De emancipatiebewegingen en de kunst van de jaren zestig staan niet los van "
                  "elkaar.</strong> Dezelfde jaren, dezelfde beweging: jongeren, vrouwen en minderheden "
                  "eisten een plaats op, en de kunst brak tegelijk met wat hoort en niet hoort."),
        ]),
    ],
    onthoud=[
        "Emancipatie: een groep verwerft gelijke rechten en maakt zich los uit een ondergeschikte positie.",
        "Vrouwen kregen in 1948 stemrecht voor de nationale verkiezingen.",
        "Het glazen plafond is een onzichtbare grens die vrouwen van de hoogste functies weghoudt.",
        "België opende in 2003 als tweede land ter wereld het huwelijk voor koppels van hetzelfde geslacht.",
        "Rosa Parks weigerde in 1955 haar zitplaats op de bus aan een witte reiziger af te staan.",
        "Martin Luther King staat voor geweldloos verzet en gelijke rechten voor alle Amerikanen.",
        "Een beweging voert actie rond een thema, een partij komt op bij verkiezingen.",
        "Popart haalt haar beelden uit reclame, strips en supermarkt, met felle, vlakke kleuren.",
        "Warhol gebruikte de zeefdruk, Lichtenstein vergrote stripbeelden met zichtbare drukstippen.",
    ],
)

# ───────────────────────── 12. Redeneren met historische bronnen
BUNDELS["redeneren-met-historische-bronnen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Redeneren met historische bronnen",
    onder="Een onderzoekbare vraag stellen, en het stappenplan van de bronnenanalyse uitvoeren.",
    secties=[
        dict(kop="De historische vraag", blokken=[
            ("p", "Dit onderdeel weegt een vijfde van je examen. Het is geen leerstof die je van buiten "
                  "leert maar een <strong>werkwijze</strong>. Ze begint bij een <strong>onderzoekbare "
                  "historische vraag</strong>, een vraag die onderzoekbaar is. Die moet <strong>afgebakend zijn in de tijd</strong>, "
                  "<strong>afgebakend in de ruimte</strong>, en er moeten <strong>bronnen bestaan om ze te "
                  "beantwoorden</strong>. Een vraag die <strong>met ja of nee</strong> af te doen valt, "
                  "levert geen onderzoek op."),
            ("p", "Je kan ook afbakenen binnen de <strong>maatschappelijke domeinen</strong>: <strong>het "
                  "politieke en het sociale domein</strong>, <strong>het economische domein</strong> en "
                  "<strong>het culturele domein</strong>. Wat de onderzoeker zelf leuk vindt, is geen "
                  "domein."),
            ("kader", "Vergelijk: <em>Hoe veranderde het werk van vrouwen in de Gentse textielfabrieken "
                      "tussen 1880 en 1900?</em> heeft een tijd, een plaats, een groep en een domein. "
                      "<em>Hoe was het leven van de mensen vroeger in de hele wereld?</em> heeft geen van "
                      "die vier."),
        ]),
        dict(kop="Stap 1: de context van elke bron", blokken=[
            ("p", "<strong>Het eerste wat je bij een bronnenanalyse doet, is informatie verzamelen over de "
                  "context van de bron.</strong> Je situeert haar in de drie vensters van het <strong>historisch "
                  "referentiekader</strong>: in de tijd, in de ruimte en in de maatschappelijke "
                  "<strong>domeinen</strong>."),
            ("p", "Dan bepaal je de <strong>soort</strong>. Een <strong>primaire bron</strong> is <strong>een "
                  "bron die uit de onderzochte periode zelf stamt</strong>; een handboek geschiedenis uit "
                  "2015 over de Russische revolutie is een <strong>geschreven secundaire bron</strong>. "
                  "<strong>Een secundaire bron is daarom niet minder waard dan een primaire bron</strong>: "
                  "primair en secundair zeggen iets over de afstand in tijd, niet over de kwaliteit. En "
                  "<strong>of een bron primair of secundair is, hangt mee af van de vraag die je "
                  "stelt</strong>: een schoolboek uit 1950 is primair voor een onderzoek naar wat men in "
                  "1950 aan kinderen leerde."),
            ("p", "Naar <strong>vorm</strong> onderscheid je <strong>geschreven bronnen zoals brieven en "
                  "kranten</strong>, <strong>materiële bronnen zoals gebouwen en gereedschap</strong>, "
                  "<strong>audiovisuele bronnen zoals foto's en filmbeelden</strong>, en mondelinge bronnen. "
                  "Munten uit de zestiende eeuw die een archeoloog bij een opgraving vindt, zijn dus <strong>een materiële "
                  "primaire bron</strong>."),
            ("p", "Je <strong>contextualiseert de maker</strong> (de maker contextualiseren): <strong>zijn naam, beroep en "
                  "afkomst</strong>, <strong>zijn maatschappelijke positie en zijn perspectief</strong>, en "
                  "<strong>of hij ooggetuige of tijdgenoot was</strong>. De <strong>opdrachtgever</strong> "
                  "is <strong>degene die de bron liet maken en er dus een bedoeling mee had</strong>. Van "
                  "elke bron bepaal je ook het <strong>doelpubliek</strong> (voor wie), de inhoud (wat), de "
                  "<strong>bedoeling</strong> (waarom) en de <strong>mate van bewerking</strong>: "
                  "<strong>hoeveel er aan de bron veranderd is voor ze bij jou terechtkwam</strong>."),
            ("p", "Ontbreken er gegevens, dan <strong>noteer je dat die contextgegevens ontbreken en hou je "
                  "daar rekening mee</strong>. Een gat benoemen is iets anders dan het met een gok opvullen."),
        ]),
        dict(kop="Standplaatsgebondenheid", blokken=[
            ("p", "<strong>Standplaatsgebondenheid</strong> betekent dat <strong>de maker van een bron "
                  "kijkt vanuit zijn eigen positie, tijd en belangen</strong>. Een officier en een gewone "
                  "soldaat zien dezelfde slag anders, niet omdat een van beiden liegt."),
            ("p", "Daarom geeft <strong>een ooggetuige niet altijd een objectief verslag</strong>: hij ziet "
                  "maar een stuk, hij heeft belangen, en zijn geheugen schuift."),
            ("p", "Neem een <strong>wervingsaffiche van een regering uit 1915</strong>, een affiche die jonge mannen oproept om "
                  "dienst te nemen. Het <strong>doelpubliek</strong> zijn <strong>jonge mannen die nog niet "
                  "in het leger zitten</strong>, niet wij die ze vandaag lezen. De <strong>bedoeling</strong> "
                  "is <strong>mensen overtuigen en tot handelen aanzetten</strong>. En <strong>een bron die "
                  "propaganda is, is daarom niet onbruikbaar</strong>: ze is een slechte bron over wat er "
                  "écht gebeurde en een uitstekende over wat men wilde laten geloven."),
        ]),
        dict(kop="Stap 3: bruikbaar, betrouwbaar, representatief", blokken=[
            ("p", "Na stap 2, het lezen of bekijken van de inhoud, volgt het interpreteren en beoordelen. "
                  "<strong>Je kan de inhoud van een bron niet goed beoordelen zonder iets over de maker te "
                  "weten</strong>, en daarom komt de context eerst."),
            ("p", tabel(["Criterium", "Wat je beoordeelt", "Richtvragen"], [
                ["Bruikbaarheid", "of de bron een antwoord geeft op jóúw historische vraag",
                 "geeft ze rechtstreekse informatie? onrechtstreekse? een volledig, gedeeltelijk of geen antwoord?"],
                ["Betrouwbaarheid", "of je op de inhoud kan afgaan",
                 "had de maker er belang bij? schreef hij pas jaren later? spreekt de bron andere bronnen tegen?"],
                ["Representativiteit", "of de bron het standpunt van één mens of van een hele groep weergeeft",
                 "zijn er bronnen die op een ander standpunt wijzen?"],
                ["Presentatie", "de manier waarop de bron aan jou getoond wordt, met of zonder bewerking",
                 "vertaald, ingekort, bijgesneden? met welk doel?"],
            ])),
            ("p", "Welke elementen de <strong>betrouwbaarheid versterken</strong>: <strong>andere, onafhankelijke "
                  "bronnen vertellen hetzelfde</strong>. Dat heet bronnen <strong>kruisen</strong>. Een "
                  "bron in een <strong>vreemde taal</strong> is daarom niet minder betrouwbaar, en "
                  "<strong>een bron die kort na de gebeurtenis gemaakt werd, is niet automatisch "
                  "betrouwbaar</strong>: een krant van de dag zelf kan vol geruchten zitten."),
            ("p", "Bij <strong>representativiteit</strong>: heb je voor de vraag hoe arbeiders in 1890 over "
                  "hun werk dachten maar <strong>één brief van één arbeider</strong>, dan is het probleem "
                  "dat <strong>één brief niet representatief is voor een hele bevolkingsgroep</strong>. De "
                  "brief blijft waardevol, hij toont alleen niet dat iedereen er zo over dacht. Hou er ook "
                  "rekening mee dat <strong>van arme en ongeletterde groepen veel minder geschreven bronnen "
                  "bewaard zijn dan van rijke en machtige groepen</strong>."),
            ("p", "Bij <strong>presentatie</strong>: wordt een foto van een betoging <strong>zo bijgesneden "
                  "dat enkel de drukste hoek te zien is</strong>, dan <strong>lijkt de betoging veel groter "
                  "dan ze in werkelijkheid was</strong>. Er is niets vervalst en toch klopt het beeld niet "
                  "meer. <strong>Een bron vertalen of inkorten kan de betekenis ervan verschuiven.</strong>"),
            ("p", "Tot slot het <strong>beoogde effect</strong>: <strong>wat de maker bij zijn publiek "
                  "wilde teweegbrengen</strong>. Toont een schilderij een veldslag met de eigen vorst "
                  "heldhaftig in het midden, dan besluit je dat <strong>de bron vooral iets zegt over hoe de "
                  "vorst gezien wilde worden</strong>."),
        ]),
        dict(kop="Bronnen vergelijken en antwoorden", blokken=[
            ("p", "Je <strong>vergelijkt bronnen om gelijkenissen en verschillen te vinden en zo tot een "
                  "beter antwoord te komen</strong>. Spreken twee bronnen over dezelfde staking elkaar "
                  "tegen, dan <strong>onderzoek je de standplaats en de bedoeling van elke maker</strong>. "
                  "Een tegenspraak is geen probleem maar een aanwijzing."),
            ("p", "<strong>Een historische vraag beantwoord je niet het best met bronnen uit één enkele "
                  "hoek.</strong> Hoe meer verschillende hoeken, hoe vollediger je beeld; een verhaal dat "
                  "nergens wringt, heeft meestal bronnen weggelaten."),
            ("p", "Het <strong>stappenplan</strong> in volgorde: <strong>de context van elke bron "
                  "verzamelen</strong>, <strong>de inhoud van elke bron lezen of bekijken</strong>, "
                  "<strong>elke bron interpreteren en beoordelen</strong>, en als laatste stap <strong>de "
                  "informatie uit de bronnen samenbrengen met je historische kennis</strong>. Zelf een bron "
                  "maken hoort bij geen enkele stap."),
        ]),
    ],
    onthoud=[
        "Een onderzoekbare vraag is afgebakend in tijd en ruimte, en er bestaan bronnen voor.",
        "Bij een bronnenanalyse verzamel je eerst informatie over de context van de bron.",
        "Primair en secundair zeggen iets over de afstand in tijd, niet over de kwaliteit.",
        "Ontbreken er contextgegevens, dan noteer je dat en hou je er rekening mee.",
        "Standplaatsgebondenheid: de maker kijkt vanuit zijn eigen positie, tijd en belangen.",
        "Een bron die propaganda is, is daarom niet onbruikbaar.",
        "Je beoordeelt bruikbaarheid, betrouwbaarheid, representativiteit en presentatie.",
        "Onafhankelijke bronnen die hetzelfde vertellen, versterken de betrouwbaarheid: dat heet kruisen.",
        "Stappenplan: context, inhoud, interpreteren en beoordelen, samenbrengen met je kennis.",
    ],
)

# ───────────────────────── 13. Beeldvorming, vergelijken en verleden-heden-toekomst
BUNDELS["beeldvorming-vergelijken-en-verleden-heden-toekomst-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Beeldvorming, vergelijken en verleden-heden-toekomst",
    onder="De twaalf redeneerwijzen, het vergelijken van samenlevingen, en wat het verleden vandaag betekent.",
    secties=[
        dict(kop="Historische beeldvorming", blokken=[
            ("p", "<strong>Historische beeldvorming</strong> is <strong>het beeld van het verleden dat "
                  "iemand opbouwt uit bronnen en interpretatie</strong>. Het verleden zelf ligt achter ons; "
                  "wat wij hebben, is een beeld dat iemand gemaakt heeft."),
            ("p", "<strong>Over dezelfde gebeurtenis kunnen meerdere historische beelden naast elkaar "
                  "bestaan</strong>, en <strong>twee historici die dezelfde bronnen gebruiken, komen niet "
                  "altijd tot precies hetzelfde beeld</strong>. Het beeld van een historische figuur "
                  "verandert <strong>omdat er nieuwe bronnen opduiken en de samenleving andere vragen "
                  "stelt</strong>. Leopold II in België is daar het duidelijkste voorbeeld van."),
            ("p", "De <strong>standplaatsgebondenheid van een historicus</strong> werkt zo: <strong>zijn "
                  "tijd, zijn afkomst en zijn overtuiging sturen welke vragen hij stelt</strong>. "
                  "<strong>Een historicus kan vanuit zijn eigen positie dus niet volledig neutraal naar het verleden kijken.</strong> "
                  "Hij kan wel eerlijk zijn over zijn vertrekpunt, zijn bronnen tonen en andere lezingen "
                  "bespreken. Ook de <strong>bewerking</strong> speelt mee: <strong>een bewerkte bron kan "
                  "een ander beeld oproepen dan het origineel</strong>, zeker wanneer er een hedendaags "
                  "waarden- en normenkader bij meespeelt."),
            ("p", "<strong>Bewijs gebruiken</strong> betekent dat <strong>elke uitspraak over het verleden "
                  "op bronnen moet kunnen steunen</strong>. Zonder bron is het een mening."),
        ]),
        dict(kop="De historische redeneerwijzen", blokken=[
            ("p", "De fiche somt er twaalf op: <strong>oorzaak en gevolg benoemen</strong>, bedoelde en "
                  "onbedoelde gevolgen onderscheiden, <strong>meerdere perspectieven hanteren</strong>, "
                  "<strong>continuïteit en verandering benoemen</strong>, evolutie en revolutie benoemen, "
                  "bewijs gebruiken, actualiseren, verbanden leggen, historisch contextualiseren, menselijke "
                  "actoren benoemen, veralgemening analyseren en stereotypering analyseren."),
            ("p", tabel(["Redeneerwijze", "Wat ze inhoudt"], [
                ["Bedoeld tegenover onbedoeld gevolg",
                 "een bedoeld gevolg is wat de betrokkene wilde bereiken, een onbedoeld gevolg niet"],
                ["Continuïteit", "iets blijft over een lange periode in grote lijnen hetzelfde"],
                ["Evolutie tegenover revolutie",
                 "een evolutie verloopt geleidelijk, een revolutie is een plotse en diepe omslag"],
                ["Actualiseren",
                 "een verband leggen tussen een gebeurtenis uit het verleden en de wereld van vandaag"],
                ["Historisch contextualiseren",
                 "een gebeurtenis begrijpen vanuit de tijd en de omstandigheden waarin ze plaatsvond"],
                ["Agency of menselijke actoren",
                 "mensen maken zelf keuzes en bepalen mee hoe de geschiedenis loopt"],
            ])),
            ("p", "Het Marshallplan wilde Europa heropbouwen; dat het Europa ook stevig in het westerse "
                  "kamp vastzette, is een <strong>onbedoeld gevolg</strong>. Rosa Parks die blijft zitten, "
                  "is <strong>agency</strong>. En let op bij <strong>actualiseren</strong>: het verleden "
                  "<em>beoordelen</em> met de maatstaf van vandaag is net de valkuil, niet de redeneerwijze. "
                  "Begrijpen is iets anders dan goedpraten."),
            ("p", "<strong>Meerdere perspectieven hanteren</strong> is nuttig <strong>omdat elke betrokken "
                  "groep de gebeurtenis anders beleefde en anders vertelt</strong>. De kolonisator, de "
                  "gekoloniseerde en de missionaris vertellen drie verhalen over dezelfde kolonie."),
        ]),
        dict(kop="Veralgemening en stereotypering", blokken=[
            ("p", "<strong>Een veralgemening is een uitspraak die van enkele gevallen een regel voor een "
                  "hele groep maakt.</strong> Een <strong>stereotypering</strong> is <strong>een vast en "
                  "vereenvoudigd beeld dat men aan een hele groep mensen toeschrijft</strong>."),
            ("p", "Beschrijft een schoolboek uit de jaren zestig de lokale bevolking van een kolonie als "
                  "onwetend en lui, dan <strong>analyseer je die zin als stereotypering en vraag je wat ze "
                  "over de maker zegt</strong>. De zin is een slechte bron over de kolonie en een "
                  "uitstekende bron over hoe men in België in de jaren zestig over die kolonie dacht."),
        ]),
        dict(kop="Samenlevingen vergelijken", blokken=[
            ("p", "Je vergelijkt samenlevingen uit verschillende periodes <strong>om gelijkenissen en "
                  "verschillen te zien en zo elke samenleving beter te begrijpen</strong>, niet om er een "
                  "rangorde van te maken. Je vergelijkt zowel <strong>binnen eenzelfde periode</strong> als "
                  "<strong>tussen periodes</strong>, van de prehistorie tot de hedendaagse tijd."),
            ("p", tabel(["Groep kenmerken", "Vergelijkingspunten"], [
                ["Politiek", "imperialisme en neokolonialisme, de staatsvorm (democratie of dictatuur), de verhouding tussen bestuurders en bestuurden"],
                ["Sociaal", "migratie en wij-zij-denken, slavernij en onvrije arbeid, de gelaagdheid van de samenleving"],
                ["Cultureel", "kunstuitingen, levensbeschouwing, de multiculturele samenleving, propaganda"],
                ["Economisch", "industrialisering en arbeidsorganisatie, handel en handelsnetwerken, het economisch systeem"],
            ])),
            ("p", "Twee voorbeelden die de fiche zelf noemt. Het <strong>verschil tussen het imperialisme "
                  "van de vroegmoderne tijd en dat van de negentiende eeuw</strong>: <strong>in de "
                  "negentiende eeuw werd het binnenland bezet en bestuurd, eerder vooral de kust</strong>. "
                  "De motieven leken op elkaar, de middelen verschilden enorm. En de "
                  "<strong>staatsvorm onder Mao vergeleken met China vandaag</strong>: <strong>in beide "
                  "gevallen is er één partij aan de macht, maar de economie verschilt grondig</strong>, "
                  "politieke continuïteit naast economische verandering."),
            ("p", "<strong>Slavernij komt in meerdere historische periodes voor, telkens in een andere "
                  "vorm</strong>, en <strong>in eenzelfde periode waren de samenlevingen over de hele wereld "
                  "niet op dezelfde manier georganiseerd</strong>: in de negentiende eeuw bestonden een "
                  "industrieel Engeland, een keizerlijk China en koloniale samenlevingen náást elkaar."),
        ]),
        dict(kop="Collectieve herinnering", blokken=[
            ("p", "Een <strong>collectieve herinnering</strong> is <strong>het gedeelde beeld dat een groep "
                  "van een gebeurtenis bewaart en doorgeeft</strong>. Je herkent er een aan dat <strong>er "
                  "jaarlijks op een vaste dag bij stilgestaan wordt</strong>, dat <strong>er monumenten of "
                  "gedenkplaten voor in de openbare ruimte staan</strong>, en dat <strong>een hele groep er "
                  "een gevoel en een betekenis over deelt</strong>. Het aantal bronnen zegt daar niets over."),
            ("p", "<strong>De manier waarop men de Holocaust herdenkt, is sinds 1945 niet dezelfde "
                  "gebleven.</strong> Vlak na de oorlog sprak men vooral over de oorlog in het algemeen; "
                  "pas vanaf de jaren zestig en zeventig kwam de genocide op de Joden centraal te staan. "
                  "Dat kwam doordat <strong>overlevenden begonnen te spreken, er onderzoek kwam, en de "
                  "samenleving andere vragen stelde</strong>. Vandaag is 27 januari de internationale "
                  "herdenkingsdag."),
            ("p", "Nu de laatste ooggetuigen wegvallen, blijft herdenken belangrijk omdat <strong>onderwijs "
                  "en bronnen de herinnering dan moeten overnemen</strong>. En <strong>de betekenis die men "
                  "aan een historische figuur geeft, kan van groep tot groep verschillen</strong>: voor de "
                  "ene een held, voor de andere een onderdrukker."),
        ]),
        dict(kop="De democratische rechtsstaat en jouw rol", blokken=[
            ("p", "Men spreekt van een <strong>rechtsstaat</strong> en niet enkel van een democratie "
                  "<strong>omdat ook een verkozen meerderheid zich aan de wet en de grondrechten moet "
                  "houden</strong>. Een meerderheid die alles zou mogen, kan een minderheid haar rechten "
                  "afnemen."),
            ("p", "Die rechtsstaat werkt op verschillende bestuursniveaus, <strong>van de gemeente over de deelstaten tot het federale niveau "
                  "en de Europese Unie</strong>: op elk van die niveaus stem je, worden er regels gemaakt en "
                  "kan je naar een rechter stappen."),
            ("p", "<strong>Beperkingen</strong> in de praktijk: <strong>niet iedereen wordt in de politiek "
                  "even goed vertegenwoordigd</strong>, <strong>wie geld of een netwerk heeft, krijgt soms "
                  "meer gehoor</strong>, en <strong>trage procedures laten problemen soms lang "
                  "aanslepen</strong>. Kritiek op de regering hoort daar niet bij; waar die niet mag, is er "
                  "geen rechtsstaat meer. <strong>Een democratie kan ook van binnenuit onder druk komen te "
                  "staan, zonder staatsgreep of oorlog</strong>, door de pers aan banden te leggen of "
                  "rechters onder druk te zetten."),
            ("p", "Zelf <strong>verantwoordelijkheid opnemen</strong> kan door <strong>te gaan stemmen, je "
                  "te informeren en je mening onderbouwd te verdedigen</strong>, en daarnaast door lid te "
                  "worden van een vereniging, een petitie te tekenen of naar een inspraakavond van je "
                  "gemeente te gaan."),
            ("kader", "Waarom je het verleden bestudeert als je over de toekomst nadenkt: <strong>omdat je "
                      "er processen in herkent die vandaag opnieuw aan het werk zijn</strong>. Voorspellen "
                      "kan geschiedenis niet. Herkennen wel: hoe propaganda werkt, hoe een crisis een "
                      "samenleving splijt, hoe rechten verworven en verloren raken."),
        ]),
    ],
    onthoud=[
        "Historische beeldvorming is het beeld van het verleden opgebouwd uit bronnen en interpretatie.",
        "Een historicus kan niet volledig neutraal naar het verleden kijken.",
        "Bewijs gebruiken: elke uitspraak over het verleden moet op bronnen kunnen steunen.",
        "Een bedoeld gevolg is wat de betrokkene wilde bereiken, een onbedoeld gevolg niet.",
        "Actualiseren is een verband leggen met vandaag, niet het verleden beoordelen met de maatstaf van nu.",
        "Een stereotypering is een vast en vereenvoudigd beeld van een hele groep mensen.",
        "Je vergelijkt samenlevingen om ze beter te begrijpen, niet om er een rangorde van te maken.",
        "Een collectieve herinnering is het gedeelde beeld dat een groep bewaart en doorgeeft.",
        "In een rechtsstaat moet ook een verkozen meerderheid zich aan de wet en de grondrechten houden.",
    ],
)

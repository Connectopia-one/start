"""Restauratie, revolutie en het ontstaan van België — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="europa-1815.webp", zelf=False,
         wat="Kaart van Europa na het Congres van Wenen (1815), met het Verenigd Koninkrijk der Nederlanden, Pruisen met het Rijnland en de Duitse Bond duidelijk te zien. Liefst zonder namen in de landen, of met letters A, B, C erop.",
         waar="Wikimedia Commons, zoek 'Europe 1815 map' (veel kaarten in het publieke domein).",
         vragen="kaartvraag over de bufferstaten"),
    dict(bestand="septemberdagen-1830.webp", zelf=False,
         wat="Het schilderij 'Episode uit de Septemberdagen 1830' van Gustaf Wappers (1834-1835), in het publieke domein.",
         waar="Wikimedia Commons, zoek 'Wappers Septemberdagen'.",
         vragen="casus over het schilderij als bron"),
]

VRAGEN = [
    # --- Wenen
    tabel(
        "Welke beslissingen van het Congres van Wenen dienden om Frankrijk in te dijken?",
        [
            ("Rond Frankrijk kwamen bufferstaten die een nieuwe Franse aanval moesten opvangen.", J),
            ("Pruisen kreeg het Rijnland erbij, aan de grens met Frankrijk.", J),
            ("De Duitse staten werden samengebracht in één sterk keizerrijk.", F),
            ("Frankrijk kreeg alle gebieden van Napoleon terug.", F),
        ],
        "Bufferstaten rond Frankrijk, met Pruisen aan de Rijn. De Duitse staten werden niet tot één rijk samengevoegd.",
    ),
    klik(
        "Bekijk de kaart van Europa in 1815. Klik op de bufferstaat die het Congres van Wenen ten noorden van Frankrijk oprichtte.",
        "europa-1815.webp",
        [[29.5, 33, 8, 20]],
        "Gebied A: het Verenigd Koninkrijk der Nederlanden, Noord en Zuid samen onder Willem I. B is Pruisen met het Rijnland, C de grens van de Duitse Bond.",
    ),
    mk(
        "Wat bedoelden de vorsten in Wenen met het beginsel van de legitimiteit?",
        [
            "Dat de oude dynastieën het rechtmatige gezag hebben",
            "Dat elk volk zelf en vrij zijn eigen regering mag kiezen",
            "Dat grenzen de taal en de wensen van de bevolking volgen",
            "Dat een geschreven grondwet boven elke vorst moet staan",
        ],
        0,
        "Legitimiteit betekende: terug naar de vorstenhuizen van voor 1789. De andere drie zijn net wat liberalen en nationalisten vroegen.",
    ),
    mk(
        "In welke mate bereikte het Congres van Wenen zijn doelstellingen? Kies de best onderbouwde beoordeling.",
        [
            "Deels: er kwam decennialang geen grote oorlog, maar de revoluties van 1830 en 1848 toonden dat de oude orde niet te herstellen was",
            "Volledig: na 1815 kwam er in heel Europa geen enkele opstand of revolutie meer, want de vorsten hielden alles stevig in handen",
            "Helemaal niet: kort na 1815 voerden de grote mogendheden alweer een grote oorlog tegen elkaar, waardoor alle afspraken vervielen",
            "Volledig: de grenzen die in 1815 getekend werden, zijn tot vandaag onveranderd gebleven, ook die van de Nederlanden",
        ],
        0,
        "Het evenwicht hield lang stand, maar liberale en nationale bewegingen lieten zich niet onderdrukken. Dat zie je aan de revolutiegolven en aan het ontstaan van België in 1830.",
    ),
    sleep(
        "Men wilde na Napoleon de toestand van voor 1789 herstellen: dat heet [[restauratie]]. Omdat de vorsten bij de grenzen geen rekening hielden met de [[taal]] en de wensen van de bevolking, volgden er revolutiegolven in 1830 en 1848.",
        ["revolutie", "godsdienst"],
        "Restauratie is herstel. Het negeren van taal en wensen van de bevolking verklaart veel van de opstanden die volgden.",
    ),
    # --- liberalisme en nationalisme
    sorteer(
        "Verbindend of ontbindend nationalisme?",
        ["Verbindend", "Ontbindend"],
        [
            ["De eenmaking van Italië", "Verbindend"],
            ["De Belgische afscheiding van Nederland", "Ontbindend"],
            ["De Griekse opstand tegen het Ottomaanse Rijk", "Ontbindend"],
            ["De eenmaking van Duitsland", "Verbindend"],
            ["De Poolse opstand tegen Rusland", "Ontbindend"],
        ],
        "Verbindend nationalisme brengt losse staten van hetzelfde volk samen. Ontbindend nationalisme maakt zich los uit een groter geheel.",
    ),
    tabel(
        "Een liberaal uit de burgerij schrijft rond 1825 zijn wensen op. Welke punten passen in zijn lijstje?",
        [
            ("Een grondwet die de macht van de vorst beperkt", J),
            ("Vrijheid van drukpers, vereniging en godsdienst", J),
            ("Een overheid die de economie sterk stuurt", F),
            ("Stemrecht voor iedereen, ook voor wie geen belasting betaalt", F),
        ],
        "De liberalen kwamen vooral uit de burgerij. Ze wilden zo weinig mogelijk staatsbemoeienis met de economie, en ze verdedigden het cijnskiesrecht.",
    ),
    mk(
        "Waarom gingen liberalisme en nationalisme in de 19de eeuw vaak samen?",
        [
            "Allebei keerden ze zich tegen vorsten die zonder grondwet en zonder het volk regeerden",
            "Allebei wilden ze de vorstenhuizen van voor 1789 weer stevig en voorgoed aan de macht brengen",
            "Allebei werden ze krachtig gesteund door Metternich en het Congres van Wenen",
            "Allebei wilden ze dat de staat alle fabrieken en banken in handen nam",
        ],
        0,
        "Ze hadden dezelfde tegenstander: de orde van Wenen met vorsten die regeerden zonder grondwet of inspraak.",
    ),
    # --- Willem I
    sorteer(
        "Welke grief van het Zuiden tegen Willem I hoort in welk domein?",
        ["Politiek", "Economisch", "Cultureel"],
        [
            ["Te weinig zetels voor het aantal inwoners", "Politiek"],
            ["Het Noorden wilde vrijhandel, het Zuiden bescherming van zijn industrie", "Economisch"],
            ["Het Nederlands werd opgelegd als bestuurstaal", "Cultureel"],
            ["De koning bemoeide zich met de opleiding van priesters", "Cultureel"],
        ],
        "Zetels zijn politiek, handel is economisch. Taal en godsdienst horen bij het culturele domein.",
    ),
    mk(
        "In 1828 sloten katholieken en liberalen de unie der oppositie. Waarom is dat opvallend?",
        [
            "Ze waren normaal tegenstanders, maar hadden een gemeenschappelijke vijand in Willem I",
            "Ze waren het over alles eens en werkten al eeuwenlang nauw samen in het Zuiden",
            "Ze wilden allebei dat het Zuiden zo snel mogelijk bij Frankrijk zou horen",
            "Ze werden allebei door koning Willem I zelf gesteund en betaald",
        ],
        0,
        "Katholieken en liberalen verschilden sterk van mening, maar de grieven tegen Willem I brachten hen samen. Dat samengaan bleef ook na 1830 bestaan.",
    ),
    # --- revolutie
    volgorde(
        "Zet de fases van de Belgische revolutie in de juiste volgorde.",
        ["De opvoering van De Stomme van Portici", "De septemberdagen", "Het Voorlopig Bewind neemt het bestuur over", "De onafhankelijkheid wordt uitgeroepen", "De grondwet wordt afgekondigd"],
        "25 augustus 1830 de opera, dan de septemberdagen, het Voorlopig Bewind, op 4 oktober de onafhankelijkheid, en in 1831 de grondwet van het Nationaal Congres.",
    ),
    keuze(
        "België werd in 1831 een [[*constitutionele parlementaire monarchie|absolute monarchie|republiek]]: een koning, maar met een grondwet boven hem en een parlement [[*naast|onder|boven]] hem.",
        "Een constitutionele monarchie heeft een grondwet die de macht van de koning beperkt. Het parlement maakt de wetten.",
    ),
    tabel(
        "Een leerling zegt: \"België was in 1831 al een democratie.\" Welke gegevens spreken dat tegen?",
        [
            ("Alleen wie genoeg belasting betaalde, mocht stemmen.", J),
            ("Bij de eerste verkiezingen stemden maar enkele procenten van de bevolking.", J),
            ("De grondwet schreef de vrijheid van drukpers in.", F),
            ("De grondwet schreef de vrijheid van vereniging in.", F),
        ],
        "De vrijheden waren modern voor die tijd. Maar door het cijnskiesrecht mocht maar een kleine groep stemmen: modern, nog niet democratisch.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Stemrecht enkel voor wie genoeg belasting betaalt", "Cijnskiesrecht"],
            ["Katholieken en liberalen besturen samen na 1830", "Unionisme"],
            ["Een groep met een gedeelde taal, cultuur en geschiedenis wil een eigen staat", "Nationalisme"],
        ],
        ["Legitimiteit", "Restauratie"],
        "Drie begrippen uit dit thema. Legitimiteit en restauratie horen bij het Congres van Wenen.",
    ),
    casus(
        "Bekijk het schilderij. Gustaf Wappers schilderde het in 1834 en 1835 in opdracht van de Belgische staat. Het toont burgers, arbeiders en een vrouw met de Belgische vlag op de barricaden in Brussel in september 1830. De opstandelingen staan in het licht en kijken vastberaden.",
        [
            met_prent("septemberdagen-1830.webp", mk(
                "Wat is dit schilderij voor iemand die de septemberdagen onderzoekt?",
                ["Een primaire bron, want het komt uit de tijd zelf", "Een secundaire bron, want het werd pas na 1900 geschilderd", "Een materiële bron, want het is een beeld uit steen", "Een mondelinge bron, want het vertelt een verhaal"],
                0,
                "Het werd een paar jaar na de feiten gemaakt, door een tijdgenoot. Voor een onderzoek naar 1830 is het dus een primaire, audiovisuele bron.",
            ), volgt=True),
            mk(
                "Wat wilde de opdrachtgever wellicht met dit schilderij bereiken?",
                [
                    "De jonge staat een heldhaftig verhaal over zijn ontstaan geven",
                    "Koning Willem I bedanken voor zijn jarenlange bestuur van het Zuiden",
                    "Tonen dat de revolutie vooral van boeren op het platteland kwam",
                    "Een neutraal en volledig verslag geven van wat er precies gebeurde",
                ],
                0,
                "De Belgische staat bestelde het werk. Licht, vlag en vastberaden gezichten maken van de opstand een heldendaad: het zegt vooral iets over hoe België gezien wilde worden.",
            ),
            tabel(
                "Mag je op basis van dit schilderij deze besluiten trekken?",
                [
                    ("De nieuwe Belgische staat wilde de revolutie als een heldendaad herinneren.", "Mag"),
                    ("Elke inwoner van het Zuiden steunde de opstand.", "Mag niet"),
                    ("Het schilderij toont precies hoe de gevechten verliepen.", "Mag niet"),
                ],
                "Het schilderij is een uitstekende bron over de beeldvorming die de staat wilde. Over wat er echt gebeurde, of over wat iedereen dacht, zegt het veel minder.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- Vlaamse beweging
    tabel(
        "Welke uitspraken over taal in het jonge België kloppen?",
        [
            ("Het Frans was in heel het land de taal van bestuur en rechtbank, ook in Vlaanderen.", J),
            ("De Vlaamse beweging begon als een politieke partij.", F),
            ("Een historische roman uit 1838 gaf de beweging een verhaal.", J),
            ("De eerste taalwetten die het Nederlands erkenden, kwamen er meteen in 1831.", F),
        ],
        "De Vlaamse beweging was eerst cultureel, rond taal en letteren. De eerste taalwetten kwamen pas vanaf de jaren 1870, veertig jaar na de onafhankelijkheid.",
    ),
    mk(
        "Hoeveel jaar na de Belgische onafhankelijkheid kwamen de eerste taalwetten die het Nederlands erkenden ongeveer?",
        ["Ongeveer veertig jaar", "Ongeveer vier jaar", "Ongeveer honderd jaar", "Ongeveer tien jaar"],
        0,
        "Onafhankelijk in 1830, de eerste taalwetten vanaf de jaren 1870: zo'n veertig jaar later.",
    ),
    # --- Duitsland
    tabel(
        "Een leerling vat de Duitse eenmaking samen. Welke middelen van Pruisen noemt ze terecht?",
        [
            ("Oorlogen tegen Denemarken, Oostenrijk en Frankrijk", J),
            ("Een douane-unie die de staten economisch bond", J),
            ("Handige diplomatie tussen de mogendheden", J),
            ("Een volksraadpleging in alle Duitse staten", F),
        ],
        "Oorlog, economie en diplomatie. Een volksraadpleging hoorde er niet bij.",
    ),
    mk(
        "Waarom liet men het Duitse Keizerrijk in 1871 uitroepen in de Spiegelzaal van Versailles?",
        [
            "Om de overwinning in het hart van het verslagen Frankrijk te tonen",
            "Omdat Versailles in die jaren de hoofdstad van Pruisen was geworden",
            "Omdat het Congres van Wenen in 1815 ook al in die zaal had vergaderd",
            "Omdat er in Berlijn nog geen zaal groot genoeg was voor de vorsten",
        ],
        0,
        "Het was een vernedering voor Frankrijk. In 1919 werden de rollen omgedraaid: in dezelfde zaal moest Duitsland het Verdrag van Versailles tekenen.",
    ),
    mk(
        "Hoe veranderde de Duitse eenmaking de territoriale verhoudingen in Europa?",
        [
            "In het midden van Europa stond plots een grote industriële en militaire macht, en het evenwicht van Wenen was voorbij",
            "Er kwamen negenendertig nieuwe kleine Duitse staten bij, en Europa raakte daardoor nog meer verdeeld dan in 1815",
            "Duitsland werd een kleine, neutrale bufferstaat tussen Frankrijk en Rusland, zonder eigen leger of industrie",
            "Er veranderde niets aan de kaart, want de Duitse staten bleven gewoon in hetzelfde losse verband als na Wenen",
        ],
        0,
        "Uit een los verband van staten groeide één sterk rijk. Dat brak het evenwicht dat Wenen had opgebouwd.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["Het Congres van Wenen eindigt", "De unie der oppositie wordt gesloten", "België wordt onafhankelijk", "Het Duitse Keizerrijk wordt uitgeroepen", "Duitsland tekent het Verdrag van Versailles"],
        "1815, 1828, 1830, 1871 en 1919.",
    ),
    open_(
        "Leg uit hoe een beslissing van het Congres van Wenen op lange termijn bijdroeg tot het ontstaan van België.",
        "Wenen voegde Noord en Zuid samen in het Verenigd Koninkrijk der Nederlanden, zonder rekening te houden met de taal en de wensen van de bevolking. In het Zuiden groeiden grieven over taal, godsdienst, zetels en economie. Daardoor sloten katholieken en liberalen de unie der oppositie, en in 1830 volgde de revolutie.",
    ),
    mk(
        "Een historicus schrijft: \"De opera De Stomme van Portici was de oorzaak van de Belgische revolutie.\" Wat is de beste reactie?",
        [
            "De opera was de aanleiding; de oorzaken waren de opgestapelde grieven tegen Willem I",
            "Dat klopt: zonder die ene opera was er in 1830 nooit een revolutie gekomen in Brussel",
            "De opera was de oorzaak, en de grieven tegen Willem I waren slechts de aanleiding ervan",
            "De opera had er niets mee te maken, want de revolutie begon in Antwerpen en niet in Brussel",
        ],
        0,
        "Een aanleiding is de vonk, oorzaken zijn de opgestapelde spanningen. Hier waren dat de grieven over taal, godsdienst, zetels en economie.",
    ),
    keuze(
        "Na 1815 waren de Duitse staten verenigd in de [[*Duitse Bond|Triple Entente|Volkenbond]], een los verband van [[*negenendertig|zeven|twee]] zelfstandige staten.",
        "Wenen bracht ze niet samen in één rijk. Pas in 1871 kwam het Duitse Keizerrijk.",
    ),
    sleep(
        "Het Congres van Wenen werd geleid door de Oostenrijkse kanselier [[Metternich]]. De roman De Leeuw van Vlaanderen van [[Conscience]] gaf de Vlaamse beweging een verhaal. De Duitse eenmaking werd geleid door de Pruisische minister-president [[Bismarck]].",
        ["Napoleon", "Leopold I", "Willem I"],
        "Metternich leidde Wenen, Conscience schreef het boek van 1838 en Bismarck leidde de Duitse eenmaking. Napoleon was in 1815 al verslagen.",
    ),
    mk(
        "Waarom hadden de vorsten in Wenen weinig oog voor de wensen van de bevolking, en wat was daarvan een gevolg?",
        [
            "Ze dachten aan het evenwicht tussen de mogendheden; daardoor groeiden liberale en nationale bewegingen",
            "Ze lieten in elke streek een volksraadpleging houden; daardoor bleef het overal in Europa lange tijd rustig",
            "Ze wilden Frankrijk groter en sterker maken; daardoor kwam Napoleon kort nadien opnieuw aan de macht",
            "Ze volgden zorgvuldig de taalgrenzen; daardoor ontstonden er overal in Europa nieuwe, eentalige staten",
        ],
        0,
        "Wenen tekende grenzen voor het evenwicht en het herstel van de oude vorsten. De bevolking telde niet mee, en dat voedde later de opstanden.",
    ),
    mk(
        "Hoe reageerden de grote mogendheden op de revolutiegolven van 1830 en 1848?",
        [
            "Ze onderdrukten ze of probeerden ze in te dammen",
            "Ze steunden de opstandelingen met hun legers",
            "Ze lieten overal volksraadplegingen organiseren",
            "Ze ontbonden het Congres en tekenden nieuwe grenzen",
        ],
        0,
        "De mogendheden wilden de orde van Wenen bewaren en reageerden met onderdrukking of indammen.",
    ),
    keuze(
        "Het Congres van Wenen eindigde in hetzelfde jaar als [[*de slag bij Waterloo|de Belgische revolutie|de Franse Revolutie]]. Je situeert het congres in de eerste plaats in het [[*politieke|culturele|sociale]] domein.",
        "Waterloo en het einde van het congres vallen allebei in 1815. Een congres dat grenzen tekent, hoort bij het politieke domein.",
    ),
]

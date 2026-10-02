# -*- coding: utf-8 -*-
"""Modern imperialisme en de wedloop om Afrika.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: het modern
imperialisme vanaf ongeveer 1870, zijn oorzaken, de verdeling van Afrika onder
de Europese mogendheden, en de beeldvorming die daarbij hoorde.

Deel 1 gaat over wat imperialisme is en waarom het opkwam. Deel 2 gaat over de
wedloop zelf, de Conferentie van Berlijn en de gevolgen tot vandaag.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is imperialisme?",
        opties=[
            "een staat breidt zijn macht uit over andere gebieden en volken",
            "een staat sluit zijn grenzen voor alle vreemde handelaars",
            "een staat geeft zijn kolonies hun onafhankelijkheid terug",
            "een staat laat zijn inwoners naar een ander land verhuizen",
        ],
        antwoord=0,
        uitleg="Die macht kan militair, politiek of economisch zijn, en loopt vaak over alle drie samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is nieuw aan het modern imperialisme vanaf ongeveer 1870?",
        opties=[
            "hele gebieden werden bezet en door Europa zelf bestuurd",
            "Europese schepen bezochten voor het eerst andere werelddelen",
            "Europa dreef voor het eerst handel met Azië en met Afrika",
            "Europa stichtte enkel nog handelsposten aan de kusten",
        ],
        antwoord=0,
        uitleg="Vroeger ging het vooral om kustposten voor de handel. Nu werd het binnenland zelf ingenomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke economische oorzaken had het modern imperialisme?",
        opties=[
            "Europa had grondstoffen nodig voor zijn nieuwe nijverheden",
            "Europa zocht markten om zijn fabrieksgoederen te verkopen",
            "Europa had een tekort aan steenkool in zijn eigen bodem",
            "Europa wilde zijn eigen landbouwgrond aan Afrika verkopen",
        ],
        antwoord=[0, 1],
        uitleg="Rubber, palmolie, katoen en erts kwamen van ver. De afgewerkte goederen gingen dezelfde weg terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke politieke oorzaak had het modern imperialisme?",
        opties=[
            "een grote mogendheid wilde niet achterblijven bij haar rivalen",
            "een grote mogendheid wilde haar eigen leger kunnen afschaffen",
            "een grote mogendheid wilde haar grondwet in Afrika invoeren",
            "een grote mogendheid wilde haar kolonies aan Europa afgeven",
        ],
        antwoord=0,
        uitleg="Kolonies golden als bewijs van macht. Wie er geen had, telde in de ogen van de anderen minder mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde het superioriteitsdenken bij het imperialisme?",
        opties=[
            "Europeanen vonden hun eigen beschaving hoger en dus voorbeeldig",
            "Europeanen vonden alle volken van de wereld volkomen gelijk",
            "Europeanen vonden hun eigen godsdienst niet het verspreiden waard",
            "Europeanen vonden de talen van Afrika rijker dan hun eigen taal",
        ],
        antwoord=0,
        uitleg="Zo kon men de verovering voorstellen als een opdracht in plaats van als een roof.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de gedachte dat Europa de plicht had andere volken te beschaven?",
        antwoord=["beschavingsmissie", "de beschavingsmissie", "civilisatiemissie"],
        uitleg="Dat verhaal diende als rechtvaardiging. In de praktijk ging het om grondstoffen, macht en prestige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kolonie?",
        opties=[
            "een gebied dat door een vreemde staat bestuurd wordt",
            "een gebied dat met een vreemde staat handel drijft",
            "een gebied dat zijn eigen vorst en wetten behoudt",
            "een gebied dat door de Volkenbond bestuurd wordt",
        ],
        antwoord=0,
        uitleg="Het bestuur, de wetten en de belastingen kwamen van buiten, en de winst ging dezelfde weg uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een protectoraat?",
        opties=[
            "een gebied dat zijn eigen vorst houdt onder vreemd toezicht",
            "een gebied dat volledig door een vreemde staat bestuurd wordt",
            "een gebied dat door twee mogendheden samen bestuurd wordt",
            "een gebied dat zijn volledige onafhankelijkheid behouden heeft",
        ],
        antwoord=0,
        uitleg="Het inlandse bestuur bleef op papier overeind, maar de beslissingen vielen elders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde de techniek van de tweede industriële revolutie bij de verovering van Afrika?",
        opties=[
            "stoomschepen, geweren en geneesmiddelen maakten het binnenland bereikbaar",
            "de verovering van het binnenland gebeurde volledig zonder nieuwe techniek",
            "de telegraaf en de spoorweg werden in Afrika nooit aangelegd",
            "Europese legers gebruikten er dezelfde wapens als de inwoners",
        ],
        antwoord=0,
        uitleg="Kinine tegen malaria en repeteergeweren maakten het verschil. De machtsverhouding was volkomen ongelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelden de missionarissen in de kolonies?",
        opties=[
            "zij verspreidden het geloof en richtten scholen en hospitalen op",
            "zij verzetten zich overal tegen het bestuur van hun eigen land",
            "zij hielden zich uitsluitend met de handel in grondstoffen bezig",
            "zij vertrokken pas na de onafhankelijkheid naar de kolonies",
        ],
        antwoord=0,
        uitleg="Zij waren tegelijk een deel van het koloniale gezag en soms de enigen die misbruiken aanklaagden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke betekenis had het Suezkanaal voor het imperialisme?",
        opties=[
            "het verkortte de zeeweg tussen Europa en Azië aanzienlijk",
            "het verbond de Atlantische met de Stille Oceaan",
            "het maakte de reis rond Kaap de Goede Hoop noodzakelijk",
            "het sloot de Middellandse Zee voor Europese schepen af",
        ],
        antwoord=0,
        uitleg="Daardoor werd Egypte strategisch zo belangrijk dat Groot-Brittannië er de hand op legde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het modern imperialisme hangt samen met de behoefte aan grondstoffen van de tweede industriële revolutie.",
        antwoord=True,
        uitleg="Rubber voor fietsen en auto's, palmolie voor zeep, koper voor draden: alles kwam van elders.",
    ),
    dict(
        type="waarofniet",
        vraag="Europa had voor 1870 al het hele binnenland van Afrika onder bestuur.",
        antwoord=False,
        uitleg="Rond 1870 hield Europa vooral kustgebieden bezet. De verdeling van het binnenland kwam daarna.",
    ),
    dict(
        type="waarofniet",
        vraag="Het nationalisme van de negentiende eeuw voedde ook het imperialisme.",
        antwoord=True,
        uitleg="Wie zijn natie groot wilde zien, wilde kolonies. Zo werd de wedloop ook een zaak van prestige.",
    ),
    dict(
        type="waarofniet",
        vraag="Kolonies waren voor de Europese staten altijd een bron van winst.",
        antwoord=False,
        uitleg="Sommige kolonies kostten meer aan bestuur en leger dan ze opbrachten. De winst was vaak van bedrijven.",
    ),
    dict(
        type="waarofniet",
        vraag="In een protectoraat bleef het plaatselijke bestuur op papier bestaan.",
        antwoord=True,
        uitleg="De vorst mocht blijven, maar een Europese resident of adviseur bepaalde de koers.",
    ),
    dict(
        type="invultekst",
        vraag="Welk kanaal werd in 1869 geopend en verkortte de weg naar Azië?",
        antwoord=["het Suezkanaal", "Suezkanaal", "Suez"],
        uitleg="Het verbindt de Middellandse Zee met de Rode Zee. Daardoor werd Egypte een strategisch knooppunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de oorzaken van het imperialisme kloppen?",
        opties=[
            "economische redenen: grondstoffen, markten en belegging",
            "politieke redenen: prestige en strategische steunpunten",
            "er was één enkele oorzaak die alles verklaart",
            "de Afrikaanse staten vroegen Europa zelf om bestuur",
        ],
        antwoord=[0, 1],
        uitleg="Daar komen nog ideologische redenen bij. Één oorzaak aanwijzen zou het verhaal plat maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een tekst uit 1890 over de plicht van de blanke man om andere volken te leiden. Hoe lees je dat?",
        opties=[
            "als een rechtvaardiging van de overheersing van die tijd",
            "als een betrouwbare beschrijving van die andere volken",
            "als een tekst van een tegenstander van het imperialisme",
            "als een wetenschappelijk bewijs voor ongelijke volken",
        ],
        antwoord=0,
        uitleg="Zo'n tekst zegt alles over hoe Europa naar zichzelf keek, en niets over wie het overheerste.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je het imperialisme?",
        opties=[
            "in het economische domein, met grondstoffen en markten",
            "in het politieke domein, met macht en bestuur over gebied",
            "in geen enkel maatschappelijk domein van die tijd",
            "uitsluitend in het culturele domein van de zending",
        ],
        antwoord=[0, 1],
        uitleg="Het culturele domein speelt mee in de beeldvorming, maar economie en politiek zijn de drijfveren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er op de Conferentie van Berlijn van 1884 en 1885?",
        opties=[
            "de mogendheden maakten afspraken over de verdeling van Afrika",
            "de mogendheden gaven Afrika zijn onafhankelijkheid terug",
            "de mogendheden verdeelden Europa na de val van Napoleon",
            "de mogendheden richtten daar de Volkenbond op",
        ],
        antwoord=0,
        uitleg="Er zat geen enkele Afrikaanse vertegenwoordiger aan die tafel. Over hun hoofden werd beslist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke regel spraken de mogendheden in Berlijn af om een gebied te mogen opeisen?",
        opties=[
            "wie een gebied echt bezet, mag het ook opeisen",
            "wie een gebied als eerste op een kaart zet, mag het opeisen",
            "wie de inwoners om toestemming vraagt, mag het opeisen",
            "wie het hoogste bod doet bij de Volkenbond, mag het opeisen",
        ],
        antwoord=0,
        uitleg="Die regel van de effectieve bezetting gaf het sein voor een wedloop met soldaten en vlaggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie kreeg op de Conferentie van Berlijn het Congobekken toegewezen?",
        opties=[
            "koning Leopold II als persoonlijk bezit",
            "de Belgische staat als gewone kolonie",
            "Groot-Brittannië als protectoraat",
            "Frankrijk als invloedssfeer",
        ],
        antwoord=0,
        uitleg="Niet België, maar de koning zelf. Dat maakt het geval van Congo in Europa uitzonderlijk.",
    ),
    dict(
        type="invultekst",
        vraag="In welke stad legden de mogendheden in 1884 en 1885 de regels voor de verdeling van Afrika vast?",
        antwoord=["Berlijn", "in Berlijn"],
        uitleg="Rijkskanselier Bismarck zat de conferentie voor. Daarna ging de wedloop pas echt van start.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel van Afrika was in 1914 in Europese handen?",
        opties=[
            "bijna het hele werelddeel, op twee staten na",
            "ongeveer de helft van het hele werelddeel",
            "enkel de kusten en de grote riviermondingen",
            "nog geen kwart van het hele werelddeel",
        ],
        antwoord=0,
        uitleg="Alleen Ethiopië en Liberia waren toen nog onafhankelijk. Al de rest was verdeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee Afrikaanse staten bleven rond 1914 onafhankelijk?",
        opties=[
            "Ethiopië en Liberia",
            "Egypte en Marokko",
            "Congo en Rwanda",
            "Zuid-Afrika en Kenia",
        ],
        antwoord=0,
        uitleg="Ethiopië had een Italiaans leger verslagen; Liberia was gesticht door vrijgemaakte slaven uit Amerika.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1896 bij Adwa in Ethiopië?",
        opties=[
            "een Ethiopisch leger versloeg een Italiaans invasieleger",
            "een Italiaans leger veroverde het hele land Ethiopië",
            "de mogendheden verdeelden Ethiopië onder elkaar",
            "Ethiopië werd een protectoraat van Groot-Brittannië",
        ],
        antwoord=0,
        uitleg="Die nederlaag was in Europa een schok, want ze paste niet in het beeld van de eigen onoverwinnelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van verzet kwamen er in de kolonies tegen het Europese bestuur?",
        opties=[
            "gewapende opstanden tegen de koloniale legers",
            "weigeren te werken of belasting te betalen",
            "een stem opeisen in het parlement van de kolonisator",
            "een zaak aanhangig maken bij de Verenigde Naties",
        ],
        antwoord=[0, 1],
        uitleg="De Verenigde Naties bestonden nog niet, en in de parlementen van Europa hadden kolonies geen zitje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg hebben de koloniale grenzen tot vandaag?",
        opties=[
            "veel grenzen lopen dwars door gebieden van één volk",
            "alle grenzen volgen precies de taalgrenzen van Afrika",
            "alle grenzen werden na 1960 helemaal opnieuw getekend",
            "de grenzen zijn na de onafhankelijkheid volledig verdwenen",
        ],
        antwoord=0,
        uitleg="Ze werden met een lat op een kaart in Europa getrokken. Veel staten leven nog met dat erfstuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werd de economie van een kolonie meestal ingericht?",
        opties=[
            "op de uitvoer van enkele grondstoffen naar het moederland",
            "op een eigen zware industrie voor de plaatselijke markt",
            "op de invoer van grondstoffen uit het moederland",
            "op de handel met de buurlanden in het eigen werelddeel",
        ],
        antwoord=0,
        uitleg="Rubber, koper, katoen of cacao: één of twee producten. Zulke eenzijdigheid maakt een land kwetsbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de menselijke tentoonstellingen op de wereldtentoonstellingen rond 1900?",
        opties=[
            "mensen uit de kolonies werden aan het publiek tentoongesteld",
            "kunstwerken uit de kolonies werden in een museum opgesteld",
            "machines uit de kolonies werden aan ingenieurs voorgesteld",
            "landkaarten van de kolonies werden aan het publiek getoond",
        ],
        antwoord=0,
        uitleg="In Tervuren gebeurde dat in 1897. Een aantal van die mensen is hier gestorven en begraven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spanningen tussen de mogendheden kwamen uit de wedloop om Afrika?",
        opties=[
            "Frankrijk en Groot-Brittannië stonden in 1898 bij Fashoda tegenover elkaar",
            "Duitsland en Frankrijk kwamen over Marokko tweemaal in botsing",
            "Groot-Brittannië en Rusland verdeelden Congo onder elkaar",
            "Italië en Spanje voerden een oorlog over Egypte en Suez",
        ],
        antwoord=[0, 1],
        uitleg="Die botsingen rond 1900 maakten de bondgenootschappen vaster. Zo liep de weg verder naar 1914.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de Conferentie van Berlijn zat ook een Afrikaanse vertegenwoordiger aan tafel.",
        antwoord=False,
        uitleg="Er zat niemand uit Afrika bij. Dat is een van de redenen waarom de grenzen zo willekeurig lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="De regel van de effectieve bezetting versnelde de verdeling van Afrika.",
        antwoord=True,
        uitleg="Wie te lang wachtte, zag de vlag van een ander staan. Dat maakte er een wedloop van.",
    ),
    dict(
        type="waarofniet",
        vraag="De inwoners van de kolonies hebben zich nooit tegen het Europese bestuur verzet.",
        antwoord=False,
        uitleg="Er waren opstanden in Duits-Zuidwest-Afrika, in Duits-Oost-Afrika en op veel andere plaatsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Ethiopië slaagde erin een Europees invasieleger te verslaan.",
        antwoord=True,
        uitleg="Bij Adwa in 1896, tegen Italië. Daardoor bleef het land tot in de jaren dertig onafhankelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De koloniale economie liet de kolonies zelf hun industrie uitbouwen.",
        antwoord=False,
        uitleg="Grondstoffen gingen weg, afgewerkte goederen kwamen terug. Eigen industrie paste daar niet in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een gebied dat door een vreemde staat bestuurd wordt en dat grondstoffen moet leveren?",
        antwoord=["een kolonie", "kolonie", "de kolonie"],
        uitleg="Het verschil met een protectoraat is dat daar het eigen bestuur op papier overeind blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een kaart van Afrika uit 1914 met rechte grenzen en kleurvlakken per mogendheid. Wat besluit je?",
        opties=[
            "de grenzen zijn in Europa getekend, niet door de volken ter plaatse",
            "de grenzen volgen de rivieren en de bergketens van het werelddeel",
            "de grenzen zijn door de Afrikaanse staten zelf afgesproken",
            "de kaart dateert van na de onafhankelijkheid van de kolonies",
        ],
        antwoord=0,
        uitleg="Rechte lijnen door woestijn en savanne zijn het handschrift van een conferentietafel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men het imperialisme een oorzaak van de Eerste Wereldoorlog?",
        opties=[
            "de wedloop om gebied maakte de mogendheden rivalen",
            "de kolonies vielen Europa in 1914 zelf aan",
            "de kolonies weigerden na 1914 nog grondstoffen te leveren",
            "de mogendheden gaven hun kolonies in 1914 vrij",
        ],
        antwoord=0,
        uitleg="Elke crisis om een gebied dreef de bondgenootschappen verder in hun stellingen.",
    ),
]

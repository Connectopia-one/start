# -*- coding: utf-8 -*-
"""Congo: van Congo-Vrijstaat tot Belgisch Congo.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: Congo als
voorbeeld van het modern imperialisme, van de Congo-Vrijstaat van Leopold II
over de overname door België tot het koloniale bestuur voor 1960.

Deel 1 gaat over de Vrijstaat en de wandaden die er gebeurden. Deel 2 gaat over
Belgisch Congo: wie er bestuurde, wie er winst maakte en wat de inwoners wel en
niet mochten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie was de eigenaar van de Congo-Vrijstaat na 1885?",
        opties=[
            "koning Leopold II in persoon",
            "de Belgische staat en haar parlement",
            "een vennootschap van Britse handelaars",
            "de Conferentie van Berlijn zelf",
        ],
        antwoord=0,
        uitleg="Niet België, maar de koning zelf. Het Belgische parlement had er geen zeg in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ontdekkingsreiziger verkende Congo in opdracht van Leopold II?",
        opties=[
            "Henry Morton Stanley",
            "David Livingstone",
            "James Cook",
            "Ferdinand de Lesseps",
        ],
        antwoord=0,
        uitleg="Hij liet plaatselijke leiders verdragen ondertekenen die zij vaak niet konden lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee rechtvaardigde Leopold II zijn onderneming in Congo tegenover Europa?",
        opties=[
            "met de strijd tegen de slavenhandel en met de beschaving",
            "met de nood aan nieuwe landbouwgrond voor Belgische boeren",
            "met de bescherming van de Belgische grenzen in Europa",
            "met de vraag van de Congolese leiders om een koning",
        ],
        antwoord=0,
        uitleg="Dat verhaal maakte in Europa veel goed. De werkelijkheid in het gebied zag er heel anders uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke producten brachten de Vrijstaat zijn grootste winsten?",
        opties=[
            "rubber uit de wilde lianen van het regenwoud",
            "ivoor uit de jacht op olifanten in het binnenland",
            "steenkool uit de mijnen van het Katangese plateau",
            "graan van de akkers langs de Congostroom",
        ],
        antwoord=[0, 1],
        uitleg="Rubber werd goud waard toen de fiets en de auto doorbraken. De vraag uit Europa was onverzadigbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werd het rubber in de Vrijstaat ingezameld?",
        opties=[
            "dorpen moesten onder dwang een vastgelegde hoeveelheid leveren",
            "arbeiders deden het vrijwillig tegen een afgesproken loon",
            "Europese arbeiders werden daarvoor uit België overgebracht",
            "machines in grote fabrieken deden dat werk in de plaats",
        ],
        antwoord=0,
        uitleg="Wie zijn quotum niet haalde, werd gestraft. Gijzelingen van vrouwen en kinderen waren gewoon.",
    ),
    dict(
        type="invultekst",
        vraag="Welk product uit het regenwoud bracht de Congo-Vrijstaat het meeste geld op?",
        antwoord=["rubber", "het rubber", "caoutchouc"],
        uitleg="De vraag kwam van de fietsen en de auto's van de tweede industriële revolutie in Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de Force Publique?",
        opties=[
            "het leger en de politie van de Congo-Vrijstaat",
            "de vereniging van Belgische handelaars in Congo",
            "de rechtbank die de wandaden in Congo onderzocht",
            "de school die Congolese ambtenaren moest opleiden",
        ],
        antwoord=0,
        uitleg="Zij hield de quota af te dwingen. Haar soldaten waren Congolees, haar officieren Europees.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke wandaden werden onder het bestuur van de Vrijstaat vastgesteld?",
        opties=[
            "dwangarbeid met zweepslagen en gijzelingen als straf",
            "het afhakken van handen van wie het quotum niet haalde",
            "de verplichte schoolplicht voor alle Congolese kinderen",
            "de invoering van het algemeen stemrecht in de kolonie",
        ],
        antwoord=[0, 1],
        uitleg="Soldaten moesten elke kogel verantwoorden met een hand, en dat leidde tot verminking van levenden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de chicotte die in de Vrijstaat werd gebruikt?",
        opties=[
            "een zweep van gedroogde huid, gebruikt om te straffen",
            "een werktuig om het rubber uit de lianen te tappen",
            "een boot waarmee men de Congostroom kon bevaren",
            "een munt waarmee men de arbeiders uitbetaalde",
        ],
        antwoord=0,
        uitleg="Een straf met de chicotte kon dodelijk zijn. Ze werd ook onder het Belgische bestuur nog toegepast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie klaagde de wandaden in de Congo-Vrijstaat in Europa aan?",
        opties=[
            "de Britse journalist Edmund Dene Morel",
            "de Britse consul Roger Casement met zijn verslag",
            "de Conferentie van Berlijn met een nieuw verdrag",
            "de Volkenbond met een onderzoekscommissie",
        ],
        antwoord=[0, 1],
        uitleg="De Volkenbond bestond nog niet. Hun campagne zette Leopold II internationaal onder druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1908 met Congo?",
        opties=[
            "de Belgische staat nam de kolonie van de koning over",
            "de kolonie werd onafhankelijk onder een eigen bestuur",
            "de kolonie werd aan Groot-Brittannië doorverkocht",
            "de kolonie werd door de Volkenbond onder toezicht geplaatst",
        ],
        antwoord=0,
        uitleg="Onder internationale druk stemde het parlement de overname. Zo werd de Vrijstaat Belgisch Congo.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar nam de Belgische staat Congo van Leopold II over?",
        antwoord=["1908"],
        uitleg="Vanaf dan heette het Belgisch Congo en besliste het parlement in Brussel over de kolonie.",
    ),
    dict(
        type="waarofniet",
        vraag="De Congo-Vrijstaat was een kolonie van de Belgische staat.",
        antwoord=False,
        uitleg="Ze was persoonlijk bezit van Leopold II. België nam ze pas in 1908 over.",
    ),
    dict(
        type="waarofniet",
        vraag="Leopold II heeft Congo nooit zelf bezocht.",
        antwoord=True,
        uitleg="Hij bestuurde zijn gebied van hieruit, met ambtenaren en vennootschappen als tussenpersonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Onder de Vrijstaat werd de bevolking van Congo zwaar getroffen door geweld, honger en ziekte.",
        antwoord=True,
        uitleg="Schattingen van het dodental lopen uiteen en gaan tot in de miljoenen. Zekere cijfers zijn er niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De dwangarbeid voor het rubber gebeurde met instemming van de dorpen.",
        antwoord=False,
        uitleg="Er was geen instemming, wel een quotum en een straf. Gijzeling van gezinsleden was een gewoon middel.",
    ),
    dict(
        type="waarofniet",
        vraag="De kritiek op de Vrijstaat kwam vooral uit het buitenland.",
        antwoord=True,
        uitleg="Britse journalisten, diplomaten en missionarissen brachten de feiten naar buiten. In België bleef het stil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een verslag van een Britse consul uit 1904 over verminkingen in Congo. Hoe ga je met die bron om?",
        opties=[
            "je toetst ze aan andere bronnen, zoals missieverslagen en foto's",
            "je verwerpt ze, want een consul is altijd partijdig",
            "je neemt ze over, want een officieel verslag kan niet mis zijn",
            "je legt ze naast je neer, want ze is te oud om nog te kloppen",
        ],
        antwoord=0,
        uitleg="Verschillende bronnen van verschillende kanten vertelden hetzelfde. Dat maakt het beeld sterk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een foto uit 1904 van een Congolese man met een verminkte hand. Wat zegt die bron?",
        opties=[
            "dat verminking als straf of als bewijsstuk werd gebruikt",
            "dat de man bij het rubbertappen een ongeluk heeft gehad",
            "dat het beeld later in een studio in scène is gezet",
            "dat de Belgische staat dit toen al verboden had",
        ],
        antwoord=0,
        uitleg="Zulke foto's werden door missionarissen genomen en in Europa als bewijsmateriaal gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je de Vrijstaat van Leopold II?",
        opties=[
            "in het economische domein, met rubber en ivoor als winst",
            "in het politieke domein, met de macht over een gebied",
            "in geen enkel maatschappelijk domein van die tijd",
            "uitsluitend in het culturele domein van de zending",
        ],
        antwoord=[0, 1],
        uitleg="De missies horen in het culturele domein, maar de drijfveer van de Vrijstaat was winst en macht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie machten bestuurden Belgisch Congo in de praktijk?",
        opties=[
            "de koloniale staat met haar ambtenaren",
            "de kerk met haar missies en haar scholen",
            "een verkozen parlement van de Congolezen zelf",
            "de Verenigde Naties met een eigen bestuur",
        ],
        antwoord=[0, 1],
        uitleg="Daar hoorden ook de grote vennootschappen bij. Men spreekt daarom van het koloniale drieluik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grondstof maakte Katanga voor België zo waardevol?",
        opties=[
            "koper",
            "rubber",
            "ivoor",
            "steenkool",
        ],
        antwoord=0,
        uitleg="De Union Minière du Haut-Katanga werd een van de grootste mijnbedrijven ter wereld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelden de missies in Belgisch Congo?",
        opties=[
            "zij verzorgden het grootste deel van het onderwijs",
            "zij bestuurden de kolonie in plaats van de ambtenaren",
            "zij hielden zich enkel met de mijnbouw in Katanga bezig",
            "zij waren er pas na de onafhankelijkheid actief",
        ],
        antwoord=0,
        uitleg="Lager onderwijs bereikte veel kinderen. Hoger onderwijs bleef bijna tot het einde onbestaande.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke politieke rechten hadden de Congolezen in Belgisch Congo?",
        opties=[
            "zij hadden geen stemrecht en geen eigen volksvertegenwoordiging",
            "zij konden afgevaardigden naar het parlement in Brussel sturen",
            "zij kozen hun eigen gouverneur-generaal bij verkiezingen",
            "zij hadden dezelfde rechten als de inwoners van België",
        ],
        antwoord=0,
        uitleg="Het bestuur werd in Brussel beslist en door ambtenaren uitgevoerd. De bevolking werd niet geraadpleegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het paternalisme van het Belgische koloniale bestuur?",
        opties=[
            "men behandelde de bevolking als kinderen die geleid moeten worden",
            "men liet de bevolking haar eigen bestuur en wetten uitwerken",
            "men gaf de bevolking dezelfde rechten als de Belgen zelf",
            "men stuurde Congolese studenten naar de universiteit in België",
        ],
        antwoord=0,
        uitleg="Zorg voor scholen en hospitalen hoorde erbij, maar zeggenschap niet. Daar kwam de botsing van 1960 uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de houding waarbij een bestuur de bevolking als onmondige kinderen behandelt?",
        antwoord=["paternalisme", "het paternalisme"],
        uitleg="Het woord komt van pater, vader. Goed bedoelde zorg zonder enige zeggenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie waren de évolués in Belgisch Congo?",
        opties=[
            "Congolezen met een opleiding en een baan in het bestuur",
            "Belgische ambtenaren die een loopbaan in de kolonie maakten",
            "missionarissen die in de kolonie een school openden",
            "Congolese leiders die tegen het koloniale bestuur vochten",
        ],
        antwoord=0,
        uitleg="Zij vormden een kleine middengroep. Juist uit hun rangen kwam later de eis voor onafhankelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemde men Belgisch Congo in Europa een modelkolonie?",
        opties=[
            "omdat er scholen en hospitalen waren en de mijnen winst maakten",
            "omdat de Congolezen er stemrecht en een parlement hadden",
            "omdat er geen enkele vorm van dwangarbeid meer bestond",
            "omdat de kolonie zich zelf bestuurde zonder Belgisch toezicht",
        ],
        antwoord=0,
        uitleg="Dat beeld hield geen rekening met het ontbreken van rechten en met de dwang die bleef bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grondstof uit Congo speelde in de Tweede Wereldoorlog een bijzondere rol?",
        opties=[
            "uranium uit de mijn van Shinkolobwe",
            "rubber uit de wouden van Equateur",
            "ivoor uit de jacht in het binnenland",
            "diamant uit de rivieren van Kasaï",
        ],
        antwoord=0,
        uitleg="Het werd gebruikt voor de eerste atoombommen. Congo kwam daarmee in de wereldpolitiek terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe leefden Belgen en Congolezen in de koloniale steden samen?",
        opties=[
            "gescheiden, in eigen wijken met eigen voorzieningen",
            "door elkaar, in dezelfde wijken en dezelfde scholen",
            "uitsluitend in dorpen buiten de steden om",
            "samen in één wijk, met hetzelfde loon voor hetzelfde werk",
        ],
        antwoord=0,
        uitleg="Er waren aparte wijken, aparte scholen en een avondklok voor Congolezen in de Europese stad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kwamen er in Congo de eerste universiteiten?",
        opties=[
            "in de jaren vijftig, kort voor de onafhankelijkheid",
            "in 1908, meteen bij de overname door België",
            "in de jaren twintig, na de Eerste Wereldoorlog",
            "pas na de onafhankelijkheid van het land",
        ],
        antwoord=0,
        uitleg="Daardoor waren er in 1960 maar een handvol Congolezen met een universitair diploma.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grondstof uit Katanga was voor de Belgische mijnbedrijven het belangrijkst?",
        antwoord=["koper", "het koper"],
        uitleg="Rond het koper van Katanga werd een hele industrie en een hele stad gebouwd.",
    ),
    dict(
        type="waarofniet",
        vraag="Belgisch Congo had een gouverneur-generaal die door Brussel werd aangesteld.",
        antwoord=True,
        uitleg="Hij voerde uit wat de minister van Koloniën besliste. De bevolking koos hem niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De Congolezen kregen in Belgisch Congo stemrecht voor het parlement in Brussel.",
        antwoord=False,
        uitleg="Zij hadden geen enkele politieke vertegenwoordiging, niet in Congo en niet in België.",
    ),
    dict(
        type="waarofniet",
        vraag="De overname door België in 1908 maakte een einde aan alle dwangarbeid in Congo.",
        antwoord=False,
        uitleg="De ergste excessen namen af, maar verplichte arbeid en verplichte teelten bleven bestaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Het lager onderwijs in Belgisch Congo was grotendeels in handen van de missies.",
        antwoord=True,
        uitleg="Daardoor was het bereik groot, en de inhoud volledig door de kerk en de kolonisator bepaald.",
    ),
    dict(
        type="waarofniet",
        vraag="In 1960 had Congo een ruime groep van eigen artsen, ingenieurs en hoge ambtenaren.",
        antwoord=False,
        uitleg="Door het ontbreken van hoger onderwijs waren die er amper. Dat maakte de overgang bijzonder moeilijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over Belgisch Congo kloppen?",
        opties=[
            "staat, kerk en grote bedrijven bestuurden samen de kolonie",
            "de Congolezen hadden geen politieke rechten",
            "de Congolezen konden een eigen regering verkiezen",
            "de kolonie bouwde haar eigen zware industrie uit",
        ],
        antwoord=[0, 1],
        uitleg="De economie bleef op uitvoer van grondstoffen gericht. Een eigen industrie paste daar niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een schoolboek uit 1950 waarin Congo als een geschenk van België wordt beschreven. Hoe lees je dat?",
        opties=[
            "als beeldvorming van de kolonisator over zichzelf",
            "als een betrouwbare beschrijving van het koloniale bestuur",
            "als een getuigenis van de Congolese bevolking zelf",
            "als een wetenschappelijk verslag van een onderzoeker",
        ],
        antwoord=0,
        uitleg="Wie zo'n bron leest, leert hoe België naar zichzelf keek. Over Congo zelf zegt ze bijna niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen Belgisch Congo en het modern imperialisme?",
        opties=[
            "het is er een voorbeeld van, met bestuur en winst van buiten",
            "het is er een uitzondering op: Congo bestuurde zichzelf volledig",
            "het is er een tegenvoorbeeld van: België zocht geen grondstoffen",
            "het heeft er niets mee te maken: Congo was een protectoraat",
        ],
        antwoord=0,
        uitleg="Alle kenmerken komen samen: een conferentie in Europa, grondstoffen voor de industrie, bestuur van buiten.",
    ),
]

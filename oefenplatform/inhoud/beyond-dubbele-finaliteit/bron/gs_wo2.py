# -*- coding: utf-8 -*-
"""De Tweede Wereldoorlog en de Holocaust.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: het verloop van
de oorlog, de bezetting van België met collaboratie en verzet, de Holocaust, en
de nasleep met de processen en de rechten van de mens.

Deel 1 gaat over het verloop en over bezet België. Deel 2 gaat over de
vervolging en de vernietiging van de Joden, en over wat er na 1945 uit geleerd is.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Met welke gebeurtenis begon de Tweede Wereldoorlog in Europa?",
        opties=[
            "de Duitse inval in Polen in september 1939",
            "de Duitse inval in België in mei 1940",
            "de aanval op Pearl Harbor in december 1941",
            "de Duitse inval in de Sovjet-Unie in juni 1941",
        ],
        antwoord=0,
        uitleg="Twee dagen later verklaarden Frankrijk en Groot-Brittannië Duitsland de oorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een blitzkrieg?",
        opties=[
            "een snelle aanval met tanks, vliegtuigen en motorvoertuigen",
            "een oorlog die jarenlang in loopgraven wordt uitgevochten",
            "een oorlog die uitsluitend in de lucht wordt gevoerd",
            "een aanval met bombardementen en daarna een belegering",
        ],
        antwoord=0,
        uitleg="Precies het omgekeerde van de stellingenoorlog van 1914. Polen en Frankrijk vielen in weken.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke dag van 1940 viel het Duitse leger België binnen?",
        antwoord=["10 mei", "10 mei 1940"],
        uitleg="Diezelfde dag vielen ook Nederland en Luxemburg. De aanval op Frankrijk liep daar dwars door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lang duurde de Belgische veldtocht van mei 1940?",
        opties=[
            "achttien dagen",
            "vier jaar",
            "tien dagen",
            "achttien maanden",
        ],
        antwoord=0,
        uitleg="Daarna gaf het leger zich over. Van de IJzerstelling van 1914 was deze keer geen sprake.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover kwamen koning Leopold III en zijn regering in 1940 in botsing?",
        opties=[
            "de koning bleef in het bezette land, de regering week uit naar Londen",
            "de koning week uit naar Londen, de regering bleef in het land",
            "de koning wilde de oorlog voortzetten, de regering wilde zich overgeven",
            "de koning en de regering weken samen naar Congo uit",
        ],
        antwoord=0,
        uitleg="Die breuk werd na de oorlog de koningskwestie, en ze heeft hem uiteindelijk zijn troon gekost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is collaboratie?",
        opties=[
            "samenwerken met de bezetter van je land",
            "je verzetten tegen de bezetter van je land",
            "je land verlaten zolang de oorlog duurt",
            "weigeren voor de bezetter te gaan werken",
        ],
        antwoord=0,
        uitleg="Sommigen deden het uit overtuiging, anderen uit berekening. Na de oorlog volgde de repressie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen nam het verzet in bezet België aan?",
        opties=[
            "gewapende acties tegen spoorwegen en bezettingstroepen",
            "sluikpers die nieuws verspreidde buiten de censuur om",
            "deelname aan de verkiezingen voor het parlement",
            "klachten indienen bij de rechtbanken van de bezetter",
        ],
        antwoord=[0, 1],
        uitleg="Er waren geen verkiezingen en geen rechtsmiddelen. Wie iets wou doen, moest het in het geheim doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de verplichte tewerkstelling in bezet België?",
        opties=[
            "Belgen werden gedwongen in Duitsland te gaan werken",
            "Belgen werden gedwongen in het Belgische leger te dienen",
            "Belgen mochten niet meer buiten hun gemeente werken",
            "Belgen moesten verplicht op het land gaan werken",
        ],
        antwoord=0,
        uitleg="Wie zich onttrok, werd werkweigeraar en moest onderduiken. Velen kwamen zo bij het verzet terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in juni 1941 aan het oostfront?",
        opties=[
            "Duitsland viel de Sovjet-Unie binnen",
            "de Sovjet-Unie viel Duitsland binnen",
            "Duitsland en de Sovjet-Unie sloten vrede",
            "de Sovjet-Unie veroverde Berlijn",
        ],
        antwoord=0,
        uitleg="Daarmee verbrak Duitsland zijn eigen pact van 1939. Het oostfront werd het bloedigste van de oorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom traden de Verenigde Staten in december 1941 in de oorlog?",
        opties=[
            "Japan had hun vloot in Pearl Harbor aangevallen",
            "Duitsland had hun vloot in de Atlantische Oceaan aangevallen",
            "de Volkenbond had hen daartoe uitdrukkelijk verplicht",
            "Groot-Brittannië had hun om soldaten gevraagd",
        ],
        antwoord=0,
        uitleg="Daarna verklaarde ook Duitsland hen de oorlog. Zo werd het conflict pas echt wereldwijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veldslag wordt als keerpunt aan het oostfront beschouwd?",
        opties=[
            "de slag om Stalingrad",
            "de slag om Engeland",
            "de slag bij Waterloo",
            "de slag om de Ardennen",
        ],
        antwoord=0,
        uitleg="Een heel Duits leger ging er verloren. Vanaf dan schoof het front onophoudelijk naar het westen.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke dag van 1944 landden de Geallieerden in Normandië?",
        antwoord=["6 juni", "6 juni 1944", "D-day"],
        uitleg="Het grootste landingsleger uit de geschiedenis. Drie maanden later was België bevrijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer werd het grootste deel van België bevrijd?",
        opties=[
            "in september 1944",
            "in mei 1940",
            "in mei 1945",
            "in december 1944",
        ],
        antwoord=0,
        uitleg="In december volgde nog het Ardennenoffensief, de laatste Duitse poging om het tij te keren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee eindigde de oorlog tegen Japan in augustus 1945?",
        opties=[
            "met twee atoombommen op Japanse steden",
            "met een landing van de Geallieerden in Tokio",
            "met een vredesverdrag zonder enige strijd",
            "met de verovering van Japan door de Sovjet-Unie",
        ],
        antwoord=0,
        uitleg="Hiroshima en Nagasaki werden vernietigd. Daarmee begon ook het atoomtijdperk van de Koude Oorlog.",
    ),
    dict(
        type="waarofniet",
        vraag="België werd in mei 1940 binnengevallen hoewel het zich neutraal had verklaard.",
        antwoord=True,
        uitleg="Net als in 1914. De neutraliteit heeft het land ook de tweede keer niet beschermd.",
    ),
    dict(
        type="waarofniet",
        vraag="In bezet België waren er vrije verkiezingen en een vrije pers.",
        antwoord=False,
        uitleg="Het parlement vergaderde niet en de pers stond onder censuur. Daarom ontstond de sluikpers.",
    ),
    dict(
        type="waarofniet",
        vraag="Zowel collaboratie als verzet kwamen in bezet België voor.",
        antwoord=True,
        uitleg="De meeste mensen deden geen van beide: zij probeerden vooral de oorlog door te komen.",
    ),
    dict(
        type="waarofniet",
        vraag="De Tweede Wereldoorlog werd vooral in loopgraven uitgevochten, zoals de Eerste.",
        antwoord=False,
        uitleg="Deze oorlog was er een van beweging: tanks, vliegtuigen en snelle doorbraken over grote afstanden.",
    ),
    dict(
        type="waarofniet",
        vraag="De burgerbevolking was in de Tweede Wereldoorlog een doelwit van de oorlogsvoering.",
        antwoord=True,
        uitleg="Steden werden gebombardeerd en Antwerpen kreeg honderden V-bommen over zich heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een foto uit 1944 van juichende mensen rond een tank in een Belgische straat. Wat herken je?",
        opties=[
            "de bevrijding in september 1944",
            "de inval in mei 1940",
            "het Ardennenoffensief in december 1944",
            "de mobilisatie van het leger in 1939",
        ],
        antwoord=0,
        uitleg="Juichende mensen rond Geallieerde voertuigen horen bij de bevrijding, niet bij een inval.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het woord Holocaust of Shoah?",
        opties=[
            "de systematische vernietiging van de Joden van Europa",
            "de bombardementen op de Duitse en Britse steden",
            "de verplichte tewerkstelling van Europese arbeiders",
            "de vlucht van miljoenen mensen uit hun eigen land",
        ],
        antwoord=0,
        uitleg="Shoah is het Hebreeuwse woord. Het gaat om een vernietiging die door een staat gepland werd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen gingen aan de vernietiging van de Joden vooraf?",
        opties=[
            "uitsluiting bij wet van beroepen, scholen en openbaar leven",
            "verplichte kentekens en registratie van wie Joods was",
            "een volksstemming over de behandeling van de Joden",
            "een uitspraak van een internationale rechtbank",
        ],
        antwoord=[0, 1],
        uitleg="Eerst uitsluiten, dan isoleren, dan deporteren. Elke stap maakte de volgende makkelijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was een getto in de bezette gebieden in Oost-Europa?",
        opties=[
            "een afgesloten wijk waar Joden gedwongen moesten wonen",
            "een kamp waar krijgsgevangenen werden vastgehouden",
            "een fabriek waar dwangarbeiders moesten werken",
            "een wijk die bij een bombardement verwoest was",
        ],
        antwoord=0,
        uitleg="Honger en ziekte kostten er al duizenden het leven voor de deportaties naar de kampen begonnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd op de conferentie in Wannsee in januari 1942 besproken?",
        opties=[
            "de organisatie van de vernietiging van de Joden van Europa",
            "de vredesvoorwaarden tussen Duitsland en de Sovjet-Unie",
            "de verdeling van Afrika onder de Europese mogendheden",
            "de oprichting van de Verenigde Naties na de oorlog",
        ],
        antwoord=0,
        uitleg="Hooggeplaatste ambtenaren stemden er de uitvoering af. De moord zelf was toen al begonnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het verschil tussen een concentratiekamp en een vernietigingskamp?",
        opties=[
            "een vernietigingskamp was voor het doden ingericht",
            "een concentratiekamp was voor het doden ingericht",
            "er was tussen die twee geen enkel verschil",
            "een vernietigingskamp lag altijd in Duitsland zelf",
        ],
        antwoord=0,
        uitleg="In een concentratiekamp stierven mensen van dwangarbeid, honger en geweld. De vernietigingskampen lagen in Polen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk vernietigingskamp in bezet Polen is het bekendste geworden?",
        antwoord=["Auschwitz", "Auschwitz-Birkenau"],
        uitleg="Daar werden ook de Joden uit België naartoe gevoerd. Het is nu een gedenkplaats en een museum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van waar in België werden de Joden naar de kampen gedeporteerd?",
        opties=[
            "uit de Dossinkazerne in Mechelen",
            "uit het Noordstation in Brussel",
            "uit de haven van Antwerpen",
            "uit de citadel van Luik",
        ],
        antwoord=0,
        uitleg="Die kazerne was het verzamelkamp. Nu staat er het museum en het documentatiecentrum Kazerne Dossin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel Joden werden uit België gedeporteerd?",
        opties=[
            "meer dan vijfentwintigduizend mensen",
            "ongeveer tweehonderd mensen",
            "ongeveer tweeduizend mensen",
            "meer dan een half miljoen mensen",
        ],
        antwoord=0,
        uitleg="Slechts een kleine minderheid van hen heeft de oorlog overleefd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werden Joodse kinderen in bezet België soms gered?",
        opties=[
            "zij werden ondergebracht bij gezinnen, kloosters en instellingen",
            "zij mochten van de bezetter met hun ouders het land verlaten",
            "zij werden door het Rode Kruis naar Zwitserland gebracht",
            "zij werden door de gemeenten officieel geregistreerd",
        ],
        antwoord=0,
        uitleg="Verzetsgroepen vervalsten papieren en zochten onderdak. Daarom zijn er duizenden kinderen gered.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke andere groepen werden door het naziregime vervolgd?",
        opties=[
            "Roma en Sinti",
            "mensen met een handicap",
            "de leden van de eigen partij",
            "de officieren van het eigen leger",
        ],
        antwoord=[0, 1],
        uitleg="Ook homoseksuelen, politieke tegenstanders en Jehova's getuigen werden opgepakt en vermoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel Joden kwamen in de Holocaust om het leven?",
        opties=[
            "ongeveer zes miljoen mensen",
            "ongeveer zeshonderdduizend mensen",
            "ongeveer zestigduizend mensen",
            "ongeveer zestig miljoen mensen",
        ],
        antwoord=0,
        uitleg="Dat is het geheel van de oorlog in Europa niet meegerekend; die kostte tientallen miljoenen mensen het leven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het opzettelijk uitroeien van een volk of een groep?",
        antwoord=["genocide", "volkerenmoord", "een genocide"],
        uitleg="Het woord werd tijdens de oorlog gevormd en kort daarna in het internationaal recht opgenomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in Neurenberg in 1945 en 1946?",
        opties=[
            "leiders van het naziregime stonden er terecht",
            "het vredesverdrag met Duitsland werd er ondertekend",
            "de Verenigde Naties werden er opgericht",
            "Duitsland werd er in vier zones verdeeld",
        ],
        antwoord=0,
        uitleg="Voor het eerst stonden leiders terecht voor misdaden tegen de menselijkheid. Dat was nieuw in het recht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke internationale teksten en instellingen kwamen uit de oorlog?",
        opties=[
            "de Verenigde Naties in 1945",
            "de Universele Verklaring van de Rechten van de Mens in 1948",
            "de Volkenbond in Genève",
            "het Verdrag van Versailles",
        ],
        antwoord=[0, 1],
        uitleg="De Volkenbond en Versailles horen bij de vorige oorlog. Deze keer wilde men het sterker aanpakken.",
    ),
    dict(
        type="waarofniet",
        vraag="De vervolging van de Joden begon met uitsluiting bij wet, nog voor de oorlog.",
        antwoord=True,
        uitleg="De Neurenberger wetten van 1935 ontnamen hen hun burgerrechten. De vernietiging kwam later.",
    ),
    dict(
        type="waarofniet",
        vraag="De Holocaust was het werk van enkele individuen zonder hulp van ambtenaren.",
        antwoord=False,
        uitleg="Er waren registers, treinen, verordeningen en ambtenaren voor nodig. Juist dat maakt haar zo verontrustend.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook uit België zijn Joden naar de vernietigingskampen gedeporteerd.",
        antwoord=True,
        uitleg="Meer dan vijfentwintigduizend mensen, via de Dossinkazerne in Mechelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Niemand in bezet Europa heeft geprobeerd Joden te helpen.",
        antwoord=False,
        uitleg="Duizenden mensen hebben onderdak of papieren geregeld. Israël eert hen als rechtvaardigen onder de volkeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Het begrip misdaad tegen de menselijkheid werd pas na de Tweede Wereldoorlog in het recht opgenomen.",
        antwoord=True,
        uitleg="Het proces van Neurenberg heeft dat begrip in de rechtspraak gebracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een getuigenis van een overlevende van Auschwitz, zestig jaar na de feiten. Hoe ga je ermee om?",
        opties=[
            "als een waardevolle bron, die je naast documenten en cijfers legt",
            "als een bron die je verwerpt, want het geheugen bedriegt altijd",
            "als een bron die alle andere bronnen overbodig maakt",
            "als een bron zonder waarde, want ze is niet van die tijd zelf",
        ],
        antwoord=0,
        uitleg="Een getuigenis zegt hoe iemand het beleefde. Voor de omvang en de organisatie heb je documenten nodig.",
    ),
]

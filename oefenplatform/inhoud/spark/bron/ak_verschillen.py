# -*- coding: utf-8 -*-
"""De vragen voor "Waarom landschappen verschillen" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "verschillen tussen landschappen"
(7,5 % van het examen), samen met de ruimtelijke patronen uit de rubriek
ervoor.

Deel 1 gaat over de patronen zelf: de reliëfeenheden van België, de
klimaatzones, de vegetatiezones en de bevolkingsspreiding in de wereld.
Deel 2 gaat over de relaties tussen de landschapsvormende lagen, over
natuurlijke tegenover menselijke landschappen, en over duurzaamheid met het
5P-model.

De dertien reliëfeenheden staan woordelijk in de fiche en worden hier ook
woordelijk gebruikt. Het patroon erachter is wat een kind moet begrijpen:
België klimt van de Noordzee naar het zuidoosten, van laagvlakte over
laagplateau naar plateau. Wie hier iets bijschrijft, controleert de naam in de
fiche, want "Haspengouws Laagplateau" en "Plateau van Herve" zijn geen namen
die je uit je hoofd mag benaderen.

Er wordt nergens gevraagd om iets op een kaart aan te wijzen. In het
oefenplatform ligt er geen kaart naast de vraag; het aanwijzen zelf gebeurt in
de leerbundel en in de oefenbundel, waar de kaart wel meegeleverd wordt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je rijdt van de Belgische kust naar de Ardennen. Wat gebeurt er onderweg met het landschap?",
        opties=[
            "Het gaat geleidelijk omhoog",
            "Het blijft van begin tot eind even vlak",
            "Het gaat eerst omhoog en daarna weer omlaag",
            "Het gaat geleidelijk naar beneden",
        ],
        antwoord=0,
        uitleg="België klimt van het noordwesten naar het zuidoosten. Aan zee ligt alles nog rond het niveau van de zeespiegel, in de Ardennen zit je honderden meters hoger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten reliëfeenheden onderscheidt men in België?",
        opties=[
            "Laagvlaktes, laagplateaus en plateaus",
            "Bergen, heuvels en dalen",
            "Kustgebied, binnenland en grensstreek",
            "Noord, midden en zuid",
        ],
        antwoord=0,
        uitleg="De laagvlaktes liggen het laagst, in het noorden. Daarboven komen de laagplateaus in het midden van het land, en in het zuiden de plateaus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn laagvlaktes volgens de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "De Kempense Laagvlakte",
            "De Laagvlakte van de Kust",
            "De Vlaamse Laagvlakte",
            "Het Plateau van Herve",
            "Het Lotharings Plateau",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt drie laagvlaktes: de Kempense, die van de Kust en de Vlaamse. Herve en Lotharingen zijn plateaus en liggen veel hoger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn laagplateaus volgens de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "Het Haspengouws Laagplateau",
            "Het Henegouws Laagplateau",
            "Het Brabants Laagplateau",
            "De Fagne-Famennedepressie",
            "Het Plateau van de Ardennen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt vier laagplateaus: het Haspengouwse, het Henegouwse, het Brabantse en het Kempense. De Fagne-Famennedepressie en de Ardennen horen bij de zuidelijke eenheden.",
    ),
    dict(
        type="invultekst",
        vraag="Het hoogste punt van België, het Signaal van Botrange, ligt op het Plateau van de Hoge ___.",
        antwoord="Venen",
        uitleg="Het Signaal van Botrange ligt op 694 meter, op het Plateau van de Hoge Venen in de provincie Luik. Het is een hoogveengebied, geen bergtop.",
    ),
    dict(
        type="waarofniet",
        vraag="De polders liggen in de Laagvlakte van de Kust.",
        antwoord=True,
        uitleg="De polders zijn stukken land op de zee gewonnen, achter de duinen. Ze liggen laag, soms zelfs onder het niveau van de zeespiegel, en worden droog gehouden met dijken en pompen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reliëfeenheid ligt het hoogst?",
        opties=[
            "Het Plateau van de Ardennen",
            "Het Brabants Laagplateau",
            "De Vlaamse Laagvlakte",
            "De Kempense Laagvlakte",
        ],
        antwoord=0,
        uitleg="Het Plateau van de Ardennen en het aangrenzende Plateau van de Hoge Venen zijn de hoogste delen van België. De laagvlaktes in het noorden liggen het laagst.",
    ),
    dict(
        type="waarofniet",
        vraag="De Heuvelruggen van de Condroz vormen een vlak plateau zonder noemenswaardige hoogteverschillen.",
        antwoord=False,
        uitleg="De Condroz is juist géén vlak plateau maar een golvend gebied: harde zandsteenruggen wisselen af met zachtere kalksteendalen. Daardoor ontstond dat ribbelpatroon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klimaatzones noemt de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "Warm",
            "Gematigd",
            "Koud",
            "Bergachtig",
            "Winderig",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche werkt met vijf woorden voor klimaatzones: warm, gematigd, koud, droog en nat. Bergachtig gaat over reliëf, winderig over het weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar op aarde liggen de warmste klimaatzones?",
        opties=[
            "Rond de evenaar",
            "Rond de polen",
            "Rond de poolcirkels",
            "Op het westelijk halfrond",
        ],
        antwoord=0,
        uitleg="Rond de evenaar valt het zonlicht het steilst in, dus warmt het oppervlak er het sterkst op. Naar de polen toe valt het licht steeds schuiner en wordt het kouder.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke klimaatzone ligt België?",
        opties=[
            "De gematigde zone",
            "De warme zone",
            "De koude zone",
            "De droge zone",
        ],
        antwoord=0,
        uitleg="België heeft een gematigd zeeklimaat: zachte winters, koele zomers en het hele jaar door neerslag. De zee vlakt de uitersten af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vegetatiezones volgens de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "De toendra",
            "De taiga",
            "De savanne",
            "Het hoogveen",
            "De polder",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zeven vegetatiezones: toendra, taiga, loofwoud, steppe, savanne, regenwoud en (ijs)woestijn. Hoogveen en polder zijn Belgische landschappen, geen wereldwijde zones.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taiga?",
        opties=[
            "Een brede gordel naaldbos in het noorden",
            "Een grasvlakte met verspreide bomen in de tropen",
            "Een gebied zonder bomen met mossen en korstmossen",
            "Een dicht bos met veel regen dicht bij de evenaar",
        ],
        antwoord=0,
        uitleg="De taiga is het uitgestrekte naaldbos van Rusland, Scandinavië en Canada. Nog noordelijker, waar het te koud wordt voor bomen, begint de toendra.",
    ),
    dict(
        type="invultekst",
        vraag="De vegetatiezone met grasvlakten en verspreide bomen, tussen de woestijn en het regenwoud, heet de ___.",
        antwoord="savanne",
        uitleg="De savanne heeft een nat en een droog seizoen. Er groeit gras met hier en daar een boom, en er leven grote kuddes grazers.",
    ),
    dict(
        type="waarofniet",
        vraag="In de vegetatiezone van het loofwoud ligt ook België.",
        antwoord=True,
        uitleg="Van nature zou een groot deel van België loofbos zijn: beuken, eiken, berken. Dat het er niet meer staat, komt doordat de mens het gekapt heeft voor akkers en steden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom groeien er in een woestijn zo weinig planten?",
        opties=[
            "Omdat er veel te weinig neerslag valt",
            "Omdat de zon er de planten verbrandt",
            "Omdat de bodem er uit vast gesteente bestaat",
            "Omdat het er 's nachts te koud wordt om te groeien",
        ],
        antwoord=0,
        uitleg="Een woestijn is in de eerste plaats droog, niet warm. Ook op Antarctica ligt woestijn: een ijswoestijn, waar het wel koud is maar even weinig neerslag valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de bevolkingsspreiding van de wereld?",
        opties=[
            "Waar veel en waar weinig mensen wonen",
            "Hoeveel mensen er in totaal op aarde leven",
            "Hoe snel de wereldbevolking elk jaar groeit",
            "Waar de mensen naartoe verhuizen en waarom",
        ],
        antwoord=0,
        uitleg="Bevolkingsspreiding is een patroon op de kaart: dichtbevolkte gebieden tegenover gebieden waar bijna niemand woont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebieden zijn van nature dunbevolkt? Er zijn er meerdere juist.",
        opties=[
            "Woestijnen",
            "Hooggebergten",
            "Poolgebieden",
            "Rivierdalen met vruchtbare grond",
            "Kustvlaktes met een gematigd klimaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Waar het te droog, te hoog of te koud is, wonen weinig mensen. Vruchtbare rivierdalen en gematigde kustvlaktes trekken er juist veel aan.",
    ),
    dict(
        type="waarofniet",
        vraag="België is een van de dunstbevolkte landen van Europa.",
        antwoord=False,
        uitleg="Net omgekeerd: België telt veel inwoners op een kleine oppervlakte. Vlaanderen is zelfs een van de dichtstbevolkte streken van het hele werelddeel.",
    ),
    dict(
        type="invultekst",
        vraag="Het aantal inwoners per vierkante kilometer noemt men de bevolkings___.",
        antwoord="dichtheid",
        uitleg="Bevolkingsdichtheid maakt gebieden vergelijkbaar. Een groot land met weinig mensen heeft een lage dichtheid, ook al zijn het er in totaal veel.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In de Ardennen staan veel bossen en in Haspengouw liggen vooral akkers en boomgaarden. Waardoor komt dat verschil?",
        opties=[
            "Door het samenspel van reliëf, bodem en klimaat",
            "Doordat de mensen er andere gewoontes hebben",
            "Doordat de provinciegrens er anders loopt",
            "Doordat er in het zuiden meer toeristen komen",
        ],
        antwoord=0,
        uitleg="Haspengouw heeft een vruchtbare leembodem en een vlak reliëf: ideaal voor akkers en fruit. De Ardennen liggen hoog, zijn kouder en hebben een schrale bodem op vast gesteente, dus daar blijft het bos.",
    ),
    dict(
        type="waarofniet",
        vraag="De landschapsvormende lagen staan los van elkaar en beïnvloeden elkaar niet.",
        antwoord=False,
        uitleg="Ze werken juist op elkaar in. Het reliëf beïnvloedt het klimaat, het klimaat de vegetatie, de bodem de landbouw, en het water bepaalt mee waar mensen gaan wonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe hoger je in een gebergte klimt, hoe minder er groeit. Welke relatie zie je daar?",
        opties=[
            "Tussen het reliëf, het klimaat en de vegetatie",
            "Tussen de bodem, de industrie en de bebouwing",
            "Tussen het water, de ontginning en de recreatie",
            "Tussen de bevolking, de wegen en de landbouw",
        ],
        antwoord=0,
        uitleg="Hoger worden betekent kouder worden. Boven een bepaalde hoogte, de boomgrens, is het te koud voor bomen, en nog hoger blijft alleen rots en sneeuw over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen veel grote steden aan een rivier?",
        opties=[
            "Omdat water drinken, vervoer en handel mogelijk maakte",
            "Omdat rivierwater het bouwen goedkoper maakt",
            "Omdat er langs een rivier nooit overstromingen zijn",
            "Omdat de grond langs een rivier het stevigst is",
        ],
        antwoord=0,
        uitleg="Een rivier gaf drinkwater, een vaarweg, vis en energie voor molens. Daarom groeiden nederzettingen aan het water uit tot steden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de bodem en de landbouw kloppen? Er zijn er meerdere juist.",
        opties=[
            "Een leembodem is vruchtbaar en goed voor akkerbouw",
            "Een natte bodem leent zich eerder voor weiland",
            "Een schrale zandbodem levert minder op per hectare",
            "Op elke bodem groeit precies hetzelfde even goed",
            "De bodem heeft niets met de landbouw te maken",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bodem bepaalt in hoge mate wat rendeert. Op leem staat graan en fruit, op natte grond staat gras met koeien erop, en op arm zand moest er vroeger heide blijven liggen.",
    ),
    dict(
        type="invultekst",
        vraag="De hoogte waarboven het in een gebergte te koud is voor bomen, heet de boom___.",
        antwoord="boomgrens",
        uitleg="Boven de boomgrens vind je nog gras, mos en rots. Hoe verder van de evenaar, hoe lager die grens ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een natuurlijk landschap?",
        opties=[
            "Een landschap dat de mens nauwelijks veranderd heeft",
            "Een landschap waar geen enkele plant groeit",
            "Een landschap dat door de overheid beschermd wordt",
            "Een landschap dat er elk seizoen anders uitziet",
        ],
        antwoord=0,
        uitleg="Echt onaangeroerde landschappen zijn zeldzaam: hoge bergen, poolgebieden, stukken regenwoud. In België is bijna elk landschap door de mens gevormd.",
    ),
    dict(
        type="waarofniet",
        vraag="De polders zijn een voorbeeld van een menselijk landschap.",
        antwoord=True,
        uitleg="De polders bestaan alleen doordat mensen dijken aanlegden en water wegpompten. Zonder dat onderhoud zou de zee een deel ervan terugnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent duurzaamheid?",
        opties=[
            "Voorzien in wat we nu nodig hebben zonder later tekort te doen",
            "Alles wat we gebruiken zo lang mogelijk laten meegaan",
            "Zo weinig mogelijk verplaatsen en zo veel mogelijk thuisblijven",
            "Producten kopen die in eigen land gemaakt werden",
        ],
        antwoord=0,
        uitleg="Duurzaam handelen betekent dat wat je vandaag doet, de volgende generaties niet in de problemen brengt. Het gaat dus niet alleen over spullen langer gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vijf P's van het duurzaamheidsmodel? Er zijn er meerdere juist.",
        opties=[
            "Planet",
            "People",
            "Prosperity",
            "Production",
            "Protection",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf P's zijn Planet, People, Prosperity, Peace en Partnership. Production en Protection horen er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente legt een nieuw bos aan en beschermt een beekvallei. Onder welke P valt dat vooral?",
        opties=[
            "Planet",
            "Prosperity",
            "Peace",
            "Partnership",
        ],
        antwoord=0,
        uitleg="Planet gaat over de aarde zelf: natuur, klimaat, water, bodem, biodiversiteit. Een bos aanleggen is daar een voorbeeld van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf betaalt zijn werknemers een eerlijk loon en zorgt voor veilige werkomstandigheden. Onder welke P valt dat vooral?",
        opties=[
            "People",
            "Planet",
            "Peace",
            "Partnership",
        ],
        antwoord=0,
        uitleg="People gaat over de mensen: gezondheid, onderwijs, gelijke kansen, waardig werk. Wie zijn mensen goed behandelt, werkt aan die P.",
    ),
    dict(
        type="invultekst",
        vraag="De P van het 5P-model die over samenwerkingsverbanden gaat, is ___.",
        antwoord="Partnership",
        uitleg="Partnership betekent dat landen, bedrijven en organisaties samenwerken. Klimaatverandering of armoede lost geen enkel land alleen op.",
    ),
    dict(
        type="waarofniet",
        vraag="De vijf P's hangen samen: wat de ene vooruithelpt, kan de andere tegelijk schaden.",
        antwoord=True,
        uitleg="Ze staan niet los van elkaar. Een fabriek die de rivier vervuilt, kan wel Prosperity dienen, maar schaadt Planet en People tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort vrede in een model over duurzaamheid?",
        opties=[
            "Omdat er in een oorlog niets opgebouwd of beschermd wordt",
            "Omdat vrede voeren altijd goedkoper is dan oorlog voeren",
            "Omdat landen in vrede meer grondstoffen ontginnen",
            "Omdat de natuur zich enkel in vredestijd herstelt",
        ],
        antwoord=0,
        uitleg="Peace staat in het model omdat duurzame ontwikkeling stilvalt bij geweld: scholen sluiten, landbouw stopt, mensen slaan op de vlucht en het landschap raakt verwoest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden passen bij Prosperity, de P van welvaart? Er zijn er meerdere juist.",
        opties=[
            "Iedereen kan werk vinden dat genoeg opbrengt",
            "Er is betaalbare energie voor elk gezin",
            "Bedrijven kunnen hun producten vlot vervoeren",
            "De biodiversiteit in de beekvallei gaat vooruit",
            "Twee landen sluiten vrede na een lang conflict",
        ],
        antwoord=[0, 1, 2],
        uitleg="Prosperity gaat over welvaart: werk, inkomen, energie, economie en infrastructuur. Biodiversiteit hoort bij Planet en vrede sluiten bij Peace.",
    ),
    dict(
        type="waarofniet",
        vraag="Een landschap dat vandaag duurzaam beheerd wordt, blijft daarna vanzelf zo.",
        antwoord=False,
        uitleg="Een landschap blijft veranderen, en de druk erop ook. Duurzaam beheer is werk dat blijft doorlopen, geen eindpunt dat je één keer bereikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee dorpen liggen even ver van de stad, maar het ene groeide veel sterker. Wat is daarvoor de beste verklaring?",
        opties=[
            "Het ene ligt aan een spoorlijn en het andere niet",
            "Het ene heeft een oudere kerk dan het andere",
            "Het ene ligt op de zonzijde van de heuvel",
            "Het ene heeft een langere naam dan het andere",
        ],
        antwoord=0,
        uitleg="Bereikbaarheid is een van de sterkste verklaringen voor groei. Wie vlot naar de stad kan sporen, gaat er wonen; zonder verbinding blijft een dorp klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijken twee landschappen met hetzelfde klimaat soms toch heel verschillend?",
        opties=[
            "Omdat de andere lagen er anders zijn",
            "Omdat het klimaat elke tien jaar verandert",
            "Omdat er in het ene meer regen valt dan in het andere",
            "Omdat men er een andere taal spreekt",
        ],
        antwoord=0,
        uitleg="Klimaat is maar één laag. Bij hetzelfde klimaat kunnen het reliëf, de bodem, het water en vooral het landgebruik grondig verschillen.",
    ),
    dict(
        type="invultekst",
        vraag="Een landschap dat vrijwel volledig door mensen gevormd is, noem je een ___ landschap.",
        antwoord="menselijk",
        uitleg="Een polder, een havengebied of een verkaveling zijn menselijke landschappen. Het tegenovergestelde is een natuurlijk landschap.",
    ),
]

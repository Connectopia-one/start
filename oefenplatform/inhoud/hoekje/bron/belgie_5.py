# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Geschiedenis van België, deel 5: Gemini-reeks 4 van Kim, aangevuld.

Van de tien vragen uit Kims Gemini-reeks 4 (26 oktober 2026) stonden er vijf
al in deel 1 tot 4: de koning-soldaat, de Koningskwestie, de taalgrens, de
Boerenkrijg en de staatshervormingen. Gemini gaf bij de wereldtentoonstelling
van 1935 een fout antwoord; die vraag is herschreven rond wat er toen
werkelijk gevierd werd. Nieuw zijn Jacob van Artevelde, de Blijde Inkomst,
het verdrag van Verdun, de slag bij Leuven en de tentoonstelling van 1935, met
vijftien eigen vragen erbij.
"""

VAK = "Geschiedenis van België"
BESTAND = "geschiedenis-van-belgie.json"
TITEL = "Graven, geleerden en wereldtentoonstellingen"
VOLGORDE = 5

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": r"In \(843\) werd het rijk van Karel de Grote onder zijn drie kleinzonen verdeeld. Hoe heet dat verdrag?",
        "opties": [
            "Het verdrag van Verdun",
            "Het verdrag van Utrecht",
            "Het verdrag van Westfalen",
            "Het verdrag van Versailles",
        ],
        "antwoord": 0,
        "uitleg": r"Er kwam een westelijk rijk, waaruit later Frankrijk groeide, een oostelijk rijk, het latere Duitsland, en een smalle strook ertussen. De Schelde werd een grens: Vlaanderen ten westen ervan hoorde bij het westen, Brabant ten oosten bij de middenstrook. Die verdeling verklaart waarom onze gewesten eeuwenlang tussen twee grote buren in lagen. De andere verdragen kwamen veel later: Utrecht in \(1713\), Westfalen in \(1648\) en Versailles in \(1919\).",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In \(891\) versloeg de Oost-Frankische koning Arnulf bij Leuven een leger. Wie waren zijn tegenstanders?",
        "opties": [
            "Vikingen, die al jaren langs de rivieren plunderden",
            "Romeinen, die hun oude gebied wilden heroveren",
            "Spanjaarden, die de Nederlanden kwamen bezetten",
            "Hunnen, die vanuit het oosten Europa binnenvielen",
        ],
        "antwoord": 0,
        "uitleg": "De Vikingen voeren met hun platte schepen ver de rivieren op en hadden een kamp aan de Dijle. Arnulf van Karinthië viel het aan, en volgens de kronieken kleurde de Dijle rood. Daarna werden de Vikingaanvallen in onze streken veel zeldzamer. De Romeinen waren toen al vier eeuwen weg, en de Spanjaarden kwamen pas zevenhonderd jaar later.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In de veertiende eeuw sloot de Gentse leider Jacob van Artevelde vriendschap met Engeland, tegen de wil van de graaf van Vlaanderen. Waarom?",
        "opties": [
            "De Gentse weverijen hadden Engelse wol nodig om te kunnen draaien",
            "Hij wilde zelf koning van Engeland worden na de dood van de vorst",
            "Engeland had beloofd om Gent een eigen haven aan zee te geven",
            "De graaf was zelf een Engelsman en had Gent aan Frankrijk verkocht",
        ],
        "antwoord": 0,
        "uitleg": r"Gent was een van de grootste steden van Europa, en bijna iedereen leefde er van laken. De wol daarvoor kwam uit Engeland. Toen de graaf de kant van Frankrijk koos en de Engelse koning de wol tegenhield, stonden de weefgetouwen stil. Van Artevelde koos daarom voor de handel met Engeland en bestuurde Vlaanderen jarenlang zowat zelf. In \(1345\) werd hij in Gent zelf vermoord. Zijn standbeeld staat op de Vrijdagmarkt.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Wat was de Blijde Inkomst die de hertogin van Brabant in \(1356\) moest zweren?",
        "opties": [
            "Een oorkonde met de rechten van de steden die de vorst moest respecteren",
            "Een feeststoet waarmee de hertogin voor het eerst Brussel binnenreed",
            "Een belasting die elke stad betaalde als er een nieuwe vorst kwam",
            "Een vredesverdrag waarmee Brabant zich bij Vlaanderen aansloot",
        ],
        "antwoord": 0,
        "uitleg": "Hertogin Johanna en haar man Wenceslas kregen Brabant pas nadat ze plechtig beloofden de rechten van de steden en hun inwoners te eerbiedigen. Hielden ze zich er niet aan, dan mochten de onderdanen hun gehoorzaamheid opzeggen. Elke nieuwe hertog moest die belofte opnieuw zweren, tot het einde van de achttiende eeuw. De naam klinkt als een feest, en de intocht was dat ook, maar het was vooral een contract.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is Maria van Bourgondië, die in 1482 na een val van haar paard stierf, zo belangrijk voor onze geschiedenis?",
        "opties": [
            "Door haar huwelijk kwamen de Nederlanden in handen van de Habsburgers",
            "Ze stichtte de universiteit van Leuven met het geld van haar vader",
            "Ze verkocht Vlaanderen voor een flinke som aan de Franse koning",
            "Ze was de eerste vrouw die in Brugge tot burgemeester gekozen werd",
        ],
        "antwoord": 0,
        "uitleg": r"Maria was de enige erfgename van de rijke Bourgondische hertogen. Ze trouwde met Maximiliaan van Oostenrijk, een Habsburger. Hun kleinzoon was keizer Karel, geboren in Gent, en zijn zoon Filips II, de koning van Spanje. Zo kwamen onze gewesten bij het Spaanse rijk terecht, met alle gevolgen van dien. Maria ligt begraven in de Onze-Lieve-Vrouwekerk in Brugge. De universiteit van Leuven bestond al sinds \(1425\), van voor haar geboorte.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Andreas Vesalius uit Brussel publiceerde in \(1543\) een boek dat de geneeskunde veranderde. Waarover ging het?",
        "opties": [
            "Over de bouw van het menselijk lichaam, getekend na eigen ontleding",
            "Over de planeten die rond de zon draaien in plaats van rond de aarde",
            "Over het slijpen van glas tot brillen en de eerste vergrootglazen",
            "Over de pest en hoe je je met kruiden tegen besmetting beschermt",
        ],
        "antwoord": 0,
        "uitleg": r"Dokters lazen eeuwenlang wat de Griekse arts Galenus schreef, die vooral apen en varkens had opengesneden. Vesalius deed het zelf, bij mensen, en tekende alles heel precies na: spieren, botten, bloedvaten. Hij vond zo honderden fouten bij Galenus. In datzelfde jaar \(1543\) verscheen ook het boek van Copernicus over de zon in het midden: een topjaar voor de wetenschap.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De Vlaming Gerard Mercator, geboren in Rupelmonde, maakte iets wat we vandaag nog elke dag gebruiken. Wat?",
        "opties": [
            "Een manier om de bolle aarde plat op een kaart te tekenen",
            "Het kompas met een naald die op een puntje kan draaien",
            "Een tabel om de tijd in elk land ter wereld uit te rekenen",
            "Een kijker om op zee de sterren te volgen en de weg te vinden",
        ],
        "antwoord": 0,
        "uitleg": r"Een sinaasappelschil kun je niet plat leggen zonder te scheuren of te rekken. Mercator koos in \(1569\) om te rekken, zo dat een rechte koerslijn op zijn kaart ook op zee een vaste kompasrichting is. Zeelui waren er dol op. De keerzijde: landen ver van de evenaar lijken veel te groot, Groenland lijkt zo groot als Afrika terwijl Afrika veertien keer groter is. Kaartapps op je gsm gebruiken nog altijd een versie ervan.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het woord atlas voor een boek vol landkaarten komt van Mercator.",
        "antwoord": True,
        "uitleg": r"Mercator noemde zijn verzameling kaarten naar Atlas, een mythische koning die volgens hem de eerste hemelbol had gemaakt. Zijn boek verscheen in \(1595\), een jaar na zijn dood. Sindsdien heet elk kaartenboek een atlas.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Wat gebeurde er in de zomer van \(1566\) tijdens de Beeldenstorm?",
        "opties": [
            "Protestanten vernielden beelden en schilderijen in de kerken",
            "Een orkaan blies de beelden van de Brugse belforttoren omver",
            "Kunstenaars gingen de straat op om meer loon te eisen",
            "De Spaanse koning liet alle bronzen beelden smelten tot kanonnen",
        ],
        "antwoord": 0,
        "uitleg": "Het begon in augustus in de Westhoek en ging als een lopend vuurtje door de Nederlanden. Volgens de protestanten hoorden beelden van heiligen niet in een kerk. Filips II zag het als opstand en stuurde de hertog van Alva met een leger. Dat was het begin van de Tachtigjarige Oorlog, die de Nederlanden uiteindelijk in een noordelijk en een zuidelijk deel zou splitsen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Brussel is altijd de hoofdstad geweest van het gebied dat nu België is.",
        "antwoord": False,
        "uitleg": r"Een land België bestond pas vanaf \(1830\), dus er was ook geen vaste hoofdstad. De graven van Vlaanderen zaten vaak in Gent of Brugge, en onder Margareta van Oostenrijk was Mechelen in het begin van de zestiende eeuw de hoofdstad van de Nederlanden. Brussel werd pas onder de Bourgondiërs en de Habsburgers de belangrijkste hofstad.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Onze streken worden het slagveld van Europa genoemd. Waarom?",
        "opties": [
            "Buitenlandse legers vochten hier eeuwenlang hun grote veldslagen uit",
            "Onze vorsten voerden zelf meer oorlogen dan alle buurlanden samen",
            "Er staan hier meer burchten en kastelen dan in elk ander land",
            "Het Belgische leger was eeuwenlang het grootste van heel Europa",
        ],
        "antwoord": 0,
        "uitleg": "Vlak, rijk en precies tussen Frankrijk, Engeland, Duitsland en Nederland in: wie elkaar wilde bevechten, deed dat vaak hier. Denk aan Kortrijk in 1302, Waterloo in 1815, Ieper in de Eerste en het Ardennenoffensief in de Tweede Wereldoorlog. Bijna altijd vochten er vreemde legers, die zelf van heel ergens anders kwamen.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Wat bedacht de Belg Zénobe Gramme rond \(1870\)?",
        "opties": [
            "Een dynamo die genoeg stroom leverde om fabrieken te laten draaien",
            "De eerste gloeilamp die urenlang bleef branden zonder te springen",
            "Een batterij die je met een hendel weer met de hand kon opladen",
            "De eerste telefoonlijn, die Luik en Brussel met elkaar verbond",
        ],
        "antwoord": 0,
        "uitleg": "Gramme was een schrijnwerker uit de buurt van Hoei die zich in Parijs met elektriciteit bezighield. Zijn dynamo zette draaiende beweging om in een gelijkmatige stroom, en dat was het begin van elektriciteit voor fabrieken en straatverlichting. Draai je de machine om en stuur je er stroom door, dan wordt ze een motor. Zijn naam staat op de Eiffeltoren, als een van de tweeënzeventig geleerden die daar geëerd worden.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Het Belgische volkslied, de Brabançonne, ontstond tijdens de opstand van \(1830\).",
        "antwoord": True,
        "uitleg": "De tekst werd in september 1830 geschreven door Jenneval, een Franse acteur die in Brussel speelde. Hij sneuvelde een paar weken later zelf in de gevechten. De tekst is daarna een paar keer herschreven, ook om hem minder vijandig tegen Nederland te maken. Er bestaat een Nederlandse, een Franse en een Duitse versie.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In de nacht van \(25\) augustus \(1914\) ging de universiteitsbibliotheek van Leuven in vlammen op. Wie stak ze in brand?",
        "opties": [
            "Duitse soldaten, als wraakactie tijdens hun inval in België",
            "Belgische soldaten, om de boeken niet in vijandelijke handen te laten",
            "Studenten, uit protest tegen het bestuur van hun universiteit",
            "Niemand, het was een blikseminslag tijdens een zomerstorm",
        ],
        "antwoord": 0,
        "uitleg": r"Na een vals alarm over Belgische sluipschutters staken Duitse troepen een groot deel van Leuven in brand. Zo'n \(250\) inwoners kwamen om, en de bibliotheek verloor honderdduizenden boeken en eeuwenoude handschriften. De hele wereld was geschokt. Met geld uit Amerika werd een nieuwe bibliotheek gebouwd, en die brandde in \(1940\) opnieuw af.",
    },
    {
        "type": "invultekst",
        "vraag": "In welke stad staat het belfort met de vergulde draak bovenop?",
        "antwoord": "Gent",
        "uitleg": "De draak waakt al sinds de veertiende eeuw over Gent, als symbool van de macht en de vrijheid van de stad. In het belfort bewaarden de Gentenaars hun belangrijkste oorkonden, achter dikke deuren en sloten. Volgens een legende komt de draak uit Brugge, als buit, maar daar is geen bewijs voor.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het Manneken Pis dat je in Brussel op de hoek van de straat ziet, is een kopie.",
        "antwoord": True,
        "uitleg": r"Het origineel van Jérôme Duquesnoy uit \(1619\) werd zo vaak gestolen en beschadigd dat het in een museum op de Grote Markt veilig bewaard wordt. Op straat staat sinds \(1965\) een kopie. Het mannetje heeft wel meer dan duizend eigen kostuums gekregen, van brandweerman tot astronaut.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Olympische Spelen zijn nog nooit in België gehouden.",
        "antwoord": False,
        "uitleg": r"In \(1920\) vonden de Zomerspelen in Antwerpen plaats, twee jaar na de Eerste Wereldoorlog. Voor het eerst werd er toen een olympische eed afgelegd en wapperde de vlag met de vijf ringen. Duitsland en zijn bondgenoten mochten niet meedoen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wie was Pater Damiaan uit Tremelo?",
        "opties": [
            "Een priester die op Hawaï voor melaatsen zorgde en zelf ziek werd",
            "Een monnik die in Brugge het eerste ziekenhuis van Europa stichtte",
            "Een missionaris die als eerste Europeaan de bron van de Kongo vond",
            "Een Leuvense geleerde die een geneesmiddel tegen de pest uitvond",
        ],
        "antwoord": 0,
        "uitleg": r"Jozef De Veuster trok in \(1873\) naar het eiland Molokai, waar zieken met lepra werden achtergelaten. Hij bouwde er huizen, een school en een kerk, verzorgde de zieken en begroef de doden. Na zestien jaar stierf hij zelf aan de ziekte. In \(2005\) werd hij bij een televisiewedstrijd van de VRT verkozen tot de grootste Belg.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"De wereldtentoonstelling van \(1935\) op de Heizel in Brussel vierde een eeuwfeest. Welk?",
        "opties": [
            "Honderd jaar trein, sinds de eerste spoorlijn van Brussel naar Mechelen",
            "Honderd jaar België, sinds de opstand en de onafhankelijkheid van 1830",
            "Honderd jaar stemrecht voor alle Belgische mannen en vrouwen samen",
            "Honderd jaar Atomium, het bekendste bouwwerk op de vlakte van de Heizel",
        ],
        "antwoord": 0,
        "uitleg": r"In \(1835\) reed de eerste trein van het Europese vasteland tussen Brussel en Mechelen, en dat werd honderd jaar later groots gevierd. Voor de tentoonstelling bouwde men de grote paleizen van de Heizel, die vandaag nog dienen voor beurzen. Honderd jaar België was al in \(1930\) gevierd, met tentoonstellingen in Antwerpen en Luik. Het Atomium kwam pas bij Expo \(58\).",
    },
    {
        "type": "invultekst",
        "vraag": r"Hoeveel provincies telt België sinds Brabant in \(1995\) in twee gesplitst werd? Geef een getal.",
        "antwoord": "10",
        "uitleg": "Vijf Vlaamse: West-Vlaanderen, Oost-Vlaanderen, Antwerpen, Vlaams-Brabant en Limburg. Vijf Waalse: Henegouwen, Namen, Luik, Luxemburg en Waals-Brabant. Brussel hoort sindsdien bij geen enkele provincie. Vóór de splitsing waren het er negen.",
    },
]

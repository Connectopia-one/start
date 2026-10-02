# -*- coding: utf-8 -*-
"""De Eerste Wereldoorlog en de Vrede van Versailles.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de oorzaken en
de aanleiding van de oorlog, het verloop aan het front en in bezet België, de
oorlog als totale oorlog, en de vrede van 1919 met haar gevolgen.

Deel 1 gaat over de weg naar de oorlog en over het front. Deel 2 gaat over het
leven in bezet land, het einde van de oorlog en de vrede van Versailles.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke oorzaken van de Eerste Wereldoorlog worden doorgaans aangewezen?",
        opties=[
            "de bondgenootschappen tussen de mogendheden",
            "de wapenwedloop tussen de grote legers",
            "de afschaffing van het leger in Duitsland en in Frankrijk",
            "het gebrek aan belangstelling voor kolonies in Europa",
        ],
        antwoord=[0, 1],
        uitleg="Twee kampen tegenover elkaar, en elk land dat zijn leger en vloot uitbouwde. Daar komen het nationalisme en de wedloop om kolonies bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de aanleiding van de Eerste Wereldoorlog?",
        opties=[
            "de moord op de Oostenrijkse troonopvolger in Sarajevo",
            "de inval van het Duitse leger in België in augustus",
            "de revolutie van de arbeiders in het Russische rijk",
            "de weigering van Frankrijk om Elzas af te staan",
        ],
        antwoord=0,
        uitleg="Die moord in juni 1914 zette de verdragen in werking. Binnen vijf weken stond half Europa in oorlog.",
    ),
    dict(
        type="invultekst",
        vraag="In welke stad werd in juni 1914 de Oostenrijkse troonopvolger doodgeschoten?",
        antwoord=["Sarajevo", "in Sarajevo"],
        uitleg="De stad lag in Bosnië, dat Oostenrijk-Hongarije kort daarvoor had ingelijfd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de Balkan voor 1914 het kruitvat van Europa?",
        opties=[
            "staten en mogendheden botsten er over hetzelfde gebied",
            "er lagen de grootste kruitfabrieken van het hele werelddeel",
            "er werd het meeste geld aan legers en wapens uitgegeven",
            "er was geen enkele staat die een eigen leger bezat",
        ],
        antwoord=0,
        uitleg="Het Ottomaanse rijk viel er terug, en Rusland en Oostenrijk-Hongarije wilden er beide invloed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom viel het Duitse leger in augustus 1914 België binnen?",
        opties=[
            "om Frankrijk langs het noorden snel te kunnen verslaan",
            "om de Belgische steenkoolmijnen in handen te krijgen",
            "om de Belgische koning van zijn troon te stoten",
            "om Congo van de Belgische staat af te nemen",
        ],
        antwoord=0,
        uitleg="Dat was de kern van het Duitse oorlogsplan. De Belgische neutraliteit woog daar niet tegen op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed de Belgische regering met het Duitse ultimatum van augustus 1914?",
        opties=[
            "zij wees het af en liet het leger zich verzetten",
            "zij aanvaardde het en liet de troepen vrij door",
            "zij vroeg de Volkenbond om tussen te komen",
            "zij verklaarde Frankrijk daarop de oorlog",
        ],
        antwoord=0,
        uitleg="Die weigering bracht Groot-Brittannië in de oorlog, want het had de Belgische neutraliteit gewaarborgd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar kwam het Belgische front in het najaar van 1914 tot stilstand?",
        opties=[
            "achter de IJzer, in de Westhoek",
            "achter de Maas, bij Luik en Namen",
            "achter de Schelde, bij Antwerpen",
            "achter de Samber, bij Charleroi",
        ],
        antwoord=0,
        uitleg="Door de vlakte onder water te zetten kon men de laatste strook België vier jaar lang houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe hielden de Belgen het Duitse leger aan de IJzer tegen?",
        opties=[
            "zij zetten de vlakte achter de rivier onder water",
            "zij bouwden er een betonnen muur dwars door het land",
            "zij staken de bruggen over de IJzer in brand",
            "zij lieten het Franse leger de stelling overnemen",
        ],
        antwoord=0,
        uitleg="Met de sluizen bij Nieuwpoort en het getij van de zee werd de vlakte onbegaanbaar voor een leger.",
    ),
    dict(
        type="invultekst",
        vraag="Welke rivier werd de frontlijn in het onbezette stukje België?",
        antwoord=["de IJzer", "IJzer"],
        uitleg="Het front liep van Nieuwpoort tot Ieper. Daarachter lag een kleine strook vrij België.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een loopgravenoorlog?",
        opties=[
            "de legers liggen maanden in stellingen zonder veel te vorderen",
            "de legers trekken snel met ruiters en voertuigen door het land",
            "de legers vechten uitsluitend op zee en in de lucht",
            "de legers sluiten na elke veldslag meteen een wapenstilstand",
        ],
        antwoord=0,
        uitleg="De verdediging was sterker dan de aanval. Daarom kostte elke honderd meter duizenden mensenlevens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nieuwe wapens werden in de Eerste Wereldoorlog ingezet?",
        opties=[
            "gifgas en de mitrailleur",
            "de tank en het vliegtuig",
            "de atoombom en de raket",
            "het kruisboog en het ridderzwaard",
        ],
        antwoord=[0, 1],
        uitleg="De atoombom en de raket komen uit de Tweede Wereldoorlog. Hier ging de techniek al over in massavernietiging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar werd in april 1915 voor het eerst op grote schaal gifgas gebruikt?",
        opties=[
            "bij Ieper, aan het front in de Westhoek",
            "bij Verdun, aan het front in Lotharingen",
            "bij de Somme, aan het front in Picardië",
            "bij Gallipoli, aan de kust van Turkije",
        ],
        antwoord=0,
        uitleg="Daardoor draagt een van die gassen nog altijd de naam van de stad: mosterdgas heet ook yperiet.",
    ),
    dict(
        type="waarofniet",
        vraag="België werd in 1914 binnengevallen hoewel zijn neutraliteit door verdragen gewaarborgd was.",
        antwoord=True,
        uitleg="Die waarborg uit 1839 bleek een papieren waarborg. Het militaire plan woog zwaarder.",
    ),
    dict(
        type="waarofniet",
        vraag="De Eerste Wereldoorlog was na enkele maanden beslist.",
        antwoord=False,
        uitleg="Men verwachtte een korte oorlog, maar het front kwam vast te liggen en het duurde vier jaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Aan de IJzer bleef een klein deel van België onbezet.",
        antwoord=True,
        uitleg="Daar bleven de koning en het leger. De regering zelf week uit naar Frankrijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Belgische leger vocht in de Eerste Wereldoorlog aan de zijde van Duitsland.",
        antwoord=False,
        uitleg="Het vocht tegen de inval, aan de kant van Frankrijk en Groot-Brittannië.",
    ),
    dict(
        type="waarofniet",
        vraag="De nieuwe wapens maakten de aanval veel gemakkelijker dan de verdediging.",
        antwoord=False,
        uitleg="Het omgekeerde: mitrailleurs en prikkeldraad maakten een aanval over open veld haast zinloos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het front in de Westhoek kloppen?",
        opties=[
            "de soldaten leefden maanden in loopgraven met modder en ratten",
            "de stad Ieper werd in de oorlog bijna volledig verwoest",
            "het front verschoof er elke week over tientallen kilometers",
            "er werd aan dat front geen enkel nieuw wapen uitgeprobeerd",
        ],
        antwoord=[0, 1],
        uitleg="Het front lag er jarenlang bijna stil, en juist daar werd het gifgas als eerste ingezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een foto van soldaten in een loopgraaf met gasmaskers op. Uit welke oorlog komt die?",
        opties=[
            "uit de Eerste Wereldoorlog",
            "uit de Frans-Duitse oorlog van 1870",
            "uit de Tiendaagse Veldtocht van 1831",
            "uit de Golfoorlog van de jaren negentig",
        ],
        antwoord=0,
        uitleg="Loopgraaf en gasmasker samen zijn het beeld bij uitstek van de oorlog van 1914 tot 1918.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de Eerste Wereldoorlog een wereldoorlog?",
        opties=[
            "er werd ook buiten Europa gevochten en kolonies werden ingezet",
            "alle landen van de wereld hebben eraan deelgenomen",
            "de oorlog werd uitsluitend op de wereldzeeën uitgevochten",
            "de oorlog begon tegelijk in alle werelddelen van de aarde",
        ],
        antwoord=0,
        uitleg="Er werd gevochten in Afrika, in het Midden-Oosten en op zee, en soldaten kwamen uit alle werelddelen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat de Eerste Wereldoorlog een totale oorlog was?",
        opties=[
            "de hele samenleving en economie werden op de oorlog gericht",
            "er werd op alle continenten van de aarde tegelijk gevochten",
            "alle wapens die bestonden werden tegelijk ingezet",
            "alle legers werden na de oorlog volledig afgeschaft",
        ],
        antwoord=0,
        uitleg="Fabrieken maakten wapens, de staat regelde de voedselvoorraad en de pers werd gecensureerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen had de totale oorlog voor de vrouwen in Europa?",
        opties=[
            "zij namen in de fabrieken het werk van de soldaten over",
            "zij werkten in de hospitalen en de hulpdiensten achter het front",
            "zij kregen tijdens de oorlog overal het stemrecht toegekend",
            "zij werden door de wet uit elke fabriek geweerd",
        ],
        antwoord=[0, 1],
        uitleg="Hun werk tijdens de oorlog versterkte na 1918 wel het pleidooi voor vrouwenstemrecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is propaganda in oorlogstijd?",
        opties=[
            "berichten die de eigen zaak mooi voorstellen",
            "berichten die de feiten zo nauwkeurig mogelijk weergeven",
            "berichten van het leger aan zijn eigen officieren",
            "berichten van het Rode Kruis over de krijgsgevangenen",
        ],
        antwoord=0,
        uitleg="De eigen zaak wordt mooi en de vijand lelijk. Een affiche uit 1915 is dus een bron over de beeldvorming, niet over de feiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe leefde de bevolking in bezet België?",
        opties=[
            "met voedselschaarste, opeisingen en gedwongen arbeid",
            "ongeveer zoals voor de oorlog, want de bezetter liet alles",
            "met vrije verkiezingen voor een eigen parlement",
            "met een volledig open grens naar Nederland en Frankrijk",
        ],
        antwoord=0,
        uitleg="Duizenden werkloze Belgen werden naar Duitsland gedeporteerd om er te werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de Flamenpolitik van de Duitse bezetter?",
        opties=[
            "de Vlaamse eisen steunen om België te verdelen",
            "de Vlaamse taal in het hele land verbieden",
            "de Vlamingen uit het Belgische leger weren",
            "de Vlaamse bevolking naar Duitsland overbrengen",
        ],
        antwoord=0,
        uitleg="Zo vergunde de bezetter de vernederlandsing van de universiteit van Gent. Wie meewerkte, heette activist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de Frontbeweging aan de IJzer?",
        opties=[
            "Vlaamse soldaten met taaleisen in het leger",
            "Duitse soldaten die het front wilden verlaten",
            "Waalse soldaten die een eigen leger wilden vormen",
            "burgers die aan het front voedsel gingen verdelen",
        ],
        antwoord=0,
        uitleg="Bevelen in het Frans aan Nederlandstalige soldaten zorgden voor wrok. Die werkte na de oorlog door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebeurtenissen van 1917 veranderden de loop van de oorlog?",
        opties=[
            "de Verenigde Staten kwamen in de oorlog",
            "in Rusland brak een revolutie uit",
            "Duitsland sloot vrede met Frankrijk en Groot-Brittannië",
            "Italië en Spanje verklaarden samen de oorlog aan Duitsland",
        ],
        antwoord=[0, 1],
        uitleg="Rusland viel uit de oorlog weg, dus kon Duitsland troepen uit het oosten halen. Tegelijk kwam er een frisse tegenstander bij.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke datum van 1918 werd de wapenstilstand gesloten?",
        antwoord=["11 november", "11 november 1918", "11/11"],
        uitleg="Nog altijd een feestdag in België. Het verdrag met de vredesvoorwaarden volgde pas het jaar daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar werd in 1919 het vredesverdrag met Duitsland gesloten?",
        opties=[
            "in Versailles, bij Parijs",
            "in Wenen, in Oostenrijk",
            "in Berlijn, in Duitsland",
            "in Londen, in Engeland",
        ],
        antwoord=0,
        uitleg="Dat Duitsland de voorwaarden niet mocht bespreken maar enkel ondertekenen, werd er zwaar aangerekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden legde het Verdrag van Versailles aan Duitsland op?",
        opties=[
            "het moest herstelbetalingen doen voor de aangerichte schade",
            "het mocht enkel nog een klein leger op de been houden",
            "het mocht zijn kolonies in Afrika en Azië behouden",
            "het mocht zelf de hoogte van de schadevergoeding bepalen",
        ],
        antwoord=[0, 1],
        uitleg="De kolonies werden als mandaatgebied onder de overwinnaars verdeeld. België kreeg Ruanda-Urundi.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk artikel van het Verdrag van Versailles werd in Duitsland het zwaarst ervaren?",
        opties=[
            "het artikel dat Duitsland de schuld van de oorlog gaf",
            "het artikel dat de Volkenbond in Genève oprichtte",
            "het artikel dat de nieuwe staten in Europa erkende",
            "het artikel dat de scheepvaart op de Rijn vrij maakte",
        ],
        antwoord=0,
        uitleg="Op die schuld steunden de herstelbetalingen. In Duitsland sprak men van een dictaat, niet van een vrede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebieden kreeg België na de Eerste Wereldoorlog?",
        opties=[
            "Eupen en Malmedy, en Ruanda-Urundi",
            "Luxemburg en Nederlands Limburg in hun geheel",
            "de Elzas en Lotharingen aan de Franse grens",
            "een deel van het Rijnland met de stad Keulen",
        ],
        antwoord=0,
        uitleg="De Elzas en Lotharingen gingen naar Frankrijk. Het Rijnland bleef Duits, maar zonder leger.",
    ),
    dict(
        type="invultekst",
        vraag="Welke internationale organisatie werd na de Eerste Wereldoorlog opgericht om oorlog te voorkomen?",
        antwoord=["de Volkenbond", "Volkenbond"],
        uitleg="Zij vergaderde in Genève. Dat de Verenigde Staten er niet bij waren, maakte haar van het begin af aan zwak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijken verdwenen door de Eerste Wereldoorlog?",
        opties=[
            "het Oostenrijks-Hongaarse en het Ottomaanse rijk",
            "het Russische en het Duitse keizerrijk",
            "het Britse en het Franse koloniale rijk",
            "het Spaanse en het Portugese koloniale rijk",
        ],
        antwoord=[0, 1],
        uitleg="Uit de brokstukken ontstonden nieuwe staten in Midden-Europa, vaak met minderheden binnen hun grenzen.",
    ),
    dict(
        type="waarofniet",
        vraag="Duitsland mocht in Versailles over de vredesvoorwaarden onderhandelen.",
        antwoord=False,
        uitleg="Het mocht enkel ondertekenen. Daarom werd het verdrag er als een dictaat ervaren.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Verdrag van Versailles legde Duitsland herstelbetalingen op.",
        antwoord=True,
        uitleg="De som was zo hoog dat ze de Duitse economie jarenlang is blijven bezwaren.",
    ),
    dict(
        type="waarofniet",
        vraag="De Verenigde Staten waren lid van de Volkenbond die zij zelf hadden voorgesteld.",
        antwoord=False,
        uitleg="Hun senaat weigerde het verdrag. Daardoor miste de Volkenbond haar sterkste lid.",
    ),
    dict(
        type="waarofniet",
        vraag="Het verdrag van 1919 heeft in Duitsland wrok nagelaten die later politiek gebruikt werd.",
        antwoord=True,
        uitleg="Het dictaat van Versailles werd een vast thema van wie de republiek wilde afbreken.",
    ),
    dict(
        type="waarofniet",
        vraag="Na de Eerste Wereldoorlog bleven de grenzen in Midden-Europa precies dezelfde.",
        antwoord=False,
        uitleg="Er kwamen nieuwe staten als Polen, Tsjechoslowakije en Joegoslavië op de kaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een Duitse krant uit 1920 die over het dictaat van Versailles spreekt. Wat leer je daaruit?",
        opties=[
            "hoe het verdrag in Duitsland werd ervaren en gebruikt",
            "wat er precies in de artikelen van het verdrag stond",
            "wat de overwinnaars met hun voorwaarden bedoelden",
            "hoeveel de herstelbetalingen uiteindelijk hebben opgebracht",
        ],
        antwoord=0,
        uitleg="Voor de inhoud lees je het verdrag zelf. Zo'n krant vertelt je hoe erover gesproken werd.",
    ),
]

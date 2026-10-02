# -*- coding: utf-8 -*-
"""Het interbellum: de opkomst van het totalitarisme.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de periode
tussen de twee wereldoorlogen, met de Russische revolutie en de Sovjet-Unie, het
fascisme in Italië, de wereldcrisis van de jaren dertig, nazi-Duitsland en de
weg naar een nieuwe oorlog.

Deel 1 gaat over de revolutie in Rusland, over Italië en over de crisis. Deel 2
gaat over nazi-Duitsland, over de kenmerken van een totalitaire staat en over de
jaren voor 1939.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de periode tussen de twee wereldoorlogen?",
        opties=[
            "het interbellum",
            "de restauratie",
            "de belle époque",
            "de wederopbouw",
        ],
        antwoord=0,
        uitleg="Letterlijk: tussen de oorlogen. Het loopt van 1918 tot 1939.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1917 in Rusland?",
        opties=[
            "de tsaar verdween en de bolsjewieken namen de macht",
            "de tsaar voerde het algemeen stemrecht voor mannen in",
            "het land werd door Duitsland volledig bezet",
            "het land sloot zich bij de Volkenbond aan",
        ],
        antwoord=0,
        uitleg="Eerst viel de tsaar, en later dat jaar namen de bolsjewieken van Lenin de macht over.",
    ),
    dict(
        type="invultekst",
        vraag="Wie leidde in 1917 de bolsjewieken bij de machtsovername in Rusland?",
        antwoord=["Lenin", "Vladimir Lenin"],
        uitleg="Hij paste het marxisme aan zijn land aan: een kleine, strak geleide partij nam de macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed Stalin met de economie van de Sovjet-Unie?",
        opties=[
            "hij liet ze door de staat plannen in vijfjarenplannen",
            "hij liet ze volledig aan de vrije markt over",
            "hij gaf de fabrieken aan hun vroegere eigenaars terug",
            "hij maakte van het land een louter landbouwstaat",
        ],
        antwoord=0,
        uitleg="Zware industrie kwam eerst, koopwaren voor de mensen kwamen laatst. De groei was echt, de prijs enorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de collectivisering van de landbouw onder Stalin?",
        opties=[
            "de boeren moesten hun grond en vee inbrengen",
            "de boeren kregen eigen grond van de staat in bezit",
            "de boeren mochten hun oogst vrij op de markt verkopen",
            "de boeren werden van alle belastingen vrijgesteld",
        ],
        antwoord=0,
        uitleg="Alles ging naar grote staatsbedrijven. Wie zich verzette, werd verbannen of gedood; in Oekraïne volgde een hongersnood met miljoenen doden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen gebruikte Stalin om zijn macht te verzekeren?",
        opties=[
            "een geheime politie die tegenstanders oppakte",
            "werkkampen waar gevangenen dwangarbeid deden",
            "vrije verkiezingen met verschillende partijen",
            "een vrije pers die de partij mocht bekritiseren",
        ],
        antwoord=[0, 1],
        uitleg="Tijdens de Grote Terreur werden ook partijleiders en officieren zelf opgepakt en gedood.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie kwam in 1922 in Italië aan de macht?",
        opties=[
            "Benito Mussolini",
            "Adolf Hitler",
            "Francisco Franco",
            "Jozef Stalin",
        ],
        antwoord=0,
        uitleg="Na een mars van zijn aanhangers naar Rome werd hij door de koning tot regeringsleider benoemd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het fascisme van Mussolini?",
        opties=[
            "één partij, één leider en geen enkele oppositie",
            "een parlement met verschillende partijen naast elkaar",
            "een staat die zich buiten de economie houdt",
            "een leger dat volledig wordt afgeschaft",
        ],
        antwoord=0,
        uitleg="De staat kwam boven het individu, en de leider boven de staat. Zijn titel was Il Duce, de leider.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in oktober 1929 op de beurs van New York?",
        opties=[
            "de koersen stortten in en een wereldcrisis volgde",
            "de koersen stegen tot een nooit gezien hoogtepunt",
            "de beurs werd door de regering voorgoed gesloten",
            "de beurs verhuisde naar Washington en Chicago",
        ],
        antwoord=0,
        uitleg="Banken vielen om, bedrijven sloten en de werkloosheid schoot omhoog, ook in Europa.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar stortte de beurs van New York in en begon de wereldcrisis?",
        antwoord=["1929"],
        uitleg="De crisis duurde jaren. Juist in die jaren groeiden de partijen die de democratie afwezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen had de wereldcrisis van de jaren dertig in Europa?",
        opties=[
            "massale werkloosheid en armoede in de industriesteden",
            "groei van partijen die de democratie afwezen",
            "een sterke stijging van de lonen in alle fabrieken",
            "een snelle uitbreiding van de wereldhandel",
        ],
        antwoord=[0, 1],
        uitleg="Wie zijn werk kwijt was, luisterde makkelijker naar wie eenvoudige en harde oplossingen beloofde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kwam de Weimarrepubliek in Duitsland in de problemen?",
        opties=[
            "herstelbetalingen, inflatie en crisis",
            "zij had geen grondwet en geen parlement om te besturen",
            "zij werd door de Volkenbond uit Europa gesloten",
            "zij weigerde het algemeen stemrecht in te voeren",
        ],
        antwoord=0,
        uitleg="Ze werd ook van het begin af aan belast met de schuld voor het verdrag van Versailles.",
    ),
    dict(
        type="waarofniet",
        vraag="De Sovjet-Unie had onder Stalin een economie die door de staat gepland werd.",
        antwoord=True,
        uitleg="Vijfjarenplannen bepaalden wat er gemaakt werd, en de staat bezat de fabrieken en de grond.",
    ),
    dict(
        type="waarofniet",
        vraag="In de Sovjet-Unie van Stalin waren er vrije verkiezingen met verschillende partijen.",
        antwoord=False,
        uitleg="Er was één partij. Wie zich verzette, verdween naar een werkkamp of werd doodgeschoten.",
    ),
    dict(
        type="waarofniet",
        vraag="Mussolini werd door de Italiaanse koning als regeringsleider benoemd.",
        antwoord=True,
        uitleg="De dreiging van zijn mars op Rome volstond. Daarna bouwde hij zijn macht stap voor stap uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De wereldcrisis van de jaren dertig bleef beperkt tot de Verenigde Staten.",
        antwoord=False,
        uitleg="Door de internationale handel en de leningen sloeg ze meteen over naar Europa.",
    ),
    dict(
        type="waarofniet",
        vraag="De crisis van de jaren dertig maakte in Europa de democratie sterker.",
        antwoord=False,
        uitleg="Het omgekeerde: in veel landen kwamen autoritaire regimes aan de macht of dicht erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de Sovjet-Unie onder Stalin kloppen?",
        opties=[
            "de zware industrie groeide snel onder de vijfjarenplannen",
            "de collectivisering kostte miljoenen mensen het leven",
            "de boeren bleven eigenaar van hun grond en hun vee",
            "de partij liet een vrije pers en vrije vakbonden toe",
        ],
        antwoord=[0, 1],
        uitleg="Groei en terreur liepen daar samen op. Dat maakt de beoordeling van dit tijdvak zo scherp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een affiche uit de Sovjet-Unie van 1931 met gespierde arbeiders bij een hoogoven. Hoe lees je die?",
        opties=[
            "als propaganda voor de vijfjarenplannen van de staat",
            "als een getrouwe weergave van het leven in een fabriek",
            "als een aanklacht tegen de werkomstandigheden",
            "als een vrije uiting van een onafhankelijke kunstenaar",
        ],
        antwoord=0,
        uitleg="Kunst stond in dienst van het plan. Wat de affiche laat zien, is wat de staat wilde laten zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen de Vrede van Versailles en het interbellum?",
        opties=[
            "de wrok om het verdrag hielp de nazipartij groeien",
            "het verdrag zorgde voor dertig jaar rust in heel Europa",
            "het verdrag maakte van Duitsland de sterkste mogendheid",
            "het verdrag gaf Duitsland zijn kolonies in Afrika terug",
        ],
        antwoord=0,
        uitleg="Wie het dictaat wilde herzien, had altijd publiek. Dat thema bleef twintig jaar renderen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer werd Hitler in Duitsland rijkskanselier?",
        opties=[
            "in januari 1933",
            "in november 1918",
            "in oktober 1929",
            "in september 1939",
        ],
        antwoord=0,
        uitleg="Hij werd benoemd, niet verkozen tot staatshoofd. Binnen enkele maanden lag alle macht bij hem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bouwde Hitler na 1933 zijn alleenheerschappij uit?",
        opties=[
            "hij liet zich volmachten geven om zonder parlement te regeren",
            "hij verbood de andere partijen en de vrije vakbonden",
            "hij liet elk jaar vrije verkiezingen met meer partijen houden",
            "hij liet de rechters volledig onafhankelijk hun werk doen",
        ],
        antwoord=[0, 1],
        uitleg="Na de brand in de Rijksdag kwamen de volmachten. Daarna ging het hele staatsbestel op de schop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een totalitaire staat?",
        opties=[
            "één partij en één leider met alle macht",
            "een geheime politie, terreur en censuur",
            "een parlement waarin de oppositie mag spreken",
            "rechters die de regering mogen tegenspreken",
        ],
        antwoord=[0, 1],
        uitleg="Een totalitaire staat wil niet enkel gehoorzaamheid, maar greep op het hele leven van zijn burgers.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een staat die greep wil hebben op het hele leven van zijn burgers?",
        antwoord=["een totalitaire staat", "totalitaire staat", "totalitair"],
        uitleg="Het woord komt van totaal. Daarin verschilt zo'n staat van een gewone dictatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde propaganda in nazi-Duitsland?",
        opties=[
            "zij moest het volk achter de leider krijgen",
            "zij moest de burgers zo nauwkeurig mogelijk inlichten",
            "zij werd door de kranten vrij en zelfstandig gemaakt",
            "zij werd door de regering uitdrukkelijk verboden",
        ],
        antwoord=0,
        uitleg="Er was een apart ministerie voor. Radio, film en massabijeenkomsten werden er systematisch voor ingezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelden de Neurenberger wetten van 1935?",
        opties=[
            "zij ontnamen de Joden hun rechten als burger",
            "zij regelden de werkdag en het loon van arbeiders",
            "zij verboden de oorlogsvoorbereiding in Duitsland",
            "zij gaven de vrouwen het stemrecht in Duitsland",
        ],
        antwoord=0,
        uitleg="Burgerrechten, huwelijk en beroep werden langs een raciale lijn verdeeld. De uitsluiting werd wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in november 1938 tijdens de Kristalnacht?",
        opties=[
            "synagogen en Joodse winkels werden in brand gestoken en geplunderd",
            "de nazi's wonnen de verkiezingen met een absolute meerderheid",
            "Duitsland viel Polen binnen en begon de oorlog in Europa",
            "de Joden in Duitsland kregen hun burgerrechten terug",
        ],
        antwoord=0,
        uitleg="Het geweld was door de staat zelf aangemoedigd. Duizenden mensen werden daarna opgepakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol spelen jeugdbewegingen in een totalitaire staat?",
        opties=[
            "zij moeten de kinderen vroeg aan de leider binden",
            "zij staan volledig los van de partij en de staat",
            "zij worden door een totalitaire staat verboden",
            "zij vormen er de oppositie tegen de regering",
        ],
        antwoord=0,
        uitleg="Wie de jeugd heeft, heeft de toekomst. Daarom stonden school, sport en vrije tijd onder toezicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een autoritaire en een totalitaire staat?",
        opties=[
            "een totalitaire staat wil ook het denken van zijn burgers beheersen",
            "een autoritaire staat laat vrije verkiezingen en een vrije pers toe",
            "een totalitaire staat heeft geen geheime politie nodig",
            "een autoritaire staat heeft geen leger en geen politie",
        ],
        antwoord=0,
        uitleg="Een autoritaire staat eist gehoorzaamheid. Een totalitaire staat eist ook overtuiging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke politiek volgden Frankrijk en Groot-Brittannië tegenover Hitler voor 1939?",
        opties=[
            "zij gaven toe in de hoop zo een oorlog te vermijden",
            "zij vielen Duitsland bij de eerste schending aan",
            "zij sloten een bondgenootschap met Duitsland",
            "zij lieten de Volkenbond Duitsland bezetten",
        ],
        antwoord=0,
        uitleg="Die politiek heet appeasement. Ze gaf Hitler tijd en gebied, en ze heeft de oorlog niet voorkomen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de politiek van toegeven aan Hitler om een oorlog te vermijden?",
        antwoord=["appeasement", "de appeasementpolitiek", "verzoeningspolitiek"],
        uitleg="Het hoogtepunt was de conferentie van München in 1938, waar Tsjechoslowakije gebied moest afstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen zette Hitler voor september 1939?",
        opties=[
            "hij liet zijn leger het Rijnland opnieuw bezetten",
            "hij lijfde Oostenrijk bij Duitsland in",
            "hij gaf Elzas en Lotharingen aan Frankrijk terug",
            "hij trad met Duitsland tot de Volkenbond toe",
        ],
        antwoord=[0, 1],
        uitleg="Daarna kwamen Sudetenland en de rest van Tsjechoslowakije. Elke stap bleef zonder gevolg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat spraken Duitsland en de Sovjet-Unie in augustus 1939 af?",
        opties=[
            "zij beloofden elkaar niet aan te vallen",
            "zij sloten een bondgenootschap tegen Italië en Japan",
            "zij beloofden allebei hun leger sterk te verkleinen",
            "zij traden samen tot de Volkenbond in Genève toe",
        ],
        antwoord=0,
        uitleg="In een geheim deel verdeelden zij Polen onder elkaar. Een week later viel Duitsland het land binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hitler kwam in Duitsland langs een benoeming aan de macht, niet langs een staatsgreep.",
        antwoord=True,
        uitleg="Zijn partij was de grootste geworden. Daarna heeft hij de democratie met wetten afgebroken.",
    ),
    dict(
        type="waarofniet",
        vraag="In nazi-Duitsland bleven de vakbonden en de andere partijen gewoon bestaan.",
        antwoord=False,
        uitleg="Zij werden in 1933 verboden of ontbonden. Wat overbleef, stond onder leiding van de partij.",
    ),
    dict(
        type="waarofniet",
        vraag="De Neurenberger wetten maakten de uitsluiting van de Joden tot wet.",
        antwoord=True,
        uitleg="Zij ontnamen hen het burgerrecht. Daarmee werd het racisme van het regime in de wet ingeschreven.",
    ),
    dict(
        type="waarofniet",
        vraag="De conferentie van München in 1938 heeft de oorlog voorgoed afgewend.",
        antwoord=False,
        uitleg="Enkele maanden later nam Duitsland de rest van Tsjechoslowakije, en in september 1939 Polen.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook in België kwamen er in de jaren dertig partijen op die de democratie afwezen.",
        antwoord=True,
        uitleg="Rex en het Vlaams Nationaal Verbond haalden zetels, en keken naar de regimes in het buitenland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een foto van een massabijeenkomst met vlaggen, rijen en één spreker op een podium. Wat herken je?",
        opties=[
            "de propaganda van een totalitair regime",
            "een vrije verkiezingsbijeenkomst van meerdere partijen",
            "een vergadering van de Volkenbond in Genève",
            "een vakbondsbetoging voor een kortere werkdag",
        ],
        antwoord=0,
        uitleg="De opstelling is het boodschappelijke: de massa in orde, de leider alleen boven haar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen de wereldcrisis en de opkomst van het nazisme?",
        opties=[
            "de werkloosheid maakte de partij voor veel kiezers aantrekkelijk",
            "de crisis maakte de Duitse economie juist sterker dan ooit",
            "de crisis had op de Duitse verkiezingen geen enkele invloed",
            "de crisis deed het aantal werklozen in Duitsland dalen",
        ],
        antwoord=0,
        uitleg="Tussen 1929 en 1932 steeg het aantal werklozen sterk, en groeide zijn partij van klein tot grootste.",
    ),
]

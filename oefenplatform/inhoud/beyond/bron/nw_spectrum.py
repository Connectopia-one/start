# -*- coding: utf-8 -*-
"""🌍 Beyond — Het elektromagnetisch spectrum.

Fysica, de kop "Elektromagnetisch spectrum" uit de vakfiche
natuurwetenschappen 3DO. Deel 1 gaat over de elektromagnetische golf zelf, de
ordening van het spectrum en het verband tussen golflengte, frequentie en
energie, met de drie indelingen van de leerstof. Deel 2 gaat over de interactie
met materie, over de toepassingen en over de bescherming tegen de hoogenergetische
straling.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat voor soort golf is een elektromagnetische golf?",
        opties=[
            "een transversale golf die geen middenstof nodig heeft",
            "een longitudinale golf die lucht nodig heeft",
            "een transversale golf die enkel in water reist",
            "een longitudinale golf die enkel in metaal reist",
        ],
        antwoord=0,
        uitleg="Daarom kan het licht van de zon door het lege heelal naar ons komen. Geluid, een mechanische golf, kan dat niet.",
    ),
    dict(
        type="invultekst",
        vraag="Met welke snelheid beweegt een elektromagnetische golf in vacuüm?",
        antwoord=["de lichtsnelheid", "lichtsnelheid"],
        uitleg="Dat is ongeveer 300 000 kilometer per seconde, voor elke soort straling van het spectrum. In glas of water gaat de golf trager.",
    ),
    dict(
        type="waarofniet",
        vraag="Een elektromagnetische golf gaat trager als ze van vacuüm in glas komt.",
        antwoord=True,
        uitleg="In een middenstof botst de golf voortdurend op deeltjes en wordt ze afgeremd. Komt ze weer in vacuüm, dan haalt ze opnieuw de lichtsnelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke straling heeft de grootste golflengte van het hele spectrum?",
        opties=["radiogolven", "microgolven", "ultraviolet", "gammastraling"],
        antwoord=0,
        uitleg="Radiogolven staan helemaal aan de kant van de lange golven en de lage frequentie. Gammastraling staat aan de andere kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke straling heeft de hoogste energie van het hele spectrum?",
        opties=["gammastraling", "radiogolven", "infraroodstraling", "zichtbaar licht"],
        antwoord=0,
        uitleg="Een hogere frequentie betekent meer energie per golf. Gammastraling heeft dus de kortste golflengte en de grootste energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet het spectrum van lage naar hoge frequentie. Welke rij is juist?",
        opties=[
            "radio, microgolven, infrarood, zichtbaar licht, ultraviolet, röntgen, gamma",
            "gamma, röntgen, ultraviolet, zichtbaar licht, infrarood, microgolven, radio",
            "zichtbaar licht, infrarood, radio, microgolven, ultraviolet, röntgen, gamma",
            "radio, infrarood, microgolven, zichtbaar licht, röntgen, ultraviolet, gamma",
        ],
        antwoord=0,
        uitleg="Die rij volgt tegelijk de stijgende energie en de dalende golflengte. Infrarood zit net naast rood, ultraviolet net naast violet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere golflengte hoort bij een lagere frequentie.",
        antwoord=True,
        uitleg="De snelheid ligt vast, dus moet het ene zakken als het andere stijgt. Golflengte en frequentie zijn omgekeerd verbonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een golf met een hoge frequentie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "haar golflengte is klein",
            "haar energie is groot",
            "ze zit aan de kant van röntgen en gamma",
            "ze gaat sneller dan een golf met een lage frequentie",
        ],
        antwoord=[0, 1, 2],
        uitleg="In vacuüm hebben alle elektromagnetische golven precies dezelfde snelheid. Enkel hun golflengte, frequentie en energie verschillen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke straling zit net naast het rode licht, aan de kant van de langere golven?",
        antwoord=["infrarood", "infraroodstraling", "IR"],
        uitleg="Rood heeft van het zichtbare licht de langste golflengte. Aan de andere kant van het zichtbare licht, naast violet, zit ultraviolet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stralingen zijn ioniserend? Kruis alles aan wat juist is.",
        opties=["gammastraling", "röntgenstraling", "hoogenergetische uv-straling", "radiogolven"],
        antwoord=[0, 1, 2],
        uitleg="Ioniserend betekent dat de golf elektronen uit atomen kan losslaan. Radiogolven hebben daar veel te weinig energie voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk deel van het spectrum kan een mens zien?",
        opties=[
            "enkel het zichtbare licht, van rood tot violet",
            "het zichtbare licht en infrarood samen",
            "het zichtbare licht en ultraviolet samen",
            "het hele spectrum van radio tot gamma",
        ],
        antwoord=0,
        uitleg="Dat is een heel smal stukje van het hele spectrum. Infrarood voelen we soms als warmte, maar zien doen we het niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke soort elektromagnetische straling is schadelijk voor de mens.",
        antwoord=False,
        uitleg="Radiogolven en microgolven in gewone hoeveelheden zijn dat niet. Het gevaar begint bij de hoogenergetische straling, dus uv, röntgen en gamma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het doordringend vermogen van een straling?",
        opties=[
            "hoe diep ze in materie kan binnendringen",
            "hoe sterk ze een kleur kan geven",
            "hoe snel ze in vacuüm beweegt",
            "hoeveel golven er per seconde passeren",
        ],
        antwoord=0,
        uitleg="Gammastraling dringt heel diep door en heeft daarom dik lood of beton nodig. Hoe hoger de energie, hoe groter dat vermogen in het algemeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men radiogolven voor communicatie over grote afstand?",
        opties=[
            "ze dragen ver en worden niet snel geabsorbeerd",
            "ze hebben de hoogste energie van het spectrum",
            "ze kunnen door lood en beton heen",
            "ze zijn met het oog goed te zien",
        ],
        antwoord=0,
        uitleg="Door hun lange golflengte raken ze ver en kunnen ze ook rond hindernissen buigen. Daarom werken radio, televisie en gsm met dat deel van het spectrum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt een magnetron microgolven?",
        opties=[
            "de watermoleculen in het eten nemen die energie goed op",
            "microgolven hebben de hoogste energie van het spectrum",
            "microgolven maken het eten zichtbaar warm van kleur",
            "microgolven dringen door lood en beton heen",
        ],
        antwoord=0,
        uitleg="De opgenomen energie doet de watermoleculen sneller bewegen en zo wordt het eten warm. Microgolven zijn niet ioniserend, dus maken ze het eten niet radioactief.",
    ),
    dict(
        type="invultekst",
        vraag="Welke straling van het spectrum heeft het grootste doordringend vermogen?",
        antwoord=["gammastraling", "gamma"],
        uitleg="Ze heeft de hoogste energie en de kortste golflengte. Daarom heb je dik lood of beton nodig om ze tegen te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Gammastraling gaat in vacuüm sneller dan radiogolven.",
        antwoord=False,
        uitleg="Van radiogolven tot gammastraling halen ze in vacuüm allemaal precies de lichtsnelheid. Het verschil zit in golflengte, frequentie en energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je weet dat een straling niet zichtbaar is, een lange golflengte heeft en niet ioniserend is. Welke straling kan dat zijn?",
        opties=["microgolven", "ultraviolet", "röntgenstraling", "gammastraling"],
        antwoord=0,
        uitleg="De drie andere hebben juist een korte golflengte en veel energie. Microgolven zitten net naast de radiogolven aan de lange kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke indelingen van elektromagnetische straling bestaan er? Kruis alles aan wat juist is.",
        opties=[
            "zichtbaar en niet-zichtbaar",
            "schadelijk en niet-schadelijk",
            "ioniserend en niet-ioniserend",
            "goedkoop en duur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Met die drie kan je van elke toepassing zeggen waar ze staat. De prijs van een toestel hoort niet bij de eigenschappen van de straling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is uv-straling gevaarlijker voor je huid dan zichtbaar licht?",
        opties=[
            "uv heeft meer energie per golf en kan in cellen schade aanrichten",
            "uv heeft een veel grotere golflengte dan licht",
            "uv beweegt veel sneller dan zichtbaar licht",
            "uv wordt door de huid helemaal weerkaatst",
        ],
        antwoord=0,
        uitleg="Door die energie kan uv bindingen in het DNA van huidcellen beschadigen. Daarom is zonnecrème geen overbodige luxe.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie dingen kunnen er gebeuren als straling op materie valt?",
        opties=[
            "absorberen, doorlaten of weerkaatsen",
            "versnellen, vertragen of stoppen",
            "opwarmen, afkoelen of smelten",
            "ioniseren, polariseren of magnetiseren",
        ],
        antwoord=0,
        uitleg="Welke van de drie het wordt, hangt af van de straling én van de stof. Vaak gebeuren ze alle drie een beetje tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is gras groen?",
        opties=[
            "het weerkaatst het groene licht en absorbeert de andere kleuren",
            "het absorbeert het groene licht en weerkaatst de andere kleuren",
            "het zendt zelf groen licht uit",
            "het laat alle kleuren behalve groen door",
        ],
        antwoord=0,
        uitleg="De kleur die je ziet, is de kleur die naar je oog terugkomt. De andere kleuren worden door het blad opgenomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een röntgenfoto zijn de botten wit omdat ze meer straling absorberen dan het zachte weefsel.",
        antwoord=True,
        uitleg="Waar de straling tegengehouden wordt, komt er minder op de plaat. Zacht weefsel laat de straling grotendeels door en wordt dus donkerder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen werken met radiogolven? Kruis alles aan wat juist is.",
        opties=[
            "een wifinetwerk",
            "een gsm",
            "televisie via een antenne",
            "een warmtelamp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie sturen informatie via radiogolven door de lucht. Een warmtelamp werkt met infraroodstraling.",
    ),
    dict(
        type="invultekst",
        vraag="Met welke straling werkt een afstandsbediening van een televisie?",
        antwoord=["infrarood", "infraroodstraling", "IR"],
        uitleg="Het lampje vooraan zendt onzichtbare infraroodstraling uit. Met een telefooncamera kan je dat flikkeren soms wel zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee werkt een warmtebeeldcamera of een nachtkijker?",
        opties=[
            "met infraroodstraling",
            "met ultraviolette straling",
            "met röntgenstraling",
            "met radiogolven",
        ],
        antwoord=0,
        uitleg="Elk warm voorwerp zendt infraroodstraling uit. De camera maakt van die onzichtbare straling een beeld dat wij kunnen zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen werken met ultraviolette straling? Kruis alles aan wat juist is.",
        opties=[
            "een zonnebank",
            "een valsgelddetector",
            "desinfectie van water of oppervlakken",
            "een gewone keramische kookplaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uv maakt bepaalde stoffen zichtbaar oplichten en kan bacteriën doden. Een keramische kookplaat werkt met infraroodstraling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een blacklight werkt met infraroodstraling.",
        antwoord=False,
        uitleg="Een blacklight zendt ultraviolette straling uit. Die zie je zelf niet, maar bepaalde stoffen lichten eronder op, en daarmee vind je ook valse bankbiljetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke straling werkt een bagagescanner op een luchthaven?",
        opties=["röntgenstraling", "infraroodstraling", "radiogolven", "microgolven"],
        antwoord=0,
        uitleg="Röntgenstraling dringt door de koffer maar wordt door metaal sterk geabsorbeerd. Daardoor zie je op het beeld wat er binnen zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men gammastraling om voedsel te steriliseren?",
        opties=[
            "haar hoge energie doodt de micro-organismen erin",
            "ze warmt het voedsel tot boven de honderd graden op",
            "ze maakt het voedsel langer zichtbaar mooi van kleur",
            "ze wordt door het voedsel helemaal weerkaatst",
        ],
        antwoord=0,
        uitleg="De straling beschadigt het DNA van bacteriën en schimmels. Het voedsel zelf wordt daardoor niet radioactief.",
    ),
    dict(
        type="invultekst",
        vraag="Welke straling gebruikt men bij radiotherapie tegen kanker?",
        antwoord=["gammastraling", "gamma"],
        uitleg="Haar hoge energie beschadigt het DNA van de kankercellen. De bundel wordt heel precies gericht om het gezonde weefsel te sparen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bescherm je je tegen röntgen- en gammastraling?",
        opties=[
            "met een loodschort of een dikke betonnen wand",
            "met een gewone katoenen jas over je kleren",
            "met een zonnebril met heel donkere glazen",
            "met een laagje water van ongeveer een centimeter",
        ],
        antwoord=0,
        uitleg="Je hebt een zware stof nodig, want die straling dringt diep door. Daarom draagt een tandarts een loodschort of gaat die uit het lokaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonnecrème en een zonnebril met uv-filter beschermen tegen ultraviolette straling.",
        antwoord=True,
        uitleg="Ze absorberen of weerkaatsen de uv voor ze je huid of je oog bereikt. Schaduw zoeken en kleding helpen natuurlijk ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen horen bij bescherming tegen hoogenergetische straling? Kruis alles aan wat juist is.",
        opties=[
            "een loodschort dragen",
            "afstand houden van de bron",
            "de tijd bij de bron zo kort mogelijk houden",
            "een luidere alarmbel installeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Afschermen, afstand en tijd zijn de drie klassieke maatregelen. Een alarm waarschuwt wel, maar houdt geen straling tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom houdt een metalen rooster in de deur van een magnetron de microgolven binnen?",
        opties=[
            "het werkt als een kooi van Faraday",
            "het absorbeert alle microgolven volledig",
            "het zet de microgolven om in zichtbaar licht",
            "het laat de microgolven wel door, maar heel traag",
        ],
        antwoord=0,
        uitleg="De openingen zijn veel kleiner dan de golflengte van de microgolven, dus geraken ze er niet door. Het zichtbare licht heeft een veel kortere golflengte en kan wel passeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gsm werkt met straling die ioniserend is.",
        antwoord=False,
        uitleg="Een gsm werkt met radiogolven, en die hebben veel te weinig energie om te ioniseren. Ioniserend wordt het pas bij hoogenergetisch uv, röntgen en gamma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Men meet in een fabriek de dikte van een metalen plaat met straling. Welke straling is daarvoor logisch?",
        opties=[
            "straling die diep doordringt, zoals gamma",
            "zichtbaar licht van een heel sterke lamp",
            "radiogolven van een gewone radiozender",
            "infraroodstraling van een warmtelamp",
        ],
        antwoord=0,
        uitleg="Hoe dikker de plaat, hoe meer van de straling geabsorbeerd wordt. Uit wat er doorkomt, kan het toestel de dikte berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toepassing stuurt straling door een voorwerp en meet wat er aan de andere kant aankomt. Welk soort interactie gebruikt ze?",
        opties=[
            "transmissie en absorptie",
            "enkel weerkaatsing van de bundel",
            "enkel polarisatie van de bundel",
            "enkel resonantie in het voorwerp",
        ],
        antwoord=0,
        uitleg="Een deel gaat erdoor en een deel wordt opgenomen, en het verschil geeft de informatie. Een röntgenfoto en een diktemeting werken allebei zo.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel waarbij straling door een stof heen gaat?",
        antwoord=["transmissie", "doorlaten"],
        uitleg="De twee andere mogelijkheden zijn absorberen en weerkaatsen. Glas laat zichtbaar licht door maar houdt een groot deel van de uv tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt een toestel dat met onzichtbare straling bacteriën doodt in een waterleiding. Welke straling is dat?",
        opties=["ultraviolette straling", "infraroodstraling", "microgolven", "radiogolven"],
        antwoord=0,
        uitleg="Uv beschadigt het DNA van micro-organismen, zodat ze zich niet meer kunnen delen. Daarom gebruikt men het voor desinfectie van water en oppervlakken.",
    ),
]

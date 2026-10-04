# -*- coding: utf-8 -*-
"""Duurzame chemie en de circulaire economie — 🌍 Beyond, chemie.

Deel 1 gaat over de kringloop: de lineaire economie van wieg tot graf, de
keteneconomie ertussen, de circulaire economie van wieg tot wieg, de ladder van
Lansink, downcycling, de duurzame ontwikkelingsdoelen, de vijf P's en
greenwashing. Deel 2 gaat over de stoffen en de cijfers: biogebaseerd,
biodegradeerbaar en composteerbaar, de kleuren van waterstof, wit, grijs en
zwart water, de atoomeconomie van een reactie en microplastics.

De ladder van Lansink wordt in woorden beschreven van boven naar onder, zodat de
vragen ook zonder de tekening te lezen zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met een lineaire economie?",
        opties=[
            "grondstof, product, gebruik en daarna afval dat verdwijnt",
            "grondstof, product, gebruik en daarna opnieuw grondstof",
            "grondstof, product, hergebruik en daarna nog eens gebruik",
            "grondstof, product, recyclage en daarna weer hetzelfde",
        ],
        antwoord=0,
        uitleg="Zo'n keten heet van wieg tot graf. Aan het eind blijft er afval over dat "
        "nergens meer dienst doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het idee achter cradle to cradle?",
        opties=[
            "het afval van het ene product is de grondstof van het volgende",
            "het afval van het ene product wordt netjes gestort of verbrand",
            "het afval van het ene product wordt zo klein mogelijk gehouden",
            "het afval van het ene product wordt in het buitenland verwerkt",
        ],
        antwoord=0,
        uitleg="Van wieg tot wieg: er is geen eindpunt. Dat vraagt dat je al bij het "
        "ontwerp nadenkt over wat er later met het materiaal gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat bovenaan de ladder van Lansink?",
        opties=[
            "preventie: zorgen dat het afval niet ontstaat",
            "recyclage: het materiaal opnieuw bruikbaar maken",
            "hergebruik: het voorwerp een tweede leven geven",
            "verbranding: er nog energie uit halen",
        ],
        antwoord=0,
        uitleg="De ladder zet de manieren van afvalbeheer op een rij van best naar "
        "slechtst. Onderaan staat storten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen staan hoger op de ladder van Lansink dan verbranden? Kruis alles aan wat juist is.",
        opties=[
            "preventie",
            "hergebruik",
            "storten",
            "lozen in de rivier",
        ],
        antwoord=[0, 1],
        uitleg="Storten staat helemaal onderaan en lozen staat er zelfs niet op. "
        "Verbranden met energierecuperatie zit net boven storten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is downcycling?",
        opties=[
            "recycleren tot een product van mindere kwaliteit",
            "recycleren tot een product van dezelfde kwaliteit",
            "recycleren tot een product van hogere kwaliteit",
            "recycleren tot een product van kleinere afmeting",
        ],
        antwoord=0,
        uitleg="Een petfles die tot vulling voor een jas wordt, kan daarna niet meer "
        "terug naar een fles. Het materiaal zakt elke ronde een trapje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een keteneconomie?",
        opties=[
            "een tussenvorm die veel hergebruikt maar toch nog afval overhoudt",
            "een volledige kringloop waarin er helemaal geen afval meer is",
            "een rechte keten waarin elk product na gebruik gestort wordt",
            "een korte keten waarin elke grondstof uit de eigen streek komt",
        ],
        antwoord=0,
        uitleg="Ze zit tussen lineair en circulair in. Er wordt al veel gerecycleerd, "
        "maar helemaal rond is de cirkel nog niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is greenwashing?",
        opties=[
            "een product groener voorstellen dan het in werkelijkheid is",
            "een product grondig wassen voordat het gerecycleerd wordt",
            "een product groen verven om het beter te laten opvallen",
            "een product groener maken door minder water te gebruiken",
        ],
        antwoord=0,
        uitleg="Een blaadje op de verpakking of het woord natuurlijk zegt op zich niets. "
        "Kijk naar wat er echt gemeten en bewezen is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de keten van wieg tot graf in één woord?",
        antwoord=["lineair", "lineaire economie", "lineaire"],
        uitleg="Het tegendeel is circulair, van wieg tot wieg. Ertussen zit de "
        "keteneconomie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de duurzame ontwikkelingsdoelen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er zijn er zeventien",
            "ze zijn afgesproken binnen de Verenigde Naties",
            "ze gelden enkel voor de rijkste landen",
            "ze gaan uitsluitend over het klimaat",
        ],
        antwoord=[0, 1],
        uitleg="Ze gelden voor alle landen en gaan ook over armoede, gezondheid, "
        "onderwijs en gelijkheid. Het streefjaar is 2030.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vijf P's van duurzame ontwikkeling?",
        opties=[
            "people, planet, prosperity, peace en partnership",
            "people, planet, profit, plastic en productie",
            "planet, product, proces, profit en preventie",
            "people, product, planning, profit en politiek",
        ],
        antwoord=0,
        uitleg="Het oudere model sprak van people, planet en profit. De vijf P's voegen "
        "vrede en samenwerking toe en spreken van welvaart.",
    ),
    dict(
        type="waarofniet",
        vraag="Hergebruik staat hoger op de ladder van Lansink dan recyclage.",
        antwoord=True,
        uitleg="Bij hergebruik blijft het voorwerp zelf heel, bij recyclage moet je het "
        "eerst afbreken tot grondstof. Dat laatste kost meer energie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een circulaire economie bestaat het woord afval eigenlijk niet meer.",
        antwoord=True,
        uitleg="Wat uit het ene proces komt, gaat als grondstof in het volgende. In de "
        "praktijk haalt geen enkele keten dat volledig.",
    ),
    dict(
        type="waarofniet",
        vraag="Downcycling en recyclage betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="Downcycling is recyclage waarbij de kwaliteit zakt. Recyclage op gelijk "
        "niveau houdt het materiaal wel bruikbaar voor hetzelfde doel.",
    ),
    dict(
        type="waarofniet",
        vraag="Storten staat op de ladder van Lansink net boven verbranden.",
        antwoord=False,
        uitleg="Storten staat juist onderaan, onder verbranden. Bij verbranden met "
        "energierecuperatie haal je er nog warmte of stroom uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes maken een product beter geschikt voor een kringloop? Kruis alles aan wat juist is.",
        opties=[
            "de onderdelen kunnen weer van elkaar los",
            "er zitten zo weinig verschillende materialen in",
            "de onderdelen zijn met lijm aan elkaar vast",
            "er zitten zo veel verschillende materialen in",
        ],
        antwoord=[0, 1],
        uitleg="Wat je niet kan scheiden, kan je niet zuiver recycleren. Een gelijmd "
        "mengsel van zeven kunststoffen eindigt meestal in de oven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je recyclage waarbij de kwaliteit van het materiaal daalt?",
        antwoord=["downcycling", "downcyclen", "downcycleren"],
        uitleg="Het materiaal blijft in omloop, maar zakt elke ronde een trapje. Daarna "
        "is terug naar het oorspronkelijke product niet meer mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is preventie de beste trede van de ladder?",
        opties=[
            "afval dat nooit ontstaat, moet ook nooit verwerkt worden",
            "afval dat gestort wordt, verdwijnt na een tijd van zelf",
            "afval dat verbrand wordt, levert altijd genoeg energie op",
            "afval dat gerecycleerd wordt, blijft altijd even bruikbaar",
        ],
        antwoord=0,
        uitleg="Elke andere trede kost nog energie, transport en materiaal. Minder "
        "verpakking of een langere levensduur kost dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over greenwashing zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een vaag woord als natuurlijk is nog geen bewijs",
            "een groene verpakking zegt niets over de inhoud",
            "een keurmerk met controle is altijd greenwashing",
            "een bedrijf dat cijfers publiceert, doet er altijd aan",
        ],
        antwoord=[0, 1],
        uitleg="Een onafhankelijk gecontroleerd keurmerk en openbare cijfers zijn juist "
        "wat je nodig hebt om een bewering na te gaan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel duurzame ontwikkelingsdoelen zijn er?",
        antwoord=["17", "zeventien"],
        uitleg="Ze werden in 2015 afgesproken bij de Verenigde Naties, met 2030 als "
        "streefjaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kringloop van wieg tot wieg in één woord?",
        antwoord=["circulair", "circulaire economie", "circulaire"],
        uitleg="Daar gaat wat overblijft als grondstof terug in het begin. Het tegendeel "
        "is lineair, van wieg tot graf.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent biogebaseerd?",
        opties=[
            "de grondstof komt uit biomassa in plaats van uit aardolie",
            "de stof wordt door bacteriën in de natuur volledig afgebroken",
            "de stof valt in een composthoop binnen twaalf weken uiteen",
            "de stof is onschadelijk voor elk dier dat ervan zou eten",
        ],
        antwoord=0,
        uitleg="Het zegt enkel waar de grondstof van komt. Biogebaseerd plastic kan even "
        "goed honderden jaren blijven liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent biodegradeerbaar?",
        opties=[
            "micro-organismen kunnen de stof afbreken tot kleine moleculen",
            "de grondstof van de stof komt oorspronkelijk uit biomassa",
            "de stof lost helemaal op in water zonder iets achter te laten",
            "de stof kan eindeloos opnieuw gerecycleerd worden tot dezelfde",
        ],
        antwoord=0,
        uitleg="Hoe snel en onder welke omstandigheden staat er niet bij. In koud "
        "zeewater kan hetzelfde materiaal jaren blijven liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over composteerbaar zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is strenger dan biodegradeerbaar",
            "er hoort een tijd en een temperatuur bij",
            "het betekent hetzelfde als biogebaseerd",
            "het mag altijd bij het gewone tuinafval",
        ],
        antwoord=[0, 1],
        uitleg="Industrieel composteerbaar vraagt een installatie op een hoge "
        "temperatuur. In je eigen compostbak gebeurt dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maakt men groene waterstof?",
        opties=[
            "elektrolyse van water met stroom uit wind of zon",
            "elektrolyse van water met stroom uit een gascentrale",
            "stoomreforming van aardgas zonder iets af te vangen",
            "stoomreforming van aardgas met opslag van de CO₂",
        ],
        antwoord=0,
        uitleg="De derde manier geeft grijze waterstof, de vierde blauwe. De kleur zegt "
        "niets over het gas zelf, enkel over hoe het gemaakt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen grijze en blauwe waterstof?",
        opties=[
            "bij blauwe wordt de CO₂ afgevangen en opgeslagen",
            "bij blauwe wordt er helemaal geen aardgas gebruikt",
            "bij blauwe wordt er water in plaats van gas gesplitst",
            "bij blauwe wordt er enkel stroom uit zon gebruikt",
        ],
        antwoord=0,
        uitleg="Beide beginnen bij aardgas. Bij grijze waterstof gaat de koolstofdioxide "
        "gewoon de lucht in.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kleur waterstof komt uit elektrolyse met hernieuwbare stroom?",
        antwoord=["groen", "groene", "groene waterstof"],
        uitleg="Uit aardgas komt grijze waterstof, en met afvang van de CO₂ blauwe. De "
        "kleur verwijst naar de productiewijze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is grijs water?",
        opties=[
            "licht vervuild water van bad, wastafel en wasmachine",
            "water uit het toilet met fecaliën en urine erin",
            "zuiver drinkbaar water zoals het uit de kraan komt",
            "water dat na zuivering weer in de rivier belandt",
        ],
        antwoord=0,
        uitleg="Wit water is drinkbaar, zwart water komt uit het toilet. Grijs water kan "
        "vaak nog dienen om door te spoelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over wit, grijs en zwart water zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "wit water is drinkbaar",
            "zwart water komt uit het toilet",
            "grijs water is drinkbaar",
            "zwart water komt uit de wastafel",
        ],
        antwoord=[0, 1],
        uitleg="Grijs water is licht vervuild en niet drinkbaar, maar wel herbruikbaar. "
        "Zwart water moet altijd eerst naar de zuivering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de atoomeconomie van een reactie?",
        opties=[
            "welk deel van de massa van de reagentia in het product zit",
            "welk deel van de reagentia uiteindelijk ook echt reageert",
            "welk deel van de energie in het eindproduct bewaard blijft",
            "welk deel van het product na zuivering nog bruikbaar is",
        ],
        antwoord=0,
        uitleg="Ze kijkt naar de reactievergelijking zelf, dus naar hoeveel massa "
        "noodgedwongen in bijproducten terechtkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reactie heeft in principe de hoogste atoomeconomie?",
        opties=[
            "een additiereactie waarbij alles in het product belandt",
            "een eliminatiereactie waarbij er water afgesplitst wordt",
            "een substitutiereactie waarbij er een zout vrijkomt",
            "een condensatiereactie waarbij er een molecule wegvalt",
        ],
        antwoord=0,
        uitleg="Bij een additie komen beide reagentia volledig in het product. Bij de "
        "drie andere gaat er altijd massa naar een bijproduct.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de atoomeconomie van een additie waarbij geen bijproduct ontstaat?",
        antwoord=["100 %", "100%", "100"],
        uitleg="Alle massa van de reagentia zit dan in het gewenste product. In de "
        "praktijk haalt het rendement dat zelden, want niet alles reageert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is een microplastic?",
        opties=[
            "kleiner dan vijf millimeter",
            "kleiner dan vijf micrometer",
            "kleiner dan vijf nanometer",
            "kleiner dan vijf centimeter",
        ],
        antwoord=0,
        uitleg="Dat is dus met het oog nog zichtbaar. Nanoplastics zijn nog duizend keer "
        "kleiner en kunnen tot in cellen komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over microplastics zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "primaire microplastics zijn al klein gemaakt",
            "secundaire ontstaan door afbraak van groter plastic",
            "primaire microplastics ontstaan enkel in de zee",
            "secundaire zijn altijd biodegradeerbaar gemaakt",
        ],
        antwoord=[0, 1],
        uitleg="Korrels in scrubs of grondstofpellets zijn primair. Een fles die in de "
        "zon en de golven uiteenvalt, geeft secundaire deeltjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Een biogebaseerde kunststof is daarom ook biodegradeerbaar.",
        antwoord=False,
        uitleg="De twee woorden zeggen iets anders: het eerste gaat over de grondstof, "
        "het tweede over de afbraak. Bio-pet uit plantaardige grondstof breekt niet af.",
    ),
    dict(
        type="waarofniet",
        vraag="Waterstof zelf is bij elke kleur precies dezelfde stof.",
        antwoord=True,
        uitleg="H₂ is H₂. De kleur zegt alleen met welke grondstof en welke energie het "
        "gemaakt werd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoog rendement en een hoge atoomeconomie betekenen hetzelfde.",
        antwoord=False,
        uitleg="Het rendement meet hoeveel je er echt uithaalt, de atoomeconomie wat de "
        "vergelijking in het beste geval toelaat. Je kan 100 % atoomeconomie hebben met "
        "een slecht rendement.",
    ),
    dict(
        type="waarofniet",
        vraag="Katalyse helpt de groene chemie omdat de katalysator niet opgebruikt raakt.",
        antwoord=True,
        uitleg="Hij komt na de reactie terug vrij en kan opnieuw dienen. Een "
        "stoichiometrisch reagens eindigt wel als afval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk principe van de groene chemie staat het hoogst?",
        opties=[
            "afval voorkomen in plaats van het achteraf opruimen",
            "afval scheiden in plaats van het samen te verbranden",
            "afval verbranden in plaats van het ergens te storten",
            "afval verdunnen in plaats van het gericht af te voeren",
        ],
        antwoord=0,
        uitleg="Dat is dezelfde gedachte als de bovenste trede van de ladder van Lansink. "
        "Verdunnen lost trouwens niets op: de stof blijft in het milieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een solvent dikwijls het grootste milieuprobleem van een synthese?",
        opties=[
            "er gaat meestal veel meer solvent in dan reagens",
            "een solvent reageert altijd mee tot een bijproduct",
            "een solvent verhoogt altijd de atoomeconomie niet",
            "een solvent blijft altijd volledig in het product",
        ],
        antwoord=0,
        uitleg="In massa is het solvent vaak het grootste deel van alles wat de reactor "
        "ingaat. Daarom zoekt men naar reacties in water of zonder solvent.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het water uit het toilet?",
        antwoord=["zwart water", "zwart", "zwarte"],
        uitleg="Wit water is drinkbaar en grijs water komt van bad en wasmachine. Zwart "
        "water moet altijd naar de waterzuivering.",
    ),
]

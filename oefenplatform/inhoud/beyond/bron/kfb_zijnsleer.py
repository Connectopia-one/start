# -*- coding: utf-8 -*-
"""Zijnsleer: schijn en werkelijkheid, worden en zijn.

Thema filosofie dat enkel in kunstbeschouwing en filosofie (fiche 3DDO)
staat, niet in filosofie en recht:

    basisbegrippen schijn en werkelijkheid, worden en zijn, en hun relatie,
    bij Parmenides, Plato en Aristoteles
    immanentie en transcendentie bij Plato, Aristoteles en Immanuel Kant
    noodzakelijkheid (Spinoza), toeval (Hume, Sartre), doelgerichtheid
    (Aristoteles, Hegel) en existentialistische denkers

Deel 1: schijn en werkelijkheid, worden en zijn, immanentie en transcendentie.
Deel 2: noodzakelijkheid, toeval en doelgerichtheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat onderzoekt de zijnsleer of ontologie?",
        opties=[
            "wat de werkelijkheid ten diepste is en wat bestaan betekent",
            "hoe je een goede tekst schrijft met een duidelijke structuur",
            "welke handelingen moreel goed of slecht zijn in een dilemma",
            "hoe je met de rede een geldige redenering opbouwt zonder fouten",
        ],
        antwoord=0,
        uitleg="Ontologie komt van het Griekse 'on', het zijnde. Ethiek gaat over goed en kwaad, logica over geldig redeneren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het begrippenpaar schijn en werkelijkheid?",
        opties=[
            "wat we waarnemen, is misschien niet hoe de dingen echt zijn",
            "alles wat we zien, bestaat precies zoals we het zien",
            "dromen zijn altijd echter dan wat we overdag waarnemen",
            "enkel dingen die licht geven, zijn echt werkelijk",
        ],
        antwoord=0,
        uitleg="De zintuigen tonen een verschijning. De vraag is of daarachter een andere, echte werkelijkheid zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het begrippenpaar worden en zijn?",
        opties=[
            "de vraag of de werkelijkheid altijd verandert of ten diepste onveranderlijk is",
            "de vraag hoe een kind stap voor stap opgroeit tot een volwassene met een beroep",
            "de vraag of je beter iets wordt dan dat je iets bent in de samenleving",
            "de vraag hoe lang een mens kan leven als hij gezond eet en genoeg beweegt",
        ],
        antwoord=0,
        uitleg="Worden staat voor verandering, zijn voor wat blijft. Filosofen verschillen over wat het echte is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe koppelt Parmenides schijn en werkelijkheid aan worden en zijn?",
        opties=[
            "worden is schijn, het ware zijn is één en onveranderlijk",
            "alleen verandering is echt, wat blijft is maar schijn",
            "schijn en werkelijkheid zijn hetzelfde, alles is zoals het lijkt",
            "worden en zijn bestaan allebei even echt naast elkaar, zonder verschil",
        ],
        antwoord=0,
        uitleg="Voor Parmenides bedriegen de zintuigen ons. Het denken toont dat het zijn niet kan ontstaan of vergaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt voor Plato de echte werkelijkheid?",
        opties=[
            "in de wereld van de ideeën, eeuwig en onveranderlijk",
            "in de zichtbare wereld, die we met de zintuigen kennen",
            "in onze dromen, die ons de toekomst tonen",
            "in de wetten die de staat voor iedereen maakt",
        ],
        antwoord=0,
        uitleg="De zichtbare wereld van het worden is een schaduw of afbeelding. De ideeën zijn het ware zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kijkt Aristoteles naar worden en zijn?",
        opties=[
            "de vorm zit in de dingen, en worden is mogelijkheid die werkelijkheid wordt",
            "verandering bestaat niet, het zijn is één, eeuwig en onbeweeglijk",
            "de echte dingen bestaan enkel in een aparte wereld van ideeën",
            "alles is toeval, er zit geen vorm, orde of doel in de natuur rondom ons",
        ],
        antwoord=0,
        uitleg="Een eikel is in mogelijkheid een eik. Worden is voor Aristoteles echt en begrijpelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent transcendent?",
        opties=[
            "iets wat boven of buiten de ervaarbare wereld uitgaat",
            "iets wat volledig binnen de wereld van de dingen zelf ligt",
            "iets wat je met je zintuigen kunt meten en wegen",
            "iets wat enkel in een kunstwerk kan bestaan",
        ],
        antwoord=0,
        uitleg="Transcendent is het tegenovergestelde van immanent, wat binnen de wereld zelf ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de ideeënleer van Plato transcendent en de vormleer van Aristoteles immanent?",
        opties=[
            "bij Plato bestaan de ideeën los van de dingen, bij Aristoteles zit de vorm in de dingen",
            "bij Plato zit de vorm in de dingen, bij Aristoteles bestaan de ideeën erbuiten",
            "Plato geloofde helemaal niet in ideeën, Aristoteles wel",
            "Plato en Aristoteles waren het daarover volledig eens, zonder enig verschil",
        ],
        antwoord=0,
        uitleg="Aristoteles haalde de vorm als het ware uit de hemel van Plato terug naar de dingen zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Kant met het ding op zich?",
        opties=[
            "de werkelijkheid zoals ze in zichzelf is, onkenbaar voor ons",
            "een voorwerp dat je in je hand kunt nemen, meten en wegen",
            "het eerste ding dat een kind leert benoemen als het praat",
            "de vorm die Aristoteles in elk ding van de natuur zag zitten",
        ],
        antwoord=0,
        uitleg="Wij kennen enkel de dingen zoals ze aan ons verschijnen, door ons verstand en onze zintuigen heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken passen bij Kant?",
        opties=[
            "we kennen de verschijnselen, niet het ding op zich",
            "kennis blijft binnen de grenzen van de mogelijke ervaring",
            "met het verstand kunnen we God en de ziel even zeker kennen als een tafel",
            "de zintuigen geven ons rechtstreeks de werkelijkheid zoals ze in zichzelf is",
        ],
        antwoord=[0, 1],
        uitleg="Kant trekt een grens: wat buiten de ervaring ligt, is transcendent en kunnen we niet kennen.",
    ),
    dict(
        type="invultekst",
        vraag="Een ander woord voor de zijnsleer, uit het Grieks, is ...",
        antwoord=["ontologie", "metafysica"],
        uitleg="Ontologie is de leer van het zijnde. Metafysica is de ruimere naam voor dit domein.",
    ),
    dict(
        type="invultekst",
        vraag="Wat binnen de wereld of de dingen zelf ligt, noemt men ...",
        antwoord=["immanent"],
        uitleg="Het tegengestelde is transcendent: wat erboven of erbuiten ligt.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Parmenides is de verandering die we zien, een betrouwbaar beeld van de werkelijkheid.",
        antwoord=False,
        uitleg="Parmenides vindt net dat verandering schijn is. Het denken moet ons voorbij de zintuigen leiden.",
    ),
    dict(
        type="waarofniet",
        vraag="De grotallegorie van Plato kun je lezen als een beeld van schijn en werkelijkheid.",
        antwoord=True,
        uitleg="De schaduwen op de wand zijn de schijn. Buiten de grot, in het zonlicht, ligt de werkelijkheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Aristoteles plaatst de vormen in een aparte wereld, ver weg van de dingen.",
        antwoord=False,
        uitleg="Dat doet Plato. Aristoteles legt de vorm in de dingen zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Kant vindt dat ons verstand mee bepaalt hoe de werkelijkheid aan ons verschijnt.",
        antwoord=True,
        uitleg="Ruimte, tijd en oorzaak zijn volgens Kant vormen waarmee wij de ervaring ordenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stok in het water lijkt gebroken, maar is recht. Welk begrippenpaar illustreert dit?",
        opties=["schijn en werkelijkheid", "worden en zijn", "toeval en noodzaak", "individu en gemeenschap"],
        antwoord=0,
        uitleg="De zintuigen tonen iets anders dan wat er echt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rups wordt een vlinder. Hoe zou Aristoteles dat uitleggen?",
        opties=[
            "wat in mogelijkheid al in de rups zat, wordt werkelijkheid",
            "de verandering is schijn, er is in werkelijkheid niets gebeurd",
            "de rups is een slechte kopie van het idee van de vlinder",
            "het is puur toeval en heeft geen enkele richting",
        ],
        antwoord=0,
        uitleg="Voor Aristoteles is worden de verwerkelijking van een mogelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke denker hoort bij welke visie op de werkelijkheid?",
        opties=[
            "Parmenides: het zijn is één; Plato: ideeën los van de dingen; Aristoteles: vorm in de dingen",
            "Parmenides: alles verandert; Plato: vorm in de dingen; Aristoteles: ideeën los van de dingen",
            "Parmenides: vorm in de dingen; Plato: het zijn is één; Aristoteles: alles is toeval",
            "Parmenides: ideeën los van de dingen; Plato: alles is toeval; Aristoteles: het zijn is één",
        ],
        antwoord=0,
        uitleg="Dat is de lijn van streng monisme naar twee werelden naar één wereld met vorm en stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de vraag naar schijn en werkelijkheid ook belangrijk voor de kenleer?",
        opties=[
            "als de zintuigen misleiden, moet je weten hoe je toch iets kunt kennen",
            "omdat de kenleer alleen over kunst, smaak en schoonheid gaat",
            "omdat de zintuigen ons volgens alle filosofen nooit kunnen misleiden",
            "omdat schijn en werkelijkheid enkel in de ethiek en de politiek voorkomen",
        ],
        antwoord=0,
        uitleg="Zijnsleer en kenleer hangen samen: wat is er, en hoe kunnen we dat weten?",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Spinoza met noodzakelijkheid?",
        opties=[
            "alles volgt noodzakelijk uit God of de natuur, niets kon anders",
            "alles gebeurt toevallig, zonder enige oorzaak, reden of plan",
            "de mens kiest volledig vrij, los van elke oorzaak",
            "enkel de dingen die we zelf nodig hebben om te leven, bestaan echt",
        ],
        antwoord=0,
        uitleg="Voor Spinoza is er geen toeval: wie de oorzaken kent, ziet dat alles zo moest gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt David Hume over oorzaak en gevolg?",
        opties=[
            "we zien enkel dat dingen op elkaar volgen, de noodzakelijke band zelf zien we nooit",
            "we kunnen met het verstand alleen bewijzen dat elke oorzaak noodzakelijk een gevolg heeft",
            "oorzaak en gevolg bestaan enkel in de wereld van de ideeën",
            "elk gevolg is door God vooraf bepaald en dus noodzakelijk",
        ],
        antwoord=0,
        uitleg="De noodzaak is volgens Hume een gewoonte van onze geest. Zo krijgt het toeval meer ruimte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe hangt het toeval samen met het denken van Sartre?",
        opties=[
            "het bestaan van de mens is toevallig en heeft geen vooraf gegeven doel",
            "de mens heeft een vaste natuur die al zijn keuzes noodzakelijk bepaalt",
            "alles in het leven van de mens volgt een goddelijk plan dat vastligt",
            "de geschiedenis gaat noodzakelijk naar een vooraf bepaald einde",
        ],
        antwoord=0,
        uitleg="Sartre spreekt over de contingentie of toevalligheid van het bestaan. Een doel moet de mens zelf maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met doelgerichtheid of teleologie?",
        opties=[
            "dingen en gebeurtenissen zijn gericht op een doel",
            "alles gebeurt zonder richting, puur door toeval",
            "enkel mensen kunnen een doel hebben, de natuur nooit",
            "alles is vooraf vastgelegd door de stand van de sterren",
        ],
        antwoord=0,
        uitleg="Telos is Grieks voor doel. Het tegenovergestelde is een wereld waarin alles toevallig gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet Aristoteles doelgerichtheid in de natuur?",
        opties=[
            "elk ding streeft naar zijn eigen aard, zoals een eikel naar een eik",
            "de natuur heeft geen doelen, alles is blinde noodzaak zonder richting",
            "enkel de goden hebben een doel, de natuur volgt hen blind en zonder reden",
            "doelen bestaan enkel in de wereld van de ideeën, los van de dingen",
        ],
        antwoord=0,
        uitleg="Bij Aristoteles is het doel of telos de laatste oorzaak: waartoe iets er is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van de geschiedenis volgens Hegel?",
        opties=[
            "de geest groeit stap voor stap naar het besef van vrijheid",
            "de geschiedenis heeft geen enkel doel en is puur toeval",
            "de geschiedenis draait in een kring en herhaalt zich eindeloos",
            "de geschiedenis eindigt wanneer alle dingen opnieuw stof worden",
        ],
        antwoord=0,
        uitleg="Hegel ziet de geschiedenis als een proces met een richting, via tegenstellingen die telkens opgeheven worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke denkers verbinden we met toeval?",
        opties=["David Hume", "Jean-Paul Sartre", "Benedictus de Spinoza", "Georg Wilhelm Friedrich Hegel"],
        antwoord=[0, 1],
        uitleg="Spinoza staat voor noodzakelijkheid, Hegel voor doelgerichtheid in de geschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben existentialistische denkers gemeen in hun kijk op het bestaan?",
        opties=[
            "de wereld heeft geen vooraf gegeven zin, de mens moet die zelf geven",
            "de mens moet zich volledig aanpassen aan een vast plan van de natuur",
            "het bestaan van de mens is volledig door de stand van de sterren bepaald",
            "de mens kan pas gelukkig zijn als hij nergens meer over nadenkt of twijfelt",
        ],
        antwoord=0,
        uitleg="Bij Sartre, Camus en De Beauvoir staat de eigen keuze en verantwoordelijkheid centraal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noemt Albert Camus het absurde?",
        opties=[
            "de botsing tussen de mens die zin zoekt en een zwijgende wereld",
            "een grappige toneelvoorstelling zonder verhaal of duidelijk einde",
            "het geloof dat alles in de wereld een vast doel heeft",
            "de regel dat elke oorzaak in de natuur noodzakelijk een gevolg heeft",
        ],
        antwoord=0,
        uitleg="Camus gebruikt het beeld van Sisyphus, die steeds opnieuw zijn steen omhoog rolt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ziet Spinoza het begrijpen van de noodzaak als een vorm van vrijheid?",
        opties=[
            "wie begrijpt waarom alles gebeurt, wordt minder door angst gedreven",
            "wie de noodzaak begrijpt, kan de natuurwetten zelf veranderen",
            "omdat de noodzaak volgens Spinoza eigenlijk maar schijn is, zoals bij Parmenides",
            "omdat vrijheid voor Spinoza betekent dat je alles toevallig laat gebeuren",
        ],
        antwoord=0,
        uitleg="Vrijheid is voor Spinoza inzicht, niet het ontbreken van oorzaken.",
    ),
    dict(
        type="invultekst",
        vraag="De leer dat dingen gericht zijn op een doel, heet ...",
        antwoord=["teleologie", "doelgerichtheid"],
        uitleg="Telos betekent doel of einde.",
    ),
    dict(
        type="invultekst",
        vraag="De filosoof die zegt dat alles noodzakelijk uit God of de natuur volgt, is Benedictus de ...",
        antwoord=["Spinoza"],
        uitleg="Spinoza schreef de Ethica, in de vorm van een wiskundig bewijs.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Spinoza bestaat er echt toeval in de natuur.",
        antwoord=False,
        uitleg="Wat wij toeval noemen, is volgens Spinoza onwetendheid over de oorzaken.",
    ),
    dict(
        type="waarofniet",
        vraag="Hegel ziet de geschiedenis als een doelgericht proces.",
        antwoord=True,
        uitleg="De geschiedenis is voor Hegel de ontwikkeling van de geest naar vrijheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Hume kunnen we de noodzakelijke band tussen oorzaak en gevolg rechtstreeks waarnemen.",
        antwoord=False,
        uitleg="We zien enkel dat het ene op het andere volgt. De noodzaak voegen we er zelf aan toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor existentialisten heeft het leven niet vanzelf een vaste zin.",
        antwoord=True,
        uitleg="De mens moet zelf zin geven aan zijn bestaan door te kiezen en te handelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: 'Het moest zo gebeuren, alles heeft een oorzaak, en wie alle oorzaken kent, kan het begrijpen.' Bij welke denker past dit?",
        opties=["Spinoza", "Sartre", "Camus", "Hume"],
        antwoord=0,
        uitleg="Dat is het idee van noodzakelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: 'Er is geen plan voor mijn leven. Ik besta toevallig, en ik moet zelf kiezen wat ik ervan maak.' Bij welke denker past dit?",
        opties=["Sartre", "Spinoza", "Hegel", "Aristoteles"],
        antwoord=0,
        uitleg="Toeval van het bestaan en eigen keuze zijn typisch voor het existentialisme van Sartre.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan doelgerichtheid en toeval tegenover elkaar?",
        opties=[
            "doel zegt dat dingen een richting hebben, toeval dat het ook anders kon",
            "doelgerichtheid en toeval betekenen eigenlijk precies hetzelfde in de filosofie",
            "toeval bestaat enkel in de kunst, doelgerichtheid enkel in de wiskunde en de fysica",
            "doelgerichtheid gaat enkel over dieren, toeval enkel over planten en stenen",
        ],
        antwoord=0,
        uitleg="Het zijn twee verschillende antwoorden op de vraag waarom de dingen gaan zoals ze gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over noodzaak, toeval en doel klopt?",
        opties=[
            "Spinoza: noodzaak; Hume en Sartre: toeval; Aristoteles en Hegel: doel",
            "Spinoza: toeval; Hume en Hegel: noodzaak; Sartre en Aristoteles: doel",
            "Sartre: noodzaak; Aristoteles en Hume: toeval; Spinoza en Hegel: doel",
            "Hegel: toeval; Sartre en Spinoza: doel; Hume en Aristoteles: noodzaak",
        ],
        antwoord=0,
        uitleg="Dit is de verdeling van de denkers over de drie begrippen.",
    ),
]

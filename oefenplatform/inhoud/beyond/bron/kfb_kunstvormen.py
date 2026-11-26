# -*- coding: utf-8 -*-
"""Kunst, cultuur en de kunstvormen.

Het eerste thema van kunstbeschouwing in kunstbeschouwing en filosofie
🌍 Beyond doorstroom (fiche 3DDO, humane wetenschappen). De fiche vraagt:

    kunst als deel van een cultuur: de enge en de brede betekenis van cultuur
    de kunstvormen: architectuur en design; audiovisuele kunsten (film,
        fotografie, videokunst); beeldende kunsten (schilderkunst,
        beeldhouwkunst); conceptuele kunst en installatiekunst; literatuur;
        podiumkunsten (dans, theater, muziek)
    de middelen van vormgeving: bouwstenen, materialen, techniek, met in
        bijlage 1 de bouwstenen per kunstvorm (beeld, dans, drama, media,
        muziek)

Deel 1 zijn cultuur en de kunstvormen.
Deel 2 zijn de middelen van vormgeving en de bouwstenen uit bijlage 1.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoel je met cultuur in de enge betekenis?",
        opties=[
            "kunst en wat men vroeger de hogere vormen van beschaving noemde, zoals literatuur, muziek en schilderkunst",
            "alles wat een groep mensen aanleert en doorgeeft, van taal en gewoonten tot eetgewoonten",
            "enkel de gewoonten rond feesten en religieuze rituelen in een land",
            "de manier waarop een land zijn economie en zijn handel organiseert",
        ],
        antwoord=0,
        uitleg="In de enge betekenis is cultuur vooral kunst. In de brede betekenis is het alles wat mensen samen aanleren en doorgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoel je met cultuur in de brede betekenis?",
        opties=[
            "alles wat een groep mensen aanleert en doorgeeft: taal, waarden, gewoonten, kleding, eten en ook kunst",
            "enkel de kunstwerken die in een museum hangen of in een concertzaal klinken",
            "de kunst die door de overheid betaald wordt, zoals een stadsschouwburg",
            "de natuurlijke omgeving van een volk, zoals bergen, rivieren en klimaat",
        ],
        antwoord=0,
        uitleg="De brede betekenis omvat de hele manier van leven van een groep. Kunst is daar één deel van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden horen bij cultuur in de brede betekenis, maar niet bij de enge?",
        opties=[
            "de manier waarop een familie samen het nieuwjaar viert",
            "de gewoonte om elkaar bij het begroeten drie kussen te geven",
            "een symfonie in een concertzaal",
            "een roman van een bekende schrijver",
        ],
        antwoord=[0, 1],
        uitleg="Feestgewoonten en begroetingen zijn cultuur in de brede zin. Een symfonie en een roman zijn kunst en horen ook bij de enge betekenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt men dat kunst een deel van een cultuur is?",
        opties=[
            "kunst toont en beïnvloedt de waarden, gewoonten en vragen van de groep waarin ze ontstaat",
            "kunst ontstaat altijd los van de samenleving, enkel uit het hoofd van de kunstenaar",
            "elke cultuur maakt exact dezelfde soort kunst als alle andere culturen",
            "kunst bestaat pas sinds er musea zijn, dus sinds de moderne tijd",
        ],
        antwoord=0,
        uitleg="Kunst groeit uit een cultuur en zegt er iets over. Ze kan die cultuur ook mee vormen of in vraag stellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke kunstvorm behoren film, fotografie en videokunst?",
        opties=["audiovisuele kunsten", "beeldende kunsten", "podiumkunsten", "conceptuele kunst"],
        antwoord=0,
        uitleg="Audiovisueel betekent met beeld en geluid, of met een camera gemaakt. Film, fotografie en videokunst horen daarbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke kunstvorm behoren dans, theater en muziek?",
        opties=["podiumkunsten", "audiovisuele kunsten", "beeldende kunsten", "installatiekunst"],
        antwoord=0,
        uitleg="Podiumkunsten worden live voor een publiek uitgevoerd, meestal op een podium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee kunsten noemt men beeldende kunsten?",
        opties=["schilderkunst", "beeldhouwkunst", "dans", "fotografie"],
        antwoord=[0, 1],
        uitleg="Schilderkunst en beeldhouwkunst zijn beeldende kunsten. Dans is een podiumkunst en fotografie een audiovisuele kunst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kunstenaar vult een lege zaal met honderden oude stoelen, waar de bezoekers tussen moeten lopen. Welke kunstvorm herken je?",
        opties=["installatiekunst", "beeldhouwkunst", "podiumkunst", "architectuur en design"],
        antwoord=0,
        uitleg="Bij installatiekunst richt de kunstenaar een hele ruimte in, en de bezoeker staat er middenin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat voorop in conceptuele kunst?",
        opties=[
            "het idee achter het werk, meer dan het afgewerkte voorwerp of het vakmanschap",
            "een zo getrouw mogelijke weergave van een landschap of een persoon",
            "de ambachtelijke techniek van het schilderen met olieverf in dunne lagen",
            "het verhaal van een toneelstuk dat acteurs op een podium spelen",
        ],
        antwoord=0,
        uitleg="Bij conceptuele kunst is het concept, het idee, het eigenlijke kunstwerk. Het voorwerp is soms bijzaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ontwerper tekent een stoel die mooi is, maar vooral goed moet zitten en in een fabriek gemaakt kan worden. Bij welke kunstvorm hoort dit?",
        opties=["architectuur en design", "beeldhouwkunst", "conceptuele kunst", "installatiekunst"],
        antwoord=0,
        uitleg="Design verbindt vorm met gebruik. Net als bij architectuur moet het ontwerp ook werken.",
    ),
    dict(
        type="invultekst",
        vraag="Dans, theater en muziek horen bij de ...kunsten.",
        antwoord=["podium", "podiumkunsten"],
        uitleg="Podiumkunsten worden live uitgevoerd voor een publiek.",
    ),
    dict(
        type="invultekst",
        vraag="Kunst waarbij de kunstenaar een volledige ruimte inricht, zodat de bezoeker er middenin staat, heet ...kunst.",
        antwoord=["installatie", "installatiekunst"],
        uitleg="De ruimte zelf hoort bij het werk. De bezoeker beleeft het door erin rond te lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Literatuur is een van de kunstvormen.",
        antwoord=True,
        uitleg="Romans, gedichten en toneelteksten zijn kunst met taal als materiaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Fotografie hoort bij de beeldende kunsten, net als schilderkunst.",
        antwoord=False,
        uitleg="In deze indeling hoort fotografie bij de audiovisuele kunsten, samen met film en videokunst.",
    ),
    dict(
        type="waarofniet",
        vraag="Gewoonten rond eten en feesten horen bij cultuur in de brede betekenis.",
        antwoord=True,
        uitleg="De brede betekenis omvat alles wat een groep aanleert en doorgeeft, niet alleen kunst.",
    ),
    dict(
        type="waarofniet",
        vraag="In de enge betekenis van cultuur gaat het vooral over taal, kleding en eetgewoonten.",
        antwoord=False,
        uitleg="Dat is de brede betekenis. De enge betekenis gaat vooral over kunst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fotograaf maakt een reeks zwart-witportretten van mijnwerkers. Welke kunstvorm is dit?",
        opties=["audiovisuele kunst", "beeldende kunst", "literatuur", "podiumkunst"],
        antwoord=0,
        uitleg="Fotografie hoort in deze indeling bij de audiovisuele kunsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gebouw wordt ook als kunstwerk bekeken. Waarom is architectuur dan anders dan een schilderij?",
        opties=[
            "een gebouw moet ook bruikbaar zijn en wordt van binnen en van buiten beleefd",
            "een gebouw heeft nooit een boodschap of een functie buiten het wonen",
            "architectuur kan geen kunst zijn omdat je ze niet in een museum kan hangen",
            "een gebouw wordt altijd door één enkele kunstenaar met de hand gemaakt",
        ],
        antwoord=0,
        uitleg="Architectuur combineert vorm met gebruik. Je loopt erin rond en het moet een doel dienen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een choreograaf maakt een voorstelling waarin zes dansers bewegen op live muziek. Welke kunstvormen komen samen?",
        opties=["podiumkunsten", "audiovisuele kunsten", "architectuur en design", "beeldende kunsten"],
        antwoord=0,
        uitleg="Dans en muziek zijn allebei podiumkunsten. Ze worden live gebracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kunstenaar schrijft op een muur enkel de zin: dit werk bestaat pas als jij erover nadenkt. Welke kunstvorm herken je het best?",
        opties=["conceptuele kunst", "literatuur", "beeldhouwkunst", "design"],
        antwoord=0,
        uitleg="Het idee is hier het werk. Dat is typisch voor conceptuele kunst.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie middelen van vormgeving onderscheidt men?",
        opties=["bouwstenen", "materialen", "techniek", "opdrachtgever"],
        antwoord=[0, 1, 2],
        uitleg="Bouwstenen, materialen en techniek zijn de middelen. De opdrachtgever hoort bij de context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de bouwstenen van een kunstwerk?",
        opties=[
            "de basiselementen waarmee het werk is opgebouwd, zoals kleur, lijn en licht bij beeld",
            "de stenen en het cement waarmee een gebouw of een beeld gemaakt wordt",
            "de mensen die het werk hebben betaald en besteld",
            "de musea en galerieën waar het werk getoond wordt",
        ],
        antwoord=0,
        uitleg="Bouwstenen zijn de elementen waarmee een kunstenaar vormgeeft. Ze verschillen per kunstvorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bouwstenen bij beeld?",
        opties=["kleur", "licht", "melodie", "tempo"],
        antwoord=[0, 1],
        uitleg="Bij beeld zijn vorm, kleur, licht, textuur, lijn, ruimte en compositie de bouwstenen. Melodie hoort bij muziek, tempo bij muziek, dans of drama.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kijkt of een schilderij veel of weinig contrast heeft tussen licht en donker. Welke bouwsteen onderzoek je?",
        opties=["licht", "lijn", "textuur", "vorm"],
        antwoord=0,
        uitleg="Bij licht kijk je naar een heldere of donkere indruk, schaduwen en het contrast tussen licht en donker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je merkt dat de verf dik en ruw is aangebracht met een paletmes. Welke bouwsteen beschrijf je?",
        opties=["textuur", "kleur", "compositie", "ruimte"],
        antwoord=0,
        uitleg="Textuur gaat over het oppervlak: ruw of glad, en met welk instrument het gemaakt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat de belangrijkste figuren op een schilderij samen een denkbeeldige driehoek vormen. Welke bouwsteen is dat?",
        opties=["compositie", "lijn", "vorm", "licht"],
        antwoord=0,
        uitleg="Compositie gaat over de spreiding en rangschikking van de elementen, soms in een geometrische figuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat er perspectief is en dat de figuren aan de rand afgesneden zijn. Welke bouwsteen beschrijf je?",
        opties=["ruimte", "textuur", "kleur", "licht"],
        antwoord=0,
        uitleg="Bij ruimte kijk je naar perspectief, het ruimtelijk effect van schaduw en afgesneden figuren aan de rand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bouwstenen horen bij muziek?",
        opties=["ritme", "klankkleur", "perspectief", "textuur van verf"],
        antwoord=[0, 1],
        uitleg="Bij muziek zijn ritme, melodie, dynamiek, tempo, klankkleur, harmonie en structuur de bouwstenen. Perspectief en textuur van verf horen bij beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stuk muziek begint zacht en wordt steeds luider. Welke bouwsteen beschrijf je?",
        opties=["klanksterkte of dynamiek", "klankkleur", "melodie", "structuur"],
        antwoord=0,
        uitleg="Een crescendo is een kwestie van klanksterkte of dynamiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hoort dat de hoofdmelodie door een cello gespeeld wordt. Welke bouwsteen beschrijf je?",
        opties=["klankkleur", "tempo", "ritme", "harmonie"],
        antwoord=0,
        uitleg="Klankkleur gaat over welk instrument of welke stem de melodie brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een film kijk je of er veel close-ups zijn en of de camera van boven of van onder filmt. Welke bouwsteen bij media is dat?",
        opties=["kader", "montage", "geluid", "licht"],
        antwoord=0,
        uitleg="Kader gaat over het type shot en het perspectief, zoals vogel- of kikkerperspectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een filmmaker gebruikt slow motion en laat twee beelden zacht in elkaar overvloeien. Welke bouwsteen bij media is dat?",
        opties=["montage", "camera", "kader", "geluid"],
        antwoord=0,
        uitleg="Montage gaat over de overgangen tussen shots, fades en de snelheid van de gemonteerde beelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een dansvoorstelling bewegen de dansers niet synchroon en spelen ze in op elkaars bewegingen. Welke bouwsteen bij dans beschrijf je?",
        opties=["relatie", "kracht", "tijd", "ruimte"],
        antwoord=0,
        uitleg="Relatie gaat over synchroon dansen of niet, inspelen op elkaar en interactie met het publiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bouwstenen horen bij drama of theater?",
        opties=["rol", "samenspel", "structuur", "klankkleur"],
        antwoord=[0, 1, 2],
        uitleg="Bij drama zijn rol, ruimte, tijd, structuur en samenspel de bouwstenen. Klankkleur hoort bij muziek.",
    ),
    dict(
        type="invultekst",
        vraag="Het oppervlak van een werk, ruw of glad, regelmatig of onregelmatig, noem je de ...",
        antwoord=["textuur"],
        uitleg="Textuur hangt ook af van de drager en het instrument, zoals een penseel, een spons of een spuitbus.",
    ),
    dict(
        type="invultekst",
        vraag="Bij beeld noem je de spreiding en de rangschikking van de elementen de ...",
        antwoord=["compositie"],
        uitleg="De compositie bepaalt waar je oog eerst naartoe gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="De bouwstenen zijn voor elke kunstvorm dezelfde.",
        antwoord=False,
        uitleg="Elke kunstvorm heeft eigen bouwstenen. Bij beeld is dat onder meer kleur en compositie, bij muziek ritme en melodie, bij dans kracht en relatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Materiaal en techniek zijn ook middelen van vormgeving, naast de bouwstenen.",
        antwoord=True,
        uitleg="Waarmee iets gemaakt is (materiaal) en hoe (techniek) zijn de twee andere middelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Tempo is een bouwsteen die je onderzoekt bij een schilderij.",
        antwoord=False,
        uitleg="Tempo hoort bij muziek, dans of drama, kunstvormen die in de tijd verlopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij beeld hoort bij de bouwsteen kleur ook de vraag of de kleuren realistisch of onrealistisch zijn.",
        antwoord=True,
        uitleg="Bij kleur kijk je naar primaire of secundaire kleuren, realistisch of niet, en fel of zacht.",
    ),
]

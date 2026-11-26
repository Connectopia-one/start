# -*- coding: utf-8 -*-
"""Middeleeuwen, renaissance en barok.

Vierde thema kunstbeschouwing (fiche 3DDO, kunsthistorisch referentiekader):
basiskenmerken (context en vormelijke kenmerken) en de bekendste
vertegenwoordigers van

    kunst van de middeleeuwen: romaans, gotiek, Vlaamse primitieven
    renaissance
    barok

Bekende namen en werken uit elk handboek: Jan van Eyck (Lam Gods,
Arnolfiniportret), Leonardo da Vinci, Michelangelo, Rafaël, Rubens,
Rembrandt, Caravaggio, Bernini, de Notre-Dame en de kathedraal van Chartres.

Deel 1 zijn de middeleeuwen (romaans, gotiek, Vlaamse primitieven).
Deel 2 zijn renaissance en barok.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie was in de middeleeuwen de belangrijkste opdrachtgever voor kunst?",
        opties=[
            "de kerk",
            "de fabrieksbazen uit de steden",
            "de musea van de grote steden",
            "het volk dat kaartjes kocht voor een tentoonstelling",
        ],
        antwoord=0,
        uitleg="Kerken, kloosters en bisschoppen bestelden het meeste werk. Kunst moest het geloof uitleggen en eren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij een romaanse kerk?",
        opties=[
            "dikke muren en kleine ramen",
            "rondbogen",
            "spitsbogen en enorme glasramen",
            "luchtbogen aan de buitenkant om de muren te steunen",
        ],
        antwoord=[0, 1],
        uitleg="Romaanse kerken zijn zwaar en eerder donker. Spitsbogen, grote glasramen en luchtbogen zijn gotisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wilden gotische bouwmeesters bereiken met hoge gewelven en grote glasramen?",
        opties=[
            "een lichte, hoge ruimte die naar de hemel en naar God wijst",
            "een donkere, gesloten ruimte die bescherming bood tegen aanvallen",
            "een zo goedkoop mogelijke kerk met weinig stenen",
            "een gebouw dat leek op een Romeinse tempel",
        ],
        antwoord=0,
        uitleg="Licht stond voor het goddelijke. De gotiek wilde hoogte en licht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke techniek maakte het mogelijk dat gotische muren dunner werden, met grotere ramen?",
        opties=["luchtbogen en steunberen", "de rondboog", "de koepel van beton", "het tongewelf"],
        antwoord=0,
        uitleg="Luchtbogen vangen de druk van het gewelf op aan de buitenkant. Zo hoeft de muur niet alles te dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kathedraal is een bekend voorbeeld van gotiek?",
        opties=[
            "de Notre-Dame van Parijs",
            "het Pantheon van Rome",
            "het Parthenon van Athene",
            "het Colosseum van Rome",
        ],
        antwoord=0,
        uitleg="De Notre-Dame van Parijs en de kathedraal van Chartres zijn schoolvoorbeelden van gotiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor de manier waarop middeleeuwse schilders vóór de Vlaamse primitieven heiligen afbeeldden?",
        opties=[
            "vlak, met een gouden achtergrond en zonder echte diepte",
            "met een wiskundig berekend perspectief en een verdwijnpunt",
            "als gewone mensen in een realistisch landschap met licht en schaduw",
            "met wilde penseelstreken en felle onnatuurlijke kleuren",
        ],
        antwoord=0,
        uitleg="De gouden achtergrond toont een hemelse, tijdloze wereld. Diepte was niet het doel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie schilderde, samen met zijn broer Hubert, het Lam Gods in Gent?",
        opties=["Jan van Eyck", "Rubens", "Rembrandt", "Leonardo da Vinci"],
        antwoord=0,
        uitleg="Het Lam Gods is een veelluik in de Sint-Baafskathedraal van Gent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de Vlaamse primitieven bekend?",
        opties=[
            "olieverf in dunne lagen, met heel veel details",
            "echte stoffen, juwelen en spiegelingen",
            "grote, snelle penseelstreken zonder details",
            "abstracte vlakken zonder herkenbare figuren",
        ],
        antwoord=[0, 1],
        uitleg="Met dunne lagen olieverf toonden ze glans, stof en spiegelingen tot in het kleinste detail.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heten de Vlaamse primitieven zo?",
        opties=[
            "men zag hen later als de eersten van een nieuwe schilderkunst in de Nederlanden",
            "ze werkten met heel primitief gereedschap uit de steentijd",
            "ze schilderden vooral grotten en jachttaferelen",
            "ze konden nog geen olieverf maken en gebruikten modder",
        ],
        antwoord=0,
        uitleg="Primitief betekent hier de eersten, niet ongeschoold. Hun techniek was net heel verfijnd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk werk van Jan van Eyck toont een koppel in een kamer, met een bolle spiegel aan de muur?",
        opties=[
            "het Arnolfiniportret",
            "de Nachtwacht",
            "de Schepping van Adam",
            "de Kruisafneming",
        ],
        antwoord=0,
        uitleg="In de spiegel zie je de kamer en twee kleine figuren. De Nachtwacht is van Rembrandt.",
    ),
    dict(
        type="invultekst",
        vraag="Een gekleurd raam uit stukjes glas in lood, typisch voor de gotiek, heet een ...",
        antwoord=["glasraam", "brandglasraam", "glas-in-loodraam"],
        uitleg="De glasramen vertelden bijbelverhalen aan mensen die niet konden lezen.",
    ),
    dict(
        type="invultekst",
        vraag="Een schilderij uit meerdere panelen, zoals het Lam Gods, heet een ...",
        antwoord=["veelluik", "polyptiek", "retabel"],
        uitleg="Met twee panelen is het een tweeluik, met drie een drieluik.",
    ),
    dict(
        type="waarofniet",
        vraag="De gotische bouwstijl gebruikt de spitsboog.",
        antwoord=True,
        uitleg="De spitsboog leidt de druk beter af dan de rondboog. Daardoor kon men hoger bouwen.",
    ),
    dict(
        type="waarofniet",
        vraag="Middeleeuwse kunst toonde vooral alledaagse taferelen en had weinig met het geloof te maken.",
        antwoord=False,
        uitleg="De meeste middeleeuwse kunst was religieus: ze toonde bijbelverhalen en heiligen.",
    ),
    dict(
        type="waarofniet",
        vraag="Romaanse kerken zijn meestal lichter dan gotische kerken.",
        antwoord=False,
        uitleg="Het is omgekeerd. Romaanse kerken hebben kleine ramen en dikke muren, gotische kerken veel glas.",
    ),
    dict(
        type="waarofniet",
        vraag="De Vlaamse primitieven werkten vooral in steden zoals Brugge en Gent.",
        antwoord=True,
        uitleg="In de 15de eeuw waren die steden rijk door handel. Rijke burgers bestelden er ook kunst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien paneel: een heilige in een kamer met een open raam naar een stad, met piepkleine details in stoffen, metaal en glas, in heldere olieverf. Uit welke stroming komt het wellicht?",
        opties=["Vlaamse primitieven", "barok", "romaanse kunst", "Romeinse kunst"],
        antwoord=0,
        uitleg="De fijne details in olieverf en het doorkijkje naar een stad zijn typisch voor de Vlaamse primitieven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien gebouw: hoge spitse torens, grote ronde rozetvensters, spitsbogen en luchtbogen aan de buitenkant. Welke stijl is dat?",
        opties=["gotiek", "romaans", "barok", "Griekse architectuur"],
        antwoord=0,
        uitleg="Spitsbogen, luchtbogen en grote glasramen zijn de kenmerken van de gotiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vertelden kerken bijbelverhalen in beelden en glasramen?",
        opties=[
            "de meeste mensen konden niet lezen, dus de beelden legden het geloof uit",
            "boeken bestonden nog niet in de middeleeuwen, ook niet met de hand geschreven",
            "het was verboden om in de kerk te spreken",
            "de beelden waren goedkoper dan kaarsen",
        ],
        antwoord=0,
        uitleg="Kunst had een didactische, verhalende functie: men noemde ze wel de bijbel van de armen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde er bij de Vlaamse primitieven tegenover de oudere middeleeuwse schilderkunst?",
        opties=[
            "de heiligen staan in een herkenbare, realistische wereld met kamers en landschappen",
            "ze stopten helemaal met religieuze onderwerpen",
            "ze gingen weer op grotwanden schilderen",
            "ze schilderden alleen nog met goud zonder figuren",
        ],
        antwoord=0,
        uitleg="Het onderwerp bleef vaak religieus, maar de wereld errond werd realistisch en gedetailleerd.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het woord renaissance?",
        opties=[
            "wedergeboorte, van de kunst en kennis van de klassieke oudheid",
            "het einde van alle kunst en wetenschap in Europa na de pest",
            "de nieuwe kunst van de fabrieken en de grote steden",
            "het geloof dat de wereld plat is",
        ],
        antwoord=0,
        uitleg="Men greep terug naar de Grieken en Romeinen. Dat begon in de 15de eeuw in Italië, vooral in Florence.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij de schilderkunst van de renaissance?",
        opties=[
            "het lijnperspectief met een verdwijnpunt",
            "de mens als middelpunt, met juiste verhoudingen",
            "een gouden achtergrond zonder diepte",
            "vlakke figuren met het hoofd van opzij en het oog van voren",
        ],
        antwoord=[0, 1],
        uitleg="Het perspectief gaf diepte, de mens kreeg een centrale plaats. De gouden achtergrond is middeleeuws, de aspectieve figuur Egyptisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het humanisme, de denkwijze achter de renaissance?",
        opties=[
            "de mens, zijn verstand en zijn mogelijkheden staan centraal",
            "alles in het leven draait enkel om het hiernamaals en de hemel",
            "de mens is niet belangrijk, enkel de natuur en de dieren tellen",
            "kunst mag geen mensen afbeelden",
        ],
        antwoord=0,
        uitleg="Humanisten bestudeerden de klassieke teksten en hadden veel vertrouwen in wat de mens kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie schilderde de Mona Lisa?",
        opties=["Leonardo da Vinci", "Michelangelo", "Rafaël", "Rembrandt"],
        antwoord=0,
        uitleg="Leonardo da Vinci was schilder, uitvinder en wetenschapper tegelijk, een echte renaissancemens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werken zijn van Michelangelo?",
        opties=[
            "het marmeren beeld David",
            "het plafond van de Sixtijnse Kapel",
            "de Nachtwacht",
            "het Lam Gods",
        ],
        antwoord=[0, 1],
        uitleg="Michelangelo was beeldhouwer en schilder. De Nachtwacht is van Rembrandt, het Lam Gods van Van Eyck.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sfumato, een techniek van Leonardo da Vinci?",
        opties=[
            "zachte, wazige overgangen zonder harde lijnen",
            "felle kleuren pal naast elkaar zonder enige overgang",
            "schilderen met stukjes glas in lood",
            "beelden uit brons gieten",
        ],
        antwoord=0,
        uitleg="Sfumato betekent als rook. De Mona Lisa heeft zo een zacht, geheimzinnig gezicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij de barok?",
        opties=[
            "veel beweging en diagonalen",
            "sterke contrasten van licht en donker",
            "rust, symmetrie en strakke horizontale lijnen",
            "vlakke figuren met een gouden achtergrond",
        ],
        antwoord=[0, 1],
        uitleg="De barok wil de kijker meeslepen met drama, beweging en licht. Rust en symmetrie passen beter bij de renaissance.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het sterke contrast tussen licht en donker, dat Caravaggio vaak gebruikte?",
        opties=["clair-obscur", "sfumato", "contrapposto", "perspectief"],
        antwoord=0,
        uitleg="Clair-obscur of chiaroscuro: figuren komen fel uit een donkere achtergrond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunstenaar uit Antwerpen is een groot meester van de barok?",
        opties=["Rubens", "Jan van Eyck", "Michelangelo", "Leonardo da Vinci"],
        antwoord=0,
        uitleg="Rubens schilderde grote, bewogen werken zoals de Kruisoprichting en de Kruisafneming in de kathedraal van Antwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liet de katholieke kerk in de barok veel indrukwekkende kunst maken?",
        opties=[
            "als antwoord op de reformatie wilde ze gelovigen ontroeren en de pracht van het geloof tonen",
            "omdat de kerk geld wilde verdienen met de verkoop van schilderijen aan musea",
            "omdat de kerk alle religieuze kunst wilde laten verdwijnen",
            "omdat de kunstenaars weigerden voor koningen te werken",
        ],
        antwoord=0,
        uitleg="Dat heet de contrareformatie. Kunst moest het gevoel aanspreken en het geloof versterken.",
    ),
    dict(
        type="invultekst",
        vraag="Een techniek waarbij evenwijdige lijnen samenkomen in één verdwijnpunt, heet het ...",
        antwoord=["lijnperspectief", "perspectief", "centraal perspectief"],
        uitleg="Zo krijgt een plat schilderij diepte. Het werd in de renaissance in Florence uitgewerkt.",
    ),
    dict(
        type="invultekst",
        vraag="De Nederlandse schilder van de Nachtwacht heet ...",
        antwoord=["Rembrandt", "Rembrandt van Rijn"],
        uitleg="Rembrandt is bekend voor zijn spel met licht en donker en zijn zelfportretten.",
    ),
    dict(
        type="waarofniet",
        vraag="De renaissance begon in Italië.",
        antwoord=True,
        uitleg="Vooral in Florence, met rijke opdrachtgevers zoals de familie Medici.",
    ),
    dict(
        type="waarofniet",
        vraag="Barokkunst is meestal rustig, sober en zonder veel versiering.",
        antwoord=False,
        uitleg="Barok is net bewogen, dramatisch en rijk versierd.",
    ),
    dict(
        type="waarofniet",
        vraag="In de renaissance kregen ook rijke families en vorsten, naast de kerk, een grote rol als opdrachtgever.",
        antwoord=True,
        uitleg="Families zoals de Medici in Florence bestelden schilderijen, beelden en paleizen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bernini was vooral een schilder van kleine portretten.",
        antwoord=False,
        uitleg="Bernini was een barokbeeldhouwer en architect in Rome, bekend voor bewogen marmeren beelden en het Sint-Pietersplein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien schilderij: een rustige, symmetrische scène in een gebouw met zuilen, alle lijnen lopen naar één punt in het midden, de figuren hebben juiste verhoudingen. Uit welke stroming komt het wellicht?",
        opties=["renaissance", "barok", "gotiek", "Vlaamse primitieven"],
        antwoord=0,
        uitleg="Symmetrie, rust, perspectief met één verdwijnpunt en klassieke zuilen wijzen op de renaissance.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien schilderij: figuren in een sterke diagonale beweging, wapperende kleren, fel licht dat uit het donker valt, veel emotie. Uit welke stroming komt het wellicht?",
        opties=["barok", "renaissance", "romaanse kunst", "Egyptische kunst"],
        antwoord=0,
        uitleg="Beweging, diagonalen, drama en clair-obscur zijn typisch voor de barok.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een groot verschil tussen renaissance en barok?",
        opties=[
            "de renaissance zoekt rust en evenwicht, de barok zoekt beweging en emotie",
            "de renaissance is altijd abstract, de barok altijd realistisch",
            "de renaissance gebruikt nog geen perspectief, de barok wel voor het eerst",
            "de renaissance komt in de tijd pas na de barok, als reactie erop",
        ],
        antwoord=0,
        uitleg="De barok komt na de renaissance en breekt de rust open met beweging en drama.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom past een groot doek van Rubens met veel beweging goed in een barokke kerk?",
        opties=[
            "het moest de gelovigen raken en meeslepen, net zoals de rijk versierde kerk zelf",
            "het was het enige formaat dat Rubens in zijn atelier kon schilderen",
            "barokke kerken mochten geen beelden bevatten, enkel grote schilderijen",
            "het diende vooral om de koude muren van de kerk te isoleren in de winter",
        ],
        antwoord=0,
        uitleg="Functie en vorm horen samen: een werk dat wil ontroeren, kiest voor groot, bewogen en dramatisch.",
    ),
]

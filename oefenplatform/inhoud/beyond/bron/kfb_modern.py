# -*- coding: utf-8 -*-
"""Van romantiek tot popart: moderne en hedendaagse kunst.

Vijfde thema kunstbeschouwing (fiche 3DDO, kunsthistorisch referentiekader):

    kunst van de moderne tijd: romantiek, realisme, impressionisme, ...
    kunst uit de hedendaagse tijd: popart, ...
    verband tussen stromingen: romantiek als reactie op het neoclassicisme,
    realisme als reactie op de romantiek, modernisme als reactie op de
    veranderende wereld (industriële revolutie, nieuwe technologie),
    postmodernisme als reactie op het modernisme

Bekende namen: David (neoclassicisme), Delacroix, Turner en Friedrich
(romantiek), Courbet en Millet (realisme), Monet en Renoir (impressionisme),
Van Gogh, Munch, Picasso, Mondriaan, Warhol en Lichtenstein (popart).

Deel 1: neoclassicisme, romantiek, realisme, impressionisme.
Deel 2: modernisme, popart, postmodernisme, en de stromingen als reactie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar haalde het neoclassicisme, rond 1800, zijn voorbeeld?",
        opties=[
            "bij de kunst van de Griekse en Romeinse oudheid",
            "bij de grotschilderingen uit de prehistorie",
            "bij de Japanse houtsneden uit de 19de eeuw",
            "bij de reclame en de strips uit de krant",
        ],
        antwoord=0,
        uitleg="Neo betekent nieuw: men greep opnieuw terug naar de klassieke oudheid, met strakke lijnen, rust en helden uit de geschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke schilder hoort bij het neoclassicisme?",
        opties=["Jacques-Louis David", "Claude Monet", "Andy Warhol", "Vincent van Gogh"],
        antwoord=0,
        uitleg="David schilderde strakke, heldhaftige taferelen, zoals De eed van de Horatii en De dood van Marat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stond centraal in de romantiek?",
        opties=[
            "gevoel, verbeelding en de macht van de natuur",
            "het verstand, regels en strakke symmetrie",
            "het gewone werk van boeren en arbeiders, zonder opsmuk",
            "felle reclamebeelden en bekende merken uit de winkel",
        ],
        antwoord=0,
        uitleg="De romantiek stelde het gevoel boven het verstand: stormen, ruïnes, verlangen en het onbekende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunstenaars horen bij de romantiek?",
        opties=["Eugène Delacroix", "Caspar David Friedrich", "Gustave Courbet", "Roy Lichtenstein"],
        antwoord=[0, 1],
        uitleg="Delacroix schilderde De vrijheid leidt het volk, Friedrich De wandelaar boven de nevelzee. Courbet is realisme, Lichtenstein popart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wilden de realisten in het midden van de 19de eeuw tonen?",
        opties=[
            "het gewone leven zoals het is, ook armoede en zwaar werk",
            "dromen en nachtmerries die niet in de werkelijkheid bestaan",
            "heldendaden uit de Griekse en Romeinse geschiedenis",
            "enkel kleurvlakken en lijnen, zonder herkenbare figuren",
        ],
        antwoord=0,
        uitleg="Realisten zoals Courbet en Millet schilderden boeren, arbeiders en gewone mensen, zonder ze mooier te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk werk hoort bij het realisme?",
        opties=[
            "De arenlezeressen van Millet",
            "De vrijheid leidt het volk van Delacroix",
            "Impressie, opkomende zon van Monet",
            "Marilyn Monroe van Warhol",
        ],
        antwoord=0,
        uitleg="Millet toont drie vrouwen die achtergebleven aren oprapen: zwaar, gewoon werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wilden de impressionisten vastleggen?",
        opties=[
            "de indruk van een moment, met het veranderende licht",
            "een verhaal uit de bijbel met veel details",
            "een perfect afgewerkt beeld zonder zichtbare penseelstreek",
            "een strak geometrisch patroon van rechte lijnen",
        ],
        antwoord=0,
        uitleg="Ze schilderden vaak buiten, snel, met losse toetsen, om het licht van dat ogenblik te vangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken passen bij het impressionisme?",
        opties=[
            "losse, zichtbare penseelstreken",
            "lichte kleuren en schilderen in open lucht",
            "donkere achtergronden met fel licht op één figuur",
            "strakke contouren en vlakke kleuren zoals in een strip",
        ],
        antwoord=[0, 1],
        uitleg="Het donkere clair-obscur hoort bij de barok, de strakke contouren bij de popart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van welk schilderij kreeg het impressionisme zijn naam?",
        opties=[
            "Impressie, opkomende zon van Claude Monet",
            "De Nachtwacht van Rembrandt",
            "De Schreeuw van Edvard Munch",
            "De eed van de Horatii van David",
        ],
        antwoord=0,
        uitleg="Een criticus gebruikte die titel spottend. De schilders namen de naam daarna zelf over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitvinding uit de 19de eeuw maakte het voor impressionisten makkelijker om buiten te schilderen?",
        opties=[
            "verf in tubes die je kon meenemen",
            "de elektrische lamp in het atelier",
            "de computer met tekenprogramma",
            "het glas in lood voor ramen",
        ],
        antwoord=0,
        uitleg="Met verf in tubes en een draagbare ezel kon je overal schilderen, ook langs de rivier of in een veld.",
    ),
    dict(
        type="invultekst",
        vraag="De stroming die gevoel, natuurkrachten en verbeelding boven het verstand plaatst, heet de ...",
        antwoord=["romantiek"],
        uitleg="De romantiek kwam op rond 1800, als reactie op het strakke neoclassicisme.",
    ),
    dict(
        type="invultekst",
        vraag="De schilder van de reeksen waterlelies en de kathedraal van Rouen heet Claude ...",
        antwoord=["Monet"],
        uitleg="Monet schilderde hetzelfde onderwerp vaak opnieuw, telkens in ander licht.",
    ),
    dict(
        type="waarofniet",
        vraag="De romantiek ontstond als reactie op het neoclassicisme.",
        antwoord=True,
        uitleg="Tegenover de strakke regels en het verstand van het neoclassicisme zette de romantiek gevoel en verbeelding.",
    ),
    dict(
        type="waarofniet",
        vraag="Het realisme wilde de werkelijkheid mooier en heldhaftiger tonen dan ze was.",
        antwoord=False,
        uitleg="Net niet: het realisme wilde de werkelijkheid tonen zoals ze is, ook het zware en lelijke.",
    ),
    dict(
        type="waarofniet",
        vraag="Impressionisten gebruikten vaak zwart om schaduwen te schilderen.",
        antwoord=False,
        uitleg="Ze schilderden schaduwen liever met kleur, zoals blauw of paars, omdat schaduw in het licht ook kleur heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="De uitvinding van de fotografie speelde mee in de vernieuwing van de schilderkunst in de 19de eeuw.",
        antwoord=True,
        uitleg="De foto kon de werkelijkheid vastleggen. Schilders zochten daarom andere dingen, zoals licht, indruk en gevoel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien schilderij: een eenzame figuur op een rots, op de rug gezien, boven een woeste zee in de mist. Uit welke stroming komt het wellicht?",
        opties=["romantiek", "realisme", "popart", "neoclassicisme"],
        antwoord=0,
        uitleg="De eenzame mens tegenover de grote natuur is een typisch beeld van de romantiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien schilderij: een zonnige tuin, snelle kleurtoetsen naast elkaar, geen harde lijnen, het licht schittert op het water. Uit welke stroming komt het wellicht?",
        opties=["impressionisme", "barok", "realisme", "neoclassicisme"],
        antwoord=0,
        uitleg="Losse toetsen, licht en een moment buiten wijzen op het impressionisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom reageerde het realisme tegen de romantiek?",
        opties=[
            "het vond de romantiek te dromerig en wilde het echte leven van gewone mensen tonen",
            "het vond de romantiek te nuchter en wilde meer dromen en verbeelding",
            "het wilde opnieuw strakke Griekse helden en tempels schilderen",
            "het wilde stoppen met schilderen en enkel nog foto's maken",
        ],
        antwoord=0,
        uitleg="Tegenover verbeelding en drama zette het realisme de gewone, vaak harde werkelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatschappelijke context hoort bij het realisme?",
        opties=[
            "de industriële revolutie, met arbeiders, armoede en sociale onrust",
            "de bouw van de piramiden in het oude Egypte",
            "de bloeitijd van de kloosters in de vroege middeleeuwen",
            "de opkomst van televisie en reclame na 1950",
        ],
        antwoord=0,
        uitleg="De snelle veranderingen en de harde omstandigheden van gewone mensen kregen aandacht in de kunst.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waartegen reageerde het modernisme, rond 1900?",
        opties=[
            "tegen een snel veranderende wereld, met fabrieken, steden en nieuwe technologie",
            "tegen de komst van de computer en het internet in elk huis",
            "tegen de bouw van romaanse kerken met dikke muren en kleine ramen in de dorpen",
            "tegen de Egyptische regels voor het tekenen van mensen",
        ],
        antwoord=0,
        uitleg="Modernisten zochten een nieuwe kunst voor een nieuwe tijd en braken met oude regels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor het expressionisme?",
        opties=[
            "felle, onnatuurlijke kleuren en vervormde figuren om een gevoel te tonen",
            "een zo juist mogelijke kopie van de werkelijkheid, zoals een foto",
            "rustige, symmetrische scènes met klassieke zuilen en een verdwijnpunt in het midden",
            "beelden uit reclame, strips en bekende merken uit de winkel, in herhaling",
        ],
        antwoord=0,
        uitleg="De kunstenaar toont wat hij voelt, niet hoe iets er echt uitziet. Denk aan De Schreeuw van Munch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deden Picasso en Braque in het kubisme?",
        opties=[
            "ze toonden een onderwerp van verschillende kanten tegelijk, in hoekige vlakken",
            "ze schilderden het licht van één moment met losse toetsen",
            "ze maakten zachte, wazige overgangen zonder lijnen, zoals in de Mona Lisa",
            "ze kopieerden stripplaatjes met grote stippen en vergrootten ze op doek",
        ],
        antwoord=0,
        uitleg="Het kubisme brak het ene standpunt van het perspectief open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor de abstracte werken van Mondriaan?",
        opties=[
            "rechte zwarte lijnen en vlakken in rood, geel en blauw",
            "realistische landschappen met molens en koeien",
            "bewogen figuren in clair-obscur, met fel licht uit een donkere achtergrond",
            "foto's van filmsterren in felle kleuren, vele keren herhaald",
        ],
        antwoord=0,
        uitleg="Mondriaan herleidde alles tot lijnen en primaire kleuren, zonder herkenbaar onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar haalde de popart in de jaren 1950 en 1960 zijn beelden?",
        opties=[
            "uit reclame, strips, film en producten uit de winkel",
            "uit de bijbel en de levens van de heiligen",
            "uit de Griekse mythologie en de Romeinse geschiedenis",
            "uit de natuur, met stormen, bergen en ruïnes",
        ],
        antwoord=0,
        uitleg="Popart komt van popular art: de kunst van de massacultuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunstenaars horen bij de popart?",
        opties=["Andy Warhol", "Roy Lichtenstein", "Claude Monet", "Peter Paul Rubens"],
        antwoord=[0, 1],
        uitleg="Warhol maakte de soepblikken en Marilyn Monroe, Lichtenstein vergrote stripplaatjes met stippen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maakte Andy Warhol vaak hetzelfde beeld vele keren met zeefdruk?",
        opties=[
            "om te tonen hoe beelden en producten in de massacultuur eindeloos herhaald worden",
            "omdat hij niet kon tekenen en dus enkel foto's mocht gebruiken",
            "omdat de kerk hem dat vroeg voor een groot altaarstuk in een kathedraal",
            "om het veranderende licht van één bepaald moment buiten vast te leggen",
        ],
        antwoord=0,
        uitleg="Zijn atelier heette The Factory. Hij werkte zoals een fabriek die hetzelfde product maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor postmodernisme?",
        opties=[
            "het mengt stijlen, citeert oude kunst en speelt met humor en ironie",
            "het zoekt één zuivere stijl en verbiedt elke versiering",
            "het kopieert de natuur zo exact mogelijk, zoals een foto, zonder enige humor",
            "het toont enkel religieuze taferelen voor kerken, in opdracht van de bisschop",
        ],
        antwoord=0,
        uitleg="Het postmodernisme gelooft niet in één juiste weg. Alles mag gemengd en opnieuw gebruikt worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstond het postmodernisme?",
        opties=[
            "als reactie op het modernisme, dat streng zocht naar één nieuwe, zuivere vorm",
            "als reactie op de gotiek, die volgens de kunstenaars veel te veel glasramen gebruikte",
            "als reactie op de prehistorische kunst in de grotten van Lascaux en Altamira",
            "als reactie op het verbod om kunst te verkopen aan musea en verzamelaars",
        ],
        antwoord=0,
        uitleg="Het modernisme was ernstig en zocht vernieuwing. Het postmodernisme reageerde met spel en mengvormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke schilder uit Nederland, met felle kleuren en dikke, draaiende penseelstreken, wordt vaak bij het begin van het expressionisme genoemd?",
        opties=["Vincent van Gogh", "Rembrandt", "Jan van Eyck", "Piet Mondriaan"],
        antwoord=0,
        uitleg="Van Gogh werkte na het impressionisme. Zijn kleuren en lijnen drukken vooral gevoel uit.",
    ),
    dict(
        type="invultekst",
        vraag="De stroming die beelden uit reclame, strips en massacultuur gebruikt, heet de ...",
        antwoord=["popart", "pop-art", "pop art"],
        uitleg="Popart ontstond in Groot-Brittannië en de Verenigde Staten in de jaren 1950 en 1960.",
    ),
    dict(
        type="invultekst",
        vraag="De stroming van Picasso en Braque, met hoekige vlakken en meerdere standpunten tegelijk, heet het ...",
        antwoord=["kubisme"],
        uitleg="Kubus betekent blokje. Een criticus vond de werken op blokjes lijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Popart maakte een duidelijk onderscheid tussen hoge kunst en alledaagse producten zoals soepblikken.",
        antwoord=False,
        uitleg="Popart vervaagde net dat onderscheid: een soepblik kon kunst worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het modernisme hangt samen met de industriële revolutie en nieuwe technologieën.",
        antwoord=True,
        uitleg="Fabrieken, treinen, fotografie en grote steden veranderden de wereld. Kunstenaars zochten een kunst die daarbij paste.",
    ),
    dict(
        type="waarofniet",
        vraag="Abstracte kunst toont altijd een duidelijk herkenbaar onderwerp.",
        antwoord=False,
        uitleg="Abstracte kunst laat het herkenbare onderwerp net los. Vorm, lijn en kleur zijn het onderwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="De barok kan je zien als een reactie op de rust en het evenwicht van de renaissance.",
        antwoord=True,
        uitleg="De barok brak de rust open met beweging, drama en contrast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien werk: een groot stripplaatje van een huilende vrouw, met dikke zwarte lijnen, felle vlakke kleuren en zichtbare rasterstippen. Uit welke stroming komt het wellicht?",
        opties=["popart", "impressionisme", "romantiek", "kubisme"],
        antwoord=0,
        uitleg="Strip, stippen en vlakke kleuren zijn typisch voor de popart, zoals bij Lichtenstein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien portret: een gezicht uit hoekige vlakken, de neus van opzij en de ogen van voren, in bruine en grijze tinten. Uit welke stroming komt het wellicht?",
        opties=["kubisme", "realisme", "renaissance", "impressionisme"],
        antwoord=0,
        uitleg="Meerdere standpunten tegelijk en hoekige vlakken wijzen op het kubisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke volgorde ontstonden deze kunststromingen?",
        opties=[
            "neoclassicisme, romantiek, realisme, impressionisme, popart",
            "romantiek, popart, neoclassicisme, impressionisme, realisme",
            "impressionisme, realisme, neoclassicisme, popart, romantiek",
            "popart, impressionisme, romantiek, realisme, neoclassicisme",
        ],
        antwoord=0,
        uitleg="Rond 1800 neoclassicisme, dan romantiek, rond 1850 realisme, vanaf 1870 impressionisme, na 1950 popart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband tussen stromingen klopt?",
        opties=[
            "de renaissance reageerde op de middeleeuwen door terug te grijpen naar de klassieke oudheid",
            "de romantiek reageerde op de popart door meer reclame te gebruiken",
            "het realisme reageerde op het impressionisme door nog losser en sneller te schilderen",
            "de gotiek reageerde op de barok door opnieuw kleinere ramen en dikkere muren te bouwen",
        ],
        antwoord=0,
        uitleg="De andere verbanden kloppen niet in de tijd: een stroming kan niet reageren op iets wat pas later komt.",
    ),
]

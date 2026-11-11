# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Het ademhalingsstelsel.

Biologie, blok "Stofwisselingsfysiologie en secretie", kop "Het
ademhalingsstelsel". Deel 1 gaat over de bouw van het ademhalingsstelsel en
de ademhalingsbewegingen, deel 2 over gaswisseling, hemoglobine, het
spirogram en de aandoeningen.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "In welke volgorde gaat ingeademde lucht door de luchtwegen?",
        [
            "neusholte, keelholte, strottenhoofd, luchtpijp, bronchiën, bronchiolen, longblaasjes",
            "neusholte, luchtpijp, keelholte, strottenhoofd, bronchiolen, bronchiën, longblaasjes",
            "keelholte, neusholte, bronchiën, luchtpijp, strottenhoofd, longblaasjes, bronchiolen",
            "neusholte, strottenhoofd, keelholte, bronchiolen, luchtpijp, bronchiën, longblaasjes",
        ],
        0,
        "De lucht gaat van de neus- of mondholte naar de keelholte, het strottenhoofd en de luchtpijp. Die splitst in bronchiën en bronchiolen, die eindigen in de longblaasjes.",
    ),
    M(
        "Wat doet de neusholte met de ingeademde lucht? Kruis alles aan wat juist is.",
        ["ze verwarmt de lucht", "ze droogt de lucht uit", "ze filtert stofdeeltjes uit de lucht", "ze haalt de zuurstof uit de lucht"],
        [0, 2],
        "Neusschelpen, slijmvlies en haartjes verwarmen, bevochtigen en zuiveren de lucht. Ze drogen de lucht dus niet uit. De zuurstof wordt pas in de longblaasjes opgenomen.",
    ),
    M(
        "Wat is de taak van het trilhaarepitheel met slijmcellen in de luchtwegen?",
        [
            "stof en ziektekiemen in slijm vangen en naar de keel afvoeren",
            "zuurstof uit de lucht opnemen en meteen aan het bloed in de haarvaten geven",
            "de luchtpijp stevig openhouden bij het inademen",
            "geluid maken wanneer de lucht langs de stembanden gaat",
        ],
        0,
        "Het slijm vangt deeltjes op en de trilhaartjes slaan het naar boven, naar de keel. Daar slik je het in of hoest je het op.",
    ),
    M(
        "Wat houdt de luchtpijp altijd open, ook als je inademt?",
        ["kraakbeenringen in de wand", "de druk van het bloed", "het middenrif", "het longvlies"],
        0,
        "Hoefijzervormige kraakbeenringen houden de luchtpijp open. Aan de achterkant zijn ze open, zodat de slokdarm erachter kan uitzetten bij het slikken.",
    ),
    I(
        "Hoe heten de kleine luchtzakjes aan het einde van de bronchiolen, waar de gaswisseling gebeurt?",
        ["longblaasjes", "alveolen"],
        "De longen tellen honderden miljoenen longblaasjes. Samen hebben ze een oppervlak zo groot als een tennisveld.",
    ),
    M(
        "Waarom zijn de longblaasjes goed geschikt voor gaswisseling? Kruis alles aan wat juist is.",
        [
            "ze hebben samen een enorm groot oppervlak",
            "hun wand is erg dun",
            "ze zijn omringd door een dicht net van haarvaten",
            "ze hebben een dikke laag kraakbeen in hun wand",
        ],
        [0, 1, 2],
        "Groot oppervlak, een wand van één cel dik en veel haarvaten zorgen voor snelle diffusie van O₂ en CO₂. Kraakbeen zit enkel in de grotere luchtwegen.",
    ),
    W(
        "De rechterlong heeft drie longkwabben en de linkerlong twee.",
        True,
        "De linkerlong is iets kleiner en heeft maar twee kwabben, want aan de linkerkant ligt het hart.",
    ),
    M(
        "Wat is de pleuraholte?",
        [
            "de dunne ruimte met vocht tussen het longvlies en het borstvlies",
            "de holte binnen in de luchtpijp waar de lucht door stroomt",
            "de ruimte in het strottenhoofd waar de stembanden liggen",
            "de holte tussen de neusschelpen in de neus, waar de lucht verwarmd wordt",
        ],
        0,
        "Het longvlies bekleedt de long, het borstvlies de binnenkant van de borstkas. Het pleuravocht daartussen laat de long soepel meebewegen.",
    ),
    M(
        "Wat gebeurt er bij de inademing met de middenrifademhaling?",
        [
            "het middenrif trekt samen en wordt platter, zodat de borstholte groter wordt",
            "het middenrif ontspant en bolt op, zodat de borstholte kleiner wordt en lucht binnenstroomt",
            "de buikspieren duwen de longen omhoog en de lucht naar binnen",
            "de longen zuigen zich zelf vol lucht door hun eigen spieren",
        ],
        0,
        "Als het middenrif samentrekt, zakt het. De borstholte wordt groter, de druk in de longen daalt en lucht stroomt naar binnen.",
    ),
    M(
        "Zet de stappen van de inademing in de juiste volgorde.",
        [
            "ademhalingsspieren trekken samen, de borstholte wordt groter, de druk in de longen daalt, lucht stroomt naar binnen",
            "lucht stroomt naar binnen, de druk in de longen daalt, de borstholte wordt groter, de ademhalingsspieren trekken samen",
            "de druk in de longen stijgt, de borstholte wordt kleiner, de ademhalingsspieren ontspannen, lucht stroomt naar binnen",
            "de borstholte wordt groter, de ademhalingsspieren ontspannen, lucht stroomt naar buiten, de druk in de longen daalt",
        ],
        0,
        "De spieren werken eerst. Daardoor vergroot de borstholte, daalt de druk onder de luchtdruk buiten, en volgt de lucht.",
    ),
    W(
        "De longen zetten bij het inademen zelf uit omdat ze eigen spieren hebben.",
        False,
        "De longen hebben geen spieren om zelf uit te zetten. Ze volgen de beweging van de borstkas en het middenrif, dankzij het pleuravocht.",
    ),
    M(
        "Welke spieren zorgen bij de ribademhaling voor het optillen van de ribben?",
        ["de tussenribspieren", "de buikspieren", "de kringspieren van de luchtpijp", "de spieren van het strottenhoofd"],
        0,
        "Bij de ribademhaling of borstademhaling heffen de tussenribspieren de ribben op. De borstkas wordt breder en dieper.",
    ),
    W(
        "Bij een rustige uitademing ontspannen de ademhalingsspieren en veert de borstkas vanzelf terug.",
        True,
        "Een rustige uitademing is passief. Alleen bij een krachtige uitademing, zoals bij hoesten, helpen de buikspieren actief mee.",
    ),
    M(
        "Welke ribben zijn rechtstreeks met het borstbeen verbonden?",
        ["de ware ribben", "de valse ribben", "de zwevende ribben", "geen enkele rib"],
        0,
        "De ware ribben zitten met hun eigen kraakbeen vast aan het borstbeen. Valse ribben zijn onrechtstreeks verbonden en zwevende ribben helemaal niet.",
    ),
    I(
        "Hoe heet het klepje dat bij het slikken de ingang van het strottenhoofd afsluit?",
        "strottenklepje",
        "Het strottenklepje belet dat voedsel in de luchtpijp terechtkomt. Gebeurt dat toch, dan verslik je je en hoest je het eruit.",
    ),
    M(
        "Hoe heet de plaats waar de hoofdbronchus, de bloedvaten en de zenuwen de long binnengaan?",
        ["de longhilus", "de longkwab", "het longtrechtertje", "de pleuraholte"],
        0,
        "Bij de longhilus, aan de binnenkant van de long, komen de bronchus, de longslagader, de longaders en de zenuwen de long in en uit.",
    ),
    W(
        "Bij de buikademhaling bewegen vooral de tussenribspieren, en het middenrif blijft stil.",
        False,
        "Buik- of middenrifademhaling gebeurt vooral door het middenrif. De tussenribspieren zorgen voor de borst- of ribademhaling.",
    ),
    M(
        "Waar zit het strottenhoofd?",
        [
            "tussen de keelholte en de luchtpijp, met de stembanden erin",
            "tussen de luchtpijp en de bronchiën, onder het borstbeen in de borstkas",
            "tussen de neusholte en de mondholte, achter het verhemelte",
            "tussen de longen en het middenrif, onder in de borstkas",
        ],
        0,
        "Het strottenhoofd of larynx ligt boven aan de luchtpijp. Aan de buitenkant voel je de adamsappel. Binnenin zitten de stembanden.",
    ),
    M(
        "Waarom krijgen rokers vaak last van slijm en hoesten?",
        [
            "rook beschadigt de trilharen, zodat het slijm niet meer goed afgevoerd wordt",
            "rook maakt de luchtpijp breder, zodat er meer stof binnenkomt",
            "rook verdubbelt het aantal longblaasjes, die dan meer slijm maken",
            "rook verlaagt de lichaamstemperatuur in de luchtwegen",
        ],
        0,
        "Rook verlamt en beschadigt de trilharen. Het slijm blijft liggen en moet opgehoest worden: de typische rokershoest.",
    ),
    W(
        "De gaswisseling tussen lucht en bloed gebeurt in de luchtpijp en de bronchiën.",
        False,
        "Luchtpijp en bronchiën zijn enkel aanvoerwegen. De gaswisseling gebeurt in de longblaasjes, waar de wand dun genoeg is.",
    ),
]

DEEL2 = [
    M(
        "Hoe gaan zuurstof en koolstofdioxide in de longblaasjes van de lucht naar het bloed en omgekeerd?",
        ["door diffusie", "door actief transport met ATP", "door fagocytose", "door filtratie onder hoge druk"],
        0,
        "Gassen diffunderen van een plaats met hoge naar een plaats met lage partiële druk. Daar is geen energie voor nodig.",
    ),
    M(
        "Waarom gaat zuurstof in de longblaasjes het bloed in?",
        [
            "de partiële druk van O₂ is in de longblaasjes hoger dan in het bloed van de haarvaten",
            "de partiële druk van O₂ is in het bloed hoger dan in de longblaasjes",
            "hemoglobine pompt de zuurstof actief uit de longblaasjes naar binnen",
            "de bloeddruk in de longen zuigt de zuurstof door de wand",
        ],
        0,
        "Het bloed dat in de longen aankomt, is zuurstofarm. Zuurstof diffundeert dus van de longblaasjes naar het bloed.",
    ),
    M(
        "Bij welke omstandigheden laat hemoglobine zuurstof makkelijker los? Kruis alles aan wat juist is.",
        ["een hogere temperatuur", "een hogere CO₂-concentratie", "een hogere pH, dus basischer", "een hogere O₂-concentratie"],
        [0, 1],
        "In werkende spieren is het warmer, er is meer CO₂ en het is zuurder, dus de pH is lager. De zuurstofaffiniteit van hemoglobine daalt dan en de zuurstof komt vrij waar ze nodig is.",
    ),
    M(
        "Deoxyhemoglobine + O₂ ⇌ oxyhemoglobine. Naar welke kant verschuift dit evenwicht in de longblaasjes, volgens het principe van Le Chatelier?",
        [
            "naar rechts, want de O₂-concentratie is er hoog",
            "naar links, want de O₂-concentratie is er hoog",
            "naar rechts, want de CO₂-concentratie is er hoog",
            "het verschuift niet, want het is een evenwicht",
        ],
        0,
        "In de longen is er veel zuurstof. Het evenwicht verschuift naar de kant die zuurstof wegwerkt: er ontstaat oxyhemoglobine.",
    ),
    W(
        "In de weefsels verschuift het evenwicht tussen deoxyhemoglobine en oxyhemoglobine naar de kant van deoxyhemoglobine.",
        True,
        "In de weefsels is weinig zuurstof. Het evenwicht verschuift naar links, oxyhemoglobine geeft zijn zuurstof af en wordt weer deoxyhemoglobine.",
    ),
    I(
        "Hoe noemt men de mate waarin hemoglobine zuurstof bindt en vasthoudt?",
        ["zuurstofaffiniteit", "affiniteit"],
        "Een hoge zuurstofaffiniteit betekent dat hemoglobine zuurstof stevig vasthoudt, zoals in de longen. In actieve weefsels daalt de affiniteit.",
    ),
    M(
        "Op welke manieren wordt CO₂ van de weefsels naar de longen vervoerd? Kruis alles aan wat juist is.",
        [
            "opgelost in het plasma",
            "gebonden aan hemoglobine",
            "als waterstofcarbonaat (HCO₃⁻) in het plasma",
            "gebonden aan de bloedplaatjes",
        ],
        [0, 1, 2],
        "Een klein deel CO₂ is gewoon opgelost, een deel zit aan hemoglobine en het grootste deel reist als waterstofcarbonaat in het plasma.",
    ),
    W(
        "Het grootste deel van het CO₂ wordt aan hemoglobine gebonden vervoerd.",
        False,
        "De meeste CO₂, ongeveer 70 %, reist als waterstofcarbonaat in het plasma. Ongeveer een vijfde zit aan hemoglobine en de rest is opgelost.",
    ),
    M(
        "Wat is een spirogram?",
        [
            "een grafiek van het volume lucht dat iemand in- en uitademt in de tijd",
            "een grafiek van de elektrische activiteit van het hart tijdens de inspanning",
            "een foto van de longen gemaakt met röntgenstralen",
            "een meting van de hoeveelheid zuurstof in het bloed",
        ],
        0,
        "Met een spirometer meet men hoeveel lucht iemand in- en uitademt. Op het spirogram lees je onder meer het ademvolume en de vitale capaciteit af.",
    ),
    I(
        "Hoe heet de hoeveelheid lucht die je bij een gewone, rustige ademhaling in- en uitademt?",
        ["ademvolume", "ademvolume in rust"],
        "Het ademvolume in rust is ongeveer een halve liter. Daarbovenop kan je nog veel meer lucht in- of uitademen.",
    ),
    M(
        "Wat is de vitale capaciteit?",
        [
            "de grootste hoeveelheid lucht die je na een maximale inademing kan uitademen",
            "de hoeveelheid lucht die na een maximale uitademing in de longen blijft",
            "de hoeveelheid lucht die je per minuut in rust inademt",
            "de hoeveelheid lucht in de luchtpijp en de bronchiën",
        ],
        0,
        "De vitale capaciteit is ademvolume plus complementair volume plus uitademingsreservevolume. Bij een volwassene is dat zo'n vier à vijf liter.",
    ),
    M(
        "Wat is het restvolume?",
        [
            "de lucht die na een maximale uitademing nog in de longen blijft",
            "de lucht die je bij een rustige ademhaling in- en uitademt",
            "de lucht die je na een gewone inademing nog extra kan inademen",
            "de lucht die je na een gewone uitademing nog extra kan uitademen",
        ],
        0,
        "Het restvolume kan je niet uitademen. Het houdt de longblaasjes open. Vitale capaciteit en restvolume samen vormen de totale longcapaciteit.",
    ),
    W(
        "Het complementair volume is de lucht die je na een gewone inademing nog extra kan inademen.",
        True,
        "Het complementair volume is de extra lucht bij een diepe inademing. Samen met het ademvolume vormt het de inademingscapaciteit.",
    ),
    M(
        "Welke factoren kunnen de vitale capaciteit beïnvloeden? Kruis alles aan wat juist is.",
        ["de leeftijd", "het geslacht", "roken", "veel sporten"],
        [0, 1, 2, 3],
        "Alle vier spelen mee. De vitale capaciteit daalt met de leeftijd en door roken, en ze is gemiddeld groter bij mannen en bij wie veel sport.",
    ),
    M(
        "Wat gebeurt er bij een astma-aanval?",
        [
            "de bronchiolen vernauwen en zwellen op, zodat ademen moeilijk gaat",
            "de longblaasjes vullen zich met bloed door een gebarsten ader in de long",
            "het middenrif verlamt tijdelijk en de longen vallen samen",
            "de luchtpijp verstopt volledig door een stuk voedsel",
        ],
        0,
        "Bij astma verkrampen de spiertjes rond de bronchiolen, het slijmvlies zwelt op en er komt meer slijm. Een puffer laat de luchtwegen weer verwijden.",
    ),
    M(
        "Wat is mucoviscidose?",
        [
            "een erfelijke ziekte waarbij taai slijm de luchtwegen en de alvleesklier verstopt",
            "een infectie van de longen door een virus dat via de lucht van mens op mens overgaat",
            "een allergie voor pollen die vooral in de lente voorkomt",
            "een ontsteking van de stembanden door te luid te roepen",
        ],
        0,
        "Mucoviscidose of taaislijmziekte is erfelijk. Het taaie slijm geeft longinfecties en verstoort de spijsvertering. Kinesitherapie en medicatie helpen het slijm los te maken.",
    ),
    M(
        "Wat gebeurt er bij hyperventilatie?",
        [
            "je ademt te snel en te diep, zodat je te veel CO₂ uitademt",
            "je ademt te traag, zodat er te veel CO₂ in het bloed blijft",
            "je longblaasjes vullen zich met vocht door een infectie",
            "je luchtpijp vernauwt door een allergische reactie",
        ],
        0,
        "Door te snel te ademen daalt het CO₂-gehalte in het bloed. Dat geeft tintelingen, duizeligheid en een benauwd gevoel. Rustig en traag ademen helpt.",
    ),
    W(
        "Mucoviscidose is besmettelijk en wordt overgedragen via hoesten en niezen.",
        False,
        "Mucoviscidose is een erfelijke aandoening en niet besmettelijk. Het kind erft van beide ouders een afwijkend gen.",
    ),
    W(
        "Regelmatig sporten kan de vitale capaciteit vergroten.",
        True,
        "Training versterkt de ademhalingsspieren, waardoor je dieper kan in- en uitademen. Daardoor neemt de vitale capaciteit toe.",
    ),
    M(
        "Waaruit bestaat de totale longcapaciteit?",
        [
            "de vitale capaciteit plus het restvolume",
            "het ademvolume plus het complementair volume",
            "het restvolume plus het ademvolume",
            "de inademingscapaciteit plus het ademvolume",
        ],
        0,
        "De totale longcapaciteit is alle lucht die de longen na een maximale inademing bevatten: de vitale capaciteit en het restvolume samen.",
    ),
]

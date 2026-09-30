# -*- coding: utf-8 -*-
"""De vragen voor "Geloof, kunst en macht in de middeleeuwen".

Uit de vakfiche: de christelijke samenleving (bekering van West-Europa, de
organisatie van de Kerk, de houding tegenover andere godsdiensten en
minderheden, de invloed op het dagelijkse leven), kunst en cultuur (romaans en
gotisch, de Vlaamse primitieven, het middeleeuwse mens- en wereldbeeld, de
geleerdheid), de strijd om de macht (Frankrijk, Engeland, de Guldensporenslag)
en de niet-westerse samenleving: het Arabische Rijk, de zijderoutes en de
kruistochten.

Deel 1 gaat over geloof en kunst. Deel 2 over macht en over het contact met de
islamitische wereld.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe verspreidde het christendom zich over West-Europa?",
        opties=[
            "missionarissen bekeerden eerst de vorst, en daarna zijn volk",
            "elk gezin koos vrij en persoonlijk voor het nieuwe geloof",
            "Romeinse soldaten legden het overal met geweld op",
            "het kwam mee met de handelaars uit Azië",
        ],
        antwoord=0,
        uitleg="Bekeerde je de koning, dan volgde zijn hofhouding en daarna zijn onderdanen. Daarom is de doop van Clovis zo'n keerpunt.",
    ),
    dict(
        type="waarofniet",
        vraag="Oude gewoonten verdwenen niet altijd: sommige feesten en gebruiken kregen gewoon een christelijke betekenis.",
        antwoord=True,
        uitleg="Een midwinterfeest werd Kerstmis, een bron werd een heiligenbron. Dat samengaan is precies de versmelting van Germaanse, Romeinse en christelijke gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe was de katholieke Kerk in de middeleeuwen opgebouwd?",
        opties=[
            "als een piramide met de paus bovenaan, dan bisschoppen en pastoors",
            "als een vereniging waarin elke gelovige evenveel te zeggen had",
            "als een aantal losse kerken zonder onderling verband",
            "als een onderdeel van het leger van de koning",
        ],
        antwoord=0,
        uitleg="Die vaste ordening gaf de Kerk een macht die over de grenzen van vorstendommen heen reikte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een geestelijke die in een klooster leeft volgens een regel?",
        antwoord="een monnik",
        uitleg="Bidden, werken en studeren volgens een vaste regel. Benedictus schreef de bekendste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rollen vervulden de kloosters naast het gebed?",
        opties=[
            "ze kopieerden en bewaarden oude teksten",
            "ze ontgonnen woeste grond tot landbouwgrond",
            "ze zorgden voor zieken en reizigers",
            "ze sloegen de munten van de koning",
        ],
        antwoord=[0, 1, 2],
        uitleg="Munten slaan was een recht van de vorst. De drie andere taken maakten van een klooster een centrum van de streek.",
    ),
    dict(
        type="waarofniet",
        vraag="De Kerk bepaalde mee het ritme van het dagelijkse leven.",
        antwoord=True,
        uitleg="De klokken gaven de uren aan, de zondag en de feestdagen de week en het jaar, en doop, huwelijk en begrafenis de levensloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is ketterij in de middeleeuwse betekenis?",
        opties=[
            "een geloofsopvatting die van de leer van de Kerk afwijkt",
            "het weigeren van belastingen aan de koning",
            "het spreken van een andere taal dan het Latijn",
            "het verlaten van je geboortedorp zonder toestemming",
        ],
        antwoord=0,
        uitleg="Omdat geloof en samenleving samenvielen, werd afwijken van de leer ook als een aanval op de orde zelf gezien.",
    ),
    dict(
        type="waarofniet",
        vraag="Joden hadden in de middeleeuwse steden dezelfde rechten als christenen.",
        antwoord=False,
        uitleg="Ze mochten vaak geen grond bezitten en geen ambacht uitoefenen, moesten soms apart wonen of een kenteken dragen, en werden bij rampen zoals de pest als zondebok aangewezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je een middeleeuwse bron over joden extra kritisch lezen?",
        opties=[
            "ze is bijna altijd door een christelijke auteur geschreven, met zijn beeld van de ander",
            "ze is zonder uitzondering vervalst, meestal door een latere kopiist van het handschrift",
            "ze is nooit bewaard gebleven, want zulke teksten werden systematisch vernietigd",
            "ze is nooit in het Latijn geschreven maar altijd in een streektaal die weinigen lazen",
        ],
        antwoord=0,
        uitleg="De stem van de groep zelf ontbreekt meestal. Wat je leest, is het beeld dat men van hen had, niet noodzakelijk hun leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor diende christelijke kunst voor wie niet kon lezen?",
        opties=[
            "als een verhaal in beeld: glasramen, beelden en muurschilderingen vertelden de Bijbel",
            "als versiering zonder verdere betekenis, enkel bedoeld om de muren op te vrolijken",
            "als bewijs van de rijkdom van de bouwheer, en verder als niets anders dan dat",
            "als een geheimtaal die enkel de monniken van het klooster konden ontcijferen",
        ],
        antwoord=0,
        uitleg="Men noemde een kerk daarom wel eens de bijbel van de armen. Ook vandaag verspreidt die kunst nog waarden, in gebouwen die er nog staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij een romaans bouwwerk?",
        opties=[
            "rondbogen",
            "dikke muren met kleine vensters",
            "een zware, gesloten en donkere indruk",
            "luchtbogen aan de buitenkant",
        ],
        antwoord=[0, 1, 2],
        uitleg="Luchtbogen horen bij de gotiek. De romaanse kerk moet haar gewicht met dikke muren dragen, en dus blijven de vensters klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakte de gotische kerk lichter en hoger dan de romaanse?",
        opties=[
            "spitsbogen, kruisribgewelven en luchtbogen vangen het gewicht op",
            "men gebruikte voortaan veel lichtere steensoorten uit verre groeven",
            "men bouwde de muren in hout in plaats van in zware natuursteen",
            "men liet het dak gewoon weg en liet de kerk vanboven open staan",
        ],
        antwoord=0,
        uitleg="Draagt het geraamte het gewicht, dan hoeft de muur dat niet meer. Daar kunnen dan grote glasramen in.",
    ),
    dict(
        type="waarofniet",
        vraag="Romaans en gotisch verschillen enkel in de versiering, niet in de bouwtechniek.",
        antwoord=False,
        uitleg="Het verschil zit juist in de techniek: de rondboog duwt naar buiten, de spitsboog vooral naar beneden. Dat verandert het hele gebouw.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de boog met een punt bovenaan, kenmerkend voor de gotiek?",
        antwoord="een spitsboog",
        uitleg="Ze leidt het gewicht steiler naar beneden dan een rondboog, zodat de muren dunner mogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men Jan van Eyck en zijn tijdgenoten de Vlaamse primitieven?",
        opties=[
            "omdat ze bij de eersten waren die met olieverf zo gedetailleerd schilderden",
            "omdat hun werk ruw en onafgewerkt is in vergelijking met wat later kwam",
            "omdat ze enkel met houtskool tekenden en nooit met verf hebben gewerkt",
            "omdat ze uit een primitieve samenleving kwamen zonder steden of handel",
        ],
        antwoord=0,
        uitleg="Primitief betekent hier eerste, niet onbeholpen. Het Lam Gods in Gent toont hoe ver die techniek al stond.",
    ),
    dict(
        type="waarofniet",
        vraag="In het middeleeuwse wereldbeeld stond de aarde in het midden en was alles door God geordend.",
        antwoord=True,
        uitleg="Elk wezen had zijn vaste plaats in die ordening, van steen tot engel. Ook de standenleer past in dat beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je dat een middeleeuwse kaart geen aardrijkskundige kaart is zoals wij die kennen?",
        opties=[
            "Jeruzalem staat in het midden en het oosten bovenaan",
            "ze is op perkament of papier getekend in plaats van gedrukt",
            "ze gebruikt kleuren om land en water uit elkaar te houden",
            "ze toont zeeën en rivieren en ook de kusten van de continenten",
        ],
        antwoord=0,
        uitleg="Zo'n kaart ordent de wereld naar geloof, niet naar afstand. Ze meet niet, ze vertelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloed hadden de Arabische wetenschappen op christelijk Europa?",
        opties=[
            "Griekse teksten kwamen via Arabische vertalingen terug in Europa",
            "de cijfers waarmee wij nog altijd rekenen, kwamen langs die weg",
            "geneeskunde, sterrenkunde en wiskunde gingen er sterk op vooruit",
            "de boekdrukkunst met losse letters werd er uitgevonden en verspreid",
        ],
        antwoord=[0, 1, 2],
        uitleg="De boekdrukkunst met losse letters komt van Gutenberg, in de 15de eeuw. De drie andere lopen wel via Córdoba, Toledo en Palermo.",
    ),
    dict(
        type="waarofniet",
        vraag="Er bestond in de middeleeuwen geen hoger onderwijs.",
        antwoord=False,
        uitleg="Vanaf de 12de eeuw ontstaan universiteiten, zoals Bologna, Parijs en later Leuven. Men studeerde er in het Latijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="De organisatie van de katholieke Kerk situeer je vooral in welk maatschappelijk domein?",
        opties=[
            "het culturele domein",
            "het economische domein",
            "het maritieme domein",
            "het militaire domein",
        ],
        antwoord=0,
        uitleg="Godsdienst hoort bij cultuur. Dat de Kerk ook grond bezat en macht uitoefende, maakt haar daarnaast ook economisch en politiek van belang.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe verliep de macht van de koning in Frankrijk in de late middeleeuwen?",
        opties=[
            "de koning breidde zijn gebied en zijn gezag stap voor stap uit",
            "de koning verloor bijna al zijn macht aan een parlement van adel en steden",
            "de koning werd voortaan door het volk van het hele land verkozen",
            "de koning verdween helemaal en Frankrijk werd een republiek met raden",
        ],
        antwoord=0,
        uitleg="Van een koning die alleen rond Parijs iets te zeggen had, groeit hij uit tot vorst van een groot en centraal bestuurd rijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakte de Engelse monarchie anders dan de Franse?",
        opties=[
            "de koning moest zijn macht delen met een parlement",
            "de koning beschikte over helemaal geen eigen leger",
            "de koning werd door de paus in Rome aangesteld en afgezet",
            "de koning regeerde zonder enige adel naast zich in het land",
        ],
        antwoord=0,
        uitleg="Met de Magna Carta van 1215 en het latere parlement wordt de Engelse koning aan regels gebonden. In Frankrijk gaat het net de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="De Magna Carta legde vast dat ook de koning zich aan afspraken moest houden.",
        antwoord=True,
        uitleg="De adel dwong het af in 1215. Het is geen democratie, maar wel het begin van een macht die niet meer onbeperkt is.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar vond de Guldensporenslag plaats?",
        antwoord="1302",
        uitleg="Op 11 juli 1302 bij Kortrijk. Die datum is vandaag de feestdag van de Vlaamse Gemeenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie stonden er in de Guldensporenslag tegenover elkaar?",
        opties=[
            "een Vlaams leger met veel stedelingen tegen het ridderleger van de Franse koning",
            "het leger van de koning van Engeland tegen het leger van de koning van Frankrijk",
            "de troepen van de paus in Rome tegen die van de keizer van het Duitse Rijk",
            "twee Vlaamse steden die onderling om de macht in het graafschap streden",
        ],
        antwoord=0,
        uitleg="De graaf van Vlaanderen was leenman van de Franse koning. De steden, met de ambachten voorop, kwamen tegen diens greep in opstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen had de Guldensporenslag voor het graafschap Vlaanderen?",
        opties=[
            "de Franse inlijving werd voorlopig afgewend",
            "de ambachten kregen meer invloed in de steden",
            "Vlaanderen moest later toch zware betalingen aan Frankrijk doen",
            "Vlaanderen werd onmiddellijk een onafhankelijk koninkrijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een koninkrijk werd het niet; de graaf bleef leenman van de Franse koning. De drie andere gevolgen zijn er wel gekomen.",
    ),
    dict(
        type="waarofniet",
        vraag="De Guldensporenslag was in de eerste plaats een taalstrijd tussen Nederlands en Frans.",
        antwoord=False,
        uitleg="Het ging over macht, geld en zeggenschap in de steden. De taalkant is er pas in de 19de eeuw bij gekomen, toen men het verleden voor het heden gebruikte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer ontstaat de islam en begint de groei van het Arabische Rijk?",
        opties=[
            "vanaf ongeveer 600",
            "vanaf ongeveer 300",
            "vanaf ongeveer 1000",
            "vanaf ongeveer 1300",
        ],
        antwoord=0,
        uitleg="Mohammed leeft rond 570 tot 632. Daarna gaat de uitbreiding bijzonder snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gebied hoorde op het hoogtepunt van het Arabische Rijk er níét bij?",
        opties=[
            "Scandinavië",
            "het Arabische schiereiland",
            "Noord-Afrika",
            "het grootste deel van Spanje",
        ],
        antwoord=0,
        uitleg="Het rijk strekte zich uit van Spanje tot voorbij Perzië, maar reikte nooit tot het hoge noorden. Dat lees je af op een historische kaart.",
    ),
    dict(
        type="waarofniet",
        vraag="De islam verspreidde zich in één enkele golf, binnen de tien jaar, over heel zijn latere gebied.",
        antwoord=False,
        uitleg="Het ging in fasen: eerst het Arabische schiereiland, daarna Perzië en Noord-Afrika, en pas later Spanje. Op een historische kaart zie je die fasen naast elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin blonk de Arabische cultuur juist níét uit?",
        opties=[
            "in het bouwen van stoommachines",
            "in wiskunde en sterrenkunde",
            "in sierschrift en bouwkunst",
            "in het bewaren van Griekse teksten",
        ],
        antwoord=0,
        uitleg="Stoommachines komen pas veel later, in Engeland. In de drie andere zaken liep de Arabische wereld eeuwenlang op Europa voor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de handelswegen die het Westen met China verbonden?",
        antwoord="de zijderoutes",
        uitleg="Niet één weg maar een net van routes, over land en over zee. Er ging veel meer over dan zijde alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de motieven voor de kruistochten?",
        opties=[
            "godsdienstige: de heilige plaatsen in bezit krijgen",
            "economische: handel en buit",
            "sociale: jongere adellijke zonen zochten een eigen gebied",
            "wetenschappelijke: de sterrenkunde bestuderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wetenschap was geen motief, al kwam er wel kennis mee terug. De drie andere lopen door elkaar bij bijna elke deelnemer.",
    ),
    dict(
        type="waarofniet",
        vraag="De kruistochten leverden op lange termijn een blijvend christelijk rijk in het Midden-Oosten op.",
        antwoord=False,
        uitleg="De veroverde staten hielden het nog geen twee eeuwen vol. In 1291 viel Akko, het laatste steunpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen hadden de kruistochten voor West-Europa?",
        opties=[
            "meer handel met het oosten, via Italiaanse steden",
            "nieuwe producten en kennis kwamen mee terug",
            "de verhouding met moslims en joden verhardde",
            "de standensamenleving verdween en iedereen werd vrij",
        ],
        antwoord=[0, 1, 2],
        uitleg="De standen bleven gewoon bestaan. De drie andere gevolgen zijn er wel gekomen, en ze spreken elkaar niet tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het contact tussen de islamitische wereld en het Westen bestond zowel uit oorlog als uit handel en kennisoverdracht.",
        antwoord=True,
        uitleg="In Toledo en Palermo werd samen vertaald terwijl er elders gevochten werd. Een contact is zelden alleen maar het ene of het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je de kruistochten niet enkel vanuit de westerse bronnen bekijken?",
        opties=[
            "wie schrijft, kiest wat hij vertelt; de Arabische kronieken geven een ander beeld",
            "de westerse bronnen zijn zonder uitzondering achteraf vervalst door kopiisten",
            "er zijn uit het Westen zelf helemaal geen bronnen over die tochten bewaard",
            "de Arabische bronnen zijn allemaal vertaald en dus onbetrouwbaar geworden",
        ],
        antwoord=0,
        uitleg="Twee bronnen over dezelfde veldslag kunnen allebei eerlijk zijn en toch iets anders belangrijk vinden. Dat is standplaatsgebondenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de macht van de Franse en de Engelse koning aan het einde van de middeleeuwen?",
        opties=[
            "de Franse koning regeert steeds meer alleen, de Engelse steeds meer met een parlement",
            "de Franse koning heeft een parlement naast zich, de Engelse regeert helemaal alleen",
            "ze worden allebei door de adel van hun land verkozen bij elke troonopvolging",
            "geen van beiden heeft aan het einde van de middeleeuwen nog enige echte macht",
        ],
        antwoord=0,
        uitleg="Die twee wegen lopen eeuwen later nog door: Frankrijk eindigt bij een absolute vorst, Engeland bij een koning die met het parlement moet rekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="De feestdag van 11 juli laat zien hoe een middeleeuwse gebeurtenis vandaag nog betekenis krijgt.",
        antwoord=True,
        uitleg="Wat men op 11 juli viert, is in de loop van de tijd veranderd. Dat een herdenking meegroeit met haar eigen tijd, hoort bij beeldvorming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Onder welk maatschappelijk domein breng je de Guldensporenslag vooral onder?",
        opties=[
            "het politieke domein",
            "het culturele domein",
            "het economische domein",
            "het sociale domein",
        ],
        antwoord=0,
        uitleg="Het gaat over wie het gezag heeft over Vlaanderen. De sociale kant, de opstand van de ambachten, loopt er wel doorheen.",
    ),
]

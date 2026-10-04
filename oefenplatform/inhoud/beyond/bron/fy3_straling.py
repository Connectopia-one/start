# -*- coding: utf-8 -*-
"""Kernenergie, straling en haar effecten — 🌍 Beyond, fysica.

Deel 1 gaat over de energie van de kern: de rustenergie met de formule van
Einstein, het massadefect, de bindingsenergie en de specifieke
bindingsenergie, de energievallei, het verschil tussen kernsplijting en
kernfusie, de bouw en de beveiliging van een kerncentrale, en de drie
categorieën radioactief afval met hun berging in België. Deel 2 gaat over de
straling zelf: het ioniserend en het doordringend vermogen van alfa-, bèta-
en gammastraling, de stoffen die ze tegenhouden, het verschil tussen
bestraling en besmetting, de geabsorbeerde, de equivalente en de effectieve
dosis met hun weegfactoren, de beschermingsmaatregelen, en de toepassingen van
de PET-scan tot het doorstralen van voedsel.

De rode draad is dat een kleine massa een enorme energie is, en dat dezelfde
straling geneest of schaadt naargelang de dosis en de plaats waar ze
terechtkomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de formule van Einstein over een massa?",
        opties=[
            "elke massa is een hoeveelheid energie, namelijk m maal c kwadraat",
            "elke massa wordt zwaarder naarmate ze sneller beweegt dan c",
            "elke massa heeft een energie gelijk aan m maal c",
            "elke massa valt met een versnelling gelijk aan c kwadraat",
        ],
        antwoord=0,
        uitleg="Omdat c kwadraat enorm groot is, zit er in een kleine massa veel energie. In "
        "de kernfysica rekent men ook met 931,49 MeV per atomaire massa-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het massadefect van een kern?",
        opties=[
            "het verschil tussen de massa van de losse nucleonen en de kern",
            "het verschil tussen het massagetal en het atoomnummer",
            "het verschil tussen de massa van twee isotopen",
            "het deel van de massa dat bij verval overblijft",
        ],
        antwoord=0,
        uitleg="De kern weegt minder dan zijn delen apart. Die ontbrekende massa zit als "
        "bindingsenergie in de kern.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de energie die nodig is om een kern in losse nucleonen te splitsen?",
        antwoord=["de bindingsenergie", "bindingsenergie", "kernbindingsenergie"],
        uitleg="Ze is het massadefect maal c kwadraat. Per nucleon heet ze de specifieke "
        "bindingsenergie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de specifieke bindingsenergie van een kern?",
        opties=[
            "de bindingsenergie gedeeld door het aantal nucleonen",
            "de bindingsenergie maal het aantal nucleonen",
            "de bindingsenergie gedeeld door het atoomnummer",
            "de bindingsenergie van het hele atoom samen",
        ],
        antwoord=0,
        uitleg="Zo kan je kernen van verschillende grootte vergelijken. Hoe groter ze is, "
        "hoe stabieler de kern.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kern met een grotere specifieke bindingsenergie is stabieler.",
        antwoord=True,
        uitleg="Elk nucleon zit er dan steviger in. IJzer ligt daarin het laagst in de "
        "energievallei, en dus het stabielst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kernsplijting?",
        opties=[
            "een zware kern valt in twee lichtere kernen uiteen",
            "twee lichte kernen smelten tot één zwaardere samen",
            "een kern zendt een foton met veel energie uit",
            "een kern vangt een elektron uit zijn eigen schil op",
        ],
        antwoord=0,
        uitleg="Dat is wat er in een kerncentrale met uranium gebeurt. Smelten van lichte "
        "kernen heet kernfusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom komt er bij fusie van lichte kernen energie vrij?",
        opties=[
            "de nieuwe kern heeft een grotere specifieke bindingsenergie",
            "de nieuwe kern heeft een kleinere specifieke bindingsenergie",
            "de nieuwe kern heeft meer nucleonen dan de twee samen",
            "de nieuwe kern zendt daarbij al zijn neutronen uit",
        ],
        antwoord=0,
        uitleg="De kern zakt dus dieper in de energievallei, en dat verschil komt vrij. Bij "
        "zware kernen gebeurt datzelfde door te splijten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke processen leveren energie? Kruis alles aan wat juist is.",
        opties=[
            "fusie van twee lichte kernen",
            "splijting van een zware kern",
            "fusie van twee zware kernen",
            "splijting van een heel lichte kern",
        ],
        antwoord=[0, 1],
        uitleg="Beide bewegen naar ijzer toe, het diepste punt van de energievallei. De "
        "andere twee zouden er net energie voor nodig hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk proces levert de energie van de zon?",
        opties=[
            "kernfusie van waterstof tot helium",
            "kernsplijting van uranium tot lichtere kernen",
            "de verbranding van waterstof met zuurstof",
            "het radioactief verval van zware kernen",
        ],
        antwoord=0,
        uitleg="Dat gebeurt in de proton-protoncyclus. Daar is een enorme druk en "
        "temperatuur voor nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Welke splijtstof gebruikt een gewone kerncentrale?",
        antwoord=["uranium", "uraan", "uranium-235"],
        uitleg="Het gaat om de isotoop met massagetal 235, verrijkt in splijtstaven. Een "
        "neutron splijt die kern en er komen nieuwe neutronen vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dienen de regelstaven in een kernreactor?",
        opties=[
            "ze vangen neutronen weg en houden de kettingreactie in de hand",
            "ze leveren extra neutronen om de reactie te versnellen",
            "ze koelen het water in het reactorvat af",
            "ze houden de straling binnen de betonnen koepel",
        ],
        antwoord=0,
        uitleg="Schuif je ze diep in de kern, dan vertraagt de reactie. Zo blijft de "
        "kettingreactie gecontroleerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen horen bij een kerncentrale op kernsplijting? Kruis alles aan wat juist is.",
        opties=[
            "een reactorvat met splijtstaven en regelstaven",
            "een stoomgenerator en een turbine",
            "een betonnen koepel rond de reactor",
            "een schoorsteen die de rook van de brandstof afvoert",
        ],
        antwoord=[0, 1, 2],
        uitleg="Er wordt niets verbrand, dus is er geen rook en geen schoorsteen. De "
        "koeltoren laat enkel waterdamp ontsnappen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kerncentrale op kernsplijting stoot bij het opwekken van stroom geen CO₂ uit.",
        antwoord=True,
        uitleg="Er wordt niets verbrand, dus komt er geen koolstofdioxide vrij. Het nadeel "
        "zit in het radioactief afval en in het risico van een ongeval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voordelen heeft een centrale op kernfusie boven een op kernsplijting?",
        opties=[
            "veel minder langlevend afval en geen kettingreactie die ontspoort",
            "veel minder brandstof nodig maar wel meer langlevend afval",
            "een veel eenvoudigere bouw en een veel lagere temperatuur",
            "een veel hogere opbrengst maar meer CO₂-uitstoot",
        ],
        antwoord=0,
        uitleg="Het nadeel is dat de nodige temperatuur en druk enorm hoog zijn. Daarom "
        "bestaat er nog geen fusiecentrale die stroom levert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Volgens welke twee kenmerken wordt radioactief afval ingedeeld?",
        opties=[
            "de intensiteit van de straling en hoe lang ze duurt",
            "het gewicht van het afval en waar het van komt",
            "de kleur van het afval en de plaats van berging",
            "het aantal vaten en het land van herkomst",
        ],
        antwoord=0,
        uitleg="Zo krijg je laag-, middel- en hoogactief afval, elk kortlevend of "
        "langlevend. Daaruit volgen de drie categorieën A, B en C.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk afval zit in categorie A?",
        opties=[
            "kortlevend laagactief en middelactief afval",
            "langlevend laagactief en middelactief afval",
            "kort- en langlevend hoogactief afval",
            "alle afval van een ziekenhuis",
        ],
        antwoord=0,
        uitleg="Categorie B is het langlevende laag- en middelactieve afval, categorie C het "
        "hoogactieve. In België gaat categorie A naar een berging aan de oppervlakte in Dessel.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor hoogactief afval van categorie C ligt in België al een definitieve bergingsplaats vast.",
        antwoord=False,
        uitleg="Voor dat afval wordt een berging diep in de grond onderzocht, maar er is nog "
        "geen plaats vastgelegd. Enkel voor categorie A is de keuze gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar komt laagactief afval onder meer van?",
        opties=[
            "van beschermkledij en gereedschap uit een ziekenhuis of labo",
            "van de gebruikte splijtstaven van een kernreactor",
            "van de betonnen koepel rond een reactorvat",
            "van het koelwater uit de koeltoren",
        ],
        antwoord=0,
        uitleg="Hoogactief afval komt wel van de gebruikte splijtstaven zelf. Hoe actiever "
        "het afval, hoe zwaarder de bescherming bij het verwerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel energie zit er volgens Einstein in 1 g massa? Neem c gelijk aan 3 · 10⁸ m/s.",
        opties=[
            "ongeveer 9 · 10¹³ J",
            "ongeveer 9 · 10¹⁶ J",
            "ongeveer 3 · 10⁵ J",
            "ongeveer 9 · 10⁶ J",
        ],
        antwoord=0,
        uitleg="E is m maal c kwadraat, met m gelijk aan 0,001 kilogram. Dat is 0,001 maal 9 "
        "maal tien tot de macht 16.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een kernproces blijft de totale massa van de deeltjes precies gelijk.",
        antwoord=False,
        uitleg="Een klein stuk massa wordt energie, en dat is net waar de opbrengst van komt. "
        "Massa en energie samen blijven wel bewaard.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke straling heeft het grootste ioniserend vermogen?",
        opties=[
            "alfastraling",
            "bètastraling",
            "gammastraling",
            "ze zijn alle drie gelijk",
        ],
        antwoord=0,
        uitleg="Een alfadeeltje is zwaar en dubbel geladen, dus slaat het veel elektronen "
        "los. Juist daarom komt het niet ver.",
    ),
    dict(
        type="waarofniet",
        vraag="Alfastraling heeft van de drie soorten het grootste doordringend vermogen.",
        antwoord=False,
        uitleg="Ze komt niet eens door een blad papier. Gammastraling is een foton zonder "
        "lading en gaat wel door beton heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen houden welke straling tegen? Kruis alles aan wat juist is.",
        opties=[
            "een blad papier houdt alfastraling tegen",
            "een plaatje aluminium houdt bètastraling tegen",
            "een dikke laag lood of beton zwakt gammastraling af",
            "een laag water houdt gammastraling volledig tegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gammastraling kan je afzwakken maar niet helemaal stoppen. Daarom werkt men "
        "met dikte, afstand en tijd samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Alfastraling buigt af in een elektrisch veld.",
        antwoord=True,
        uitleg="Ze is positief geladen, dus voelt ze de kracht van het veld. Gammastraling "
        "heeft geen lading en gaat recht door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe gedragen de drie soorten straling zich in een magnetisch veld?",
        opties=[
            "alfa en bèta buigen naar tegengestelde kanten, gamma gaat recht",
            "alle drie buigen naar dezelfde kant af",
            "gamma buigt het sterkst af en alfa het minst",
            "geen van de drie buigt in een magnetisch veld af",
        ],
        antwoord=0,
        uitleg="Alfa is positief en bèta-min negatief, dus krijgen ze een kracht in "
        "tegengestelde zin. Een foton voelt het veld niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen bestraling en besmetting?",
        opties=[
            "bij besmetting zit de radioactieve stof op of in je lichaam",
            "bij bestraling zit de radioactieve stof op of in je lichaam",
            "bij besmetting is de dosis altijd veel kleiner",
            "bij bestraling gaat het altijd om alfastraling",
        ],
        antwoord=0,
        uitleg="Bij bestraling sta je in de straling van een bron buiten je. Ga je weg, dan "
        "stopt de bestraling, maar een besmetting neem je mee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een besmetting waarbij de radioactieve stof in het lichaam zit?",
        antwoord=["inwendige besmetting", "inwendig", "een inwendige besmetting"],
        uitleg="Dat gebeurt door inademen of inslikken. Zit de stof op de huid, dan heet het "
        "een uitwendige besmetting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de geabsorbeerde dosis?",
        opties=[
            "de energie van de straling per kilogram weefsel",
            "de energie van de straling per seconde",
            "het aantal vervallen per seconde in de bron",
            "de energie van één foton van de straling",
        ],
        antwoord=0,
        uitleg="Ze krijgt het symbool D en staat in gray. De activiteit van de bron staat "
        "wel in becquerel.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de geabsorbeerde dosis uit?",
        antwoord=["gray", "Gy", "de gray"],
        uitleg="Eén gray is één joule per kilogram. De equivalente en de effectieve dosis "
        "staan wel in sievert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de equivalente dosis?",
        opties=[
            "de geabsorbeerde dosis maal de stralingsweegfactor",
            "de geabsorbeerde dosis maal de weefselweegfactor",
            "de geabsorbeerde dosis gedeeld door de tijd",
            "de geabsorbeerde dosis van het hele lichaam samen",
        ],
        antwoord=0,
        uitleg="Zo houd je er rekening mee dat alfastraling meer schade doet. Ze staat in "
        "sievert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft alfastraling een veel hogere stralingsweegfactor dan gammastraling?",
        opties=[
            "ze geeft haar energie in een heel klein gebied af",
            "ze dringt veel dieper in het lichaam door",
            "ze heeft een veel hogere frequentie",
            "ze blijft veel langer in het weefsel aanwezig",
        ],
        antwoord=0,
        uitleg="Alle ionisaties komen dan op dezelfde paar cellen terecht. Van buiten is ze "
        "ongevaarlijk, maar ingeslikt of ingeademd juist niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de weefselweegfactor?",
        opties=[
            "om te verrekenen dat sommige organen gevoeliger zijn",
            "om te verrekenen dat sommige stralingen gevaarlijker zijn",
            "om de dosis per kilogram weefsel te berekenen",
            "om de activiteit van de bron te berekenen",
        ],
        antwoord=0,
        uitleg="Met die factor kom je van de equivalente naar de effectieve dosis. Het "
        "beenmerg weegt bijvoorbeeld zwaarder dan de huid.",
    ),
    dict(
        type="waarofniet",
        vraag="De effectieve dosis houdt rekening met de soort straling en met het bestraalde weefsel.",
        antwoord=True,
        uitleg="Ze is de geabsorbeerde dosis met beide weegfactoren erbij. Daarom is net zij "
        "de maat voor het risico voor de mens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen beschermen tegen ioniserende straling? Kruis alles aan wat juist is.",
        opties=[
            "verder van de bron gaan staan",
            "zo kort mogelijk in de buurt van de bron blijven",
            "een afscherming van lood of beton tussen jou en de bron",
            "de bron verwarmen zodat ze sneller uitgewerkt is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verwarmen doet niets, want verval trekt zich daar niets van aan. Afstand, "
        "tijd en afscherming zijn de drie die werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom deelt men bij een kernongeval jodiumpillen uit?",
        opties=[
            "de schildklier zit dan vol en neemt geen radioactief jodium meer op",
            "het jodium in de pil breekt de radioactieve stoffen af",
            "het jodium houdt de gammastraling van buiten tegen",
            "het jodium versnelt het verval van de radioactieve stoffen",
        ],
        antwoord=0,
        uitleg="Het gaat dus om een inwendige besmetting voorkomen. Tegen de straling van "
        "buiten helpt de pil niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk effect heeft ioniserende straling op een cel?",
        opties=[
            "ze kan het DNA beschadigen en de cel doen afsterven of muteren",
            "ze maakt de cel alleen maar warmer dan normaal",
            "ze maakt de celwand elektrisch geladen zonder meer",
            "ze heeft op een levende cel geen enkel effect",
        ],
        antwoord=0,
        uitleg="Daarom kan een hoge dosis stralingsziekte geven en een lage het risico op "
        "kanker verhogen. In de radiotherapie gebruikt men dat net om tumorcellen te doden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen gebruiken ioniserende straling? Kruis alles aan wat juist is.",
        opties=[
            "het doorstralen van voedsel om het langer te bewaren",
            "radiotherapie tegen een tumor",
            "een PET-scan met een radioactieve tracer",
            "een echografie van een baby",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een echografie werkt met ultrasoon geluid en dus niet met straling. De "
        "eerste drie werken wel met ioniserende straling.",
    ),
    dict(
        type="waarofniet",
        vraag="Doorstraald voedsel wordt zelf radioactief.",
        antwoord=False,
        uitleg="De straling doodt de bacteriën en gaat er daarna uit; er blijft geen bron in "
        "het voedsel achter. Daarom mag het ook gewoon verkocht worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is natuurlijke straling?",
        opties=[
            "straling van radon uit de bodem en van de kosmos",
            "straling van een röntgentoestel in het ziekenhuis",
            "straling van het afval van een kerncentrale",
            "straling van een zonnebank of een blacklight",
        ],
        antwoord=0,
        uitleg="Iedereen krijgt daar elk jaar een dosis van. De andere drie zijn kunstmatige "
        "bronnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men in een PET-scan een stof met een korte halveringstijd?",
        opties=[
            "zo is de straling in het lichaam snel weer weg",
            "zo geeft de stof van het begin veel meer straling",
            "zo blijft de stof langer in het orgaan zitten",
            "zo kan men de scan jaren later herhalen",
        ],
        antwoord=0,
        uitleg="De dosis voor de patiënt blijft daardoor beperkt. Er moet wel genoeg "
        "activiteit zijn om een beeld te maken.",
    ),
]

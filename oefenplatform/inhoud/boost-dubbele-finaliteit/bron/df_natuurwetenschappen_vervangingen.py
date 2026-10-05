# -*- coding: utf-8 -*-
"""De vragen die voor 🚀 Boost dubbele finaliteit anders moeten dan bij
doorstroom, voor natuurwetenschappen.

De sleutel is de vraagtekst van de doorstroomvraag, de waarde is de vraag die
in de plaats komt. `bouw_natuurwetenschappen.py` hiernaast wisselt ze om en
stopt als een sleutel niet meer bestaat.

Wat de fiche van de dubbele finaliteit **niet** vraagt en wat hier dus
verdwijnt:

  * **Biologie.** De indeling van het leven (driedomeinensysteem,
    vijfrijkensysteem, prokaryoot en eukaryoot) staat er niet in. Wat er wel
    in staat, is de bouw van een bacterie, een virus, een gist en een
    schimmel, en de weg waarlangs ze binnendringen.
  * **Chemie.** De relatieve atoommassa en de absolute massa van een atoom
    staan er niet in. De elektronenconfiguratie volgens Bohr en het
    elektron-stipmodel wel.
  * **Fysica.** Hier is het verschil het grootst. Arbeid, de formules van de
    kinetische, de gravitationele en de elastische energie, de specifieke
    warmtecapaciteit, de latente warmte, het warmtetransport, de vrije val,
    de verticale worp, de veerconstante, de zwaarteveldsterkte, de
    hydrostatische druk, het beginsel van Pascal en de gaswetten met de
    kelvinschaal: niets daarvan staat in de fiche. Achteraan zegt ze
    uitdrukkelijk welke vier formules je moet kennen, en dat zijn
    P = |ΔE| / Δt, het rendement, p = F / A en R = U / I.

In de plaats komen de dingen die de fiche wél zet: de open, gesloten en
geïsoleerde systemen, de energiebalans met haar nuttige en ongewenste energie,
koeling en isolatie, warmte tegenover temperatuur, de inwendige energie en de
cohesiekrachten, de vier kenmerken van een kracht en het samenstellen van
krachtvectoren, het traagheidsbeginsel met zijn voorbeelden uit het verkeer,
en bij druk de manometer, de barometer, de overdruk en de onderdruk met hun
toepassingen.

Elke vervanging houdt hetzelfde type: een waar-of-niet-waar-vraag blijft waar
of blijft niet waar, en een meerkeuzevraag met meerdere juiste antwoorden
houdt er meerdere. Zo blijft het evenwicht per hoofdstuk kloppen.
"""

VERVANGINGEN = {}

# ───────────────────────────── Micro-organismen: geen indeling van het leven,
# wel de bouw en de weg waarlangs ze binnenkomen.
VERVANGINGEN.update(
    {
        "Uit welke drie domeinen bestaat het driedomeinensysteem?": dict(
            type="meerkeuze",
            vraag="Welke vormen kan je bij bacteriën onder de microscoop zien?",
            opties=[
                "bolvormig, staafvormig, kommavormig of spiraalvormig",
                "alleen bolvormig of staafvormig, nooit een andere vorm",
                "altijd spiraalvormig, met voor elke soort een vaste lengte",
                "altijd bolvormig, met een draadje eraan om zich te bewegen",
            ],
            antwoord=0,
            uitleg="De bolvormige noemen we kokken, de staafvormige bacillen, de kommavormige vibrionen en de spiraalvormige spirillen. De vorm helpt om een bacterie te herkennen.",
        ),
        "Welke rijken horen bij het vijfrijkensysteem? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke onderdelen kan je bij een bacterie terugvinden? Kruis alles aan wat juist is.",
            opties=[
                "een celwand rond het celmembraan",
                "een slijmlaag aan de buitenkant",
                "een plasmide naast het grote DNA",
                "een echte kern met een kernmembraan",
            ],
            antwoord=[0, 1, 2],
            uitleg="Een bacterie heeft DNA, een celmembraan en een celwand, en daarbij vaak een slijmlaag, een plasmide, pili of een zweephaar. Een echte kern met kernmembraan heeft ze niet.",
        ),
        "Een prokaryote cel heeft geen kernmembraan.": dict(
            type="waarofniet",
            vraag="Een gistcel heeft een kern, een bacteriecel niet.",
            antwoord=True,
            uitleg="Gisten zijn eencellig, maar hun erfelijk materiaal zit in een kern. Bij een bacterie ligt het DNA vrij in de cel.",
        ),
        "Waarom staan virussen niet in de tree of life?": dict(
            type="meerkeuze",
            vraag="Hoe deelt men virussen in naar hun gastheer?",
            opties=[
                "in dierlijke virussen, plantaardige virussen en bacteriofagen",
                "in virussen van het water, van de lucht en van de bodem",
                "in virussen met een enveloppe en virussen met alleen spikes",
                "in eencellige virussen en meercellige virussen",
            ],
            antwoord=0,
            uitleg="Een virus kan alleen binnen in een levende cel van zijn eigen soort gastheer. Een bacteriofaag valt bacteriën aan, een plantaardig virus plantencellen.",
        ),
        "Hoe noem je een organisme waarvan de cel wél een echte kern met kernmembraan heeft?": dict(
            type="invultekst",
            vraag="Hoe noem je een virus dat bacteriën als gastheer gebruikt?",
            antwoord=["bacteriofaag", "faag"],
            uitleg="Een bacteriofaag spuit zijn erfelijk materiaal in een bacterie. Men onderzoekt ze als mogelijk middel tegen bacteriën die niet meer op antibiotica reageren.",
        ),
        "Een bacteriekweek groeit vanaf het begin even snel en blijft dat doen zolang er voedsel is.": dict(
            type="waarofniet",
            vraag="Gisten en schimmels zijn allebei eencellig.",
            antwoord=False,
            uitleg="Een gist is eencellig, een schimmel is opgebouwd uit lange schimmeldraden en dus meercellig. Dat is een van de verschillen in bouw tussen de twee.",
        ),
        "Schimmels zijn eukaryoot.": dict(
            type="waarofniet",
            vraag="Een schimmel is opgebouwd uit schimmeldraden.",
            antwoord=True,
            uitleg="Die draden samen vormen het schimmelweefsel dat je als pluis op oud brood ziet. Aan de uiteinden maakt de schimmel sporen om zich te verspreiden.",
        ),
        "Waarom is een indeling als het driedomeinensysteem nuttig?": dict(
            type="meerkeuze",
            vraag="Langs welke wegen dringen micro-organismen het lichaam binnen?",
            opties=[
                "langs de mond, de luchtwegen, de ogen en wondjes in de huid",
                "alleen langs de mond, want alles moet mee met de voeding",
                "alleen langs wondjes, want de huid laat anders niets door",
                "langs de huid, maar nooit langs de ogen of de luchtwegen",
            ],
            antwoord=0,
            uitleg="De gave huid is een goede barrière, de openingen van het lichaam niet. Handen wassen, hoesten in je elleboog en een wondje afdekken sluiten juist die wegen af.",
        ),
    }
)

# ───────────────────────────── Het atoom: geen atoommassa's, wel de
# elektronenconfiguratie en het stipmodel.
VERVANGINGEN.update(
    {
        "Wat is de relatieve atoommassa?": dict(
            type="meerkeuze",
            vraag="Wat lees je af uit de symbolische voorstelling van een atoom met zijn massagetal en zijn atoomnummer?",
            opties=[
                "hoeveel protonen, neutronen en elektronen het atoom heeft",
                "hoeveel moleculen van die stof er in een druppel passen",
                "welke plaats het atoom in een chemische reactie inneemt",
                "hoeveel energie er in de kern van het atoom opgeslagen zit",
            ],
            antwoord=0,
            uitleg="Het atoomnummer Z is het aantal protonen, en in een neutraal atoom ook het aantal elektronen. Het massagetal A min het atoomnummer geeft het aantal neutronen.",
        ),
        "Welk symbool gebruiken we voor de atoommassa-eenheid?": dict(
            type="invultekst",
            vraag="Hoe noem je het model waarin je de elektronen van de buitenste schil als stipjes rond het symbool van het element zet?",
            antwoord=["elektron-stipmodel", "stipmodel", "elektronstipmodel"],
            uitleg="In het elektron-stipmodel staat alleen de buitenste schil. Voor zuurstof zet je dus zes stipjes rond de O, want zuurstof heeft zes elektronen in zijn buitenste schil.",
        ),
        "Hoe reken je de absolute massa van een atoom uit?": dict(
            type="meerkeuze",
            vraag="Hoe noteer je de elektronenconfiguratie van een zwavelatoom met atoomnummer 16?",
            opties=[
                "2, 8, 6",
                "2, 8, 8",
                "8, 6, 2",
                "2, 6, 8",
            ],
            antwoord=0,
            uitleg="Je vult de schillen van binnen naar buiten: eerst twee elektronen, dan acht, en de zes die overblijven komen in de derde schil. Samen zijn dat de zestien elektronen.",
        ),
        "De relatieve atoommassa van een atoom druk je uit in kilogram.": dict(
            type="waarofniet",
            vraag="In het elektron-stipmodel zet je alle elektronen van het atoom rond het symbool.",
            antwoord=False,
            uitleg="Alleen de elektronen van de buitenste schil komen erin. Die bepalen hoe het atoom reageert; de binnenste schillen laat je weg.",
        ),
    }
)

# ───────────────────────────── Energie: geen arbeid en geen formules voor de
# kinetische, gravitationele of elastische energie. Wel de systemen, de
# energiebalans, het vermogen en het rendement.
VERVANGINGEN.update(
    {
        "Wanneer verricht een kracht arbeid op een voorwerp?": dict(
            type="meerkeuze",
            vraag="Welk systeem wisselt met zijn omgeving zowel energie als materie uit?",
            opties=[
                "een open systeem",
                "een gesloten systeem",
                "een geïsoleerd systeem",
                "een systeem in evenwicht",
            ],
            antwoord=0,
            uitleg="Een open kookpot is een open systeem: er gaat warmte weg en er verdwijnt ook waterdamp. Een gesloten systeem laat alleen energie door, een geïsoleerd systeem niets.",
        ),
        "Wat is de eenheid van arbeid en van energie?": dict(
            type="meerkeuze",
            vraag="Hoeveel joule is één kilowattuur?",
            opties=[
                "3 600 000 joule",
                "1000 joule",
                "3600 joule",
                "60 000 joule",
            ],
            antwoord=0,
            uitleg="Een kilowattuur is duizend watt gedurende één uur, dus 1000 joule per seconde maal 3600 seconden. Daarom reken je op je elektriciteitsfactuur in kilowattuur en niet in joule.",
        ),
        "Een kracht die loodrecht op de verplaatsing staat, verricht geen arbeid.": dict(
            type="waarofniet",
            vraag="Bij een energieomzetting gaat er altijd een deel van de energie naar een vorm die je niet wou, meestal warmte.",
            antwoord=True,
            uitleg="Dat verlies noemen we energiedissipatie. Daarom is het rendement van een omzetting nooit honderd procent.",
        ),
        "Wanneer is de arbeid van een kracht negatief?": dict(
            type="meerkeuze",
            vraag="Waarom moet een computer gekoeld worden?",
            opties=[
                "omdat een deel van de elektrische energie in warmte omgezet wordt",
                "omdat de stroom anders in de verkeerde richting gaat lopen",
                "omdat de koeling de elektrische energie in het toestel opslaat",
                "omdat een warm toestel meer energie uit het net kan trekken",
            ],
            antwoord=0,
            uitleg="De warmte is hier de ongewenste energie. Zonder ventilator of koelplaat blijft die warmte in het toestel zitten en loopt de temperatuur te hoog op.",
        ),
        "Een gewicht hangt stil aan een koord. Welke arbeid verricht de spankracht?": dict(
            type="meerkeuze",
            vraag="Welke energieomzetting gebeurt er in een gasfornuis?",
            opties=[
                "chemische energie in thermische energie",
                "elektrische energie in chemische energie",
                "thermische energie in chemische energie",
                "stralingsenergie in elektrische energie",
            ],
            antwoord=0,
            uitleg="Het aardgas bevat chemische energie. Bij de verbranding komt die vrij als warmte, en een deel ervan gaat als licht en als warme lucht naast de pot verloren.",
        ),
        "Je duwt een doos van 3 meter ver met een kracht van 40 newton in de zin van de beweging. Hoeveel arbeid verricht je?": dict(
            type="meerkeuze",
            vraag="Je zet de deur van de koelkast open in een afgesloten keuken en laat ze zo staan. Wat gebeurt er met de temperatuur in de keuken?",
            opties=[
                "ze stijgt, want de motor zet elektrische energie in warmte om",
                "ze daalt, want de koelkast haalt warmte uit de keuken weg",
                "ze blijft gelijk, want de warmte gaat rond in dezelfde ruimte",
                "ze daalt eerst en stijgt daarna tot precies dezelfde waarde",
            ],
            antwoord=0,
            uitleg="Een koelkast verplaatst warmte van binnen naar buiten en zet daarbij zelf elektrische energie om. In een gesloten keuken komt die energie er bovenop, dus wordt het warmer.",
        ),
        "Hoe bereken je de kinetische energie van een voorwerp?": dict(
            type="meerkeuze",
            vraag="Welke energieomzetting gebeurt er in een zonnepaneel?",
            opties=[
                "stralingsenergie in elektrische energie",
                "elektrische energie in stralingsenergie",
                "chemische energie in elektrische energie",
                "thermische energie in stralingsenergie",
            ],
            antwoord=0,
            uitleg="Het licht van de zon is stralingsenergie. Een deel ervan wordt elektrische energie, de rest warmt het paneel op en is dus niet nuttig.",
        ),
        "Een voorwerp van 2 kilogram beweegt met 3 meter per seconde. Hoeveel kinetische energie heeft het?": dict(
            type="meerkeuze",
            vraag="Een lamp van 10 watt brandt een half uur. Hoeveel energie zet ze om?",
            opties=[
                "18 000 joule",
                "300 joule",
                "5 joule",
                "36 000 joule",
            ],
            antwoord=0,
            uitleg="Uit P = |ΔE| / Δt volgt ΔE = P · Δt. Een half uur is 1800 seconden, en 10 watt maal 1800 seconden is 18 000 joule.",
        ),
        "Wie twee keer zo snel rijdt, heeft vier keer zo veel kinetische energie.": dict(
            type="waarofniet",
            vraag="Een toestel met een rendement van honderd procent bestaat in de praktijk niet.",
            antwoord=True,
            uitleg="Er gaat altijd een deel van de energie naar warmte, geluid of wrijving. Hoe beter een toestel, hoe kleiner dat deel, maar nul wordt het nooit.",
        ),
        "Hoe bereken je de gravitationele potentiële energie van een voorwerp?": dict(
            type="meerkeuze",
            vraag="Hoe bereken je het rendement van een energieomzetting?",
            opties=[
                "de nuttige energie delen door de totale energie",
                "de totale energie delen door de nuttige energie",
                "de nuttige energie aftrekken van de totale energie",
                "de nuttige energie vermenigvuldigen met de tijdsduur",
            ],
            antwoord=0,
            uitleg="Dat is de formule η = Enuttig / Etotaal. Je krijgt een getal tussen 0 en 1, dat je met honderd vermenigvuldigt om het als een percentage te schrijven.",
        ),
        "Een bal van 1 kilogram valt van 5 meter hoog. Hoeveel kinetische energie heeft hij net voor de bodem, met 10 newton per kilogram?": dict(
            type="meerkeuze",
            vraag="Een waterkoker neemt 150 000 joule op en daarvan gaat 120 000 joule naar het water. Wat is het rendement?",
            opties=[
                "80 procent",
                "20 procent",
                "125 procent",
                "30 procent",
            ],
            antwoord=0,
            uitleg="120 000 gedeeld door 150 000 is 0,8, dus tachtig procent. De andere 30 000 joule warmt de kan, het water dat achterblijft en de lucht errond op.",
        ),
        "Welke uitspraken over de energiebalans van een slingerende schommel zijn juist? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke uitspraken over een gloeilamp van 60 watt zijn juist? Kruis alles aan wat juist is.",
            opties=[
                "ze zet elektrische energie om in licht en in warmte",
                "het grootste deel van de energie komt vrij als warmte",
                "haar rendement voor licht is laag",
                "ze zet alle energie die ze opneemt om in licht",
            ],
            antwoord=[0, 1, 2],
            uitleg="Bij een gloeilamp is het licht de nuttige energie en de warmte de ongewenste. Een ledlamp geeft bij hetzelfde licht veel minder warmte en heeft dus een beter rendement.",
        ),
        "Hoe bereken je de elastische potentiële energie van een uitgerekte veer?": dict(
            type="meerkeuze",
            vraag="Welke energieomzetting gebeurt er in een windmolen?",
            opties=[
                "kinetische energie van de wind in elektrische energie",
                "elektrische energie in kinetische energie van de wind",
                "stralingsenergie van de zon in kinetische energie",
                "chemische energie van de lucht in elektrische energie",
            ],
            antwoord=0,
            uitleg="De bewegende lucht duwt de wieken rond en de generator maakt daar elektrische energie van. Een deel gaat als geluid en warmte in de as verloren.",
        ),
    }
)

# ───────────────────────────── Warmte: geen warmtetransport, geen specifieke
# warmtecapaciteit en geen latente warmte. Wel warmte tegenover temperatuur,
# de warmtebalans, de inwendige energie en de voorbeelden van de fiche.
VERVANGINGEN.update(
    {
        "Welke vormen van warmtetransport zijn er? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke situaties zijn een voorbeeld van thermisch evenwicht? Kruis alles aan wat juist is.",
            opties=[
                "een glas water dat al een uur in de kamer staat",
                "een thermometer die in een bad niet meer verandert",
                "twee blokken metaal tegen elkaar met dezelfde temperatuur",
                "een ijsblokje dat je net in een glas water hebt gelegd",
            ],
            antwoord=[0, 1, 2],
            uitleg="In thermisch evenwicht hebben twee systemen dezelfde temperatuur en gaat er geen warmte meer van het ene naar het andere. Het ijsblokje is daar nog lang niet.",
        ),
        "Hoe noem je het warmtetransport dat ook door het luchtledige gaat?": dict(
            type="invultekst",
            vraag="Hoe noem je de energie die in de deeltjes van een stof zelf zit?",
            antwoord=["inwendige energie"],
            uitleg="De inwendige energie bestaat uit twee delen: de kinetische energie van de bewegende deeltjes en de potentiële energie die in de krachten tussen de deeltjes zit.",
        ),
        "Hoe gaat warmte door een metalen staaf?": dict(
            type="meerkeuze",
            vraag="Je legt een warm blok metaal in koud water. Welk voorwerp geeft warmte af en welk neemt warmte op?",
            opties=[
                "het blok geeft warmte af en het water neemt warmte op",
                "het water geeft warmte af en het blok neemt warmte op",
                "ze geven allebei warmte af aan de lucht van de kamer",
                "er gaat geen warmte over zolang ze elkaar niet raken",
            ],
            antwoord=0,
            uitleg="Warmte gaat altijd van het warmere naar het koudere voorwerp. Dat blijft doorgaan tot ze dezelfde temperatuur hebben, dus tot er thermisch evenwicht is.",
        ),
        "Bij convectie verplaatst de stof zelf zich en neemt ze de warmte mee.": dict(
            type="waarofniet",
            vraag="Warmte is de energie die van het ene systeem naar het andere gaat door een verschil in temperatuur.",
            antwoord=True,
            uitleg="Zonder temperatuurverschil is er geen warmte-uitwisseling. Warmte is dus geen eigenschap die in een voorwerp zit, maar energie die onderweg is.",
        ),
        "Hoe bereken je de merkbare warmte van een stof?": dict(
            type="meerkeuze",
            vraag="Wat gebeurt er met de deeltjes van een stof als haar temperatuur stijgt?",
            opties=[
                "ze bewegen sneller, dus hun kinetische energie neemt toe",
                "ze bewegen trager, dus hun kinetische energie neemt af",
                "ze worden zwaarder, dus de massa van de stof neemt toe",
                "ze blijven even snel, maar ze gaan verder uit elkaar staan",
            ],
            antwoord=0,
            uitleg="Temperatuur is een maat voor de beweging van de deeltjes. Meer warmte betekent snellere deeltjes en dus een hogere inwendige kinetische energie.",
        ),
        "Wat betekent een grote specifieke warmtecapaciteit?": dict(
            type="meerkeuze",
            vraag="Waarom is water een goede koelvloeistof in een motor?",
            opties=[
                "omdat het veel warmte opneemt zonder snel op te warmen",
                "omdat het veel sneller stroomt dan andere vloeistoffen",
                "omdat het bij hoge temperatuur meteen in damp overgaat",
                "omdat het geen enkele warmte van de motor kan opnemen",
            ],
            antwoord=0,
            uitleg="Water kan veel warmte wegnemen terwijl zijn eigen temperatuur maar langzaam stijgt. Daarom gebruikt men het in de koelkring van een motor en in een verwarmingsketel.",
        ),
        "Met welk toestel meet je in het labo hoeveel warmte een stof opneemt of afgeeft?": dict(
            type="invultekst",
            vraag="Welke grootheid meet je met een thermometer?",
            antwoord=["temperatuur", "de temperatuur"],
            uitleg="Een thermometer meet de temperatuur, niet de warmte. Hoeveel warmte er in het spel is, hangt ook af van de massa en de soort stof.",
        ),
        "Een halve liter water vraagt even veel warmte als een hele liter om er tien graden bij te krijgen.": dict(
            type="waarofniet",
            vraag="Warmte en temperatuur zijn twee woorden voor dezelfde grootheid.",
            antwoord=False,
            uitleg="Temperatuur zegt hoe snel de deeltjes bewegen, warmte is de energie die van het ene systeem naar het andere gaat. Een bad van 30 graden geeft meer warmte af dan een kopje van 30 graden.",
        ),
        "Waarom voelt een tegelvloer kouder aan dan een tapijt bij dezelfde temperatuur?": dict(
            type="meerkeuze",
            vraag="Waarom beregenen fruitboeren hun bomen als er nachtvorst op weg is?",
            opties=[
                "omdat water bij het bevriezen warmte afgeeft aan de knoppen",
                "omdat water bij het bevriezen warmte uit de knoppen opneemt",
                "omdat de laag water het licht van de maan weerkaatst",
                "omdat nat hout veel moeilijker breekt dan droog hout",
            ],
            antwoord=0,
            uitleg="Bij het stollen geeft een stof warmte af. Het water dat op de knoppen bevriest houdt ze zo rond nul graden, net warm genoeg om de vorstschade te voorkomen.",
        ),
        "Je verwarmt 2 kilogram water van 20 naar 30 graden. De specifieke warmtecapaciteit is 4180 joule per kilogram per graad. Hoeveel warmte is dat?": dict(
            type="meerkeuze",
            vraag="Waarom isoleert men de buitenmuren en het dak van een huis?",
            opties=[
                "om minder warmte te verliezen en dus minder te moeten verwarmen",
                "om de warmte in de muren zelf te kunnen opslaan voor de nacht",
                "om de temperatuur in het huis overal exact gelijk te houden",
                "om te verhinderen dat de muren bij vorst zouden beschadigen",
            ],
            antwoord=0,
            uitleg="Isolatie vertraagt het weglopen van warmte naar buiten. De warmte verdwijnt dan minder snel, dus moet de verwarming minder energie omzetten.",
        ),
        "Een stof met een kleine specifieke warmtecapaciteit koelt heel langzaam af.": dict(
            type="waarofniet",
            vraag="Een voorwerp met een hogere temperatuur bevat altijd meer warmte dan een voorwerp met een lagere temperatuur.",
            antwoord=False,
            uitleg="Het hangt ook af van de massa en de stof. Een kopje thee van 80 graden geeft veel minder warmte af dan een vol bad van 40 graden.",
        ),
        "Waarom stijgt warme lucht in een kamer naar het plafond?": dict(
            type="meerkeuze",
            vraag="Waarom blijft het aan de kust in de winter zachter dan in het binnenland?",
            opties=[
                "omdat het zeewater zijn warmte traag en lang afgeeft",
                "omdat de zee in de winter zelf warmte begint te maken",
                "omdat er aan de kust meer zon op het water valt",
                "omdat zout water pas bij een veel lagere temperatuur bevriest",
            ],
            antwoord=0,
            uitleg="De zee warmt in de zomer langzaam op en koelt in de winter langzaam af. Die traagheid van water maakt het klimaat aan de kust minder scherp dan verder landinwaarts.",
        ),
        "Hoe noem je de warmte die je merkt aan een verandering van temperatuur?": dict(
            type="invultekst",
            vraag="Hoe noem je de krachten die de deeltjes van een vloeistof bij elkaar houden?",
            antwoord=["cohesiekrachten", "cohesiekracht", "cohesie"],
            uitleg="Om een vloeistof te laten verdampen, moet je die cohesiekrachten overwinnen. De energie daarvoor gaat naar de inwendige potentiële energie, niet naar de temperatuur.",
        ),
        "Je giet een liter water van 80 graden bij een liter water van 20 graden. Wat wordt de eindtemperatuur ongeveer?": dict(
            type="meerkeuze",
            vraag="Je roert koude melk in warme koffie. Wat zegt de warmtebalans over die twee?",
            opties=[
                "de warmte die de koffie afgeeft, neemt de melk op",
                "de koffie en de melk geven allebei warmte af aan de tas",
                "de melk geeft warmte af tot ze even warm is als de koffie",
                "er gaat geen warmte over, want het blijft dezelfde vloeistof",
            ],
            antwoord=0,
            uitleg="De warmtebalans is de wet van behoud van energie in een andere vorm: wat het ene systeem afgeeft, komt bij het andere terecht, tot ze dezelfde temperatuur hebben.",
        ),
        "Hoe bereken je de latente warmte bij een faseovergang?": dict(
            type="meerkeuze",
            vraag="Wat gebeurt er met de inwendige energie van ijs terwijl het smelt?",
            opties=[
                "de inwendige potentiële energie stijgt, de temperatuur blijft gelijk",
                "de inwendige kinetische energie stijgt en de temperatuur stijgt mee",
                "de inwendige energie blijft gelijk, alleen de vorm verandert",
                "de inwendige potentiële energie daalt en er komt warmte vrij",
            ],
            antwoord=0,
            uitleg="De opgenomen warmte gaat naar het losmaken van de deeltjes uit hun vaste plaats, dus naar de inwendige potentiële energie. Daarom blijft de thermometer op nul graden staan.",
        ),
        "Hoe noem je de warmte die bij een faseovergang opgenomen wordt zonder dat de temperatuur stijgt?": dict(
            type="invultekst",
            vraag="Hoe noem je de temperatuur waarbij een vaste stof vloeibaar wordt?",
            antwoord=["smeltpunt", "het smeltpunt"],
            uitleg="Bij een zuivere stof is het smeltpunt een vaste temperatuur, en het stolpunt ligt op diezelfde waarde. Voor water is dat nul graden.",
        ),
        "Hoeveel warmte heb je nodig om 0,5 kilogram ijs te smelten, met 334 000 joule per kilogram?": dict(
            type="meerkeuze",
            vraag="Waarom blijft een drankje met ijsblokjes erin lang koud?",
            opties=[
                "omdat het smeltende ijs warmte opneemt zonder zelf op te warmen",
                "omdat het ijs koude afgeeft zolang er nog een blokje over is",
                "omdat het ijs de warmte van buiten tegen de wand tegenhoudt",
                "omdat het drankje door het ijs veel minder snel verdampt",
            ],
            antwoord=0,
            uitleg="Zolang er ijs smelt, gaat de opgenomen warmte naar de faseovergang en blijft het mengsel rond nul graden. Pas als het laatste blokje weg is, begint het drankje op te warmen.",
        ),
    }
)

# ───────────────────────────── Kracht: geen vrije val, geen verticale worp en
# geen veerconstante. Wel de kracht als vector, het samenstellen van
# krachtvectoren en de bewegingstoestand met haar voorbeelden uit het verkeer.
VERVANGINGEN.update(
    {
        "Wat is een vrije val?": dict(
            type="meerkeuze",
            vraag="Welke vier kenmerken heeft een kracht als vectoriële grootheid?",
            opties=[
                "grootte, richting, zin en aangrijpingspunt",
                "grootte, massa, snelheid en aangrijpingspunt",
                "richting, zin, massa en tijdsduur",
                "grootte, richting, gewicht en oppervlakte",
            ],
            antwoord=0,
            uitleg="Een kracht is niet alleen een getal. Je moet ook weten langs welke lijn ze werkt, in welke zin van die lijn, en op welk punt van het voorwerp ze aangrijpt.",
        ),
        "Hoe groot is de valversnelling op aarde ongeveer?": dict(
            type="meerkeuze",
            vraag="Hoe stel je een kracht in een tekening voor?",
            opties=[
                "met een pijl die in het aangrijpingspunt begint",
                "met een cirkel rond het punt waar de kracht werkt",
                "met een getal naast het voorwerp, zonder pijl",
                "met een rechte lijn zonder begin en zonder einde",
            ],
            antwoord=0,
            uitleg="De lengte van de pijl geeft de grootte, de lijn de richting en de punt de zin. Het begin van de pijl ligt in het aangrijpingspunt.",
        ),
        "Bij een vrije val zonder luchtweerstand vallen een steen en een pluim even snel.": dict(
            type="waarofniet",
            vraag="Een kracht heeft niet alleen een grootte, maar ook een richting en een zin.",
            antwoord=True,
            uitleg="Daarom is een kracht een vectoriële grootheid. Twee krachten van 10 newton kunnen elkaar opheffen of samen 20 newton geven, afhankelijk van hun zin.",
        ),
        "Je gooit een bal recht naar boven. Wat gebeurt er in het hoogste punt?": dict(
            type="meerkeuze",
            vraag="Een kist staat stil op de vloer. Hoe groot is de resulterende kracht erop?",
            opties=[
                "nul newton, want de zwaartekracht en de normaalkracht heffen elkaar op",
                "even groot als de zwaartekracht, want die werkt altijd naar beneden",
                "even groot als de normaalkracht, want de vloer duwt het hardst",
                "niet te bepalen zolang je de massa van de kist niet kent",
            ],
            antwoord=0,
            uitleg="De kist beweegt niet, dus is de resulterende kracht nul. De vloer duwt met de normaalkracht precies even hard omhoog als de zwaartekracht naar beneden trekt.",
        ),
        "Hoe noem je de beweging van een bal die je recht naar boven gooit?": dict(
            type="invultekst",
            vraag="Hoe noem je het punt van een voorwerp waarin een kracht aangrijpt?",
            antwoord=["aangrijpingspunt", "het aangrijpingspunt"],
            uitleg="Het aangrijpingspunt is een van de vier kenmerken van een kracht. In een tekening begint de pijl van de kracht daar.",
        ),
        "Een steen valt uit stilstand. Welke snelheid heeft hij na 2 seconden, met 10 meter per seconde kwadraat als valversnelling?": dict(
            type="meerkeuze",
            vraag="Twee mensen duwen een kast in dezelfde zin, de een met 80 en de ander met 50 newton. Hoe groot is de resulterende kracht?",
            opties=[
                "130 newton",
                "30 newton",
                "65 newton",
                "80 newton",
            ],
            antwoord=0,
            uitleg="Krachten op één lijn en in dezelfde zin tel je op. Zouden ze tegen elkaar in duwen, dan zou je ze van elkaar aftrekken en 30 newton overhouden.",
        ),
        "Bij een verticale worp naar boven is de versnelling tijdens het opgaan naar boven gericht.": dict(
            type="waarofniet",
            vraag="Een voorwerp dat vertraagt, heeft geen enkele kracht meer op zich werken.",
            antwoord=False,
            uitleg="Vertragen is juist een dynamisch effect van een resulterende kracht, die dan tegen de beweging in werkt. Bij een auto die remt is dat de wrijvingskracht van de remmen en de weg.",
        ),
        "Een voorwerp in een vrije val heeft tijdens het vallen een steeds grotere versnelling.": dict(
            type="waarofniet",
            vraag="Een vrachtwagen en een auto die met dezelfde snelheid rijden, hebben dezelfde remkracht nodig om te stoppen.",
            antwoord=False,
            uitleg="De vrachtwagen heeft veel meer massa en dus veel meer traagheid. Om hem op dezelfde afstand tot stilstand te brengen is een veel grotere remkracht nodig.",
        ),
        "Je laat een bal vallen en gooit een tweede bal op hetzelfde ogenblik recht naar beneden. Wat verschilt er?": dict(
            type="meerkeuze",
            vraag="Waarom moet de lading van een vrachtwagen goed vastgemaakt worden?",
            opties=[
                "omdat de lading door haar traagheid bij het remmen doorschuift",
                "omdat de lading anders zwaarder weegt dan de vrachtwagen zelf",
                "omdat de wrijving tussen de lading en de vloer anders te groot is",
                "omdat de lading anders de normaalkracht van de weg wegneemt",
            ],
            antwoord=0,
            uitleg="Dat is het traagheidsbeginsel: zonder kracht gaat de lading verder met de snelheid die ze had. Remt de vrachtwagen, dan schuift de lading naar voren tot iets haar tegenhoudt.",
        ),
        "Hoe bereken je de grootte van de zwaartekracht op een voorwerp?": dict(
            type="meerkeuze",
            vraag="Welke kracht duwt een voorwerp loodrecht weg van het oppervlak waarop het rust?",
            opties=[
                "de normaalkracht",
                "de wrijvingskracht",
                "de zwaartekracht",
                "de stuwkracht",
            ],
            antwoord=0,
            uitleg="De normaalkracht staat altijd loodrecht op het oppervlak. Op een vlakke vloer wijst ze dus recht naar boven, op een helling schuin weg van de helling.",
        ),
        "Een voorwerp van 5 kilogram hangt stil aan een veer. Hoe groot is de veerkracht, met 10 newton per kilogram?": dict(
            type="meerkeuze",
            vraag="Welke kracht laat een raket vooruitgaan?",
            opties=[
                "de stuwkracht",
                "de normaalkracht",
                "de veerkracht",
                "de wrijvingskracht",
            ],
            antwoord=0,
            uitleg="De uitgestoten gassen duwen de raket vooruit met een stuwkracht. Bij een auto heet de kracht die hetzelfde doet de motorkracht.",
        ),
        "Hoe bereken je de veerkracht van een veer?": dict(
            type="meerkeuze",
            vraag="Waarom is de remafstand van een auto langer op een natte weg?",
            opties=[
                "omdat de wrijvingskracht tussen de band en de weg kleiner is",
                "omdat de auto op een natte weg meer massa en traagheid heeft",
                "omdat de normaalkracht van de weg op de auto kleiner wordt",
                "omdat de motorkracht op een natte weg blijft doorwerken",
            ],
            antwoord=0,
            uitleg="Een kleinere wrijvingskracht betekent een kleinere resulterende kracht die de auto vertraagt. Daarom is de remweg langer, en bij een hogere snelheid nog veel langer.",
        ),
        "Een veer met een grotere veerconstante rekt bij dezelfde kracht minder uit.": dict(
            type="waarofniet",
            vraag="Een voorwerp blijft in rust of beweegt rechtdoor met een constante snelheid zolang de resulterende kracht nul is.",
            antwoord=True,
            uitleg="Dat is het traagheidsbeginsel. Een kracht is dus niet nodig om een beweging aan te houden, alleen om ze te veranderen.",
        ),
        "Welke uitspraken over de zwaarteveldsterkte zijn juist? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke krachten werken op een vliegtuig dat in de lucht vliegt? Kruis alles aan wat juist is.",
            opties=[
                "de stuwkracht van de motoren",
                "de zwaartekracht naar beneden",
                "de wrijvingskracht van de lucht",
                "de normaalkracht van de landingsbaan",
            ],
            antwoord=[0, 1, 2],
            uitleg="Een normaalkracht bestaat alleen zolang het vliegtuig op een oppervlak rust. In de lucht blijven de stuwkracht, de zwaartekracht, de luchtwrijving en de draagkracht van de vleugels over.",
        ),
        "Een veer rekt 4 centimeter uit bij een kracht van 20 newton. Wat is de veerconstante?": dict(
            type="meerkeuze",
            vraag="Twee krachten van 60 en 25 newton werken op hetzelfde punt op één lijn, maar in tegengestelde zin. Hoe groot is de resulterende kracht?",
            opties=[
                "35 newton",
                "85 newton",
                "60 newton",
                "1500 newton",
            ],
            antwoord=0,
            uitleg="Op één lijn en in tegengestelde zin trek je de grootten van elkaar af. De zin van de resulterende kracht is die van de grootste van de twee.",
        ),
        "Hoeveel newton is de zwaartekracht op een massa van 2 kilogram, met 10 newton per kilogram?": dict(
            type="invultekst",
            vraag="Hoe noem je de kracht waarmee een veer terugduwt als je ze indrukt?",
            antwoord=["veerkracht", "de veerkracht"],
            uitleg="De veerkracht werkt tegen de vervorming in. Laat je de veer los, dan duwt die kracht ze terug naar haar oorspronkelijke lengte.",
        ),
    }
)

# ───────────────────────────── Druk: geen hydrostatische druk, geen beginsel
# van Pascal en geen gaswetten met de kelvinschaal. Wel p = F / A, de gasdruk
# volgens het deeltjesmodel, de manometer en de barometer, de overdruk en de
# onderdruk, en de toepassingen die de fiche opsomt.
VERVANGINGEN.update(
    {
        "Hoe noem je de druk die door het gewicht van een vloeistof zelf ontstaat?": dict(
            type="invultekst",
            vraag="Met welk toestel meet je de druk van een gas in een vat of een leiding?",
            antwoord=["manometer", "een manometer"],
            uitleg="Een manometer meet de druk binnen in een vat, bijvoorbeeld in een gasfles of aan een fietspomp. De luchtdruk buiten meet je met een barometer.",
        ),
        "Waarvan hangt de hydrostatische druk in een vloeistof af? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke voorbeelden gebruiken een groot oppervlak om de druk klein te houden? Kruis alles aan wat juist is.",
            opties=[
                "de brede rupsbanden van een graafmachine",
                "de sneeuwschoenen van een wandelaar",
                "de brede poten onder een zware kast",
                "de scherpe punt van een duimspijker",
            ],
            antwoord=[0, 1, 2],
            uitleg="Bij dezelfde kracht geeft een groter oppervlak een kleinere druk, dus zak je minder diep weg en beschadig je de ondergrond niet. Een duimspijker wil juist een heel grote druk.",
        ),
        "De hydrostatische druk op tien meter diepte is groter dan op twee meter diepte.": dict(
            type="waarofniet",
            vraag="Je meet druk in pascal, en honderd pascal is één hectopascal.",
            antwoord=True,
            uitleg="Hecto betekent honderd, kilo betekent duizend. Een weerbericht spreekt over 1013 hectopascal, en dat is hetzelfde als 101 300 pascal.",
        ),
        "Wat zegt het beginsel van Pascal?": dict(
            type="meerkeuze",
            vraag="Wat betekent overdruk?",
            opties=[
                "een druk die hoger is dan de druk van de omgeving",
                "een druk die lager is dan de druk van de omgeving",
                "de druk die een gas op de bodem van een vat uitoefent",
                "de hoogste druk die een vat kan verdragen zonder te breken",
            ],
            antwoord=0,
            uitleg="In een opgepompte fietsband heerst overdruk, in een vacuümzak voor voeding onderdruk. Een manometer toont vaak net dat verschil met de buitenlucht.",
        ),
        "Waarom moet je tijdens het duiken je oren klaren?": dict(
            type="meerkeuze",
            vraag="Waarom suizen je oren als een vliegtuig opstijgt?",
            opties=[
                "omdat de luchtdruk buiten daalt en de druk in je oor nog hoog blijft",
                "omdat de luchtdruk buiten stijgt en je oor die druk niet verdraagt",
                "omdat de lucht in je oor bij het stijgen helemaal verdwijnt",
                "omdat de motoren van het vliegtuig de lucht rond je hoofd verwarmen",
            ],
            antwoord=0,
            uitleg="Er komt dan een drukverschil over je trommelvel te staan. Slikken of gapen opent het buisje naar je neus, zodat de druk aan beide kanten weer gelijk wordt.",
        ),
        "Een duiker ondervindt op grote diepte alleen de hydrostatische druk, niet de luchtdruk.": dict(
            type="waarofniet",
            vraag="De luchtdruk is op elke hoogte precies dezelfde.",
            antwoord=False,
            uitleg="Hoe hoger je komt, hoe minder lucht er nog boven je ligt en hoe lager de luchtdruk. Daarom staat een zak chips in de bergen bol.",
        ),
        "Waarom staat een hydraulische pers met een kleine kracht een grote kracht te leveren?": dict(
            type="meerkeuze",
            vraag="Waarom kan je met een rietje een vloeistof opzuigen?",
            opties=[
                "omdat de druk in het rietje daalt en de luchtdruk de drank omhoog duwt",
                "omdat je met je mond aan de vloeistof zelf een kracht geeft",
                "omdat de druk in het rietje stijgt en de drank daardoor meegaat",
                "omdat een vloeistof altijd naar de kleinste opening toe stroomt",
            ],
            antwoord=0,
            uitleg="Zuigen maakt onderdruk in het rietje. Het verschil met de luchtdruk op de drank in het glas duwt de vloeistof dan naar boven.",
        ),
        "Nul kelvin is het absolute nulpunt, waarbij de deeltjes geen kinetische energie meer hebben.": dict(
            type="waarofniet",
            vraag="De druk van een gas in een gesloten fles stijgt als je de fles verwarmt.",
            antwoord=True,
            uitleg="De deeltjes gaan sneller bewegen en botsen daardoor vaker en harder tegen de wand. Op een spuitbus staat daarom dat je ze niet mag verwarmen.",
        ),
        "Hoeveel kelvin is 27 graden Celsius?": dict(
            type="meerkeuze",
            vraag="Hoeveel pascal is één kilopascal?",
            opties=[
                "1000 pascal",
                "100 pascal",
                "10 pascal",
                "1 000 000 pascal",
            ],
            antwoord=0,
            uitleg="Kilo betekent duizend. De druk van een fietsband schrijf je daarom liever in kilopascal of in bar dan in pascal, want in pascal krijg je heel grote getallen.",
        ),
        "Hoe noem je de temperatuurschaal die bij het absolute nulpunt begint?": dict(
            type="invultekst",
            vraag="Hoe noem je de druk van de lucht rond ons, die op zeeniveau ongeveer 1013 hectopascal is?",
            antwoord=["luchtdruk", "atmosferische druk", "de luchtdruk"],
            uitleg="De luchtdruk komt van het gewicht van de lucht boven ons. Een barometer meet hem, en een dalende luchtdruk kondigt vaak slechter weer aan.",
        ),
        "Wat is een isotherm proces?": dict(
            type="meerkeuze",
            vraag="Waarom zit er op een drukvat een veiligheidsklep?",
            opties=[
                "omdat de klep opengaat zodra de druk binnen te hoog wordt",
                "omdat de klep de druk binnen altijd op dezelfde waarde houdt",
                "omdat de klep verhindert dat er lucht in het vat kan komen",
                "omdat de klep de temperatuur van het gas in het vat meet",
            ],
            antwoord=0,
            uitleg="De klep laat gas ontsnappen voor de druk het vat kan doen barsten. Verwarmt een gasfles in de zon, dan stijgt de druk, en net dan is die klep nodig.",
        ),
        "Bij een isochoor proces blijft het volume van het gas gelijk.": dict(
            type="waarofniet",
            vraag="Een gas oefent druk uit doordat zijn deeltjes tegen de wand botsen.",
            antwoord=True,
            uitleg="Elke botsing geeft een duwtje. Miljarden botsingen per seconde samen voelen aan als een gelijkmatige druk op de hele wand.",
        ),
        "Welke grootheden zijn toestandsgrootheden van een gas? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke eenheden gebruikt men voor druk? Kruis alles aan wat juist is.",
            opties=[
                "pascal",
                "kilopascal",
                "hectopascal",
                "newton",
            ],
            antwoord=[0, 1, 2],
            uitleg="De newton is de eenheid van kracht, niet van druk. Een pascal is één newton per vierkante meter.",
        ),
        "Hoe noem je een proces waarbij de druk van het gas gelijk blijft?": dict(
            type="invultekst",
            vraag="Welke grootheid deel je door de oppervlakte om de druk te krijgen?",
            antwoord=["kracht", "de kracht"],
            uitleg="De formule is p = F / A, dus druk is de grootte van de kracht per oppervlakte. Dezelfde kracht op een kleiner oppervlak geeft dus een grotere druk.",
        ),
        "Een gas van 2 liter bij 1 bar wordt bij gelijke temperatuur tot 1 liter samengeperst. Wat is de druk?": dict(
            type="meerkeuze",
            vraag="Je duwt met 600 newton op een oppervlak van 0,2 vierkante meter. Hoe groot is de druk?",
            opties=[
                "3000 pascal",
                "120 pascal",
                "300 pascal",
                "30 000 pascal",
            ],
            antwoord=0,
            uitleg="Je deelt de kracht door de oppervlakte: 600 newton gedeeld door 0,2 vierkante meter is 3000 pascal, of 3 kilopascal.",
        ),
        "Een reëel gas gedraagt zich precies zoals een ideaal gas, bij elke druk en temperatuur.": dict(
            type="waarofniet",
            vraag="Bij dezelfde kracht geeft een groter oppervlak een grotere druk.",
            antwoord=False,
            uitleg="Het omgekeerde: een groter oppervlak verdeelt dezelfde kracht over meer plaats, dus wordt de druk kleiner. Daarom zak je met sneeuwschoenen minder diep weg.",
        ),
        "Hoe ziet de grafiek van de druk tegenover het volume van een gas uit, bij een vaste temperatuur?": dict(
            type="meerkeuze",
            vraag="Waarom pompen wielrijders hun banden in de zomer wat minder hard op?",
            opties=[
                "omdat de warmte de druk in de band nog verder doet stijgen",
                "omdat de warmte de druk in de band juist doet dalen",
                "omdat het rubber in de zomer veel steviger wordt",
                "omdat een zachte band in de zomer minder wrijving geeft",
            ],
            antwoord=0,
            uitleg="Warme lucht in de band betekent sneller bewegende deeltjes en dus een hogere druk. Een band die je in de zomer tot de bovengrens oppompt, staat daarna te hard.",
        ),
        "Een gas van 300 kelvin bij 1 bar wordt in een gesloten vat tot 600 kelvin verwarmd. Wat is de druk?": dict(
            type="meerkeuze",
            vraag="Waarom kan een gasfles ontploffen als ze in de volle zon staat?",
            opties=[
                "omdat de deeltjes sneller bewegen en de druk in de fles stijgt",
                "omdat het gas in de fles door de warmte vloeibaar wordt",
                "omdat de wand van de fles door de warmte dunner wordt",
                "omdat de luchtdruk buiten de fles door de zon sterk daalt",
            ],
            antwoord=0,
            uitleg="Het volume van de stalen fles kan niet mee, dus komt alle warmte in de druk terecht. Daarom bewaart men gasflessen in de schaduw en zet men er een veiligheidsklep op.",
        ),
        "In de gaswetten moet je de temperatuur in kelvin invullen en niet in graden Celsius.": dict(
            type="waarofniet",
            vraag="Je kan de druk op een oppervlak kleiner maken door het oppervlak te vergroten of de kracht te verkleinen.",
            antwoord=True,
            uitleg="Dat volgt rechtstreeks uit p = F / A. Een rugzak met brede banden is daar een voorbeeld van: dezelfde kracht, maar over meer schouder verdeeld.",
        ),
        "Welke uitspraken over het absolute nulpunt zijn juist? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke uitspraken over de druk van een gas zijn juist? Kruis alles aan wat juist is.",
            opties=[
                "ze stijgt als je het gas in een kleinere ruimte perst",
                "ze stijgt als je het gas in een gesloten vat verwarmt",
                "ze komt van de botsingen van de deeltjes tegen de wand",
                "ze werkt alleen op de bodem van het vat",
            ],
            antwoord=[0, 1, 2],
            uitleg="De deeltjes bewegen in alle richtingen, dus duwt het gas overal even hard tegen de wand. Vaker of harder botsen betekent meer druk.",
        ),
        "Hoeveel graden Celsius is 273 kelvin?": dict(
            type="invultekst",
            vraag="Hoeveel pascal is één hectopascal?",
            antwoord=["100", "honderd"],
            uitleg="Hecto betekent honderd. De 1013 hectopascal van het weerbericht zijn dus 101 300 pascal.",
        ),
        # Dezelfde vraag, maar de uitleg noemde een isobaar proces. Dat woord
        # hoort bij de gaswetten en staat niet in deze fiche.
        "Waarom loopt een ballon die je in de koelkast legt, wat leeg?": dict(
            type="meerkeuze",
            vraag="Waarom loopt een ballon die je in de koelkast legt, wat leeg?",
            opties=[
                "de deeltjes bewegen trager, dus daalt de druk en krimpt de ballon",
                "er ontsnapt lucht door de koude wand van de ballon naar buiten",
                "de lucht in de ballon wordt vloeibaar bij een lagere temperatuur",
                "het rubber van de ballon wordt bij koude veel elastischer dan ervoor",
            ],
            antwoord=0,
            uitleg="Tragere deeltjes botsen minder hard tegen de wand. De ballon krimpt tot de druk binnen weer in evenwicht is met de luchtdruk buiten.",
        ),
    }
)

# ───────────────────────────── Laatste schoonmaak: vragen die op zich wel in
# deze fiche passen, maar in een optie of in hun uitleg nog een begrip uit de
# doorstroomfiche noemen. De vraag blijft, het begrip gaat eruit.
VERVANGINGEN.update(
    {
        "Je krijgt een organisme te zien dat eencellig is, geen kernmembraan heeft en zich door celsplitsing vermeerdert. Waar hoort het thuis?": dict(
            type="meerkeuze",
            vraag="Je krijgt een organisme te zien dat eencellig is, geen kern heeft en zich door celsplitsing vermeerdert. Wat is het?",
            opties=[
                "een bacterie",
                "een gist",
                "een schimmel",
                "een virus",
            ],
            antwoord=0,
            uitleg="Een gist is eencellig maar heeft een kern, een schimmel bestaat uit schimmeldraden, en een virus is geen cel. Alleen bij een bacterie ligt het DNA vrij in de cel.",
        ),
        "Waarom lijken de eigenschappen van elementen in eenzelfde groep zo sterk op elkaar?": dict(
            type="meerkeuze",
            vraag="Waarom lijken de eigenschappen van elementen in eenzelfde groep zo sterk op elkaar?",
            opties=[
                "ze hebben evenveel elektronen in hun buitenste schil",
                "ze hebben evenveel neutronen in hun kern",
                "ze hebben allemaal evenveel protonen in hun kern",
                "ze staan alle vier in dezelfde periode van het PSE",
            ],
            antwoord=0,
            uitleg="Het chemische gedrag wordt bepaald door de buitenste schil. Zijn die gelijk, dan reageren de elementen op dezelfde manier.",
        ),
        "Hoe noem je de energie die een voorwerp heeft door zijn hoogte boven de grond?": dict(
            type="invultekst",
            vraag="Hoe noem je de energie die een voorwerp heeft door zijn hoogte boven de grond?",
            antwoord=["gravitationele potentiële energie", "gravitationele energie"],
            uitleg="Hoe hoger en hoe zwaarder het voorwerp, hoe meer van die energie het heeft. Daarom slaat een stuwmeer hoog in de bergen zo veel energie op.",
        ),
        "Waarom wordt een rem warm als je met de fiets afdaalt en blijft remmen?": dict(
            type="meerkeuze",
            vraag="Waarom wordt een rem warm als je met de fiets afdaalt en blijft remmen?",
            opties=[
                "de kinetische energie van de fiets wordt door wrijving warmte",
                "de rem haalt warmte uit de lucht die eromheen langs stroomt",
                "de chemische energie in het remblokje komt daarbij vrij",
                "de hoogte-energie van de fiets wordt rechtstreeks stralingsenergie",
            ],
            antwoord=0,
            uitleg="De wrijving tussen het remblokje en de velg zet de energie van de bewegende fiets om in warmte. Die warmte is hier de ongewenste energie.",
        ),
        "Waarom blijft de zee in september nog warm terwijl de lucht al afkoelt?": dict(
            type="meerkeuze",
            vraag="Waarom houd je een brandwonde onder koud stromend water?",
            opties=[
                "omdat het stromende water warmte uit de huid blijft wegnemen",
                "omdat koud water koude in de huid brengt waar de warmte zat",
                "omdat het water de huid daardoor sneller laat verdampen",
                "omdat koud water de bloedvaten in de huid juist verwijdt",
            ],
            antwoord=0,
            uitleg="Koude kan niet overgaan, warmte wel. Stromend water voert de warmte af en blijft zelf koud, zodat de warmte niet dieper in het weefsel trekt.",
        ),
        "Welke uitspraken over warmte en temperatuur zijn juist? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke uitspraken over warmte en temperatuur zijn juist? Kruis alles aan wat juist is.",
            opties=[
                "temperatuur meet je in graden Celsius",
                "warmte is energie en meet je in joule",
                "warmte gaat altijd van warm naar koud",
                "warmte en temperatuur zijn twee woorden voor hetzelfde",
            ],
            antwoord=[0, 1, 2],
            uitleg="Temperatuur zegt hoe snel de deeltjes bewegen, warmte is de energie die van het ene systeem naar het andere gaat. Je kan warmte dus niet in graden uitdrukken.",
        ),
        "Welke faseovergangen zijn het? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke faseovergangen zijn het? Kruis alles aan wat juist is.",
            opties=[
                "sublimeren",
                "condenseren",
                "desublimeren",
                "krimpen",
            ],
            antwoord=[0, 1, 2],
            uitleg="Sublimeren is van vast rechtstreeks naar gas, desublimeren het omgekeerde. Krimpen is geen faseovergang: de stof blijft dan in dezelfde fase.",
        ),
        "Waarom kan je je lelijk verbranden aan stoom van honderd graden, erger dan aan water van honderd graden?": dict(
            type="meerkeuze",
            vraag="Waarom kan je je lelijk verbranden aan stoom van honderd graden, erger dan aan water van honderd graden?",
            opties=[
                "de stoom geeft bij het condenseren op je huid nog extra warmte af",
                "de stoom is in werkelijkheid veel heter dan honderd graden",
                "de stoom dringt veel sneller door je huid dan vloeibaar water",
                "de stoom blijft veel langer op je huid liggen dan water zou doen",
            ],
            antwoord=0,
            uitleg="Om water te laten verdampen is veel warmte nodig, en bij het condenseren komt die er weer uit. Op je huid komt die warmte dus bovenop de warmte van het water zelf.",
        ),
        "Je legt een ijsblokje in een glas water en het water koelt af. Waarom?": dict(
            type="meerkeuze",
            vraag="Je legt een ijsblokje in een glas water en het water koelt af. Waarom?",
            opties=[
                "het ijs neemt warmte uit het water op om te kunnen smelten",
                "het ijs geeft koude af aan het water om het heen",
                "het ijs duwt het warme water naar de bovenkant van het glas",
                "het ijs laat de warmte van het water door zich heen stralen",
            ],
            antwoord=0,
            uitleg="Koude bestaat niet als iets dat overgaat. Het smelten haalt warmte uit het water zonder dat het ijs zelf warmer wordt, en daardoor zakt de temperatuur.",
        ),
        "Welke uitspraken over massa en gewicht zijn juist? Kruis alles aan wat juist is.": dict(
            type="meerkeuze",
            vraag="Welke uitspraken over massa en gewicht zijn juist? Kruis alles aan wat juist is.",
            opties=[
                "massa is de hoeveelheid materie in een voorwerp",
                "gewicht is een kracht en meet je in newton",
                "je massa blijft op de maan dezelfde",
                "je gewicht blijft op de maan hetzelfde",
            ],
            antwoord=[0, 1, 2],
            uitleg="Je massa is overal gelijk, ook op de maan. Je gewicht is daar ongeveer zes keer kleiner, want de maan trekt veel minder hard aan je dan de aarde.",
        ),
        "Je meet de zwaartekracht op verschillende massa's en zet ze in een grafiek. Wat zie je?": dict(
            type="meerkeuze",
            vraag="Je meet de zwaartekracht op verschillende massa's en zet ze in een grafiek. Wat zie je?",
            opties=[
                "een rechte door de oorsprong, want de twee zijn recht evenredig",
                "een kromme die naar boven afbuigt bij grotere massa's",
                "een vlakke lijn, want de zwaartekracht blijft altijd gelijk",
                "een rechte die daalt, want een grotere massa valt trager",
            ],
            antwoord=0,
            uitleg="Twee keer zoveel massa geeft twee keer zoveel zwaartekracht, dus liggen alle meetpunten op één rechte die in de oorsprong begint.",
        ),
    }
)

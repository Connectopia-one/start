# -*- coding: utf-8 -*-
"""Veilig en duurzaam werken in het labo — 🌍 Beyond, biologie.

Deel 1 gaat over het materiaal: glaswerk, de bunsenbrander, de balans, de
thermometer en de microscoop, met het meetbereik en de nauwkeurigheid erbij.
Deel 2 gaat over stoffen en biologisch materiaal: de gevarenpictogrammen, de
hygiëne bij het werken met kweken en weefsel, het sorteren van afval en het
duurzaam omspringen met producten.

De fiche vraagt dat de leerling uitlegt hoe veilig en duurzaam gewerkt wordt
en goede van slechte werkwijzen onderscheidt. Het is dus geen praktijkproef op
papier: de vragen leggen telkens een werkwijze voor en vragen waarom ze goed
of fout is. De pictogrammen worden in woorden beschreven, want een tekening
ervan zou de eigenlijke vorm verraden of vervalsen.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag="Wat lees je altijd eerst, voor je met een product begint te werken?",
        antwoord=["het etiket", "etiket", "de etiket"],
        uitleg="Op het etiket staan de pictogrammen, de gevarenzinnen en de "
        "voorzorgsmaatregelen. Wie dat overslaat, weet niet wat hij in handen heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het meetbereik van een instrument?",
        opties=[
            "tussen welke waarden het betrouwbaar meet",
            "hoe fijn de schaalverdeling is",
            "hoe lang het meegaat voor het stuk is",
            "hoeveel het instrument weegt",
        ],
        antwoord=0,
        uitleg="Meet je buiten dat bereik, dan klopt het resultaat niet en kan het toestel "
        "beschadigen. Een balans voor 200 gram belaad je dus niet met een kilo.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de kleinste waarde die je met een instrument nog kunt onderscheiden?",
        antwoord=["nauwkeurigheid", "de nauwkeurigheid", "precisie"],
        uitleg="Een thermometer met streepjes van een halve graad lees je niet af tot op "
        "een honderdste. Je noteert dus niet meer cijfers dan het toestel aankan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet je een meettoestel uit als je niet meet?",
        opties=[
            "om stroom en batterijen te sparen",
            "omdat het anders verkeerde waarden geeft",
            "omdat het anders niet meer te gebruiken is",
            "omdat het anders opwarmt en ontploft",
        ],
        antwoord=0,
        uitleg="Dat is het duurzame deel van het werken: energie en materiaal sparen. Een "
        "toestel dat de hele les aan staat, verbruikt voor niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een balans zet je altijd op nul voor je iets afweegt.",
        antwoord=True,
        uitleg="Zo weeg je het recipiënt niet mee. Vergeet je dat, dan meet je een massa "
        "die er niet is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als er glaswerk breekt? Kruis alles aan wat juist is.",
        opties=[
            "de scherven met borstel en blik opruimen",
            "de scherven bij het glasafval doen",
            "de scherven met de blote hand oprapen",
            "de scherven met water in de gootsteen spoelen",
        ],
        antwoord=[0, 1],
        uitleg="Scherven raak je niet met de hand aan en ze horen niet bij het gewone "
        "afval. In de gootsteen beschadigen ze bovendien de afvoer.",
    ),
    dict(
        type="waarofniet",
        vraag="Je bedient elektrische toestellen nooit met natte handen.",
        antwoord=True,
        uitleg="Water geleidt stroom, dus stijgt de kans op een schok. Dat geldt ook voor "
        "een natte werkbank onder het toestel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je meteen als je iets morst?",
        opties=[
            "opkuisen volgens de voorschriften van dat product",
            "er een blad papier overleggen tot later",
            "wachten tot het vanzelf opdroogt",
            "er water bij gieten om het te verdunnen",
        ],
        antwoord=0,
        uitleg="Gemorste producten geven glij- en contactgevaar, en sommige dampen uit. "
        "Welke stof het is, bepaalt hoe je opruimt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop let je bij het werken met een bunsenbrander? Kruis alles aan wat juist is.",
        opties=[
            "lang haar en losse kledij vastmaken",
            "geen brandbare producten in de buurt zetten",
            "de vlam blauw houden omdat die niet heet is",
            "de brander onbewaakt laten branden tussen twee proeven",
        ],
        antwoord=[0, 1],
        uitleg="De blauwe vlam is net de heetste en bovendien slecht zichtbaar. Een brander "
        "laat je nooit zonder toezicht branden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom draag je een veiligheidsbril bij het verhitten van een vloeistof?",
        opties=[
            "de vloeistof kan opspatten of overkoken",
            "de damp maakt het glas van de bril helder",
            "de bril houdt de warmte van je gezicht",
            "de bril verbetert het zicht op de schaal",
        ],
        antwoord=0,
        uitleg="Een vloeistof kan plots overkoken en wegspatten. Ogen herstellen zich niet "
        "van een spat zuur of kokend water.",
    ),
    dict(
        type="invultekst",
        vraag="Waarmee pak je een warm bekerglas vast?",
        antwoord=["bekerglastang", "een tang", "tang"],
        uitleg="Glas ziet er warm net zo uit als koud. Daarom pak je het vast met een tang "
        "of een hittebestendige handschoen.",
    ),
    dict(
        type="invultekst",
        vraag="Aan welke twee delen draag je een microscoop?",
        antwoord=["arm en voet", "statiefarm en voet", "voet en arm"],
        uitleg="De lenzen zijn het kostbaarste en het kwetsbaarste deel. Daarom draag je "
        "het toestel aan de statiefarm en onder de voet, en nooit aan een los onderdeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom start je het bekijken van een preparaat met het kleinste objectief?",
        opties=[
            "zo vind je het beeld en vermijd je schade aan de lens",
            "zo is het beeld meteen het scherpst van allemaal",
            "zo gebruikt de microscoop minder licht",
            "zo is het preparaat sneller droog",
        ],
        antwoord=0,
        uitleg="Bij een klein objectief is het beeldveld groter en is de afstand tot het "
        "glas veilig. Pas daarna schakel je naar een sterkere vergroting.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de grootste vergroting stel je scherp met de grove stelschroef.",
        antwoord=False,
        uitleg="Met de grove schroef duw je het objectief door het dekglaasje. Op die "
        "stand gebruik je alleen de fijne stelschroef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je glaswerk na gebruik onmiddellijk schoon?",
        opties=[
            "opgedroogde resten gaan er nadien moeilijk af",
            "glas wordt anders sneller breekbaar",
            "nat glaswerk is beter zichtbaar in de kast",
            "anders mag het niet in de kast",
        ],
        antwoord=0,
        uitleg="Resten die indrogen, vragen later meer water en meer product. Dat is zowel "
        "onveilig voor de volgende gebruiker als verspilling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn goed bij het meten? Kruis alles aan wat juist is.",
        opties=[
            "het instrument kiezen dat bij de grootte van de meting past",
            "noteren met evenveel cijfers als het toestel aangeeft",
            "een meting naar boven afronden tot een mooi getal",
            "het toestel ijken met een willekeurig voorwerp",
        ],
        antwoord=[0, 1],
        uitleg="Een passend bereik en een eerlijke notatie houden het resultaat bruikbaar. "
        "Afronden tot een mooi getal verzint nauwkeurigheid die er niet is.",
    ),
    dict(
        type="waarofniet",
        vraag="Je ruikt aan een product door het flesje recht onder je neus te houden.",
        antwoord=False,
        uitleg="Als je al ruikt, dan door met je hand wat damp naar je toe te wuiven. "
        "Rechtstreeks inademen kan luchtwegen en longen beschadigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je de handleiding van een toestel voor je het gebruikt?",
        opties=[
            "ze zegt hoe je het veilig en juist bedient",
            "ze bevat de prijs van de onderdelen",
            "ze vervangt het etiket van de producten",
            "ze geeft de uitslag van de proef",
        ],
        antwoord=0,
        uitleg="In de handleiding staan het bereik, de bediening en het onderhoud. Zonder "
        "die kennis beschadig je het toestel of meet je verkeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zet een warme kolf meteen op de koude stenen tafel. Wat is daar fout aan?",
        opties=[
            "door het plotse temperatuurverschil kan het glas barsten",
            "het glas wordt daardoor te snel vuil",
            "de tafel neemt de stof van het glas gedeeltelijk over",
            "de kolf weegt daarna niet meer juist",
        ],
        antwoord=0,
        uitleg="Glas zet uit en krimpt bij temperatuurverschillen. Een snelle afkoeling "
        "geeft spanningen en dus barsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort duurzaam werken bij veilig werken?",
        opties=[
            "minder product gebruiken geeft ook minder afval en risico",
            "duurzaam werken duurt langer en dus veiliger",
            "duurzaam werken vervangt de persoonlijke beschermingsmiddelen",
            "duurzaam werken geldt alleen buiten het labo",
        ],
        antwoord=0,
        uitleg="Wie afmeet wat hij nodig heeft, morst minder en gooit minder weg. Zuinig "
        "omgaan met producten is dus tegelijk veiliger.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent een pictogram met een vlam op een oranje of rood omrand ruitje?",
        opties=[
            "het product is ontvlambaar",
            "het product is giftig bij inslikken",
            "het product tast metalen aan",
            "het product is gevaarlijk voor het water",
        ],
        antwoord=0,
        uitleg="De vlam waarschuwt voor ontvlambaarheid. Zo'n product komt niet in de buurt "
        "van een bunsenbrander of een vonk.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor waarschuwt het pictogram met een doodshoofd?",
        antwoord=["giftig", "acuut giftig", "vergiftiging"],
        uitleg="Dat teken staat voor giftig bij inademen, inslikken of huidcontact. Het "
        "uitroepteken waarschuwt voor de mildere irritatie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk pictogram toont een hand en een oppervlak waarop een vloeistof inwerkt?",
        antwoord=["bijtend", "corrosief", "het bijtende"],
        uitleg="Bijtende stoffen tasten huid, ogen en materialen aan. Bij die producten "
        "horen altijd bril en handschoenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een product zonder gevarenpictogram is altijd volkomen veilig.",
        antwoord=False,
        uitleg="Een ontbrekend pictogram betekent alleen dat die gevaren niet gelden. Je "
        "leest nog steeds het etiket en je drinkt nog steeds niets in een labo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom eet of drink je niet in een labo?",
        opties=[
            "producten en kiemen kunnen zo in je lichaam komen",
            "eten maakt de meettoestellen onnauwkeurig",
            "eten verandert de uitslag van de proef die je doet",
            "eten is er te duur",
        ],
        antwoord=0,
        uitleg="Via je handen of een glas komt er zo iets binnen dat er niet hoort. Daarom "
        "blijven drank en eten buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je om met een bacteriekweek in een petrischaal? Kruis alles aan wat juist is.",
        opties=[
            "de schaal gesloten houden",
            "de handen nadien grondig wassen",
            "de schaal openen om eraan te ruiken",
            "de schaal bij het papierafval gooien",
        ],
        antwoord=[0, 1],
        uitleg="Ook een onschuldige kweek kan ongewenste kiemen bevatten. Ze gaat gesloten "
        "weer weg en wordt eerst ontsmet of gesteriliseerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontsmet je het werkblad voor én na een proef met biologisch materiaal? Kruis alles aan wat juist is.",
        opties=[
            "vooraf houdt het je proef zuiver",
            "achteraf houdt het de volgende gebruiker veilig",
            "het laat de weegschaal juister meten",
            "het verdrijft de geur van het product",
        ],
        antwoord=[0, 1],
        uitleg="Ontsmetten werkt dus in twee richtingen: het beschermt je proef én de "
        "mensen die na jou aan die tafel werken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het volledig kiemvrij maken van materiaal, meestal met stoom onder druk?",
        antwoord=["steriliseren", "sterilisatie", "autoclaveren"],
        uitleg="In een autoclaaf gaat alles bij ruim honderd graden onder druk. Ontsmetten "
        "doodt het meeste, steriliseren alles.",
    ),
    dict(
        type="waarofniet",
        vraag="Biologisch afval mag gewoon bij het restafval.",
        antwoord=False,
        uitleg="Kweken, weefsel en besmet materiaal gaan in een aparte, gemerkte container. "
        "Die wordt apart verwerkt of eerst gesteriliseerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom giet je chemisch afval niet in de gootsteen?",
        opties=[
            "het komt zo in het oppervlaktewater terecht",
            "het beschadigt de kraan van de gootsteen",
            "het maakt het water te hard",
            "het verdampt anders te traag",
        ],
        antwoord=0,
        uitleg="De waterzuivering haalt niet alles eruit, en sommige stoffen zijn zelfs in "
        "kleine hoeveelheden schadelijk voor het leven in het water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met de rest van een product dat je afgemeten hebt maar niet gebruikt?",
        opties=[
            "in het daarvoor voorziene afvalvat doen",
            "terug in de voorraadfles gieten",
            "in de gootsteen uitgieten met veel water",
            "in de vuilnisbak van de klas gooien",
        ],
        antwoord=0,
        uitleg="Teruggieten vervuilt de hele voorraad met wat er in je recipiënt zat. "
        "Daarom meet je ook zo precies mogelijk af, zodat er weinig overblijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Je werkt met levende organismen zo dat ze zo weinig mogelijk ongemak hebben.",
        antwoord=True,
        uitleg="Dat is zowel een ethische als een wetenschappelijke regel: een dier onder "
        "stress geeft ook andere resultaten. Waar het kan, wordt een alternatief gekozen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn duurzaam? Kruis alles aan wat juist is.",
        opties=[
            "afmeten wat je nodig hebt en niet meer",
            "glaswerk hergebruiken na schoonmaken",
            "elke proef met de dubbele hoeveelheid doen",
            "wegwerpmateriaal kiezen waar glas volstaat",
        ],
        antwoord=[0, 1],
        uitleg="Minder product betekent minder afval en minder risico. Wegwerpmateriaal "
        "houd je voor de gevallen waar steriliteit het vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom draag je handschoenen bij het werken met menselijk of dierlijk weefsel?",
        opties=[
            "om besmetting in twee richtingen te voorkomen",
            "om het weefsel warm te houden",
            "om de weegschaal niet vuil te maken",
            "om het weefsel beter vast te kunnen houden",
        ],
        antwoord=0,
        uitleg="Je beschermt jezelf tegen wat in het weefsel zit en het weefsel tegen de "
        "kiemen van je handen. Handschoenen vervangen het handen wassen niet.",
    ),
    dict(
        type="invultekst",
        vraag="Wat doe je als eerste bij een spat van een bijtend product in je oog?",
        antwoord=["spoelen", "uitspoelen", "oog spoelen"],
        uitleg="Minutenlang spoelen met veel water, met het oog open. Pas daarna wordt er "
        "hulp gehaald, en het etiket gaat mee naar de arts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling pipetteert met de mond om sneller te werken. Waarom is dat fout?",
        opties=[
            "het product kan in de mond terechtkomen",
            "de pipet wordt daardoor onnauwkeurig",
            "de vloeistof wordt daardoor te warm",
            "de pipet is daarvoor te lang",
        ],
        antwoord=0,
        uitleg="Eén verkeerde zuigbeweging volstaat. Daarom gebruik je altijd een "
        "pipetteerballon of een pipetteerhulp.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor je een proef start, kijk je na waar de nooddouche en de oogdouche hangen.",
        antwoord=True,
        uitleg="Bij een ongeval tellen seconden. Dan is er geen tijd om te zoeken waar iets "
        "hangt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat op een etiket ook hoe je het product bewaart?",
        opties=[
            "verkeerd bewaren maakt het gevaarlijker of onbruikbaar",
            "het bepaalt de prijs van het product",
            "het bepaalt hoe snel het product opgebruikt moet zijn",
            "het bepaalt in welk lokaal je werkt",
        ],
        antwoord=0,
        uitleg="Sommige stoffen ontleden in licht of warmte, andere reageren met elkaar. "
        "Daarom staan niet alle producten in dezelfde kast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep laat een microscooplamp de hele les branden zonder te kijken. Wat is daar fout aan?",
        opties=[
            "het verbruikt stroom en verkort de levensduur van de lamp",
            "het verandert de vergroting van het objectief dat je kiest",
            "het maakt het preparaat steriel",
            "het beschadigt de fijne stelschroef",
        ],
        antwoord=0,
        uitleg="Een toestel dat niet gebruikt wordt, gaat uit. Dat is de kern van duurzaam "
        "werken in een labo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je tijdens een proef meteen wat je doet en meet?",
        opties=[
            "achteraf is niet meer na te gaan wat er precies gebeurde",
            "het verhoogt de nauwkeurigheid van de balans",
            "het is nodig om het afval achteraf correct te sorteren",
            "het maakt het opruimen sneller",
        ],
        antwoord=0,
        uitleg="Wie uit het hoofd noteert, vult onbewust aan. Een verslag dat niemand kan "
        "nagaan, is wetenschappelijk waardeloos.",
    ),
]

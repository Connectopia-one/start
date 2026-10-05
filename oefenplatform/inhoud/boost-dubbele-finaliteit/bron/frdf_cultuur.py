# -*- coding: utf-8 -*-
"""De Franstalige wereld: omgangsvormen, gewoontes en sociale conventies.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. Bij "Lezen en
luisteren" staat er: je illustreert aspecten van maatschappijen en culturen
waarin Frans gesproken wordt. Op het examen krijg je teksten waarin
socioculturele aspecten belicht worden: het dagelijkse leven,
leefomstandigheden, gewoontes, sociale verhoudingen, waarden en normen,
lichaamstaal en sociale conventies. De fiche geeft er zelf twee voorbeelden
bij: je haalt uit een tekst wat de eetgewoonten zijn in Frankrijk, en je merkt
op dat in Franstalig België iedereen elkaar met een kus begroet, ook mannen.

Bij "Schrijven, spreken en interactie" komt hetzelfde terug langs de andere
kant: je legt alledaagse sociale contacten (begroeten, aanspreken, afscheid
nemen, bedanken, uitnodigen, je verontschuldigen), je past je taal aan de
ontvanger aan, je respecteert de beleefdheidsconventies en je gebruikt de
juiste toon. Daar hoort de keuze tussen tu en vous bij, en de conditionnel de
politesse.

Deel 1 gaat over begroeten, aanspreken en de omgangsvormen zelf. Deel 2 gaat
over het Frans als taal in België en in de wereld, en over wat je uit een tekst
over gewoontes kan halen.
"""

BOULANGERIE = (
    "Quand tu entres dans une boulangerie en France, tu dis « Bonjour » avant de demander ton "
    "pain. Si tu commences par « Je voudrais une baguette », la vendeuse te répondra peut-être "
    "« Bonjour » d'abord. Ce n'est pas de la mauvaise humeur : c'est l'ordre normal."
)
REPAS = (
    "Chez nous, le repas principal est le soir, vers 19 h 30 ou 20 h. On commence souvent par "
    "une entrée, puis le plat, et le fromage vient avant le dessert. Le pain reste sur la table "
    "pendant tout le repas, à côté de l'assiette."
)
TUTOYER = (
    "Au travail, j'appelle mes collègues par leur prénom et on se dit tu. Mais quand un client "
    "entre, je passe au vous, même s'il a mon âge. Et je recommence à dire vous à un collègue "
    "que je ne connais pas encore."
)

DEEL1 = [
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {BOULANGERIE} » Wat leer je hier over de omgangsvormen?",
         opties=["Je zegt eerst bonjour, en pas daarna waarvoor je komt.",
                 "Je mag in een bakkerij niets vragen zonder te wachten.",
                 "Verkopers in Frankrijk zijn vaak onvriendelijk.",
                 "Je moet in een winkel altijd tu gebruiken."],
         antwoord=0,
         uitleg="C'est l'ordre normal: dat is de gewone orde. Eerst de begroeting, dan de vraag."),
    dict(type="meerkeuze",
         vraag="Je spreekt in een Franse winkel een verkoper aan die je niet kent. Wat zeg je?",
         opties=["Bonjour, madame.",
                 "Salut, ça va ?",
                 "Coucou !",
                 "Bonjour, tu as du pain ?"],
         antwoord=0,
         uitleg="Salut en coucou zijn voor vrienden. Tegen iemand die je niet kent gebruik je bonjour en de vous-vorm."),
    dict(type="meerkeuze",
         vraag="Wanneer gebruik je in het Frans tu, en wanneer vous? Welke uitspraken zijn juist?",
         opties=["tu tegen een vriend of een klasgenoot",
                 "vous tegen een volwassene die je niet kent",
                 "vous tegen één persoon kan ook, uit hoffelijkheid",
                 "tu tegen een onbekende klant op je werk"],
         antwoord=[0, 1, 2],
         uitleg="Vous is zowel het meervoud als de hoffelijke vorm voor één persoon. Tegen een klant die je niet kent, blijf je bij vous."),
    dict(type="waarofniet",
         vraag="Als je in Frankrijk een politieagent of een verkoper aanspreekt, zeg je altijd eerst bonjour.",
         antwoord=True,
         uitleg="Dat hoort bij de beleefdheidsconventies: de begroeting komt voor de vraag."),
    dict(type="meerkeuze",
         vraag="Je schrijft een mail aan een werkgever die je niet kent en je wil vragen of je mag komen langskomen. Welke vorm is het meest gepast?",
         opties=["Pourriez-vous me dire quand je peux venir ?",
                 "Tu peux me dire quand je viens ?",
                 "Dis-moi quand je dois venir.",
                 "Je viens demain, d'accord ?"],
         antwoord=0,
         uitleg="Pourriez-vous is de conditionnel de politesse: zou u kunnen. Samen met de vous-vorm is dat de toon voor een onbekende volwassene."),
    dict(type="invultekst",
         vraag="Welke Franse aanspreking gebruik je in een mail aan een vrouw van wie je de naam niet kent? Schrijf het woord.",
         antwoord=["Madame", "madame"],
         uitleg="Madame, zonder naam, aan het begin van de mail. Ken je de naam wel, dan schrijf je Madame Dupont."),
    dict(type="waarofniet",
         vraag="In Franstalig België begroeten ook mannen elkaar met een kus.",
         antwoord=True,
         uitleg="La bise hoort er bij vrienden en familie bij, ook tussen mannen. Dat verrast wie het niet gewoon is."),
    dict(type="meerkeuze",
         vraag="Je komt een Franstalige vriend tegen op straat. Welke begroetingen passen?",
         opties=["Salut !",
                 "Coucou, ça va ?",
                 "Bonjour, monsieur.",
                 "Bonsoir, madame."],
         antwoord=[0, 1],
         uitleg="Salut en coucou zijn informeel en dus voor vrienden. Monsieur en madame maken het juist formeel."),
    dict(type="meerkeuze",
         vraag="Hoe neem je in het Frans afscheid van iemand die je morgen opnieuw ziet?",
         opties=["À demain !", "Bonjour !", "Enchanté !", "S'il vous plaît."],
         antwoord=0,
         uitleg="À demain betekent tot morgen. Enchanté zeg je bij een eerste kennismaking."),
    dict(type="invultekst",
         vraag="Welk Frans woord zeg je om je te verontschuldigen als je per ongeluk tegen iemand botst? Schrijf één woord.",
         antwoord=["pardon", "Pardon"],
         uitleg="Pardon, of Excusez-moi als je het wat uitgebreider wil zeggen."),
    dict(type="meerkeuze",
         vraag="Iemand zegt tegen jou « Je suis désolé, je suis en retard. » Wat antwoord je?",
         opties=["Ce n'est pas grave.",
                 "Merci beaucoup.",
                 "Avec plaisir.",
                 "Bon appétit."],
         antwoord=0,
         uitleg="Ce n'est pas grave betekent het is niet erg. Reageren op een verontschuldiging hoort bij de alledaagse sociale contacten."),
    dict(type="waarofniet",
         vraag="Je gebruikt dezelfde toon in een mail aan een leraar als in een bericht aan je beste vriend.",
         antwoord=False,
         uitleg="Je past je taal aan de ontvanger aan. Aan een leraar schrijf je vous en een gepaste groet, aan een vriend tu en salut."),
    dict(type="meerkeuze",
         vraag="Je wil iemand in het Frans uitnodigen om zaterdag te komen eten. Welke zin past?",
         opties=["Tu viens manger chez moi samedi ?",
                 "Je mange chez toi samedi.",
                 "Tu as mangé samedi ?",
                 "Je voudrais manger samedi."],
         antwoord=0,
         uitleg="Een uitnodiging is een vraag aan de ander. De andere zinnen vertellen iets over jezelf of vragen naar het verleden."),
    dict(type="waarofniet",
         vraag="Lichaamstaal hoort bij de dingen die je in een gesprek in het Frans in het oog moet houden.",
         antwoord=True,
         uitleg="Je gebruikt zelf lichaamstaal om je boodschap over te brengen, en je schat die van je gesprekspartner in om er goed op te reageren."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {TUTOYER} » Wanneer gaat deze persoon over naar vous?",
         opties=["bij een klant, en bij een collega die hij nog niet kent",
                 "alleen bij een klant",
                 "bij elke collega, ook bij wie hij goed kent",
                 "alleen bij iemand die ouder is dan hij"],
         antwoord=0,
         uitleg="Je passe au vous quand un client entre, en je recommence à dire vous à un collègue que je ne connais pas encore. De leeftijd speelt er juist geen rol: même s'il a mon âge."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje over het werk hangt de keuze tussen tu en vous af van de leeftijd van de andere persoon.",
         antwoord=False,
         uitleg="Même s'il a mon âge: zelfs als hij mijn leeftijd heeft, blijft het vous. Wat telt, is de verhouding, niet de leeftijd."),
    dict(type="meerkeuze",
         vraag="Welk Frans woord of welke uitdrukking zeg je vóór het eten?",
         opties=["Bon appétit !", "Bonne nuit !", "À tes souhaits !", "Bonne route !"],
         antwoord=0,
         uitleg="Bon appétit zeg je aan tafel. Bonne nuit is welterusten, bonne route is goede reis."),
    dict(type="invultekst",
         vraag="Met welk Frans woord bedank je iemand? Schrijf één woord.",
         antwoord=["merci", "Merci"],
         uitleg="Merci, of merci beaucoup als je het wat warmer wil zeggen."),
    dict(type="meerkeuze",
         vraag="Je sluit een formele mail in het Frans af. Welke twee slotformules passen?",
         opties=["Cordialement,",
                 "Je vous remercie d'avance.",
                 "Bisous !",
                 "À plus !"],
         antwoord=[0, 1],
         uitleg="Cordialement en je vous remercie d'avance horen bij een formele mail. Bisous en à plus zijn voor vrienden."),
    dict(type="waarofniet",
         vraag="Tegen iemand die je met vous aanspreekt, zeg je s'il te plaît.",
         antwoord=False,
         uitleg="Dan wordt het s'il vous plaît. Allebei betekenen ze alstublieft of alsjeblieft, maar je kiest de vorm die past bij hoe je de persoon aanspreekt."),
]

BELGIQUE = (
    "En Belgique, trois langues sont officielles : le néerlandais, le français et l'allemand. "
    "Le français est la langue de la Wallonie et, avec le néerlandais, de Bruxelles. Un Belge "
    "francophone dit septante et nonante, là où un Français dit soixante-dix et quatre-vingt-dix."
)
FRANCO = (
    "Le français n'est pas parlé qu'en France. On le parle aussi en Belgique, en Suisse, au "
    "Luxembourg, au Québec et dans de nombreux pays d'Afrique. Les mots et l'accent ne sont pas "
    "partout les mêmes, mais on se comprend."
)
FETE = (
    "Le 21 juillet, la Belgique fête sa fête nationale : il y a un défilé à Bruxelles et les "
    "écoles sont fermées, mais c'est les vacances. En France, la fête nationale est le 14 "
    "juillet, avec des feux d'artifice le soir du 13 ou du 14."
)
MARCHE_FR = (
    "Dans beaucoup de villes françaises, les magasins ferment entre midi et deux heures, surtout "
    "dans les petites rues. Le dimanche, seule la boulangerie est ouverte, et souvent le matin "
    "seulement."
)

DEEL2 = [
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {BELGIQUE} » Welke uitspraken over het Frans in België zijn juist?",
         opties=["Frans is een van de drie officiële talen van België.",
                 "Frans is de taal van Wallonië.",
                 "In Brussel zijn Frans en Nederlands samen officieel.",
                 "Frans is de enige officiële taal van België."],
         antwoord=[0, 1, 2],
         uitleg="Trois langues sont officielles: Nederlands, Frans en Duits. De laatste keuze spreekt dat tegen."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje over België. Welk Frans woord gebruikt een Belg voor negentig, waar een Fransman quatre-vingt-dix zegt? Schrijf het woord.",
         antwoord=["nonante"],
         uitleg="Septante is zeventig en nonante is negentig. Dat hoor je in België en in een deel van Zwitserland."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje spreken Belgen en Fransen een verschillende taal.",
         antwoord=False,
         uitleg="Het is dezelfde taal, met een paar andere woorden. Een taal kan van streek tot streek verschillen zonder een andere taal te worden."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {FRANCO} » Wat is de hoofdgedachte?",
         opties=["Frans wordt in veel landen gesproken, met verschillen maar zonder begripsproblemen.",
                 "Frans is alleen in Frankrijk de echte taal.",
                 "Wie Frans leert, moet het accent van Parijs leren.",
                 "In Afrika spreekt men een andere taal dan het Frans."],
         antwoord=0,
         uitleg="Les mots et l'accent ne sont pas partout les mêmes, mais on se comprend. Dat is waar de tekst naartoe werkt."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Welke plaatsen noemt het waar Frans gesproken wordt?",
         opties=["Zwitserland",
                 "Luxemburg",
                 "Québec",
                 "Portugal"],
         antwoord=[0, 1, 2],
         uitleg="La Suisse, le Luxembourg, le Québec. Portugal staat er niet bij."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje klinkt het Frans overal in de wereld precies hetzelfde.",
         antwoord=False,
         uitleg="Les mots et l'accent ne sont pas partout les mêmes: de woorden en het accent zijn niet overal gelijk."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {FETE} » Op welke datum is de nationale feestdag van Frankrijk?",
         opties=["14 juli", "21 juli", "13 juli", "1 juli"],
         antwoord=0,
         uitleg="En France, la fête nationale est le 14 juillet. In België is het 21 juli."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje. Op welke dag van juli viert België zijn nationale feestdag? Schrijf alleen het getal.",
         antwoord=["21"],
         uitleg="Le 21 juillet, la Belgique fête sa fête nationale."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje vallen de twee nationale feestdagen in dezelfde maand.",
         antwoord=True,
         uitleg="De 14de en de 21ste juillet, allebei in juli."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {MARCHE_FR} » Je bent op een zondagnamiddag in een Frans dorp en je wil brood. Wat mag je verwachten?",
         opties=["De bakker is waarschijnlijk al gesloten.",
                 "Alle winkels zijn open tot de avond.",
                 "De bakker is zeker open tot zes uur.",
                 "Je kan alleen op zondagnamiddag brood kopen."],
         antwoord=0,
         uitleg="Le dimanche, seule la boulangerie est ouverte, et souvent le matin seulement. Souvent le matin seulement: vaak alleen 's ochtends."),
    dict(type="waarofniet",
         vraag="Volgens datzelfde tekstje blijven kleine Franse winkels over de middag vaak twee uur toe.",
         antwoord=True,
         uitleg="Les magasins ferment entre midi et deux heures, surtout dans les petites rues."),
    dict(type="meerkeuze",
         vraag="Op het examen kunnen in een tekst socioculturele aspecten belicht worden. Welke horen daarbij?",
         opties=["gewoontes",
                 "waarden en normen",
                 "sociale verhoudingen",
                 "de spelling van werkwoorden"],
         antwoord=[0, 1, 2],
         uitleg="Zeven dingen horen erbij: het dagelijkse leven, leefomstandigheden, gewoontes, sociale verhoudingen, waarden en normen, lichaamstaal en sociale conventies. Spelling hoort bij de grammatica, niet hierbij."),
    dict(type="meerkeuze",
         vraag="Je leest een Franse tekst over hoe men in Frankrijk aan tafel gaat. Welk socioculturele aspect is dat?",
         opties=["gewoontes uit het dagelijkse leven",
                 "lichaamstaal",
                 "sociale verhoudingen",
                 "waarden en normen"],
         antwoord=0,
         uitleg="Eetgewoonten horen bij het dagelijkse leven en bij de gewoontes."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {REPAS} » Wat komt er volgens de tekst vóór het dessert?",
         opties=["de kaas", "de voorgerechten", "het brood", "de soep"],
         antwoord=0,
         uitleg="Le fromage vient avant le dessert. Dat is een gewoonte die in België en Nederland minder vast ligt."),
    dict(type="waarofniet",
         vraag="Volgens datzelfde tekstje over de maaltijd is het middagmaal de hoofdmaaltijd.",
         antwoord=False,
         uitleg="Le repas principal est le soir, vers 19 h 30 ou 20 h: de hoofdmaaltijd is 's avonds, rond half acht of acht uur."),
    dict(type="invultekst",
         vraag="Nog dat tekstje over de maaltijd. Welk Frans woord betekent 'bord'? Schrijf het woord.",
         antwoord=["assiette"],
         uitleg="À côté de l'assiette: naast het bord. Het is une assiette, vrouwelijk."),
    dict(type="meerkeuze",
         vraag="Waarom hoort cultuur en omgangsvormen bij een taalexamen?",
         opties=["Omdat je een taal gebruikt om met mensen om te gaan, en dan moet je hun gewoontes kennen.",
                 "Omdat de examencommissie een cultuurexamen afneemt.",
                 "Omdat je anders de grammatica niet kan leren.",
                 "Omdat het Frans in België moeilijker is dan in Frankrijk."],
         antwoord=0,
         uitleg="Je leert de cultuur van je Franstalige gesprekspartner beter kennen, en daardoor verloopt de communicatie vlotter."),
    dict(type="waarofniet",
         vraag="Wie in het Frans de verkeerde toon kiest, kan onbedoeld onvriendelijk klinken, ook als elk woord juist gespeld is.",
         antwoord=True,
         uitleg="Register en beleefdheidsconventies zijn een eigen beoordelingsrij op het examen, naast woordenschat en grammatica."),
    dict(type="invultekst",
         vraag="Hoe heet de kus op de wang waarmee Franstaligen elkaar begroeten? Schrijf het Franse woord.",
         antwoord=["bise", "la bise"],
         uitleg="Faire la bise. In Franstalig België doen ook mannen dat onder elkaar."),
    dict(type="meerkeuze",
         vraag="Je krijgt op het examen een tekst over het leven van een jongere in Senegal. Wat verwacht de opdracht van jou?",
         opties=["Dat je eruit haalt wat die tekst over het dagelijkse leven daar zegt.",
                 "Dat je de aardrijkskunde van Senegal kent.",
                 "Dat je de geschiedenis van het land kan vertellen.",
                 "Dat je de tekst in het Nederlands vertaalt."],
         antwoord=0,
         uitleg="Je illustreert aspecten van maatschappijen en culturen waarin Frans gesproken wordt, aan de hand van wat er in de tekst staat."),
]

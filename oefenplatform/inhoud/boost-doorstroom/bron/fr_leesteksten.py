# -*- coding: utf-8 -*-
"""Begrijpend lezen: langere Franse teksten.

Toegevoegd op 27 november 2026, na de enquête van een tester die zelf Frans
geeft: er waren te weinig leesopdrachten. De vragen in "Een Franse tekst
analyseren" staan elk op een tekstje van een paar zinnen. Het examen Frans 1
(lezen en luisteren, 120 minuten, niveau B1) legt je langere teksten voor,
waarin je verbanden moet leggen tussen alinea's en moet afleiden wat er niet
letterlijk staat.

Daarom krijgt elk hoofdstuk hier één langere tekst, die bovenaan blijft staan
terwijl je de twintig vragen maakt (de leestekst van het hoofdstuk, zoals bij
begrijpend lezen in Start en Spark). Woorden tussen sterretjes komen in de
woordenlijst: daar tik je op voor de vertaling. De vragen gaan nooit over de
betekenis van een woord uit die lijst.

Wat er gevraagd wordt, volgt de onderdelen van het lezen voor Frans 1:
onderwerp, hoofdgedachte en hoofdpunten, gegevens opzoeken, verwijswoorden en
signaalwoorden, het verband tussen delen van een tekst, de tekstsoort, de
bedoeling van de schrijver, twee teksten vergelijken, en bij een verhaal de
personages, de volgorde en wat je moet afleiden.

Deel 1: een informatief krantenartikel en een lezersbrief over hetzelfde
onderwerp (informatief en opiniërend).
Deel 2: een kort verhaal (narratief en literair).

De teksten zijn zelf geschreven; de personen en de krant zijn verzonnen.
"""

TITEL1 = "Ne jetez pas, réparez !"

TEKST1 = """
Texte A — un article

Le premier samedi du mois, la salle des fêtes de Marche-en-Famenne ressemble à
un grand atelier. Sur de longues tables, on voit des *grille-pain*, des lampes,
des vélos d'enfant et même une machine à café qui ne fait plus de café.
Bienvenue au Repair Café, où des *bénévoles* aident les habitants à réparer
leurs objets cassés, gratuitement.

L'idée est née aux Pays-Bas en 2009. Aujourd'hui, il existe des Repair Cafés
dans des dizaines de pays, et la Belgique en compte plus d'une centaine.

« Nous ne sommes pas un magasin », explique Marc Dufour, 67 ans, ancien
électricien et bénévole depuis quatre ans. « Le visiteur reste à côté de nous
pendant la réparation. Il regarde, il pose des questions, et souvent, il
apprend à le faire lui-même la fois suivante. »

Les chiffres de l'année passée montrent que le système fonctionne : sur 412
objets apportés, 287 ont été réparés. Pour les autres, il manquait souvent une
*pièce*, ou bien la réparation était trop dangereuse. « Un appareil qui
chauffe, comme un sèche-cheveux, on l'ouvre avec beaucoup de prudence »,
précise Marc.

Pourtant, l'organisation a un problème : les bénévoles *vieillissent*. La
plupart ont plus de soixante ans, et peu de jeunes viennent les rejoindre.
C'est pourquoi le Repair Café a contacté l'école secondaire de la ville. Depuis
janvier, six élèves de quatrième viennent chaque mois. Ils réparent surtout des
téléphones et des ordinateurs, des objets que les bénévoles plus âgés
connaissent moins bien.

Texte B — le courrier des lecteurs

Bravo pour votre article sur le Repair Café. J'y suis allée le mois dernier
avec ma vieille *machine à coudre*, et je suis repartie avec une machine qui
marche… et avec un nouvel ami ! Je ne suis cependant pas d'accord avec la
dernière phrase de votre article, qui présente les jeunes comme les seuls qui
connaissent la technologie. Ma voisine a 72 ans et elle répare des ordinateurs
depuis trente ans.

Le vrai problème, à mon avis, ce n'est pas l'âge : c'est que trop peu de gens
savent que ces ateliers existent. Il faudrait que la commune en parle
*davantage*, par exemple dans son bulletin mensuel.

Nadia, Marche-en-Famenne
"""

WOORDEN1 = [
    ("grille-pain", "een broodrooster"),
    ("bénévoles", "vrijwilligers, mensen die helpen zonder ervoor betaald te worden"),
    ("pièce", "hier: een onderdeel van een toestel"),
    ("vieillissent", "worden ouder, van het werkwoord vieillir"),
    ("machine à coudre", "een naaimachine"),
    ("davantage", "meer, vaker"),
]

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Waarover gaat tekst A?",
         opties=[
             "over een plek waar mensen samen kapotte spullen herstellen",
             "over een winkel die tweedehandstoestellen verkoopt",
             "over een school die leerlingen een technisch beroep laat leren",
             "over de geschiedenis van de elektriciteit in België",
         ],
         antwoord=0,
         uitleg="Het onderwerp zeg je in enkele woorden. De eerste alinea zegt het al: in het Repair Café helpen vrijwilligers de inwoners hun kapotte voorwerpen te herstellen."),
    dict(type="meerkeuze",
         vraag="Wat is de hoofdgedachte van tekst A?",
         opties=[
             "Het Repair Café werkt goed, maar heeft jonge vrijwilligers nodig.",
             "Wie een kapot toestel heeft, gooit het beter meteen weg en koopt een nieuw.",
             "Alleen oudere mensen kunnen nog een toestel herstellen.",
             "Het Repair Café is in 2009 in Marche-en-Famenne zelf begonnen.",
         ],
         antwoord=0,
         uitleg="De hoofdgedachte is de boodschap van de hele tekst in één zin. Het artikel toont met cijfers dat het systeem werkt (le système fonctionne) en zegt daarna dat er te weinig jonge vrijwilligers zijn."),
    dict(type="invultekst",
         vraag="Hoeveel voorwerpen werden vorig jaar hersteld? Schrijf het getal in cijfers.",
         antwoord=["287"],
         uitleg="Sur 412 objets apportés, 287 ont été réparés: van de 412 binnengebrachte voorwerpen werden er 287 hersteld."),
    dict(type="meerkeuze",
         vraag="In welk land ontstond het idee van het Repair Café?",
         opties=["in Nederland", "in België", "in Frankrijk", "in Luxemburg"],
         antwoord=0,
         uitleg="L'idée est née aux Pays-Bas: les Pays-Bas is Nederland."),
    dict(type="waarofniet",
         vraag="In het Repair Café betaal je een kleine prijs voor elke herstelling.",
         antwoord=False,
         uitleg="De eerste alinea eindigt met gratuitement: de herstelling is gratis."),
    dict(type="meerkeuze",
         vraag="Wat bedoelt Marc met 'Nous ne sommes pas un magasin'?",
         opties=[
             "De bezoeker kijkt mee en leert zelf iets bij.",
             "Ze verkopen geen nieuwe toestellen, alleen oude.",
             "Het café is enkel op zaterdag open.",
             "Je kan er niets te drinken kopen.",
         ],
         antwoord=0,
         uitleg="Hij legt het zelf uit in de zinnen die volgen: de bezoeker blijft ernaast, kijkt, stelt vragen en kan het de volgende keer vaak zelf."),
    dict(type="meerkeuze",
         vraag="Waarom lukt een herstelling soms niet, volgens tekst A?",
         opties=[
             "er ontbreekt een onderdeel",
             "de herstelling is te gevaarlijk",
             "de bezoeker heeft geen tijd om te wachten",
             "de vrijwilligers kennen het merk van het toestel niet",
         ],
         antwoord=[0, 1],
         uitleg="Il manquait souvent une pièce, ou bien la réparation était trop dangereuse: twee redenen, verbonden door ou bien, of ook."),
    dict(type="meerkeuze",
         vraag="'On l'ouvre avec beaucoup de prudence.' Waarnaar verwijst l' in die zin?",
         opties=[
             "naar een toestel dat warm wordt, zoals een haardroger",
             "naar de grote zaal waar het Repair Café elke maand plaatsvindt",
             "naar de deur van het atelier",
             "naar de doos met gereedschap van Marc",
         ],
         antwoord=0,
         uitleg="Een verwijswoord verwijst terug naar iets van daarvoor. Vlak ervoor staat un appareil qui chauffe, comme un sèche-cheveux: een toestel dat warm wordt, zoals een haardroger."),
    dict(type="meerkeuze",
         vraag="Wat betekent 'Pourtant' aan het begin van de alinea over het probleem?",
         opties=["toch", "daarom", "bovendien", "bijvoorbeeld"],
         antwoord=0,
         uitleg="Pourtant kondigt een tegenstelling aan: het systeem werkt, en toch is er een probleem."),
    dict(type="meerkeuze",
         vraag="'Les bénévoles vieillissent … C'est pourquoi le Repair Café a contacté l'école.' Welk verband leggen de woorden 'C'est pourquoi'?",
         opties=[
             "oorzaak en gevolg",
             "een tegenstelling tussen twee feiten",
             "een opsomming van gelijke dingen",
             "een voorbeeld bij een regel",
         ],
         antwoord=0,
         uitleg="C'est pourquoi betekent daarom. De vrijwilligers worden ouder (de oorzaak), dus vraagt het Repair Café hulp aan de school (het gevolg)."),
    dict(type="waarofniet",
         vraag="De leerlingen herstellen vooral toestellen die de oudere vrijwilligers minder goed kennen.",
         antwoord=True,
         uitleg="Ils réparent surtout des téléphones et des ordinateurs, des objets que les bénévoles plus âgés connaissent moins bien."),
    dict(type="invultekst",
         vraag="Hoeveel leerlingen komen elke maand helpen? Eén getal.",
         antwoord=["6", "zes", "six"],
         uitleg="Depuis janvier, six élèves de quatrième viennent chaque mois: zes leerlingen van het vierde jaar."),
    dict(type="meerkeuze",
         vraag="Wat voor soort tekst is tekst B?",
         opties=["een lezersbrief", "een nieuwsartikel", "een gebruiksaanwijzing", "een verhaal"],
         antwoord=0,
         uitleg="Le courrier des lecteurs is de rubriek met brieven van lezers. Nadia reageert op het artikel en ondertekent met haar naam."),
    dict(type="meerkeuze",
         vraag="Wat bracht Nadia mee naar het Repair Café?",
         opties=["een oude naaimachine", "een computer van haar buurvrouw", "een broodrooster", "een kinderfiets"],
         antwoord=0,
         uitleg="J'y suis allée le mois dernier avec ma vieille machine à coudre."),
    dict(type="meerkeuze",
         vraag="Waarmee is Nadia het niet eens?",
         opties=[
             "dat alleen jongeren iets van technologie zouden kennen",
             "dat het Repair Café zijn herstellingen helemaal gratis doet",
             "dat de vrijwilligers vriendelijk zijn",
             "dat er te weinig tafels in de zaal staan",
         ],
         antwoord=0,
         uitleg="Je ne suis cependant pas d'accord avec la dernière phrase: die zin stelt de jongeren voor als de enigen die de technologie kennen. Haar buurvrouw van 72 bewijst het tegendeel."),
    dict(type="meerkeuze",
         vraag="Wat is volgens Nadia het echte probleem?",
         opties=[
             "Te weinig mensen weten dat de ateliers bestaan.",
             "De vrijwilligers worden te oud om nog veilig te herstellen.",
             "Er zijn te weinig onderdelen.",
             "De gemeente geeft geen geld.",
         ],
         antwoord=0,
         uitleg="Le vrai problème, ce n'est pas l'âge : c'est que trop peu de gens savent que ces ateliers existent. Ze spreekt het artikel dus tegen: niet de leeftijd is het probleem."),
    dict(type="meerkeuze",
         vraag="Wat stelt Nadia voor?",
         opties=[
             "dat de gemeente er meer over vertelt",
             "dat de school meer leerlingen stuurt",
             "dat het Repair Café elke week opengaat",
             "dat bezoekers voortaan een kleine bijdrage betalen",
         ],
         antwoord=0,
         uitleg="Il faudrait que la commune en parle davantage, par exemple dans son bulletin mensuel: in het maandblad van de gemeente."),
    dict(type="waarofniet",
         vraag="Tekst A en tekst B gaan over hetzelfde onderwerp, maar in tekst B geeft de schrijfster ook haar mening.",
         antwoord=True,
         uitleg="Allebei gaan ze over het Repair Café. Tekst A brengt vooral feiten en cijfers; tekst B zegt à mon avis en je ne suis pas d'accord: dat is een opiniërende tekst."),
    dict(type="waarofniet",
         vraag="De buurvrouw van Nadia is een van de leerlingen die in het Repair Café helpen.",
         antwoord=False,
         uitleg="Ma voisine a 72 ans: de buurvrouw is 72 jaar en dus geen leerling van het vierde jaar."),
    dict(type="meerkeuze",
         vraag="Waarover hebben allebei de teksten het?",
         opties=[
             "het Repair Café in Marche-en-Famenne",
             "jongeren en technologie",
             "de cijfers van vorig jaar",
             "het land waar het idee begon",
         ],
         antwoord=[0, 1],
         uitleg="De cijfers en het begin in Nederland staan alleen in tekst A. Het Repair Café zelf en de vraag wie de technologie kent, komen in allebei terug."),
]

TITEL2 = "Le dernier bus"

TEKST2 = """
Le dernier bus

Il était presque dix heures du soir quand Lucas est sorti de la salle de sport.
Il pleuvait, et la rue était vide. Il a regardé sa montre et il a commencé à
courir : le dernier bus pour son village passait à 21 h 52.

Quand il est arrivé à l'arrêt, le bus était déjà parti. Lucas a vu ses feux
rouges disparaître au bout de la rue. Il a sorti son téléphone pour appeler sa
mère, mais l'écran est resté noir. La batterie était vide.

« Génial », a-t-il dit à voix haute, et il s'est assis sous l'*abri*. Il avait
froid, il avait faim, et il commençait à avoir un peu peur. Son village était
à douze kilomètres. À pied, il lui faudrait presque trois heures.

Une petite voiture s'est arrêtée devant l'abri. Une vieille dame a baissé la
vitre.

« Tu as *raté* le bus, toi aussi ? Ça m'arrivait tout le temps quand j'avais
ton âge. »

Lucas a hésité. Sa mère lui répétait toujours qu'il ne fallait jamais monter
dans la voiture d'un inconnu.

« Je ne veux pas vous déranger, madame. Est-ce que je pourrais seulement
utiliser votre téléphone ? »

La dame a souri et lui a tendu un vieux *téléphone à clapet*. « Bien sûr. Il
est plus vieux que toi, mais il marche. »

Sa mère a répondu tout de suite. Elle n'était pas fâchée ; elle était surtout
*soulagée*. « Reste où tu es, j'arrive dans vingt minutes. »

La dame n'est pas repartie. Elle a attendu dans sa voiture, le moteur allumé,
jusqu'à ce que la voiture de la mère de Lucas apparaisse au coin de la rue.
Puis elle a fait un petit signe de la main et elle est partie.

Dans la voiture, Lucas a raconté toute l'histoire. Sa mère a écouté sans rien
dire. À la fin, elle a seulement demandé : « Et tu sais comment elle
s'appelle ? »

Lucas a *secoué la tête*. Il ne lui avait même pas demandé son nom. Ce soir-là,
avant de s'endormir, il s'est promis une chose : la prochaine fois que
quelqu'un aurait besoin d'aide, ce serait lui qui s'arrêterait.
"""

WOORDEN2 = [
    ("abri", "het bushokje, de schuilplaats aan de halte"),
    ("raté", "gemist, van het werkwoord rater"),
    ("téléphone à clapet", "een klaptelefoon, een oud gsm-model dat je openklapt"),
    ("soulagée", "opgelucht, omdat iets toch goed afloopt"),
    ("secoué la tête", "het hoofd geschud, om nee te zeggen"),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Waarom begint Lucas te lopen?",
         opties=[
             "Hij wil de laatste bus nog halen.",
             "Het begint plots hard te regenen.",
             "Hij is te laat voor zijn sportles.",
             "Hij ziet zijn moeder aan de overkant.",
         ],
         antwoord=0,
         uitleg="Hij kijkt op zijn horloge en begint te lopen, want le dernier bus passait à 21 h 52. Het regende al toen hij buitenkwam."),
    dict(type="invultekst",
         vraag="Om hoe laat vertrok de laatste bus naar het dorp van Lucas? Schrijf het uur zoals in de tekst.",
         antwoord=["21 h 52", "21h52", "21:52", "21.52"],
         uitleg="Le dernier bus pour son village passait à 21 h 52. In het Frans schrijf je het uur vaak met een h tussen de uren en de minuten."),
    dict(type="meerkeuze",
         vraag="Hoe voelt Lucas zich terwijl hij aan de halte zit?",
         opties=[
             "hij heeft het koud",
             "hij heeft honger",
             "hij is een beetje bang",
             "hij is boos op zijn moeder",
         ],
         antwoord=[0, 1, 2],
         uitleg="Il avait froid, il avait faim, et il commençait à avoir un peu peur. Over boosheid op zijn moeder staat er niets."),
    dict(type="meerkeuze",
         vraag="Waarom kan Lucas zijn moeder niet met zijn eigen telefoon bellen?",
         opties=[
             "De batterij is leeg.",
             "Hij kent haar nummer niet vanbuiten.",
             "Er is geen bereik in de straat.",
             "Zijn telefoon ligt nog in de sporthal.",
         ],
         antwoord=0,
         uitleg="L'écran est resté noir. La batterie était vide: het scherm bleef zwart, de batterij was leeg."),
    dict(type="waarofniet",
         vraag="Het dorp van Lucas ligt zo dichtbij dat hij er in een half uur te voet is.",
         antwoord=False,
         uitleg="Son village était à douze kilomètres. À pied, il lui faudrait presque trois heures: bijna drie uur stappen."),
    dict(type="meerkeuze",
         vraag="Lucas zegt 'Génial' als hij alleen aan de halte staat. Wat bedoelt hij?",
         opties=[
             "Hij meent het omgekeerde: het is een ramp.",
             "Hij is blij dat hij nu rustig in de regen kan wachten.",
             "Hij vindt de straat mooi in de regen.",
             "Hij heeft net een goed idee gekregen.",
         ],
         antwoord=0,
         uitleg="Hij heeft de bus gemist en zijn telefoon is leeg. Génial (geweldig) is hier ironisch: hij zegt het omgekeerde van wat hij denkt."),
    dict(type="meerkeuze",
         vraag="'Tu as raté le bus, toi aussi ?' Wat bedoelt de dame met 'toi aussi'?",
         opties=[
             "Zij heeft vroeger zelf vaak de bus gemist.",
             "Zij heeft vanavond net zoals Lucas de laatste bus gemist.",
             "Lucas lijkt op haar kleinzoon.",
             "Zij woont ook in het dorp van Lucas.",
         ],
         antwoord=0,
         uitleg="Ze zegt erna: ça m'arrivait tout le temps quand j'avais ton âge. De imparfait arrivait toont een gewoonte van vroeger, toen ze zo oud was als hij."),
    dict(type="meerkeuze",
         vraag="Waarom stapt Lucas niet in de auto van de dame?",
         opties=[
             "Zijn moeder heeft hem geleerd niet bij onbekenden in te stappen.",
             "Hij wil liever de hele weg naar zijn dorp in de regen te voet gaan.",
             "De auto van de dame is te klein.",
             "De dame vraagt het hem niet.",
         ],
         antwoord=0,
         uitleg="Sa mère lui répétait toujours qu'il ne fallait jamais monter dans la voiture d'un inconnu: nooit instappen bij iemand die je niet kent."),
    dict(type="meerkeuze",
         vraag="Wat vraagt Lucas aan de dame?",
         opties=[
             "of hij even haar telefoon mag gebruiken",
             "of ze hem tot aan de deur van zijn huis wil brengen",
             "hoe laat de volgende bus komt",
             "of ze zijn moeder kent",
         ],
         antwoord=0,
         uitleg="Est-ce que je pourrais seulement utiliser votre téléphone ? Met je pourrais, een conditionnel, vraagt hij het beleefd."),
    dict(type="waarofniet",
         vraag="Volgens de dame is haar telefoon ouder dan Lucas.",
         antwoord=True,
         uitleg="Il est plus vieux que toi, mais il marche: hij is ouder dan jij, maar hij werkt."),
    dict(type="meerkeuze",
         vraag="Hoe reageert de moeder van Lucas aan de telefoon?",
         opties=[
             "Ze is niet boos, ze komt hem halen.",
             "Ze is erg boos en zegt dat hij moet stappen.",
             "Ze neemt niet op.",
             "Ze vraagt hem de bus van morgen te nemen.",
         ],
         antwoord=0,
         uitleg="Elle n'était pas fâchée: ze was niet boos. Ze zegt dat ze er binnen twintig minuten is."),
    dict(type="meerkeuze",
         vraag="Wat betekent 'Reste où tu es' in de tekst?",
         opties=[
             "Blijf waar je bent.",
             "Kom naar huis.",
             "Bel me later terug.",
             "Ga terug naar de sporthal.",
         ],
         antwoord=0,
         uitleg="Reste is de impératif van rester, blijven. Où tu es is waar je bent."),
    dict(type="waarofniet",
         vraag="De dame rijdt weg zodra Lucas zijn moeder gebeld heeft.",
         antwoord=False,
         uitleg="La dame n'est pas repartie. Elle a attendu ... jusqu'à ce que la voiture de la mère de Lucas apparaisse: ze wacht tot de moeder er is."),
    dict(type="meerkeuze",
         vraag="Waarom wacht de dame tot de moeder er is? De tekst zegt het niet letterlijk. Wat kan je eruit afleiden?",
         opties=[
             "Ze wil zeker zijn dat Lucas niet alleen in het donker blijft.",
             "Ze wil de moeder van Lucas eens goed de les spellen over dat late uur.",
             "Haar auto wil niet meer starten.",
             "Ze wacht tot Lucas haar telefoon teruggeeft.",
         ],
         antwoord=0,
         uitleg="Ze laat de motor draaien, wacht, zwaait en rijdt weg zonder iets te zeggen. Ze wil de moeder niet spreken: ze blijft gewoon tot Lucas veilig is."),
    dict(type="meerkeuze",
         vraag="Wie vertelt dit verhaal?",
         opties=[
             "een verteller die over Lucas vertelt",
             "Lucas zelf, die alles in de ik-vorm vertelt",
             "de oude dame",
             "de moeder van Lucas",
         ],
         antwoord=0,
         uitleg="Er staat il en Lucas, nooit je voor Lucas. Het is een verteller die van buitenaf over Lucas vertelt en ook weet wat hij denkt."),
    dict(type="meerkeuze",
         vraag="Wat voor soort tekst is 'Le dernier bus'?",
         opties=["een verhaal", "een betoog", "een nieuwsbericht", "een gebruiksaanwijzing"],
         antwoord=0,
         uitleg="Er zijn personages, een plaats, een tijd en gebeurtenissen die elkaar opvolgen: dat is een verhalende of narratieve tekst."),
    dict(type="waarofniet",
         vraag="Aan het einde weet Lucas niet hoe de dame heet.",
         antwoord=True,
         uitleg="Il ne lui avait même pas demandé son nom: hij had haar zelfs haar naam niet gevraagd."),
    dict(type="meerkeuze",
         vraag="Wat neemt Lucas zich op het einde voor?",
         opties=[
             "zelf stoppen als iemand anders hulp nodig heeft",
             "altijd een opgeladen telefoon bij zich hebben",
             "nooit meer zo laat naar de sporthal gaan",
             "de dame opzoeken om haar te bedanken",
         ],
         antwoord=0,
         uitleg="La prochaine fois que quelqu'un aurait besoin d'aide, ce serait lui qui s'arrêterait: de volgende keer zou hij zelf degene zijn die stopt."),
    dict(type="meerkeuze",
         vraag="Welke zinnen passen bij de boodschap van het verhaal?",
         opties=[
             "Een kleine daad van een vreemde kan veel betekenen.",
             "Wie geholpen wordt, kan later zelf iemand helpen.",
             "Met onbekenden praat je nooit, ook niet als je in nood zit.",
             "Een oude klaptelefoon is altijd beter dan een nieuwe smartphone.",
         ],
         antwoord=[0, 1],
         uitleg="Een onbekende dame helpt Lucas zonder er iets voor terug te vragen, en daardoor besluit hij om zelf ook te helpen. Lucas praat wel met haar: hij stapt alleen niet in."),
    dict(type="waarofniet",
         vraag="In de auto luistert de moeder van Lucas naar zijn verhaal zonder iets te zeggen.",
         antwoord=True,
         uitleg="Sa mère a écouté sans rien dire. Pas op het einde stelt ze één vraag."),
]

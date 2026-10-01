# -*- coding: utf-8 -*-
"""Een Franse tekst analyseren: onderwerp, hoofdgedachte, hoofdpunten, verbanden.

Uit de vakfiche Frans 1 van de 2de graad doorstroomfinaliteit, onderdeel
"Lezen en luisteren". Alleen het lezen: luisteren vraagt geluid.

Het examen Frans 1 duurt 120 minuten en bestaat volledig uit lezen en
luisteren, dus dit is het zwaarste onderdeel dat je hier kan inoefenen. Het
ERK-niveau is B1, een stap boven de eerste graad: je moet niet alleen begrijpen
wat er staat, maar ook verbanden leggen tussen delen van een tekst, en
informatie halen uit wat er niet letterlijk staat.

Elke leesvraag staat op een echt Frans tekstje. Een vraag over lezen zonder
tekst is geen leesvraag. De tekstjes hieronder zijn kort genoeg om op een
telefoon te lezen en lang genoeg om iets te moeten afleiden.

Deel 1 oefent wat er in de tekst staat: onderwerp, hoofdgedachte, hoofdpunten
en losse gegevens. Deel 2 oefent wat je eruit moet afleiden: de bedoeling van
de schrijver, de toon, het verband tussen twee zinnen en het verschil tussen
twee teksten over hetzelfde.
"""

VELO = (
    "Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui "
    "travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte "
    "rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens "
    "essayer. Après l'essai, un habitant sur trois achète son propre vélo."
)
CANTINE = (
    "Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat "
    "végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont "
    "plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le "
    "cuisinier explique que le secret n'est pas le menu, mais le goût."
)
ORAGE = (
    "Hier soir, un orage violent a traversé le sud du pays. Plusieurs routes ont été fermées "
    "pendant deux heures. Il n'y a pas de blessés, mais une centaine de maisons sont restées "
    "sans électricité jusqu'à ce matin."
)
STAGE = (
    "Madame, Monsieur, Je suis élève en quatrième année et je cherche un stage de deux "
    "semaines au mois de février. Je m'intéresse beaucoup au travail de votre laboratoire. Je "
    "suis libre tous les jours et je peux venir me présenter quand vous voulez. Je vous "
    "remercie d'avance pour votre réponse."
)
MARCHE = (
    "Le samedi matin, la place est pleine. On y vend des légumes, du fromage et des fleurs. "
    "Les prix sont plus élevés qu'au supermarché, mais les clients reviennent chaque semaine. "
    "« Ici, je sais qui a cultivé mes tomates », dit une dame de soixante ans."
)
FORUM = (
    "Marie : J'ai acheté ce casque il y a deux mois et le son est déjà mauvais d'un côté. "
    "Quelqu'un a le même problème ? — Yacine : Chez moi, c'était le câble. Je l'ai remplacé "
    "pour douze euros et tout fonctionne. — Lila : Moi, j'ai renvoyé le mien. La garantie "
    "dure deux ans, profites-en."
)

DEEL1 = [
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: '{VELO}' Waarover gaat deze tekst?",
         opties=["over het uitlenen van elektrische fietsen",
                 "over het verkeer in de stad Namen",
                 "over de prijs van een elektrische fiets",
                 "over het werk van de inwoners van Namen"],
         antwoord=0,
         uitleg="Prêter is uitlenen, un vélo is een fiets. Het onderwerp zeg je in enkele woorden: waarover gaat de tekst?"),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over Namen. Wat is de hoofdgedachte, dus de belangrijkste boodschap?",
         opties=["Wie een fiets mag proberen, koopt er vaak zelf een.",
                 "Elektrische fietsen zijn te duur voor veel mensen.",
                 "De stad wil iedereen een gratis fiets geven.",
                 "Namen ligt te ver van de werkplaats van de inwoners."],
         antwoord=0,
         uitleg="De laatste zin geeft het weg: na de proef koopt een op de drie zelf een fiets. Dat is waar de hele tekst naartoe werkt."),
    dict(type="invultekst",
         vraag="Nog altijd het tekstje over Namen. Hoeveel weken mag je de fiets houden? Schrijf het cijfer.",
         antwoord=["6"],
         uitleg="Le prêt dure six semaines: het uitlenen duurt zes weken."),
    dict(type="waarofniet",
         vraag="In het tekstje over Namen kost het niets om de fiets zes weken te mogen proberen.",
         antwoord=True,
         uitleg="Le prêt dure six semaines et ne coûte rien: het lenen duurt zes weken en kost niets."),
    dict(type="meerkeuze",
         vraag="Welke dingen staan er letterlijk in het tekstje over Namen?",
         opties=["De stad leent fietsen uit sinds drie jaar.",
                 "Je moet verder dan vijf kilometer van je werk wonen.",
                 "Een op de drie koopt daarna zelf een fiets.",
                 "De stad verkoopt de gebruikte fietsen door."],
         antwoord=[0, 1, 2],
         uitleg="Depuis trois ans, à plus de cinq kilomètres, un habitant sur trois. Over doorverkopen staat er niets."),
    dict(type="meerkeuze",
         vraag="Wat betekent 'essayer' in het tekstje over Namen?",
         opties=["proberen", "betalen", "herstellen", "bestellen"],
         antwoord=0,
         uitleg="Laisser les gens essayer: de mensen laten proberen. L'essai in de volgende zin is de proef zelf."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: '{CANTINE}' Waarover gaat het?",
         opties=["over een nieuw menu in de schoolkantine",
                 "over de klachten van de leerlingen",
                 "over het werk van een schoolkok",
                 "over vegetarisch eten in België"],
         antwoord=0,
         uitleg="Le menu de la cantine: het menu van de kantine. Dat is waar alles in deze tekst over gaat."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over de kantine. Wat is de hoofdgedachte?",
         opties=["Het menu werkte pas toen het eten lekker was.",
                 "Leerlingen eten liever vlees dan groenten.",
                 "Een school moet minder vlees serveren.",
                 "De kantine was in september nog niet klaar."],
         antwoord=0,
         uitleg="De laatste zin zegt het met zoveel woorden: le secret n'est pas le menu, mais le goût. Niet het menu maar de smaak."),
    dict(type="waarofniet",
         vraag="In het tekstje over de kantine waren de leerlingen vanaf het begin tevreden.",
         antwoord=False,
         uitleg="Au début, beaucoup d'élèves se sont plaints: in het begin klaagden veel leerlingen."),
    dict(type="invultekst",
         vraag="Nog het tekstje over de kantine. Hoeveel maanden later serveert de kantine dubbel zoveel maaltijden? Schrijf het cijfer.",
         antwoord=["3"],
         uitleg="Trois mois plus tard: drie maanden later."),
    dict(type="meerkeuze",
         vraag="Wat betekent 'se plaindre', zoals in 'les élèves se sont plaints'?",
         opties=["klagen", "proeven", "betalen", "wachten"],
         antwoord=0,
         uitleg="Se plaindre is klagen. Une plainte is een klacht."),
    dict(type="meerkeuze",
         vraag=f"Lees dit nieuwsbericht: '{ORAGE}' Wat is het onderwerp?",
         opties=["de gevolgen van een zwaar onweer",
                 "het weer van de komende dagen",
                 "een ongeval op een afgesloten weg",
                 "een panne bij de elektriciteitsmaatschappij"],
         antwoord=0,
         uitleg="Un orage violent is een hevig onweer. De rest van het bericht somt op wat dat onweer veroorzaakte."),
    dict(type="meerkeuze",
         vraag="Welke gevolgen van dat onweer worden in het bericht genoemd?",
         opties=["wegen die een tijd dicht waren",
                 "huizen zonder elektriciteit",
                 "gewonden in het zuiden van het land",
                 "treinen die niet meer reden"],
         antwoord=[0, 1],
         uitleg="Routes fermées en maisons sans électricité staan er. Il n'y a pas de blessés betekent net dat er géén gewonden zijn, en over treinen staat er niets."),
    dict(type="waarofniet",
         vraag="In het nieuwsbericht over het onweer vielen er gewonden.",
         antwoord=False,
         uitleg="Il n'y a pas de blessés: er zijn geen gewonden. Let op die ontkenning, ze draait de hele zin om."),
    dict(type="invultekst",
         vraag="Hoeveel huizen zaten er volgens het nieuwsbericht ongeveer zonder stroom? Antwoord in cijfers.",
         antwoord=["100"],
         uitleg="Une centaine de maisons is een honderdtal huizen. Une centaine is dus niet precies honderd, maar ongeveer."),
    dict(type="meerkeuze",
         vraag=f"Lees deze brief: '{STAGE}' Wat vraagt de schrijver?",
         opties=["een stageplaats van twee weken",
                 "een vaste job in een laboratorium",
                 "een afspraak om het labo te bezoeken",
                 "informatie over het vierde jaar"],
         antwoord=0,
         uitleg="Je cherche un stage de deux semaines: ik zoek een stage van twee weken. Dat is waarvoor de brief geschreven is."),
    dict(type="waarofniet",
         vraag="De schrijver van die brief laat weten wanneer hij of zij beschikbaar is.",
         antwoord=True,
         uitleg="Je suis libre tous les jours: ik ben elke dag vrij. Dat is precies wat een stageplaats wil weten."),
    dict(type="meerkeuze",
         vraag="In welke maand wil de schrijver van die brief stage lopen?",
         opties=["februari", "januari", "april", "september"],
         antwoord=0,
         uitleg="Au mois de février: in de maand februari."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: '{MARCHE}' Welke hoofdpunten staan erin?",
         opties=["Op zaterdagochtend is het plein vol.",
                 "De prijzen liggen hoger dan in de supermarkt.",
                 "De klanten komen toch elke week terug.",
                 "De markt verdwijnt door de supermarkt."],
         antwoord=[0, 1, 2],
         uitleg="Hoofdpunten zijn de zinnen waar de tekst op steunt. Dat de markt zou verdwijnen staat er nergens."),
    dict(type="waarofniet",
         vraag="Op de markt uit dat tekstje liggen de prijzen hoger dan in de supermarkt.",
         antwoord=True,
         uitleg="Les prix sont plus élevés qu'au supermarché. Plus élevé is hoger, niet lager, en dat is net wat de tekst merkwaardig vindt."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag=f"Lees opnieuw: '{VELO}' Waarom schrijft de stad dit volgens jou?",
         opties=["om mensen te overtuigen de fiets eens te proberen",
                 "om te waarschuwen voor het drukke verkeer",
                 "om elektrische fietsen te verkopen aan inwoners",
                 "om uit te leggen hoe je een fiets herstelt"],
         antwoord=0,
         uitleg="De tekst eindigt op een cijfer dat goed nieuws is voor de stad. Dat is geen toeval: de bedoeling is je over de streep trekken."),
    dict(type="meerkeuze",
         vraag="In het tekstje over Namen staat: 'L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer.' Welk verband legt die zin?",
         opties=["een tegenstelling tussen twee bedoelingen",
                 "een oorzaak en een gevolg",
                 "een opsomming van twee voordelen",
                 "een voorbeeld bij de vorige zin"],
         antwoord=0,
         uitleg="Ne … pas …, mais … zet twee dingen tegenover elkaar: niet dit, maar dat. Dat is een tegenstelling."),
    dict(type="waarofniet",
         vraag="Uit het tekstje over Namen kan je afleiden dat twee op de drie inwoners na de proef geen eigen fiets kopen.",
         antwoord=True,
         uitleg="Un habitant sur trois achète: een op de drie koopt. De andere twee dus niet. Dat staat er niet letterlijk, maar je kan het berekenen."),
    dict(type="meerkeuze",
         vraag=f"Lees opnieuw: '{CANTINE}' Welke toon heeft deze tekst?",
         opties=["rustig vaststellend", "boos", "bezorgd", "spottend"],
         antwoord=0,
         uitleg="Er staat geen enkel oordeel in. De tekst zet gewoon op een rij wat er veranderd is en wat het opbracht."),
    dict(type="meerkeuze",
         vraag="In het tekstje over de kantine staat 'Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant.' Wat doet dat zinnetje in de tekst?",
         opties=["het laat zien dat de verandering gelukt is",
                 "het verklaart waarom de leerlingen klaagden",
                 "het geeft een voorbeeld van een vegetarisch gerecht",
                 "het vergelijkt twee scholen met elkaar"],
         antwoord=0,
         uitleg="Na de klachten komt het cijfer dat bewijst dat het toch goed kwam. De tekst draait precies op dat ene zinnetje."),
    dict(type="meerkeuze",
         vraag="Welke woorden in het tekstje over de kantine wijzen op een tijdsverloop?",
         opties=["en septembre", "au début", "trois mois plus tard", "le cuisinier"],
         antwoord=[0, 1, 2],
         uitleg="Die drie zetten de gebeurtenissen na elkaar. Le cuisinier is gewoon wie er spreekt."),
    dict(type="waarofniet",
         vraag="In het tekstje over de kantine is het een leerling die uitlegt waarom het nu wel lukt.",
         antwoord=False,
         uitleg="Le cuisinier explique que…: de kok legt het uit. De leerlingen komen in die tekst alleen voor als wie klaagde."),
    dict(type="meerkeuze",
         vraag=f"Lees opnieuw: '{ORAGE}' Wat voor soort tekst is dit?",
         opties=["een kort nieuwsbericht", "een reclameboodschap", "een persoonlijke brief", "een handleiding"],
         antwoord=0,
         uitleg="Hier soir, feiten, cijfers, geen mening en geen aanspreking. Zo ziet een nieuwsbericht eruit."),
    dict(type="meerkeuze",
         vraag="In het bericht over het onweer staat 'Il n'y a pas de blessés, mais une centaine de maisons sont restées sans électricité.' Wat doet het woordje 'mais' daar?",
         opties=["het zwakt het goede nieuws weer af",
                 "het geeft de oorzaak van de schade",
                 "het somt een tweede gevolg op",
                 "het herhaalt de vorige zin in andere woorden"],
         antwoord=0,
         uitleg="Mais is maar. Eerst iets geruststellends, dan toch een nadeel. Zo'n woordje stuurt hoe je de zin leest."),
    dict(type="invultekst",
         vraag="Welk Frans woord in dat bericht betekent 'gewonden'?",
         antwoord=["blesses", "blessés"],
         uitleg="Des blessés zijn gewonden. Blesser is kwetsen of verwonden."),
    dict(type="meerkeuze",
         vraag=f"Lees opnieuw: '{STAGE}' Hoe weet je dat dit een formele brief is?",
         opties=["aan de aanhef en aan het gebruik van vous",
                 "aan de datum bovenaan",
                 "aan de korte zinnen",
                 "aan het onderwerp van de brief"],
         antwoord=0,
         uitleg="Madame, Monsieur en je vous remercie: wie zo begint en zo aanspreekt, schrijft formeel. Met tu zou dezelfde brief ineens veel te familiair klinken."),
    dict(type="meerkeuze",
         vraag="Welke zinnen uit die stagebrief zijn beleefdheidsformules?",
         opties=["Madame, Monsieur",
                 "Je vous remercie d'avance pour votre réponse.",
                 "Je suis élève en quatrième année.",
                 "Je cherche un stage de deux semaines."],
         antwoord=[0, 1],
         uitleg="De eerste twee zijn vaste formules die je in elke brief kan gebruiken. De andere twee geven echte informatie."),
    dict(type="waarofniet",
         vraag="De schrijver van de stagebrief zegt waarom juist dat labo hem of haar interesseert.",
         antwoord=True,
         uitleg="Je m'intéresse beaucoup au travail de votre laboratoire. Dat is kort, maar het is wel degelijk een reden."),
    dict(type="meerkeuze",
         vraag=f"Lees opnieuw: '{MARCHE}' Wat wil de schrijver met het citaat van de dame van zestig?",
         opties=["uitleggen waarom mensen de hogere prijs betalen",
                 "aantonen dat de markt vooral oudere klanten heeft",
                 "bewijzen dat de tomaten van de markt beter smaken",
                 "laten zien dat de supermarkt te weinig keuze heeft"],
         antwoord=0,
         uitleg="Het citaat volgt meteen op de zin over de hogere prijzen. Het antwoordt dus op de vraag waarom de klanten toch terugkomen."),
    dict(type="waarofniet",
         vraag="Uit het tekstje over de markt blijkt dat de dame van zestig haar tomaten zelf kweekt.",
         antwoord=False,
         uitleg="Je sais qui a cultivé mes tomates: ik weet wie mijn tomaten gekweekt heeft. Ze weet dus wie het deed, maar zij is het niet."),
    dict(type="meerkeuze",
         vraag=f"Lees dit stukje van een forum: '{FORUM}' Wat is het probleem van Marie?",
         opties=["een koptelefoon die langs één kant slecht klinkt",
                 "een koptelefoon die ze niet kan terugsturen",
                 "een kabel die ze nergens vindt",
                 "een garantie die net verlopen is"],
         antwoord=0,
         uitleg="Le son est déjà mauvais d'un côté: het geluid is al slecht aan één kant."),
    dict(type="meerkeuze",
         vraag="Welke oplossingen stellen de anderen op dat forum voor?",
         opties=["de kabel vervangen",
                 "een beroep doen op de garantie",
                 "een nieuwe koptelefoon kopen",
                 "het toestel zelf openmaken"],
         antwoord=[0, 1],
         uitleg="Yacine verving de kabel, Lila wijst op de garantie van twee jaar. De twee andere antwoorden stelt niemand voor."),
    dict(type="waarofniet",
         vraag="Op dat forum heeft Yacine zijn koptelefoon teruggestuurd.",
         antwoord=False,
         uitleg="Yacine verving de kabel voor twaalf euro. Lila is diegene die het hare terugstuurde. Lees goed wie wat zegt."),
    dict(type="meerkeuze",
         vraag="Het tekstje over de markt en het stukje forum gaan allebei over kopen. Wat is het grootste verschil?",
         opties=["het ene beschrijft, het andere geeft raad",
                 "het ene is formeel, het andere informeel",
                 "het ene is recenter dan het andere",
                 "het ene gaat over eten, het andere over kleding"],
         antwoord=0,
         uitleg="Teksten vergelijken hoort bij lezen op dit niveau. De markttekst vertelt wat er te zien is; op het forum antwoorden mensen op een vraag."),
    dict(type="invultekst",
         vraag="In het forumstukje raadt Lila aan: 'profites-en'. Welk Frans werkwoord staat daarin, in de infinitief?",
         antwoord=["profiter"],
         uitleg="Profiter de quelque chose is van iets profiteren of er gebruik van maken. Het en verwijst hier naar de garantie van twee jaar."),
]

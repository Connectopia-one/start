# -*- coding: utf-8 -*-
"""Woordvelden: tijd en plaats, het weer, reizen, vervoer, landen.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. De woordvelden die
hier aan bod komen: dagen, maanden, seizoenen en feesten; uur en plaats; het
weer; vakantie en reizen; transportmiddelen; landen en nationaliteiten; en de
cijfers, maten en hoeveelheden die daarbij horen.

Dit zijn de woorden waarmee een tekst zegt wanneer en waar iets gebeurt. Een
uurtabel, een weerbericht, een reisverslag, een bericht over een vertraging: op
het examen moet je daar de gegevens uit halen die je nodig hebt.

Deel 1 gaat over tijd en plaats: de dagen, de maanden, de seizoenen, het uur en
de woorden die zeggen waar iets ligt. Deel 2 gaat over het weer, over reizen en
vervoer, en over de landen en nationaliteiten.
"""

AGENDA = (
    "Lundi : cours jusqu'à quatre heures. Mardi : dentiste à dix-sept heures trente. Mercredi "
    "après-midi : libre. Jeudi : entraînement de basket. Vendredi : anniversaire de Lila. "
    "Samedi matin : courses. Dimanche : rien, enfin."
)
SAISONS = (
    "En Belgique, le printemps commence en mars et l'été en juin. Les grandes vacances durent de "
    "juillet à fin août. L'automne apporte la pluie et les feuilles mortes, et l'hiver les jours "
    "courts. Noël tombe le 25 décembre, le Nouvel An le 1er janvier."
)
PLAN = (
    "La gare est tout droit, au bout de l'avenue. La poste se trouve à droite, juste après le "
    "pont. L'arrêt de bus est en face de la boulangerie, entre la pharmacie et la banque. Le "
    "parking se trouve derrière l'église."
)

DEEL1 = [
    # --- Les jours et les mois ------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze agenda: « {AGENDA} » Op welke dag is er niets gepland?",
         opties=["zondag", "woensdag", "zaterdag", "maandag"],
         antwoord=0,
         uitleg="Dimanche : rien, enfin. Rien betekent niets; woensdagnamiddag is wel vrij, maar de voormiddag niet."),
    dict(type="meerkeuze",
         vraag="Dezelfde agenda. Hoe laat is de tandarts?",
         opties=["half zes 's avonds", "half vijf", "vijf uur", "zeventien uur"],
         antwoord=0,
         uitleg="Dix-sept heures trente is 17.30 u, dus half zes. Het Frans gebruikt in een agenda de klok van vierentwintig uur."),
    dict(type="invultekst",
         vraag="Nog die agenda. Op welke dag is er basketbaltraining? Schrijf de dag in het Nederlands.",
         antwoord=["donderdag"],
         uitleg="Jeudi : entraînement de basket. Jeudi is donderdag."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn dagen van de week?",
         opties=["mardi",
                 "vendredi",
                 "dimanche",
                 "janvier"],
         antwoord=[0, 1, 2],
         uitleg="Dinsdag, vrijdag, zondag. Janvier is januari, een maand. Dagen en maanden schrijf je in het Frans met een kleine letter."),
    dict(type="waarofniet",
         vraag="In het Frans schrijf je de dagen en de maanden met een hoofdletter.",
         antwoord=False,
         uitleg="Lundi, janvier, mars: altijd klein. Dat is anders dan in het Engels."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {SAISONS} » In welke maand begint de lente?",
         opties=["maart", "juni", "januari", "september"],
         antwoord=0,
         uitleg="Le printemps commence en mars. Le printemps is de lente."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje. Welk Frans woord betekent 'winter'? Schrijf het woord zonder lidwoord.",
         antwoord=["hiver"],
         uitleg="L'hiver, met een stille h, dus l' en niet le."),
    dict(type="meerkeuze",
         vraag="Nog dat tekstje. Wanneer valt Nieuwjaar?",
         opties=["op 1 januari", "op 25 december", "op 31 december", "in de lente"],
         antwoord=0,
         uitleg="Le Nouvel An le 1er janvier. 1er is premier, de eerste."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje lopen de grote vakantie van juli tot eind augustus.",
         antwoord=True,
         uitleg="Les grandes vacances durent de juillet à fin août. Les vacances staat in het Frans altijd in het meervoud."),
    dict(type="meerkeuze",
         vraag="Welk Frans woord betekent 'herfst'?",
         opties=["l'automne", "l'été", "le printemps", "l'hiver"],
         antwoord=0,
         uitleg="L'automne. L'été is de zomer, le printemps de lente, l'hiver de winter."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'verjaardag'? Schrijf het woord zonder lidwoord.",
         antwoord=["anniversaire"],
         uitleg="Un anniversaire. Bonne fête zeg je op een naamdag, bon anniversaire op een verjaardag."),
    # --- L'heure --------------------------------------------------------------
    dict(type="meerkeuze",
         vraag="Hoe zeg je in het Frans « het is kwart voor negen »?",
         opties=["Il est neuf heures moins le quart.",
                 "Il est huit heures et quart.",
                 "Il est neuf heures et quart.",
                 "Il est huit heures moins le quart."],
         antwoord=0,
         uitleg="Moins le quart betekent een kwart minder, dus kwart voor. Et quart is kwart na."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'half', zoals in « il est trois heures et ... »? Schrijf één woord.",
         antwoord=["demie"],
         uitleg="Trois heures et demie is half vier. Let op: demie met een e, omdat heure vrouwelijk is."),
    dict(type="waarofniet",
         vraag="Midi betekent middernacht.",
         antwoord=False,
         uitleg="Midi is twaalf uur 's middags, minuit is middernacht. Twee woorden die je snel verwart."),
    # --- Les lieux -------------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze uitleg: « {PLAN} » Waar is de bushalte?",
         opties=["tegenover de bakkerij",
                 "naast de kerk",
                 "achter de brug",
                 "voor het station"],
         antwoord=0,
         uitleg="En face de la boulangerie. En face de betekent tegenover."),
    dict(type="meerkeuze",
         vraag="Dezelfde uitleg. Waar staat de parking?",
         opties=["achter de kerk", "voor de kerk", "naast de post", "op het plein"],
         antwoord=0,
         uitleg="Derrière l'église. Derrière is achter, devant is voor."),
    dict(type="invultekst",
         vraag="Nog die uitleg. Welke Franse uitdrukking betekent 'rechtdoor'? Vul in: « tout ... ». Schrijf één woord.",
         antwoord=["droit"],
         uitleg="Tout droit is rechtdoor; à droite is naar rechts. Eén letter verschil, een heel ander antwoord."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zeggen waar iets ligt?",
         opties=["entre",
                 "derrière",
                 "à côté de",
                 "pendant"],
         antwoord=[0, 1, 2],
         uitleg="Tussen, achter, naast. Pendant betekent tijdens en zegt wanneer, niet waar."),
    dict(type="waarofniet",
         vraag="Sous betekent onder en sur betekent op.",
         antwoord=True,
         uitleg="Le chat est sous la table of sur la table: twee heel verschillende plaatsen voor dezelfde kat."),
    dict(type="meerkeuze",
         vraag="Iemand zegt « C'est au bout de la rue. » Waar moet je zijn?",
         opties=["aan het einde van de straat",
                 "aan het begin van de straat",
                 "in het midden van de straat",
                 "aan de overkant van de straat"],
         antwoord=0,
         uitleg="Le bout is het uiteinde. Au bout de la rue: helemaal op het einde."),
]

METEO = (
    "Demain, le temps restera gris dans tout le pays. Il pleuvra le matin en Wallonie, avec un "
    "vent assez fort venant de l'ouest. Les températures ne dépasseront pas douze degrés. En "
    "fin de journée, quelques éclaircies à la côte."
)
TRAIN = (
    "Le train de 14 h 05 vers Namur a un retard de vingt minutes. Les voyageurs pour Charleroi "
    "doivent changer à Ottignies. Le train suivant part à 14 h 35, voie 3."
)
VACANCES = (
    "L'été dernier, nous sommes partis dix jours en Espagne. Nous avons pris l'avion jusqu'à "
    "Barcelone, puis le train jusqu'à la côte. L'hôtel était simple mais propre, et la mer était "
    "à deux cents mètres. Je voudrais y retourner."
)
PAYS = (
    "Dans ma classe, il y a des élèves de partout. Yacine est marocain, Lena est allemande, "
    "Mateo vient d'Italie et Noor est née en Belgique. On parle français entre nous, mais "
    "chacun connaît encore une autre langue."
)

DEEL2 = [
    # --- La météo ---------------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit weerbericht: « {METEO} » Wat voor weer wordt het morgen?",
         opties=["grijs, met regen in de voormiddag in Wallonië",
                 "zonnig in het hele land",
                 "regen in de namiddag aan de kust",
                 "warm, met meer dan twintig graden"],
         antwoord=0,
         uitleg="Le temps restera gris en il pleuvra le matin en Wallonie. Pleuvoir is regenen."),
    dict(type="invultekst",
         vraag="Hetzelfde weerbericht. Hoeveel graden wordt het maximaal? Schrijf alleen het getal.",
         antwoord=["12"],
         uitleg="Les températures ne dépasseront pas douze degrés. Dépasser is overschrijden."),
    dict(type="meerkeuze",
         vraag="Nog dat weerbericht. Uit welke richting komt de wind?",
         opties=["uit het westen", "uit het oosten", "uit het noorden", "uit het zuiden"],
         antwoord=0,
         uitleg="Venant de l'ouest. L'ouest is het westen, l'est het oosten, le nord het noorden, le sud het zuiden."),
    dict(type="waarofniet",
         vraag="Volgens dat weerbericht komen er op het einde van de dag opklaringen aan de kust.",
         antwoord=True,
         uitleg="Quelques éclaircies à la côte. Une éclaircie is een opklaring, van clair, helder."),
    dict(type="meerkeuze",
         vraag="Welke Franse uitdrukkingen gaan over het weer?",
         opties=["il fait beau",
                 "il neige",
                 "il y a du vent",
                 "il est tard"],
         antwoord=[0, 1, 2],
         uitleg="Het is mooi weer, het sneeuwt, het waait. Il est tard betekent het is laat, en dat gaat over de tijd."),
    dict(type="invultekst",
         vraag="Hoe zeg je in het Frans 'het regent'? Schrijf de twee woorden.",
         antwoord=["il pleut"],
         uitleg="Pleuvoir is een onpersoonlijk werkwoord: het bestaat alleen in de derde persoon enkelvoud, net als neiger, sneeuwen."),
    dict(type="waarofniet",
         vraag="Il fait froid betekent dat het warm is.",
         antwoord=False,
         uitleg="Froid is koud, chaud is warm. Il fait chaud is dus het omgekeerde."),
    # --- Les transports -----------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit bericht: « {TRAIN} » Hoeveel vertraging heeft de trein van 14 u 05?",
         opties=["twintig minuten", "vijf minuten", "dertig minuten", "een halfuur"],
         antwoord=0,
         uitleg="Un retard de vingt minutes. Un retard is een vertraging."),
    dict(type="meerkeuze",
         vraag="Hetzelfde bericht. Wat moeten de reizigers naar Charleroi doen?",
         opties=["overstappen in Ottignies",
                 "wachten op de trein van 14 u 35",
                 "naar spoor 3 gaan",
                 "een andere trein in Namen nemen"],
         antwoord=0,
         uitleg="Doivent changer à Ottignies. Changer betekent hier van trein veranderen, overstappen."),
    dict(type="invultekst",
         vraag="Nog dat bericht. Welk Frans woord betekent 'spoor'? Schrijf het woord zonder lidwoord.",
         antwoord=["voie"],
         uitleg="Voie 3. Une voie is een spoor; un quai is het perron."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn vervoermiddelen?",
         opties=["le tram",
                 "l'avion",
                 "le bateau",
                 "le quai"],
         antwoord=[0, 1, 2],
         uitleg="Tram, vliegtuig, boot. Un quai is het perron of de kaai, dus een plaats."),
    dict(type="waarofniet",
         vraag="Je zegt in het Frans prendre le bus en niet aller le bus.",
         antwoord=True,
         uitleg="Prendre le bus, prendre le train, prendre l'avion. Met de wagen is en voiture, te voet is à pied."),
    dict(type="meerkeuze",
         vraag="Hoe zeg je in het Frans « ik ga met de fiets »?",
         opties=["Je vais à vélo.",
                 "Je vais en vélo.",
                 "Je prends à vélo.",
                 "Je fais le vélo."],
         antwoord=0,
         uitleg="À vélo of à pied, want je zit erop of erin niet. En voiture, en train, en bus: daar zit je in."),
    # --- Les vacances -------------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit verslagje: « {VACANCES} » Hoe zijn ze tot aan de kust gekomen?",
         opties=["met het vliegtuig tot Barcelona en dan met de trein",
                 "met de wagen in één keer",
                 "met het vliegtuig tot aan de kust",
                 "met de trein en dan met de bus"],
         antwoord=0,
         uitleg="Nous avons pris l'avion jusqu'à Barcelone, puis le train jusqu'à la côte. Jusqu'à betekent tot aan."),
    dict(type="invultekst",
         vraag="Hetzelfde verslagje. Hoeveel dagen zijn ze weggeweest? Schrijf alleen het getal.",
         antwoord=["10"],
         uitleg="Dix jours en Espagne."),
    dict(type="waarofniet",
         vraag="Volgens dat verslagje lag het hotel ver van de zee.",
         antwoord=False,
         uitleg="La mer était à deux cents mètres: de zee lag op tweehonderd meter, dus dichtbij."),
    # --- Les pays et les nationalités -----------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {PAYS} » Welke nationaliteit heeft Lena?",
         opties=["Duitse", "Marokkaanse", "Italiaanse", "Belgische"],
         antwoord=0,
         uitleg="Lena est allemande. Allemand of allemande betekent Duits."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje. Uit welk land komt Mateo? Schrijf het land in het Nederlands.",
         antwoord=["Italië", "italie"],
         uitleg="Mateo vient d'Italie. Bij een land dat met een klinker begint, wordt de tot d'."),
    dict(type="waarofniet",
         vraag="Een nationaliteit schrijf je in het Frans met een kleine letter: je suis belge.",
         antwoord=True,
         uitleg="Het land krijgt wel een hoofdletter: la Belgique, la France. Het bijvoeglijk naamwoord niet."),
    dict(type="meerkeuze",
         vraag="Hoe zeg je in het Frans « ik woon in Frankrijk »?",
         opties=["J'habite en France.",
                 "J'habite à France.",
                 "J'habite dans France.",
                 "J'habite le France."],
         antwoord=0,
         uitleg="Bij een vrouwelijk land gebruik je en: en France, en Belgique, en Italie. Bij een stad gebruik je à: à Paris."),
]

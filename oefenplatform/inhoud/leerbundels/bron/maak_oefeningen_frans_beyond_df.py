# -*- coding: utf-8 -*-
"""Oefenbundels Frans — 🌍 Beyond dubbele finaliteit, 5de en 6de middelbaar.

Zestien bundels, één per thema van `beyond-dubbele-finaliteit/frans.json`.

Deze fiche (Frans 1 en Frans 2, derde graad dubbele finaliteit) blijft op
ERK A2+ staan. Wat ze niet vraagt, staat hier dus ook niet in, ook niet als
oefening: de subjonctif, de gérondif, de plus-que-parfait, de indirecte rede
en de passieve zin. Daarom worden de reeksen "Le subjonctif", "Le gérondif",
"Le plus-que-parfait", "Le discours indirect" en "La voix passive" van
doorstroom hier niet overgenomen.

Wat doorstroom niet heeft maar deze fiche wel: een eigen thema over de
tegenwoordige tijd en de gebiedende wijs, en vijf woordveldthemas in plaats
van twee. Die zijn hier dus van nul geschreven.
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import maak_oefeningen_frans_beyond as door

VAK = "Frans"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NIVEAU = "-beyond-dubbele-finaliteit"
VOOR = "oefenbundel-"
W, WW, WL = "150px", "220px", "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."
HOE = [
    "Schrijf met potlood, dan kan je gerust iets wegvegen en opnieuw proberen.",
    "Zet de accenten erbij: op papier horen ze er gewoon op.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands of Engels woord lijkt, "
    "en lees daarna de hele zin nog eens.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]
HOE_LEZEN = [
    "Lees de tekst eerst één keer helemaal, zonder te stoppen bij een woord dat je "
    "niet kent.",
    "Lees daarna de vragen, en pas dan de tekst een tweede keer.",
    "Streep bij elk antwoord aan waar je het in de tekst gevonden hebt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


def reeks(slug, kop, weg=()):
    """Eén reeks uit de bundel van doorstroom, eventueel zonder een paar
    oefeningen die hier te zwaar zijn (nummer vanaf 1)."""
    for r in door.OEFENBUNDELS[VOOR + slug + "-beyond"]["reeksen"]:
        if r["kop"] == kop:
            r = copy.deepcopy(r)
            if weg:
                r["oefeningen"] = [o for i, o in enumerate(r["oefeningen"], 1)
                                   if i not in weg]
            return r
    raise KeyError(f"{slug}: {kop}")


# ============================================================
zet("een-franse-tekst-lezen",
    titel="Een Franse tekst lezen",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Le texte",
             opdracht="Lees de tekst.",
             oefeningen=[
                 ("tekst",
                  "<p><strong>Le vélo de Madame Lambert</strong></p>"
                  "<p>Madame Lambert a soixante-huit ans et elle habite à Namur. "
                  "Chaque matin, elle prend son vélo et elle va au marché. Elle achète "
                  "du pain, des légumes et parfois du poisson. « Je n'aime pas la voiture, "
                  "dit-elle. En ville, le vélo est plus rapide, et je ne cherche pas de "
                  "place pour me garer. »</p>"
                  "<p>Il y a deux ans, son vélo est tombé en panne. Le magasin voulait "
                  "quatre-vingts euros pour la réparation. C'était trop cher pour elle. "
                  "Alors elle est allée au « Repair Café » du quartier. Là, des bénévoles "
                  "aident les gens à réparer leurs objets. Ils ne font pas le travail pour "
                  "vous : ils vous montrent comment faire. En deux heures, le vélo "
                  "roulait de nouveau. Madame Lambert n'a rien payé, mais elle a apporté "
                  "un gâteau.</p>"
                  "<p>Aujourd'hui, elle y retourne un samedi par mois, mais pas pour son "
                  "vélo. Elle apprend aux autres à recoudre un bouton et à raccourcir un "
                  "pantalon. « À mon âge, on ne travaille plus, dit-elle en riant. Mais on "
                  "sait encore des choses. »</p>"),
             ]),
        dict(kop="Comprendre le texte",
             opdracht="Antwoord in het Nederlands, met een volledige zin.",
             oefeningen=[
                 ("kort", "Waar woont madame Lambert?", "in Namen", W),
                 ("kort", "Waarom neemt ze liever de fiets dan de auto?",
                  "in de stad is de fiets sneller en ze moet geen parkeerplaats zoeken", WL),
                 ("kort", "Hoeveel vroeg de winkel voor de herstelling?",
                  "tachtig euro", W),
                 ("open", "Wat doen de vrijwilligers van het Repair Café precies, en wat "
                          "doen ze niet?",
                  "Ze helpen de mensen hun eigen spullen herstellen en leggen uit hoe het "
                  "moet. Ze doen het werk niet in jouw plaats.", 3),
                 ("kort", "Wat bracht ze mee in plaats van geld?", "een cake", W),
                 ("kort", "Wat leert ze er nu zelf aan anderen?",
                  "een knoop aanzetten en een broek korter maken", WL),
             ]),
        dict(kop="Les mots du texte",
             opdracht="Zoek het Franse woord in de tekst.",
             oefeningen=[
                 ("rij", [("de markt", "le marché"), ("de herstelling", "la réparation"),
                          ("een vrijwilliger", "un bénévole"), ("te duur", "trop cher"),
                          ("parkeren", "se garer"), ("een knoop", "un bouton")],
                  "Welk Frans woord staat er?", WW),
                 ("kort", "Wat betekent <em>tomber en panne</em>?",
                  "stuk vallen, niet meer werken", WL),
             ]),
        dict(kop="Vrai ou faux?",
             opdracht="Waar of niet waar? Schrijf erbij in welke alinea je het vindt.",
             oefeningen=[
                 ("waar", "Madame Lambert gaat één keer per week naar de markt.", False),
                 ("waar", "Ze heeft haar fiets zelf hersteld, met hulp.", True),
                 ("waar", "Ze betaalde tachtig euro in het Repair Café.", False),
                 ("waar", "Ze gaat er nu nog elke maand naartoe.", True),
             ]),
        dict(kop="Entre les lignes",
             opdracht="Antwoord in twee of drie zinnen.",
             oefeningen=[
                 ("open", "Waarom zegt madame Lambert <em>on sait encore des choses</em>, "
                          "denk je?",
                  "Omdat ze wil zeggen dat je na je pensioen nog altijd nuttig bent. Ze "
                  "werkt niet meer, maar ze kan nog dingen die ze kan doorgeven.", 4),
             ]),
    ])

# ============================================================
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    reeksen=[
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Quel type de texte?"),
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Fait ou opinion?"),
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Les mots de liaison"),
        dict(kop="Où le lis-tu?",
             opdracht="Schrijf waar je zo'n tekst tegenkomt.",
             oefeningen=[
                 ("rij", [("une recette", "in een kookboek of op een website met recepten"),
                          ("un horaire de train", "in de stationshal of in een app"),
                          ("une petite annonce", "in een krant of op een verkoopsite"),
                          ("un mode d'emploi", "in het doosje bij een toestel"),
                          ("un faire-part", "in de brievenbus, bij een geboorte of een huwelijk")],
                  "Waar lees je dat?", WL),
                 ("kort", "Wat wil een advertentie dat je doet?",
                  "iets kopen of ergens naartoe gaan", WL),
             ]),
    ])

# ============================================================
zet("de-franstalige-wereld-gewoontes-en-reizen",
    titel="De Franstalige wereld: gewoontes en reizen",
    reeksen=[
        reeks("de-franstalige-wereld-omgangsvormen-en-gewoontes", "Tu ou vous?", weg=(2,)),
        reeks("de-franstalige-wereld-omgangsvormen-en-gewoontes", "Les usages"),
        reeks("de-franstalige-wereld-omgangsvormen-en-gewoontes", "Le français dans le monde",
              weg=(3,)),
        dict(kop="En voyage",
             opdracht="Schrijf de Franse zin die je in die situatie zegt.",
             oefeningen=[
                 ("rij", [("Je vraagt de weg naar het station.",
                           "Pardon, où est la gare, s'il vous plaît ?"),
                          ("Je vraagt een ticket naar Luik.",
                           "Un billet pour Liège, s'il vous plaît."),
                          ("Je vraagt wat het kost.", "Combien ça coûte ?"),
                          ("Je zegt dat je een kamer gereserveerd hebt.",
                           "J'ai réservé une chambre."),
                          ("Je vraagt of ze Nederlands spreken.",
                           "Est-ce que vous parlez néerlandais ?"),
                          ("Je zegt dat je je trein gemist hebt.", "J'ai raté mon train.")],
                  "Welke Franse zin?", WL),
                 ("rij", [("un aller-retour", "een heen-en-terugticket"),
                          ("le quai", "het perron"), ("la douane", "de douane"),
                          ("l'auberge de jeunesse", "de jeugdherberg")],
                  "Wat betekent het?", WW),
             ]),
    ])

# ============================================================
zet("schrijven-en-spreken-in-het-frans",
    titel="Schrijven en spreken in het Frans",
    reeksen=[
        reeks("schrijven-en-schriftelijke-interactie", "La structure", weg=(3, 4)),
        reeks("schrijven-en-schriftelijke-interactie", "La lettre formelle"),
        reeks("schrijven-en-schriftelijke-interactie", "Plus poli"),
        dict(kop="Au téléphone",
             opdracht="Vul het gesprek aan in het Frans.",
             oefeningen=[
                 ("rij", [("Je meldt je aan de telefoon.", "Allô, bonjour, c'est ... à l'appareil."),
                          ("Je vraagt naar iemand.", "Est-ce que je peux parler à ... ?"),
                          ("Je hebt het niet begrepen.",
                           "Pardon, pouvez-vous répéter, s'il vous plaît ?"),
                          ("Je vraagt of hij langzamer spreekt.",
                           "Pouvez-vous parler plus lentement ?"),
                          ("Je sluit af.", "Merci beaucoup, au revoir.")],
                  "Welke Franse zin?", WL),
                 ("open", "Wat zeg je als je een woord niet kent terwijl je aan het spreken "
                          "bent?",
                  "Je legt het met andere woorden uit: Comment dit-on ... en français ? of "
                  "C'est une chose pour ... Stilvallen helpt niet, verder praten met de "
                  "woorden die je wel kent wel.", 3),
             ]),
        reeks("schrijven-en-schriftelijke-interactie", "Relire son texte"),
    ])

# ============================================================
zet("woordvelden-dagelijks-leven-eten-en-wonen",
    titel="Woordvelden: dagelijks leven, eten en wonen",
    reeksen=[
        dict(kop="Ma journée",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("opstaan", "se lever"), ("zich wassen", "se laver"),
                          ("zich aankleden", "s'habiller"), ("ontbijten", "prendre le petit déjeuner"),
                          ("naar bed gaan", "se coucher"), ("slapen", "dormir")],
                  "Welk Frans woord?", WW),
                 ("rij", [("gisteren", "hier"), ("morgen", "demain"),
                          ("'s middags", "à midi"), ("elke dag", "chaque jour"),
                          ("nooit", "jamais"), ("soms", "parfois")],
                  "Welk Frans woord?", WW),
                 ("open", "Schrijf in drie Franse zinnen wat je vanmorgen gedaan hebt.",
                  "Een eigen antwoord met drie volledige zinnen in de passé composé, "
                  "bijvoorbeeld: Je me suis levé à sept heures. J'ai mangé du pain avec de "
                  "la confiture. Puis j'ai pris le bus pour aller à l'école.", 4),
             ]),
        dict(kop="La personne",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een neef of nicht", "un cousin, une cousine"),
                          ("een buur", "un voisin"), ("vriendelijk", "gentil"),
                          ("verlegen", "timide"), ("moe", "fatigué"), ("blij", "content")],
                  "Welk Frans woord?", WW),
             ]),
        reeks("woordvelden-de-mens-gezondheid-eten-en-wonen", "La table"),
        dict(kop="Au magasin",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een kilo appels", "un kilo de pommes"),
                          ("een stuk kaas", "un morceau de fromage"),
                          ("een doos eieren", "une boîte d'œufs"),
                          ("een fles water", "une bouteille d'eau"),
                          ("de kassa", "la caisse"), ("het wisselgeld", "la monnaie")],
                  "Welk Frans woord?", WW),
                 ("kort", "Welk woordje staat er altijd tussen een hoeveelheid en het "
                          "product?", "de of d'", W),
             ]),
        reeks("woordvelden-de-mens-gezondheid-eten-en-wonen", "Le logement", weg=(3,)),
    ])

# ============================================================
zet("woordvelden-gezondheid-natuur-en-milieu",
    titel="Woordvelden: gezondheid, natuur en milieu",
    reeksen=[
        reeks("woordvelden-de-mens-gezondheid-eten-en-wonen", "La santé"),
        dict(kop="Le corps",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("het hoofd", "la tête"), ("de rug", "le dos"),
                          ("de buik", "le ventre"), ("de hand", "la main"),
                          ("het been", "la jambe"), ("de tand", "la dent"),
                          ("het oog", "l'œil"), ("het oor", "l'oreille")],
                  "Welk Frans woord?", WW),
                 ("kort", "Hoe zeg je dat je hoofdpijn hebt?", "j'ai mal à la tête", WL),
             ]),
        dict(kop="La nature et le temps",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een boom", "un arbre"), ("een boerderij", "une ferme"),
                          ("het bos", "la forêt"), ("de kust", "la côte"),
                          ("een rivier", "une rivière"), ("een veld", "un champ")],
                  "Welk Frans woord?", WW),
                 ("rij", [("Il fait beau.", "het is mooi weer"), ("Il pleut.", "het regent"),
                          ("Il gèle.", "het vriest"), ("Il y a du vent.", "het waait"),
                          ("Le ciel est couvert.", "de lucht is bewolkt")],
                  "Wat betekent het?", WW),
                 ("kort", "Met welk werkwoord begint bijna elke Franse zin over het weer?",
                  "faire: il fait ...", WL),
             ]),
        dict(kop="L'environnement",
             opdracht="Schrijf het Franse woord of de uitdrukking.",
             oefeningen=[
                 ("rij", [("het afval", "les déchets"), ("sorteren", "trier"),
                          ("vervuiling", "la pollution"),
                          ("hernieuwbare energie", "l'énergie renouvelable"),
                          ("een vuilnisbak", "une poubelle"), ("het verbruik", "la consommation")],
                  "Welk Frans woord?", WW),
                 ("open", "Schrijf in drie Franse zinnen wat jij thuis doet voor het milieu.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: Chez nous, on "
                  "trie le papier et le verre. Je prends le vélo pour aller à l'école. En "
                  "hiver, nous ne chauffons pas toutes les pièces.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-school-werk-geld-en-verkeer",
    titel="Woordvelden: school, werk, geld en verkeer",
    reeksen=[
        reeks("woordvelden-school-werk-reizen-en-de-samenleving", "À l'école et au travail",
              weg=(3,)),
        dict(kop="L'argent",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("sparen", "économiser"), ("lenen", "emprunter"),
                          ("betalen", "payer"), ("de rekening", "l'addition"),
                          ("een korting", "une réduction"), ("goedkoop", "pas cher, bon marché"),
                          ("de koopjes", "les soldes")],
                  "Welk Frans woord?", WW),
                 ("rij", [("Ça coûte combien ?", "hoeveel kost het?"),
                          ("Je paie par carte.", "ik betaal met de kaart"),
                          ("C'est trop cher pour moi.", "dat is te duur voor mij"),
                          ("Vous avez la monnaie ?", "hebt u het gepast?")],
                  "Wat betekent het?", WW),
             ]),
        dict(kop="Sur la route",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("het voetpad", "le trottoir"), ("het kruispunt", "le carrefour"),
                          ("het verkeerslicht", "le feu"), ("de file", "l'embouteillage"),
                          ("de bushalte", "l'arrêt de bus"), ("het spitsuur", "l'heure de pointe")],
                  "Welk Frans woord?", WW),
                 ("rij", [("rechts afslaan", "tourner à droite"),
                          ("rechtdoor rijden", "aller tout droit"),
                          ("oversteken", "traverser"), ("opletten", "faire attention")],
                  "Welk Frans woord?", WW),
                 ("open", "Leg in drie Franse zinnen de weg uit van je school naar je huis.",
                  "Een eigen antwoord met drie volledige zinnen en richtingen, bijvoorbeeld: "
                  "Tu sors de l'école et tu tournes à gauche. Tu vas tout droit jusqu'au feu. "
                  "Puis tu traverses la rue et ma maison est la troisième à droite.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-kunst-geschiedenis-en-de-samenleving",
    titel="Woordvelden: kunst, geschiedenis en de samenleving",
    reeksen=[
        dict(kop="L'art et la culture",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een schilderij", "un tableau"), ("een tentoonstelling", "une exposition"),
                          ("een museum", "un musée"), ("een lied", "une chanson"),
                          ("een toneelstuk", "une pièce de théâtre"),
                          ("een kunstenaar", "un artiste")],
                  "Welk Frans woord?", WW),
                 ("rij", [("Ça me plaît.", "dat bevalt me"),
                          ("Je trouve ça beau.", "ik vind dat mooi"),
                          ("Ce n'est pas mon goût.", "dat is mijn smaak niet"),
                          ("Ça ne me dit rien.", "dat spreekt me niet aan")],
                  "Wat betekent het?", WW),
             ]),
        dict(kop="L'histoire",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("de oorlog", "la guerre"), ("de vrede", "la paix"),
                          ("een eeuw", "un siècle"), ("het kasteel", "le château"),
                          ("de koning", "le roi"), ("een gebeurtenis", "un événement")],
                  "Welk Frans woord?", WW),
                 ("kort", "Hoe schrijf je 1914 in het Frans?",
                  "mille neuf cent quatorze", WL),
             ]),
        dict(kop="La société",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een verkiezing", "une élection"), ("een wet", "une loi"),
                          ("de gemeente", "la commune"), ("betogen", "manifester"),
                          ("vrijwilligerswerk doen", "faire du bénévolat"),
                          ("de armoede", "la pauvreté")],
                  "Welk Frans woord?", WW),
                 ("open", "Schrijf in drie Franse zinnen je mening over één van die "
                          "onderwerpen. Gebruik <em>à mon avis</em> en <em>parce que</em>.",
                  "Een eigen antwoord met drie volledige zinnen en een reden, bijvoorbeeld: À "
                  "mon avis, le bénévolat est important. On aide les autres et on apprend "
                  "beaucoup. Je voudrais le faire parce que j'aime travailler avec des "
                  "enfants.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-wetenschap-techniek-en-taal",
    titel="Woordvelden: wetenschap, techniek en taal",
    reeksen=[
        dict(kop="La technique",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een toestel", "un appareil"), ("de knop", "le bouton"),
                          ("het scherm", "l'écran"), ("de batterij", "la batterie"),
                          ("de lader", "le chargeur"), ("het wachtwoord", "le mot de passe"),
                          ("een bestand", "un fichier"), ("herstellen", "réparer")],
                  "Welk Frans woord?", WW),
                 ("rij", [("Ça ne marche pas.", "het werkt niet"),
                          ("Allume l'ordinateur.", "zet de computer aan"),
                          ("Éteins la lumière.", "doe het licht uit"),
                          ("Branche le chargeur.", "steek de lader in")],
                  "Wat betekent het?", WW),
             ]),
        dict(kop="Les sciences",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een proef", "une expérience"), ("meten", "mesurer"),
                          ("wegen", "peser"), ("het gewicht", "le poids"),
                          ("de temperatuur", "la température"), ("een resultaat", "un résultat")],
                  "Welk Frans woord?", WW),
                 ("kort", "Pas op met <em>une expérience</em>: welke twee betekenissen heeft "
                          "het?", "een proef, en ervaring", WL),
             ]),
        dict(kop="Les mots de la langue",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een woord", "un mot"), ("een zin", "une phrase"),
                          ("een vraag", "une question"), ("een voorbeeld", "un exemple"),
                          ("vertalen", "traduire"), ("uitspreken", "prononcer"),
                          ("een fout", "une faute")],
                  "Welk Frans woord?", WW),
                 ("rij", [("Comment dit-on ... en français ?", "hoe zeg je ... in het Frans?"),
                          ("Qu'est-ce que ça veut dire ?", "wat betekent dat?"),
                          ("Comment ça s'écrit ?", "hoe schrijf je dat?"),
                          ("Je ne comprends pas.", "ik begrijp het niet")],
                  "Wat betekent het?", WL),
                 ("open", "Waarom zijn die vier zinnen de nuttigste van de hele bundel?",
                  "Met die vier kan je een gesprek voortzetten ook als je een woord niet "
                  "kent. Je vraagt het gewoon in het Frans in plaats van stil te vallen of "
                  "naar het Nederlands over te schakelen.", 3),
             ]),
    ])

# ============================================================
zet("lidwoorden-aanwijzers-bezitters-en-getallen",
    titel="Lidwoorden, aanwijzers, bezitters en getallen",
    reeksen=[
        reeks("naamwoorden-lidwoorden-en-determinanten", "Le genre"),
        reeks("naamwoorden-lidwoorden-en-determinanten", "Le pluriel"),
        reeks("naamwoorden-lidwoorden-en-determinanten",
              "Article défini, indéfini ou partitif?"),
        reeks("naamwoorden-lidwoorden-en-determinanten", "Les déterminants", weg=(2, 3)),
        dict(kop="Les nombres",
             opdracht="Schrijf het getal in woorden.",
             oefeningen=[
                 ("rij", [("17", "dix-sept"), ("21", "vingt et un"),
                          ("71", "soixante et onze"), ("80", "quatre-vingts"),
                          ("95", "quatre-vingt-quinze"), ("200", "deux cents"),
                          ("1 000", "mille")],
                  "In woorden?", WW),
                 ("rij", [("de eerste", "le premier, la première"),
                          ("de tweede", "le deuxième"), ("de vijfde", "le cinquième"),
                          ("de helft", "la moitié"), ("een kwart", "un quart")],
                  "Welk Frans woord?", WW),
                 ("kort", "Wat zeggen ze in België voor 70 en 90?",
                  "septante en nonante", WL),
             ]),
    ])

# ============================================================
zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    titel="Voornaamwoorden en betrekkelijke bijzinnen",
    reeksen=[
        dict(kop="Les pronoms sujets et toniques",
             opdracht="Vul het juiste voornaamwoord in.",
             oefeningen=[
                 ("rij", [("... suis belge. (ik)", "je"), ("... sont partis. (zij, mv.)", "ils"),
                          ("C'est pour ... . (mij)", "moi"),
                          ("... et ma sœur, nous habitons ici. (ik)", "Moi"),
                          ("Chez ... , c'est calme. (hen)", "eux")],
                  "Welk voornaamwoord?", W),
                 ("kort", "Wanneer gebruik je <em>moi</em> en niet <em>je</em>?",
                  "na een voorzetsel, na c'est, of als je het beklemtoont", WL),
             ]),
        reeks("voornaamwoorden-cod-coi-y-en-en", "COD ou COI?"),
        reeks("voornaamwoorden-cod-coi-y-en-en", "Remplace", weg=(2,)),
        reeks("voornaamwoorden-cod-coi-y-en-en", "Y et en", weg=(3,)),
        reeks("voornaamwoorden-cod-coi-y-en-en", "Les relatifs"),
    ])

# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    titel="Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    reeksen=[
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen", "L'accord"),
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen", "Avant ou après?",
              weg=(3,)),
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen", "L'adverbe"),
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen", "Les degrés"),
        dict(kop="Les prépositions",
             opdracht="Vul het juiste voorzetsel in.",
             oefeningen=[
                 ("rij", [("Je vais ... Paris.", "à Paris"), ("Je vais ... France.", "en France"),
                          ("Je viens ... Belgique.", "de Belgique"),
                          ("Il habite ... Portugal.", "au Portugal"),
                          ("Le livre est ... la table.", "sur la table"),
                          ("Le chat est ... la chaise.", "sous la chaise"),
                          ("J'attends ... midi.", "jusqu'à midi")],
                  "Welk voorzetsel?", WW),
                 ("kort", "Welk voorzetsel neem je bij een land met een vrouwelijke naam, en "
                          "welk bij een mannelijke?",
                  "en bij vrouwelijk (en France), au bij mannelijk (au Portugal)", WL),
             ]),
    ])

# ============================================================
zet("de-tegenwoordige-tijd-en-de-gebiedende-wijs",
    titel="De tegenwoordige tijd en de gebiedende wijs",
    reeksen=[
        dict(kop="Les trois groupes",
             opdracht="Vervoeg in de tegenwoordige tijd.",
             oefeningen=[
                 ("rij", [("je (parler)", "je parle"), ("nous (parler)", "nous parlons"),
                          ("tu (finir)", "tu finis"), ("ils (finir)", "ils finissent"),
                          ("il (vendre)", "il vend"), ("vous (vendre)", "vous vendez")],
                  "Welke vorm?", WW),
                 ("kort", "Welke uitgang krijgt de wij-vorm in alle drie de groepen?",
                  "-ons", W),
             ]),
        dict(kop="Les verbes irréguliers",
             opdracht="Vervoeg in de tegenwoordige tijd.",
             oefeningen=[
                 ("rij", [("je (être)", "je suis"), ("nous (avoir)", "nous avons"),
                          ("il (aller)", "il va"), ("vous (faire)", "vous faites"),
                          ("elles (pouvoir)", "elles peuvent"), ("tu (vouloir)", "tu veux"),
                          ("je (devoir)", "je dois"), ("on (venir)", "on vient"),
                          ("nous (prendre)", "nous prenons"), ("ils (savoir)", "ils savent")],
                  "Welke vorm?", WW),
                 ("kies", "Welke vorm is juist?",
                  ["vous faisez", "vous faites", "vous faitez"], 1),
             ]),
        dict(kop="Les verbes pronominaux",
             opdracht="Vervoeg het wederkerend werkwoord.",
             oefeningen=[
                 ("rij", [("je (se lever)", "je me lève"),
                          ("tu (se laver)", "tu te laves"),
                          ("il (s'habiller)", "il s'habille"),
                          ("nous (se dépêcher)", "nous nous dépêchons"),
                          ("ils (s'appeler)", "ils s'appellent")],
                  "Welke vorm?", WL),
                 ("kort", "Waar staat het wederkerend voornaamwoord in een ontkennende zin?",
                  "tussen ne en het werkwoord: je ne me lève pas", WL),
             ]),
        dict(kop="L'impératif",
             opdracht="Zet in de gebiedende wijs.",
             oefeningen=[
                 ("rij", [("tu (écouter)", "Écoute !"), ("vous (écouter)", "Écoutez !"),
                          ("nous (partir)", "Partons !"), ("tu (être) sage", "Sois sage !"),
                          ("vous (avoir) du courage", "Ayez du courage !"),
                          ("tu (se lever)", "Lève-toi !"),
                          ("tu (ne pas parler)", "Ne parle pas !")],
                  "Welke vorm?", WL),
                 ("open", "Welke twee dingen vallen weg bij de tu-vorm van de gebiedende "
                          "wijs van een -er werkwoord?",
                  "Het woordje tu verdwijnt, en de s van de uitgang: tu écoutes wordt "
                  "écoute. Bij de andere groepen blijft de s wel staan (finis).", 3),
             ]),
    ])

# ============================================================
zet("de-verleden-tijden",
    titel="De verleden tijden",
    reeksen=[
        reeks("de-verleden-tijden-en-de-accord-van-het-deelwoord", "Le participe passé"),
        reeks("de-verleden-tijden-en-de-accord-van-het-deelwoord", "Avoir ou être?", weg=(2,)),
        dict(kop="L'accord simple",
             opdracht="Vul de juiste vorm in en zeg waarom.",
             oefeningen=[
                 ("rij", [("Elle est (parti).", "partie: être, dus mee met het onderwerp"),
                          ("Les filles sont (arrivé).", "arrivées: être, meervoud vrouwelijk"),
                          ("Elle a (mangé) la pomme.", "mangé: avoir, dus geen overeenkomst"),
                          ("Ils ont (fini) le travail.", "fini: avoir, dus geen overeenkomst"),
                          ("Elles se sont (levé).",
                           "levées: wederkerend, mee met het onderwerp")],
                  "Welke vorm, en waarom?", WL),
                 ("kort", "Met welk hulpwerkwoord gaat het deelwoord mee met het onderwerp?",
                  "être", W),
             ]),
        dict(kop="L'imparfait",
             opdracht="Zet in de imparfait.",
             oefeningen=[
                 ("rij", [("je (parler)", "je parlais"), ("nous (avoir)", "nous avions"),
                          ("il (être)", "il était"), ("elles (faire)", "elles faisaient"),
                          ("tu (aller)", "tu allais"), ("on (prendre)", "on prenait")],
                  "Welke vorm?", WW),
                 ("kort", "Welk werkwoord is het enige dat zijn stam niet van de nous-vorm "
                          "haalt?", "être: j'étais", WL),
             ]),
        reeks("de-verleden-tijden-en-de-accord-van-het-deelwoord",
              "Imparfait ou passé composé?"),
    ])

# ============================================================
zet("de-toekomende-tijd-en-de-conditionnel",
    titel="De toekomende tijd en de conditionnel",
    reeksen=[
        dict(kop="Le futur proche",
             opdracht="Zet in de futur proche (aller + infinitief).",
             oefeningen=[
                 ("rij", [("je (partir)", "je vais partir"),
                          ("nous (manger)", "nous allons manger"),
                          ("il (venir)", "il va venir"),
                          ("elles (faire)", "elles vont faire"),
                          ("tu (ne pas travailler)", "tu ne vas pas travailler")],
                  "Welke vorm?", WL),
                 ("kort", "Wat is het verschil in gevoel tussen <em>je vais partir</em> en "
                          "<em>je partirai</em>?",
                  "je vais partir is dichtbij en zeker, je partirai verder weg", WL),
             ]),
        reeks("futur-conditionnel-subjonctif-en-de-gerundif", "Le futur simple"),
        reeks("futur-conditionnel-subjonctif-en-de-gerundif", "Le conditionnel"),
        dict(kop="Si...",
             opdracht="Vul de juiste tijd in.",
             oefeningen=[
                 ("rij", [("S'il fait beau, nous (sortir).", "nous sortirons"),
                          ("Si tu veux, je (venir).", "je viendrai"),
                          ("Si j'avais de l'argent, je (voyager).", "je voyagerais"),
                          ("Si elle était là, elle (aider).", "elle aiderait")],
                  "Welke vorm?", WL),
                 ("open", "Welke twee combinaties met si moet je kennen?",
                  "Si + présent met de futur in de hoofdzin voor iets dat echt kan gebeuren, "
                  "en si + imparfait met de conditionnel voor iets dat je je alleen "
                  "voorstelt.", 3),
             ]),
    ])

# ============================================================
zet("zinsbouw-zinsdelen-en-congruentie",
    titel="Zinsbouw, zinsdelen en congruentie",
    reeksen=[
        dict(kop="Les parties de la phrase",
             opdracht="Onderstreep het onderwerp en schrijf het werkwoord erbij.",
             oefeningen=[
                 ("rij", [("Les enfants jouent dans le jardin.", "les enfants — jouent"),
                          ("Mon frère et moi partons demain.", "mon frère et moi — partons"),
                          ("La plupart des élèves sont arrivés.",
                           "la plupart des élèves — sont"),
                          ("Il y a trois livres sur la table.", "il — y a"),
                          ("Ma sœur, qui habite à Gand, vient ce soir.", "ma sœur — vient")],
                  "Onderwerp en werkwoord?", WL),
                 ("kort", "Wat is de gewone orde van een Franse mededelende zin?",
                  "onderwerp, werkwoord, voorwerp, dan de rest", WL),
             ]),
        reeks("zinsbouw-indirecte-rede-en-de-passieve-zin", "La question"),
        reeks("zinsbouw-indirecte-rede-en-de-passieve-zin", "La négation"),
        dict(kop="La congruence",
             opdracht="Verbeter de zin en zeg welke regel je toepast.",
             oefeningen=[
                 ("rij", [("Les élèves est content.",
                           "sont contents: werkwoord en bijvoeglijk naamwoord in het meervoud"),
                          ("Ma sœur est parti.", "partie: être, dus mee met het onderwerp"),
                          ("Les filles sont petit.", "petites: meervoud vrouwelijk"),
                          ("Mon frère et moi est arrivé.",
                           "nous sommes arrivés: twee personen, dus nous"),
                          ("Elle a des yeux bleu.", "bleus: meervoud")],
                  "Hoe hoort het, en waarom?", WL),
                 ("open", "Welke drie dingen kijk je na in elke zin die je schrijft?",
                  "Of het werkwoord bij het onderwerp past, of het bijvoeglijk naamwoord "
                  "meegaat in geslacht en getal, en of het deelwoord na être meegaat met het "
                  "onderwerp.", 3),
             ]),
    ])

_ORDE = ["een-franse-tekst-lezen", "tekstsoorten-en-de-bedoeling-van-een-tekst",
         "de-franstalige-wereld-gewoontes-en-reizen", "schrijven-en-spreken-in-het-frans",
         "woordvelden-dagelijks-leven-eten-en-wonen",
         "woordvelden-gezondheid-natuur-en-milieu",
         "woordvelden-school-werk-geld-en-verkeer",
         "woordvelden-kunst-geschiedenis-en-de-samenleving",
         "woordvelden-wetenschap-techniek-en-taal",
         "lidwoorden-aanwijzers-bezitters-en-getallen",
         "voornaamwoorden-en-betrekkelijke-bijzinnen",
         "bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
         "de-tegenwoordige-tijd-en-de-gebiedende-wijs", "de-verleden-tijden",
         "de-toekomende-tijd-en-de-conditionnel", "zinsbouw-zinsdelen-en-congruentie"]
assert sorted(_ORDE) == sorted(s[len(VOOR):-len(NIVEAU)] for s in OEFENBUNDELS), \
    "orde klopt niet met de bundels"
OEFENBUNDELS = {VOOR + s + NIVEAU: OEFENBUNDELS[VOOR + s + NIVEAU] for s in _ORDE}

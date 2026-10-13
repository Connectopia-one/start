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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-franse-tekst-lezen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder woordenboek, en onderstreep "
                   "daarna de cijfers en de namen. Daar gaan de vragen over.",
            waarom=[],
        ),
        dict(
            aanpak="Elk antwoord staat in de tekst. Zoek de alinea terug en antwoord met wat daar "
                   "staat; een korte volledige zin is genoeg.",
            waarom=[
                "In Namen, dus Namur in het Frans. Let op de Franse namen van onze steden: Namur, "
                "Liège, Anvers, Gand, Bruges, Louvain.",
                "Noem beide redenen, want ze geeft er twee: sneller in de stad, en geen "
                "parkeerplaats zoeken. Eén van de twee is maar de helft.",
                None,
                "Noem ook wat ze niet doen, want dat is uitdrukkelijk gevraagd. Dat ze het werk "
                "niet in jouw plaats doen, is het hele idee van zo'n café.",
                "Een cake, un gâteau. Dat detail zegt iets over de sfeer: je betaalt er niet, je "
                "brengt iets mee.",
                "Noem beide: een knoop aanzetten en een broek korter maken. Zo zie je dat ze van "
                "iemand die geholpen werd, iemand is geworden die helpt.",
            ],
        ),
        dict(
            aanpak="Zoek het Franse woord in de tekst zelf terug in plaats van het uit je hoofd te "
                   "vertalen. Zo leer je het in zijn context, en dat blijft beter hangen.",
            waarom=[
                "Let op un bénévole: een vrijwilliger, van bene en volo, goed willen. En se garer "
                "is wederkerend, dus met se, terwijl wij gewoon parkeren zeggen.",
                "Stuk vallen of niet meer werken. Het is een vaste uitdrukking, dus niet woord voor "
                "woord te vertalen, en ze geldt voor een auto, een fiets en een machine.",
            ],
        ),
        dict(
            aanpak="Bij waar of niet waar moet je de plaats in de tekst aanwijzen. Let op de kleine "
                   "woordjes: chaque matin, une fois par semaine, encore. Daar zit het verschil.",
            waarom=[
                "Niet waar: chaque matin, dus elke ochtend en niet één keer per week. Zulke vragen "
                "testen of je het bijwoord van tijd gelezen hebt.",
                None,
                "Niet waar: de winkel vroeg tachtig euro, en dat is precies de reden dat ze naar "
                "het Repair Café ging. Let op wie wat vroeg.",
                None,
            ],
        ),
        dict(
            aanpak="Hier staat het antwoord niet in de tekst. Lees het citaat nog eens en vraag je "
                   "af waarom zij dat zegt, met wat je over haar weet.",
            waarom=[
                "Noem dat ze iets over haar leeftijd en haar nut zegt. Elk antwoord dat je met de "
                "tekst kan verdedigen is goed, zolang je erbij zegt waaruit je het haalt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-en-de-bedoeling-van-een-tekst-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je telkens af wat de tekst van jou wil: iets weten, iets doen, iets "
                   "vinden, of meegaan in een verhaal. Dat doel bepaalt de soort, niet het "
                   "onderwerp.",
            waarom=[
                "Let op het verschil tussen prescriptif en persuasif: een recept zegt stap voor "
                "stap wat je moet doen, een advertentie wil je overtuigen. En tussen informatif en "
                "argumentatif: een artikel brengt feiten, een open brief verdedigt een standpunt.",
                "Aan de imperatief en de genummerde stappen: mélangez, ajoutez, laissez cuire. Dat "
                "is de snelste herkenning van alle zes.",
            ],
        ),
        dict(
            aanpak="Een feit kan je nakijken, een mening niet. Zoek dus naar woorden die een "
                   "waardering uitdrukken: een overtreffende trap, à mon avis, clairement.",
            waarom=[
                "De eerste, derde en vijfde noemen een jaartal, een verhouding en een bedrag: alle "
                "drie na te kijken. Let op: een feit hoeft niet juist te zijn om een feit te zijn, "
                "het moet enkel te controleren zijn.",
                "Le plus beau is een overtreffende trap van een smaakoordeel, en à mon avis zegt "
                "zelf dat het een mening is. Juist dat soort woorden zoek je.",
            ],
        ),
        dict(
            aanpak="Een verbindingswoord moet passen bij de verhouding tussen de twee delen: "
                   "tegenstelling, gevolg, voorwaarde of reden. Lees de zin dus eerst zonder het "
                   "woord en bepaal welke van de vier het is.",
            waarom=[
                "Let op pourtant en cependant: beide betekenen nochtans of toch, en ze staan bij "
                "een tegenstelling. Donc en c'est pourquoi staan bij een gevolg, en parce que bij "
                "een reden.",
                "Let op en revanche: daarentegen, dus een tegenstelling, terwijl en outre erbij "
                "optelt. Deze vier woorden staan vooraan in de zin en maken je tekst "
                "overzichtelijk.",
            ],
        ),
        dict(
            aanpak="Elke tekstsoort heeft haar eigen plaats. Vraag je af waar zoiets fysiek "
                   "terechtkomt: in een doosje, in een brievenbus, op een bord in het station.",
            waarom=[
                "Let op un faire-part: een kaartje bij een geboorte, een huwelijk of een "
                "overlijden. En un mode d'emploi is de handleiding, letterlijk de manier van "
                "gebruiken.",
                "Iets kopen of ergens naartoe gaan. Een advertentie wil dus niet dat je iets weet "
                "maar dat je iets doet, en dat is wat ze persuasif maakt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-franstalige-wereld-gewoontes-en-reizen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee vragen beslissen: ken ik deze persoon, en is hij van mijn leeftijd? Twee "
                   "keer ja geeft tu, voor de rest neem je vous. In twijfel is vous altijd de "
                   "veilige keuze.",
            waarom=[
                "Let op de moeder van een vriend: ouder dan jij en niet echt bekend, dus vous. En "
                "in elke werkrelatie begin je met vous, ook bij iemand van je eigen leeftijd.",
            ],
        ),
        dict(
            aanpak="Deze woorden hoor je in elk gesprek en in elke film, maar ze hebben geen "
                   "letterlijke Nederlandse tegenhanger. Leer ze met het moment of het gebruik "
                   "erbij.",
            waarom=[
                "Let op la rentrée: niet enkel de eerste schooldag maar de hele terugkeer na de "
                "zomer, ook op het werk. En le bac is het Franse eindexamen van het secundair; "
                "Belgie heeft dat niet.",
                "De veertiende juli, de bestorming van de Bastille in 1789. In Belgie is het 21 "
                "juli, en dat is een handige vergelijking.",
                "Bonjour. In Frankrijk is een vraag zonder bonjour onbeleefd, ook aan een loket of "
                "in een winkel. Het is het woord dat de deur opent.",
            ],
        ),
        dict(
            aanpak="Frans is niet van Frankrijk alleen. Leer bij elk gebied één voorbeeld, en leer "
                   "de varianten als paar: de Belgische of Canadese vorm naast de Franse.",
            waarom=[
                "Let op Marokko: Frans is daar geen officiële taal, want dat zijn het Arabisch en "
                "het Amazigh, maar het wordt veel gebruikt in het onderwijs en het bestuur. Senegal "
                "en de Democratische Republiek Congo hebben het wel als officiële taal.",
                "Let op septante en nonante: die gebruiken wij en de Zwitsers, Frankrijk zegt "
                "soixante-dix en quatre-vingt-dix. La fin de semaine is Quebecs, want daar vermijdt "
                "men Engelse woorden veel meer.",
            ],
        ),
        dict(
            aanpak="Op reis heb je een handvol vaste zinnen nodig. Begin met pardon of excusez-moi, "
                   "eindig met s'il vous plaît, en je komt er in elke situatie.",
            waarom=[
                "Let op combien ça coûte: in de spreektaal met ça, terwijl combien est-ce que cela "
                "coûte formeler is. En j'ai raté mon train: rater is missen, van een trein of een "
                "afspraak.",
                "Let op le quai: het perron, en ook de kade aan het water. En la douane is de "
                "douane, met un douanier als beambte.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-en-spreken-in-het-frans-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een tekst zonder opbouw leest als een lijst. Weet dus voor je begint wat je "
                   "eerste en wat je laatste zin wordt.",
            waarom=[
                None,
                "Un paragraphe, met een ph. Let op dat une phrase een zin is en geen alinea; die "
                "twee worden het vaakst verward.",
            ],
        ),
        dict(
            aanpak="Een formele mail in het Frans ligt veel vaster dan bij ons. Leer de aanspreking "
                   "en de slotformule letterlijk vanbuiten, dan hoef je enkel het midden te "
                   "bedenken.",
            waarom=[
                "Let op Madame, Monsieur zonder naam als je niet weet wie het leest, met een komma "
                "erachter. En de slotformule staat altijd apart op haar eigen regel, vóór je naam.",
                "Begin met de aanspreking en dan onmiddellijk je reden. In een Franse mail val je "
                "niet met de deur in huis, maar je draait er ook niet drie zinnen omheen.",
            ],
        ),
        dict(
            aanpak="De conditionnel maakt een vraag hoffelijk: je voudrais in plaats van je veux, "
                   "pourriez-vous in plaats van vous pouvez. Herken hem aan de uitgang -rais of "
                   "-riez.",
            waarom=[
                "Let op j'aimerais: dat is de conditionnel van aimer en niet de tegenwoordige tijd "
                "j'aime. En een gebiedende wijs zoals donnez-moi klinkt in het Frans erg direct, "
                "dus die vervang je het best helemaal door een vraag.",
            ],
        ),
        dict(
            aanpak="Telefoneren is het moeilijkste deel, want je ziet de ander niet. Zorg dat je de "
                   "zin om iets te laten herhalen klaar hebt voor je belt.",
            waarom=[
                "Let op c'est ... à l'appareil: letterlijk aan het toestel, en dat is de vaste "
                "manier om je naam te zeggen. Pardon vooraan maakt je vraag om te herhalen "
                "vriendelijk.",
                "Noem dat je blijft praten in plaats van stil te vallen. Comment dit-on ... en "
                "français is de zin die je uit elke blokkade haalt, en een goede spreker gebruikt "
                "hem zonder schaamte.",
            ],
        ),
        dict(
            aanpak="Lees je tekst een laatste keer met één vraag per keer: staan alle werkwoorden "
                   "juist, en komt alles overeen in getal en geslacht. Twee korte rondes vinden meer "
                   "dan één algemene.",
            waarom=[
                "Let op elle est allée: aller hoort bij de werkwoorden met être, en dan gaat het "
                "deelwoord mee met het onderwerp. En nous mangeons krijgt een e, want zonder die e "
                "zou de g hard klinken.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-dagelijks-leven-eten-en-wonen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de woorden van je eigen dag in de orde waarin je ze doet. Zo heb je een "
                   "ketting in plaats van een lijst.",
            waarom=[
                "Let op dat se lever, se laver, s'habiller en se coucher wederkerend zijn: in de "
                "passé composé nemen ze être, dus je me suis levé. Prendre le petit déjeuner is "
                "ontbijten; déjeuner alleen is in Frankrijk middagmalen.",
                "Let op jamais en parfois: die zetten de hele zin in een ander licht, en ze staan "
                "meestal na het werkwoord. Hier is gisteren en niet hier zoals in het Nederlands.",
                "Schrijf in de passé composé, want het gaat over vanmorgen. Zet er een verbindings"
                "woord tussen, bijvoorbeeld puis of ensuite, dan is het al een tekst in plaats van "
                "drie losse zinnen.",
            ],
        ),
        dict(
            aanpak="Een bijvoeglijk naamwoord over een persoon moet mee met die persoon: gentil "
                   "wordt gentille, content wordt contente. Leer dus telkens beide vormen.",
            waarom=[
                "Let op un cousin en une cousine: het Frans maakt onderscheid tussen een neef en "
                "een nicht, wij niet. En timide is zowel mannelijk als vrouwelijk, want het eindigt "
                "al op een e.",
            ],
        ),
        dict(
            aanpak="Leer de maaltijden en het bestek samen met het werkwoord dat erbij hoort: "
                   "mettre la table, débarrasser, faire la vaisselle.",
            waarom=[
                "Let op à emporter: dat lees je op elke Franse winkelruit, naast sur place voor ter "
                "plaatse eten. Une entrée is een voorgerecht en niet de ingang, al is dat hetzelfde "
                "woord.",
                "Noem beide, want juist dat verschil levert misverstanden op. Bij ons is le dîner "
                "het middagmaal, in Frankrijk het avondmaal, en daar heet het middagmaal le "
                "déjeuner.",
            ],
        ),
        dict(
            aanpak="In een winkel gaat bijna elke zin over een hoeveelheid. Leer de maten en het "
                   "woordje dat erbij hoort als één geheel.",
            waarom=[
                "Let op une boîte d'œufs met d' omdat œufs met een klinker begint. En la monnaie is "
                "het wisselgeld of de munt, terwijl l'argent het geld in het algemeen is.",
                "De of d' voor een klinker. Dus un kilo de pommes zonder lidwoord, nooit un kilo "
                "des pommes: dat is de fout die iedereen één keer maakt.",
            ],
        ),
        dict(
            aanpak="Wonen heeft zijn eigen woordenlijst. Leer de twee rollen samen, want ze komen "
                   "altijd in paar voor: le locataire en le propriétaire.",
            waarom=[
                "Let op le rez-de-chaussée: het gelijkvloers, en de verdieping erboven is le "
                "premier étage. Wat wij de eerste verdieping noemen, is dus hetzelfde, maar het "
                "gelijkvloers telt niet mee.",
                "Let op une tâche met een accent: een taak of klusje, terwijl une tache zonder "
                "accent een vlek is. Eén streepje verschil geeft een heel andere zin.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-gezondheid-natuur-en-milieu-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij de dokter draait bijna alles om één bouwsteen: avoir mal à. Zet die vast en "
                   "je kan elke klacht zeggen.",
            waarom=[
                "Let op une ordonnance: het voorschrift van de dokter, en daarmee ga je naar la "
                "pharmacie. Un médecin généraliste is de huisarts, un spécialiste de specialist.",
                "Noem de juiste vorm erbij. Het Frans zegt waar je pijn hebt met avoir mal à, dus "
                "j'ai mal à la tête, j'ai mal au dos, j'ai mal aux dents, en niet met een bezittend "
                "woord zoals wij.",
            ],
        ),
        dict(
            aanpak="Leer bij elk lichaamsdeel ook het lidwoord, want dat beslist of het à la, au of "
                   "aux wordt in de klachtzin.",
            waarom=[
                "Let op l'œil met het meervoud les yeux: dat is onregelmatig en het staat in elk "
                "examen. En la dent is vrouwelijk, dus j'ai mal aux dents in het meervoud.",
                None,
            ],
        ),
        dict(
            aanpak="Het weer heeft in het Frans zijn eigen vorm: il fait, il y a of één werkwoord "
                   "alleen. Leer de drie soorten apart.",
            waarom=[
                "Let op une rivière en un fleuve: een fleuve mondt uit in de zee, een rivière in "
                "een andere rivier. De Maas is un fleuve, de Demer une rivière.",
                "Let op il gèle en il pleut: die hebben geen faire nodig, want het werkwoord zegt "
                "zelf al wat het weer doet. Il y a du vent gebruikt dan weer il y a.",
                "Faire, in de vorm il fait. Il fait beau, il fait froid, il fait du soleil: met die "
                "ene bouwsteen kan je het grootste deel van een weerbericht zeggen.",
            ],
        ),
        dict(
            aanpak="De milieuwoorden lijken op onze eigen woorden, maar let op het geslacht en op "
                   "het meervoud: les déchets staat altijd in het meervoud.",
            waarom=[
                "Let op la consommation: het verbruik, en consommer verbruiken. Trier is sorteren, "
                "en dat woord staat op elke Franse vuilnisbak.",
                "Gebruik on of nous als je over het gezin spreekt, en je als je over jezelf "
                "spreekt. Drie zinnen met een werkwoord in de tegenwoordige tijd volstaan; het gaat "
                "om wat je gewoonlijk doet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-geld-en-verkeer-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="School en werk gebruiken dezelfde soort woorden: een vak, een uurrooster, een "
                   "gesprek, een papier dat bewijst wat je kan. Leer ze naast elkaar.",
            waarom=[
                "Let op une matière: een vak op school, en ook een stof of materiaal. En la "
                "récréation is de pauze op school; een pauze op het werk is une pause.",
                "Let op postuler pour un emploi: solliciteren, en un entretien is het gesprek dat "
                "erop volgt. Au chômage is werkloos, en être licencié is ontslagen worden, dus het "
                "overkomt je.",
            ],
        ),
        dict(
            aanpak="Rond geld hangen vaste zinnetjes die je aan een kassa hoort. Leer de vraag en "
                   "het antwoord samen, dan kan je echt afrekenen.",
            waarom=[
                "Let op emprunter en prêter: emprunter is lenen van iemand, prêter is uitlenen aan "
                "iemand. En l'addition is de rekening in een restaurant, la facture een factuur.",
                "Let op Vous avez la monnaie: dat vraagt of je het gepast hebt of klein geld hebt, "
                "niet of je geld hebt. Ça coûte combien is de spreektaalvorm van combien est-ce que "
                "cela coûte.",
            ],
        ),
        dict(
            aanpak="Een weg uitleggen vraagt maar een handvol werkwoorden. Leer tourner, aller tout "
                   "droit en traverser, en zet er jusqu'à bij om te zeggen tot waar.",
            waarom=[
                "Let op le feu: het verkeerslicht, en ook het vuur. En l'embouteillage is de file, "
                "van une bouteille, dus letterlijk het flessenhals-effect.",
                "Let op tout droit en à droite: tout droit is rechtdoor, à droite is naar rechts. "
                "Dat is de verwarring die iemand letterlijk de verkeerde kant op stuurt.",
                "Gebruik tu met het werkwoord in de tegenwoordige tijd, dat is de gewone manier om "
                "een weg uit te leggen. Zet er jusqu'au feu of jusqu'à l'église bij, dan weet de "
                "ander waar hij moet stoppen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-kunst-geschiedenis-en-de-samenleving-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Over kunst spreken is vooral zeggen wat je ervan vindt. Leer naast de woorden "
                   "voor de dingen ook de vier zinnen om je mening te geven.",
            waarom=[
                "Let op un tableau: een schilderij, en ook het bord in de klas. Une pièce de "
                "théâtre is een toneelstuk; une pièce alleen is een kamer of een stuk.",
                "Let op Ça me plaît: letterlijk het bevalt mij, dus het ding is het onderwerp en "
                "niet jij. En Ça ne me dit rien is een vaste uitdrukking: het zegt mij niets, het "
                "trekt mij niet aan.",
            ],
        ),
        dict(
            aanpak="Geschiedenis vraagt jaartallen, en die zeg je in het Frans met de volle "
                   "honderden. Oefen er een paar luidop, want geschreven lijken ze makkelijker dan "
                   "ze klinken.",
            waarom=[
                "Let op un siècle: een eeuw, en le dix-neuvième siècle is de negentiende eeuw, dus "
                "van 1801 tot 1900. Un événement heeft twee accenten, beide naar rechts.",
                "Mille neuf cent quatorze, dus duizend negenhonderd veertien. Je kan ook dix-neuf "
                "cent quatorze horen, maar de eerste vorm is de veiligste om te schrijven.",
            ],
        ),
        dict(
            aanpak="De woorden over de samenleving staan in elke krant. Leer er telkens het "
                   "werkwoord bij: une élection en élire, une manifestation en manifester.",
            waarom=[
                "Let op la commune: de gemeente, en le conseil communal de gemeenteraad. Faire du "
                "bénévolat is vrijwilligerswerk doen, van un bénévole, een vrijwilliger.",
                "Gebruik à mon avis vooraan en parce que in de tweede of derde zin, want dat is "
                "precies wat gevraagd is. Welk onderwerp je kiest maakt niet uit, zolang je je "
                "mening onderbouwt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-wetenschap-techniek-en-taal-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Techniek bestaat vooral uit werkwoorden in de gebiedende wijs: aanzetten, "
                   "uitdoen, insteken. Leer de paren samen, dan ken je er twee tegelijk.",
            waarom=[
                "Let op le mot de passe: letterlijk het woord om te passeren. En la batterie is de "
                "batterij van een toestel; une pile is een losse batterij die je koopt.",
                "Let op allumer en éteindre: aanzetten en uitdoen, en die twee gelden voor een licht "
                "en voor een toestel. Ça ne marche pas betekent het werkt niet, al betekent marcher "
                "ook stappen.",
            ],
        ),
        dict(
            aanpak="De wetenschapswoorden lijken op onze eigen, maar de werkwoorden zijn anders: "
                   "mesurer, peser, calculer. Leer bij elk het zelfstandig naamwoord: la mesure, le "
                   "poids, le calcul.",
            waarom=[
                "Let op le poids: met een d die je niet hoort, van peser. En la température heeft "
                "twee accenten, allebei naar rechts.",
                "Noem beide betekenissen, want dat is de hele vraag. Une expérience is een proef in "
                "het labo en ook ervaring, en enkel de zin eromheen maakt duidelijk welke van de "
                "twee bedoeld is.",
            ],
        ),
        dict(
            aanpak="Dit zijn de woorden waarmee je over de taal zelf spreekt. Je hebt ze nodig in "
                   "de klas, en vooral om een gesprek verder te zetten als je iets niet begrijpt.",
            waarom=[
                "Let op une phrase: een zin, en niet een frase of een alinea. En une faute is een "
                "fout; une erreur kan ook een vergissing in een berekening zijn.",
                "Let op Comment ça s'écrit: met het wederkerende s', want het Frans zegt hoe schrijft "
                "dat zich. En Qu'est-ce que ça veut dire is letterlijk wat wil dat zeggen.",
                "Noem dat je met die vier in het Frans kan blijven. Dat is precies wat een "
                "taalexamen spreken beoordeelt: niet of je alles kent, maar of je verder kan zonder "
                "over te schakelen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-lidwoorden-aanwijzers-bezitters-en-getallen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het geslacht van een Frans woord zit vaak in zijn uitgang. Leer de vier "
                   "grootste groepen, dan hoef je veel minder vanbuiten te leren.",
            waarom=[
                "Let op le problème: ondanks de e op het einde is het mannelijk, net als le système "
                "en le programme. En l'eau is vrouwelijk, wat je enkel ziet aan de la belle eau, "
                "want het lidwoord verdwijnt voor de klinker.",
                "De uitgang -tion, zoals la nation, la question, la solution. Daartegenover zijn "
                "-age en -ment bijna altijd mannelijk: le voyage, le silence hoort bij een derde "
                "groep op -ence, die vrouwelijk is behalve enkele uitzonderingen zoals le silence.",
            ],
        ),
        dict(
            aanpak="De gewone regel is een s erbij, maar een handvol uitgangen doen iets anders. "
                   "Leer die apart, want ze komen heel vaak voor.",
            waarom=[
                "Let op de drie groepen: -al wordt -aux (un journal, un cheval), -ail wordt soms "
                "-aux (un travail), en -eau wordt -eaux. Un oeil wordt des yeux, en dat is volledig "
                "onregelmatig.",
                "Het blijft hetzelfde. Un prix, des prix; un nez, des nez. Alleen het lidwoord "
                "verraadt dan het meervoud, dus lees dat goed.",
            ],
        ),
        dict(
            aanpak="Vraag je per zin af welk van de drie je nodig hebt: de hele soort (le), een "
                   "ervan (un), of een deel ervan (du). Het werkwoord helpt: aimer vraagt le, "
                   "manger en boire vragen du.",
            waarom=[
                "Let op J'aime le fromage: bij aimer gebruik je het bepaald lidwoord, want je houdt "
                "van de kaas in het algemeen. Bij boire en acheter neem je het delend lidwoord: je "
                "bois de l'eau, il achète du pain.",
                "Du, de la en des worden de of d' in een ontkenning. Dus je ne mange pas de viande, "
                "en niet pas de la viande. Het bepaald lidwoord verandert wel niet: je n'aime pas "
                "le fromage blijft.",
            ],
        ),
        dict(
            aanpak="Een aanwijzer en een bezitter komen altijd vooraan en gaan mee met het woord "
                   "erachter, niet met de persoon. Kijk dus naar het naamwoord.",
            waarom=[
                "Let op cet arbre: voor een mannelijk woord dat met een klinker begint neem je cet, "
                "niet ce en niet cette. En leur décision heeft geen s, want er is maar één "
                "beslissing; leurs décisions zou meerdere zijn.",
            ],
        ),
        dict(
            aanpak="De Franse getallen boven zestig rekenen. Schrijf er een paar voluit tot je de "
                   "koppeltekens en de s automatisch zet.",
            waarom=[
                "Let op de s: quatre-vingts en deux cents krijgen een s omdat er niets achter komt, "
                "maar quatre-vingt-quinze verliest hem weer. Mille krijgt nooit een s. En soixante "
                "et onze schrijft et, net als vingt et un.",
                "Let op le premier met zijn vrouwelijke vorm la première; de andere rangtelwoorden "
                "maken gewoon -ième. La moitié is de helft als hoeveelheid, un demi is een half in "
                "een berekening.",
                "Septante en nonante, net als in Zwitserland. Frankrijk zegt soixante-dix en "
                "quatre-vingt-dix, en beide vormen zijn juist Frans; in een examen schrijf je het "
                "best de Franse vorm.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-en-betrekkelijke-bijzinnen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Frans heeft twee reeksen: de korte vormen bij het werkwoord (je, tu, il) en "
                   "de lange vormen die alleen kunnen staan (moi, toi, lui). Vraag je af of het "
                   "voornaamwoord tegen een werkwoord aan staat.",
            waarom=[
                "Let op Moi et ma soeur, nous habitons ici: de lange vorm vooraan, en daarna nog "
                "eens nous bij het werkwoord. Dat dubbele is in het Frans juist en bij ons niet.",
                "Noem alle drie de gevallen. Na een voorzetsel (pour moi, chez eux), na c'est "
                "(c'est moi) en bij nadruk (moi, je pense que...). In alle andere gevallen staat de "
                "korte vorm bij het werkwoord.",
            ],
        ),
        dict(
            aanpak="Het verschil tussen COD en COI zit in één woordje: staat er à voor het "
                   "voorwerp. Zonder à is het een COD, met à een COI.",
            waarom=[
                "Let op téléphoner à en répondre à: in het Frans met à, bij ons zonder voorzetsel. "
                "Juist bij die werkwoorden kies je dan lui of leur en niet le of la.",
                "Noem beide vragen. Je vois qui of je vois quoi geeft het COD, je parle à qui geeft "
                "het COI. Die ene toets beslist later of je le of lui schrijft.",
            ],
        ),
        dict(
            aanpak="Het voornaamwoord komt vóór het werkwoord, ook in een ontkenning en in de passé "
                   "composé. Kijk eerst of het voorwerp een COD of een COI was.",
            waarom=[
                "Let op Je l'ai vu: het voornaamwoord staat voor de hulpwerkwoordsvorm ai en niet "
                "voor vu. En bij een ontkenning gaat het ertussen: elle ne le connaît pas.",
            ],
        ),
        dict(
            aanpak="Y en en nemen elk hun eigen soort voorwerp over. Kijk naar het voorzetsel in de "
                   "oorspronkelijke zin: à geeft y, de geeft en.",
            waarom=[
                "Let op Elle en a trois: en vervangt ook een hoeveelheid, en dan blijft het getal "
                "staan. En avoir besoin de wordt en as besoin, want het voorzetsel is de.",
                "Noem het voorzetsel bij elk. Y hoort bij à en bij een plaats, en hoort bij de, du, "
                "de la, des en bij hoeveelheden. Dat is de hele regel, en met die ene toets kan je "
                "altijd kiezen.",
            ],
        ),
        dict(
            aanpak="Zoek bij elk betrekkelijk woord wat er onmiddellijk achter komt. Volgt er een "
                   "werkwoord, dan is het qui; volgt er een onderwerp, dan is het que.",
            waarom=[
                "Let op dont: dat staat waar het Nederlands waarover of waarvan zegt, dus bij een "
                "werkwoord of een naamwoord met de. Parler de iets wordt dont tout le monde parle.",
                "Noem de toets zelf. Qui als er geen onderwerp volgt, want qui is dan het "
                "onderwerp; que als er wel een onderwerp volgt, want que is dan het voorwerp. Voor "
                "een klinker wordt que qu'.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Maak eerst de vrouwelijke vorm, en zet daarna pas de s voor het meervoud. In "
                   "die orde maak je veel minder fouten.",
            waarom=[
                "Let op de groepen: -eux wordt -euse (heureux, heureuse), -il verdubbelt de l "
                "(gentil, gentille), en blanc wordt blanche. Vieux en frais zijn apart: vieille en "
                "fraîche. Des murs vieux blijft vieux, want het meervoud mannelijk verandert niet.",
            ],
        ),
        dict(
            aanpak="De meeste Franse bijvoeglijke naamwoorden komen achter het naamwoord. Enkel een "
                   "kleine groep korte, veelgebruikte woorden gaat ervoor.",
            waarom=[
                "Let op une belle histoire: beau wordt belle voor een vrouwelijk woord, en het "
                "staat vooraan. Een kleur en een nationaliteit staan altijd achteraan: une voiture "
                "rouge, un plat italien.",
                "Noem de groep en geef er voorbeelden bij. Het zijn de korte, veelgebruikte: beau, "
                "bon, grand, petit, jeune, vieux, nouveau, joli, mauvais. Alle andere komen "
                "achteraan.",
            ],
        ),
        dict(
            aanpak="Een bijwoord maak je uit de vrouwelijke vorm plus -ment. Twee uitgangen doen "
                   "iets anders, en twee woorden zijn volledig onregelmatig.",
            waarom=[
                "Let op évidemment en couramment: bij -ent en -ant wordt het -emment en -amment, en "
                "die klinken allebei als -amment. En vraiment verliest de e van vraie.",
                "De vrouwelijke vorm. Lente geeft lentement, heureuse geeft heureusement. Bon en "
                "mauvais vallen buiten de regel: die geven bien en mal.",
            ],
        ),
        dict(
            aanpak="Vergelijken gaat met plus, moins of aussi, en daarna que. Drie woorden hebben "
                   "een eigen vorm en die moet je kennen.",
            waarom=[
                "Let op de drie onregelmatige: bon wordt meilleur, bien wordt mieux, mauvais wordt "
                "pire. Meilleur hoort bij een naamwoord, mieux bij een werkwoord: un meilleur livre, "
                "il travaille mieux.",
                "Plus bon bestaat niet, en plus meilleur is dubbel. Meilleur is zelf al de "
                "vergrotende trap van bon, dus er mag geen plus bij.",
                "Que. Plus grand que, moins cher que, aussi cher que. Bij een overtreffende trap "
                "neem je de: le plus grand de la classe.",
            ],
        ),
        dict(
            aanpak="Bij een stad hoort à, bij een land hangt het van het geslacht af. Leer de drie "
                   "vormen als een rijtje: à Paris, en France, au Portugal.",
            waarom=[
                "Let op de drie reeksen: à bij een stad, en bij een vrouwelijk land, au bij een "
                "mannelijk land en aux bij een meervoud (aux Pays-Bas). Komen uit een land is de of "
                "du: je viens de Belgique, je viens du Portugal.",
                "Noem beide met een voorbeeld. En bij een vrouwelijk land, dus en France en en "
                "Belgique, en au bij een mannelijk land, dus au Portugal en au Canada. Een land dat "
                "op een e eindigt is bijna altijd vrouwelijk; le Mexique is de bekende uitzondering.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijd-en-de-gebiedende-wijs-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk eerst naar de uitgang van het hele werkwoord: -er, -ir of -re. Die bepaalt "
                   "welk rijtje uitgangen je neemt.",
            waarom=[
                "Let op tu finis en ils finissent: de werkwoorden op -ir schuiven een -iss- in bij "
                "de meervoudsvormen. En il vend eindigt op een d die je niet hoort, zonder uitgang.",
                "De uitgang -ons. Nous parlons, nous finissons, nous vendons; en zelfs bij de "
                "onregelmatige werkwoorden blijft het -ons, met être als enige uitzondering (nous "
                "sommes).",
            ],
        ),
        dict(
            aanpak="Deze tien werkwoorden komen in bijna elke zin voor. Leer ze volledig vanbuiten, "
                   "want regels helpen hier niet.",
            waarom=[
                "Let op elles peuvent, tu veux en ils savent: pouvoir, vouloir en savoir veranderen "
                "van klank in het meervoud. En on vient staat in het enkelvoud, ook al betekent on "
                "vaak wij.",
                "Faire hoort bij de drie werkwoorden met een vous-vorm op -tes: vous faites, vous "
                "dites, vous êtes. Alle andere werkwoorden hebben -ez.",
            ],
        ),
        dict(
            aanpak="Een wederkerend werkwoord heeft twee delen: het voornaamwoord en het werkwoord. "
                   "Vervoeg beide, want het voornaamwoord verandert mee met de persoon.",
            waarom=[
                "Let op nous nous dépêchons: twee keer nous, en dat is juist. En ils s'appellent "
                "verdubbelt de l, net als je m'appelle.",
                "Tussen ne en het werkwoord, dus je ne me lève pas. Het voornaamwoord blijft altijd "
                "tegen het werkwoord aan plakken, ook in een ontkenning.",
            ],
        ),
        dict(
            aanpak="De gebiedende wijs is de vervoegde vorm zonder het voornaamwoord ervoor. Enkel "
                   "être en avoir hebben een eigen vorm.",
            waarom=[
                "Let op Lève-toi: in een bevel komt het voornaamwoord erachter met een streepje, en "
                "te wordt toi. In een ontkenning gaat het weer vooraan: ne te lève pas.",
                "Noem beide. Het woordje tu valt weg en bij een werkwoord op -er valt ook de s weg: "
                "tu écoutes wordt écoute. Bij finir blijft de s wel staan, dus finis.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-verleden-tijden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De deelwoorden van de -er werkwoorden zijn makkelijk (-é), maar de "
                   "onregelmatige moet je stuk per stuk kennen. Leer ze in groepjes met dezelfde "
                   "uitgang.",
            waarom=[
                "Let op de groepen: pris, mis en écrit eindigen op een letter die je niet hoort; "
                "ouvert en mort op -t; venu, vécu en dû op -u. Dû draagt een accent om hem van het "
                "lidwoord du te onderscheiden.",
            ],
        ),
        dict(
            aanpak="Bijna alles neemt avoir. Alleen de werkwoorden van beweging en verandering van "
                   "toestand nemen être, en alle wederkerende werkwoorden ook.",
            waarom=[
                "Let op il a descendu l'escalier: descendre neemt normaal être, maar met een lijdend "
                "voorwerp erachter neemt het avoir. Hetzelfde geldt voor monter, sortir en passer.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist alles: welk hulpwerkwoord staat er. Bij être gaat het "
                   "deelwoord mee met het onderwerp, bij avoir niet.",
            waarom=[
                "Let op Elle a mangé la pomme: geen e aan mangé, ook al is elle vrouwelijk, want "
                "het hulpwerkwoord is avoir. Dat voelt fout en is juist het punt van de oefening.",
                "Être. Elle est partie, ils sont restés, elles sont arrivées. Bij avoir blijft het "
                "deelwoord onveranderd, behalve als het lijdend voorwerp ervoor staat.",
            ],
        ),
        dict(
            aanpak="De imparfait maak je uit de nous-vorm van de tegenwoordige tijd: haal de -ons "
                   "weg en zet -ais, -ais, -ait, -ions, -iez, -aient. Eén werkwoord valt buiten de "
                   "regel.",
            waarom=[
                "Let op elles faisaient: de stam komt van nous faisons, dus fais-. En on prenait "
                "komt van nous prenons, niet van il prend.",
                "Être, met de stam ét-: j'étais, tu étais, il était. Alle andere werkwoorden, ook "
                "avoir en aller, halen hun stam netjes uit de nous-vorm.",
            ],
        ),
        dict(
            aanpak="Vraag je af of het gaat over hoe het was of over wat er gebeurde. Woorden als "
                   "hier en soudain wijzen naar de passé composé, chaque en quand j'étais petit naar "
                   "de imparfait.",
            waarom=[
                "Let op de twee zinnen met quand: il pleuvait quand je suis sorti en elle lisait "
                "quand il est entré. Het decor staat in de imparfait, en wat er dan plots gebeurt in "
                "de passé composé.",
                "Noem beide. De imparfait geeft het decor, dus hoe het was en wat gewoonte was; de "
                "passé composé geeft de gebeurtenis, dus wat er op dat moment gebeurde en afgelopen "
                "is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-toekomende-tijd-en-de-conditionnel-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De futur proche is de makkelijkste toekomst: vervoeg aller en zet het hele "
                   "werkwoord erachter. Enkel aller verandert.",
            waarom=[
                "Let op tu ne vas pas travailler: de ontkenning gaat rond aller, niet rond het hele "
                "werkwoord. Dus nooit tu ne vas travailler pas.",
                "Noem beide. Je vais partir voelt dichtbij en bijna beslist, je partirai staat "
                "verder weg en klinkt formeler. In spreektaal hoor je bijna altijd de eerste.",
            ],
        ),
        dict(
            aanpak="Voor de futur simple neem je het hele werkwoord en plak je er de vormen van "
                   "avoir achter. Een twintigtal werkwoorden heeft een eigen stam, en die moet je "
                   "kennen.",
            waarom=[
                "Let op de eigen stammen: être geeft ser-, avoir aur-, aller ir-, faire fer-, venir "
                "viendr-, pouvoir pourr- en voir verr-. Ze eindigen allemaal op een r, en daarna "
                "komen gewoon de uitgangen.",
                "De vormen van avoir: -ai, -as, -a, -ons, -ez, -ont. Je hoort j'ai, tu as, il a "
                "terug in je parlerai, tu parleras, il parlera, en dat is het handigste "
                "steuntje van de hele tijd.",
            ],
        ),
        dict(
            aanpak="De conditionnel heeft dezelfde stam als de futur, maar de uitgangen van de "
                   "imparfait. Ken je de futur, dan ken je de conditionnel er gratis bij.",
            waarom=[
                "Let op dat de stam dezelfde blijft: je serai wordt je serais, je pourrai wordt je "
                "pourrais. Enkel de uitgang verschilt, en in de ik-vorm hoor je dat verschil bijna "
                "niet, dus let op het schrijven.",
                "Let op dat de si-zin in de imparfait staat en de hoofdzin in de conditionnel. Dus "
                "si j'avais en nooit si j'aurais; die laatste vorm bestaat niet in deze combinatie.",
                "De imparfait. Si + imparfait in het eerste deel, conditionnel in het tweede: si "
                "tu étudiais, tu réussirais. Dat is het vaste paar voor iets dat je je enkel "
                "voorstelt.",
            ],
        ),
        dict(
            aanpak="Kijk naar de tijd in de si-zin, want die beslist de tijd van de hoofdzin. "
                   "Présent geeft futur, imparfait geeft conditionnel.",
            waarom=[
                "Let op S'il fait beau, nous sortirons: de si-zin blijft in de tegenwoordige tijd, "
                "ook al gaat de zin over morgen. Een futur na si bestaat niet.",
                "Noem beide paren. Si + présent met de futur voor iets dat echt kan gebeuren, en si "
                "+ imparfait met de conditionnel voor iets dat je je voorstelt. Die twee combinaties "
                "dekken zowat alles.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsbouw-zinsdelen-en-congruentie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek altijd eerst het werkwoord, en vraag dan wie of wat het doet. Zo vind je "
                   "het onderwerp, ook als er een bijzin tussen staat.",
            waarom=[
                "Let op Ma soeur, qui habite à Gand, vient ce soir: het onderwerp is ma soeur, en de "
                "bijzin tussen de komma's heeft zijn eigen werkwoord habite. En bij il y a is il "
                "een vast onderwerp dat niets aanduidt.",
                "Onderwerp, werkwoord, voorwerp, dan de rest. Het Frans wijkt daar veel minder van "
                "af dan het Nederlands, dat zijn werkwoord vaak achteraan zet.",
            ],
        ),
        dict(
            aanpak="Een vraag kan op drie manieren: met de stem alleen, met est-ce que, of met "
                   "omkering. De eerste hoort in spreektaal, de derde in een schrijfopdracht.",
            waarom=[
                "Let op Que fais-tu: bij omkering wordt qu'est-ce que gewoon que. En het streepje "
                "tussen werkwoord en voornaamwoord is verplicht.",
                "Om twee klinkers te scheiden. Habite eindigt op een e en il begint met een i, dus "
                "schuift er een t tussen: habite-t-il. Hetzelfde bij a-t-il en va-t-elle.",
            ],
        ),
        dict(
            aanpak="Een Franse ontkenning heeft twee delen: ne voor het werkwoord en het tweede "
                   "woord erachter. In de passé composé staat dat tweede woord tussen het "
                   "hulpwerkwoord en het deelwoord.",
            waarom=[
                "Let op Je n'ai vu personne: personne staat achter het deelwoord omdat het hier het "
                "voorwerp is, terwijl pas encore in il n'est pas encore parti wel tussen est en "
                "parti komt. En ne wordt n' voor een klinker.",
            ],
        ),
        dict(
            aanpak="Overeenkomst is de fout die het vaakst punten kost, want je hoort hem niet. "
                   "Lees je zin dus een keer met enkel die vraag in je hoofd.",
            waarom=[
                "Let op Mon frère et moi: twee personen samen geven nous, dus nous sommes arrivés "
                "met een s. En elle a des yeux bleus krijgt een s, want bleu gaat mee met yeux en "
                "niet met elle.",
                "Noem de drie na elkaar. Past het werkwoord bij het onderwerp, gaat het bijvoeglijk "
                "naamwoord mee in geslacht en getal, en gaat het deelwoord na être mee met het "
                "onderwerp. Dat zijn de drie controles die bijna al je fouten vinden.",
            ],
        ),
    ],
)

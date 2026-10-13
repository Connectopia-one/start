# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Frans 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

Net als de vragen op het scherm dekt dit **alleen het schriftelijke Frans**:
lezen, schrijven, woordenschat en grammatica. Luisteren, spreken en de
gesprekken staan er niet in; daar heb je geluid en een gesprekspartner voor
nodig.

Het ERK-niveau is B1+ tot B2. Hier horen dus wél de subjonctif, de gérondif,
de plus-que-parfait, de indirecte rede en de passieve zin bij; in dubbele
finaliteit niet.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm. Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/frans.json` en naast de leerbundel van hetzelfde thema in
`maak_frans_beyond.py`.

Op papier staan de accenten er wél gewoon op. Dat online invulantwoorden soms
zonder accenten vergeleken worden, is een toegeving aan het toetsenbord, geen
regel over hoe je het schrijft.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Frans"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NIVEAU = "-beyond"
VOOR = "oefenbundel-"

W = "150px"
WW = "220px"
WL = "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Zet de accenten erbij: op papier horen ze er gewoon op.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands of Engels woord lijkt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

HOE_LEZEN = [
    "Lees de tekst eerst helemaal door. Je moet niet elk woord kennen.",
    "Onderstreep de woorden die je niet kent en probeer ze te raden uit de zin eromheen.",
    "Kom bij elke vraag terug naar de tekst.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("een-franse-tekst-analyseren",
    titel="Een Franse tekst analyseren",
    onder="Twee teksten en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Texte A", opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Le train de nuit revient</h3>"
                  "<p>Pendant vingt ans, les trains de nuit ont presque disparu d'Europe. Les "
                  "compagnies les trouvaient trop chers: un wagon-lit transporte moins de "
                  "voyageurs qu'une voiture de jour, et le personnel doit travailler la nuit. "
                  "Depuis 2021, pourtant, les lignes se multiplient à nouveau.</p>"
                  "<p>„Nos clients ne cherchent pas la vitesse”, explique Marta Leclerc, "
                  "responsable d'une compagnie autrichienne. „Ils cherchent à gagner une "
                  "journée. On part à vingt heures, on dort, et on arrive à neuf heures au "
                  "centre-ville, sans contrôle de sécurité et sans taxi.”</p>"
                  "<p>L'argument écologique compte aussi: un trajet Bruxelles-Vienne en train "
                  "émet environ trente fois moins de CO2 que le même trajet en avion. Mais le "
                  "prix reste un obstacle. Un lit en cabine à deux coûte souvent plus cher "
                  "qu'un billet d'avion acheté à l'avance.</p>"
                  "<p>„Tant que l'avion ne paiera pas de taxe sur le kérosène, nous jouerons "
                  "avec des règles différentes”, dit Marta Leclerc. „Nous ne demandons pas une "
                  "faveur. Nous demandons les mêmes règles.”</p>"),
             ]),
        dict(kop="Comprendre le texte",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Waarom verdwenen de nachttreinen volgens de tekst?",
                  "ze waren te duur: minder reizigers per rijtuig en nachtwerk", WL),
                 ("kort", "Sinds welk jaar komen de lijnen weer terug?", "sinds 2021", W),
                 ("kort", "Wat zoeken de klanten volgens Marta Leclerc?",
                  "niet snelheid, maar een dag winnen", WL),
                 ("kort", "Hoeveel minder CO2 stoot de trein Brussel-Wenen uit dan het "
                          "vliegtuig?", "ongeveer dertig keer minder", WW),
                 ("open", "Welk obstakel blijft volgens de tekst bestaan, en waarom?",
                  "De prijs: een bed in een tweepersoonscabine kost vaak meer dan een "
                  "vliegtuigticket dat op voorhand gekocht is, onder meer omdat er op kerosine "
                  "geen belasting betaald wordt.", 4),
                 ("open", "Wat vraagt Marta Leclerc precies? Geef het in je eigen woorden.",
                  "Geen gunst of steun, maar dezelfde regels voor trein en vliegtuig, dus ook "
                  "een belasting op de brandstof van het vliegtuig.", 3),
             ]),
        dict(kop="Les mots du texte",
             opdracht="Zoek het Franse woord in de tekst.",
             oefeningen=[
                 ("rij", [("verdwijnen", "disparaître"), ("vermenigvuldigen, toenemen",
                                                          "se multiplier"),
                          ("een reiziger", "un voyageur"), ("een obstakel", "un obstacle"),
                          ("op voorhand", "à l'avance"), ("een gunst", "une faveur")],
                  "Welk Frans woord?", WW),
                 ("kort", "Wat betekent <em>tant que</em> in de laatste alinea?",
                  "zolang als", W),
             ]),
        dict(kop="Texte B", opdracht="Lees ook deze korte tekst.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Parti de Bruxelles à 19 h 22, arrivé à Vienne à 9 h 10. La cabine "
                  "était propre et le petit-déjeuner correct. Par contre, impossible de dormir "
                  "avant minuit: les arrêts sont bruyants et la climatisation fait du bruit. "
                  "Pour le prix, j'attendais mieux. Je recommande quand même, mais prenez des "
                  "bouchons d'oreilles.</em></p>"),
                 ("kies", "Welk oordeel geeft de schrijver?",
                  ["volledig positief", "gemengd, maar overwegend positief",
                   "gemengd, maar overwegend negatief", "volledig negatief"], 1),
                 ("kort", "Welke twee klachten geeft hij?",
                  "lawaai bij de haltes en van de airco, en de prijs", WL),
                 ("kort", "Welke woordgroep toont dat hij het toch aanraadt?",
                  "je recommande quand même", WW),
             ]),
        dict(kop="Entre les lignes",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Tekst A is een artikel, tekst B een reisverslag. Noem twee "
                          "verschillen die je in de taal zelf kan aanwijzen.",
                  "Tekst A werkt met cijfers, een naam en citaten tussen aanhalingstekens en "
                  "staat in de derde persoon. Tekst B staat in de ik-vorm, geeft meningen "
                  "(propre, correct, j'attendais mieux) en spreekt de lezer aan (prenez).", 4),
                 ("open", "Welke vraag blijft na beide teksten onbeantwoord?",
                  "Een eigen antwoord, bijvoorbeeld: wat een ticket precies kost, hoeveel "
                  "lijnen er bijkomen, of de nachttrein zonder subsidie rendabel kan zijn.",
                  3),
             ]),
    ])

# ============================================================
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    reeksen=[
        dict(kop="Quel type de texte?",
             opdracht="Schrijf de tekstsoort: informatif, persuasif, prescriptif, "
                      "argumentatif, narratif of littéraire.",
             oefeningen=[
                 ("rij", [("une recette de cuisine", "prescriptif"),
                          ("une publicité pour un parfum", "persuasif"),
                          ("un article sur les élections", "informatif"),
                          ("une lettre ouverte contre un projet", "argumentatif"),
                          ("un conte pour enfants", "narratif"),
                          ("un poème de Prévert", "littéraire")],
                  "Welke soort?", WW),
                 ("kort", "Hoe herken je een prescriptieve tekst meteen?",
                  "aan de imperatief en de genummerde stappen", WL),
             ]),
        dict(kop="Fait ou opinion?",
             opdracht="Schrijf F of O.",
             oefeningen=[
                 ("rij", [("Le pont a été ouvert en 1964.", "F"),
                          ("C'est le plus beau pont du pays.", "O"),
                          ("Trois élèves sur quatre viennent à vélo.", "F"),
                          ("À mon avis, le vélo est la meilleure solution.", "O"),
                          ("La commune a dépensé deux millions d'euros.", "F")],
                  "F of O?", "58px"),
                 ("kort", "Welke woorden verraden een mening in zin 2 en 4?",
                  "le plus beau en à mon avis, la meilleure", WL),
             ]),
        dict(kop="Les mots de liaison",
             opdracht="Vul het passende verbindingswoord in.",
             oefeningen=[
                 ("rij", [("Il pleuvait; ..., le match a eu lieu.", "cependant / pourtant"),
                          ("Le bus était en retard, ... nous avons raté le train.",
                           "donc / c'est pourquoi"),
                          ("Elle a beaucoup travaillé, ... elle a échoué.", "pourtant"),
                          ("... tu pars maintenant, tu l'auras.", "Si"),
                          ("Il est resté chez lui ... il était malade.", "parce que")],
                  "Welk woord?", WW),
                 ("rij", [("d'abord", "om te beginnen"), ("en revanche", "daarentegen"),
                          ("en outre", "bovendien"), ("en somme", "kortom")],
                  "Wat betekent het?", WW),
             ]),
        dict(kop="Le registre",
             opdracht="Schrijf soutenu, courant of familier, en geef een courante versie.",
             oefeningen=[
                 ("rij", [("Je vous saurais gré de me répondre.", "soutenu: Merci de me répondre."),
                          ("Il y a un souci avec ma commande.", "courant"),
                          ("C'est nul, ce truc.", "familier: Ce n'est pas bon."),
                          ("Veuillez agréer mes salutations distinguées.",
                           "soutenu: Cordialement.")],
                  "Welk register?", WL),
                 ("kort", "Welke aanspreekvorm gebruik je in een mail aan een onbekende?",
                  "vous", W),
             ]),
    ])


# ============================================================
zet("de-franstalige-wereld-omgangsvormen-en-gewoontes",
    titel="De Franstalige wereld: omgangsvormen en gewoontes",
    reeksen=[
        dict(kop="Tu ou vous?",
             opdracht="Schrijf tu of vous, en in enkele woorden waarom.",
             oefeningen=[
                 ("rij", [("tegen een klasgenoot", "tu: iemand van je leeftijd die je kent"),
                          ("tegen de moeder van een vriend", "vous: een volwassene die je niet goed kent"),
                          ("tegen een verkoper in een winkel", "vous: een onbekende"),
                          ("tegen je neef van tien", "tu: familie en een kind"),
                          ("in een mail aan een stagebegeleider", "vous: een werkrelatie")],
                  "Tu of vous, en waarom?", WL),
                 ("open", "Wat doe je als iemand jou met <em>tu</em> aanspreekt en jij hem met "
                          "<em>vous</em>?",
                  "Je mag het zo laten tot hij het zelf voorstelt. Vaak zegt men dan <em>on "
                  "peut se tutoyer</em>, en daarna gebruik je tu. Zelf overschakelen zonder dat "
                  "is in Frankrijk onbeleefd.", 4),
             ]),
        dict(kop="Les usages",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("la bise", "een kus op de wang bij de begroeting"),
                          ("la rentrée", "het begin van het schooljaar"),
                          ("le bac", "het eindexamen van het secundair in Frankrijk"),
                          ("les soldes", "de koopjes"),
                          ("la Francophonie", "de Franstalige wereld samen")],
                  "Wat is het?", WL),
                 ("kort", "Op welke dag viert Frankrijk zijn nationale feestdag?",
                  "14 juli", W),
                 ("kort", "Welk woord zeg je altijd eerst als je iemand iets vraagt?",
                  "bonjour", W),
             ]),
        dict(kop="Le français dans le monde",
             opdracht="Antwoord kort, met de atlas erbij als je wil.",
             oefeningen=[
                 ("rij", [("twee Franstalige landen in Europa", "la Belgique, la Suisse"),
                          ("een Franstalige provincie in Canada", "le Québec"),
                          ("twee Franstalige landen in Afrika", "le Sénégal, le Maroc, la RD Congo"),
                          ("de drie gewesten van België",
                           "la Flandre, la Wallonie, Bruxelles-Capitale")],
                  "Welke?", WL),
                 ("rij", [("septante (BE)", "soixante-dix"), ("nonante (BE)", "quatre-vingt-dix"),
                          ("la fin de semaine (QC)", "le week-end"),
                          ("une drache (BE)", "une grosse averse")],
                  "Hoe zegt men het in Frankrijk?", WW),
                 ("open", "Waarom is het nuttig om die varianten te kennen, ook als je zelf de "
                          "Franse vorm gebruikt?",
                  "Je komt ze tegen in teksten, in films en in gesprekken met mensen uit "
                  "België, Zwitserland of Québec. Wie ze niet herkent, mist de betekenis of "
                  "denkt ten onrechte dat het een fout is.", 3),
             ]),
        dict(kop="Savoir-vivre",
             opdracht="Schrijf de passende Franse zin.",
             oefeningen=[
                 ("rij", [("Je verontschuldigt je.", "Je suis désolé(e). / Excusez-moi."),
                          ("Iemand verontschuldigt zich bij jou.", "Ce n'est pas grave."),
                          ("Je feliciteert iemand.", "Félicitations ! / Beau travail !"),
                          ("Je bedankt formeel.", "Je vous remercie."),
                          ("Je vraagt beleefd om hulp.", "Pourriez-vous m'aider, s'il vous plaît ?")],
                  "Welke Franse zin?", WL),
             ]),
    ])

# ============================================================
zet("literaire-teksten-en-literatuurbeleving",
    titel="Literaire teksten en literatuurbeleving",
    reeksen=[
        dict(kop="Le vocabulaire du récit",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("de verteller", "le narrateur"), ("een personage", "un personnage"),
                          ("de verhaallijn", "l'intrigue"), ("de plaats en de tijd", "le cadre"),
                          ("het thema", "le thème"), ("een hoofdstuk", "un chapitre")],
                  "Welk Frans woord?", WW),
                 ("rij", [("een roman", "un roman"), ("een kortverhaal", "une nouvelle"),
                          ("een gedicht", "un poème"), ("een toneelstuk", "une pièce de théâtre"),
                          ("een stripverhaal", "une bande dessinée")],
                  "Welk Frans woord?", WW),
                 ("kort", "Pas op met <em>une nouvelle</em>: welke twee betekenissen heeft het?",
                  "een kortverhaal, en een nieuwtje", WL),
             ]),
        dict(kop="Les figures de style",
             opdracht="Schrijf welke stijlfiguur het is.",
             oefeningen=[
                 ("rij", [("Il est fort comme un lion.", "une comparaison"),
                          ("Cette ville est un labyrinthe.", "une métaphore"),
                          ("Le vent murmure dans les arbres.", "une personnification"),
                          ("Je te l'ai dit mille fois.", "une hyperbole")],
                  "Welke stijlfiguur?", WW),
                 ("kort", "Wat is het verschil tussen een vergelijking en een metafoor?",
                  "een vergelijking gebruikt comme, een metafoor niet", WL),
             ]),
        dict(kop="Lire un extrait",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>La maison sentait la cire et le pain froid. Grand-mère ne disait rien, "
                  "mais elle avait mis trois assiettes sur la table, comme chaque dimanche, "
                  "comme si personne n'était parti. Dehors, la pluie tombait sur les tuiles du "
                  "hangar. Je suis resté debout dans l'entrée, mon sac à la main, et j'ai compté "
                  "jusqu'à dix avant d'oser avancer.</em></p>"),
                 ("kort", "Welke zintuigen spreekt de eerste zin aan?",
                  "de reuk: was en koud brood", WL),
                 ("open", "Wat vertelt het derde bord over de grootmoeder, zonder dat het er "
                          "staat?",
                  "Dat ze iemand die weg is nog altijd verwacht of niet wil loslaten. Ze zegt "
                  "niets, maar haar gebaar toont het verdriet of de gewoonte die ze niet "
                  "opgeeft.", 4),
                 ("open", "Welk gevoel heeft de verteller, en waaraan zie je dat?",
                  "Hij aarzelt en is gespannen: hij blijft met zijn tas in de hand in de gang "
                  "staan en telt tot tien voor hij durft binnen te gaan.", 3),
                 ("kort", "In welke tijd staat <em>je suis resté</em>, en wat doet die tijd "
                          "hier?", "passé composé: de handeling die het verhaal vooruit duwt",
                  WL),
             ]),
        dict(kop="Ta lecture",
             opdracht="Schrijf in het Frans, met volledige zinnen.",
             oefeningen=[
                 ("open", "Schrijf drie zinnen over een boek of een film die indruk op je "
                          "maakte. Gebruik <em>j'ai aimé</em>, <em>parce que</em> en <em>ce qui "
                          "m'a frappé</em>.",
                  "Een eigen antwoord van drie volledige zinnen met een mening en een reden, "
                  "bijvoorbeeld: J'ai aimé ce film parce que les personnages ne sont pas "
                  "parfaits. Ce qui m'a frappé, c'est la fin. Je le conseillerais à quelqu'un "
                  "qui aime les histoires lentes.", 4),
                 ("rij", [("Ce livre m'a touché.", "dit boek heeft me geraakt"),
                          ("Je me suis identifié au personnage.",
                           "ik herkende mezelf in het personage"),
                          ("La fin m'a déçu.", "het einde heeft me ontgoocheld"),
                          ("Je n'ai pas pu le lâcher.", "ik kon het niet wegleggen")],
                  "Wat betekent het?", WL),
             ]),
    ])

# ============================================================
zet("schrijven-en-schriftelijke-interactie",
    titel="Schrijven en schriftelijke interactie",
    reeksen=[
        dict(kop="La structure",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Uit welke drie delen bestaat een goed opgebouwde tekst?",
                  "een inleiding, een midden en een slot", WL),
                 ("kort", "Hoe heet een alinea in het Frans?", "un paragraphe", WW),
                 ("kort", "Wat is taakvoltooiing in één zin?",
                  "je doel is bereikt: de lezer weet wat hij moest weten", WL),
                 ("waar", "Een tekst die foutloos is maar de vraag niet beantwoordt, scoort "
                          "goed op taakvoltooiing.", False),
             ]),
        dict(kop="La lettre formelle",
             opdracht="Zet de delen in de juiste orde met 1 tot 6.",
             oefeningen=[
                 ("rij", [("Madame, Monsieur,", "1"),
                          ("Je me permets de vous écrire au sujet de...", "2"),
                          ("de uitleg van je vraag", "3"),
                          ("Je vous remercie d'avance de votre réponse.", "4"),
                          ("Veuillez agréer mes salutations distinguées.", "5"),
                          ("je naam", "6")],
                  "Welk nummer?", "58px"),
                 ("open", "Schrijf de eerste twee zinnen van een mail waarin je informatie "
                          "vraagt over een zomercursus.",
                  "Een eigen antwoord, bijvoorbeeld: Madame, Monsieur, je me permets de vous "
                  "écrire au sujet de votre cours d'été. Je voudrais savoir s'il reste des "
                  "places pour le mois de juillet.", 3),
             ]),
        dict(kop="Plus poli",
             opdracht="Herschrijf hoffelijker, met de conditionnel.",
             oefeningen=[
                 ("rij", [("Je veux un renseignement.", "Je voudrais un renseignement."),
                          ("Vous pouvez m'aider?", "Pourriez-vous m'aider ?"),
                          ("J'aime réserver une table.", "J'aimerais réserver une table."),
                          ("Donnez-moi votre réponse.",
                           "Auriez-vous l'amabilité de me répondre ?")],
                  "Hoe schrijf je het?", WL),
             ]),
        dict(kop="Relire son texte",
             opdracht="Verbeter de fout en zeg welke regel je toepast.",
             oefeningen=[
                 ("rij", [("Les enfants est content.", "sont contents: werkwoord en bijvoeglijk naamwoord in het meervoud"),
                          ("Elle a allé à Paris.", "elle est allée: aller neemt être, en het deelwoord gaat mee"),
                          ("Je vais au école.", "à l'école: à + la wordt niet au"),
                          ("Il a prit le train.", "il a pris: het deelwoord van prendre is pris"),
                          ("Nous mangons.", "nous mangeons: een e na de g")],
                  "Hoe hoort het, en waarom?", WL),
                 ("kort", "Wat doe je als allerlaatste voor je je tekst afgeeft?",
                  "nalezen op werkwoordsvormen en overeenkomst", WL),
             ]),
    ])

# ============================================================
zet("woordvelden-de-mens-gezondheid-eten-en-wonen",
    titel="Woordvelden: de mens, gezondheid, eten en wonen",
    reeksen=[
        dict(kop="La personne",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een familielid", "un parent"), ("een neef of nicht", "un cousin, une cousine"),
                          ("een buur", "un voisin"), ("trots", "fier, fière"),
                          ("gespannen", "stressé"), ("verlegen", "timide")],
                  "Welk Frans woord?", WW),
                 ("rij", [("s'entendre bien avec quelqu'un", "goed overeenkomen met iemand"),
                          ("avoir le moral à zéro", "zich slecht voelen"),
                          ("en avoir assez de", "er genoeg van hebben"),
                          ("prendre soin de soi", "goed voor zichzelf zorgen")],
                  "Wat betekent het?", WL),
             ]),
        dict(kop="La santé",
             opdracht="Schrijf het Franse woord of de uitdrukking.",
             oefeningen=[
                 ("rij", [("keelpijn hebben", "avoir mal à la gorge"),
                          ("koorts", "la fièvre"), ("een voorschrift", "une ordonnance"),
                          ("de apotheek", "la pharmacie"), ("een huisarts", "un médecin généraliste"),
                          ("genezen", "guérir")],
                  "Welk Frans woord?", WW),
                 ("kort", "Waarom kan je niet zeggen <em>j'ai une douleur dans ma tête</em>?",
                  "in het Frans zeg je avoir mal à la tête", WL),
             ]),
        dict(kop="La table",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("het ontbijt", "le petit déjeuner"), ("een voorgerecht", "une entrée"),
                          ("pikant", "épicé"), ("om mee te nemen", "à emporter"),
                          ("een lepel", "une cuillère"), ("afwassen", "faire la vaisselle")],
                  "Welk Frans woord?", WW),
                 ("kort", "Wat is in België <em>le dîner</em>, en wat in Frankrijk?",
                  "bij ons het middagmaal, in Frankrijk het avondmaal", WL),
             ]),
        dict(kop="Le logement",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("de huur", "le loyer"), ("een huurder", "un locataire"),
                          ("de eigenaar", "le propriétaire"), ("het gelijkvloers", "le rez-de-chaussée"),
                          ("de zolder", "le grenier"), ("verhuizen", "déménager")],
                  "Welk Frans woord?", WW),
                 ("rij", [("une tâche ménagère", "een klusje in huis"),
                          ("ranger sa chambre", "zijn kamer opruimen"),
                          ("une poubelle", "een vuilnisbak"), ("un rideau", "een gordijn")],
                  "Wat betekent het?", WW),
                 ("open", "Beschrijf je eigen kamer in drie Franse zinnen.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: Ma chambre est "
                  "petite mais claire. Il y a un lit, un bureau et une armoire. Les murs sont "
                  "blancs et il y a des photos au-dessus du lit.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-school-werk-reizen-en-de-samenleving",
    titel="Woordvelden: school, werk, reizen en de samenleving",
    reeksen=[
        dict(kop="À l'école et au travail",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een vak", "une matière"), ("een uurrooster", "un horaire"),
                          ("de pauze", "la récréation"), ("slagen voor een examen", "réussir un examen"),
                          ("een diploma", "un diplôme"), ("nota's nemen", "prendre des notes")],
                  "Welk Frans woord?", WW),
                 ("rij", [("solliciteren", "postuler pour un emploi"),
                          ("een sollicitatiegesprek", "un entretien"),
                          ("een loon", "un salaire"), ("werkloos", "au chômage"),
                          ("ontslagen worden", "être licencié"), ("deeltijds", "à temps partiel")],
                  "Welk Frans woord?", WW),
                 ("kort", "Wat betekent <em>passer un examen</em>?",
                  "een examen afleggen, niet slagen", WL),
             ]),
        dict(kop="Les voyages",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een heen-en-terugticket", "un aller-retour"),
                          ("de bagage", "les bagages"), ("een vertraging", "un retard"),
                          ("een staking", "une grève"), ("een omleiding", "une déviation"),
                          ("een verblijf", "un séjour")],
                  "Welk Frans woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>un voyage</em> en <em>un trajet</em>?",
                  "un voyage is de hele reis, un trajet het stuk weg", WL),
                 ("open", "Schrijf in het Frans dat je trein een uur vertraging had en dat je "
                          "je afspraak gemist hebt.",
                  "Mon train avait une heure de retard, donc j'ai raté mon rendez-vous.", 2),
             ]),
        dict(kop="La société",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("een verkiezing", "une élection"), ("een wet", "une loi"),
                          ("een burger", "un citoyen"), ("betogen", "manifester"),
                          ("de armoede", "la pauvreté"), ("een vluchteling", "un réfugié")],
                  "Welk Frans woord?", WW),
                 ("rij", [("un syndicat", "een vakbond"), ("un impôt", "een belasting"),
                          ("le conseil communal", "de gemeenteraad"),
                          ("faire du bénévolat", "vrijwilligerswerk doen")],
                  "Wat betekent het?", WL),
                 ("open", "Geef in drie Franse zinnen je mening over vrijwilligerswerk op "
                          "school. Gebruik <em>à mon avis</em> en <em>parce que</em>.",
                  "Een eigen antwoord met drie volledige zinnen en een reden, bijvoorbeeld: À "
                  "mon avis, le bénévolat devrait faire partie de l'école. On apprend des "
                  "choses qu'un livre ne donne pas. Mais il faut que ce soit un choix, parce "
                  "que l'obligation tue l'envie.", 4),
             ]),
    ])


# ============================================================
zet("naamwoorden-lidwoorden-en-determinanten",
    titel="Naamwoorden, lidwoorden en determinanten",
    reeksen=[
        dict(kop="Le genre",
             opdracht="Schrijf le of la voor het woord.",
             oefeningen=[
                 ("rij", [("... problème", "le problème"), ("... page", "la page"),
                          ("... voyage", "le voyage"), ("... nation", "la nation"),
                          ("... silence", "le silence"), ("... liberté", "la liberté"),
                          ("... musée", "le musée"), ("... eau", "l'eau (f.)")],
                  "Le of la?", WW),
                 ("kort", "Welke uitgang is bijna altijd vrouwelijk: -age, -ment of -tion?",
                  "-tion", WW),
             ]),
        dict(kop="Le pluriel",
             opdracht="Zet in het meervoud.",
             oefeningen=[
                 ("rij", [("un journal", "des journaux"), ("un cheval", "des chevaux"),
                          ("un cadeau", "des cadeaux"), ("un œil", "des yeux"),
                          ("un travail", "des travaux"), ("un prix", "des prix")],
                  "Het meervoud?", WW),
                 ("kort", "Wat gebeurt er met het meervoud van een woord dat al op -s, -x of "
                          "-z eindigt?", "het blijft hetzelfde", WL),
             ]),
        dict(kop="Article défini, indéfini ou partitif?",
             opdracht="Vul in: le, la, les, un, une, des, du, de la of d'.",
             oefeningen=[
                 ("rij", [("Je bois ... eau.", "de l'eau"), ("J'aime ... fromage.", "le fromage"),
                          ("Il achète ... pain.", "du pain"),
                          ("Elle a ... amis en France.", "des amis"),
                          ("Je ne mange pas ... viande.", "de viande"),
                          ("Il y a ... neige sur la route.", "de la neige")],
                  "Welk lidwoord?", WW),
                 ("kort", "Welke regel geldt voor het delend lidwoord in een ontkennende zin?",
                  "du, de la en des worden de of d'", WL),
             ]),
        dict(kop="Les déterminants",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("... livre est à moi. (dit)", "Ce livre"),
                          ("... histoire me plaît. (dit)", "Cette histoire"),
                          ("... amis sont partis. (deze)", "Ces amis"),
                          ("... arbre est vieux. (die)", "Cet arbre"),
                          ("Où sont ... clés? (jouw)", "tes clés"),
                          ("C'est ... décision. (hun)", "leur décision")],
                  "Welke vorm?", WW),
                 ("rij", [("... élèves sont présents. (elke)", "Chaque élève est présent."),
                          ("J'ai ... questions. (een paar)", "quelques questions"),
                          ("Il a lu ... les pages. (alle)", "toutes les pages"),
                          ("Je n'ai ... idée. (geen enkel)", "aucune idée")],
                  "Hoe schrijf je het?", WL),
                 ("open", "Waarom staat <em>chaque</em> altijd bij een enkelvoud, ook al "
                          "bedoel je iedereen?",
                  "Chaque kijkt naar één persoon of zaak per keer: chaque élève, één leerling "
                  "na de andere. Wil je het meervoud, dan gebruik je tous les of toutes les.",
                  3),
             ]),
    ])

# ============================================================
zet("voornaamwoorden-cod-coi-y-en-en",
    titel="Voornaamwoorden: COD, COI, y en en",
    reeksen=[
        dict(kop="COD ou COI?",
             opdracht="Onderstreep het voorwerp en schrijf COD of COI.",
             oefeningen=[
                 ("rij", [("Je vois mon frère.", "mon frère: COD"),
                          ("Je parle à mon frère.", "à mon frère: COI"),
                          ("Elle téléphone à sa mère.", "à sa mère: COI"),
                          ("Nous attendons le bus.", "le bus: COD"),
                          ("Il répond au professeur.", "au professeur: COI")],
                  "Wat, en welke soort?", WL),
                 ("kort", "Met welke vraag vind je het COD, en met welke het COI?",
                  "qui/quoi voor het COD, à qui voor het COI", WL),
             ]),
        dict(kop="Remplace",
             opdracht="Herschrijf met een voornaamwoord.",
             oefeningen=[
                 ("rij", [("Je vois Marie.", "Je la vois."),
                          ("Je parle à Marie.", "Je lui parle."),
                          ("Il achète les billets.", "Il les achète."),
                          ("Nous écrivons à nos amis.", "Nous leur écrivons."),
                          ("Elle ne connaît pas cet homme.", "Elle ne le connaît pas."),
                          ("J'ai vu le film.", "Je l'ai vu.")],
                  "Herschrijf.", WL),
                 ("kort", "Waar staat het voornaamwoord in een ontkennende zin?",
                  "tussen ne en het werkwoord", WL),
             ]),
        dict(kop="Y et en",
             opdracht="Herschrijf met y of en.",
             oefeningen=[
                 ("rij", [("Je vais à Paris.", "J'y vais."),
                          ("Il pense à son examen.", "Il y pense."),
                          ("Nous mangeons du pain.", "Nous en mangeons."),
                          ("Elle a trois frères.", "Elle en a trois."),
                          ("Je reviens de Bruxelles.", "J'en reviens."),
                          ("Tu as besoin d'aide?", "Tu en as besoin ?")],
                  "Herschrijf.", WL),
                 ("open", "Wat is de regel achter y en en in één zin elk?",
                  "Y vervangt wat met à of een plaats erbij staat; en vervangt wat met de, du, "
                  "de la, des of een hoeveelheid erbij staat.", 3),
             ]),
        dict(kop="L'ordre des pronoms",
             opdracht="Zet de twee voornaamwoorden in de juiste orde.",
             oefeningen=[
                 ("rij", [("Il donne le livre à Marie.", "Il le lui donne."),
                          ("Je donne les clés à mes parents.", "Je les leur donne."),
                          ("Elle me montre la photo.", "Elle me la montre."),
                          ("Il y a du café. Tu en veux?", "Il y en a.")],
                  "Herschrijf.", WL),
                 ("kort", "Welke orde geldt bij me, te, nous, vous naast le, la, les?",
                  "eerst me/te/nous/vous, dan le/la/les", WL),
                 ("kort", "En bij lui en leur?", "eerst le/la/les, dan lui/leur", WL),
             ]),
        dict(kop="Les relatifs",
             opdracht="Vul in: qui, que, où, dont.",
             oefeningen=[
                 ("rij", [("Le livre ... j'ai lu est triste.", "que"),
                          ("La fille ... habite ici est belge.", "qui"),
                          ("La ville ... je suis né est petite.", "où"),
                          ("Le film ... tout le monde parle.", "dont"),
                          ("C'est le prof ... nous a aidés.", "qui"),
                          ("L'auteur ... je connais le nom.", "dont")],
                  "Welk woord?", W),
                 ("kort", "Hoe weet je of je qui of que moet nemen?",
                  "qui als er geen onderwerp volgt, que als er wel een onderwerp volgt", WL),
             ]),
    ])

# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen",
    titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    reeksen=[
        dict(kop="L'accord",
             opdracht="Schrijf de juiste vorm.",
             oefeningen=[
                 ("rij", [("une robe (blanc)", "blanche"), ("des livres (nouveau)", "nouveaux"),
                          ("une amie (heureux)", "heureuse"), ("des filles (gentil)", "gentilles"),
                          ("une question (sérieux)", "sérieuse"), ("des murs (vieux)", "vieux"),
                          ("une eau (frais)", "fraîche"), ("des idées (fou)", "folles")],
                  "Welke vorm?", WW),
             ]),
        dict(kop="Avant ou après?",
             opdracht="Zet het bijvoeglijk naamwoord op zijn plaats.",
             oefeningen=[
                 ("rij", [("une maison (grand)", "une grande maison"),
                          ("une voiture (rouge)", "une voiture rouge"),
                          ("un homme (jeune)", "un jeune homme"),
                          ("un film (intéressant)", "un film intéressant"),
                          ("une histoire (beau)", "une belle histoire"),
                          ("un plat (italien)", "un plat italien")],
                  "Hoe schrijf je het?", WL),
                 ("kort", "Welke soort bijvoeglijke naamwoorden staan vóór het naamwoord?",
                  "de korte en vaak gebruikte: beau, bon, grand, petit, jeune, vieux, nouveau",
                  WL),
                 ("open", "Wat verandert er aan de betekenis van <em>un grand homme</em> "
                          "tegenover <em>un homme grand</em>?",
                  "Un grand homme is een belangrijk man, un homme grand een man die groot van "
                  "gestalte is. De plaats van het bijvoeglijk naamwoord verandert hier dus de "
                  "betekenis.", 3),
             ]),
        dict(kop="L'adverbe",
             opdracht="Maak het bijwoord.",
             oefeningen=[
                 ("rij", [("lent", "lentement"), ("heureux", "heureusement"),
                          ("vrai", "vraiment"), ("évident", "évidemment"),
                          ("courant", "couramment"), ("bon", "bien"), ("mauvais", "mal")],
                  "Welk bijwoord?", WW),
                 ("kort", "Van welke vorm van het bijvoeglijk naamwoord vertrek je om -ment "
                          "aan te plakken?", "de vrouwelijke vorm", WL),
             ]),
        dict(kop="Les degrés",
             opdracht="Schrijf de gevraagde trap.",
             oefeningen=[
                 ("rij", [("grand (vergrotend)", "plus grand"),
                          ("grand (overtreffend)", "le plus grand"),
                          ("bon (vergrotend)", "meilleur"),
                          ("bon (overtreffend)", "le meilleur"),
                          ("bien (vergrotend)", "mieux"),
                          ("mauvais (vergrotend)", "pire of plus mauvais"),
                          ("cher (even duur als)", "aussi cher que"),
                          ("cher (minder duur dan)", "moins cher que")],
                  "Welke vorm?", WW),
                 ("kies", "Welke zin is juist?",
                  ["Ce livre est plus bon que l'autre.",
                   "Ce livre est meilleur que l'autre.",
                   "Ce livre est plus meilleur que l'autre."], 1),
                 ("kort", "Welk woord gebruik je na een vergrotende trap om te vergelijken?",
                  "que", W),
             ]),
    ])

# ============================================================
zet("de-verleden-tijden-en-de-accord-van-het-deelwoord",
    titel="De verleden tijden en de accord van het deelwoord",
    reeksen=[
        dict(kop="Le participe passé",
             opdracht="Schrijf het deelwoord.",
             oefeningen=[
                 ("rij", [("prendre", "pris"), ("faire", "fait"), ("mettre", "mis"),
                          ("écrire", "écrit"), ("ouvrir", "ouvert"), ("venir", "venu"),
                          ("vivre", "vécu"), ("naître", "né"), ("mourir", "mort"),
                          ("devoir", "dû")],
                  "Het deelwoord?", WW),
             ]),
        dict(kop="Avoir ou être?",
             opdracht="Zet in de passé composé.",
             oefeningen=[
                 ("rij", [("je (aller)", "je suis allé(e)"), ("nous (finir)", "nous avons fini"),
                          ("elle (partir)", "elle est partie"),
                          ("ils (rester)", "ils sont restés"),
                          ("tu (voir)", "tu as vu"),
                          ("elles (se lever)", "elles se sont levées"),
                          ("il (descendre l'escalier)", "il a descendu l'escalier")],
                  "Welke vorm?", WL),
                 ("open", "Waarom neemt <em>descendre</em> de ene keer être en de andere keer "
                          "avoir?",
                  "Zonder voorwerp is het een beweging: il est descendu. Met een lijdend "
                  "voorwerp wordt het een handeling op iets: il a descendu l'escalier. Monter, "
                  "sortir, rentrer en passer doen hetzelfde.", 4),
             ]),
        dict(kop="L'accord du participe",
             opdracht="Vul de juiste vorm in en zeg waarom.",
             oefeningen=[
                 ("rij", [("Elle est (parti).", "partie: être, dus mee met het onderwerp"),
                          ("Les filles sont (arrivé).", "arrivées: être, meervoud vrouwelijk"),
                          ("Elle a (mangé) la pomme.", "mangé: avoir, voorwerp staat erna"),
                          ("La pomme qu'elle a (mangé).", "mangée: het COD staat ervoor"),
                          ("Je les ai (vu).", "vus: het COD les staat ervoor"),
                          ("Elles se sont (lavé).", "lavées: wederkerend, mee met het onderwerp")],
                  "Welke vorm, en waarom?", WL),
                 ("kort", "Wanneer gaat een deelwoord met avoir toch mee in geslacht en getal?",
                  "als het lijdend voorwerp vóór het werkwoord staat", WL),
             ]),
        dict(kop="Imparfait ou passé composé?",
             opdracht="Zet het werkwoord in de juiste tijd.",
             oefeningen=[
                 ("rij", [("Hier, je (manger) une pizza.", "j'ai mangé"),
                          ("Quand j'étais petit, je (jouer) dehors.", "je jouais"),
                          ("Il (pleuvoir) quand je suis sorti.", "il pleuvait"),
                          ("Soudain, le téléphone (sonner).", "a sonné"),
                          ("Chaque dimanche, nous (aller) chez grand-mère.", "nous allions"),
                          ("Elle (lire) un livre quand il est entré.", "elle lisait")],
                  "Welke tijd en vorm?", WL),
                 ("kort", "Welke tijd geeft het decor, en welke de gebeurtenis?",
                  "de imparfait het decor, de passé composé de gebeurtenis", WL),
             ]),
        dict(kop="Le plus-que-parfait",
             opdracht="Zet in de plus-que-parfait.",
             oefeningen=[
                 ("rij", [("j'ai fini", "j'avais fini"), ("elle est partie", "elle était partie"),
                          ("nous avons vu", "nous avions vu"),
                          ("ils se sont levés", "ils s'étaient levés")],
                  "Welke vorm?", WL),
                 ("open", "Leg met een eigen voorbeeld uit wat de plus-que-parfait doet.",
                  "Hij zegt dat iets nog vroeger gebeurde dan een ander verleden: Quand je suis "
                  "arrivé, le train était déjà parti. Eerst was de trein weg, daarna kwam ik "
                  "aan.", 3),
             ]),
    ])

# ============================================================
zet("futur-conditionnel-subjonctif-en-de-gerundif",
    titel="Futur, conditionnel, subjonctif en de gérondif",
    reeksen=[
        dict(kop="Le futur simple",
             opdracht="Zet in de futur simple.",
             oefeningen=[
                 ("rij", [("je (parler)", "je parlerai"), ("nous (finir)", "nous finirons"),
                          ("il (être)", "il sera"), ("tu (avoir)", "tu auras"),
                          ("elles (aller)", "elles iront"), ("je (faire)", "je ferai"),
                          ("vous (venir)", "vous viendrez"), ("on (pouvoir)", "on pourra"),
                          ("je (voir)", "je verrai")],
                  "Welke vorm?", WW),
                 ("kort", "Welke twee uitgangen hoor je in elke persoon van de futur terug?",
                  "de vormen van avoir: -ai, -as, -a, -ons, -ez, -ont", WL),
             ]),
        dict(kop="Le conditionnel",
             opdracht="Zet in de conditionnel présent.",
             oefeningen=[
                 ("rij", [("je (vouloir)", "je voudrais"), ("nous (aimer)", "nous aimerions"),
                          ("il (être)", "il serait"), ("tu (pouvoir)", "tu pourrais"),
                          ("elles (savoir)", "elles sauraient"), ("on (devoir)", "on devrait")],
                  "Welke vorm?", WW),
                 ("rij", [("Si j'avais le temps, je (venir).", "je viendrais"),
                          ("Si tu étudiais, tu (réussir).", "tu réussirais"),
                          ("S'il faisait beau, nous (sortir).", "nous sortirions")],
                  "Vul aan.", WL),
                 ("kort", "Welke tijd staat in de si-zin als de hoofdzin in de conditionnel "
                          "staat?", "de imparfait", WL),
             ]),
        dict(kop="Le subjonctif",
             opdracht="Zet in de subjonctif présent.",
             oefeningen=[
                 ("rij", [("que je (parler)", "que je parle"), ("que tu (finir)", "que tu finisses"),
                          ("qu'il (être)", "qu'il soit"), ("que nous (avoir)", "que nous ayons"),
                          ("qu'elle (aller)", "qu'elle aille"),
                          ("que je (faire)", "que je fasse"),
                          ("que vous (pouvoir)", "que vous puissiez"),
                          ("qu'on (savoir)", "qu'on sache")],
                  "Welke vorm?", WW),
                 ("rij", [("Il faut que tu (venir).", "que tu viennes"),
                          ("Je veux qu'il (partir).", "qu'il parte"),
                          ("Bien qu'elle (être) fatiguée, elle travaille.", "qu'elle soit"),
                          ("Je pense qu'il (avoir) raison.", "qu'il a: indicatif na penser")],
                  "Vul aan.", WL),
                 ("open", "Waarom staat er na <em>je pense que</em> géén subjonctif, en na "
                          "<em>je ne pense pas que</em> wel?",
                  "Je pense que stelt iets als een feit, dus indicatif. In de ontkenning wordt "
                  "het onzeker, en dan komt de subjonctif: je ne pense pas qu'il ait raison.",
                  4),
             ]),
        dict(kop="Le gérondif",
             opdracht="Herschrijf met een gérondif.",
             oefeningen=[
                 ("rij", [("Il chante et il travaille.", "Il travaille en chantant."),
                          ("Elle lit quand elle mange.", "Elle mange en lisant."),
                          ("Si tu travailles, tu réussiras.",
                           "En travaillant, tu réussiras."),
                          ("Il est tombé quand il courait.", "Il est tombé en courant.")],
                  "Herschrijf.", WL),
                 ("rij", [("faire", "en faisant"), ("avoir", "en ayant"),
                          ("être", "en étant"), ("savoir", "en sachant")],
                  "De gérondif?", WW),
                 ("kort", "Van welke persoonsvorm maak je de gérondif?",
                  "van nous in de tegenwoordige tijd, zonder -ons", WL),
             ]),
    ])

# ============================================================
zet("zinsbouw-indirecte-rede-en-de-passieve-zin",
    titel="Zinsbouw, indirecte rede en de passieve zin",
    reeksen=[
        dict(kop="La question",
             opdracht="Schrijf de vraag op de twee andere manieren.",
             oefeningen=[
                 ("rij", [("Tu viens ? (met est-ce que)", "Est-ce que tu viens ?"),
                          ("Tu viens ? (met omkering)", "Viens-tu ?"),
                          ("Où est-ce qu'il habite ? (omkering)", "Où habite-t-il ?"),
                          ("Qu'est-ce que tu fais ? (omkering)", "Que fais-tu ?")],
                  "Hoe schrijf je het?", WL),
                 ("kort", "Waarom staat er een t in <em>habite-t-il</em>?",
                  "om twee klinkers te scheiden bij de omkering", WL),
             ]),
        dict(kop="La négation",
             opdracht="Maak ontkennend met het woord tussen haakjes.",
             oefeningen=[
                 ("rij", [("Il parle. (ne... pas)", "Il ne parle pas."),
                          ("J'ai vu quelqu'un. (personne)", "Je n'ai vu personne."),
                          ("Il mange quelque chose. (rien)", "Il ne mange rien."),
                          ("Elle fume encore. (plus)", "Elle ne fume plus."),
                          ("Il est déjà parti. (pas encore)", "Il n'est pas encore parti."),
                          ("Je vais souvent. (jamais)", "Je ne vais jamais.")],
                  "Herschrijf.", WL),
             ]),
        dict(kop="Le discours indirect",
             opdracht="Zet over naar de indirecte rede.",
             oefeningen=[
                 ("rij", [('Il dit : « Je suis fatigué. »', "Il dit qu'il est fatigué."),
                          ('Elle a dit : « Je viens. »', "Elle a dit qu'elle venait."),
                          ("Il a dit : « J\'ai fini. »", "Il a dit qu'il avait fini."),
                          ("Elle m\'a demandé : « Tu viens ? »",
                           "Elle m'a demandé si je venais."),
                          ('Il a demandé : « Où habites-tu ? »',
                           "Il a demandé où j'habitais."),
                          ('Elle a dit : « Pars ! »', "Elle m'a dit de partir.")],
                  "Herschrijf.", WL),
                 ("tabel", ["directe rede", "na een verleden tijd"],
                  [["présent", None], ["passé composé", None],
                   ["futur simple", None], ["imparfait", None]],
                  "présent → imparfait · passé composé → plus-que-parfait · "
                  "futur simple → conditionnel présent · imparfait → imparfait", "170px"),
                 ("kort", "Welk woord gebruik je voor een vraag zonder vraagwoord?",
                  "si", W),
             ]),
        dict(kop="La voix passive",
             opdracht="Zet in de passieve vorm.",
             oefeningen=[
                 ("rij", [("Le facteur apporte la lettre.",
                           "La lettre est apportée par le facteur."),
                          ("Les élèves ont écrit ces textes.",
                           "Ces textes ont été écrits par les élèves."),
                          ("On construira une école.", "Une école sera construite."),
                          ("Un journaliste a pris la photo.",
                           "La photo a été prise par un journaliste.")],
                  "Herschrijf.", WL),
                 ("open", "Waarom verdwijnt <em>on</em> in de passieve vorm?",
                  "On noemt geen echte dader, dus er valt niemand te vermelden met par. De "
                  "passieve zin zonder par is daar precies de bedoeling.", 3),
                 ("kort", "Met welk werkwoord bouw je de passieve vorm, en wat doet het "
                          "deelwoord?",
                  "met être, en het deelwoord gaat mee met het onderwerp", WL),
             ]),
    ])

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-franse-tekst-analyseren-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder woordenboek, en onderstreep "
                   "daarna de cijfers, de namen en de citaten. Daar gaan de vragen bijna altijd "
                   "over.",
            waarom=[],
        ),
        dict(
            aanpak="Zoek bij elke vraag de plaats in de tekst terug en antwoord met wat daar "
                   "staat. Bij de vragen met een cijfer staat het antwoord letterlijk in de tekst.",
            waarom=[
                "Noem beide redenen, want de tekst geeft er twee: minder reizigers per rijtuig en "
                "nachtwerk voor het personeel. Eén van de twee is maar de helft van het antwoord.",
                None,
                "Let op de nuance: ze zeggen niet dat snelheid hun onverschillig laat, ze zoeken "
                "iets anders, namelijk een dag winnen. Dat is wat in de tekst staat.",
                "Ongeveer dertig keer minder. Let op het verschil tussen dertig keer minder en "
                "dertig procent minder: in zo'n vraag zit juist dat onderscheid.",
                "Noem de prijs én de reden erbij, de kerosine zonder belasting. Zonder die reden "
                "is het geen antwoord op de vraag waarom.",
                "Noem dat ze geen gunst vraagt maar dezelfde regels. Dat onderscheid is het hele "
                "punt van haar citaat, en het woord faveur uit reeks 3 komt er rechtstreeks uit.",
            ],
        ),
        dict(
            aanpak="Zoek het Franse woord in de tekst zelf terug in plaats van het uit je hoofd te "
                   "vertalen. Zo leer je het woord in zijn context, en dat blijft beter hangen.",
            waarom=[
                "Let op se multiplier: een wederkerend werkwoord, dus met se. En op à l'avance: een "
                "vaste uitdrukking, die je niet woord voor woord kan bouwen.",
                "Zolang als. Let op dat tant que met de indicatief gaat, ook als het over de "
                "toekomst gaat: tant que le kérosène ne sera pas taxé.",
            ],
        ),
        dict(
            aanpak="Een reisverslag mengt lof en klacht. Zoek eerst wat positief is, dan de "
                   "klachten, en kijk waar het eindigt: par contre en quand même markeren de "
                   "bochten.",
            waarom=[
                "Gemengd maar overwegend positief, en het bewijs staat op het einde: je recommande "
                "quand même. Wie toch aanraadt, is niet negatief, hoeveel klachten hij ook geeft.",
                "Noem beide klachten, dus ook de prijs. Pour le prix, j'attendais mieux is een "
                "klacht in een beleefde vorm, en die moet je als klacht lezen.",
                "Je recommande quand même. Quand même betekent toch, en het verraadt dat het "
                "oordeel ondanks de klachten positief blijft.",
            ],
        ),
        dict(
            aanpak="Hier moet je niet meer zoeken maar vergelijken. Kijk naar de persoon, naar de "
                   "soort woorden (cijfers of meningen) en naar wie er aangesproken wordt.",
            waarom=[
                "Noem telkens een verschil dat je in de taal kan aanwijzen, niet in de inhoud. De "
                "imperatief prenez is daarvan het duidelijkste voorbeeld: een artikel spreekt zijn "
                "lezer niet zo aan.",
                "Hier is elk goed onderbouwd antwoord juist. Zeg er wel bij waarom die vraag "
                "belangrijk is, dan wordt het een argument en geen opsomming.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-en-de-bedoeling-van-een-tekst-beyond"] = dict(
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
                "optelt. Deze vier woorden zijn precies wat een betoog overzichtelijk maakt, en ze "
                "staan vooraan in de zin.",
            ],
        ),
        dict(
            aanpak="Het Frans heeft drie registers: soutenu voor een brief of een officiële mail, "
                   "courant voor gewoon gebruik, familier onder vrienden. Hoe langer en hoe meer "
                   "hulpwerkwoorden, hoe formeler.",
            waarom=[
                "Let op de twee soutenu-vormen: je vous saurais gré de en veuillez agréer zijn "
                "vaste formules die je niet woord voor woord mag vertalen. En truc en c'est nul "
                "horen bij het familier register, dus niet in een schooltaak.",
                "Vous. Tutoyer doe je enkel bij wie je kent of onder jongeren; in een mail aan een "
                "onbekende is vous de enige veilige keuze.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-franstalige-wereld-omgangsvormen-en-gewoontes-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee vragen beslissen: ken ik deze persoon, en is hij van mijn leeftijd? Twee "
                   "keer ja geeft tu, voor de rest neem je vous. In twijfel is vous altijd de "
                   "veilige keuze.",
            waarom=[
                "Let op de moeder van een vriend: ouder dan jij en niet echt bekend, dus vous. En "
                "op de mail aan een stagebegeleider: in elke werkrelatie begin je met vous, ook bij "
                "iemand van je eigen leeftijd.",
                "Noem dat je wacht tot hij het voorstelt en noem de formule on peut se tutoyer. In "
                "Frankrijk wordt zelf overschakelen als te familiair gevoeld, en dat is een "
                "verschil met Vlaanderen.",
            ],
        ),
        dict(
            aanpak="Deze woorden hoor je in elk gesprek en in elke film, maar ze hebben geen "
                   "letterlijke Nederlandse tegenhanger. Leer ze met het moment of het gebruik "
                   "erbij.",
            waarom=[
                "Let op la rentrée: niet enkel de eerste schooldag maar de hele terugkeer na de "
                "zomer, ook op het werk en in de politiek. En le bac is het Franse diploma van het "
                "secundair; Belgie heeft dat examen niet.",
                "De veertiende juli, de bestorming van de Bastille in 1789. In Belgie is de "
                "nationale feestdag 21 juli, en dat is een handige vergelijking.",
                "Bonjour. In Frankrijk is een vraag zonder bonjour onbeleefd, ook aan een loket of "
                "in een winkel. Het is het woord dat de deur opent.",
            ],
        ),
        dict(
            aanpak="Frans is niet van Frankrijk alleen. Leer bij elk gebied één voorbeeld, en leer "
                   "de varianten als paar: de Belgische of Canadese vorm naast de Franse.",
            waarom=[
                "Let op Marokko: Frans is daar geen officiële taal, want dat zijn het Arabisch en "
                "het Amazigh, maar het wordt veel gebruikt in het onderwijs, het bestuur en de "
                "handel. Senegal en de Democratische Republiek Congo hebben het wel als officiële "
                "taal.",
                "Let op septante en nonante: die gebruiken wij en de Zwitsers, Frankrijk zegt "
                "soixante-dix en quatre-vingt-dix. En op la fin de semaine: dat is Quebecs, want "
                "daar vermijdt men Engelse woorden veel meer dan in Frankrijk.",
                "Noem dat je ze tegenkomt in teksten en gesprekken. Het punt is niet welke vorm "
                "beter is, maar dat geen van de twee een fout is.",
            ],
        ),
        dict(
            aanpak="Dit zijn vaste wendingen voor een gesprek: verontschuldigen, antwoorden, "
                   "feliciteren, bedanken en beleefd vragen. Leer ze als geheel en spreek ze "
                   "luidop uit.",
            waarom=[
                "Let op désolé met een e erbij als een meisje het zegt: désolée. En op pourriez-"
                "vous, de conditionnel: die maakt een vraag beleefd, terwijl pouvez-vous directer "
                "klinkt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-literaire-teksten-en-literatuurbeleving-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer eerst het gereedschap om over een verhaal te praten: wie vertelt, wie "
                   "speelt mee, wat gebeurt er, waar en wanneer, en waarover gaat het. Daarmee kan "
                   "je elk boek bespreken.",
            waarom=[
                "Let op le cadre: dat is de plaats én de tijd samen, wat in het Engels the setting "
                "heet. En l'intrigue is de verhaallijn, niet de intrige in de zin van een complot.",
                "Let op une bande dessinée: in het Frans is een strip een volwaardig genre, met "
                "eigen prijzen en een eigen plaats in de boekhandel.",
                "Een kortverhaal en een nieuwtje. Dus les nouvelles aan de radio zijn het nieuws, "
                "en une nouvelle de Maupassant is een kortverhaal.",
            ],
        ),
        dict(
            aanpak="Vier stijlfiguren met een eenvoudige test: staat er comme, dan is het een "
                   "vergelijking. Doet een ding iets menselijks, dan is het een personificatie. Is "
                   "het schromelijk overdreven, dan een hyperbool.",
            waarom=[
                "Let op mille fois: niemand bedoelt duizend, en dat is precies wat een hyperbool "
                "is. En le vent murmure geeft de wind een menselijke daad.",
                "De vergelijking gebruikt comme en zegt dus dat iets óp iets anders lijkt; de "
                "metafoor laat dat woordje weg en zegt dat het iets anders ís. Daarom is een "
                "metafoor sterker.",
            ],
        ),
        dict(
            aanpak="Bij een literair fragment staat het antwoord zelden letterlijk in de tekst. "
                   "Zoek de details, de geuren, de gebaren, de getallen, en vraag je af wat ze "
                   "verraden.",
            waarom=[
                "De reuk: la cire en le pain froid. Dat een schrijver met een geur begint, zet je "
                "meteen in het huis, en dat is een keuze en geen toeval.",
                "Noem wat het gebaar verraadt zonder dat het er staat. Dat is precies wat men "
                "literair lezen noemt: de tekst zegt het niet, en toch weet je het.",
                "Noem het gevoel én waaraan je het ziet. Zonder dat tweede deel is het een gok; "
                "met de tas in de hand en het tellen tot tien is het een onderbouwd antwoord.",
                "Passé composé, en die duwt het verhaal vooruit. Zet dat naast la pluie tombait in "
                "de imparfait: dat is het decor, en dat verschil komt in de bundel over de verleden "
                "tijden terug.",
            ],
        ),
        dict(
            aanpak="Hier schrijf je zelf, in het Frans. Gebruik de gevraagde wendingen en zet bij "
                   "elke mening een reden, want een mening zonder reden is geen antwoord.",
            waarom=[
                "Houd het bij drie volle zinnen. Let op ce qui m'a frappé, c'est: die constructie "
                "met c'est erna is vast, en ze laat je mooi iets uitlichten.",
                "Deze vier zinnen kan je in elke boekbespreking gebruiken. Let op m'a touché en m'a "
                "déçu: het lijdend voorwerp me staat vóór het werkwoord, dus gaat het deelwoord "
                "ermee mee. Is een meisje aan het woord, dan schrijft ze m'a touchée en m'a déçue.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-en-schriftelijke-interactie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Bij een schrijftaak wordt niet enkel je Frans beoordeeld maar ook of je de "
                   "opdracht uitvoert. Lees de opdracht dus twee keer en vink af wat erin gevraagd "
                   "wordt.",
            waarom=[
                None,
                "Un paragraphe. Let op: une alinéa bestaat in het Frans niet in die betekenis; un "
                "alinéa is wel het inspringen of een lid van een wetsartikel.",
                "Noem dat je doel bereikt is en dat de lezer weet wat hij moest weten. Dat is wat "
                "taakvoltooiing betekent, en het staat los van de taalfouten.",
                "Niet waar, en dit is de belangrijkste les van de reeks. Een foutloze tekst over "
                "iets anders scoort op taakvoltooiing nul, want de lezer weet nog niet wat hij "
                "moest weten.",
            ],
        ),
        dict(
            aanpak="Een formele brief heeft een vaste orde: aanspreking, aanleiding, uitleg, "
                   "bedanking, slotformule, naam. Die orde is in het Frans strikter dan bij ons, "
                   "dus leer ze als een vast schema.",
            waarom=[
                "Let op Madame, Monsieur zonder cher als je de naam niet kent. En op de "
                "slotformule: veuillez agréer mes salutations distinguées hoort bij een onbekende, "
                "cordialement is minder formeel.",
                "Houd het bij twee zinnen en zet in de eerste meteen waarover het gaat. Je me "
                "permets de vous écrire au sujet de is de vaste opening, en daarna volgt je echte "
                "vraag.",
            ],
        ),
        dict(
            aanpak="De conditionnel maakt een vraag beleefd: je voudrais in plaats van je veux, "
                   "pourriez-vous in plaats van pouvez-vous. Dat is in het Frans geen opsmuk maar "
                   "de gewone omgangsvorm.",
            waarom=[
                "Let op j'aimerais: dat betekent ik zou graag, terwijl j'aime ik hou van betekent. "
                "En auriez-vous l'amabilité de is de hoffelijkste vorm van alle vier.",
            ],
        ),
        dict(
            aanpak="Let bij het nalezen op drie dingen in deze orde: de overeenkomst van het "
                   "werkwoord met zijn onderwerp, de keuze tussen avoir en être, en de "
                   "overeenkomst van het bijvoeglijk naamwoord.",
            waarom=[
                "Let op de derde: école is vrouwelijk en begint met een klinker, dus wordt à la "
                "école tot à l'école. Au bestaat enkel als samentrekking van à le, en dat is de "
                "fout die hier gemaakt wordt.",
                "Noem wat je nakijkt: de werkwoordsvormen en de overeenkomst. Dat zijn de twee "
                "plaatsen waar de meeste punten te rapen zijn, en net daar gaat het snelst mis als "
                "je haast hebt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-de-mens-gezondheid-eten-en-wonen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer bij elk woord ook zijn vrouwelijke vorm, want die is in het Frans vaak "
                   "anders: fier wordt fière, un cousin wordt une cousine. En leer de uitdrukkingen "
                   "als geheel.",
            waarom=[
                "Let op un parent: dat is zowel een ouder als een familielid, dus de betekenis "
                "hangt van de context af. En op fier, fière: de vrouwelijke vorm krijgt een accent "
                "grave.",
                "Dit zijn vaste uitdrukkingen die je niet woord voor woord kan bouwen. Let op "
                "s'entendre bien avec: wederkerend én met avec, en op en avoir assez de, waarin de "
                "en niet te vertalen is.",
            ],
        ),
        dict(
            aanpak="Bij ziekte en gezondheid werkt het Frans met avoir mal à plus het lichaamsdeel. "
                   "Leer dat ene patroon, en de helft van dit woordveld volgt eruit.",
            waarom=[
                "Let op une ordonnance: een voorschrift van de dokter. Het woord betekent ook een "
                "verordening, en in het Frans van de rechtbank een beschikking.",
                "Noem het patroon avoir mal à la tête. En let op het bezittelijk: in het Frans zeg "
                "je bij een lichaamsdeel meestal la en niet ma, dus j'ai mal à la tête en niet à ma "
                "tête.",
            ],
        ),
        dict(
            aanpak="Eten is een woordveld waar Frankrijk en Belgie van elkaar verschillen. Leer de "
                   "woorden en let apart op de namen van de maaltijden.",
            waarom=[
                "Let op faire la vaisselle: afwassen, met faire en niet met laver. En op à "
                "emporter, de vaste uitdrukking op elke frituur en elk restaurant.",
                "Noem beide: bij ons het middagmaal, in Frankrijk het avondmaal. Daarom zegt men in "
                "Frankrijk déjeuner voor het middagmaal, terwijl dat bij ons het ontbijt lijkt.",
            ],
        ),
        dict(
            aanpak="Wonen leer je per paar: huurder en eigenaar, gelijkvloers en zolder. En let op "
                   "de werkwoorden: déménager voor verhuizen, ranger voor opruimen.",
            waarom=[
                "Let op le rez-de-chaussée: het gelijkvloers, en de eerste verdieping heet dan le "
                "premier étage. En op un locataire tegenover le propriétaire: de huurder betaalt, "
                "de eigenaar bezit.",
                "Let op une tâche met een accent circonflexe: dat is een taak, terwijl une tache "
                "zonder accent een vlek is. Eén dakje scheelt dus een hele betekenis.",
                "Houd het bij drie volle zinnen en gebruik il y a, want daarmee kan je alles "
                "opsommen wat in een kamer staat. Let op de overeenkomst: les murs sont blancs, met "
                "de s erbij.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-reizen-en-de-samenleving-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="School en werk zijn woordvelden met vaste combinaties. Leer het werkwoord altijd "
                   "mee: réussir un examen, postuler pour un emploi, prendre des notes.",
            waarom=[
                "Let op une matière: een vak, terwijl un cours een les of een cursus is. En op "
                "réussir un examen: slagen, niet afleggen, en dat is wat oefening 3 uitlegt.",
                "Let op être licencié voor ontslagen worden, met être, en op au chômage voor "
                "werkloos. En un entretien betekent zowel een gesprek als een onderhoud, dus de "
                "context beslist.",
                "Een examen afleggen, dus enkel deelnemen. J'ai passé l'examen zegt niets over het "
                "resultaat; wil je zeggen dat je geslaagd bent, dan is het j'ai réussi.",
            ],
        ),
        dict(
            aanpak="Reiswoorden heb je nodig in een gesprek aan een loket of in een klacht. Leer ze "
                   "met hun lidwoord, want veel ervan zijn mannelijk ondanks hun Nederlandse "
                   "tegenhanger.",
            waarom=[
                "Let op les bagages: in het Frans meervoud, terwijl het Engelse luggage onteltbaar "
                "is. En op une grève: een staking, niet te verwarren met la grève in de betekenis "
                "van het strand.",
                "Un voyage is de hele reis, un trajet het stuk weg dat je aflegt. Daarom zegt men "
                "le trajet entre Bruxelles et Namur, en bon voyage als iemand vertrekt.",
                "Let op avait une heure de retard: de imparfait voor de toestand, en de vaste "
                "constructie avoir du retard. En rater is missen, van een trein of een afspraak.",
            ],
        ),
        dict(
            aanpak="Woorden over de samenleving komen in elke krantentekst voor. Leer ze samen met "
                   "hun werkwoord: manifester, voter, faire du bénévolat.",
            waarom=[
                "Let op un citoyen, une citoyenne, en op manifester: betogen, terwijl une "
                "manifestation de betoging is. Un réfugié is een vluchteling met erkenning, un "
                "demandeur d'asile iemand die ze aanvraagt.",
                "Let op un impôt met een stille p, en op un syndicat: een vakbond, niet een "
                "syndicaat in de zin van een bedrijf.",
                "Houd het bij drie volle zinnen met à mon avis en parce que. Let op il faut que: "
                "daarna komt de subjonctif, dus que ce soit en niet que c'est.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-naamwoorden-lidwoorden-en-determinanten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het geslacht leer je het snelst aan de uitgang. Vrouwelijk zijn bijna altijd "
                   "de woorden op -tion, -té en -ée; mannelijk die op -age, -ment en -eau. De rest "
                   "leer je met het lidwoord erbij.",
            waarom=[
                "Let op le problème en le musée: die lijken vrouwelijk door hun e maar zijn het "
                "niet. En l'eau is vrouwelijk, ook al zie je dat niet aan het lidwoord, want voor "
                "een klinker wordt la altijd l'.",
                "De uitgang -tion. Daarom is la nation, la question en la solution vrouwelijk, "
                "terwijl -age en -ment mannelijk zijn: le voyage, le gouvernement.",
            ],
        ),
        dict(
            aanpak="Het meervoud krijgt een s, behalve bij de vaste groepen: -al wordt -aux, -eau "
                   "wordt -eaux, en wie al op -s, -x of -z eindigt, verandert niet.",
            waarom=[
                "Let op des yeux: het meervoud van un oeil is helemaal anders, en dat moet je "
                "gewoon kennen. Un travail wordt des travaux, net als un journal en un cheval.",
                "Het blijft hetzelfde: un prix, des prix. Enkel het lidwoord verraadt dan het "
                "meervoud, en in de uitspraak hoor je het niet.",
            ],
        ),
        dict(
            aanpak="Drie soorten lidwoorden, drie vragen. Gaat het over iets in het algemeen, dan "
                   "le of la. Over één exemplaar, dan un of une. Over een onbepaalde hoeveelheid, "
                   "dan het delend lidwoord du, de la of des.",
            waarom=[
                "Let op het verschil tussen j'aime le fromage (kaas in het algemeen) en il achète "
                "du pain (een onbepaalde hoeveelheid). En op je ne mange pas de viande: in een "
                "ontkenning wordt du of de la gewoon de.",
                "Du, de la en des worden de of d'. Dus je bois du café wordt je ne bois pas de "
                "café, en dat is een van de regels die het vaakst vergeten wordt.",
            ],
        ),
        dict(
            aanpak="Een determinant moet mee met het woord erna. Ce, cette, ces voor dit en deze, "
                   "met cet voor een mannelijk woord dat met een klinker begint, en de "
                   "bezittelijke vormen mon, ton, son, notre, votre, leur.",
            waarom=[
                "Let op cet arbre: mannelijk én met een klinker, dus cet en niet ce. En op leur "
                "décision: leur blijft onveranderd in het enkelvoud, leurs krijgt een s bij een "
                "meervoud.",
                "Let op chaque élève est présent, met alles in het enkelvoud, en op aucune idée, "
                "dat ook enkelvoud is. Tous les en toutes les gaan daarentegen met een meervoud.",
                "Noem dat chaque één per keer bekijkt. En noem het alternatief tous les of toutes "
                "les, want dan heb je ook de oplossing voor wie het meervoud wil.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-cod-coi-y-en-en-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek het werkwoord en stel twee vragen: qui of quoi geeft het COD, à qui geeft "
                   "het COI. Staat er à of au voor, dan is het bijna altijd een COI.",
            waarom=[
                "Let op téléphoner à en répondre à: in het Nederlands bellen we iemand zonder "
                "voorzetsel, in het Frans met à. Daarom zijn dat COI's, en dat bepaalt welk "
                "voornaamwoord je straks neemt.",
                "Qui of quoi voor het COD, à qui voor het COI. Doe die proef altijd eerst, want "
                "wie de soort verkeerd bepaalt, kiest ook het verkeerde voornaamwoord.",
            ],
        ),
        dict(
            aanpak="Het COD wordt le, la of les; het COI wordt lui of leur. Het voornaamwoord komt "
                   "vóór het werkwoord, en voor een klinker wordt le of la tot l'.",
            waarom=[
                "Let op lui en leur: die gebruik je voor zowel een man als een vrouw, want ze "
                "vervangen een COI. En op je l'ai vu: het voornaamwoord komt voor het "
                "hulpwerkwoord, niet voor het deelwoord.",
                "Tussen ne en het werkwoord: elle ne le connaît pas. De twee delen van de "
                "ontkenning blijven dus om het hele geheel staan.",
            ],
        ),
        dict(
            aanpak="Y en en zijn twee kleine woorden met elk één taak. Y vervangt wat met à staat "
                   "of een plaats; en vervangt wat met de staat of een hoeveelheid.",
            waarom=[
                "Let op elle en a trois: en vervangt het naamwoord en het getal blijft staan. En "
                "op j'en reviens: revenir de, dus en, terwijl aller à y geeft.",
                "Noem beide regels, elk in één zin. Een handig steuntje: à geeft y, de geeft en, en "
                "beide woordjes bevatten letterlijk de klank van hun voorzetsel.",
            ],
        ),
        dict(
            aanpak="Staan er twee voornaamwoorden samen, dan geldt een vaste orde. Met me, te, "
                   "nous of vous komen die eerst; met lui of leur komt le, la of les eerst. Y en en "
                   "staan altijd achteraan.",
            waarom=[
                "Let op il y en a: y staat voor en, en dat is de orde die je ook in il y a terug "
                "ziet. Bij il le lui donne komt het COD eerst omdat het tweede een lui is.",
                "Eerst me, te, nous, vous, dan le, la, les. Dus elle me la montre, en niet elle la "
                "me montre.",
                "Eerst le, la, les, dan lui, leur. Dus il le lui donne, precies omgekeerd aan de "
                "vorige regel, en dat is wat deze reeks moeilijk maakt.",
            ],
        ),
        dict(
            aanpak="Vier betrekkelijke voornaamwoorden met elk hun plaats: qui als onderwerp, que "
                   "als lijdend voorwerp, où bij een plaats of een tijd, dont bij een de.",
            waarom=[
                "Let op dont: dat gebruik je waar het Frans de of du vraagt, zoals parler de of le "
                "nom de. Daarom le film dont tout le monde parle en l'auteur dont je connais le nom.",
                "Qui als er geen onderwerp volgt, que als er wel een onderwerp volgt. Een snelle "
                "proef: komt er na het woordje meteen een werkwoord, dan is het qui.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een bijvoeglijk naamwoord gaat mee met zijn naamwoord in geslacht en getal. De "
                   "gewone regel is een e voor vrouwelijk en een s voor meervoud; de rest zijn "
                   "groepen die je moet kennen.",
            waarom=[
                "Let op de onregelmatige: blanc wordt blanche, frais wordt fraîche, fou wordt "
                "folle. En op vieux en sérieux: woorden op -eux worden vrouwelijk -euse, maar in "
                "het mannelijk meervoud verandert er niets.",
            ],
        ),
        dict(
            aanpak="In het Frans staat het bijvoeglijk naamwoord meestal achter het naamwoord. "
                   "Enkel een kleine groep korte, veelgebruikte woorden staat ervoor: beau, bon, "
                   "grand, petit, jeune, vieux, nouveau.",
            waarom=[
                "Let op het patroon: kleur en herkomst staan altijd achteraan (rouge, italien), "
                "de korte woorden ervoor (grande, jeune, belle). Une belle histoire, want beau "
                "wordt belle voor een vrouwelijk woord.",
                "De korte en vaak gebruikte. Een handig steuntje uit het Engels: BAGS, voor "
                "beauty, age, goodness en size, en dat dekt precies die groep.",
                "Noem beide betekenissen. Dat de plaats de betekenis verandert, geldt bij meer "
                "woorden: un ancien élève is een oud-leerling, un élève ancien een oude leerling.",
            ],
        ),
        dict(
            aanpak="Een bijwoord maak je van de vrouwelijke vorm plus -ment: lente wordt lentement. "
                   "Woorden op -ent en -ant worden -emment en -amment, en bon en mauvais hebben een "
                   "eigen vorm.",
            waarom=[
                "Let op évidemment en couramment: die klinken beide als amment, en toch schrijft "
                "de eerste emment, naar évident. En bon wordt bien, mauvais wordt mal: geen "
                "ment-vorm.",
                "Van de vrouwelijke vorm: heureuse wordt heureusement. Daarom is het ook lentement "
                "en niet lentment, want je vertrekt van lente.",
            ],
        ),
        dict(
            aanpak="De trappen gaan met plus, le plus, aussi en moins, plus que om te vergelijken. "
                   "Drie woorden hebben een eigen vorm: bon wordt meilleur, bien wordt mieux, "
                   "mauvais wordt pire.",
            waarom=[
                "Let op het verschil tussen meilleur en mieux: meilleur hoort bij bon en staat bij "
                "een naamwoord, mieux hoort bij bien en staat bij een werkwoord. Il chante mieux, "
                "maar c'est un meilleur chanteur.",
                "Ce livre est meilleur que l'autre. Plus bon bestaat niet, en plus meilleur is een "
                "dubbele trap, dus ook fout.",
                "Que. Dus plus grand que, aussi cher que, moins cher que: altijd que en nooit "
                "comme, en dat is een valkuil voor wie uit het Nederlands vertaalt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-verleden-tijden-en-de-accord-van-het-deelwoord-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De deelwoorden van de regelmatige werkwoorden volgen hun groep (-é, -i, -u). "
                   "De onregelmatige moet je kennen, en ze zitten in kleine groepjes: pris, mis, "
                   "écrit eindigen alle op een consonant die je niet hoort.",
            waarom=[
                "Let op né en mort: die hoor je zelden in een andere vorm, en toch komen ze vaak "
                "voor. En op dû met een accent circonflexe, om het te onderscheiden van du.",
            ],
        ),
        dict(
            aanpak="De meeste werkwoorden nemen avoir. Être nemen de wederkerende werkwoorden en "
                   "een kleine groep van beweging en verandering: aller, venir, partir, rester, "
                   "naître, mourir en hun familie.",
            waarom=[
                "Let op de laatste: il a descendu l'escalier met avoir, want er staat een lijdend "
                "voorwerp. Zonder voorwerp zou het il est descendu zijn, en dat is wat oefening 3 "
                "uitlegt.",
                "Noem het verschil met en zonder lijdend voorwerp, en noem de andere werkwoorden "
                "die het ook doen. Dat zijn monter, sortir, rentrer en passer.",
            ],
        ),
        dict(
            aanpak="Drie regels, in deze orde. Met être gaat het deelwoord mee met het onderwerp. "
                   "Met avoir gaat het mee als het lijdend voorwerp ervóór staat. Bij een "
                   "wederkerend werkwoord gaat het mee met het onderwerp.",
            waarom=[
                "Vergelijk de derde en de vierde: elle a mangé la pomme zonder overeenkomst, la "
                "pomme qu'elle a mangée met overeenkomst. Alleen de plaats van het voorwerp "
                "verschilt, en dat is de hele regel.",
                "Als het lijdend voorwerp vóór het werkwoord staat, dus bij que, bij les, of bij "
                "een vraag met quelle. Daarom je les ai vus met een s erbij.",
            ],
        ),
        dict(
            aanpak="De imparfait is het decor: wat al bezig was, wat gewoonlijk gebeurde, hoe iets "
                   "was. De passé composé is de gebeurtenis die het verhaal vooruit duwt. Woorden "
                   "als chaque dimanche en quand j'étais petit wijzen naar de imparfait, soudain en "
                   "hier naar de passé composé.",
            waarom=[
                "Let op het patroon in de derde en de zesde: de lange handeling in de imparfait, de "
                "korte die ertussen komt in de passé composé. Il pleuvait quand je suis sorti.",
                "De imparfait het decor, de passé composé de gebeurtenis. Met die ene regel kan je "
                "bijna elke keuze in een verhaal maken.",
            ],
        ),
        dict(
            aanpak="De plus-que-parfait is het verleden van het verleden: je neemt de imparfait van "
                   "avoir of être plus het deelwoord. Je hebt er dus altijd twee momenten voor "
                   "nodig.",
            waarom=[
                "Let op dat de keuze tussen avoir en être dezelfde blijft als in de passé composé: "
                "elle était partie met être, nous avions vu met avoir.",
                "Geef een eigen voorbeeld met twee momenten en zet ze in de juiste orde. Zonder "
                "dat tweede moment is er geen reden om de plus-que-parfait te gebruiken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-futur-conditionnel-subjonctif-en-de-gerundif-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De futur bouw je op de infinitief plus de uitgangen van avoir. Een handvol "
                   "werkwoorden heeft een eigen stam, en die moet je kennen: aller geeft ir-, faire "
                   "geeft fer-, voir geeft verr-.",
            waarom=[
                "Let op de onregelmatige stammen: ils iront, je ferai, vous viendrez, on pourra, je "
                "verrai. De uitgangen zijn wel altijd dezelfde, ook daar.",
                "De vormen van avoir: ai, as, a, ons, ez, ont. Daarom is je parlerai letterlijk "
                "parler plus ai, en dat is een handige manier om de uitgangen nooit meer te "
                "vergeten.",
            ],
        ),
        dict(
            aanpak="De conditionnel heeft dezelfde stam als de futur, maar met de uitgangen van de "
                   "imparfait. Ken je de futur, dan ken je de conditionnel ook.",
            waarom=[
                "Let op je voudrais en on devrait: dat zijn de twee vormen die je het vaakst nodig "
                "hebt, voor een beleefde vraag en voor een raad.",
                "In een si-zin staat de imparfait en in de hoofdzin de conditionnel: si j'avais le "
                "temps, je viendrais. Na si komt dus nooit de conditionnel zelf.",
                "De imparfait. Dat is de vaste combinatie, net zoals si plus présent bij een futur "
                "hoort: si j'ai le temps, je viendrai.",
            ],
        ),
        dict(
            aanpak="De subjonctif maak je van de stam van ils in de tegenwoordige tijd, plus de "
                   "uitgangen e, es, e, ions, iez, ent. Hij komt na que bij een wil, een "
                   "noodzaak, een gevoel of een twijfel.",
            waarom=[
                "Let op de onregelmatige: qu'il soit, que nous ayons, qu'elle aille, que je fasse, "
                "que vous puissiez, qu'on sache. Dat zijn precies de werkwoorden die je het meest "
                "gebruikt.",
                "Let op de laatste: na je pense que komt de indicatif, want het wordt als een feit "
                "gesteld. Il faut que, je veux que en bien que vragen wel de subjonctif.",
                "Noem het verschil tussen een feit stellen en twijfelen. Dat is het hele criterium: "
                "de subjonctif hoort bij wat gewild, gevreesd of betwijfeld wordt, niet bij wat "
                "vaststaat.",
            ],
        ),
        dict(
            aanpak="De gérondif is en plus de vorm op -ant. Hij zegt hoe of wanneer iets gebeurt, "
                   "en het onderwerp van beide delen moet hetzelfde zijn.",
            waarom=[
                "Let erop dat de twee handelingen van dezelfde persoon zijn: il travaille en "
                "chantant, hij zingt en werkt zelf. Bij twee verschillende personen kan de gérondif "
                "niet.",
                "Let op de drie onregelmatige: en ayant, en étant, en sachant. De rest volgt gewoon "
                "uit de nous-vorm.",
                "Van nous in de tegenwoordige tijd, zonder de uitgang ons: nous faisons geeft en "
                "faisant. Dat is dezelfde stam als die van de imparfait.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsbouw-indirecte-rede-en-de-passieve-zin-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het Frans heeft drie manieren om een vraag te stellen: met de stem alleen, met "
                   "est-ce que, en met de omkering. De derde is de meest formele en de enige waar "
                   "je op een streepje moet letten.",
            waarom=[
                "Let op Que fais-tu: in de omkering wordt qu'est-ce que gewoon que. En op het "
                "streepje tussen werkwoord en voornaamwoord, dat in de omkering altijd nodig is.",
                "Om twee klinkers te scheiden: habite eindigt op een e en il begint met een i, dus "
                "komt er een t tussen. Hetzelfde bij a-t-il en va-t-elle.",
            ],
        ),
        dict(
            aanpak="Een ontkenning in het Frans heeft twee delen: ne en een tweede woord. Dat "
                   "tweede woord bepaalt de betekenis: pas, plus, jamais, rien, personne.",
            waarom=[
                "Let op de plaats bij een samengestelde tijd: je n'ai vu personne, dus ne voor het "
                "hulpwerkwoord en personne na het deelwoord. Bij pas encore staat het wel "
                "ertussen: il n'est pas encore parti.",
            ],
        ),
        dict(
            aanpak="In de indirecte rede verschuift alles een stap: de tijd, de persoon en de "
                   "vraagvorm. Een vraag zonder vraagwoord wordt si, een bevel wordt de plus "
                   "infinitief.",
            waarom=[
                "Let op de eerste: na il dit in de tegenwoordige tijd verschuift er niets. Pas na "
                "een inleiding in het verleden gaat présent naar imparfait, en dat is wat de tabel "
                "erna geeft.",
                "Vul de vier verschuivingen in. De imparfait blijft imparfait, want verder terug "
                "dan de plus-que-parfait gaat het niet.",
                "Si. Dus elle m'a demandé si je venais, en niet que je venais; dat laatste zou een "
                "mededeling zijn in plaats van een vraag.",
            ],
        ),
        dict(
            aanpak="De passieve vorm maak je met être plus het deelwoord, en het deelwoord gaat mee "
                   "met het onderwerp. De dader komt er met par bij, of verdwijnt.",
            waarom=[
                "Let op de tijd: être staat in de tijd van de actieve zin. Ont écrit geeft ont été "
                "écrits, on construira geeft sera construite.",
                "Noem dat on geen echte dader noemt. Daarom is de passieve zin zonder par hier "
                "precies de juiste vertaling van on.",
                "Met être, en het deelwoord gaat mee met het onderwerp. Daarom la photo a été "
                "prise, met een e erbij, en ces textes ont été écrits, met een s.",
            ],
        ),
    ],
)

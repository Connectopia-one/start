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
                  [["présent", "imparfait"], ["passé composé", "plus-que-parfait"],
                   ["futur simple", "conditionnel présent"], ["imparfait", "imparfait"]],
                  "Vul de tabel aan: welke tijd wordt wat?", "170px"),
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

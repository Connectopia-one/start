# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van Frans 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Dezelfde leerstof en dezelfde woorden, maar een andere richting: waar
het scherm vraagt wat een woord betekent, vraagt de bundel om het zelf te
schrijven. Zo moet een kind twee keer nadenken in plaats van twee keer hetzelfde
antwoord op te schrijven. Wie hier iets bijschrijft, legt het dus eerst naast de
vragen in `../../start/frans.json` en `../../start/frans-prenten.json`.

Bij een taalvak staat het invulvakje breder dan bij wiskunde: "vendredi" past
niet in een vakje dat voor een getal van twee cijfers gemaakt is.

De twee laatste bundels horen bij de hoofdstukken waarin je beschrijft wat je
ziet. Die krijgen **de prent zelf** mee, ingebakken in de pdf, zodat de oefening
ook op papier werkt. DE PRENT IS DE BRON: elke oefening erover is nageteld op
het beeld. Maakt iemand later een nieuwe prent, dan moeten die oefeningen
opnieuw geschreven worden, net als de vragen op het scherm.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

PRENTEN = pathlib.Path(__file__).resolve().parents[3] / "public" / "prenten" / "frans"

W = "120px"    # een los woord
WW = "170px"   # een lang woord of twee woorden
WL = "240px"   # een kort zinnetje

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Weet je een woord niet meer? Sla het over en kom er op het einde op terug.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

HOE_PRENT = [
    "Kijk eerst een hele minuut naar de prent, voor je iets opschrijft.",
    "Twijfel je tussen twee antwoorden? Kijk nog eens naar de prent, niet naar de woorden.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def prent(naam):
    """De prent van een beschrijfhoofdstuk, ingebakken in de pdf."""
    return bundel.foto(PRENTEN / f"{naam}.webp", breedte="100%")


# ============================================================
OEFENBUNDELS["oefenbundel-woorden-voor-elke-dag"] = dict(
    vak="Frans", titel="Woorden voor elke dag",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tellen",
             opdracht="Let op de valstrikken: cinq en quinze en cinquante lijken op elkaar.",
             oefeningen=[
                 ("rij", [("6", "six"), ("12", "douze"), ("15", "quinze"),
                          ("9", "neuf"), ("17", "dix-sept"), ("20", "vingt")],
                  "Schrijf het getal voluit in het Frans.", WW),
                 ("rij", [("quatorze", "14"), ("trente", "30"),
                          ("cinquante", "50"), ("huit", "8"), ("cent", "100")],
                  "Schrijf het getal in cijfers.", "70px"),
                 ("kort", "Welk getal komt vlak na dix-huit?", "dix-neuf", WW),
                 ("kort", "Welk getal komt vlak voor treize?", "douze", WW),
                 ("kies", "Welk getal is het grootst?",
                  ["quinze", "cinquante", "cinq", "quarante"], 1),
                 ("waar", "Vanaf dix-sept plak je twee getallen aan elkaar: dix en sept.", True),
             ]),

        dict(kop="Kleuren",
             opdracht="Schrijf het Franse woord op de lijn.",
             oefeningen=[
                 ("rij", [("rood", "rouge"), ("blauw", "bleu"), ("geel", "jaune"),
                          ("groen", "vert"), ("zwart", "noir"), ("wit", "blanc")],
                  "Welke kleur is het?", W),
                 ("rij", [("gris", "grijs"), ("rose", "roze"), ("brun", "bruin")],
                  "En nu andersom: wat betekent het?", W),
                 ("kies", "Welke kleur krijg je als je rouge en blanc mengt?",
                  ["rose", "gris", "vert", "jaune"], 0),
                 ("waar", "Bij een vrouwelijk woord schrijf je \"une voiture verte\", met een e erbij.",
                  True),
             ]),

        dict(kop="De dagen van de week",
             opdracht="Bijna elke dag eindigt op -di. Eén niet.",
             oefeningen=[
                 ("rij", [("dinsdag", "mardi"), ("donderdag", "jeudi"),
                          ("zaterdag", "samedi"), ("maandag", "lundi")],
                  "Schrijf de dag in het Frans.", WW),
                 ("kort", "Welke dag komt vlak voor samedi?", "vendredi", WW),
                 ("kort", "Welke dag komt vlak na dimanche?", "lundi", WW),
                 ("kies", "Welke dag eindigt NIET op -di?",
                  ["mercredi", "dimanche", "vendredi", "jeudi"], 1),
                 ("open", "Schrijf de zeven dagen in de juiste volgorde, van lundi tot dimanche.",
                  "lundi · mardi · mercredi · jeudi · vendredi · samedi · dimanche", 2),
             ]),

        dict(kop="De maanden en de seizoenen",
             opdracht="Denk aan de kleine letter: in het Frans krijgt een maand er nooit een hoofdletter.",
             oefeningen=[
                 ("rij", [("maart", "mars"), ("mei", "mai"),
                          ("september", "septembre"), ("december", "décembre")],
                  "Schrijf de maand in het Frans.", WW),
                 ("kort", "Welke maand komt vlak na juin?", "juillet", WW),
                 ("waar", "Je mag \"Janvier\" met een hoofdletter schrijven, net als in het Engels.",
                  False),
                 ("kies", "In welk seizoen valt avril?",
                  ["l'hiver", "le printemps", "l'été", "l'automne"], 1),
                 ("kort", "Hoe heet de zomer in het Frans? Schrijf het met zijn lidwoord.", "l'été", WW),
             ]),

        dict(kop="Vandaag, gisteren, morgen",
             opdracht="Drie woordjes die je elke dag nodig hebt.",
             oefeningen=[
                 ("rij", [("vandaag", "aujourd'hui"), ("gisteren", "hier"),
                          ("morgen", "demain")],
                  "Schrijf het in het Frans.", WW),
                 ("waar", "In aujourd'hui staat een apostrof in het midden.", True),
             ]),

        dict(kop="Groeten en beleefd zijn",
             opdracht="Kies wat je zou zeggen.",
             oefeningen=[
                 ("kies", "Je komt om acht uur 's morgens de klas binnen. Wat zeg je?",
                  ["Bonjour !", "Bonsoir !", "Bonne nuit !", "Au revoir !"], 0),
                 ("kies", "Je gaat slapen. Wat zeg je?",
                  ["Bonne nuit !", "Bonjour !", "Salut !", "Merci !"], 0),
                 ("kort", "Iemand zegt merci tegen jou. Wat antwoord je? (twee woordjes)",
                  "de rien", WW),
                 ("rij", [("merci beaucoup", "hartelijk dank"),
                          ("s'il vous plaît", "alstublieft"),
                          ("au revoir", "tot ziens")],
                  "Wat betekent het?", WW),
                 ("waar", "Salut zeg je zowel als je toekomt als als je weggaat.", True),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-mezelf-voorstellen"] = dict(
    vak="Frans", titel="Mezelf voorstellen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Je naam en je leeftijd",
             opdracht="Vul de zin aan.",
             oefeningen=[
                 ("kort", "Je ... appelle Sofie. (het ontbrekende woordje)", "m'", "80px"),
                 ("kort", "Vraag aan iemand hoe hij heet. Schrijf de hele vraag in het Frans.",
                  "Comment tu t'appelles ?", WL),
                 ("kort", "Je bent tien jaar. Schrijf het in het Frans, met avoir.",
                  "J'ai dix ans", WL),
                 ("kies", "Welke zin klopt?",
                  ["Je suis onze ans", "J'ai onze ans", "J'ai onze", "Je suis onze"], 1),
                 ("waar", "In het Frans zeg je dat je jaren hébt, niet dat je jaren bént.", True),
             ]),

        dict(kop="Waar je woont en waar je vandaan komt",
             opdracht="Let op het verschil tussen wonen en komen uit.",
             oefeningen=[
                 ("kort", "Ik woon in Genk. Schrijf het in het Frans.", "J'habite à Genk", WL),
                 ("kort", "Ik kom uit België. Schrijf het in het Frans.",
                  "Je viens de Belgique", WL),
                 ("kies", "Iemand zegt: \"Je viens de France.\" Wat vertelt hij?",
                  ["waar hij vandaan komt", "waar hij woont",
                   "waar hij naartoe gaat", "hoe oud hij is"], 0),
                 ("waar", "Je + habite wordt j'habite, want de h hoor je niet.", True),
             ]),

        dict(kop="Je gezin",
             opdracht="Schrijf het Franse woord, met le of la ervoor.",
             oefeningen=[
                 ("rij", [("de vader", "le père"), ("de zus", "la sœur"),
                          ("de broer", "le frère"), ("de moeder", "la mère")],
                  "Wie is het?", WW),
                 ("kort", "Hoe zeg je \"de grootouders\" in het Frans? (twee woordjes)",
                  "les grands-parents", WW),
                 ("rij", [("... frère (mijn broer)", "mon"), ("... sœur (mijn zus)", "ma"),
                          ("... parents (mijn ouders)", "mes")],
                  "Mon, ma of mes?", "80px"),
                 ("kies", "Welke zin klopt?",
                  ["Ma père s'appelle Tom", "Mon père s'appelle Tom",
                   "Mes père s'appelle Tom", "Me père s'appelle Tom"], 1),
                 ("open", "Schrijf in het Frans wie er bij jou thuis wonen. Begin met \"Chez moi, il y a\".",
                  "Bijvoorbeeld: Chez moi, il y a mon père, ma mère et ma sœur.", 2),
             ]),

        dict(kop="Tu of vous?",
             opdracht="Tu is vertrouwd, vous is beleefd.",
             oefeningen=[
                 ("rij", [("je beste vriendin", "tu"), ("de directeur van je school", "vous"),
                          ("je kleine broer", "tu"), ("een onbekende in de winkel", "vous")],
                  "Zeg je tu of vous tegen deze persoon?", "80px"),
                 ("kies", "Je stelt jezelf voor aan de mama van een vriend. Wat zeg je?",
                  ["Salut, je m'appelle …", "Bonjour madame, je m'appelle …",
                   "Ça va, tu ?", "Au revoir madame"], 1),
                 ("waar", "Tegen je leerkracht zeg je vous.", True),
             ]),

        dict(kop="Hoe gaat het?",
             opdracht="Vul aan of vertaal.",
             oefeningen=[
                 ("kort", "Iemand vraagt \"Ça va ?\" en het gaat goed. Wat antwoord je?",
                  "Ça va bien, merci", WL),
                 ("kort", "Je ontmoet iemand voor het eerst. Welk woord zeg je? (aangenaam)",
                  "enchanté", WW),
                 ("waar", "Een meisje schrijft \"enchantée\", met een e erbij.", True),
                 ("kort", "Ik ben Belg. Schrijf het in het Frans.", "Je suis belge", WL),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-etre-en-avoir"] = dict(
    vak="Frans", titel="Être en avoir",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee rijtjes",
             opdracht="Vul de tabel aan. Kijk daarna pas naar het antwoordblad.",
             oefeningen=[
                 ("tabel", ["", "être (zijn)", "avoir (hebben)"],
                  [["je / j'", None, None], ["tu", None, None], ["il / elle", None, None],
                   ["nous", None, None], ["vous", None, None], ["ils / elles", None, None]],
                  "être: je suis · tu es · il est · nous sommes · vous êtes · ils sont — "
                  "avoir: j'ai · tu as · il a · nous avons · vous avez · ils ont"),
                 ("kort", "Welke vorm van être hoort bij vous?", "êtes", W),
                 ("kort", "Welke vorm van avoir hoort bij nous?", "avons", W),
             ]),

        dict(kop="Être of avoir?",
             opdracht="Zet er het juiste werkwoord bij. Denk: is het een toestand, of iets dat je hebt?",
             oefeningen=[
                 ("rij", [("ik heb dorst", "j'ai soif"), ("zij is lief", "elle est gentille"),
                          ("ik heb het warm", "j'ai chaud"), ("wij zijn moe", "nous sommes fatigués")],
                  "Schrijf het in het Frans.", WL),
                 ("kies", "Welke zin klopt?",
                  ["Je suis faim", "J'ai faim", "Je suis la faim", "J'ai le faim"], 1),
                 ("kies", "Hoe zeg je \"je hebt gelijk\"?",
                  ["tu es raison", "tu as raison", "tu es la raison", "tu as le raison"], 1),
                 ("waar", "\"Je suis froid\" zou betekenen dat jij zelf een koude persoon bent.",
                  True),
                 ("open", "Leg in je eigen woorden uit wanneer je avoir gebruikt en wanneer être.",
                  "Avoir voor iets dat je hebt: honger, dorst, koud, gelijk, een leeftijd. "
                  "Être voor een toestand of een eigenschap: moe, blij, lief, Belg, te laat.", 3),
             ]),

        dict(kop="Eén letter verschil",
             opdracht="Deze lijken op elkaar. Lees traag.",
             oefeningen=[
                 ("rij", [("ils sont", "zij zijn"), ("ils ont", "zij hebben"),
                          ("il est", "hij is"), ("il a", "hij heeft")],
                  "Wat betekent het?", WW),
                 ("kies", "Welke zin betekent \"zij hebben twee katten\"?",
                  ["Elles sont deux chats", "Elles ont deux chats",
                   "Elles avez deux chats", "Elles est deux chats"], 1),
                 ("kort", "Vul aan: \"Tu ... mon ami.\" (jij bent mijn vriend)", "es", "80px"),
                 ("kort", "Vul aan: \"Elle ... un vélo rouge.\" (zij heeft een rode fiets)",
                  "a", "80px"),
                 ("waar", "\"Tu es\" schrijf je met een t achteraan, net als \"il est\".", False),
             ]),

        dict(kop="Zinnen maken",
             opdracht="Schrijf hele zinnen.",
             oefeningen=[
                 ("kort", "Wij hebben een grote hond. (un grand chien)",
                  "Nous avons un grand chien", WL),
                 ("kort", "Jullie zijn te laat. (en retard)", "Vous êtes en retard", WL),
                 ("open", "Schrijf drie zinnen over jezelf: één met être, één met avoir en één met je leeftijd.",
                  "Bijvoorbeeld: Je suis belge. J'ai un chien. J'ai onze ans.", 3),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-de-tegenwoordige-tijd"] = dict(
    vak="Frans", titel="De tegenwoordige tijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De werkwoorden op -er",
             opdracht="Haal de -er eraf en plak er de uitgang van de persoon aan.",
             oefeningen=[
                 ("tabel", ["", "chanter", "regarder"],
                  [["je", None, None], ["tu", None, None], ["nous", None, None],
                   ["ils", None, None]],
                  "chanter: je chante · tu chantes · nous chantons · ils chantent — "
                  "regarder: je regarde · tu regardes · nous regardons · ils regardent"),
                 ("rij", [("je (manger)", "je mange"), ("tu (jouer)", "tu joues"),
                          ("vous (écouter)", "vous écoutez"), ("elles (parler)", "elles parlent")],
                  "Vervoeg in de tegenwoordige tijd.", WL),
                 ("kies", "Welke zin klopt?",
                  ["Je parles français", "Je parle français",
                   "Je parlons français", "Je parlez français"], 1),
                 ("waar", "De uitgang -ent hoor je niet: ils parlent klinkt als il parle.", True),
             ]),

        dict(kop="Aller: gaan",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("je", "vais"), ("nous", "allons"), ("ils", "vont"), ("tu", "vas")],
                  "Welke vorm van aller hoort erbij?", W),
                 ("kort", "Wij gaan naar school. (à l'école)", "Nous allons à l'école", WL),
                 ("kies", "Wat betekent \"Je vais manger\"?",
                  ["ik ga eten", "ik eet", "ik heb gegeten", "ik at"], 0),
                 ("open", "Schrijf in het Frans wat jij straks gaat doen. Gebruik aller + een werkwoord.",
                  "Bijvoorbeeld: Je vais jouer. Of: Je vais regarder la télé.", 2),
             ]),

        dict(kop="Faire: doen of maken",
             opdracht="Let op vous faites en ils font.",
             oefeningen=[
                 ("rij", [("je", "fais"), ("vous", "faites"), ("nous", "faisons"),
                          ("elles", "font")],
                  "Welke vorm van faire hoort erbij?", W),
                 ("kort", "Wij maken ons huiswerk. (nos devoirs)", "Nous faisons nos devoirs", WL),
                 ("kies", "Welke twee horen bij faire?",
                  ["ils font en vous faites", "ils vont en vous allez",
                   "ils sont en vous êtes", "ils ont en vous avez"], 0),
                 ("kort", "Vraag aan iemand wat hij doet. Schrijf de hele vraag.",
                  "Qu'est-ce que tu fais ?", WL),
             ]),

        dict(kop="Het weer",
             opdracht="Over het weer zegt het Frans il fait.",
             oefeningen=[
                 ("rij", [("het is koud", "il fait froid"), ("het is warm", "il fait chaud"),
                          ("het is mooi weer", "il fait beau")],
                  "Schrijf het in het Frans.", WL),
                 ("waar", "Over het weer zeg je \"il est froid\".", False),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-zinnen-bouwen"] = dict(
    vak="Frans", titel="Zinnen bouwen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Le, la, l' of les?",
             opdracht="Zet het juiste lidwoord voor het woord.",
             oefeningen=[
                 ("rij", [("... table", "la"), ("... livre", "le"), ("... école", "l'"),
                          ("... filles", "les"), ("... ami", "l'"), ("... garçon", "le")],
                  "Le, la, l' of les?", "70px"),
                 ("rij", [("... table (een)", "une"), ("... livre (een)", "un"),
                          ("... livres (enkele)", "des")],
                  "Un, une of des?", "70px"),
                 ("kort", "Zet in het meervoud: le livre", "les livres", WW),
                 ("waar", "Voor een woord dat met een klinker begint, worden le en la allebei l'.",
                  True),
             ]),

        dict(kop="Ontkennen",
             opdracht="Zet ne vóór en pas ná het werkwoord.",
             oefeningen=[
                 ("rij", [("Je parle anglais.", "Je ne parle pas anglais."),
                          ("Il aime le chocolat.", "Il n'aime pas le chocolat."),
                          ("Elle habite ici.", "Elle n'habite pas ici.")],
                  "Maak de zin ontkennend.", "260px"),
                 ("kort", "Ik heb geen hond. (un chien)", "Je n'ai pas de chien", WL),
                 ("kies", "Waarom wordt ne soms n'?",
                  ["omdat het woord erna met een klinker begint",
                   "omdat de zin lang is", "omdat het een vraag is",
                   "omdat het werkwoord op -er eindigt"], 0),
                 ("waar", "Na een ontkenning wordt un of une meestal de.", True),
             ]),

        dict(kop="Vragen stellen",
             opdracht="Denk aan de spatie voor het vraagteken.",
             oefeningen=[
                 ("rij", [("waar", "où"), ("wanneer", "quand"),
                          ("waarom", "pourquoi"), ("hoe", "comment")],
                  "Schrijf het vraagwoord in het Frans.", WW),
                 ("kort", "Maak er een vraag van met est-ce que: \"Tu aimes le chocolat.\"",
                  "Est-ce que tu aimes le chocolat ?", "260px"),
                 ("kort", "Met welk woord antwoord je meestal op pourquoi? (twee woordjes)",
                  "parce que", WW),
                 ("waar", "In het Frans schrijf je een spatie voor een vraagteken.", True),
             ]),

        dict(kop="Het bijvoeglijk naamwoord",
             opdracht="In het Frans komt het meestal achter het woord.",
             oefeningen=[
                 ("rij", [("een zwarte hond", "un chien noir"),
                          ("een rode auto", "une voiture rouge"),
                          ("een klein meisje", "une petite fille")],
                  "Schrijf het in het Frans.", WL),
                 ("kies", "Welke zin klopt?",
                  ["une rouge voiture", "un voiture rouge",
                   "une voiture rouge", "une voiture rouges"], 2),
                 ("kort", "Zet in het meervoud: une petite fille", "les petites filles", WW),
                 ("waar", "Bij een vrouwelijk woord krijgt het bijvoeglijk naamwoord meestal een e bij.",
                  True),
             ]),

        dict(kop="Woordjes die zinnen aan elkaar knopen",
             opdracht="Kies et, ou of mais.",
             oefeningen=[
                 ("rij", [("Julie ... Lucas", "et"), ("du thé ... du café ?", "ou"),
                          ("J'aime le chocolat, ... je préfère les bonbons.", "mais")],
                  "Vul aan met et, ou of mais.", "80px"),
                 ("open", "Schrijf twee zinnen over jezelf in het Frans: één gewone en één ontkennende.",
                  "Bijvoorbeeld: J'aime le foot. Je n'aime pas les tomates.", 3),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-op-school-en-onderweg"] = dict(
    vak="Frans", titel="Op school en onderweg",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In je boekentas",
             opdracht="Schrijf het Franse woord, met un of une ervoor.",
             oefeningen=[
                 ("rij", [("een schrift", "un cahier"), ("een gom", "une gomme"),
                          ("een boekentas", "un cartable"), ("een pennenzak", "une trousse")],
                  "Wat is het in het Frans?", WW),
                 ("kies", "Waarmee schrijf je als je het nog wil kunnen uitgommen?",
                  ["un stylo", "un crayon", "un livre", "une règle"], 1),
                 ("kort", "Welk Frans woord betekent zowel een lat als een afspraak?",
                  "une règle", WW),
             ]),

        dict(kop="Op school",
             opdracht="Vul aan of vertaal.",
             oefeningen=[
                 ("kort", "Hoe heet de speeltijd in het Frans? (twee woordjes)",
                  "la récréation", WW),
                 ("kort", "Hoe heet het schoolvak wiskunde in het Frans? (meervoud)",
                  "les mathématiques", WW),
                 ("rij", [("Ouvrez votre livre.", "Open je boek."),
                          ("Je ne comprends pas.", "Ik begrijp het niet."),
                          ("Répétez, s'il vous plaît.", "Herhaal, alstublieft.")],
                  "Wat zegt de leerkracht, of wat zeg jij?", "230px"),
                 ("kies", "De leerkracht spreekt te snel. Wat zeg je?",
                  ["Ouvrez votre livre.", "Répétez, s'il vous plaît.",
                   "C'est combien ?", "Au revoir !"], 1),
             ]),

        dict(kop="De weg vragen",
             opdracht="Let op: à droite en tout droit lijken op elkaar.",
             oefeningen=[
                 ("rij", [("links", "à gauche"), ("rechts", "à droite"),
                          ("rechtdoor", "tout droit")],
                  "Schrijf het in het Frans.", WW),
                 ("kies", "Iemand zegt: \"Allez tout droit.\" Wat doe je?",
                  ["je slaat links af", "je slaat rechts af",
                   "je gaat rechtdoor", "je keert om"], 2),
                 ("rij", [("une rue", "een straat"), ("une place", "een plein"),
                          ("un pont", "een brug"), ("la gare", "het station")],
                  "Wat betekent het?", WW),
                 ("waar", "\"La gare\" en \"un garage\" betekenen hetzelfde.", False),
             ]),

        dict(kop="In de winkel",
             opdracht="Waar ga je naartoe?",
             oefeningen=[
                 ("rij", [("je wil brood kopen", "la boulangerie"),
                          ("je wil een boek kopen", "la librairie"),
                          ("je wil een boek lenen", "la bibliothèque")],
                  "Welke plaats in het Frans?", WW),
                 ("kies", "Wat vraag je als je wil weten wat iets kost?",
                  ["C'est combien ?", "C'est comment ?",
                   "C'est quand ?", "C'est où ?"], 0),
                 ("waar", "Une librairie is een bibliotheek waar je boeken leent.", False),
             ]),

        dict(kop="Onderweg",
             opdracht="À of en? Op de fiets zit je erop, in de bus zit je erin.",
             oefeningen=[
                 ("rij", [("met de fiets", "à vélo"), ("te voet", "à pied"),
                          ("met de bus", "en bus"), ("met de auto", "en voiture")],
                  "Schrijf het in het Frans.", WW),
                 ("open", "Schrijf in het Frans hoe jij naar school gaat. Begin met \"Je vais à l'école\".",
                  "Bijvoorbeeld: Je vais à l'école à vélo. Of: Je vais à l'école en bus.", 2),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-een-tekstje-lezen"] = dict(
    vak="Frans", titel="Een tekstje lezen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="La lecture",
             opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Le chat de la boulangerie</h3>"
                  "<p>Tous les mercredis, Théo va à la boulangerie avec sa maman. La boulangerie "
                  "est dans la rue de l'école, à côté de la pharmacie.</p>"
                  "<p>Devant la porte, il y a toujours un chat gris. Il s'appelle Pompon. Théo "
                  "caresse le chat et le chat ronronne.</p>"
                  "<p>« Bonjour Théo ! » dit le boulanger. « Un pain et quatre croissants, "
                  "s'il vous plaît », dit la maman de Théo. Le boulanger rit : « Et un croissant "
                  "pour le chat ? » Théo dit non : les chats ne mangent pas de croissants.</p>"
                  "<p>Dehors, il fait froid. Théo porte le sac, parce que sa maman porte le pain. "
                  "Le sac n'est pas lourd. À la maison, ils mangent les croissants avec du "
                  "chocolat chaud.</p>"),
             ]),

        dict(kop="Les questions",
             opdracht="Zoek in de tekst de zin waar de vraag over gaat, en lees die traag.",
             oefeningen=[
                 ("kies", "Op welke dag speelt dit verhaaltje zich af?",
                  ["op maandag", "op woensdag", "op vrijdag", "op zondag"], 1),
                 ("kort", "Hoe heet de kat? Schrijf zijn naam.", "Pompon", WW),
                 ("kies", "Welke kleur heeft de kat?",
                  ["zwart", "wit", "grijs", "de kleur staat er niet bij"], 2),
                 ("kort", "Hoeveel croissants koopt de mama van Théo? Geef het getal in cijfers.",
                  "4", "70px"),
                 ("kies", "Welke winkel staat naast de bakkerij?",
                  ["la pharmacie", "la librairie", "la bibliothèque", "la piscine"], 0),
                 ("waar", "Théo geeft een croissant aan de kat.", False),
                 ("waar", "Het is koud buiten.", True),
                 ("kies", "Waarom draagt Théo de zak?",
                  ["omdat zijn mama het brood draagt", "omdat de zak zwaar is",
                   "omdat hij sterk is", "omdat zijn mama moe is"], 0),
                 ("kort", "Wat drinken ze thuis bij de croissants? (drie woordjes in het Frans)",
                  "du chocolat chaud", WW),
                 ("kies", "Welke titel past het best bij dit verhaaltje?",
                  ["La pharmacie", "Le chat de la boulangerie",
                   "L'école de Théo", "Les croissants de la maman"], 1),
             ]),

        dict(kop="Les mots",
             opdracht="Deze woorden staan in de tekst.",
             oefeningen=[
                 ("rij", [("le boulanger", "de bakker"), ("devant", "voor"),
                          ("dehors", "buiten"), ("le sac", "de zak")],
                  "Wat betekent het?", WW),
                 ("rij", [("naast", "à côté de"), ("zwaar", "lourd"),
                          ("aaien", "caresser")],
                  "En nu andersom: schrijf het in het Frans.", WW),
                 ("kies", "In de tekst staat \"ne … pas\". Wat doet dat met de zin?",
                  ["het maakt de zin ontkennend", "het maakt er een vraag van",
                   "het maakt de zin langer", "het verandert niets"], 0),
             ]),

        dict(kop="Zelf schrijven",
             opdracht="Nu jij.",
             oefeningen=[
                 ("open", "Schrijf drie zinnen in het Frans over een winkel waar jij graag komt.",
                  "Bijvoorbeeld: J'aime la boulangerie. Il y a du pain et des croissants. "
                  "Le boulanger est gentil.", 4),
             ]),
    ])

# ============================================================
BESCHRIJF_HOE = [
    "Zeg altijd eerst wáár iets staat: à gauche, à droite, au milieu, en haut, en bas.",
    "Begin een zin met \"Sur l'image, il y a …\".",
    "Bij een kleur: een vrouwelijk woord krijgt er een e bij (une tente verte).",
]

OEFENBUNDELS["oefenbundel-wat-zie-je-op-de-prent"] = dict(
    vak="Frans", titel="Wat zie je op de prent?",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_PRENT,
    reeksen=[
        dict(kop="De prent",
             opdracht="Kijk goed. Alle oefeningen hierna gaan over deze prent.",
             oefeningen=[
                 ("tekst", prent("wat-zie-je-op-de-prent")),
                 ("tekst", "<p style='margin:.6em 0 0'><b>Onthoud dit.</b> " +
                  " &nbsp;·&nbsp; ".join(BESCHRIJF_HOE) + "</p>"),
             ]),

        dict(kop="Wat staat er op?",
             opdracht="Schrijf het Franse woord, met un of une ervoor.",
             oefeningen=[
                 ("rij", [("de berg", "une montagne"), ("de brug", "un pont"),
                          ("de rivier", "une rivière"), ("de boom", "un arbre")],
                  "Zoek het op de prent en schrijf het in het Frans.", WW),
                 ("rij", [("un écureuil", "een eekhoorn"), ("une barrière", "een hek"),
                          ("un casque", "een helm"), ("le ciel", "de lucht")],
                  "Wat betekent het? Zoek het ook op de prent.", WW),
                 ("kort", "Hoe zeg je \"het konijn\" in het Frans? (twee woordjes)",
                  "le lapin", WW),
             ]),

        dict(kop="Waar staat het?",
             opdracht="Antwoord met à gauche, à droite, au milieu, en haut of en bas.",
             oefeningen=[
                 ("rij", [("de zon", "en haut à droite"), ("de koe", "à gauche"),
                          ("de brug", "à droite"), ("het konijn", "en bas à droite")],
                  "Waar staat het op de prent?", "180px"),
                 ("waar", "Les montagnes sont en haut sur l'image.", True),
                 ("kies", "Waar rijdt de jongen?",
                  ["en haut", "en bas", "au milieu", "à gauche"], 2),
             ]),

        dict(kop="Tellen en kleuren",
             opdracht="Tel op de prent zelf, niet uit je hoofd.",
             oefeningen=[
                 ("rij", [("... vache", "une"), ("... oiseaux dans le ciel", "trois"),
                          ("... lapin", "un")],
                  "Hoeveel? Schrijf het getal in het Frans.", W),
                 ("rij", [("le vélo", "bleu"), ("la veste du garçon", "rouge"),
                          ("le casque", "bleu")],
                  "Welke kleur? Schrijf het Franse woord.", W),
                 ("kies", "Welke kleuren heeft de koe?",
                  ["tout blanc", "noir et blanc", "brun et blanc", "tout brun"], 2),
             ]),

        dict(kop="Er is en er is niet",
             opdracht="Il y a, of il n'y a pas de?",
             oefeningen=[
                 ("rij", [("un pont", "il y a"), ("un chien", "il n'y a pas de"),
                          ("une rivière", "il y a"), ("un cheval", "il n'y a pas de")],
                  "Staat het op de prent? Schrijf il y a of il n'y a pas de.", "180px"),
                 ("kort", "Schrijf in het Frans: er is een koe op de prent.",
                  "Sur l'image, il y a une vache", "260px"),
                 ("waar", "Il y a un canard dans la rivière.", True),
             ]),

        dict(kop="Zelf beschrijven",
             opdracht="Nu jij. Kijk naar de prent en schrijf.",
             oefeningen=[
                 ("open", "Schrijf drie zinnen over deze prent in het Frans. "
                          "Gebruik in elke zin il y a en een plaats (à gauche, à droite, au milieu).",
                  "Bijvoorbeeld: À gauche, il y a un écureuil dans un arbre. "
                  "Au milieu, il y a un garçon sur un vélo bleu. "
                  "À droite, il y a une vache derrière une barrière.", 5),
                 ("open", "Schrijf één zin over iets dat er NIET op staat. Gebruik il n'y a pas de.",
                  "Bijvoorbeeld: Il n'y a pas de chien sur l'image.", 2),
             ]),
    ])

# ============================================================
OEFENBUNDELS["oefenbundel-wat-zie-je-aan-zee"] = dict(
    vak="Frans", titel="Wat zie je aan zee?",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_PRENT,
    reeksen=[
        dict(kop="De prent",
             opdracht="Kijk goed. Alle oefeningen hierna gaan over deze prent.",
             oefeningen=[
                 ("tekst", prent("wat-zie-je-aan-zee")),
                 ("tekst", "<p style='margin:.6em 0 0'><b>Onthoud dit.</b> " +
                  " &nbsp;·&nbsp; ".join(BESCHRIJF_HOE) + "</p>"),
             ]),

        dict(kop="Wat staat er op?",
             opdracht="Schrijf het Franse woord, met un of une ervoor.",
             oefeningen=[
                 ("rij", [("de tent", "une tente"), ("de vuurtoren", "un phare"),
                          ("de boot", "un bateau"), ("de emmer", "un seau")],
                  "Zoek het op de prent en schrijf het in het Frans.", WW),
                 ("rij", [("un coquillage", "een schelp"), ("le sable", "het zand"),
                          ("une cabane", "een hut"), ("un ponton", "een steiger")],
                  "Wat betekent het? Zoek het ook op de prent.", WW),
                 ("kort", "Hoe zeg je \"het strand\" in het Frans? (twee woordjes)",
                  "la plage", WW),
                 ("kort", "Hoe noem je een kasteel van zand in het Frans? (drie woordjes)",
                  "un château de sable", WW),
             ]),

        dict(kop="De mensen en de dieren",
             opdracht="Kijk wie wat doet.",
             oefeningen=[
                 ("rij", [("de jongen met de blauwe pet", "il pêche"),
                          ("de jongen in de rode trui", "il caresse un chien"),
                          ("het meisje met de hoed", "elle ramasse des coquillages")],
                  "Wat doet die persoon? Schrijf het in het Frans.", "230px"),
                 ("kies", "Wat draagt de jongen op de steiger op zijn hoofd?",
                  ["un chapeau", "une casquette", "un casque", "rien"], 1),
                 ("kort", "Hoeveel kinderen staan er op de prent? Schrijf het getal in het Frans.",
                  "trois", W),
                 ("kort", "Hoeveel eenden zwemmen er in het water? Schrijf het getal in het Frans.",
                  "trois", W),
                 ("waar", "Il y a un chat dans la cabane.", True),
             ]),

        dict(kop="Waar staat het, en welke kleur?",
             opdracht="Antwoord met à gauche, à droite, au milieu, en haut of en bas.",
             oefeningen=[
                 ("rij", [("le phare", "à droite"), ("la tente", "à gauche"),
                          ("le château de sable", "en bas à droite")],
                  "Waar staat het op de prent?", "180px"),
                 ("rij", [("la tente", "verte"), ("le seau", "rouge"),
                          ("le bateau à rames", "blanc")],
                  "Welke kleur? Let op de e bij een vrouwelijk woord.", W),
                 ("kies", "Hoe laat op de dag speelt deze prent zich af?",
                  ["'s morgens vroeg", "'s middags", "'s avonds", "'s nachts"], 2),
                 ("kort", "Schrijf in het Frans dat de zon ondergaat. (drie woordjes)",
                  "le soleil se couche", "230px"),
             ]),

        dict(kop="Er is en er is niet",
             opdracht="Il y a, of il n'y a pas de?",
             oefeningen=[
                 ("rij", [("des arbres", "il y a"), ("une voiture", "il n'y a pas de"),
                          ("un chien", "il y a"), ("un cheval", "il n'y a pas de")],
                  "Staat het op de prent? Schrijf il y a of il n'y a pas de.", "180px"),
                 ("kort", "Schrijf in het Frans: er is een vuurtoren op de prent.",
                  "Sur l'image, il y a un phare", "260px"),
             ]),

        dict(kop="Zelf beschrijven",
             opdracht="Nu jij. Kijk naar de prent en schrijf.",
             oefeningen=[
                 ("open", "Schrijf vier zinnen over deze prent in het Frans. "
                          "Vertel waar het is, wat je ziet en wat de kinderen doen.",
                  "Bijvoorbeeld: L'image est à la mer. Il y a trois enfants sur la plage. "
                  "À gauche, il y a une tente verte. Le garçon sur le ponton pêche.", 6),
             ]),
    ])

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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-woorden-voor-elke-dag"] = dict(
    reeksen=[
        dict(aanpak="Let op de drie die op elkaar lijken: cinq is 5, quinze is 15 en cinquante is 50. "
                    "Lees ze luidop na elkaar, dan hoor je het verschil beter dan je het ziet.",
             waarom=[
                 "Vanaf 17 plakt het Frans twee getallen aan elkaar met een streepje: dix-sept is "
                 "tien-zeven, dix-huit tien-acht, dix-neuf tien-negen.",
                 None,
                 None,
                 None,
                 "Quinze is 15 en cinq is 5, maar cinquante is 50 en quarante 40. De uitgang -ante "
                 "maakt er een tiental van.",
                 None,
             ]),
        dict(aanpak="Een kleur past zich aan het woord ervoor aan: bij een vrouwelijk woord komt er "
                    "meestal een e bij (une voiture verte).",
             waarom=[
                 None,
                 None,
                 None,
                 "Vert wordt verte bij een vrouwelijk woord, net zoals noir noire wordt. Bij rouge en "
                 "jaune verandert er niets, want die eindigen al op een e.",
             ]),
        dict(aanpak="Zes van de zeven dagen eindigen op -di. Zeg ze in volgorde op, dan vind je de "
                    "dag ervoor en erna bijna vanzelf.",
             waarom=[
                 None,
                 None,
                 None,
                 "Dimanche is de enige dag die niet op -di eindigt. In het Frans begint de week "
                 "trouwens met lundi, dus dimanche staat achteraan.",
                 None,
             ]),
        dict(aanpak="Maanden krijgen in het Frans géén hoofdletter, net zoals in het Nederlands. Dat is "
                    "het verschil met het Engels.",
             waarom=[
                 None,
                 None,
                 "In het Engels is het January, in het Frans janvier met een kleine letter. Hetzelfde "
                 "geldt voor de dagen.",
                 None,
                 "Été begint met een klinker, dus wordt le een l': l'été. Datzelfde gebeurt bij "
                 "l'hiver en l'automne; alleen le printemps houdt zijn le.",
             ]),
        dict(aanpak="Drie woordjes die je elke dag nodig hebt. Hier helpt alleen herhalen.",
             waarom=[None, None]),
        dict(aanpak="Kijk naar het moment van de dag en naar wie er voor je staat: bonjour overdag, "
                    "bonsoir 's avonds, en salut alleen bij mensen die je goed kent.",
             waarom=[
                 None,
                 "Bonne nuit zeg je enkel bij het slapengaan. Kom je 's avonds ergens aan, dan is het "
                 "bonsoir.",
                 None,
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-mezelf-voorstellen"] = dict(
    reeksen=[
        dict(aanpak="Het Frans zegt dat je jaren hébt, niet dat je jaren bént: j'ai dix ans. En bij "
                    "s'appeler verandert het woordje voor het werkwoord mee: je m'appelle, tu "
                    "t'appelles.",
             waarom=[
                 "Me wordt m' voor een klinker: je m'appelle. Dat gebeurt in het Frans telkens als twee "
                 "klinkers tegen elkaar botsen.",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Habiter is wonen, venir de is komen uit. Vraag je dus af of het over nu gaat "
                    "(waar je woont) of over je herkomst.",
             waarom=[
                 "Bij een stad hoort à: j'habite à Genk. Bij een land is het en of au: j'habite en "
                 "Belgique.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Mon, ma of mes hangt af van het woord dat erna komt: mon bij een mannelijk woord, "
                    "ma bij een vrouwelijk, mes bij een meervoud.",
             waarom=[
                 None,
                 None,
                 None,
                 "Père is mannelijk, dus mon père. Zou het ma zijn, dan moest het woord erna vrouwelijk "
                 "zijn, zoals ma mère.",
                 None,
             ]),
        dict(aanpak="Tu is vertrouwd, vous is beleefd. Bij twijfel neem je vous: te beleefd zijn is in "
                    "het Frans nooit een fout.",
             waarom=[
                 None,
                 "Tegen de mama van een vriend hoort bonjour madame en vous. Salut en ça va zijn voor "
                 "leeftijdsgenoten.",
                 None,
             ]),
        dict(aanpak="Deze zinnetjes zeg je elke dag. Leer ze als één geheel, niet woord voor woord.",
             waarom=[
                 None,
                 None,
                 "Een jongen schrijft enchanté, een meisje enchantée met een extra e. Je hoort geen "
                 "verschil, je ziet het alleen.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-etre-en-avoir"] = dict(
    reeksen=[
        dict(aanpak="Deze twee rijtjes zijn de basis van alles wat daarna komt. Schrijf ze een paar "
                    "keer uit het hoofd op, en kijk pas daarna na.",
             waarom=[None, None, None]),
        dict(aanpak="Vraag je af of het om een toestand gaat (être: moe, lief, Belg) of om iets dat je "
                    "hebt (avoir: honger, dorst, koud, gelijk, een leeftijd). Het Nederlands zegt hier "
                    "soms zijn waar het Frans avoir gebruikt.",
             waarom=[
                 "Ik heb het warm is j'ai chaud, met avoir. Het Frans ziet warmte als iets dat je hebt, "
                 "niet als iets dat je bent.",
                 None,
                 None,
                 "Je suis froid betekent dat jij als persoon koud of kil bent. Wil je zeggen dat je het "
                 "koud hebt, dan is het j'ai froid.",
                 None,
             ]),
        dict(aanpak="Sont en ont schelen één letter maar betekenen iets heel anders: sont is zijn, ont "
                    "is hebben. Lees deze reeks traag.",
             waarom=[
                 "Ils sont is zij zijn, ils ont is zij hebben. Eén letter verschil, en de zin betekent "
                 "iets anders.",
                 None,
                 None,
                 None,
                 "Tu es schrijf je zonder t, il est met een t. Je hoort het verschil niet, dus hier "
                 "helpt alleen kijken.",
             ]),
        dict(aanpak="Zoek eerst wie er iets doet, kies dan de vorm, en schrijf pas daarna de hele zin "
                    "op.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijd"] = dict(
    reeksen=[
        dict(aanpak="Haal de -er van het hele werkwoord en plak er de uitgang van de persoon aan: -e, "
                    "-es, -e, -ons, -ez, -ent. Die uitgangen zijn voor élk werkwoord op -er dezelfde.",
             waarom=[
                 None,
                 None,
                 "Je krijgt -e, tu krijgt -es, nous krijgt -ons en vous krijgt -ez. Je parlons en je "
                 "parlez horen dus bij een andere persoon.",
                 "Je hoort -e, -es en -ent niet: je parle, tu parles en ils parlent klinken hetzelfde. "
                 "Daarom moet je bij het schrijven kijken wie er vooraan staat.",
             ]),
        dict(aanpak="Aller is onregelmatig: je vais, tu vas, il va, nous allons, vous allez, ils vont. "
                    "Die vormen moet je gewoon kennen.",
             waarom=[
                 None,
                 None,
                 "Aller plus een werkwoord is de naaste toekomst: je vais manger betekent ik ga eten, "
                 "dus straks. Ik eet nu is je mange.",
                 None,
             ]),
        dict(aanpak="Faire is ook onregelmatig, en de twee vormen die het vaakst fout gaan zijn vous "
                    "faites en ils font.",
             waarom=[
                 None,
                 None,
                 "Vous faites en ils font zijn de twee die er niet uitzien zoals de rest. Vous faisez "
                 "bestaat niet.",
                 None,
             ]),
        dict(aanpak="Over het weer zegt het Frans il fait: il fait froid, il fait beau. Letterlijk "
                    "vertalen met être werkt hier niet.",
             waarom=[
                 None,
                 "Il est froid zou betekenen dat een ding koud is. Over het weer zeg je il fait froid.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-zinnen-bouwen"] = dict(
    reeksen=[
        dict(aanpak="Le hoort bij een mannelijk woord, la bij een vrouwelijk, les bij een meervoud, en "
                    "voor een klinker worden le en la allebei l'.",
             waarom=[
                 "École en ami beginnen met een klinker, dus l'école en l'ami. Je ziet dan niet meer of "
                 "het woord mannelijk of vrouwelijk is; dat moet je erbij leren.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Een ontkenning in het Frans heeft twee delen: ne vóór het werkwoord en pas erna. "
                    "Beide moeten er staan.",
             waarom=[
                 None,
                 "Na een ontkenning wordt un, une of des meestal de: j'ai un chien wordt je n'ai pas de "
                 "chien.",
                 None,
                 None,
             ]),
        dict(aanpak="Met est-ce que maak je van elke zin een vraag, zonder iets anders te veranderen. "
                    "En let op de spatie vóór het vraagteken: die hoort er in het Frans bij.",
             waarom=[None, None, None, None]),
        dict(aanpak="In het Frans komt het bijvoeglijk naamwoord meestal áchter het woord (un chien "
                    "noir). Een handvol korte woorden zoals petit en grand gaat ervoor.",
             waarom=[
                 None,
                 "Voiture is vrouwelijk, dus une, en de kleur komt erachter: une voiture rouge. Rouge "
                 "eindigt al op een e en verandert verder niet.",
                 "Alles gaat mee in het meervoud: les petites filles krijgt een s bij het lidwoord, bij "
                 "het bijvoeglijk naamwoord én bij het zelfstandig naamwoord.",
                 None,
             ]),
        dict(aanpak="Et verbindt, ou laat kiezen, en mais zet twee dingen tegenover elkaar.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-op-school-en-onderweg"] = dict(
    reeksen=[
        dict(aanpak="Leer elk woord meteen met zijn un of une erbij. Het lidwoord onthouden is later "
                    "veel moeilijker dan het nu mee te leren.",
             waarom=[
                 None,
                 "Un crayon is een potlood, un stylo een balpen. Alleen een potlood kan je uitgommen.",
                 None,
             ]),
        dict(aanpak="Dit zijn de zinnen die in de klas vallen. Zeg ze luidop, dan herken je ze ook als "
                    "de leerkracht ze gebruikt.",
             waarom=[None, None, None, None]),
        dict(aanpak="Let goed op à droite en tout droit: die twee lijken op elkaar maar sturen je een "
                    "andere kant uit.",
             waarom=[
                 "À droite is naar rechts, tout droit is rechtdoor. Het verschil zit in het kleine "
                 "woordje ervoor.",
                 None,
                 None,
                 "La gare is het station, un garage is de garage. Ze lijken op elkaar, maar het is niet "
                 "dezelfde plaats.",
             ]),
        dict(aanpak="Denk aan wat je in de winkel komt doen: kopen of lenen? Dat is hier het hele "
                    "verschil.",
             waarom=[
                 "Une librairie is een boekenwinkel, une bibliothèque een bibliotheek. Het Franse woord "
                 "lijkt op library in het Engels, en dat is net de valstrik.",
                 None,
                 None,
             ]),
        dict(aanpak="Op iets waar je op zit, gebruikt het Frans à (à vélo, à pied). In iets waar je in "
                    "zit, is het en (en bus, en voiture).",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-een-tekstje-lezen"] = dict(
    reeksen=[
        dict(aanpak="Lees de tekst eerst helemaal, zonder op elk woord te blijven hangen. Je moet niet "
                    "elk woord kennen om te begrijpen waar het over gaat.",
             waarom=[]),
        dict(aanpak="Zoek bij elke vraag de zin in de tekst waar het antwoord in staat, en lees die "
                    "traag opnieuw. Staat iets er niet, dan is dat ook een antwoord.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 None,
                 "Dat staat nergens in de tekst. Wat er niet staat, mag je er niet bij denken, hoe "
                 "logisch het ook lijkt.",
                 None,
                 None,
                 None,
                 "De titel moet over het hele verhaaltje gaan, niet over één zin eruit. De apotheek en "
                 "de school komen wel voor, maar dragen het verhaal niet.",
             ]),
        dict(aanpak="Deze woorden staan in de tekst. Zoek ze daar terug: in een zin onthoud je een "
                    "woord veel beter dan los in een lijst.",
             waarom=[None, None, None]),
        dict(aanpak="Schrijf korte zinnen met woorden die je zeker kent. Drie eenvoudige zinnen die "
                    "kloppen zijn beter dan één lange zin vol twijfel.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-wat-zie-je-op-de-prent"] = dict(
    reeksen=[
        dict(aanpak="Kijk eerst rustig naar de hele prent voor je begint. Overloop ze daarna in stukken: "
                    "links, in het midden, rechts, boven en onder.",
             waarom=[]),
        dict(aanpak="Leer elk woord met un of une erbij, en zoek het telkens ook echt op de prent. Zo "
                    "hang je het woord aan een beeld in plaats van aan een vertaling.",
             waarom=[None, None, None]),
        dict(aanpak="Zeg altijd eerst wáár iets staat en dan pas wat het is: à gauche, il y a un arbre. "
                    "Zo bouw je in het Frans een beschrijving op.",
             waarom=[None, None, None]),
        dict(aanpak="Tel op de prent zelf, niet uit je hoofd. En let bij une vache op de e: un wordt "
                    "une bij een vrouwelijk woord, ook als het om het getal één gaat.",
             waarom=[
                 "Une vache en un lapin: het getal één past zich aan het woord aan, net als het "
                 "lidwoord. Bij trois oiseaux verandert er niets meer.",
                 None,
                 None,
             ]),
        dict(aanpak="Staat het erop, dan il y a. Staat het er niet, dan il n'y a pas de, met de in "
                    "plaats van un of une.",
             waarom=[
                 "Na een ontkenning wordt un of une altijd de: il y a un chien wordt il n'y a pas de "
                 "chien.",
                 None,
                 None,
             ]),
        dict(aanpak="Begin elke zin met een plaats, dan il y a, en dan pas het ding. Dat is het patroon "
                    "van de hele bundel.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-wat-zie-je-aan-zee"] = dict(
    reeksen=[
        dict(aanpak="Kijk eerst rustig naar de hele prent voor je begint. Overloop ze daarna in stukken: "
                    "links, in het midden, rechts, boven en onder.",
             waarom=[]),
        dict(aanpak="Leer elk woord met un of une erbij, en zoek het telkens ook echt op de prent. Zo "
                    "hang je het woord aan een beeld in plaats van aan een vertaling.",
             waarom=[None, None, None, None]),
        dict(aanpak="Kijk wie wat doet, en schrijf het als een hele zin: il pêche, elle ramasse. Het "
                    "werkwoord past zich aan die ene persoon aan.",
             waarom=[
                 None,
                 "Une casquette is een pet met een klep, un chapeau een hoed met een rand, un casque "
                 "een helm. Die drie worden vaak verwisseld.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Zeg eerst wáár iets staat en dan pas wat het is. En let bij de kleur op de e: bij "
                    "een vrouwelijk woord krijgt ze er meestal een bij.",
             waarom=[
                 None,
                 "La tente is vrouwelijk, dus verte met een e. Le seau is mannelijk, en rouge eindigt "
                 "al op een e en verandert niet.",
                 None,
                 None,
             ]),
        dict(aanpak="Staat het erop, dan il y a. Staat het er niet, dan il n'y a pas de, met de in "
                    "plaats van un, une of des.",
             waarom=[
                 "Na een ontkenning wordt un, une of des altijd de: il y a une voiture wordt il n'y a "
                 "pas de voiture.",
                 None,
             ]),
        dict(aanpak="Begin met waar het is, zeg dan wat je ziet, en eindig met wat de mensen doen. Vier "
                    "korte zinnen die kloppen, zijn beter dan één lange.",
             waarom=[None]),
    ],
)

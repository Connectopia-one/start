# -*- coding: utf-8 -*-
"""De leerbundels voor Frans, categorie Start (5de en 6de leerjaar).

Negen bundels, één per hoofdstuk: de zeven van `inhoud/start/frans.json` en de
twee beschrijfhoofdstukken van `inhoud/start/frans-prenten.json`.

Frans hoort niet bij de minimumdoelen van het lager onderwijs. Wij zetten het
er zelf bij, net als Engels: kinderen komen er vroeg mee in aanraking, en een
goede basis kan geen kwaad. Dat staat ook in de eerste bundel, zodat niemand
denkt dat een kind hier op school al op beoordeeld wordt.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../start/frans.json` en
`python3 dekking.py ../../start/frans-prenten.json` doen daar het voorwerk
voor; daarna gaat elke vraag nog één voor één naast de tekst.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Frans"
tabel = bundel.tabel

NIET_VERPLICHT = (
    "<strong>Frans hoort niet bij de minimumdoelen van het lager onderwijs.</strong> "
    "Wij bieden het toch aan, omdat kinderen in België vroeg met Frans in aanraking komen "
    "en een goede basis geen kwaad kan. Oefen dus gerust mee, maar weet dat je hier op "
    "school nog niet op beoordeeld wordt."
)

BUNDELS = {}

# ===========================================================================
BUNDELS["woorden-voor-elke-dag"] = dict(
    vak=VAK, titel="Woorden voor elke dag",
    onder="De woorden die je het vaakst nodig hebt: getallen, kleuren, dagen, maanden en groeten.",
    secties=[
        dict(kop="Waarom Frans?", blokken=[
            ("kader", NIET_VERPLICHT),
        ]),
        dict(kop="Tellen", blokken=[
            ("fig", tabel(["1 tot 10", "11 tot 20", "Tientallen"], [
                ["un, deux, trois", "onze, douze, treize", "dix, vingt, trente"],
                ["quatre, cinq, six", "quatorze, quinze, seize", "quarante, cinquante"],
                ["sept, huit, neuf, dix", "dix-sept, dix-huit, dix-neuf, vingt", "soixante, cent"],
            ]), "Acht is huit: de h schrijf je wel, maar je hoort ze niet."),
            ("p", "Tot en met <strong>seize</strong> (16) heeft elk getal een eigen woord. "
                  "Vanaf <strong>dix-sept</strong> plak je ze aan elkaar: dix-sept is tien-zeven, "
                  "dix-huit is tien-acht."),
            ("p", "Na <strong>vingt</strong> (20) tel je verder met vingt et un, vingt-deux, "
                  "vingt-trois. Let op de valstrikken: <strong>quinze</strong> is vijftien, "
                  "<strong>cinq</strong> is vijf en <strong>cinquante</strong> is vijftig. "
                  "<strong>Douze</strong> is twaalf, <strong>deux</strong> is twee."),
        ]),
        dict(kop="Kleuren", blokken=[
            ("fig", svg.kleurstalen([
                ("rouge", "rood", "#c0392b"), ("bleu", "blauw", "#2f6fb0"),
                ("jaune", "geel", "#e8b820"), ("vert", "groen", "#2f7d4f"),
                ("noir", "zwart", "#23291f"), ("blanc", "wit", "#f4f1e6"),
                ("gris", "grijs", "#8d8d8d"), ("rose", "roze", "#e08aa8"),
            ]), "Bruin is brun of marron; allebei mag."),
            ("p", "Bij een vrouwelijk woord krijgt een kleur er meestal een <strong>e</strong> bij: "
                  "un chien <strong>noir</strong>, une voiture <strong>noire</strong>. Je hoort het "
                  "verschil bij noir niet, bij vert wel: vert klinkt als 'ver', verte als 'vert'."),
        ]),
        dict(kop="De dagen van de week", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["lundi", "maandag"], ["mardi", "dinsdag"], ["mercredi", "woensdag"],
                ["jeudi", "donderdag"], ["vendredi", "vrijdag"],
                ["samedi", "zaterdag"], ["dimanche", "zondag"],
            ], "70%"), "Bijna elke dag eindigt op -di. Alleen dimanche begint ermee."),
            ("p", "De volgorde ken je best uit je hoofd, want daar wordt naar gevraagd: na "
                  "<strong>jeudi</strong> komt <strong>vendredi</strong>, na vendredi komt samedi."),
        ]),
        dict(kop="De maanden en de seizoenen", blokken=[
            ("p", "janvier, février, mars, avril, mai, juin, juillet, août, septembre, "
                  "octobre, novembre, décembre."),
            ("weetje", "In het Frans schrijf je een maand met een <strong>kleine letter</strong>, "
                       "net als in het Nederlands. In het Engels krijgt hij wél een hoofdletter: "
                       "March, April, May. Dat verschil is een makkelijk punt om te verdienen."),
            ("p", "<strong>Juin</strong> is juni en <strong>juillet</strong> is juli. Die twee "
                  "lijken op elkaar, dus lees goed."),
            ("fig", tabel(["Seizoen", "Frans", "Maanden"], [
                ["de winter", "l'hiver", "décembre, janvier, février"],
                ["de lente", "le printemps", "mars, avril, mai"],
                ["de zomer", "l'été", "juin, juillet, août"],
                ["de herfst", "l'automne", "septembre, octobre, novembre"],
            ]), "Janvier valt midden in de winter, l'hiver."),
        ]),
        dict(kop="Vandaag, gisteren, morgen", blokken=[
            ("p", "<strong>aujourd'hui</strong> is vandaag, <strong>hier</strong> is gisteren en "
                  "<strong>demain</strong> is morgen. Aujourd'hui schrijf je met een apostrof in "
                  "het midden."),
        ]),
        dict(kop="Groeten en beleefd zijn", blokken=[
            ("fig", svg.spreekballonnen([
                ("overdag", "Bonjour !", True),
                ("'s avonds", "Bonsoir !", False),
                ("voor het slapen", "Bonne nuit !", True),
                ("bij het weggaan", "Au revoir !", False),
            ]), "Bonjour zeg je overdag, bonsoir als het avond wordt."),
            ("p", "<strong>Salut</strong> kan zowel hallo als dag betekenen: je gebruikt het bij "
                  "het komen én bij het gaan, maar alleen tegen mensen die je goed kent. "
                  "<strong>Au revoir</strong> is tot ziens, dus alleen bij het weggaan."),
            ("fig", tabel(["Je zegt", "Betekenis"], [
                ["merci", "dank je wel"],
                ["merci beaucoup", "hartelijk dank"],
                ["de rien", "graag gedaan (antwoord op merci)"],
                ["je vous en prie", "graag gedaan, wat beleefder"],
                ["s'il vous plaît", "alstublieft"],
                ["s'il te plaît", "alsjeblieft, tegen een vriend"],
            ], "80%"), "Zegt iemand merci, dan antwoord je met de rien."),
        ]),
    ],
    onthoud=[
        "Tot en met seize heeft elk getal een eigen woord; vanaf dix-sept plak je ze aan elkaar.",
        "quinze is 15, cinq is 5, cinquante is 50. Douze is 12, deux is 2.",
        "Bijna elke dag eindigt op -di; alleen dimanche begint ermee.",
        "Een maand schrijf je met een kleine letter, net als in het Nederlands.",
        "juin is juni, juillet is juli.",
        "Bonjour overdag, bonsoir 's avonds, au revoir bij het weggaan.",
        "Zegt iemand merci, dan antwoord je met de rien.",
    ],
)

# ===========================================================================
BUNDELS["mezelf-voorstellen"] = dict(
    vak=VAK, titel="Mezelf voorstellen",
    onder="Je naam, je leeftijd, waar je woont en wie er bij je thuis wonen.",
    secties=[
        dict(kop="Hoe heet je?", blokken=[
            ("fig", svg.spreekballonnen([
                ("vraag", "Comment tu t'appelles ?", True),
                ("antwoord", "Je m'appelle Lucas.", False),
                ("vraag", "Quel âge as-tu ?", True),
                ("antwoord", "J'ai douze ans.", False),
            ]), "De twee vragen die altijd komen, met hun antwoord."),
            ("p", "<strong>Comment tu t'appelles ?</strong> betekent hoe heet je. Je antwoordt met "
                  "<strong>Je m'appelle …</strong> Het woordje <em>me</em> wordt <strong>m'</strong> "
                  "voor een klinker, met een apostrof erachter: je m'appelle, niet je me appelle."),
        ]),
        dict(kop="Hoe oud ben je?", blokken=[
            ("p", "<strong>Quel âge as-tu ?</strong> is hoe oud ben je. En hier zit de valstrik "
                  "waar bijna iedereen op struikelt: in het Nederlands <em>ben</em> je elf jaar, "
                  "in het Frans <strong>heb</strong> je jaren."),
            ("kader", "Je zegt <strong>J'ai onze ans</strong>: ik heb elf jaar. Dus met "
                      "<strong>avoir</strong> (hebben), niet met être (zijn). "
                      "<em>Je suis onze ans</em> is fout, en het woordje <strong>ans</strong> mag "
                      "je niet weglaten: J'ai onze klopt ook niet."),
            ("p", "Bij een <strong>nationaliteit</strong> gebruik je wél être: "
                  "<strong>Je suis belge</strong> (ik ben Belg), <strong>Je suis française</strong> "
                  "(ik ben Frans, over een meisje). Suis is de vorm van être die bij je hoort."),
        ]),
        dict(kop="Waar woon je?", blokken=[
            ("p", "<strong>Habiter</strong> is wonen. Bij je wordt dat <strong>j'habite</strong>: "
                  "je + habite worden aan elkaar geplakt, want habite begint met een h die je niet "
                  "hoort. <em>J'habite à Hasselt</em> betekent ik woon in Hasselt, "
                  "<em>J'habite à Gand</em> ik woon in Gent."),
            ("p", "<strong>Venir de</strong> is komen uit: <em>Je viens de Belgique</em> betekent "
                  "ik kom uit België. Dat is iets anders dan er wonen of ernaartoe gaan."),
        ]),
        dict(kop="Je gezin", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le père", "de vader"], ["la mère", "de moeder"],
                ["les parents", "de ouders"], ["le frère", "de broer"],
                ["la sœur", "de zus"], ["les grands-parents", "de grootouders"],
            ], "70%"), "Frère schrijf je met een accent grave op de eerste e; sœur met de letter œ."),
            ("p", "<strong>Mon</strong> zet je voor een mannelijk woord en <strong>ma</strong> voor "
                  "een vrouwelijk woord: <em>mon frère</em>, <em>ma sœur</em>, <em>ma mère</em>. "
                  "Bij meer dan één wordt het <strong>mes</strong>: mes frères, mes sœurs, "
                  "<strong>mes parents</strong>."),
            ("p", "<strong>Tu as des frères et sœurs ?</strong> betekent heb jij broers en zussen. "
                  "<em>Tu as …?</em> is heb jij …?"),
            ("weetje", "Typ je een antwoord in zonder de accenten, dan telt het hier toch juist. "
                       "Het platform zet de juiste schrijfwijze er wel bij, zodat je ze leert."),
        ]),
        dict(kop="Hoe gaat het?", blokken=[
            ("p", "<strong>Ça va ?</strong> is hoe gaat het. Je antwoordt met "
                  "<strong>ça va bien, merci</strong> of met ça va mal als het niet goed gaat."),
            ("p", "<strong>Enchanté</strong> zeg je als je iemand voor het eerst ontmoet: het "
                  "betekent aangenaam. Een meisje schrijft <strong>enchantée</strong>, met een e erbij."),
        ]),
        dict(kop="Tu of vous?", blokken=[
            ("fig", svg.persoonsvormen([
                ("je familie|je vrienden|kinderen", "tu", svg.FOREST),
                ("je leerkracht|een onbekende|een volwassene", "vous", svg.AMBER),
            ]), "Tu is vertrouwd, vous is beleefd. Niet omgekeerd."),
            ("p", "Tegen je <strong>leerkracht</strong> en tegen een volwassene die je niet goed "
                  "kent, zeg je dus <strong>vous</strong>. Tegen je beste vriend zeg je "
                  "<strong>tu</strong>."),
            ("kader", "Stel je je voor aan de mama van een vriend, dan zeg je "
                      "<strong>Bonjour madame, je m'appelle …</strong> Salut en tu zijn daar te "
                      "familiair voor."),
        ]),
    ],
    onthoud=[
        "Je m'appelle … voor je naam, J'ai … ans voor je leeftijd.",
        "In het Frans heb je jaren: J'ai onze ans, nooit je suis onze ans.",
        "Bij een nationaliteit gebruik je wél être: je suis belge.",
        "J'habite à … is ik woon in …, je viens de … is ik kom uit …",
        "mon bij een mannelijk woord, ma bij een vrouwelijk, mes bij meer dan één.",
        "tu tegen familie en vrienden, vous tegen je leerkracht en onbekenden.",
    ],
)

# ===========================================================================
BUNDELS["etre-en-avoir"] = dict(
    vak=VAK, titel="Être en avoir",
    onder="Zijn en hebben: de twee werkwoorden die je het vaakst nodig hebt, en wanneer je welk gebruikt.",
    secties=[
        dict(kop="De twee belangrijkste werkwoorden", blokken=[
            ("p", "<strong>Être</strong> betekent zijn. <strong>Avoir</strong> betekent hebben. "
                  "Ze zijn allebei onregelmatig, dus je leert ze uit het hoofd. Daarna kan je er "
                  "heel veel mee. Ter vergelijking: <em>aller</em> is gaan en <em>faire</em> is "
                  "doen of maken."),
        ]),
        dict(kop="Être: zijn", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["je suis", "ik ben"], ["tu es", "jij bent"],
                ["il est / elle est", "hij is / zij is"],
                ["nous sommes", "wij zijn"], ["vous êtes", "jullie zijn of u bent"],
                ["ils sont / elles sont", "zij zijn"],
            ], "70%"), "Vous êtes krijgt een dakje op de e."),
            ("p", "<strong>Tu es</strong> mon ami betekent jij bent mijn vriend. Pas op: "
                  "<em>est</em> met een t hoort bij il of elle, <em>es</em> zonder t bij tu. "
                  "Je hoort dat verschil niet, je ziet het alleen."),
            ("p", "<strong>Ils sont</strong> en <strong>elles sont</strong> hebben dezelfde vorm. "
                  "Alleen het woordje ervoor verschilt: ils voor een groep met minstens één jongen, "
                  "elles voor een groep meisjes. <em>Elles sont contentes</em> betekent zij zijn blij, "
                  "<em>Ils sont fatigués</em> zij zijn moe."),
        ]),
        dict(kop="Avoir: hebben", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["j'ai", "ik heb"], ["tu as", "jij hebt"],
                ["il a / elle a", "hij heeft / zij heeft"],
                ["nous avons", "wij hebben"], ["vous avez", "jullie hebben of u hebt"],
                ["ils ont / elles ont", "zij hebben"],
            ], "70%"), "Il a schrijf je zonder s en zonder accent."),
            ("p", "<strong>J'ai un chien</strong>: je + ai worden j'ai, want twee klinkers na "
                  "elkaar spreken lastig. <em>Nous avons trois chiens</em> betekent wij hebben "
                  "drie honden, <em>Ils ont deux chats</em> zij hebben twee katten."),
            ("kader", "<strong>Ils sont</strong> is zij <em>zijn</em>, <strong>ils ont</strong> is "
                      "zij <em>hebben</em>. Eén letter verschil, en een heel andere betekenis. "
                      "Hetzelfde geldt voor <strong>il a</strong> (hij heeft) en "
                      "<strong>il est</strong> (hij is): il a onze ans klopt, il est onze ans niet."),
        ]),
        dict(kop="Wat je in het Frans hebt", blokken=[
            ("p", "Een hele reeks dingen waar wij <em>zijn</em> of <em>het hebben</em> zeggen, "
                  "gaan in het Frans met <strong>avoir</strong>:"),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["j'ai faim", "ik heb honger"],
                ["j'ai soif", "ik heb dorst"],
                ["j'ai froid", "ik heb het koud"],
                ["j'ai chaud", "ik heb het warm"],
                ["tu as raison", "je hebt gelijk"],
                ["j'ai douze ans", "ik ben twaalf jaar"],
            ], "70%"), "Allemaal met avoir, nooit met être."),
            ("weetje", "<em>Je suis froid</em> zou betekenen dat jij zélf een koude persoon bent. "
                       "Wil je zeggen dat je het koud hebt, dan is het <strong>j'ai froid</strong>."),
        ]),
        dict(kop="Wanneer dan wél être?", blokken=[
            ("p", "Voor een <strong>toestand</strong> of een eigenschap: moe, blij, lief, te laat. "
                  "<em>Elle est gentille</em> (zij is lief), <em>Vous êtes en retard</em> (jullie "
                  "zijn te laat), <em>Ils sont fatigués</em> (zij zijn moe)."),
            ("fig", svg.persoonsvormen([
                ("moe|blij|lief|Belg|te laat", "être", svg.FOREST),
                ("honger|dorst|koud|gelijk|… jaar", "avoir", svg.AMBER),
            ]), "Twijfel je? Vraag je af of het een toestand is (être) of iets dat je hebt (avoir)."),
        ]),
    ],
    onthoud=[
        "Être is zijn, avoir is hebben. Allebei onregelmatig, dus uit het hoofd.",
        "es zonder t hoort bij tu, est met t bij il en elle.",
        "ils sont is zij zijn, ils ont is zij hebben. Eén letter verschil.",
        "Honger, dorst, koud, warm, gelijk en je leeftijd gaan met avoir.",
        "Een toestand of een eigenschap gaat met être: moe, blij, lief, te laat.",
    ],
)

# ===========================================================================
BUNDELS["de-tegenwoordige-tijd"] = dict(
    vak=VAK, titel="De tegenwoordige tijd",
    onder="De werkwoorden op -er, en de twee onregelmatige die je overal tegenkomt: aller en faire.",
    secties=[
        dict(kop="De werkwoorden op -er", blokken=[
            ("p", "De meeste Franse werkwoorden eindigen in het woordenboek op <strong>-er</strong>. "
                  "Die vorm heet de <strong>infinitief</strong>: parler (spreken), jouer (spelen), "
                  "regarder (kijken), manger (eten), chanter (zingen), écouter (luisteren). "
                  "Herken je die -er, dan weet je meteen hoe je het werkwoord vervoegt."),
            ("p", "Je haalt de <strong>-er</strong> eraf en plakt er de uitgang van de persoon aan:"),
            ("fig", tabel(["Persoon", "Uitgang", "parler", "jouer"], [
                ["je", "-e", "je parle", "je joue"],
                ["tu", "-es", "tu parles", "tu joues"],
                ["il / elle", "-e", "il parle", "elle joue"],
                ["nous", "-ons", "nous parlons", "nous jouons"],
                ["vous", "-ez", "vous parlez", "vous jouez"],
                ["ils / elles", "-ent", "ils parlent", "elles jouent"],
            ]), "Bij nous is het altijd -ons, bij vous altijd -ez."),
            ("kader", "<strong>De uitgang -ent hoor je niet.</strong> <em>Ils parlent</em> klinkt "
                      "precies hetzelfde als <em>il parle</em>. Je ziet het verschil alleen op "
                      "papier, dus lees goed wie er vooraan staat."),
            ("p", "De s van <strong>tu</strong> is de tweede valstrik: <em>tu parles</em>, "
                  "<em>tu joues</em>, met s. Bij <strong>je</strong> is het zonder: "
                  "<em>je parle</em>. <em>Je parles français</em> is dus fout. En bij één persoon "
                  "hoort -e: <em>Elle mange une pomme</em>, niet elle mangent of elle manges."),
            ("p", "<em>Tu joues au football</em> betekent jij speelt voetbal, "
                  "<em>Vous regardez la télé</em> jullie kijken tv, "
                  "<em>Elle écoute de la musique</em> zij luistert naar muziek, "
                  "<em>Nous chantons bien</em> wij zingen goed en "
                  "<em>Ils jouent dehors</em> zij spelen buiten."),
        ]),
        dict(kop="Aller: gaan", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["je vais", "ik ga"], ["tu vas", "jij gaat"], ["il va / elle va", "hij gaat"],
                ["nous allons", "wij gaan"], ["vous allez", "jullie gaan"],
                ["ils vont / elles vont", "zij gaan"],
            ], "70%"), "Aller is onregelmatig, maar bij nous is het toch gewoon allons."),
            ("p", "<em>Je vais au cinéma</em> is ik ga naar de bioscoop, "
                  "<em>Nous allons à l'école</em> wij gaan naar school en "
                  "<em>Ils vont à la maison</em> zij gaan naar huis."),
            ("p", "Zet je <strong>aller</strong> voor een werkwoord uit het woordenboek, dan krijg "
                  "je de <strong>nabije toekomst</strong>: <em>Je vais manger</em> betekent ik ga "
                  "eten. Dus niet ik eet, en ook niet ik heb gegeten."),
        ]),
        dict(kop="Faire: doen of maken", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["je fais", "ik doe"], ["tu fais", "jij doet"], ["il fait / elle fait", "hij doet"],
                ["nous faisons", "wij doen"], ["vous faites", "jullie doen"],
                ["ils font / elles font", "zij doen"],
            ], "70%"), "Vous faites en ils font zijn de twee die je moet onthouden."),
            ("p", "<strong>Qu'est-ce que tu fais ?</strong> betekent wat doe je. "
                  "<em>Nous faisons nos devoirs</em> is wij maken ons huiswerk: "
                  "<strong>faire les devoirs</strong> is huiswerk maken."),
            ("kader", "<strong>Ils font</strong> hoort bij faire (zij doen), <strong>ils vont</strong> "
                      "bij aller (zij gaan). Die twee lijken op elkaar, dus lees goed."),
        ]),
        dict(kop="Het weer gaat met faire", blokken=[
            ("p", "Over het weer zegt het Frans <strong>il fait</strong>: <em>il fait froid</em> "
                  "(het is koud), <em>il fait chaud</em> (het is warm), <em>il fait beau</em> "
                  "(het is mooi weer). Letterlijk staat er dat het koud <em>maakt</em>."),
        ]),
    ],
    onthoud=[
        "Haal de -er weg en plak de uitgang eraan: -e, -es, -e, -ons, -ez, -ent.",
        "De uitgang -ent hoor je niet: ils parlent klinkt als il parle.",
        "tu krijgt een s (tu parles), je niet (je parle).",
        "aller: je vais, tu vas, il va, nous allons, vous allez, ils vont.",
        "aller plus een werkwoord is de nabije toekomst: je vais manger is ik ga eten.",
        "faire: vous faites en ils font zijn de twee die je moet onthouden.",
        "Over het weer zegt het Frans il fait: il fait froid, il fait beau.",
    ],
)

# ===========================================================================
BUNDELS["zinnen-bouwen"] = dict(
    vak=VAK, titel="Zinnen bouwen",
    onder="Le en la, meervoud, ontkennen, vragen stellen en waar het bijvoeglijk naamwoord staat.",
    secties=[
        dict(kop="Elk woord heeft een geslacht", blokken=[
            ("p", "In het Frans is elk woord mannelijk of vrouwelijk, ook een tafel of een boek. "
                  "Dat bepaalt welk lidwoord je gebruikt."),
            ("fig", tabel(["", "de / het", "een"], [
                ["mannelijk", "le livre", "un livre"],
                ["vrouwelijk", "la fille, la table", "une table"],
                ["voor een klinker", "l'ami, l'école", "un ami, une école"],
                ["meervoud", "les livres, les filles", "des livres"],
            ]), "Le garçon is de jongen, la fille het meisje."),
            ("p", "Voor een woord dat met een klinker begint, worden <strong>le</strong> en "
                  "<strong>la</strong> allebei <strong>l'</strong>: l'ami, l'école. Twee klinkers "
                  "na elkaar spreken lastig, dus valt er een weg."),
            ("p", "In het <strong>meervoud</strong> worden le en la allebei <strong>les</strong>, "
                  "en het woord krijgt een <strong>s</strong>: le livre wordt <strong>les "
                  "livres</strong>. <strong>Un</strong> en <strong>une</strong> betekenen allebei "
                  "een: un livre (mannelijk), une table (vrouwelijk)."),
        ]),
        dict(kop="Een zin ontkennen", blokken=[
            ("fig", svg.woordvolgorde([
                ("", "Je", svg.DIM), ("ontkenning", "ne", svg.AMBER),
                ("werkwoord", "parle", svg.FOREST), ("ontkenning", "pas", svg.AMBER),
                ("", "anglais", svg.DIM),
            ]), "Het werkwoord komt tussen ne en pas in."),
            ("p", "Je zet <strong>ne</strong> vóór en <strong>pas</strong> ná het werkwoord. "
                  "<em>Je ne parle pas anglais</em> betekent ik spreek geen Engels. Twee woordjes "
                  "dus, met het werkwoord ertussen."),
            ("p", "Voor een klinker wordt <strong>ne</strong> tot <strong>n'</strong>: "
                  "<em>je n'aime pas</em>, <em>il n'est pas</em>, <em>elle n'habite pas ici</em>. "
                  "En na een ontkenning wordt un of une meestal <strong>de</strong>: "
                  "<em>Je n'ai pas de chien</em> is ik heb geen hond."),
        ]),
        dict(kop="Een vraag stellen", blokken=[
            ("p", "De makkelijkste manier is <strong>est-ce que</strong> vooraan de zin te zetten. "
                  "De rest blijft gewoon staan: <em>Est-ce que tu aimes le chocolat ?</em> "
                  "De woorden omdraaien mag ook, maar dat is moeilijker."),
            ("fig", tabel(["Vraagwoord", "Betekenis", "Voorbeeld"], [
                ["où", "waar", "Où habites-tu ?"],
                ["quand", "wanneer", "Quand est-ce que tu viens ?"],
                ["pourquoi", "waarom", "Pourquoi es-tu triste ?"],
                ["comment", "hoe", "Comment ça va ?"],
            ]), "Op pourquoi antwoord je meestal met parce que, omdat."),
            ("weetje", "In het Frans staat er een <strong>spatie vóór</strong> een vraagteken en "
                       "een uitroepteken: <em>Comment ça va ?</em> en <em>Bonjour !</em> Die regel "
                       "kent het Nederlands niet."),
        ]),
        dict(kop="Waar staat het bijvoeglijk naamwoord?", blokken=[
            ("p", "In het Nederlands zeg je een <em>zwarte</em> hond, met de kleur ervóór. In het "
                  "Frans staat het bijvoeglijk naamwoord meestal <strong>achter</strong> het woord: "
                  "<em>un chien noir</em>, <em>une voiture rouge</em>."),
            ("p", "Bij een <strong>vrouwelijk</strong> woord krijgt het er meestal een "
                  "<strong>e</strong> bij: <em>un petit garçon</em>, <em>une petite fille</em>. "
                  "In het meervoud komt er nog een <strong>s</strong> bij: les petites filles."),
            ("kader", "Een rode auto is dus <strong>une voiture rouge</strong>: voiture is "
                      "vrouwelijk (une), en de kleur komt erachter. <em>Une rouge voiture</em> en "
                      "<em>un voiture rouge</em> kloppen allebei niet."),
        ]),
        dict(kop="Woordjes die zinnen aan elkaar knopen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["et", "en"], ["ou", "of"], ["mais", "maar"], ["parce que", "omdat"],
            ], "60%"), "J'aime le chocolat, mais je préfère les bonbons."),
            ("p", "De woordvolgorde van het Frans is dus <strong>niet</strong> altijd dezelfde als "
                  "in het Nederlands: de kleur verhuist naar achter, en in een ontkenning staat het "
                  "werkwoord tussen ne en pas."),
        ]),
    ],
    onthoud=[
        "le bij een mannelijk woord, la bij een vrouwelijk, l' voor een klinker, les in het meervoud.",
        "un en une betekenen allebei een: un livre, une table.",
        "Ontkennen doe je met ne … pas, met het werkwoord ertussen.",
        "Voor een klinker wordt ne tot n'; na een ontkenning wordt un of une meestal de.",
        "Est-ce que vooraan maakt van elke zin een vraag.",
        "Het bijvoeglijk naamwoord staat meestal achter het woord: un chien noir.",
        "In het Frans staat er een spatie vóór een vraagteken en een uitroepteken.",
    ],
)

# ===========================================================================
BUNDELS["op-school-en-onderweg"] = dict(
    vak=VAK, titel="Op school en onderweg",
    onder="Je schoolgerief, de vakken, de weg vragen en de zinnetjes die je in de klas nodig hebt.",
    secties=[
        dict(kop="In je boekentas", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un cartable", "een boekentas"], ["une trousse", "een pennenzak"],
                ["un livre", "een boek"], ["un cahier", "een schrift"],
                ["un stylo", "een balpen"], ["un crayon", "een potlood"],
                ["une gomme", "een gom"], ["une règle", "een lat"],
                ["une boîte à tartines", "een brooddoos"],
            ], "70%"), "Un stylo is een balpen, un crayon een potlood."),
            ("weetje", "<strong>Une règle</strong> betekent zowel het voorwerp waarmee je meet "
                       "als een afspraak, een regel die je moet volgen. Net als in het Nederlands, "
                       "waar een lat en een regel ook twee dingen zijn."),
        ]),
        dict(kop="Op school", blokken=[
            ("p", "<strong>La récréation</strong> is de speeltijd; in de spreektaal korten ze dat "
                  "af tot <strong>la récré</strong>."),
            ("p", "De vakken: <strong>les mathématiques</strong>, le français, le néerlandais, "
                  "l'histoire. Het schoolvak wiskunde heet in het Frans altijd in het "
                  "<strong>meervoud</strong>: les mathématiques, in de spreektaal afgekort tot "
                  "les maths."),
            ("fig", svg.spreekballonnen([
                ("de leerkracht", "Ouvrez votre livre.", True),
                ("jij", "Je ne comprends pas.", False),
                ("jij", "Répétez, s'il vous plaît.", False),
            ]), "De drie zinnetjes die je in de klas het meest nodig hebt."),
            ("p", "<strong>Ouvrir</strong> is openen en <strong>fermer</strong> is sluiten, dus "
                  "<em>Ouvrez votre livre</em> betekent open je boek. "
                  "<strong>Comprendre</strong> is begrijpen: <em>Je ne comprends pas</em> is ik "
                  "begrijp het niet. En <strong>répéter</strong> is herhalen, handig als iemand te "
                  "snel spreekt."),
        ]),
        dict(kop="De weg vragen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["à gauche", "links"], ["à droite", "rechts"],
                ["tout droit", "rechtdoor"], ["une rue", "een straat"],
                ["une place", "een plein"], ["un pont", "een brug"],
                ["la gare", "het station"], ["un garage", "een garage"],
            ], "70%"), "Tournez à gauche betekent sla links af."),
            ("kader", "<strong>À droite</strong> is naar rechts, <strong>tout droit</strong> is "
                      "rechtdoor. Die twee lijken op elkaar en worden voortdurend verward. "
                      "En <strong>la gare</strong> (het station) lijkt op un garage, maar dat is "
                      "iets anders."),
        ]),
        dict(kop="In de winkel", blokken=[
            ("fig", tabel(["Frans", "Je koopt er"], [
                ["la boulangerie", "brood, le pain"],
                ["la pharmacie", "medicijnen"],
                ["la librairie", "boeken — je koopt ze"],
                ["la bibliothèque", "boeken — je leent ze"],
                ["la piscine", "niets, dat is het zwembad"],
            ], "80%"), "Une librairie is een boekhandel, geen bibliotheek."),
            ("p", "Wil je weten wat iets kost, dan vraag je <strong>C'est combien ?</strong> "
                  "of <em>Ça coûte combien ?</em>"),
        ]),
        dict(kop="Onderweg", blokken=[
            ("p", "<strong>À vélo</strong> is met de fiets en <strong>à pied</strong> te voet. "
                  "Zit je ín het voertuig, dan gebruik je <strong>en</strong>: "
                  "<strong>en bus</strong> (met de bus), <strong>en voiture</strong> (met de auto). "
                  "Op de fiets zit je erop, vandaar à vélo."),
            ("p", "<em>Je vais à l'école à vélo</em> betekent dus ik ga met de fiets naar school."),
        ]),
    ],
    onthoud=[
        "un stylo is een balpen, un crayon een potlood.",
        "Wiskunde heet altijd in het meervoud: les mathématiques.",
        "à droite is naar rechts, tout droit is rechtdoor.",
        "la librairie is een boekhandel, la bibliothèque de bibliotheek.",
        "C'est combien ? vraag je om te weten wat iets kost.",
        "à vélo en à pied, maar en bus en en voiture.",
    ],
)

# ===========================================================================
BUNDELS["een-tekstje-lezen"] = dict(
    vak=VAK, titel="Een tekstje lezen",
    onder="Een echt Frans verhaaltje lezen, ook als je niet elk woord kent.",
    secties=[
        dict(kop="Je hoeft niet elk woord te kennen", blokken=[
            ("p", "Een tekst lezen in een taal die je aan het leren bent, gaat niet woord voor "
                  "woord. Lees eerst de hele tekst door en kijk wat je <strong>wél</strong> "
                  "herkent: namen, getallen, dagen, woorden die op het Nederlands of het Engels "
                  "lijken. Daarna pas de moeilijke stukken."),
            ("kader", "De meeste vragen bij een tekst zijn te beantwoorden met de woorden die je "
                      "al kent. Zoek in de tekst de <strong>zin</strong> waar de vraag over gaat, "
                      "en lees die zin dan traag."),
        ]),
        dict(kop="De woorden van dit verhaaltje", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le marché", "de markt"], ["la marchande", "de marktvrouw"],
                ["le grand-père", "de grootvader"], ["l'église", "de kerk"],
                ["à côté de", "naast"], ["la place", "het plein"],
                ["le panier", "de mand"], ["lourd", "zwaar"],
                ["la soupe", "de soep"], ["préféré", "favoriet"],
            ], "70%"), "Deze woorden komen allemaal in het verhaaltje voor."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une pomme", "een appel"], ["les pommes de terre", "de aardappelen"],
                ["les carottes", "de wortelen"], ["les fleurs", "de bloemen"],
                ["le pain", "het brood"], ["la boulangerie", "de bakkerij"],
                ["il pleut", "het regent"], ["à midi", "'s middags"],
                ["tout de suite", "meteen"], ["alors", "dus"],
            ], "70%"), "Une pomme is een appel; les pommes de terre zijn aardappelen."),
            ("weetje", "<strong>Il pleut</strong> komt van pleuvoir, regenen. Over het weer zegt "
                       "het Frans bijna altijd <em>il</em>: il pleut, il fait froid, il fait beau."),
        ]),
        dict(kop="Werkwoorden die je in een verhaaltje tegenkomt", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["acheter → il achète", "kopen → hij koopt"],
                ["dire → il dit", "zeggen → hij zegt"],
                ["rire → il rit", "lachen → hij lacht"],
                ["manger → elle mange", "eten → zij eet"],
                ["rentrer → ils rentrent", "naar huis gaan → zij gaan naar huis"],
                ["porter → elle porte", "dragen → zij draagt"],
                ["faire → elle fait", "maken → zij maakt"],
            ]), "Allemaal in de tegenwoordige tijd, zoals je in hoofdstuk 4 geleerd hebt."),
            ("p", "Staat een verhaaltje helemaal in de <strong>tegenwoordige tijd</strong>, dan "
                  "lees je het alsof het nu gebeurt. Dat maakt het makkelijker: je hoeft geen "
                  "andere tijden te herkennen."),
        ]),
        dict(kop="Let op de kleine woordjes", blokken=[
            ("p", "<strong>Le samedi</strong> betekent op zaterdag, en dus niet op woensdag, "
                  "vrijdag of zondag. <strong>Ne … pas</strong> keert de zin om: "
                  "<em>Camille ne va pas à l'école</em> betekent dat ze juist <em>niet</em> naar "
                  "school gaat. Lees die twee woordjes dus altijd mee."),
            ("p", "<strong>Le mien aussi</strong> betekent de mijne ook: iemand die dat zegt, is "
                  "het met je eens. Zegt iemand dat, dan vindt hij er dus niet anders over."),
            ("p", "<strong>Mon jour préféré</strong> is mijn lievelingsdag: <em>le jour</em> is de "
                  "dag en <em>préféré</em> favoriet. Zo'n uitdrukking van twee bekende woorden "
                  "komt in bijna elk tekstje voor."),
            ("p", "En de beleefde woorden uit hoofdstuk 1 komen terug in het verhaal: wie een "
                  "winkel of een kraam binnenstapt, begroet met <strong>bonjour</strong>, bedankt "
                  "met <strong>merci</strong> en vraagt iets met <strong>s'il vous plaît</strong>."),
            ("p", "Bij een vraag naar de <strong>titel</strong> van een tekst kies je wat over de "
                  "hele tekst gaat, niet wat maar in één zin voorkomt."),
        ]),
    ],
    onthoud=[
        "Lees eerst de hele tekst door en kijk wat je wél herkent.",
        "Zoek de zin waar de vraag over gaat, en lees die dan traag.",
        "le samedi betekent op zaterdag, en dus niet op een andere dag.",
        "ne … pas keert de zin om: lees die twee woordjes altijd mee.",
        "il pleut is het regent; over het weer zegt het Frans il.",
        "Een titel gaat over de hele tekst, niet over één zin.",
    ],
)

# ===========================================================================
BESCHRIJVEN_INLEIDING = (
    "Op het examen van de Examencommissie krijg je bij een taal een <strong>foto of "
    "prent</strong>, en moet je in die taal vertellen wat je ziet. Hier oefen je de woorden en "
    "de zinnetjes die je daarvoor nodig hebt. Wie die kent, kan straks ook zelf een beschrijving "
    "schrijven."
)

ER_IS = [
    ("p", "Elke beschrijving begint met <strong>il y a</strong>: er is, of er zijn. Het verandert "
          "nooit van vorm, hoeveel dingen er ook staan."),
    ("fig", svg.spreekballonnen([
        ("één ding", "Sur l'image, il y a un garçon.", True),
        ("meer dingen", "Il y a trois oiseaux.", False),
        ("iets dat er niet is", "Il n'y a pas de chien.", True),
    ]), "Il y a wordt il n'y a pas de als iets er juist niet is."),
    ("p", "<strong>Sur l'image</strong> betekent op de prent. Begin je zin daarmee, dan weet de "
          "lezer meteen waar je het over hebt. <em>Sur l'image, je suis …</em> of "
          "<em>Sur l'image, j'ai …</em> klopt niet: dat gaat over jou, niet over de prent."),
]

WAAR_STAAT_HET = [
    ("fig", svg.fotokader(), "Met deze woorden deel je elke prent in."),
    ("p", "<strong>À gauche</strong> is links, <strong>à droite</strong> is rechts en "
          "<strong>au milieu</strong> in het midden. En van boven naar onder: "
          "<strong>en haut</strong> is bovenaan, <strong>en bas</strong> is onderaan. Samen kan je "
          "zo elk plekje aanwijzen: <em>en haut à droite</em> is rechtsboven, <em>en bas à "
          "droite</em> rechtsonder en <em>en bas à gauche</em> linksonder."),
]

BUNDELS["wat-zie-je-op-de-prent"] = dict(
    vak=VAK, titel="Wat zie je op de prent?",
    onder="Vertellen wat er op een beeld te zien is: er is en er zijn, links en rechts, kleuren en aantallen.",
    secties=[
        dict(kop="Waarvoor dient dit?", blokken=[("kader", BESCHRIJVEN_INLEIDING)]),
        dict(kop="Er is en er zijn", blokken=ER_IS),
        dict(kop="Waar staat het?", blokken=WAAR_STAAT_HET),
        dict(kop="De dieren op deze prent", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une vache", "een koe"], ["un écureuil", "een eekhoorn"],
                ["un oiseau", "een vogel"], ["un lapin", "een konijn"],
                ["un canard", "een eend"], ["un chien", "een hond"],
                ["un chat", "een kat"], ["un cheval", "een paard"],
                ["un poisson", "een vis"], ["une grenouille", "een kikker"],
                ["une tortue", "een schildpad"],
            ], "70%"), "Niet alles uit deze lijst staat op de prent: kijk goed."),
            ("p", "Wil je zeggen wat een dier <strong>doet</strong>, dan hang je er een werkwoord "
                  "aan met <strong>qui</strong>: <em>un lapin qui court</em> (een konijn dat loopt), "
                  "<em>un chat qui dort</em> (een kat die slaapt), <em>un chien qui joue</em> "
                  "(een hond die speelt), <em>un cheval qui mange</em> (een paard dat eet)."),
        ]),
        dict(kop="Het landschap", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une montagne", "een berg"], ["un pont", "een brug"],
                ["une rivière", "een rivier"], ["le soleil", "de zon"],
                ["le ciel", "de lucht"], ["un arbre", "een boom"],
                ["une barrière", "een hek"], ["l'herbe", "het gras"],
            ], "70%"), "Le soleil is de zon; il fait du soleil betekent het is zonnig."),
            ("p", "Wat er in de lucht gebeurt, zeg je met <strong>voler</strong> (vliegen): "
                  "<em>Trois oiseaux volent dans le ciel</em> betekent er vliegen drie vogels in "
                  "de lucht."),
        ]),
        dict(kop="Mensen en wat ze dragen", blokken=[
            ("p", "<strong>Porter</strong> is dragen: <em>Le garçon porte un casque</em> betekent "
                  "de jongen draagt een helm. <strong>Un casque</strong> is een helm en "
                  "<strong>une veste</strong> is een jas."),
            ("p", "<strong>Faire du vélo</strong> is fietsen, net zoals faire du sport sporten is. "
                  "Andere dingen die iemand kan doen: <em>jouer au football</em> (voetballen), "
                  "<em>marcher à l'école</em> (naar school stappen), <em>nager</em> (zwemmen)."),
        ]),
        dict(kop="Tellen en kleuren op een prent", blokken=[
            ("p", "Tel altijd na op de prent zelf, en zet het getal vooraan: un, deux, trois, "
                  "quatre, cinq. Bij één ding hangt het af van het woord: <strong>un</strong> "
                  "oiseau (mannelijk), <strong>une</strong> vache (vrouwelijk). Vanaf twee maakt "
                  "dat niet meer uit, en krijgt het woord een <strong>s</strong>: deux arbres, "
                  "trois oiseaux."),
            ("p", "Twee kleuren samen zeg je met <strong>et</strong>: <em>brun et blanc</em> "
                  "(bruin en wit), <em>noir et blanc</em> (zwart en wit). Is iets helemaal in één "
                  "kleur, dan zeg je <strong>tout</strong>: tout brun, tout blanc."),
            ("kader", "Bij dit soort vragen lijken de antwoorden bewust op elkaar. "
                      "<strong>Kijk eerst naar de prent, en pas daarna naar de antwoorden.</strong> "
                      "Twijfel je tussen bleu en rouge, of tussen deux en trois, tel dan nog eens."),
        ]),
    ],
    onthoud=[
        "Elke beschrijving begint met il y a; dat verandert nooit van vorm.",
        "Is iets er juist niet, dan wordt het il n'y a pas de.",
        "Sur l'image betekent op de prent.",
        "à gauche, à droite, au milieu, en haut, en bas.",
        "Met qui hang je een werkwoord aan een dier: un chat qui dort.",
        "porter is dragen: le garçon porte un casque.",
        "Kijk eerst naar de prent, en pas daarna naar de antwoorden.",
    ],
)

# ===========================================================================
BUNDELS["wat-zie-je-aan-zee"] = dict(
    vak=VAK, titel="Wat zie je aan zee?",
    onder="Nog een beeld beschrijven, met de woorden van het strand, de boten en het kamperen.",
    secties=[
        dict(kop="Waarvoor dient dit?", blokken=[("kader", BESCHRIJVEN_INLEIDING)]),
        dict(kop="Er is en er zijn", blokken=ER_IS),
        dict(kop="Waar staat het?", blokken=WAAR_STAAT_HET),
        dict(kop="Waar speelt het zich af?", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["à la mer", "aan zee"], ["à la montagne", "in de bergen"],
                ["dans la ville", "in de stad"], ["dans la forêt", "in het bos"],
            ], "70%"), "Zie je water, boten en zand, dan is het à la mer."),
            ("p", "<strong>La mer</strong> is de zee en <strong>la plage</strong> is het strand. "
                  "<strong>Le sable</strong> is zand, dus een <strong>château de sable</strong> is "
                  "een zandkasteel: château betekent kasteel."),
        ]),
        dict(kop="Aan het water", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un bateau", "een boot"], ["un phare", "een vuurtoren"],
                ["un seau", "een emmer"], ["un coquillage", "een schelp"],
                ["un canard", "een eend"], ["un arbre", "een boom"],
                ["une cabane", "een hut"], ["une tente", "een tent"],
            ], "70%"), "Un phare, de vuurtoren, staat meestal op de rotsen."),
            ("p", "Pas op met woorden die op elkaar lijken: <strong>un bateau</strong> is een boot, "
                  "maar un bain is een bad, une balle een bal en un lit een bed. En "
                  "<strong>une tente</strong> is een tent, geen tafel (une table), toren (une tour) "
                  "of trap (un escalier)."),
        ]),
        dict(kop="De mensen op de prent", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un garçon", "een jongen"], ["une fille", "een meisje"],
                ["un homme", "een man"], ["une femme", "een vrouw"],
                ["un enfant", "een kind"], ["les enfants", "de kinderen"],
            ], "70%"), "La fille is het meisje, le garçon de jongen."),
            ("p", "Wil je er iets bij vertellen, dan zet je het werkwoord erachter: "
                  "<em>La fille porte une robe</em> (het meisje draagt een jurk), "
                  "<em>Le garçon sur le ponton pêche</em> (de jongen op de steiger vist). "
                  "<strong>Un ponton</strong> is een steiger: de houten loopplank die het water "
                  "in steekt."),
        ]),
        dict(kop="Dieren aan zee", blokken=[
            ("p", "<strong>Un chien</strong> is een hond en <strong>un chat</strong> een kat. In "
                  "het water zwemmen <strong>des canards</strong> (eenden); in een ander water zou "
                  "je <em>des poissons</em> (vissen), <em>des tortues</em> (schildpadden) of "
                  "<em>des grenouilles</em> (kikkers) kunnen zien."),
            ("p", "<strong>Caresser</strong> is aaien: <em>Le garçon caresse un chien</em> betekent "
                  "de jongen aait een hond."),
        ]),
        dict(kop="Wat de mensen doen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Il pêche.", "Hij vist."], ["Il nage.", "Hij zwemt."],
                ["Il dort.", "Hij slaapt."], ["Il chante.", "Hij zingt."],
            ], "60%"), "Pêcher is vissen; een hengel is une canne à pêche."),
            ("p", "En over de zon: <strong>le soleil se couche</strong> betekent dat de zon "
                  "ondergaat. Hangt de zon laag boven het water en is de lucht oranje, dan is het "
                  "avond."),
        ]),
        dict(kop="Kleren en kleuren", blokken=[
            ("p", "<strong>Porter</strong> is dragen. <strong>Un chapeau</strong> is een hoed, met "
                  "een rand rondom; <strong>une casquette</strong> is een pet, met een klep "
                  "vooraan. Dat verschil is precies het soort ding waar zo'n vraag naar peilt. "
                  "<strong>Une robe</strong> is een jurk, <strong>un casque</strong> een helm, "
                  "<strong>un manteau</strong> een jas en <strong>un parapluie</strong> een "
                  "paraplu. Die laatste drie draag je niet op je hoofd, dus ze passen niet als "
                  "er naar een hoed gevraagd wordt."),
            ("p", "Bij een vrouwelijk woord krijgt de kleur er een <strong>e</strong> bij: "
                  "<em>la tente est verte</em> (de tent is groen), maar <em>le seau est rouge</em> "
                  "(de emmer is rood), want rouge eindigt al op een e."),
            ("kader", "Tel de mensen en de dieren <strong>op de prent zelf</strong>, niet uit je "
                      "hoofd. Un, deux, trois, quatre: het verschil tussen twee en drie kinderen is "
                      "vaak precies waar de vraag om draait."),
        ]),
    ],
    onthoud=[
        "Elke beschrijving begint met il y a; is iets er niet, dan il n'y a pas de.",
        "à gauche, à droite, au milieu, en haut, en bas.",
        "la mer is de zee, la plage het strand, le sable het zand.",
        "un chapeau heeft een rand rondom, une casquette een klep vooraan.",
        "Bij een vrouwelijk woord krijgt de kleur er een e bij: la tente est verte.",
        "Tel de mensen en de dieren op de prent zelf, niet uit je hoofd.",
    ],
)

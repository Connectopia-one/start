# -*- coding: utf-8 -*-
"""Eén overkoepelende leerbundel per vak voor 🧱 Basis: Frans, Nederlands en wiskunde.

Kim op 11 november 2026: "mss is het wel interessant dat er gewoon bij basis 1
overkoepelende leerbundel is per vak en niet per hoofdstuk? dan zijn er 3
bundels". Basis is vooral oefenen; een kind dat vastloopt, vindt in één bundel
per vak alles terug wat in de vragen gevraagd wordt, onderwerp per onderwerp.

Dezelfde bundel hangt bij elk hoofdstuk van dat vak (deel 1 en deel 2).
Alles hieruit komt uit de vragen van basis/<vak>.json en wiskunde-extra.json:
geen leerstof erbij die daar niet gevraagd wordt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
from bundel import tabel

BASIS = "🧱 Basis — de bouwstenen herhalen"
PLAATS = ["D", "H", "T", "E", "t", "h", "d"]

BUNDELS = {}


# ---------------------------------------------------------------------------
# Frans
# ---------------------------------------------------------------------------
BUNDELS["frans-alles-op-een-rij-basis"] = dict(
    vak="Frans", niveau=BASIS, titel="Frans in Basis: alles op een rij",
    onder="De woorden en zinnetjes die je elke dag nodig hebt, onderwerp per onderwerp. "
          "Zoek het onderwerp op waar je mee oefent.",
    secties=[
        dict(kop="1. Getallen", blokken=[
            ("p", "De getallen tot twintig ken je best vanbuiten. Daarna bouw je verder met tientallen."),
            ("p", tabel(["getal", "Frans", "getal", "Frans"], [
                ["1", "un", "11", "onze"], ["2", "deux", "12", "douze"],
                ["3", "trois", "13", "treize"], ["4", "quatre", "14", "quatorze"],
                ["5", "cinq", "15", "quinze"], ["6", "six", "16", "seize"],
                ["7", "sept", "17", "dix-sept"], ["8", "huit", "18", "dix-huit"],
                ["9", "neuf", "19", "dix-neuf"], ["10", "dix", "20", "vingt"],
            ])),
            ("p", tabel(["getal", "Frans", "letterlijk"], [
                ["70", "soixante-dix", "zestig-tien"],
                ["80", "quatre-vingts", "vier-twintig"],
                ["90", "quatre-vingt-dix", "vier-twintig-tien"],
                ["100", "cent", ""],
            ])),
            ("weetje", "<strong>Neuf</strong> betekent negen, maar ook <strong>nieuw</strong>. "
                       "Uit de zin weet je welke van de twee het is."),
        ]),
        dict(kop="2. Kleuren", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["rouge", "rood", "noir", "zwart"],
                ["vert", "groen", "blanc", "wit"],
                ["jaune", "geel", "bleu", "blauw"],
                ["bleu clair", "lichtblauw", "", ""],
            ])),
            ("kader", "Een kleur staat in het Frans meestal <strong>achter</strong> het woord: "
                      "<em>un vélo rouge</em> is een rode fiets."),
        ]),
        dict(kop="3. Dagen, maanden en tijd", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["lundi", "maandag", "vendredi", "vrijdag"],
                ["mardi", "dinsdag", "samedi", "zaterdag"],
                ["mercredi", "woensdag", "dimanche", "zondag"],
                ["jeudi", "donderdag", "le week-end", "het weekend"],
            ])),
            ("p", "De Franse week begint op <strong>lundi</strong>. Twee maanden die vaak terugkomen: "
                  "<strong>janvier</strong> is januari en <strong>juillet</strong> is juli. "
                  "Dagen en maanden krijgen in het Frans <strong>geen hoofdletter</strong>."),
            ("p", tabel(["Frans", "Nederlands"], [
                ["aujourd'hui", "vandaag"], ["demain", "morgen"], ["hier", "gisteren"],
                ["la semaine", "de week"], ["le mois", "de maand"], ["le matin", "de ochtend"],
            ])),
        ]),
        dict(kop="4. Hoe laat is het?", blokken=[
            ("p", "Je vraagt het uur met <strong>Quelle heure est-il ?</strong>"),
            ("p", tabel(["Frans", "Nederlands"], [
                ["Il est trois heures.", "Het is drie uur."],
                ["Il est huit heures.", "Het is acht uur."],
                ["... et quart", "kwart over ..."],
                ["... moins le quart", "kwart voor ..."],
                ["midi", "middag, twaalf uur 's middags"],
            ])),
            ("weetje", "<strong>Midi</strong> is twaalf uur 's middags, niet middernacht."),
        ]),
        dict(kop="5. Jezelf voorstellen", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["Bonjour", "Goeiedag (overdag)"], ["Salut", "Hoi (tegen vrienden)"],
                ["Au revoir", "Tot ziens"], ["Ça va ?", "Hoe gaat het?"],
                ["Comment tu t'appelles ?", "Hoe heet je?"], ["Je m'appelle Lotte.", "Ik heet Lotte."],
                ["J'ai douze ans.", "Ik ben twaalf jaar."], ["J'habite à Hasselt.", "Ik woon in Hasselt."],
                ["Tu viens d'où ?", "Waar kom je vandaan?"], ["Enchanté", "Aangenaam"],
            ])),
            ("kader", "Je leeftijd zeg je met <strong>avoir</strong> (hebben): <em>j'ai douze ans</em>, "
                      "letterlijk ik heb twaalf jaren. <em>Je suis douze ans</em> is fout."),
        ]),
        dict(kop="6. Beleefd zijn en hulp vragen", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["oui", "ja"], ["merci", "dank je wel"], ["De rien", "Graag gedaan (antwoord op merci)"],
                ["S'il vous plaît", "Alstublieft"], ["Pardon", "Sorry, pardon"],
                ["Je ne comprends pas.", "Ik begrijp het niet."],
                ["Comment ça s'écrit ?", "Hoe schrijf je dat?"],
            ])),
            ("kader", "<strong>Tu</strong> zeg je tegen een vriend of iemand van je familie. "
                      "<strong>Vous</strong> zeg je tegen een volwassene die je niet kent, en tegen meer mensen tegelijk."),
        ]),
        dict(kop="7. De familie", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["le père", "de vader", "la mère", "de moeder"],
                ["le frère", "de broer", "la sœur", "de zus"],
                ["le fils", "de zoon", "la fille", "de dochter"],
                ["les parents", "de ouders", "les grands-parents", "de grootouders"],
                ["la grand-mère", "de oma", "l'oncle", "de oom"],
                ["un cousin", "een neef", "une cousine", "een nicht"],
            ])),
            ("kader", "<strong>Mon</strong> of <strong>ma</strong> (mijn) hangt af van het woord erachter, "
                      "niet van wie er spreekt: <em>mon père</em>, <em>ma sœur</em>. "
                      "Voor meer dan één gebruik je <strong>mes</strong>: <em>mes frères</em>."),
            ("p", "Nog een paar zinnetjes: <em>Il est grand.</em> (Hij is groot.) "
                  "<em>Elle est gentille.</em> (Zij is lief.) <em>J'ai un chien.</em> (Ik heb een hond.) "
                  "<em>Nous sommes quatre à la maison.</em> (We zijn met vier thuis.)"),
        ]),
        dict(kop="8. Eten en drinken", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["le pain", "het brood", "l'eau", "het water"],
                ["le fromage", "de kaas", "le lait", "de melk"],
                ["la pomme", "de appel", "la viande", "het vlees"],
                ["le poisson", "de vis", "le dessert", "het nagerecht"],
                ["le petit déjeuner", "het ontbijt", "l'assiette", "het bord"],
                ["une baguette", "een lang, smal brood", "sans sucre", "zonder suiker"],
            ])),
            ("p", tabel(["Frans", "Nederlands"], [
                ["J'ai faim.", "Ik heb honger."], ["J'ai soif.", "Ik heb dorst."],
                ["C'est bon.", "Het is lekker."], ["Je voudrais un croissant.", "Ik zou graag een croissant hebben."],
            ])),
        ]),
        dict(kop="9. Winkelen", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["le magasin", "de winkel", "la caisse", "de kassa"],
                ["la boulangerie", "de bakkerij", "le prix", "de prijs"],
                ["la librairie", "de boekenwinkel", "la monnaie", "het wisselgeld"],
                ["cher", "duur", "bon marché", "goedkoop"],
                ["ouvert", "open", "fermé", "gesloten"],
            ])),
            ("p", tabel(["Frans", "Nederlands"], [
                ["Vous désirez ?", "Wat mag het zijn?"], ["C'est combien ?", "Hoeveel kost het?"],
                ["C'est trop cher.", "Het is te duur."], ["Je paie par carte.", "Ik betaal met de kaart."],
                ["un kilo de pommes", "een kilo appels"],
            ])),
            ("kader", "Na een maat zoals <em>un kilo</em> staat gewoon <strong>de</strong>: "
                      "<em>un kilo de pommes</em>."),
            ("weetje", "<strong>La librairie</strong> lijkt op bibliotheek, maar het is een boekenwinkel."),
        ]),
        dict(kop="10. Op school", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["l'école", "de school", "le livre", "het boek"],
                ["le cahier", "het schrift", "le crayon", "het potlood"],
                ["la gomme", "de gom", "le professeur", "de leerkracht"],
                ["la récréation", "de speeltijd", "les devoirs", "het huiswerk"],
                ["une erreur", "een fout", "un exercice", "een oefening"],
                ["les vacances", "de vakantie (altijd meervoud)", "", ""],
            ])),
            ("p", tabel(["Frans", "Nederlands"], [
                ["Ouvrez vos livres.", "Open jullie boeken."], ["Écoutez bien.", "Luister goed."],
                ["Répétez, s'il vous plaît.", "Herhaal, alstublieft."], ["Je ne sais pas.", "Ik weet het niet."],
                ["Comment dit-on ... en français ?", "Hoe zeg je ... in het Frans?"],
            ])),
        ]),
        dict(kop="11. Thuis en in de stad", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["la maison", "het huis", "la rue", "de straat"],
                ["la cuisine", "de keuken", "la gare", "het station"],
                ["la chambre", "de slaapkamer", "l'hôpital", "het ziekenhuis"],
                ["le jardin", "de tuin", "la voiture", "de auto"],
                ["la cave", "de kelder", "le vélo", "de fiets"],
                ["un arrêt de bus", "een bushalte", "", ""],
            ])),
            ("p", tabel(["Frans", "Nederlands"], [
                ["Où est la gare ?", "Waar is het station?"], ["à droite", "rechts"],
                ["à gauche", "links"], ["tout droit", "rechtdoor"], ["C'est loin ?", "Is het ver?"],
                ["Je vais à l'école à pied.", "Ik ga te voet naar school."],
            ])),
            ("weetje", "Het dakje op de o in <em>l'hôpital</em> en <em>l'hôtel</em> staat daar omdat er vroeger een s stond. "
                       "Denk aan ons woord hospitaal."),
        ]),
        dict(kop="12. Vier werkwoorden die je elke dag nodig hebt", blokken=[
            ("p", tabel(["", "être (zijn)", "avoir (hebben)", "aller (gaan)", "faire (doen, maken)"], [
                ["je", "suis", "ai", "vais", "fais"],
                ["tu", "es", "as", "vas", "fais"],
                ["il, elle", "est", "a", "va", "fait"],
                ["nous", "sommes", "avons", "allons", "faisons"],
                ["vous", "êtes", "avez", "allez", "faites"],
                ["ils, elles", "sont", "ont", "vont", "font"],
            ])),
            ("p", "Let op: <em>ils sont</em> is zij zijn, <em>ils ont</em> is zij hebben. "
                  "<em>Vous êtes</em> betekent jullie zijn of u bent. "
                  "Over het weer zeg je <em>il fait</em>: <em>Il fait froid.</em> (Het is koud.) "
                  "En <em>Quel âge as-tu ?</em> vraagt hoe oud je bent."),
        ]),
        dict(kop="13. Werkwoorden op -er", blokken=[
            ("p", "Veel werkwoorden eindigen op <strong>-er</strong>: <em>parler</em> (spreken), "
                  "<em>manger</em> (eten), <em>aimer</em> (graag hebben), <em>regarder</em> (kijken)."),
            ("kader", "Bij <strong>je</strong> haal je de -er weg en zet je er een <strong>-e</strong> achter: "
                      "<em>parler</em> wordt <em>je parle</em>. <em>Je parles</em> is fout."),
        ]),
        dict(kop="14. Niet doen: ne ... pas", blokken=[
            ("kader", "<strong>Ne</strong> staat vóór het werkwoord en <strong>pas</strong> erachter: "
                      "<em>Je ne sais pas.</em> (Ik weet het niet.) <em>Il ne sait pas.</em> (Hij weet het niet.)"),
            ("p", "Na een ontkenning wordt <em>du</em> of <em>de la</em> gewoon <strong>de</strong>: "
                  "<em>Je ne mange pas de viande.</em> (Ik eet geen vlees.)"),
        ]),
        dict(kop="15. Vragen stellen", blokken=[
            ("p", tabel(["Frans", "Nederlands", "Frans", "Nederlands"], [
                ["pourquoi", "waarom", "quand", "wanneer"],
                ["Qui est-ce ?", "Wie is dat?", "Qu'est-ce que c'est ?", "Wat is dat?"],
                ["beaucoup", "veel", "toujours", "altijd"],
            ])),
        ]),
    ],
    onthoud=[
        "Een kleur staat meestal achter het woord: un vélo rouge.",
        "Mon of ma hangt af van het woord erachter: mon père, ma sœur.",
        "Je leeftijd zeg je met avoir: j'ai douze ans.",
        "Tu tegen een vriend, vous tegen een onbekende volwassene.",
        "Bij werkwoorden op -er krijgt je een -e: je parle.",
        "Niet doen: ne vóór en pas achter het werkwoord.",
    ],
)


# ---------------------------------------------------------------------------
# Nederlands
# ---------------------------------------------------------------------------
BUNDELS["nederlands-alles-op-een-rij-basis"] = dict(
    vak="Nederlands", niveau=BASIS, titel="Nederlands in Basis: alles op een rij",
    onder="Woordsoorten, werkwoorden, zinsdelen en spelling. Elk onderwerp kort, met een voorbeeld.",
    secties=[
        dict(kop="1. Woordsoorten: wat doet elk woord?", blokken=[
            ("p", tabel(["woordsoort", "wat doet het?", "voorbeeld"], [
                ["lidwoord", "staat vóór een zelfstandig naamwoord; er zijn er maar drie: de, het, een", "<strong>de</strong> hond"],
                ["zelfstandig naamwoord", "een woord voor een ding, dier, persoon of gedachte", "een grote <strong>tafel</strong>"],
                ["bijvoeglijk naamwoord", "zegt hoe iets is, hoort bij een zelfstandig naamwoord", "de <strong>rode</strong> fiets"],
                ["werkwoord", "zegt wat er gebeurt; je kan het vervoegen", "Sara <strong>leest</strong>"],
                ["bijwoord", "zegt iets over het werkwoord, bijvoorbeeld hoe", "hij loopt <strong>snel</strong>"],
            ])),
            ("fig", svg.zinsdelen([("De", "lidwoord", svg.DIM), ("kat", "zelfst. naamwoord", svg.FOREST),
                                   ("slaapt", "werkwoord", svg.AMBER)]),
             "Een hele zin met maar drie woordsoorten."),
            ("kader", "Niet elk woord op -en is een werkwoord: <em>boeken</em> en <em>kinderen</em> zijn zelfstandige naamwoorden. "
                      "Of een woord de of het krijgt, moet je per woord weten: <em>het boek</em>."),
        ]),
        dict(kop="2. Nog meer woordsoorten", blokken=[
            ("p", tabel(["woordsoort", "wat doet het?", "voorbeelden"], [
                ["persoonlijk voornaamwoord", "vervangt een naam", "ik, jij, hij, zij, wij, hem"],
                ["bezittelijk voornaamwoord", "zegt van wie iets is", "mijn, jouw, zijn, haar, ons, hun"],
                ["voorzetsel", "zegt waar of wanneer", "op, in, onder, naast, achter, tijdens"],
                ["voegwoord", "plakt twee stukken aan elkaar", "en, of, maar, want, omdat"],
                ["telwoord", "zegt hoeveel", "drie, veel, weinig, enkele"],
            ])),
            ("kader", "Trucje voor een voorzetsel: past het in <em>de kat zit ... de doos</em>? "
                      "Dan is het een voorzetsel: op, in, onder, naast."),
            ("p", "<em>Jij</em> is persoonlijk, <em>jouw</em> is bezittelijk: jouw jas. "
                  "<em>Wij</em> is ik samen met anderen."),
        ]),
        dict(kop="3. Het werkwoord nu: de stam", blokken=[
            ("p", "De <strong>stam</strong> vind je door -en van het hele werkwoord te halen. "
                  "Klinkt het dan anders, dan pas je één letter aan."),
            ("p", tabel(["heel werkwoord", "stam", "waarom?"], [
                ["werken", "werk", "gewoon -en weg"],
                ["lopen", "loop", "anders klinkt de o kort"],
                ["spelen", "speel", "anders klinkt de e kort"],
                ["zitten", "zit", "nooit twee dezelfde medeklinkers achteraan"],
                ["rijden", "rijd", "de d hoor je niet, maar je schrijft hem wel"],
                ["schrijven", "schrijf", "een v achteraan wordt een f"],
            ])),
        ]),
        dict(kop="4. Wanneer komt er een t bij?", blokken=[
            ("fig", svg.werkwoord_nu(), "De ik-vorm is altijd de kale stam. Bij jij, hij, zij en u komt er een t bij."),
            ("kader", "Staat <strong>jij</strong> of <strong>je</strong> vlak <strong>achter</strong> het werkwoord, "
                      "dan valt de t weg: <em>jij komt</em>, maar <em>kom jij?</em> "
                      "Bij <strong>u</strong> en <strong>hij</strong> blijft de t altijd: <em>komt u morgen?</em>"),
            ("p", "Eindigt de stam al op een d, dan schrijf je dt: <em>hij vindt</em>, <em>jij wordt</em>. "
                  "Eindigt hij al op een t, dan komt er geen tweede bij: <em>weet jij</em>, <em>hij weet</em>. "
                  "Bij wij, jullie en zij (meer dan één) neem je het hele werkwoord: <em>wij gaan</em>, <em>jullie zijn</em>."),
        ]),
        dict(kop="5. De verleden tijd", blokken=[
            ("p", "Een <strong>zwak</strong> werkwoord krijgt -te of -de: <em>werken, werkte</em>. "
                  "Een <strong>sterk</strong> werkwoord verandert van klinker: <em>lopen, liep</em>; "
                  "<em>zingen, zong</em>; <em>geven, gaf</em>. Die leer je vanbuiten."),
            ("fig", svg.kofschip(), "Eindigt de stam op t, k, f, s, ch of p, dan wordt het -te. Anders -de."),
            ("p", tabel(["werkwoord", "stam", "verleden tijd"], [
                ["werken", "werk", "werkte"], ["hopen", "hoop", "hoopte"], ["praten", "praat", "praatte"],
                ["spelen", "speel", "speelde"], ["antwoorden", "antwoord", "antwoordde"],
                ["leven", "leef", "leefde (je kijkt naar de v van leven)"],
            ])),
        ]),
        dict(kop="6. Het voltooid deelwoord", blokken=[
            ("p", "Het voltooid deelwoord staat bij <em>heb</em>, <em>is</em> of <em>wordt</em>. "
                  "Meestal komt er ge- voor, en weer kiest 't kofschip tussen t en d: "
                  "<em>gewerkt</em>, <em>gespeeld</em>, <em>gemaakt</em>. Sterke werkwoorden eindigen op -en: "
                  "<em>gelopen</em>, <em>geschreven</em>."),
            ("kader", "<strong>gebeurd of gebeurt?</strong> Staat er is, heeft of heb bij, dan is het een voltooid deelwoord "
                      "met d: <em>het is gebeurd</em>. Zonder hulpwerkwoord is het nu: <em>dat gebeurt</em>."),
            ("p", "Begint het werkwoord met be-, ver-, ont- of her-, dan komt er geen ge- bij: "
                  "<em>betaald</em>, <em>verteld</em>, <em>verhuisd</em>. Bij verhuizen en verven kijk je naar de z en de v "
                  "van het hele werkwoord: <em>verhuisd</em>, <em>geverfd</em>."),
        ]),
        dict(kop="7. Zinsdelen: persoonsvorm en onderwerp", blokken=[
            ("kader", "<strong>Persoonsvorm</strong>: maak van de zin een vraag. Het woord dat naar voren springt, "
                      "is de persoonsvorm. <em>De hond blaft</em> wordt <em>Blaft de hond?</em> "
                      "Een gewone zin heeft er precies één."),
            ("kader", "<strong>Onderwerp</strong>: vraag <em>wie of wat</em> plus de persoonsvorm. "
                      "<em>Wie of wat blaft?</em> De hond."),
            ("fig", svg.zinsdelen([("Morgen", "bepaling van tijd", svg.DIM), ("komt", "persoonsvorm", svg.AMBER),
                                   ("mijn oma", "onderwerp", svg.FOREST)]),
             "Het onderwerp staat niet altijd vooraan."),
            ("p", "Een voltooid deelwoord zoals <em>gevoetbald</em> is nooit de persoonsvorm: "
                  "het verandert niet mee als je de zin in een andere tijd zet."),
        ]),
        dict(kop="8. Lijdend voorwerp en bepalingen", blokken=[
            ("kader", "<strong>Lijdend voorwerp</strong>: vraag <em>wie of wat</em> plus persoonsvorm plus onderwerp. "
                      "<em>Wie of wat eet Sara?</em> Een appel."),
            ("p", "Niet elke zin heeft een lijdend voorwerp: <em>De baby slaapt.</em> "
                  "<strong>Bepalingen</strong> zeggen waar (<em>in de tuin</em>), wanneer (<em>gisteren</em>) of hoe. "
                  "Een zinsdeel kan uit meer woorden bestaan: <em>de kinderen uit onze straat</em>."),
            ("kader", "Het onderwerp beslist de vorm van het werkwoord. <em>De zak met appels <strong>is</strong> zwaar</em>: "
                      "het onderwerp is de zak, één zak, dus is."),
        ]),
        dict(kop="9. Het meervoud", blokken=[
            ("p", tabel(["regel", "voorbeelden"], [
                ["meestal -en", "boek, boeken"],
                ["op -el, -em, -en, -er: een s", "tafel, tafels; bakker, bakkers"],
                ["na een losse klinker: 's", "auto's, foto's, oma's"],
                ["korte klinker: medeklinker dubbel", "bus, bussen; kat, katten"],
                ["lange klinker in open lettergreep: één klinker", "raam, ramen"],
                ["een paar woorden: -eren", "kind, kinderen; ei, eieren"],
                ["uit het Latijn", "museum, musea of museums"],
            ])),
        ]),
        dict(kop="10. Het verkleinwoord", blokken=[
            ("fig", svg.verkleinwoorden(), "Na een m komt -pje, na -ing komt -kje, na een korte klinker met l, m, n of r komt -etje."),
        ]),
        dict(kop="11. Hoofdletters en leestekens", blokken=[
            ("p", tabel(["wel een hoofdletter", "geen hoofdletter"], [
                ["het begin van een zin", "dagen: maandag"],
                ["namen, landen en steden: België, Antwerpen", "maanden: januari"],
                ["talen: Nederlands, Frans", "ik midden in een zin"],
            ])),
            ("p", tabel(["leesteken", "waar?"], [
                ["vraagteken ?", "achter een vraag: Hoe heet jij?"],
                ["uitroepteken !", "bij een uitroep of bevel: Pas op!"],
                ["komma ,", "tussen delen van een opsomming, en tussen twee stukken van een zin: Als het regent, blijven we thuis."],
                ["aanhalingstekens", "rond woorden die iemand letterlijk zegt"],
            ])),
            ("kader", "Samenstellingen schrijf je aan elkaar: <em>fietspad</em>, <em>voetbalploeg</em>, "
                      "<em>handdoek</em> (hand + doek, dus twee d's)."),
        ]),
    ],
    onthoud=[
        "De stam vind je door -en van het hele werkwoord te halen.",
        "Ik: kale stam. Jij, hij, u: stam + t. Jij achter het werkwoord: geen t.",
        "'t Kofschip (t, k, f, s, ch, p) kiest tussen -te en -de.",
        "Is, heeft of heb erbij: voltooid deelwoord, zoals gebeurd.",
        "Persoonsvorm: maak er een vraag van. Onderwerp: wie of wat plus persoonsvorm.",
        "Dagen en maanden zonder hoofdletter, talen met.",
    ],
)


# ---------------------------------------------------------------------------
# Wiskunde
# ---------------------------------------------------------------------------
BUNDELS["wiskunde-alles-op-een-rij-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Wiskunde in Basis: alles op een rij",
    onder="De bouwstenen van wiskunde in één bundel: de komma, maten, wiskundewoorden, breuken, "
          "kommagetallen, ggd en kgv.",
    secties=[
        dict(kop="1. Maal en gedeeld door 10, 100 en 1000", blokken=[
            ("fig", svg.cijfertabel(PLAATS, [
                dict(cijfers=["", "", "", "3", "4", "5", ""], komma=3, label="3,45"),
                dict(cijfers=["", "", "3", "4", "5", "", ""], komma=3, label="× 10 = 34,5"),
                dict(cijfers=["", "3", "4", "5", "", "", ""], komma=3, label="× 100 = 345"),
            ], accent=3),
             "D = duizendtal, H = honderdtal, T = tiental, E = eenheid; t, h, d = tiende, honderdste, duizendste."),
            ("kader", r"Tel de nullen. Zoveel plaatsen springt de komma. <strong>Maal</strong>: naar <strong>rechts</strong>, "
                      r"het getal wordt groter. <strong>Gedeeld door</strong>: naar <strong>links</strong>, het getal wordt kleiner. "
                      r"Is er geen plaats meer, zet er een \(0\) bij: \(3{,}45 \times 1000 = 3450\)."),
        ]),
        dict(kop="2. Maten omzetten", blokken=[
            ("fig", svg.maatladder(["km", "hm", "dam", "m", "dm", "cm", "mm"]), "Lengte: de hoofdmaat is de meter."),
            ("fig", svg.maatladder(["kg", "hg", "dag", "g", "dg", "cg", "mg"]), "Gewicht: de hoofdmaat is de gram."),
            ("fig", svg.maatladder(["hl", "dal", "l", "dl", "cl", "ml"]), "Inhoud: de hoofdmaat is de liter."),
            ("kader", r"Elke trede is maal of gedeeld door \(10\). Naar een <strong>kleinere</strong> maat (trapje af): "
                      r"<strong>maal</strong>, je krijgt meer stuks: \(2\) m \(= 200\) cm. Naar een <strong>grotere</strong> maat: "
                      r"<strong>gedeeld door</strong>: \(350\) cm \(= 3{,}5\) m."),
        ]),
        dict(kop="3. Wiskundewoorden", blokken=[
            ("p", tabel(["bewerking", "voorbeeld", "namen"], [
                ["optellen", r"\(5 + 3 = 8\)", "termen, som"],
                ["aftrekken", r"\(9 - 4 = 5\)", "aftrektal, aftrekker, verschil"],
                ["vermenigvuldigen", r"\(6 \times 4 = 24\)", "factoren, product"],
                ["delen", r"\(20 : 4 = 5\)", "deeltal, deler, quotiënt"],
                ["delen met rest", r"\(17 : 5 = 3\) rest \(2\)", r"quotiënt \(3\), rest \(2\)"],
            ])),
            ("fig", svg.breuk_namen(3, 4), "De teller staat boven de breukstreep, de noemer eronder."),
        ]),
        dict(kop="4. Breuken, kommagetallen en gehele getallen", blokken=[
            ("kader", r"Een breuk is een deling: \(\tfrac{3}{4} = 3 : 4 = 0{,}75\). "
                      r"Bij een noemer \(10\), \(100\) of \(1000\) gaat het snel: \(\tfrac{7}{10} = 0{,}7\) en \(\tfrac{65}{100} = 0{,}65\)."),
            ("p", tabel(["breuk", "kommagetal"], [
                [r"\(\tfrac{1}{2}\)", r"\(0{,}5\)"], [r"\(\tfrac{1}{4}\)", r"\(0{,}25\)"],
                [r"\(\tfrac{3}{4}\)", r"\(0{,}75\)"], [r"\(\tfrac{1}{5}\)", r"\(0{,}2\)"],
                [r"\(\tfrac{1}{10}\)", r"\(0{,}1\)"],
            ], breed="60%")),
            ("p", r"Is de teller een veelvoud van de noemer, dan is de breuk een geheel getal: \(\tfrac{12}{4} = 3\). "
                  r"Is de teller groter dan de noemer, dan is de breuk meer dan één: \(\tfrac{5}{4} = 1{,}25\)."),
        ]),
        dict(kop="5. Delers en veelvouden: ggd en kgv", blokken=[
            ("p", r"\(3\) is een <strong>deler</strong> van \(12\), want \(12 : 3\) gaat precies op. "
                  r"\(12\) is een <strong>veelvoud</strong> van \(3\)."),
            ("kader", r"<strong>ggd</strong> = de grootste gemeenschappelijke deler. Delers van \(12\): \(1, 2, 3, 4, 6, 12\). "
                      r"Delers van \(18\): \(1, 2, 3, 6, 9, 18\). Samen: \(1, 2, 3, 6\). De grootste is \(6\), dus ggd\((12, 18) = 6\)."),
            ("kader", r"<strong>kgv</strong> = het kleinste gemeenschappelijk veelvoud. Veelvouden van \(4\): \(4, 8, 12, 16, \ldots\) "
                      r"Veelvouden van \(6\): \(6, 12, 18, \ldots\) Het eerste dat in beide rijtjes staat, is \(12\), dus kgv\((4, 6) = 12\)."),
        ]),
        dict(kop="6. Kommagetallen vergelijken", blokken=[
            ("fig", svg.naast_elkaar([svg.procentraster(70, 150), svg.procentraster(65, 150)]),
             r"Links \(0{,}7\), rechts \(0{,}65\). Links is meer gekleurd."),
            ("kader", r"Maak de getallen even lang door nullen achteraan bij te schrijven: \(0{,}7 = 0{,}70\). "
                      r"Nu vergelijk je \(70\) honderdsten met \(65\) honderdsten. Dus \(0{,}7\) is <strong>groter</strong> dan \(0{,}65\). "
                      r"Een getal met meer cijfers na de komma is dus niet altijd groter."),
            ("p", r"Vergelijk eerst wat vóór de komma staat, dan de tienden, dan de honderdsten. "
                  r"Van klein naar groot: \(0{,}099\), \(0{,}1\), \(0{,}11\), \(0{,}2\)."),
        ]),
        dict(kop="7. Kommagetallen optellen en aftrekken", blokken=[
            ("kader", r"Zet de komma's onder elkaar en vul aan met nullen. Tel dan op of trek af zoals gewoonlijk, "
                      r"en zet de komma in de uitkomst op dezelfde plaats."),
            ("p", tabel(["", "", ""], [
                [r"\(\phantom{+}\,3{,}45\)", r"\(\phantom{-}\,5{,}00\)", r"\(\phantom{+}\,0{,}6\)"],
                [r"\(+\,2{,}50\)", r"\(-\,1{,}25\)", r"\(+\,0{,}4\)"],
                [r"\(=\,5{,}95\)", r"\(=\,3{,}75\)", r"\(=\,1{,}0 = 1\)"],
            ], breed="60%")),
            ("p", r"Let op: \(0{,}6 + 0{,}4\) is \(1\), niet \(0{,}10\). Tien tienden samen zijn één geheel."),
        ]),
        dict(kop="8. Breuken in beeld", blokken=[
            ("fig", svg.naast_elkaar([svg.breukfiguur("cirkel", 3, 8), svg.breukfiguur("strook", 3, 4)]),
             r"Links \(\tfrac{3}{8}\): \(8\) gelijke stukken, \(3\) gekleurd. Rechts \(\tfrac{3}{4}\)."),
            ("kader", r"De <strong>noemer</strong> zegt in hoeveel <strong>gelijke</strong> stukken het geheel verdeeld is. "
                      r"De <strong>teller</strong> zegt hoeveel stukken gekleurd zijn. Hoe meer stukken, hoe kleiner elk stuk: "
                      r"\(\tfrac{1}{3}\) is meer dan \(\tfrac{1}{4}\)."),
            ("p", r"Dezelfde hoeveelheid kan je op meer manieren schrijven: \(\tfrac{2}{4} = \tfrac{4}{8} = \tfrac{1}{2}\). "
                  r"Zo eenvoudig mogelijk schrijven doe je door teller en noemer door hetzelfde getal te delen: "
                  r"\(\tfrac{4}{6} = \tfrac{2}{3}\)."),
        ]),
    ],
    onthoud=[
        "Maal 10, 100, 1000: de komma springt naar rechts, zoveel plaatsen als er nullen zijn.",
        "Naar een kleinere maat: maal. Naar een grotere maat: gedeeld door.",
        "Een breuk is een deling: teller gedeeld door noemer.",
        "Kommagetallen vergelijken: maak ze even lang met nullen achteraan.",
        "Optellen en aftrekken: komma onder komma.",
        "ggd: grootste deler die ze delen. kgv: kleinste veelvoud dat ze delen.",
    ],
)


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

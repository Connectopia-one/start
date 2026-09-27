# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Frans ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Dezelfde pdf gaat dus bij allebei.

Net als de vragen op het scherm dekt dit **enkel de schriftelijke onderdelen**
van het examen: lezen, schrijven, woordenschat en grammatica. Spreken en
luisteren staan er niet in.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Wie hier iets bijschrijft, legt het eerst naast `../../spark/frans.json`.

Een leesvraag hoort op een echt tekstje in die taal te staan en niet op het
begrip alleen. De leesbundel draagt daarom zijn eigen Franse tekst mee.

Op papier staan de accenten er wél gewoon op. Dat online invulantwoorden
zonder accenten vergeleken worden, is een toegeving aan het toetsenbord, geen
regel over hoe je het schrijft.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "150px"
WW = "220px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Zet de accenten erbij: op papier horen ze er gewoon op.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands of Engels woord lijkt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-een-franse-tekst-lezen-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Een Franse tekst lezen",
    onder="Een tekst en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Lees de tekst eerst helemaal door. Je moet niet elk woord kennen.",
        "Onderstreep de woorden die je niet kent en probeer ze eerst te raden.",
        "Kom bij elke vraag terug naar de tekst.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
    ],
    reeksen=[
        dict(kop="La lecture",
             opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Une école sans cartable</h3>"
                  "<p>Depuis septembre, les élèves du collège Saint-Exupéry à Namur ne portent "
                  "plus de cartable. Tous leurs livres sont sur une tablette. L'école a acheté "
                  "trois cents tablettes, une pour chaque élève.</p>"
                  "<p>„Les sacs étaient trop lourds”, explique la directrice. „Certains élèves "
                  "portaient huit kilos sur le dos, tous les jours. Le médecin scolaire nous a "
                  "prévenus: c'est mauvais pour le dos.”</p>"
                  "<p>Cependant, tout n'est pas parfait. Les élèves disent qu'ils lisent moins "
                  "bien sur un écran. „Sur papier, je retrouve vite la page. Sur la tablette, je "
                  "cherche longtemps”, dit Lucas, treize ans. De plus, la batterie ne tient pas "
                  "toujours toute la journée.</p>"
                  "<p>L'école a donc gardé une solution: chaque classe a encore dix livres sur "
                  "papier dans l'armoire. „Environ un élève sur quatre les utilise”, dit la "
                  "directrice. „Nous allons évaluer le projet en juin, avec les élèves.”</p>"),
             ]),

        dict(kop="Wat staat er in de tekst",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Hoeveel tablettes heeft de school gekocht?", "driehonderd", W),
                 ("kort", "Hoe oud is Lucas?", "dertien jaar", W),
                 ("open", "Waarom schafte de school de boekentas af? Geef de reden uit de tekst.",
                  "De tassen waren te zwaar: sommige leerlingen droegen elke dag acht kilo op "
                  "hun rug, en de schoolarts waarschuwde dat dat slecht is voor de rug.", 4),
                 ("open", "Noem twee nadelen die in de tekst staan.",
                  "De leerlingen lezen minder goed op een scherm en vinden moeilijker de juiste "
                  "bladzijde terug, en de batterij houdt het niet altijd de hele dag vol.", 4),
                 ("kort", "Schrijf het onderwerp van deze tekst in enkele woorden.",
                  "een school zonder boekentas, met tablets", WW),
             ]),

        dict(kop="Woorden raden uit de tekst",
             opdracht="Gebruik de zin eromheen. Sla je woordenboek pas daarna open.",
             oefeningen=[
                 ("rij", [("lourds", "zwaar"), ("cependant", "nochtans / toch"),
                          ("l'armoire", "de kast"), ("environ", "ongeveer"),
                          ("de plus", "bovendien")],
                  "Wat betekent dit woord in de tekst?", WW),
                 ("open", "„Environ un élève sur quatre les utilise.” Naar wie of wat verwijst "
                          "'les' in deze zin?",
                  "Naar de tien papieren boeken in de kast.", 3),
                 ("waar", "Een Frans woord dat op een Nederlands of Engels woord lijkt, betekent "
                          "altijd hetzelfde.", False),
             ]),

        dict(kop="Strategie",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Boven een tekst staat 'Les jeunes et les écrans', met een foto van "
                          "een gsm erbij. Wat doe je het best vóór je begint te lezen?",
                  "Je gebruikt de titel en de foto om te voorspellen waarover het gaat, en je "
                  "bedenkt welke woorden je waarschijnlijk zal tegenkomen. Dan lees je sneller "
                  "en herken je meer.", 4),
                 ("rij", [("selon une étude récente", "er komt een bron of een cijfer"),
                          ("d'après l'auteur", "er komt een mening, geen feit"),
                          ("il est interdit de", "er komt een verbod"),
                          ("il s'agit de", "er komt het onderwerp")],
                  "Wat kondigt dit aan?", WW),
                 ("waar", "Je moet elk Frans woord kennen om een tekst te begrijpen.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-signaalwoorden-en-verwijswoorden-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Tekstsoorten, signaalwoorden en verwijswoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort",
             opdracht="Kijk naar de werkwoordsvorm en naar wat de tekst van je wil.",
             oefeningen=[
                 ("rij", [("Coupez les tomates. Ajoutez le sel.", "prescriptief"),
                          ("Ce film est ennuyeux, je ne le conseille à personne.", "argumentatief"),
                          ("Bruxelles compte plus d'un million d'habitants.", "informatief"),
                          ("Il était une fois une petite fille…", "narratief / literair")],
                  "Welke tekstsoort is dit?", WW),
                 ("open", "Waarom is het nuttig om te weten wat voor soort tekst je leest?",
                  "Je weet dan wat je moet zoeken: bij een instructie de stappen, bij een "
                  "informatieve tekst de feiten, bij een mening de argumenten. Je leest "
                  "gerichter en sneller.", 4),
             ]),

        dict(kop="Signaalwoorden",
             opdracht="Schrijf de betekenis én het verband.",
             oefeningen=[
                 ("rij", [("d'abord", "eerst"), ("puis", "daarna"), ("ensuite", "vervolgens"),
                          ("enfin", "ten slotte")],
                  "Wat betekent dit?"),
                 ("rij", [("parce que", "reden: omdat"), ("donc", "gevolg: dus"),
                          ("mais", "tegenstelling: maar"), ("pourtant", "tegenstelling: nochtans"),
                          ("par exemple", "voorbeeld: bijvoorbeeld"),
                          ("de plus", "toevoeging: bovendien")],
                  "Wat betekent dit, en welk verband kondigt het aan?", WW),
                 ("rij", [("Je reste à la maison ___ il pleut.", "parce qu'"),
                          ("Il a beaucoup travaillé, ___ il est fatigué.", "donc"),
                          ("Elle est petite, ___ elle court très vite.", "mais / pourtant")],
                  "Vul het passende signaalwoord in.", WW),
             ]),

        dict(kop="Verwijswoorden",
             opdracht="Schrijf naar wie of wat het woord verwijst.",
             oefeningen=[
                 ("rij", [("Les élèves sont en classe. <b>Ils</b> écoutent.", "les élèves"),
                          ("Je vais à Paris. J'<b>y</b> vais en train.", "à Paris"),
                          ("Ma sœur adore les chats. Elle <b>en</b> a trois.", "des chats"),
                          ("Marie parle à Paul. Elle <b>lui</b> explique tout.", "à Paul")],
                  "Naar wie of wat verwijst het vette woord?", WW),
                 ("waar", "'En' vervangt meestal een plaats en 'y' meestal een hoeveelheid.",
                  False),
                 ("open", "Leg uit wanneer je 'y' gebruikt en wanneer 'en'.",
                  "'Y' vervangt een plaats of een woordgroep met 'à'. 'En' vervangt een "
                  "hoeveelheid of een woordgroep met 'de'.", 4),
                 ("open", "Wat doe je als een verwijswoord in je eigen tekst onduidelijk is?",
                  "Je schrijft het woord waarnaar het verwijst opnieuw voluit, of je zet de "
                  "zinnen dichter bij elkaar zodat er geen twijfel meer is.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-berichten-uitnodigingen-en-mails-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Schrijven: berichten, uitnodigingen en mails",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vaste zinnen",
             opdracht="Schrijf de Franse zin voluit, met accenten.",
             oefeningen=[
                 ("rij", [("Hartelijk dank.", "Merci beaucoup."),
                          ("Sorry / het spijt me.", "Pardon. / Je suis désolé(e)."),
                          ("Graag gedaan.", "De rien. / Je vous en prie."),
                          ("Ik zou graag…", "Je voudrais…")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("rij", [("Kan je me helpen?", "Peux-tu m'aider ?"),
                          ("Alstublieft (beleefd).", "S'il vous plaît."),
                          ("Tot binnenkort.", "À bientôt.")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("kort", "Wat betekent 'Je vous prie de m'excuser' ?",
                  "ik verontschuldig me / mijn excuses", WW),
             ]),

        dict(kop="Tu of vous",
             opdracht="Denk aan wie de ontvanger is.",
             oefeningen=[
                 ("rij", [("aan een vriend", "tu"), ("aan een onbekende volwassene", "vous"),
                          ("aan je leerkracht", "vous"), ("aan je neefje van zes", "tu")],
                  "Tu of vous?", W),
                 ("waar", "Tegen een onbekende volwassene schrijf je in het Frans 'tu'.", False),
                 ("rij", [("aan een vriend", "Salut ! / Coucou !"),
                          ("aan een leerkracht", "Bonjour Madame, / Bonjour Monsieur,")],
                  "Welke aanhef past?", WW),
                 ("rij", [("aan een vriend", "À bientôt ! / Bises !"),
                          ("aan een leerkracht", "Cordialement, / Bien à vous,")],
                  "Welke slotgroet past?", WW),
             ]),

        dict(kop="Zelf schrijven",
             opdracht="Schrijf hieronder. Kleine fouten mogen, zolang je boodschap duidelijk is.",
             oefeningen=[
                 ("open", "Schrijf in het Frans een uitnodiging van drie zinnen voor je "
                          "verjaardagsfeest. Zet er zeker in: wat, wanneer, hoe laat en waar.",
                  "Bijvoorbeeld: « Salut ! Je fête mon anniversaire samedi 12 octobre à 15 h, "
                  "chez moi, rue des Tilleuls 8. Tu viens ? Réponds-moi avant jeudi ! »", 6),
                 ("open", "Schrijf in het Frans een korte mail (drie zinnen) aan een sportclub "
                          "om te vragen hoeveel het lidgeld kost. Gebruik 'vous'.",
                  "Bijvoorbeeld: « Bonjour Madame, Monsieur, Je m'appelle Lotte et je voudrais "
                  "m'inscrire à votre club de natation. Pourriez-vous me dire combien coûte la "
                  "cotisation ? Merci d'avance. Cordialement, Lotte »", 6),
                 ("open", "Je kan niet naar een afspraak komen. Schrijf één Franse zin waarin je "
                          "je verontschuldigt en de reden geeft.",
                  "Bijvoorbeeld: « Je suis désolée, je ne peux pas venir samedi parce que je "
                  "suis malade. »", 3),
             ]),

        dict(kop="Nakijken",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Wat doe je als laatste, vóór je je tekst indient?",
                  "Je leest hem helemaal na: staan alle gevraagde onderdelen erin, klopt de "
                  "lengte, en heb je 'tu' of 'vous' overal volgehouden?", 4),
                 ("waar", "Emoji's kunnen ook in een formele mail, zolang het er niet te veel "
                          "zijn.", False),
                 ("open", "Je zit vast omdat je een woord niet kent. Wat doe je?",
                  "Je omschrijft het met woorden die je wel kent, of je kiest een zin die "
                  "hetzelfde zegt met andere woorden. Je laat de zin niet half staan.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-foto-of-afbeelding-beschrijven-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Een foto of afbeelding beschrijven",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waar staat het",
             opdracht="Schrijf de Franse uitdrukking of de Nederlandse betekenis.",
             oefeningen=[
                 ("rij", [("à gauche", "links"), ("à droite", "rechts"),
                          ("au milieu", "in het midden"), ("au premier plan", "op de voorgrond"),
                          ("à l'arrière-plan", "op de achtergrond"), ("au fond", "achteraan")],
                  "Wat betekent dit?", WW),
                 ("waar", "'Au premier plan' betekent 'op de achtergrond'.", False),
                 ("rij", [("voor het huis", "devant la maison"),
                          ("achter de boom", "derrière l'arbre"),
                          ("op de tafel", "sur la table"), ("in de tuin", "dans le jardin")],
                  "Hoe schrijf je dat in het Frans?", WW),
             ]),

        dict(kop="Il y a",
             opdracht="Schrijf hele zinnen.",
             oefeningen=[
                 ("rij", [("Er is een hond.", "Il y a un chien."),
                          ("Er zijn twee kinderen.", "Il y a deux enfants."),
                          ("Ik zie een kerk.", "Je vois une église."),
                          ("Op de foto zie je een markt.", "Sur la photo, il y a un marché.")],
                  "Schrijf de Franse zin.", WW),
                 ("open", "Waarom is 'il y a' zo handig als je een foto beschrijft?",
                  "Het werkt voor enkelvoud én meervoud, en je hebt er geen ander werkwoord voor "
                  "nodig. Met die ene uitdrukking kan je alles benoemen wat je ziet.", 4),
             ]),

        dict(kop="Mensen en sfeer",
             opdracht="Let op het verschil tussen wat je ziet en wat je denkt.",
             oefeningen=[
                 ("rij", [("Ils sont contents.", "ze zijn blij"),
                          ("Elle a l'air triste.", "ze lijkt verdrietig"),
                          ("Elle a les yeux bleus.", "ze heeft blauwe ogen"),
                          ("Il porte un manteau rouge.", "hij draagt een rode jas"),
                          ("Ils sont en train de préparer le repas.",
                           "ze zijn de maaltijd aan het klaarmaken")],
                  "Wat betekent dit?", WW),
                 ("waar", "'Elle a l'air triste' betekent 'ze is boos'.", False),
                 ("rij", [("Je pense que…", "ik denk dat…"),
                          ("Il me semble que…", "het lijkt me dat…"),
                          ("On dirait que…", "het lijkt alsof…")],
                  "Wat betekent deze voorzichtige uitdrukking?", WW),
                 ("open", "Waarom zet je er beter geen dingen bij die je niet op de foto ziet?",
                  "Dan beschrijf je niet meer de foto maar je eigen verhaal. Wat je vermoedt, "
                  "zeg je voorzichtig met 'je pense que' of 'on dirait que'.", 4),
             ]),

        dict(kop="Zelf beschrijven",
             opdracht="Denk aan de volgorde: eerst het geheel, dan de details, dan je mening.",
             oefeningen=[
                 ("open", "Beschrijf in vier Franse zinnen een foto van een klas tijdens de les. "
                          "Zeg wat je in het algemeen ziet, wat er links en rechts staat, wat de "
                          "mensen doen, en wat je ervan vindt.",
                  "Bijvoorbeeld: « Sur la photo, il y a une classe avec une vingtaine d'élèves. "
                  "À gauche, on voit le tableau et le professeur. À droite, les élèves écrivent "
                  "dans leur cahier. Je pense qu'ils travaillent bien, parce que tout le monde "
                  "est concentré. »", 7),
                 ("open", "Je hebt maar een beperkte lengte gekregen. Wat laat je als eerste "
                          "vallen?",
                  "De kleine details en de herhalingen. Wat je zeker houdt, is het algemene "
                  "beeld, de plaats van de belangrijkste dingen, en één zin met je mening en de "
                  "reden erbij.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-mensen-familie-gevoelens-en-gezondheid-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Woordenschat: mensen, familie, gevoelens en gezondheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="La famille",
             opdracht="Schrijf het Franse woord mét het lidwoord.",
             oefeningen=[
                 ("rij", [("de moeder", "la mère"), ("de broer", "le frère"),
                          ("de zus", "la sœur"), ("de ouders", "les parents"),
                          ("de grootvader", "le grand-père"), ("de neef (zoon van je oom)", "le cousin")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("rij", [("ma belle-mère", "mijn schoonmoeder of stiefmoeder"),
                          ("un neveu", "een neef (zoon van je broer of zus)"),
                          ("une tante", "een tante")],
                  "Wat betekent dit?", WW),
             ]),

        dict(kop="Zich voorstellen",
             opdracht="Schrijf hele zinnen, met accenten.",
             oefeningen=[
                 ("rij", [("Ik heet Lotte.", "Je m'appelle Lotte."),
                          ("Ik ben veertien jaar.", "J'ai quatorze ans."),
                          ("Ik ben Belg.", "Je suis belge."),
                          ("Ik woon in Hasselt.", "J'habite à Hasselt.")],
                  "Schrijf de Franse zin.", WW),
                 ("waar", "In het Frans zeg je je leeftijd met 'être': 'je suis douze ans'.",
                  False),
                 ("open", "Leg uit waarom 'J'ai quatorze ans' klopt en 'Je suis quatorze ans' "
                          "niet.",
                  "Het Frans gebruikt voor leeftijd het werkwoord 'avoir' (hebben), letterlijk "
                  "'ik heb veertien jaren'. Het Nederlands gebruikt 'zijn', en die twee mag je "
                  "niet door elkaar halen.", 4),
             ]),

        dict(kop="Les sentiments",
             opdracht="Let op: sommige gevoelens gebruiken 'être', andere 'avoir'.",
             oefeningen=[
                 ("rij", [("Je suis content.", "ik ben blij"), ("J'ai peur.", "ik ben bang"),
                          ("Je suis inquiet.", "ik ben ongerust"),
                          ("J'ai faim.", "ik heb honger"),
                          ("Je me sens mieux.", "ik voel me beter")],
                  "Wat betekent dit?", WW),
                 ("rij", [("ik ben moe", "Je suis fatigué(e)."),
                          ("ik heb dorst", "J'ai soif."),
                          ("ik ben verdrietig", "Je suis triste.")],
                  "Schrijf de Franse zin.", WW),
             ]),

        dict(kop="Chez le médecin",
             opdracht="Denk aan 'avoir mal à' voor pijn.",
             oefeningen=[
                 ("rij", [("le bras", "de arm"), ("la tête", "het hoofd"),
                          ("les yeux", "de ogen"), ("les cheveux", "het haar"),
                          ("le ventre", "de buik"), ("la gorge", "de keel")],
                  "Wat betekent dit?", WW),
                 ("rij", [("ik heb hoofdpijn", "J'ai mal à la tête."),
                          ("ik heb buikpijn", "J'ai mal au ventre."),
                          ("ik heb keelpijn", "J'ai mal à la gorge."),
                          ("ik ben ziek", "Je suis malade.")],
                  "Schrijf de Franse zin.", WW),
                 ("open", "Waarom staat er 'au ventre' en niet 'à le ventre'?",
                  "'À + le' trekt in het Frans altijd samen tot 'au'. Bij een vrouwelijk woord "
                  "blijft het 'à la' (à la tête).", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-eten-wonen-kleding-en-dagelijkse-dingen-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Woordenschat: eten, wonen, kleding en dagelijkse dingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="La nourriture",
             opdracht="Schrijf het Franse woord mét het lidwoord.",
             oefeningen=[
                 ("rij", [("het brood", "le pain"), ("het water", "l'eau"),
                          ("een appel", "une pomme"), ("de melk", "le lait"),
                          ("de kaas", "le fromage")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("rij", [("le petit déjeuner", "het ontbijt"), ("le déjeuner", "het middagmaal"),
                          ("le dîner", "het avondmaal")],
                  "Wat betekent dit?", WW),
                 ("waar", "'Le déjeuner' is in Frankrijk het ontbijt.", False),
             ]),

        dict(kop="La maison",
             opdracht="Schrijf het Franse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("la chambre", "de slaapkamer"), ("la cuisine", "de keuken"),
                          ("la salle de bains", "de badkamer"),
                          ("la salle de séjour", "de woonkamer"), ("le jardin", "de tuin")],
                  "Wat betekent dit?", WW),
                 ("rij", [("de tafel", "la table"), ("de stoel", "la chaise"),
                          ("het bed", "le lit"), ("de koelkast", "le frigo")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("rij", [("en bois", "van hout"), ("en verre", "van glas"),
                          ("rond", "rond"), ("carré", "vierkant")],
                  "Wat betekent dit?", WW),
             ]),

        dict(kop="Les vêtements et les couleurs",
             opdracht="Let op waar de kleur staat.",
             oefeningen=[
                 ("rij", [("un manteau", "een jas"), ("une robe", "een jurk"),
                          ("les chaussures", "de schoenen"), ("un pantalon", "een broek")],
                  "Wat betekent dit?", WW),
                 ("rij", [("rood", "rouge"), ("blauw", "bleu"), ("groen", "vert"),
                          ("zwart", "noir")],
                  "Hoe schrijf je die kleur in het Frans?"),
                 ("open", "Schrijf in het Frans: 'zij draagt een blauwe jurk'. Let op de plaats "
                          "van de kleur.",
                  "« Elle porte une robe bleue. » De kleur staat achter het naamwoord, en ze "
                  "krijgt een -e omdat 'robe' vrouwelijk is.", 3),
                 ("waar", "In het Frans staat de kleur meestal achter het naamwoord.", True),
             ]),

        dict(kop="Faire les courses",
             opdracht="Schrijf hele zinnen waar dat gevraagd wordt.",
             oefeningen=[
                 ("rij", [("Ça coûte combien ?", "hoeveel kost dat?"),
                          ("Je fais les courses.", "ik doe boodschappen"),
                          ("Faire la cuisine", "koken"),
                          ("C'est délicieux.", "dat is heerlijk")],
                  "Wat betekent dit?", WW),
                 ("open", "Schrijf in het Frans: 'Ik zou graag een stokbrood willen, "
                          "alstublieft.'",
                  "« Je voudrais une baguette, s'il vous plaît. »", 3),
                 ("rij", [("la boulangerie", "de bakkerij"), ("le supermarché", "de supermarkt"),
                          ("un portefeuille", "een portefeuille"),
                          ("un porte-monnaie", "een portemonnee")],
                  "Wat betekent dit?", WW),
                 ("open", "'Porte-monnaie' bestaat uit twee woorden die je al kent. Leg uit hoe "
                          "je de betekenis kan raden.",
                  "'Porter' is dragen en 'la monnaie' is het kleingeld. Samen: iets waarin je je "
                  "geld draagt, dus een portemonnee. Samenstellingen herkennen scheelt veel "
                  "opzoekwerk.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-school-beroepen-sport-en-vrije-tijd-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Woordenschat: school, beroepen, sport en vrije tijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Instructietaal",
             opdracht="Dit zijn de woorden waarmee de examenvragen zelf geschreven zijn.",
             oefeningen=[
                 ("rij", [("Cochez la bonne réponse.", "kruis het juiste antwoord aan"),
                          ("Complétez la phrase.", "vul de zin aan"),
                          ("Reliez.", "verbind met elkaar"),
                          ("Justifiez votre réponse.", "verantwoord je antwoord"),
                          ("Vrai ou faux ?", "waar of niet waar?"),
                          ("Répondez en français.", "antwoord in het Frans")],
                  "Wat moet je doen?", WW),
                 ("waar", "'Reliez' betekent dat je iets moet doorstrepen.", False),
                 ("open", "Waarom is instructietaal zo belangrijk op het examen?",
                  "Je kan de leerstof kennen en toch punten verliezen omdat je de opdracht "
                  "verkeerd begrepen hebt. Wie 'justifiez' niet kent, geeft enkel het antwoord "
                  "en vergeet de uitleg.", 4),
             ]),

        dict(kop="L'école",
             opdracht="Schrijf het Franse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("l'école", "de school"), ("un élève", "een leerling"),
                          ("les devoirs", "het huiswerk"), ("un emploi du temps", "een uurrooster"),
                          ("la note", "het cijfer / de nota"), ("une matière", "een vak")],
                  "Wat betekent dit?", WW),
                 ("rij", [("een boek", "un livre"), ("een schrift", "un cahier"),
                          ("de leerkracht", "le professeur")],
                  "Hoe schrijf je dat in het Frans?", WW),
             ]),

        dict(kop="Les métiers",
             opdracht="Let op de vrouwelijke vorm waar die bestaat.",
             oefeningen=[
                 ("rij", [("un métier", "een beroep"), ("une infirmière", "een verpleegkundige"),
                          ("un boulanger", "een bakker"), ("un vendeur", "een verkoper"),
                          ("un médecin", "een dokter")],
                  "Wat betekent dit?", WW),
                 ("kort", "Wat betekent 'Il travaille dans un bureau' ?",
                  "hij werkt in een kantoor", WW),
             ]),

        dict(kop="Le sport et le temps libre",
             opdracht="Let op 'jouer à' en 'jouer de'.",
             oefeningen=[
                 ("rij", [("la natation", "het zwemmen"), ("l'entraînement", "de training"),
                          ("gagner", "winnen"), ("perdre", "verliezen"),
                          ("un spectacle", "een voorstelling")],
                  "Wat betekent dit?", WW),
                 ("rij", [("Je joue ___ football.", "au"), ("Je joue ___ guitare.", "de la")],
                  "Vul aan: 'jouer à' bij een sport, 'jouer de' bij een instrument.", W),
                 ("waar", "Bij een muziekinstrument gebruik je 'jouer à': 'jouer à la guitare'.",
                  False),
                 ("rij", [("télécharger", "downloaden"), ("un ordinateur", "een computer"),
                          ("envoyer un message", "een bericht sturen"),
                          ("un réseau social", "een sociaal netwerk")],
                  "Wat betekent dit?", WW),
                 ("open", "Schrijf in het Frans: 'Wat is je favoriete hobby?' en geef zelf een "
                          "antwoord van één zin.",
                  "« Quel est ton passe-temps préféré ? » Bijvoorbeeld: « Je fais du basket "
                  "deux fois par semaine. »", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-getallen-tijd-weer-reizen-en-landen-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Woordenschat: getallen, tijd, weer, reizen en landen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Les nombres",
             opdracht="Schrijf het cijfer of het woord.",
             oefeningen=[
                 ("rij", [("quinze", "15"), ("soixante-dix", "70"), ("quatre-vingts", "80"),
                          ("quatre-vingt-dix-sept", "97"), ("cent", "100")],
                  "Welk getal is dit?"),
                 ("rij", [("21", "vingt et un"), ("60", "soixante"), ("75", "soixante-quinze"),
                          ("90", "quatre-vingt-dix")],
                  "Schrijf dit getal voluit in het Frans.", WW),
                 ("rij", [("premier", "de eerste"), ("troisième", "de derde"),
                          ("dernier", "de laatste")],
                  "Wat betekent dit rangtelwoord?", WW),
             ]),

        dict(kop="Le temps qui passe",
             opdracht="Let op: 'le temps' betekent zowel het weer als de tijd.",
             oefeningen=[
                 ("rij", [("lundi", "maandag"), ("mercredi", "woensdag"),
                          ("samedi", "zaterdag"), ("juillet", "juli"), ("l'été", "de zomer")],
                  "Wat betekent dit?", WW),
                 ("rij", [("Il est huit heures et quart.", "kwart over acht"),
                          ("Il est sept heures moins le quart.", "kwart voor zeven"),
                          ("Il est huit heures et demie.", "halfnegen"),
                          ("Il est midi.", "het is twaalf uur 's middags")],
                  "Hoe laat is het?", WW),
                 ("open", "Waarom is 'huit heures et demie' halfnegen en niet halfacht?",
                  "Het Frans telt vanaf het uur dat geweest is: acht uur en een half. Het "
                  "Nederlands telt naar het volgende uur toe: half negen.", 4),
                 ("rij", [("aujourd'hui", "vandaag"), ("demain", "morgen"),
                          ("hier", "gisteren")],
                  "Wat betekent dit?", WW),
             ]),

        dict(kop="Le temps qu'il fait",
             opdracht="Over het weer zeg je 'il fait' of 'il y a'.",
             oefeningen=[
                 ("rij", [("Il fait froid.", "het is koud"), ("Il fait beau.", "het is mooi weer"),
                          ("Il y a du soleil.", "de zon schijnt"),
                          ("Il pleut.", "het regent")],
                  "Wat betekent dit?", WW),
                 ("waar", "Over het weer zeg je in het Frans 'il est froid'.", False),
                 ("kort", "Schrijf in het Frans: 'Wat voor weer is het?'",
                  "Quel temps fait-il ?", WW),
             ]),

        dict(kop="Voyager",
             opdracht="Let op 'à', 'en' en 'de' bij landen en steden.",
             oefeningen=[
                 ("rij", [("les vacances", "de vakantie"), ("un aller-retour", "een heen-en-terugticket"),
                          ("le train", "de trein"), ("la gare", "het station")],
                  "Wat betekent dit?", WW),
                 ("rij", [("Ik ga naar Parijs.", "Je vais à Paris."),
                          ("Ik ga naar Frankrijk.", "Je vais en France."),
                          ("Ik kom uit België.", "Je viens de Belgique.")],
                  "Schrijf de Franse zin.", WW),
                 ("open", "Waarom staat er 'à Paris' maar 'en France'?",
                  "Bij een stad gebruik je 'à'. Bij een vrouwelijk land gebruik je 'en'. "
                  "(Bij een mannelijk land wordt het 'au': au Portugal.)", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grammatica-lidwoorden-naamwoorden-en-voornaamwoorden-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Grammatica: lidwoorden, naamwoorden en voornaamwoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Les articles",
             opdracht="Bepaald, onbepaald of deelaanduidend?",
             oefeningen=[
                 ("rij", [("le, la, les", "bepaald (défini)"),
                          ("un, une, des", "onbepaald (indéfini)"),
                          ("du, de la, des", "deelaanduidend (partitif)")],
                  "Welke soort lidwoorden zijn dit?", WW),
                 ("rij", [("___ table (de tafel)", "la"), ("___ livre (het boek)", "le"),
                          ("___ école (de school)", "l'"), ("___ maison (een huis)", "une")],
                  "Vul het lidwoord in.", W),
                 ("rij", [("à + le", "au"), ("à + les", "aux"), ("de + le", "du"),
                          ("de + les", "des")],
                  "Wat wordt dit samen?", W),
                 ("waar", "De -s van een Frans meervoud hoor je altijd duidelijk.", False),
             ]),

        dict(kop="Na een ontkenning",
             opdracht="Na 'ne … pas' wordt het lidwoord 'de'.",
             oefeningen=[
                 ("rij", [("Je n'ai pas ___ frère.", "de"), ("Je ne bois pas ___ lait.", "de"),
                          ("Il n'y a pas ___ pain.", "de")],
                  "Vul aan.", W),
                 ("open", "Schrijf deze zin ontkennend: 'Je mange une pomme.'",
                  "« Je ne mange pas de pomme. » Let op: 'une' wordt 'de' na de ontkenning.", 3),
             ]),

        dict(kop="Les adjectifs",
             opdracht="Let op de plaats én op de uitgang.",
             oefeningen=[
                 ("rij", [("une voiture ___ (rood)", "rouge"), ("une robe ___ (groen)", "verte"),
                          ("les ___ maisons (mooi)", "belles"),
                          ("un ___ garçon (klein)", "petit")],
                  "Vul de juiste vorm in.", WW),
                 ("open", "Waar staat het bijvoeglijk naamwoord meestal in het Frans, en welke "
                          "zijn de uitzonderingen?",
                  "Meestal achter het naamwoord (une voiture rouge). Een korte, veelgebruikte "
                  "groep staat ervoor: beau, bon, grand, petit, jeune, vieux, joli, nouveau.", 5),
                 ("rij", [("groter dan", "plus grand que"), ("de grootste", "le plus grand"),
                          ("minder groot dan", "moins grand que")],
                  "Hoe schrijf je dat in het Frans?", WW),
                 ("waar", "'Meilleur' is de vergrotende trap van 'mauvais'.", False),
             ]),

        dict(kop="Les pronoms",
             opdracht="Let op waar het voornaamwoord in de zin komt.",
             oefeningen=[
                 ("rij", [("Je vois <b>Marie</b>.", "Je la vois."),
                          ("Je parle <b>à Paul</b>.", "Je lui parle."),
                          ("Je mange <b>la pomme</b>.", "Je la mange.")],
                  "Schrijf de zin opnieuw en vervang het vette deel door een voornaamwoord.", WW),
                 ("waar", "Een persoonlijk voornaamwoord als voorwerp staat in het Frans vóór "
                          "het werkwoord.", True),
                 ("rij", [("Je ___ lave les mains.", "me"),
                          ("Elle ___ lève à sept heures.", "se"),
                          ("Nous ___ promenons.", "nous")],
                  "Vul het wederkerend voornaamwoord in.", W),
                 ("open", "Waarom moet je weten of een Frans woord mannelijk of vrouwelijk is?",
                  "Het lidwoord, het bijvoeglijk naamwoord en soms het voornaamwoord passen zich "
                  "eraan aan. Kies je het verkeerde geslacht, dan sleept de fout door de hele "
                  "zin.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grammatica-werkwoorden-tijden-en-zinsbouw-spark"] = dict(
    vak="Frans", niveau=SPARK, titel="Grammatica: werkwoorden, tijden en zinsbouw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Le présent",
             opdracht="Vervoeg in de tegenwoordige tijd.",
             oefeningen=[
                 ("tabel", ["werkwoord", "je / j'", "nous", "ils"],
                  [["parler", None, None, None], ["être", None, None, None],
                   ["avoir", None, None, None]],
                  "parler: je parle · nous parlons · ils parlent — "
                  "être: je suis · nous sommes · ils sont — "
                  "avoir: j'ai · nous avons · ils ont"),
                 ("rij", [("je (aller)", "je vais"), ("tu (faire)", "tu fais"),
                          ("elle (venir)", "elle vient")],
                  "Vervoeg in het présent.", WW),
                 ("waar", "'Aller' eindigt op -er, dus je vervoegt het net zoals 'parler'.",
                  False),
             ]),

        dict(kop="Infinitief, persoonsvorm of deelwoord",
             opdracht="Ze klinken hetzelfde, maar ze zijn het niet.",
             oefeningen=[
                 ("rij", [("aller", "infinitief"), ("allez", "persoonsvorm (vous)"),
                          ("allé", "voltooid deelwoord"), ("parlé", "voltooid deelwoord"),
                          ("parler", "infinitief")],
                  "Infinitief, persoonsvorm of voltooid deelwoord?", WW),
                 ("open", "Waarom staat dit onderscheid in de vakfiche, denk je?",
                  "Omdat -er, -ez en -é in het Frans hetzelfde klinken. Wie ze niet uit elkaar "
                  "houdt, schrijft 'j'ai aller' of 'vous parlé'. Je hoort het verschil niet, je "
                  "moet het weten.", 5),
             ]),

        dict(kop="Verleden en toekomst",
             opdracht="Let op het hulpwerkwoord: avoir of être.",
             oefeningen=[
                 ("rij", [("ik heb gegeten", "j'ai mangé"), ("ik ben gegaan", "je suis allé(e)"),
                          ("ik ga eten (straks)", "je vais manger"),
                          ("ik heb net gegeten", "je viens de manger")],
                  "Schrijf de Franse vorm.", WW),
                 ("kort", "Welk hulpwerkwoord hoort bij 'aller' in de passé composé?",
                  "être", W),
                 ("open", "Leg het verschil uit tussen 'je vais manger' en 'je viens de manger'.",
                  "'Je vais manger' is de nabije toekomst: ik ga zo meteen eten. 'Je viens de "
                  "manger' is het nabije verleden: ik heb net gegeten.", 4),
             ]),

        dict(kop="Zinsbouw",
             opdracht="Let op de plaats van 'ne … pas'.",
             oefeningen=[
                 ("rij", [("Je mange.", "Je ne mange pas."),
                          ("Il travaille ici.", "Il ne travaille pas ici."),
                          ("Nous sommes prêts.", "Nous ne sommes pas prêts.")],
                  "Maak deze zin ontkennend.", WW),
                 ("rij", [("Ferme la porte !", "gebiedende wijs"),
                          ("Quelle belle journée !", "uitroepend"),
                          ("Est-ce que tu viens ?", "vragend"),
                          ("Il pleut aujourd'hui.", "mededelend")],
                  "Welke zinssoort is dit?", WW),
                 ("open", "Geef twee manieren om in het Frans een vraag te stellen, met een "
                          "voorbeeld bij elke manier.",
                  "Met 'est-ce que' vooraan: « Est-ce que tu viens ? » Of door de omkering van "
                  "onderwerp en werkwoord: « Viens-tu ? » In spreektaal kan ook de gewone "
                  "zinsvolgorde met een vraagteken: « Tu viens ? »", 5),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)

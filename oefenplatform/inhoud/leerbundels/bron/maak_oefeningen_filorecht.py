# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij filosofie en recht 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus dezelfde pdf hangt bij allebei. Twintig bundels,
dezelfde twintig sleutels als in `maak_filorecht.py`, met `oefenbundel-` ervoor.

De oefeningen zijn met opzet ándere vragen dan die op het scherm. Dit vak
bestaat voor zijn filosofische helft uit posities die je moet kunnen onderscheiden
en voor zijn juridische helft uit begrippen die op elkaar lijken. Daarom zijn de
oefeningen daarop gebouwd: een stelling bij de juiste denker of de juiste
rechtbank zetten, een schema aanvullen, en in je eigen woorden zeggen waarom twee
begrippen niet hetzelfde zijn. Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/filosofie-en-recht.json`.

Dezelfde waarschuwing als bij de vragen en de leerbundels: de fiche noemt een
veertigtal filosofen. **Zet er geen citaat, geen boektitel en geen experiment bij
dat de fiche niet vermeldt.** Een verzonnen citaat in de mond van een echte
auteur leest als een feit, en dat is hier de gevaarlijkste fout die je kan maken.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Filosofie en recht"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "130px"
WW = "200px"
WL = "260px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een stelling: zeg niet alleen welke denker of welk begrip het is, maar ook waaraan je het ziet.",
    "Lees bij twee posities die op elkaar lijken eerst nog eens wat ze onderscheidt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-de-eigenheid-van-de-filosofie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De eigenheid van de filosofie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Feitenvraag of filosofische vraag",
             opdracht="Schrijf bij elke vraag of het een feitenvraag of een filosofische vraag is.",
             oefeningen=[
                 ("rij", [("Hoeveel jongeren gaan naar het hoger onderwijs?", "feitenvraag"),
                          ("Heeft iedereen recht op hoger onderwijs?", "filosofische vraag"),
                          ("Hoeveel mensen geven aan ooit gelogen te hebben?", "feitenvraag"),
                          ("Mag je liegen om iemand te sparen?", "filosofische vraag")],
                  "Feitenvraag of filosofische vraag?", WW),
                 ("rij", [("Wat is een rechtvaardige straf?", "filosofische vraag"),
                          ("Hoeveel mensen zitten er in de gevangenis?", "feitenvraag"),
                          ("Wat maakt iemand een mens?", "filosofische vraag"),
                          ("Bij welke temperatuur kookt water?", "feitenvraag")],
                  "Feitenvraag of filosofische vraag?", WW),
                 ("open", "Leg in je eigen woorden uit waarom een filosoof zijn vraag niet met een "
                          "experiment kan beslechten.",
                  "Omdat zijn vraag niet over meetbare feiten gaat maar over begrippen en waarden. Je "
                  "kan meten hoeveel mensen iets rechtvaardig vinden, maar niet of het rechtvaardig "
                  "is. Daarom werkt hij met argumenten en met begrippen die hij scherp maakt.", 5),
             ]),
        dict(kop="Natuurwetenschap, menswetenschap of filosofie",
             opdracht="Zet elk vak of elke vraag in de juiste groep.",
             oefeningen=[
                 ("rij", [("de sterrenkunde", "natuurwetenschap"),
                          ("de sociologie", "menswetenschap"),
                          ("wat kan ik weten?", "filosofie"),
                          ("de biologie", "natuurwetenschap")],
                  "In welke groep hoort dit?", WW),
                 ("rij", [("de psychologie", "menswetenschap"),
                          ("wat is een mens?", "filosofie"),
                          ("de scheikunde", "natuurwetenschap"),
                          ("de geschiedenis", "menswetenschap")],
                  "In welke groep hoort dit?", WW),
                 ("kort", "Wat betekent het woord filosofie letterlijk?", "liefde voor de wijsheid", WL),
                 ("waar", "Een filosoof bezit de wijsheid; daarom heet zijn vak zo.", False),
             ]),
        dict(kop="Van mythologie naar filosofie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["", "Mythologie", "Natuurfilosofie"],
                  [["de verklaring", None, None],
                   ["de houding", None, None],
                   ["te toetsen?", None, None]],
                  "mythologie: de wil van de goden, het verhaal aanvaarden, niet te toetsen; "
                  "natuurfilosofie: oorzaken in de natuur zelf, de verklaring bevragen, "
                  "te toetsen met argumenten en later met onderzoek", W),
                 ("open", "Waarom kan je een mythisch verhaal nergens op nakijken?",
                  "Omdat het alles verklaart. Wat er ook gebeurt, het past in het verhaal, en dus is "
                  "er geen uitkomst die het verhaal zou tegenspreken. Dezelfde zwakte komt bij Popper "
                  "terug onder de naam niet te weerleggen.", 5),
                 ("kies", "Waarmee begint de westerse filosofie volgens de fiche?",
                  ["met de mythologie van de Grieken", "met de natuurfilosofie",
                   "met de ethiek van Aristoteles", "met de Verlichting"], 1),
                 ("open", "Filosofie begint bij verwondering. Leg uit wat dat betekent en geef er zelf "
                          "een voorbeeld bij.",
                  "Verwondering is stilstaan bij iets dat voor iedereen vanzelfsprekend is, en er een "
                  "vraag over stellen. Bijvoorbeeld: waarom vinden wij het eerlijk dat iedereen één "
                  "stem heeft? Wie zich nergens meer over verwondert, stelt ook geen vragen meer.", 5),
                 ("kort", "Hoeveel filosofische domeinen noemt deze fiche, naast de argumentatieleer?",
                  "drie", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bronnen-van-kennis-rationalisme-en-empirisme-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bronnen van kennis, rationalisme en empirisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vijf bronnen van kennis",
             opdracht="Schrijf bij elk voorbeeld welke bron van kennis aan het werk is.",
             oefeningen=[
                 ("rij", [("je ziet dat de stok in het water geknikt lijkt", "de zintuigen"),
                          ("je weet nog wat je gisteren at", "het geheugen"),
                          ("je weet dat je nu kwaad bent", "de introspectie"),
                          ("je weet dat de aarde om de zon draait", "verhalen van anderen")],
                  "Welke bron?", WW),
                 ("rij", [("alle mensen zijn sterfelijk, dus ook jij", "de afleiding"),
                          ("je hoort een auto aankomen", "de zintuigen"),
                          ("je leest in een boek wie de eerste koning was", "verhalen van anderen"),
                          ("je merkt dat je zenuwachtig bent", "de introspectie")],
                  "Welke bron?", WW),
                 ("open", "Waarom is de vraag welke bron betrouwbaar is geen schoolse maar een "
                          "dagelijkse vraag?",
                  "Omdat verreweg het meeste van wat je weet uit verhalen van anderen komt, en dat kan "
                  "je zelf niet nakijken. Dat de aarde om de zon draait, heb je niet zelf vastgesteld. "
                  "Elke dag beslis je dus wie of wat je gelooft.", 5),
             ]),
        dict(kop="Rationalisme en empirisme",
             opdracht="Vul het schema aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["", "Rationalisme", "Empirisme"],
                  [["bron van kennis", None, None],
                   ["naam of namen", None, None],
                   ["redeneert met", None, None],
                   ["zekerheid", None, None]],
                  "rationalisme: de rede, Descartes, deductie van algemeen naar bijzonder, zeker als "
                  "de premissen kloppen; empirisme: de ervaring, Locke en Hume, inductie van bijzonder "
                  "naar algemeen, nooit helemaal zeker", W),
                 ("kort", "Hoe heet de werkwijze waarmee Descartes aan alles twijfelt?",
                  "de methodische twijfel", WL),
                 ("rij", [("alle mensen zijn sterfelijk, jij bent een mens, dus jij bent sterfelijk",
                           "deductie"),
                          ("elke zwaan die ik zag was wit, dus alle zwanen zijn wit", "inductie"),
                          ("alle metalen geleiden, koper is een metaal, dus koper geleidt", "deductie"),
                          ("de bus was drie keer te laat, dus hij is altijd te laat", "inductie")],
                  "Deductie of inductie?", WW),
                 ("open", "Waarom geeft inductie nooit volle zekerheid? Gebruik de zwaan in je "
                          "antwoord.",
                  "Omdat je van een aantal waarnemingen naar een algemene regel springt, en je nooit "
                  "alles gezien hebt. Eén zwarte zwaan volstaat om de regel alle zwanen zijn wit om te "
                  "gooien. Hoeveel witte zwanen je ook telt, de volgende kan de regel breken.", 5),
                 ("waar", "Rationalisme en empirisme sluiten elkaar uit; een onderzoeker moet kiezen.",
                  False),
             ]),
        dict(kop="De grot en de AUB-methode",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Vertel de grotallegorie van Plato in drie of vier zinnen, en zeg waar het "
                          "verhaal om gaat.",
                  "Mensen zitten vastgeketend in een grot met hun rug naar de uitgang en zien enkel "
                  "schaduwen op de wand, die ze voor de werkelijkheid houden. Komt er één los en gaat "
                  "hij naar buiten, dan verblindt het licht hem eerst, en vertelt hij het binnen, dan "
                  "geloven de anderen hem niet. Waar het om gaat: wat je dagelijks waarneemt, hoeft "
                  "niet de hele werkelijkheid te zijn, en wie iets anders komt vertellen, botst op "
                  "weerstand.", 7),
                 ("tabel", ["Letter", "Waar ze voor staat", "Hoe je begint"],
                  [["A", None, None], ["U", None, None], ["B", None, None]],
                  "A = argument (mijn argument is dat ...), U = uitleg (want ..., dit is goed want "
                  "...), B = bijvoorbeeld (stel je voor ...)", W),
                 ("kort", "Hoe noemt men een argument waarin je naar iemand met gezag verwijst?",
                  "een gezagsargument", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-natuurfilosofie-naar-wetenschap-falsificatie-en-demarcatie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Van natuurfilosofie naar wetenschap: falsificatie en demarcatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Verificatie en falsificatie",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent het woord demarcatie?", "afbakening", WL),
                 ("open", "Wat is het demarcatieprobleem?",
                  "De vraag waar je de grens trekt tussen wetenschap en wat zich als wetenschap "
                  "voordoet. Dus: waaraan zie je of een uitspraak wetenschappelijk is?", 4),
                 ("tabel", ["", "Verificatie", "Falsificatie"],
                  [["de vraag", None, None],
                   ["het probleem of de kracht", None, None]],
                  "verificatie vraagt: kan ik dit bevestigen, en haar probleem is dat bevestiging "
                  "altijd toevallig kan zijn; falsificatie vraagt: wat zou dit weerleggen, en haar "
                  "kracht is dat één tegenvoorbeeld beslissend is", W),
                 ("kort", "Welke filosoof koos falsificatie als maatstaf?", "Popper", WL),
                 ("open", "Waarom verklaart een theorie die niets uitsluit volgens Popper niets?",
                  "Omdat er geen enkele waarneming is die haar zou tegenspreken. Wie op elke mogelijke "
                  "uitkomst zegt dat ze zijn theorie bevestigt, heeft geen sterke theorie maar een "
                  "onweerlegbare, en dus leert ze je niets over de wereld.", 5),
                 ("waar", "Een wetenschappelijke theorie die weerlegd werd, was dus eigenlijk "
                          "pseudowetenschap.", False),
             ]),
        dict(kop="Pseudowetenschap herkennen",
             opdracht="Schrijf bij elk voorbeeld welk kenmerk van pseudowetenschap je ziet.",
             oefeningen=[
                 ("rij", [("de voorspelling is zo ruim dat ze altijd uitkomt", "vage voorspellingen"),
                          ("de grondlegger heeft het gezegd, dus het klopt", "beroep op gezag"),
                          ("bij een tegenvoorbeeld wordt de theorie wat bijgedraaid", "uitvluchten"),
                          ("de methode is nergens gepubliceerd", "geen controle")],
                  "Welk kenmerk?", WW),
                 ("open", "Pseudowetenschap is niet hetzelfde als ongelijk hebben. Leg uit waar het "
                          "verschil dan wel zit.",
                  "Het verschil zit in de toetsbaarheid, niet in de uitkomst. Een wetenschappelijke "
                  "theorie die weerlegd wordt, was wel degelijk wetenschappelijk, want ze sloot iets "
                  "uit. Pseudowetenschap sluit niets uit en kan dus ook niet weerlegd worden.", 5),
                 ("kies", "Wat kenmerkt de wetenschap volgens de bundel?",
                  ["dat ze gelijk heeft", "dat ze een verzameling feiten is",
                   "dat ze zichzelf kan verbeteren", "dat ze nooit van mening verandert"], 2),
             ]),
        dict(kop="Namen en lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("keek, ordende en deelde in: planten, dieren, staatsvormen", "Aristoteles"),
                          ("eiste waarneming en experiment in plaats van het gezag van oude boeken",
                           "Bacon"),
                          ("koos falsificatie als maatstaf voor wetenschap", "Popper")],
                  "Welke naam?", WW),
                 ("tabel", ["Stap", "Wat je doet"],
                  [["1. oriënterend lezen", None],
                   ["2. grondig lezen", None],
                   ["3. reflectie", None]],
                  "1: de tekst in zijn geheel lezen, letten op indeling, signaalwoorden en "
                  "kernbegrippen, en per alinea een kernzin aanduiden; 2: herlezen, woorden opzoeken, "
                  "zinnen ontleden, verbanden aanduiden en samenvatten; 3: tegenvoorbeelden zoeken en "
                  "je eigen kritiek formuleren", WL),
                 ("open", "Wat is de toets van stap 2: waaraan weet je dat je klaar bent met grondig "
                          "lezen?",
                  "Je moet daarna met je eigen woorden aan een vriend kunnen uitleggen hoe de auteur "
                  "zijn stelling verdedigt. Lukt dat niet, dan ben je nog niet klaar met lezen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-lichaam-en-geest-monisme-en-dualisme-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Lichaam en geest: monisme en dualisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Monist of dualist",
             opdracht="Schrijf bij elke filosoof of hij monist of dualist is, en waaraan je dat ziet.",
             oefeningen=[
                 ("rij", [("Parmenides", "monist"),
                          ("Plato", "dualist"),
                          ("Descartes", "dualist"),
                          ("Spinoza", "monist")],
                  "Monist of dualist?", WW),
                 ("kort", "Van welk woord komt monisme, en wat betekent dat?", "monos, één", WL),
                 ("kort", "Van welk woord komt dualisme, en wat betekent dat?", "duo, twee", WL),
                 ("open", "Aristoteles wordt niet bij de dualisten gerekend. Leg uit waarom niet, met "
                          "zijn visie op de ziel.",
                  "Bij hem is de ziel de vorm van het lichaam: je kan ze onderscheiden maar niet "
                  "scheiden. Sterft het lichaam, dan is er geen ziel die ergens verder reist. Daarom "
                  "leunt hij naar het monisme.", 5),
             ]),
        dict(kop="De stellingen bij de juiste naam",
             opdracht="Schrijf bij elke stelling welke filosoof ze verdedigt.",
             oefeningen=[
                 ("rij", [("het zijnde is één en onveranderlijk", "Parmenides"),
                          ("de ziel staat los van het lichaam en is onsterfelijk", "Plato"),
                          ("de ziel is de vorm van het lichaam", "Aristoteles"),
                          ("denken en uitgebreidheid zijn twee werkelijkheden", "Descartes")],
                  "Welke filosoof?", WW),
                 ("kort", "Wie maakt van denken en uitgebreidheid twee kanten van één werkelijkheid?",
                  "Spinoza", WL),
                 ("open", "Wat is het interactieprobleem, en bij wie komt het op?",
                  "Het komt op bij Descartes. Als het denken en het stoffelijke twee heel verschillende "
                  "werkelijkheden zijn, hoe kan een gedachte dan je benen in beweging zetten? Er moet "
                  "iets oversteken tussen twee werelden, en het is niet duidelijk hoe.", 5),
                 ("open", "Hoe lost Spinoza dat probleem op?",
                  "Door de knip ongedaan te maken. Bij hem is er één werkelijkheid, met denken en "
                  "uitgebreidheid als twee kanten daarvan. Moet er niets meer oversteken, dan is er "
                  "ook geen brug nodig.", 4),
             ]),
        dict(kop="Westers en niet-westers, en vandaag",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "In veel niet-westerse tradities is de scheiding tussen lichaam en geest "
                          "minder scherp of ontbreekt ze.", True),
                 ("open", "Wat zegt het boeddhisme over het zelf, en waarom staat dat ver van de "
                          "westerse ziel?",
                  "Dat er geen vast, blijvend zelf is: wat jij bent, is een geheel dat voortdurend "
                  "verandert. Dat staat ver van een ziel die het lichaam overleeft, want daar is het "
                  "zelf juist het blijvende deel.", 5),
                 ("open", "Hersenonderzoek toont samenhang tussen brein en ervaring. Waarom beslecht "
                          "dat het debat niet?",
                  "Omdat samenhang aantonen iets anders is dan aantonen dat geest en brein hetzelfde "
                  "zijn. Die laatste stap is een filosofische stap en geen meting, en daarom blijft "
                  "het debat open.", 5),
                 ("kies", "Waarom is het nuttig de westerse indeling met een niet-westerse te "
                          "vergelijken?",
                  ["om te bewijzen dat de westerse indeling fout is",
                   "om te zien dat de westerse indeling zelf een keuze is",
                   "omdat niet-westerse tradities ouder zijn",
                   "omdat het op het examen staat"], 1),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-cultuur-en-natuur-mens-dier-en-machine-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Cultuur en natuur: mens, dier en machine",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Exclusief menselijk",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent exclusief menselijk?",
                  "uitsluitend bij de mens", WL),
                 ("waar", "Exclusief menselijk betekent dat de mens het vaker of sterker heeft dan "
                          "andere wezens.", False),
                 ("tabel", ["Kandidaat", "Argument ervoor", "Argument ertegen"],
                  [["emoties", None, None], ["de rede", None, None]],
                  "emoties: mensen benoemen hun gevoelens en praten erover, maar ook dieren vertonen "
                  "angst, woede en wat op rouw lijkt; de rede: mensen kunnen over hun eigen denken "
                  "nadenken, maar ook dieren leren, gebruiken werktuigen en werken samen", W),
                 ("open", "Waarom is de vraag wat exclusief menselijk is een filosofische en geen "
                          "biologische vraag?",
                  "Vaststellen wat dieren kunnen, is onderzoek. Maar beslissen welk van die verschillen "
                  "echt telt om de mens mens te noemen, gaat over begrippen en waarden, en dat kan "
                  "geen experiment beslechten.", 5),
                 ("open", "Waarom houdt de tegenstelling natuur tegenover cultuur bij de mens nergens "
                          "helemaal stand?",
                  "Omdat ons lichaam grenzen vastlegt en cultuur daarbinnen van alles mogelijk maakt. "
                  "Eten, slapen en taal zijn allemaal tegelijk natuurlijk en cultureel, dus valt wat "
                  "natuur is en wat cultuur niet netjes uit elkaar te halen.", 5),
             ]),
        dict(kop="Drie benaderingen van emoties",
             opdracht="Schrijf bij elk voorbeeld welke benadering je ziet.",
             oefeningen=[
                 ("rij", [("je schrikt van een harde knal, waar je ook geboren bent", "naturalistisch"),
                          ("luid huilen op een begrafenis hoort er in het ene land bij en in het "
                           "andere niet", "cultureel en historisch"),
                          ("je was kwaad tot je hoorde dat het per ongeluk was", "cognitief")],
                  "Welke benadering?", WL),
                 ("open", "Waaraan herken je de cognitieve benadering het makkelijkst?",
                  "De gebeurtenis blijft dezelfde, je oordeel erover verandert, en de emotie verandert "
                  "mee. Het is dus je inschatting die de emotie draagt.", 4),
                 ("waar", "De drie benaderingen sluiten elkaar uit: één emotie hoort bij één "
                          "benadering.", False),
             ]),
        dict(kop="Mens, dier en machine",
             opdracht="Zet elke stelling bij de juiste denker.",
             oefeningen=[
                 ("rij", [("de mens is een dier dat over rede beschikt", "Aristoteles"),
                          ("een dier werkt als een machine; enkel de mens heeft een denkende geest",
                           "Descartes"),
                          ("de mens krijgt geen ereplaats boven de natuur", "Nietzsche"),
                          ("de mens is een machine; voor zijn denken is geen aparte ziel nodig",
                           "La Mettrie")],
                  "Welke denker?", WW),
                 ("kort", "Welke hedendaagse hersenonderzoeker zegt dat wat wij ons zelf noemen het "
                          "werk van onze hersenen is?", "Swaab", WL),
                 ("open", "Wat is het bezwaar tegen de visie van Descartes op dieren?",
                  "Het gaat over pijn. Als een dier niets ervaart, waarom gedraagt het zich dan precies "
                  "zoals een wezen dat pijn heeft? Dat gedrag is moeilijk te verklaren als er niets "
                  "achter zit.", 5),
                 ("open", "Waarom kiest de fiche bewustzijn als maatstaf bij mens en machine, en niet "
                          "wat een machine kan?",
                  "Omdat wat een machine kán voortdurend opschuift: rekenen, schaken, spreken. De vraag "
                  "die blijft, is of er iets is dat het is om die machine te zijn. Gedrag dat op "
                  "bewustzijn lijkt, bewijst nog geen bewustzijn.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vrijheid-en-determinisme-van-de-oudheid-tot-de-19de-eeuw-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vrijheid en determinisme van de oudheid tot de 19de eeuw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Lot, toeval of determinisme",
             opdracht="Schrijf bij elk voorbeeld welk van de drie je ziet.",
             oefeningen=[
                 ("rij", [("de voorspelling komt uit, hoe je ook vlucht", "lot"),
                          ("jij wint de lotto; niets had dat voor jou bestemd", "toeval"),
                          ("je keuze volgt uit oorzaken, zonder dat iemand het zo wilde",
                           "determinisme"),
                          ("je botst op een oude vriend in een vreemde stad", "toeval")],
                  "Lot, toeval of determinisme?", WW),
                 ("tabel", ["Woord", "Bedoeling?", "Lag het vast?"],
                  [["lot", None, None], ["toeval", None, None], ["determinisme", None, None]],
                  "lot: ja en ja; toeval: nee en nee; determinisme: niet noodzakelijk een bedoeling, "
                  "maar het lag wel vast", W),
                 ("open", "Van welk woord komt determinisme, en waarom past die herkomst?",
                  "Van determineren: vastleggen. Het past omdat het determinisme zegt dat alles wat "
                  "gebeurt vastligt door wat eraan voorafging. Het is kaler dan het lot, want er hoeft "
                  "geen bedoeling achter te zitten, en strenger dan toeval.", 5),
             ]),
        dict(kop="De oudheid",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "In de Griekse mythologie kunnen de goden het lot omkeren.", False),
                 ("open", "Wat is de wrange kern van het verhaal van Oedipus?",
                  "Wie zijn voorspelling probeert te ontlopen, vervult ze juist daardoor. De vlucht "
                  "voor het lot blijkt zelf een deel van het lot.", 4),
                 ("rij", [("alles bestaat uit atomen die volgens vaste wetten bewegen", "Democritus"),
                          ("de vrijheid zit in je houding, niet in de gebeurtenis", "de Stoïcijnen"),
                          ("de vrije wil en de voorzienigheid gaan samen", "Thomas van Aquino")],
                  "Welke naam?", WL),
                 ("open", "Leg het onderscheid van de Stoïcijnen uit, met een eigen voorbeeld.",
                  "Zij scheiden wat in je macht ligt van wat niet in je macht ligt. Dat de trein "
                  "uitvalt, ligt niet in jouw macht; wat je erover denkt en hoe je ermee omgaat, wel. "
                  "Daar leggen zij de vrijheid.", 5),
             ]),
        dict(kop="Van de middeleeuwen tot de 19de eeuw",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het wereldbeeld van de 17de eeuw waarin natuurwetten alles "
                          "vastleggen?", "mechanisch determinisme", WL),
                 ("open", "Welke vraag stelt dat mechanisch determinisme scherp over de mens?",
                  "Zit de mens ook in die machine? Zo ja, dan ligt ook zijn keuze vast. Zo nee, dan "
                  "moet je uitleggen waarom hij een uitzondering is op de natuurwetten.", 5),
                 ("rij", [("je kan doen wat je wil, maar je kan niet kiezen wát je wil",
                           "Schopenhauer"),
                          ("de vrije wil is een bedenksel om schuld toe te wijzen", "Nietzsche")],
                  "Welke filosoof?", WL),
                 ("open", "Waarom is deze vraag niet enkel schools? Gebruik het strafrecht in je "
                          "antwoord.",
                  "Ons strafrecht gaat ervan uit dat iemand anders had kunnen handelen. Een streng "
                  "determinisme maakt het begrip schuld dan moeilijk te verdedigen, en dus ook straffen "
                  "die bedoeld zijn om schuld te laten boeten.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vrijheid-en-determinisme-in-de-20ste-eeuw-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vrijheid en determinisme in de 20ste eeuw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vijf denkers, vijf posities",
             opdracht="Zet elke stelling bij de juiste denker.",
             oefeningen=[
                 ("rij", [("je situatie koos je niet; je leven op je nemen wel", "Heidegger"),
                          ("je bent gedoemd tot vrijheid; niet kiezen is ook kiezen", "Sartre"),
                          ("macht en normen vormen mee wat je wil", "Foucault"),
                          ("vrij ben je als je wil wat je wil willen", "Frankfurt")],
                  "Welke denker?", WW),
                 ("kort", "Wie vindt dat er geen vrije wil is en dat ons strafrecht dat moet "
                          "verwerken?", "Verplaetse", WL),
                 ("open", "Zet de vijf denkers op een rij van heel veel vrijheid naar heel weinig, en "
                          "leg je uiterste twee kort uit.",
                  "Sartre, Heidegger, Frankfurt, Foucault, Verplaetse. Bij Sartre is de vrijheid "
                  "volledig en onontkoombaar: je kan er niet aan ontsnappen. Bij Verplaetse is er geen "
                  "vrije wil, en dus ook geen schuld om te vergelden.", 6),
             ]),
        dict(kop="Heidegger en Sartre",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe noemt Heidegger het feit dat je je tijd, je lichaam en je afkomst niet "
                          "koos?", "geworpenheid", WL),
                 ("open", "Wat bedoelt Heidegger met een oneigenlijk bestaan? Zeg ook wat het níét is.",
                  "Leven zoals men nu eenmaal leeft, zonder er zelf voor in te staan. Het is niet "
                  "hetzelfde als liegen: het gaat over wegkijken, je leven laten lopen zoals het hoort "
                  "te lopen, met de gewoonte als stuurman.", 5),
                 ("open", "Leg uit wat Sartre bedoelt met de existentie gaat aan de essentie vooraf. "
                          "Gebruik het voorbeeld van een mes.",
                  "Er ligt geen vaste menselijke natuur klaar; je wordt wie je bent door te handelen. "
                  "Bij een mes is het omgekeerd: daarvan ligt het doel vast voordat het gemaakt wordt. "
                  "Bij een mens komt het bestaan eerst en het wat hij is daarna.", 5),
                 ("rij", [("ik moest wel, ik ben nu eenmaal zo", "kwade trouw"),
                          ("ik koos dit en draag de gevolgen", "geen kwade trouw"),
                          ("ik deed niets, dus ik koos niets", "kwade trouw")],
                  "Kwade trouw of niet, volgens Sartre?", WL),
                 ("waar", "Bij Sartre is vrijheid een gemak, want je kan altijd kiezen.", False),
             ]),
        dict(kop="Foucault, Frankfurt en Verplaetse",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe noemt Foucault het vormen van mensen door scholen, wetten en "
                          "gewoonten?", "disciplinering", WL),
                 ("open", "Wat is het punt van Foucault over macht, als er geen geweld bij komt?",
                  "Dat niemand je dwingt en je verlangen toch mee gevormd wordt door de wereld waarin "
                  "je bent opgegroeid. Een keuze die vrij lijkt, kan nog altijd een keuze zijn tussen "
                  "mogelijkheden die jou zijn aangereikt.", 5),
                 ("tabel", ["", "Eerste orde", "Tweede orde", "Vrij?"],
                  [["de ene", None, None, None], ["de andere", None, None, None]],
                  "de ene heeft een drang en wil die drang niet hebben: niet vrij, hij wordt "
                  "meegesleept; de andere heeft die drang en wil ze ook hebben: vrij, het verlangen is "
                  "het zijne", W),
                 ("open", "Waarom heet de positie van Frankfurt verzoenend?",
                  "Omdat vrijheid en een wereld vol oorzaken bij hem naast elkaar kunnen bestaan. Zijn "
                  "vraag is niet of je keuze zonder oorzaak was, maar of ze echt van jou is.", 4),
                 ("open", "Verplaetse zegt dat er geen vrije wil is. Welke maatregelen blijven dan toch "
                          "mogelijk, en welke komt onder druk?",
                  "Beschermen, behandelen en voorkomen blijven mogelijk, want die hebben geen schuld "
                  "nodig. Enkel vergelden heeft dat wel, en net dat komt onder druk.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ethiek-basisbegrippen-en-vier-benaderingen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ethiek: basisbegrippen en vier benaderingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waarde of norm",
             opdracht="Schrijf bij elk voorbeeld of het een waarde of een norm is.",
             oefeningen=[
                 ("rij", [("eerlijkheid", "waarde"),
                          ("je mag niet spieken", "norm"),
                          ("respect", "waarde"),
                          ("je laat iemand uitspreken", "norm")],
                  "Waarde of norm?", WW),
                 ("open", "Leg uit waarom dezelfde waarde in twee landen andere normen kan opleveren.",
                  "Omdat de waarde algemeen is en de norm concreet. Respect voor ouderen is overal een "
                  "waarde, maar hoe je dat hoort te laten zien, met een buiging, met een titel of met "
                  "een handdruk, verschilt van plaats tot plaats.", 5),
             ]),
        dict(kop="Universalisme en relativisme",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("er zijn morele regels die overal en voor iedereen gelden",
                           "moreel universalisme"),
                          ("wat goed is hangt af van wie het zegt of van welke groep",
                           "moreel relativisme"),
                          ("morele opvattingen horen bij een cultuur en zijn niet van buitenaf te "
                           "beoordelen", "cultuurrelativisme")],
                  "Welk standpunt?", WL),
                 ("open", "Wat is het bekendste bezwaar tegen het cultuurrelativisme?",
                  "Wie zegt dat je een cultuur niet van buitenaf mag beoordelen, haalt daarmee ook de "
                  "grond onder elke kritiek op onrecht weg. Je kan dan over niets meer zeggen dat het "
                  "fout is, ook niet over je eigen samenleving.", 5),
                 ("waar", "Een universalist moet ontkennen dat er culturele verschillen in moraal "
                          "bestaan.", False),
                 ("open", "Waarom hoort de vrije wil bij de basisbegrippen van de ethiek?",
                  "Omdat verwijten dat iemand anders had moeten handelen alleen zin heeft als hij "
                  "anders kón handelen. Zonder keuzevrijheid valt er niemand nog verantwoordelijk te "
                  "stellen.", 5),
             ]),
        dict(kop="Dilemma's, benaderingen en Hume",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Wat maakt een moreel dilemma pijnlijk?",
                  "Dat elke mogelijkheid iets van waarde kost en er geen schone uitweg is. Ook de beste "
                  "keuze laat iets achter dat je niet wou opgeven.", 4),
                 ("rij", [("een bevraging over wat mensen van orgaandonatie vinden",
                           "descriptieve ethiek"),
                          ("is orgaandonatie een plicht?", "normatieve ethiek")],
                  "Descriptief of normatief?", WL),
                 ("tabel", ["Richting", "Waar ze naar kijkt", "Haar vraag"],
                  [["gevolgenethiek", None, None], ["plichtethiek", None, None],
                   ["deugdethiek", None, None], ["zorgethiek", None, None]],
                  "gevolgenethiek: de uitkomst, wat brengt dit teweeg; plichtethiek: de regel, welke "
                  "regel bindt mij hier; deugdethiek: de persoon, wat voor mens word ik hiermee; "
                  "zorgethiek: de relatie, wat heeft deze mens van mij nodig", W),
                 ("rij", [("mensen eten al duizenden jaren vlees", "een beschrijving"),
                          ("wij zouden minder vlees moeten eten", "een voorschrift"),
                          ("mensen eten al duizenden jaren vlees, dus mogen we dat blijven doen",
                           "de sprong die Hume aanwijst")],
                  "Beschrijving, voorschrift of de sprong?", WL),
                 ("open", "Welk woordje doet bij de is-ought sprong het werk, en waarom is dat een "
                          "probleem?",
                  "Het woordje dus. Dat iets zo is of zo was, zegt op zich niet dat het zo mag blijven. "
                  "Tussen een beschrijving en een voorschrift zit een stap die je apart moet "
                  "verdedigen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-gevolgenethiek-en-plichtethiek-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Gevolgenethiek en plichtethiek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De gevolgenethiek",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Onder welke tweede naam is de gevolgenethiek bekend?",
                  "het utilitarisme", WL),
                 ("kort", "Van welk woord komt die naam, en wat betekent het?", "utilitas, nut", WL),
                 ("rij", [("streef naar het grootste geluk voor het grootste aantal", "Bentham"),
                          ("wie kan lijden telt mee, ook dieren", "Singer")],
                  "Welke filosoof?", WL),
                 ("kort", "Hoe noemt Singer het vooroordeel dat enkel de eigen soort meetelt?",
                  "soortisme", WL),
                 ("open", "De onpartijdigheid is de sterke en de koude kant van het utilitarisme. Leg "
                          "beide kanten uit.",
                  "Sterk: jouw geluk telt niet zwaarder omdat het het jouwe is, dus niemand wordt "
                  "voorgetrokken. Koud: een optelsom vertelt niet wie de rekening betaalt. Tien mensen "
                  "heel gelukkig en één diep ongelukkig geeft toch een positieve som.", 6),
                 ("open", "Noem de drie bezwaren tegen de gevolgenethiek.",
                  "Eén: de minderheid kan geofferd worden aan de som. Twee: je kent de gevolgen van je "
                  "daad vooraf niet volledig, want je moet de toekomst inschatten. Drie: het bezwaar "
                  "van Hume, dat de vaststelling dát mensen geluk zoeken nog geen norm oplevert dat "
                  "geluk de maatstaf móét zijn.", 6),
             ]),
        dict(kop="Kant",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent categorisch?", "onvoorwaardelijk", WL),
                 ("rij", [("lieg niet", "categorische imperatief"),
                          ("wil je slagen, dan moet je studeren", "hypothetische imperatief"),
                          ("hou je woord", "categorische imperatief"),
                          ("wil je gezond blijven, beweeg dan", "hypothetische imperatief")],
                  "Categorisch of hypothetisch?", WW),
                 ("open", "Schrijf de categorische imperatief op zoals de bundel ze formuleert.",
                  "Handel enkel volgens een regel waarvan je kan willen dat ze voor allen geldt.", 3),
                 ("open", "Wat zegt de tweede formulering van Kant, en wat volgt daaruit?",
                  "Behandel een mens nooit louter als een middel voor jouw doel. Daaruit volgt dat je "
                  "iemand niet mag gebruiken, ook niet voor een mooi doel: een mens is geen "
                  "instrument.", 5),
                 ("open", "Noem de twee bekende bezwaren tegen Kant.",
                  "Eén: hij is zo streng dat hij ook in uitzonderlijke gevallen geen leugen toelaat, "
                  "zelfs niet tegen iemand die je vriend komt zoeken om hem kwaad te doen. Twee: zijn "
                  "imperatief zegt welke vorm een regel moet hebben, maar niet wat je concreet moet "
                  "doen.", 6),
                 ("waar", "Kant is een moreel relativist, want zijn plicht hangt van de situatie af.",
                  False),
             ]),
        dict(kop="Levinas, en de twee naast elkaar",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Waar begint de moraal bij Levinas, en waarin verschilt dat van Kant?",
                  "Bij het gelaat van de ander dat je aanspreekt en je verantwoordelijk maakt. Kant "
                  "vertrekt van een algemene regel die de rede toetst, Levinas van de ontmoeting met "
                  "deze ene mens. Onvoorwaardelijk zijn ze beide, en bij beide weegt de uitkomst niet "
                  "mee.", 6),
                 ("tabel", ["", "Gevolgenethiek", "Plichtethiek"],
                  [["beslissend", None, None],
                   ["belofte nakomen", None, None],
                   ["zwak punt", None, None]],
                  "gevolgenethiek: de uitkomst, een belofte nakomen enkel als het goed uitvalt, en de "
                  "minderheid kan geofferd worden; plichtethiek: de regel of de plicht, een belofte "
                  "nakomen ook als het nadelig uitvalt, en ze kan onbuigzaam worden", W),
                 ("open", "Twee ethische richtingen kunnen bij hetzelfde geval tot een tegengesteld "
                          "besluit komen. Waarom is dat niet enkel lastig maar ook nuttig?",
                  "Lastig, omdat er dan geen eenduidig antwoord is: dat is wat een moreel dilemma zo "
                  "moeilijk maakt. Nuttig, omdat je door beide kanten uit te werken ziet wat er precies "
                  "op het spel staat en wat elke keuze kost.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-deugdethiek-en-zorgethiek-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Deugdethiek en zorgethiek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vier kardinale deugden",
             opdracht="Vul het schema aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Deugd", "Wat ze is", "Het midden tussen"],
                  [["verstandigheid", None, None], ["rechtvaardigheid", None, None],
                   ["moed", None, None], ["matigheid", None, None]],
                  "verstandigheid: weten wat hier het juiste is, tussen onbezonnenheid en "
                  "besluiteloosheid; rechtvaardigheid: ieder geven wat hem toekomt, tussen voortrekken "
                  "en benadelen; moed: doen wat nodig is ondanks je angst, tussen lafheid en overmoed; "
                  "matigheid: maat houden in genot, tussen onthouding en overdaad", W),
                 ("kort", "Van welk woord komt kardinaal, en wat betekent het?", "cardo, spil", WL),
                 ("waar", "Een deugd is het gemiddelde van wat mensen doen.", False),
                 ("open", "Een deugd is het midden tussen een tekort en een overdaad. Waarom is dat "
                          "midden niet altijd op dezelfde plaats?",
                  "Omdat het juiste midden van de situatie afhangt. Wat in de ene situatie moedig is, "
                  "is in de andere overmoed. Daarom hoort er verstandigheid bij: weten wat hier het "
                  "juiste is.", 5),
                 ("open", "Hoe krijg je een deugd volgens Aristoteles?",
                  "Niet cadeau: je bouwt ze op door ze te oefenen tot ze een gewoonte wordt, zoals je "
                  "een instrument leert bespelen.", 4),
             ]),
        dict(kop="Nussbaum, Hume en Foot",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel capaciteiten noemt Nussbaum?", "tien", W),
                 ("open", "Waarom zijn de capaciteiten van Nussbaum mogelijkheden en geen prestaties?",
                  "Omdat het gaat over wat elke mens moet kunnen om een menswaardig leven te leiden, "
                  "niet over wat hij ervan maakt. Of je ook speelt of meebeslist, is jouw zaak; dat je "
                  "het zou kunnen, is wat telt.", 5),
                 ("rij", [("medelijden", "natuurlijke deugd"),
                          ("rechtvaardigheid", "artificiële deugd"),
                          ("vriendelijkheid", "natuurlijke deugd"),
                          ("je woord houden", "artificiële deugd")],
                  "Natuurlijke of artificiële deugd, volgens Hume?", WW),
                 ("open", "Noem de drie kenmerken waaraan Foot een deugd herkent.",
                  "Ze is goed voor de mens en zijn omgeving, ze zit in je wil en niet enkel in je "
                  "kunnen, en ze vangt een zwakke plek in onze neigingen op.", 5),
                 ("open", "Dat derde kenmerk verklaart waarom de lijst van deugden eruitziet zoals ze "
                          "eruitziet. Leg dat uit met moed en matigheid.",
                  "Moed is nodig omdat wij angst kennen, matigheid omdat wij verleid worden. Waar geen "
                  "bekoring is, is geen deugd nodig: er hoort geen deugd bij iets dat ons nooit "
                  "moeilijk valt.", 5),
             ]),
        dict(kop="De zorgethiek",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Van welk mensbeeld vertrekt de zorgethiek, en waarin verschilt dat van de "
                          "plicht- en de gevolgenethiek?",
                  "Van mensen als kwetsbaar en van elkaar afhankelijk: niemand komt alleen door het "
                  "leven. De plicht- en de gevolgenethiek kijken van buitenaf en onpartijdig, met een "
                  "regel voor allen of een som over allen. De zorgethiek begint bij deze mens in deze "
                  "relatie.", 6),
                 ("open", "Waarom liggen de wortels van de zorgethiek in het feminisme?",
                  "Omdat de ethiek lang vertrok van een onafhankelijke, redelijke burger. Wie "
                  "afhankelijk was en wie voor hem zorgde, kwam in dat beeld niet voor, want zorg gold "
                  "als vrouwenwerk.", 5),
                 ("open", "Wat was volgens Gilligan de fout in bestaand onderzoek naar morele "
                          "ontwikkeling?",
                  "Niet dat meisjes lager uitkwamen, maar dat de maatstaf maar één stem in beeld had. "
                  "Naast de stem van de rechtvaardigheid staat een stem van de zorg.", 5),
                 ("tabel", ["Fase", "Wat er gebeurt", "Morele kwaliteit"],
                  [["zorgen om", None, None], ["zorgen voor", None, None],
                   ["zorg verlenen", None, None], ["zorg ontvangen", None, None]],
                  "zorgen om: je merkt dat er nood is, betrokkenheid; zorgen voor: je neemt er "
                  "verantwoordelijkheid voor op, verantwoordelijkheid; zorg verlenen: je doet het werk, "
                  "bekwaamheid; zorg ontvangen: je kijkt hoe het aankomt, wederkerigheid", W),
                 ("rij", [("je ziet de nood maar doet er niets mee", "blijft steken bij de eerste fase"),
                          ("je bedoelt het goed maar je kan het niet", "strandt bij de derde fase"),
                          ("je kijkt niet na hoe je zorg aankomt", "mist de vierde fase")],
                  "Welke fase ontbreekt hier?", WL),
                 ("open", "Wat hebben de deugdethiek en de zorgethiek met elkaar gemeen?",
                  "Beide kijken minder naar de losse daad dan de gevolgen- en de plichtethiek. De "
                  "deugdethiek kijkt naar de persoon die handelt, de zorgethiek naar de relatie waarin "
                  "hij staat.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ethiek-en-geluk-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ethiek en geluk",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De oudheid",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Met welk Grieks woord noemt Aristoteles het geluk?", "eudaimonia", WL),
                 ("open", "Waarom beoordeel je eudaimonia over een heel leven en niet over een dag?",
                  "Omdat het geen stemming is maar een manier van leven volgens de deugd. Eén goede "
                  "dag maakt geen geslaagd leven, net zoals één zwaluw de lente niet maakt.", 5),
                 ("waar", "Epicurus zocht het geluk in zoveel genot als mogelijk.", False),
                 ("open", "Wat is bij Epicurus geluk, en welke raad volgt eruit?",
                  "De rust die overblijft als pijn en onrust weg zijn: geen pijn, geen angst, geen "
                  "honger, en goede vrienden. Zijn raad is je verlangens te beperken tot wat je echt "
                  "nodig hebt, want wie weinig nodig heeft, mist ook minder.", 5),
                 ("rij", [("gemoedsrust door te scheiden wat in je macht ligt", "het stoïcisme"),
                          ("loslaten van verlangen en van wat niet blijft", "oosterse wijsheden"),
                          ("rust, geen pijn en goede vrienden", "Epicurus"),
                          ("bloeien volgens de deugd", "Aristoteles")],
                  "Welke visie?", WW),
                 ("open", "Epicurus, het stoïcisme en de oosterse wijsheden gaan dezelfde richting uit. "
                          "Welke?",
                  "Minder aan de haak van het geluk dat van buiten moet komen. Ze leggen het geluk niet "
                  "bij wat je krijgt of bereikt, maar bij hoe je met je verlangens omgaat. De weg "
                  "verschilt, de richting niet.", 5),
             ]),
        dict(kop="Is geluk de maatstaf?",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["", "Kant", "Bentham"],
                  [["geluk als maatstaf?", None, None],
                   ["waarom", None, None],
                   ["je plicht doe je", None, None]],
                  "Kant: nee, want wat iemand gelukkig maakt verschilt van mens tot mens terwijl een "
                  "moreel gebod voor allen moet gelden, en je plicht doe je om de plicht; Bentham: ja, "
                  "genot min pijn voor zoveel mensen als mogelijk, en je plicht doe je om wat ze "
                  "opbrengt", W),
                 ("open", "Kant sluit geluk niet helemaal uit. Wat zegt hij er dan wel over?",
                  "Dat wie zijn plicht doet geluk verdient. Maar de twee vallen niet samen, en een daad "
                  "die je stelt omdat ze jou gelukkig maakt, is bij hem niet moreel.", 5),
                 ("open", "Wat is het bezwaar tegen geluk als optelsom?",
                  "Een getal zegt niet wie van de betrokkenen de prijs betaalt. De som verbergt de "
                  "verdeling, en een hoge som kan dus op heel ongelijk verdeeld geluk rusten.", 5),
             ]),
        dict(kop="Schopenhauer, Levinas en De Wachter",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("geluk is hoogstens het tijdelijk ontbreken van gemis", "Schopenhauer"),
                          ("het geluk ligt in de verantwoordelijkheid voor de ander", "Levinas"),
                          ("verdriet en tegenslag horen bij een leven en mogen er zijn",
                           "De Wachter")],
                  "Welke denker?", WL),
                 ("open", "Waarom heet de visie van Schopenhauer pessimistisch?",
                  "Omdat de wil ons van verlangen naar verlangen drijft: onvervuld verlangen doet pijn "
                  "en vervuld verlangen laat verveling achter. Er blijft dan weinig anders dan het "
                  "tijdelijk ontbreken van gemis.", 5),
                 ("open", "Waarop richt de kritiek van De Wachter zich, en waar zoekt hij het geluk "
                          "wel?",
                  "Op de druk om altijd gelukkig te moeten zijn, want juist die druk maakt mensen "
                  "ongelukkig. Hij zoekt het geluk in verbondenheid met anderen en in kleine dingen.", 5),
                 ("open", "Met welke twee vragen krijg je de hele rij visies uit elkaar?",
                  "Zoekt deze filosoof het geluk binnen de mens of bij de ander? En is geluk bij hem "
                  "wel of niet de maatstaf van de moraal?", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-argumentatieleer-redeneervormen-en-drogredenen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumentatieleer: redeneervormen en drogredenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Antecedens en consequens",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["Deel", "Naam", "Betekenis van het woord"],
                  [["het regent", None, None], ["de straat is nat", None, None]],
                  "het regent is het antecedens, wat voorafgaat; de straat is nat is het consequens, "
                  "wat volgt", W),
                 ("rij", [("je studeert, dus je slaagt", "geldig"),
                          ("je bent geslaagd, dus je hebt gestudeerd", "ongeldig"),
                          ("je studeerde niet, dus je slaagt niet", "ongeldig"),
                          ("je bent niet geslaagd, dus je studeerde niet", "geldig")],
                  "Geldig of ongeldig?", WW),
                 ("kort", "Hoe heet de geldige vorm waarin je het antecedens bevestigt?",
                  "modus ponens", WL),
                 ("kort", "Hoe heet de geldige vorm waarin je het consequens ontkent?",
                  "modus tollens", WL),
                 ("open", "Waarom werkt de bevestiging van het consequens niet? Gebruik de natte "
                          "straat.",
                  "Omdat de straat ook nat kan zijn van een schoonmaakwagen. Uit het gevolg volgt de "
                  "voorwaarde niet: er kunnen andere oorzaken zijn die hetzelfde gevolg geven.", 5),
                 ("open", "Waarom werkt de ontkenning van het antecedens niet?",
                  "Omdat het gevolg er nog altijd kan zijn zonder die voorwaarde. Het regent niet, en "
                  "toch kan de straat nat zijn.", 4),
             ]),
        dict(kop="Geldig is niet waar",
             opdracht="Antwoord met ja of nee en leg kort uit.",
             oefeningen=[
                 ("rij", [("kan een geldige redenering een onwaar besluit hebben?",
                           "ja, als een premisse onwaar is"),
                          ("maakt een waar besluit een redenering geldig?", "nee, dat kan toeval zijn"),
                          ("heeft een ongeldige redenering altijd een onwaar besluit?",
                           "nee, ze bewijst het alleen niet")],
                  "Ja of nee, en waarom?", WL),
                 ("open", "Waar gaat geldigheid over, als het niet over de inhoud gaat?",
                  "Over de vorm: als de premissen waar zijn, moet het besluit ook waar zijn. Of die "
                  "premissen werkelijk waar zijn, is een andere vraag.", 4),
                 ("open", "In het voorbeeld als je studeert, slaag je zit een onware premisse. Welke, "
                          "en wat betekent dat voor de modus tollens erop?",
                  "Dat studeren altijd tot slagen leidt, is niet waar. De modus tollens blijft geldig, "
                  "want de vorm klopt, maar het besluit staat of valt met die eerste regel.", 5),
             ]),
        dict(kop="Drogredenen",
             opdracht="Schrijf bij elk voorbeeld welke drogreden je ziet.",
             oefeningen=[
                 ("rij", [("jouw voorstel is niets waard, want jij hebt nooit gestudeerd",
                           "op de persoon"),
                          ("je wil minder vlees eten? dus je wil geen boerderijen meer",
                           "de stroman"),
                          ("of je bent voor dit plan, of je bent tegen vooruitgang",
                           "de valse tweedeling"),
                          ("laat je dit toe, dan sta je straks alles toe", "het hellend vlak")],
                  "Welke drogreden?", WL),
                 ("rij", [("iedereen doet het, dus het mag", "het beroep op de massa"),
                          ("een bekende acteur zegt dat dit middel werkt",
                           "de onbevoegde autoriteit"),
                          ("ik ken er twee die dat doen, dus ze doen het allemaal",
                           "de overhaaste generalisatie"),
                          ("het is natuurlijk, dus het is goed", "het beroep op de natuur")],
                  "Welke drogreden?", WL),
                 ("open", "Waarom is het beroep op de natuur het is-ought probleem van Hume in "
                          "zakformaat?",
                  "Omdat het uit wat is besluit wat zou moeten: dit komt in de natuur voor, dus het is "
                  "goed. Gif is ook natuurlijk, en dus volgt uit natuurlijk zijn nog niets over goed "
                  "zijn.", 5),
                 ("open", "Hoe weerleg je een drogreden?",
                  "Niet door harder te spreken, maar door te benoemen wat er aan de stap zelf mankeert: "
                  "waarom volgt het besluit niet uit wat er gezegd is? Let op: het besluit kan om een "
                  "andere reden best juist zijn.", 5),
                 ("waar", "Wie een drogreden gebruikt, doet dat altijd met opzet.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-democratische-rechtsstaat-en-haar-principes-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De democratische rechtsstaat en haar principes",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rechtsstaat en democratie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat is een rechtsstaat, in één zin?",
                  "een staat waarin ook de overheid aan het recht gebonden is", WL),
                 ("open", "Waarom zijn rechtsstaat en democratie niet hetzelfde? Geef bij elk een "
                          "voorbeeld van een land dat het ene heeft en het andere niet.",
                  "Een staat kan netjes zijn wetten volgen zonder verkiezingen te houden: dan is er "
                  "rechtsstatelijkheid zonder democratie. En een staat kan verkiezingen houden en zich "
                  "daarna niet aan het recht houden: een land waar de winnaar rechters kan afzetten die "
                  "hem tegenspreken, heeft wel verkiezingen maar geen rechtsstaat.", 6),
                 ("kort", "Uit welke periode komen de waarden waarop onze rechtsstaat rust?",
                  "de Verlichting", WL),
                 ("open", "Noem die waarden, en zeg waar je ze terugvindt.",
                  "Vrijheid, gelijkheid en de waardigheid van elke mens. Je vindt ze terug aan het "
                  "begin van de grondwet en in de mensenrechten.", 4),
             ]),
        dict(kop="De vijf principes",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Principe", "Wat het zegt"],
                  [["het meerderheidsprincipe", None],
                   ["een constitutie of grondwet", None],
                   ["de scheiding der machten", None],
                   ["onafhankelijke en onpartijdige rechtspraak", None],
                   ["fundamentele rechten en vrijheden", None]],
                  "meerderheid: een beslissing geldt als de meerderheid ze steunt; grondwet: de "
                  "hoogste wet, die de macht afbakent; scheiding der machten: wetten maken, uitvoeren "
                  "en recht spreken liggen in verschillende handen; rechtspraak: de rechter krijgt geen "
                  "bevel en heeft geen band met de partijen; grondrechten: rechten die elke mens heeft "
                  "en die de overheid moet eerbiedigen", WL),
                 ("open", "De vijf principes dragen elkaar. Geef twee voorbeelden van wat er gebeurt "
                          "als er één wegvalt.",
                  "Grondrechten zonder onafhankelijke rechter zijn tekst op papier, want je kan ze "
                  "nergens laten gelden. En een grondwet zonder scheiding der machten geeft niemand "
                  "tegengewicht, want dan maakt en controleert dezelfde macht de regels.", 6),
                 ("open", "Wat is de keerzijde van het meerderheidsprincipe, en wat vangt die op?",
                  "Dat een meerderheid een minderheid kan overstemmen. Daarom mag een meerderheid niet "
                  "alles beslissen: de grondrechten beschermen de minderheid tegen haar wil.", 5),
                 ("open", "Waarom is een grondwet moeilijker te wijzigen dan een gewone wet?",
                  "Omdat ze de spelregels vastlegt waaraan de wetgever zelf gebonden is. Een "
                  "meerderheid van vandaag mag die spelregels niet in haar eigen voordeel omgooien.", 5),
                 ("waar", "De grondwet bevat alle wetten van een land.", False),
             ]),
        dict(kop="Grondrechten, onafhankelijk en onpartijdig",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Mogen grondrechten beperkt worden? Noem de drie voorwaarden.",
                  "Ja, maar binnen grenzen: de beperking moet in de wet staan, ze moet een doel dienen, "
                  "en ze moet door een rechter te toetsen zijn.", 5),
                 ("open", "Waarom weegt het recht op een eerlijk proces zo zwaar?",
                  "Omdat je zonder dat recht al je andere rechten niet kan verdedigen. Een recht dat je "
                  "nergens kan laten gelden, is geen recht.", 4),
                 ("rij", [("een minister zegt een rechter wat hij moet beslissen",
                           "de onafhankelijkheid"),
                          ("een rechter moet oordelen over een zaak van zijn eigen zus",
                           "de onpartijdigheid"),
                          ("een partij in het parlement dreigt met een tuchtstraf voor een vonnis",
                           "de onafhankelijkheid")],
                  "Welke eis komt hier in het gedrang?", WL),
                 ("open", "Een onafhankelijke rechter is wél aan de wet gebonden. Wat betekent zijn "
                          "onafhankelijkheid dan precies?",
                  "Dat niemand hem kan voorschrijven hoe hij die wet toepast. Hij oordeelt binnen de "
                  "wet, maar zonder bevel van de regering of het parlement.", 5),
                 ("open", "Waarom trekt een rechter zich bij twijfel over zijn onpartijdigheid terug, "
                          "ook als hij zeker weet dat hij eerlijk zou oordelen?",
                  "Omdat de schijn al genoeg is. Een proces moet niet alleen eerlijk zijn maar ook "
                  "eerlijk lijken, anders vertrouwt niemand de uitspraak nog.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-scheiding-der-machten-en-de-rechterlijke-macht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De scheiding der machten en de rechterlijke macht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Drie machten",
             opdracht="Vul het schema aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Macht", "Instelling", "Functie"],
                  [["de wetgevende macht", None, None],
                   ["de uitvoerende macht", None, None],
                   ["de rechterlijke macht", None, None]],
                  "wetgevende: de parlementen, de wetten maken en de regering controleren; "
                  "uitvoerende: de regeringen en hun administratie, de wetten uitvoeren en het land "
                  "besturen; rechterlijke: de hoven en de rechtbanken, de wet toepassen op een "
                  "concreet geval", W),
                 ("kort", "Met welke filosoof uit de 18de eeuw wordt de scheiding der machten "
                          "verbonden?", "Montesquieu", WL),
                 ("open", "Waarom is de scheiding der machten zo belangrijk? Geef het argument in één "
                          "of twee zinnen.",
                  "Omdat macht die zichzelf controleert, niets controleert. Zo kan niemand tegelijk de "
                  "regel maken, hem toepassen en over zijn eigen fouten oordelen.", 4),
                 ("waar", "Dat het bestuur door de scheiding der machten trager werkt, is een fout in "
                          "het ontwerp.", False),
                 ("open", "Het woord is scheiding, niet afzondering. Wat is het verschil?",
                  "De machten houden elkaar juist in het oog en werken op elkaar in; elkaar "
                  "controleren hoort bij het ontwerp. Afzondering zou betekenen dat ze niets met elkaar "
                  "te maken hebben, en dan zou er ook geen tegengewicht zijn.", 5),
                 ("kort", "Heeft België één parlement of meerdere?", "meerdere", W),
             ]),
        dict(kop="Controle en evenwicht",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("nagaan of een wet met de grondwet in overeenstemming is",
                           "het Grondwettelijk Hof"),
                          ("beslissingen van het bestuur nakijken en vernietigen", "de Raad van State"),
                          ("de regering ondervragen en over de begroting stemmen", "het parlement")],
                  "Wie doet dit?", WL),
                 ("open", "Wat is het sterkste controlemiddel van het parlement, en waarom?",
                  "De begroting. Zonder de steun van het parlement geraakt een regering niet aan haar "
                  "geld en niet aan haar wetten, en dan kan ze niets meer doen.", 5),
                 ("open", "Wat betekent controle en evenwicht, en wat betekent het niet?",
                  "Het betekent dat elke macht middelen heeft om de andere twee binnen hun grenzen te "
                  "houden, dus een wederzijdse rem. Het betekent niet dat de drie machten even groot "
                  "moeten zijn.", 5),
             ]),
        dict(kop="De rechterlijke macht beschermd",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Waarom worden rechters in België niet verkozen?",
                  "Omdat een rechter die stemmen moet halen, afhankelijk wordt van wat populair is. "
                  "Zijn benoeming loopt daarom via een onafhankelijke instelling die op bekwaamheid "
                  "selecteert.", 5),
                 ("open", "Waarom hoort de vaste benoeming bij de onafhankelijkheid?",
                  "Omdat wie niet afgezet kan worden, onbevangen tegen de macht in kan oordelen. Een "
                  "rechter die zijn plaats kan verliezen door een onwelkom vonnis, is geen "
                  "onafhankelijke rechter.", 5),
                 ("open", "Waarom moet een rechter zijn vonnis motiveren?",
                  "Zodat iedereen kan nagaan waarop zijn beslissing berust. Een gemotiveerd vonnis is "
                  "te controleren en in beroep aan te vechten, en dat hoort bij een eerlijk proces.", 5),
                 ("kort", "Wat organiseert de minister van Justitie wel, en wat beslist hij nooit?",
                  "de dienst, nooit het vonnis", WL),
                 ("rij", [("een minister zet een rechter onder druk over een vonnis", "schending"),
                          ("een parlement stemt een wet die één lopende rechtszaak beslecht",
                           "schending"),
                          ("een regering weigert een vonnis uit te voeren dat haar niet past",
                           "schending"),
                          ("het parlement stemt een nieuwe algemene wet", "geen schending")],
                  "Schending van de scheiding der machten?", WW),
                 ("open", "Waarom is een wet die één lopende rechtszaak beslecht een schending?",
                  "Omdat een wet algemeen moet zijn: ze geldt voor iedereen in dezelfde situatie. Wie "
                  "een wet maakt voor één zaak, spreekt in feite recht, en dat is het werk van de "
                  "rechter.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-functies-van-justitie-de-rechtspraak-en-de-deontologie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De functies van justitie, de rechtspraak en de deontologie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vijf functies van justitie",
             opdracht="Schrijf bij elk voorbeeld welke functie je ziet.",
             oefeningen=[
                 ("rij", [("iemand uit de buurt van zijn slachtoffer houden", "veiligheid"),
                          ("een vonnis over een huurgeschil", "conflictbeslechting"),
                          ("optreden na rellen", "ordehandhaving"),
                          ("een werkstraf opleggen", "bestraffing")],
                  "Welke functie?", WW),
                 ("kort", "Hoeveel functies van justitie noemt de fiche?", "vijf", W),
                 ("open", "Waarom is preventie het werk dat je niet ziet omdat het lukt?",
                  "Omdat dat de wet bestaat en overtredingen gevolgen hebben, al veel mensen tegenhoudt. "
                  "Wat niet gebeurt, valt niemand op, en toch is dat precies het resultaat.", 5),
                 ("open", "Bij welke tak van het recht hoort conflictbeslechting typisch, en waarom is "
                          "ze nodig?",
                  "Bij het burgerlijk recht. Zonder rechter zou een geschil blijven duren of met geweld "
                  "eindigen, want er is dan niemand die het met een beslissing kan afsluiten.", 5),
                 ("waar", "Bestraffing is de belangrijkste functie van justitie; de andere komen "
                          "erna.", False),
             ]),
        dict(kop="Vier principes van de rechtspraak",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["Principe", "Wat het betekent"],
                  [["het vermoeden van onschuld", None],
                   ["onafhankelijkheid en onpartijdigheid", None],
                   ["openbaarheid", None],
                   ["hoor en wederhoor", None]],
                  "vermoeden van onschuld: je bent onschuldig tot een rechter je schuld vaststelt, het "
                  "bewijs komt van wie vervolgt en twijfel valt in jouw voordeel uit; "
                  "onafhankelijkheid en onpartijdigheid: geen bevel van de andere machten en geen band "
                  "met de partijen; openbaarheid: een zitting en een uitspraak zijn in beginsel voor "
                  "iedereen toegankelijk; hoor en wederhoor: elke partij mag op de argumenten van de "
                  "andere antwoorden", WL),
                 ("open", "Wanneer kan een zitting met gesloten deuren doorgaan? Geef een voorbeeld.",
                  "Wanneer een zwaarder belang meespeelt, bijvoorbeeld het belang van een kind of de "
                  "privacy. De zittingen van de jeugdrechtbank zijn daarom niet openbaar.", 5),
                 ("open", "Waarom raakt trial by media aan het vermoeden van onschuld?",
                  "Omdat een krant die een verdachte al een dader noemt, een oordeel uitspreekt dat nog "
                  "niet gevallen is. De rechter heeft dan nog niets vastgesteld, en toch staat het "
                  "oordeel er al.", 5),
             ]),
        dict(kop="Deontologie, beroepsgeheim en melden",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["", "Wetgeving", "Deontologische code"],
                  [["komt van", None, None], ["geldt voor", None, None],
                   ["bij schending", None, None]],
                  "wetgeving: van de wetgever, voor iedereen, met een sanctie van de rechter; code: van "
                  "de beroepsgroep zelf, voor wie dat beroep uitoefent, met een sanctie van de "
                  "beroepsorde of de werkgever", W),
                 ("waar", "Een deontologische code komt in de plaats van de wet voor wie dat beroep "
                          "uitoefent.", False),
                 ("rij", [("wat iemand je in vertrouwen vertelt, mag je niet verder vertellen",
                           "het beroepsgeheim"),
                          ("terughoudend zijn over alles wat je op je werk verneemt",
                           "de discretieplicht"),
                          ("bij ernstig en dreigend gevaar moet je spreken", "de meldingsplicht")],
                  "Welk aspect?", WL),
                 ("open", "Wie beschermt het beroepsgeheim eigenlijk, en waarom?",
                  "Wie hulp zoekt, niet de hulpverlener. Zonder die zekerheid durft niemand nog iets te "
                  "vertellen, en dan bereikt de hulp de mensen niet meer die ze nodig hebben.", 5),
                 ("rij", [("een kind vertelt dat het thuis geslagen wordt en dat het vanavond opnieuw "
                           "dreigt te gebeuren", "de meldingsplicht"),
                          ("een medewerker vertelt op een feestje over een dossier zonder de naam te "
                           "noemen", "de discretieplicht")],
                  "Welke plicht speelt hier?", WL),
                 ("open", "Waarom is de discretieplicht geschonden als er geen naam valt?",
                  "Omdat details een mens herkenbaar maken, ook zonder naam. En wie dit hoort, weet "
                  "voortaan dat je over je cliënten praat, en dat ondermijnt het vertrouwen.", 5),
                 ("open", "Waarom is een deontologische code nooit een lijst met kant-en-klare "
                          "antwoorden?",
                  "Omdat plichten in één situatie tegen elkaar in kunnen gaan. Zwijgen en melden kunnen "
                  "in dezelfde casus beide opkomen, en dan vraagt het een afweging in plaats van een "
                  "regel.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-actuele-thema-s-binnen-recht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Actuele thema's binnen recht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het schema",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Activiteit", "Wat je doet"],
                  [["1. beschrijven", None], ["2. verklaren", None],
                   ["3. oplossingen evalueren", None]],
                  "beschrijven: de context schetsen (voor wie is het een probleem, waarom, waar, hoe "
                  "ontstaan) en standpunten vergelijken; verklaren: meerdere oorzaken inbrengen en die "
                  "ordenen per invalshoek; evalueren: oplossingen met hun perspectieven herkennen en "
                  "ook de ongewenste gevolgen benoemen", WL),
                 ("open", "Noem de vijf invalshoeken.",
                  "Economisch, sociaal, cultureel, politiek en juridisch.", 3),
                 ("open", "Wat betekent redeneren met bewijs in dit schema?",
                  "Meerdere bronnen inzetten en vergelijken, letten op betrouwbare en valide data, en "
                  "gegevens uit onderzoek gebruiken om je uitspraken over oorzaken en oplossingen te "
                  "onderbouwen.", 5),
                 ("open", "Waarom is het erkennen van de prijs van een oplossing een sterkte van je "
                          "betoog?",
                  "Omdat elke oplossing een prijs heeft. Wie die benoemt, laat zien dat hij de kwestie "
                  "doorziet; wie ze verzwijgt, laat een lezer de zwakke plek zelf vinden. Het staat "
                  "trouwens met zoveel woorden in het schema.", 5),
             ]),
        dict(kop="Thema's rond het proces",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel juryleden heeft een volksjury, en hoe worden ze aangewezen?",
                  "twaalf, bij lot", WL),
                 ("open", "Geef één argument om de volksjury te behouden en één om ze af te schaffen.",
                  "Behouden: recht spreken blijft dan iets van de samenleving zelf en niet alleen van "
                  "beroepsjuristen. Afschaffen: een assisenproces duurt lang, kost veel en weegt zwaar "
                  "op de juryleden.", 5),
                 ("open", "Waarom bestaan de vormregels waarvan een schending een procedurefout "
                          "oplevert, en waarom voelt zo'n fout toch onrechtvaardig?",
                  "De vormregels beschermen de rechten van de verdediging, dus ze zijn er niet voor "
                  "niets. En toch kan een zaak die daardoor strandt voor een slachtoffer heel "
                  "onrechtvaardig voelen, want de feiten blijven wat ze waren.", 6),
                 ("open", "Bij trial by media staan twee grondrechten tegenover elkaar. Welke?",
                  "Het vermoeden van onschuld tegenover de persvrijheid.", 3),
                 ("open", "Noem drie oorzaken van de kloof tussen burger en justitie.",
                  "Traagheid, kostprijs en moeilijke taal. Wie justitie niet begrijpt, vertrouwt haar "
                  "ook moeilijker.", 4),
             ]),
        dict(kop="Straf en strafuitvoering",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("je zit je straf thuis uit onder elektronisch toezicht", "de enkelband"),
                          ("onbetaalde arbeid voor de samenleving", "de werkstraf"),
                          ("kleine huizen in de buurt, gericht op de terugkeer",
                           "transitie- en detentiehuizen"),
                          ("een maatregel voor wie door een stoornis niet toerekeningsvatbaar is",
                           "de internering")],
                  "Welke vorm?", WL),
                 ("open", "Wat is het argument voor alternatieve straffen, in één zin?",
                  "Wie na zijn straf nog een huis, werk en een gezin heeft, hervalt minder snel.", 3),
                 ("open", "Geef bij strengere strafmaten een argument van beide kanten.",
                  "Voorstanders wijzen op afschrikking en op het gevoel van rechtvaardigheid. "
                  "Tegenstanders wijzen op overbevolkte gevangenissen en op herval na de straf.", 5),
                 ("open", "Waarom is internering een maatregel en geen straf? Gebruik de vrije wil in "
                          "je antwoord.",
                  "Omdat een straf schuld veronderstelt en een maatregel vertrekt van zorg en "
                  "veiligheid. Wie door een stoornis niet anders kón, kan je moeilijk schuldig noemen, "
                  "en dus valt de grond onder het straffen weg terwijl zorg en bescherming blijven.", 6),
                 ("kort", "Vanaf welke leeftijd kan een uithandengeving bij een minderjarige?",
                  "zestien jaar", WL),
                 ("open", "Waarom bestaat verjaring, en waarvoor geldt ze vandaag niet meer?",
                  "Omdat bewijs verdwijnt en getuigen vergeten, en een proces na heel lange tijd dus "
                  "moeilijk eerlijk te voeren is. Voor sommige zeer ernstige misdrijven geldt vandaag "
                  "geen verjaring meer.", 5),
                 ("waar", "Een justitiehuis en een transitiehuis zijn twee namen voor hetzelfde.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-buitengerechtelijke-procedures-en-juridische-bijstand-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Buitengerechtelijke procedures en juridische bijstand",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wie beslist?",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Weg", "Wat gebeurt er", "Wie beslist"],
                  [["bemiddeling", None, None], ["verzoening", None, None],
                   ["arbitrage", None, None]],
                  "bemiddeling: een neutrale bemiddelaar begeleidt het gesprek, de partijen beslissen "
                  "zelf; verzoening of minnelijke schikking: de partijen regelen het met een afspraak "
                  "en beslissen zelf; arbitrage: de partijen leggen het geschil voor aan een arbiter "
                  "die ze samen kiezen, en die beslist", W),
                 ("kort", "Wat betekent buitengerechtelijk?",
                  "buiten de rechtbank om", WL),
                 ("open", "Met welke ene vraag krijg je de drie wegen uit elkaar?",
                  "Wie beslist? Bij bemiddeling en verzoening beslissen de partijen zelf; bij arbitrage "
                  "beslist een derde, net als bij een rechter, maar die derde is door de partijen zelf "
                  "gekozen.", 5),
             ]),
        dict(kop="Bemiddeling",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem vier voordelen van bemiddeling.",
                  "Ze is sneller, meestal goedkoper, vertrouwelijk, en de relatie tussen de partijen "
                  "blijft beter overeind.", 4),
                 ("open", "Waarom weegt dat laatste voordeel zo zwaar? Geef twee voorbeelden.",
                  "Omdat mensen daarna vaak nog met elkaar verder moeten, bijvoorbeeld ouders na een "
                  "scheiding of twee buren. Een vonnis maakt een winnaar en een verliezer; een akkoord "
                  "dat ze zelf maakten, houdt die verhouding leefbaar.", 5),
                 ("open", "Wat is de keerzijde van bemiddeling, en wat gebeurt er als ze niet lukt?",
                  "Ze werkt alleen als beide partijen willen: wie weigert te praten, kan niet verplicht "
                  "worden tot een akkoord. Lukt ze niet, dan staat de weg naar de rechter nog altijd "
                  "open; je verliest je recht om te procederen er niet mee.", 5),
                 ("waar", "Bemiddeling bestaat alleen voordat een zaak bij de rechter komt.", False),
             ]),
        dict(kop="Juridische bijstand en de adressen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("tabel", ["", "Eerstelijnsbijstand", "Tweedelijnsbijstand"],
                  [["wat je krijgt", None, None], ["hoe lang", None, None],
                   ["prijs", None, None]],
                  "eerste lijn: een eerste advies, een algemene inlichting of een doorverwijzing, in "
                  "een kort gesprek, gratis en voor iedereen; tweede lijn: een advocaat die je dossier "
                  "opneemt en je bijstaat, zolang je zaak duurt, gratis of gedeeltelijk gratis als je "
                  "inkomen laag genoeg is", W),
                 ("kort", "Hoe noemen mensen de advocaat van de tweede lijn in de volksmond?",
                  "een pro deo advocaat", WL),
                 ("open", "Is pro deo een gunst? Leg uit.",
                  "Nee, het is een recht als je inkomen onder de grens zit. De advocaat wordt dan door "
                  "de overheid vergoed in plaats van door jou.", 4),
                 ("open", "Waarom bestaat juridische bijstand? Gebruik de gelijkheid voor de wet in je "
                          "antwoord.",
                  "Omdat gelijkheid voor de wet in de praktijk anders van je bankrekening zou afhangen: "
                  "een procedure vraagt geld en kennis. Zonder bijstand zou wie het niet kan betalen "
                  "zijn rechten nergens kunnen laten gelden.", 5),
                 ("rij", [("gratis juridisch eerstelijnsadvies", "de wetswinkel"),
                          ("informatie over justitie, slachtofferonthaal en de opvolging van straffen",
                           "het justitiehuis"),
                          ("hulp bij wonen, geld, relaties en geweld", "het CAW"),
                          ("een pro deo advocaat aanvragen", "het Bureau voor Juridische Bijstand")],
                  "Waar moet je zijn?", WL),
                 ("open", "Twee buren maken ruzie over een haag. Wat raad je aan, en waarom?",
                  "Bemiddeling. Ze blijven buren, dus een akkoord dat ze zelf maken houdt beter stand "
                  "dan een vonnis waarbij één van de twee verliest en ze daarna nog jaren naast elkaar "
                  "wonen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-gerechtelijke-piramide-rechtbanken-en-hoven-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gerechtelijke piramide: rechtbanken en hoven",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Twee soorten bevoegdheid",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("waarover gaat het?", "de materiële bevoegdheid"),
                          ("waar is het gebeurd?", "de territoriale bevoegdheid")],
                  "Welke bevoegdheid?", WL),
                 ("open", "Pas de twee samen toe op een conflict van 3.000 euro tussen twee mensen uit "
                          "Hasselt.",
                  "Materieel hoort het bij het vredegerecht, want het is een kleiner geschil onder de "
                  "5.000 euro. Territoriaal gaat het naar het vredegerecht van het kanton Hasselt, want "
                  "daar wonen ze.", 5),
             ]),
        dict(kop="Welke rechtbank?",
             opdracht="Schrijf bij elke zaak de juiste rechtbank.",
             oefeningen=[
                 ("rij", [("een huurgeschil van 2.000 euro", "het vredegerecht"),
                          ("een verkeersongeval", "de politierechtbank"),
                          ("een ontslag", "de arbeidsrechtbank"),
                          ("een faillissement", "de ondernemingsrechtbank")],
                  "Welke rechtbank?", WL),
                 ("rij", [("een scheiding en de regeling voor de kinderen", "de familierechtbank"),
                          ("een zwaardere strafzaak", "de correctionele rechtbank"),
                          ("een minderjarige met een als misdrijf omschreven feit", "de jeugdrechtbank"),
                          ("een geschil over een uitkering", "de arbeidsrechtbank")],
                  "Welke rechtbank of afdeling?", WL),
                 ("kort", "Tot welk bedrag behandelt het vredegerecht kleinere geschillen?",
                  "5.000 euro", WL),
                 ("open", "Noem de vijf afdelingen van de rechtbank van eerste aanleg.",
                  "De burgerlijke rechtbank, de correctionele rechtbank, de familierechtbank, de "
                  "jeugdrechtbank en de strafuitvoeringsrechtbank.", 4),
                 ("waar", "De zittingen van de jeugdrechtbank zijn openbaar, net als alle andere.",
                  False),
             ]),
        dict(kop="De hoven, en de weg omhoog",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("behandelt de zaak een tweede keer, over de feiten én het recht",
                           "het hof van beroep"),
                          ("de zwaarste misdaden, met een volksjury", "het Hof van Assisen"),
                          ("kijkt enkel of het recht juist is toegepast", "het Hof van Cassatie")],
                  "Welk hof?", WL),
                 ("open", "Wat is het verschil tussen beroep en cassatie?",
                  "Bij beroep wordt de zaak een tweede keer volledig behandeld, over de feiten en het "
                  "recht. Cassatie kijkt niet meer naar de feiten maar enkel naar de vraag of het recht "
                  "juist is toegepast, en verbreekt een uitspraak die de wet schendt. De zaak gaat dan "
                  "terug naar een ander hof.", 6),
                 ("tabel", ["Van", "Beroep bij"],
                  [["het vredegerecht of de politierechtbank", None],
                   ["de rechtbank van eerste aanleg", None],
                   ["het hof van beroep", None]],
                  "van het vredegerecht of de politierechtbank naar de rechtbank van eerste aanleg; "
                  "van eerste aanleg naar het hof van beroep; van het hof van beroep naar het Hof van "
                  "Cassatie, en enkel over de toepassing van het recht", WL),
                 ("rij", [("een uitspraak van een rechtbank", "een vonnis"),
                          ("een uitspraak van een hof", "een arrest")],
                  "Vonnis of arrest?", WL),
                 ("open", "Waarom bestaat beroep in twee instanties?",
                  "Omdat een rechter zich kan vergissen. Een tweede volledige behandeling vangt een "
                  "fout op, en dat is een waarborg voor de rechtzoekende en geen vertragingstruc.", 5),
                 ("open", "Wat gebeurt er als je de termijn om beroep aan te tekenen laat "
                          "voorbijgaan?",
                  "Dan wordt het vonnis definitief, ook als het fout was. De termijn is dus niet "
                  "vrijblijvend.", 4),
                 ("kort", "Welke twee hoven staan naast de piramide, met een eigen taak?",
                  "het Grondwettelijk Hof en de Raad van State", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-burgerlijk-recht-en-strafrecht-het-verloop-van-een-procedure-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Burgerlijk recht en strafrecht: het verloop van een procedure",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Twee takken",
             opdracht="Vul het schema aan en zet elke zaak in de juiste tak.",
             oefeningen=[
                 ("tabel", ["", "Burgerlijk recht", "Strafrecht"],
                  [["gaat over", None, None], ["wie start", None, None],
                   ["tegen wie", None, None], ["wat de rechter beslist", None, None]],
                  "burgerlijk: een geschil tussen twee partijen, gestart door de eiser, tegen de "
                  "verweerder, en de rechter beslist wie recht heeft op wat; straf: een misdrijf tegen "
                  "de samenleving, gestart door het openbaar ministerie, tegen de beklaagde of "
                  "verdachte, en de rechter beslist over schuld en straf", W),
                 ("rij", [("een onbetaalde factuur", "burgerlijk recht"),
                          ("rijden onder invloed", "strafrecht"),
                          ("een scheiding", "burgerlijk recht"),
                          ("diefstal", "strafrecht")],
                  "Welke tak?", WW),
                 ("open", "Dezelfde feiten kunnen in beide takken terechtkomen. Leg dat uit met een "
                          "vechtpartij, en zeg hoe een slachtoffer maar één procedure nodig heeft.",
                  "Wie bij een vechtpartij iemand verwondt, kan strafrechtelijk gestraft worden én "
                  "burgerlijk de schade moeten vergoeden. Het slachtoffer kan zich in de strafzaak "
                  "burgerlijke partij stellen: dan behandelt de strafrechter ook de schadevergoeding, "
                  "en hoeft er geen tweede procedure te komen.", 6),
             ]),
        dict(kop="De burgerlijke procedure",
             opdracht="Zet de stappen op hun plaats en antwoord kort.",
             oefeningen=[
                 ("tabel", ["Stap", "Wat gebeurt er"],
                  [["1. de inleiding", None], ["2. de uitwisseling van stukken", None],
                   ["3. de zitting", None], ["4. het vonnis", None], ["5. de uitvoering", None]],
                  "inleiding: de eiser brengt de zaak voor de rechtbank, meestal met een dagvaarding "
                  "door een gerechtsdeurwaarder; stukken: elke partij legt haar argumenten en bewijzen "
                  "neer in conclusies en kan op de andere antwoorden; zitting: de advocaten pleiten; "
                  "vonnis: de rechter beslist en motiveert; uitvoering: wie in het ongelijk gesteld is "
                  "moet het vonnis uitvoeren, desnoods door een gerechtsdeurwaarder", WL),
                 ("kort", "Welk principe van de rechtspraak zit in stap 2?", "hoor en wederhoor", WL),
                 ("open", "Waarom stelt de rechter in de familie- en jeugdrechtbank vaak bemiddeling "
                          "voor?",
                  "Omdat de partijen daar bijna altijd met elkaar verder moeten. Een akkoord dat ze "
                  "zelf maken, houdt beter stand dan een vonnis dat hen wordt opgelegd.", 5),
                 ("waar", "Een burgerlijke procedure eindigt altijd met een vonnis.", False),
             ]),
        dict(kop="Van feit tot proces",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat is een misdrijf?",
                  "een gedraging die de wet strafbaar stelt", WL),
                 ("kort", "Hoe heet het officiële verslag dat de politie maakt?",
                  "een proces-verbaal", WL),
                 ("tabel", ["", "Het opsporingsonderzoek", "Het gerechtelijk onderzoek"],
                  [["wie leidt", None, None], ["wanneer", None, None], ["waarom zo", None, None]],
                  "opsporingsonderzoek: het openbaar ministerie, de gewone gang van zaken, snel en "
                  "soepel; gerechtelijk onderzoek: de onderzoeksrechter, bij ernstige zaken of wanneer "
                  "zware onderzoeksdaden nodig zijn, omdat een onafhankelijke rechter moet beslissen "
                  "over maatregelen die diep in iemands rechten snijden, zoals een huiszoeking", W),
                 ("open", "Noem de drie wegen die het parket na het vooronderzoek heeft.",
                  "Seponeren, een minnelijke schikking voorstellen, of vervolgen.", 3),
                 ("open", "Waarom is seponeren geen vrijspraak?",
                  "Omdat een vrijspraak van een rechter komt, na een proces. Seponeren is een "
                  "beslissing van het parket om geen proces te starten, bijvoorbeeld bij te weinig "
                  "bewijs of een te klein feit.", 5),
                 ("rij", [("beslist of de zaak naar de rechtbank gaat, en over de aanhouding",
                           "de raadkamer"),
                          ("behandelt het beroep tegen die beslissingen bij het hof van beroep",
                           "de kamer van inbeschuldigingstelling")],
                  "Welke kamer?", WL),
                 ("kort", "Hoe heet het eigenlijke proces, dat openbaar is en met getuigen en "
                          "pleidooien?", "het onderzoek ter terechtzitting", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-juridische-termen-en-actoren-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Juridische termen en actoren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wie staat er tegenover wie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("wie de zaak begint en iets vraagt, in een burgerlijke zaak", "de eiser"),
                          ("wie zich tegen die eis verdedigt", "de verweerder"),
                          ("wie tijdens het vooronderzoek in het vizier staat", "de verdachte"),
                          ("wie voor de strafrechter terechtstaat", "de beklaagde")],
                  "Wie is dit?", WL),
                 ("kort", "Hoe heet een slachtoffer dat in de strafzaak zelf een schadevergoeding "
                          "vraagt?", "de burgerlijke partij", WL),
                 ("kort", "Hoe heet wie voor het Hof van Assisen terechtstaat?",
                  "de beschuldigde", WL),
                 ("open", "Waarom is een verdachte geen dader?",
                  "Omdat zijn schuld nog niet door een rechter is vastgesteld. Dat is het vermoeden van "
                  "onschuld: tot die uitspraak valt er geen oordeel over hem.", 4),
             ]),
        dict(kop="De mensen van justitie",
             opdracht="Schrijf bij elke taak wie ze doet.",
             oefeningen=[
                 ("rij", [("vervolgt misdrijven in naam van de samenleving",
                           "het openbaar ministerie"),
                          ("leidt een gerechtelijk onderzoek bij ernstige zaken",
                           "de onderzoeksrechter"),
                          ("houdt het dossier bij en schrijft op wat er op de zitting gebeurt",
                           "de griffier"),
                          ("betekent een dagvaarding en voert een vonnis uit",
                           "de gerechtsdeurwaarder")],
                  "Wie doet dit?", WL),
                 ("kort", "Wie staat aan het hoofd van het parket?", "de procureur", WL),
                 ("open", "Waarom is de onderzoeksrechter de lastigste om te plaatsen?",
                  "Omdat hij niet voor het parket en niet voor de verdediging werkt. Hij is rechter en "
                  "geen vervolger: hij zoekt de waarheid, en dus ook het bewijs dat iemand onschuldig "
                  "is.", 5),
                 ("waar", "Zonder griffier is er geen geldige zitting.", True),
                 ("open", "Waaraan is een advocaat gebonden, naast de wet?",
                  "Aan zijn beroepsgeheim en aan de deontologie van de balie, de beroepsregels die de "
                  "advocaten voor zichzelf hebben opgesteld.", 4),
             ]),
        dict(kop="De woorden in een dossier",
             opdracht="Schrijf bij elke omschrijving het juiste woord.",
             oefeningen=[
                 ("rij", [("de officiële uitnodiging om voor de rechtbank te verschijnen",
                           "een dagvaarding"),
                          ("alle stukken die in een strafzaak verzameld zijn", "het strafdossier"),
                          ("een zaak opnieuw laten behandelen door een hogere rechter", "beroep"),
                          ("een uitspraak laten nakijken op de toepassing van het recht", "cassatie")],
                  "Welk woord?", WL),
                 ("rij", [("de zaak zonder gevolg laten, door het parket", "seponeren"),
                          ("een zaak regelen met een afspraak, zonder vonnis",
                           "een minnelijke schikking"),
                          ("alles wat gebeurt voor de zaak voor de rechter komt", "het vooronderzoek"),
                          ("de uitspraak van een hof", "een arrest")],
                  "Welk woord?", WL),
                 ("open", "Waarom is het nuttig deze woorden te kennen, ook als je geen jurist wordt?",
                  "Omdat een brief van een advocaat of een deurwaarder in deze taal geschreven is. Wie "
                  "ze niet begrijpt, weet niet wat er van hem gevraagd wordt en mist een termijn. De "
                  "moeilijke taal van justitie is een van de redenen voor de kloof met de burger, en "
                  "net daarom is het nuttig ze te kennen.", 6),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-de-eigenheid-van-de-filosofie-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="De proef is eenvoudig: kan je het antwoord in principe gaan meten, tellen of "
                   "opzoeken? Dan is het een feitenvraag. Gaat het over wat juist, goed of "
                   "wezenlijk is, dan is het een filosofische vraag.",
            waarom=[
                "Let op de paren: hoeveel jongeren naar het hoger onderwijs gaan is te tellen, of "
                "iedereen er recht op heeft niet. Elk paar zet dezelfde twee vragen naast elkaar, "
                "en dat is precies de bedoeling.",
                "Let op wat is een rechtvaardige straf tegenover hoeveel mensen in de gevangenis "
                "zitten. Een vraag die met hoeveel of wanneer begint, is bijna altijd een "
                "feitenvraag; een vraag die met wat is of mag je begint, bijna altijd een "
                "filosofische.",
                "Noem dat zijn vraag niet over meetbare feiten gaat maar over begrippen en waarden. "
                "Het scherpe onderscheid: je kan meten hoeveel mensen iets rechtvaardig vinden, "
                "maar niet of het rechtvaardig is.",
            ],
        ),
        dict(
            aanpak="Natuurwetenschappen onderzoeken de stof en de natuur, menswetenschappen de "
                   "mens en de samenleving, en de filosofie de vragen die achter beide liggen. Een "
                   "vraag die begint met wat is of wat kan ik, hoort bij de filosofie.",
            waarom=[
                "Let op de derde: wat kan ik weten is geen psychologie maar filosofie, want ze "
                "vraagt niet hoe mensen leren maar wat kennis is.",
                "Let op de geschiedenis: die staat bij de menswetenschappen, want ze onderzoekt "
                "mensen en samenlevingen, ook al werkt ze met bronnen zoals een natuurwetenschapper "
                "met metingen.",
                "Liefde voor de wijsheid, van philia en sophia. Het woord zelf zegt dus dat je de "
                "wijsheid zoekt en niet dat je ze hebt, en dat is het antwoord op de volgende "
                "oefening.",
                "Niet waar, en de naam zegt net het omgekeerde: een filosoof is een liefhebber van "
                "de wijsheid, iemand die ernaar zoekt. Socrates zei dat hij vooral wist dat hij "
                "niets wist.",
            ],
        ),
        dict(
            aanpak="Zet de twee manieren van verklaren naast elkaar: een mythisch verhaal legt de "
                   "oorzaak buiten de wereld, bij de goden, en de natuurfilosofie zoekt ze in de "
                   "natuur zelf. Dat ene verschil verklaart alle antwoorden in deze reeks.",
            waarom=[
                "Vul de tabel rij per rij in en let op de laatste rij: te toetsen of niet. Dat is "
                "het punt waar de natuurfilosofie echt iets nieuws doet.",
                "Noem dat het verhaal alles verklaart. Dat klinkt als een sterkte en is net de "
                "zwakte: een verklaring die nooit tegengesproken kan worden, zegt niets. Bij Popper "
                "heet dat niet te weerleggen, en dat komt in een later hoofdstuk terug.",
                "Met de natuurfilosofie, niet met de mythologie. De mythologie komt ervoor, maar "
                "ze is nog geen filosofie, want ze bevraagt haar eigen verklaring niet.",
                "Noem beide helften: wat verwondering is, en je eigen voorbeeld. Een goed voorbeeld "
                "gaat over iets alledaags; verwondering over iets uitzonderlijks is gewoon "
                "nieuwsgierigheid.",
                "Drie, zoals de hoofdstukken erna laten zien: kennis, mens en wereld, en ethiek. De "
                "argumentatieleer staat daar los van, want ze is het gereedschap dat je in alle "
                "drie gebruikt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bronnen-van-kennis-rationalisme-en-empirisme-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk voorbeeld af hoe je het te weten komt: door te kijken of te "
                   "horen (de zintuigen), door het te herinneren, door naar binnen te kijken (de "
                   "introspectie), door iemand te geloven, of door het uit iets anders af te "
                   "leiden.",
            waarom=[
                "Let op de laatste: dat de aarde om de zon draait, heb je niet zelf gezien of "
                "berekend, dus komt het uit verhalen van anderen. Dat voelt vreemd voor iets wat "
                "zeker is, en dat is precies het punt van oefening 3.",
                "Let op het verschil tussen de eerste en de rest: alle mensen zijn sterfelijk, dus "
                "ook jij, is een afleiding en geen waarneming. Daar komt geen enkel zintuig aan te "
                "pas.",
                "Noem dat het meeste van je kennis van anderen komt en dat je dat niet kan nakijken. "
                "Dat maakt de vraag wie je gelooft een dagelijkse keuze, en niet iets van de "
                "filosofieles alleen.",
            ],
        ),
        dict(
            aanpak="Houd de twee stromingen aan hun vertrekpunt uit elkaar: het rationalisme begint "
                   "bij de rede en werkt met deductie, het empirisme bij de ervaring en werkt met "
                   "inductie. Daaruit volgt ook hun zekerheid.",
            waarom=[
                "Vul de tabel rij per rij in. De laatste rij is de belangrijkste: deductie is zeker "
                "als de premissen kloppen, inductie nooit helemaal, en dat is wat oefening 7 "
                "uitlegt.",
                "De methodische twijfel: twijfelen aan alles wat ook maar kan betwijfeld worden, om "
                "te zien wat overblijft. Wat overbleef, was dat hij twijfelde en dus dacht.",
                "Deductie gaat van algemeen naar bijzonder, inductie van bijzonder naar algemeen. "
                "Een handig steuntje: bij inductie zie je een paar gevallen en maak je er een regel "
                "van, en dat is wat de bus in de laatste doet.",
                "Noem de zwarte zwaan. Dat is het klassieke voorbeeld, en het is ook echt gebeurd: "
                "in Europa dacht men eeuwen dat alle zwanen wit waren, tot men ze in Australie zag.",
                "Niet waar. Een onderzoeker gebruikt beide: hij bedenkt met zijn rede een hypothese "
                "en toetst ze aan de ervaring. Kant probeerde de twee uitdrukkelijk te verzoenen.",
            ],
        ),
        dict(
            aanpak="De grotallegorie en de AUB-methode lijken los te staan maar horen samen: het "
                   "eerste zegt waarom een goed argument nodig is, het tweede hoe je er een bouwt.",
            waarom=[
                "Noem de ketenen, de schaduwen, de ene die buiten komt en de ongelovige reactie van "
                "de anderen. En zeg waar het om gaat, want zonder die laatste zin heb je een "
                "verhaal naverteld en geen vraag beantwoord.",
                "Vul de drie letters aan: argument, uitleg, bijvoorbeeld. De u is het stuk dat men "
                "vergeet, en net daar zit de kracht van een betoog: zonder uitleg is een argument "
                "enkel een mening met een voorbeeld erbij.",
                "Een gezagsargument. Het is niet vanzelf fout: naar een vakman verwijzen is "
                "redelijk. Het wordt een drogreden als die persoon geen kenner is van dit onderwerp, "
                "en dat komt in het hoofdstuk over drogredenen terug.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-van-natuurfilosofie-naar-wetenschap-falsificatie-en-demarcatie-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Alles in deze reeks hangt aan één omslag: niet vragen wat mijn theorie "
                   "bevestigt, maar wat ze zou weerleggen. Houd die vraag in je hoofd en de "
                   "antwoorden volgen.",
            waarom=[
                "Afbakening, van het Franse marquer, een grens zetten. Het woord zegt dus al "
                "waarover het probleem gaat.",
                "Noem dat het om de grens gaat en formuleer ze als een vraag. De bijzaak is "
                "waar de grens precies ligt; de hoofdzaak is dat er een maatstaf nodig is.",
                "Vul de tabel rij per rij in. De kern staat in de laatste rij: honderd "
                "bevestigingen bewijzen niets, één tegenvoorbeeld beslist, en dat is waarom "
                "Popper voor falsificatie koos.",
                "Popper, Karl Popper. Hij werkte in de twintigste eeuw en wou vooral een maatstaf "
                "die ook pseudowetenschap kon uitsluiten.",
                "Noem dat ze niets uitsluit. Een theorie die met elke uitkomst te verzoenen is, "
                "verbiedt niets, en wie niets verbiedt, voorspelt ook niets.",
                "Niet waar, en dit is de belangrijkste nuance van het hele hoofdstuk. Een weerlegde "
                "theorie was juist wél wetenschappelijk, want ze sloot iets uit en men kon "
                "vaststellen dat het misliep. Zie ook oefening 8.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk voorbeeld af wat er gebeurt als de voorspelling niet uitkomt. "
                   "Wordt de theorie dan wat bijgedraaid, of wordt ze opgegeven? Dat verschil is "
                   "het hele kenmerk.",
            waarom=[
                "Let op het verschil tussen vage voorspellingen en uitvluchten: de eerste kan niet "
                "misgaan, bij de tweede wordt de theorie ná de tegenslag aangepast. Beide zorgen "
                "ervoor dat ze nooit fout kan zijn.",
                "Noem dat het verschil in de toetsbaarheid zit en niet in de uitkomst. Dat is "
                "hetzelfde antwoord als bij oefening 6, nu in volle zinnen.",
                "Dat ze zichzelf kan verbeteren. Daarom is een weerlegging geen schande voor de "
                "wetenschap maar haar motor, en dat onderscheidt haar van een leer die nooit van "
                "mening verandert.",
            ],
        ),
        dict(
            aanpak="Drie namen, drie stappen in dezelfde geschiedenis: eerst ordenen, dan meten, "
                   "dan toetsen. En drie leesstappen die daarmee overeenkomen: lezen, begrijpen, "
                   "bekritiseren.",
            waarom=[
                "Let op de orde in de tijd: Aristoteles in de oudheid, Bacon aan het begin van de "
                "moderne tijd, Popper in de twintigste eeuw. Bacon keerde zich uitdrukkelijk tegen "
                "het gezag van oude boeken, ook dat van Aristoteles.",
                "Vul de drie stappen aan. Dat de derde stap kritiek is, betekent dat lezen niet "
                "stopt bij begrijpen: je moet ook zoeken wat de auteur zou tegenspreken, precies "
                "zoals Popper vraagt.",
                "Noem de proef met de vriend. Dat is een eerlijke toets, want uitleggen is iets "
                "anders dan herkennen, en bij herkennen stopt men meestal te vroeg.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-lichaam-en-geest-monisme-en-dualisme-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist bij elke filosoof: zijn lichaam en geest twee verschillende "
                   "dingen die van elkaar kunnen bestaan, of twee kanten van hetzelfde? Twee "
                   "werkelijkheden is dualisme, één is monisme.",
            waarom=[
                "Let op Plato en Descartes naast elkaar: beide scheiden ziel en lichaam, maar met "
                "eeuwen ertussen. Parmenides en Spinoza staan aan de andere kant, en ook daar "
                "liggen eeuwen tussen.",
                "Monos, het Griekse woord voor één. Daarom is monisme de stelling dat er maar één "
                "soort werkelijkheid is.",
                "Duo, twee. Hetzelfde woorddeel zit in duel en duo, en dat helpt om de twee termen "
                "niet te verwisselen.",
                "Noem dat de ziel bij hem de vorm van het lichaam is, en wat daaruit volgt bij de "
                "dood. Onderscheiden zonder te scheiden: dat is de hele kern van zijn positie.",
            ],
        ),
        dict(
            aanpak="Leer elke stelling in de woorden van de filosoof zelf: het zijnde is één, de "
                   "ziel is onsterfelijk, de ziel is de vorm van het lichaam, denken en "
                   "uitgebreidheid zijn twee. Die vier formules dekken de hele reeks.",
            waarom=[
                "Let op uitgebreidheid: dat is het woord van Descartes voor alles wat plaats "
                "inneemt, dus het stoffelijke. Zijn tweedeling is denken tegenover uitgebreidheid.",
                "Spinoza. Hij gebruikt dezelfde twee woorden als Descartes, maar noemt ze twee "
                "kanten van één werkelijkheid in plaats van twee werkelijkheden. Dat ene verschil "
                "maakt hem een monist.",
                "Noem bij wie het opkomt en waarom. Descartes legde de ontmoeting bij de pijnappelklier "
                "in de hersenen, maar daarmee is de vraag verschoven en niet opgelost.",
                "Noem dat hij de knip ongedaan maakt. Zo zie je waarom het interactieprobleem geen "
                "los raadsel is maar een gevolg van de keuze voor twee werkelijkheden.",
            ],
        ),
        dict(
            aanpak="Hier gaat het over de vraag of de westerse tweedeling de enige mogelijke is. "
                   "Houd twee dingen uit elkaar: wat onderzoek vaststelt, en wat je daaruit "
                   "filosofisch besluit.",
            waarom=[
                "Waar. In verschillende tradities denkt men eerder in geheel en samenhang dan in "
                "twee delen, en dat is geen gebrek maar een andere indeling.",
                "Noem dat er geen vast, blijvend zelf is. Daarmee is ook de vraag of de ziel het "
                "lichaam overleeft niet zomaar te stellen, want er is niets blijvends dat zou "
                "overleven.",
                "Noem het verschil tussen samenhang en identiteit. Dat is dezelfde fout als "
                "besluiten dat twee dingen hetzelfde zijn omdat ze altijd samen voorkomen, en die "
                "stap is filosofisch, niet experimenteel.",
                "Om te zien dat de westerse indeling zelf een keuze is. Vergelijken dient dus niet "
                "om de ene traditie fout te verklaren, maar om te merken dat wat vanzelfsprekend "
                "lijkt, het niet is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-cultuur-en-natuur-mens-dier-en-machine-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Houd twee vragen uit elkaar: wat kunnen dieren ook, en wat telt er voor ons om "
                   "de mens mens te noemen? De eerste is onderzoek, de tweede filosofie. Bijna alle "
                   "fouten in dit hoofdstuk komen van die twee door elkaar halen.",
            waarom=[
                "Uitsluitend bij de mens, dus bij niemand anders. Dat is een strenge eis, en dat is "
                "precies waarom er zo weinig overblijft.",
                "Niet waar. Vaker of sterker is een gradueel verschil; exclusief betekent dat het "
                "bij andere wezens helemaal niet voorkomt. Dat verschil maakt of een kenmerk de "
                "toets haalt.",
                "Vul de tabel rij per rij in en let erop dat elke rij twee kanten heeft: wat "
                "mensen doen én wat dieren ook blijken te doen. Zo zie je waarom geen van de twee "
                "de toets van exclusief haalt.",
                "Noem dat het beslissen welk verschil telt, een vraag over begrippen en waarden is. "
                "Vaststellen dat kraaien werktuigen gebruiken, is onderzoek; besluiten dat dat niet "
                "meetelt, is het niet.",
                "Noem dat eten, slapen en taal tegelijk natuurlijk en cultureel zijn. Daarom is de "
                "tegenstelling bruikbaar om over te denken, maar niet als strakke indeling.",
            ],
        ),
        dict(
            aanpak="De drie benaderingen kijken naar dezelfde emotie op drie plaatsen: in het "
                   "lichaam, in de gewoonten van een samenleving, en in je oordeel over wat er "
                   "gebeurt.",
            waarom=[
                "Let op het eerste: waar je ook geboren bent, dus niet cultureel. En op het derde: "
                "de knal of de gebeurtenis blijft dezelfde, enkel je oordeel verandert.",
                "Noem dat de gebeurtenis gelijk blijft en je oordeel verandert. Dat is de "
                "scherpste proef, en ze werkt bij elk voorbeeld van deze benadering.",
                "Niet waar. Eén emotie heeft meestal alle drie de kanten: een lichamelijke reactie, "
                "een vorm die je samenleving eraan geeft, en een oordeel. De drie zijn brillen, "
                "geen vakjes.",
            ],
        ),
        dict(
            aanpak="Zet de vier posities op een lijn van hoog naar laag: de mens als redelijk dier, "
                   "de mens als enige met een geest, de mens zonder ereplaats, en de mens als "
                   "machine. Dan zie je waar elke naam staat.",
            waarom=[
                "Let op Descartes en La Mettrie naast elkaar: beide gebruiken het beeld van de "
                "machine, maar Descartes houdt de mens erbuiten en La Mettrie niet. Dat is het hele "
                "verschil tussen hun posities.",
                "Swaab. Zijn stelling sluit aan bij La Mettrie, maar met hersenonderzoek in plaats "
                "van met filosofie, en daarom geldt hier dezelfde nuance als bij oefening 12.",
                "Noem het gedrag bij pijn. Dat bezwaar is ook juridisch belangrijk geworden: onze "
                "wetten op dierenwelzijn gaan ervan uit dat een dier wel iets ervaart.",
                "Noem dat kunnen voortdurend opschuift en dat ervaren de vraag is die blijft. "
                "Daarom kan je uit een machine die praat als een mens nog niet besluiten dat er "
                "iemand is om te zijn.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vrijheid-en-determinisme-van-de-oudheid-tot-de-19de-eeuw-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Stel bij elk voorbeeld twee vragen: lag het vast, en zat er een bedoeling "
                   "achter? Lot is vast met bedoeling, determinisme is vast zonder bedoeling, "
                   "toeval is geen van beide.",
            waarom=[
                "Let op het eerste en het derde: bij het lot is er iets dat het zo wil, bij het "
                "determinisme enkel een keten van oorzaken. Dat is hetzelfde onderscheid als in de "
                "tabel erna.",
                "Vul de twee kolommen in: lag het vast, en zat er een bedoeling achter? Met die "
                "twee vragen kan je elk voorbeeld in deze reeks plaatsen.",
                "Noem het woord determineren, vastleggen. En noem beide vergelijkingen: kaler dan "
                "het lot omdat er geen bedoeling bij hoort, strenger dan toeval omdat het wel "
                "vastligt.",
            ],
        ),
        dict(
            aanpak="In de oudheid liggen drie antwoorden naast elkaar: het lot van de mythologie, "
                   "de atomen van Democritus en de innerlijke vrijheid van de Stoicijnen. Zet er "
                   "telkens bij waar de vrijheid dan nog zit.",
            waarom=[
                "Niet waar, en dat is net het bijzondere: ook de goden zijn aan het lot gebonden. "
                "Daardoor is er in die verhalen niemand meer bij wie je in beroep kan gaan.",
                "Noem dat de vlucht zelf deel van het lot blijkt. Dat is wat het verhaal zo "
                "benauwend maakt: elke poging om te ontsnappen werkt mee.",
                "Let op Democritus: hij is de eerste met een determinisme zonder goden, en daarmee "
                "de voorganger van het mechanische wereldbeeld uit de derde reeks.",
                "Noem het onderscheid tussen wat in je macht ligt en wat niet, en geef er een eigen "
                "voorbeeld bij. Zonder voorbeeld blijft het een formule, en net het voorbeeld laat "
                "zien of je het begrijpt.",
            ],
        ),
        dict(
            aanpak="Van de zeventiende eeuw af wordt de natuur als een machine gezien, en dat zet "
                   "de vraag scherp. Let bij elke denker op waar hij de vrijheid plaatst, of waarom "
                   "hij ze schrapt.",
            waarom=[
                "Mechanisch determinisme: de wereld als een uurwerk dat volgens vaste wetten "
                "doorloopt. Laplace dacht dat wie alle posities kende, de hele toekomst kon "
                "berekenen.",
                "Noem beide takken van de vraag: zit de mens erin of is hij een uitzondering? Juist "
                "omdat beide antwoorden iets kosten, blijft de vraag open.",
                "Let op het verschil: Schopenhauer laat de handeling vrij maar niet het willen, "
                "Nietzsche verdenkt het hele begrip van een bedoeling. Dat tweede is een verwijt aan "
                "de moraal en niet enkel een analyse.",
                "Noem dat het strafrecht uitgaat van anders kunnen handelen. Daarom vraagt een "
                "rechter ook naar toerekeningsvatbaarheid, en dat is deze filosofische vraag in "
                "juridische vorm.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vrijheid-en-determinisme-in-de-20ste-eeuw-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf denkers, vijf plaatsen waar de vrijheid zit: in het opnemen van je leven, "
                   "in de keuze zelf, in wat je wil willen, in wat de samenleving van je maakt, of "
                   "nergens. Leer ze aan die ene formule.",
            waarom=[
                "Let op Heidegger en Sartre naast elkaar: beide zeggen dat je je situatie niet "
                "koos, maar Sartre legt alle gewicht op de keuze en Heidegger op het opnemen van "
                "wat je aantreft.",
                "Verplaetse, Jan Verplaetse. Hij is de enige van de vijf die uitdrukkelijk "
                "besluiten trekt voor het strafrecht, en dat komt in oefening 13 terug.",
                "Zet de rij in die orde en leg enkel je twee uitersten uit, zoals gevraagd. Dat "
                "Sartre de vrijheid een verdoemenis noemt, maakt hem het uiterste: meer vrijheid "
                "kan je niet toekennen.",
            ],
        ),
        dict(
            aanpak="Houd bij Heidegger twee woorden vast: geworpenheid voor wat je aantreft, en "
                   "eigenlijk tegenover oneigenlijk voor hoe je ermee omgaat. Bij Sartre: gedoemd "
                   "tot vrijheid en kwade trouw.",
            waarom=[
                "Geworpenheid: je bent in een tijd, een lichaam en een afkomst geworpen zonder dat "
                "iemand het je vroeg. Het woord zelf zegt dat je er niet voor koos.",
                "Noem ook wat het níét is, want dat is uitdrukkelijk gevraagd. Oneigenlijk leven is "
                "geen bedrog maar wegkijken, en dat maakt het ook veel gewoner dan liegen.",
                "Noem het mes, want daarmee wordt de formule helder: bij een voorwerp ligt het doel "
                "vast voor het bestaat, bij een mens net niet. De uitdrukking komt van Sartre zelf: "
                "de existentie gaat aan de essentie vooraf.",
                "Let op de laatste: ik deed niets, dus ik koos niets is bij Sartre juist wél een "
                "keuze. Niet kiezen bestaat bij hem niet, en dat is waarom hij het een uitvlucht "
                "noemt.",
                "Niet waar, en dat is de kern van gedoemd tot vrijheid. Omdat je niets kan "
                "aanwijzen dat voor jou beslist, draag je alles zelf, en dat noemt Sartre een last.",
            ],
        ),
        dict(
            aanpak="Deze drie staan op een rij van minder naar geen vrijheid: Foucault zegt dat je "
                   "verlangen gevormd wordt, Frankfurt verzoent vrijheid met oorzaken, en "
                   "Verplaetse schrapt de vrije wil. Let bij elk op wat er dan nog overblijft.",
            waarom=[
                "Disciplinering. Het punt is dat dit niet met geweld gebeurt maar met gewoonten, "
                "schema's en verwachtingen, en daarom merk je het nauwelijks.",
                "Noem dat niemand je dwingt en je verlangen toch gevormd wordt. Dat is wat zijn "
                "machtsbegrip bijzonder maakt: macht zit niet enkel bij wie beveelt.",
                "Vul beide rijen in en let op het woordje willen in de tweede verdieping: wil je de "
                "drang die je hebt ook hebben? Dat is de hele toets van Frankfurt.",
                "Noem dat zijn vraag niet is of je keuze zonder oorzaak was, maar of ze van jou is. "
                "Daarmee hoeft hij het determinisme niet te ontkennen, en vandaar het woord "
                "verzoenend.",
                "Noem de vier maatregelen en zeg welke er sneuvelt. Enkel vergelden heeft schuld "
                "nodig; beschermen, behandelen en voorkomen kunnen zonder, en dat is de kern van "
                "zijn voorstel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ethiek-basisbegrippen-en-vier-benaderingen-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Een waarde is een algemeen goed dat je nastreeft, een norm is de concrete regel "
                   "die eruit volgt. Staat er een gebod of een verbod in, dan is het een norm.",
            waarom=[
                "Let op het patroon: elk paar bestaat uit een waarde en een norm die eruit volgt. "
                "Eerlijkheid is de waarde, niet spieken de regel die er in een school uit volgt.",
                "Noem dat de waarde algemeen is en de norm concreet. Daarom kan je het over de "
                "waarde eens zijn en over de norm van mening verschillen, en daar gaan de meeste "
                "discussies over.",
            ],
        ),
        dict(
            aanpak="Houd de drie standpunten uit elkaar aan de vraag: gelden morele regels overal "
                   "(universalisme), hangen ze van de spreker af (moreel relativisme), of horen ze "
                   "bij een cultuur die je niet van buitenaf mag beoordelen (cultuurrelativisme)?",
            waarom=[
                "Let op het verschil tussen de laatste twee: moreel relativisme kijkt naar wie het "
                "zegt, cultuurrelativisme naar de groep waarin het gezegd wordt. Dat tweede is het "
                "standpunt dat in oefening 4 onder vuur komt.",
                "Noem dat ook kritiek op onrecht dan onmogelijk wordt, ook in je eigen samenleving. "
                "Dat laatste is de scherpste vorm van het bezwaar: het treft niet alleen de kritiek "
                "op anderen.",
                "Niet waar. Een universalist kan rustig toegeven dat de normen verschillen; hij "
                "houdt enkel vol dat sommige waarden overal gelden. Verschil vaststellen en "
                "verschil goedkeuren zijn twee dingen.",
                "Noem dat verwijten enkel zin heeft als iemand anders kón handelen. Daarmee hangt "
                "de hele ethiek vast aan het hoofdstuk over de vrije wil.",
            ],
        ),
        dict(
            aanpak="Vier benaderingen kijken naar vier verschillende dingen: de uitkomst, de regel, "
                   "de persoon en de relatie. Leer ze aan de vraag die elk stelt, dan kan je elke "
                   "casus met vier brillen bekijken.",
            waarom=[
                "Noem dat elke uitweg iets van waarde kost. Dat is het verschil met een moeilijke "
                "keuze: bij een dilemma blijft er ook na de beste beslissing iets onherstelbaar.",
                "Descriptief beschrijft wat mensen vinden, normatief vraagt wat juist is. Een "
                "bevraging kan dus nooit beslechten of iets een plicht is, en dat is hetzelfde "
                "punt als bij Hume in oefening 10.",
                "Vul de vier rijen in met hun eigen vraag erbij. Die vier vragen zijn het "
                "gereedschap voor de hoofdstukken die volgen, waar elke benadering apart aan bod "
                "komt.",
                "Let op het verschil tussen de eerste twee en de derde: de derde zegt hetzelfde als "
                "de eerste, maar plakt er met dus een voorschrift aan. Daar zit de sprong.",
                "Het woordje dus. Dat is de is-ought sprong van Hume, en de les is niet dat de "
                "stap altijd fout is, maar dat je hem apart moet verdedigen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gevolgenethiek-en-plichtethiek-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="De gevolgenethiek kijkt enkel naar de uitkomst: wat brengt het meeste geluk "
                   "teweeg, voor zoveel mogelijk wezens? Houd bij elke vraag in het oog dat de daad "
                   "zelf er niet toe doet, enkel wat ze oplevert.",
            waarom=[
                "Het utilitarisme. De twee namen betekenen hetzelfde, dus gebruik ze door elkaar "
                "zoals je handboek dat doet.",
                "Van utilitas, nut. De naam zegt dus al dat iets goed is naar wat het opbrengt.",
                "Let op de uitbreiding bij Singer: Bentham telt geluk, Singer vraagt van wie je het "
                "meetelt. Dat is dezelfde gedachte, maar met een ruimere kring.",
                "Soortisme, naar het patroon van racisme en seksisme. Zijn punt is niet dat een mens "
                "en een varken gelijk zijn, maar dat lijden lijden is, bij wie het ook voorkomt.",
                "Noem beide kanten, want de vraag vraagt ze uitdrukkelijk. Het voorbeeld van tien "
                "gelukkigen en één diep ongelukkige laat zien hoe een optelsom onrecht kan "
                "verbergen.",
                "Noem alle drie en houd ze kort. Het derde is het bezwaar van Hume uit het vorige "
                "hoofdstuk, nu op het utilitarisme toegepast.",
            ],
        ),
        dict(
            aanpak="Bij Kant telt de regel en niet de uitkomst. De toets is: kan ik willen dat "
                   "iedereen dit doet? Een regel die enkel werkt zolang anderen hem niet volgen, "
                   "zakt op die toets.",
            waarom=[
                "Onvoorwaardelijk, dus zonder als of tenzij. Dat is het hele verschil met een "
                "hypothetische imperatief, die altijd met een wil je begint.",
                "Let op het patroon: de hypothetische beginnen met wil je, de categorische zijn "
                "kale geboden. Kant vindt enkel die tweede moreel, want de eerste hangen van je "
                "doel af.",
                "Schrijf ze in de woorden van de bundel. Let op de twee delen: enkel volgens een "
                "regel, en waarvan je kan willen dat ze voor allen geldt.",
                "Noem beide helften: wat de formulering zegt en wat eruit volgt. Let op het woordje "
                "louter: een mens als middel gebruiken mag, zolang hij niet enkel middel is. Een "
                "bakker betalen is geen misbruik.",
                "Noem beide bezwaren. Het eerste is het klassieke voorbeeld van de moordenaar aan "
                "de deur, het tweede is dat zijn toets een vorm oplegt en geen inhoud.",
                "Niet waar, en het is net het omgekeerde: zijn plicht geldt onvoorwaardelijk, voor "
                "iedereen en in elke situatie. Juist dat maakt hem voor sommigen te streng.",
            ],
        ),
        dict(
            aanpak="Levinas zet de ethiek nog eens anders: niet bij de uitkomst en niet bij de "
                   "regel, maar bij de ontmoeting. Vergelijk hem met Kant op twee punten: waar het "
                   "begint, en of de uitkomst meeweegt.",
            waarom=[
                "Noem het gelaat en het verschil met Kant. Let op wat ze gemeen hebben: bij beiden "
                "weegt de uitkomst niet mee, en dat plaatst beiden tegenover de gevolgenethiek.",
                "Vul de tabel rij per rij in en let op de rij over de belofte: daar botsen de twee "
                "richtingen het duidelijkst. De laatste rij noemt van elke richting haar eigen "
                "zwakte.",
                "Noem beide kanten, lastig en nuttig. Dat je met twee brillen verder komt dan met "
                "één, is de hele reden dat dit hoofdstuk vier benaderingen naast elkaar zet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-deugdethiek-en-zorgethiek-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Bij een deugd horen altijd drie dingen: wat ze is, het tekort eronder en de "
                   "overdaad erboven. Leer ze als een rij van drie, dan heb je de hele tabel in je "
                   "hoofd.",
            waarom=[
                "Vul de tabel rij per rij in: de deugd, het tekort en de overdaad. Let op de "
                "overdaad van verstandigheid: besluiteloosheid, want eindeloos afwegen is ook geen "
                "verstandigheid.",
                "Van cardo, spil of deurhengsel. Deze vier zijn dus de deugden waarop de andere "
                "draaien.",
                "Niet waar, en dit is de val van het woord midden. Het midden van Aristoteles is "
                "het juiste punt tussen twee uitersten, niet het gemiddelde van wat mensen doen. "
                "Doet iedereen hetzelfde fout, dan is dat nog geen deugd.",
                "Noem dat het midden van de situatie afhangt en dat daar verstandigheid bij hoort. "
                "Daarom is de deugdethiek geen regelboek: ze vraagt oordeelsvermogen.",
                "Noem dat je ze oefent tot ze een gewoonte wordt. Het Griekse woord ethos betekent "
                "ook gewoonte, en dat is de reden dat ethiek zo heet.",
            ],
        ),
        dict(
            aanpak="Drie denkers die de deugdethiek verder brengen: Nussbaum met een lijst van wat "
                   "elke mens moet kunnen, Hume met de vraag waar een deugd vandaan komt, en Foot "
                   "met de vraag waaraan je er een herkent.",
            waarom=[
                "Tien. Let erop dat het een lijst van capaciteiten is en geen lijst van deugden, "
                "en dat is wat oefening 7 uitlegt.",
                "Noem dat het over kunnen gaat en niet over doen. Daarom is het ook een maatstaf "
                "voor een samenleving: die moet de mogelijkheid geven, niet het resultaat afdwingen.",
                "Natuurlijk is wat vanzelf opkomt, artificieel wat een samenleving moet inrichten. "
                "Medelijden voel je zonder afspraak; rechtvaardigheid en je woord houden vragen "
                "regels en gewoonten.",
                "Noem alle drie. Het tweede kenmerk, in je wil en niet enkel in je kunnen, sluit "
                "talent uit: goed kunnen zingen is geen deugd.",
                "Noem beide voorbeelden en het besluit erbij: waar geen bekoring is, is geen deugd "
                "nodig. Daarom staat er geen deugd op de lijst voor dingen die ons nooit moeilijk "
                "vallen.",
            ],
        ),
        dict(
            aanpak="De zorgethiek begint niet bij een regel of een som maar bij de band tussen "
                   "mensen. Houd de vier fasen in je hoofd, want daarmee kan je ook zeggen waar het "
                   "misloopt.",
            waarom=[
                "Noem het mensbeeld en het verschil met de twee andere richtingen. Dat de zorgethiek "
                "partijdig durft te zijn, is geen vergetelheid maar een keuze: deze mens in deze "
                "relatie.",
                "Noem dat de ethiek lang van een onafhankelijke burger vertrok. Wie zorgde en wie "
                "zorg nodig had, viel daarmee buiten het beeld, en dat is wat de zorgethiek "
                "rechtzet.",
                "Noem dat de maatstaf zelf eenzijdig was, niet dat meisjes anders zijn. Dat is de "
                "kern van Gilligans kritiek: ze verving de ene stem niet door de andere maar zette "
                "er een tweede naast.",
                "Vul de vier fasen aan met de houding die erbij hoort. De vierde, zorg ontvangen, is "
                "de fase die men vergeet, en net daar blijkt of je zorg aankomt zoals je bedoelde.",
                "Elk voorbeeld faalt in een andere fase. Dat is precies waarvoor de vier fasen "
                "dienen: niet om zorg te beschrijven, maar om te zien waar ze strandt.",
                "Noem wat ze gemeen hebben en waarin ze dan nog verschillen. Beide kijken voorbij "
                "de losse daad: de een naar de persoon, de ander naar de relatie.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ethiek-en-geluk-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="In de oudheid liggen vier antwoorden naast elkaar. Zoek bij elk waar het geluk "
                   "zit: in bloeien volgens de deugd, in rust, in je houding, of in loslaten. Dat "
                   "ene woord per visie houdt de hele reeks bij elkaar.",
            waarom=[
                "Eudaimonia. Het wordt vaak met geluk vertaald, maar het betekent eerder bloeien of "
                "een geslaagd leven, en dat is wat oefening 2 uitlegt.",
                "Noem dat het een manier van leven is en geen stemming. Het beeld van de ene "
                "zwaluw komt van Aristoteles zelf.",
                "Niet waar, en dit is het grootste misverstand over Epicurus. Hij raadt juist aan "
                "je verlangens te beperken; de betekenis van epicurist als levensgenieter is er "
                "later bij gekomen.",
                "Noem beide helften: wat geluk bij hem is en welke raad eruit volgt. Zijn geluk is "
                "een afwezigheid, en dat verklaart waarom hij zo weinig nodig heeft.",
                "Let op het verschil tussen de eerste en de laatste: het stoicisme werkt met je "
                "houding tegenover wat gebeurt, Aristoteles met het ontplooien van je vermogens. Dat "
                "zijn twee heel verschillende wegen.",
                "Noem dat alle drie het geluk minder van buiten laten komen. Dat is de "
                "gemeenschappelijke richting; de wegen erheen zijn verschillend, en dat mag je "
                "erbij zeggen.",
            ],
        ),
        dict(
            aanpak="De vraag van deze reeks is niet of geluk waardevol is, maar of het de maatstaf "
                   "van de moraal mag zijn. Kant zegt nee, Bentham ja, en de reden zit telkens in "
                   "wat een gebod moet kunnen.",
            waarom=[
                "Vul de tabel rij per rij in. De kern bij Kant: wat mensen gelukkig maakt "
                "verschilt, en een moreel gebod moet voor allen gelden. Daarom kan geluk bij hem "
                "geen maatstaf zijn.",
                "Noem dat wie zijn plicht doet geluk verdient, maar dat de twee niet samenvallen. "
                "Zo zie je dat Kant geluk niet veracht; hij weigert het enkel als grond van de "
                "moraal.",
                "Noem dat de som de verdeling verbergt. Dit is hetzelfde bezwaar als bij het "
                "utilitarisme in het vorige hoofdstuk, nu toegepast op geluk als cijfer.",
            ],
        ),
        dict(
            aanpak="Drie moderne stemmen: Schopenhauer die het geluk wegrelativeert, Levinas die "
                   "het buiten jezelf legt, en De Wachter die zich tegen de gelukdwang verzet.",
            waarom=[
                "Let op Levinas: bij hem is geluk geen doel maar een gevolg van je "
                "verantwoordelijkheid. Dat sluit aan bij wat hij in het vorige hoofdstuk over het "
                "gelaat zei.",
                "Noem de kringloop van verlangen en verveling. Dat is wat zijn visie pessimistisch "
                "maakt: beide uitkomsten van een verlangen vallen slecht uit.",
                "Noem beide helften: waartegen hij zich keert en waar hij het geluk wel zoekt. Zijn "
                "punt is dat de eis om gelukkig te zijn zelf ongelukkig maakt, en dat is een "
                "kritiek op onze tijd, niet op het geluk.",
                "Noem de twee vragen, want daarmee kan je de hele rij ordenen: binnen de mens of "
                "bij de ander, en wel of niet de maatstaf van de moraal.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-argumentatieleer-redeneervormen-en-drogredenen-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="In een als-dan-zin heet het eerste deel het antecedens en het tweede het "
                   "consequens. Twee bewegingen zijn geldig: het antecedens bevestigen, en het "
                   "consequens ontkennen. De twee andere zijn dat niet.",
            waarom=[
                "Vul beide delen in met hun naam. Antecedens betekent wat voorafgaat, consequens "
                "wat volgt; het staat in de woorden zelf.",
                "Let op het patroon: de eerste en de vierde zijn geldig, de tweede en de derde "
                "niet. Dat zijn precies de twee geldige bewegingen uit de aanpak hierboven.",
                "Modus ponens, van ponere, plaatsen of stellen. Je stelt het antecedens en trekt "
                "het consequens.",
                "Modus tollens, van tollere, wegnemen. Je neemt het consequens weg en daarmee valt "
                "ook het antecedens.",
                "Noem de schoonmaakwagen of een andere oorzaak. De kern: hetzelfde gevolg kan meer "
                "dan één oorzaak hebben, en daarom mag je niet terugrekenen.",
                "Noem dat het gevolg er ook zonder die voorwaarde kan zijn. Dit en de vorige "
                "oefening zijn twee kanten van dezelfde fout: de als-dan-zin wordt als een "
                "gelijkheid gelezen.",
            ],
        ),
        dict(
            aanpak="Houd twee dingen uit elkaar: een geldige vorm en een waar besluit. Geldig gaat "
                   "over de stap van premissen naar besluit, waar over de inhoud.",
            waarom=[
                "Let op de tweede en de derde: ook een rammelende redenering kan bij een juist "
                "besluit uitkomen. Ze bewijst het dan enkel niet, en dat is een belangrijk "
                "verschil.",
                "Noem de formule: als de premissen waar zijn, moet het besluit waar zijn. Dat moet "
                "is het hele begrip geldigheid.",
                "Noem welke premisse onwaar is en zeg wat er met de geldigheid gebeurt. Dat een "
                "redenering geldig blijft met een onware premisse, is precies waarom je altijd "
                "beide moet nakijken.",
            ],
        ),
        dict(
            aanpak="Een drogreden is een stap die lijkt te kloppen en het niet doet. Vraag je bij "
                   "elk voorbeeld af: wordt hier iets over de zaak gezegd, of over iets anders, de "
                   "persoon, de massa, de natuur?",
            waarom=[
                "Let op de stroman: de tegenstander krijgt een standpunt in de mond dat hij niet "
                "innam, en dat wordt dan weerlegd. En op het hellend vlak: een reeks stappen wordt "
                "als onvermijdelijk voorgesteld zonder dat te onderbouwen.",
                "Let op de onbevoegde autoriteit: naar een kenner verwijzen is redelijk, naar "
                "iemand met gezag op een ánder gebied niet. En op de overhaaste generalisatie: dat "
                "is de inductie uit het hoofdstuk over kennis, maar met veel te weinig gevallen.",
                "Noem dat het van is naar ought springt. En noem een tegenvoorbeeld zoals gif of "
                "een ziekte, want daarmee valt het argument meteen om.",
                "Noem dat je de stap benoemt en niet de persoon. En noem de nuance erbij: een "
                "drogreden weerleggen betekent niet dat het besluit fout is, enkel dat dit argument "
                "het niet steunt.",
                "Niet waar. Vaak gebruikt iemand een drogreden zonder het te merken, omdat ze goed "
                "klinkt. Daarom is ze benoemen nuttiger dan iemand van oneerlijkheid verdenken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-democratische-rechtsstaat-en-haar-principes-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Houd twee begrippen scherp uit elkaar: democratie gaat over wie beslist, "
                   "rechtsstaat over of de macht zelf aan regels gebonden is. Daarmee kan je deze "
                   "hele reeks ordenen.",
            waarom=[
                "Noem uitdrukkelijk dat ook de overheid eraan gebonden is. Dat laatste is het hele "
                "punt: dat er wetten zijn, heeft elke staat.",
                "Noem van elke kant een voorbeeld, zonder een land te hoeven noemen: een bestuur "
                "dat netjes zijn eigen wetten volgt zonder verkiezingen, en een verkozen bestuur "
                "dat zich daarna aan geen rechter stoort.",
                "De Verlichting, de achttiende eeuw. Dat is dezelfde periode als Montesquieu uit "
                "het volgende hoofdstuk.",
                "Noem de drie waarden en waar je ze terugvindt. Dat ze zowel in de grondwet als in "
                "de mensenrechten staan, laat zien dat ze niet van één land zijn.",
            ],
        ),
        dict(
            aanpak="De vijf principes zijn geen lijstje maar een bouwwerk: elk principe vangt een "
                   "zwakte van de andere op. Leer ze dus met de vraag erbij: waartegen beschermt "
                   "dit?",
            waarom=[
                "Vul de tabel rij per rij in. Let op de rij over de grondwet: ze is niet enkel de "
                "hoogste wet, ze bakent ook af wat de macht mag, en dat is wat oefening 8 uitlegt.",
                "Geef twee voorbeelden waarin één principe wegvalt. Dat is de beste manier om te "
                "zien waarvoor een principe dient: kijk wat er zonder gebeurt.",
                "Noem de keerzijde en wat ze opvangt. Dat grondrechten de meerderheid beperken, is "
                "geen gebrek aan democratie maar de reden dat een democratie houdbaar blijft.",
                "Noem dat ze de spelregels vastlegt waaraan de wetgever zelf gebonden is. Daarom "
                "vraagt een grondwetswijziging in Belgie een bijzondere meerderheid en verkiezingen "
                "ertussen.",
                "Niet waar. De grondwet bevat de grondregels: de rechten, de instellingen en hun "
                "bevoegdheden. De gewone wetten, decreten en besluiten staan eronder en moeten "
                "ermee kloppen.",
            ],
        ),
        dict(
            aanpak="Hier gaat het over hoe rechten echt iets waard worden. Twee woorden om niet te "
                   "verwisselen: onafhankelijk gaat over druk van buiten, onpartijdig over een band "
                   "met de zaak zelf.",
            waarom=[
                "Noem de drie voorwaarden. Dat een beperking door een rechter te toetsen moet zijn, "
                "is de voorwaarde die men vergeet en net de belangrijkste.",
                "Noem dat je zonder dat recht je andere rechten niet kan verdedigen. Daarom heet "
                "het ook een procedureel recht: het is het recht om je rechten te halen.",
                "Let op het verschil: druk van een minister of van het parlement raakt de "
                "onafhankelijkheid, een band met een partij in de zaak raakt de onpartijdigheid.",
                "Noem dat niemand hem kan voorschrijven hoe hij de wet toepast. Onafhankelijk "
                "betekent dus niet vrij van de wet, en dat is precies de verwarring die de vraag "
                "wil uitsluiten.",
                "Noem dat de schijn al genoeg is. Een proces moet niet enkel eerlijk zijn maar ook "
                "eerlijk lijken, en daarom bestaat de mogelijkheid tot wraking.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-scheiding-der-machten-en-de-rechterlijke-macht-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Drie machten, drie werkwoorden: maken, uitvoeren en toepassen op een concreet "
                   "geval. Hang aan elk werkwoord zijn instelling, dan ligt de hele reeks vast.",
            waarom=[
                "Vul de tabel rij per rij in: wie het is en wat ze doet. Let op de rij van de "
                "wetgevende macht: die maakt niet enkel wetten, ze controleert ook de regering, en "
                "dat komt in reeks 2 terug.",
                "Montesquieu, in De l'esprit des lois. Hij verwoordde het als eerste scherp, al "
                "bouwde hij op wat Locke eerder schreef.",
                "Noem dat macht die zichzelf controleert, niets controleert. Dat is het argument in "
                "één zin, en alles in dit hoofdstuk volgt eruit.",
                "Niet waar. De rem is bedoeld: snelheid is niet het doel, maar wel dat niemand "
                "alleen kan beslissen. Dat traagheid soms ergert, hoort bij de prijs.",
                "Noem dat de machten elkaar juist in het oog houden. Daarom spreekt men ook van "
                "controle en evenwicht, en niet van drie eilanden.",
                "Meerdere: naast het federale parlement hebben de gemeenschappen en de gewesten "
                "elk hun eigen parlement, elk met eigen bevoegdheden.",
            ],
        ),
        dict(
            aanpak="Controle en evenwicht betekent dat elke macht middelen heeft om de andere "
                   "binnen hun grenzen te houden. Zoek bij elke instelling dus wie ze controleert "
                   "en waarop.",
            waarom=[
                "Let op het verschil tussen de eerste twee: het Grondwettelijk Hof toetst wetten "
                "aan de grondwet, de Raad van State kijkt beslissingen van het bestuur na. Wetten "
                "tegenover bestuursdaden, dat is de scheidslijn.",
                "Noem de begroting en zeg waarom ze zo sterk is. Zonder geld en zonder wetten kan "
                "een regering niets, en daarom valt een regering in de praktijk op een begroting.",
                "Noem ook wat het niet betekent, want dat is uitdrukkelijk gevraagd. Evenwicht gaat "
                "over wederzijdse rem, niet over gelijke grootte.",
            ],
        ),
        dict(
            aanpak="De rechterlijke macht is de zwakste van de drie: ze heeft geen leger en geen "
                   "geld. Daarom is ze met waarborgen omringd. Vraag je bij elke waarborg af "
                   "waartegen ze beschermt.",
            waarom=[
                "Noem dat een rechter die stemmen moet halen, afhankelijk wordt van wat populair "
                "is. In Belgie benoemt de Koning op voordracht van de Hoge Raad voor de Justitie, "
                "die op bekwaamheid selecteert.",
                "Noem dat wie niet afgezet kan worden, onbevangen kan oordelen. Dat is dezelfde "
                "reden waarom ook de wedde van een rechter beschermd is.",
                "Noem dat een gemotiveerd vonnis te controleren en aan te vechten is. De "
                "motiveringsplicht is dus niet beleefdheid maar een voorwaarde voor beroep.",
                "De dienst, nooit het vonnis. Hij zorgt voor gebouwen, personeel en middelen, en "
                "blijft met zijn handen van de uitspraak.",
                "Let op de laatste: een nieuwe algemene wet is precies het werk van het parlement, "
                "en dus geen schending. Het verschil met de tweede is het woord algemeen, en dat is "
                "wat oefening 15 uitlegt.",
                "Noem dat een wet algemeen moet zijn. Wie voor één zaak wetgeeft, spreekt in feite "
                "recht, en dat verklaart ook waarom dit in het Europees Hof al meermaals is "
                "aangevochten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-functies-van-justitie-de-rechtspraak-en-de-deontologie-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk voorbeeld af wat justitie hier eigenlijk doet: iemand "
                   "beschermen, een geschil beslechten, de orde herstellen, straffen, of "
                   "voorkomen. Dat zijn de vijf functies.",
            waarom=[
                "Let op het verschil tussen veiligheid en ordehandhaving: veiligheid richt zich op "
                "een bepaalde persoon die bedreigd wordt, ordehandhaving op de samenleving als "
                "geheel.",
                "Vijf: veiligheid, conflictbeslechting, ordehandhaving, bestraffing en preventie. "
                "Die vijfde komt in geen enkel voorbeeld van reeks 1 voor, en dat is precies het "
                "punt van oefening 3.",
                "Noem dat wat niet gebeurt, niemand opvalt. Daarom wordt preventie ook het "
                "makkelijkst weggesneden als er bespaard moet worden.",
                "Noem het burgerlijk recht en waarom de functie nodig is. Zonder iemand die een "
                "geschil kan afsluiten, blijft het duren of eindigt het met geweld, en dat is het "
                "beeld van een samenleving zonder rechter.",
                "Niet waar. De vijf functies staan naast elkaar en niet in een rangorde; "
                "bestraffing valt enkel het meest op in het nieuws.",
            ],
        ),
        dict(
            aanpak="Vier principes die van een proces een eerlijk proces maken. Zet er bij elk de "
                   "vraag bij: wat zou er gebeuren als dit principe wegviel?",
            waarom=[
                "Vul de tabel rij per rij in. Let op de rij van het vermoeden van onschuld: ze "
                "bestaat uit drie delen, en het derde, twijfel in jouw voordeel, is het stuk dat "
                "men vergeet.",
                "Noem een voorbeeld, want dat is gevraagd. Dat de jeugdrechtbank niet openbaar "
                "zit, is het duidelijkste geval, en het laat zien dat openbaarheid een beginsel is "
                "met uitzonderingen.",
                "Noem dat het oordeel al valt voor de rechter iets vaststelde. Dit komt in het "
                "volgende hoofdstuk terug als een botsing van twee grondrechten.",
            ],
        ),
        dict(
            aanpak="Deontologie is de beroepsethiek: regels die een beroepsgroep zichzelf oplegt, "
                   "naast de wet. Houd daarbij drie plichten uit elkaar: zwijgen over wat in "
                   "vertrouwen gezegd is, terughoudend zijn over je werk, en spreken bij gevaar.",
            waarom=[
                "Vul de tabel rij per rij in: van wie ze komt, voor wie ze geldt en wie straft. "
                "Dat de sanctie van de beroepsorde komt en niet van een rechter, is het "
                "duidelijkste verschil.",
                "Niet waar, en dit is de kern: een code komt bóven de wet en niet in de plaats van "
                "de wet. Wie zijn code volgt maar de wet overtreedt, is nog altijd strafbaar.",
                "Let op het verschil tussen beroepsgeheim en discretieplicht: het eerste gaat over "
                "wat iemand je toevertrouwt, het tweede over alles wat je op je werk verneemt. Het "
                "tweede is ruimer maar minder zwaar.",
                "Noem dat het de hulpvrager beschermt. Dat is de belangrijkste nuance van het hele "
                "hoofdstuk: het beroepsgeheim is geen voorrecht van de hulpverlener.",
                "Let op het verschil in dreiging: bij ernstig en dreigend gevaar mag en moet je "
                "spreken, bij een praatje op een feestje gaat het om terughoudendheid.",
                "Noem beide redenen: herkenbaar zonder naam, en het vertrouwen dat je verliest bij "
                "wie het hoort. Dat tweede is de reden waarom zo'n verhaal ook schade doet als "
                "niemand de persoon kent.",
                "Noem dat plichten tegen elkaar in kunnen gaan. Zwijgen en melden botsen in "
                "dezelfde casus, en dan heb je een afweging nodig in plaats van een regel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-actuele-thema-s-binnen-recht-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Het schema geeft je drie niveaus: beschrijven, verklaren en evalueren. Werk ze "
                   "in die orde af, want je kan niets verklaren wat je niet eerst beschreven hebt.",
            waarom=[
                "Vul de drie niveaus aan. Let op de derde rij: ook de ongewenste gevolgen benoemen "
                "hoort erbij, en dat is precies wat oefening 4 uitlegt.",
                "Noem alle vijf. Een goede oefening: neem één thema en zoek bij elke invalshoek één "
                "zin, dan merk je welke invalshoek je vanzelf vergeet.",
                "Noem de drie elementen: meerdere bronnen, betrouwbare en valide data, en onderzoek "
                "om je uitspraken te steunen. Een mening met één bron is geen redeneren met bewijs.",
                "Noem dat elke oplossing een prijs heeft. Wie ze zelf benoemt, neemt het argument "
                "van de tegenpartij weg; wie ze verzwijgt, laat het klaarliggen.",
            ],
        ),
        dict(
            aanpak="Drie discussies rond het proces: de volksjury, de procedurefout en de pers. "
                   "Bij elk hoort een botsing tussen twee goede dingen, en dat is wat de discussie "
                   "levend houdt.",
            waarom=[
                "Twaalf, bij lot aangewezen uit de kiezerslijsten. Dat lot is geen gemakkigheid "
                "maar het principe: zo kan niemand de samenstelling kiezen.",
                "Geef één argument van elke kant, zoals gevraagd. Dat assisen zwaar weegt op de "
                "juryleden, is een argument dat men vaak vergeet omdat het niet over de beklaagde "
                "gaat.",
                "Noem beide helften: waarvoor de vormregels dienen en waarom het toch onrecht "
                "voelt. Beide kanten erkennen is hier het hele antwoord, en dat is het schema uit "
                "reeks 1 in de praktijk.",
                "Het vermoeden van onschuld tegenover de persvrijheid. Twee grondrechten, en "
                "daarom is het geen kwestie van goed tegen slecht maar van afwegen.",
                "Noem alle drie. Dat moeilijke taal erbij staat, is de reden dat justitie werkt aan "
                "begrijpelijke vonnissen en aan uitleg bij een uitspraak.",
            ],
        ),
        dict(
            aanpak="Bij straf en strafuitvoering is de kernvraag altijd dezelfde: waarvoor dient "
                   "deze maatregel, vergelden, beschermen of herval voorkomen? Daarmee kan je elke "
                   "oefening in deze reeks beantwoorden.",
            waarom=[
                "Let op het verschil tussen de laatste twee: transitie- en detentiehuizen zijn een "
                "vorm van straf uitvoeren, internering is een maatregel en geen straf. Dat verschil "
                "legt oefening 13 uit.",
                "Noem huis, werk en gezin in één zin. Dat is het argument in zijn kortste vorm, en "
                "het gaat over herval en niet over mildheid.",
                "Geef één argument van elke kant. Let erop dat beide kanten zich op cijfers "
                "beroepen, en dat is precies waarom redeneren met bewijs uit reeks 1 hier nodig is.",
                "Noem dat een straf schuld veronderstelt en een maatregel niet. Zo zie je dat het "
                "hoofdstuk over de vrije wil geen theorie was: het zit in onze wetgeving.",
                "Zestien jaar. Uithandengeving betekent dat een minderjarige niet door de "
                "jeugdrechter maar als een meerderjarige behandeld wordt, en dat blijft een "
                "uitzondering.",
                "Noem dat bewijs verdwijnt en getuigen vergeten. Voor de zwaarste misdrijven heeft "
                "de wetgever de verjaring afgeschaft, omdat het belang van vervolging daar zwaarder "
                "weegt.",
                "Niet waar. Een justitiehuis is de plaats waar justitieassistenten werken, met "
                "onder meer begeleiding en slachtofferonthaal; een transitiehuis is kleinschalige "
                "detentie gericht op de terugkeer na de straf.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-buitengerechtelijke-procedures-en-juridische-bijstand-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag ordent dit hele hoofdstuk: wie beslist uiteindelijk? Bij bemiddeling "
                   "en verzoening de partijen zelf, bij arbitrage een derde die ze samen kozen, bij "
                   "een proces een rechter die ze niet kozen.",
            waarom=[
                "Vul de drie rijen in en let op de laatste: bij arbitrage geeft men de beslissing "
                "wél uit handen. Dat is waarom arbitrage dichter bij een proces staat dan bij "
                "bemiddeling.",
                "Buiten de rechtbank om. Het woord zegt niet dat het geen juridische waarde heeft: "
                "een bemiddelingsakkoord kan door een rechter bekrachtigd worden.",
                "Noem de vraag wie beslist en pas ze op de drie toe. Met die ene vraag kan je ze "
                "altijd uit elkaar houden, ook als je de namen even kwijt bent.",
            ],
        ),
        dict(
            aanpak="Bij bemiddeling gaan de voordelen en de keerzijde over hetzelfde: de partijen "
                   "houden het in eigen hand. Dat maakt ze sneller en zachter, maar ook afhankelijk "
                   "van hun bereidheid.",
            waarom=[
                "Noem alle vier. Dat vertrouwelijkheid erbij staat, is een echt verschil met een "
                "proces: een zitting is in beginsel openbaar en een vonnis is dat ook.",
                "Noem twee voorbeelden, want dat is gevraagd. De kern: een vonnis maakt een "
                "winnaar en een verliezer, en dat is lastig als je daarna nog met elkaar verder "
                "moet.",
                "Noem beide helften, de keerzijde en wat er bij mislukking gebeurt. Dat je je recht "
                "om te procederen niet verliest, is wat bemiddeling zo weinig riskant maakt.",
                "Niet waar. Ook tijdens een lopende procedure kan een rechter de partijen naar "
                "bemiddeling sturen, en soms gebeurt dat op zijn voorstel.",
            ],
        ),
        dict(
            aanpak="Juridische bijstand bestaat in twee lijnen: een kort eerste advies voor "
                   "iedereen, en een advocaat die je dossier opneemt als je inkomen laag genoeg is. "
                   "Houd daarbij de adressen uit elkaar aan wat ze doen.",
            waarom=[
                "Vul de tabel rij per rij in: wat je krijgt, hoe lang, en voor wie. Het verschil "
                "zit vooral in de duur: een gesprek tegenover je hele zaak.",
                "Een pro deo advocaat. De officiële naam is juridische tweedelijnsbijstand, en in "
                "de wet heet de advocaat dan aangestelde of toegevoegde advocaat.",
                "Noem dat het een recht is en geen gunst. En noem dat de overheid de advocaat "
                "vergoedt, want dat verklaart waarom het geen liefdadigheid is.",
                "Noem dat gelijkheid voor de wet anders van je bankrekening zou afhangen. Dat is "
                "het argument in één zin, en het verbindt dit hoofdstuk met de principes van de "
                "rechtsstaat.",
                "Let op het verschil tussen de wetswinkel en het Bureau voor Juridische Bijstand: "
                "de eerste geeft een eerste advies, het tweede stelt een advocaat aan. En het CAW "
                "is geen juridisch adres maar hulpverlening.",
                "Noem bemiddeling en waarom. Dit is dezelfde reden als bij oefening 5: ze blijven "
                "buren, dus de verhouding na de ruzie weegt mee.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-gerechtelijke-piramide-rechtbanken-en-hoven-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Om te weten waar een zaak thuishoort, heb je twee vragen nodig: waarover gaat "
                   "het (materieel) en waar is het gebeurd of waar woont de verweerder "
                   "(territoriaal). Beide moeten kloppen.",
            waarom=[
                "Materieel gaat over het soort zaak en het bedrag, territoriaal over de plaats. De "
                "eerste vraag kiest de soort rechtbank, de tweede welke van die rechtbanken in het "
                "land.",
                "Pas beide vragen toe, zoals gevraagd. Onder 5.000 euro is het vredegerecht "
                "bevoegd, en het kanton volgt uit de woonplaats.",
            ],
        ),
        dict(
            aanpak="Elke rechtbank heeft haar eigen soort zaken. Leer ze aan één sleutelwoord: "
                   "huur en kleine geschillen, verkeer, werk, onderneming, familie, misdrijven en "
                   "minderjarigen.",
            waarom=[
                "Let op de politierechtbank: ondanks haar naam gaat ze over verkeer en lichte "
                "overtredingen, niet over de politie. Dat is de valkuil van deze reeks.",
                "Let op het verschil tussen de jeugdrechtbank en de correctionele rechtbank: de "
                "leeftijd beslist, niet de ernst. En op de arbeidsrechtbank, die zowel over ontslag "
                "als over uitkeringen gaat.",
                "Vijfduizend euro. Daarboven gaat een burgerlijke zaak naar de rechtbank van eerste "
                "aanleg.",
                "Noem alle vijf. Dat de strafuitvoeringsrechtbank erbij staat, is logisch zodra je "
                "het hoofdstuk over straf gelezen hebt: ook het verloop van een straf wordt door "
                "een rechter bewaakt.",
                "Niet waar. De jeugdrechtbank zit niet openbaar, om het kind te beschermen. Dat is "
                "de uitzondering op de openbaarheid uit het hoofdstuk over de rechtspraak.",
            ],
        ),
        dict(
            aanpak="De piramide heeft drie verdiepingen: eerst de feiten, dan een tweede volledige "
                   "behandeling, dan enkel nog het recht. Houd dat laatste goed vast, want daar "
                   "zitten de meeste fouten.",
            waarom=[
                "Let op het Hof van Cassatie: het is geen derde beroep. Het kijkt niet naar de "
                "feiten en spreekt geen nieuw oordeel over de zaak uit.",
                "Noem beide en vooral dat cassatie de zaak terugstuurt. Daarom zegt men dat "
                "cassatie een uitspraak verbreekt en niet hervormt.",
                "Vul de drie trappen in. Let op de laatste regel: enkel over de toepassing van het "
                "recht, en dat is dezelfde grens als in oefening 9.",
                "Een rechtbank spreekt een vonnis uit, een hof een arrest. Een handig steuntje: hof "
                "en arrest hebben beide iets plechtigs.",
                "Noem dat een rechter zich kan vergissen. En noem dat het een waarborg is, geen "
                "vertragingstruc, want dat is wat de vraag met twee instanties bedoelt.",
                "Noem dat het vonnis definitief wordt, ook als het fout was. Daarom is de termijn "
                "zelf een van de eerste dingen die een advocaat nakijkt.",
                "Het Grondwettelijk Hof en de Raad van State. Ze staan naast de piramide omdat ze "
                "geen gewone geschillen beslechten: het ene toetst wetten aan de grondwet, het "
                "andere beslissingen van het bestuur.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-burgerlijk-recht-en-strafrecht-het-verloop-van-een-procedure-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke zaak af wie er tegenover wie staat. Twee particulieren met "
                   "een geschil is burgerlijk recht; de samenleving tegenover iemand die de wet "
                   "overtrad, is strafrecht.",
            waarom=[
                "Vul de tabel rij per rij in en let op de rij over wie de zaak start: een "
                "particulier tegenover het openbaar ministerie. Dat is het duidelijkste verschil "
                "tussen de twee takken.",
                "Let op het patroon: geld en familie bij het burgerlijk recht, verkeer en diefstal "
                "bij het strafrecht. Dat is geen toeval: het strafrecht gaat over wat de wet "
                "strafbaar stelt.",
                "Noem de vechtpartij in beide takken én de burgerlijke partijstelling. Dat laatste "
                "is het praktische stuk: het spaart het slachtoffer een tweede procedure.",
            ],
        ),
        dict(
            aanpak="Een burgerlijke procedure heeft vijf stappen: inleiden, stukken uitwisselen, "
                   "pleiten, vonnis, uitvoering. Onthoud dat de laatste stap erbij hoort, want een "
                   "vonnis dat niet uitgevoerd wordt, helpt niemand.",
            waarom=[
                "Vul de vijf stappen in. Let erop dat de uitvoering de laatste is en niet "
                "vanzelfsprekend: daarvoor is soms opnieuw een deurwaarder nodig.",
                "Hoor en wederhoor: elke partij mag op de argumenten van de andere antwoorden. Dat "
                "is hetzelfde principe als in het hoofdstuk over de rechtspraak.",
                "Noem dat de partijen met elkaar verder moeten. Dat is dezelfde reden als bij de "
                "buren uit het hoofdstuk over bemiddeling.",
                "Niet waar. Veel zaken eindigen met een akkoord tussen de partijen, soms tijdens de "
                "procedure zelf, en dan komt er geen vonnis.",
            ],
        ),
        dict(
            aanpak="Volg de weg van een strafzaak in de orde waarin ze loopt: een feit, een "
                   "proces-verbaal, een vooronderzoek, een beslissing van het parket, en pas "
                   "daarna een proces. Dan vallen alle termen op hun plaats.",
            waarom=[
                "Noem dat de wet het strafbaar moet stellen. Zonder strafwet is er geen misdrijf, "
                "hoe verwerpelijk het gedrag ook is, en dat is het legaliteitsbeginsel.",
                "Een proces-verbaal, kortweg pv. Het is geen vonnis en geen beschuldiging, enkel "
                "een vaststelling op papier.",
                "Vul beide rijen in: wie leidt het en wanneer. De kern van de laatste kolom: een "
                "huiszoeking of een aanhouding snijdt diep in iemands rechten, dus moet een "
                "onafhankelijke rechter beslissen.",
                "Noem alle drie. Dat seponeren erbij hoort, verklaart waarom veel aangiftes nooit "
                "bij een rechter komen.",
                "Noem dat een vrijspraak van een rechter komt. Dat verschil is belangrijk voor een "
                "slachtoffer: bij een sepot is er geen uitspraak over schuld, in geen van beide "
                "richtingen.",
                "De raadkamer beslist, de kamer van inbeschuldigingstelling behandelt het beroep. "
                "Een steuntje: de tweede naam hoort bij het hof van beroep, en klinkt ook "
                "zwaarder.",
                "Het onderzoek ter terechtzitting. Let op het verschil met het vooronderzoek: dat "
                "is niet openbaar, dit wel, en dat is precies het moment waarop de openbaarheid "
                "speelt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-juridische-termen-en-actoren-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="De naam van een partij hangt af van twee dingen: in welke tak je zit, en hoe "
                   "ver de zaak staat. Eiser en verweerder horen bij een burgerlijke zaak, "
                   "verdachte en beklaagde bij een strafzaak.",
            waarom=[
                "Let op het verschil tussen verdachte en beklaagde: dezelfde persoon, een andere "
                "fase. Verdachte tijdens het vooronderzoek, beklaagde zodra hij voor de rechter "
                "staat.",
                "De burgerlijke partij. Zo hoeft het slachtoffer geen tweede, burgerlijke "
                "procedure te starten, en dat is wat in het vorige hoofdstuk met de vechtpartij "
                "werd uitgelegd.",
                "De beschuldigde. Drie namen voor dezelfde rol dus, elk in een andere fase of voor "
                "een ander rechtscollege: verdachte, beklaagde, beschuldigde.",
                "Noem het vermoeden van onschuld. Dat is niet alleen een juridisch punt maar ook "
                "een taalkundig: wie in de krant dader schrijft waar verdachte hoort, velt het "
                "oordeel zelf.",
            ],
        ),
        dict(
            aanpak="Zet de mensen van justitie op een rij naar hun rol: vervolgen, onderzoeken, "
                   "optekenen, betekenen en uitvoeren, verdedigen, en oordelen. Elk heeft precies "
                   "één rol, en die rollen mogen niet door elkaar lopen.",
            waarom=[
                "Let op de gerechtsdeurwaarder: hij staat aan het begin én het einde van een zaak, "
                "want hij betekent de dagvaarding en voert het vonnis uit.",
                "De procureur, met zijn substituten. Bij een hof van beroep heet hij de "
                "procureur-generaal.",
                "Noem dat hij rechter is en geen vervolger. Dat hij ook het ontlastende bewijs moet "
                "zoeken, is het stuk dat men vergeet, en net dat maakt zijn rol bijzonder.",
                "Waar. De griffier maakt de zitting rechtsgeldig en houdt het dossier bij; zonder "
                "hem kan een zaak niet doorgaan. Zijn werk valt niet op en is onmisbaar.",
                "Noem het beroepsgeheim en de deontologie van de balie. Dat sluit aan bij het "
                "hoofdstuk over deontologie: een code naast de wet, met de orde als tuchtinstantie.",
            ],
        ),
        dict(
            aanpak="Deze woorden komen allemaal in een brief of een dossier voor. Leer ze aan wat "
                   "ze met je dóen: je uitnodigen, je zaak opnieuw laten bekijken, je zaak zonder "
                   "gevolg laten.",
            waarom=[
                "Let op het verschil tussen beroep en cassatie: opnieuw behandelen tegenover enkel "
                "nakijken of het recht juist is toegepast. Dat is dezelfde grens als in het "
                "hoofdstuk over de piramide.",
                "Let op seponeren en de minnelijke schikking: in beide gevallen komt er geen "
                "vonnis, maar bij een schikking is er wel een afspraak en meestal een betaling.",
                "Noem de brief en de termijn. Dat moeilijke taal meespeelt in de kloof tussen "
                "burger en justitie, is hetzelfde punt als in het hoofdstuk over actuele thema's.",
            ],
        ),
    ],
)

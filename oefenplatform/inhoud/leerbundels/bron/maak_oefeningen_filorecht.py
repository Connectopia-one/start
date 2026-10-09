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
                 ("open", "Leg uit wat Sartre bedoelt met de existentie gaat aan de essentie voorbij. "
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

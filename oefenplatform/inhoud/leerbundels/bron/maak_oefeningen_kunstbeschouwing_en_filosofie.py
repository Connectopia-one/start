# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij kunstbeschouwing en filosofie 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: stellingen om
te wegen, begrippen om toe te passen op een eigen voorbeeld, en redeneringen om
uit te schrijven. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-doorstroom/kunstbeschouwing-en-filosofie.json` en naast
`maak_kunstbeschouwing_en_filosofie.py`.

Een kunstwerk wordt hier beschreven in woorden en nooit afgebeeld: we hebben de
rechten op die afbeeldingen niet.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Kunstbeschouwing en filosofie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
NIVEAU = "-boost-doorstroom"
VOOR = "oefenbundel-"

W = "120px"
WW = "200px"
WL = "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een filosofische vraag telt de redenering, niet het aantal woorden.",
    "Schrijf bij een mening altijd je argument erbij.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("kunst-als-deel-van-een-cultuur",
    titel="Kunst als deel van een cultuur",
    reeksen=[
        dict(kop="Wat doet kunst in een samenleving?",
             opdracht="Schrijf bij elk voorbeeld welke functie van kunst je herkent.",
             oefeningen=[
                 ("rij", [("een glasraam dat het bijbelverhaal vertelt aan wie niet kan lezen",
                           "een religieuze en verhalende functie"),
                          ("een standbeeld van een vorst op het marktplein",
                           "een machtsfunctie"),
                          ("een affiche die oproept om te stemmen", "een politieke functie"),
                          ("een lied dat je zingt op een trouwfeest", "een rituele functie"),
                          ("een schilderij dat alleen mooi wil zijn", "een esthetische functie"),
                          ("een installatie die je doet nadenken over afval",
                           "een kritische functie")],
                  "Welke functie is dit?", WL),
                 ("open", "Waarom zegt men dat kunst nooit los staat van haar tijd?",
                  "Een kunstenaar werkt met de middelen, de opdrachtgevers, de geloofswereld en "
                  "de vragen van zijn eigen tijd. Wat hij maakt is daar een antwoord op, ook "
                  "als hij zich ertegen afzet.", 4),
             ]),
        dict(kop="Wie bepaalt wat kunst is?",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Een urinoir in een museum: kunst of niet? Geef één argument voor en "
                          "één tegen.",
                  "Voor: de kunstenaar kiest het voorwerp, geeft het een nieuwe plaats en dwingt "
                  "je na te denken over wat kunst is; dat is een artistieke daad. Tegen: er is "
                  "geen vakmanschap aan te pas gekomen en het voorwerp bestond al, dus er is "
                  "niets gemaakt.", 5),
                 ("open", "Welke rol spelen musea, critici en veilinghuizen in wat als kunst "
                          "geldt?",
                  "Zij beslissen wat getoond, besproken en verkocht wordt, en bepalen daarmee "
                  "mee wat de samenleving als kunst erkent. Dat is geen eigenschap van het werk "
                  "zelf maar een oordeel van instellingen.", 4),
                 ("waar", "Of iets kunst is, kan je objectief meten.", False),
             ]),
        dict(kop="Kunst en macht",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een heerser laat een reusachtig ruiterstandbeeld van zichzelf "
                  "oprichten op het plein voor het parlement. Het beeld staat op een hoge "
                  "sokkel; de heerser kijkt in de verte en houdt een opgeheven arm.</em></p>"),
                 ("open", "Welke boodschap draagt de vorm van dit beeld? Noem drie middelen.",
                  "De grootte en de sokkel zetten hem letterlijk boven de toeschouwer; het paard "
                  "toont macht en overwinning; de blik in de verte maakt van hem een leider met "
                  "een plan.", 4),
                 ("open", "Waarom staat het beeld juist voor het parlement?",
                  "De plaats laat zien dat zijn gezag boven of naast dat van de volksvertegen"
                  "woordiging staat; de context is een deel van de boodschap.", 3),
                 ("open", "Jaren later wordt het beeld weggehaald. Wat zegt dat over de "
                          "verhouding tussen kunst en macht?",
                  "Dat kunst in de openbare ruimte meeverandert met wie de macht heeft: een "
                  "beeld blijft staan zolang de boodschap gedragen wordt.", 3),
             ]),
    ])


# ============================================================
zet("de-kunstvormen",
    titel="De kunstvormen",
    reeksen=[
        dict(kop="Indelen",
             opdracht="Zet elke kunstvorm in de juiste kolom.",
             oefeningen=[
                 ("tabel", ["kunstvorm", "ruimtelijk, tijdelijk of allebei"],
                  [["schilderkunst", None], ["muziek", None], ["dans", None],
                   ["architectuur", None], ["film", None], ["beeldhouwkunst", None]],
                  "schilderkunst: ruimtelijk · muziek: tijdelijk · dans: allebei · "
                  "architectuur: ruimtelijk · film: allebei · beeldhouwkunst: ruimtelijk",
                  "190px"),
                 ("open", "Leg het verschil uit tussen een ruimtelijke en een tijdelijke "
                          "kunstvorm.",
                  "Een ruimtelijke kunstvorm staat er in zijn geheel en jij bepaalt hoe lang je "
                  "kijkt. Een tijdelijke kunstvorm ontvouwt zich in de tijd en het werk bepaalt "
                  "het tempo.", 3),
             ]),
        dict(kop="De middelen van elke kunstvorm",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("schilderkunst", "lijn, kleur, vlak, licht, compositie"),
                          ("beeldhouwkunst", "volume, materiaal, textuur, standpunt"),
                          ("architectuur", "ruimte, constructie, licht, materiaal"),
                          ("muziek", "melodie, ritme, klankkleur, dynamiek"),
                          ("dans", "beweging, ruimte, tijd, kracht"),
                          ("film", "beeld, montage, geluid, cameravoering")],
                  "Met welke middelen werkt deze kunstvorm?", WL),
                 ("open", "Waarom noemt men architectuur een kunst én een techniek?",
                  "Een gebouw moet tegelijk mooi zijn en blijven staan, en het moet werken voor "
                  "wie erin woont. De vorm hangt dus vast aan constructie, materiaal en "
                  "gebruik.", 4),
             ]),
        dict(kop="Kijken en beschrijven",
             opdracht="Lees de beschrijving en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een schilderij toont een kamer met één raam links. Het licht valt "
                  "schuin binnen op een vrouw die aan een tafel een brief leest. De rest van de "
                  "kamer ligt in halfschaduw. De vrouw staat niet in het midden maar iets naar "
                  "rechts; voor haar op tafel ligt een opengevouwen kaart.</em></p>"),
                 ("open", "Beschrijf de compositie in twee zinnen.",
                  "Het licht komt van links en leidt je oog naar de vrouw, die iets uit het "
                  "midden staat. De donkere omgeving sluit de rest af, zodat alleen zij en de "
                  "brief overblijven.", 3),
                 ("open", "Wat doet het licht met de betekenis?",
                  "Het licht zondert haar af en maakt van het lezen een stil, bijna plechtig "
                  "moment; wat in de schaduw ligt, doet er even niet toe.", 3),
                 ("open", "Welke vraag zou je stellen om van beschrijven naar interpreteren te "
                          "gaan?",
                  "Bijvoorbeeld: waarom ligt die kaart daar? Wat zegt dat over wie de brief "
                  "schreef en hoe ver die persoon is?", 3),
                 ("waar", "Beschrijven en interpreteren zijn hetzelfde.", False),
             ]),
    ])


# ============================================================
zet("kunst-van-de-prehistorie-tot-de-middeleeuwen",
    titel="Kunst van de prehistorie tot de middeleeuwen",
    reeksen=[
        dict(kop="Zet op volgorde",
             opdracht="Nummer van oud naar jong, 1 tot 6.",
             oefeningen=[
                 ("rij", [("de grotschilderingen van Lascaux", "1"),
                          ("de piramiden van Gizeh", "2"),
                          ("het Parthenon in Athene", "3"),
                          ("het Colosseum in Rome", "4"),
                          ("een romaanse abdijkerk", "5"),
                          ("een gotische kathedraal", "6")],
                  "Welk nummer krijgt dit?", "70px"),
                 ("open", "Waarom zijn de grotschilderingen geen kunst in onze betekenis van "
                          "het woord?",
                  "Ze waren waarschijnlijk niet gemaakt om bekeken en bewonderd te worden maar "
                  "hadden een rituele of magische bedoeling. Het idee van kunst als vrij werk "
                  "van een kunstenaar bestond toen niet.", 4),
             ]),
        dict(kop="Egypte, Griekenland, Rome",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de vaste houding met het hoofd in zijaanzicht en de borst van voren",
                           "de Egyptische aspectiviteit"),
                          ("de zuilorde met het eenvoudige, strakke kapiteel", "dorisch"),
                          ("de zuilorde met de krullen", "ionisch"),
                          ("de zuilorde met de acanthusbladeren", "korinthisch"),
                          ("de Romeinse bouwvorm die grote overspanningen mogelijk maakte",
                           "de boog en het gewelf"),
                          ("het Romeinse bouwmateriaal dat gegoten kon worden",
                           "beton (opus caementicium)")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Wat namen de Romeinen over van de Grieken, en wat voegden ze toe?",
                  "Ze namen de zuilorden, de beeldhouwkunst en de tempelvorm over. Ze voegden "
                  "de boog, het gewelf, de koepel en beton toe, waarmee ze veel grotere en "
                  "praktischer gebouwen konden maken.", 4),
             ]),
        dict(kop="Romaans of gotisch?",
             opdracht="Schrijf romaans of gotisch op.",
             oefeningen=[
                 ("rij", [("de rondboog", "romaans"), ("de spitsboog", "gotisch"),
                          ("dikke muren en kleine ramen", "romaans"),
                          ("luchtbogen aan de buitenkant", "gotisch"),
                          ("een donker, zwaar en gesloten gevoel", "romaans"),
                          ("hoge glasramen en veel licht", "gotisch")],
                  "Welke stijl is dit?", WW),
                 ("open", "Leg uit hoe de luchtboog een gotische kathedraal hoger en lichter "
                          "maakte.",
                  "De luchtboog vangt de zijwaartse druk van het gewelf buiten het gebouw op. "
                  "De muren hoeven dan niet meer dik te zijn om te dragen, zodat er grote ramen "
                  "in kunnen en het gebouw hoger kan worden.", 4),
                 ("open", "Welke boodschap wilde een gotische kathedraal overbrengen?",
                  "Dat je opkijkt naar het hemelse: alles streeft naar boven en het licht door "
                  "de glasramen maakt van de binnenruimte iets onaards.", 3),
             ]),
    ])


# ============================================================
zet("kunststromingen-van-de-renaissance-tot-vandaag",
    titel="Kunststromingen van de renaissance tot vandaag",
    reeksen=[
        dict(kop="De stroming bij het kenmerk",
             opdracht="Vul de stroming in.",
             oefeningen=[
                 ("rij", [("evenwicht, perspectief, de mens als maat", "renaissance"),
                          ("beweging, sterk licht-donker, overdaad", "barok"),
                          ("de indruk van het moment, losse toets, buiten geschilderd",
                           "impressionisme"),
                          ("het gevoel van de kunstenaar, felle kleuren, vervorming",
                           "expressionisme"),
                          ("de werkelijkheid in vlakken en vanuit meerdere standpunten",
                           "kubisme"),
                          ("de droom en het onbewuste, onmogelijke combinaties", "surrealisme")],
                  "Welke stroming is dit?", WW),
                 ("rij", [("alleen vlak, lijn en kleur, geen herkenbaar onderwerp",
                           "abstracte kunst"),
                          ("beelden uit reclame en strips", "popart"),
                          ("het idee telt meer dan het voorwerp", "conceptuele kunst"),
                          ("terug naar de regels van de oudheid, strak en koel",
                           "classicisme / neoclassicisme"),
                          ("gevoel, natuurgeweld, het verleden als droom", "romantiek"),
                          ("het leven zoals het is, ook het harde", "realisme")],
                  "Welke stroming is dit?", WW),
             ]),
        dict(kop="Waarom verandert kunst?",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Welke uitvinding uit de negentiende eeuw duwde schilders weg van "
                          "het natuurgetrouw afbeelden? Leg uit.",
                  "De fotografie. Een machine kon voortaan beter en sneller een gelijkend beeld "
                  "maken, dus gingen schilders zoeken naar wat een foto niet kon: de indruk, "
                  "het gevoel, de vorm zelf.", 4),
                 ("open", "Hoe werkte de Eerste Wereldoorlog door in de kunst?",
                  "Het geloof in vooruitgang en redelijkheid brak; stromingen als dada en het "
                  "expressionisme zetten zich af tegen de oude orde en tegen de schoonheid "
                  "zelf.", 3),
                 ("open", "Waarom is er vandaag geen hoofdstroming meer?",
                  "Kunstenaars werken wereldwijd, met alle middelen tegelijk, en niemand bepaalt "
                  "nog wat de volgende stap is. Verschillende manieren bestaan naast elkaar.", 3),
             ]),
        dict(kop="Een werk plaatsen",
             opdracht="Lees de beschrijving en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een schilderij toont een stadsgezicht in korte, losse toetsen. De "
                  "contouren zijn niet getrokken; het lijkt alsof de huizen trillen. De kleuren "
                  "zijn licht en de schaduwen zijn blauw en paars in plaats van bruin. Je ziet "
                  "dat het regent zonder dat er één regendruppel geschilderd is.</em></p>"),
                 ("open", "Bij welke stroming hoort dit werk? Geef twee argumenten uit de "
                          "beschrijving.",
                  "Het impressionisme: de losse toets zonder contour en de gekleurde schaduwen "
                  "in plaats van bruin zijn twee kenmerken van die stroming.", 3),
                 ("open", "Wat bedoelt men met 'de indruk van het moment'?",
                  "Dat de schilder niet het voorwerp zelf wil weergeven maar hoe het licht er op "
                  "dat ene ogenblik op viel; een uur later ziet hetzelfde tafereel er anders "
                  "uit.", 3),
                 ("waar", "Een stroming begint en eindigt op een vaste datum.", False),
             ]),
    ])


# ============================================================
zet("samenlevingen-inhoud-en-context-van-een-kunstuiting",
    titel="Samenlevingen, inhoud en context van een kunstuiting",
    reeksen=[
        dict(kop="Drie soorten context",
             opdracht="Schrijf bij elke vraag welke context ze onderzoekt.",
             oefeningen=[
                 ("rij", [("Wie betaalde voor dit werk?", "de sociaal-economische context"),
                          ("Welk geloof hing samen met dit onderwerp?",
                           "de levensbeschouwelijke context"),
                          ("Welke oorlog woedde er net?", "de politiek-historische context"),
                          ("Welke nieuwe verf was toen uitgevonden?", "de technische context"),
                          ("Waar hing het werk oorspronkelijk?", "de ruimtelijke context"),
                          ("Welke andere kunstenaars werkten er in dezelfde stad?",
                           "de artistieke context")],
                  "Welke context onderzoekt deze vraag?", WL),
                 ("open", "Waarom verandert de betekenis van een werk als het verhuist van een "
                          "kerk naar een museum?",
                  "In de kerk maakte het deel uit van een gebed en van een ruimte; in het museum "
                  "staat het als los voorwerp naast andere werken en kijk je er vooral naar als "
                  "kunst. De plaats bepaalt mee hoe je het leest.", 4),
             ]),
        dict(kop="Opdrachtgever en kunstenaar",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem drie soorten opdrachtgevers uit de kunstgeschiedenis en zeg "
                          "wat elk ervan wilde.",
                  "De kerk wilde geloofsverhalen tonen aan wie niet kon lezen. Vorsten en adel "
                  "wilden hun macht en afkomst tonen. Rijke burgers en gilden wilden hun stand "
                  "en hun stad tonen.", 4),
                 ("open", "Hoe veranderde de positie van de kunstenaar tussen de middeleeuwen "
                          "en de renaissance?",
                  "In de middeleeuwen was hij een ambachtsman in een gilde die vaak niet "
                  "signeerde. In de renaissance werd hij een erkende maker met een eigen naam, "
                  "een eigen stijl en soms een eigen mening.", 4),
                 ("waar", "Wie betaalt, bepaalt in de kunstgeschiedenis vaak mee wat er te "
                          "zien is.", True),
             ]),
        dict(kop="Een werk ontleden",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een groot doek toont een groep soldaten die in het donker een stad "
                  "binnentrekt. Op de voorgrond ligt een gevallen man; een vrouw knielt bij hem. "
                  "Het enige felle licht komt van een brandend huis rechts. Het werk werd "
                  "geschilderd twee jaar na een oorlog, in opdracht van een stadsbestuur, en "
                  "hing in het stadhuis.</em></p>"),
                 ("open", "Wat vertelt de opdrachtgever je over de bedoeling?",
                  "Een stadsbestuur dat dit in het stadhuis hangt, wil het lijden van de stad "
                  "laten herinneren en zijn eigen rol in dat verhaal vastleggen.", 3),
                 ("open", "Wat doet het licht in dit werk?",
                  "Het brandende huis is de enige lichtbron en richt alle aandacht op het geweld; "
                  "de rest blijft donker, waardoor de soldaten dreigend en anoniem blijven.", 3),
                 ("open", "Welke vraag kan je niet beantwoorden zonder de context erbij te "
                          "halen?",
                  "Wie de soldaten zijn en of de schilder hen als bevrijders of als bezetters "
                  "toont: dat hangt af van welke oorlog het is en van wiens kant het stadhuis "
                  "stond.", 3),
             ]),
    ])


# ============================================================
zet("richtvragen-en-de-middelen-van-vormgeving",
    titel="Richtvragen en de middelen van vormgeving",
    reeksen=[
        dict(kop="De vier richtvragen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("Wat zie ik, zonder te oordelen?", "beschrijven"),
                          ("Hoe is het gemaakt en opgebouwd?", "analyseren"),
                          ("Wat betekent het en waarom denk ik dat?", "interpreteren"),
                          ("Wat vind ik ervan, en op welke grond?", "oordelen"),
                          ("de stap die je nooit mag overslaan", "beschrijven"),
                          ("de stap waarin je argumenten geeft", "oordelen")],
                  "Welke richtvraag is dit?", WW),
                 ("open", "Waarom beginnen we met beschrijven en niet met oordelen?",
                  "Wie meteen oordeelt, ziet alleen nog wat zijn oordeel bevestigt. Door eerst "
                  "nauwkeurig te beschrijven, blijf je open voor wat er echt staat.", 3),
             ]),
        dict(kop="De middelen benoemen",
             opdracht="Welk vormgevingsmiddel wordt hier gebruikt?",
             oefeningen=[
                 ("rij", [("alles loopt naar één punt in de diepte", "het lijnperspectief"),
                          ("de verte is blauwiger en vager", "het luchtperspectief"),
                          ("hard licht en diepe schaduw naast elkaar", "clair-obscur"),
                          ("de twee helften zijn elkaars spiegelbeeld", "symmetrie"),
                          ("het belangrijkste staat niet in het midden", "een asymmetrische "
                           "compositie"),
                          ("de kleuren liggen tegenover elkaar op de kleurencirkel",
                           "complementair kleurgebruik")],
                  "Welk middel is dit?", WL),
                 ("open", "Leg uit waarom een driehoekige compositie rust geeft.",
                  "Een driehoek staat breed op de grond en loopt naar één top. Je oog volgt die "
                  "lijnen naar boven en komt tot stilstand, zonder dat iets kan omvallen.", 3),
             ]),
        dict(kop="Toepassen op een beschrijving",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een affiche toont een enkele rode appel midden op een zwart vlak. "
                  "Onderaan staat in kleine witte letters één woord. De appel is scherp "
                  "gefotografeerd; het zwart is volledig leeg.</em></p>"),
                 ("open", "Beschrijf eerst, zonder te oordelen.",
                  "Eén rode appel in het midden van een zwart, leeg vlak, scherp weergegeven, "
                  "met onderaan één klein wit woord.", 2),
                 ("open", "Analyseer: welke middelen zorgen dat je naar de appel kijkt?",
                  "Het kleurcontrast rood op zwart, de lege ruimte eromheen, de centrale plaats "
                  "en de scherpte tegenover het effen zwart.", 3),
                 ("open", "Interpreteer: wat zou de maker kunnen bedoelen?",
                  "Dat het product op zich volstaat: geen decor, geen uitleg, alleen het "
                  "voorwerp. De leegte maakt er iets kostbaars van.", 3),
                 ("open", "Oordeel, met een argument.",
                  "Bijvoorbeeld: ik vind de affiche sterk, omdat ze met één beeld en één woord "
                  "alles zegt en je blik nergens anders heen kan.", 3),
             ]),
    ])


# ============================================================
zet("de-eigenheid-van-de-filosofie",
    titel="De eigenheid van de filosofie",
    reeksen=[
        dict(kop="Wat maakt een vraag filosofisch?",
             opdracht="Schrijf bij elke vraag op of ze filosofisch is, en waarom wel of niet.",
             oefeningen=[
                 ("rij", [("Hoeveel inwoners telt België?", "nee, een feitenvraag"),
                          ("Wat is rechtvaardigheid?", "ja, een begripsvraag"),
                          ("Hoe werkt een motor?", "nee, een technische vraag"),
                          ("Mag je liegen om iemand te beschermen?", "ja, een ethische vraag"),
                          ("Wanneer eindigde de Tweede Wereldoorlog?",
                           "nee, een geschiedenisvraag"),
                          ("Bestaat er een vrije wil?", "ja, een filosofische vraag")],
                  "Filosofisch of niet, en waarom?", WL),
                 ("open", "Geef drie kenmerken van een filosofische vraag.",
                  "Je kan ze niet met een meting of een opzoeking beantwoorden, ze gaat over de "
                  "vooronderstellingen achter het gewone denken, en elk antwoord moet met "
                  "argumenten verdedigd worden.", 4),
             ]),
        dict(kop="Filosofie naast andere vakken",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen de vraag van een bioloog en die van een "
                          "filosoof over leven?",
                  "De bioloog onderzoekt hoe levende wezens werken en wat leven kenmerkt; de "
                  "filosoof vraagt wat we met leven bedoelen en of een leven waarde heeft.", 3),
                 ("open", "Waarom is filosofie geen godsdienst?",
                  "Een godsdienst vertrekt van een geloof en van gezaghebbende teksten; de "
                  "filosofie vertrekt van vragen en aanvaardt alleen wat met argumenten "
                  "verdedigd kan worden, ook over het geloof zelf.", 4),
                 ("open", "Wat bedoelde Socrates met 'ik weet dat ik niets weet'?",
                  "Dat hij, anders dan wie meende het te weten, zijn eigen onwetendheid kende. "
                  "Dat besef is het beginpunt van echt onderzoek.", 3),
                 ("waar", "Een filosofische vraag heeft altijd één juist antwoord.", False),
             ]),
        dict(kop="Verwondering",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom noemt men verwondering het begin van de filosofie?",
                  "Omdat filosofie start waar het vanzelfsprekende plots niet meer vanzelf "
                  "spreekt: pas als je je afvraagt waarom iets zo is, kan je er vragen over "
                  "stellen.", 3),
                 ("open", "Neem iets alledaags, bijvoorbeeld je gsm of je schooluren, en maak "
                          "er een filosofische vraag van.",
                  "Bijvoorbeeld: is tijd iets dat bestaat, of alleen iets dat wij meten? Of: "
                  "ben ik vrij als ik zelf kies om elke avond op mijn scherm te kijken?", 3),
             ]),
    ])


# ============================================================
zet("de-oorsprong-van-de-westerse-filosofie",
    titel="De oorsprong van de westerse filosofie",
    reeksen=[
        dict(kop="Van mythos naar logos",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("verklaren met verhalen over goden", "mythos"),
                          ("verklaren met redenen en argumenten", "logos"),
                          ("de eerste filosofen, in Milete", "de natuurfilosofen"),
                          ("hij zei dat alles water is", "Thales"),
                          ("hij zei dat alles stroomt", "Herakleitos"),
                          ("hij zei dat verandering onmogelijk is", "Parmenides")],
                  "Over wie of wat gaat dit?", WW),
                 ("open", "Leg uit waarom de overgang van mythos naar logos een breuk is.",
                  "Een mythe vraagt dat je gelooft wat overgeleverd is; de logos vraagt dat je "
                  "een reden geeft die iedereen kan nagaan en tegenspreken. Daarmee begint "
                  "kritiek mogelijk te worden.", 4),
             ]),
        dict(kop="De drie grote Grieken",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["filosoof", "manier van werken", "kernidee"],
                  [["Socrates", None, None], ["Plato", None, None], ["Aristoteles", None, None]],
                  "Socrates: het gesprek met vragen, de maieutiek; wie het goede kent, doet het "
                  "goede · Plato: de dialoog, de ideeënleer; achter de zichtbare dingen liggen "
                  "volmaakte ideeën · Aristoteles: waarnemen en ordenen; kennis begint bij de "
                  "zintuigen, en deugd ligt in het midden", "200px"),
                 ("open", "Leg de grotallegorie van Plato uit in enkele zinnen.",
                  "Mensen zitten vastgebonden in een grot en zien alleen schaduwen op de wand. "
                  "Wie loskomt en naar buiten gaat, ziet de echte dingen en het zonlicht. "
                  "Wie terugkeert om dat te vertellen, wordt niet geloofd.", 4),
                 ("open", "Waarin verschilt Aristoteles van zijn leermeester Plato?",
                  "Plato zoekt de waarheid in een wereld van ideeën boven de zichtbare dingen; "
                  "Aristoteles zoekt ze in de dingen zelf, door te kijken, te verzamelen en in "
                  "te delen.", 3),
                 ("kort", "Hoe heet de gespreksmethode van Socrates?",
                  "de maieutiek / de vroedvrouwmethode", WW),
             ]),
        dict(kop="Doordenken",
             opdracht="Antwoord met een argument.",
             oefeningen=[
                 ("open", "Socrates zegt: wie het goede kent, doet het goede. Ben je het "
                          "daarmee eens?",
                  "Een goed antwoord weegt beide kanten: mensen weten vaak wel wat goed is en "
                  "doen het toch niet, uit angst, gewoonte of eigenbelang. Dat pleit tegen "
                  "Socrates. Daartegenover kan je stellen dat echt kennen meer is dan weten: "
                  "wie het goede volledig doorziet, wil het ook.", 5),
                 ("open", "Herken je de grot van Plato in iets van vandaag?",
                  "Bijvoorbeeld in een tijdlijn die alleen toont wat je al denkt: je ziet een "
                  "beeld van de wereld dat voor jou gemaakt is en houdt het voor de "
                  "werkelijkheid.", 3),
             ]),
    ])


# ============================================================
zet("soorten-vragen-en-de-filosofische-vraag",
    titel="Soorten vragen en de filosofische vraag",
    reeksen=[
        dict(kop="Welke soort vraag?",
             opdracht="Schrijf op: feitenvraag, waardevraag, begripsvraag of zinvraag.",
             oefeningen=[
                 ("rij", [("Hoeveel graden is het buiten?", "feitenvraag"),
                          ("Is het eerlijk dat niet iedereen evenveel verdient?",
                           "waardevraag"),
                          ("Wat betekent 'eerlijk' precies?", "begripsvraag"),
                          ("Waarom bestaat er iets in plaats van niets?", "zinvraag"),
                          ("Wanneer is iemand volwassen?", "begripsvraag"),
                          ("Mag je een dier doden voor voedsel?", "waardevraag")],
                  "Welke soort vraag is dit?", WW),
                 ("open", "Waarom helpt het om eerst te bepalen welk soort vraag je voorhebt?",
                  "Omdat elke soort een andere aanpak vraagt: een feitenvraag zoek je op, een "
                  "begripsvraag ontleed je, en een waardevraag beantwoord je met argumenten.", 3),
             ]),
        dict(kop="Van gewone vraag naar filosofische vraag",
             opdracht="Herschrijf de vraag zodat ze filosofisch wordt.",
             oefeningen=[
                 ("open", "Hoeveel uur slaapt een puber gemiddeld?",
                  "Bijvoorbeeld: heb je het recht om zelf te bepalen hoe laat je gaat slapen, "
                  "ook als het je schadelijk is?", 2),
                 ("open", "Welke straf staat er op diefstal?",
                  "Bijvoorbeeld: wat maakt een straf rechtvaardig, en wat wil een samenleving "
                  "met straffen bereiken?", 2),
                 ("open", "Hoeveel mensen gebruiken sociale media?",
                  "Bijvoorbeeld: ben je nog jezelf als je voortdurend een beeld van jezelf "
                  "toont aan anderen?", 2),
                 ("open", "Welk dier is het slimst?",
                  "Bijvoorbeeld: wat bedoelen we met intelligentie, en mogen we dieren "
                  "beoordelen met een menselijke maat?", 2),
             ]),
        dict(kop="Een vraag openhouden",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is een suggestieve vraag? Geef een voorbeeld en verbeter ze.",
                  "Een vraag die het antwoord al in zich draagt, bijvoorbeeld: vind je ook niet "
                  "dat jongeren te veel op hun gsm zitten? Beter: welke rol speelt de gsm in het "
                  "leven van jongeren?", 4),
                 ("open", "Waarom is 'wat denk jij ervan' nog geen filosofisch gesprek?",
                  "Omdat meningen naast elkaar zetten nog geen onderzoek is. Het wordt "
                  "filosofisch zodra je om argumenten vraagt en die samen toetst.", 3),
                 ("waar", "Een goede filosofische vraag kan je met ja of nee afdoen.", False),
             ]),
    ])


# ============================================================
zet("de-filosofische-domeinen",
    titel="De filosofische domeinen",
    reeksen=[
        dict(kop="Welk domein?",
             opdracht="Schrijf het domein op.",
             oefeningen=[
                 ("rij", [("Wat bestaat er echt?", "metafysica / ontologie"),
                          ("Hoe weten we iets?", "kennisleer"),
                          ("Wat is juist handelen?", "ethiek"),
                          ("Wat is een rechtvaardige samenleving?", "politieke filosofie"),
                          ("Wat is schoonheid?", "esthetica"),
                          ("Wat is een geldige redenering?", "logica")],
                  "Welk domein is dit?", WW),
                 ("rij", [("Bestaat de ziel los van het lichaam?", "metafysica"),
                          ("Kan ik mijn zintuigen vertrouwen?", "kennisleer"),
                          ("Mag een arts iemand laten sterven?", "ethiek"),
                          ("Waarom zou ik de wet gehoorzamen?", "politieke filosofie"),
                          ("Is een lelijk schilderij slechte kunst?", "esthetica"),
                          ("Volgt dit besluit uit die twee zinnen?", "logica")],
                  "Welk domein is dit?", WW),
             ]),
        dict(kop="Rationalisme en empirisme",
             opdracht="Vul aan of antwoord.",
             oefeningen=[
                 ("rij", [("kennis komt vooral uit het denken", "rationalisme"),
                          ("kennis komt vooral uit de ervaring", "empirisme"),
                          ("Descartes", "rationalisme"), ("Hume", "empirisme"),
                          ("de geest als onbeschreven blad", "empirisme"),
                          ("aangeboren ideeën", "rationalisme")],
                  "Welke stroming hoort hierbij?", WW),
                 ("open", "Wat bedoelde Descartes met 'ik denk, dus ik ben'?",
                  "Hij twijfelde aan alles, maar aan het twijfelen zelf kon hij niet twijfelen. "
                  "Dat er iemand twijfelt, is dus het eerste zekere punt.", 3),
                 ("open", "Geef één bezwaar tegen het empirisme.",
                  "Niet alles wat we weten komt uit ervaring: wiskundige waarheden zoals dat "
                  "twee plus twee vier is, gelden zonder dat je het hoeft na te meten.", 3),
             ]),
        dict(kop="Toepassen",
             opdracht="Antwoord met een argument.",
             oefeningen=[
                 ("open", "Bij welk domein hoort de vraag of een computer kan denken? Leg uit "
                          "waarom er meer dan één antwoord mogelijk is.",
                  "Bij de metafysica en de kennisleer tegelijk: ze gaat over wat denken is en "
                  "over wat we kunnen weten van een ander wezen. Wie ze stelt als 'mogen we een "
                  "computer rechten geven', verschuift ze naar de ethiek.", 4),
                 ("open", "Geef voor twee domeinen een vraag uit je eigen leven.",
                  "Bijvoorbeeld ethiek: mag ik een vriend verklikken om hem te helpen? En "
                  "kennisleer: hoe weet ik of wat ik online lees waar is?", 3),
             ]),
    ])


# ============================================================
zet("de-filosofische-vaardigheden",
    titel="De filosofische vaardigheden",
    reeksen=[
        dict(kop="Een redenering ontleden",
             opdracht="Schrijf de premissen en het besluit apart op.",
             oefeningen=[
                 ("open", "Alle mensen zijn sterfelijk. Socrates is een mens. Dus is Socrates "
                          "sterfelijk.",
                  "Premisse 1: alle mensen zijn sterfelijk. Premisse 2: Socrates is een mens. "
                  "Besluit: Socrates is sterfelijk.", 3),
                 ("open", "Wie niet studeert, slaagt niet. Lotte slaagde niet. Dus studeerde "
                          "Lotte niet. Klopt deze redenering?",
                  "Nee. Uit 'wie niet studeert, slaagt niet' volgt niet dat elke gezakte niet "
                  "gestudeerd heeft; er kunnen andere oorzaken zijn. Dat is de drogreden van de "
                  "ontkende voorwaarde.", 4),
                 ("open", "Wat is het verschil tussen een geldige en een ware redenering?",
                  "Geldig gaat over de vorm: als de premissen waar zijn, moet het besluit "
                  "volgen. Waar gaat over de inhoud: kloppen de premissen ook echt? Een "
                  "geldige redenering met een valse premisse geeft een vals besluit.", 4),
             ]),
        dict(kop="Drogredenen herkennen",
             opdracht="Noem de drogreden.",
             oefeningen=[
                 ("rij", [("Je hebt zelf een auto, dus zwijg over het klimaat.",
                           "op de man spelen"),
                          ("Iedereen doet het, dus het mag.", "beroep op de massa"),
                          ("Als we dit toelaten, eindigen we in chaos.", "hellend vlak"),
                          ("Je bent het niet eens, dus je bent tegen de school.",
                           "stroman"),
                          ("Een bekende acteur zegt het, dus het klopt.",
                           "vals beroep op gezag"),
                          ("Of je bent voor ons, of je bent tegen ons.", "vals dilemma")],
                  "Welke drogreden is dit?", WW),
                 ("open", "Leg uit waarom een drogreden overtuigend kan klinken.",
                  "Ze speelt in op een gevoel of op een gewoonte in plaats van op de inhoud, en "
                  "ze heeft vaak de vorm van een geldige redenering.", 3),
             ]),
        dict(kop="Begrippen verhelderen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Geef een definitie van 'vriend' en zoek er dan zelf een "
                          "tegenvoorbeeld bij.",
                  "Bijvoorbeeld: een vriend is iemand die je graag ziet en die je vertrouwt. "
                  "Tegenvoorbeeld: je vertrouwt je huisarts ook, en die is geen vriend; er is "
                  "dus meer nodig, zoals wederkerigheid en gekozen nabijheid.", 4),
                 ("open", "Wat is een gedachte-experiment? Geef er een.",
                  "Een verzonnen situatie waarmee je een idee op de proef stelt. Bijvoorbeeld: "
                  "als je een pil kon nemen die je levenslang gelukkig maakt maar alles vals "
                  "laat voelen, zou je ze nemen? Dat test wat geluk voor je betekent.", 4),
                 ("open", "Noem drie regels voor een goed filosofisch gesprek.",
                  "Laat elkaar uitspreken, vraag door naar het argument in plaats van naar de "
                  "persoon, en durf je eigen standpunt te veranderen als het argument beter is.",
                  3),
             ]),
    ])


# ============================================================
zet("lichaam-en-geest",
    titel="Lichaam en geest",
    reeksen=[
        dict(kop="De standpunten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("lichaam en geest zijn twee verschillende dingen", "dualisme"),
                          ("alles is uiteindelijk stof", "materialisme"),
                          ("de geest is wat de hersenen doen", "fysicalisme"),
                          ("de filosoof van het dualisme", "Descartes"),
                          ("het probleem hoe twee soorten dingen elkaar kunnen raken",
                           "het interactieprobleem"),
                          ("de vraag hoe uit stof beleving ontstaat",
                           "het moeilijke bewustzijnsprobleem")],
                  "Over welk begrip gaat dit?", WL),
                 ("open", "Leg het interactieprobleem van Descartes uit.",
                  "Als de geest onstoffelijk is en het lichaam stoffelijk, blijft onverklaard "
                  "hoe een gedachte een arm in beweging kan zetten. Twee dingen van een andere "
                  "soort kunnen elkaar moeilijk raken.", 4),
             ]),
        dict(kop="Argumenten wegen",
             opdracht="Antwoord met een argument.",
             oefeningen=[
                 ("open", "Geef één argument voor en één tegen de stelling dat jij je "
                          "hersenen bent.",
                  "Voor: elke verandering in de hersenen, door een slag of een medicijn, "
                  "verandert ook wat je denkt en voelt. Tegen: een beschrijving van neuronen "
                  "vertelt niet hoe het voelt om pijn te hebben; dat gevoel lijkt iets anders "
                  "dan de stof zelf.", 5),
                 ("open", "Wat is het gedachte-experiment van de kamer van Mary, en wat wil het "
                          "aantonen?",
                  "Mary weet alles over kleur maar heeft alleen zwart-wit gezien. Als ze voor "
                  "het eerst rood ziet, leert ze dan iets nieuws? Als het antwoord ja is, is "
                  "niet alle kennis in feiten over stof te vatten.", 4),
                 ("waar", "Als je een handeling in de hersenen kan meten voor iemand zich "
                          "bewust is van zijn keuze, is daarmee bewezen dat er geen vrije wil "
                          "is.", False),
             ]),
        dict(kop="Vrije wil",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("alles ligt vast door wat eraan voorafging", "determinisme"),
                          ("er is echte keuzevrijheid", "libertarisme"),
                          ("vrijheid en determinisme gaan samen", "compatibilisme"),
                          ("vrij zijn is doen wat je zelf wil, ook als dat willen bepaald is",
                           "compatibilisme"),
                          ("het experiment van Libet", "meting voor het bewuste besluit"),
                          ("zonder vrije wil geen verantwoordelijkheid", "een bezwaar tegen "
                           "het determinisme")],
                  "Waarover gaat dit?", WL),
                 ("open", "Als er geen vrije wil zou zijn, wat betekent dat voor straffen?",
                  "Straffen als vergelding wordt dan moeilijk te verdedigen. Je kan nog wel "
                  "ingrijpen om herhaling te voorkomen en om mensen te beschermen, maar niet "
                  "meer omdat iemand het verdient.", 4),
             ]),
    ])


# ============================================================
zet("mens-en-dier",
    titel="Mens en dier",
    reeksen=[
        dict(kop="Wat zou de mens uniek maken?",
             opdracht="Schrijf bij elk voorstel één tegenwerping.",
             oefeningen=[
                 ("open", "De mens is het enige wezen dat gereedschap gebruikt.",
                  "Kraaien buigen een draad tot een haak en chimpansees gebruiken stokken en "
                  "stenen; het klopt dus niet.", 2),
                 ("open", "De mens is het enige wezen met taal.",
                  "Bijen, dolfijnen en apen geven informatie door. Wat wel bijzonder lijkt, is "
                  "de grammatica waarmee mensen oneindig veel nieuwe zinnen kunnen maken.", 3),
                 ("open", "De mens is het enige wezen dat weet dat het sterft.",
                  "Dat is moeilijk te weerleggen maar ook moeilijk te bewijzen: we weten niet "
                  "wat een dier weet. Olifanten en sommige apen tonen wel gedrag rond dode "
                  "soortgenoten.", 3),
                 ("open", "De mens is het enige wezen met cultuur.",
                  "Groepen chimpansees geven eigen gewoontes door die buurgroepen niet hebben; "
                  "dat lijkt op cultuur, al is ze veel beperkter.", 2),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de mens boven het dier plaatsen omdat hij mens is", "speciesisme"),
                          ("het vermogen om te lijden", "sentiëntie"),
                          ("zichzelf herkennen in een spiegel", "zelfbewustzijn"),
                          ("de mens als maat van alles", "antropocentrisme"),
                          ("de mens als onaf wezen dat zichzelf moet vormen",
                           "de mens als tekortwezen"),
                          ("de gedachte dat dieren rechten kunnen hebben", "dierenethiek")],
                  "Over welk begrip gaat dit?", WL),
                 ("open", "Waarom vond Bentham de vraag 'kunnen zij lijden' belangrijker dan "
                          "'kunnen zij denken'?",
                  "Omdat het vermogen om pijn te voelen volstaat om iets of iemand in je morele "
                  "afweging mee te tellen. Verstand is dan niet de maat.", 3),
             ]),
        dict(kop="Een standpunt opbouwen",
             opdracht="Schrijf uit.",
             oefeningen=[
                 ("open", "Mag je dieren houden voor vlees? Geef twee argumenten voor en twee "
                          "tegen.",
                  "Voor: mensen eten al duizenden jaren vlees en veeteelt geeft voedsel en werk; "
                  "als het dier goed leeft en pijnloos sterft, is er weinig schade. Tegen: een "
                  "dier dat kan lijden heeft er belang bij te blijven leven, en de huidige "
                  "veeteelt brengt veel dierenleed en milieuschade mee.", 6),
                 ("open", "Schrijf je eigen standpunt in drie zinnen, met minstens één reden "
                          "en één toegeving aan de andere kant.",
                  "Elk eerlijk standpunt is goed zolang het een reden geeft en toegeeft wat er "
                  "tegen pleit.", 4),
             ]),
    ])


# ============================================================
zet("de-ethische-stromingen-en-hun-filosofen",
    titel="De ethische stromingen en hun filosofen",
    reeksen=[
        dict(kop="Drie stromingen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["stroming", "waar kijkt ze naar?", "filosoof"],
                  [["deugdethiek", None, None], ["plichtethiek", None, None],
                   ["gevolgenethiek", None, None]],
                  "deugdethiek: naar de persoon en zijn karakter, Aristoteles · "
                  "plichtethiek: naar de handeling en de regel, Kant · "
                  "gevolgenethiek: naar de uitkomst voor iedereen, Bentham en Mill", "190px"),
                 ("rij", [("Je mag nooit liegen, ook niet om iemand te redden.", "plichtethiek"),
                          ("Lieg als dat het grootste geluk oplevert.", "gevolgenethiek"),
                          ("Wat zou een eerlijk mens hier doen?", "deugdethiek"),
                          ("Handel zo dat je regel een wet voor iedereen kan zijn.",
                           "plichtethiek"),
                          ("Tel het leed en het geluk van alle betrokkenen op.",
                           "gevolgenethiek"),
                          ("Deugd ligt in het midden tussen twee uitersten.", "deugdethiek")],
                  "Welke stroming is dit?", WW),
             ]),
        dict(kop="Kant en Mill",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is de categorische imperatief van Kant, in je eigen woorden?",
                  "Handel alleen volgens een regel waarvan je kan willen dat iedereen ze altijd "
                  "volgt. En: behandel een mens nooit alleen als middel, altijd ook als doel.",
                  4),
                 ("open", "Geef één sterk punt en één zwak punt van de plichtethiek.",
                  "Sterk: ze beschermt de mens tegen berekeningen die hem opofferen voor het "
                  "grotere geheel. Zwak: ze kan star worden, want ze laat geen uitzondering toe "
                  "ook als de gevolgen rampzalig zijn.", 4),
                 ("open", "Geef één sterk punt en één zwak punt van de gevolgenethiek.",
                  "Sterk: ze kijkt naar wat er echt gebeurt en weegt alle betrokkenen mee. "
                  "Zwak: ze kan onrecht tegen één persoon goedpraten als de meerderheid er "
                  "beter van wordt, en gevolgen zijn moeilijk te voorspellen.", 4),
                 ("open", "Wat bedoelt Aristoteles met de gulden middenweg? Geef een "
                          "voorbeeld.",
                  "Een deugd ligt tussen een tekort en een teveel. Moed ligt tussen lafheid en "
                  "roekeloosheid; vrijgevigheid tussen gierigheid en verkwisting.", 3),
             ]),
        dict(kop="Het dilemma van de trolley",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een op hol geslagen tram rijdt op vijf mensen af. Je kan een wissel "
                  "omzetten; dan rijdt hij op één mens af. In een tweede versie kan je geen "
                  "wissel omzetten maar wel één zware man van een brug duwen, waardoor de tram "
                  "stopt en vijf mensen gered zijn.</em></p>"),
                 ("open", "Wat zegt een gevolgenethicus over de eerste versie?",
                  "Zet de wissel om: één dode is minder erg dan vijf, dus de uitkomst is "
                  "beter.", 2),
                 ("open", "Wat zegt een plichtethicus over de tweede versie?",
                  "Duw niet: je gebruikt die man dan louter als middel om anderen te redden, en "
                  "dat mag nooit.", 2),
                 ("open", "Waarom vinden de meeste mensen de tweede versie moeilijker, ook al "
                          "is de rekensom dezelfde?",
                  "Omdat je in de tweede versie iemand eigenhandig gebruikt en doodt, terwijl je "
                  "in de eerste een gevaar verlegt. Ons morele gevoel maakt dat onderscheid, ook "
                  "al telt de rekensom even zwaar.", 4),
             ]),
    ])


# ============================================================
zet("begrippen-uit-de-moraalfilosofie",
    titel="Begrippen uit de moraalfilosofie",
    reeksen=[
        dict(kop="De begrippen uit elkaar houden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het geheel van wat een groep goed en kwaad noemt", "moraal"),
                          ("het nadenken over die moraal", "ethiek"),
                          ("wat iemand belangrijk vindt", "een waarde"),
                          ("de concrete regel die daaruit volgt", "een norm"),
                          ("de innerlijke stem die je iets verwijt", "het geweten"),
                          ("de verplichting om rekenschap af te leggen",
                           "verantwoordelijkheid")],
                  "Over welk begrip gaat dit?", WW),
                 ("open", "Leg het verschil tussen moraal en ethiek uit met een voorbeeld.",
                  "De moraal zegt: liegen hoort niet. De ethiek vraagt: waarom eigenlijk, en "
                  "geldt dat ook als een leugen een leven redt?", 3),
                 ("waar", "Elke norm komt voort uit een waarde.", True),
             ]),
        dict(kop="Feit en waarde",
             opdracht="Schrijf op of het een feit of een waardeoordeel is.",
             oefeningen=[
                 ("rij", [("In België is de doodstraf afgeschaft.", "feit"),
                          ("De doodstraf is barbaars.", "waardeoordeel"),
                          ("Negen op de tien jongeren heeft een gsm.", "feit"),
                          ("Jongeren hangen te veel aan hun gsm.", "waardeoordeel"),
                          ("Roken verhoogt de kans op longkanker.", "feit"),
                          ("De overheid moet roken verbieden.", "waardeoordeel")],
                  "Feit of waardeoordeel?", WW),
                 ("open", "Wat is de is-behoort-kloof van Hume?",
                  "Uit een beschrijving van hoe iets is, volgt niet vanzelf hoe het behoort te "
                  "zijn. Er is altijd een waardepremisse nodig om van een feit naar een norm te "
                  "gaan.", 4),
                 ("open", "Geef een voorbeeld van een redenering die die kloof overspringt.",
                  "Bijvoorbeeld: in de natuur eet het ene dier het andere, dus mogen wij vlees "
                  "eten. Dat het zo is, zegt nog niet dat het zo hoort.", 3),
             ]),
        dict(kop="Tolerantie en vrijheid",
             opdracht="Antwoord met een argument.",
             oefeningen=[
                 ("open", "Wat is het schadebeginsel van Mill?",
                  "Een samenleving mag iemands vrijheid alleen beperken om schade aan anderen "
                  "te voorkomen, niet om die persoon tegen zichzelf te beschermen.", 3),
                 ("open", "Geldt dat beginsel ook voor de fietshelm of de gordel? Weeg beide "
                          "kanten.",
                  "Strikt genomen schaad je vooral jezelf, dus Mill zou tegen de plicht zijn. "
                  "Daartegenover staat dat de kosten van zware letsels door de hele samenleving "
                  "gedragen worden, wat van de schade toch een gedeelde zaak maakt.", 5),
                 ("open", "Waar ligt volgens jou de grens van tolerantie? Geef een reden.",
                  "Een goed antwoord noemt de paradox van de tolerantie: wie alles verdraagt, "
                  "verdraagt ook wie de tolerantie zelf wil afschaffen. De grens ligt dan bij "
                  "wat anderen hun vrijheid of veiligheid ontneemt.", 4),
             ]),
    ])


# ============================================================
zet("ethische-vraagstukken-analyseren",
    titel="Ethische vraagstukken analyseren",
    reeksen=[
        dict(kop="Het stappenplan",
             opdracht="Zet de stappen in de juiste volgorde, 1 tot 6.",
             oefeningen=[
                 ("rij", [("de feiten verzamelen", "1"),
                          ("de betrokkenen en hun belangen in kaart brengen", "2"),
                          ("de ethische vraag scherp formuleren", "3"),
                          ("de argumenten voor en tegen op een rij zetten", "4"),
                          ("de stromingen erop toepassen", "5"),
                          ("een standpunt innemen en verantwoorden", "6")],
                  "Welke stap is dit?", "70px"),
                 ("open", "Waarom staat 'de feiten verzamelen' vooraan?",
                  "Veel meningsverschillen gaan eigenlijk over de feiten en niet over de "
                  "waarden. Pas als duidelijk is wat er echt aan de hand is, kan je er "
                  "eerlijk over oordelen.", 3),
             ]),
        dict(kop="Een casus uitwerken",
             opdracht="Lees en werk het stappenplan af.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Een school wil camera's met gezichtsherkenning aan de ingang om "
                  "spijbelen tegen te gaan en om te weten wie er binnen is bij een "
                  "evacuatie. Leerlingen worden niet om toestemming gevraagd; de beelden "
                  "worden een maand bewaard.</em></p>"),
                 ("open", "Wie zijn de betrokkenen en wat is hun belang?",
                  "Leerlingen (privacy en vrijheid), ouders (veiligheid van hun kind), de "
                  "school (orde, aanwezigheid, aansprakelijkheid), leerkrachten (werklast) en "
                  "de samenleving (grenzen aan toezicht).", 4),
                 ("open", "Formuleer de ethische vraag in één zin.",
                  "Mag een school de privacy van al haar leerlingen beperken om spijbelen "
                  "tegen te gaan en de veiligheid te verhogen?", 2),
                 ("open", "Geef twee argumenten voor en twee tegen.",
                  "Voor: bij een brand weet je meteen wie binnen is, en spijbelen daalt wat de "
                  "kansen van leerlingen beschermt. Tegen: iedereen wordt behandeld als "
                  "verdachte terwijl de meesten niets doen, en gezichtsgegevens zijn "
                  "onvervangbaar als ze lekken.", 5),
                 ("open", "Wat zegt een plichtethicus, en wat een gevolgenethicus?",
                  "De plichtethicus wijst erop dat leerlingen zo louter als middel voor de orde "
                  "gebruikt worden en dat toestemming ontbreekt. De gevolgenethicus telt af: "
                  "als de winst in veiligheid groot is en het risico op misbruik klein, kan het "
                  "verdedigbaar zijn.", 4),
                 ("open", "Neem een standpunt in en verantwoord het, met één toegeving aan de "
                          "andere kant.",
                  "Elk standpunt is goed zolang het een reden geeft en erkent wat ertegen "
                  "pleit, bijvoorbeeld: geen gezichtsherkenning, maar wel een gewone "
                  "aanwezigheidsregistratie, want die geeft de meeste veiligheidswinst met de "
                  "minste inbreuk.", 4),
             ]),
        dict(kop="Nog twee vraagstukken",
             opdracht="Formuleer de kernvraag en geef bij elk één argument van beide kanten.",
             oefeningen=[
                 ("open", "Een ziekenhuis heeft één orgaan en twee patiënten.",
                  "Kernvraag: op welke grond mag je kiezen wie leeft? Voor leeftijd of "
                  "slaagkans: dat levert de meeste gewonnen levensjaren op. Tegen: elk leven "
                  "telt evenveel, dus een loting of de wachtlijst is eerlijker.", 4),
                 ("open", "Een bedrijf laat een algoritme sollicitaties voorselecteren.",
                  "Kernvraag: mag een beslissing over iemands kansen aan een machine worden "
                  "overgelaten? Voor: een algoritme is consequent en kent de vermoeidheid van "
                  "een mens niet. Tegen: het leert uit het verleden en herhaalt dus de "
                  "discriminatie die er al in zat, zonder dat iemand het ziet.", 4),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}


UITLEGBLADEN["oefenbundel-kunst-als-deel-van-een-cultuur-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek bij elk voorbeeld de vraag: waarvoor dient dit werk, en voor wie? Een functie "
                    "zit niet in het materiaal maar in wat het werk in een samenleving doet.",
             waarom=[
                 "Eén werk kan meerdere functies hebben, en meestal is dat ook zo: een glasraam vertelt én "
                 "versiert én toont de rijkdom van wie het betaalde. Noem bij zo'n vraag de functie die "
                 "het sterkst meespeelt.",
                 "Daarom staat bij een kunstwerk altijd de context: wie gaf de opdracht, waar hing het, "
                 "wie mocht het zien? Zonder die gegevens kan je het werk niet lezen, enkel bekijken.",
             ]),
        dict(aanpak="Deze vraag heeft geen juist antwoord maar wel goede en slechte argumenten. Geef dus "
                    "argumenten, geen mening, en zorg dat je ook de andere kant eerlijk weergeeft.",
             waarom=[
                 "Het gaat over Fontaine van Marcel Duchamp uit 1917. Zo'n voorwerp heet een readymade, en "
                 "het verlegde de vraag van hoe goed iets gemaakt is naar wat de kunstenaar met een keuze "
                 "kan zeggen.",
                 "Dat heet de kunstwereld: het geheel van musea, galerieën, critici, scholen en kopers. "
                 "Hetzelfde voorwerp op een rommelmarkt is geen kunst, in een museumzaal wel, en net dat "
                 "maakt het een sociaal gegeven.",
                 "Meten kan je de afmetingen en de materialen, niet de status van kunst. Dat betekent niet "
                 "dat alles even goed is: je kan wel beargumenteren waarom een werk sterk of zwak is.",
             ]),
        dict(aanpak="Bij een werk in de openbare ruimte lees je drie dingen: de vorm (grootte, standpunt, "
                    "houding), de plaats, en wie de opdracht gaf. Die drie samen maken de boodschap.",
             waarom=[
                 "Let op het standpunt van de toeschouwer: door de sokkel moet je opkijken, en opkijken is "
                 "letterlijk en figuurlijk hetzelfde woord. Dat is geen toeval maar een ontwerpkeuze.",
                 "Dat heet de context, en bij openbare kunst is ze even belangrijk als het werk. Hetzelfde "
                 "beeld in een museumzaal zou iets heel anders betekenen.",
                 "Daarom zijn standbeelden zo vaak voorwerp van discussie: ze blijven staan voor een "
                 "boodschap die de samenleving misschien niet meer deelt. Weghalen, laten staan of een "
                 "bord erbij zetten zijn alle drie manieren om daarmee om te gaan.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-kunstvormen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je af of het werk er in zijn geheel staat of zich in de tijd ontvouwt. Staat "
                    "het er, dan is het ruimtelijk; speelt het zich af, dan is het tijdelijk; dans en film "
                    "zijn beide.",
             waarom=[
                 "Dans en film zijn de tussengevallen: ze gebeuren in de tijd én gebruiken de ruimte. "
                 "Daarom heten ze ruimtelijk-tijdelijke kunstvormen.",
                 "Dat verschil bepaalt hoe je kijkt: bij een schilderij kies je zelf waar je begint, bij "
                 "muziek of film bepaalt het werk de orde en het tempo. Daarom kan je een schilderij niet "
                 "spoilen en een film wel.",
             ]),
        dict(aanpak="Elke kunstvorm heeft eigen middelen, en net die middelen bespreek je als je over een "
                    "werk schrijft. Leer ze per kunstvorm, dan heb je altijd woorden om mee te beginnen.",
             waarom=[
                 "Let op beeldhouwkunst: het standpunt hoort bij de middelen, want je kan rondom het werk "
                 "lopen. Bij een schilderij is het standpunt juist door de kunstenaar vastgelegd.",
                 "Daarom spreekt men bij architectuur van de drie eisen van Vitruvius: stevigheid, "
                 "bruikbaarheid en schoonheid. Een gebouw dat mooi is en instort, is geen goede "
                 "architectuur.",
             ]),
        dict(aanpak="Werk in twee stappen: eerst beschrijven wat je ziet, dan interpreteren wat het "
                    "betekent. Houd die twee gescheiden, want een beschrijving zonder interpretatie kan "
                    "iedereen nakijken en een interpretatie zonder beschrijving hangt in de lucht.",
             waarom=[
                 "Een compositie beschrijf je met richtingen en plaatsen: links, uit het midden, naar de "
                 "achtergrond. Noem ook wat de blik leidt, hier het licht.",
                 "Licht is in de schilderkunst zowel een middel als een betekenis: het kiest voor jou wat "
                 "belangrijk is. Deze beschrijving past bij een interieur van Vermeer, waar dat net het "
                 "kenmerk is.",
                 "Een goede interpretatievraag vertrekt van iets wat je echt in het werk ziet. De kaart op "
                 "de tafel is zo'n detail: het verwijst naar verte en afwezigheid.",
                 "Beschrijven is wat er staat, interpreteren is wat het zou kunnen betekenen. In een "
                 "bespreking komen ze na elkaar, en bij een examenvraag staat er meestal uitdrukkelijk "
                 "welke van de twee gevraagd wordt.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-kunst-van-de-prehistorie-tot-de-middeleeuwen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Hang een tijdlijn op aan enkele vaste punten: de grotschilderingen rond 17.000 jaar "
                    "geleden, de piramiden rond 2500 voor Christus, het Parthenon in de vijfde eeuw voor "
                    "Christus, het Colosseum rond 80 na Christus, romaans in de elfde en twaalfde eeuw, "
                    "gotisch vanaf de twaalfde.",
             waarom=[
                 "Let op de laatste twee: romaans komt vóór gotisch, en de gotiek begint in Frankrijk rond "
                 "1140. Grieks komt vóór Romeins, en dat is bij de bouwkunst ook te zien, want de Romeinen "
                 "bouwden verder op de Griekse vormen.",
                 "Dit is een belangrijke gedachte voor het hele vak: ons begrip van kunst, met een "
                 "kunstenaar die vrij werkt en een publiek dat bewondert, is zelf historisch en ontstond "
                 "pas in de renaissance.",
             ]),
        dict(aanpak="Leer de drie zuilorden aan hun kapiteel: dorisch is strak, ionisch heeft krullen "
                    "(voluten), korinthisch heeft bladeren. Bij Rome horen de boog, het gewelf, de koepel "
                    "en beton.",
             waarom=[
                 "Aspectiviteit betekent dat elk lichaamsdeel van zijn meest kenbare kant wordt getoond, "
                 "niet zoals het oog het ziet. Egyptische kunst wilde dus niet nabootsen maar duidelijk "
                 "maken, en daarom verandert ze eeuwenlang bijna niet.",
                 "De kern in één zin: de Grieken gaven de vorm, de Romeinen de techniek. Daarom kon Rome "
                 "iets bouwen wat Griekenland niet kon, zoals het Pantheon met zijn koepel en de "
                 "aquaducten.",
             ]),
        dict(aanpak="Romaans of gotisch herken je aan de boog: rond is romaans, spits is gotisch. Al de "
                    "rest volgt daaruit: de spitsboog en de luchtboog maken dunnere muren, grotere ramen "
                    "en meer hoogte mogelijk.",
             waarom=[
                 "Onthoud het als een ketting: spitsboog en kruisribgewelf leiden de druk naar punten, de "
                 "luchtboog vangt die buiten op, dus kunnen de muren dunner en de ramen groter. Eén "
                 "technische vondst verandert het hele gebouw.",
                 "Hier zie je techniek en betekenis samenkomen: de bouwmeesters wilden licht en hoogte om "
                 "religieuze redenen, en de luchtboog was het middel dat het mogelijk maakte.",
                 "Het licht is daarbij geen versiering maar theologie: men zag licht als een beeld van het "
                 "goddelijke. Daarom werd het glasraam zo belangrijk, en niet enkel om de verhalen te "
                 "vertellen.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-kunststromingen-van-de-renaissance-tot-vandaag-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Hang elke stroming op aan één kernwoord: renaissance is evenwicht, barok is beweging, "
                    "impressionisme is licht, expressionisme is gevoel, kubisme is vorm, surrealisme is "
                    "droom. Dan herken je ze aan één kenmerk.",
             waarom=[
                 "Let op het verschil tussen impressionisme en expressionisme: het eerste wil de indruk van "
                 "buiten weergeven, het tweede de uitdrukking van binnen. De namen zeggen het: impressie "
                 "komt binnen, expressie gaat buiten.",
                 "Let op de tegenstelling tussen classicisme en romantiek: ze volgen op elkaar en zijn "
                 "elkaars tegendeel, regels tegenover gevoel. Dat patroon, een stroming die reageert op "
                 "de vorige, komt in de hele kunstgeschiedenis terug.",
             ]),
        dict(aanpak="Kunst verandert niet uit zichzelf maar door iets daarbuiten: een uitvinding, een "
                    "oorlog, een nieuw publiek. Zoek bij zo'n vraag altijd die buitenoorzaak.",
             waarom=[
                 "De fotografie nam de taak van het gelijkende portret over, en die taak was eeuwenlang "
                 "een belangrijke bron van inkomen. Daarmee kwam de vraag vrij: wat kan schilderkunst wat "
                 "een foto niet kan?",
                 "Dada is het sterkste voorbeeld: kunst die zichzelf belachelijk maakt, omdat de oude "
                 "schoonheid na de loopgraven niet meer te verdedigen leek.",
                 "Men noemt die toestand postmodern of pluralistisch. Dat betekent niet dat er niets meer "
                 "gebeurt, maar dat er geen enkele richting is die de toon zet.",
             ]),
        dict(aanpak="Een werk plaatsen doe je met kenmerken uit de beschrijving, niet met een naam die je "
                    "toevallig kent. Noem dus altijd twee concrete dingen die je in het werk ziet.",
             waarom=[
                 "De gekleurde schaduw is het meest verraderlijke kenmerk: vóór het impressionisme waren "
                 "schaduwen bruin of zwart, daarna blauw en paars, omdat men keek naar wat het oog echt "
                 "ziet.",
                 "Daarom schilderden de impressionisten buiten, en soms hetzelfde tafereel op "
                 "verschillende uren van de dag. Monet maakte zo reeksen van dezelfde kathedraal en "
                 "dezelfde hooischelven.",
                 "Stromingen overlappen, lopen door en krijgen hun naam vaak pas achteraf, soms van een "
                 "criticus die het als scheldwoord bedoelde. Jaartallen in een handboek zijn dus "
                 "richtpunten, geen grenzen.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-samenlevingen-inhoud-en-context-van-een-kunstuiting-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Elke contextvraag heeft een eigen gebied: geld, geloof, politiek, techniek, plaats of "
                    "de kunst eromheen. Zoek bij elke vraag naar welk gebied ze peilt.",
             waarom=[
                 "De technische context wordt vaak onderschat: verf in tubes maakte het buiten schilderen "
                 "van de impressionisten mogelijk, en olieverf maakte de fijne lagen van de Vlaamse "
                 "primitieven mogelijk. Techniek bepaalt mee wat een kunstenaar kan doen.",
                 "Dat heet decontextualisering. Veel museumstukken zijn altaarstukken, grafbeelden of "
                 "rituele voorwerpen die nooit bedoeld waren om in een rij aan een witte muur te hangen. "
                 "Daarom staat er een bordje bij, en dat bordje is een deel van de uitleg.",
             ]),
        dict(aanpak="Wie de opdracht gaf, bepaalt vaak het onderwerp en soms de vorm. Noem bij een "
                    "opdrachtgever dus altijd wat die ermee wilde.",
             waarom=[
                 "Een vierde soort is er vandaag bijgekomen: de overheid en de openbare instellingen, met "
                 "subsidies en opdrachten voor openbare ruimte. En de markt zelf: een kunstenaar die werk "
                 "maakt voor een galerie heeft geen opdrachtgever maar wel een koper in gedachten.",
                 "Dat is ook de reden dat we middeleeuwse kunstenaars vaak niet bij naam kennen en "
                 "renaissancekunstenaars wel. Het idee van het genie, de kunstenaar met een eigen visie, "
                 "hoort bij de renaissance en niet bij alle tijden.",
                 "Dat is geen cynisme maar een onderzoeksvraag: wie betaalde, wat wilde die, en wat deed "
                 "de kunstenaar daarmee? Soms volgde hij braaf, soms smokkelde hij er zijn eigen "
                 "boodschap in.",
             ]),
        dict(aanpak="Werk een werk af in drie lagen: wat zie je, hoe is het gemaakt, en wat weet je over "
                    "de omstandigheden? De derde laag kan de betekenis omdraaien, dus hou ze apart.",
             waarom=[
                 "De plaats van bestemming is hier de sleutel: een stadhuis is geen privéwoning. Het werk "
                 "spreekt dus in naam van de stad en niet van één persoon.",
                 "Dat is clair-obscur in dienst van de inhoud: wat je niet ziet, is even belangrijk als "
                 "wat je ziet. Het donker maakt de soldaten naamloos, en dus wisselbaar.",
                 "Dit is de kern van deze bundel: dezelfde beelden kunnen een klaagzang of een "
                 "overwinningsstuk zijn, en enkel de context beslist. Daarom begint kunstbeschouwing met "
                 "wie, wanneer en waar, en niet met mooi of niet mooi.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-richtvragen-en-de-middelen-van-vormgeving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vier stappen in deze orde: beschrijven, analyseren, interpreteren, oordelen. Elke "
                    "stap gebruikt de vorige, dus overslaan kan niet.",
             waarom=[
                 "Let op het verschil tussen analyseren en interpreteren: analyseren gaat over hoe het "
                 "gemaakt is, interpreteren over wat het betekent. Bij analyseren kan je nog naar het werk "
                 "wijzen, bij interpreteren moet je argumenteren.",
                 "Dat is ook de reden dat mooi of niet mooi als eerste reactie zo weinig oplevert: je kijkt "
                 "dan niet meer. Een oordeel aan het einde, met argumenten uit de eerste drie stappen, is "
                 "wel zinvol.",
             ]),
        dict(aanpak="Leer de middelen aan hun effect: perspectief maakt diepte, clair-obscur maakt drama, "
                    "symmetrie maakt rust, complementaire kleuren maken spanning. Dan kan je ze ook "
                    "gebruiken in een bespreking.",
             waarom=[
                 "Lijnperspectief en luchtperspectief werken samen: het eerste met lijnen die naar een "
                 "verdwijnpunt lopen, het tweede met kleur en scherpte. Clair-obscur betekent letterlijk "
                 "licht-donker, en Caravaggio en Rembrandt zijn er de bekendste meesters van.",
                 "Daarom gebruikten renaissanceschilders de driehoek zo vaak in religieuze taferelen: de "
                 "vorm zelf brengt de rust die bij het onderwerp past. Bij barok zie je net diagonalen, "
                 "en die geven beweging.",
             ]),
        dict(aanpak="Loop de vier richtvragen in orde af op dezelfde afbeelding. Let erop dat je in stap "
                    "één nog niets interpreteert en in stap vier een argument geeft.",
             waarom=[
                 "Let erop dat er in een beschrijving geen woorden als mooi, krachtig of saai staan. Enkel "
                 "wat een ander kan nakijken: aantal, kleur, plaats, scherpte.",
                 "Negatieve ruimte is hier het sterkste middel: juist door wat er niet staat, kijk je naar "
                 "de appel. In reclame heet dat whitespace, ook als ze zwart is.",
                 "Een interpretatie mag een vermoeden zijn, maar moet steunen op wat je in stap twee vond. "
                 "Daarom staat interpreteren pas op de derde plaats.",
                 "Een oordeel zonder grond is een mening; een oordeel met een grond uit je analyse is "
                 "kunstbeschouwing. Je mag het werk ook zwak vinden, zolang je zegt waarom.",
             ]),
    ]
)

UITLEGBLADEN["oefenbundel-de-eigenheid-van-de-filosofie-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke vraag af hoe je ze zou beantwoorden. Kan je het opzoeken, "
                   "nameten of natellen, dan is ze niet filosofisch. Moet je eerst uitmaken wat "
                   "een woord betekent, of moet je een antwoord met argumenten verdedigen, dan "
                   "wel. Een vraag is dus niet filosofisch omdat ze moeilijk is, maar omdat een "
                   "meting of een opzoeking ze niet kan beslechten.",
            waarom=[
                "Let op de twee die er het dichtst bij liggen. Wanneer eindigde de Tweede "
                "Wereldoorlog is geen filosofische vraag, al gaat ze over iets groots: de datum "
                "staat vast. Mag je liegen om iemand te beschermen is er wel een, al lijkt ze "
                "klein: geen enkel onderzoek kan uitmaken wat je mag.",
                None,
            ],
        ),
        dict(
            aanpak="Hier moet je filosofie naast een ander vak zetten. Doe dat altijd door de "
                   "vraag te vergelijken, niet het onderwerp: bioloog en filosoof kunnen beide "
                   "over leven spreken, maar de een vraagt hoe het werkt en de ander wat we "
                   "ermee bedoelen en wat het waard is.",
            waarom=[
                "Twee vakken kunnen dus hetzelfde woord in de mond nemen en toch iets heel "
                "anders onderzoeken. Daarom is de scheidingslijn tussen vakken niet het "
                "onderwerp maar het soort vraag.",
                "Pas op dat je filosofie en godsdienst niet tegenover elkaar zet als ongelovig "
                "tegen gelovig. Het verschil zit in waar je mag beginnen: een godsdienst mag "
                "van een geloof vertrekken, de filosofie moet elk vertrekpunt zelf nog "
                "verantwoorden, dat van het geloof én dat van het ongeloof.",
                "Het is geen bescheiden zinnetje maar een methode. Wie meent het al te weten, "
                "stelt geen vragen meer; wie zijn onwetendheid kent, kan beginnen onderzoeken.",
                "Niet waar, maar let op wat dat niet betekent: dat elk antwoord even goed is. "
                "Een antwoord zonder argument of met een tegenspraak erin blijft fout, ook als "
                "er geen enkel juist antwoord vaststaat.",
            ],
        ),
        dict(
            aanpak="Verwondering is de omgekeerde beweging van gewoonte. Je begint niet bij iets "
                   "vreemds maar bij iets gewoons, en je vraagt waarom het eigenlijk zo is. Bij "
                   "de laatste oefening is elk eigen voorbeeld goed, zolang je vraag niet met "
                   "een opzoeking te beantwoorden valt.",
            waarom=[
                "Verwondering is dus geen gevoel dat je overvalt maar iets wat je zelf doet: je "
                "weigert een tijdje om iets vanzelfsprekend te vinden.",
                "Toets je eigen vraag: kan je ze met een cijfer of een opzoeking beantwoorden, "
                "dan heb je nog een feitenvraag en moet je een stap verder.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-oorsprong-van-de-westerse-filosofie-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Mythos en logos zijn twee manieren om iets te verklaren, niet twee tijdperken "
                   "die elkaar netjes opvolgen. Bij de namen hoort telkens één stelling; leer ze "
                   "aan die stelling en niet aan het rijtje.",
            waarom=[
                "Herakleitos en Parmenides staan hier bewust naast elkaar: de ene zegt dat "
                "alles verandert, de andere dat verandering onmogelijk is. Dat is de eerste "
                "grote tegenstelling van de westerse filosofie, en het hele vak dat erop volgt "
                "zoekt een weg tussen die twee.",
                "De breuk zit niet in de inhoud. Dat alles water is, is even moeilijk te "
                "geloven als een verhaal over goden. De breuk zit in wat er van je gevraagd "
                "wordt: een reden die je kan nagaan en tegenspreken.",
            ],
        ),
        dict(
            aanpak="Zet de drie naast elkaar met telkens twee dingen: hoe ze te werk gaan en wat "
                   "ze beweren. Socrates werkt met vragen, Plato met dialogen en ideeën, "
                   "Aristoteles met kijken en ordenen. Die drie manieren van werken bestaan "
                   "vandaag nog in de wetenschap en in de filosofie.",
            waarom=[
                None,
                "Let op de laatste zin van de allegorie, die men vaak vergeet: wie terugkeert "
                "wordt niet geloofd. Plato schrijft dat met Socrates in gedachten, die ter dood "
                "gebracht werd. De allegorie gaat dus niet enkel over kennis maar ook over wat "
                "een samenleving doet met wie haar beeld doorprikt.",
                "Je kan het verschil in één beweging zetten: Plato wijst naar boven, weg van de "
                "zichtbare dingen, Aristoteles wijst naar beneden, naar de dingen zelf. Op de "
                "beroemde fresco van Rafaël staan ze zo ook getekend.",
                "Maieutiek komt van het Griekse woord voor vroedvrouw. Dat beeld is het punt: "
                "Socrates beweert dat hij niets inbrengt, hij helpt enkel naar buiten wat er in "
                "de ander al zat.",
            ],
        ),
        dict(
            aanpak="Hier wordt niet gevraagd wat Socrates of Plato precies bedoelde, maar wat jij "
                   "ervan vindt, met een argument. Een goed antwoord noemt eerst wat er voor de "
                   "stelling pleit, dan wat ertegen pleit, en kiest dan.",
            waarom=[
                "De sterkste tegenwerping is de alledaagse: mensen weten vaak heel goed wat "
                "goed is en doen het toch niet. Wie Socrates wil verdedigen, moet dan een "
                "zwaardere betekenis aan kennen geven dan alleen weten.",
                "Elk voorbeeld waarin je iets voor de werkelijkheid houdt terwijl het voor jou "
                "geselecteerd is, past hier. Het hoeft niet over schermen te gaan: een school, "
                "een dorp of een vriendenkring kan ook een grot zijn.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-soorten-vragen-en-de-filosofische-vraag-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vier soorten, en telkens een eigen toets. Een feitenvraag zoek je op. Een "
                   "begripsvraag vraagt wat een woord betekent. Een waardevraag vraagt of iets "
                   "mag of goed is. Een zinvraag vraagt waarom er iets is of waartoe het dient. "
                   "Hoor je in de vraag een woord als eerlijk, mag of volwassen, kijk dan of er "
                   "naar de betekenis van dat woord gevraagd wordt of naar een beoordeling.",
            waarom=[
                "Wanneer is iemand volwassen lijkt een feitenvraag omdat er een leeftijd op "
                "staat in de wet. Maar de vraag is net wat volwassen betekent, en daarover zegt "
                "die leeftijd niets: hij is gekozen, niet gevonden.",
                None,
            ],
        ),
        dict(
            aanpak="Een gewone vraag filosofisch maken doe je niet door ze moeilijker te maken, "
                   "maar door een stap achteruit te zetten: achter elk cijfer zit een "
                   "vooronderstelling. Vraag naar die vooronderstelling. Een vast hulpmiddel: zet "
                   "mag, moet, betekent of ben ik in je nieuwe vraag.",
            waarom=[
                "Van hoeveel uur naar mag ik zelf kiezen: je verlegt de vraag van een getal naar "
                "wie over je lichaam en je tijd beslist.",
                "Welke straf erop staat kan je opzoeken in het strafwetboek. Wat een straf "
                "rechtvaardig maakt, niet: daar moet je kiezen tussen vergelden, beschermen, "
                "afschrikken of herstellen.",
                "Het aantal gebruikers is een cijfer. De vraag erachter gaat over identiteit: "
                "verandert er iets aan wie je bent als je je voortdurend laat zien.",
                "Let op de tweede helft van dit antwoord. Je vraagt niet alleen wat "
                "intelligentie is, maar ook of de maatstaf zelf eerlijk is. Een octopus "
                "beoordelen op wat een mens kan, zegt meer over ons dan over de octopus.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over het openhouden van een vraag. Een vraag is open "
                   "als er meer dan één antwoord denkbaar is dat je ernstig moet nemen. Zodra je "
                   "eigen mening al in de vraag zit, of zodra ja of nee volstaat, ligt ze dicht.",
            waarom=[
                "Het verraderlijke aan vind je ook niet dat is dat het klinkt als vragen terwijl "
                "het aandringen is. Je herkent zo'n vraag doordat nee zeggen onhoffelijk aanvoelt.",
                "Meningen naast elkaar zetten is nog geen filosofie. Het verschil is de "
                "vervolgvraag: waarom denk je dat, en wat zou je van gedacht doen veranderen.",
                "Niet waar. Een vraag die met ja of nee af is, is een keuzevraag; een "
                "filosofische vraag blijft na dat ja of nee vragen om een reden.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-filosofische-domeinen-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Zes domeinen, en bij elk één kernwoord. Metafysica: bestaan. Kennisleer: "
                   "weten. Ethiek: handelen. Politieke filosofie: samenleven. Esthetica: "
                   "schoonheid en kunst. Logica: de vorm van een redenering. Zoek in de vraag "
                   "dus naar dat kernwoord en niet naar het onderwerp: een vraag over een "
                   "schilderij kan evengoed in de esthetica als in de ethiek thuishoren.",
            waarom=[
                "Metafysica en ontologie worden hier als één domein gegeven. Streng genomen is "
                "de ontologie het deel van de metafysica dat over bestaan gaat; vandaar de twee "
                "namen bij één vraag.",
                "Deze tweede rij is dezelfde reeks domeinen, maar nu met een concrete vraag in "
                "plaats van een algemene. Dat is net de bedoeling: je moet het domein kunnen "
                "herkennen zonder dat het woord erbij staat.",
            ],
        ),
        dict(
            aanpak="Rationalisme en empirisme verschillen over de bron van kennis: het denken of "
                   "de ervaring. Onthoud twee namen per kant, Descartes tegenover Hume, en twee "
                   "beelden: aangeboren ideeën tegenover het onbeschreven blad.",
            waarom=[
                "Het onbeschreven blad is het beeld van Locke: de geest begint leeg en de "
                "ervaring schrijft erop. Aangeboren ideeën zijn het tegendeel: iets wat je al "
                "meehad voor je iets ervoer.",
                "Let op wat Descartes hier precies bewijst. Niet dat hij een lichaam heeft of "
                "dat de wereld bestaat, enkel dat er iemand aan het twijfelen is. Het is een "
                "heel klein maar onwankelbaar vertrekpunt.",
                "Elk bezwaar dat een soort kennis aanwijst die niet uit ervaring komt, is goed. "
                "Naast de wiskunde kan je ook denken aan de logica, of aan het feit dat je uit "
                "ervaring nooit kan afleiden dat iets altijd zo zal blijven, een bezwaar dat "
                "Hume zelf opmerkte.",
            ],
        ),
        dict(
            aanpak="Hier moet je zelf met de domeinen werken. Besef dat eenzelfde kwestie in "
                   "meerdere domeinen past en dat de formulering beslist waar ze belandt.",
            waarom=[
                "Het punt is de laatste zin: door de vraag anders te stellen, verhuist ze van "
                "domein. Dat is geen slordigheid maar iets wat je in een gesprek kan gebruiken, "
                "om te zien waarover het eigenlijk gaat.",
                "Toets je eigen twee vragen: staat er in de ene mag of moet, en in de andere hoe "
                "weet ik, dan heb je echt twee verschillende domeinen en niet twee keer hetzelfde.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-filosofische-vaardigheden-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Een redenering ontleden doe je in twee stappen. Zoek eerst het besluit, dat "
                   "is de zin waar dus, daarom of bijgevolg voor staat. Alles wat overblijft, "
                   "zijn de premissen. Toets daarna of het besluit echt móet volgen, en niet "
                   "alleen aannemelijk klinkt.",
            waarom=[
                None,
                "Pas op met de naam. Hier wordt een gevolg bevestigd en daaruit de voorwaarde "
                "besloten, en dat heet de bevestiging van het gevolg; de ontkende voorwaarde is "
                "de omgekeerde fout, waarbij je uit Lotte studeerde wel besluit dat ze dus "
                "slaagde. Beide zijn ongeldig, en de twee namen worden vaak verwisseld. Waar "
                "het echt om gaat: slagen kan ook op een andere manier mislukken dan door niet "
                "te studeren.",
                "Dit is het verschil dat de hele logica draagt. Alle katten kunnen vliegen, "
                "Minoes is een kat, dus Minoes kan vliegen is perfect geldig en toch onwaar. "
                "Geldigheid zegt dus niets over de werkelijkheid, alleen over de band tussen "
                "premissen en besluit.",
            ],
        ),
        dict(
            aanpak="Zes drogredenen, en bij elk een vast patroon. Op de man spelen: de persoon "
                   "in plaats van het argument. Beroep op de massa: veel in plaats van juist. "
                   "Hellend vlak: een ramp aan het eind van een reeks stappen die niemand "
                   "aantoont. Stroman: een slechtere versie van wat de ander zei. Vals beroep "
                   "op gezag: iemand die er niets van kent. Vals dilemma: twee keuzes waar er "
                   "meer zijn.",
            waarom=[
                "Let op het hellend vlak: het is niet altijd een drogreden. Wie aantoont dat "
                "elke stap de volgende echt waarschijnlijker maakt, geeft een geldig argument. "
                "Het wordt een drogreden als de stappen alleen genoemd worden en niet aangetoond.",
                "Dat is de reden waarom je ze moet leren benoemen. Een drogreden werkt niet "
                "omdat mensen dom zijn, maar omdat ze op het eerste gehoor de vorm van een goed "
                "argument heeft.",
            ],
        ),
        dict(
            aanpak="De derde reeks gaat over het verhelderen van begrippen. De werkwijze is "
                   "altijd dezelfde: geef een definitie, zoek er dan zelf een geval bij dat eraan "
                   "voldoet en toch niet past, en pas je definitie aan. Dat heen en weer is het "
                   "werk zelf, niet een teken dat je het fout had.",
            waarom=[
                "Elke definitie met een eigen tegenvoorbeeld is goed. Het tegenvoorbeeld hoort "
                "wel écht aan je definitie te voldoen, anders weerlegt het niets.",
                "Een gedachte-experiment is geen verzinsel om het verzinsel: het is een proef "
                "waarin je één ding verandert en kijkt wat je oordeel doet. Daarom mag het "
                "onmogelijk zijn, zolang het duidelijk is.",
                "Drie andere regels mogen ook, zolang de laatste erbij staat. Dat je van gedacht "
                "mag veranderen is wat een filosofisch gesprek onderscheidt van een discussie "
                "die je wil winnen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-lichaam-en-geest-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Twee grote standpunten: het dualisme zegt twee soorten dingen, het "
                   "materialisme of fysicalisme zegt één soort. Elk heeft zijn eigen zwakke "
                   "plek, en die twee zwakke plekken staan in dit rijtje: het interactieprobleem "
                   "bij het dualisme, het bewustzijnsprobleem bij het fysicalisme.",
            waarom=[
                "Materialisme en fysicalisme liggen vlak bij elkaar: fysicalisme is de modernere "
                "naam, omdat de natuurkunde vandaag meer kent dan stof alleen, bijvoorbeeld "
                "velden en energie.",
                "Descartes loste het zelf op met de pijnappelklier, de plaats waar geest en "
                "lichaam elkaar zouden raken. Dat antwoord gelooft niemand nog, maar het "
                "probleem is nooit verdwenen, en dat is wat je hier moet kunnen uitleggen.",
            ],
        ),
        dict(
            aanpak="Hier moet je twee kanten kunnen innemen zonder te kiezen. Dat is een "
                   "vaardigheid op zich: eerst het sterkste argument voor, dan het sterkste "
                   "tegen. Bij de derde oefening moet je oppassen voor een te snelle stap van "
                   "een meting naar een besluit over vrijheid.",
            waarom=[
                None,
                "De kracht van dit experiment zit in het woord alles: Mary weet werkelijk elk "
                "feit over kleur. Als ze dan nog iets leert, is er iets wat geen enkel feit over "
                "stof kon zeggen. Wie het fysicalisme verdedigt, antwoordt meestal dat ze geen "
                "nieuw feit leert maar een nieuwe manier om er iets mee te doen.",
                "Niet waar, en de reden is belangrijk. Zo'n meting toont dat je besluit al op weg "
                "was voor je het merkte. Of jij degene bent die het nam, is daarmee niet "
                "uitgemaakt: je hersenen zijn niet iets anders dan jij. Het experiment van Libet "
                "ging bovendien over een klein, willekeurig gebaar, niet over een keuze waar je "
                "over nadenkt.",
            ],
        ),
        dict(
            aanpak="Drie standpunten over vrije wil, en één die vaak vergeten wordt: het "
                   "compatibilisme. Dat zegt niet dat determinisme fout is, maar dat vrij zijn "
                   "iets anders betekent dan onbepaald zijn, namelijk handelen uit je eigen "
                   "wil en zonder dwang.",
            waarom=[
                "Het compatibilisme staat hier twee keer in: eerst als naam, dan als uitleg. Dat "
                "is bewust, want juist bij dat standpunt helpt de naam je niet en de omschrijving "
                "wel.",
                "Dit is de reden waarom de vraag niet alleen voor filosofen is. Merk op dat de "
                "twee doelen van straffen hier uit elkaar vallen: beschermen en voorkomen "
                "blijven overeind zonder vrije wil, vergelden niet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-mens-en-dier-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vier keer dezelfde oefening: iemand noemt iets wat alleen de mens zou kunnen, "
                   "en jij zoekt een dier dat het ook doet. Wie telkens een tegenwerping vindt, "
                   "merkt het patroon: het verschil tussen mens en dier blijkt bijna nooit een "
                   "grens maar een kwestie van meer of minder.",
            waarom=[
                "Je kan het nog scherper stellen: kraaien maken gereedschap niet alleen, ze "
                "bewaren het ook voor later. Dat is precies wat men vroeger als bewijs van "
                "menselijk vooruitdenken aanhaalde.",
                "Let op dat de tegenwerping hier de stelling niet gewoon omkeert maar ze "
                "verbetert. Dat is de beste soort tegenwerping: niet de mens is uniek omdat hij "
                "taal heeft, wel misschien omdat hij met regels oneindig veel nieuwe zinnen kan "
                "vormen.",
                "Hier moet je toegeven dat je het niet weet, en dat is een geldig antwoord. Dat "
                "we niet in een dier kunnen kijken, is zelf een filosofisch probleem; het heet "
                "het probleem van andere geesten en geldt strikt genomen ook voor andere mensen.",
                None,
            ],
        ),
        dict(
            aanpak="Zes begrippen. Twee ervan lijken op elkaar maar zijn het niet: speciesisme "
                   "is het verwijt, antropocentrisme het standpunt dat verweten wordt. En let op "
                   "sentiëntie: dat is kunnen voelen, niet kunnen denken. Juist dat onderscheid "
                   "beslist in de dierenethiek wie meetelt.",
            waarom=[
                "De mens als tekortwezen hoort er een beetje tussen uit: het is geen begrip uit "
                "de dierenethiek maar uit de antropologie. De gedachte is dat de mens net door "
                "zijn gebrek aan instinct en vacht zichzelf moet vormen, en dat daarin zijn "
                "cultuur ontstaat.",
                "Bentham verschuift de vraag van vermogen naar kwetsbaarheid, en dat heeft "
                "gevolgen. Op verstand kan je gradaties maken, en dan vallen ook baby's en zwaar "
                "zieke mensen buiten de kring. Op lijden niet.",
            ],
        ),
        dict(
            aanpak="Bij de laatste twee wordt niet gevraagd wat juist is maar dat je een "
                   "standpunt opbouwt. De vaste vorm: een stelling, minstens één reden, en één "
                   "toegeving aan de andere kant. Die toegeving is geen zwakte; ze toont dat je "
                   "het tegenargument gelezen hebt.",
            waarom=[
                "Merk op dat de argumenten voor vlees het dierenwelzijn niet ontkennen maar een "
                "voorwaarde stellen: als het dier goed leeft en pijnloos sterft. Zo wordt het "
                "een argument over hoe, niet over of, en dat is het eerlijkste debat.",
                "Toets je drie zinnen: staat er een stelling, een omdat en een hoewel, dan is "
                "het goed, ook als je besluit het tegenovergestelde is van dat van je buur.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-ethische-stromingen-en-hun-filosofen-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Drie stromingen, en elk kijkt naar een ander punt van dezelfde handeling. "
                   "Deugdethiek kijkt naar de persoon, plichtethiek naar de handeling en de "
                   "regel, gevolgenethiek naar de uitkomst. Onthoud ze aan die drie woorden "
                   "persoon, regel en uitkomst, en de namen volgen van zelf.",
            waarom=[
                None,
                "Lees de zinnen en zoek telkens waar ze naar kijken. Handel zo dat je regel een "
                "wet voor iedereen kan zijn gaat over de regel, dus plichtethiek, ook al staat "
                "het woord plicht er niet in. Wat zou een eerlijk mens hier doen gaat over de "
                "persoon, dus deugdethiek.",
            ],
        ),
        dict(
            aanpak="De sterke en de zwakke punten van de twee grote stromingen zijn elkaars "
                   "spiegelbeeld: wat de plichtethiek beschermt, is net wat de gevolgenethiek "
                   "kan opofferen, en wat de gevolgenethiek meeneemt, is net wat de plichtethiek "
                   "negeert. Leer ze dus als een paar, niet apart.",
            waarom=[
                "Kant gaf twee formuleringen, en die tweede is de nuttigste om te onthouden: "
                "een mens nooit louter als middel. Daarmee kan je bijna elk ethisch vraagstuk "
                "aanpakken, ook zonder de eerste formulering.",
                None,
                "Pas op dat je gevolgenethiek niet verwart met eigenbelang. Ze telt juist het "
                "geluk en het leed van álle betrokkenen, jouw eigen stem even zwaar als die van "
                "een vreemde. Dat maakt ze veeleisend, niet gemakzuchtig.",
                "De middenweg is geen rekenkundig midden, maar het juiste midden voor deze "
                "persoon in deze situatie. Voor een brandweerman ligt moed elders dan voor een "
                "voorbijganger, en dat hoort zo bij Aristoteles.",
            ],
        ),
        dict(
            aanpak="Het tramdilemma bestaat in twee versies met dezelfde rekensom, en net dat "
                   "verschil is het punt. Antwoord dus niet wat jij zou doen, maar wat elke "
                   "stroming zegt, en zoek daarna waarom ons gevoel de twee versies toch anders "
                   "beoordeelt.",
            waarom=[
                None,
                "Let erop dat de plichtethicus de vijf doden niet goedkeurt. Hij zegt enkel dat "
                "jij die man niet mag gebruiken; dat de tram verder rijdt, is niet jouw daad maar "
                "wat er gebeurt. Dat onderscheid tussen doen en laten gebeuren draagt hier het "
                "hele antwoord.",
                "Dit is de kern van de hele oefening. Het verschil in gevoel is geen fout in ons "
                "denken dat je moet wegrekenen: het is zelf een gegeven waar een ethiek "
                "rekenschap van moet geven. Daarom wordt dit dilemma al vijftig jaar besproken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-begrippen-uit-de-moraalfilosofie-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vier paren die vaak door elkaar lopen. Moraal is wat een groep vindt, ethiek "
                   "is het nadenken erover. Een waarde is wat je belangrijk vindt, een norm is de "
                   "regel die eruit volgt. Zoek in elke omschrijving dus of het gaat over wat men "
                   "doet of over het onderzoek ernaar.",
            waarom=[
                None,
                "Een goed voorbeeld laat de ethiek de moraal bevrágen. Zegt je voorbeeld twee "
                "keer hetzelfde met andere woorden, dan heb je het verschil nog niet te pakken.",
                "Waar, maar er zit een valkuil in de omgekeerde richting. Uit één waarde volgt "
                "niet één norm: eerlijkheid kan zowel de norm je zegt altijd de waarheid als de "
                "norm je zwijgt liever dan te kwetsen opleveren. De waarde beslist dus niet "
                "alleen.",
            ],
        ),
        dict(
            aanpak="Een feit kan je nagaan, waar of onwaar. Een waardeoordeel beoordeelt iets. "
                   "De woorden te veel, moet, barbaars en beter verraden bijna altijd een "
                   "waardeoordeel. Pas op: dat een uitspraak een cijfer bevat, maakt ze nog geen "
                   "feit, en dat ze over moraal gaat, maakt ze nog geen waardeoordeel.",
            waarom=[
                "Vergelijk de paren twee aan twee: ze gaan telkens over hetzelfde onderwerp, "
                "eerst als feit en dan als oordeel. Dat is net hoe het in een discussie gaat: "
                "iedereen is het over het cijfer eens en oneens over wat eruit volgt.",
                "Dit heet ook de naturalistische drogreden, al gebruiken filosofen die naam voor "
                "iets nauwers. Waar het om gaat: er is altijd nog een waardepremisse nodig, "
                "en die blijft in een discussie vaak onuitgesproken.",
                "Elk voorbeeld waarin van zo is naar zo hoort gesprongen wordt, is goed. Andere "
                "veelvoorkomende: het is altijd zo geweest, dus het hoort zo. Of: de meerderheid "
                "vindt het, dus het is juist.",
            ],
        ),
        dict(
            aanpak="Het schadebeginsel is een grens aan de macht van de samenleving, niet aan "
                   "jouw eigen keuzes. Bij elke toepassing moet je dus twee vragen stellen: wie "
                   "wordt hier geschaad, en is die schade alleen voor jezelf? Het antwoord is "
                   "zelden zuiver, en net daar wordt de oefening interessant.",
            waarom=[
                None,
                "Dit is het klassieke tegenargument tegen Mill: in een samenleving met gedeelde "
                "ziekteverzekering raakt bijna elke schade aan jezelf ook de anderen. Wie dat "
                "argument doortrekt, kan er echter bijna alles mee verbieden, en dat is de "
                "tegenwerping op de tegenwerping.",
                "De paradox komt van Popper. Merk op dat ze geen vrijbrief is om alles te "
                "verbieden wat je niet bevalt: ze zegt enkel dat tolerantie niet verplicht is "
                "tegenover wie de tolerantie zelf wil opheffen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ethische-vraagstukken-analyseren-boost-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Zes stappen, en de volgorde is geen vormkwestie. Eerst kijken wat er aan de "
                   "hand is, dan wie het raakt, dan wat de vraag precies is; pas daarna "
                   "argumenten, stromingen en een besluit. Wie met stap zes begint, zoekt enkel "
                   "nog argumenten voor wat hij al vond.",
            waarom=[
                None,
                "Dat is in een discussie ook het nuttigste om te weten: hoor je mensen van "
                "mening verschillen, vraag dan eerst of ze het over de feiten eens zijn. Heel "
                "vaak blijkt het daar al mis te gaan, en dan is de ethische discussie nog niet "
                "begonnen.",
            ],
        ),
        dict(
            aanpak="Hier werk je het stappenplan af op één casus. Twee dingen helpen. Noem bij "
                   "de betrokkenen ook wie er niet bij is maar wel geraakt wordt, en formuleer "
                   "de vraag als een mag-vraag met beide belangen erin, zodat ze niet al "
                   "beantwoord is.",
            waarom=[
                "Let op de laatste in de lijst: de samenleving. Dat lijkt ver weg, maar als één "
                "school gezichtsherkenning normaal maakt, verschuift wat we overal normaal "
                "vinden. Die gewenning is zelf een gevolg om mee te rekenen.",
                "Toets je eigen zin: staan er beide belangen in, privacy én veiligheid, dan is "
                "ze goed. Staat er enkel mag een school camera's plaatsen, dan heb je de helft "
                "van het vraagstuk weggelaten.",
                "Het sterkste argument tegen is het tweede: gezichtsgegevens kan je niet "
                "veranderen zoals een wachtwoord. Dat maakt het risico van een lek blijvend, en "
                "dat is iets anders dan een gewone inbreuk op privacy.",
                "Merk op dat de gevolgenethicus hier niet gewoon ja zegt. Hij stelt voorwaarden, "
                "een grote winst en een klein risico, en net die voorwaarden kan je nagaan. Zo "
                "wordt een stroming een werktuig in plaats van een mening.",
                "Het voorbeeldantwoord kiest het middel met de meeste winst en de minste "
                "inbreuk. Dat is een vaste manier om zo'n vraagstuk te beslechten: zoek of er "
                "een lichter middel bestaat dat hetzelfde doel haalt.",
            ],
        ),
        dict(
            aanpak="Twee korte vraagstukken, en bij elk wordt enkel de kernvraag en één argument "
                   "per kant gevraagd. De kernvraag is niet wat moet er gebeuren maar op welke "
                   "grond mag je zo beslissen; daarin zit het hele vraagstuk.",
            waarom=[
                "Het verschil tussen de twee antwoorden is een verschil tussen stromingen: "
                "gewonnen levensjaren tellen is gevolgenethiek, elk leven telt evenveel is "
                "plichtethiek. Daarom kan je hier niet uitrekenen wie gelijk heeft.",
                "Let op het tweede argument: het bezwaar is niet dat de machine zich vergist, "
                "maar dat ze zich onzichtbaar vergist, en altijd in dezelfde richting. Een mens "
                "die discrimineert kan je aanspreken; een model dat het uit het verleden leerde, "
                "moet eerst iemand opmerken.",
            ],
        ),
    ],
)

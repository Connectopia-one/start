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

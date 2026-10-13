# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij sociale en gedragswetenschappen 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: casussen om
in te delen, schema's om aan te vullen, en opdrachten waarbij je een begrip op
je eigen leven moet toepassen. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-doorstroom/sociale-en-gedragswetenschappen.json` en naast
`maak_sociale_en_gedragswetenschappen.py`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Sociale en gedragswetenschappen"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
NIVEAU = "-boost-doorstroom"
VOOR = "oefenbundel-"

W = "120px"
WW = "200px"
WL = "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een casus: onderstreep eerst wat er feitelijk gebeurt, pas daarna oordeel je.",
    "Een begrip ken je pas als je er een eigen voorbeeld bij kan geven.",
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
zet("ontwikkeling-groeien-rijpen-en-leren",
    titel="Ontwikkeling: groeien, rijpen en leren",
    reeksen=[
        dict(kop="Groei, rijping of leren?",
             opdracht="Schrijf bij elk voorbeeld op welk van de drie het is.",
             oefeningen=[
                 ("rij", [("Een kind wordt tussen zijn tiende en twaalfde twaalf centimeter langer.",
                           "groei"),
                          ("Een baby kan rechtop zitten zodra zijn rugspieren sterk genoeg zijn.",
                           "rijping"),
                          ("Een jongere leert fietsen na veel vallen en opstaan.", "leren"),
                          ("Een puber krijgt een zwaardere stem.", "rijping"),
                          ("Een kind leert de tafel van zeven.", "leren"),
                          ("Een kind weegt op zijn zesde zes kilo meer dan op zijn vijfde.",
                           "groei")],
                  "Wat is dit?", WW),
                 ("open", "Wat is het verschil tussen groei en rijping?",
                  "Groei gaat over toenemen in omvang, dus langer en zwaarder worden. Rijping "
                  "gaat over het klaar raken van het lichaam en het zenuwstelsel, waardoor "
                  "iets mogelijk wordt dat eerst niet kon.", 3),
                 ("open", "Waarom heeft leren zonder rijping weinig zin? Geef een voorbeeld.",
                  "Je kan iets pas leren als het lichaam er klaar voor is. Een baby van zes "
                  "maanden leer je niet lopen, hoeveel je ook oefent: zijn spieren en evenwicht "
                  "zijn nog niet rijp.", 3),
             ]),
        dict(kop="Aanleg en omgeving",
             opdracht="Vul aan of antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe noemen we alles wat je bij je geboorte meekrijgt?",
                  "aanleg / erfelijkheid", WW),
                 ("kort", "Hoe noemen we alles wat van buitenaf op je inwerkt?",
                  "de omgeving / het milieu", WW),
                 ("open", "Twee broers groeien in hetzelfde gezin op en worden heel "
                          "verschillende mensen. Geef twee verklaringen.",
                  "Ze hebben een andere aanleg, en de omgeving is voor hen niet dezelfde: ze "
                  "hebben een andere plaats in het gezin, andere vrienden, andere leerkrachten "
                  "en ze roepen bij dezelfde ouders ander gedrag op.", 4),
                 ("waar", "Volgens de huidige wetenschap bepaalt de aanleg alles en doet de "
                          "omgeving er weinig toe.", False),
             ]),
        dict(kop="Kenmerken van ontwikkeling",
             opdracht="Vul de tabel aan met een voorbeeld uit je eigen leven.",
             oefeningen=[
                 ("tabel", ["kenmerk", "wat het betekent", "jouw voorbeeld"],
                  [["ontwikkeling verloopt in fasen", "er zijn herkenbare stappen", None],
                   ["ontwikkeling is levenslang", "ze stopt niet bij achttien", None],
                   ["ontwikkeling verloopt ongelijk", "niet elk gebied even snel", None],
                   ["ontwikkeling is onomkeerbaar", "je gaat niet terug naar een vorige fase",
                    None]],
                  "Elk eigen voorbeeld is goed zolang het bij het kenmerk past: bijvoorbeeld "
                  "eerst kruipen en dan lopen; op je vijftigste nog een taal leren; sneller "
                  "groeien dan dat je gedrag meegroeit; opnieuw leren lezen gaat niet terug "
                  "naar niet kunnen lezen.", "200px"),
                 ("open", "Leg uit wat een gevoelige periode is.",
                  "Een tijd waarin een kind bijzonder vatbaar is om iets te leren, zoals taal "
                  "in de eerste levensjaren. Daarna lukt het nog wel, maar moeizamer.", 3),
             ]),
        dict(kop="Een casus",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Jonas is elf. Hij is dit jaar tien centimeter gegroeid en past in "
                  "geen enkele broek meer. Op school leert hij breuken optellen, wat eerst "
                  "niet lukte. Thuis valt zijn moeder op dat hij sinds kort zelf merkt wanneer "
                  "zijn zus verdrietig is, iets wat hij vroeger niet zag.</em></p>"),
                 ("open", "Benoem de drie soorten verandering die in deze tekst staan.",
                  "Groei (tien centimeter), leren (breuken optellen) en rijping of sociale "
                  "ontwikkeling (merken dat zijn zus verdrietig is).", 3),
                 ("open", "Welke kenmerken van ontwikkeling zie je terug in deze casus?",
                  "Dat ontwikkeling op meerdere gebieden tegelijk loopt, en ongelijk: zijn "
                  "lichaam, zijn denken en zijn omgang met anderen veranderen alle drie, maar "
                  "niet in hetzelfde tempo.", 3),
             ]),
    ])


# ============================================================
zet("de-fysieke-ontwikkeling",
    titel="De fysieke ontwikkeling",
    reeksen=[
        dict(kop="De grote lijn",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de ontwikkeling van het hoofd naar de voeten",
                           "cefalocaudaal"),
                          ("de ontwikkeling van het midden naar buiten",
                           "proximodistaal"),
                          ("de grote bewegingen van het hele lichaam", "grove motoriek"),
                          ("de kleine bewegingen van vingers en handen", "fijne motoriek"),
                          ("de eerste groeispurt", "het eerste levensjaar"),
                          ("de tweede groeispurt", "de puberteit")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Leg uit waarom een baby eerst zijn hoofd kan optillen en pas veel "
                          "later kan lopen.",
                  "De ontwikkeling verloopt van boven naar beneden: het zenuwstelsel rijpt "
                  "eerst in het hoofd en de nek, en pas daarna in de romp en de benen.", 3),
             ]),
        dict(kop="De puberteit",
             opdracht="Zet elk kenmerk in de juiste kolom.",
             oefeningen=[
                 ("tabel", ["kenmerk", "primair of secundair geslachtskenmerk"],
                  [["de baarmoeder", None], ["de baardgroei", None],
                   ["de teelballen", None], ["de borstontwikkeling", None],
                   ["de bredere heupen", None], ["de zwaardere stem", None]],
                  "baarmoeder: primair · baardgroei: secundair · teelballen: primair · "
                  "borstontwikkeling: secundair · heupen: secundair · stem: secundair",
                  "160px"),
                 ("kort", "Hoe heet de eerste menstruatie?", "de menarche", WW),
                 ("kort", "Hoe heet de klier die de puberteit op gang brengt?",
                  "de hypofyse", WW),
                 ("open", "Waarom zijn meisjes in het eerste middelbaar vaak langer dan "
                          "jongens, en later niet meer?",
                  "De groeispurt begint bij meisjes gemiddeld twee jaar vroeger. Jongens "
                  "beginnen later maar groeien dan langer en meer, zodat ze meisjes "
                  "inhalen.", 3),
             ]),
        dict(kop="Hersenen in ontwikkeling",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Welk hersendeel rijpt als laatste uit?",
                  "de prefrontale cortex / de voorste hersenschors", WW),
                 ("kort", "Tot ongeveer welke leeftijd duurt dat?",
                  "tot ongeveer 25 jaar", W),
                 ("open", "Waarom nemen pubers meer risico's dan volwassenen? Gebruik de "
                          "begrippen beloningssysteem en prefrontale cortex.",
                  "Het beloningssysteem is in de puberteit al volop actief en zoekt sterke "
                  "prikkels, terwijl de prefrontale cortex, die de rem en de planning "
                  "verzorgt, nog niet is uitgerijpt. De aandrijving is er dus eerder dan de "
                  "rem.", 4),
                 ("open", "Wat is snoeien of pruning in de hersenen?",
                  "Het opruimen van verbindingen die weinig gebruikt worden, zodat de "
                  "verbindingen die wel gebruikt worden sneller en sterker worden.", 3),
             ]),
        dict(kop="Een casus",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Lotte is dertien en de kleinste van haar klas. Haar vriendinnen "
                  "hebben allemaal al hun eerste menstruatie gehad. Ze vraagt zich af of er "
                  "iets mis is met haar. Haar moeder was vroeger ook een laatbloeier.</em></p>"),
                 ("open", "Wat zou je Lotte uitleggen over het tempo van de puberteit?",
                  "Dat het normale bereik heel breed is: de puberteit kan bij meisjes tussen "
                  "ongeveer acht en dertien jaar beginnen. Te vroeg of te laat zegt niets over "
                  "hoe ze er uiteindelijk uitziet.", 3),
                 ("open", "Welke rol speelt erfelijkheid hier?",
                  "Het tempo van de puberteit is sterk erfelijk; dat haar moeder laat was, "
                  "maakt het waarschijnlijk dat Lotte dat ook is.", 2),
                 ("waar", "Een kind dat vroeg in de puberteit komt, wordt uiteindelijk altijd "
                          "groter dan een laatbloeier.", False),
             ]),
    ])


# ============================================================
zet("de-cognitieve-ontwikkeling-volgens-piaget",
    titel="De cognitieve ontwikkeling volgens Piaget",
    reeksen=[
        dict(kop="De vier stadia",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["stadium", "leeftijd", "wat er nieuw is"],
                  [["sensomotorisch", None, None], ["preoperationeel", None, None],
                   ["concreet-operationeel", None, None], ["formeel-operationeel", None, None]],
                  "sensomotorisch: 0 tot 2 jaar, leren via zintuigen en bewegen, "
                  "objectpermanentie · preoperationeel: 2 tot 7 jaar, symbolen en taal, nog "
                  "egocentrisch · concreet-operationeel: 7 tot 11 jaar, logisch denken over "
                  "wat er is, conservatie · formeel-operationeel: vanaf 11 jaar, denken over "
                  "wat mogelijk is, hypotheses", "190px"),
                 ("rij", [("een kind zoekt een bal die onder een doek verdwijnt",
                           "sensomotorisch"),
                          ("een kind doet alsof een stok een zwaard is", "preoperationeel"),
                          ("een kind weet dat het water gelijk blijft in een ander glas",
                           "concreet-operationeel"),
                          ("een jongere bedenkt hoe de wereld zou zijn zonder geld",
                           "formeel-operationeel"),
                          ("een kind denkt dat iedereen ziet wat hij ziet", "preoperationeel"),
                          ("een kind sorteert blokken op kleur én op vorm tegelijk",
                           "concreet-operationeel")],
                  "In welk stadium hoort dit?", WW),
             ]),
        dict(kop="De begrippen van Piaget",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het inpassen van nieuwe informatie in wat je al weet?",
                  "assimilatie", WW),
                 ("kort", "Hoe heet het aanpassen van je schema aan nieuwe informatie?",
                  "accommodatie", WW),
                 ("open", "Een kind noemt elk dier met vier poten een hond. Dan ziet het een "
                          "koe. Leg uit wat er bij assimilatie gebeurt en wat bij "
                          "accommodatie.",
                  "Bij assimilatie noemt het de koe ook een hond: het past het nieuwe dier in "
                  "het oude schema. Bij accommodatie maakt het een nieuw schema voor koe, "
                  "omdat het oude schema niet meer klopt.", 4),
                 ("kort", "Hoe heet het besef dat iets blijft bestaan als je het niet ziet?",
                  "objectpermanentie", WW),
                 ("kort", "Hoe heet het besef dat hoeveelheid niet verandert door een andere "
                          "vorm?", "conservatie", WW),
             ]),
        dict(kop="Een proefje uitleggen",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Je giet water uit een breed, laag glas over in een smal, hoog glas. "
                  "Een kind van vier zegt dat er nu meer water is. Een kind van acht zegt dat "
                  "het evenveel blijft.</em></p>"),
                 ("open", "Hoe heet dit proefje en wat test het?",
                  "Het is een conservatieproef; ze test of een kind begrijpt dat de "
                  "hoeveelheid gelijk blijft als de vorm verandert.", 3),
                 ("open", "Waarom zegt het kind van vier dat er meer water is?",
                  "Het let maar op één kenmerk tegelijk, hier de hoogte, en kan de handeling "
                  "niet in gedachten terugdraaien.", 3),
                 ("open", "In welk stadium zit elk van de twee kinderen?",
                  "Het kind van vier zit in het preoperationele stadium, dat van acht in het "
                  "concreet-operationele.", 2),
                 ("open", "Noem één punt van kritiek op de theorie van Piaget.",
                  "Hij onderschatte wat jonge kinderen kunnen: met eenvoudiger opdrachten "
                  "blijken ze vaardigheden vroeger te hebben. Ook verlopen de stadia minder "
                  "strak en minder voor alle gebieden tegelijk dan hij dacht.", 4),
             ]),
    ])


# ============================================================
zet("de-morele-ontwikkeling-volgens-kohlberg",
    titel="De morele ontwikkeling volgens Kohlberg",
    reeksen=[
        dict(kop="De drie niveaus en zes stadia",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["niveau", "stadium 1", "stadium 2"],
                  [["preconventioneel", None, None], ["conventioneel", None, None],
                   ["postconventioneel", None, None]],
                  "preconventioneel: straf vermijden / eigenbelang en ruilen · "
                  "conventioneel: de brave jongen, wat anderen van je vinden / wet en orde · "
                  "postconventioneel: sociaal contract en rechten / universele "
                  "ethische principes", "200px"),
                 ("rij", [("Ik doe het niet, want ik word gestraft.", "stadium 1"),
                          ("Ik help jou als jij mij helpt.", "stadium 2"),
                          ("Ik doe het omdat men dat van mij verwacht.", "stadium 3"),
                          ("Een wet is een wet, anders is het chaos.", "stadium 4"),
                          ("De wet kan veranderd worden als ze onrechtvaardig is.",
                           "stadium 5"),
                          ("Een mensenleven telt zwaarder dan eender welke wet.",
                           "stadium 6")],
                  "In welk stadium hoort deze redenering?", WW),
                 ("open", "Waarom kijkt Kohlberg naar de redenering en niet naar het antwoord?",
                  "Twee mensen kunnen hetzelfde doen om heel verschillende redenen. Het niveau "
                  "van morele ontwikkeling zit in het waarom, niet in het wat.", 3),
             ]),
        dict(kop="Het dilemma van Heinz",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<p><em>De vrouw van Heinz is doodziek. Eén apotheker heeft een medicijn dat "
                  "haar kan redden, maar vraagt er tien keer de kostprijs voor. Heinz kan het "
                  "niet betalen. Hij breekt 's nachts in en neemt het medicijn mee.</em></p>"),
                 ("rij", [("Hij mag dat niet, hij komt in de gevangenis.", "stadium 1"),
                          ("Hij mag dat, want hij wil zijn vrouw nog nodig hebben.",
                           "stadium 2"),
                          ("Een goede echtgenoot doet dat voor zijn vrouw.", "stadium 3"),
                          ("Stelen is tegen de wet, wat de reden ook is.", "stadium 4"),
                          ("De wet beschermt eigendom, maar leven gaat voor.", "stadium 5"),
                          ("Het recht op leven is een principe boven elke wet.", "stadium 6")],
                  "Welk stadium hoort bij deze reactie?", WW),
                 ("open", "Twee leerlingen zeggen allebei dat Heinz mag stelen. Kan hun "
                          "stadium toch verschillen? Leg uit.",
                  "Ja. De een kan het zeggen omdat hij zijn vrouw nodig heeft (stadium 2), de "
                  "ander omdat het recht op leven boven de wet staat (stadium 6). Het antwoord "
                  "is hetzelfde, de redenering niet.", 4),
             ]),
        dict(kop="Kritiek en toepassing",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Welke kritiek gaf Carol Gilligan op Kohlberg?",
                  "Dat zijn schaal gebouwd is op rechtvaardigheid en regels, een manier van "
                  "redeneren die bij jongens vaker voorkomt, en dat zorg en verbondenheid "
                  "daardoor als een lager niveau scoren terwijl ze dat niet zijn.", 4),
                 ("open", "Noem nog twee punten van kritiek.",
                  "De dilemma's zijn gekunsteld en staan ver van het echte leven, en wat mensen "
                  "zeggen komt niet altijd overeen met wat ze doen. Daarbij zijn de hoogste "
                  "stadia sterk westers gekleurd.", 4),
                 ("open", "Geef een voorbeeld van stadium 4 uit je eigen schoolleven.",
                  "Bijvoorbeeld: ik spiek niet omdat het schoolreglement dat verbiedt en "
                  "regels nu eenmaal voor iedereen gelden.", 3),
             ]),
    ])


# ============================================================
zet("de-sociale-ontwikkeling-en-de-gehechtheid",
    titel="De sociale ontwikkeling en de gehechtheid",
    reeksen=[
        dict(kop="De vier gehechtheidsstijlen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["stijl", "bij het weggaan", "bij het terugkomen"],
                  [["veilig gehecht", None, None], ["vermijdend", None, None],
                   ["ambivalent", None, None], ["gedesorganiseerd", None, None]],
                  "veilig: huilt, maar laat zich troosten en speelt weer verder · "
                  "vermijdend: reageert weinig, negeert de ouder bij terugkomst · "
                  "ambivalent: erg overstuur, zoekt troost maar duwt die ook weg · "
                  "gedesorganiseerd: tegenstrijdig gedrag, bevriest of nadert met afgewend "
                  "hoofd", "190px"),
                 ("kort", "Hoe heet de proef waarmee dit onderzocht wordt?",
                  "de vreemdesituatietest", WW),
                 ("kort", "Wie bedacht die proef?", "Mary Ainsworth", WW),
                 ("kort", "Wie bedacht de gehechtheidstheorie?", "John Bowlby", WW),
             ]),
        dict(kop="Casussen",
             opdracht="Welke stijl zie je, en waaraan?",
             oefeningen=[
                 ("open", "Milan van anderhalf huilt hard als zijn papa de kamer uit gaat. Als "
                          "papa terugkomt, loopt hij naar hem toe, laat zich even knuffelen en "
                          "gaat daarna weer spelen.",
                  "Veilig gehecht: hij toont zijn verdriet, zoekt troost, neemt die aan en "
                  "durft daarna weer op verkenning.", 3),
                 ("open", "Noor van twee kijkt nauwelijks op als haar mama weggaat, en gaat bij "
                          "haar terugkeer verder met haar blokken zonder te kijken.",
                  "Vermijdend: ze toont geen protest en zoekt geen contact, wat niet betekent "
                  "dat ze geen stress heeft.", 3),
                 ("open", "Sam van twee is ontroostbaar als zijn mama weg is, en als ze "
                          "terugkomt wil hij op haar arm maar slaat haar tegelijk weg.",
                  "Ambivalent: hij zoekt en weigert troost tegelijk en komt niet tot rust.", 3),
                 ("waar", "Een vermijdend gehecht kind heeft geen band met zijn ouder.", False),
             ]),
        dict(kop="Waarom het ertoe doet",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het beeld van jezelf en anderen dat uit de vroege band "
                          "groeit?", "het intern werkmodel", WW),
                 ("open", "Waarom noemt men de ouder een veilige basis?",
                  "Omdat een kind van daaruit durft te verkennen: het gaat weg om te spelen en "
                  "komt terug om bij te tanken als het schrikt.", 3),
                 ("open", "Wat is sensitieve responsiviteit, en waarom is dat belangrijker dan "
                          "de hoeveelheid tijd die een ouder bij het kind is?",
                  "Het is het opmerken van wat het kind uitzendt en er juist en op tijd op "
                  "ingaan. Een kind hecht zich aan wie betrouwbaar reageert, niet aan wie het "
                  "meeste uren aanwezig is.", 4),
                 ("open", "Kan een gehechtheidsstijl later nog veranderen? Leg uit.",
                  "Ja. Een stijl is geen stempel: nieuwe betrouwbare relaties, een partner of "
                  "therapie kunnen het werkmodel bijstellen. Het gaat wel trager naarmate je "
                  "ouder wordt.", 3),
             ]),
    ])


# ============================================================
zet("de-psychosociale-ontwikkeling-volgens-erikson",
    titel="De psychosociale ontwikkeling volgens Erikson",
    reeksen=[
        dict(kop="De acht fasen",
             opdracht="Vul de tegenstelling en de leeftijd aan.",
             oefeningen=[
                 ("tabel", ["fase", "tegenstelling", "ongeveer"],
                  [["zuigeling", None, None], ["peuter", None, None],
                   ["kleuter", None, None], ["schoolkind", None, None],
                   ["adolescent", None, None], ["jonge volwassene", None, None],
                   ["volwassene", None, None], ["ouderdom", None, None]],
                  "zuigeling: basisvertrouwen tegenover wantrouwen, 0-1 · "
                  "peuter: autonomie tegenover schaamte en twijfel, 1-3 · "
                  "kleuter: initiatief tegenover schuldgevoel, 3-6 · "
                  "schoolkind: vlijt tegenover minderwaardigheid, 6-12 · "
                  "adolescent: identiteit tegenover rolverwarring, 12-20 · "
                  "jonge volwassene: intimiteit tegenover isolement, 20-40 · "
                  "volwassene: zorgzaamheid tegenover stagnatie, 40-65 · "
                  "ouderdom: integriteit tegenover wanhoop, 65 en ouder", "210px"),
                 ("open", "Waarom noemt Erikson zijn fasen psychosociaal en niet psychoseksueel "
                          "zoals Freud?",
                  "Omdat de motor bij hem niet de driften zijn maar de botsing tussen wat de "
                  "persoon wil en wat de samenleving van hem vraagt.", 3),
             ]),
        dict(kop="Casussen",
             opdracht="Welke fase en welke uitkomst?",
             oefeningen=[
                 ("open", "Een peuter wil zelf zijn jas dichtdoen. Zijn vader duwt zijn handen "
                          "weg en doet het snel zelf, elke dag opnieuw.",
                  "Fase autonomie tegenover schaamte en twijfel. Als dit blijft duren, leert "
                  "het kind dat het zelf niets kan en groeit twijfel in plaats van "
                  "autonomie.", 4),
                 ("open", "Een meisje van veertien probeert om de maand een andere stijl, een "
                          "andere vriendengroep en een andere mening uit.",
                  "Fase identiteit tegenover rolverwarring. Uitproberen hoort bij deze fase: zo "
                  "bouwt ze een eigen identiteit op.", 3),
                 ("open", "Een man van vijftig leidt op zijn werk jonge collega's op en vindt "
                          "dat de zinvolste dag van zijn week.",
                  "Fase zorgzaamheid tegenover stagnatie, met een goede uitkomst: hij geeft "
                  "door aan een volgende generatie.", 3),
                 ("waar", "Wie een fase niet goed doorkomt, kan die later niet meer "
                          "inhalen.", False),
             ]),
        dict(kop="Identiteit",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat bedoelt Erikson met rolverwarring?",
                  "Dat een jongere er niet uit raakt wie hij is en wat hij wil, en blijft "
                  "zweven tussen rollen zonder ergens bij te horen.", 3),
                 ("open", "Waarom duurt de identiteitsfase vandaag langer dan in de tijd van "
                          "Erikson?",
                  "Jongeren studeren langer, gaan later samenwonen en werken, en hebben veel "
                  "meer keuzemogelijkheden. Het zoeken duurt daardoor langer.", 3),
                 ("open", "Geef voor jezelf één voorbeeld van iets wat bij jouw fase hoort.",
                  "Elk eerlijk voorbeeld is goed zolang het over identiteit gaat: een keuze "
                  "voor een studie, een mening die van je ouders verschilt, of uitproberen bij "
                  "welke groep je hoort.", 3),
             ]),
    ])


# ============================================================
zet("persoonlijkheid-karakter-en-temperament",
    titel="Persoonlijkheid, karakter en temperament",
    reeksen=[
        dict(kop="Drie woorden uit elkaar houden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het geheel van wat iemand typisch maakt", "persoonlijkheid"),
                          ("de aangeboren manier van reageren, al bij een baby zichtbaar",
                           "temperament"),
                          ("het stuk dat je door opvoeding en ervaring verwerft", "karakter"),
                          ("het duurzame, herkenbare in iemands gedrag", "een trek"),
                          ("de rol die je op een bepaald moment speelt", "geen "
                           "persoonlijkheidskenmerk"),
                          ("de bui waarin je vandaag bent", "een stemming, geen trek")],
                  "Over welk begrip gaat dit?", WW),
                 ("open", "Waarom is temperament geen volledige verklaring voor wie iemand "
                          "wordt?",
                  "Temperament is de basis waarmee je start, maar opvoeding, ervaringen en "
                  "keuzes bouwen daar karakter bovenop. Dezelfde aanleg kan in een andere "
                  "omgeving een heel andere volwassene opleveren.", 4),
             ]),
        dict(kop="De Big Five",
             opdracht="Vul de tabel aan met het kenmerk en zijn tegenpool.",
             oefeningen=[
                 ("tabel", ["trek", "hoge score", "lage score"],
                  [["openheid", None, None], ["consciëntieusheid", None, None],
                   ["extraversie", None, None], ["altruïsme", None, None],
                   ["emotionele stabiliteit", None, None]],
                  "openheid: nieuwsgierig en fantasierijk / houdt van het vertrouwde · "
                  "consciëntieusheid: ordelijk en volhoudend / losser en spontaner · "
                  "extraversie: zoekt gezelschap en prikkels / stiller, laadt alleen op · "
                  "altruïsme: meegaand en behulpzaam / kritisch en op zichzelf · "
                  "emotionele stabiliteit: rustig onder stress / snel ongerust (neuroticisme)",
                  "190px"),
                 ("rij", [("houdt van vaste gewoontes, geen verrassingen", "lage openheid"),
                          ("maakt altijd op tijd af wat hij belooft", "hoge consciëntieusheid"),
                          ("laadt op door een avond alleen thuis", "lage extraversie"),
                          ("vermijdt ruzie en geeft snel toe", "hoog altruïsme"),
                          ("ligt dagen wakker van een opmerking", "lage emotionele stabiliteit"),
                          ("wil altijd iets nieuws proberen", "hoge openheid")],
                  "Welke trek en welke kant?", WW),
                 ("waar", "Een hoge score op een Big Five-trek is altijd beter dan een "
                          "lage.", False),
             ]),
        dict(kop="Hoe meet je dat?",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem twee manieren om persoonlijkheid te onderzoeken en geef bij "
                          "elke één nadeel.",
                  "Een vragenlijst: snel en vergelijkbaar, maar mensen antwoorden sociaal "
                  "wenselijk. Observatie: je ziet echt gedrag, maar ze kost veel tijd en de "
                  "waarnemer kleurt mee.", 4),
                 ("open", "Wat is sociale wenselijkheid?",
                  "Antwoorden geven die goed overkomen in plaats van antwoorden die kloppen.", 2),
                 ("open", "Waarom zegt een persoonlijkheidstest niets over wat iemand waard "
                          "is?",
                  "Een test beschrijft hoe iemand doorgaans reageert, niet of dat goed of "
                  "slecht is. Elke trek heeft sterke en zwakke kanten, afhankelijk van de "
                  "situatie.", 3),
             ]),
    ])


# ============================================================
zet("het-zelfconcept-zelfbeeld-en-zelfwaardering",
    titel="Het zelfconcept: zelfbeeld en zelfwaardering",
    reeksen=[
        dict(kop="De begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het beeld dat je van jezelf hebt", "het zelfbeeld"),
                          ("hoe tevreden je over jezelf bent", "de zelfwaardering"),
                          ("wie je zou willen zijn", "het ideale zelf"),
                          ("hoe je denkt dat anderen je zien", "het sociale zelf"),
                          ("het geloof dat je een taak aankan", "zelfeffectiviteit"),
                          ("het geheel van die beelden samen", "het zelfconcept")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Leg het verschil uit tussen zelfbeeld en zelfwaardering met een "
                          "voorbeeld.",
                  "Het zelfbeeld is de beschrijving: ik ben niet sportief. De zelfwaardering is "
                  "het oordeel erbij: dat vind ik erg, of dat kan mij niets schelen. Hetzelfde "
                  "zelfbeeld kan dus met een hoge of lage zelfwaardering samengaan.", 4),
             ]),
        dict(kop="Waar komt het vandaan?",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het idee dat je jezelf ziet in hoe anderen op je "
                          "reageren?", "de spiegel van anderen", WW),
                 ("open", "Wat is sociale vergelijking, en wanneer doet ze pijn?",
                  "Jezelf meten aan anderen. Ze doet pijn als je je opwaarts vergelijkt met "
                  "mensen die veel beter zijn op iets dat voor jou belangrijk is.", 3),
                 ("open", "Waarom kan sociale media de zelfwaardering van jongeren onder druk "
                          "zetten?",
                  "Je vergelijkt je eigen gewone dag met de uitgekozen hoogtepunten van "
                  "anderen, en dat de hele dag door. De vergelijking is dus oneerlijk en "
                  "voortdurend.", 3),
                 ("waar", "Een hoge zelfwaardering is hetzelfde als arrogantie.", False),
             ]),
        dict(kop="Casussen",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("open", "Amina krijgt een zeven op tien en denkt: ik ben slecht in wiskunde. "
                          "Haar buur krijgt dezelfde zeven en denkt: ik had drie punten meer "
                          "kunnen halen als ik dat hoofdstuk nog eens gedaan had. Wat is het "
                          "verschil?",
                  "Amina schrijft het resultaat toe aan een vaste eigenschap van zichzelf, haar "
                  "buur aan iets wat ze kan veranderen. Dat tweede houdt de zelfwaardering "
                  "heel en geeft een volgende stap.", 4),
                 ("open", "Noem twee dingen die een leerkracht kan doen om het zelfbeeld van "
                          "een leerling te versterken.",
                  "Feedback geven op het werk en de aanpak in plaats van op de persoon, en "
                  "taken geven waarin de leerling echt succes kan boeken zodat zijn "
                  "zelfeffectiviteit groeit.", 4),
                 ("open", "Wat bedoelt men met een groeigerichte mindset?",
                  "Het idee dat je kunnen niet vastligt maar groeit door inspanning en "
                  "oefening, zodat een fout informatie is en geen oordeel.", 3),
             ]),
    ])


# ============================================================
zet("emoties-componenten-en-functies",
    titel="Emoties: componenten en functies",
    reeksen=[
        dict(kop="De vier componenten",
             opdracht="Zet elk zinnetje bij de juiste component.",
             oefeningen=[
                 ("rij", [("mijn hart gaat sneller kloppen", "de lichamelijke component"),
                          ("ik voel me bang", "de belevingscomponent"),
                          ("ik denk: dit loopt verkeerd af", "de cognitieve component"),
                          ("ik zet een stap achteruit", "de gedragscomponent"),
                          ("mijn handen worden klam", "de lichamelijke component"),
                          ("ik roep om hulp", "de gedragscomponent")],
                  "Welke component is dit?", WW),
                 ("open", "Waarom is het nuttig om een emotie in componenten op te delen?",
                  "Omdat je dan ziet waar je kan ingrijpen: je kan je lichaam kalmeren, je "
                  "gedachte bijstellen of je gedrag veranderen, ook als het gevoel zelf blijft "
                  "duren.", 3),
             ]),
        dict(kop="De functies van emoties",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem drie functies van emoties en geef bij elke een voorbeeld.",
                  "Signaalfunctie: angst waarschuwt voor gevaar. Sociale functie: je gezicht "
                  "laat anderen zien hoe het met je gaat. Motiverende functie: woede brengt je "
                  "in beweging om iets recht te zetten.", 4),
                 ("kort", "Hoe heten de emoties die overal ter wereld herkend worden?",
                  "basisemoties", WW),
                 ("open", "Noem er zes.",
                  "Blijdschap, verdriet, angst, woede, walging en verbazing.", 2),
                 ("open", "Wat zijn secundaire of sociale emoties? Geef er twee.",
                  "Emoties die pas ontstaan als je jezelf met de ogen van anderen kan bekijken, "
                  "zoals schaamte, schuld, jaloezie en trots.", 3),
             ]),
        dict(kop="Omgaan met emoties",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("kort", "Hoe heet het sturen van je eigen emoties?",
                  "emotieregulatie", WW),
                 ("rij", [("Ik ga eerst tot tien tellen.", "regulatie vooraf, gedrag"),
                          ("Ik zeg tegen mezelf: hij bedoelde het niet zo.",
                           "herwaardering, cognitief"),
                          ("Ik kijk de hele avond series om er niet aan te denken.",
                           "vermijden"),
                          ("Ik schrijf op wat me dwarszit.", "uiten"),
                          ("Ik hou mijn gezicht in de plooi op het podium.", "onderdrukken"),
                          ("Ik bel mijn beste vriendin.", "steun zoeken")],
                  "Welke manier van omgaan is dit?", WW),
                 ("open", "Waarom werkt onderdrukken op lange termijn slechter dan "
                          "herwaarderen?",
                  "Onderdrukken kost veel energie en verandert het gevoel zelf niet; het "
                  "lichaam blijft gespannen. Herwaarderen verandert de gedachte waardoor de "
                  "emotie zelf zwakker wordt.", 4),
                 ("waar", "Een emotie die je niet toont, is er niet.", False),
             ]),
    ])


# ============================================================
zet("motivatie-en-attributies",
    titel="Motivatie en attributies",
    reeksen=[
        dict(kop="Van binnen of van buiten",
             opdracht="Schrijf intrinsiek of extrinsiek op.",
             oefeningen=[
                 ("rij", [("Ik lees omdat ik het verhaal wil kennen.", "intrinsiek"),
                          ("Ik studeer om geen straf te krijgen.", "extrinsiek"),
                          ("Ik train omdat ik het gevoel na een loop fijn vind.",
                           "intrinsiek"),
                          ("Ik werk voor het loon.", "extrinsiek"),
                          ("Ik oefen gitaar omdat ik beter wil worden.", "intrinsiek"),
                          ("Ik maak mijn taak voor de punten.", "extrinsiek")],
                  "Welke motivatie is dit?", WW),
                 ("open", "Wat kan er gebeuren als je een kind begint te belonen voor iets wat "
                          "het uit zichzelf graag deed?",
                  "De beloning kan de eigen drijfveer verdringen: het kind doet het daarna voor "
                  "de beloning en stopt als die wegvalt.", 3),
             ]),
        dict(kop="De drie basisbehoeften",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("zelf kunnen kiezen hoe je iets aanpakt", "autonomie"),
                          ("het gevoel dat je het kan", "competentie"),
                          ("ergens bij horen", "verbondenheid"),
                          ("een leerkracht die je keuze geeft in je taak", "autonomie"),
                          ("een opdracht net boven je huidige niveau", "competentie"),
                          ("samenwerken in een groep die je graag ziet", "verbondenheid")],
                  "Welke behoefte wordt hier vervuld?", WW),
                 ("open", "Een leerkracht wil haar klas meer motiveren. Geef voor elke "
                          "basisbehoefte één concrete maatregel.",
                  "Autonomie: leerlingen laten kiezen uit drie onderwerpen voor hun taak. "
                  "Competentie: de taak in stappen opdelen zodat elk succes zichtbaar is. "
                  "Verbondenheid: in vaste duo's laten werken en elkaars werk laten "
                  "nalezen.", 4),
             ]),
        dict(kop="Attributies",
             opdracht="Vul de twee kenmerken in: intern of extern, en stabiel of veranderlijk.",
             oefeningen=[
                 ("tabel", ["uitspraak", "intern of extern", "stabiel of veranderlijk"],
                  [["Ik ben nu eenmaal slecht in talen.", None, None],
                   ["Die toets was veel te moeilijk.", None, None],
                   ["Ik had te weinig geoefend.", None, None],
                   ["Ik had geluk met de vragen.", None, None],
                   ["Ik ben er gewoon goed in.", None, None],
                   ["De leerkracht verbetert streng.", None, None]],
                  "slecht in talen: intern en stabiel · toets te moeilijk: extern en stabiel · "
                  "te weinig geoefend: intern en veranderlijk · geluk: extern en veranderlijk · "
                  "goed in: intern en stabiel · strenge leerkracht: extern en stabiel",
                  "150px"),
                 ("open", "Welke attributie is het gunstigst na een slecht resultaat, en "
                          "waarom?",
                  "Intern en veranderlijk, zoals te weinig geoefend. Je houdt dan zelf de hand "
                  "aan het stuur en je ziet meteen wat je een volgende keer anders kan doen.", 4),
                 ("open", "Wat is aangeleerde hulpeloosheid?",
                  "Het opgeven nadat je herhaaldelijk ervaren hebt dat wat je ook doet niets "
                  "uitmaakt; je probeert dan niet meer, ook niet als het wel zou lukken.", 3),
                 ("open", "Wat is de fundamentele attributiefout?",
                  "Bij anderen het gedrag te snel verklaren vanuit hun persoon en te weinig "
                  "vanuit hun situatie, terwijl we bij onszelf net naar de situatie wijzen.", 3),
             ]),
    ])


# ============================================================
zet("cultuur-en-cultuuruitingen",
    titel="Cultuur en cultuuruitingen",
    reeksen=[
        dict(kop="Wat is cultuur?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("alles wat een groep mensen samen maakt en doorgeeft", "cultuur"),
                          ("het zichtbare deel: kledij, eten, feesten", "materiële cultuur"),
                          ("het onzichtbare deel: waarden, normen, opvattingen",
                           "immateriële cultuur"),
                          ("wat een groep belangrijk vindt", "een waarde"),
                          ("de regel die uit die waarde volgt", "een norm"),
                          ("een groep met een eigen stijl binnen een cultuur", "een subcultuur")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Geef bij de waarde 'respect voor ouderen' twee normen.",
                  "Je staat recht in de bus voor iemand die ouder is, en je spreekt een oudere "
                  "aan met u.", 2),
                 ("open", "Leg de ijsbergvergelijking van cultuur uit.",
                  "Boven water zie je kledij, taal, eten en feesten. Onder water zitten de "
                  "waarden, opvattingen over tijd, gezag en familie — veel groter, en net dat "
                  "deel zorgt voor botsingen.", 4),
             ]),
        dict(kop="Hoog, laag, massa",
             opdracht="Zet elk voorbeeld in de juiste kolom.",
             oefeningen=[
                 ("tabel", ["voorbeeld", "welke cultuuruiting"],
                  [["een opera in de schouwburg", None], ["een carnavalstoet", None],
                   ["een serie op een streamingdienst", None], ["een volksdans", None],
                   ["een tentoonstelling moderne kunst", None], ["een voetbalmatch op tv", None]],
                  "opera: hoge cultuur · carnavalstoet: volkscultuur · serie: massacultuur · "
                  "volksdans: volkscultuur · tentoonstelling: hoge cultuur · "
                  "voetbal op tv: massacultuur", "170px"),
                 ("open", "Waarom is het onderscheid tussen hoge en lage cultuur betwist?",
                  "Het is geen eigenschap van het werk zelf maar een oordeel van wie de macht "
                  "heeft om te benoemen. Jazz en film golden ooit als laag en worden nu in "
                  "musea getoond.", 4),
             ]),
        dict(kop="Botsende culturen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het oordelen over een andere cultuur vanuit de eigen "
                          "maatstaven?", "etnocentrisme", WW),
                 ("kort", "Hoe heet het begrijpen van een gewoonte binnen haar eigen "
                          "context?", "cultuurrelativisme", WW),
                 ("open", "Geef een voorbeeld van etnocentrisme uit het dagelijkse leven.",
                  "Bijvoorbeeld: zeggen dat mensen die met hun handen eten geen manieren "
                  "hebben, terwijl dat in hun cultuur de gewone en nette manier is.", 3),
                 ("open", "Waar loopt het cultuurrelativisme tegen een grens aan?",
                  "Bij praktijken die mensenrechten schenden: begrijpen waarom iets bestaat is "
                  "iets anders dan het goedkeuren.", 3),
             ]),
    ])


# ============================================================
zet("socialisatie-enculturatie-en-acculturatie",
    titel="Socialisatie, enculturatie en acculturatie",
    reeksen=[
        dict(kop="Drie woorden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het proces waarin je de normen van je groep leert",
                           "socialisatie"),
                          ("het ingroeien in je eigen cultuur van bij de geboorte",
                           "enculturatie"),
                          ("het aanpassen aan een andere cultuur na contact", "acculturatie"),
                          ("het afleren van wat je gewend was", "desocialisatie"),
                          ("het leren van nieuwe rollen in een nieuwe omgeving",
                           "hersocialisatie"),
                          ("het gezin, de school, de media", "socialisatie-instanties")],
                  "Over welk begrip gaat dit?", WW),
                 ("open", "Waarom stopt socialisatie niet na de kindertijd?",
                  "Elke nieuwe rol vraagt opnieuw leren: een eerste job, ouder worden, verhuizen "
                  "naar een ander land. Dat is secundaire socialisatie.", 3),
             ]),
        dict(kop="Wie socialiseert?",
             opdracht="Zet elke invloed bij de juiste instantie.",
             oefeningen=[
                 ("rij", [("je leert aan tafel wachten tot iedereen bediend is", "het gezin"),
                          ("je leert op tijd komen en je beurt afwachten", "de school"),
                          ("je leert wat in jouw groep cool is", "de leeftijdgenoten"),
                          ("je leert hoe een relatie er zou moeten uitzien", "de media"),
                          ("je leert welke feestdagen je viert",
                           "de levensbeschouwelijke groep"),
                          ("je leert hoe je je op een werkvloer gedraagt", "het werk")],
                  "Welke socialisatie-instantie?", WW),
                 ("open", "Waarom wordt de rol van leeftijdgenoten groter in de puberteit?",
                  "Een jongere bouwt een eigen identiteit op los van het gezin, en zoekt "
                  "daarvoor bevestiging bij wie in dezelfde fase zit.", 3),
             ]),
        dict(kop="Acculturatie in vier strategieën",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["strategie", "eigen cultuur behouden?", "nieuwe cultuur overnemen?"],
                  [["integratie", None, None], ["assimilatie", None, None],
                   ["separatie", None, None], ["marginalisatie", None, None]],
                  "integratie: ja en ja · assimilatie: nee en ja · separatie: ja en nee · "
                  "marginalisatie: nee en nee", "150px"),
                 ("rij", [("Hij spreekt thuis Turks en op school Nederlands, en voelt zich "
                           "in beide thuis.", "integratie"),
                          ("Zij laat alles van vroeger los en wil enkel nog Belgisch zijn.",
                           "assimilatie"),
                          ("Hij blijft volledig binnen de eigen gemeenschap.", "separatie"),
                          ("Zij voelt zich nergens meer bij horen.", "marginalisatie"),
                          ("Hij viert zowel Kerstmis als het Suikerfeest.", "integratie"),
                          ("Zij spreekt haar moedertaal niet meer met haar kinderen.",
                           "assimilatie")],
                  "Welke strategie is dit?", WW),
                 ("open", "Welke strategie hangt volgens onderzoek het sterkst samen met "
                          "welbevinden, en waarom?",
                  "Integratie: je verliest je wortels niet en je hebt tegelijk toegang tot de "
                  "nieuwe samenleving, dus je hebt steun van twee kanten.", 3),
                 ("open", "Wat is een cultuurschok?",
                  "De verwarring en het ongemak als de vanzelfsprekende regels van je eigen "
                  "cultuur plots niet meer gelden en je niet weet hoe je je moet gedragen.", 3),
             ]),
    ])


# ============================================================
zet("sociale-instituties",
    titel="Sociale instituties",
    reeksen=[
        dict(kop="De vijf grote instituties",
             opdracht="Vul de tabel aan met één functie per institutie.",
             oefeningen=[
                 ("tabel", ["institutie", "een functie"],
                  [["het gezin", None], ["het onderwijs", None], ["de economie", None],
                   ["de politiek", None], ["de levensbeschouwing", None]],
                  "gezin: kinderen grootbrengen en primaire socialisatie · "
                  "onderwijs: kennis doorgeven en mensen plaatsen op de arbeidsmarkt · "
                  "economie: goederen en diensten voortbrengen en verdelen · "
                  "politiek: beslissingen nemen die voor iedereen gelden en orde handhaven · "
                  "levensbeschouwing: zin geven en een gemeenschap vormen", "260px"),
                 ("open", "Wat is een sociale institutie precies?",
                  "Een vast, breed gedragen patroon van regels en rollen waarmee een "
                  "samenleving een basisbehoefte invult. Het is geen gebouw en geen "
                  "organisatie, maar de manier waarop iets geregeld is.", 4),
             ]),
        dict(kop="Manifest en latent",
             opdracht="Schrijf bij elke functie of ze manifest of latent is.",
             oefeningen=[
                 ("rij", [("de school leert je lezen en rekenen", "manifest"),
                          ("de school houdt kinderen overdag van de straat", "latent"),
                          ("de school is de plaats waar veel mensen hun partner leren kennen",
                           "latent"),
                          ("het gezin voedt kinderen op", "manifest"),
                          ("het gezin geeft ongelijkheid door van de ene generatie op de "
                           "volgende", "latent"),
                          ("een examen meet wat je kent", "manifest")],
                  "Manifest of latent?", WW),
                 ("open", "Leg het verschil uit tussen een manifeste en een latente functie.",
                  "Een manifeste functie is bedoeld en zichtbaar; een latente functie is een "
                  "onbedoeld maar wel echt gevolg.", 3),
                 ("kort", "Wie bedacht dit onderscheid?", "Robert Merton", WW),
             ]),
        dict(kop="Het gezin verandert",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("een koppel met kinderen", "kerngezin"),
                          ("ouders, kinderen, grootouders onder één dak", "uitgebreid gezin"),
                          ("één ouder met kinderen", "eenoudergezin"),
                          ("twee gezinnen die samensmelten", "nieuw samengesteld gezin"),
                          ("een koppel zonder kinderen", "gezin zonder kinderen"),
                          ("mensen zonder bloedband die samen een huishouden vormen",
                           "samenwoners")],
                  "Welke gezinsvorm is dit?", WW),
                 ("open", "Noem drie veranderingen in het Belgische gezin van de laatste "
                          "vijftig jaar.",
                  "Minder kinderen en later een eerste kind, meer echtscheidingen en dus meer "
                  "eenoudergezinnen en nieuw samengestelde gezinnen, en veel vaker twee "
                  "werkende ouders.", 4),
                 ("open", "Welke taken van het gezin zijn deels naar andere instituties "
                          "verschoven?",
                  "Opvang en onderwijs naar de crèche en de school, zorg voor zieken en ouderen "
                  "naar de gezondheidszorg, en de productie van voedsel en kleren naar de "
                  "economie.", 4),
             ]),
    ])


# ============================================================
zet("sociale-groepen-en-de-typologie-van-merton",
    titel="Sociale groepen en de typologie van Merton",
    reeksen=[
        dict(kop="Soorten groepen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een kleine groep met persoonlijke, warme banden",
                           "primaire groep"),
                          ("een grotere groep met zakelijke banden rond een doel",
                           "secundaire groep"),
                          ("de groep waar je zelf bij hoort", "de wij-groep"),
                          ("de groep waar je niet bij hoort", "de zij-groep"),
                          ("de groep waaraan je je spiegelt", "de referentiegroep"),
                          ("mensen die toevallig samen staan te wachten", "geen groep, "
                           "een categorie of een menigte")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Kan een referentiegroep een groep zijn waar je niet bij hoort? Leg "
                          "uit.",
                  "Ja. Je kan je spiegelen aan een groep waar je graag bij wil horen, "
                  "bijvoorbeeld de leerlingen van een richting die je volgend jaar wil doen.", 3),
                 ("waar", "Een gezin is een secundaire groep.", False),
             ]),
        dict(kop="De typologie van Merton",
             opdracht="Vul de tabel aan: aanvaardt de persoon de doelen en de middelen?",
             oefeningen=[
                 ("tabel", ["type", "doelen", "middelen"],
                  [["conformisme", None, None], ["innovatie", None, None],
                   ["ritualisme", None, None], ["terugtrekking", None, None],
                   ["opstand", None, None]],
                  "conformisme: ja en ja · innovatie: ja en nee · ritualisme: nee en ja · "
                  "terugtrekking: nee en nee · opstand: vervangt allebei", "110px"),
                 ("rij", [("Zij studeert hard om een goede job te krijgen.", "conformisme"),
                          ("Hij wil rijk worden en steelt daarvoor.", "innovatie"),
                          ("Hij komt elke dag werken maar gelooft nergens meer in.",
                           "ritualisme"),
                          ("Zij haakt helemaal af en leeft op straat.", "terugtrekking"),
                          ("Zij wil een heel ander systeem en voert actie.", "opstand"),
                          ("Hij spiekt om te slagen.", "innovatie")],
                  "Welk type is dit?", WW),
                 ("open", "Wat wil Merton met deze indeling verklaren?",
                  "Waarom mensen afwijkend gedrag stellen: niet omdat ze slecht zijn, maar "
                  "omdat de samenleving iedereen dezelfde doelen oplegt zonder iedereen "
                  "dezelfde middelen te geven om ze te bereiken.", 4),
             ]),
        dict(kop="Wat een groep met je doet",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het aanpassen van je mening aan die van de groep?",
                  "conformeren / conformisme", WW),
                 ("kort", "Hoe heet het verschijnsel waarbij een hechte groep kritiek smoort?",
                  "groepsdenken", WW),
                 ("open", "Wat toonde het lijnenexperiment van Asch?",
                  "Dat mensen een zichtbaar fout antwoord gaan geven als de hele groep voor hen "
                  "dat ook doet; ongeveer een derde van de antwoorden volgde de groep.", 3),
                 ("open", "Noem twee manieren om groepsdenken te voorkomen.",
                  "Iemand uitdrukkelijk de rol van tegenspreker geven, en eerst ieder apart "
                  "laten opschrijven wat hij denkt voor je er samen over praat.", 3),
             ]),
    ])


# ============================================================
zet("sociale-positie-sociale-rol-en-rollenconflicten",
    titel="Sociale positie, sociale rol en rollenconflicten",
    reeksen=[
        dict(kop="Positie, rol en verwachting",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de plaats die je inneemt in een geheel", "de sociale positie"),
                          ("het gedrag dat bij die plaats verwacht wordt", "de sociale rol"),
                          ("een positie die je krijgt zonder er iets voor te doen",
                           "een toegeschreven positie"),
                          ("een positie die je verwerft", "een verworven positie"),
                          ("alle rollen die je tegelijk hebt", "de rollenset"),
                          ("de regels die bij een rol horen", "de rolverwachtingen")],
                  "Hoe noemen we dit?", WW),
                 ("rij", [("dochter", "toegeschreven"), ("verpleegkundige", "verworven"),
                          ("oudste van het gezin", "toegeschreven"),
                          ("kapitein van de ploeg", "verworven"),
                          ("Belg door geboorte", "toegeschreven"),
                          ("vrijwilliger bij de jeugdbeweging", "verworven")],
                  "Toegeschreven of verworven?", WW),
             ]),
        dict(kop="Rollenconflicten",
             opdracht="Schrijf op welk soort conflict het is en leg het in één zin uit.",
             oefeningen=[
                 ("open", "Sara moet vanavond studeren voor haar examen, maar haar werkgever "
                          "vraagt haar in te springen in de winkel.",
                  "Een conflict tussen rollen: haar rol als leerling botst met haar rol als "
                  "werkneemster.", 3),
                 ("open", "Een leerkracht moet tegelijk streng beoordelen en een "
                          "vertrouwenspersoon zijn voor dezelfde leerling.",
                  "Een conflict binnen één rol: twee verwachtingen bij dezelfde rol botsen.", 3),
                 ("open", "Een jonge ploegleider moet oudere collega's aansturen die hem nog "
                          "als leerjongen zien.",
                  "Een conflict binnen één rol, door tegenstrijdige verwachtingen van de "
                  "rolpartners: hij moet leiden terwijl zij hem niet als leider zien.", 3),
                 ("open", "Noem drie manieren om met een rollenconflict om te gaan.",
                  "Prioriteiten stellen en kiezen welke rol voorgaat, de rollen in tijd en "
                  "plaats scheiden, of met de rolpartners praten om de verwachtingen bij te "
                  "stellen.", 4),
             ]),
        dict(kop="Rolafstand en rolidentificatie",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het samenvallen met je rol?", "rolidentificatie", WW),
                 ("kort", "Hoe heet het bewust afstand houden van je rol?", "rolafstand", WW),
                 ("open", "Geef van allebei een voorbeeld uit een ziekenhuis.",
                  "Rolidentificatie: een verpleegkundige die ook thuis over niets anders praat "
                  "dan haar afdeling. Rolafstand: een verpleegkundige die een grapje maakt om "
                  "te laten zien dat ze meer is dan haar uniform.", 4),
                 ("open", "Waarom is te sterke rolidentificatie een risico in een zorgberoep?",
                  "Je neemt het werk helemaal mee naar huis en vindt geen afstand meer; dat "
                  "verhoogt de kans op uitputting.", 3),
             ]),
    ])


# ============================================================
zet("sociale-status-en-kansen-in-de-samenleving",
    titel="Sociale status en kansen in de samenleving",
    reeksen=[
        dict(kop="Status en stratificatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de waardering die aan een positie hangt", "sociale status"),
                          ("de gelaagde opbouw van een samenleving", "sociale stratificatie"),
                          ("de beweging van de ene laag naar de andere", "sociale mobiliteit"),
                          ("omhoog of omlaag in de lagen", "verticale mobiliteit"),
                          ("een andere job op hetzelfde niveau", "horizontale mobiliteit"),
                          ("een samenleving waarin je laag vastligt bij je geboorte",
                           "een gesloten stratificatie")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Welke drie bronnen van ongelijkheid onderscheidde Max Weber?",
                  "Bezit of economische klasse, status of aanzien, en macht.", 3),
                 ("open", "Geef een beroep met een hoog aanzien maar een bescheiden loon, en "
                          "leg uit wat dat toont.",
                  "Bijvoorbeeld een leerkracht of een verpleegkundige. Het toont dat status en "
                  "inkomen niet samenvallen: aanzien en bezit zijn twee verschillende bronnen "
                  "van positie.", 3),
             ]),
        dict(kop="Kapitaal volgens Bourdieu",
             opdracht="Zet elk voorbeeld bij de juiste soort kapitaal.",
             oefeningen=[
                 ("rij", [("een spaarrekening en een huis", "economisch kapitaal"),
                          ("een diploma en belezenheid", "cultureel kapitaal"),
                          ("een oom die je aan een stage helpt", "sociaal kapitaal"),
                          ("weten hoe je je in een sollicitatie gedraagt",
                           "cultureel kapitaal"),
                          ("lid zijn van een vereniging met veel contacten",
                           "sociaal kapitaal"),
                          ("een erfenis", "economisch kapitaal")],
                  "Welk kapitaal is dit?", WW),
                 ("open", "Leg uit hoe cultureel kapitaal een kind op school kan bevoordelen.",
                  "Een kind dat thuis de taal, de boeken en de omgangsvormen van de school al "
                  "meekrijgt, herkent op school wat er van hem verwacht wordt. Het hoeft dus "
                  "minder bij te leren dan een kind dat die wereld niet kent.", 4),
                 ("kort", "Hoe heet het verschijnsel dat onderwijs ongelijkheid eerder "
                          "bevestigt dan wegwerkt?", "sociale reproductie", WW),
             ]),
        dict(kop="Kansen en cijfers",
             opdracht="Lees de tabel en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<table class='invul'><tr><th>diploma van de ouders</th>"
                  "<th>kinderen met een diploma hoger onderwijs</th></tr>"
                  "<tr><td>geen diploma secundair</td><td>18 %</td></tr>"
                  "<tr><td>diploma secundair</td><td>42 %</td></tr>"
                  "<tr><td>diploma hoger onderwijs</td><td>71 %</td></tr></table>"
                  "<p style='font-size:.9em'>Verzonnen cijfers, enkel om mee te oefenen.</p>"),
                 ("kort", "Hoeveel procentpunten verschil zit er tussen de hoogste en de "
                          "laagste rij?", "53 procentpunten", W),
                 ("open", "Welk verband lees je in deze tabel?",
                  "Hoe hoger het diploma van de ouders, hoe groter de kans dat het kind een "
                  "diploma hoger onderwijs haalt.", 2),
                 ("open", "Waarom mag je uit deze tabel niet besluiten dat het diploma van de "
                          "ouders de oorzaak is?",
                  "Een verband is nog geen oorzaak. Er kunnen andere factoren meespelen die met "
                  "allebei samenhangen, zoals inkomen, de buurt, de school of de taal die thuis "
                  "gesproken wordt.", 4),
                 ("open", "Noem twee maatregelen waarmee een overheid deze ongelijkheid wil "
                          "verkleinen.",
                  "Studietoelagen en lagere inschrijvingsgelden, en extra werkingsmiddelen voor "
                  "scholen met veel leerlingen uit kansarme gezinnen.", 3),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}


UITLEGBLADEN["oefenbundel-ontwikkeling-groeien-rijpen-en-leren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie woorden, drie vragen. Gaat het over groter of zwaarder worden, dan is het groei. "
                    "Gaat het over iets wat vanzelf mogelijk wordt zodra het lichaam er klaar voor is, dan "
                    "is het rijping. Moest er geoefend worden, dan is het leren.",
             waarom=[
                 "Let op de stem van de puber: dat is rijping en niet leren, want er is niets geoefend. En "
                 "rechtop zitten is ook rijping, al lijkt het op iets wat een baby leert.",
                 "Een handige formulering: groei is meer van hetzelfde, rijping is iets nieuws dat mogelijk "
                 "wordt. Groei kan je meten met een meetlat, rijping niet.",
                 "Dat is het begrip rijpheid of schoolrijpheid: oefenen werkt alleen als het lichaam en "
                 "het zenuwstelsel er klaar voor zijn. Daarom heeft het weinig zin een kind te laten "
                 "oefenen op iets waar het nog niet aan toe is.",
             ]),
        dict(aanpak="Aanleg is wat van binnenuit komt, omgeving is wat van buitenaf komt. Bij bijna elke "
                    "eigenschap werken de twee samen, dus noem ze bij een verklaring ook beide.",
             waarom=[
                 "Je spreekt ook van nature, of van het genotype: wat in je genen zit. Wat je er uiteindelijk "
                 "van ziet, het fenotype, is altijd het resultaat van aanleg én omgeving.",
                 "Hier zegt men ook nurture. Opvoeding is daar een deel van, maar niet alles: school, "
                 "vrienden, taal, buurt en toeval horen er ook bij.",
                 "Het belangrijkste inzicht hier: hetzelfde gezin is voor twee kinderen niet dezelfde "
                 "omgeving. Een oudste en een jongste groeien op bij andere ouders, want die ouders zijn "
                 "zelf veranderd, en elk kind roept ander gedrag bij hen op.",
                 "De vraag is niet aanleg óf omgeving maar hoe de twee samenwerken. Dat heet interactie: "
                 "aanleg bepaalt mee welke omgeving je opzoekt, en de omgeving bepaalt mee wat je aanleg "
                 "kan worden.",
             ]),
        dict(aanpak="Ontwikkeling heeft vaste kenmerken: ze loopt in een vaste orde, ze gaat levenslang "
                    "door, ze verloopt niet op elk gebied even snel, en ze is niet omkeerbaar.",
             waarom=[
                 "Bij zo'n tabel is het je eigen voorbeeld dat telt, niet een vaste oplossing. Wat wel "
                 "moet: je voorbeeld moet duidelijk bij dat ene kenmerk horen.",
                 "Taal is het bekendste voorbeeld: wie als kind twee talen hoort, leert ze zonder moeite. "
                 "Een gevoelige periode is wel geen harde deur, en daarin verschilt ze van wat men vroeger "
                 "een kritieke periode noemde.",
             ]),
        dict(aanpak="Bij een casus zoek je de begrippen van de theorie terug in de tekst. Onderstreep eerst "
                    "elke verandering die er staat, en zet er pas daarna het juiste woord bij.",
             waarom=[
                 "Let op de derde: dat zijn zus verdrietig is ziet hij nu wel en vroeger niet. Dat is geen "
                 "les die hij kreeg, dus is het geen leren in de enge zin maar sociale ontwikkeling.",
                 "Het sleutelwoord hier is ongelijk tempo: zijn lichaam, zijn denken en zijn sociale "
                 "gevoel ontwikkelen elk op hun eigen snelheid. Daarom kan een kind er oud uitzien en zich "
                 "nog heel jong gedragen, of omgekeerd.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-fysieke-ontwikkeling-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Twee richtingen en twee soorten motoriek. Cefalocaudaal is van het hoofd naar de "
                    "voeten, proximodistaal van het midden naar de buitenkant. Grove motoriek zijn de "
                    "grote bewegingen, fijne motoriek de kleine.",
             waarom=[
                 "De woorden verraden zichzelf: cefaal is hoofd en caudaal is staart, proximaal is dichtbij "
                 "en distaal is ver weg. Wie dat weet, hoeft ze niet uit het hoofd te leren.",
                 "Dat is de cefalocaudale richting in actie. Dezelfde regel verklaart ook waarom een baby "
                 "eerst met zijn hele arm zwaait en pas later met zijn vingers iets kan oppakken: dat is "
                 "de proximodistale richting.",
             ]),
        dict(aanpak="Primaire geslachtskenmerken horen bij de voortplantingsorganen zelf, secundaire zijn "
                    "al de rest wat in de puberteit verandert. Vraag je dus af: dient dit rechtstreeks "
                    "voor de voortplanting?",
             waarom=[
                 "Baardgroei, borstontwikkeling, bredere heupen en een zwaardere stem dienen niet "
                 "rechtstreeks voor de voortplanting, en zijn dus secundair. Baarmoeder en teelballen wel, "
                 "en die zijn er al bij de geboorte.",
                 "Menarche komt van maand, net als menstruatie. Bij jongens heet de eerste zaadlozing de "
                 "spermarche.",
                 "Volledig gezegd begint het in de hypothalamus, die met GnRH de hypofyse aanzet; de "
                 "hypofyse geeft dan FSH en LH af aan de geslachtsklieren. De hypofyse is dus de schakel "
                 "die het startsignaal doorgeeft.",
                 "Daardoor zie je in het eerste middelbaar vaak meisjes die een kop groter zijn dan de "
                 "jongens. Twee jaar later is dat beeld omgedraaid, zonder dat er bij iemand iets is "
                 "misgelopen.",
             ]),
        dict(aanpak="Twee begrippen verklaren bijna alles over het puberbrein: de prefrontale cortex is de "
                    "rem en rijpt als laatste, en het beloningssysteem is de aandrijving en is vroeg al "
                    "volop actief.",
             waarom=[
                 "De prefrontale cortex zit vooraan, achter je voorhoofd, en verzorgt plannen, overzien, "
                 "gevolgen inschatten en remmen.",
                 "Rond vijfentwintig jaar, en bij de ene wat vroeger dan bij de andere. Dat verklaart ook "
                 "waarom autoverzekeringen voor jonge bestuurders duurder zijn.",
                 "Het beeld dat vaak gebruikt wordt: een auto met een sterke motor en remmen die nog "
                 "ingereden moeten worden. Het gaat dus niet om onwil of om minder verstand, maar om een "
                 "verschil in tempo tussen twee hersendelen.",
                 "Pruning klinkt als verlies maar is winst: door de ongebruikte verbindingen weg te halen "
                 "wordt het netwerk efficiënter. Wat je veel doet, wordt sterker; wat je niet doet, "
                 "verdwijnt.",
             ]),
        dict(aanpak="Bij een casus over tempo is het antwoord bijna altijd hetzelfde: het normale bereik is "
                    "breed, en erfelijkheid bepaalt mee waar iemand in dat bereik zit.",
             waarom=[
                 "Belangrijk om erbij te zeggen: haar eindlengte en haar ontwikkeling hangen niet af van "
                 "wanneer het begint. Zo'n uitleg haalt bij een dertienjarige echt zorgen weg.",
                 "Wanneer de puberteit begint, is een van de sterker erfelijke kenmerken. Vragen hoe het "
                 "bij de ouders liep, is dus geen praatje maar echte informatie.",
                 "Vaak is het net omgekeerd: wie vroeg begint, stopt ook vroeger met groeien, en wie laat "
                 "begint, groeit langer door. Vroeg groot zijn is dus geen voorspelling van uiteindelijk "
                 "groot zijn.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-cognitieve-ontwikkeling-volgens-piaget-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vier stadia, elk met één kernbegrip: sensomotorisch met objectpermanentie, "
                    "preoperationeel met symbolen en egocentrisme, concreet-operationeel met conservatie, "
                    "formeel-operationeel met denken over het mogelijke.",
             waarom=[
                 "De leeftijden zijn richtcijfers, geen regels. Wat vastligt volgens Piaget is de orde van "
                 "de stadia, niet het tempo.",
                 "Let op de twee die in hetzelfde stadium horen: alsof een stok een zwaard is (symbolisch "
                 "spel) en denken dat iedereen ziet wat jij ziet (egocentrisme) zijn beide "
                 "preoperationeel. Egocentrisme betekent hier niet egoïstisch maar nog niet in staat om "
                 "het standpunt van een ander in te nemen.",
             ]),
        dict(aanpak="Assimilatie en accommodatie zijn de twee manieren waarop je met nieuwe informatie "
                    "omgaat: ofwel pas je de informatie in je schema, ofwel pas je je schema aan de "
                    "informatie aan.",
             waarom=[
                 "Een geheugensteun: bij assimilatie buig je de wereld naar je schema, bij accommodatie "
                 "buig je je schema naar de wereld.",
                 "Accommodatie is het zwaardere werk van de twee, en daarom gebeurt het pas als "
                 "assimilatie niet meer lukt. Dat ongemak noemt Piaget een verstoring van het evenwicht.",
                 "Let erop dat je in je antwoord beide richtingen laat zien met hetzelfde voorbeeld. Dat "
                 "is wat zo'n vraag toetst, en niet of je de definities kan opzeggen.",
                 "Objectpermanentie is de reden dat kiekeboe spelen zo leuk is: voor een heel jonge baby "
                 "is iets wat je niet ziet echt weg, en daarom is het terugkomen een verrassing.",
                 "Conservatie geldt voor hoeveelheid, aantal, gewicht en volume, en een kind krijgt die "
                 "niet alle vier tegelijk onder de knie.",
             ]),
        dict(aanpak="Bij zo'n proefje hoort altijd dezelfde uitleg: het jonge kind kijkt naar één kenmerk "
                    "tegelijk en kan de handeling niet in gedachten terugdraaien.",
             waarom=[
                 "Deze proef is het bekendste experiment van Piaget. Er bestaan ook versies met klei of "
                 "met knopen in een rij, en die testen hetzelfde idee.",
                 "Dat gedachtelijk terugdraaien heet reversibiliteit. Het kind zou kunnen bedenken dat je "
                 "het water ook weer kan terugschenken, en dan is de hoeveelheid duidelijk gelijk.",
                 "Zeg bij zo'n antwoord altijd het stadium én wat je in het gedrag ziet. Enkel een "
                 "leeftijdsgrens citeren is geen uitleg.",
                 "Een derde punt van kritiek: Piaget bekeek vooral het kind alleen tegenover de wereld. "
                 "Vygotsky legde de nadruk op wat een kind kan met hulp van iemand anders, en die zone "
                 "van naaste ontwikkeling kwam bij Piaget niet aan bod.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-morele-ontwikkeling-volgens-kohlberg-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie niveaus met elk twee stadia. Preconventioneel kijkt naar de gevolgen voor "
                    "jezelf, conventioneel naar wat anderen en de wet verwachten, postconventioneel naar "
                    "principes die boven de wet staan. Zoek in elke redenering wie of wat de maatstaf is.",
             waarom=[
                 "Het woord conventioneel is de sleutel: een conventie is een afspraak. Onder dat niveau "
                 "ben je nog bij jezelf, erboven kijk je naar principes achter de afspraken.",
                 "Let op het verschil tussen stadium 3 en 4: in stadium 3 is de maatstaf wat de mensen om "
                 "je heen van je denken, in stadium 4 de wet en de orde in de samenleving als geheel.",
                 "Daarom bestaat zijn onderzoek uit dilemma's: elk antwoord kan op elk niveau verdedigd "
                 "worden, en net het waarom verraadt het stadium.",
             ]),
        dict(aanpak="Zoek bij elke reactie de maatstaf: eigen gevolgen, eigenbelang, wat anderen vinden, de "
                    "wet, de bedoeling achter de wet, of een principe boven de wet.",
             waarom=[
                 "Let op stadium 2: dat hij haar nog nodig heeft is eigenbelang en geen liefde. Daarin "
                 "verschilt het van stadium 3, waar het gaat om wat een goede echtgenoot hoort te doen.",
                 "Dit is de kern van de hele theorie. Daarom is dit het soort vraag dat op een examen "
                 "terugkomt, en daarom moet je in een antwoord altijd de redenering citeren.",
             ]),
        dict(aanpak="Bij kritiek op een theorie zeg je niet dat ze fout is maar wat ze mist. Noem telkens "
                    "wie de kritiek gaf en waarop ze ingaat.",
             waarom=[
                 "Gilligan noemt dat de zorgethiek: niet wie heeft recht, maar wie heeft mij nodig. Haar "
                 "punt is niet dat vrouwen lager scoren, maar dat de meetlat één manier van denken "
                 "bevoordeelt.",
                 "Dat laatste is een belangrijk voorbehoud: Kohlberg meet wat mensen zeggen over een "
                 "verzonnen geval, niet wat ze doen als het hen zelf raakt. Die twee lopen vaak uiteen.",
                 "Zo'n vraag toetst of je het stadium kan toepassen op jouw wereld. Let erop dat je "
                 "voorbeeld echt bij stadium 4 past: de maatstaf moet de regel zelf zijn, niet de straf en "
                 "niet wat je vrienden zouden denken.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-sociale-ontwikkeling-en-de-gehechtheid-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Let bij een gehechtheidsstijl op twee momenten: hoe het kind reageert bij het weggaan "
                    "én hoe het reageert bij de terugkomst. Dat tweede moment is het belangrijkste.",
             waarom=[
                 "Vergelijk de vier: veilig protesteert en laat zich troosten, vermijdend protesteert niet, "
                 "ambivalent komt niet tot rust, en gedesorganiseerd vertoont tegenstrijdig gedrag. Niet "
                 "huilen is dus geen teken van een veilige band.",
                 "In het Engels heet ze de strange situation. Een vreemde komt binnen, de ouder gaat weg en "
                 "komt terug, en de onderzoeker kijkt vooral naar dat laatste.",
                 "Ainsworth was een medewerkster van Bowlby; zij bracht het meten erbij. De vierde stijl, "
                 "gedesorganiseerd, is nog later toegevoegd door Main en Solomon.",
                 "Bowlby zag gehechtheid als een biologisch systeem: een jong dier dat bij gevaar dichtbij "
                 "een verzorger blijft, overleeft beter. Daarom is gehechtheid geen verwennerij maar een "
                 "overlevingsmechanisme.",
             ]),
        dict(aanpak="Noem bij een casus altijd de stijl én waaraan je het ziet. Zonder dat tweede stuk is "
                    "je antwoord een gok, ook als de stijl juist is.",
             waarom=[
                 "De drie delen van veilige gehechtheid zitten alle drie in deze casus: protest, troost "
                 "aannemen, en daarna weer durven verkennen.",
                 "Dit is belangrijk om te weten: metingen van hartslag en stresshormonen laten zien dat "
                 "zulke kinderen wél stress hebben. Ze hebben geleerd die niet te laten zien, omdat er "
                 "vroeger weinig op kwam.",
                 "Dat heen en weer is het kenmerk: de troost is te onvoorspelbaar geweest om op te "
                 "vertrouwen, en daarom blijft het kind bezig met de ouder in plaats van te gaan spelen.",
                 "Elk kind hecht zich, ook aan een ouder die weinig reageert; de stijl verschilt, de band "
                 "niet. Alleen bij ernstige verwaarlozing kan gehechtheid echt uitblijven.",
             ]),
        dict(aanpak="De vroege band werkt door als een innerlijk model: wat kan ik verwachten van anderen, "
                    "en ben ik het waard dat men mij helpt? Dat verklaart waarom dit onderwerp verder "
                    "reikt dan de kinderjaren.",
             waarom=[
                 "Het intern werkmodel is als een bril: je ziet nieuwe mensen door wat je vroeg geleerd "
                 "hebt. Daarom speelt gehechtheid ook mee in vriendschappen en in latere relaties.",
                 "Let op dat het twee kanten heeft: een veilige basis om van weg te gaan en een veilige "
                 "haven om naar terug te keren. Zonder dat tweede gaat een kind niet weg.",
                 "Dit is het antwoord op de vraag of een kind naar de crèche mag: het gaat om de kwaliteit "
                 "van het reageren, niet om het aantal uren. Daarom kunnen ook een onthaalmoeder, een oma "
                 "of een pleegouder een gehechtheidsfiguur zijn.",
                 "Dat heet verworven veiligheid. Zeg er wel bij dat het geen kwestie van willen is en dat "
                 "het tijd kost; anders klinkt het te gemakkelijk.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-psychosociale-ontwikkeling-volgens-erikson-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Elke fase bij Erikson is een botsing tussen twee polen. Onthoud de reeks aan de "
                    "leeftijden, en let erop dat de uitkomst nooit volledig het ene of het andere is: het "
                    "gaat om het overwicht.",
             waarom=[
                 "Vul altijd beide polen in, niet enkel de goede. De tegenstelling ís de fase, en een "
                 "beetje wantrouwen of schaamte is zelfs nodig om in de wereld te overleven.",
                 "Daarom gaan zijn fasen ook door na de kindertijd, tot in de ouderdom. Bij Freud stopte "
                 "de ontwikkeling in de puberteit; Erikson was de eerste met een theorie over het hele "
                 "leven.",
             ]),
        dict(aanpak="Zoek bij een casus eerst de leeftijd, dan de fase, en zeg daarna welke kant het op "
                    "gaat. Het gaat dus om twee antwoorden: welke fase, en welke uitkomst.",
             waarom=[
                 "Let erop dat het om het patroon gaat en niet om één keer: elke dag opnieuw de handen "
                 "wegduwen leert het kind dat het zelf niets kan. Eén keer helpen omdat je haast hebt, "
                 "doet dat niet.",
                 "Dit is belangrijk voor ouders: zulk uitproberen is geen probleemgedrag maar het werk van "
                 "deze fase. Wie nooit iets uitprobeert, loopt juist het risico op rolverwarring.",
                 "Zorgzaamheid heet bij Erikson generativiteit: iets doorgeven aan een volgende generatie, "
                 "door kinderen, werk, onderwijs of vrijwilligerswerk. Het tegendeel, stagnatie, is het "
                 "gevoel dat je alleen nog rondjes draait.",
                 "Een fase die slecht uitvalt, is geen eindvonnis: ze maakt een volgende fase moeilijker, "
                 "maar nieuwe ervaringen en relaties kunnen er later nog aan werken.",
             ]),
        dict(aanpak="De identiteitsfase is de bekendste van de acht. Let bij vragen erover op het verschil "
                    "tussen zoeken, wat hoort bij de fase, en vastlopen, wat rolverwarring is.",
             waarom=[
                 "Rolverwarring is dus niet hetzelfde als twijfelen. Twijfelen en uitproberen hoort bij de "
                 "fase; blijven zweven zonder ergens bij te horen is het risico.",
                 "Men spreekt daarom van een verlengde adolescentie of van emerging adulthood. Keuzevrijheid "
                 "maakt het zoeken niet makkelijker maar langer.",
                 "Bij zo'n vraag telt je eigen eerlijke voorbeeld. Wat moet kloppen, is de band met de "
                 "fase: het moet over wie je bent of wil worden gaan, niet enkel over wat je graag doet.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-persoonlijkheid-karakter-en-temperament-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie woorden die op elkaar lijken: temperament is wat je meekrijgt, karakter is wat "
                    "je verwerft, persoonlijkheid is het geheel. Let er ook op wat géén "
                    "persoonlijkheidskenmerk is: een rol en een stemming horen bij het moment.",
             waarom=[
                 "De test voor een trek is duur en herkenbaar: toont iemand dit gedrag al jaren en in "
                 "verschillende situaties? Een slechte bui van vandaag is dat niet.",
                 "Een nuttig beeld: temperament is de grondstof, karakter is wat er door opvoeding en "
                 "ervaring van gemaakt wordt. Een druk temperament kan een enthousiaste leider worden of "
                 "iemand die nergens tot rust komt, en de omgeving telt daarin mee.",
             ]),
        dict(aanpak="De Big Five zijn vijf schalen, geen types. Iedereen heeft op elke schaal een plaats, "
                    "en de vijf samen beschrijven een persoonlijkheid. Onthoud ze met het rijtje openheid, "
                    "consciëntieusheid, extraversie, altruïsme en emotionele stabiliteit.",
             waarom=[
                 "Vul altijd beide kanten in: een lage score is geen gebrek maar de andere pool. Lage "
                 "extraversie is introversie, en dat is iets anders dan verlegenheid.",
                 "Let op de laatste pool: emotionele stabiliteit wordt ook als neuroticisme geschreven, en "
                 "dan is de schaal omgekeerd. Kijk dus altijd welke kant de vragenlijst meet.",
                 "Een hoge consciëntieusheid helpt bij studeren maar kan doorslaan in perfectionisme; een "
                 "laag altruïsme maakt lastig in een team maar handig in een onderhandeling. De vraag is "
                 "altijd: past deze trek bij deze situatie?",
             ]),
        dict(aanpak="Bij elk meetinstrument horen voordelen en nadelen. Noem dus niet enkel de methode maar "
                    "ook wat ze vertekent.",
             waarom=[
                 "Een derde manier is de beoordeling door anderen: hoe zien je ouders of je collega's je? "
                 "Die botst vaak met je zelfbeeld, en dat verschil is zelf interessant.",
                 "Daarom bevatten goede vragenlijsten controlevragen en vragen ze hetzelfde op meerdere "
                 "manieren. Bij een sollicitatie is sociale wenselijkheid natuurlijk het sterkst.",
                 "Dat is het belangrijkste voorbehoud bij dit hele hoofdstuk: een persoonlijkheidstest is "
                 "een beschrijving, geen rapport. Pas op met online tests die je in een vast type stoppen; "
                 "de Big Five werkt met schalen, net omdat mensen niet in vakjes passen.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-het-zelfconcept-zelfbeeld-en-zelfwaardering-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Houd beschrijven en beoordelen uit elkaar. Het zelfbeeld beschrijft, de zelfwaardering "
                    "beoordeelt, en het zelfconcept is alles samen, met daarin ook het ideale zelf en het "
                    "sociale zelf.",
             waarom=[
                 "Zelfeffectiviteit is smaller dan zelfwaardering: het gaat om één taak. Je kan een lage "
                 "zelfwaardering hebben en toch zeker zijn dat je kan koken.",
                 "Dat is ook waarom iemand met goede punten een lage zelfwaardering kan hebben: niet het "
                 "zelfbeeld maakt het verschil maar hoe zwaar je dat punt laat wegen.",
             ]),
        dict(aanpak="Het zelfbeeld komt van buiten naar binnen: uit wat anderen teruggeven en uit "
                    "vergelijking met anderen. Zoek bij elke vraag welke van die twee bronnen aan het werk "
                    "is.",
             waarom=[
                 "In de vakliteratuur heet dit het spiegelzelf of looking-glass self, van Cooley: je ziet "
                 "jezelf zoals je denkt dat anderen je zien, en dat hoeft niet te kloppen.",
                 "Neerwaartse vergelijking kan je zelfwaardering juist opkrikken, maar ten koste van de "
                 "ander. Opwaartse vergelijking kan ook motiveren, als het verschil niet te groot is.",
                 "Een belangrijk detail: het gaat niet enkel om de inhoud maar om de frequentie. Vroeger "
                 "vergeleek je je met je klas, nu met de hele wereld, de hele dag door.",
                 "Een stabiele, hoge zelfwaardering heeft de ander niet nodig als maatstaf. Arrogantie is "
                 "juist vaak een hoge maar wankele zelfwaardering die voortdurend bevestiging zoekt.",
             ]),
        dict(aanpak="Bij een casus over zelfbeeld zoek je naar de toeschrijving: zegt de persoon iets over "
                    "een vaste eigenschap van zichzelf, of over iets wat hij kan veranderen?",
             waarom=[
                 "Dat is het verschil tussen een vaste en een veranderlijke toeschrijving, en het is de "
                 "kern van dit hoofdstuk. Hetzelfde cijfer, een heel ander gevolg voor hoe je verder "
                 "studeert.",
                 "Let op de nuance bij feedback: ook complimenten op de persoon (je bent zo slim) werken "
                 "minder goed dan complimenten op het werk (je hebt dat goed aangepakt). Een leeg "
                 "compliment houdt trouwens geen stand, want het kind merkt het verschil met de "
                 "werkelijkheid.",
                 "Dat begrip komt van Carol Dweck. Opgelet met de kortsluiting: een groeigerichte mindset "
                 "betekent niet dat alles lukt als je er maar in gelooft, maar dat inspanning en aanpak "
                 "verschil maken.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-emoties-componenten-en-functies-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vier componenten bij elke emotie: wat je lichaam doet, wat je voelt, wat je denkt en "
                    "wat je doet. Vraag je bij elk zinnetje af op welk van die vier het gaat.",
             waarom=[
                 "Let op het verschil tussen de belevingscomponent (ik voel me bang) en de cognitieve "
                 "component (ik denk dat dit verkeerd afloopt). Het eerste is het gevoel zelf, het tweede "
                 "de gedachte eromheen.",
                 "Dat is ook waarom dit meer is dan een indeling: bij angst kan je je ademhaling "
                 "kalmeren, je gedachte nakijken of toch die stap zetten. Drie ingangen naar hetzelfde "
                 "gevoel.",
             ]),
        dict(aanpak="Emoties zijn geen storing maar hebben een functie. Noem er bij zo'n vraag altijd drie "
                    "met een voorbeeld: signaal, sociaal en motiverend.",
             waarom=[
                 "Een vierde functie die vaak vergeten wordt: emoties helpen beslissen. Wie geen enkel "
                 "gevoel bij twee opties heeft, raakt niet tot een keuze.",
                 "Men spreekt ook van primaire emoties. Ekman onderzocht gezichtsuitdrukkingen in heel "
                 "verschillende culturen en vond dat die zes overal herkend worden.",
                 "Onthoud ze als drie paren: blij en verdrietig, bang en kwaad, verbaasd en vol afkeer. "
                 "Sommige lijsten voegen er verachting aan toe.",
                 "Het verschil met de basisemoties zit in het zelfbewustzijn: schaamte en trots kunnen "
                 "niet bestaan zonder jezelf door de ogen van anderen te kunnen zien. Daarom komen ze "
                 "later in de ontwikkeling, rond de tweede verjaardag.",
             ]),
        dict(aanpak="Emotieregulatie kan op vier plaatsen aangrijpen: vóór de situatie, bij de gedachte, "
                    "bij het gevoel of bij de uiting. Zoek bij elk voorbeeld waar het ingrijpt.",
             waarom=[
                 "Het gaat niet om emoties uitzetten maar om ermee omgaan. Niet elke manier is even "
                 "gezond, en dat is net wat deze reeks laat zien.",
                 "Let op het verschil tussen vermijden en onderdrukken: bij vermijden ga je de situatie "
                 "uit de weg, bij onderdrukken blijf je erin maar laat je niets zien. Beide werken op "
                 "korte termijn en kosten op lange termijn.",
                 "Onderzoek van Gross laat dat verschil goed zien: wie onderdrukt, heeft evenveel "
                 "lichamelijke stress en wordt daarbij minder goed begrepen door anderen. Onderdrukken "
                 "kan wel nuttig zijn op een moment waarop het echt niet past, zoals op dat podium.",
                 "Dat is het hele punt van de componenten: de lichamelijke kant en de beleving lopen door, "
                 "ook als de gedragscomponent stil blijft. Daarom merken mensen soms wel dat er iets is, "
                 "ook als je niets zegt.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-motivatie-en-attributies-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je af waar de drijfveer zit. Doe je het voor de activiteit zelf, dan is het "
                    "intrinsiek; doe je het voor iets wat erna komt, zoals een beloning, een punt of het "
                    "vermijden van straf, dan is het extrinsiek.",
             waarom=[
                 "Let op het verschil tussen oefenen omdat je beter wil worden (intrinsiek: de groei zelf "
                 "is het doel) en oefenen voor een punt (extrinsiek). Dezelfde handeling, een andere "
                 "drijfveer.",
                 "Dat heet het verdringingseffect of overjustification. Het is ook waarom een beloning voor "
                 "lezen soms tegen werkt: het kind leert dat lezen iets is waarvoor je betaald moet "
                 "worden. Een beloning werkt wel beter als ze onverwacht komt of als erkenning in plaats "
                 "van als afspraak.",
             ]),
        dict(aanpak="Drie basisbehoeften uit de zelfdeterminatietheorie: autonomie (zelf kunnen kiezen), "
                    "competentie (voelen dat je het kan) en verbondenheid (ergens bij horen). Zoek bij elk "
                    "voorbeeld welke van die drie vervuld wordt.",
             waarom=[
                 "Let op de opdracht net boven je niveau: die voedt competentie, want te makkelijk geeft "
                 "geen gevoel van kunnen en te moeilijk ondermijnt het. Dat is dezelfde gedachte als de "
                 "zone van naaste ontwikkeling bij Vygotsky.",
                 "Bij zo'n vraag moet je drie maatregelen geven, één per behoefte, en ze moeten concreet "
                 "zijn. Meer motivatie geven bestaat niet: je maakt de omstandigheden waarin motivatie "
                 "groeit.",
             ]),
        dict(aanpak="Een attributie heeft twee kenmerken: ligt de oorzaak bij jezelf (intern) of buiten "
                    "jezelf (extern), en is ze blijvend (stabiel) of te veranderen (veranderlijk)? Zet "
                    "altijd beide kenmerken in je antwoord.",
             waarom=[
                 "Let op geluk: dat is extern én veranderlijk, want het kan de volgende keer anders "
                 "uitvallen. Een strenge leerkracht is extern en stabiel, want die blijft streng.",
                 "Dat is het nuttigste inzicht van dit hoofdstuk: niet het resultaat maar de verklaring "
                 "bepaalt wat je daarna doet. Intern en stabiel (ik ben nu eenmaal slecht in talen) sluit "
                 "elke volgende stap af.",
                 "Aangeleerde hulpeloosheid komt van onderzoek van Seligman. Het is de uiterste vorm van "
                 "een extern-stabiele verklaring: wat ik doe, verandert niets.",
                 "Een voorbeeld: wie niet opstaat in de bus is onbeschoft (persoon), maar als ik zelf blijf "
                 "zitten, is het omdat ik mij niet goed voel (situatie). Bij onszelf zien we de "
                 "omstandigheden wel, bij anderen niet.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-cultuur-en-cultuuruitingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Cultuur heeft een zichtbaar en een onzichtbaar deel. Houd ook waarde en norm uit "
                    "elkaar: een waarde is wat je belangrijk vindt, een norm is de concrete regel die "
                    "eruit volgt.",
             waarom=[
                 "Een subcultuur is geen tegencultuur: ze heeft een eigen stijl binnen de grotere cultuur. "
                 "Verzet een groep zich tegen de kernwaarden, dan spreekt men van een tegencultuur.",
                 "Let bij zo'n vraag op dat je echte normen geeft en geen tweede waarde. Een norm is "
                 "gedrag dat je kan zien: rechtstaan, aanspreken met u, eerst laten opscheppen.",
                 "Daarom leiden cultuurverschillen zo vaak tot misverstanden: je ziet de kleding en het "
                 "eten, maar je botst op opvattingen over tijd, gezag of familie die je niet kan zien, ook "
                 "niet bij jezelf.",
             ]),
        dict(aanpak="Hoge cultuur, volkscultuur en massacultuur zijn beschrijvingen van publiek en "
                    "verspreiding, niet van kwaliteit. Zoek dus wie het maakt en voor wie.",
             waarom=[
                 "Massacultuur is wat via media aan heel veel mensen tegelijk wordt verspreid; "
                 "volkscultuur groeit in een streek of gemeenschap en wordt doorgegeven. Carnaval en "
                 "volksdans zijn niet minder waard dan opera, ze hebben een andere oorsprong.",
                 "Men spreekt van cultureel kapitaal: wie thuis met opera en musea opgroeit, heeft "
                 "toegang tot wat als hoge cultuur geldt. Dat verband tussen cultuur en sociale positie "
                 "komt van Bourdieu.",
             ]),
        dict(aanpak="Twee houdingen tegenover een andere cultuur: etnocentrisme meet met de eigen meetlat, "
                    "cultuurrelativisme bekijkt een gewoonte binnen haar eigen context. Let erop dat "
                    "begrijpen niet hetzelfde is als goedkeuren.",
             waarom=[
                 "Het woord zegt het: ethnos is volk, centrum is midden. Je eigen groep in het midden "
                 "zetten gebeurt bijna automatisch, en daarom is het geen verwijt maar iets om bij jezelf "
                 "op te merken.",
                 "Cultuurrelativisme is een onderzoekshouding: eerst begrijpen hoe iets in die samenleving "
                 "werkt, voor je er een oordeel over hebt.",
                 "Een goed voorbeeld raakt aan iets kleins en dagelijks. Daar zit etnocentrisme namelijk "
                 "het vaakst: in wat wij normaal noemen, van eten tot op tijd komen.",
                 "Daarom spreekt men van gematigd cultuurrelativisme: je begrijpt een praktijk in haar "
                 "context, en toch blijven de mensenrechten de grens. Zonder die grens zou elke praktijk "
                 "goedgepraat kunnen worden omdat ze bij een cultuur hoort.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-socialisatie-enculturatie-en-acculturatie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Let op de voorvoegsels: en-culturatie is ingroeien in je eigen cultuur, ac-culturatie "
                    "is aanpassen na contact met een andere, de-socialisatie is afleren en "
                    "her-socialisatie is opnieuw leren.",
             waarom=[
                 "De- en hersocialisatie horen bij elkaar: wie in het leger gaat of in een nieuw land "
                 "aankomt, moet eerst oude gewoontes loslaten voor nieuwe passen.",
                 "Men onderscheidt primaire socialisatie (in het gezin, de basis) van secundaire "
                 "socialisatie (later, in school, werk en samenleving). Die tweede stopt nooit.",
             ]),
        dict(aanpak="Zoek bij elke invloed wie het je leert. Dezelfde regel kan van verschillende "
                    "instanties komen, en soms spreken ze elkaar tegen; dat heet een socialisatieconflict.",
             waarom=[
                 "Let op de media: die leren niet alleen feiten maar vooral verwachtingen, over relaties, "
                 "lichaam en succes. Daarom is media-opvoeding een deel van socialisatie geworden.",
                 "Belangrijk daarbij: dat betekent niet dat het gezin geen invloed meer heeft. Voor grote "
                 "waarden blijkt het gezin ook in de puberteit het zwaarst te wegen; de "
                 "leeftijdgenoten wegen vooral in stijl, smaak en gedrag van elke dag.",
             ]),
        dict(aanpak="De vier strategieën van Berry volgen uit twee vragen: hou je de eigen cultuur vast, "
                    "en neem je de nieuwe over? Twee keer ja is integratie, nee en ja is assimilatie, ja en "
                    "nee is separatie, twee keer nee is marginalisatie.",
             waarom=[
                 "Vul altijd de twee vragen apart in; dan rollen de vier namen er automatisch uit en hoef "
                 "je ze niet van buiten te leren.",
                 "Let op het verschil tussen integratie en assimilatie: wie beide feesten viert, "
                 "integreert; wie de eigen taal laat vallen, assimileert. In het dagelijkse taalgebruik "
                 "worden die twee woorden vaak door elkaar gebruikt, in dit vak niet.",
                 "Bij deze vraag hoort ook dat het niet alleen aan de nieuwkomer ligt: integratie kan enkel "
                 "als de ontvangende samenleving er ruimte voor laat. Bij discriminatie wordt separatie of "
                 "marginalisatie bijna onvermijdelijk.",
                 "Een cultuurschok treft ook wie niet migreert: een uitwisselingsjaar, een internaat of "
                 "een eerste job in een heel ander milieu kan hetzelfde geven. Hij verloopt in fasen, van "
                 "de eerste opwinding naar crisis en daarna gewenning.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-sociale-instituties-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Een institutie is geen gebouw maar een manier waarop iets geregeld is. Zoek bij elke "
                    "institutie welke basisbehoefte van de samenleving ze invult.",
             waarom=[
                 "Let erop dat je een functie geeft en geen beschrijving: niet wat het gezin is, maar waar "
                 "het voor dient. Elke institutie heeft er meerdere; één goede volstaat hier.",
                 "Het verschil tussen institutie en organisatie: het onderwijs is de institutie, jouw "
                 "school is een organisatie binnen die institutie. Daarom bestaat het onderwijs verder "
                 "als een school sluit.",
             ]),
        dict(aanpak="Manifest is bedoeld, latent is onbedoeld maar wel echt. Vraag je af: zou je dit in de "
                    "doelstellingen van die institutie terugvinden?",
             waarom=[
                 "Let op de school die kinderen van de straat houdt: dat is geen bijzaak maar een echte "
                 "maatschappelijke functie, ze staat alleen in geen enkele eindterm. Daarom is ze latent.",
                 "Een derde soort gevolg bestaat ook: een disfunctie, een gevolg dat schadelijk is. Dat "
                 "het onderwijs ongelijkheid doorgeeft is zowel latent als een disfunctie.",
                 "Merton is dezelfde socioloog als die van de typologie van afwijkend gedrag en van de "
                 "wij- en zij-groep. Zijn werk komt in dit vak dus meermaals terug.",
             ]),
        dict(aanpak="Zet bij de gezinsvormen telkens de samenstelling naast de naam. Bij de vraag naar "
                    "veranderingen geef je cijfers of duidelijke tendensen, geen meningen.",
             waarom=[
                 "Een nieuw samengesteld gezin heet ook een stiefgezin of een plusgezin. En samenwoners "
                 "zonder bloedband vormen wel een huishouden, maar in de statistiek niet altijd een "
                 "gezin: wat als gezin telt, is zelf een afspraak.",
                 "Een vierde verandering: huwen is niet langer de regel. Veel koppels wonen samen zonder "
                 "te trouwen, en kinderen worden vaak buiten het huwelijk geboren; dat was vijftig jaar "
                 "geleden uitzonderlijk.",
                 "Dat heet functieverlies van het gezin, maar het is geen verval: taken verschuiven, en "
                 "het gezin houdt net de taken over die moeilijk te vervangen zijn, zoals geborgenheid en "
                 "opvoeding.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-sociale-groepen-en-de-typologie-van-merton-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Bij een groep hoort besef van samenhoren en onderlinge betrokkenheid. Vraag je dus "
                    "eerst af of het echt een groep is, en kijk daarna naar de soort: primair of "
                    "secundair, wij of zij, en of ze als maatstaf dient.",
             waarom=[
                 "Mensen die samen op een bus wachten vormen een menigte, geen groep: er is geen "
                 "onderlinge band en geen besef van samenhoren. Een categorie is nog iets anders: alle "
                 "zestienjarigen van het land horen in dezelfde categorie zonder elkaar te kennen.",
                 "Daarom werkt reclame met referentiegroepen: ze laat de groep zien waar je bij zou willen "
                 "horen. Een referentiegroep kan zelfs een zij-groep zijn waar je je juist tegen afzet.",
                 "Een gezin is de primaire groep bij uitstek: klein, persoonlijk, duurzaam en niet rond één "
                 "doel gebouwd. Een voetbalclub of een klas is secundair, al kunnen daarbinnen primaire "
                 "groepjes ontstaan.",
             ]),
        dict(aanpak="De typologie van Merton volgt uit twee vragen: aanvaardt iemand de doelen van de "
                    "samenleving, en aanvaardt hij de toegelaten middelen om ze te halen? De vijf types "
                    "zijn de combinaties daarvan.",
             waarom=[
                 "Let op ritualisme: daar zijn de doelen juist opgegeven en blijven de middelen over, dus "
                 "nee en ja. Opstand valt buiten het schema, want daar worden doel én middel door iets "
                 "anders vervangen.",
                 "Spieken is innovatie, net als stelen: het doel (slagen, rijk worden) is aanvaard, het "
                 "middel niet. Innovatie heeft hier dus niets met creativiteit in de goede zin te maken.",
                 "Dat heet de spanningstheorie of straintheorie. Het is een maatschappelijke verklaring "
                 "van afwijkend gedrag, en dus iets anders dan een verklaring uit de persoon. Kritiek "
                 "erop: ze verklaart vooral misdaad uit armoede en minder goed de criminaliteit van wie "
                 "al veel heeft.",
             ]),
        dict(aanpak="Een groep oefent druk uit, ook zonder dat iemand iets vraagt. Let bij deze reeks op "
                    "het verschil tussen je mening aanpassen (conformeren) en een groep die kritiek niet "
                    "meer toelaat (groepsdenken).",
             waarom=[
                 "Conformeren is niet per definitie slecht: zonder conformisme is samenleven onmogelijk. "
                 "Het wordt een probleem als het je eigen oordeel verdringt.",
                 "Groepsdenken komt van Janis. Het treft net hechte groepen met een sterke leider en veel "
                 "tijdsdruk, en het is onderzocht bij grote politieke blunders.",
                 "Het mooiste aan dat experiment: één medestander volstond al om de druk sterk te doen "
                 "zakken. Niet de groep zelf maar de eenzaamheid maakt het zwaar om tegen te spreken.",
                 "Een derde manier: de leider zijn mening als laatste laten zeggen. Zegt hij ze eerst, dan "
                 "is het gesprek vaak al voorbij.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-sociale-positie-sociale-rol-en-rollenconflicten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Positie is de plaats, rol is het verwachte gedrag bij die plaats. Een handig beeld: "
                    "de positie is het stuk op het schaakbord, de rol is hoe het mag bewegen.",
             waarom=[
                 "Je hebt nooit één positie: leerling, dochter, vriendin, ploeglid en klant tegelijk. Dat "
                 "geheel is je rollenset, en net daar kunnen conflicten uit ontstaan.",
                 "De grens is niet altijd scherp: geslacht en leeftijd zijn toegeschreven, maar oudste van "
                 "het gezin zijn ook, want dat heb je niet gekozen. Alles waar je zelf iets voor gedaan "
                 "hebt, is verworven.",
             ]),
        dict(aanpak="Twee soorten rollenconflict: tussen twee rollen die je tegelijk hebt, of binnen één "
                    "rol waar twee verwachtingen botsen. Zeg bij elk antwoord welk soort het is én welke "
                    "verwachtingen botsen.",
             waarom=[
                 "Dit is het schoolvoorbeeld van een conflict tussen rollen: twee verschillende rollen "
                 "vragen op hetzelfde moment iets anders.",
                 "Hier is er maar één rol, die van leerkracht, met twee verwachtingen erin: beoordelen en "
                 "vertrouwen geven. Daarom heet dit een intra-rolconflict.",
                 "De rolpartners zijn hier de sleutel: zijn rol is duidelijk, maar zijn collega's "
                 "verwachten iets anders van hem dan zijn functie vraagt.",
                 "Een vierde manier bestaat ook: een rol tijdelijk neerleggen of afstoten, bijvoorbeeld "
                 "een vrijwilligerstaak opgeven in een examenperiode. Dat is geen falen maar een keuze.",
             ]),
        dict(aanpak="Rolidentificatie is samenvallen met je rol, rolafstand is laten zien dat je meer bent "
                    "dan je rol. Geen van de twee is op zich goed of slecht; het gaat om de maat.",
             waarom=[
                 "Een zekere rolidentificatie is nodig om een rol geloofwaardig te vervullen. Niemand "
                 "vertrouwt een arts die zijn rol duidelijk niet serieus neemt.",
                 "Rolafstand is een begrip van Goffman, die het sociale leven beschreef als een toneel met "
                 "rollen, een voorkant en een achterkant.",
                 "Mooi te zien hoe rolafstand ook een beroepsvaardigheid is: humor en een stapje afstand "
                 "houden zorgverleners overeind. Patiënten zelf doen hetzelfde met hun rol van zieke.",
                 "Daarom hoort afstand bij het vak en niet bij ongeïnteresseerdheid. Dat heet "
                 "professionele nabijheid: betrokken zijn zonder het werk mee naar bed te nemen.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-sociale-status-en-kansen-in-de-samenleving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Status is de waardering, stratificatie is de gelaagdheid, mobiliteit is de beweging "
                    "ertussen. Let bij mobiliteit op de richting: verticaal is omhoog of omlaag, "
                    "horizontaal is zijwaarts.",
             waarom=[
                 "Men onderscheidt ook mobiliteit tussen generaties (je doet het beter of slechter dan je "
                 "ouders) van mobiliteit binnen een loopbaan. Het eerste zegt het meest over de kansen in "
                 "een samenleving.",
                 "Weber zette zich daarmee af tegen Marx, die vooral naar bezit keek. Weber zegt: aanzien "
                 "en macht zijn aparte bronnen, en ze lopen niet altijd samen.",
                 "Daarom werkt zo'n voorbeeld: aanzien en loon vallen uiteen. Omgekeerd bestaat ook, "
                 "bijvoorbeeld een beroep met een hoog inkomen en weinig aanzien. Men spreekt dan van "
                 "statusinconsistentie.",
             ]),
        dict(aanpak="Drie soorten kapitaal bij Bourdieu: economisch (geld en bezit), cultureel (kennis, "
                    "diploma's, omgangsvormen) en sociaal (je netwerk). Zoek bij elk voorbeeld welke "
                    "hulpbron iemand gebruikt.",
             waarom=[
                 "Let op het vierde voorbeeld: weten hoe je je in een sollicitatie gedraagt is cultureel "
                 "kapitaal, al staat het op geen diploma. Juist die onzichtbare vorm maakt vaak het "
                 "verschil.",
                 "Daarom is de school niet neutraal: ze meet mee wat kinderen thuis al meekregen. Dat is "
                 "geen verwijt aan de school, het is wel de verklaring van een deel van de verschillen.",
                 "Sociale reproductie betekent dat de verschillen zich door de generaties herhalen. Dat is "
                 "ook de brug naar de latente functie van onderwijs uit de bundel over instituties.",
             ]),
        dict(aanpak="Lees bij een tabel eerst wat er precies staat: wat is de rij, wat is de kolom, en zijn "
                    "het procenten of aantallen? Antwoord daarna in de taal van de tabel.",
             waarom=[
                 "\\(71 - 18 = 53\\). Zeg procentpunten en niet procent: van \\(18\\) naar \\(71\\) is bijna "
                 "vier keer zoveel, en dat is iets anders dan \\(53\\,\\%\\) meer.",
                 "Een verband beschrijven is iets anders dan het verklaren. Houd het bij wat je ziet: hoe "
                 "hoger de rij, hoe hoger het percentage.",
                 "Dat is dezelfde regel als bij de ijsjes en de verdrinkingen in wiskunde: samenhang is "
                 "geen oorzaak. Hier is een deel van de verklaring wel aannemelijk, maar de tabel alleen "
                 "bewijst het niet.",
                 "Andere maatregelen die men gebruikt: gratis onderwijs tot achttien jaar, brede eerste "
                 "graad om de keuze uit te stellen, en studiebegeleiding. Zeg bij zo'n vraag ook dat geen "
                 "enkele maatregel de ongelijkheid helemaal wegwerkt.",
             ]),
    ]
)

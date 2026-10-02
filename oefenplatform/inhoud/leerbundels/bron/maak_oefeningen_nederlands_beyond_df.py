# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Nederlands 🌍 Beyond dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere teksten om in te delen, andere zinnen om te ontleden, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een zin
herschrijven, een oordeel verantwoorden). Wie hier iets bijschrijft, legt het
eerst naast `../../beyond-dubbele-finaliteit/nederlands.json`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond-dubbele-finaliteit". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen. Het achtervoegsel houdt ze uit elkaar van Beyond
doorstroom, van Boost en van ✨ Spark, die thema's met bijna dezelfde titel
hebben.

Geen enkel citaat in deze bundels is van een bestaande dichter of schrijver.
Elke voorbeeldzin en elk voorbeeldfragment is zelf geschreven.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Nederlands"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm.",
    "Bij een zin die je moet herschrijven: schrijf de hele zin uit, niet enkel het stuk dat verandert.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-onderwerp-hoofdgedachte-en-hoofdpunten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Onderwerp, hoofdgedachte en hoofdpunten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Onderwerp of hoofdgedachte?",
             opdracht="Noteer bij elke formulering of het een onderwerp of een hoofdgedachte is.",
             oefeningen=[
                 ("rij", [("de nieuwe sporthal", "onderwerp"),
                          ("de nieuwe sporthal staat op de verkeerde plaats", "hoofdgedachte"),
                          ("sorteren van afval", "onderwerp")], "Wat is het?", WW),
                 ("rij", [("wie minder sorteert, betaalt best meer", "hoofdgedachte"),
                          ("het openbaar vervoer in de provincie", "onderwerp"),
                          ("de bus rijdt te weinig om de auto te vervangen", "hoofdgedachte")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Hoofdpunt of detail?",
             opdracht="Een artikel verdedigt dat de schoolbibliotheek langer open moet. Noteer bij elke zin of ze een hoofdpunt of een detail is.",
             oefeningen=[
                 ("kort", "Na vier uur kan niemand nog binnen om te studeren.", "hoofdpunt", WW),
                 ("kort", "De bibliothecaris heet Ingrid en werkt er al elf jaar.", "detail", WW),
                 ("kort", "Wie thuis geen stille plek heeft, valt af.", "hoofdpunt", WW),
                 ("kort", "De zaal heeft achtentwintig stoelen.", "detail", WW),
             ]),
        dict(kop="Zelf formuleren",
             opdracht="Schrijf de hoofdgedachte in één volledige zin.",
             oefeningen=[
                 ("open", "Een tekst stelt vast dat jongeren minder lezen, noemt daarvoor drie oorzaken "
                          "en besluit dat scholen meer leestijd moeten inbouwen.",
                  "Scholen moeten tijd vrijmaken om te lezen, want jongeren lezen vandaag minder dan "
                  "vroeger. (Eén zin met een boodschap erin, niet enkel het onderwerp 'lezen bij jongeren'.)", 4),
                 ("open", "Een reportage laat drie gezinnen zien die hun energiefactuur niet meer kunnen "
                          "betalen, en vraagt zich af waarom de steun hen niet bereikt.",
                  "De bestaande steun bereikt de gezinnen die hem het meest nodig hebben niet. (Het "
                  "onderwerp is de energiefactuur; de hoofdgedachte is wat de reportage daarover zegt.)", 4),
             ]),
        dict(kop="Relevant of niet?",
             opdracht="Je opdracht is: hoeveel kost het openbaar vervoer voor een scholier per jaar? Streep door wat je voor die vraag niet nodig hebt.",
             oefeningen=[
                 ("kort", "de prijs van een jaarabonnement voor jongeren", "relevant", WW),
                 ("kort", "het aantal reizigers op lijn 12", "niet relevant", WW),
                 ("kort", "de korting voor wie in een groot gezin woont", "relevant", WW),
                 ("kort", "de kleur van de nieuwe bussen", "niet relevant", WW),
             ]),
        dict(kop="Samenvatten en notities",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een klasgenoot vat een tekst van drie bladzijden samen in twee bladzijden, "
                          "met alle voorbeelden erin. Wat is er mis en wat raad je hem aan?",
                  "Een samenvatting hoort korter te zijn dan de tekst, en de voorbeelden en details horen "
                  "er niet in. Hij moet de hoofdgedachte en de hoofdpunten in eigen woorden opschrijven, "
                  "en de uitweidingen weglaten.", 5),
                 ("open", "Waarom neem je bij een luistertekst notities terwijl je luistert, en niet "
                          "achteraf?",
                  "Omdat je niet kan terugspoelen: wat voorbij is, is weg. Je schrijft kort, in "
                  "steekwoorden en met afkortingen, en je laat witruimte om meteen na de tekst aan te "
                  "vullen.", 5),
                 ("open", "Twee artikels over hetzelfde onderwerp geven een ander cijfer. Hoe pak je dat "
                          "aan?",
                  "Je kijkt van wanneer elk cijfer is en van wie het komt. Meestal verklaart dat het "
                  "verschil al. Gebruik je ze toch samen, dan vermeld je uit welke tekst je wat haalt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-en-teksttypes-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tekstsoorten en teksttypes",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort?",
             opdracht="Noteer bij elke tekst tot welke soort ze in de eerste plaats hoort.",
             oefeningen=[
                 ("rij", [("een bijsluiter bij een zalf", "prescriptief"),
                          ("een reisverslag van drie weken Noorwegen", "narratief"),
                          ("een lezersbrief over de nieuwe parkeertarieven", "opiniërend")],
                  "Welke soort?", WW),
                 ("rij", [("een affiche van een partij met één kreet erop", "persuasief"),
                          ("een artikel dat uitlegt hoe een zonnepaneel werkt", "informatief"),
                          ("een gedicht over een verlaten fabriek", "literair")], "Welke soort?", WW),
                 ("rij", [("een betoog over een rookverbod op het schoolterrein", "argumentatief"),
                          ("een handleiding bij een fietspomp", "prescriptief"),
                          ("een stand-upnummer over verhuizen", "literair")], "Welke soort?", WW),
             ]),
        dict(kop="Twee soorten tegelijk",
             opdracht="Noteer welke twee soorten in deze teksten samenkomen.",
             oefeningen=[
                 ("kort", "een recensie van een restaurant", "informatief en opiniërend", WL),
                 ("kort", "een ballade die een schipbreuk navertelt", "literair en narratief", WL),
                 ("kort", "een blog die een dag vertelt en dan een product aanraadt", "narratief en persuasief", WL),
                 ("kort", "een handleiding met uitleg over hoe het toestel werkt", "prescriptief en informatief", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Een strip kan een literaire tekst zijn.", True),
                 ("waar", "Een tekst in dialect kan op je examen niet voorkomen.", False),
                 ("waar", "Reclame, propaganda en nepnieuws horen alle drie bij de persuasieve teksten.", True),
                 ("waar", "Een reportage op televisie hoort tot een andere soort dan een krantenartikel, want het kanaal verschilt.", False),
                 ("waar", "Een protestlied is in de eerste plaats een opiniërende tekst.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een bedrijf laat een artikel schrijven dat eruitziet als een gewoon "
                          "nieuwsbericht. Hoe heet zo'n tekst, en waarom kiest het bedrijf die vorm?",
                  "Het is een publireportage, en dus een persuasieve tekst. Het bedrijf kiest die vorm "
                  "omdat een neutraal uitziende tekst meer vertrouwen krijgt dan een advertentie.", 5),
                 ("open", "Welke vraag helpt je het best om de soort van een tekst te bepalen, en waarom "
                          "die vraag?",
                  "Wat wil de zender met deze tekst bereiken? Omdat de soort van een tekst van zijn "
                  "bedoeling afhangt en niet van zijn kanaal of zijn lengte. Wie de bedoeling kent, weet "
                  "ook hoe kritisch hij moet lezen.", 5),
                 ("open", "Een vriend zegt dat een tekst óf informatief óf opiniërend is, nooit beide. "
                          "Wat antwoord je?",
                  "Veel teksten combineren meer dan één bedoeling. Een recensie zegt zowel waarover iets "
                  "gaat als wat de schrijver vindt. Je zoekt dan wat de belangrijkste bedoeling is, maar "
                  "je hoeft niet te kiezen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk alarmbelletje?",
             opdracht="Noteer bij elk signaal waar je op moet letten.",
             oefeningen=[
                 ("rij", [("er staat geen datum bij het artikel", "misschien verouderd"),
                          ("de titel staat volledig in hoofdletters", "speelt op je gevoel"),
                          ("er staat geen auteur bij", "niemand is aanspreekbaar")],
                  "Waar wijst dat op?", WL),
                 ("rij", [("het cijfer heeft geen bron", "niet na te gaan"),
                          ("de enige bron is de verkoper zelf", "belang bij de uitkomst"),
                          ("de foto is van een ander jaar", "beeld uit de context")],
                  "Waar wijst dat op?", WL),
             ]),
        dict(kop="Framing",
             opdracht="Schrijf voor elk woord een woord dat hetzelfde feit benoemt maar het omgekeerde gevoel geeft.",
             oefeningen=[
                 ("rij", [("een protestactie", "een rel"),
                          ("een prijsaanpassing", "een prijsstijging"),
                          ("een koerswijziging", "een draaikont")], "Omgekeerd gekleurd", WW),
                 ("rij", [("een vluchteling", "een illegaal"),
                          ("een hervorming", "een besparing"),
                          ("een spaarzame regering", "een krenterige regering")],
                  "Omgekeerd gekleurd", WW),
             ]),
        dict(kop="Betrouwbaar of niet?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Een tekst met veel bronvermeldingen is daarom nog niet betrouwbaar.", True),
                 ("waar", "Een website met een strakke, professionele vormgeving is betrouwbaarder dan een lelijke.", False),
                 ("waar", "Een bron met een belang bij de uitkomst mag je gebruiken, als je dat belang vermeldt.", True),
                 ("waar", "Een filmpje waarin iemand iets zegt, bewijst dat die persoon dat gezegd heeft.", False),
                 ("waar", "Nepnieuws wil geld of invloed; satire wil je doen lachen.", True),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Schrijf in volle zinnen wat je concreet doet.",
             oefeningen=[
                 ("open", "Een bericht in je groepschat zegt dat de school morgen sluit. Wat doe je voor je "
                          "het doorstuurt?",
                  "Ik zoek de oorspronkelijke bron: staat het op de website van de school of in een mail "
                  "van de directie? Zolang ik dat niet vind, stuur ik het niet door. Een bericht zonder "
                  "afzender is geen nieuws.", 5),
                 ("open", "Je vindt één cijfer dat precies je stelling bevestigt, en drie andere teksten "
                          "zeggen iets anders. Wat doe je?",
                  "Ik ga na waar dat ene cijfer van komt en van wanneer het is. Klopt het niet met de "
                  "andere bronnen, dan pas ik mijn stelling aan in plaats van de drie andere weg te "
                  "laten. Alleen bronnen kiezen die je passen, is zelf framing.", 5),
                 ("open", "Een foto bij een artikel laat een overstroomde straat zien. Hoe controleer je of "
                          "ze bij dit bericht hoort?",
                  "Ik zoek de foto terug met een omgekeerde beeldzoekopdracht en kijk waar en wanneer ze "
                  "eerder opdook. Een echte foto van een andere plaats of een ander jaar is nog altijd "
                  "misleidend.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-communicatiemodel-en-ruis-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het communicatiemodel en ruis",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het model benoemen",
             opdracht="Vul de tabel aan voor deze situatie: de gemeente stuurt alle inwoners een brief over het nieuwe containerpark.",
             oefeningen=[
                 ("tabel", ["Onderdeel", "In deze situatie"],
                  [["zender", ""], ["boodschap", ""], ["ontvanger", ""], ["kanaal", ""],
                   ["context", ""], ["doel", ""], ["effect", ""]],
                  "zender: de gemeente — boodschap: hoe en wanneer het containerpark open is — "
                  "ontvanger: alle inwoners — kanaal: een brief op papier — context: de regeling "
                  "verandert binnenkort — doel: de inwoners informeren — effect: wat de brief bij hen "
                  "teweegbrengt, bijvoorbeeld dat ze hun gewoonte aanpassen of de brief weggooien",
                  WL),
             ]),
        dict(kop="Welke ruis?",
             opdracht="Noteer of het om externe of interne ruis gaat, en waar ze zit.",
             oefeningen=[
                 ("rij", [("een grasmachine draait buiten het klaslokaal", "externe ruis"),
                          ("je denkt aan je toets van straks", "interne ruis"),
                          ("de verbinding valt steeds weg", "externe ruis")], "Welke ruis?", WW),
                 ("rij", [("je leest de mail boos, want je had gisteren ruzie met de afzender", "interne ruis"),
                          ("je mist de helft van de podcast in een drukke trein", "externe ruis"),
                          ("je hebt een vooroordeel over de spreker", "interne ruis")],
                  "Welke ruis?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Hetzelfde bericht kan bij twee ontvangers een ander effect hebben.", True),
                 ("waar", "Wie het kanaal van een bericht kent, weet daarmee ook wie de zender is.", False),
                 ("waar", "Een gesprek aan tafel heeft ook een kanaal.", True),
                 ("waar", "Het kanaal heeft geen invloed op hoe formeel je schrijft.", False),
                 ("waar", "Het doel hoort bij de zender en het effect bij de ontvanger.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom staan het doel en het effect apart in het model?",
                  "Omdat ze niet altijd samenvallen: het doel hoort bij de zender, het effect bij de "
                  "ontvanger. Een reclamespot wil je iets doen kopen, en het effect kan ergernis zijn. "
                  "Een zender kan het effect van zijn boodschap dus niet volledig voorspellen.", 5),
                 ("open", "Waarom is een mail een lastiger kanaal dan een gesprek, als je iets gevoeligs "
                          "moet zeggen?",
                  "In een mail valt alles weg wat je toon duidelijk maakt: je stem, je gezicht, de pauzes. "
                  "En je ziet de reactie van de ander niet, dus je kan niet bijsturen. Een gesprek geeft "
                  "je die feedback meteen.", 5),
                 ("open", "Dezelfde uitnodiging gaat naar je grootmoeder en naar je klasgenoten. Wat "
                          "verandert er aan de boodschap, en wat niet?",
                  "De feiten blijven gelijk: wat, waar en wanneer. Wat verandert is de toon, de aanspreking "
                  "en het kanaal. Bij mijn grootmoeder wordt het een kaartje met u; bij mijn klas een "
                  "bericht met jij.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstopbouw-alineaverbanden-en-vaste-tekststructuren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tekstopbouw, alineaverbanden en vaste tekststructuren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk verband?",
             opdracht="Noteer het verband tussen de twee alinea's.",
             oefeningen=[
                 ("rij", [("de straat ligt blank — de riool is te klein", "oorzakelijk"),
                          ("bussen in de stad — bussen op het platteland", "tegenstellend"),
                          ("eerst inschrijven, dan betalen, dan komen", "chronologisch")],
                  "Welk verband?", WL),
                 ("rij", [("om de files te verminderen verlaagt de stad de snelheid", "doel-middel"),
                          ("drie soorten fietsen, elk apart besproken", "opsommend"),
                          ("net als in Gent kiest ook Hasselt daarvoor", "vergelijkend")],
                  "Welk verband?", WL),
                 ("rij", [("alles samen blijkt de maatregel te werken", "concluderend"),
                          ("eerst wat het oplevert, dan wat het kost", "voordelen-nadelen"),
                          ("dit geldt alleen als de prijzen blijven stijgen", "voorwaardelijk")],
                  "Welk verband?", WL),
             ]),
        dict(kop="Welke tekststructuur?",
             opdracht="Noteer welke vaste structuur deze tekst volgt.",
             oefeningen=[
                 ("kort", "de straat ligt blank, dit zijn de oorzaken en dit de oplossingen", "de probleemstructuur", WL),
                 ("kort", "een nieuwe regeling wordt voorgesteld, uitgelegd en verdedigd", "de maatregelstructuur", WL),
                 ("kort", "een restaurant beoordeeld op eten, prijs, service en inrichting", "de evaluatiestructuur", WL),
                 ("kort", "twee soorten verwarming naast elkaar, met dezelfde vier criteria", "de vergelijkingsstructuur", WL),
                 ("kort", "hoe een dorp in honderd jaar een stad werd", "de ontwikkelingsstructuur", WL),
                 ("kort", "vraag, methode, resultaten en besluit", "de onderzoeksstructuur", WL),
             ]),
        dict(kop="De alinea herschrijven",
             opdracht="Deze alinea's lopen door elkaar. Schrijf op waar je een nieuwe alinea zou beginnen en waarom.",
             oefeningen=[
                 ("open", "De bibliotheek sluit om vier uur. Wie later wil studeren, moet naar huis. Thuis "
                          "is het niet altijd stil. Daarnaast is de leeszaal te klein. Er zijn maar "
                          "achtentwintig stoelen. In de examenperiode zitten mensen op de grond.",
                  "Een nieuwe alinea bij \"Daarnaast is de leeszaal te klein.\" De eerste alinea gaat over "
                  "de openingsuren, de tweede over de plaats. Eén alinea hoort één punt te behandelen, en "
                  "\"daarnaast\" is hier het signaalwoord dat het tweede punt aankondigt.", 5),
                 ("open", "Waarom is de laatste alinea van een betoog zelden de plaats voor een nieuw "
                          "argument?",
                  "Het slot is er om de hoofdgedachte samen te vatten en de lezer iets mee te geven. Een "
                  "nieuw argument daar heeft geen ruimte meer om uitgewerkt of weerlegd te worden, dus het "
                  "zwakt je betoog eerder af dan dat het het versterkt.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Eén alinea mag meerdere zinnen beslaan, maar hoort één punt te behandelen.", True),
                 ("waar", "De inleiding van een tekst noemt altijd al de conclusie.", False),
                 ("waar", "Een tussentitel is een hulp voor de lezer, niet voor de schrijver alleen.", True),
                 ("waar", "Een tekst met een probleem-en-oplossingstructuur kan nooit ook argumenteren.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-structuuraanduiders-verwijswoorden-en-signaalwoorden-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Structuuraanduiders: verwijswoorden en signaalwoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat kondigt het signaalwoord aan?",
             opdracht="Noteer welk verband het woord aankondigt.",
             oefeningen=[
                 ("rij", [("ten eerste, ten tweede", "een opsomming"), ("toch", "een tegenstelling"),
                          ("daardoor", "een gevolg")], "Welk verband?", WL),
                 ("rij", [("want", "een reden"), ("indien", "een voorwaarde"),
                          ("kortom", "een samenvatting")], "Welk verband?", WL),
                 ("rij", [("hoewel", "een tegenstelling of een toegeving"),
                          ("enerzijds, anderzijds", "een afweging van twee kanten"),
                          ("echter", "de schrijver spreekt nu iets tegen")], "Welk verband?", WL),
             ]),
        dict(kop="Waar verwijst het naar?",
             opdracht="Noteer naar welk woord of welke woordgroep het vetgedrukte verwijswoord verwijst.",
             oefeningen=[
                 ("kort", "De gemeente plaatste nieuwe banken. Ze staan nu in de schaduw. (ze)", "de nieuwe banken", WL),
                 ("kort", "Mijn broer belde mijn oom. Hij was net thuis. (hij — dubbelzinnig)", "onduidelijk: mijn broer of mijn oom", WL),
                 ("kort", "Het dak lekt al maanden. Dat kost de school veel geld. (dat)", "dat het dak al maanden lekt", WL),
                 ("kort", "De leerlingen schreven een brief. Die ligt op het secretariaat. (die)", "de brief", WL),
             ]),
        dict(kop="Herschrijven",
             opdracht="Herschrijf de zin zodat het verwijswoord niet meer dubbelzinnig is. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "Pieter vertelde aan Wout dat hij de sleutel kwijt was.",
                  "Pieter vertelde aan Wout dat Wout de sleutel kwijt was. Of: Pieter vertelde aan Wout "
                  "dat hij, Pieter, de sleutel kwijt was. Je vervangt het verwijswoord door de naam, of "
                  "je zet de naam erachter.", 4),
                 ("open", "De school kocht nieuwe laptops voor de leerkrachten. Ze werken nu sneller.",
                  "De school kocht nieuwe laptops voor de leerkrachten. Die toestellen werken nu sneller. "
                  "(Of: De leerkrachten werken nu sneller.) Door \"ze\" te vervangen door een naamwoord "
                  "wordt duidelijk wie of wat er sneller werkt.", 4),
             ]),
        dict(kop="Het juiste signaalwoord",
             opdracht="Kies het woord dat het verband het best weergeeft.",
             oefeningen=[
                 ("kies", "De bus rijdt maar twee keer per dag. ___ neemt bijna niemand hem.",
                  ["Daarom", "Bovendien", "Hoewel"], 0),
                 ("kies", "Het plan is goedkoop. ___ gaat het de files niet oplossen.",
                  ["Toch", "Dus", "Namelijk"], 0),
                 ("kies", "Je mag meerijden, ___ je op tijd aan de halte staat.",
                  ["indien", "echter", "kortom"], 0),
                 ("kies", "Er kwamen te weinig inschrijvingen. ___ ging de reis niet door.",
                  ["Bijgevolg", "Daarentegen", "Bijvoorbeeld"], 0),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-argumentatie-feiten-en-meningen-en-drogredenen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Argumentatie, feiten en meningen, en drogredenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Feit of mening?",
             opdracht="Noteer bij elke uitspraak of het een feit of een mening is.",
             oefeningen=[
                 ("rij", [("de bus rijdt twee keer per dag", "feit"),
                          ("de bus rijdt veel te weinig", "mening"),
                          ("het containerpark is op zaterdag open", "feit")], "Wat is het?", WW),
                 ("rij", [("die regel is onrechtvaardig", "mening"),
                          ("de school telt 812 leerlingen", "feit"),
                          ("iedereen vindt dat een goed idee", "mening")], "Wat is het?", WW),
             ]),
        dict(kop="Welke drogreden?",
             opdracht="Noteer welke drogreden hier gebruikt wordt.",
             oefeningen=[
                 ("kort", "Je kan daar niets van zeggen, je hebt zelf geen auto.", "een persoonlijke aanval", WL),
                 ("kort", "Zeven op de tien jongeren doet het, dus het kan geen kwaad.", "een beroep op de massa", WL),
                 ("kort", "Laten we dit toestaan, dan staan we morgen voor de afgrond.", "het hellend vlak", WL),
                 ("kort", "Dat is zo omdat het nu eenmaal zo is.", "een cirkelredenering", WL),
                 ("kort", "Veel mensen vinden dat, dus het klopt.", "een beroep op de massa", WL),
                 ("kort", "Hij is rijk, dus over een taks mag hij niets zeggen.", "een persoonlijke aanval", WL),
             ]),
        dict(kop="Het argument beoordelen",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "\"In Nederland werkt het ook, dus bij ons zal het werken.\" Welke soort "
                          "argumentatie is dat, en waar wankelt ze?",
                  "Het is een argument op basis van vergelijking. Het wankelt bij de vraag of die twee "
                  "gevallen wel genoeg op elkaar lijken: verschillen ze sterk, dan zegt het ene weinig "
                  "over het andere.", 5),
                 ("open", "Waarom zet je in een betoog ook een tegenargument, als je het daarna weerlegt?",
                  "Omdat je lezer dat tegenargument zelf al bedacht had. Door het te noemen en te "
                  "weerleggen laat je zien dat je het kent, en neemt hij de rest van je betoog ernstiger. "
                  "Een betoog dat de tegenkant wegstopt, lijkt zwakker.", 5),
                 ("open", "Iemand gebruikt een drogreden om zijn stelling te verdedigen. Is zijn stelling "
                          "daarmee fout?",
                  "Nee. Het argument sneuvelt, de stelling niet. Een slecht argument voor iets dat toch "
                  "waar is, bestaat: je moet de stelling dan met een ander argument beoordelen.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Een drogreden kan overtuigen, ook al is hij niet geldig.", True),
                 ("waar", "Een uitspraak met een cijfer erin is daarom een feit.", False),
                 ("waar", "Een argumentatieve tekst kan ook feiten bevatten.", True),
                 ("waar", "Een standpunt zonder argumenten is nog altijd een betoog.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-lees-en-luisterstrategieen-en-notities-nemen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Lees- en luisterstrategieën en notities nemen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke strategie?",
             opdracht="Noteer welke leesstrategie bij deze opdracht hoort.",
             oefeningen=[
                 ("rij", [("je wil weten of de tekst over jouw onderwerp gaat", "skimmen"),
                          ("je zoekt het telefoonnummer onderaan", "scannen of zoekend lezen"),
                          ("je moet de tekst morgen kunnen navertellen", "intensief lezen")],
                  "Welke strategie?", WL),
                 ("rij", [("je bekijkt de titel, de tussenkoppen en het slot", "skimmen"),
                          ("je zoekt in een jaarverslag hoeveel leden er zijn", "scannen of zoekend lezen"),
                          ("je staat stil bij elk verwijswoord en elke stap", "intensief lezen")],
                  "Welke strategie?", WL),
             ]),
        dict(kop="Notities inkorten",
             opdracht="Schrijf deze zinnen als notitie op: enkel de kern, in steekwoorden.",
             oefeningen=[
                 ("kort", "De gemeenteraad heeft in december beslist dat het containerpark vanaf maart ook op zaterdagvoormiddag open is.",
                  "containerpark: vanaf maart ook za vm (beslissing dec.)", WL),
                 ("kort", "Omdat er te weinig inschrijvingen waren, gaat de uitstap naar de kust niet door.",
                  "uitstap kust afgelast — te weinig inschrijvingen", WL),
                 ("kort", "Er zijn drie oorzaken, waarvan de spreker de tweede het belangrijkste vindt.",
                  "3 oorzaken; nr. 2 = belangrijkste (volgens spreker)", WL),
             ]),
        dict(kop="Voor, tijdens, na",
             opdracht="Noteer of je dit vóór, tijdens of ná het lezen doet.",
             oefeningen=[
                 ("rij", [("de titel en de tussentitels doorlopen", "voor"),
                          ("in de kantlijn een vraagteken zetten", "tijdens"),
                          ("je samenvatting vergelijken met de tekst", "na")], "Wanneer?", WW),
                 ("rij", [("bedenken wat je al over het onderwerp weet", "voor"),
                          ("een onbekend woord uit de context raden", "tijdens"),
                          ("nagaan of je je leesdoel gehaald hebt", "na")], "Wanneer?", WW),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom laat je bij notities van een luistertekst witruimte open?",
                  "Omdat je niet kan terugspoelen en dus soms iets mist. In die witruimte vul je meteen na "
                  "de tekst aan wat je je nog herinnert, of je zet er een vraag die je nadien opzoekt.", 4),
                 ("open", "Je hebt een tekst gelezen en je begrijpt de laatste alinea niet. Noem twee "
                          "dingen die je doet, in de juiste orde.",
                  "Eerst lees ik die alinea opnieuw, trager, en ik kijk of een vorige alinea uitlegt waar "
                  "ze op terugkomt. Helpt dat niet, dan zoek ik het sleutelwoord op of vraag ik het. Wat "
                  "je niet doet, is doorlezen en hopen dat het goed komt.", 5),
                 ("open", "Hoe weet je of je een studietekst echt begrepen hebt?",
                  "Ik probeer de hoofdgedachte en de hoofdpunten in eigen woorden na te vertellen, zonder "
                  "naar de tekst te kijken. Lukt dat niet, dan heb ik de tekst gelezen maar niet "
                  "begrepen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-multimediale-elementen-en-non-verbale-communicatie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Multimediale elementen en non-verbale communicatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat doet het element?",
             opdracht="Noteer wat dit element met de boodschap doet.",
             oefeningen=[
                 ("rij", [("een foto van een huilend kind bij een artikel over armoede", "speelt op je gevoel"),
                          ("een grafiek met de cijfers van tien jaar", "maakt een verloop zichtbaar"),
                          ("een tussentitel in het vet", "helpt je de weg vinden")],
                  "Wat doet het?", WL),
                 ("rij", [("dreigende muziek onder een reportage", "stuurt je oordeel"),
                          ("een schema met pijlen bij een uitleg", "maakt de stappen duidelijk"),
                          ("een kadertje met één cijfer erin", "zet dat cijfer in de kijker")],
                  "Wat doet het?", WL),
             ]),
        dict(kop="Welk kanaal van non-verbale communicatie?",
             opdracht="Noteer het juiste woord: mimiek, lichaamshouding, oogcontact, afstand, stemgebruik, stilte of de handen.",
             oefeningen=[
                 ("rij", [("je trekt je wenkbrauwen op", "mimiek"),
                          ("je gaat een stap achteruit", "afstand"),
                          ("je laat je stem zakken", "stemgebruik")], "Welk kanaal?", WL),
                 ("rij", [("je kruist je armen", "lichaamshouding"),
                          ("je zwijgt even voor je belangrijkste punt", "stilte"),
                          ("je geeft met je handen een verband aan", "de handen")], "Welk kanaal?", WL),
                 ("rij", [("je kijkt de zaal rond in plaats van naar één punt", "oogcontact"),
                          ("je spreekt trager en laat pauzes vallen", "stemgebruik"),
                          ("je wendt je hoofd af terwijl je 'prima' zegt", "mimiek en houding")],
                  "Welk kanaal?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Een grafiek kan een juist cijfer tonen en toch misleiden.", True),
                 ("waar", "Non-verbale signalen betekenen in elke cultuur hetzelfde.", False),
                 ("waar", "Een onderschrift kan de betekenis van een foto helemaal doen kantelen.", True),
                 ("waar", "Wie zijn stem niet varieert, komt even overtuigend over.", False),
                 ("waar", "Beeld en tekst die hetzelfde zeggen, versterken elkaar.", True),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een staafdiagram begint niet bij nul maar bij 95. Wat is daar het effect van?",
                  "Kleine verschillen lijken dan enorm, want de staven schelen veel meer dan de cijfers. "
                  "Het cijfer kan correct zijn terwijl het beeld liegt. Kijk dus altijd eerst naar de "
                  "zij-as.", 5),
                 ("open", "Je geeft een presentatie en je kijkt alleen naar je scherm. Wat verlies je "
                          "daarmee?",
                  "Je verliest het oogcontact, en daarmee ook de feedback: je ziet niet of ze je volgen. "
                  "Bovendien lijkt een spreker die niet opkijkt onzeker, ook als zijn inhoud klopt.", 5),
                 ("open", "Een filmpje toont een drukke straat terwijl de stem over eenzaamheid spreekt. "
                          "Werkt dat?",
                  "Ja, maar op een andere manier: het beeld spreekt de tekst tegen en dat contrast maakt "
                  "de boodschap sterker. Je moet het wel bewust doen; een beeld dat per ongeluk iets "
                  "anders zegt, verwart je kijker.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verhaallijn-personages-en-vertelperspectief-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Verhaallijn, personages en vertelperspectief",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk perspectief?",
             opdracht="Noteer bij elk fragment welk vertelperspectief het gebruikt.",
             oefeningen=[
                 ("kort", "Ik wist niet of ze me geloofde. Haar gezicht gaf niets weg.", "ik-perspectief", WL),
                 ("kort", "Hij voelde de brief in zijn zak. Zij wist al drie dagen wat erin stond.", "alwetende verteller", WL),
                 ("kort", "Ze wist niet dat hij al vertrokken was.", "alwetende verteller", WL),
                 ("kort", "Elk hoofdstuk is van een ander personage, over dezelfde dag.", "meervoudig perspectief", WL),
                 ("kort", "Ik vertel dat ik niets gestolen heb; op bladzijde 90 blijkt van wel.", "onbetrouwbare verteller", WL),
             ]),
        dict(kop="Rond of vlak?",
             opdracht="Noteer of dit personage rond of vlak is, en in één woord waarom.",
             oefeningen=[
                 ("kort", "de buurman die in elk kapittel precies hetzelfde moppert", "vlak", WW),
                 ("kort", "de zus die eerst meedoet en halverwege weigert", "rond", WW),
                 ("kort", "de treinconducteur die één keer een kaartje vraagt", "vlak", WW),
                 ("kort", "de hoofdfiguur die aan het eind iets toegeeft", "rond", WW),
             ]),
        dict(kop="De verhaallijn",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een verhaal begint met een vrouw die in de regen voor een gesloten deur staat. "
                          "Pas in hoofdstuk drie lees je hoe het zover kwam. Hoe heet die sprong terug, "
                          "en wat levert hij op?",
                  "Dat is een flashback of terugblik: een sprong terug in de tijd binnen het verhaal. Hij "
                  "levert spanning op, want de vraag is niet meer wat er gebeurt maar waarom het zover "
                  "kwam.", 5),
                 ("open", "Wat is het verschil tussen de verhaallijn en de tijdlijn van de "
                          "gebeurtenissen?",
                  "De tijdlijn is de orde waarin de gebeurtenissen echt plaatsvonden; de verhaallijn is "
                  "de orde waarin je ze te lezen krijgt. Een verhaal hoeft niet chronologisch verteld te "
                  "worden om te kloppen: met een flashback liggen die twee anders.", 5),
                 ("open", "Waarom vertrouw je een ik-verteller niet zomaar?",
                  "Omdat je alleen ziet wat hij ziet en alleen hoort wat hij zegt. Hij kan zich vergissen, "
                  "iets verzwijgen of zich beter voordoen. Een onbetrouwbare verteller is zelfs een "
                  "techniek: de lezer merkt stilaan dat het verhaal niet klopt.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Eén verhaal kan halverwege van perspectief wisselen.", True),
                 ("waar", "De ik-verteller is altijd de schrijver zelf.", False),
                 ("waar", "Een vlak personage kan toch belangrijk zijn voor de verhaallijn.", True),
                 ("waar", "Een alwetende verteller kan niet in de gedachten van een personage kijken.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tijd-ruimte-thema-en-spanningsopbouw-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tijd, ruimte, thema en spanningsopbouw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tijdsbehandeling",
             opdracht="Noteer of de schrijver hier de tijd overslaat (een tijdsprong), de tijd vertraagt, of het verhaal in de tegenwoordige tijd zet.",
             oefeningen=[
                 ("rij", [("drie jaar later stond het huis er nog", "een tijdsprong"),
                          ("de hele bladzijde gaat over één moment", "de tijd vertragen"),
                          ("de zomer ging voorbij in twee regels", "een tijdsprong")], "Wat doet hij?", WL),
                 ("rij", [("een gedachte van het personage beslaat een bladzijde", "de tijd vertragen"),
                          ("wat er die winter gebeurde, slaat het boek over", "een tijdsprong"),
                          ("'ze duwt de deur open en kijkt rond'", "de tegenwoordige tijd")],
                  "Wat doet hij?", WL),
             ]),
        dict(kop="Ruimte en sfeer",
             opdracht="Noteer welke sfeer deze ruimte oproept, en in één woord waarmee.",
             oefeningen=[
                 ("kort", "een keuken met beslagen ruiten en soep op het vuur", "warm, beschut", WL),
                 ("kort", "een lege parking onder één werkende lamp", "dreigend, verlaten", WL),
                 ("kort", "een wachtzaal met tl-licht en vastgeschroefde stoelen", "koud, onpersoonlijk", WL),
             ]),
        dict(kop="Onderwerp of thema?",
             opdracht="Noteer of dit het onderwerp of het thema van het boek is.",
             oefeningen=[
                 ("rij", [("een verhuizing", "onderwerp"), ("afscheid nemen", "thema"),
                          ("schuld die een kind van zijn ouders overneemt", "thema")], "Wat is het?", WW),
                 ("rij", [("een oorlog", "onderwerp"), ("opgroeien in twee culturen", "thema"),
                          ("een zomer aan de kust", "onderwerp")], "Wat is het?", WW),
             ]),
        dict(kop="Spanning",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem drie middelen waarmee een schrijver spanning opbouwt, en zeg van elk wat "
                          "het doet.",
                  "Verzwijgen: wat de lezer niet weet, wil hij weten. Een aangekondigd gevaar dat nog "
                  "niet toeslaat. Een deadline, zoals een trein die om zes uur vertrekt, die de "
                  "personages onder tijdsdruk zet. Ook een voorafschaduwing of vooruitwijzing werkt zo: "
                  "een detail dat vooruitwijst naar wat komt.", 6),
                 ("open", "Wat is een cliffhanger, en waarom staat hij net op het eind van een "
                          "hoofdstuk?",
                  "Een cliffhanger eindigt op het spannendste moment, zonder uitkomst. Op het eind van "
                  "een hoofdstuk werkt dat omdat de lezer daar normaal zou stoppen: nu leest hij door.", 5),
                 ("open", "Een verhaal laat je van het begin weten dat het slecht eindigt. Kan dat nog "
                          "spannend zijn?",
                  "Ja. De spanning gaat dan niet over wát er gebeurt maar over hoe het zover komt, en of "
                  "iemand het nog kan keren. Dat de lezer meer weet dan het personage, maakt de scènes "
                  "juist zwaarder.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-genres-fictie-en-non-fictie-en-je-eigen-leeservaring-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Genres, fictie en non-fictie, en je eigen leeservaring",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk genre?",
             opdracht="Noteer het genre.",
             oefeningen=[
                 ("rij", [("een lang verhaal met meerdere verhaallijnen", "de roman"),
                          ("korter, met minder verhaallijnen", "de novelle"),
                          ("kort, en het draait om één moment", "het kortverhaal")],
                  "Welk genre?", WL),
                 ("rij", [("tekstballonnen en kaders, met wit ertussen", "de strip"),
                          ("dezelfde middelen, langer en voor een ouder publiek", "de graphic novel"),
                          ("haast volledig dialoog en regieaanwijzingen", "de toneeltekst")],
                  "Welk genre?", WL),
                 ("rij", [("een boek over het leven van een echte persoon", "de biografie"),
                          ("een boek dat iemand over zijn eigen leven schrijft", "de autobiografie"),
                          ("werkt met ritme, regelval en beeldtaal", "de poezie")], "Welk genre?", WL),
             ]),
        dict(kop="Fictie of non-fictie?",
             opdracht="Noteer wat het is.",
             oefeningen=[
                 ("kort", "een roman over een echte oorlog, met bedachte gesprekken", "fictie", WW),
                 ("kort", "een boek waarin een echte politicus bedachte gesprekken voert", "fictie", WW),
                 ("kort", "een reisverhaal van wat de schrijver zelf meemaakte", "non-fictie", WW),
                 ("kort", "een graphic novel over een oorlog, met echte getuigenissen", "non-fictie", WW),
             ]),
        dict(kop="Je leeservaring verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen. Zeg niet alleen wát je vindt, maar ook waaróm.",
             oefeningen=[
                 ("open", "Beschrijf een boek dat je niet uitgelezen hebt, en zeg waarom je stopte. "
                          "Gebruik minstens één begrip uit dit thema.",
                  "Een goed antwoord noemt de titel, zegt wat er niet werkte (de spanning kwam te laat, "
                  "het perspectief hield je op afstand, het genre lag je niet) en verbindt dat aan een "
                  "begrip. Stoppen is een geldig oordeel, zolang je het kan verantwoorden.", 6),
                 ("open", "Mag je een boek goed vinden dat je niet graag las? Leg uit.",
                  "Ja. Of je iets graag leest, gaat over je smaak; of het goed is, gaat over hoe het "
                  "gemaakt is: de opbouw, de personages, de taal. Een boek kan je zwaar vallen en toch "
                  "sterk zijn. Zeg dus wat je vond én waarom.", 5),
                 ("open", "Twee lezers lezen hetzelfde boek en hebben een heel ander oordeel. Hoe kan "
                          "dat?",
                  "Omdat je leeservaring ook van jou afhangt: wat je al gelezen hebt, wat je herkent, in "
                  "welke stemming je was. Daarom hoort een oordeel altijd met een reden erbij, anders kan "
                  "de ander er niets mee.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Eén boek kan tot meerdere genres horen.", True),
                 ("waar", "Een verhaal dat op echte feiten berust, is daarom non-fictie.", False),
                 ("waar", "Poëzie moet rijmen om poëzie te zijn.", False),
                 ("waar", "Een graphic novel kan ook non-fictie zijn.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-taalvarieteiten-registers-en-beleefdheid-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Taalvariëteiten, registers en beleefdheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke variëteit?",
             opdracht="Noteer of het om standaardtaal, tussentaal, dialect, een vaktaal of een groepstaal gaat.",
             oefeningen=[
                 ("rij", [("de taal van het journaal", "standaardtaal"),
                          ("ge moet daar is naar gaan kijken", "tussentaal"),
                          ("een arts die over een anamnese spreekt", "jargon of vaktaal")],
                  "Welke variëteit?", WL),
                 ("rij", [("woorden die enkel in één streek bestaan", "dialect of streektaal"),
                          ("de taal van jongeren onderling", "jongerentaal"),
                          ("een akte bij de notaris", "standaardtaal")], "Welke variëteit?", WL),
             ]),
        dict(kop="Van register wisselen",
             opdracht="Herschrijf de zin in het gevraagde register. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "Formeel maken: \"Kunde gij da ding is doorsturen?\"",
                  "Zou u dat document willen doorsturen? (Standaardtaal, u, een naamwoord in plaats van "
                  "\"dat ding\", en geen \"is\" voor \"eens\".)", 3),
                 ("open", "Formeel maken: \"We gaan dat volgende week ff bekijken.\"",
                  "Wij bekijken dat volgende week. Of: We nemen dat volgende week door. (Geen afkorting, "
                  "geen \"gaan\" als vulwerkwoord.)", 3),
                 ("open", "Informeel maken: \"Gelieve uw aanwezigheid tijdig te bevestigen.\"",
                  "Laat even weten of je komt. (Je in plaats van u, een gewoon werkwoord in plaats van "
                  "\"gelieve te\".)", 3),
             ]),
        dict(kop="U of je?",
             opdracht="Noteer wat je hier gebruikt, en waarom in één woord.",
             oefeningen=[
                 ("kort", "een mail aan de directeur van een school waar je solliciteert", "u — afstand", WL),
                 ("kort", "een bericht aan een klasgenoot", "je — vertrouwd", WL),
                 ("kort", "een brief aan de dienst burgerzaken", "u — formeel", WL),
                 ("kort", "een praatje met je stagebegeleider die zelf jij zegt", "je — hij begon", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Is dialect minder goed dan standaardtaal? Leg uit.",
                  "Nee. Een dialect heeft zijn eigen regels en is even volwaardig. Wat verschilt, is waar "
                  "je het kan gebruiken: standaardtaal wordt overal begrepen, een dialect alleen in zijn "
                  "streek. Dat is een kwestie van bereik, niet van kwaliteit.", 5),
                 ("open", "Waarom is te formeel schrijven ook een fout?",
                  "Omdat je register bij je situatie moet passen. Een plechtige brief aan een vriend "
                  "klinkt afstandelijk of spottend, en de ander weet niet meer hoe hij je moet lezen. "
                  "Te formeel is even misplaatst als te familiair.", 5),
                 ("open", "Een arts legt een diagnose uit aan een patiënt. Hoe doet ze dat het best?",
                  "Ze gebruikt gewone woorden en noemt de vakterm erbij. Dan begrijpt de patiënt het "
                  "meteen, en kan hij het woord later terugvinden in een verslag. Jargon is onder "
                  "vakgenoten precies, maar tegenover een leek sluit het buiten.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-taal-en-identiteit-stereotypering-inclusie-en-exclusie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Taal en identiteit: stereotypering, inclusie en exclusie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat gebeurt er in de zin?",
             opdracht="Noteer wat deze formulering doet: generaliseren, stereotyperen, uitsluiten of insluiten.",
             oefeningen=[
                 ("kort", "Jongeren lezen niet meer.", "een veralgemening", WL),
                 ("kort", "Die zijn allemaal muzikaal.", "een stereotype", WL),
                 ("kort", "Veel jongeren in dit onderzoek lezen minder dan vroeger.", "precies: niets van de twee", WL),
                 ("kort", "Een vacature zoekt een jonge, dynamische kracht.", "uitsluiten", WL),
                 ("kort", "Een tekst spreekt over de gewone Vlaming.", "een norm stellen, dus uitsluiten", WL),
                 ("kort", "Moeilijke vaktermen worden bij het eerste gebruik uitgelegd.", "inclusief taalgebruik", WL),
             ]),
        dict(kop="Herschrijven",
             opdracht="Herschrijf de zin zodat niemand uitgesloten wordt. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "Beste heren, hierbij de uitnodiging voor de vergadering.",
                  "Beste leden, hierbij de uitnodiging voor de vergadering. (Een aanspreking die niemand "
                  "van de groep weglaat.)", 3),
                 ("open", "Elke leerling moet zijn boek meebrengen.",
                  "Elke leerling brengt zijn of haar boek mee. Of: Alle leerlingen brengen hun boek mee. "
                  "(Het meervoud lost het eenvoudigst op.)", 3),
                 ("open", "De vergadering is op de eerste verdieping, dus kom op tijd voor de trap.",
                  "De vergadering is op de eerste verdieping; er is een lift naast de trap. (Je noemt de "
                  "weg die iedereen kan nemen.)", 3),
             ]),
        dict(kop="Gevoelswaarde",
             opdracht="Noteer welk woord van het paar positiever klinkt, en wat het verschil is.",
             oefeningen=[
                 ("rij", [("zuinig / gierig", "zuinig"),
                          ("volhardend / koppig", "volhardend"),
                          ("ambitieus / gehaaid", "ambitieus")], "Positiever", WW),
                 ("rij", [("behulpzaam / bemoeiziek", "behulpzaam"),
                          ("sober / kaal", "sober"),
                          ("eigenzinnig / dwars", "eigenzinnig")], "Positiever", WW),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom is \"ik bedoelde het niet slecht\" geen antwoord op de opmerking dat "
                          "een woord kwetst?",
                  "Omdat het effect van een woord niet alleen van je bedoeling afhangt. De ander hoort wat "
                  "er staat, niet wat je dacht. Je kan je bedoeling uitleggen, maar het woord blijft "
                  "kwetsen, dus je kiest een ander.", 5),
                 ("open", "Een nieuwsbericht noemt bij één verdachte zijn afkomst en bij een andere niet. "
                          "Wat is daar het probleem mee?",
                  "De lezer verbindt de daad met die afkomst. Informatie die niets verklaart maar wel "
                  "gekoppeld wordt, blijft toch hangen. Een schrijver is verantwoordelijk voor het beeld "
                  "dat zijn woorden oproepen, ook wat hij niet bedoelde.", 5),
                 ("open", "Geef één reden waarom taal zo verbonden is met identiteit.",
                  "Omdat hoe iemand spreekt bij hoort wie hij is: je streek, je groep, je vak klinken "
                  "erin mee. Daarom raakt kritiek op iemands taal vaak harder aan dan bedoeld.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-klanken-spelling-diakritische-tekens-en-interpunctie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Klanken, spelling, diakritische tekens en interpunctie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Werkwoordspelling",
             opdracht="Vul het werkwoord juist in.",
             oefeningen=[
                 ("rij", [("hij ... (antwoorden, nu)", "antwoordt"),
                          ("ik ... (verwachten, nu)", "verwacht"),
                          ("zij ... (gebeuren, verleden tijd)", "gebeurde")], "Juiste vorm", WW),
                 ("rij", [("het is ... (gebeuren, voltooid)", "gebeurd"),
                          ("wat jij ... (willen, nu)", "wil of wilt"),
                          ("hij heeft het ... (verwachten, voltooid)", "verwacht")], "Juiste vorm", WW),
                 ("rij", [("zij ... (vinden, verleden tijd)", "vond"),
                          ("word jij of wordt jij? (vraag)", "word jij"),
                          ("hij ... (worden, nu)", "wordt")], "Juiste vorm", WW),
             ]),
        dict(kop="Tussenletters",
             opdracht="Schrijf het samengestelde woord juist.",
             oefeningen=[
                 ("rij", [("pannen + koek", "pannenkoek"), ("zon + bloem", "zonnebloem"),
                          ("boek + winkel", "boekwinkel")], "Juist geschreven", WW),
                 ("rij", [("tand + arts", "tandarts"), ("koning + huis", "koningshuis"),
                          ("hemel + lichaam", "hemellichaam")], "Juist geschreven", WW),
             ]),
        dict(kop="Diakritische tekens",
             opdracht="Zet het juiste teken en noteer hoe het teken heet.",
             oefeningen=[
                 ("rij", [("een idee (meervoud)", "ideeen wordt ideeën — trema"),
                          ("een cafe", "café — accent aigu"),
                          ("een appel waar je van eet", "appel; appèl is een oproep — accent grave")],
                  "Teken en naam", WL),
             ]),
        dict(kop="Interpunctie",
             opdracht="Zet de ontbrekende tekens en schrijf de zin volledig uit.",
             oefeningen=[
                 ("open", "Toen ze binnenkwam stonden alle stoelen al klaar",
                  "Toen ze binnenkwam, stonden alle stoelen al klaar. (Komma na een bijzin die vooraan "
                  "staat, punt op het eind.)", 3),
                 ("open", "Ik heb drie dingen nodig potlood papier en een gom",
                  "Ik heb drie dingen nodig: potlood, papier en een gom. (Dubbelpunt voor de opsomming, "
                  "komma's tussen de delen, geen komma voor \"en\".)", 3),
                 ("open", "Mijn broer die in Gent woont komt morgen langs",
                  "Mijn broer, die in Gent woont, komt morgen langs. (Twee komma's rond de bijgevoegde "
                  "informatie: zonder die komma's zou je meerdere broers hebben.)", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "In een vraag met \"jij\" achter het werkwoord valt de t weg: word jij.", True),
                 ("waar", "Een trema en een accent aigu doen hetzelfde.", False),
                 ("waar", "Een komma kan de betekenis van een zin veranderen.", True),
                 ("waar", "Alle samenstellingen met een meervoud erin krijgen een tussen-n.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordsoorten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Woordsoorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Benoem de woordsoort",
             opdracht="Noteer de woordsoort van het vetgedrukte woord.",
             oefeningen=[
                 ("rij", [("de fiets staat <b>onder</b> het afdak", "voorzetsel"),
                          ("hij liep <b>snel</b> naar binnen", "bijwoord"),
                          ("<b>die</b> jas is van mij", "aanwijzend voornaamwoord")], "Woordsoort", WL),
                 ("rij", [("we wachten, <b>want</b> het regent", "voegwoord"),
                          ("<b>mijn</b> boek ligt boven", "bezittelijk voornaamwoord"),
                          ("een <b>snelle</b> fiets", "bijvoeglijk naamwoord")], "Woordsoort", WL),
                 ("rij", [("<b>er</b> staat iemand aan de deur", "bijwoord"),
                          ("ze gaf het <b>hem</b>", "persoonlijk voornaamwoord"),
                          ("<b>drie</b> stoelen stonden leeg", "telwoord")], "Woordsoort", WL),
             ]),
        dict(kop="Bijvoeglijk naamwoord of bijwoord?",
             opdracht="Noteer wat het vetgedrukte woord is, en waar het bij hoort.",
             oefeningen=[
                 ("kort", "een <b>snelle</b> trein", "bijvoeglijk naamwoord — bij trein", WL),
                 ("kort", "de trein rijdt <b>snel</b>", "bijwoord — bij rijdt", WL),
                 ("kort", "een <b>mooi</b> verhaal", "bijvoeglijk naamwoord — bij verhaal", WL),
                 ("kort", "ze schrijft <b>mooi</b>", "bijwoord — bij schrijft", WL),
             ]),
        dict(kop="Zelf zoeken",
             opdracht="Zoek in de zin het gevraagde woord en schrijf het op.",
             oefeningen=[
                 ("kort", "Het voorzetsel in: \"De sleutel lag achter de kast.\"", "achter", WW),
                 ("kort", "Het onderschikkende voegwoord in: \"Ik kom niet omdat ik moet werken.\"", "omdat", WW),
                 ("kort", "Het lidwoord in: \"Er stond een auto in de straat.\" (onbepaald)", "een", WW),
                 ("kort", "Het wederkerend voornaamwoord in: \"Hij vergist zich altijd.\"", "zich", WW),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Hetzelfde woord kan tot twee woordsoorten horen. Geef een voorbeeld en leg "
                          "uit hoe je het verschil ziet.",
                  "\"Dat\" is een aanwijzend voornaamwoord in \"dat boek\" en een voegwoord in \"ik weet "
                  "dat hij komt\". Je ziet het verschil aan de functie in de zin, niet aan het woord zelf: "
                  "kijk waar het bij hoort en wat het verbindt.", 6),
                 ("open", "Waarom helpt het om een woord te vervangen als je de woordsoort zoekt?",
                  "Omdat je zo test wat er op die plaats kan staan. Als je \"onder\" kan vervangen door "
                  "\"naast\" of \"boven\", staat er een voorzetsel. Past er een bijvoeglijk naamwoord, "
                  "dan hoort het woord bij een naamwoord.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Morfologie: samenstellingen, afleidingen en werkwoordstijden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Samenstelling of afleiding?",
             opdracht="Noteer wat het woord is, en uit welke delen het bestaat.",
             oefeningen=[
                 ("rij", [("tafelpoot", "samenstelling: tafel + poot"),
                          ("onvriendelijk", "afleiding: on- + vriendelijk"),
                          ("boekenkast", "samenstelling: boeken + kast")], "Wat en hoe?", WL),
                 ("rij", [("verzorging", "afleiding: ver- + zorg + -ing"),
                          ("spoorwegovergang", "samenstelling uit drie delen"),
                          ("schrijver", "afleiding: schrijv- + -er")], "Wat en hoe?", WL),
             ]),
        dict(kop="De stam vinden",
             opdracht="Noteer de stam van het werkwoord.",
             oefeningen=[
                 ("rij", [("werken", "werk"), ("verwachten", "verwacht"),
                          ("antwoorden", "antwoord")], "Stam", WW),
                 ("rij", [("gebeuren", "gebeur"), ("zetten", "zet"),
                          ("rijden", "rijd")], "Stam", WW),
             ]),
        dict(kop="De juiste tijd",
             opdracht="Noteer in welke tijd de zin staat.",
             oefeningen=[
                 ("rij", [("hij heeft gewerkt", "voltooid tegenwoordige tijd"),
                          ("hij werkte", "verleden tijd"),
                          ("hij zal werken", "toekomende tijd")], "Welke tijd?", WL),
                 ("rij", [("hij had gewerkt voor ik aankwam", "voltooid verleden tijd"),
                          ("hij werkt", "tegenwoordige tijd"),
                          ("morgen ga ik", "toekomende tijd")], "Welke tijd?", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Wat is de stam van een werkwoord, en waarom is de stam niet hetzelfde als de "
                          "infinitief?",
                  "De stam is de infinitief zonder uitgang: de stam van werken is werk. De infinitief is "
                  "het hele woord, de stam het deel waarop je de vormen bouwt. Daarom spel je met de "
                  "stam, niet met de infinitief.", 5),
                 ("open", "Geef twee woorden die met een voorvoegsel zijn afgeleid en twee met een "
                          "achtervoegsel, en zeg wat het voor- of achtervoegsel doet.",
                  "Voorvoegsel: onvriendelijk (on- maakt het tegengestelde), verbouwen (ver- geeft een "
                  "verandering). Achtervoegsel: schrijver (-er maakt er een persoon van), verzorging "
                  "(-ing maakt er een handeling of een ding van).", 6),
                 ("open", "Wat is het verschil tussen een sterk en een zwak werkwoord? Geef van elk een "
                          "voorbeeld.",
                  "Bij een sterk werkwoord verandert de klinker in de verleden tijd: lopen wordt liep, "
                  "zingen wordt zong en gezongen. Bij een zwak werkwoord komt er alleen een uitgang bij "
                  "en blijft de klinker dezelfde: werken wordt werkte en gewerkt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-zinsontleding-en-zinsbouw-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Zinsontleding en zinsbouw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Onderwerp en persoonsvorm",
             opdracht="Noteer de persoonsvorm en het onderwerp van de zin.",
             oefeningen=[
                 ("rij", [("Mijn zus belde gisteren op.", "belde — mijn zus"),
                          ("Er stonden drie fietsen in de gang.", "stonden — drie fietsen"),
                          ("Morgen komt de loodgieter langs.", "komt — de loodgieter")],
                  "Persoonsvorm en onderwerp", WL),
             ]),
        dict(kop="Welk zinsdeel?",
             opdracht="Noteer de functie van het vetgedrukte zinsdeel.",
             oefeningen=[
                 ("rij", [("Ze gaf <b>haar broer</b> het boek.", "meewerkend voorwerp"),
                          ("Ze gaf haar broer <b>het boek</b>.", "lijdend voorwerp"),
                          ("Hij is <b>leraar</b>.", "naamwoordelijk deel van het gezegde")],
                  "Welke functie?", WL),
                 ("rij", [("<b>Gisteren</b> stond de bus stil.", "bijwoordelijke bepaling van tijd"),
                          ("Hij speelt <b>in de tuin</b>.", "bijwoordelijke bepaling van plaats"),
                          ("<b>De man met de hoed</b> lachte.", "onderwerp")], "Welke functie?", WL),
             ]),
        dict(kop="Hoofdzin en bijzin",
             opdracht="Noteer hoeveel hoofdzinnen en hoeveel bijzinnen de zin bevat.",
             oefeningen=[
                 ("kort", "Ik kom niet, omdat ik moet werken.", "1 hoofdzin, 1 bijzin", WL),
                 ("kort", "Hij belde en zij opende de deur.", "2 hoofdzinnen, 0 bijzinnen", WL),
                 ("kort", "Toen het begon te regenen, liepen we naar binnen, want we hadden geen paraplu.",
                  "2 hoofdzinnen, 1 bijzin", WL),
             ]),
        dict(kop="Herschrijven",
             opdracht="Herschrijf de zin zodat hij vlot leest. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "Door het feit dat er sprake was van een vertraging, is de aankomst later "
                          "geweest dan voorzien.",
                  "Door de vertraging kwamen we later aan dan voorzien. (Weg met \"door het feit dat\" en "
                  "\"er is sprake van\"; een gewoon werkwoord in plaats van een naamwoord.)", 4),
                 ("open", "De brief die naar de ouders die vorig jaar ingeschreven waren gestuurd werd, "
                          "was onduidelijk.",
                  "De brief aan de ouders die vorig jaar inschreven, was onduidelijk. (Eén bijzin minder, "
                  "en de bepaling niet in de andere gepropt: anders staat je persoonsvorm te ver van je "
                  "onderwerp.)", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een kruisje in de juiste kolom.",
             oefeningen=[
                 ("waar", "Een zin kan meer dan één persoonsvorm hebben.", True),
                 ("waar", "Elke zin heeft een lijdend voorwerp.", False),
                 ("waar", "In een bijzin staat de persoonsvorm meestal achteraan.", True),
                 ("waar", "Het onderwerp staat altijd vooraan in de zin.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-semantiek-betekenisrelaties-gevoelswaarde-en-humor-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Semantiek: betekenisrelaties, gevoelswaarde en humor",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke relatie?",
             opdracht="Noteer de relatie tussen de twee woorden.",
             oefeningen=[
                 ("rij", [("fiets en vervoermiddel", "vervoermiddel is het hyperoniem"),
                          ("groot en klein", "antoniemen"),
                          ("beginnen en starten", "synoniemen")], "Welke relatie?", WL),
                 ("rij", [("bank (om te zitten) en bank (met geld)", "homoniemen"),
                          ("roos (bloem) en roos (in het haar)", "homoniemen"),
                          ("roos en bloem", "bloem is het hyperoniem")], "Welke relatie?", WL),
             ]),
        dict(kop="Letterlijk of figuurlijk?",
             opdracht="Noteer wat de uitdrukking betekent.",
             oefeningen=[
                 ("rij", [("de kat uit de boom kijken", "afwachten"),
                          ("boter op het hoofd hebben", "zelf schuld hebben"),
                          ("iets door de vingers zien", "niet bestraffen")], "Betekenis", WL),
                 ("rij", [("van de hand in de tand leven", "van dag tot dag"),
                          ("het hoofd koel houden", "rustig blijven"),
                          ("een oogje in het zeil houden", "opletten")], "Betekenis", WL),
             ]),
        dict(kop="Waarop werkt de grap?",
             opdracht="Noteer wat deze vorm van humor laat werken: woordspel, ironie, overdrijving of een onverwachte wending.",
             oefeningen=[
                 ("kort", "\"Mooi weer\", zei hij, terwijl het goot.", "ironie", WL),
                 ("kort", "Ik heb duizend keer gezegd dat ik niet overdrijf.", "overdrijving", WL),
                 ("kort", "Een bank die omvalt is nog altijd een meubel.", "woordspel op een homoniem", WL),
                 ("kort", "Hij studeerde drie weken en vergat de dag van het examen.", "onverwachte wending", WL),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Twee woorden zijn synoniem, en toch kan je ze niet altijd verwisselen. Leg uit "
                          "met een voorbeeld.",
                  "\"Sterven\" en \"heengaan\" betekenen hetzelfde, maar hun gevoelswaarde verschilt: in "
                  "een rouwbericht past \"heengaan\", in een verslag \"sterven\". Synoniemen delen hun "
                  "betekenis, niet hun gevoelswaarde.", 5),
                 ("open", "Waarom werkt ironie niet altijd in een bericht?",
                  "Omdat ironie van je toon leeft, en die hoort de lezer niet. In een gesprek hoor je aan "
                  "mijn stem dat ik het omgekeerde bedoel; in geschreven tekst moet iets anders dat "
                  "signaleren, en zonder dat signaal neemt de lezer je letterlijk.", 5),
                 ("open", "Wat is het verschil tussen twee homoniemen en één woord met meerdere "
                          "betekenissen? Geef van elk een voorbeeld.",
                  "Bij homoniemen zijn het twee woorden die toevallig dezelfde vorm hebben en niets met "
                  "elkaar te maken hebben: de bank om op te zitten en de bank waar je geld haalt. Bij één "
                  "woord met meerdere betekenissen horen die betekenissen bij elkaar: de voet van een mens "
                  "en de voet van een berg zijn allebei het onderste deel.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-en-schriftelijke-interactie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Schrijven en schriftelijke interactie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stap van het schrijfproces?",
             opdracht="Noteer of dit bij plannen, schrijven, herwerken of nalezen hoort.",
             oefeningen=[
                 ("rij", [("je notities in de orde van het gesprek zetten", "plannen"),
                          ("de eerste versie uitschrijven", "schrijven"),
                          ("twee alinea's van plaats wisselen", "herwerken")], "Welke stap?", WL),
                 ("rij", [("de werkwoordsvormen controleren", "nalezen"),
                          ("een alinea die niets toevoegt schrappen", "herwerken"),
                          ("je tekst luidop lezen om te horen waar een zin niet loopt", "nalezen")],
                  "Welke stap?", WL),
             ]),
        dict(kop="Welke tekstvorm, en wat hoort erin?",
             opdracht="Noteer de vorm die hier past en wat er in die vorm hoort.",
             oefeningen=[
                 ("kort", "je wil later terugvinden wat beslist werd en wie wat doet", "het verslag", WL),
                 ("kort", "je wil een standpunt verdedigen met argumenten", "het opiniestuk of betoog", WL),
                 ("kort", "iemand moet een toestel stap voor stap gebruiken", "de instructie", WL),
                 ("kort", "je product werd niet geleverd en je wil een oplossing", "de klacht: feiten, data, bedragen", WL),
                 ("kort", "je wil weten of een bedrijf nog werk heeft", "de sollicitatiebrief", WL),
             ]),
        dict(kop="Herschrijven",
             opdracht="Herschrijf zodat het past bij de ontvanger. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "In een sollicitatiemail: \"Ik zou wel es willen komen werken bij jullie, lijkt "
                          "me wel tof.\"",
                  "Graag solliciteer ik voor de vacature in uw winkel. Ik ga vlot met klanten om en ik "
                  "kan op zaterdag werken. (Standaardtaal, en je zegt wat jij voor de werkgever kan "
                  "doen, niet enkel wat jij wil.)", 4),
                 ("open", "In een klachtenmail: \"Dit is belachelijk, jullie doen nooit iets.\"",
                  "Mijn pakket is drie weken na de bestelling nog niet geleverd. Ik vraag u het alsnog te "
                  "verzenden of het bedrag terug te storten. (Een feit, een duidelijke vraag, geen "
                  "verwijt: zo krijg je sneller wat je wil.)", 4),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom lees je je tekst beter de dag nadien na?",
                  "Omdat je dan niet meer weet wat je bedoelde te schrijven, maar ziet wat er staat. "
                  "Meteen na het schrijven leest je hoofd de bedoeling mee en glijd je over fouten en "
                  "onduidelijke zinnen heen.", 5),
                 ("open", "Wat is het verschil tussen herwerken en nalezen, en welke komt eerst?",
                  "Herwerken gaat over de opbouw: alinea's schrappen, verplaatsen, verduidelijken. "
                  "Nalezen gaat over de spelling en de werkwoorden. Herwerken komt eerst: een alinea die "
                  "sneuvelt, hoef je niet gespeld te hebben.", 5),
                 ("open", "Noem twee dingen die je vastlegt vóór je de eerste zin schrijft, en zeg wat "
                          "daarvan afhangt.",
                  "Mijn doel en mijn publiek. Daar hangt van af hoeveel voorkennis ik veronderstel, of "
                  "ik vaktermen uitleg of gewoon gebruik, en welke lengte en toon de tekst krijgt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spreken-en-gesprekken-voeren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Spreken en gesprekken voeren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Open of gesloten vraag?",
             opdracht="Noteer of dit een open of een gesloten vraag is, en wat ze je oplevert.",
             oefeningen=[
                 ("rij", [("Hoe verliep de vergadering?", "open: je krijgt een verhaal"),
                          ("Komt u donderdag?", "gesloten: ja of nee"),
                          ("Waarom koos je daarvoor?", "open: je krijgt een verhaal")],
                  "Welke vraag?", WL),
                 ("rij", [("Is het dossier verstuurd?", "gesloten: ja of nee"),
                          ("Wat zou er volgens u moeten veranderen?", "open: je krijgt een verhaal"),
                          ("Spreken we af om tien uur?", "gesloten: legt vast")], "Welke vraag?", WL),
             ]),
        dict(kop="Wat doe je in een gesprek?",
             opdracht="Noteer hoe dat heet, of wat je ermee bereikt.",
             oefeningen=[
                 ("rij", [("je spreekt op je moment en laat de ander uitspreken", "beurten nemen"),
                          ("je zegt kort in eigen woorden wat de ander zei", "samenvatten of parafraseren"),
                          ("je vraagt: bedoel je dat…?", "navragen met je eigen woorden")],
                  "Hoe heet dat?", WL),
                 ("rij", [("je kijkt de ander aan en knikt af en toe", "laten merken dat je luistert"),
                          ("je benoemt waar jullie het wel over eens zijn", "een moeilijk gesprek op gang houden"),
                          ("je noemt wie wat doet en tegen wanneer", "een afspraak concreet maken")],
                  "Hoe heet dat?", WL),
             ]),
        dict(kop="Beter formuleren",
             opdracht="Herschrijf wat je zegt. Schrijf de hele zin uit.",
             oefeningen=[
                 ("open", "In een discussie: \"Dat is gewoon stom, dat werkt nooit.\"",
                  "Ik denk dat dat niet werkt, omdat we er geen tijd voor hebben op donderdag. (Je zegt "
                  "wat je vindt én waarom, en je valt het plan aan en niet de persoon.)", 4),
                 ("open", "Aan het begin van je presentatie: \"Euh, ik ga iets zeggen over mijn "
                          "onderwerp.\"",
                  "Wist u dat niemand hier op school water kan drinken na vier uur? Daarover gaat het, "
                  "in drie punten. (Je begint met iets dat de aandacht vangt en je onderwerp aankondigt, "
                  "en je zegt hoeveel punten je behandelt.)", 4),
             ]),
        dict(kop="Zelf verwoorden",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom werkt een presentatie met steekwoorden beter dan een voorgelezen "
                          "presentatie?",
                  "Wie voorleest, kijkt niet: je verliest je oogcontact en je kan niet bijsturen als de "
                  "zaal je niet volgt. Met steekwoorden blijf je spreken in plaats van lezen.", 5),
                 ("open", "Twee mensen vallen elkaar in de rede. Wat doe je?",
                  "Ik vraag om één voor één te spreken. Een vlot gesprek is een reeks beurten: wie "
                  "altijd neemt of altijd wacht, verstoort het.", 4),
                 ("open", "Je geeft iemand telefonisch een instructie. Hoe weet je dat het overkwam?",
                  "Ik laat de ander op het einde de stappen terug zeggen. Op de vraag \"is het "
                  "duidelijk?\" antwoordt bijna iedereen ja, dus die vraag zegt niets.", 4),
             ]),
    ],
)

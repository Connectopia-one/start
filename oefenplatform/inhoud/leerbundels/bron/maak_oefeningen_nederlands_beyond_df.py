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
                          ("werkt met ritme, regelval en beeldtaal", "de poëzie")], "Welk genre?", WL),
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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-onderwerp-hoofdgedachte-en-hoofdpunten-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén proef scheidt de twee: een onderwerp zeg je in een paar woorden, een "
                   "hoofdgedachte is een hele zin met een bewering erin.",
            waarom=[
                "Let erop dat een hoofdgedachte een werkwoord heeft. Waar je ja of nee op kan "
                "antwoorden, is een hoofdgedachte.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je bij elke zin af of ze het standpunt draagt. Draagt ze het, dan is het een "
                   "hoofdpunt; is ze enkel aardig om te weten, dan is het een detail.",
            waarom=[
                None,
                "Let erop dat een naam en een aantal jaren dienst niets met de openingsuren te maken "
                "hebben. Namen en kleine cijfers zijn bijna altijd details.",
                None,
                "Let erop dat ook een cijfer een detail kan zijn. Het aantal stoelen zegt niets over "
                "de vraag of de bibliotheek langer open moet.",
            ],
        ),
        dict(
            aanpak="Schrijf de hoofdgedachte als één zin met een boodschap erin, en zet erbij wat het "
                   "onderwerp was. Zo zie je zelf of je niet enkel het onderwerp herhaalt.",
            waarom=[
                "Let erop dat lezen bij jongeren het onderwerp is. De hoofdgedachte is wat de tekst "
                "daarover beweert, namelijk dat scholen leestijd moeten inbouwen.",
                "Let erop dat een reportage een hoofdgedachte kan hebben zonder ze uit te spreken. Wat "
                "ze laat zien en vraagt, is wat ze bedoelt.",
            ],
        ),
        dict(
            aanpak="Hou je opdracht naast elk gegeven: kost het openbaar vervoer per jaar voor een "
                   "scholier? Alles wat die vraag niet helpt beantwoorden, valt weg.",
            waarom=[
                None,
                "Let erop dat het aantal reizigers interessant is en jouw vraag niet beantwoordt. "
                "Relevantie hangt van de opdracht af en niet van de bron.",
                "Let erop dat de korting wel meetelt: ze verandert de prijs die een scholier echt "
                "betaalt.",
                None,
            ],
        ),
        dict(
            aanpak="Drie vragen over samenvatten en notities. Hou vast dat een samenvatting korter is, "
                   "en dat je bij luisteren niet kan terugspoelen.",
            waarom=[
                "Noem beide delen: wat er mis is en wat hij moet doen. Dat de voorbeelden eruit "
                "moeten, is het concrete advies.",
                "Noem dat je niet kan terugspoelen. En noem de manier: steekwoorden, afkortingen en "
                "witruimte om achteraf aan te vullen.",
                "Noem de datum en de afzender. Meestal verklaart dat het verschil al, en anders zeg je "
                "in je tekst welk cijfer van welke bron komt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-en-teksttypes-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke tekst af wat de zender wil: iets laten weten, iets laten doen, "
                   "je overtuigen, een verhaal vertellen, of iets laten voelen door de vorm.",
            waarom=[
                "Let op prescriptief: dat is de soort die zegt wat je moet doen, zoals een bijsluiter "
                "of een handleiding.",
                None,
                "Let op het verschil tussen argumentatief en persuasief: een betoog bouwt argumenten "
                "op, een affiche met één kreet wil enkel overtuigen.",
            ],
        ),
        dict(
            aanpak="Hier horen er altijd twee soorten bij. Lees de tekst in stukken: het ene stuk "
                   "informeert of vertelt, het andere beoordeelt of overtuigt.",
            waarom=[
                None,
                None,
                "Let op de blog: het verhaal maakt je welwillend en de aanbeveling is het echte doel. "
                "Dat is precies hoe sluikreclame werkt.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat literair kan zijn, wat op het examen kan "
                   "komen, en of het kanaal de soort bepaalt.",
            waarom=[
                None,
                "Niet waar: ook een gesprek in dialect of tussentaal kan op het examen staan. Je moet "
                "die variëteit juist kunnen plaatsen.",
                "Waar, en toch zijn het geen gelijken: reclame wil verkopen, propaganda wil je denken "
                "sturen, en nepnieuws doet alsof het nieuws is. Alle drie willen ze je overtuigen.",
                "Niet waar: het kanaal verandert de soort niet. Een reportage en een artikel kunnen "
                "even goed informatief zijn.",
                None,
            ],
        ),
        dict(
            aanpak="Drie open vragen over hetzelfde idee: de bedoeling van de zender beslist de soort, "
                   "en één tekst kan meerdere bedoelingen hebben.",
            waarom=[
                "Noem beide delen: hoe zo'n tekst heet en waarom het bedrijf die vorm kiest. Dat een "
                "neutraal uitziende tekst meer vertrouwen krijgt, is de kern.",
                "Noem ook waarom die vraag de beste is. De bedoeling beslist de soort, en ze zegt je "
                "ook hoe kritisch je moet lezen.",
                "Noem dat je wel het belangrijkste doel zoekt. Zo geef je je vriend een stukje gelijk "
                "zonder zijn stelling over te nemen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes signalen. Vraag je bij elk af wat je mist: de tijd, de afzender, de bron van "
                   "een cijfer, of de oorspronkelijke context van een beeld.",
            waarom=[
                "Let op de hoofdletters: die werken op je gevoel in plaats van op je verstand. Dat is "
                "een vormsignaal en geen inhoudelijk argument, en net daarom valt het op.",
                "Let op de foto van een ander jaar: het beeld zelf kan echt zijn en toch misleiden. "
                "Dat komt in de laatste reeks terug.",
            ],
        ),
        dict(
            aanpak="Bij framing blijft het feit gelijk en verandert het gevoel. Zoek telkens het woord "
                   "dat dezelfde zaak benoemt met de omgekeerde bijklank.",
            waarom=[
                "Let erop dat beide woorden hetzelfde beschrijven. Een protestactie en een rel kunnen "
                "dezelfde namiddag zijn, enkel de kant verschilt.",
                "Let op spaarzaam en krenterig: hetzelfde beleid, een lovend en een afkeurend woord. "
                "Zulke paren zijn het bewijs dat woordkeuze een standpunt is.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat bronvermeldingen en vormgeving bewijzen, "
                   "wanneer je een belanghebbende bron mag gebruiken, en wat beelden bewijzen.",
            waarom=[
                "Waar: de bronnen kunnen slecht gekozen zijn of iets anders zeggen dan de tekst "
                "beweert. Je kijkt dus ook naar welke bronnen het zijn.",
                "Niet waar: een vormgeving kost een paar uur. Juist nepsites zien er vaak heel "
                "verzorgd uit.",
                "Waar, en dat is belangrijk: je mag de fabrikant of de partij citeren, zolang je zegt "
                "wie het is. Verzwijgen maakt het misleidend.",
                "Niet waar: beeld en geluid zijn vandaag te bewerken, en ook te monteren uit hun "
                "context. Een filmpje is een aanwijzing en geen bewijs.",
                None,
            ],
        ),
        dict(
            aanpak="Drie keer de vraag wat je concreet doet. Het antwoord is telkens hetzelfde soort: "
                   "terug naar de oorspronkelijke bron.",
            waarom=[
                "Noem dat je het niet doorstuurt zolang je de bron niet vindt. Dat is de stap die "
                "mensen overslaan, en doorsturen is zelf verspreiden.",
                "Noem dat je je stelling aanpast. Enkel de bronnen kiezen die je passen, is zelf "
                "framing, en dat is het ongemakkelijke deel van dit antwoord.",
                "Noem de omgekeerde beeldzoekopdracht met naam. En noem dat een echte foto van een "
                "andere plaats nog altijd misleidend is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-communicatiemodel-en-ruis-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vul het model altijd in dezelfde orde in: wie, wat, aan wie, waarmee, waarin, "
                   "waarvoor, en met welk gevolg.",
            waarom=[
                "Let op het verschil tussen het doel en het effect: het doel is wat de gemeente wil, "
                "het effect is wat de inwoners ermee doen. Die twee staan niet voor niets apart.",
            ],
        ),
        dict(
            aanpak="Eén vraag: zit de storing buiten de personen (externe ruis) of in hun hoofd "
                   "(interne ruis)? Geluid en techniek zijn buiten, gedachten en gevoelens binnen.",
            waarom=[
                None,
                "Let op de boze mail: de woorden veranderen niet, jouw humeur wel. Ruzie van gisteren "
                "en een vooroordeel zijn dus interne ruis, ook al voelt het alsof de tekst het doet.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: dat één bericht meerdere effecten kan hebben, "
                   "wat het kanaal wel en niet zegt, en wie doel en effect toekomen.",
            waarom=[
                None,
                "Niet waar: hetzelfde kanaal kan door iedereen gebruikt worden. Een brief zegt niet of "
                "de gemeente of een bedrijf hem stuurde; dat moet je in de tekst zoeken.",
                "Waar: het kanaal is dan de lucht en je stem. Elk gesprek heeft een kanaal, en bij een "
                "gesprek zit de feedback erbij.",
                "Niet waar: op papier schrijf je formeler dan in een appje. Het kanaal stuurt je toon "
                "mee, en dat is een van de redenen om het bewust te kiezen.",
                None,
            ],
        ),
        dict(
            aanpak="Drie open vragen over hetzelfde model. Noem bij elke vraag de onderdelen met hun "
                   "naam: zender, ontvanger, kanaal, doel, effect.",
            waarom=[
                "Noem dat ze niet altijd samenvallen, met een voorbeeld. Dat een zender het effect "
                "niet kan voorspellen, is de kern.",
                "Noem beide nadelen: de toon valt weg en je ziet de reactie niet. Dat tweede is wat "
                "een gesprek sterker maakt bij iets gevoeligs.",
                "Noem allebei: wat gelijk blijft en wat verandert. De feiten blijven, de toon en het "
                "kanaal volgen de ontvanger.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstopbouw-alineaverbanden-en-vaste-tekststructuren-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij twee alinea's af hoe de tweede zich tot de eerste verhoudt: volgt ze "
                   "eruit, spreekt ze tegen, komt ze erna, of vergelijkt ze?",
            waarom=[
                "Let op het verschil tussen oorzakelijk en chronologisch: bij het eerste veroorzaakt "
                "de ene alinea de andere, bij het tweede volgt ze er enkel in de tijd op.",
                "Let op doel-middel: er staat wat men wil bereiken en wat men daarvoor doet. Het "
                "woordje om kondigt dat bijna altijd aan.",
                "Let op voorwaardelijk: er staat niet dat het zo is, maar dat het zo is als iets "
                "anders gebeurt. Als en alleen als zijn de signalen.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke tekst af welke vragen hij achtereenvolgens beantwoordt. Die reeks "
                   "vragen is de structuur.",
            waarom=[
                None,
                "Let op het verschil tussen de probleem- en de maatregelstructuur: de eerste vertrekt "
                "van wat er mis is, de tweede van wat men gaat doen.",
                "Let op het verschil tussen evalueren en vergelijken: bij het eerste beoordeel je één "
                "zaak op criteria, bij het tweede zet je twee zaken op dezelfde criteria naast elkaar.",
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Een alinea hoort één punt te behandelen. Zoek het signaalwoord dat een tweede punt "
                   "aankondigt, en begin daar een nieuwe alinea.",
            waarom=[
                "Noem beide delen: waar je begint en waarom. Dat het woord daarnaast het tweede punt "
                "aankondigt, is het argument.",
                "Noem waarvoor het slot wel dient. Een nieuw argument heeft daar geen ruimte meer om "
                "uitgewerkt te worden, en dat zwakt je betoog af.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een alinea is, wat een inleiding doet, en "
                   "of structuren te combineren zijn.",
            waarom=[
                None,
                "Niet waar: soms houdt de schrijver zijn besluit bewust voor het einde. In een "
                "zakelijke tekst zet men het vaak wel vooraan, maar het is geen regel.",
                None,
                "Niet waar: een tekst kan een probleem schetsen en tegelijk zijn oplossing verdedigen. "
                "Structuren kunnen in elkaar zitten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-structuuraanduiders-verwijswoorden-en-signaalwoorden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer per verband één signaalwoord, dan herken je de rest erbij. Lees bij twijfel de "
                   "twee zinnen eromheen: de inhoud beslist.",
            waarom=[
                "Let op daardoor: dat kondigt een gevolg aan, dus wat eruit volgt. Daarom en bijgevolg "
                "doen hetzelfde.",
                "Let op kortom: dat vat samen wat je al gelezen hebt en voegt niets nieuws toe. Wie dat "
                "woord ziet, mag weten dat de kern volgt.",
                "Let op hoewel: dat geeft iets toe en spreekt het dan tegen. Echter doet hetzelfde, "
                "maar begint een nieuwe zin.",
            ],
        ),
        dict(
            aanpak="Zoek bij een verwijswoord altijd wat het vervangt, en lees de zin dan opnieuw met "
                   "dat woord erin. Past er meer dan één mogelijkheid, dan is de zin dubbelzinnig.",
            waarom=[
                None,
                "Let erop dat dubbelzinnig hier het juiste antwoord is. Hij kan op beide personen "
                "wijzen, en dat is precies waarom de volgende reeks je laat herschrijven.",
                "Let erop dat dat hier naar een hele zin verwijst en niet naar één woord. Een "
                "verwijswoord kan ook een gedachte vervangen.",
                None,
            ],
        ),
        dict(
            aanpak="Bij herschrijven heb je twee oplossingen: het verwijswoord vervangen door de naam, "
                   "of de naam erachter zetten. Kies de vorm die het vlotst leest.",
            waarom=[
                "Noem ook hoe je het oplost, zoals het antwoord doet. En let erop dat beide lezingen "
                "mogelijk zijn: je kiest er één en maakt die duidelijk.",
                "Let erop dat je hier een naamwoord moet toevoegen, zoals die toestellen. Enkel een "
                "ander voornaamwoord kiezen lost de dubbelzinnigheid niet op.",
            ],
        ),
        dict(
            aanpak="Lees de twee zinnen eerst zonder het woord en zeg zelf wat het verband is. Kies dan "
                   "het woord dat precies dat verband weergeeft.",
            waarom=[
                "Let erop dat hier een gevolg staat en geen toevoeging. Bovendien zou een tweede reden "
                "aankondigen, en die staat er niet.",
                "Let op de tegenstelling: goedkoop en toch niet werkend. Dus zou een gevolg maken, en "
                "dat klopt hier niet.",
                "Let erop dat indien een voorwaarde geeft. Echter en kortom horen bij heel andere "
                "verbanden.",
                "Let erop dat bijgevolg een gevolg aankondigt, net als daarom. Daarentegen zou een "
                "tegenstelling maken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-argumentatie-feiten-en-meningen-en-drogredenen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: kan je het nagaan? Een feit kan je controleren, een mening is een "
                   "waardering en verschilt van persoon tot persoon.",
            waarom=[
                "Let op het verschil tussen de eerste en de tweede: hoe vaak de bus rijdt, is te "
                "controleren; of dat te weinig is, is een waardering.",
                "Let op iedereen vindt dat: dat lijkt een feit maar is een mening, en meestal niet "
                "eens waar. Wie iedereen zegt, bedoelt zichzelf en zijn vrienden.",
            ],
        ),
        dict(
            aanpak="Leer de vier bij hun kern: de man in plaats van zijn argument, veel mensen in "
                   "plaats van een reden, een reeks rampen zonder bewijs, en een argument dat zijn "
                   "eigen stelling herhaalt.",
            waarom=[
                "Let erop dat je geen auto hebben niets zegt over je argument. Dat is wat een "
                "persoonlijke aanval doet: de persoon raken in plaats van de redenering.",
                None,
                "Let op de reeks gevolgen zonder bewijs: dat is het hellend vlak. Elke stap wordt "
                "voorgesteld als onvermijdelijk, en dat is net wat niet aangetoond is.",
                "Let erop dat het argument hier niets toevoegt: het herhaalt de stelling in andere "
                "woorden. Daarom heet het een cirkel.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Drie open vragen over hoe sterk een argument is. Antwoord in volle zinnen en noem "
                   "het soort argument met zijn naam.",
            waarom=[
                "Noem beide delen: dat het een vergelijking is, en de voorwaarde waarop ze staat of "
                "valt. Die voorwaarde is de gelijkenis tussen de twee gevallen.",
                "Noem waarom het je betoog sterker maakt en niet zwakker. Een lezer die zijn bezwaar "
                "ziet staan, voelt zich ernstig genomen.",
                "Let op het verschil tussen het argument en de stelling: enkel het argument sneuvelt. "
                "Dat is de kern van deze vraag.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een drogreden wel kan, wanneer iets een "
                   "feit is, en wat een betoog nodig heeft.",
            waarom=[
                None,
                "Niet waar: een cijfer kan verzonnen of verkeerd zijn, en in een mening gebruikt "
                "worden. Veel te duur voor 40 euro heeft een cijfer en blijft een mening.",
                None,
                "Niet waar: een betoog bestaat net uit een standpunt met argumenten eronder. Zonder "
                "argumenten heb je enkel een mening.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-lees-en-luisterstrategieen-en-notities-nemen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Je leesdoel kiest je strategie: wil je weten waarover het gaat (skimmen), zoek je "
                   "één gegeven (scannen), of moet je het echt kennen (intensief)?",
            waarom=[
                "Let op het verschil tussen skimmen en scannen: bij het eerste neem je de hele tekst "
                "vluchtig door, bij het tweede zoek je naar één bepaald gegeven en lees je de rest niet.",
                None,
            ],
        ),
        dict(
            aanpak="Houd drie dingen over: waarover het gaat, wat erover gezegd wordt, en wat je nodig "
                   "hebt om het later te begrijpen. Lidwoorden, voegwoorden en bijzaken mogen weg.",
            waarom=[
                None,
                "Let erop dat de reden in je notitie blijft staan. Enkel uitstap afgelast verliest "
                "waarom het afgelast is, en dat is net wat je morgen niet meer weet.",
                "Let erop dat volgens de spreker erbij blijft. Dat het de tweede oorzaak is, is een "
                "feit; dat ze de belangrijkste is, is zijn mening.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat je al kan zonder de tekst (voor), wat de tekst zelf nodig heeft "
                   "(tijdens) en wat je pas achteraf kan nagaan (na).",
            waarom=[
                None,
                "Let op het verschil tussen de eerste en de derde: je samenvatting vergelijken kan "
                "pas als er een samenvatting is, dus na.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over je eigen werkwijze. Antwoord in volle zinnen en noem telkens "
                   "wat je concreet doet.",
            waarom=[
                "Noem de reden en wat je met die ruimte doet. Dat je niet kan terugspoelen, is het "
                "verschil met een leestekst.",
                "Let erop dat de orde telt: eerst zelf opnieuw lezen, dan pas opzoeken of vragen. En "
                "noem ook wat je niet doet.",
                "Noem de proef die je doet: navertellen in eigen woorden, zonder de tekst. Een tekst "
                "herlezen voelt als begrijpen en is het niet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-multimediale-elementen-en-non-verbale-communicatie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk element af of het je iets laat zien, je de weg wijst, of je iets "
                   "laat voelen. Die derde groep stuurt je oordeel.",
            waarom=[
                "Let op het verschil tussen de eerste en de tweede: een foto werkt op je gevoel, een "
                "grafiek op je verstand. Allebei overtuigen, maar langs een andere weg.",
                "Let op de muziek: er wordt niets gezegd en toch weet je al wat je moet denken. Dat "
                "is net waarom muziek onder een reportage niet onschuldig is.",
            ],
        ),
        dict(
            aanpak="Vraag je af met welk deel van jezelf je het signaal geeft: je gezicht, je lichaam, "
                   "je ogen, je stem, je handen, de ruimte, of de stilte.",
            waarom=[
                None,
                "Let op de stilte: niets zeggen is ook een signaal. Een pauze voor je kernpunt maakt "
                "dat punt zwaarder.",
                "Let op het derde geval: je woorden en je lichaam zeggen iets anders. Bij zo'n "
                "tegenstelling gelooft je gesprekspartner bijna altijd het lichaam.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: dat beeld kan misleiden zonder te liegen, dat "
                   "non-verbale taal niet overal hetzelfde betekent, en wat stem en onderschrift doen.",
            waarom=[
                None,
                "Niet waar: hoeveel afstand hoort, of je iemand in de ogen kijkt, zelfs een duim "
                "omhoog verschilt per cultuur. Daarom lees je zo'n signaal met voorzichtigheid.",
                None,
                "Niet waar: wie altijd op dezelfde toon spreekt, verliest zijn publiek, ook met een "
                "goede inhoud. Variatie in je stem houdt de aandacht vast.",
                None,
            ],
        ),
        dict(
            aanpak="Drie open vragen over beeld, stem en de verhouding tussen de twee. Antwoord in "
                   "volle zinnen.",
            waarom=[
                "Noem beide delen: wat het effect is en waar je het ziet. Dat de zij-as je dat "
                "verklapt, is het praktische deel van je antwoord.",
                "Noem beide verliezen: de feedback en de indruk die je maakt. Dat je niet ziet of ze "
                "volgen, is het grootste.",
                "Let erop dat je ja antwoordt met een voorwaarde erbij. Een contrast werkt, maar enkel "
                "als het gewild is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verhaallijn-personages-en-vertelperspectief-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist bijna alles: wie weet hier wat? Weet de verteller meer dan één "
                   "personage kan weten, dan is hij alwetend.",
            waarom=[
                "Let erop dat de ik hier juist niet weet wat de ander denkt. Dat is het teken van een "
                "ik-perspectief: één hoofd van binnenuit, de rest van buitenaf.",
                "Let erop dat de verteller in twee hoofden kijkt binnen dezelfde zin. Daarom is hij "
                "alwetend en niet gebonden aan één personage.",
                None,
                "Let op het verschil met de alwetende verteller: hier krijgt elk personage zijn eigen "
                "hoofdstuk, en de verteller blijft telkens in dat ene hoofd.",
                "Let erop dat het bedrog later uitkomt: dat is wat een verteller onbetrouwbaar maakt. "
                "Het is een gewilde techniek, geen fout van de schrijver.",
            ],
        ),
        dict(
            aanpak="Eén vraag: verandert dit personage, of blijft het hetzelfde? Verandering of twijfel "
                   "maakt het rond, altijd dezelfde reactie maakt het vlak.",
            waarom=[
                None,
                "Let op het keerpunt: eerst meedoen, dan weigeren. Die ommekeer is precies wat een "
                "rond personage onderscheidt.",
                None,
                "Let erop dat één toegeven al genoeg is. Een personage moet niet van kop tot staart "
                "veranderen om rond te zijn.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over de orde van het verhaal en over de verteller. Noem de "
                   "begrippen met hun naam.",
            waarom=[
                "Noem beide delen: hoe de techniek heet en wat ze oplevert. Dat de vraag van wat naar "
                "waarom verschuift, is de winst.",
                "Noem allebei met hun eigen woorden: de orde waarin het gebeurde en de orde waarin je "
                "het leest. Een flashback laat die twee uiteenlopen.",
                "Noem drie redenen zoals het antwoord doet: vergissen, verzwijgen, zich beter "
                "voordoen. En noem dat het ook een techniek kan zijn.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: of een perspectief kan wisselen, wie de ik is, "
                   "en wat een alwetende verteller kan.",
            waarom=[
                None,
                "Niet waar: de ik is een personage dat de schrijver bedacht heeft. Soms lijkt hij op "
                "zijn maker, maar dat mag je nooit veronderstellen.",
                None,
                "Niet waar: dat is net wat alwetend betekent. Hij kan in elk hoofd kijken, en vaak in "
                "meerdere hoofden na elkaar.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tijd-ruimte-thema-en-spanningsopbouw-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vergelijk de tijd in het verhaal met de ruimte op papier: veel tijd in weinig "
                   "regels is een sprong, weinig tijd in veel regels is vertraging.",
            waarom=[
                "Let erop dat de eerste en de derde allebei een sprong zijn, ook al staat het er "
                "anders: drie jaar later en in twee regels slaan allebei tijd over.",
                "Let op de derde: ze duwt staat in de tegenwoordige tijd, en dat haalt het verhaal "
                "dichterbij. Het is geen sprong en geen vertraging maar een keuze van werkwoordstijd.",
            ],
        ),
        dict(
            aanpak="Zoek in de beschrijving het detail dat de sfeer maakt: het licht, de temperatuur, "
                   "de geur, of hoe de dingen vastzitten. Noem dat detail in je antwoord.",
            waarom=[
                None,
                "Let op de ene werkende lamp: juist dat ene licht maakt het dreigend. Een volledig "
                "verlichte parking zou gewoon leeg zijn.",
                "Let op vastgeschroefd: meubels die niemand kan verzetten, zeggen dat je hier niets "
                "te zeggen hebt. Dat maakt de ruimte onpersoonlijk.",
            ],
        ),
        dict(
            aanpak="Het onderwerp kan je aanwijzen (waarover gaat het?), het thema moet je formuleren "
                   "(wat zegt het boek daarover?). Een thema is bijna altijd een begrip, geen ding.",
            waarom=[
                "Let op het verschil tussen de eerste en de tweede: een verhuizing is wat er gebeurt, "
                "afscheid nemen is waarover het gaat. Hetzelfde boek heeft beide.",
                "Let op de tweede: opgroeien in twee culturen is geen gebeurtenis maar een spanning "
                "die het hele boek door loopt. Daarom is het een thema.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over spanning. Antwoord in volle zinnen en noem de middelen met "
                   "hun naam.",
            waarom=[
                "Noem er drie met telkens hun werking erbij, zoals het antwoord doet. Verzwijgen, "
                "dreiging en tijdsdruk zijn de duidelijkste.",
                "Noem beide delen: wat een cliffhanger is en waarom hij daar staat. Dat de lezer daar "
                "normaal zou stoppen, is de reden.",
                "Let erop dat je ja antwoordt en uitlegt waar de spanning dan zit: niet in wat, maar "
                "in hoe. Dat de lezer meer weet dan het personage, is een eigen soort spanning.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-genres-fictie-en-non-fictie-en-je-eigen-leeservaring-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Let bij verhalend werk op de lengte en het aantal verhaallijnen, en bij de rest op "
                   "de vorm: beeld, dialoog, regelval.",
            waarom=[
                "Let op de orde van lang naar kort: roman, novelle, kortverhaal. Dat een kortverhaal "
                "om één moment draait, is het duidelijkste kenmerk.",
                "Let op het verschil tussen de strip en de graphic novel: de middelen zijn dezelfde, "
                "de lengte en het publiek niet.",
                None,
            ],
        ),
        dict(
            aanpak="Eén vraag: zijn de gesprekken en de gebeurtenissen bedacht? Bedachte scènes maken "
                   "het fictie, ook als het decor echt is.",
            waarom=[
                "Let erop dat een echte oorlog het niet non-fictie maakt. Zodra de gesprekken bedacht "
                "zijn, is het fictie met een echt decor.",
                "Let erop dat ook een echte persoon in fictie kan belanden. Wat hij in het boek zegt, "
                "heeft hij nooit gezegd.",
                None,
                "Let erop dat de vorm niets beslist: een graphic novel met echte getuigenissen is "
                "non-fictie. Beeldtaal is geen bewijs van fictie.",
            ],
        ),
        dict(
            aanpak="Een oordeel zonder reden kan niemand iets mee doen. Zeg dus wat je vond, en "
                   "waaraan je dat merkte: de opbouw, het perspectief, de taal, het genre.",
            waarom=[
                "Noem het begrip erbij, zoals de opdracht vraagt. En weet dat stoppen een geldig "
                "oordeel is zolang je het verantwoordt.",
                "Let op het verschil tussen graag lezen en goed vinden: het eerste is smaak, het "
                "tweede gaat over hoe het boek gemaakt is.",
                "Noem waar dat verschil vandaan komt: uit de lezer. Daarom hoort er bij elk oordeel "
                "een reden, anders kan de ander er niets mee.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: of genres kunnen overlappen, wat echte feiten "
                   "wel en niet beslissen, en wat poëzie nodig heeft.",
            waarom=[
                None,
                "Niet waar: zodra er bedacht is wat er gezegd of gedacht werd, is het fictie. Echte "
                "feiten als vertrekpunt veranderen dat niet.",
                "Niet waar: de meeste moderne gedichten rijmen niet. Ritme, regelval en beeldtaal "
                "maken een gedicht, rijm is een mogelijkheid.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-taalvarieteiten-registers-en-beleefdheid-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af wie zo spreekt: iedereen in het hele taalgebied (standaardtaal), een "
                   "streek (dialect), een vak (jargon), een leeftijdsgroep (groepstaal), of niemand "
                   "helemaal consequent (tussentaal).",
            waarom=[
                "Let op de tweede: ge en is zijn geen dialect en geen standaardtaal, maar iets "
                "ertussen. Dat is precies wat tussentaal is.",
                "Let op de derde: een notarisakte is extreem formeel en toch standaardtaal. Formeel en "
                "standaardtaal zijn twee verschillende dingen.",
            ],
        ),
        dict(
            aanpak="Bij formeel maken verander je drie dingen: het voornaamwoord (u), de woorden "
                   "(voluit en precies) en de vorm van je vraag. Bij informeel maken doe je het omgekeerde.",
            waarom=[
                "Noem ook wat je verandert, zoals het antwoord doet. En let op dat ding: een formele "
                "zin noemt waarover het gaat.",
                "Let op ff en gaan bekijken: een afkorting en een vulwerkwoord horen niet in een "
                "formele zin. We bekijken is korter en formeler tegelijk.",
                "Let erop dat gelieve te een ouderwetse vorm is die je in een appje nooit gebruikt. "
                "Laat weten zegt hetzelfde met een gewoon werkwoord.",
            ],
        ),
        dict(
            aanpak="U zet afstand, je zet nabijheid. Bij twijfel kies je u, behalve als de ander zelf "
                   "jij zegt: dan volg je hem.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat je de ander volgt: als hij jij zegt, is u blijven zeggen afstandelijk. "
                "Daarom is dit het enige geval van de vier met je.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over hoe je je taal aanpast. Antwoord in volle zinnen en noem "
                   "telkens het verschil tussen goed en passend.",
            waarom=[
                "Let op het onderscheid dat het antwoord maakt: bereik tegenover kwaliteit. Dat een "
                "dialect eigen regels heeft, hoort erbij.",
                "Noem de reden: je register moet bij je situatie passen. Te formeel klinkt afstandelijk "
                "of spottend, en dat is even hinderlijk als te familiair.",
                "Noem beide delen: gewone woorden en de vakterm erbij. Waarom die vakterm nuttig "
                "blijft, staat in het antwoord: de patiënt vindt hem terug in een verslag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-taal-en-identiteit-stereotypering-inclusie-en-exclusie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk naar het bereik van de zin: zegt hij iets over allemaal, of is hij afgebakend? "
                   "En kijk wie er binnen en wie erbuiten valt.",
            waarom=[
                "Let erop dat er geen enkele afbakening in staat: niet welke jongeren, niet waar, niet "
                "vergeleken met wat. Daarom is het een veralgemening.",
                "Let op het verschil met de eerste: hier wordt een eigenschap aan een groep gekoppeld, "
                "en dat is wat een stereotype doet.",
                "Let erop dat deze zin juist is afgebakend: veel, in dit onderzoek, minder dan vroeger. "
                "Daarom valt ze onder geen van de twee.",
                "Let erop dat jong hier niets met het werk te maken heeft. Een eis die niemand nodig "
                "heeft maar wel mensen weghoudt, sluit uit.",
                "Let erop dat de gewone Vlaming een norm stelt: wie er niet aan beantwoordt, is "
                "blijkbaar ongewoon. Dat sluit uit zonder iemand te noemen.",
                None,
            ],
        ),
        dict(
            aanpak="Zoek het woord dat een deel van je lezers weglaat, en vervang het door een vorm die "
                   "niemand buitensluit. Het meervoud is daarvoor je beste middel.",
            waarom=[
                "Let erop dat je enkel de aanspreking verandert. De rest van de zin was al in orde.",
                "Let erop dat het meervoud alle leerlingen brengen hun boek mee de kortste oplossing "
                "is. Zijn of haar werkt ook maar leest zwaarder.",
                "Let erop dat je niet verzwijgt dat het op de eerste verdieping is, maar erbij zet hoe "
                "iedereen er komt. Informatie toevoegen is beter dan iets weglaten.",
            ],
        ),
        dict(
            aanpak="Elk paar noemt dezelfde eigenschap, één keer welwillend en één keer afkeurend. Dat "
                   "verschil zit niet in het feit maar in het woord.",
            waarom=[
                "Let erop dat zuinig en gierig hetzelfde gedrag beschrijven. Enkel het oordeel van de "
                "spreker verschilt, en dat heet gevoelswaarde.",
                "Let op het derde paar: eigenzinnig klinkt als een eigen koers, dwars als tegenwerken. "
                "Hetzelfde gedrag, een ander oordeel.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over het verschil tussen je bedoeling en je effect. Antwoord in "
                   "volle zinnen.",
            waarom=[
                "Noem beide delen: dat het effect niet van je bedoeling afhangt, en wat je dan wel "
                "doet. Een ander woord kiezen is het antwoord.",
                "Noem waarom het blijft hangen: de lezer legt zelf het verband. Dat je ook "
                "verantwoordelijk bent voor wat je niet bedoelde, is de kern.",
                "Noem één reden met een voorbeeld erbij: je streek, je groep of je vak klinkt mee in "
                "hoe je spreekt. Daarom raakt kritiek op iemands taal hem persoonlijk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-klanken-spelling-diakritische-tekens-en-interpunctie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vul in deze orde in: welke tijd, welke persoon, en pas dan de vorm. Twijfel je "
                   "tussen d en dt, vervang het werkwoord door lopen: hij loopt, dus stam plus t.",
            waarom=[
                "Let erop dat de stam van antwoorden al op een d eindigt, dus komt er in de derde "
                "persoon nog een t bij: antwoordt. Bij ik blijft het antwoord.",
                "Let op het tweede: wil en wilt zijn na jij allebei correct, en dat is een van de "
                "weinige keuzes die het Nederlands toelaat.",
                "Let op het tweede: in een vraag staat jij achter het werkwoord en valt de t weg, dus "
                "word jij. In hij wordt blijft ze staan.",
            ],
        ),
        dict(
            aanpak="Zet tussen de twee delen een n als het eerste deel in je hoofd enkel een meervoud "
                   "op -en heeft (pannen, boeken). Hoor je geen meervoud, dan komt er geen n.",
            waarom=[
                "Let op zonnebloem: zon heeft wel een meervoud op -en, maar er is er maar één, en "
                "daarom komt er geen tussen-n. Hetzelfde geldt voor zonneschijn en maneschijn.",
                "Let op koningshuis: hier staat een s en geen n. Je hoort die s, en dat is precies de "
                "regel voor de tussen-s.",
            ],
        ),
        dict(
            aanpak="Elk teken heeft zijn eigen taak: het trema splitst twee klinkers, het accent aigu "
                   "komt uit het Frans mee, en het accent grave onderscheidt twee woorden.",
            waarom=[
                "Let op het derde: de appel die je eet heeft geen teken. Enkel appèl, een oproep of een "
                "samenkomst, krijgt er een, en net daarom staat het teken er.",
            ],
        ),
        dict(
            aanpak="Zoek eerst waar de zin uit elkaar valt, en zet daar je teken. Een bijzin vooraan "
                   "krijgt een komma erachter, bijgevoegde informatie krijgt er twee.",
            waarom=[
                None,
                "Let erop dat er geen komma voor en staat in een opsomming. De dubbelpunt kondigt de "
                "opsomming aan.",
                "Let erop dat de twee komma's hier de betekenis bepalen: met komma's heb je één broer, "
                "zonder komma's heb je er meerdere en woont deze in Gent.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de t bij jij in een vraag, wat de tekens doen, "
                   "en of de tussen-n een vaste regel is.",
            waarom=[
                None,
                "Niet waar: een trema splitst twee klinkers die je anders samen zou lezen, een accent "
                "aigu komt vaak uit het Frans mee of legt de klemtoon. Twee verschillende taken.",
                None,
                "Niet waar: zonnebloem en zonneschijn hebben er geen, want er is maar één zon. De "
                "regel heeft uitzonderingen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordsoorten-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk niet naar het woord maar naar wat het doet: iets noemen, iets zeggen over een "
                   "naamwoord, iets zeggen over een werkwoord, of twee delen verbinden.",
            waarom=[
                "Let op het verschil tussen de eerste twee: onder zegt waar iets staat ten opzichte "
                "van iets anders en krijgt een naamwoord achter zich; snel zegt hoe hij liep.",
                None,
                "Let op er in de eerste zin: het wijst niet naar iets aanwijsbaars maar vult de plaats "
                "vooraan op. Daarom heet het een bijwoord en geen voornaamwoord.",
            ],
        ),
        dict(
            aanpak="Eén vraag: waar hoort het woord bij? Hoort het bij een naamwoord, dan is het "
                   "bijvoeglijk; hoort het bij het werkwoord, dan is het een bijwoord.",
            waarom=[
                None,
                "Let erop dat het woord zelf niet verandert in snel rijden, maar zijn rol wel. Alleen "
                "de plaats in de zin verklapt het.",
                None,
                "Let erop dat mooi hier geen uitgang heeft en toch van soort verandert. Vergelijk met "
                "een mooi verhaal: daar hoort het bij verhaal, hier bij schrijft.",
            ],
        ),
        dict(
            aanpak="Zoek niet het eerste woord dat erop lijkt, maar pas de proef toe: een voorzetsel "
                   "kan je vervangen door naast of boven, een voegwoord verbindt twee delen.",
            waarom=[
                None,
                "Let op onderschikkend: omdat maakt van de tweede helft een bijzin, en dat merk je aan "
                "de persoonsvorm die naar achteren schuift. Want zou nevenschikkend zijn.",
                "Let op onbepaald: een auto is nog geen bepaalde auto, de straat wel. Daarom is een "
                "het antwoord en niet de.",
                "Let erop dat zich bij het werkwoord hoort en naar het onderwerp terugwijst. Dat is "
                "precies wat wederkerend betekent.",
            ],
        ),
        dict(
            aanpak="Twee open vragen over hoe je een woordsoort vindt. Antwoord in volle zinnen en geef "
                   "telkens een voorbeeld.",
            waarom=[
                "Noem een voorbeeld met twee zinnen erbij, zoals het antwoord doet. Dat de functie "
                "beslist en niet het woord, is de kern.",
                "Noem de proef met een voorbeeld: kan naast of boven er staan, dan is het een "
                "voorzetsel. Vervangen is sneller dan een rijtje opzeggen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af of elk deel ook alleen kan staan. Twee hele woorden geven een "
                   "samenstelling; een stuk dat niet alleen kan staan is een voor- of achtervoegsel, "
                   "en dan heb je een afleiding.",
            waarom=[
                "Let op het verschil tussen de eerste en de tweede: tafel en poot bestaan apart, on- "
                "bestaat niet apart. Daarom is het ene een samenstelling en het andere een afleiding.",
                "Let op spoorwegovergang: drie delen die elk alleen kunnen staan, dus nog altijd een "
                "samenstelling. Lengte maakt er geen afleiding van.",
            ],
        ),
        dict(
            aanpak="Haal -en van de infinitief af, en kijk dan of je een dubbele letter moet "
                   "wegstrepen: zetten geeft zet, rijden geeft rijd.",
            waarom=[
                "Let op antwoorden: de stam eindigt al op een d, en dat is net waarom hij antwoordt "
                "zo lastig is om te spellen.",
                "Let op zetten en rijden: de dubbele t valt weg, en de d van rijden blijft staan ook "
                "al hoor je hem als een t.",
            ],
        ),
        dict(
            aanpak="Kijk eerst of er een hulpwerkwoord staat. Hebben of zijn plus een deelwoord maakt "
                   "het voltooid, zullen of gaan maakt het toekomend, en de rest lees je af van het "
                   "werkwoord zelf.",
            waarom=[
                None,
                "Let op de eerste: had gewerkt staat in de voltooid verleden tijd, want het gebeurde "
                "al voor een ander moment in het verleden. Vergelijk met heeft gewerkt.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over hoe woorden gemaakt zijn. Antwoord in volle zinnen en geef "
                   "telkens de voorbeelden erbij.",
            waarom=[
                "Noem beide delen: wat de stam is en waarom hij niet gelijk is aan de infinitief. Dat "
                "je met de stam spelt, is het nut ervan.",
                "Noem er vier, twee van elk, met telkens wat het voegsel doet. Het antwoord geeft de "
                "duidelijkste.",
                "Noem het verschil in de klinker, met een voorbeeld van elk. Dat zwakke werkwoorden "
                "enkel een uitgang krijgen, is de andere helft.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsontleding-en-zinsbouw-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek altijd eerst de persoonsvorm: dat is het werkwoord dat van vorm verandert als "
                   "je de zin in een andere tijd zet. Vraag dan wie of wat die handeling doet.",
            waarom=[
                "Let op de tweede zin: er is niet het onderwerp. Drie fietsen stonden, dus drie "
                "fietsen is het onderwerp, ook al staat het niet vooraan.",
            ],
        ),
        dict(
            aanpak="Vraag het in deze orde: wie of wat plus de persoonsvorm geeft het onderwerp, dan "
                   "wie of wat plus het onderwerp geeft het lijdend voorwerp, en aan wie geeft het "
                   "meewerkend voorwerp.",
            waarom=[
                "Let erop dat de eerste twee dezelfde zin zijn met een ander vetgedrukt deel. Haar "
                "broer is aan wie, het boek is wat ze gaf.",
                "Let op de derde: de man met de hoed is één zinsdeel, ook al bestaat het uit vijf "
                "woorden. Een zinsdeel kan je in zijn geheel vooraan of achteraan zetten.",
            ],
        ),
        dict(
            aanpak="Tel de persoonsvormen: zoveel zinnen heb je. Begint een zin met omdat, toen, dat of "
                   "een ander onderschikkend voegwoord, dan is het een bijzin.",
            waarom=[
                None,
                "Let op en: dat verbindt twee gelijkwaardige zinnen, dus twee hoofdzinnen. Vergelijk "
                "met omdat in de vorige.",
                "Let erop dat je drie persoonsvormen vindt: begon, liepen en hadden. Toen maakt de "
                "eerste een bijzin, want laat de derde een hoofdzin.",
            ],
        ),
        dict(
            aanpak="Zoek wat je kan weglaten: door het feit dat, er is sprake van, en naamwoorden waar "
                   "een werkwoord kan staan. Zet daarna je persoonsvorm dicht bij je onderwerp.",
            waarom=[
                "Noem ook wat je weglaat, zoals het antwoord doet. Vertraging in plaats van er was "
                "sprake van een vertraging is de hele winst.",
                "Let erop dat er twee bijzinnen in elkaar zaten. Door er één van te maken, komt de "
                "persoonsvorm was weer dicht bij brief te staan.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoeveel persoonsvormen een zin kan hebben, "
                   "welke zinsdelen moeten en welke niet, en waar ze staan.",
            waarom=[
                None,
                "Niet waar: hij slaapt heeft er geen, en bij een naamwoordelijk gezegde zoals hij is "
                "leraar kan er nooit een staan.",
                None,
                "Niet waar: in morgen komt de loodgieter langs staat het achter de persoonsvorm, en in "
                "een vraag ook. De plaats verklapt het onderwerp niet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-semantiek-betekenisrelaties-gevoelswaarde-en-humor-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af of het ene woord onder het andere valt (hyperoniem), of ze hetzelfde "
                   "zeggen (synoniem), het tegengestelde (antoniem), of enkel dezelfde vorm hebben "
                   "zonder verband (homoniem).",
            waarom=[
                "Let op de eerste: fiets valt onder vervoermiddel, dus is vervoermiddel het ruimere "
                "woord. Het ruimere woord is het hyperoniem.",
                "Let op de derde: roos en bloem lijken op de twee gevallen ervoor maar zijn het niet. "
                "Hier hoort het ene onder het andere, dus is het een hyperoniem.",
            ],
        ),
        dict(
            aanpak="Een uitdrukking betekent iets anders dan wat er staat, dus zoek niet de losse "
                   "woorden op. Vervang de hele uitdrukking door één gewoon woord.",
            waarom=[
                "Let op boter op het hoofd hebben: je kan er niets van de losse woorden afleiden. "
                "Zulke uitdrukkingen moet je kennen, raden lukt zelden.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af waar de grap op draait: op een woord met twee betekenissen, op het "
                   "omgekeerde zeggen van wat je bedoelt, op maat, of op een wending die je niet zag "
                   "komen.",
            waarom=[
                None,
                "Let erop dat de zin zichzelf tegenspreekt: duizend keer is zelf een overdrijving. "
                "Daar zit de grap in.",
                "Let op bank: het woord betekent hier twee dingen tegelijk, en dat is wat een "
                "woordspel op een homoniem doet.",
                "Let erop dat de eerste helft je iets anders laat verwachten dan de tweede. Die "
                "breuk is de hele grap.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over betekenis en toon. Antwoord in volle zinnen en geef telkens "
                   "een voorbeeld.",
            waarom=[
                "Noem het begrip erbij: synoniemen delen hun betekenis, niet hun gevoelswaarde. Een "
                "voorbeeld met twee situaties maakt het duidelijk.",
                "Noem waarom het misgaat: je toon ontbreekt. En noem dat een signaal nodig is, want "
                "zonder dat leest de ander je letterlijk.",
                "Noem het onderscheid met een voorbeeld van elk, zoals het antwoord doet. Bij "
                "homoniemen is er geen verband, bij één woord met meerdere betekenissen wel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-en-schriftelijke-interactie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af waar je aan werkt: aan je plan, aan je tekst, aan de opbouw van je "
                   "tekst, of aan de taal erin. Dat laatste is nalezen.",
            waarom=[
                None,
                "Let op het verschil tussen de tweede en de derde: een alinea schrappen is herwerken, "
                "want je verandert de opbouw. Luidop lezen om een zin te horen, is nalezen.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat je ontvanger met de tekst moet kunnen doen: terugvinden, geloven, "
                   "uitvoeren, oplossen of je aannemen. Dat doel kiest je tekstvorm.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat een klacht leeft van gegevens: wat, wanneer, welk bedrag, welk "
                "ordernummer. Zonder die gegevens kan de ander niets nagaan.",
                None,
            ],
        ),
        dict(
            aanpak="Twee dingen tegelijk: breng de taal naar het juiste register, en zet erin wat de "
                   "ontvanger nodig heeft om iets te doen.",
            waarom=[
                "Let op de verschuiving: niet wat jij wil, maar wat jij voor hen kan doen. Dat is wat "
                "een sollicitatiebrief van een gewone mail onderscheidt.",
                "Let erop dat je een feit en een vraag geeft. Een verwijt geeft de ander niets om op "
                "te antwoorden; een duidelijke vraag wel.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over je werkwijze. Antwoord in volle zinnen en noem telkens de "
                   "reden erbij.",
            waarom=[
                "Noem het verschil tussen wat je bedoelde en wat er staat. Dat je hoofd de bedoeling "
                "meeleest, is waarom je eigen fouten onzichtbaar zijn.",
                "Noem beide delen en de orde: eerst de opbouw, dan de taal. Dat je een geschrapte "
                "alinea niet hoeft te spellen, is het argument.",
                "Noem er twee, zoals het antwoord doet: je doel en je publiek. En zeg wat ervan "
                "afhangt, want daarom leg je ze vooraf vast.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-spreken-en-gesprekken-voeren-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén proef: kan de ander met ja of nee antwoorden? Dan is de vraag gesloten. Vragen "
                   "met hoe, wat of waarom zijn open.",
            waarom=[
                None,
                "Let op de derde: spreken we af om tien uur is gesloten en dat is hier net de "
                "bedoeling. Een gesloten vraag legt iets vast, en dat is geen tekort.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat je met je zet bereikt: de ander laten spreken, nagaan of je hem "
                   "goed begreep, laten merken dat je luistert, of iets vastleggen.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: samenvatten zegt wat je begreep, "
                "navragen stelt er een vraag van. Het tweede laat de ander je verbeteren.",
                "Let op de tweede: beginnen bij waar je het wel over eens bent, haalt de spanning uit "
                "een moeilijk gesprek. Daarna pas het punt waar jullie verschillen.",
            ],
        ),
        dict(
            aanpak="Twee dingen tegelijk: zeg wat je vindt met een reden erbij, en raak het plan en "
                   "niet de persoon.",
            waarom=[
                "Let erop dat je antwoord een reden bevat. Dat is stom is geen argument, en de ander "
                "kan er niets mee.",
                "Let erop dat je met iets concreets begint en je opbouw aankondigt. Euh, ik ga iets "
                "zeggen verliest je publiek in de eerste seconde.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over spreken en luisteren. Antwoord in volle zinnen en noem "
                   "telkens wat je concreet doet.",
            waarom=[
                "Noem beide verliezen van voorlezen: je oogcontact en je mogelijkheid om bij te "
                "sturen. Spreken in plaats van lezen is de winst.",
                "Noem wat je doet en waarom: een gesprek bestaat uit beurten. En let erop dat ook "
                "altijd wachten het gesprek verstoort.",
                "Noem de proef die je doet: laten terugzeggen. En noem waarom is het duidelijk niets "
                "oplevert, want bijna iedereen zegt daarop ja.",
            ],
        ),
    ],
)

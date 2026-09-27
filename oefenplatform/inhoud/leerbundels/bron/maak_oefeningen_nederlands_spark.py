# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Nederlands ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Dezelfde pdf gaat dus bij allebei.
De twee hoofdstukken begrijpend lezen staan wél los van elkaar en krijgen elk
hun eigen bundel.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Wie hier iets bijschrijft, legt het eerst naast
`../../spark/nederlands.json` en `../../spark/nederlands-begrijpend-lezen.json`.

Bij een taalvak staat het invulvakje breder: "bijwoordelijke bepaling" past
niet in een vakje dat voor een getal van twee cijfers gemaakt is.

Een leesvraag hoort op een echte tekst te staan en niet op het begrip alleen.
De twee leesbundels dragen daarom hun eigen tekst mee, een andere dan die op
het scherm, met vragen die alleen daarover gaan.
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
    "Antwoord bij een open vraag in een volledige zin.",
    "Sta je vast bij een woord? Lees de zin ervoor en erna nog eens; vaak staat de betekenis daar.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-onderwerp-hoofdgedachte-en-hoofdpunten-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Onderwerp, hoofdgedachte en hoofdpunten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Onderwerp of hoofdgedachte",
             opdracht="Een onderwerp is een woordgroep, een hoofdgedachte is een volledige zin.",
             oefeningen=[
                 ("rij", [("Zwerfvuil langs fietspaden", "onderwerp"),
                          ("Scholen moeten later beginnen, want tieners slapen te weinig.",
                           "hoofdgedachte"),
                          ("De opwarming van de zeeën", "onderwerp"),
                          ("Een huisdier maakt kinderen verantwoordelijker.", "hoofdgedachte")],
                  "Onderwerp of hoofdgedachte?", WW),
                 ("open", "Leg in je eigen woorden uit wat het verschil is tussen het onderwerp "
                          "en de hoofdgedachte van een tekst.",
                  "Het onderwerp is waarover de tekst gaat, in één of enkele woorden. De "
                  "hoofdgedachte is wat de tekst daarover zegt, in een volledige zin.", 4),
                 ("waar", "Het onderwerp van een tekst schrijf je altijd op in een volledige "
                          "zin.", False),
             ]),

        dict(kop="Werken met een korte tekst",
             opdracht="Lees het tekstje hieronder en beantwoord de vragen eronder.",
             oefeningen=[
                 ("tekst",
                  "<p><b>Steeds meer scholen schaffen de papieren agenda af.</b> De afspraken "
                  "staan dan in een app op de gsm. Leerkrachten vinden dat handig: een wijziging "
                  "is meteen bij iedereen. Toch klagen nogal wat leerlingen dat ze net "
                  "slechter overzicht hebben. Op papier zag je een hele week in één blik, op een "
                  "scherm scrol je van dag naar dag. Bovendien duikt bij het openen van de app "
                  "meteen een melding van iets anders op. Onderzoekers raden daarom aan om de "
                  "twee te combineren: digitaal voor de wijzigingen, op papier voor het "
                  "overzicht.</p>"),
                 ("kort", "Wat is het onderwerp van deze tekst?",
                  "de digitale schoolagenda", WW),
                 ("open", "Schrijf de hoofdgedachte van deze tekst in één zin.",
                  "Een digitale agenda is handig voor wijzigingen, maar geeft minder overzicht "
                  "dan papier, dus je combineert ze het best.", 3),
                 ("open", "Noem twee hoofdpunten uit deze tekst.",
                  "Een wijziging is meteen bij iedereen; op een scherm zie je geen hele week in "
                  "één blik; de app leidt af met meldingen; onderzoekers raden een combinatie "
                  "aan.", 4),
                 ("open", "Welke zin uit de tekst is eerder een detail dan een hoofdpunt? "
                          "Schrijf ze over.",
                  "'Op papier zag je een hele week in één blik, op een scherm scrol je van dag "
                  "naar dag' is de uitleg bij een hoofdpunt, geen apart hoofdpunt.", 3),
             ]),

        dict(kop="Notities nemen",
             opdracht="Denk aan wat je achteraf nog moet kunnen gebruiken.",
             oefeningen=[
                 ("rij", [("de hele zin overschrijven", "niet doen"),
                          ("kernwoorden en cijfers noteren", "wel doen"),
                          ("pas beginnen als het filmpje gedaan is", "niet doen"),
                          ("pijltjes zetten tussen oorzaak en gevolg", "wel doen")],
                  "Wel of niet doen bij notities?", WW),
                 ("open", "Waarom noteer je tijdens het luisteren en niet pas achteraf?",
                  "Een gesproken tekst kan je niet teruglezen. Wat je niet noteert terwijl het "
                  "gezegd wordt, ben je kwijt.", 3),
                 ("kort", "Hoe heet een schema met vertakkingen vanuit één centraal woord?",
                  "een woordweb (mindmap)", W),
             ]),

        dict(kop="Onbekende woorden",
             opdracht="Eerst zelf proberen, pas dan opzoeken.",
             oefeningen=[
                 ("open", "Je komt het woord 'wateroverlast' tegen en je kent het niet. Noem "
                          "twee manieren om de betekenis af te leiden vóór je het opzoekt.",
                  "Kijk naar de delen waaruit het woord bestaat (water + overlast). Lees de zin "
                  "ervoor en erna: vaak legt de tekst het zelf uit of geeft ze een voorbeeld.", 4),
                 ("waar", "Een hoofdpunt kan je weglaten zonder dat je de hoofdgedachte nog "
                          "begrijpt.", False),
                 ("open", "Je hebt de hoofdgedachte gevonden, maar één alinea past er niet bij. "
                          "Wat doe je?",
                  "Je leest die alinea opnieuw: misschien is het een tegenargument of een "
                  "uitweiding, of misschien klopt je hoofdgedachte nog niet helemaal en moet je "
                  "ze bijstellen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-en-het-communicatiemodel-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Tekstsoorten en het communicatiemodel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort",
             opdracht="Vraag je af wat de maker met die tekst wil bereiken.",
             oefeningen=[
                 ("rij", [("een bijsluiter bij een geneesmiddel", "instructief"),
                          ("een verslag van de gemeenteraad", "informatief"),
                          ("een affiche tegen te snel rijden", "overtuigend"),
                          ("een kortverhaal in een tijdschrift", "literair"),
                          ("een dagboekfragment", "verhalend")],
                  "Welke tekstsoort is dit?", WW),
                 ("waar", "Een folder van een politieke partij is een informatieve tekst.",
                  False),
                 ("waar", "Een tekst heeft altijd precies één doel.", False),
                 ("open", "Wat is het verschil tussen een reportage en een reclamefilmpje over "
                          "hetzelfde product?",
                  "Een reportage wil informeren en toont ook nadelen; een reclamefilmpje wil "
                  "overtuigen en laat alleen de goede kanten zien. De zender is een ander: een "
                  "redactie tegenover het bedrijf zelf.", 5),
             ]),

        dict(kop="Het communicatiemodel",
             opdracht="Zender, ontvanger, boodschap, kanaal, doel en context.",
             oefeningen=[
                 ("tekst",
                  "<p><i>Gebruik voor de volgende oefening deze situatie:</i> je stuurt een mail "
                  "naar de sportclub om te vragen of je een training kan inhalen.</p>"),
                 ("rij", [("wie verstuurt", "de zender: jij"),
                          ("voor wie het bedoeld is", "de ontvanger: de sportclub"),
                          ("waarlangs het gaat", "het kanaal: de mail"),
                          ("wat je wil bereiken", "het doel: een training inhalen")],
                  "Vul aan voor de situatie hierboven.", WW),
                 ("kort", "Hoe noem je de situatie waarin je communiceert: waar je bent en wat "
                          "er net gebeurd is?", "de context", W),
                 ("open", "Je stuurt over een vertraagde bus een geërgerd bericht met emoji's "
                          "naar je beste vriendin, maar naar je leerkracht schrijf je het "
                          "anders. Leg uit welk element van het communicatiemodel dat verklaart.",
                  "De ontvanger, en daarmee ook de context. Dezelfde boodschap krijgt een andere "
                  "vorm naargelang met wie je praat en hoe formeel de situatie is.", 4),
             ]),

        dict(kop="Herkennen zonder titel",
             opdracht="Let op de aanspreking, de werkwoordsvorm en de opbouw.",
             oefeningen=[
                 ("rij", [("'Beste ouders, … Met vriendelijke groeten, de directie'",
                           "een formele brief of mail van de school"),
                          ("'Neem eerst de doos uit de verpakking. Draai daarna …'",
                           "een instructie of handleiding"),
                          ("'Ik vond het traag op gang komen, maar het einde raakte me.'",
                           "een recensie")],
                  "Welke soort tekst is dit?", WW),
                 ("open", "Waarom is het nuttig om te weten met welke tekstsoort je te maken "
                          "hebt?",
                  "Je weet dan wat je mag verwachten en hoe kritisch je moet lezen. Bij een "
                  "overtuigende tekst let je op wat er wordt weggelaten, bij een instructie "
                  "volg je de stappen in volgorde.", 4),
                 ("open", "Een bedrijf maakt een filmpje dat eruitziet als een reportage, maar "
                          "het gaat over hun eigen product. Hoe noem je dat, en waarom is het "
                          "misleidend?",
                  "Dat is sluikreclame of native advertising. Het misleidt omdat je denkt dat "
                  "je een onafhankelijk verslag ziet, terwijl de zender er belang bij heeft.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-feiten-meningen-en-betrouwbaarheid-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Feiten, meningen en betrouwbaarheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Feit of mening",
             opdracht="Een feit kan je nagaan, een mening niet.",
             oefeningen=[
                 ("rij", [("Hasselt telt meer dan 80 000 inwoners.", "feit"),
                          ("Hasselt is de gezelligste stad van Limburg.", "mening"),
                          ("Deze koptelefoon weegt 240 gram.", "feit"),
                          ("Deze koptelefoon zit veel te strak.", "mening")],
                  "Feit of mening?", WW),
                 ("open", "Waaraan herken je een mening die vermomd is als feit?",
                  "Aan woorden die een waardering geven (het beste, veel te, iedereen weet) en "
                  "aan het ontbreken van een bron of een getal dat je kan nagaan.", 4),
                 ("waar", "Een mening onderbouw je het best met andere meningen.", False),
             ]),

        dict(kop="Betrouwbaar of niet",
             opdracht="Kijk naar de auteur, de datum, de bron en het doel.",
             oefeningen=[
                 ("open", "Een bericht heeft geen auteur, staat alleen op sociale media en linkt "
                          "naar een site vol advertenties. Noem drie redenen waarom je "
                          "voorzichtig bent.",
                  "Er is geen auteur die verantwoordelijk is; geen enkel nieuwsmedium neemt het "
                  "over; en de site verdient aan kliks, dus ze heeft er belang bij dat je "
                  "doorklikt in plaats van dat het klopt.", 5),
                 ("open", "In een tekst staat: 'Uit onderzoek van de KU Leuven (2025) blijkt dat "
                          "62 % van de leerlingen te weinig slaapt.' Wat maakt dit sterker dan "
                          "'veel leerlingen slapen te weinig'?",
                  "Er staat een bron bij, een jaartal en een precies cijfer. Je kan dat "
                  "nakijken; de vage zin kan je niet controleren.", 4),
                 ("waar", "Een professioneel ogende website is daarom betrouwbaar.", False),
                 ("open", "Een tekst over elektrische steps komt van een fabrikant van steps. "
                          "Wat doe je met die informatie?",
                  "Je gooit ze niet weg, maar je leest ze kritisch: de cijfers kloppen "
                  "misschien, maar de nadelen ontbreken. Je zoekt er een onafhankelijke bron "
                  "bij.", 4),
                 ("kort", "Hoe noem je verzonnen nieuws dat zich voordoet als echt nieuws?",
                  "nepnieuws (fake news)", W),
             ]),

        dict(kop="Standpunt en argumenten",
             opdracht="Een argument zegt waaróm, niet enkel dát.",
             oefeningen=[
                 ("rij", [("Onze school moet een overdekte fietsenstalling krijgen.", "standpunt"),
                          ("Nu staan de fietsen bij regen onder water en roesten de kettingen.",
                           "argument"),
                          ("Ik vind fietsen leuk.", "geen van beide, een smaak")],
                  "Standpunt, argument of geen van beide?", WW),
                 ("open", "Bedenk twee argumenten bij het standpunt 'Onze klas verdient een "
                          "kraantjeswaterfontein'.",
                  "Bijvoorbeeld: leerlingen drinken dan minder blikjes frisdrank, wat gezonder "
                  "is; er komt minder plastic afval; en wie zijn fles vergeet, kan toch drinken "
                  "in plaats van de hele dag dorst te hebben.", 4),
                 ("waar", "Wie overtuigen wil, laat de nadelen het best helemaal weg.", False),
                 ("open", "Twee betrouwbare teksten spreken elkaar tegen. Wat doe je?",
                  "Je kijkt wie ze geschreven heeft en wanneer, of ze over precies hetzelfde "
                  "gaan, en je zoekt een derde bron. Soms hebben ze allebei gelijk over een "
                  "ander stuk van de zaak.", 4),
             ]),

        dict(kop="Stereotypering",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("kort", "Hoe noem je een vast en te algemeen beeld van een hele groep mensen?",
                  "een stereotype", W),
                 ("open", "Geef een voorbeeld van stereotypering in een tekst, en leg uit "
                          "waarom het misleidt.",
                  "Bijvoorbeeld 'jongeren hangen de hele dag aan hun scherm'. Het maakt van een "
                  "hele groep één persoon, terwijl die groep juist enorm verschilt. De lezer "
                  "denkt daarna dat het over iedereen gaat.", 5),
                 ("open", "Waarom stuur je een bericht niet door als je niet zeker weet of het "
                          "klopt?",
                  "Elke keer dat iemand het deelt, lijkt het geloofwaardiger en bereikt het meer "
                  "mensen. Een rechtzetting achteraf haalt nooit evenveel lezers als het "
                  "bericht zelf.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekststructuur-en-signaalwoorden-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Tekststructuur en signaalwoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Signaalwoorden en hun verband",
             opdracht="Schrijf het verband op, niet een voorbeeldzin.",
             oefeningen=[
                 ("rij", [("want", "reden"), ("daardoor", "gevolg"), ("hoewel", "tegenstelling"),
                          ("bijvoorbeeld", "voorbeeld"), ("kortom", "samenvatting"),
                          ("als", "voorwaarde")],
                  "Welk verband kondigt dit woord aan?", WW),
                 ("rij", [("Ik was te laat ___ de trein vertraging had.", "omdat / want"),
                          ("Het was koud. ___ trok hij zijn dikke jas aan.", "Daarom"),
                          ("Hij had hard gestudeerd. ___ haalde hij een onvoldoende.", "Toch"),
                          ("Ik neem de trein ___ ik geen rijbewijs heb.", "omdat / want")],
                  "Vul het passende signaalwoord in.", WW),
                 ("waar", "Elk signaalwoord hoort bij precies één verband.", False),
             ]),

        dict(kop="Verbanden herkennen",
             opdracht="Schrijf bij elk paar zinnen welk verband ertussen ligt.",
             oefeningen=[
                 ("rij", [("De gemeente plaatste camera's. Toch bleef het sluikstorten doorgaan.",
                           "tegenstelling"),
                          ("Er kwamen meer fietsers. Daardoor was er minder file.", "gevolg"),
                          ("Bovendien kost het minder.", "opsomming / toevoeging")],
                  "Welk verband is dit?", WW),
                 ("open", "'De leerlingen kregen hun rapport. Hun ouders moesten het "
                          "ondertekenen.' Naar wie verwijst 'hun' in de tweede zin?",
                  "Naar de leerlingen uit de eerste zin.", 2),
                 ("waar", "Als je niet vindt naar wie een verwijswoord verwijst, is de tekst op "
                          "dat punt onduidelijk.", True),
             ]),

        dict(kop="De opbouw van een tekst",
             opdracht="Inleiding, midden, slot.",
             oefeningen=[
                 ("rij", [("Kortom, de fiets wint het op korte afstand.", "slot"),
                          ("Steeds meer leerlingen komen met de fiets naar school.", "inleiding"),
                          ("Ten eerste is fietsen goedkoper dan de bus.", "midden")],
                  "Hoort deze zin in de inleiding, het midden of het slot?", WW),
                 ("open", "Je krijgt vier losse alinea's en moet er een tekst van maken. "
                          "Waaraan zie je welke alinea de inleiding is?",
                  "Die introduceert het onderwerp zonder al te antwoorden, en bevat geen "
                  "signaalwoorden die terugverwijzen (dus, daarom, kortom). Vaak stelt ze een "
                  "vraag of geeft ze een aanleiding.", 4),
                 ("waar", "In het slot van een tekst mag je nieuwe argumenten introduceren die "
                          "je nergens uitgewerkt hebt.", False),
                 ("open", "Wat is er mis met deze tekst: 'Fietsen is gezond. Mijn fiets is "
                          "blauw. In de stad staan veel auto's.'?",
                  "De zinnen hebben geen verband met elkaar: er staan geen signaalwoorden en er "
                  "is geen rode draad. Het is geen alinea maar drie losse mededelingen.", 4),
                 ("kort", "Hoe heten de kleine titels boven de delen van een tekst?",
                  "tussentitels", W),
             ]),

        dict(kop="Zelf ordenen",
             opdracht="Zet de zinnen in een logische volgorde.",
             oefeningen=[
                 ("rij", [("Kortom, later beginnen loont.", "4"),
                          ("Tieners slapen gemiddeld een uur te weinig.", "1"),
                          ("Daardoor zijn ze in het eerste lesuur minder alert.", "2"),
                          ("Scholen die later starten, zien betere resultaten.", "3")],
                  "Zet in volgorde: schrijf 1 tot 4.", WW),
                 ("open", "Je schrijft een betoog met drie argumenten. Waar zet je je sterkste "
                          "argument, en waarom?",
                  "Op het einde, vlak voor je besluit. Dat blijft het best hangen. Sommigen "
                  "zetten het eerst om meteen indruk te maken; wat je niet doet, is het "
                  "wegstoppen in het midden.", 4),
                 ("open", "Waarom let je bij een luistertekst extra op signaalwoorden?",
                  "Je kan niet terugbladeren. De signaalwoorden zijn je enige houvast om te "
                  "horen of er een reden, een tegenstelling of een besluit aankomt.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-spreken-en-gesprekken-voeren-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Schrijven, spreken en gesprekken voeren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Voor je begint",
             opdracht="Denk aan doel, publiek en opbouw.",
             oefeningen=[
                 ("kort", "Hoe heet het plan met kernwoorden dat je maakt vóór je begint te "
                          "schrijven?", "een schrijfplan", W),
                 ("rij", [("een zoekertje voor je oude gitaar", "verkopen: overtuigen"),
                          ("een mail om je in te schrijven bij een club", "iets gedaan krijgen"),
                          ("een mail aan een vriend over je weekend", "vertellen"),
                          ("een handleiding voor een gezelschapsspel", "instrueren")],
                  "Wat is je doel bij deze opdracht?", WW),
                 ("open", "Wat betekent taakvoltooiing bij een schrijfopdracht?",
                  "Dat je alles doet wat er gevraagd werd: de juiste tekstsoort, het juiste "
                  "publiek, alle gevraagde onderdelen erin, en de opgegeven lengte.", 4),
             ]),

        dict(kop="Een echte opdracht",
             opdracht="Schrijf hieronder een eerste versie. Je hoeft nog niet mooi te schrijven.",
             oefeningen=[
                 ("open", "Schrijf een zoekertje van drie of vier zinnen om je oude fiets te "
                          "verkopen. Zet er zeker in: wat het is, in welke staat, de prijs en "
                          "hoe men je bereikt.",
                  "Een goed zoekertje noemt het merk en type, de leeftijd en staat (eerlijk, ook "
                  "de krassen), de prijs, en één manier om contact op te nemen. Kort, zonder "
                  "overdrijving, met een reden waarom je ze verkoopt.", 6),
                 ("open", "Schrijf de eerste twee zinnen van een formele mail aan de gemeente "
                          "over een kapot voetpad: de aanhef en je eerste zin.",
                  "Bijvoorbeeld: 'Geachte mevrouw, geachte heer,' gevolgd door 'Met deze mail "
                  "wil ik u melden dat het voetpad in de Kerkstraat ter hoogte van nummer 14 al "
                  "enkele weken opengebroken ligt.' Geen 'hey' en geen emoji.", 5),
             ]),

        dict(kop="Formeel of informeel",
             opdracht="Let op de aanhef, de slotgroet en de woordkeuze.",
             oefeningen=[
                 ("rij", [("Geachte mevrouw", "formeel"), ("Hey!", "informeel"),
                          ("Met vriendelijke groeten", "formeel"), ("Groetjes", "informeel"),
                          ("Zou u zo vriendelijk willen zijn", "formeel")],
                  "Formeel of informeel?", WW),
                 ("waar", "Een formele brief sluit je af met 'groetjes'.", False),
                 ("open", "Wat kan een spellingcontrole niet voor je doen?",
                  "Ze ziet geen fout woord dat correct gespeld is (dan in plaats van als, hij "
                  "word in plaats van hij wordt), en ze beoordeelt je opbouw, je toon en je "
                  "argumenten niet.", 4),
             ]),

        dict(kop="Spreken en gesprekken",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Wat doe je als je tijdens het spreken een woord niet vindt?",
                  "Je omschrijft het ('het ding waarmee je …'), je gebruikt een synoniem, of je "
                  "zegt gewoon dat je het woord even kwijt bent en praat verder. Stilvallen en "
                  "wachten helpt niet.", 4),
                 ("open", "Noem drie dingen die een gesprek gaande houden.",
                  "Open vragen stellen, doorvragen op wat de ander zegt, zelf iets toevoegen in "
                  "plaats van enkel ja of nee antwoorden, en laten zien dat je luistert door te "
                  "knikken of samen te vatten.", 4),
                 ("waar", "Een gesprek beëindig je het best door gewoon weg te lopen.", False),
                 ("open", "Je spreekopdracht duurt twee minuten. Hoe bereid je die voor?",
                  "Je maakt een kort plan met drie of vier kernwoorden, je oefent hardop en "
                  "klokt de tijd, en je schrijft je tekst niet volledig uit: dan lees je voor in "
                  "plaats van te spreken.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-register-taalvariatie-en-non-verbale-communicatie-spark"] = dict(
    vak="Nederlands", niveau=SPARK,
    titel="Register, taalvariatie en non-verbale communicatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Taalvariëteiten",
             opdracht="Dialect, tussentaal, standaardtaal of jargon?",
             oefeningen=[
                 ("rij", [("Wat zaat ge daar aan 't doen?", "tussentaal"),
                          ("Wat ben je daar aan het doen?", "standaardtaal"),
                          ("De patiënt vertoont een verhoogde bezinking.", "jargon"),
                          ("een woord dat je enkel in één dorp hoort", "dialect")],
                  "Welke taalvariëteit is dit?", WW),
                 ("kort", "Hoe heet de taalvorm tussen dialect en standaardtaal in, die je vaak "
                          "in Vlaamse series hoort?", "tussentaal", W),
                 ("waar", "Belgisch-Nederlands en Nederlands-Nederlands zijn allebei vormen van "
                          "de standaardtaal.", True),
                 ("waar", "Wie tussentaal spreekt, maakt daarmee automatisch spelfouten.",
                  False),
             ]),

        dict(kop="Het juiste register kiezen",
             opdracht="Denk aan met wie je praat en in welke situatie.",
             oefeningen=[
                 ("rij", [("solliciteren per mail voor een vakantiejob", "formeel"),
                          ("een bericht naar je ploegmaats", "informeel"),
                          ("een mail aan de directeur", "formeel"),
                          ("een gesprek met een onbekende volwassene", "formeel (u)")],
                  "Formeel of informeel register?", WW),
                 ("open", "Herschrijf deze zin formeel: 'Hey, kunde gij ons ne keer laten weten "
                          "wanneer da begint?'",
                  "Bijvoorbeeld: 'Geachte mevrouw, zou u ons kunnen laten weten wanneer de "
                  "activiteit begint?'", 4),
                 ("open", "Je schrijft aan je oma, die niets van computers weet, over een "
                          "probleem met haar tablet. Wat doe je met je taalgebruik?",
                  "Je laat het jargon weg of legt het uit, je gebruikt korte zinnen en "
                  "alledaagse woorden, en je beschrijft wat ze moet zien in plaats van hoe iets "
                  "heet.", 4),
             ]),

        dict(kop="Non-verbale communicatie",
             opdracht="Wat zeg je zonder woorden?",
             oefeningen=[
                 ("rij", [("iemand aankijken terwijl je spreekt", "oogcontact"),
                          ("hoe je stem stijgt en daalt", "intonatie"),
                          ("hoe dicht je bij iemand gaat staan", "afstand (persoonlijke ruimte)"),
                          ("je armen kruisen", "lichaamshouding")],
                  "Hoe noem je dit?", WW),
                 ("open", "Je geeft een spreekbeurt en kijkt de hele tijd naar je blad. Welk "
                          "effect heeft dat op je publiek?",
                  "Je klinkt onzeker en je publiek haakt af: zonder oogcontact voelt niemand "
                  "zich aangesproken. Je stem gaat ook naar beneden in plaats van naar de zaal.", 4),
                 ("open", "Je leest in een appgroep: 'ok.' met een punt erachter. Waarom kan dat "
                          "kil overkomen?",
                  "In korte berichten hoort er meestal geen punt. Wie er toch een zet, lijkt de "
                  "zin af te kappen, alsof er geen enthousiasme of geen verdere uitleg volgt.", 4),
                 ("open", "Een leerkracht zegt met een zucht: 'Dat is dan weer prachtig gedaan.' "
                          "Wat kan er aan de hand zijn?",
                  "De woorden zeggen iets positiefs, de toon iets negatiefs. Dat is ironie: het "
                  "non-verbale deel bepaalt dan de echte betekenis.", 4),
                 ("waar", "Een smiley maakt ook een formele mail vriendelijker en mag daar dus "
                          "gerust in.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-literatuur-en-beeldspraak-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Literatuur en beeldspraak",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Over een verhaal praten",
             opdracht="Gebruik de vaste begrippen.",
             oefeningen=[
                 ("rij", [("wie er in het verhaal voorkomt", "de personages"),
                          ("waar het zich afspeelt", "de ruimte"),
                          ("wanneer en hoe lang", "de tijd"),
                          ("de rode draad van gebeurtenissen", "de verhaallijn")],
                  "Hoe heet dit?", WW),
                 ("rij", [("een verzonnen verhaal", "fictie"),
                          ("een boek over de echte Titanic", "non-fictie"),
                          ("een strip", "fictie én literair")],
                  "Fictie of non-fictie?", WW),
                 ("waar", "Een verhaal dat in de ik-vorm geschreven is, is daarom waargebeurd.",
                  False),
             ]),

        dict(kop="Letterlijk of figuurlijk",
             opdracht="Schrijf bij elke zin wat er bedoeld wordt.",
             oefeningen=[
                 ("rij", [("Hij at zijn bord leeg.", "letterlijk"),
                          ("Hij is door het lint gegaan.", "figuurlijk: hij werd woedend"),
                          ("Het regende pijpenstelen.", "figuurlijk: het regende heel hard"),
                          ("Ze zette de ramen open.", "letterlijk")],
                  "Letterlijk of figuurlijk? Wat betekent het?", WW),
                 ("rij", [("Mijn broer is een beer.", "beeldspraak zonder vergelijkingswoord"),
                          ("Mijn broer is zo sterk als een beer.", "een vergelijking")],
                  "Wat voor beeldspraak is dit?", WW),
                 ("open", "Leg het verschil uit tussen een vergelijking en beeldspraak zonder "
                          "vergelijkingswoord.",
                  "Bij een vergelijking staat er een woord als 'zo … als' of 'lijkt op'; je "
                  "ziet dat twee dingen naast elkaar gezet worden. Zonder dat woord wordt het "
                  "ene ding het andere genoemd, wat sterker klinkt.", 5),
                 ("open", "'Hij kreeg het op zijn heupen.' Je kent deze uitdrukking niet. Wat "
                          "doe je?",
                  "Je kijkt naar de zin eromheen: aan de situatie merk je vaak of het iets "
                  "positiefs of negatiefs is. Helpt dat niet, dan zoek je de uitdrukking op; "
                  "letterlijk vertalen werkt hier niet.", 4),
             ]),

        dict(kop="Je mening over een boek",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("rij", [("Ik vond het een goed boek.", "te vaag"),
                          ("Het eerste deel was traag, maar vanaf het ongeluk kon ik niet meer "
                           "stoppen.", "sterk"),
                          ("Het was saai.", "te vaag")],
                  "Is dit een sterke uitspraak over een boek, of te vaag?", WW),
                 ("open", "Waarom zeggen twee lezers soms iets heel anders over hetzelfde "
                          "gedicht?",
                  "Een gedicht laat veel open. Iedereen leest het met zijn eigen ervaringen "
                  "erbij, dus hetzelfde beeld roept bij de een iets anders op dan bij de "
                  "ander.", 4),
                 ("open", "Een gedicht gebruikt korte regels, witruimte en herhaling. Waarom "
                          "doet een dichter dat?",
                  "Om het ritme en de nadruk te sturen. De witruimte dwingt je te pauzeren, de "
                  "herhaling laat een woord zwaarder wegen dan in gewone zinnen.", 4),
                 ("open", "Je schrijft zelf een kort verhaal. Welke bouwstenen heb je zeker "
                          "nodig?",
                  "Een of meer personages, een ruimte, een tijd, en een verhaallijn met een "
                  "probleem dat opgelost of net niet opgelost raakt.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spelling-leestekens-en-werkwoordsvormen-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Spelling, leestekens en werkwoordsvormen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De persoonsvorm in de tegenwoordige tijd",
             opdracht="Stam, stam + t, of de hele vorm. Zoek eerst het onderwerp.",
             oefeningen=[
                 ("rij", [("Wat ___ jij daarvan? (vinden)", "vind"),
                          ("Hij ___ altijd te laat. (antwoorden)", "antwoordt"),
                          ("___ jij me even? (helpen)", "Help"),
                          ("Zij ___ de brief. (versturen)", "verstuurt")],
                  "Vul de juiste vorm in.", W),
                 ("open", "Waarom schrijf je 'hij verwacht' zonder extra t?",
                  "De stam is 'verwacht' en eindigt al op een t. Er komt geen tweede t bij; twee "
                  "dezelfde medeklinkers na elkaar schrijf je niet.", 4),
                 ("waar", "Je hoort het verschil tussen 'hij wordt' en 'hij word'.", False),
             ]),

        dict(kop="Verleden tijd en voltooid deelwoord",
             opdracht="Denk aan het ezelsbruggetje 't kofschip.",
             oefeningen=[
                 ("rij", [("werken", "werkte — gewerkt"), ("leren", "leerde — geleerd"),
                          ("praten", "praatte — gepraat"), ("bellen", "belde — gebeld")],
                  "Geef de verleden tijd en het voltooid deelwoord.", WW),
                 ("kort", "Hoe heet het ezelsbruggetje met t, k, f, s, ch en p?",
                  "'t kofschip", W),
                 ("waar", "Een voltooid deelwoord eindigt nooit op -dt.", True),
                 ("rij", [("Ik ___ mijn huiswerk al gemaakt. (hebben)", "had / heb"),
                          ("Gisteren ___ het de hele dag. (regenen)", "regende"),
                          ("Morgen ___ ik komen. (zullen)", "zal")],
                  "Vul in.", W),
             ]),

        dict(kop="Leestekens en hoofdletters",
             opdracht="Zet de leestekens er zelf bij.",
             oefeningen=[
                 ("rij", [("Als het morgen regent blijven we thuis", "komma na 'regent'"),
                          ("Ze vroeg Kom je mee", "aanhalingstekens rond 'Kom je mee?' en een vraagteken"),
                          ("Ik heb alles nodig papier lijm en een schaar", "dubbele punt na 'nodig', komma's in de opsomming")],
                  "Welk leesteken ontbreekt, en waar?", WW),
                 ("rij", [("frans", "Frans"), ("de franse buurvrouw", "de Franse buurvrouw"),
                          ("hasselt", "Hasselt"), ("maandag", "maandag (geen hoofdletter)")],
                  "Schrijf juist, met of zonder hoofdletter.", WW),
                 ("kort", "Hoe heten de twee puntjes op de e in 'zeeën'?", "een trema", W),
                 ("open", "Waarom schrijf je 'zee-eend' met een koppelteken?",
                  "Omdat er anders drie klinkers na elkaar staan die je verkeerd zou lezen. Het "
                  "streepje houdt de twee woorddelen uit elkaar.", 3),
             ]),

        dict(kop="Meervoud, verkleinwoord en verwarrende woorden",
             opdracht="Let op wat je hoort én op wat je weet.",
             oefeningen=[
                 ("rij", [("man", "mannen"), ("maan", "manen"), ("kind", "kinderen"),
                          ("foto", "foto's"), ("auto", "auto's")],
                  "Geef het meervoud.", W),
                 ("rij", [("boom", "boompje"), ("koning", "koninkje"), ("bloem", "bloempje")],
                  "Geef het verkleinwoord.", W),
                 ("rij", [("Ik ___ het boek op tafel. (leggen)", "leg"),
                          ("Het boek ___ op tafel. (liggen)", "ligt")],
                  "Liggen of leggen? Vul in.", W),
                 ("open", "Je hebt je tekst geschreven en de spellingcontrole meldt niets. Wat "
                          "doe je nog?",
                  "Zelf nalezen, het liefst hardop. De controle ziet geen fout woord dat correct "
                  "gespeld is: hij word, dan in plaats van als, of een zin zonder werkwoord.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordsoorten-en-woordvorming-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Woordsoorten en woordvorming",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Woordsoorten benoemen",
             opdracht="Schrijf de woordsoort voluit.",
             oefeningen=[
                 ("tekst",
                  "<p><i>Gebruik deze zin voor de eerste oefening:</i> "
                  "<b>De oude buurvrouw fietst elke ochtend rustig naar de markt.</b></p>"),
                 ("rij", [("buurvrouw", "zelfstandig naamwoord"), ("oude", "bijvoeglijk naamwoord"),
                          ("fietst", "werkwoord"), ("rustig", "bijwoord"),
                          ("naar", "voorzetsel"), ("De", "lidwoord")],
                  "Welke woordsoort is dit in de zin hierboven?", WW),
                 ("rij", [("hij, zij, wij", "persoonlijk voornaamwoord"),
                          ("mijn, jouw, ons", "bezittelijk voornaamwoord"),
                          ("deze, die, dat", "aanwijzend voornaamwoord"),
                          ("wie, wat, welke", "vragend voornaamwoord")],
                  "Welk soort voornaamwoord is dit?", WW),
                 ("waar", "'Deze' en 'die' zijn bezittelijke voornaamwoorden.", False),
             ]),

        dict(kop="Hetzelfde woord, een andere soort",
             opdracht="Kijk naar wat het woord in die zin doet.",
             oefeningen=[
                 ("open", "In 'Deze fiets is nieuw' en 'Deze is nieuw' — wat is het verschil "
                          "voor het woord 'deze'?",
                  "In de eerste zin hoort het bij een zelfstandig naamwoord: het is een "
                  "aanwijzend voornaamwoord dat bijvoeglijk gebruikt wordt. In de tweede staat "
                  "het alleen en vervangt het dat naamwoord: zelfstandig gebruikt.", 5),
                 ("open", "Wat is het verschil tussen een bijvoeglijk naamwoord en een bijwoord?",
                  "Een bijvoeglijk naamwoord zegt iets over een zelfstandig naamwoord ('de "
                  "snelle fietser'). Een bijwoord zegt iets over het werkwoord of over de hele "
                  "zin ('hij fietst snel').", 4),
                 ("waar", "Een woord kan in de ene zin een andere woordsoort zijn dan in de "
                          "andere.", True),
             ]),

        dict(kop="Woordvorming",
             opdracht="Samenstelling, afleiding, voorvoegsel of achtervoegsel?",
             oefeningen=[
                 ("rij", [("voetbalclub", "samenstelling"), ("onvriendelijk", "afleiding"),
                          ("bakker", "afleiding"), ("tandartspraktijk", "samenstelling"),
                          ("vriendschap", "afleiding")],
                  "Samenstelling of afleiding?", WW),
                 ("rij", [("on- in onvriendelijk", "voorvoegsel"),
                          ("-schap in vriendschap", "achtervoegsel"),
                          ("-er in bakker", "achtervoegsel")],
                  "Voorvoegsel of achtervoegsel?", WW),
                 ("open", "Je leest het woord 'onderbenutting' en je kent het niet. Leid de "
                          "betekenis af uit de delen.",
                  "onder- betekent te weinig, benutten is gebruiken, -ing maakt er een "
                  "zelfstandig naamwoord van. Samen: het feit dat iets te weinig gebruikt "
                  "wordt.", 4),
             ]),

        dict(kop="Synoniemen en homoniemen",
             opdracht="Let op: dezelfde vorm of dezelfde betekenis?",
             oefeningen=[
                 ("kort", "Hoe noem je een woord met dezelfde vorm maar twee heel verschillende "
                          "betekenissen, zoals 'bank'?", "een homoniem", W),
                 ("rij", [("bank", "homoniem"), ("mooi en fraai", "synoniemen"),
                          ("slot", "homoniem"), ("groot en omvangrijk", "synoniemen")],
                  "Homoniem of synoniemen?", WW),
                 ("open", "Geef drie synoniemen van 'mooi'.",
                  "Bijvoorbeeld: fraai, prachtig, schitterend, knap, beeldig.", 3),
                 ("open", "Waarom gebruik je synoniemen in een tekst?",
                  "Om niet telkens hetzelfde woord te herhalen, en om nauwkeuriger te zijn: "
                  "'prachtig' zegt iets anders dan 'aardig'.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-zinsdelen-zinssoorten-en-congruentie-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Zinsdelen, zinssoorten en congruentie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De persoonsvorm en het onderwerp",
             opdracht="Zet de zin in een andere tijd om de persoonsvorm te vinden.",
             oefeningen=[
                 ("tekst",
                  "<p><i>Gebruik deze zin voor de eerste twee oefeningen:</i> "
                  "<b>Op zaterdag bezorgt de postbode onze buren een groot pakket.</b></p>"),
                 ("rij", [("de persoonsvorm", "bezorgt"), ("het onderwerp", "de postbode"),
                          ("het lijdend voorwerp", "een groot pakket"),
                          ("het meewerkend voorwerp", "onze buren"),
                          ("de bijwoordelijke bepaling", "op zaterdag")],
                  "Welk woord of welke woordgroep is dit?", WW),
                 ("open", "Welke vraag gebruik je om het onderwerp te vinden, en welke voor het "
                          "lijdend voorwerp?",
                  "Onderwerp: 'wie of wat + persoonsvorm?'. Lijdend voorwerp: 'wie of wat + "
                  "persoonsvorm + onderwerp?'.", 4),
                 ("waar", "Voor een lijdend voorwerp kan je meestal 'aan' of 'voor' zetten.",
                  False),
             ]),

        dict(kop="Zinssoorten",
             opdracht="Mededelend, vragend, bevelend of uitroepend?",
             oefeningen=[
                 ("rij", [("Sluit het raam.", "bevelend"),
                          ("Wat een lawaai maakt die machine!", "uitroepend"),
                          ("Zou je het raam even willen sluiten?", "vragend"),
                          ("De machine maakt veel lawaai.", "mededelend")],
                  "Welke zinssoort is dit?", WW),
                 ("rij", [("Hij komt niet mee.", "ontkennend"), ("Ik heb niemand gezien.",
                          "ontkennend"), ("Hij komt mee.", "bevestigend")],
                  "Bevestigend of ontkennend?", WW),
                 ("waar", "Een bevelende zin begint altijd met het onderwerp.", False),
             ]),

        dict(kop="Enkelvoudig of samengesteld",
             opdracht="Tel de persoonsvormen.",
             oefeningen=[
                 ("rij", [("Ik wist niet dat je ziek was, dus ik belde niet.", "3"),
                          ("Na de les fietste hij meteen naar huis.", "1"),
                          ("Hij belde aan en wachtte.", "2")],
                  "Hoeveel persoonsvormen staan er?", W),
                 ("open", "Wat vertelt het aantal persoonsvormen je over een zin?",
                  "Uit hoeveel deelzinnen de zin bestaat. Eén persoonsvorm is een enkelvoudige "
                  "zin, meer dan één is een samengestelde zin.", 3),
             ]),

        dict(kop="Congruentie",
             opdracht="Onderwerp en persoonsvorm moeten bij elkaar passen.",
             oefeningen=[
                 ("rij", [("De regering hebben een beslissing genomen.", "heeft"),
                          ("Een groep leerlingen staan buiten.", "staat"),
                          ("Er komen drie gasten.", "juist"),
                          ("Jij en ik gaat samen.", "gaan")],
                  "Verbeter de persoonsvorm, of schrijf 'juist'.", WW),
                 ("open", "Waarom is 'De regering hebben een beslissing genomen' fout?",
                  "'De regering' is enkelvoud, ook al zitten er veel mensen in. De persoonsvorm "
                  "moet dus 'heeft' zijn.", 3),
                 ("open", "In 'Er komen drie gasten' staat het onderwerp achter de "
                          "persoonsvorm. Wat is het onderwerp, en hoe vind je het?",
                  "'Drie gasten'. Je vraagt: wie of wat komen er? 'Er' is geen onderwerp maar "
                  "een opvulwoord.", 4),
                 ("open", "Waarom helpt zinsontleding je bij het schrijven?",
                  "Je ziet waar je zin uit elkaar valt: een ontbrekend werkwoord, een "
                  "persoonsvorm die niet bij het onderwerp past, of een bepaling die zo ver van "
                  "haar zinsdeel staat dat de lezer haar verkeerd leest.", 4),
             ]),
    ],
)

# ============================================================
# De twee hoofdstukken begrijpend lezen staan los van elkaar, dus elk zijn
# eigen bundel. De leestekst hieronder is een andere dan die op het scherm.
# ============================================================
OEFENBUNDELS["oefenbundel-begrijpend-lezen-de-smartphone-op-school-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Begrijpend lezen — de smartphone op school",
    onder="Een tekst en {aantal} vragen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Lees de tekst eerst helemaal door voor je aan de vragen begint.",
        "Kom bij elke vraag terug naar de tekst: het antwoord staat er of volgt eruit.",
        "Duid in de tekst aan waar je het antwoord gevonden hebt.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
    ],
    reeksen=[
        dict(kop="De tekst",
             opdracht="Lees eerst deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Het uur zonder scherm</h3>"
                  "<p>Sinds september voert het Sint-Jozefinstituut in Herk-de-Stad een "
                  "opvallende regel in: tijdens de middagpauze gaan alle gsm's in een gesloten "
                  "kastje. Niet enkel bij de eerstejaars, maar bij iedereen, tot en met het "
                  "zesde jaar. De school noemt het 'het uur zonder scherm'.</p>"
                  "<p>Directeur Vandeput geeft toe dat het idee niet van de leerkrachten kwam. "
                  "„Het was de leerlingenraad die erover begon”, zegt hij. „Ze vertelden dat ze "
                  "elkaar tijdens de pauze nauwelijks nog spraken. Iedereen zat wel ergens, maar "
                  "niemand zat samen.”</p>"
                  "<p>De eerste weken verliepen stroef. Een aantal leerlingen weigerde het "
                  "toestel af te geven, en er kwamen boze mails van ouders die hun kind "
                  "onbereikbaar vonden. Daarom belt het secretariaat nu zelf als er iets "
                  "dringends is. Sindsdien zijn de klachten grotendeels verdwenen.</p>"
                  "<p>Wat het oplevert, is moeilijker te meten. De school telde wel dat het "
                  "aantal leerlingen dat 's middags meedoet aan een sportactiviteit, "
                  "verdubbelde: van 40 naar ongeveer 85. Of de leerlingen ook beter opletten in "
                  "het vijfde lesuur, durft Vandeput niet te zeggen. „Dat zou ik graag beweren, "
                  "maar ik heb er geen cijfers over. Wat ik wél zie, is dat de refter luider is "
                  "dan vroeger. En dat vind ik een goed teken.”</p>"
                  "<p>Niet iedereen is overtuigd. Sommige leerlingen vinden dat de school te ver "
                  "gaat. „Ik gebruik mijn gsm net om even alleen te zijn”, zegt een leerlinge "
                  "van het vijfde jaar. „Dat is toch niet hetzelfde als asociaal doen?” De "
                  "school belooft de regel in januari opnieuw te bekijken, samen met de "
                  "leerlingenraad die ze bedacht heeft.</p>"),
             ]),

        dict(kop="Wat staat er",
             opdracht="Zoek het antwoord in de tekst.",
             oefeningen=[
                 ("kort", "Van wie kwam het idee voor het uur zonder scherm?",
                  "van de leerlingenraad", WW),
                 ("kort", "Voor welke leerlingen geldt de regel?",
                  "voor iedereen, van het eerste tot het zesde jaar", WW),
                 ("kort", "Hoeveel leerlingen doen er nu 's middags mee aan een sportactiviteit?",
                  "ongeveer 85", W),
                 ("open", "Welke twee problemen kwamen er in de eerste weken, en wat deed de "
                          "school eraan?",
                  "Leerlingen weigerden hun toestel af te geven, en ouders klaagden dat hun kind "
                  "onbereikbaar was. De school liet het secretariaat zelf bellen bij iets "
                  "dringends.", 4),
             ]),

        dict(kop="Wat er niet letterlijk staat",
             opdracht="Leid af uit de tekst en leg uit waaruit je het afleidt.",
             oefeningen=[
                 ("open", "Schrijf de hoofdgedachte van deze tekst in één zin.",
                  "Een school haalt de gsm's weg tijdens de middagpauze; dat levert zichtbaar "
                  "meer contact en sport op, maar niet iedereen is het ermee eens en de regel "
                  "wordt opnieuw bekeken.", 3),
                 ("open", "„Iedereen zat wel ergens, maar niemand zat samen.” Wat bedoelt de "
                          "directeur met die zin?",
                  "Dat de leerlingen lichamelijk wel in dezelfde ruimte zaten, maar ieder met "
                  "zijn eigen scherm bezig was en er dus geen echt contact was.", 4),
                 ("open", "De directeur noemt de luidere refter 'een goed teken'. Waarom vindt "
                          "hij dat?",
                  "Lawaai betekent hier dat de leerlingen weer met elkaar praten. Stilte in een "
                  "refter vol tieners wees er net op dat iedereen op zijn scherm zat.", 4),
                 ("open", "Welke zin in de tekst toont dat de directeur eerlijk is over wat hij "
                          "niet weet? Schrijf ze over.",
                  "„Dat zou ik graag beweren, maar ik heb er geen cijfers over.” Hij geeft toe "
                  "dat hij niet kan aantonen dat leerlingen beter opletten.", 3),
                 ("kort", "Welk cijfer in de tekst is een feit dat je kan nagaan?",
                  "het aantal sporters: van 40 naar ongeveer 85", WW),
                 ("open", "Wat is het argument van de leerlinge uit het vijfde jaar tegen de "
                          "regel?",
                  "Dat ze haar gsm gebruikt om even alleen te zijn, en dat alleen willen zijn "
                  "niet hetzelfde is als asociaal doen.", 3),
                 ("waar", "Uit de tekst blijkt dat de leerlingen nu beter opletten in het "
                          "vijfde lesuur.", False),
                 ("open", "Is deze tekst vooral informatief of vooral overtuigend? Leg je "
                          "antwoord uit met iets uit de tekst.",
                  "Vooral informatief: de tekst laat zowel de school als een tegenstander aan "
                  "het woord, noemt de problemen in de eerste weken, en zegt eerlijk wat er niet "
                  "gemeten is. Een overtuigende tekst zou die twijfel weglaten.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-begrijpend-lezen-hoe-de-fiets-werd-wat-hij-is-spark"] = dict(
    vak="Nederlands", niveau=SPARK, titel="Begrijpend lezen — hoe de fiets werd wat hij is",
    onder="Een tekst en {aantal} vragen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Lees de tekst eerst helemaal door voor je aan de vragen begint.",
        "Kom bij elke vraag terug naar de tekst: het antwoord staat er of volgt eruit.",
        "Duid in de tekst aan waar je het antwoord gevonden hebt.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
    ],
    reeksen=[
        dict(kop="De tekst",
             opdracht="Lees eerst deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>De uitvinding die niemand wilde</h3>"
                  "<p>Wie vandaag een fiets koopt, krijgt een toestel dat al meer dan honderd "
                  "jaar nauwelijks veranderd is: twee wielen van gelijke grootte, een ketting "
                  "naar het achterwiel, en een frame in de vorm van twee driehoeken. Die vorm "
                  "kreeg in 1885 haar naam: de <i>safety bicycle</i>, de veilige fiets. Dat "
                  "woord 'veilig' zegt alles over wat eraan voorafging.</p>"
                  "<p>De fietsen daarvóór hadden een voorwiel zo groot als een mens. Dat was "
                  "geen gril. Er bestond nog geen ketting, dus de trappers zaten rechtstreeks "
                  "aan het wiel. Eén omwenteling van je benen was één omwenteling van het wiel, "
                  "en hoe groter dat wiel, hoe verder je kwam. Wie snel wilde rijden, moest dus "
                  "hoog zitten. En wie hoog zit, valt ver.</p>"
                  "<p>De ketting loste dat in één keer op. Met een groot tandwiel vooraan en een "
                  "klein achteraan draait het achterwiel meermaals per pedaalomwenteling. Je "
                  "kon dus even snel rijden op kleine wielen. Plots moest niemand nog hoog "
                  "zitten.</p>"
                  "<p>Toch verkocht de nieuwe fiets in het begin slecht. De oude hoge fiets gold "
                  "als sportief en stoer; de lage werd uitgelachen als een toestel voor wie bang "
                  "was. Pas toen er in 1888 luchtbanden bij kwamen — een uitvinding van een "
                  "dierenarts die het comfort van zijn zoon wilde verbeteren — sloeg het om. Met "
                  "lucht in de banden was de lage fiets niet alleen veiliger, maar ook sneller "
                  "dan de hoge. Wielrenners stapten over, en daarna iedereen.</p>"
                  "<p>Historici wijzen er graag op wat daarna gebeurde. De fiets was het eerste "
                  "vervoermiddel dat een gewone arbeider kon betalen, en het eerste dat vrouwen "
                  "zonder begeleiding buiten hun dorp bracht. Een uitvinding die begon als een "
                  "oplossing voor gebroken polsen, veranderde uiteindelijk wie er waar mocht "
                  "komen.</p>"),
             ]),

        dict(kop="Wat staat er",
             opdracht="Zoek het antwoord in de tekst.",
             oefeningen=[
                 ("kort", "In welk jaar kreeg de safety bicycle haar naam?", "1885", W),
                 ("kort", "Wie vond de luchtband uit, volgens de tekst?",
                  "een dierenarts", WW),
                 ("open", "Waarom hadden de oudste fietsen zo'n groot voorwiel? Leg de reden "
                          "uit.",
                  "Er was nog geen ketting, dus de trappers zaten rechtstreeks aan het wiel. Eén "
                  "pedaalomwenteling was één wielomwenteling, dus een groter wiel betekende een "
                  "grotere afstand per trap.", 4),
                 ("open", "Hoe loste de ketting dat probleem op?",
                  "Met een groot tandwiel vooraan en een klein achteraan draait het achterwiel "
                  "meerdere keren per pedaalomwenteling. Je haalt dus dezelfde snelheid met "
                  "kleine wielen.", 4),
             ]),

        dict(kop="Wat er niet letterlijk staat",
             opdracht="Leid af uit de tekst en leg uit waaruit je het afleidt.",
             oefeningen=[
                 ("open", "Wat bedoelt de schrijver met de titel 'De uitvinding die niemand "
                          "wilde'?",
                  "Dat de veilige lage fiets in het begin slecht verkocht: mensen vonden hem "
                  "niet stoer. Pas later werd hij de fiets die iedereen kocht.", 4),
                 ("open", "„En wie hoog zit, valt ver.” Waarom staat die korte zin daar, denk "
                          "je?",
                  "Ze vat in vijf woorden samen waarom die fietsen gevaarlijk waren, en ze legt "
                  "meteen uit waar het woord 'veilig' in safety bicycle vandaan komt. Door de "
                  "korte zin valt ze extra op.", 4),
                 ("open", "Waarom sloeg de lage fiets pas om in 1888 en niet in 1885?",
                  "Pas met luchtbanden werd hij ook sneller dan de hoge fiets. Zolang hij enkel "
                  "veiliger was, woog dat niet op tegen het imago van stoer en sportief.", 4),
                 ("open", "De laatste alinea gaat niet meer over techniek. Waarover gaat ze wel, "
                          "en waarom sluit de schrijver daarmee af?",
                  "Over het maatschappelijke gevolg: arbeiders en vrouwen konden zich verplaatsen. "
                  "De schrijver sluit daarmee af om te tonen dat een technische uitvinding het "
                  "leven van mensen kan veranderen, veel verder dan waarvoor ze bedoeld was.", 5),
                 ("kort", "Schrijf het onderwerp van deze tekst in enkele woorden.",
                  "de ontwikkeling van de moderne fiets", WW),
                 ("waar", "Volgens de tekst was de lage fiets meteen een succes.", False),
                 ("open", "In de tekst staan feiten en meningen door elkaar. Geef één zin die "
                          "een feit is en één die een mening of een interpretatie is.",
                  "Feit: 'Die vorm kreeg in 1885 haar naam.' Interpretatie: 'Dat woord veilig "
                  "zegt alles over wat eraan voorafging.'", 4),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)

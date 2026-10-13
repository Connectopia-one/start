# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Engels 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere Engelse tekstjes, andere zinnen om te verbeteren, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een zin
herschrijven, zelf een mail opstellen). Wie hier iets bijschrijft, legt het
eerst naast `../../boost-doorstroom/engels.json`.

De leesoefeningen staan op echte Engelse tekstjes, zoals het hoort bij een
taalvak. Ze zijn nieuw geschreven voor deze bundel, dus je kan ze niet
terugvinden in de vragen op het scherm.

In elke bundel staat achteraan één reeks "Voor het echte leven". Die vraagt
om te luisteren of te spreken, want luisteren is de helft van het examen
Engels 1 en mondelinge interactie en spreken zijn samen 38 % van Engels 2.
Dat leer je niet achter een scherm. Laat die reeks staan.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Engels"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf bij een zin die je moet verbeteren de hele zin over, niet alleen het woord dat verandert.",
    "Bij een vraag over een tekst: onderstreep in de tekst waar je het antwoord gevonden hebt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def echte_leven(opdracht, antwoord, regels=6):
    """De vaste slotreeks over luisteren en spreken."""
    return dict(
        kop="Voor het echte leven",
        opdracht="Deze oefening maak je op papier, maar ze is pas af als je ze ook echt gedaan hebt.",
        oefeningen=[("open", opdracht, antwoord, regels)],
    )


# ============================================================
OEFENBUNDELS["oefenbundel-een-engelse-tekst-analyseren-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Een Engelse tekst analyseren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tekst A: the night bus",
             opdracht="Lees de tekst en beantwoord de vragen eronder.",
             oefeningen=[
                 ("tekst",
                  "<em>Since September, our town has had a night bus at weekends. It leaves the station "
                  "every hour between midnight and four in the morning. The council says the service is "
                  "meant for people who work late shifts, but so far most passengers have been students "
                  "coming home from the city. Drivers report that the four o'clock bus is almost always "
                  "empty. Unless more people start using it, the council will cut the service in June.</em>"),
                 ("kort", "Wat is het onderwerp? Antwoord in enkele woorden.", "de nachtbus in de stad", WL),
                 ("open", "Wat is de hoofdgedachte? Antwoord in één hele zin.",
                  "Er rijdt sinds september een nachtbus, maar hij wordt te weinig gebruikt en dreigt te verdwijnen.", 3),
                 ("kort", "Hoeveel bussen rijden er per nacht? Antwoord met een getal.", "5 (van middernacht tot vier uur, elk uur)", W),
                 ("open", "Voor wie was de dienst bedoeld, en wie gebruikt hem vooral? Dat staat er letterlijk.",
                  "Bedoeld voor mensen die late shiften werken; vooral studenten die uit de stad naar huis komen.", 3),
                 ("open", "Leid af: gaat de bus van vier uur waarschijnlijk verdwijnen? Waarom denk je dat?",
                  "Waarschijnlijk wel: de chauffeurs melden dat die bus bijna altijd leeg is, en de gemeente schrapt de dienst als er niet meer mensen opstappen.", 4),
                 ("kort", "Welk verband legt 'unless' in de laatste zin?", "een voorwaarde: if not", WL),
             ]),
        dict(kop="Tekst B: een beoordeling",
             opdracht="Lees de beoordeling en beantwoord de vragen.",
             oefeningen=[
                 ("tekst",
                  "<em>We booked the walking tour because the reviews were so good. Our guide knew every "
                  "street and every story, and two hours flew by. The only thing I would change is the "
                  "starting time: nine in the morning on a Sunday is early, and half the group arrived "
                  "late. Would I go again? Absolutely.</em>"),
                 ("kies", "Welk oordeel geeft de schrijver?",
                  ["volledig positief", "gemengd, maar overwegend positief", "gemengd, maar overwegend negatief", "volledig negatief"], 1),
                 ("kort", "Welk woord of welke woordgroep draagt het enige punt van kritiek?", "the starting time (nine on a Sunday is early)", WL),
                 ("open", "Wat betekent 'two hours flew by'? Leg uit in het Nederlands.",
                  "De twee uur gingen razendsnel voorbij, dus de schrijver verveelde zich niet.", 3),
                 ("kies", "Welke tekstsoort is dit?",
                  ["informatief", "prescriptief", "opiniërend", "narratief"], 2),
             ]),
        dict(kop="Tussen de regels lezen",
             opdracht="Schrijf bij elke zin wat je eruit mag afleiden. Eén zin volstaat.",
             oefeningen=[
                 ("kort", "Unlike his brother, Tom has never learnt to drive.", "de broer kan wel autorijden", WL),
                 ("kort", "The shop is closed on Sundays and on bank holidays.", "op een feestdag die op zondag valt, is het zeker gesloten", WL),
                 ("kort", "The last tickets went in under ten minutes.", "de tickets waren bijzonder snel uitverkocht", WL),
                 ("kort", "Pupils who forget their swimming kit will watch from the side.", "wie zijn zwemgerief vergeet, mag niet meezwemmen", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Omcirkel het juiste antwoord.",
             oefeningen=[
                 ("waar", "Het onderwerp van een tekst schrijf je in een hele zin, de hoofdgedachte in enkele woorden.", False),
                 ("waar", "Wat je uit een tekst afleidt, moet volgen uit die tekst maar hoeft er niet letterlijk in te staan.", True),
                 ("waar", "Een tekst analyseren betekent dat je hem eerst volledig vertaalt.", False),
                 ("waar", "Bij één gerichte vraag zoek je in de tekst naar de vorm die je nodig hebt, bijvoorbeeld een uur of een datum.", True),
                 ("waar", "Vind je de hoofdgedachte niet, dan lees je best de titel en de eerste en laatste zin opnieuw.", True),
             ]),
        echte_leven(
            "Zoek een Engelstalig nieuwsfilmpje van hoogstens drie minuten. Kijk het één keer zonder "
            "ondertitels. Schrijf daarna hieronder op wat het onderwerp was, in enkele woorden, en wat de "
            "hoofdgedachte was, in één hele zin. Kijk het dan nog eens met ondertitels en verbeter jezelf.",
            "Vrij antwoord. Wie na één keer kijken het onderwerp al heeft, zit goed; de hoofdgedachte vraagt "
            "meestal een tweede keer.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-tekstverbanden-en-verwijswoorden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Tekstsoorten, tekstverbanden en verwijswoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort?",
             opdracht="Schrijf bij elk fragment de tekstsoort: informatief, persuasief, opiniërend, "
                      "prescriptief, narratief of literair.",
             oefeningen=[
                 ("rij", [("Shake well before use. Do not take more than two tablets a day.", "prescriptief"),
                          ("The exhibition runs from 4 May until 30 June at the city museum.", "informatief"),
                          ("Give blood today. It costs you an hour and it saves a life.", "persuasief")],
                  "Welke tekstsoort?", WL),
                 ("rij", [("If you ask me, the new timetable was a bad idea from the start.", "opiniërend"),
                          ("We left at dawn, walked all day and slept in a barn.", "narratief"),
                          ("The wind read the letters no one had sent.", "literair")],
                  "Welke tekstsoort?", WL),
             ]),
        dict(kop="Signaalwoorden",
             opdracht="Schrijf bij elk signaalwoord welk verband het legt: oorzaak, gevolg, tegenstelling, "
                      "voorbeeld, toevoeging of vergelijking.",
             oefeningen=[
                 ("rij", [("because", "oorzaak"), ("therefore", "gevolg"), ("however", "tegenstelling"),
                          ("for instance", "voorbeeld")], "Welk verband?", WW),
                 ("rij", [("in addition", "toevoeging"), ("unlike", "vergelijking"), ("as a result", "gevolg"),
                          ("although", "tegenstelling")], "Welk verband?", WW),
                 ("rij", [("despite", "tegenstelling"), ("so", "gevolg"), ("since", "oorzaak"),
                          ("yet", "tegenstelling")], "Welk verband?", WW),
             ]),
        dict(kop="Vul het signaalwoord in",
             opdracht="Vul het woord in dat het gevraagde verband legt. Er is telkens één goed antwoord.",
             oefeningen=[
                 ("kort", "The bridge was closed, … we had to go round. (gevolg)", "so", W),
                 ("kort", "… the weather was awful, we had a great weekend. (tegenstelling, vooraan)", "Although", W),
                 ("kort", "Many birds are in trouble. …, the curlew has almost disappeared. (voorbeeld)", "For instance", WW),
                 ("kort", "… the heavy rain, the match went ahead. (tegenstelling, gevolgd door een naamwoord)", "Despite", W),
             ]),
        dict(kop="Waar verwijst het woord naar?",
             opdracht="Schrijf op waarnaar het vetgedrukte woord verwijst.",
             oefeningen=[
                 ("kort", "My aunt lives in Cork. <strong>She</strong> visits us every summer.", "de tante", WL),
                 ("kort", "The school scrapped the Friday test. <strong>This</strong> surprised everyone.",
                  "het schrappen van de vrijdagtoets", WL),
                 ("kort", "The roads were icy and the buses were late. <strong>It</strong> was a difficult morning.",
                  "naar de hele situatie van de vorige zin", WL),
                 ("kort", "Ann lent Iris her bike. Wiens fiets is het volgens de gewone lezing?", "die van Ann", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Omcirkel het juiste antwoord.",
             oefeningen=[
                 ("waar", "Eén tekst kan kenmerken van meer dan één tekstsoort hebben.", True),
                 ("waar", "Signaalwoorden staan er alleen om een tekst mooier te laten klinken.", False),
                 ("waar", "Een bijsluiter is een prescriptieve tekst.", True),
                 ("waar", "Therefore en however betekenen ongeveer hetzelfde.", False),
                 ("waar", "Although en but staan niet op dezelfde plaats in de zin.", True),
             ]),
        echte_leven(
            "Zoek een Engelstalige podcastaflevering over een onderwerp dat je interesseert en luister tien "
            "minuten. Noteer elk signaalwoord dat je hoort en zet erachter welk verband het legde. Vertel "
            "daarna aan iemand, in het Engels, waar die tien minuten over gingen.",
            "Vrij antwoord. Vier of vijf signaalwoorden in tien minuten is normaal; hoor je er geen, luister "
            "dan naar een gesprek of een discussie in plaats van naar een verhaal.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-engelstalige-wereld-gewoontes-en-conventies-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De Engelstalige wereld: gewoontes en conventies",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Brits of Amerikaans?",
             opdracht="Bij elk woord staat maar één van de twee varianten. Schrijf de andere erbij.",
             oefeningen=[
                 ("rij", [("lift", "elevator"), ("vacation", "holiday"), ("lorry", "truck"),
                          ("gas", "petrol")], "De andere variant", WW),
                 ("rij", [("fall", "autumn"), ("flat", "apartment"), ("crisps", "chips"),
                          ("soccer", "football")], "De andere variant", WW),
             ]),
        dict(kop="Spelling",
             opdracht="Schrijf de Britse spelling naast de Amerikaanse.",
             oefeningen=[
                 ("rij", [("color", "colour"), ("center", "centre"), ("favorite", "favourite"),
                          ("traveled", "travelled")], "Brits", WW),
             ]),
        dict(kop="Lezen wat er staat",
             opdracht="Beantwoord kort.",
             oefeningen=[
                 ("kort", "Een Britse uitnodiging zegt: the reception is on the first floor. Op welke verdieping is dat bij ons?",
                  "op de eerste verdieping, dus niet op het gelijkvloers", WL),
                 ("kort", "Een Britse brief is gedateerd 9/12/2027. Welke datum is dat?", "9 december 2027", WL),
                 ("kort", "Een Amerikaanse weerman kondigt 95 degrees aan. Warm of koud?", "warm: ongeveer 35 °C, want het is Fahrenheit", WL),
                 ("kort", "Op een Brits bord staat: Please queue here. Wat doe je?", "je sluit achteraan in de rij aan", WL),
                 ("kort", "Hoeveel kilometer is ongeveer 10 miles?", "ongeveer 16 km", W),
             ]),
        dict(kop="Aanhef en afsluiter",
             opdracht="Schrijf bij elke situatie de juiste aanhef én de juiste afsluiter.",
             oefeningen=[
                 ("tabel", ["Situatie", "Aanhef", "Afsluiter"],
                  [["je schrijft naar een secretariaat en kent de naam niet", None, None],
                   ["je schrijft naar mevrouw Taylor, van wie je de naam kent", None, None],
                   ["je schrijft naar je penvriend Sam", None, None]],
                  "Dear Sir or Madam, / Yours faithfully, — Dear Ms Taylor, / Yours sincerely, — "
                  "Hi Sam, / Best wishes, (of See you soon, of Take care,)", WW),
                 ("kort", "Welke aanspreking gebruik je voor een vrouw van wie je niet weet of ze getrouwd is?", "Ms", W),
             ]),
        dict(kop="Zeg het beleefd",
             opdracht="Herschrijf elke zin zo dat hij beleefd klinkt in het Engels.",
             oefeningen=[
                 ("kort", "Tell me when the course starts.", "Could you tell me when the course starts?", WL),
                 ("kort", "I want a room for two nights.", "I would like a room for two nights, please.", WL),
                 ("kort", "Give me your address.", "Could you give me your address, please?", WL),
                 ("open", "Iemand zegt tegen jou: I'm sorry I'm late. Schrijf twee gepaste reacties.",
                  "Bijvoorbeeld: That's all right, don't worry. / No problem, we've only just started.", 3),
             ]),
        dict(kop="Feesten",
             opdracht="Zet het feest bij de datum.",
             oefeningen=[
                 ("rij", [("4 juli", "Independence Day"), ("17 maart", "St Patrick's Day"),
                          ("31 oktober", "Halloween"), ("vierde donderdag van november", "Thanksgiving")],
                  "Welk feest?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Omcirkel het juiste antwoord.",
             oefeningen=[
                 ("waar", "England en Great Britain betekenen hetzelfde.", False),
                 ("waar", "Op een examen mag je Brits en Amerikaans Engels door elkaar gebruiken.", False),
                 ("waar", "In de Verenigde Staten is het in een restaurant gebruikelijk om fooi te geven.", True),
                 ("waar", "Engels is ook in India en in Zuid-Afrika een officiële taal.", True),
                 ("waar", "Please en thank you gebruik je in het Engels ongeveer even vaak als bij ons.", False),
             ]),
        echte_leven(
            "Kijk een half uur naar een Britse en een half uur naar een Amerikaanse reeks of film. Schrijf "
            "hieronder vijf woorden op die je in de ene wel en in de andere niet zou verwachten, en zeg van "
            "elk welke variant het is.",
            "Vrij antwoord. Denk aan lift en elevator, flat en apartment, rubbish en trash, queue en line, "
            "mate en buddy.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-schriftelijke-interactie-en-literatuurbeleving-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Schrijven, schriftelijke interactie en literatuurbeleving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke schrijfopdracht?",
             opdracht="Schrijf bij elke situatie welke opdracht het is: iets vertellen, iets uitleggen, "
                      "overtuigen, informatie vragen, je mening geven of informatie geven.",
             oefeningen=[
                 ("rij", [("Je schrijft aan je penvriend wat je op het schoolfeest meemaakte.", "iets vertellen"),
                          ("Je legt uit hoe je een fietsband plakt.", "iets uitleggen"),
                          ("Je wil je zus meekrijgen naar een concert.", "overtuigen")],
                  "Welke opdracht?", WL),
                 ("rij", [("Je mailt een jeugdherberg over de prijzen.", "informatie vragen"),
                          ("Je schrijft in de schoolkrant wat jij van de nieuwe uurregeling vindt.", "je mening geven"),
                          ("Je stuurt de groep de plaats en het uur van de afspraak door.", "informatie geven")],
                  "Welke opdracht?", WL),
             ]),
        dict(kop="Zeg het in het Engels",
             opdracht="Schrijf één Engelse zin die doet wat er gevraagd wordt.",
             oefeningen=[
                 ("kort", "Nodig iemand uit om zaterdag mee te gaan.", "Would you like to join us on Saturday?", WL),
                 ("kort", "Toon belangstelling voor iemand die ziek was.", "Are you feeling better now?", WL),
                 ("kort", "Bedank iemand bij wie je gelogeerd hebt.", "Thank you so much, I had a wonderful time.", WL),
                 ("kort", "Verontschuldig je en geef een reden.", "Sorry I missed your call, I was on the train.", WL),
                 ("kort", "Sla een uitnodiging beleefd af.", "I'd love to, but I'm afraid I can't.", WL),
                 ("kort", "Vraag hoe je je kan inschrijven voor een cursus.", "I would like to know how I can register for the course.", WL),
             ]),
        dict(kop="Waarop word je beoordeeld?",
             opdracht="Vul de tabel aan met wat er bij elk punt gevraagd wordt.",
             oefeningen=[
                 ("tabel", ["Beoordelingspunt", "Wat er gevraagd wordt"],
                  [["taakvoltooiing", None], ["tekststructuur en samenhang", None],
                   ["register", None], ["tekstopbouw en lay-out", None]],
                  "taakvoltooiing: je boodschap komt over en je opdracht is volledig uitgevoerd — "
                  "tekststructuur en samenhang: een inleiding, een midden en een slot, met verbindende woorden — "
                  "register: je toon past bij wie je aanspreekt — "
                  "tekstopbouw en lay-out: een titel en duidelijke alinea's", WL),
                 ("kort", "Hoe noem je het als je boodschap overkomt en je opdracht volledig is uitgevoerd?", "taakvoltooiing", WW),
                 ("kort", "Je krijgt een opdracht van 120 tot 150 woorden en je schrijft er 70. Waar verlies je punten?", "op taakvoltooiing", WW),
             ]),
        dict(kop="Vastzitten en toch verder",
             opdracht="Omschrijf elk woord in het Engels zonder het woord zelf te gebruiken. Eén zin volstaat.",
             oefeningen=[
                 ("kort", "crutches", "the sticks you walk with after you break a leg", WL),
                 ("kort", "a fortnight", "two weeks", WL),
                 ("kort", "a plumber", "someone who repairs pipes and taps", WL),
                 ("kort", "a receipt", "the paper you get in a shop that shows what you paid", WL),
             ]),
        dict(kop="Leeservaring of samenvatting?",
             opdracht="Schrijf bij elke zin of het een leeservaring (L) of een samenvatting (S) is.",
             oefeningen=[
                 ("rij", [("The story is set in Dublin in 1916.", "S"),
                          ("The ending made me feel uncomfortable.", "L"),
                          ("I recognised myself in the younger brother.", "L"),
                          ("The book has three parts.", "S")], "L of S?", W),
             ]),
        dict(kop="Schrijf zelf",
             opdracht="Schrijf de gevraagde tekst. Hou je aan het aantal woorden.",
             oefeningen=[
                 ("open", "Schrijf een mail van 60 tot 80 woorden aan een jeugdherberg in Wales. Vraag naar de prijs "
                          "per nacht, of er ontbijt bij zit, en of je een fiets kan huren. Gebruik de juiste aanhef "
                          "en afsluiter.",
                  "Bijvoorbeeld: Dear Sir or Madam, I am writing to ask about a stay in July. Could you tell me how "
                  "much a night costs, and whether breakfast is included? I would also like to know if it is "
                  "possible to hire a bike. Thank you in advance. Yours faithfully, … — Let op: drie vragen, dus "
                  "drie vragen beantwoord; Dear Sir or Madam gaat met Yours faithfully.", 10),
                 ("open", "Je vriend schrijft: 'We're going to the coast on Sunday. Do you want to come? And can you "
                          "bring your camera?' Schrijf een antwoord van 40 tot 60 woorden waarin je op allebei de "
                          "vragen ingaat.",
                  "Bijvoorbeeld: Hi, thanks for asking! I'd love to come on Sunday. I'll bring my camera, but the "
                  "battery is almost dead, so I'll charge it on Saturday night. What time are we leaving? See you "
                  "soon, … — Bij schriftelijke interactie mag je geen enkele vraag laten liggen.", 8),
             ]),
        echte_leven(
            "Vraag aan iemand die Engels kent om je zelfgeschreven mail hardop voor te lezen. Luister waar "
            "hij of zij hapert: dat zijn de zinnen die niet lopen. Schrijf hieronder op welke twee zinnen je "
            "gaat herschrijven en waarom.",
            "Vrij antwoord. Haperen gebeurt meestal bij te lange zinnen en bij een letterlijk vertaalde "
            "Nederlandse woordvolgorde.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-woordvelden-mensen-gezondheid-en-het-dagelijkse-leven-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: mensen, gezondheid en het dagelijkse leven",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Familie",
             opdracht="Vul het Engelse woord in.",
             oefeningen=[
                 ("rij", [("de zoon van je zus", "nephew"), ("de dochter van je broer", "niece"),
                          ("het kind van je tante", "cousin"), ("de zus van je moeder", "aunt")],
                  "In het Engels", WW),
                 ("rij", [("de moeder van je echtgenoot", "mother-in-law"), ("je kleinzoon", "grandson"),
                          ("de nieuwe echtgenote van je vader", "stepmother")], "In het Engels", WW),
             ]),
        dict(kop="Een formulier invullen",
             opdracht="Schrijf bij elk Engels veld wat je erin zet.",
             oefeningen=[
                 ("rij", [("surname", "je achternaam"), ("date of birth", "je geboortedatum"),
                          ("marital status", "je burgerlijke staat"), ("occupation", "je beroep")],
                  "Wat vul je in?", WW),
             ]),
        dict(kop="Gevoelens en gezondheid",
             opdracht="Vul in of beantwoord kort.",
             oefeningen=[
                 ("kort", "Schrijf het Engelse woord voor teleurgesteld. Let op de spelling.", "disappointed", WW),
                 ("kort", "Welk woord is ongeveer het tegenovergestelde van cheerful?", "gloomy", W),
                 ("kort", "Hoe zeg je in het Engels dat je keelpijn hebt?", "I have a sore throat", WL),
                 ("kort", "Wat betekent I'm feeling a bit under the weather?", "ik voel me niet zo lekker", WL),
                 ("kort", "Waar ga je in het Verenigd Koninkrijk naartoe voor een geneesmiddel?", "to the chemist's", WW),
             ]),
        dict(kop="Arm of been?",
             opdracht="Schrijf bij elk lichaamsdeel of het bij de arm (A), het been (B) of het hoofd en de romp (H) hoort.",
             oefeningen=[
                 ("rij", [("elbow", "A"), ("ankle", "B"), ("wrist", "A"), ("neck", "H")], "A, B of H?", W),
                 ("rij", [("knee", "B"), ("shoulder", "A"), ("hip", "B"), ("throat", "H")], "A, B of H?", W),
             ]),
        dict(kop="Do of make?",
             opdracht="Vul do of make in, in de juiste vorm.",
             oefeningen=[
                 ("rij", [("… the washing-up", "do"), ("… the bed", "make"), ("… your homework", "do"),
                          ("… a mistake", "make")], "do of make?", W),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "My hairs are very long.", "My hair is very long.", WL),
                 ("kort", "This trousers is too short.", "These trousers are too short.", WL),
                 ("kort", "I need two breads, please.", "I need two loaves of bread, please.", WL),
                 ("kort", "She is wearing two reds jackets.", "She is wearing two red jackets.", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Omcirkel het juiste antwoord.",
             oefeningen=[
                 ("waar", "De first floor van een Brits gebouw is ons gelijkvloers.", False),
                 ("waar", "Een starter is op een Engelse menukaart het voorgerecht.", True),
                 ("waar", "Het Engelse woord arm kan je ook gebruiken voor iemand met weinig geld.", False),
                 ("waar", "Nationaliteiten schrijf je in het Engels met een hoofdletter.", True),
                 ("waar", "Washing-up liquid is waspoeder voor de machine.", False),
             ]),
        echte_leven(
            "Loop één dag rond met je telefoon en noteer in het Engels tien dingen die je aanraakt of "
            "gebruikt: meubels, kleren, eten, gerief. Ken je het woord niet, zoek het dan op. Zeg ze de dag "
            "erna hardop op zonder je lijstje.",
            "Vrij antwoord. Wie tien woorden opschrijft en er de dag erna zes onthoudt, doet het goed.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-woordvelden-school-werk-reizen-en-de-samenleving-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: school, werk, reizen en de samenleving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Instructietaal",
             opdracht="Schrijf bij elke opdracht wat je moet doen.",
             oefeningen=[
                 ("rij", [("Tick the correct box.", "het juiste vakje aankruisen"),
                          ("Underline the verb.", "het werkwoord onderlijnen"),
                          ("Circle the odd one out.", "het woord omcirkelen dat er niet bij hoort")],
                  "Wat doe je?", WL),
                 ("rij", [("Match the words with the pictures.", "elk woord verbinden met de juiste afbeelding"),
                          ("Fill in the gaps.", "de gaten in de tekst invullen"),
                          ("Summarise the text.", "de tekst samenvatten, dus zelf schrijven")],
                  "Wat doe je?", WL),
             ]),
        dict(kop="School",
             opdracht="Vul het Engelse woord in.",
             oefeningen=[
                 ("rij", [("het lessenrooster", "timetable"), ("een vak", "subject"),
                          ("een trimester", "term"), ("de directeur van een Britse school", "headteacher")],
                  "In het Engels", WW),
                 ("kort", "Hoe zeg je in het Engels dat je een examen aflegt?", "to sit an exam", WW),
                 ("kort", "En dat je het moet overdoen?", "to resit it", WW),
             ]),
        dict(kop="Beroepen",
             opdracht="Schrijf het Engelse beroep.",
             oefeningen=[
                 ("rij", [("loodgieter", "plumber"), ("chirurg", "surgeon"), ("vroedvrouw", "midwife"),
                          ("makelaar", "estate agent")], "In het Engels", WW),
                 ("rij", [("verpleegkundige", "nurse"), ("advocaat", "solicitor"), ("slager", "butcher"),
                          ("schrijnwerker", "carpenter")], "In het Engels", WW),
             ]),
        dict(kop="Werk",
             opdracht="Beantwoord kort.",
             oefeningen=[
                 ("kort", "Welk voorzetsel hoort bij apply … a job?", "for", W),
                 ("kort", "Iemand zegt: I resigned last month. Wat is er gebeurd?", "die persoon nam zelf ontslag", WL),
                 ("kort", "En bij I was made redundant?", "die persoon werd ontslagen", WL),
                 ("kort", "Waarom kan je niet two works zeggen?", "work is ontelbaar; een baan is a job", WL),
             ]),
        dict(kop="Onderweg en in de winkel",
             opdracht="Vul in of beantwoord kort.",
             oefeningen=[
                 ("kort", "Je wil heen en terug met de trein. Welk ticket vraag je in het VK?", "a return ticket", WW),
                 ("kort", "Wat is een subway in het Verenigd Koninkrijk?", "een tunnel voor voetgangers", WL),
                 ("kort", "Op het bord staat: delayed by 20 minutes. Wat betekent dat?", "twintig minuten vertraging", WL),
                 ("kort", "Je koopt iets dat stuk blijkt. Wat vraag je in de winkel?", "a refund", W),
                 ("kort", "Wat heb je daarvoor nodig?", "your receipt", W),
                 ("kort", "Waar koop je in het VK kranten en tijdschriften?", "at the newsagent's", WW),
             ]),
        dict(kop="Weer en tijd",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("motregen", "drizzle"), ("mistig", "foggy"), ("ijskoud", "freezing"),
                          ("de weersvoorspelling", "the weather forecast")], "In het Engels", WW),
                 ("rij", [("half past seven", "7.30"), ("quarter to nine", "8.45"),
                          ("quarter past six", "6.15"), ("a fortnight", "twee weken")], "Hoe laat of hoe lang?", WW),
             ]),
        dict(kop="Play, go of do?",
             opdracht="Vul het juiste werkwoord in.",
             oefeningen=[
                 ("rij", [("… football", "play"), ("… swimming", "go"), ("… yoga", "do"),
                          ("… tennis", "play")], "play, go of do?", W),
             ]),
        echte_leven(
            "Bel of mail in het Engels naar een jeugdherberg, een museum of een festival in een Engelstalig "
            "land met één echte vraag. Schrijf hieronder op wat je gevraagd hebt en wat je geantwoord kreeg.",
            "Vrij antwoord. Mailen mag, bellen leert meer: dan moet je ook luisteren.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-nouns-articles-quantifiers-en-numerals-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Nouns, articles, quantifiers en numerals",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het meervoud",
             opdracht="Schrijf het meervoud.",
             oefeningen=[
                 ("rij", [("country", "countries"), ("key", "keys"), ("leaf", "leaves"), ("box", "boxes")],
                  "Meervoud", WW),
                 ("rij", [("potato", "potatoes"), ("photo", "photos"), ("crisis", "crises"), ("wolf", "wolves")],
                  "Meervoud", WW),
                 ("rij", [("man", "men"), ("tooth", "teeth"), ("goose", "geese"), ("person", "people")],
                  "Meervoud", WW),
                 ("rij", [("sheep", "sheep"), ("fish", "fish"), ("series", "series"), ("toothbrush", "toothbrushes")],
                  "Meervoud", WW),
             ]),
        dict(kop="Telbaar of ontelbaar?",
             opdracht="Schrijf T bij een telbaar woord en O bij een ontelbaar.",
             oefeningen=[
                 ("rij", [("advice", "O"), ("chair", "T"), ("furniture", "O"), ("suitcase", "T")], "T of O?", W),
                 ("rij", [("news", "O"), ("job", "T"), ("work", "O"), ("information", "O")], "T of O?", W),
             ]),
        dict(kop="De bezitsvorm",
             opdracht="Schrijf de Engelse woordgroep.",
             oefeningen=[
                 ("rij", [("de fiets van mijn broer", "my brother's bike"),
                          ("de kamer van de meisjes (meer dan één)", "the girls' room"),
                          ("het speelgoed van de kinderen", "the children's toys"),
                          ("het dak van het huis", "the roof of the house")], "In het Engels", WL),
             ]),
        dict(kop="A, an, the of niets?",
             opdracht="Vul in. Schrijf een streepje als er niets hoort.",
             oefeningen=[
                 ("rij", [("She is … nurse.", "a"), ("We waited … hour.", "an"),
                          ("He studies … history.", "—"), ("I speak … English.", "—")], "Vul in", W),
                 ("rij", [("She goes to … university in Leeds.", "a"), ("… book you lent me was great.", "The"),
                          ("He is … honest man.", "an"), ("I like … music.", "—")], "Vul in", W),
             ]),
        dict(kop="Much, many, a few of a little?",
             opdracht="Vul het juiste woord in.",
             oefeningen=[
                 ("rij", [("How … water do you need?", "much"), ("How … books did you buy?", "many"),
                          ("I have … friends in Leeds.", "a few"), ("Add … salt.", "a little")], "Vul in", W),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "He is teacher in a primary school.", "He is a teacher in a primary school.", WL),
                 ("kort", "There is a lot of people in the queue.", "There are a lot of people in the queue.", WL),
                 ("kort", "The news are good today.", "The news is good today.", WL),
                 ("kort", "Is there some milk left?", "Is there any milk left?", WL),
                 ("kort", "I need two informations.", "I need two pieces of information.", WL),
             ]),
        dict(kop="Telwoorden en getallen",
             opdracht="Schrijf voluit of beantwoord kort.",
             oefeningen=[
                 ("rij", [("3de", "third"), ("5de", "fifth"), ("9de", "ninth"), ("12de", "twelfth")],
                  "Rangtelwoord", WW),
                 ("kort", "Schrijf 1,250 voluit zoals een Brit het leest.", "one thousand two hundred and fifty", WL),
                 ("kort", "Hoe schrijf je het getal 3,5 in het Engels?", "3.5", W),
                 ("kort", "Waarom is 'two thousands people' fout?", "na een getal krijgt thousand geen meervouds-s", WL),
             ]),
        echte_leven(
            "Luister naar een Engelstalig sportverslag of weerbericht en schrijf vijf getallen op die je "
            "hoort, in cijfers én voluit. Let op de punt en de komma.",
            "Vrij antwoord. Grote getallen en decimalen zijn wat je in een verslag het vaakst mist.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-pronouns-de-zeven-soorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Pronouns: de zeven soorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort?",
             opdracht="Schrijf bij elk woord welke soort voornaamwoord het is: persoonlijk, bezittelijk, "
                      "wederkerend, aanwijzend, vragend, betrekkelijk of onbepaald.",
             oefeningen=[
                 ("rij", [("them", "persoonlijk"), ("hers", "bezittelijk"), ("themselves", "wederkerend"),
                          ("those", "aanwijzend")], "Welke soort?", WW),
                 ("rij", [("whose", "vragend of betrekkelijk"), ("which", "vragend of betrekkelijk"),
                          ("nobody", "onbepaald"), ("each", "onbepaald")], "Welke soort?", WW),
             ]),
        dict(kop="Vul het juiste voornaamwoord in",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("… and I went to Cork.", "She (of He)"), ("This present is for … .", "her (of him)"),
                          ("The cat licked … paw.", "its"), ("Is this bag …?", "yours")], "Vul in", WW),
                 ("rij", [("He cut … while cooking.", "himself"), ("We painted the room … .", "ourselves"),
                          ("… shoes over there are mine.", "Those"), ("… bag is this?", "Whose")], "Vul in", WW),
             ]),
        dict(kop="Its of it's?",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("The dog wagged … tail.", "its"), ("… raining again.", "It's"),
                          ("The house and … garden are for sale.", "its"), ("… been a long day.", "It's")],
                  "its of it's?", W),
             ]),
        dict(kop="Betrekkelijke bijzinnen",
             opdracht="Vul who, which, that, whose, where of when in. Soms is er meer dan één mogelijkheid.",
             oefeningen=[
                 ("rij", [("The woman … lives next door is a vet.", "who (of that)"),
                          ("The shop … sells old records is closed.", "which (of that)"),
                          ("This is the town … I grew up.", "where"),
                          ("I remember the day … we met.", "when")], "Vul in", WW),
                 ("kort", "In welke zin mag het betrekkelijk voornaamwoord weg? The book that I read / The man who called me.",
                  "in The book that I read, want er volgt meteen een nieuw onderwerp", WL),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "Her and me went to the cinema.", "She and I went to the cinema.", WL),
                 ("kort", "They did it theirselves.", "They did it themselves.", WL),
                 ("kort", "I didn't see nothing.", "I didn't see anything.", WL),
                 ("kort", "Everybody were there on time.", "Everybody was there on time.", WL),
                 ("kort", "The film what I saw was long.", "The film that I saw was long.", WL),
                 ("kort", "Is this yours book?", "Is this your book?", WL),
             ]),
        dict(kop="Maak de zin duidelijk",
             opdracht="Schrijf de zin zo over dat er geen twijfel meer is naar wie verwezen wordt.",
             oefeningen=[
                 ("open", "Tom told Ben that he had passed.",
                  "Bijvoorbeeld: Tom told Ben that Ben had passed. (of: … that Tom himself had passed.) "
                  "Herhaal de naam zodra twee antwoorden even goed passen.", 3),
                 ("open", "The teachers helped the pupils, and they thanked them.",
                  "Bijvoorbeeld: The teachers helped the pupils, and the pupils thanked them.", 3),
             ]),
        echte_leven(
            "Neem een Engelstalige tekst van één bladzijde. Onderstreep elk voornaamwoord en teken een pijl "
            "naar het woord waar het naar verwijst. Blijft er één over waar je twijfelt, schrijf die zin dan "
            "hieronder op.",
            "Vrij antwoord. Twijfel ontstaat bijna altijd als twee mogelijke antwoorden hetzelfde geslacht of "
            "hetzelfde getal hebben.", 6),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-adjectives-adverbs-comparatives-en-voorzetsels-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Adjectives, adverbs, comparatives en voorzetsels",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Maak het bijwoord",
             opdracht="Schrijf het bijwoord bij het bijvoeglijk naamwoord.",
             oefeningen=[
                 ("rij", [("careful", "carefully"), ("easy", "easily"), ("terrible", "terribly"),
                          ("good", "well")], "Bijwoord", WW),
                 ("rij", [("angry", "angrily"), ("simple", "simply"), ("fast", "fast"), ("hard", "hard")],
                  "Bijwoord", WW),
             ]),
        dict(kop="Bijvoeglijk naamwoord of bijwoord?",
             opdracht="Omcirkel het juiste woord en schrijf het in.",
             oefeningen=[
                 ("rij", [("She sings (good / well).", "well"), ("The soup tastes (delicious / deliciously).", "delicious"),
                          ("Drive (careful / carefully)!", "carefully"), ("He looks (happy / happily).", "happy")],
                  "Het juiste woord", WW),
             ]),
        dict(kop="Hard of hardly?",
             opdracht="Vul in en schrijf erachter wat de zin betekent.",
             oefeningen=[
                 ("kort", "She has worked … all week and she is exhausted.", "hard — ze heeft hard gewerkt", WL),
                 ("kort", "He has … worked this week, so he has no excuse.", "hardly — hij heeft bijna niets gedaan", WL),
                 ("kort", "I haven't seen her … . (de laatste tijd)", "lately", W),
             ]),
        dict(kop="Vergelijken",
             opdracht="Schrijf de vergrotende en de overtreffende trap.",
             oefeningen=[
                 ("tabel", ["Woord", "Vergrotende trap", "Overtreffende trap"],
                  [["big", None, None], ["easy", None, None], ["expensive", None, None],
                   ["good", None, None], ["bad", None, None]],
                  "bigger / biggest — easier / easiest — more expensive / the most expensive — "
                  "better / best — worse / worst", WW),
                 ("kort", "Wat betekent: This test is not as hard as the last one?", "deze toets is makkelijker", WL),
                 ("kort", "Vul aan: The more you practise, … it gets. (easy)", "the easier", WW),
             ]),
        dict(kop="At, on of in?",
             opdracht="Vul het juiste voorzetsel van tijd in.",
             oefeningen=[
                 ("rij", [("… seven o'clock", "at"), ("… Monday", "on"), ("… July", "in"), ("… night", "at")],
                  "Vul in", W),
                 ("rij", [("… 2027", "in"), ("… 14 March", "on"), ("… the morning", "in"),
                          ("… Friday morning", "on")], "Vul in", W),
             ]),
        dict(kop="Vaste voorzetsels",
             opdracht="Vul het voorzetsel in. Schrijf een streepje als er geen hoort.",
             oefeningen=[
                 ("rij", [("wait … the bus", "for"), ("listen … music", "to"), ("good … maths", "at"),
                          ("afraid … spiders", "of")], "Vul in", W),
                 ("rij", [("married … him", "to"), ("interested … history", "in"), ("discuss … the problem", "—"),
                          ("arrive … London", "in")], "Vul in", W),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "She has two reds cars.", "She has two red cars.", WL),
                 ("kort", "He runs very fastly.", "He runs very fast.", WL),
                 ("kort", "This one is very better.", "This one is much better.", WL),
                 ("kort", "She is taller than me by far, as tall than her sister.", "She is taller than me by far, as tall as her sister.", WL),
                 ("kort", "We arrived to the station at six.", "We arrived at the station at six.", WL),
             ]),
        echte_leven(
            "Beschrijf aan iemand, in het Engels en in één minuut, de kamer waarin je zit. Gebruik minstens "
            "vijf bijvoeglijke naamwoorden en drie voorzetsels van plaats. Schrijf achteraf op welke drie "
            "woorden je niet vond.",
            "Vrij antwoord. De woorden die je niet vindt, zijn precies de woorden die je moet opzoeken.", 6),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-tegenwoordige-tijden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De tegenwoordige tijden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Present simple",
             opdracht="Zet het werkwoord in de derde persoon enkelvoud.",
             oefeningen=[
                 ("rij", [("to watch", "watches"), ("to fly", "flies"), ("to play", "plays"),
                          ("to go", "goes")], "He of she …", WW),
                 ("rij", [("to do", "does"), ("to miss", "misses"), ("to carry", "carries"),
                          ("to fix", "fixes")], "He of she …", WW),
             ]),
        dict(kop="Present simple of present continuous?",
             opdracht="Zet het werkwoord tussen haakjes in de juiste tijd.",
             oefeningen=[
                 ("rij", [("Look! It (rain).", "is raining"), ("It (rain) a lot in Belgium.", "rains"),
                          ("I (work) in a shop every Saturday.", "work"),
                          ("She (write) a letter right now.", "is writing")], "Juiste vorm", WW),
                 ("rij", [("I (know) the answer.", "know"), ("They (wait) outside at the moment.", "are waiting"),
                          ("We (meet) at six tonight, it's arranged.", "are meeting"),
                          ("The sun (rise) in the east.", "rises")], "Juiste vorm", WW),
             ]),
        dict(kop="De -ing-vorm",
             opdracht="Schrijf de -ing-vorm.",
             oefeningen=[
                 ("rij", [("sit", "sitting"), ("write", "writing"), ("lie", "lying"), ("begin", "beginning")],
                  "-ing-vorm", WW),
             ]),
        dict(kop="Present perfect",
             opdracht="Vul in of vertaal.",
             oefeningen=[
                 ("kort", "Vertaal: Ik woon sinds 2020 in Antwerpen.", "I have lived in Antwerp since 2020.", WL),
                 ("kort", "Vertaal: Ik ben mijn sleutels kwijt.", "I have lost my keys.", WL),
                 ("rij", [("I have lived here … three years.", "for"), ("She has worked here … Monday.", "since"),
                          ("Have you finished …?", "yet"), ("I have … seen that film.", "already")],
                  "Vul in", W),
             ]),
        dict(kop="Present perfect of past simple?",
             opdracht="Zet het werkwoord tussen haakjes in de juiste tijd.",
             oefeningen=[
                 ("rij", [("I (see) her yesterday.", "saw"), ("I (know) him for years.", "have known"),
                          ("We (move) house in 2019.", "moved"),
                          ("She (call) me two hours ago.", "called")], "Juiste vorm", WW),
                 ("kort", "Waarom is 'I have been to London last year' fout?",
                  "last year is een afgesloten tijd, dus past simple: I went to London last year", WL),
                 ("kort", "Waarom is 'When have you arrived?' fout?",
                  "when vraagt naar een precies moment: When did you arrive?", WL),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "Does she lives here?", "Does she live here?", WL),
                 ("kort", "There is three books on the table.", "There are three books on the table.", WL),
                 ("kort", "I am knowing the answer.", "I know the answer.", WL),
                 ("kort", "Have you ever ate sushi?", "Have you ever eaten sushi?", WL),
                 ("kort", "I have been knowing her for years.", "I have known her for years.", WL),
                 ("kort", "How long are you learning English?", "How long have you been learning English?", WL),
             ]),
        echte_leven(
            "Vertel aan iemand, in het Engels, wat je vandaag al gedaan hebt en wat je nu aan het doen bent. "
            "Gebruik minstens één present perfect en één present continuous. Schrijf hieronder de twee zinnen "
            "op die je gezegd hebt.",
            "Vrij antwoord. Bijvoorbeeld: I have finished my homework. I am waiting for dinner.", 6),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-verleden-en-de-toekomende-tijden-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De verleden en de toekomende tijden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie vormen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Basisvorm", "Verleden tijd", "Voltooid deelwoord"],
                  [["go", None, None], ["see", None, None], ["take", None, None], ["write", None, None],
                   ["buy", None, None], ["drink", None, None], ["bring", None, None]],
                  "went gone — saw seen — took taken — wrote written — bought bought — drank drunk — "
                  "brought brought", WW),
             ]),
        dict(kop="Regelmatige past simple",
             opdracht="Schrijf de verleden tijd.",
             oefeningen=[
                 ("rij", [("study", "studied"), ("stop", "stopped"), ("like", "liked"), ("travel", "travelled")],
                  "Past simple", WW),
             ]),
        dict(kop="Past simple of past continuous?",
             opdracht="Zet het werkwoord tussen haakjes in de juiste tijd.",
             oefeningen=[
                 ("rij", [("I (read) when the phone rang.", "was reading"),
                          ("While we (wait), it started to rain.", "were waiting"),
                          ("She (cook) while he was setting the table.", "was cooking"),
                          ("He (arrive) at eight.", "arrived")], "Juiste vorm", WW),
             ]),
        dict(kop="Past perfect",
             opdracht="Vul de past perfect in en beantwoord de vraag.",
             oefeningen=[
                 ("rij", [("The train (leave) already when we arrived.", "had left"),
                          ("By the time she called, I (go) to bed.", "had gone"),
                          ("She (never see) the sea before that trip.", "had never seen")], "Juiste vorm", WW),
                 ("kort", "When I got home, my brother had cooked dinner. Wie deed wat eerst?",
                  "hij kookte eerst, daarna kwam ik thuis", WL),
                 ("kort", "Waarom hoeft 'Yesterday I walked to school' geen past perfect?",
                  "er is geen tweede, later moment om mee te vergelijken", WL),
             ]),
        dict(kop="Will of going to?",
             opdracht="Vul in en schrijf er in één woord bij waarom.",
             oefeningen=[
                 ("kort", "That bag looks heavy. I … help you.", "will (beslissing op het moment zelf)", WL),
                 ("kort", "I … study medicine, that's been my plan for years.", "am going to (een plan)", WL),
                 ("kort", "Look at those clouds. It … rain.", "is going to (voorspelling met bewijs)", WL),
                 ("kort", "I promise I … tell anyone.", "won't (een belofte)", WL),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "She didn't came yesterday.", "She didn't come yesterday.", WL),
                 ("kort", "Did you was there?", "Were you there?", WL),
                 ("kort", "I was knowing the answer.", "I knew the answer.", WL),
                 ("kort", "She will to come tomorrow.", "She will come tomorrow.", WL),
                 ("kort", "She won't can come tomorrow.", "She won't be able to come tomorrow.", WL),
                 ("kort", "I will call you when I will arrive.", "I will call you when I arrive.", WL),
                 ("kort", "If it will rain, we will stay at home.", "If it rains, we will stay at home.", WL),
             ]),
        echte_leven(
            "Vertel aan iemand in het Engels wat je vorig weekend gedaan hebt en wat je volgend weekend van "
            "plan bent. Gebruik minstens één past simple, één past continuous en één going to. Schrijf de "
            "drie zinnen hieronder op.",
            "Vrij antwoord. Bijvoorbeeld: I went to my grandmother's. It was raining all afternoon. Next "
            "weekend I am going to visit my cousin.", 7),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-modal-auxiliaries-imperative-en-infinitive-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Modal auxiliaries, imperative en infinitive",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat doet het modale werkwoord?",
             opdracht="Schrijf bij elke zin wat het modale werkwoord uitdrukt: kunnen, toestemming, "
                      "verplichting, verbod, advies, mogelijkheid of conclusie.",
             oefeningen=[
                 ("rij", [("She can swim.", "kunnen"), ("May I leave early?", "toestemming"),
                          ("You must wear a helmet.", "verplichting"),
                          ("You mustn't park here.", "verbod")], "Wat drukt het uit?", WW),
                 ("rij", [("You should see a doctor.", "advies"), ("It might rain tomorrow.", "mogelijkheid"),
                          ("He must be exhausted.", "conclusie"),
                          ("That can't be true.", "conclusie (het tegendeel)")], "Wat drukt het uit?", WW),
             ]),
        dict(kop="Mustn't of don't have to?",
             opdracht="Vul in en schrijf er de Nederlandse betekenis bij.",
             oefeningen=[
                 ("kort", "You … come if you are tired. (het hoeft niet)", "don't have to — je hoeft niet te komen", WL),
                 ("kort", "You … touch that, it's dangerous. (het is verboden)", "mustn't — je mag dat niet aanraken", WL),
                 ("kort", "Zet in de verleden tijd: I must go.", "I had to go.", WL),
             ]),
        dict(kop="Gebiedende wijs",
             opdracht="Schrijf de gevraagde zin in het Engels.",
             oefeningen=[
                 ("rij", [("Doe de deur dicht.", "Close the door."), ("Doe het raam niet open.", "Don't open the window."),
                          ("Laten we vanavond naar de film gaan.", "Let's go to the cinema tonight."),
                          ("Ga zitten, alsjeblieft.", "Please sit down.")], "In het Engels", WL),
             ]),
        dict(kop="To, kaal of -ing?",
             opdracht="Zet het werkwoord tussen haakjes in de juiste vorm.",
             oefeningen=[
                 ("rij", [("I want (go) home.", "to go"), ("She made me (laugh).", "laugh"),
                          ("I enjoy (read) books.", "reading"), ("He left without (say) goodbye.", "saying")],
                  "Juiste vorm", WW),
                 ("rij", [("She is good at (draw).", "drawing"), ("Let him (go).", "go"),
                          ("I hope (see) you soon.", "to see"), ("I look forward to (hear) from you.", "hearing")],
                  "Juiste vorm", WW),
             ]),
        dict(kop="De nadrukkelijke do",
             opdracht="Schrijf bij elke zin of de do nadruk geeft (N) of een gewone vraag of ontkenning vormt (G).",
             oefeningen=[
                 ("rij", [("I do like your new coat.", "N"), ("Do you want tea?", "G"),
                          ("She does look tired.", "N"), ("He doesn't live here.", "G")], "N of G?", W),
             ]),
        dict(kop="Verbeter de zin",
             opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
             oefeningen=[
                 ("kort", "She cans swim very well.", "She can swim very well.", WL),
                 ("kort", "She can to swim very well.", "She can swim very well.", WL),
                 ("kort", "Please to sit down.", "Please sit down.", WL),
                 ("kort", "I look forward to hear from you.", "I look forward to hearing from you.", WL),
                 ("kort", "Enjoy you at the party!", "Enjoy yourself at the party!", WL),
                 ("kort", "Is raining today.", "It is raining today.", WL),
                 ("kort", "Takes an hour to get there.", "It takes an hour to get there.", WL),
             ]),
        echte_leven(
            "Vraag iemand in het Engels om je met iets te helpen, op drie manieren: met can, met could en "
            "met would you mind. Vraag daarna aan die persoon welke van de drie het vriendelijkst klonk, en "
            "schrijf het antwoord hieronder op.",
            "Vrij antwoord. Meestal komt could of would you mind er als vriendelijkst uit; can klinkt vlot "
            "maar direct.", 6),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-zinsdelen-soorten-zinnen-en-bijzinnen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Zinsdelen, soorten zinnen en bijzinnen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De zinsdelen",
             opdracht="Vul de tabel aan met de Engelse woorden uit de zin.",
             oefeningen=[
                 ("tabel", ["Zin", "Onderwerp", "Persoonsvorm", "Lijdend voorwerp"],
                  [["My little sister reads three books a week.", None, None, None],
                   ["The children were playing football.", None, None, None],
                   ["She wrote a long letter.", None, None, None]],
                  "My little sister / reads / three books — The children / were / football — "
                  "She / wrote / a long letter", W),
                 ("kort", "Wat is het meewerkend voorwerp in: He gave his friend a present?", "his friend", WW),
                 ("kort", "Schrijf die zin met to erbij.", "He gave a present to his friend.", WL),
             ]),
        dict(kop="De woordvolgorde",
             opdracht="Zet de woorden in de juiste volgorde.",
             oefeningen=[
                 ("kort", "very much / this film / I like", "I like this film very much.", WL),
                 ("kort", "last night / at the concert / she sang / beautifully", "She sang beautifully at the concert last night.", WL),
                 ("kort", "home / I / yesterday / went", "Yesterday I went home.", WL),
             ]),
        dict(kop="Welk soort zin?",
             opdracht="Schrijf bij elke zin het soort: mededelend, ontkennend, vragend, bevelend of uitroepend.",
             oefeningen=[
                 ("rij", [("She plays tennis.", "mededelend"), ("She doesn't want to go.", "ontkennend"),
                          ("Does she play tennis?", "vragend")], "Welk soort?", WW),
                 ("rij", [("Close the door.", "bevelend"), ("What a beautiful garden!", "uitroepend"),
                          ("How fast she runs!", "uitroepend")], "Welk soort?", WW),
             ]),
        dict(kop="Maak er een vraag van",
             opdracht="Schrijf de vraag.",
             oefeningen=[
                 ("rij", [("She plays tennis.", "Does she play tennis?"), ("He can swim.", "Can he swim?"),
                          ("They have finished.", "Have they finished?"),
                          ("You are coming tonight.", "Are you coming tonight?")], "De vraag", WL),
                 ("kort", "Vul de aanhangvraag aan: You're coming tonight, …?", "aren't you", WW),
             ]),
        dict(kop="Is of are?",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("The news … good.", "is"), ("Everybody … here.", "is"),
                          ("The police … looking for him.", "are"),
                          ("One of my friends … coming tonight.", "is")], "is of are?", W),
             ]),
        dict(kop="Voegwoorden",
             opdracht="Vul het juiste voegwoord in: because, so, but, although of unless.",
             oefeningen=[
                 ("rij", [("I stayed at home … it was raining.", "because"),
                          ("It was raining, … I stayed at home.", "so"),
                          ("She was tired, … she kept working.", "but"),
                          ("… she was tired, she kept working.", "Although")], "Vul in", WW),
                 ("kort", "… you hurry, you will miss the bus.", "Unless", W),
                 ("kort", "Wat betekent unless?", "if not", W),
             ]),
        dict(kop="Komma of geen komma?",
             opdracht="Beantwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent: The students who worked hard passed?",
                  "alleen de groep die hard werkte, slaagde", WL),
                 ("kort", "En: The students, who worked hard, passed?",
                  "ze werkten allemaal hard en slaagden allemaal", WL),
                 ("kort", "Waar staat de komma in: When I arrived she was asleep?",
                  "achter de bijzin: When I arrived, she was asleep.", WL),
             ]),
        dict(kop="Conditionals zero en first",
             opdracht="Schrijf bij elke zin of het een zero of een first is, en vul het werkwoord aan.",
             oefeningen=[
                 ("rij", [("If you mix blue and yellow, you (get) green.", "zero — get"),
                          ("If you study hard, you (pass).", "first — will pass"),
                          ("If you press this button, the light (go) on.", "zero — goes"),
                          ("If it rains, we (stay) at home.", "first — will stay")], "Zero of first, en de vorm", WL),
                 ("kort", "Waarom is 'If it will rain, we will stay at home' fout?",
                  "na if komt geen will; de will hoort in de hoofdzin", WL),
             ]),
        echte_leven(
            "Zoek een Engelstalige tekst van één bladzijde. Onderstreep vijf samengestelde zinnen en "
            "omcirkel in elk het voegwoord. Schrijf hieronder op welke drie voegwoorden het vaakst "
            "terugkwamen.",
            "Vrij antwoord. And, but en because zijn in bijna elke tekst de drie meest gebruikte.", 6),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-engelse-tekst-analyseren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Lees de tekst eerst één keer helemaal door zonder te stoppen bij woorden die je "
                    "niet kent. Pas daarna lees je met de vragen ernaast.",
             waarom=[
                 None,
                 "Het onderwerp schrijf je in enkele woorden, de hoofdgedachte in één hele zin. Dat is "
                 "het verschil tussen waarover het gaat en wat de tekst erover zegt.",
                 None,
                 None,
                 "Dit staat er niet letterlijk; je leidt het af uit twee zinnen samen. Zeg er dus altijd "
                 "bij waaruit je het haalt.",
                 None,
             ]),
        dict(aanpak="Zoek bij een beoordeling eerst het algemene oordeel, en daarna de zinnen die ervan "
                    "afwijken. Juist die nuance is wat gevraagd wordt.",
             waarom=[None, None, None, None]),
        dict(aanpak="Let op het woordje dat het verschil maakt: unlike, who, on … and on. Daar hangt de "
                    "hele afleiding aan.",
             waarom=[None, None, None, None]),
        dict(aanpak="Let op de woorden altijd, alleen en eerst. Daar zit meestal het verschil tussen "
                    "waar en niet waar.",
             waarom=[
                 "Net omgekeerd: het onderwerp in enkele woorden, de hoofdgedachte in een hele zin.",
                 None,
                 "Vertalen is traag en meestal niet nodig. Je leest gericht naar wat de vraag vraagt.",
                 None,
                 None,
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Eén keer kijken zonder "
                    "ondertitels is het punt van de opdracht.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-tekstverbanden-en-verwijswoorden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elk fragment af wat het van je wil: iets laten doen, iets laten "
                    "weten, overtuigen, vertellen of iets laten voelen.",
             waarom=[None, None]),
        dict(aanpak="Leer de signaalwoorden per verband in groepjes. Zo herken je ook een woord dat je "
                    "nog nooit zag aan de plaats waar het staat.",
             waarom=[None, None, None]),
        dict(aanpak="Let niet alleen op de betekenis maar ook op de bouw: although en since krijgen een "
                    "hele zin achter zich, despite en because of een naamwoord.",
             waarom=[None, None, None, None]),
        dict(aanpak="Zoek bij een verwijswoord altijd terug in de tekst. Let erop dat this en it ook "
                    "naar een hele zin kunnen verwijzen, niet enkel naar één woord.",
             waarom=[None, None, None, None]),
        dict(aanpak="Let op de woorden alleen en hetzelfde. Een signaalwoord stuurt de lezer; het is "
                    "geen versiering.",
             waarom=[
                 None,
                 "Signaalwoorden leggen verbanden. Haal ze weg en de lezer moet zelf raden hoe de zinnen "
                 "samenhangen.",
                 None,
                 "Therefore legt een gevolg, however een tegenstelling. Dat zijn twee heel verschillende "
                 "verbanden.",
                 None,
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Noteer de signaalwoorden "
                    "terwijl je luistert, niet achteraf.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-de-engelstalige-wereld-gewoontes-en-conventies-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Leer de woordparen samen, als paar. Zo weet je meteen welke variant je voor je "
                    "hebt, en dat helpt bij het lezen.",
             waarom=[None, None]),
        dict(aanpak="De Britse spelling houdt -our, -re en de dubbele l. De Amerikaanse maakt het "
                    "korter.",
             waarom=[None]),
        dict(aanpak="Let bij praktische teksten op de conventies: verdiepingen, datums, graden en "
                    "afstanden lopen niet gelijk met de onze.",
             waarom=[
                 "In het Brits is the ground floor het gelijkvloers en the first floor de verdieping "
                 "erboven. In het Amerikaans is the first floor het gelijkvloers.",
                 "In het Brits staat de dag eerst, in het Amerikaans de maand. Dezelfde datum kan dus "
                 "twee dingen betekenen.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Aanhef en afsluiter horen bij elkaar: ken je de naam, dan Yours sincerely; ken je "
                    "ze niet, dan Yours faithfully.",
             waarom=[None, None]),
        dict(aanpak="Beleefdheid zit in het Engels in de vorm: could, would en please maken van een "
                    "bevel een vraag.",
             waarom=[None, None, None, None]),
        dict(aanpak="Leer de feesten met hun datum én hun land erbij. Een datum alleen volstaat niet.",
             waarom=[None]),
        dict(aanpak="Let op de woorden hetzelfde en even vaak. Daar zitten de klassieke misverstanden.",
             waarom=[
                 "England is één land van Great Britain, naast Scotland en Wales. Voeg je Northern "
                 "Ireland toe, dan krijg je the United Kingdom.",
                 "Kies er één en houd die vol in heel je tekst. Door elkaar gebruiken telt wel als "
                 "fout.",
                 None,
                 None,
                 "In het Engels gebruik je please en thank you veel vaker dan bij ons: ook voor kleine "
                 "dingen, en ook tegen mensen die je goed kent.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Noteer terwijl je kijkt, "
                    "niet achteraf uit het hoofd.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-schriftelijke-interactie-en-literatuurbeleving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elke situatie af wat je met je tekst wil bereiken. Dat doel bepaalt "
                    "je opbouw én je toon.",
             waarom=[None, None]),
        dict(aanpak="Leer deze zinnen als vaste bouwstenen. Op een examen heb je ze zo klaar en hoef je "
                    "niets meer te bedenken.",
             waarom=[None, None, None, None, None, None]),
        dict(aanpak="Je punten komen uit vier hoeken tegelijk. Loop ze na voor je indient, niet enkel "
                    "de spelling.",
             waarom=[
                 None,
                 None,
                 "De opgegeven lengte hoort bij de opdracht. Met de helft van de woorden kan je de taak "
                 "niet volledig uitvoeren, ook al is elk woord juist.",
             ]),
        dict(aanpak="Ken je een woord niet, omschrijf het dan met woorden die je wel kent. Een zin half "
                    "laten staan kost meer punten dan een omweg.",
             waarom=[None, None, None, None]),
        dict(aanpak="Een samenvatting zegt wat er in het boek staat; een leeservaring zegt wat het met "
                    "jou deed. Let op het woordje I.",
             waarom=[None]),
        dict(aanpak="Vink af wat gevraagd wordt voor je begint, en tel achteraf je woorden. Bij "
                    "interactie beantwoord je élke vraag van de ander.",
             waarom=[None, None]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Waar de voorlezer hapert, "
                    "loopt je zin niet.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-mensen-gezondheid-en-het-dagelijkse-leven-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Teken een stamboompje. Dan zie je meteen wie langs welke kant staat en welk woord "
                    "erbij hoort.",
             waarom=[
                 "Nephew en niece gaan een trapje omlaag (het kind van je broer of zus), cousin gaat "
                 "opzij (het kind van je tante of oom).",
                 "In-law betekent aangetrouwd, step- betekent stief. Twee verschillende dingen.",
             ]),
        dict(aanpak="De woorden van een formulier leer je als groep: je komt ze op elk formulier "
                    "opnieuw tegen.",
             waarom=[None]),
        dict(aanpak="Leer gevoelswoorden met hun tegengestelde erbij, en pijnklachten met hun vaste "
                    "uitdrukking.",
             waarom=[None, None, None, None, None]),
        dict(aanpak="Loop in gedachten je lichaam af van boven naar beneden en benoem elk deel in het "
                    "Engels.",
             waarom=[None, None]),
        dict(aanpak="De vuistregel: do bij werk en taken, make bij iets wat je maakt of voortbrengt. De "
                    "uitzonderingen leer je als vaste uitdrukking.",
             waarom=[None]),
        dict(aanpak="Zoek eerst welke regel geschonden wordt: een ontelbaar woord, een meervoudig "
                    "kledingstuk, of een bijvoeglijk naamwoord dat geen -s krijgt.",
             waarom=[
                 "Hair is ontelbaar, net als water en bread: nooit een -s en het werkwoord in het "
                 "enkelvoud.",
                 "Trousers bestaat alleen in het meervoud, dus these en are.",
                 None,
                 "Een bijvoeglijk naamwoord krijgt in het Engels nooit een meervouds-s.",
             ]),
        dict(aanpak="Let bij deze uitspraken op de valse vrienden en op de Britse gewoontes.",
             waarom=[
                 "The ground floor is het gelijkvloers; the first floor ligt daarboven.",
                 None,
                 "Arm betekent in het Engels de arm van je lichaam. Weinig geld hebben is poor.",
                 None,
                 "Washing-up liquid is afwasmiddel voor met de hand. Waspoeder is washing powder of "
                 "detergent.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Woorden die je elke dag "
                    "aanraakt, blijven het best hangen.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-reizen-en-de-samenleving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Instructietaal is de taal van de opgave zelf. Ken je die niet, dan verlies je "
                    "punten op een oefening die je eigenlijk kon.",
             waarom=[None, None]),
        dict(aanpak="Schoolwoorden verschillen tussen Brits en Amerikaans. Leer de Britse vorm, met de "
                    "vaste werkwoorden erbij.",
             waarom=[None, None, None]),
        dict(aanpak="Leer beroepen in groepjes per sector. Veel ervan lijken niet op het Nederlandse "
                    "woord, dus herhaling helpt.",
             waarom=[None, None]),
        dict(aanpak="Let bij werk op twee dingen: het vaste voorzetsel, en wie het ontslag neemt.",
             waarom=[
                 None,
                 None,
                 None,
                 "Work is ontelbaar, net als advice en information. Eén betrekking is a job.",
             ]),
        dict(aanpak="Leer de reiswoorden in de volgorde van de reis: ticket, perron, vertraging, en wat "
                    "je in een winkel nodig hebt.",
             waarom=[
                 None,
                 "Opgelet: in de Verenigde Staten is the subway de metro. In het Verenigd Koninkrijk is "
                 "dat the underground of the tube.",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Weerwoorden eindigen vaak op -y. Het uur zeg je met past en to, vanuit het hele "
                    "uur.",
             waarom=[None, None]),
        dict(aanpak="Onthoud de drie vaste combinaties: play bij een balsport of een spel, go bij een "
                    "sport op -ing, do bij de rest.",
             waarom=[None]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Bellen leert meer dan "
                    "mailen, want dan moet je ook luisteren.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-nouns-articles-quantifiers-en-numerals-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Het meervoud volgt vier groepen: de gewone -s, woorden op s/sh/ch/x met -es, een "
                    "medeklinker plus y wordt -ies, en f of fe wordt ves.",
             waarom=[
                 None,
                 "Potato krijgt -es, photo niet. Woorden die uit een andere taal komen, houden vaak "
                 "gewoon -s.",
                 "Man, tooth, goose en person zijn onregelmatig; die leer je uit het hoofd.",
                 "Sheep, fish en series blijven gelijk in het meervoud.",
             ]),
        dict(aanpak="Vraag je af of je er een getal voor kan zetten. Kan dat niet, dan is het "
                    "ontelbaar en krijgt het nooit een -s.",
             waarom=[None, None]),
        dict(aanpak="Bij personen gebruik je 's. Bij dingen zeg je meestal of the. In het meervoud "
                    "komt de apostrof na de -s.",
             waarom=[None]),
        dict(aanpak="A of an kies je op de klánk, niet op de letter. Bij een vak, een taal of iets in "
                    "het algemeen staat er geen lidwoord.",
             waarom=[None, None]),
        dict(aanpak="Much en a little horen bij ontelbare woorden, many en a few bij telbare.",
             waarom=[None]),
        dict(aanpak="Zoek bij elke zin eerst welke regel geschonden wordt. Daarna schrijf je de hele "
                    "zin correct over.",
             waarom=[
                 "Een beroep krijgt in het Engels altijd a of an.",
                 "People is een meervoud, dus there are.",
                 "News ziet eruit als een meervoud maar is ontelbaar: the news is.",
                 "In een vraag of een ontkenning gebruik je any; some blijft voor bevestigende zinnen.",
                 "Information is ontelbaar: je telt het met pieces of.",
             ]),
        dict(aanpak="De rangtelwoorden eindigen op -th, op first, second en third na. Let bij getallen "
                    "op de punt en de komma.",
             waarom=[
                 None,
                 None,
                 "In het Engels is de punt het decimaalteken en de komma het duizendtalteken. Bij ons is "
                 "dat net omgekeerd.",
                 None,
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Getallen zijn wat je in "
                    "gesproken Engels het snelst mist.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-pronouns-de-zeven-soorten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elk voornaamwoord af wat het doet: iemand vervangen, bezit aanduiden, "
                    "terugwijzen naar het onderwerp, aanwijzen, vragen of onbepaald laten.",
             waarom=[None, None]),
        dict(aanpak="Let op de plaats in de zin: vóór het werkwoord staat de onderwerpsvorm, erachter "
                    "de voorwerpsvorm.",
             waarom=[None, None]),
        dict(aanpak="Een ezelsbruggetje: kan je het lezen als it is, dan schrijf je it's. Anders its, "
                    "zonder apostrof.",
             waarom=[None]),
        dict(aanpak="Who gaat over personen, which over dingen, that over allebei. Where en when "
                    "verwijzen naar een plaats of een tijd.",
             waarom=[None, None]),
        dict(aanpak="Zoek bij elke zin eerst welke regel geschonden wordt, en schrijf dan de hele zin "
                    "over.",
             waarom=[
                 "Vóór het werkwoord hoort de onderwerpsvorm: she and I, niet her and me.",
                 "Theirselves bestaat niet; het is themselves.",
                 "In het Engels staat er maar één ontkenning per zin: didn't … anything.",
                 "Everybody, somebody en nobody zijn enkelvoud: was, niet were.",
                 "What kan geen betrekkelijk voornaamwoord zijn na een naamwoord; gebruik that of which.",
                 "Your staat vóór een naamwoord, yours staat alleen.",
             ]),
        dict(aanpak="Zodra twee antwoorden even goed passen, herhaal je gewoon de naam. Duidelijkheid "
                    "gaat voor elegantie.",
             waarom=[None, None]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Pijlen tekenen laat je "
                    "zelf zien waar de tekst wringt.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-adjectives-adverbs-comparatives-en-voorzetsels-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Een bijwoord krijgt meestal -ly. Een -y wordt -ily, een -le wordt -ly, en good "
                    "wordt well.",
             waarom=[
                 None,
                 "Fast en hard blijven gelijk. Hardly bestaat ook, maar betekent iets heel anders.",
             ]),
        dict(aanpak="Vraag je af waarover het woord iets zegt: over een naamwoord (bijvoeglijk) of over "
                    "het werkwoord (bijwoord). Na look, taste, feel en seem komt een bijvoeglijk "
                    "naamwoord.",
             waarom=[None]),
        dict(aanpak="Hard betekent hard of zwaar, hardly betekent nauwelijks. Dat is een "
                    "betekenisverschil, geen vormverschil.",
             waarom=[None, None, None]),
        dict(aanpak="Tot twee lettergrepen: -er en -est. Langer: more en the most. Good, bad en far "
                    "zijn onregelmatig.",
             waarom=[
                 None,
                 "Not as … as betekent minder dan. Deze toets is dus makkelijker dan de vorige.",
                 None,
             ]),
        dict(aanpak="De tijdsvoorzetsels gaan van groot naar klein: in voor een jaar of maand, on voor "
                    "een dag of datum, at voor een uur.",
             waarom=[None, None]),
        dict(aanpak="Vaste voorzetsels leer je samen met het woord, als één geheel. Ze volgen geen "
                    "regel.",
             waarom=[
                 None,
                 "Let op discuss: dat krijgt géén voorzetsel, anders dan het Nederlandse praten over.",
             ]),
        dict(aanpak="Zoek bij elke zin welke regel geschonden wordt, en schrijf de hele zin correct "
                    "over.",
             waarom=[
                 "Een bijvoeglijk naamwoord krijgt in het Engels nooit een meervouds-s.",
                 "Fast is al een bijwoord; fastly bestaat niet.",
                 "Een vergrotende trap versterk je met much of far, niet met very.",
                 "Gelijkheid gaat met as … as, een verschil met than.",
                 "Arrive gaat met at bij een plaats en met in bij een stad of land, nooit met to.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. De woorden die je niet "
                    "vindt, zijn precies de woorden die je moet opzoeken.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="In de derde persoon enkelvoud komt er -s bij. Na s, sh, ch, x en o wordt dat -es, "
                    "en een medeklinker plus y wordt -ies.",
             waarom=[None, None]),
        dict(aanpak="De present simple is voor wat altijd of gewoonlijk zo is, de continuous voor wat nu "
                    "aan het gebeuren is of al afgesproken staat.",
             waarom=[
                 None,
                 "Know is een werkwoord van denken en voelen: dat staat niet in de continuous. Hetzelfde "
                 "geldt voor like, want, understand en believe.",
             ]),
        dict(aanpak="Een korte klinker plus één medeklinker verdubbelt die medeklinker, een stomme -e "
                    "valt weg, en -ie wordt -ying.",
             waarom=[None]),
        dict(aanpak="De present perfect verbindt vroeger met nu: iets begon in het verleden en loopt "
                    "door, of het gevolg is nu nog te zien.",
             waarom=[
                 "In het Nederlands zeg je ik woon, in het Engels have lived: het is begonnen in 2020 en "
                 "nog altijd zo.",
                 "Je bent ze nog kwijt, dus het gevolg is er nu nog. Daarom geen past simple.",
                 "For staat bij een duur, since bij een beginpunt.",
             ]),
        dict(aanpak="Staat er een afgesloten tijd bij (yesterday, in 2019, two hours ago), dan is het "
                    "past simple. Loopt het door tot nu, dan present perfect.",
             waarom=[None, None, None]),
        dict(aanpak="Zoek bij elke zin welke regel geschonden wordt, en schrijf de hele zin correct over.",
             waarom=[
                 "Na does komt de kale vorm; de -s zit al in does.",
                 "Books is meervoud, dus there are.",
                 None,
                 "Na have komt het voltooid deelwoord: eaten, niet ate.",
                 "Know staat niet in de continuous, ook niet in de present perfect.",
                 "How long gaat over iets dat nog duurt: have been learning.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Het verschil tussen de twee "
                    "tijden voel je pas als je ze hardop gebruikt.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-de-verleden-en-de-toekomende-tijden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De onregelmatige werkwoorden leer je in drie vormen tegelijk. Let op dat de tweede "
                    "en de derde soms gelijk zijn (bought, brought) en soms niet (went, gone).",
             waarom=[None]),
        dict(aanpak="Bij de regelmatige komt er -ed bij: een medeklinker plus y wordt -ied, en een korte "
                    "klinker plus één medeklinker verdubbelt.",
             waarom=[None]),
        dict(aanpak="De past continuous is de achtergrond, de past simple is wat er in die achtergrond "
                    "gebeurde. Daarom while bij de lange en when bij de korte.",
             waarom=[None]),
        dict(aanpak="De past perfect is het verleden vóór het verleden: je hebt er altijd een tweede, "
                    "later moment bij nodig.",
             waarom=[None, None, None]),
        dict(aanpak="Will is wat je op het moment zelf beslist of belooft, going to is een plan of een "
                    "voorspelling waar je bewijs voor ziet.",
             waarom=[None, None, None, None]),
        dict(aanpak="Zoek bij elke zin welke regel geschonden wordt, en schrijf de hele zin correct over.",
             waarom=[
                 "Na didn't komt de kale vorm; de verleden tijd zit al in didn't.",
                 "Was is zelf al een werkwoordsvorm: bij to be maak je de vraag met de omgekeerde "
                 "woordorde, niet met did.",
                 None,
                 "Na will komt de kale vorm, zonder to.",
                 "Twee modale werkwoorden kunnen niet achter elkaar: can wordt be able to.",
                 "Na when, as soon as en before komt in het Engels een tegenwoordige tijd, ook al gaat "
                 "het over de toekomst.",
                 "Na if komt geen will; de will hoort in de hoofdzin.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Drie tijden in één verhaal "
                    "is precies wat een spreekexamen vraagt.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-modal-auxiliaries-imperative-en-infinitive-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Een modaal werkwoord zegt niet wát er gebeurt maar hoe je ertegenover staat. Must "
                    "kan zowel een verplichting als een conclusie zijn; de rest van de zin verraadt welke.",
             waarom=[
                 None,
                 "Must be exhausted is geen bevel maar een conclusie: je leidt het af uit wat je ziet. "
                 "Het tegendeel daarvan is can't be, niet mustn't be.",
             ]),
        dict(aanpak="Mustn't is een verbod, don't have to betekent dat het niet nodig is. Dat is het "
                    "grootste verschil van dit hoofdstuk.",
             waarom=[
                 None,
                 None,
                 "Must heeft geen verleden tijd; daarvoor gebruik je had to.",
             ]),
        dict(aanpak="De gebiedende wijs is de kale vorm, zonder onderwerp en zonder to. De ontkenning is "
                    "don't, en een voorstel begint met let's.",
             waarom=[None]),
        dict(aanpak="Na want, hope en decide komt to, na make en let de kale vorm, en na een voorzetsel "
                    "of na enjoy de -ing-vorm.",
             waarom=[
                 None,
                 "Let op look forward to: die to is een voorzetsel, geen infinitief, dus er komt -ing "
                 "achter.",
             ]),
        dict(aanpak="Staat er do of does in een bevestigende zin, dan geeft het nadruk. In een vraag of "
                    "een ontkenning is het gewoon het hulpwerkwoord.",
             waarom=[None]),
        dict(aanpak="Zoek bij elke zin welke regel geschonden wordt, en schrijf de hele zin correct over.",
             waarom=[
                 "Een modaal werkwoord krijgt nooit een -s.",
                 "Na een modaal werkwoord komt de kale vorm, zonder to.",
                 "De gebiedende wijs is de kale vorm; please verandert daar niets aan.",
                 None,
                 "Enjoy heeft een lijdend voorwerp nodig: enjoy yourself.",
                 "Een Engelse zin heeft altijd een onderwerp; bij het weer is dat it.",
                 "Ook hier moet er een onderwerp staan: it takes.",
             ]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. Hoe vriendelijk iets klinkt, "
                    "hoor je van iemand anders beter dan van jezelf.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-zinsdelen-soorten-zinnen-en-bijzinnen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek eerst de persoonsvorm, dan het onderwerp (wie of wat doet het), dan het lijdend "
                    "voorwerp (wie of wat ondergaat het).",
             waarom=[
                 None,
                 "Het meewerkend voorwerp is aan wie je iets geeft. Het staat zonder to vóór het lijdend "
                 "voorwerp.",
                 "Zet je het achter het lijdend voorwerp, dan moet er to bij. Twee volgordes, dezelfde "
                 "betekenis.",
             ]),
        dict(aanpak="De Engelse woordorde is onderwerp, werkwoord, voorwerp, en dan plaats vóór tijd. "
                    "Een tijdsbepaling kan ook helemaal vooraan.",
             waarom=[
                 None,
                 None,
                 "Yesterday mag vooraan of achteraan, maar niet tussen het onderwerp en het werkwoord.",
             ]),
        dict(aanpak="Kijk naar de vorm, niet naar de inhoud: een vraagteken, een don't, een kale vorm of "
                    "een what a verraadt het soort.",
             waarom=[None, None]),
        dict(aanpak="Zit er al een hulpwerkwoord in de zin, dan zet je dat vooraan. Zit er geen, dan "
                    "haal je do, does of did erbij.",
             waarom=[
                 None,
                 "Een aanhangvraag is altijd het omgekeerde van de zin ervoor: bevestigend wordt "
                 "ontkennend.",
             ]),
        dict(aanpak="Let op de woorden die eruitzien als een meervoud maar het niet zijn, en op police, "
                    "dat het omgekeerde doet.",
             waarom=[
                 "One of my friends lijkt meervoud, maar het onderwerp is one: dus is.",
             ]),
        dict(aanpak="Because geeft de reden, so het gevolg. But en although geven allebei een tegenstelling, "
                    "maar although staat vooraan in de bijzin.",
             waarom=[
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Zonder komma beperkt de bijzin: ze zegt over wélke je het hebt. Met komma's is ze "
                    "extra informatie die je kan weglaten.",
             waarom=[None, None, None]),
        dict(aanpak="De zero conditional is een algemene waarheid: twee keer een tegenwoordige tijd. De "
                    "first gaat over één geval in de toekomst: if plus tegenwoordige tijd, dan will.",
             waarom=[None, None]),
        dict(aanpak="Deze oefening is pas af als je ze ook echt gedaan hebt. In een echte tekst zie je "
                    "welke voegwoorden je zelf te weinig gebruikt.",
             waarom=[None]),
    ],
)

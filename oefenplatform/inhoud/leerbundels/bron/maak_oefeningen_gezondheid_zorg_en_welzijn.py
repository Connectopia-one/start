# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij gezondheid, zorg en welzijn
🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere opgaven, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
situaties, andere menu's en opdrachten die je enkel op papier kan maken — een
dagmenu samenstellen, een werkplan uitschrijven, een onderdeel benoemen op een
tekening. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/gezondheid-zorg-en-welzijn.json` en naast
`maak_gezondheid_zorg_en_welzijn.py`.

Dit vak raakt aan echte lichamen en echte zorg. Er staat hier dus geen medisch
advies en geen diagnose in: wat een leerling moet kennen voor het examen, en
telkens de verwijzing naar de huisarts of de 112 waar die hoort.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Gezondheid, zorg en welzijn"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIVEAU = "-boost-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "110px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een vraag met een stappenplan: schrijf de stappen in de juiste orde, niet door elkaar.",
    "Waar je iets moet benoemen, schrijf je het woord volledig uit.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("waarnemen-van-prikkel-tot-reactie",
    titel="Waarnemen: van prikkel tot reactie",
    reeksen=[
        dict(kop="De weg van de prikkel",
             opdracht="Zet de schakels in de juiste orde, van 1 tot 6.",
             oefeningen=[
                 ("rij", [("de prikkel", "1"),
                          ("de receptor in het zintuig", "2"),
                          ("de gevoelszenuw", "3"),
                          ("de hersenen of het ruggemerg", "4"),
                          ("de bewegingszenuw", "5"),
                          ("de spier of de klier", "6")],
                  "Welke schakel?", W),
                 ("open", "Wat is het verschil tussen een prikkel en een reactie?",
                  "Een prikkel is de verandering die het zintuig oppikt, bijvoorbeeld licht of "
                  "warmte. De reactie is wat het lichaam daarna doet.", 3),
             ]),
        dict(kop="De zintuigen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("licht", "het oog"),
                          ("geluid", "het oor"),
                          ("geur", "de neus"),
                          ("smaak", "de tong"),
                          ("druk, warmte en pijn", "de huid"),
                          ("de stand van je hoofd", "het evenwichtsorgaan in het oor")],
                  "Welk zintuig?", WL),
                 ("rij", [("de cel die een prikkel oppikt", "de receptor"),
                          ("de drempel waaronder je niets voelt", "de prikkeldrempel"),
                          ("wennen aan een geur na enkele minuten", "adaptatie"),
                          ("de prikkel waar een receptor op gebouwd is",
                           "de adequate prikkel"),
                          ("wat je zintuig doorgeeft aan de zenuw", "een impuls"),
                          ("waar de waarneming echt gebeurt", "in de hersenen")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="Waarnemen gaat niet altijd goed",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom ruik je je eigen huis niet, en een bezoeker wel?",
                  "Je receptoren zijn aan die geur gewend geraakt. Dat is adaptatie: ze geven "
                  "een onveranderde prikkel na een tijd niet meer door.", 3),
                 ("open", "Je stapt uit het donker in de zon en ziet even niets. Wat gebeurt "
                          "er?",
                  "Je oog moet zich aanpassen: de pupil vernauwt en de staafjes zijn "
                  "overbelicht. Na enkele seconden nemen de kegeltjes het over.", 3),
                 ("open", "Waarom is zorg voor iemand met weinig gehoor niet hetzelfde als "
                          "luider praten?",
                  "Luider praten vervormt vaak het geluid. Beter is rustig en duidelijk "
                  "spreken, het gezicht laten zien en zorgen dat er geen achtergrondgeluid "
                  "is.", 3),
             ]),
    ])


# ============================================================
zet("het-oog-en-het-oor",
    titel="Het oog en het oor",
    reeksen=[
        dict(kop="Onderdelen van het oog",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de doorzichtige voorkant", "het hoornvlies"),
                          ("de gekleurde ring", "de iris"),
                          ("de opening in het midden", "de pupil"),
                          ("de bolle lens achter de pupil", "de ooglens"),
                          ("het vlies met de lichtgevoelige cellen", "het netvlies"),
                          ("de zenuw naar de hersenen", "de oogzenuw")],
                  "Welk onderdeel?", WL),
                 ("rij", [("de cellen voor kleur en scherpte", "de kegeltjes"),
                          ("de cellen voor zwak licht", "de staafjes"),
                          ("de plek waar je het scherpst ziet", "de gele vlek"),
                          ("de plek waar je niets ziet", "de blinde vlek"),
                          ("de lens dikker maken om dichtbij te zien", "accommoderen"),
                          ("de spier die de pupil regelt", "de irisspier")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Waarom zie je 's nachts bijna geen kleur?",
                  "Bij weinig licht werken alleen de staafjes, en die zien geen kleur. De "
                  "kegeltjes hebben meer licht nodig.", 3),
             ]),
        dict(kop="Onderdelen van het oor",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de schelp aan de buitenkant", "de oorschelp"),
                          ("het vlies dat meetrilt", "het trommelvel"),
                          ("de drie kleine beentjes", "hamer, aambeeld en stijgbeugel"),
                          ("het slakkenhuis", "het slakkenhuis of de cochlea"),
                          ("de drie ringen voor je evenwicht", "de halfcirkelvormige kanalen"),
                          ("het buisje naar de neusholte", "de buis van Eustachius")],
                  "Welk onderdeel?", WL),
                 ("open", "Waarom helpt slikken of gapen bij een pijnlijk oor in het "
                          "vliegtuig?",
                  "Daarmee open je de buis van Eustachius, zodat de druk aan beide zijden van "
                  "het trommelvel weer gelijk wordt.", 3),
                 ("open", "Waarom raadt men af om met een wattenstaafje in het oor te gaan?",
                  "Je duwt het oorsmeer verder naar binnen en je kan het trommelvel "
                  "beschadigen. Het oor ruimt zichzelf op.", 3),
             ]),
        dict(kop="Het oog en het oor beschermen",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Gehoorschade door lawaai herstelt na een nacht slapen.", False),
                 ("waar", "Boven 85 decibel is langdurig lawaai schadelijk.", True),
                 ("waar", "Een veiligheidsbril is op school alleen nodig bij chemie.", False),
                 ("waar", "Een zonnebril zonder uv-filter is slechter dan geen zonnebril.",
                  True),
                 ("waar", "Oordopjes op een fuif verminderen het geluid zonder de muziek "
                          "onherkenbaar te maken.", True),
                 ("waar", "Wie een scherm gebruikt, hoort geregeld in de verte te kijken.",
                  True),
             ]),
    ])


# ============================================================
zet("spieren-beenderen-en-gewrichten",
    titel="Spieren, beenderen en gewrichten",
    reeksen=[
        dict(kop="Het skelet",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het bot in je bovenarm", "het bovenarmbeen"),
                          ("de twee botten in je onderarm", "de ellepijp en het spaakbeen"),
                          ("het bot in je bovenbeen", "het femur of bovenbeen"),
                          ("de twee botten in je onderbeen", "het scheenbeen en het kuitbeen"),
                          ("de botten van de wervelkolom", "de wervels"),
                          ("de korf rond je hart en longen", "de ribbenkast")],
                  "Welk bot?", WL),
                 ("rij", [("beschermen", "schedel en ribben"),
                          ("steunen", "de wervelkolom"),
                          ("bewegen", "de botten van de ledematen"),
                          ("bloed aanmaken", "het beenmerg"),
                          ("kalk opslaan", "het botweefsel"),
                          ("de laag die een bot glad houdt in het gewricht", "het kraakbeen")],
                  "Welke taak hoort waar?", WL),
             ]),
        dict(kop="Gewrichten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de schouder", "een kogelgewricht"),
                          ("de elleboog", "een scharniergewricht"),
                          ("de nek bij ja-nee knikken", "een rolgewricht"),
                          ("de duim", "een zadelgewricht"),
                          ("de knie", "een scharniergewricht"),
                          ("tussen twee wervels", "een stijf gewricht met tussenwervelschijf")],
                  "Welk soort gewricht?", WL),
                 ("rij", [("verbindt bot met bot", "een ligament of band"),
                          ("verbindt spier met bot", "een pees"),
                          ("de vloeistof die het gewricht smeert", "het gewrichtsvocht"),
                          ("het zakje rond het gewricht", "het gewrichtskapsel"),
                          ("een band die uitscheurt", "een verstuiking of distorsie"),
                          ("een bot dat uit het gewricht schiet", "een ontwrichting")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="Spieren",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat een antagonistenpaar is, met de arm als voorbeeld.",
                  "Twee spieren die tegengesteld werken. De biceps plooit de arm, de triceps "
                  "strekt hem. Een spier kan alleen trekken, nooit duwen, dus heb je er twee "
                  "nodig.", 3),
                 ("rij", [("de spier die je bewust aanspreekt", "een skeletspier, dwarsgestreept"),
                          ("de spier in je darmwand", "een gladde spier, onbewust"),
                          ("de spier van je hart", "de hartspier"),
                          ("de spier korter maken", "samentrekken of contraheren"),
                          ("de stijfheid twee dagen na het sporten", "spierpijn"),
                          ("wat opwarmen doet", "de spier soepel en warm maken")],
                  "Vul aan.", WL),
                 ("open", "Waarom hef je een zware doos met je benen en niet met je rug?",
                  "Je rugwervels en tussenwervelschijven kunnen die kracht niet dragen in een "
                  "gebogen stand. Je beenspieren zijn veel sterker en je rug blijft recht.",
                  3),
             ]),
    ])


# ============================================================
zet("het-zenuwstelsel-en-de-reflexen",
    titel="Het zenuwstelsel en de reflexen",
    reeksen=[
        dict(kop="De indeling",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de hersenen en het ruggemerg samen", "het centrale zenuwstelsel"),
                          ("alle zenuwen daarbuiten", "het perifere zenuwstelsel"),
                          ("het deel dat je bewust stuurt", "het willekeurige zenuwstelsel"),
                          ("het deel dat buiten je om werkt", "het autonome zenuwstelsel"),
                          ("het deel dat versnelt bij schrik", "de sympathicus"),
                          ("het deel dat tot rust brengt", "de parasympathicus")],
                  "Welk deel?", WL),
                 ("rij", [("de zenuwcel", "het neuron"),
                          ("de lange uitloper", "het axon"),
                          ("de korte uitlopers", "de dendrieten"),
                          ("de ruimte tussen twee neuronen", "de synaps"),
                          ("het signaal door een neuron", "de impuls"),
                          ("het isolerende laagje rond een axon", "de myelineschede")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="De hersenen",
             opdracht="Zet achter elke taak het hersendeel.",
             oefeningen=[
                 ("rij", [("denken, taal en beslissen", "de grote hersenen"),
                          ("evenwicht en soepele beweging", "de kleine hersenen"),
                          ("de ademhaling en de hartslag", "de hersenstam"),
                          ("de regeling van honger, dorst en temperatuur", "de hypothalamus"),
                          ("de doorgeefpost naar de grote hersenen", "de thalamus"),
                          ("de eenvoudige reflex zonder de hersenen", "het ruggemerg")],
                  "Welk deel?", WL),
                 ("open", "Waarom is een hersenschudding iets om serieus te nemen, ook als "
                          "iemand gewoon rechtstaat?",
                  "De klachten kunnen pas uren later komen: hoofdpijn, braken, verwardheid. "
                  "Laat de persoon niet alleen en bel de huisarts, en 112 bij "
                  "bewustzijnsverlies.", 3),
             ]),
        dict(kop="De reflexboog",
             opdracht="Zet de schakels van een kniereflex in de juiste orde, van 1 tot 5.",
             oefeningen=[
                 ("rij", [("de tik op de pees", "1"),
                          ("de receptor in de spier", "2"),
                          ("de gevoelszenuw naar het ruggemerg", "3"),
                          ("de schakeling in het ruggemerg", "4"),
                          ("de bewegingszenuw naar de spier", "5"),
                          ("de bewuste gedachte erover", "komt pas achteraf")],
                  "Welke schakel?", WL),
                 ("open", "Waarom gaat een reflex niet langs de hersenen?",
                  "Dan zou het te lang duren. Het ruggemerg schakelt direct door, zodat je je "
                  "hand al terugtrekt voor je de pijn voelt.", 3),
                 ("open", "Geef twee voorbeelden van een reflex die je lichaam beschermt.",
                  "Je hand terugtrekken van iets heets, met je ogen knipperen bij een "
                  "voorwerp, hoesten als er iets in je luchtweg komt, braken bij bedorven "
                  "voedsel.", 3),
             ]),
    ])


# ============================================================
zet("gezondheid-in-kaart-gordon-en-het-icf",
    titel="Gezondheid in kaart: Gordon en het ICF",
    reeksen=[
        dict(kop="De patronen van Gordon",
             opdracht="Zet achter elke vraag welk gezondheidspatroon ze in kaart brengt.",
             oefeningen=[
                 ("rij", [("Wat eet en drinkt u op een dag?", "voeding en stofwisseling"),
                          ("Hoe slaapt u 's nachts?", "slaap en rust"),
                          ("Kan u zich zelf wassen en kleden?", "activiteit en beweging"),
                          ("Hoe gaat u om met spanning?", "stressverwerking"),
                          ("Met wie heeft u contact?", "rollen en relaties"),
                          ("Wat betekent uw geloof voor u?", "waarden en levensovertuiging")],
                  "Welk patroon?", WL),
                 ("open", "Waarom vraagt een zorgkundige naar álle patronen en niet alleen "
                          "naar de klacht?",
                  "Een klacht hangt samen met de rest. Wie slecht slaapt eet minder, en wie "
                  "niemand ziet beweegt minder. Je ziet de hele mens pas als je alles "
                  "nagaat.", 3),
             ]),
        dict(kop="Het ICF",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een versleten heupgewricht", "functies en anatomische structuren"),
                          ("niet meer kunnen traplopen", "activiteiten"),
                          ("niet meer naar de kaartclub gaan", "participatie"),
                          ("een huis met een trap en geen lift", "externe factoren"),
                          ("de leeftijd en het karakter van de persoon",
                           "persoonlijke factoren"),
                          ("de medische naam van de aandoening", "de gezondheidstoestand")],
                  "Welk onderdeel van het ICF?", WL),
                 ("open", "Twee mensen hebben dezelfde versleten knie. De ene woont "
                          "gelijkvloers met een winkel om de hoek, de andere op de derde "
                          "verdieping zonder lift. Wat zegt het ICF daarover?",
                  "De aandoening is dezelfde, maar de participatie verschilt door de externe "
                  "factoren. Gezondheid is niet alleen wat er in het lichaam gebeurt.", 3),
                 ("open", "Waarom spreekt het ICF over participatie en niet enkel over "
                          "zelfstandigheid?",
                  "Meedoen met anderen hoort bij gezond zijn. Iemand kan zich alleen wassen "
                  "en toch volledig geïsoleerd leven.", 3),
             ]),
        dict(kop="Gezondheid breed bekeken",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Geef de omschrijving van gezondheid van de "
                          "Wereldgezondheidsorganisatie en noem één kritiek erop.",
                  "Gezondheid is een toestand van volledig lichamelijk, geestelijk en sociaal "
                  "welbevinden en niet alleen de afwezigheid van ziekte. De kritiek is dat "
                  "bijna niemand daar altijd aan voldoet, en dat wie chronisch ziek is dan "
                  "per definitie ongezond zou zijn.", 3),
                 ("open", "Wat bedoelt men met positieve gezondheid?",
                  "Dat je kijkt naar wat iemand nog wél kan en belangrijk vindt, in plaats van "
                  "enkel naar de ziekte. Het vertrekt van de veerkracht van de persoon.", 3),
             ]),
    ])


# ============================================================
zet("ziek-zijn-en-eerste-hulp",
    titel="Ziek zijn en eerste hulp",
    reeksen=[
        dict(kop="Ziekte en ziekteverwekkers",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een griep", "een virus"),
                          ("een blaasontsteking", "een bacterie"),
                          ("voetschimmel", "een schimmel"),
                          ("hoofdluizen", "een parasiet"),
                          ("waar antibiotica tegen werken", "bacteriën"),
                          ("waar antibiotica niet tegen werken", "virussen")],
                  "Vul aan.", WL),
                 ("open", "Waarom schrijft een arts geen antibioticum voor bij een gewone "
                          "verkoudheid?",
                  "Een verkoudheid is een virus, en daar doen antibiotica niets tegen. Ze "
                  "nodeloos nemen maakt bacteriën wel resistent.", 3),
                 ("rij", [("de tijd tussen besmetting en de eerste klachten",
                           "de incubatietijd"),
                          ("een ziekte die lang duurt", "chronisch"),
                          ("een ziekte die plots en kort is", "acuut"),
                          ("een ziekte die van mens tot mens gaat", "besmettelijk"),
                          ("de ziekte die wereldwijd rondgaat", "een pandemie"),
                          ("wat een vaccin doet", "het lichaam leert zich verdedigen")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="Eerste hulp: de juiste orde",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 5.",
             oefeningen=[
                 ("rij", [("zorg eerst voor je eigen veiligheid", "1"),
                          ("ga na of het slachtoffer reageert", "2"),
                          ("roep hulp en bel 112", "3"),
                          ("controleer de ademhaling", "4"),
                          ("start de reanimatie als er geen ademhaling is", "5"),
                          ("de persoon een glas water geven", "doe je niet")],
                  "Welke stap?", WL),
                 ("rij", [("het noodnummer in België", "112"),
                          ("het nummer van het Antigifcentrum", "070 245 245"),
                          ("de verhouding bij reanimatie van een volwassene",
                           "30 compressies op 2 beademingen"),
                          ("het ritme van de compressies", "100 tot 120 per minuut"),
                          ("waar je duwt bij reanimatie", "midden op het borstbeen"),
                          ("het toestel dat een schok geeft", "de AED of defibrillator")],
                  "Wat is het antwoord?", WL),
             ]),
        dict(kop="Wat doe je bij",
             opdracht="Schrijf in enkele zinnen wat je doet. Twijfel je, dan bel je 112.",
             oefeningen=[
                 ("open", "een brandwond van een hete pan op de hand",
                  "Minstens tien minuten onder lauw stromend water houden. Geen ijs, geen "
                  "zalf, geen tandpasta. Ringen af, de blaren niet openmaken. Bij een grote "
                  "of diepe wonde naar de arts.", 3),
                 ("open", "een neusbloeding",
                  "Rechtop zitten, hoofd licht voorover, de zachte neusvleugels tien minuten "
                  "dichtknijpen. Niet het hoofd achterover, want dan slik je het bloed in.",
                  3),
                 ("open", "iemand die stilaan wegdraait maar nog ademt",
                  "In stabiele zijligging leggen, warm houden, de ademhaling blijven volgen en "
                  "112 bellen.", 3),
                 ("open", "een verstuikte voet op de sportles",
                  "Rust, ijs in een doek van vijftien minuten, een drukverband en de voet hoog "
                  "leggen. Bij veel zwelling of niet kunnen stappen naar de arts.", 3),
             ]),
    ])


# ============================================================
zet("gezondheid-bevorderen-preventie-voeding-en-beweging",
    titel="Gezondheid bevorderen: preventie, voeding en beweging",
    reeksen=[
        dict(kop="Soorten preventie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een vaccinatie tegen mazelen", "primaire preventie"),
                          ("een bevolkingsonderzoek naar darmkanker", "secundaire preventie"),
                          ("revalidatie na een hartinfarct", "tertiaire preventie"),
                          ("een rookverbod in de horeca", "primaire preventie"),
                          ("de bloeddruk laten meten bij de huisarts",
                           "secundaire preventie"),
                          ("leren leven met diabetes", "tertiaire preventie")],
                  "Welke preventie?", WL),
                 ("open", "Wat is het verschil tussen primaire en secundaire preventie, in één "
                          "zin?",
                  "Primaire preventie voorkomt dat je ziek wordt, secundaire preventie vindt "
                  "een ziekte vroeg, voor je er iets van merkt.", 2),
             ]),
        dict(kop="De voedingsdriehoek",
             opdracht="Zet achter elk voedingsmiddel waar het in de voedingsdriehoek staat.",
             oefeningen=[
                 ("rij", [("water", "helemaal bovenaan, de basis"),
                          ("groenten en fruit", "de donkergroene laag"),
                          ("volkoren brood", "de groene laag"),
                          ("vlees en kaas", "de oranje laag, met maat"),
                          ("een zak chips", "de rode bol, buiten de driehoek"),
                          ("een frisdrank met suiker", "de rode bol, buiten de driehoek")],
                  "Waar staat het?", WL),
                 ("open", "Waarom staat de voedingsdriehoek op zijn kop, met water bovenaan?",
                  "Wat bovenaan het breedst is, eet of drink je het meest. De driehoek toont "
                  "de verhoudingen, niet een rangschikking van belangrijk naar onbelangrijk.",
                  3),
                 ("open", "Stel een dagmenu op met ontbijt, middagmaal, avondmaal en twee "
                          "tussendoortjes, en zet er telkens bij welke laag je gebruikt.",
                  "Een goed antwoord haalt bij elke maaltijd uit de groene lagen, zet water "
                  "als drank, gebruikt vlees of kaas met maat en houdt de rode bol tot een "
                  "uitzondering. Bijvoorbeeld: havermout met fruit, volkoren boterham met kip "
                  "en tomaat, soep en een appel, pasta met veel groenten en wat kaas, en een "
                  "handvol noten.", 8),
             ]),
        dict(kop="Beweging",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de aanbeveling voor een jongere, per dag", "minstens 60 minuten"),
                          ("de aanbeveling voor een volwassene, per week",
                           "minstens 150 minuten matig"),
                          ("hoe vaak spierversterkend per week", "twee keer"),
                          ("de maat van matig bewegen", "je kan praten maar niet zingen"),
                          ("de maat van intensief bewegen", "praten gaat moeizaam"),
                          ("hoelang je best niet aan één stuk zit", "niet langer dan een uur")],
                  "Wat is de richtlijn?", WL),
                 ("open", "Noem drie manieren om beweging in een gewone schooldag te krijgen, "
                          "zonder sportclub.",
                  "Te voet of met de fiets naar school, de trap in plaats van de lift, "
                  "rechtstaan en rondstappen tijdens de pauze, boodschappen te voet doen.", 3),
                 ("open", "Waarom is zitten ook ongezond als je daarnaast genoeg sport?",
                  "Lang stilzitten heeft een eigen effect op de bloedvaten en de "
                  "stofwisseling. Een uur sport maakt acht uur zitten niet ongedaan.", 3),
             ]),
    ])


# ============================================================
zet("kwaliteitsbewust-handelen",
    titel="Kwaliteitsbewust handelen",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de zorg die je zou willen voor je eigen ouder", "goede zorg"),
                          ("de persoon staat centraal, niet de taak", "persoonsgerichte zorg"),
                          ("zelf kunnen beslissen over je leven", "autonomie"),
                          ("de eigen waarde van de persoon", "de waardigheid"),
                          ("de plicht om niets door te vertellen", "het beroepsgeheim"),
                          ("de regels van je beroepsgroep", "de deontologische code")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Een bewoner wil geen bad. Wat doe je, en wat doe je zeker niet?",
                  "Je vraagt waarom, zoekt een alternatief zoals wassen aan de lavabo of een "
                  "ander moment, en je legt het vast in het dossier. Je dwingt niet en je laat "
                  "het ook niet gewoon vallen zonder er iets mee te doen.", 3),
             ]),
        dict(kop="De PDCA-cirkel",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 4, en zet erbij wat je "
                      "concreet doet.",
             oefeningen=[
                 ("rij", [("plan: afspreken hoe je het gaat doen", "1"),
                          ("do: het uitvoeren", "2"),
                          ("check: nagaan of het gelukt is", "3"),
                          ("act: bijsturen wat niet werkte", "4"),
                          ("waar de cirkel daarna opnieuw begint", "bij plan"),
                          ("waarom het een cirkel is en geen lijst",
                           "kwaliteit is nooit af, je blijft bijsturen")],
                  "Welke stap?", WL),
                 ("open", "In een woonzorgcentrum vallen er veel bewoners in de nacht. Werk de "
                          "vier stappen van de PDCA-cirkel uit voor dat probleem.",
                  "Plan: afspreken dat er nachtlampjes komen en dat de weg naar het toilet "
                  "vrij blijft. Do: de lampjes plaatsen en het team briefen. Check: na een "
                  "maand de valincidenten tellen. Act: waar het niet hielp zoeken naar een "
                  "andere oorzaak, bijvoorbeeld medicatie of slecht schoeisel.", 8),
             ]),
        dict(kop="Jezelf en je team",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een fout toegeven en een fout verzwijgen "
                          "voor de kwaliteit van de zorg?",
                  "Een gemelde fout kan het team nakijken en voorkomen. Een verzwegen fout "
                  "komt terug, bij iemand anders en vaak erger.", 3),
                 ("open", "Wat is reflecteren, en waarom is dat deel van je werk?",
                  "Achteraf nadenken over wat je deed, wat goed ging en wat je anders zou "
                  "doen. Zo verbeter je je eigen handelen in plaats van enkel routine te "
                  "herhalen.", 3),
                 ("open", "Noem drie signalen dat een zorgkundige zelf tegen haar grenzen "
                          "loopt.",
                  "Slecht slapen, kort aangebonden zijn tegen bewoners, zich dood voelen op "
                  "weg naar het werk, fouten maken die anders niet gebeuren, zich afsluiten "
                  "van collega's.", 3),
             ]),
    ])


# ============================================================
zet("voedingsstoffen-en-een-evenwichtig-dagmenu",
    titel="Voedingsstoffen en een evenwichtig dagmenu",
    reeksen=[
        dict(kop="De voedingsstoffen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de bouwstof van je spieren", "eiwitten"),
                          ("de belangrijkste brandstof", "koolhydraten"),
                          ("de meest energierijke voedingsstof", "vetten"),
                          ("de stof die je darmen op gang houdt", "vezels"),
                          ("de stoffen die je in kleine hoeveelheden nodig hebt",
                           "vitaminen en mineralen"),
                          ("de stof waar je lichaam voor twee derden uit bestaat", "water")],
                  "Welke voedingsstof?", WL),
                 ("rij", [("1 gram koolhydraten", "4 kcal"),
                          ("1 gram eiwit", "4 kcal"),
                          ("1 gram vet", "9 kcal"),
                          ("1 gram vezels", "levert nauwelijks energie"),
                          ("1 gram water", "0 kcal"),
                          ("1 gram alcohol", "7 kcal")],
                  "Hoeveel energie?", WW),
             ]),
        dict(kop="Vitaminen en mineralen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("voor je gezichtsvermogen en je huid", "vitamine A"),
                          ("voor de opname van kalk, uit zonlicht", "vitamine D"),
                          ("voor je weerstand, uit fruit en groenten", "vitamine C"),
                          ("voor je bloedstolling", "vitamine K"),
                          ("voor je botten en tanden", "calcium"),
                          ("voor je rode bloedcellen", "ijzer")],
                  "Welke stof?", WL),
                 ("rij", [("de vitaminen die in vet oplossen", "A, D, E en K"),
                          ("de vitaminen die in water oplossen", "B en C"),
                          ("wat er met vitamine C gebeurt bij lang koken", "hij gaat verloren"),
                          ("het mineraal dat je best beperkt", "natrium, uit zout"),
                          ("de bron van ijzer die het best opgenomen wordt", "vlees"),
                          ("wat de opname van plantaardig ijzer helpt",
                           "vitamine C erbij eten")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Rekenen aan een menu",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "Een portie pasta bevat 60 g koolhydraten, 10 g eiwit en 5 g vet. "
                          "Hoeveel kcal is dat?", "325 kcal", W),
                 ("kort", "Hoeveel procent van die energie komt uit vet?",
                  "45 gedeeld door 325 is ongeveer 13,8 %", WW),
                 ("kort", "Een jongere heeft 2 400 kcal per dag nodig. Hoeveel procent van zijn "
                          "dagbehoefte dekt die portie?", "ongeveer 13,5 %", WW),
                 ("open", "Een menu haalt 45 % van zijn energie uit vet. Is dat veel, en wat "
                          "pas je aan?",
                  "Dat is te veel; de richtlijn is ongeveer 30 tot 35 %. Minder boter, saus en "
                  "gefrituurd, meer volkoren en groenten.", 3),
             ]),
    ])


# ============================================================
zet("voedselveiligheid-en-voedselhygiene",
    titel="Voedselveiligheid en voedselhygiëne",
    reeksen=[
        dict(kop="Besmetting",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("van rauw vlees naar de salade via hetzelfde mes",
                           "kruisbesmetting"),
                          ("de bacterie die vaak op rauw gevogelte zit", "salmonella"),
                          ("de bacterie die zich in de koelkast nog vermeerdert", "listeria"),
                          ("wat bacteriën nodig hebben om te groeien",
                           "warmte, vocht, voedsel en tijd"),
                          ("de temperatuurzone waar ze het snelst groeien",
                           "tussen 4 en 60 graden"),
                          ("wat afdoden gebeurt bij", "voldoende lang verhitten")],
                  "Vul aan.", WL),
                 ("rij", [("de temperatuur van een koelkast", "tussen 4 en 7 graden"),
                          ("de temperatuur van een diepvries", "−18 graden"),
                          ("de kerntemperatuur van gaar gevogelte", "75 graden"),
                          ("hoelang je handen wast", "minstens 20 seconden"),
                          ("waar rauw vlees in de koelkast hoort", "onderaan, apart"),
                          ("wat je nooit doet met ontdooid vlees",
                           "opnieuw invriezen zonder te bereiden")],
                  "Wat is de regel?", WL),
             ]),
        dict(kop="Datums en bewaren",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("te gebruiken tot", "een uiterste datum, daarna weggooien"),
                          ("ten minste houdbaar tot", "een kwaliteitsdatum, vaak nog goed"),
                          ("op verse vis en gehakt staat", "te gebruiken tot"),
                          ("op droge pasta staat", "ten minste houdbaar tot"),
                          ("de regel eerst in, eerst uit", "fifo"),
                          ("wat je op een restje schrijft", "wat het is en van welke dag")],
                  "Vul aan.", WL),
                 ("open", "Een pak yoghurt is twee dagen over de ten minste houdbaar tot. Wat "
                          "doe je?",
                  "Kijken, ruiken en een beetje proeven. Is er niets aan te merken, dan is het "
                  "nog goed. Bij een bolle deksel of een vreemde geur gooi je het weg.", 3),
                 ("open", "Waarom mag je warm eten niet gewoon in de koelkast laten afkoelen?",
                  "Het warmt de hele koelkast op en het blijft te lang in de gevaarlijke zone. "
                  "Je koelt eerst snel af, in een platte schaal of onder koud water.", 3),
             ]),
        dict(kop="HACCP in de keuken",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "HACCP betekent dat je de gevaren opspoort en de kritieke punten "
                          "beheerst.", True),
                 ("waar", "Een keukenhanddoek om je handen af te drogen is hygiënischer dan "
                          "papier.", False),
                 ("waar", "Een snijplank voor rauw vlees en een andere voor groenten is een "
                          "maatregel tegen kruisbesmetting.", True),
                 ("waar", "Juwelen en een uurwerk mag je aanhouden in een professionele "
                          "keuken.", False),
                 ("waar", "De temperatuur van de koelkast hoort dagelijks genoteerd te "
                          "worden.", True),
                 ("waar", "Wie maagdarmklachten heeft, mag die dag niet met voedsel werken.",
                  True),
             ]),
    ])


# ============================================================
zet("voedsel-bewaren",
    titel="Voedsel bewaren",
    reeksen=[
        dict(kop="Technieken",
             opdracht="Zet achter elke techniek waarom ze werkt.",
             oefeningen=[
                 ("rij", [("koelen", "bacteriën groeien veel langzamer"),
                          ("diepvriezen", "het water is bevroren, dus onbruikbaar"),
                          ("drogen", "er is geen vocht meer"),
                          ("zouten", "het zout trekt het water uit de cellen"),
                          ("inmaken in zuur", "de zuurtegraad is te laag voor bacteriën"),
                          ("steriliseren", "alles wordt afgedood door de hitte")],
                  "Waarom werkt het?", WL),
                 ("rij", [("melk 15 seconden op 72 graden", "pasteuriseren"),
                          ("melk die maanden buiten de koelkast kan", "gesteriliseerd of UHT"),
                          ("de lucht uit het pak halen", "vacuüm verpakken"),
                          ("de lucht vervangen door een ander gasmengsel",
                           "beschermende atmosfeer"),
                          ("bestralen om bacteriën te doden", "doorstralen"),
                          ("suiker toevoegen aan fruit", "confituur maken")],
                  "Hoe heet de techniek?", WL),
             ]),
        dict(kop="Waar bewaar je wat?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("aardappelen", "donker en koel, niet in de koelkast"),
                          ("bananen", "op kamertemperatuur"),
                          ("tomaten", "op kamertemperatuur, voor de smaak"),
                          ("rauw gehakt", "onderaan in de koelkast, zelfde dag gebruiken"),
                          ("boter", "in de koelkast of het boterkamertje"),
                          ("bloem en rijst", "droog en in een gesloten doos")],
                  "Hoe bewaren?", WL),
                 ("open", "Waarom horen aardappelen niet in de koelkast?",
                  "Bij die temperatuur wordt het zetmeel omgezet in suiker. Ze worden zoet en "
                  "bruinen te snel in de pan.", 3),
                 ("open", "Waarom ruikt een koelkast naar meloen als er een opengesneden "
                          "meloen in staat?",
                  "Geuren trekken in andere voedingsmiddelen, vooral in boter en melk. Dek "
                  "alles af of doe het in een gesloten doos.", 3),
             ]),
        dict(kop="Verspilling",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem vier manieren om in een gezin minder eten weg te gooien.",
                  "Een boodschappenlijst maken op basis van wat er al is, de fifo-regel "
                  "toepassen, restjes bewaren en de volgende dag opeten, kleinere porties "
                  "opscheppen en bijnemen, en de diepvries gebruiken voor wat je niet op "
                  "krijgt.", 4),
                 ("open", "Wat is het verschil tussen verspilling bij de consument en bij de "
                          "producent?",
                  "Bij de producent gaat het vooral om wat niet aan de normen voor vorm of "
                  "maat voldoet; bij de consument om wat gekocht is en niet opgegeten.", 3),
             ]),
    ])


# ============================================================
zet("boodschappen-doen-en-de-tafel-dekken",
    titel="Boodschappen doen en de tafel dekken",
    reeksen=[
        dict(kop="Slim boodschappen doen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de prijs per kilo of per liter", "de eenheidsprijs"),
                          ("waarmee je twee pakken van verschillende grootte vergelijkt",
                           "de eenheidsprijs"),
                          ("de lijst van wat erin zit, van veel naar weinig",
                           "de ingrediëntenlijst"),
                          ("de tabel met de kcal en de voedingsstoffen",
                           "de voedingswaardetabel"),
                          ("het logo dat zegt dat er geen gluten in zit", "het glutenlogo"),
                          ("de stoffen die verplicht vermeld worden voor wie allergisch is",
                           "de allergenen")],
                  "Hoe noemen we dit?", WL),
                 ("kort", "Een pak van 500 g kost 2,45 euro, een pak van 750 g kost "
                          "3,45 euro. Wat is de eenheidsprijs per kilo van het eerste?",
                  "4,90 euro per kg", WW),
                 ("kort", "En van het tweede?", "4,60 euro per kg", WW),
                 ("open", "Is het grootste pak altijd het voordeligste? Leg uit.",
                  "Niet altijd: soms is het kleinere pak per kilo goedkoper, en een groot pak "
                  "dat je niet op krijgt is helemaal duur. Kijk altijd naar de eenheidsprijs "
                  "én naar wat je echt gebruikt.", 3),
             ]),
        dict(kop="Het etiket lezen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Op een pak koekjes staat als eerste ingrediënt suiker. Wat zegt dat "
                          "je?",
                  "De ingrediënten staan in volgorde van gewicht. Suiker als eerste betekent "
                  "dat er meer suiker in zit dan bloem.", 3),
                 ("open", "Waarom staan de voedingswaarden per 100 g en niet per koekje?",
                  "Zo kan je twee producten met elkaar vergelijken. Reken het zelf om naar "
                  "jouw portie, want een portie kan veel groter zijn dan 100 g.", 3),
                 ("open", "Wat is een E-nummer, en is dat per definitie slecht?",
                  "Een toegelaten toevoegsel met een Europees nummer, bijvoorbeeld een "
                  "bewaarmiddel of een kleurstof. Het is niet per definitie slecht: E300 is "
                  "gewoon vitamine C.", 3),
             ]),
        dict(kop="De tafel dekken",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("waar het mes ligt", "rechts, snijkant naar het bord"),
                          ("waar de vork ligt", "links"),
                          ("waar het dessertgerei ligt", "boven het bord"),
                          ("waar het glas staat", "rechtsboven, bij de punt van het mes"),
                          ("in welke orde je het gerei neemt", "van buiten naar binnen"),
                          ("waar het broodbordje staat", "linksboven")],
                  "Waar hoort het?", WL),
                 ("teken", "Teken een gedekt couvert voor een voorgerecht met vis en een "
                           "hoofdgerecht met vlees, en benoem elk stuk.",
                  "Bord in het midden. Links twee vorken: de visvork buiten, de vleesvork "
                  "binnen. Rechts twee messen met de snijkant naar het bord: het vismes "
                  "buiten, het vleesmes binnen. Dessertgerei boven het bord, glas rechtsboven, "
                  "broodbordje linksboven.", 60),
                 ("open", "Waarom wordt er van buiten naar binnen gegeten?",
                  "Het gerei ligt in de orde van de gangen. Wie van buiten naar binnen neemt, "
                  "heeft altijd het juiste stuk bij de hand.", 2),
             ]),
    ])


# ============================================================
zet("interieurzorg-ruimtes-vuil-en-technieken",
    titel="Interieurzorg: ruimtes, vuil en technieken",
    reeksen=[
        dict(kop="Soorten vuil",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("stof en kruimels", "los vuil"),
                          ("een opgedroogde vlek op de tafel", "vastzittend vuil"),
                          ("kalkaanslag op de kraan", "vastzittend vuil, mineraal"),
                          ("vet op de dampkap", "vastzittend vuil, vettig"),
                          ("bacteriën op een snijplank", "onzichtbaar vuil"),
                          ("een kras in de vloer", "geen vuil, schade")],
                  "Welk soort vuil?", WL),
                 ("rij", [("tegen vet", "een ontvetter, alkalisch"),
                          ("tegen kalk", "een zuur middel, bijvoorbeeld azijn"),
                          ("tegen bacteriën", "een desinfecterend middel"),
                          ("voor een gewone vloer", "een allesreiniger"),
                          ("op een marmeren blad nooit", "een zuur middel"),
                          ("wat je nooit mengt", "bleekwater en een zuur middel")],
                  "Welk middel?", WL),
                 ("open", "Waarom mag je bleekwater en een zuur middel nooit samen gebruiken?",
                  "Dan komt er chloorgas vrij, en dat is giftig om in te ademen. Gebruik één "
                  "middel per keer en spoel tussendoor.", 3),
             ]),
        dict(kop="De technieken",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("met een droge doek het stof wegnemen", "droog afnemen"),
                          ("met een licht vochtige doek", "vochtig afnemen"),
                          ("met water en een middel", "nat reinigen"),
                          ("eerst het vuil losmaken en laten inwerken", "inweken"),
                          ("met een machine die zuigt en schrobt", "machinaal reinigen"),
                          ("de bacteriën doden na het reinigen", "desinfecteren")],
                  "Welke techniek?", WL),
                 ("open", "Waarom desinfecteer je nooit op een vuile oppervlakte?",
                  "Het middel komt niet bij de bacteriën omdat het vuil ervoor zit. Je "
                  "reinigt eerst, dan desinfecteer je.", 3),
                 ("open", "Waarom werk je van boven naar onder en van droog naar nat?",
                  "Wat je naar beneden doet vallen, ruim je daarna nog op. En nat werk maakt "
                  "droog stof tot modder.", 3),
             ]),
        dict(kop="Per ruimte",
             opdracht="Schrijf bij elke ruimte op wat de bijzondere aandacht vraagt.",
             oefeningen=[
                 ("rij", [("de keuken", "vet, kruisbesmetting, de snijplanken"),
                          ("de badkamer", "kalk, schimmel, vochtige doeken"),
                          ("het toilet", "een eigen materiaal, desinfecteren, handschoenen"),
                          ("de slaapkamer", "stof en huisstofmijt, verluchten"),
                          ("de leefruimte", "stof, vlekken op textiel"),
                          ("de trap", "de valrisico's en losliggende tapijten")],
                  "Waar let je op?", WL),
                 ("open", "Waarom gebruik je voor het toilet een apart materiaal?",
                  "Anders breng je de bacteriën van het toilet over naar de lavabo of de "
                  "keuken. Vaak werkt men met kleurcodes voor de doeken.", 3),
             ]),
    ])


# ============================================================
zet("methodisch-veilig-en-duurzaam-schoonmaken",
    titel="Methodisch, veilig en duurzaam schoonmaken",
    reeksen=[
        dict(kop="Methodisch werken",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 6.",
             oefeningen=[
                 ("rij", [("nagaan wat er precies moet gebeuren", "1"),
                          ("het materiaal en de middelen klaarzetten", "2"),
                          ("de ruimte vrijmaken en verluchten", "3"),
                          ("het werk uitvoeren, van boven naar onder", "4"),
                          ("nakijken of alles goed is", "5"),
                          ("het materiaal reinigen en opbergen", "6")],
                  "Welke stap?", W),
                 ("open", "Waarom hoort het materiaal opbergen bij het werk en niet erna?",
                  "Een vuile dweil of een natte doek wordt een bron van bacteriën en geur. Het "
                  "werk is pas af als het materiaal klaar is voor de volgende keer.", 3),
                 ("open", "Je hebt één uur voor een appartement en je komt tijd tekort. Hoe "
                          "kies je wat je eerst doet?",
                  "Eerst wat de gezondheid raakt en wat gevaarlijk is: keuken, toilet, "
                  "badkamer en de doorgangen. Het stof op een kast kan wachten. Je meldt wat "
                  "je niet gedaan hebt.", 3),
             ]),
        dict(kop="Veilig werken",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de pictogrammen op een fles", "de gevaarsymbolen"),
                          ("het blad met de gevaren en de eerste hulp",
                           "de veiligheidsfiche"),
                          ("wat je draagt bij een bijtend middel", "handschoenen en een bril"),
                          ("wat je nooit doet met een middel", "overgieten in een andere fles"),
                          ("wat je bij een natte vloer plaatst", "een waarschuwingsbord"),
                          ("de houding bij het dweilen", "rechte rug, benen gebogen")],
                  "Vul aan.", WL),
                 ("rij", [("een middel op je huid", "overvloedig spoelen met water"),
                          ("een middel in je oog", "minstens tien minuten spoelen, dan arts"),
                          ("een middel ingeslikt", "niet doen braken, Antigifcentrum bellen"),
                          ("het nummer van het Antigifcentrum", "070 245 245"),
                          ("een gemorste fles op de vloer", "afdekken, verluchten, opruimen "
                           "met handschoenen"),
                          ("wat je meeneemt naar de arts", "de fles of de veiligheidsfiche")],
                  "Wat doe je?", WL),
             ]),
        dict(kop="Duurzaam",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem vier manieren om duurzamer schoon te maken.",
                  "Doseren volgens de verpakking, met microvezel en water werken waar dat "
                  "kan, navulbare flessen gebruiken, koud of lauw water in plaats van warm, "
                  "en herbruikbare doeken in plaats van wegwerpdoekjes.", 4),
                 ("open", "Waarom is twee keer zoveel middel gebruiken niet twee keer zo "
                          "schoon?",
                  "Boven de juiste dosering werkt het middel niet beter. Er blijft wel een "
                  "film achter die plakt en nieuw vuil vasthoudt, en het belast het water.",
                  3),
                 ("open", "Wat is het voordeel van microvezel boven een gewone doek?",
                  "De vezels nemen stof en bacteriën mechanisch mee, zodat je met water "
                  "alleen al veel haalt en minder middel nodig hebt.", 3),
             ]),
    ])


# ============================================================
zet("zorg-voor-de-woon-en-leefomgeving",
    titel="Zorg voor de woon- en leefomgeving",
    reeksen=[
        dict(kop="Een veilige woning",
             opdracht="Schrijf bij elk risico op wat je eraan doet.",
             oefeningen=[
                 ("rij", [("een losliggend tapijt in de gang", "wegnemen of vastleggen"),
                          ("een donkere trap", "een lamp en een schakelaar boven en onder"),
                          ("een gladde badkamervloer", "een antislipmat en een handgreep"),
                          ("een snoer dwars over de vloer", "langs de wand leggen"),
                          ("geen rookmelder", "er een plaatsen, per verdieping"),
                          ("medicatie op het keukenblad", "in een afgesloten kastje")],
                  "Wat doe je?", WL),
                 ("open", "Waarom is vallen bij ouderen zo ingrijpend?",
                  "Een gebroken heup betekent vaak een operatie, lang revalideren en soms "
                  "nooit meer thuis kunnen wonen. Voorkomen weegt veel zwaarder dan "
                  "herstellen.", 3),
             ]),
        dict(kop="Comfort in huis",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de aangename temperatuur in een leefruimte",
                           "ongeveer 20 graden"),
                          ("de temperatuur in een slaapkamer", "ongeveer 16 tot 18 graden"),
                          ("hoe vaak je verlucht", "elke dag, kort en flink open"),
                          ("waarom je verlucht", "vocht, CO2 en geuren weg"),
                          ("wat te veel vocht geeft", "schimmel en huisstofmijt"),
                          ("het hulpmiddel dat de luchtvochtigheid meet", "een hygrometer")],
                  "Vul aan.", WL),
                 ("open", "Waarom is een raam een kwartier wijd open beter dan een raam de "
                          "hele dag op een kier?",
                  "Je wisselt de lucht snel zonder de muren te laten afkoelen. Een kier laat "
                  "de warmte weglopen en verlucht nauwelijks.", 3),
                 ("open", "Er staat schimmel in de hoek achter de kast. Wat is de oorzaak en "
                          "wat doe je?",
                  "Daar circuleert geen lucht en de muur is kouder, zodat het vocht neerslaat. "
                  "Zet de kast enkele centimeters van de muur, verlucht beter en maak de "
                  "schimmel weg met een geschikt middel en handschoenen.", 3),
             ]),
        dict(kop="Afval en hulpmiddelen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een lege fles frisdrank van plastic", "pmd"),
                          ("een krant", "papier en karton"),
                          ("een confituurpot van glas", "de glasbol"),
                          ("aardappelschillen", "gft"),
                          ("een lege batterij", "het containerpark of een inzamelpunt"),
                          ("een restje verf", "klein gevaarlijk afval")],
                  "Waar hoort het?", WL),
                 ("rij", [("om zich recht te houden bij het stappen", "een rollator"),
                          ("om in en uit bad te komen", "een badplank of beugel"),
                          ("om hoger te zitten op het toilet", "een toiletverhoger"),
                          ("om een kous aan te trekken", "een kousaantrekker"),
                          ("om iets van de vloer te nemen", "een grijptang"),
                          ("om te blijven liggen en toch te eten", "een bedtafel")],
                  "Welk hulpmiddel?", WL),
             ]),
    ])


# ============================================================
zet("linnenzorg-sorteren-wassen-en-strijken",
    titel="Linnenzorg: sorteren, wassen en strijken",
    reeksen=[
        dict(kop="Sorteren",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("waarop je in de eerste plaats sorteert", "op kleur"),
                          ("waarop je daarna sorteert", "op temperatuur en textielsoort"),
                          ("wat een nieuwe rode trui kan doen", "afgeven op het wit"),
                          ("wat je apart wast bij ziekte", "besmet linnen, op hoge temperatuur"),
                          ("wat in een waszak hoort", "fijne stukken en beha's"),
                          ("wat je controleert voor je wast", "de zakken en de vlekken")],
                  "Vul aan.", WL),
                 ("rij", [("een teil in water", "wassen, met de temperatuur erin"),
                          ("een driehoek", "bleken"),
                          ("een vierkant met een cirkel", "drogen in de droogkast"),
                          ("een strijkijzer", "strijken, met de punten voor de temperatuur"),
                          ("een cirkel", "chemisch reinigen"),
                          ("een kruis door een symbool", "mag niet")],
                  "Welk onderhoudssymbool?", WL),
             ]),
        dict(kop="Wassen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("katoen, stevig en wit", "60 graden"),
                          ("gekleurd katoen", "30 of 40 graden"),
                          ("wol", "het wolprogramma, koud of 30 graden"),
                          ("synthetisch", "30 of 40 graden"),
                          ("waar de temperatuur over gaat", "hoe vuil en welk textiel"),
                          ("waarom je de trommel niet volstouwt",
                           "het water en het poeder komen er niet overal bij")],
                  "Welke temperatuur?", WL),
                 ("open", "Een witte handdoek is grauw geworden. Noem twee mogelijke oorzaken.",
                  "Te veel wasmiddel dat niet uitspoelt, te lage temperatuur, of samen gewassen "
                  "met gekleurde stukken die afgeven.", 3),
                 ("open", "Waarom is 60 graden voor beddengoed bij ziekte verstandig?",
                  "Bij die temperatuur worden de meeste ziekteverwekkers afgedood. Bij 30 "
                  "graden blijven ze leven, ook in de machine.", 3),
             ]),
        dict(kop="Vlekken en strijken",
             opdracht="Schrijf bij elke vlek op wat je doet. Eerst behandelen, dan wassen.",
             oefeningen=[
                 ("rij", [("rode wijn", "deppen, zout erop, dan koud spoelen"),
                          ("bloed", "koud water, nooit warm"),
                          ("vet of olie", "afstoffen met talk of zeep, dan warm wassen"),
                          ("balpen", "alcohol of handgel, dan wassen"),
                          ("gras", "alcohol of een voorbehandelmiddel"),
                          ("kauwgom", "eerst invriezen, dan afbreken")],
                  "Wat doe je?", WL),
                 ("open", "Waarom nooit warm water op een bloedvlek?",
                  "De eiwitten in het bloed stollen bij warmte en zetten zich vast in de "
                  "vezel. Dan gaat de vlek er niet meer uit.", 3),
                 ("rij", [("wol", "op één punt, lauw, met een doek ertussen"),
                          ("zijde", "op één punt, langs de binnenkant"),
                          ("katoen", "op drie punten, met stoom"),
                          ("linnen", "op drie punten, licht vochtig"),
                          ("synthetisch", "op één punt, laag"),
                          ("een hemd", "eerst de kraag, dan de manchetten, dan de rug")],
                  "Hoe strijk je het?", WL),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-waarnemen-van-prikkel-tot-reactie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De weg van prikkel tot reactie is altijd dezelfde keten van zes schakels. "
                   "Onthoud ze aan de richting: naar binnen met de gevoelszenuw, beslissen in "
                   "het midden, naar buiten met de bewegingszenuw. Noemt een vraag een spier of "
                   "een klier, dan zit je aan het einde van de keten.",
            waarom=[
                "Merk op dat schakel 4 twee mogelijkheden heeft. Bij een reflex beslist het "
                "ruggemerg, en dan gaat het sneller omdat de prikkel niet eerst naar de hersenen "
                "moet. Daarom trek je je hand terug voor je de pijn voelt.",
                None,
            ],
        ),
        dict(
            aanpak="Elk zintuig heeft één prikkel waarvoor het gebouwd is, en dat heet de "
                   "adequate prikkel. Let op het oor: het bevat twee zintuigen, een voor geluid "
                   "en een voor evenwicht. De huid is er ook een met meerdere soorten receptoren "
                   "in zich.",
            waarom=[
                None,
                "De laatste twee lijnen zijn het belangrijkste van deze bundel: je zintuig geeft "
                "enkel impulsen door, en de waarneming zelf gebeurt in de hersenen. Daarom kan je "
                "iets zien dat er niet is, en kan iemand nog pijn voelen in een been dat er niet "
                "meer is.",
            ],
        ),
        dict(
            aanpak="De drie oefeningen gaan over waarnemen dat tekortschiet: wennen, aanpassen, "
                   "en het verlies van een zintuig. Bij de laatste wordt om zorg gevraagd, niet "
                   "om biologie: antwoord dus met wat je doet, niet met wat er stuk is.",
            waarom=[
                "Adaptatie is geen gebrek maar een nuttige eigenschap. Je receptoren melden "
                "veranderingen, en wat niet verandert, hoef je niet te blijven voelen; anders zou "
                "je je kleren de hele dag voelen.",
                "Let op de orde: eerst de pupil, die in een seconde vernauwt, en daarna de "
                "overgang van staafjes naar kegeltjes. Omgekeerd, van licht naar donker, duurt "
                "het veel langer, tot twintig minuten, omdat de staafjes zich moeten herstellen.",
                "Dit is de kern van zorgzaam omgaan met slechthorendheid. Roepen vervormt de "
                "klanken en overstemt de lipbeweging die de persoon net gebruikt. Zorg dus eerst "
                "voor stilte en zicht op je gezicht, en spreek dan gewoon.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-oog-en-het-oor-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Volg het licht van buiten naar binnen: hoornvlies, pupil met de iris errond, "
                   "lens, netvlies, oogzenuw. Zo staat de eerste rij ook geordend. In de tweede "
                   "rij zitten de cellen en de plekken op dat netvlies.",
            waarom=[
                None,
                "Houd de gele en de blinde vlek goed uit elkaar. In de gele vlek zitten de "
                "kegeltjes het dichtst op elkaar, in de blinde vlek zit geen enkele cel omdat "
                "daar de oogzenuw vertrekt. Je merkt die blinde vlek niet, want je hersenen "
                "vullen hem op.",
                "Reken het aan jezelf na in een donkere kamer: je ziet vormen maar geen kleuren, "
                "en in je ooghoeken zie je beweging beter dan in het midden. Dat komt doordat de "
                "staafjes vooral buiten de gele vlek zitten.",
            ],
        ),
        dict(
            aanpak="Ook het oor volg je van buiten naar binnen: oorschelp, trommelvel, de drie "
                   "beentjes, het slakkenhuis. Daarnaast twee onderdelen die niets met horen te "
                   "maken hebben: de halfcirkelvormige kanalen voor je evenwicht en de buis van "
                   "Eustachius voor de druk.",
            waarom=[
                None,
                "De buis van Eustachius is dus geen onderdeel van het horen maar van de "
                "drukregeling. Bij kinderen is die buis korter en vlakker, en daarom krijgen zij "
                "veel vaker een middenoorontsteking.",
                "Het oor ruimt zichzelf op: het oorsmeer schuift met de huid naar buiten. Een "
                "wattenstaafje werkt dus tegen die beweging in, en bij harde oorsmeer is een "
                "huisarts of een spoeling de juiste weg.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over bescherming. Eén regel geeft de meeste antwoorden: "
                   "schade aan het oog en het oor is zelden omkeerbaar. Alles wat suggereert dat "
                   "het van zelf goed komt, is dus bijna altijd niet waar.",
            waarom=[
                "Niet waar, en dit is de belangrijkste van de zes. De haarcellen in het "
                "slakkenhuis groeien niet terug. Dat gepiep na een fuif verdwijnt wel, maar een "
                "deel van de schade blijft en stapelt op over de jaren.",
                "Waar, en dat is de grens die ook in de wet staat voor werk. Let op dat decibel "
                "niet gewoon optelt: tien decibel meer klinkt ongeveer dubbel zo luid en is tien "
                "keer zo veel geluidsenergie, dus boven 100 decibel gaat het snel.",
                "Niet waar. Ook bij slijpen, zagen, hameren en werken met warme vloeistoffen kan "
                "er iets in je oog komen. Het gevaar hangt af van wat je doet, niet van het vak "
                "waarin je zit.",
                "Waar, en dat verrast de meesten. Een donker glas laat je pupil opengaan terwijl "
                "het uv doorlaat, dus komt er meer schadelijk licht binnen dan zonder bril. Kijk "
                "dus naar het label en niet naar de donkerte van het glas.",
                None,
                "Waar. De vuistregel is twintig seconden in de verte kijken na twintig minuten "
                "scherm. Het gaat om de spier die je lens bolt: die staat bij dichtbij kijken "
                "voortdurend aangespannen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-spieren-beenderen-en-gewrichten-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De botten van de ledematen zitten in een vast patroon: één bot in het "
                   "bovenste deel, twee in het onderste. Dat geldt voor de arm en voor het been, "
                   "en daarmee heb je de eerste vier lijnen al. De tweede rij gaat over de taken "
                   "van het skelet, en dat zijn er vijf.",
            waarom=[
                None,
                "Dat een bot bloed aanmaakt en kalk opslaat, wordt het vaakst vergeten. Een "
                "skelet is geen dood geraamte maar levend weefsel dat voortdurend afbreekt en "
                "opbouwt; daarom kan een bot genezen en daarom kan het ook brozer worden.",
            ],
        ),
        dict(
            aanpak="Houd de soorten gewrichten uit elkaar aan hun beweging: een kogelgewricht "
                   "draait alle kanten op, een scharnier maar één richting, een rolgewricht "
                   "draait om zijn as, een zadelgewricht twee richtingen. In de tweede rij staan "
                   "de delen errond en de twee kwetsuren.",
            waarom=[
                "Bij de nek is er een nuance: het draaien van je hoofd om nee te zeggen gebeurt "
                "in het rolgewricht tussen de eerste twee wervels, terwijl het ja-knikken "
                "gebeurt tussen je schedel en de eerste wervel. Twee gewrichten dus, en het "
                "rolgewricht is dat van de nee-beweging.",
                "Houd band en pees uit elkaar met wat ze verbinden: band is bot aan bot, pees is "
                "spier aan bot. Daarom is een verstuiking een bandletsel en voelt ze anders dan "
                "een spierscheur.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over spieren en over wat ze kunnen. Onthoud één "
                   "eigenschap waaruit bijna alles volgt: een spier kan enkel trekken. Daarom "
                   "komen ze in paren, en daarom hef je zwaar gewicht met de spieren die het "
                   "kunnen trekken en niet met je rug.",
            waarom=[
                "De laatste zin is het hele antwoord: een spier kan niet duwen. Elk gewricht dat "
                "in twee richtingen beweegt, heeft dus minstens twee spieren nodig, en terwijl de "
                "ene trekt, laat de andere los.",
                "Let op de drie soorten spieren. Enkel de skeletspieren spreek je bewust aan; de "
                "gladde spieren en de hartspier werken zonder dat je eraan denkt, en dat is ook "
                "de reden dat je je hart niet kan stilleggen.",
                "Reken het mechanisch na: met een gebogen rug werkt je wervelkolom als een hefboom "
                "met een heel korte arm, en dan wordt de kracht op je tussenwervelschijven veel "
                "groter dan het gewicht van de doos. Recht blijven en plooien in je knieën haalt "
                "die hefboom weg.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-zenuwstelsel-en-de-reflexen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het zenuwstelsel wordt twee keer ingedeeld, en dat is wat verwarring geeft. "
                   "De eerste indeling is naar plaats: centraal tegenover perifeer. De tweede is "
                   "naar sturing: willekeurig tegenover autonoom, en dat autonome deel valt nog "
                   "eens uiteen in sympathicus en parasympathicus.",
            waarom=[
                "Onthoud de sympathicus als het gaspedaal en de parasympathicus als de rem: de "
                "eerste maakt je klaar om te vluchten of te vechten, de tweede om te rusten en te "
                "verteren. Ze werken allebei altijd, en het evenwicht tussen de twee verschuift.",
                "Let op de synaps. Dat is geen onderdeel van een cel maar de ruimte ertussen, en "
                "het signaal steekt die over met stoffen en niet met elektriciteit. Daarom werken "
                "veel medicijnen juist op die plaats in.",
            ],
        ),
        dict(
            aanpak="Leer de hersendelen aan hun soort taak: de grote hersenen doen wat je bewust "
                   "doet, de kleine hersenen de fijne afstemming van beweging, de hersenstam wat "
                   "nooit mag stoppen. De hypothalamus regelt het innerlijke evenwicht en de "
                   "thalamus geeft door.",
            waarom=[
                "Merk op waarom de hersenstam zo kwetsbaar is: daar zit wat je nooit bewust "
                "stuurt en wat ook nooit mag uitvallen. Een letsel daar is daardoor veel "
                "gevaarlijker dan hetzelfde letsel in de grote hersenen.",
                "Het punt van deze vraag is de vertraging. Een bloeding in de schedel geeft "
                "soms urenlang geen klachten, en daarom beoordeel je een hersenschudding niet "
                "aan hoe iemand er onmiddellijk na de val uitziet.",
            ],
        ),
        dict(
            aanpak="Een reflexboog heeft dezelfde schakels als de gewone weg van prikkel tot "
                   "reactie, maar met het ruggemerg in het midden in plaats van de hersenen. "
                   "Daarom zijn het er vijf en niet zes, en daarom komt de bewuste gedachte pas "
                   "achteraf.",
            waarom=[
                "Let op de laatste lijn: je merkt de reflex pas als hij al gebeurd is. De "
                "hersenen krijgen het signaal wel, maar langs een andere weg en dus later.",
                None,
                "Twee voorbeelden volstaan. Ze hebben alle hetzelfde kenmerk: ze beschermen iets "
                "wat niet kan wachten op een beslissing, namelijk je huid, je oog of je luchtweg.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gezondheid-in-kaart-gordon-en-het-icf-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De patronen van Gordon zijn een lijst om een mens volledig in kaart te "
                   "brengen. Zoek bij elke vraag naar het werkwoord: eten hoort bij voeding, "
                   "slapen bij slaap en rust, zich wassen bij activiteit. Een vraag over andere "
                   "mensen hoort bij rollen en relaties.",
            waarom=[
                "Let erop dat zich kunnen wassen en kleden bij activiteit en beweging hoort en "
                "niet bij hygiëne. Gordon kijkt naar wat iemand kan, niet naar wat hij doet.",
                "Dit is de kern van zo'n lijst. Hij bestaat juist om te verhinderen dat je alleen "
                "vraagt naar wat de persoon zelf vermeldt. Wie over zijn knie klaagt, vertelt "
                "niet spontaan dat hij daardoor niemand meer ziet.",
            ],
        ),
        dict(
            aanpak="Het ICF kijkt naar drie lagen van hetzelfde probleem: het lichaam (functies "
                   "en structuren), de persoon (activiteiten) en zijn leven met anderen "
                   "(participatie). Errond staan twee soorten factoren: externe, buiten de "
                   "persoon, en persoonlijke, in de persoon.",
            waarom=[
                "Vergelijk de eerste drie lijnen: het is drie keer dezelfde heup. Het versleten "
                "gewricht is de structuur, het niet kunnen traplopen de activiteit, en het "
                "wegblijven van de kaartclub de participatie. Zo hoort het ICF gelezen.",
                "Let op wat hier niet gezegd wordt: de knie is niet erger bij de tweede persoon. "
                "Wat verschilt, is de omgeving, en net daarom kan je aan zo'n situatie iets doen "
                "zonder de knie te genezen.",
                "Dit is het nuttigste verschil van het hele hoofdstuk. Zelfstandigheid is kunnen "
                "zonder hulp; participatie is meedoen. De eerste kan heel hoog zijn terwijl de "
                "tweede bijna nul is, en dan is er nog altijd een probleem.",
            ],
        ),
        dict(
            aanpak="De twee laatste oefeningen vragen om een omschrijving én een houding. Ken de "
                   "definitie van de Wereldgezondheidsorganisatie woordelijk genoeg om ze op te "
                   "schrijven, en ken er één kritiek bij; dat tweede is wat het verschil maakt op "
                   "een examen.",
            waarom=[
                "De kritiek is scherper dan ze lijkt. Met die definitie is iemand met diabetes "
                "of met een beperking nooit gezond, wat niet klopt met hoe die mensen zelf "
                "leven. Daarom zoekt men al jaren naar een andere omschrijving.",
                "Positieve gezondheid is het antwoord op die kritiek, van Machteld Huber. In de "
                "zorg verandert dat de eerste vraag: niet wat is er mis, maar wat wil u opnieuw "
                "kunnen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ziek-zijn-en-eerste-hulp-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier soorten ziekteverwekkers, en één regel die telt: antibiotica werken "
                   "enkel tegen bacteriën. Leer bij elke ziekte dus eerst de verwekker en pas "
                   "daarna de behandeling. De begrippen in de derde rij gaan over het verloop "
                   "van een ziekte en niet over de oorzaak.",
            waarom=[
                None,
                "Noem in je antwoord beide delen. Het eerste is dat het niet helpt, het tweede "
                "dat het schaadt: elke nodeloze kuur geeft bacteriën een kans om er ongevoelig "
                "voor te worden. Daarom is antibioticaresistentie een probleem van iedereen.",
                "Let op de incubatietijd, want die verklaart waarom besmettelijke ziekten zich "
                "zo snel verspreiden: je bent al besmettelijk voor je weet dat je ziek bent.",
            ],
        ),
        dict(
            aanpak="De eerste stappen van eerste hulp staan in een vaste orde, en die orde is er "
                   "om een reden: eerst jezelf, want een tweede slachtoffer helpt niemand, dan "
                   "het bewustzijn, dan hulp, dan de ademhaling. Leer ook de nummers en de "
                   "cijfers van de reanimatie uit het hoofd.",
            waarom=[
                "Let op de laatste lijn: iemand die niet goed bij bewustzijn is, mag niets te "
                "drinken krijgen, want hij kan zich verslikken. In de eigenlijke richtlijn roep "
                "je meteen om hulp van omstaanders en laat je 112 bellen zodra je weet dat de "
                "ademhaling niet normaal is; ben je alleen, dan bel je zelf eerst.",
                "Ken deze cijfers uit het hoofd, want in een noodgeval zoek je ze niet op: 30 op "
                "2, honderd tot honderdtwintig per minuut, midden op het borstbeen. En onthoud "
                "dat de 112-operator je door de reanimatie praat als je het niet meer weet.",
            ],
        ),
        dict(
            aanpak="Vier situaties, en bij elk hetzelfde patroon: wat doe je, wat doe je niet, "
                   "en wanneer ga je naar een arts. Dat tweede deel is waar de punten zitten, "
                   "want bij elk van deze vier bestaat er een oude gewoonte die juist schaadt.",
            waarom=[
                "Tien minuten is lang, en dat is net het punt: de meeste mensen koelen te kort. "
                "Zalf, ijs en tandpasta houden de warmte vast of beschadigen de huid, en een "
                "blaar is een steriel verband dat je niet opent.",
                "Het hoofd achterover is de oude gewoonte die hier fout is: het bloed loopt dan "
                "naar je maag en je kan er misselijk van worden. Knijp de zachte punt van de "
                "neus dicht en niet het harde bot erboven.",
                "Zijligging dient om de luchtweg vrij te houden als iemand zou braken. Blijf de "
                "ademhaling volgen, want stopt ze, dan begin je te reanimeren.",
                "Dit is de regel van rust, ijs, druk en hoog, met het ijs altijd in een doek: "
                "rechtstreeks op de huid geeft koudeschade. Niet kunnen stappen is het teken dat "
                "er meer dan een verstuiking kan zijn.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gezondheid-bevorderen-preventie-voeding-en-beweging-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie soorten preventie volgen de tijdlijn van een ziekte: primair voor ze "
                   "er is, secundair terwijl ze er al is maar nog niet voelbaar, tertiair als ze "
                   "er is en blijft. Vraag je dus bij elk voorbeeld af waar de persoon op die "
                   "tijdlijn staat.",
            waarom=[
                "Let op het rookverbod. Dat is primaire preventie, al is het geen medische "
                "handeling: een maatregel voor een hele bevolking kan evengoed preventie zijn als "
                "een inenting. Vaak is ze zelfs doeltreffender.",
                None,
            ],
        ),
        dict(
            aanpak="De voedingsdriehoek werkt met verhoudingen: hoe breder de laag, hoe meer je "
                   "er best van eet. Alles van plantaardige oorsprong zit in de groene lagen, "
                   "dierlijke producten in de oranje, en wat buiten de driehoek staat hoort "
                   "nergens in een dagmenu thuis.",
            waarom=[
                "Merk op dat de rode bol buiten de driehoek staat en niet onderaan. Dat is geen "
                "tekenfout: die producten horen niet in een evenwichtig menu en zijn een "
                "uitzondering, niet de kleinste laag.",
                "Dit is het verschil met de oude voedingsdriehoek. De nieuwe zet water bovenaan "
                "omdat het breedste deel het meeste is; de driehoek zegt dus niets over hoe "
                "belangrijk een voedingsstof is.",
                "Toets je eigen menu aan drie dingen: staat er bij elke maaltijd iets uit de "
                "groene lagen, is water de drank, en komt de rode bol er maar één keer of niet "
                "in voor? Dan is het goed, welke gerechten je ook koos.",
            ],
        ),
        dict(
            aanpak="Ken de richtlijnen met hun getallen: zestig minuten per dag voor een jongere, "
                   "honderdvijftig minuten per week voor een volwassene, twee keer per week "
                   "spierversterkend. En onthoud de praattoets, want die is handiger dan een "
                   "hartslagmeter.",
            waarom=[
                "De praattoets is iets wat je in elke les sport kan gebruiken: kan je nog praten "
                "maar niet zingen, dan beweeg je matig; gaat praten moeizaam, dan is het "
                "intensief. Daarvoor heb je geen toestel nodig.",
                None,
                "Dit is de belangrijkste nuance van de bundel. Lang stilzitten is een eigen "
                "risico, naast te weinig bewegen. Daarom luidt de richtlijn ook: sta elk uur "
                "even op, ook op een dag dat je gesport hebt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kwaliteitsbewust-handelen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De begrippen van deze reeks gaan alle over dezelfde vraag: van wie is dit "
                   "leven? Autonomie en waardigheid zijn van de persoon, het beroepsgeheim en de "
                   "deontologische code zijn jouw plichten. Bij een weigering is dus niet de "
                   "vraag hoe je overtuigt, maar hoe je de keuze eerbiedigt.",
            waarom=[
                None,
                "Let op de twee dingen die je zeker niet doet, want daar zitten de punten. Niet "
                "dwingen is het ene; het ook niet gewoon laten vallen is het andere. Een "
                "weigering is informatie: ze gaat het dossier in, zodat het team ernaar kan "
                "zoeken.",
            ],
        ),
        dict(
            aanpak="PDCA is een cirkel van vier Engelse woorden: plan, do, check, act. Onthoud "
                   "vooral de derde en de vierde, want die worden in de praktijk het vaakst "
                   "overgeslagen: nagaan of het werkte, en dan echt bijsturen.",
            waarom=[
                "Dat het een cirkel is en geen lijstje, is het hele punt. Na act begin je opnieuw "
                "bij plan, want wat je bijstuurde moet je ook weer nagaan.",
                "Let op de check in dit voorbeeld: de valincidenten tellen. Zonder dat cijfer "
                "weet je niet of de lampjes hielpen, en dan is act gokwerk. Noem bij een "
                "PDCA-oefening dus altijd wát je gaat meten.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over jezelf in je werk: fouten, reflectie en grenzen. "
                   "Bij alle drie wordt niet naar een regel gevraagd maar naar een houding, dus "
                   "antwoord met wat je doet en waarom het voor de bewoner uitmaakt.",
            waarom=[
                "Het punt is niet eerlijkheid om de eerlijkheid. Een gemelde fout maakt een "
                "oorzaak zichtbaar, en daarom spreekt men in de zorg van een veilige meldcultuur: "
                "melden mag geen straf opleveren, anders meldt niemand nog iets.",
                None,
                "Drie van de genoemde volstaan. Merk op dat ze alle buiten de zorgtaken liggen: "
                "je merkt het eerst aan je slaap, je humeur en je weg naar het werk. Zulke "
                "signalen melden is geen zwakte maar deel van kwaliteitsvol werk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voedingsstoffen-en-een-evenwichtig-dagmenu-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes voedingsstoffen met elk hun rol, en drie getallen die je uit het hoofd "
                   "moet kennen: koolhydraten en eiwitten geven 4 kcal per gram, vet 9 en alcohol "
                   "7. Met die drie cijfers kan je elke energieberekening van dit hoofdstuk maken.",
            waarom=[
                None,
                "Merk op dat vet meer dan dubbel zo veel energie geeft als koolhydraten. Daarom "
                "weegt een beetje boter of saus zwaarder door in een dagmenu dan een flinke "
                "portie pasta, en daarom staat alcohol met zijn 7 kcal ook niet voor niets in dit "
                "rijtje.",
            ],
        ),
        dict(
            aanpak="Leer de vitaminen aan hun taak en niet aan hun letter alleen. Twee groepen "
                   "om uit elkaar te houden: A, D, E en K lossen op in vet, B en C in water. Dat "
                   "verschil verklaart waarom je de ene kan opslaan en de andere elke dag nodig "
                   "hebt.",
            waarom=[
                None,
                "Let op de laatste twee lijnen, want die zijn praktisch. IJzer uit planten wordt "
                "slecht opgenomen, maar vitamine C erbij helpt: spinazie met een partje citroen "
                "of linzen met paprika. Dat is iets wat je in een keuken echt gebruikt.",
            ],
        ),
        dict(
            aanpak="Reken altijd in twee stappen. Eerst de energie per voedingsstof, dus de "
                   "grammen maal 4, 4 en 9, en dan optellen. Voor een percentage deel je de "
                   "energie uit die stof door het totaal, en nooit de grammen door de grammen.",
            waarom=[
                "60 × 4 = 240, 10 × 4 = 40 en 5 × 9 = 45, samen 325 kcal.",
                "45 gedeeld door 325 = 0,138, dus ongeveer 13,8 procent. Reken dus met de "
                "kilocalorieën en niet met de grammen: op gewicht is dat vet maar 7 procent van "
                "de voedingsstoffen in die portie, en dat zou een heel ander beeld geven.",
                "325 gedeeld door 2 400 = 0,135, dus ongeveer 13,5 procent van de dagbehoefte.",
                "Noem in je antwoord de richtlijn, want daarmee toon je waaraan je het afmeet: "
                "ongeveer 30 tot 35 procent van de energie uit vet. En let op dat je niet gewoon "
                "minder gaat eten: je vervangt vet door volkoren en groenten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voedselveiligheid-en-voedselhygiene-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bacteriën hebben vier dingen nodig: warmte, vocht, voedsel en tijd. Haal er "
                   "één weg en ze groeien niet. Daar komen alle regels van dit hoofdstuk uit, en "
                   "ook de getallen: koel houden haalt de warmte weg, snel verwerken haalt de "
                   "tijd weg, verhitten doodt wat er al is.",
            waarom=[
                "Let op listeria. Die is bijzonder omdat ze zich ook in de koelkast nog "
                "vermeerdert, dus koelen volstaat er niet. Daarom wordt rauwmelkse kaas en "
                "voorverpakte vis afgeraden aan zwangere vrouwen.",
                "Onthoud de vier getallen: 4 tot 7 graden in de koelkast, −18 in de diepvries, "
                "75 graden kerntemperatuur voor gevogelte, 20 seconden handen wassen. Dat zijn "
                "ook precies de cijfers die in een keukeninspectie nagekeken worden. Ontdooid "
                "vlees mag je wel opnieuw invriezen nadat je het bereid hebt.",
            ],
        ),
        dict(
            aanpak="Houd de twee datums goed uit elkaar: te gebruiken tot is een veiligheidsgrens "
                   "en ten minste houdbaar tot een kwaliteitsgrens. De eerste staat op wat snel "
                   "bederft, zoals verse vis en gehakt; de tweede op droge en lang bewaarbare "
                   "waren.",
            waarom=[
                None,
                "Bij een ten minste houdbaar tot mag je dus zelf oordelen met je ogen, je neus "
                "en een beetje smaak. Bij een te gebruiken tot nooit: daar kan het bederf er niet "
                "aan te zien zijn.",
                "Noem in je antwoord beide redenen. De koelkast zelf opwarmen is er één, maar het "
                "tweede is belangrijker: warm eten dat langzaam afkoelt, staat uren in de zone "
                "tussen 4 en 60 graden, en net daar groeien bacteriën het snelst.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over werken in een keuken. Toets ze aan de vier "
                   "groeivoorwaarden en aan één extra vraag: kan hier iets van de ene plaats naar "
                   "de andere overgaan? Alles wat vocht vasthoudt of wat je niet kan "
                   "schoonmaken, is in een keuken verdacht.",
            waarom=[
                "HACCP is een werkwijze en geen lijst regels: je zoekt zelf de gevaren in jouw "
                "keuken en legt vast op welke punten je ze beheerst en nagaat. Daarom ziet een "
                "HACCP-plan in elke zaak anders uit.",
                "Niet waar. Een keukenhanddoek blijft vochtig en wordt tientallen keren gebruikt, "
                "dus hij is een ideale plaats voor bacteriën. Papier gebruik je één keer en gooi "
                "je weg.",
                None,
                "Niet waar. Onder een ring of een uurwerk blijft vuil en vocht zitten, je kan er "
                "niet onder wassen, en een steentje of een bandje kan in het eten vallen.",
                "Waar. Dat dagelijkse briefje is geen papierwerk om het papierwerk: zonder "
                "meting weet niemand dat de koelkast al drie dagen op 12 graden staat.",
                "Waar, en dit is de belangrijkste van de zes. Wie maagdarmklachten heeft, kan de "
                "verwekker doorgeven aan alles wat hij aanraakt. Dat melden is een plicht en geen "
                "keuze.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voedsel-bewaren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Elke bewaartechniek haalt een van de vier groeivoorwaarden weg. Koelen en "
                   "diepvriezen halen de warmte weg, drogen en zouten het water, inmaken "
                   "verandert de zuurtegraad, en steriliseren doodt wat er al is. Zoek bij elke "
                   "techniek dus welke voorwaarde verdwijnt.",
            waarom=[
                "Let op het verschil tussen diepvriezen en steriliseren. Diepvriezen doodt niets: "
                "het legt de bacteriën stil doordat het water bevroren is. Daarom zijn ze na het "
                "ontdooien weer actief, en moet je ontdooid voedsel snel verwerken.",
                "Pasteuriseren en steriliseren verschillen in temperatuur en in gevolg. "
                "Gepasteuriseerde melk moet in de koelkast en blijft enkele dagen goed; "
                "gesteriliseerde of UHT-melk kan maanden in de kast, maar smaakt anders omdat de "
                "hitte ook de eiwitten verandert.",
            ],
        ),
        dict(
            aanpak="Waar iets bewaard wordt, hangt af van twee dingen: hoe snel het bederft en "
                   "of koude de kwaliteit schaadt. Bij vlees, vis en zuivel beslist de "
                   "veiligheid; bij aardappelen, tomaten en bananen beslist de smaak, en die "
                   "worden door de koelkast juist slechter.",
            waarom=[
                None,
                "Dit is zetmeel dat in suiker omgezet wordt, en het is omkeerbaar: laat je "
                "koude aardappelen enkele dagen op kamertemperatuur staan, dan verdwijnt die "
                "zoete smaak weer grotendeels.",
                "Vetten nemen geuren het makkelijkst op, en dat is de reden dat juist boter en "
                "melk naar meloen of naar kaas gaan smaken. Afdekken is dus niet alleen tegen "
                "uitdrogen.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over verspilling. Bij de eerste oefening worden er vier "
                   "manieren gevraagd, dus geef er echt vier en maak ze concreet: zeggen dat je "
                   "minder moet weggooien is geen manier.",
            waarom=[
                "Vier van de genoemde volstaan. Merk op dat ze alle vier voor het weggooien "
                "ingrijpen: bij het kopen, bij het opbergen, bij het opscheppen en bij het "
                "bewaren. Dat is ook waarom een boodschappenlijst het meeste oplevert.",
                "Dit verschil is belangrijk voor wat eraan te doen is. Bij de producent gaat het "
                "om normen en om de vraag van de winkel, dus daar helpt het veranderen van die "
                "normen; bij de consument gaat het om gewoonten in huis.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-boodschappen-doen-en-de-tafel-dekken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De eenheidsprijs is de prijs per kilo of per liter, en je berekent ze door de "
                   "prijs te delen door het gewicht in kilo. Zet beide pakken om naar dezelfde "
                   "eenheid voor je vergelijkt; dat is de enige manier om twee verschillende "
                   "groottes naast elkaar te leggen.",
            waarom=[
                None,
                "2,45 gedeeld door 0,5 kg = 4,90 euro per kilo. Deel dus door het gewicht in "
                "kilo en niet in gram, of zet je uitkomst maal duizend.",
                "3,45 gedeeld door 0,75 kg = 4,60 euro per kilo. Het grote pak is hier dus 30 "
                "cent per kilo goedkoper.",
                "Let op het tweede deel van het antwoord, want dat vergeten de meesten: een groot "
                "pak dat je weggooit, is per opgegeten kilo het duurste van de twee. De "
                "eenheidsprijs is dus niet het enige dat telt.",
            ],
        ),
        dict(
            aanpak="Een etiket lees je op drie plaatsen: de ingrediëntenlijst zegt wat erin zit "
                   "en in welke verhouding, de voedingswaardetabel zegt hoeveel energie en "
                   "voedingsstoffen, en de allergenen staan er verplicht in het vet. De orde van "
                   "de ingrediënten is de sleutel.",
            waarom=[
                None,
                "Reken het zelf om, want daar gaat het mis. Weegt een koekje 25 gram, dan is de "
                "tabel vier keer te veel; is je portie 150 gram pasta, dan anderhalve keer te "
                "weinig. Veel producten vermelden daarom ook een kolom per portie.",
                "Het voorbeeld E300 is het punt van deze vraag: dat is ascorbinezuur, dus gewoon "
                "vitamine C. Een E-nummer betekent enkel dat de stof toegelaten en onderzocht is, "
                "niet dat ze kunstmatig of schadelijk is.",
            ],
        ),
        dict(
            aanpak="Het dekken volgt twee regels. Mes en lepel rechts, vork links, en alles in de "
                   "orde van de gangen van buiten naar binnen. De snijkant van het mes kijkt "
                   "altijd naar het bord. Met die twee regels kan je elk couvert zelf opbouwen.",
            waarom=[
                "Het glas staat bij de punt van het mes, dus rechtsboven, en het broodbordje aan "
                "de andere kant, linksboven. Dat is geen willekeur: je neemt je glas met je "
                "rechterhand en je brood met je linker.",
                "Let bij je tekening op de orde van buiten naar binnen: de vis komt eerst, dus "
                "liggen het vismes en de visvork aan de buitenkant. Zet je het omgekeerd, dan "
                "pakt de gast bij de eerste gang het verkeerde stuk.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-interieurzorg-ruimtes-vuil-en-technieken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Soort vuil en soort middel horen bij elkaar. Vet vraagt een alkalisch middel, "
                   "kalk een zuur, bacteriën een desinfecterend middel. Zoek dus eerst wat het "
                   "vuil ís, en kies dan het middel; omgekeerd werken met één fles voor alles "
                   "haalt bij kalk en bij vet niets uit.",
            waarom=[
                "Let op de laatste twee lijnen: ze zijn geen vuil zoals de andere. Bacteriën zie "
                "je niet en zijn er toch, en een kras is schade die met geen enkel middel weggaat. "
                "Wie dat laatste blijft wrijven, maakt het erger.",
                "Op marmer en op natuursteen nooit een zuur middel, en dat is de ene lijn uit dit "
                "rijtje die echt geld kost: azijn of ontkalker bijt de steen aan en laat matte "
                "vlekken na die niet meer weggaan.",
                "Chloorgas, en dat is geen theorie: dat gebeurt elk jaar in gewone badkamers. "
                "Spoel dus goed tussen twee middelen, en zet nooit een tweede product op een "
                "oppervlak dat nog van het eerste nat is.",
            ],
        ),
        dict(
            aanpak="De technieken staan in opklimmende orde: droog, vochtig, nat, en als het "
                   "nodig is desinfecteren. Kies altijd de lichtste techniek die het vuil "
                   "wegneemt, want elke stap verder kost meer water, meer middel en meer tijd, "
                   "en kan het materiaal beschadigen.",
            waarom=[
                None,
                "Dit is de belangrijkste regel van het hoofdstuk, en ze wordt het vaakst "
                "overtreden. Reinigen en desinfecteren zijn twee aparte stappen in die orde; "
                "spuiten op een vuile plank doet niets dan het etiket geloven.",
                "Noem beide redenen. Van boven naar onder is logisch, maar van droog naar nat "
                "wordt vergeten: eerst stoffen en stofzuigen, dan dweilen. Omgekeerd maak je van "
                "het stof slijk en veeg je het uit over de vloer.",
            ],
        ),
        dict(
            aanpak="Elke ruimte heeft zijn eigen vuil en zijn eigen gevaar: de keuken vet en "
                   "kruisbesmetting, de badkamer kalk en vocht, het toilet bacteriën, de "
                   "slaapkamer stof. De trap is een buitenbeentje: daar gaat het niet om vuil "
                   "maar om vallen.",
            waarom=[
                None,
                "Kleurcodes zijn hier de praktische oplossing: in de zorg heeft het toilet "
                "bijvoorbeeld rood en de keuken geel. Zo kan niemand zich vergissen, ook niet "
                "wie de taal niet goed kent of nieuw is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-methodisch-veilig-en-duurzaam-schoonmaken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Methodisch werken is zes stappen, met het eigenlijke schoonmaken pas op de "
                   "vierde plaats. De drie stappen ervoor bepalen of het werk lukt, en de twee "
                   "erna horen er even hard bij. Begin je bij stap vier, dan sta je halverwege "
                   "zonder het juiste middel.",
            waarom=[
                None,
                "Een natte dweil die in de emmer blijft, is na een dag een bron van bacteriën en "
                "van geur. Daarom hoort het uitwassen en drogen bij het werk; de volgende "
                "schoonmaak begint anders met vuil materiaal.",
                "Let op de laatste zin van het antwoord: je meldt wat je niet gedaan hebt. Dat is "
                "het verschil tussen kiezen en overslaan, en het is precies wat een goede "
                "zorgkundige onderscheidt.",
            ],
        ),
        dict(
            aanpak="Veilig werken met middelen gaat over drie dingen: lezen wat erop staat, de "
                   "juiste bescherming dragen, en weten wat je doet als het misgaat. Ken de "
                   "eerste hulp per ongeval uit het hoofd, en ook het nummer van het "
                   "Antigifcentrum.",
            waarom=[
                "Nooit overgieten in een andere fles: dat is de regel waar ongelukken met "
                "kinderen vandaan komen. Zonder het juiste etiket weet niemand wat erin zit, ook "
                "de arts niet.",
                "Let op het verschil tussen huid en oog: spoelen doe je in beide gevallen, maar "
                "bij een oog minstens tien minuten en daarna altijd naar een arts. En bij "
                "inslikken nooit doen braken, want een bijtend middel beschadigt bij het "
                "opkomen een tweede keer.",
            ],
        ),
        dict(
            aanpak="Duurzaam schoonmaken gaat niet over een ander product kopen maar over minder "
                   "en juister gebruiken. De vier manieren die gevraagd worden, moeten dus "
                   "concreet zijn: doseren, microvezel, navullen, koud water, herbruikbare "
                   "doeken.",
            waarom=[
                "Vier van de genoemde volstaan. Doseren is daarbij het eerste, want het kost "
                "niets en levert meteen op: de dop van een fles is bijna altijd ruimer dan de "
                "aanbevolen dosis.",
                "Noem beide gevolgen, want het tweede verbaast: overdoseren maakt vuiler. De film "
                "die achterblijft, is plakkerig en houdt nieuw stof vast, zodat je sneller "
                "opnieuw moet poetsen.",
                "Het woord mechanisch is hier de kern. Microvezel neemt het vuil mee door de "
                "vorm van de vezels, dus niet door een middel. Daarom werkt ze met water alleen "
                "al, en daarom moet je ze ook niet met wasverzachter wassen: dat verstopt de "
                "vezels.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zorg-voor-de-woon-en-leefomgeving-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij elk risico hoort een maatregel die het risico wegneemt en niet enkel "
                   "waarschuwt. Zeg dus niet opletten maar wegnemen, vastleggen, bijlichten of "
                   "wegzetten. De meeste ongevallen in huis zijn vallen, en de meeste vallen "
                   "gebeuren op een gelijkvloers.",
            waarom=[
                "Let op de trap: twee schakelaars, boven en onder. Eén schakelaar betekent dat "
                "iemand de trap in het donker op of af moet, en dat is net wat je wil vermijden.",
                "Het antwoord moet die zwaarte noemen: na een heupbreuk komt een groot deel van de "
                "ouderen niet meer terug naar de eigen woning. Daarom is een antislipmat van "
                "tien euro een van de nuttigste dingen in de thuiszorg.",
            ],
        ),
        dict(
            aanpak="Comfort in huis heeft vaste getallen: ongeveer 20 graden in de leefruimte, 16 "
                   "tot 18 in de slaapkamer, en elke dag kort en flink verluchten. Onthoud ook "
                   "waarom je verlucht: vocht, CO2 en geuren weg, en niet om af te koelen.",
            waarom=[
                None,
                "Reken het aan het vocht af: een kier laat de muren afkoelen, en op een koude "
                "muur slaat vocht neer. Een kwartier wijd open wisselt de lucht terwijl de muren "
                "hun warmte houden, en dat is precies het omgekeerde effect.",
                "Merk op dat het antwoord met de oorzaak begint en niet met het middel. Schimmel "
                "wegpoetsen zonder de kast te verzetten, betekent dat ze binnen de maand "
                "terugkomt.",
            ],
        ),
        dict(
            aanpak="De laatste reeks is tweeledig: afval sorteren en hulpmiddelen kennen. Bij het "
                   "afval beslist het materiaal en niet wat er in zat; bij de hulpmiddelen hoort "
                   "bij elke handeling één toestel, en die namen moet je kunnen gebruiken in een "
                   "gesprek met een ergotherapeut.",
            waarom=[
                "Let op de laatste twee: een batterij en een restje verf mogen nooit bij het "
                "restafval. Die horen bij het klein gevaarlijk afval, want de stoffen erin komen "
                "anders in de bodem en in het water terecht.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-linnenzorg-sorteren-wassen-en-strijken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Sorteren gebeurt in die orde: eerst op kleur, dan op temperatuur en "
                   "textielsoort. En lees altijd het etiket, want de symbolen beslissen. Vier "
                   "vormen om te kennen: teil is wassen, driehoek is bleken, vierkant is drogen, "
                   "strijkijzer is strijken, en een kruis betekent niet doen.",
            waarom=[
                None,
                "De punten in het strijkijzer en in de teil geven de temperatuur: één punt is "
                "lauw, drie punten is heet. Ken je enkel die twee uitersten, dan kan je al bijna "
                "elk etiket lezen.",
            ],
        ),
        dict(
            aanpak="De temperatuur hangt van twee dingen af: hoe vuil het is en welk textiel het "
                   "is. Stevig wit katoen kan 60 graden, gekleurd katoen en synthetisch 30 of 40, "
                   "wol enkel het wolprogramma. Vul de trommel losjes, want water en wasmiddel "
                   "moeten overal bij kunnen.",
            waarom=[
                None,
                "Twee oorzaken volstaan. Merk op dat te veel wasmiddel ook grauw maakt: de resten "
                "blijven in de vezel zitten. Grauw is dus niet altijd te weinig gewassen; het is "
                "vaak te veel product.",
                "Dit is de reden waarom zestig graden in de zorg bestaat. Bij dertig graden "
                "overleven veel verwekkers de was, en ze kunnen dan ook in de machine zelf "
                "blijven zitten. Draai daarom af en toe een warm programma leeg.",
            ],
        ),
        dict(
            aanpak="Bij vlekken geldt één regel die bijna alles verklaart: behandelen voor je "
                   "wast, en bij eiwitvlekken altijd koud. Bij het strijken geldt de temperatuur "
                   "van het etiket, en voor een hemd een vaste orde: eerst de kraag, dan de "
                   "manchetten, dan de rug.",
            waarom=[
                "Let op het verschil tussen de twee soorten vlekken. Bloed, ei en melk zijn "
                "eiwitten en moeten koud; vet en olie hebben juist warmte nodig. Doe je het "
                "omgekeerd, dan zet je de vlek vast.",
                "De eiwitten stollen, net zoals een ei in de pan. Dat is onomkeerbaar, en daarom "
                "staat deze regel apart in het blad: koud water is bij bloed geen voorkeur maar "
                "een voorwaarde.",
                "Wol en zijde met één punt, en bij wol een doek ertussen; katoen en linnen met "
                "drie punten. Strijk zijde langs de binnenkant, want warm ijzer op de goede kant "
                "geeft glanzende plekken die er niet meer uitgaan.",
            ],
        ),
    ],
)

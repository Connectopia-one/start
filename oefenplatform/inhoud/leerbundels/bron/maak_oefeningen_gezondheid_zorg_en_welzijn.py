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

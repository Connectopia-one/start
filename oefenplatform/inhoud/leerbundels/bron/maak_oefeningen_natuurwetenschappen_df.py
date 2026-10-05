# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen 🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

Gebouwd zoals de leerbundels van deze categorie, in `maak_natuurwetenschappen_df.py`:
de reeksen die even goed op deze fiche passen komen van 🚀 Boost doorstroom, de
reeksen die daar over leerstof gaan die deze fiche niet vraagt, vallen weg of
worden vervangen. De bundel over biologische feedback is helemaal nieuw, want
die kop staat alleen in deze fiche zo.

Wie hier iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/natuurwetenschappen.json`, naast de leerbundel
van hetzelfde thema en naast de fiche zelf. De oefeningen zijn met opzet ándere
opgaven dan die van het hoofdstuk op het scherm.

Onderaan loopt dezelfde controle als bij de leerbundels: geen woord uit de
doorstroomfiche dat hier niet thuishoort.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel
import maak_oefeningen_natuurwetenschappen_boost as doorstroom
import maak_natuurwetenschappen_df as leerbundels

VAK = "Natuurwetenschappen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "120px"
WW = "185px"
WL = "250px"

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een rekenopgave: schrijf je tussenstappen op, ook als je ze in je hoofd kan maken.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

# Dezelfde lijst verboden woorden als bij de leerbundels.
VERBODEN = leerbundels.VERBODEN

MEE = [
    ("biodiversiteit-en-micro-organismen",
     "micro-organismen-het-microbioom-en-bewaring",
     "Micro-organismen, het microbioom en bewaring"),
    ("voortplanting-en-de-hormonale-regeling", None, None),
    ("mengsels-en-zuivere-stoffen", None, None),
    ("enkelvoudige-en-samengestelde-stoffen-en-chemische-reacties",
     "chemische-formules-en-chemische-reacties",
     "Chemische formules en chemische reacties"),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", None, None),
    ("elektriciteit-en-de-wet-van-ohm",
     "elektriciteit-de-wet-van-ohm-en-veiligheid",
     "Elektriciteit, de wet van Ohm en veiligheid"),
    ("veilig-werken-meten-en-levensreddend-handelen", None, None),
    ("grootheden-eenheden-en-wetenschappelijk-onderzoek", None, None),
]

ORDE = [
    "biologische-feedback-en-homeostase",
    "micro-organismen-het-microbioom-en-bewaring",
    "voortplanting-en-de-hormonale-regeling",
    "mengsels-en-zuivere-stoffen",
    "chemische-formules-en-chemische-reacties",
    "de-bouw-van-het-atoom-en-het-periodiek-systeem",
    "energieomzettingen-vermogen-en-rendement",
    "warmte-faseovergangen-en-inwendige-energie",
    "kracht-als-vector-en-bewegingstoestand",
    "druk-in-het-dagelijkse-leven",
    "elektriciteit-de-wet-van-ohm-en-veiligheid",
    "veilig-werken-meten-en-levensreddend-handelen",
    "grootheden-eenheden-en-wetenschappelijk-onderzoek",
]


def tekst_van(oef) -> str:
    """De tekst van een oefening, zonder de breedtes van de invulvakjes."""
    stukken = []
    for d in oef:
        if isinstance(d, str) and d.endswith("px"):
            continue
        stukken.append(str(d))
    return " ".join(stukken)


def _bron(kort: str) -> dict:
    sleutel = VOOR + kort + OUD
    if sleutel not in doorstroom.OEFENBUNDELS:
        raise SystemExit(f"Onbekende doorstroombundel: {sleutel}")
    return doorstroom.OEFENBUNDELS[sleutel]


def reeks(kort: str, kop: str, nieuwe_kop: str = None, zonder: tuple = ()) -> dict:
    """Een hele reeks uit een doorstroombundel, los gekopieerd."""
    raak = [r for r in _bron(kort)["reeksen"] if r["kop"] == kop]
    if len(raak) != 1:
        raise SystemExit(f"{kort}: {len(raak)} reeksen heten {kop!r}, verwacht 1")
    uit = copy.deepcopy(raak[0])
    for haak in zonder:
        treffers = [i for i, o in enumerate(uit["oefeningen"]) if haak in tekst_van(o)]
        if len(treffers) != 1:
            raise SystemExit(f"{kort} §{kop}: {len(treffers)} oefeningen met {haak!r}, verwacht 1")
        uit["oefeningen"].pop(treffers[0])
    if nieuwe_kop:
        uit["kop"] = nieuwe_kop
    return uit


# ─────────────────────────────────────────────────────────────
# De nieuwe reeksen voor de bundels die meekomen.
# ─────────────────────────────────────────────────────────────
MICRO_BOUW = dict(
    kop="De bouw van dichtbij",
    opdracht="Vul aan, kies of leg uit.",
    oefeningen=[
        ("rij", [("bolvormige bacteriën", "kokken"),
                 ("staafvormige bacteriën", "bacillen"),
                 ("kommavormige bacteriën", "vibrionen")], "Hoe heten ze?", WW),
        ("rij", [("spiraalvormige bacteriën", "spirillen"),
                 ("een virus met bacteriën als gastheer", "een bacteriofaag")], "Hoe heten ze?", WL),
        ("kort", "Hoe heet het extra ringetje DNA naast het grote DNA van een bacterie?",
         "een plasmide", WW),
        ("kort", "Waarmee beweegt een bacterie zich voort?", "met een zweephaar", WW),
        ("waar", "Een bacterie heeft een echte kern met een kernmembraan.", False),
        ("waar", "Een gist is eencellig en heeft wél een kern.", True),
        ("waar", "Een schimmel is opgebouwd uit schimmeldraden en dus meercellig.", True),
        ("open", "Je krijgt een organisme te zien dat eencellig is, geen kern heeft en zich door "
                 "celsplitsing vermeerdert. Wat is het, en waarom is het geen gist?",
         "Een bacterie. Een gist is ook eencellig, maar die heeft een kern en vermeerdert zich door "
         "knopvorming.", 4),
        ("open", "Noem de drie onderdelen die je bij een virus kan tegenkomen en zeg waarom een "
                 "virus een gastheer nodig heeft.",
         "Erfelijk materiaal, een eiwitmantel of kapsel, en bij sommige soorten een enveloppe met "
         "spikes. Een virus kan zich niet zelf vermeerderen en heeft daarvoor de cel van een "
         "gastheer nodig.", 5),
    ],
)

MICRO_BINNEN = dict(
    kop="Hoe komen ze binnen?",
    opdracht="Vul aan of leg uit.",
    oefeningen=[
        ("kies", "Langs welke wegen dringen micro-organismen je lichaam binnen?",
         ["langs de mond, de luchtwegen, de ogen en wondjes in de huid",
          "alleen langs de mond, met de voeding mee",
          "alleen langs wondjes, want de huid laat niets door"], 0),
        ("open", "Waarom is handen wassen zo doeltreffend, terwijl je er geen enkel micro-organisme "
                 "mee doodt dat al binnen is?",
         "Het haalt de micro-organismen van je handen weg voor ze langs je mond, je ogen of een "
         "wondje binnen kunnen. Je sluit dus de weg af in plaats van ze te bestrijden.", 4),
        ("open", "Hoe deel je virussen in naar hun gastheer?",
         "In dierlijke virussen, plantaardige virussen en bacteriofagen.", 3),
    ],
)

ATOOM_ELEKTRONEN = dict(
    kop="Elektronenconfiguratie en het stipmodel",
    opdracht="Vul aan of leg uit.",
    oefeningen=[
        ("rij", [("zuurstof, atoomnummer 8", "2, 6"),
                 ("natrium, atoomnummer 11", "2, 8, 1"),
                 ("zwavel, atoomnummer 16", "2, 8, 6")], "Welke configuratie?", WW),
        ("kort", "Hoeveel elektronen passen er in de eerste schil?", "twee", W),
        ("kort", "Hoe heet het model waarin je alleen de buitenste schil als stipjes rond het "
                 "symbool zet?", "het elektron-stipmodel", WL),
        ("waar", "In het elektron-stipmodel zet je alle elektronen van het atoom rond het symbool.",
         False),
        ("open", "Een atoom heeft massagetal 23 en atoomnummer 11. Hoeveel protonen, neutronen en "
                 "elektronen heeft het, en hoe weet je dat?",
         "Elf protonen, want dat is het atoomnummer. Twaalf neutronen, want 23 min 11. En elf "
         "elektronen, want het atoom is neutraal.", 5),
    ],
)

INGREPEN = [
    ("micro-organismen-het-microbioom-en-bewaring", "schrap-reeks", "Prokaryoot of eukaryoot?", None),
    ("micro-organismen-het-microbioom-en-bewaring", "schrap-reeks",
     "Uitgebreid: het driedomeinensysteem", None),
    ("micro-organismen-het-microbioom-en-bewaring", "reeks-vooraan", None, MICRO_BOUW),
    ("micro-organismen-het-microbioom-en-bewaring", "reeks-achteraan", None, MICRO_BINNEN),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", "schrap-reeks",
     "Uitgebreid: absolute massa en de atoommassa-eenheid", None),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", "vervang-oefening",
     "Waarom staat de relatieve atoommassa", [
         ("open", "Twee atomen zijn isotopen van elkaar. Wat hebben ze gemeen en waarin "
                  "verschillen ze?",
          "Ze hebben hetzelfde aantal protonen, dus hetzelfde atoomnummer en hetzelfde element. Ze "
          "verschillen in hun aantal neutronen, en dus in hun massagetal.", 4),
     ]),
    ("de-bouw-van-het-atoom-en-het-periodiek-systeem", "reeks-achteraan", None, ATOOM_ELEKTRONEN),
    # Deze fiche zet bij temperatuur de graad Celsius, niet de kelvin.
    ("grootheden-eenheden-en-wetenschappelijk-onderzoek", "vervang-oefening", "kelvin", [
        ("rij", [("druk", "pascal"), ("temperatuur", "graden Celsius")], "Welke SI-eenheid?", WW),
    ]),
]


# ─────────────────────────────────────────────────────────────
# De bundels die hier opnieuw samengesteld worden.
# ─────────────────────────────────────────────────────────────
HERBOUW = {}

HERBOUW["energieomzettingen-vermogen-en-rendement"] = dict(
    vak=VAK, niveau=DF, titel="Energieomzettingen, vermogen en rendement",
    onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Welke energievorm?",
             opdracht="Schrijf de naam van de energievorm.",
             oefeningen=[
                 ("rij", [("een steen hoog op een muur", "gravitationele energie"),
                          ("een rijdende auto", "kinetische energie"),
                          ("een ingedrukte veer", "elastische energie")], "Welke vorm?", WL),
                 ("rij", [("een volle batterij", "chemische energie"),
                          ("een warme radiator", "thermische energie"),
                          ("het licht van de zon", "stralingsenergie")], "Welke vorm?", WL),
             ]),
        dict(kop="Welke omzetting?",
             opdracht="Schrijf de omzetting als twee energievormen met een pijl ertussen.",
             oefeningen=[
                 ("rij", [("een zonnepaneel", "straling naar elektrisch"),
                          ("een windmolen", "kinetisch naar elektrisch"),
                          ("een gasfornuis", "chemisch naar thermisch")], "Welke omzetting?", WL),
                 ("open", "Een fiets daalt een berg af en de rijder blijft remmen. Welke omzetting "
                          "gebeurt er, en waar komt die energie terecht?",
                  "De kinetische energie van de fiets wordt door de wrijving warmte. Die warmte "
                  "komt in de remblokjes, de velg en de lucht errond terecht.", 4),
             ]),
        dict(kop="Open, gesloten of geïsoleerd?",
             opdracht="Schrijf open, gesloten of geïsoleerd.",
             oefeningen=[
                 ("rij", [("wisselt energie én materie uit", "open"),
                          ("wisselt alleen energie uit", "gesloten"),
                          ("wisselt niets van de twee uit", "geïsoleerd")], "Welk systeem?", WW),
                 ("kort", "Een kookpot zonder deksel op het vuur: welk systeem?", "een open systeem",
                  WL),
                 ("open", "Waarom bestaat er in de praktijk geen volledig geïsoleerd systeem?",
                  "Er lekt altijd een beetje warmte naar de omgeving. Zelfs een goede thermosfles "
                  "koelt na een dag af.", 3),
             ]),
        dict(kop="Nuttig of ongewenst?",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("het licht van een gloeilamp", "nuttig"),
                          ("de warmte van een gloeilamp", "ongewenst"),
                          ("de warmte van een waterkoker", "nuttig")], "Nuttig of ongewenst?", WW),
                 ("kort", "Hoe noem je het verlies van bruikbare energie naar een ongewenste vorm?",
                  "energiedissipatie", WL),
                 ("open", "Waarom heeft een computer koeling nodig?",
                  "Een deel van de elektrische energie wordt warmte. Zonder koeling blijft die "
                  "warmte in het toestel en loopt de temperatuur te hoog op.", 4),
                 ("open", "Je zet in een afgesloten keuken de deur van de koelkast open en laat "
                          "ze zo staan. Wat gebeurt er met de temperatuur in die keuken, en waarom?",
                  "Ze stijgt. De koelkast verplaatst warmte van binnen naar buiten en de motor zet "
                  "daarbij zelf nog elektrische energie in warmte om. In een gesloten keuken komt "
                  "die energie er dus bovenop.", 5),
             ]),
        dict(kop="Eenheden van energie",
             opdracht="Reken uit of vul aan.",
             oefeningen=[
                 ("kort", "Hoeveel joule is één kilowattuur?", "3 600 000 joule", WW),
                 ("kort", "Een lamp van 10 watt brandt een half uur. Hoeveel energie zet ze om?",
                  "18 000 joule", WW),
                 ("waar", "Een kilowattuur is een eenheid van vermogen.", False),
                 ("open", "Waarom rekent je elektriciteitsfactuur in kilowattuur en niet in joule?",
                  "Eén kilowattuur is 3 600 000 joule. In joule zou je met onhandig grote getallen "
                  "moeten werken.", 3),
             ]),
        dict(kop="Energie blijft bewaard",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Beschrijf de energiebalans van een slingerende schommel.",
                  "In het hoogste punt is de gravitationele energie het grootst en de kinetische "
                  "energie nul. In het laagste punt is het omgekeerd. Zonder wrijving blijft de som "
                  "van de twee gelijk.", 5),
             ] + reeks("arbeid-energie-vermogen-en-rendement", "Energie blijft bewaard",
                       zonder=("Beschrijf de energiebalans",))["oefeningen"]),
        reeks("arbeid-energie-vermogen-en-rendement", "Vermogen",
              zonder=("Twee kranen tillen",)),
        reeks("arbeid-energie-vermogen-en-rendement", "Rendement"),
    ],
)

HERBOUW["warmte-faseovergangen-en-inwendige-energie"] = dict(
    vak=VAK, niveau=DF, titel="Warmte, faseovergangen en inwendige energie",
    onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Warmte of temperatuur?",
             opdracht="Schrijf warmte of temperatuur.",
             oefeningen=[
                 ("rij", [("meet je in joule", "warmte"),
                          ("meet je in graden Celsius", "temperatuur"),
                          ("gaat van het ene systeem naar het andere", "warmte")],
                  "Wat is het?", WW),
                 ("open", "Leg het verschil uit tussen temperatuur en warmte.",
                  "Temperatuur zegt hoe snel de deeltjes gemiddeld bewegen. Warmte is de energie "
                  "die van een warm naar een koud systeem overgaat door hun temperatuurverschil.",
                  4),
                 ("waar", "Warmte gaat altijd van het warme naar het koude voorwerp.", True),
                 ("waar", "Een voorwerp met een hogere temperatuur bevat altijd meer warmte dan "
                          "een voorwerp met een lagere temperatuur.", False),
             ]),
        dict(kop="Wie geeft af en wie neemt op?",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("een warm blok metaal in koud water", "het blok geeft af"),
                          ("koude melk in warme koffie", "de melk neemt op")],
                  "Wie doet wat?", WL),
                 ("kort", "Hoe noem je de toestand waarin er geen warmte meer overgaat?",
                  "thermisch evenwicht", WL),
                 ("open", "Je wil de eindtemperatuur van een mengsel berekenen. Welke redenering "
                          "gebruik je daarvoor?",
                  "Je stelt een warmtebalans op: de warmte die het warme deel afgeeft, is de "
                  "warmte die het koude deel opneemt. Dat is de wet van behoud van energie.", 4),
             ]),
        dict(kop="De inwendige energie",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Uit welke twee delen bestaat de inwendige energie?",
                  "de kinetische en de potentiële", WL),
                 ("kort", "Hoe heten de krachten die de deeltjes van een vloeistof bij elkaar "
                          "houden?", "cohesiekrachten", WL),
                 ("open", "Wat gebeurt er met de inwendige energie van ijs terwijl het smelt, en "
                          "waarom blijft de thermometer dan op nul graden staan?",
                  "De inwendige potentiële energie stijgt, want de warmte gaat naar het losmaken "
                  "van de deeltjes uit hun vaste plaats. De deeltjes gaan niet sneller bewegen, en "
                  "dus stijgt de temperatuur niet.", 5),
             ]),
        reeks("warmte-en-faseovergangen", "Welke faseovergang?"),
        reeks("warmte-en-faseovergangen", "Waar of niet waar?"),
        reeks("warmte-en-faseovergangen", "Uitleggen"),
        dict(kop="Warmte in het dagelijkse leven",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom gebruikt men water als koelvloeistof in een motor?",
                  "Water neemt veel warmte op zonder zelf snel op te warmen. Het kan dus veel "
                  "warmte uit de motor wegvoeren.", 4),
                 ("open", "Waarom beregenen fruitboeren hun bomen als er nachtvorst op weg is?",
                  "Water geeft bij het bevriezen warmte af aan de knoppen. Zo blijven die rond nul "
                  "graden en bevriezen ze zelf niet.", 4),
                 ("open", "Waarom houd je een brandwonde onder koud stromend water?",
                  "Het stromende water blijft warmte uit de huid wegnemen. Koude breng je niet "
                  "binnen; warmte voer je af.", 4),
                 ("open", "Waarom kan je je erger verbranden aan stoom van honderd graden dan aan "
                          "water van honderd graden?",
                  "Bij het condenseren op je huid komt de warmte vrij die het water nodig had om "
                  "te verdampen. Die komt bovenop de warmte van het water zelf.", 4),
                 ("open", "Waarom blijft het aan de kust in de winter zachter dan in het "
                          "binnenland?",
                  "Het zeewater geeft zijn warmte traag en lang af. Daardoor loopt de zee achter "
                  "op de lucht en blijft het aan de kust minder scherp.", 4),
             ]),
    ],
)

HERBOUW["kracht-als-vector-en-bewegingstoestand"] = dict(
    vak=VAK, niveau=DF, titel="Kracht als vector en bewegingstoestand",
    onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Een kracht tekenen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Noem de vier kenmerken van een kracht.",
                  "grootte, richting, zin, aangrijpingspunt", WL),
                 ("kort", "Wat is de eenheid van kracht?", "de newton", W),
                 ("kort", "Met welk toestel meet je de grootte van een kracht?",
                  "een dynamometer", WW),
                 ("kort", "Hoe heet het punt waarin de hele zwaartekracht op een voorwerp "
                          "aangrijpt?", "het zwaartepunt", WW),
                 ("open", "Hoe stel je een kracht voor in een tekening? Zeg wat de lengte, de lijn "
                          "en de punt van je pijl betekenen.",
                  "Met een pijl die in het aangrijpingspunt begint. De lengte geeft de grootte, de "
                  "lijn de richting en de punt de zin.", 4),
             ]),
        reeks("vrije-val-verticale-worp-en-krachten", "Welke kracht?"),
        dict(kop="Nog twee soorten krachten",
             opdracht="Schrijf de naam van de kracht.",
             oefeningen=[
                 ("rij", [("laat een raket vooruitgaan", "de stuwkracht"),
                          ("laat een auto vooruitgaan", "de motorkracht")], "Welke kracht?", WL),
             ]),
        dict(kop="Krachten samenstellen",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Twee mensen duwen een kast in dezelfde zin, met 80 en met 50 newton. "
                          "Hoe groot is de resulterende kracht?", "130 newton", WW),
                 ("kort", "Twee krachten van 60 en 25 newton werken op één lijn in tegengestelde "
                          "zin. Hoe groot is de resulterende kracht?", "35 newton", WW),
                 ("kort", "Twee krachten van 30 en 40 newton maken een hoek van 90 graden. Hoe "
                          "groot is de resultante?", "50 newton", WW),
                 ("waar", "Twee even grote krachten in tegengestelde zin geven samen een dubbel zo "
                          "grote kracht.", False),
                 ("open", "Hoe noem je de ene kracht die hetzelfde effect heeft als alle krachten "
                          "samen, en hoe vind je ze als de krachten op één lijn liggen?",
                  "De resultante of resulterende kracht. Liggen ze in dezelfde zin, dan tel je de "
                  "grootten op; liggen ze in tegengestelde zin, dan trek je ze van elkaar af en "
                  "houd je de zin van de grootste.", 5),
             ]),
        dict(kop="Rust, constante snelheid, versnellen of vertragen",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("kies", "Wat gebeurt er met een voorwerp waarop geen resulterende kracht werkt?",
                  ["het blijft in rust of beweegt met een constante snelheid rechtdoor",
                   "het valt altijd naar beneden",
                   "het versnelt tot het een vaste snelheid haalt"], 0),
                 ("rij", [("een voorwerp vervormt", "een statisch effect"),
                          ("een voorwerp versnelt", "een dynamisch effect"),
                          ("een voorwerp verandert van richting", "een dynamisch effect")],
                  "Statisch of dynamisch effect?", WL),
                 ("waar", "Een voorwerp dat vertraagt, heeft geen enkele kracht meer op zich "
                          "werken.", False),
                 ("open", "Je zit in een bus die plots remt en je schuift naar voren. Verklaar dat "
                          "met het traagheidsbeginsel.",
                  "Je lichaam blijft met dezelfde snelheid vooruit bewegen, want er werkt geen "
                  "kracht op je die je meteen vertraagt. De bus vertraagt wel, en daarom schuif je "
                  "naar voren.", 4),
                 ("open", "Een kist staat stil op de vloer. Welke twee krachten werken erop, en "
                          "hoe groot is de resulterende kracht?",
                  "De zwaartekracht naar beneden en de normaalkracht van de vloer naar boven. Ze "
                  "zijn even groot en tegengesteld, dus is de resulterende kracht nul newton.", 4),
             ]),
        reeks("vrije-val-verticale-worp-en-krachten", "Massa of gewicht?",
              zonder=("Hoe groot is zijn gewicht?",)),
        reeks("vrije-val-verticale-worp-en-krachten", "Evenwicht"),
        dict(kop="Traagheid in het verkeer",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom moet de lading van een vrachtwagen goed vastgemaakt worden?",
                  "Bij het remmen schuift de lading door haar traagheid door: ze blijft met de "
                  "snelheid die ze had verder bewegen tot iets haar tegenhoudt.", 4),
                 ("open", "Een vrachtwagen en een auto rijden even snel. Welke van de twee heeft "
                          "de grootste remkracht nodig om op dezelfde afstand te stoppen, en "
                          "waarom?",
                  "De vrachtwagen. Hij heeft veel meer massa en dus veel meer traagheid, en dan is "
                  "er een veel grotere remkracht nodig om hem even snel tot stilstand te brengen.",
                  4),
                 ("open", "Waarom is de remafstand van een auto langer op een natte weg?",
                  "De wrijvingskracht tussen de band en het wegdek is kleiner. De resulterende "
                  "kracht die de auto vertraagt is dus kleiner, en de remweg wordt langer.", 4),
                 ("open", "Welke krachten werken op een vliegtuig in de lucht, en welke niet?",
                  "De stuwkracht van de motoren, de zwaartekracht naar beneden, de wrijvingskracht "
                  "van de lucht en de draagkracht van de vleugels. Een normaalkracht werkt er niet "
                  "op: die bestaat alleen zolang het vliegtuig op een oppervlak rust.", 5),
             ]),
    ],
)

HERBOUW["druk-in-het-dagelijkse-leven"] = dict(
    vak=VAK, niveau=DF, titel="Druk in het dagelijkse leven",
    onder=ONDER, hoe=HOE,
    reeksen=[
        reeks("druk-en-de-gaswetten", "Rekenen met druk"),
        dict(kop="Eenheden van druk",
             opdracht="Reken uit of vul aan.",
             oefeningen=[
                 ("kort", "Hoeveel pascal is één kilopascal?", "1000 pascal", WW),
                 ("kort", "Hoeveel pascal is één hectopascal?", "100 pascal", WW),
                 ("kort", "Je duwt met 600 newton op 0,2 vierkante meter. Hoe groot is de druk?",
                  "3000 pascal", WW),
                 ("waar", "De newton is een eenheid van druk.", False),
                 ("open", "Het weerbericht spreekt over 1013 hectopascal. Hoeveel pascal is dat, "
                          "en wat meet men daarmee?",
                  "101 300 pascal. Dat is de luchtdruk, gemeten met een barometer.", 3),
             ]),
        dict(kop="Luchtdruk, overdruk en onderdruk",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("hoger dan de omgevingsdruk", "overdruk"),
                          ("lager dan de omgevingsdruk", "onderdruk")], "Wat is het?", WW),
                 ("rij", [("meet de luchtdruk buiten", "een barometer"),
                          ("meet de druk in een vat of leiding", "een manometer")],
                  "Welk toestel?", WL),
                 ("waar", "De luchtdruk is op elke hoogte precies dezelfde.", False),
                 ("open", "Waarom kan je met een rietje een vloeistof opzuigen?",
                  "Je maakt onderdruk in het rietje. Het verschil met de luchtdruk op de drank in "
                  "het glas duwt de vloeistof dan omhoog.", 4),
                 ("open", "Waarom suizen je oren als een vliegtuig opstijgt, en wat helpt daartegen?",
                  "De luchtdruk buiten daalt terwijl de druk in je oor nog hoog blijft, en dat "
                  "drukverschil staat op je trommelvel. Slikken of gapen maakt de druk aan beide "
                  "kanten weer gelijk.", 4),
                 ("open", "Waarom staat een zak chips bol als je hem mee de bergen in neemt?",
                  "Boven in de bergen is de luchtdruk lager, terwijl de druk in de zak gelijk "
                  "blijft. Die overdruk duwt de zak bol.", 4),
             ]),
        dict(kop="Groot of klein oppervlak?",
             opdracht="Schrijf of het oppervlak groot of klein gemaakt wordt, en waarom.",
             oefeningen=[
                 ("rij", [("de rupsbanden van een graafmachine", "groot, om niet weg te zakken"),
                          ("de sneeuwschoenen van een wandelaar", "groot, om niet weg te zakken"),
                          ("de punt van een duimspijker", "klein, om door te dringen")],
                  "Groot of klein?", WL),
                 ("open", "Je moet een zware kast op een houten vloer zetten en je kan kiezen "
                          "tussen vier smalle poten en vier brede. Welke kies je, en leg je keuze "
                          "uit met p = F / A?",
                  "De brede. De kracht blijft dezelfde, maar het oppervlak is groter, dus is de "
                  "druk op de vloer kleiner en komen er geen putjes in het hout.", 5),
             ]),
        reeks("druk-en-de-gaswetten", "Druk in gassen"),
        dict(kop="Gasdruk in het dagelijkse leven",
             opdracht="Kruis aan of leg in volledige zinnen uit.",
             oefeningen=[
                 ("waar", "Een gas oefent alleen naar beneden druk uit.", False),
                 ("open", "Waarom kan een gasfles in de volle zon ontploffen?",
                  "De deeltjes gaan sneller bewegen en botsen harder tegen de wand, dus stijgt de "
                  "druk. Het volume van de stalen fles kan niet mee, en bij een te hoge druk "
                  "begeeft ze het.", 4),
                 ("open", "Waarvoor dient een veiligheidsklep op een drukvat?",
                  "Ze gaat open zodra de druk binnen te hoog wordt en laat gas ontsnappen, nog "
                  "voor het vat kan barsten.", 4),
                 ("open", "Waarom pompen wielrijders hun banden in de zomer wat minder hard op?",
                  "De warme lucht in de band geeft een hogere druk. Een band die je in de zomer tot "
                  "de bovengrens oppompt, staat daarna te hard.", 4),
                 ("open", "Waarom loopt een ballon die je in de koelkast legt wat leeg?",
                  "De deeltjes bewegen trager, dus daalt de druk. De ballon krimpt tot de druk "
                  "binnen weer in evenwicht is met de luchtdruk buiten.", 4),
             ]),
    ],
)

HERBOUW["biologische-feedback-en-homeostase"] = dict(
    vak=VAK, niveau=DF, titel="Biologische feedback en homeostase",
    onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="De woorden van een feedbacksysteem",
             opdracht="Schrijf bij elke omschrijving het juiste woord.",
             oefeningen=[
                 ("rij", [("vangt de prikkel op", "de receptor"),
                          ("geeft het signaal door", "de conductor"),
                          ("voert de reactie uit", "de effector")], "Welke schakel?", WL),
                 ("rij", [("vergelijkt met de normwaarde", "het controlecentrum"),
                          ("de waarde waarrond geregeld wordt", "de normwaarde")],
                  "Welk woord?", WL),
                 ("kort", "Hoe noem je het stabiel houden van het inwendige milieu?",
                  "homeostase", WW),
                 ("kort", "Hoe noem je elke verandering in het inwendige of het uitwendige milieu?",
                  "een prikkel", WW),
             ]),
        dict(kop="Wie is wat bij de mens?",
             opdracht="Schrijf receptor, conductor of effector.",
             oefeningen=[
                 ("rij", [("de zintuigcellen in de huid", "receptor"),
                          ("het zenuwstelsel en de hormonen", "conductor"),
                          ("de spieren en de klieren", "effector")], "Wat is het?", WW),
                 ("kort", "Welke twee delen van de hersenen treden hier op als controlecentrum?",
                  "de hersenen en de hersenstam", WL),
                 ("open", "Zet de weg van een feedbacksysteem in de juiste volgorde en leg uit "
                          "waarom het een cirkel is.",
                  "Prikkel, receptor, conductor, effector, reactie. De reactie verandert de prikkel "
                  "zelf weer, en zo begint het opnieuw.", 4),
             ]),
        dict(kop="Negatief of positief?",
             opdracht="Schrijf negatieve of positieve feedback.",
             oefeningen=[
                 ("rij", [("je gaat zweten als je temperatuur stijgt", "negatieve feedback"),
                          ("de weeën bij een bevalling worden krachtiger", "positieve feedback"),
                          ("insuline doet je glucosegehalte dalen", "negatieve feedback")],
                  "Welke feedback?", WL),
                 ("waar", "Bij negatieve feedback versterkt het lichaam de verandering die het "
                          "gemeten heeft.", False),
                 ("open", "Leg uit waarom de woorden negatief en positief hier niets zeggen over "
                          "goed of slecht.",
                  "Negatief betekent dat de reactie de verandering tegenwerkt, positief dat ze de "
                  "verandering versterkt. Bloedstolling is positieve feedback en is net heel "
                  "nuttig.", 4),
             ]),
        dict(kop="De lichaamstemperatuur",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("te warm: de bloedvaten in de huid", "verwijden"),
                          ("te koud: de bloedvaten in de huid", "vernauwen"),
                          ("te koud: de spieren beginnen te", "rillen")], "Wat gebeurt er?", WW),
                 ("kort", "Welke receptoren in de huid meten de temperatuur?",
                  "warmte- en koudereceptoren", WL),
                 ("open", "Waarom koelt zweten je af, en waarom werkt dat minder goed in vochtige "
                          "lucht?",
                  "Het zweet verdampt en neemt daarvoor warmte van je lichaam op. In vochtige "
                  "lucht verdampt het slechter, dus wordt er minder warmte weggenomen.", 4),
                 ("open", "Waarom worden je handen bleek en koud als je buiten in de kou staat, "
                          "terwijl je organen op temperatuur blijven?",
                  "De bloedvaten in je huid vernauwen. Daardoor blijft het warme bloed in je "
                  "binnenste en gaat er aan de buitenkant minder warmte verloren.", 4),
             ]),
        dict(kop="De glucosespiegel",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("laat de lever glucose opslaan", "insuline"),
                          ("laat de lever glycogeen afbreken", "glucagon"),
                          ("maakt beide hormonen", "de alvleesklier")], "Wat of wie?", WW),
                 ("kort", "Als welke stof slaat de lever glucose op?", "als glycogeen", WW),
                 ("waar", "Glucagon zorgt ervoor dat de lever glucose opslaat als glycogeen.",
                  False),
                 ("open", "Je hebt een paar uur niet gegeten en je glucosegehalte daalt onder de "
                          "normwaarde. Beschrijf wat er gebeurt, met de hormonen en de organen erbij.",
                  "De alvleesklier meet het te lage gehalte en geeft glucagon af. De lever breekt "
                  "glycogeen af tot glucose en geeft dat aan het bloed, zodat het gehalte weer "
                  "stijgt.", 5),
                 ("open", "Bij diabetes type 1 maakt de alvleesklier geen insuline meer. Wat loopt "
                          "er mis in het feedbacksysteem?",
                  "Het meten gaat nog, maar het signaal valt weg. De lever en de spiercellen "
                  "krijgen geen bevel om glucose op te nemen, en daardoor blijft het gehalte in "
                  "het bloed te hoog.", 5),
             ]),
        dict(kop="Nog drie feedbacksystemen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Noem de schakels van de bloeddrukregeling: wie meet, wie beslist en "
                          "wie voert uit?",
                  "Receptoren in de wand van grote bloedvaten meten de druk, de hersenstam "
                  "beslist, en het hart en de bloedvaten voeren uit.", 4),
                 ("open", "Wat gebeurt er met je hartritme bij stress, en waarvoor dient dat?",
                  "Het versnelt, zodat je spieren meer zuurstof en glucose krijgen en je lichaam "
                  "klaar is om te handelen.", 4),
                 ("open", "Hoe houdt een plant haar waterhuishouding in evenwicht, en waarom is "
                          "dat negatieve feedback?",
                  "Ze sluit haar huidmondjes als ze te veel water dreigt te verliezen. De reactie "
                  "werkt het waterverlies tegen, en dat is negatieve feedback.", 4),
                 ("open", "Op een schema staat een pijl met een minteken van een klier naar de "
                          "hersenen. Wat betekent die pijl?",
                  "De klier remt met haar hormoon het controlecentrum af. De pijl geeft de richting "
                  "van de invloed, het minteken zegt dat ze remmend is.", 4),
             ]),
    ],
)


def pas_toe(bundels: dict):
    for kort, soort, waar, inhoud in INGREPEN:
        if kort not in bundels:
            raise SystemExit(f"Onbekende bundel in INGREPEN: {kort}")
        reeksen = bundels[kort]["reeksen"]
        if soort == "schrap-reeks":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} reeksen heten {waar!r}, verwacht 1")
            reeksen.pop(raak[0])
        elif soort == "reeks-vooraan":
            reeksen.insert(0, copy.deepcopy(inhoud))
        elif soort == "reeks-achteraan":
            reeksen.append(copy.deepcopy(inhoud))
        elif soort == "vervang-oefening":
            raak = [
                (i, j)
                for i, r in enumerate(reeksen)
                for j, o in enumerate(r["oefeningen"])
                if waar in tekst_van(o)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} oefeningen met {waar!r}, verwacht 1")
            i, j = raak[0]
            reeksen[i]["oefeningen"][j : j + 1] = inhoud
        else:
            raise SystemExit(f"Onbekende ingreep: {soort}")


def bouw() -> dict:
    uit = {}
    for bron, nieuwe_kort, nieuwe_titel in MEE:
        b = copy.deepcopy(_bron(bron))
        b["niveau"] = DF
        if nieuwe_titel:
            b["titel"] = nieuwe_titel
        uit[nieuwe_kort or bron] = b
    pas_toe(uit)
    uit.update(copy.deepcopy(HERBOUW))

    if sorted(uit) != sorted(ORDE):
        tekort = sorted(set(ORDE) - set(uit))
        teveel = sorted(set(uit) - set(ORDE))
        raise SystemExit(f"De bundels kloppen niet met ORDE. Ontbreekt: {tekort}. Te veel: {teveel}.")

    for kort, b in uit.items():
        alles = " ".join(
            [b["titel"]]
            + [r["kop"] for r in b["reeksen"]]
            + [r.get("opdracht", "") for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{kort} gebruikt nog {woord!r}, dat staat niet op deze fiche")
        aantal = sum(len(r["oefeningen"]) for r in b["reeksen"])
        if aantal < 15:
            raise SystemExit(f"{kort} heeft maar {aantal} oefeningen")

    return {VOOR + kort + NIEUW: uit[kort] for kort in ORDE}


OEFENBUNDELS = bouw()

if __name__ == "__main__":
    for sleutel, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, sleutel)
        print(" ", sleutel)

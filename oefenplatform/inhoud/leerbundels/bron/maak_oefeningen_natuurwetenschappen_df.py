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
        ("rij", [(r"zuurstof, atoomnummer \(8\)", r"\(2\), \(6\)"),
                 (r"natrium, atoomnummer \(11\)", r"\(2\), \(8\), \(1\)"),
                 (r"zwavel, atoomnummer \(16\)", r"\(2\), \(8\), \(6\)")], "Welke configuratie?", WW),
        ("kort", "Hoeveel elektronen passen er in de eerste schil?", "twee", W),
        ("kort", "Hoe heet het model waarin je alleen de buitenste schil als stipjes rond het "
                 "symbool zet?", "het elektron-stipmodel", WL),
        ("waar", "In het elektron-stipmodel zet je alle elektronen van het atoom rond het symbool.",
         False),
        ("open", r"Een atoom heeft massagetal \(23\) en atoomnummer \(11\). Hoeveel protonen, neutronen en "
                 "elektronen heeft het, en hoe weet je dat?",
         r"Elf protonen, want dat is het atoomnummer. Twaalf neutronen, want \(23\) min \(11\). En elf "
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
                 ("kort", "Hoeveel joule is één kilowattuur?", r"\(3\,600\,000\) joule", WW),
                 ("kort", r"Een lamp van \(10\) watt brandt een half uur. Hoeveel energie zet ze om?",
                  r"\(18\,000\) joule", WW),
                 ("waar", "Een kilowattuur is een eenheid van vermogen.", False),
                 ("open", "Waarom rekent je elektriciteitsfactuur in kilowattuur en niet in joule?",
                  r"Eén kilowattuur is \(3\,600\,000\) joule. In joule zou je met onhandig grote getallen "
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
                 ("kort", r"Twee mensen duwen een kast in dezelfde zin, met \(80\) en met \(50\) newton. "
                          "Hoe groot is de resulterende kracht?", r"\(130\) newton", WW),
                 ("kort", r"Twee krachten van \(60\) en \(25\) newton werken op één lijn in tegengestelde "
                          "zin. Hoe groot is de resulterende kracht?", r"\(35\) newton", WW),
                 ("kort", r"Twee krachten van \(30\) en \(40\) newton maken een hoek van \(90\) graden. Hoe "
                          "groot is de resultante?", r"\(50\) newton", WW),
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
                 ("kort", "Hoeveel pascal is één kilopascal?", r"\(1000\) pascal", WW),
                 ("kort", "Hoeveel pascal is één hectopascal?", r"\(100\) pascal", WW),
                 ("kort", r"Je duwt met \(600\) newton op \(0{,}2\) vierkante meter. Hoe groot is de druk?",
                  r"\(3000\) pascal", WW),
                 ("waar", "De newton is een eenheid van druk.", False),
                 ("open", r"Het weerbericht spreekt over \(1013\) hectopascal. Hoeveel pascal is dat, "
                          "en wat meet men daarmee?",
                  r"\(101\,300\) pascal. Dat is de luchtdruk, gemeten met een barometer.", 3),
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
                          r"uit met \(p = F / A\)?",
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
                 ("open", r"Bij diabetes type \(1\) maakt de alvleesklier geen insuline meer. Wat loopt "
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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}


UITLEGBLADEN["oefenbundel-biologische-feedback-en-homeostase-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een feedbacksysteem heeft altijd dezelfde schakels: iets meet (receptor), iets geeft door (conductor), iets beslist (controlecentrum) en iets doet (effector). Zoek bij elke omschrijving welke van die vier taken erin zit.",
            waarom=[
                "De drie woorden zeggen zelf wat ze doen: een receptor recipieert of ontvangt, een conductor geleidt, een effector brengt een effect tot stand.",
                "De normwaarde is geen vast getal maar een smalle band waarbinnen het lichaam wil blijven: je temperatuur schommelt over de dag en blijft toch in orde.",
                "Homeostase betekent letterlijk gelijk blijven staan. Het is geen stilstand: je lichaam werkt voortdurend om die waarden gelijk te houden.",
                None,
            ],
        ),
        dict(
            aanpak="Leg de drie schakels op je eigen lichaam. Wat voelt iets? Wat vervoert het bericht? Wat beweegt of maakt iets aan?",
            waarom=[
                "Er zijn twee conductors naast elkaar: het zenuwstelsel is snel en kort, de hormonen zijn trager maar werken langer. Klieren horen bij de effectoren, want ze maken een stof aan; dat is ook een reactie.",
                "Het regelcentrum voor je temperatuur zit in de hypothalamus, een klein gebied in de hersenen, en de hersenstam regelt zaken als hartritme en ademhaling. Het zijn dus plekken in de hersenen, niet de hersenen als geheel.",
                "Het is een cirkel omdat de reactie de prikkel zelf verandert: je zweet, je temperatuur daalt, en daardoor meet de receptor iets anders. Een systeem dat zijn eigen resultaat niet terugmeet, kan niet regelen.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat de reactie met de verandering doet. Werkt ze de verandering tegen, dan is het negatieve feedback; maakt ze de verandering groter, dan is het positieve feedback.",
            waarom=[
                "De weeën zijn het schoolvoorbeeld van positieve feedback: elke wee duwt het kind lager, dat geeft meer prikkeling, dat geeft meer oxytocine en dus nog krachtigere weeën. Het stopt pas als het kind geboren is.",
                "Het is net omgekeerd: negatieve feedback werkt de verandering tegen en brengt de waarde terug naar de normwaarde. Versterken is wat positieve feedback doet.",
                "Positieve feedback is vaak nuttig maar bijna altijd kort: bloedstolling, een bevalling. Een systeem dat zichzelf blijft versterken loopt uit de hand, dus het heeft een eindpunt nodig.",
            ],
        ),
        dict(
            aanpak="Denk bij temperatuur aan twee knoppen: hoeveel warmte je maakt, en hoeveel warmte je laat ontsnappen. Verwijde bloedvaten laten warmte weg, vernauwde houden ze binnen, rillen maakt warmte bij.",
            waarom=[
                "Verwijden brengt meer warm bloed naar de huid, waar de warmte kan weg; vernauwen houdt het bloed in je binnenste. Rillen is onwillekeurig spierwerk, en spieren die werken maken warmte.",
                "Er zijn twee soorten receptoren, want het lichaam moet beide richtingen kunnen meten. Eén soort zou niet volstaan om te weten of het te warm of te koud is.",
                "Verdampen kost energie, en die energie haalt het zweet uit je huid. In vochtige lucht zit al veel waterdamp, dus verdampt er minder en blijft het zweet op je huid staan zonder te koelen. Daarom voelt 30 °C in vochtige lucht veel zwaarder aan.",
                "Dat is een keuze van het lichaam: je organen op temperatuur houden is belangrijker dan je vingers warm houden. Bij echte kou gaat het te ver en krijg je bevriezingsschade aan vingers, tenen en oren.",
            ],
        ),
        dict(
            aanpak="Twee hormonen uit dezelfde klier doen het tegenovergestelde: insuline bergt glucose op, glucagon haalt ze weer boven. Onthoud insuline als de in-knop, naar de cellen toe.",
            waarom=[
                "De alvleesklier is hier receptor en controlecentrum tegelijk: ze meet het glucosegehalte in het bloed dat erlangs stroomt en geeft meteen zelf het hormoon af.",
                "Glycogeen is een lange keten van glucosemoleculen aan elkaar, een voorraadvorm. Zo kan er veel glucose opgeslagen liggen zonder dat het water aantrekt zoals losse glucose zou doen.",
                "Omgekeerd: glucagon breekt glycogeen juist áf tot glucose. Insuline is het hormoon dat laat opslaan.",
                None,
                "Het hele systeem meet nog goed; de boodschap raakt enkel niet verzonden. Daarom helpt insuline inspuiten: je vervangt het ontbrekende signaal, niet het meten.",
            ],
        ),
        dict(
            aanpak="Zoek bij elk nieuw systeem dezelfde vier schakels terug. Als je kan zeggen wie meet, wie beslist en wie uitvoert, heb je het systeem begrepen, ook als je het nooit eerder zag.",
            waarom=[
                "Die drukreceptoren zitten in de halsslagader en in de aorta, net waar het bloed het hart verlaat. Daar is de druk het meest zeggend voor de rest van het lichaam.",
                "Stress is geen storing in de homeostase maar een omschakeling: het lichaam zet tijdelijk een andere normwaarde, omdat handelen op dat moment belangrijker is dan rust.",
                "Een plant heeft geen zenuwen en toch een feedbacksysteem. Dat laat zien dat het geen eigenschap van dieren is maar een manier van regelen die overal in het leven voorkomt.",
                "Een minteken op een schema wil niet zeggen minder of slecht, maar remmend. Zo'n remmende pijl van de effector terug naar het controlecentrum is precies de lus van negatieve feedback.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-micro-organismen-het-microbioom-en-bewaring-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd drie groepen apart: bacteriën (geen kern), gisten en schimmels (wel een kern) en virussen (geen cel). De vorm van een bacterie zit in haar naam: kok is bol, bacil is staaf, vibrio is komma, spiril is spiraal.",
            waarom=[
                "De namen komen uit het Grieks en het Latijn: kokkos is bes of korrel, bacillus is stokje, vibrio komt van trillen of kronkelen.",
                "Een bacteriofaag is geen bacterie maar een virus dat bacteriën aanvalt; faag komt van eten. Pas op dat je die niet in het rijtje vormen zet.",
                "Een plasmide is klein maar belangrijk: bacteriën geven er genen mee aan elkaar door, en daar zitten ook de genen voor resistentie tegen antibiotica bij.",
                None,
                "Een bacterie is prokaryoot: haar DNA ligt los in de cel zonder kernmembraan eromheen. Een kern hebben is net het onderscheid met gisten en schimmels.",
                "Een gist is eukaryoot én eencellig. Eencellig en meercellig zegt dus niets over het hebben van een kern; dat zijn twee verschillende vragen.",
                "Die draden heten hyfen, en samen vormen ze een mycelium. Het grootste deel van een schimmel zit meestal onzichtbaar in het voedsel of in de bodem.",
                "Twee kenmerken samen maken het sluitend: eencellig past bij beide, maar geen kern en celsplitsing passen enkel bij een bacterie.",
                "Niet elk virus heeft een enveloppe. Die buitenste laag komt van het membraan van de gastheercel, en de spikes erin gebruikt het virus om de volgende cel te herkennen.",
            ],
        ),
        dict(
            aanpak="Vermeerderen zegt veel over wat een organisme is. Kan het zich zelf delen, dan leeft het zelfstandig; heeft het een andere cel nodig, dan niet.",
            waarom=[
                "Bij celsplitsing ontstaan twee gelijke cellen; bij knopvorming groeit er een kleiner dochtercelletje aan de moedercel, dat loslaat. Daarom zien gistcellen onder de microscoop vaak uit als twee bolletjes aan elkaar.",
                "Dat is de kern van de discussie of een virus leeft: het heeft erfelijk materiaal, maar geen eigen stofwisseling, geen eigen energie en geen eigen vermeerdering.",
                None,
            ],
        ),
        dict(
            aanpak="Let op de voorvoegsels: an- betekent zonder, aëroob verwijst naar lucht, auto- betekent zelf, hetero- betekent anders. Dan hoef je deze woorden niet uit het hoofd te leren.",
            waarom=[
                "Autotroof en heterotroof gaan over waar de energierijke stoffen vandaan komen; aëroob en anaëroob over het zuurstofgas. Dat zijn twee aparte vragen, en een organisme kan dus bijvoorbeeld anaëroob en heterotroof tegelijk zijn.",
                "Een spore heeft een dikke wand, bijna geen water en geen stofwisseling. Daarom overleven sporen koken, drogen en desinfecteren soms wel, en is steriliseren met stoom onder druk nodig om ze te doden.",
                "Die drie zijn de sleutel tot bewaren: haal er één weg en de groei stopt. Drogen haalt het vocht weg, koelen de temperatuur, vacuüm trekken bij sommige soorten het zuurstofgas.",
            ],
        ),
        dict(
            aanpak="Let bij een waar-of-niet-waarvraag op woorden als volledig, altijd en alles. Dat zijn precies de plekken waar een bijna juiste zin fout wordt.",
            waarom=[
                "Griep wordt veroorzaakt door een virus, en een antibioticum werkt enkel op bacteriën. Antibiotica nemen tegen een virus helpt niet en vergroot wel de resistentie.",
                "Dat is natuurlijke selectie in het klein: het middel doodt de gevoelige bacteriën en laat net de ongevoelige over, die zich dan ongestoord vermeerderen. Daarom moet je een kuur volledig afmaken.",
                "Pasteuriseren verhit kort tot ongeveer 72 °C: de ziekteverwekkers gaan eraan, maar sporen en sommige hittebestendige soorten overleven. Daarom moet gepasteuriseerde melk nog in de koelkast; steriliseren gaat verder, tot boven 100 °C.",
                "Daarin verschillen probiotica van prebiotica: probiotica zijn de levende micro-organismen zelf, prebiotica zijn de vezels waarop de micro-organismen in je darm leven.",
            ],
        ),
        dict(
            aanpak="Micro-organismen zijn niet enkel lastig: in de keuken en de industrie doen ze het werk. Vraag je bij een bewaarmethode altijd af welke groeivoorwaarde je wegneemt.",
            waarom=[
                "Bij het rijzen is het gas de bedoeling: de gist maakt koolstofdioxide dat in het deeg blijft zitten. Melkzuurbacteriën maken zuur, en in dat zuur klontert het eiwit van de melk samen tot yoghurt.",
                "De drie methoden pakken verschillende voorwaarden aan: drogen en zouten halen het water weg, pasteuriseren doodt met warmte. Zouten en zoeten werken via osmose: buiten de cel is de oplossing zo geconcentreerd dat er water uit de cel wordt getrokken.",
                "Dat heet gisting of fermentatie. Dezelfde gist maakt in brood vooral koolstofdioxide en in bier vooral alcohol: wat je overhoudt, hangt af van de omstandigheden en van wat er met het gas en de alcohol gebeurt.",
            ],
        ),
        dict(
            aanpak="Micro-organismen horen bij elk ecosysteem, ook bij het ecosysteem dat je zelf bent. Te veel of te weinig van een soort is bijna altijd het probleem, niet hun aanwezigheid.",
            waarom=[
                "Je darmmicrobioom weegt samen ongeveer anderhalve kilo en helpt bij de spijsvertering, bij vitaminen en bij je weerstand. Een antibioticakuur treft het ook, en daarom loopt de darm dan vaak enkele dagen in de war.",
                "Let op de orde: de algen sterven en worden afgebroken, en net die afbraak verbruikt het zuurstofgas. Het zuurstofgehalte zakt dus niet door de algen zelf maar door hun afbraak.",
                "Dat is het verschil tussen een bron bestrijden en een weg afsluiten. Bij hygiëne gaat het vaak om het tweede, en dat is meestal eenvoudiger en doeltreffender.",
                "Let op de drie middelen naast elkaar: een antibioticum tegen bacteriën, een antimycoticum tegen schimmels en een antiviraal middel tegen virussen. Het juiste middel hangt dus af van welke groep de infectie veroorzaakt.",
            ],
        ),
        dict(
            aanpak="Een besmetting heeft altijd een weg naar binnen. Zoek de plaatsen waar de buitenwereld je binnenste raakt: de mond, de luchtwegen, de ogen en elke wonde in de huid.",
            waarom=[
                "De gave huid is een goede barrière, maar de openingen en de slijmvliezen zijn dat veel minder. Daarom werken een mondmasker, handen wassen en een pleister allemaal op hetzelfde principe.",
                "Deze oefening komt terug op wat je bij nummer 25 al zei, nu met de nadruk op het verschil tussen doden en verwijderen. Zeep maakt de vettige buitenlaag van veel micro-organismen los, zodat het water ze meeneemt.",
                "De indeling gaat dus niet over de vorm of de grootte van het virus maar over wie het ziek maakt. Een bacteriofaag heeft bacteriën als gastheer en is voor ons ongevaarlijk; die worden zelfs onderzocht als alternatief voor antibiotica.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-voortplanting-en-de-hormonale-regeling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Volg de weg van de cel. Bij de vrouw: eierstok, eileider, baarmoeder. Bij de man: teelbal, bijbal, zaadleider. Elk orgaan heeft één taak op die weg, en de orde van de organen is de orde van de taken.",
            waarom=[
                "De bevruchting gebeurt in de eileider, niet in de baarmoeder: de zaadcel komt de eicel daar al tegen, en het bevruchte eitje reist daarna nog een paar dagen naar de baarmoeder.",
                "De bijbal is een opgerold kanaaltje van enkele meters tegen de teelbal aan. De zaadcellen worden in de teelbal gevormd maar zijn pas na die tocht door de bijbal beweeglijk.",
            ],
        ),
        dict(
            aanpak="De cyclus wordt geteld vanaf de eerste dag van de menstruatie. Dat is tegenstrijdig met je gevoel, want dan begint de cyclus met wat eruit gaat, maar het is de enige dag die je zonder meting kan vaststellen.",
            waarom=[
                "Juist daarom begint men te tellen bij het bloedverlies: de eisprong zelf voel je meestal niet, dus die kan niet als dag 1 dienen.",
                "Achtentwintig dagen is een gemiddelde, geen regel. Alles tussen ongeveer 21 en 35 dagen is gewoon, en bij dezelfde persoon kan het van maand tot maand verschillen.",
                "De eisprong valt ongeveer veertien dagen vóór de volgende menstruatie, niet veertien dagen na de vorige. Bij een langere cyclus schuift vooral de eerste helft op.",
                "Het geel lichaam is wat er van de leeggelopen follikel overblijft. Het maakt progesteron, en als er geen zwangerschap volgt, verdwijnt het na ongeveer twee weken; daardoor zakt het progesteron en komt de menstruatie.",
            ],
        ),
        dict(
            aanpak="Let bij deze zinnen op het orgaan en op de richting. Veel bijna juiste zinnen zetten het goede hormoon bij het verkeerde orgaan, of laten een remming als een stimulatie klinken.",
            waarom=[
                "De eierstok is dus niet enkel de plaats waar de eicel rijpt, maar ook een klier: de rijpende follikel maakt het oestrogeen zelf aan.",
                "De eileider vangt de eicel op, met haar trilharen en haar franjes. De baarmoeder ligt verderop; de eicel komt daar enkel aan als ze bevrucht is en de reis maakt.",
                "Dat verschil is ongeveer een halve graad en komt van het progesteron. Daarom kan temperatuur meten helpen om vast te stellen dat de eisprong al voorbij is, maar niet om hem te voorspellen.",
                "Bij de man is er geen cyclus: de zaadcelvorming loopt doorlopend, dag na dag, en één zaadcel heeft ongeveer tweeënzeventig dagen nodig om te rijpen.",
                "Inhibine is letterlijk een remmer. Het komt uit de cellen van Sertoli en uit de follikel, en het zorgt ervoor dat de hypofyse niet eindeloos FSH blijft aanmaken. Dat is negatieve feedback.",
            ],
        ),
        dict(
            aanpak="De hormonen lopen in een ketting van boven naar beneden: hypothalamus, hypofyse, geslachtsklier. GnRH is het startsignaal, FSH en LH zijn de bevelen, en oestrogeen, progesteron en testosteron zijn de hormonen van de klier zelf.",
            waarom=[
                "Let op het verschil tussen FSH en LH: FSH laat de follikel rijpen (de F van follikel helpt), LH geeft met een plotse piek het sein voor de eisprong. Beide komen uit de hypofyse, maar ze doen iets anders.",
                "Oestrogeen bouwt op in de eerste helft, progesteron houdt in stand in de tweede helft. Die taakverdeling verklaart ook waarom de menstruatie komt als het progesteron wegvalt.",
                "Dat is het mooie aan dit systeem: de top van de ketting is bij man en vrouw dezelfde, en enkel de klier onderaan verschilt. Daardoor werkt de feedback ook bij beiden op dezelfde manier.",
            ],
        ),
        dict(
            aanpak="In de teelbal zitten twee soorten hulpcellen naast de rijpende zaadcellen. Leydig maakt het hormoon, Sertoli verzorgt de cellen.",
            waarom=[
                "Onthoud het aan de taak: Leydig levert, Sertoli steunt. De cellen van Sertoli maken ook inhibine, en zo laten ze aan de hypofyse weten hoe de zaadcelvorming vordert.",
                "Het gaat om ongeveer twee graden lager dan de lichaamstemperatuur. Daarom trekt de huid van de balzak samen bij kou en hangt ze losser bij warmte: dat is zelf ook een vorm van temperatuurregeling.",
                "Testosteron doet meer dan de geslachtskenmerken: het werkt ook op de spier- en botopbouw en op het aanmaken van rode bloedcellen. Eén hormoon heeft bijna altijd meerdere doelwitten.",
            ],
        ),
        dict(
            aanpak="Zoek bij een hormoonsysteem altijd de weg terug. Een systeem met enkel pijlen naar beneden kan niet regelen; pas met een pijl terug naar boven kan het zichzelf bijsturen.",
            waarom=[
                "Bij de cyclus zit er ook een stuk positieve feedback in: het stijgende oestrogeen zet de hypofyse net aan om de LH-piek te geven. Daarna neemt de negatieve feedback het weer over.",
                "Dit is dezelfde lus als bij de temperatuur of de glucose, met andere spelers. Daarom is één keer het principe begrijpen genoeg om alle hormoonsystemen te kunnen volgen.",
                "Een minteken betekent remmend, niet minder of slecht. Zo'n remmende pijl van de klier terug naar de hypofyse is precies wat een systeem stabiel houdt.",
                "Het slijmvlies is in de tweede helft van de cyclus dik en goed doorbloed, klaar voor een innesteling. Progesteron houdt dat in stand; valt het weg, dan laat de laag los. De pil werkt onder meer door dat hormoonverloop vlak te houden.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-mengsels-en-zuivere-stoffen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Stel één vraag: zit er meer dan één soort stof in? Zo ja, dan is het een mengsel, ook als je dat niet ziet. Een zuivere stof bestaat uit één soort deeltje, en dat mag een verbinding zijn zoals water of zout.",
            waarom=[
                "Lucht ziet er enkelvoudig uit maar is een mengsel van stikstof, zuurstofgas, argon, koolstofdioxide en waterdamp. Keukenzout is daarentegen één verbinding, natriumchloride, en dus een zuivere stof.",
                "Kraantjeswater is water met opgeloste zouten en kalk erin; daarom kalkt een waterketel aan en gedestilleerd water niet. Brons is koper met tin, dus ook een mengsel, al ziet het uit als één metaal.",
            ],
        ),
        dict(
            aanpak="Homogeen betekent dat je de bestanddelen niet meer kan onderscheiden, ook niet met een gewone microscoop. Zie of meet je twee fasen naast elkaar, dan is het heterogeen.",
            waarom=[
                "Messing is een legering, en een legering is homogeen: de metalen zijn tot op het niveau van de atomen vermengd. Slagroom niet: daarin zitten luchtbelletjes die je gewoon ziet.",
                "Rook is heterogeen, ook al lijkt het één wolk: er zweven vaste deeltjes in een gas. Suiker in water is wel homogeen, want de suikermoleculen liggen los tussen de watermoleculen.",
            ],
        ),
        dict(
            aanpak="De naam van een mengsel komt van de twee fasen die erin zitten. Vloeistof in vloeistof is een emulsie, vast in vloeistof een suspensie, gas in vloeistof of vast een schuim, vast of vloeibaar in gas een aerosol, metaal in metaal een legering.",
            waarom=[
                "Vinaigrette is olie in azijn, twee vloeistoffen die niet mengen, dus een emulsie; daarom moet je ze opschudden. Krijt in water blijft een suspensie en bezinkt, want het is een vaste stof.",
                "Slagroom is een schuim omdat je er lucht in klopt. Het is dus niet het vet dat het volume maakt maar het gas.",
                "Messing is koper met zink en is geler; brons is koper met tin en is roder. Twee legeringen van hetzelfde hoofdmetaal, met een ander tweede metaal en andere eigenschappen.",
            ],
        ),
        dict(
            aanpak="Een scheidingstechniek gebruikt een verschil in een stofeigenschap en laat de stoffen zelf ongemoeid. Dat onderscheid, scheiden tegenover reageren, loopt door deze hele reeks.",
            waarom=[
                "Een zuivere stof heeft één smeltpunt en één kookpunt; een mengsel smelt en kookt over een traject. Dat is dan ook de proef waarmee je in het labo nagaat of een stof zuiver is.",
                "Daarom kan je een mengsel ook weer scheiden: het zout in zeewater is nog gewoon zout, en de olie in een vinaigrette is nog gewoon olie. Bij een chemische reactie is dat niet zo.",
                "Dat is net het verschil met een chemische reactie: na filtreren of destilleren heb je dezelfde stoffen als ervoor, enkel apart. Daarom is destilleren van zeewater geen reactie.",
                "Zeven werkt met grote korrels en een grof gaas, filtreren met kleine deeltjes en fijne poriën, maar het principe is hetzelfde: wat te groot is blijft achter.",
            ],
        ),
        dict(
            aanpak="Een stofeigenschap hangt niet af van hoeveel je ervan hebt. Vraag je af: verandert het getal als ik maar de helft neem? Zo ja, dan is het geen stofeigenschap.",
            waarom=[
                "Massa is geen stofeigenschap, massadichtheid wel: een halve liter water heeft de helft van de massa maar nog altijd dezelfde dichtheid van ongeveer 1 g/cm³. Daarmee kan je een stof herkennen, met de massa niet.",
                "Hetzelfde onderscheid: volume hangt van je staal af, oplosbaarheid en geleidbaarheid niet. Oplosbaarheid wordt wel gegeven bij een temperatuur, want ze verandert met de temperatuur.",
                "Let op de redenering: je besluit niet uit één meting maar uit het verloop. Een zuivere stof blijft tijdens het koken op dezelfde temperatuur staan omdat alle energie in de faseovergang gaat.",
            ],
        ),
        dict(
            aanpak="Kies je techniek op het verschil tussen de bestanddelen. Deeltjesgrootte geeft filtreren of zeven, kookpunt geeft destilleren of indampen, magnetisme geeft een magneet, dichtheid geeft centrifugeren of een scheitrechter.",
            waarom=[
                "Filtreren kan het zout niet uit water halen, want de opgeloste ionen gaan door elke filter mee. Destilleren wel, want het verschil in kookpunt is groot.",
                "Indampen en destilleren gebruiken hetzelfde verschil maar houden iets anders over: bij indampen hou je het zout en laat je het water weg, bij destilleren vang je juist het water op.",
                "Bij chromatografie gebruik je een derde eigenschap: hoe sterk een kleurstof aan het papier blijft hangen tegenover hoe goed ze meegaat met het oplosmiddel. Daarom lopen de kleuren verschillend hoog op.",
            ],
        ),
        dict(
            aanpak="Residu en filtraat zijn een vast woordenpaar bij het filtreren. Residu blijft, filtraat loopt door. Denk aan residu zoals in restant en aan filtraat als wat gefiltreerd is.",
            waarom=[
                None,
                None,
                "Filtreren werkt op grootte, en een vloeistofdruppel heeft geen vaste grootte: ze vervormt en glipt door de poriën. Voor twee vloeistoffen gebruik je dus het verschil in dichtheid.",
                "Welk deel het afval is, hangt af van wat je wil hebben, niet van de techniek. Bij het winnen van een neerslag of bij het zeven van grind is het residu precies het product.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-chemische-formules-en-chemische-reacties-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk hoeveel verschillende symbolen er in de formule staan. Eén soort atoom is een enkelvoudige stof, ook als er meerdere atomen in het deeltje zitten; twee of meer soorten maken een samengestelde stof.",
            waarom=[
                "O₂ en O₃ zijn allebei enkelvoudig, al bestaat het deeltje uit twee of drie atomen: het gaat om het aantal verschillende elementen, niet om het aantal atomen. O₂ is zuurstofgas, O₃ is ozon, twee heel verschillende stoffen uit hetzelfde element.",
                None,
            ],
        ),
        dict(
            aanpak="Een symbool begint altijd met een hoofdletter en heeft hoogstens één kleine letter erbij. Sommige symbolen komen uit de Latijnse naam: Na van natrium, K van kalium, Au van aurum, Fe van ferrum, Cu van cuprum.",
            waarom=[
                "Die drie zijn de klassieke valkuilen, want hun symbool lijkt niet op de Nederlandse naam. Goud is Au van aurum; Go bestaat niet.",
                "Let op de hoofdletters: Co is kobalt en CO is koolstofmonoxide. Eén letter verkeerd schrijven maakt van een element een verbinding.",
                None,
            ],
        ),
        dict(
            aanpak="De coëfficiënt staat vóór de formule en geldt voor alles wat erachter komt. De index staat klein achter een symbool en geldt enkel voor dat symbool, of voor de haakjes ervoor. Reken dus eerst per deeltje en vermenigvuldig daarna met de coëfficiënt.",
            waarom=[
                None,
                "De index 2 hoort bij de zuurstof, niet bij het hele deeltje. Dat verschil tussen vóór en achter bepaalt alles in deze reeks.",
                "Per watermolecule drie atomen: twee waterstof en één zuurstof. Drie moleculen maakt 3 maal 3, dus 9.",
                "Het haakje is de moeilijkheid: de 2 achter (OH) geldt voor de O én voor de H. Per deeltje dus 1 calcium, 2 zuurstof en 2 waterstof, samen 5, en 5 maal 2 geeft 10.",
                "Hou de twee stappen gescheiden: eerst de atomen in één deeltje, dan maal de coëfficiënt. Wie meteen alles door elkaar telt, vergeet bijna altijd één van de twee.",
            ],
        ),
        dict(
            aanpak="Metalen staan links en in het midden van het periodiek systeem, niet-metalen rechtsboven. Metalen glanzen, geleiden en zijn vervormbaar; niet-metalen meestal niet.",
            waarom=[
                "Kwik is een metaal, ook al is het vloeibaar bij kamertemperatuur. De toestand zegt niets over metaal of niet-metaal: ijzer is vast, kwik vloeibaar en toch zijn beide metalen.",
                None,
                "Het is net omgekeerd: glans en vervormbaarheid zijn eigenschappen van metalen. Niet-metalen zijn vaak gassen of brokkelige vaste stoffen zoals zwavel.",
            ],
        ),
        dict(
            aanpak="Bij deze stoffen hoort telkens één eigenschap die hun gebruik verklaart. Zoek de eigenschap, dan hoef je het gebruik niet apart te onthouden.",
            waarom=[
                "Chloorgas ruikt scherp en is giftig; het werd in de Eerste Wereldoorlog als strijdgas gebruikt. Dat is iets anders dan het chloor in zwembadwater, waar het in een verbinding zit.",
                "De edelgassen zijn de oplichters in reclameborden: neon geeft oranjerood, argon en kwikdamp geven blauw. Dat ze bijna niet reageren, is precies waarom ze veilig in een buis kunnen gloeien.",
                "Dat is een afweging tussen twee eigenschappen: waterstofgas is lichter en zou beter dragen, maar het verbrandt. Het luchtschip Hindenburg werkte op waterstofgas, en na die brand in 1937 is men op helium overgestapt.",
                "Dat heet allotropie. Het laat zien dat niet alleen de atomen maar ook hun ordening de stofeigenschappen bepaalt: in grafiet liggen de atomen in laagjes die over elkaar glijden, in diamant in een stevig ruimtelijk netwerk.",
            ],
        ),
        dict(
            aanpak="Tel links en rechts van de pijl hetzelfde aantal atomen van elk element. Begin met het element dat in de minste stoffen voorkomt en eindig met zuurstof of waterstof, want die zitten overal in.",
            waarom=[
                "Zuurstofgas is O₂, dus je krijgt het nooit per één atoom. Daarom moet links van H₂O een 2 staan: dat geeft twee zuurstofatomen rechts, en precies één O₂ links.",
                "Dezelfde reden als hiervoor: één O₂ levert twee zuurstofatomen, dus heb je twee MgO nodig, en dus ook twee Mg.",
                "Hier helpt de orde: eerst de koolstof (1 en 1), dan de waterstof (4 links, dus 2 H₂O rechts), en dan tel je de zuurstof rechts: 2 in CO₂ plus 2 in de twee watermoleculen is 4, dus 2 O₂ links.",
                "Het verschil in één zin: de coëfficiënt zegt hoeveel deeltjes, de index zegt welk deeltje. H₂O en H₂O₂ zijn water en waterstofperoxide, twee heel verschillende stoffen.",
            ],
        ),
        dict(
            aanpak="Bij een reactie verdwijnt of ontstaat er geen enkel atoom: ze worden enkel anders geschikt. Weegt het minder, zoek dan wat ontsnapt is; weegt het meer, zoek dan wat erbij gekomen is.",
            waarom=[
                "Het vat moet wel afgesloten zijn, want het zuurstofgas dat de reactie gebruikt moet erin blijven. In een open schaal lijkt magnesium juist zwaarder te worden, want daar komt zuurstof uit de lucht bij het vaste overblijfsel.",
                "Daarom weegt men bij zo'n proef in een gesloten vat. De wet van behoud van massa geldt altijd; wat je meet, hangt af van wat je binnen je weegschaal houdt.",
            ],
        ),
        dict(
            aanpak="Exo betekent naar buiten, endo naar binnen. Een exo-energetische reactie geeft energie aan de omgeving en voelt warm aan; een endo-energetische haalt energie uit de omgeving en voelt koud aan.",
            waarom=[
                "Let op de valkuil: een reactie die koud aanvoelt, is niet koud omdat ze koude maakt, maar omdat ze warmte uit je hand en de beker wegneemt. Koude afgeven bestaat niet.",
                "Zo'n koudegevoel is precies hoe een koelzakje uit de apotheek werkt: binnenin lost een zout op, en dat kost energie die uit de omgeving komt.",
                "Lager, want de energie die de reactie afgaf, zit niet meer in de stoffen. Wat de stoffen verliezen, krijgt de omgeving, en daarom warmt die op.",
                None,
                "Reagentia komen van reageren: de stoffen waarmee je begint. De pijl leest je als wordt omgezet in, niet als is gelijk aan.",
                None,
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-de-bouw-van-het-atoom-en-het-periodiek-systeem-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie deeltjes, drie plaatsen, drie ladingen. Proton en neutron zitten in de kern, elektronen eromheen. Onthoud de lading aan de naam: een proton is positief, een neutron is neutraal, dus blijft voor het elektron negatief over.",
            waarom=[
                "Een proton en een neutron wegen ongeveer hetzelfde; een elektron is bijna tweeduizend keer lichter. Daarom bepalen de kerndeeltjes de massa en de elektronen de chemie.",
                "De kern is wel ongelooflijk klein tegenover het hele atoom: zou de kern een voetbal zijn, dan lagen de elektronen honderden meters verder. Een atoom is dus vooral leegte.",
                "Daarom is een atoom als geheel neutraal. Komt er een elektron bij of gaat er een af, dan heet het geen atoom meer maar een ion.",
            ],
        ),
        dict(
            aanpak="Twee getallen, twee betekenissen: het atoomnummer is het aantal protonen, het massagetal is protonen plus neutronen. Dus altijd massagetal min atoomnummer voor de neutronen.",
            waarom=[
                "Reken mee: 23 min 11 is 12, en 16 min 8 is 8. Bij de lichte elementen zijn de aantallen vaak bijna gelijk; bij de zware zitten er veel meer neutronen dan protonen in de kern.",
                "Het atoomnummer geeft meteen twee dingen: het aantal protonen altijd, en het aantal elektronen zolang het atoom neutraal is. Bij een ion klopt het tweede niet meer.",
                None,
            ],
        ),
        dict(
            aanpak="Isotopen zijn hetzelfde element met een andere massa. Het aantal protonen bepaalt welk element het is, dus dat mag niet verschillen; enkel het aantal neutronen varieert.",
            waarom=[
                "Daarom reageren isotopen chemisch bijna gelijk: de elektronen zijn dezelfde. Ze verschillen wel in massa en soms in stabiliteit, en dat gebruikt men bij koolstofdatering met koolstof-14.",
                "Een ander atoomnummer zou een ander element betekenen. Het atoomnummer is de identiteitskaart van een element; het massagetal niet.",
                None,
            ],
        ),
        dict(
            aanpak="Periode is de rij (horizontaal), groep is de kolom (verticaal). Het groepsnummer geeft bij de hoofdgroepen het aantal valentie-elektronen, het periodenummer het aantal bezette schillen.",
            waarom=[
                "Onthoud het met de klinker: periode is een rij, dus liggend. De elementen in één groep lijken op elkaar omdat ze hetzelfde aantal buitenste elektronen hebben.",
                "Twee valentie-elektronen uit de groep, vier bezette schillen uit de periode. Het is dus calcium, en het staat bij de aardalkalimetalen.",
                "Vul de schillen op: 2 in de eerste, 8 in de tweede, en de elfde elektron begint de derde schil. Die ene buitenste elektron verklaart waarom natrium zo graag reageert.",
                None,
            ],
        ),
        dict(
            aanpak="Atomen reageren om aan een volle buitenste schil te komen. Zoek dus telkens de kortste weg daarnaartoe: een paar elektronen afstaan of een paar opnemen, wat het minst werk is.",
            waarom=[
                "De edelgassen hebben die verdeling van nature, en daarom is ze de maatstaf. Alle andere atomen proberen er met opnemen, afstaan of delen te komen.",
                "Zuurstof heeft zes valentie-elektronen: twee erbij geeft acht, zes eraf geeft nul. Twee is de kortste weg, dus wordt het O²⁻. Metalen links hebben er maar één of twee, en voor hen is afstaan net het makkelijkst.",
                "Daarom heten ze edel: ze doen niet mee. Helium heeft al bij twee elektronen een volle eerste schil, de andere edelgassen bij acht.",
                "Helium, neon en argon zijn de drie bekendste; krypton, xenon en radon horen er ook bij. Ze staan allemaal in de laatste kolom.",
            ],
        ),
        dict(
            aanpak="Het periodiek systeem leest als een landkaart: metalen links en in het midden, niet-metalen rechtsboven, en de edelgassen in de laatste kolom. Eigenschappen veranderen geleidelijk als je erin wandelt.",
            waarom=[
                "De scheidingslijn loopt diagonaal naar rechtsonder. Daarlangs liggen de metalloïden zoals silicium, die zich half als metaal en half als niet-metaal gedragen; daar steunt de hele elektronica op.",
                "Dat lees je af aan het groepsnummer, niet aan het periodenummer. Het periodenummer geeft het aantal bezette schillen; die twee niet verwisselen is hier de hele oefening.",
                "Naar rechts komen de atomen steeds dichter bij een volle schil, en dus nemen ze liever elektronen op dan af te staan. Fluor, rechtsboven, is daarin het sterkst van alle elementen.",
            ],
        ),
        dict(
            aanpak="Vul de schillen van binnen naar buiten: maximaal 2 in de eerste, dan 8, dan 8. Wat na het vullen in de buitenste schil overblijft, zijn de valentie-elektronen, en net die zet je in het stipmodel.",
            waarom=[
                "Reken na bij zwavel: 2 plus 8 is 10, en 16 min 10 is 6 in de buitenste schil. Zwavel en zuurstof hebben dus beide zes valentie-elektronen, en daarom staan ze in dezelfde groep en lijken ze op elkaar.",
                "Twee, want de eerste schil is de kleinste. Daarom is helium met zijn twee elektronen al een edelgas.",
                None,
                "Alleen de valentie-elektronen, want die doen de chemie. De binnenste schillen laat je weg, net omdat ze niet meedoen aan een binding.",
                "Dit is de samenvatting van de hele bundel in één oefening: het atoomnummer geeft de protonen, het massagetal min het atoomnummer geeft de neutronen, en neutraal betekent even veel elektronen als protonen. Het is natrium.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-energieomzettingen-vermogen-en-rendement-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elk voorbeeld waar de energie in zit. Zit ze in de hoogte, dan is ze gravitationeel; in de beweging, dan kinetisch; in een vervorming, dan elastisch; in de stof zelf, dan chemisch; in de temperatuur, dan thermisch.",
            waarom=[
                "Gravitationele energie hangt af van de hoogte én van de massa: een zware steen op dezelfde muur heeft er meer van. Een ingedrukte veer en een uitgerekt elastiek zijn allebei elastisch, want de energie zit in de vervorming.",
                "Chemische energie zit in de bindingen tussen de atomen. Daarom hebben voedsel, brandstof en een batterij dezelfde soort energie, al lijken ze niets op elkaar.",
            ],
        ),
        dict(
            aanpak="Schrijf een omzetting altijd als van wat naar wat. Vraag je af welke vorm er binnenkomt en welke er nuttig uit komt; de rest gaat meestal als warmte weg.",
            waarom=[
                "Een windmolen zet de kinetische energie van de lucht om, niet de energie van de wind als iets aparts. Bewegende lucht is gewoon massa met snelheid.",
                "Dit is het typische geval van energie die niet verdwijnt maar onbruikbaar wordt: na de afdaling zit ze als warmte in de remmen en in de lucht, en daar kan je ze niet meer uit halen. Daarom worden velgen op een lange afdaling echt heet.",
            ],
        ),
        dict(
            aanpak="Vraag je twee dingen af: kan er materie in of uit, en kan er energie in of uit? Beide ja is open, alleen energie is gesloten, geen van beide is geïsoleerd.",
            waarom=[
                "Een gesloten systeem is dus niet dicht voor warmte, enkel voor stof. Een gesloten fles water koelt wel af, maar er gaat geen water uit.",
                "Uit een pot zonder deksel ontsnapt waterdamp, dus gaat er materie weg, en er gaat ook warmte heen en weer. Met een deksel erop zou het bijna een gesloten systeem zijn.",
                "Een geïsoleerd systeem is een rekenmodel, geen voorwerp. Het is wel een nuttig model: je rekent eerst zonder verlies en kijkt daarna hoeveel het in het echt scheelt.",
            ],
        ),
        dict(
            aanpak="Of een energievorm nuttig of ongewenst is, hangt niet af van de vorm maar van je bedoeling. Dezelfde warmte is nuttig in een waterkoker en ongewenst in een lamp.",
            waarom=[
                "Daarom is warmte niet per definitie verlies. De vraag is altijd: waarvoor heb ik dit toestel gekocht?",
                "Dissipatie betekent verspreiden. De energie is niet weg, maar ze is over de omgeving uitgesmeerd en daardoor niet meer bruikbaar.",
                "Een computer verbruikt geen energie maar zet ze om: bijna alles wat erin gaat, komt er als warmte weer uit. Daarom kan je het vermogen van een computer bijna als een kleine verwarming rekenen.",
                "Dit is de klassieke valkuil van de koelkast: ze maakt geen koude maar verplaatst warmte, en de motor voegt er zelf nog warmte bij. In een gesloten ruimte wordt het dus warmer, niet koeler. Dat is ook waarom een airco een buitenunit nodig heeft.",
            ],
        ),
        dict(
            aanpak="Energie is vermogen maal tijd. Reken altijd eerst om naar watt en seconden, of blijf consequent in kilowatt en uur; door elkaar gebruiken geeft vrijwel altijd een fout met een factor duizend of drieduizendzeshonderd.",
            waarom=[
                "Reken na: 1000 watt maal 3600 seconden geeft 3 600 000 joule. Eén kilowattuur is dus 3,6 megajoule.",
                "Een half uur is 1800 seconden, en 10 maal 1800 is 18 000 joule. Wie met 0,5 rekent in plaats van 1800, komt op 5 uit en dat is geen energie.",
                "Een kilowattuur is energie, geen vermogen: het is een vermogen (kilowatt) maal een tijd (uur). De eenheid van vermogen is de watt.",
                "Een gezin verbruikt zowat 3000 kWh per jaar, dus ruim 10 miljard joule. Daarom kiest de factuur voor de grotere eenheid.",
            ],
        ),
        dict(
            aanpak="Energie verdwijnt nooit; ze verandert enkel van vorm. Bij een vraag over verlies zoek je dus niet waar de energie heen is, maar in welke vorm ze terechtgekomen is.",
            waarom=[
                "Op de hoogste punten staat de schommel een ogenblik stil, dus is de kinetische energie daar echt nul. Alle energie zit dan in de hoogte, en in het laagste punt zit ze helemaal in de snelheid.",
                "Let op het onderscheid tussen verloren en niet meer bruikbaar. De warmte in de lucht en in de ophanging is er nog, maar je krijgt er de schommel niet opnieuw mee hoog.",
                "Wrijving zet energie om in warmte, maar laat ze niet verdwijnen. De wet van behoud van energie geldt altijd, ook met wrijving.",
            ],
        ),
        dict(
            aanpak="Vermogen is energie per tijd: P = E / t. Zoek je de energie, dan draai je het om: E = P maal t. Eén watt is één joule per seconde.",
            waarom=[
                "600 gedeeld door 3 is 200 watt. Let op de eenheid: het antwoord is watt, niet joule, want je deelde door een tijd.",
                "2000 maal 30 is 60 000 joule, dus 60 kilojoule. Hier is het antwoord wel joule, want je vermenigvuldigde met een tijd.",
                "Hier is kilowattuur net het handigst: 1000 watt is 1 kilowatt, en 1 kilowatt maal 2 uur is 2 kWh. Omrekenen naar joule zou 7 200 000 geven, hetzelfde antwoord in een lastiger getal.",
            ],
        ),
        dict(
            aanpak="Rendement is nuttige energie gedeeld door toegevoerde energie, maal honderd. Zoek dus eerst welk getal het nuttige is en welk het totale; het nuttige is altijd het kleinste van de twee.",
            waarom=[
                "400 gedeeld door 500 is 0,8, dus 80 procent. De 100 joule die overblijft, is de dissipatie.",
                "Hier reken je omgekeerd: 25 procent van 800 is 200 joule nuttig, en er gaat dus 600 joule als warmte verloren.",
                "Dat volgt uit de tweede hoofdwet van de thermodynamica, maar je ziet het ook gewoon: elk toestel heeft lagers, draden of lucht die het opwarmt. Een elektrische verwarming haalt wel bijna 100 procent, net omdat warmte daar het nuttige is.",
                "Minder verlies betekent per definitie minder warmte. Daarom kan een ledlamp in een plastic houder, terwijl een gloeilamp van 60 watt zijn omgeving echt heet maakt: daar ging zowat 95 procent als warmte weg.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-warmte-faseovergangen-en-inwendige-energie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Temperatuur is een toestand, warmte is een stroom. Een voorwerp heeft een temperatuur, maar warmte is iets wat tussen twee voorwerpen beweegt. Let dus op de eenheid: joule bij warmte, graden bij temperatuur.",
            waarom=[
                "Je kan de temperatuur van een voorwerp opmeten; de warmte niet, want die is geen eigenschap van het voorwerp maar de energie die erin of eruit gaat.",
                "Temperatuur hangt af van hoe snel de deeltjes gemiddeld bewegen, niet van hoeveel er zijn. Daarom is het een gemiddelde en geen totaal.",
                "Dat is de richting die nooit omkeert zonder hulp. Een koelkast of een warmtepomp kan warmte wel de andere kant op duwen, maar daarvoor is energie nodig.",
                "Dit is het verschil tussen temperatuur en hoeveelheid: een vonk van 1000 °C heeft veel minder energie dan een bad van 40 °C, want in dat bad zitten honderden kilo's water. Daarom kan je een vonk opvangen en in een heet bad niet stappen.",
            ],
        ),
        dict(
            aanpak="Bij elk mengsel geeft het warmere deel af en neemt het koudere op, tot ze dezelfde temperatuur hebben. Zet dat op papier als een balans: wat het ene verliest, krijgt het andere.",
            waarom=[
                "Vraag je bij zulke oefeningen altijd af wie het warmst begint. De melk is kouder dan de koffie, dus neemt de melk op en geeft de koffie af; de eindtemperatuur ligt tussen de twee.",
                "Thermisch evenwicht betekent niet dat de beweging stopt, enkel dat de twee dezelfde temperatuur hebben en er even veel warmte beide kanten op gaat.",
                "De warmtebalans is gewoon de wet van behoud van energie in een andere jas. Wel moet je dan aannemen dat er niets naar de omgeving weglekt, en dat is in het echt nooit helemaal waar.",
            ],
        ),
        dict(
            aanpak="Inwendige energie heeft twee delen: de beweging van de deeltjes (kinetisch) en hun onderlinge binding (potentieel). Bij een temperatuurstijging verandert het eerste, bij een faseovergang het tweede.",
            waarom=[
                "Dat onderscheid is de sleutel tot deze hele bundel: één soort warmte doet de deeltjes sneller bewegen, de andere maakt ze los van elkaar.",
                "Cohesie is de aantrekking tussen deeltjes van dezelfde stof, adhesie die tussen deeltjes van verschillende stoffen. Cohesie maakt een druppel bol, adhesie laat water aan het glas kleven.",
                "Daarom spreekt men van smeltwarmte: energie die erin gaat zonder dat de thermometer beweegt. Je ziet het ook aan een glas met ijs: dat blijft rond nul graden zolang er ijs in zit.",
            ],
        ),
        dict(
            aanpak="Er zijn zes faseovergangen, drie heen en drie terug. Naar een losser geordende toestand (vast naar vloeibaar naar gas) kost warmte; de omgekeerde richting geeft warmte af.",
            waarom=[
                "Onthoud de regel in plaats van de zes namen: losser maken kost energie. Smelten en verdampen gaan dus allebei naar losser, dus nemen ze op.",
                "Condenseren en stollen zijn de terugwegen, en die geven precies dezelfde hoeveelheid energie weer af. Daarom verwarmt condenserende damp zo sterk.",
                "Sublimeren zie je bij droogijs en bij sneeuw die verdwijnt zonder te smelten; desublimeren bij rijm, die rechtstreeks uit de lucht op een koude ruit groeit.",
            ],
        ),
        dict(
            aanpak="Let hier op de woorden altijd en nooit. Bij warmte en faseovergangen zijn er een paar bekende uitzonderingen, en water is bijna altijd de uitzondering.",
            waarom=[
                "Alle warmte gaat tijdens het smelten naar het losmaken van de deeltjes. Bij een mengsel klopt dit niet meer: dat smelt over een traject.",
                "Verdampen vraagt warmte, en die haalt de vloeistof uit wat eronder zit. Daarom koelt een natte doek, een nat T-shirt of een kruik water in een zandbed af.",
                "Water is net de uitzondering: tussen 0 en 4 °C zet het bij afkoelen uit in plaats van te krimpen, en bij bevriezen zet het nog verder uit. Daarom barsten waterleidingen bij vorst.",
                "Dat ijs lichter is dan water bij dezelfde omvang, komt van diezelfde uitzondering. Als ijs zoals bijna alle stoffen zwaarder was dan zijn vloeistof, zouden meren van onderaf dichtvriezen en zou er onder het ijs geen leven overleven.",
            ],
        ),
        dict(
            aanpak="Een vraag naar waarom gaat bijna altijd over één van twee dingen: energie die in een faseovergang gaat in plaats van in temperatuur, of materiaal dat uitzet en krimpt. Zoek eerst welke van de twee.",
            waarom=[
                None,
                "Het is dus niet de vochtigheid die koelt maar het verdampen. Daarom helpt zweten niet goed in vochtige lucht: daar verdampt het nauwelijks en blijft het op je huid staan.",
                "Een vloer van tien meter kan bij een temperatuurverschil van twintig graden al enkele millimeters langer worden. Daarom hebben ook bruggen en spoorrails uitzetvoegen.",
                "Dat is condenseren: warme lucht kan meer waterdamp bevatten dan koude. Hetzelfde gebeurt aan de buitenkant van een koud glas, en dat water komt dus uit de lucht en niet uit het glas.",
            ],
        ),
        dict(
            aanpak="In het dagelijkse leven draait warmte bijna altijd rond drie eigenschappen van water: het kan veel warmte opnemen, het geeft bij bevriezen warmte af, en bij condenseren komt de verdampingswarmte weer vrij.",
            waarom=[
                "Water heeft een hoge specifieke warmtecapaciteit: per kilogram en per graad neemt het meer warmte op dan zowat elke andere gewone stof. Daarom staat er water in een motor, in een radiator en in een kruik.",
                "Dat klinkt tegenstrijdig, water sproeien tegen de vorst, maar bevriezend water geeft zijn stollingswarmte af, en zolang er water bevriest blijft de temperatuur rond nul. De knop zelf bevriest pas bij een lagere temperatuur en blijft zo gespaard.",
                "Dat is een nuttige verbetering van wat mensen vaak denken: koude bestaat niet als iets wat je toevoegt. Daarom moet het water blijven stromen, want stilstaand water warmt op en voert dan niets meer af. Tien minuten koelen is de richtlijn.",
                "Water van 100 °C geeft enkel zijn warmte af terwijl het afkoelt; stoom geeft eerst zijn condensatiewarmte en dán nog de warmte van het afkoelen. Dat is per gram een veelvoud, en daarom zijn stoomwonden zoveel erger.",
                "Dat is hetzelfde principe als de koelvloeistof, maar op de schaal van een zee: het water neemt in de zomer warmte op en geeft die in de winter traag weer af. Daarom is het verschil tussen zomer en winter aan de kust kleiner dan in het binnenland.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-kracht-als-vector-en-bewegingstoestand-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een kracht is meer dan een getal. Je moet vier dingen weten voor ze vastligt: hoe groot, langs welke lijn, welke kant op die lijn, en waar ze aangrijpt. Een pijl geeft die vier tegelijk weer.",
            waarom=[
                "Let op het verschil tussen richting en zin: de richting is de lijn (verticaal, horizontaal), de zin is de kant op die lijn (naar boven of naar beneden). Daarom zijn het twee aparte kenmerken.",
                "Eén newton is ongeveer de kracht waarmee een appel van honderd gram naar beneden wordt getrokken. Zo heb je een gevoel voor de orde van grootte.",
                "Een dynamometer is in de kern een veer met een schaal: hoe verder de veer uitrekt, hoe groter de kracht. Een weegschaal meet eigenlijk ook een kracht en rekent die voor jou om naar kilogram.",
                "Het zwaartepunt hoeft niet in de stof te liggen: bij een ring of een hoefijzer ligt het in de lege ruimte. Het is het punt waarin je het voorwerp in evenwicht kan houden.",
                "Belangrijk bij het tekenen: twee krachten van verschillende grootte krijgen pijlen van verschillende lengte, en je zet erbij hoeveel newton één centimeter voorstelt. Zonder die schaal zegt de lengte niets.",
            ],
        ),
        dict(
            aanpak="Zoek bij elke kracht wie of wat ze uitoefent. De zwaartekracht komt van de aarde, de normaalkracht van een oppervlak, de wrijvingskracht van het contact, de veerkracht van een vervormd voorwerp.",
            waarom=[
                "Wrijving werkt altijd tegen de beweging in, en dat maakt haar niet enkel lastig: zonder wrijving kon je niet stappen, niet remmen en niet sturen.",
                "De normaalkracht heet zo omdat ze loodrecht (normaal) op het oppervlak staat. Ze bestaat enkel zolang er contact is: haal de vloer weg en de normaalkracht verdwijnt meteen.",
            ],
        ),
        dict(
            aanpak="Bij een motor of een raket komt de kracht van het toestel zelf. Wat eruit geduwd wordt, duwt even hard terug, en dat is de kern van de stuwkracht.",
            waarom=[
                "Een raket heeft geen lucht of weg nodig om zich tegen af te zetten: ze stoot gassen naar achteren, en die duwen de raket naar voren. Daarom werkt een raket ook in het luchtledige en een propeller niet.",
            ],
        ),
        dict(
            aanpak="Krachten op één lijn tel je op of trek je van elkaar af. Staan ze loodrecht, dan gebruik je de stelling van Pythagoras. De resultante is de ene kracht die hetzelfde doet als alle andere samen.",
            waarom=[
                "80 plus 50 is 130 newton, en de zin blijft dezelfde als die van de twee duwkrachten.",
                "60 min 25 is 35 newton, in de zin van de grootste van de twee. De zin van je antwoord vermelden hoort erbij, want een kracht is een vector.",
                "Met Pythagoras: 30² is 900, 40² is 1600, samen 2500, en de wortel daarvan is 50 newton. Let op dat 30 plus 40 hier níet 70 geeft: optellen mag enkel als de krachten op dezelfde lijn liggen.",
                "Net omgekeerd: ze heffen elkaar op en de resultante is nul. Dat is precies het geval van het boek op de tafel verderop in deze bundel.",
                "Hou bij de resultante altijd drie dingen bij: haar grootte, haar richting en haar zin. Enkel een getal opschrijven is bij een kracht nooit een volledig antwoord.",
            ],
        ),
        dict(
            aanpak="De vraag is nooit of er krachten werken maar of ze elkaar opheffen. Is de resultante nul, dan verandert de snelheid niet; is ze niet nul, dan versnelt of vertraagt het voorwerp of verandert het van richting.",
            waarom=[
                "Dit is het traagheidsbeginsel, de eerste wet van Newton. Rust en een constante snelheid zijn voor de natuurkunde dezelfde toestand: in beide gevallen verandert de snelheid niet.",
                "Een statisch effect verandert de vorm, een dynamisch effect de bewegingstoestand. Van richting veranderen is ook dynamisch, al blijft de snelheid in getal gelijk: de richting hoort bij de snelheid.",
                "Vertragen vraagt juist een kracht, namelijk een die tegen de beweging in werkt. Zonder enige kracht zou het voorwerp net met dezelfde snelheid blijven doorgaan.",
                "Dat verklaart ook waarom een gordel nodig is: de gordel is de kracht die jou vertraagt. Zonder gordel vertraag je pas bij de botsing tegen het stuur of het glas.",
                "Krachten die elkaar opheffen betekent niet dat er geen krachten zijn. Dat onderscheid is het halve examen bij dit hoofdstuk.",
            ],
        ),
        dict(
            aanpak="Massa is hoeveel stof er in een voorwerp zit, in kilogram, en verandert nooit. Gewicht is de kracht waarmee een hemellichaam eraan trekt, in newton, en verandert met waar je bent.",
            waarom=[
                "In het dagelijkse taalgebruik zeggen we gewicht waar we massa bedoelen; in de fysica is dat onderscheid wel van belang. Op aarde reken je het gewicht als de massa maal ongeveer 9,81 newton per kilogram.",
                "Op de maan is je gewicht ongeveer zes keer kleiner, en je massa precies dezelfde. Met evenveel moeite kan je er dus zes keer hoger springen, maar een rollende kar is er even moeilijk tegen te houden.",
                "Gewichtloos betekent niet zonder zwaartekracht: in het ruimtestation werkt de zwaartekracht nog bijna even sterk als op de grond. Alles valt er samen rond de aarde, en daarom voelt niemand een normaalkracht.",
            ],
        ),
        dict(
            aanpak="Een voorwerp in evenwicht staat niet noodzakelijk stil: evenwicht betekent dat de resultante nul is. Zoek dus telkens de krachten, en kijk of ze elkaar opheffen.",
            waarom=[
                "De normaalkracht is er net zo groot als nodig: leg je een tweede boek erop, dan duwt de tafel harder terug. Ze volgt dus de belasting, tot de tafel het begeeft.",
                "Dat eindpunt heet de grenssnelheid. Een springer zonder open valscherm haalt ongeveer tweehonderd kilometer per uur, met een open valscherm nog zowat twintig: hetzelfde principe, een veel groter oppervlak.",
            ],
        ),
        dict(
            aanpak="Verkeersvragen gaan bijna altijd over twee dingen: traagheid (massa blijft doorgaan) en wrijving (het contact met de weg remt). Zoek welk van de twee in de vraag zit.",
            waarom=[
                "Een lading van duizend kilo die bij vijftig kilometer per uur losschiet, komt met dezelfde snelheid tegen de cabine aan. Daarom gaat het bij sjorren niet om vallen maar om traagheid.",
                "Hoe meer massa, hoe meer kracht er nodig is voor dezelfde vertraging. Dat is de tweede wet van Newton: F is m maal a. Daarom hebben vrachtwagens veel zwaardere remmen en toch een langere remweg.",
                "Opgelet: het is de wrijving die remt, niet de remmen zelf. Een geblokkeerd wiel op nat wegdek glijdt; daarom zit er ABS op, dat de wielen net laat blijven rollen.",
                "Dit is een goede toets voor het begrip: de normaalkracht bestaat enkel bij contact met een oppervlak. De draagkracht van de vleugels is iets anders: die komt van de lucht die langs de vleugel stroomt.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-druk-in-het-dagelijkse-leven-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Druk is kracht per oppervlak: p = F / A. Zoek eerst welke twee van de drie je hebt. Werk altijd in newton en vierkante meter, dan komt het antwoord in pascal uit.",
            waarom=[
                "200 gedeeld door 0,5 is 400 pascal. Door een getal kleiner dan één delen maakt het antwoord groter: op een half zo groot oppervlak is de druk dubbel zo hoog.",
                "Hier draai je de formule om: F is p maal A, dus 300 maal 2 is 600 newton.",
                "Eén pascal is één newton per vierkante meter, en dat is heel weinig: de luchtdruk is ruim honderdduizend pascal. Daarom rekent men in de praktijk met hectopascal of bar.",
                "Het is de verhouding die telt, niet de kracht alleen. Hetzelfde idee zit in een rupsband, een breed skilatje en de poten van een waterloper.",
            ],
        ),
        dict(
            aanpak="De voorvoegsels horen bij elke eenheid: kilo is duizend keer, hecto is honderd keer. Reken altijd eerst om naar pascal voor je vergelijkt.",
            waarom=[
                None,
                "Hecto komt van honderd. Het weerbericht gebruikt hectopascal omdat de luchtdruk dan een handig getal rond 1000 wordt.",
                "600 gedeeld door 0,2 is 3000 pascal, dus 3 kilopascal. Let op de komma: wie door 2 deelt in plaats van door 0,2 zit er een factor tien naast.",
                "De newton is een kracht, de pascal een druk. Dezelfde kracht geeft op een punt een enorme druk en op een plaat een kleine; daarom zijn het twee verschillende grootheden.",
                "1013 hectopascal is 101 300 pascal, ongeveer de gemiddelde luchtdruk op zeeniveau. Een lagedrukgebied zit daaronder en brengt meestal regen, een hogedrukgebied erboven.",
            ],
        ),
        dict(
            aanpak="Druk vergelijk je altijd met de omgeving. Hoger dan buiten is overdruk, lager is onderdruk. Een drukverschil is wat beweging veroorzaakt: lucht en vloeistof gaan van hoog naar laag.",
            waarom=[
                "Een manometer wijst meestal de overdruk aan, niet de volledige druk. Een fietsband van 4 bar staat dus op 4 bar meer dan de lucht errond.",
                "Onthoud het aan de naam: baro komt van gewicht of zwaarte, en de luchtdruk is letterlijk het gewicht van de luchtkolom boven je.",
                "De luchtdruk daalt met de hoogte, want er ligt minder lucht boven je. Op de top van de Mont Blanc is hij nog ongeveer de helft van die op zeeniveau.",
                "Dat is een goede verbetering van wat mensen vaak denken: je trekt de drank niet omhoog, de luchtdruk duwt haar omhoog. Daarom werkt een rietje niet in het luchtledige, en kan je met een rietje nooit hoger dan ongeveer tien meter zuigen.",
                "Dat buisje naar je neus- en keelholte heet de buis van Eustachius. Slikken, gapen of zachtjes blazen met dichtgeknepen neus opent het even, en dan is de druk weer gelijk.",
                "Let op de redenering: de lucht in de zak zet niet uit omdat er iets bij komt, maar omdat er buiten minder tegendruk is. Dat is hetzelfde principe als de oren in het vliegtuig, maar met een zak in plaats van een trommelvel.",
            ],
        ),
        dict(
            aanpak="Wil je weinig druk, maak dan het oppervlak groot; wil je veel druk, maak het klein. Welke van de twee je nodig hebt, hangt af van wat je wil bereiken: dragen of doordringen.",
            waarom=[
                "Hetzelfde voorwerp kan beide kanten gebruiken: een mes heeft een scherpe snijkant (kleine A, veel druk) en een brede rug waar je gerust op kan duwen.",
                "Met de formule erbij: F blijft hetzelfde, A wordt groter, dus p wordt kleiner. Precies daarvoor zet men viltjes of brede plaatjes onder de poten van een zware kast.",
            ],
        ),
        dict(
            aanpak="Druk in een gas komt van botsende deeltjes. Meer deeltjes, snellere deeltjes of minder ruimte geven telkens meer botsingen tegen de wand, en dus meer druk.",
            waarom=[
                "Dat de druk in alle richtingen gelijk is, komt doordat de deeltjes in alle richtingen door elkaar vliegen. Daarom duwt een opgeblazen ballon overal even hard tegen zijn wand.",
                "Verwarmen laat de deeltjes sneller bewegen. Het volume kan in een stalen fles niet mee, dus kan enkel de druk stijgen.",
                "Daarom staat er ook op dat je een spuitbus niet in het vuur mag gooien, zelfs niet als ze leeg lijkt: er zit altijd nog drijfgas in.",
            ],
        ),
        dict(
            aanpak="Elke vraag in deze reeks is dezelfde: hoe snel bewegen de deeltjes, en kan het volume mee? Antwoord dus met de deeltjes én met de wand, niet enkel met warmer of kouder.",
            waarom=[
                "Een gas duwt in alle richtingen, ook omhoog en zijwaarts. Daarom hoeft een gevulde ballon niet op iets te staan om bol te blijven.",
                "In de zon kan het staal van een fles ruim vijftig graden halen. Daarom staan gasflessen in de schaduw en met hun klep naar boven.",
                "Een veiligheidsklep is bewust het zwakste punt: liever gecontroleerd gas laten ontsnappen dan een vat dat openscheurt. Een snelkookpan heeft er daarom ook een.",
                "Vijftien graden warmer geeft al merkbaar meer druk in de band. Oppompen doe je met een koude band, en de aanbevolen waarde geldt ook voor een koude band.",
                "Dit is het omgekeerde van de spuitbus: tragere deeltjes, minder botsingen, lagere druk. Omdat een ballon wel kan krimpen, geeft het volume mee en blijft de druk ongeveer gelijk aan die buiten. In de warmte wordt de ballon weer bol.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-elektriciteit-de-wet-van-ohm-en-veiligheid-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie grootheden, drie eenheden, drie toestellen. Stroomsterkte is hoeveel er per seconde passeert, spanning is het duwtje dat de stroom veroorzaakt, weerstand is hoe moeilijk de stroom erdoor komt.",
            waarom=[
                "Een beeld dat helpt: spanning is het hoogteverschil, stroom is hoeveel water er stroomt, weerstand is hoe nauw de buis is. De toestelnamen volgen de eenheden, dus die hoef je niet apart te leren.",
                "In serie, want de stroom moet er dóór om gemeten te worden. Een ampèremeter heeft daarom een heel kleine eigen weerstand.",
                "Parallel, want je meet het verschil tussen twee punten, zoals je een hoogteverschil meet. Een voltmeter heeft net een heel grote weerstand, zodat er bijna geen stroom door haar heen gaat.",
            ],
        ),
        dict(
            aanpak="De wet van Ohm: U = R maal I. Zoek welke twee je hebt en vorm de formule om: I = U / R en R = U / I. Reken in volt, ampère en ohm, nooit in milliampère.",
            waarom=[
                "12 gedeeld door 20 is 0,6 ampère, dus 600 milliampère. Een antwoord kleiner dan één is bij stroom heel gewoon.",
                "50 maal 0,2 is 10 volt. Hier vermenigvuldig je, want je zoekt U.",
                "230 gedeeld door 2 is 115 ohm. Dat is ongeveer de weerstand van een toestel van 460 watt op het net.",
                "Zo leest de formule zich: staat R in de noemer, dan werkt hij omgekeerd. Halveer R en I verdubbelt, verdubbel R en I halveert. Dat heet een omgekeerd evenredig verband.",
            ],
        ),
        dict(
            aanpak="Metalen en zoutoplossingen geleiden, kunststof, glas, droog hout en droge lucht niet. Let op het woord droog: water met zouten erin geleidt wel, en dat maakt een natte hand gevaarlijk.",
            waarom=[
                "Droog hout isoleert, vochtig hout veel minder. Daarom is een houten ladder bij elektriciteitswerken geen garantie, zeker niet buiten in de regen.",
                "Een zoutoplossing geleidt doordat er geladen ionen in bewegen, niet doordat er elektronen door een metaal lopen. Je lichaam is in de kern ook een zoutoplossing, en daarom geleidt het.",
                "Het is omgekeerd: goed geleiden betekent weinig weerstand. Geleidingsvermogen en weerstand zijn twee manieren om hetzelfde te zeggen, in tegengestelde richting.",
                "Een snoer heeft dus twee taken tegelijk: de stroom geleiden waar hij moet gaan en hem tegenhouden waar hij niet mag komen. Een beschadigde mantel maakt precies die tweede taak stuk.",
            ],
        ),
        dict(
            aanpak="In serie ligt er maar één weg: de weerstanden tel je op. Parallel liggen er meerdere wegen naast elkaar: de totale weerstand wordt kleiner dan de kleinste afzonderlijke.",
            waarom=[
                "In serie gewoon 10 plus 10 is 20 ohm. De stroom moet door beide, dus wordt het moeilijker.",
                "Parallel geldt 1/R = 1/10 + 1/10, dus R is 5 ohm. Bij twee gelijke weerstanden parallel is het altijd de helft. Verrassend maar logisch: twee wegen naast elkaar laten meer stroom door dan één.",
                "Daarom waren oude kerstlichtjes zo lastig: één kapot lampje en de hele slinger lag eruit. Nieuwe slingers zijn daarom anders geschakeld.",
                "Twee redenen die je beide moet noemen: dezelfde spanning op elke lamp (230 volt) én afzonderlijk schakelbaar. Daarom is een huisinstallatie parallel, met de schakelaars in serie met elk hun eigen lamp.",
            ],
        ),
        dict(
            aanpak="De weerstand van een draad hangt af van drie dingen: langer geeft meer weerstand, dikker geeft minder, en het materiaal zelf bepaalt de rest.",
            waarom=[
                "Weer het waterbeeld: een lange, nauwe buis laat minder door dan een korte, wijde. Bij een draad geldt precies hetzelfde.",
                "Dit is het Joule-effect omgekeerd gedacht: weerstand plus stroom geeft warmte, en een te dunne draad bij een zwaar toestel wordt heet. Daarom staat op een verlengsnoer hoeveel ampère het mag dragen, en rolt men het best helemaal uit.",
            ],
        ),
        dict(
            aanpak="Vermogen is spanning maal stroom: P = U maal I. Voor het verbruik reken je dat vermogen maal de tijd, en voor kilowattuur deel je het vermogen eerst door duizend.",
            waarom=[
                "230 maal 2 is 460 watt. Je kan het ook met de weerstand van 115 ohm nagaan: dat geeft hetzelfde.",
                "60 watt is 0,06 kilowatt, en 0,06 maal 5 uur is 0,3 kWh. Tegen zowat 35 cent per kWh kost dat ongeveer tien cent.",
                "Het Joule-effect is zowel nuttig als lastig: nuttig in een kachel of een broodrooster, lastig in een snoer of een gsm-lader die warm wordt. Dezelfde natuurwet, een andere bedoeling.",
            ],
        ),
        dict(
            aanpak="Twee beveiligingen die iets anders doen: de zekering beschermt de installatie tegen te veel stroom, de verliesstroomschakelaar beschermt de mens tegen stroom die een verkeerde weg neemt.",
            waarom=[
                "Een zekering springt bij bijvoorbeeld 16 ampère; dat is veel meer dan een mens verdraagt. Daarom alleen is een zekering geen bescherming voor personen, en is de verliesstroomschakelaar verplicht.",
                "De aarding geeft de stroom een gemakkelijkere weg dan door jouw lichaam. Aarding en verliesstroomschakelaar werken dus samen: de ene leidt de stroom weg, de andere merkt dat op en schakelt af.",
                "Dat is de eerste regel van elke eerste hulp: eerst je eigen veiligheid. Wie het slachtoffer aanraakt terwijl de stroom erop staat, wordt zelf het tweede slachtoffer. Lukt afschakelen niet, dan duw je de persoon weg met iets dat niet geleidt, zoals droog hout.",
                "Ze meet of er even veel stroom terugkomt als er heen gaat. Mist er iets, dan loopt dat ergens weg, mogelijk door een mens, en ze schakelt binnen enkele honderdsten van een seconde af.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-veilig-werken-meten-en-levensreddend-handelen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Elk pictogram beeldt af wat er kan gebeuren. Een vlam is brand, een doodshoofd is giftig, een wegvretende hand is bijtend, een dode vis en boom is gevaarlijk voor het milieu. Lees ook altijd de tekst naast het teken.",
            waarom=[
                "Het doodshoofd staat voor acuut giftig. Een uitroepteken is het lichtere teken: schadelijk of irriterend, maar niet dodelijk bij een kleine hoeveelheid.",
                "Bijtende stoffen tasten je huid en je ogen aan en vreten ook metaal weg. Daarom horen bij zulke stoffen altijd handschoenen en een bril, en nooit een metalen schaaltje.",
                "Naast de pictogrammen horen er ook gevaren- en veiligheidsaanduidingen te staan. Een product uit een flesje zonder etiket gebruik je niet, want je weet niet wat het is.",
            ],
        ),
        dict(
            aanpak="De labovoorschriften komen niet uit willekeur: achter elk ervan zit een ongeval dat iemand eens overkomen is. Vraag je bij elke regel af wat er zou kunnen misgaan zonder die regel.",
            waarom=[
                "Terugschenken kan de hele voorraadfles verontreinigen met wat er aan je glaswerk hing. Giet dus liever iets te weinig uit en vul bij.",
                "Een spatje kan ook van de tafel van je buur komen. Daarom geldt het hele labo als één werkplek en blijft de bril op zolang er iemand werkt.",
                "Je wappert voorzichtig met je hand wat damp naar je toe, op afstand, en je ademt nooit diep over de opening in. Eén diepe inademing van ammoniak of chloor volstaat om je luchtwegen te beschadigen.",
                "Onthoud het met een spreekwijze: water eerst. Verdunnen geeft veel warmte, en een beetje zuur in veel water verdeelt die warmte over de hele hoeveelheid; water op onverdund zuur kan lokaal gaan koken en opspatten.",
                "In de afvoer kunnen stoffen elkaar tegenkomen die je nooit zou mengen, bijvoorbeeld een zuur en een bleekmiddel. Daarnaast is een waterzuivering niet gemaakt voor zware metalen of oplosmiddelen.",
            ],
        ),
        dict(
            aanpak="Nauwkeurig meten is een vaardigheid: het juiste toestel, de juiste kijkhoek, en niet meer cijfers opschrijven dan je echt gemeten hebt.",
            waarom=[
                "Een maatkolf en een pipet zijn nauwkeuriger dan een maatcilinder, en een bekerglas is enkel geschikt om iets ruw af te meten. Op elk stuk glaswerk staat zijn nauwkeurigheid.",
                "Die fout heet parallax. De holle bovenkant van de vloeistof heet de meniscus, en bij water lees je onderaan die meniscus af.",
                "Alle cijfers die je echt gemeten hebt tellen mee, de nul erbij als ze gemeten is. 1,2 meter zegt dus iets anders dan 1,20 meter: het tweede is tien keer nauwkeuriger gemeten.",
                "Herhalen helpt enkel tegen toevallige fouten, niet tegen een systematische. Een weegschaal die vijf gram te hoog staat, blijft dat bij elke meting; die vind je enkel door te ijken.",
            ],
        ),
        dict(
            aanpak="Eerste hulp heeft een vaste orde: veiligheid, toestand nagaan, hulp bellen, handelen. Wie die orde volgt, hoeft bij een ongeval niet na te denken over wat eerst komt.",
            waarom=[
                "Dat geldt ook bij een verkeersongeval (fluohesje, waarschuwingsdriehoek), bij elektriciteit (eerst afschakelen) en bij gas of rook (niet naar binnen gaan). Jouw veiligheid is geen egoïsme maar een voorwaarde.",
                "112 werkt in heel Europa, ook op een gsm zonder simkaart. 1733 is er voor de huisarts van wacht, als het niet dringend is.",
                "De zijligging dient om de luchtweg vrij te houden, zodat de tong niet achteruitzakt en braaksel eruit kan lopen. Blijven kijken is een deel van de hulp: ademt de persoon niet meer normaal, dan begin je met reanimeren.",
            ],
        ),
        dict(
            aanpak="Bij een hartstilstand telt elke minuut: zonder hulp zakt de kans om te overleven met zowat tien procent per minuut. Daarom: niet twijfelen, bellen en duwen.",
            waarom=[
                "Die happende bewegingen heten gaspen en komen vaak voor in de eerste minuten. Wie ze voor ademen aanziet, begint niet te reanimeren, en dat is de gevaarlijkste fout bij dit onderwerp.",
                "Dertig massages en twee beademingen, in een tempo van ongeveer honderd tot honderdtwintig per minuut. Durf je niet te beademen, dan is enkel blijven duwen veel beter dan niets doen.",
                "Vijf tot zes centimeter, op het midden van de borstkas, en laat de borstkas tussen twee massages volledig terugkomen. Te zacht duwen brengt geen bloed rond.",
                "Hulp bellen gaat voor, want een AED en de ambulance zijn nodig; daarna meteen duwen. Zijligging is net wat je niet doet bij iemand die niet ademt: die ligt op de rug op een harde ondergrond.",
                "Je gaat door tot de hulpdiensten het overnemen, tot het slachtoffer weer normaal ademt, of tot je echt niet meer kan. Daarom wissel je met iemand anders af, elke twee minuten; stoppen is geen optie.",
            ],
        ),
        dict(
            aanpak="Bij verdrinking en verslikking is de vraag telkens dezelfde: hoe help ik zonder zelf in gevaar te komen, en hoe krijg ik de luchtweg weer vrij?",
            waarom=[
                "Reik iets aan, gooi iets dat drijft of gebruik een stok. Een paniekerend slachtoffer trekt zijn redder mee onder water; daarom springt zelfs een goede zwemmer niet zomaar in.",
                "Kan iemand nog hoesten, dan laat je hoesten: dat is de sterkste manier om het eruit te krijgen. Pas als dat niet meer gaat, geef je slagen tussen de schouderbladen en daarna buikstoten. Bij een baby van minder dan één jaar geen buikstoten maar borststoten.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-grootheden-eenheden-en-wetenschappelijk-onderzoek-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een grootheid is wat je meet, een eenheid is waarin je het uitdrukt. Zeven grootheden zijn de basis van het SI-stelsel; alle andere eenheden zijn daaruit samengesteld, zoals de newton en de joule.",
            waarom=[
                "Deze drie zijn basiseenheden: ze zijn niet uit andere opgebouwd. De kilogram is de enige basiseenheid met een voorvoegsel al in haar naam.",
                "Deze drie zijn afgeleid: één newton is één kilogram maal meter per seconde kwadraat, één joule is één newton maal meter, en één watt is één joule per seconde.",
                "Let op: de echte SI-eenheid van temperatuur is de kelvin, en graden Celsius is de eenheid waarin we het dagelijks uitdrukken. Een verschil van één graad Celsius is wel precies één kelvin; enkel het nulpunt verschilt, want 0 °C is 273,15 K.",
                "Een getal zonder eenheid is geen meetresultaat. Twaalf kan twaalf meter, twaalf seconden of twaalf graden zijn, en daar valt niets mee te doen.",
            ],
        ),
        dict(
            aanpak="Omrekenen gaat over de voorvoegsels: kilo is duizend keer meer, centi honderd keer minder, milli duizend keer minder, micro een miljoen keer minder. Vraag je altijd af of je antwoord groter of kleiner moet worden dan wat je had.",
            waarom=[
                "Van kilogram naar gram maal duizend, van centimeter naar meter gedeeld door honderd. Het eerste antwoord wordt dus groter, het tweede kleiner; die controle haalt de meeste fouten eruit.",
                "2,5 kilometer is 2500 meter, en 3 milliliter is 0,003 liter. Een milliliter is trouwens precies één kubieke centimeter.",
                "Micro staat voor een miljoenste, dus 10⁻⁶. Twee microseconden is 2 maal 10⁻⁶ seconden, of 0,000002 seconden; met machten van tien schrijf je dat zonder nullen te tellen.",
            ],
        ),
        dict(
            aanpak="Kijk eerst naar de grafiek of naar de getallen. Een rechte door de oorsprong is recht evenredig, een rechte ernaast is lineair, een product dat gelijk blijft is omgekeerd evenredig, en vier keer meer bij twee keer meer is kwadratisch.",
            waarom=[
                "Elk recht evenredig verband is ook lineair, maar niet elk lineair verband is recht evenredig. Dat is de valkuil in deze reeks.",
                "Bij omgekeerd evenredig blijft het product gelijk: 2 maal 12, 4 maal 6, 8 maal 3. Bij kwadratisch gaat het maal vier als de oorzaak maal twee gaat, zoals bij de oppervlakte van een vierkant.",
                "Een voorbeeld maakt het scherp: een taxi met een opstapkost van 5 euro plus 2 euro per kilometer is lineair maar niet recht evenredig. Bij nul kilometer betaal je al iets, en dus loopt de rechte niet door de oorsprong.",
            ],
        ),
        dict(
            aanpak="Nauwkeurigheid zit niet enkel in je toestel maar ook in hoe je het resultaat opschrijft. Nooit meer cijfers dan je gemeten hebt, en altijd eerst schatten zodat je een onzinnig antwoord meteen ziet.",
            waarom=[
                "Elk cijfer dat je opschrijft is een belofte over je nauwkeurigheid. 325 gram belooft gram-nauwkeurigheid, en dat is precies wat deze balans kan.",
                "Twee nullen erbij schrijven zou betekenen dat je zeker weet dat het niet 325,01 is, en dat weet je niet. Afrondingsfouten binnen je berekening mag je wel langer meeslepen; enkel je eindresultaat rond je af.",
                "Een schatting beschermt je tegen een fout met een factor duizend. Reken je de massa van een appel uit en kom je op 20 kilo, dan weet je dat er iets mis is zonder je berekening na te lezen.",
                "Dit onderscheid bepaalt wat je eraan kan doen: herhalen helpt tegen toeval, ijken en nakijken van je opstelling helpen tegen een systematische fout. Een scheve weegschaal word je door honderd metingen niet kwijt.",
            ],
        ),
        dict(
            aanpak="De wetenschappelijke methode loopt van vraag naar besluit: eerst het probleem afbakenen, dan een hypothese, dan een plan, dan meten, en daarna besluiten en terugkijken.",
            waarom=[
                "De hypothese komt vóór het plan, en het plan vóór het meten. Wie eerst meet en daarna een verwachting formuleert, kan altijd iets vinden dat lijkt te kloppen.",
                "Een hypothese is geen gok maar een onderbouwde verwachting, met een reden erbij. Ze moet ook te weerleggen zijn; een uitspraak die altijd waar is, kan je niet onderzoeken.",
                "Reflectie is geen formaliteit: daar zeg je wat er aan je methode schortte en wat je volgende keer anders zou doen. Een onderzoek zonder reflectie is niet af.",
                "Een weerlegde hypothese is een geldig resultaat. Je weet nu iets wat je ervoor niet wist, en dat is precies hoe wetenschap werkt. Enkel je gegevens bijsturen om je hypothese te sparen is fout.",
            ],
        ),
        dict(
            aanpak="Een goede proef verandert één ding en houdt al de rest gelijk. Wat je verandert is de variabele; alles wat gelijk blijft, zorgt ervoor dat je het verschil aan die ene variabele mag toeschrijven.",
            waarom=[
                "Je hebt ook meer dan één plantje per groep nodig, want één plantje kan toevallig zwak zijn. Een groep zonder extra licht is je controlegroep.",
                "Twee dingen samen veranderen heet een verstorende variabele. Daarom heet dit een gecontroleerd experiment: één knop tegelijk.",
                "Herhaalbaarheid is geen papierwerk maar de kern van het vak: een resultaat dat niemand anders kan nabootsen, telt niet. Daarom staat in elk wetenschappelijk artikel een stuk over de methode.",
                "Dat is wetenschappelijke integriteit, en ze geldt even hard voor een schoolopdracht als voor een labo. Een resultaat dat niet bij je verwachting past, is net het interessante resultaat.",
            ],
        ),
        dict(
            aanpak="Ontwerpen gaat in dezelfde geest als onderzoeken, maar het eindpunt is een oplossing in plaats van een antwoord. Eerst het probleem scherp krijgen en de criteria opschrijven, dan bouwen, dan testen en verbeteren.",
            waarom=[
                "Engineering is het ontwerpen en bouwen zelf, technologie gaat over de middelen en de toestellen. Vier vakgebieden die bij een echt probleem altijd samen opduiken.",
                "Criteria zijn de eisen (het moet honderd kilo dragen), randvoorwaarden zijn de grenzen (het mag niet meer dan twintig euro kosten). Zonder criteria kan je niet beoordelen of je oplossing werkt.",
                "Een probleem scherp stellen is het halve werk. Wie meteen begint te bouwen, lost vaak niet het probleem op dat er echt was.",
                "Dat heet decompositie, en het is ook de manier waarop programmeurs werken. Bijkomend voordeel: aan losse delen kan je met meerdere mensen tegelijk werken.",
                "Mooi te zien hoe de vier samenwerkten: biologie en chemie voor het vaccin zelf, techniek voor de koelketen tot min zeventig graden, en wiskunde voor de modellen die de verspreiding voorspelden. Geen van de vier alleen had het gekund.",
                "Testen en verbeteren horen bij het ontwerpen: bijna geen enkele eerste versie haalt alle criteria. Dat wordt vaak een cyclus die je meermaals doorloopt.",
            ],
        ),
    ]
)

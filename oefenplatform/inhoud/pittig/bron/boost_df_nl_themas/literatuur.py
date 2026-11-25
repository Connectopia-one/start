"""Fictie, personages, verhaallijn, tijd en ruimte — pittig (Boost dubbele finaliteit, Nederlands).

Strikt binnen nldf_literatuur: fictie en non-fictie, literaire teksten,
personages, verhaallijn, tijd en ruimte, boodschap en je eigen beleving.
Geen verteller, rijmschema of stromingen: die staan enkel bij doorstroom."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, PAARS, ROOD, GEEL, LICHTGROEN

BP = Prent("boekenplank", "Zes boeken op een plank", "zes boeken naast elkaar met een titel en een soort, letters A tot F")
BOEKEN = [
    ("A", ["Het geheim van", "de vuurtoren"], "roman", BLAUW),
    ("B", ["Mijn leven", "op de fiets"], "biografie van een wielrenner", ORANJE),
    ("C", ["Reisgids", "Portugal"], "reisgids", LICHTGROEN),
    ("D", ["De draak van", "Dommelstein"], "strip", PAARS),
    ("E", ["Koken voor", "beginners"], "kookboek", GEEL),
    ("F", ["Sprookjes", "van overal"], "sprookjesboek", ROOD),
]
BP.rect(40, 560, 920, 18, GRIJS, DONKER, 2, 2)
LET = {}
for i, (t, titel, soort, kleur) in enumerate(BOEKEN):
    x = 50 + i * 152
    BP.rect(x, 110, 140, 450, kleur, DONKER, 8, 3)
    BP.rect(x + 6, 150, 128, 90, "#ffffff", DONKER, 4, 2)
    BP.tekst(x + 70, 188, titel[0], 16, vet=True); BP.tekst(x + 70, 214, titel[1], 16, vet=True)
    BP.rect(x + 6, 300, 128, 110, "#ffffff", DONKER, 4, 2)
    woorden = soort.split()
    regels = [" ".join(woorden[:2]), " ".join(woorden[2:])] if len(woorden) > 2 else [soort]
    for j, r in enumerate(regels):
        BP.tekst(x + 70, 350 + j * 26, r, 16)
    BP.letter(x + 70, 510, t)
    LET[t] = (x + 70, 510)
U = "boekenplank.svg"
Z = {t: Prent.zone(50 + i * 152, 110, 140, 450) for i, (t, *_ ) in enumerate(BOEKEN)}

FRAGMENT = ("Lees het fragment.\n\n"
            "In het kleine vissersdorp wist iedereen alles van iedereen. Toch had niemand gezien dat Noor elke avond naar de oude vuurtoren liep. "
            "Daar, boven aan de wenteltrap, las ze de brieven van haar grootvader, die veertig jaar eerder op zee verdwenen was.\n\n"
            "'Waarom vertel je het niet aan je mama?' vroeg haar vriend Ilias, die haar op een avond gevolgd was.\n"
            "Noor zweeg. Ze dacht aan de winter van haar achtste verjaardag, toen ze haar moeder had horen huilen bij een oude foto.\n\n"
            "De volgende ochtend legde ze de brieven op de keukentafel.")

VRAGEN = [
    klik("Bekijk de boekenplank. Klik op alle boeken met non-fictie.", U, [Z["B"], Z["C"], Z["E"]],
         "Een biografie, een reisgids en een kookboek gaan over wat echt bestaat of gebeurd is. Een roman, een strip en sprookjes zijn verzonnen."),
    klik("Klik op het boek dat vooral instructies geeft en dus geen literaire tekst is.", U, [Z["E"]],
         "Een kookboek zegt je wat je moet doen, net als een bijsluiter."),
    klik("Klik op het boek dat met tekeningen en taal samen een verzonnen verhaal vertelt.", U, [Z["D"]],
         "Een strip vertelt met beeld en taal, en kan net zo goed literair zijn."),
    casus(FRAGMENT, [
        inv("Wie is het hoofdpersonage? Eén naam.", ["Noor"], "Het verhaal draait rond haar en haar geheim."),
        tabel("Hoort dit bij de ruimte of bij de tijd van het verhaal?",
              [("het vissersdorp", "ruimte"), ("elke avond", "tijd"), ("de oude vuurtoren", "ruimte"), ("de volgende ochtend", "tijd")],
              "De ruimte is waar het speelt, de tijd is wanneer en hoe lang.", ["ruimte", "tijd"]),
        keuze("Door de herinnering aan haar achtste verjaardag wordt het verhaal [[*niet chronologisch|helemaal chronologisch|zonder tijd]] verteld.", "Het verhaal springt even terug naar vroeger."),
        mk("Waarom is het opvallend dat niemand Noor naar de vuurtoren ziet lopen?",
           ["in zo'n klein dorp blijft bijna niets geheim", "omdat de vuurtoren eigenlijk op een andere planeet staat", "omdat het hele verhaal ver in de toekomst speelt", "omdat Noor in dit fragment maar een bijpersonage is"],
           0, "De ruimte is geen decor: in een dorp waar iedereen alles weet, valt een geheim extra op."),
        keuze("Ilias is in dit fragment een [[*bijpersonage|hoofdpersonage|schrijver]].", "Hij speelt mee, maar het verhaal draait niet rond hem."),
        tabel("Staat dit letterlijk in de tekst, of is het een interpretatie?",
              [("Noor leest de brieven van haar grootvader.", "staat in de tekst"), ("Noor wil haar moeder geen verdriet doen.", "interpretatie"), ("Ilias volgde Noor op een avond.", "staat in de tekst"), ("Het verhaal toont dat zwijgen een familie kan verdelen.", "interpretatie")],
              "Een interpretatie leid je af; je moet ze kunnen staven met wat er staat.", ["staat in de tekst", "interpretatie"]),
        mk("Welke zin verwoordt het best je eigen beleving bij het fragment?",
           ["Ik voelde mee met Noor, omdat ik ook eens iets verzweeg om iemand te sparen.", "Het fragment telt drie alinea's en er komen twee personages in voor, plus een moeder.", "Noor loopt elke avond naar de vuurtoren en leest daar de brieven van haar opa.", "Het is een goed fragment, want het is gewoon heel goed geschreven en dus mooi."],
           0, "Beleving is wat het fragment met jou deed, met een waarom erbij. Navertellen of tellen is geen beleving."),
        open_("Wat zou de boodschap van dit fragment kunnen zijn? Leg uit met een detail uit de tekst.",
              "Misschien dat een geheim zwaarder wordt hoe langer je het bewaart. Noor draagt de brieven alleen, maar op het einde legt ze ze toch op de keukentafel."),
    ]),
    sorteer("Fictie of non-fictie?", ["fictie", "non-fictie"],
            [("een sprookje over een pratende vos", "fictie"), ("het dagboek van een echte bergbeklimmer", "non-fictie"), ("een sciencefictionverhaal op Mars", "fictie"), ("een krantenartikel over de verkiezingen", "non-fictie"), ("een jeugdroman over een meisje dat een paard redt", "fictie")],
            "Fictie is verzonnen, ook als het heel echt lijkt."),
    tabel("Is dit een literaire tekst?",
          [("een gedicht over de zee", J), ("een strip over een oorlog", J), ("de bijsluiter van een pijnstiller", F), ("een liedtekst over heimwee", J), ("een treinregeling", F)],
          "Literaire teksten hebben een esthetische waarde en spelen in op emoties."),
    mk("Wat is het verschil tussen een hoofdpersonage en een bijpersonage?",
       ["het verhaal draait vooral rond het hoofdpersonage", "een hoofdpersonage is altijd aardig en dapper", "een bijpersonage komt in het hele boek maar in één enkele zin voor", "het hoofdpersonage is altijd de schrijver zelf"],
       0, "Een hoofdpersonage hoeft niet sympathiek te zijn: het is degene wiens verhaal je volgt."),
    koppel("Koppel het begrip aan het voorbeeld uit een jeugdboek.",
           [("ruimte", "een verlaten pretpark"), ("tijd", "één zomer in 1985"), ("personage", "een jongen die zijn hond zoekt"), ("verhaallijn", "hij zoekt, vindt een spoor en vindt de hond terug")],
           ["de prijs van het boek"],
           "Waar, wanneer, wie en wat er gebeurt."),
    volgorde("Een verhaal begint met: 'Ik stond voor de poort van mijn nieuwe school.' Daarna springt het terug naar de dag dat het gezin besliste te verhuizen. Zet de gebeurtenissen in de volgorde waarin ze echt gebeurden.",
             ["het gezin beslist te verhuizen", "de verhuiswagen rijdt weg", "de ik staat voor de poort van de nieuwe school", "de ik zit voor het eerst in de nieuwe klas"],
             "Het verhaal vertelt niet chronologisch, maar de gebeurtenissen zelf hebben wel een volgorde."),
    keuze("Twee personages die elk om de beurt een hoofdstuk krijgen, geven een boek [[*twee verhaallijnen|twee schrijvers|twee ruimtes]].", "Die lijnen komen vaak op het einde samen."),
    tabel("Klopt dit over personages?",
          [("Een hoofdpersonage moet sympathiek zijn.", F), ("Een personage dat niet verandert, kan toch interessant zijn.", J), ("De schrijver is altijd ook een personage in zijn roman.", F), ("Personages kunnen tegenover elkaar staan.", J)],
          "De schrijver staat buiten het verhaal, de personages staan erin."),
    mk("Je praat over je boek. Wat toont het best dat je erover nagedacht hebt?",
       ["je zegt welk personage je raakte en waarom", "je vertelt de volledige verhaallijn van begin tot einde na", "je zegt hoeveel bladzijden het boek telt en wanneer het verscheen", "je zegt dat het boek mooi was en dat iedereen het moet lezen"],
       0, "Er wordt gevraagd wat je ervan vond en waarom, niet enkel wat er gebeurt."),
    inv("Hoe noem je het personage rond wie een verhaal vooral draait? Eén woord.", ["hoofdpersonage", "het hoofdpersonage"], "Het hoofdpersonage."),
    keuze("Een verhaal dat zich op één avond afspeelt, beslaat [[*een korte tijd|een lange tijd|geen tijd]].", "Tijd gaat ook over hoeveel tijd het verhaal beslaat."),
    sorteer("Gaat deze vraag over de personages, de ruimte of de tijd?", ["personages", "ruimte", "tijd"],
            [("Wie helpt het hoofdpersonage?", "personages"), ("In welke eeuw speelt het verhaal?", "tijd"), ("Hoe ziet het huis eruit waar alles gebeurt?", "ruimte"), ("Wie verandert er het meest?", "personages"), ("Speelt het in een stad of op het platteland?", "ruimte"), ("Hoeveel jaren beslaat het verhaal?", "tijd")],
            "Wie, waar en wanneer."),
    tabel("Is dit een onderbouwde mening over een boek?",
          [("Het boek sprak me niet aan, omdat de personages vlak bleven.", J), ("Het boek is slecht.", F), ("Het einde vond ik sterk, want het liet me lang nadenken.", J), ("Iedereen vindt het een topboek.", F)],
          "Een mening over een boek mag negatief zijn, zolang je zegt waarom."),
    mk("Waarom is de tijd waarin een verhaal speelt belangrijk?",
       ["ze bepaalt wat de personages kunnen en mogen doen", "ze zegt hoe lang de schrijver aan het boek gewerkt heeft", "ze is enkel belangrijk bij non-fictie zoals geschiedenisboeken", "ze vertelt in welk jaar je het boek moet lezen voor school"],
       0, "Een verhaal in de middeleeuwen kent geen gsm's; de tijd zet grenzen."),
    keuze("Zeggen wat een boek met jou deed, noem je je [[*beleving|samenvatting|verhaallijn]].", "Dat kan niemand nakijken, maar je moet het wel uitleggen."),
    sleep("Het verhaal speelt in een berghut in de Alpen: dat is de [[ruimte]]. Het beslaat één sneeuwstorm van drie dagen: dat is de [[tijd]]. Drie vrienden zitten er vast: dat zijn de [[personages]]. Ze maken ruzie, verzoenen zich en worden gered: dat is de [[verhaallijn]].",
          ["boodschap", "bijsluiter"],
          "Ruimte en tijd zetten het verhaal ergens neer; de verhaallijn is wat er gebeurt."),
    keuze("Een reisverslag over een tocht door IJsland waarin de schrijver ook vertelt wat hij voelde, blijft [[*non-fictie|fictie|een gedicht]].", "De reis is echt gebeurd; gevoelens maken het nog niet verzonnen."),
    mk("Welke vraag helpt je om de boodschap van een verhaal te vinden?",
       ["wat wil de tekst me laten inzien over mensen?", "hoeveel hoofdstukken en bladzijden telt het boek in totaal?", "in welk jaar werd de schrijver geboren?", "welke kleur heeft de kaft van het boek?"],
       0, "De boodschap staat er zelden letterlijk; je leidt ze af uit wat er gebeurt."),
    keuze("Je herkent jezelf in een personage. Dat wordt pas interessant als je zegt [[*in welke situatie en waarom|hoe oud de schrijver is|hoeveel het boek kostte]].", "Herkenning met een voorbeeld erbij zegt iets over jou en over het boek."),
    open_("Kies een boek, film of strip die je kent. Beschrijf in drie zinnen het hoofdpersonage, de ruimte en de tijd.",
          "Het hoofdpersonage is een meisje van twaalf dat haar broer zoekt. Het verhaal speelt in een grote stad aan de kust. Het beslaat één week in de zomervakantie."),
]

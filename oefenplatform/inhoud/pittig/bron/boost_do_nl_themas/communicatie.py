"""Zender, ruis en de zeven tekstsoorten — pittig (🚀 Boost doorstroom, Nederlands).

Eigen vragen en korte teksten strikt binnen nl_communicatie, met een
zelfgetekend communicatiemodel zonder woorden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

CM = Prent("communicatiemodel-leeg", "Het communicatiemodel zonder woorden", "een groot kader met links een persoon, rechts een persoon, een envelop op een pijl ertussen en een wolk met krabbels boven de pijl, met letters A tot E")
CM.rect(40, 60, 920, 520, "#fbf7ee", DONKER, 24, 3)          # context
CM.cirkel(170, 250, 45, "#f6d6b8", DONKER, 3); CM.pad("M 100 420 Q 170 300 240 420 Z", "#9cc0e0", DONKER, 3)   # persoon links
CM.cirkel(830, 250, 45, "#f6d6b8", DONKER, 3); CM.pad("M 760 420 Q 830 300 900 420 Z", "#e0b49c", DONKER, 3)  # persoon rechts
CM.pijl(270, 340, 730, 340, DONKER, 6)                          # kanaal
CM.rect(445, 300, 110, 75, "white", DONKER, 6, 3); CM.lijn(445, 300, 500, 345, DONKER, 3); CM.lijn(555, 300, 500, 345, DONKER, 3)   # envelop
CM.pad("M 400 200 Q 420 150 470 165 Q 500 130 545 160 Q 600 150 600 200 Q 610 240 560 235 Q 520 255 480 235 Q 420 250 400 200 Z", "#e6e6e6", DONKER, 3)
CM.pad("M 440 200 l 15 -15 l 15 20 l 15 -20 l 15 20 l 15 -20 l 15 20 l 15 -15", "none", ROOD, 3)   # ruis
LET = {"A": (170, 480), "B": (830, 480), "C": (500, 420), "D": (640, 190), "E": (110, 110)}
for t, (x, y) in LET.items():
    CM.letter(x, y, t)
U = "communicatiemodel-leeg.svg"
Z = {t: Prent.rond(x, y, 34) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Klik op de letter bij de zender.", U, [Z["A"]],
         "De pijl vertrekt bij de zender en gaat naar de ontvanger."),
    klik("Klik op de letter bij de ontvanger.", U, [Z["B"]],
         "De boodschap komt aan bij de ontvanger."),
    klik("Klik op de letter bij wat de boodschap onderweg stoort.", U, [Z["D"]],
         "Ruis is elke storing die maakt dat de boodschap niet of verkeerd aankomt."),
    klik("Het grote kader rond alles staat voor de situatie: de plaats, het moment, de relatie. Klik op de letter bij dat element.", U, [Z["E"]],
         "Dat is de context."),
    koppel("Koppel het element van het communicatiemodel aan het voorbeeld. Situatie: de directeur mailt alle ouders dat de school morgen dicht is door een storm.",
           [("zender", "de directeur"), ("ontvanger", "de ouders"), ("kanaal", "de mail"), ("context", "de storm die eraan komt")],
           ["het rijmschema"],
           "Een rijmschema hoort bij poëzie."),
    sorteer("Interne of externe ruis?", ["interne ruis", "externe ruis"],
            [("je bent met je gedachten bij je voetbalmatch", "interne ruis"), ("de bouwwerf naast de klas", "externe ruis"), ("je kent het onderwerp helemaal niet", "interne ruis"), ("het beeld van je videogesprek bevriest", "externe ruis"), ("je hebt hoofdpijn", "interne ruis")],
            "Interne ruis zit in de zender of de ontvanger zelf."),
    casus("De stad hangt overal affiches op: 'Fiets veilig: draag een helm!' Een maand later blijkt dat jongeren de affiche vooral delen omdat de foto er grappig uitziet. Bijna niemand draagt meer een helm.", [
        keuze("Wat de stad wou bereiken, een helm laten dragen, is het [[*doel|effect|kanaal]].", "Het doel is wat de zender wil bereiken."),
        keuze("Dat jongeren de affiche vooral grappig vinden, is het [[*effect|doel|context]].", "Het effect is wat er werkelijk gebeurt."),
        mk("Wat besluit je?",
           ["het effect wijkt af van het doel", "doel en effect vallen hier netjes samen", "de affiche heeft eigenlijk geen zender", "het kanaal is hier de helm zelf"],
           0, "Doel en effect lopen uit elkaar."),
        keuze("Naar het doel is deze affiche een [[*persuasieve|narratieve|literaire]] tekst.", "Ze wil je gedrag beïnvloeden."),
    ]),
    mk("Je vertelt een vriend over je nieuwe job via een spraakbericht en daarna nog eens in een mail. Wat blijft gelijk?",
       ["zender, boodschap en ontvanger", "enkel het kanaal blijft hetzelfde", "het kanaal en de ontvanger samen", "niets, want alles verandert mee"],
       0, "Enkel de weg, het kanaal, verandert."),
    mk("'Doe de deur dicht.' Waarom klinkt die zin anders van je vriend dan van de directeur?",
       ["de context is anders", "het kanaal is anders", "de boodschap is langer", "er is meer externe ruis"],
       0, "De relatie tussen zender en ontvanger hoort bij de context."),
    tabel("Klopt dit over het communicatiemodel?",
          [("Ruis kan ook in de ontvanger zelf zitten.", J), ("Doel en effect zijn altijd hetzelfde.", F), ("Een bericht zonder zender is minder betrouwbaar.", J), ("Bij reclame zijn de acteurs de zender.", F)],
          "Bij reclame is de adverteerder de zender."),
    sorteer("Welke tekstsoort is deze tekst: informatief, prescriptief of narratief?", ["informatief", "prescriptief", "narratief"],
            [("een krantenartikel over de nieuwe tramlijn", "informatief"), ("een handleiding van een printer", "prescriptief"), ("een vlog over een reis door Portugal", "narratief"), ("het schoolreglement", "prescriptief"), ("een interview met een dokter", "informatief")],
            "Prescriptief schrijft voor hoe je iets doet."),
    sorteer("Welke tekstsoort is deze tekst: persuasief, opiniërend of argumentatief?", ["persuasief", "opiniërend", "argumentatief"],
            [("een reclamespot voor een energiedrank", "persuasief"), ("een filmrecensie met vier sterren", "opiniërend"), ("een betoog over gratis openbaar vervoer", "argumentatief"), ("een folder van een partij voor de verkiezingen", "persuasief"), ("een productreview van een gsm", "opiniërend")],
            "Een argumentatieve tekst bouwt het standpunt op met argumenten."),
    casus("Lees de tekst.\n\n'Ben jij die jongere die elke ochtend moe opstaat? Dan heb je Vitaboost nodig! Eén blikje en je knalt de dag door. Alle toppers drinken het. Nu in promo: twee halen, één betalen!'", [
        mk("Wat is het hoofddoel van de zender?",
           ["je het drankje laten kopen", "je uitleggen hoe energie werkt", "je een spannend verhaal vertellen", "zijn eerlijke oordeel over drankjes geven"],
           0, "Het is reclame."),
        keuze("Deze tekst is [[*persuasief|argumentatief|prescriptief]].", "Hij wil beïnvloeden, zonder sterke argumenten."),
        mk("Waarom is dit geen argumentatieve tekst?",
           ["hij beïnvloedt zonder redenering", "er staat geen enkel woord in hoofdletters in", "hij is veel te kort om een betoog te zijn", "er staat geen datum of plaats bij de reclame"],
           0, "Argumentatieve teksten leunen op de redenering zelf."),
    ]),
    mk("Een artikel in een tijdschrift prijst een nieuwe sportdrank en onderaan staat klein 'in samenwerking met Hydrafit'. Wat is dit?",
       ["een publireportage", "een informatief artikel", "een recensie", "een narratieve tekst"],
       0, "Betaalde reclame in de vorm van een artikel."),
    mk("Een satirische nieuwssite schrijft dat de minister op Mars gaat wonen. Waarom is dat geen informatieve tekst?",
       ["het doel is je te laten lachen", "er staat helemaal geen auteur bij", "het gaat over de ruimte en Mars", "satire is altijd een prescriptieve tekst"],
       0, "Je kijkt naar het doel van de zender."),
    tabel("Klopt dit over de tekstsoorten?",
          [("Een strip kan literair zijn.", J), ("Eén tekst hoort altijd bij maar één tekstsoort.", F), ("Een recept is prescriptief.", J), ("Een pleidooi is narratief.", F)],
          "Een pleidooi is argumentatief. Bij gemengde teksten kijk je naar het hoofddoel."),
    koppel("Koppel het woord aan zijn oorsprong.",
           [("persuasief", "overtuigen"), ("narratief", "vertellen"), ("prescriptief", "voorschrijven")],
           ["oordelen in de krant"],
           "Persuadere is overtuigen, narrare is vertellen."),
    mk("Twee leerlingen schrijven over de nieuwe schoolbel. Lena schrijft: 'Die bel is vreselijk, echt niet om aan te horen.' Aya schrijft: 'De bel moet weg: ze stoort de lessen ernaast, ze schrikt jonge kinderen af en een zachtere bel kost maar twintig euro.' Wat klopt?",
       ["Aya bouwt haar oordeel op met argumenten", "Lena's tekst heeft helemaal geen standpunt", "Aya's tekst geeft helemaal geen mening", "Lena's tekst is een literaire tekst"],
       0, "Allebei hebben ze een standpunt."),
    keuze("Literaire teksten hebben een [[*esthetische|voorschrijvende|zakelijke]] waarde en spelen in op emoties.", "Een gedicht of een kortverhaal is literair."),
    casus("Lees de tekst.\n\n'Zet de bloem, het zout en de gist in een kom. Voeg langzaam 300 ml lauw water toe. Kneed tien minuten. Laat het deeg een uur rijzen.'", [
        keuze("Deze tekst is [[*prescriptief|narratief|opiniërend]].", "Hij schrijft voor wat je in welke volgorde doet."),
        mk("Wat is het doel van de zender?",
           ["je stap voor stap iets leren doen", "je overtuigen om brood te kopen", "je oordeel over brood vragen", "je vertellen wat hij gisteren deed"],
           0, "Wie instructies geeft, wil dat je daarna zelf iets kan."),
    ]),
    tabel("Welke vragen stel je als je het communicatiemodel op een tekst toepast?",
          [("Wie is de zender?", J), ("Voor wie is de tekst bedoeld?", J), ("Hoeveel strofen telt de tekst?", F), ("Wat wil de zender bereiken?", J)],
          "Het aantal strofen hoort bij de vorm."),
    inv("Hoe noem je met één woord de drager waarlangs een boodschap gaat, zoals een mail of een telefoon?", ["kanaal", "het kanaal"], "Het kanaal."),
    keuze("Een bericht op een forum helemaal in hoofdletters komt meestal over als [[*schreeuwerig|vriendelijk|zakelijk]].", "Hoofdletters worden gelezen als roepen."),
    open_("Leg met een eigen voorbeeld uit wat het verschil is tussen interne en externe ruis.",
          "Interne ruis zit in de zender of de ontvanger zelf, bijvoorbeeld als je moe bent en maar de helft hoort. Externe ruis komt van buitenaf, zoals lawaai van een bouwwerf tijdens een gesprek."),
]

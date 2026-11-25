"""Feit en mening, stelling, argument en conclusie — pittig (Boost dubbele finaliteit, Nederlands).

Strikt binnen nldf_argumenteren: feit en mening, stelling, standpunt, argument,
tegenargument, conclusie, zelf argumenteren en een gesprek voeren. Geen
drogredenen en geen soorten argumentatie, die staan enkel bij doorstroom."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from ..boost_do_nl_themas import argumenteren as _do

BRIEF = ("Lees de brief.\n\n"
         "Geachte schepen van jeugd\n\n"
         "Ik schrijf u omdat het jeugdhuis in onze gemeente op vrijdag om 22 uur sluit. Volgens mij moet het tot middernacht open blijven. "
         "Ten eerste hebben jongeren dan een veilige plek om af te spreken. Uit een bevraging van de jeugdraad blijkt bovendien dat 140 jongeren dat willen. "
         "Sommige buren vrezen lawaai. Daarom stellen wij voor dat de muziek na 22 uur binnen blijft. "
         "Kortom: een langere openingstijd is goed voor de jongeren en haalbaar voor de buurt.\n\n"
         "Met vriendelijke groeten\nLina, leerlingenraad")

VRAGEN = _do.BASIS + [
    _do.VRAGEN[len(_do.BASIS) + 7],  # Maakt dit een argument sterker?
    casus(BRIEF, [
        tabel("Feit of mening in deze brief?",
              [("Het jeugdhuis sluit op vrijdag om 22 uur.", "feit"), ("Volgens mij moet het tot middernacht open blijven.", "mening"), ("Volgens de bevraging willen 140 jongeren dat.", "feit"), ("Een langere openingstijd is goed voor de jongeren.", "mening")],
              "Het uur en de uitkomst van de bevraging kan je nagaan.", ["feit", "mening"]),
        keuze("Het standpunt van Lina is [[*voor een langere openingstijd|tegen een langere openingstijd|nog niet bepaald]].", "Ze kiest duidelijk een kant."),
        keuze("'Sommige buren vrezen lawaai' is een [[*tegenargument|conclusie|stelling]].", "Lina noemt het bezwaar en geeft er meteen een antwoord op."),
        keuze("'Kortom' kondigt [[*de conclusie|een nieuw argument|een tegenargument]] aan.", "Het slot vat samen wat uit de argumenten volgt."),
        mk("Welk register gebruikt Lina in haar brief?",
           ["formeel, met u en een nette groet", "informeel, met jij en een paar emoji's", "spreektaal, zoals in een chat met vrienden", "dialect, omdat de schepen uit dezelfde gemeente komt"],
           0, "Aan een onbekende volwassene schrijf je formeel."),
    ]),
    sorteer("Stelling, argument of conclusie?", ["stelling", "argument", "conclusie"],
            [("De school moet elke middag soep aanbieden.", "stelling"), ("want warme soep is gezond", "argument"), ("omdat leerlingen na een warme maaltijd beter opletten", "argument"), ("Soep op school is dus een goed idee.", "conclusie")],
            "Na 'want' en 'omdat' komt een reden, na 'dus' het besluit."),
    tabel("Is dit een echt argument bij de stelling 'De speelplaats moet meer groen krijgen'?",
          [("want bomen geven schaduw op warme dagen", J), ("want ik vind dat er meer groen moet komen", F), ("want planten houden de lucht frisser", J), ("want de directeur rijdt met een blauwe auto", F)],
          "Een argument geeft een reden die echt met de stelling te maken heeft, en herhaalt het standpunt niet."),
    volgorde("Zet de zinnen van dit opiniestuk in een logische volgorde.",
             ["Ik vind dat de bib ook op zondag open moet.", "Ten eerste hebben veel leerlingen dan tijd om te studeren.", "Ten tweede is het thuis vaak te druk om te leren.", "Een zondagsopening is dus een goede zaak."],
             "Eerst de stelling, dan de argumenten, dan de conclusie."),
    keuze("In een gesprek over een maatschappelijk thema reageer je best [[*respectvol en oplossingsgericht|zo luid mogelijk|enkel met je eigen ervaring]].", "Het doel is samen verder raken, niet winnen."),
    tabel("Hoort dit bij een goed gesprek over een maatschappelijk thema?",
          [("ingaan op wat de ander zegt", J), ("de ander onderbreken als je het oneens bent", F), ("je standpunt bijstellen als een argument klopt", J), ("enkel je eigen argumenten blijven herhalen", F)],
          "Luisteren en erop ingaan maken een gesprek sterker."),
    mk("Iemand zegt: 'Een autovrije zondag is slecht voor de winkels.' Welke reactie is oplossingsgericht?",
       ["Mogen de winkels die dag dan buiten een markt houden?", "Dat is onzin, want winkels zijn helemaal niet belangrijk voor een stad.", "Jij denkt ook altijd alleen maar aan geld, dat weet toch iedereen.", "Dan houden we dit gesprek beter meteen op, want zo komen we nergens."],
       0, "Je erkent het bezwaar en zoekt iets waar allebei mee verder kunnen."),
    keuze("Wie in een gesprek eerst kort herhaalt wat de ander zei, toont dat hij [[*goed geluisterd heeft|het met alles eens is|het gesprek wil afronden]].", "Herhalen is geen toegeven; het toont respect en voorkomt misverstanden."),
    inv("Welk signaalwoord past op de puntjes? 'De speelplaats moet groener, ... bomen geven schaduw.' Eén woord.", ["want", "omdat"], "Want of omdat kondigt een reden aan."),
    mk("Stelling: 'Jongeren moeten gratis met de bus kunnen.' Welk argument kan je nagaan?",
       ["in onze klas komen twaalf van de twintig leerlingen met de bus", "bussen zijn gewoon superleuk", "ik vind dat iedereen dat eigenlijk zou moeten verdienen, zeker jongeren", "het zou echt geweldig zijn voor de hele wereld en voor iedereen"],
       0, "Een aantal in je eigen klas kan je tellen; de andere zinnen zijn meningen."),
    tabel("Klopt dit over een conclusie?",
          [("Een conclusie volgt uit de argumenten.", J), ("Een conclusie is hetzelfde als een samenvatting.", F), ("Signaalwoorden als 'dus' en 'kortom' kondigen vaak de conclusie aan.", J), ("In de conclusie zet je je sterkste nieuwe argument.", F)],
          "Een conclusie trekt de lijn door en brengt niets nieuws meer aan."),
    keuze("'Ik heb zelf al twee keer bijna een ongeval gehad op dat kruispunt.' Dat argument komt uit [[*eigen ervaring|een onderzoek|een krantenbericht]].", "Het mag, en het maakt je tekst levendig."),
    mk("Waarom is één eigen ervaring alleen een zwak argument?",
       ["ze zegt nog niets over de meeste mensen", "eigen ervaringen zijn eigenlijk altijd gelogen", "je mag nooit 'ik' schrijven in een opiniestuk aan de gemeente", "een ervaring telt in een tekst altijd als tegenargument"],
       0, "Eén geval is geen regel; een cijfer of een bron erbij maakt het sterker."),
    sleep("De gemeente moet meer fietspaden aanleggen, [[want]] veel leerlingen fietsen naar school. [[Bovendien]] is fietsen goed voor het milieu. Sommigen vinden fietspaden te duur. [[Maar]] een fietspad kost veel minder dan een nieuwe weg. [[Kortom]], fietspaden zijn een goede keuze.",
          ["Hoewel", "Tenzij"],
          "Want geeft een reden, bovendien voegt iets toe, maar draait de richting om en kortom besluit."),
    open_("Je praat met een klasgenoot over de stelling 'Huiswerk moet afgeschaft worden.' Hij zegt dat hij 's avonds te moe is om nog te leren. Jij bent het oneens. Schrijf in twee zinnen hoe je respectvol en oplossingsgericht reageert.",
          "Ik snap dat je 's avonds moe bent, dat herken ik. Misschien kunnen we voorstellen dat er minder huiswerk komt, maar dat je een deel op school in een studie-uur mag maken?"),
]

# -*- coding: utf-8 -*-
"""Uitdaging Engels ✨ Spark (11 november 2026), in de vormen van het examen van
de Examencommissie: 30 vragen die alle hoofdstukken door elkaar halen, met een
casus (een uitnodiging per mail), een tabel, keuzelijsten, slepen, koppelen,
sorteren, volgorde, twee klikvragen op een zelf getekende prent en een open
schrijfopdracht. Geen nieuwe leerstof: alles staat in de leerbundels van
Engels Spark. Invulantwoorden zijn één woord dat maar op één manier kan.
De prenten tekent inhoud/uitdaging/maak_prenten_spark_engels.py.
"""
NIVEAU = "spark"
VAK = "Engels"
BESTAND = "spark-engels-uitdaging.json"
AANTAL = 30
J, F = True, False
MAP = "/examenvormen/engels-spark"


def mk(vraag, opties, plaats, uitleg):
    """opties[0] is het juiste antwoord; plaats is waar het komt te staan."""
    rest = list(opties[1:])
    rest.insert(plaats, opties[0])
    return {"type": "meerkeuze", "vraag": vraag, "opties": rest, "antwoord": plaats, "uitleg": uitleg}


def iv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def wn(vraag, antwoord, uitleg):
    return {"type": "waarofniet", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg):
    return {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}


def keuze(vraag, uitleg):
    return {"type": "keuzelijst", "vraag": vraag, "uitleg": uitleg}


def volgorde(vraag, stappen, uitleg):
    return {"type": "volgorde", "vraag": vraag, "opties": stappen, "uitleg": uitleg}


def koppel(vraag, paren, extra, uitleg):
    return {"type": "koppelen", "vraag": vraag, "paren": paren, "extra": extra, "uitleg": uitleg}


def sorteer(vraag, kolommen, items, uitleg):
    return {"type": "sorteren", "vraag": vraag, "kolommen": kolommen, "items": items, "uitleg": uitleg}


def sleep(vraag, extra, uitleg):
    return {"type": "sleepzin", "vraag": vraag, "extra": extra, "uitleg": uitleg}


def klik(vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"{MAP}/{prent}", "zones": zones, "uitleg": uitleg}


def open_(vraag, voorbeeld, uitleg=None):
    v = {"type": "open", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def casus(tekst, vragen):
    return {"casus": tekst, "vragen": vragen}


VRAGEN = [
    casus("Lees de mail. 'Hi Emma, I'm having a party for my twelfth birthday on Saturday 14 June. It starts at half past two in the afternoon and finishes at six. We are going to play games in the garden, so bring some old clothes! My house is at 12 Park Road, next to the library. Could you please let me know before Wednesday if you can come? Bye, Lily'",
          [mk("Hoe laat begint het feest?",
              ["om half drie 's middags", "om half twee 's middags", "om twee uur 's middags", "om zes uur 's avonds"], 1,
              "Half past two is half drie: dertig minuten na twee uur. Om zes uur (six) is het feest gedaan."),
           mk("Waarom moet Emma oude kleren meebrengen?",
              ["Ze gaan spelletjes spelen in de tuin.", "Het wordt een verkleedfeest met thema.",
               "Ze gaan samen een muur schilderen.", "Het gaat de hele dag regenen."], 2,
              "Lily schrijft: we are going to play games in the garden, so bring some old clothes. So geeft het gevolg aan."),
           tabel("Lees elke uitspraak over de mail. Is ze juist of fout?",
                 [("Lily wordt twaalf jaar.", J),
                  ("Het feest is op een zondag.", F),
                  ("Lily woont naast de bibliotheek.", J),
                  ("Emma moet vóór woensdag laten weten of ze komt.", J),
                  ("Het is een formele mail.", F)],
                 "Twelfth birthday is de twaalfde verjaardag. Saturday is zaterdag. A library is een bibliotheek. Hi en Bye maken de mail informeel."),
           keuze("Lily begint haar mail met [[*Hi Emma|Dear Mrs Smith]] en sluit af met [[*Bye|Kind regards]]. Dat maakt het een [[*informele|formele]] mail. Met [[*Could you please|You must]] vraagt ze iets op een beleefde manier.",
                 "Hi en Bye zijn informeel, Dear Mr of Mrs en Kind regards zijn neutraal. Could you please is de beleefde vorm.")]),
    klik("Klik op de klok die twenty to nine aanwijst.", "vier-klokken.svg", [[51, 2, 23, 96]],
         "Twenty to nine is twintig minuten vóór negen uur, dus 8.40 uur. To is ervoor, past is erover. Klok C staat op 8.40 uur."),
    klik("Een Brit zegt: 'My flat is on the first floor.' Klik op die verdieping.", "gebouw-verdiepingen.svg", [[20, 56, 60, 20]],
         "In het Brits Engels is de first floor de eerste verdieping, één trap hoger dan de begane grond (ground floor). In Amerika is first floor net de begane grond."),
    mk("Welke vraag over de piano is juist?",
       ["Does she play the piano?", "Does she plays the piano?", "Do she play the piano?", "Does she play piano the?"], 2,
       "In een vraag verhuist de -s van she naar does. Daarna blijft het werkwoord kaal: does she play."),
    keuze("The film was very [[*boring|bored]], so I was [[*bored|boring]] after ten minutes.",
          "Een film is boring (saai). Jij bent bored: je verveelt je."),
    sleep("Yesterday I [[went]] to the shop and [[bought]] some bread. I [[saw]] my teacher there.",
          ["goed", "buyed", "seen"],
          "Yesterday vraagt de past simple: go–went, buy–bought, see–saw. Buyed en goed bestaan niet, en seen gebruik je niet zonder have."),
    koppel("Koppel elk signaalwoord aan wat het aangeeft.",
           [["first", "een volgorde"], ["because", "een oorzaak"], ["so", "een gevolg"], ["however", "een tegenstelling"]],
           ["een voorbeeld"],
           "First – then – finally geeft een volgorde, because een oorzaak, so een gevolg, but en however een tegenstelling."),
    sorteer("Kan je dit tellen of niet? Sleep elk woord naar de juiste kolom.",
            ["Telbaar", "Ontelbaar"],
            [["apple", "Telbaar"], ["chair", "Telbaar"], ["sandwich", "Telbaar"], ["book", "Telbaar"],
             ["bread", "Ontelbaar"], ["water", "Ontelbaar"], ["rice", "Ontelbaar"], ["advice", "Ontelbaar"]],
           "Bread, water, rice en advice tel je niet: je zegt two slices of bread, nooit two breads. Een appel, stoel, boterham of boek tel je wel."),
    volgorde("Zet de delen van een nette mail aan een leerkracht in de juiste volgorde.",
             ["Dear Mr Jones,", "Een inleiding: waarom je schrijft", "Het middenstuk met je vraag", "Kind regards,", "Je naam"],
             "Aanhef, inleiding, midden, slotgroet en dan je naam. Dear Mr Jones en Kind regards zijn de neutrale vormen."),
    iv("Vul aan met één Engels woord: 'My aunt's son is my ...'", "cousin",
       "Het kind van je tante of oom is je cousin. Dat woord geldt voor een neef én voor een nicht."),
    iv("Zet in het meervoud met één Engels woord: one knife, two ...", "knives",
       "Bij knife wordt de f een v: knife – knives."),
    iv("Vul a of an in: '... hour'", "an",
       "A of an hangt af van de klank. De h van hour hoor je niet, dus begint het met een klinkerklank: an hour."),
    mk("In New York zegt het weerbericht dat het 86 graden is. Hoe komt dat?",
       ["De VS meten de temperatuur in Fahrenheit.", "In New York is het bijna altijd heel heet.",
        "In de VS tellen ze de afstand in miles.", "Het weerbericht meet de temperatuur in de zon."], 3,
       "De VS meten in Fahrenheit en in miles. 86 graden Fahrenheit is een warme zomerdag, geen kokend water."),
    wn("In het Verenigd Koninkrijk en in Ierland rijden de auto's links.", J,
       "In het VK en in Ierland rijden ze links, in de VS rechts zoals bij ons."),
    wn("Een Amerikaan die chips bestelt, krijgt frieten.", F,
       "In Amerika zijn chips de chips uit een zakje. In Groot-Brittannië zijn chips frieten."),
    mk("Met welk voorvoegsel maak je possible ontkennend?",
       ["im-", "un-", "dis-", "in-"], 1,
       "Possible wordt impossible. Un-, im- en dis- ontkennen allemaal een woord, maar elk woord heeft zijn eigen voorvoegsel."),
    mk("Wat is a return ticket?",
       ["een kaartje heen en terug", "een kaartje voor enkele reis", "een kaartje dat je terugbetaald krijgt", "een kaartje voor de terugreis alleen"], 2,
       "A return ticket is heen en terug. A single ticket is enkele reis."),
    wn("In 'The dog wags it's tail' staat it's juist geschreven.", F,
       "It's betekent it is. Van hem of van haar is its, zonder apostrof: the dog wags its tail."),
    mk("Welke zin over een boek is juist?",
       ["This book is mine.", "This is mine book.", "This book is my.", "These book is mine."], 3,
       "Voor een naamwoord staat my (my book), alleen staat mine (it is mine). Bij één boek hoort this, niet these."),
    mk("Welke zin over twee fietsen is juist?",
       ["My bike is better than yours.", "My bike is more better than yours.", "My bike is gooder than yours.", "My bike is more good than yours."], 0,
       "Good wordt better, en dan zet je er nooit nog more voor."),
    wn("Je zegt 'I play the piano', maar 'I play tennis' zonder the.", J,
       "Bij een muziekinstrument zet je the, bij een sport niet."),
    iv("Hoe zeg je 12 uur 's nachts in het Engels? Antwoord met één woord.", "midnight",
       "Middernacht is midnight. Twaalf uur 's middags is noon."),
    mk("Welke zin vertelt wat er nu op dit moment bezig is?",
       ["Look! It is raining.", "It rains a lot in Belgium.", "It rained yesterday.", "It will rain tomorrow."], 1,
       "Iets dat nu bezig is, zet je in de present continuous: it is raining. It rains a lot is een gewoonte."),
    wn("Afraid gebruik je met of: 'I am afraid of spiders.'", J,
       "Je zegt altijd afraid of, nooit afraid from."),
    mk("Lees: 'Tom has a little dog. It sleeps in the kitchen.' Naar wie of wat verwijst it?",
       ["naar de hond", "naar Tom", "naar de keuken", "naar het bed"], 0,
       "Een verwijswoord wijst naar het dichtstbijzijnde passende woord ervóór: a little dog."),
    wn("'He goes to school by foot' is juist Engels.", F,
       "Met de fiets, de auto of de trein is by bike, by car, by train. Te voet is on foot."),
    open_("Schrijf een korte uitnodiging in het Engels (twee of drie zinnen) voor een filmavond bij jou thuis. Zeg wanneer, waar en waarvoor.",
          "Hi Sam, would you like to come to a film night at my house on Friday at seven o'clock? I live at 5 Station Street. Let me know if you can come! Bye, Noor",
          "Een uitnodiging zegt wanneer, waar en waarvoor. Would you like…? is de beleefde manier om iemand uit te nodigen."),
]
